


import pandas as pd
from datetime import datetime

#Abro los ficheros con los que voy a tratar


df_cpe_iot=pd.read_excel('cpes_iot_2023.xlsx')
df_cpe_sh=pd.read_excel('cpes_smart_home_2023.xlsx')



#Variables donde almacenare el contador de anio de modificacion
count_lastmodidate_2023_cpe_iot=0
count_lastmodidate_2022_cpe_iot=0
count_lastmodidate_2021_cpe_iot=0
count_lastmodidate_2020_cpe_iot=0
count_lastmodidate_2019_cpe_iot=0
count_lastmodidate_2018_cpe_iot=0

for r in range(0,len(df_cpe_iot["cpes.lastModifiedDate"])):
    str_anio_modifdate_cpe_iot=df_cpe_iot["cpes.lastModifiedDate"][r].split("-")
    anio_modifdate_cpe_iot=int(str_anio_modifdate_cpe_iot[0])
    if(anio_modifdate_cpe_iot >= 2023):
        count_lastmodidate_2023_cpe_iot+=1
    elif(anio_modifdate_cpe_iot >= 2022):
        count_lastmodidate_2022_cpe_iot+=1
    elif(anio_modifdate_cpe_iot >= 2021):
        count_lastmodidate_2021_cpe_iot+=1
    elif(anio_modifdate_cpe_iot >= 2020):
        count_lastmodidate_2020_cpe_iot+=1
    elif(anio_modifdate_cpe_iot >= 2019):
        count_lastmodidate_2019_cpe_iot+=1
    else:
        count_lastmodidate_2018_cpe_iot+=1
        

print("**************************ESTADÍSTICAS FECHA DE ULTIMA MODIFICACION CPE IOT********************************")
print("\n")
print("LA FECHA DE ULTIMA MODIFICACION EN "+str(count_lastmodidate_2023_cpe_iot)+" VULNERABILIDADES ES EN 2023\n")
print("LA FECHA DE ULTIMA MODIFICACION EN "+str(count_lastmodidate_2022_cpe_iot)+" VULNERABILIDADES ES EN 2022 \n")
print("LA FECHA DE ULTIMA MODIFICACION EN "+str(count_lastmodidate_2021_cpe_iot)+" VULNERABILIDADES ES EN 2021 \n")
print("LA FECHA DE ULTIMA MODIFICACION EN "+str(count_lastmodidate_2020_cpe_iot)+" VULNERABILIDADES ES EN 2020 \n")
print("LA FECHA DE ULTIMA MODIFICACION EN "+str(count_lastmodidate_2019_cpe_iot)+" VULNERABILIDADES ES EN 2019 \n")
print("LA FECHA DE ULTIMA MODIFICACION EN "+str(count_lastmodidate_2018_cpe_iot)+"  VULNERABILIDADES ES ANTERIOR A 2019 \n")
print("\n")
print("**************************PORCENTAJE FECHA DE ULTIMA MODIFICACION CPE IOT********************************")
print("\n")
print("EL "+str(float(((count_lastmodidate_2023_cpe_iot*100)/len(df_cpe_iot["cpes.lastModifiedDate"]))))+" % DE LAS VULNERABILIDADES FUE MODIFICADO POR ULTIMA VEZ EN 2023 \n")
print("EL "+str(float(((count_lastmodidate_2022_cpe_iot*100)/len(df_cpe_iot["cpes.lastModifiedDate"]))))+" % DE LAS VULNERABILIDADES FUE MODIFICADO POR ULTIMA VEZ EN 2022 \n")
print("EL "+str(float(((count_lastmodidate_2021_cpe_iot*100)/len(df_cpe_iot["cpes.lastModifiedDate"]))))+" % DE LAS VULNERABILIDADES FUE MODIFICADO POR ULTIMA VEZ EN 2021 \n")
print("EL "+str(float(((count_lastmodidate_2020_cpe_iot*100)/len(df_cpe_iot["cpes.lastModifiedDate"]))))+" % DE LAS VULNERABILIDADES FUE MODIFICADO POR ULTIMA VEZ EN 2020 \n")
print("EL "+str(float(((count_lastmodidate_2019_cpe_iot*100)/len(df_cpe_iot["cpes.lastModifiedDate"]))))+" % DE LAS VULNERABILIDADES FUE MODIFICADO POR ULTIMA VEZ EN 2019 \n")
print("EL "+str(float(((count_lastmodidate_2018_cpe_iot*100)/len(df_cpe_iot["cpes.lastModifiedDate"]))))+" % DE LAS VULNERABILIDADES FUE MODIFICADO POR ULTIMA VEZ ANTES DE 2019 \n")
print("\n")












#Variables donde almacenare el contador de anio de modificacion
count_lastmodidate_2023_cpe_sh=0
count_lastmodidate_2022_cpe_sh=0
count_lastmodidate_2021_cpe_sh=0
count_lastmodidate_2020_cpe_sh=0
count_lastmodidate_2019_cpe_sh=0
count_lastmodidate_2018_cpe_sh=0

for j in range(0,len(df_cpe_sh["cpes.lastModifiedDate"])):
    str_anio_modifdate_cpe_sh=df_cpe_sh["cpes.lastModifiedDate"][j].split("-")
    anio_modifdate_cpe_sh=int(str_anio_modifdate_cpe_sh[0])
    if(anio_modifdate_cpe_sh >= 2023):
        count_lastmodidate_2023_cpe_sh+=1
    elif(anio_modifdate_cpe_sh >= 2022):
        count_lastmodidate_2022_cpe_sh+=1
    elif(anio_modifdate_cpe_sh >= 2021):
        count_lastmodidate_2021_cpe_sh+=1
    elif(anio_modifdate_cpe_sh >= 2020):
        count_lastmodidate_2020_cpe_sh+=1
    elif(anio_modifdate_cpe_sh >= 2019):
        count_lastmodidate_2019_cpe_sh+=1
    else:
        count_lastmodidate_2018_cpe_sh+=1
        

print("**************************ESTADÍSTICAS FECHA DE ULTIMA MODIFICACION CPE SMART HOME********************************")
print("\n")
print("LA FECHA DE ULTIMA MODIFICACION EN "+str(count_lastmodidate_2023_cpe_sh)+" VULNERABILIDADES ES EN 2023\n")
print("LA FECHA DE ULTIMA MODIFICACION EN "+str(count_lastmodidate_2022_cpe_sh)+" VULNERABILIDADES ES EN 2022 \n")
print("LA FECHA DE ULTIMA MODIFICACION EN "+str(count_lastmodidate_2021_cpe_sh)+" VULNERABILIDADES ES EN 2021 \n")
print("LA FECHA DE ULTIMA MODIFICACION EN "+str(count_lastmodidate_2020_cpe_sh)+" VULNERABILIDADES ES EN 2020 \n")
print("LA FECHA DE ULTIMA MODIFICACION EN "+str(count_lastmodidate_2019_cpe_sh)+" VULNERABILIDADES ES EN 2019 \n")
print("LA FECHA DE ULTIMA MODIFICACION EN "+str(count_lastmodidate_2018_cpe_sh)+" VULNERABILIDADES ES ANTERIOR A 2019 \n")
print("\n")
print("**************************PORCENTAJE FECHA DE ULTIMA MODIFICACION CPE SMART HOME********************************")
print("\n")
print("EL "+str(float(((count_lastmodidate_2023_cpe_sh*100)/len(df_cpe_sh["cpes.lastModifiedDate"]))))+" % DE LAS VULNERABILIDADES FUE MODIFICADO POR ULTIMA VEZ EN 2023 \n")
print("EL "+str(float(((count_lastmodidate_2022_cpe_sh*100)/len(df_cpe_sh["cpes.lastModifiedDate"]))))+" % DE LAS VULNERABILIDADES FUE MODIFICADO POR ULTIMA VEZ EN 2022 \n")
print("EL "+str(float(((count_lastmodidate_2021_cpe_sh*100)/len(df_cpe_sh["cpes.lastModifiedDate"]))))+" % DE LAS VULNERABILIDADES FUE MODIFICADO POR ULTIMA VEZ EN 2021 \n")
print("EL "+str(float(((count_lastmodidate_2020_cpe_sh*100)/len(df_cpe_sh["cpes.lastModifiedDate"]))))+" % DE LAS VULNERABILIDADES FUE MODIFICADO POR ULTIMA VEZ EN 2020 \n")
print("EL "+str(float(((count_lastmodidate_2019_cpe_sh*100)/len(df_cpe_sh["cpes.lastModifiedDate"]))))+" % DE LAS VULNERABILIDADES FUE MODIFICADO POR ULTIMA VEZ EN 2019 \n")
print("EL "+str(float(((count_lastmodidate_2018_cpe_sh*100)/len(df_cpe_sh["cpes.lastModifiedDate"]))))+" % DE LAS VULNERABILIDADES FUE MODIFICADO POR ULTIMA VEZ ANTES DE 2019 \n")
print("\n")








print("**************************ESTADÍSTICAS FECHA DE ULTIMA MODIFICACION CPES PARTE IOT Y SMART HOME CONJUNTAS********************************")
print("\n")
print("LA FECHA DE ULTIMA MODIFICACION EN "+str(count_lastmodidate_2023_cpe_sh+count_lastmodidate_2023_cpe_iot)+" VULNERABILIDADES ES EN 2023\n")
print("LA FECHA DE ULTIMA MODIFICACION EN "+str(count_lastmodidate_2022_cpe_sh+count_lastmodidate_2022_cpe_iot)+" VULNERABILIDADES ES EN 2022 \n")
print("LA FECHA DE ULTIMA MODIFICACION EN "+str(count_lastmodidate_2021_cpe_sh+count_lastmodidate_2021_cpe_iot)+" VULNERABILIDADES ES EN 2021 \n")
print("LA FECHA DE ULTIMA MODIFICACION EN "+str(count_lastmodidate_2020_cpe_sh+count_lastmodidate_2020_cpe_iot)+" VULNERABILIDADES ES EN 2020 \n")
print("LA FECHA DE ULTIMA MODIFICACION EN "+str(count_lastmodidate_2019_cpe_sh+count_lastmodidate_2019_cpe_iot)+" VULNERABILIDADES ES EN 2019 \n")
print("LA FECHA DE ULTIMA MODIFICACION EN "+str(count_lastmodidate_2018_cpe_sh+count_lastmodidate_2018_cpe_iot)+" VULNERABILIDADES ES ANTERIOR A 2019 \n")
print("\n")


total_cpe_lastmodidate_2023=count_lastmodidate_2023_cpe_sh+count_lastmodidate_2023_cpe_iot
total_cpe_lastmodidate_2022=count_lastmodidate_2022_cpe_sh+count_lastmodidate_2022_cpe_iot
total_cpe_lastmodidate_2021=count_lastmodidate_2021_cpe_sh+count_lastmodidate_2021_cpe_iot
total_cpe_lastmodidate_2020=count_lastmodidate_2020_cpe_sh+count_lastmodidate_2020_cpe_iot
total_cpe_lastmodidate_2019=count_lastmodidate_2019_cpe_sh+count_lastmodidate_2019_cpe_iot
total_cpe_lastmodidate_2018=count_lastmodidate_2018_cpe_sh+count_lastmodidate_2018_cpe_iot

len_total_cpe_lastmodidate=len(df_cpe_sh["cpes.lastModifiedDate"])+len(df_cpe_iot["cpes.lastModifiedDate"])

print("**************************PORCENTAJE FECHA DE ULTIMA MODIFICACION CPES PARTE IOT Y SMART HOME CONJUNTAS********************************")
print("\n")



print("EL "+str(float(((total_cpe_lastmodidate_2023*100)/len_total_cpe_lastmodidate)))+" % DE LAS VULNERABILIDADES FUE MODIFICADO POR ULTIMA VEZ EN 2023 \n")
print("EL "+str(float(((total_cpe_lastmodidate_2022*100)/len_total_cpe_lastmodidate)))+" % DE LAS VULNERABILIDADES FUE MODIFICADO POR ULTIMA VEZ EN 2022 \n")
print("EL "+str(float(((total_cpe_lastmodidate_2021*100)/len_total_cpe_lastmodidate)))+" % DE LAS VULNERABILIDADES FUE MODIFICADO POR ULTIMA VEZ EN 2021 \n")
print("EL "+str(float(((total_cpe_lastmodidate_2020*100)/len_total_cpe_lastmodidate)))+" % DE LAS VULNERABILIDADES FUE MODIFICADO POR ULTIMA VEZ EN 2020 \n")
print("EL "+str(float(((total_cpe_lastmodidate_2019*100)/len_total_cpe_lastmodidate)))+" % DE LAS VULNERABILIDADES FUE MODIFICADO POR ULTIMA VEZ EN 2019 \n")
print("EL "+str(float(((total_cpe_lastmodidate_2018*100)/len_total_cpe_lastmodidate)))+" % DE LAS VULNERABILIDADES FUE MODIFICADO POR ULTIMA VEZ ANTES DE 2019 \n")









