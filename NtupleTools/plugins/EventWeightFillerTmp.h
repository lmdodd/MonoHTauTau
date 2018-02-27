// system include files
#include <memory>

// user include files

#include <TTree.h>
#include "TH2D.h"
#include <TFile.h>

#include "MonoHTauTau/NtupleTools/interface/NtupleFillerBase.h"
#include "DataFormats/VertexReco/interface/Vertex.h"
#include "SimDataFormats/PileupSummaryInfo/interface/PileupSummaryInfo.h"

#include "CommonTools/Utils/interface/StringObjectFunction.h"
#include "boost/filesystem.hpp"
//#include "MonoHTauTau/NtupleTools/plugins/HTTTnP.C"

//
// class decleration
//

template<typename T>
class EventWeightFillerTmp : public NtupleFillerBase {
    public:
        EventWeightFillerTmp(){
        }

        EventWeightFillerTmp(const edm::ParameterSet& iConfig, TTree* t, edm::ConsumesCollector && iC ):
            src_(iC.consumes<std::vector<T> >(iConfig.getParameter<edm::InputTag>("src"))) 
    {
        value = new float[2];
        t->Branch("WPt_reweight",&value[0],"WPt_reweight/F");
        t->Branch("ZPt_reweight",&value[1],"ZPt_reweight/F");
        std::string base = std::getenv("CMSSW_BASE");
        std::string fKFactor ="/src/MonoHTauTau/Configuration/data/kfactor.root";
        std::string file=base+fKFactor;
        bool fis   = boost::filesystem::exists( file );
        if (fis ){
            std::cout<<"INFO::V-Pt reweighting using kfacotr map"<<std::endl;
            f_Map = new TFile(file.c_str(),"READONLY");
            h1_EWK_W    = (TH1F*)f_Map->Get("EWKcorr/W");
            h1_EWK_Z    = (TH1F*)f_Map->Get("EWKcorr/Z");
            h1_LO_W    = (TH1F*)f_Map->Get("WJets_LO/inv_pt");
            h1_LO_Z    = (TH1F*)f_Map->Get("ZJets_LO/inv_pt");
            h1_EWK_W->Divide(h1_LO_W);
            h1_EWK_Z->Divide(h1_LO_Z);
            h1_W = (TH1F*) h1_EWK_W->Clone();
            h1_Z = (TH1F*) h1_EWK_Z->Clone();
        }
        else{
            std::cout<<"INFO::V-pt reweighting histo not found"<<std::endl;
        }

    }

        ~EventWeightFillerTmp()
        { 
        }

        void fill(const edm::Event& iEvent, const edm::EventSetup& iSetup)
        {
            float pt = 0;
            float wvalue = 0;
            float zvalue = 0;
            edm::Handle<std::vector<T>> handle;
            if( iEvent.getByToken(src_,handle)){
                pt = handle->at(0).genBosonPt();
                //printf("Gen Boson pt: %0.2f \n", pt);
                if (pt < 150) pt=151;
                wvalue = h1_W->GetBinContent(h1_W->GetXaxis()->FindBin(pt));   
                zvalue=h1_Z->GetBinContent(h1_Z->GetXaxis()->FindBin(pt));
            }

            value[0]=wvalue;
            value[1]=zvalue;

            //printf("Gen Boson pt: %0.2f W-Kfactor: %0.2f  Z-factor: %0.2f\n ", pt, value[0],value[1]);
        }

    protected:
        edm::EDGetTokenT<std::vector<T> > src_;
        TFile *f_Map;
        TH1F *h1_EWK_W;
        TH1F *h1_EWK_Z;
        TH1F *h1_LO_W;
        TH1F *h1_LO_Z;
        TH1F *h1_W;
        TH1F *h1_Z;
        float* value;

};




#include "MonoHTauTau/DataFormats/interface/CompositePtrCandidateT1T2MEt.h"
#include "MonoHTauTau/DataFormats/interface/CompositePtrCandidateTMEt.h"

typedef EventWeightFillerTmp<PATMuTauPair> PATMuTauPairWeightFillerTmp;
typedef EventWeightFillerTmp<PATElecTauPair> PATEleTauPairWeightFillerTmp;
typedef EventWeightFillerTmp<PATDiTauPair> PATDiTauPairWeightFillerTmp;



