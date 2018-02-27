import os
import subprocess
import re


name = '20180227_v1'
projectName = 'HTT_PLAYPEN'

dataset = [
        '/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM',
        '/ttHJetToNonbb_M125_13TeV_amcatnloFXFX_madspin_pythia8_mWCutfix/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/MINIAODSIM'
]


def submit(sample, requestName, filesPerJob):
    res = 'farmoutAnalysisJobs $1 --vsize-limit=8000 --skip-existing-output --assume-input-files-exist --input-files-per-job='+filesPerJob+' --input-dbs-path='+sample+' '+requestName+' $CMSSW_BASE $CMSSW_BASE/src/MonoHTauTau/CRAB/XTT_CONDOR/SUB-MC.py'
    os.system(res)
    #os.system(res)

psetName = 'SUB-MC.py'
#config.JobType.inputFiles = ["%s/src/MonoHTauTau/Configuration/data" % os.environ["CMSSW_BASE"]]
for sample in dataset:
  (_, primaryDS, conditions, dataTier) = sample.split('/')
  print 'submitting %s' % primaryDS
  requestName = '_'.join([projectName,name, primaryDS])
  #if len(requestName)>90:
  #    print 'rename sample %s... more than 100 characters' % requestName
  #    requestName = requestName[:90]
  #    print 'submitting name as %s' % requestName

  m = re.match(r".*(_ext[0-9]*)-", conditions)
  if m:
      requestName += m.groups()[0]



  inputDataset = sample 
  filesPerJob = '10'
  submit(inputDataset, requestName, filesPerJob)
