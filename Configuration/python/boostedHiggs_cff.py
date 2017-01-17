import FWCore.ParameterSet.Config as cms


#Import tool that creates the cut sequence
from MonoHTauTau.Configuration.tools.CutSequenceProducer import *


################################        Mu-Track          ###################################

MTKanalysisConfigurator = CutSequenceProducer(initialCounter  = 'initialEventsMTK',
                                  pyModuleName = __name__,
                                  pyNameSpace  = locals())
#Add smearing
MTKanalysisConfigurator.addTrkSmearing('patOverloadedTracks','MTK')
MTKanalysisConfigurator.addSmearing('patOverloadedTaus','triggeredPatMuons','triggeredPatElectrons','filteredJets','slimmedMETs','MTK')
#Create di muon pairs for veto purposes
MTKanalysisConfigurator.addDiCandidateModule('diMuonsTrk','PATMuPairProducer','smearedMuonsMTK','smearedMuonsMTK','slimmedMETs','','smearedJetsMTK',0,9999,text = '',leadingObjectsOnly = False,dR = 0.15,recoMode = "",genParticles='prunedGenParticles',drmax=False)
MTKanalysisConfigurator.addSelector('diMuonsTrkOS','PATMuPairSelector','leg1.isPFMuon&&leg2.isPFMuon&&abs(leg1.eta())<2.4&&abs(leg2.eta())<2.4&&abs(leg1.userFloat("dZ"))<0.2&&abs(leg2.userFloat("dZ"))<0.2&&abs(leg2.userFloat("dXY"))<0.045&&abs(leg2.userFloat("dXY"))<0.045&&charge==0&&leg1.isTrackerMuon&&leg2.isTrackerMuon&&leg1.isGlobalMuon&&leg2.isGlobalMuon&&leg1.pt()>15&&leg2.pt()>15&&leg1.userFloat("dBRelIso")<0.3&&leg2.userFloat("dBRelIso")<0.3','DiMuonCreationMTK',0,100)
MTKanalysisConfigurator.addSorter('diMuonsTrkOSSorted','PATMuPairSorter')

#Make DiTaus   
MTKanalysisConfigurator.addDiCandidateModule('muTracks','PATMuTrackPairProducer','smearedMuonsMTK','smearedTracksMTK','smearedMETMTK','smearedTausMTK','smearedJetsMTK',1,9999,text='AtLeastOneMuTrack',leadingObjectsOnly = False,dR = 0.3,recoMode ="",genParticles='prunedGenParticles',drmax=True)
MTKanalysisConfigurator.addSelector('muTracksMuonPtEta','PATMuTrackPairSelector','leg1.pt()>50&&abs(leg1.eta())<1.47','MTKMuonPtEta',1)
MTKanalysisConfigurator.addSelector('muTracksTrackPtEta','PATMuTrackPairSelector','leg2.pt()>50&&abs(leg2.eta())<1.47','MTKTrackPtEta',1)
MTKanalysisConfigurator.addSelector('muTracksMuonMediumID','PATMuTrackPairSelector','leg1.userInt("mediumID")>0','MTKMuonMediumID',1)
MTKanalysisConfigurator.addSelector('muTracksMuonVertices','PATMuTrackPairSelector','abs(leg1.userFloat("dZ"))<0.2&&abs(leg1.userFloat("dXY"))<0.045','MTKMuonVertices',1)
MTKanalysisConfigurator.addMuTrackLVeto('muTracksLVeto','TightElectrons','TightMuons')
MTKanalysisConfigurator.addMuTrackLeptonIso('muTracksLIso')
MTKanalysisConfigurator.addSelector('muTracksMuonVeto','PATMuTrackPairSelector','lVeto==0','MTKMuonVeto',1)
MTKanalysisConfigurator.addSorter('muTracksSorted','PATMuTrackPairSorter')
MTKanalysisConfigurator.addSelector('muTracksOS','PATMuTrackPairSelector','charge==0','MTKOS',1)


#create the sequence
selectionSequenceMTK =MTKanalysisConfigurator.returnSequence()

################################		Mu-Tau			###################################
MTanalysisConfigurator = CutSequenceProducer(initialCounter  = 'initialEventsMT',
                                  pyModuleName = __name__,
                                  pyNameSpace  = locals())

#Add smearing
MTanalysisConfigurator.addSmearing('patOverloadedTaus','triggeredPatMuons','triggeredPatElectrons','filteredJets','slimmedMETs','MT')
#Create di muon pairs for veto purposes
MTanalysisConfigurator.addDiCandidateModule('diMuons','PATMuPairProducer','smearedMuonsMT','smearedMuonsMT','slimmedMETs','','smearedJetsMT',0,9999,text = '',leadingObjectsOnly = False,dR = 0.15,recoMode = "",genParticles='prunedGenParticles')
MTanalysisConfigurator.addSelector('diMuonsOS','PATMuPairSelector','leg1.isPFMuon&&leg2.isPFMuon&&abs(leg1.eta())<2.4&&abs(leg2.eta())<2.4&&abs(leg1.userFloat("dZ"))<0.2&&abs(leg2.userFloat("dZ"))<0.2&&abs(leg2.userFloat("dXY"))<0.045&&abs(leg2.userFloat("dXY"))<0.045&&charge==0&&leg1.isTrackerMuon&&leg2.isTrackerMuon&&leg1.isGlobalMuon&&leg2.isGlobalMuon&&leg1.pt()>15&&leg2.pt()>15&&leg1.userFloat("dBRelIso")<0.3&&leg2.userFloat("dBRelIso")<0.3','DiMuonCreationMT',0,100)
MTanalysisConfigurator.addSorter('diMuonsOSSorted','PATMuPairSorter')

#Make DiTaus   
MTanalysisConfigurator.addDiCandidateModule('muTaus','PATMuTauPairProducer','smearedMuonsMT','smearedTausMT','smearedMETMT','smearedTausMT','smearedJetsMT',1,9999,text='AtLeastOneMuTau',leadingObjectsOnly = False,dR = 0.3,recoMode ="",genParticles='prunedGenParticles',drmax=True)
MTanalysisConfigurator.addSelector('muTausMuonPtEta','PATMuTauPairSelector','leg1.pt()>50&&abs(leg1.eta())<2.1','MTMuonPtEta',1)
MTanalysisConfigurator.addSelector('muTausTauPtEta','PATMuTauPairSelector','leg2.pt()>50&&abs(leg2.eta())<2.1','MTTauPtEta',1)
MTanalysisConfigurator.addSelector('muTausMuonMediumID','PATMuTauPairSelector','leg1.userInt("mediumID")>0','MTMuonMediumID',1)
MTanalysisConfigurator.addSelector('muTausMuonVertices','PATMuTauPairSelector','abs(leg1.userFloat("dZ"))<0.2&&abs(leg1.userFloat("dXY"))<0.045','MTMuonVertices',1)
MTanalysisConfigurator.addSelector('muTausDecayFound','PATMuTauPairSelector','leg2.tauID("decayModeFindingNewDMs")>0.5','MTTauDecayFound',1)
MTanalysisConfigurator.addSelector('muTausDecayVertex','PATMuTauPairSelector','abs(leg2.userFloat("taudZ"))<0.2','MTTauVertex',1)
MTanalysisConfigurator.addSelector('muTausTauLooseID','PATMuTauPairSelector','leg2.tauID("byLooseIsolationMVArun2v1DBoldDMwLT")>0.5','MTTauLooseID',1)
MTanalysisConfigurator.addMuTauLVeto('muTausLVeto','TightElectrons','TightMuons')
MTanalysisConfigurator.addSelector('muTausMuonVeto','PATMuTauPairSelector','lVeto==0','MTMuonVeto',1)
MTanalysisConfigurator.addSelector('muTausChargeNot2','PATMuTauPairSelector','abs(leg2.charge())==1','MTChargeIsABS1',1)
MTanalysisConfigurator.addSorter('muTausSorted','PATMuTauPairSorter')
#MTanalysisConfigurator.addSelector('muTausMuonIsolation','PATMuTauPairSelector','leg1.userFloat("dBRelIso")<0.15','MTMuonIsolation',1)
#MTanalysisConfigurator.addSelector('muTausTauID','PATMuTauPairSelector','leg2.tauID("byTightIsolationMVArun2v1DBoldDMwLT")>0.5','MTTauID',1)
#MTanalysisConfigurator.addSelector('muTausTauElectronVeto','PATMuTauPairSelector','leg2.tauID("againstElectronVLooseMVA6")>0.5','MTAgainstElectron',1)
#MTanalysisConfigurator.addSelector('muTausTauMuonVeto','PATMuTauPairSelector','leg2.tauID("againstMuonLoose3")>0','MTAgainstMuon',1)
MTanalysisConfigurator.addSelector('muTausOS','PATMuTauPairSelector','charge==0','MTOS',1)


#create the sequence
selectionSequenceMT =MTanalysisConfigurator.returnSequence()



###############################			Tau-Tau 		###################################
TTanalysisConfigurator = CutSequenceProducer(initialCounter  = 'initialEventsTT',
                                  pyModuleName = __name__,
                                  pyNameSpace  = locals())

TTanalysisConfigurator.addSmearing('patOverloadedTaus','triggeredPatMuons','triggeredPatElectrons','filteredJets','slimmedMETs','TT')

TTanalysisConfigurator.addDiCandidateModule('diNonBoostTaus','PATDiTauPairProducer','slimmedTaus','slimmedTaus','smearedMETTT','slimmedTaus','smearedJetsTT',1,9999,text = '',leadingObjectsOnly = False,dR = 0.3,recoMode = "",genParticles='prunedGenParticles')
TTanalysisConfigurator.addSelector('diNonBoostTausID','PATDiTauPairSelector','leg1.pt()>40&&leg2.pt()>40&&leg1.tauID("decayModeFinding")>0.5&&leg2.tauID("decayModeFinding")>0.5&&leg1.tauID("byLooseIsolationMVArun2v1DBdR03oldDMwLT")&&leg2.tauID("byLooseIsolationMVArun2v1DBdR03oldDMwLT")','DiNonBoostTauCreationMT',0,100)
TTanalysisConfigurator.addSorter('diNonBoostTausOSSorted','PATDiTauPairSorter')

#
#Make DiTaus
TTanalysisConfigurator.addDiCandidateModule('diTaus','PATDiTauPairProducer','smearedTausTT','smearedTausTT','smearedMETTT','smearedTausTT','smearedJetsTT',1,9999,text = 'AtLeastOneDiTau',leadingObjectsOnly = False,dR = 0.6,recoMode = "",genParticles='prunedGenParticles',drmax=True)

TTanalysisConfigurator.addSelector('diTausTau1PtEta','PATDiTauPairSelector','leg1.pt()>40&&abs(leg1.eta())<1.47','TTTau1PtEta',1)
TTanalysisConfigurator.addSelector('diTausTau2PtEta','PATDiTauPairSelector','leg2.pt()>40&&abs(leg2.eta())<1.47','TTTau2PtEta',1)
TTanalysisConfigurator.addSelector('diTaus1DecayFound','PATDiTauPairSelector','leg1.tauID("decayModeFinding")>0.5','TTTau1DecayFound',1)
TTanalysisConfigurator.addSelector('diTaus2DecayFound','PATDiTauPairSelector','leg2.tauID("decayModeFinding")>0.5','TTTau2DecayFound',1)
TTanalysisConfigurator.addSelector('diTaus1DecayVertex','PATDiTauPairSelector','abs(leg1.userFloat("taudZ"))<0.2','TTTau1VertexFound',1)
TTanalysisConfigurator.addSelector('diTaus2DecayVertex','PATDiTauPairSelector','abs(leg2.userFloat("taudZ"))<0.2','TTTau2VertexFound',1)
TTanalysisConfigurator.addSelector('diTaus1TauLooseIsolation','PATDiTauPairSelector','leg1.tauID("byLooseIsolationMVArun2v1DBdR03oldDMwLT") > 0.5','TTTauLooseIso1',1)
TTanalysisConfigurator.addSelector('diTaus2TauLooseIsolation','PATDiTauPairSelector','leg2.tauID("byLooseIsolationMVArun2v1DBdR03oldDMwLT") > 0.5','TTTauLooseIso2',1)
TTanalysisConfigurator.addSelector('diTausChargeNot2','PATDiTauPairSelector','abs(leg1.charge())==1&&abs(leg2.charge())==1','TTChargeIsABS1',1)
TTanalysisConfigurator.addDiTauLVeto('diTausLVeto','TightElectrons','TightMuons')
TTanalysisConfigurator.addSelector('diTausLeptVeto','PATDiTauPairSelector','lVeto==0','TTLVeto',1)
TTanalysisConfigurator.addSorter('diTausSorted','PATDiTauPairSorter')
#TTanalysisConfigurator.addSelector('diTausTau1Isolation','PATDiTauPairSelector','leg1.tauID("byMediumIsolationMVArun2v1DBdR03oldDMwLT") > 0.5','TTTauMediumIso1',1)
#TTanalysisConfigurator.addSelector('diTausTau2Isolation','PATDiTauPairSelector','leg2.tauID("byMediumIsolationMVArun2v1DBdR03oldDMwLT") > 0.5','TTTauMediumIso2',1)
TTanalysisConfigurator.addSelector('diTausTau1MuonVeto','PATDiTauPairSelector','leg1.tauID("againstMuonLoose3")','TTAgainstMuon1',1)
TTanalysisConfigurator.addSelector('diTausTau2MuonVeto','PATDiTauPairSelector','leg2.tauID("againstMuonLoose3")','TTAgainstMuon2',1)
TTanalysisConfigurator.addSelector('diTausTau1ElectronVeto','PATDiTauPairSelector','leg1.tauID("againstElectronVLooseMVA6")>0','TTAgainstElectron1',1)
TTanalysisConfigurator.addSelector('diTausTau2ElectronVeto','PATDiTauPairSelector','leg2.tauID("againstElectronVLooseMVA6")>0','TTAgainstElectron2',1)
TTanalysisConfigurator.addSelector('diTausOS','PATDiTauPairSelector','charge==0','TTOS',1)

#create the sequence
selectionSequenceTT =TTanalysisConfigurator.returnSequence()

