MonoHTauTau
==========

H->tautau (+ many other) Final States! : )


#Set Up instructions:

```
cmsrel CMSSW_8_0_26_patch1 #for 2016 analysis
cd CMSSW_8_0_26_patch1/src/
cmsenv
git cms-init 
git clone --recursive -b master https://github.com/lmdodd/MonoHTauTau.git   
cd MonoHTauTau
source recipe13TeV.sh
export USER_CXXFLAGS="-Wno-delete-non-virtual-dtor -Wno-error=unused-but-set-variable -Wno-error=unused-variable -Wno-error=sign-compare -Wno-error=reorder"
scram b -j 8
```

To test 

```
cd MonoHTauTau
cmsRun LT-MC.py
```


To plot please use https://github.com/lmdodd/StatTools

#Building comments
Major Changes/Issues detailed in table

| Kind Of Issue  | Issue Detail |
| ------------- | ------------- |
| Integrate DiTau  | Integrate diTau Branch. Paritally done |
| ESscaling | ADD TAU ES |
| METShapes | ADD MET SHAPE |
| TBC | TBC |

In general To see what needs to be fixed ``` grep -r FIXME *``` or ``` CHECKME```.



