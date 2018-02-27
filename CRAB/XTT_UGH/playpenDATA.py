from WMCore.Configuration import Configuration
import os
import re


name = 'Jun14_submission_v1_DATA'
projectName = 'MONOHTT_PLAYPEN'

dataset = [
'/SingleMuon/Run2016H-03Feb2017_ver3-v1/MINIAOD',
'/SingleMuon/Run2016H-03Feb2017_ver2-v1/MINIAOD',
'/SingleMuon/Run2016G-03Feb2017-v1/MINIAOD',
'/SingleMuon/Run2016B-03Feb2017_ver2-v2/MINIAOD',
'/SingleMuon/Run2016C-03Feb2017-v1/MINIAOD',
'/SingleMuon/Run2016D-03Feb2017-v1/MINIAOD',
'/SingleMuon/Run2016E-03Feb2017-v1/MINIAOD',
'/SingleMuon/Run2016F-03Feb2017-v1/MINIAOD',
'/SingleElectron/Run2016B-03Feb2017_ver2-v2/MINIAOD',
'/SingleElectron/Run2016C-03Feb2017-v1/MINIAOD',
'/SingleElectron/Run2016D-03Feb2017-v1/MINIAOD',
'/SingleElectron/Run2016E-03Feb2017-v1/MINIAOD',
'/SingleElectron/Run2016F-03Feb2017-v1/MINIAOD',
'/SingleElectron/Run2016G-03Feb2017-v1/MINIAOD',
'/SingleElectron/Run2016H-03Feb2017_ver2-v1/MINIAOD',
'/SingleElectron/Run2016H-03Feb2017_ver3-v1/MINIAOD',
'/Tau/Run2016B-03Feb2017_ver2-v2/MINIAOD',
'/Tau/Run2016C-03Feb2017-v1/MINIAOD',
'/Tau/Run2016D-03Feb2017-v1/MINIAOD',
'/Tau/Run2016E-03Feb2017-v1/MINIAOD',
'/Tau/Run2016F-03Feb2017-v1/MINIAOD',
'/Tau/Run2016G-03Feb2017-v1/MINIAOD',
'/Tau/Run2016H-03Feb2017_ver2-v1/MINIAOD',
'/Tau/Run2016H-03Feb2017_ver3-v1/MINIAOD'
]


if __name__ == '__main__':
    from CRABAPI.RawCommand import crabCommand

def submit(config):
    res = crabCommand('submit', config = config)

from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()
config.General.workArea = '/cms/laura/crab_workArea_'+projectName+'_'+name
config.General.transferOutputs = True
config.General.transferLogs = True
config.JobType.pluginName = 'Analysis'
config.Data.publication = False
config.Site.storageSite = 'T2_US_Wisconsin'
config.JobType.psetName = 'SUB-JSON-Rereco.py'
config.JobType.maxMemoryMB = 4500
#config.JobType.inputFiles = ["%s/src/MonoHTauTau/Configuration/data" % os.environ["CMSSW_BASE"]]
config.Data.lumiMask = '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions16/13TeV/Final/Cert_271036-284044_13TeV_PromptReco_Collisions16_JSON.txt'
config.Data.inputDBS = 'global'
config.Data.splitting = 'LumiBased'
for sample in dataset:
  (_, primaryDS, conditions, dataTier) = sample.split('/')
  print 'submitting %s' % primaryDS
  config.General.requestName = '_'.join([projectName,'Mar17', primaryDS,conditions])

  if (conditions=='Run2016H-03Feb2017_ver2-v1' or conditions=='Run2016H-03Feb2017_ver3-v1'):
      config.JobType.psetName = 'SUB-JSON-Promptreco.py'
  else: 
      config.JobType.psetName = 'SUB-JSON-Rereco.py'

  if len(config.General.requestName)>100:
      print 'skipping sample %s... more than 100 characters' % config.General.requestName
      break


  config.Data.inputDataset = sample 
  config.Data.unitsPerJob = 200
  config.Data.totalUnits = -1
  config.Data.outLFNDirBase = '/store/user/%s/crab_%s/%s/%s' % (getUsernameFromSiteDB(), projectName, name,primaryDS)
  submit(config)
