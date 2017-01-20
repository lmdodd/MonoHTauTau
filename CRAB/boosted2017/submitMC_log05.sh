#!/bin/sh
voms-proxy-init --voms cms --valid 100:00


######HIGGS SAMPLES #############
#ggH
farmoutAnalysisJobs  $1 --vsize-limit=8000 --assume-input-files-exist   --input-dbs-path=/GluGluHToTauTau_M125_13TeV_powheg_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM  20170116_boosted_ggHtautau_125 $CMSSW_BASE $CMSSW_BASE/src/MonoHTauTau/CRAB/boosted2017/SUB-MC.py
farmoutAnalysisJobs  $1 --vsize-limit=8000 --assume-input-files-exist   --input-dbs-path=/VBFHToTauTau_M125_13TeV_powheg_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM  20170116_boosted_vbfHtautau_125 $CMSSW_BASE $CMSSW_BASE/src/MonoHTauTau/CRAB/boosted2017/SUB-MC.py

############ZH#################
farmoutAnalysisJobs $1 --vsize-limit=8000  --assume-input-files-exist   --input-dbs-path=/ZHToTauTau_M125_13TeV_powheg_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM 20170116_boosted_ZHtautau_125 $CMSSW_BASE $CMSSW_BASE/src/MonoHTauTau/CRAB/boosted2017/SUB-MC.py  


########ZJETS SAMPLES#############
farmoutAnalysisJobs $1 --vsize-limit=8000 --assume-input-files-exist   --input-dbs-path=/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v2/MINIAODSIM 20170116_boosted_ZJets_ext $CMSSW_BASE $CMSSW_BASE/src/MonoHTauTau/CRAB/boosted2017/SUB-MC.py  

farmoutAnalysisJobs $1 --vsize-limit=8000 --assume-input-files-exist   --input-dbs-path=/DY1JetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM 20170116_boosted_Z1Jets $CMSSW_BASE $CMSSW_BASE/src/MonoHTauTau/CRAB/boosted2017/SUB-MC.py  

farmoutAnalysisJobs $1 --vsize-limit=8000 --assume-input-files-exist   --input-dbs-path=/DY2JetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM 20170116_boosted_Z2Jets $CMSSW_BASE $CMSSW_BASE/src/MonoHTauTau/CRAB/boosted2017/SUB-MC.py  

farmoutAnalysisJobs $1 --vsize-limit=8000 --assume-input-files-exist   --input-dbs-path=/DY3JetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM 20170116_boosted_Z3Jets $CMSSW_BASE $CMSSW_BASE/src/MonoHTauTau/CRAB/boosted2017/SUB-MC.py  
farmoutAnalysisJobs $1 --vsize-limit=8000 --assume-input-files-exist   --input-dbs-path=/DY4JetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM 20170116_boosted_Z4Jets $CMSSW_BASE $CMSSW_BASE/src/MonoHTauTau/CRAB/boosted2017/SUB-MC.py  

#farmoutAnalysisJobs $1 --vsize-limit=8000 --assume-input-files-exist   --input-dbs-path=/DYJetsToLL_M-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM 20170116_boosted_ZJets_150 $CMSSW_BASE $CMSSW_BASE/src/MonoHTauTau/CRAB/boosted2017/SUB-MC.py  

########TT SAMPLES################
farmoutAnalysisJobs $1 --vsize-limit=8000 --assume-input-files-exist   --input-files-per-job=1 --input-dbs-path=/TT_TuneCUETP8M2T4_13TeV-powheg-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM 20170116_boosted_TT $CMSSW_BASE $CMSSW_BASE/src/MonoHTauTau/CRAB/boosted2017/SUB-MC.py  

farmoutAnalysisJobs $1 --vsize-limit=8000 --assume-input-files-exist   --input-files-per-job=1 --input-dbs-path=/TT_TuneCUETP8M2T4_13TeV-powheg-pythia8/RunIISummer16MiniAODv2-PUMoriond17_backup_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM 20170116_boosted_TT_backup $CMSSW_BASE $CMSSW_BASE/src/MonoHTauTau/CRAB/boosted2017/SUB-MC.py  

