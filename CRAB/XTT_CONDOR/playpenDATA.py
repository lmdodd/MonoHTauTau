import os
import re

name = '20180302_v1'
projectName = 'HTT_PLAYPEN'


dataset = [
        '/SingleMuon/Run2016H-03Feb2017_ver3-v1/MINIAOD',
        '/SingleMuon/Run2016H-03Feb2017_ver2-v1/MINIAOD',
        '/SingleMuon/Run2016G-03Feb2017-v1/MINIAOD',
        '/SingleMuon/Run2016B-03Feb2017_ver2-v2/MINIAOD',
        '/SingleMuon/Run2016C-03Feb2017-v1/MINIAOD',
        '/SingleMuon/Run2016D-03Feb2017-v1/MINIAOD',
        '/SingleMuon/Run2016E-03Feb2017-v1/MINIAOD',
        '/SingleMuon/Run2016F-03Feb2017-v1/MINIAOD'
]


def submit(sample, requestName, filesPerJob,fileToUse):
    res = 'farmoutAnalysisJobs $1 --vsize-limit=8000 --assume-input-files-exist --input-files-per-job='+filesPerJob+' --input-dbs-path='+sample+' '+requestName+' $CMSSW_BASE $CMSSW_BASE/src/MonoHTauTau/CRAB/XTT_CONDOR/'+fileToUse
    os.system(res)

psetName = 'SUB-JSON-Boost.py'
#config.JobType.inputFiles = ["%s/src/MonoHTauTau/Configuration/data" % os.environ["CMSSW_BASE"]]
for sample in dataset:
  (_, primaryDS, conditions, dataTier) = sample.split('/')
  print 'submitting %s' % primaryDS
  requestName = '_'.join([projectName,name, primaryDS,conditions])
  m = re.match(r".*(_ext[0-9]*)-", conditions)
  if m:
      requestName += m.groups()[0]

  if len(requestName)>100:
      print 'rename sample %s... more than 100 characters' % requestName
      requestName = requestName[:99]
      print 'submitting name as %s' % requestName

  if (conditions=='Run2016H-03Feb2017_ver2-v1' or conditions=='Run2016H-03Feb2017_ver3-v1'):
      psetName = 'SUB-JSON-Promptreco.py'
  else: 
      psetName = 'SUB-JSON-Boost.py'


  inputDataset = sample 
  filesPerJob = '1'
  submit(inputDataset, requestName, filesPerJob, psetName)

