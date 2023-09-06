
import pandas as pd

#Abrimos los ficheros con los que se trabajara
df_ali_iot=pd.read_excel('alienvault_iot_2023.xlsx')

#Vector para guardar las referencias de objetos de Alienvault para iot
object_refs_alienvault_iot=[]

#Vector para guardar los IDS de Alienvault para iot
ids_alienvault_iot=[]


elementos_coincidentes_refs_id_alienvault_iot=[]






#Recorro la columna de referencia de objetos para ALIENVAULT IOT
for k in range(0,len(df_ali_iot["object_refs"])):
    #Compruebo si la fila correspondiente de la columna object_refs tiene valor
    if(df_ali_iot["object_refs"][k] !='NONE'):
        #Compruebo si hay mas de un elemento en la fila o no
        if(',' in df_ali_iot["object_refs"][k]):
            #Obtengo los distintos valores de object_refs que existen en la fila y los guardo en un vector
            obj_ref_ali_iot = df_ali_iot["object_refs"][k].split(',')
            #Recorro el vector obtenido de los object_refs que existen en la fila actual
            for j in range(0,len(obj_ref_ali_iot)):
                #Inserto los valores de object_refs de la correspondiente fila en el vector de object_refs en caso de que no sean NONE
                if((obj_ref_ali_iot[j].replace('[','').replace(']','').replace("'","").replace("","").replace(" ",""))!='NONE'):
                    object_refs_alienvault_iot.append(obj_ref_ali_iot[j].replace('[','').replace(']','').replace("'","").replace("","").replace(" ",""))
        else:
            #Si hay una unica referencia de objeto en la fila , lo inserto en el vector de referencias de objetos
            object_refs_alienvault_iot.append(df_ali_iot["object_refs"][k].replace('[','').replace(']','').replace("'","").replace("",""))
            

            
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
            
            
            
            
            
            
            
            
            
            
            
#Compruebo si existen referencias de objetos de ALIENVAULT e ids coincidentes  
for elem_refs in object_refs_alienvault_iot:
    if elem_refs in ids_alienvault_iot:
        elementos_coincidentes_refs_id_alienvault_iot.append(elem_refs)

#Imprimo los resultados         
if(len(elementos_coincidentes_refs_id_alienvault_iot)==0):
    print("NO HAY OBJETOS DE REFERENCIA E IDS DE ALIENVAULT COINCIDENTES PARA LA RAMA IOT")
else:
    print("EXISTEN "+str(len(elementos_coincidentes_refs_id_alienvault_iot))+" OBJETOS DE REFERENCIA DE ALIENVAULT E IDS COINCIDENTES PARA LA RAMA IOT:")
    print("\n")
    for g in range(0,len(elementos_coincidentes_refs_id_alienvault_iot)):
        print("  -  "+elementos_coincidentes_refs_id_alienvault_iot[g])
        print("\n")
       
        
#Abrimos los ficheros con los que se trabajara
df_ali_sh=pd.read_excel('alienvault_smart_home_2023.xlsx')

#Vector para guardar las referencias de objetos de Alienvault para SMART HOME
object_refs_alienvault_sh=[]

#Vector para guardar los IDS de Alienvault para SMART HOME
ids_alienvault_sh=[]


elementos_coincidentes_refs_id_alienvault_sh=[]






#Recorro la columna de referencia de objetos para ALIENVAULT SMART HOME
for k in range(0,len(df_ali_sh["object_refs"])):
    #Compruebo si la fila correspondiente de la columna object_refs tiene valor
    if(df_ali_sh["object_refs"][k] !='NONE'):
        #Compruebo si hay mas de un elemento en la fila o no
        if(',' in df_ali_sh["object_refs"][k]):
            #Obtengo los distintos valores de object_refs que existen en la fila y los guardo en un vector
            obj_ref_ali_sh = df_ali_sh["object_refs"][k].split(',')
            #Recorro el vector obtenido de los object_refs que existen en la fila actual
            for j in range(0,len(obj_ref_ali_sh)):
                #Inserto los valores de object_refs de la correspondiente fila en el vector de object_refs en caso de que no sean NONE
                if((obj_ref_ali_sh[j].replace('[','').replace(']','').replace("'","").replace("","").replace(" ",""))!='NONE'):
                    object_refs_alienvault_sh.append(obj_ref_ali_sh[j].replace('[','').replace(']','').replace("'","").replace("","").replace(" ",""))
        else:
            #Si hay una unica referencia de objeto en la fila , lo inserto en el vector de referencias de objetos
            object_refs_alienvault_sh.append(df_ali_sh["object_refs"][k].replace('[','').replace(']','').replace("'","").replace("",""))
            

            
#Recorro la columna de ID para ALIENVAULT SMART HOME
for k in range(0,len(df_ali_sh["id"])):
    #Compruebo si la fila correspondiente de la columna ID tiene valor
    if(df_ali_sh["id"][k] !='NONE'):
        #Compruebo si hay mas de un elemento en la fila o no
        if(',' in df_ali_sh["id"][k]):
            #Obtengo los distintos valores de IDs que existen en la fila y los guardo en un vector
            id_ali_sh = df_ali_sh["id"][k].split(',')
            #Recorro el vector obtenido de los IDS que existen en la fila actual
            for j in range(0,len(id_ali_sh)):
                #Inserto los valores de ID de la correspondiente fila en el vector de IDS en caso de que no sean NONE
                if((id_ali_sh[j].replace('[','').replace(']','').replace("'","").replace("","").replace(" ",""))!='NONE'):
                    ids_alienvault_sh.append(id_ali_sh[j].replace('[','').replace(']','').replace("'","").replace("","").replace(" ",""))
        else:
            #Si hay un unico ID en la fila , lo inserto en el vector de IDS
            ids_alienvault_sh.append(df_ali_sh["id"][k].replace('[','').replace(']','').replace("'","").replace("",""))            
            
            
            
            
            
            
            
            
            
            
            
#Compruebo si existen referencias de objetos de ALIENVAULT e ids coincidentes  
for elem_refs in object_refs_alienvault_sh:
    if elem_refs in ids_alienvault_sh:
        elementos_coincidentes_refs_id_alienvault_sh.append(elem_refs)

#Imprimo los resultados         
if(len(elementos_coincidentes_refs_id_alienvault_sh)==0):
    print("NO HAY OBJETOS DE REFERENCIA E IDS DE ALIENVAULT COINCIDENTES PARA LA RAMA SMART HOME")
else:
    print("EXISTEN "+str(len(elementos_coincidentes_refs_id_alienvault_sh))+" OBJETOS DE REFERENCIA DE ALIENVAULT E IDS COINCIDENTES PARA LA RAMA SMART HOME:")
    print("\n")
    for g in range(0,len(elementos_coincidentes_refs_id_alienvault_sh)):
        print("  -  "+elementos_coincidentes_refs_id_alienvault_sh[g])
        print("\n")
        
        
        
        
        
#Compruebo si hay elementos coincidentes entre las partes IOT Y SMART HOME

#Vector donde guardare los OBJETOS DE REFERENCIA de ambas partes
objectrefs_alienvault=[]
#Vector donde guardare los ids de ambas partes
ids_alienvault=[]
#Vector donde guardare los elementos coincidentes de OBJECT REF E IDS
elementos_coincidentes_alienvault=[]

#Inserto los elementos de IOT y SMART HOME de las partes de IDS Y OBJETOS DE REFERENCIA en el vector correspondiente
for elem_refs in object_refs_alienvault_iot:
    objectrefs_alienvault.append(elem_refs)

for elem_refs_sh in object_refs_alienvault_sh:
    objectrefs_alienvault.append(elem_refs_sh)


for elem_refsalienvault in ids_alienvault_iot:
    ids_alienvault.append(elem_refsalienvault)

for elem_refsalienvault_sh in ids_alienvault_sh:
    ids_alienvault.append(elem_refsalienvault_sh)


#Busco los elementos coincidentes
for elem_refss in objectrefs_alienvault:
    if elem_refss in ids_alienvault:
        elementos_coincidentes_alienvault.append(elem_refss)

#Imprimo los resultados         
if(len(elementos_coincidentes_alienvault)==0):
    print("NO HAY IDS Y OBJETOS DE REFERENCIA DE ALIENVAULT COINCIDENTES")
else:
    print("EXISTEN "+str(len(elementos_coincidentes_alienvault))+" OBJETOS DE REFERENCIA E IDS DE ALIENVAULT COINCIDENTES:")
    print("\n")
    for g in range(0,len(elementos_coincidentes_alienvault)):
        print("  -  "+elementos_coincidentes_alienvault[g])
        print("\n")

        
numero_indicadores_coincidentes=0
numero_identidad_coincidentes=0
numero_vulnerabilidad_coincidentes=0

for h in range(0,len(elementos_coincidentes_alienvault)):
    if("identity" in elementos_coincidentes_alienvault[h]):
        numero_identidad_coincidentes+=1
            
    elif("indicator" in elementos_coincidentes_alienvault[h]):
        numero_indicadores_coincidentes+=1
        
    elif("vulnerability" in elementos_coincidentes_alienvault[h]):
        numero_vulnerabilidad_coincidentes+=1
    else:
        print(elementos_coincidentes_alienvault[h])

print("\n")
print("\n")
print("*************************************ESTADÍSTICAS OBJETOS DE REFERENCIA E IDS DE ALIENVAULT COINCIDENTES PARTE IOT Y SMART HOME CONJUNTAS : *************************************")    
print("\n")
print(" - DE UN TOTAL DE "+str(len(elementos_coincidentes_alienvault))+" OBJETOS DE REFERENCIA CUYO IDENTIFICADOR VIENE INDICADO EN LAS FUENTES DE DATOS, LAS ESTADÍSTICAS DE TIPO DE OBJETO DE REFERENCIA SON LAS SIGUIENTES :")
print("\n")
print("  -  EXISTEN "+str(numero_indicadores_coincidentes)+" OBJETOS DE REFERENCIA E IDS DE ALIENVAULT COINCIDENTES DE TIPO INDICADOR")
print("\n")
print("  -  EXISTEN "+str(numero_identidad_coincidentes)+" OBJETOS DE REFERENCIA E IDS DE ALIENVAULT COINCIDENTES DE TIPO IDENTIDAD")
print("\n")
print("  -  EXISTEN "+str(numero_vulnerabilidad_coincidentes)+" OBJETOS DE REFERENCIA E IDS DE ALIENVAULT COINCIDENTES DE TIPO VULNERABILIDAD")
print("\n")
print("\n")


