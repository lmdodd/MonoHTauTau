#include "MonoHTauTau/RecoTools/plugins/MiniAODLeptonVeto.h"

#include "FWCore/Framework/interface/MakerMacros.h"

#include "DataFormats/Candidate/interface/Candidate.h"
#include "DataFormats/PatCandidates/interface/Muon.h"
#include "DataFormats/PatCandidates/interface/Electron.h"
#include "DataFormats/PatCandidates/interface/Tau.h"
#include "DataFormats/PatCandidates/interface/PackedCandidate.h"



typedef MiniAODLeptonVeto<pat::Muon, pat::Tau> PATMuTauLVeto;
typedef MiniAODLeptonVeto<pat::Electron, pat::Tau> PATElecTauLVeto;
typedef MiniAODLeptonVeto<pat::Tau, pat::Tau> PATDiTauLVeto;
typedef MiniAODLeptonVeto<pat::Electron, pat::PackedCandidate> PATEleTrackLVeto;
typedef MiniAODLeptonVeto<pat::Muon, pat::PackedCandidate> PATMuTrackLVeto;



DEFINE_FWK_MODULE(PATMuTauLVeto);
DEFINE_FWK_MODULE(PATElecTauLVeto);
DEFINE_FWK_MODULE(PATDiTauLVeto);
DEFINE_FWK_MODULE(PATEleTrackLVeto);
DEFINE_FWK_MODULE(PATMuTrackLVeto);

