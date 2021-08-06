#-----------------------------
#File for downloading info from the vaccine website, creating the database
#and some plots to upload to github
#Author: Rodrigo Zepeda
#Contact: rzepeda17[at]gmail.com
#----------------------------------------
date=$(date '+%Y-%m-%d')
python3 main.py
python3 plots.py
python3 onedataset.py
git add .
git commit -m "Se actualizadon datos hasta ${date}"
git push origin main