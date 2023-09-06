import pandas as pd
from datetime import datetime

#Abro los ficheros con los que voy a tratar


df_cve_iot=pd.read_excel('cves_iot_2023.xlsx')
df_cve_sh=pd.read_excel('cves_smart_home_2023.xlsx')



#Variables donde almacenare el contador de anio de modificacion
count_lastmodidate_2023_cve_iot=0
count_lastmodidate_2022_cve_iot=0
count_lastmodidate_2021_cve_iot=0
count_lastmodidate_2020_cve_iot=0
count_lastmodidate_2019_cve_iot=0
count_lastmodidate_2018_cve_iot=0

#Recorro las distintas filas para comprobar la fecha de modificacion del CVE 

for r in range(0,len(df_cve_iot["CVE_Items.lastModifiedDate"])):
    str_anio_modifdate_cve_iot=df_cve_iot["CVE_Items.lastModifiedDate"][r].split("-")
    anio_modifdate_cve_iot=int(str_anio_modifdate_cve_iot[0])
    if(anio_modifdate_cve_iot >= 2023):
        count_lastmodidate_2023_cve_iot+=1
    elif(anio_modifdate_cve_iot >= 2022):
        count_lastmodidate_2022_cve_iot+=1
    elif(anio_modifdate_cve_iot >= 2021):
        count_lastmodidate_2021_cve_iot+=1
    elif(anio_modifdate_cve_iot >= 2020):
        count_lastmodidate_2020_cve_iot+=1
    elif(anio_modifdate_cve_iot >= 2019):
        count_lastmodidate_2019_cve_iot+=1
    else:
        count_lastmodidate_2018_cve_iot+=1
        

print("**************************FECHA DE ULTIMA MODIFICACION CVE IOT********************************")
print("\n")
print("LA FECHA DE ULTIMA MODIFICACION EN "+str(count_lastmodidate_2023_cve_iot)+" VULNERABILIDADES ES EN 2023\n")
print("LA FECHA DE ULTIMA MODIFICACION EN "+str(count_lastmodidate_2022_cve_iot)+" VULNERABILIDADES ES EN 2022 \n")
print("LA FECHA DE ULTIMA MODIFICACION EN "+str(count_lastmodidate_2021_cve_iot)+" VULNERABILIDADES ES EN 2021 \n")
print("LA FECHA DE ULTIMA MODIFICACION EN "+str(count_lastmodidate_2020_cve_iot)+" VULNERABILIDADES ES EN 2020 \n")
print("LA FECHA DE ULTIMA MODIFICACION EN "+str(count_lastmodidate_2019_cve_iot)+" VULNERABILIDADES ES EN 2019 \n")
print("LA FECHA DE ULTIMA MODIFICACION EN "+str(count_lastmodidate_2018_cve_iot)+"  VULNERABILIDADES ES ANTERIOR A 2019 \n")
print("\n")
print("**************************PORCENTAJE FECHA DE ULTIMA MODIFICACION CVE IOT********************************")
print("\n")
print("EL "+str(float(((count_lastmodidate_2023_cve_iot*100)/len(df_cve_iot["CVE_Items.lastModifiedDate"]))))+" % DE LAS VULNERABILIDADES FUE MODIFICADO POR ULTIMA VEZ EN 2023 \n")
print("EL "+str(float(((count_lastmodidate_2022_cve_iot*100)/len(df_cve_iot["CVE_Items.lastModifiedDate"]))))+" % DE LAS VULNERABILIDADES FUE MODIFICADO POR ULTIMA VEZ EN 2022 \n")
print("EL "+str(float(((count_lastmodidate_2021_cve_iot*100)/len(df_cve_iot["CVE_Items.lastModifiedDate"]))))+" % DE LAS VULNERABILIDADES FUE MODIFICADO POR ULTIMA VEZ EN 2021 \n")
print("EL "+str(float(((count_lastmodidate_2020_cve_iot*100)/len(df_cve_iot["CVE_Items.lastModifiedDate"]))))+" % DE LAS VULNERABILIDADES FUE MODIFICADO POR ULTIMA VEZ EN 2020 \n")
print("EL "+str(float(((count_lastmodidate_2019_cve_iot*100)/len(df_cve_iot["CVE_Items.lastModifiedDate"]))))+" % DE LAS VULNERABILIDADES FUE MODIFICADO POR ULTIMA VEZ EN 2019 \n")
print("EL "+str(float(((count_lastmodidate_2018_cve_iot*100)/len(df_cve_iot["CVE_Items.lastModifiedDate"]))))+" % DE LAS VULNERABILIDADES FUE MODIFICADO POR ULTIMA VEZ ANTES DE 2019 \n")
print("\n")












#Variables donde almacenare el contador de anio de modificacion
count_lastmodidate_2023_cve_sh=0
count_lastmodidate_2022_cve_sh=0
count_lastmodidate_2021_cve_sh=0
count_lastmodidate_2020_cve_sh=0
count_lastmodidate_2019_cve_sh=0
count_lastmodidate_2018_cve_sh=0

#Recorro las distintas filas para comprobar la fecha de modificacion del CVE 

for j in range(0,len(df_cve_sh["CVE_Items.lastModifiedDate"])):
    str_anio_modifdate_cve_sh=df_cve_sh["CVE_Items.lastModifiedDate"][j].split("-")
    anio_modifdate_cve_sh=int(str_anio_modifdate_cve_sh[0])
    if(anio_modifdate_cve_sh >= 2023):
        count_lastmodidate_2023_cve_sh+=1
    elif(anio_modifdate_cve_sh >= 2022):
        count_lastmodidate_2022_cve_sh+=1
    elif(anio_modifdate_cve_sh >= 2021):
        count_lastmodidate_2021_cve_sh+=1
    elif(anio_modifdate_cve_sh >= 2020):
        count_lastmodidate_2020_cve_sh+=1
    elif(anio_modifdate_cve_sh >= 2019):
        count_lastmodidate_2019_cve_sh+=1
    else:
        count_lastmodidate_2018_cve_sh+=1
        

print("**************************FECHA DE ULTIMA MODIFICACION CVE SMART HOME********************************")
print("\n")
print("LA FECHA DE ULTIMA MODIFICACION EN "+str(count_lastmodidate_2023_cve_sh)+" VULNERABILIDADES ES EN 2023\n")
print("LA FECHA DE ULTIMA MODIFICACION EN "+str(count_lastmodidate_2022_cve_sh)+" VULNERABILIDADES ES EN 2022 \n")
print("LA FECHA DE ULTIMA MODIFICACION EN "+str(count_lastmodidate_2021_cve_sh)+" VULNERABILIDADES ES EN 2021 \n")
print("LA FECHA DE ULTIMA MODIFICACION EN "+str(count_lastmodidate_2020_cve_sh)+" VULNERABILIDADES ES EN 2020 \n")
print("LA FECHA DE ULTIMA MODIFICACION EN "+str(count_lastmodidate_2019_cve_sh)+" VULNERABILIDADES ES EN 2019 \n")
print("LA FECHA DE ULTIMA MODIFICACION EN "+str(count_lastmodidate_2018_cve_sh)+" VULNERABILIDADES ES ANTERIOR A 2019 \n")
print("\n")
print("**************************PORCENTAJE FECHA DE ULTIMA MODIFICACION CVE SMART HOME********************************")
print("\n")
print("EL "+str(float(((count_lastmodidate_2023_cve_sh*100)/len(df_cve_sh["CVE_Items.lastModifiedDate"]))))+" % DE LAS VULNERABILIDADES FUE MODIFICADO POR ULTIMA VEZ EN 2023 \n")
print("EL "+str(float(((count_lastmodidate_2022_cve_sh*100)/len(df_cve_sh["CVE_Items.lastModifiedDate"]))))+" % DE LAS VULNERABILIDADES FUE MODIFICADO POR ULTIMA VEZ EN 2022 \n")
print("EL "+str(float(((count_lastmodidate_2021_cve_sh*100)/len(df_cve_sh["CVE_Items.lastModifiedDate"]))))+" % DE LAS VULNERABILIDADES FUE MODIFICADO POR ULTIMA VEZ EN 2021 \n")
print("EL "+str(float(((count_lastmodidate_2020_cve_sh*100)/len(df_cve_sh["CVE_Items.lastModifiedDate"]))))+" % DE LAS VULNERABILIDADES FUE MODIFICADO POR ULTIMA VEZ EN 2020 \n")
print("EL "+str(float(((count_lastmodidate_2019_cve_sh*100)/len(df_cve_sh["CVE_Items.lastModifiedDate"]))))+" % DE LAS VULNERABILIDADES FUE MODIFICADO POR ULTIMA VEZ EN 2019 \n")
print("EL "+str(float(((count_lastmodidate_2018_cve_sh*100)/len(df_cve_sh["CVE_Items.lastModifiedDate"]))))+" % DE LAS VULNERABILIDADES FUE MODIFICADO POR ULTIMA VEZ ANTES DE 2019 \n")
print("\n")








print("**************************FECHA DE ULTIMA MODIFICACION CVE PARTE IOT Y SMART HOME CONJUNTAS********************************")
print("\n")
print("LA FECHA DE ULTIMA MODIFICACION EN "+str(count_lastmodidate_2023_cve_sh+count_lastmodidate_2023_cve_iot)+" VULNERABILIDADES ES EN 2023\n")
print("LA FECHA DE ULTIMA MODIFICACION EN "+str(count_lastmodidate_2022_cve_sh+count_lastmodidate_2022_cve_iot)+" VULNERABILIDADES ES EN 2022 \n")
print("LA FECHA DE ULTIMA MODIFICACION EN "+str(count_lastmodidate_2021_cve_sh+count_lastmodidate_2021_cve_iot)+" VULNERABILIDADES ES EN 2021 \n")
print("LA FECHA DE ULTIMA MODIFICACION EN "+str(count_lastmodidate_2020_cve_sh+count_lastmodidate_2020_cve_iot)+" VULNERABILIDADES ES EN 2020 \n")
print("LA FECHA DE ULTIMA MODIFICACION EN "+str(count_lastmodidate_2019_cve_sh+count_lastmodidate_2019_cve_iot)+" VULNERABILIDADES ES EN 2019 \n")
print("LA FECHA DE ULTIMA MODIFICACION EN "+str(count_lastmodidate_2018_cve_sh+count_lastmodidate_2018_cve_iot)+" VULNERABILIDADES ES ANTERIOR A 2019 \n")
print("\n")


total_cve_lastmodidate_2023=count_lastmodidate_2023_cve_sh+count_lastmodidate_2023_cve_iot
total_cve_lastmodidate_2022=count_lastmodidate_2022_cve_sh+count_lastmodidate_2022_cve_iot
total_cve_lastmodidate_2021=count_lastmodidate_2021_cve_sh+count_lastmodidate_2021_cve_iot
total_cve_lastmodidate_2020=count_lastmodidate_2020_cve_sh+count_lastmodidate_2020_cve_iot
total_cve_lastmodidate_2019=count_lastmodidate_2019_cve_sh+count_lastmodidate_2019_cve_iot
total_cve_lastmodidate_2018=count_lastmodidate_2018_cve_sh+count_lastmodidate_2018_cve_iot

len_total_cve_lastmodidate=len(df_cve_sh["CVE_Items.lastModifiedDate"])+len(df_cve_iot["CVE_Items.lastModifiedDate"])

print("**************************PORCENTAJE FECHA DE ULTIMA MODIFICACION CVE PARTE IOT Y SMART HOME CONJUNTAS********************************")
print("\n")



print("EL "+str(float(((total_cve_lastmodidate_2023*100)/len_total_cve_lastmodidate)))+" % DE LAS VULNERABILIDADES FUE MODIFICADO POR ULTIMA VEZ EN 2023 \n")
print("EL "+str(float(((total_cve_lastmodidate_2022*100)/len_total_cve_lastmodidate)))+" % DE LAS VULNERABILIDADES FUE MODIFICADO POR ULTIMA VEZ EN 2022 \n")
print("EL "+str(float(((total_cve_lastmodidate_2021*100)/len_total_cve_lastmodidate)))+" % DE LAS VULNERABILIDADES FUE MODIFICADO POR ULTIMA VEZ EN 2021 \n")
print("EL "+str(float(((total_cve_lastmodidate_2020*100)/len_total_cve_lastmodidate)))+" % DE LAS VULNERABILIDADES FUE MODIFICADO POR ULTIMA VEZ EN 2020 \n")
print("EL "+str(float(((total_cve_lastmodidate_2019*100)/len_total_cve_lastmodidate)))+" % DE LAS VULNERABILIDADES FUE MODIFICADO POR ULTIMA VEZ EN 2019 \n")
print("EL "+str(float(((total_cve_lastmodidate_2018*100)/len_total_cve_lastmodidate)))+" % DE LAS VULNERABILIDADES FUE MODIFICADO POR ULTIMA VEZ ANTES DE 2019 \n")









