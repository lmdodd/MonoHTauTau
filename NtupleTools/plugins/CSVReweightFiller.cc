#include "FWCore/Framework/interface/MakerMacros.h"
#include "MonoHTauTau/NtupleTools/plugins/CSVReweightFiller.h"

DEFINE_EDM_PLUGIN(NtupleFillerFactory, PATMuTauPairCSVReweightFiller, "PATMuTauPairCSVReweightFiller");
DEFINE_EDM_PLUGIN(NtupleFillerFactory, PATEleTauPairCSVReweightFiller, "PATEleTauPairCSVReweightFiller");
DEFINE_EDM_PLUGIN(NtupleFillerFactory, PATDiTauPairCSVReweightFiller, "PATDiTauPairCSVReweightFiller");
