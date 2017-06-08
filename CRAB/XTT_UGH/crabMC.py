from WMCore.Configuration import Configuration
from CRABClient.UserUtilities import config, getUsernameFromSiteDB


name = 'test_feb24_v1'
projectName = 'MONOHTT'


config = Configuration()
#General                                                                                                                                                                           
config.section_('General')
config.General.requestName = 'job_Monohiggs_v4'
config.General.workArea = '/cms/laura/crab_projects_2016'
config.General.transferLogs = True
#JobType                                                                                                                                                                           
config.section_('JobType')
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'SUB-MC.py'

#Data                                                                                                                                                                              
config.section_('Data')
config.Data.inputDataset = '/GluGluHToTauTau_M125_13TeV_powheg_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 3
config.Data.publication = False
#config.Data.totalUnits =  3
config.Data.totalUnits =  -1
#config.Data.ignoreLocality = True                                                                                                                                                 

config.Data.outLFNDirBase = '/store/user/%s/crab_%s/%s/' % (getUsernameFromSiteDB(), projectName, name)
#User                                                                                                                                                                              
config.section_('User')
#Site                                                                                                                     
config.section_('Site')
config.Site.storageSite = 'T2_US_Wisconsin'

