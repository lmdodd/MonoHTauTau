#include "PhysicsTools/FWLite/interface/CommandLineParser.h" 
#include "TFile.h"
#include "TROOT.h"
#include "TKey.h"
#include "TTree.h"
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

    readdir(f,parser, TreeToUse),

    f->Close();

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

            float taupt=-10.0;
            float tauM=-10.0;
            float tauDM=-10.0;


            float taupt1=-10.0;
            float taupt2=-10.0;
            float tauM1=-10.0;
            float tauM2=-10.0;
            float tauDM1=-10.0;
            float tauDM2=-10.0;

            float newtaupt=-10.0;
            float newtauptUP=-10.0;
            float newtauptDOWN=-10.0;
            float newtaupt2=-10.0;
            float newtauptUP2=-10.0;
            float newtauptDOWN2=-10.0;



            TTree *t = (TTree*)obj;
            printf("Found tree -> weighting\n");

            TBranch *newBranch1 = t->Branch("taupt",&newtaupt,"taupt/F");
            TBranch *newBranch2 = t->Branch("taupt_UP",&newtauptUP,"taupt_UP/F");
            TBranch *newBranch3 = t->Branch("taupt_DOWN",&newtauptDOWN,"taupt_DOWN/F");
            TBranch *newBranch4 = t->Branch("taupt_2",&newtaupt2,"taupt_2/F");
            TBranch *newBranch5 = t->Branch("taupt_2UP",&newtauptUP2,"taupt_2UP/F");
            TBranch *newBranch6 = t->Branch("taupt_2DOWN",&newtauptDOWN2,"taupt_2DOWN/F");


            std::cout<<"KeyName "<<keyname<<" or key->GetName() "<<key->GetName()<<std::endl;
            if(std::string(TreeToUse).find("muTauEvent")!= std::string::npos || std::string(TreeToUse).find("eleTauEvent")!= std::string::npos){
                std::cout<<"Using muTau!"<<std::endl;
                t->SetBranchAddress("pt_2",&taupt);
                t->SetBranchAddress("m_2",&tauM);
                t->SetBranchAddress("tauDecayMode",&tauDM);

            }
            else if(std::string(TreeToUse).find("diTauEvent")!= std::string::npos){
                std::cout<<"Using diTau!"<<std::endl;

                t->SetBranchAddress("pt_1",&taupt1);
                t->SetBranchAddress("pt_2",&taupt2);
                t->SetBranchAddress("tauDecayMode_1",&tauDM1);
                t->SetBranchAddress("tauDecayMode_2",&tauDM2);

            }

            for(Int_t i=0;i<t->GetEntries();++i)
            {
                t->GetEntry(i);

                if(std::string(TreeToUse).find("muTauEvent")!= std::string::npos || std::string(TreeToUse).find("eleTauEvent")!= std::string::npos){
                    newtaupt=0;
                    newtauptUP=0;
                    newtauptDOWN=0;

                    if (tauDM==0) newtaupt=taupt*0.995;
                    else if (tauDM==1) newtaupt=taupt*1.011;
                    else if (tauDM==10) newtaupt=taupt*1.006;             


                    newtauptUP=newtaupt*1.012;
                    newtauptDOWN=newtaupt*0.988;
                    newBranch1->Fill();
                    newBranch2->Fill();
                    newBranch3->Fill();
                }

                else if(std::string(TreeToUse).find("diTauEvent")!= std::string::npos){
                    newtaupt=0;
                    newtauptUP=0;
                    newtauptDOWN=0;

                    newtaupt2=0;
                    newtauptUP2=0;
                    newtauptDOWN2=0;

                    if (tauDM1==0) newtaupt=taupt1*0.995;
                    else if (tauDM1==1) newtaupt=taupt1*1.011;
                    else if (tauDM1==10) newtaupt=taupt1*1.006;             
                    if (tauDM2==0) newtaupt2=taupt2*0.995;
                    else if (tauDM2==1) newtaupt2=taupt2*1.011;
                    else if (tauDM2==10) newtaupt2=taupt2*1.006;             

                    newtauptUP=newtaupt*1.012;
                    newtauptDOWN=newtaupt*0.988;

                    newtauptUP2=newtaupt2*1.012;
                    newtauptDOWN2=newtaupt2*0.988;


                    newBranch1->Fill();
                    newBranch2->Fill();
                    newBranch3->Fill();
                    newBranch4->Fill();
                    newBranch5->Fill();
                    newBranch6->Fill();
                }

            }
            t->Write("",TObject::kOverwrite);
        }//end else if object A
    }//end while key
}//end read directory
