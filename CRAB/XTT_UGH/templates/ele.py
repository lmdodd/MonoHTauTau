process.eventSelectionET = cms.Path(process.selectionSequenceET)

from MonoHTauTau.Configuration.tools.ntupleTools_monohiggs import addEleTauEventTree
addEleTauEventTree(process,'eleTauEventTree')
addEleTauEventTree(process,'eleTauEventTreeFinal','eleTausOS','diElectronsOSSorted')

addEventSummary(process,True,'ET','eventSelectionET')


process.TFileService.fileName=cms.string("$outputFileName")

