MonoHTauTau
==========

H->tautau (+ many other) Final States! : )


#Set Up instructions:

```
cmsrel CMSSW_8_0_14 #for 2016 analysis
cd CMSSW_8_0_14/src/
cmsenv
git cms-init 
git clone --recursive -b master https://github.com/lmdodd/MonoHTauTau.git   
cd MonoHTauTau
source recipe13TeV.sh
export USER_CXXFLAGS="-Wno-delete-non-virtual-dtor -Wno-error=unused-but-set-variable -Wno-error=unused-variable -Wno-error=sign-compare -Wno-error=reorder"
scram b -j 8
```
To plot please use https://github.com/lmdodd/StatTools

#Building comments

Critical: Go Through CheckMes and FixMes again. Check Good Vertices.

candidateAuxFunctions brought to MiniAod (Were in TauAnalysis, use again?)

Major Changes/Issues detailed in table

| Kind Of Issue  | Issue Detail |
| ------------- | ------------- |
| Integrate DiTau  | Integrate diTau Branch. Paritally done. di tau can almost be run from 80X_miniAODv2|
| ESscaling | ADD TAU ES |
| no particle embedding yet | TBC |
| TBC | TBC |

In general To see what needs to be fixed ``` grep -r FIXME *``` or ``` CHECKME```.



