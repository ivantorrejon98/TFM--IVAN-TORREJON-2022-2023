
import pandas as pd

#Abrimos los ficheros con los que se trabajara
df_vuln_ibm_iot=pd.read_excel('vulnerabilidades_ibm_iot_2023.xlsx')
df_malw_ana_ibm_iot=pd.read_excel('ibm_analisis_maliciosos_iot_2023_v2.xlsx')
df_gru_ame_ibm_iot=pd.read_excel('ibm_grupo_amenazas_2023.xlsx')
df_ibm_sector=pd.read_excel('ibm_sector_v2.xlsx')
df_th_act_rep_ibm_iot=pd.read_excel('ibm_threat_activity_report_iot_2023_v2.xlsx')


#Vector para guardar los IDS de IBM para iot
ids_ibm_iot=[]



#Inserto un separador para cada fichero de IBM IOT
ids_ibm_iot.append("IDS VULNERABILIDADES_IBM_IOT")


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
ids_ibm_iot.append("IDS IBM_ANALISIS_MALICIOSOS_IOT")


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
ids_ibm_iot.append("IDS IBM_GRUPO_AMENAZAS")


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
ids_ibm_iot.append("IDS IBM_SECTOR")


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
ids_ibm_iot.append("IDS IBM_THREAT_ACTIVITY_REPORT")

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
            
            
            
            
            
            
            
            
            
#Vector para guardar las referencias de objetos de IBM para iot
objectrefs_ibm_iot=[]

#Vector para guardar las referencias de objetis de IBM y los  IDS de Alienvault coincidentes
elementos_coincidentes_ids_refs_iot=[]


#Inserto un separador para cada fichero de IBM IOT
objectrefs_ibm_iot.append("OBJETOS DE REFERENCIA IBM_ANALISIS_MALICIOSOS_IOT")


#Recorro la columna object_refs del fichero de analisis malicios IBM para IOT
for q in range(0,len(df_malw_ana_ibm_iot["object_refs"])):
    #Compruebo si la fila correspondiente de la columna OBJETOS DE REFERENCIA tiene valor
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
objectrefs_ibm_iot.append("OBJETOS DE REFERENCIA IBM_GRUPO_AMENAZAS")


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
objectrefs_ibm_iot.append("OBJETOS DE REFERENCIA IBM_SECTOR")


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
objectrefs_ibm_iot.append("OBJETOS DE REFERENCIA IBM_THREAT_ACTIVITY_REPORT")

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
        

print("\n")
#Compruebo si existen referencias de objetos de IBM y ALIENVAULT coincidentes  
for elem_refs in ids_ibm_iot:
    if (elem_refs in objectrefs_ibm_iot) and (elem_refs not in elementos_coincidentes_ids_refs_iot):
        elementos_coincidentes_ids_refs_iot.append(elem_refs)

#Imprimo los resultados         
if(len(elementos_coincidentes_ids_refs_iot)==0):
    print("NO HAY OBJETOS DE REFERENCIA E IDS DE IBM COINCIDENTES PARA LA RAMA IOT")
else:
    print("EXISTEN "+str(len(elementos_coincidentes_ids_refs_iot))+" OBJETOS DE REFERENCIA E IDS DE IBM COINCIDENTES PARA LA RAMA IOT:")
    print("\n")
    for g in range(0,len(elementos_coincidentes_ids_refs_iot)):
        print("  -  "+elementos_coincidentes_ids_refs_iot[g])
        print("\n")
        


#Abrimos los ficheros con los que se trabajara
df_vuln_ibm_sh=pd.read_excel('vulnerabilidades_ibm_smart_home_2023.xlsx')
df_malw_ana_ibm_sh=pd.read_excel('ibm_analisis_maliciosos_smarthome_2023.xlsx')
df_gru_ame_ibm_sh=pd.read_excel('ibm_grupo_amenazas_2023.xlsx')
df_ibm_sector=pd.read_excel('ibm_sector_v2.xlsx')
df_th_act_rep_ibm_sh=pd.read_excel('ibm_threat_activity_report_smarthome_2023_v2.xlsx')


#Vector para guardar los IDS de IBM para SMART HOME
ids_ibm_sh=[]



#Inserto un separador para cada fichero de IBM SMART HOME
ids_ibm_sh.append("IDS VULNERABILIDADES_IBM_sh")


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
ids_ibm_sh.append("IDS IBM_ANALISIS_MALICIOSOS_sh")


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
ids_ibm_sh.append("IDS IBM_GRUPO_AMENAZAS")


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
ids_ibm_sh.append("IDS IBM_SECTOR")


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
ids_ibm_sh.append("IDS IBM_THREAT_ACTIVITY_REPORT")

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
            
            
            
            
            
            
            
            
            
#Vector para guardar las referencias de objetos de IBM para SMART HOME
objectrefs_ibm_sh=[]

#Vector para guardar las referencias de objetis de IBM y los  IDS de Alienvault coincidentes
elementos_coincidentes_ids_refs_sh=[]


#Inserto un separador para cada fichero de IBM SMART HOME
objectrefs_ibm_sh.append("OBJETOS DE REFERENCIA IBM_ANALISIS_MALICIOSOS_sh")


#Recorro la columna object_refs del fichero de analisis malicios IBM para SMART HOME
for q in range(0,len(df_malw_ana_ibm_sh["object_refs"])):
    #Compruebo si la fila correspondiente de la columna OBJETOS DE REFERENCIA tiene valor
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
objectrefs_ibm_sh.append("OBJETOS DE REFERENCIA IBM_GRUPO_AMENAZAS")


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
objectrefs_ibm_sh.append("OBJETOS DE REFERENCIA IBM_SECTOR")


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
objectrefs_ibm_sh.append("OBJETOS DE REFERENCIA IBM_THREAT_ACTIVITY_REPORT")

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
        


            
#Compruebo si existen referencias de objetos de IBM y ALIENVAULT coincidentes  
for elem_refs in ids_ibm_sh:
    if (elem_refs in objectrefs_ibm_sh) and (elem_refs not in elementos_coincidentes_ids_refs_sh):
        elementos_coincidentes_ids_refs_sh.append(elem_refs)
print("\n")
print("\n")
print("\n")
#Imprimo los resultados         
if(len(elementos_coincidentes_ids_refs_sh)==0):
    print("NO HAY OBJETOS DE REFERENCIA E IDS DE IBM COINCIDENTES PARA LA RAMA SMART HOME")
else:
    print("EXISTEN "+str(len(elementos_coincidentes_ids_refs_sh))+" OBJETOS DE REFERENCIA E IDS DE IBM COINCIDENTES PARA LA RAMA SMART HOME:")
    print("\n")
    for g in range(0,len(elementos_coincidentes_ids_refs_sh)):
        print("  -  "+elementos_coincidentes_ids_refs_sh[g])
        print("\n")
        

        
#Compruebo si hay elementos coincidentes entre las partes IOT Y SMART HOME

#Vector donde guardare los OBJETOS DE REFERENCIA de ambas partes
objectrefs_ibm=[]
#Vector donde guardare los ids de ambas partes
ids_ibm=[]
#Vector donde guardare los elementos coincidentes de OBJECT REF E IDS
elementos_coincidentes_ibm=[]

#Inserto los elementos de IOT y SMART HOME de las partes de IDS Y OBJETOS DE REFERENCIA en el vector correspondiente
for elem_refs in objectrefs_ibm_iot:
    objectrefs_ibm.append(elem_refs)

for elem_refs_sh in objectrefs_ibm_sh:
    objectrefs_ibm.append(elem_refs_sh)


for elem_refsibm in ids_ibm_iot:
    ids_ibm.append(elem_refsibm)

for elem_refsibm_sh in ids_ibm_sh:
    ids_ibm.append(elem_refsibm_sh)


#Busco los elementos coincidentes
for elem_refss in objectrefs_ibm:
    if elem_refss in ids_ibm:
        elementos_coincidentes_ibm.append(elem_refss)

print("\n")
print("\n")
print("\n")
#Imprimo los resultados         
if(len(elementos_coincidentes_ibm)==0):
    print("NO HAY IDS Y OBJETOS DE REFERENCIA DE  IBM COINCIDENTES")
else:
    print("EXISTEN "+str(len(elementos_coincidentes_ibm))+" OBJETOS DE REFERENCIA E IDS DE IBM COINCIDENTES:")
    print("\n")
    for g in range(0,len(elementos_coincidentes_ibm)):
        print("  -  "+elementos_coincidentes_ibm[g])
        print("\n")

print("\n")
print("\n")
#Averiguo el número existente de los tipos de objetos de referencia coincidentes para IBM
count_indicator=0
count_markingdef=0
for h in range(0,len(elementos_coincidentes_ibm)):
    if("indicator" in elementos_coincidentes_ibm[h]):
        count_indicator+=1
    elif("marking" in elementos_coincidentes_ibm[h]):
        count_markingdef+=1
     else:
        print(elementos_coincidentes_ibm[h])

print("\n")
print("\n")
print("*************************************ESTADÍSTICAS OBJETOS DE REFERENCIA E IDS DE OBJETOS ENCONTRADOS EN IBM COINCIDENTES PARTE IOT Y SMART HOME CONJUNTAS : *************************************")    
print("\n")
print(" - DE UN TOTAL DE "+str(len(elementos_coincidentes_ibm))+" OBJETOS DE REFERENCIA CUYO IDENTIFICADOR VIENE INDICADO EN LAS FUENTES DE DATOS, LAS ESTADÍSTICAS DE TIPO DE OBJETO DE REFERENCIA SON LAS SIGUIENTES :")
print("\n")
print("\n")
print("  -  EXISTEN "+str(count_indicator)+" OBJETOS DE REFERENCIA E IDS DE IBM COINCIDENTES DE TIPO INDICADOR")
print("\n")
print("  -  EXISTEN "+str(count_markingdef)+" OBJETOS DE REFERENCIA E IDS DE IBM COINCIDENTES DE TIPO DEFINICION DE MARCADO")
print("\n")
print("\n")











































