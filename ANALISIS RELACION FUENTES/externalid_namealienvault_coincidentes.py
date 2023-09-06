
import pandas as pd

df_alienvault_iot=pd.read_excel('alienvault_iot_2023.xlsx')
df_vulnibm_iot=pd.read_excel('vulnerabilidades_ibm_iot_2023.xlsx')


#Vector donde guardaremos los valores de la columna NAME donde se encuentra algun EXTERNAL REFERENCE ID
ibmexternalreferenceid_name_alienvault_iot=[]
#Vector donde guardaremos los valores no duplicados de la columna NAME donde se encuentra algun EXTERNAL REFERENCE ID
ibmexternalreferenceid_name_alienvault_iot=[]
#Vector donde guardaremos los EXTERNAL REFERENCE IDS incluidos en la columna NAME junto con el valor de la columna NAME
ibmexternalreferenceid_names_coincidentes_alienvault_iot=[]
#Vector donde guardaremos los EXTERNAL REFERENCE IDS incluidos en la columna NAME junto con el valor de la columna NAME, no duplicados
ibmexternalreferenceid_names_coincidentes_alienvault_iot_def=[]



#Recorremos la columna _NAME_ del fichero de ALIENVAULT iot
for i in range(0,len(df_alienvault_iot["name"])):
    #Si el nombre no esta especificado no hago nada
    if(df_alienvault_iot["name"][i] !='NONE'):
        #Vector donde guardaremos todos los NAMEs de la columna
        NAME_alienvault_iot=[]
        #Compruebo si en cada fila de la columna NAME hay solo un valor o varios
        if((",") in (df_alienvault_iot["name"][i])):
            #Si hay varios valores de NAME en la misma fila, separo cada uno de los valores
            aux_NAME_alienvault_iot = df_alienvault_iot["name"][i].split(',')
            #Inserto cada valor de NAME de cada fila en el vector donde estaran todos los valores de NAME, quitando algunos caracteres especiales y espacios
            for j in range(0,len(aux_NAME_alienvault_iot)):
                NAME_alienvault_iot.append(aux_NAME_alienvault_iot[j].replace('[','').replace(']','').replace("'","").replace(" ",""))
        #Si en la fila hay un solo valor de NAME, inserto directamente ese valor
        else:
            NAME_alienvault_iot.append(df_alienvault_iot["name"][i].replace('[','').replace(']','').replace("'","").replace(" ",""))
            
        #Compruebo en todos los valores que hemos insertado de NAME de la correspondiente fila si en alguno viene la cadena _vulnibm_, e inserto esos valores de NAME en el siguiente vector de nombres de EXTERNAL REFERENCE IDS
        ibmexternalreferenceid_name_iot=[]   
        for l in range(0,len(NAME_alienvault_iot)):
            if('CVE' in NAME_alienvault_iot[l] or 'cve'in NAME_alienvault_iot[l]):
                ibmexternalreferenceid_name_iot.append(NAME_alienvault_iot[l])
        
                
        #Si en la fila de la columna NAME hay algun valor que incluye la cadena CVE, la insertamos en el array general de EXTERNAL REFERENCE IDS de la columna NAME
        if(len(ibmexternalreferenceid_name_iot)>0):
            for y in range(0,len(ibmexternalreferenceid_name_iot)):
                #Si aparte del ID del EXTERNAL REFERENCE ID viene alguna cadena de texto mas
                arrayaux=ibmexternalreferenceid_name_iot[y].split("-")
                for i in range(0,len(arrayaux)):
                    if(len(arrayaux[i])==4):
                        #Recorremos el string hasta que encontramos el anio que forma parte del ID del EXTERNAL REFERENCE ID
                        if(arrayaux[i][0] == '2' and arrayaux[i][1] == '0' and (arrayaux[i][2] == '2' or arrayaux[i][2] == '1')):
                            #Creamos el string con el id del EXTERNAL REFERENCE ID
                            strax="CVE-"+arrayaux[i]+"-"+arrayaux[i+1]
                            #Comprobamos si la subcadena que viene despues del anio del ID del EXTERNAL REFERENCE ID es de longitud mayor que 4
                            if(len(arrayaux[i+1])>4):

                                #Comprobamos si el caracter siguiente es un numero o una letra
                                if(arrayaux[i+1][4] == '0' or arrayaux[i+1][4] == '1' or arrayaux[i+1][4] == '2' or arrayaux[i+1][4] == '3' or arrayaux[i+1][4] == '4' or arrayaux[i+1][4] == '5' or arrayaux[i+1][4] == '6' or arrayaux[i+1][4] == '7' or arrayaux[i+1][4] == '8' or arrayaux[i+1][4] == '9' ):
                                    #Comprobamos si la subcadena posterior al anio del ID del EXTERNAL REFERENCE ID es de largo mayor que 5
                                    if(len(arrayaux[i+1])>5):
                                        #Comprobamos si el caracter siguiente es un numero o letra
                                        if(arrayaux[i+1][5] == '0' or arrayaux[i+1][5] == '1' or arrayaux[i+1][5] == '2' or arrayaux[i+1][5] == '3' or arrayaux[i+1][5] == '4' or arrayaux[i+1][5] == '5' or arrayaux[i+1][5] == '6' or arrayaux[i+1][5] == '7' or arrayaux[i+1][5] == '8' or arrayaux[i+1][5] == '9' ):
                                            print("@")
                                            print(strax[0:13])
                                        else:
                                            #Si el siguiente caracter es una letra, dejamos de recorrer el string
                                            if(strax[0:14] not in ibmexternalreferenceid_name_alienvault_iot):
                                                ibmexternalreferenceid_name_alienvault_iot.append(strax[0:14])
                                    else:
                                        if(strax[0:14] not in ibmexternalreferenceid_name_alienvault_iot):
                                            ibmexternalreferenceid_name_alienvault_iot.append(strax[0:14])
                                else:
                                    #Dejamos de recorrer el string cuando encontremos una letra y no una cifra
                                    if(strax[0:13] not in ibmexternalreferenceid_name_alienvault_iot):
                                        ibmexternalreferenceid_name_alienvault_iot.append(strax[0:13])
                            else:
                                #Insertamos el ID del EXTERNAL REFERENCE ID si el largo del substring posterior al anio del ID del EXTERNAL REFERENCE ID es de longitud 4 o menor
                                if(strax not in ibmexternalreferenceid_name_alienvault_iot):
                                    ibmexternalreferenceid_name_alienvault_iot.append(strax)                                   
#Comprobamos los EXTERNAL REFERENCE IDS IDS coincidentes entre ALIENVAULT EXTERNAL REFERENCE ID
if(len(ibmexternalreferenceid_name_alienvault_iot)>0) :   
    #Recorro los IDS de la vulnerabilidades en el excel de EXTERNAL REFERENCE IDS
    for w in range(0,len(df_vulnibm_iot["external_references_external_id"])):
        if((df_vulnibm_iot["external_references_external_id"][w].replace('[','').replace(']','').replace("'","").replace("","").replace(" ","")) in ibmexternalreferenceid_name_alienvault_iot):
            ibmexternalreferenceid_names_coincidentes_alienvault_iot.append(df_vulnibm_iot["external_references_external_id"][w].replace('[','').replace(']','').replace("'","").replace("","").replace(" ",""))


print("\n")
#Si hemos encontrado EXTERNAL REFERENCES IDS coincidentes en la columna NAME de ALIENVAULT, los imprimo por pantalla
if(len(ibmexternalreferenceid_names_coincidentes_alienvault_iot)>0):
    print("EXISTEN "+str(len(ibmexternalreferenceid_names_coincidentes_alienvault_iot))+" IDENTIFICADORES DE REFERENCIAS EXTERNAS EN IBM COINCIDENTES O CONTENIDOS EN LA COLUMNA NOMBRE DE ALIENVAULT PARA LA PARTE IOT :")
    print("\n")
    for t in range(0,len(ibmexternalreferenceid_names_coincidentes_alienvault_iot)):
        print("- "+ibmexternalreferenceid_names_coincidentes_alienvault_iot[t])
        print("\n")
        
else:
    print("NO HAY IDENTIFICADORES DE REFERENCIAS EXTERNAS EN IBM COINCIDENTES O CONTENIDOS EN LA COLUMNA NOMBRE DE ALIENVAULT PARA LA PARTE IOT")
    
    
    
    
    
    
    


df_alienvault_sh=pd.read_excel('alienvault_smart_home_2023.xlsx')
df_vulnibm_sh=pd.read_excel('vulnerabilidades_ibm_smart_home_2023.xlsx')


#Vector donde guardaremos los valores de la columna NAME donde se encuentra algun EXTERNAL REFERENCE ID
ibmexternalreferenceid_name_alienvault_sh=[]
#Vector donde guardaremos los valores no duplicados de la columna NAME donde se encuentra algun EXTERNAL REFERENCE ID
ibmexternalreferenceid_name_alienvault_sh=[]
#Vector donde guardaremos los EXTERNAL REFERENCE IDS incluidos en la columna NAME junto con el valor de la columna NAME
ibmexternalreferenceid_names_coincidentes_alienvault_sh=[]
#Vector donde guardaremos los EXTERNAL REFERENCE IDS incluidos en la columna NAME junto con el valor de la columna NAME, no duplicados
ibmexternalreferenceid_names_coincidentes_alienvault_sh_def=[]



#Recorremos la columna _NAME_ del fichero de ALIENVAULT SMART HOME
for i in range(0,len(df_alienvault_sh["name"])):
    #Si el nombre no esta especificado no hago nada
    if(df_alienvault_sh["name"][i] !='NONE'):
        #Vector donde guardaremos todos los NAMEs de la columna
        NAME_alienvault_sh=[]
        #Compruebo si en cada fila de la columna NAME hay solo un valor o varios
        if((",") in (df_alienvault_sh["name"][i])):
            #Si hay varios valores de NAME en la misma fila, separo cada uno de los valores
            aux_NAME_alienvault_sh = df_alienvault_sh["name"][i].split(',')
            #Inserto cada valor de NAME de cada fila en el vector donde estaran todos los valores de NAME, quitando algunos caracteres especiales y espacios
            for j in range(0,len(aux_NAME_alienvault_sh)):
                NAME_alienvault_sh.append(aux_NAME_alienvault_sh[j].replace('[','').replace(']','').replace("'","").replace(" ",""))
        #Si en la fila hay un solo valor de NAME, inserto directamente ese valor
        else:
            NAME_alienvault_sh.append(df_alienvault_sh["name"][i].replace('[','').replace(']','').replace("'","").replace(" ",""))
            
        #Compruebo en todos los valores que hemos insertado de NAME de la correspondiente fila si en alguno viene la cadena _vulnibm_, e inserto esos valores de NAME en el siguiente vector de nombres de EXTERNAL REFERENCE IDS
        ibmexternalreferenceid_name_sh=[]   
        for l in range(0,len(NAME_alienvault_sh)):
            if('CVE' in NAME_alienvault_sh[l] or 'cve'in NAME_alienvault_sh[l]):
                ibmexternalreferenceid_name_sh.append(NAME_alienvault_sh[l])
        
                
        #Si en la fila de la columna NAME hay algun valor que incluye la cadena CVE, la insertamos en el array general de EXTERNAL REFERENCE IDS de la columna NAME
        if(len(ibmexternalreferenceid_name_sh)>0):
            for y in range(0,len(ibmexternalreferenceid_name_sh)):
                #Si aparte del ID del EXTERNAL REFERENCE ID viene alguna cadena de texto mas
                arrayaux=ibmexternalreferenceid_name_sh[y].split("-")
                for i in range(0,len(arrayaux)):
                    if(len(arrayaux[i])==4):
                        #Recorremos el string hasta que encontramos el anio que forma parte del ID del EXTERNAL REFERENCE ID
                        if(arrayaux[i][0] == '2' and arrayaux[i][1] == '0' and (arrayaux[i][2] == '2' or arrayaux[i][2] == '1')):
                            #Creamos el string con el id del EXTERNAL REFERENCE ID
                            strax="CVE-"+arrayaux[i]+"-"+arrayaux[i+1]
                            #Comprobamos si la subcadena que viene despues del anio del ID del EXTERNAL REFERENCE ID es de longitud mayor que 4
                            if(len(arrayaux[i+1])>4):

                                #Comprobamos si el caracter siguiente es un numero o una letra
                                if(arrayaux[i+1][4] == '0' or arrayaux[i+1][4] == '1' or arrayaux[i+1][4] == '2' or arrayaux[i+1][4] == '3' or arrayaux[i+1][4] == '4' or arrayaux[i+1][4] == '5' or arrayaux[i+1][4] == '6' or arrayaux[i+1][4] == '7' or arrayaux[i+1][4] == '8' or arrayaux[i+1][4] == '9' ):
                                    #Comprobamos si la subcadena posterior al anio del ID del EXTERNAL REFERENCE ID es de largo mayor que 5
                                    if(len(arrayaux[i+1])>5):
                                        #Comprobamos si el caracter siguiente es un numero o letra
                                        if(arrayaux[i+1][5] == '0' or arrayaux[i+1][5] == '1' or arrayaux[i+1][5] == '2' or arrayaux[i+1][5] == '3' or arrayaux[i+1][5] == '4' or arrayaux[i+1][5] == '5' or arrayaux[i+1][5] == '6' or arrayaux[i+1][5] == '7' or arrayaux[i+1][5] == '8' or arrayaux[i+1][5] == '9' ):
                                            print("@")
                                            print(strax[0:13])
                                        else:
                                            #Si el siguiente caracter es una letra, dejamos de recorrer el string
                                            if(strax[0:14] not in ibmexternalreferenceid_name_alienvault_sh):
                                                ibmexternalreferenceid_name_alienvault_sh.append(strax[0:14])
                                    else:
                                        if(strax[0:14] not in ibmexternalreferenceid_name_alienvault_sh):
                                            ibmexternalreferenceid_name_alienvault_sh.append(strax[0:14])
                                else:
                                    #Dejamos de recorrer el string cuando encontremos una letra y no una cifra
                                    if(strax[0:13] not in ibmexternalreferenceid_name_alienvault_sh):
                                        ibmexternalreferenceid_name_alienvault_sh.append(strax[0:13])
                            else:
                                #Insertamos el ID del EXTERNAL REFERENCE ID si el largo del substring posterior al anio del ID del EXTERNAL REFERENCE ID es de longitud 4 o menor
                                if(strax not in ibmexternalreferenceid_name_alienvault_sh):
                                    ibmexternalreferenceid_name_alienvault_sh.append(strax)                                   
#Comprobamos los EXTERNAL REFERENCE IDS IDS coincidentes entre ALIENVAULT EXTERNAL REFERENCE ID
if(len(ibmexternalreferenceid_name_alienvault_sh)>0) :   
    #Recorro los IDS de la vulnerabilidades en el excel de EXTERNAL REFERENCE IDS
    for w in range(0,len(df_vulnibm_sh["external_references_external_id"])):
        if((df_vulnibm_sh["external_references_external_id"][w].replace('[','').replace(']','').replace("'","").replace("","").replace(" ","")) in ibmexternalreferenceid_name_alienvault_sh):
            ibmexternalreferenceid_names_coincidentes_alienvault_sh.append(df_vulnibm_sh["external_references_external_id"][w].replace('[','').replace(']','').replace("'","").replace("","").replace(" ",""))

print("\n")
print("\n")
#Si hemos encontrado EXTERNAL REFERENCES IDS coincidentes en la columna NAME de ALIENVAULT, los imprimo por pantalla
if(len(ibmexternalreferenceid_names_coincidentes_alienvault_sh)>0):
    print("EXISTEN "+str(len(ibmexternalreferenceid_names_coincidentes_alienvault_sh))+" IDENTIFICADORES DE REFERENCIAS EXTERNAS EN IBM COINCIDENTES O CONTENIDOS EN LA COLUMNA NOMBRE DE ALIENVAULT PARA LA PARTE SMART HOME :")
    print("\n")
    for t in range(0,len(ibmexternalreferenceid_names_coincidentes_alienvault_sh)):
        print("- "+ibmexternalreferenceid_names_coincidentes_alienvault_sh[t])
        print("\n")
        
else:
    print("NO HAY IDENTIFICADORES DE REFERENCIAS EXTERNAS EN IBM COINCIDENTES O CONTENIDOS EN LA COLUMNA NOMBRE DE ALIENVAULT PARA LA PARTE SMART HOME")
    
    
    
    
    
    
    
    


#Vector donde guardaremos los valores de la columna NAME donde se encuentra algun EXTERNAL REFERENCE ID
ibmexternalreferenceid_name_alienvault_iotsh=[]
#Vector donde guardaremos los valores no duplicados de la columna NAME donde se encuentra algun EXTERNAL REFERENCE ID
ibmexternalreferenceid_name_alienvault_iotsh=[]
#Vector donde guardaremos los EXTERNAL REFERENCE IDS incluidos en la columna NAME junto con el valor de la columna NAME
ibmexternalreferenceid_names_coincidentes_alienvault_iotsh=[]
#Vector donde guardaremos los EXTERNAL REFERENCE IDS incluidos en la columna NAME junto con el valor de la columna NAME, no duplicados
ibmexternalreferenceid_names_coincidentes_alienvault_iotsh_def=[]



#Recorremos la columna _NAME_ del fichero de ALIENVAULT IOT
for i in range(0,len(df_alienvault_iot["name"])):
    #Si el nombre no esta especificado no hago nada
    if(df_alienvault_iot["name"][i] !='NONE'):
        #Vector donde guardaremos todos los NAMEs de la columna
        NAME_alienvault_iotsh=[]
        #Compruebo si en cada fila de la columna NAME hay solo un valor o varios
        if((",") in (df_alienvault_iot["name"][i])):
            #Si hay varios valores de NAME en la misma fila, separo cada uno de los valores
            aux_NAME_alienvault_iotsh = df_alienvault_iot["name"][i].split(',')
            #Inserto cada valor de NAME de cada fila en el vector donde estaran todos los valores de NAME, quitando algunos caracteres especiales y espacios
            for j in range(0,len(aux_NAME_alienvault_iotsh)):
                NAME_alienvault_iotsh.append(aux_NAME_alienvault_iotsh[j].replace('[','').replace(']','').replace("'","").replace(" ",""))
        #Si en la fila hay un solo valor de NAME, inserto directamente ese valor
        else:
            NAME_alienvault_iotsh.append(df_alienvault_iot["name"][i].replace('[','').replace(']','').replace("'","").replace(" ",""))
            
        #Compruebo en todos los valores que hemos insertado de NAME de la correspondiente fila si en alguno viene la cadena _vulnibm_, e inserto esos valores de NAME en el siguiente vector de nombres de EXTERNAL REFERENCE IDS
        ibmexternalreferenceid_name_iotsh=[]   
        for l in range(0,len(NAME_alienvault_iotsh)):
            if('CVE' in NAME_alienvault_iotsh[l] or 'cve'in NAME_alienvault_iotsh[l]):
                ibmexternalreferenceid_name_iotsh.append(NAME_alienvault_iotsh[l])
        
                
        #Si en la fila de la columna NAME hay algun valor que incluye la cadena CVE, la insertamos en el array general de EXTERNAL REFERENCE IDS de la columna NAME
        if(len(ibmexternalreferenceid_name_iotsh)>0):
            for y in range(0,len(ibmexternalreferenceid_name_iotsh)):
                #Si aparte del ID del EXTERNAL REFERENCE ID viene alguna cadena de texto mas
                arrayaux=ibmexternalreferenceid_name_iotsh[y].split("-")
                for i in range(0,len(arrayaux)):
                    if(len(arrayaux[i])==4):
                        #Recorremos el string hasta que encontramos el anio que forma parte del ID del EXTERNAL REFERENCE ID
                        if(arrayaux[i][0] == '2' and arrayaux[i][1] == '0' and (arrayaux[i][2] == '2' or arrayaux[i][2] == '1')):
                            #Creamos el string con el id del EXTERNAL REFERENCE ID
                            strax="CVE-"+arrayaux[i]+"-"+arrayaux[i+1]
                            #Comprobamos si la subcadena que viene despues del anio del ID del EXTERNAL REFERENCE ID es de longitud mayor que 4
                            if(len(arrayaux[i+1])>4):

                                #Comprobamos si el caracter siguiente es un numero o una letra
                                if(arrayaux[i+1][4] == '0' or arrayaux[i+1][4] == '1' or arrayaux[i+1][4] == '2' or arrayaux[i+1][4] == '3' or arrayaux[i+1][4] == '4' or arrayaux[i+1][4] == '5' or arrayaux[i+1][4] == '6' or arrayaux[i+1][4] == '7' or arrayaux[i+1][4] == '8' or arrayaux[i+1][4] == '9' ):
                                    #Comprobamos si la subcadena posterior al anio del ID del EXTERNAL REFERENCE ID es de largo mayor que 5
                                    if(len(arrayaux[i+1])>5):
                                        #Comprobamos si el caracter siguiente es un numero o letra
                                        if(arrayaux[i+1][5] == '0' or arrayaux[i+1][5] == '1' or arrayaux[i+1][5] == '2' or arrayaux[i+1][5] == '3' or arrayaux[i+1][5] == '4' or arrayaux[i+1][5] == '5' or arrayaux[i+1][5] == '6' or arrayaux[i+1][5] == '7' or arrayaux[i+1][5] == '8' or arrayaux[i+1][5] == '9' ):
                                            print("@")
                                            print(strax[0:13])
                                        else:
                                            #Si el siguiente caracter es una letra, dejamos de recorrer el string
                                            if(strax[0:14] not in ibmexternalreferenceid_name_alienvault_iotsh):
                                                ibmexternalreferenceid_name_alienvault_iotsh.append(strax[0:14])
                                    else:
                                        if(strax[0:14] not in ibmexternalreferenceid_name_alienvault_iotsh):
                                            ibmexternalreferenceid_name_alienvault_iotsh.append(strax[0:14])
                                else:
                                    #Dejamos de recorrer el string cuando encontremos una letra y no una cifra
                                    if(strax[0:13] not in ibmexternalreferenceid_name_alienvault_iotsh):
                                        ibmexternalreferenceid_name_alienvault_iotsh.append(strax[0:13])
                            else:
                                #Insertamos el ID del EXTERNAL REFERENCE ID si el largo del substring posterior al anio del ID del EXTERNAL REFERENCE ID es de longitud 4 o menor
                                if(strax not in ibmexternalreferenceid_name_alienvault_iotsh):
                                    ibmexternalreferenceid_name_alienvault_iotsh.append(strax)                                   
#Comprobamos los EXTERNAL REFERENCE IDS IDS coincidentes entre ALIENVAULT EXTERNAL REFERENCE ID
if(len(ibmexternalreferenceid_name_alienvault_iotsh)>0) :   
    #Recorro los IDS de la vulnerabilidades en el excel de EXTERNAL REFERENCE IDS
    for w in range(0,len(df_vulnibm_sh["external_references_external_id"])):
        if((df_vulnibm_sh["external_references_external_id"][w].replace('[','').replace(']','').replace("'","").replace("","").replace(" ","")) in ibmexternalreferenceid_name_alienvault_iotsh):
            ibmexternalreferenceid_names_coincidentes_alienvault_iotsh.append(df_vulnibm_sh["external_references_external_id"][w].replace('[','').replace(']','').replace("'","").replace("","").replace(" ",""))

print("\n")
print("\n")
#Si hemos encontrado EXTERNAL REFERENCES IDS coincidentes en la columna NAME de ALIENVAULT, los imprimo por pantalla
if(len(ibmexternalreferenceid_names_coincidentes_alienvault_iotsh)>0):
    print("EXISTE "+str(len(ibmexternalreferenceid_names_coincidentes_alienvault_iotsh))+" IDENTIFICADOR DE REFERENCIAS EXTERNAS EN IBM DE LA PARTE SMART HOME COINCIDENTE O CONTENIDO EN LA COLUMNA NOMBRE DE ALIENVAULT PARA LA PARTE IOT :")
    print("\n")
    for t in range(0,len(ibmexternalreferenceid_names_coincidentes_alienvault_iotsh)):
        print("- "+ibmexternalreferenceid_names_coincidentes_alienvault_iotsh[t])
        print("\n")
        
else:
    print("NO HAY IDENTIFICADORES DE REFERENCIAS EXTERNAS EN IBM DE LA PARTE SMART HOME COINCIDENTES O CONTENIDOS EN LA COLUMNA NOMBRE DE ALIENVAULT PARA LA PARTE IOT")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    


#Vector donde guardaremos los valores de la columna NAME donde se encuentra algun EXTERNAL REFERENCE ID
ibmexternalreferenceid_name_alienvault_shiot=[]
#Vector donde guardaremos los valores no duplicados de la columna NAME donde se encuentra algun EXTERNAL REFERENCE ID
ibmexternalreferenceid_name_alienvault_shiot=[]
#Vector donde guardaremos los EXTERNAL REFERENCE IDS incluidos en la columna NAME junto con el valor de la columna NAME
ibmexternalreferenceid_names_coincidentes_alienvault_shiot=[]
#Vector donde guardaremos los EXTERNAL REFERENCE IDS incluidos en la columna NAME junto con el valor de la columna NAME, no duplicados
ibmexternalreferenceid_names_coincidentes_alienvault_shiot_def=[]



#Recorremos la columna _NAME_ del fichero de ALIENVAULT SMART HOME
for i in range(0,len(df_alienvault_sh["name"])):
    #Si el nombre no esta especificado no hago nada
    if(df_alienvault_sh["name"][i] !='NONE'):
        #Vector donde guardaremos todos los NAMEs de la columna
        NAME_alienvault_shiot=[]
        #Compruebo si en cada fila de la columna NAME hay solo un valor o varios
        if((",") in (df_alienvault_sh["name"][i])):
            #Si hay varios valores de NAME en la misma fila, separo cada uno de los valores
            aux_NAME_alienvault_shiot = df_alienvault_sh["name"][i].split(',')
            #Inserto cada valor de NAME de cada fila en el vector donde estaran todos los valores de NAME, quitando algunos caracteres especiales y espacios
            for j in range(0,len(aux_NAME_alienvault_shiot)):
                NAME_alienvault_shiot.append(aux_NAME_alienvault_shiot[j].replace('[','').replace(']','').replace("'","").replace(" ",""))
        #Si en la fila hay un solo valor de NAME, inserto directamente ese valor
        else:
            NAME_alienvault_shiot.append(df_alienvault_sh["name"][i].replace('[','').replace(']','').replace("'","").replace(" ",""))
            
        #Compruebo en todos los valores que hemos insertado de NAME de la correspondiente fila si en alguno viene la cadena _vulnibm_, e inserto esos valores de NAME en el siguiente vector de nombres de EXTERNAL REFERENCE IDS
        ibmexternalreferenceid_name_shiot=[]   
        for l in range(0,len(NAME_alienvault_shiot)):
            if('CVE' in NAME_alienvault_shiot[l] or 'cve'in NAME_alienvault_shiot[l]):
                ibmexternalreferenceid_name_shiot.append(NAME_alienvault_shiot[l])
        
                
        #Si en la fila de la columna NAME hay algun valor que incluye la cadena CVE, la insertamos en el array general de EXTERNAL REFERENCE IDS de la columna NAME
        if(len(ibmexternalreferenceid_name_shiot)>0):
            for y in range(0,len(ibmexternalreferenceid_name_shiot)):
                #Si aparte del ID del EXTERNAL REFERENCE ID viene alguna cadena de texto mas
                arrayaux=ibmexternalreferenceid_name_shiot[y].split("-")
                for i in range(0,len(arrayaux)):
                    if(len(arrayaux[i]) ==4):
                        #Recorremos el string hasta que encontramos el anio que forma parte del ID del EXTERNAL REFERENCE ID
                        if(arrayaux[i][0] == '2' and arrayaux[i][1] == '0' and (arrayaux[i][2] == '2' or arrayaux[i][2] == '1')):
                            #Creamos el string con el id del EXTERNAL REFERENCE ID
                            strax="CVE-"+arrayaux[i]+"-"+arrayaux[i+1]
                            #Comprobamos si la subcadena que viene despues del anio del ID del EXTERNAL REFERENCE ID es de longitud mayor que 4
                            if(len(arrayaux[i+1])>4):

                                #Comprobamos si el caracter siguiente es un numero o una letra
                                if(arrayaux[i+1][4] == '0' or arrayaux[i+1][4] == '1' or arrayaux[i+1][4] == '2' or arrayaux[i+1][4] == '3' or arrayaux[i+1][4] == '4' or arrayaux[i+1][4] == '5' or arrayaux[i+1][4] == '6' or arrayaux[i+1][4] == '7' or arrayaux[i+1][4] == '8' or arrayaux[i+1][4] == '9' ):
                                    #Comprobamos si la subcadena posterior al anio del ID del EXTERNAL REFERENCE ID es de largo mayor que 5
                                    if(len(arrayaux[i+1])>5):
                                        #Comprobamos si el caracter siguiente es un numero o letra
                                        if(arrayaux[i+1][5] == '0' or arrayaux[i+1][5] == '1' or arrayaux[i+1][5] == '2' or arrayaux[i+1][5] == '3' or arrayaux[i+1][5] == '4' or arrayaux[i+1][5] == '5' or arrayaux[i+1][5] == '6' or arrayaux[i+1][5] == '7' or arrayaux[i+1][5] == '8' or arrayaux[i+1][5] == '9' ):
                                            print("@")
                                            print(strax[0:13])
                                        else:
                                            #Si el siguiente caracter es una letra, dejamos de recorrer el string
                                            if(strax[0:14] not in ibmexternalreferenceid_name_alienvault_shiot):
                                                ibmexternalreferenceid_name_alienvault_shiot.append(strax[0:14])
                                    else:
                                        if(strax[0:14] not in ibmexternalreferenceid_name_alienvault_shiot):
                                            ibmexternalreferenceid_name_alienvault_shiot.append(strax[0:14])
                                else:
                                    #Dejamos de recorrer el string cuando encontremos una letra y no una cifra
                                    if(strax[0:13] not in ibmexternalreferenceid_name_alienvault_shiot):
                                        ibmexternalreferenceid_name_alienvault_shiot.append(strax[0:13])
                            else:
                                #Insertamos el ID del EXTERNAL REFERENCE ID si el largo del substring posterior al anio del ID del EXTERNAL REFERENCE ID es de longitud 4 o menor
                                if(strax not in ibmexternalreferenceid_name_alienvault_shiot):
                                    ibmexternalreferenceid_name_alienvault_shiot.append(strax)                                   
#Comprobamos los EXTERNAL REFERENCE IDS IDS coincidentes entre ALIENVAULT EXTERNAL REFERENCE ID
if(len(ibmexternalreferenceid_name_alienvault_shiot)>0) :   
    #Recorro los IDS de la vulnerabilidades en el excel de EXTERNAL REFERENCE IDS
    for w in range(0,len(df_vulnibm_iot["external_references_external_id"])):
        if((df_vulnibm_iot["external_references_external_id"][w].replace('[','').replace(']','').replace("'","").replace("","").replace(" ","")) in ibmexternalreferenceid_name_alienvault_shiot):
            ibmexternalreferenceid_names_coincidentes_alienvault_shiot.append(df_vulnibm_iot["external_references_external_id"][w].replace('[','').replace(']','').replace("'","").replace("","").replace(" ",""))

print("\n")
print("\n")
#Si hemos encontrado EXTERNAL REFERENCES IDS coincidentes en la columna NAME de ALIENVAULT, los imprimo por pantalla
if(len(ibmexternalreferenceid_names_coincidentes_alienvault_shiot)>0):
    print("EXISTEN "+str(len(ibmexternalreferenceid_names_coincidentes_alienvault_shiot))+"IDENTIFICADORES DE REFERENCIAS EXTERNAS EN IBM DE LA PARTE IOT COINCIDENTES O CONTENIDOS EN LA COLUMNA NOMBRE DE ALIENVAULT PARA LA PARTE SMART HOME :")
    print("\n")
    for t in range(0,len(ibmexternalreferenceid_names_coincidentes_alienvault_shiot)):
        print("- "+ibmexternalreferenceid_names_coincidentes_alienvault_shiot[t])
        print("\n")
        
else:
    print("NO HAY IDENTIFICADORES DE REFERENCIAS EXTERNAS EN IBM DE LA PARTE IOT COINCIDENTES O CONTENIDOS EN LA COLUMNA NOMBRE DE ALIENVAULT PARA LA PARTE SMART HOME")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
   
    
    
    
    




































































