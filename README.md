# TFM--IVAN-TORREJON-2022-2023
Repositorio con todos los datos utilizados y elaborados para manejar y obtener información de inteligencia de amenazas sobre dispositivos IOT y Smart Home.

La rama "FICHEROS-PYTHON" almacena todos los ficheros desarrollados en Python para este proyecto, subdividiéndolos en carpetas según su función.

En la carpeta "JSON A EXCEL/", se encuentran los 14  ficheros en python desarrollados para convertir los datos obtenidos en formato JSON de cada una de las plataformas a un excel donde se unifiquen los datos de cada plataforma según el término de búsqueda "IOT" o "Smart Home". Cada fila del excel recoge un JSON obtenido .
Cada uno de los archivos python está nombrado con la fuente a la que pertenece y el sufijo para conocer si pertenece a la búsqueda del término "IOT" o "Smart Home". Por ejemplo "alienvault_smart_home.py", es el fichero en python generado para estructurar y pasar todos los datos de los JSON obtenidos de Alienvault OTX para la búsqueda "Smart Home" a un Excel donde se recojan todos estos datos de forma unificada, donde cada fila recoge cada uno de los JSON obtenidos.

En la carpeta "ANÁLISIS CAMPOS INDIVIDUALES/" se encuentran los ficheros Python en carpetas, nombradas según la fuente analizada, en los que se estudian los detalles del análisis de campos de forma individual para obtener resultado de estos análisis. En el archivo 
"README.md" dentro de la carpeta "ANÁLISIS CAMPOS INDIVIDUALES/" se encuentra más información sobre estos ficheros.

En la carpeta "ANÁLISIS RELACIÓN COLUMNAS/" se encuentran los ficheros Python clasfiicados en carpetas, nombradas según la fuente analizada, en los que se estudian los detalles del análisis de relación entre campos de cada una de las fuentes, para obtener resultado de estos análisis. En el archivo  "README.md" dentro de la carpeta "ANÁLISIS RELACIÓN COLUMNAS/" se encuentra más información sobre estos ficheros.

En la carpeta "ANÁLISIS RELACIÓN FUENTES/" se encuentran los ficheros Python nombrados según los campos analizados, en los que se estudian las relaciones de campos entre distintas fuentes, para obtener resultado de estos análisis. Todos estos archivos están comentados, lo que permite entender cómo se realizó el código.

Los ficheros "ibm_grupo_amenazas" e "ibm_sector" no contienen en su nombre "IOT" O "Smart Home" debido a que la búsqueda para los dos términos devuelve los mismos resultados.
