# VacunadosMX

> **Nota** A partir del 25 de febrero del 2022 los datos se actualizan diario a las 3:55 de la mañana Ciudad de México.

Scrapper para descargar la cantidad de vacunados por estado en México así como los datos.

![](https://github.com/RodrigoZepeda/VacunadosMX/blob/main/images/Dosis_per_capita_ordenados_recientes.png)


## Datos
Los datos son han sido descargados de manera (semi) diaria de el mapa de http://vacunacovid.gob.mx/wordpress/. La carpeta [raw](https://github.com/RodrigoZepeda/VacunadosMX/tree/main/raw) contiene los html crudos donde se encuentran los datos mientras que [data](https://github.com/RodrigoZepeda/VacunadosMX/tree/main/data) contiene archivos .csv organizados por fecha y [processed](https://github.com/RodrigoZepeda/VacunadosMX/tree/main/data) contiene la base de datos en `.csv` con los días que han tenido observaciones distintas. 

Los datos para el cálculo per capita vienen del Censo de Población y Vivienda 2020 del [INEGI](https://www.inegi.org.mx/programas/ccpv/2020/#Tabulados). 

## Ejecución
Basta con ejecutar el [main.py](https://github.com/RodrigoZepeda/VacunadosMX/blob/main/main.py) para descargar los datos ese día. La información histórica se guarda en [data](https://github.com/RodrigoZepeda/VacunadosMX/tree/main/data). Como sugerencia procura automatizar la descarga diaria por ejemplo siguiendo estos consejos: https://towardsdatascience.com/how-to-easily-automate-your-python-scripts-on-mac-and-windows-459388c9cc94

## Imágenes
Las imágenes se encuentran en [images](https://github.com/RodrigoZepeda/VacunadosMX/tree/main/images). Son los datos más actuales del repositorio. Para reproducir las gráficas basta con correr [plots.py](https://github.com/RodrigoZepeda/VacunadosMX/blob/main/plots.py)

## Querétaro
Querétaro no tuvo datos por mucho tiempo por lo que se reporta como vacío. 
