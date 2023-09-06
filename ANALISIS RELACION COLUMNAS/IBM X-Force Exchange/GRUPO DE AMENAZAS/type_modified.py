


import pandas as pd
from datetime import datetime

#Abro los ficheros con los que voy a tratar


df_thgroup = pd.read_excel('ibm_grupo_amenazas_2023.xlsx')





#Variables donde almacenare el contador de tipo segun el anio de modificacion
count_modified_date_2023_thgroup_typereport=0
count_modified_date_2023_thgroup_typeindicator=0
count_modified_date_2023_thgroup_typemarkingdefinition=0
#Variables donde almacenare el contador de anio de modificacion 
count_modified_date_2023_thgroup=0

count_modified_date_2022_thgroup_typereport=0
count_modified_date_2022_thgroup_typeindicator=0
count_modified_date_2022_thgroup_typemarkingdefinition=0
count_modified_date_2022_thgroup=0


count_modified_date_2021_thgroup_typereport=0
count_modified_date_2021_thgroup_typeindicator=0
count_modified_date_2021_thgroup_typemarkingdefinition=0
count_modified_date_2021_thgroup=0


count_modified_date_2020_thgroup_typereport=0
count_modified_date_2020_thgroup_typeindicator=0
count_modified_date_2020_thgroup_typemarkingdefinition=0
count_modified_date_2020_thgroup=0


count_modified_date_2019_thgroup_typereport=0
count_modified_date_2019_thgroup_typeindicator=0
count_modified_date_2019_thgroup_typemarkingdefinition=0
count_modified_date_2019_thgroup=0


count_modified_date_2018_thgroup_typereport=0
count_modified_date_2018_thgroup_typeindicator=0
count_modified_date_2018_thgroup_typemarkingdefinition=0
count_modified_date_2018_thgroup=0

count_thgroup_typereport=0
count_thgroup_typeindicator=0
count_thgroup_typemarkingdefinition=0

#Contador de OBJETOS totales
count_thgroup_total=0


#Comprobamos el anio de modificacion 
for r in range(0,len(df_thgroup["modified"])):
    #Si existen varios valores para una misma fila
    if('[' in df_thgroup["modified"][r]):
        #Obtengo los valores de fecha de modificacion
        aux=df_thgroup["modified"][r].split(",")
        #Recorro los distintos valores de la misma fila
        for l in range(0,len(aux)):
            if(len(aux)>0):
                aux_str=aux[l].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
                if(aux_str!='NONE'):
                    #Obtengo el anio de modificacion
                    count_thgroup_total+=1
                    str_anio_publishdate_thgroup=aux_str.split("-")
                    anio_publishdate_thgroup=int(str_anio_publishdate_thgroup[0])
                    #Compruebo el anio de modificacion
                    if(anio_publishdate_thgroup >= 2023):
                        count_modified_date_2023_thgroup+=1
                        #Obtengo los distintos valores de tipo en la fila actual
                        auxx=df_thgroup["type"][r].split(",")
                        #Obtengo los valores individuales de tipo en la fila actual
                        auxx_str=auxx[l].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
                        #Compruebo el tipo
                        if(auxx_str == 'report'):
                            count_thgroup_typereport+=1
                            count_modified_date_2023_thgroup_typereport+=1
                        elif(auxx_str == 'indicator'):
                            count_thgroup_typeindicator+=1
                            count_modified_date_2023_thgroup_typeindicator+=1
                        elif(auxx_str == 'marking-definition'):
                            count_thgroup_typemarkingdefinition+=1
                            count_modified_date_2023_thgroup_typemarkingdefinition+=1 
                                 
                                
                    elif(anio_publishdate_thgroup >= 2022):
                        count_modified_date_2022_thgroup+=1
                        auxx=df_thgroup["type"][r].split(",")
                        auxx_str=auxx[l].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
                        if(auxx_str == 'report'):
                            count_thgroup_typereport+=1
                            count_modified_date_2022_thgroup_typereport+=1
                        elif(auxx_str == 'indicator'):
                            count_thgroup_typeindicator+=1
                            count_modified_date_2022_thgroup_typeindicator+=1
                        elif(auxx_str == 'marking-definition'):
                            count_thgroup_typemarkingdefinition+=1
                            count_modified_date_2022_thgroup_typemarkingdefinition+=1 
                                
                    elif(anio_publishdate_thgroup >= 2021):
                        count_modified_date_2021_thgroup+=1
                        auxx=df_thgroup["type"][r].split(",")
                        auxx_str=auxx[l].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
                        if(auxx_str == 'report'):
                            count_thgroup_typereport+=1
                            count_modified_date_2021_thgroup_typereport+=1
                        elif(auxx_str == 'indicator'):
                            count_thgroup_typeindicator+=1
                            count_modified_date_2021_thgroup_typeindicator+=1
                        elif(auxx_str == 'marking-definition'):
                            count_thgroup_typemarkingdefinition+=1
                            count_modified_date_2021_thgroup_typemarkingdefinition+=1 
                                
                    elif(anio_publishdate_thgroup >= 2020):
                        count_modified_date_2020_thgroup+=1
                        auxx=df_thgroup["type"][r].split(",")
                        auxx_str=auxx[l].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
                        if(auxx_str == 'report'):
                            count_thgroup_typereport+=1
                            count_modified_date_2020_thgroup_typereport+=1
                        elif(auxx_str == 'indicator'):
                            count_thgroup_typeindicator+=1
                            count_modified_date_2020_thgroup_typeindicator+=1
                        elif(auxx_str == 'marking-definition'):
                            count_thgroup_typemarkingdefinition+=1
                            count_modified_date_2020_thgroup_typemarkingdefinition+=1 
                                
                                
                    elif(anio_publishdate_thgroup >= 2019):
                        count_modified_date_2019_thgroup+=1
                        auxx=df_thgroup["type"][r].split(",")
                        auxx_str=auxx[l].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
                        if(auxx_str == 'report'):
                            count_thgroup_typereport+=1
                            count_modified_date_2019_thgroup_typereport+=1
                        elif(auxx_str == 'indicator'):
                            count_thgroup_typeindicator+=1
                            count_modified_date_2019_thgroup_typeindicator+=1
                        elif(auxx_str == 'marking-definition'):
                            count_thgroup_typemarkingdefinition+=1
                            count_modified_date_2019_thgroup_typemarkingdefinition+=1 
                                
                                
                    else: 
                        count_modified_date_2018_thgroup+=1
                        auxx=df_thgroup["type"][r].split(",")
                        auxx_str=auxx[l].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
                        if(auxx_str == 'report'):
                            count_thgroup_typereport+=1
                            count_modified_date_2018_thgroup_typereport+=1
                        elif(auxx_str == 'indicator'):
                            count_thgroup_typeindicator+=1
                            count_modified_date_2018_thgroup_typeindicator+=1
                        elif(auxx_str == 'marking-definition'):
                            count_thgroup_typemarkingdefinition+=1
                            count_modified_date_2018_thgroup_typemarkingdefinition+=1
    else:
        #Si existe un unico valor de fecha de modificacion y tipo para la fila actual
        str_anio_publishdate_thgroup=df_thgroup["modified"][r].split("-")
        anio_publishdate_thgroup=int(str_anio_publishdate_thgroup[0])
        count_thgroup_total+=1
        #Compruebo el anio de modificacion
        if(anio_publishdate_thgroup >= 2023):
            count_modified_date_2023_thgroup+=1
            #Compruebo el TIPO DE OBJETO
            if(df_thgroup["type"][r] == 'report'):
                count_thgroup_typereport+=1
                count_modified_date_2023_thgroup_typereport+=1  
            elif(df_thgroup["type"][r] == 'indicator'):
                count_thgroup_typeindicator+=1
                count_modified_date_2023_thgroup_typeindicator+=1  
            elif(df_thgroup["type"][r] == 'marking-definition'):
                count_thgroup_typemarkingdefinition+=1
                count_modified_date_2023_thgroup_typemarkingdefinition+=1
                
        elif(anio_publishdate_thgroup >= 2022):
            count_modified_date_2022_thgroup+=1
            if(df_thgroup["type"][r] == 'report'):
                count_thgroup_typereport+=1
                count_modified_date_2022_thgroup_typereport+=1  
            elif(df_thgroup["type"][r] == 'indicator'):
                count_thgroup_typeindicator+=1
                count_modified_date_2022_thgroup_typeindicator+=1  
            elif(df_thgroup["type"][r] == 'marking-definition'):
                count_thgroup_typemarkingdefinition+=1
                count_modified_date_2022_thgroup_typemarkingdefinition+=1
        elif(anio_publishdate_thgroup >= 2021):
            count_modified_date_2021_thgroup+=1
            if(df_thgroup["type"][r] == 'report'):
                count_thgroup_typereport+=1
                count_modified_date_2021_thgroup_typereport+=1  
            elif(df_thgroup["type"][r] == 'indicator'):
                count_thgroup_typeindicator+=1
                count_modified_date_2021_thgroup_typeindicator+=1  
            elif(df_thgroup["type"][r] == 'marking-definition'):
                count_thgroup_typemarkingdefinition+=1
                count_modified_date_2021_thgroup_typemarkingdefinition+=1
        elif(anio_publishdate_thgroup >= 2020):
            count_modified_date_2020_thgroup+=1
            if(df_thgroup["type"][r] == 'report'):
                count_thgroup_typereport+=1
                count_modified_date_2020_thgroup_typereport+=1  
            elif(df_thgroup["type"][r] == 'indicator'):
                count_thgroup_typeindicator+=1
                count_modified_date_2020_thgroup_typeindicator+=1  
            elif(df_thgroup["type"][r] == 'marking-definition'):
                count_thgroup_typemarkingdefinition+=1
                count_modified_date_2020_thgroup_typemarkingdefinition+=1
        elif(anio_publishdate_thgroup >= 2019):
            count_modified_date_2019_thgroup+=1
            if(df_thgroup["type"][r] == 'report'):
                count_thgroup_typereport+=1
                count_modified_date_2019_thgroup_typereport+=1  
            elif(df_thgroup["type"][r] == 'indicator'):
                count_thgroup_typeindicator+=1
                count_modified_date_2019_thgroup_typeindicator+=1  
            elif(df_thgroup["type"][r] == 'marking-definition'):
                count_thgroup_typemarkingdefinition+=1
                count_modified_date_2019_thgroup_typemarkingdefinition+=1
        else:
            count_modified_date_2018_thgroup+=1
            if(df_thgroup["type"][r] == 'report'):
                count_thgroup_typereport+=1
                count_modified_date_2018_thgroup_typereport+=1  
            elif(df_thgroup["type"][r] == 'indicator'):
                count_thgroup_typeindicator+=1
                count_modified_date_2018_thgroup_typeindicator+=1  
            elif(df_thgroup["type"][r] == 'marking-definition'):
                count_thgroup_typemarkingdefinition+=1
                count_modified_date_2018_thgroup_typemarkingdefinition+=1
                
                
print("****************************ESTADÍSTICAS TIPO DE OBJETO/FECHA DE MODIFICACION DE OBJETO INFORMES GRUPO DE AMENAZAS IBM****************************")
print("\n")                            
                
print("\n")
print(" DE UN TOTAL DE "+str(count_thgroup_total)+" OBJETOS :\n") 
print("\n")
print("   - LAS ESTADISTICAS DE FECHA DE MODIFICACION SON LAS SIGUIENTES:  \n")
print("      -    EN  "+str(count_modified_date_2023_thgroup)+" OBJETOS LA FECHA DE MODIFICACION ES 2023. LAS ESTADÍSTICAS DE TIPO DE OBJETO SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(count_modified_date_2023_thgroup_typereport)+" OBJETOS MODIFICADOS EN 2023, EL TIPO ES REPORTE ")
print("            -    EN  "+str(count_modified_date_2023_thgroup_typeindicator)+" OBJETOS MODIFICADOS EN 2023, EL TIPO ES INDICADOR")
print("            -    EN  "+str(count_modified_date_2023_thgroup_typemarkingdefinition)+" OBJETOS MODIFICADOS EN 2023, EL TIPO ES DEFINICION DE MARCADO ")
print("\n")
print("      -    EN  "+str(count_modified_date_2022_thgroup)+" OBJETOS LA FECHA DE MODIFICACION ES 2022. LAS ESTADÍSTICAS DE TIPO DE OBJETO SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(count_modified_date_2022_thgroup_typereport)+" OBJETOS MODIFICADOS EN 2022, EL TIPO ES REPORTE ")
print("            -    EN  "+str(count_modified_date_2022_thgroup_typeindicator)+" OBJETOS MODIFICADOS EN 2022, EL TIPO ES INDICADOR")
print("            -    EN  "+str(count_modified_date_2022_thgroup_typemarkingdefinition)+" OBJETOS MODIFICADOS EN 2022, EL TIPO ES DEFINICION DE MARCADO ")
print("\n")
print("      -    EN  "+str(count_modified_date_2021_thgroup)+" OBJETOS LA FECHA DE MODIFICACION ES 2021. LAS ESTADÍSTICAS DE TIPO DE OBJETO SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(count_modified_date_2021_thgroup_typereport)+" OBJETOS MODIFICADOS EN 2021, EL TIPO ES REPORTE ")
print("            -    EN  "+str(count_modified_date_2021_thgroup_typeindicator)+" OBJETOS MODIFICADOS EN 2021, EL TIPO ES INDICADOR")
print("            -    EN  "+str(count_modified_date_2021_thgroup_typemarkingdefinition)+" OBJETOS MODIFICADOS EN 2021, EL TIPO ES DEFINICION DE MARCADO ")
print("\n")
print("      -    EN  "+str(count_modified_date_2020_thgroup)+" OBJETOS LA FECHA DE MODIFICACION ES 2020. LAS ESTADÍSTICAS DE TIPO DE OBJETO SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(count_modified_date_2020_thgroup_typereport)+" OBJETOS MODIFICADOS EN 2020, EL TIPO ES REPORTE ")
print("            -    EN  "+str(count_modified_date_2020_thgroup_typeindicator)+" OBJETOS MODIFICADOS EN 2020, EL TIPO ES INDICADOR")
print("            -    EN  "+str(count_modified_date_2020_thgroup_typemarkingdefinition)+" OBJETOS MODIFICADOS EN 2020, EL TIPO ES DEFINICION DE MARCADO ")
print("\n")
print("      -    EN  "+str(count_modified_date_2019_thgroup)+" OBJETOS LA FECHA DE MODIFICACION ES 2019. LAS ESTADÍSTICAS DE TIPO DE OBJETO SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(count_modified_date_2019_thgroup_typereport)+" OBJETOS MODIFICADOS EN 2019, EL TIPO ES REPORTE ")
print("            -    EN  "+str(count_modified_date_2019_thgroup_typeindicator)+" OBJETOS MODIFICADOS EN 2019, EL TIPO ES INDICADOR")
print("            -    EN  "+str(count_modified_date_2019_thgroup_typemarkingdefinition)+" OBJETOS MODIFICADOS EN 2019, EL TIPO ES DEFINICION DE MARCADO ")
print("\n")
print("      -    EN  "+str(count_modified_date_2018_thgroup)+" OBJETOS LA FECHA DE MODIFICACION ES 2018 O ANTERIOR. LAS ESTADÍSTICAS DE TIPO DE OBJETO SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(count_modified_date_2018_thgroup_typereport)+" OBJETOS MODIFICADOS EN 2018 O ANTES, EL TIPO ES REPORTE ")
print("            -    EN  "+str(count_modified_date_2018_thgroup_typeindicator)+" OBJETOS MODIFICADOS EN 2018 O ANTES, EL TIPO ES INDICADOR")
print("            -    EN  "+str(count_modified_date_2018_thgroup_typemarkingdefinition)+" OBJETOS MODIFICADOS EN 2018 O ANTES, EL TIPO ES DEFINICION DE MARCADO ")
print("\n")
print("   - LAS ESTADISTICAS DE TIPO DE REGISTRO SON LAS SIGUIENTES:  \n")
print("      -    EN  "+str(count_thgroup_typereport)+" OBJETOS EL TIPO DE REGISTRO ES REPORTEE. LAS ESTADÍSTICAS DE FECHA DE MODIFICACION SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(count_modified_date_2023_thgroup_typereport)+" OBJETOS LA FECHA DE MODIFICACION ES 2023 ")
print("            -    EN  "+str(count_modified_date_2022_thgroup_typereport)+" OBJETOS LA FECHA DE MODIFICACION ES 2022")
print("            -    EN  "+str(count_modified_date_2021_thgroup_typereport)+" OBJETOS LA FECHA DE MODIFICACION ES 2021 ")
print("            -    EN  "+str(count_modified_date_2020_thgroup_typereport)+" OBJETOS LA FECHA DE MODIFICACION ES 2020 ")
print("            -    EN  "+str(count_modified_date_2019_thgroup_typereport)+" OBJETOS LA FECHA DE MODIFICACION ES 2019")
print("            -    EN  "+str(count_modified_date_2018_thgroup_typereport)+" OBJETOS LA FECHA DE MODIFICACION ES 2018 O ANTERIOR ")
print("\n")
print("      -    EN  "+str(count_thgroup_typeindicator)+" OBJETOS EL TIPO DE REGISTRO ES INDICADOR. LAS ESTADÍSTICAS DE FECHA DE MODIFICACION SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(count_modified_date_2023_thgroup_typeindicator)+" OBJETOS LA FECHA DE MODIFICACION ES 2023 ")
print("            -    EN  "+str(count_modified_date_2022_thgroup_typeindicator)+" OBJETOS LA FECHA DE MODIFICACION ES 2022")
print("            -    EN  "+str(count_modified_date_2021_thgroup_typeindicator)+" OBJETOS LA FECHA DE MODIFICACION ES 2021 ")
print("            -    EN  "+str(count_modified_date_2020_thgroup_typeindicator)+" OBJETOS LA FECHA DE MODIFICACION ES 2020 ")
print("            -    EN  "+str(count_modified_date_2019_thgroup_typeindicator)+" OBJETOS LA FECHA DE MODIFICACION ES 2019")
print("            -    EN  "+str(count_modified_date_2018_thgroup_typeindicator)+" OBJETOS LA FECHA DE MODIFICACION ES 2018 O ANTERIOR ")
print("\n")
print("      -    EN  "+str(count_thgroup_typemarkingdefinition)+" OBJETOS EL TIPO DE REGISTRO ES DEFINICION DE MARCADO. LAS ESTADÍSTICAS DE FECHA DE MODIFICACION SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(count_modified_date_2023_thgroup_typemarkingdefinition)+" OBJETOS LA FECHA DE MODIFICACION ES 2023 ")
print("            -    EN  "+str(count_modified_date_2022_thgroup_typemarkingdefinition)+" OBJETOS LA FECHA DE MODIFICACION ES 2022")
print("            -    EN  "+str(count_modified_date_2021_thgroup_typemarkingdefinition)+" OBJETOS LA FECHA DE MODIFICACION ES 2021 ")
print("            -    EN  "+str(count_modified_date_2020_thgroup_typemarkingdefinition)+" OBJETOS LA FECHA DE MODIFICACION ES 2020 ")
print("            -    EN  "+str(count_modified_date_2019_thgroup_typemarkingdefinition)+" OBJETOS LA FECHA DE MODIFICACION ES 2019")
print("            -    EN  "+str(count_modified_date_2018_thgroup_typemarkingdefinition)+" OBJETOS LA FECHA DE MODIFICACION ES 2018 O ANTERIOR ")
print("\n")








print("****************************PORCENTAJE TIPO DE OBJETO/FECHA DE MODIFICACION DE OBJETO INFORMES GRUPO DE AMENAZAS IBM****************************")
print("\n")                            
                
print("\n")
print(" DE UN TOTAL DE "+str(count_thgroup_total)+" OBJETOS :\n") 
print("\n")
print("   - LOS PORCENTAJES DE FECHA DE MODIFICACION SON LOS SIGUIENTES:  \n")
if(count_modified_date_2023_thgroup>0):
    print("      -    EN EL  "+str(float(((count_modified_date_2023_thgroup*100)/count_thgroup_total)))+" % DE OBJETOS LA FECHA DE MODIFICACION ES 2023. LOS PORCENTAJES DE TIPO DE OBJETO SON LOS SIGUIENTES:  \n")
    print("\n")
    print("            -    EN EL  "+str(float(((count_modified_date_2023_thgroup_typereport*100)/count_modified_date_2023_thgroup)))+" % DE OBJETOS MODIFICADOS EN 2023, EL TIPO ES REPORTE ")
    print("            -    EN EL  "+str(float(((count_modified_date_2023_thgroup_typeindicator*100)/count_modified_date_2023_thgroup)))+" % DE OBJETOS MODIFICADOS EN 2023, EL TIPO ES INDICADOR")
    print("            -    EN EL  "+str(float(((count_modified_date_2023_thgroup_typemarkingdefinition*100)/count_modified_date_2023_thgroup)))+" % DE OBJETOS MODIFICADOS EN 2023, EL TIPO ES DEFINICION DE MARCADO ")
    print("\n")
print("      -    EN EL  "+str(float(((count_modified_date_2022_thgroup*100)/count_thgroup_total)))+" % DE OBJETOS LA FECHA DE MODIFICACION ES 2022. LOS PORCENTAJESS DE TIPO DE OBJETO SON LOS SIGUIENTES:  \n")
print("\n")
print("            -    EN EL  "+str(float(((count_modified_date_2022_thgroup_typereport*100)/count_modified_date_2022_thgroup)))+" % DE OBJETOS MODIFICADOS EN 2022, EL TIPO ES REPORTE ")
print("            -    EN EL  "+str(float(((count_modified_date_2022_thgroup_typeindicator*100)/count_modified_date_2022_thgroup)))+" % DE OBJETOS MODIFICADOS EN 2022, EL TIPO ES INDICADOR")
print("            -    EN EL  "+str(float(((count_modified_date_2022_thgroup_typemarkingdefinition*100)/count_modified_date_2022_thgroup)))+" % DE OBJETOS MODIFICADOS EN 2022, EL TIPO ES DEFINICION DE MARCADO ")
print("\n")
print("      -    EN EL  "+str(float(((count_modified_date_2021_thgroup*100)/count_thgroup_total)))+" % DE OBJETOS LA FECHA DE MODIFICACION ES 2021. LOS PORCENTAJES DE TIPO DE OBJETO SON LOS SIGUIENTES:  \n")
print("\n")
print("            -    EN EL  "+str(float(((count_modified_date_2021_thgroup_typereport*100)/count_modified_date_2021_thgroup)))+" % DE OBJETOS MODIFICADOS EN 2021, EL TIPO ES REPORTE ")
print("            -    EN EL  "+str(float(((count_modified_date_2021_thgroup_typeindicator*100)/count_modified_date_2021_thgroup)))+" % DE OBJETOS MODIFICADOS EN 2021, EL TIPO ES INDICADOR")
print("            -    EN EL  "+str(float(((count_modified_date_2021_thgroup_typemarkingdefinition*100)/count_modified_date_2021_thgroup)))+" % DE OBJETOS MODIFICADOS EN 2021, EL TIPO ES DEFINICION DE MARCADO ")
print("\n")
if(count_modified_date_2020_thgroup>0):
    print("      -    EN EL  "+str(float(((count_modified_date_2020_thgroup*100)/count_thgroup_total)))+" % DE OBJETOS LA FECHA DE MODIFICACION ES 2020. LOS PORCENTAJES DE TIPO DE OBJETO SON LOS SIGUIENTES:  \n")
    print("\n")
    print("            -    EN EL  "+str(float(((count_modified_date_2020_thgroup_typereport*100)/count_modified_date_2020_thgroup)))+" % DE OBJETOS MODIFICADOS EN 2020, EL TIPO ES REPORTE ")
    print("            -    EN EL  "+str(float(((count_modified_date_2020_thgroup_typeindicator*100)/count_modified_date_2020_thgroup)))+" % DE OBJETOS MODIFICADOS EN 2020, EL TIPO ES INDICADOR")
    print("            -    EN EL  "+str(float(((count_modified_date_2020_thgroup_typemarkingdefinition*100)/count_modified_date_2020_thgroup)))+" % DE OBJETOS MODIFICADOS EN 2020, EL TIPO ES DEFINICION DE MARCADO ")
    print("\n")
if(count_modified_date_2019_thgroup>0):
    print("      -    EN EL  "+str(float(((count_modified_date_2019_thgroup*100)/count_thgroup_total)))+" % DE OBJETOS LA FECHA DE MODIFICACION ES 2019. LOS PORCENTAJES DE TIPO DE OBJETO SON LOS SIGUIENTES:  \n")
    print("\n")
    print("            -    EN EL  "+str(float(((count_modified_date_2019_thgroup_typereport*100)/count_modified_date_2019_thgroup)))+" % DE OBJETOS MODIFICADOS EN 2019, EL TIPO ES REPORTE ")
    print("            -    EN EL  "+str(float(((count_modified_date_2019_thgroup_typeindicator*100)/count_modified_date_2019_thgroup)))+" % DE OBJETOS MODIFICADOS EN 2019, EL TIPO ES INDICADOR")
    print("            -    EN EL  "+str(float(((count_modified_date_2019_thgroup_typemarkingdefinition*100)/count_modified_date_2019_thgroup)))+" % DE OBJETOS MODIFICADOS EN 2019, EL TIPO ES DEFINICION DE MARCADO ")
    print("\n")
if(count_modified_date_2018_thgroup>0):
    print("      -    EN EL  "+str(float(((count_modified_date_2018_thgroup*100)/count_thgroup_total)))+" % DE OBJETOS LA FECHA DE MODIFICACION ES 2018 O ANTERIOR. LOS PORCENTAJES DE TIPO DE OBJETO SON LOS SIGUIENTES:  \n")
    print("\n")
    print("            -    EN EL  "+str(float(((count_modified_date_2018_thgroup_typereport*100)/count_modified_date_2018_thgroup)))+" % DE OBJETOS MODIFICADOS EN 2018 O ANTERIORMENTE, EL TIPO ES REPORTE ")
    print("            -    EN EL  "+str(float(((count_modified_date_2018_thgroup_typeindicator*100)/count_modified_date_2018_thgroup)))+" % DE OBJETOS MODIFICADOS EN 2018 O ANTERIORMENTE, EL TIPO ES INDICADOR")
    print("            -    EN EL  "+str(float(((count_modified_date_2018_thgroup_typemarkingdefinition*100)/count_modified_date_2018_thgroup)))+" % DE OBJETOS MODIFICADOS EN 2018 O ANTERIORMENTE, EL TIPO ES DEFINICION DE MARCADO ")
    print("\n")
print("   - LOS PORCENTAJES DE TIPO DE REGISTRO SON LOS SIGUIENTES:  \n")
print("      -    EN EL  "+str(float(((count_thgroup_typereport*100)/count_thgroup_total)))+" % DE OBJETOS EL TIPO DE REGISTRO ES REPORTE. LOS PORCENTAJES DE FECHA DE MODIFICACION SON LOS SIGUIENTES:  \n")
print("\n")
print("            -    EN EL  "+str(float(((count_modified_date_2023_thgroup_typereport*100)/count_thgroup_typereport)))+" % DE OBJETOS LA FECHA DE MODIFICACION ES 2023 ")
print("            -    EN EL  "+str(float(((count_modified_date_2022_thgroup_typereport*100)/count_thgroup_typereport)))+" % DE OBJETOS LA FECHA DE MODIFICACION ES 2022")
print("            -    EN EL  "+str(float(((count_modified_date_2021_thgroup_typereport*100)/count_thgroup_typereport)))+" % DE OBJETOS LA FECHA DE MODIFICACION ES 2021 ")
print("            -    EN EL  "+str(float(((count_modified_date_2020_thgroup_typereport*100)/count_thgroup_typereport)))+" % DE OBJETOS LA FECHA DE MODIFICACION ES 2020 ")
print("            -    EN EL  "+str(float(((count_modified_date_2019_thgroup_typereport*100)/count_thgroup_typereport)))+" % DE OBJETOS LA FECHA DE MODIFICACION ES 2019")
print("            -    EN EL  "+str(float(((count_modified_date_2018_thgroup_typereport*100)/count_thgroup_typereport)))+" % DE OBJETOS LA FECHA DE MODIFICACION ES 2018 O ANTERIOR ")
print("\n")
if(count_thgroup_typeindicator>0):
    print("      -    EN EL  "+str(float(((count_thgroup_typeindicator*100)/count_thgroup_total)))+" % DE OBJETOS EL TIPO DE REGISTRO ES INDICADOR. LOS PORCENTAJES DE FECHA DE MODIFICACION SON LOS SIGUIENTES:  \n")
    print("\n")
    print("            -    EN EL  "+str(float(((count_modified_date_2023_thgroup_typeindicator*100)/count_thgroup_typeindicator)))+" % DE OBJETOS LA FECHA DE MODIFICACION ES 2023 ")
    print("            -    EN EL  "+str(float(((count_modified_date_2022_thgroup_typeindicator*100)/count_thgroup_typeindicator)))+" % DE OBJETOS LA FECHA DE MODIFICACION ES 2022")
    print("            -    EN EL  "+str(float(((count_modified_date_2021_thgroup_typeindicator*100)/count_thgroup_typeindicator)))+" % DE OBJETOS LA FECHA DE MODIFICACION ES 2021 ")
    print("            -    EN EL  "+str(float(((count_modified_date_2020_thgroup_typeindicator*100)/count_thgroup_typeindicator)))+" % DE OBJETOS LA FECHA DE MODIFICACION ES 2020 ")
    print("            -    EN EL  "+str(float(((count_modified_date_2019_thgroup_typeindicator*100)/count_thgroup_typeindicator)))+" % DE OBJETOS LA FECHA DE MODIFICACION ES 2019")
    print("            -    EN EL  "+str(float(((count_modified_date_2018_thgroup_typeindicator*100)/count_thgroup_typeindicator)))+" % DE OBJETOS LA FECHA DE MODIFICACION ES 2018 O ANTERIOR ")
    print("\n")
if(count_thgroup_typemarkingdefinition>0):
    print("      -    EN EL  "+str(float(((count_thgroup_typemarkingdefinition*100)/count_thgroup_total)))+" % DE OBJETOS EL TIPO DE REGISTRO ES DEFINICION DE MARCADO. LOS PORCENTAJES DE FECHA DE MODIFICACION SON LOS SIGUIENTES:  \n")
    print("\n")
    print("            -    EN EL  "+str(float(((count_modified_date_2023_thgroup_typemarkingdefinition*100)/count_thgroup_typemarkingdefinition)))+" % DE OBJETOS LA FECHA DE MODIFICACION ES 2023 ")
    print("            -    EN EL  "+str(float(((count_modified_date_2022_thgroup_typemarkingdefinition*100)/count_thgroup_typemarkingdefinition)))+" % DE OBJETOS LA FECHA DE MODIFICACION ES 2022")
    print("            -    EN EL  "+str(float(((count_modified_date_2021_thgroup_typemarkingdefinition*100)/count_thgroup_typemarkingdefinition)))+" % DE OBJETOS LA FECHA DE MODIFICACION ES 2021 ")
    print("            -    EN EL  "+str(float(((count_modified_date_2020_thgroup_typemarkingdefinition*100)/count_thgroup_typemarkingdefinition)))+" % DE OBJETOS LA FECHA DE MODIFICACION ES 2020 ")
    print("            -    EN EL  "+str(float(((count_modified_date_2019_thgroup_typemarkingdefinition*100)/count_thgroup_typemarkingdefinition)))+" % DE OBJETOS LA FECHA DE MODIFICACION ES 2019")
    print("            -    EN EL  "+str(float(((count_modified_date_2018_thgroup_typemarkingdefinition*100)/count_thgroup_typemarkingdefinition)))+" % DE OBJETOS LA FECHA DE MODIFICACION ES 2018 O ANTERIOR ")
    print("\n")

















