

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

#Vector para guardar las referencias de objetos de IBM para iot
objectrefs_ibm_iot=[]

#Vector para guardar las referencias de objetis de IBM y los  IDS de Alienvault coincidentes
elementos_coincidentes_refs_id_iot=[]


#Inserto un separador para cada fichero de IBM IOT
objectrefs_ibm_iot.append("IBM_ANALISIS_MALICIOSOS_IOT")
objectrefs_ibm_iot.append("************************")

#Recorro la columna object_refs del fichero de analisis malicios IBM para IOT
for q in range(0,len(df_malw_ana_ibm_iot["object_refs"])):
    #Compruebo si la fila correspondiente de la columna REFERENCIAS DE OBJETOS tiene valor
    if(df_malw_ana_ibm_iot["object_refs"][q] !='NONE'):
        #Compruebo si hay mas de un elemento en la fila o no
        if(',' in df_malw_ana_ibm_iot["object_refs"][q]):
            #Obtengo los distintos valores de object_refs que existen en la fila y los guardo en un vector
            objectrefs_mal_ana_ibm_filas = df_malw_ana_ibm_iot["object_refs"][q].split(',')
            #Recorro el vector obtenido de los object_refs que existen en la fila actual
            for j in range(0,len(objectrefs_mal_ana_ibm_filas)):
                #Inserto los valores de object_ref de la correspondiente fila en el vector de object_refs en caso de que no sean NONE
                if((objectrefs_mal_ana_ibm_filas[j].replace('[','').replace(']','').replace("'","").replace("","").replace(" ",""))!='NONE'):
                    objectrefs_ibm_iot.append(objectrefs_mal_ana_ibm_filas[j].replace('[','').replace(']','').replace("'","").replace("","").replace(" ",""))
        else:
            #Si hay un unico object_ref en la fila , lo inserto en el vector de object_refs 
            objectrefs_ibm_iot.append(df_malw_ana_ibm_iot["object_refs"][q].replace('[','').replace(']','').replace("'","").replace("",""))
            

#Inserto un separador para cada fichero de IBM IOT            
objectrefs_ibm_iot.append("IBM_GRUPO_AMENAZAS")
objectrefs_ibm_iot.append("************************")

#Recorro la columna object_refs del fichero de grupo de amenazas IBM para IOT
for e in range(0,len(df_gru_ame_ibm_iot["object_refs"])):
    #Compruebo si la fila correspondiente de la columna object_refs tiene valor
    if(df_gru_ame_ibm_iot["object_refs"][e] !='NONE'):
        #Compruebo si hay mas de un elemento en la fila o no
        if(',' in df_gru_ame_ibm_iot["object_refs"][e]):
            #Obtengo los distintos valores de object_refs que existen en la fila y los guardo en un vector
            objectrefs_gru_ame_ibm_filas = df_gru_ame_ibm_iot["object_refs"][e].split(',')
            #Recorro el vector obtenido de los object_refs que existen en la fila actual
            for j in range(0,len(objectrefs_gru_ame_ibm_filas)):
                #Inserto los valores de object_ref de la correspondiente fila en el vector de object_refs en caso de que no sean NONE
                if((objectrefs_gru_ame_ibm_filas[j].replace('[','').replace(']','').replace("'","").replace("","").replace(" ",""))!='NONE'):
                    objectrefs_ibm_iot.append(objectrefs_gru_ame_ibm_filas[j].replace('[','').replace(']','').replace("'","").replace("","").replace(" ",""))
        else:
            #Si hay un unico object_ref en la fila , lo inserto en el vector de object_refs
            objectrefs_ibm_iot.append(df_gru_ame_ibm_iot["object_refs"][e].replace('[','').replace(']','').replace("'","").replace("",""))
        

#Inserto un separador para cada fichero de IBM IOT          
objectrefs_ibm_iot.append("IBM_SECTOR")
objectrefs_ibm_iot.append("************************")

#Recorro la columna object_refs del fichero de sector IBM para IOT
for r in range(0,len(df_ibm_sector["object_refs"])):
    #Compruebo si la fila correspondiente de la columna object_refs tiene valor
    if(df_ibm_sector["object_refs"][r] !='NONE'):
        #Compruebo si hay mas de un elemento en la fila o no
        if(',' in df_ibm_sector["object_refs"][r]):
            #Obtengo los distintos valores de object_refs que existen en la fila y los guardo en un vector
            objectrefs_sector_ibm_filas = df_ibm_sector["object_refs"][r].split(',')
            #Recorro el vector obtenido de los object_refs que existen en la fila actual
            for j in range(0,len(objectrefs_sector_ibm_filas)):
                #Inserto los valores de object_ref de la correspondiente fila en el vector de object_refs en caso de que no sean NONE
                if((objectrefs_sector_ibm_filas[j].replace('[','').replace(']','').replace("'","").replace("","").replace(" ",""))!='NONE'):
                    objectrefs_ibm_iot.append(objectrefs_sector_ibm_filas[j].replace('[','').replace(']','').replace("'","").replace("","").replace(" ",""))
        else:
            #Si hay un unico object_ref en la fila , lo inserto en el vector de object_refs
            objectrefs_ibm_iot.append(df_ibm_sector["object_refs"][r].replace('[','').replace(']','').replace("'","").replace("",""))
        

#Inserto un separador para cada fichero de THREAT ACTIVITY REPORT IOT         
objectrefs_ibm_iot.append("IBM_THREAT_ACTIVITY_REPORT")
objectrefs_ibm_iot.append("************************")
#Recorro la columna object_refs del fichero de threat activity report IBM para IOT
for t in range(0,len(df_th_act_rep_ibm_iot["object_refs"])):
    #Compruebo si la fila correspondiente de la columna object_refs tiene valor
    if(df_th_act_rep_ibm_iot["object_refs"][t] !='NONE'):
        #Compruebo si hay mas de un elemento en la fila o no
        if(',' in df_th_act_rep_ibm_iot["object_refs"][t]):
            #Obtengo los distintos valores de object_refs que existen en la fila y los guardo en un vector
            objectrefs_th_act_rep_ibm_filas = df_th_act_rep_ibm_iot["object_refs"][t].split(',')
            #Recorro el vector obtenido de los object_refs que existen en la fila actual
            for j in range(0,len(objectrefs_th_act_rep_ibm_filas)):
                #Inserto los valores de object_ref de la correspondiente fila en el vector de object_refs en caso de que no sean NONE
                if((objectrefs_th_act_rep_ibm_filas[j].replace('[','').replace(']','').replace("'","").replace("","").replace(" ",""))!='NONE'):
                    objectrefs_ibm_iot.append(objectrefs_th_act_rep_ibm_filas[j].replace('[','').replace(']','').replace("'","").replace("","").replace(" ",""))
        else:
            #Si hay un unico object_ref en la fila , lo inserto en el vector de object_refs
            objectrefs_ibm_iot.append(df_th_act_rep_ibm_iot["object_refs"][t].replace('[','').replace(']','').replace("'","").replace("",""))
        

#Recorro la columna de ID para ALIENVAULT IOT
for k in range(0,len(df_ali_iot["id"])):
    #Compruebo si la fila correspondiente de la columna ID tiene valor
    if(df_ali_iot["id"][k] !='NONE'):
        #Compruebo si hay mas de un elemento en la fila o no
        if(',' in df_ali_iot["id"][k]):
            #Obtengo los distintos valores de IDs que existen en la fila y los guardo en un vector
            id_ali_iot = df_ali_iot["id"][k].split(',')
            #Recorro el vector obtenido de los IDS que existen en la fila actual
            for j in range(0,len(id_ali_iot)):
                #Inserto los valores de ID de la correspondiente fila en el vector de IDS en caso de que no sean NONE
                if((id_ali_iot[j].replace('[','').replace(']','').replace("'","").replace("","").replace(" ",""))!='NONE'):
                    ids_alienvault_iot.append(id_ali_iot[j].replace('[','').replace(']','').replace("'","").replace("","").replace(" ",""))
        else:
            #Si hay un unico ID en la fila , lo inserto en el vector de IDS
            ids_alienvault_iot.append(df_ali_iot["id"][k].replace('[','').replace(']','').replace("'","").replace("",""))
            
#Compruebo si existen referencias de objetos de IBM e ids de ALIENVAULT coincidentes  
for elem_refs in ids_alienvault_iot:
    if elem_refs in objectrefs_ibm_iot:
        elementos_coincidentes_refs_id_iot.append(elem_refs)

#Imprimo los resultados         
if(len(elementos_coincidentes_refs_id_iot)==0):
    print("NO HAY REFERENCIAS DE OBJETOS DE IBM  E IDS DE ALIENVAULT COINCIDENTES PARA LA RAMA IOT")
else:
    print("REFERENCIAS DE OBJETOS DE IBM E IDS DE ALIENVAULT COINCIDENTES PARA LA RAMA IOT:")
    print("\n")
    for g in range(0,len(elementos_coincidentes_refs_id_iot)):
        print(elementos_coincidentes_refs_id_iot[g])
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

#Vector para guardar las referencias de objetos de IBM para SMART HOME
objectrefs_ibm_sh=[]

#Vector para guardar los ids de ALIENVAULT y las referencias de objetos de IBM coincidentes
elementos_coincidentes_refs_id_sh=[]



#Inserto un separador para cada fichero de IBM SMART HOME
objectrefs_ibm_sh.append("IBM_ANALISIS_MALICIOSOS_sh")
objectrefs_ibm_sh.append("************************")

#Recorro la columna object_refs del fichero de analisis malicios IBM para SMART HOME
for q in range(0,len(df_malw_ana_ibm_sh["object_refs"])):
    #Compruebo si la fila correspondiente de la columna object_refs tiene valor
    if(df_malw_ana_ibm_sh["object_refs"][q] !='NONE'):
        #Compruebo si hay mas de un elemento en la fila o no
        if(',' in df_malw_ana_ibm_sh["object_refs"][q]):
            #Obtengo los distintos valores de object_refs que existen en la fila y los guardo en un vector
            objectrefs_mal_ana_ibm_filas = df_malw_ana_ibm_sh["object_refs"][q].split(',')
            #Recorro el vector obtenido de los object_refs que existen en la fila actual
            for j in range(0,len(objectrefs_mal_ana_ibm_filas)):
                #Inserto los valores de object_ref de la correspondiente fila en el vector de object_refs en caso de que no sean NONE
                if((objectrefs_mal_ana_ibm_filas[j].replace('[','').replace(']','').replace("'","").replace("","").replace(" ",""))!='NONE'):
                    objectrefs_ibm_sh.append(objectrefs_mal_ana_ibm_filas[j].replace('[','').replace(']','').replace("'","").replace("","").replace(" ",""))
        else:
            #Si hay un unico object_ref en la fila , lo inserto en el vector de object_refs 
            objectrefs_ibm_sh.append(df_malw_ana_ibm_sh["object_refs"][q].replace('[','').replace(']','').replace("'","").replace("",""))
            

#Inserto un separador para cada fichero de IBM SMART HOME            
objectrefs_ibm_sh.append("IBM_GRUPO_AMENAZAS")
objectrefs_ibm_sh.append("************************")

#Recorro la columna object_refs del fichero de grupo de amenazas IBM para SMART HOME
for e in range(0,len(df_gru_ame_ibm_sh["object_refs"])):
    #Compruebo si la fila correspondiente de la columna object_refs tiene valor
    if(df_gru_ame_ibm_sh["object_refs"][e] !='NONE'):
        #Compruebo si hay mas de un elemento en la fila o no
        if(',' in df_gru_ame_ibm_sh["object_refs"][e]):
            #Obtengo los distintos valores de object_refs que existen en la fila y los guardo en un vector
            objectrefs_gru_ame_ibm_filas = df_gru_ame_ibm_sh["object_refs"][e].split(',')
            #Recorro el vector obtenido de los object_refs que existen en la fila actual
            for j in range(0,len(objectrefs_gru_ame_ibm_filas)):
                #Inserto los valores de object_ref de la correspondiente fila en el vector de object_refs en caso de que no sean NONE
                if((objectrefs_gru_ame_ibm_filas[j].replace('[','').replace(']','').replace("'","").replace("","").replace(" ",""))!='NONE'):
                    objectrefs_ibm_sh.append(objectrefs_gru_ame_ibm_filas[j].replace('[','').replace(']','').replace("'","").replace("","").replace(" ",""))
        else:
            #Si hay un unico object_ref en la fila , lo inserto en el vector de object_refs
            objectrefs_ibm_sh.append(df_gru_ame_ibm_sh["object_refs"][e].replace('[','').replace(']','').replace("'","").replace("",""))
        

#Inserto un separador para cada fichero de IBM SMART HOME          
objectrefs_ibm_sh.append("IBM_SECTOR")
objectrefs_ibm_sh.append("************************")

#Recorro la columna object_refs del fichero de sector IBM para SMART HOME
for r in range(0,len(df_ibm_sector["object_refs"])):
    #Compruebo si la fila correspondiente de la columna object_refs tiene valor
    if(df_ibm_sector["object_refs"][r] !='NONE'):
        #Compruebo si hay mas de un elemento en la fila o no
        if(',' in df_ibm_sector["object_refs"][r]):
            #Obtengo los distintos valores de object_refs que existen en la fila y los guardo en un vector
            objectrefs_sector_ibm_filas = df_ibm_sector["object_refs"][r].split(',')
            #Recorro el vector obtenido de los object_refs que existen en la fila actual
            for j in range(0,len(objectrefs_sector_ibm_filas)):
                #Inserto los valores de object_ref de la correspondiente fila en el vector de object_refs en caso de que no sean NONE
                if((objectrefs_sector_ibm_filas[j].replace('[','').replace(']','').replace("'","").replace("","").replace(" ",""))!='NONE'):
                    objectrefs_ibm_sh.append(objectrefs_sector_ibm_filas[j].replace('[','').replace(']','').replace("'","").replace("","").replace(" ",""))
        else:
            #Si hay un unico object_ref en la fila , lo inserto en el vector de object_refs
            objectrefs_ibm_sh.append(df_ibm_sector["object_refs"][r].replace('[','').replace(']','').replace("'","").replace("",""))
        

#Inserto un separador para cada fichero de THREAT ACTIVITY REPORT SMART HOME         
objectrefs_ibm_sh.append("IBM_THREAT_ACTIVITY_REPORT")
objectrefs_ibm_sh.append("************************")
#Recorro la columna object_refs del fichero de threat activity report IBM para SMART HOME
for t in range(0,len(df_th_act_rep_ibm_sh["object_refs"])):
    #Compruebo si la fila correspondiente de la columna object_refs tiene valor
    if(df_th_act_rep_ibm_sh["object_refs"][t] !='NONE'):
        #Compruebo si hay mas de un elemento en la fila o no
        if(',' in df_th_act_rep_ibm_sh["object_refs"][t]):
            #Obtengo los distintos valores de object_refs que existen en la fila y los guardo en un vector
            objectrefs_th_act_rep_ibm_filas = df_th_act_rep_ibm_sh["object_refs"][t].split(',')
            #Recorro el vector obtenido de los object_refs que existen en la fila actual
            for j in range(0,len(objectrefs_th_act_rep_ibm_filas)):
                #Inserto los valores de object_ref de la correspondiente fila en el vector de object_refs en caso de que no sean NONE
                if((objectrefs_th_act_rep_ibm_filas[j].replace('[','').replace(']','').replace("'","").replace("","").replace(" ",""))!='NONE'):
                    objectrefs_ibm_sh.append(objectrefs_th_act_rep_ibm_filas[j].replace('[','').replace(']','').replace("'","").replace("","").replace(" ",""))
        else:
            #Si hay un unico object_ref en la fila , lo inserto en el vector de object_refs
            objectrefs_ibm_sh.append(df_th_act_rep_ibm_sh["object_refs"][t].replace('[','').replace(']','').replace("'","").replace("",""))
        

#Recorro la columna de IDS para ALIENVAULT SMART HOME
for k in range(0,len(df_ali_sh["id"])):
    #Compruebo si la fila correspondiente de la columna ID tiene valor
    if(df_ali_sh["id"][k] !='NONE'):
        #Compruebo si hay mas de un elemento en la fila o no
        if(',' in df_ali_sh["id"][k]):
            #Obtengo los distintos valores de ID que existen en la fila y los guardo en un vector
            id_ali_sh = df_ali_sh["id"][k].split(',')
            #Recorro el vector obtenido de los IDs que existen en la fila actual
            for j in range(0,len(id_ali_sh)):
                #Inserto los valores de IDs de la correspondiente fila en el vector de IDs en caso de que no sean NONE
                if((id_ali_sh[j].replace('[','').replace(']','').replace("'","").replace("","").replace(" ",""))!='NONE'):
                    ids_alienvault_sh.append(id_ali_sh[j].replace('[','').replace(']','').replace("'","").replace("","").replace(" ",""))
        else:
            #Si hay una unica ID en la fila , lo inserto en el vector de IDs
            ids_alienvault_sh.append(df_ali_sh["id"][k].replace('[','').replace(']','').replace("'","").replace("",""))
            
#Compruebo si existen IDS de ALIENVAULT y object_refs de IBM coincidentes 
for elem_refs in ids_alienvault_sh:
    if elem_refs in objectrefs_ibm_sh:
        elementos_coincidentes_refs_id_sh.append(elem_refs)

#Imprimo los resultados         
if(len(elementos_coincidentes_refs_id_sh)==0):
    print("NO HAY IDS DE ALIENVAULT Y REFERENCIAS DE OBJETOS DE IBM COINCIDENTES PARA LA RAMA SMART HOME")
else:
    print("IDS DE ALIENVAULT Y REFERENCIAS DE OBJETOS DE IBM COINCIDENTES PARA LA RAMA SMART HOME:")
    print("\n")
    for g in range(0,len(elementos_coincidentes_refs_id_sh)):
        print(elementos_coincidentes_refs_id_sh[g])
        print("\n")



















