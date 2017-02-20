// system include files
#include <memory>
// user include files

#include <TFile.h>
#include <TTree.h>
#include <TH2D.h>
#include "TH1.h"
#include "TRandom3.h"

#include "MonoHTauTau/NtupleTools/interface/NtupleFillerBase.h"

#include "CommonTools/Utils/interface/StringObjectFunction.h"
#include "boost/filesystem.hpp"

//
// class decleration
//

template<typename T>
class POGSFsFiller : public NtupleFillerBase {
    public:
        POGSFsFiller(){
        }


        POGSFsFiller(const edm::ParameterSet& iConfig, TTree* t, edm::ConsumesCollector && iC ):
            src_(iC.consumes<std::vector<T> >(iConfig.getParameter<edm::InputTag>("src"))), 
            Mu_(iConfig.getParameter<bool>("isMu"))
    {
        value = new float[9]; 
        t->Branch("POGtrigger",&value[0],"POGtrigger/F");
        t->Branch("POGtriggerErr",&value[1],"POGtriggerErr/F");
        t->Branch("POGid1",&value[2],"POGid1/F");
        t->Branch("POGid1Err",&value[3],"POGid1Err/F");
        t->Branch("POGid2",&value[4],"POGid2/F");
        t->Branch("POGid2Err",&value[5],"POGid2Err/F");
        t->Branch("POGtrack",&value[6],"POGtrack/F");
        t->Branch("POGtrackErr",&value[7],"POGtrackErr/F");

        std::string base = std::getenv("CMSSW_BASE");
        std::string fPath =   "/src/MonoHTauTau/Configuration/data/";
        std::vector<std::string> fFile =  {"BCDEF_trigger.root","GH_trigger.root","BCDEF_MUON_IDISO.root","GH_MUON_IDISO.root"};

        if (!Mu_)
            fFile =  {"EleSoup.root","passingMVA80wp80X.root","passingMVA90wp80X.root","RecoEGEffi.root"};

        std::string path1= base+fPath+fFile[0];
        std::string path2= base+fPath+fFile[1];
        std::string path3= base+fPath+fFile[2];
        std::string path4= base+fPath+fFile[3];
        isFile_   = boost::filesystem::exists(path1)&&boost::filesystem::exists(path2)&&boost::filesystem::exists(path3)&&boost::filesystem::exists(path4);
        if (isFile_){
            std::cout<<"INFO:: POGSFsFiller using files"<<std::endl;
            f_file1 = TFile::Open(path1.c_str());
            f_file2 = TFile::Open(path2.c_str());
            f_file3 = TFile::Open(path3.c_str());
            f_file4 = TFile::Open(path4.c_str());
        }
        else { std::cout<<"WARNING::POGSFsFiller No efficiency file found!!!"<<std::endl;}

        if(Mu_){
            h2_trigger = (TH2D*)f_file1->Get("IsoMu24_OR_IsoTkMu24_PtEtaBins/abseta_pt_ratio");
            h2_trigger2    = (TH2D*)f_file2->Get("IsoMu24_OR_IsoTkMu24_PtEtaBins/abseta_pt_ratio");
            h2_id1    = (TH2D*)f_file3->Get("MC_NUM_TightID_DEN_genTracks_PAR_pt_eta/abseta_pt_ratio");
            h2_iso1    = (TH2D*)f_file3->Get("TightISO_TightID_pt_eta/abseta_pt_ratio");
            h2_id2    = (TH2D*)f_file4->Get("MC_NUM_TightID_DEN_genTracks_PAR_pt_eta/abseta_pt_ratio");
            h2_iso2    = (TH2D*)f_file4->Get("TightISO_TightID_pt_eta/abseta_pt_ratio");
        }
        else
        {
            h2_trigger= (TH2D*)f_file1->Get("probe_sc_abseta_probe_sc_pt_PLOT");
            h2_id1    = (TH2D*)f_file2->Get("EGamma_SF2D");
            h2_id2    = (TH2D*)f_file3->Get("EGamma_SF2D");
            h2_trk    = (TH2D*)f_file4->Get("EGamma_SF2D");
        }

    }


        ~POGSFsFiller()
        { 
        }

        void fill(const edm::Event& iEvent, const edm::EventSetup& iSetup)
        {

            float Trigger = 0;
            float TriggerErr = 0; float ID1=0; float ID1Err=0 ; float ID2=0; float ID2Err =0 ; float TRK=0; float TRKErr=0;
            edm::Handle<std::vector<T>> handle;
            if( iEvent.getByToken(src_,handle)){
                double pt = handle->at(0).leg1()->pt();
                double eta = handle->at(0).leg1()->eta();
                if (Mu_ ){ 
                    float period3 = h2_trigger->GetBinContent( h2_trigger->GetXaxis()->FindBin(std::abs(eta)), h2_trigger->GetYaxis()->FindBin(std::min(pt,499.)) );
                    float period4 = h2_trigger2->GetBinContent( h2_trigger2->GetXaxis()->FindBin(std::abs(eta)), h2_trigger2->GetYaxis()->FindBin(std::min(pt,499.)) );

                    Trigger = (period3*20.5 +period4*16.3)/36.8;

                    TriggerErr = h2_trigger2->GetBinError( h2_trigger2->GetXaxis()->FindBin(std::abs(eta)), h2_trigger2->GetYaxis()->FindBin(std::min(pt,499.)) );

                    float id1 = h2_id1->GetBinContent( h2_id1->GetXaxis()->FindBin(std::abs(eta)), h2_id1->GetYaxis()->FindBin(std::min(pt,499.)) );
                    float id2 = h2_id2->GetBinContent( h2_id2->GetXaxis()->FindBin(std::abs(eta)), h2_id2->GetYaxis()->FindBin(std::min(pt,499.)) );
                    ID1 = (id1*20.5+id2*16.3)/36.8;

                    ID1Err = h2_id1->GetBinError( h2_id1->GetXaxis()->FindBin(std::abs(eta)), h2_id1->GetYaxis()->FindBin(std::min(pt,499.)) );
                    float iso1 = h2_iso1->GetBinContent( h2_iso1->GetXaxis()->FindBin(std::abs(eta)), h2_iso1->GetYaxis()->FindBin(std::min(pt,499.)) );
                    float iso2 = h2_iso2->GetBinContent( h2_iso2->GetXaxis()->FindBin(std::abs(eta)), h2_iso2->GetYaxis()->FindBin(std::min(pt,499.)) );
                    ID2 = (iso1*20.5+iso2*16.3)/36.8; 

                    ID2Err = h2_id2->GetBinError( h2_id2->GetXaxis()->FindBin(std::abs(eta)), h2_id2->GetYaxis()->FindBin(std::min(pt,499.)) );
                    TRK = 1.0;
                    TRKErr = 1.0;
                }
                else{ 
                    Trigger = h2_trigger->GetBinContent( h2_trigger->GetXaxis()->FindBin(std::abs(eta)), h2_trigger->GetYaxis()->FindBin(std::min(pt,199.)) );
                    TriggerErr = h2_trigger->GetBinError( h2_trigger->GetXaxis()->FindBin(std::abs(eta)), h2_trigger->GetYaxis()->FindBin(std::min(pt,199.)) );
                    ID1 = h2_id1->GetBinContent( h2_id1->GetXaxis()->FindBin(eta), h2_id1->GetYaxis()->FindBin(std::min(pt,499.) ));
                    ID1Err = h2_id1->GetBinError( h2_id1->GetXaxis()->FindBin(eta), h2_id1->GetYaxis()->FindBin(std::min(pt,499.)) );
                    ID2 = h2_id2->GetBinContent( h2_id2->GetXaxis()->FindBin(eta), h2_id2->GetYaxis()->FindBin(std::min(pt,499.)) );
                    ID2Err = h2_id2->GetBinError( h2_id2->GetXaxis()->FindBin(eta), h2_id2->GetYaxis()->FindBin(std::min(pt,499.)) );
                    TRK = h2_trk->GetBinContent( h2_trk->GetXaxis()->FindBin(eta), 50.);
                    TRKErr = h2_trk->GetBinError( h2_trk->GetXaxis()->FindBin(eta), 50. );
                }
            }


            value[0]=Trigger;
            value[1]=TriggerErr;
            value[2]=ID1;
            value[3]=ID1Err;
            value[4]=ID2;
            value[5]=ID2Err;
            value[6]=TRK;
            value[7]=TRKErr;
        }


    protected:
        edm::EDGetTokenT<std::vector<T> > src_;
        std::string tag_;
        bool Mu_;
        bool isFile_;
        //std::vector<float> value;
        float* value;
        TFile *f_file1;
        TFile *f_file2;
        TFile *f_file3;
        TFile *f_file4;
        TH2D *h2_trigger;
        TH2D *h2_trigger2;
        TH2D *h2_id1;
        TH2D *h2_iso1;
        TH2D *h2_id2;
        TH2D *h2_iso2;
        TH2D *h2_trk;
        TH1F *h1_trk;


};

#include "MonoHTauTau/DataFormats/interface/CompositePtrCandidateT1T2MEt.h"
#include "MonoHTauTau/DataFormats/interface/CompositePtrCandidateTMEt.h"

typedef POGSFsFiller<PATMuTauPair> PATMuTauPairPOGSFsFiller;
typedef POGSFsFiller<PATElecTauPair> PATEleTauPairPOGSFsFiller;
typedef POGSFsFiller<PATMuTrackPair> PATMuTrackPairPOGSFsFiller;
typedef POGSFsFiller<PATEleTrackPair> PATEleTrackPairPOGSFsFiller;
