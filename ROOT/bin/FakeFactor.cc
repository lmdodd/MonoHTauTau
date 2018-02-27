#include "PhysicsTools/FWLite/interface/CommandLineParser.h" 
#include "TFile.h"
#include "TROOT.h"
#include "TKey.h"
#include "TTree.h"
#include "TH1F.h"
#include "TMath.h"
#include "TFileMerger.h"
#include <iostream>



void readdir(TDirectory *dir,optutl::CommandLineParser parser, TH1F* hWpt0, TH1F* hWpt1, TH1F* hWpt10, TH1F* hWpt0_2, TH1F* hWpt1_2, TH1F* hWpt10_2,TH1F* hWpt0_1, TH1F* hWpt1_1, TH1F* hWpt10_1);


int main (int argc, char* argv[]) 
{
    optutl::CommandLineParser parser ("Sets Event Weights in the ntuple");
    parser.addOption("histoName",optutl::CommandLineParser::kString,"Counter Histogram Name","EventSummary");
    parser.addOption("weight",optutl::CommandLineParser::kDouble,"Weight to apply",1.0);
    parser.addOption("branchT",optutl::CommandLineParser::kString,"BranchT","FakeRateWeightTight");
    parser.addOption("branchL",optutl::CommandLineParser::kString,"BranchL","FakeRateWeightLoose");
    parser.addOption("branchAI",optutl::CommandLineParser::kString,"BranchAI","FakeRateWeightAI");


    parser.parseArguments (argc, argv);



    TFile *fWpt    = new TFile("fakeRate.root","UPDATE");
    TH1F* hWpt0 = 0;
    TH1F* hWpt1 = 0;
    TH1F* hWpt10 = 0;
    TH1F* hWpt0_2 = 0;
    TH1F* hWpt1_2 = 0;
    TH1F* hWpt10_2 = 0;
    TH1F* hWpt0_1 = 0;
    TH1F* hWpt1_1 = 0;
    TH1F* hWpt10_1 = 0;
 
    if(fWpt!=0 && fWpt->IsOpen()) {
        hWpt0 = (TH1F*)fWpt->Get("Tight_DM0");
        hWpt0->Divide((TH1F*)fWpt->Get("None_DM0"));
        hWpt1 = (TH1F*)fWpt->Get("Tight_DM1");
        hWpt1->Divide((TH1F*)fWpt->Get("None_DM1"));
        hWpt10 = (TH1F*)fWpt->Get("Tight_DM10");
        hWpt10->Divide((TH1F*)fWpt->Get("None_DM10"));

        hWpt0_2 = (TH1F*)fWpt->Get("Loose_DM0");
        hWpt0_2->Divide((TH1F*)fWpt->Get("None_DM0"));
        hWpt1_2 = (TH1F*)fWpt->Get("Loose_DM1");
        hWpt1_2->Divide((TH1F*)fWpt->Get("None_DM1"));
        hWpt10_2 = (TH1F*)fWpt->Get("Loose_DM10");
        hWpt10_2->Divide((TH1F*)fWpt->Get("None_DM10"));

        hWpt0_1 = (TH1F*)fWpt->Get("Medium_DM0");
        hWpt0_1->Divide((TH1F*)fWpt->Get("None_DM0"));
        hWpt1_1 = (TH1F*)fWpt->Get("Medium_DM1");
        hWpt1_1->Divide((TH1F*)fWpt->Get("None_DM1"));
        hWpt10_1 = (TH1F*)fWpt->Get("Medium_DM10");
        hWpt10_1->Divide((TH1F*)fWpt->Get("None_DM10"));


        printf("ENABLING W WEIGHTING USING HISTOGRAM\n");
    }
    else{
        printf("ERROR!!! WEIGHT FILE NOT FOUND!!! EXITING!!!\n");
        return 0;
    }


    TFile *f0 = new TFile(parser.stringValue("outputFile").c_str(),"UPDATE");   
    readdir(f0,parser,hWpt0,hWpt1,hWpt10,hWpt0_2,hWpt1_2,hWpt10_2, hWpt0_1,  hWpt1_1,  hWpt10_1);
    f0->Close();

    if(fWpt!=0 && fWpt->IsOpen())
        fWpt->Close();


} 


void readdir(TDirectory *dir,optutl::CommandLineParser parser, TH1F* hWpt0, TH1F* hWpt1, TH1F* hWpt10,  TH1F* hWpt0_2, TH1F* hWpt1_2, TH1F* hWpt10_2,TH1F* hWpt0_1, TH1F* hWpt1_1, TH1F* hWpt10_1) 
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
            readdir(subdir,parser,hWpt0,hWpt1, hWpt10,hWpt0_2,hWpt1_2,hWpt10_2, hWpt0_1,  hWpt1_1,  hWpt10_1);
            dirsav->cd();
        }
        else if(obj->IsA()->InheritsFrom(TTree::Class())) {
            TTree *t = (TTree*)obj;
            float weight;
            float weight1;
            float weight2;


            TBranch *newBranch = t->Branch(parser.stringValue("branchT").c_str(),&weight,(parser.stringValue("branchT")+"/F").c_str());
            TBranch *newBranch1 = t->Branch(parser.stringValue("branchAI").c_str(),&weight1,(parser.stringValue("branchAI")+"/F").c_str());
            TBranch *newBranch2 = t->Branch(parser.stringValue("branchL").c_str(),&weight2,(parser.stringValue("branchL")+"/F").c_str());
            float gen_match_1=-1;
            float gen_match_2=-1;
            float tauDecayMode=-1;
            float tauDecayMode_1=-1;
            float tauDecayMode_2=-1;
            float pt_1,pt_2;
            t->SetBranchAddress("gen_match_1",&gen_match_1); //InvMass
            t->SetBranchAddress("gen_match_2",&gen_match_2); //InvMass
            t->SetBranchAddress("tauDecayMode",&tauDecayMode); //InvMass
            t->SetBranchAddress("tauDecayMode_1",&tauDecayMode_1); //InvMass
            t->SetBranchAddress("tauDecayMode_2",&tauDecayMode_2); //InvMass
            t->SetBranchAddress("pt_1",&pt_1); //InvMass
            t->SetBranchAddress("pt_2",&pt_2); //InvMass

            printf("Found tree -> weighting\n");
            for(Int_t i=0;i<t->GetEntries();++i){
                t->GetEntry(i);
                //
                float fakerate=0;
                float fakerate1=0;
                float fakerate2=0;

                if (tauDecayMode!=-1){
                    if (tauDecayMode==0){
                        fakerate = hWpt0->GetBinContent(hWpt0->GetXaxis()->FindBin(pt_2));
                        fakerate1 = hWpt0_1->GetBinContent(hWpt0_1->GetXaxis()->FindBin(pt_2));
                        fakerate2 = hWpt0_2->GetBinContent(hWpt0_2->GetXaxis()->FindBin(pt_2));
                    }
                    else if (tauDecayMode==1){
                        fakerate = hWpt1->GetBinContent(hWpt1->GetXaxis()->FindBin(pt_2));
                        fakerate1 = hWpt1_1->GetBinContent(hWpt1_1->GetXaxis()->FindBin(pt_2));
                        fakerate2 = hWpt1_2->GetBinContent(hWpt1_2->GetXaxis()->FindBin(pt_2));
                    }
                    else if (tauDecayMode==10){
                        fakerate = hWpt10->GetBinContent(hWpt10->GetXaxis()->FindBin(pt_2));
                        fakerate1 = hWpt10_1->GetBinContent(hWpt10_1->GetXaxis()->FindBin(pt_2));
                        fakerate2 = hWpt10_2->GetBinContent(hWpt10_2->GetXaxis()->FindBin(pt_2));
                    }
                    else {
                        fakerate=0;
                        fakerate1=0;
                        fakerate2=0;
                    }

                    weight = fakerate /(1-fakerate); 
                    weight1 = fakerate1 /(1-fakerate1); 
                    weight2 = fakerate2 /(1-fakerate2); 
                }

                else{ //diTau channel
                    float fakerate=0;
                    float fakerate1=0;
                    float fakerate2=0;
                    float fakerateA=0;
                    float fakerateB=0;
                    float fakerateC=0;
                    bool isTrueA = false;
                    bool isTrueB = false;


                    if (gen_match_1==5) isTrueA=true; 
                    if (gen_match_2==5) isTrueB=true; 

                    if (tauDecayMode_1==0){
                        fakerate = hWpt0->GetBinContent(hWpt0->GetXaxis()->FindBin(pt_1));
                        fakerate1 = hWpt0_1->GetBinContent(hWpt0_1->GetXaxis()->FindBin(pt_1));
                        fakerate2 = hWpt0_2->GetBinContent(hWpt0_2->GetXaxis()->FindBin(pt_1));
                    }
                    else if (tauDecayMode_1==1){
                        fakerate = hWpt1->GetBinContent(hWpt1->GetXaxis()->FindBin(pt_1));
                        fakerate1 = hWpt1_1->GetBinContent(hWpt1_1->GetXaxis()->FindBin(pt_1));
                        fakerate2 = hWpt1_2->GetBinContent(hWpt1_2->GetXaxis()->FindBin(pt_1));
                    }
                    else if (tauDecayMode_1==10){
                        fakerate = hWpt10->GetBinContent(hWpt10->GetXaxis()->FindBin(pt_1));
                        fakerate1 = hWpt10_1->GetBinContent(hWpt10_1->GetXaxis()->FindBin(pt_1));
                        fakerate2 = hWpt10_2->GetBinContent(hWpt10_2->GetXaxis()->FindBin(pt_1));
                    }
                    else {
                        fakerate=0;
                        fakerate1=0;
                        fakerate2=0;
                    }


                    if (tauDecayMode_2==0){
                        fakerateA = hWpt0->GetBinContent(hWpt0->GetXaxis()->FindBin(pt_2));
                        fakerateB = hWpt0_1->GetBinContent(hWpt0_1->GetXaxis()->FindBin(pt_2));
                        fakerateC = hWpt0_2->GetBinContent(hWpt0_2->GetXaxis()->FindBin(pt_2));
                    }
                    else if (tauDecayMode_2==1){
                        fakerateA = hWpt1->GetBinContent(hWpt1->GetXaxis()->FindBin(pt_2));
                        fakerateB = hWpt1_1->GetBinContent(hWpt1_1->GetXaxis()->FindBin(pt_2));
                        fakerateC = hWpt1_2->GetBinContent(hWpt1_2->GetXaxis()->FindBin(pt_2));
                    }
                    else if (tauDecayMode_2==10){
                        fakerateA = hWpt10->GetBinContent(hWpt10->GetXaxis()->FindBin(pt_2));
                        fakerateB = hWpt10_1->GetBinContent(hWpt10_1->GetXaxis()->FindBin(pt_2));
                        fakerateC = hWpt10_2->GetBinContent(hWpt10_2->GetXaxis()->FindBin(pt_2));
                    }
                    else {
                        fakerateA=0;
                        fakerateB=0;
                        fakerateC=0;
                    }

                    if (!isTrueA&&!isTrueB){
                        //std::cout<<"both false"<<std::endl;
                        weight = (fakerate /(1-fakerate))*(fakerateA /(1-fakerateA));
                        weight1 = (fakerate1 /(1-fakerate1))*(fakerateB /(1-fakerateB));
                        weight2 = (fakerate2 /(1-fakerate2))*(fakerateC /(1-fakerateC));
                    }
                    else if (isTrueA&&!isTrueB){
                        //std::cout<<"el false"<<std::endl;
                        weight =(fakerateA /(1-fakerateA));
                        weight1=(fakerateB /(1-fakerateB));
                        weight2=(fakerateC /(1-fakerateC));
                    }
                    else if (!isTrueA&&isTrueB){
                        //std::cout<<"el false"<<std::endl;
                        weight = (fakerate /(1-fakerate));
                        weight1 = (fakerate1 /(1-fakerate1));
                        weight2 = (fakerate2 /(1-fakerate2));
                    }
                    else{
                        weight =1;
                        weight1=1;
                        weight2=1;
                    }

                }

                newBranch->Fill();
                newBranch1->Fill();
                newBranch2->Fill();
            }
            t->Write("",TObject::kOverwrite);
        }



    }

}
