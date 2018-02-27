#!/bin/sh

#cp -r /nfs_scratch/$USER/monohiggs_unweighted/ /nfs_scratch/$USER/monohiggs_weighted/ 
#cd /nfs_scratch/$USER/monohiggs_weighted1

#cd /nfs_scratch/$USER/monohiggs_Z
cd /nfs_scratch/$USER/monohiggs_wjets


weight=2;
weightTT=2;
weightH=2;
weightW=1;
weightEWK=2;
weightTriBoson=2;
weightBaryonic=2;
weightZN=2;
weightAh=0;

weightZ=2;
weightZPt=2;

weightZinv=3;


#hadd WJETS.root WJets*root 
#rm WZTo3L1Nu_amc.root 
#rm WWTo1L1Nu2Q.root 
#hadd Znunu.root ZJetsNuNu*root 
#hadd smH125.root ggH125.root vbfH125.root ZH125.root WpH125.root WmH125.root ttH.root ggHWW.root vbfHWW.root 

if [ $weightH -eq 1 ]
then
    echo 'weight ggH'
    EventWeightsIterativeGen outputFile='ggH125.root'     weight=3.04597    histoName='MT/results' sumHistoName='sumweights/genWeights' 
    echo 'weight vbf'
    EventWeightsIterativeGen outputFile='vbfH125.root'     weight=0.2371314    histoName='MT/results' sumHistoName='sumweights/genWeights' 
    echo 'weight ZH'
    EventWeightsIterativeGen outputFile='ZH125.root'     weight=0.05542053    histoName='MT/results' sumHistoName='sumweights/genWeights' 

    echo 'weight HWW'
    EventWeightsIterativeGen outputFile='ggHWW.root'     weight=1.09644    histoName='MT/results' sumHistoName='sumweights/genWeights' 
    EventWeightsIterativeGen outputFile='vbfHWW.root'     weight=0.085359    histoName='MT/results' sumHistoName='sumweights/genWeights' 

    echo 'weight WH'
    EventWeightsIterativeGen outputFile='WpH125.root'     weight=0.052    histoName='MT/results' sumHistoName='sumweights/genWeights' 
    EventWeightsIterativeGen outputFile='WmH125.root'     weight=0.0334    histoName='MT/results' sumHistoName='sumweights/genWeights' 

    EventWeightsIterativeGen outputFile='ttH.root'     weight=0.2151    histoName='MT/results' sumHistoName='sumweights/genWeights' 

fi

if [ $weightZN -eq 1 ]
then
    echo 'weight ZN'
    EventWeightsIterativeZNuNu root200=ZJetsNuNu200.root root400=ZJetsNuNu400.root root600=ZJetsNuNu600.root root800=ZJetsNuNu800.root root1200=ZJetsNuNu1200.root root2500=ZJetsNuNu2500.root rootinf=ZJetsNuNuInf.root   weight=1    histoName='MT/results' 
    #hadd Znunu.root ZJetsNuNu*root 
fi

if [ $weightW -eq 1 ]
then
    #hadd WJetsInclu.root WJetsMLM.root WJetsMLM_ext.root 
    #EventWeightsIterativeWJetsHT  weight=1    histoName='MT/results' 
    #hadd WJETSHT.root WJets*root 
    EventWeightsIterativeWJets  weight=1    histoName='MT/results' 

    hadd WJETS.root WJets*root 
fi


if [ $weightZ -eq 1 ]
then
    EventWeightsIterativeZJets    weight=1    histoName='MT/results'  
    hadd ZJETS.root ZJets_ext.root Z1Jets.root Z2Jets.root Z3Jets.root Z4Jets.root 
fi

if [ $weightZPt -eq 1 ]
then
    #make sure Zpt root file is around!!!
    EventWeightsIterativeZPt  outputFile='ZJETS.root'  weight=1    histoName='MT/results' 
    EventWeightsIterativeZPt  outputFile='EWKZ.root'  weight=1    histoName='MT/results' 
    #EventWeightsForEfficiencyIsolation  outputFile='ZJETS.root' 
    #EventWeightsForEfficiencyTracking  outputFile='ZJETS.root' 
fi


if [ $weightTT -eq 1 ]
then
    echo 'Weight TT'
    nohup EventWeightsIterativeTT outputFile='TT.root'  weight=831.76     histoName='MT/results' sumHistoName='sumweights/genWeights' &
    #EventWeightsIterativeTT has top pt reweighting

fi

if [ $weight -eq 1 ]
then

    EventWeightsIterativeGen outputFile='TTZ.root'      weight=0.2529  histoName='MT/results' sumHistoName='sumweights/genWeights'
    EventWeightsIterativeGen outputFile='TTW.root'      weight=0.2043  histoName='MT/results' sumHistoName='sumweights/genWeights'
    EventWeightsIterativeGen outputFile='Wg_LNuG.root'  weight=511.0  histoName='MT/results' sumHistoName='sumweights/genWeights'
    EventWeightsIterativeGen outputFile='Wg_LNuEE.root'  weight=2.793  histoName='MT/results' sumHistoName='sumweights/genWeights'
    EventWeightsIterativeGen outputFile='Wg_LNuMuMu.root'  weight=3.526  histoName='MT/results' sumHistoName='sumweights/genWeights'

    echo 'Weight ZZ'
    EventWeightsIterativeGen outputFile='ZZTo2L2Q.root'      weight=3.22  histoName='MT/results' sumHistoName='sumweights/genWeights'
    EventWeightsIterativeGen outputFile='ZZTo2Q2Nu.root'      weight=4.03  histoName='MT/results' sumHistoName='sumweights/genWeights'
    EventWeightsIterativeGen outputFile='ZZTo4L.root'      weight=1.212  histoName='MT/results' sumHistoName='sumweights/genWeights'
    EventWeightsIterativeGen outputFile='ZZTo2L2Nu.root'     weight=0.564   histoName='MT/results' sumHistoName='sumweights/genWeights'


    echo 'Weight WZ'
    EventWeightsIterativeGen outputFile='WZTo1L1Nu2Q.root'      weight=10.71   histoName='MT/results' sumHistoName='sumweights/genWeights'
    EventWeightsIterativeGen outputFile='WZTo2L2Q.root'      weight=5.595   histoName='MT/results' sumHistoName='sumweights/genWeights'
    EventWeightsIterativeGen outputFile='WZTo1L3Nu.root'      weight=3.05   histoName='MT/results' sumHistoName='sumweights/genWeights'
    #EventWeightsIterativeGen outputFile='WZTo3L1Nu_amc.root'      weight=5.26   histoName='MT/results' sumHistoName='sumweights/genWeights'
    EventWeightsIterativeGen outputFile='WZTo3L1Nu_pow.root'      weight=4.43   histoName='MT/results' sumHistoName='sumweights/genWeights'

    echo 'Weight WW'
    EventWeightsIterativeGen outputFile='WWTo1L1Nu2Q.root'     weight=43.53     histoName='MT/results' sumHistoName='sumweights/genWeights'
    EventWeightsIterativeGen outputFile='WWTo1L1NuQQ.root'     weight=43.53     histoName='MT/results' sumHistoName='sumweights/genWeights'

    EventWeightsIterativeGen outputFile='WWTo2L2Q.root'     weight=10.48    histoName='MT/results' sumHistoName='sumweights/genWeights'
    EventWeightsIterativeGen outputFile='WWTo2L2Nu.root'     weight=12.178   histoName='MT/results' sumHistoName='sumweights/genWeights'
    EventWeightsIterativeGen outputFile='GluGluWWTo2L2Nu.root'     weight=0.59   histoName='MT/results' sumHistoName='sumweights/genWeights' #gg->WW (3.974 × 0.1086 × 0.1086 × (9 × 1.4)
    #CHANGE ME
    EventWeightsIterativeGen outputFile='WW_EWK.root'     weight=0.345   histoName='MT/results' sumHistoName='sumweights/genWeights'
    EventWeightsIterativeGen outputFile='WW_DPS.root'     weight=1.62   histoName='MT/results' sumHistoName='sumweights/genWeights'
    EventWeightsIterativeGen outputFile='WW_SS_EWK.root'     weight=0.026   histoName='MT/results' sumHistoName='sumweights/genWeights'
    EventWeightsIterativeGen outputFile='WW_SS_QCD.root'     weight=0.026   histoName='MT/results' sumHistoName='sumweights/genWeights'

    echo 'Weight t_tW'
    EventWeightsIterativeGen outputFile='t_tW.root'       weight=38.09    histoName='MT/results' sumHistoName='sumweights/genWeights'
    echo 'Weight tBar_tW'
    EventWeightsIterativeGen outputFile='tBar_tW.root'    weight=38.09    histoName='MT/results' sumHistoName='sumweights/genWeights'
    echo 'Weight St_antitop'
    EventWeightsIterativeGen outputFile='St_antitop.root'       weight=24.11    histoName='MT/results' sumHistoName='sumweights/genWeights' #80.59 pb * 3*.108
    echo 'Weight St_top'
    EventWeightsIterativeGen outputFile='St_top.root'       weight=39.852    histoName='MT/results' sumHistoName='sumweights/genWeights' #136 * 3*.108

    #hadd -f DiBoson.root WWTo*root WZTo*root ZZTo*.root St_*.root t*tW.root VVTo*root
fi


if [ $weightBaryonic -eq 1 ]
then
    EventWeightsIterativeGen outputFile='ZpBaryonic_Zp10000_MChi1.root'     weight=1    histoName='MT/results' sumHistoName='sumweights/genWeights'
    EventWeightsIterativeGen outputFile='ZpBaryonic_Zp10000_MChi10.root'     weight=1    histoName='MT/results' sumHistoName='sumweights/genWeights'
    EventWeightsIterativeGen outputFile='ZpBaryonic_Zp10000_MChi1000.root'     weight=1    histoName='MT/results' sumHistoName='sumweights/genWeights'
    EventWeightsIterativeGen outputFile='ZpBaryonic_Zp10000_MChi150.root'     weight=1    histoName='MT/results' sumHistoName='sumweights/genWeights'
    EventWeightsIterativeGen outputFile='ZpBaryonic_Zp10000_MChi50.root'     weight=1    histoName='MT/results' sumHistoName='sumweights/genWeights'
    EventWeightsIterativeGen outputFile='ZpBaryonic_Zp10000_MChi500.root'     weight=1    histoName='MT/results' sumHistoName='sumweights/genWeights'
    EventWeightsIterativeGen outputFile='ZpBaryonic_Zp1000_MChi1.root'     weight=1    histoName='MT/results' sumHistoName='sumweights/genWeights'
    EventWeightsIterativeGen outputFile='ZpBaryonic_Zp1000_MChi1000.root'     weight=1    histoName='MT/results' sumHistoName='sumweights/genWeights'
    EventWeightsIterativeGen outputFile='ZpBaryonic_Zp1000_MChi150.root'     weight=1    histoName='MT/results' sumHistoName='sumweights/genWeights'
    EventWeightsIterativeGen outputFile='ZpBaryonic_Zp100_MChi1.root'     weight=1    histoName='MT/results' sumHistoName='sumweights/genWeights'
    EventWeightsIterativeGen outputFile='ZpBaryonic_Zp100_MChi10.root'     weight=1    histoName='MT/results' sumHistoName='sumweights/genWeights'
    EventWeightsIterativeGen outputFile='ZpBaryonic_Zp10_MChi1.root'     weight=1    histoName='MT/results' sumHistoName='sumweights/genWeights'
    EventWeightsIterativeGen outputFile='ZpBaryonic_Zp10_MChi10.root'     weight=1    histoName='MT/results' sumHistoName='sumweights/genWeights'
    EventWeightsIterativeGen outputFile='ZpBaryonic_Zp10_MChi1000.root'     weight=1    histoName='MT/results' sumHistoName='sumweights/genWeights'
    EventWeightsIterativeGen outputFile='ZpBaryonic_Zp10_MChi150.root'     weight=1    histoName='MT/results' sumHistoName='sumweights/genWeights'
    EventWeightsIterativeGen outputFile='ZpBaryonic_Zp10_MChi50.root'     weight=1    histoName='MT/results' sumHistoName='sumweights/genWeights'
    EventWeightsIterativeGen outputFile='ZpBaryonic_Zp10_MChi500.root'     weight=1    histoName='MT/results' sumHistoName='sumweights/genWeights'
    EventWeightsIterativeGen outputFile='ZpBaryonic_Zp500_MChi500.root'     weight=1    histoName='MT/results' sumHistoName='sumweights/genWeights'
    EventWeightsIterativeGen outputFile='ZpBaryonic_Zp500_MChi150.root'     weight=1    histoName='MT/results' sumHistoName='sumweights/genWeights'
    EventWeightsIterativeGen outputFile='ZpBaryonic_Zp200_MChi150.root'     weight=1    histoName='MT/results' sumHistoName='sumweights/genWeights'
    EventWeightsIterativeGen outputFile='ZpBaryonic_Zp200_MChi50.root'     weight=1    histoName='MT/results' sumHistoName='sumweights/genWeights'
    EventWeightsIterativeGen outputFile='ZpBaryonic_Zp50_MChi1.root'     weight=1    histoName='MT/results' sumHistoName='sumweights/genWeights'
    EventWeightsIterativeGen outputFile='ZpBaryonic_Zp50_MChi10.root'     weight=1    histoName='MT/results' sumHistoName='sumweights/genWeights'
fi

if [ $weightZinv -eq 1 ]
then
    EventWeightsIterativeGen outputFile='Zprime600Zh.root'     weight=1    histoName='MT/results' sumHistoName='sumweights/genWeights'
    EventWeightsIterativeGen outputFile='Zprime800Zh.root'     weight=1    histoName='MT/results' sumHistoName='sumweights/genWeights'
    EventWeightsIterativeGen outputFile='Zprime1000Zh.root'     weight=1    histoName='MT/results' sumHistoName='sumweights/genWeights'
    EventWeightsIterativeGen outputFile='Zprime1200Zh.root'     weight=1    histoName='MT/results' sumHistoName='sumweights/genWeights'
    EventWeightsIterativeGen outputFile='Zprime1400Zh.root'     weight=1    histoName='MT/results' sumHistoName='sumweights/genWeights'
    EventWeightsIterativeGen outputFile='Zprime1700Zh.root'     weight=1    histoName='MT/results' sumHistoName='sumweights/genWeights'
    EventWeightsIterativeGen outputFile='Zprime2000Zh.root'     weight=1    histoName='MT/results' sumHistoName='sumweights/genWeights'
    EventWeightsIterativeGen outputFile='Zprime2500Zh.root'     weight=1    histoName='MT/results' sumHistoName='sumweights/genWeights'
fi


if [ $weightAh -eq 1 ]
then
    echo 'Zprime600A300h.root'
    EventWeightsIterativeGen outputFile='Zprime600A300h.root'     weight=1    histoName='MT/results' sumHistoName='sumweights/genWeights'
    echo 'Zprime600A400h.root'
    EventWeightsIterativeGen outputFile='Zprime600A400h.root'     weight=1    histoName='MT/results' sumHistoName='sumweights/genWeights'
    echo 'Zprime800A300h.root'
    EventWeightsIterativeGen outputFile='Zprime800A300h.root'     weight=1    histoName='MT/results' sumHistoName='sumweights/genWeights'
    echo 'Zprime800A400h.root'
    EventWeightsIterativeGen outputFile='Zprime800A400h.root'     weight=1    histoName='MT/results' sumHistoName='sumweights/genWeights'
    echo 'Zprime800A500h.root'
    EventWeightsIterativeGen outputFile='Zprime800A500h.root'     weight=1    histoName='MT/results' sumHistoName='sumweights/genWeights'
    echo 'Zprime800A600h.root'
    EventWeightsIterativeGen outputFile='Zprime800A600h.root'     weight=1    histoName='MT/results' sumHistoName='sumweights/genWeights'
    echo 'Zprime1000A300h.root'
    EventWeightsIterativeGen outputFile='Zprime1000A300h.root'     weight=1    histoName='MT/results' sumHistoName='sumweights/genWeights'
    echo 'Zprime1000A400h.root'
    EventWeightsIterativeGen outputFile='Zprime1000A400h.root'     weight=1    histoName='MT/results' sumHistoName='sumweights/genWeights'
    echo 'Zprime1000A500h.root'
    EventWeightsIterativeGen outputFile='Zprime1000A500h.root'     weight=1    histoName='MT/results' sumHistoName='sumweights/genWeights'
    echo 'Zprime1000A600h.root'
    EventWeightsIterativeGen outputFile='Zprime1000A600h.root'     weight=1    histoName='MT/results' sumHistoName='sumweights/genWeights'
    echo 'Zprime1000A700h.root'
    EventWeightsIterativeGen outputFile='Zprime1000A700h.root'     weight=1    histoName='MT/results' sumHistoName='sumweights/genWeights'
    echo 'Zprime1000A800h.root'
    EventWeightsIterativeGen outputFile='Zprime1000A800h.root'     weight=1    histoName='MT/results' sumHistoName='sumweights/genWeights'
    echo 'Zprime1200A300h.root'
    EventWeightsIterativeGen outputFile='Zprime1200A300h.root'     weight=1    histoName='MT/results' sumHistoName='sumweights/genWeights'
    echo 'Zprime1200A400h.root'
    EventWeightsIterativeGen outputFile='Zprime1200A400h.root'     weight=1    histoName='MT/results' sumHistoName='sumweights/genWeights'
    echo 'Zprime1200A500h.root'
    EventWeightsIterativeGen outputFile='Zprime1200A500h.root'     weight=1    histoName='MT/results' sumHistoName='sumweights/genWeights'
    echo 'Zprime1200A600h.root'
    EventWeightsIterativeGen outputFile='Zprime1200A600h.root'     weight=1    histoName='MT/results' sumHistoName='sumweights/genWeights'
    echo 'Zprime1200A700h.root'
    EventWeightsIterativeGen outputFile='Zprime1200A700h.root'     weight=1    histoName='MT/results' sumHistoName='sumweights/genWeights'
    echo 'Zprime1200A800h.root'
    EventWeightsIterativeGen outputFile='Zprime1200A800h.root'     weight=1    histoName='MT/results' sumHistoName='sumweights/genWeights'
    echo 'Zprime1400A300h.root'
    EventWeightsIterativeGen outputFile='Zprime1400A300h.root'     weight=1    histoName='MT/results' sumHistoName='sumweights/genWeights'
    echo 'Zprime1400A400h.root'
    EventWeightsIterativeGen outputFile='Zprime1400A400h.root'     weight=1    histoName='MT/results' sumHistoName='sumweights/genWeights'
    echo 'Zprime1400A500h.root'
    EventWeightsIterativeGen outputFile='Zprime1400A500h.root'     weight=1    histoName='MT/results' sumHistoName='sumweights/genWeights'
    echo 'Zprime1400A600h.root'
    EventWeightsIterativeGen outputFile='Zprime1400A600h.root'     weight=1    histoName='MT/results' sumHistoName='sumweights/genWeights'
    echo 'Zprime1400A700h.root'
    EventWeightsIterativeGen outputFile='Zprime1400A700h.root'     weight=1    histoName='MT/results' sumHistoName='sumweights/genWeights'
    echo 'Zprime1400A800h.root'
    EventWeightsIterativeGen outputFile='Zprime1400A800h.root'     weight=1    histoName='MT/results' sumHistoName='sumweights/genWeights'
    echo 'Zprime1700A300h.root'
    EventWeightsIterativeGen outputFile='Zprime1700A300h.root'     weight=1    histoName='MT/results' sumHistoName='sumweights/genWeights'
    echo 'Zprime1700A400h.root'
    EventWeightsIterativeGen outputFile='Zprime1700A400h.root'     weight=1    histoName='MT/results' sumHistoName='sumweights/genWeights'
    echo 'Zprime1700A500h.root'
    EventWeightsIterativeGen outputFile='Zprime1700A500h.root'     weight=1    histoName='MT/results' sumHistoName='sumweights/genWeights'
    echo 'Zprime1700A600h.root'
    EventWeightsIterativeGen outputFile='Zprime1700A600h.root'     weight=1    histoName='MT/results' sumHistoName='sumweights/genWeights'
    echo 'Zprime1700A700h.root'
    EventWeightsIterativeGen outputFile='Zprime1700A700h.root'     weight=1    histoName='MT/results' sumHistoName='sumweights/genWeights'
    echo 'Zprime1700A800h.root'
    EventWeightsIterativeGen outputFile='Zprime1700A800h.root'     weight=1    histoName='MT/results' sumHistoName='sumweights/genWeights'
    echo 'Zprime2000A300h.root'
    EventWeightsIterativeGen outputFile='Zprime2000A300h.root'     weight=1    histoName='MT/results' sumHistoName='sumweights/genWeights'
    echo 'Zprime2000A400h.root'
    EventWeightsIterativeGen outputFile='Zprime2000A400h.root'     weight=1    histoName='MT/results' sumHistoName='sumweights/genWeights'
    echo 'Zprime2000A500h.root'
    EventWeightsIterativeGen outputFile='Zprime2000A500h.root'     weight=1    histoName='MT/results' sumHistoName='sumweights/genWeights'
    echo 'Zprime2000A600h.root'
    EventWeightsIterativeGen outputFile='Zprime2000A600h.root'     weight=1    histoName='MT/results' sumHistoName='sumweights/genWeights'
    echo 'Zprime2000A700h.root'
    EventWeightsIterativeGen outputFile='Zprime2000A700h.root'     weight=1    histoName='MT/results' sumHistoName='sumweights/genWeights'
    echo 'Zprime2000A800h.root'
    EventWeightsIterativeGen outputFile='Zprime2000A800h.root'     weight=1    histoName='MT/results' sumHistoName='sumweights/genWeights'
    echo 'Zprime2500A300h.root'
    EventWeightsIterativeGen outputFile='Zprime2500A300h.root'     weight=1    histoName='MT/results' sumHistoName='sumweights/genWeights'
    echo 'Zprime2500A400h.root'
    EventWeightsIterativeGen outputFile='Zprime2500A400h.root'     weight=1    histoName='MT/results' sumHistoName='sumweights/genWeights'
    echo 'Zprime2500A500h.root'
    EventWeightsIterativeGen outputFile='Zprime2500A500h.root'     weight=1    histoName='MT/results' sumHistoName='sumweights/genWeights'
    echo 'Zprime2500A600h.root'
    EventWeightsIterativeGen outputFile='Zprime2500A600h.root'     weight=1    histoName='MT/results' sumHistoName='sumweights/genWeights'
    echo 'Zprime2500A700h.root'
    EventWeightsIterativeGen outputFile='Zprime2500A700h.root'     weight=1    histoName='MT/results' sumHistoName='sumweights/genWeights'
    echo 'Zprime2500A800h.root'
    EventWeightsIterativeGen outputFile='Zprime2500A800h.root'     weight=1    histoName='MT/results' sumHistoName='sumweights/genWeights'
fi

if [ $weightEWK -eq 1 ]
then
    echo 'Weight EWK'
    EventWeightsIterativeGen outputFile='EWKZ2JetLL.root'  weight=3.987    histoName='MT/results' sumHistoName='sumweights/genWeights' 
    EventWeightsIterativeGen outputFile='EWKZ2JetNuNu.root'  weight=10.01    histoName='MT/results' sumHistoName='sumweights/genWeights' 
    EventWeightsIterativeGen outputFile='EWKminus2jet.root'  weight=20.25    histoName='MT/results' sumHistoName='sumweights/genWeights' 
    EventWeightsIterativeGen outputFile='EWKplus2jet.root'  weight=25.62    histoName='MT/results' sumHistoName='sumweights/genWeights' 

    hadd EWK.root EWK*root 
    hadd EWKZ.root EWKZ*root 
    hadd EWKW.root EWK*2jet.root 

fi

if [ $weightTriBoson -eq 1 ]
then
    echo 'Weight Triboson'
    nohup EventWeightsIterativeGen outputFile='WWW.root'  weight=0.2086    histoName='MT/results' sumHistoName='sumweights/genWeights' &
    nohup EventWeightsIterativeGen outputFile='WWZ.root'  weight=0.1651    histoName='MT/results' sumHistoName='sumweights/genWeights' &
    nohup EventWeightsIterativeGen outputFile='WZZ.root'  weight=0.05565   histoName='MT/results' sumHistoName='sumweights/genWeights' &
    nohup EventWeightsIterativeGen outputFile='ZZZ.root'  weight=0.01398   histoName='MT/results' sumHistoName='sumweights/genWeights' &
fi

