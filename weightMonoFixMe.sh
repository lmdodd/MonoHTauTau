#!/bin/sh

#mkdir /nfs_scratch/$USER/monohiggs_weighted
#cp /nfs_scratch/$USER/monohiggs_unweighted/* /nfs_scratch/$USER/monohiggs_weighted/.
cd /nfs_scratch/$USER/monohiggs_2/

weight=1;
weightBaryonic=1;
weightAh=1;



if [ $weight -eq 1 ]
then
    nohup EventWeightsIterativeFakeTauPt  outputFile='EWK.root' &
    nohup EventWeightsIterativeFakeTauPt  outputFile='smH125.root' &
    nohup EventWeightsIterativeFakeTauPt  outputFile='WJETSHT.root' &
    nohup EventWeightsIterativeFakeTauPt  outputFile='ZJETS.root' &
    nohup EventWeightsIterativeFakeTauPt  outputFile='TT.root' &
    nohup EventWeightsIterativeFakeTauPt  outputFile='Znunu.root' &
    nohup EventWeightsIterativeFakeTauPt  outputFile='DiBoson.root' &
fi


if [ $weightBaryonic -eq 1 ]
then
    EventWeightsIterativeFakeTauPt outputFile='ZpBaryonic_Zp10000_MChi1.root'     
    EventWeightsIterativeFakeTauPt outputFile='ZpBaryonic_Zp10000_MChi10.root'     
    EventWeightsIterativeFakeTauPt outputFile='ZpBaryonic_Zp10000_MChi1000.root'     
    EventWeightsIterativeFakeTauPt outputFile='ZpBaryonic_Zp10000_MChi150.root'     
    EventWeightsIterativeFakeTauPt outputFile='ZpBaryonic_Zp10000_MChi50.root'     
    EventWeightsIterativeFakeTauPt outputFile='ZpBaryonic_Zp10000_MChi500.root'     
    EventWeightsIterativeFakeTauPt outputFile='ZpBaryonic_Zp1000_MChi1.root'     
    EventWeightsIterativeFakeTauPt outputFile='ZpBaryonic_Zp1000_MChi1000.root'     
    EventWeightsIterativeFakeTauPt outputFile='ZpBaryonic_Zp1000_MChi150.root'     
    EventWeightsIterativeFakeTauPt outputFile='ZpBaryonic_Zp100_MChi1.root'     
    EventWeightsIterativeFakeTauPt outputFile='ZpBaryonic_Zp100_MChi10.root'     
    EventWeightsIterativeFakeTauPt outputFile='ZpBaryonic_Zp10_MChi1.root'     
    EventWeightsIterativeFakeTauPt outputFile='ZpBaryonic_Zp10_MChi10.root'     
    EventWeightsIterativeFakeTauPt outputFile='ZpBaryonic_Zp10_MChi1000.root'     
    EventWeightsIterativeFakeTauPt outputFile='ZpBaryonic_Zp10_MChi150.root'     
    EventWeightsIterativeFakeTauPt outputFile='ZpBaryonic_Zp10_MChi50.root'     
    EventWeightsIterativeFakeTauPt outputFile='ZpBaryonic_Zp10_MChi500.root'     
    EventWeightsIterativeFakeTauPt outputFile='ZpBaryonic_Zp500_MChi500.root'     
    EventWeightsIterativeFakeTauPt outputFile='ZpBaryonic_Zp500_MChi150.root'   
    #EventWeightsIterativeFakeTauPt outputFile='ZpBaryonic_Zp500_MChi1.root'     
fi

if [ $weightAh -eq 1 ]
then
    echo 'Zprime600A300h.root'
    EventWeightsIterativeFakeTauPt outputFile='Zprime600A300h.root' 
    echo 'Zprime600A400h.root'
    EventWeightsIterativeFakeTauPt outputFile='Zprime600A400h.root' 
    echo 'Zprime800A300h.root'
    EventWeightsIterativeFakeTauPt outputFile='Zprime800A300h.root' 
    echo 'Zprime800A400h.root'
    EventWeightsIterativeFakeTauPt outputFile='Zprime800A400h.root' 
    echo 'Zprime800A500h.root'
    EventWeightsIterativeFakeTauPt outputFile='Zprime800A500h.root' 
    echo 'Zprime800A600h.root'
    EventWeightsIterativeFakeTauPt outputFile='Zprime800A600h.root' 
    echo 'Zprime1000A300h.root'
    EventWeightsIterativeFakeTauPt outputFile='Zprime1000A300h.root' 
    echo 'Zprime1000A400h.root'
    EventWeightsIterativeFakeTauPt outputFile='Zprime1000A400h.root' 
    echo 'Zprime1000A500h.root'
    EventWeightsIterativeFakeTauPt outputFile='Zprime1000A500h.root' 
    echo 'Zprime1000A600h.root'
    EventWeightsIterativeFakeTauPt outputFile='Zprime1000A600h.root' 
    echo 'Zprime1000A700h.root'
    EventWeightsIterativeFakeTauPt outputFile='Zprime1000A700h.root' 
    echo 'Zprime1000A800h.root'
    EventWeightsIterativeFakeTauPt outputFile='Zprime1000A800h.root' 
    echo 'Zprime1200A300h.root'
    EventWeightsIterativeFakeTauPt outputFile='Zprime1200A300h.root' 
    echo 'Zprime1200A400h.root'
    EventWeightsIterativeFakeTauPt outputFile='Zprime1200A400h.root' 
    echo 'Zprime1200A500h.root'
    EventWeightsIterativeFakeTauPt outputFile='Zprime1200A500h.root'
    echo 'Zprime1200A600h.root'
    EventWeightsIterativeFakeTauPt outputFile='Zprime1200A600h.root'
    echo 'Zprime1200A700h.root'
    EventWeightsIterativeFakeTauPt outputFile='Zprime1200A700h.root'
    echo 'Zprime1200A800h.root'
    EventWeightsIterativeFakeTauPt outputFile='Zprime1200A800h.root'
    echo 'Zprime1400A300h.root'
    EventWeightsIterativeFakeTauPt outputFile='Zprime1400A300h.root'
    echo 'Zprime1400A400h.root'
    EventWeightsIterativeFakeTauPt outputFile='Zprime1400A400h.root'
    echo 'Zprime1400A500h.root'
    EventWeightsIterativeFakeTauPt outputFile='Zprime1400A500h.root'
    echo 'Zprime1400A600h.root'
    EventWeightsIterativeFakeTauPt outputFile='Zprime1400A600h.root'
    echo 'Zprime1400A700h.root'
    EventWeightsIterativeFakeTauPt outputFile='Zprime1400A700h.root'
    echo 'Zprime1400A800h.root'
    EventWeightsIterativeFakeTauPt outputFile='Zprime1400A800h.root' 
    echo 'Zprime1700A300h.root'
    EventWeightsIterativeFakeTauPt outputFile='Zprime1700A300h.root' 
    echo 'Zprime1700A400h.root'
    EventWeightsIterativeFakeTauPt outputFile='Zprime1700A400h.root' 
    echo 'Zprime1700A500h.root'
    EventWeightsIterativeFakeTauPt outputFile='Zprime1700A500h.root' 
    echo 'Zprime1700A600h.root'
    EventWeightsIterativeFakeTauPt outputFile='Zprime1700A600h.root' 
    echo 'Zprime1700A700h.root'
    EventWeightsIterativeFakeTauPt outputFile='Zprime1700A700h.root' 
    echo 'Zprime1700A800h.root'
    EventWeightsIterativeFakeTauPt outputFile='Zprime1700A800h.root'  
    echo 'Zprime2000A300h.root'
    EventWeightsIterativeFakeTauPt outputFile='Zprime2000A300h.root'
    echo 'Zprime2000A400h.root'
    EventWeightsIterativeFakeTauPt outputFile='Zprime2000A400h.root'
    echo 'Zprime2000A500h.root'
    EventWeightsIterativeFakeTauPt outputFile='Zprime2000A500h.root' 
    echo 'Zprime2000A600h.root'
    EventWeightsIterativeFakeTauPt outputFile='Zprime2000A600h.root' 
    echo 'Zprime2000A700h.root'
    EventWeightsIterativeFakeTauPt outputFile='Zprime2000A700h.root'
    echo 'Zprime2000A800h.root'
    EventWeightsIterativeFakeTauPt outputFile='Zprime2000A800h.root' 
    echo 'Zprime2500A300h.root'
    EventWeightsIterativeFakeTauPt outputFile='Zprime2500A300h.root'  
    echo 'Zprime2500A400h.root'
    EventWeightsIterativeFakeTauPt outputFile='Zprime2500A400h.root'   
    echo 'Zprime2500A500h.root'
    EventWeightsIterativeFakeTauPt outputFile='Zprime2500A500h.root'    
    echo 'Zprime2500A600h.root'
    EventWeightsIterativeFakeTauPt outputFile='Zprime2500A600h.root'     
    echo 'Zprime2500A700h.root'
    EventWeightsIterativeFakeTauPt outputFile='Zprime2500A700h.root'     
    echo 'Zprime2500A800h.root'
    EventWeightsIterativeFakeTauPt outputFile='Zprime2500A800h.root'     
fi

