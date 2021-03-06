#include "PhysicsTools/FWLite/interface/CommandLineParser.h" 
#include "TFile.h"
#include "TROOT.h"
#include "TKey.h"
#include "TTree.h"
#include "TH2D.h"
#include "TMath.h"
#include "TFileMerger.h"
#include <iostream>

using namespace std;


void readdir(TDirectory *dir,optutl::CommandLineParser parser,TH2D* hist,bool isOne); 



int main (int argc, char* argv[]) 
{
    optutl::CommandLineParser parser ("Sets Event Weights in the ntuple");
    parser.addOption("histoName",optutl::CommandLineParser::kString,"Counter Histogram Name","EventSummary");
    parser.addOption("isOne",optutl::CommandLineParser::kDouble,"isOne, sets output to 1",1.0);

    parser.parseArguments (argc, argv);
    std::cout << "EXTRA COMMANDS:"
        << "\n --- isOne: " << parser.doubleValue("isOne")
        << std::endl;
    bool isOne = parser.doubleValue("isOne");



    TFile *fZpt  = new TFile("zzKfactorGenPt.root","UPDATE");
    TH2D* hZpt = 0;
    if(fZpt!=0 && fZpt->IsOpen()) {
        hZpt = (TH2D*)fZpt->Get("zzKfactorGenPt");;
        printf("ENABLING W WEIGHTING USING HISTOGRAM\n");
    }
    else{
        printf("ERROR!!! WEIGHT FILE NOT FOUND!!! EXITING!!!\n");
        return 0;
    }


    TFile *f0 = new TFile(parser.stringValue("outputFile").c_str(),"UPDATE");   
    readdir(f0,parser,hZpt,isOne);
    f0->Close();

    if(fZpt!=0 && fZpt->IsOpen())
        fZpt->Close();


} 


void readdir(TDirectory *dir,optutl::CommandLineParser parser, TH2D* hist, bool isOne) 
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
            readdir(subdir,parser,hist,isOne);
            dirsav->cd();
        }
        else if(obj->IsA()->InheritsFrom(TTree::Class())) {
            TTree *t = (TTree*)obj;
            float weight;
            float weightUp;
            float weightDown;


            TBranch *newBranch = t->Branch("ZZ_kfactor",&weight,"ZZ_kfactor/F");
            TBranch *newBranch1 = t->Branch("ZZ_kfactorUp",&weightUp,"ZZ_kfactorUp/F");
            TBranch *newBranch2 = t->Branch("ZZ_kfactorDown",&weightDown,"ZZ_kfactorDown/F");
            float genPt=0;
            t->SetBranchAddress("PtReweight",&genPt); //InvMass

            for(Int_t i=0;i<t->GetEntries();++i){
                t->GetEntry(i);
                weight =  1.0;
                weightUp =  1.0;
                weightDown =  1.0;

                if(!isOne){

                    float xval = hist->GetXaxis()->FindBin(genPt);
                    if (genPt>2000)
                        xval = 1999.;

                    float yval0 = hist->GetBinContent(xval,1);
                    float yval1 = hist->GetBinContent(xval,2);
                    float yval2 = hist->GetBinContent(xval,3);
                    float yval3 = hist->GetBinContent(xval,4);
                    if (!(yval0>0)){
                        yval0=1;
                        yval1=1;
                        yval2=1;
                        yval3=1;
                    }
                    weight = yval1/yval0;
                    weightUp = yval2/yval1;
                    weightDown = yval3/yval1;
                }

                newBranch->Fill();
                newBranch1->Fill();
                newBranch2->Fill();
            }
            t->Write("",TObject::kOverwrite);
        }



    }

}
