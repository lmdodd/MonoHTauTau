#include "PhysicsTools/FWLite/interface/CommandLineParser.h" 
#include "PhysicsTools/Utilities/interface/Lumi3DReWeighting.h"
#include "PhysicsTools/Utilities/interface/LumiReWeighting.h"
#include "TFile.h"
#include "TROOT.h"
#include "TKey.h"
#include "TTree.h"
#include "TH1F.h"
#include <iostream>

using std::cout;
using std::endl;

void readdir(TDirectory *dir,optutl::CommandLineParser parser,float ev); 


int main (int argc, char* argv[]) 
{
   optutl::CommandLineParser parser ("Sets Event Weights in the ntuple");
   parser.addOption("histoName",optutl::CommandLineParser::kString,"Counter Histogram Name","EventSummary");
   
   parser.parseArguments (argc, argv);
   

 
   TFile *f = new TFile(parser.stringValue("outputFile").c_str(),"UPDATE");   
   
   readdir(f,parser,0);

   f->Close();

} 


void readdir(TDirectory *dir,optutl::CommandLineParser parser,float ev) 
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
		  readdir(subdir,parser,ev);
		  dirsav->cd();
	  }
	  else if(obj->IsA()->InheritsFrom(TTree::Class())) {
		  float weight2;
		  float weight3;

		  TTree *t = (TTree*)obj;
		  TBranch *newBranch2 = t->Branch("fakeTauEffiUp",&weight2,"fakeTauEffiUp/F");
		  TBranch *newBranch3 = t->Branch("fakeTauEffiDown",&weight3,"fakeTauEffiDown/F");

		  float tauPt=0;
		  t->SetBranchAddress("pt_2",&tauPt); //genPy


		  printf("Found tree -> weighting\n");
		  for(Int_t i=0;i<t->GetEntries();++i)
		  {
              t->GetEntry(i);
              if (tauPt>200)
                  tauPt=200.;

              weight2 = 0.8 *tauPt/100.0;
              weight3 = 1.2 *tauPt/100.0;
              newBranch2->Fill();
              newBranch3->Fill();
          }
          t->Write("",TObject::kOverwrite);
      }//end else if object A
  }//end while key
}//end read directory
