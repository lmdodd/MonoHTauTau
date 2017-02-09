import FWCore.ParameterSet.Config as cms

process = cms.Process("ANALYSIS")
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')

process.GlobalTag.globaltag = '80X_mcRun2_asymptotic_2016_TrancheIV_v8'


process.options   = cms.untracked.PSet(wantSummary = cms.untracked.bool(False))
process.options.allowUnscheduled = cms.untracked.bool(True)


#added in etau and mutau triggers
from MonoHTauTau.Configuration.tools.analysisToolsBoostedHiggsObject import *
defaultReconstructionMC(process,'HLT',
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

process.eventSelectionTT = cms.Path(process.selectionSequenceTT)
process.eventSelectionMT = cms.Path(process.selectionSequenceMT)
process.eventSelectionMTK = cms.Path(process.selectionSequenceMTK)


#Systematic Shifts 1sigma
#process.eventSelectionMTTauUp    = createSystematics(process,process.selectionSequenceMT,'TauUp',1.0,1.0,1.03,0,1.0)
#process.eventSelectionMTTauDown  = createSystematics(process,process.selectionSequenceMT,'TauDown',1.0,1.0,0.97,0,1.0)
#process.eventSelectionMTJetUp    = createSystematics(process,process.selectionSequenceMT,'JetUp',1.0,1.0,1.0,1,1.0)
#process.eventSelectionMTJetDown  = createSystematics(process,process.selectionSequenceMT,'JetDown',1.0,1.0,1.0,-1,1.0)

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
addDiTauEventTree(process,'diTauEventTreeFinal','diTausOS','diNonBoostTausOSSorted')

from MonoHTauTau.Configuration.tools.ntupleToolsBoostedHiggs import addMuTauEventTree
addMuTauEventTree(process,'muTauEventTree')
addMuTauEventTree(process,'muTauEventTreeFinal','muTausOS','diMuonsOSSorted')

#track trees
from MonoHTauTau.Configuration.tools.ntupleToolsBoostedHiggs import addMuTrackEventTree
addMuTrackEventTree(process,'muTrackEventTree')
addMuTrackEventTree(process,'muTrackEventTreeFinal','muTracksOS','diMuonsTrkOSSorted')


addEventSummary(process,True,'TT','eventSelectionTT')
addEventSummary(process,True,'MT','eventSelectionMT')
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

process.source = cms.Source("PoolSource",
        fileNames = cms.untracked.vstring(
            '/store/mc/RunIISummer16MiniAODv2/MonoHtautau_ZpBaryonic_MZp-10000_MChi-1000_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/1A466397-5CC9-E611-AB62-C81F66B73FCF.root'
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
        fileName = cms.string("higgs.root")
        )
