# TFM--IVAN-TORREJON-2022-2023
Repositorio con todos los datos utilizados y elaborados para manejar y obtener información de inteligencia de amenazas sobre dispositivos IOT y Smart Home.


Cada uno de los ficheros, desarrollados en draw.io. incluye el esquema en forma de árbol y la relación entre los campos de cada una de las fuentes.
La estructura se basa en nodos, que tienen hijos, padres y nodos hoja, que no tienen hijos. Los nodos cuyo borde tiene una línea discontinua, no tienen un valor único, si no que pueden estar formados por una lista de datos. Los nodos cuyo borde no es discontínuo, tienen un valor único.
Los nodos se organizan por niveles, en el nivel superior están los padres y en el nivel inferior los hijos del nodo en el que nos situemos.
Los nodos cuyo color de fondo concida con el de un nivel superior, son nodos hoja y tienen relación de padre hijo. Esto significa que el campo padre está compuesto y deriva en los nodos hijos. Los hijos no tienen más derivaciones.
Los nodos situados debajo del padre pero cuyo color no coincida con el del padre, tienen a su vez otros nodos hijos, es decir, campos derivados de él. 

- El fichero "ALIENVAULT_def.draw.io" incluye la estructura utilizada para los ficheros obtenidos de Alienvault OTX. Para este caso, todos los campos utilizados por Alienvault, no tienen relación de padre/hijo, no existen derivaciones de campos. Los campos "Labels", "Object_refs" y "Aliases" pueden estar compuestos por listas de valores.
- El fichero "CPES_def" incluye la estructura para los CPEs obtenidos.Los campos "refs" y "titles" pueden contener múltiples valores.
- El fichero "CVES_DEF" incluye la estructura para los CVES obtenidos.
- El fichero "IBM_def" incluye la estructura para los informes y vulnerabilidades obtenidos de IBM XForce Exchange. Los nodos en color azul son campos utilizados exclusivamente para describir vulnerabilidades. El resto se utiliza para describir los objetos de IBM, no específicos de vulnerabilidades.

Para visualizar los esquemas, es necesario acceder a https://app.diagrams.net/ e importar estos esquemas.
