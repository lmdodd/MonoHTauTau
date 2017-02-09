import FWCore.ParameterSet.Config as cms

from MonoHTauTau.Configuration.tools.analysisToolsBoostedHiggsObject import TriggerPaths,TriggerRes,TriggerProcess,TriggerFilter



def makeCollSize(srcName,tagName):
    PSet = cms.PSet(
            pluginType = cms.string("CollectionSizeFiller"),
            src        = cms.InputTag(srcName),
            tag        = cms.string(tagName)
            )
    return PSet

def makeCollSizeVeto(srcName,size, tagName):
    PSet = cms.PSet(
            pluginType = cms.string("CollectionSizeVetoFiller"),
            src        = cms.InputTag(srcName),
            size       = cms.untracked.double(size),
            tag        = cms.string(tagName)
            )
    return PSet

def makeCollSizeOS(srcName,size, tagName):
    PSet = cms.PSet(
            pluginType = cms.string("OSCollectionSizeFiller"),
            src        = cms.InputTag(srcName),
            size       = cms.untracked.double(size),
            tag        = cms.string(tagName)
            )
    return PSet

def makeLTrackGeneric(plugin,sourceDiTaus,tagName,methodName):
    PSet = cms.PSet(
            pluginType  = cms.string(plugin),
            src         = cms.InputTag(sourceDiTaus),
            tag         = cms.string(tagName),
            method      = cms.string(methodName),
            )
    return PSet
def makeMuTrackPair(sourceDiTaus,tagName,methodName,leadingOnly=True):
    PSet = cms.PSet(
            pluginType  = cms.string("PATMuTrackPairFiller"),
            src         = cms.InputTag(sourceDiTaus),
            tag         = cms.string(tagName),
            method      = cms.string(methodName),
            leadingOnly = cms.untracked.bool(leadingOnly)
            )
    return PSet
def makeMuTrackMET(sourceDiTaus, sourceMET, prefix):
   PSet = cms.PSet(
         pluginType  = cms.string("PATMuTrackPairMETFiller"),
         src         = cms.InputTag(sourceDiTaus),
         met         = cms.InputTag(sourceMET),
         tag         = cms.string(prefix)
   )
   return PSet
def makeMuTrackMETUncert(sourceDiTaus, sourceMET, prefix, shift):
   PSet = cms.PSet(
         pluginType  = cms.string("PATMuTrackPairMETFillerUncert"),
         src         = cms.InputTag(sourceDiTaus),
         met         = cms.InputTag(sourceMET),
         tag         = cms.string(prefix),
         uncert      = cms.string(shift) #EnUp or EnDown Available
   )
   return PSet
def makeMuTrackPOGSF(sourceDiTaus):
   PSet = cms.PSet(
         pluginType  = cms.string("PATMuTrackPairPOGSFsFiller"),
         src         = cms.InputTag(sourceDiTaus),
         isMu      = cms.bool(True)
   )
   return PSet
def makeMuTrackJetCountPair(sourceDiTaus,tagName,methodName,leadingOnly=True):
    PSet = cms.PSet(
            pluginType  = cms.string("PATMuTrackPairJetCountFiller"),
            src         = cms.InputTag(sourceDiTaus),
            tag         = cms.string(tagName),
            method      = cms.string(methodName),
            leadingOnly = cms.untracked.bool(leadingOnly)
            )
    return PSet
def makeMuTrackTauEffCSV(sourceDiTaus):
   PSet = cms.PSet(
         pluginType  = cms.string("PATMuTrackPairEffCSVFiller"),
         src         = cms.InputTag(sourceDiTaus)
   )
   return PSet


###############di-Tau#################
def makeDiTauPair(sourceDiTaus,tagName,methodName,leadingOnly=True):
   PSet = cms.PSet(
         pluginType  = cms.string("PATDiTauPairFiller"),
         src         = cms.InputTag(sourceDiTaus),
         tag         = cms.string(tagName),
         method      = cms.string(methodName),
         leadingOnly = cms.untracked.bool(leadingOnly)
   )
   return PSet
def makeDiTauMET(sourceDiTaus, sourceMET, prefix):
   PSet = cms.PSet(
         pluginType  = cms.string("PATDiTauPairMETFiller"),
         src         = cms.InputTag(sourceDiTaus),
         met         = cms.InputTag(sourceMET),
         tag         = cms.string(prefix)
   )
   return PSet
def makeDiTauEffCSV(sourceDiTaus):
   PSet = cms.PSet(
         pluginType  = cms.string("PATDiTauPairEffCSVFiller"),
         src         = cms.InputTag(sourceDiTaus)
   )
   return PSet
def makeDiTauCSVShape(sourceDiTaus):
   PSet = cms.PSet(
         pluginType  = cms.string("PATDiTauPairCSVReweightFiller"),
         src         = cms.InputTag(sourceDiTaus)
   )
   return PSet
def makeDiTauMETUncert(sourceDiTaus, sourceMET, prefix, shift):
   PSet = cms.PSet(
         pluginType  = cms.string("PATDiTauPairMETFillerUncert"),
         src         = cms.InputTag(sourceDiTaus),
         met         = cms.InputTag(sourceMET),
         tag         = cms.string(prefix),
         uncert      = cms.string(shift) #EnUp or EnDown Available
   )
   return PSet
def makeDiTauJetCountPair(sourceDiTaus,tagName,methodName,leadingOnly=True):
    PSet = cms.PSet(
            pluginType  = cms.string("PATDiTauPairJetCountFiller"),
            src         = cms.InputTag(sourceDiTaus),
            tag         = cms.string(tagName),
            method      = cms.string(methodName),
            leadingOnly = cms.untracked.bool(leadingOnly)
            )
    return PSet




def addMuTrackEventTree(process,name,src = 'muTracksSorted', srcLL = 'diMuonsOSSorted', srcU='TightMuons', srcE='TightElectrons', srcT='TightTaus'):
    process.TFileService = cms.Service("TFileService", fileName = cms.string("analysis.root") )
    eventTree = cms.EDAnalyzer('EventTreeMaker',
           genEvent = cms.InputTag('generator'),
           coreCollections = cms.InputTag(src),
           trigger = cms.PSet(
               pluginType = cms.string("TriggerFiller"),
               #src        = cms.InputTag("TriggerResults","","HLT"),
               src = cms.InputTag(TriggerRes,"",TriggerProcess),
               prescales = cms.InputTag("patTrigger"),
               paths      = cms.vstring(TriggerPaths)
               ),
           metfilter = cms.PSet(
               pluginType = cms.string("TriggerFilterFiller"),
               src = cms.InputTag(TriggerRes,"",TriggerFilter),
               BadChargedCandidateFilter = cms.InputTag("BadChargedCandidateFilter"),
               BadPFMuonFilter           = cms.InputTag("BadPFMuonFilter"),
               paths      = cms.vstring(
                   "Flag_HBHENoiseFilter",
                   "Flag_HBHENoiseIsoFilter", 
                   "Flag_globalTightHalo2016Filter",
                   "Flag_goodVertices",
                   "Flag_eeBadScFilter",
                   "Flag_EcalDeadCellTriggerPrimitiveFilter"
                   )
               ),

           pu = cms.PSet(
               pluginType = cms.string("PUFiller"),
               src        = cms.InputTag("slimmedAddPileupInfo"),
               tag        = cms.string("pu")
               ),
           cov = cms.PSet(
               pluginType = cms.string("METSignificanceFiller"),
               src        = cms.InputTag("METSignificance"),
               tag        = cms.string("metcov")
               ),
           PVsSync = cms.PSet(
               pluginType = cms.string("VertexSizeFiller"),
               src        = cms.InputTag("offlineSlimmedPrimaryVertices"),
               tag        = cms.string("npv")
               ),
           PVs = cms.PSet(
               pluginType = cms.string("VertexSizeFiller"),
               src        = cms.InputTag("offlineSlimmedPrimaryVertices"),
               tag        = cms.string("vertices")
               ),
           muTrackPOG = makeMuTrackPOGSF(src),#FILLED

           muTrackSize = makeCollSize(src,"nCands"),
           muTrackOS = makeCollSizeOS(src,0,"os"),
           genTaus = makeCollSize("genTauCands","genTaus"), 
           muMuSize = makeCollSize(srcLL,"diLeptons"),#CHECKME
           muMuSizeVeto = makeCollSizeVeto(srcLL,0,"dilepton_veto"),#CHECKME

           muonsSizeMT = makeCollSize(srcU,"tightMuons"),
           tausSizeMT = makeCollSize(srcT,"tightTaus"),
           muonsSizeMTVeto = makeCollSizeVeto(srcU,1,"extramuon_veto"),
           electronsSizeMT = makeCollSize(srcE,"tightElectrons"),
           electronsSizeMTVeto = makeCollSizeVeto(srcE,0,"extraelec_veto"),

           muTrackDR = makeMuTrackPair(src,"dR","dR12"), 

           muTrackCharge = makeMuTrackPair(src,"charge","charge"),
           q_1 = makeMuTrackPair(src,"q_1","leg1.charge"),
           q_2 = makeMuTrackPair(src,"q_2","leg2.charge"),
           muTrackPt = makeMuTrackPair(src,"pth","pt"),
           muTrackHT = makeMuTrackPair(src,"ht","ht"),
           muTrackMass = makeMuTrackPair(src,"m_vis","mass"),
           muTracklVeto = makeMuTrackPair(src,"lVeto","lVeto"),
           muTracklIso = makeMuTrackPair(src,"lIso","lIso"),

           muTrackFullPt = makeMuTrackPair(src,"fullPt","fullPt"),
           muTrackEta = makeMuTrackPair(src,"fullEta","fullEta"),
           muTrackPhi = makeMuTrackPair(src,"fullPhi","fullPhi"),
           muTrackE = makeMuTrackPair(src,"fullEnergy","fullEnergy"),

           muTrackPt1 =  makeMuTrackPair(src,"pt_1","leg1.pt"), 
           muTrackPt2 =  makeMuTrackPair(src,"pt_2","leg2.pt"), 
           muTrackEta1 = makeMuTrackPair(src,"eta_1","leg1.eta"),
           muTrackEta2 = makeMuTrackPair(src,"eta_2","leg2.eta"),
           muTrackPhi1 = makeMuTrackPair(src,"phi_1","leg1.phi"),
           muTrackPhi2 = makeMuTrackPair(src,"phi_2","leg2.phi"),

           muTrackMassLL = makeLTrackGeneric("PATMuPairFiller",srcLL,"LLmass","mass"),
           muTrackPt1LL =  makeLTrackGeneric("PATMuPairFiller",srcLL,"LLpt_1","leg1.pt"), 
           muTrackPt2LL =  makeLTrackGeneric("PATMuPairFiller",srcLL,"LLpt_2","leg2.pt"), 
           muTrackEta1LL = makeLTrackGeneric("PATMuPairFiller",srcLL,"LLeta_1","leg1.eta"),
           muTrackEta2LL = makeLTrackGeneric("PATMuPairFiller",srcLL,"LLeta_2","leg2.eta"),
           muTrackPhi1LL = makeLTrackGeneric("PATMuPairFiller",srcLL,"LLphi_1","leg1.phi"),
           muTrackPhi2LL = makeLTrackGeneric("PATMuPairFiller",srcLL,"LLphi_2","leg2.phi"),

           muTrackMET1 = makeMuTrackMET(src,"slimmedMETs","pf"),
           muTrackMET2 = makeMuTrackMET(src,"slimmedMETsPuppi","puppi"),
           muTrackMETUncertUp = makeMuTrackMETUncert(src,"slimmedMETs","pf","EnUp"),#FILLED
           muTrackMETUncertDown = makeMuTrackMETUncert(src,"slimmedMETs","pf","EnDown"),#FILLED
 
           muTrackMET = makeMuTrackPair(src,"met","met.pt()"),
           muTrackMETPhi = makeMuTrackPair(src,"metphi","met.phi()"),

           muTrackMT = makeMuTrackPair(src,"mt12","mt12MET"),
           muTrackMT1 = makeMuTrackPair(src,"mt_1","mt1MET"),
           muTrackMT2 = makeMuTrackPair(src,"mt_2","mt2MET"),

           muTrackMJJ = makeMuTrackPair(src,"mJJ","mJJ"),
           muTrackJJPt = makeMuTrackPair(src,"ptJJ","ptJJ"),
           muTrackJJEta = makeMuTrackPair(src,"etaJJ","etaJJ"),
           muTrackJJPhi = makeMuTrackPair(src,"phiJJ","phiJJ"),
           muTrackJJEnergy = makeMuTrackPair(src,"energyJJ","energyJJ"),
           muTrackVBFDEta = makeMuTrackPair(src,"jdeta","vbfDEta"),
           muTrackVBFMass = makeMuTrackPair(src,"mjj","vbfMass"),#vbfMass
           muTrackVBFJets20 = makeMuTrackPair(src,"njetigap20","vbfNJetsGap20"),
           muTrackVBFJets30 = makeMuTrackPair(src,"njetingap","vbfNJetsGap30"),

           #Muon IDs and Isolation
           muTrackRelPFIsoDB03 = makeMuTrackPair(src,"iso_1",'leg1.userFloat("dBRelIso03")'),
           muTrackRelPFIsoDB04 = makeMuTrackPair(src,"iso04_1",'leg1.userFloat("dBRelIso")'),
           muTracksumCharged04 = makeMuTrackPair(src,"sumChargedHadronPt04_1",'leg1.pfIsolationR04().sumChargedHadronPt'),
           muTracksumNeutral04 = makeMuTrackPair(src,"sumNeutralHadronPt04_1",'leg1.pfIsolationR04().sumNeutralHadronEt'),
           muTracksumPhoton04 = makeMuTrackPair(src,"sumPhotonPt04_1",'leg1.pfIsolationR04().sumPhotonEt'),
           muTracksumPU04 = makeMuTrackPair(src,"sumPUPt04_1",'leg1.pfIsolationR04().sumPUPt'),

           muTracksumCharged03 = makeMuTrackPair(src,"sumChargedHadronPt03_1",'leg1.pfIsolationR03().sumChargedHadronPt'),
           muTracksumNeutral03 = makeMuTrackPair(src,"sumNeutralHadronPt03_1",'leg1.pfIsolationR03().sumNeutralHadronEt'),
           muTracksumPhoton03 = makeMuTrackPair(src,"sumPhotonPt03_1",'leg1.pfIsolationR03().sumPhotonEt'),
           muTracksumPU03 = makeMuTrackPair(src,"sumPUPt03_1",'leg1.pfIsolationR03().sumPUPt'),

           muTrackLooseID = makeMuTrackPair(src,"id_m_loose_1",'leg1.isLooseMuon()'),
           muTrackMediumID = makeMuTrackPair(src,"id_m_medium_1_INVALID",'leg1.isMediumMuon()'),
           muTrackUserMediumID = makeMuTrackPair(src,"id_m_medium_1",'leg1.userInt("mediumID")'),
           muTrackTightID = makeMuTrackPair(src,"id_m_tight_1",'leg1.userInt("tightID")'),
           #muTrackMuTriggerMatch = makeMuTrackPair(src,"lTrigger",'leg1.userFloat("hltL3crIsoL1sMu20L1f0L2f10QL3f22QL3trkIsoFiltered0p09")'),
           muTrackPzeta = makeMuTrackPair(src,"pZeta",'pZeta-1.5*pZetaVis'),
           muTrackPZ = makeMuTrackPair(src,"pZ",'pZeta'),
           muTrackPZV = makeMuTrackPair(src,"pzetavis",'pZetaVis'),
           muTrackHadMass = makeMuTrackPair(src,"m_2",'leg2.mass()'),

           muTrackMuDZ = makeMuTrackPair(src,"dZ_1","leg1.userFloat('dZ')"),
           muTrackTauDZ = makeMuTrackPair(src,"dZ_2","leg2.dz"),
           muTrackMuDXY = makeMuTrackPair(src,"d0_1","leg1.userFloat('dXY')"),
           muTrackTauDXY = makeMuTrackPair(src,"d0_2","leg2.dxy"),


           muTrackGenPt1 = makeMuTrackPair(src,"genPt1",'p4Leg1gen().pt()'),
           muTrackGenPt2 = makeMuTrackPair(src,"genPt2",'p4Leg2gen().pt()'),
           muTrackPdg1 = makeMuTrackPair(src,"pdg1",'genPdg1()'),
           muTrackPdg2 = makeMuTrackPair(src,"pdg2",'genPdg2()'),
           muTrackVisGenPt1 = makeMuTrackPair(src,"genVisPt1",'p4VisLeg1gen().pt()'),
           muTrackVisGenPt2 = makeMuTrackPair(src,"genVisPt2",'p4VisLeg2gen().pt()'),
           muTrackGenVisMass = makeMuTrackPair(src,"genVisMass",'p4VisGen().M()'),
           muTrackGenMassMatched = makeMuTrackPair(src,"genFullMassMatched",'p4gen().M()'),
           muTrackGenMass = makeMuTrackPair(src,"fullGenMass",'genBosonMass()'),
           muTrackGenBosonPt = makeMuTrackPair(src,"genpT",'p4GenBoson().pt()'),
           muTrackGenBosonMass = makeMuTrackPair(src,"genMass",'p4GenBoson().M()'),
           muTrackGenBosonPx = makeMuTrackPair(src,"genpX",'p4GenBoson().px()'),
           muTrackGenBosonPy = makeMuTrackPair(src,"genpY",'p4GenBoson().py()'),
           muTrackGenBosonVisPx = makeMuTrackPair(src,"vispX",'p4GenBosonVis().px()'),
           muTrackGenBosonVisPy = makeMuTrackPair(src,"vispY",'p4GenBosonVis().py()'),
           muTrackGenIsPrompt1 = makeMuTrackPair(src,"isPrompt1",'isPrompt1()'),
           muTrackGenIsPromptFS1 = makeMuTrackPair(src,"isPromptFS1",'isPromptFS1()'),
           muTrackGenIsDirectTauDecay1 = makeMuTrackPair(src,"isTauDecay1",'isDirectPromptTauDecayProduct1()'),
           muTrackGenIsDirectTauDecayFS1 = makeMuTrackPair(src,"isTauDecayFS1",'isDirectPromptTauDecayProductFS1()'),
           muTrackGenIsPrompt2 = makeMuTrackPair(src,"isPrompt2",'isPrompt2()'),
           muTrackGenIsPromptFS2 = makeMuTrackPair(src,"isPromptFS2",'isPromptFS2()'),
           muTrackGenIsDirectTauDecay2 = makeMuTrackPair(src,"isTauDecay2",'isDirectPromptTauDecayProduct2()'),
           muTrackGenIsDirectTauDecayFS2 = makeMuTrackPair(src,"isTauDecayFS2",'isDirectPromptTauDecayProductFS2()'),
           #Jets
           muTrackJetsPt20nbtag = makeMuTrackJetCountPair(src,"nbtag",'userFloat("isbtagged")&&pt()>20&&abs(eta)<2.4&&userFloat("idLoose")&&bDiscriminator("pfCombinedInclusiveSecondaryVertexV2BJetTags")>.8484'),
           muTrackJetsPt20nbtagLoose = makeMuTrackJetCountPair(src,"nbtagLooseNoSF",'pt()>20&&abs(eta)<2.4&&userFloat("idLoose")&&bDiscriminator("pfCombinedInclusiveSecondaryVertexV2BJetTags")>0.5426'),
           muTrackJetsPt20nbtagNoSF = makeMuTrackJetCountPair(src,"nbtagNoSF",'pt()>20&&abs(eta)<2.4&&userFloat("idLoose")&&bDiscriminator("pfCombinedInclusiveSecondaryVertexV2BJetTags")>.8484'),
           muTrackJetsPt30nbtagNoSf = makeMuTrackJetCountPair(src,"nbtag30",'userFloat("isbtagged")&&pt()>30&&abs(eta)<2.4&&userFloat("idLoose")&&bDiscriminator("pfCombinedInclusiveSecondaryVertexV2BJetTags")>.8484'),
           muTrackJetsPt30nbtag = makeMuTrackJetCountPair(src,"nbtag30",'pt()>30&&abs(eta)<2.4&&userFloat("idLoose")&&bDiscriminator("pfCombinedInclusiveSecondaryVertexV2BJetTags")>.8484'),
           muTrackJetsPt30njets = makeMuTrackJetCountPair(src,"njets",'pt()>30&&abs(eta)<4.7&&userFloat("idLoose")'),
           muTrackJetsPt30njetsnopu = makeMuTrackJetCountPair(src,"njetspuID",'pt()>30&&abs(eta)<4.7&&userFloat("idLoose")&&!userFloat("puIDLoose")'),
           muTrackJetsPt20njets = makeMuTrackJetCountPair(src,"njetspt20",'pt()>20&&abs(eta)<4.7&&userFloat("idLoose")'),
           muTrackJetsPt20njetsnopu = makeMuTrackJetCountPair(src,"njetspt20puID",'pt()>20&&abs(eta)<4.7&&userFloat("idLoose")&&!userFloat("puIDLoose")'),
           muTrackJetsPt20TagMatch = makeMuTrackJetCountPair(src,"nTaggableJetsPt20Matched",'pt()>20&&abs(eta)<2.4&&abs(partonFlavour)==5'),
           muTrackJetsPt20TagNoMatch = makeMuTrackJetCountPair(src,"nTaggableJetsPt20NotMatched",'pt()>30&&abs(eta)<2.4&&abs(partonFlavour)!=5'),
           mumuDR = makeLTrackGeneric("PATMuPairFiller",srcLL,"diLeptonDR","dR12"),#FIXME

           higgsPt = cms.PSet(
                   pluginType = cms.string("PATGenParticleFiller"),
                   src        = cms.InputTag("genDaughters"),
                   tag        = cms.string("higgsPt"),
                   method     = cms.string('pt()'),
                   leadingOnly=cms.untracked.bool(True)
                   ), 

           muTrackLHEProduct = cms.PSet(
                   pluginType = cms.string("LHEProductFiller"),
                   src        = cms.InputTag("externalLHEProducer"),
                   tag        = cms.string("LHEProduct"),
                   ),
           muTrackEmbedPtWeight = cms.PSet(
                   pluginType = cms.string("GenFilterInfoWeightFiller"),
                   src        = cms.InputTag("generator"),
                   #src        = cms.InputTag("generator","EmbWeight"),
                   tag        = cms.string("aMCNLO_weight"),
                   ),#FIXME #CHECKME
           muTrackEmbedPt = cms.PSet(
                   pluginType = cms.string("PATGenParticleFiller"),
                   src        = cms.InputTag("genDaughters"),
                   tag        = cms.string("embeddedPt"),#CHECKME
                   method     = cms.string("pt"),
                   leadingOnly=cms.untracked.bool(False)
                   ),#FIXME #CHECKME
           muTrackEmbedEta = cms.PSet(
                   pluginType = cms.string("PATGenParticleFiller"),
                   src        = cms.InputTag("genDaughters"),
                   tag        = cms.string("embeddedEta"),
                   method     = cms.string("eta"),
                   leadingOnly=cms.untracked.bool(False)
                   )#FIXME #CHECKME

           )

    setattr(process, name, eventTree)
    p = cms.Path(getattr(process,name))
    setattr(process, name+'Path', p)






#####################################################################
#####################################################################
#####################################################################
#####################################################################
#####################################################################
#######################   L-Tau THINGS  #############################
#####################################################################
#####################################################################
#####################################################################
#####################################################################
#####################################################################
#####################################################################

#######################   L-Tau  #############################
def makeLTauGeneric(plugin,sourceDiTaus,tagName,methodName):
   PSet = cms.PSet(
         pluginType  = cms.string(plugin),
         src         = cms.InputTag(sourceDiTaus),
         tag         = cms.string(tagName),
         method      = cms.string(methodName),
   )
   return PSet

#######################   L-Tau  #############################
def makeMuTauPair(sourceDiTaus,tagName,methodName,leadingOnly=True):
   PSet = cms.PSet(
         pluginType  = cms.string("PATMuTauPairFiller"),
         src         = cms.InputTag(sourceDiTaus),
         tag         = cms.string(tagName),
         method      = cms.string(methodName),
         leadingOnly = cms.untracked.bool(leadingOnly)
   )
   return PSet
def makeMuTauCSVPair(sourceDiTaus,tagName,cutName,methodName,rank):
   PSet = cms.PSet(
         pluginType  = cms.string("PATMuTauPairCSVJetVarFiller"),
         src         = cms.InputTag(sourceDiTaus),
         tag         = cms.string(tagName),
         cut         = cms.string(cutName),
         method      = cms.string(methodName),
         rank = cms.untracked.double(rank)
   )
   return PSet
def makeMuTauPtNoPair(sourceDiTaus,tagName,cutName,methodName,rank):
   PSet = cms.PSet(
         pluginType  = cms.string("PATMuTauPairPtJetVarFiller"),
         src         = cms.InputTag(sourceDiTaus),
         tag         = cms.string(tagName),
         cut         = cms.string(cutName),
         method      = cms.string(methodName),
         rank = cms.untracked.double(rank)
   )
   return PSet
def makeMuTauPtPair(sourceDiTaus,tagName,cutName,methodName,rank):
   PSet = cms.PSet(
         pluginType  = cms.string("PATMuTauPairPtJetPairVarFiller"),
         src         = cms.InputTag(sourceDiTaus),
         tag         = cms.string(tagName),
         cut         = cms.string(cutName),
         method      = cms.string(methodName),
         rank = cms.untracked.double(rank)
   )
   return PSet
def makeMuTauMET(sourceDiTaus, sourceMET, prefix):
   PSet = cms.PSet(
         pluginType  = cms.string("PATMuTauPairMETFiller"),
         src         = cms.InputTag(sourceDiTaus),
         met         = cms.InputTag(sourceMET),
         tag         = cms.string(prefix)
   )
   return PSet
def makeMuTauEventWeight(sourceDiTaus):
   PSet = cms.PSet(
         pluginType  = cms.string("PATMuTauPairWeightFiller"),
         src         = cms.InputTag(sourceDiTaus),
         tag         = cms.string("Mu"),
         isMuon      = cms.bool(True)
   )
   return PSet
def makeMuTauPOGSF(sourceDiTaus):
   PSet = cms.PSet(
         pluginType  = cms.string("PATMuTauPairPOGSFsFiller"),
         src         = cms.InputTag(sourceDiTaus),
         isMu      = cms.bool(True)
   )
   return PSet
def makeMuTauEventWeightTmp(sourceDiTaus):
   PSet = cms.PSet(
         pluginType  = cms.string("PATMuTauPairWeightFillerTmp"),
         src         = cms.InputTag(sourceDiTaus),
         tag         = cms.string("MyMu"),
         isMuon      = cms.bool(True)
   )
   return PSet
def makeMuTauGenMatch(sourceDiTaus):
   PSet = cms.PSet(
         pluginType  = cms.string("PATMuTauPairGenMCMatching"),
         src         = cms.InputTag(sourceDiTaus)
   )
   return PSet
def makeMuTauEffCSV(sourceDiTaus):
   PSet = cms.PSet(
         pluginType  = cms.string("PATMuTauPairEffCSVFiller"),
         src         = cms.InputTag(sourceDiTaus)
   )
   return PSet

def makeMuTauCSVShape(sourceDiTaus):
   PSet = cms.PSet(
         pluginType  = cms.string("PATMuTauPairCSVReweightFiller"),
         src         = cms.InputTag(sourceDiTaus)
   )
   return PSet
def makeMuTauJetCountPair(sourceDiTaus,tagName,methodName,leadingOnly=True):
   PSet = cms.PSet(
         pluginType  = cms.string("PATMuTauPairJetCountFiller"),
         src         = cms.InputTag(sourceDiTaus),
         tag         = cms.string(tagName),
         method      = cms.string(methodName),
         leadingOnly = cms.untracked.bool(leadingOnly)
   )
   return PSet



def addMuTauEventTree(process,name,src = 'muTausSorted', srcLL = 'diMuonsOSSorted', srcU='TightMuons', srcE='TightElectrons',srcT='TightTaus'):
   process.TFileService = cms.Service("TFileService", fileName = cms.string("analysis.root") )
   eventTree = cms.EDAnalyzer('EventTreeMaker',
                              genEvent = cms.InputTag('generator'),
                              coreCollections = cms.InputTag(src),
                              trigger = cms.PSet(
                                  pluginType = cms.string("TriggerFiller"),
                                  src = cms.InputTag(TriggerRes,"",TriggerProcess),
                                   prescales = cms.InputTag("patTrigger"),
                                  paths      = cms.vstring(TriggerPaths)
                                  ),

                              metfilter = cms.PSet(
                                  pluginType = cms.string("TriggerFilterFiller"),
                                  src = cms.InputTag(TriggerRes,"",TriggerFilter),
                                  BadChargedCandidateFilter = cms.InputTag("BadChargedCandidateFilter"),
                                  BadPFMuonFilter           = cms.InputTag("BadPFMuonFilter"),
                                  paths      = cms.vstring(
                                      "Flag_HBHENoiseFilter",
                                      "Flag_HBHENoiseIsoFilter", 
                                      "Flag_globalTightHalo2016Filter",
                                      "Flag_goodVertices",
                                      "Flag_eeBadScFilter",
                                      "Flag_EcalDeadCellTriggerPrimitiveFilter"
                                      )
                                  ),


                              pu = cms.PSet(
                                  pluginType = cms.string("PUFiller"),
                                  src        = cms.InputTag("slimmedAddPileupInfo"),
                                  tag        = cms.string("pu")
                              ),
                              cov = cms.PSet(
                                  pluginType = cms.string("METSignificanceFiller"),
                                  src        = cms.InputTag("METSignificance"),
                                  tag        = cms.string("metcov")
                              ),
                              PVsSync = cms.PSet(
                                  pluginType = cms.string("VertexSizeFiller"),
                                  src        = cms.InputTag("offlineSlimmedPrimaryVertices"),
                                  tag        = cms.string("npv")
                              ),#FILLED
                              PVs = cms.PSet(
                                  pluginType = cms.string("VertexSizeFiller"),
                                  src        = cms.InputTag("offlineSlimmedPrimaryVertices"),
                                  tag        = cms.string("vertices")
                              ),#FILLED
 
                              muTauPOG = makeMuTauPOGSF(src),#FILLED
                              muTauEventWeight = makeMuTauEventWeight(src),#FILLED
                              muTauEventWeightTmp = makeMuTauEventWeightTmp(src),#FILLED
                              muTauGenMCMatch = makeMuTauGenMatch(src),#FILLED
                              muTauEffCSV = makeMuTauEffCSV(src),#FILLED
                              muTauCSVShape = makeMuTauCSVShape(src),#FILLED
                              muTauSize = makeCollSize(src,"nCands"),#FILLED
                              muTauOS = makeCollSizeOS(src,0,"os"),#FILLED
                              genTaus = makeCollSize("genTauCands","genTaus"), 
                              muMuSize = makeCollSize(srcLL,"diLeptons"),#CHECKME
                              muMuSizeVeto = makeCollSizeVeto(srcLL,0,"dilepton_veto"),#CHECKME

                              muonsSizeMT = makeCollSize(srcU,"tightMuons"),#FILLED
                              tausSizeMT = makeCollSize(srcT,"tightTaus"),#FILLED
                              muonsSizeMTVeto = makeCollSizeVeto(srcU,1,"extramuon_veto"),#FILLED
                              electronsSizeMT = makeCollSize(srcE,"tightElectrons"),#FILLED
                              electronsSizeMTVeto = makeCollSizeVeto(srcE,0,"extraelec_veto"),#FILLED

                              muTauDR = makeMuTauPair(src,"dR","dR12"), 
                              tauSingleL1 =  makeMuTauPair(src,"tauSingleL1_2","leg2.userFloat('LooseIsoPFTau20_SingleL1')"), 
                              tauL1 =  makeMuTauPair(src,"tauL1_2","leg2.userFloat('LooseIsoPFTau20')"), 
                              tauMediumL1 =  makeMuTauPair(src,"tauMediumL1_2","leg2.userFloat('MediumIsoPFTau35_Trk_eta2p1')"),

                              tauNIsoTracks =  makeMuTauPair(src,"tauNIsoTracks","leg2.userFloat('nIsoTracks')"), #FILLED
                              muTaunIsoGamma = makeMuTauPair(src,"nIsoGamma",'leg2.userFloat("nIsoGamma")'),
                              muTaunIsoNeutral = makeMuTauPair(src,"nIsoNeutral",'leg2.userFloat("nIsoNeutral")'),


                              tauNMatchedSeg =  makeMuTauPair(src,"tauMuonNMatchedSeg","leg2.userFloat('muonNMatchedSeg')"),#FILLED
                              tauTauHadMatched = makeMuTauPair(src,"tauMuonMatched","leg2.userFloat('muonTauHadMatched')"),#FILLED
                              tauLeadChargedHadrTrackPt = makeMuTauPair(src,"tauLeadChargedHadrTrackPt","leg2.userFloat('leadChargedHadrTrackPt')"),#FILLED

                              #mass2ES = makeMuTauPair(src,"mass2ES","leg2.userFloat('ESmass')"),#FILLED
                              #pt2ES = makeMuTauPair(src,"pt2ES","leg2.userFloat('ESpt')"),#FILLED
                              #pt2initial = makeMuTauPair(src,"pt2preES","leg2.userFloat('preESpt')"),#FILLED
                              #phi2initial = makeMuTauPair(src,"phi2preES","leg2.userFloat('preESphi')"),#FILLED

                              muTauCharge = makeMuTauPair(src,"charge","charge"),#FILLED
                              q_1 = makeMuTauPair(src,"q_1","leg1.charge"),#FILLED
                              q_2 = makeMuTauPair(src,"q_2","leg2.charge"),#FILLED

                              muTauPt = makeMuTauPair(src,"pth","pt"),#FILLED
                              muTauHT = makeMuTauPair(src,"ht","ht"),#FILLED
                              muTauMass = makeMuTauPair(src,"m_vis","mass"),#FILLED
                              #muTauSVPt = makeMuTauPair(src,"pt_sv","svPt"),#FILLEDATLATERSTAGE
                              #muTauSVMass = makeMuTauPair(src,"m_sv","svMass"),#FILLEDATLATERSTAGE
                  muTaulVeto = makeMuTauPair(src,"lVeto","lVeto"),

                              muTauFullPt = makeMuTauPair(src,"fullPt","fullPt"),#FILLED
                              muTauEta = makeMuTauPair(src,"fullEta","fullEta"),#FILLED
                              muTauPhi = makeMuTauPair(src,"fullPhi","fullPhi"),#FILLED
                              muTauE = makeMuTauPair(src,"fullEnergy","fullEnergy"),#FILLED

                              muTauPt1 =  makeMuTauPair(src,"pt_1","leg1.pt"), #FILLED
                              muTauPt2 =  makeMuTauPair(src,"pt_2","leg2.pt"), #FILLED
                              muTauEta1 = makeMuTauPair(src,"eta_1","leg1.eta"),#FILLED
                              muTauEta2 = makeMuTauPair(src,"eta_2","leg2.eta"),#FILLED
                              muTauPhi1 = makeMuTauPair(src,"phi_1","leg1.phi"),#FILLED
                              muTauPhi2 = makeMuTauPair(src,"phi_2","leg2.phi"),#FILLED

                  muTauMassLL = makeLTauGeneric("PATMuPairFiller",srcLL,"LLmass","mass"),
                              muTauPt1LL =  makeLTauGeneric("PATMuPairFiller",srcLL,"LLpt_1","leg1.pt"), #FILLED
                              muTauPt2LL =  makeLTauGeneric("PATMuPairFiller",srcLL,"LLpt_2","leg2.pt"), #FILLED
                              muTauEta1LL = makeLTauGeneric("PATMuPairFiller",srcLL,"LLeta_1","leg1.eta"),#FILLED
                              muTauEta2LL = makeLTauGeneric("PATMuPairFiller",srcLL,"LLeta_2","leg2.eta"),#FILLED
                              muTauPhi1LL = makeLTauGeneric("PATMuPairFiller",srcLL,"LLphi_1","leg1.phi"),#FILLED
                              muTauPhi2LL = makeLTauGeneric("PATMuPairFiller",srcLL,"LLphi_2","leg2.phi"),#FILLED

                              #muTauMETCal = makeMuTauPair(src,"metCal","calibratedMET.pt()"),#NOLONGLERUSED
                              #muTauMETPhi = makeMuTauPair(src,"metphi","metPhi"),#NOLONGERUSED
                              muTauMET1 = makeMuTauMET(src,"slimmedMETs","pf"),#FILLED
                              muTauMET2 = makeMuTauMET(src,"slimmedMETsPuppi","puppi"),#FILLED
                              muTauMET3 = makeMuTauMET(src,"MVAMET:MVAMET","mva"),#FILLED
 
                              #muTauGenMET = makeMuTauPair(src,"genMET","met.genMET().pt"),#FILLED
                              muTauMET = makeMuTauPair(src,"met","met.pt()"),#FILLED
                              muTauMETPhi = makeMuTauPair(src,"metphi","met.phi()"),#FILLED
                              #muTauMET = makeMuTauPair(src,"mvamet","met.pt()"),#FILLED
                              #muTauMETx = makeMuTauPair(src,"mvamet_ex","met.px()"),#FILLED
                              #muTauMETy = makeMuTauPair(src,"mvamet_ey","met.py()"),#FILLED
                              #muTauMETPhi = makeMuTauPair(src,"mvametphi","met.phi()"),#FILLED
                              #muTauMvaCovMat00 = makeMuTauPair(src,"mvacov00","covMatrix00"),#FIXME
                              #muTauMvaCovMat10 = makeMuTauPair(src,"mvacov10","covMatrix10"),#FIXME
                              #muTauMvaCovMat01 = makeMuTauPair(src,"mvacov01","covMatrix01"),#FIXME
                              #muTauMvaCovMat11 = makeMuTauPair(src,"mvacov11","covMatrix11"),#FIXME

                              muTauMT = makeMuTauPair(src,"mt12","mt12MET"),#FILLED
                              muTauMT1 = makeMuTauPair(src,"mt_1","mt1MET"),#FILLED
                              muTauMT2 = makeMuTauPair(src,"mt_2","mt2MET"),#FILLED

                              muTauTopGenPt = makeMuTauPair(src,"topGenPt","topGenPt"), #FIXME
                              muTauAntiTopGenPt = makeMuTauPair(src,"antiTopGenPt","antiTopGenPt"), #FIXME

                              #BTAGS AND JETS
                              muTauMJJReg = makeMuTauPair(src,"mJJReg","mJJReg"),#FIXME
                              muTauMJJ = makeMuTauPair(src,"mJJ","mJJ"),#FILLED
                              muTauJJPt = makeMuTauPair(src,"ptJJ","ptJJ"),
                              muTauJJEta = makeMuTauPair(src,"etaJJ","etaJJ"),
                              muTauJJPhi = makeMuTauPair(src,"phiJJ","phiJJ"),
                              muTauJJEnergy = makeMuTauPair(src,"energyJJ","energyJJ"),
                              muTauVBFDEta = makeMuTauPair(src,"vbfDEta","vbfDEta"),
                              muTauVBFDPhi = makeMuTauPair(src,"vbfDPhi","vbfDPhi"),
                              muTauVBFMass = makeMuTauPair(src,"vbfMass","vbfMass"),#vbfMass
                              muTauVBFJets20 = makeMuTauPair(src,"njetigap20","vbfNJetsGap20"),
                              muTauVBFJets30 = makeMuTauPair(src,"njetingap","vbfNJetsGap30"),

                              #Muon IDs and Isolation
                              muTauRelPFIsoDB03 = makeMuTauPair(src,"iso_1",'leg1.userFloat("dBRelIso03")'),
                              muTauRelPFIsoDB04 = makeMuTauPair(src,"iso04_1",'leg1.userFloat("dBRelIso")'),
                              muTausumCharged04 = makeMuTauPair(src,"sumChargedHadronPt04_1",'leg1.pfIsolationR04().sumChargedHadronPt'),
                              muTausumNeutral04 = makeMuTauPair(src,"sumNeutralHadronPt04_1",'leg1.pfIsolationR04().sumNeutralHadronEt'),
                              muTausumPhoton04 = makeMuTauPair(src,"sumPhotonPt04_1",'leg1.pfIsolationR04().sumPhotonEt'),
                              muTausumPU04 = makeMuTauPair(src,"sumPUPt04_1",'leg1.pfIsolationR04().sumPUPt'),

                              muTausumCharged03 = makeMuTauPair(src,"sumChargedHadronPt03_1",'leg1.pfIsolationR03().sumChargedHadronPt'),
                              muTausumNeutral03 = makeMuTauPair(src,"sumNeutralHadronPt03_1",'leg1.pfIsolationR03().sumNeutralHadronEt'),
                              muTausumPhoton03 = makeMuTauPair(src,"sumPhotonPt03_1",'leg1.pfIsolationR03().sumPhotonEt'),
                              muTausumPU03 = makeMuTauPair(src,"sumPUPt03_1",'leg1.pfIsolationR03().sumPUPt'),

                              muTauLooseID = makeMuTauPair(src,"id_m_loose_1",'leg1.isLooseMuon()'),
                              #muTauMediumID = makeMuTauPair(src,"id_m_medium_1",'leg1.isMediumMuon()'),
                              muTauTightID = makeMuTauPair(src,"id_m_tight_1",'leg1.userInt("tightID")'),
                              muTauUserMediumID = makeMuTauPair(src,"id_m_medium_1",'leg1.userInt("mediumID")'),
                              muTauDecayMode = makeMuTauPair(src,"tauDecayMode",'leg2.decayMode()'),
                              muTauDecayFound = makeMuTauPair(src,"decayModeFinding_2",'leg2.tauID("decayModeFinding")'),
                              muTauDecayFoundOld = makeMuTauPair(src,"decayModeFindingOldDMs_2",'leg2.tauID("decayModeFinding")'),
                              muTauDecayFoundNew = makeMuTauPair(src,"decayModeFindingNewDMs_2",'leg2.tauID("decayModeFindingNewDMs")'),
                              muTauProngs = makeMuTauPair(src,"tauProngs",'leg2.signalChargedHadrCands.size()'),#see Decay Modes
                              muTauMuTriggerMatch = makeMuTauPair(src,"lTrigger",'leg1.userFloat("hltL3crIsoL1sMu22L1f0L2f10QL3f24QL3trkIsoFiltered0p09")'),
                              muTauMuTriggerMatchTau = makeMuTauPair(src,"lt1Trigger",'leg1.userFloat("hltOverlapFilterSingleIsoMu19LooseIsoPFTau20")'),
                              muTauMuTriggerMatchTau1 = makeMuTauPair(src,"lt2Trigger",'leg1.userFloat("hltL3crIsoL1sSingleMu18erIorSingleMu20erL1f0L2f10QL3f19QL3trkIsoFiltered0p09")'),
                              muTauPzeta = makeMuTauPair(src,"pZeta",'pZeta-1.5*pZetaVis'),
                              muTauPZ = makeMuTauPair(src,"pZ",'pZeta'),
                              muTauPZV = makeMuTauPair(src,"pzetavis",'pZetaVis'),
                              muTauTauZIP = makeMuTauPair(src,"tauZIP",'leg2.userFloat("zIP")'),
                              muTauHadMass = makeMuTauPair(src,"m_2",'leg2.mass()'),

                              muTauMuDZ = makeMuTauPair(src,"dZ_1","leg1.userFloat('dZ')"),
                              muTauTauDZ = makeMuTauPair(src,"dZ_2","leg2.userFloat('taudZ')"),
                              muTauMuDXY = makeMuTauPair(src,"d0_1","leg1.userFloat('dXY')"),
                              muTauTauDXY = makeMuTauPair(src,"d0_2","leg2.userFloat('taudXY')"),

                              muTauHaddxy = makeMuTauPair(src,"dxy_2",'leg2.dxy()'),
                              muTauHaddxy_Sig = makeMuTauPair(src,"dxy_Sig_2",'leg2.dxy_Sig()'),

                              muTauHadflightLengthx = makeMuTauPair(src,"flightLengthx_2",'leg2.flightLength().x()'),
                              muTauHadflightLengthy = makeMuTauPair(src,"flightLengthy_2",'leg2.flightLength().y()'),
                              muTauHadflightLengthz = makeMuTauPair(src,"flightLengthz_2",'leg2.flightLength().x()'),
                              muTauHadflightLength = makeMuTauPair(src,"flightLength_2",'sqrt(leg2.flightLength().Mag2)'),
                              muTauHadflightLengthSig = makeMuTauPair(src,"flightLengthSig_2",'leg2.flightLengthSig()'),
                              muTauHadhasSecondaryVertex = makeMuTauPair(src,"hasSecondaryVertex_2",'leg2.hasSecondaryVertex()'),


                              muTautau_pt_weighted_dr_signal = makeMuTauPair(src,"tau_pt_weighted_dr_signal",'leg2.userFloat("tau_pt_weighted_dr_signal")'),
                              muTautau_pt_weighted_deta_strip = makeMuTauPair(src,"tau_pt_weighted_deta_strip",'leg2.userFloat("tau_pt_weighted_deta_strip")'),
                              muTautau_pt_weighted_dphi_strip = makeMuTauPair(src,"tau_pt_weighted_dphi_strip",'leg2.userFloat("tau_pt_weighted_dphi_strip")'),
                              muTautau_pt_weighted_dr_iso = makeMuTauPair(src,"tau_pt_weighted_dr_iso",'leg2.userFloat("tau_pt_weighted_dr_iso")'),
                              muTaun_photons_total = makeMuTauPair(src,"n_photons_total",'leg2.userFloat("n_photons_total")'),
                              #tauIDs
                              muTauByCombIsoDBRaw3 = makeMuTauPair(src,"byCombinedIsolationDeltaBetaCorrRaw3Hits_2",'leg2.tauID("byCombinedIsolationDeltaBetaCorrRaw3Hits")'),
                              muTauByCombIsoLoose = makeMuTauPair(src,"tauIsoLoose",'leg2.tauID("byLooseCombinedIsolationDeltaBetaCorr3Hits")'),
                              muTauByCombIsoMedium = makeMuTauPair(src,"tauIsoMedium",'leg2.tauID("byMediumCombinedIsolationDeltaBetaCorr3Hits")'),
                              muTauByCombIsoTight = makeMuTauPair(src,"tauIsoTight",'leg2.tauID("byTightCombinedIsolationDeltaBetaCorr3Hits")'),
                              muTauByNewDMMVAIso = makeMuTauPair(src,"byIsolationMVArun2v1DBnewDMwLTraw_2",'leg2.tauID("byIsolationMVArun2v1DBnewDMwLTraw")'),
                              muTauByOldDMMVAIso = makeMuTauPair(src,"byIsolationMVArun2v1DBoldDMwLTraw_2",'leg2.tauID("byIsolationMVArun2v1DBoldDMwLTraw")'),
                              muTauByOldDMMVAIsoTight = makeMuTauPair(src,"byTightIsolationMVArun2v1DBoldDMwLT_2",'leg2.tauID("byTightIsolationMVArun2v1DBoldDMwLT")'),
                              muTaubyTightIsolationMVArun2v1DBdR03oldDMwLT = makeMuTauPair(src,"byTightIsolationMVArun2v1DBdR03oldDMwLT_2",'leg2.tauID("byTightIsolationMVArun2v1DBdR03oldDMwLT")'),
                              muTaubyTightIsolationMVArun2v1PWdR03oldDMwLT = makeMuTauPair(src,"byTightIsolationMVArun2v1PWdR03oldDMwLT_2",'leg2.tauID("byTightIsolationMVArun2v1PWdR03oldDMwLT")'),
                              muTaubyTightIsolationMVArun2v1PWoldDMwLT = makeMuTauPair(src,"byTightIsolationMVArun2v1PWoldDMwLT_2",'leg2.tauID("byTightIsolationMVArun2v1PWoldDMwLT")'),
                              muTauByOldDMMVAIsoMedium = makeMuTauPair(src,"byMediumIsolationMVArun2v1DBoldDMwLT_2",'leg2.tauID("byMediumIsolationMVArun2v1DBoldDMwLT")'),
                              muTauByOldDMMVAIsoLoose = makeMuTauPair(src,"byLooseIsolationMVArun2v1DBoldDMwLT_2",'leg2.tauID("byLooseIsolationMVArun2v1DBoldDMwLT")'),

                              muTaubyLooseIsolationMVArun2v1DBdR03oldDMwLT = makeMuTauPair(src,"byLooseIsolationMVArun2v1DBdR03oldDMwLT_2",'leg2.tauID("byLooseIsolationMVArun2v1DBdR03oldDMwLT")'),
                              muTaubyMediumIsolationMVArun2v1DBdR03oldDMwLT = makeMuTauPair(src,"byMediumIsolationMVArun2v1DBdR03oldDMwLT_2",'leg2.tauID("byMediumIsolationMVArun2v1DBdR03oldDMwLT")'),
                              muTaubyVTightIsolationMVArun2v1DBdR03oldDMwLT = makeMuTauPair(src,"byVTightIsolationMVArun2v1DBdR03oldDMwLT_2",'leg2.tauID("byVTightIsolationMVArun2v1DBdR03oldDMwLT")'),

                              muTauByCharged = makeMuTauPair(src,"chargedIsoPtSum_2",'leg2.tauID("chargedIsoPtSum")'),
                              muTauByNeutral = makeMuTauPair(src,"neutralIsoPtSum_2",'leg2.tauID("neutralIsoPtSum")'),
                              muTauByPU = makeMuTauPair(src,"puCorrPtSum_2",'leg2.tauID("puCorrPtSum")'), 
                              muTauAgainstMuonTight3 = makeMuTauPair(src,"againstMuonTight3_2",'leg2.tauID("againstMuonTight3")'),
                              #muTauAgainstMuonTight4 = makeMuTauPair(src,"againstMuonTight4_2",'leg2.tauID("againstMuonTight4")'),
                              muTauAgainstEleVLooseMVA6 = makeMuTauPair(src,"againstElectronVLooseMVA6_2",'leg2.tauID("againstElectronVLooseMVA6")'),
                              muTauagainstElectronMVA6Raw = makeMuTauPair(src,"againstElectronMVA6Raw_2",'leg2.tauID("againstElectronMVA6Raw")'),
                              muTauagainstElectronMVA6category = makeMuTauPair(src,"againstElectronMVA6category_2",'leg2.tauID("againstElectronMVA6category")'),
                              muTauagainstElectronMediumMVA6 = makeMuTauPair(src,"againstElectronMediumMVA6_2",'leg2.tauID("againstElectronMediumMVA6")'),
                              muTauagainstElectronTightMVA6 = makeMuTauPair(src,"againstElectronTightMVA6_2",'leg2.tauID("againstElectronTightMVA6")'),
                              muTauagainstElectronVLooseMVA6 = makeMuTauPair(src,"againstElectronVLooseMVA6_2",'leg2.tauID("againstElectronVLooseMVA6")'),
                              muTauagainstElectronVTightMVA6 = makeMuTauPair(src,"againstElectronVTightMVA6_2",'leg2.tauID("againstElectronVTightMVA6")'),
                              muTaubyIsolationMVArun2v1DBdR03oldDMwLTraw = makeMuTauPair(src,"byIsolationMVArun2v1DBdR03oldDMwLTraw_2",'leg2.tauID("byIsolationMVArun2v1DBdR03oldDMwLTraw")'),
                              muTaubyPhotonPtSumOutsideSignalCone = makeMuTauPair(src,"byPhotonPtSumOutsideSignalCone_2",'leg2.tauID("byPhotonPtSumOutsideSignalCone")'),
                              muTauchargedIsoPtSumdR03 = makeMuTauPair(src,"chargedIsoPtSumdR03_2",'leg2.tauID("chargedIsoPtSumdR03")'),
                              muTauneutralIsoPtSumWeight = makeMuTauPair(src,"neutralIsoPtSumWeight_2",'leg2.tauID("neutralIsoPtSumWeight")'),
                              muTauneutralIsoPtSumWeightdR03 = makeMuTauPair(src,"neutralIsoPtSumWeightdR03_2",'leg2.tauID("neutralIsoPtSumWeightdR03")'),
                              muTauneutralIsoPtSumdR03 = makeMuTauPair(src,"neutralIsoPtSumdR03_2",'leg2.tauID("neutralIsoPtSumdR03")'),
                              muTauphotonPtSumOutsideSignalCone = makeMuTauPair(src,"photonPtSumOutsideSignalCone_2",'leg2.tauID("photonPtSumOutsideSignalCone")'),
                              muTauphotonPtSumOutsideSignalConedR03 = makeMuTauPair(src,"photonPtSumOutsideSignalConedR03_2",'leg2.tauID("photonPtSumOutsideSignalConedR03")'),
                              muTaufootprintCorrection = makeMuTauPair(src,"footprintCorrection_2",'leg2.tauID("footprintCorrection")'),
                              muTaufootprintCorrectiondR03 = makeMuTauPair(src,"footprintCorrectiondR03_2",'leg2.tauID("footprintCorrectiondR03")'),

                              muTauGenPt1 = makeMuTauPair(src,"genPt1",'p4Leg1gen().pt()'),
                              muTauGenPt2 = makeMuTauPair(src,"genPt2",'p4Leg2gen().pt()'),
                              muTauPdg1 = makeMuTauPair(src,"pdg1",'genPdg1()'),
                              muTauPdg2 = makeMuTauPair(src,"pdg2",'genPdg2()'),
                              muTauVisGenPt1 = makeMuTauPair(src,"genVisPt1",'p4VisLeg1gen().pt()'),
                              muTauVisGenPt2 = makeMuTauPair(src,"genVisPt2",'p4VisLeg2gen().pt()'),
                              muTauGenVisMass = makeMuTauPair(src,"genVisMass",'p4VisGen().M()'),
                              muTauGenMassMatched = makeMuTauPair(src,"genFullMassMatched",'p4gen().M()'),
                              muTauGenMass = makeMuTauPair(src,"fullGenMass",'genBosonMass()'),
                              muTauGenBosonPt = makeMuTauPair(src,"genpT",'p4GenBoson().pt()'),
                              muTauGenBosonMass = makeMuTauPair(src,"genMass",'p4GenBoson().M()'),
                              muTauGenBosonPx = makeMuTauPair(src,"genpX",'p4GenBoson().px()'),
                              muTauGenBosonPy = makeMuTauPair(src,"genpY",'p4GenBoson().py()'),
                              muTauGenBosonVisPx = makeMuTauPair(src,"vispX",'p4GenBosonVis().px()'),
                              muTauGenBosonVisPy = makeMuTauPair(src,"vispY",'p4GenBosonVis().py()'),

                              muTauGenIsPrompt1 = makeMuTauPair(src,"isPrompt1",'isPrompt1()'),
                              muTauGenIsPromptFS1 = makeMuTauPair(src,"isPromptFS1",'isPromptFS1()'),
                              muTauGenIsDirectTauDecay1 = makeMuTauPair(src,"isTauDecay1",'isDirectPromptTauDecayProduct1()'),
                              muTauGenIsDirectTauDecayFS1 = makeMuTauPair(src,"isTauDecayFS1",'isDirectPromptTauDecayProductFS1()'),

                              muTauGenIsPrompt2 = makeMuTauPair(src,"isPrompt2",'isPrompt2()'),
                              muTauGenIsPromptFS2 = makeMuTauPair(src,"isPromptFS2",'isPromptFS2()'),
                              muTauGenIsDirectTauDecay2 = makeMuTauPair(src,"isTauDecay2",'isDirectPromptTauDecayProduct2()'),
                              muTauGenIsDirectTauDecayFS2 = makeMuTauPair(src,"isTauDecayFS2",'isDirectPromptTauDecayProductFS2()'),

                              #Jets
                              muTauJetsPt20nbtag = makeMuTauJetCountPair(src,"nbtag",'userFloat("isbtagged")&&pt()>20&&abs(eta)<2.4&&userFloat("idLoose")&&bDiscriminator("pfCombinedInclusiveSecondaryVertexV2BJetTags")>.8484'),
                              muTauJetsPt20nbtagLoose = makeMuTauJetCountPair(src,"nbtagLooseNoSF",'pt()>20&&abs(eta)<2.4&&userFloat("idLoose")&&bDiscriminator("pfCombinedInclusiveSecondaryVertexV2BJetTags")>0.5426'),
                              muTauJetsPt20nbtagNoSF = makeMuTauJetCountPair(src,"nbtagNoSF",'pt()>20&&abs(eta)<2.4&&userFloat("idLoose")&&bDiscriminator("pfCombinedInclusiveSecondaryVertexV2BJetTags")>.8484'),
                              muTauJetsPt30nbtagNoSf = makeMuTauJetCountPair(src,"nbtag30",'userFloat("isbtagged")&&pt()>30&&abs(eta)<2.4&&userFloat("idLoose")&&bDiscriminator("pfCombinedInclusiveSecondaryVertexV2BJetTags")>.8484'),
                              muTauJetsPt30nbtag = makeMuTauJetCountPair(src,"nbtag30",'pt()>30&&abs(eta)<2.4&&userFloat("idLoose")&&bDiscriminator("pfCombinedInclusiveSecondaryVertexV2BJetTags")>.8484'),

                              muTauJetsPt30njets = makeMuTauJetCountPair(src,"njets",'pt()>30&&abs(eta)<4.7&&userFloat("idLoose")'),
                              muTauJetsPt30njetsnopu = makeMuTauJetCountPair(src,"njetspuID",'pt()>30&&abs(eta)<4.7&&userFloat("idLoose")&&!userFloat("puIDLoose")'),
                              muTauJetsPt20njets = makeMuTauJetCountPair(src,"njetspt20",'pt()>20&&abs(eta)<4.7&&userFloat("idLoose")'),
                              muTauJetsPt20njetsnopu = makeMuTauJetCountPair(src,"njetspt20puID",'pt()>20&&abs(eta)<4.7&&userFloat("idLoose")&&!userFloat("puIDLoose")'),


                              muTauJet1PtPtSort = makeMuTauPtPair(src,"jpt_1",'abs(eta())<4.7&&pt()>20&&userFloat("idLoose")','pt()',0),
                              muTauJet2PtPtSort = makeMuTauPtPair(src,"jpt_2",'abs(eta())<4.7&&pt()>20&&userFloat("idLoose")','pt()',1),
                              muTauJet1PFIDPtSort = makeMuTauPtPair(src,"jpfid_1",'abs(eta())<4.7&&pt()>20&&userFloat("idLoose")','userFloat("idLoose")',0),
                              muTauJet2PFIDPtSort = makeMuTauPtPair(src,"jpfid_2",'abs(eta())<4.7&&pt()>20&&userFloat("idLoose")','userFloat("idLoose")',1),
                              muTauJet1PUIDPtSort = makeMuTauPtPair(src,"jpuid_1",'abs(eta())<4.7&&pt()>20&&userFloat("idLoose")','userFloat("puID")',0),
                              muTauJet2PUIDPtSort = makeMuTauPtPair(src,"jpuid_2",'abs(eta())<4.7&&pt()>20&&userFloat("idLoose")','userFloat("puID")',1),
                              muTauJet1MVAPtSort = makeMuTauPtPair(src,"jmva_1",'abs(eta())<4.7&&pt()>20&&userFloat("idLoose")',"userFloat('pileupJetId:fullDiscriminant')",0),
                              muTauJet2MVAPtSort = makeMuTauPtPair(src,"jmva_2",'abs(eta())<4.7&&pt()>20&&userFloat("idLoose")',"userFloat('pileupJetId:fullDiscriminant')",1),
                              muTauJet1EtaPtSort = makeMuTauPtPair(src,"jeta_1",'abs(eta())<4.7&&pt()>20&&userFloat("idLoose")','eta()',0),
                              muTauJet2EtaPtSort = makeMuTauPtPair(src,"jeta_2",'abs(eta())<4.7&&pt()>20&&userFloat("idLoose")','eta()',1),
                              muTauJet1PhiPtSort = makeMuTauPtPair(src,"jphi_1",'abs(eta())<4.7&&pt()>20&&userFloat("idLoose")','phi()',0),
                              muTauJet2PhiPtSort = makeMuTauPtPair(src,"jphi_2",'abs(eta())<4.7&&pt()>20&&userFloat("idLoose")','phi()',1),
                              muTauJet1CSVPtSort = makeMuTauPtPair(src,"jcsv_1",'abs(eta())<2.4&&pt()>20&&userFloat("idLoose")','bDiscriminator("pfCombinedInclusiveSecondaryVertexV2BJetTags")',0),
                              muTauJet2CSVPtSort = makeMuTauPtPair(src,"jcsv_2",'abs(eta())<2.4&&pt()>20&&userFloat("idLoose")','bDiscriminator("pfCombinedInclusiveSecondaryVertexV2BJetTags")',1),
                              muTauJet1MedIdPtSort = makeMuTauPtPair(src,"jtlvID_1",'','userFloat("idTightLepVeto")',0),
                              muTauJet2MedIdPtSort = makeMuTauPtPair(src,"jtlvID_2",'','userFloat("idTightLepVeto")',1),
                              muTauJet1TightIdPtSort = makeMuTauPtPair(src,"jtightID_1",'','userFloat("idTight")',0),
                              muTauJet2TightIdPtSort = makeMuTauPtPair(src,"jtightID_2",'','userFloat("idTight")',1),

                              muTauBJet1PtPtSort = makeMuTauPtPair(src,"bpt_1",'abs(eta())<2.4&&pt()>20&&userFloat("idLoose")&&bDiscriminator("pfCombinedInclusiveSecondaryVertexV2BJetTags")>0.8484','pt()',0),
                              muTauBJet2PtPtSort = makeMuTauPtPair(src,"bpt_2",'abs(eta())<2.4&&pt()>20&&userFloat("idLoose")&&bDiscriminator("pfCombinedInclusiveSecondaryVertexV2BJetTags")>0.8484','pt()',1),
                              muTauBJet1MVAPtSort = makeMuTauPtPair(src,"bmva_1",'abs(eta())<2.4&&pt()>20&&userFloat("idLoose")&&bDiscriminator("pfCombinedInclusiveSecondaryVertexV2BJetTags")>0.8484',"userFloat('pileupJetId:fullDiscriminant')",0),
                              muTauBJet2MVAPtSort = makeMuTauPtPair(src,"bmva_2",'abs(eta())<2.4&&pt()>20&&userFloat("idLoose")&&bDiscriminator("pfCombinedInclusiveSecondaryVertexV2BJetTags")>0.8484',"userFloat('pileupJetId:fullDiscriminant')",1),
                              muTauBJet1PFIDPtSort = makeMuTauPtPair(src,"bpfid_1",'abs(eta())<2.4&&pt()>20&&userFloat("idLoose")&&bDiscriminator("pfCombinedInclusiveSecondaryVertexV2BJetTags")>0.8484','userFloat("idLoose")',0),
                              muTauBJet2PFIDPtSort = makeMuTauPtPair(src,"bpfid_2",'abs(eta())<2.4&&pt()>20&&userFloat("idLoose")&&bDiscriminator("pfCombinedInclusiveSecondaryVertexV2BJetTags")>0.8484','userFloat("idLoose")',1),
                              muTauBJet1PUIDPtSort = makeMuTauPtPair(src,"bpuid_1",'abs(eta())<2.4&&pt()>20&&userFloat("idLoose")&&bDiscriminator("pfCombinedInclusiveSecondaryVertexV2BJetTags")>0.8484','userFloat("puID")',0),
                              muTauBJet2PUIDPtSort = makeMuTauPtPair(src,"bpuid_2",'abs(eta())<2.4&&pt()>20&&userFloat("idLoose")&&bDiscriminator("pfCombinedInclusiveSecondaryVertexV2BJetTags")>0.8484','userFloat("puID")',1),
                              muTauBJet1EtaPtSort = makeMuTauPtPair(src,"beta_1",'abs(eta())<2.4&&pt>20&&userFloat("idLoose")&&bDiscriminator("pfCombinedInclusiveSecondaryVertexV2BJetTags")>0.8484','eta()',0),
                              muTauBJet2EtaPtSort = makeMuTauPtPair(src,"beta_2",'abs(eta())<2.4&&pt>20&&userFloat("idLoose")&&bDiscriminator("pfCombinedInclusiveSecondaryVertexV2BJetTags")>0.8484','eta()',1),
                              muTauBJet1PhiPtSort = makeMuTauPtPair(src,"bphi_1",'abs(eta())<2.4&&pt>20&&userFloat("idLoose")&&bDiscriminator("pfCombinedInclusiveSecondaryVertexV2BJetTags")>0.8484','phi()',0),
                              muTauBJet2PhiPtSort = makeMuTauPtPair(src,"bphi_2",'abs(eta())<2.4&&pt>20&&userFloat("idLoose")&&bDiscriminator("pfCombinedInclusiveSecondaryVertexV2BJetTags")>0.8484','phi()',1),
                              muTauBJet1CSVPtSort = makeMuTauPtPair(src,"bcsv_1",'abs(eta())<2.4&&pt()>20&&userFloat("idLoose")&&bDiscriminator("pfCombinedInclusiveSecondaryVertexV2BJetTags")>.8484','bDiscriminator("pfCombinedInclusiveSecondaryVertexV2BJetTags")',0),
                              muTauBJet2CSVPtSort = makeMuTauPtPair(src,"bcsv_2",'abs(eta())<2.4&&pt()>20&&userFloat("idLoose")&&bDiscriminator("pfCombinedInclusiveSecondaryVertexV2BJetTags")>.8484','bDiscriminator("pfCombinedInclusiveSecondaryVertexV2BJetTags")',1),

                              muTauJetsPt20TagMatch = makeMuTauJetCountPair(src,"nTaggableJetsPt20Matched",'pt()>20&&abs(eta)<2.4&&abs(partonFlavour)==5'),
                              muTauJetsPt20TagNoMatch = makeMuTauJetCountPair(src,"nTaggableJetsPt20NotMatched",'pt()>30&&abs(eta)<2.4&&abs(partonFlavour)!=5'),
                              muTauFirstJetShape = makeLTauGeneric("PATMuTauPairHighestPtJetVarFiller",src,"highestJetShape",'userFloat("ptRMS")'),
                              muTauFirstJetCSV = makeLTauGeneric("PATMuTauPairHighestPtJetVarFiller",src,"highestJetBTagCSV",'bDiscriminator("pfCombinedInclusiveSecondaryVertexV2BJetTags")'),

                              mumuDR = makeLTauGeneric("PATMuPairFiller",srcLL,"diLeptonDR","dR12"),#FIXME

                              higgsPt = cms.PSet(
                                  pluginType = cms.string("PATGenParticleFiller"),
                                  src        = cms.InputTag("genDaughters"),
                                  tag        = cms.string("higgsPt"),
                                  method     = cms.string('pt()'),
                                  leadingOnly=cms.untracked.bool(True)
                              ),#FILLED in higgs sample

                              #muTauLHEProduct = cms.PSet(
                              #    pluginType = cms.string("LHEProductFiller"),
                              #    src        = cms.InputTag("source"),
                              #    tag        = cms.string("LHEProduct"),
                              #),
                              muTauLHEProduct2 = cms.PSet(
                                  pluginType = cms.string("LHEProductFiller"),
                                  src        = cms.InputTag("externalLHEProducer"),
                                  tag        = cms.string("LHEProduct"),
                              ),
                              muTauEmbedPtWeight = cms.PSet(
                                  pluginType = cms.string("GenFilterInfoWeightFiller"),
                                  src        = cms.InputTag("generator"),
                                  #src        = cms.InputTag("generator","EmbWeight"),
                                  tag        = cms.string("aMCNLO_weight"),
                              ),#FIXME #CHECKME
                              muTauEmbedPt = cms.PSet(
                                  pluginType = cms.string("PATGenParticleFiller"),
                                  src        = cms.InputTag("genDaughters"),
                                  tag        = cms.string("embeddedPt"),#CHECKME
                                  method     = cms.string("pt"),
                                  leadingOnly=cms.untracked.bool(False)
                              ),#FIXME #CHECKME
                              muTauEmbedEta = cms.PSet(
                                  pluginType = cms.string("PATGenParticleFiller"),
                                  src        = cms.InputTag("genDaughters"),
                                  tag        = cms.string("embeddedEta"),
                                  method     = cms.string("eta"),
                                  leadingOnly=cms.untracked.bool(False)
                              )#FIXME #CHECKME

   )

   setattr(process, name, eventTree)
   p = cms.Path(getattr(process,name))
   setattr(process, name+'Path', p)


############################Di-Tau#####################

def addDiTauEventTree(process,name,src = 'diTausSorted', srcU='TightMuons', srcE='TightElectrons', srcTT='diNonBoostTausOSSorted'):
   process.TFileService = cms.Service("TFileService", fileName = cms.string("analysis.root") )
   eventTree = cms.EDAnalyzer('EventTreeMaker',
                              genEvent = cms.InputTag('generator'),
                              coreCollections = cms.InputTag(src),
                              trigger = cms.PSet(
                                  pluginType = cms.string("TriggerFiller"),
                                  src = cms.InputTag(TriggerRes,"",TriggerProcess),
                                  prescales = cms.InputTag("patTrigger"),
                                  paths      = cms.vstring(TriggerPaths)
                                  ),
                              metfilter = cms.PSet(
                                  pluginType = cms.string("TriggerFilterFiller"),
                                  src = cms.InputTag(TriggerRes,"",TriggerFilter),
                                  BadChargedCandidateFilter = cms.InputTag("BadChargedCandidateFilter"),
                                  BadPFMuonFilter           = cms.InputTag("BadPFMuonFilter"),
                                  paths      = cms.vstring(
                                      "Flag_HBHENoiseFilter",
                                      "Flag_HBHENoiseIsoFilter", 
                                      "Flag_globalTightHalo2016Filter",
                                      "Flag_goodVertices",
                                      "Flag_eeBadScFilter",
                                      "Flag_EcalDeadCellTriggerPrimitiveFilter"
                                      )
                                  ),


                              pu = cms.PSet(
                                  pluginType = cms.string("PUFiller"),
                                  src        = cms.InputTag("slimmedAddPileupInfo"),
                                  tag        = cms.string("pu")
                              ),
                              cov = cms.PSet(
                                  pluginType = cms.string("METSignificanceFiller"),
                                  src        = cms.InputTag("METSignificance"),
                                  tag        = cms.string("metcov")
                              ),
                              PVsSync = cms.PSet(
                                  pluginType = cms.string("VertexSizeFiller"),
                                  src        = cms.InputTag("offlineSlimmedPrimaryVertices"),
                                  tag        = cms.string("npv")
                              ),#FILLED
                              PVs = cms.PSet(
                                  pluginType = cms.string("VertexSizeFiller"),
                                  src        = cms.InputTag("offlineSlimmedPrimaryVertices"),
                                  tag        = cms.string("vertices")
                              ),#FILLED
 
                              diTauSize = makeCollSize(src,"nCands"),#FILLED
                              diTauOS = makeCollSizeOS(src,0,"os"),#FILLED
                              genTaus = makeCollSize("genTauCands","genTaus"), 

                              tausSizeTT = makeCollSize(srcTT,"diNonBoostTausOSSorted"),#FILLED
                              muonsSizeMT = makeCollSize(srcU,"tightMuons"),#FILLED
                              muonsSizeMTVeto = makeCollSizeVeto(srcU,1,"extramuon_veto"),#FILLED
                              electronsSizeMT = makeCollSize(srcE,"tightElectrons"),#FILLED
                              electronsSizeMTVeto = makeCollSizeVeto(srcE,0,"extraelec_veto"),#FILLED

                              diTauDR = makeDiTauPair(src,"dR","dR12"), 
                              tauSingleL1 =  makeDiTauPair(src,"tauSingleL1_2","leg2.userFloat('LooseIsoPFTau20_SingleL1')"), 
                              tauL1 =  makeDiTauPair(src,"tauL1_2","leg2.userFloat('LooseIsoPFTau20')"), 
                              tauMediumL1 =  makeDiTauPair(src,"tauMediumL1_2","leg2.userFloat('MediumIsoPFTau35_Trk_eta2p1')"),

                              tauNIsoTracks1 =  makeDiTauPair(src,"tauNIsoTracks","leg2.userFloat('nIsoTracks')"), #FILLED
                              diTaunIsoGamma1 = makeDiTauPair(src,"nIsoGamma",'leg2.userFloat("nIsoGamma")'),
                              diTaunIsoNeutral1 = makeDiTauPair(src,"nIsoNeutral",'leg2.userFloat("nIsoNeutral")'),
                              tauNIsoTracks2 =  makeDiTauPair(src,"tauNIsoTracks","leg2.userFloat('nIsoTracks')"), #FILLED
                              diTaunIsoGamma2 = makeDiTauPair(src,"nIsoGamma",'leg2.userFloat("nIsoGamma")'),
                              diTaunIsoNeutral2 = makeDiTauPair(src,"nIsoNeutral",'leg2.userFloat("nIsoNeutral")'),


                              tauLeadChargedHadrTrackPt1 = makeDiTauPair(src,"tauLeadChargedHadrTrackPt_1","leg1.userFloat('leadChargedHadrTrackPt')"),#FILLED
                              tauLeadChargedHadrTrackPt2 = makeDiTauPair(src,"tauLeadChargedHadrTrackPt_2","leg2.userFloat('leadChargedHadrTrackPt')"),#FILLED

                              diTauCharge = makeDiTauPair(src,"charge","charge"),#FILLED
                              q_1 = makeDiTauPair(src,"q_1","leg1.charge"),#FILLED
                              q_2 = makeDiTauPair(src,"q_2","leg2.charge"),#FILLED

                              diTauPt = makeDiTauPair(src,"pth","pt"),#FILLED
                              diTauHT = makeDiTauPair(src,"ht","ht"),#FILLED
                              diTauMass = makeDiTauPair(src,"m_vis","mass"),#FILLED
                              diTaulVeto = makeDiTauPair(src,"lVeto","lVeto"),

                              diTauPt1 =  makeDiTauPair(src,"pt_1","leg1.pt"), #FILLED
                              diTauPt2 =  makeDiTauPair(src,"pt_2","leg2.pt"), #FILLED
                              diTauEta1 = makeDiTauPair(src,"eta_1","leg1.eta"),#FILLED
                              diTauEta2 = makeDiTauPair(src,"eta_2","leg2.eta"),#FILLED
                              diTauPhi1 = makeDiTauPair(src,"phi_1","leg1.phi"),#FILLED
                              diTauPhi2 = makeDiTauPair(src,"phi_2","leg2.phi"),#FILLED

                              diTauMET1 = makeDiTauMET(src,"slimmedMETs","pf"),#FILLED
                              diTauMET2 = makeDiTauMET(src,"slimmedMETsPuppi","puppi"),#FILLED
                              diTauMETUncertUp = makeDiTauMETUncert(src,"slimmedMETs","pf","EnUp"),#FILLED
                              diTauMETUncertDown = makeDiTauMETUncert(src,"slimmedMETs","pf","EnDown"),#FILLED
 
                              diTauMET = makeDiTauPair(src,"met","met.pt()"),#FILLED
                              diTauMETPhi = makeDiTauPair(src,"metphi","met.phi()"),#FILLED

                              diTauMT = makeDiTauPair(src,"mt12","mt12MET"),#FILLED
                              diTauMT1 = makeDiTauPair(src,"mt_1","mt1MET"),#FILLED
                              diTauMT2 = makeDiTauPair(src,"mt_2","mt2MET"),#FILLED
                              
                              diTauTopGenPt = makeDiTauPair(src,"topGenPt","topGenPt"),#FIXME
                              diTauAntiTopGenPt = makeDiTauPair(src,"antiTopGenPt","antiTopGenPt"),#FIXME

                              #BTAGS AND JETS
                              diTauMJJ = makeDiTauPair(src,"mJJ","mJJ"),#FILLED
                              diTauJJPt = makeDiTauPair(src,"ptJJ","ptJJ"),
                              diTauJJEta = makeDiTauPair(src,"etaJJ","etaJJ"),
                              diTauJJPhi = makeDiTauPair(src,"phiJJ","phiJJ"),
                              diTauJJEnergy = makeDiTauPair(src,"energyJJ","energyJJ"),
                              diTauVBFDEta = makeDiTauPair(src,"vbfDEta","vbfDEta"),
                              diTauVBFDPhi = makeDiTauPair(src,"vbfDPhi","vbfDPhi"),
                              diTauVBFMass = makeDiTauPair(src,"vbfMass","vbfMass"),#vbfMass
                              diTauVBFJets20 = makeDiTauPair(src,"njetigap20","vbfNJetsGap20"),
                              diTauVBFJets30 = makeDiTauPair(src,"njetingap","vbfNJetsGap30"),
                              diTauDM1 = makeDiTauPair(src, "decayMode_1",'leg1.decayMode()'),
                              diTauDM2 = makeDiTauPair(src, "decayMode_2",'leg2.decayMode()'),
                              diTauIsoLooseMVA31 = makeDiTauPair(src, "byLooseIsolationMVArun2v1DBdR03oldDMwLT_1",'leg1.tauID("byLooseIsolationMVArun2v1DBdR03oldDMwLT")'),
                              diTauIsoLooseMVA32 = makeDiTauPair(src, "byLooseIsolationMVArun2v1DBdR03oldDMwLT_2",'leg2.tauID("byLooseIsolationMVArun2v1DBdR03oldDMwLT")'),
                              diTauIsoMediumMVA31 = makeDiTauPair(src, "byMediumIsolationMVArun2v1DBdR03oldDMwLT_1",'leg1.tauID("byMediumIsolationMVArun2v1DBdR03oldDMwLT")'),
                              diTauIsoMediumMVA32 = makeDiTauPair(src, "byMediumIsolationMVArun2v1DBdR03oldDMwLT_2",'leg2.tauID("byMediumIsolationMVArun2v1DBdR03oldDMwLT")'),
                              diTauIsoTightMVA31 = makeDiTauPair(src, "byTightIsolationMVArun2v1DBdR03oldDMwLT_1",'leg1.tauID("byTightIsolationMVArun2v1DBdR03oldDMwLT")'),
                              diTauIsoTightMVA32 = makeDiTauPair(src, "byTightIsolationMVArun2v1DBdR03oldDMwLT_2",'leg2.tauID("byTightIsolationMVArun2v1DBdR03oldDMwLT")'),
                              diTauIsoVTightMVA31 = makeDiTauPair(src, "byVTightIsolationMVArun2v1DBdR03oldDMwLT_1",'leg1.tauID("byVTightIsolationMVArun2v1DBdR03oldDMwLT")'),
                              diTauIsoVTightMVA32 = makeDiTauPair(src, "byVTightIsolationMVArun2v1DBdR03oldDMwLT_2",'leg2.tauID("byVTightIsolationMVArun2v1DBdR03oldDMwLT")'),

                              diTauchargedIsoPtSumdR031 = makeDiTauPair(src, "chargedIsoPtSumdR03_1",'leg1.tauID("chargedIsoPtSumdR03")'),
                              diTauchargedIsoPtSumdR032 = makeDiTauPair(src, "chargedIsoPtSumdR03_2",'leg2.tauID("chargedIsoPtSumdR03")'),
                              diTauagainstMuonLoose31 = makeDiTauPair(src, "againstMuonLoose3_1",'leg1.tauID("againstMuonLoose3")'),
                              diTauagainstMuonLoose32 = makeDiTauPair(src, "againstMuonLoose3_2",'leg2.tauID("againstMuonLoose3")'),
                              diTauagainstMuonTight31 = makeDiTauPair(src, "againstMuonTight3_1",'leg1.tauID("againstMuonTight3")'),
                              diTauagainstMuonTight32 = makeDiTauPair(src, "againstMuonTight3_2",'leg2.tauID("againstMuonTight3")'),
                              diTauagainstElectronVLooseMVA61 = makeDiTauPair(src, "againstElectronVLooseMVA6_1",'leg1.tauID("againstElectronVLooseMVA6")'),
                              diTauagainstElectronVLooseMVA62 = makeDiTauPair(src, "againstElectronVLooseMVA6_2",'leg2.tauID("againstElectronVLooseMVA6")'),

                              diTauDecayFound = makeDiTauPair(src,"decayModeFinding_2",'leg2.tauID("decayModeFinding")'),
                              diTauDecayFoundNew = makeDiTauPair(src,"decayModeFindingNewDMs_2",'leg2.tauID("decayModeFindingNewDMs")'),
                              diTauProngs = makeDiTauPair(src,"tauProngs",'leg2.signalChargedHadrCands.size()'),#see Decay Modes
                              diTauPzeta = makeDiTauPair(src,"pZeta",'pZeta-1.5*pZetaVis'),
                              diTauPZ = makeDiTauPair(src,"pZ",'pZeta'),
                              diTauPZV = makeDiTauPair(src,"pzetavis",'pZetaVis'),
                              diTauHadMass = makeDiTauPair(src,"m_2",'leg2.mass()'),

                              diTauMuDZ = makeDiTauPair(src,"dZ_1","leg1.userFloat('taudZ')"),
                              diTauTauDZ = makeDiTauPair(src,"dZ_2","leg2.userFloat('taudZ')"),
                              diTauMuDXY = makeDiTauPair(src,"d0_1","leg1.userFloat('taudXY')"),
                              diTauTauDXY = makeDiTauPair(src,"d0_2","leg2.userFloat('taudXY')"),
                              diTauGenPt1 = makeDiTauPair(src,"genPt1",'p4Leg1gen().pt()'),
                              diTauGenPt2 = makeDiTauPair(src,"genPt2",'p4Leg2gen().pt()'),
                              diTauPdg1 = makeDiTauPair(src,"pdg1",'genPdg1()'),
                              diTauPdg2 = makeDiTauPair(src,"pdg2",'genPdg2()'),
                              diTauVisGenPt1 = makeDiTauPair(src,"genVisPt1",'p4VisLeg1gen().pt()'),
                              diTauVisGenPt2 = makeDiTauPair(src,"genVisPt2",'p4VisLeg2gen().pt()'),
                              diTauGenVisMass = makeDiTauPair(src,"genVisMass",'p4VisGen().M()'),
                              diTauGenMassMatched = makeDiTauPair(src,"genFullMassMatched",'p4gen().M()'),
                              diTauGenMass = makeDiTauPair(src,"fullGenMass",'genBosonMass()'),
                              diTauGenBosonPt = makeDiTauPair(src,"genpT",'p4GenBoson().pt()'),
                              diTauGenBosonMass = makeDiTauPair(src,"genMass",'p4GenBoson().M()'),
                              diTauGenBosonPx = makeDiTauPair(src,"genpX",'p4GenBoson().px()'),
                              diTauGenBosonPy = makeDiTauPair(src,"genpY",'p4GenBoson().py()'),
                              diTauGenBosonVisPx = makeDiTauPair(src,"vispX",'p4GenBosonVis().px()'),
                              diTauGenBosonVisPy = makeDiTauPair(src,"vispY",'p4GenBosonVis().py()'),

                              diTauGenIsPrompt1 = makeDiTauPair(src,"isPrompt1",'isPrompt1()'),
                              diTauGenIsPromptFS1 = makeDiTauPair(src,"isPromptFS1",'isPromptFS1()'),
                              diTauGenIsDirectTauDecay1 = makeDiTauPair(src,"isTauDecay1",'isDirectPromptTauDecayProduct1()'),
                              diTauGenIsDirectTauDecayFS1 = makeDiTauPair(src,"isTauDecayFS1",'isDirectPromptTauDecayProductFS1()'),
                              diTauGenIsPrompt2 = makeDiTauPair(src,"isPrompt2",'isPrompt2()'),
                              diTauGenIsPromptFS2 = makeDiTauPair(src,"isPromptFS2",'isPromptFS2()'),
                              diTauGenIsDirectTauDecay2 = makeDiTauPair(src,"isTauDecay2",'isDirectPromptTauDecayProduct2()'),
                              diTauGenIsDirectTauDecayFS2 = makeDiTauPair(src,"isTauDecayFS2",'isDirectPromptTauDecayProductFS2()'),

                              #diTauJetsPt20nbtag = makeDiTauJetCountPair(src,"nbtag",'userFloat("isbtagged")&&pt()>20&&abs(eta)<2.4&&userFloat("idLoose")&&bDiscriminator("pfCombinedInclusiveSecondaryVertexV2BJetTags")>0.8484'),
                              diTauJetsPt20nbtagNoSF = makeDiTauJetCountPair(src,"nbtagNoSF",'pt()>20&&abs(eta)<2.4&&userFloat("idLoose")&&bDiscriminator("pfCombinedInclusiveSecondaryVertexV2BJetTags")>.8484'),

                              higgsPt = cms.PSet(
                                  pluginType = cms.string("PATGenParticleFiller"),
                                  src        = cms.InputTag("genDaughters"),
                                  tag        = cms.string("higgsPt"),
                                  method     = cms.string('pt()'),
                                  leadingOnly=cms.untracked.bool(True)
                              ),#FILLED in higgs sample

                              diTauLHEProduct2 = cms.PSet(
                                  pluginType = cms.string("LHEProductFiller"),
                                  src        = cms.InputTag("externalLHEProducer"),
                                  tag        = cms.string("LHEProduct"),
                              ),
                              diTauEmbedPtWeight = cms.PSet(
                                  pluginType = cms.string("GenFilterInfoWeightFiller"),
                                  src        = cms.InputTag("generator"),
                                  #src        = cms.InputTag("generator","EmbWeight"),
                                  tag        = cms.string("aMCNLO_weight"),
                              ),#FIXME #CHECKME
                              diTauEmbedPt = cms.PSet(
                                  pluginType = cms.string("PATGenParticleFiller"),
                                  src        = cms.InputTag("genDaughters"),
                                  tag        = cms.string("embeddedPt"),#CHECKME
                                  method     = cms.string("pt"),
                                  leadingOnly=cms.untracked.bool(False)
                              ),#FIXME #CHECKME
                              diTauEmbedEta = cms.PSet(
                                  pluginType = cms.string("PATGenParticleFiller"),
                                  src        = cms.InputTag("genDaughters"),
                                  tag        = cms.string("embeddedEta"),
                                  method     = cms.string("eta"),
                                  leadingOnly=cms.untracked.bool(False)
                              )#FIXME #CHECKME

   )

   setattr(process, name, eventTree)
   p = cms.Path(getattr(process,name))
   setattr(process, name+'Path', p)

