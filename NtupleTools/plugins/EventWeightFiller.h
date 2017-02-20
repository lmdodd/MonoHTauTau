// system include files
#include <memory>

// user include files

#include <TTree.h>

#include "MonoHTauTau/NtupleTools/interface/NtupleFillerBase.h"
#include "DataFormats/VertexReco/interface/Vertex.h"
#include "SimDataFormats/PileupSummaryInfo/interface/PileupSummaryInfo.h"
#include "HTT-utilities/LepEffInterface/interface/ScaleFactor.h" //HTT Weights
//#include "MonoHTauTau/Configuration/data/fitfunc

#include "CommonTools/Utils/interface/StringObjectFunction.h"
#include "boost/filesystem.hpp"

//
// class decleration
//

template<typename T>
class EventWeightFiller : public NtupleFillerBase {
    public:
        EventWeightFiller(){
        }


        EventWeightFiller(const edm::ParameterSet& iConfig, TTree* t, edm::ConsumesCollector && iC ):
            src_(iC.consumes<std::vector<T> >(iConfig.getParameter<edm::InputTag>("src"))), 
            tag_(iConfig.getParameter<std::string>("tag")),
            isMu_(iConfig.getParameter<bool>("isMuon"))
    {
        value = new float[5];
        t->Branch("idisoweight_1",&value[0],"idisoweight_1/F");
        t->Branch("trigweight_1",&value[1],"trigweight_1/F");
        t->Branch((tag_+"EffWeight").c_str(),&value[2],(tag_+"EffWeight/F").c_str());
        t->Branch("trigeff_1",&value[3],"trigeff_1/F");
        t->Branch("antiiso_1",&value[4],"antiiso_1/F");
        std::string base = std::getenv("CMSSW_BASE");
        std::string fMuonIsolation =   "/src/HTT-utilities/LepEffInterface/data/Muon/Run2016BtoH/Muon_IdIso_IsoLt0p15_2016BtoH_eff.root";
        std::string fMuonTrigger =   "/src/HTT-utilities/LepEffInterface/data/Muon/Run2016BtoH/Muon_IsoMu24_OR_TkIsoMu24_2016BtoH_eff.root";
        std::string fEleIsolation =   "/src/HTT-utilities/LepEffInterface/data/Electron/Run2016BtoH/Electron_IdIso_IsoLt0p1_eff.root";
        std::string fEleTrigger =   "/src/HTT-utilities/LepEffInterface/data/Electron/Run2016BtoH/Electron_Ele25WPTight_eff.root";

        std::string fMuonIsolationAI =   "/src/HTT-utilities/LepEffInterface/data/Muon/Run2016BtoH/Muon_antiisolated_0p15to0p25_IdIso_eff.root";
        std::string fMuonTriggerAI =   "/src/HTT-utilities/LepEffInterface/data/Muon/Run2016BtoH/Muon_antiisolated_0p15to0p25_IsoMu24ORTkIsoMu24_eff_rb.root";
        std::string fEleIsolationAI =   "/src/HTT-utilities/LepEffInterface/data/Electron/Run2016BtoH/Electron_antiisolated_0p10to0p20_IdIso_eff.root";
        std::string fEleTriggerAI =   "/src/HTT-utilities/LepEffInterface/data/Electron/Run2016BtoH/Electron_Ele25WPTight_antiisolated_Iso0p1to0p3_eff_rb.root";
        std::string fileIso;
        std::string fileTrig;
        std::string fileIsoAI;
        std::string fileTrigAI;
        if (isMu_) {
            fileIso= base+fMuonIsolation;
            fileTrig= base+fMuonTrigger;
            fileIsoAI= base+fMuonIsolationAI;
            fileTrigAI= base+fMuonTriggerAI;
            bool fis   = boost::filesystem::exists( fileTrig   ) && boost::filesystem::exists( fileIso ) && boost::filesystem::exists( fileTrigAI  ) && boost::filesystem::exists( fileIsoAI);
            std::cout<<"file exist: "<<fis<<std::endl;
        }
        else {
            fileIso= base+fEleIsolation;
            fileTrig= base+fEleTrigger;
            fileIsoAI= base+fEleIsolationAI;
            fileTrigAI= base+fEleTriggerAI;
            bool fis   = boost::filesystem::exists( fileTrig   ) && boost::filesystem::exists( fileIso ) && boost::filesystem::exists( fileTrigAI  ) && boost::filesystem::exists( fileIsoAI) ;
            std::cout<<"file exist: "<<fis<<std::endl;

        }

        myScaleFactorIso = new ScaleFactor();
        myScaleFactorTrig = new ScaleFactor();
        myScaleFactorIsoAI = new ScaleFactor();
        myScaleFactorTrigAI = new ScaleFactor();

        myScaleFactorIso->init_ScaleFactor(fileIso);
        myScaleFactorTrig->init_ScaleFactor(fileTrig);
        myScaleFactorIsoAI->init_ScaleFactor(fileIsoAI);
        myScaleFactorTrigAI->init_ScaleFactor(fileTrigAI);

    }


        ~EventWeightFiller()
        { 
        }

        void fill(const edm::Event& iEvent, const edm::EventSetup& iSetup)
        {
            float pt = 0;
            float eta = 0;

            //function_pt = new StringObjectFunction<T>("leg1.pt");
            //function_eta = new StringObjectFunction<T>("leg1.eta");
            edm::Handle<std::vector<T>> handle;
            if( iEvent.getByToken(src_,handle)){
                pt = handle->at(0).leg1()->pt();
                eta = handle->at(0).leg1()->eta();
            }

            //double efficiency_data = myScaleFactorIso->get_EfficiencyData(pt, eta);
            //double efficiency_MC = myScaleFactorIso->get_EfficiencyMC(pt,eta);
            double scaleFactorIso = myScaleFactorIso->get_ScaleFactor(pt,eta);
            double scaleFactorTrig = myScaleFactorTrig->get_ScaleFactor(pt,eta);
            double efficiencyTrig = myScaleFactorTrig->get_EfficiencyData(pt,eta);

            value[0]=scaleFactorIso;
            value[1]=scaleFactorTrig;
            value[2]=(scaleFactorTrig*scaleFactorIso);
            value[3]=efficiencyTrig;
            value[4]= myScaleFactorIsoAI->get_ScaleFactor(pt,eta)*myScaleFactorTrigAI->get_ScaleFactor(pt,eta);
        }


    protected:
        edm::EDGetTokenT<std::vector<T> > src_;
        std::string tag_;
        bool isMu_;
        float* value;
        ScaleFactor *myScaleFactorIso; 
        ScaleFactor *myScaleFactorIsoAI; 
        ScaleFactor *myScaleFactorTrig;
        ScaleFactor *myScaleFactorTrigAI;


};




#include "MonoHTauTau/DataFormats/interface/CompositePtrCandidateT1T2MEt.h"
#include "MonoHTauTau/DataFormats/interface/CompositePtrCandidateTMEt.h"

typedef EventWeightFiller<PATMuTauPair> PATMuTauPairWeightFiller;
typedef EventWeightFiller<PATElecTauPair> PATEleTauPairWeightFiller;



