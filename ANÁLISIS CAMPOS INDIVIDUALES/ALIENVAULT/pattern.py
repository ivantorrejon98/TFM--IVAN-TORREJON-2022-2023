

import pandas as pd
from datetime import datetime

#Abro los ficheros con los que voy a tratar


df_alienvault_iot = pd.read_excel('alienvault_iot_2023.xlsx')




#Variables donde almacenare el contador de tipo patron de Alienvault IOT
count_pattern_domain_alienvault_iot=0
count_pattern_url_alienvault_iot=0
count_pattern_hashes_alienvault_iot=0
count_pattern_email_alienvault_iot=0
count_pattern_another_alienvault_iot=0
count_pattern_ipv4_alienvault_iot=0
#Variable auxiliar para almacenar el total de patrones
len_aux_iot=0


#Comprobamos el tipo de patron
for r in range(0,len(df_alienvault_iot["pattern"])):
    #Compruebo si hay varios patrones en la fila actual
    if('[' in df_alienvault_iot["pattern"][r]):
        aux=df_alienvault_iot["pattern"][r].split(",")
        for l in range(0,len(aux)):
            if(len(aux)>0):
                aux_str=aux[l].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
                if('domain' in aux_str):
                    len_aux_iot+=1
                    count_pattern_domain_alienvault_iot+=1  
                elif('url' in aux_str):
                    len_aux_iot+=1
                    count_pattern_url_alienvault_iot+=1  
                elif('hashes' in aux_str):
                    len_aux_iot+=1
                    count_pattern_hashes_alienvault_iot+=1  
                elif('email' in aux_str):
                    len_aux_iot+=1
                    count_pattern_email_alienvault_iot+=1  
                elif('ipv4' in aux_str):
                    len_aux_iot+=1
                    count_pattern_ipv4_alienvault_iot+=1 
                else:
                    if(aux_str!='NONE'):
                        len_aux_iot+=1
                        count_pattern_another_alienvault_iot+=1
    else:
        #Si existe un unico patron en la fila actual
        if('domain' in df_alienvault_iot["pattern"][r]):
            len_aux_iot+=1
            count_pattern_domain_alienvault_iot+=1  
        elif('url' in df_alienvault_iot["pattern"][r]):
            len_aux_iot+=1
            count_pattern_url_alienvault_iot+=1  
        elif('hashes' in df_alienvault_iot["pattern"][r]):
            len_aux_iot+=1
            count_pattern_hashes_alienvault_iot+=1  
        elif('email' in df_alienvault_iot["pattern"][r]):
            len_aux_iot+=1
            count_pattern_email_alienvault_iot+=1 
        elif('ipv4' in df_alienvault_iot["pattern"][r]):
            len_aux_iot+=1
            count_pattern_ipv4_alienvault_iot+=1 
        else:
            if(df_alienvault_iot["pattern"][r]!='NONE'):
                len_aux_iot+=1
                count_pattern_another_alienvault_iot+=1
        

print("**************************ESTADÍSTICAS TIPO DE PATRON ALIENVAULT IOT ********************************")
print("\n")
print("HAY "+str(count_pattern_domain_alienvault_iot)+" PATRONES DE TIPO DOMINIO \n")
print("HAY "+str(count_pattern_url_alienvault_iot)+" PATRONES DE TIPO URL \n")
print("HAY "+str(count_pattern_hashes_alienvault_iot)+" PATRONES DE TIPO HASH \n")
print("HAY "+str(count_pattern_email_alienvault_iot)+" PATRONES DE TIPO MENSAJE DE EMAIL \n")
print("HAY "+str(count_pattern_ipv4_alienvault_iot)+" PATRONES DE TIPO DIRECCION IPV4 \n")

print("\n")
print("**************************PORCENTAJE TIPO DE PATRON ALIENVAULT IOT ********************************")
print("\n")

print("EL "+str(float((count_pattern_domain_alienvault_iot*100)/(len_aux_iot)))+"% DE LOS PATRONES ES DE TIPO DOMINIO \n")
print("EL "+str(float((count_pattern_url_alienvault_iot*100)/(len_aux_iot)))+"% DE LOS PATRONES ES DE TIPO URL \n")
print("EL "+str(float((count_pattern_hashes_alienvault_iot*100)/(len_aux_iot)))+"% DE LOS PATRONES ES DE TIPO HASH \n")
print("EL "+str(float((count_pattern_email_alienvault_iot*100)/(len_aux_iot)))+"% DE LOS PATRONES ES DE TIPO MENSAJE DE EMAIL \n")
print("EL "+str(float((count_pattern_ipv4_alienvault_iot*100)/(len_aux_iot)))+"% DE LOS PATRONES ES DE TIPO DIRECCION IPV4 \n")

print("\n")





#Abro los ficheros con los que voy a tratar


df_alienvault_sh = pd.read_excel('alienvault_smart_home_2023.xlsx')




#Variables donde almacenare el contador de tipo patron de Alienvault SMART HOME
count_pattern_domain_alienvault_sh=0
count_pattern_url_alienvault_sh=0
count_pattern_hashes_alienvault_sh=0
count_pattern_email_alienvault_sh=0
count_pattern_another_alienvault_sh=0
count_pattern_ipv4_alienvault_sh=0
#Variable auxiliar para almacenar el total de patrones
len_aux_sh=0


#Comprobamos el tipo de patron
for r in range(0,len(df_alienvault_sh["pattern"])):
    #Si existen varios patrones en la fila actual
    if('[' in df_alienvault_sh["pattern"][r]):
        aux=df_alienvault_sh["pattern"][r].split(",")
        for l in range(0,len(aux)):
            if(len(aux)>0):
                aux_str=aux[l].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
                if('domain' in aux_str):
                    len_aux_sh+=1
                    count_pattern_domain_alienvault_sh+=1  
                elif('url' in aux_str):
                    len_aux_sh+=1
                    count_pattern_url_alienvault_sh+=1  
                elif('hashes' in aux_str):
                    len_aux_sh+=1
                    count_pattern_hashes_alienvault_sh+=1  
                elif('email' in aux_str):
                    len_aux_sh+=1
                    count_pattern_email_alienvault_sh+=1  
                elif('ipv4' in aux_str):
                    len_aux_sh+=1
                    count_pattern_ipv4_alienvault_sh+=1 
                else:
                    if(aux_str!='NONE'):
                        len_aux_sh+=1
                        count_pattern_another_alienvault_sh+=1
    else:
        #Si existe un unico patron en la fila actual
        if('domain' in df_alienvault_sh["pattern"][r]):
            len_aux_sh+=1
            count_pattern_domain_alienvault_sh+=1  
        elif('url' in df_alienvault_sh["pattern"][r]):
            len_aux_sh+=1
            count_pattern_url_alienvault_sh+=1  
        elif('hashes' in df_alienvault_sh["pattern"][r]):
            len_aux_sh+=1
            count_pattern_hashes_alienvault_sh+=1  
        elif('email' in df_alienvault_sh["pattern"][r]):
            len_aux_sh+=1
            count_pattern_email_alienvault_sh+=1 
        elif('ipv4' in df_alienvault_sh["pattern"][r]):
            len_aux_sh+=1
            count_pattern_ipv4_alienvault_sh+=1 
        else:
            if(df_alienvault_sh["pattern"][r]!='NONE'):
                len_aux_sh+=1
                count_pattern_another_alienvault_sh+=1
        

print("**************************ESTADÍSTICAS TIPO DE PATRON ALIENVAULT SMART HOME ********************************")
print("\n")
print("HAY "+str(count_pattern_domain_alienvault_sh)+" PATRONES DE TIPO DOMINIO \n")
print("HAY "+str(count_pattern_url_alienvault_sh)+" PATRONES DE TIPO URL \n")
print("HAY "+str(count_pattern_hashes_alienvault_sh)+" PATRONES DE TIPO HASH \n")
print("HAY "+str(count_pattern_email_alienvault_sh)+" PATRONES DE TIPO MENSAJE DE EMAIL \n")
print("HAY "+str(count_pattern_ipv4_alienvault_sh)+" PATRONES DE TIPO DIRECCION IPV4 \n")


print("\n")
print("**************************PORCENTAJE TIPO DE PATRON ALIENVAULT SMART HOME ********************************")
print("\n")

print("EL "+str(float((count_pattern_domain_alienvault_sh*100)/(len_aux_sh)))+"% DE LOS PATRONES ES DE TIPO DOMINIO \n")
print("EL "+str(float((count_pattern_url_alienvault_sh*100)/(len_aux_sh)))+"% DE LOS PATRONES ES DE TIPO URL \n")
print("EL "+str(float((count_pattern_hashes_alienvault_sh*100)/(len_aux_sh)))+"% DE LOS PATRONES ES DE TIPO HASH \n")
print("EL "+str(float((count_pattern_email_alienvault_sh*100)/(len_aux_sh)))+"% DE LOS PATRONES ES DE TIPO MENSAJE DE EMAIL \n")
print("EL "+str(float((count_pattern_ipv4_alienvault_sh*100)/(len_aux_sh)))+"% DE LOS PATRONES ES DE TIPO DIRECCION IPV4 \n")


print("\n")



print("**************************ESTADÍSTICAS TIPO DE PATRON ALIENVAULT PARTE IOT Y SMART HOME CONJUNTAS********************************")
print("\n")
print("HAY "+str(count_pattern_domain_alienvault_sh+count_pattern_domain_alienvault_iot)+" PATRONES DE TIPO DOMINIO \n")
print("HAY "+str(count_pattern_url_alienvault_sh+count_pattern_url_alienvault_iot)+" PATRONES DE TIPO URL \n")
print("HAY "+str(count_pattern_hashes_alienvault_sh+count_pattern_hashes_alienvault_iot)+" PATRONES DE TIPO HASH \n")
print("HAY "+str(count_pattern_email_alienvault_sh+count_pattern_email_alienvault_iot)+" PATRONES DE TIPO MENSAJE DE EMAIL \n")
print("HAY "+str(count_pattern_ipv4_alienvault_sh+count_pattern_ipv4_alienvault_iot)+" PATRONES DE TIPO DIRECCION IPV4 \n")


print("\n")
print("**************************PORCENTAJE TIPO DE PATRON ALIENVAULT PARTE IOT Y SMART HOME CONJUNTAS********************************")
print("\n")

print("EL "+str(float((((count_pattern_domain_alienvault_sh+count_pattern_domain_alienvault_iot)*100)/(len_aux_iot+len_aux_sh))))+"% DE LOS PATRONES ES DE TIPO DOMINIO \n")
print("EL "+str(float((((count_pattern_url_alienvault_sh+count_pattern_url_alienvault_iot)*100)/(len_aux_iot+len_aux_sh))))+"% DE LOS PATRONES ES DE TIPO URL \n")
print("EL "+str(float((((count_pattern_hashes_alienvault_sh+count_pattern_hashes_alienvault_iot)*100)/(len_aux_iot+len_aux_sh))))+"% DE LOS PATRONES ES DE TIPO HASH \n")
print("EL "+str(float((((count_pattern_email_alienvault_sh+count_pattern_email_alienvault_iot)*100)/(len_aux_iot+len_aux_sh))))+"% DE LOS PATRONES ES DE TIPO MENSAJE DE EMAIL \n")
print("EL "+str(float((((count_pattern_ipv4_alienvault_sh+count_pattern_ipv4_alienvault_iot)*100)/(len_aux_iot+len_aux_sh))))+"% DE LOS PATRONES ES DE TIPO DIRECCION IPV4 \n")


print("\n")

