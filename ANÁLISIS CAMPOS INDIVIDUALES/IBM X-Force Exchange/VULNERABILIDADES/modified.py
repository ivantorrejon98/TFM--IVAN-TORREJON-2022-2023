

import pandas as pd
from datetime import datetime

#Abro los ficheros con los que voy a tratar


df_vuln_ibm_iot = pd.read_excel('vulnerabilidades_ibm_iot_2023.xlsx')


#Variables donde almacenare el contador de anio de modificacion de VULNERABILIDADES IBM
count_modidate_2023_vuln_ibm_iot=0
count_modidate_2022_vuln_ibm_iot=0
count_modidate_2021_vuln_ibm_iot=0
count_modidate_2020_vuln_ibm_iot=0
count_modidate_2019_vuln_ibm_iot=0
count_modidate_2018_vuln_ibm_iot=0

#Variable para almacenar el numero de objetos
len_aux_iot=0
#Comprobamos el anio de modificacion
for r in range(0,len(df_vuln_ibm_iot["modified"])):
    #Compruebo si estamos ante un vector o un valor unico
    if('[' in df_vuln_ibm_iot["modified"][r]):
        #Obtengo los distintos valores del vector
        aux=df_vuln_ibm_iot["modified"][r].split(",")
        #Recorro los valores del vector
        for l in range(0,len(aux)):
            if(len(aux)>0):
                #Elimino caracteres especiales de cada valor del vector
                aux_str=aux[l].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
                if(aux_str!='NONE'):
                    len_aux_iot+=1
                    #Obtengo el anio de modificacion
                    str_anio_modidate_vuln_ibm_iot=aux_str.split("-")
                    anio_modidate_vuln_ibm_iot=int(str_anio_modidate_vuln_ibm_iot[0])
                    #Obtengo el anio de modificacion y aumento los contadores segun sea el anio
                    if(anio_modidate_vuln_ibm_iot >= 2023):
                        count_modidate_2023_vuln_ibm_iot+=1
                    elif(anio_modidate_vuln_ibm_iot >= 2022):
                        count_modidate_2022_vuln_ibm_iot+=1
                    elif(anio_modidate_vuln_ibm_iot >= 2021):
                        count_modidate_2021_vuln_ibm_iot+=1
                    elif(anio_modidate_vuln_ibm_iot >= 2020):
                        count_modidate_2020_vuln_ibm_iot+=1
                    elif(anio_modidate_vuln_ibm_iot >= 2019):
                        count_modidate_2019_vuln_ibm_iot+=1
                    else:
                        count_modidate_2018_vuln_ibm_iot+=1 
    else:
        len_aux_iot+=1
        #Si el valor es unico y no un vector
        str_anio_modidate_vuln_ibm_iot=df_vuln_ibm_iot["modified"][r].split("-")
        anio_modidate_vuln_ibm_iot=int(str_anio_modidate_vuln_ibm_iot[0])
        #Obtengo el anio de modificacion
        if(anio_modidate_vuln_ibm_iot >= 2023):
            count_modidate_2023_vuln_ibm_iot+=1
        elif(anio_modidate_vuln_ibm_iot >= 2022):
            count_modidate_2022_vuln_ibm_iot+=1
        elif(anio_modidate_vuln_ibm_iot >= 2021):
            count_modidate_2021_vuln_ibm_iot+=1
        elif(anio_modidate_vuln_ibm_iot >= 2020):
            count_modidate_2020_vuln_ibm_iot+=1
        elif(anio_modidate_vuln_ibm_iot >= 2019):
            count_modidate_2019_vuln_ibm_iot+=1
        else:
            count_modidate_2018_vuln_ibm_iot+=1
        

print("**************************ESTADÍSTICAS FECHA DE MODIFICACION OBJETOS VULNERABILIDADES PARTE IOT********************************")
print("\n")
print("LA FECHA DE MODIFICACION EN "+str(count_modidate_2023_vuln_ibm_iot)+" OBJETOS ES  EN 2023\n")
print("LA FECHA DE MODIFICACION EN "+str(count_modidate_2022_vuln_ibm_iot)+" OBJETOS ES  EN 2022 \n")
print("LA FECHA DE MODIFICACION EN "+str(count_modidate_2021_vuln_ibm_iot)+" OBJETOS ES  EN 2021 \n")
print("LA FECHA DE MODIFICACION EN "+str(count_modidate_2020_vuln_ibm_iot)+" OBJETOS ES  EN 2020 \n")
print("LA FECHA DE MODIFICACION EN "+str(count_modidate_2019_vuln_ibm_iot)+" OBJETOS ES  EN 2019 \n")
print("LA FECHA DE MODIFICACION EN "+str(count_modidate_2018_vuln_ibm_iot)+"  OBJETOS ES  ANTERIOR A 2019 \n")
print("\n")
print("**************************PORCENTAJE FECHA DE MODIFICACION OBJETOS VULNERABILIDADES PARTE IOT********************************")
print("\n")
print("EL "+str(float(((count_modidate_2023_vuln_ibm_iot*100)/len_aux_iot)))+" % DE LOS OBJETOS FUERON MODIFICADOS EN 2023 \n")
print("EL "+str(float(((count_modidate_2022_vuln_ibm_iot*100)/len_aux_iot)))+" % DE LOS OBJETOS FUERON MODIFICADOS EN 2022 \n")
print("EL "+str(float(((count_modidate_2021_vuln_ibm_iot*100)/len_aux_iot)))+" % DE LOS OBJETOS FUERON MODIFICADOS EN 2021 \n")
print("EL "+str(float(((count_modidate_2020_vuln_ibm_iot*100)/len_aux_iot)))+" % DE LOS OBJETOS FUERON MODIFICADOS EN 2020 \n")
print("EL "+str(float(((count_modidate_2019_vuln_ibm_iot*100)/len_aux_iot)))+" % DE LOS OBJETOS FUERON MODIFICADOS EN 2019 \n")
print("EL "+str(float(((count_modidate_2018_vuln_ibm_iot*100)/len_aux_iot)))+" % DE LOS OBJETOS FUERON MODIFICADOS ANTES DE 2019 \n")
print("\n")



df_vuln_ibm_sh = pd.read_excel('vulnerabilidades_ibm_smart_home_2023.xlsx')



#Variables donde almacenare el contador de anio de modificacion de VULNERABILIDADES IBM
count_modidate_2023_vuln_ibm_sh=0
count_modidate_2022_vuln_ibm_sh=0
count_modidate_2021_vuln_ibm_sh=0
count_modidate_2020_vuln_ibm_sh=0
count_modidate_2019_vuln_ibm_sh=0
count_modidate_2018_vuln_ibm_sh=0

#Variable para almacenar el numero de objetos
len_aux_sh=0

#Comprobamos el anio de modificacion 
for r in range(0,len(df_vuln_ibm_sh["modified"])):
    #Compruebo si estamos ante un vector o un valor unico
    if('[' in df_vuln_ibm_sh["modified"][r]):
        #Obtengo los distintos valores del vector
        aux=df_vuln_ibm_sh["modified"][r].split(",")
        #Recorro los valores del vector
        for l in range(0,len(aux)):
            if(len(aux)>0):
                aux_str=aux[l].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
                if(aux_str!='NONE'):
                    len_aux_sh+=1
                    #Obtengo el anio de modificacion y aumento los contadores segun sea el anio
                    str_anio_modidate_vuln_ibm_sh=aux_str.split("-")
                    anio_modidate_vuln_ibm_sh=int(str_anio_modidate_vuln_ibm_sh[0])
                    if(anio_modidate_vuln_ibm_sh >= 2023):
                        count_modidate_2023_vuln_ibm_sh+=1
                    elif(anio_modidate_vuln_ibm_sh >= 2022):
                        count_modidate_2022_vuln_ibm_sh+=1
                    elif(anio_modidate_vuln_ibm_sh >= 2021):
                        count_modidate_2021_vuln_ibm_sh+=1
                    elif(anio_modidate_vuln_ibm_sh >= 2020):
                        count_modidate_2020_vuln_ibm_sh+=1
                    elif(anio_modidate_vuln_ibm_sh >= 2019):
                        count_modidate_2019_vuln_ibm_sh+=1
                    else:
                        count_modidate_2018_vuln_ibm_sh+=1 
    else:
        len_aux_sh+=1
        #Obtengo el anio de modificacion y aumento los contadores segun sea el anio
        str_anio_modidate_vuln_ibm_sh=df_vuln_ibm_sh["modified"][r].split("-")
        anio_modidate_vuln_ibm_sh=int(str_anio_modidate_vuln_ibm_sh[0])
        if(anio_modidate_vuln_ibm_sh >= 2023):
            count_modidate_2023_vuln_ibm_sh+=1
        elif(anio_modidate_vuln_ibm_sh >= 2022):
            count_modidate_2022_vuln_ibm_sh+=1
        elif(anio_modidate_vuln_ibm_sh >= 2021):
            count_modidate_2021_vuln_ibm_sh+=1
        elif(anio_modidate_vuln_ibm_sh >= 2020):
            count_modidate_2020_vuln_ibm_sh+=1
        elif(anio_modidate_vuln_ibm_sh >= 2019):
            count_modidate_2019_vuln_ibm_sh+=1
        else:
            count_modidate_2018_vuln_ibm_sh+=1
        

print("**************************ESTADÍSTICAS FECHA DE MODIFICACION OBJETOS VULNERABILIDADES PARTE SMART HOME********************************")
print("\n")
print("LA FECHA DE MODIFICACION EN "+str(count_modidate_2023_vuln_ibm_sh)+" OBJETOS ES  EN 2023\n")
print("LA FECHA DE MODIFICACION EN "+str(count_modidate_2022_vuln_ibm_sh)+" OBJETOS ES  EN 2022 \n")
print("LA FECHA DE MODIFICACION EN "+str(count_modidate_2021_vuln_ibm_sh)+" OBJETOS ES  EN 2021 \n")
print("LA FECHA DE MODIFICACION EN "+str(count_modidate_2020_vuln_ibm_sh)+" OBJETOS ES  EN 2020 \n")
print("LA FECHA DE MODIFICACION EN "+str(count_modidate_2019_vuln_ibm_sh)+" OBJETOS ES  EN 2019 \n")
print("LA FECHA DE MODIFICACION EN "+str(count_modidate_2018_vuln_ibm_sh)+"  OBJETOS ES  ANTERIOR A 2019 \n")
print("\n")
print("**************************PORCENTAJE FECHA DE MODIFICACION OBJETOS VULNERABILIDADES PARTE SMART HOME********************************")
print("\n")
print("EL "+str(float(((count_modidate_2023_vuln_ibm_sh*100)/len_aux_sh)))+" % DE LOS OBJETOS FUERON MODIFICADOS EN 2023 \n")
print("EL "+str(float(((count_modidate_2022_vuln_ibm_sh*100)/len_aux_sh)))+" % DE LOS OBJETOS FUERON MODIFICADOS EN 2022 \n")
print("EL "+str(float(((count_modidate_2021_vuln_ibm_sh*100)/len_aux_sh)))+" % DE LOS OBJETOS FUERON MODIFICADOS EN 2021 \n")
print("EL "+str(float(((count_modidate_2020_vuln_ibm_sh*100)/len_aux_sh)))+" % DE LOS OBJETOS FUERON MODIFICADOS EN 2020 \n")
print("EL "+str(float(((count_modidate_2019_vuln_ibm_sh*100)/len_aux_sh)))+" % DE LOS OBJETOS FUERON MODIFICADOS EN 2019 \n")
print("EL "+str(float(((count_modidate_2018_vuln_ibm_sh*100)/len_aux_sh)))+" % DE LOS OBJETOS FUERON MODIFICADOS ANTES DE 2019 \n")
print("\n")


















print("**************************ESTADÍSTICAS FECHA DE MODIFICACION OBJETOS VULNERABILIDADES PARTE IOT Y SMART HOME CONJUNTAS********************************")
print("\n")
print("LA FECHA DE MODIFICACION EN "+str(count_modidate_2023_vuln_ibm_sh+count_modidate_2023_vuln_ibm_iot)+" OBJETOS ES  EN 2023\n")
print("LA FECHA DE MODIFICACION EN "+str(count_modidate_2022_vuln_ibm_sh+count_modidate_2022_vuln_ibm_iot)+" OBJETOS ES  EN 2022 \n")
print("LA FECHA DE MODIFICACION EN "+str(count_modidate_2021_vuln_ibm_sh+count_modidate_2021_vuln_ibm_iot)+" OBJETOS ES  EN 2021 \n")
print("LA FECHA DE MODIFICACION EN "+str(count_modidate_2020_vuln_ibm_sh+count_modidate_2020_vuln_ibm_iot)+" OBJETOS ES  EN 2020 \n")
print("LA FECHA DE MODIFICACION EN "+str(count_modidate_2019_vuln_ibm_sh+count_modidate_2019_vuln_ibm_iot)+" OBJETOS ES  EN 2019 \n")
print("LA FECHA DE MODIFICACION EN "+str(count_modidate_2018_vuln_ibm_sh+count_modidate_2018_vuln_ibm_iot)+"  OBJETOS ES  ANTERIOR A 2019 \n")
print("\n")
print("**************************PORCENTAJE FECHA DE MODIFICACION OBJETOS VULNERABILIDADES PARTE IOT Y SMART HOME CONJUNTAS********************************")
print("\n")
print("EL "+str(float((((count_modidate_2023_vuln_ibm_sh+count_modidate_2023_vuln_ibm_iot)*100)/(len_aux_iot+len_aux_sh))))+" % DE LOS OBJETOS FUERON MODIFICADOS EN 2023 \n")
print("EL "+str(float((((count_modidate_2022_vuln_ibm_sh+count_modidate_2022_vuln_ibm_iot)*100)/(len_aux_iot+len_aux_sh))))+" % DE LOS OBJETOS FUERON MODIFICADOS EN 2022 \n")
print("EL "+str(float((((count_modidate_2021_vuln_ibm_sh+count_modidate_2021_vuln_ibm_iot)*100)/(len_aux_iot+len_aux_sh))))+" % DE LOS OBJETOS FUERON MODIFICADOS EN 2021 \n")
print("EL "+str(float((((count_modidate_2020_vuln_ibm_sh+count_modidate_2020_vuln_ibm_iot)*100)/(len_aux_iot+len_aux_sh))))+" % DE LOS OBJETOS FUERON MODIFICADOS EN 2020 \n")
print("EL "+str(float((((count_modidate_2019_vuln_ibm_sh+count_modidate_2019_vuln_ibm_iot)*100)/(len_aux_iot+len_aux_sh))))+" % DE LOS OBJETOS FUERON MODIFICADOS EN 2019 \n")
print("EL "+str(float((((count_modidate_2018_vuln_ibm_sh+count_modidate_2018_vuln_ibm_iot)*100)/(len_aux_iot+len_aux_sh))))+" % DE LOS OBJETOS FUERON MODIFICADOS ANTES DE 2019 \n")
print("\n")








