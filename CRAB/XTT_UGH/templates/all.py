
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

addEventSummary(process,False,'MT','eventSelectionMT')
addEventSummary(process,False,'ET','eventSelectionET')
addEventSummary(process,False,'TT','eventSelectionTT')


process.TFileService.fileName=cms.string("$outputFileName")

