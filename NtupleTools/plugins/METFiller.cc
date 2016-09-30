#include "FWCore/Framework/interface/MakerMacros.h"
#include "MonoHTauTau/NtupleTools/plugins/METFiller.h"

DEFINE_EDM_PLUGIN(NtupleFillerFactory, PATMuTauPairMETFiller, "PATMuTauPairMETFiller");
DEFINE_EDM_PLUGIN(NtupleFillerFactory, PATEleTauPairMETFiller, "PATEleTauPairMETFiller");
DEFINE_EDM_PLUGIN(NtupleFillerFactory, PATDiTauPairMETFiller, "PATDiTauPairMETFiller");
DEFINE_EDM_PLUGIN(NtupleFillerFactory, PATMuTrackPairMETFiller, "PATMuTrackPairMETFiller");
DEFINE_EDM_PLUGIN(NtupleFillerFactory, PATEleTrackPairMETFiller, "PATEleTrackPairMETFiller");
