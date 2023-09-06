

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
    
    
    
    
#Vector para almacenar el nombre de los vendedores de las CPES
array_iot=[]
#Vector para almacenar el numero de veces que aparece un vendedor de una CPE
arraycounter_iot=[]

#Consulto los valores de las cpes coincidentes para las partes iot y smart home
for l in range(0,len(indexcpe23Uris_cpes)):
    r=int(indexcpe23Uris_cpes[l])    
    #Si existen varias cpe23Uris en una misma fila
    if('[' in df_cpe_iot["cpes.cpe23Uri"][r]):
        #Obtengo los valores de cpe23Uris
        aux=df_cpe_iot["cpes.cpe23Uri"][r].split(",")
        #Recorro los valores
        for k in range(0,len(aux)):
            if(len(aux)>0):
                aux_str=aux[k].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
                #Obtengo el valor vendedor para la cpe actual
                aux2=aux_str.split(":")
                vendor=aux2[3]
                #Si no existe el vendedor actual lo insertamos en el array y ponemos el contador de apariciones a 1
                if vendor not in array_iot:
                    array_iot.append(vendor)
                    arraycounter_iot.append(1)
                else:
                    #Si ya existe aumentamos su contador de apariciones en una unidad
                    index=array_iot.index(vendor)
                    counter=int(arraycounter_iot[index])
                    counter=counter+1
                    arraycounter_iot[index]=counter
    else:
        #Si existe un unico valor de cpe23Uri en la fila actual
        aux_str=df_cpe_iot["cpes.cpe23Uri"][r].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
        #Obtengo el valor de type/part del cpe23Uri actual
        aux2=aux_str.split(":")
        vendor=aux2[3]
        #Si no existe el vendedor actual lo insertamos en el array y ponemos el contador de apariciones a 1
        if vendor not in array_iot:
            array_iot.append(vendor)
            arraycounter_iot.append(1)
        else:
            #Si ya existe aumentamos su contador de apariciones en una unidad
            index=array_iot.index(vendor)
            counter=int(arraycounter_iot[index])
            counter=counter+1
            arraycounter_iot[index]=counter
            
            
                
#Consulto el tipo de referencia y el anio de modificacion para los cpes coincidentes que no hemos analizado aun
for u in range(0,len(indexcpe23Uris_cpes_sh)):
    r=int(indexcpe23Uris_cpes_sh[u])    
    #Recorro los valores de fecha de ultima modificacion
    #Si existen varias cpe23Uris en una misma fila
    if('[' in df_cpe_sh["cpes.cpe23Uri"][r]):
        #Obtengo los valores de cpe23Uris
        aux=df_cpe_sh["cpes.cpe23Uri"][r].split(",")
        #Recorro los valores
        for k in range(0,len(aux)):
            if(len(aux)>0):
                aux_str=aux[k].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
                #Obtengo el valor vendedor para la cpe actual
                aux2=aux_str.split(":")
                vendor=aux2[3]
                #Si no existe el vendedor actual lo insertamos en el array y ponemos el contador de apariciones a 1
                if vendor not in array_iot:
                    array_iot.append(vendor)
                    arraycounter_iot.append(1)
                else:
                    #Si ya existe aumentamos su contador de apariciones en una unidad
                    index=array_iot.index(vendor)
                    counter=int(arraycounter_iot[index])
                    counter=counter+1
                    arraycounter_iot[index]=counter
    else:
        #Si existe un unico valor de cpe23Uri en la fila actual
        aux_str=df_cpe_sh["cpes.cpe23Uri"][r].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
        #Obtengo el valor de type/part del cpe23Uri actual
        aux2=aux_str.split(":")
        vendor=aux2[3]
        #Si no existe el vendedor actual lo insertamos en el array y ponemos el contador de apariciones a 1
        if vendor not in array_iot:
            array_iot.append(vendor)
            arraycounter_iot.append(1)
        else:
            #Si ya existe aumentamos su contador de apariciones en una unidad
            index=array_iot.index(vendor)
            counter=int(arraycounter_iot[index])
            counter=counter+1
            arraycounter_iot[index]=counter
            
            

                
                
print("**************************ESTADÍSTICAS VENDEDOR CPES COINCIDENTES PARA HIJOS DE NODOS DE CVES Y CPE********************************")
print("\n")
print("  DE UN TOTAL DE  "+str(len(cpes_coinc_iotsh))+" CPES COINCIDENTES, LAS ESTADÍSTICAS DE VENDEDOR SON LAS SIGUIENTES : \n")

for g in range(0,len(array_iot)):
    print("  -  EN UN TOTAL DE  "+str(arraycounter_iot[g])+" CPES EL VENDEDOR ES "+str(array_iot[g].upper())+" \n")


print("\n")
print("**************************PORCENTAJE VENDEDOR CPES COINCIDENTES PARA HIJOS DE NODOS DE CVES Y CPE********************************")
print("\n")
print("  DE UN TOTAL DE  "+str(len(cpes_coinc_iotsh))+" CPES, LOS PORCENTAJES DE VENDEDOR SON LOS SIGUIENTES : \n")
for g in range(0,len(array_iot)):
    print("  -  EL "+str(float(((arraycounter_iot[g]*100)/len(df_cpe_iot["cpes.cpe23Uri"]))))+" % DE LOS CPES COINCIDENTES TIENEN COMO VENDEDOR "+str(array_iot[g].upper())+" \n")