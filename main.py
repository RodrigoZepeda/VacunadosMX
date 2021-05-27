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
url_js    = 'http://vacunacovid.gob.mx/wordpress'
js_text   = requests.get(url_js, allow_redirects=True).text

#Guardamos el raw
file_js = open(raw_folder + "/" + date.today().strftime('%Y-%m-%d') + ".html","w")
file_js.writelines(str(js_text.encode('utf-8')))
file_js.close()

#Limpiamos el texto para obtener el número de vacunados
vaccine_data = re.sub("(<!--.*?-->)", "", js_text, flags=re.DOTALL)
vaccine_data = re.split(" <svg xmlns:mapsvg=.*?>", vaccine_data)[1]
vaccine_data = re.split("</svg>",vaccine_data, 1)[0]
vaccine_data = vaccine_data.replace("\n","")
vaccine_data = re.split("<path d=.*?",vaccine_data)
re.split('data-title=\".*?\"', vaccine_data[2])[1]
vacunas = []
for i in range(len(vaccine_data)):

    #Get state name
    match_title = re.search('data-title=\".*?\"', vaccine_data[i])
    if match_title:
        title = match_title.group(0).replace("data-title=","").replace("\"","")

    #Get state number
    match_vacunados = re.search('data-vacunados=\".*?\"', vaccine_data[i])
    if match_vacunados:
        vacunados = match_vacunados.group(0).replace("data-vacunados=", "").replace("\"", "").replace(",","")

    if match_title and match_vacunados:
        vacunas.append({"Estado": title, "vacunados": vacunados})
        print(title + ": " + vacunados + " vacunados")


#Parseamos el número de vacunados
dfvacunas = pd.DataFrame.from_dict(vacunas)
dfvacunas['vacunados'] = pd.to_numeric(dfvacunas['vacunados'])
dfvacunas['descarga']  = datetime.now().strftime("%d-%b-%Y (%H:%M:%S)")

#Guardamos
dfvacunas.to_csv(download_folder + "/" + download_name, index = False)

print("Datos descargados en " + download_folder + "/" + download_name)
