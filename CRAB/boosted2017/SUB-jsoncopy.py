import FWCore.ParameterSet.Config as cms

process = cms.Process("ANALYSIS")
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')


#process.GlobalTag.globaltag = '80X_dataRun2_Prompt_ICHEP16JEC_v0'
process.GlobalTag.globaltag = '80X_dataRun2_Prompt_v14'

process.options   = cms.untracked.PSet(wantSummary = cms.untracked.bool(False))
process.options.allowUnscheduled = cms.untracked.bool(True)

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
		$inputFileNames
		),
		inputCommands=cms.untracked.vstring(
						'keep *',
		)
)

import FWCore.PythonUtilities.LumiList as LumiList
process.source.lumisToProcess = LumiList.LumiList(filename = '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions16/13TeV/Cert_271036-284044_13TeV_PromptReco_Collisions16_JSON_NoL1T.txt').getVLuminosityBlockRange()


process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)


#added in etau and mutau triggers
from MonoHTauTau.Configuration.tools.analysisToolsBoostedHiggsObject import *
defaultReconstruction(process,'HLT',
        [
            'HLT_IsoMu18_v', 
            'HLT_IsoMu20_v', 
            'HLT_IsoMu22_v', 
            'HLT_IsoMu22_eta2p1_v', 
            'HLT_IsoTkMu22_v',
            'HLT_IsoTkMu22_eta2p1_v',
            'HLT_IsoMu24_v', 
            'HLT_Mu50_v', 
            'HLT_IsoMu17_eta2p1_LooseIsoPFTau20_v',
            'HLT_IsoMu17_eta2p1_LooseIsoPFTau20_SingleL1_v',
            'HLT_IsoMu19_eta2p1_LooseIsoPFTau20_v',
            'HLT_IsoMu19_eta2p1_LooseIsoPFTau20_SingleL1_v',
            'HLT_IsoMu21_eta2p1_LooseIsoPFTau20_SingleL1_v',
            'HLT_Ele22_eta2p1_WPLoose_LooseIsoPFTau20_v',
            'HLT_Ele22_eta2p1_WPLoose_LooseIsoPFTau20_SingleL1_v',
            'HLT_Ele23_WPLoose_Gsf_v',
            'HLT_Ele24_eta2p1_WPLoose_Gsf_v',
            'HLT_Ele24_eta2p1_WPLoose_Gsf_LooseIsoPFTau20_v',
            'HLT_Ele24_eta2p1_WPLoose_Gsf_LooseIsoPFTau20_SingleL1_v',
            'HLT_Ele24_WPLoose_Gsf_v',
            'HLT_Ele25_eta2p1_WPLoose_Gsf_v',
            'HLT_Ele25_eta2p1_WPTight_Gsf_v',	
            'HLT_Ele27_WPLoose_Gsf_v',
            'HLT_Ele27_WPTight_Gsf_v',
            'HLT_Ele27_eta2p1_WPLoose_Gsf_v',
            'HLT_Ele27_eta2p1_WPTight_Gsf_v',
            'HLT_Ele45_WPLoose_Gsf_v',
            'HLT_VLooseIsoPFTau140_Trk50_eta2p1_v',
            'HLT_LooseIsoPFTau50_Trk30_eta2p1_MET90_v',
            'HLT_MET200_v5',
            'HLT_PFHT125_v5',
            'HLT_PFMET120_PFMHT120_IDTight_v',
            'HLT_MonoCentralPFJet80_PFMETNoMu110_PFMHTNoMu110_IDTight_v',
            'HLT_DoubleMediumIsoPFTau35_Trk1_eta2p1_Reg_v',
            'HLT_DoubleMediumIsoPFTau40_Trk1_eta2p1_Reg_v',
            'HLT_DoubleMediumCombinedIsoPFTau35_Trk1_eta2p1_Reg_v',
            'HLT_DoubleMediumCombinedIsoPFTau40_Trk1_eta2p1_Reg_v',
            'HLT_DoubleMediumCombinedIsoPFTau40_Trk1_eta2p1_v',
            'HLT_PFMET170_NoiseCleaned',
            'HLT_VLooseIsoPFTau120_Trk50_eta2p1_v',
            'HLT_PFMET170_NoiseCleaned',
            'HLT_PFMET90_PFMHT90_IDTight',
            'HLT_CaloJet500_NoJetID',
            'HLT_ECALHT800'
            ])



#EventSelection
process.load("MonoHTauTau.Configuration.boostedHiggs_cff")


process.eventSelectionTT = cms.Path(process.selectionSequenceTT)
#process.eventSelectionMT = cms.Path(process.selectionSequenceMT)
#process.eventSelectionET = cms.Path(process.selectionSequenceET)
#process.eventSelectionETK = cms.Path(process.selectionSequenceETK)
process.eventSelectionMTK = cms.Path(process.selectionSequenceMTK)

#boosted taus 

from MonoHTauTau.Configuration.tools.ntupleToolsBoostedHiggs import addDiTauEventTree
addDiTauEventTree(process,'diTauEventTree')
addDiTauEventTree(process,'diTauEventTreeFinal','diTausOS')

#from MonoHTauTau.Configuration.tools.ntupleToolsBoostedHiggs import addMuTauEventTree
#addMuTauEventTree(process,'muTauEventTree')
#addMuTauEventTree(process,'muTauEventTreeFinal','muTausOS','diMuonsOSSorted')

#from MonoHTauTau.Configuration.tools.ntupleToolsBoostedHiggs import addEleTauEventTree
#addEleTauEventTree(process,'eleTauEventTree')
#addEleTauEventTree(process,'eleTauEventTreeFinal','eleTausOS','diElectronsOSSorted')

#track trees
from MonoHTauTau.Configuration.tools.ntupleToolsBoostedHiggs import addMuTrackEventTree
addMuTrackEventTree(process,'muTrackEventTree')
addMuTrackEventTree(process,'muTrackEventTreeFinal','muTracksOS','diMuonsTrkOSSorted')

#from MonoHTauTau.Configuration.tools.ntupleToolsBoostedHiggs import addEleTrackEventTree
#addEleTrackEventTree(process,'eleTrackEventTree')
#addEleTrackEventTree(process,'eleTrackEventTreeFinal','eleTracksOS','diElectronsOSSorted')

addEventSummary(process,True,'TT','eventSelectionTT')
#addEventSummary(process,True,'MT','eventSelectionMT')
#addEventSummary(process,True,'ET','eventSelectionET')
addEventSummary(process,True,'MTK','eventSelectionMTK')
#addEventSummary(process,True,'ETK','eventSelectionETK')


process.TFileService.fileName=cms.string("$outputFileName")

