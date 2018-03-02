import FWCore.ParameterSet.Config as cms

process = cms.Process("ANALYSIS")
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')

process.GlobalTag.globaltag = '80X_dataRun2_Prompt_v16'

process.options   = cms.untracked.PSet(wantSummary = cms.untracked.bool(False))
process.options.allowUnscheduled = cms.untracked.bool(True)

# Make the framework shut up.
process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 1000


process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
		$inputFileNames
		),
		inputCommands=cms.untracked.vstring(
						'keep *',
		)
)

import FWCore.PythonUtilities.LumiList as LumiList
process.source.lumisToProcess = LumiList.LumiList(filename = '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions16/13TeV/ReReco/Final/Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON.txt').getVLuminosityBlockRange()


process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)


#added in etau and mutau triggers
from MonoHTauTau.Configuration.tools.analysisToolsBoostedHiggsObject import *
defaultReconstruction(process,'HLT',
        [
            'HLT_Mu50_v',
            'HLT_TkMu50_v',
            'HLT_LooseIsoPFTau50_Trk30_eta2p1_MET90_v',
            'HLT_MET200_v',
            'HLT_VLooseIsoPFTau140_Trk50_eta2p1_v',
            'HLT_VLooseIsoPFTau120_Trk50_eta2p1_v',
            'HLT_PFMET170_NoiseCleaned',
            'HLT_PFMET90_PFMHT90_IDTight',
            'HLT_MonoCentralPFJet80_PFMETNoMu110_PFMHTNoMu110_IDTight_v8',
            'HLT_CaloJet500_NoJetID',
            'HLT_ECALHT800'
            ])


#EventSelection
process.load("MonoHTauTau.Configuration.boostedHiggs_cff")



process.eventSelectionMTK = cms.Path(process.selectionSequenceMTK)


#track trees
from MonoHTauTau.Configuration.tools.ntupleToolsBoostedHiggs import addMuTrackEventTree
addMuTrackEventTree(process,'muTrackEventTree')
addMuTrackEventTree(process,'muTrackEventTreeFinal','muTracksOS','diMuonsTrkOSSorted')

addEventSummary(process,True,'MTK','eventSelectionMTK')


process.TFileService.fileName=cms.string("$outputFileName")

