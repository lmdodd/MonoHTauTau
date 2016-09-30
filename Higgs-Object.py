import FWCore.ParameterSet.Config as cms

process = cms.Process("ANALYSIS")
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')

process.GlobalTag.globaltag = '80X_mcRun2_asymptotic_2016_miniAODv2_v1'



process.options   = cms.untracked.PSet(wantSummary = cms.untracked.bool(False))
process.options.allowUnscheduled = cms.untracked.bool(True)


process.maxEvents = cms.untracked.PSet(
        input = cms.untracked.int32(-1)
        )


# Make the framework shut up.
process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 100


process.source = cms.Source("PoolSource",
        fileNames = cms.untracked.vstring(
            #'file:tester.root'
            #'/store/mc/RunIISpring16MiniAODv2/WJetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14_ext1-v1/40000/0002BEE4-D55B-E611-B35D-0017A4770C08.root'
            '/store/mc/RunIISpring16MiniAODv2/ZprimeToA0hToA0chichihtautau_2HDM_MZp-2500_MA0-400_13TeV-madgraph/MINIAODSIM/PUSpring16RAWAODSIM_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/70000/96A23DDC-FE25-E611-93E6-D8D385AF8AB2.root'
),
        inputCommands=cms.untracked.vstring(
            'keep *',
            'keep *_l1extraParticles_*_*',
            )
        )

process.dump=cms.EDAnalyzer('EventContentAnalyzer')


#added in etau and mutau triggers
from MonoHTauTau.Configuration.tools.analysisToolsBoostedHiggsObject import *
defaultReconstructionMC(process,'HLT2',
        [
            'HLT_IsoMu18_v', 
            'HLT_IsoMu20_v', 
            'HLT_IsoMu22_v', 
            'HLT_IsoTkMu22_v', 
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
            'HLT_DoubleMediumIsoPFTau35_Trk1_eta2p1_Reg_v',
            'HLT_DoubleMediumIsoPFTau40_Trk1_eta2p1_Reg_v',
            'HLT_PFMET170_NoiseCleaned',
            'HLT_PFMET90_PFMHT90_IDTight',
            'HLT_CaloJet500_NoJetID',
            'HLT_ECALHT800'
            ])




#EventSelection
process.load("MonoHTauTau.Configuration.boostedHiggs_cff")

process.metCalibration.applyCalibration = cms.bool(False)

process.eventSelectionTT = cms.Path(process.selectionSequenceTT)
process.eventSelectionMT = cms.Path(process.selectionSequenceMT)
process.eventSelectionET = cms.Path(process.selectionSequenceET)
process.eventSelectionETK = cms.Path(process.selectionSequenceETK)
process.eventSelectionMTK = cms.Path(process.selectionSequenceMTK)

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

from MonoHTauTau.Configuration.tools.ntupleToolsBoostedHiggs import addDiTauEventTree
addDiTauEventTree(process,'diTauEventTree')
addDiTauEventTree(process,'diTauEventTreeFinal','diTausOS')

#boosted taus 
from MonoHTauTau.Configuration.tools.ntupleToolsBoostedHiggs import addMuTauEventTree
addMuTauEventTree(process,'muTauEventTree')
addMuTauEventTree(process,'muTauEventTreeFinal','muTausOS','diMuonsOSSorted')

from MonoHTauTau.Configuration.tools.ntupleToolsBoostedHiggs import addEleTauEventTree
addEleTauEventTree(process,'eleTauEventTree')
addEleTauEventTree(process,'eleTauEventTreeFinal','eleTausOS','diElectronsOSSorted')

#track trees
from MonoHTauTau.Configuration.tools.ntupleToolsBoostedHiggs import addMuTrackEventTree
addMuTrackEventTree(process,'muTrackEventTree')
addMuTrackEventTree(process,'muTrackEventTreeFinal','muTracksOS','diMuonsTrkOSSorted')

from MonoHTauTau.Configuration.tools.ntupleToolsBoostedHiggs import addEleTrackEventTree
addEleTrackEventTree(process,'eleTrackEventTree')
addEleTrackEventTree(process,'eleTrackEventTreeFinal','eleTracksOS','diElectronsOSSorted')

addEventSummary(process,True,'TT','eventSelectionTT')
addEventSummary(process,True,'MT','eventSelectionMT')
addEventSummary(process,True,'ET','eventSelectionET')
addEventSummary(process,True,'MTK','eventSelectionMTK')
addEventSummary(process,True,'ETK','eventSelectionETK')

#dump_file = open('dump.py','w')
#dump_file.write(process.dumpPython())
