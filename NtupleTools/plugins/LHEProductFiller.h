// system include files
#include <memory>
#include "TLorentzVector.h"
#include <vector>
// user include files
#include <TTree.h>
#include "SimDataFormats/GeneratorProducts/interface/LHEEventProduct.h"
#include "MonoHTauTau/NtupleTools/interface/NtupleFillerBase.h"

//
// class decleration
//

class LHEProductFiller : public NtupleFillerBase {
	public:
		LHEProductFiller(){
		}


		LHEProductFiller(const edm::ParameterSet& iConfig, TTree* t,edm::ConsumesCollector && iC):
			src_(iC.consumes<LHEEventProduct>(iConfig.getParameter<edm::InputTag> ("src"))),
			tag_(iConfig.getParameter<std::string>("tag"))
	{
		value1 = 0;
		value2 = 0;
		value3 = 0;
		value4 = 0;
		value5 = 0;
        Svalue = new float[9];
		t->Branch((tag_+"_njet").c_str(),&value1,(tag_+"_njet/I").c_str());
		t->Branch((tag_+"_mll").c_str(),&value2,(tag_+"_mll/I").c_str());
		t->Branch((tag_+"_ht").c_str(),&value3,(tag_+"_ht/F").c_str());
		t->Branch((tag_+"_pdfweight").c_str(),&value4,(tag_+"_pdfweight/F").c_str());
		t->Branch((tag_+"_nlheweight").c_str(),&value5,(tag_+"_nlheweight/I").c_str());
		t->Branch((tag_+"_genWeight_QCDscale_muR1_muF1").c_str(),&Svalue[0],(tag_+"_genWeight_QCDscale_muR1_muF1/F").c_str());
		t->Branch((tag_+"_genWeight_QCDscale_muR1_muF2").c_str(),&Svalue[1],(tag_+"_genWeight_QCDscale_muR1_muF2/F").c_str());
		t->Branch((tag_+"_genWeight_QCDscale_muR1_muF0p5").c_str(),&Svalue[2],(tag_+"_genWeight_QCDscale_muR1_muF0p5/F").c_str());
		t->Branch((tag_+"_genWeight_QCDscale_muR2_muF1").c_str(),&Svalue[3],(tag_+"_genWeight_QCDscale_muR2_muF1/F").c_str());
		t->Branch((tag_+"_genWeight_QCDscale_muR2_muF2").c_str(),&Svalue[4],(tag_+"_genWeight_QCDscale_muR2_muF2/F").c_str());
		t->Branch((tag_+"_genWeight_QCDscale_muR2_muF0p5").c_str(),&Svalue[5],(tag_+"_genWeight_QCDscale_muR2_muF0p5/F").c_str());
		t->Branch((tag_+"_genWeight_QCDscale_muR0p5_muF1").c_str(),&Svalue[6],(tag_+"_genWeight_QCDscale_muR0p5_muF1/F").c_str());
		t->Branch((tag_+"_genWeight_QCDscale_muR0p5_muF2").c_str(),&Svalue[7],(tag_+"_genWeight_QCDscale_muR0p5_muF2/F").c_str());
		t->Branch((tag_+"_genWeight_QCDscale_muR0p5_muF0p5").c_str(),&Svalue[8],(tag_+"_genWeight_QCDscale_muR0p5_muF0p5/F").c_str());
	}


		~LHEProductFiller()
		{

		}


		void fill(const edm::Event& iEvent, const edm::EventSetup& iSetup)
		{
			edm::Handle<LHEEventProduct> lheEventProduct;
			value1=0;
			value2=0;
			value3=0;
			value3=4;
			int NParton=0;
			int NL=0;
			float HT=0;
			float pdfWeight_=0;
			int nlheWeights_=0;
			float genWeight_QCDscale_muR1_muF1_ =0; 
			float genWeight_QCDscale_muR1_muF2_ =0; 
			float genWeight_QCDscale_muR1_muF0p5_ =0; 
            float genWeight_QCDscale_muR2_muF1_ = 0;
            float genWeight_QCDscale_muR2_muF2_ = 0;
            float genWeight_QCDscale_muR2_muF0p5_ = 0;
            float genWeight_QCDscale_muR0p5_muF1_ =0;
            float genWeight_QCDscale_muR0p5_muF2_ =0;
            float genWeight_QCDscale_muR0p5_muF0p5_ =0;
            std::vector<float>    pdfSystWeight_;
            std::vector<float>    lheNormalizedWeights_;
            std::vector<std::string>   lheWeightIDs_;



			TLorentzVector l;
            if(iEvent.getByToken(src_,lheEventProduct)) {
                int nup = lheEventProduct->hepeup().NUP;


                pdfWeight_ = lheEventProduct->originalXWGTUP(); // PDF weight of this event !
                for (unsigned i = 0; i < lheEventProduct->weights().size(); ++i) {
                    pdfSystWeight_.push_back(lheEventProduct->weights()[i].wgt);
                }
                nlheWeights_ = lheEventProduct->weights().size();
                for (unsigned i = 0; i < lheEventProduct->weights().size(); ++i) {
                    lheNormalizedWeights_.push_back(lheEventProduct->weights()[i].wgt/lheEventProduct->originalXWGTUP());
                    lheWeightIDs_.push_back(lheEventProduct->weights()[i].id);
                }
                if(nlheWeights_ >= 9){
                    genWeight_QCDscale_muR1_muF1_ = lheEventProduct->weights()[0].wgt/lheEventProduct->originalXWGTUP();
                    genWeight_QCDscale_muR1_muF2_ = lheEventProduct->weights()[1].wgt/lheEventProduct->originalXWGTUP();
                    genWeight_QCDscale_muR1_muF0p5_ = lheEventProduct->weights()[2].wgt/lheEventProduct->originalXWGTUP();
                    genWeight_QCDscale_muR2_muF1_ = lheEventProduct->weights()[3].wgt/lheEventProduct->originalXWGTUP();
                    genWeight_QCDscale_muR2_muF2_ = lheEventProduct->weights()[4].wgt/lheEventProduct->originalXWGTUP();
                    genWeight_QCDscale_muR2_muF0p5_ = lheEventProduct->weights()[5].wgt/lheEventProduct->originalXWGTUP();
                    genWeight_QCDscale_muR0p5_muF1_ = lheEventProduct->weights()[6].wgt/lheEventProduct->originalXWGTUP();
                    genWeight_QCDscale_muR0p5_muF2_ = lheEventProduct->weights()[7].wgt/lheEventProduct->originalXWGTUP();
                    genWeight_QCDscale_muR0p5_muF0p5_ = lheEventProduct->weights()[8].wgt/lheEventProduct->originalXWGTUP();
                }


                for (int i = 0; i < nup ; ++i) {
                    if (lheEventProduct->hepeup().ISTUP[i] == 1 && (abs(lheEventProduct->hepeup().IDUP[i])<6||lheEventProduct->hepeup().IDUP[i]==21 )) {
                        ++NParton;	
                    }
                    if (lheEventProduct->hepeup().ISTUP[i] == 1 && (abs(lheEventProduct->hepeup().IDUP[i])==11||abs(lheEventProduct->hepeup().IDUP[i])==13||abs(lheEventProduct->hepeup().IDUP[i])==15 )) {
                        l += TLorentzVector(lheEventProduct->hepeup().PUP[i].x[0], lheEventProduct->hepeup().PUP[i].x[1], lheEventProduct->hepeup().PUP[i].x[2], lheEventProduct->hepeup().PUP[i].x[3]);	   
                        ++NL;
                    }

                    //calculate MAdgraph HT
                    int absPdgId = TMath::Abs(lheEventProduct->hepeup().IDUP[i]);
                    if (lheEventProduct->hepeup().ISTUP[i]==1&&((absPdgId >= 1 && absPdgId <= 6) || absPdgId == 21) ) { // quarks and gluons
                        HT += TMath::Sqrt(TMath::Power(lheEventProduct->hepeup().PUP[i].x[0], 2.) + TMath::Power(lheEventProduct->hepeup().PUP[i].x[1], 2.)); // first entry is px, second py

                    }

                }
            }


            value1 = NParton;
            if (NL==2) value2 = l.M();
            value3 = HT;
            value4 = pdfWeight_;
            value5 = nlheWeights_;
            //std::cout<<"HT :"<<HT<<std::endl;

           Svalue[0]=genWeight_QCDscale_muR1_muF1_ ;
           Svalue[1]=genWeight_QCDscale_muR1_muF2_ ;
           Svalue[2]=genWeight_QCDscale_muR1_muF0p5_ ;
           Svalue[3]=genWeight_QCDscale_muR2_muF1_ ;
           Svalue[4]=genWeight_QCDscale_muR2_muF2_ ;
           Svalue[5]=genWeight_QCDscale_muR2_muF0p5_ ;
           Svalue[6]=genWeight_QCDscale_muR0p5_muF1_ ;
           Svalue[7]=genWeight_QCDscale_muR0p5_muF2_ ;
           Svalue[8]=genWeight_QCDscale_muR0p5_muF0p5_ ;

        }


    protected:
        edm::EDGetTokenT<LHEEventProduct> src_;
        std::string tag_;
        int value1;
        int value2;
        float value3;
        float value4;
        int value5;

        float* Svalue;

};







