#!/bin/sh 

#voms-proxy-init --voms cms --valid 100:00

cat templates/SUB-JSON-BCDEF.py > SUB-JSON-ALL-BCDEF.py
cat templates/all.py >> SUB-JSON-ALL-BCDEF.py

cat templates/SUB-JSON-BCDEF.py > SUB-JSON-MU-BCDEF.py
cat templates/mu.py >> SUB-JSON-MU-BCDEF.py

cat templates/SUB-JSON-BCDEF.py > SUB-JSON-ELE-BCDEF.py
cat templates/ele.py >> SUB-JSON-ELE-BCDEF.py

cat templates/SUB-JSON-BCDEF.py > SUB-JSON-TAU-BCDEF.py
cat templates/tau.py >> SUB-JSON-TAU-BCDEF.py

cat templates/SUB-JSON-ReReco.py > SUB-JSON-ALL-ReReco.py
cat templates/all.py >> SUB-JSON-ALL-ReReco.py

cat templates/SUB-JSON-ReReco.py > SUB-JSON-MU-ReReco.py
cat templates/mu.py >> SUB-JSON-MU-ReReco.py

cat templates/SUB-JSON-ReReco.py > SUB-JSON-ELE-ReReco.py
cat templates/ele.py >> SUB-JSON-ELE-ReReco.py

cat templates/SUB-JSON-ReReco.py > SUB-JSON-TAU-ReReco.py
cat templates/tau.py >> SUB-JSON-TAU-ReReco.py

cat templates/SUB-JSON.py > SUB-JSON-ALL.py
cat templates/all.py >> SUB-JSON-ALL.py

cat templates/SUB-JSON.py > SUB-JSON-MU.py
cat templates/mu.py >> SUB-JSON-MU.py

cat templates/SUB-JSON.py > SUB-JSON-ELE.py
cat templates/ele.py >> SUB-JSON-ELE.py

cat templates/SUB-JSON.py > SUB-JSON-TAU.py
cat templates/tau.py >> SUB-JSON-TAU.py

#bash submitDATA.sh 
bash submitDATA.sh --skip-existing-output
