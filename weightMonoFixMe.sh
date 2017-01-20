#!/bin/sh

#mkdir /nfs_scratch/$USER/monohiggs_weighted
#cp /nfs_scratch/$USER/monohiggs_unweighted/* /nfs_scratch/$USER/monohiggs_weighted/.
cd /nfs_scratch/$USER/monohiggs_DY/

weight=0;
weightBaryonic=0;
weightAh=0;

nohup EventWeightsIterativeFixMe  outputFile='ZJETS.root' &


if [ $weight -eq 1 ]
then
    nohup EventWeightsIterativeFixMe  outputFile='smH125.root' &
    nohup EventWeightsIterativeFixMe  outputFile='WJETS.root' &
    nohup EventWeightsIterativeFixMe  outputFile='ZJETS.root' &
    nohup EventWeightsIterativeFixMe  outputFile='TT.root' &
    nohup EventWeightsIterativeFixMe  outputFile='Znunu.root' &
    nohup EventWeightsIterativeFixMe  outputFile='DiBoson.root' &
fi


if [ $weightBaryonic -eq 1 ]
then
    EventWeightsIterativeFixMe outputFile='ZpBaryonic_Zp10000_MChi1.root'     
    EventWeightsIterativeFixMe outputFile='ZpBaryonic_Zp10000_MChi10.root'     
    EventWeightsIterativeFixMe outputFile='ZpBaryonic_Zp10000_MChi1000.root'     
    EventWeightsIterativeFixMe outputFile='ZpBaryonic_Zp10000_MChi150.root'     
    EventWeightsIterativeFixMe outputFile='ZpBaryonic_Zp10000_MChi50.root'     
    EventWeightsIterativeFixMe outputFile='ZpBaryonic_Zp10000_MChi500.root'     
    EventWeightsIterativeFixMe outputFile='ZpBaryonic_Zp1000_MChi1.root'     
    EventWeightsIterativeFixMe outputFile='ZpBaryonic_Zp1000_MChi1000.root'     
    EventWeightsIterativeFixMe outputFile='ZpBaryonic_Zp1000_MChi150.root'     
    #EventWeightsIterativeFixMe outputFile='ZpBaryonic_Zp100_MChi1.root'     
    EventWeightsIterativeFixMe outputFile='ZpBaryonic_Zp100_MChi10.root'     
    EventWeightsIterativeFixMe outputFile='ZpBaryonic_Zp10_MChi1.root'     
    EventWeightsIterativeFixMe outputFile='ZpBaryonic_Zp10_MChi10.root'     
    EventWeightsIterativeFixMe outputFile='ZpBaryonic_Zp10_MChi1000.root'     
    #EventWeightsIterativeFixMe outputFile='ZpBaryonic_Zp10_MChi150.root'     
    EventWeightsIterativeFixMe outputFile='ZpBaryonic_Zp10_MChi50.root'     
    EventWeightsIterativeFixMe outputFile='ZpBaryonic_Zp10_MChi500.root'     
    EventWeightsIterativeFixMe outputFile='ZpBaryonic_Zp500_MChi500.root'     
    EventWeightsIterativeFixMe outputFile='ZpBaryonic_Zp500_MChi150.root'   
    #EventWeightsIterativeFixMe outputFile='ZpBaryonic_Zp500_MChi1.root'     
fi

if [ $weightAh -eq 1 ]
then
    echo 'Zprime600A300h.root'
    EventWeightsIterativeFixMe outputFile='Zprime600A300h.root' 
    echo 'Zprime600A400h.root'
    EventWeightsIterativeFixMe outputFile='Zprime600A400h.root' 
    echo 'Zprime800A300h.root'
    EventWeightsIterativeFixMe outputFile='Zprime800A300h.root' 
    echo 'Zprime800A400h.root'
    EventWeightsIterativeFixMe outputFile='Zprime800A400h.root' 
    echo 'Zprime800A500h.root'
    EventWeightsIterativeFixMe outputFile='Zprime800A500h.root' 
    echo 'Zprime800A600h.root'
    EventWeightsIterativeFixMe outputFile='Zprime800A600h.root' 
    echo 'Zprime1000A300h.root'
    EventWeightsIterativeFixMe outputFile='Zprime1000A300h.root' 
    echo 'Zprime1000A400h.root'
    EventWeightsIterativeFixMe outputFile='Zprime1000A400h.root' 
    echo 'Zprime1000A500h.root'
    EventWeightsIterativeFixMe outputFile='Zprime1000A500h.root' 
    echo 'Zprime1000A600h.root'
    EventWeightsIterativeFixMe outputFile='Zprime1000A600h.root' 
    echo 'Zprime1000A700h.root'
    EventWeightsIterativeFixMe outputFile='Zprime1000A700h.root' 
    echo 'Zprime1000A800h.root'
    EventWeightsIterativeFixMe outputFile='Zprime1000A800h.root' 
    echo 'Zprime1200A300h.root'
    EventWeightsIterativeFixMe outputFile='Zprime1200A300h.root' 
    echo 'Zprime1200A400h.root'
    EventWeightsIterativeFixMe outputFile='Zprime1200A400h.root' 
    echo 'Zprime1200A500h.root'
    EventWeightsIterativeFixMe outputFile='Zprime1200A500h.root'
    echo 'Zprime1200A600h.root'
    EventWeightsIterativeFixMe outputFile='Zprime1200A600h.root'
    echo 'Zprime1200A700h.root'
    EventWeightsIterativeFixMe outputFile='Zprime1200A700h.root'
    echo 'Zprime1200A800h.root'
    EventWeightsIterativeFixMe outputFile='Zprime1200A800h.root'
    echo 'Zprime1400A300h.root'
    EventWeightsIterativeFixMe outputFile='Zprime1400A300h.root'
    echo 'Zprime1400A400h.root'
    EventWeightsIterativeFixMe outputFile='Zprime1400A400h.root'
    echo 'Zprime1400A500h.root'
    EventWeightsIterativeFixMe outputFile='Zprime1400A500h.root'
    echo 'Zprime1400A600h.root'
    EventWeightsIterativeFixMe outputFile='Zprime1400A600h.root'
    echo 'Zprime1400A700h.root'
    EventWeightsIterativeFixMe outputFile='Zprime1400A700h.root'
    echo 'Zprime1400A800h.root'
    EventWeightsIterativeFixMe outputFile='Zprime1400A800h.root' 
    echo 'Zprime1700A300h.root'
    EventWeightsIterativeFixMe outputFile='Zprime1700A300h.root' 
    echo 'Zprime1700A400h.root'
    EventWeightsIterativeFixMe outputFile='Zprime1700A400h.root' 
    echo 'Zprime1700A500h.root'
    EventWeightsIterativeFixMe outputFile='Zprime1700A500h.root' 
    echo 'Zprime1700A600h.root'
    EventWeightsIterativeFixMe outputFile='Zprime1700A600h.root' 
    echo 'Zprime1700A700h.root'
    EventWeightsIterativeFixMe outputFile='Zprime1700A700h.root' 
    echo 'Zprime1700A800h.root'
    EventWeightsIterativeFixMe outputFile='Zprime1700A800h.root'  
    echo 'Zprime2000A300h.root'
    EventWeightsIterativeFixMe outputFile='Zprime2000A300h.root'
    echo 'Zprime2000A400h.root'
    EventWeightsIterativeFixMe outputFile='Zprime2000A400h.root'
    echo 'Zprime2000A500h.root'
    EventWeightsIterativeFixMe outputFile='Zprime2000A500h.root' 
    echo 'Zprime2000A600h.root'
    EventWeightsIterativeFixMe outputFile='Zprime2000A600h.root' 
    echo 'Zprime2000A700h.root'
    EventWeightsIterativeFixMe outputFile='Zprime2000A700h.root'
    echo 'Zprime2000A800h.root'
    EventWeightsIterativeFixMe outputFile='Zprime2000A800h.root' 
    echo 'Zprime2500A300h.root'
    EventWeightsIterativeFixMe outputFile='Zprime2500A300h.root'  
    echo 'Zprime2500A400h.root'
    EventWeightsIterativeFixMe outputFile='Zprime2500A400h.root'   
    echo 'Zprime2500A500h.root'
    EventWeightsIterativeFixMe outputFile='Zprime2500A500h.root'    
    echo 'Zprime2500A600h.root'
    EventWeightsIterativeFixMe outputFile='Zprime2500A600h.root'     
    echo 'Zprime2500A700h.root'
    EventWeightsIterativeFixMe outputFile='Zprime2500A700h.root'     
    echo 'Zprime2500A800h.root'
    EventWeightsIterativeFixMe outputFile='Zprime2500A800h.root'     
fi

