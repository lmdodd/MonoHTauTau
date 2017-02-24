/*
 * Embeds the muon ID as recommended by the Muon POG
 * Author: Devin N. Taylor, UW-Madison
 */

// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDProducer.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"

#include "DataFormats/Common/interface/ValueMap.h"
#include "DataFormats/VertexReco/interface/Vertex.h"
#include "DataFormats/VertexReco/interface/VertexFwd.h"

#include "DataFormats/PatCandidates/interface/Muon.h"
#include "DataFormats/MuonReco/interface/MuonSelectors.h"

//#include <math.h>

// class declaration
class MiniAODMuonIDEmbedder : public edm::EDProducer {
    public:
        explicit MiniAODMuonIDEmbedder(const edm::ParameterSet& pset);
        virtual ~MiniAODMuonIDEmbedder(){}
        void produce(edm::Event& evt, const edm::EventSetup& es);
        bool isICHEPmedium(const reco::Muon & recoMu);
        bool is2016BCDEFmedium(const reco::Muon & recoMu);
        bool is2016GHmedium(const reco::Muon & recoMu);

    private:
        edm::EDGetTokenT<pat::MuonCollection> muonsCollection_;
        edm::EDGetTokenT<reco::VertexCollection> vtxToken_;
        reco::Vertex pv_;
};

bool MiniAODMuonIDEmbedder::isICHEPmedium(const reco::Muon & recoMu)
{
    // Fixes inefficiency due to HIP/(strip dynamic inefficiency)
    // https://twiki.cern.ch/twiki/bin/viewauth/CMS/SWGuideMuonIdRun2?Short_Term_Medium_Muon_Definitio=#Short_Term_Medium_Muon_Definitio
    bool goodGlob = recoMu.isGlobalMuon() &&
        recoMu.globalTrack()->normalizedChi2() < 3 &&
        recoMu.combinedQuality().chi2LocalPosition < 12 &&
        recoMu.combinedQuality().trkKink < 20;
    bool isMedium = muon::isLooseMuon(recoMu) &&
        recoMu.innerTrack()->validFraction() > 0.49 &&
        muon::segmentCompatibility(recoMu) > (goodGlob ? 0.303 : 0.451);
    return isMedium;
}

bool MiniAODMuonIDEmbedder::is2016BCDEFmedium(const reco::Muon & recoMu)
{
    bool goodGlob = recoMu.isGlobalMuon() && 
        recoMu.globalTrack()->normalizedChi2() < 3 && 
        recoMu.combinedQuality().chi2LocalPosition < 12 && 
        recoMu.combinedQuality().trkKink < 20; 
    bool isMedium = muon::isLooseMuon(recoMu) && 
        recoMu.innerTrack()->validFraction() > 0.49 && 
        muon::segmentCompatibility(recoMu) > (goodGlob ? 0.303 : 0.451); 
    return isMedium; 
}

bool MiniAODMuonIDEmbedder::is2016GHmedium(const reco::Muon & recoMu)
{
    bool goodGlob = recoMu.isGlobalMuon() && 
        recoMu.globalTrack()->normalizedChi2() < 3 && 
        recoMu.combinedQuality().chi2LocalPosition < 12 && 
        recoMu.combinedQuality().trkKink < 20; 
    bool isMedium = muon::isLooseMuon(recoMu) && 
        recoMu.innerTrack()->validFraction() > 0.8 && 
        muon::segmentCompatibility(recoMu) > (goodGlob ? 0.303 : 0.451); 
    return isMedium; 
}



// class member functions
MiniAODMuonIDEmbedder::MiniAODMuonIDEmbedder(const edm::ParameterSet& pset) {
    muonsCollection_ = consumes<pat::MuonCollection>(pset.getParameter<edm::InputTag>("src"));
    vtxToken_            = consumes<reco::VertexCollection>(pset.getParameter<edm::InputTag>("vertices"));

    produces<pat::MuonCollection>();
}

void MiniAODMuonIDEmbedder::produce(edm::Event& evt, const edm::EventSetup& es) {
    edm::Handle<std::vector<pat::Muon>> muonsCollection;
    evt.getByToken(muonsCollection_ , muonsCollection);

    edm::Handle<reco::VertexCollection> vertices;
    evt.getByToken(vtxToken_, vertices);
    if (vertices->empty()) return; // skip the event if no PV found
    pv_ = vertices->front();

    const std::vector<pat::Muon> * muons = muonsCollection.product();

    unsigned int nbMuon =  muons->size();

    std::auto_ptr<pat::MuonCollection> output(new pat::MuonCollection);
    output->reserve(nbMuon);

    //std::cout<<"NMuons: "<<nbMuon<<std::endl;
    for(unsigned i = 0 ; i < nbMuon; i++){
        pat::Muon muon(muons->at(i));
        //pat::Muon muon = muons->at(i);


        if(muon.muonBestTrack().isNonnull()) {
            float xy = muon.muonBestTrack()->dxy(vertices->at(0).position());
            float z = muon.muonBestTrack()->dz(vertices->at(0).position());
            muon.addUserFloat("dXY",xy); //bestTrack
            muon.addUserFloat("dZ",z); //bestTrack

        }
        else {
            muon.addUserFloat("dXY",-999.);
            muon.addUserFloat("dZ",-999.);
        }

        //std::cout<<"muon "<<i<<" pt: "<<muon.pt()<<std::endl;
        //std::cout<<"     isMediumMuon(): "<<muon::isMediumMuon(muon)<<std::endl;
        float muIso = (muon.pfIsolationR04().sumChargedHadronPt + std::max(
                    muon.pfIsolationR04().sumNeutralHadronEt +
                    muon.pfIsolationR04().sumPhotonEt - 
                    0.5 * muon.pfIsolationR04().sumPUPt, 0.0)) / muon.pt(); 
        //std::cout<<"     Muon Isolation04: "<<muIso<<std::endl;

        float muIso03 = (muon.pfIsolationR03().sumChargedHadronPt + std::max(
                    muon.pfIsolationR03().sumNeutralHadronEt +
                    muon.pfIsolationR03().sumPhotonEt - 
                    0.5 * muon.pfIsolationR03().sumPUPt, 0.0)) / muon.pt();

        //std::cout<<"     Muon Isolation03: "<<muIso03<<std::endl;

        int muId = 0; 
        //std::cout<<"     muID initialized to: "<<muId<<std::endl;
        //std::cout<<"     muon.globalTrack() isNonnull: "<<muon.globalTrack().isNonnull()<<std::endl;
        muId =MiniAODMuonIDEmbedder::is2016BCDEFmedium(muon); 

        int muTightId = 0; 
        muTightId = muon.isTightMuon(pv_);
        //std::cout<<"     muIDsetto: "<<muTightId<<std::endl;

        muon.addUserFloat("dBRelIso",muIso);
        muon.addUserFloat("iso",muIso);
        muon.addUserFloat("dBRelIso03",muIso03);
        muon.addUserInt("mediumID",muId);
        muon.addUserInt("tightID",muTightId);

        output->push_back(muon);
    }

    evt.put(output);
}

// define plugin
DEFINE_FWK_MODULE(MiniAODMuonIDEmbedder);
