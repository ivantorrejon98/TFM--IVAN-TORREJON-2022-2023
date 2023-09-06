


import pandas as pd
from datetime import datetime

#Abro los ficheros con los que voy a tratar


df_alienvault_iot = pd.read_excel('alienvault_iot_2023.xlsx')

#Variables donde almacenare el contador de anio de creacion de los objetos de pulsos de ALIENVAULT
count_createdate_2023_alienvault_iot=0
count_createdate_2022_alienvault_iot=0
count_createdate_2021_alienvault_iot=0
count_createdate_2020_alienvault_iot=0
count_createdate_2019_alienvault_iot=0
count_createdate_2018_alienvault_iot=0

#Variable para almacenar el numero de objetos de ALIENVAULT
len_aux_iot=0

#Comprobamos el anio de creacion
for r in range(0,len(df_alienvault_iot["created"])):
    #Comprobamos si existen varios objetos para la fila actual
    if('[' in df_alienvault_iot["created"][r]):
        #Obtenemos los objetos
        aux_iot=df_alienvault_iot["created"][r].split(",")
        for l in range(0,len(aux_iot)):
            if(len(aux_iot)>0):
                aux_str=aux_iot[l].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
                if(aux_str!='NONE'):
                    len_aux_iot+=1
                    str_anio_createdate_alienvault_iot=aux_str.split("-")
                    anio_createdate_alienvault_iot=int(str_anio_createdate_alienvault_iot[0])
                    if(anio_createdate_alienvault_iot >= 2023):
                        count_createdate_2023_alienvault_iot+=1
                    elif(anio_createdate_alienvault_iot >= 2022):
                        count_createdate_2022_alienvault_iot+=1
                    elif(anio_createdate_alienvault_iot >= 2021):
                        count_createdate_2021_alienvault_iot+=1
                    elif(anio_createdate_alienvault_iot >= 2020):
                        count_createdate_2020_alienvault_iot+=1
                    elif(anio_createdate_alienvault_iot >= 2019):
                        count_createdate_2019_alienvault_iot+=1
                    else:
                        count_createdate_2018_alienvault_iot+=1 
    else:
        len_aux_iot+=1
        str_anio_createdate_alienvault_iot=df_alienvault_iot["created"][r].split("-")
        anio_createdate_alienvault_iot=int(str_anio_createdate_alienvault_iot[0])
        if(anio_createdate_alienvault_iot >= 2023):
            count_createdate_2023_alienvault_iot+=1
        elif(anio_createdate_alienvault_iot >= 2022):
            count_createdate_2022_alienvault_iot+=1
        elif(anio_createdate_alienvault_iot >= 2021):
            count_createdate_2021_alienvault_iot+=1
        elif(anio_createdate_alienvault_iot >= 2020):
            count_createdate_2020_alienvault_iot+=1
        elif(anio_createdate_alienvault_iot >= 2019):
            count_createdate_2019_alienvault_iot+=1
        else:
            count_createdate_2018_alienvault_iot+=1
        

print("**************************ESTADÍSTICAS FECHA DE CREACION PULSOS ALIENVAULT IOT********************************")
print("\n")
print("LA FECHA DE CREACION EN "+str(count_createdate_2023_alienvault_iot)+" OBJETOS ES 2023\n")
print("LA FECHA DE CREACION EN "+str(count_createdate_2022_alienvault_iot)+" OBJETOS ES 2022 \n")
print("LA FECHA DE CREACION EN "+str(count_createdate_2021_alienvault_iot)+" OBJETOS ES 2021 \n")
print("LA FECHA DE CREACION EN "+str(count_createdate_2020_alienvault_iot)+" OBJETOS ES 2020 \n")
print("LA FECHA DE CREACION EN "+str(count_createdate_2019_alienvault_iot)+" OBJETOS ES 2019 \n")
print("LA FECHA DE CREACION EN "+str(count_createdate_2018_alienvault_iot)+" OBJETOS ES ANTERIOR A 2019 \n")
print("\n")
print("**************************PORCENTAJE FECHA DE CREACION PULSOS ALIENVAULT IOT********************************")
print("\n")
print("EL "+str(float((count_createdate_2023_alienvault_iot*100)/(len_aux_iot)))+" % DE LOS OBJETOS FUERON CREADOS EN 2023 \n")
print("EL "+str(float((count_createdate_2022_alienvault_iot*100)/(len_aux_iot)))+" % DE LOS OBJETOS FUERON CREADOS EN 2022 \n")
print("EL "+str(float((count_createdate_2021_alienvault_iot*100)/(len_aux_iot)))+" % DE LOS OBJETOS FUERON CREADOS EN 2021 \n")
print("EL "+str(float((count_createdate_2020_alienvault_iot*100)/(len_aux_iot)))+" % DE LOS OBJETOS FUERON CREADOS EN 2020 \n")
print("EL "+str(float((count_createdate_2019_alienvault_iot*100)/(len_aux_iot)))+" % DE LOS OBJETOS FUERON CREADOS EN 2019 \n")
print("EL "+str(float((count_createdate_2018_alienvault_iot*100)/(len_aux_iot)))+" % DE LOS OBJETOS FUERON CREADOS ANTES DE 2019 \n")
print("\n")



df_alienvault_sh = pd.read_excel('alienvault_smart_home_2023.xlsx')





#Variables donde almacenare el contador de anio de creacion de los objetos de pulsos de ALIENVAULT
count_createdate_2023_alienvault_sh=0
count_createdate_2022_alienvault_sh=0
count_createdate_2021_alienvault_sh=0
count_createdate_2020_alienvault_sh=0
count_createdate_2019_alienvault_sh=0
count_createdate_2018_alienvault_sh=0

#Variable para almacenar el numero de objetos de ALIENVAULT
len_aux_sh=0

#Comprobamos el anio de creacion
for r in range(0,len(df_alienvault_sh["created"])):
    if('[' in df_alienvault_sh["created"][r]):
        aux_sh=df_alienvault_sh["created"][r].split(",")
        for l in range(0,len(aux_sh)):
            if(len(aux_sh)>0):
                aux_str=aux_sh[l].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
                if(aux_str!='NONE'):
                    len_aux_sh+=1
                    str_anio_createdate_alienvault_sh=aux_str.split("-")
                    anio_createdate_alienvault_sh=int(str_anio_createdate_alienvault_sh[0])
                    if(anio_createdate_alienvault_sh >= 2023):
                        count_createdate_2023_alienvault_sh+=1
                    elif(anio_createdate_alienvault_sh >= 2022):
                        count_createdate_2022_alienvault_sh+=1
                    elif(anio_createdate_alienvault_sh >= 2021):
                        count_createdate_2021_alienvault_sh+=1
                    elif(anio_createdate_alienvault_sh >= 2020):
                        count_createdate_2020_alienvault_sh+=1
                    elif(anio_createdate_alienvault_sh >= 2019):
                        count_createdate_2019_alienvault_sh+=1
                    else:
                        count_createdate_2018_alienvault_sh+=1 
    else:
        len_aux_sh+=1
        str_anio_createdate_alienvault_sh=df_alienvault_sh["created"][r].split("-")
        anio_createdate_alienvault_sh=int(str_anio_createdate_alienvault_sh[0])
        if(anio_createdate_alienvault_sh >= 2023):
            count_createdate_2023_alienvault_sh+=1
        elif(anio_createdate_alienvault_sh >= 2022):
            count_createdate_2022_alienvault_sh+=1
        elif(anio_createdate_alienvault_sh >= 2021):
            count_createdate_2021_alienvault_sh+=1
        elif(anio_createdate_alienvault_sh >= 2020):
            count_createdate_2020_alienvault_sh+=1
        elif(anio_createdate_alienvault_sh >= 2019):
            count_createdate_2019_alienvault_sh+=1
        else:
            count_createdate_2018_alienvault_sh+=1
        

print("**************************ESTADÍSTICAS FECHA DE CREACION OBJETOS ALIENVAULT SMART HOME********************************")
print("\n")
print("LA FECHA DE CREACION EN "+str(count_createdate_2023_alienvault_sh)+" OBJETOS ES 2023\n")
print("LA FECHA DE CREACION EN "+str(count_createdate_2022_alienvault_sh)+" OBJETOS ES 2022 \n")
print("LA FECHA DE CREACION EN "+str(count_createdate_2021_alienvault_sh)+" OBJETOS ES 2021 \n")
print("LA FECHA DE CREACION EN "+str(count_createdate_2020_alienvault_sh)+" OBJETOS ES 2020 \n")
print("LA FECHA DE CREACION EN "+str(count_createdate_2019_alienvault_sh)+" OBJETOS ES 2019 \n")
print("LA FECHA DE CREACION EN "+str(count_createdate_2018_alienvault_sh)+" OBJETOS ES ANTERIOR A 2019 \n")
print("\n")
print("**************************PORCENTAJE FECHA DE CREACION OBJETOS ALIENVAULT SMART HOME********************************")
print("\n")
print("EL "+str(float((count_createdate_2023_alienvault_sh*100)/(len_aux_sh)))+" % DE LOS OBJETOS FUERON CREADOS EN 2023 \n")
print("EL "+str(float((count_createdate_2022_alienvault_sh*100)/(len_aux_sh)))+" % DE LOS OBJETOS FUERON CREADOS EN 2022 \n")
print("EL "+str(float((count_createdate_2021_alienvault_sh*100)/(len_aux_sh)))+" % DE LOS OBJETOS FUERON CREADOS EN 2021 \n")
print("EL "+str(float((count_createdate_2020_alienvault_sh*100)/(len_aux_sh)))+" % DE LOS OBJETOS FUERON CREADOS EN 2020 \n")
print("EL "+str(float((count_createdate_2019_alienvault_sh*100)/(len_aux_sh)))+" % DE LOS OBJETOS FUERON CREADOS EN 2019 \n")
print("EL "+str(float((count_createdate_2018_alienvault_sh*100)/(len_aux_sh)))+" % DE LOS OBJETOS FUERON CREADOS ANTES DE 2019 \n")
print("\n")



print("**************************ESTADÍSTICAS FECHA DE CREACION OBJETOS ALIENVAULT PARTE IOT Y SMART HOME CONJUNTAS********************************")
print("\n")
print("LA FECHA DE CREACION EN "+str(count_createdate_2023_alienvault_sh+count_createdate_2023_alienvault_iot)+" OBJETOS ES 2023\n")
print("LA FECHA DE CREACION EN "+str(count_createdate_2022_alienvault_sh+count_createdate_2022_alienvault_iot)+" OBJETOS ES 2022 \n")
print("LA FECHA DE CREACION EN "+str(count_createdate_2021_alienvault_sh+count_createdate_2021_alienvault_iot)+" OBJETOS ES 2021 \n")
print("LA FECHA DE CREACION EN "+str(count_createdate_2020_alienvault_sh+count_createdate_2020_alienvault_iot)+" OBJETOS ES 2020 \n")
print("LA FECHA DE CREACION EN "+str(count_createdate_2019_alienvault_sh+count_createdate_2019_alienvault_iot)+" OBJETOS ES 2019 \n")
print("LA FECHA DE CREACION EN "+str(count_createdate_2018_alienvault_sh+count_createdate_2018_alienvault_iot)+" OBJETOS ES ANTERIOR A 2019 \n")
print("\n")
print("**************************PORCENTAJE FECHA DE CREACION OBJETOS ALIENVAULT PARTE IOT Y SMART HOME CONJUNTAS********************************")
print("\n")
print("EL "+str(float((((count_createdate_2023_alienvault_sh+count_createdate_2023_alienvault_iot)*100)/(len_aux_iot+len_aux_sh))))+" % DE LOS OBJETOS FUERON CREADOS EN 2023 \n")
print("EL "+str(float((((count_createdate_2022_alienvault_sh+count_createdate_2022_alienvault_iot)*100)/(len_aux_iot+len_aux_sh))))+" % DE LOS OBJETOS FUERON CREADOS EN 2022 \n")
print("EL "+str(float((((count_createdate_2021_alienvault_sh+count_createdate_2021_alienvault_iot)*100)/(len_aux_iot+len_aux_sh))))+" % DE LOS OBJETOS FUERON CREADOS EN 2021 \n")
print("EL "+str(float((((count_createdate_2020_alienvault_sh+count_createdate_2020_alienvault_iot)*100)/(len_aux_iot+len_aux_sh))))+" % DE LOS OBJETOS FUERON CREADOS EN 2020 \n")
print("EL "+str(float((((count_createdate_2019_alienvault_sh+count_createdate_2019_alienvault_iot)*100)/(len_aux_iot+len_aux_sh))))+" % DE LOS OBJETOS FUERON CREADOS EN 2019 \n")
print("EL "+str(float((((count_createdate_2018_alienvault_sh+count_createdate_2018_alienvault_iot)*100)/(len_aux_iot+len_aux_sh))))+" % DE LOS OBJETOS FUERON CREADOS ANTES DE 2019 \n")
print("\n")



