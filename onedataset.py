import pandas as pd
import glob
import os
from datetime import date
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

sns.set_theme(style="ticks")

#---------------------------------------------
#            DATOS DE VACUNAS
#---------------------------------------------

#Import datasets
path = r'data' # use your path
all_files = glob.glob(os.path.join(path, "*.csv"))

#Join datasets in unique dataframe
df = pd.concat((pd.read_csv(f) for f in all_files), ignore_index=True)

#Obtain difference in values
df["descarga"] = pd.to_datetime(df["descarga"], format="%d-%b-%Y (%H:%M:%S)")
df             = df.sort_values("descarga", ascending=True, na_position = "last")
df['diff']     = df.groupby(['Estado'])['vacunados'].diff().fillna(0)

#Get the initial values
df_initial     = df[df["descarga"] == min(df["descarga"])]
df_last        = df[df["descarga"] == max(df["descarga"])]

#Get the subsequent values that haven't changed
unique_downloads = pd.unique(df[df["diff"] != 0]["descarga"])
df_subsequent    = df[df["descarga"].isin(unique_downloads)]

df_final = pd.concat([df_initial, df_subsequent],  ignore_index=True)
df_final = df_final.sort_values("descarga", ascending=True, na_position = "last")

#---------------------------------------------
#            DATOS DE POBLACIÓN INEGI
#---------------------------------------------

#Lectura del archivo
individuos = pd.read_csv("inegi/INEGI_Exporta_20210528154428.csv", encoding='latin1')
edades     = individuos.columns[2:20]

#Limpiamos las commas
for col in edades:
    individuos[col] = individuos[col].str.replace(",", "").astype(int)

#Sumamos las edades de interés
individuos["Poblacion_INEGI"] = individuos[edades].sum(axis = 1)

#Cambio de los nombres para homologar
individuos.loc[individuos["Estado"] == "Veracruz de Ignacio de la Llave", ["Estado"]] = "Veracruz"
individuos.loc[individuos["Estado"] == "Michoacán de Ocampo", ["Estado"]] = "Michoacán"
individuos.loc[individuos["Estado"] == "Ciudad de México", ["Estado"]] = "CDMX"
individuos.loc[individuos["Estado"] == "Coahuila de Zaragoza", ["Estado"]] = "Coahuila"
individuos.loc[individuos["Estado"] == "México", ["Estado"]] = "Estado de México"
individuos = individuos[["Estado","Poblacion_INEGI"]]

#Juntamos ambas bases
dosis_per_capita = pd.merge(df_final, individuos, on = "Estado")
dosis_per_capita["dosis_per_capita"] = dosis_per_capita["vacunados"] / dosis_per_capita["Poblacion_INEGI"]

#Renombrar columna vacunados por dosis
dosis_per_capita.rename(columns={'vacunados':'dosis'}, inplace=True)
dosis_per_capita = dosis_per_capita.drop(columns=['diff'])
dosis_per_capita = dosis_per_capita.sort_values(by = ["descarga","Estado"], ascending=True, na_position = "last")

#Guardar en csv
download_name           = "Vacunados-" + date.today().strftime('%Y-%m-%d') + ".csv"
dosis_per_capita["Dia"] = dosis_per_capita.descarga.dt.date
dosis_per_capita.to_csv(os.path.join("processed", download_name), index = False)
