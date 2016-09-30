#include "FWCore/Framework/interface/MakerMacros.h"
#include "MonoHTauTau/NtupleTools/plugins/POGSFsFiller.h"

DEFINE_EDM_PLUGIN(NtupleFillerFactory, PATMuTauPairPOGSFsFiller, "PATMuTauPairPOGSFsFiller");
DEFINE_EDM_PLUGIN(NtupleFillerFactory, PATEleTauPairPOGSFsFiller, "PATEleTauPairPOGSFsFiller");
DEFINE_EDM_PLUGIN(NtupleFillerFactory, PATMuTrackPairPOGSFsFiller, "PATMuTrackPairPOGSFsFiller");
DEFINE_EDM_PLUGIN(NtupleFillerFactory, PATEleTrackPairPOGSFsFiller, "PATEleTrackPairPOGSFsFiller");
