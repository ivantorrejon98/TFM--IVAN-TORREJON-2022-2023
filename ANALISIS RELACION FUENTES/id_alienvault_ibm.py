

import pandas as pd

#Abrimos los ficheros con los que se trabajara
df_ali_iot=pd.read_excel('alienvault_iot_2023.xlsx')
df_vuln_ibm_iot=pd.read_excel('vulnerabilidades_ibm_iot_2023.xlsx')
df_malw_ana_ibm_iot=pd.read_excel('ibm_analisis_maliciosos_iot_2023_v2.xlsx')
df_gru_ame_ibm_iot=pd.read_excel('ibm_grupo_amenazas_2023.xlsx')
df_ibm_sector=pd.read_excel('ibm_sector_v2.xlsx')
df_th_act_rep_ibm_iot=pd.read_excel('ibm_threat_activity_report_iot_2023_v2.xlsx')


#Vector para guardar los IDS de Alienvault para iot
ids_alienvault_iot=[]

#Vector para guardar los IDS de IBM para iot
ids_ibm_iot=[]

#Vector para guardar los ids de IBM y los IDS de Alienvault coincidentes
elementos_coincidentes_id_iot=[]

#Inserto un separador para cada fichero de IBM IOT
ids_ibm_iot.append("VULNERABILIDADES_IBM_IOT")
ids_ibm_iot.append("************************")

#Recorro la columna ID del fichero de vulnerabilidades IBM para IOT
for h in range(0,len(df_vuln_ibm_iot["id"])):
    #Compruebo si la fila correspondiente de la columna ID tiene valor
    if(df_vuln_ibm_iot["id"][h] !='NONE'):
        #Compruebo si hay mas de un elemento en la fila o no
        if(',' in df_vuln_ibm_iot["id"][h]):
            #Obtengo los distintos valores de id que existen en la fila y los guardo en un vector
            ids_vuln_ibm_filas = df_vuln_ibm_iot["id"][h].split(',')
            #Recorro el vector obtenido de los id que existen en la fila actual
            for j in range(0,len(ids_vuln_ibm_filas)):
                #Inserto los valores de ID de la correspondiente fila en el vector de IDS en caso de que no sean NONE
                if((ids_vuln_ibm_filas[j].replace('[','').replace(']','').replace("'","").replace("","").replace(" ",""))!='NONE'):
                    ids_ibm_iot.append(ids_vuln_ibm_filas[j].replace('[','').replace(']','').replace("'","").replace("","").replace(" ",""))
        #Si hay un unico ID en la fila , lo inserto en el vector de IDS 
        else:
            ids_ibm_iot.append(df_vuln_ibm_iot["id"][h].replace('[','').replace(']','').replace("'","").replace("",""))

#Inserto un separador para cada fichero de IBM IOT
ids_ibm_iot.append("IBM_ANALISIS_MALICIOSOS_IOT")
ids_ibm_iot.append("************************")

#Recorro la columna ID del fichero de analisis malicios IBM para IOT
for q in range(0,len(df_malw_ana_ibm_iot["id"])):
    #Compruebo si la fila correspondiente de la columna ID tiene valor
    if(df_malw_ana_ibm_iot["id"][q] !='NONE'):
        #Compruebo si hay mas de un elemento en la fila o no
        if(',' in df_malw_ana_ibm_iot["id"][q]):
            #Obtengo los distintos valores de id que existen en la fila y los guardo en un vector
            ids_mal_ana_ibm_filas = df_malw_ana_ibm_iot["id"][q].split(',')
            #Recorro el vector obtenido de los id que existen en la fila actual
            for j in range(0,len(ids_mal_ana_ibm_filas)):
                #Inserto los valores de ID de la correspondiente fila en el vector de IDS en caso de que no sean NONE
                if((ids_mal_ana_ibm_filas[j].replace('[','').replace(']','').replace("'","").replace("","").replace(" ",""))!='NONE'):
                    ids_ibm_iot.append(ids_mal_ana_ibm_filas[j].replace('[','').replace(']','').replace("'","").replace("","").replace(" ",""))
        else:
            #Si hay un unico ID en la fila , lo inserto en el vector de IDS 
            ids_ibm_iot.append(df_malw_ana_ibm_iot["id"][q].replace('[','').replace(']','').replace("'","").replace("",""))
            

#Inserto un separador para cada fichero de IBM IOT            
ids_ibm_iot.append("IBM_GRUPO_AMENAZAS")
ids_ibm_iot.append("************************")

#Recorro la columna ID del fichero de grupo de amenazas IBM para IOT
for e in range(0,len(df_gru_ame_ibm_iot["id"])):
    #Compruebo si la fila correspondiente de la columna ID tiene valor
    if(df_gru_ame_ibm_iot["id"][e] !='NONE'):
        #Compruebo si hay mas de un elemento en la fila o no
        if(',' in df_gru_ame_ibm_iot["id"][e]):
            #Obtengo los distintos valores de id que existen en la fila y los guardo en un vector
            ids_gru_ame_ibm_filas = df_gru_ame_ibm_iot["id"][e].split(',')
            #Recorro el vector obtenido de los id que existen en la fila actual
            for j in range(0,len(ids_gru_ame_ibm_filas)):
                #Inserto los valores de ID de la correspondiente fila en el vector de IDS en caso de que no sean NONE
                if((ids_gru_ame_ibm_filas[j].replace('[','').replace(']','').replace("'","").replace("","").replace(" ",""))!='NONE'):
                    ids_ibm_iot.append(ids_gru_ame_ibm_filas[j].replace('[','').replace(']','').replace("'","").replace("","").replace(" ",""))
        else:
            #Si hay un unico ID en la fila , lo inserto en el vector de IDS
            ids_ibm_iot.append(df_gru_ame_ibm_iot["id"][e].replace('[','').replace(']','').replace("'","").replace("",""))
        

#Inserto un separador para cada fichero de IBM IOT          
ids_ibm_iot.append("IBM_SECTOR")
ids_ibm_iot.append("************************")

#Recorro la columna ID del fichero de sector IBM para IOT
for r in range(0,len(df_ibm_sector["id"])):
    #Compruebo si la fila correspondiente de la columna ID tiene valor
    if(df_ibm_sector["id"][r] !='NONE'):
        #Compruebo si hay mas de un elemento en la fila o no
        if(',' in df_ibm_sector["id"][r]):
            #Obtengo los distintos valores de id que existen en la fila y los guardo en un vector
            ids_sector_ibm_filas = df_ibm_sector["id"][r].split(',')
            #Recorro el vector obtenido de los id que existen en la fila actual
            for j in range(0,len(ids_sector_ibm_filas)):
                #Inserto los valores de ID de la correspondiente fila en el vector de IDS en caso de que no sean NONE
                if((ids_sector_ibm_filas[j].replace('[','').replace(']','').replace("'","").replace("","").replace(" ",""))!='NONE'):
                    ids_ibm_iot.append(ids_sector_ibm_filas[j].replace('[','').replace(']','').replace("'","").replace("","").replace(" ",""))
        else:
            #Si hay un unico ID en la fila , lo inserto en el vector de IDS
            ids_ibm_iot.append(df_ibm_sector["id"][r].replace('[','').replace(']','').replace("'","").replace("",""))
        

#Inserto un separador para cada fichero de THREAT ACTIVITY REPORT IOT         
ids_ibm_iot.append("IBM_THREAT_ACTIVITY_REPORT")
ids_ibm_iot.append("************************")
#Recorro la columna ID del fichero de threat activity report IBM para IOT
for t in range(0,len(df_th_act_rep_ibm_iot["id"])):
    #Compruebo si la fila correspondiente de la columna ID tiene valor
    if(df_th_act_rep_ibm_iot["id"][t] !='NONE'):
        #Compruebo si hay mas de un elemento en la fila o no
        if(',' in df_th_act_rep_ibm_iot["id"][t]):
            #Obtengo los distintos valores de id que existen en la fila y los guardo en un vector
            ids_th_act_rep_ibm_filas = df_th_act_rep_ibm_iot["id"][t].split(',')
            #Recorro el vector obtenido de los id que existen en la fila actual
            for j in range(0,len(ids_th_act_rep_ibm_filas)):
                #Inserto los valores de ID de la correspondiente fila en el vector de IDS en caso de que no sean NONE
                if((ids_th_act_rep_ibm_filas[j].replace('[','').replace(']','').replace("'","").replace("","").replace(" ",""))!='NONE'):
                    ids_ibm_iot.append(ids_th_act_rep_ibm_filas[j].replace('[','').replace(']','').replace("'","").replace("","").replace(" ",""))
        else:
            #Si hay un unico ID en la fila , lo inserto en el vector de IDS
            ids_ibm_iot.append(df_th_act_rep_ibm_iot["id"][t].replace('[','').replace(']','').replace("'","").replace("",""))
        

#Recorro la columna de IDs para ALIENVAULT IOT
for k in range(0,len(df_ali_iot["id"])):
    #Compruebo si la fila correspondiente de la columna ID tiene valor
    if(df_ali_iot["id"][k] !='NONE'):
        #Compruebo si hay mas de un elemento en la fila o no
        if(',' in df_ali_iot["id"][k]):
            #Obtengo los distintos valores de IDS que existen en la fila y los guardo en un vector
            ids_ali_iot = df_ali_iot["id"][k].split(',')
            #Recorro el vector obtenido de los IDS que existen en la fila actual
            for j in range(0,len(ids_ali_iot)):
                #Inserto los valores de IDS de la correspondiente fila en el vector de IDS en caso de que no sean NONE
                if((ids_ali_iot[j].replace('[','').replace(']','').replace("'","").replace("","").replace(" ",""))!='NONE'):
                    ids_alienvault_iot.append(ids_ali_iot[j].replace('[','').replace(']','').replace("'","").replace("","").replace(" ",""))
        else:
            #Si hay una unica referencia de objeto en la fila , lo inserto en el vector de referencias de objetos
            ids_alienvault_iot.append(df_ali_iot["id"][k].replace('[','').replace(']','').replace("'","").replace("",""))
            
#Compruebo si existen referencias de objetos de ALIENVAULT e ids de IBM coincidentes  
for elem_refs in ids_alienvault_iot:
    if elem_refs in ids_ibm_iot:
        elementos_coincidentes_id_iot.append(elem_refs)

#Imprimo los resultados         
if(len(elementos_coincidentes_id_iot)==0):
    print("NO HAY IDS DE ALIENVAULT E IBM COINCIDENTES PARA LA RAMA IOT")
else:
    print("IDS DE ALIENVAULT E IBM COINCIDENTES PARA LA RAMA IOT:")
    print("\n")
    for g in range(0,len(elementos_coincidentes_id_iot)):
        print(elementos_coincidentes_id_iot[g])
        print("\n")


        
        
        

#Abrimos los ficheros con los que se trabajara
df_ali_sh=pd.read_excel('alienvault_smart_home_2023.xlsx')
df_vuln_ibm_sh=pd.read_excel('vulnerabilidades_ibm_smart_home_2023.xlsx')
df_malw_ana_ibm_sh=pd.read_excel('ibm_analisis_maliciosos_smarthome_2023.xlsx')
df_gru_ame_ibm_sh=pd.read_excel('ibm_grupo_amenazas_2023.xlsx')
df_ibm_sector=pd.read_excel('ibm_sector_v2.xlsx')
df_th_act_rep_ibm_sh=pd.read_excel('ibm_threat_activity_report_smarthome_2023_v2.xlsx')


#Vector para guardar los IDS de Alienvault para SMART HOME
ids_alienvault_sh=[]

#Vector para guardar los IDS de IBM para SMART HOME
ids_ibm_sh=[]

#Vector para guardar los ids de IBM y los IDS de Alienvault coincidentes
elementos_coincidentes_id_sh=[]

#Inserto un separador para cada fichero de IBM SMART HOME
ids_ibm_sh.append("VULNERABILIDADES_IBM_sh")
ids_ibm_sh.append("************************")

#Recorro la columna ID del fichero de vulnerabilidades IBM para SMART HOME
for h in range(0,len(df_vuln_ibm_sh["id"])):
    #Compruebo si la fila correspondiente de la columna ID tiene valor
    if(df_vuln_ibm_sh["id"][h] !='NONE'):
        #Compruebo si hay mas de un elemento en la fila o no
        if(',' in df_vuln_ibm_sh["id"][h]):
            #Obtengo los distintos valores de id que existen en la fila y los guardo en un vector
            ids_vuln_ibm_filas = df_vuln_ibm_sh["id"][h].split(',')
            #Recorro el vector obtenido de los id que existen en la fila actual
            for j in range(0,len(ids_vuln_ibm_filas)):
                #Inserto los valores de ID de la correspondiente fila en el vector de IDS en caso de que no sean NONE
                if((ids_vuln_ibm_filas[j].replace('[','').replace(']','').replace("'","").replace("","").replace(" ",""))!='NONE'):
                    ids_ibm_sh.append(ids_vuln_ibm_filas[j].replace('[','').replace(']','').replace("'","").replace("","").replace(" ",""))
        #Si hay un unico ID en la fila , lo inserto en el vector de IDS 
        else:
            ids_ibm_sh.append(df_vuln_ibm_sh["id"][h].replace('[','').replace(']','').replace("'","").replace("",""))

#Inserto un separador para cada fichero de IBM SMART HOME
ids_ibm_sh.append("IBM_ANALISIS_MALICIOSOS_sh")
ids_ibm_sh.append("************************")

#Recorro la columna ID del fichero de analisis malicios IBM para SMART HOME
for q in range(0,len(df_malw_ana_ibm_sh["id"])):
    #Compruebo si la fila correspondiente de la columna ID tiene valor
    if(df_malw_ana_ibm_sh["id"][q] !='NONE'):
        #Compruebo si hay mas de un elemento en la fila o no
        if(',' in df_malw_ana_ibm_sh["id"][q]):
            #Obtengo los distintos valores de id que existen en la fila y los guardo en un vector
            ids_mal_ana_ibm_filas = df_malw_ana_ibm_sh["id"][q].split(',')
            #Recorro el vector obtenido de los id que existen en la fila actual
            for j in range(0,len(ids_mal_ana_ibm_filas)):
                #Inserto los valores de ID de la correspondiente fila en el vector de IDS en caso de que no sean NONE
                if((ids_mal_ana_ibm_filas[j].replace('[','').replace(']','').replace("'","").replace("","").replace(" ",""))!='NONE'):
                    ids_ibm_sh.append(ids_mal_ana_ibm_filas[j].replace('[','').replace(']','').replace("'","").replace("","").replace(" ",""))
        else:
            #Si hay un unico ID en la fila , lo inserto en el vector de IDS 
            ids_ibm_sh.append(df_malw_ana_ibm_sh["id"][q].replace('[','').replace(']','').replace("'","").replace("",""))
            

#Inserto un separador para cada fichero de IBM SMART HOME            
ids_ibm_sh.append("IBM_GRUPO_AMENAZAS")
ids_ibm_sh.append("************************")

#Recorro la columna ID del fichero de grupo de amenazas IBM para SMART HOME
for e in range(0,len(df_gru_ame_ibm_sh["id"])):
    #Compruebo si la fila correspondiente de la columna ID tiene valor
    if(df_gru_ame_ibm_sh["id"][e] !='NONE'):
        #Compruebo si hay mas de un elemento en la fila o no
        if(',' in df_gru_ame_ibm_sh["id"][e]):
            #Obtengo los distintos valores de id que existen en la fila y los guardo en un vector
            ids_gru_ame_ibm_filas = df_gru_ame_ibm_sh["id"][e].split(',')
            #Recorro el vector obtenido de los id que existen en la fila actual
            for j in range(0,len(ids_gru_ame_ibm_filas)):
                #Inserto los valores de ID de la correspondiente fila en el vector de IDS en caso de que no sean NONE
                if((ids_gru_ame_ibm_filas[j].replace('[','').replace(']','').replace("'","").replace("","").replace(" ",""))!='NONE'):
                    ids_ibm_sh.append(ids_gru_ame_ibm_filas[j].replace('[','').replace(']','').replace("'","").replace("","").replace(" ",""))
        else:
            #Si hay un unico ID en la fila , lo inserto en el vector de IDS
            ids_ibm_sh.append(df_gru_ame_ibm_sh["id"][e].replace('[','').replace(']','').replace("'","").replace("",""))
        

#Inserto un separador para cada fichero de IBM SMART HOME          
ids_ibm_sh.append("IBM_SECTOR")
ids_ibm_sh.append("************************")

#Recorro la columna ID del fichero de sector IBM para SMART HOME
for r in range(0,len(df_ibm_sector["id"])):
    #Compruebo si la fila correspondiente de la columna ID tiene valor
    if(df_ibm_sector["id"][r] !='NONE'):
        #Compruebo si hay mas de un elemento en la fila o no
        if(',' in df_ibm_sector["id"][r]):
            #Obtengo los distintos valores de id que existen en la fila y los guardo en un vector
            ids_sector_ibm_filas = df_ibm_sector["id"][r].split(',')
            #Recorro el vector obtenido de los id que existen en la fila actual
            for j in range(0,len(ids_sector_ibm_filas)):
                #Inserto los valores de ID de la correspondiente fila en el vector de IDS en caso de que no sean NONE
                if((ids_sector_ibm_filas[j].replace('[','').replace(']','').replace("'","").replace("","").replace(" ",""))!='NONE'):
                    ids_ibm_sh.append(ids_sector_ibm_filas[j].replace('[','').replace(']','').replace("'","").replace("","").replace(" ",""))
        else:
            #Si hay un unico ID en la fila , lo inserto en el vector de IDS
            ids_ibm_sh.append(df_ibm_sector["id"][r].replace('[','').replace(']','').replace("'","").replace("",""))
        

#Inserto un separador para cada fichero de THREAT ACTIVITY REPORT SMART HOME         
ids_ibm_sh.append("IBM_THREAT_ACTIVITY_REPORT")
ids_ibm_sh.append("************************")
#Recorro la columna ID del fichero de threat activity report IBM para SMART HOME
for t in range(0,len(df_th_act_rep_ibm_sh["id"])):
    #Compruebo si la fila correspondiente de la columna ID tiene valor
    if(df_th_act_rep_ibm_sh["id"][t] !='NONE'):
        #Compruebo si hay mas de un elemento en la fila o no
        if(',' in df_th_act_rep_ibm_sh["id"][t]):
            #Obtengo los distintos valores de id que existen en la fila y los guardo en un vector
            ids_th_act_rep_ibm_filas = df_th_act_rep_ibm_sh["id"][t].split(',')
            #Recorro el vector obtenido de los id que existen en la fila actual
            for j in range(0,len(ids_th_act_rep_ibm_filas)):
                #Inserto los valores de ID de la correspondiente fila en el vector de IDS en caso de que no sean NONE
                if((ids_th_act_rep_ibm_filas[j].replace('[','').replace(']','').replace("'","").replace("","").replace(" ",""))!='NONE'):
                    ids_ibm_sh.append(ids_th_act_rep_ibm_filas[j].replace('[','').replace(']','').replace("'","").replace("","").replace(" ",""))
        else:
            #Si hay un unico ID en la fila , lo inserto en el vector de IDS
            ids_ibm_sh.append(df_th_act_rep_ibm_sh["id"][t].replace('[','').replace(']','').replace("'","").replace("",""))
        

#Recorro la columna de IDs para ALIENVAULT SMART HOME
for k in range(0,len(df_ali_sh["id"])):
    #Compruebo si la fila correspondiente de la columna ID tiene valor
    if(df_ali_sh["id"][k] !='NONE'):
        #Compruebo si hay mas de un elemento en la fila o no
        if(',' in df_ali_sh["id"][k]):
            #Obtengo los distintos valores de IDS que existen en la fila y los guardo en un vector
            ids_ali_sh = df_ali_sh["id"][k].split(',')
            #Recorro el vector obtenido de los IDS que existen en la fila actual
            for j in range(0,len(ids_ali_sh)):
                #Inserto los valores de IDS de la correspondiente fila en el vector de IDS en caso de que no sean NONE
                if((ids_ali_sh[j].replace('[','').replace(']','').replace("'","").replace("","").replace(" ",""))!='NONE'):
                    ids_alienvault_sh.append(ids_ali_sh[j].replace('[','').replace(']','').replace("'","").replace("","").replace(" ",""))
        else:
            #Si hay una unica referencia de objeto en la fila , lo inserto en el vector de referencias de objetos
            ids_alienvault_sh.append(df_ali_sh["id"][k].replace('[','').replace(']','').replace("'","").replace("",""))
            
#Compruebo si existen referencias de objetos de ALIENVAULT e ids de IBM coincidentes 
for elem_refs in ids_alienvault_sh:
    if elem_refs in ids_ibm_sh:
        elementos_coincidentes_id_sh.append(elem_refs)

#Imprimo los resultados         
if(len(elementos_coincidentes_id_sh)==0):
    print("NO HAY IDS DE ALIENVAULT E IBM COINCIDENTES PARA LA RAMA SMART HOME")
else:
    print("IDS DE ALIENVAULT E IBM COINCIDENTES PARA LA RAMA SMART HOME:")
    print("\n")
    for g in range(0,len(elementos_coincidentes_id_sh)):
        print(elementos_coincidentes_id_sh[g])
        print("\n")



#Compruebo si hay elementos coincidentes entre las partes IOT Y SMART HOME

#Vector donde guardare los elementos coincidentes de ambas partes en Alienvault
ids_alienvault=[]
#Vector donde guardare los elementos coincidentes de ambas partes en IBM
ids_ibm=[]
#Vector donde guardare los elementos coincidentes de ALIENVAULT Y SMART HOME
elementos_coincidentes_id=[]

#Inserto los elementos de IOT y SMART HOME de las partes de IOT Y ALIENVAULT en el vector correspondiente
for elem_refs in ids_alienvault_iot:
    ids_alienvault.append(elem_refs)

for elem_refs_sh in ids_alienvault_sh:
    ids_alienvault.append(elem_refs_sh)


for elem_refsibm in ids_ibm_iot:
    ids_ibm.append(elem_refsibm)

for elem_refsibm_sh in ids_ibm_sh:
    ids_ibm.append(elem_refsibm_sh)


#Busco los elementos coincidentes
for elem_refss in ids_alienvault:
    if elem_refss in ids_ibm:
        elementos_coincidentes_id.append(elem_refss)

#Imprimo los resultados         
if(len(elementos_coincidentes_id)==0):
    print("NO HAY IDS DE ALIENVAULT E IBM COINCIDENTES")
else:
    print("IDS DE ALIENVAULT E IBM COINCIDENTES :")
    print("\n")
    for g in range(0,len(elementos_coincidentes_id)):
        print(elementos_coincidentes_id[g])
        print("\n")



































