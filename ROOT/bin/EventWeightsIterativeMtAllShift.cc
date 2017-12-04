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


void readdir(TDirectory *dir,optutl::CommandLineParser parser,  char TreeToUse[], int isWJets);


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

    readdir(f,parser, TreeToUse, parser.doubleValue("isWJets"));

    f->Close();

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
void readdir(TDirectory *dir,optutl::CommandLineParser parser,char TreeToUse[], int isWJets)
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
            readdir(subdir,parser, TreeToUse, parser.doubleValue("isWJets"));
            dirsav->cd();
        }
        else if(obj->IsA()->InheritsFrom(TTree::Class())) {

            float mtTot=0.0;
            float mtTotUp=0.0;
            float mtTotDown=0.0;
            float mtTotCESUP=0.0;
            float mtTotCESDOWN=0.0;
            float mtTotUESUP=0.0;
            float mtTotUESDOWN=0.0;

            float pdgid=0.0;
            float lpt=0.0;
            float leta=0.0;
            float lphi=0.0;
            float lM=0.0;

            float taupt=0.0;
            float tauptCorr=0.0;
            float taueta=0.0;
            float tauphi=0.0;

            float mt;
            float pfmet;
            float pfmetphi;
            float pfmetEnUp;
            float pfmetphiEnUp;
            float pfmetEnDown;
            float pfmetphiEnDown;
            float pfmetJetUp;
            float pfmetphiJetUp;
            float pfmetJetDown;
            float pfmetphiJetDown;

            float tauDM=0.0;
            float tauM=0.0;
            float gen_match=0;


            int njets;
            float  genPx=-999.    , // generator Z/W/Higgs px (float)
                   genPy =-999.   , // generator Z/W/Higgs py (float)
                   visPx =-999.   , // generator visible Z/W/Higgs px (float)
                   visPy =-999.   ;

            float metcorr_ex = -10; // corrected met px (float)
            float metcorr_ey = -10;  // corrected met py (float)

            float metcorr_ex_UESUP = -10; // corrected met px (float)
            float metcorr_ey_UESUP = -10;  // corrected met py (float)

            float metcorr_ex_UESDOWN = -10; // corrected met px (float)
            float metcorr_ey_UESDOWN = -10;  // corrected met py (float)

            float metcorr_ex_CESUP = -10; // corrected met px (float)
            float metcorr_ey_CESUP = -10;  // corrected met py (float)

            float metcorr_ex_CESDOWN = -10; // corrected met px (float)
            float metcorr_ey_CESDOWN = -10;  // corrected met py (float)


            TLorentzVector tauold; 
            TLorentzVector tau; 
            TLorentzVector deltatau; 
            TLorentzVector l; 

            TLorentzVector met; 
            TLorentzVector metuesup; 
            TLorentzVector metuesdown; 
            TLorentzVector metcesup; 
            TLorentzVector metcesdown; 

            TTree *t = (TTree*)obj;

            TBranch *newBranch1 = t->Branch("mtTot",&mtTot,"mtTot_REDO/F");
            TBranch *newBranch1a = t->Branch("mtTot_UP",&mtTotUp,"mtTot_UP/F");
            TBranch *newBranch1b = t->Branch("mtTot_DOWN",&mtTotDown,"mtTot_DOWN/F");
            TBranch *newBranch2 = t->Branch("mtTot_CES_UP",&mtTotCESUP,"mtTot_CES_UP/F");
            TBranch *newBranch3 = t->Branch("mtTot_CES_DOWN",&mtTotCESDOWN,"mtTot_CES_DOWN/F");
            TBranch *newBranch4 = t->Branch("mtTot_UES_UP",&mtTotUESUP,"mtTot_UES_UP/F");
            TBranch *newBranch5 = t->Branch("mtTot_UES_DOWN",&mtTotUESDOWN,"mtTot_UES_DOWN/F");


            t->SetBranchAddress("pt_2",&taupt);
            t->SetBranchAddress("taupt",&tauptCorr);
            t->SetBranchAddress("eta_2",&taueta);
            t->SetBranchAddress("phi_2",&tauphi);
            t->SetBranchAddress("m_2",&tauM);
            t->SetBranchAddress("m_1",&lM);

            t->SetBranchAddress("pt_1",&lpt);
            t->SetBranchAddress("eta_1",&leta);
            t->SetBranchAddress("phi_1",&lphi);
            t->SetBranchAddress("pdg1",&pdgid);

            t->SetBranchAddress("tauDecayMode",&tauDM);
            t->SetBranchAddress("gen_match_2",&gen_match);

            t->SetBranchAddress("njets", &njets);

            t->SetBranchAddress("genpX",&genPx);
            t->SetBranchAddress("genpY",&genPy);
            t->SetBranchAddress("vispX",&visPx);
            t->SetBranchAddress("vispY",&visPy);


            t->SetBranchAddress("mt_1",&mt);
            t->SetBranchAddress("pfmet",&pfmet);
            t->SetBranchAddress("pfmetphi",&pfmetphi);
            t->SetBranchAddress("pfmetEnUp",&pfmetEnUp);
            t->SetBranchAddress("pfmetphiEnUp",&pfmetphiEnUp);
            t->SetBranchAddress("pfmetEnDown",&pfmetEnDown);
            t->SetBranchAddress("pfmetphiEnDown",&pfmetphiEnDown);
            t->SetBranchAddress("pfmetJetUp",&pfmetJetUp);
            t->SetBranchAddress("pfmetphiJetUp",&pfmetphiJetUp);
            t->SetBranchAddress("pfmetJetDown",&pfmetJetDown);
            t->SetBranchAddress("pfmetphiJetDown",&pfmetphiJetDown);

            printf("Found tree -> weighting\n");
            std::cout<<"KeyName "<<keyname<<" or key->GetName() "<<key->GetName()<<std::endl;


            for(Int_t i=0;i<t->GetEntries();++i)
            {
                t->GetEntry(i);

                metcorr_ex = pfmet*TMath::Cos(pfmetphi);
                metcorr_ey = pfmet*TMath::Sin(pfmetphi);
                metcorr_ex_UESUP = pfmetEnUp*TMath::Cos(pfmetphiEnUp);
                metcorr_ey_UESUP = pfmetEnUp*TMath::Sin(pfmetphiEnUp);
                metcorr_ex_UESDOWN = pfmetEnDown*TMath::Cos(pfmetphiEnDown);
                metcorr_ey_UESDOWN = pfmetEnDown*TMath::Sin(pfmetphiEnDown);
                metcorr_ex_CESUP = pfmetJetUp*TMath::Cos(pfmetphiJetUp);
                metcorr_ey_CESUP = pfmetJetUp*TMath::Sin(pfmetphiJetUp);
                metcorr_ex_CESDOWN = pfmetJetDown*TMath::Cos(pfmetphiJetDown);
                metcorr_ey_CESDOWN = pfmetJetDown*TMath::Sin(pfmetphiJetDown);



                mtTot=0;
                mtTotUp=0;
                mtTotDown=0;
                mtTotUESUP=0;
                mtTotUESDOWN=0;
                mtTotCESUP=0;
                mtTotCESDOWN=0;
                lM=0;

                if (abs(pdgid)==11){
                    lM=0.00051100;
                }
                else if (abs(pdgid)==13){ 
                    //std::cout<<"muon mass"<<std::endl;
                    lM=0.105658;
                }

                //if (tauDM==0) newtaupt=taupt*0.995;
                //else if (tauDM==1) newtaupt=taupt*1.011;
                //else if (tauDM==10) newtaupt=taupt*1.006;             


                //std::cout<<"L 4 vector: "<<lpt<<","<<leta<<","<<lphi<<","<<lM <<std::endl;
                //std::cout<<"Tau Orig. 4 vector: "<<taupt<<","<<taueta<<","<<tauphi<<","<<tauM <<std::endl;
                //std::cout<<"Tau New 4 vector: "<<tauptCorr<<","<<taueta<<","<<tauphi<<","<<tauM <<std::endl;
                l.SetPtEtaPhiM(lpt,leta,lphi,lM); 
                tauold.SetPtEtaPhiM(taupt,taueta,tauphi,tauM);
                tau.SetPtEtaPhiM(tauptCorr,taueta,tauphi,tauM);
                deltatau = tau -tauold;

                float dx= deltatau.Px();
                float dy= deltatau.Py();

                //std::cout<<"DeltaTau px: "<<dx<<"DeltaTau py: "<<dy<<std::endl;

                metcorr_ex = metcorr_ex-dx;
                metcorr_ey = metcorr_ey-dy;
                metcorr_ex_UESUP = metcorr_ex_UESUP-dx;
                metcorr_ex_UESDOWN = metcorr_ex_UESDOWN-dx;
                metcorr_ex_CESUP = metcorr_ex_CESUP-dx;
                metcorr_ex_CESDOWN = metcorr_ex_CESDOWN-dx;
                metcorr_ey_UESUP = metcorr_ey_UESUP-dy;
                metcorr_ey_UESDOWN = metcorr_ey_UESDOWN-dy;
                metcorr_ey_CESUP = metcorr_ey_CESUP-dy;
                metcorr_ey_CESDOWN = metcorr_ey_CESDOWN-dy;

                float metcor = TMath::Sqrt( metcorr_ex*metcorr_ex + metcorr_ey*metcorr_ey);

                float metcorUESUP = TMath::Sqrt( metcorr_ex_UESUP*metcorr_ex_UESUP + metcorr_ey_UESUP*metcorr_ey_UESUP);
                float metcorUESDOWN = TMath::Sqrt( metcorr_ex_UESDOWN*metcorr_ex_UESDOWN + metcorr_ey_UESDOWN*metcorr_ey_UESDOWN);
                float metcorCESUP = TMath::Sqrt( metcorr_ex_CESUP*metcorr_ex_CESUP + metcorr_ey_CESUP*metcorr_ey_CESUP);
                float metcorCESDOWN = TMath::Sqrt( metcorr_ex_CESDOWN*metcorr_ex_CESDOWN + metcorr_ey_CESDOWN*metcorr_ey_CESDOWN);

                float metcorphi = TMath::ATan2(metcorr_ey,metcorr_ex);

                float metcorUESUPphi = TMath::ATan2(metcorr_ey_UESUP,metcorr_ex_UESUP);
                float metcorUESDOWNphi =TMath::ATan2(metcorr_ey_UESDOWN,metcorr_ex_UESDOWN);; 
                float metcorCESUPphi = TMath::ATan2(metcorr_ey_CESUP,metcorr_ex_CESUP);
                float metcorCESDOWNphi = TMath::ATan2(metcorr_ey_CESDOWN,metcorr_ex_CESDOWN);

                met.SetPtEtaPhiM(metcor,0,metcorphi,0);

                metuesup.SetPtEtaPhiM(metcorUESUP,0,metcorUESUPphi,0);
                metuesdown.SetPtEtaPhiM(metcorUESDOWN,0,metcorUESDOWNphi,0);
                metcesup.SetPtEtaPhiM(metcorCESUP,0,metcorCESUPphi,0);
                metcesdown.SetPtEtaPhiM(metcorCESDOWN,0,metcorCESDOWNphi,0);

                //double px = l.Px() + met.Px();
                //double py = l.Py() + met.Py();
                //double et = l.Et() + TMath::Sqrt(met.Px()*met.Px() + met.Py()*met.Py());
                //double mt2 = et*et - (px*px + py*py);
                //double othermt =  TMath::Sqrt(mt2);

                //mvis= calcMVis(l,tau);
                mtTot= calcMttot(l,tau,met);
                mtTotUESUP=calcMttot(l,tau,metuesup);
                mtTotUESDOWN=calcMttot(l,tau,metuesdown);
                mtTotCESUP=calcMttot(l,tau,metcesup);
                mtTotCESDOWN=calcMttot(l,tau,metcesdown);

                //std::cout<<" mtRecoil_1: "<<mt<<" \t othermt:"<<othermt<<"\t MtRedo: "<<mtTot<<" \t mtTotUESUp: "<<mtTotUESUP<<" \t mtTotUESDown: "<<mtTotUESDOWN
                //    <<" \t mtTotCESUP: "<<mtTotCESUP<<" \t mtTotCESDOWN: "<<mtTotCESDOWN
                //    <<" \t met: "<<met.Mt()<<" \t pfmet: "<<pfmet<<" \t metcomp: "<<metComp<<std::endl;

                newBranch1->Fill();
                newBranch2->Fill();
                newBranch3->Fill();
                newBranch4->Fill();
                newBranch5->Fill();
            }
            dir->cd();
            t->Write("",TObject::kOverwrite);

        }//end else if object A
    }//end while key
}//end read directory
