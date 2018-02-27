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
MTKanalysisConfigurator.addSelector('muTracksMuonPtEta','PATMuTrackPairSelector','leg1.pt()>50&&abs(leg1.eta())<2.4','MTKMuonPtEta',1)
MTKanalysisConfigurator.addSelector('muTracksTrackPtEta','PATMuTrackPairSelector','leg2.pt()>50&&abs(leg2.eta())<2.4','MTKTrackPtEta',1)
MTKanalysisConfigurator.addSelector('muTracksMuonMediumID','PATMuTrackPairSelector','leg1.userInt("tightID")>0','MTKMuonTightID',1)
MTKanalysisConfigurator.addSelector('muTracksMuonVertices','PATMuTrackPairSelector','abs(leg1.userFloat("dZ"))<0.2&&abs(leg1.userFloat("dXY"))<0.045','MTKMuonVertices',1)
MTKanalysisConfigurator.addMuTrackLVeto('muTracksLVeto','TightElectrons','TightMuons')
MTKanalysisConfigurator.addMuTrackLeptonIso('muTracksLIso')
MTKanalysisConfigurator.addSelector('muTracksMuonVeto','PATMuTrackPairSelector','lVeto==0','MTKMuonVeto',1)
MTKanalysisConfigurator.addSorter('muTracksSorted','PATMuTrackPairSorter')
MTKanalysisConfigurator.addSelector('muTracksOS','PATMuTrackPairSelector','charge==0','MTKOS',1)

#create the sequence
selectionSequenceMTK =MTKanalysisConfigurator.returnSequence()

