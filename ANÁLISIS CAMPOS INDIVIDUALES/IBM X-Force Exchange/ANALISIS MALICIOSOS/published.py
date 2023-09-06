

import pandas as pd
from datetime import datetime

#Abro los ficheros con los que voy a tratar


df_malw_ana_iot = pd.read_excel('ibm_analisis_maliciosos_iot_2023.xlsx')


#Variables donde almacenare el contador de anio de publicacion de ANALISIS MALICIOSOS
count_publishedate_2023_malw_ana_iot=0
count_publishedate_2022_malw_ana_iot=0
count_publishedate_2021_malw_ana_iot=0
count_publishedate_2020_malw_ana_iot=0
count_publishedate_2019_malw_ana_iot=0
count_publishedate_2018_malw_ana_iot=0

#Comprobamos el anio de publicacion
for r in range(0,len(df_malw_ana_iot["published"])):
    #Comprobamos si existen varios objetos STIX 2.1 en la fila actual
    if('[' in df_malw_ana_iot["published"][r]):
        aux=df_malw_ana_iot["published"][r].split(",")
        for l in range(0,len(aux)):
            if(len(aux)>0):
                aux_str=aux[l].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
                if(aux_str!='NONE'):
                    str_anio_publishdate_malw_ana_iot=aux_str.split("-")
                    anio_publishdate_malw_ana_iot=int(str_anio_publishdate_malw_ana_iot[0])
                    if(anio_publishdate_malw_ana_iot >= 2023):
                        count_publishedate_2023_malw_ana_iot+=1
                    elif(anio_publishdate_malw_ana_iot >= 2022):
                        count_publishedate_2022_malw_ana_iot+=1
                    elif(anio_publishdate_malw_ana_iot >= 2021):
                        count_publishedate_2021_malw_ana_iot+=1
                    elif(anio_publishdate_malw_ana_iot >= 2020):
                        count_publishedate_2020_malw_ana_iot+=1
                    elif(anio_publishdate_malw_ana_iot >= 2019):
                        count_publishedate_2019_malw_ana_iot+=1
                    else:
                        count_publishedate_2018_malw_ana_iot+=1 
    else:
        #Si existe un unico objeto STIX 2.1 en la fila actual
        str_anio_publishdate_malw_ana_iot=df_malw_ana_iot["published"][r].split("-")
        anio_publishdate_malw_ana_iot=int(str_anio_publishdate_malw_ana_iot[0])
        if(anio_publishdate_malw_ana_iot >= 2023):
            count_publishedate_2023_malw_ana_iot+=1
        elif(anio_publishdate_malw_ana_iot >= 2022):
            count_publishedate_2022_malw_ana_iot+=1
        elif(anio_publishdate_malw_ana_iot >= 2021):
            count_publishedate_2021_malw_ana_iot+=1
        elif(anio_publishdate_malw_ana_iot >= 2020):
            count_publishedate_2020_malw_ana_iot+=1
        elif(anio_publishdate_malw_ana_iot >= 2019):
            count_publishedate_2019_malw_ana_iot+=1
        else:
            count_publishedate_2018_malw_ana_iot+=1
        

print("**************************ESTADISTICAS FECHA DE PUBLICACION OBJETOS STIX PARA INFORMES ANALISIS MALICIOSOS IBM PARTE IOT********************************")
print("\n")
print("LA FECHA DE PUBLICACION EN "+str(count_publishedate_2023_malw_ana_iot)+" OBJETOS ES EN 2023\n")
print("LA FECHA DE PUBLICACION EN "+str(count_publishedate_2022_malw_ana_iot)+" OBJETOS ES EN 2022 \n")
print("LA FECHA DE PUBLICACION EN "+str(count_publishedate_2021_malw_ana_iot)+" OBJETOS ES EN 2021 \n")
print("LA FECHA DE PUBLICACION EN "+str(count_publishedate_2020_malw_ana_iot)+" OBJETOS ES EN 2020 \n")
print("LA FECHA DE PUBLICACION EN "+str(count_publishedate_2019_malw_ana_iot)+" OBJETOS ES EN 2019 \n")
print("LA FECHA DE PUBLICACION EN "+str(count_publishedate_2018_malw_ana_iot)+"  OBJETOS ES ANTERIOR A 2019 \n")
print("\n")
print("**************************PORCENTAJE FECHA DE PUBLICACION OBJETOS STIX PARA INFORMES ANALISIS MALICIOSOS IBM PARTE IOT********************************")
print("\n")
print("EL "+str(float(((count_publishedate_2023_malw_ana_iot*100)/len(df_malw_ana_iot["published"]))))+" % DE LOS OBJETOS FUERON PUBLICADOS EN 2023 \n")
print("EL "+str(float(((count_publishedate_2022_malw_ana_iot*100)/len(df_malw_ana_iot["published"]))))+" % DE LOS OBJETOS FUERON PUBLICADOS EN 2022 \n")
print("EL "+str(float(((count_publishedate_2021_malw_ana_iot*100)/len(df_malw_ana_iot["published"]))))+" % DE LOS OBJETOS FUERON PUBLICADOS EN 2021 \n")
print("EL "+str(float(((count_publishedate_2020_malw_ana_iot*100)/len(df_malw_ana_iot["published"]))))+" % DE LOS OBJETOS FUERON PUBLICADOS EN 2020 \n")
print("EL "+str(float(((count_publishedate_2019_malw_ana_iot*100)/len(df_malw_ana_iot["published"]))))+" % DE LOS OBJETOS FUERON PUBLICADOS EN 2019 \n")
print("EL "+str(float(((count_publishedate_2018_malw_ana_iot*100)/len(df_malw_ana_iot["published"]))))+" % DE LOS OBJETOS FUERON PUBLICADOS ANTES DE 2019 \n")
print("\n")



df_malw_ana_sh = pd.read_excel('ibm_analisis_maliciosos_smarthome_2023.xlsx')





#Variables donde almacenare el contador de anio de publicacion de IBM ANALISIS MALICIOSOS
count_publishedate_2023_malw_ana_sh=0
count_publishedate_2022_malw_ana_sh=0
count_publishedate_2021_malw_ana_sh=0
count_publishedate_2020_malw_ana_sh=0
count_publishedate_2019_malw_ana_sh=0
count_publishedate_2018_malw_ana_sh=0

#Comprobamos el anio de modificacion 
for r in range(0,len(df_malw_ana_sh["published"])):
    #Comprobamos si existen varios objetos STIX 2.1 para la fila actual
    if('[' in df_malw_ana_sh["published"][r]):
        aux=df_malw_ana_sh["published"][r].split(",")
        for l in range(0,len(aux)):
            if(len(aux)>0):
                aux_str=aux[l].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
                if(aux_str!='NONE'):
                    str_anio_publishdate_malw_ana_sh=aux_str.split("-")
                    anio_publishdate_malw_ana_sh=int(str_anio_publishdate_malw_ana_sh[0])
                    if(anio_publishdate_malw_ana_sh >= 2023):
                        count_publishedate_2023_malw_ana_sh+=1
                    elif(anio_publishdate_malw_ana_sh >= 2022):
                        count_publishedate_2022_malw_ana_sh+=1
                    elif(anio_publishdate_malw_ana_sh >= 2021):
                        count_publishedate_2021_malw_ana_sh+=1
                    elif(anio_publishdate_malw_ana_sh >= 2020):
                        count_publishedate_2020_malw_ana_sh+=1
                    elif(anio_publishdate_malw_ana_sh >= 2019):
                        count_publishedate_2019_malw_ana_sh+=1
                    else:
                        count_publishedate_2018_malw_ana_sh+=1 
    else:
        #Si existe un unico objeto para la fila actual
        str_anio_publishdate_malw_ana_sh=df_malw_ana_sh["published"][r].split("-")
        anio_publishdate_malw_ana_sh=int(str_anio_publishdate_malw_ana_sh[0])
        if(anio_publishdate_malw_ana_sh >= 2023):
            count_publishedate_2023_malw_ana_sh+=1
        elif(anio_publishdate_malw_ana_sh >= 2022):
            count_publishedate_2022_malw_ana_sh+=1
        elif(anio_publishdate_malw_ana_sh >= 2021):
            count_publishedate_2021_malw_ana_sh+=1
        elif(anio_publishdate_malw_ana_sh >= 2020):
            count_publishedate_2020_malw_ana_sh+=1
        elif(anio_publishdate_malw_ana_sh >= 2019):
            count_publishedate_2019_malw_ana_sh+=1
        else:
            count_publishedate_2018_malw_ana_sh+=1
        

print("**************************ESTADISTICAS FECHA DE PUBLICACION OBJETOS STIX PARA INFORMES ANALISIS MALICIOSOS IBM PARTE SMART HOME********************************")
print("\n")
print("LA FECHA DE PUBLICACION EN "+str(count_publishedate_2023_malw_ana_sh)+" OBJETOS ES EN 2023\n")
print("LA FECHA DE PUBLICACION EN "+str(count_publishedate_2022_malw_ana_sh)+" OBJETOS ES EN 2022 \n")
print("LA FECHA DE PUBLICACION EN "+str(count_publishedate_2021_malw_ana_sh)+" OBJETOS ES EN 2021 \n")
print("LA FECHA DE PUBLICACION EN "+str(count_publishedate_2020_malw_ana_sh)+" OBJETOS ES EN 2020 \n")
print("LA FECHA DE PUBLICACION EN "+str(count_publishedate_2019_malw_ana_sh)+" OBJETOS ES EN 2019 \n")
print("LA FECHA DE PUBLICACION EN "+str(count_publishedate_2018_malw_ana_sh)+"  OBJETOS ES ANTERIOR A 2019 \n")
print("\n")
print("**************************PORCENTAJE FECHA DE PUBLICACION OBJETOS STIX PARA INFORMES ANALISIS MALICIOSOS IBM PARTE SMART HOME********************************")
print("\n")
print("EL "+str(float(((count_publishedate_2023_malw_ana_sh*100)/len(df_malw_ana_sh["published"]))))+" % DE LOS OBJETOS FUERON PUBLICADOS EN 2023 \n")
print("EL "+str(float(((count_publishedate_2022_malw_ana_sh*100)/len(df_malw_ana_sh["published"]))))+" % DE LOS OBJETOS FUERON PUBLICADOS EN 2022 \n")
print("EL "+str(float(((count_publishedate_2021_malw_ana_sh*100)/len(df_malw_ana_sh["published"]))))+" % DE LOS OBJETOS FUERON PUBLICADOS EN 2021 \n")
print("EL "+str(float(((count_publishedate_2020_malw_ana_sh*100)/len(df_malw_ana_sh["published"]))))+" % DE LOS OBJETOS FUERON PUBLICADOS EN 2020 \n")
print("EL "+str(float(((count_publishedate_2019_malw_ana_sh*100)/len(df_malw_ana_sh["published"]))))+" % DE LOS OBJETOS FUERON PUBLICADOS EN 2019 \n")
print("EL "+str(float(((count_publishedate_2018_malw_ana_sh*100)/len(df_malw_ana_sh["published"]))))+" % DE LOS OBJETOS FUERON PUBLICADOS ANTES DE 2019 \n")
print("\n")


















print("**************************ESTADISTICAS FECHA DE PUBLICACION OBJETOS STIX PARA INFORMES ANALISIS MALICIOSOS IBM PARTE IOT Y SMART HOME CONJUNTAS********************************")
print("\n")
print("LA FECHA DE PUBLICACION EN "+str(count_publishedate_2023_malw_ana_sh+count_publishedate_2023_malw_ana_iot)+" OBJETOS ES EN 2023\n")
print("LA FECHA DE PUBLICACION EN "+str(count_publishedate_2022_malw_ana_sh+count_publishedate_2022_malw_ana_iot)+" OBJETOS ES EN 2022 \n")
print("LA FECHA DE PUBLICACION EN "+str(count_publishedate_2021_malw_ana_sh+count_publishedate_2021_malw_ana_iot)+" OBJETOS ES EN 2021 \n")
print("LA FECHA DE PUBLICACION EN "+str(count_publishedate_2020_malw_ana_sh+count_publishedate_2020_malw_ana_iot)+" OBJETOS ES EN 2020 \n")
print("LA FECHA DE PUBLICACION EN "+str(count_publishedate_2019_malw_ana_sh+count_publishedate_2019_malw_ana_iot)+" OBJETOS ES EN 2019 \n")
print("LA FECHA DE PUBLICACION EN "+str(count_publishedate_2018_malw_ana_sh+count_publishedate_2018_malw_ana_iot)+"  OBJETOS ES ANTERIOR A 2019 \n")
print("\n")
print("**************************PORCENTAJE ESTADISTICAS FECHA DE PUBLICACION OBJETOS STIX PARA INFORMES ANALISIS MALICIOSOS IBM PARTE IOT Y SMART HOME CONJUNTAS********************************")
print("\n")
print("EL "+str(float((((count_publishedate_2023_malw_ana_sh+count_publishedate_2023_malw_ana_iot)*100)/(len(df_malw_ana_sh["published"])+len(df_malw_ana_iot["published"])))))+" % DE LOS OBJETOS FUERON PUBLICADOS EN 2023 \n")
print("EL "+str(float((((count_publishedate_2022_malw_ana_sh+count_publishedate_2022_malw_ana_iot)*100)/(len(df_malw_ana_sh["published"])+len(df_malw_ana_iot["published"])))))+" % DE LOS OBJETOS FUERON PUBLICADOS EN 2022 \n")
print("EL "+str(float((((count_publishedate_2021_malw_ana_sh+count_publishedate_2021_malw_ana_iot)*100)/(len(df_malw_ana_sh["published"])+len(df_malw_ana_iot["published"])))))+" % DE LOS OBJETOS FUERON PUBLICADOS EN 2021 \n")
print("EL "+str(float((((count_publishedate_2020_malw_ana_sh+count_publishedate_2020_malw_ana_iot)*100)/(len(df_malw_ana_sh["published"])+len(df_malw_ana_iot["published"])))))+" % DE LOS OBJETOS FUERON PUBLICADOS EN 2020 \n")
print("EL "+str(float((((count_publishedate_2019_malw_ana_sh+count_publishedate_2019_malw_ana_iot)*100)/(len(df_malw_ana_sh["published"])+len(df_malw_ana_iot["published"])))))+" % DE LOS OBJETOS FUERON PUBLICADOS EN 2019 \n")
print("EL "+str(float((((count_publishedate_2018_malw_ana_sh+count_publishedate_2018_malw_ana_iot)*100)/(len(df_malw_ana_sh["published"])+len(df_malw_ana_iot["published"])))))+" % DE LOS OBJETOS FUERON PUBLICADOS ANTES DE 2019 \n")
print("\n")


