import pandas as pd
import requests
import re
from datetime import datetime
from datetime import date

download_name   = "Vacunados MX por estado  " + date.today().strftime('%Y-%m-%d') + ".csv"
download_folder = "data"
raw_folder      = "raw"

print("Descargando datos estatales")

#Descarga del javascript donde están los datos
url_js    = 'http://vacunacovid.gob.mx/wordpress/wp-content/themes/vacunamx/custom/js/home.js'
js_text   = requests.get(url_js, allow_redirects=True).text

#Guardamos el raw
file_js = open(raw_folder + "/home " + date.today().strftime('%Y-%m-%d') + ".js","w")
file_js.writelines(js_text)
file_js.close()

#Limpiamos el texto para obtener el número de vacunados
vaccine_data = re.split("let vacunas_data", js_text)[1]
vaccine_data = re.split(";", vaccine_data, 1)[0]
vaccine_data = vaccine_data.replace("\n","")
vaccine_data = vaccine_data.replace(" ","")
vaccine_data = "vacunas_data" + vaccine_data

#Creamos la variable de vaccine data
exec(vaccine_data)

#Parseamos el número de vacunados
dfvacunas = pd.DataFrame.from_dict(vacunas_data)
dfvacunas['vacunados'] = dfvacunas['vacunados'].str.replace(r',', '').astype(int)
dfvacunas['descarga']  = datetime.now().strftime("%d-%b-%Y (%H:%M:%S)")

#Guardamos
dfvacunas.to_csv(download_folder + "/" + download_name, index = False)

print("Datos descargados en " + download_folder + "/" + download_name)
