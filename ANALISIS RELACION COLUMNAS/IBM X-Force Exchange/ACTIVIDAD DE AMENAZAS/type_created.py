


import pandas as pd
from datetime import datetime

#Abro los ficheros con los que voy a tratar


df_thract_iot = pd.read_excel('ibm_threat_activity_report_iot_2023_v2.xlsx')





#Variables donde almacenare el contador de tipo segun el anio de creacion
count_created_date_2023_thract_iot_typereport=0
count_created_date_2023_thract_iot_typeindicator=0
count_created_date_2023_thract_iot_typemarkingdefinition=0
#Variables donde almacenare el contador de anio de creacion 
count_created_date_2023_thract_iot=0

count_created_date_2022_thract_iot_typereport=0
count_created_date_2022_thract_iot_typeindicator=0
count_created_date_2022_thract_iot_typemarkingdefinition=0
count_created_date_2022_thract_iot=0


count_created_date_2021_thract_iot_typereport=0
count_created_date_2021_thract_iot_typeindicator=0
count_created_date_2021_thract_iot_typemarkingdefinition=0
count_created_date_2021_thract_iot=0


count_created_date_2020_thract_iot_typereport=0
count_created_date_2020_thract_iot_typeindicator=0
count_created_date_2020_thract_iot_typemarkingdefinition=0
count_created_date_2020_thract_iot=0


count_created_date_2019_thract_iot_typereport=0
count_created_date_2019_thract_iot_typeindicator=0
count_created_date_2019_thract_iot_typemarkingdefinition=0
count_created_date_2019_thract_iot=0


count_created_date_2018_thract_iot_typereport=0
count_created_date_2018_thract_iot_typeindicator=0
count_created_date_2018_thract_iot_typemarkingdefinition=0
count_created_date_2018_thract_iot=0

count_thract_iot_typereport=0
count_thract_iot_typeindicator=0
count_thract_iot_typemarkingdefinition=0

#Contador de OBJETOs totales
count_thract_iot_total=0


#Comprobamos el anio de creacion 
for r in range(0,len(df_thract_iot["created"])):
    #Si existen varios valores para una misma fila
    if('[' in df_thract_iot["created"][r]):
        #Obtengo los valores de fecha de creacion
        aux=df_thract_iot["created"][r].split(",")
        #Recorro los distintos valores de la misma fila
        for l in range(0,len(aux)):
            if(len(aux)>0):
                aux_str=aux[l].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
                if(aux_str!='NONE'):
                    #Obtengo el anio de creacion
                    count_thract_iot_total+=1
                    str_anio_publishdate_thract_iot=aux_str.split("-")
                    anio_publishdate_thract_iot=int(str_anio_publishdate_thract_iot[0])
                    #Compruebo el anio de creacion
                    if(anio_publishdate_thract_iot >= 2023):
                        count_created_date_2023_thract_iot+=1
                        #Obtengo los distintos valores de tipo en la fila actual
                        auxx=df_thract_iot["type"][r].split(",")
                        #Obtengo los valores individuales de tipo en la fila actual
                        auxx_str=auxx[l].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
                        #Compruebo el tipo
                        if(auxx_str == 'report'):
                            count_thract_iot_typereport+=1
                            count_created_date_2023_thract_iot_typereport+=1
                        elif(auxx_str == 'indicator'):
                            count_thract_iot_typeindicator+=1
                            count_created_date_2023_thract_iot_typeindicator+=1
                        elif(auxx_str == 'marking-definition'):
                            count_thract_iot_typemarkingdefinition+=1
                            count_created_date_2023_thract_iot_typemarkingdefinition+=1 
                                 
                                
                    elif(anio_publishdate_thract_iot >= 2022):
                        count_created_date_2022_thract_iot+=1
                        auxx=df_thract_iot["type"][r].split(",")
                        auxx_str=auxx[l].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
                        if(auxx_str == 'report'):
                            count_thract_iot_typereport+=1
                            count_created_date_2022_thract_iot_typereport+=1
                        elif(auxx_str == 'indicator'):
                            count_thract_iot_typeindicator+=1
                            count_created_date_2022_thract_iot_typeindicator+=1
                        elif(auxx_str == 'marking-definition'):
                            count_thract_iot_typemarkingdefinition+=1
                            count_created_date_2022_thract_iot_typemarkingdefinition+=1 
                                
                    elif(anio_publishdate_thract_iot >= 2021):
                        count_created_date_2021_thract_iot+=1
                        auxx=df_thract_iot["type"][r].split(",")
                        auxx_str=auxx[l].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
                        if(auxx_str == 'report'):
                            count_thract_iot_typereport+=1
                            count_created_date_2021_thract_iot_typereport+=1
                        elif(auxx_str == 'indicator'):
                            count_thract_iot_typeindicator+=1
                            count_created_date_2021_thract_iot_typeindicator+=1
                        elif(auxx_str == 'marking-definition'):
                            count_thract_iot_typemarkingdefinition+=1
                            count_created_date_2021_thract_iot_typemarkingdefinition+=1 
                                
                    elif(anio_publishdate_thract_iot >= 2020):
                        count_created_date_2020_thract_iot+=1
                        auxx=df_thract_iot["type"][r].split(",")
                        auxx_str=auxx[l].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
                        if(auxx_str == 'report'):
                            count_thract_iot_typereport+=1
                            count_created_date_2020_thract_iot_typereport+=1
                        elif(auxx_str == 'indicator'):
                            count_thract_iot_typeindicator+=1
                            count_created_date_2020_thract_iot_typeindicator+=1
                        elif(auxx_str == 'marking-definition'):
                            count_thract_iot_typemarkingdefinition+=1
                            count_created_date_2020_thract_iot_typemarkingdefinition+=1 
                                
                                
                    elif(anio_publishdate_thract_iot >= 2019):
                        count_created_date_2019_thract_iot+=1
                        auxx=df_thract_iot["type"][r].split(",")
                        auxx_str=auxx[l].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
                        if(auxx_str == 'report'):
                            count_thract_iot_typereport+=1
                            count_created_date_2019_thract_iot_typereport+=1
                        elif(auxx_str == 'indicator'):
                            count_thract_iot_typeindicator+=1
                            count_created_date_2019_thract_iot_typeindicator+=1
                        elif(auxx_str == 'marking-definition'):
                            count_thract_iot_typemarkingdefinition+=1
                            count_created_date_2019_thract_iot_typemarkingdefinition+=1 
                                
                                
                    else: 
                        count_created_date_2018_thract_iot+=1
                        auxx=df_thract_iot["type"][r].split(",")
                        auxx_str=auxx[l].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
                        if(auxx_str == 'report'):
                            count_thract_iot_typereport+=1
                            count_created_date_2018_thract_iot_typereport+=1
                        elif(auxx_str == 'indicator'):
                            count_thract_iot_typeindicator+=1
                            count_created_date_2018_thract_iot_typeindicator+=1
                        elif(auxx_str == 'marking-definition'):
                            count_thract_iot_typemarkingdefinition+=1
                            count_created_date_2018_thract_iot_typemarkingdefinition+=1
    else:
        #Si existe un unico valor de fecha de creacion y tipo para la fila actual
        str_anio_publishdate_thract_iot=df_thract_iot["created"][r].split("-")
        anio_publishdate_thract_iot=int(str_anio_publishdate_thract_iot[0])
        count_thract_iot_total+=1
        #Compruebo el anio de creacion
        if(anio_publishdate_thract_iot >= 2023):
            count_created_date_2023_thract_iot+=1
            #Compruebo el tipo de OBJETO
            if(df_thract_iot["type"][r] == 'report'):
                count_thract_iot_typereport+=1
                count_created_date_2023_thract_iot_typereport+=1  
            elif(df_thract_iot["type"][r] == 'indicator'):
                count_thract_iot_typeindicator+=1
                count_created_date_2023_thract_iot_typeindicator+=1  
            elif(df_thract_iot["type"][r] == 'marking-definition'):
                count_thract_iot_typemarkingdefinition+=1
                count_created_date_2023_thract_iot_typemarkingdefinition+=1
                
        elif(anio_publishdate_thract_iot >= 2022):
            count_created_date_2022_thract_iot+=1
            if(df_thract_iot["type"][r] == 'report'):
                count_thract_iot_typereport+=1
                count_created_date_2022_thract_iot_typereport+=1  
            elif(df_thract_iot["type"][r] == 'indicator'):
                count_thract_iot_typeindicator+=1
                count_created_date_2022_thract_iot_typeindicator+=1  
            elif(df_thract_iot["type"][r] == 'marking-definition'):
                count_thract_iot_typemarkingdefinition+=1
                count_created_date_2022_thract_iot_typemarkingdefinition+=1
        elif(anio_publishdate_thract_iot >= 2021):
            count_created_date_2021_thract_iot+=1
            if(df_thract_iot["type"][r] == 'report'):
                count_thract_iot_typereport+=1
                count_created_date_2021_thract_iot_typereport+=1  
            elif(df_thract_iot["type"][r] == 'indicator'):
                count_thract_iot_typeindicator+=1
                count_created_date_2021_thract_iot_typeindicator+=1  
            elif(df_thract_iot["type"][r] == 'marking-definition'):
                count_thract_iot_typemarkingdefinition+=1
                count_created_date_2021_thract_iot_typemarkingdefinition+=1
        elif(anio_publishdate_thract_iot >= 2020):
            count_created_date_2020_thract_iot+=1
            if(df_thract_iot["type"][r] == 'report'):
                count_thract_iot_typereport+=1
                count_created_date_2020_thract_iot_typereport+=1  
            elif(df_thract_iot["type"][r] == 'indicator'):
                count_thract_iot_typeindicator+=1
                count_created_date_2020_thract_iot_typeindicator+=1  
            elif(df_thract_iot["type"][r] == 'marking-definition'):
                count_thract_iot_typemarkingdefinition+=1
                count_created_date_2020_thract_iot_typemarkingdefinition+=1
        elif(anio_publishdate_thract_iot >= 2019):
            count_created_date_2019_thract_iot+=1
            if(df_thract_iot["type"][r] == 'report'):
                count_thract_iot_typereport+=1
                count_created_date_2019_thract_iot_typereport+=1  
            elif(df_thract_iot["type"][r] == 'indicator'):
                count_thract_iot_typeindicator+=1
                count_created_date_2019_thract_iot_typeindicator+=1  
            elif(df_thract_iot["type"][r] == 'marking-definition'):
                count_thract_iot_typemarkingdefinition+=1
                count_created_date_2019_thract_iot_typemarkingdefinition+=1
        else:
            count_created_date_2018_thract_iot+=1
            if(df_thract_iot["type"][r] == 'report'):
                count_thract_iot_typereport+=1
                count_created_date_2018_thract_iot_typereport+=1  
            elif(df_thract_iot["type"][r] == 'indicator'):
                count_thract_iot_typeindicator+=1
                count_created_date_2018_thract_iot_typeindicator+=1  
            elif(df_thract_iot["type"][r] == 'marking-definition'):
                count_thract_iot_typemarkingdefinition+=1
                count_created_date_2018_thract_iot_typemarkingdefinition+=1
                
                
print("***************************ESTADÍSTICAS TIPO DE OBJETO/FECHA DE CREACIÓN INFORME ACTIVIDAD DE AMENAZAS IBM PARTE IOT***************************")
print("\n")                            
                
print("\n")
print(" DE UN TOTAL DE "+str(count_thract_iot_total)+" OBJETOS :\n") 
print("\n")
print("   - LAS ESTADISTICAS DE FECHA DE CREACION SON LAS SIGUIENTES:  \n")
print("      -    EN  "+str(count_created_date_2023_thract_iot)+" OBJETOS LA FECHA DE CREACION ES 2023. LAS ESTADÍSTICAS DE TIPO DE OBJETO SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(count_created_date_2023_thract_iot_typereport)+" OBJETOS CREADOS EN 2023, EL TIPO ES REPORTE ")
print("            -    EN  "+str(count_created_date_2023_thract_iot_typeindicator)+" OBJETOS CREADOS EN 2023, EL TIPO ES INDICADOR")
print("            -    EN  "+str(count_created_date_2023_thract_iot_typemarkingdefinition)+" OBJETOS CREADOS EN 2023, EL TIPO ES DEFINICION DE MARCADO ")
print("\n")
print("      -    EN  "+str(count_created_date_2022_thract_iot)+" OBJETOS LA FECHA DE CREACION ES 2022. LAS ESTADÍSTICAS DE TIPO DE OBJETO SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(count_created_date_2022_thract_iot_typereport)+" OBJETOS CREADOS EN 2022, EL TIPO ES REPORTE ")
print("            -    EN  "+str(count_created_date_2022_thract_iot_typeindicator)+" OBJETOS CREADOS EN 2022, EL TIPO ES INDICADOR")
print("            -    EN  "+str(count_created_date_2022_thract_iot_typemarkingdefinition)+" OBJETOS CREADOS EN 2022, EL TIPO ES DEFINICION DE MARCADO ")
print("\n")
print("      -    EN  "+str(count_created_date_2021_thract_iot)+" OBJETOS LA FECHA DE CREACION ES 2021. LAS ESTADÍSTICAS DE TIPO DE OBJETO SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(count_created_date_2021_thract_iot_typereport)+" OBJETOS CREADOS EN 2021, EL TIPO ES REPORTE ")
print("            -    EN  "+str(count_created_date_2021_thract_iot_typeindicator)+" OBJETOS CREADOS EN 2021, EL TIPO ES INDICADOR")
print("            -    EN  "+str(count_created_date_2021_thract_iot_typemarkingdefinition)+" OBJETOS CREADOS EN 2021, EL TIPO ES DEFINICION DE MARCADO ")
print("\n")
print("      -    EN  "+str(count_created_date_2020_thract_iot)+" OBJETOS LA FECHA DE CREACION ES 2020. LAS ESTADÍSTICAS DE TIPO DE OBJETO SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(count_created_date_2020_thract_iot_typereport)+" OBJETOS CREADOS EN 2020, EL TIPO ES REPORTE ")
print("            -    EN  "+str(count_created_date_2020_thract_iot_typeindicator)+" OBJETOS CREADOS EN 2020, EL TIPO ES INDICADOR")
print("            -    EN  "+str(count_created_date_2020_thract_iot_typemarkingdefinition)+" OBJETOS CREADOS EN 2020, EL TIPO ES DEFINICION DE MARCADO ")
print("\n")
print("      -    EN  "+str(count_created_date_2019_thract_iot)+" OBJETOS LA FECHA DE CREACION ES 2019. LAS ESTADÍSTICAS DE TIPO DE OBJETO SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(count_created_date_2019_thract_iot_typereport)+" OBJETOS CREADOS EN 2019, EL TIPO ES REPORTE ")
print("            -    EN  "+str(count_created_date_2019_thract_iot_typeindicator)+" OBJETOS CREADOS EN 2019, EL TIPO ES INDICADOR")
print("            -    EN  "+str(count_created_date_2019_thract_iot_typemarkingdefinition)+" OBJETOS CREADOS EN 2019, EL TIPO ES DEFINICION DE MARCADO ")
print("\n")
print("      -    EN  "+str(count_created_date_2018_thract_iot)+" OBJETOS LA FECHA DE CREACION ES 2018 O ANTERIOR. LAS ESTADÍSTICAS DE TIPO DE OBJETO SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(count_created_date_2018_thract_iot_typereport)+" OBJETOS CREADOS EN 2018 O ANTES, EL TIPO ES REPORTE ")
print("            -    EN  "+str(count_created_date_2018_thract_iot_typeindicator)+" OBJETOS CREADOS EN 2018 O ANTES, EL TIPO ES INDICADOR")
print("            -    EN  "+str(count_created_date_2018_thract_iot_typemarkingdefinition)+" OBJETOS CREADOS EN 2018 O ANTES, EL TIPO ES DEFINICION DE MARCADO ")
print("\n")
print("   - LAS ESTADISTICAS DE TIPO DE OBJETO SON LAS SIGUIENTES:  \n")
print("      -    EN  "+str(count_thract_iot_typereport)+" OBJETOS EL TIPO DE OBJETO ES REPORTE. LAS ESTADÍSTICAS DE FECHA DE CREACION SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(count_created_date_2023_thract_iot_typereport)+" OBJETOS LA FECHA DE CREACION ES 2023 ")
print("            -    EN  "+str(count_created_date_2022_thract_iot_typereport)+" OBJETOS LA FECHA DE CREACION ES 2022")
print("            -    EN  "+str(count_created_date_2021_thract_iot_typereport)+" OBJETOS LA FECHA DE CREACION ES 2021 ")
print("            -    EN  "+str(count_created_date_2020_thract_iot_typereport)+" OBJETOS LA FECHA DE CREACION ES 2020 ")
print("            -    EN  "+str(count_created_date_2019_thract_iot_typereport)+" OBJETOS LA FECHA DE CREACION ES 2019")
print("            -    EN  "+str(count_created_date_2018_thract_iot_typereport)+" OBJETOS LA FECHA DE CREACION ES 2018 O ANTERIOR ")
print("\n")
print("      -    EN  "+str(count_thract_iot_typeindicator)+" OBJETOS EL TIPO DE OBJETO ES INDICADOR. LAS ESTADÍSTICAS DE FECHA DE CREACION SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(count_created_date_2023_thract_iot_typeindicator)+" OBJETOS LA FECHA DE CREACION ES 2023 ")
print("            -    EN  "+str(count_created_date_2022_thract_iot_typeindicator)+" OBJETOS LA FECHA DE CREACION ES 2022")
print("            -    EN  "+str(count_created_date_2021_thract_iot_typeindicator)+" OBJETOS LA FECHA DE CREACION ES 2021 ")
print("            -    EN  "+str(count_created_date_2020_thract_iot_typeindicator)+" OBJETOS LA FECHA DE CREACION ES 2020 ")
print("            -    EN  "+str(count_created_date_2019_thract_iot_typeindicator)+" OBJETOS LA FECHA DE CREACION ES 2019")
print("            -    EN  "+str(count_created_date_2018_thract_iot_typeindicator)+" OBJETOS LA FECHA DE CREACION ES 2018 O ANTERIOR ")
print("\n")
print("      -    EN  "+str(count_thract_iot_typemarkingdefinition)+" OBJETOS EL TIPO DE OBJETO ES DEFINICION DE MARCADO. LAS ESTADÍSTICAS DE FECHA DE CREACION SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(count_created_date_2023_thract_iot_typemarkingdefinition)+" OBJETOS LA FECHA DE CREACION ES 2023 ")
print("            -    EN  "+str(count_created_date_2022_thract_iot_typemarkingdefinition)+" OBJETOS LA FECHA DE CREACION ES 2022")
print("            -    EN  "+str(count_created_date_2021_thract_iot_typemarkingdefinition)+" OBJETOS LA FECHA DE CREACION ES 2021 ")
print("            -    EN  "+str(count_created_date_2020_thract_iot_typemarkingdefinition)+" OBJETOS LA FECHA DE CREACION ES 2020 ")
print("            -    EN  "+str(count_created_date_2019_thract_iot_typemarkingdefinition)+" OBJETOS LA FECHA DE CREACION ES 2019")
print("            -    EN  "+str(count_created_date_2018_thract_iot_typemarkingdefinition)+" OBJETOS LA FECHA DE CREACION ES 2018 O ANTERIOR ")
print("\n")








print("***************************PORCENTAJE TIPO DE OBJETO/FECHA DE CREACIÓN INFORME ACTIVIDAD DE AMENAZAS IBM PARTE IOT***************************")
print("\n")                            
                
print("\n")
print(" DE UN TOTAL DE "+str(count_thract_iot_total)+" OBJETOS :\n") 
print("\n")
print("   - LOS PORCENTAJES DE FECHA DE CREACION SON LAS SIGUIENTES:  \n")
print("      -    EN EL  "+str(float(((count_created_date_2023_thract_iot*100)/count_thract_iot_total)))+" % DE OBJETOS LA FECHA DE CREACION ES 2023. LOS PORCENTAJES DE TIPO DE OBJETO SON LOS SIGUIENTES:  \n")
print("\n")
print("            -    EN EL  "+str(float(((count_created_date_2023_thract_iot_typereport*100)/count_created_date_2023_thract_iot)))+" % DE OBJETOS CREADOS EN 2023, EL TIPO ES REPORTE ")
print("            -    EN EL  "+str(float(((count_created_date_2023_thract_iot_typeindicator*100)/count_created_date_2023_thract_iot)))+" % DE OBJETOS CREADOS EN 2023, EL TIPO ES INDICADOR")
print("            -    EN EL  "+str(float(((count_created_date_2023_thract_iot_typemarkingdefinition*100)/count_created_date_2023_thract_iot)))+" % DE OBJETOS CREADOS EN 2023, EL TIPO ES DEFINICION DE MARCADO ")
print("\n")
print("      -    EN EL  "+str(float(((count_created_date_2022_thract_iot*100)/count_thract_iot_total)))+" % DE OBJETOS LA FECHA DE CREACION ES 2022. LOS PORCENTAJESS DE TIPO DE OBJETO SON LOS SIGUIENTES:  \n")
print("\n")
print("            -    EN EL  "+str(float(((count_created_date_2022_thract_iot_typereport*100)/count_created_date_2022_thract_iot)))+" % DE OBJETOS CREADOS EN 2022, EL TIPO ES REPORTE ")
print("            -    EN EL  "+str(float(((count_created_date_2022_thract_iot_typeindicator*100)/count_created_date_2022_thract_iot)))+" % DE OBJETOS CREADOS EN 2022, EL TIPO ES INDICADOR")
print("            -    EN EL  "+str(float(((count_created_date_2022_thract_iot_typemarkingdefinition*100)/count_created_date_2022_thract_iot)))+" % DE OBJETOS CREADOS EN 2022, EL TIPO ES DEFINICION DE MARCADO ")
print("\n")
print("      -    EN EL  "+str(float(((count_created_date_2021_thract_iot*100)/count_thract_iot_total)))+" % DE OBJETOS LA FECHA DE CREACION ES 2021. LOS PORCENTAJES DE TIPO DE OBJETO SON LOS SIGUIENTES:  \n")
print("\n")
print("            -    EN EL  "+str(float(((count_created_date_2021_thract_iot_typereport*100)/count_created_date_2021_thract_iot)))+" % DE OBJETOS CREADOS EN 2021, EL TIPO ES REPORTE ")
print("            -    EN EL  "+str(float(((count_created_date_2021_thract_iot_typeindicator*100)/count_created_date_2021_thract_iot)))+" % DE OBJETOS CREADOS EN 2021, EL TIPO ES INDICADOR")
print("            -    EN EL  "+str(float(((count_created_date_2021_thract_iot_typemarkingdefinition*100)/count_created_date_2021_thract_iot)))+" % DE OBJETOS CREADOS EN 2021, EL TIPO ES DEFINICION DE MARCADO ")
print("\n")
if(count_created_date_2020_thract_iot>0):
    print("      -    EN EL  "+str(float(((count_created_date_2020_thract_iot*100)/count_thract_iot_total)))+" % DE OBJETOS LA FECHA DE CREACION ES 2020. LOS PORCENTAJES DE TIPO DE OBJETO SON LOS SIGUIENTES:  \n")
    print("\n")
    print("            -    EN EL  "+str(float(((count_created_date_2020_thract_iot_typereport*100)/count_created_date_2020_thract_iot)))+" % DE OBJETOS CREADOS EN 2020, EL TIPO ES REPORTE ")
    print("            -    EN EL  "+str(float(((count_created_date_2020_thract_iot_typeindicator*100)/count_created_date_2020_thract_iot)))+" % DE OBJETOS CREADOS EN 2020, EL TIPO ES INDICADOR")
    print("            -    EN EL  "+str(float(((count_created_date_2020_thract_iot_typemarkingdefinition*100)/count_created_date_2020_thract_iot)))+" % DE OBJETOS CREADOS EN 2020, EL TIPO ES DEFINICION DE MARCADO ")
    print("\n")
if(count_created_date_2019_thract_iot>0):
    print("      -    EN EL  "+str(float(((count_created_date_2019_thract_iot*100)/count_thract_iot_total)))+" % DE OBJETOS LA FECHA DE CREACION ES 2019. LOS PORCENTAJES DE TIPO DE OBJETO SON LOS SIGUIENTES:  \n")
    print("\n")
    print("            -    EN EL  "+str(float(((count_created_date_2019_thract_iot_typereport*100)/count_created_date_2019_thract_iot)))+" % DE OBJETOS CREADOS EN 2019, EL TIPO ES REPORTE ")
    print("            -    EN EL  "+str(float(((count_created_date_2019_thract_iot_typeindicator*100)/count_created_date_2019_thract_iot)))+" % DE OBJETOS CREADOS EN 2019, EL TIPO ES INDICADOR")
    print("            -    EN EL  "+str(float(((count_created_date_2019_thract_iot_typemarkingdefinition*100)/count_created_date_2019_thract_iot)))+" % DE OBJETOS CREADOS EN 2019, EL TIPO ES DEFINICION DE MARCADO ")
    print("\n")
if(count_created_date_2018_thract_iot>0):
    print("      -    EN EL  "+str(float(((count_created_date_2018_thract_iot*100)/count_thract_iot_total)))+" % DE OBJETOS LA FECHA DE CREACION ES 2018 O ANTERIOR. LOS PORCENTAJES DE TIPO DE OBJETO SON LOS SIGUIENTES:  \n")
    print("\n")
    print("            -    EN EL  "+str(float(((count_created_date_2018_thract_iot_typereport*100)/count_created_date_2018_thract_iot)))+" % DE OBJETOS CREADOS EN 2018 O ANTERIORMENTE, EL TIPO ES REPORTE ")
    print("            -    EN EL  "+str(float(((count_created_date_2018_thract_iot_typeindicator*100)/count_created_date_2018_thract_iot)))+" % DE OBJETOS CREADOS EN 2018 O ANTERIORMENTE, EL TIPO ES INDICADOR")
    print("            -    EN EL  "+str(float(((count_created_date_2018_thract_iot_typemarkingdefinition*100)/count_created_date_2018_thract_iot)))+" % DE OBJETOS CREADOS EN 2018 O ANTERIORMENTE, EL TIPO ES DEFINICION DE MARCADO ")
    print("\n")
print("   - LOS PORCENTAJES DE TIPO DE OBJETO SON LOS SIGUIENTES:  \n")
print("      -    EN EL  "+str(float(((count_thract_iot_typereport*100)/count_thract_iot_total)))+" % DE OBJETOS EL TIPO DE OBJETO ES REPORTE. LOS PORCENTAJES DE FECHA DE CREACION SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN EL  "+str(float(((count_created_date_2023_thract_iot_typereport*100)/count_thract_iot_typereport)))+" % DE OBJETOS LA FECHA DE CREACION ES 2023 ")
print("            -    EN EL  "+str(float(((count_created_date_2022_thract_iot_typereport*100)/count_thract_iot_typereport)))+" % DE OBJETOS LA FECHA DE CREACION ES 2022")
print("            -    EN EL  "+str(float(((count_created_date_2021_thract_iot_typereport*100)/count_thract_iot_typereport)))+" % DE OBJETOS LA FECHA DE CREACION ES 2021 ")
print("            -    EN EL  "+str(float(((count_created_date_2020_thract_iot_typereport*100)/count_thract_iot_typereport)))+" % DE OBJETOS LA FECHA DE CREACION ES 2020 ")
print("            -    EN EL  "+str(float(((count_created_date_2019_thract_iot_typereport*100)/count_thract_iot_typereport)))+" % DE OBJETOS LA FECHA DE CREACION ES 2019")
print("            -    EN EL  "+str(float(((count_created_date_2018_thract_iot_typereport*100)/count_thract_iot_typereport)))+" % DE OBJETOS LA FECHA DE CREACION ES 2018 O ANTERIOR ")
print("\n")
print("      -    EN EL  "+str(float(((count_thract_iot_typeindicator*100)/count_thract_iot_total)))+" % DE OBJETOS EL TIPO DE OBJETO ES INDICADOR. LOS PORCENTAJES DE FECHA DE CREACION SON LOS SIGUIENTES:  \n")
print("\n")
print("            -    EN EL  "+str(float(((count_created_date_2023_thract_iot_typeindicator*100)/count_thract_iot_typeindicator)))+" % DE OBJETOS LA FECHA DE CREACION ES 2023 ")
print("            -    EN EL  "+str(float(((count_created_date_2022_thract_iot_typeindicator*100)/count_thract_iot_typeindicator)))+" % DE OBJETOS LA FECHA DE CREACION ES 2022")
print("            -    EN EL  "+str(float(((count_created_date_2021_thract_iot_typeindicator*100)/count_thract_iot_typeindicator)))+" % DE OBJETOS LA FECHA DE CREACION ES 2021 ")
print("            -    EN EL  "+str(float(((count_created_date_2020_thract_iot_typeindicator*100)/count_thract_iot_typeindicator)))+" % DE OBJETOS LA FECHA DE CREACION ES 2020 ")
print("            -    EN EL  "+str(float(((count_created_date_2019_thract_iot_typeindicator*100)/count_thract_iot_typeindicator)))+" % DE OBJETOS LA FECHA DE CREACION ES 2019")
print("            -    EN EL  "+str(float(((count_created_date_2018_thract_iot_typeindicator*100)/count_thract_iot_typeindicator)))+" % DE OBJETOS LA FECHA DE CREACION ES 2018 O ANTERIOR ")
print("\n")
print("      -    EN EL  "+str(float(((count_thract_iot_typemarkingdefinition*100)/count_thract_iot_total)))+" % DE OBJETOS EL TIPO DE OBJETO ES DEFINICION DE MARCADO. LOS PORCENTAJES DE FECHA DE CREACION SON LOS SIGUIENTES:  \n")
print("\n")
print("            -    EN EL  "+str(float(((count_created_date_2023_thract_iot_typemarkingdefinition*100)/count_thract_iot_typemarkingdefinition)))+" % DE OBJETOS LA FECHA DE CREACION ES 2023 ")
print("            -    EN EL  "+str(float(((count_created_date_2022_thract_iot_typemarkingdefinition*100)/count_thract_iot_typemarkingdefinition)))+" % DE OBJETOS LA FECHA DE CREACION ES 2022")
print("            -    EN EL  "+str(float(((count_created_date_2021_thract_iot_typemarkingdefinition*100)/count_thract_iot_typemarkingdefinition)))+" % DE OBJETOS LA FECHA DE CREACION ES 2021 ")
print("            -    EN EL  "+str(float(((count_created_date_2020_thract_iot_typemarkingdefinition*100)/count_thract_iot_typemarkingdefinition)))+" % DE OBJETOS LA FECHA DE CREACION ES 2020 ")
print("            -    EN EL  "+str(float(((count_created_date_2019_thract_iot_typemarkingdefinition*100)/count_thract_iot_typemarkingdefinition)))+" % DE OBJETOS LA FECHA DE CREACION ES 2019")
print("            -    EN EL  "+str(float(((count_created_date_2018_thract_iot_typemarkingdefinition*100)/count_thract_iot_typemarkingdefinition)))+" % DE OBJETOS LA FECHA DE CREACION ES 2018 O ANTERIOR ")
print("\n")









df_thract_sh = pd.read_excel('ibm_threat_activity_report_smarthome_2023.xlsx')





#Variables donde almacenare el contador de tipo segun el anio de creacion
count_created_date_2023_thract_sh_typereport=0
count_created_date_2023_thract_sh_typeindicator=0
count_created_date_2023_thract_sh_typemarkingdefinition=0
#Variables donde almacenare el contador de anio de creacion 
count_created_date_2023_thract_sh=0

count_created_date_2022_thract_sh_typereport=0
count_created_date_2022_thract_sh_typeindicator=0
count_created_date_2022_thract_sh_typemarkingdefinition=0
count_created_date_2022_thract_sh=0


count_created_date_2021_thract_sh_typereport=0
count_created_date_2021_thract_sh_typeindicator=0
count_created_date_2021_thract_sh_typemarkingdefinition=0
count_created_date_2021_thract_sh=0


count_created_date_2020_thract_sh_typereport=0
count_created_date_2020_thract_sh_typeindicator=0
count_created_date_2020_thract_sh_typemarkingdefinition=0
count_created_date_2020_thract_sh=0


count_created_date_2019_thract_sh_typereport=0
count_created_date_2019_thract_sh_typeindicator=0
count_created_date_2019_thract_sh_typemarkingdefinition=0
count_created_date_2019_thract_sh=0


count_created_date_2018_thract_sh_typereport=0
count_created_date_2018_thract_sh_typeindicator=0
count_created_date_2018_thract_sh_typemarkingdefinition=0
count_created_date_2018_thract_sh=0

count_thract_sh_typereport=0
count_thract_sh_typeindicator=0
count_thract_sh_typemarkingdefinition=0

#Contador de OBJETOs totales
count_thract_sh_total=0


#Comprobamos el anio de creacion 
for r in range(0,len(df_thract_sh["created"])):
    #Si existen varios valores para una misma fila
    if('[' in df_thract_sh["created"][r]):
        #Obtengo los valores de fecha de creacion
        aux=df_thract_sh["created"][r].split(",")
        #Recorro los distintos valores de la misma fila
        for l in range(0,len(aux)):
            if(len(aux)>0):
                aux_str=aux[l].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
                if(aux_str!='NONE'):
                    #Obtengo el anio de creacion
                    count_thract_sh_total+=1
                    str_anio_publishdate_thract_sh=aux_str.split("-")
                    anio_publishdate_thract_sh=int(str_anio_publishdate_thract_sh[0])
                    #Compruebo el anio de creacion
                    if(anio_publishdate_thract_sh >= 2023):
                        count_created_date_2023_thract_sh+=1
                        #Obtengo los distintos valores de tipo en la fila actual
                        auxx=df_thract_sh["type"][r].split(",")
                        #Obtengo los valores individuales de tipo en la fila actual
                        auxx_str=auxx[l].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
                        #Compruebo el tipo
                        if(auxx_str == 'report'):
                            count_thract_sh_typereport+=1
                            count_created_date_2023_thract_sh_typereport+=1
                        elif(auxx_str == 'indicator'):
                            count_thract_sh_typeindicator+=1
                            count_created_date_2023_thract_sh_typeindicator+=1
                        elif(auxx_str == 'marking-definition'):
                            count_thract_sh_typemarkingdefinition+=1
                            count_created_date_2023_thract_sh_typemarkingdefinition+=1 
                                 
                                
                    elif(anio_publishdate_thract_sh >= 2022):
                        count_created_date_2022_thract_sh+=1
                        auxx=df_thract_sh["type"][r].split(",")
                        auxx_str=auxx[l].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
                        if(auxx_str == 'report'):
                            count_thract_sh_typereport+=1
                            count_created_date_2022_thract_sh_typereport+=1
                        elif(auxx_str == 'indicator'):
                            count_thract_sh_typeindicator+=1
                            count_created_date_2022_thract_sh_typeindicator+=1
                        elif(auxx_str == 'marking-definition'):
                            count_thract_sh_typemarkingdefinition+=1
                            count_created_date_2022_thract_sh_typemarkingdefinition+=1 
                                
                    elif(anio_publishdate_thract_sh >= 2021):
                        count_created_date_2021_thract_sh+=1
                        auxx=df_thract_sh["type"][r].split(",")
                        auxx_str=auxx[l].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
                        if(auxx_str == 'report'):
                            count_thract_sh_typereport+=1
                            count_created_date_2021_thract_sh_typereport+=1
                        elif(auxx_str == 'indicator'):
                            count_thract_sh_typeindicator+=1
                            count_created_date_2021_thract_sh_typeindicator+=1
                        elif(auxx_str == 'marking-definition'):
                            count_thract_sh_typemarkingdefinition+=1
                            count_created_date_2021_thract_sh_typemarkingdefinition+=1 
                                
                    elif(anio_publishdate_thract_sh >= 2020):
                        count_created_date_2020_thract_sh+=1
                        auxx=df_thract_sh["type"][r].split(",")
                        auxx_str=auxx[l].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
                        if(auxx_str == 'report'):
                            count_thract_sh_typereport+=1
                            count_created_date_2020_thract_sh_typereport+=1
                        elif(auxx_str == 'indicator'):
                            count_thract_sh_typeindicator+=1
                            count_created_date_2020_thract_sh_typeindicator+=1
                        elif(auxx_str == 'marking-definition'):
                            count_thract_sh_typemarkingdefinition+=1
                            count_created_date_2020_thract_sh_typemarkingdefinition+=1 
                                
                                
                    elif(anio_publishdate_thract_sh >= 2019):
                        count_created_date_2019_thract_sh+=1
                        auxx=df_thract_sh["type"][r].split(",")
                        auxx_str=auxx[l].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
                        if(auxx_str == 'report'):
                            count_thract_sh_typereport+=1
                            count_created_date_2019_thract_sh_typereport+=1
                        elif(auxx_str == 'indicator'):
                            count_thract_sh_typeindicator+=1
                            count_created_date_2019_thract_sh_typeindicator+=1
                        elif(auxx_str == 'marking-definition'):
                            count_thract_sh_typemarkingdefinition+=1
                            count_created_date_2019_thract_sh_typemarkingdefinition+=1 
                                
                                
                    else: 
                        count_created_date_2018_thract_sh+=1
                        auxx=df_thract_sh["type"][r].split(",")
                        auxx_str=auxx[l].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
                        if(auxx_str == 'report'):
                            count_thract_sh_typereport+=1
                            count_created_date_2018_thract_sh_typereport+=1
                        elif(auxx_str == 'indicator'):
                            count_thract_sh_typeindicator+=1
                            count_created_date_2018_thract_sh_typeindicator+=1
                        elif(auxx_str == 'marking-definition'):
                            count_thract_sh_typemarkingdefinition+=1
                            count_created_date_2018_thract_sh_typemarkingdefinition+=1
    else:
        #Si existe un unico valor de fecha de creacion y tipo para la fila actual
        str_anio_publishdate_thract_sh=df_thract_sh["created"][r].split("-")
        anio_publishdate_thract_sh=int(str_anio_publishdate_thract_sh[0])
        count_thract_sh_total+=1
        #Compruebo el anio de creacion
        if(anio_publishdate_thract_sh >= 2023):
            count_created_date_2023_thract_sh+=1
            #Compruebo el tipo de OBJETO
            if(df_thract_sh["type"][r] == 'report'):
                count_thract_sh_typereport+=1
                count_created_date_2023_thract_sh_typereport+=1  
            elif(df_thract_sh["type"][r] == 'indicator'):
                count_thract_sh_typeindicator+=1
                count_created_date_2023_thract_sh_typeindicator+=1  
            elif(df_thract_sh["type"][r] == 'marking-definition'):
                count_thract_sh_typemarkingdefinition+=1
                count_created_date_2023_thract_sh_typemarkingdefinition+=1
                
        elif(anio_publishdate_thract_sh >= 2022):
            count_created_date_2022_thract_sh+=1
            if(df_thract_sh["type"][r] == 'report'):
                count_thract_sh_typereport+=1
                count_created_date_2022_thract_sh_typereport+=1  
            elif(df_thract_sh["type"][r] == 'indicator'):
                count_thract_sh_typeindicator+=1
                count_created_date_2022_thract_sh_typeindicator+=1  
            elif(df_thract_sh["type"][r] == 'marking-definition'):
                count_thract_sh_typemarkingdefinition+=1
                count_created_date_2022_thract_sh_typemarkingdefinition+=1
        elif(anio_publishdate_thract_sh >= 2021):
            count_created_date_2021_thract_sh+=1
            if(df_thract_sh["type"][r] == 'report'):
                count_thract_sh_typereport+=1
                count_created_date_2021_thract_sh_typereport+=1  
            elif(df_thract_sh["type"][r] == 'indicator'):
                count_thract_sh_typeindicator+=1
                count_created_date_2021_thract_sh_typeindicator+=1  
            elif(df_thract_sh["type"][r] == 'marking-definition'):
                count_thract_sh_typemarkingdefinition+=1
                count_created_date_2021_thract_sh_typemarkingdefinition+=1
        elif(anio_publishdate_thract_sh >= 2020):
            count_created_date_2020_thract_sh+=1
            if(df_thract_sh["type"][r] == 'report'):
                count_thract_sh_typereport+=1
                count_created_date_2020_thract_sh_typereport+=1  
            elif(df_thract_sh["type"][r] == 'indicator'):
                count_thract_sh_typeindicator+=1
                count_created_date_2020_thract_sh_typeindicator+=1  
            elif(df_thract_sh["type"][r] == 'marking-definition'):
                count_thract_sh_typemarkingdefinition+=1
                count_created_date_2020_thract_sh_typemarkingdefinition+=1
        elif(anio_publishdate_thract_sh >= 2019):
            count_created_date_2019_thract_sh+=1
            if(df_thract_sh["type"][r] == 'report'):
                count_thract_sh_typereport+=1
                count_created_date_2019_thract_sh_typereport+=1  
            elif(df_thract_sh["type"][r] == 'indicator'):
                count_thract_sh_typeindicator+=1
                count_created_date_2019_thract_sh_typeindicator+=1  
            elif(df_thract_sh["type"][r] == 'marking-definition'):
                count_thract_sh_typemarkingdefinition+=1
                count_created_date_2019_thract_sh_typemarkingdefinition+=1
        else:
            count_created_date_2018_thract_sh+=1
            if(df_thract_sh["type"][r] == 'report'):
                count_thract_sh_typereport+=1
                count_created_date_2018_thract_sh_typereport+=1  
            elif(df_thract_sh["type"][r] == 'indicator'):
                count_thract_sh_typeindicator+=1
                count_created_date_2018_thract_sh_typeindicator+=1  
            elif(df_thract_sh["type"][r] == 'marking-definition'):
                count_thract_sh_typemarkingdefinition+=1
                count_created_date_2018_thract_sh_typemarkingdefinition+=1
                
                
print("***************************ESTADÍSTICAS TIPO DE OBJETO/FECHA DE CREACIÓN INFORME ACTIVIDAD DE AMENAZAS IBM PARTE SMART HOME***************************")
print("\n")                            
                
print("\n")
print(" DE UN TOTAL DE "+str(count_thract_sh_total)+" OBJETOS :\n") 
print("\n")
print("   - LAS ESTADISTICAS DE FECHA DE CREACION SON LAS SIGUIENTES:  \n")
print("      -    EN  "+str(count_created_date_2023_thract_sh)+" OBJETOS LA FECHA DE CREACION ES 2023. LAS ESTADÍSTICAS DE TIPO DE OBJETO SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(count_created_date_2023_thract_sh_typereport)+" OBJETOS CREADOS EN 2023, EL TIPO ES REPORTE ")
print("            -    EN  "+str(count_created_date_2023_thract_sh_typeindicator)+" OBJETOS CREADOS EN 2023, EL TIPO ES INDICADOR")
print("            -    EN  "+str(count_created_date_2023_thract_sh_typemarkingdefinition)+" OBJETOS CREADOS EN 2023, EL TIPO ES DEFINICION DE MARCADO ")
print("\n")
print("      -    EN  "+str(count_created_date_2022_thract_sh)+" OBJETOS LA FECHA DE CREACION ES 2022. LAS ESTADÍSTICAS DE TIPO DE OBJETO SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(count_created_date_2022_thract_sh_typereport)+" OBJETOS CREADOS EN 2022, EL TIPO ES REPORTE ")
print("            -    EN  "+str(count_created_date_2022_thract_sh_typeindicator)+" OBJETOS CREADOS EN 2022, EL TIPO ES INDICADOR")
print("            -    EN  "+str(count_created_date_2022_thract_sh_typemarkingdefinition)+" OBJETOS CREADOS EN 2022, EL TIPO ES DEFINICION DE MARCADO ")
print("\n")
print("      -    EN  "+str(count_created_date_2021_thract_sh)+" OBJETOS LA FECHA DE CREACION ES 2021. LAS ESTADÍSTICAS DE TIPO DE OBJETO SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(count_created_date_2021_thract_sh_typereport)+" OBJETOS CREADOS EN 2021, EL TIPO ES REPORTE ")
print("            -    EN  "+str(count_created_date_2021_thract_sh_typeindicator)+" OBJETOS CREADOS EN 2021, EL TIPO ES INDICADOR")
print("            -    EN  "+str(count_created_date_2021_thract_sh_typemarkingdefinition)+" OBJETOS CREADOS EN 2021, EL TIPO ES DEFINICION DE MARCADO ")
print("\n")
print("      -    EN  "+str(count_created_date_2020_thract_sh)+" OBJETOS LA FECHA DE CREACION ES 2020. LAS ESTADÍSTICAS DE TIPO DE OBJETO SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(count_created_date_2020_thract_sh_typereport)+" OBJETOS CREADOS EN 2020, EL TIPO ES REPORTE ")
print("            -    EN  "+str(count_created_date_2020_thract_sh_typeindicator)+" OBJETOS CREADOS EN 2020, EL TIPO ES INDICADOR")
print("            -    EN  "+str(count_created_date_2020_thract_sh_typemarkingdefinition)+" OBJETOS CREADOS EN 2020, EL TIPO ES DEFINICION DE MARCADO ")
print("\n")
print("      -    EN  "+str(count_created_date_2019_thract_sh)+" OBJETOS LA FECHA DE CREACION ES 2019. LAS ESTADÍSTICAS DE TIPO DE OBJETO SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(count_created_date_2019_thract_sh_typereport)+" OBJETOS CREADOS EN 2019, EL TIPO ES REPORTE ")
print("            -    EN  "+str(count_created_date_2019_thract_sh_typeindicator)+" OBJETOS CREADOS EN 2019, EL TIPO ES INDICADOR")
print("            -    EN  "+str(count_created_date_2019_thract_sh_typemarkingdefinition)+" OBJETOS CREADOS EN 2019, EL TIPO ES DEFINICION DE MARCADO ")
print("\n")
print("      -    EN  "+str(count_created_date_2018_thract_sh)+" OBJETOS LA FECHA DE CREACION ES 2018 O ANTERIOR. LAS ESTADÍSTICAS DE TIPO DE OBJETO SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(count_created_date_2018_thract_sh_typereport)+" OBJETOS CREADOS EN 2018 O ANTES, EL TIPO ES REPORTE ")
print("            -    EN  "+str(count_created_date_2018_thract_sh_typeindicator)+" OBJETOS CREADOS EN 2018 O ANTES, EL TIPO ES INDICADOR")
print("            -    EN  "+str(count_created_date_2018_thract_sh_typemarkingdefinition)+" OBJETOS CREADOS EN 2018 O ANTES, EL TIPO ES DEFINICION DE MARCADO ")
print("\n")
print("   - LAS ESTADISTICAS DE TIPO DE OBJETO SON LAS SIGUIENTES:  \n")
print("      -    EN  "+str(count_thract_sh_typereport)+" OBJETOS EL TIPO DE OBJETO ES REPORTE. LAS ESTADÍSTICAS DE FECHA DE CREACION SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(count_created_date_2023_thract_sh_typereport)+" OBJETOS LA FECHA DE CREACION ES 2023 ")
print("            -    EN  "+str(count_created_date_2022_thract_sh_typereport)+" OBJETOS LA FECHA DE CREACION ES 2022")
print("            -    EN  "+str(count_created_date_2021_thract_sh_typereport)+" OBJETOS LA FECHA DE CREACION ES 2021 ")
print("            -    EN  "+str(count_created_date_2020_thract_sh_typereport)+" OBJETOS LA FECHA DE CREACION ES 2020 ")
print("            -    EN  "+str(count_created_date_2019_thract_sh_typereport)+" OBJETOS LA FECHA DE CREACION ES 2019")
print("            -    EN  "+str(count_created_date_2018_thract_sh_typereport)+" OBJETOS LA FECHA DE CREACION ES 2018 O ANTERIOR ")
print("\n")
print("      -    EN  "+str(count_thract_sh_typeindicator)+" OBJETOS EL TIPO DE OBJETO ES INDICADOR. LAS ESTADÍSTICAS DE FECHA DE CREACION SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(count_created_date_2023_thract_sh_typeindicator)+" OBJETOS LA FECHA DE CREACION ES 2023 ")
print("            -    EN  "+str(count_created_date_2022_thract_sh_typeindicator)+" OBJETOS LA FECHA DE CREACION ES 2022")
print("            -    EN  "+str(count_created_date_2021_thract_sh_typeindicator)+" OBJETOS LA FECHA DE CREACION ES 2021 ")
print("            -    EN  "+str(count_created_date_2020_thract_sh_typeindicator)+" OBJETOS LA FECHA DE CREACION ES 2020 ")
print("            -    EN  "+str(count_created_date_2019_thract_sh_typeindicator)+" OBJETOS LA FECHA DE CREACION ES 2019")
print("            -    EN  "+str(count_created_date_2018_thract_sh_typeindicator)+" OBJETOS LA FECHA DE CREACION ES 2018 O ANTERIOR ")
print("\n")
print("      -    EN  "+str(count_thract_sh_typemarkingdefinition)+" OBJETOS EL TIPO DE OBJETO ES DEFINICION DE MARCADO. LAS ESTADÍSTICAS DE FECHA DE CREACION SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(count_created_date_2023_thract_sh_typemarkingdefinition)+" OBJETOS LA FECHA DE CREACION ES 2023 ")
print("            -    EN  "+str(count_created_date_2022_thract_sh_typemarkingdefinition)+" OBJETOS LA FECHA DE CREACION ES 2022")
print("            -    EN  "+str(count_created_date_2021_thract_sh_typemarkingdefinition)+" OBJETOS LA FECHA DE CREACION ES 2021 ")
print("            -    EN  "+str(count_created_date_2020_thract_sh_typemarkingdefinition)+" OBJETOS LA FECHA DE CREACION ES 2020 ")
print("            -    EN  "+str(count_created_date_2019_thract_sh_typemarkingdefinition)+" OBJETOS LA FECHA DE CREACION ES 2019")
print("            -    EN  "+str(count_created_date_2018_thract_sh_typemarkingdefinition)+" OBJETOS LA FECHA DE CREACION ES 2018 O ANTERIOR ")
print("\n")








print("***************************PORCENTAJE TIPO DE OBJETO/FECHA DE CREACIÓN INFORME ACTIVIDAD DE AMENAZAS IBM PARTE SMART HOME***************************")
print("\n")                            
                
print("\n")
print(" DE UN TOTAL DE "+str(count_thract_sh_total)+" OBJETOS :\n") 
print("\n")
print("   - LOS PORCENTAJES DE FECHA DE CREACION SON LAS SIGUIENTES:  \n")
print("      -    EN EL  "+str(float(((count_created_date_2023_thract_sh*100)/count_thract_sh_total)))+" % DE OBJETOS LA FECHA DE CREACION ES 2023. LOS PORCENTAJES DE TIPO DE OBJETO SON LOS SIGUIENTES:  \n")
print("\n")
print("            -    EN EL  "+str(float(((count_created_date_2023_thract_sh_typereport*100)/count_created_date_2023_thract_sh)))+" % DE OBJETOS CREADOS EN 2023, EL TIPO ES REPORTE ")
print("            -    EN EL  "+str(float(((count_created_date_2023_thract_sh_typeindicator*100)/count_created_date_2023_thract_sh)))+" % DE OBJETOS CREADOS EN 2023, EL TIPO ES INDICADOR")
print("            -    EN EL  "+str(float(((count_created_date_2023_thract_sh_typemarkingdefinition*100)/count_created_date_2023_thract_sh)))+" % DE OBJETOS CREADOS EN 2023, EL TIPO ES DEFINICION DE MARCADO ")
print("\n")
print("      -    EN EL  "+str(float(((count_created_date_2022_thract_sh*100)/count_thract_sh_total)))+" % DE OBJETOS LA FECHA DE CREACION ES 2022. LOS PORCENTAJESS DE TIPO DE OBJETO SON LOS SIGUIENTES:  \n")
print("\n")
print("            -    EN EL  "+str(float(((count_created_date_2022_thract_sh_typereport*100)/count_created_date_2022_thract_sh)))+" % DE OBJETOS CREADOS EN 2022, EL TIPO ES REPORTE ")
print("            -    EN EL  "+str(float(((count_created_date_2022_thract_sh_typeindicator*100)/count_created_date_2022_thract_sh)))+" % DE OBJETOS CREADOS EN 2022, EL TIPO ES INDICADOR")
print("            -    EN EL  "+str(float(((count_created_date_2022_thract_sh_typemarkingdefinition*100)/count_created_date_2022_thract_sh)))+" % DE OBJETOS CREADOS EN 2022, EL TIPO ES DEFINICION DE MARCADO ")
print("\n")
print("      -    EN EL  "+str(float(((count_created_date_2021_thract_sh*100)/count_thract_sh_total)))+" % DE OBJETOS LA FECHA DE CREACION ES 2021. LOS PORCENTAJES DE TIPO DE OBJETO SON LOS SIGUIENTES:  \n")
print("\n")
print("            -    EN EL  "+str(float(((count_created_date_2021_thract_sh_typereport*100)/count_created_date_2021_thract_sh)))+" % DE OBJETOS CREADOS EN 2021, EL TIPO ES REPORTE ")
print("            -    EN EL  "+str(float(((count_created_date_2021_thract_sh_typeindicator*100)/count_created_date_2021_thract_sh)))+" % DE OBJETOS CREADOS EN 2021, EL TIPO ES INDICADOR")
print("            -    EN EL  "+str(float(((count_created_date_2021_thract_sh_typemarkingdefinition*100)/count_created_date_2021_thract_sh)))+" % DE OBJETOS CREADOS EN 2021, EL TIPO ES DEFINICION DE MARCADO ")
print("\n")
if(count_created_date_2020_thract_sh>0):
    print("      -    EN EL  "+str(float(((count_created_date_2020_thract_sh*100)/count_thract_sh_total)))+" % DE OBJETOS LA FECHA DE CREACION ES 2020. LOS PORCENTAJES DE TIPO DE OBJETO SON LOS SIGUIENTES:  \n")
    print("\n")
    print("            -    EN EL  "+str(float(((count_created_date_2020_thract_sh_typereport*100)/count_created_date_2020_thract_sh)))+" % DE OBJETOS CREADOS EN 2020, EL TIPO ES REPORTE ")
    print("            -    EN EL  "+str(float(((count_created_date_2020_thract_sh_typeindicator*100)/count_created_date_2020_thract_sh)))+" % DE OBJETOS CREADOS EN 2020, EL TIPO ES INDICADOR")
    print("            -    EN EL  "+str(float(((count_created_date_2020_thract_sh_typemarkingdefinition*100)/count_created_date_2020_thract_sh)))+" % DE OBJETOS CREADOS EN 2020, EL TIPO ES DEFINICION DE MARCADO ")
    print("\n")
if(count_created_date_2019_thract_sh>0):
    print("      -    EN EL  "+str(float(((count_created_date_2019_thract_sh*100)/count_thract_sh_total)))+" % DE OBJETOS LA FECHA DE CREACION ES 2019. LOS PORCENTAJES DE TIPO DE OBJETO SON LOS SIGUIENTES:  \n")
    print("\n")
    print("            -    EN EL  "+str(float(((count_created_date_2019_thract_sh_typereport*100)/count_created_date_2019_thract_sh)))+" % DE OBJETOS CREADOS EN 2019, EL TIPO ES REPORTE ")
    print("            -    EN EL  "+str(float(((count_created_date_2019_thract_sh_typeindicator*100)/count_created_date_2019_thract_sh)))+" % DE OBJETOS CREADOS EN 2019, EL TIPO ES INDICADOR")
    print("            -    EN EL  "+str(float(((count_created_date_2019_thract_sh_typemarkingdefinition*100)/count_created_date_2019_thract_sh)))+" % DE OBJETOS CREADOS EN 2019, EL TIPO ES DEFINICION DE MARCADO ")
    print("\n")
if(count_created_date_2018_thract_sh>0):
    print("      -    EN EL  "+str(float(((count_created_date_2018_thract_sh*100)/count_thract_sh_total)))+" % DE OBJETOS LA FECHA DE CREACION ES 2018 O ANTERIOR. LOS PORCENTAJES DE TIPO DE OBJETO SON LOS SIGUIENTES:  \n")
    print("\n")
    print("            -    EN EL  "+str(float(((count_created_date_2018_thract_sh_typereport*100)/count_created_date_2018_thract_sh)))+" % DE OBJETOS CREADOS EN 2018 O ANTERIORMENTE, EL TIPO ES REPORTE ")
    print("            -    EN EL  "+str(float(((count_created_date_2018_thract_sh_typeindicator*100)/count_created_date_2018_thract_sh)))+" % DE OBJETOS CREADOS EN 2018 O ANTERIORMENTE, EL TIPO ES INDICADOR")
    print("            -    EN EL  "+str(float(((count_created_date_2018_thract_sh_typemarkingdefinition*100)/count_created_date_2018_thract_sh)))+" % DE OBJETOS CREADOS EN 2018 O ANTERIORMENTE, EL TIPO ES DEFINICION DE MARCADO ")
    print("\n")
print("   - LOS PORCENTAJES DE TIPO DE OBJETO SON LOS SIGUIENTES:  \n")
if(count_thract_sh_total>0):
    print("      -    EN EL  "+str(float(((count_thract_sh_typereport*100)/count_thract_sh_total)))+" % DE OBJETOS EL TIPO DE OBJETO ES REPORTE. LOS PORCENTAJES DE FECHA DE CREACION SON LAS SIGUIENTES:  \n")
    print("\n")
    print("            -    EN EL  "+str(float(((count_created_date_2023_thract_sh_typereport*100)/count_thract_sh_typereport)))+" % DE OBJETOS LA FECHA DE CREACION ES 2023 ")
    print("            -    EN EL  "+str(float(((count_created_date_2022_thract_sh_typereport*100)/count_thract_sh_typereport)))+" % DE OBJETOS LA FECHA DE CREACION ES 2022")
    print("            -    EN EL  "+str(float(((count_created_date_2021_thract_sh_typereport*100)/count_thract_sh_typereport)))+" % DE OBJETOS LA FECHA DE CREACION ES 2021 ")
    print("            -    EN EL  "+str(float(((count_created_date_2020_thract_sh_typereport*100)/count_thract_sh_typereport)))+" % DE OBJETOS LA FECHA DE CREACION ES 2020 ")
    print("            -    EN EL  "+str(float(((count_created_date_2019_thract_sh_typereport*100)/count_thract_sh_typereport)))+" % DE OBJETOS LA FECHA DE CREACION ES 2019")
    print("            -    EN EL  "+str(float(((count_created_date_2018_thract_sh_typereport*100)/count_thract_sh_typereport)))+" % DE OBJETOS LA FECHA DE CREACION ES 2018 O ANTERIOR ")
    print("\n")
if(count_thract_sh_typeindicator>0):
    print("      -    EN EL  "+str(float(((count_thract_sh_typeindicator*100)/count_thract_sh_total)))+" % DE OBJETOS EL TIPO DE OBJETO ES INDICADOR. LOS PORCENTAJES DE FECHA DE CREACION SON LOS SIGUIENTES:  \n")
    print("\n")
    print("            -    EN EL  "+str(float(((count_created_date_2023_thract_sh_typeindicator*100)/count_thract_sh_typeindicator)))+" % DE OBJETOS LA FECHA DE CREACION ES 2023 ")
    print("            -    EN EL  "+str(float(((count_created_date_2022_thract_sh_typeindicator*100)/count_thract_sh_typeindicator)))+" % DE OBJETOS LA FECHA DE CREACION ES 2022")
    print("            -    EN EL  "+str(float(((count_created_date_2021_thract_sh_typeindicator*100)/count_thract_sh_typeindicator)))+" % DE OBJETOS LA FECHA DE CREACION ES 2021 ")
    print("            -    EN EL  "+str(float(((count_created_date_2020_thract_sh_typeindicator*100)/count_thract_sh_typeindicator)))+" % DE OBJETOS LA FECHA DE CREACION ES 2020 ")
    print("            -    EN EL  "+str(float(((count_created_date_2019_thract_sh_typeindicator*100)/count_thract_sh_typeindicator)))+" % DE OBJETOS LA FECHA DE CREACION ES 2019")
    print("            -    EN EL  "+str(float(((count_created_date_2018_thract_sh_typeindicator*100)/count_thract_sh_typeindicator)))+" % DE OBJETOS LA FECHA DE CREACION ES 2018 O ANTERIOR ")
    print("\n")
if(count_thract_sh_typemarkingdefinition>0):
    print("      -    EN EL  "+str(float(((count_thract_sh_typemarkingdefinition*100)/count_thract_sh_total)))+" % DE OBJETOS EL TIPO DE OBJETO ES DEFINICION DE MARCADO. LOS PORCENTAJES DE FECHA DE CREACION SON LOS SIGUIENTES:  \n")
    print("\n")
    print("            -    EN EL  "+str(float(((count_created_date_2023_thract_sh_typemarkingdefinition*100)/count_thract_sh_typemarkingdefinition)))+" % DE OBJETOS LA FECHA DE CREACION ES 2023 ")
    print("            -    EN EL  "+str(float(((count_created_date_2022_thract_sh_typemarkingdefinition*100)/count_thract_sh_typemarkingdefinition)))+" % DE OBJETOS LA FECHA DE CREACION ES 2022")
    print("            -    EN EL  "+str(float(((count_created_date_2021_thract_sh_typemarkingdefinition*100)/count_thract_sh_typemarkingdefinition)))+" % DE OBJETOS LA FECHA DE CREACION ES 2021 ")
    print("            -    EN EL  "+str(float(((count_created_date_2020_thract_sh_typemarkingdefinition*100)/count_thract_sh_typemarkingdefinition)))+" % DE OBJETOS LA FECHA DE CREACION ES 2020 ")
    print("            -    EN EL  "+str(float(((count_created_date_2019_thract_sh_typemarkingdefinition*100)/count_thract_sh_typemarkingdefinition)))+" % DE OBJETOS LA FECHA DE CREACION ES 2019")
    print("            -    EN EL  "+str(float(((count_created_date_2018_thract_sh_typemarkingdefinition*100)/count_thract_sh_typemarkingdefinition)))+" % DE OBJETOS LA FECHA DE CREACION ES 2018 O ANTERIOR ")
    print("\n")






print("***************************ESTADÍSTICAS TIPO DE OBJETO/FECHA DE CREACIÓN INFORME ACTIVIDAD DE AMENAZAS IBM PARTE IOT Y SMART HOME CONJUNTAS***************************")
print("\n")                            
                
print("\n")
print(" DE UN TOTAL DE "+str(count_thract_iot_total+count_thract_sh_total)+" OBJETOS :\n") 
print("\n")
print("   - LAS ESTADISTICAS DE FECHA DE CREACION SON LAS SIGUIENTES:  \n")
print("      -    EN  "+str(count_created_date_2023_thract_iot+count_created_date_2023_thract_sh)+" OBJETOS LA FECHA DE CREACION ES 2023. LAS ESTADÍSTICAS DE TIPO DE OBJETO SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(count_created_date_2023_thract_iot_typereport+count_created_date_2023_thract_sh_typereport)+" OBJETOS CREADOS EN 2023, EL TIPO ES REPORTE ")
print("            -    EN  "+str(count_created_date_2023_thract_iot_typeindicator+count_created_date_2023_thract_sh_typeindicator)+" OBJETOS CREADOS EN 2023, EL TIPO ES INDICADOR")
print("            -    EN  "+str(count_created_date_2023_thract_iot_typemarkingdefinition+count_created_date_2023_thract_sh_typemarkingdefinition)+" OBJETOS CREADOS EN 2023, EL TIPO ES DEFINICION DE MARCADO ")
print("\n")
print("      -    EN  "+str(count_created_date_2022_thract_iot+count_created_date_2022_thract_sh)+" OBJETOS LA FECHA DE CREACION ES 2022. LAS ESTADÍSTICAS DE TIPO DE OBJETO SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(count_created_date_2022_thract_iot_typereport+count_created_date_2022_thract_sh_typereport)+" OBJETOS CREADOS EN 2022, EL TIPO ES REPORTE ")
print("            -    EN  "+str(count_created_date_2022_thract_iot_typeindicator+count_created_date_2022_thract_sh_typeindicator)+" OBJETOS CREADOS EN 2022, EL TIPO ES INDICADOR")
print("            -    EN  "+str(count_created_date_2022_thract_iot_typemarkingdefinition+count_created_date_2022_thract_sh_typemarkingdefinition)+" OBJETOS CREADOS EN 2022, EL TIPO ES DEFINICION DE MARCADO ")
print("\n")
print("      -    EN  "+str(count_created_date_2021_thract_iot+count_created_date_2021_thract_sh)+" OBJETOS LA FECHA DE CREACION ES 2021. LAS ESTADÍSTICAS DE TIPO DE OBJETO SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(count_created_date_2021_thract_iot_typereport+count_created_date_2021_thract_sh_typereport)+" OBJETOS CREADOS EN 2021, EL TIPO ES REPORTE ")
print("            -    EN  "+str(count_created_date_2021_thract_iot_typeindicator+count_created_date_2021_thract_sh_typeindicator)+" OBJETOS CREADOS EN 2021, EL TIPO ES INDICADOR")
print("            -    EN  "+str(count_created_date_2021_thract_iot_typemarkingdefinition+count_created_date_2021_thract_sh_typemarkingdefinition)+" OBJETOS CREADOS EN 2021, EL TIPO ES DEFINICION DE MARCADO ")
print("\n")
print("      -    EN  "+str(count_created_date_2020_thract_iot+count_created_date_2020_thract_sh)+" OBJETOS LA FECHA DE CREACION ES 2020. LAS ESTADÍSTICAS DE TIPO DE OBJETO SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(count_created_date_2020_thract_iot_typereport+count_created_date_2020_thract_sh_typereport)+" OBJETOS CREADOS EN 2020, EL TIPO ES REPORTE ")
print("            -    EN  "+str(count_created_date_2020_thract_iot_typeindicator+count_created_date_2020_thract_sh_typeindicator)+" OBJETOS CREADOS EN 2020, EL TIPO ES INDICADOR")
print("            -    EN  "+str(count_created_date_2020_thract_iot_typemarkingdefinition+count_created_date_2020_thract_sh_typemarkingdefinition)+" OBJETOS CREADOS EN 2020, EL TIPO ES DEFINICION DE MARCADO ")
print("\n")
print("      -    EN  "+str(count_created_date_2019_thract_iot+count_created_date_2019_thract_sh)+" OBJETOS LA FECHA DE CREACION ES 2019. LAS ESTADÍSTICAS DE TIPO DE OBJETO SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(count_created_date_2019_thract_iot_typereport+count_created_date_2019_thract_sh_typereport)+" OBJETOS CREADOS EN 2019, EL TIPO ES REPORTE ")
print("            -    EN  "+str(count_created_date_2019_thract_iot_typeindicator+count_created_date_2019_thract_sh_typeindicator)+" OBJETOS CREADOS EN 2019, EL TIPO ES INDICADOR")
print("            -    EN  "+str(count_created_date_2019_thract_iot_typemarkingdefinition+count_created_date_2019_thract_sh_typemarkingdefinition)+" OBJETOS CREADOS EN 2019, EL TIPO ES DEFINICION DE MARCADO ")
print("\n")
print("      -    EN  "+str(count_created_date_2018_thract_iot+count_created_date_2018_thract_sh)+" OBJETOS LA FECHA DE CREACION ES 2018. LAS ESTADÍSTICAS DE TIPO DE OBJETO SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(count_created_date_2018_thract_iot_typereport+count_created_date_2018_thract_sh_typereport)+" OBJETOS CREADOS EN 2018, EL TIPO ES REPORTE ")
print("            -    EN  "+str(count_created_date_2018_thract_iot_typeindicator+count_created_date_2018_thract_sh_typeindicator)+" OBJETOS CREADOS EN 2018, EL TIPO ES INDICADOR")
print("            -    EN  "+str(count_created_date_2018_thract_iot_typemarkingdefinition+count_created_date_2018_thract_sh_typemarkingdefinition)+" OBJETOS CREADOS EN 2018, EL TIPO ES DEFINICION DE MARCADO ")
print("\n")
print("   - LAS ESTADISTICAS DE TIPO DE OBJETO SON LAS SIGUIENTES:  \n")
print("      -    EN  "+str(count_thract_iot_typereport+count_thract_sh_typereport)+" OBJETOS EL TIPO DE OBJETO ES REPORTE. LAS ESTADÍSTICAS DE FECHA DE CREACION SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(count_created_date_2023_thract_iot_typereport+count_created_date_2023_thract_sh_typereport)+" OBJETOS LA FECHA DE CREACION ES 2023 ")
print("            -    EN  "+str(count_created_date_2022_thract_iot_typereport+count_created_date_2022_thract_sh_typereport)+" OBJETOS LA FECHA DE CREACION ES 2022")
print("            -    EN  "+str(count_created_date_2021_thract_iot_typereport+count_created_date_2021_thract_sh_typereport)+" OBJETOS LA FECHA DE CREACION ES 2021 ")
print("            -    EN  "+str(count_created_date_2020_thract_iot_typereport+count_created_date_2020_thract_sh_typereport)+" OBJETOS LA FECHA DE CREACION ES 2020 ")
print("            -    EN  "+str(count_created_date_2019_thract_iot_typereport+count_created_date_2019_thract_sh_typereport)+" OBJETOS LA FECHA DE CREACION ES 2019")
print("            -    EN  "+str(count_created_date_2018_thract_iot_typereport+count_created_date_2018_thract_sh_typereport)+" OBJETOS LA FECHA DE CREACION ES 2018 O ANTERIOR ")
print("\n")
print("      -    EN  "+str(count_thract_iot_typeindicator+count_thract_sh_typeindicator)+" OBJETOS EL TIPO DE OBJETO ES INDICADOR. LAS ESTADÍSTICAS DE FECHA DE CREACION SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(count_created_date_2023_thract_iot_typeindicator+count_created_date_2023_thract_sh_typeindicator)+" OBJETOS LA FECHA DE CREACION ES 2023 ")
print("            -    EN  "+str(count_created_date_2022_thract_iot_typeindicator+count_created_date_2022_thract_sh_typeindicator)+" OBJETOS LA FECHA DE CREACION ES 2022")
print("            -    EN  "+str(count_created_date_2021_thract_iot_typeindicator+count_created_date_2021_thract_sh_typeindicator)+" OBJETOS LA FECHA DE CREACION ES 2021 ")
print("            -    EN  "+str(count_created_date_2020_thract_iot_typeindicator+count_created_date_2020_thract_sh_typeindicator)+" OBJETOS LA FECHA DE CREACION ES 2020 ")
print("            -    EN  "+str(count_created_date_2019_thract_iot_typeindicator+count_created_date_2019_thract_sh_typeindicator)+" OBJETOS LA FECHA DE CREACION ES 2019")
print("            -    EN  "+str(count_created_date_2018_thract_iot_typeindicator+count_created_date_2018_thract_sh_typeindicator)+" OBJETOS LA FECHA DE CREACION ES 2018 O ANTERIOR ")
print("\n")

print("      -    EN  "+str(count_thract_iot_typemarkingdefinition+count_thract_sh_typemarkingdefinition)+" OBJETOS EL TIPO DE OBJETO ES DEFINICION DE MARCADO. LAS ESTADÍSTICAS DE FECHA DE CREACION SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(count_created_date_2023_thract_iot_typemarkingdefinition+count_created_date_2023_thract_sh_typemarkingdefinition)+" OBJETOS LA FECHA DE CREACION ES 2023 ")
print("            -    EN  "+str(count_created_date_2022_thract_iot_typemarkingdefinition+count_created_date_2022_thract_sh_typemarkingdefinition)+" OBJETOS LA FECHA DE CREACION ES 2022")
print("            -    EN  "+str(count_created_date_2021_thract_iot_typemarkingdefinition+count_created_date_2021_thract_sh_typemarkingdefinition)+" OBJETOS LA FECHA DE CREACION ES 2021 ")
print("            -    EN  "+str(count_created_date_2020_thract_iot_typemarkingdefinition+count_created_date_2020_thract_sh_typemarkingdefinition)+" OBJETOS LA FECHA DE CREACION ES 2020 ")
print("            -    EN  "+str(count_created_date_2019_thract_iot_typemarkingdefinition+count_created_date_2019_thract_sh_typemarkingdefinition)+" OBJETOS LA FECHA DE CREACION ES 2019")
print("            -    EN  "+str(count_created_date_2018_thract_iot_typemarkingdefinition+count_created_date_2018_thract_sh_typemarkingdefinition)+" OBJETOS LA FECHA DE CREACION ES 2018 O ANTERIOR ")
print("\n")













print("***************************PORCENTAJE TIPO DE OBJETO/FECHA DE CREACIÓN INFORME ACTIVIDAD DE AMENAZAS IBM PARTE IOT Y SMART HOME CONJUNTAS***************************")
print("\n")                            
                
print("\n")
print(" DE UN TOTAL DE "+str(count_thract_iot_total+count_thract_sh_total)+" OBJETOS :\n") 
print("\n")
print("   - LOS PORCENTAJES DE FECHA DE CREACION SON LOS SIGUIENTES:  \n")
print("      -    EN EL  "+str(float(((count_created_date_2023_thract_iot+count_created_date_2023_thract_sh)*100)/(count_thract_iot_total+count_thract_sh_total)))+" % DE OBJETOS LA FECHA DE CREACION ES 2023. LOS PORCENTAJES DE TIPO DE OBJETO SON LOS SIGUIENTES:  \n")
print("\n")
print("            -    EN EL  "+str(float((((count_created_date_2023_thract_iot_typereport+count_created_date_2023_thract_sh_typereport)*100)/(count_created_date_2023_thract_iot+count_created_date_2023_thract_sh))))+" % DE OBJETOS CREADOS EN 2023, EL TIPO ES REPORTE ")
print("            -    EN EL  "+str(float((((count_created_date_2023_thract_iot_typeindicator+count_created_date_2023_thract_sh_typeindicator)*100)/(count_created_date_2023_thract_iot+count_created_date_2023_thract_sh))))+" % DE OBJETOS CREADOS EN 2023, EL TIPO ES INDICADOR")
print("            -    EN EL  "+str(float((((count_created_date_2023_thract_iot_typemarkingdefinition+count_created_date_2023_thract_sh_typemarkingdefinition)*100)/(count_created_date_2023_thract_iot+count_created_date_2023_thract_sh))))+" % DE OBJETOS CREADOS EN 2023, EL TIPO ES DEFINICION DE MARCADO ")
print("\n")
print("      -    EN EL  "+str(float(((count_created_date_2022_thract_iot+count_created_date_2022_thract_sh)*100)/(count_thract_iot_total+count_thract_sh_total)))+" % DE OBJETOS LA FECHA DE CREACION ES 2022. LOS PORCENTAJES DE TIPO DE OBJETO SON LOS SIGUIENTES:  \n")
print("\n")
print("            -    EN EL  "+str(float((((count_created_date_2022_thract_iot_typereport+count_created_date_2022_thract_sh_typereport)*100)/(count_created_date_2022_thract_iot+count_created_date_2022_thract_sh))))+" % DE OBJETOS CREADOS EN 2022, EL TIPO ES REPORTE ")
print("            -    EN EL  "+str(float((((count_created_date_2022_thract_iot_typeindicator+count_created_date_2022_thract_sh_typeindicator)*100)/(count_created_date_2022_thract_iot+count_created_date_2022_thract_sh))))+" % DE OBJETOS CREADOS EN 2022, EL TIPO ES INDICADOR")
print("            -    EN EL  "+str(float((((count_created_date_2022_thract_iot_typemarkingdefinition+count_created_date_2022_thract_sh_typemarkingdefinition)*100)/(count_created_date_2022_thract_iot+count_created_date_2022_thract_sh))))+" % DE OBJETOS CREADOS EN 2022, EL TIPO ES DEFINICION DE MARCADO ")
print("\n")
print("      -    EN EL  "+str(float(((count_created_date_2021_thract_iot+count_created_date_2021_thract_sh)*100)/(count_thract_iot_total+count_thract_sh_total)))+" % DE OBJETOS LA FECHA DE CREACION ES 2021. LOS PORCENTAJES DE TIPO DE OBJETO SON LOS SIGUIENTES:  \n")
print("\n")
print("            -    EN EL  "+str(float((((count_created_date_2021_thract_iot_typereport+count_created_date_2021_thract_sh_typereport)*100)/(count_created_date_2021_thract_iot+count_created_date_2021_thract_sh))))+" % DE OBJETOS CREADOS EN 2021, EL TIPO ES REPORTE ")
print("            -    EN EL  "+str(float((((count_created_date_2021_thract_iot_typeindicator+count_created_date_2021_thract_sh_typeindicator)*100)/(count_created_date_2021_thract_iot+count_created_date_2021_thract_sh))))+" % DE OBJETOS CREADOS EN 2021, EL TIPO ES INDICADOR")
print("            -    EN EL  "+str(float((((count_created_date_2021_thract_iot_typemarkingdefinition+count_created_date_2021_thract_sh_typemarkingdefinition)*100)/(count_created_date_2021_thract_iot+count_created_date_2021_thract_sh))))+" % DE OBJETOS CREADOS EN 2021, EL TIPO ES DEFINICION DE MARCADO ")
print("\n")
if((count_created_date_2020_thract_iot+count_created_date_2020_thract_sh)>0):
    print("      -    EN EL  "+str(float(((count_created_date_2020_thract_iot+count_created_date_2020_thract_sh)*100)/(count_thract_iot_total+count_thract_sh_total)))+" % DE OBJETOS LA FECHA DE CREACION ES 2020. LOS PORCENTAJES DE TIPO DE OBJETO SON LOS SIGUIENTES:  \n")
    print("\n")
    print("            -    EN EL  "+str(float((((count_created_date_2020_thract_iot_typereport+count_created_date_2020_thract_sh_typereport)*100)/(count_created_date_2020_thract_iot+count_created_date_2020_thract_sh))))+" % DE OBJETOS CREADOS EN 2020, EL TIPO ES REPORTE ")
    print("            -    EN EL  "+str(float((((count_created_date_2020_thract_iot_typeindicator+count_created_date_2020_thract_sh_typeindicator)*100)/(count_created_date_2020_thract_iot+count_created_date_2020_thract_sh))))+" % DE OBJETOS CREADOS EN 2020, EL TIPO ES INDICADOR")
    print("            -    EN EL  "+str(float((((count_created_date_2020_thract_iot_typemarkingdefinition+count_created_date_2020_thract_sh_typemarkingdefinition)*100)/(count_created_date_2020_thract_iot+count_created_date_2020_thract_sh))))+" % DE OBJETOS CREADOS EN 2020, EL TIPO ES DEFINICION DE MARCADO ")
    print("\n")
if((count_created_date_2019_thract_iot+count_created_date_2019_thract_sh)>0):
    print("      -    EN EL  "+str(float(((count_created_date_2019_thract_iot+count_created_date_2019_thract_sh)*100)/(count_thract_iot_total+count_thract_sh_total)))+" % DE OBJETOS LA FECHA DE CREACION ES 2019. LOS PORCENTAJES DE TIPO DE OBJETO SON LOS SIGUIENTES:  \n")
    print("\n")
    print("            -    EN EL  "+str(float((((count_created_date_2019_thract_iot_typereport+count_created_date_2019_thract_sh_typereport)*100)/(count_created_date_2019_thract_iot+count_created_date_2019_thract_sh))))+" % DE OBJETOS CREADOS EN 2019, EL TIPO ES REPORTE ")
    print("            -    EN EL  "+str(float((((count_created_date_2019_thract_iot_typeindicator+count_created_date_2019_thract_sh_typeindicator)*100)/(count_created_date_2019_thract_iot+count_created_date_2019_thract_sh))))+" % DE OBJETOS CREADOS EN 2019, EL TIPO ES INDICADOR")
    print("            -    EN EL  "+str(float((((count_created_date_2019_thract_iot_typemarkingdefinition+count_created_date_2019_thract_sh_typemarkingdefinition)*100)/(count_created_date_2019_thract_iot+count_created_date_2019_thract_sh))))+" % DE OBJETOS CREADOS EN 2019, EL TIPO ES DEFINICION DE MARCADO ")
    print("\n")
if((count_created_date_2018_thract_iot+count_created_date_2018_thract_sh)>0):
    print("      -    EN EL  "+str(float(((count_created_date_2018_thract_iot+count_created_date_2018_thract_sh)*100)/(count_thract_iot_total+count_thract_sh_total)))+" % DE OBJETOS LA FECHA DE CREACION ES 2018 O ANTERIOR. LOS PORCENTAJES DE TIPO DE OBJETO SON LOS SIGUIENTES:  \n")
    print("\n")
    print("            -    EN EL  "+str(float((((count_created_date_2018_thract_iot_typereport+count_created_date_2018_thract_sh_typereport)*100)/(count_created_date_2018_thract_iot+count_created_date_2018_thract_sh))))+" % DE OBJETOS CREADOS EN 2018 O ANTERIORMENTE, EL TIPO ES REPORTE ")
    print("            -    EN EL  "+str(float((((count_created_date_2018_thract_iot_typeindicator+count_created_date_2018_thract_sh_typeindicator)*100)/(count_created_date_2018_thract_iot+count_created_date_2018_thract_sh))))+" % DE OBJETOS CREADOS EN 2018 O ANTERIORMENTE, EL TIPO ES INDICADOR")
    print("            -    EN EL  "+str(float((((count_created_date_2018_thract_iot_typemarkingdefinition+count_created_date_2018_thract_sh_typemarkingdefinition)*100)/(count_created_date_2018_thract_iot+count_created_date_2018_thract_sh))))+" % DE OBJETOS CREADOS EN 2018 O ANTERIORMENTE, EL TIPO ES DEFINICION DE MARCADO ")
    print("\n")
print("   - LOS PORCENTAJES DE TIPO DE OBJETO SON LAS SIGUIENTES:  \n")
print("      -    EN EL  "+str(float((((count_thract_iot_typereport+count_thract_sh_typereport)*100)/(count_thract_iot_total+count_thract_sh_total))))+" % DE OBJETOS EL TIPO DE OBJETO ES REPORTE. LOS PORCENTAJES DE FECHA DE CREACION SON LOS SIGUIENTES:  \n")
print("\n")
print("            -    EN EL  "+str(float((((count_created_date_2023_thract_iot_typereport+count_created_date_2023_thract_sh_typereport)*100)/(count_thract_iot_typereport+count_thract_sh_typereport))))+" % DE OBJETOS LA FECHA DE CREACION ES 2023 ")
print("            -    EN EL  "+str(float((((count_created_date_2022_thract_iot_typereport+count_created_date_2022_thract_sh_typereport)*100)/(count_thract_iot_typereport+count_thract_sh_typereport))))+" % DE OBJETOS LA FECHA DE CREACION ES 2022")
print("            -    EN EL  "+str(float((((count_created_date_2021_thract_iot_typereport+count_created_date_2021_thract_sh_typereport)*100)/(count_thract_iot_typereport+count_thract_sh_typereport))))+" % DE OBJETOS LA FECHA DE CREACION ES 2021 ")
print("            -    EN EL  "+str(float((((count_created_date_2020_thract_iot_typereport+count_created_date_2020_thract_sh_typereport)*100)/(count_thract_iot_typereport+count_thract_sh_typereport))))+" % DE OBJETOS LA FECHA DE CREACION ES 2020 ")
print("            -    EN EL  "+str(float((((count_created_date_2019_thract_iot_typereport+count_created_date_2019_thract_sh_typereport)*100)/(count_thract_iot_typereport+count_thract_sh_typereport))))+" % DE OBJETOS LA FECHA DE CREACION ES 2019")
print("            -    EN EL  "+str(float((((count_created_date_2018_thract_iot_typereport+count_created_date_2018_thract_sh_typereport)*100)/(count_thract_iot_typereport+count_thract_sh_typereport))))+" % DE OBJETOS LA FECHA DE CREACION ES 2018 O ANTERIOR ")
print("\n")
print("      -    EN EL  "+str(float((((count_thract_iot_typeindicator+count_thract_sh_typeindicator)*100)/(count_thract_iot_total+count_thract_sh_total))))+" % DE OBJETOS EL TIPO DE OBJETO ES INDICADOR. LOS PORCENTAJES DE FECHA DE CREACION SON LOS SIGUIENTES:  \n")
print("\n")
print("            -    EN EL  "+str(float((((count_created_date_2023_thract_iot_typeindicator+count_created_date_2023_thract_sh_typeindicator)*100)/(count_thract_iot_typeindicator+count_thract_sh_typeindicator))))+" % DE OBJETOS LA FECHA DE CREACION ES 2023 ")
print("            -    EN EL  "+str(float((((count_created_date_2022_thract_iot_typeindicator+count_created_date_2022_thract_sh_typeindicator)*100)/(count_thract_iot_typeindicator+count_thract_sh_typeindicator))))+" % DE OBJETOS LA FECHA DE CREACION ES 2022")
print("            -    EN EL  "+str(float((((count_created_date_2021_thract_iot_typeindicator+count_created_date_2021_thract_sh_typeindicator)*100)/(count_thract_iot_typeindicator+count_thract_sh_typeindicator))))+" % DE OBJETOS LA FECHA DE CREACION ES 2021 ")
print("            -    EN EL  "+str(float((((count_created_date_2020_thract_iot_typeindicator+count_created_date_2020_thract_sh_typeindicator)*100)/(count_thract_iot_typeindicator+count_thract_sh_typeindicator))))+" % DE OBJETOS LA FECHA DE CREACION ES 2020 ")
print("            -    EN EL  "+str(float((((count_created_date_2019_thract_iot_typeindicator+count_created_date_2019_thract_sh_typeindicator)*100)/(count_thract_iot_typeindicator+count_thract_sh_typeindicator))))+" % DE OBJETOS LA FECHA DE CREACION ES 2019")
print("            -    EN EL  "+str(float((((count_created_date_2018_thract_iot_typeindicator+count_created_date_2018_thract_sh_typeindicator)*100)/(count_thract_iot_typeindicator+count_thract_sh_typeindicator))))+" % DE OBJETOS LA FECHA DE CREACION ES 2018 O ANTERIOR ")
print("\n")
print("      -    EN EL  "+str(float((((count_thract_iot_typemarkingdefinition+count_thract_sh_typemarkingdefinition)*100)/(count_thract_iot_total+count_thract_sh_total))))+" % DE OBJETOS EL TIPO DE OBJETO ES DEFINICION DE MARCADO. LOS PORCENTAJES DE FECHA DE CREACION SON LOS SIGUIENTES:  \n")
print("\n")
print("            -    EN EL  "+str(float((((count_created_date_2023_thract_iot_typemarkingdefinition+count_created_date_2023_thract_sh_typemarkingdefinition)*100)/(count_thract_iot_typemarkingdefinition+count_thract_sh_typemarkingdefinition))))+" % DE OBJETOS LA FECHA DE CREACION ES 2023 ")
print("            -    EN EL  "+str(float((((count_created_date_2022_thract_iot_typemarkingdefinition+count_created_date_2022_thract_sh_typemarkingdefinition)*100)/(count_thract_iot_typemarkingdefinition+count_thract_sh_typemarkingdefinition))))+" % DE OBJETOS LA FECHA DE CREACION ES 2022")
print("            -    EN EL  "+str(float((((count_created_date_2021_thract_iot_typemarkingdefinition+count_created_date_2021_thract_sh_typemarkingdefinition)*100)/(count_thract_iot_typemarkingdefinition+count_thract_sh_typemarkingdefinition))))+" % DE OBJETOS LA FECHA DE CREACION ES 2021 ")
print("            -    EN EL  "+str(float((((count_created_date_2020_thract_iot_typemarkingdefinition+count_created_date_2020_thract_sh_typemarkingdefinition)*100)/(count_thract_iot_typemarkingdefinition+count_thract_sh_typemarkingdefinition))))+" % DE OBJETOS LA FECHA DE CREACION ES 2020 ")
print("            -    EN EL  "+str(float((((count_created_date_2019_thract_iot_typemarkingdefinition+count_created_date_2019_thract_sh_typemarkingdefinition)*100)/(count_thract_iot_typemarkingdefinition+count_thract_sh_typemarkingdefinition))))+" % DE OBJETOS LA FECHA DE CREACION ES 2019")
print("            -    EN EL  "+str(float((((count_created_date_2018_thract_iot_typemarkingdefinition+count_created_date_2018_thract_sh_typemarkingdefinition)*100)/(count_thract_iot_typemarkingdefinition+count_thract_sh_typemarkingdefinition))))+" % DE OBJETOS LA FECHA DE CREACION ES 2018 O ANTERIOR ")
print("\n")











