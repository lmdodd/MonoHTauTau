#include "PhysicsTools/FWLite/interface/CommandLineParser.h" 
#include "TFile.h"
#include "TROOT.h"
#include "TKey.h"
#include "TTree.h"
#include "TH1F.h"
#include "TMath.h"
#include "TFileMerger.h"



void readdir(TDirectory *dir,optutl::CommandLineParser parser,TH1F* hist); 



int main (int argc, char* argv[]) 
{
    optutl::CommandLineParser parser ("Sets Event Weights in the ntuple");
    parser.addOption("histoName",optutl::CommandLineParser::kString,"Counter Histogram Name","EventSummary");
    parser.addOption("weight",optutl::CommandLineParser::kDouble,"Weight to apply",1.0);
    parser.addOption("branch",optutl::CommandLineParser::kString,"Branch","EWKonlyREDO");


    parser.parseArguments (argc, argv);



    TFile *fWpt    = new TFile("kfactor.root","UPDATE");
    TH1F* hWpt = 0;
    if(fWpt!=0 && fWpt->IsOpen()) {
        hWpt = (TH1F*)fWpt->Get("EWKcorr/W");;
        hWpt->Divide((TH1F*)fWpt->Get("WJets_012j_NLO/nominal"));
        printf("ENABLING W WEIGHTING USING HISTOGRAM\n");
    }
    else{
        printf("ERROR!!! WEIGHT FILE NOT FOUND!!! EXITING!!!\n");
        return 0;
    }


    TFile *f0 = new TFile(parser.stringValue("outputFile").c_str(),"UPDATE");   
    readdir(f0,parser,hWpt);
    f0->Close();

    if(fWpt!=0 && fWpt->IsOpen())
        fWpt->Close();


} 


void readdir(TDirectory *dir,optutl::CommandLineParser parser, TH1F* hist) 
{
    TDirectory *dirsav = gDirectory;
    TIter next(dir->GetListOfKeys());
    TKey *key;
    while ((key = (TKey*)next())) {
        printf("Found key=%s \n",key->GetName());
        TObject *obj = key->ReadObj();

        if (obj->IsA()->InheritsFrom(TDirectory::Class())) {
            dir->cd(key->GetName());
            TDirectory *subdir = gDirectory;
            readdir(subdir,parser,hist);
            dirsav->cd();
        }
        else if(obj->IsA()->InheritsFrom(TTree::Class())) {
            TTree *t = (TTree*)obj;
            float weight;


            TBranch *newBranch = t->Branch(parser.stringValue("branch").c_str(),&weight,(parser.stringValue("branch")+"/F").c_str());
            float genPt=0;
            t->SetBranchAddress("PtReweight",&genPt); //InvMass

            //float genPx=0;
            //float genPy=0;
            //t->SetBranchAddress("genpX",&genPx); //genPx
            //t->SetBranchAddress("genpY",&genPy); //genPy


            printf("Found tree -> weighting\n");
            for(Int_t i=0;i<t->GetEntries();++i){
                t->GetEntry(i);
                //float genpT = TMath::Sqrt(genPx*genPx+genPy*genPy);
                //I think the above is more correct
                //printf("Found genPt -> %f,\n",genPt);
                //
                weight =  1.0;
                if (genPt < 150) genPt=151;
                weight = hist->GetBinContent(hist->GetXaxis()->FindBin(genPt));

                newBranch->Fill();
            }
            t->Write("",TObject::kOverwrite);
        }



    }

}
