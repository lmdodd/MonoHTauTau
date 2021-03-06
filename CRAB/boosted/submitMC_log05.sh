#!/bin/sh
voms-proxy-init --voms cms --valid 100:00


######HIGGS SAMPLES #############
#ggH
/cms/sw/farmout/farmoutAnalysisJobs.fix  $1 --vsize-limit=8000 --skip-existing-output  --assume-input-files-exist  --input-dbs-path=/GluGluHToTauTau_M125_13TeV_powheg_pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/MINIAODSIM  20161128_boosted_ggHtautau_125 $CMSSW_BASE $CMSSW_BASE/src/MonoHTauTau/CRAB/boosted/SUB-MC-HLT2.py
/cms/sw/farmout/farmoutAnalysisJobs.fix  $1 --vsize-limit=8000 --skip-existing-output --assume-input-files-exist   --input-dbs-path=/VBFHToTauTau_M125_13TeV_powheg_pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/MINIAODSIM  20161128_boosted_vbfHtautau_125 $CMSSW_BASE $CMSSW_BASE/src/MonoHTauTau/CRAB/boosted/SUB-MC-HLT2.py

############ZH#################
/cms/sw/farmout/farmoutAnalysisJobs.fix $1 --vsize-limit=8000 --skip-existing-output  --assume-input-files-exist --skip-existing-output --input-dbs-path=/ZHToTauTau_M125_13TeV_powheg_pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/MINIAODSIM 20161128_boosted_ZHtautau_125 $CMSSW_BASE $CMSSW_BASE/src/MonoHTauTau/CRAB/boosted/SUB-MC-HLT2.py  

########ZJETS SAMPLES#############
#/cms/sw/farmout/farmoutAnalysisJobs.fix $1 --vsize-limit=8000 --skip-existing-output  --assume-input-files-exist  --input-dbs-path=/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv1-PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/MINIAODSIM 20161128_boosted_ZJets $CMSSW_BASE $CMSSW_BASE/src/MonoHTauTau/CRAB/boosted/SUB-MC.py  
/cms/sw/farmout/farmoutAnalysisJobs.fix $1 --vsize-limit=8000 --skip-existing-output  --assume-input-files-exist  --input-dbs-path=/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_80X_mcRun2_asymptotic_2016_miniAODv2_v0_ext1-v1/MINIAODSIM 20161128_boosted_ZJets_ext $CMSSW_BASE $CMSSW_BASE/src/MonoHTauTau/CRAB/boosted/SUB-MC.py  

/cms/sw/farmout/farmoutAnalysisJobs.fix $1 --vsize-limit=8000 --skip-existing-output  --assume-input-files-exist  --input-dbs-path=/DY1JetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM 20161128_boosted_Z1Jets $CMSSW_BASE $CMSSW_BASE/src/MonoHTauTau/CRAB/boosted/SUB-MC.py  
/cms/sw/farmout/farmoutAnalysisJobs.fix $1 --vsize-limit=8000 --skip-existing-output  --assume-input-files-exist  --input-dbs-path=/DY2JetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM 20161128_boosted_Z2Jets $CMSSW_BASE $CMSSW_BASE/src/MonoHTauTau/CRAB/boosted/SUB-MC.py  
/cms/sw/farmout/farmoutAnalysisJobs.fix $1 --vsize-limit=8000 --skip-existing-output  --assume-input-files-exist  --input-dbs-path=/DY3JetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM 20161128_boosted_Z3Jets $CMSSW_BASE $CMSSW_BASE/src/MonoHTauTau/CRAB/boosted/SUB-MC.py  
/cms/sw/farmout/farmoutAnalysisJobs.fix $1 --vsize-limit=8000 --skip-existing-output  --assume-input-files-exist  --input-dbs-path=/DY4JetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM 20161128_boosted_Z4Jets $CMSSW_BASE $CMSSW_BASE/src/MonoHTauTau/CRAB/boosted/SUB-MC.py  

/cms/sw/farmout/farmoutAnalysisJobs.fix $1 --vsize-limit=8000 --skip-existing-output  --assume-input-files-exist  --input-dbs-path=/DYJetsToLL_M-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM 20161128_boosted_ZJets_150 $CMSSW_BASE $CMSSW_BASE/src/MonoHTauTau/CRAB/boosted/SUB-MC.py  

########TT SAMPLES################
/cms/sw/farmout/farmoutAnalysisJobs.fix $1 --vsize-limit=8000 --skip-existing-output  --assume-input-files-exist  --input-files-per-job=1 --input-dbs-path=/TT_TuneCUETP8M1_13TeV-powheg-pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14_ext3-v1/MINIAODSIM 20161128_boosted_TT $CMSSW_BASE $CMSSW_BASE/src/MonoHTauTau/CRAB/boosted/SUB-MC-HLT2.py  
#/cms/sw/farmout/farmoutAnalysisJobs.fix $1 --vsize-limit=8000 --skip-existing-output  --assume-input-files-exist  --input-files-per-job=1 --input-dbs-path=/TTJets_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM 20161128_boosted_TTJets $CMSSW_BASE $CMSSW_BASE/src/MonoHTauTau/CRAB/boosted/SUB-MC.py  

