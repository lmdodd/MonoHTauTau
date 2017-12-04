#include "PhysicsTools/FWLite/interface/CommandLineParser.h" 
#include "TFile.h"
#include "TROOT.h"
#include "TKey.h"
#include "TTree.h"
#include "TH1F.h"
#include "TH2F.h"
#include "TH2D.h"
#include "TF1.h"
#include <math.h> 
#include "TMath.h" 
#include <limits>
#include "RooWorkspace.h"
#include "RooRealVar.h"


void readdir(TDirectory *dir,optutl::CommandLineParser parser,RooWorkspace *w, char TreeToUse[]); 




int main (int argc, char* argv[]) 
{
    optutl::CommandLineParser parser ("Sets Event Weights in the ntuple");
    parser.addOption("branch",optutl::CommandLineParser::kString,"Branch","__QCDIDISO__");
    parser.addOption("branch1",optutl::CommandLineParser::kString,"Branch","__QCDTRIG__");
    parser.addOption("IsoFile",optutl::CommandLineParser::kString,"Iso Hist","htt_scalefactors_sm_moriond_v2.root");
    parser.parseArguments (argc, argv);


    TFile *f = new TFile(parser.stringValue("outputFile").c_str(),"UPDATE");

    char TreeToUse[80]="first" ;


    TFile fIso("htt_scalefactors_sm_moriond_v2.root");
    RooWorkspace *w = (RooWorkspace*)fIso.Get("w");
    fIso.Close();


    readdir(f,parser,w,TreeToUse);
    f->Close();

} 


void readdir(TDirectory *dir, optutl::CommandLineParser parser,RooWorkspace *w, char TreeToUse[]) 
{



    TDirectory *dirsav = gDirectory;
    TIter next(dir->GetListOfKeys());
    TKey *key;
    while ((key = (TKey*)next())) {
        printf("Found key=%s \n",key->GetName());
        TString keyname = key->GetName();

        if (keyname=="CircJetID_puv2"||keyname=="sumweights"){
            printf("Skipping key %s . Not weighting. \n",key->GetName());
            continue;
        }

        TObject *obj = key->ReadObj();

        if (obj->IsA()->InheritsFrom(TDirectory::Class())) {
            dir->cd(key->GetName());
            sprintf(TreeToUse,"%s",key->GetName());
            TDirectory *subdir = gDirectory;
            readdir(subdir,parser,w,TreeToUse);
            dirsav->cd();
        }
        else if(obj->IsA()->InheritsFrom(TTree::Class())) {
            TTree *t = (TTree*)obj;
            float weight = 1.0;
            float weight1 = 1.0;
            float weightUp = 1.0;
            float weightDown = 1.0;
            float weight_redo1 = 1.0;
            float weight_redo2 = 1.0;
            float weight_redo3 = 1.0;
            float weight_tauid = 1.0;
            TBranch *newBranch  = t->Branch(parser.stringValue("branch").c_str(),&weight,(parser.stringValue("branch")+"/F").c_str());
            TBranch *newBranch1  = t->Branch(parser.stringValue("branch1").c_str(),&weight1,(parser.stringValue("branch1")+"/F").c_str());
            TBranch *newBranch2 = t->Branch("fakeTauEffiUp",&weightUp,"fakeTauEffiUp/F");
            TBranch *newBranch3 = t->Branch("fakeTauEffiDown",&weightDown,"fakeTauEffiDown/F");
            TBranch *newBranch4 = t->Branch("idisoweight_REDO",&weight_redo1,"idisoweight_REDO/F");
            TBranch *newBranch5 = t->Branch("trigweight_REDO",&weight_redo2,"trigweight_REDO/F");
            TBranch *newBranch7 = t->Branch("trigweight_Binned",&weight_redo3,"trigweight_Binned/F");
            TBranch *newBranch6 = t->Branch("TAUID1",&weight_tauid,"TAUID1/F");


            std::cout<<"here1"<<std::endl;

            float pt1;
            float tauPt;
            float eta1;
            float eta2;
            float iso1;
            float gen_match;
            float gen_match1;
            float tauDM;
            float tauDM1;

            t->SetBranchAddress("pt_1",&pt1);
            t->SetBranchAddress("pt_2",&tauPt);
            t->SetBranchAddress("eta_1",&eta1);
            t->SetBranchAddress("eta_2",&eta2);
            t->SetBranchAddress("gen_match_2",&gen_match);
            t->SetBranchAddress("gen_match_1",&gen_match1);

            std::cout<<"here2"<<std::endl;

            printf("Found tree -> weighting\n");
            std::cout<<"KeyName "<<keyname<<" or key->GetName() "<<key->GetName()<<std::endl;
            if(std::string(TreeToUse).find("muTauEvent")!= std::string::npos){
                std::cout<<"Using muTau!"<<std::endl;
            }
            else if(std::string(TreeToUse).find("eleTauEvent")!= std::string::npos){
                std::cout<<"Using eleTau!"<<std::endl;
            }


            for(Int_t i=0;i<t->GetEntries();++i)
            {
                t->GetEntry(i);
                weight=1.0;
                weight1=1.0;
                weightUp =1.0;
                weightDown=1.0;
                weight_redo1=1.0;
                weight_redo2=1.0;
                weight_tauid=1.0;
                //printf("Wvar: pt:%f, eta:%f, iso:%f \n",pt1,eta1,iso1);
                if(std::string(TreeToUse).find("muTauEvent")!= std::string::npos){
                    t->SetBranchAddress("tauDecayMode",&tauDM);
                    t->SetBranchAddress("iso_1",&iso1);
                    w->var("m_pt")->setVal(pt1);
                    w->var("m_eta")->setVal(eta1);
                    w->var("t_pt")->setVal(tauPt);
                    w->var("t_eta")->setVal(eta2);
                    w->var("t_dm")->setVal(tauDM);

                    weight=w->function("m_idiso_aiso0p15to0p3_desy_ratio")->getVal();
                    weight_redo1 = w->function("m_idiso0p15_desy_ratio")->getVal();

                    if (pt1>23){
                        weight_redo2 = w->function("m_trgMu22OR_eta2p1_desy_ratio")->getVal();
                        weight1 = w->function("m_trgMu22OR_eta2p1_aiso0p15to0p3_desy_ratio")->getVal();
                    }
                    else{
                        weight_redo2 = w->function("t_genuine_TightIso_mt_ratio")->getVal()*w->function("m_trgMu19leg_eta2p1_desy_ratio")->getVal();
                        weight1 = w->function("t_genuine_TightIso_mt_ratio")->getVal()*w->function("m_trgMu19leg_eta2p1_aiso0p15to0p3_desy_ratio")->getVal();
                    }


                    if (gen_match==1||gen_match==3){
                        if (std::abs(eta2)<1.460)  weight_tauid=1.213;
                        else if (std::abs(eta2)>1.558)  weight_tauid=1.375;
                    }
                    else if (gen_match==2||gen_match==4){
                        if (std::abs(eta2)<0.4)  weight_tauid=1.263;
                        else if (std::abs(eta2)<0.8)  weight_tauid=1.364;
                        else if (std::abs(eta2)<1.2)  weight_tauid=0.854;
                        else if (std::abs(eta2)<1.7)  weight_tauid=1.712;
                        else if (std::abs(eta2)<2.3)  weight_tauid=2.324;
                    }
                    else if(gen_match==5){
                        weight_tauid*=0.94;
                    }
                    else if(gen_match==6){
                        if (tauPt>200)tauPt=200.;

                        float w = 1.22493-0.00444605*tauPt+0.0000104656*tauPt*tauPt;
                        weightUp = w;
                        weightDown = 1/w;
                    }

                }
                else if(std::string(TreeToUse).find("eleTauEvent")!= std::string::npos){
                    t->SetBranchAddress("tauDecayMode",&tauDM);
                    t->SetBranchAddress("iso_1",&iso1);
                    w->var("e_pt")->setVal(pt1);
                    w->var("e_eta")->setVal(eta1);


                    weight= w->function("e_idiso_aiso0p1to0p3_desy_ratio")->getVal();
                    weight1 = w->function("e_trgEle25eta2p1WPTight_aiso0p1to0p3_desy_data")->getVal();
                    //printf("Ele function: id:%f,  trig:%f \n", ele_id_scalefactor, weight1);

                    weight_redo1 = w->function("e_idiso0p1_desy_ratio")->getVal();
                    weight_redo2 = w->function("e_trgEle25eta2p1WPTight_desy_ratio")->getVal();
                    //printf("Ele function: id:%f,  trig:%f \n", weight_redo1, weight_redo2);

                    if (gen_match==1||gen_match==3){
                        if (std::abs(eta2)<1.460)  weight_tauid=1.402;
                        else if (std::abs(eta2)>1.558)  weight_tauid=1.9;
                    }
                    else if (gen_match==2||gen_match==4){
                        if (std::abs(eta2)<0.4)  weight_tauid=1.012;
                        else if (std::abs(eta2)<0.8)  weight_tauid=1.007;
                        else if (std::abs(eta2)<1.2)  weight_tauid=0.870;
                        else if (std::abs(eta2)<1.7)  weight_tauid=1.154;
                        else if (std::abs(eta2)<2.3)  weight_tauid=2.281;
                    }
                    else if(gen_match==5){
                        weight_tauid*=0.94;
                    }
                    else if(gen_match==6){
                        if (tauPt>200)tauPt=200.;

                        float w = 1.22493-0.00444605*tauPt+0.0000104656*tauPt*tauPt;
                        weightUp = w;
                        weightDown = 1/w;
                    }


                }
                else if(std::string(TreeToUse).find("diTauEvent")!= std::string::npos){
                    t->SetBranchAddress("tauDecayMode_1",&tauDM1);
                    t->SetBranchAddress("tauDecayMode_2",&tauDM);
                    w->var("t_pt")->setVal(pt1);
                    //w->var("t_eta")->setVal(eta1);
                    w->var("t_dm")->setVal(tauDM1);

                    float tau1 = w->function("t_binned_genuine_TightIso_tt_ratio")->getVal();
                    //float tau3 = w->function("t_genuine_TightIso_tt_data")->getVal();
                    float tau5 = w->function("t_genuine_TightIso_tt_ratio")->getVal();

                    w->var("t_pt")->setVal(tauPt);
                    //w->var("t_eta")->setVal(eta2);
                    w->var("t_dm")->setVal(tauDM);

                    float tau2 = w->function("t_binned_genuine_TightIso_tt_ratio")->getVal();
                    //float tau4 = w->function("t_genuine_TightIso_tt_data")->getVal();
                    float tau6 = w->function("t_genuine_TightIso_tt_ratio")->getVal();

                    //weight_redo1 = tau3*tau4; //idisoi=Eff Eff is now scale factor uncertinty 
                    weight_redo2 = tau5*tau6; //trig_REDO=normal
                    weight_redo3 = tau1*tau2; //trig binned = binneed

                    if(gen_match==5){
                        weight_tauid*=0.94;
                    }
                    else if(gen_match==6){
                        if (tauPt>200)tauPt=200.;

                        float w = 1.22493-0.00444605*tauPt+0.0000104656*tauPt*tauPt;
                        weightUp = w;
                        weightDown = 1/w;
                    }
                    if(gen_match1==5){
                        weight_tauid*=0.94;
                    }

                    else if(gen_match1==6){
                        if (pt1>200)pt1=200.;

                        float w = 1.22493-0.00444605*pt1+0.0000104656*pt1*pt1;
                        weightUp = w;
                        weightDown = 1/w;
                    }

                    if (pt1<60){
                        weight_redo1 = (60-pt1)/200.0+0.02;
                    }
                    else weight_redo1=0.02;

                    if (tauPt<60){
                        weight_redo1 += (60-tauPt)/200.0+0.02;
                    }
                    else weight_redo1 += 0.02;
                    /*
                       std::cout<<std::endl;
                       std::cout<<"Tau 1 Pt: "<<pt1<<" DM: "<<tauDM1<<" \t Tau 2 Pt "<<tauPt<<" DM: "<<tauDM<<std::endl;
                       std::cout<<"\tEfficiency: "<<weight_redo1<<" leg1: "<<tau3<<"\t leg2: "<<tau4<<std::endl;
                       std::cout<<"\tFit Scale Factor: "<<weight_redo2<<" leg1: "<<tau5<<"\t leg2: "<<tau6<<std::endl;
                       std::cout<<"\tBinned Scale Factor: "<<weight_redo3<<" leg1: "<<tau1<<"\t leg2: "<<tau2<<std::endl;
                       */
                    //loose

                    if (gen_match==1||gen_match==3){
                        if (std::abs(eta2)<1.460)  weight_tauid*=1.213;
                        else if (std::abs(eta2)>1.558)  weight_tauid*=1.375;
                    }
                    else if (gen_match==2||gen_match==4){
                        if (std::abs(eta2)<0.4)  weight_tauid*=1.012;
                        else if (std::abs(eta2)<0.8)  weight_tauid*=1.007;
                        else if (std::abs(eta2)<1.2)  weight_tauid*=0.870;
                        else if (std::abs(eta2)<1.7)  weight_tauid*=1.154;
                        else if (std::abs(eta2)<2.3)  weight_tauid*=2.281;
                    }

                    if (gen_match1==1||gen_match1==3){
                        if (std::abs(eta1)<1.460)  weight_tauid*=1.213;
                        else if (std::abs(eta1)>1.558)  weight_tauid*=1.375;
                    }
                    else if (gen_match1==2||gen_match1==4){
                        if (std::abs(eta1)<0.4)  weight_tauid*=1.012;
                        else if (std::abs(eta1)<0.8)  weight_tauid*=1.007;
                        else if (std::abs(eta1)<1.2)  weight_tauid*=0.870;
                        else if (std::abs(eta1)<1.7)  weight_tauid*=1.154;
                        else if (std::abs(eta1)<2.3)  weight_tauid*=2.281;
                    }


                }
                else{
                    std::cout<<"TreeToUse "<< std::string(TreeToUse)<<" does not match diTauEvent muTauEvent or eleTauEvent... Skipping!!"<<std::endl;
                }
                /*
                   Minimizer is Linear
                   Chi2                      =      6.45499
                   NDf                       =           17
                   p0                        =      1.22493   +/-   0.183521
                   p1                        =  -0.00444605   +/-   0.00513471
                   p2                        =  1.04856e-05   +/-   2.83123e-05
                   */

                newBranch->Fill();
                newBranch1->Fill();
                newBranch2->Fill();
                newBranch3->Fill();
                newBranch4->Fill();
                newBranch5->Fill();
                newBranch6->Fill();
                newBranch7->Fill();


            }

            t->Write("",TObject::kOverwrite);
        }
    }
}
