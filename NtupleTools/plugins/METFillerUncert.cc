#include "FWCore/Framework/interface/MakerMacros.h"
#include "MonoHTauTau/NtupleTools/plugins/METFillerUncert.h"

DEFINE_EDM_PLUGIN(NtupleFillerFactory, PATMuTauPairMETFillerUncert, "PATMuTauPairMETFillerUncert");
DEFINE_EDM_PLUGIN(NtupleFillerFactory, PATEleTauPairMETFillerUncert, "PATEleTauPairMETFillerUncert");
DEFINE_EDM_PLUGIN(NtupleFillerFactory, PATDiTauPairMETFillerUncert, "PATDiTauPairMETFillerUncert");
DEFINE_EDM_PLUGIN(NtupleFillerFactory, PATMuTrackPairMETFillerUncert, "PATMuTrackPairMETFillerUncert");
DEFINE_EDM_PLUGIN(NtupleFillerFactory, PATEleTrackPairMETFillerUncert, "PATEleTrackPairMETFillerUncert");
