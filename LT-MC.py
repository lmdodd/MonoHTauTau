import FWCore.ParameterSet.Config as cms

process = cms.Process("ANALYSIS")
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')

process.GlobalTag.globaltag = '80X_mcRun2_asymptotic_2016_TrancheIV_v8'


process.options   = cms.untracked.PSet(wantSummary = cms.untracked.bool(False))
process.options.allowUnscheduled = cms.untracked.bool(True)


# Make the framework shut up.
process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 500


process.source = cms.Source("PoolSource",
        fileNames = cms.untracked.vstring(
            '/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v2/60000/8EE3D66F-E1C3-E611-B3D5-6CC2173BBD70.root'
            ),
        inputCommands=cms.untracked.vstring(
            'keep *',
            )
        )

process.maxEvents = cms.untracked.PSet(
        input = cms.untracked.int32(-1)
        )

#added in etau and mutau triggers
from MonoHTauTau.Configuration.tools.analysisToolsXTauTau import *
defaultReconstructionMC(process,'HLT',
        [
            'HLT_IsoMu22_v', 
            'HLT_IsoTkMu22_v',
            'HLT_IsoMu22_eta2p1_v', 
            'HLT_IsoTkMu22_eta2p1_v',
            'HLT_IsoMu24_v', 
            'HLT_IsoTkMu24_v', 
            'HLT_IsoMu19_eta2p1_LooseIsoPFTau20_v',
            'HLT_IsoMu19_eta2p1_LooseIsoPFTau20_SingleL1_v',
            'HLT_IsoMu21_eta2p1_LooseIsoPFTau20_SingleL1_v',
            'HLT_Ele22_eta2p1_WPLoose_LooseIsoPFTau20_v',
            'HLT_Ele22_eta2p1_WPLoose_LooseIsoPFTau20_SingleL1_v',
            'HLT_Ele24_eta2p1_WPLoose_Gsf_LooseIsoPFTau20_v',
            'HLT_Ele24_eta2p1_WPLoose_Gsf_LooseIsoPFTau20_SingleL1_v',
            'HLT_Ele25_eta2p1_WPTight_Gsf_v',	
            'HLT_Ele27_WPTight_Gsf_v',
            'HLT_Ele27_eta2p1_WPTight_Gsf_v',
            'HLT_DoubleMediumIsoPFTau35_Trk1_eta2p1_Reg_v',
            'HLT_DoubleMediumIsoPFTau40_Trk1_eta2p1_Reg_v',
            'HLT_DoubleMediumCombinedIsoPFTau35_Trk1_eta2p1_Reg_v',
            'HLT_DoubleMediumCombinedIsoPFTau40_Trk1_eta2p1_Reg_v',
            'HLT_DoubleMediumCombinedIsoPFTau40_Trk1_eta2p1_v',
            'HLT_VLooseIsoPFTau140_Trk50_eta2p1_v',
            'HLT_VLooseIsoPFTau120_Trk50_eta2p1_v',
            'HLT_PFMET170_NoiseCleaned',
            'HLT_PFMET90_PFMHT90_IDTight',
            'HLT_CaloJet500_NoJetID',
            'HLT_ECALHT800'
            ])



        #EventSelection
process.load("MonoHTauTau.Configuration.monohiggs_cff")


process.eventSelectionMT = cms.Path(process.selectionSequenceMT)
process.eventSelectionET = cms.Path(process.selectionSequenceET)
process.eventSelectionTT = cms.Path(process.selectionSequenceTT)
#Systematic Shifts 1sigma

process.eventSelectionMTTauNom    = createSystematics(process,process.selectionSequenceMT,'TauNom', 1.00, 1.00, 1.00, 0, 1.00, 0.00, 0.00, 0.982, 1.010, 1.004)
process.eventSelectionMTTauUp    = createSystematics(process,process.selectionSequenceMT, 'TauUp',  1.00, 1.00, 1.00, 0, 1.00, 0.00, 0.00, 0.988, 1.016, 1.01)
process.eventSelectionMTTauDown  = createSystematics(process,process.selectionSequenceMT,'TauDown', 1.00, 1.00, 1.00, 0, 1.00, 0.00, 0.00, 0.976, 1.004, 0.998)
#process.eventSelectionMTJetUp    = createSystematics(process,process.selectionSequenceMT,'JetUp',   1.00, 1.00, 1.00, 1, 1.00, 0.00, 0.00, 0.982, 1.010, 1.004)
#process.eventSelectionMTJetDown    = createSystematics(process,process.selectionSequenceMT,'JetDown',   1.00, 1.00, 1.00, -1, 1.00, 0.00, 0.00, 0.982, 1.010, 1.004)

process.eventSelectionETTauNom    = createSystematics(process,process.selectionSequenceET,'TauNom', 1.00, 1.00, 1.00, 0, 1.00, 0.00, 0.00, 0.982, 1.010, 1.004)
process.eventSelectionETTauUp    = createSystematics(process,process.selectionSequenceET, 'TauUp',  1.00, 1.00, 1.00, 0, 1.00, 0.00, 0.00, 0.988, 1.016, 1.01)
process.eventSelectionETTauDown  = createSystematics(process,process.selectionSequenceET,'TauDown', 1.00, 1.00, 1.00, 0, 1.00, 0.00, 0.00, 0.976, 1.004, 0.998)
#process.eventSelectionETJetUp    = createSystematics(process,process.selectionSequenceET,'JetUp',   1.00, 1.00, 1.00, 1, 1.00, 0.00, 0.00, 0.982, 1.010, 1.004)
#process.eventSelectionETJetDown    = createSystematics(process,process.selectionSequenceET,'JetDown',   1.00, 1.00, 1.00, -1, 1.00, 0.00, 0.00, 0.982, 1.010, 1.004)

process.eventSelectionTTTauNom    = createSystematics(process,process.selectionSequenceTT,'TauNom', 1.00, 1.00, 1.00, 0, 1.00, 0.00, 0.00, 0.982, 1.010, 1.004)
process.eventSelectionTTTauUp    = createSystematics(process,process.selectionSequenceTT, 'TauUp',  1.00, 1.00, 1.00, 0, 1.00, 0.00, 0.00, 0.988, 1.016, 1.01)
process.eventSelectionTTTauDown  = createSystematics(process,process.selectionSequenceTT,'TauDown', 1.00, 1.00, 1.00, 0, 1.00, 0.00, 0.00, 0.976, 1.004, 0.998)
#process.eventSelectionTTJetUp    = createSystematics(process,process.selectionSequenceTT,'JetUp',   1.00, 1.00, 1.00, 1, 1.00, 0.00, 0.00, 0.982, 1.010, 1.004)
#process.eventSelectionTTJetDown    = createSystematics(process,process.selectionSequenceTT,'JetDown',   1.00, 1.00, 1.00, -1, 1.00, 0.00, 0.00, 0.982, 1.010, 1.004)





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


from MonoHTauTau.Configuration.tools.ntupleTools_monohiggs import addMuTauEventTree
addMuTauEventTree(process,'muTauEventTree')
#addMuTauEventTree(process,'muTauEventTreeFinal','muTausOS','diMuonsOSSorted')


from MonoHTauTau.Configuration.tools.ntupleTools_monohiggs import addEleTauEventTree
addEleTauEventTree(process,'eleTauEventTree')
#addEleTauEventTree(process,'eleTauEventTreeFinal','eleTausOS','diElectronsOSSorted')

from MonoHTauTau.Configuration.tools.ntupleTools_monohiggs import addDiTauEventTree
addDiTauEventTree(process,'diTauEventTree')
#addDiTauEventTree(process,'diTauEventTreeFinal','diTausOS')

#Final trees afor shapes after shifts
addMuTauEventTree(process,'muTauEventTreeTauNom','muTausSortedTauNom','diMuonsOSTauNom')
addMuTauEventTree(process,'muTauEventTreeTauUp','muTausSortedTauUp','diMuonsOSTauUp')
addMuTauEventTree(process,'muTauEventTreeTauDown','muTausSortedTauDown','diMuonsOSTauDown')

addEleTauEventTree(process,'eleTauEventTreeTauNom','eleTausSortedTauNom','diElectronsOSTauNom')
addEleTauEventTree(process,'eleTauEventTreeTauUp','eleTausSortedTauUp','diElectronsOSTauUp')
addEleTauEventTree(process,'eleTauEventTreeTauDown','eleTausSortedTauDown','diElectronsOSTauDown')

addDiTauEventTree(process,'diTauEventTreeTauNom','diTausSortedTauNom')
addDiTauEventTree(process,'diTauEventTreeTauUp','diTausSortedTauUp')
addDiTauEventTree(process,'diTauEventTreeTauDown','diTausSortedTauDown')


addEventSummary(process,True,'MT','eventSelectionMT')
addEventSummary(process,True,'ET','eventSelectionET')
addEventSummary(process,True,'TT','eventSelectionTT')


