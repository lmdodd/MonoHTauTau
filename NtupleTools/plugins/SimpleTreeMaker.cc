#include "FWCore/Framework/interface/MakerMacros.h"
#include "MonoHTauTau/NtupleTools/plugins/SimpleTreeMaker.h"
#include "MonoHTauTau/DataFormats/interface/CompositePtrCandidateTMEt.h"
#include "MonoHTauTau/DataFormats/interface/CompositePtrCandidateTMEtFwd.h"
#include "MonoHTauTau/DataFormats/interface/CompositePtrCandidateT1T2MEt.h"
#include "MonoHTauTau/DataFormats/interface/CompositePtrCandidateT1T2MEtFwd.h"


typedef SimpleTreeMaker<pat::Tau> PATTauTree;


DEFINE_FWK_MODULE(PATTauTree);

