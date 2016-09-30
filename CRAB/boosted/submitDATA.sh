#!/bin/sh
voms-proxy-init --voms cms --valid 100:00

#Submit the reprocessed Data
#/cms/sw/farmout/farmoutAnalysisJobs.fix  $1 --assume-input-files-exist --skip-existing-output  --vsize-limit=8000  --input-files-per-job=1 --input-dbs-path=/SingleMuon/Run2016B-PromptReco-v2/MINIAOD SINGLEMUON2016B_BOOST_Aug21 $CMSSW_BASE $CMSSW_BASE/src/UWAnalysis/CRAB/boosted/SUB-JSON.py  
#/cms/sw/farmout/farmoutAnalysisJobs.fix  $1  --assume-input-files-exist --skip-existing-output  --vsize-limit=8000   --input-files-per-job=1 --input-dbs-path=/SingleMuon/Run2016C-PromptReco-v2/MINIAOD SINGLEMUON2016C_BOOST_Aug21 $CMSSW_BASE $CMSSW_BASE/src/UWAnalysis/CRAB/boosted/SUB-JSON.py  
#/cms/sw/farmout/farmoutAnalysisJobs.fix  $1  --assume-input-files-exist --skip-existing-output  --vsize-limit=8000   --input-files-per-job=1 --input-dbs-path=/SingleMuon/Run2016D-PromptReco-v2/MINIAOD SINGLEMUON2016D_BOOST_Aug21 $CMSSW_BASE $CMSSW_BASE/src/UWAnalysis/CRAB/boosted/SUB-JSON.py  

/cms/sw/farmout/farmoutAnalysisJobs.fix  $1  --assume-input-files-exist --skip-existing-output  --vsize-limit=8000   --input-files-per-job=1 --input-dbs-path=/SingleElectron/Run2016B-PromptReco-v2/MINIAOD SINGLEELE2016B_BOOST_Aug21 $CMSSW_BASE $CMSSW_BASE/src/UWAnalysis/CRAB/boosted/SUB-JSON.py  
/cms/sw/farmout/farmoutAnalysisJobs.fix  $1  --assume-input-files-exist --skip-existing-output  --vsize-limit=8000   --input-files-per-job=1 --input-dbs-path=/SingleElectron/Run2016C-PromptReco-v2/MINIAOD SINGLEELE2016C_BOOST_Aug21 $CMSSW_BASE $CMSSW_BASE/src/UWAnalysis/CRAB/boosted/SUB-JSON.py  
/cms/sw/farmout/farmoutAnalysisJobs.fix  $1  --assume-input-files-exist --skip-existing-output  --vsize-limit=8000   --input-files-per-job=1 --input-dbs-path=/SingleElectron/Run2016D-PromptReco-v2/MINIAOD SINGLEELE2016D_BOOST_Aug21 $CMSSW_BASE $CMSSW_BASE/src/UWAnalysis/CRAB/boosted/SUB-JSON.py  

#/cms/sw/farmout/farmoutAnalysisJobs.fix  $1  --assume-input-files-exist --skip-existing-output  --vsize-limit=8000   --input-files-per-job=1 --input-dbs-path=/Tau/Run2016B-PromptReco-v2/MINIAOD TAU2016B_BOOST_Aug21 $CMSSW_BASE $CMSSW_BASE/src/UWAnalysis/CRAB/boosted/SUB-JSON.py  
#/cms/sw/farmout/farmoutAnalysisJobs.fix  $1  --assume-input-files-exist --skip-existing-output  --vsize-limit=8000   --input-files-per-job=1 --input-dbs-path=/Tau/Run2016C-PromptReco-v2/MINIAOD TAU2016C_BOOST_Aug21 $CMSSW_BASE $CMSSW_BASE/src/UWAnalysis/CRAB/boosted/SUB-JSON.py  
#/cms/sw/farmout/farmoutAnalysisJobs.fix  $1  --assume-input-files-exist --skip-existing-output  --vsize-limit=8000   --input-files-per-job=1 --input-dbs-path=/Tau/Run2016D-PromptReco-v2/MINIAOD TAU2016D_BOOST_Aug21 $CMSSW_BASE $CMSSW_BASE/src/UWAnalysis/CRAB/boosted/SUB-JSON.py  
