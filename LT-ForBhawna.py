import FWCore.ParameterSet.Config as cms

process = cms.Process("ANALYSIS")
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')

process.GlobalTag.globaltag = '80X_mcRun2_asymptotic_2016_TrancheIV_v8'

#process.options   = cms.untracked.PSet(wantSummary = cms.untracked.bool(True))
process.options   = cms.untracked.PSet(wantSummary = cms.untracked.bool(False))
process.options.allowUnscheduled = cms.untracked.bool(True)


process.maxEvents = cms.untracked.PSet(
        input = cms.untracked.int32(-1)
        )


# Make the framework shut up.
process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 1000


process.source = cms.Source("PoolSource",
        fileNames = cms.untracked.vstring(
            #'file:pickevents.root'
            '/store/mc/RunIISummer16MiniAODv2/ZprimeToA0hToA0chichihtautau_2HDM_MZp-1200_MA0-300_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/128B8DDC-E1C9-E611-A09D-0CC47A78A4B0.root'
            ),
        firstEvent = cms.untracked.uint32(5),
        inputCommands=cms.untracked.vstring(
            'keep *',
            'keep *_l1extraParticles_*_*',
            )
        )

#process.dump=cms.EDAnalyzer('EventContentAnalyzer')


#added in etau and mutau triggers
from MonoHTauTau.Configuration.tools.analysisToolsXTauTau import *
defaultReconstructionMC(process,'HLT',
        [
            'HLT_IsoMu18_v', 
            'HLT_IsoMu20_v', 
            'HLT_IsoMu22_v', 
            'HLT_IsoMu22_eta2p1_v', 
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

createGeneratedParticles(process, 'genDaughters',
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
                    "keep pdgId = 25",
                    "keep pdgId = 35",
                    "keep pdgId = 37",
                    "keep pdgId = 36"
                    ]
                )


createGeneratedParticles(process,
                'genTauCands',
                [
                    "keep pdgId = {tau+} & mother.pdgId()= {Z0}",
                    "keep pdgId = {tau-} & mother.pdgId() = {Z0}"
                    ]
                )

#EventSelection
process.load("MonoHTauTau.Configuration.monohiggs_cff")


process.eventSelectionMT = cms.Path(process.selectionSequenceMT)
process.eventSelectionET = cms.Path(process.selectionSequenceET)
process.eventSelectionTT = cms.Path(process.selectionSequenceTT)

from MonoHTauTau.Configuration.tools.ntupleTools_monohiggs import addMuTauEventTree
addMuTauEventTree(process,'muTauEventTree')
addMuTauEventTree(process,'muTauEventTreeFinal','muTausOS','diMuonsOSSorted')

from MonoHTauTau.Configuration.tools.ntupleTools_monohiggs import addEleTauEventTree
addEleTauEventTree(process,'eleTauEventTree')
addEleTauEventTree(process,'eleTauEventTreeFinal','eleTausOS','diElectronsOSSorted')

from MonoHTauTau.Configuration.tools.ntupleTools_monohiggs import addDiTauEventTree
addDiTauEventTree(process,'diTauEventTree')
addDiTauEventTree(process,'diTauEventTreeFinal','diTausOS')

addEventSummary(process,True,'MT','eventSelectionMT')
addEventSummary(process,True,'ET','eventSelectionET')
addEventSummary(process,True,'TT','eventSelectionTT')

