import pandas as pd
from datetime import datetime

#Abro los ficheros con los que voy a tratar

df_ibm_thrgroup = pd.read_excel('ibm_grupo_amenazas_2023.xlsx')





#Variables donde almacenare el contador de anio de creacion de IBM GRUPO DE AMENAZAS
count_createdate_2023_ibm_thrgroup=0
count_createdate_2022_ibm_thrgroup=0
count_createdate_2021_ibm_thrgroup=0
count_createdate_2020_ibm_thrgroup=0
count_createdate_2019_ibm_thrgroup=0
count_createdate_2018_ibm_thrgroup=0

#Comprobamos el anio de creacion
for r in range(0,len(df_ibm_thrgroup["created"])):
    #Comprobamos si en la entrada actual existen varios objetos STIX 2.1
    if('[' in df_ibm_thrgroup["created"][r]):
        aux=df_ibm_thrgroup["created"][r].split(",")
        for l in range(0,len(aux)):
            if(len(aux)>0):
                aux_str=aux[l].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
                if(aux_str!='NONE'):
                    str_anio_createdate_ibm_thrgroup=aux_str.split("-")
                    anio_createdate_ibm_thrgroup=int(str_anio_createdate_ibm_thrgroup[0])
                    if(anio_createdate_ibm_thrgroup >= 2023):
                        count_createdate_2023_ibm_thrgroup+=1
                    elif(anio_createdate_ibm_thrgroup >= 2022):
                        count_createdate_2022_ibm_thrgroup+=1
                    elif(anio_createdate_ibm_thrgroup >= 2021):
                        count_createdate_2021_ibm_thrgroup+=1
                    elif(anio_createdate_ibm_thrgroup >= 2020):
                        count_createdate_2020_ibm_thrgroup+=1
                    elif(anio_createdate_ibm_thrgroup >= 2019):
                        count_createdate_2019_ibm_thrgroup+=1
                    else:
                        count_createdate_2018_ibm_thrgroup+=1 
    else:
        #Si en la entrada actual únicamente hay un objeto STIX 2.1
        str_anio_createdate_ibm_thrgroup=df_ibm_thrgroup["created"][r].split("-")
        anio_createdate_ibm_thrgroup=int(str_anio_createdate_ibm_thrgroup[0])
        if(anio_createdate_ibm_thrgroup >= 2023):
            count_createdate_2023_ibm_thrgroup+=1
        elif(anio_createdate_ibm_thrgroup >= 2022):
            count_createdate_2022_ibm_thrgroup+=1
        elif(anio_createdate_ibm_thrgroup >= 2021):
            count_createdate_2021_ibm_thrgroup+=1
        elif(anio_createdate_ibm_thrgroup >= 2020):
            count_createdate_2020_ibm_thrgroup+=1
        elif(anio_createdate_ibm_thrgroup >= 2019):
            count_createdate_2019_ibm_thrgroup+=1
        else:
            count_createdate_2018_ibm_thrgroup+=1
        

print("**************************ESTADÍSTICAS FECHA DE CREACION IBM GRUPO DE AMENAZAS********************************")
print("\n")
print("LA FECHA DE CREACION EN "+str(count_createdate_2023_ibm_thrgroup)+" OBJETOS ES EN 2023\n")
print("LA FECHA DE CREACION EN "+str(count_createdate_2022_ibm_thrgroup)+" OBJETOS ES EN 2022 \n")
print("LA FECHA DE CREACION EN "+str(count_createdate_2021_ibm_thrgroup)+" OBJETOS ES EN 2021 \n")
print("LA FECHA DE CREACION EN "+str(count_createdate_2020_ibm_thrgroup)+" OBJETOS ES EN 2020 \n")
print("LA FECHA DE CREACION EN "+str(count_createdate_2019_ibm_thrgroup)+" OBJETOS ES EN 2019 \n")
print("LA FECHA DE CREACION EN "+str(count_createdate_2018_ibm_thrgroup)+"  OBJETOS ES ANTERIOR A 2019 \n")
print("\n")
print("**************************PORCENTAJE FECHA DE CREACION IBM GRUPO DE AMENAZAS********************************")
print("\n")
print("EL "+str(float(((count_createdate_2023_ibm_thrgroup*100)/len(df_ibm_thrgroup["created"]))))+" % DE LOS OBJETOS FUE CREADO EN 2023 \n")
print("EL "+str(float(((count_createdate_2022_ibm_thrgroup*100)/len(df_ibm_thrgroup["created"]))))+" % DE LOS OBJETOS FUE CREADO EN 2022 \n")
print("EL "+str(float(((count_createdate_2021_ibm_thrgroup*100)/len(df_ibm_thrgroup["created"]))))+" % DE LOS OBJETOS FUE CREADO EN 2021 \n")
print("EL "+str(float(((count_createdate_2020_ibm_thrgroup*100)/len(df_ibm_thrgroup["created"]))))+" % DE LOS OBJETOS FUE CREADO EN 2020 \n")
print("EL "+str(float(((count_createdate_2019_ibm_thrgroup*100)/len(df_ibm_thrgroup["created"]))))+" % DE LOS OBJETOS FUE CREADO EN 2019 \n")
print("EL "+str(float(((count_createdate_2018_ibm_thrgroup*100)/len(df_ibm_thrgroup["created"]))))+" % DE LOS OBJETOS FUE CREADO ANTES DE 2019 \n")
print("\n")







