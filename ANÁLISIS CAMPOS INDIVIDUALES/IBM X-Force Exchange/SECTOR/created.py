import pandas as pd
from datetime import datetime

#Abro los ficheros con los que voy a tratar

df_ibm_sector = pd.read_excel('ibm_sector_v2.xlsx')





#Variables donde almacenare el contador de anio de CREACION de IBM SECTOR
count_createdate_2023_ibm_sector=0
count_createdate_2022_ibm_sector=0
count_createdate_2021_ibm_sector=0
count_createdate_2020_ibm_sector=0
count_createdate_2019_ibm_sector=0
count_createdate_2018_ibm_sector=0

#Comprobamos el anio de CREACION 
for r in range(0,len(df_ibm_sector["created"])):
    #Comprobamos si en la fila actual existen varios objetos STIX 2.1
    if('[' in df_ibm_sector["created"][r]):
        aux=df_ibm_sector["created"][r].split(",")
        for l in range(0,len(aux)):
            if(len(aux)>0):
                aux_str=aux[l].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
                if(aux_str!='NONE'):
                    str_anio_createdate_ibm_sector=aux_str.split("-")
                    anio_createdate_ibm_sector=int(str_anio_createdate_ibm_sector[0])
                    if(anio_createdate_ibm_sector >= 2023):
                        count_createdate_2023_ibm_sector+=1
                    elif(anio_createdate_ibm_sector >= 2022):
                        count_createdate_2022_ibm_sector+=1
                    elif(anio_createdate_ibm_sector >= 2021):
                        count_createdate_2021_ibm_sector+=1
                    elif(anio_createdate_ibm_sector >= 2020):
                        count_createdate_2020_ibm_sector+=1
                    elif(anio_createdate_ibm_sector >= 2019):
                        count_createdate_2019_ibm_sector+=1
                    else:
                        count_createdate_2018_ibm_sector+=1 
    else:
        #Si en la fila actual existe unicamente un objeto STIX 2.1
        str_anio_createdate_ibm_sector=df_ibm_sector["created"][r].split("-")
        anio_createdate_ibm_sector=int(str_anio_createdate_ibm_sector[0])
        if(anio_createdate_ibm_sector >= 2023):
            count_createdate_2023_ibm_sector+=1
        elif(anio_createdate_ibm_sector >= 2022):
            count_createdate_2022_ibm_sector+=1
        elif(anio_createdate_ibm_sector >= 2021):
            count_createdate_2021_ibm_sector+=1
        elif(anio_createdate_ibm_sector >= 2020):
            count_createdate_2020_ibm_sector+=1
        elif(anio_createdate_ibm_sector >= 2019):
            count_createdate_2019_ibm_sector+=1
        else:
            count_createdate_2018_ibm_sector+=1
        

print("**************************ESTADÍSTICAS FECHA DE CREACION IBM SECTOR********************************")
print("\n")
print("LA FECHA DE CREACION EN "+str(count_createdate_2023_ibm_sector)+" OBJETOS ES EN 2023\n")
print("LA FECHA DE CREACION EN "+str(count_createdate_2022_ibm_sector)+" OBJETOS ES EN 2022 \n")
print("LA FECHA DE CREACION EN "+str(count_createdate_2021_ibm_sector)+" OBJETOS ES EN 2021 \n")
print("LA FECHA DE CREACION EN "+str(count_createdate_2020_ibm_sector)+" OBJETOS ES EN 2020 \n")
print("LA FECHA DE CREACION EN "+str(count_createdate_2019_ibm_sector)+" OBJETOS ES EN 2019 \n")
print("LA FECHA DE CREACION EN "+str(count_createdate_2018_ibm_sector)+"  OBJETOS ES ANTERIOR A 2019 \n")
print("\n")
print("**************************PORCENTAJE FECHA DE CREACION IBM SECTOR********************************")
print("\n")
print("EL "+str(float(((count_createdate_2023_ibm_sector*100)/len(df_ibm_sector["created"]))))+" % DE LOS OBJETOS FUERON CREADOS EN 2023 \n")
print("EL "+str(float(((count_createdate_2022_ibm_sector*100)/len(df_ibm_sector["created"]))))+" % DE LOS OBJETOS FUERON CREADOS EN 2022 \n")
print("EL "+str(float(((count_createdate_2021_ibm_sector*100)/len(df_ibm_sector["created"]))))+" % DE LOS OBJETOS FUERON CREADOS EN 2021 \n")
print("EL "+str(float(((count_createdate_2020_ibm_sector*100)/len(df_ibm_sector["created"]))))+" % DE LOS OBJETOS FUERON CREADOS EN 2020 \n")
print("EL "+str(float(((count_createdate_2019_ibm_sector*100)/len(df_ibm_sector["created"]))))+" % DE LOS OBJETOS FUERON CREADOS EN 2019 \n")
print("EL "+str(float(((count_createdate_2018_ibm_sector*100)/len(df_ibm_sector["created"]))))+" % DE LOS OBJETOS FUERON CREADOS ANTES DE 2019 \n")
print("\n")









