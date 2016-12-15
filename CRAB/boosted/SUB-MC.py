import FWCore.ParameterSet.Config as cms

process = cms.Process("ANALYSIS")
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')

process.GlobalTag.globaltag = '80X_mcRun2_asymptotic_2016_miniAODv2_v1'


process.options   = cms.untracked.PSet(wantSummary = cms.untracked.bool(False))
process.options.allowUnscheduled = cms.untracked.bool(True)



#added in etau and mutau triggers
from MonoHTauTau.Configuration.tools.analysisToolsBoostedHiggsObject import *
defaultReconstructionMC(process,'HLT',
        [
            'HLT_IsoMu18_v', 
            'HLT_IsoMu20_v', 
            'HLT_IsoMu22_v', 
            'HLT_IsoMu22_eta2p1_v', 
            'HLT_IsoTkMu22_eta2p1_v',
            'HLT_IsoTkMu22_v',
            'HLT_IsoMu24_v', 
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
            'HLT_VLooseIsoPFTau140_Trk50_eta2p1_v',
            'HLT_VLooseIsoPFTau120_Trk50_eta2p1_v',
            'HLT_PFMET170_NoiseCleaned',
            'HLT_PFMET90_PFMHT90_IDTight',
            'HLT_CaloJet500_NoJetID',
            'HLT_ECALHT800'
            ])



        #EventSelection
process.load("MonoHTauTau.Configuration.boostedHiggs_cff")

process.metCalibration.applyCalibration = cms.bool(False)

process.eventSelectionTT = cms.Path(process.selectionSequenceTT)
#process.eventSelectionMT = cms.Path(process.selectionSequenceMT)
#process.eventSelectionET = cms.Path(process.selectionSequenceET)
#process.eventSelectionETK = cms.Path(process.selectionSequenceETK)
process.eventSelectionMTK = cms.Path(process.selectionSequenceMTK)


#Systematic Shifts 1sigma
#process.eventSelectionMTTauUp    = createSystematics(process,process.selectionSequenceMT,'TauUp',1.0,1.0,1.03,0,1.0)
#process.eventSelectionMTTauDown  = createSystematics(process,process.selectionSequenceMT,'TauDown',1.0,1.0,0.97,0,1.0)
#process.eventSelectionMTJetUp    = createSystematics(process,process.selectionSequenceMT,'JetUp',1.0,1.0,1.0,1,1.0)
#process.eventSelectionMTJetDown  = createSystematics(process,process.selectionSequenceMT,'JetDown',1.0,1.0,1.0,-1,1.0)

#process.eventSelectionETTauUp    = createSystematics(process,process.selectionSequenceET,'TauUp',1.00,1.0,1.03,0,1.0)
#process.eventSelectionETTauDown  = createSystematics(process,process.selectionSequenceET,'TauDown',1.0,1.0,0.97,0,1.0)
#process.eventSelectionETJetUp    = createSystematics(process,process.selectionSequenceET,'JetUp',1.0,1.0,1.0,1,1.0)
#process.eventSelectionETJetDown  = createSystematics(process,process.selectionSequenceET,'JetDown',1.0,1.0,1.0,-1,1.0)



createGeneratedParticles(process,
        'genDaughters',
        [
            "keep++ pdgId = {Z0}",
            "keep pdgId = {tau+}",
            "keep pdgId = {tau-}",
            "keep pdgId = {mu+}",
            "keep pdgId = {mu-}",
            "keep pdgId = 6",
            "keep pdgId = -6",
            "keep pdgId = 11",
            "keep pdgId = -11",
            ]
        )


createGeneratedParticles(process,
        'genTauCands',
        [
            "keep pdgId = {tau+}",
            "keep pdgId = {tau-}"
            ]
        )



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


#Final trees afor shapes after shifts
#addMuTauEventTree(process,'muTauEventTreeTauUp','muTausSortedTauUp','diMuonsOSTauUp')
#addMuTauEventTree(process,'muTauEventTreeTauDown','muTausSortedTauDown','diMuonsOSTauDown')
#addMuTauEventTree(process,'muTauEventTreeFinalTauUp','muTausOSTauUp','diMuonsOSTauUp')
#addMuTauEventTree(process,'muTauEventTreeFinalTauDown','muTausOSTauDown','diMuonsOSTauDown')
#addMuTauEventTree(process,'muTauEventTreeJetUp','muTausSortedJetUp','diMuonsOSJetUp')
#addMuTauEventTree(process,'muTauEventTreeJetDown','muTausSortedJetDown','diMuonsOSJetDown')
#addMuTauEventTree(process,'muTauEventTreeFinalJetUp','muTausOSJetUp','diMuonsOSJetUp')
#addMuTauEventTree(process,'muTauEventTreeFinalJetDown','muTausOSJetDown','diMuonsOSJetDown')
#
#addEleTauEventTree(process,'eleTauEventTreeTauUp','eleTausSortedTauUp','diElectronsOSTauUp')
#addEleTauEventTree(process,'eleTauEventTreeTauDown','eleTausSortedTauDown','diElectronsOSTauDown')
#addEleTauEventTree(process,'eleTauEventTreeFinalTauUp','eleTausOSTauUp','diElectronsOSTauUp')
#addEleTauEventTree(process,'eleTauEventTreeFinalTauDown','eleTausOSTauDown','diElectronsOSTauDown')
#addEleTauEventTree(process,'eleTauEventTreeJetUp','eleTausSortedJetUp','diElectronsOSJetUp')
#addEleTauEventTree(process,'eleTauEventTreeJetDown','eleTausSortedJetDown','diElectronsOSJetDown')
#addEleTauEventTree(process,'eleTauEventTreeFinalJetUp','eleTausOSJetUp','diElectronsOSJetUp')
#addEleTauEventTree(process,'eleTauEventTreeFinalJetDown','eleTausOSJetDown','diElectronsOSJetDown')
#
#

process.source = cms.Source("PoolSource",
        fileNames = cms.untracked.vstring(
            $inputFileNames
            ),
        inputCommands=cms.untracked.vstring(
            'keep *',
            )
        )

process.maxEvents = cms.untracked.PSet(
        input = cms.untracked.int32(-1)
        )

#process.TFileService.fileName=cms.string("$outputFileName")
process.TFileService = cms.Service(
        "TFileService",
        fileName = cms.string("$outputFileName")
        )
