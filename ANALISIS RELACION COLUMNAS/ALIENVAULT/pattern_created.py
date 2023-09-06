
import pandas as pd
from datetime import datetime

#Abro los ficheros con los que voy a tratar


df_alienvault_iot = pd.read_excel('alienvault_iot_2023.xlsx')





#Variables donde almacenare el contador de valores de patron segun el anio de creacion
count_created_date_2023_alienvault_iot_pattern_domainname=0
count_created_date_2023_alienvault_iot_pattern_urlvalue=0
count_created_date_2023_alienvault_iot_pattern_filehashes=0
count_created_date_2023_alienvault_iot_pattern_emailmessage=0
count_created_date_2023_alienvault_iot_pattern_ipv4addr=0
#Variables donde almacenare el contador de OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT creados en un anio especifico
count_created_date_2023_alienvault_iot=0

count_created_date_2022_alienvault_iot_pattern_domainname=0
count_created_date_2022_alienvault_iot_pattern_urlvalue=0
count_created_date_2022_alienvault_iot_pattern_filehashes=0
count_created_date_2022_alienvault_iot_pattern_emailmessage=0
count_created_date_2022_alienvault_iot_pattern_ipv4addr=0
count_created_date_2022_alienvault_iot=0


count_created_date_2021_alienvault_iot_pattern_domainname=0
count_created_date_2021_alienvault_iot_pattern_urlvalue=0
count_created_date_2021_alienvault_iot_pattern_filehashes=0
count_created_date_2021_alienvault_iot_pattern_emailmessage=0
count_created_date_2021_alienvault_iot_pattern_ipv4addr=0
count_created_date_2021_alienvault_iot=0


count_created_date_2020_alienvault_iot_pattern_domainname=0
count_created_date_2020_alienvault_iot_pattern_urlvalue=0
count_created_date_2020_alienvault_iot_pattern_filehashes=0
count_created_date_2020_alienvault_iot_pattern_emailmessage=0
count_created_date_2020_alienvault_iot_pattern_ipv4addr=0
count_created_date_2020_alienvault_iot=0


count_created_date_2019_alienvault_iot_pattern_domainname=0
count_created_date_2019_alienvault_iot_pattern_urlvalue=0
count_created_date_2019_alienvault_iot_pattern_filehashes=0
count_created_date_2019_alienvault_iot_pattern_emailmessage=0
count_created_date_2019_alienvault_iot_pattern_ipv4addr=0
count_created_date_2019_alienvault_iot=0


count_created_date_2018_alienvault_iot_pattern_domainname=0
count_created_date_2018_alienvault_iot_pattern_urlvalue=0
count_created_date_2018_alienvault_iot_pattern_filehashes=0
count_created_date_2018_alienvault_iot_pattern_emailmessage=0
count_created_date_2018_alienvault_iot_pattern_ipv4addr=0
count_created_date_2018_alienvault_iot=0

count_alienvault_iot_pattern_domainname=0
count_alienvault_iot_pattern_urlvalue=0
count_alienvault_iot_pattern_filehashes=0
count_alienvault_iot_pattern_emailmessage=0
count_alienvault_iot_pattern_ipv4addr=0

count_alienvault_iot_total=0
count_alienvault_iot_totalpulses=0


#Comprobamos el anio de CREACION 
for r in range(0,len(df_alienvault_iot["created"])):
    if('[' in df_alienvault_iot["created"][r]):
        #Obtengo los distintos valores de fecha de creacion y patron para la fila actual
        aux=df_alienvault_iot["created"][r].split(",")
        auxx=df_alienvault_iot["pattern"][r].split(",")
        for l in range(0,len(aux)):
            if(len(aux)>0):
                #Compruebo que coincida el numero de valores
                if(len(aux)==len(auxx)):
                    #Obtengo el valor de fecha de creacion
                    aux_str=aux[l].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
                    if(aux_str!='NONE'):
                        count_alienvault_iot_total+=1
                        str_anio_createdate_alienvault_iot=aux_str.split("-")
                        #Obtengo el valor de fecha de creacion
                        anio_createdate_alienvault_iot=int(str_anio_createdate_alienvault_iot[0])
                        #Compruebo el valor de fecha de creacion
                        if(anio_createdate_alienvault_iot >= 2023):
                            count_created_date_2023_alienvault_iot+=1
                            auxx_str=auxx[l].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
                            if(auxx_str!='NONE'):
                                #Compruebo el valor de patron
                                if('domain-name' in auxx_str):
                                    count_alienvault_iot_totalpulses+=1
                                    count_alienvault_iot_pattern_domainname+=1
                                    count_created_date_2023_alienvault_iot_pattern_domainname+=1
                                elif('url:value' in auxx_str):
                                    count_alienvault_iot_totalpulses+=1
                                    count_alienvault_iot_pattern_urlvalue+=1
                                    count_created_date_2023_alienvault_iot_pattern_urlvalue+=1
                                elif('file:hashes' in auxx_str):
                                    count_alienvault_iot_totalpulses+=1
                                    count_alienvault_iot_pattern_filehashes+=1
                                    count_created_date_2023_alienvault_iot_pattern_filehashes+=1 
                                elif('email-message' in auxx_str):
                                    count_alienvault_iot_totalpulses+=1
                                    count_alienvault_iot_pattern_emailmessage+=1
                                    count_created_date_2023_alienvault_iot_pattern_emailmessage+=1
                                elif('ipv4-addr' in auxx_str):
                                    count_alienvault_iot_totalpulses+=1
                                    count_alienvault_iot_pattern_ipv4addr+=1
                                    count_created_date_2023_alienvault_iot_pattern_ipv4addr+=1


                        elif(anio_createdate_alienvault_iot >= 2022):
                            count_created_date_2022_alienvault_iot+=1
                            auxx_str=auxx[l].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
                            if(auxx_str!='NONE'):
                                if('domain-name' in auxx_str):
                                    count_alienvault_iot_totalpulses+=1
                                    count_alienvault_iot_pattern_domainname+=1
                                    count_created_date_2022_alienvault_iot_pattern_domainname+=1
                                elif('url:value' in auxx_str):
                                    count_alienvault_iot_totalpulses+=1
                                    count_alienvault_iot_pattern_urlvalue+=1
                                    count_created_date_2022_alienvault_iot_pattern_urlvalue+=1
                                elif('file:hashes' in auxx_str):
                                    count_alienvault_iot_totalpulses+=1
                                    count_alienvault_iot_pattern_filehashes+=1
                                    count_created_date_2022_alienvault_iot_pattern_filehashes+=1 
                                elif('email-message' in auxx_str):
                                    count_alienvault_iot_totalpulses+=1
                                    count_alienvault_iot_pattern_emailmessage+=1
                                    count_created_date_2022_alienvault_iot_pattern_emailmessage+=1
                                elif('ipv4-addr' in auxx_str):
                                    count_alienvault_iot_totalpulses+=1
                                    count_alienvault_iot_pattern_ipv4addr+=1
                                    count_created_date_2022_alienvault_iot_pattern_ipv4addr+=1

                        elif(anio_createdate_alienvault_iot >= 2021):
                            count_created_date_2021_alienvault_iot+=1
                            auxx_str=auxx[l].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
                            if(auxx_str!='NONE'):
                                if('domain-name' in auxx_str):
                                    count_alienvault_iot_totalpulses+=1
                                    count_alienvault_iot_pattern_domainname+=1
                                    count_created_date_2021_alienvault_iot_pattern_domainname+=1
                                elif('url:value' in auxx_str):
                                    count_alienvault_iot_totalpulses+=1
                                    count_alienvault_iot_pattern_urlvalue+=1
                                    count_created_date_2021_alienvault_iot_pattern_urlvalue+=1
                                elif('file:hashes' in auxx_str):
                                    count_alienvault_iot_totalpulses+=1
                                    count_alienvault_iot_pattern_filehashes+=1
                                    count_created_date_2021_alienvault_iot_pattern_filehashes+=1
                                elif('email-message' in auxx_str):
                                    count_alienvault_iot_totalpulses+=1
                                    count_alienvault_iot_pattern_emailmessage+=1
                                    count_created_date_2021_alienvault_iot_pattern_emailmessage+=1
                                elif('ipv4-addr' in auxx_str):
                                    count_alienvault_iot_totalpulses+=1
                                    count_alienvault_iot_pattern_ipv4addr+=1
                                    count_created_date_2021_alienvault_iot_pattern_ipv4addr+=1

                        elif(anio_createdate_alienvault_iot >= 2020):
                            count_created_date_2020_alienvault_iot+=1
                            auxx_str=auxx[l].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
                            if(auxx_str!='NONE'):
                                if('domain-name' in auxx_str):
                                    count_alienvault_iot_totalpulses+=1
                                    count_alienvault_iot_pattern_domainname+=1
                                    count_created_date_2020_alienvault_iot_pattern_domainname+=1
                                elif('url:value' in auxx_str):
                                    count_alienvault_iot_totalpulses+=1
                                    count_alienvault_iot_pattern_urlvalue+=1
                                    count_created_date_2020_alienvault_iot_pattern_urlvalue+=1
                                elif('file:hashes' in auxx_str):
                                    count_alienvault_iot_totalpulses+=1
                                    count_alienvault_iot_pattern_filehashes+=1
                                    count_created_date_2020_alienvault_iot_pattern_filehashes+=1 
                                elif('email-message' in auxx_str):
                                    count_alienvault_iot_totalpulses+=1
                                    count_alienvault_iot_pattern_emailmessage+=1
                                    count_created_date_2020_alienvault_iot_pattern_emailmessage+=1
                                elif('ipv4-addr' in auxx_str):
                                    count_alienvault_iot_totalpulses+=1
                                    count_alienvault_iot_pattern_ipv4addr+=1
                                    count_created_date_2020_alienvault_iot_pattern_ipv4addr+=1


                        elif(anio_createdate_alienvault_iot >= 2019):
                            count_created_date_2019_alienvault_iot+=1
                            auxx_str=auxx[l].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
                            if(auxx_str!='NONE'):
                                if('domain-name' in auxx_str):
                                    count_alienvault_iot_totalpulses+=1
                                    count_alienvault_iot_pattern_domainname+=1
                                    count_created_date_2019_alienvault_iot_pattern_domainname+=1
                                elif('url:value' in auxx_str):
                                    count_alienvault_iot_totalpulses+=1
                                    count_alienvault_iot_pattern_urlvalue+=1
                                    count_created_date_2019_alienvault_iot_pattern_urlvalue+=1
                                elif('file:hashes' in auxx_str):
                                    count_alienvault_iot_totalpulses+=1
                                    count_alienvault_iot_pattern_filehashes+=1
                                    count_created_date_2019_alienvault_iot_pattern_filehashes+=1
                                elif('email-message' in auxx_str):
                                    count_alienvault_iot_totalpulses+=1
                                    count_alienvault_iot_pattern_emailmessage+=1
                                    count_created_date_2019_alienvault_iot_pattern_emailmessage+=1
                                elif('ipv4-addr' in auxx_str):
                                    count_alienvault_iot_totalpulses+=1
                                    count_alienvault_iot_pattern_ipv4addr+=1
                                    count_created_date_2019_alienvault_iot_pattern_ipv4addr+=1


                        else: 
                            count_created_date_2018_alienvault_iot+=1
                            auxx_str=auxx[l].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
                            if(auxx_str!='NONE'):
                                if('domain-name' in auxx_str):
                                    count_alienvault_iot_totalpulses+=1
                                    count_alienvault_iot_pattern_domainname+=1
                                    count_created_date_2018_alienvault_iot_pattern_domainname+=1
                                elif('url:value' in auxx_str):
                                    count_alienvault_iot_totalpulses+=1
                                    count_alienvault_iot_pattern_urlvalue+=1
                                    count_created_date_2018_alienvault_iot_pattern_urlvalue+=1
                                elif('file:hashes' in auxx_str):
                                    count_alienvault_iot_totalpulses+=1
                                    count_alienvault_iot_pattern_filehashes+=1
                                    count_created_date_2018_alienvault_iot_pattern_filehashes+=1
                                elif('email-message' in auxx_str):
                                    count_alienvault_iot_totalpulses+=1
                                    count_alienvault_iot_pattern_emailmessage+=1
                                    count_created_date_2018_alienvault_iot_pattern_emailmessage+=1
                                elif('ipv4-addr' in auxx_str):
                                    count_alienvault_iot_totalpulses+=1
                                    count_alienvault_iot_pattern_ipv4addr+=1
                                    count_created_date_2018_alienvault_iot_pattern_ipv4addr+=1
    else:
        #Si existe un unico valor de fecha de creacion para la fila actual, obtengo el anio de creacion
        str_anio_createdate_alienvault_iot=df_alienvault_iot["created"][r].split("-")
        anio_createdate_alienvault_iot=int(str_anio_createdate_alienvault_iot[0])
        count_alienvault_iot_total+=1
        #Obtengo los valores de patron para la fila actual
        auxx=df_alienvault_iot["pattern"][r].split(",")
        
        for l in range(0,len(auxx)):
            if(len(auxx)>0):
                auxx_str=auxx[l].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
                if(auxx_str!='NONE'):
                    count_alienvault_iot_totalpulses+=1
                    #Compruebo el anio de creacion
                    if(anio_createdate_alienvault_iot >= 2023):
                        count_created_date_2023_alienvault_iot+=1
                        #Compruebo el valor de patron
                        if('domain-name' in auxx_str):
                            count_alienvault_iot_pattern_domainname+=1
                            count_created_date_2023_alienvault_iot_pattern_domainname+=1  
                        elif('url:value' in auxx_str):
                            count_alienvault_iot_pattern_urlvalue+=1
                            count_created_date_2023_alienvault_iot_pattern_urlvalue+=1  
                        elif('file:hashes' in auxx_str):
                            count_alienvault_iot_pattern_filehashes+=1
                            count_created_date_2023_alienvault_iot_pattern_filehashes+=1
                        elif('email-message' in auxx_str):
                            count_alienvault_iot_pattern_emailmessage+=1
                            count_created_date_2023_alienvault_iot_pattern_emailmessage+=1
                        elif('ipv4-addr' in auxx_str):
                            count_alienvault_iot_pattern_ipv4addr+=1
                            count_created_date_2023_alienvault_iot_pattern_ipv4addr+=1

                    elif(anio_createdate_alienvault_iot >= 2022):
                        count_created_date_2022_alienvault_iot+=1
                        if('domain-name' in auxx_str):
                            count_alienvault_iot_pattern_domainname+=1
                            count_created_date_2022_alienvault_iot_pattern_domainname+=1  
                        elif('url:value' in auxx_str):
                            count_alienvault_iot_pattern_urlvalue+=1
                            count_created_date_2022_alienvault_iot_pattern_urlvalue+=1  
                        elif('file:hashes' in auxx_str):
                            count_alienvault_iot_pattern_filehashes+=1
                            count_created_date_2022_alienvault_iot_pattern_filehashes+=1
                        elif('email-message' in auxx_str):
                            count_alienvault_iot_pattern_emailmessage+=1
                            count_created_date_2022_alienvault_iot_pattern_emailmessage+=1
                        elif('ipv4-addr' in auxx_str):
                            count_alienvault_iot_pattern_ipv4addr+=1
                            count_created_date_2022_alienvault_iot_pattern_ipv4addr+=1
                    elif(anio_createdate_alienvault_iot >= 2021):
                        count_created_date_2021_alienvault_iot+=1
                        if('domain-name' in auxx_str):
                            count_alienvault_iot_pattern_domainname+=1
                            count_created_date_2021_alienvault_iot_pattern_domainname+=1  
                        elif('url:value' in auxx_str):
                            count_alienvault_iot_pattern_urlvalue+=1
                            count_created_date_2021_alienvault_iot_pattern_urlvalue+=1  
                        elif('file:hashes' in auxx_str):
                            count_alienvault_iot_pattern_filehashes+=1
                            count_created_date_2021_alienvault_iot_pattern_filehashes+=1
                        elif('email-message' in auxx_str):
                            count_alienvault_iot_pattern_emailmessage+=1
                            count_created_date_2021_alienvault_iot_pattern_emailmessage+=1
                        elif('ipv4-addr' in auxx_str):
                            count_alienvault_iot_pattern_ipv4addr+=1
                            count_created_date_2021_alienvault_iot_pattern_ipv4addr+=1
                    elif(anio_createdate_alienvault_iot >= 2020):
                        count_created_date_2020_alienvault_iot+=1
                        if('domain-name' in auxx_str):
                            count_alienvault_iot_pattern_domainname+=1
                            count_created_date_2020_alienvault_iot_pattern_domainname+=1  
                        elif('url:value' in auxx_str):
                            count_alienvault_iot_pattern_urlvalue+=1
                            count_created_date_2020_alienvault_iot_pattern_urlvalue+=1  
                        elif('file:hashes' in auxx_str):
                            count_alienvault_iot_pattern_filehashes+=1
                            count_created_date_2020_alienvault_iot_pattern_filehashes+=1
                        elif('email-message' in auxx_str):
                            count_alienvault_iot_pattern_emailmessage+=1
                            count_created_date_2020_alienvault_iot_pattern_emailmessage+=1
                        elif('ipv4-addr' in auxx_str):
                            count_alienvault_iot_pattern_ipv4addr+=1
                            count_created_date_2020_alienvault_iot_pattern_ipv4addr+=1
                    elif(anio_createdate_alienvault_iot >= 2019):
                        count_created_date_2019_alienvault_iot+=1
                        if('domain-name' in auxx_str):
                            count_alienvault_iot_pattern_domainname+=1
                            count_created_date_2019_alienvault_iot_pattern_domainname+=1  
                        elif('url:value' in auxx_str):
                            count_alienvault_iot_pattern_urlvalue+=1
                            count_created_date_2019_alienvault_iot_pattern_urlvalue+=1  
                        elif('file:hashes' in auxx_str):
                            count_alienvault_iot_pattern_filehashes+=1
                            count_created_date_2019_alienvault_iot_pattern_filehashes+=1
                        elif('email-message' in auxx_str):
                            count_alienvault_iot_pattern_emailmessage+=1
                            count_created_date_2019_alienvault_iot_pattern_emailmessage+=1
                        elif('ipv4-addr' in auxx_str):
                            count_alienvault_iot_pattern_ipv4addr+=1
                            count_created_date_2019_alienvault_iot_pattern_ipv4addr+=1
                    else:
                        count_created_date_2018_alienvault_iot+=1
                        if('domain-name' in auxx_str):
                            count_alienvault_iot_pattern_domainname+=1
                            count_created_date_2018_alienvault_iot_pattern_domainname+=1  
                        elif('url:value' in auxx_str):
                            count_alienvault_iot_pattern_urlvalue+=1
                            count_created_date_2018_alienvault_iot_pattern_urlvalue+=1  
                        elif('file:hashes' in auxx_str):
                            count_alienvault_iot_pattern_filehashes+=1
                            count_created_date_2018_alienvault_iot_pattern_filehashes+=1
                        elif('email-message' in auxx_str):
                            count_alienvault_iot_pattern_emailmessage+=1
                            count_created_date_2018_alienvault_iot_pattern_emailmessage+=1
                        elif('ipv4-addr' in auxx_str):
                            count_alienvault_iot_pattern_ipv4addr+=1
                            count_created_date_2018_alienvault_iot_pattern_ipv4addr+=1
                
                
print("******************ESTADÍSTICAS TIPO DE PATRÓN/FECHA DE CREACIÓN OBJETOS TIPO INDICADOR ALIENVAULT PARTE IOT******************")
print("\n")                            
                
print("\n")
print(" DE UN TOTAL DE "+str(count_alienvault_iot_totalpulses)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT :\n") 
print("\n")
print("   - LAS ESTADISTICAS DE FECHA DE CREACION SON LAS SIGUIENTES:  \n")
print("      -    EN  "+str(count_created_date_2023_alienvault_iot)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2023. LAS ESTADÍSTICAS DE PATRÓN SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(count_created_date_2023_alienvault_iot_pattern_domainname)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT CREADOS EN 2023, EL PATRÓN ES NOMBRE DE DOMINIO ")
print("            -    EN  "+str(count_created_date_2023_alienvault_iot_pattern_urlvalue)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT CREADOS EN 2023, EL PATRÓN ES VALOR DE URL")
print("            -    EN  "+str(count_created_date_2023_alienvault_iot_pattern_filehashes)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT CREADOS EN 2023, EL PATRÓN ES UN HASH DE UN ARCHIVO ")
print("            -    EN  "+str(count_created_date_2023_alienvault_iot_pattern_filehashes)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT CREADOS EN 2023, EL PATRÓN ES MENSAJE DE EMAIL ")
print("            -    EN  "+str(count_created_date_2023_alienvault_iot_pattern_ipv4addr)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT CREADOS EN 2023, EL PATRÓN ES UNA DIRECCIÓN IPV4 ")
print("\n")
print("      -    EN  "+str(count_created_date_2022_alienvault_iot)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2022. LAS ESTADÍSTICAS DE PATRÓN SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(count_created_date_2022_alienvault_iot_pattern_domainname)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT CREADOS EN 2022, EL PATRÓN ES NOMBRE DE DOMINIO ")
print("            -    EN  "+str(count_created_date_2022_alienvault_iot_pattern_urlvalue)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT CREADOS EN 2022, EL PATRÓN ES VALOR DE URL")
print("            -    EN  "+str(count_created_date_2022_alienvault_iot_pattern_filehashes)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT CREADOS EN 2022, EL PATRÓN ES UN HASH DE UN ARCHIVO ")
print("            -    EN  "+str(count_created_date_2022_alienvault_iot_pattern_filehashes)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT CREADOS EN 2022, EL PATRÓN ES MENSAJE DE EMAIL ")
print("            -    EN  "+str(count_created_date_2022_alienvault_iot_pattern_ipv4addr)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT CREADOS EN 2022, EL PATRÓN ES UNA DIRECCIÓN IPV4 ")
print("\n")
print("      -    EN  "+str(count_created_date_2021_alienvault_iot)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2021. LAS ESTADÍSTICAS DE PATRÓN SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(count_created_date_2021_alienvault_iot_pattern_domainname)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT CREADOS EN 2021, EL PATRÓN ES NOMBRE DE DOMINIO ")
print("            -    EN  "+str(count_created_date_2021_alienvault_iot_pattern_urlvalue)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT CREADOS EN 2021, EL PATRÓN ES VALOR DE URL")
print("            -    EN  "+str(count_created_date_2021_alienvault_iot_pattern_filehashes)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT CREADOS EN 2021, EL PATRÓN ES UN HASH DE UN ARCHIVO ")
print("            -    EN  "+str(count_created_date_2021_alienvault_iot_pattern_filehashes)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT CREADOS EN 2021, EL PATRÓN ES MENSAJE DE EMAIL ")
print("            -    EN  "+str(count_created_date_2021_alienvault_iot_pattern_ipv4addr)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT CREADOS EN 2021, EL PATRÓN ES UNA DIRECCIÓN IPV4 ")
print("\n")
print("      -    EN  "+str(count_created_date_2020_alienvault_iot)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2020. LAS ESTADÍSTICAS DE PATRÓN SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(count_created_date_2020_alienvault_iot_pattern_domainname)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT CREADOS EN 2020, EL PATRÓN ES NOMBRE DE DOMINIO ")
print("            -    EN  "+str(count_created_date_2020_alienvault_iot_pattern_urlvalue)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT CREADOS EN 2020, EL PATRÓN ES VALOR DE URL")
print("            -    EN  "+str(count_created_date_2020_alienvault_iot_pattern_filehashes)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT CREADOS EN 2020, EL PATRÓN ES UN HASH DE UN ARCHIVO ")
print("            -    EN  "+str(count_created_date_2020_alienvault_iot_pattern_filehashes)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT CREADOS EN 2020, EL PATRÓN ES MENSAJE DE EMAIL ")
print("            -    EN  "+str(count_created_date_2020_alienvault_iot_pattern_ipv4addr)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT CREADOS EN 2020, EL PATRÓN ES UNA DIRECCIÓN IPV4 ")
print("\n")
print("      -    EN  "+str(count_created_date_2019_alienvault_iot)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2019. LAS ESTADÍSTICAS DE PATRÓN SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(count_created_date_2019_alienvault_iot_pattern_domainname)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT CREADOS EN 2019, EL PATRÓN ES NOMBRE DE DOMINIO ")
print("            -    EN  "+str(count_created_date_2019_alienvault_iot_pattern_urlvalue)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT CREADOS EN 2019, EL PATRÓN ES VALOR DE URL")
print("            -    EN  "+str(count_created_date_2019_alienvault_iot_pattern_filehashes)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT CREADOS EN 2019, EL PATRÓN ES UN HASH DE UN ARCHIVO ")
print("            -    EN  "+str(count_created_date_2019_alienvault_iot_pattern_filehashes)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT CREADOS EN 2019, EL PATRÓN ES MENSAJE DE EMAIL ")
print("            -    EN  "+str(count_created_date_2019_alienvault_iot_pattern_ipv4addr)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT CREADOS EN 2019, EL PATRÓN ES UNA DIRECCIÓN IPV4 ")
print("\n")
print("      -    EN  "+str(count_created_date_2018_alienvault_iot)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2018 O ANTERIOR. LAS ESTADÍSTICAS DE PATRÓN SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(count_created_date_2018_alienvault_iot_pattern_domainname)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT CREADOS EN 2018 O ANTES, EL PATRÓN ES NOMBRE DE DOMINIO ")
print("            -    EN  "+str(count_created_date_2018_alienvault_iot_pattern_urlvalue)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT CREADOS EN 2018 O ANTES, EL PATRÓN ES VALOR DE URL")
print("            -    EN  "+str(count_created_date_2018_alienvault_iot_pattern_filehashes)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT CREADOS EN 2018 O ANTES, EL PATRÓN ES UN HASH DE UN ARCHIVO ")
print("            -    EN  "+str(count_created_date_2018_alienvault_iot_pattern_filehashes)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT CREADOS EN 2018, EL PATRÓN ES MENSAJE DE EMAIL ")
print("            -    EN  "+str(count_created_date_2018_alienvault_iot_pattern_ipv4addr)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT CREADOS EN 2018, EL PATRÓN ES UNA DIRECCIÓN IPV4 ")
print("\n")
print("   - LAS ESTADISTICAS DE PATRON SON LAS SIGUIENTES:  \n")
print("      -    EN  "+str(count_alienvault_iot_pattern_domainname)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT EL PATRÓN ES NOMBRE DE DOMINIO. LAS ESTADÍSTICAS DE FECHA DE CREACION SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(count_created_date_2023_alienvault_iot_pattern_domainname)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2023 ")
print("            -    EN  "+str(count_created_date_2022_alienvault_iot_pattern_domainname)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2022")
print("            -    EN  "+str(count_created_date_2021_alienvault_iot_pattern_domainname)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2021 ")
print("            -    EN  "+str(count_created_date_2020_alienvault_iot_pattern_domainname)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2020 ")
print("            -    EN  "+str(count_created_date_2019_alienvault_iot_pattern_domainname)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2019")
print("            -    EN  "+str(count_created_date_2018_alienvault_iot_pattern_domainname)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2018 O ANTERIOR ")
print("\n")
print("      -    EN  "+str(count_alienvault_iot_pattern_urlvalue)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT EL PATRÓN ES VALOR DE URL. LAS ESTADÍSTICAS DE FECHA DE CREACION SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(count_created_date_2023_alienvault_iot_pattern_urlvalue)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2023 ")
print("            -    EN  "+str(count_created_date_2022_alienvault_iot_pattern_urlvalue)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2022")
print("            -    EN  "+str(count_created_date_2021_alienvault_iot_pattern_urlvalue)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2021 ")
print("            -    EN  "+str(count_created_date_2020_alienvault_iot_pattern_urlvalue)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2020 ")
print("            -    EN  "+str(count_created_date_2019_alienvault_iot_pattern_urlvalue)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2019")
print("            -    EN  "+str(count_created_date_2018_alienvault_iot_pattern_urlvalue)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2018 O ANTERIOR ")
print("\n")
print("      -    EN  "+str(count_alienvault_iot_pattern_filehashes)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT EL PATRÓN ES UN HASH DE UN ARCHIVO. LAS ESTADÍSTICAS DE FECHA DE CREACION SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(count_created_date_2023_alienvault_iot_pattern_filehashes)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2023 ")
print("            -    EN  "+str(count_created_date_2022_alienvault_iot_pattern_filehashes)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2022")
print("            -    EN  "+str(count_created_date_2021_alienvault_iot_pattern_filehashes)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2021 ")
print("            -    EN  "+str(count_created_date_2020_alienvault_iot_pattern_filehashes)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2020 ")
print("            -    EN  "+str(count_created_date_2019_alienvault_iot_pattern_filehashes)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2019")
print("            -    EN  "+str(count_created_date_2018_alienvault_iot_pattern_filehashes)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2018 O ANTERIOR ")
print("\n")
print("      -    EN  "+str(count_alienvault_iot_pattern_emailmessage)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT EL PATRÓN ES MENSAJE DE EMAIL. LAS ESTADÍSTICAS DE FECHA DE CREACION SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(count_created_date_2023_alienvault_iot_pattern_emailmessage)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2023 ")
print("            -    EN  "+str(count_created_date_2022_alienvault_iot_pattern_emailmessage)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2022")
print("            -    EN  "+str(count_created_date_2021_alienvault_iot_pattern_emailmessage)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2021 ")
print("            -    EN  "+str(count_created_date_2020_alienvault_iot_pattern_emailmessage)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2020 ")
print("            -    EN  "+str(count_created_date_2019_alienvault_iot_pattern_emailmessage)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2019")
print("            -    EN  "+str(count_created_date_2018_alienvault_iot_pattern_emailmessage)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2018 O ANTERIOR ")
print("\n")
print("      -    EN  "+str(count_alienvault_iot_pattern_ipv4addr)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT EL PATRÓN ES UNA DIRECCIÓN IPV4. LAS ESTADÍSTICAS DE FECHA DE CREACION SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(count_created_date_2023_alienvault_iot_pattern_ipv4addr)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2023 ")
print("            -    EN  "+str(count_created_date_2022_alienvault_iot_pattern_ipv4addr)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2022")
print("            -    EN  "+str(count_created_date_2021_alienvault_iot_pattern_ipv4addr)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2021 ")
print("            -    EN  "+str(count_created_date_2020_alienvault_iot_pattern_ipv4addr)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2020 ")
print("            -    EN  "+str(count_created_date_2019_alienvault_iot_pattern_ipv4addr)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2019")
print("            -    EN  "+str(count_created_date_2018_alienvault_iot_pattern_ipv4addr)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2018 O ANTERIOR ")
print("\n")








print("******************PORCENTAJE TIPO DE PATRÓN/FECHA DE CREACIÓN OBJETOS TIPO INDICADOR ALIENVAULT PARTE IOT******************")
print("\n")                            
                
print("\n")
print(" DE UN TOTAL DE "+str(count_alienvault_iot_totalpulses)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT :\n") 
print("\n")
print("   - LOS PORCENTAJES DE FECHA DE CREACION SON LOS SIGUIENTES:  \n")
if(count_created_date_2023_alienvault_iot>0):
    print("      -    EN EL  "+str(float(((count_created_date_2023_alienvault_iot*100)/count_alienvault_iot_totalpulses)))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2023. LOS PORCENTAJES DE PATRÓN SON LOS SIGUIENTES:  \n")
    print("\n")
    print("            -    EN EL  "+str(float(((count_created_date_2023_alienvault_iot_pattern_domainname*100)/count_created_date_2023_alienvault_iot)))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT CREADOS EN 2023, EL PATRÓN ES NOMBRE DE DOMINIO ")
    print("            -    EN EL  "+str(float(((count_created_date_2023_alienvault_iot_pattern_urlvalue*100)/count_created_date_2023_alienvault_iot)))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT CREADOS EN 2023, EL PATRÓN ES VALOR DE URL")
    print("            -    EN EL  "+str(float(((count_created_date_2023_alienvault_iot_pattern_filehashes*100)/count_created_date_2023_alienvault_iot)))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT CREADOS EN 2023, EL PATRÓN ES UN HASH DE UN ARCHIVO ")
    print("            -    EN EL  "+str(float(((count_created_date_2023_alienvault_iot_pattern_emailmessage*100)/count_created_date_2023_alienvault_iot)))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT CREADOS EN 2023, EL PATRÓN ES MENSAJE DE EMAIL ")
    print("            -    EN EL  "+str(float(((count_created_date_2023_alienvault_iot_pattern_ipv4addr*100)/count_created_date_2023_alienvault_iot)))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT CREADOS EN 2023, EL PATRÓN ES UNA DIRECCIÓN IPV4 ")
    print("\n")
if(count_created_date_2022_alienvault_iot>0):
    print("      -    EN EL  "+str(float(((count_created_date_2022_alienvault_iot*100)/count_alienvault_iot_totalpulses)))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2022. LOS PORCENTAJESS DE PATRÓN SON LAS SIGUIENTES:  \n")
    print("\n")
    print("            -    EN EL  "+str(float(((count_created_date_2022_alienvault_iot_pattern_domainname*100)/count_created_date_2022_alienvault_iot)))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT CREADOS EN 2022, EL PATRÓN ES NOMBRE DE DOMINIO ")
    print("            -    EN EL  "+str(float(((count_created_date_2022_alienvault_iot_pattern_urlvalue*100)/count_created_date_2022_alienvault_iot)))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT CREADOS EN 2022, EL PATRÓN ES VALOR DE URL")
    print("            -    EN EL  "+str(float(((count_created_date_2022_alienvault_iot_pattern_filehashes*100)/count_created_date_2022_alienvault_iot)))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT CREADOS EN 2022, EL PATRÓN ES UN HASH DE UN ARCHIVO ")
    print("            -    EN EL  "+str(float(((count_created_date_2022_alienvault_iot_pattern_emailmessage*100)/count_created_date_2022_alienvault_iot)))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT CREADOS EN 2022, EL PATRÓN ES MENSAJE DE EMAIL ")
    print("            -    EN EL  "+str(float(((count_created_date_2022_alienvault_iot_pattern_ipv4addr*100)/count_created_date_2022_alienvault_iot)))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT CREADOS EN 2022, EL PATRÓN ES UNA DIRECCIÓN IPV4 ")
    print("\n")
if(count_created_date_2021_alienvault_iot>0):
    print("      -    EN EL  "+str(float(((count_created_date_2021_alienvault_iot*100)/count_alienvault_iot_totalpulses)))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2021. LOS PORCENTAJES DE PATRÓN SON LOS SIGUIENTES:  \n")
    print("\n")
    print("            -    EN EL  "+str(float(((count_created_date_2021_alienvault_iot_pattern_domainname*100)/count_created_date_2021_alienvault_iot)))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT CREADOS EN 2021, EL PATRÓN ES NOMBRE DE DOMINIO ")
    print("            -    EN EL  "+str(float(((count_created_date_2021_alienvault_iot_pattern_urlvalue*100)/count_created_date_2021_alienvault_iot)))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT CREADOS EN 2021, EL PATRÓN ES VALOR DE URL")
    print("            -    EN EL  "+str(float(((count_created_date_2021_alienvault_iot_pattern_filehashes*100)/count_created_date_2021_alienvault_iot)))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT CREADOS EN 2021, EL PATRÓN ES UN HASH DE UN ARCHIVO ")
    print("            -    EN EL  "+str(float(((count_created_date_2021_alienvault_iot_pattern_emailmessage*100)/count_created_date_2021_alienvault_iot)))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT CREADOS EN 2021, EL PATRÓN ES MENSAJE DE EMAIL ")
    print("            -    EN EL  "+str(float(((count_created_date_2021_alienvault_iot_pattern_ipv4addr*100)/count_created_date_2021_alienvault_iot)))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT CREADOS EN 2021, EL PATRÓN ES UNA DIRECCIÓN IPV4 ")
    print("\n")
if(count_created_date_2020_alienvault_iot>0):
    print("      -    EN EL  "+str(float(((count_created_date_2020_alienvault_iot*100)/count_alienvault_iot_totalpulses)))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2020. LOS PORCENTAJES DE PATRÓN SON LOS SIGUIENTES:  \n")
    print("\n")
    print("            -    EN EL  "+str(float(((count_created_date_2020_alienvault_iot_pattern_domainname*100)/count_created_date_2020_alienvault_iot)))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT CREADOS EN 2020, EL PATRÓN ES NOMBRE DE DOMINIO ")
    print("            -    EN EL  "+str(float(((count_created_date_2020_alienvault_iot_pattern_urlvalue*100)/count_created_date_2020_alienvault_iot)))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT CREADOS EN 2020, EL PATRÓN ES VALOR DE URL")
    print("            -    EN EL  "+str(float(((count_created_date_2020_alienvault_iot_pattern_filehashes*100)/count_created_date_2020_alienvault_iot)))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT CREADOS EN 2020, EL PATRÓN ES UN HASH DE UN ARCHIVO ")
    print("            -    EN EL  "+str(float(((count_created_date_2020_alienvault_iot_pattern_emailmessage*100)/count_created_date_2020_alienvault_iot)))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT CREADOS EN 2020, EL PATRÓN ES MENSAJE DE EMAIL ")
    print("            -    EN EL  "+str(float(((count_created_date_2020_alienvault_iot_pattern_ipv4addr*100)/count_created_date_2020_alienvault_iot)))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT CREADOS EN 2020, EL PATRÓN ES UNA DIRECCIÓN IPV4 ")
    print("\n")
if(count_created_date_2019_alienvault_iot>0):
    print("      -    EN EL  "+str(float(((count_created_date_2019_alienvault_iot*100)/count_alienvault_iot_totalpulses)))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2019. LOS PORCENTAJES DE PATRÓN SON LOS SIGUIENTES:  \n")
    print("\n")
    print("            -    EN EL  "+str(float(((count_created_date_2019_alienvault_iot_pattern_domainname*100)/count_created_date_2019_alienvault_iot)))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT CREADOS EN 2019, EL PATRÓN ES NOMBRE DE DOMINIO ")
    print("            -    EN EL  "+str(float(((count_created_date_2019_alienvault_iot_pattern_urlvalue*100)/count_created_date_2019_alienvault_iot)))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT CREADOS EN 2019, EL PATRÓN ES VALOR DE URL")
    print("            -    EN EL  "+str(float(((count_created_date_2019_alienvault_iot_pattern_filehashes*100)/count_created_date_2019_alienvault_iot)))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT CREADOS EN 2019, EL PATRÓN ES UN HASH DE UN ARCHIVO ")
    print("            -    EN EL  "+str(float(((count_created_date_2019_alienvault_iot_pattern_emailmessage*100)/count_created_date_2019_alienvault_iot)))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT CREADOS EN 2019, EL PATRÓN ES MENSAJE DE EMAIL ")
    print("            -    EN EL  "+str(float(((count_created_date_2019_alienvault_iot_pattern_ipv4addr*100)/count_created_date_2019_alienvault_iot)))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT CREADOS EN 2019, EL PATRÓN ES UNA DIRECCIÓN IPV4 ")
    print("\n")
if(count_created_date_2018_alienvault_iot>0):
    print("      -    EN EL  "+str(float(((count_created_date_2018_alienvault_iot*100)/count_alienvault_iot_totalpulses)))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2018 O ANTERIOR. LOS PORCENTAJES DE PATRÓN SON LOS SIGUIENTES:  \n")
    print("\n")
    print("            -    EN EL  "+str(float(((count_created_date_2018_alienvault_iot_pattern_domainname*100)/count_created_date_2018_alienvault_iot)))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT CREADOS EN 2018 O ANTERIORMENTE, EL PATRÓN ES NOMBRE DE DOMINIO ")
    print("            -    EN EL  "+str(float(((count_created_date_2018_alienvault_iot_pattern_urlvalue*100)/count_created_date_2018_alienvault_iot)))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT CREADOS EN 2018 O ANTERIORMENTE, EL PATRÓN ES VALOR DE URL")
    print("            -    EN EL  "+str(float(((count_created_date_2018_alienvault_iot_pattern_filehashes*100)/count_created_date_2018_alienvault_iot)))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT CREADOS EN 2018 O ANTERIORMENTE, EL PATRÓN ES UN HASH DE UN ARCHIVO ")
    print("            -    EN EL  "+str(float(((count_created_date_2018_alienvault_iot_pattern_emailmessage*100)/count_created_date_2018_alienvault_iot)))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT CREADOS EN 2018, EL PATRÓN ES MENSAJE DE EMAIL ")
    print("            -    EN EL  "+str(float(((count_created_date_2018_alienvault_iot_pattern_ipv4addr*100)/count_created_date_2018_alienvault_iot)))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT CREADOS EN 2018, EL PATRÓN ES UNA DIRECCIÓN IPV4 ")
    print("\n")
print("   - LOS PORCENTAJES DE PATRON SON LOS SIGUIENTES:  \n")
if(count_alienvault_iot_pattern_domainname>0):
    print("      -    EN EL  "+str(float(((count_alienvault_iot_pattern_domainname*100)/count_alienvault_iot_totalpulses)))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT EL PATRÓN ES NOMBRE DE DOMINIO. LOS PORCENTAJES DE FECHA DE CREACION SON LOS SIGUIENTES:  \n")
    print("\n")
    print("            -    EN EL  "+str(float(((count_created_date_2023_alienvault_iot_pattern_domainname*100)/count_alienvault_iot_pattern_domainname)))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2023 ")
    print("            -    EN EL  "+str(float(((count_created_date_2022_alienvault_iot_pattern_domainname*100)/count_alienvault_iot_pattern_domainname)))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2022")
    print("            -    EN EL  "+str(float(((count_created_date_2021_alienvault_iot_pattern_domainname*100)/count_alienvault_iot_pattern_domainname)))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2021 ")
    print("            -    EN EL  "+str(float(((count_created_date_2020_alienvault_iot_pattern_domainname*100)/count_alienvault_iot_pattern_domainname)))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2020 ")
    print("            -    EN EL  "+str(float(((count_created_date_2019_alienvault_iot_pattern_domainname*100)/count_alienvault_iot_pattern_domainname)))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2019")
    print("            -    EN EL  "+str(float(((count_created_date_2018_alienvault_iot_pattern_domainname*100)/count_alienvault_iot_pattern_domainname)))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2018 O ANTERIOR ")
    print("\n")
if(count_alienvault_iot_pattern_urlvalue>0):
    print("      -    EN EL  "+str(float(((count_alienvault_iot_pattern_urlvalue*100)/count_alienvault_iot_totalpulses)))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT EL PATRÓN ES VALOR DE URL. LOS PORCENTAJES DE FECHA DE CREACION SON LOS SIGUIENTES:  \n")
    print("\n")
    print("            -    EN EL  "+str(float(((count_created_date_2023_alienvault_iot_pattern_urlvalue*100)/count_alienvault_iot_pattern_urlvalue)))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2023 ")
    print("            -    EN EL  "+str(float(((count_created_date_2022_alienvault_iot_pattern_urlvalue*100)/count_alienvault_iot_pattern_urlvalue)))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2022")
    print("            -    EN EL  "+str(float(((count_created_date_2021_alienvault_iot_pattern_urlvalue*100)/count_alienvault_iot_pattern_urlvalue)))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2021 ")
    print("            -    EN EL  "+str(float(((count_created_date_2020_alienvault_iot_pattern_urlvalue*100)/count_alienvault_iot_pattern_urlvalue)))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2020 ")
    print("            -    EN EL  "+str(float(((count_created_date_2019_alienvault_iot_pattern_urlvalue*100)/count_alienvault_iot_pattern_urlvalue)))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2019")
    print("            -    EN EL  "+str(float(((count_created_date_2018_alienvault_iot_pattern_urlvalue*100)/count_alienvault_iot_pattern_urlvalue)))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2018 O ANTERIOR ")
    print("\n")
if(count_alienvault_iot_pattern_filehashes>0):
    print("      -    EN EL  "+str(float(((count_alienvault_iot_pattern_filehashes*100)/count_alienvault_iot_totalpulses)))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT EL PATRÓN ES UN HASH DE UN ARCHIVO. LOS PORCENTAJES DE FECHA DE CREACION SON LOS SIGUIENTES:  \n")
    print("\n")
    print("            -    EN EL  "+str(float(((count_created_date_2023_alienvault_iot_pattern_filehashes*100)/count_alienvault_iot_pattern_filehashes)))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2023 ")
    print("            -    EN EL  "+str(float(((count_created_date_2022_alienvault_iot_pattern_filehashes*100)/count_alienvault_iot_pattern_filehashes)))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2022")
    print("            -    EN EL  "+str(float(((count_created_date_2021_alienvault_iot_pattern_filehashes*100)/count_alienvault_iot_pattern_filehashes)))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2021 ")
    print("            -    EN EL  "+str(float(((count_created_date_2020_alienvault_iot_pattern_filehashes*100)/count_alienvault_iot_pattern_filehashes)))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2020 ")
    print("            -    EN EL  "+str(float(((count_created_date_2019_alienvault_iot_pattern_filehashes*100)/count_alienvault_iot_pattern_filehashes)))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2019")
    print("            -    EN EL  "+str(float(((count_created_date_2018_alienvault_iot_pattern_filehashes*100)/count_alienvault_iot_pattern_filehashes)))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2018 O ANTERIOR ")
    print("\n")
if(count_alienvault_iot_pattern_emailmessage>0):
    print("      -    EN EL  "+str(float(((count_alienvault_iot_pattern_emailmessage*100)/count_alienvault_iot_totalpulses)))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT EL PATRÓN ES MENSAJE DE EMAIL. LOS PORCENTAJES DE FECHA DE CREACION SON LOS SIGUIENTES:  \n")
    print("\n")
    print("            -    EN EL  "+str(float(((count_created_date_2023_alienvault_iot_pattern_emailmessage*100)/count_alienvault_iot_pattern_emailmessage)))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2023 ")
    print("            -    EN EL  "+str(float(((count_created_date_2022_alienvault_iot_pattern_emailmessage*100)/count_alienvault_iot_pattern_emailmessage)))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2022")
    print("            -    EN EL  "+str(float(((count_created_date_2021_alienvault_iot_pattern_emailmessage*100)/count_alienvault_iot_pattern_emailmessage)))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2021 ")
    print("            -    EN EL  "+str(float(((count_created_date_2020_alienvault_iot_pattern_emailmessage*100)/count_alienvault_iot_pattern_emailmessage)))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2020 ")
    print("            -    EN EL  "+str(float(((count_created_date_2019_alienvault_iot_pattern_emailmessage*100)/count_alienvault_iot_pattern_emailmessage)))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2019")
    print("            -    EN EL  "+str(float(((count_created_date_2018_alienvault_iot_pattern_emailmessage*100)/count_alienvault_iot_pattern_emailmessage)))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2018 O ANTERIOR ")
    print("\n")
if(count_alienvault_iot_pattern_ipv4addr>0):
    print("      -    EN EL  "+str(float(((count_alienvault_iot_pattern_ipv4addr*100)/count_alienvault_iot_totalpulses)))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT EL PATRÓN ES UNA DIRECCIÓN IPV4. LOS PORCENTAJES DE FECHA DE CREACION SON LOS SIGUIENTES:  \n")
    print("\n")
    print("            -    EN EL  "+str(float(((count_created_date_2023_alienvault_iot_pattern_ipv4addr*100)/count_alienvault_iot_pattern_ipv4addr)))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2023 ")
    print("            -    EN EL  "+str(float(((count_created_date_2022_alienvault_iot_pattern_ipv4addr*100)/count_alienvault_iot_pattern_ipv4addr)))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2022")
    print("            -    EN EL  "+str(float(((count_created_date_2021_alienvault_iot_pattern_ipv4addr*100)/count_alienvault_iot_pattern_ipv4addr)))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2021 ")
    print("            -    EN EL  "+str(float(((count_created_date_2020_alienvault_iot_pattern_ipv4addr*100)/count_alienvault_iot_pattern_ipv4addr)))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2020 ")
    print("            -    EN EL  "+str(float(((count_created_date_2019_alienvault_iot_pattern_ipv4addr*100)/count_alienvault_iot_pattern_ipv4addr)))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2019")
    print("            -    EN EL  "+str(float(((count_created_date_2018_alienvault_iot_pattern_ipv4addr*100)/count_alienvault_iot_pattern_ipv4addr)))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2018 O ANTERIOR ")
    print("\n")

    
    
    
    
    
    
    
    
    
    
    
    

#Abro los ficheros con los que voy a tratar


df_alienvault_sh = pd.read_excel('alienvault_smart_home_2023.xlsx')



#Variables donde almacenare el contador de valores de patron segun el anio de creacion
count_created_date_2023_alienvault_sh_pattern_domainname=0
count_created_date_2023_alienvault_sh_pattern_urlvalue=0
count_created_date_2023_alienvault_sh_pattern_filehashes=0
count_created_date_2023_alienvault_sh_pattern_emailmessage=0
count_created_date_2023_alienvault_sh_pattern_ipv4addr=0
#Variables donde almacenare el contador de OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT creados en un anio especifico
count_created_date_2023_alienvault_sh=0

count_created_date_2022_alienvault_sh_pattern_domainname=0
count_created_date_2022_alienvault_sh_pattern_urlvalue=0
count_created_date_2022_alienvault_sh_pattern_filehashes=0
count_created_date_2022_alienvault_sh_pattern_emailmessage=0
count_created_date_2022_alienvault_sh_pattern_ipv4addr=0
count_created_date_2022_alienvault_sh=0


count_created_date_2021_alienvault_sh_pattern_domainname=0
count_created_date_2021_alienvault_sh_pattern_urlvalue=0
count_created_date_2021_alienvault_sh_pattern_filehashes=0
count_created_date_2021_alienvault_sh_pattern_emailmessage=0
count_created_date_2021_alienvault_sh_pattern_ipv4addr=0
count_created_date_2021_alienvault_sh=0


count_created_date_2020_alienvault_sh_pattern_domainname=0
count_created_date_2020_alienvault_sh_pattern_urlvalue=0
count_created_date_2020_alienvault_sh_pattern_filehashes=0
count_created_date_2020_alienvault_sh_pattern_emailmessage=0
count_created_date_2020_alienvault_sh_pattern_ipv4addr=0
count_created_date_2020_alienvault_sh=0


count_created_date_2019_alienvault_sh_pattern_domainname=0
count_created_date_2019_alienvault_sh_pattern_urlvalue=0
count_created_date_2019_alienvault_sh_pattern_filehashes=0
count_created_date_2019_alienvault_sh_pattern_emailmessage=0
count_created_date_2019_alienvault_sh_pattern_ipv4addr=0
count_created_date_2019_alienvault_sh=0


count_created_date_2018_alienvault_sh_pattern_domainname=0
count_created_date_2018_alienvault_sh_pattern_urlvalue=0
count_created_date_2018_alienvault_sh_pattern_filehashes=0
count_created_date_2018_alienvault_sh_pattern_emailmessage=0
count_created_date_2018_alienvault_sh_pattern_ipv4addr=0
count_created_date_2018_alienvault_sh=0

count_alienvault_sh_pattern_domainname=0
count_alienvault_sh_pattern_urlvalue=0
count_alienvault_sh_pattern_filehashes=0
count_alienvault_sh_pattern_emailmessage=0
count_alienvault_sh_pattern_ipv4addr=0

count_alienvault_sh_total=0
count_alienvault_sh_totalpulses=0


#Comprobamos el anio de CREACION 
for r in range(0,len(df_alienvault_sh["created"])):
    if('[' in df_alienvault_sh["created"][r]):
        #Obtengo los distintos valores de fecha de creacion y patron para la fila actual
        aux=df_alienvault_sh["created"][r].split(",")
        auxx=df_alienvault_sh["pattern"][r].split(",")
        for l in range(0,len(aux)):
            if(len(aux)>0):
                #Compruebo que coincida el numero de valores
                if(len(aux)==len(auxx)):
                    #Obtengo el valor de fecha de creacion
                    aux_str=aux[l].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
                    if(aux_str!='NONE'):
                        count_alienvault_sh_total+=1
                        str_anio_createdate_alienvault_sh=aux_str.split("-")
                        #Obtengo el valor de fecha de creacion
                        anio_createdate_alienvault_sh=int(str_anio_createdate_alienvault_sh[0])
                        #Compruebo el valor de fecha de creacion
                        if(anio_createdate_alienvault_sh >= 2023):
                            count_created_date_2023_alienvault_sh+=1
                            auxx_str=auxx[l].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
                            if(auxx_str!='NONE'):
                                #Compruebo el valor de patron
                                if('domain-name' in auxx_str):
                                    count_alienvault_sh_totalpulses+=1
                                    count_alienvault_sh_pattern_domainname+=1
                                    count_created_date_2023_alienvault_sh_pattern_domainname+=1
                                elif('url:value' in auxx_str):
                                    count_alienvault_sh_totalpulses+=1
                                    count_alienvault_sh_pattern_urlvalue+=1
                                    count_created_date_2023_alienvault_sh_pattern_urlvalue+=1
                                elif('file:hashes' in auxx_str):
                                    count_alienvault_sh_totalpulses+=1
                                    count_alienvault_sh_pattern_filehashes+=1
                                    count_created_date_2023_alienvault_sh_pattern_filehashes+=1 
                                elif('email-message' in auxx_str):
                                    count_alienvault_sh_totalpulses+=1
                                    count_alienvault_sh_pattern_emailmessage+=1
                                    count_created_date_2023_alienvault_sh_pattern_emailmessage+=1
                                elif('ipv4-addr' in auxx_str):
                                    count_alienvault_sh_totalpulses+=1
                                    count_alienvault_sh_pattern_ipv4addr+=1
                                    count_created_date_2023_alienvault_sh_pattern_ipv4addr+=1


                        elif(anio_createdate_alienvault_sh >= 2022):
                            count_created_date_2022_alienvault_sh+=1
                            auxx_str=auxx[l].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
                            if(auxx_str!='NONE'):
                                if('domain-name' in auxx_str):
                                    count_alienvault_sh_totalpulses+=1
                                    count_alienvault_sh_pattern_domainname+=1
                                    count_created_date_2022_alienvault_sh_pattern_domainname+=1
                                elif('url:value' in auxx_str):
                                    count_alienvault_sh_totalpulses+=1
                                    count_alienvault_sh_pattern_urlvalue+=1
                                    count_created_date_2022_alienvault_sh_pattern_urlvalue+=1
                                elif('file:hashes' in auxx_str):
                                    count_alienvault_sh_totalpulses+=1
                                    count_alienvault_sh_pattern_filehashes+=1
                                    count_created_date_2022_alienvault_sh_pattern_filehashes+=1 
                                elif('email-message' in auxx_str):
                                    count_alienvault_sh_totalpulses+=1
                                    count_alienvault_sh_pattern_emailmessage+=1
                                    count_created_date_2022_alienvault_sh_pattern_emailmessage+=1
                                elif('ipv4-addr' in auxx_str):
                                    count_alienvault_sh_totalpulses+=1
                                    count_alienvault_sh_pattern_ipv4addr+=1
                                    count_created_date_2022_alienvault_sh_pattern_ipv4addr+=1

                        elif(anio_createdate_alienvault_sh >= 2021):
                            count_created_date_2021_alienvault_sh+=1
                            auxx_str=auxx[l].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
                            if(auxx_str!='NONE'):
                                if('domain-name' in auxx_str):
                                    count_alienvault_sh_totalpulses+=1
                                    count_alienvault_sh_pattern_domainname+=1
                                    count_created_date_2021_alienvault_sh_pattern_domainname+=1
                                elif('url:value' in auxx_str):
                                    count_alienvault_sh_totalpulses+=1
                                    count_alienvault_sh_pattern_urlvalue+=1
                                    count_created_date_2021_alienvault_sh_pattern_urlvalue+=1
                                elif('file:hashes' in auxx_str):
                                    count_alienvault_sh_totalpulses+=1
                                    count_alienvault_sh_pattern_filehashes+=1
                                    count_created_date_2021_alienvault_sh_pattern_filehashes+=1
                                elif('email-message' in auxx_str):
                                    count_alienvault_sh_totalpulses+=1
                                    count_alienvault_sh_pattern_emailmessage+=1
                                    count_created_date_2021_alienvault_sh_pattern_emailmessage+=1
                                elif('ipv4-addr' in auxx_str):
                                    count_alienvault_sh_totalpulses+=1
                                    count_alienvault_sh_pattern_ipv4addr+=1
                                    count_created_date_2021_alienvault_sh_pattern_ipv4addr+=1

                        elif(anio_createdate_alienvault_sh >= 2020):
                            count_created_date_2020_alienvault_sh+=1
                            auxx_str=auxx[l].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
                            if(auxx_str!='NONE'):
                                if('domain-name' in auxx_str):
                                    count_alienvault_sh_totalpulses+=1
                                    count_alienvault_sh_pattern_domainname+=1
                                    count_created_date_2020_alienvault_sh_pattern_domainname+=1
                                elif('url:value' in auxx_str):
                                    count_alienvault_sh_totalpulses+=1
                                    count_alienvault_sh_pattern_urlvalue+=1
                                    count_created_date_2020_alienvault_sh_pattern_urlvalue+=1
                                elif('file:hashes' in auxx_str):
                                    count_alienvault_sh_totalpulses+=1
                                    count_alienvault_sh_pattern_filehashes+=1
                                    count_created_date_2020_alienvault_sh_pattern_filehashes+=1 
                                elif('email-message' in auxx_str):
                                    count_alienvault_sh_totalpulses+=1
                                    count_alienvault_sh_pattern_emailmessage+=1
                                    count_created_date_2020_alienvault_sh_pattern_emailmessage+=1
                                elif('ipv4-addr' in auxx_str):
                                    count_alienvault_sh_totalpulses+=1
                                    count_alienvault_sh_pattern_ipv4addr+=1
                                    count_created_date_2020_alienvault_sh_pattern_ipv4addr+=1


                        elif(anio_createdate_alienvault_sh >= 2019):
                            count_created_date_2019_alienvault_sh+=1
                            auxx_str=auxx[l].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
                            if(auxx_str!='NONE'):
                                if('domain-name' in auxx_str):
                                    count_alienvault_sh_totalpulses+=1
                                    count_alienvault_sh_pattern_domainname+=1
                                    count_created_date_2019_alienvault_sh_pattern_domainname+=1
                                elif('url:value' in auxx_str):
                                    count_alienvault_sh_totalpulses+=1
                                    count_alienvault_sh_pattern_urlvalue+=1
                                    count_created_date_2019_alienvault_sh_pattern_urlvalue+=1
                                elif('file:hashes' in auxx_str):
                                    count_alienvault_sh_totalpulses+=1
                                    count_alienvault_sh_pattern_filehashes+=1
                                    count_created_date_2019_alienvault_sh_pattern_filehashes+=1
                                elif('email-message' in auxx_str):
                                    count_alienvault_sh_totalpulses+=1
                                    count_alienvault_sh_pattern_emailmessage+=1
                                    count_created_date_2019_alienvault_sh_pattern_emailmessage+=1
                                elif('ipv4-addr' in auxx_str):
                                    count_alienvault_sh_totalpulses+=1
                                    count_alienvault_sh_pattern_ipv4addr+=1
                                    count_created_date_2019_alienvault_sh_pattern_ipv4addr+=1


                        else: 
                            count_created_date_2018_alienvault_sh+=1
                            auxx_str=auxx[l].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
                            if(auxx_str!='NONE'):
                                if('domain-name' in auxx_str):
                                    count_alienvault_sh_totalpulses+=1
                                    count_alienvault_sh_pattern_domainname+=1
                                    count_created_date_2018_alienvault_sh_pattern_domainname+=1
                                elif('url:value' in auxx_str):
                                    count_alienvault_sh_totalpulses+=1
                                    count_alienvault_sh_pattern_urlvalue+=1
                                    count_created_date_2018_alienvault_sh_pattern_urlvalue+=1
                                elif('file:hashes' in auxx_str):
                                    count_alienvault_sh_totalpulses+=1
                                    count_alienvault_sh_pattern_filehashes+=1
                                    count_created_date_2018_alienvault_sh_pattern_filehashes+=1
                                elif('email-message' in auxx_str):
                                    count_alienvault_sh_totalpulses+=1
                                    count_alienvault_sh_pattern_emailmessage+=1
                                    count_created_date_2018_alienvault_sh_pattern_emailmessage+=1
                                elif('ipv4-addr' in auxx_str):
                                    count_alienvault_sh_totalpulses+=1
                                    count_alienvault_sh_pattern_ipv4addr+=1
                                    count_created_date_2018_alienvault_sh_pattern_ipv4addr+=1
    else:
        #Si existe un unico valor de fecha de creacion para la fila actual, obtengo el anio de creacion
        str_anio_createdate_alienvault_sh=df_alienvault_sh["created"][r].split("-")
        anio_createdate_alienvault_sh=int(str_anio_createdate_alienvault_sh[0])
        count_alienvault_sh_total+=1
        #Obtengo los valores de patron para la fila actual
        auxx=df_alienvault_sh["pattern"][r].split(",")
        
        for l in range(0,len(auxx)):
            if(len(auxx)>0):
                auxx_str=auxx[l].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
                if(auxx_str!='NONE'):
                    count_alienvault_sh_totalpulses+=1
                    #Compruebo el anio de creacion
                    if(anio_createdate_alienvault_sh >= 2023):
                        count_created_date_2023_alienvault_sh+=1
                        #Compruebo el valor de patron
                        if('domain-name' in auxx_str):
                            count_alienvault_sh_pattern_domainname+=1
                            count_created_date_2023_alienvault_sh_pattern_domainname+=1  
                        elif('url:value' in auxx_str):
                            count_alienvault_sh_pattern_urlvalue+=1
                            count_created_date_2023_alienvault_sh_pattern_urlvalue+=1  
                        elif('file:hashes' in auxx_str):
                            count_alienvault_sh_pattern_filehashes+=1
                            count_created_date_2023_alienvault_sh_pattern_filehashes+=1
                        elif('email-message' in auxx_str):
                            count_alienvault_sh_pattern_emailmessage+=1
                            count_created_date_2023_alienvault_sh_pattern_emailmessage+=1
                        elif('ipv4-addr' in auxx_str):
                            count_alienvault_sh_pattern_ipv4addr+=1
                            count_created_date_2023_alienvault_sh_pattern_ipv4addr+=1

                    elif(anio_createdate_alienvault_sh >= 2022):
                        count_created_date_2022_alienvault_sh+=1
                        if('domain-name' in auxx_str):
                            count_alienvault_sh_pattern_domainname+=1
                            count_created_date_2022_alienvault_sh_pattern_domainname+=1  
                        elif('url:value' in auxx_str):
                            count_alienvault_sh_pattern_urlvalue+=1
                            count_created_date_2022_alienvault_sh_pattern_urlvalue+=1  
                        elif('file:hashes' in auxx_str):
                            count_alienvault_sh_pattern_filehashes+=1
                            count_created_date_2022_alienvault_sh_pattern_filehashes+=1
                        elif('email-message' in auxx_str):
                            count_alienvault_sh_pattern_emailmessage+=1
                            count_created_date_2022_alienvault_sh_pattern_emailmessage+=1
                        elif('ipv4-addr' in auxx_str):
                            count_alienvault_sh_pattern_ipv4addr+=1
                            count_created_date_2022_alienvault_sh_pattern_ipv4addr+=1
                    elif(anio_createdate_alienvault_sh >= 2021):
                        count_created_date_2021_alienvault_sh+=1
                        if('domain-name' in auxx_str):
                            count_alienvault_sh_pattern_domainname+=1
                            count_created_date_2021_alienvault_sh_pattern_domainname+=1  
                        elif('url:value' in auxx_str):
                            count_alienvault_sh_pattern_urlvalue+=1
                            count_created_date_2021_alienvault_sh_pattern_urlvalue+=1  
                        elif('file:hashes' in auxx_str):
                            count_alienvault_sh_pattern_filehashes+=1
                            count_created_date_2021_alienvault_sh_pattern_filehashes+=1
                        elif('email-message' in auxx_str):
                            count_alienvault_sh_pattern_emailmessage+=1
                            count_created_date_2021_alienvault_sh_pattern_emailmessage+=1
                        elif('ipv4-addr' in auxx_str):
                            count_alienvault_sh_pattern_ipv4addr+=1
                            count_created_date_2021_alienvault_sh_pattern_ipv4addr+=1
                    elif(anio_createdate_alienvault_sh >= 2020):
                        count_created_date_2020_alienvault_sh+=1
                        if('domain-name' in auxx_str):
                            count_alienvault_sh_pattern_domainname+=1
                            count_created_date_2020_alienvault_sh_pattern_domainname+=1  
                        elif('url:value' in auxx_str):
                            count_alienvault_sh_pattern_urlvalue+=1
                            count_created_date_2020_alienvault_sh_pattern_urlvalue+=1  
                        elif('file:hashes' in auxx_str):
                            count_alienvault_sh_pattern_filehashes+=1
                            count_created_date_2020_alienvault_sh_pattern_filehashes+=1
                        elif('email-message' in auxx_str):
                            count_alienvault_sh_pattern_emailmessage+=1
                            count_created_date_2020_alienvault_sh_pattern_emailmessage+=1
                        elif('ipv4-addr' in auxx_str):
                            count_alienvault_sh_pattern_ipv4addr+=1
                            count_created_date_2020_alienvault_sh_pattern_ipv4addr+=1
                    elif(anio_createdate_alienvault_sh >= 2019):
                        count_created_date_2019_alienvault_sh+=1
                        if('domain-name' in auxx_str):
                            count_alienvault_sh_pattern_domainname+=1
                            count_created_date_2019_alienvault_sh_pattern_domainname+=1  
                        elif('url:value' in auxx_str):
                            count_alienvault_sh_pattern_urlvalue+=1
                            count_created_date_2019_alienvault_sh_pattern_urlvalue+=1  
                        elif('file:hashes' in auxx_str):
                            count_alienvault_sh_pattern_filehashes+=1
                            count_created_date_2019_alienvault_sh_pattern_filehashes+=1
                        elif('email-message' in auxx_str):
                            count_alienvault_sh_pattern_emailmessage+=1
                            count_created_date_2019_alienvault_sh_pattern_emailmessage+=1
                        elif('ipv4-addr' in auxx_str):
                            count_alienvault_sh_pattern_ipv4addr+=1
                            count_created_date_2019_alienvault_sh_pattern_ipv4addr+=1
                    else:
                        count_created_date_2018_alienvault_sh+=1
                        if('domain-name' in auxx_str):
                            count_alienvault_sh_pattern_domainname+=1
                            count_created_date_2018_alienvault_sh_pattern_domainname+=1  
                        elif('url:value' in auxx_str):
                            count_alienvault_sh_pattern_urlvalue+=1
                            count_created_date_2018_alienvault_sh_pattern_urlvalue+=1  
                        elif('file:hashes' in auxx_str):
                            count_alienvault_sh_pattern_filehashes+=1
                            count_created_date_2018_alienvault_sh_pattern_filehashes+=1
                        elif('email-message' in auxx_str):
                            count_alienvault_sh_pattern_emailmessage+=1
                            count_created_date_2018_alienvault_sh_pattern_emailmessage+=1
                        elif('ipv4-addr' in auxx_str):
                            count_alienvault_sh_pattern_ipv4addr+=1
                            count_created_date_2018_alienvault_sh_pattern_ipv4addr+=1
                
                
print("******************ESTADÍSTICAS TIPO DE PATRÓN/FECHA DE CREACIÓN OBJETOS TIPO INDICADOR ALIENVAULT PARTE SMART HOME******************")
print("\n")                            
                
print("\n")
print(" DE UN TOTAL DE "+str(count_alienvault_sh_totalpulses)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT :\n") 
print("\n")
print("   - LAS ESTADISTICAS DE FECHA DE CREACION SON LAS SIGUIENTES:  \n")
print("      -    EN  "+str(count_created_date_2023_alienvault_sh)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2023. LAS ESTADÍSTICAS DE PATRÓN SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(count_created_date_2023_alienvault_sh_pattern_domainname)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT CREADOS EN 2023, EL PATRÓN ES NOMBRE DE DOMINIO ")
print("            -    EN  "+str(count_created_date_2023_alienvault_sh_pattern_urlvalue)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT CREADOS EN 2023, EL PATRÓN ES VALOR DE URL")
print("            -    EN  "+str(count_created_date_2023_alienvault_sh_pattern_filehashes)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT CREADOS EN 2023, EL PATRÓN ES UN HASH DE UN ARCHIVO ")
print("            -    EN  "+str(count_created_date_2023_alienvault_sh_pattern_filehashes)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT CREADOS EN 2023, EL PATRÓN ES MENSAJE DE EMAIL ")
print("            -    EN  "+str(count_created_date_2023_alienvault_sh_pattern_ipv4addr)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT CREADOS EN 2023, EL PATRÓN ES UNA DIRECCIÓN IPV4 ")
print("\n")
print("      -    EN  "+str(count_created_date_2022_alienvault_sh)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2022. LAS ESTADÍSTICAS DE PATRÓN SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(count_created_date_2022_alienvault_sh_pattern_domainname)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT CREADOS EN 2022, EL PATRÓN ES NOMBRE DE DOMINIO ")
print("            -    EN  "+str(count_created_date_2022_alienvault_sh_pattern_urlvalue)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT CREADOS EN 2022, EL PATRÓN ES VALOR DE URL")
print("            -    EN  "+str(count_created_date_2022_alienvault_sh_pattern_filehashes)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT CREADOS EN 2022, EL PATRÓN ES UN HASH DE UN ARCHIVO ")
print("            -    EN  "+str(count_created_date_2022_alienvault_sh_pattern_filehashes)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT CREADOS EN 2022, EL PATRÓN ES MENSAJE DE EMAIL ")
print("            -    EN  "+str(count_created_date_2022_alienvault_sh_pattern_ipv4addr)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT CREADOS EN 2022, EL PATRÓN ES UNA DIRECCIÓN IPV4 ")
print("\n")
print("      -    EN  "+str(count_created_date_2021_alienvault_sh)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2021. LAS ESTADÍSTICAS DE PATRÓN SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(count_created_date_2021_alienvault_sh_pattern_domainname)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT CREADOS EN 2021, EL PATRÓN ES NOMBRE DE DOMINIO ")
print("            -    EN  "+str(count_created_date_2021_alienvault_sh_pattern_urlvalue)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT CREADOS EN 2021, EL PATRÓN ES VALOR DE URL")
print("            -    EN  "+str(count_created_date_2021_alienvault_sh_pattern_filehashes)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT CREADOS EN 2021, EL PATRÓN ES UN HASH DE UN ARCHIVO ")
print("            -    EN  "+str(count_created_date_2021_alienvault_sh_pattern_filehashes)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT CREADOS EN 2021, EL PATRÓN ES MENSAJE DE EMAIL ")
print("            -    EN  "+str(count_created_date_2021_alienvault_sh_pattern_ipv4addr)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT CREADOS EN 2021, EL PATRÓN ES UNA DIRECCIÓN IPV4 ")
print("\n")
print("      -    EN  "+str(count_created_date_2020_alienvault_sh)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2020. LAS ESTADÍSTICAS DE PATRÓN SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(count_created_date_2020_alienvault_sh_pattern_domainname)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT CREADOS EN 2020, EL PATRÓN ES NOMBRE DE DOMINIO ")
print("            -    EN  "+str(count_created_date_2020_alienvault_sh_pattern_urlvalue)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT CREADOS EN 2020, EL PATRÓN ES VALOR DE URL")
print("            -    EN  "+str(count_created_date_2020_alienvault_sh_pattern_filehashes)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT CREADOS EN 2020, EL PATRÓN ES UN HASH DE UN ARCHIVO ")
print("            -    EN  "+str(count_created_date_2020_alienvault_sh_pattern_filehashes)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT CREADOS EN 2020, EL PATRÓN ES MENSAJE DE EMAIL ")
print("            -    EN  "+str(count_created_date_2020_alienvault_sh_pattern_ipv4addr)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT CREADOS EN 2020, EL PATRÓN ES UNA DIRECCIÓN IPV4 ")
print("\n")
print("      -    EN  "+str(count_created_date_2019_alienvault_sh)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2019. LAS ESTADÍSTICAS DE PATRÓN SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(count_created_date_2019_alienvault_sh_pattern_domainname)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT CREADOS EN 2019, EL PATRÓN ES NOMBRE DE DOMINIO ")
print("            -    EN  "+str(count_created_date_2019_alienvault_sh_pattern_urlvalue)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT CREADOS EN 2019, EL PATRÓN ES VALOR DE URL")
print("            -    EN  "+str(count_created_date_2019_alienvault_sh_pattern_filehashes)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT CREADOS EN 2019, EL PATRÓN ES UN HASH DE UN ARCHIVO ")
print("            -    EN  "+str(count_created_date_2019_alienvault_sh_pattern_filehashes)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT CREADOS EN 2019, EL PATRÓN ES MENSAJE DE EMAIL ")
print("            -    EN  "+str(count_created_date_2019_alienvault_sh_pattern_ipv4addr)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT CREADOS EN 2019, EL PATRÓN ES UNA DIRECCIÓN IPV4 ")
print("\n")
print("      -    EN  "+str(count_created_date_2018_alienvault_sh)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2018 O ANTERIOR. LAS ESTADÍSTICAS DE PATRÓN SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(count_created_date_2018_alienvault_sh_pattern_domainname)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT CREADOS EN 2018 O ANTES, EL PATRÓN ES NOMBRE DE DOMINIO ")
print("            -    EN  "+str(count_created_date_2018_alienvault_sh_pattern_urlvalue)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT CREADOS EN 2018 O ANTES, EL PATRÓN ES VALOR DE URL")
print("            -    EN  "+str(count_created_date_2018_alienvault_sh_pattern_filehashes)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT CREADOS EN 2018 O ANTES, EL PATRÓN ES UN HASH DE UN ARCHIVO ")
print("            -    EN  "+str(count_created_date_2018_alienvault_sh_pattern_filehashes)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT CREADOS EN 2018, EL PATRÓN ES MENSAJE DE EMAIL ")
print("            -    EN  "+str(count_created_date_2018_alienvault_sh_pattern_ipv4addr)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT CREADOS EN 2018, EL PATRÓN ES UNA DIRECCIÓN IPV4 ")
print("\n")
print("   - LAS ESTADISTICAS DE PATRON SON LAS SIGUIENTES:  \n")
print("      -    EN  "+str(count_alienvault_sh_pattern_domainname)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT EL PATRÓN ES NOMBRE DE DOMINIO. LAS ESTADÍSTICAS DE FECHA DE CREACION SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(count_created_date_2023_alienvault_sh_pattern_domainname)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2023 ")
print("            -    EN  "+str(count_created_date_2022_alienvault_sh_pattern_domainname)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2022")
print("            -    EN  "+str(count_created_date_2021_alienvault_sh_pattern_domainname)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2021 ")
print("            -    EN  "+str(count_created_date_2020_alienvault_sh_pattern_domainname)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2020 ")
print("            -    EN  "+str(count_created_date_2019_alienvault_sh_pattern_domainname)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2019")
print("            -    EN  "+str(count_created_date_2018_alienvault_sh_pattern_domainname)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2018 O ANTERIOR ")
print("\n")
print("      -    EN  "+str(count_alienvault_sh_pattern_urlvalue)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT EL PATRÓN ES VALOR DE URL. LAS ESTADÍSTICAS DE FECHA DE CREACION SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(count_created_date_2023_alienvault_sh_pattern_urlvalue)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2023 ")
print("            -    EN  "+str(count_created_date_2022_alienvault_sh_pattern_urlvalue)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2022")
print("            -    EN  "+str(count_created_date_2021_alienvault_sh_pattern_urlvalue)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2021 ")
print("            -    EN  "+str(count_created_date_2020_alienvault_sh_pattern_urlvalue)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2020 ")
print("            -    EN  "+str(count_created_date_2019_alienvault_sh_pattern_urlvalue)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2019")
print("            -    EN  "+str(count_created_date_2018_alienvault_sh_pattern_urlvalue)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2018 O ANTERIOR ")
print("\n")
print("      -    EN  "+str(count_alienvault_sh_pattern_filehashes)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT EL PATRÓN ES UN HASH DE UN ARCHIVO. LAS ESTADÍSTICAS DE FECHA DE CREACION SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(count_created_date_2023_alienvault_sh_pattern_filehashes)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2023 ")
print("            -    EN  "+str(count_created_date_2022_alienvault_sh_pattern_filehashes)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2022")
print("            -    EN  "+str(count_created_date_2021_alienvault_sh_pattern_filehashes)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2021 ")
print("            -    EN  "+str(count_created_date_2020_alienvault_sh_pattern_filehashes)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2020 ")
print("            -    EN  "+str(count_created_date_2019_alienvault_sh_pattern_filehashes)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2019")
print("            -    EN  "+str(count_created_date_2018_alienvault_sh_pattern_filehashes)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2018 O ANTERIOR ")
print("\n")
print("      -    EN  "+str(count_alienvault_sh_pattern_emailmessage)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT EL PATRÓN ES MENSAJE DE EMAIL. LAS ESTADÍSTICAS DE FECHA DE CREACION SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(count_created_date_2023_alienvault_sh_pattern_emailmessage)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2023 ")
print("            -    EN  "+str(count_created_date_2022_alienvault_sh_pattern_emailmessage)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2022")
print("            -    EN  "+str(count_created_date_2021_alienvault_sh_pattern_emailmessage)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2021 ")
print("            -    EN  "+str(count_created_date_2020_alienvault_sh_pattern_emailmessage)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2020 ")
print("            -    EN  "+str(count_created_date_2019_alienvault_sh_pattern_emailmessage)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2019")
print("            -    EN  "+str(count_created_date_2018_alienvault_sh_pattern_emailmessage)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2018 O ANTERIOR ")
print("\n")
print("      -    EN  "+str(count_alienvault_sh_pattern_ipv4addr)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT EL PATRÓN ES UNA DIRECCIÓN IPV4. LAS ESTADÍSTICAS DE FECHA DE CREACION SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(count_created_date_2023_alienvault_sh_pattern_ipv4addr)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2023 ")
print("            -    EN  "+str(count_created_date_2022_alienvault_sh_pattern_ipv4addr)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2022")
print("            -    EN  "+str(count_created_date_2021_alienvault_sh_pattern_ipv4addr)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2021 ")
print("            -    EN  "+str(count_created_date_2020_alienvault_sh_pattern_ipv4addr)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2020 ")
print("            -    EN  "+str(count_created_date_2019_alienvault_sh_pattern_ipv4addr)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2019")
print("            -    EN  "+str(count_created_date_2018_alienvault_sh_pattern_ipv4addr)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2018 O ANTERIOR ")
print("\n")








print("******************PORCENTAJE TIPO DE PATRÓN/FECHA DE CREACIÓN OBJETOS TIPO INDICADOR ALIENVAULT PARTE SMART HOME******************")
print("\n")                            
                
print("\n")
print(" DE UN TOTAL DE "+str(count_alienvault_sh_totalpulses)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT :\n") 
print("\n")
print("   - LOS PORCENTAJES DE FECHA DE CREACION SON LOS SIGUIENTES:  \n")
if(count_created_date_2023_alienvault_sh>0):
    print("      -    EN EL  "+str(float(((count_created_date_2023_alienvault_sh*100)/count_alienvault_sh_totalpulses)))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2023. LOS PORCENTAJES DE PATRÓN SON LOS SIGUIENTES:  \n")
    print("\n")
    print("            -    EN EL  "+str(float(((count_created_date_2023_alienvault_sh_pattern_domainname*100)/count_created_date_2023_alienvault_sh)))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT CREADOS EN 2023, EL PATRÓN ES NOMBRE DE DOMINIO ")
    print("            -    EN EL  "+str(float(((count_created_date_2023_alienvault_sh_pattern_urlvalue*100)/count_created_date_2023_alienvault_sh)))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT CREADOS EN 2023, EL PATRÓN ES VALOR DE URL")
    print("            -    EN EL  "+str(float(((count_created_date_2023_alienvault_sh_pattern_filehashes*100)/count_created_date_2023_alienvault_sh)))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT CREADOS EN 2023, EL PATRÓN ES UN HASH DE UN ARCHIVO ")
    print("            -    EN EL  "+str(float(((count_created_date_2023_alienvault_sh_pattern_emailmessage*100)/count_created_date_2023_alienvault_sh)))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT CREADOS EN 2023, EL PATRÓN ES MENSAJE DE EMAIL ")
    print("            -    EN EL  "+str(float(((count_created_date_2023_alienvault_sh_pattern_ipv4addr*100)/count_created_date_2023_alienvault_sh)))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT CREADOS EN 2023, EL PATRÓN ES UNA DIRECCIÓN IPV4 ")
    print("\n")
if(count_created_date_2022_alienvault_sh>0):
    print("      -    EN EL  "+str(float(((count_created_date_2022_alienvault_sh*100)/count_alienvault_sh_totalpulses)))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2022. LOS PORCENTAJESS DE PATRÓN SON LAS SIGUIENTES:  \n")
    print("\n")
    print("            -    EN EL  "+str(float(((count_created_date_2022_alienvault_sh_pattern_domainname*100)/count_created_date_2022_alienvault_sh)))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT CREADOS EN 2022, EL PATRÓN ES NOMBRE DE DOMINIO ")
    print("            -    EN EL  "+str(float(((count_created_date_2022_alienvault_sh_pattern_urlvalue*100)/count_created_date_2022_alienvault_sh)))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT CREADOS EN 2022, EL PATRÓN ES VALOR DE URL")
    print("            -    EN EL  "+str(float(((count_created_date_2022_alienvault_sh_pattern_filehashes*100)/count_created_date_2022_alienvault_sh)))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT CREADOS EN 2022, EL PATRÓN ES UN HASH DE UN ARCHIVO ")
    print("            -    EN EL  "+str(float(((count_created_date_2022_alienvault_sh_pattern_emailmessage*100)/count_created_date_2022_alienvault_sh)))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT CREADOS EN 2022, EL PATRÓN ES MENSAJE DE EMAIL ")
    print("            -    EN EL  "+str(float(((count_created_date_2022_alienvault_sh_pattern_ipv4addr*100)/count_created_date_2022_alienvault_sh)))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT CREADOS EN 2022, EL PATRÓN ES UNA DIRECCIÓN IPV4 ")
    print("\n")
if(count_created_date_2021_alienvault_sh>0):
    print("      -    EN EL  "+str(float(((count_created_date_2021_alienvault_sh*100)/count_alienvault_sh_totalpulses)))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2021. LOS PORCENTAJES DE PATRÓN SON LOS SIGUIENTES:  \n")
    print("\n")
    print("            -    EN EL  "+str(float(((count_created_date_2021_alienvault_sh_pattern_domainname*100)/count_created_date_2021_alienvault_sh)))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT CREADOS EN 2021, EL PATRÓN ES NOMBRE DE DOMINIO ")
    print("            -    EN EL  "+str(float(((count_created_date_2021_alienvault_sh_pattern_urlvalue*100)/count_created_date_2021_alienvault_sh)))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT CREADOS EN 2021, EL PATRÓN ES VALOR DE URL")
    print("            -    EN EL  "+str(float(((count_created_date_2021_alienvault_sh_pattern_filehashes*100)/count_created_date_2021_alienvault_sh)))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT CREADOS EN 2021, EL PATRÓN ES UN HASH DE UN ARCHIVO ")
    print("            -    EN EL  "+str(float(((count_created_date_2021_alienvault_sh_pattern_emailmessage*100)/count_created_date_2021_alienvault_sh)))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT CREADOS EN 2021, EL PATRÓN ES MENSAJE DE EMAIL ")
    print("            -    EN EL  "+str(float(((count_created_date_2021_alienvault_sh_pattern_ipv4addr*100)/count_created_date_2021_alienvault_sh)))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT CREADOS EN 2021, EL PATRÓN ES UNA DIRECCIÓN IPV4 ")
    print("\n")
if(count_created_date_2020_alienvault_sh>0):
    print("      -    EN EL  "+str(float(((count_created_date_2020_alienvault_sh*100)/count_alienvault_sh_totalpulses)))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2020. LOS PORCENTAJES DE PATRÓN SON LOS SIGUIENTES:  \n")
    print("\n")
    print("            -    EN EL  "+str(float(((count_created_date_2020_alienvault_sh_pattern_domainname*100)/count_created_date_2020_alienvault_sh)))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT CREADOS EN 2020, EL PATRÓN ES NOMBRE DE DOMINIO ")
    print("            -    EN EL  "+str(float(((count_created_date_2020_alienvault_sh_pattern_urlvalue*100)/count_created_date_2020_alienvault_sh)))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT CREADOS EN 2020, EL PATRÓN ES VALOR DE URL")
    print("            -    EN EL  "+str(float(((count_created_date_2020_alienvault_sh_pattern_filehashes*100)/count_created_date_2020_alienvault_sh)))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT CREADOS EN 2020, EL PATRÓN ES UN HASH DE UN ARCHIVO ")
    print("            -    EN EL  "+str(float(((count_created_date_2020_alienvault_sh_pattern_emailmessage*100)/count_created_date_2020_alienvault_sh)))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT CREADOS EN 2020, EL PATRÓN ES MENSAJE DE EMAIL ")
    print("            -    EN EL  "+str(float(((count_created_date_2020_alienvault_sh_pattern_ipv4addr*100)/count_created_date_2020_alienvault_sh)))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT CREADOS EN 2020, EL PATRÓN ES UNA DIRECCIÓN IPV4 ")
    print("\n")
if(count_created_date_2019_alienvault_sh>0):
    print("      -    EN EL  "+str(float(((count_created_date_2019_alienvault_sh*100)/count_alienvault_sh_totalpulses)))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2019. LOS PORCENTAJES DE PATRÓN SON LOS SIGUIENTES:  \n")
    print("\n")
    print("            -    EN EL  "+str(float(((count_created_date_2019_alienvault_sh_pattern_domainname*100)/count_created_date_2019_alienvault_sh)))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT CREADOS EN 2019, EL PATRÓN ES NOMBRE DE DOMINIO ")
    print("            -    EN EL  "+str(float(((count_created_date_2019_alienvault_sh_pattern_urlvalue*100)/count_created_date_2019_alienvault_sh)))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT CREADOS EN 2019, EL PATRÓN ES VALOR DE URL")
    print("            -    EN EL  "+str(float(((count_created_date_2019_alienvault_sh_pattern_filehashes*100)/count_created_date_2019_alienvault_sh)))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT CREADOS EN 2019, EL PATRÓN ES UN HASH DE UN ARCHIVO ")
    print("            -    EN EL  "+str(float(((count_created_date_2019_alienvault_sh_pattern_emailmessage*100)/count_created_date_2019_alienvault_sh)))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT CREADOS EN 2019, EL PATRÓN ES MENSAJE DE EMAIL ")
    print("            -    EN EL  "+str(float(((count_created_date_2019_alienvault_sh_pattern_ipv4addr*100)/count_created_date_2019_alienvault_sh)))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT CREADOS EN 2019, EL PATRÓN ES UNA DIRECCIÓN IPV4 ")
    print("\n")
if(count_created_date_2018_alienvault_sh>0):
    print("      -    EN EL  "+str(float(((count_created_date_2018_alienvault_sh*100)/count_alienvault_sh_totalpulses)))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2018 O ANTERIOR. LOS PORCENTAJES DE PATRÓN SON LOS SIGUIENTES:  \n")
    print("\n")
    print("            -    EN EL  "+str(float(((count_created_date_2018_alienvault_sh_pattern_domainname*100)/count_created_date_2018_alienvault_sh)))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT CREADOS EN 2018 O ANTERIORMENTE, EL PATRÓN ES NOMBRE DE DOMINIO ")
    print("            -    EN EL  "+str(float(((count_created_date_2018_alienvault_sh_pattern_urlvalue*100)/count_created_date_2018_alienvault_sh)))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT CREADOS EN 2018 O ANTERIORMENTE, EL PATRÓN ES VALOR DE URL")
    print("            -    EN EL  "+str(float(((count_created_date_2018_alienvault_sh_pattern_filehashes*100)/count_created_date_2018_alienvault_sh)))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT CREADOS EN 2018 O ANTERIORMENTE, EL PATRÓN ES UN HASH DE UN ARCHIVO ")
    print("            -    EN EL  "+str(float(((count_created_date_2018_alienvault_sh_pattern_emailmessage*100)/count_created_date_2018_alienvault_sh)))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT CREADOS EN 2018, EL PATRÓN ES MENSAJE DE EMAIL ")
    print("            -    EN EL  "+str(float(((count_created_date_2018_alienvault_sh_pattern_ipv4addr*100)/count_created_date_2018_alienvault_sh)))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT CREADOS EN 2018, EL PATRÓN ES UNA DIRECCIÓN IPV4 ")
    print("\n")
print("   - LOS PORCENTAJES DE PATRON SON LOS SIGUIENTES:  \n")
if(count_alienvault_sh_pattern_domainname>0):
    print("      -    EN EL  "+str(float(((count_alienvault_sh_pattern_domainname*100)/count_alienvault_sh_totalpulses)))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT EL PATRÓN ES NOMBRE DE DOMINIO. LOS PORCENTAJES DE FECHA DE CREACION SON LOS SIGUIENTES:  \n")
    print("\n")
    print("            -    EN EL  "+str(float(((count_created_date_2023_alienvault_sh_pattern_domainname*100)/count_alienvault_sh_pattern_domainname)))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2023 ")
    print("            -    EN EL  "+str(float(((count_created_date_2022_alienvault_sh_pattern_domainname*100)/count_alienvault_sh_pattern_domainname)))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2022")
    print("            -    EN EL  "+str(float(((count_created_date_2021_alienvault_sh_pattern_domainname*100)/count_alienvault_sh_pattern_domainname)))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2021 ")
    print("            -    EN EL  "+str(float(((count_created_date_2020_alienvault_sh_pattern_domainname*100)/count_alienvault_sh_pattern_domainname)))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2020 ")
    print("            -    EN EL  "+str(float(((count_created_date_2019_alienvault_sh_pattern_domainname*100)/count_alienvault_sh_pattern_domainname)))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2019")
    print("            -    EN EL  "+str(float(((count_created_date_2018_alienvault_sh_pattern_domainname*100)/count_alienvault_sh_pattern_domainname)))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2018 O ANTERIOR ")
    print("\n")
if(count_alienvault_sh_pattern_urlvalue>0):
    print("      -    EN EL  "+str(float(((count_alienvault_sh_pattern_urlvalue*100)/count_alienvault_sh_totalpulses)))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT EL PATRÓN ES VALOR DE URL. LOS PORCENTAJES DE FECHA DE CREACION SON LOS SIGUIENTES:  \n")
    print("\n")
    print("            -    EN EL  "+str(float(((count_created_date_2023_alienvault_sh_pattern_urlvalue*100)/count_alienvault_sh_pattern_urlvalue)))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2023 ")
    print("            -    EN EL  "+str(float(((count_created_date_2022_alienvault_sh_pattern_urlvalue*100)/count_alienvault_sh_pattern_urlvalue)))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2022")
    print("            -    EN EL  "+str(float(((count_created_date_2021_alienvault_sh_pattern_urlvalue*100)/count_alienvault_sh_pattern_urlvalue)))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2021 ")
    print("            -    EN EL  "+str(float(((count_created_date_2020_alienvault_sh_pattern_urlvalue*100)/count_alienvault_sh_pattern_urlvalue)))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2020 ")
    print("            -    EN EL  "+str(float(((count_created_date_2019_alienvault_sh_pattern_urlvalue*100)/count_alienvault_sh_pattern_urlvalue)))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2019")
    print("            -    EN EL  "+str(float(((count_created_date_2018_alienvault_sh_pattern_urlvalue*100)/count_alienvault_sh_pattern_urlvalue)))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2018 O ANTERIOR ")
    print("\n")
if(count_alienvault_sh_pattern_filehashes>0):
    print("      -    EN EL  "+str(float(((count_alienvault_sh_pattern_filehashes*100)/count_alienvault_sh_totalpulses)))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT EL PATRÓN ES UN HASH DE UN ARCHIVO. LOS PORCENTAJES DE FECHA DE CREACION SON LOS SIGUIENTES:  \n")
    print("\n")
    print("            -    EN EL  "+str(float(((count_created_date_2023_alienvault_sh_pattern_filehashes*100)/count_alienvault_sh_pattern_filehashes)))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2023 ")
    print("            -    EN EL  "+str(float(((count_created_date_2022_alienvault_sh_pattern_filehashes*100)/count_alienvault_sh_pattern_filehashes)))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2022")
    print("            -    EN EL  "+str(float(((count_created_date_2021_alienvault_sh_pattern_filehashes*100)/count_alienvault_sh_pattern_filehashes)))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2021 ")
    print("            -    EN EL  "+str(float(((count_created_date_2020_alienvault_sh_pattern_filehashes*100)/count_alienvault_sh_pattern_filehashes)))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2020 ")
    print("            -    EN EL  "+str(float(((count_created_date_2019_alienvault_sh_pattern_filehashes*100)/count_alienvault_sh_pattern_filehashes)))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2019")
    print("            -    EN EL  "+str(float(((count_created_date_2018_alienvault_sh_pattern_filehashes*100)/count_alienvault_sh_pattern_filehashes)))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2018 O ANTERIOR ")
    print("\n")
if(count_alienvault_sh_pattern_emailmessage>0):
    print("      -    EN EL  "+str(float(((count_alienvault_sh_pattern_emailmessage*100)/count_alienvault_sh_totalpulses)))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT EL PATRÓN ES MENSAJE DE EMAIL. LOS PORCENTAJES DE FECHA DE CREACION SON LOS SIGUIENTES:  \n")
    print("\n")
    print("            -    EN EL  "+str(float(((count_created_date_2023_alienvault_sh_pattern_emailmessage*100)/count_alienvault_sh_pattern_emailmessage)))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2023 ")
    print("            -    EN EL  "+str(float(((count_created_date_2022_alienvault_sh_pattern_emailmessage*100)/count_alienvault_sh_pattern_emailmessage)))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2022")
    print("            -    EN EL  "+str(float(((count_created_date_2021_alienvault_sh_pattern_emailmessage*100)/count_alienvault_sh_pattern_emailmessage)))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2021 ")
    print("            -    EN EL  "+str(float(((count_created_date_2020_alienvault_sh_pattern_emailmessage*100)/count_alienvault_sh_pattern_emailmessage)))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2020 ")
    print("            -    EN EL  "+str(float(((count_created_date_2019_alienvault_sh_pattern_emailmessage*100)/count_alienvault_sh_pattern_emailmessage)))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2019")
    print("            -    EN EL  "+str(float(((count_created_date_2018_alienvault_sh_pattern_emailmessage*100)/count_alienvault_sh_pattern_emailmessage)))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2018 O ANTERIOR ")
    print("\n")
if(count_alienvault_sh_pattern_ipv4addr>0):
    print("      -    EN EL  "+str(float(((count_alienvault_sh_pattern_ipv4addr*100)/count_alienvault_sh_totalpulses)))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT EL PATRÓN ES UNA DIRECCIÓN IPV4. LOS PORCENTAJES DE FECHA DE CREACION SON LOS SIGUIENTES:  \n")
    print("\n")
    print("            -    EN EL  "+str(float(((count_created_date_2023_alienvault_sh_pattern_ipv4addr*100)/count_alienvault_sh_pattern_ipv4addr)))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2023 ")
    print("            -    EN EL  "+str(float(((count_created_date_2022_alienvault_sh_pattern_ipv4addr*100)/count_alienvault_sh_pattern_ipv4addr)))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2022")
    print("            -    EN EL  "+str(float(((count_created_date_2021_alienvault_sh_pattern_ipv4addr*100)/count_alienvault_sh_pattern_ipv4addr)))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2021 ")
    print("            -    EN EL  "+str(float(((count_created_date_2020_alienvault_sh_pattern_ipv4addr*100)/count_alienvault_sh_pattern_ipv4addr)))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2020 ")
    print("            -    EN EL  "+str(float(((count_created_date_2019_alienvault_sh_pattern_ipv4addr*100)/count_alienvault_sh_pattern_ipv4addr)))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2019")
    print("            -    EN EL  "+str(float(((count_created_date_2018_alienvault_sh_pattern_ipv4addr*100)/count_alienvault_sh_pattern_ipv4addr)))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2018 O ANTERIOR ")
    print("\n")

    
    
    
    
    
    
    
    
    
    
print("******************ESTADÍSTICAS TIPO DE PATRÓN/FECHA DE CREACIÓN OBJETOS TIPO INDICADOR ALIENVAULT PARTE IOT Y SMART HOME CONJUNTAS******************")
print("\n")                            
                
print("\n")
print(" DE UN TOTAL DE "+str(count_alienvault_sh_totalpulses+count_alienvault_iot_totalpulses)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT :\n") 
print("\n")
print("   - LAS ESTADISTICAS DE FECHA DE CREACION SON LAS SIGUIENTES:  \n")
print("      -    EN  "+str(count_created_date_2023_alienvault_iot+count_created_date_2023_alienvault_sh)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2023. LAS ESTADÍSTICAS DE PATRÓN SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(count_created_date_2023_alienvault_iot_pattern_domainname+count_created_date_2023_alienvault_sh_pattern_domainname)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT CREADOS EN 2023, EL PATRÓN ES NOMBRE DE DOMINIO ")
print("            -    EN  "+str(count_created_date_2023_alienvault_iot_pattern_urlvalue+count_created_date_2023_alienvault_sh_pattern_urlvalue)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT CREADOS EN 2023, EL PATRÓN ES VALOR DE URL")
print("            -    EN  "+str(count_created_date_2023_alienvault_iot_pattern_filehashes+count_created_date_2023_alienvault_sh_pattern_filehashes)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT CREADOS EN 2023, EL PATRÓN ES UN HASH DE UN ARCHIVO ")
print("            -    EN  "+str(count_created_date_2023_alienvault_iot_pattern_emailmessage+count_created_date_2023_alienvault_sh_pattern_emailmessage)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT CREADOS EN 2023, EL PATRÓN ES MENSAJE DE EMAIL ")
print("            -    EN  "+str(count_created_date_2023_alienvault_iot_pattern_ipv4addr+count_created_date_2023_alienvault_sh_pattern_ipv4addr)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT CREADOS EN 2023, EL PATRÓN ES UNA DIRECCIÓN IPV4 ")
print("\n")
print("      -    EN  "+str(count_created_date_2022_alienvault_iot+count_created_date_2022_alienvault_sh)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2022. LAS ESTADÍSTICAS DE PATRÓN SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(count_created_date_2022_alienvault_iot_pattern_domainname+count_created_date_2022_alienvault_sh_pattern_domainname)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT CREADOS EN 2022, EL PATRÓN ES NOMBRE DE DOMINIO ")
print("            -    EN  "+str(count_created_date_2022_alienvault_iot_pattern_urlvalue+count_created_date_2022_alienvault_sh_pattern_urlvalue)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT CREADOS EN 2022, EL PATRÓN ES VALOR DE URL")
print("            -    EN  "+str(count_created_date_2022_alienvault_iot_pattern_filehashes+count_created_date_2022_alienvault_sh_pattern_filehashes)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT CREADOS EN 2022, EL PATRÓN ES UN HASH DE UN ARCHIVO ")
print("            -    EN  "+str(count_created_date_2022_alienvault_iot_pattern_emailmessage+count_created_date_2022_alienvault_sh_pattern_emailmessage)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT CREADOS EN 2022, EL PATRÓN ES MENSAJE DE EMAIL ")
print("            -    EN  "+str(count_created_date_2022_alienvault_iot_pattern_ipv4addr+count_created_date_2022_alienvault_sh_pattern_ipv4addr)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT CREADOS EN 2022, EL PATRÓN ES UNA DIRECCIÓN IPV4 ")
print("\n")
print("      -    EN  "+str(count_created_date_2021_alienvault_iot+count_created_date_2021_alienvault_sh)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2021. LAS ESTADÍSTICAS DE PATRÓN SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(count_created_date_2021_alienvault_iot_pattern_domainname+count_created_date_2021_alienvault_sh_pattern_domainname)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT CREADOS EN 2021, EL PATRÓN ES NOMBRE DE DOMINIO ")
print("            -    EN  "+str(count_created_date_2021_alienvault_iot_pattern_urlvalue+count_created_date_2021_alienvault_sh_pattern_urlvalue)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT CREADOS EN 2021, EL PATRÓN ES VALOR DE URL")
print("            -    EN  "+str(count_created_date_2021_alienvault_iot_pattern_filehashes+count_created_date_2021_alienvault_sh_pattern_filehashes)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT CREADOS EN 2021, EL PATRÓN ES UN HASH DE UN ARCHIVO ")
print("            -    EN  "+str(count_created_date_2021_alienvault_iot_pattern_emailmessage+count_created_date_2021_alienvault_sh_pattern_emailmessage)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT CREADOS EN 2021, EL PATRÓN ES MENSAJE DE EMAIL ")
print("            -    EN  "+str(count_created_date_2021_alienvault_iot_pattern_ipv4addr+count_created_date_2021_alienvault_sh_pattern_ipv4addr)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT CREADOS EN 2021, EL PATRÓN ES UNA DIRECCIÓN IPV4 ")
print("\n")
print("      -    EN  "+str(count_created_date_2020_alienvault_iot+count_created_date_2020_alienvault_sh)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2020. LAS ESTADÍSTICAS DE PATRÓN SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(count_created_date_2020_alienvault_iot_pattern_domainname+count_created_date_2020_alienvault_sh_pattern_domainname)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT CREADOS EN 2020, EL PATRÓN ES NOMBRE DE DOMINIO ")
print("            -    EN  "+str(count_created_date_2020_alienvault_iot_pattern_urlvalue+count_created_date_2020_alienvault_sh_pattern_urlvalue)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT CREADOS EN 2020, EL PATRÓN ES VALOR DE URL")
print("            -    EN  "+str(count_created_date_2020_alienvault_iot_pattern_filehashes+count_created_date_2020_alienvault_sh_pattern_filehashes)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT CREADOS EN 2020, EL PATRÓN ES UN HASH DE UN ARCHIVO ")
print("            -    EN  "+str(count_created_date_2020_alienvault_iot_pattern_emailmessage+count_created_date_2020_alienvault_sh_pattern_emailmessage)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT CREADOS EN 2020, EL PATRÓN ES MENSAJE DE EMAIL ")
print("            -    EN  "+str(count_created_date_2020_alienvault_iot_pattern_ipv4addr+count_created_date_2020_alienvault_sh_pattern_ipv4addr)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT CREADOS EN 2020, EL PATRÓN ES UNA DIRECCIÓN IPV4 ")
print("\n")
print("      -    EN  "+str(count_created_date_2019_alienvault_iot+count_created_date_2019_alienvault_sh)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2019. LAS ESTADÍSTICAS DE PATRÓN SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(count_created_date_2019_alienvault_iot_pattern_domainname+count_created_date_2019_alienvault_sh_pattern_domainname)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT CREADOS EN 2019, EL PATRÓN ES NOMBRE DE DOMINIO ")
print("            -    EN  "+str(count_created_date_2019_alienvault_iot_pattern_urlvalue+count_created_date_2019_alienvault_sh_pattern_urlvalue)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT CREADOS EN 2019, EL PATRÓN ES VALOR DE URL")
print("            -    EN  "+str(count_created_date_2019_alienvault_iot_pattern_filehashes+count_created_date_2019_alienvault_sh_pattern_filehashes)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT CREADOS EN 2019, EL PATRÓN ES UN HASH DE UN ARCHIVO ")
print("            -    EN  "+str(count_created_date_2019_alienvault_iot_pattern_emailmessage+count_created_date_2019_alienvault_sh_pattern_emailmessage)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT CREADOS EN 2019, EL PATRÓN ES MENSAJE DE EMAIL ")
print("            -    EN  "+str(count_created_date_2019_alienvault_iot_pattern_ipv4addr+count_created_date_2019_alienvault_sh_pattern_ipv4addr)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT CREADOS EN 2019, EL PATRÓN ES UNA DIRECCIÓN IPV4 ")
print("\n")
print("      -    EN  "+str(count_created_date_2018_alienvault_iot+count_created_date_2018_alienvault_sh)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2018. LAS ESTADÍSTICAS DE PATRÓN SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(count_created_date_2018_alienvault_iot_pattern_domainname+count_created_date_2018_alienvault_sh_pattern_domainname)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT CREADOS EN 2018, EL PATRÓN ES NOMBRE DE DOMINIO ")
print("            -    EN  "+str(count_created_date_2018_alienvault_iot_pattern_urlvalue+count_created_date_2018_alienvault_sh_pattern_urlvalue)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT CREADOS EN 2018, EL PATRÓN ES VALOR DE URL")
print("            -    EN  "+str(count_created_date_2018_alienvault_iot_pattern_filehashes+count_created_date_2018_alienvault_sh_pattern_filehashes)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT CREADOS EN 2018, EL PATRÓN ES UN HASH DE UN ARCHIVO ")
print("            -    EN  "+str(count_created_date_2018_alienvault_iot_pattern_emailmessage+count_created_date_2018_alienvault_sh_pattern_emailmessage)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT CREADOS EN 2018, EL PATRÓN ES MENSAJE DE EMAIL ")
print("            -    EN  "+str(count_created_date_2018_alienvault_iot_pattern_ipv4addr+count_created_date_2018_alienvault_sh_pattern_ipv4addr)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT CREADOS EN 2018, EL PATRÓN ES UNA DIRECCIÓN IPV4 ")
print("\n")
print("   - LAS ESTADISTICAS DE PATRON SON LAS SIGUIENTES:  \n")
print("      -    EN  "+str(count_alienvault_iot_pattern_domainname+count_alienvault_sh_pattern_domainname)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT EL PATRÓN ES NOMBRE DE DOMINIO. LAS ESTADÍSTICAS DE FECHA DE CREACION SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(count_created_date_2023_alienvault_iot_pattern_domainname+count_created_date_2023_alienvault_sh_pattern_domainname)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2023 ")
print("            -    EN  "+str(count_created_date_2022_alienvault_iot_pattern_domainname+count_created_date_2022_alienvault_sh_pattern_domainname)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2022")
print("            -    EN  "+str(count_created_date_2021_alienvault_iot_pattern_domainname+count_created_date_2021_alienvault_sh_pattern_domainname)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2021 ")
print("            -    EN  "+str(count_created_date_2020_alienvault_iot_pattern_domainname+count_created_date_2020_alienvault_sh_pattern_domainname)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2020 ")
print("            -    EN  "+str(count_created_date_2019_alienvault_iot_pattern_domainname+count_created_date_2019_alienvault_sh_pattern_domainname)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2019")
print("            -    EN  "+str(count_created_date_2018_alienvault_iot_pattern_domainname+count_created_date_2018_alienvault_sh_pattern_domainname)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2018 O ANTERIOR ")
print("\n")
print("      -    EN  "+str(count_alienvault_iot_pattern_urlvalue+count_alienvault_sh_pattern_urlvalue)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT EL PATRÓN ES VALOR DE URL. LAS ESTADÍSTICAS DE FECHA DE CREACION SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(count_created_date_2023_alienvault_iot_pattern_urlvalue+count_created_date_2023_alienvault_sh_pattern_urlvalue)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2023 ")
print("            -    EN  "+str(count_created_date_2022_alienvault_iot_pattern_urlvalue+count_created_date_2022_alienvault_sh_pattern_urlvalue)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2022")
print("            -    EN  "+str(count_created_date_2021_alienvault_iot_pattern_urlvalue+count_created_date_2021_alienvault_sh_pattern_urlvalue)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2021 ")
print("            -    EN  "+str(count_created_date_2020_alienvault_iot_pattern_urlvalue+count_created_date_2020_alienvault_sh_pattern_urlvalue)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2020 ")
print("            -    EN  "+str(count_created_date_2019_alienvault_iot_pattern_urlvalue+count_created_date_2019_alienvault_sh_pattern_urlvalue)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2019")
print("            -    EN  "+str(count_created_date_2018_alienvault_iot_pattern_urlvalue+count_created_date_2018_alienvault_sh_pattern_urlvalue)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2018 O ANTERIOR ")
print("\n")
print("      -    EN  "+str(count_alienvault_iot_pattern_filehashes+count_alienvault_sh_pattern_filehashes)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT EL PATRÓN ES UN HASH DE UN ARCHIVO. LAS ESTADÍSTICAS DE FECHA DE CREACION SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(count_created_date_2023_alienvault_iot_pattern_filehashes+count_created_date_2023_alienvault_sh_pattern_filehashes)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2023 ")
print("            -    EN  "+str(count_created_date_2022_alienvault_iot_pattern_filehashes+count_created_date_2022_alienvault_sh_pattern_filehashes)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2022")
print("            -    EN  "+str(count_created_date_2021_alienvault_iot_pattern_filehashes+count_created_date_2021_alienvault_sh_pattern_filehashes)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2021 ")
print("            -    EN  "+str(count_created_date_2020_alienvault_iot_pattern_filehashes+count_created_date_2020_alienvault_sh_pattern_filehashes)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2020 ")
print("            -    EN  "+str(count_created_date_2019_alienvault_iot_pattern_filehashes+count_created_date_2019_alienvault_sh_pattern_filehashes)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2019")
print("            -    EN  "+str(count_created_date_2018_alienvault_iot_pattern_filehashes+count_created_date_2018_alienvault_sh_pattern_filehashes)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2018 O ANTERIOR ")
print("\n")
print("      -    EN  "+str(count_alienvault_iot_pattern_emailmessage+count_alienvault_sh_pattern_emailmessage)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT EL PATRÓN ES MENSAJE DE EMAIL. LAS ESTADÍSTICAS DE FECHA DE CREACION SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(count_created_date_2023_alienvault_iot_pattern_emailmessage+count_created_date_2023_alienvault_sh_pattern_emailmessage)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2023 ")
print("            -    EN  "+str(count_created_date_2022_alienvault_iot_pattern_emailmessage+count_created_date_2022_alienvault_sh_pattern_emailmessage)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2022")
print("            -    EN  "+str(count_created_date_2021_alienvault_iot_pattern_emailmessage+count_created_date_2021_alienvault_sh_pattern_emailmessage)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2021 ")
print("            -    EN  "+str(count_created_date_2020_alienvault_iot_pattern_emailmessage+count_created_date_2020_alienvault_sh_pattern_emailmessage)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2020 ")
print("            -    EN  "+str(count_created_date_2019_alienvault_iot_pattern_emailmessage+count_created_date_2019_alienvault_sh_pattern_emailmessage)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2019")
print("            -    EN  "+str(count_created_date_2018_alienvault_iot_pattern_emailmessage+count_created_date_2018_alienvault_sh_pattern_emailmessage)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2018 O ANTERIOR ")
print("\n")
print("      -    EN  "+str(count_alienvault_iot_pattern_ipv4addr+count_alienvault_sh_pattern_ipv4addr)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT EL PATRÓN ES UNA DIRECCIÓN IPV4. LAS ESTADÍSTICAS DE FECHA DE CREACION SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(count_created_date_2023_alienvault_iot_pattern_ipv4addr+count_created_date_2023_alienvault_sh_pattern_ipv4addr)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2023 ")
print("            -    EN  "+str(count_created_date_2022_alienvault_iot_pattern_ipv4addr+count_created_date_2022_alienvault_sh_pattern_ipv4addr)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2022")
print("            -    EN  "+str(count_created_date_2021_alienvault_iot_pattern_ipv4addr+count_created_date_2021_alienvault_sh_pattern_ipv4addr)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2021 ")
print("            -    EN  "+str(count_created_date_2020_alienvault_iot_pattern_ipv4addr+count_created_date_2020_alienvault_sh_pattern_ipv4addr)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2020 ")
print("            -    EN  "+str(count_created_date_2019_alienvault_iot_pattern_ipv4addr+count_created_date_2019_alienvault_sh_pattern_ipv4addr)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2019")
print("            -    EN  "+str(count_created_date_2018_alienvault_iot_pattern_ipv4addr+count_created_date_2018_alienvault_sh_pattern_ipv4addr)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2018 O ANTERIOR ")
print("\n")













print("******************PORCENTAJE TIPO DE PATRÓN/FECHA DE CREACIÓN OBJETOS TIPO INDICADOR DATE ALIENVAULT PARTE IOT Y SMART HOME CONJUNTAS******************")
print("\n")                            
                
print("\n")
print(" DE UN TOTAL DE "+str(count_alienvault_sh_totalpulses+count_alienvault_iot_totalpulses)+" OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT :\n") 
print("\n")
print("   - LOS PORCENTAJES DE FECHA DE CREACION SON LOS SIGUIENTES:  \n")
if((count_created_date_2023_alienvault_iot+count_created_date_2023_alienvault_sh)>0):
    print("      -    EN EL  "+str(float(((count_created_date_2023_alienvault_iot+count_created_date_2023_alienvault_sh)*100)/(count_alienvault_sh_totalpulses+count_alienvault_iot_totalpulses)))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2023. LOS PORCENTAJES DE PATRÓN SON LOS SIGUIENTES:  \n")
    print("\n")
    print("            -    EN EL  "+str(float((((count_created_date_2023_alienvault_iot_pattern_domainname+count_created_date_2023_alienvault_sh_pattern_domainname)*100)/(count_created_date_2023_alienvault_iot+count_created_date_2023_alienvault_sh))))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT CREADOS EN 2023, EL PATRÓN ES NOMBRE DE DOMINIO ")
    print("            -    EN EL  "+str(float((((count_created_date_2023_alienvault_iot_pattern_urlvalue+count_created_date_2023_alienvault_sh_pattern_urlvalue)*100)/(count_created_date_2023_alienvault_iot+count_created_date_2023_alienvault_sh))))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT CREADOS EN 2023, EL PATRÓN ES VALOR DE URL")
    print("            -    EN EL  "+str(float((((count_created_date_2023_alienvault_iot_pattern_filehashes+count_created_date_2023_alienvault_sh_pattern_filehashes)*100)/(count_created_date_2023_alienvault_iot+count_created_date_2023_alienvault_sh))))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT CREADOS EN 2023, EL PATRÓN ES UN HASH DE UN ARCHIVO ")
    print("            -    EN EL  "+str(float((((count_created_date_2023_alienvault_iot_pattern_emailmessage+count_created_date_2023_alienvault_sh_pattern_emailmessage)*100)/(count_created_date_2023_alienvault_iot+count_created_date_2023_alienvault_sh))))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT CREADOS EN 2023, EL PATRÓN ES MENSAJE DE EMAIL ")
    print("            -    EN EL  "+str(float((((count_created_date_2023_alienvault_iot_pattern_ipv4addr+count_created_date_2023_alienvault_sh_pattern_ipv4addr)*100)/(count_created_date_2023_alienvault_iot+count_created_date_2023_alienvault_sh))))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT CREADOS EN 2023, EL PATRÓN ES UNA DIRECCIÓN IPV4 ")
    print("\n")
if((count_created_date_2022_alienvault_iot+count_created_date_2022_alienvault_sh)>0):
    print("      -    EN EL  "+str(float(((count_created_date_2022_alienvault_iot+count_created_date_2022_alienvault_sh)*100)/(count_alienvault_sh_totalpulses+count_alienvault_iot_totalpulses)))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2022. LOS PORCENTAJES DE PATRÓN SON LOS SIGUIENTES:  \n")
    print("\n")
    print("            -    EN EL  "+str(float((((count_created_date_2022_alienvault_iot_pattern_domainname+count_created_date_2022_alienvault_sh_pattern_domainname)*100)/(count_created_date_2022_alienvault_iot+count_created_date_2022_alienvault_sh))))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT CREADOS EN 2022, EL PATRÓN ES NOMBRE DE DOMINIO ")
    print("            -    EN EL  "+str(float((((count_created_date_2022_alienvault_iot_pattern_urlvalue+count_created_date_2022_alienvault_sh_pattern_urlvalue)*100)/(count_created_date_2022_alienvault_iot+count_created_date_2022_alienvault_sh))))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT CREADOS EN 2022, EL PATRÓN ES VALOR DE URL")
    print("            -    EN EL  "+str(float((((count_created_date_2022_alienvault_iot_pattern_filehashes+count_created_date_2022_alienvault_sh_pattern_filehashes)*100)/(count_created_date_2022_alienvault_iot+count_created_date_2022_alienvault_sh))))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT CREADOS EN 2022, EL PATRÓN ES UN HASH DE UN ARCHIVO ")
    print("            -    EN EL  "+str(float((((count_created_date_2022_alienvault_iot_pattern_emailmessage+count_created_date_2022_alienvault_sh_pattern_emailmessage)*100)/(count_created_date_2022_alienvault_iot+count_created_date_2022_alienvault_sh))))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT CREADOS EN 2022, EL PATRÓN ES MENSAJE DE EMAIL ")
    print("            -    EN EL  "+str(float((((count_created_date_2022_alienvault_iot_pattern_ipv4addr+count_created_date_2022_alienvault_sh_pattern_ipv4addr)*100)/(count_created_date_2022_alienvault_iot+count_created_date_2022_alienvault_sh))))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT CREADOS EN 2022, EL PATRÓN ES UNA DIRECCIÓN IPV4 ")
    print("\n")
if((count_created_date_2021_alienvault_iot+count_created_date_2021_alienvault_sh)>0):
    print("      -    EN EL  "+str(float(((count_created_date_2021_alienvault_iot+count_created_date_2021_alienvault_sh)*100)/(count_alienvault_sh_totalpulses+count_alienvault_iot_totalpulses)))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2021. LOS PORCENTAJES DE PATRÓN SON LOS SIGUIENTES:  \n")
    print("\n")
    print("            -    EN EL  "+str(float((((count_created_date_2021_alienvault_iot_pattern_domainname+count_created_date_2021_alienvault_sh_pattern_domainname)*100)/(count_created_date_2021_alienvault_iot+count_created_date_2021_alienvault_sh))))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT CREADOS EN 2021, EL PATRÓN ES NOMBRE DE DOMINIO ")
    print("            -    EN EL  "+str(float((((count_created_date_2021_alienvault_iot_pattern_urlvalue+count_created_date_2021_alienvault_sh_pattern_urlvalue)*100)/(count_created_date_2021_alienvault_iot+count_created_date_2021_alienvault_sh))))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT CREADOS EN 2021, EL PATRÓN ES VALOR DE URL")
    print("            -    EN EL  "+str(float((((count_created_date_2021_alienvault_iot_pattern_filehashes+count_created_date_2021_alienvault_sh_pattern_filehashes)*100)/(count_created_date_2021_alienvault_iot+count_created_date_2021_alienvault_sh))))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT CREADOS EN 2021, EL PATRÓN ES UN HASH DE UN ARCHIVO ")
    print("            -    EN EL  "+str(float((((count_created_date_2021_alienvault_iot_pattern_emailmessage+count_created_date_2021_alienvault_sh_pattern_emailmessage)*100)/(count_created_date_2021_alienvault_iot+count_created_date_2021_alienvault_sh))))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT CREADOS EN 2021, EL PATRÓN ES MENSAJE DE EMAIL ")
    print("            -    EN EL  "+str(float((((count_created_date_2021_alienvault_iot_pattern_ipv4addr+count_created_date_2021_alienvault_sh_pattern_ipv4addr)*100)/(count_created_date_2021_alienvault_iot+count_created_date_2021_alienvault_sh))))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT CREADOS EN 2021, EL PATRÓN ES UNA DIRECCIÓN IPV4 ")
    print("\n")
if((count_created_date_2020_alienvault_iot+count_created_date_2020_alienvault_sh)>0):
    print("      -    EN EL  "+str(float(((count_created_date_2020_alienvault_iot+count_created_date_2020_alienvault_sh)*100)/(count_alienvault_sh_totalpulses+count_alienvault_iot_totalpulses)))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2020. LOS PORCENTAJES DE PATRÓN SON LOS SIGUIENTES:  \n")
    print("\n")
    print("            -    EN EL  "+str(float((((count_created_date_2020_alienvault_iot_pattern_domainname+count_created_date_2020_alienvault_sh_pattern_domainname)*100)/(count_created_date_2020_alienvault_iot+count_created_date_2020_alienvault_sh))))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT CREADOS EN 2020, EL PATRÓN ES NOMBRE DE DOMINIO ")
    print("            -    EN EL  "+str(float((((count_created_date_2020_alienvault_iot_pattern_urlvalue+count_created_date_2020_alienvault_sh_pattern_urlvalue)*100)/(count_created_date_2020_alienvault_iot+count_created_date_2020_alienvault_sh))))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT CREADOS EN 2020, EL PATRÓN ES VALOR DE URL")
    print("            -    EN EL  "+str(float((((count_created_date_2020_alienvault_iot_pattern_filehashes+count_created_date_2020_alienvault_sh_pattern_filehashes)*100)/(count_created_date_2020_alienvault_iot+count_created_date_2020_alienvault_sh))))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT CREADOS EN 2020, EL PATRÓN ES UN HASH DE UN ARCHIVO ")
    print("            -    EN EL  "+str(float((((count_created_date_2020_alienvault_iot_pattern_emailmessage+count_created_date_2020_alienvault_sh_pattern_emailmessage)*100)/(count_created_date_2020_alienvault_iot+count_created_date_2020_alienvault_sh))))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT CREADOS EN 2020, EL PATRÓN ES MENSAJE DE EMAIL ")
    print("            -    EN EL  "+str(float((((count_created_date_2020_alienvault_iot_pattern_ipv4addr+count_created_date_2020_alienvault_sh_pattern_ipv4addr)*100)/(count_created_date_2020_alienvault_iot+count_created_date_2020_alienvault_sh))))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT CREADOS EN 2020, EL PATRÓN ES UNA DIRECCIÓN IPV4 ")
    print("\n")
if((count_created_date_2019_alienvault_iot+count_created_date_2019_alienvault_sh)>0):
    print("      -    EN EL  "+str(float(((count_created_date_2019_alienvault_iot+count_created_date_2019_alienvault_sh)*100)/(count_alienvault_sh_totalpulses+count_alienvault_iot_totalpulses)))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2019. LOS PORCENTAJES DE PATRÓN SON LOS SIGUIENTES:  \n")
    print("\n")
    print("            -    EN EL  "+str(float((((count_created_date_2019_alienvault_iot_pattern_domainname+count_created_date_2019_alienvault_sh_pattern_domainname)*100)/(count_created_date_2019_alienvault_iot+count_created_date_2019_alienvault_sh))))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT CREADOS EN 2019, EL PATRÓN ES NOMBRE DE DOMINIO ")
    print("            -    EN EL  "+str(float((((count_created_date_2019_alienvault_iot_pattern_urlvalue+count_created_date_2019_alienvault_sh_pattern_urlvalue)*100)/(count_created_date_2019_alienvault_iot+count_created_date_2019_alienvault_sh))))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT CREADOS EN 2019, EL PATRÓN ES VALOR DE URL")
    print("            -    EN EL  "+str(float((((count_created_date_2019_alienvault_iot_pattern_filehashes+count_created_date_2019_alienvault_sh_pattern_filehashes)*100)/(count_created_date_2019_alienvault_iot+count_created_date_2019_alienvault_sh))))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT CREADOS EN 2019, EL PATRÓN ES UN HASH DE UN ARCHIVO ")
    print("            -    EN EL  "+str(float((((count_created_date_2019_alienvault_iot_pattern_emailmessage+count_created_date_2019_alienvault_sh_pattern_emailmessage)*100)/(count_created_date_2019_alienvault_iot+count_created_date_2019_alienvault_sh))))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT CREADOS EN 2019, EL PATRÓN ES MENSAJE DE EMAIL ")
    print("            -    EN EL  "+str(float((((count_created_date_2019_alienvault_iot_pattern_ipv4addr+count_created_date_2019_alienvault_sh_pattern_ipv4addr)*100)/(count_created_date_2019_alienvault_iot+count_created_date_2019_alienvault_sh))))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT CREADOS EN 2019, EL PATRÓN ES UNA DIRECCIÓN IPV4 ")
    print("\n")
if((count_created_date_2018_alienvault_iot+count_created_date_2018_alienvault_sh)>0):
    print("      -    EN EL  "+str(float(((count_created_date_2018_alienvault_iot+count_created_date_2018_alienvault_sh)*100)/(count_alienvault_sh_totalpulses+count_alienvault_iot_totalpulses)))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2018 O ANTERIOR. LOS PORCENTAJES DE PATRÓN SON LOS SIGUIENTES:  \n")
    print("\n")
    print("            -    EN EL  "+str(float((((count_created_date_2018_alienvault_iot_pattern_domainname+count_created_date_2018_alienvault_sh_pattern_domainname)*100)/(count_created_date_2018_alienvault_iot+count_created_date_2018_alienvault_sh))))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT CREADOS EN 2018 O ANTERIORMENTE, EL PATRÓN ES NOMBRE DE DOMINIO ")
    print("            -    EN EL  "+str(float((((count_created_date_2018_alienvault_iot_pattern_urlvalue+count_created_date_2018_alienvault_sh_pattern_urlvalue)*100)/(count_created_date_2018_alienvault_iot+count_created_date_2018_alienvault_sh))))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT CREADOS EN 2018 O ANTERIORMENTE, EL PATRÓN ES VALOR DE URL")
    print("            -    EN EL  "+str(float((((count_created_date_2018_alienvault_iot_pattern_filehashes+count_created_date_2018_alienvault_sh_pattern_filehashes)*100)/(count_created_date_2018_alienvault_iot+count_created_date_2018_alienvault_sh))))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT CREADOS EN 2018 O ANTERIORMENTE, EL PATRÓN ES UN HASH DE UN ARCHIVO ")
    print("            -    EN EL  "+str(float((((count_created_date_2018_alienvault_iot_pattern_emailmessage+count_created_date_2018_alienvault_sh_pattern_emailmessage)*100)/(count_created_date_2018_alienvault_iot+count_created_date_2018_alienvault_sh))))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT CREADOS EN 2018 O ANTERIORMENTE, EL PATRÓN ES MENSAJE DE EMAIL ")
    print("            -    EN EL  "+str(float((((count_created_date_2018_alienvault_iot_pattern_ipv4addr+count_created_date_2018_alienvault_sh_pattern_ipv4addr)*100)/(count_created_date_2018_alienvault_iot+count_created_date_2018_alienvault_sh))))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT CREADOS EN 2018, EL PATRÓN ES UNA DIRECCIÓN IPV4 ")
    print("\n")
print("   - LOS PORCENTAJES DE PATRON SON LOS SIGUIENTES:  \n")
print("      -    EN EL  "+str(float((((count_alienvault_iot_pattern_domainname+count_alienvault_sh_pattern_domainname)*100)/(count_alienvault_sh_totalpulses+count_alienvault_iot_totalpulses))))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT EL PATRÓN ES NOMBRE DE DOMINIO. LOS PORCENTAJES DE FECHA DE CREACION SON LOS SIGUIENTES:  \n")
print("\n")
print("            -    EN EL  "+str(float((((count_created_date_2023_alienvault_iot_pattern_domainname+count_created_date_2023_alienvault_sh_pattern_domainname)*100)/(count_alienvault_iot_pattern_domainname+count_alienvault_sh_pattern_domainname))))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2023 ")
print("            -    EN EL  "+str(float((((count_created_date_2022_alienvault_iot_pattern_domainname+count_created_date_2022_alienvault_sh_pattern_domainname)*100)/(count_alienvault_iot_pattern_domainname+count_alienvault_sh_pattern_domainname))))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2022")
print("            -    EN EL  "+str(float((((count_created_date_2021_alienvault_iot_pattern_domainname+count_created_date_2021_alienvault_sh_pattern_domainname)*100)/(count_alienvault_iot_pattern_domainname+count_alienvault_sh_pattern_domainname))))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2021 ")
print("            -    EN EL  "+str(float((((count_created_date_2020_alienvault_iot_pattern_domainname+count_created_date_2020_alienvault_sh_pattern_domainname)*100)/(count_alienvault_iot_pattern_domainname+count_alienvault_sh_pattern_domainname))))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2020 ")
print("            -    EN EL  "+str(float((((count_created_date_2019_alienvault_iot_pattern_domainname+count_created_date_2019_alienvault_sh_pattern_domainname)*100)/(count_alienvault_iot_pattern_domainname+count_alienvault_sh_pattern_domainname))))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2019")
print("            -    EN EL  "+str(float((((count_created_date_2018_alienvault_iot_pattern_domainname+count_created_date_2018_alienvault_sh_pattern_domainname)*100)/(count_alienvault_iot_pattern_domainname+count_alienvault_sh_pattern_domainname))))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2018 O ANTERIOR ")
print("\n")
print("      -    EN EL  "+str(float((((count_alienvault_iot_pattern_urlvalue+count_alienvault_sh_pattern_urlvalue)*100)/(count_alienvault_sh_totalpulses+count_alienvault_iot_totalpulses))))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT EL PATRÓN ES VALOR DE URL. LOS PORCENTAJES DE FECHA DE CREACION SON LOS SIGUIENTES:  \n")
print("\n")
print("            -    EN EL  "+str(float((((count_created_date_2023_alienvault_iot_pattern_urlvalue+count_created_date_2023_alienvault_sh_pattern_urlvalue)*100)/(count_alienvault_iot_pattern_urlvalue+count_alienvault_sh_pattern_urlvalue))))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2023 ")
print("            -    EN EL  "+str(float((((count_created_date_2022_alienvault_iot_pattern_urlvalue+count_created_date_2022_alienvault_sh_pattern_urlvalue)*100)/(count_alienvault_iot_pattern_urlvalue+count_alienvault_sh_pattern_urlvalue))))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2022")
print("            -    EN EL  "+str(float((((count_created_date_2021_alienvault_iot_pattern_urlvalue+count_created_date_2021_alienvault_sh_pattern_urlvalue)*100)/(count_alienvault_iot_pattern_urlvalue+count_alienvault_sh_pattern_urlvalue))))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2021 ")
print("            -    EN EL  "+str(float((((count_created_date_2020_alienvault_iot_pattern_urlvalue+count_created_date_2020_alienvault_sh_pattern_urlvalue)*100)/(count_alienvault_iot_pattern_urlvalue+count_alienvault_sh_pattern_urlvalue))))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2020 ")
print("            -    EN EL  "+str(float((((count_created_date_2019_alienvault_iot_pattern_urlvalue+count_created_date_2019_alienvault_sh_pattern_urlvalue)*100)/(count_alienvault_iot_pattern_urlvalue+count_alienvault_sh_pattern_urlvalue))))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2019")
print("            -    EN EL  "+str(float((((count_created_date_2018_alienvault_iot_pattern_urlvalue+count_created_date_2018_alienvault_sh_pattern_urlvalue)*100)/(count_alienvault_iot_pattern_urlvalue+count_alienvault_sh_pattern_urlvalue))))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2018 O ANTERIOR ")
print("\n")
print("      -    EN EL  "+str(float((((count_alienvault_iot_pattern_filehashes+count_alienvault_sh_pattern_filehashes)*100)/(count_alienvault_sh_totalpulses+count_alienvault_iot_totalpulses))))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT EL PATRÓN ES UN HASH DE UN ARCHIVO. LOS PORCENTAJES DE FECHA DE CREACION SON LOS SIGUIENTES:  \n")
print("\n")
print("            -    EN EL  "+str(float((((count_created_date_2023_alienvault_iot_pattern_filehashes+count_created_date_2023_alienvault_sh_pattern_filehashes)*100)/(count_alienvault_iot_pattern_filehashes+count_alienvault_sh_pattern_filehashes))))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2023 ")
print("            -    EN EL  "+str(float((((count_created_date_2022_alienvault_iot_pattern_filehashes+count_created_date_2022_alienvault_sh_pattern_filehashes)*100)/(count_alienvault_iot_pattern_filehashes+count_alienvault_sh_pattern_filehashes))))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2022")
print("            -    EN EL  "+str(float((((count_created_date_2021_alienvault_iot_pattern_filehashes+count_created_date_2021_alienvault_sh_pattern_filehashes)*100)/(count_alienvault_iot_pattern_filehashes+count_alienvault_sh_pattern_filehashes))))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2021 ")
print("            -    EN EL  "+str(float((((count_created_date_2020_alienvault_iot_pattern_filehashes+count_created_date_2020_alienvault_sh_pattern_filehashes)*100)/(count_alienvault_iot_pattern_filehashes+count_alienvault_sh_pattern_filehashes))))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2020 ")
print("            -    EN EL  "+str(float((((count_created_date_2019_alienvault_iot_pattern_filehashes+count_created_date_2019_alienvault_sh_pattern_filehashes)*100)/(count_alienvault_iot_pattern_filehashes+count_alienvault_sh_pattern_filehashes))))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2019")
print("            -    EN EL  "+str(float((((count_created_date_2018_alienvault_iot_pattern_filehashes+count_created_date_2018_alienvault_sh_pattern_filehashes)*100)/(count_alienvault_iot_pattern_filehashes+count_alienvault_sh_pattern_filehashes))))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2018 O ANTERIOR ")
print("\n")
print("      -    EN EL  "+str(float((((count_alienvault_iot_pattern_emailmessage+count_alienvault_sh_pattern_emailmessage)*100)/(count_alienvault_sh_totalpulses+count_alienvault_iot_totalpulses))))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT EL PATRÓN ES MENSAJE DE EMAIL. LOS PORCENTAJES DE FECHA DE CREACION SON LOS SIGUIENTES:  \n")
print("\n")
print("            -    EN EL  "+str(float((((count_created_date_2023_alienvault_iot_pattern_emailmessage+count_created_date_2023_alienvault_sh_pattern_emailmessage)*100)/(count_alienvault_iot_pattern_emailmessage+count_alienvault_sh_pattern_emailmessage))))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2023 ")
print("            -    EN EL  "+str(float((((count_created_date_2022_alienvault_iot_pattern_emailmessage+count_created_date_2022_alienvault_sh_pattern_emailmessage)*100)/(count_alienvault_iot_pattern_emailmessage+count_alienvault_sh_pattern_emailmessage))))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2022")
print("            -    EN EL  "+str(float((((count_created_date_2021_alienvault_iot_pattern_emailmessage+count_created_date_2021_alienvault_sh_pattern_emailmessage)*100)/(count_alienvault_iot_pattern_emailmessage+count_alienvault_sh_pattern_emailmessage))))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2021 ")
print("            -    EN EL  "+str(float((((count_created_date_2020_alienvault_iot_pattern_emailmessage+count_created_date_2020_alienvault_sh_pattern_emailmessage)*100)/(count_alienvault_iot_pattern_emailmessage+count_alienvault_sh_pattern_emailmessage))))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2020 ")
print("            -    EN EL  "+str(float((((count_created_date_2019_alienvault_iot_pattern_emailmessage+count_created_date_2019_alienvault_sh_pattern_emailmessage)*100)/(count_alienvault_iot_pattern_emailmessage+count_alienvault_sh_pattern_emailmessage))))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2019")
print("            -    EN EL  "+str(float((((count_created_date_2018_alienvault_iot_pattern_emailmessage+count_created_date_2018_alienvault_sh_pattern_emailmessage)*100)/(count_alienvault_iot_pattern_emailmessage+count_alienvault_sh_pattern_emailmessage))))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2018 O ANTERIOR ")
print("\n")
print("      -    EN EL  "+str(float((((count_alienvault_iot_pattern_ipv4addr+count_alienvault_sh_pattern_ipv4addr)*100)/(count_alienvault_sh_totalpulses+count_alienvault_iot_totalpulses))))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT EL PATRÓN ES UNA DIRECCIÓN IPV4ESS. LOS PORCENTAJES DE FECHA DE CREACION SON LOS SIGUIENTES:  \n")
print("\n")
print("            -    EN EL  "+str(float((((count_created_date_2023_alienvault_iot_pattern_ipv4addr+count_created_date_2023_alienvault_sh_pattern_ipv4addr)*100)/(count_alienvault_iot_pattern_ipv4addr+count_alienvault_sh_pattern_ipv4addr))))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2023 ")
print("            -    EN EL  "+str(float((((count_created_date_2022_alienvault_iot_pattern_ipv4addr+count_created_date_2022_alienvault_sh_pattern_ipv4addr)*100)/(count_alienvault_iot_pattern_ipv4addr+count_alienvault_sh_pattern_ipv4addr))))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2022")
print("            -    EN EL  "+str(float((((count_created_date_2021_alienvault_iot_pattern_ipv4addr+count_created_date_2021_alienvault_sh_pattern_ipv4addr)*100)/(count_alienvault_iot_pattern_ipv4addr+count_alienvault_sh_pattern_ipv4addr))))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2021 ")
print("            -    EN EL  "+str(float((((count_created_date_2020_alienvault_iot_pattern_ipv4addr+count_created_date_2020_alienvault_sh_pattern_ipv4addr)*100)/(count_alienvault_iot_pattern_ipv4addr+count_alienvault_sh_pattern_ipv4addr))))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2020 ")
print("            -    EN EL  "+str(float((((count_created_date_2019_alienvault_iot_pattern_ipv4addr+count_created_date_2019_alienvault_sh_pattern_ipv4addr)*100)/(count_alienvault_iot_pattern_ipv4addr+count_alienvault_sh_pattern_ipv4addr))))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2019")
print("            -    EN EL  "+str(float((((count_created_date_2018_alienvault_iot_pattern_ipv4addr+count_created_date_2018_alienvault_sh_pattern_ipv4addr)*100)/(count_alienvault_iot_pattern_ipv4addr+count_alienvault_sh_pattern_ipv4addr))))+" % DE OBJETOS DE TIPO INDICADOR DE PULSOS ALIENVAULT LA FECHA DE CREACION ES 2018 O ANTERIOR ")
print("\n")






















































