import pandas as pd
from datetime import datetime

#Abro los ficheros con los que voy a tratar


df_alienvault_iot = pd.read_excel('alienvault_iot_2023.xlsx')





#Variables donde almacenare EL TIPO DE OBJETO dado un anio de publicacion especifico
count_published_date_2023_alienvault_iot_typereport=0
count_published_date_2023_alienvault_iot_typeindicator=0
count_published_date_2023_alienvault_iot_typeidentity=0
count_published_date_2023_alienvault_iot_typevulnerability=0
#Variable donde almaceno el anio de publicacion de un OBJETO
count_published_date_2023_alienvault_iot=0

count_published_date_2022_alienvault_iot_typereport=0
count_published_date_2022_alienvault_iot_typeindicator=0
count_published_date_2022_alienvault_iot_typeidentity=0
count_published_date_2022_alienvault_iot_typevulnerability=0
count_published_date_2022_alienvault_iot=0


count_published_date_2021_alienvault_iot_typereport=0
count_published_date_2021_alienvault_iot_typeindicator=0
count_published_date_2021_alienvault_iot_typeidentity=0
count_published_date_2021_alienvault_iot_typevulnerability=0
count_published_date_2021_alienvault_iot=0


count_published_date_2020_alienvault_iot_typereport=0
count_published_date_2020_alienvault_iot_typeindicator=0
count_published_date_2020_alienvault_iot_typeidentity=0
count_published_date_2020_alienvault_iot_typevulnerability=0
count_published_date_2020_alienvault_iot=0


count_published_date_2019_alienvault_iot_typereport=0
count_published_date_2019_alienvault_iot_typeindicator=0
count_published_date_2019_alienvault_iot_typeidentity=0
count_published_date_2019_alienvault_iot_typevulnerability=0
count_published_date_2019_alienvault_iot=0


count_published_date_2018_alienvault_iot_typereport=0
count_published_date_2018_alienvault_iot_typeindicator=0
count_published_date_2018_alienvault_iot_typeidentity=0
count_published_date_2018_alienvault_iot_typevulnerability=0
count_published_date_2018_alienvault_iot=0

#Variables para almacenar el contador total de tipo de OBJETO
count_alienvault_iot_typereport=0
count_alienvault_iot_typeindicator=0
count_alienvault_iot_typeidentity=0
count_alienvault_iot_typevulnerability=0

#Variable para almacenar el contador total de OBJETOS consultados
count_alienvault_iot_total=0
#Variable para almacenar el contador total de fechas de publicacion para las que EL TIPO DE OBJETO está definido
count_alienvault_iot_totalpulses=0


#Comprobamos el anio de PUBLICACION 
for r in range(0,len(df_alienvault_iot["published"])):
    #Si existe varios anios de publicacion en una misma fila
    if('[' in df_alienvault_iot["published"][r]):
        #Obtenemos los distintos anios de publicacion
        aux=df_alienvault_iot["published"][r].split(",")
        #Recorremos los valores
        for l in range(0,len(aux)):
            if(len(aux)>0):
                #Obtengo el valor actual de fecha de publicacion
                aux_str=aux[l].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
                if(aux_str!='NONE'):
                    count_alienvault_iot_total+=1
                    #Obtengo el anio de creacion
                    str_anio_publishdate_alienvault_iot=aux_str.split("-")
                    anio_publishdate_alienvault_iot=int(str_anio_publishdate_alienvault_iot[0])
                    if(anio_publishdate_alienvault_iot >= 2023):
                        count_published_date_2023_alienvault_iot+=1
                        #Obtengo los valores de tipo de OBJETO
                        auxx=df_alienvault_iot["type"][r].split(",")
                        auxx_str=auxx[l].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
                        #Compruebo EL TIPO DE OBJETO
                        if(auxx_str == 'report'):
                            count_alienvault_iot_totalpulses+=1
                            count_alienvault_iot_typereport+=1
                            count_published_date_2023_alienvault_iot_typereport+=1
                        elif(auxx_str == 'indicator'):
                            count_alienvault_iot_totalpulses+=1
                            count_alienvault_iot_typeindicator+=1
                            count_published_date_2023_alienvault_iot_typeindicator+=1
                        elif(auxx_str == 'identity'):
                            count_alienvault_iot_totalpulses+=1
                            count_alienvault_iot_typeidentity+=1
                            count_published_date_2023_alienvault_iot_typeidentity+=1 
                        elif(auxx_str == 'vulnerability'):
                            count_alienvault_iot_totalpulses+=1
                            count_alienvault_iot_typevulnerability+=1
                            count_published_date_2023_alienvault_iot_typevulnerability+=1
                                 
                                
                    elif(anio_publishdate_alienvault_iot >= 2022):
                        count_published_date_2022_alienvault_iot+=1
                        auxx=df_alienvault_iot["type"][r].split(",")
                        auxx_str=auxx[l].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
                        if(auxx_str == 'report'):
                            count_alienvault_iot_totalpulses+=1
                            count_alienvault_iot_typereport+=1
                            count_published_date_2022_alienvault_iot_typereport+=1
                        elif(auxx_str == 'indicator'):
                            count_alienvault_iot_totalpulses+=1
                            count_alienvault_iot_typeindicator+=1
                            count_published_date_2022_alienvault_iot_typeindicator+=1
                        elif(auxx_str == 'identity'):
                            count_alienvault_iot_totalpulses+=1
                            count_alienvault_iot_typeidentity+=1
                            count_published_date_2022_alienvault_iot_typeidentity+=1 
                        elif(auxx_str == 'vulnerability'):
                            count_alienvault_iot_totalpulses+=1
                            count_alienvault_iot_typevulnerability+=1
                            count_published_date_2022_alienvault_iot_typevulnerability+=1
                                
                    elif(anio_publishdate_alienvault_iot >= 2021):
                        count_published_date_2021_alienvault_iot+=1
                        auxx=df_alienvault_iot["type"][r].split(",")
                        auxx_str=auxx[l].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
                        if(auxx_str == 'report'):
                            count_alienvault_iot_totalpulses+=1
                            count_alienvault_iot_typereport+=1
                            count_published_date_2021_alienvault_iot_typereport+=1
                        elif(auxx_str == 'indicator'):
                            count_alienvault_iot_totalpulses+=1
                            count_alienvault_iot_typeindicator+=1
                            count_published_date_2021_alienvault_iot_typeindicator+=1
                        elif(auxx_str == 'identity'):
                            count_alienvault_iot_totalpulses+=1
                            count_alienvault_iot_typeidentity+=1
                            count_published_date_2021_alienvault_iot_typeidentity+=1
                        elif(auxx_str == 'vulnerability'):
                            count_alienvault_iot_totalpulses+=1
                            count_alienvault_iot_typevulnerability+=1
                            count_published_date_2021_alienvault_iot_typevulnerability+=1
                                
                    elif(anio_publishdate_alienvault_iot >= 2020):
                        count_published_date_2020_alienvault_iot+=1
                        auxx=df_alienvault_iot["type"][r].split(",")
                        auxx_str=auxx[l].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
                        if(auxx_str == 'report'):
                            count_alienvault_iot_totalpulses+=1
                            count_alienvault_iot_typereport+=1
                            count_published_date_2020_alienvault_iot_typereport+=1
                        elif(auxx_str == 'indicator'):
                            count_alienvault_iot_totalpulses+=1
                            count_alienvault_iot_typeindicator+=1
                            count_published_date_2020_alienvault_iot_typeindicator+=1
                        elif(auxx_str == 'identity'):
                            count_alienvault_iot_totalpulses+=1
                            count_alienvault_iot_typeidentity+=1
                            count_published_date_2020_alienvault_iot_typeidentity+=1 
                        elif(auxx_str == 'vulnerability'):
                            count_alienvault_iot_totalpulses+=1
                            count_alienvault_iot_typevulnerability+=1
                            count_published_date_2020_alienvault_iot_typevulnerability+=1
                                
                                
                    elif(anio_publishdate_alienvault_iot >= 2019):
                        count_published_date_2019_alienvault_iot+=1
                        auxx=df_alienvault_iot["type"][r].split(",")
                        auxx_str=auxx[l].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
                        if(auxx_str == 'report'):
                            count_alienvault_iot_totalpulses+=1
                            count_alienvault_iot_typereport+=1
                            count_published_date_2019_alienvault_iot_typereport+=1
                        elif(auxx_str == 'indicator'):
                            count_alienvault_iot_totalpulses+=1
                            count_alienvault_iot_typeindicator+=1
                            count_published_date_2019_alienvault_iot_typeindicator+=1
                        elif(auxx_str == 'identity'):
                            count_alienvault_iot_totalpulses+=1
                            count_alienvault_iot_typeidentity+=1
                            count_published_date_2019_alienvault_iot_typeidentity+=1
                        elif(auxx_str == 'vulnerability'):
                            count_alienvault_iot_totalpulses+=1
                            count_alienvault_iot_typevulnerability+=1
                            count_published_date_2019_alienvault_iot_typevulnerability+=1
                                
                                
                    else: 
                        count_published_date_2018_alienvault_iot+=1
                        auxx=df_alienvault_iot["type"][r].split(",")
                        auxx_str=auxx[l].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
                        if(auxx_str == 'report'):
                            count_alienvault_iot_totalpulses+=1
                            count_alienvault_iot_typereport+=1
                            count_published_date_2018_alienvault_iot_typereport+=1
                        elif(auxx_str == 'indicator'):
                            count_alienvault_iot_totalpulses+=1
                            count_alienvault_iot_typeindicator+=1
                            count_published_date_2018_alienvault_iot_typeindicator+=1
                        elif(auxx_str == 'identity'):
                            count_alienvault_iot_totalpulses+=1
                            count_alienvault_iot_typeidentity+=1
                            count_published_date_2018_alienvault_iot_typeidentity+=1
                        elif(auxx_str == 'vulnerability'):
                            count_alienvault_iot_totalpulses+=1
                            count_alienvault_iot_typevulnerability+=1
                            count_published_date_2018_alienvault_iot_typevulnerability+=1
    else:
        #Si existe un unico valor de fecha de publicacion en la fila actual
        str_anio_publishdate_alienvault_iot=df_alienvault_iot["published"][r].split("-")
        #Obtengo el anio de creacion
        anio_publishdate_alienvault_iot=int(str_anio_publishdate_alienvault_iot[0])
        count_alienvault_iot_total+=1
        #Obtengo los valores de tipo para la fila actual
        auxx=df_alienvault_iot["type"][r].split(",")
        
        for l in range(0,len(auxx)):
            if(len(auxx)>0):
                auxx_str=auxx[l].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
                if(auxx_str!='NONE'):
                    count_alienvault_iot_totalpulses+=1
                    #Compruebo el anio de creacion
                    if(anio_publishdate_alienvault_iot >= 2023):
                        count_published_date_2023_alienvault_iot+=1
                        #Compruebo EL TIPO DE OBJETO
                        if(auxx_str == 'report'):
                            count_alienvault_iot_typereport+=1
                            count_published_date_2023_alienvault_iot_typereport+=1  
                        elif(auxx_str == 'indicator'):
                            count_alienvault_iot_typeindicator+=1
                            count_published_date_2023_alienvault_iot_typeindicator+=1  
                        elif(auxx_str == 'identity'):
                            count_alienvault_iot_typeidentity+=1
                            count_published_date_2023_alienvault_iot_typeidentity+=1
                        elif(auxx_str == 'vulnerability'):
                            count_alienvault_iot_typevulnerability+=1
                            count_published_date_2023_alienvault_iot_typevulnerability+=1

                    elif(anio_publishdate_alienvault_iot >= 2022):
                        count_published_date_2022_alienvault_iot+=1
                        if(auxx_str == 'report'):
                            count_alienvault_iot_typereport+=1
                            count_published_date_2022_alienvault_iot_typereport+=1  
                        elif(auxx_str == 'indicator'):
                            count_alienvault_iot_typeindicator+=1
                            count_published_date_2022_alienvault_iot_typeindicator+=1  
                        elif(auxx_str == 'identity'):
                            count_alienvault_iot_typeidentity+=1
                            count_published_date_2022_alienvault_iot_typeidentity+=1
                        elif(auxx_str == 'vulnerability'):
                            count_alienvault_iot_typevulnerability+=1
                            count_published_date_2022_alienvault_iot_typevulnerability+=1
                    elif(anio_publishdate_alienvault_iot >= 2021):
                        count_published_date_2021_alienvault_iot+=1
                        if(auxx_str == 'report'):
                            count_alienvault_iot_typereport+=1
                            count_published_date_2021_alienvault_iot_typereport+=1  
                        elif(auxx_str == 'indicator'):
                            count_alienvault_iot_typeindicator+=1
                            count_published_date_2021_alienvault_iot_typeindicator+=1  
                        elif(auxx_str == 'identity'):
                            count_alienvault_iot_typeidentity+=1
                            count_published_date_2021_alienvault_iot_typeidentity+=1
                        elif(auxx_str == 'vulnerability'):
                            count_alienvault_iot_typevulnerability+=1
                            count_published_date_2021_alienvault_iot_typevulnerability+=1
                    elif(anio_publishdate_alienvault_iot >= 2020):
                        count_published_date_2020_alienvault_iot+=1
                        if(auxx_str == 'report'):
                            count_alienvault_iot_typereport+=1
                            count_published_date_2020_alienvault_iot_typereport+=1  
                        elif(auxx_str == 'indicator'):
                            count_alienvault_iot_typeindicator+=1
                            count_published_date_2020_alienvault_iot_typeindicator+=1  
                        elif(auxx_str == 'identity'):
                            count_alienvault_iot_typeidentity+=1
                            count_published_date_2020_alienvault_iot_typeidentity+=1
                        elif(auxx_str == 'vulnerability'):
                            count_alienvault_iot_typevulnerability+=1
                            count_published_date_2020_alienvault_iot_typevulnerability+=1
                    elif(anio_publishdate_alienvault_iot >= 2019):
                        count_published_date_2019_alienvault_iot+=1
                        if(auxx_str == 'report'):
                            count_alienvault_iot_typereport+=1
                            count_published_date_2019_alienvault_iot_typereport+=1  
                        elif(auxx_str == 'indicator'):
                            count_alienvault_iot_typeindicator+=1
                            count_published_date_2019_alienvault_iot_typeindicator+=1  
                        elif(auxx_str == 'identity'):
                            count_alienvault_iot_typeidentity+=1
                            count_published_date_2019_alienvault_iot_typeidentity+=1
                        elif(auxx_str == 'vulnerability'):
                            count_alienvault_iot_typevulnerability+=1
                            count_published_date_2019_alienvault_iot_typevulnerability+=1
                    else:
                        count_published_date_2018_alienvault_iot+=1
                        if(auxx_str == 'report'):
                            count_alienvault_iot_typereport+=1
                            count_published_date_2018_alienvault_iot_typereport+=1  
                        elif(auxx_str == 'indicator'):
                            count_alienvault_iot_typeindicator+=1
                            count_published_date_2018_alienvault_iot_typeindicator+=1  
                        elif(auxx_str == 'identity'):
                            count_alienvault_iot_typeidentity+=1
                            count_published_date_2018_alienvault_iot_typeidentity+=1
                        elif(auxx_str == 'vulnerability'):
                            count_alienvault_iot_typevulnerability+=1
                            count_published_date_2018_alienvault_iot_typevulnerability+=1
                
                
print("**************ESTADÍSTICAS TIPO DE OBJETO/FECHA DE PUBLICACIÓN ALIENVAULT PARTE IOT**************")
print("\n")                            
                
print("\n")
print(" DE UN TOTAL DE "+str(count_alienvault_iot_totalpulses)+" OBJETOS :\n") 
print("\n")
print("   - LAS ESTADISTICAS DE FECHA DE PUBLICACION SON LAS SIGUIENTES:  \n")
print("      -    EN  "+str(count_published_date_2023_alienvault_iot)+" OBJETOS LA FECHA DE PUBLICACION ES 2023. LAS ESTADÍSTICAS DE TIPO DE OBJETO SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(count_published_date_2023_alienvault_iot_typereport)+" OBJETOS PUBLICADOS EN 2023, EL TIPO ES REPORTE ")
print("            -    EN  "+str(count_published_date_2023_alienvault_iot_typeindicator)+" OBJETOS PUBLICADOS EN 2023, EL TIPO ES INDICADOR")
print("            -    EN  "+str(count_published_date_2023_alienvault_iot_typeidentity)+" OBJETOS PUBLICADOS EN 2023, EL TIPO ES IDENTIDAD ")
print("            -    EN  "+str(count_published_date_2023_alienvault_iot_typeidentity)+" OBJETOS PUBLICADOS EN 2023, EL TIPO ES VULNERABILIDAD ")
print("\n")
print("      -    EN  "+str(count_published_date_2022_alienvault_iot)+" OBJETOS LA FECHA DE PUBLICACION ES 2022. LAS ESTADÍSTICAS DE TIPO DE OBJETO SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(count_published_date_2022_alienvault_iot_typereport)+" OBJETOS PUBLICADOS EN 2022, EL TIPO ES REPORTE ")
print("            -    EN  "+str(count_published_date_2022_alienvault_iot_typeindicator)+" OBJETOS PUBLICADOS EN 2022, EL TIPO ES INDICADOR")
print("            -    EN  "+str(count_published_date_2022_alienvault_iot_typeidentity)+" OBJETOS PUBLICADOS EN 2022, EL TIPO ES IDENTIDAD ")
print("            -    EN  "+str(count_published_date_2022_alienvault_iot_typeidentity)+" OBJETOS PUBLICADOS EN 2022, EL TIPO ES VULNERABILIDAD ")
print("\n")
print("      -    EN  "+str(count_published_date_2021_alienvault_iot)+" OBJETOS LA FECHA DE PUBLICACION ES 2021. LAS ESTADÍSTICAS DE TIPO DE OBJETO SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(count_published_date_2021_alienvault_iot_typereport)+" OBJETOS PUBLICADOS EN 2021, EL TIPO ES REPORTE ")
print("            -    EN  "+str(count_published_date_2021_alienvault_iot_typeindicator)+" OBJETOS PUBLICADOS EN 2021, EL TIPO ES INDICADOR")
print("            -    EN  "+str(count_published_date_2021_alienvault_iot_typeidentity)+" OBJETOS PUBLICADOS EN 2021, EL TIPO ES IDENTIDAD ")
print("            -    EN  "+str(count_published_date_2021_alienvault_iot_typeidentity)+" OBJETOS PUBLICADOS EN 2021, EL TIPO ES VULNERABILIDAD ")
print("\n")
print("      -    EN  "+str(count_published_date_2020_alienvault_iot)+" OBJETOS LA FECHA DE PUBLICACION ES 2020. LAS ESTADÍSTICAS DE TIPO DE OBJETO SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(count_published_date_2020_alienvault_iot_typereport)+" OBJETOS PUBLICADOS EN 2020, EL TIPO ES REPORTE ")
print("            -    EN  "+str(count_published_date_2020_alienvault_iot_typeindicator)+" OBJETOS PUBLICADOS EN 2020, EL TIPO ES INDICADOR")
print("            -    EN  "+str(count_published_date_2020_alienvault_iot_typeidentity)+" OBJETOS PUBLICADOS EN 2020, EL TIPO ES IDENTIDAD ")
print("            -    EN  "+str(count_published_date_2020_alienvault_iot_typeidentity)+" OBJETOS PUBLICADOS EN 2020, EL TIPO ES VULNERABILIDAD ")
print("\n")
print("      -    EN  "+str(count_published_date_2019_alienvault_iot)+" OBJETOS LA FECHA DE PUBLICACION ES 2019. LAS ESTADÍSTICAS DE TIPO DE OBJETO SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(count_published_date_2019_alienvault_iot_typereport)+" OBJETOS PUBLICADOS EN 2019, EL TIPO ES REPORTE ")
print("            -    EN  "+str(count_published_date_2019_alienvault_iot_typeindicator)+" OBJETOS PUBLICADOS EN 2019, EL TIPO ES INDICADOR")
print("            -    EN  "+str(count_published_date_2019_alienvault_iot_typeidentity)+" OBJETOS PUBLICADOS EN 2019, EL TIPO ES IDENTIDAD ")
print("            -    EN  "+str(count_published_date_2019_alienvault_iot_typeidentity)+" OBJETOS PUBLICADOS EN 2019, EL TIPO ES VULNERABILIDAD ")
print("\n")
print("      -    EN  "+str(count_published_date_2018_alienvault_iot)+" OBJETOS LA FECHA DE PUBLICACION ES 2018 O ANTERIOR. LAS ESTADÍSTICAS DE TIPO DE OBJETO SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(count_published_date_2018_alienvault_iot_typereport)+" OBJETOS PUBLICADOS EN 2018 O ANTES, EL TIPO ES REPORTE ")
print("            -    EN  "+str(count_published_date_2018_alienvault_iot_typeindicator)+" OBJETOS PUBLICADOS EN 2018 O ANTES, EL TIPO ES INDICADOR")
print("            -    EN  "+str(count_published_date_2018_alienvault_iot_typeidentity)+" OBJETOS PUBLICADOS EN 2018 O ANTES, EL TIPO ES IDENTIDAD ")
print("            -    EN  "+str(count_published_date_2018_alienvault_iot_typeidentity)+" OBJETOS PUBLICADOS EN 2018, EL TIPO ES VULNERABILIDAD ")
print("\n")
print("   - LAS ESTADISTICAS DE TIPO DE OBJETO SON LAS SIGUIENTES:  \n")
print("      -    EN  "+str(count_alienvault_iot_typereport)+" OBJETOS EL TIPO DE OBJETO ES REPORTE. LAS ESTADÍSTICAS DE FECHA DE PUBLICACION SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(count_published_date_2023_alienvault_iot_typereport)+" OBJETOS LA FECHA DE PUBLICACION ES 2023 ")
print("            -    EN  "+str(count_published_date_2022_alienvault_iot_typereport)+" OBJETOS LA FECHA DE PUBLICACION ES 2022")
print("            -    EN  "+str(count_published_date_2021_alienvault_iot_typereport)+" OBJETOS LA FECHA DE PUBLICACION ES 2021 ")
print("            -    EN  "+str(count_published_date_2020_alienvault_iot_typereport)+" OBJETOS LA FECHA DE PUBLICACION ES 2020 ")
print("            -    EN  "+str(count_published_date_2019_alienvault_iot_typereport)+" OBJETOS LA FECHA DE PUBLICACION ES 2019")
print("            -    EN  "+str(count_published_date_2018_alienvault_iot_typereport)+" OBJETOS LA FECHA DE PUBLICACION ES 2018 O ANTERIOR ")
print("\n")
print("      -    EN  "+str(count_alienvault_iot_typeindicator)+" OBJETOS EL TIPO DE OBJETO ES INDICADOR. LAS ESTADÍSTICAS DE FECHA DE PUBLICACION SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(count_published_date_2023_alienvault_iot_typeindicator)+" OBJETOS LA FECHA DE PUBLICACION ES 2023 ")
print("            -    EN  "+str(count_published_date_2022_alienvault_iot_typeindicator)+" OBJETOS LA FECHA DE PUBLICACION ES 2022")
print("            -    EN  "+str(count_published_date_2021_alienvault_iot_typeindicator)+" OBJETOS LA FECHA DE PUBLICACION ES 2021 ")
print("            -    EN  "+str(count_published_date_2020_alienvault_iot_typeindicator)+" OBJETOS LA FECHA DE PUBLICACION ES 2020 ")
print("            -    EN  "+str(count_published_date_2019_alienvault_iot_typeindicator)+" OBJETOS LA FECHA DE PUBLICACION ES 2019")
print("            -    EN  "+str(count_published_date_2018_alienvault_iot_typeindicator)+" OBJETOS LA FECHA DE PUBLICACION ES 2018 O ANTERIOR ")
print("\n")
print("      -    EN  "+str(count_alienvault_iot_typeidentity)+" OBJETOS EL TIPO DE OBJETO ES IDENTIDAD. LAS ESTADÍSTICAS DE FECHA DE PUBLICACION SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(count_published_date_2023_alienvault_iot_typeidentity)+" OBJETOS LA FECHA DE PUBLICACION ES 2023 ")
print("            -    EN  "+str(count_published_date_2022_alienvault_iot_typeidentity)+" OBJETOS LA FECHA DE PUBLICACION ES 2022")
print("            -    EN  "+str(count_published_date_2021_alienvault_iot_typeidentity)+" OBJETOS LA FECHA DE PUBLICACION ES 2021 ")
print("            -    EN  "+str(count_published_date_2020_alienvault_iot_typeidentity)+" OBJETOS LA FECHA DE PUBLICACION ES 2020 ")
print("            -    EN  "+str(count_published_date_2019_alienvault_iot_typeidentity)+" OBJETOS LA FECHA DE PUBLICACION ES 2019")
print("            -    EN  "+str(count_published_date_2018_alienvault_iot_typeidentity)+" OBJETOS LA FECHA DE PUBLICACION ES 2018 O ANTERIOR ")
print("\n")
print("      -    EN  "+str(count_alienvault_iot_typevulnerability)+" OBJETOS EL TIPO DE OBJETO ES VULNERABILIDAD. LAS ESTADÍSTICAS DE FECHA DE PUBLICACION SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(count_published_date_2023_alienvault_iot_typevulnerability)+" OBJETOS LA FECHA DE PUBLICACION ES 2023 ")
print("            -    EN  "+str(count_published_date_2022_alienvault_iot_typevulnerability)+" OBJETOS LA FECHA DE PUBLICACION ES 2022")
print("            -    EN  "+str(count_published_date_2021_alienvault_iot_typevulnerability)+" OBJETOS LA FECHA DE PUBLICACION ES 2021 ")
print("            -    EN  "+str(count_published_date_2020_alienvault_iot_typevulnerability)+" OBJETOS LA FECHA DE PUBLICACION ES 2020 ")
print("            -    EN  "+str(count_published_date_2019_alienvault_iot_typevulnerability)+" OBJETOS LA FECHA DE PUBLICACION ES 2019")
print("            -    EN  "+str(count_published_date_2018_alienvault_iot_typevulnerability)+" OBJETOS LA FECHA DE PUBLICACION ES 2018 O ANTERIOR ")
print("\n")








print("**************PORCENTAJE TIPO DE OBJETO/FECHA DE PUBLICACIÓN ALIENVAULT PARTE IOT**************")
print("\n")                            
                
print("\n")
print(" DE UN TOTAL DE "+str(count_alienvault_iot_totalpulses)+" OBJETOS :\n") 
print("\n")
print("   - LOS PORCENTAJES DE FECHA DE PUBLICACION SON LOS SIGUIENTES:  \n")
if(count_published_date_2023_alienvault_iot>0):
    print("      -    EN EL  "+str(float(((count_published_date_2023_alienvault_iot*100)/count_alienvault_iot_totalpulses)))+" % DE OBJETOS LA FECHA DE PUBLICACION ES 2023. LOS PORCENTAJES DE TIPO DE OBJETO SON LOS SIGUIENTES:  \n")
    print("\n")
    print("            -    EN EL  "+str(float(((count_published_date_2023_alienvault_iot_typereport*100)/count_published_date_2023_alienvault_iot)))+" % DE OBJETOS PUBLICADOS EN 2023, EL TIPO ES REPORTE ")
    print("            -    EN EL  "+str(float(((count_published_date_2023_alienvault_iot_typeindicator*100)/count_published_date_2023_alienvault_iot)))+" % DE OBJETOS PUBLICADOS EN 2023, EL TIPO ES INDICADOR")
    print("            -    EN EL  "+str(float(((count_published_date_2023_alienvault_iot_typeidentity*100)/count_published_date_2023_alienvault_iot)))+" % DE OBJETOS PUBLICADOS EN 2023, EL TIPO ES IDENTIDAD ")
    print("            -    EN EL  "+str(float(((count_published_date_2023_alienvault_iot_typevulnerability*100)/count_published_date_2023_alienvault_iot)))+" % DE OBJETOS PUBLICADOS EN 2023, EL TIPO ES VULNERABILIDAD ")
    print("\n")
if(count_published_date_2022_alienvault_iot>0):
    print("      -    EN EL  "+str(float(((count_published_date_2022_alienvault_iot*100)/count_alienvault_iot_totalpulses)))+" % DE OBJETOS LA FECHA DE PUBLICACION ES 2022. LOS PORCENTAJESS DE TIPO DE OBJETO SON LOS SIGUIENTES:  \n")
    print("\n")
    print("            -    EN EL  "+str(float(((count_published_date_2022_alienvault_iot_typereport*100)/count_published_date_2022_alienvault_iot)))+" % DE OBJETOS PUBLICADOS EN 2022, EL TIPO ES REPORTE ")
    print("            -    EN EL  "+str(float(((count_published_date_2022_alienvault_iot_typeindicator*100)/count_published_date_2022_alienvault_iot)))+" % DE OBJETOS PUBLICADOS EN 2022, EL TIPO ES INDICADOR")
    print("            -    EN EL  "+str(float(((count_published_date_2022_alienvault_iot_typeidentity*100)/count_published_date_2022_alienvault_iot)))+" % DE OBJETOS PUBLICADOS EN 2022, EL TIPO ES IDENTIDAD ")
    print("            -    EN EL  "+str(float(((count_published_date_2022_alienvault_iot_typevulnerability*100)/count_published_date_2022_alienvault_iot)))+" % DE OBJETOS PUBLICADOS EN 2022, EL TIPO ES VULNERABILIDAD ")
    print("\n")
if(count_published_date_2021_alienvault_iot>0):
    print("      -    EN EL  "+str(float(((count_published_date_2021_alienvault_iot*100)/count_alienvault_iot_totalpulses)))+" % DE OBJETOS LA FECHA DE PUBLICACION ES 2021. LOS PORCENTAJES DE TIPO DE OBJETO SON LOS SIGUIENTES:  \n")
    print("\n")
    print("            -    EN EL  "+str(float(((count_published_date_2021_alienvault_iot_typereport*100)/count_published_date_2021_alienvault_iot)))+" % DE OBJETOS PUBLICADOS EN 2021, EL TIPO ES REPORTE ")
    print("            -    EN EL  "+str(float(((count_published_date_2021_alienvault_iot_typeindicator*100)/count_published_date_2021_alienvault_iot)))+" % DE OBJETOS PUBLICADOS EN 2021, EL TIPO ES INDICADOR")
    print("            -    EN EL  "+str(float(((count_published_date_2021_alienvault_iot_typeidentity*100)/count_published_date_2021_alienvault_iot)))+" % DE OBJETOS PUBLICADOS EN 2021, EL TIPO ES IDENTIDAD ")
    print("            -    EN EL  "+str(float(((count_published_date_2021_alienvault_iot_typevulnerability*100)/count_published_date_2021_alienvault_iot)))+" % DE OBJETOS PUBLICADOS EN 2021, EL TIPO ES VULNERABILIDAD ")
    print("\n")
if(count_published_date_2020_alienvault_iot>0):
    print("      -    EN EL  "+str(float(((count_published_date_2020_alienvault_iot*100)/count_alienvault_iot_totalpulses)))+" % DE OBJETOS LA FECHA DE PUBLICACION ES 2020. LOS PORCENTAJES DE TIPO DE OBJETO SON LOS SIGUIENTES:  \n")
    print("\n")
    print("            -    EN EL  "+str(float(((count_published_date_2020_alienvault_iot_typereport*100)/count_published_date_2020_alienvault_iot)))+" % DE OBJETOS PUBLICADOS EN 2020, EL TIPO ES REPORTE ")
    print("            -    EN EL  "+str(float(((count_published_date_2020_alienvault_iot_typeindicator*100)/count_published_date_2020_alienvault_iot)))+" % DE OBJETOS PUBLICADOS EN 2020, EL TIPO ES INDICADOR")
    print("            -    EN EL  "+str(float(((count_published_date_2020_alienvault_iot_typeidentity*100)/count_published_date_2020_alienvault_iot)))+" % DE OBJETOS PUBLICADOS EN 2020, EL TIPO ES IDENTIDAD ")
    print("            -    EN EL  "+str(float(((count_published_date_2020_alienvault_iot_typevulnerability*100)/count_published_date_2020_alienvault_iot)))+" % DE OBJETOS PUBLICADOS EN 2020, EL TIPO ES VULNERABILIDAD ")
    print("\n")
if(count_published_date_2019_alienvault_iot>0):
    print("      -    EN EL  "+str(float(((count_published_date_2019_alienvault_iot*100)/count_alienvault_iot_totalpulses)))+" % DE OBJETOS LA FECHA DE PUBLICACION ES 2019. LOS PORCENTAJES DE TIPO DE OBJETO SON LOS SIGUIENTES:  \n")
    print("\n")
    print("            -    EN EL  "+str(float(((count_published_date_2019_alienvault_iot_typereport*100)/count_published_date_2019_alienvault_iot)))+" % DE OBJETOS PUBLICADOS EN 2019, EL TIPO ES REPORTE ")
    print("            -    EN EL  "+str(float(((count_published_date_2019_alienvault_iot_typeindicator*100)/count_published_date_2019_alienvault_iot)))+" % DE OBJETOS PUBLICADOS EN 2019, EL TIPO ES INDICADOR")
    print("            -    EN EL  "+str(float(((count_published_date_2019_alienvault_iot_typeidentity*100)/count_published_date_2019_alienvault_iot)))+" % DE OBJETOS PUBLICADOS EN 2019, EL TIPO ES IDENTIDAD ")
    print("            -    EN EL  "+str(float(((count_published_date_2019_alienvault_iot_typevulnerability*100)/count_published_date_2019_alienvault_iot)))+" % DE OBJETOS PUBLICADOS EN 2019, EL TIPO ES VULNERABILIDAD ")
    print("\n")
if(count_published_date_2018_alienvault_iot>0):
    print("      -    EN EL  "+str(float(((count_published_date_2018_alienvault_iot*100)/count_alienvault_iot_totalpulses)))+" % DE OBJETOS LA FECHA DE PUBLICACION ES 2018 O ANTERIOR. LOS PORCENTAJES DE TIPO DE OBJETO SON LOS SIGUIENTES:  \n")
    print("\n")
    print("            -    EN EL  "+str(float(((count_published_date_2018_alienvault_iot_typereport*100)/count_published_date_2018_alienvault_iot)))+" % DE OBJETOS PUBLICADOS EN 2018 O ANTERIORMENTE, EL TIPO ES REPORTE ")
    print("            -    EN EL  "+str(float(((count_published_date_2018_alienvault_iot_typeindicator*100)/count_published_date_2018_alienvault_iot)))+" % DE OBJETOS PUBLICADOS EN 2018 O ANTERIORMENTE, EL TIPO ES INDICADOR")
    print("            -    EN EL  "+str(float(((count_published_date_2018_alienvault_iot_typeidentity*100)/count_published_date_2018_alienvault_iot)))+" % DE OBJETOS PUBLICADOS EN 2018 O ANTERIORMENTE, EL TIPO ES IDENTIDAD ")
    print("            -    EN EL  "+str(float(((count_published_date_2018_alienvault_iot_typevulnerability*100)/count_published_date_2018_alienvault_iot)))+" % DE OBJETOS PUBLICADOS EN 2018, EL TIPO ES VULNERABILIDAD ")
    print("\n")
print("   - LOS PORCENTAJES DE TIPO DE OBJETO SON LOS SIGUIENTES:  \n")
if(count_alienvault_iot_typereport>0):
    print("      -    EN EL  "+str(float(((count_alienvault_iot_typereport*100)/count_alienvault_iot_totalpulses)))+" % DE OBJETOS EL TIPO DE OBJETO ES REPORTE. LOS PORCENTAJES DE FECHA DE PUBLICACION SON LOS SIGUIENTES:  \n")
    print("\n")
    print("            -    EN EL  "+str(float(((count_published_date_2023_alienvault_iot_typereport*100)/count_alienvault_iot_typereport)))+" % DE OBJETOS LA FECHA DE PUBLICACION ES 2023 ")
    print("            -    EN EL  "+str(float(((count_published_date_2022_alienvault_iot_typereport*100)/count_alienvault_iot_typereport)))+" % DE OBJETOS LA FECHA DE PUBLICACION ES 2022")
    print("            -    EN EL  "+str(float(((count_published_date_2021_alienvault_iot_typereport*100)/count_alienvault_iot_typereport)))+" % DE OBJETOS LA FECHA DE PUBLICACION ES 2021 ")
    print("            -    EN EL  "+str(float(((count_published_date_2020_alienvault_iot_typereport*100)/count_alienvault_iot_typereport)))+" % DE OBJETOS LA FECHA DE PUBLICACION ES 2020 ")
    print("            -    EN EL  "+str(float(((count_published_date_2019_alienvault_iot_typereport*100)/count_alienvault_iot_typereport)))+" % DE OBJETOS LA FECHA DE PUBLICACION ES 2019")
    print("            -    EN EL  "+str(float(((count_published_date_2018_alienvault_iot_typereport*100)/count_alienvault_iot_typereport)))+" % DE OBJETOS LA FECHA DE PUBLICACION ES 2018 O ANTERIOR ")
    print("\n")
if(count_alienvault_iot_typeindicator>0):
    print("      -    EN EL  "+str(float(((count_alienvault_iot_typeindicator*100)/count_alienvault_iot_totalpulses)))+" % DE OBJETOS EL TIPO DE OBJETO ES INDICADOR. LOS PORCENTAJES DE FECHA DE PUBLICACION SON LOS SIGUIENTES:  \n")
    print("\n")
    print("            -    EN EL  "+str(float(((count_published_date_2023_alienvault_iot_typeindicator*100)/count_alienvault_iot_typeindicator)))+" % DE OBJETOS LA FECHA DE PUBLICACION ES 2023 ")
    print("            -    EN EL  "+str(float(((count_published_date_2022_alienvault_iot_typeindicator*100)/count_alienvault_iot_typeindicator)))+" % DE OBJETOS LA FECHA DE PUBLICACION ES 2022")
    print("            -    EN EL  "+str(float(((count_published_date_2021_alienvault_iot_typeindicator*100)/count_alienvault_iot_typeindicator)))+" % DE OBJETOS LA FECHA DE PUBLICACION ES 2021 ")
    print("            -    EN EL  "+str(float(((count_published_date_2020_alienvault_iot_typeindicator*100)/count_alienvault_iot_typeindicator)))+" % DE OBJETOS LA FECHA DE PUBLICACION ES 2020 ")
    print("            -    EN EL  "+str(float(((count_published_date_2019_alienvault_iot_typeindicator*100)/count_alienvault_iot_typeindicator)))+" % DE OBJETOS LA FECHA DE PUBLICACION ES 2019")
    print("            -    EN EL  "+str(float(((count_published_date_2018_alienvault_iot_typeindicator*100)/count_alienvault_iot_typeindicator)))+" % DE OBJETOS LA FECHA DE PUBLICACION ES 2018 O ANTERIOR ")
    print("\n")
if(count_alienvault_iot_typeidentity>0):
    print("      -    EN EL  "+str(float(((count_alienvault_iot_typeidentity*100)/count_alienvault_iot_totalpulses)))+" % DE OBJETOS EL TIPO DE OBJETO ES IDENTIDAD. LOS PORCENTAJES DE FECHA DE PUBLICACION SON LOS SIGUIENTES:  \n")
    print("\n")
    print("            -    EN EL  "+str(float(((count_published_date_2023_alienvault_iot_typeidentity*100)/count_alienvault_iot_typeidentity)))+" % DE OBJETOS LA FECHA DE PUBLICACION ES 2023 ")
    print("            -    EN EL  "+str(float(((count_published_date_2022_alienvault_iot_typeidentity*100)/count_alienvault_iot_typeidentity)))+" % DE OBJETOS LA FECHA DE PUBLICACION ES 2022")
    print("            -    EN EL  "+str(float(((count_published_date_2021_alienvault_iot_typeidentity*100)/count_alienvault_iot_typeidentity)))+" % DE OBJETOS LA FECHA DE PUBLICACION ES 2021 ")
    print("            -    EN EL  "+str(float(((count_published_date_2020_alienvault_iot_typeidentity*100)/count_alienvault_iot_typeidentity)))+" % DE OBJETOS LA FECHA DE PUBLICACION ES 2020 ")
    print("            -    EN EL  "+str(float(((count_published_date_2019_alienvault_iot_typeidentity*100)/count_alienvault_iot_typeidentity)))+" % DE OBJETOS LA FECHA DE PUBLICACION ES 2019")
    print("            -    EN EL  "+str(float(((count_published_date_2018_alienvault_iot_typeidentity*100)/count_alienvault_iot_typeidentity)))+" % DE OBJETOS LA FECHA DE PUBLICACION ES 2018 O ANTERIOR ")
    print("\n")
if(count_alienvault_iot_typevulnerability>0):
    print("      -    EN EL  "+str(float(((count_alienvault_iot_typevulnerability*100)/count_alienvault_iot_totalpulses)))+" % DE OBJETOS EL TIPO DE OBJETO ES VULNERABILIDAD. LOS PORCENTAJES DE FECHA DE PUBLICACION SON LOS SIGUIENTES:  \n")
    print("\n")
    print("            -    EN EL  "+str(float(((count_published_date_2023_alienvault_iot_typevulnerability*100)/count_alienvault_iot_typevulnerability)))+" % DE OBJETOS LA FECHA DE PUBLICACION ES 2023 ")
    print("            -    EN EL  "+str(float(((count_published_date_2022_alienvault_iot_typevulnerability*100)/count_alienvault_iot_typevulnerability)))+" % DE OBJETOS LA FECHA DE PUBLICACION ES 2022")
    print("            -    EN EL  "+str(float(((count_published_date_2021_alienvault_iot_typevulnerability*100)/count_alienvault_iot_typevulnerability)))+" % DE OBJETOS LA FECHA DE PUBLICACION ES 2021 ")
    print("            -    EN EL  "+str(float(((count_published_date_2020_alienvault_iot_typevulnerability*100)/count_alienvault_iot_typevulnerability)))+" % DE OBJETOS LA FECHA DE PUBLICACION ES 2020 ")
    print("            -    EN EL  "+str(float(((count_published_date_2019_alienvault_iot_typevulnerability*100)/count_alienvault_iot_typevulnerability)))+" % DE OBJETOS LA FECHA DE PUBLICACION ES 2019")
    print("            -    EN EL  "+str(float(((count_published_date_2018_alienvault_iot_typevulnerability*100)/count_alienvault_iot_typevulnerability)))+" % DE OBJETOS LA FECHA DE PUBLICACION ES 2018 O ANTERIOR ")
    print("\n")


    
    
    
    
    
    
    
    
    
    
    
    
    
    
import pandas as pd
from datetime import datetime

#Abro los ficheros con los que voy a tratar


df_alienvault_sh = pd.read_excel('alienvault_smart_home_2023.xlsx')





#Variables donde almacenare EL TIPO DE OBJETO dado un anio de publicacion especifico
count_published_date_2023_alienvault_sh_typereport=0
count_published_date_2023_alienvault_sh_typeindicator=0
count_published_date_2023_alienvault_sh_typeidentity=0
count_published_date_2023_alienvault_sh_typevulnerability=0
#Variable donde almaceno el anio de publicacion de un OBJETO
count_published_date_2023_alienvault_sh=0

count_published_date_2022_alienvault_sh_typereport=0
count_published_date_2022_alienvault_sh_typeindicator=0
count_published_date_2022_alienvault_sh_typeidentity=0
count_published_date_2022_alienvault_sh_typevulnerability=0
count_published_date_2022_alienvault_sh=0


count_published_date_2021_alienvault_sh_typereport=0
count_published_date_2021_alienvault_sh_typeindicator=0
count_published_date_2021_alienvault_sh_typeidentity=0
count_published_date_2021_alienvault_sh_typevulnerability=0
count_published_date_2021_alienvault_sh=0


count_published_date_2020_alienvault_sh_typereport=0
count_published_date_2020_alienvault_sh_typeindicator=0
count_published_date_2020_alienvault_sh_typeidentity=0
count_published_date_2020_alienvault_sh_typevulnerability=0
count_published_date_2020_alienvault_sh=0


count_published_date_2019_alienvault_sh_typereport=0
count_published_date_2019_alienvault_sh_typeindicator=0
count_published_date_2019_alienvault_sh_typeidentity=0
count_published_date_2019_alienvault_sh_typevulnerability=0
count_published_date_2019_alienvault_sh=0


count_published_date_2018_alienvault_sh_typereport=0
count_published_date_2018_alienvault_sh_typeindicator=0
count_published_date_2018_alienvault_sh_typeidentity=0
count_published_date_2018_alienvault_sh_typevulnerability=0
count_published_date_2018_alienvault_sh=0

#Variables para almacenar el contador total de tipo de OBJETO
count_alienvault_sh_typereport=0
count_alienvault_sh_typeindicator=0
count_alienvault_sh_typeidentity=0
count_alienvault_sh_typevulnerability=0

#Variable para almacenar el contador total de OBJETOS consultados
count_alienvault_sh_total=0
#Variable para almacenar el contador total de fechas de publicacion para las que EL TIPO DE OBJETO está definido
count_alienvault_sh_totalpulses=0


#Comprobamos el anio de PUBLICACION 
for r in range(0,len(df_alienvault_sh["published"])):
    #Si existe varios anios de publicacion en una misma fila
    if('[' in df_alienvault_sh["published"][r]):
        #Obtenemos los distintos anios de publicacion
        aux=df_alienvault_sh["published"][r].split(",")
        #Recorremos los valores
        for l in range(0,len(aux)):
            if(len(aux)>0):
                #Obtengo el valor actual de fecha de publicacion
                aux_str=aux[l].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
                if(aux_str!='NONE'):
                    count_alienvault_sh_total+=1
                    #Obtengo el anio de creacion
                    str_anio_publishdate_alienvault_sh=aux_str.split("-")
                    anio_publishdate_alienvault_sh=int(str_anio_publishdate_alienvault_sh[0])
                    if(anio_publishdate_alienvault_sh >= 2023):
                        count_published_date_2023_alienvault_sh+=1
                        #Obtengo los valores de tipo de OBJETO
                        auxx=df_alienvault_sh["type"][r].split(",")
                        auxx_str=auxx[l].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
                        #Compruebo EL TIPO DE OBJETO
                        if(auxx_str == 'report'):
                            count_alienvault_sh_totalpulses+=1
                            count_alienvault_sh_typereport+=1
                            count_published_date_2023_alienvault_sh_typereport+=1
                        elif(auxx_str == 'indicator'):
                            count_alienvault_sh_totalpulses+=1
                            count_alienvault_sh_typeindicator+=1
                            count_published_date_2023_alienvault_sh_typeindicator+=1
                        elif(auxx_str == 'identity'):
                            count_alienvault_sh_totalpulses+=1
                            count_alienvault_sh_typeidentity+=1
                            count_published_date_2023_alienvault_sh_typeidentity+=1 
                        elif(auxx_str == 'vulnerability'):
                            count_alienvault_sh_totalpulses+=1
                            count_alienvault_sh_typevulnerability+=1
                            count_published_date_2023_alienvault_sh_typevulnerability+=1
                                 
                                
                    elif(anio_publishdate_alienvault_sh >= 2022):
                        count_published_date_2022_alienvault_sh+=1
                        auxx=df_alienvault_sh["type"][r].split(",")
                        auxx_str=auxx[l].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
                        if(auxx_str == 'report'):
                            count_alienvault_sh_totalpulses+=1
                            count_alienvault_sh_typereport+=1
                            count_published_date_2022_alienvault_sh_typereport+=1
                        elif(auxx_str == 'indicator'):
                            count_alienvault_sh_totalpulses+=1
                            count_alienvault_sh_typeindicator+=1
                            count_published_date_2022_alienvault_sh_typeindicator+=1
                        elif(auxx_str == 'identity'):
                            count_alienvault_sh_totalpulses+=1
                            count_alienvault_sh_typeidentity+=1
                            count_published_date_2022_alienvault_sh_typeidentity+=1 
                        elif(auxx_str == 'vulnerability'):
                            count_alienvault_sh_totalpulses+=1
                            count_alienvault_sh_typevulnerability+=1
                            count_published_date_2022_alienvault_sh_typevulnerability+=1
                                
                    elif(anio_publishdate_alienvault_sh >= 2021):
                        count_published_date_2021_alienvault_sh+=1
                        auxx=df_alienvault_sh["type"][r].split(",")
                        auxx_str=auxx[l].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
                        if(auxx_str == 'report'):
                            count_alienvault_sh_totalpulses+=1
                            count_alienvault_sh_typereport+=1
                            count_published_date_2021_alienvault_sh_typereport+=1
                        elif(auxx_str == 'indicator'):
                            count_alienvault_sh_totalpulses+=1
                            count_alienvault_sh_typeindicator+=1
                            count_published_date_2021_alienvault_sh_typeindicator+=1
                        elif(auxx_str == 'identity'):
                            count_alienvault_sh_totalpulses+=1
                            count_alienvault_sh_typeidentity+=1
                            count_published_date_2021_alienvault_sh_typeidentity+=1
                        elif(auxx_str == 'vulnerability'):
                            count_alienvault_sh_totalpulses+=1
                            count_alienvault_sh_typevulnerability+=1
                            count_published_date_2021_alienvault_sh_typevulnerability+=1
                                
                    elif(anio_publishdate_alienvault_sh >= 2020):
                        count_published_date_2020_alienvault_sh+=1
                        auxx=df_alienvault_sh["type"][r].split(",")
                        auxx_str=auxx[l].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
                        if(auxx_str == 'report'):
                            count_alienvault_sh_totalpulses+=1
                            count_alienvault_sh_typereport+=1
                            count_published_date_2020_alienvault_sh_typereport+=1
                        elif(auxx_str == 'indicator'):
                            count_alienvault_sh_totalpulses+=1
                            count_alienvault_sh_typeindicator+=1
                            count_published_date_2020_alienvault_sh_typeindicator+=1
                        elif(auxx_str == 'identity'):
                            count_alienvault_sh_totalpulses+=1
                            count_alienvault_sh_typeidentity+=1
                            count_published_date_2020_alienvault_sh_typeidentity+=1 
                        elif(auxx_str == 'vulnerability'):
                            count_alienvault_sh_totalpulses+=1
                            count_alienvault_sh_typevulnerability+=1
                            count_published_date_2020_alienvault_sh_typevulnerability+=1
                                
                                
                    elif(anio_publishdate_alienvault_sh >= 2019):
                        count_published_date_2019_alienvault_sh+=1
                        auxx=df_alienvault_sh["type"][r].split(",")
                        auxx_str=auxx[l].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
                        if(auxx_str == 'report'):
                            count_alienvault_sh_totalpulses+=1
                            count_alienvault_sh_typereport+=1
                            count_published_date_2019_alienvault_sh_typereport+=1
                        elif(auxx_str == 'indicator'):
                            count_alienvault_sh_totalpulses+=1
                            count_alienvault_sh_typeindicator+=1
                            count_published_date_2019_alienvault_sh_typeindicator+=1
                        elif(auxx_str == 'identity'):
                            count_alienvault_sh_totalpulses+=1
                            count_alienvault_sh_typeidentity+=1
                            count_published_date_2019_alienvault_sh_typeidentity+=1
                        elif(auxx_str == 'vulnerability'):
                            count_alienvault_sh_totalpulses+=1
                            count_alienvault_sh_typevulnerability+=1
                            count_published_date_2019_alienvault_sh_typevulnerability+=1
                                
                                
                    else: 
                        count_published_date_2018_alienvault_sh+=1
                        auxx=df_alienvault_sh["type"][r].split(",")
                        auxx_str=auxx[l].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
                        if(auxx_str == 'report'):
                            count_alienvault_sh_totalpulses+=1
                            count_alienvault_sh_typereport+=1
                            count_published_date_2018_alienvault_sh_typereport+=1
                        elif(auxx_str == 'indicator'):
                            count_alienvault_sh_totalpulses+=1
                            count_alienvault_sh_typeindicator+=1
                            count_published_date_2018_alienvault_sh_typeindicator+=1
                        elif(auxx_str == 'identity'):
                            count_alienvault_sh_totalpulses+=1
                            count_alienvault_sh_typeidentity+=1
                            count_published_date_2018_alienvault_sh_typeidentity+=1
                        elif(auxx_str == 'vulnerability'):
                            count_alienvault_sh_totalpulses+=1
                            count_alienvault_sh_typevulnerability+=1
                            count_published_date_2018_alienvault_sh_typevulnerability+=1
    else:
        #Si existe un unico valor de fecha de publicacion en la fila actual
        str_anio_publishdate_alienvault_sh=df_alienvault_sh["published"][r].split("-")
        #Obtengo el anio de creacion
        anio_publishdate_alienvault_sh=int(str_anio_publishdate_alienvault_sh[0])
        count_alienvault_sh_total+=1
        #Obtengo los valores de tipo para la fila actual
        auxx=df_alienvault_sh["type"][r].split(",")
        
        for l in range(0,len(auxx)):
            if(len(auxx)>0):
                auxx_str=auxx[l].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
                if(auxx_str!='NONE'):
                    count_alienvault_sh_totalpulses+=1
                    #Compruebo el anio de creacion
                    if(anio_publishdate_alienvault_sh >= 2023):
                        count_published_date_2023_alienvault_sh+=1
                        #Compruebo EL TIPO DE OBJETO
                        if(auxx_str == 'report'):
                            count_alienvault_sh_typereport+=1
                            count_published_date_2023_alienvault_sh_typereport+=1  
                        elif(auxx_str == 'indicator'):
                            count_alienvault_sh_typeindicator+=1
                            count_published_date_2023_alienvault_sh_typeindicator+=1  
                        elif(auxx_str == 'identity'):
                            count_alienvault_sh_typeidentity+=1
                            count_published_date_2023_alienvault_sh_typeidentity+=1
                        elif(auxx_str == 'vulnerability'):
                            count_alienvault_sh_typevulnerability+=1
                            count_published_date_2023_alienvault_sh_typevulnerability+=1

                    elif(anio_publishdate_alienvault_sh >= 2022):
                        count_published_date_2022_alienvault_sh+=1
                        if(auxx_str == 'report'):
                            count_alienvault_sh_typereport+=1
                            count_published_date_2022_alienvault_sh_typereport+=1  
                        elif(auxx_str == 'indicator'):
                            count_alienvault_sh_typeindicator+=1
                            count_published_date_2022_alienvault_sh_typeindicator+=1  
                        elif(auxx_str == 'identity'):
                            count_alienvault_sh_typeidentity+=1
                            count_published_date_2022_alienvault_sh_typeidentity+=1
                        elif(auxx_str == 'vulnerability'):
                            count_alienvault_sh_typevulnerability+=1
                            count_published_date_2022_alienvault_sh_typevulnerability+=1
                    elif(anio_publishdate_alienvault_sh >= 2021):
                        count_published_date_2021_alienvault_sh+=1
                        if(auxx_str == 'report'):
                            count_alienvault_sh_typereport+=1
                            count_published_date_2021_alienvault_sh_typereport+=1  
                        elif(auxx_str == 'indicator'):
                            count_alienvault_sh_typeindicator+=1
                            count_published_date_2021_alienvault_sh_typeindicator+=1  
                        elif(auxx_str == 'identity'):
                            count_alienvault_sh_typeidentity+=1
                            count_published_date_2021_alienvault_sh_typeidentity+=1
                        elif(auxx_str == 'vulnerability'):
                            count_alienvault_sh_typevulnerability+=1
                            count_published_date_2021_alienvault_sh_typevulnerability+=1
                    elif(anio_publishdate_alienvault_sh >= 2020):
                        count_published_date_2020_alienvault_sh+=1
                        if(auxx_str == 'report'):
                            count_alienvault_sh_typereport+=1
                            count_published_date_2020_alienvault_sh_typereport+=1  
                        elif(auxx_str == 'indicator'):
                            count_alienvault_sh_typeindicator+=1
                            count_published_date_2020_alienvault_sh_typeindicator+=1  
                        elif(auxx_str == 'identity'):
                            count_alienvault_sh_typeidentity+=1
                            count_published_date_2020_alienvault_sh_typeidentity+=1
                        elif(auxx_str == 'vulnerability'):
                            count_alienvault_sh_typevulnerability+=1
                            count_published_date_2020_alienvault_sh_typevulnerability+=1
                    elif(anio_publishdate_alienvault_sh >= 2019):
                        count_published_date_2019_alienvault_sh+=1
                        if(auxx_str == 'report'):
                            count_alienvault_sh_typereport+=1
                            count_published_date_2019_alienvault_sh_typereport+=1  
                        elif(auxx_str == 'indicator'):
                            count_alienvault_sh_typeindicator+=1
                            count_published_date_2019_alienvault_sh_typeindicator+=1  
                        elif(auxx_str == 'identity'):
                            count_alienvault_sh_typeidentity+=1
                            count_published_date_2019_alienvault_sh_typeidentity+=1
                        elif(auxx_str == 'vulnerability'):
                            count_alienvault_sh_typevulnerability+=1
                            count_published_date_2019_alienvault_sh_typevulnerability+=1
                    else:
                        count_published_date_2018_alienvault_sh+=1
                        if(auxx_str == 'report'):
                            count_alienvault_sh_typereport+=1
                            count_published_date_2018_alienvault_sh_typereport+=1  
                        elif(auxx_str == 'indicator'):
                            count_alienvault_sh_typeindicator+=1
                            count_published_date_2018_alienvault_sh_typeindicator+=1  
                        elif(auxx_str == 'identity'):
                            count_alienvault_sh_typeidentity+=1
                            count_published_date_2018_alienvault_sh_typeidentity+=1
                        elif(auxx_str == 'vulnerability'):
                            count_alienvault_sh_typevulnerability+=1
                            count_published_date_2018_alienvault_sh_typevulnerability+=1
                
                
print("**************ESTADÍSTICAS TIPO DE OBJETO/FECHA DE PUBLICACIÓN ALIENVAULT PARTE SMART HOME**************")
print("\n")                            
                
print("\n")
print(" DE UN TOTAL DE "+str(count_alienvault_sh_totalpulses)+" OBJETOS :\n") 
print("\n")
print("   - LAS ESTADISTICAS DE FECHA DE PUBLICACION SON LAS SIGUIENTES:  \n")
print("      -    EN  "+str(count_published_date_2023_alienvault_sh)+" OBJETOS LA FECHA DE PUBLICACION ES 2023. LAS ESTADÍSTICAS DE TIPO DE OBJETO SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(count_published_date_2023_alienvault_sh_typereport)+" OBJETOS PUBLICADOS EN 2023, EL TIPO ES REPORTE ")
print("            -    EN  "+str(count_published_date_2023_alienvault_sh_typeindicator)+" OBJETOS PUBLICADOS EN 2023, EL TIPO ES INDICADOR")
print("            -    EN  "+str(count_published_date_2023_alienvault_sh_typeidentity)+" OBJETOS PUBLICADOS EN 2023, EL TIPO ES IDENTIDAD ")
print("            -    EN  "+str(count_published_date_2023_alienvault_sh_typeidentity)+" OBJETOS PUBLICADOS EN 2023, EL TIPO ES VULNERABILIDAD ")
print("\n")
print("      -    EN  "+str(count_published_date_2022_alienvault_sh)+" OBJETOS LA FECHA DE PUBLICACION ES 2022. LAS ESTADÍSTICAS DE TIPO DE OBJETO SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(count_published_date_2022_alienvault_sh_typereport)+" OBJETOS PUBLICADOS EN 2022, EL TIPO ES REPORTE ")
print("            -    EN  "+str(count_published_date_2022_alienvault_sh_typeindicator)+" OBJETOS PUBLICADOS EN 2022, EL TIPO ES INDICADOR")
print("            -    EN  "+str(count_published_date_2022_alienvault_sh_typeidentity)+" OBJETOS PUBLICADOS EN 2022, EL TIPO ES IDENTIDAD ")
print("            -    EN  "+str(count_published_date_2022_alienvault_sh_typeidentity)+" OBJETOS PUBLICADOS EN 2022, EL TIPO ES VULNERABILIDAD ")
print("\n")
print("      -    EN  "+str(count_published_date_2021_alienvault_sh)+" OBJETOS LA FECHA DE PUBLICACION ES 2021. LAS ESTADÍSTICAS DE TIPO DE OBJETO SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(count_published_date_2021_alienvault_sh_typereport)+" OBJETOS PUBLICADOS EN 2021, EL TIPO ES REPORTE ")
print("            -    EN  "+str(count_published_date_2021_alienvault_sh_typeindicator)+" OBJETOS PUBLICADOS EN 2021, EL TIPO ES INDICADOR")
print("            -    EN  "+str(count_published_date_2021_alienvault_sh_typeidentity)+" OBJETOS PUBLICADOS EN 2021, EL TIPO ES IDENTIDAD ")
print("            -    EN  "+str(count_published_date_2021_alienvault_sh_typeidentity)+" OBJETOS PUBLICADOS EN 2021, EL TIPO ES VULNERABILIDAD ")
print("\n")
print("      -    EN  "+str(count_published_date_2020_alienvault_sh)+" OBJETOS LA FECHA DE PUBLICACION ES 2020. LAS ESTADÍSTICAS DE TIPO DE OBJETO SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(count_published_date_2020_alienvault_sh_typereport)+" OBJETOS PUBLICADOS EN 2020, EL TIPO ES REPORTE ")
print("            -    EN  "+str(count_published_date_2020_alienvault_sh_typeindicator)+" OBJETOS PUBLICADOS EN 2020, EL TIPO ES INDICADOR")
print("            -    EN  "+str(count_published_date_2020_alienvault_sh_typeidentity)+" OBJETOS PUBLICADOS EN 2020, EL TIPO ES IDENTIDAD ")
print("            -    EN  "+str(count_published_date_2020_alienvault_sh_typeidentity)+" OBJETOS PUBLICADOS EN 2020, EL TIPO ES VULNERABILIDAD ")
print("\n")
print("      -    EN  "+str(count_published_date_2019_alienvault_sh)+" OBJETOS LA FECHA DE PUBLICACION ES 2019. LAS ESTADÍSTICAS DE TIPO DE OBJETO SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(count_published_date_2019_alienvault_sh_typereport)+" OBJETOS PUBLICADOS EN 2019, EL TIPO ES REPORTE ")
print("            -    EN  "+str(count_published_date_2019_alienvault_sh_typeindicator)+" OBJETOS PUBLICADOS EN 2019, EL TIPO ES INDICADOR")
print("            -    EN  "+str(count_published_date_2019_alienvault_sh_typeidentity)+" OBJETOS PUBLICADOS EN 2019, EL TIPO ES IDENTIDAD ")
print("            -    EN  "+str(count_published_date_2019_alienvault_sh_typeidentity)+" OBJETOS PUBLICADOS EN 2019, EL TIPO ES VULNERABILIDAD ")
print("\n")
print("      -    EN  "+str(count_published_date_2018_alienvault_sh)+" OBJETOS LA FECHA DE PUBLICACION ES 2018 O ANTERIOR. LAS ESTADÍSTICAS DE TIPO DE OBJETO SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(count_published_date_2018_alienvault_sh_typereport)+" OBJETOS PUBLICADOS EN 2018 O ANTES, EL TIPO ES REPORTE ")
print("            -    EN  "+str(count_published_date_2018_alienvault_sh_typeindicator)+" OBJETOS PUBLICADOS EN 2018 O ANTES, EL TIPO ES INDICADOR")
print("            -    EN  "+str(count_published_date_2018_alienvault_sh_typeidentity)+" OBJETOS PUBLICADOS EN 2018 O ANTES, EL TIPO ES IDENTIDAD ")
print("            -    EN  "+str(count_published_date_2018_alienvault_sh_typeidentity)+" OBJETOS PUBLICADOS EN 2018, EL TIPO ES VULNERABILIDAD ")
print("\n")
print("   - LAS ESTADISTICAS DE TIPO DE OBJETO SON LAS SIGUIENTES:  \n")
print("      -    EN  "+str(count_alienvault_sh_typereport)+" OBJETOS EL TIPO DE OBJETO ES REPORTE. LAS ESTADÍSTICAS DE FECHA DE PUBLICACION SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(count_published_date_2023_alienvault_sh_typereport)+" OBJETOS LA FECHA DE PUBLICACION ES 2023 ")
print("            -    EN  "+str(count_published_date_2022_alienvault_sh_typereport)+" OBJETOS LA FECHA DE PUBLICACION ES 2022")
print("            -    EN  "+str(count_published_date_2021_alienvault_sh_typereport)+" OBJETOS LA FECHA DE PUBLICACION ES 2021 ")
print("            -    EN  "+str(count_published_date_2020_alienvault_sh_typereport)+" OBJETOS LA FECHA DE PUBLICACION ES 2020 ")
print("            -    EN  "+str(count_published_date_2019_alienvault_sh_typereport)+" OBJETOS LA FECHA DE PUBLICACION ES 2019")
print("            -    EN  "+str(count_published_date_2018_alienvault_sh_typereport)+" OBJETOS LA FECHA DE PUBLICACION ES 2018 O ANTERIOR ")
print("\n")
print("      -    EN  "+str(count_alienvault_sh_typeindicator)+" OBJETOS EL TIPO DE OBJETO ES INDICADOR. LAS ESTADÍSTICAS DE FECHA DE PUBLICACION SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(count_published_date_2023_alienvault_sh_typeindicator)+" OBJETOS LA FECHA DE PUBLICACION ES 2023 ")
print("            -    EN  "+str(count_published_date_2022_alienvault_sh_typeindicator)+" OBJETOS LA FECHA DE PUBLICACION ES 2022")
print("            -    EN  "+str(count_published_date_2021_alienvault_sh_typeindicator)+" OBJETOS LA FECHA DE PUBLICACION ES 2021 ")
print("            -    EN  "+str(count_published_date_2020_alienvault_sh_typeindicator)+" OBJETOS LA FECHA DE PUBLICACION ES 2020 ")
print("            -    EN  "+str(count_published_date_2019_alienvault_sh_typeindicator)+" OBJETOS LA FECHA DE PUBLICACION ES 2019")
print("            -    EN  "+str(count_published_date_2018_alienvault_sh_typeindicator)+" OBJETOS LA FECHA DE PUBLICACION ES 2018 O ANTERIOR ")
print("\n")
print("      -    EN  "+str(count_alienvault_sh_typeidentity)+" OBJETOS EL TIPO DE OBJETO ES IDENTIDAD. LAS ESTADÍSTICAS DE FECHA DE PUBLICACION SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(count_published_date_2023_alienvault_sh_typeidentity)+" OBJETOS LA FECHA DE PUBLICACION ES 2023 ")
print("            -    EN  "+str(count_published_date_2022_alienvault_sh_typeidentity)+" OBJETOS LA FECHA DE PUBLICACION ES 2022")
print("            -    EN  "+str(count_published_date_2021_alienvault_sh_typeidentity)+" OBJETOS LA FECHA DE PUBLICACION ES 2021 ")
print("            -    EN  "+str(count_published_date_2020_alienvault_sh_typeidentity)+" OBJETOS LA FECHA DE PUBLICACION ES 2020 ")
print("            -    EN  "+str(count_published_date_2019_alienvault_sh_typeidentity)+" OBJETOS LA FECHA DE PUBLICACION ES 2019")
print("            -    EN  "+str(count_published_date_2018_alienvault_sh_typeidentity)+" OBJETOS LA FECHA DE PUBLICACION ES 2018 O ANTERIOR ")
print("\n")
print("      -    EN  "+str(count_alienvault_sh_typevulnerability)+" OBJETOS EL TIPO DE OBJETO ES VULNERABILIDAD. LAS ESTADÍSTICAS DE FECHA DE PUBLICACION SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(count_published_date_2023_alienvault_sh_typevulnerability)+" OBJETOS LA FECHA DE PUBLICACION ES 2023 ")
print("            -    EN  "+str(count_published_date_2022_alienvault_sh_typevulnerability)+" OBJETOS LA FECHA DE PUBLICACION ES 2022")
print("            -    EN  "+str(count_published_date_2021_alienvault_sh_typevulnerability)+" OBJETOS LA FECHA DE PUBLICACION ES 2021 ")
print("            -    EN  "+str(count_published_date_2020_alienvault_sh_typevulnerability)+" OBJETOS LA FECHA DE PUBLICACION ES 2020 ")
print("            -    EN  "+str(count_published_date_2019_alienvault_sh_typevulnerability)+" OBJETOS LA FECHA DE PUBLICACION ES 2019")
print("            -    EN  "+str(count_published_date_2018_alienvault_sh_typevulnerability)+" OBJETOS LA FECHA DE PUBLICACION ES 2018 O ANTERIOR ")
print("\n")








print("**************PORCENTAJE TIPO DE OBJETO/FECHA DE PUBLICACIÓN ALIENVAULT PARTE SMART HOME**************")
print("\n")                            
                
print("\n")
print(" DE UN TOTAL DE "+str(count_alienvault_sh_totalpulses)+" OBJETOS :\n") 
print("\n")
print("   - LOS PORCENTAJES DE FECHA DE PUBLICACION SON LOS SIGUIENTES:  \n")
if(count_published_date_2023_alienvault_sh>0):
    print("      -    EN EL  "+str(float(((count_published_date_2023_alienvault_sh*100)/count_alienvault_sh_totalpulses)))+" % DE OBJETOS LA FECHA DE PUBLICACION ES 2023. LOS PORCENTAJES DE TIPO DE OBJETO SON LOS SIGUIENTES:  \n")
    print("\n")
    print("            -    EN EL  "+str(float(((count_published_date_2023_alienvault_sh_typereport*100)/count_published_date_2023_alienvault_sh)))+" % DE OBJETOS PUBLICADOS EN 2023, EL TIPO ES REPORTE ")
    print("            -    EN EL  "+str(float(((count_published_date_2023_alienvault_sh_typeindicator*100)/count_published_date_2023_alienvault_sh)))+" % DE OBJETOS PUBLICADOS EN 2023, EL TIPO ES INDICADOR")
    print("            -    EN EL  "+str(float(((count_published_date_2023_alienvault_sh_typeidentity*100)/count_published_date_2023_alienvault_sh)))+" % DE OBJETOS PUBLICADOS EN 2023, EL TIPO ES IDENTIDAD ")
    print("            -    EN EL  "+str(float(((count_published_date_2023_alienvault_sh_typevulnerability*100)/count_published_date_2023_alienvault_sh)))+" % DE OBJETOS PUBLICADOS EN 2023, EL TIPO ES VULNERABILIDAD ")
    print("\n")
if(count_published_date_2022_alienvault_sh>0):
    print("      -    EN EL  "+str(float(((count_published_date_2022_alienvault_sh*100)/count_alienvault_sh_totalpulses)))+" % DE OBJETOS LA FECHA DE PUBLICACION ES 2022. LOS PORCENTAJESS DE TIPO DE OBJETO SON LOS SIGUIENTES:  \n")
    print("\n")
    print("            -    EN EL  "+str(float(((count_published_date_2022_alienvault_sh_typereport*100)/count_published_date_2022_alienvault_sh)))+" % DE OBJETOS PUBLICADOS EN 2022, EL TIPO ES REPORTE ")
    print("            -    EN EL  "+str(float(((count_published_date_2022_alienvault_sh_typeindicator*100)/count_published_date_2022_alienvault_sh)))+" % DE OBJETOS PUBLICADOS EN 2022, EL TIPO ES INDICADOR")
    print("            -    EN EL  "+str(float(((count_published_date_2022_alienvault_sh_typeidentity*100)/count_published_date_2022_alienvault_sh)))+" % DE OBJETOS PUBLICADOS EN 2022, EL TIPO ES IDENTIDAD ")
    print("            -    EN EL  "+str(float(((count_published_date_2022_alienvault_sh_typevulnerability*100)/count_published_date_2022_alienvault_sh)))+" % DE OBJETOS PUBLICADOS EN 2022, EL TIPO ES VULNERABILIDAD ")
    print("\n")
if(count_published_date_2021_alienvault_sh>0):
    print("      -    EN EL  "+str(float(((count_published_date_2021_alienvault_sh*100)/count_alienvault_sh_totalpulses)))+" % DE OBJETOS LA FECHA DE PUBLICACION ES 2021. LOS PORCENTAJES DE TIPO DE OBJETO SON LOS SIGUIENTES:  \n")
    print("\n")
    print("            -    EN EL  "+str(float(((count_published_date_2021_alienvault_sh_typereport*100)/count_published_date_2021_alienvault_sh)))+" % DE OBJETOS PUBLICADOS EN 2021, EL TIPO ES REPORTE ")
    print("            -    EN EL  "+str(float(((count_published_date_2021_alienvault_sh_typeindicator*100)/count_published_date_2021_alienvault_sh)))+" % DE OBJETOS PUBLICADOS EN 2021, EL TIPO ES INDICADOR")
    print("            -    EN EL  "+str(float(((count_published_date_2021_alienvault_sh_typeidentity*100)/count_published_date_2021_alienvault_sh)))+" % DE OBJETOS PUBLICADOS EN 2021, EL TIPO ES IDENTIDAD ")
    print("            -    EN EL  "+str(float(((count_published_date_2021_alienvault_sh_typevulnerability*100)/count_published_date_2021_alienvault_sh)))+" % DE OBJETOS PUBLICADOS EN 2021, EL TIPO ES VULNERABILIDAD ")
    print("\n")
if(count_published_date_2020_alienvault_sh>0):
    print("      -    EN EL  "+str(float(((count_published_date_2020_alienvault_sh*100)/count_alienvault_sh_totalpulses)))+" % DE OBJETOS LA FECHA DE PUBLICACION ES 2020. LOS PORCENTAJES DE TIPO DE OBJETO SON LOS SIGUIENTES:  \n")
    print("\n")
    print("            -    EN EL  "+str(float(((count_published_date_2020_alienvault_sh_typereport*100)/count_published_date_2020_alienvault_sh)))+" % DE OBJETOS PUBLICADOS EN 2020, EL TIPO ES REPORTE ")
    print("            -    EN EL  "+str(float(((count_published_date_2020_alienvault_sh_typeindicator*100)/count_published_date_2020_alienvault_sh)))+" % DE OBJETOS PUBLICADOS EN 2020, EL TIPO ES INDICADOR")
    print("            -    EN EL  "+str(float(((count_published_date_2020_alienvault_sh_typeidentity*100)/count_published_date_2020_alienvault_sh)))+" % DE OBJETOS PUBLICADOS EN 2020, EL TIPO ES IDENTIDAD ")
    print("            -    EN EL  "+str(float(((count_published_date_2020_alienvault_sh_typevulnerability*100)/count_published_date_2020_alienvault_sh)))+" % DE OBJETOS PUBLICADOS EN 2020, EL TIPO ES VULNERABILIDAD ")
    print("\n")
if(count_published_date_2019_alienvault_sh>0):
    print("      -    EN EL  "+str(float(((count_published_date_2019_alienvault_sh*100)/count_alienvault_sh_totalpulses)))+" % DE OBJETOS LA FECHA DE PUBLICACION ES 2019. LOS PORCENTAJES DE TIPO DE OBJETO SON LOS SIGUIENTES:  \n")
    print("\n")
    print("            -    EN EL  "+str(float(((count_published_date_2019_alienvault_sh_typereport*100)/count_published_date_2019_alienvault_sh)))+" % DE OBJETOS PUBLICADOS EN 2019, EL TIPO ES REPORTE ")
    print("            -    EN EL  "+str(float(((count_published_date_2019_alienvault_sh_typeindicator*100)/count_published_date_2019_alienvault_sh)))+" % DE OBJETOS PUBLICADOS EN 2019, EL TIPO ES INDICADOR")
    print("            -    EN EL  "+str(float(((count_published_date_2019_alienvault_sh_typeidentity*100)/count_published_date_2019_alienvault_sh)))+" % DE OBJETOS PUBLICADOS EN 2019, EL TIPO ES IDENTIDAD ")
    print("            -    EN EL  "+str(float(((count_published_date_2019_alienvault_sh_typevulnerability*100)/count_published_date_2019_alienvault_sh)))+" % DE OBJETOS PUBLICADOS EN 2019, EL TIPO ES VULNERABILIDAD ")
    print("\n")
if(count_published_date_2018_alienvault_sh>0):
    print("      -    EN EL  "+str(float(((count_published_date_2018_alienvault_sh*100)/count_alienvault_sh_totalpulses)))+" % DE OBJETOS LA FECHA DE PUBLICACION ES 2018 O ANTERIOR. LOS PORCENTAJES DE TIPO DE OBJETO SON LOS SIGUIENTES:  \n")
    print("\n")
    print("            -    EN EL  "+str(float(((count_published_date_2018_alienvault_sh_typereport*100)/count_published_date_2018_alienvault_sh)))+" % DE OBJETOS PUBLICADOS EN 2018 O ANTERIORMENTE, EL TIPO ES REPORTE ")
    print("            -    EN EL  "+str(float(((count_published_date_2018_alienvault_sh_typeindicator*100)/count_published_date_2018_alienvault_sh)))+" % DE OBJETOS PUBLICADOS EN 2018 O ANTERIORMENTE, EL TIPO ES INDICADOR")
    print("            -    EN EL  "+str(float(((count_published_date_2018_alienvault_sh_typeidentity*100)/count_published_date_2018_alienvault_sh)))+" % DE OBJETOS PUBLICADOS EN 2018 O ANTERIORMENTE, EL TIPO ES IDENTIDAD ")
    print("            -    EN EL  "+str(float(((count_published_date_2018_alienvault_sh_typevulnerability*100)/count_published_date_2018_alienvault_sh)))+" % DE OBJETOS PUBLICADOS EN 2018, EL TIPO ES VULNERABILIDAD ")
    print("\n")
print("   - LOS PORCENTAJES DE TIPO DE OBJETO SON LOS SIGUIENTES:  \n")
if(count_alienvault_sh_typereport>0):
    print("      -    EN EL  "+str(float(((count_alienvault_sh_typereport*100)/count_alienvault_sh_totalpulses)))+" % DE OBJETOS EL TIPO DE OBJETO ES REPORTE. LOS PORCENTAJES DE FECHA DE PUBLICACION SON LOS SIGUIENTES:  \n")
    print("\n")
    print("            -    EN EL  "+str(float(((count_published_date_2023_alienvault_sh_typereport*100)/count_alienvault_sh_typereport)))+" % DE OBJETOS LA FECHA DE PUBLICACION ES 2023 ")
    print("            -    EN EL  "+str(float(((count_published_date_2022_alienvault_sh_typereport*100)/count_alienvault_sh_typereport)))+" % DE OBJETOS LA FECHA DE PUBLICACION ES 2022")
    print("            -    EN EL  "+str(float(((count_published_date_2021_alienvault_sh_typereport*100)/count_alienvault_sh_typereport)))+" % DE OBJETOS LA FECHA DE PUBLICACION ES 2021 ")
    print("            -    EN EL  "+str(float(((count_published_date_2020_alienvault_sh_typereport*100)/count_alienvault_sh_typereport)))+" % DE OBJETOS LA FECHA DE PUBLICACION ES 2020 ")
    print("            -    EN EL  "+str(float(((count_published_date_2019_alienvault_sh_typereport*100)/count_alienvault_sh_typereport)))+" % DE OBJETOS LA FECHA DE PUBLICACION ES 2019")
    print("            -    EN EL  "+str(float(((count_published_date_2018_alienvault_sh_typereport*100)/count_alienvault_sh_typereport)))+" % DE OBJETOS LA FECHA DE PUBLICACION ES 2018 O ANTERIOR ")
    print("\n")
if(count_alienvault_sh_typeindicator>0):
    print("      -    EN EL  "+str(float(((count_alienvault_sh_typeindicator*100)/count_alienvault_sh_totalpulses)))+" % DE OBJETOS EL TIPO DE OBJETO ES INDICADOR. LOS PORCENTAJES DE FECHA DE PUBLICACION SON LOS SIGUIENTES:  \n")
    print("\n")
    print("            -    EN EL  "+str(float(((count_published_date_2023_alienvault_sh_typeindicator*100)/count_alienvault_sh_typeindicator)))+" % DE OBJETOS LA FECHA DE PUBLICACION ES 2023 ")
    print("            -    EN EL  "+str(float(((count_published_date_2022_alienvault_sh_typeindicator*100)/count_alienvault_sh_typeindicator)))+" % DE OBJETOS LA FECHA DE PUBLICACION ES 2022")
    print("            -    EN EL  "+str(float(((count_published_date_2021_alienvault_sh_typeindicator*100)/count_alienvault_sh_typeindicator)))+" % DE OBJETOS LA FECHA DE PUBLICACION ES 2021 ")
    print("            -    EN EL  "+str(float(((count_published_date_2020_alienvault_sh_typeindicator*100)/count_alienvault_sh_typeindicator)))+" % DE OBJETOS LA FECHA DE PUBLICACION ES 2020 ")
    print("            -    EN EL  "+str(float(((count_published_date_2019_alienvault_sh_typeindicator*100)/count_alienvault_sh_typeindicator)))+" % DE OBJETOS LA FECHA DE PUBLICACION ES 2019")
    print("            -    EN EL  "+str(float(((count_published_date_2018_alienvault_sh_typeindicator*100)/count_alienvault_sh_typeindicator)))+" % DE OBJETOS LA FECHA DE PUBLICACION ES 2018 O ANTERIOR ")
    print("\n")
if(count_alienvault_sh_typeidentity>0):
    print("      -    EN EL  "+str(float(((count_alienvault_sh_typeidentity*100)/count_alienvault_sh_totalpulses)))+" % DE OBJETOS EL TIPO DE OBJETO ES IDENTIDAD. LOS PORCENTAJES DE FECHA DE PUBLICACION SON LOS SIGUIENTES:  \n")
    print("\n")
    print("            -    EN EL  "+str(float(((count_published_date_2023_alienvault_sh_typeidentity*100)/count_alienvault_sh_typeidentity)))+" % DE OBJETOS LA FECHA DE PUBLICACION ES 2023 ")
    print("            -    EN EL  "+str(float(((count_published_date_2022_alienvault_sh_typeidentity*100)/count_alienvault_sh_typeidentity)))+" % DE OBJETOS LA FECHA DE PUBLICACION ES 2022")
    print("            -    EN EL  "+str(float(((count_published_date_2021_alienvault_sh_typeidentity*100)/count_alienvault_sh_typeidentity)))+" % DE OBJETOS LA FECHA DE PUBLICACION ES 2021 ")
    print("            -    EN EL  "+str(float(((count_published_date_2020_alienvault_sh_typeidentity*100)/count_alienvault_sh_typeidentity)))+" % DE OBJETOS LA FECHA DE PUBLICACION ES 2020 ")
    print("            -    EN EL  "+str(float(((count_published_date_2019_alienvault_sh_typeidentity*100)/count_alienvault_sh_typeidentity)))+" % DE OBJETOS LA FECHA DE PUBLICACION ES 2019")
    print("            -    EN EL  "+str(float(((count_published_date_2018_alienvault_sh_typeidentity*100)/count_alienvault_sh_typeidentity)))+" % DE OBJETOS LA FECHA DE PUBLICACION ES 2018 O ANTERIOR ")
    print("\n")
if(count_alienvault_sh_typevulnerability>0):
    print("      -    EN EL  "+str(float(((count_alienvault_sh_typevulnerability*100)/count_alienvault_sh_totalpulses)))+" % DE OBJETOS EL TIPO DE OBJETO ES VULNERABILIDAD. LOS PORCENTAJES DE FECHA DE PUBLICACION SON LOS SIGUIENTES:  \n")
    print("\n")
    print("            -    EN EL  "+str(float(((count_published_date_2023_alienvault_sh_typevulnerability*100)/count_alienvault_sh_typevulnerability)))+" % DE OBJETOS LA FECHA DE PUBLICACION ES 2023 ")
    print("            -    EN EL  "+str(float(((count_published_date_2022_alienvault_sh_typevulnerability*100)/count_alienvault_sh_typevulnerability)))+" % DE OBJETOS LA FECHA DE PUBLICACION ES 2022")
    print("            -    EN EL  "+str(float(((count_published_date_2021_alienvault_sh_typevulnerability*100)/count_alienvault_sh_typevulnerability)))+" % DE OBJETOS LA FECHA DE PUBLICACION ES 2021 ")
    print("            -    EN EL  "+str(float(((count_published_date_2020_alienvault_sh_typevulnerability*100)/count_alienvault_sh_typevulnerability)))+" % DE OBJETOS LA FECHA DE PUBLICACION ES 2020 ")
    print("            -    EN EL  "+str(float(((count_published_date_2019_alienvault_sh_typevulnerability*100)/count_alienvault_sh_typevulnerability)))+" % DE OBJETOS LA FECHA DE PUBLICACION ES 2019")
    print("            -    EN EL  "+str(float(((count_published_date_2018_alienvault_sh_typevulnerability*100)/count_alienvault_sh_typevulnerability)))+" % DE OBJETOS LA FECHA DE PUBLICACION ES 2018 O ANTERIOR ")
    print("\n")


    
    
    
    
    
    
    
print("**************ESTADÍSTICAS TIPO DE OBJETO/FECHA DE PUBLICACIÓN OBJETOS PULSOS ALIENVAULT PARTE IOT Y SMART HOME CONJUNTAS**************")
print("\n")                            
                
print("\n")
print(" DE UN TOTAL DE "+str(count_alienvault_sh_totalpulses+count_alienvault_iot_totalpulses)+" OBJETOS :\n") 
print("\n")
print("   - LAS ESTADISTICAS DE FECHA DE PUBLICACION SON LAS SIGUIENTES:  \n")
print("      -    EN  "+str(count_published_date_2023_alienvault_iot+count_published_date_2023_alienvault_sh)+" OBJETOS LA FECHA DE PUBLICACION ES 2023. LAS ESTADÍSTICAS DE TIPO DE OBJETO SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(count_published_date_2023_alienvault_iot_typereport+count_published_date_2023_alienvault_sh_typereport)+" OBJETOS PUBLICADOS EN 2023, EL TIPO ES REPORTE ")
print("            -    EN  "+str(count_published_date_2023_alienvault_iot_typeindicator+count_published_date_2023_alienvault_sh_typeindicator)+" OBJETOS PUBLICADOS EN 2023, EL TIPO ES INDICADOR")
print("            -    EN  "+str(count_published_date_2023_alienvault_iot_typeidentity+count_published_date_2023_alienvault_sh_typeidentity)+" OBJETOS PUBLICADOS EN 2023, EL TIPO ES IDENTIDAD ")
print("            -    EN  "+str(count_published_date_2023_alienvault_iot_typevulnerability+count_published_date_2023_alienvault_sh_typevulnerability)+" OBJETOS PUBLICADOS EN 2023, EL TIPO ES VULNERABILIDAD ")
print("\n")
print("      -    EN  "+str(count_published_date_2022_alienvault_iot+count_published_date_2022_alienvault_sh)+" OBJETOS LA FECHA DE PUBLICACION ES 2022. LAS ESTADÍSTICAS DE TIPO DE OBJETO SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(count_published_date_2022_alienvault_iot_typereport+count_published_date_2022_alienvault_sh_typereport)+" OBJETOS PUBLICADOS EN 2022, EL TIPO ES REPORTE ")
print("            -    EN  "+str(count_published_date_2022_alienvault_iot_typeindicator+count_published_date_2022_alienvault_sh_typeindicator)+" OBJETOS PUBLICADOS EN 2022, EL TIPO ES INDICADOR")
print("            -    EN  "+str(count_published_date_2022_alienvault_iot_typeidentity+count_published_date_2022_alienvault_sh_typeidentity)+" OBJETOS PUBLICADOS EN 2022, EL TIPO ES IDENTIDAD ")
print("            -    EN  "+str(count_published_date_2022_alienvault_iot_typevulnerability+count_published_date_2022_alienvault_sh_typevulnerability)+" OBJETOS PUBLICADOS EN 2022, EL TIPO ES VULNERABILIDAD ")
print("\n")
print("      -    EN  "+str(count_published_date_2021_alienvault_iot+count_published_date_2021_alienvault_sh)+" OBJETOS LA FECHA DE PUBLICACION ES 2021. LAS ESTADÍSTICAS DE TIPO DE OBJETO SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(count_published_date_2021_alienvault_iot_typereport+count_published_date_2021_alienvault_sh_typereport)+" OBJETOS PUBLICADOS EN 2021, EL TIPO ES REPORTE ")
print("            -    EN  "+str(count_published_date_2021_alienvault_iot_typeindicator+count_published_date_2021_alienvault_sh_typeindicator)+" OBJETOS PUBLICADOS EN 2021, EL TIPO ES INDICADOR")
print("            -    EN  "+str(count_published_date_2021_alienvault_iot_typeidentity+count_published_date_2021_alienvault_sh_typeidentity)+" OBJETOS PUBLICADOS EN 2021, EL TIPO ES IDENTIDAD ")
print("            -    EN  "+str(count_published_date_2021_alienvault_iot_typevulnerability+count_published_date_2021_alienvault_sh_typevulnerability)+" OBJETOS PUBLICADOS EN 2021, EL TIPO ES VULNERABILIDAD ")
print("\n")
print("      -    EN  "+str(count_published_date_2020_alienvault_iot+count_published_date_2020_alienvault_sh)+" OBJETOS LA FECHA DE PUBLICACION ES 2020. LAS ESTADÍSTICAS DE TIPO DE OBJETO SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(count_published_date_2020_alienvault_iot_typereport+count_published_date_2020_alienvault_sh_typereport)+" OBJETOS PUBLICADOS EN 2020, EL TIPO ES REPORTE ")
print("            -    EN  "+str(count_published_date_2020_alienvault_iot_typeindicator+count_published_date_2020_alienvault_sh_typeindicator)+" OBJETOS PUBLICADOS EN 2020, EL TIPO ES INDICADOR")
print("            -    EN  "+str(count_published_date_2020_alienvault_iot_typeidentity+count_published_date_2020_alienvault_sh_typeidentity)+" OBJETOS PUBLICADOS EN 2020, EL TIPO ES IDENTIDAD ")
print("            -    EN  "+str(count_published_date_2020_alienvault_iot_typevulnerability+count_published_date_2020_alienvault_sh_typevulnerability)+" OBJETOS PUBLICADOS EN 2020, EL TIPO ES VULNERABILIDAD ")
print("\n")
print("      -    EN  "+str(count_published_date_2019_alienvault_iot+count_published_date_2019_alienvault_sh)+" OBJETOS LA FECHA DE PUBLICACION ES 2019. LAS ESTADÍSTICAS DE TIPO DE OBJETO SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(count_published_date_2019_alienvault_iot_typereport+count_published_date_2019_alienvault_sh_typereport)+" OBJETOS PUBLICADOS EN 2019, EL TIPO ES REPORTE ")
print("            -    EN  "+str(count_published_date_2019_alienvault_iot_typeindicator+count_published_date_2019_alienvault_sh_typeindicator)+" OBJETOS PUBLICADOS EN 2019, EL TIPO ES INDICADOR")
print("            -    EN  "+str(count_published_date_2019_alienvault_iot_typeidentity+count_published_date_2019_alienvault_sh_typeidentity)+" OBJETOS PUBLICADOS EN 2019, EL TIPO ES IDENTIDAD ")
print("            -    EN  "+str(count_published_date_2019_alienvault_iot_typevulnerability+count_published_date_2019_alienvault_sh_typevulnerability)+" OBJETOS PUBLICADOS EN 2019, EL TIPO ES VULNERABILIDAD ")
print("\n")
print("      -    EN  "+str(count_published_date_2018_alienvault_iot+count_published_date_2018_alienvault_sh)+" OBJETOS LA FECHA DE PUBLICACION ES 2018. LAS ESTADÍSTICAS DE TIPO DE OBJETO SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(count_published_date_2018_alienvault_iot_typereport+count_published_date_2018_alienvault_sh_typereport)+" OBJETOS PUBLICADOS EN 2018, EL TIPO ES REPORTE ")
print("            -    EN  "+str(count_published_date_2018_alienvault_iot_typeindicator+count_published_date_2018_alienvault_sh_typeindicator)+" OBJETOS PUBLICADOS EN 2018, EL TIPO ES INDICADOR")
print("            -    EN  "+str(count_published_date_2018_alienvault_iot_typeidentity+count_published_date_2018_alienvault_sh_typeidentity)+" OBJETOS PUBLICADOS EN 2018, EL TIPO ES IDENTIDAD ")
print("            -    EN  "+str(count_published_date_2018_alienvault_iot_typevulnerability+count_published_date_2018_alienvault_sh_typevulnerability)+" OBJETOS PUBLICADOS EN 2018, EL TIPO ES VULNERABILIDAD ")
print("\n")
print("   - LAS ESTADISTICAS DE TIPO DE OBJETO SON LAS SIGUIENTES:  \n")
print("      -    EN  "+str(count_alienvault_iot_typereport+count_alienvault_sh_typereport)+" OBJETOS EL TIPO DE OBJETO ES REPORTE. LAS ESTADÍSTICAS DE FECHA DE PUBLICACION SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(count_published_date_2023_alienvault_iot_typereport+count_published_date_2023_alienvault_sh_typereport)+" OBJETOS LA FECHA DE PUBLICACION ES 2023 ")
print("            -    EN  "+str(count_published_date_2022_alienvault_iot_typereport+count_published_date_2022_alienvault_sh_typereport)+" OBJETOS LA FECHA DE PUBLICACION ES 2022")
print("            -    EN  "+str(count_published_date_2021_alienvault_iot_typereport+count_published_date_2021_alienvault_sh_typereport)+" OBJETOS LA FECHA DE PUBLICACION ES 2021 ")
print("            -    EN  "+str(count_published_date_2020_alienvault_iot_typereport+count_published_date_2020_alienvault_sh_typereport)+" OBJETOS LA FECHA DE PUBLICACION ES 2020 ")
print("            -    EN  "+str(count_published_date_2019_alienvault_iot_typereport+count_published_date_2019_alienvault_sh_typereport)+" OBJETOS LA FECHA DE PUBLICACION ES 2019")
print("            -    EN  "+str(count_published_date_2018_alienvault_iot_typereport+count_published_date_2018_alienvault_sh_typereport)+" OBJETOS LA FECHA DE PUBLICACION ES 2018 O ANTERIOR ")
print("\n")
print("      -    EN  "+str(count_alienvault_iot_typeindicator+count_alienvault_sh_typeindicator)+" OBJETOS EL TIPO DE OBJETO ES INDICADOR. LAS ESTADÍSTICAS DE FECHA DE PUBLICACION SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(count_published_date_2023_alienvault_iot_typeindicator+count_published_date_2023_alienvault_sh_typeindicator)+" OBJETOS LA FECHA DE PUBLICACION ES 2023 ")
print("            -    EN  "+str(count_published_date_2022_alienvault_iot_typeindicator+count_published_date_2022_alienvault_sh_typeindicator)+" OBJETOS LA FECHA DE PUBLICACION ES 2022")
print("            -    EN  "+str(count_published_date_2021_alienvault_iot_typeindicator+count_published_date_2021_alienvault_sh_typeindicator)+" OBJETOS LA FECHA DE PUBLICACION ES 2021 ")
print("            -    EN  "+str(count_published_date_2020_alienvault_iot_typeindicator+count_published_date_2020_alienvault_sh_typeindicator)+" OBJETOS LA FECHA DE PUBLICACION ES 2020 ")
print("            -    EN  "+str(count_published_date_2019_alienvault_iot_typeindicator+count_published_date_2019_alienvault_sh_typeindicator)+" OBJETOS LA FECHA DE PUBLICACION ES 2019")
print("            -    EN  "+str(count_published_date_2018_alienvault_iot_typeindicator+count_published_date_2018_alienvault_sh_typeindicator)+" OBJETOS LA FECHA DE PUBLICACION ES 2018 O ANTERIOR ")
print("\n")
print("      -    EN  "+str(count_alienvault_iot_typeidentity+count_alienvault_sh_typeidentity)+" OBJETOS EL TIPO DE OBJETO ES IDENTIDAD. LAS ESTADÍSTICAS DE FECHA DE PUBLICACION SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(count_published_date_2023_alienvault_iot_typeidentity+count_published_date_2023_alienvault_sh_typeidentity)+" OBJETOS LA FECHA DE PUBLICACION ES 2023 ")
print("            -    EN  "+str(count_published_date_2022_alienvault_iot_typeidentity+count_published_date_2022_alienvault_sh_typeidentity)+" OBJETOS LA FECHA DE PUBLICACION ES 2022")
print("            -    EN  "+str(count_published_date_2021_alienvault_iot_typeidentity+count_published_date_2021_alienvault_sh_typeidentity)+" OBJETOS LA FECHA DE PUBLICACION ES 2021 ")
print("            -    EN  "+str(count_published_date_2020_alienvault_iot_typeidentity+count_published_date_2020_alienvault_sh_typeidentity)+" OBJETOS LA FECHA DE PUBLICACION ES 2020 ")
print("            -    EN  "+str(count_published_date_2019_alienvault_iot_typeidentity+count_published_date_2019_alienvault_sh_typeidentity)+" OBJETOS LA FECHA DE PUBLICACION ES 2019")
print("            -    EN  "+str(count_published_date_2018_alienvault_iot_typeidentity+count_published_date_2018_alienvault_sh_typeidentity)+" OBJETOS LA FECHA DE PUBLICACION ES 2018 O ANTERIOR ")
print("\n")
print("      -    EN  "+str(count_alienvault_iot_typevulnerability+count_alienvault_sh_typevulnerability)+" OBJETOS EL TIPO DE OBJETO ES VULNERABILIDAD. LAS ESTADÍSTICAS DE FECHA DE PUBLICACION SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(count_published_date_2023_alienvault_iot_typevulnerability+count_published_date_2023_alienvault_sh_typevulnerability)+" OBJETOS LA FECHA DE PUBLICACION ES 2023 ")
print("            -    EN  "+str(count_published_date_2022_alienvault_iot_typevulnerability+count_published_date_2022_alienvault_sh_typevulnerability)+" OBJETOS LA FECHA DE PUBLICACION ES 2022")
print("            -    EN  "+str(count_published_date_2021_alienvault_iot_typevulnerability+count_published_date_2021_alienvault_sh_typevulnerability)+" OBJETOS LA FECHA DE PUBLICACION ES 2021 ")
print("            -    EN  "+str(count_published_date_2020_alienvault_iot_typevulnerability+count_published_date_2020_alienvault_sh_typevulnerability)+" OBJETOS LA FECHA DE PUBLICACION ES 2020 ")
print("            -    EN  "+str(count_published_date_2019_alienvault_iot_typevulnerability+count_published_date_2019_alienvault_sh_typevulnerability)+" OBJETOS LA FECHA DE PUBLICACION ES 2019")
print("            -    EN  "+str(count_published_date_2018_alienvault_iot_typevulnerability+count_published_date_2018_alienvault_sh_typevulnerability)+" OBJETOS LA FECHA DE PUBLICACION ES 2018 O ANTERIOR ")
print("\n")













print("**************PORCENTAJE TIPO DE OBJETO/FECHA DE PUBLICACIÓN OBJETOS PULSOS ALIENVAULT PARTE IOT Y SMART HOME CONJUNTAS**************")
print("\n")                            
                
print("\n")
print(" DE UN TOTAL DE "+str(count_alienvault_sh_totalpulses+count_alienvault_iot_totalpulses)+" OBJETOS :\n") 
print("\n")
print("   - LOS PORCENTAJES DE FECHA DE PUBLICACION SON LOS SIGUIENTES:  \n")
if((count_published_date_2023_alienvault_iot+count_published_date_2023_alienvault_sh)>0):
    print("      -    EN EL  "+str(float(((count_published_date_2023_alienvault_iot+count_published_date_2023_alienvault_sh)*100)/(count_alienvault_sh_totalpulses+count_alienvault_iot_totalpulses)))+" % DE OBJETOS LA FECHA DE PUBLICACION ES 2023. LOS PORCENTAJES DE TIPO DE OBJETO SON LOS SIGUIENTES:  \n")
    print("\n")
    print("            -    EN EL  "+str(float((((count_published_date_2023_alienvault_iot_typereport+count_published_date_2023_alienvault_sh_typereport)*100)/(count_published_date_2023_alienvault_iot+count_published_date_2023_alienvault_sh))))+" % DE OBJETOS PUBLICADOS EN 2023, EL TIPO ES REPORTE ")
    print("            -    EN EL  "+str(float((((count_published_date_2023_alienvault_iot_typeindicator+count_published_date_2023_alienvault_sh_typeindicator)*100)/(count_published_date_2023_alienvault_iot+count_published_date_2023_alienvault_sh))))+" % DE OBJETOS PUBLICADOS EN 2023, EL TIPO ES INDICADOR")
    print("            -    EN EL  "+str(float((((count_published_date_2023_alienvault_iot_typeidentity+count_published_date_2023_alienvault_sh_typeidentity)*100)/(count_published_date_2023_alienvault_iot+count_published_date_2023_alienvault_sh))))+" % DE OBJETOS PUBLICADOS EN 2023, EL TIPO ES IDENTIDAD ")
    print("            -    EN EL  "+str(float((((count_published_date_2023_alienvault_iot_typevulnerability+count_published_date_2023_alienvault_sh_typevulnerability)*100)/(count_published_date_2023_alienvault_iot+count_published_date_2023_alienvault_sh))))+" % DE OBJETOS PUBLICADOS EN 2023, EL TIPO ES VULNERABILIDAD ")
    print("\n")
if((count_published_date_2022_alienvault_iot+count_published_date_2022_alienvault_sh)>0):
    print("      -    EN EL  "+str(float(((count_published_date_2022_alienvault_iot+count_published_date_2022_alienvault_sh)*100)/(count_alienvault_sh_totalpulses+count_alienvault_iot_totalpulses)))+" % DE OBJETOS LA FECHA DE PUBLICACION ES 2022. LOS PORCENTAJES DE TIPO DE OBJETO SON LOS SIGUIENTES:  \n")
    print("\n")
    print("            -    EN EL  "+str(float((((count_published_date_2022_alienvault_iot_typereport+count_published_date_2022_alienvault_sh_typereport)*100)/(count_published_date_2022_alienvault_iot+count_published_date_2022_alienvault_sh))))+" % DE OBJETOS PUBLICADOS EN 2022, EL TIPO ES REPORTE ")
    print("            -    EN EL  "+str(float((((count_published_date_2022_alienvault_iot_typeindicator+count_published_date_2022_alienvault_sh_typeindicator)*100)/(count_published_date_2022_alienvault_iot+count_published_date_2022_alienvault_sh))))+" % DE OBJETOS PUBLICADOS EN 2022, EL TIPO ES INDICADOR")
    print("            -    EN EL  "+str(float((((count_published_date_2022_alienvault_iot_typeidentity+count_published_date_2022_alienvault_sh_typeidentity)*100)/(count_published_date_2022_alienvault_iot+count_published_date_2022_alienvault_sh))))+" % DE OBJETOS PUBLICADOS EN 2022, EL TIPO ES IDENTIDAD ")
    print("            -    EN EL  "+str(float((((count_published_date_2022_alienvault_iot_typevulnerability+count_published_date_2022_alienvault_sh_typevulnerability)*100)/(count_published_date_2022_alienvault_iot+count_published_date_2022_alienvault_sh))))+" % DE OBJETOS PUBLICADOS EN 2022, EL TIPO ES VULNERABILIDAD ")
    print("\n")
if((count_published_date_2021_alienvault_iot+count_published_date_2021_alienvault_sh)>0):
    print("      -    EN EL  "+str(float(((count_published_date_2021_alienvault_iot+count_published_date_2021_alienvault_sh)*100)/(count_alienvault_sh_totalpulses+count_alienvault_iot_totalpulses)))+" % DE OBJETOS LA FECHA DE PUBLICACION ES 2021. LOS PORCENTAJES DE TIPO DE OBJETO SON LOS SIGUIENTES:  \n")
    print("\n")
    print("            -    EN EL  "+str(float((((count_published_date_2021_alienvault_iot_typereport+count_published_date_2021_alienvault_sh_typereport)*100)/(count_published_date_2021_alienvault_iot+count_published_date_2021_alienvault_sh))))+" % DE OBJETOS PUBLICADOS EN 2021, EL TIPO ES REPORTE ")
    print("            -    EN EL  "+str(float((((count_published_date_2021_alienvault_iot_typeindicator+count_published_date_2021_alienvault_sh_typeindicator)*100)/(count_published_date_2021_alienvault_iot+count_published_date_2021_alienvault_sh))))+" % DE OBJETOS PUBLICADOS EN 2021, EL TIPO ES INDICADOR")
    print("            -    EN EL  "+str(float((((count_published_date_2021_alienvault_iot_typeidentity+count_published_date_2021_alienvault_sh_typeidentity)*100)/(count_published_date_2021_alienvault_iot+count_published_date_2021_alienvault_sh))))+" % DE OBJETOS PUBLICADOS EN 2021, EL TIPO ES IDENTIDAD ")
    print("            -    EN EL  "+str(float((((count_published_date_2021_alienvault_iot_typevulnerability+count_published_date_2021_alienvault_sh_typevulnerability)*100)/(count_published_date_2021_alienvault_iot+count_published_date_2021_alienvault_sh))))+" % DE OBJETOS PUBLICADOS EN 2021, EL TIPO ES VULNERABILIDAD ")
    print("\n")
if((count_published_date_2020_alienvault_iot+count_published_date_2020_alienvault_sh)>0):
    print("      -    EN EL  "+str(float(((count_published_date_2020_alienvault_iot+count_published_date_2020_alienvault_sh)*100)/(count_alienvault_sh_totalpulses+count_alienvault_iot_totalpulses)))+" % DE OBJETOS LA FECHA DE PUBLICACION ES 2020. LOS PORCENTAJES DE TIPO DE OBJETO SON LOS SIGUIENTES:  \n")
    print("\n")
    print("            -    EN EL  "+str(float((((count_published_date_2020_alienvault_iot_typereport+count_published_date_2020_alienvault_sh_typereport)*100)/(count_published_date_2020_alienvault_iot+count_published_date_2020_alienvault_sh))))+" % DE OBJETOS PUBLICADOS EN 2020, EL TIPO ES REPORTE ")
    print("            -    EN EL  "+str(float((((count_published_date_2020_alienvault_iot_typeindicator+count_published_date_2020_alienvault_sh_typeindicator)*100)/(count_published_date_2020_alienvault_iot+count_published_date_2020_alienvault_sh))))+" % DE OBJETOS PUBLICADOS EN 2020, EL TIPO ES INDICADOR")
    print("            -    EN EL  "+str(float((((count_published_date_2020_alienvault_iot_typeidentity+count_published_date_2020_alienvault_sh_typeidentity)*100)/(count_published_date_2020_alienvault_iot+count_published_date_2020_alienvault_sh))))+" % DE OBJETOS PUBLICADOS EN 2020, EL TIPO ES IDENTIDAD ")
    print("            -    EN EL  "+str(float((((count_published_date_2020_alienvault_iot_typevulnerability+count_published_date_2020_alienvault_sh_typevulnerability)*100)/(count_published_date_2020_alienvault_iot+count_published_date_2020_alienvault_sh))))+" % DE OBJETOS PUBLICADOS EN 2020, EL TIPO ES VULNERABILIDAD ")
    print("\n")
if((count_published_date_2019_alienvault_iot+count_published_date_2019_alienvault_sh)>0):
    print("      -    EN EL  "+str(float(((count_published_date_2019_alienvault_iot+count_published_date_2019_alienvault_sh)*100)/(count_alienvault_sh_totalpulses+count_alienvault_iot_totalpulses)))+" % DE OBJETOS LA FECHA DE PUBLICACION ES 2019. LOS PORCENTAJES DE TIPO DE OBJETO SON LOS SIGUIENTES:  \n")
    print("\n")
    print("            -    EN EL  "+str(float((((count_published_date_2019_alienvault_iot_typereport+count_published_date_2019_alienvault_sh_typereport)*100)/(count_published_date_2019_alienvault_iot+count_published_date_2019_alienvault_sh))))+" % DE OBJETOS PUBLICADOS EN 2019, EL TIPO ES REPORTE ")
    print("            -    EN EL  "+str(float((((count_published_date_2019_alienvault_iot_typeindicator+count_published_date_2019_alienvault_sh_typeindicator)*100)/(count_published_date_2019_alienvault_iot+count_published_date_2019_alienvault_sh))))+" % DE OBJETOS PUBLICADOS EN 2019, EL TIPO ES INDICADOR")
    print("            -    EN EL  "+str(float((((count_published_date_2019_alienvault_iot_typeidentity+count_published_date_2019_alienvault_sh_typeidentity)*100)/(count_published_date_2019_alienvault_iot+count_published_date_2019_alienvault_sh))))+" % DE OBJETOS PUBLICADOS EN 2019, EL TIPO ES IDENTIDAD ")
    print("            -    EN EL  "+str(float((((count_published_date_2019_alienvault_iot_typevulnerability+count_published_date_2019_alienvault_sh_typevulnerability)*100)/(count_published_date_2019_alienvault_iot+count_published_date_2019_alienvault_sh))))+" % DE OBJETOS PUBLICADOS EN 2019, EL TIPO ES VULNERABILIDAD ")
    print("\n")
if((count_published_date_2018_alienvault_iot+count_published_date_2018_alienvault_sh)>0):
    print("      -    EN EL  "+str(float(((count_published_date_2018_alienvault_iot+count_published_date_2018_alienvault_sh)*100)/(count_alienvault_sh_totalpulses+count_alienvault_iot_totalpulses)))+" % DE OBJETOS LA FECHA DE PUBLICACION ES 2018 O ANTERIOR. LOS PORCENTAJES DE TIPO DE OBJETO SON LOS SIGUIENTES:  \n")
    print("\n")
    print("            -    EN EL  "+str(float((((count_published_date_2018_alienvault_iot_typereport+count_published_date_2018_alienvault_sh_typereport)*100)/(count_published_date_2018_alienvault_iot+count_published_date_2018_alienvault_sh))))+" % DE OBJETOS PUBLICADOS EN 2018 O ANTERIORMENTE, EL TIPO ES REPORTE ")
    print("            -    EN EL  "+str(float((((count_published_date_2018_alienvault_iot_typeindicator+count_published_date_2018_alienvault_sh_typeindicator)*100)/(count_published_date_2018_alienvault_iot+count_published_date_2018_alienvault_sh))))+" % DE OBJETOS PUBLICADOS EN 2018 O ANTERIORMENTE, EL TIPO ES INDICADOR")
    print("            -    EN EL  "+str(float((((count_published_date_2018_alienvault_iot_typeidentity+count_published_date_2018_alienvault_sh_typeidentity)*100)/(count_published_date_2018_alienvault_iot+count_published_date_2018_alienvault_sh))))+" % DE OBJETOS PUBLICADOS EN 2018 O ANTERIORMENTE, EL TIPO ES IDENTIDAD ")
    print("            -    EN EL  "+str(float((((count_published_date_2018_alienvault_iot_typevulnerability+count_published_date_2018_alienvault_sh_typevulnerability)*100)/(count_published_date_2018_alienvault_iot+count_published_date_2018_alienvault_sh))))+" % DE OBJETOS PUBLICADOS EN 2018 O ANTERIORMENTE, EL TIPO ES VULNERABILIDAD ")
    print("\n")
print("   - LOS PORCENTAJES DE TIPO DE OBJETO SON LOS SIGUIENTES:  \n")
print("      -    EN EL  "+str(float((((count_alienvault_iot_typereport+count_alienvault_sh_typereport)*100)/(count_alienvault_sh_totalpulses+count_alienvault_iot_totalpulses))))+" % DE OBJETOS EL TIPO DE OBJETO ES REPORTE. LOS PORCENTAJES DE FECHA DE PUBLICACION SON LOS SIGUIENTES:  \n")
print("\n")
print("            -    EN EL  "+str(float((((count_published_date_2023_alienvault_iot_typereport+count_published_date_2023_alienvault_sh_typereport)*100)/(count_alienvault_iot_typereport+count_alienvault_sh_typereport))))+" % DE OBJETOS LA FECHA DE PUBLICACION ES 2023 ")
print("            -    EN EL  "+str(float((((count_published_date_2022_alienvault_iot_typereport+count_published_date_2022_alienvault_sh_typereport)*100)/(count_alienvault_iot_typereport+count_alienvault_sh_typereport))))+" % DE OBJETOS LA FECHA DE PUBLICACION ES 2022")
print("            -    EN EL  "+str(float((((count_published_date_2021_alienvault_iot_typereport+count_published_date_2021_alienvault_sh_typereport)*100)/(count_alienvault_iot_typereport+count_alienvault_sh_typereport))))+" % DE OBJETOS LA FECHA DE PUBLICACION ES 2021 ")
print("            -    EN EL  "+str(float((((count_published_date_2020_alienvault_iot_typereport+count_published_date_2020_alienvault_sh_typereport)*100)/(count_alienvault_iot_typereport+count_alienvault_sh_typereport))))+" % DE OBJETOS LA FECHA DE PUBLICACION ES 2020 ")
print("            -    EN EL  "+str(float((((count_published_date_2019_alienvault_iot_typereport+count_published_date_2019_alienvault_sh_typereport)*100)/(count_alienvault_iot_typereport+count_alienvault_sh_typereport))))+" % DE OBJETOS LA FECHA DE PUBLICACION ES 2019")
print("            -    EN EL  "+str(float((((count_published_date_2018_alienvault_iot_typereport+count_published_date_2018_alienvault_sh_typereport)*100)/(count_alienvault_iot_typereport+count_alienvault_sh_typereport))))+" % DE OBJETOS LA FECHA DE PUBLICACION ES 2018 O ANTERIOR ")
print("\n")
print("      -    EN EL  "+str(float((((count_alienvault_iot_typeindicator+count_alienvault_sh_typeindicator)*100)/(count_alienvault_sh_totalpulses+count_alienvault_iot_totalpulses))))+" % DE OBJETOS EL TIPO DE OBJETO ES INDICADOR. LOS PORCENTAJES DE FECHA DE PUBLICACION SON LOS SIGUIENTES:  \n")
print("\n")
print("            -    EN EL  "+str(float((((count_published_date_2023_alienvault_iot_typeindicator+count_published_date_2023_alienvault_sh_typeindicator)*100)/(count_alienvault_iot_typeindicator+count_alienvault_sh_typeindicator))))+" % DE OBJETOS LA FECHA DE PUBLICACION ES 2023 ")
print("            -    EN EL  "+str(float((((count_published_date_2022_alienvault_iot_typeindicator+count_published_date_2022_alienvault_sh_typeindicator)*100)/(count_alienvault_iot_typeindicator+count_alienvault_sh_typeindicator))))+" % DE OBJETOS LA FECHA DE PUBLICACION ES 2022")
print("            -    EN EL  "+str(float((((count_published_date_2021_alienvault_iot_typeindicator+count_published_date_2021_alienvault_sh_typeindicator)*100)/(count_alienvault_iot_typeindicator+count_alienvault_sh_typeindicator))))+" % DE OBJETOS LA FECHA DE PUBLICACION ES 2021 ")
print("            -    EN EL  "+str(float((((count_published_date_2020_alienvault_iot_typeindicator+count_published_date_2020_alienvault_sh_typeindicator)*100)/(count_alienvault_iot_typeindicator+count_alienvault_sh_typeindicator))))+" % DE OBJETOS LA FECHA DE PUBLICACION ES 2020 ")
print("            -    EN EL  "+str(float((((count_published_date_2019_alienvault_iot_typeindicator+count_published_date_2019_alienvault_sh_typeindicator)*100)/(count_alienvault_iot_typeindicator+count_alienvault_sh_typeindicator))))+" % DE OBJETOS LA FECHA DE PUBLICACION ES 2019")
print("            -    EN EL  "+str(float((((count_published_date_2018_alienvault_iot_typeindicator+count_published_date_2018_alienvault_sh_typeindicator)*100)/(count_alienvault_iot_typeindicator+count_alienvault_sh_typeindicator))))+" % DE OBJETOS LA FECHA DE PUBLICACION ES 2018 O ANTERIOR ")
print("\n")
print("      -    EN EL  "+str(float((((count_alienvault_iot_typeidentity+count_alienvault_sh_typeidentity)*100)/(count_alienvault_sh_totalpulses+count_alienvault_iot_totalpulses))))+" % DE OBJETOS EL TIPO DE OBJETO ES IDENTIDAD. LOS PORCENTAJES DE FECHA DE PUBLICACION SON LOS SIGUIENTES:  \n")
print("\n")
print("            -    EN EL  "+str(float((((count_published_date_2023_alienvault_iot_typeidentity+count_published_date_2023_alienvault_sh_typeidentity)*100)/(count_alienvault_iot_typeidentity+count_alienvault_sh_typeidentity))))+" % DE OBJETOS LA FECHA DE PUBLICACION ES 2023 ")
print("            -    EN EL  "+str(float((((count_published_date_2022_alienvault_iot_typeidentity+count_published_date_2022_alienvault_sh_typeidentity)*100)/(count_alienvault_iot_typeidentity+count_alienvault_sh_typeidentity))))+" % DE OBJETOS LA FECHA DE PUBLICACION ES 2022")
print("            -    EN EL  "+str(float((((count_published_date_2021_alienvault_iot_typeidentity+count_published_date_2021_alienvault_sh_typeidentity)*100)/(count_alienvault_iot_typeidentity+count_alienvault_sh_typeidentity))))+" % DE OBJETOS LA FECHA DE PUBLICACION ES 2021 ")
print("            -    EN EL  "+str(float((((count_published_date_2020_alienvault_iot_typeidentity+count_published_date_2020_alienvault_sh_typeidentity)*100)/(count_alienvault_iot_typeidentity+count_alienvault_sh_typeidentity))))+" % DE OBJETOS LA FECHA DE PUBLICACION ES 2020 ")
print("            -    EN EL  "+str(float((((count_published_date_2019_alienvault_iot_typeidentity+count_published_date_2019_alienvault_sh_typeidentity)*100)/(count_alienvault_iot_typeidentity+count_alienvault_sh_typeidentity))))+" % DE OBJETOS LA FECHA DE PUBLICACION ES 2019")
print("            -    EN EL  "+str(float((((count_published_date_2018_alienvault_iot_typeidentity+count_published_date_2018_alienvault_sh_typeidentity)*100)/(count_alienvault_iot_typeidentity+count_alienvault_sh_typeidentity))))+" % DE OBJETOS LA FECHA DE PUBLICACION ES 2018 O ANTERIOR ")
print("\n")
print("      -    EN EL  "+str(float((((count_alienvault_iot_typevulnerability+count_alienvault_sh_typevulnerability)*100)/(count_alienvault_sh_totalpulses+count_alienvault_iot_totalpulses))))+" % DE OBJETOS EL TIPO DE OBJETO ES VULNERABILIDAD. LOS PORCENTAJES DE FECHA DE PUBLICACION SON LOS SIGUIENTES:  \n")
print("\n")
print("            -    EN EL  "+str(float((((count_published_date_2023_alienvault_iot_typevulnerability+count_published_date_2023_alienvault_sh_typevulnerability)*100)/(count_alienvault_iot_typevulnerability+count_alienvault_sh_typevulnerability))))+" % DE OBJETOS LA FECHA DE PUBLICACION ES 2023 ")
print("            -    EN EL  "+str(float((((count_published_date_2022_alienvault_iot_typevulnerability+count_published_date_2022_alienvault_sh_typevulnerability)*100)/(count_alienvault_iot_typevulnerability+count_alienvault_sh_typevulnerability))))+" % DE OBJETOS LA FECHA DE PUBLICACION ES 2022")
print("            -    EN EL  "+str(float((((count_published_date_2021_alienvault_iot_typevulnerability+count_published_date_2021_alienvault_sh_typevulnerability)*100)/(count_alienvault_iot_typevulnerability+count_alienvault_sh_typevulnerability))))+" % DE OBJETOS LA FECHA DE PUBLICACION ES 2021 ")
print("            -    EN EL  "+str(float((((count_published_date_2020_alienvault_iot_typevulnerability+count_published_date_2020_alienvault_sh_typevulnerability)*100)/(count_alienvault_iot_typevulnerability+count_alienvault_sh_typevulnerability))))+" % DE OBJETOS LA FECHA DE PUBLICACION ES 2020 ")
print("            -    EN EL  "+str(float((((count_published_date_2019_alienvault_iot_typevulnerability+count_published_date_2019_alienvault_sh_typevulnerability)*100)/(count_alienvault_iot_typevulnerability+count_alienvault_sh_typevulnerability))))+" % DE OBJETOS LA FECHA DE PUBLICACION ES 2019")
print("            -    EN EL  "+str(float((((count_published_date_2018_alienvault_iot_typevulnerability+count_published_date_2018_alienvault_sh_typevulnerability)*100)/(count_alienvault_iot_typevulnerability+count_alienvault_sh_typevulnerability))))+" % DE OBJETOS LA FECHA DE PUBLICACION ES 2018 O ANTERIOR ")
print("\n")




























