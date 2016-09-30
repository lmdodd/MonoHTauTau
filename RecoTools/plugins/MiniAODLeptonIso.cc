#include "MonoHTauTau/RecoTools/plugins/MiniAODLeptonIso.h"

#include "FWCore/Framework/interface/MakerMacros.h"

#include "DataFormats/Candidate/interface/Candidate.h"
#include "DataFormats/PatCandidates/interface/Muon.h"
#include "DataFormats/PatCandidates/interface/Electron.h"
#include "DataFormats/PatCandidates/interface/Tau.h"
#include "DataFormats/PatCandidates/interface/PackedCandidate.h"



typedef MiniAODLeptonIso<pat::Muon, pat::Tau> PATMuTauLeptonIso;
typedef MiniAODLeptonIso<pat::Electron, pat::Tau> PATElecTauLeptonIso;
typedef MiniAODLeptonIso<pat::Electron, pat::PackedCandidate> PATEleTrackLeptonIso;
typedef MiniAODLeptonIso<pat::Muon, pat::PackedCandidate> PATMuTrackLeptonIso;



DEFINE_FWK_MODULE(PATMuTauLeptonIso);
DEFINE_FWK_MODULE(PATElecTauLeptonIso);
DEFINE_FWK_MODULE(PATEleTrackLeptonIso);
DEFINE_FWK_MODULE(PATMuTrackLeptonIso);

