#!/bin/sh
voms-proxy-init --voms cms --valid 100:00


###########WZ SAMPLES#############
farmoutAnalysisJobs $1 --vsize-limit=8000 --assume-input-files-exist   --input-files-per-job=2 --input-dbs-path=/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM  20170116_boosted_WZTo1L3Nu $CMSSW_BASE $CMSSW_BASE/src/MonoHTauTau/CRAB/boosted2017/SUB-MC.py  
farmoutAnalysisJobs $1 --vsize-limit=8000 --assume-input-files-exist   --input-files-per-job=2 --input-dbs-path=/WZTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/MINIAODSIM 20170116_boosted_WZTo1L1Nu2Q $CMSSW_BASE $CMSSW_BASE/src/MonoHTauTau/CRAB/boosted2017/SUB-MC.py  
#farmoutAnalysisJobs $1 --vsize-limit=8000 --assume-input-files-exist   --input-files-per-job=2 --input-dbs-path=/WZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM 20170116_boosted_WZTo2L2Q $CMSSW_BASE $CMSSW_BASE/src/MonoHTauTau/CRAB/boosted2017/SUB-MC.py  


##########SINGLE TOP SAMPLES#############
farmoutAnalysisJobs $1 --vsize-limit=8000 --assume-input-files-exist   --input-dbs-path=/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/MINIAODSIM 20170116_boosted_tBar_tW $CMSSW_BASE $CMSSW_BASE/src/MonoHTauTau/CRAB/boosted2017/SUB-MC.py  
farmoutAnalysisJobs $1 --vsize-limit=8000 --assume-input-files-exist   --input-dbs-path=/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/MINIAODSIM 20170116_boosted_t_tW $CMSSW_BASE $CMSSW_BASE/src/MonoHTauTau/CRAB/boosted2017/SUB-MC.py  
farmoutAnalysisJobs $1 --vsize-limit=8000 --assume-input-files-exist   --input-dbs-path=/ST_t-channel_antitop_4f_inclusiveDecays_13TeV-powhegV2-madspin-pythia8_TuneCUETP8M1/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM 20170116_boosted_St_t_antitop $CMSSW_BASE $CMSSW_BASE/src/MonoHTauTau/CRAB/boosted2017/SUB-MC.py  
farmoutAnalysisJobs $1 --vsize-limit=8000 --assume-input-files-exist   --input-dbs-path=/ST_t-channel_top_4f_inclusiveDecays_13TeV-powhegV2-madspin-pythia8_TuneCUETP8M1/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM 20170116_boosted_St_t_top $CMSSW_BASE $CMSSW_BASE/src/MonoHTauTau/CRAB/boosted2017/SUB-MC.py  

###########WW SAMPLES#############
farmoutAnalysisJobs $1 --vsize-limit=8000 --assume-input-files-exist    --input-files-per-job=2 --input-dbs-path=/WWToLNuQQ_13TeV-powheg/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM  20170116_boosted_WWTo1L1Nu2Q $CMSSW_BASE $CMSSW_BASE/src/MonoHTauTau/CRAB/boosted2017/SUB-MC.py  
farmoutAnalysisJobs $1 --vsize-limit=8000 --assume-input-files-exist    --input-files-per-job=2 --input-dbs-path=/WWToLNuQQ_13TeV-powheg/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/MINIAODSIM  20170116_boosted_WWTo1L1Nu2Q_ext $CMSSW_BASE $CMSSW_BASE/src/MonoHTauTau/CRAB/boosted2017/SUB-MC.py  

###########ZZ SAMPLES#############

farmoutAnalysisJobs $1 --vsize-limit=8000 --assume-input-files-exist   --input-files-per-job=2 --input-dbs-path=/ZZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM 20170116_boosted_ZZTo2L2Q $CMSSW_BASE $CMSSW_BASE/src/MonoHTauTau/CRAB/boosted2017/SUB-MC.py  
farmoutAnalysisJobs $1 --vsize-limit=8000 --assume-input-files-exist   --input-files-per-job=2 --input-dbs-path=/ZZTo2Q2Nu_13TeV_amcatnloFXFX_madspin_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM 20170116_boosted_ZZTo2Q2Nu $CMSSW_BASE $CMSSW_BASE/src/MonoHTauTau/CRAB/boosted2017/SUB-MC.py  

###########VV SAMPLES#############
farmoutAnalysisJobs $1 --vsize-limit=8000 --assume-input-files-exist   --input-files-per-job=2 --input-dbs-path=/VVTo2L2Nu_13TeV_amcatnloFXFX_madspin_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM 20170116_boosted_VVTo2L2Nu $CMSSW_BASE $CMSSW_BASE/src/MonoHTauTau/CRAB/boosted2017/SUB-MC.py  
