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
/usr/bin/git -C /home/rodrigo/VacunadosMX add .
/usr/bin/git -C /home/rodrigo/VacunadosMX commit -m "Actualización ${date}"
/usr/bin/git -C /home/rodrigo/VacunadosMX push origin main