

import pandas as pd
#Abrimos los ficheros que vamos a utilizar
df_cve_iot=pd.read_excel('cves_iot_2023.xlsx')
df_cpe_iot=pd.read_excel('cpes_iot_2023.xlsx')


#Array en el que guardaremos los valores del cpe23Uri del fichero de cpes
cpe23Uris_cpes_children=[]
#Array en el que guardaremos los valores del cpe23Uri de LOS HIJOS DE LOS NODOS DE LA CONFIGURACIÓN DE CVE de los nodos junto al CVE relacionado de su fila
cpesUris_cves_children=[]
#Array en el que guardaremos los valores de los cpe23Uris coincidentes de cpes y childrens de cvs
cpes_children_coincidentes=[]

#Recorremos las diferentes filas de la columna children cpe23Uri en el documento de CVEs
for h in range(0,len(df_cve_iot["CVE_Items.configurations.nodes.children.cpe_match.cpe23Uri"])):
    #Comprobamos si la correspondiente fila tiene valor o no
    if(df_cve_iot["CVE_Items.configurations.nodes.children.cpe_match.cpe23Uri"][h] !='NONE'):
        #Array auxiliar para guardar los diferentes valores de los cpes de cada children, junto con la CVE de esa fila
        cpes_ch_cve=[]
        #Comprobamos si existe mas de un cpe en la fila actual 
        if(',' in df_cve_iot["CVE_Items.configurations.nodes.children.cpe_match.cpe23Uri"][h]):
            #Obtenemos los distintos valores de los cpes si existe mas de uno
            cpes_ch_iot = df_cve_iot["CVE_Items.configurations.nodes.children.cpe_match.cpe23Uri"][h].split(',')
            #Recorremos los distintos childrens que hemos obtenido y los insertamos en un array en caso de que su valor no sea NONE
            for j in range(0,len(cpes_ch_iot)):
                if(cpes_ch_iot[j]!='NONE'):
                    cpes_ch_cve.append(cpes_ch_iot[j].replace('[','').replace(']','').replace("'","").replace("","").replace(" ",""))
        else:
            #Insertamos el unico valor de cpe23uri del unico children de la fila
            cpes_ch_cve.append(df_cve_iot["CVE_Items.configurations.nodes.children.cpe_match.cpe23Uri"][h].replace('[','').replace(']','').replace("'","").replace("","").replace(" ",""))
        #Insertamos el ID de la CVE de la fila correspondiente
        cpes_ch_cve.append(df_cve_iot["CVE_Items.cve.CVE_data_meta.ID"][h])
        #Insertamos los cpes conjuntamente con el CVE de la fila
        cpesUris_cves_children.append(cpes_ch_cve)

#Guardamos todos los cpe23Uri del fichero de cpes en un vector
for l in range(0,len(df_cpe_iot["cpes.cpe23Uri"])):
    if(df_cpe_iot["cpes.cpe23Uri"][l]!="NONE"):
        cpe23Uris_cpes_children.append(df_cpe_iot["cpes.cpe23Uri"][l])

#Compruebo los cpe23Uri que coinciden entre los cpes y LOS HIJOS DE LOS NODOS DE LA CONFIGURACIÓN DE CVES
for k in range(0,len(cpesUris_cves_children)):
    for elem_cpe_ch in cpesUris_cves_children[k]:
        if elem_cpe_ch in cpe23Uris_cpes_children:
            aux_ch=[]
            aux_ch.append(elem_cpe_ch)
            aux_ch.append(cpesUris_cves_children[k][len(cpesUris_cves_children[k])-1])
            cpes_children_coincidentes.append(aux_ch)

#Vector donde guardare los ids de cves que tienen asociados cpes coincidentes
cves=[]
#Array auxiliar para asociar los cves con sus respectivos cpes coincidentes
relacion=[]

#Guardo los cves no guardados anteriormente que tienen cpes coincidentes
for d in range(0,len(cpes_children_coincidentes)):
    if(cpes_children_coincidentes[d][1] not in cves):
        cves.append(cpes_children_coincidentes[d][1])
        
#Guardo los cpes asociados a cada cve que hemos guardado anteriormente
for e in range(0,len(cves)):
    aux=[]
    for t in range(0,len(cpes_children_coincidentes)):
        if (cves[e] == cpes_children_coincidentes[t][1]):
            #Guardo los cpes asociados a cada cve
            aux.append(cpes_children_coincidentes[t][0])
    aux.append(cves[e])
    #Inserto la relacion entre cada cve y sus cpes asociados
    relacion.append(aux)

#Vector para guardar los cpes coincidentes
cpes_coinc=[]
#Imprimo la relacion de cada cve con sus cpes
#print("***************CPES ASOCIADAS CON CVES PARTE IOT*********************")
#for r in range(0,len(relacion)):
    #print("\n")
    #print("La CVE con ID : "'\033[1m'+relacion[r][len(relacion[r])-1]+'\033[0m'" tiene asociadas las siguientes CPES :\n")
    #for f in range(0,len(relacion[r])-1):
        #print("  -  "+str(relacion[r][f])+" \n")
#print("\n")
#print("\n")
#Obtengo los cpes coincidentes no repetidos
for u in range(0,len(relacion)):
    for h in range(0,len(relacion[u])-1):
        if(relacion[u][h] not in cpes_coinc):
            cpes_coinc.append(relacion[u][h])
#Imprimo los cpes coincidentes
#if(len(cpes_coinc)>0):
#    print('\033[1m'+"EXISTEN "+str(len(cpes_coinc))+" CPE23URIS COINCIDENTES ENTRE LOS CPES Y LOS HIJOS DE LOS NODOS DE LA CONFIGURACIÓN DE CVES PARA IOT: \n"+'\033[0m')
#    for g in range(0,len(cpes_coinc)):
#        print(" - "+cpes_coinc[g])
#        print("\n")
#else:
#    print("NO EXISTEN CPE23URIS COINCIDENTES ENTRE LOS CPES Y LOS HIJOS DE LOS NODOS DE LA CONFIGURACIÓN DE CVES PARA IOT")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
#ANALISIS COLUMNAS CPE COINCIDENTES PARTE SMART HOME
  
    
#Abrimos los ficheros que vamos a utilizar
df_cve_sh=pd.read_excel('cves_smart_home_2023.xlsx')
df_cpe_sh=pd.read_excel('cpes_smart_home_2023.xlsx')


#Array en el que guardaremos los valores del cpe23Uri del fichero de cpes
cpe23Uris_cpes_children_sh=[]
#Array en el que guardaremos los valores del cpe23Uri de LOS HIJOS DE LOS NODOS DE LA CONFIGURACIÓN DE CVE de los nodos junto al CVE relacionado de su fila
cpesUris_cves_children_sh=[]
#Array en el que guardaremos los valores de los cpe23Uris coincidentes de cpes y childrens de cvs
cpes_children_coincidentes_sh=[]

#Recorremos las diferentes filas de la columna children cpe23Uri en el documento de CVEs
for h in range(0,len(df_cve_sh["CVE_Items.configurations.nodes.children.cpe_match.cpe23Uri"])):
    #Comprobamos si la correspondiente fila tiene valor o no
    if(df_cve_sh["CVE_Items.configurations.nodes.children.cpe_match.cpe23Uri"][h] !='NONE'):
        #Array auxiliar para guardar los diferentes valores de los cpes de cada children, junto con la CVE de esa fila
        cpes_ch_cve_sh=[]
        #Comprobamos si existe mas de un cpe en la fila actual 
        if(',' in df_cve_sh["CVE_Items.configurations.nodes.children.cpe_match.cpe23Uri"][h]):
            #Obtenemos los distintos valores de los cpes si existe mas de uno
            cpes_ch_sh = df_cve_sh["CVE_Items.configurations.nodes.children.cpe_match.cpe23Uri"][h].split(',')
            #Recorremos los distintos childrens que hemos obtenido y los insertamos en un array en caso de que su valor no sea NONE
            for j in range(0,len(cpes_ch_sh)):
                if(cpes_ch_sh[j]!='NONE'):
                    cpes_ch_cve_sh.append(cpes_ch_sh[j].replace('[','').replace(']','').replace("'","").replace("","").replace(" ",""))
        else:
            #Insertamos el unico valor de cpe23uri del unico children de la fila
            cpes_ch_cve_sh.append(df_cve_sh["CVE_Items.configurations.nodes.children.cpe_match.cpe23Uri"][h].replace('[','').replace(']','').replace("'","").replace("","").replace(" ",""))
        #Insertamos el ID de la CVE de la fila correspondiente
        cpes_ch_cve_sh.append(df_cve_sh["CVE_Items.cve.CVE_data_meta.ID"][h])
        #Insertamos los cpes conjuntamente con el CVE de la fila
        cpesUris_cves_children_sh.append(cpes_ch_cve_sh)

#Guardamos todos los cpe23Uri del fichero de cpes en un vector
for l in range(0,len(df_cpe_sh["cpes.cpe23Uri"])):
    if(df_cpe_sh["cpes.cpe23Uri"][l]!="NONE"):
        cpe23Uris_cpes_children_sh.append(df_cpe_sh["cpes.cpe23Uri"][l])

#Compruebo los cpe23Uri que coinciden entre los cpes y LOS HIJOS DE LOS NODOS DE LA CONFIGURACIÓN DE CVES
for k in range(0,len(cpesUris_cves_children_sh)):
    for elem_cpe_ch in cpesUris_cves_children_sh[k]:
        if elem_cpe_ch in cpe23Uris_cpes_children_sh:
            aux_ch=[]
            aux_ch.append(elem_cpe_ch)
            aux_ch.append(cpesUris_cves_children_sh[k][len(cpesUris_cves_children_sh[k])-1])
            cpes_children_coincidentes_sh.append(aux_ch)

#Vector donde guardare los ids de cves que tienen asociados cpes coincidentes
cves_sh=[]
#Array auxiliar para asociar los cves con sus respectivos cpes coincidentes
relacion_sh=[]

#Guardo los cves no guardados anteriormente que tienen cpes coincidentes
for d in range(0,len(cpes_children_coincidentes_sh)):
    if(cpes_children_coincidentes_sh[d][1] not in cves_sh):
        cves_sh.append(cpes_children_coincidentes_sh[d][1])
        
#Guardo los cpes asociados a cada cve que hemos guardado anteriormente
for e in range(0,len(cves_sh)):
    aux=[]
    for t in range(0,len(cpes_children_coincidentes_sh)):
        if (cves_sh[e] == cpes_children_coincidentes_sh[t][1]):
            #Guardo los cpes asociados a cada cve
            aux.append(cpes_children_coincidentes_sh[t][0])
    aux.append(cves_sh[e])
    #Inserto la relacion entre cada cve y sus cpes asociados
    relacion_sh.append(aux)

#Vector para guardar los cpes coincidentes
cpes_coinc_sh=[]
#Imprimo la relacion de cada cve con sus cpes
#print("***************CPES ASOCIADAS CON CVES PARTE SMART HOME*********************")
#for r in range(0,len(relacion_sh)):
    #print("\n")
    #print("La CVE con ID : "'\033[1m'+relacion_sh[r][len(relacion_sh[r])-1]+'\033[0m'" tiene asociadas las siguientes CPES :\n")
    #for f in range(0,len(relacion_sh[r])-1):
        #print("  -  "+str(relacion_sh[r][f])+" \n")
#print("\n")
#print("\n")
#Obtengo los cpes coincidentes no repetidos
for u in range(0,len(relacion_sh)):
    for h in range(0,len(relacion_sh[u])-1):
        if(relacion_sh[u][h] not in cpes_coinc_sh):
            cpes_coinc_sh.append(relacion_sh[u][h])
#Imprimo los cpes coincidentes
#if(len(cpes_coinc_sh)>0):
#    print('\033[1m'+"EXISTEN "+str(len(cpes_coinc_sh))+" CPE23URIS COINCIDENTES ENTRE LOS CPES Y LOS HIJOS DE LOS NODOS DE LA CONFIGURACIÓN DE CVES PARA SMART HOME: \n"+'\033[0m')
#    for g in range(0,len(cpes_coinc_sh)):
#        print(" - "+cpes_coinc_sh[g])
#        print("\n")
#else:
#    print("NO EXISTEN CPE23URIS COINCIDENTES ENTRE LOS CPES Y LOS HIJOS DE LOS NODOS DE LA CONFIGURACIÓN DE CVES PARA SMART HOME")
    
    
    
cpes_coinc_iotsh=[]    
cpes_coinc_iotshaux=[]
    
for t in range(0,len(cpes_coinc)):
    cpes_coinc_iotsh.append(cpes_coinc[t])
    
for r in range(0,len(cpes_coinc_sh)):
    if(cpes_coinc_sh[r] not in cpes_coinc_iotsh):
        cpes_coinc_iotsh.append(cpes_coinc_sh[r])
        cpes_coinc_iotshaux.append(cpes_coinc_sh[r])
    


#Imprimo los cpes coincidentes
#if(len(cpes_coinc_iotsh)>0):
#    print('\033[1m'+"EXISTEN "+str(len(cpes_coinc_iotsh))+" CPE23URIS COINCIDENTES ENTRE LOS CPES Y LOS HIJOS DE LOS NODOS DE LA CONFIGURACIÓN DE CVES PARA IOT Y SMART HOME: \n"+'\033[0m')
#    for g in range(0,len(cpes_coinc_iotsh)):
#        print(" - "+cpes_coinc_iotsh[g])
#        print("\n")
#else:
#    print("NO EXISTEN CPE23URIS COINCIDENTES ENTRE LOS CPES Y LOS HIJOS DE LOS NODOS DE LA CONFIGURACIÓN DE CVES PARA SMART HOME")
    

#Abro los ficheros con los que voy a tratar



#Variables para almacenar el tipo de entrada segun el anio en el que fue modificado por ultima vez
cpes_lastmodified2023_typeversion_iot=0
cpes_lastmodified2023_typeproduct_iot=0
cpes_lastmodified2023_typeadvisory_iot=0
cpes_lastmodified2023_typechangelog_iot=0
cpes_lastmodified2023_typenone_iot=0
cpes_lastmodified2023_typevendor_iot=0
cpes_lastmodified2023_iot=0

cpes_lastmodified2022_typeversion_iot=0
cpes_lastmodified2022_typeproduct_iot=0
cpes_lastmodified2022_typeadvisory_iot=0
cpes_lastmodified2022_typechangelog_iot=0
cpes_lastmodified2022_typenone_iot=0
cpes_lastmodified2022_typevendor_iot=0
cpes_lastmodified2022_iot=0

cpes_lastmodified2021_typeversion_iot=0
cpes_lastmodified2021_typeproduct_iot=0
cpes_lastmodified2021_typeadvisory_iot=0
cpes_lastmodified2021_typechangelog_iot=0
cpes_lastmodified2021_typenone_iot=0
cpes_lastmodified2021_typevendor_iot=0
cpes_lastmodified2021_iot=0

cpes_lastmodified2020_typeversion_iot=0
cpes_lastmodified2020_typeproduct_iot=0
cpes_lastmodified2020_typeadvisory_iot=0
cpes_lastmodified2020_typechangelog_iot=0
cpes_lastmodified2020_typenone_iot=0
cpes_lastmodified2020_typevendor_iot=0
cpes_lastmodified2020_iot=0

cpes_lastmodified2019_typeversion_iot=0
cpes_lastmodified2019_typeproduct_iot=0
cpes_lastmodified2019_typeadvisory_iot=0
cpes_lastmodified2019_typechangelog_iot=0
cpes_lastmodified2019_typenone_iot=0
cpes_lastmodified2019_typevendor_iot=0
cpes_lastmodified2019_iot=0

cpes_lastmodified2018_typeversion_iot=0
cpes_lastmodified2018_typeproduct_iot=0
cpes_lastmodified2018_typeadvisory_iot=0
cpes_lastmodified2018_typechangelog_iot=0
cpes_lastmodified2018_typenone_iot=0
cpes_lastmodified2018_typevendor_iot=0
cpes_lastmodified2018_iot=0


#Variables para almacenar todos los cpes de la parte IOT y el indice de los cpes coincidentes para la parte iot y smart home
cpe23Uris_cpes=[]
indexcpe23Uris_cpes=[]
#Variables para almacenar todos los cpes de la parte SMART HOME y el indice de los cpes coincidentes para la parte iot y smart home aun no analizados
cpe23Uris_cpes_sh=[]
indexcpe23Uris_cpes_sh=[]

#Obtengo todos los cpes de la parte iot primero y smart home posteriormente
for r in range(0,len(df_cpe_iot["cpes.lastModifiedDate"])):
    cpe23Uris_cpes.append(df_cpe_iot["cpes.cpe23Uri"][r]) 
    
for k in range(0,len(df_cpe_sh["cpes.lastModifiedDate"])):
    cpe23Uris_cpes_sh.append(df_cpe_sh["cpes.cpe23Uri"][k]) 

#Obtengo los indices de los cpes coincidentes para la parte iot
for f in range(0,len(cpes_coinc)):
    index=cpe23Uris_cpes.index(cpes_coinc[f])
    indexcpe23Uris_cpes.append(index)
    
#Obtengo los indices de los cpes coincidentes para la parte iot y smart home que no han sido analizados    
for b in range(0,len(cpes_coinc_iotshaux)):
    index_sh=cpe23Uris_cpes_sh.index(cpes_coinc_iotshaux[b])
    indexcpe23Uris_cpes_sh.append(index_sh)

#Consulto el tipo de referencia y el anio de modificacion de las cpes coincidentes para las partes iot y smart home
for l in range(0,len(indexcpe23Uris_cpes)):
    r=int(indexcpe23Uris_cpes[l])    
#Recorro los valores de fecha de ultima modificacion
    str_anio_modifdate_cpe_iot=df_cpe_iot["cpes.lastModifiedDate"][r].split("-")
    anio_modifdate_cpe_iot=int(str_anio_modifdate_cpe_iot[0])
    if(anio_modifdate_cpe_iot >= 2023):
        #Compruebo si existen varios valores de tipo de entrada en una misma fila
        if('[' in df_cpe_iot["cpes.refs.type"][r]):
            aux=df_cpe_iot["cpes.refs.type"][r].split(",")
            for k in range(0,len(aux)):
                if(len(aux)>0):
                    #Recorro los valores de tipo de entrada para una misma fila
                    cpes_lastmodified2023_iot+=1
                    aux_str=aux[k].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
                    #Compruebo el tipo de entrada 
                    if(aux_str == 'NONE'):
                        cpes_lastmodified2023_typenone_iot+=1  
                    elif(aux_str == 'Version'):
                        cpes_lastmodified2023_typeversion_iot+=1  
                    elif(aux_str == 'Product'):
                        cpes_lastmodified2023_typeproduct_iot+=1  
                    elif(aux_str == 'Advisory'):
                        cpes_lastmodified2023_typeadvisory_iot+=1  
                    elif((aux_str == 'Change Log') or (aux_str == 'ChangeLog')):
                        cpes_lastmodified2023_typechangelog_iot+=1
                    elif(aux_str == 'Vendor'):
                        cpes_lastmodified2023_typevendor_iot+=1
        else:
            cpes_lastmodified2023_iot+=1
            if(df_cpe_iot["cpes.refs.type"][r] == 'NONE'):
                cpes_lastmodified2023_typenone_iot+=1 
            elif(df_cpe_iot["cpes.refs.type"][r] == 'Version'):
                cpes_lastmodified2023_typeversion_iot+=1 
            elif(df_cpe_iot["cpes.refs.type"][r] == 'Product'):
                cpes_lastmodified2023_typeproduct_iot+=1 
            elif(df_cpe_iot["cpes.refs.type"][r] == 'Advisory'):
                cpes_lastmodified2023_typeadvisory_iot+=1 
            elif((df_cpe_iot["cpes.refs.type"][r] == 'Change Log') or(df_cpe_iot["cpes.refs.type"][r] == 'ChangeLog')):
                cpes_lastmodified2023_typechangelog_iot+=1
            elif(df_cpe_iot["cpes.refs.type"][r] == 'Vendor'):
                cpes_lastmodified2023_typevendor_iot+=1
    elif(anio_modifdate_cpe_iot >= 2022):
        if('[' in df_cpe_iot["cpes.refs.type"][r]):
            aux=df_cpe_iot["cpes.refs.type"][r].split(",")
            for k in range(0,len(aux)):
                if(len(aux)>0):
                    cpes_lastmodified2022_iot+=1
                    aux_str=aux[k].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
                    if(aux_str == 'NONE'):
                        cpes_lastmodified2022_typenone_iot+=1  
                    elif(aux_str == 'Version'):
                        cpes_lastmodified2022_typeversion_iot+=1  
                    elif(aux_str == 'Product'):
                        cpes_lastmodified2022_typeproduct_iot+=1  
                    elif(aux_str == 'Advisory'):
                        cpes_lastmodified2022_typeadvisory_iot+=1  
                    elif((aux_str == 'Change Log') or (aux_str == 'ChangeLog')):
                        cpes_lastmodified2022_typechangelog_iot+=1
                    elif(aux_str == 'Vendor'):
                        cpes_lastmodified2022_typevendor_iot+=1
        else:
            cpes_lastmodified2022_iot+=1
            if(df_cpe_iot["cpes.refs.type"][r] == 'NONE'):
                cpes_lastmodified2022_typenone_iot+=1 
            elif(df_cpe_iot["cpes.refs.type"][r] == 'Version'):
                cpes_lastmodified2022_typeversion_iot+=1 
            elif(df_cpe_iot["cpes.refs.type"][r] == 'Product'):
                cpes_lastmodified2022_typeproduct_iot+=1 
            elif(df_cpe_iot["cpes.refs.type"][r] == 'Advisory'):
                cpes_lastmodified2022_typeadvisory_iot+=1 
            elif((df_cpe_iot["cpes.refs.type"][r] == 'Change Log') or(df_cpe_iot["cpes.refs.type"][r] == 'ChangeLog')):
                cpes_lastmodified2022_typechangelog_iot+=1
            elif(df_cpe_iot["cpes.refs.type"][r] == 'Vendor'):
                cpes_lastmodified2022_typevendor_iot+=1
    elif(anio_modifdate_cpe_iot >= 2021):
        if('[' in df_cpe_iot["cpes.refs.type"][r]):
            aux=df_cpe_iot["cpes.refs.type"][r].split(",")
            for k in range(0,len(aux)):
                if(len(aux)>0):
                    cpes_lastmodified2021_iot+=1
                    aux_str=aux[k].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
                    if(aux_str == 'NONE'):
                        cpes_lastmodified2021_typenone_iot+=1  
                    elif(aux_str == 'Version'):
                        cpes_lastmodified2021_typeversion_iot+=1  
                    elif(aux_str == 'Product'):
                        cpes_lastmodified2021_typeproduct_iot+=1  
                    elif(aux_str == 'Advisory'):
                        cpes_lastmodified2021_typeadvisory_iot+=1  
                    elif((aux_str == 'Change Log') or (aux_str == 'ChangeLog')):
                        cpes_lastmodified2021_typechangelog_iot+=1  
                    elif(aux_str == 'Vendor'):
                        cpes_lastmodified2022_typevendor_iot+=1
        else:
            cpes_lastmodified2021_iot+=1
            if(df_cpe_iot["cpes.refs.type"][r] == 'NONE'):
                cpes_lastmodified2021_typenone_iot+=1 
            elif(df_cpe_iot["cpes.refs.type"][r] == 'Version'):
                cpes_lastmodified2021_typeversion_iot+=1 
            elif(df_cpe_iot["cpes.refs.type"][r] == 'Product'):
                cpes_lastmodified2021_typeproduct_iot+=1 
            elif(df_cpe_iot["cpes.refs.type"][r] == 'Advisory'):
                cpes_lastmodified2021_typeadvisory_iot+=1 
            elif((df_cpe_iot["cpes.refs.type"][r] == 'Change Log') or(df_cpe_iot["cpes.refs.type"][r] == 'ChangeLog')):
                cpes_lastmodified2021_typechangelog_iot+=1
            elif(df_cpe_iot["cpes.refs.type"][r] == 'Vendor'):
                cpes_lastmodified2021_typevendor_iot+=1
    elif(anio_modifdate_cpe_iot >= 2020):
        if('[' in df_cpe_iot["cpes.refs.type"][r]):
            aux=df_cpe_iot["cpes.refs.type"][r].split(",")
            for k in range(0,len(aux)):
                if(len(aux)>0):
                    cpes_lastmodified2020_iot+=1
                    aux_str=aux[k].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
                    if(aux_str == 'NONE'):
                        cpes_lastmodified2020_typenone_iot+=1  
                    elif(aux_str == 'Version'):
                        cpes_lastmodified2020_typeversion_iot+=1  
                    elif(aux_str == 'Product'):
                        cpes_lastmodified2020_typeproduct_iot+=1  
                    elif(aux_str == 'Advisory'):
                        cpes_lastmodified2020_typeadvisory_iot+=1  
                    elif((aux_str == 'Change Log') or (aux_str == 'ChangeLog')):
                        cpes_lastmodified2020_typechangelog_iot+=1 
                    elif(aux_str == 'Vendor'):
                        cpes_lastmodified2020_typevendor_iot+=1
        else:
            cpes_lastmodified2020_iot+=1
            if(df_cpe_iot["cpes.refs.type"][r] == 'NONE'):
                cpes_lastmodified2020_typenone_iot+=1 
            elif(df_cpe_iot["cpes.refs.type"][r] == 'Version'):
                cpes_lastmodified2020_typeversion_iot+=1 
            elif(df_cpe_iot["cpes.refs.type"][r] == 'Product'):
                cpes_lastmodified2020_typeproduct_iot+=1 
            elif(df_cpe_iot["cpes.refs.type"][r] == 'Advisory'):
                cpes_lastmodified2020_typeadvisory_iot+=1 
            elif((df_cpe_iot["cpes.refs.type"][r] == 'Change Log') or(df_cpe_iot["cpes.refs.type"][r] == 'ChangeLog')):
                cpes_lastmodified2020_typechangelog_iot+=1
            elif(df_cpe_iot["cpes.refs.type"][r] == 'Vendor'):
                cpes_lastmodified2020_typevendor_iot+=1
    elif(anio_modifdate_cpe_iot >= 2019):
        if('[' in df_cpe_iot["cpes.refs.type"][r]):
            aux=df_cpe_iot["cpes.refs.type"][r].split(",")
            for k in range(0,len(aux)):
                if(len(aux)>0):
                    cpes_lastmodified2019_iot+=1
                    aux_str=aux[k].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
                    if(aux_str == 'NONE'):
                        cpes_lastmodified2019_typenone_iot+=1  
                    elif(aux_str == 'Version'):
                        cpes_lastmodified2019_typeversion_iot+=1  
                    elif(aux_str == 'Product'):
                        cpes_lastmodified2019_typeproduct_iot+=1  
                    elif(aux_str == 'Advisory'):
                        cpes_lastmodified2019_typeadvisory_iot+=1  
                    elif((aux_str == 'Change Log') or (aux_str == 'ChangeLog')):
                        cpes_lastmodified2019_typechangelog_iot+=1 
                    elif(aux_str == 'Vendor'):
                        cpes_lastmodified2019_typevendor_iot+=1
        else:
            cpes_lastmodified2019_iot+=1
            if(df_cpe_iot["cpes.refs.type"][r] == 'NONE'):
                cpes_lastmodified2019_typenone_iot+=1 
            elif(df_cpe_iot["cpes.refs.type"][r] == 'Version'):
                cpes_lastmodified2019_typeversion_iot+=1 
            elif(df_cpe_iot["cpes.refs.type"][r] == 'Product'):
                cpes_lastmodified2019_typeproduct_iot+=1 
            elif(df_cpe_iot["cpes.refs.type"][r] == 'Advisory'):
                cpes_lastmodified2019_typeadvisory_iot+=1 
            elif((df_cpe_iot["cpes.refs.type"][r] == 'Change Log') or(df_cpe_iot["cpes.refs.type"][r] == 'ChangeLog')):
                cpes_lastmodified2019_typechangelog_iot+=1
            elif(df_cpe_iot["cpes.refs.type"][r] == 'Vendor'):
                cpes_lastmodified2019_typevendor_iot+=1
    else:
        if('[' in df_cpe_iot["cpes.refs.type"][r]):
            aux=df_cpe_iot["cpes.refs.type"][r].split(",")
            for k in range(0,len(aux)):
                if(len(aux)>0):
                    cpes_lastmodified2018_iot+=1
                    aux_str=aux[k].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
                    if(aux_str == 'NONE'):
                        cpes_lastmodified2018_typenone_iot+=1  
                    elif(aux_str == 'Version'):
                        cpes_lastmodified2018_typeversion_iot+=1  
                    elif(aux_str == 'Product'):
                        cpes_lastmodified2018_typeproduct_iot+=1  
                    elif(aux_str == 'Advisory'):
                        cpes_lastmodified2018_typeadvisory_iot+=1  
                    elif((aux_str == 'Change Log') or (aux_str == 'ChangeLog')):
                        cpes_lastmodified2018_typechangelog_iot+=1 
                    elif(aux_str == 'Vendor'):
                        cpes_lastmodified2018_typevendor_iot+=1
        else:
            cpes_lastmodified2018_iot+=1
            if(df_cpe_iot["cpes.refs.type"][r] == 'NONE'):
                cpes_lastmodified2018_typenone_iot+=1 
            elif(df_cpe_iot["cpes.refs.type"][r] == 'Version'):
                cpes_lastmodified2018_typeversion_iot+=1 
            elif(df_cpe_iot["cpes.refs.type"][r] == 'Product'):
                cpes_lastmodified2018_typeproduct_iot+=1 
            elif(df_cpe_iot["cpes.refs.type"][r] == 'Advisory'):
                cpes_lastmodified2018_typeadvisory_iot+=1 
            elif((df_cpe_iot["cpes.refs.type"][r] == 'Change Log') or(df_cpe_iot["cpes.refs.type"][r] == 'ChangeLog')):
                cpes_lastmodified2018_typechangelog_iot+=1
            elif(df_cpe_iot["cpes.refs.type"][r] == 'Vendor'):
                cpes_lastmodified2018_typevendor_iot+=1
                
#Consulto el tipo de referencia y el anio de modificacion para los cpes coincidentes que no hemos analizado aun
for u in range(0,len(indexcpe23Uris_cpes_sh)):
    r=int(indexcpe23Uris_cpes_sh[u])    
    #Recorro los valores de fecha de ultima modificacion
    str_anio_modifdate_cpe_iot=df_cpe_sh["cpes.lastModifiedDate"][r].split("-")
    anio_modifdate_cpe_iot=int(str_anio_modifdate_cpe_iot[0])
    if(anio_modifdate_cpe_iot >= 2023):
        #Compruebo si existen varios valores de tipo de entrada en una misma fila
        if('[' in df_cpe_sh["cpes.refs.type"][r]):
            aux=df_cpe_sh["cpes.refs.type"][r].split(",")
            for k in range(0,len(aux)):
                if(len(aux)>0):
                    #Recorro los valores de tipo de entrada para una misma fila
                    cpes_lastmodified2023_iot+=1
                    aux_str=aux[k].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
                    #Compruebo el tipo de entrada 
                    if(aux_str == 'NONE'):
                        cpes_lastmodified2023_typenone_iot+=1  
                    elif(aux_str == 'Version'):
                        cpes_lastmodified2023_typeversion_iot+=1  
                    elif(aux_str == 'Product'):
                        cpes_lastmodified2023_typeproduct_iot+=1  
                    elif(aux_str == 'Advisory'):
                        cpes_lastmodified2023_typeadvisory_iot+=1  
                    elif((aux_str == 'Change Log') or (aux_str == 'ChangeLog')):
                        cpes_lastmodified2023_typechangelog_iot+=1
                    elif(aux_str == 'Vendor'):
                        cpes_lastmodified2023_typevendor_iot+=1
        else:
            cpes_lastmodified2023_iot+=1
            if(df_cpe_sh["cpes.refs.type"][r] == 'NONE'):
                cpes_lastmodified2023_typenone_iot+=1 
            elif(df_cpe_sh["cpes.refs.type"][r] == 'Version'):
                cpes_lastmodified2023_typeversion_iot+=1 
            elif(df_cpe_sh["cpes.refs.type"][r] == 'Product'):
                cpes_lastmodified2023_typeproduct_iot+=1 
            elif(df_cpe_sh["cpes.refs.type"][r] == 'Advisory'):
                cpes_lastmodified2023_typeadvisory_iot+=1 
            elif((df_cpe_sh["cpes.refs.type"][r] == 'Change Log') or(df_cpe_sh["cpes.refs.type"][r] == 'ChangeLog')):
                cpes_lastmodified2023_typechangelog_iot+=1
            elif(df_cpe_sh["cpes.refs.type"][r] == 'Vendor'):
                cpes_lastmodified2023_typevendor_iot+=1
    elif(anio_modifdate_cpe_iot >= 2022):
        if('[' in df_cpe_sh["cpes.refs.type"][r]):
            aux=df_cpe_sh["cpes.refs.type"][r].split(",")
            for k in range(0,len(aux)):
                if(len(aux)>0):
                    cpes_lastmodified2022_iot+=1
                    aux_str=aux[k].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
                    if(aux_str == 'NONE'):
                        cpes_lastmodified2022_typenone_iot+=1  
                    elif(aux_str == 'Version'):
                        cpes_lastmodified2022_typeversion_iot+=1  
                    elif(aux_str == 'Product'):
                        cpes_lastmodified2022_typeproduct_iot+=1  
                    elif(aux_str == 'Advisory'):
                        cpes_lastmodified2022_typeadvisory_iot+=1  
                    elif((aux_str == 'Change Log') or (aux_str == 'ChangeLog')):
                        cpes_lastmodified2022_typechangelog_iot+=1
                    elif(aux_str == 'Vendor'):
                        cpes_lastmodified2022_typevendor_iot+=1
        else:
            cpes_lastmodified2022_iot+=1
            if(df_cpe_sh["cpes.refs.type"][r] == 'NONE'):
                cpes_lastmodified2022_typenone_iot+=1 
            elif(df_cpe_sh["cpes.refs.type"][r] == 'Version'):
                cpes_lastmodified2022_typeversion_iot+=1 
            elif(df_cpe_sh["cpes.refs.type"][r] == 'Product'):
                cpes_lastmodified2022_typeproduct_iot+=1 
            elif(df_cpe_sh["cpes.refs.type"][r] == 'Advisory'):
                cpes_lastmodified2022_typeadvisory_iot+=1 
            elif((df_cpe_sh["cpes.refs.type"][r] == 'Change Log') or(df_cpe_sh["cpes.refs.type"][r] == 'ChangeLog')):
                cpes_lastmodified2022_typechangelog_iot+=1
            elif(df_cpe_sh["cpes.refs.type"][r] == 'Vendor'):
                cpes_lastmodified2022_typevendor_iot+=1
    elif(anio_modifdate_cpe_iot >= 2021):
        if('[' in df_cpe_sh["cpes.refs.type"][r]):
            aux=df_cpe_sh["cpes.refs.type"][r].split(",")
            for k in range(0,len(aux)):
                if(len(aux)>0):
                    cpes_lastmodified2021_iot+=1
                    aux_str=aux[k].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
                    if(aux_str == 'NONE'):
                        cpes_lastmodified2021_typenone_iot+=1  
                    elif(aux_str == 'Version'):
                        cpes_lastmodified2021_typeversion_iot+=1  
                    elif(aux_str == 'Product'):
                        cpes_lastmodified2021_typeproduct_iot+=1  
                    elif(aux_str == 'Advisory'):
                        cpes_lastmodified2021_typeadvisory_iot+=1  
                    elif((aux_str == 'Change Log') or (aux_str == 'ChangeLog')):
                        cpes_lastmodified2021_typechangelog_iot+=1  
                    elif(aux_str == 'Vendor'):
                        cpes_lastmodified2022_typevendor_iot+=1
        else:
            cpes_lastmodified2021_iot+=1
            if(df_cpe_sh["cpes.refs.type"][r] == 'NONE'):
                cpes_lastmodified2021_typenone_iot+=1 
            elif(df_cpe_sh["cpes.refs.type"][r] == 'Version'):
                cpes_lastmodified2021_typeversion_iot+=1 
            elif(df_cpe_sh["cpes.refs.type"][r] == 'Product'):
                cpes_lastmodified2021_typeproduct_iot+=1 
            elif(df_cpe_sh["cpes.refs.type"][r] == 'Advisory'):
                cpes_lastmodified2021_typeadvisory_iot+=1 
            elif((df_cpe_sh["cpes.refs.type"][r] == 'Change Log') or(df_cpe_sh["cpes.refs.type"][r] == 'ChangeLog')):
                cpes_lastmodified2021_typechangelog_iot+=1
            elif(df_cpe_sh["cpes.refs.type"][r] == 'Vendor'):
                cpes_lastmodified2021_typevendor_iot+=1
    elif(anio_modifdate_cpe_iot >= 2020):
        if('[' in df_cpe_sh["cpes.refs.type"][r]):
            aux=df_cpe_sh["cpes.refs.type"][r].split(",")
            for k in range(0,len(aux)):
                if(len(aux)>0):
                    cpes_lastmodified2020_iot+=1
                    aux_str=aux[k].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
                    if(aux_str == 'NONE'):
                        cpes_lastmodified2020_typenone_iot+=1  
                    elif(aux_str == 'Version'):
                        cpes_lastmodified2020_typeversion_iot+=1  
                    elif(aux_str == 'Product'):
                        cpes_lastmodified2020_typeproduct_iot+=1  
                    elif(aux_str == 'Advisory'):
                        cpes_lastmodified2020_typeadvisory_iot+=1  
                    elif((aux_str == 'Change Log') or (aux_str == 'ChangeLog')):
                        cpes_lastmodified2020_typechangelog_iot+=1 
                    elif(aux_str == 'Vendor'):
                        cpes_lastmodified2020_typevendor_iot+=1
        else:
            cpes_lastmodified2020_iot+=1
            if(df_cpe_sh["cpes.refs.type"][r] == 'NONE'):
                cpes_lastmodified2020_typenone_iot+=1 
            elif(df_cpe_sh["cpes.refs.type"][r] == 'Version'):
                cpes_lastmodified2020_typeversion_iot+=1 
            elif(df_cpe_sh["cpes.refs.type"][r] == 'Product'):
                cpes_lastmodified2020_typeproduct_iot+=1 
            elif(df_cpe_sh["cpes.refs.type"][r] == 'Advisory'):
                cpes_lastmodified2020_typeadvisory_iot+=1 
            elif((df_cpe_sh["cpes.refs.type"][r] == 'Change Log') or(df_cpe_sh["cpes.refs.type"][r] == 'ChangeLog')):
                cpes_lastmodified2020_typechangelog_iot+=1
            elif(df_cpe_sh["cpes.refs.type"][r] == 'Vendor'):
                cpes_lastmodified2020_typevendor_iot+=1
    elif(anio_modifdate_cpe_iot >= 2019):
        if('[' in df_cpe_sh["cpes.refs.type"][r]):
            aux=df_cpe_sh["cpes.refs.type"][r].split(",")
            for k in range(0,len(aux)):
                if(len(aux)>0):
                    cpes_lastmodified2019_iot+=1
                    aux_str=aux[k].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
                    if(aux_str == 'NONE'):
                        cpes_lastmodified2019_typenone_iot+=1  
                    elif(aux_str == 'Version'):
                        cpes_lastmodified2019_typeversion_iot+=1  
                    elif(aux_str == 'Product'):
                        cpes_lastmodified2019_typeproduct_iot+=1  
                    elif(aux_str == 'Advisory'):
                        cpes_lastmodified2019_typeadvisory_iot+=1  
                    elif((aux_str == 'Change Log') or (aux_str == 'ChangeLog')):
                        cpes_lastmodified2019_typechangelog_iot+=1 
                    elif(aux_str == 'Vendor'):
                        cpes_lastmodified2019_typevendor_iot+=1
        else:
            cpes_lastmodified2019_iot+=1
            if(df_cpe_sh["cpes.refs.type"][r] == 'NONE'):
                cpes_lastmodified2019_typenone_iot+=1 
            elif(df_cpe_sh["cpes.refs.type"][r] == 'Version'):
                cpes_lastmodified2019_typeversion_iot+=1 
            elif(df_cpe_sh["cpes.refs.type"][r] == 'Product'):
                cpes_lastmodified2019_typeproduct_iot+=1 
            elif(df_cpe_sh["cpes.refs.type"][r] == 'Advisory'):
                cpes_lastmodified2019_typeadvisory_iot+=1 
            elif((df_cpe_sh["cpes.refs.type"][r] == 'Change Log') or(df_cpe_sh["cpes.refs.type"][r] == 'ChangeLog')):
                cpes_lastmodified2019_typechangelog_iot+=1
            elif(df_cpe_sh["cpes.refs.type"][r] == 'Vendor'):
                cpes_lastmodified2019_typevendor_iot+=1
    else:
        if('[' in df_cpe_sh["cpes.refs.type"][r]):
            aux=df_cpe_sh["cpes.refs.type"][r].split(",")
            for k in range(0,len(aux)):
                if(len(aux)>0):
                    cpes_lastmodified2018_iot+=1
                    aux_str=aux[k].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
                    if(aux_str == 'NONE'):
                        cpes_lastmodified2018_typenone_iot+=1  
                    elif(aux_str == 'Version'):
                        cpes_lastmodified2018_typeversion_iot+=1  
                    elif(aux_str == 'Product'):
                        cpes_lastmodified2018_typeproduct_iot+=1  
                    elif(aux_str == 'Advisory'):
                        cpes_lastmodified2018_typeadvisory_iot+=1  
                    elif((aux_str == 'Change Log') or (aux_str == 'ChangeLog')):
                        cpes_lastmodified2018_typechangelog_iot+=1 
                    elif(aux_str == 'Vendor'):
                        cpes_lastmodified2018_typevendor_iot+=1
        else:
            cpes_lastmodified2018_iot+=1
            if(df_cpe_sh["cpes.refs.type"][r] == 'NONE'):
                cpes_lastmodified2018_typenone_iot+=1 
            elif(df_cpe_sh["cpes.refs.type"][r] == 'Version'):
                cpes_lastmodified2018_typeversion_iot+=1 
            elif(df_cpe_sh["cpes.refs.type"][r] == 'Product'):
                cpes_lastmodified2018_typeproduct_iot+=1 
            elif(df_cpe_sh["cpes.refs.type"][r] == 'Advisory'):
                cpes_lastmodified2018_typeadvisory_iot+=1 
            elif((df_cpe_sh["cpes.refs.type"][r] == 'Change Log') or(df_cpe_sh["cpes.refs.type"][r] == 'ChangeLog')):
                cpes_lastmodified2018_typechangelog_iot+=1
            elif(df_cpe_sh["cpes.refs.type"][r] == 'Vendor'):
                cpes_lastmodified2018_typevendor_iot+=1
   

                
                
print("*************************************ESTADÍSTICAS FECHA ULTIMA MODIFICACION/TIPO DE REFERENCIA DE CPES COINCIDENTES PARA HIJOS DE NODOS DE CVES Y CPE*************************************")
print("\n")                 
                
total_modified_cpe_iot=cpes_lastmodified2023_iot+cpes_lastmodified2022_iot+cpes_lastmodified2021_iot+cpes_lastmodified2020_iot+cpes_lastmodified2019_iot+cpes_lastmodified2018_iot                
                
print("\n")
print(" DE UN TOTAL DE "+str(total_modified_cpe_iot)+" REFERENCIAS DE CPES , LAS ESTADISTICAS DE RELACION DE FECHA DE MODIFICACION Y TIPO DE REFERENCIA SON LAS SIGUIENTES:  \n")
print("\n")
print("      -    EN  "+str(cpes_lastmodified2023_iot)+" REFERENCIAS DE CPES LA FECHA DE ULTIMA MODIFICACION DEL CPE ES 2023. LAS ESTADÍSTICAS DE TIPO DE REFERENCIA SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(cpes_lastmodified2023_typeversion_iot)+" REFERENCIAS EL TIPO ES VERSION ")
print("            -    EN  "+str(cpes_lastmodified2023_typeproduct_iot)+" REFERENCIAS EL TIPO ES PRODUCTO ")
print("            -    EN  "+str(cpes_lastmodified2023_typeadvisory_iot)+" REFERENCIAS EL TIPO ES AVISO ")
print("            -    EN  "+str(cpes_lastmodified2023_typechangelog_iot)+" REFERENCIAS EL TIPO ES REGISTRO DE CAMBIO ")
print("            -    EN  "+str(cpes_lastmodified2023_typevendor_iot)+" REFERENCIAS EL TIPO ES VENDEDOR ")
print("            -    EN  "+str(cpes_lastmodified2023_typenone_iot)+" REFERENCIAS EL TIPO NO VIENE ESPECIFICADO ")
print("\n")
print("      -    EN  "+str(cpes_lastmodified2022_iot)+" REFERENCIAS DE CPES LA FECHA DE ULTIMA MODIFICACION DEL CPE ES 2022. LAS ESTADÍSTICAS DE TIPO DE REFERENCIA SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(cpes_lastmodified2022_typeversion_iot)+" REFERENCIAS EL TIPO ES VERSION ")
print("            -    EN  "+str(cpes_lastmodified2022_typeproduct_iot)+" REFERENCIAS EL TIPO ES PRODUCTO ")
print("            -    EN  "+str(cpes_lastmodified2022_typeadvisory_iot)+" REFERENCIAS EL TIPO ES AVISO ")
print("            -    EN  "+str(cpes_lastmodified2022_typechangelog_iot)+" REFERENCIAS EL TIPO ES REGISTRO DE CAMBIO ")
print("            -    EN  "+str(cpes_lastmodified2022_typevendor_iot)+" REFERENCIAS EL TIPO ES VENDEDOR ")
print("            -    EN  "+str(cpes_lastmodified2022_typenone_iot)+" REFERENCIAS EL TIPO NO VIENE ESPECIFICADO ")
print("\n")
print("      -    EN  "+str(cpes_lastmodified2021_iot)+" REFERENCIAS DE CPES LA FECHA DE ULTIMA MODIFICACION DEL CPE ES 2021. LAS ESTADÍSTICAS DE TIPO DE REFERENCIA SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(cpes_lastmodified2021_typeversion_iot)+" REFERENCIAS EL TIPO ES VERSION ")
print("            -    EN  "+str(cpes_lastmodified2021_typeproduct_iot)+" REFERENCIAS EL TIPO ES PRODUCTO ")
print("            -    EN  "+str(cpes_lastmodified2021_typeadvisory_iot)+" REFERENCIAS EL TIPO ES AVISO ")
print("            -    EN  "+str(cpes_lastmodified2021_typechangelog_iot)+" REFERENCIAS EL TIPO ES REGISTRO DE CAMBIO ")
print("            -    EN  "+str(cpes_lastmodified2021_typevendor_iot)+" REFERENCIAS EL TIPO ES VENDEDOR ")
print("            -    EN  "+str(cpes_lastmodified2021_typenone_iot)+" REFERENCIAS EL TIPO NO VIENE ESPECIFICADO ")
print("\n")
print("      -    EN  "+str(cpes_lastmodified2020_iot)+" REFERENCIAS DE CPES LA FECHA DE ULTIMA MODIFICACION DEL CPE ES 2020. LAS ESTADÍSTICAS DE TIPO DE REFERENCIA SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(cpes_lastmodified2020_typeversion_iot)+" REFERENCIAS EL TIPO ES VERSION ")
print("            -    EN  "+str(cpes_lastmodified2020_typeproduct_iot)+" REFERENCIAS EL TIPO ES PRODUCTO ")
print("            -    EN  "+str(cpes_lastmodified2020_typeadvisory_iot)+" REFERENCIAS EL TIPO ES AVISO ")
print("            -    EN  "+str(cpes_lastmodified2020_typechangelog_iot)+" REFERENCIAS EL TIPO ES REGISTRO DE CAMBIO ")
print("            -    EN  "+str(cpes_lastmodified2020_typevendor_iot)+" REFERENCIAS EL TIPO ES VENDEDOR ")
print("            -    EN  "+str(cpes_lastmodified2020_typenone_iot)+" REFERENCIAS EL TIPO NO VIENE ESPECIFICADO ")
print("\n")
print("      -    EN  "+str(cpes_lastmodified2019_iot)+" REFERENCIAS DE CPES LA FECHA DE ULTIMA MODIFICACION DEL CPE ES 2019. LAS ESTADÍSTICAS DE TIPO DE REFERENCIA SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(cpes_lastmodified2019_typeversion_iot)+" REFERENCIAS EL TIPO ES VERSION ")
print("            -    EN  "+str(cpes_lastmodified2019_typeproduct_iot)+" REFERENCIAS EL TIPO ES PRODUCTO ")
print("            -    EN  "+str(cpes_lastmodified2019_typeadvisory_iot)+" REFERENCIAS EL TIPO ES AVISO ")
print("            -    EN  "+str(cpes_lastmodified2019_typechangelog_iot)+" REFERENCIAS EL TIPO ES REGISTRO DE CAMBIO ")
print("            -    EN  "+str(cpes_lastmodified2019_typevendor_iot)+" REFERENCIAS EL TIPO ES VENDEDOR ")
print("            -    EN  "+str(cpes_lastmodified2019_typenone_iot)+" REFERENCIAS EL TIPO NO VIENE ESPECIFICADO ")
print("\n")
print("      -    EN  "+str(cpes_lastmodified2018_iot)+" REFERENCIAS DE CPES LA FECHA DE ULTIMA MODIFICACION DEL CPE ES 2018 O ANTERIOR. LAS ESTADÍSTICAS DE TIPO DE REFERENCIA SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(cpes_lastmodified2018_typeversion_iot)+" REFERENCIAS EL TIPO ES VERSION ")
print("            -    EN  "+str(cpes_lastmodified2018_typeproduct_iot)+" REFERENCIAS EL TIPO ES PRODUCTO ")
print("            -    EN  "+str(cpes_lastmodified2018_typeadvisory_iot)+" REFERENCIAS EL TIPO ES AVISO ")
print("            -    EN  "+str(cpes_lastmodified2018_typechangelog_iot)+" REFERENCIAS EL TIPO ES REGISTRO DE CAMBIO ")
print("            -    EN  "+str(cpes_lastmodified2018_typevendor_iot)+" REFERENCIAS EL TIPO ES VENDEDOR ")
print("            -    EN  "+str(cpes_lastmodified2018_typenone_iot)+" REFERENCIAS EL TIPO NO VIENE ESPECIFICADO ")
print("\n")





print("*************************************PORCENTAJES FECHA ULTIMA MODIFICACION/TIPO DE REFERENCIA DE CPES COINCIDENTES PARA HIJOS DE NODOS DE CVES Y CPE*************************************")
print("\n")        
            
            
    
print("\n")
print(" DE UN TOTAL DE "+str(total_modified_cpe_iot)+" REFERENCIAS DE CPES , LOS PORCENTAJES DE RELACION DE FECHA DE MODIFICACION Y TIPO DE REFERENCIA SON LOS SIGUIENTES:  \n")
print("\n")
print("      -    EN EL "+str(float(((cpes_lastmodified2023_iot*100)/total_modified_cpe_iot)))+" % DE REFERENCIAS DE CPES LA FECHA DE ULTIMA MODIFICACION DEL CPE ES 2023. LOS PORCENTAJES DE TIPO DE REFERENCIA SON LOS SIGUIENTES:  \n")
print("\n")
print("            -    EN EL "+str(float(((cpes_lastmodified2023_typeversion_iot*100)/cpes_lastmodified2023_iot)))+" % DE REFERENCIAS EL TIPO ES VERSION  ")
print("            -    EN EL "+str(float(((cpes_lastmodified2023_typeproduct_iot*100)/cpes_lastmodified2023_iot)))+" % DE REFERENCIAS EL TIPO ES PRODUCTO ")
print("            -    EN EL "+str(float(((cpes_lastmodified2023_typeadvisory_iot*100)/cpes_lastmodified2023_iot)))+" % DE REFERENCIAS EL TIPO ES AVISO ")
print("            -    EN EL "+str(float(((cpes_lastmodified2023_typechangelog_iot*100)/cpes_lastmodified2023_iot)))+" % DE REFERENCIAS EL TIPO ES REGISTRO DE CAMBIO ")
print("            -    EN EL "+str(float(((cpes_lastmodified2023_typevendor_iot*100)/cpes_lastmodified2023_iot)))+" % DE REFERENCIAS EL TIPO ES VENDEDOR ")
print("            -    EN EL "+str(float(((cpes_lastmodified2023_typenone_iot*100)/cpes_lastmodified2023_iot)))+" % DE REFERENCIAS EL TIPO NO VIENE ESPECIFICADO ")
print("\n")
print("      -    EN EL "+str(float(((cpes_lastmodified2022_iot*100)/total_modified_cpe_iot)))+" % DE REFERENCIAS DE CPES LA FECHA DE ULTIMA MODIFICACION DEL CPE ES 2022. LOS PORCENTAJES DE TIPO DE REFERENCIA SON LOS SIGUIENTES:  \n")
print("\n")
print("            -    EN EL "+str(float(((cpes_lastmodified2022_typeversion_iot*100)/cpes_lastmodified2022_iot)))+" % DE REFERENCIAS EL TIPO ES VERSION  ")
print("            -    EN EL "+str(float(((cpes_lastmodified2022_typeproduct_iot*100)/cpes_lastmodified2022_iot)))+" % DE REFERENCIAS EL TIPO ES PRODUCTO ")
print("            -    EN EL "+str(float(((cpes_lastmodified2022_typeadvisory_iot*100)/cpes_lastmodified2022_iot)))+" % DE REFERENCIAS EL TIPO ES AVISO ")
print("            -    EN EL "+str(float(((cpes_lastmodified2022_typechangelog_iot*100)/cpes_lastmodified2022_iot)))+" % DE REFERENCIAS EL TIPO ES REGISTRO DE CAMBIO ")
print("            -    EN EL "+str(float(((cpes_lastmodified2022_typevendor_iot*100)/cpes_lastmodified2022_iot)))+" % DE REFERENCIAS EL TIPO ES VENDEDOR ")
print("            -    EN EL "+str(float(((cpes_lastmodified2022_typenone_iot*100)/cpes_lastmodified2022_iot)))+" % DE REFERENCIAS EL TIPO NO VIENE ESPECIFICADO ")
print("\n")
print("      -    EN EL "+str(float(((cpes_lastmodified2021_iot*100)/total_modified_cpe_iot)))+" % DE REFERENCIAS DE CPES LA FECHA DE ULTIMA MODIFICACION DEL CPE ES 2021. LOS PORCENTAJES DE TIPO DE REFERENCIA SON LOS SIGUIENTES:  \n")
print("\n")
print("            -    EN EL "+str(float(((cpes_lastmodified2021_typeversion_iot*100)/cpes_lastmodified2021_iot)))+" % DE REFERENCIAS EL TIPO ES VERSION  ")
print("            -    EN EL "+str(float(((cpes_lastmodified2021_typeproduct_iot*100)/cpes_lastmodified2021_iot)))+" % DE REFERENCIAS EL TIPO ES PRODUCTO ")
print("            -    EN EL "+str(float(((cpes_lastmodified2021_typeadvisory_iot*100)/cpes_lastmodified2021_iot)))+" % DE REFERENCIAS EL TIPO ES AVISO ")
print("            -    EN EL "+str(float(((cpes_lastmodified2021_typechangelog_iot*100)/cpes_lastmodified2021_iot)))+" % DE REFERENCIAS EL TIPO ES REGISTRO DE CAMBIO ")
print("            -    EN EL "+str(float(((cpes_lastmodified2021_typevendor_iot*100)/cpes_lastmodified2021_iot)))+" % DE REFERENCIAS EL TIPO ES VENDEDOR ")
print("            -    EN EL "+str(float(((cpes_lastmodified2021_typenone_iot*100)/cpes_lastmodified2021_iot)))+" % DE REFERENCIAS EL TIPO NO VIENE ESPECIFICADO ")
print("\n")
print("      -    EN EL "+str(float(((cpes_lastmodified2020_iot*100)/total_modified_cpe_iot)))+" % DE REFERENCIAS DE CPES LA FECHA DE ULTIMA MODIFICACION DEL CPE ES 2020. LOS PORCENTAJES DE TIPO DE REFERENCIA SON LOS SIGUIENTES:  \n")
print("\n")
print("            -    EN EL "+str(float(((cpes_lastmodified2020_typeversion_iot*100)/cpes_lastmodified2020_iot)))+" % DE REFERENCIAS EL TIPO ES VERSION  ")
print("            -    EN EL "+str(float(((cpes_lastmodified2020_typeproduct_iot*100)/cpes_lastmodified2020_iot)))+" % DE REFERENCIAS EL TIPO ES PRODUCTO ")
print("            -    EN EL "+str(float(((cpes_lastmodified2020_typeadvisory_iot*100)/cpes_lastmodified2020_iot)))+" % DE REFERENCIAS EL TIPO ES AVISO ")
print("            -    EN EL "+str(float(((cpes_lastmodified2020_typechangelog_iot*100)/cpes_lastmodified2020_iot)))+" % DE REFERENCIAS EL TIPO ES REGISTRO DE CAMBIO ")
print("            -    EN EL "+str(float(((cpes_lastmodified2020_typevendor_iot*100)/cpes_lastmodified2020_iot)))+" % DE REFERENCIAS EL TIPO ES VENDEDOR ")
print("            -    EN EL "+str(float(((cpes_lastmodified2020_typenone_iot*100)/cpes_lastmodified2020_iot)))+" % DE REFERENCIAS EL TIPO NO VIENE ESPECIFICADO ")
print("\n")
print("      -    EN EL "+str(float(((cpes_lastmodified2019_iot*100)/total_modified_cpe_iot)))+" % DE REFERENCIAS DE CPES LA FECHA DE ULTIMA MODIFICACION DEL CPE ES 2019. LOS PORCENTAJES DE TIPO DE REFERENCIA SON LOS SIGUIENTES:  \n")
print("\n")
print("            -    EN EL "+str(float(((cpes_lastmodified2019_typeversion_iot*100)/cpes_lastmodified2019_iot)))+" % DE REFERENCIAS EL TIPO ES VERSION  ")
print("            -    EN EL "+str(float(((cpes_lastmodified2019_typeproduct_iot*100)/cpes_lastmodified2019_iot)))+" % DE REFERENCIAS EL TIPO ES PRODUCTO ")
print("            -    EN EL "+str(float(((cpes_lastmodified2019_typeadvisory_iot*100)/cpes_lastmodified2019_iot)))+" % DE REFERENCIAS EL TIPO ES AVISO ")
print("            -    EN EL "+str(float(((cpes_lastmodified2019_typechangelog_iot*100)/cpes_lastmodified2019_iot)))+" % DE REFERENCIAS EL TIPO ES REGISTRO DE CAMBIO ")
print("            -    EN EL "+str(float(((cpes_lastmodified2019_typevendor_iot*100)/cpes_lastmodified2019_iot)))+" % DE REFERENCIAS EL TIPO ES VENDEDOR ")
print("            -    EN EL "+str(float(((cpes_lastmodified2019_typenone_iot*100)/cpes_lastmodified2019_iot)))+" % DE REFERENCIAS EL TIPO NO VIENE ESPECIFICADO ")
print("\n")
print("      -    EN EL "+str(float(((cpes_lastmodified2018_iot*100)/total_modified_cpe_iot)))+" % DE REFERENCIAS DE CPES LA FECHA DE ULTIMA MODIFICACION DEL CPE ES 2018 O ANTERIOR. LOS PORCENTAJES DE TIPO DE REFERENCIA SON LOS SIGUIENTES:  \n")
print("\n")
print("            -    EN EL "+str(float(((cpes_lastmodified2018_typeversion_iot*100)/cpes_lastmodified2018_iot)))+" % DE REFERENCIAS EL TIPO ES VERSION  ")
print("            -    EN EL "+str(float(((cpes_lastmodified2018_typeproduct_iot*100)/cpes_lastmodified2018_iot)))+" % DE REFERENCIAS EL TIPO ES PRODUCTO ")
print("            -    EN EL "+str(float(((cpes_lastmodified2018_typeadvisory_iot*100)/cpes_lastmodified2018_iot)))+" % DE REFERENCIAS EL TIPO ES AVISO ")
print("            -    EN EL "+str(float(((cpes_lastmodified2018_typechangelog_iot*100)/cpes_lastmodified2018_iot)))+" % DE REFERENCIAS EL TIPO ES REGISTRO DE CAMBIO ")
print("            -    EN EL "+str(float(((cpes_lastmodified2018_typevendor_iot*100)/cpes_lastmodified2018_iot)))+" % DE REFERENCIAS EL TIPO ES VENDEDOR ")
print("            -    EN EL "+str(float(((cpes_lastmodified2018_typenone_iot*100)/cpes_lastmodified2018_iot)))+" % DE REFERENCIAS EL TIPO NO VIENE ESPECIFICADO ")
print("\n")


