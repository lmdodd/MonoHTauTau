#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDProducer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/EventSetup.h"

#include "FWCore/MessageLogger/interface/MessageLogger.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Utilities/interface/InputTag.h"

#include "DataFormats/Common/interface/View.h"

#include "DataFormats/Math/interface/deltaR.h"
#include "DataFormats/PatCandidates/interface/PackedCandidate.h"


#include "MonoHTauTau/RecoTools/interface/FetchCollection.h"

#include "MonoHTauTau/DataFormats/interface/CompositePtrCandidateT1T2MEt.h"
#include "MonoHTauTau/DataFormats/interface/CompositePtrCandidateT1T2MEtFwd.h"

#include "MonoHTauTau/RecoTools/interface/candidateAuxFunctions.h"
#include "MonoHTauTau/RecoTools/interface/generalAuxFunctions.h"

template<typename T1, typename T2>
class MiniAODLeptonIso : public edm::EDProducer
{
  typedef edm::Ptr<T1> T1Ptr;
  typedef edm::Ptr<T2> T2Ptr;
  typedef std::vector<edm::Ptr<pat::Jet> > JetPtrVector;
  typedef std::vector<CompositePtrCandidateT1T2MEt<T1,T2> > CompositePtrCandidateCollection;

 public:

  explicit MiniAODLeptonIso(const edm::ParameterSet& cfg)
  {
    src_     = consumes<std::vector<CompositePtrCandidateT1T2MEt<T1,T2> > >(cfg.getParameter<edm::InputTag>("src"));
    pfToken_ = consumes<pat::PackedCandidateCollection>(edm::InputTag("packedPFCandidates"));

    produces<CompositePtrCandidateCollection>();
  }

  ~MiniAODLeptonIso(){}

  void beginJob()
  {

  }


  void produce(edm::Event& evt, const edm::EventSetup& es) {
    std::auto_ptr<CompositePtrCandidateCollection> out(new CompositePtrCandidateCollection);


    edm::Handle<std::vector<CompositePtrCandidateT1T2MEt<T1,T2> > > cands;

    if(evt.getByToken(src_,cands)) {

        for (unsigned int i=0;i<cands->size();++i) {

            CompositePtrCandidateT1T2MEt<T1,T2> compositePtrCandidate = cands->at(i);

            edm::Handle<pat::PackedCandidateCollection> pfs;
            evt.getByToken(pfToken_, pfs);



            // initialize sums
            double charged = 0, neutral = 0, pileup  = 0;
            // now get a list of the PF candidates used to build this compositePtrCandidate.leg1()ton, so to exclude them
            std::vector<reco::CandidatePtr> footprint;
            for (unsigned int i = 0, n = compositePtrCandidate.leg1()->numberOfSourceCandidatePtrs(); i < n; ++i) {
                footprint.push_back(compositePtrCandidate.leg1()->sourceCandidatePtr(i));
            }


            // now loop on pf candidates
            for (unsigned int i = 0, n = pfs->size(); i < n; ++i) {
                const pat::PackedCandidate &pf = (*pfs)[i];
                if (deltaR(pf,*compositePtrCandidate.leg1()) < 0.3) {
                    // pfcandidate-based footprint removal
                    //if (compositePtrCandidate.leg2()==reco::CandidatePtr(pfs,i)) std::cout<<"FOUND THE CHARGED PION"<<std::endl;
                    if (std::find(footprint.begin(), footprint.end(), reco::CandidatePtr(pfs,i)) != footprint.end()) {
                        continue;
                    }
                    if (pf.pt()==compositePtrCandidate.leg2()->pt()){ continue;}
                    if (pf.charge() == 0) {
                        if (pf.pt() > 0.5) neutral += pf.pt();
                    } 
                    else if (pf.fromPV() >= 2) {
                        charged += pf.pt();
                    } 
                    else {
                        if (pf.pt() > 0.5) pileup += pf.pt();
                    }
                }
            }
            // do deltaBeta
            double iso = charged + std::max(0.0, neutral-0.5*pileup);
            //double iso = charged; //+ std::max(0.0, neutral-0.5*pileup);
            //std::cout<<"Raw Combined Isolation: "<<iso<<" with relativeIsolation "<<iso/compositePtrCandidate.leg1()->pt()<<" with charged "<<charged<<" and neutral "<<neutral<<" and pileup "<<pileup<<std::endl;

            compositePtrCandidate.setLIso(iso);
            out->push_back(compositePtrCandidate);

        }
    }

    evt.put(out);
  }

 private:
  edm::EDGetTokenT<std::vector<CompositePtrCandidateT1T2MEt<T1,T2> > > src_;
  edm::EDGetTokenT<pat::PackedCandidateCollection> pfToken_;

};


