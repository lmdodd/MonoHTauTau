#include "FWCore/Framework/interface/MakerMacros.h"
#include "MonoHTauTau/NtupleTools/plugins/EventWeightFiller.h"

DEFINE_EDM_PLUGIN(NtupleFillerFactory, PATMuTauPairWeightFiller, "PATMuTauPairWeightFiller");
DEFINE_EDM_PLUGIN(NtupleFillerFactory, PATEleTauPairWeightFiller, "PATEleTauPairWeightFiller");
