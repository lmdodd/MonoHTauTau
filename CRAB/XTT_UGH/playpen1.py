from WMCore.Configuration import Configuration
import os
import re


name = 'Jun12_submission_v3'
projectName = 'MONOHTT_PLAYPEN'

dataset = [
'/ZprimeToA0hToA0chichihtautau_2HDM_MZp-600_MA0-300_13TeV-madgraph-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM',
'/ZprimeToA0hToA0chichihtautau_2HDM_MZp-600_MA0-400_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM'
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
config.JobType.psetName = 'SUB-MC-noTES.py'
config.JobType.maxMemoryMB = 4500
#config.JobType.inputFiles = ["%s/src/MonoHTauTau/Configuration/data" % os.environ["CMSSW_BASE"]]
config.Data.inputDBS = 'global'
config.Data.splitting = 'FileBased'
for sample in dataset:
  (_, primaryDS, conditions, dataTier) = sample.split('/')
  print 'submitting %s' % primaryDS
  config.General.requestName = '_'.join([projectName,'Mar17_v1', primaryDS])
  m = re.match(r".*(_ext[0-9]*)-", conditions)
  if m:
     config.General.requestName += m.groups()[0]

  if len(config.General.requestName)>100:
      print 'rename sample %s... more than 100 characters' % config.General.requestName
      config.General.requestName = config.General.requestName[:99]
      print 'submitting name as %s' % config.General.requestName
      

  config.Data.inputDataset = sample 
  config.Data.unitsPerJob = 15
  config.Data.totalUnits = -1
  config.Data.outLFNDirBase = '/store/user/%s/crab_%s/%s/%s' % (getUsernameFromSiteDB(), projectName, name,primaryDS)
  submit(config)
