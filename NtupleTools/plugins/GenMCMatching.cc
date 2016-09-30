#include "FWCore/Framework/interface/MakerMacros.h"
#include "MonoHTauTau/NtupleTools/plugins/GenMCMatching.h"

DEFINE_EDM_PLUGIN(NtupleFillerFactory, PATMuTauPairGenMCMatching, "PATMuTauPairGenMCMatching");
DEFINE_EDM_PLUGIN(NtupleFillerFactory, PATEleTauPairGenMCMatching, "PATEleTauPairGenMCMatching");
DEFINE_EDM_PLUGIN(NtupleFillerFactory, PATDiTauPairGenMCMatching, "PATDiTauPairGenMCMatching");

