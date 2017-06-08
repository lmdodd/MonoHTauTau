from WMCore.Configuration import Configuration
from CRABClient.UserUtilities import config, getUsernameFromSiteDB
import ConfigParser
import os
import re
import subprocess
import sys
import datetime
import glob

name = 'test_feb24_v1'
projectName = 'MONOHTT_PLAYPEN'

datasetNames=[
'/ZHToTauTau_M125_13TeV_powheg_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM',
'/VBFHToWWTo2L2Nu_M125_13TeV_powheg_JHUgen_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM',
'/GluGluHToWWTo2L2Nu_M125_13TeV_powheg_JHUgen_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM',
'/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v2/MINIAODSIM',
'/MonoHtautau_EFT_HHxg5x_MChi-200_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM',
'/MonoHtautau_EFT_HHxx_scalar_MChi-100_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM'
]

# We have to hack our way around how crab parses command line arguments :<
dataset = 'dummy'
for arg in datasetNames:
        dataset = arg 
if dataset == 'dummy':
    raise Exception("Must pass dataset argument as Data.inputDataset=...")

(_, primaryDS, conditions, dataTier) = dataset.split('/')
if dataTier == 'MINIAOD':
    isMC = 0
elif dataTier == 'MINIAODSIM':
    isMC = 1
else:
    raise Exception("Dataset malformed? Couldn't deduce isMC parameter")



config = Configuration()
#General                                                                                                                                                                           
config.section_('General')
config.General.requestName = 'job_Monohiggs_playpen'
config.General.workArea = '/cms/laura/crab_projects_2016'
config.General.transferLogs = True
#JobType                                                                                                                                                                           
config.section_('JobType')
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'SUB-MC.py'

#Data                                                                                                                                                                              
config.section_('Data')
config.Data.inputDataset = dataset 
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

