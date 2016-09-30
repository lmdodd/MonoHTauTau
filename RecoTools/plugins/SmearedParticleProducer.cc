#include "MonoHTauTau/RecoTools/plugins/SmearedParticleProducer.h"
#include "FWCore/Framework/interface/MakerMacros.h"
typedef SmearedParticleProducer<pat::Muon,GenParticleRetriever<pat::Muon> > SmearedMuonProducer;
typedef SmearedParticleProducer<pat::Electron,GenParticleRetriever<pat::Electron> > SmearedElectronProducer;
typedef SmearedParticleProducer<pat::PackedCandidate,GenTrackRetriever<pat::PackedCandidate> > SmearedTrackProducer;
 
DEFINE_FWK_MODULE(SmearedMuonProducer);
DEFINE_FWK_MODULE(SmearedElectronProducer);
DEFINE_FWK_MODULE(SmearedTrackProducer);
