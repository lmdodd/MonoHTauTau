#!/bin/sh
voms-proxy-init --voms cms --valid 100:00



########ZJETS SAMPLES#############
farmoutAnalysisJobs $1 --vsize-limit=8000 --assume-input-files-exist   --input-dbs-path=/ZprimeToA0hToA0chichihtautau_2HDM_MZp-1200_MA0-300_13TeV-madgraph-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM 20170502_MonoH_ZPrime1200_A300 $CMSSW_BASE $CMSSW_BASE/src/MonoHTauTau/CRAB/XTT_UGH/SUB-MC-noTES.py  

