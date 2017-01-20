process.eventSelectionTT = cms.Path(process.selectionSequenceTT)

from MonoHTauTau.Configuration.tools.ntupleTools_monohiggs import addDiTauEventTree
addDiTauEventTree(process,'diTauEventTree')
addDiTauEventTree(process,'diTauEventTreeFinal','diTausOS')

addEventSummary(process,True,'TT','eventSelectionTT')


process.TFileService.fileName=cms.string("$outputFileName")

