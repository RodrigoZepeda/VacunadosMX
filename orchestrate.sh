#-----------------------------
#File for downloading info from the vaccine website, creating the database
#and some plots to upload to github
#Author: Rodrigo Zepeda
#Contact: rzepeda17[at]gmail.com
#----------------------------------------
cd /home/rodrigo/VacunadosMX
date=$(date '+%Y-%m-%d')
/home/rodrigo/miniconda3/envs/VacunaDownload/bin/python main.py
/home/rodrigo/miniconda3/envs/VacunaDownload/bin/python plots.py
/home/rodrigo/miniconda3/envs/VacunaDownload/bin/python onedataset.py
git add .
git commit -m "Actualización ${date}"
git push origin main