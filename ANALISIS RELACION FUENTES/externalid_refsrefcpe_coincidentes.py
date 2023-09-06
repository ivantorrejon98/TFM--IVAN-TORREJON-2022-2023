import pandas as pd

df_cpe_iot=pd.read_excel('cpes_iot_2023.xlsx')
df_vulnibm_iot=pd.read_excel('vulnerabilidades_ibm_iot_2023.xlsx')


#Vector donde guardaremos los valores de la columna REFS_REF donde se encuentra algun EXTERNAL_REFERENCEID
externalreferenceid_REFS_REF_cpe_iot=[]
#Vector donde guardaremos los valores no duplicados de la columna REFS_REF donde se encuentra algun EXTERNAL_REFERENCEID
externalreferenceid_REFS_REF_cpe_iot=[]
#Vector donde guardaremos los EXTERNAL_REFERENCEIDS incluidos en la columna REFS_REF junto con el valor de la columna REFS_REF
externalreferenceid_REFS_REFs_coincidentes_cpe_iot=[]
#Vector donde guardaremos los EXTERNAL_REFERENCEIDS incluidos en la columna REFS_REF junto con el valor de la columna REFS_REF, no duplicados
externalreferenceid_REFS_REFs_coincidentes_cpe_iot_def=[]



#Recorremos la columna _REFS_REF_ del fichero de cpe iot
for i in range(0,len(df_cpe_iot["cpes.refs.ref"])):
    #Si el nombre no esta especificado no hago nada
    if(df_cpe_iot["cpes.refs.ref"][i] !='NONE'):
        #Vector donde guardaremos todos los REFS_REFs de la columna
        REFS_REF_cpe_iot=[]
        #Compruebo si en cada fila de la columna REFS_REF hay solo un valor o varios
        if((",") in (df_cpe_iot["cpes.refs.ref"][i])):
            #Si hay varios valores de REFS_REF en la misma fila, separo cada uno de los valores
            aux_REFS_REF_cpe_iot = df_cpe_iot["cpes.refs.ref"][i].split(',')
            #Inserto cada valor de REFS_REF de cada fila en el vector donde estaran todos los valores de REFS_REF, quitando algunos caracteres especiales y espacios
            for j in range(0,len(aux_REFS_REF_cpe_iot)):
                REFS_REF_cpe_iot.append(aux_REFS_REF_cpe_iot[j].replace('[','').replace(']','').replace("'","").replace(" ",""))
        #Si en la fila hay un solo valor de REFS_REF, inserto directamente ese valor
        else:
            REFS_REF_cpe_iot.append(df_cpe_iot["cpes.refs.ref"][i].replace('[','').replace(']','').replace("'","").replace(" ",""))
            
        #Compruebo en todos los valores que hemos insertado de REFS_REF de la correspondiente fila si en alguno viene la cadena _vulnibm_, e inserto esos valores de REFS_REF en el siguiente vector de nombres de EXTERNAL_REFERENCEIDS
        externalreferenceid_REFS_REF_iot=[]   
        for l in range(0,len(REFS_REF_cpe_iot)):
            if('CVE' in REFS_REF_cpe_iot[l] or 'cve' in REFS_REF_cpe_iot[l]):
                externalreferenceid_REFS_REF_iot.append(REFS_REF_cpe_iot[l])
        
                
        #Si en la fila de la columna REFS_REF hay algun valor que incluye la cadena EXTERNAL_REFERENCEID, la insertamos en el array general de EXTERNAL_REFERENCEIDS de la columna REFS_REF
        if(len(externalreferenceid_REFS_REF_iot)>0):
            for y in range(0,len(externalreferenceid_REFS_REF_iot)):
                #Si aparte del ID del EXTERNAL_REFERENCEID viene alguna cadena de texto mas
                arrayaux=externalreferenceid_REFS_REF_iot[y].split("-")
                for i in range(0,len(arrayaux)):
                    #Recorremos el string hasta que encontramos el anio que forma parte del ID del EXTERNAL_REFERENCEID
                    if(arrayaux[i][0] == '2' and arrayaux[i][1] == '0' and (arrayaux[i][2] == '2' or arrayaux[i][2] == '1')):
                        #Creamos el string con el id del EXTERNAL_REFERENCEID
                        strax="CVE-"+arrayaux[i]+"-"+arrayaux[i+1]
                        #Comprobamos si la subcadena que viene despues del anio del ID del EXTERNAL_REFERENCEID es de longitud mayor que 4
                        if(len(arrayaux[i+1])>4):

                            #Comprobamos si el caracter siguiente es un numero o una letra
                            if(arrayaux[i+1][4] == '0' or arrayaux[i+1][4] == '1' or arrayaux[i+1][4] == '2' or arrayaux[i+1][4] == '3' or arrayaux[i+1][4] == '4' or arrayaux[i+1][4] == '5' or arrayaux[i+1][4] == '6' or arrayaux[i+1][4] == '7' or arrayaux[i+1][4] == '8' or arrayaux[i+1][4] == '9' ):
                                #Comprobamos si la subcadena posterior al anio del ID del EXTERNAL_REFERENCEID es de largo mayor que 5
                                if(len(arrayaux[i+1])>5):
                                    #Comprobamos si el caracter siguiente es un numero o letra
                                    if(arrayaux[i+1][5] == '0' or arrayaux[i+1][5] == '1' or arrayaux[i+1][5] == '2' or arrayaux[i+1][5] == '3' or arrayaux[i+1][5] == '4' or arrayaux[i+1][5] == '5' or arrayaux[i+1][5] == '6' or arrayaux[i+1][5] == '7' or arrayaux[i+1][5] == '8' or arrayaux[i+1][5] == '9' ):
                                        print("@")
                                        print(strax[0:13])
                                    else:
                                        #Si el siguiente caracter es una letra, dejamos de recorrer el string
                                        if(strax[0:14] not in externalreferenceid_REFS_REF_cpe_iot):
                                            externalreferenceid_REFS_REF_cpe_iot.append(strax[0:14])
                                else:
                                    if(strax[0:14] not in externalreferenceid_REFS_REF_cpe_iot):
                                        externalreferenceid_REFS_REF_cpe_iot.append(strax[0:14])
                            else:
                                #Dejamos de recorrer el string cuando encontremos una letra y no una cifra
                                if(strax[0:13] not in externalreferenceid_REFS_REF_cpe_iot):
                                    externalreferenceid_REFS_REF_cpe_iot.append(strax[0:13])
                        else:
                            #Insertamos el ID del EXTERNAL_REFERENCEID si el largo del substring posterior al anio del ID del EXTERNAL_REFERENCEID es de longitud 4 o menor
                            if(strax not in externalreferenceid_REFS_REF_cpe_iot):
                                externalreferenceid_REFS_REF_cpe_iot.append(strax)                                   
#Comprobamos los EXTERNAL_REFERENCEIDS IDS coincidentes entre cpe y EXTERNAL_REFERENCEID
if(len(externalreferenceid_REFS_REF_cpe_iot)>0) :   
    #Recorro los IDS de la vulnerabilidades en el excel de EXTERNAL_REFERENCEIDS
    for w in range(0,len(df_vulnibm_iot["external_references_external_id"])):
        if((df_vulnibm_iot["external_references_external_id"][w].replace('[','').replace(']','').replace("'","").replace("","").replace(" ","")) in externalreferenceid_REFS_REF_cpe_iot):
            externalreferenceid_REFS_REFs_coincidentes_cpe_iot.append(df_vulnibm_iot["external_references_external_id"][w].replace('[','').replace(']','').replace("'","").replace("","").replace(" ",""))


#Si hemos encontrado EXTERNAL_REFERENCEIDS coincidentes en la columna REFS_REF de cpe, los imprimo por pantalla
if(len(externalreferenceid_REFS_REFs_coincidentes_cpe_iot)>0):
    print("EXISTEN "+str(len(externalreferenceid_REFS_REFs_coincidentes_cpe_iot))+" IDS DE REFERENCIAS EXTERNAS IBM COINCIDENTES O CONTENIDOS EN LAS FUENTES DE REFERENCIA DE CPE DE LA PARTE DE IOT :")
    print("\n")
    for t in range(0,len(externalreferenceid_REFS_REFs_coincidentes_cpe_iot)):
        print("- "+externalreferenceid_REFS_REFs_coincidentes_cpe_iot[t])
        print("\n")
        
else:
    print("NO HAY IDS DE REFERENCIAS EXTERNAS IBM COINCIDENTES O CONTENIDOS EN LAS FUENTES DE REFERENCIA DE CPE DE LA PARTE DE IOT ")
    
    
    
    
    
    
    


df_cpe_sh=pd.read_excel('cpes_smart_home_2023.xlsx')
df_vulnibm_sh=pd.read_excel('vulnerabilidades_ibm_smart_home_2023.xlsx')


#Vector donde guardaremos los valores de la columna REFS_REF donde se encuentra algun EXTERNAL_REFERENCEID
externalreferenceid_REFS_REF_cpe_sh=[]
#Vector donde guardaremos los valores no duplicados de la columna REFS_REF donde se encuentra algun EXTERNAL_REFERENCEID
externalreferenceid_REFS_REF_cpe_sh=[]
#Vector donde guardaremos los EXTERNAL_REFERENCEIDS incluidos en la columna REFS_REF junto con el valor de la columna REFS_REF
externalreferenceid_REFS_REFs_coincidentes_cpe_sh=[]
#Vector donde guardaremos los EXTERNAL_REFERENCEIDS incluidos en la columna REFS_REF junto con el valor de la columna REFS_REF, no duplicados
externalreferenceid_REFS_REFs_coincidentes_cpe_sh_def=[]



#Recorremos la columna _REFS_REF_ del fichero de cpe SMART HOME
for i in range(0,len(df_cpe_sh["cpes.refs.ref"])):
    #Si el nombre no esta especificado no hago nada
    if(df_cpe_sh["cpes.refs.ref"][i] !='NONE'):
        #Vector donde guardaremos todos los REFS_REFs de la columna
        REFS_REF_cpe_sh=[]
        #Compruebo si en cada fila de la columna REFS_REF hay solo un valor o varios
        if((",") in (df_cpe_sh["cpes.refs.ref"][i])):
            #Si hay varios valores de REFS_REF en la misma fila, separo cada uno de los valores
            aux_REFS_REF_cpe_sh = df_cpe_sh["cpes.refs.ref"][i].split(',')
            #Inserto cada valor de REFS_REF de cada fila en el vector donde estaran todos los valores de REFS_REF, quitando algunos caracteres especiales y espacios
            for j in range(0,len(aux_REFS_REF_cpe_sh)):
                REFS_REF_cpe_sh.append(aux_REFS_REF_cpe_sh[j].replace('[','').replace(']','').replace("'","").replace(" ",""))
        #Si en la fila hay un solo valor de REFS_REF, inserto directamente ese valor
        else:
            REFS_REF_cpe_sh.append(df_cpe_sh["cpes.refs.ref"][i].replace('[','').replace(']','').replace("'","").replace(" ",""))
            
        #Compruebo en todos los valores que hemos insertado de REFS_REF de la correspondiente fila si en alguno viene la cadena _vulnibm_, e inserto esos valores de REFS_REF en el siguiente vector de nombres de EXTERNAL_REFERENCEIDS
        externalreferenceid_REFS_REF_sh=[]   
        for l in range(0,len(REFS_REF_cpe_sh)):
            if('CVE' in REFS_REF_cpe_sh[l] or 'cve'in REFS_REF_cpe_sh[l]):
                externalreferenceid_REFS_REF_sh.append(REFS_REF_cpe_sh[l])
        
                
        #Si en la fila de la columna REFS_REF hay algun valor que incluye la cadena EXTERNAL_REFERENCEID, la insertamos en el array general de EXTERNAL_REFERENCEIDS de la columna REFS_REF
        if(len(externalreferenceid_REFS_REF_sh)>0):
            for y in range(0,len(externalreferenceid_REFS_REF_sh)):
                #Si aparte del ID del EXTERNAL_REFERENCEID viene alguna cadena de texto mas
                arrayaux=externalreferenceid_REFS_REF_sh[y].split("-")
                for i in range(0,len(arrayaux)):
                    #Recorremos el string hasta que encontramos el anio que forma parte del ID del EXTERNAL_REFERENCEID
                    if(arrayaux[i][0] == '2' and arrayaux[i][1] == '0' and (arrayaux[i][2] == '2' or arrayaux[i][2] == '1')):
                        #Creamos el string con el id del EXTERNAL_REFERENCEID
                        strax="CVE-"+arrayaux[i]+"-"+arrayaux[i+1]
                        #Comprobamos si la subcadena que viene despues del anio del ID del EXTERNAL_REFERENCEID es de longitud mayor que 4
                        if(len(arrayaux[i+1])>4):

                            #Comprobamos si el caracter siguiente es un numero o una letra
                            if(arrayaux[i+1][4] == '0' or arrayaux[i+1][4] == '1' or arrayaux[i+1][4] == '2' or arrayaux[i+1][4] == '3' or arrayaux[i+1][4] == '4' or arrayaux[i+1][4] == '5' or arrayaux[i+1][4] == '6' or arrayaux[i+1][4] == '7' or arrayaux[i+1][4] == '8' or arrayaux[i+1][4] == '9' ):
                                #Comprobamos si la subcadena posterior al anio del ID del EXTERNAL_REFERENCEID es de largo mayor que 5
                                if(len(arrayaux[i+1])>5):
                                    #Comprobamos si el caracter siguiente es un numero o letra
                                    if(arrayaux[i+1][5] == '0' or arrayaux[i+1][5] == '1' or arrayaux[i+1][5] == '2' or arrayaux[i+1][5] == '3' or arrayaux[i+1][5] == '4' or arrayaux[i+1][5] == '5' or arrayaux[i+1][5] == '6' or arrayaux[i+1][5] == '7' or arrayaux[i+1][5] == '8' or arrayaux[i+1][5] == '9' ):
                                        print("@")
                                        print(strax[0:13])
                                    else:
                                        #Si el siguiente caracter es una letra, dejamos de recorrer el string
                                        if(strax[0:14] not in externalreferenceid_REFS_REF_cpe_sh):
                                            externalreferenceid_REFS_REF_cpe_sh.append(strax[0:14])
                                else:
                                    if(strax[0:14] not in externalreferenceid_REFS_REF_cpe_sh):
                                        externalreferenceid_REFS_REF_cpe_sh.append(strax[0:14])
                            else:
                                #Dejamos de recorrer el string cuando encontremos una letra y no una cifra
                                if(strax[0:13] not in externalreferenceid_REFS_REF_cpe_sh):
                                    externalreferenceid_REFS_REF_cpe_sh.append(strax[0:13])
                        else:
                            #Insertamos el ID del EXTERNAL_REFERENCEID si el largo del substring posterior al anio del ID del EXTERNAL_REFERENCEID es de longitud 4 o menor
                            if(strax not in externalreferenceid_REFS_REF_cpe_sh):
                                externalreferenceid_REFS_REF_cpe_sh.append(strax)                                   
#Comprobamos los EXTERNAL_REFERENCEIDS IDS coincidentes entre cpe y EXTERNAL_REFERENCEID
if(len(externalreferenceid_REFS_REF_cpe_sh)>0) :   
    #Recorro los IDS de la vulnerabilidades en el excel de EXTERNAL_REFERENCEIDS
    for w in range(0,len(df_vulnibm_sh["external_references_external_id"])):
        if((df_vulnibm_sh["external_references_external_id"][w].replace('[','').replace(']','').replace("'","").replace("","").replace(" ","")) in externalreferenceid_REFS_REF_cpe_sh):
            externalreferenceid_REFS_REFs_coincidentes_cpe_sh.append(df_vulnibm_sh["external_references_external_id"][w].replace('[','').replace(']','').replace("'","").replace("","").replace(" ",""))

print("\n")
#Si hemos encontrado EXTERNAL_REFERENCEIDS coincidentes en la columna REFS_REF de cpe, los imprimo por pantalla
if(len(externalreferenceid_REFS_REFs_coincidentes_cpe_sh)>0):
    print("EXISTEN "+str(len(externalreferenceid_REFS_REFs_coincidentes_cpe_sh))+"IDS DE REFERENCIAS EXTERNAS IBM COINCIDENTES O CONTENIDOS EN LAS FUENTES DE REFERENCIA DE CPE DE LA PARTE DE SMART HOME ")
    print("\n")
    for t in range(0,len(externalreferenceid_REFS_REFs_coincidentes_cpe_sh)):
        print("- "+externalreferenceid_REFS_REFs_coincidentes_cpe_sh[t])
        print("\n")
        
else:
    print("NO HAY IDS DE REFERENCIAS EXTERNAS IBM COINCIDENTES O CONTENIDOS EN LAS FUENTES DE REFERENCIA DE CPE DE LA PARTE DE SMART HOME ")
    
    
    
    
    
    
    
    


#Vector donde guardaremos los valores de la columna REFS_REF donde se encuentra algun EXTERNAL_REFERENCEID
externalreferenceid_REFS_REF_cpe_iotsh=[]
#Vector donde guardaremos los valores no duplicados de la columna REFS_REF donde se encuentra algun EXTERNAL_REFERENCEID
externalreferenceid_REFS_REF_cpe_iotsh=[]
#Vector donde guardaremos los EXTERNAL_REFERENCEIDS incluidos en la columna REFS_REF junto con el valor de la columna REFS_REF
externalreferenceid_REFS_REFs_coincidentes_cpe_iotsh=[]
#Vector donde guardaremos los EXTERNAL_REFERENCEIDS incluidos en la columna REFS_REF junto con el valor de la columna REFS_REF, no duplicados
externalreferenceid_REFS_REFs_coincidentes_cpe_iotsh_def=[]



#Recorremos la columna _REFS_REF_ del fichero de cpe IOT
for i in range(0,len(df_cpe_iot["cpes.refs.ref"])):
    #Si el nombre no esta especificado no hago nada
    if(df_cpe_iot["cpes.refs.ref"][i] !='NONE'):
        #Vector donde guardaremos todos los REFS_REFs de la columna
        REFS_REF_cpe_iotsh=[]
        #Compruebo si en cada fila de la columna REFS_REF hay solo un valor o varios
        if((",") in (df_cpe_iot["cpes.refs.ref"][i])):
            #Si hay varios valores de REFS_REF en la misma fila, separo cada uno de los valores
            aux_REFS_REF_cpe_iotsh = df_cpe_iot["cpes.refs.ref"][i].split(',')
            #Inserto cada valor de REFS_REF de cada fila en el vector donde estaran todos los valores de REFS_REF, quitando algunos caracteres especiales y espacios
            for j in range(0,len(aux_REFS_REF_cpe_iotsh)):
                REFS_REF_cpe_iotsh.append(aux_REFS_REF_cpe_iotsh[j].replace('[','').replace(']','').replace("'","").replace(" ",""))
        #Si en la fila hay un solo valor de REFS_REF, inserto directamente ese valor
        else:
            REFS_REF_cpe_iotsh.append(df_cpe_iot["cpes.refs.ref"][i].replace('[','').replace(']','').replace("'","").replace(" ",""))
            
        #Compruebo en todos los valores que hemos insertado de REFS_REF de la correspondiente fila si en alguno viene la cadena _vulnibm_, e inserto esos valores de REFS_REF en el siguiente vector de nombres de EXTERNAL_REFERENCEIDS
        externalreferenceid_REFS_REF_iotsh=[]   
        for l in range(0,len(REFS_REF_cpe_iotsh)):
            if('CVE' in REFS_REF_cpe_iotsh[l] or 'cve'in REFS_REF_cpe_iotsh[l]):
                externalreferenceid_REFS_REF_iotsh.append(REFS_REF_cpe_iotsh[l])
        
                
        #Si en la fila de la columna REFS_REF hay algun valor que incluye la cadena EXTERNAL_REFERENCEID, la insertamos en el array general de EXTERNAL_REFERENCEIDS de la columna REFS_REF
        if(len(externalreferenceid_REFS_REF_iotsh)>0):
            for y in range(0,len(externalreferenceid_REFS_REF_iotsh)):
                #Si aparte del ID del EXTERNAL_REFERENCEID viene alguna cadena de texto mas
                arrayaux=externalreferenceid_REFS_REF_iotsh[y].split("-")
                for i in range(0,len(arrayaux)):
                    #Recorremos el string hasta que encontramos el anio que forma parte del ID del EXTERNAL_REFERENCEID
                    if(arrayaux[i][0] == '2' and arrayaux[i][1] == '0' and (arrayaux[i][2] == '2' or arrayaux[i][2] == '1')):
                        #Creamos el string con el id del EXTERNAL_REFERENCEID
                        strax="CVE-"+arrayaux[i]+"-"+arrayaux[i+1]
                        #Comprobamos si la subcadena que viene despues del anio del ID del EXTERNAL_REFERENCEID es de longitud mayor que 4
                        if(len(arrayaux[i+1])>4):

                            #Comprobamos si el caracter siguiente es un numero o una letra
                            if(arrayaux[i+1][4] == '0' or arrayaux[i+1][4] == '1' or arrayaux[i+1][4] == '2' or arrayaux[i+1][4] == '3' or arrayaux[i+1][4] == '4' or arrayaux[i+1][4] == '5' or arrayaux[i+1][4] == '6' or arrayaux[i+1][4] == '7' or arrayaux[i+1][4] == '8' or arrayaux[i+1][4] == '9' ):
                                #Comprobamos si la subcadena posterior al anio del ID del EXTERNAL_REFERENCEID es de largo mayor que 5
                                if(len(arrayaux[i+1])>5):
                                    #Comprobamos si el caracter siguiente es un numero o letra
                                    if(arrayaux[i+1][5] == '0' or arrayaux[i+1][5] == '1' or arrayaux[i+1][5] == '2' or arrayaux[i+1][5] == '3' or arrayaux[i+1][5] == '4' or arrayaux[i+1][5] == '5' or arrayaux[i+1][5] == '6' or arrayaux[i+1][5] == '7' or arrayaux[i+1][5] == '8' or arrayaux[i+1][5] == '9' ):
                                        print("@")
                                        print(strax[0:13])
                                    else:
                                        #Si el siguiente caracter es una letra, dejamos de recorrer el string
                                        if(strax[0:14] not in externalreferenceid_REFS_REF_cpe_iotsh):
                                            externalreferenceid_REFS_REF_cpe_iotsh.append(strax[0:14])
                                else:
                                    if(strax[0:14] not in externalreferenceid_REFS_REF_cpe_iotsh):
                                        externalreferenceid_REFS_REF_cpe_iotsh.append(strax[0:14])
                            else:
                                #Dejamos de recorrer el string cuando encontremos una letra y no una cifra
                                if(strax[0:13] not in externalreferenceid_REFS_REF_cpe_iotsh):
                                    externalreferenceid_REFS_REF_cpe_iotsh.append(strax[0:13])
                        else:
                            #Insertamos el ID del EXTERNAL_REFERENCEID si el largo del substring posterior al anio del ID del EXTERNAL_REFERENCEID es de longitud 4 o menor
                            if(strax not in externalreferenceid_REFS_REF_cpe_iotsh):
                                externalreferenceid_REFS_REF_cpe_iotsh.append(strax)                                   
#Comprobamos los EXTERNAL_REFERENCEIDS IDS coincidentes entre cpe y EXTERNAL_REFERENCEID
if(len(externalreferenceid_REFS_REF_cpe_iotsh)>0) :   
    #Recorro los IDS de la vulnerabilidades en el excel de EXTERNAL_REFERENCEIDS
    for w in range(0,len(df_vulnibm_sh["external_references_external_id"])):
        if((df_vulnibm_sh["external_references_external_id"][w].replace('[','').replace(']','').replace("'","").replace("","").replace(" ","")) in externalreferenceid_REFS_REF_cpe_iotsh):
            externalreferenceid_REFS_REFs_coincidentes_cpe_iotsh.append(df_vulnibm_sh["external_references_external_id"][w].replace('[','').replace(']','').replace("'","").replace("","").replace(" ",""))

print("\n")
print("\n")
#Si hemos encontrado EXTERNAL_REFERENCEIDS coincidentes en la columna REFS_REF de cpe, los imprimo por pantalla
if(len(externalreferenceid_REFS_REFs_coincidentes_cpe_iotsh)>0):
    print("EXISTEN "+str(len(externalreferenceid_REFS_REFs_coincidentes_cpe_iotsh))+" IDS DE REFERENCIAS EXTERNAS IBM DE LA RAMA DE SMART HOME COINCIDENTES O CONTENIDOS EN LAS FUENTES DE REFERENCIA DE CPE DE LA PARTE DE IOT ")
    print("\n")
    for t in range(0,len(externalreferenceid_REFS_REFs_coincidentes_cpe_iotsh)):
        print("- "+externalreferenceid_REFS_REFs_coincidentes_cpe_iotsh[t])
        print("\n")
        
else:
    print("NO HAY IDS DE REFERENCIAS EXTERNAS IBM DE LA RAMA DE SMART HOME COINCIDENTES O CONTENIDOS EN LAS FUENTES DE REFERENCIA DE CPE DE LA PARTE DE IOT ")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    


#Vector donde guardaremos los valores de la columna REFS_REF donde se encuentra algun EXTERNAL_REFERENCEID
externalreferenceid_REFS_REF_cpe_shiot=[]
#Vector donde guardaremos los valores no duplicados de la columna REFS_REF donde se encuentra algun EXTERNAL_REFERENCEID
externalreferenceid_REFS_REF_cpe_shiot=[]
#Vector donde guardaremos los EXTERNAL_REFERENCEIDS incluidos en la columna REFS_REF junto con el valor de la columna REFS_REF
externalreferenceid_REFS_REFs_coincidentes_cpe_shiot=[]
#Vector donde guardaremos los EXTERNAL_REFERENCEIDS incluidos en la columna REFS_REF junto con el valor de la columna REFS_REF, no duplicados
externalreferenceid_REFS_REFs_coincidentes_cpe_shiot_def=[]



#Recorremos la columna _REFS_REF_ del fichero de cpe SMART HOME
for i in range(0,len(df_cpe_sh["cpes.refs.ref"])):
    #Si el nombre no esta especificado no hago nada
    if(df_cpe_sh["cpes.refs.ref"][i] !='NONE'):
        #Vector donde guardaremos todos los REFS_REFs de la columna
        REFS_REF_cpe_shiot=[]
        #Compruebo si en cada fila de la columna REFS_REF hay solo un valor o varios
        if((",") in (df_cpe_sh["cpes.refs.ref"][i])):
            #Si hay varios valores de REFS_REF en la misma fila, separo cada uno de los valores
            aux_REFS_REF_cpe_shiot = df_cpe_sh["cpes.refs.ref"][i].split(',')
            #Inserto cada valor de REFS_REF de cada fila en el vector donde estaran todos los valores de REFS_REF, quitando algunos caracteres especiales y espacios
            for j in range(0,len(aux_REFS_REF_cpe_shiot)):
                REFS_REF_cpe_shiot.append(aux_REFS_REF_cpe_shiot[j].replace('[','').replace(']','').replace("'","").replace(" ",""))
        #Si en la fila hay un solo valor de REFS_REF, inserto directamente ese valor
        else:
            REFS_REF_cpe_shiot.append(df_cpe_sh["cpes.refs.ref"][i].replace('[','').replace(']','').replace("'","").replace(" ",""))
            
        #Compruebo en todos los valores que hemos insertado de REFS_REF de la correspondiente fila si en alguno viene la cadena _vulnibm_, e inserto esos valores de REFS_REF en el siguiente vector de nombres de EXTERNAL_REFERENCEIDS
        externalreferenceid_REFS_REF_shiot=[]   
        for l in range(0,len(REFS_REF_cpe_shiot)):
            if('CVE' in REFS_REF_cpe_shiot[l] or 'cve'in REFS_REF_cpe_shiot[l]):
                externalreferenceid_REFS_REF_shiot.append(REFS_REF_cpe_shiot[l])
        
                
        #Si en la fila de la columna REFS_REF hay algun valor que incluye la cadena EXTERNAL_REFERENCEID, la insertamos en el array general de EXTERNAL_REFERENCEIDS de la columna REFS_REF
        if(len(externalreferenceid_REFS_REF_shiot)>0):
            for y in range(0,len(externalreferenceid_REFS_REF_shiot)):
                #Si aparte del ID del EXTERNAL_REFERENCEID viene alguna cadena de texto mas
                arrayaux=externalreferenceid_REFS_REF_shiot[y].split("-")
                for i in range(0,len(arrayaux)):
                    #Recorremos el string hasta que encontramos el anio que forma parte del ID del EXTERNAL_REFERENCEID
                    if(arrayaux[i][0] == '2' and arrayaux[i][1] == '0' and (arrayaux[i][2] == '2' or arrayaux[i][2] == '1')):
                        #Creamos el string con el id del EXTERNAL_REFERENCEID
                        strax="CVE-"+arrayaux[i]+"-"+arrayaux[i+1]
                        #Comprobamos si la subcadena que viene despues del anio del ID del EXTERNAL_REFERENCEID es de longitud mayor que 4
                        if(len(arrayaux[i+1])>4):

                            #Comprobamos si el caracter siguiente es un numero o una letra
                            if(arrayaux[i+1][4] == '0' or arrayaux[i+1][4] == '1' or arrayaux[i+1][4] == '2' or arrayaux[i+1][4] == '3' or arrayaux[i+1][4] == '4' or arrayaux[i+1][4] == '5' or arrayaux[i+1][4] == '6' or arrayaux[i+1][4] == '7' or arrayaux[i+1][4] == '8' or arrayaux[i+1][4] == '9' ):
                                #Comprobamos si la subcadena posterior al anio del ID del EXTERNAL_REFERENCEID es de largo mayor que 5
                                if(len(arrayaux[i+1])>5):
                                    #Comprobamos si el caracter siguiente es un numero o letra
                                    if(arrayaux[i+1][5] == '0' or arrayaux[i+1][5] == '1' or arrayaux[i+1][5] == '2' or arrayaux[i+1][5] == '3' or arrayaux[i+1][5] == '4' or arrayaux[i+1][5] == '5' or arrayaux[i+1][5] == '6' or arrayaux[i+1][5] == '7' or arrayaux[i+1][5] == '8' or arrayaux[i+1][5] == '9' ):
                                        print("@")
                                        print(strax[0:13])
                                    else:
                                        #Si el siguiente caracter es una letra, dejamos de recorrer el string
                                        if(strax[0:14] not in externalreferenceid_REFS_REF_cpe_shiot):
                                            externalreferenceid_REFS_REF_cpe_shiot.append(strax[0:14])
                                else:
                                    if(strax[0:14] not in externalreferenceid_REFS_REF_cpe_shiot):
                                        externalreferenceid_REFS_REF_cpe_shiot.append(strax[0:14])
                            else:
                                #Dejamos de recorrer el string cuando encontremos una letra y no una cifra
                                if(strax[0:13] not in externalreferenceid_REFS_REF_cpe_shiot):
                                    externalreferenceid_REFS_REF_cpe_shiot.append(strax[0:13])
                        else:
                            #Insertamos el ID del EXTERNAL_REFERENCEID si el largo del substring posterior al anio del ID del EXTERNAL_REFERENCEID es de longitud 4 o menor
                            if(strax not in externalreferenceid_REFS_REF_cpe_shiot):
                                externalreferenceid_REFS_REF_cpe_shiot.append(strax)                                   
#Comprobamos los EXTERNAL_REFERENCEIDS IDS coincidentes entre cpe y EXTERNAL_REFERENCEID
if(len(externalreferenceid_REFS_REF_cpe_shiot)>0) :   
    #Recorro los IDS de la vulnerabilidades en el excel de EXTERNAL_REFERENCEIDS
    for w in range(0,len(df_vulnibm_iot["external_references_external_id"])):
        if((df_vulnibm_iot["external_references_external_id"][w].replace('[','').replace(']','').replace("'","").replace("","").replace(" ","")) in externalreferenceid_REFS_REF_cpe_shiot):
            externalreferenceid_REFS_REFs_coincidentes_cpe_shiot.append(df_vulnibm_iot["external_references_external_id"][w].replace('[','').replace(']','').replace("'","").replace("","").replace(" ",""))

print("\n")
print("\n")
#Si hemos encontrado EXTERNAL_REFERENCEIDS coincidentes en la columna REFS_REF de cpe, los imprimo por pantalla
if(len(externalreferenceid_REFS_REFs_coincidentes_cpe_shiot)>0):
    print("EXISTEN "+str(len(externalreferenceid_REFS_REFs_coincidentes_cpe_shiot))+" IDS DE REFERENCIAS EXTERNAS IBM DE LA RAMA DE IOT COINCIDENTES O CONTENIDOS EN LAS FUENTES DE REFERENCIA DE CPE DE LA PARTE DE SMART HOME ")
    print("\n")
    for t in range(0,len(externalreferenceid_REFS_REFs_coincidentes_cpe_shiot)):
        print("- "+externalreferenceid_REFS_REFs_coincidentes_cpe_shiot[t])
        print("\n")
        
else:
    print("NO HAY IDS DE REFERENCIAS EXTERNAS IBM DE LA RAMA DE IOT COINCIDENTES O CONTENIDOS EN LAS FUENTES DE REFERENCIA DE CPE DE LA PARTE DE SMART HOME ")
    
    
    
    
    
    
    
    
    


