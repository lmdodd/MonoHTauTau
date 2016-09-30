#!/bin/sh
voms-proxy-init --voms cms --valid 100:00


######HIGGS SAMPLES #############
#farmoutAnalysisJobs  $1 --vsize-limit=8000 --assume-input-files-exist --skip-existing-output --input-dbs-path=/GluGluHToTauTau_M125_13TeV_powheg_pythia8/RunIISpring16MiniAODv1-PUSpring16_MonoH_mcRun2_asymptotic_2016_v3-v1/MINIAODSIM  20160602_MonoH_ggHtautau_125 $CMSSW_BASE $CMSSW_BASE/src/MonoHTauTau/CRAB/ZTT_25ns/SUB-MC.py
#ggH
#farmoutAnalysisJobs  $1 --vsize-limit=8000 --assume-input-files-exist --skip-existing-output --input-dbs-path=/GluGluHToTauTau_M125_13TeV_powheg_pythia8/RunIISpring16MiniAODv1-PUSpring16_MonoH_mcRun2_asymptotic_2016_v3-v1/MINIAODSIM  20160602_MonoH_ggHtautau_125 $CMSSW_BASE $CMSSW_BASE/src/MonoHTauTau/CRAB/ZTT_25ns/SUB-MC.py
#farmoutAnalysisJobs  $1 --vsize-limit=8000 --assume-input-files-exist --skip-existing-output --input-dbs-path=/VBFHToTauTau_M125_13TeV_powheg_pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_reHLT_MonoH_mcRun2_asymptotic_v14-v1/MINIAODSIM  20160728_MonoH_vbfHtautau_125 $CMSSW_BASE $CMSSW_BASE/src/MonoHTauTau/CRAB/ZTT_25ns/SUB-MC-HLT2.py
#farmoutAnalysisJobs  $1 --vsize-limit=8000 --assume-input-files-exist --skip-existing-output --input-dbs-path=/SUSYGluGluToHToTauTau_M-200_TuneCUETP8M1_13TeV-pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_reHLT_MonoH_mcRun2_asymptotic_v14-v1/MINIAODSIM  20160728_MonoH_SUSY200_125 $CMSSW_BASE $CMSSW_BASE/src/MonoHTauTau/CRAB/XTT_25ns/SUB-MC-HLT2.py
#farmoutAnalysisJobs  $1 --vsize-limit=8000 --assume-input-files-exist --skip-existing-output --input-dbs-path=/SUSYGluGluToHToTauTau_M-450_TuneCUETP8M1_13TeV-pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_reHLT_MonoH_mcRun2_asymptotic_v14-v1/MINIAODSIM  20160728_MonoH_SUSY450_125 $CMSSW_BASE $CMSSW_BASE/src/MonoHTauTau/CRAB/XTT_25ns/SUB-MC-HLT2.py
#
#farmoutAnalysisJobs  $1 --vsize-limit=8000 --assume-input-files-exist --skip-existing-output --input-dbs-path=/SUSYGluGluToHToTauTau_M-130_TuneCUETP8M1_13TeV-pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_reHLT_MonoH_mcRun2_asymptotic_v14-v1/MINIAODSIM 20160602_MonoH_susy_130 $CMSSW_BASE $CMSSW_BASE/src/MonoHTauTau/CRAB/ZTT_25ns/SUB-MC.py
#farmoutAnalysisJobs  $1 --vsize-limit=8000 --assume-input-files-exist --skip-existing-output --input-dbs-path=/SUSYGluGluToHToTauTau_M-130_TuneCUETP8M1_13TeV-pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_reHLT_MonoH_mcRun2_asymptotic_v14-v1/MINIAODSIM 20160602_MonoH_susy_130 $CMSSW_BASE $CMSSW_BASE/src/MonoHTauTau/CRAB/ZTT_25ns/SUB-MC.py

