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

#METSignificance
#git cms-addpkg RecoMET/METProducers

