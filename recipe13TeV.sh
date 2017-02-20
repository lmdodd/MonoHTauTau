#!/bin/bash

pushd $CMSSW_BASE/src

pushd $CMSSW_BASE/src
git clone https://github.com/CMS-HTT/LeptonEff-interface.git HTT-utilities 
cd HTT-utilities/LepEffInterface/
git clone https://github.com/CMS-HTT/LeptonEfficiencies.git data 

pushd $CMSSW_BASE/src
git clone https://github.com/CMS-HTT/RecoilCorrections.git  HTT-utilities/RecoilCorrections 

pushd $CMSSW_BASE/src

git cms-merge-topic ikrav:egm_id_80X_v2
git cms-merge-topic cms-met:METRecipe_8020 -u
#git cms-merge-topic -u cms-met:fromCMSSW_8_0_20_postICHEPfilter
#git cms-merge-topic gpetruc:badMuonFilters_80X_v2

#METSignificance
#git cms-addpkg RecoMET/METProducers

