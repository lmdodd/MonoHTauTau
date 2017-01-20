process.eventSelectionMT = cms.Path(process.selectionSequenceMT)


from MonoHTauTau.Configuration.tools.ntupleTools_monohiggs import addMuTauEventTree
addMuTauEventTree(process,'muTauEventTree')
addMuTauEventTree(process,'muTauEventTreeFinal','muTausOS','diMuonsOSSorted')

addEventSummary(process,True,'MT','eventSelectionMT')

process.TFileService.fileName=cms.string("$outputFileName")

