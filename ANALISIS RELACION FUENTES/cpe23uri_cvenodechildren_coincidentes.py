

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
if(len(cpes_coinc)>0):
    print('\033[1m'+"EXISTEN "+str(len(cpes_coinc))+" CPE23URIS COINCIDENTES ENTRE LOS CPES Y LOS HIJOS DE LOS NODOS DE LA CONFIGURACIÓN DE CVES PARA IOT: \n"+'\033[0m')
    for g in range(0,len(cpes_coinc)):
        print(" - "+cpes_coinc[g])
        print("\n")
else:
    print("NO EXISTEN CPE23URIS COINCIDENTES ENTRE LOS CPES Y LOS HIJOS DE LOS NODOS DE LA CONFIGURACIÓN DE CVES PARA IOT")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
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
if(len(cpes_coinc_sh)>0):
    print('\033[1m'+"EXISTEN "+str(len(cpes_coinc_sh))+" CPE23URIS COINCIDENTES ENTRE LOS CPES Y LOS HIJOS DE LOS NODOS DE LA CONFIGURACIÓN DE CVES PARA SMART HOME: \n"+'\033[0m')
    for g in range(0,len(cpes_coinc_sh)):
        print(" - "+cpes_coinc_sh[g])
        print("\n")
else:
    print("NO EXISTEN CPE23URIS COINCIDENTES ENTRE LOS CPES Y LOS HIJOS DE LOS NODOS DE LA CONFIGURACIÓN DE CVES PARA SMART HOME")
    
    
    
cpes_coinc_iotsh=[]    
    
    
for t in range(0,len(cpes_coinc)):
    cpes_coinc_iotsh.append(cpes_coinc[t])
    
for r in range(0,len(cpes_coinc_sh)):
    if(cpes_coinc_sh[r] not in cpes_coinc_iotsh):
        cpes_coinc_iotsh.append(cpes_coinc_sh[r])
    

print("\n")
print("\n")
print("\n")
#Imprimo los cpes coincidentes
if(len(cpes_coinc_iotsh)>0):
    print('\033[1m'+"EXISTEN "+str(len(cpes_coinc_iotsh))+" CPE23URIS COINCIDENTES ENTRE LOS CPES Y LOS HIJOS DE LOS NODOS DE LA CONFIGURACIÓN DE CVES PARA IOT Y SMART HOME: \n"+'\033[0m')
    for g in range(0,len(cpes_coinc_iotsh)):
        print(" - "+cpes_coinc_iotsh[g])
        print("\n")
else:
    print("NO EXISTEN CPE23URIS COINCIDENTES ENTRE LOS CPES Y LOS HIJOS DE LOS NODOS DE LA CONFIGURACIÓN DE CVES PARA SMART HOME")
    
    

    
    