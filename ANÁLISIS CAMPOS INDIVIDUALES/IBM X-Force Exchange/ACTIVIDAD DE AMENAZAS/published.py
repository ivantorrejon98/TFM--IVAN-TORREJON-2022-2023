import pandas as pd
from datetime import datetime

#Abro los ficheros con los que voy a tratar


df_thract_report_iot = pd.read_excel('ibm_threat_activity_report_iot_2023_v2.xlsx')





#Variables donde almacenare el contador de anio de PUBLICACION de IBM ACTIVIDAD DE AMENAZAS
count_publishdate_2023_thract_report_iot=0
count_publishdate_2022_thract_report_iot=0
count_publishdate_2021_thract_report_iot=0
count_publishdate_2020_thract_report_iot=0
count_publishdate_2019_thract_report_iot=0
count_publishdate_2018_thract_report_iot=0

#Variable para almacenar el numero de objetos totales
len_aux_iot=0
#Comprobamos el anio de PUBLICACION 
for r in range(0,len(df_thract_report_iot["published"])):
    #Compruebo si hay varios objetos en la fila actual
    if('[' in df_thract_report_iot["published"][r]):
        #Obtengo los distintos objetos
        aux=df_thract_report_iot["published"][r].split(",")
        for l in range(0,len(aux)):
            if(len(aux)>0):
                aux_str=aux[l].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
                if(aux_str!='NONE'):
                    len_aux_iot+=1
                    str_anio_publishedate_thract_report_iot=aux_str.split("-")
                    anio_publishedate_thract_report_iot=int(str_anio_publishedate_thract_report_iot[0])
                    if(anio_publishedate_thract_report_iot >= 2023):
                        count_publishdate_2023_thract_report_iot+=1
                    elif(anio_publishedate_thract_report_iot >= 2022):
                        count_publishdate_2022_thract_report_iot+=1
                    elif(anio_publishedate_thract_report_iot >= 2021):
                        count_publishdate_2021_thract_report_iot+=1
                    elif(anio_publishedate_thract_report_iot >= 2020):
                        count_publishdate_2020_thract_report_iot+=1
                    elif(anio_publishedate_thract_report_iot >= 2019):
                        count_publishdate_2019_thract_report_iot+=1
                    else:
                        count_publishdate_2018_thract_report_iot+=1 
    else:
        len_aux_iot+=1
        #Si existe un unico objeto en la fila actual
        str_anio_publishedate_thract_report_iot=df_thract_report_iot["published"][r].split("-")
        anio_publishedate_thract_report_iot=int(str_anio_publishedate_thract_report_iot[0])
        if(anio_publishedate_thract_report_iot >= 2023):
            count_publishdate_2023_thract_report_iot+=1
        elif(anio_publishedate_thract_report_iot >= 2022):
            count_publishdate_2022_thract_report_iot+=1
        elif(anio_publishedate_thract_report_iot >= 2021):
            count_publishdate_2021_thract_report_iot+=1
        elif(anio_publishedate_thract_report_iot >= 2020):
            count_publishdate_2020_thract_report_iot+=1
        elif(anio_publishedate_thract_report_iot >= 2019):
            count_publishdate_2019_thract_report_iot+=1
        else:
            count_publishdate_2018_thract_report_iot+=1
        

print("**************************ESTADÍSTICAS FECHA DE PUBLICACION OBJETO PARA INFORMES IBM ACTIVIDAD DE AMENAZAS PARTE IOT********************************")
print("\n")
print("LA FECHA DE PUBLICACION EN "+str(count_publishdate_2023_thract_report_iot)+" OBJETOS ES EN 2023\n")
print("LA FECHA DE PUBLICACION EN "+str(count_publishdate_2022_thract_report_iot)+" OBJETOS ES EN 2022 \n")
print("LA FECHA DE PUBLICACION EN "+str(count_publishdate_2021_thract_report_iot)+" OBJETOS ES EN 2021 \n")
print("LA FECHA DE PUBLICACION EN "+str(count_publishdate_2020_thract_report_iot)+" OBJETOS ES EN 2020 \n")
print("LA FECHA DE PUBLICACION EN "+str(count_publishdate_2019_thract_report_iot)+" OBJETOS ES EN 2019 \n")
print("LA FECHA DE PUBLICACION EN "+str(count_publishdate_2018_thract_report_iot)+"  OBJETOS ES ANTERIOR A 2019 \n")
print("\n")
print("**************************PORCENTAJE FECHA DE PUBLICACION OBJETO PARA INFORMES IBM ACTIVIDAD DE AMENAZAS PARTE IOT********************************")
print("\n")
print("EL "+str(float(((count_publishdate_2023_thract_report_iot*100)/len_aux_iot)))+" % DE LOS OBJETOS FUERON PUBLICADOS EN 2023 \n")
print("EL "+str(float(((count_publishdate_2022_thract_report_iot*100)/len_aux_iot)))+" % DE LOS OBJETOS FUERON PUBLICADOS EN 2022 \n")
print("EL "+str(float(((count_publishdate_2021_thract_report_iot*100)/len_aux_iot)))+" % DE LOS OBJETOS FUERON PUBLICADOS EN 2021 \n")
print("EL "+str(float(((count_publishdate_2020_thract_report_iot*100)/len_aux_iot)))+" % DE LOS OBJETOS FUERON PUBLICADOS EN 2020 \n")
print("EL "+str(float(((count_publishdate_2019_thract_report_iot*100)/len_aux_iot)))+" % DE LOS OBJETOS FUERON PUBLICADOS EN 2019 \n")
print("EL "+str(float(((count_publishdate_2018_thract_report_iot*100)/len_aux_iot)))+" % DE LOS OBJETOS FUERON PUBLICADOS ANTES DE 2019 \n")
print("\n")



df_thract_report_sh = pd.read_excel('ibm_threat_activity_report_smarthome_2023_v2.xlsx')





#Variables donde almacenare el contador de anio de PUBLICACION de IBM ACTIVIDAD DE AMENAZAS
count_publishdate_2023_thract_report_sh=0
count_publishdate_2022_thract_report_sh=0
count_publishdate_2021_thract_report_sh=0
count_publishdate_2020_thract_report_sh=0
count_publishdate_2019_thract_report_sh=0
count_publishdate_2018_thract_report_sh=0
len_aux_sh=0

#Comprobamos el anio de PUBLICACION 
for r in range(0,len(df_thract_report_sh["published"])):
    #Compruebo si hay varios objetos en la fila actual
    if('[' in df_thract_report_sh["published"][r]):
        #Obtengo los objetos
        aux=df_thract_report_sh["published"][r].split(",")
        for l in range(0,len(aux)):
            if(len(aux)>0):
                aux_str=aux[l].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
                if(aux_str!='NONE'):
                    len_aux_sh+=1
                    str_anio_publishedate_thract_report_sh=aux_str.split("-")
                    anio_publishedate_thract_report_sh=int(str_anio_publishedate_thract_report_sh[0])
                    if(anio_publishedate_thract_report_sh >= 2023):
                        count_publishdate_2023_thract_report_sh+=1
                    elif(anio_publishedate_thract_report_sh >= 2022):
                        count_publishdate_2022_thract_report_sh+=1
                    elif(anio_publishedate_thract_report_sh >= 2021):
                        count_publishdate_2021_thract_report_sh+=1
                    elif(anio_publishedate_thract_report_sh >= 2020):
                        count_publishdate_2020_thract_report_sh+=1
                    elif(anio_publishedate_thract_report_sh >= 2019):
                        count_publishdate_2019_thract_report_sh+=1
                    else:
                        count_publishdate_2018_thract_report_sh+=1 
    else:
        len_aux_sh+=1
        #Si existe un unico objeto en la fila actual
        str_anio_publishedate_thract_report_sh=df_thract_report_sh["published"][r].split("-")
        anio_publishedate_thract_report_sh=int(str_anio_publishedate_thract_report_sh[0])
        if(anio_publishedate_thract_report_sh >= 2023):
            count_publishdate_2023_thract_report_sh+=1
        elif(anio_publishedate_thract_report_sh >= 2022):
            count_publishdate_2022_thract_report_sh+=1
        elif(anio_publishedate_thract_report_sh >= 2021):
            count_publishdate_2021_thract_report_sh+=1
        elif(anio_publishedate_thract_report_sh >= 2020):
            count_publishdate_2020_thract_report_sh+=1
        elif(anio_publishedate_thract_report_sh >= 2019):
            count_publishdate_2019_thract_report_sh+=1
        else:
            count_publishdate_2018_thract_report_sh+=1
        

print("**************************ESTADÍSTICAS FECHA DE PUBLICACION OBJETO PARA INFORMES IBM ACTIVIDAD DE AMENAZAS PARTE SMART HOME********************************")
print("\n")
print("LA FECHA DE PUBLICACION EN "+str(count_publishdate_2023_thract_report_sh)+" OBJETOS ES EN 2023\n")
print("LA FECHA DE PUBLICACION EN "+str(count_publishdate_2022_thract_report_sh)+" OBJETOS ES EN 2022 \n")
print("LA FECHA DE PUBLICACION EN "+str(count_publishdate_2021_thract_report_sh)+" OBJETOS ES EN 2021 \n")
print("LA FECHA DE PUBLICACION EN "+str(count_publishdate_2020_thract_report_sh)+" OBJETOS ES EN 2020 \n")
print("LA FECHA DE PUBLICACION EN "+str(count_publishdate_2019_thract_report_sh)+" OBJETOS ES EN 2019 \n")
print("LA FECHA DE PUBLICACION EN "+str(count_publishdate_2018_thract_report_sh)+"  OBJETOS ES ANTERIOR A 2019 \n")
print("\n")
print("**************************PORCENTAJE FECHA DE PUBLICACION OBJETO PARA INFORMES IBM ACTIVIDAD DE AMENAZAS PARTE SMART HOME********************************")
print("\n")
print("EL "+str(float(((count_publishdate_2023_thract_report_sh*100)/len_aux_sh)))+" % DE LOS OBJETOS FUERON PUBLICADOS EN 2023 \n")
print("EL "+str(float(((count_publishdate_2022_thract_report_sh*100)/len_aux_sh)))+" % DE LOS OBJETOS FUERON PUBLICADOS EN 2022 \n")
print("EL "+str(float(((count_publishdate_2021_thract_report_sh*100)/len_aux_sh)))+" % DE LOS OBJETOS FUERON PUBLICADOS EN 2021 \n")
print("EL "+str(float(((count_publishdate_2020_thract_report_sh*100)/len_aux_sh)))+" % DE LOS OBJETOS FUERON PUBLICADOS EN 2020 \n")
print("EL "+str(float(((count_publishdate_2019_thract_report_sh*100)/len_aux_sh)))+" % DE LOS OBJETOS FUERON PUBLICADOS EN 2019 \n")
print("EL "+str(float(((count_publishdate_2018_thract_report_sh*100)/len_aux_sh)))+" % DE LOS OBJETOS FUERON PUBLICADOS ANTES DE 2019 \n")
print("\n")




print("**************************ESTADÍSTICAS FECHA DE PUBLICACION OBJETO PARA INFORMES IBM ACTIVIDAD DE AMENAZAS PARTE Y SMART HOME CONJUNTAS********************************")
print("\n")
print("LA FECHA DE PUBLICACION EN "+str(count_publishdate_2023_thract_report_sh+count_publishdate_2023_thract_report_iot)+" OBJETOS ES EN 2023\n")
print("LA FECHA DE PUBLICACION EN "+str(count_publishdate_2022_thract_report_sh+count_publishdate_2022_thract_report_iot)+" OBJETOS ES EN 2022 \n")
print("LA FECHA DE PUBLICACION EN "+str(count_publishdate_2021_thract_report_sh+count_publishdate_2021_thract_report_iot)+" OBJETOS ES EN 2021 \n")
print("LA FECHA DE PUBLICACION EN "+str(count_publishdate_2020_thract_report_sh+count_publishdate_2020_thract_report_iot)+" OBJETOS ES EN 2020 \n")
print("LA FECHA DE PUBLICACION EN "+str(count_publishdate_2019_thract_report_sh+count_publishdate_2019_thract_report_iot)+" OBJETOS ES EN 2019 \n")
print("LA FECHA DE PUBLICACION EN "+str(count_publishdate_2018_thract_report_sh+count_publishdate_2018_thract_report_iot)+"  OBJETOS ES ANTERIOR A 2019 \n")
print("\n")
print("**************************PORCENTAJE FECHA DE PUBLICACION OBJETO PARA INFORMES IBM ACTIVIDAD DE AMENAZAS PARTE IOT Y SMART HOME CONJUNTAS********************************")
print("\n")
print("EL "+str(float((((count_publishdate_2023_thract_report_sh+count_publishdate_2023_thract_report_iot)*100)/(len_aux_iot+len_aux_sh))))+" % DE LOS OBJETOS FUERON PUBLICADOS EN 2023 \n")
print("EL "+str(float((((count_publishdate_2022_thract_report_sh+count_publishdate_2022_thract_report_iot)*100)/(len_aux_iot+len_aux_sh))))+" % DE LOS OBJETOS FUERON PUBLICADOS EN 2022 \n")
print("EL "+str(float((((count_publishdate_2021_thract_report_sh+count_publishdate_2021_thract_report_iot)*100)/(len_aux_iot+len_aux_sh))))+" % DE LOS OBJETOS FUERON PUBLICADOS EN 2021 \n")
print("EL "+str(float((((count_publishdate_2020_thract_report_sh+count_publishdate_2020_thract_report_iot)*100)/(len_aux_iot+len_aux_sh))))+" % DE LOS OBJETOS FUERON PUBLICADOS EN 2020 \n")
print("EL "+str(float((((count_publishdate_2019_thract_report_sh+count_publishdate_2019_thract_report_iot)*100)/(len_aux_iot+len_aux_sh))))+" % DE LOS OBJETOS FUERON PUBLICADOS EN 2019 \n")
print("EL "+str(float((((count_publishdate_2018_thract_report_sh+count_publishdate_2018_thract_report_iot)*100)/(len_aux_iot+len_aux_sh))))+" % DE LOS OBJETOS FUERON PUBLICADOS ANTES DE 2019 \n")
print("\n")










