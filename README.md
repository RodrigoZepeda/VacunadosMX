# VacunadosMX
Scrapper para descargar la cantidad de vacunados por estado en México

![](https://github.com/RodrigoZepeda/VacunadosMX/blob/main/images/Dosis_per_capita_actualizados.png)

## Datos
Los datos son descargados de manera diaria de el mapa de http://vacunacovid.gob.mx/wordpress/. La carpeta [raw](https://github.com/RodrigoZepeda/VacunadosMX/tree/main/raw) contiene los html crudos donde se encuentran los datos mientras que [data](https://github.com/RodrigoZepeda/VacunadosMX/tree/main/data) contiene archivos .csv organizados por fecha. 

Los datos para el cálculo per capita vienen del Censo de Población y Vivienda 2020 del [INEGI](https://www.inegi.org.mx/programas/ccpv/2020/#Tabulados). 



## Ejecución
Basta con ejecutar el [main.py](https://github.com/RodrigoZepeda/VacunadosMX/blob/main/main.py) para descargar los datos ese día. La información histórica se guarda en [data](https://github.com/RodrigoZepeda/VacunadosMX/tree/main/data). Como sugerencia procura automatizar la descarga diaria por ejemplo siguiendo estos consejos: https://towardsdatascience.com/how-to-easily-automate-your-python-scripts-on-mac-and-windows-459388c9cc94

## Imágenes
Las imágenes se encuentran en [images](https://github.com/RodrigoZepeda/VacunadosMX/tree/main/images). Son los datos más actuales del repositorio. Para reproducir las gráficas basta con correr [plots.py](https://github.com/RodrigoZepeda/VacunadosMX/blob/main/plots.py)
