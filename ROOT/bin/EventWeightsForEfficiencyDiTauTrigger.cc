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
    parser.addOption("IsoFile",optutl::CommandLineParser::kString,"Iso Hist","htt_scalefactors_sm_moriond_v1.root");
    parser.parseArguments (argc, argv);


    TFile *f = new TFile(parser.stringValue("outputFile").c_str(),"UPDATE");

    char TreeToUse[80]="first" ;


    TFile fIso("htt_scalefactors_sm_moriond_v1.root");
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
            TBranch *newBranch = t->Branch("ditauweight",&weight,"ditauweight/F");



            float pt1;
            float eta1;
            float tauDM;

            t->SetBranchAddress("pt_1",&pt1);
            t->SetBranchAddress("eta_1",&eta1);
            t->SetBranchAddress("tauDecayMode",&tauDM);

            printf("Found tree -> weighting\n");
            std::cout<<"KeyName "<<keyname<<" or key->GetName() "<<key->GetName()<<std::endl;

            for(Int_t i=0;i<t->GetEntries();++i)
            {
                t->GetEntry(i);
                weight=1.0;
                //printf("Wvar: pt:%f, eta:%f, iso:%f \n",pt1,eta1,iso1);
                if(std::string(TreeToUse).find("muTauEvent")!= std::string::npos){
                    w->var("m_eta")->setVal(eta1);

                    weight = w->function("m_trk_ratio")->getVal();
                }
                else if(std::string(TreeToUse).find("eleTauEvent")!= std::string::npos){
                    w->var("e_pt")->setVal(pt1);
                    w->var("e_eta")->setVal(eta1);

                    weight = w->function("e_trk_ratio")->getVal();
                }
                else{
                    std::cout<<"TreeToUse "<< std::string(TreeToUse)<<" does not match muTauEvent or eleTauEvent... Skipping!!"<<std::endl;
                    continue;
                }

                newBranch->Fill();

            }

            t->Write("",TObject::kOverwrite);
        }
    }
}
