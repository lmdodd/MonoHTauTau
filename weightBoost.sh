#!/bin/sh

#mkdir /nfs_scratch/$USER/monohiggs_weighted
#cp /nfs_scratch/$USER/monohiggs_unweighted/* /nfs_scratch/$USER/monohiggs_weighted/.
cd /nfs_scratch/$USER/monohiggs_boosted_weighted/

weight=0;
weightTT=0;
weightH=1;
weightW=0;
weightBaryonic=3;
weightZ=0;
weightZN=0;
weightZinv=0;
weightAh=0;


if [ $weightH -eq 1 ]
then
    echo 'weight ggH'
    EventWeightsIterativeGen outputFile='ggH125.root'     weight=2.767578    histoName='TT/results' sumHistoName='sumweights/genWeights' 
    echo 'weight vbf'
    EventWeightsIterativeGen outputFile='vbfH125.root'     weight=0.2371314    histoName='TT/results' sumHistoName='sumweights/genWeights' 
    echo 'weight ZH'
    EventWeightsIterativeGen outputFile='zH125.root'     weight=0.05542053    histoName='TT/results' sumHistoName='sumweights/genWeights' 
    hadd smH125.root ggH125.root vbfH125.root zH125.root  
fi

if [ $weightZN -eq 1 ]
then
    EventWeightsIterativeZNuNu root200=ZJetsNuNu200.root root400=ZJetsNuNu400.root root600=ZJetsNuNu600.root root800=ZJetsNuNu800.root root1200=ZJetsNuNu1200.root root2500=ZJetsNuNu2500.root rootinf=ZJetsNuNuInf.root   weight=1    histoName='TT/results' 
    hadd Znunu.root ZJetsNuNu*root 
fi

if [ $weightW -eq 1 ]
then
    EventWeightsIterativeWJetsHT  weight=1    histoName='TT/results' 
    #hadd WJETSHT.root WJets*root 
    #EventWeightsIterativeWJets  weight=1    histoName='TT/results' 
    hadd WJETS.root WJets*root 
fi


if [ $weightZ -eq 1 ]
then
    EventWeightsIterativeZJets    weight=1    histoName='TT/results' 
    hadd ZJETS.root ZJets_ext1.root Z1Jets.root Z2Jets.root Z3Jets.root Z4Jets.root ZJets_150.root
    #make sure Zpt root file is around!!!
    #currently unused
    #EventWeightsIterativeZPt    weight=1    histoName='TT/results' 
fi


if [ $weightTT -eq 1 ]
then
    echo 'Weight TT'
    nohup EventWeightsIterativeTT outputFile='TT.root'  weight=831.76     histoName='TT/results' sumHistoName='sumweights/genWeights' &
    #EventWeightsIterativeTT has top pt reweighting

fi

if [ $weight -eq 1 ]
then

    #echo 'Weight WAMC'
    echo 'Weight ZZ'
    EventWeightsIterativeGen outputFile='ZZTo2L2Q.root'      weight=3.22  histoName='TT/results' sumHistoName='sumweights/genWeights'
    #EventWeightsIterativeGen outputFile='ZZTo4L.root'      weight=1.212  histoName='TT/results' sumHistoName='sumweights/genWeights'


    echo 'Weight WZ 1L1NuQQ'
    EventWeightsIterativeGen outputFile='WZTo1L1Nu2Q.root'      weight=10.71   histoName='TT/results' sumHistoName='sumweights/genWeights'
    echo 'Weight WZ 2L2Q'
    EventWeightsIterativeGen outputFile='WZTo2L2Q.root'      weight=5.595   histoName='TT/results' sumHistoName='sumweights/genWeights'
    echo 'Weight WZ 1L3Nu'
    EventWeightsIterativeGen outputFile='WZTo1L3Nu.root'      weight=3.05   histoName='TT/results' sumHistoName='sumweights/genWeights'
    #EventWeightsIterativeGen outputFile='WZJTo1L3Nu.root'      weight=4.708   histoName='TT/results' sumHistoName='sumweights/genWeights'
    #add m_ll>30

    echo 'Weight WW to L1Nu QQ'
    EventWeightsIterativeGen outputFile='WWTo1L1Nu2Q.root'     weight=1.212     histoName='TT/results' sumHistoName='sumweights/genWeights'
    #EventWeightsIterativeGen outputFile='WWTo2L2Q.root'     weight=49.997    histoName='TT/results' sumHistoName='sumweights/genWeights'

    echo 'Weight VV to 2L2Nu'
    EventWeightsIterativeGen outputFile='VVTo2L2Nu.root'     weight=11.95    histoName='TT/results' sumHistoName='sumweights/genWeights'

    echo 'Weight t_tW'
    EventWeightsIterativeGen outputFile='t_tW.root'       weight=35.6    histoName='TT/results' sumHistoName='sumweights/genWeights'
    echo 'Weight tBar_tW'
    EventWeightsIterativeGen outputFile='tBar_tW.root'    weight=35.6    histoName='TT/results' sumHistoName='sumweights/genWeights'
    echo 'Weight St_antitop'
    EventWeightsIterativeGen outputFile='St_antitop.root'       weight=26.23    histoName='TT/results' sumHistoName='sumweights/genWeights' #80.59 pb * 3*.108
    echo 'Weight St_top'
    EventWeightsIterativeGen outputFile='St_top.root'       weight=44.07    histoName='TT/results' sumHistoName='sumweights/genWeights' #136 * 3*.108

    hadd -f DiBoson.root WWTo*root WZTo*root ZZTo*.root St_*.root t*tW.root VVTo*root
fi


if [ $weightBaryonic -eq 1 ]
then
    EventWeightsIterativeGen outputFile='ZpBaryonic_Zp10000_MChi1.root'     weight=1    histoName='TT/results' sumHistoName='sumweights/genWeights'
    EventWeightsIterativeGen outputFile='ZpBaryonic_Zp10000_MChi10.root'     weight=1    histoName='TT/results' sumHistoName='sumweights/genWeights'
    EventWeightsIterativeGen outputFile='ZpBaryonic_Zp10000_MChi1000.root'     weight=1    histoName='TT/results' sumHistoName='sumweights/genWeights'
    EventWeightsIterativeGen outputFile='ZpBaryonic_Zp10000_MChi150.root'     weight=1    histoName='TT/results' sumHistoName='sumweights/genWeights'
    EventWeightsIterativeGen outputFile='ZpBaryonic_Zp10000_MChi50.root'     weight=1    histoName='TT/results' sumHistoName='sumweights/genWeights'
    EventWeightsIterativeGen outputFile='ZpBaryonic_Zp10000_MChi500.root'     weight=1    histoName='TT/results' sumHistoName='sumweights/genWeights'
    EventWeightsIterativeGen outputFile='ZpBaryonic_Zp1000_MChi1.root'     weight=1    histoName='TT/results' sumHistoName='sumweights/genWeights'
    EventWeightsIterativeGen outputFile='ZpBaryonic_Zp1000_MChi1000.root'     weight=1    histoName='TT/results' sumHistoName='sumweights/genWeights'
    EventWeightsIterativeGen outputFile='ZpBaryonic_Zp1000_MChi150.root'     weight=1    histoName='TT/results' sumHistoName='sumweights/genWeights'
    EventWeightsIterativeGen outputFile='ZpBaryonic_Zp100_MChi1.root'     weight=1    histoName='TT/results' sumHistoName='sumweights/genWeights'
    EventWeightsIterativeGen outputFile='ZpBaryonic_Zp100_MChi10.root'     weight=1    histoName='TT/results' sumHistoName='sumweights/genWeights'
    EventWeightsIterativeGen outputFile='ZpBaryonic_Zp10_MChi1.root'     weight=1    histoName='TT/results' sumHistoName='sumweights/genWeights'
    EventWeightsIterativeGen outputFile='ZpBaryonic_Zp10_MChi10.root'     weight=1    histoName='TT/results' sumHistoName='sumweights/genWeights'
    EventWeightsIterativeGen outputFile='ZpBaryonic_Zp10_MChi1000.root'     weight=1    histoName='TT/results' sumHistoName='sumweights/genWeights'
    EventWeightsIterativeGen outputFile='ZpBaryonic_Zp10_MChi150.root'     weight=1    histoName='TT/results' sumHistoName='sumweights/genWeights'
    EventWeightsIterativeGen outputFile='ZpBaryonic_Zp10_MChi50.root'     weight=1    histoName='TT/results' sumHistoName='sumweights/genWeights'
    EventWeightsIterativeGen outputFile='ZpBaryonic_Zp10_MChi500.root'     weight=1    histoName='TT/results' sumHistoName='sumweights/genWeights'
    EventWeightsIterativeGen outputFile='ZpBaryonic_Zp500_MChi500.root'     weight=1    histoName='TT/results' sumHistoName='sumweights/genWeights'
    EventWeightsIterativeGen outputFile='ZpBaryonic_Zp500_MChi150.root'     weight=1    histoName='TT/results' sumHistoName='sumweights/genWeights'
    EventWeightsIterativeGen outputFile='ZpBaryonic_Zp500_MChi1.root'     weight=1    histoName='TT/results' sumHistoName='sumweights/genWeights'
fi

if [ $weightZinv -eq 1 ]
then
    EventWeightsIterativeGen outputFile='Zprime600Zh.root'     weight=1    histoName='TT/results' sumHistoName='sumweights/genWeights'
    EventWeightsIterativeGen outputFile='Zprime800Zh.root'     weight=1    histoName='TT/results' sumHistoName='sumweights/genWeights'
    EventWeightsIterativeGen outputFile='Zprime1000Zh.root'     weight=1    histoName='TT/results' sumHistoName='sumweights/genWeights'
    EventWeightsIterativeGen outputFile='Zprime1200Zh.root'     weight=1    histoName='TT/results' sumHistoName='sumweights/genWeights'
    EventWeightsIterativeGen outputFile='Zprime1400Zh.root'     weight=1    histoName='TT/results' sumHistoName='sumweights/genWeights'
    EventWeightsIterativeGen outputFile='Zprime1700Zh.root'     weight=1    histoName='TT/results' sumHistoName='sumweights/genWeights'
    #EventWeightsIterativeGen outputFile='Zprime2000Zh.root'     weight=1    histoName='TT/results' sumHistoName='sumweights/genWeights'
    #EventWeightsIterativeGen outputFile='Zprime2500Zh.root'     weight=1    histoName='TT/results' sumHistoName='sumweights/genWeights'
fi


if [ $weightAh -eq 1 ]
then
    echo 'Zprime600A300h.root'
    EventWeightsIterativeGen outputFile='Zprime600A300h.root'     weight=1    histoName='TT/results' sumHistoName='sumweights/genWeights'
    echo 'Zprime600A400h.root'
    EventWeightsIterativeGen outputFile='Zprime600A400h.root'     weight=1    histoName='TT/results' sumHistoName='sumweights/genWeights'
    echo 'Zprime800A300h.root'
    EventWeightsIterativeGen outputFile='Zprime800A300h.root'     weight=1    histoName='TT/results' sumHistoName='sumweights/genWeights'
    echo 'Zprime800A400h.root'
    EventWeightsIterativeGen outputFile='Zprime800A400h.root'     weight=1    histoName='TT/results' sumHistoName='sumweights/genWeights'
    echo 'Zprime800A500h.root'
    EventWeightsIterativeGen outputFile='Zprime800A500h.root'     weight=1    histoName='TT/results' sumHistoName='sumweights/genWeights'
    echo 'Zprime800A600h.root'
    EventWeightsIterativeGen outputFile='Zprime800A600h.root'     weight=1    histoName='TT/results' sumHistoName='sumweights/genWeights'
    echo 'Zprime1000A300h.root'
    EventWeightsIterativeGen outputFile='Zprime1000A300h.root'     weight=1    histoName='TT/results' sumHistoName='sumweights/genWeights'
    echo 'Zprime1000A400h.root'
    EventWeightsIterativeGen outputFile='Zprime1000A400h.root'     weight=1    histoName='TT/results' sumHistoName='sumweights/genWeights'
    echo 'Zprime1000A500h.root'
    EventWeightsIterativeGen outputFile='Zprime1000A500h.root'     weight=1    histoName='TT/results' sumHistoName='sumweights/genWeights'
    echo 'Zprime1000A600h.root'
    EventWeightsIterativeGen outputFile='Zprime1000A600h.root'     weight=1    histoName='TT/results' sumHistoName='sumweights/genWeights'
    echo 'Zprime1000A700h.root'
    EventWeightsIterativeGen outputFile='Zprime1000A700h.root'     weight=1    histoName='TT/results' sumHistoName='sumweights/genWeights'
    echo 'Zprime1000A800h.root'
    EventWeightsIterativeGen outputFile='Zprime1000A800h.root'     weight=1    histoName='TT/results' sumHistoName='sumweights/genWeights'
    echo 'Zprime1200A300h.root'
    EventWeightsIterativeGen outputFile='Zprime1200A300h.root'     weight=1    histoName='TT/results' sumHistoName='sumweights/genWeights'
    echo 'Zprime1200A400h.root'
    EventWeightsIterativeGen outputFile='Zprime1200A400h.root'     weight=1    histoName='TT/results' sumHistoName='sumweights/genWeights'
    echo 'Zprime1200A500h.root'
    EventWeightsIterativeGen outputFile='Zprime1200A500h.root'     weight=1    histoName='TT/results' sumHistoName='sumweights/genWeights'
    echo 'Zprime1200A600h.root'
    EventWeightsIterativeGen outputFile='Zprime1200A600h.root'     weight=1    histoName='TT/results' sumHistoName='sumweights/genWeights'
    echo 'Zprime1200A700h.root'
    EventWeightsIterativeGen outputFile='Zprime1200A700h.root'     weight=1    histoName='TT/results' sumHistoName='sumweights/genWeights'
    echo 'Zprime1200A800h.root'
    EventWeightsIterativeGen outputFile='Zprime1200A800h.root'     weight=1    histoName='TT/results' sumHistoName='sumweights/genWeights'
    echo 'Zprime1400A300h.root'
    EventWeightsIterativeGen outputFile='Zprime1400A300h.root'     weight=1    histoName='TT/results' sumHistoName='sumweights/genWeights'
    echo 'Zprime1400A400h.root'
    EventWeightsIterativeGen outputFile='Zprime1400A400h.root'     weight=1    histoName='TT/results' sumHistoName='sumweights/genWeights'
    echo 'Zprime1400A500h.root'
    EventWeightsIterativeGen outputFile='Zprime1400A500h.root'     weight=1    histoName='TT/results' sumHistoName='sumweights/genWeights'
    echo 'Zprime1400A600h.root'
    EventWeightsIterativeGen outputFile='Zprime1400A600h.root'     weight=1    histoName='TT/results' sumHistoName='sumweights/genWeights'
    echo 'Zprime1400A700h.root'
    EventWeightsIterativeGen outputFile='Zprime1400A700h.root'     weight=1    histoName='TT/results' sumHistoName='sumweights/genWeights'
    echo 'Zprime1400A800h.root'
    EventWeightsIterativeGen outputFile='Zprime1400A800h.root'     weight=1    histoName='TT/results' sumHistoName='sumweights/genWeights'
    echo 'Zprime1700A300h.root'
    EventWeightsIterativeGen outputFile='Zprime1700A300h.root'     weight=1    histoName='TT/results' sumHistoName='sumweights/genWeights'
    echo 'Zprime1700A400h.root'
    EventWeightsIterativeGen outputFile='Zprime1700A400h.root'     weight=1    histoName='TT/results' sumHistoName='sumweights/genWeights'
    echo 'Zprime1700A500h.root'
    EventWeightsIterativeGen outputFile='Zprime1700A500h.root'     weight=1    histoName='TT/results' sumHistoName='sumweights/genWeights'
    echo 'Zprime1700A600h.root'
    EventWeightsIterativeGen outputFile='Zprime1700A600h.root'     weight=1    histoName='TT/results' sumHistoName='sumweights/genWeights'
    echo 'Zprime1700A700h.root'
    EventWeightsIterativeGen outputFile='Zprime1700A700h.root'     weight=1    histoName='TT/results' sumHistoName='sumweights/genWeights'
    echo 'Zprime1700A800h.root'
    EventWeightsIterativeGen outputFile='Zprime1700A800h.root'     weight=1    histoName='TT/results' sumHistoName='sumweights/genWeights'
    echo 'Zprime2000A300h.root'
    EventWeightsIterativeGen outputFile='Zprime2000A300h.root'     weight=1    histoName='TT/results' sumHistoName='sumweights/genWeights'
    echo 'Zprime2000A400h.root'
    EventWeightsIterativeGen outputFile='Zprime2000A400h.root'     weight=1    histoName='TT/results' sumHistoName='sumweights/genWeights'
    echo 'Zprime2000A500h.root'
    EventWeightsIterativeGen outputFile='Zprime2000A500h.root'     weight=1    histoName='TT/results' sumHistoName='sumweights/genWeights'
    echo 'Zprime2000A600h.root'
    EventWeightsIterativeGen outputFile='Zprime2000A600h.root'     weight=1    histoName='TT/results' sumHistoName='sumweights/genWeights'
    echo 'Zprime2000A700h.root'
    EventWeightsIterativeGen outputFile='Zprime2000A700h.root'     weight=1    histoName='TT/results' sumHistoName='sumweights/genWeights'
    echo 'Zprime2000A800h.root'
    EventWeightsIterativeGen outputFile='Zprime2000A800h.root'     weight=1    histoName='TT/results' sumHistoName='sumweights/genWeights'
    echo 'Zprime2500A300h.root'
    EventWeightsIterativeGen outputFile='Zprime2500A300h.root'     weight=1    histoName='TT/results' sumHistoName='sumweights/genWeights'
    echo 'Zprime2500A400h.root'
    EventWeightsIterativeGen outputFile='Zprime2500A400h.root'     weight=1    histoName='TT/results' sumHistoName='sumweights/genWeights'
    echo 'Zprime2500A500h.root'
    EventWeightsIterativeGen outputFile='Zprime2500A500h.root'     weight=1    histoName='TT/results' sumHistoName='sumweights/genWeights'
    echo 'Zprime2500A600h.root'
    EventWeightsIterativeGen outputFile='Zprime2500A600h.root'     weight=1    histoName='TT/results' sumHistoName='sumweights/genWeights'
    echo 'Zprime2500A700h.root'
    EventWeightsIterativeGen outputFile='Zprime2500A700h.root'     weight=1    histoName='TT/results' sumHistoName='sumweights/genWeights'
    echo 'Zprime2500A800h.root'
    EventWeightsIterativeGen outputFile='Zprime2500A800h.root'     weight=1    histoName='TT/results' sumHistoName='sumweights/genWeights'
fi

