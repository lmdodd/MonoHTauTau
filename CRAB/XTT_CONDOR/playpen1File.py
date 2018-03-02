import os
import subprocess
import re


name = '20180302_v1'
projectName = 'HTT_PLAYPEN'

dataset = [
     '/QCD_Pt-120to170_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM'
]


def submit(sample, requestName, filesPerJob):
    res = 'farmoutAnalysisJobs $1 --vsize-limit=4000 --assume-input-files-exist --input-files-per-job='+filesPerJob+' --input-dbs-path='+sample+' '+requestName+' $CMSSW_BASE $CMSSW_BASE/src/MonoHTauTau/CRAB/XTT_CONDOR/SUB-MC.py'
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
