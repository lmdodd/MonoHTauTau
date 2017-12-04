#include "PhysicsTools/FWLite/interface/CommandLineParser.h" 
#include "TFile.h"
#include "TROOT.h"
#include "TKey.h"
#include "TTree.h"
#include "TLorentzVector.h"
#include "TH1F.h"
#include <iostream>


using std::cout;
using std::endl;


void readdir(TDirectory *dir,optutl::CommandLineParser parser,  char TreeToUse[]);


int main (int argc, char* argv[]) 
{
    optutl::CommandLineParser parser ("Sets Event Weights in the ntuple");

    char TreeToUse[80]="first" ;

    parser.addOption("isWJets",optutl::CommandLineParser::kDouble,"isWJets",0.0);
    parser.parseArguments (argc, argv);

    std::cout << "EXTRA COMMANDS:"
        << "\n --- isWJets: " << parser.doubleValue("isWJets")
        << std::endl;


    TFile *f = new TFile(parser.stringValue("outputFile").c_str(),"UPDATE");   

    readdir(f,parser, TreeToUse);

    f->Close();

} 

double calcMt1(TLorentzVector l, TLorentzVector met){
    double px = l.Px() + met.Px();
    double py = l.Py() + met.Py();
    double et = l.Et() + TMath::Sqrt(met.Px()*met.Px() + met.Py()*met.Py());
    double mt2 = et*et - (px*px + py*py);
    return  TMath::Sqrt(mt2);
}

double calcMttot(TLorentzVector l1, TLorentzVector l2, TLorentzVector met){
    double px = l1.Px() + l2.Px() + met.Px();
    double py = l1.Py() + l2.Py() + met.Py();
    double et = l1.Et() + l2.Et() +  TMath::Sqrt(met.Px()*met.Px() + met.Py()*met.Py());
    double mt2 = et*et - (px*px + py*py);
    return  TMath::Sqrt(mt2);
}
double calcMVis(TLorentzVector l1, TLorentzVector l2){
    double m = (l1+l2).M();
    return m; 
}

double calcPTH(TLorentzVector l1, TLorentzVector l2){
    double m = (l1+l2).Pt();
    return m; 
}

void readdir(TDirectory *dir,optutl::CommandLineParser parser,char TreeToUse[])
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
            TDirectory *subdir = gDirectory;
            sprintf(TreeToUse,"%s",key->GetName());
            readdir(subdir,parser, TreeToUse);
            dirsav->cd();
        }
        else if(obj->IsA()->InheritsFrom(TTree::Class())) {

            float metcorr_ex = -10; // corrected met px (float)
            float metcorr_ey = -10;  // corrected met py (float)

            float metcorr_ex_UP = -10; // corrected met px (float)
            float metcorr_ey_UP = -10;  // corrected met py (float)
            float metcorr_ex_DOWN = -10; // corrected met px (float)
            float metcorr_ey_DOWN = -10;  // corrected met py (float)


            float mtTot=0.0;
            float mtTotUp=0.0;
            float mtTotDown=0.0;


            float metREDO=0.0;
            float metREDOUp=0.0;
            float metREDODown=0.0;

            float mvis=0.0;
            float mvisUp=0.0;
            float mvisDown=0.0;

            float lepptREDO=0.0;
            float lepptREDOUp=0.0;
            float lepptREDODown=0.0;

            float pthREDO=0.0;
            float pthREDOUp=0.0;
            float pthREDODown=0.0;


            //Other
            float pdgid=0.0;
            float lpt=0.0;
            float lptUp=0.0;
            float lptDown=0.0;
            float leta=0.0;
            float lphi=0.0;
            float lM=0.0;

            float taupt=0.0;
            float tauM=0.0;
            float taueta=0.0;
            float tauphi=0.0;

            float pfmet=0.0;
            float pfmetphi=0.0;

            TTree *t = (TTree*)obj;

            TBranch *newBranch1 = t->Branch("pfmt_LREDO",&mtTot,"pfmt_LREDO/F");
            TBranch *newBranch2 = t->Branch("pfmt_LUP",&mtTotUp,"pfmt_LUP/F");
            TBranch *newBranch3 = t->Branch("pfmt_LDOWN",&mtTotDown,"pfmt_LDOWN/F");

            TBranch *newBranch4 = t->Branch("mvis_LREDO",&mvis,"mvis_LREDO/F");
            TBranch *newBranch5 = t->Branch("mvis_LUP",&mvisUp,"mvis_LUP/F");
            TBranch *newBranch6 = t->Branch("mvis_LDOWN",&mvisDown,"mvis_LDOWN/F");

            TBranch *newBranch7 = t->Branch("metREDO_LREDO",&metREDO,"metREDO_LREDO/F");
            TBranch *newBranch8 = t->Branch("metREDO_LUP",&metREDOUp,"metREDO_LUP/F");
            TBranch *newBranch9 = t->Branch("metREDO_LDOWN",&metREDODown,"metREDO_LDOWN/F");

            //ADD PTH, MVIS
            TBranch *newBranch10 = t->Branch("lepptREDO_LREDO",&lepptREDO,"lepptREDO_LREDO/F");
            TBranch *newBranch11 = t->Branch("lepptREDO_LUP",&lepptREDOUp,"lepptREDO_LUP/F");
            TBranch *newBranch12 = t->Branch("lepptREDO_LDOWN",&lepptREDODown,"lepptREDO_LDOWN/F");

            TBranch *newBranch16 = t->Branch("pthREDO_LREDO",&pthREDO,"pthREDO_LREDO/F");
            TBranch *newBranch17 = t->Branch("pthREDO_LUP",&pthREDOUp,"pthREDO_LUP/F");
            TBranch *newBranch18 = t->Branch("pthREDO_LDOWN",&pthREDODown,"pthREDO_LDOWN/F");


            t->SetBranchAddress("pfmet",&pfmet);
            t->SetBranchAddress("pfmetphi",&pfmetphi);

            t->SetBranchAddress("pt_2",&taupt);
            t->SetBranchAddress("eta_2",&taueta);
            t->SetBranchAddress("phi_2",&tauphi);
            t->SetBranchAddress("m_2",&tauM);

            t->SetBranchAddress("pt_1",&lpt);
            t->SetBranchAddress("m_1",&lM);
            t->SetBranchAddress("eta_1",&leta);
            t->SetBranchAddress("phi_1",&lphi);
            t->SetBranchAddress("pdg1",&pdgid);


            printf("Found tree -> weighting\n");
            std::cout<<"KeyName "<<keyname<<" or key->GetName() "<<key->GetName()<<std::endl;


            for(Int_t i=0;i<t->GetEntries();++i)
            {
                t->GetEntry(i);


                mtTot=0.0;
                mtTotUp=0.0;
                mtTotDown=0.0;

                metREDO=0.0;
                metREDOUp=0.0;
                metREDODown=0.0;

                mvis=0.0;
                mvisUp=0.0;
                mvisDown=0.0;

                lepptREDO=0.0;
                lepptREDOUp=0.0;
                lepptREDODown=0.0;

                pthREDO=0.0;
                pthREDOUp=0.0;
                pthREDODown=0.0;

                float scale = 1.0; 

                if(std::string(TreeToUse).find("muTauEvent")!= std::string::npos){
                    lM=0.00051100;
                    scale = 0.002;
                }
                else if(std::string(TreeToUse).find("eleTauEvent")!= std::string::npos){
                    lM=0.105658;

                    if (fabs(leta>1.479))
                        scale=0.025;
                    else
                        scale=0.01;
                }

                lptUp=lpt*(1+scale);
                lptDown=lpt*(1-scale);

                TLorentzVector l,lup,ldown,tau,tauup,taudown,met, metup,metdown;

                l.SetPtEtaPhiM(lpt,leta,lphi,lM); 
                tau.SetPtEtaPhiM(taupt,taueta,tauphi,tauM);

                lup.SetPtEtaPhiM(lptUp,leta,lphi,lM); 
                ldown.SetPtEtaPhiM(lptDown,leta,lphi,lM); 

                tauup = tau;
                taudown =tau;

                float dxUp= (tau-tauup+l-lup).Px();
                float dxDown= (tau-taudown+l-ldown).Px();
                float dyUp= (tau-tauup+l-lup).Py();
                float dyDown= (tau-taudown+l-ldown).Py();

                //std::cout<<"DeltaTau px: "<<dx<<"DeltaTau py: "<<dy<<std::endl;

                metcorr_ex = pfmet*TMath::Cos(pfmetphi);
                metcorr_ey = pfmet*TMath::Sin(pfmetphi);

                metcorr_ex_UP = metcorr_ex-dxUp; 
                metcorr_ey_UP = metcorr_ey-dyUp;
                metcorr_ex_DOWN = metcorr_ex-dxDown; 
                metcorr_ey_DOWN = metcorr_ey-dyDown;


                float metcor = TMath::Sqrt( metcorr_ex*metcorr_ex + metcorr_ey*metcorr_ey);

                float metcorUP = TMath::Sqrt( metcorr_ex_UP*metcorr_ex_UP + metcorr_ey_UP*metcorr_ey_UP);
                float metcorDOWN = TMath::Sqrt( metcorr_ex_DOWN*metcorr_ex_DOWN + metcorr_ey_DOWN*metcorr_ey_DOWN);
                float metcorphi = TMath::ATan2(metcorr_ey,metcorr_ex);
                float metcorphiUp = TMath::ATan2(metcorr_ey_UP,metcorr_ex_UP);
                float metcorphiDown = TMath::ATan2(metcorr_ey_DOWN,metcorr_ex_DOWN);

                met.SetPtEtaPhiM(metcor,0,metcorphi,0);
                metup.SetPtEtaPhiM(metcorUP,0,metcorphiUp,0);
                metdown.SetPtEtaPhiM(metcorDOWN,0,metcorphiDown,0);

                metREDO=metcor;
                metREDOUp=metcorUP;
                metREDODown=metcorDOWN;

                pthREDO=calcPTH(l,tau);
                pthREDOUp=calcPTH(lup,tauup);
                pthREDODown=calcPTH(ldown,taudown);

                lepptREDO=l.Pt();
                lepptREDOUp=lup.Pt();
                lepptREDODown=ldown.Pt();

                //mvis= calcMVis(l,tau);
                mtTot=calcMttot(l,tau,met);
                mtTotUp=calcMttot(lup,tauup,metup);
                mtTotDown=calcMttot(ldown,taudown,metdown);

                mvis=calcMVis(l,tau);
                mvisUp=calcMVis(lup,tauup);
                mvisDown=calcMVis(ldown,taudown);

                newBranch1->Fill();
                newBranch2->Fill();
                newBranch3->Fill();

                newBranch4->Fill();
                newBranch5->Fill();
                newBranch6->Fill();

                newBranch7->Fill();
                newBranch8->Fill();
                newBranch9->Fill();

                newBranch10->Fill();
                newBranch11->Fill();
                newBranch12->Fill();

                newBranch16->Fill();
                newBranch17->Fill();
                newBranch18->Fill();



            }
            dir->cd();
            t->Write("",TObject::kOverwrite);

        }//end else if object A
    }//end while key
}//end read directory
