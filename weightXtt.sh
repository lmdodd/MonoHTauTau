#!/bin/sh
mkdir /nfs_scratch/$USER/monohiggs_weighted/
cp /nfs_scratch/$USER/monohiggs_unweighted/* /nfs_scratch/$USER/monohiggs_weighted/
cd /nfs_scratch/$USER/monohiggs_weighted/


weightZ=0;
weightZinv=0;
weightAh=1;


if [ $weightZinv -eq 1 ]
    then
    echo 'weight Zinvh 600'
    EventWeightsIterativeGen outputFile='Zprime600Zh.root'     weight=1    histoName='MT/results' sumHistoName='sumweights/genWeights'
    echo 'weight Zinvh 800'
    EventWeightsIterativeGen outputFile='Zprime800Zh.root'     weight=1    histoName='MT/results' sumHistoName='sumweights/genWeights'
    echo 'weight Zinvh 1000'
    EventWeightsIterativeGen outputFile='Zprime1000Zh.root'     weight=1    histoName='MT/results' sumHistoName='sumweights/genWeights'
    echo 'weight Zinvh 1200'
    EventWeightsIterativeGen outputFile='Zprime1200Zh.root'     weight=1    histoName='MT/results' sumHistoName='sumweights/genWeights'
    echo 'weight Zinvh 1400'
    EventWeightsIterativeGen outputFile='Zprime1400Zh.root'     weight=1    histoName='MT/results' sumHistoName='sumweights/genWeights'
    echo 'weight Zinvh 1700'
    EventWeightsIterativeGen outputFile='Zprime1700Zh.root'     weight=1    histoName='MT/results' sumHistoName='sumweights/genWeights'
    echo 'weight Zinvh 2000'
    EventWeightsIterativeGen outputFile='Zprime2000Zh.root'     weight=1    histoName='MT/results' sumHistoName='sumweights/genWeights'
    echo 'weight Zinvh 2500'
    EventWeightsIterativeGen outputFile='Zprime2500Zh.root'     weight=1    histoName='MT/results' sumHistoName='sumweights/genWeights'
fi

if [ $weightAh -eq 1 ]
    then
    EventWeightsIterativeGen outputFile='Zprime600A300h.root'     weight=1    histoName='MT/results' sumHistoName='sumweights/genWeights'
    EventWeightsIterativeGen outputFile='Zprime800A300h.root'     weight=1    histoName='MT/results' sumHistoName='sumweights/genWeights'
    EventWeightsIterativeGen outputFile='Zprime1000A300h.root'     weight=1    histoName='MT/results' sumHistoName='sumweights/genWeights'
    EventWeightsIterativeGen outputFile='Zprime1200A300h.root'     weight=1    histoName='MT/results' sumHistoName='sumweights/genWeights'
    EventWeightsIterativeGen outputFile='Zprime1400A300h.root'     weight=1    histoName='MT/results' sumHistoName='sumweights/genWeights'
    EventWeightsIterativeGen outputFile='Zprime1700A300h.root'     weight=1    histoName='MT/results' sumHistoName='sumweights/genWeights'
    EventWeightsIterativeGen outputFile='Zprime2000A300h.root'     weight=1    histoName='MT/results' sumHistoName='sumweights/genWeights'
    EventWeightsIterativeGen outputFile='Zprime2500A300h.root'     weight=1    histoName='MT/results' sumHistoName='sumweights/genWeights'
    echo 'weight ZAh 1'
    EventWeightsIterativeGen outputFile='Zprime600A400h.root'     weight=1    histoName='MT/results' sumHistoName='sumweights/genWeights'
    echo 'weight ZAh 2'
    EventWeightsIterativeGen outputFile='Zprime800A400h.root'     weight=1    histoName='MT/results' sumHistoName='sumweights/genWeights'
    echo 'weight ZAh 3'
    EventWeightsIterativeGen outputFile='Zprime800A500h.root'     weight=1    histoName='MT/results' sumHistoName='sumweights/genWeights'
    echo 'weight ZAh 4'
    EventWeightsIterativeGen outputFile='Zprime800A600h.root'     weight=1    histoName='MT/results' sumHistoName='sumweights/genWeights'
    echo 'weight ZAh 5'
    EventWeightsIterativeGen outputFile='Zprime1000A400h.root'     weight=1    histoName='MT/results' sumHistoName='sumweights/genWeights'
    echo 'weight ZAh 6'
    EventWeightsIterativeGen outputFile='Zprime1000A500h.root'     weight=1    histoName='MT/results' sumHistoName='sumweights/genWeights'
    echo 'weight ZAh 7'
    EventWeightsIterativeGen outputFile='Zprime1000A600h.root'     weight=1    histoName='MT/results' sumHistoName='sumweights/genWeights'
    echo 'weight ZAh 8'
    EventWeightsIterativeGen outputFile='Zprime1000A700h.root'     weight=1    histoName='MT/results' sumHistoName='sumweights/genWeights'
    echo 'weight ZAh 9'
    EventWeightsIterativeGen outputFile='Zprime1000A800h.root'     weight=1    histoName='MT/results' sumHistoName='sumweights/genWeights'
    echo 'weight ZAh 10'
    EventWeightsIterativeGen outputFile='Zprime1200A400h.root'     weight=1    histoName='MT/results' sumHistoName='sumweights/genWeights'
    echo 'weight ZAh 11'
    EventWeightsIterativeGen outputFile='Zprime1200A500h.root'     weight=1    histoName='MT/results' sumHistoName='sumweights/genWeights'
    echo 'weight ZAh 12'
    EventWeightsIterativeGen outputFile='Zprime1200A600h.root'     weight=1    histoName='MT/results' sumHistoName='sumweights/genWeights'
    echo 'weight ZAh 13'
    EventWeightsIterativeGen outputFile='Zprime1200A700h.root'     weight=1    histoName='MT/results' sumHistoName='sumweights/genWeights'
    echo 'weight ZAh 14'
    EventWeightsIterativeGen outputFile='Zprime1200A800h.root'     weight=1    histoName='MT/results' sumHistoName='sumweights/genWeights'
    echo 'weight ZAh 15'
    EventWeightsIterativeGen outputFile='Zprime1400A400h.root'     weight=1    histoName='MT/results' sumHistoName='sumweights/genWeights'
    echo 'weight ZAh 16'
    EventWeightsIterativeGen outputFile='Zprime1400A500h.root'     weight=1    histoName='MT/results' sumHistoName='sumweights/genWeights'
    echo 'weight ZAh 17'
    EventWeightsIterativeGen outputFile='Zprime1400A600h.root'     weight=1    histoName='MT/results' sumHistoName='sumweights/genWeights'
    echo 'weight ZAh 18'
    EventWeightsIterativeGen outputFile='Zprime1400A700h.root'     weight=1    histoName='MT/results' sumHistoName='sumweights/genWeights'
    echo 'weight ZAh 19'
    EventWeightsIterativeGen outputFile='Zprime1400A800h.root'     weight=1    histoName='MT/results' sumHistoName='sumweights/genWeights'
    echo 'weight ZAh 20'
    EventWeightsIterativeGen outputFile='Zprime1700A400h.root'     weight=1    histoName='MT/results' sumHistoName='sumweights/genWeights'
    echo 'weight ZAh 21'
    EventWeightsIterativeGen outputFile='Zprime1700A500h.root'     weight=1    histoName='MT/results' sumHistoName='sumweights/genWeights'
    echo 'weight ZAh 22'
    EventWeightsIterativeGen outputFile='Zprime1700A600h.root'     weight=1    histoName='MT/results' sumHistoName='sumweights/genWeights'
    echo 'weight ZAh 23'
    EventWeightsIterativeGen outputFile='Zprime1700A700h.root'     weight=1    histoName='MT/results' sumHistoName='sumweights/genWeights'
    echo 'weight ZAh 24'
    EventWeightsIterativeGen outputFile='Zprime1700A800h.root'     weight=1    histoName='MT/results' sumHistoName='sumweights/genWeights'
    echo 'weight ZAh 25'
    EventWeightsIterativeGen outputFile='Zprime2000A400h.root'     weight=1    histoName='MT/results' sumHistoName='sumweights/genWeights'
    echo 'weight ZAh 26'
    EventWeightsIterativeGen outputFile='Zprime2000A500h.root'     weight=1    histoName='MT/results' sumHistoName='sumweights/genWeights'
    echo 'weight ZAh 27'
    EventWeightsIterativeGen outputFile='Zprime2000A600h.root'     weight=1    histoName='MT/results' sumHistoName='sumweights/genWeights'
    echo 'weight ZAh 28'
    EventWeightsIterativeGen outputFile='Zprime2000A700h.root'     weight=1    histoName='MT/results' sumHistoName='sumweights/genWeights'
    echo 'weight ZAh 29'
    EventWeightsIterativeGen outputFile='Zprime2000A800h.root'     weight=1    histoName='MT/results' sumHistoName='sumweights/genWeights'
    echo 'weight ZAh 30'
    EventWeightsIterativeGen outputFile='Zprime2500A400h.root'     weight=1    histoName='MT/results' sumHistoName='sumweights/genWeights'
    echo 'weight ZAh 31'
    EventWeightsIterativeGen outputFile='Zprime2500A500h.root'     weight=1    histoName='MT/results' sumHistoName='sumweights/genWeights'
    echo 'weight ZAh 32'
    EventWeightsIterativeGen outputFile='Zprime2500A600h.root'     weight=1    histoName='MT/results' sumHistoName='sumweights/genWeights'
    echo 'weight ZAh 33'
    EventWeightsIterativeGen outputFile='Zprime2500A700h.root'     weight=1    histoName='MT/results' sumHistoName='sumweights/genWeights'
    echo 'weight ZAh 34'
    EventWeightsIterativeGen outputFile='Zprime2500A800h.root'     weight=1    histoName='MT/results' sumHistoName='sumweights/genWeights'
fi

if [ $weightZ -eq 1 ]
    then
    EventWeightsIterativeZNuNu root200=ZJetsNuNu200.root root400=ZJetsNuNu400.root root600=ZJetsNuNu600.root root800=ZJetsNuNu800.root root1200=ZJetsNuNu1200.root root2500=ZJetsNuNu2500.root rootinf=ZJetsNuNuInf.root   weight=1    histoName='MT/results' 
    hadd Znunu.root ZJetsNuNu*root 
     
fi

