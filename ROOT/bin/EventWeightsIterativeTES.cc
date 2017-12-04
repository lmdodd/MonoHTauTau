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

    parser.parseArguments (argc, argv);

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
double calcHyp(double a,double b ){
    return  TMath::Sqrt(a*a +b*b);
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

            float mtTot=0.0;
            float mtTotUp=0.0;
            float mtTotUp0=0.0;
            float mtTotUp1=0.0;
            float mtTotUp10=0.0;
            float mtTotDown=0.0;
            float mtTotDown0=0.0;
            float mtTotDown1=0.0;
            float mtTotDown10=0.0;

            float metREDO=0.0;
            float metREDOUp=0.0;
            float metREDOUp0=0.0;
            float metREDOUp1=0.0;
            float metREDOUp10=0.0;
            float metREDODown=0.0;
            float metREDODown0=0.0;
            float metREDODown1=0.0;
            float metREDODown10=0.0;

            float mvis=0.0;
            float mvisUp=0.0;
            float mvisUp0=0.0;
            float mvisUp1=0.0;
            float mvisUp10=0.0;
            float mvisDown=0.0;
            float mvisDown0=0.0;
            float mvisDown1=0.0;
            float mvisDown10=0.0;

            float tauptREDO=0.0;
            float tauptREDOUp=0.0;
            float tauptREDOUp0=0.0;
            float tauptREDOUp1=0.0;
            float tauptREDOUp10=0.0;
            float tauptREDODown=0.0;
            float tauptREDODown0=0.0;
            float tauptREDODown1=0.0;
            float tauptREDODown10=0.0;

            float taupt2REDO=0.0;
            float taupt2REDOUp=0.0;
            float taupt2REDOUp0=0.0;
            float taupt2REDOUp1=0.0;
            float taupt2REDOUp10=0.0;
            float taupt2REDODown=0.0;
            float taupt2REDODown0=0.0;
            float taupt2REDODown1=0.0;
            float taupt2REDODown10=0.0;

            float pthREDO=0.0;
            float pthREDOUp=0.0;
            float pthREDOUp0=0.0;
            float pthREDOUp1=0.0;
            float pthREDOUp10=0.0;
            float pthREDODown=0.0;
            float pthREDODown0=0.0;
            float pthREDODown1=0.0;
            float pthREDODown10=0.0;


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

            float gen_match_1=-1.0;
            float gen_match_2=-1.0;
            float tauDM=-1.0;
            float tauDM1=-1.0;
            float tauDM2=-1.0;

            float pfmet=0.0;
            float pfmetphi=0.0;

            TTree *t = (TTree*)obj;

            TBranch *newBranch1 = t->Branch("pfmt_REDO",&mtTot,"pfmt_REDO/F");
            TBranch *newBranch2 = t->Branch("pfmt_UP",&mtTotUp,"pfmt_UP/F");
            TBranch *newBranch2a = t->Branch("pfmt_UP0",&mtTotUp0,"pfmt_UP0/F");
            TBranch *newBranch2b = t->Branch("pfmt_UP1",&mtTotUp1,"pfmt_UP1/F");
            TBranch *newBranch2c = t->Branch("pfmt_UP10",&mtTotUp10,"pfmt_UP10/F");
            TBranch *newBranch3 = t->Branch("pfmt_DOWN",&mtTotDown,"pfmt_DOWN/F");
            TBranch *newBranch3a = t->Branch("pfmt_DOWN0",&mtTotDown0,"pfmt_DOWN0/F");
            TBranch *newBranch3b = t->Branch("pfmt_DOWN1",&mtTotDown1,"pfmt_DOWN1/F");
            TBranch *newBranch3c = t->Branch("pfmt_DOWN10",&mtTotDown10,"pfmt_DOWN10/F");

            TBranch *newBranch4 = t->Branch("mvis_REDO",&mvis,"mvis_REDO/F");
            TBranch *newBranch5 = t->Branch("mvis_UP",&mvisUp,"mvis_UP/F");
            TBranch *newBranch5a = t->Branch("mvis_UP0",&mvisUp0,"mvis_UP0/F");
            TBranch *newBranch5b = t->Branch("mvis_UP1",&mvisUp1,"mvis_UP1/F");
            TBranch *newBranch5c = t->Branch("mvis_UP10",&mvisUp10,"mvis_UP10/F");
            TBranch *newBranch6 = t->Branch("mvis_DOWN",&mvisDown,"mvis_DOWN/F");
            TBranch *newBranch6a = t->Branch("mvis_DOWN0",&mvisDown0,"mvis_DOWN0/F");
            TBranch *newBranch6b = t->Branch("mvis_DOWN1",&mvisDown1,"mvis_DOWN1/F");
            TBranch *newBranch6c = t->Branch("mvis_DOWN10",&mvisDown10,"mvis_DOWN10/F");

            TBranch *newBranch7 = t->Branch("metREDO_REDO",&metREDO,"metREDO_REDO/F");
            TBranch *newBranch8 = t->Branch("metREDO_UP",&metREDOUp,"metREDO_UP/F");
            TBranch *newBranch8a = t->Branch("metREDO_UP0",&metREDOUp0,"metREDO_UP0/F");
            TBranch *newBranch8b = t->Branch("metREDO_UP1",&metREDOUp1,"metREDO_UP1/F");
            TBranch *newBranch8c = t->Branch("metREDO_UP10",&metREDOUp10,"metREDO_UP10/F");
            TBranch *newBranch9 = t->Branch("metREDO_DOWN",&metREDODown,"metREDO_DOWN/F");
            TBranch *newBranch9a = t->Branch("metREDO_DOWN0",&metREDODown0,"metREDO_DOWN0/F");
            TBranch *newBranch9b = t->Branch("metREDO_DOWN1",&metREDODown1,"metREDO_DOWN1/F");
            TBranch *newBranch9c = t->Branch("metREDO_DOWN10",&metREDODown10,"metREDO_DOWN10/F");

            //ADD PTH, MVIS
            TBranch *newBranch10 = t->Branch("tauptREDO_REDO",&tauptREDO,"tauptREDO_REDO/F");
            TBranch *newBranch11 = t->Branch("tauptREDO_UP",&tauptREDOUp,"tauptREDO_UP/F");
            TBranch *newBranch11a = t->Branch("tauptREDO_UP0",&tauptREDOUp0,"tauptREDO_UP0/F");
            TBranch *newBranch11b = t->Branch("tauptREDO_UP1",&tauptREDOUp1,"tauptREDO_UP1/F");
            TBranch *newBranch11c = t->Branch("tauptREDO_UP10",&tauptREDOUp10,"tauptREDO_UP10/F");
            TBranch *newBranch12 = t->Branch("tauptREDO_DOWN",&tauptREDODown,"tauptREDO_DOWN/F");
            TBranch *newBranch12a = t->Branch("tauptREDO_DOWN0",&tauptREDODown0,"tauptREDO_DOWN0/F");
            TBranch *newBranch12b = t->Branch("tauptREDO_DOWN1",&tauptREDODown1,"tauptREDO_DOWN1/F");
            TBranch *newBranch12c = t->Branch("tauptREDO_DOWN10",&tauptREDODown10,"tauptREDO_DOWN10/F");

            TBranch *newBranch13 = t->Branch("taupt2REDO_REDO",&taupt2REDO,"taupt2REDO_REDO/F");
            TBranch *newBranch14 = t->Branch("taupt2REDO_UP",&taupt2REDOUp,"taupt2REDO_UP/F");
            TBranch *newBranch14a = t->Branch("taupt2REDO_UP0",&taupt2REDOUp0,"taupt2REDO_UP0/F");
            TBranch *newBranch14b = t->Branch("taupt2REDO_UP1",&taupt2REDOUp1,"taupt2REDO_UP1/F");
            TBranch *newBranch14c = t->Branch("taupt2REDO_UP10",&taupt2REDOUp10,"taupt2REDO_UP10/F");
            TBranch *newBranch15 = t->Branch("taupt2REDO_DOWN",&taupt2REDODown,"taupt2REDO_DOWN/F");
            TBranch *newBranch15a = t->Branch("taupt2REDO_DOWN0",&taupt2REDODown0,"taupt2REDO_DOWN0/F");
            TBranch *newBranch15b = t->Branch("taupt2REDO_DOWN1",&taupt2REDODown1,"taupt2REDO_DOWN1/F");
            TBranch *newBranch15c = t->Branch("taupt2REDO_DOWN10",&taupt2REDODown10,"taupt2REDO_DOWN10/F");

            TBranch *newBranch16 = t->Branch("pthREDO_REDO",&pthREDO,"pthREDO_REDO/F");
            TBranch *newBranch17 = t->Branch("pthREDO_UP",&pthREDOUp,"pthREDO_UP/F");
            TBranch *newBranch17a = t->Branch("pthREDO_UP0",&pthREDOUp0,"pthREDO_UP0/F");
            TBranch *newBranch17b = t->Branch("pthREDO_UP1",&pthREDOUp1,"pthREDO_UP1/F");
            TBranch *newBranch17c = t->Branch("pthREDO_UP10",&pthREDOUp10,"pthREDO_UP10/F");
            TBranch *newBranch18 = t->Branch("pthREDO_DOWN",&pthREDODown,"pthREDO_DOWN/F");
            TBranch *newBranch18a = t->Branch("pthREDO_DOWN0",&pthREDODown0,"pthREDO_DOWN0/F");
            TBranch *newBranch18b = t->Branch("pthREDO_DOWN1",&pthREDODown1,"pthREDO_DOWN1/F");
            TBranch *newBranch18c = t->Branch("pthREDO_DOWN10",&pthREDODown10,"pthREDO_DOWN10/F");


            t->SetBranchAddress("gen_match_1",&gen_match_1);
            t->SetBranchAddress("gen_match_2",&gen_match_2);

            t->SetBranchAddress("pfmet",&pfmet);
            t->SetBranchAddress("pfmetphi",&pfmetphi);

            t->SetBranchAddress("pt_2",&taupt);
            t->SetBranchAddress("eta_2",&taueta);
            t->SetBranchAddress("phi_2",&tauphi);
            t->SetBranchAddress("m_2",&tauM);

            std::cout<<"Printing TreeToUse: "<<TreeToUse<<std::endl; 
            t->SetBranchAddress("tauDecayMode_2",&tauDM2);
            t->SetBranchAddress("tauDecayMode",&tauDM);
            t->SetBranchAddress("tauDecayMode_1",&tauDM1);

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
                mtTotUp0=0.0;
                mtTotUp1=0.0;
                mtTotUp10=0.0;
                mtTotDown=0.0;
                mtTotDown0=0.0;
                mtTotDown1=0.0;
                mtTotDown10=0.0;

                metREDO=0.0;
                metREDOUp=0.0;
                metREDOUp0=0.0;
                metREDOUp1=0.0;
                metREDOUp10=0.0;
                metREDODown=0.0;
                metREDODown0=0.0;
                metREDODown1=0.0;
                metREDODown10=0.0;

                mvis=0.0;
                mvisUp=0.0;
                mvisUp0=0.0;
                mvisUp1=0.0;
                mvisUp10=0.0;
                mvisDown=0.0;
                mvisDown0=0.0;
                mvisDown1=0.0;
                mvisDown10=0.0;

                tauptREDO=0.0;
                tauptREDOUp=0.0;
                tauptREDOUp0=0.0;
                tauptREDOUp1=0.0;
                tauptREDOUp10=0.0;
                tauptREDODown=0.0;
                tauptREDODown0=0.0;
                tauptREDODown1=0.0;
                tauptREDODown10=0.0;

                taupt2REDO=0.0;
                taupt2REDOUp=0.0;
                taupt2REDOUp0=0.0;
                taupt2REDOUp1=0.0;
                taupt2REDOUp10=0.0;
                taupt2REDODown=0.0;
                taupt2REDODown0=0.0;
                taupt2REDODown1=0.0;
                taupt2REDODown10=0.0;

                pthREDO=0.0;
                pthREDOUp=0.0;
                pthREDOUp0=0.0;
                pthREDOUp1=0.0;
                pthREDOUp10=0.0;
                pthREDODown=0.0;
                pthREDODown0=0.0;
                pthREDODown1=0.0;
                pthREDODown10=0.0;


                TLorentzVector l,lup,ldown,tau,tauup,taudown,met, metup,metdown;
                TLorentzVector lup0,ldown0,tauup0,taudown0,metup0,metdown0;
                TLorentzVector lup1,ldown1,tauup1,taudown1,metup1,metdown1;
                TLorentzVector lup10,ldown10,tauup10,taudown10,metup10,metdown10;
                TLorentzVector lold,tauold;

                //SET THE LEPTON MASS, NOT IN TREE
                if(std::string(TreeToUse).find("muTauEvent")!= std::string::npos){
                    lM=0.00051100;
                }
                else if(std::string(TreeToUse).find("eleTauEvent")!= std::string::npos){
                    lM=0.105658;
                }

                //SET THE OLD FOUR VECTORS BEFORE NOMINAL SCALING 
                tauold.SetPtEtaPhiM(taupt,taueta,tauphi,tauM);
                lold.SetPtEtaPhiM(lpt,leta,lphi,lM); 

                //SHIFT THE NOMINAL TAUS 
                //Only shift gen_match_5 
                //Do not shift the pi0 mass 
                if(std::string(TreeToUse).find("muTauEvent")!= std::string::npos || std::string(TreeToUse).find("eleTauEvent")!= std::string::npos){
                    if (gen_match_2==5){
                        if (tauDM==0){
                            taupt=taupt*0.995;
                        }
                        else if (tauDM==1) {
                            taupt=taupt*1.011;
                            tauM = tauM *1.011;
                        }
                        else if (tauDM==10) {
                            taupt=taupt*1.006;             
                            tauM = tauM *1.006;
                        }
                    }
                }
                else if(std::string(TreeToUse).find("diTauEvent")!= std::string::npos){

                    if (gen_match_1==5){
                        if (tauDM1==0) lpt=lpt*0.995;
                        else if (tauDM1==1) 
                        {
                            lpt=lpt*1.011;
                            lM=lM*1.011;
                        }
                        else if (tauDM1==10)
                        {
                            lpt=lpt*1.006;             
                            lM=lM*1.006;             
                        }
                    }
                    if (gen_match_2==5){
                        if (tauDM2==0) taupt=taupt*0.995;
                        else if (tauDM2==1){
                            taupt=taupt*1.011;
                            tauM=tauM*1.011;
                        }
                        else if (tauDM2==10){
                            taupt=taupt*1.006;             
                            tauM=tauM*1.006;             
                        }
                    }
                }

                //THESE ARE SCALED NOMINAL VECTORS
                tau.SetPtEtaPhiM(taupt,taueta,tauphi,tauM);
                l.SetPtEtaPhiM(lpt,leta,lphi,lM); 

                float dx= (tauold-tau+lold-l).Px();
                float dy= (tauold-tau+lold-l).Py();

                float met_ex = pfmet*TMath::Cos(pfmetphi);
                float met_ey = pfmet*TMath::Sin(pfmetphi);
                metcorr_ex= met_ex-dx; //shifted new nominal met
                metcorr_ey = met_ey-dy; //shifted new nominal met


                if(std::string(TreeToUse).find("muTauEvent")!= std::string::npos || std::string(TreeToUse).find("eleTauEvent")!= std::string::npos){
                    lptUp=lpt;
                    lptDown=lpt;
                    lup.SetPtEtaPhiM(lptUp,leta,lphi,lM); 
                    lup0.SetPtEtaPhiM(lptUp,leta,lphi,lM); 
                    lup1.SetPtEtaPhiM(lptUp,leta,lphi,lM); 
                    lup10.SetPtEtaPhiM(lptUp,leta,lphi,lM); 
                    ldown.SetPtEtaPhiM(lptDown,leta,lphi,lM); 
                    ldown0.SetPtEtaPhiM(lptDown,leta,lphi,lM); 
                    ldown1.SetPtEtaPhiM(lptDown,leta,lphi,lM); 
                    ldown10.SetPtEtaPhiM(lptDown,leta,lphi,lM); 

                    if (gen_match_2==5){
                        if(tauDM==0){
                            tauup.SetPtEtaPhiM(taupt*1.012,taueta,tauphi,tauM);
                            taudown.SetPtEtaPhiM(taupt*0.988,taueta,tauphi,tauM);

                            tauup0.SetPtEtaPhiM(taupt*1.012,taueta,tauphi,tauM);
                            taudown0.SetPtEtaPhiM(taupt*0.988,taueta,tauphi,tauM);

                            //Other DM no shift
                            tauup1.SetPtEtaPhiM(taupt,taueta,tauphi,tauM);
                            tauup10.SetPtEtaPhiM(taupt,taueta,tauphi,tauM);
                            taudown1.SetPtEtaPhiM(taupt,taueta,tauphi,tauM);
                            taudown10.SetPtEtaPhiM(taupt,taueta,tauphi,tauM);

                        }
                        else if (tauDM==1){
                            tauup.SetPtEtaPhiM(taupt*1.012,taueta,tauphi,tauM*1.012);
                            tauup1.SetPtEtaPhiM(taupt*1.012,taueta,tauphi,tauM*1.012);
                            taudown.SetPtEtaPhiM(taupt*0.988,taueta,tauphi,tauM*0.988);
                            taudown1.SetPtEtaPhiM(taupt*0.988,taueta,tauphi,tauM*0.988);

                            //Other DM no shift
                            tauup0.SetPtEtaPhiM(taupt,taueta,tauphi,tauM);
                            taudown0.SetPtEtaPhiM(taupt,taueta,tauphi,tauM);
                            tauup10.SetPtEtaPhiM(taupt,taueta,tauphi,tauM);
                            taudown10.SetPtEtaPhiM(taupt,taueta,tauphi,tauM);
                        }
                        else{
                            tauup.SetPtEtaPhiM(taupt*1.012,taueta,tauphi,tauM*1.012);
                            tauup10.SetPtEtaPhiM(taupt*1.012,taueta,tauphi,tauM*1.012);
                            taudown.SetPtEtaPhiM(taupt*0.988,taueta,tauphi,tauM*0.988);
                            taudown10.SetPtEtaPhiM(taupt*0.988,taueta,tauphi,tauM*0.988);

                            //Other DM no shift
                            tauup0.SetPtEtaPhiM(taupt,taueta,tauphi,tauM);
                            taudown0.SetPtEtaPhiM(taupt,taueta,tauphi,tauM);
                            tauup1.SetPtEtaPhiM(taupt,taueta,tauphi,tauM);
                            taudown1.SetPtEtaPhiM(taupt,taueta,tauphi,tauM);

                        }

                    }//only shift true taus
                    else{
                        tauup.SetPtEtaPhiM(taupt,taueta,tauphi,tauM);
                        tauup0.SetPtEtaPhiM(taupt,taueta,tauphi,tauM);
                        tauup1.SetPtEtaPhiM(taupt,taueta,tauphi,tauM);
                        tauup10.SetPtEtaPhiM(taupt,taueta,tauphi,tauM);
                        taudown.SetPtEtaPhiM(taupt,taueta,tauphi,tauM);
                        taudown0.SetPtEtaPhiM(taupt,taueta,tauphi,tauM);
                        taudown1.SetPtEtaPhiM(taupt,taueta,tauphi,tauM);
                        taudown10.SetPtEtaPhiM(taupt,taueta,tauphi,tauM);
                    }//other shapes are bogus, unchanged

                }
                else if(std::string(TreeToUse).find("diTauEvent")!= std::string::npos){

                    if (gen_match_2==5){
                        if (tauDM2==0){
                            tauup.SetPtEtaPhiM(taupt*1.012,taueta,tauphi,tauM);
                            taudown.SetPtEtaPhiM(taupt*0.988,taueta,tauphi,tauM);
                            tauup0.SetPtEtaPhiM(taupt*1.012,taueta,tauphi,tauM);
                            taudown0.SetPtEtaPhiM(taupt*0.988,taueta,tauphi,tauM);

                            //Other DM no shift
                            tauup1.SetPtEtaPhiM(taupt,taueta,tauphi,tauM);
                            tauup10.SetPtEtaPhiM(taupt,taueta,tauphi,tauM);
                            taudown1.SetPtEtaPhiM(taupt,taueta,tauphi,tauM);
                            taudown10.SetPtEtaPhiM(taupt,taueta,tauphi,tauM);
                        }
                        else if (tauDM2==1){
                            tauup.SetPtEtaPhiM(taupt*1.012,taueta,tauphi,tauM*1.012);
                            tauup1.SetPtEtaPhiM(taupt*1.012,taueta,tauphi,tauM*1.012);
                            taudown.SetPtEtaPhiM(taupt*0.988,taueta,tauphi,tauM*0.988);
                            taudown1.SetPtEtaPhiM(taupt*0.988,taueta,tauphi,tauM*0.988);

                            //Other DM no shift
                            tauup0.SetPtEtaPhiM(taupt,taueta,tauphi,tauM);
                            tauup10.SetPtEtaPhiM(taupt,taueta,tauphi,tauM);
                            taudown0.SetPtEtaPhiM(taupt,taueta,tauphi,tauM);
                            taudown10.SetPtEtaPhiM(taupt,taueta,tauphi,tauM);
                        }
                        else{
                            tauup.SetPtEtaPhiM(taupt*1.012,taueta,tauphi,tauM*1.012);
                            tauup10.SetPtEtaPhiM(taupt*1.012,taueta,tauphi,tauM*1.012);
                            taudown.SetPtEtaPhiM(taupt*0.988,taueta,tauphi,tauM*0.988);
                            taudown10.SetPtEtaPhiM(taupt*0.988,taueta,tauphi,tauM*0.988);

                            //Other DM no shift
                            tauup0.SetPtEtaPhiM(taupt,taueta,tauphi,tauM);
                            tauup1.SetPtEtaPhiM(taupt,taueta,tauphi,tauM);
                            taudown0.SetPtEtaPhiM(taupt,taueta,tauphi,tauM);
                            taudown1.SetPtEtaPhiM(taupt,taueta,tauphi,tauM);
 
                        }
                    }
                    else{//FILL extra up and down shifts as no change
                        tauup.SetPtEtaPhiM(taupt,taueta,tauphi,tauM);
                        tauup0.SetPtEtaPhiM(taupt,taueta,tauphi,tauM);
                        tauup1.SetPtEtaPhiM(taupt,taueta,tauphi,tauM);
                        tauup10.SetPtEtaPhiM(taupt,taueta,tauphi,tauM);
                        taudown.SetPtEtaPhiM(taupt,taueta,tauphi,tauM);
                        taudown0.SetPtEtaPhiM(taupt,taueta,tauphi,tauM);
                        taudown1.SetPtEtaPhiM(taupt,taueta,tauphi,tauM);
                        taudown10.SetPtEtaPhiM(taupt,taueta,tauphi,tauM);
                    }

                    if (gen_match_1==5){
                        if (tauDM1==0){
                            lup.SetPtEtaPhiM(lpt*1.012,leta,lphi,lM); 
                            lup0.SetPtEtaPhiM(lpt*1.012,leta,lphi,lM); 
                            ldown.SetPtEtaPhiM(lpt*0.988,leta,lphi,lM); 
//Other DM No shift
                            lup0.SetPtEtaPhiM(lpt,leta,lphi,lM); 
                            lup1.SetPtEtaPhiM(lpt,leta,lphi,lM); 
                            lup10.SetPtEtaPhiM(lpt,leta,lphi,lM); 
                            ldown0.SetPtEtaPhiM(lpt,leta,lphi,lM); 
                            ldown1.SetPtEtaPhiM(lpt,leta,lphi,lM); 
                            ldown10.SetPtEtaPhiM(lpt,leta,lphi,lM); 

                            ldown0.SetPtEtaPhiM(lpt*0.988,leta,lphi,lM); 
                        }
                        else if(tauDM1==1) {
                            lup.SetPtEtaPhiM(lpt*1.012,leta,lphi,lM*1.012); 
                            lup1.SetPtEtaPhiM(lpt*1.012,leta,lphi,lM*1.012); 
                            ldown.SetPtEtaPhiM(lpt*0.988,leta,lphi,lM*0.988); 
                            ldown1.SetPtEtaPhiM(lpt*0.988,leta,lphi,lM*0.988); 
//Other DM No shift
                            lup0.SetPtEtaPhiM(lpt,leta,lphi,lM); 
                            lup1.SetPtEtaPhiM(lpt,leta,lphi,lM); 
                            lup10.SetPtEtaPhiM(lpt,leta,lphi,lM); 
                            ldown0.SetPtEtaPhiM(lpt,leta,lphi,lM); 
                            ldown1.SetPtEtaPhiM(lpt,leta,lphi,lM); 
                            ldown10.SetPtEtaPhiM(lpt,leta,lphi,lM); 

                        }
                        else {
                            lup.SetPtEtaPhiM(lpt*1.012,leta,lphi,lM*1.012); 
                            lup10.SetPtEtaPhiM(lpt*1.012,leta,lphi,lM*1.012); 
                            ldown.SetPtEtaPhiM(lpt*0.988,leta,lphi,lM*0.988); 
                            ldown10.SetPtEtaPhiM(lpt*0.988,leta,lphi,lM*0.988); 
                            //Other DM No shift
                            lup0.SetPtEtaPhiM(lpt,leta,lphi,lM); 
                            lup1.SetPtEtaPhiM(lpt,leta,lphi,lM); 
                            lup10.SetPtEtaPhiM(lpt,leta,lphi,lM); 
                            ldown0.SetPtEtaPhiM(lpt,leta,lphi,lM); 
                            ldown1.SetPtEtaPhiM(lpt,leta,lphi,lM); 
                            ldown10.SetPtEtaPhiM(lpt,leta,lphi,lM); 
                        }
                    }
                    else{//Fill unchanged vectors if not genmatched
                        lup.SetPtEtaPhiM(lpt,leta,lphi,lM); 
                        lup0.SetPtEtaPhiM(lpt,leta,lphi,lM); 
                        lup1.SetPtEtaPhiM(lpt,leta,lphi,lM); 
                        lup10.SetPtEtaPhiM(lpt,leta,lphi,lM); 
                        ldown.SetPtEtaPhiM(lpt,leta,lphi,lM); 
                        ldown0.SetPtEtaPhiM(lpt,leta,lphi,lM); 
                        ldown1.SetPtEtaPhiM(lpt,leta,lphi,lM); 
                        ldown10.SetPtEtaPhiM(lpt,leta,lphi,lM); 
                    }
                }//end di tau vector setting


                float dxUp= (tau-tauup+l-lup).Px();
                float dxDown= (tau-taudown+l-ldown).Px();
                float dyUp= (tau-tauup+l-lup).Py();
                float dyDown= (tau-taudown+l-ldown).Py();

                float dxUp0= (tau-tauup0+l-lup0).Px();
                float dxDown0= (tau-taudown0+l-ldown0).Px();
                float dyUp0= (tau-tauup0+l-lup0).Py();
                float dyDown0= (tau-taudown0+l-ldown0).Py();
                float dxUp1= (tau-tauup1+l-lup1).Px();
                float dxDown1= (tau-taudown1+l-ldown1).Px();
                float dyUp1= (tau-tauup1+l-lup1).Py();
                float dyDown1= (tau-taudown1+l-ldown1).Py();
                float dxUp10= (tau-tauup10+l-lup10).Px();
                float dxDown10= (tau-taudown10+l-ldown10).Px();
                float dyUp10= (tau-tauup10+l-lup10).Py();
                float dyDown10= (tau-taudown10+l-ldown10).Py();

                //std::cout<<"DeltaTau px: "<<dx<<"DeltaTau py: "<<dy<<std::endl;

                float metcor = calcHyp( metcorr_ex,metcorr_ey);

                float metcorUP = calcHyp( metcorr_ex-dxUp,metcorr_ey-dyUp);
                float metcorUP0 = calcHyp( metcorr_ex-dxUp0,metcorr_ey-dyUp0);
                float metcorUP1 = calcHyp( metcorr_ex-dxUp1,metcorr_ey-dyUp1);
                float metcorUP10 = calcHyp( metcorr_ex-dxUp10,metcorr_ey-dyUp10);

                float metcorDOWN = calcHyp( metcorr_ex-dxDown,metcorr_ey-dyDown);
                float metcorDOWN0 = calcHyp( metcorr_ex-dxDown0,metcorr_ey-dyDown0);
                float metcorDOWN1 = calcHyp( metcorr_ex-dxDown1,metcorr_ey-dyDown1);
                float metcorDOWN10 = calcHyp( metcorr_ex-dxDown10,metcorr_ey-dyDown10);

                float metcorphi = TMath::ATan2(metcorr_ey,metcorr_ex);

                float metcorphiUp = TMath::ATan2(metcorr_ey-dyUp,metcorr_ex-dxUp);
                float metcorphiUp0 = TMath::ATan2(metcorr_ey-dyUp0,metcorr_ex-dxUp0);
                float metcorphiUp1 = TMath::ATan2(metcorr_ey-dyUp1,metcorr_ex-dxUp1);
                float metcorphiUp10 = TMath::ATan2(metcorr_ey-dyUp10,metcorr_ex-dxUp10);

                float metcorphiDown = TMath::ATan2(metcorr_ey-dyDown,metcorr_ex-dyDown);
                float metcorphiDown0 = TMath::ATan2(metcorr_ey-dyDown0,metcorr_ex-dyDown0);
                float metcorphiDown1 = TMath::ATan2(metcorr_ey-dyDown1,metcorr_ex-dyDown1);
                float metcorphiDown10 = TMath::ATan2(metcorr_ey-dyDown10,metcorr_ex-dyDown10);

                met.SetPtEtaPhiM(metcor,0,metcorphi,0);
                metup.SetPtEtaPhiM(metcorUP,0,metcorphiUp,0);
                metup0.SetPtEtaPhiM(metcorUP0,0,metcorphiUp0,0);
                metup1.SetPtEtaPhiM(metcorUP1,0,metcorphiUp1,0);
                metup10.SetPtEtaPhiM(metcorUP10,0,metcorphiUp10,0);

                metdown.SetPtEtaPhiM(metcorDOWN,0,metcorphiDown,0);
                metdown0.SetPtEtaPhiM(metcorDOWN0,0,metcorphiDown0,0);
                metdown1.SetPtEtaPhiM(metcorDOWN1,0,metcorphiDown1,0);
                metdown10.SetPtEtaPhiM(metcorDOWN10,0,metcorphiDown10,0);

                metREDO=metcor;
                metREDOUp=metcorUP;
                metREDOUp0=metcorUP0;
                metREDOUp1=metcorUP1;
                metREDOUp10=metcorUP10;
                metREDODown=metcorDOWN;
                metREDODown0=metcorDOWN0;
                metREDODown1=metcorDOWN1;
                metREDODown10=metcorDOWN10;

                pthREDO=calcPTH(l,tau);
                pthREDOUp=calcPTH(lup,tauup);
                pthREDOUp0=calcPTH(lup0,tauup0);
                pthREDOUp1=calcPTH(lup1,tauup1);
                pthREDOUp10=calcPTH(lup10,tauup10);
                pthREDODown=calcPTH(ldown,taudown);
                pthREDODown0=calcPTH(ldown0,taudown0);
                pthREDODown1=calcPTH(ldown1,taudown1);
                pthREDODown10=calcPTH(ldown10,taudown10);

                tauptREDO=tau.Pt();
                tauptREDOUp=tauup.Pt();
                tauptREDOUp0=tauup0.Pt();
                tauptREDOUp1=tauup1.Pt();
                tauptREDOUp10=tauup10.Pt();
                tauptREDODown=taudown.Pt();
                tauptREDODown0=taudown0.Pt();
                tauptREDODown1=taudown1.Pt();
                tauptREDODown10=taudown10.Pt();

                taupt2REDO=l.Pt();
                taupt2REDOUp=lup.Pt();
                taupt2REDOUp0=lup0.Pt();
                taupt2REDOUp1=lup1.Pt();
                taupt2REDOUp10=lup10.Pt();
                taupt2REDODown=ldown.Pt();
                taupt2REDODown0=ldown0.Pt();
                taupt2REDODown1=ldown1.Pt();
                taupt2REDODown10=ldown10.Pt();

                //mvis= calcMVis(l,tau);
                mtTot=calcMttot(l,tau,met);
                mtTotUp=calcMttot(lup,tauup,metup);
                mtTotUp0=calcMttot(lup0,tauup0,metup0);
                mtTotUp1=calcMttot(lup1,tauup1,metup1);
                mtTotUp10=calcMttot(lup10,tauup10,metup10);
                mtTotDown=calcMttot(ldown,taudown,metdown);
                mtTotDown0=calcMttot(ldown0,taudown0,metdown0);
                mtTotDown1=calcMttot(ldown1,taudown1,metdown1);
                mtTotDown10=calcMttot(ldown10,taudown10,metdown10);

                mvis=calcMVis(l,tau);
                mvisUp=calcMVis(lup,tauup);
                mvisUp0=calcMVis(lup0,tauup0);
                mvisUp1=calcMVis(lup1,tauup1);
                mvisUp10=calcMVis(lup10,tauup10);
                mvisDown=calcMVis(ldown,taudown);
                mvisDown0=calcMVis(ldown0,taudown0);
                mvisDown1=calcMVis(ldown1,taudown1);
                mvisDown10=calcMVis(ldown10,taudown10);

                newBranch1->Fill();
                newBranch2->Fill();
                newBranch2a->Fill();
                newBranch2b->Fill();
                newBranch2c->Fill();
                newBranch3->Fill();
                newBranch3a->Fill();
                newBranch3b->Fill();
                newBranch3c->Fill();

                newBranch4->Fill();
                newBranch5->Fill();
                newBranch5a->Fill();
                newBranch5b->Fill();
                newBranch5c->Fill();
                newBranch6->Fill();
                newBranch6a->Fill();
                newBranch6b->Fill();
                newBranch6c->Fill();

                newBranch7->Fill();
                newBranch8->Fill();
                newBranch8a->Fill();
                newBranch8b->Fill();
                newBranch8c->Fill();
                newBranch9->Fill();
                newBranch9a->Fill();
                newBranch9b->Fill();
                newBranch9c->Fill();

                newBranch10->Fill();
                newBranch11->Fill();
                newBranch11a->Fill();
                newBranch11b->Fill();
                newBranch11c->Fill();
                newBranch12->Fill();
                newBranch12a->Fill();
                newBranch12b->Fill();
                newBranch12c->Fill();

                newBranch13->Fill();
                newBranch14->Fill();
                newBranch14a->Fill();
                newBranch14b->Fill();
                newBranch14c->Fill();
                newBranch15->Fill();
                newBranch15a->Fill();
                newBranch15b->Fill();
                newBranch15c->Fill();

                newBranch16->Fill();
                newBranch17->Fill();
                newBranch17a->Fill();
                newBranch17b->Fill();
                newBranch17c->Fill();
                newBranch18->Fill();
                newBranch18a->Fill();
                newBranch18b->Fill();
                newBranch18c->Fill();



            }
            dir->cd();
            t->Write("",TObject::kOverwrite);

        }//end else if object A
    }//end while key
}//end read directory
