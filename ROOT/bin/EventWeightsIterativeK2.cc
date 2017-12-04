#include "PhysicsTools/FWLite/interface/CommandLineParser.h" 
#include "TFile.h"
#include "TROOT.h"
#include "TKey.h"
#include "TTree.h"
#include "TH1F.h"
#include "TMath.h"
#include "TFileMerger.h"
#include <iostream>


using namespace std;

void readdir(TDirectory *dir,optutl::CommandLineParser parser,TH1F* hist, bool isOne); 



int main (int argc, char* argv[]) 
{
    optutl::CommandLineParser parser ("Sets Event Weights in the ntuple");
    parser.addOption("histoName",optutl::CommandLineParser::kString,"Counter Histogram Name","EventSummary");
    parser.addOption("isOne",optutl::CommandLineParser::kDouble,"If true, embed 1",0.0);
    parser.addOption("branch",optutl::CommandLineParser::kString,"Branch","WWNLOewk");


    parser.parseArguments (argc, argv);
    std::cout << "EXTRA COMMANDS:"
        << "\n --- isOne: " << parser.doubleValue("isOne")
        << std::endl;
    bool isOne = parser.doubleValue("isOne");

    TFile *fWpt    = new TFile("WWsigma.root","UPDATE");
    TH1F* hWpt = 0;
    if(fWpt!=0 && fWpt->IsOpen()) {
        hWpt = (TH1F*)fWpt->Get("NLOEW");
        printf("ENABLING W WEIGHTING USING HISTOGRAM\n");
    }
    else{
        printf("ERROR!!! WEIGHT FILE NOT FOUND!!! EXITING!!!\n");
        return 0;
    }


    TFile *f0 = new TFile(parser.stringValue("outputFile").c_str(),"UPDATE");   
    readdir(f0,parser,hWpt, isOne);
    f0->Close();

    if(fWpt!=0 && fWpt->IsOpen())
        fWpt->Close();


} 


void readdir(TDirectory *dir,optutl::CommandLineParser parser, TH1F* hist, bool isOne) 
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
            readdir(subdir,parser,hist,isOne);
            dirsav->cd();
        }
        else if(obj->IsA()->InheritsFrom(TTree::Class())) {
            TTree *t = (TTree*)obj;
            float weight;


            TBranch *newBranch = t->Branch(parser.stringValue("branch").c_str(),&weight,(parser.stringValue("branch")+"/F").c_str());
            float pfmet=0;
            printf("Found tree -> weighting\n");

            t->SetBranchAddress("met",&pfmet); //InvMass

            for(Int_t i=0;i<t->GetEntries();++i){
                t->GetEntry(i);

                weight =  1.0;

                if (!isOne){
                    if (pfmet>1999) pfmet=1999.;


                    if (pfmet>20){

                        int bin = hist->GetXaxis()->FindBin(pfmet);
                        weight = hist->GetBinContent(bin);
                    }
                }
                newBranch->Fill();
            }
            t->Write("",TObject::kOverwrite);
        }



    }

}
