# TFM--IVAN-TORREJON-2022-2023
Repositorio con todos los datos utilizados y elaborados para manejar y obtener información de inteligencia de amenazas sobre dispositivos IOT y Smart Home.

La rama "FICHEROS-PYTHON" almacena todos los ficheros desarrollados en Python para este proyecto, subdividiéndolos en carpetas según su función.

En la carpeta "JSON A EXCEL", se encuentran los 14  ficheros en python desarrollados para convertir los datos obtenidos en formato JSON de cada una de las plataformas a un excel donde se unifiquen los datos de cada plataforma según el término de búsqueda "IOT" o "Smart Home". Cada fila del excel recoge un JSON obtenido .
Cada uno de los archivos python está nombrado con la fuente a la que pertenece y el sufijo para conocer si pertenece a la búsqueda del término "IOT" o "Smart Home". Por ejemplo "alienvault_smart_home.py", es el fichero en python generado para estructurar y pasar todos los datos de los JSON obtenidos de Alienvault OTX para la búsqueda "Smart Home" a un Excel donde se recojan todos estos datos de forma unificada, donde cada fila recoge cada uno de los JSON obtenidos.

Los ficheros "ibm_grupo_amenazas" e "ibm_sector" no contienen en su nombre "IOT" O "Smart Home" debido a que la búsqueda para los dos términos devuelve los mismos resultados.
