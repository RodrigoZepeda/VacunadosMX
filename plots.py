import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import pandas as pd
import os

sns.set(style="darkgrid")

#---------------------------------------------
#            GRÁFICA DE TOTALES
#---------------------------------------------

#Obtenemos el archivo más reciente
#https://stackoverflow.com/questions/58881381/using-python-to-identify-and-load-last-csv-file-in-directory-by-updated-time
path = "data/"
csvs = [x for x in os.listdir(path) if  x.endswith(".csv")]
most_recent = max(csvs, key=lambda x: os.stat(os.path.join(path, x)).st_mtime)

#Lectura del archivo
vacunas           = pd.read_csv(path + most_recent)
vacunas           = vacunas.sort_values('Estado')

#Imagen
g           = sns.catplot(data=vacunas, kind="bar", x="Estado", y="vacunados", height=6, aspect=2)
loc, labels = plt.xticks()
g.set_xticklabels(labels, rotation=90)
g.set(title = "Github: RodrigoZepeda/VacunasMX | Fuente: Página del gobierno: http://vacunacovid.gob.mx/wordpress/", ylabel='Vacunas aplicadas', xlabel='Entidad')
for ax in g.axes.flat:
    ax.yaxis.set_major_formatter(ticker.StrMethodFormatter('{x:,.0f}'))
plt.suptitle('Total de vacunas aplicadas por entidad federativa en México')
plt.tight_layout()
plt.savefig('images/Vacunados_actualizados.png', dpi = 750)

#---------------------------------------------
#            GRÁFICA PER CÁPITA
#---------------------------------------------
#Datos del INEGI. Fuente CENSO 2020. https://www.inegi.org.mx/programas/ccpv/2020/#Tabulados

#Lectura del archivo
individuos = pd.read_csv("inegi/INEGI_Exporta_20210528154428.csv", encoding='latin1')
edades     = individuos.columns[2:20]

#Limpiamos las commas
for col in edades:
    individuos[col] = individuos[col].str.replace(",", "").astype(int)

#Sumamos las edades de interés
individuos["Population"] = individuos[edades].sum(axis = 1)

#Cambio de los nombres para homologar
individuos.loc[individuos["Estado"] == "Veracruz de Ignacio de la Llave", ["Estado"]] = "Veracruz"
individuos.loc[individuos["Estado"] == "Michoacán de Ocampo", ["Estado"]] = "Michoacán"
individuos.loc[individuos["Estado"] == "Ciudad de México", ["Estado"]] = "CDMX"
individuos.loc[individuos["Estado"] == "Coahuila de Zaragoza", ["Estado"]] = "Coahuila"
individuos.loc[individuos["Estado"] == "México", ["Estado"]] = "Estado de México"

#Juntamos ambas bases
dosis_per_capita = pd.merge(vacunas, individuos, on = "Estado")
dosis_per_capita["Dosis_per_capita"] = dosis_per_capita["vacunados"] / dosis_per_capita["Population"]

#Imagen
g = sns.catplot(data=dosis_per_capita, kind="bar", x="Estado", y="Dosis_per_capita", height=6, aspect=2)
loc, labels = plt.xticks()
g.set(title = "Github: RodrigoZepeda/VacunasMX | Fuente: INEGI Censo 2020 y Página del gobierno: http://vacunacovid.gob.mx/wordpress/",
      ylabel='Vacunas per capita', xlabel='Entidad')
g.set_xticklabels(labels, rotation=90)
plt.suptitle('Total de vacunas aplicadas per capita por entidad federativa en México')
plt.tight_layout()
plt.savefig('images/Dosis_per_capita_actualizados.png', dpi = 750)
