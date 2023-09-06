



import pandas as pd

df_sector_iot=pd.read_excel('ibm_sector_v2.xlsx')
df_cve_iot=pd.read_excel('cves_iot_2023.xlsx')


#Vector donde guardaremos los valores de la columna NAME donde se encuentra algun CVE
cves_NAME_sector_iot=[]
#Vector donde guardaremos los valores no duplicados de la columna NAME donde se encuentra algun CVE
cves_NAME_sector_iot=[]
#Vector donde guardaremos los CVES incluidos en la columna NAME junto con el valor de la columna NAME
cves_names_coincidentes_sector_iot=[]
#Vector donde guardaremos los CVES incluidos en la columna NAME junto con el valor de la columna NAME, no duplicados
cves_names_coincidentes_sector_iot_def=[]



#Recorremos la columna _NAME_ del fichero de SECTOR IBM iot
for i in range(0,len(df_sector_iot["name"])):
    #Si el nombre no esta especificado no hago nada
    if(df_sector_iot["name"][i] !='NONE'):
        #Vector donde guardaremos todos los NAMEs de la columna
        NAME_sector_iot=[]
        #Compruebo si en cada fila de la columna NAME hay solo un valor o varios
        if((",") in (df_sector_iot["name"][i])):
            #Si hay varios valores de NAME en la misma fila, separo cada uno de los valores
            aux_NAME_sector_iot = df_sector_iot["name"][i].split(',')
            #Inserto cada valor de NAME de cada fila en el vector donde estaran todos los valores de NAME, quitando algunos caracteres especiales y espacios
            for j in range(0,len(aux_NAME_sector_iot)):
                NAME_sector_iot.append(aux_NAME_sector_iot[j].replace('[','').replace(']','').replace("'","").replace(" ",""))
        #Si en la fila hay un solo valor de NAME, inserto directamente ese valor
        else:
            NAME_sector_iot.append(df_sector_iot["name"][i].replace('[','').replace(']','').replace("'","").replace(" ",""))
            
        #Compruebo en todos los valores que hemos insertado de NAME de la correspondiente fila si en alguno viene la cadena _CVE_, e inserto esos valores de NAME en el siguiente vector de nombres de CVES
        cves_NAME_iot=[]   
        for l in range(0,len(NAME_sector_iot)):
            if('CVE' in NAME_sector_iot[l] or 'cve'in NAME_sector_iot[l]):
                cves_NAME_iot.append(NAME_sector_iot[l])
        
                
        #Si en la fila de la columna NAME hay algun valor que incluye la cadena CVE, la insertamos en el array general de CVES de la columna NAME
        if(len(cves_NAME_iot)>0):
            for y in range(0,len(cves_NAME_iot)):
                #Si aparte del ID del CVE viene alguna cadena de texto mas
                arrayaux=cves_NAME_iot[y].split("-")
                for i in range(0,len(arrayaux)):
                    if(len(arrayaux[i])==4):
                        #Recorremos el string hasta que encontramos el anio que forma parte del ID del CVE
                        if(arrayaux[i][0] == '2' and arrayaux[i][1] == '0' and (arrayaux[i][2] == '2' or arrayaux[i][2] == '1')):
                            #Creamos el string con el id del CVE
                            strax="CVE-"+arrayaux[i]+"-"+arrayaux[i+1]
                            #Comprobamos si la subcadena que viene despues del anio del ID del CVE es de longitud mayor que 4
                            if(len(arrayaux[i+1])>4):

                                #Comprobamos si el caracter siguiente es un numero o una letra
                                if(arrayaux[i+1][4] == '0' or arrayaux[i+1][4] == '1' or arrayaux[i+1][4] == '2' or arrayaux[i+1][4] == '3' or arrayaux[i+1][4] == '4' or arrayaux[i+1][4] == '5' or arrayaux[i+1][4] == '6' or arrayaux[i+1][4] == '7' or arrayaux[i+1][4] == '8' or arrayaux[i+1][4] == '9' ):
                                    #Comprobamos si la subcadena posterior al anio del ID del CVE es de largo mayor que 5
                                    if(len(arrayaux[i+1])>5):
                                        #Comprobamos si el caracter siguiente es un numero o letra
                                        if(arrayaux[i+1][5] == '0' or arrayaux[i+1][5] == '1' or arrayaux[i+1][5] == '2' or arrayaux[i+1][5] == '3' or arrayaux[i+1][5] == '4' or arrayaux[i+1][5] == '5' or arrayaux[i+1][5] == '6' or arrayaux[i+1][5] == '7' or arrayaux[i+1][5] == '8' or arrayaux[i+1][5] == '9' ):
                                            print("@")
                                            print(strax[0:13])
                                        else:
                                            #Si el siguiente caracter es una letra, dejamos de recorrer el string
                                            if(strax[0:14] not in cves_NAME_sector_iot):
                                                cves_NAME_sector_iot.append(strax[0:14])
                                    else:
                                        if(strax[0:14] not in cves_NAME_sector_iot):
                                            cves_NAME_sector_iot.append(strax[0:14])
                                else:
                                    #Dejamos de recorrer el string cuando encontremos una letra y no una cifra
                                    if(strax[0:13] not in cves_NAME_sector_iot):
                                        cves_NAME_sector_iot.append(strax[0:13])
                            else:
                                #Insertamos el ID del CVE si el largo del substring posterior al anio del ID del CVE es de longitud 4 o menor
                                if(strax not in cves_NAME_sector_iot):
                                    cves_NAME_sector_iot.append(strax)                                   
#Comprobamos los CVES IDS coincidentes entre SECTOR IBM y CVE
if(len(cves_NAME_sector_iot)>0) :   
    #Recorro los IDS de la vulnerabilidades en el excel de CVES
    for w in range(0,len(df_cve_iot["CVE_Items.cve.CVE_data_meta.ID"])):
        if((df_cve_iot["CVE_Items.cve.CVE_data_meta.ID"][w].replace('[','').replace(']','').replace("'","").replace("","").replace(" ","")) in cves_NAME_sector_iot):
            cves_names_coincidentes_sector_iot.append(df_cve_iot["CVE_Items.cve.CVE_data_meta.ID"][w].replace('[','').replace(']','').replace("'","").replace("","").replace(" ",""))


#Si hemos encontrado CVES coincidentes en la columna NAME de SECTOR IBM, los imprimo por pantalla
if(len(cves_names_coincidentes_sector_iot)>0):
    print("EXISTEN "+str(len(cves_names_coincidentes_sector_iot))+" CVES CONTENIDOS EN LA COLUMNA NAME DE SECTOR IBM IOT :")
    print("\n")
    for t in range(0,len(cves_names_coincidentes_sector_iot)):
        print("- "+cves_names_coincidentes_sector_iot[t])
        print("\n")
        
else:
    print("NO HAY IDENTIFICADORES DE CVES CONTENIDOS O COINCIDENTES EN EL NOMBRE DE OBJETO DE INFORMES DE SECTOR DE IBM LA RAMA IOT")
    
    
    
    
    
    
    


df_sector_sh=pd.read_excel('ibm_sector_v2.xlsx')
df_cve_sh=pd.read_excel('cves_smart_home_2023.xlsx')


#Vector donde guardaremos los valores de la columna NAME donde se encuentra algun CVE
cves_NAME_sector_sh=[]
#Vector donde guardaremos los valores no duplicados de la columna NAME donde se encuentra algun CVE
cves_NAME_sector_sh=[]
#Vector donde guardaremos los CVES incluidos en la columna NAME junto con el valor de la columna NAME
cves_names_coincidentes_sector_sh=[]
#Vector donde guardaremos los CVES incluidos en la columna NAME junto con el valor de la columna NAME, no duplicados
cves_names_coincidentes_sector_sh_def=[]



#Recorremos la columna _NAME_ del fichero de SECTOR IBM SMART HOME
for i in range(0,len(df_sector_sh["name"])):
    #Si el nombre no esta especificado no hago nada
    if(df_sector_sh["name"][i] !='NONE'):
        #Vector donde guardaremos todos los NAMEs de la columna
        NAME_sector_sh=[]
        #Compruebo si en cada fila de la columna NAME hay solo un valor o varios
        if((",") in (df_sector_sh["name"][i])):
            #Si hay varios valores de NAME en la misma fila, separo cada uno de los valores
            aux_NAME_sector_sh = df_sector_sh["name"][i].split(',')
            #Inserto cada valor de NAME de cada fila en el vector donde estaran todos los valores de NAME, quitando algunos caracteres especiales y espacios
            for j in range(0,len(aux_NAME_sector_sh)):
                NAME_sector_sh.append(aux_NAME_sector_sh[j].replace('[','').replace(']','').replace("'","").replace(" ",""))
        #Si en la fila hay un solo valor de NAME, inserto directamente ese valor
        else:
            NAME_sector_sh.append(df_sector_sh["name"][i].replace('[','').replace(']','').replace("'","").replace(" ",""))
            
        #Compruebo en todos los valores que hemos insertado de NAME de la correspondiente fila si en alguno viene la cadena _CVE_, e inserto esos valores de NAME en el siguiente vector de nombres de CVES
        cves_NAME_sh=[]   
        for l in range(0,len(NAME_sector_sh)):
            if('CVE' in NAME_sector_sh[l] or 'cve'in NAME_sector_sh[l]):
                cves_NAME_sh.append(NAME_sector_sh[l])
        
                
        #Si en la fila de la columna NAME hay algun valor que incluye la cadena CVE, la insertamos en el array general de CVES de la columna NAME
        if(len(cves_NAME_sh)>0):
            for y in range(0,len(cves_NAME_sh)):
                #Si aparte del ID del CVE viene alguna cadena de texto mas
                arrayaux=cves_NAME_sh[y].split("-")
                for i in range(0,len(arrayaux)):
                    if(len(arrayaux[i])==4):
                        #Recorremos el string hasta que encontramos el anio que forma parte del ID del CVE
                        if(arrayaux[i][0] == '2' and arrayaux[i][1] == '0' and (arrayaux[i][2] == '2' or arrayaux[i][2] == '1')):
                            #Creamos el string con el id del CVE
                            strax="CVE-"+arrayaux[i]+"-"+arrayaux[i+1]
                            #Comprobamos si la subcadena que viene despues del anio del ID del CVE es de longitud mayor que 4
                            if(len(arrayaux[i+1])>4):

                                #Comprobamos si el caracter siguiente es un numero o una letra
                                if(arrayaux[i+1][4] == '0' or arrayaux[i+1][4] == '1' or arrayaux[i+1][4] == '2' or arrayaux[i+1][4] == '3' or arrayaux[i+1][4] == '4' or arrayaux[i+1][4] == '5' or arrayaux[i+1][4] == '6' or arrayaux[i+1][4] == '7' or arrayaux[i+1][4] == '8' or arrayaux[i+1][4] == '9' ):
                                    #Comprobamos si la subcadena posterior al anio del ID del CVE es de largo mayor que 5
                                    if(len(arrayaux[i+1])>5):
                                        #Comprobamos si el caracter siguiente es un numero o letra
                                        if(arrayaux[i+1][5] == '0' or arrayaux[i+1][5] == '1' or arrayaux[i+1][5] == '2' or arrayaux[i+1][5] == '3' or arrayaux[i+1][5] == '4' or arrayaux[i+1][5] == '5' or arrayaux[i+1][5] == '6' or arrayaux[i+1][5] == '7' or arrayaux[i+1][5] == '8' or arrayaux[i+1][5] == '9' ):
                                            print("@")
                                            print(strax[0:13])
                                        else:
                                            #Si el siguiente caracter es una letra, dejamos de recorrer el string
                                            if(strax[0:14] not in cves_NAME_sector_sh):
                                                cves_NAME_sector_sh.append(strax[0:14])
                                    else:
                                        if(strax[0:14] not in cves_NAME_sector_sh):
                                            cves_NAME_sector_sh.append(strax[0:14])
                                else:
                                    #Dejamos de recorrer el string cuando encontremos una letra y no una cifra
                                    if(strax[0:13] not in cves_NAME_sector_sh):
                                        cves_NAME_sector_sh.append(strax[0:13])
                            else:
                                #Insertamos el ID del CVE si el largo del substring posterior al anio del ID del CVE es de longitud 4 o menor
                                if(strax not in cves_NAME_sector_sh):
                                    cves_NAME_sector_sh.append(strax)                                   
#Comprobamos los CVES IDS coincidentes entre SECTOR IBM y CVE
if(len(cves_NAME_sector_sh)>0) :   
    #Recorro los IDS de la vulnerabilidades en el excel de CVES
    for w in range(0,len(df_cve_sh["CVE_Items.cve.CVE_data_meta.ID"])):
        if((df_cve_sh["CVE_Items.cve.CVE_data_meta.ID"][w].replace('[','').replace(']','').replace("'","").replace("","").replace(" ","")) in cves_NAME_sector_sh):
            cves_names_coincidentes_sector_sh.append(df_cve_sh["CVE_Items.cve.CVE_data_meta.ID"][w].replace('[','').replace(']','').replace("'","").replace("","").replace(" ",""))


#Si hemos encontrado CVES coincidentes en la columna NAME de SECTOR IBM, los imprimo por pantalla
if(len(cves_names_coincidentes_sector_sh)>0):
    print("EXISTEN "+str(len(cves_names_coincidentes_sector_sh))+" CVES CONTENIDOS EN LA COLUMNA NAME DE SECTOR IBM SMART HOME :")
    print("\n")
    for t in range(0,len(cves_names_coincidentes_sector_sh)):
        print("- "+cves_names_coincidentes_sector_sh[t])
        print("\n")
        
else:
    print("NO HAY IDENTIFICADORES DE CVES CONTENIDOS O COINCIDENTES EN EL NOMBRE DE OBJETO DE INFORMES DE SECTOR DE IBM LA RAMA SMART HOME")
    
    
    
    
    
    
    
    


#Vector donde guardaremos los valores de la columna NAME donde se encuentra algun CVE
cves_NAME_sector_iotsh=[]
#Vector donde guardaremos los valores no duplicados de la columna NAME donde se encuentra algun CVE
cves_NAME_sector_iotsh=[]
#Vector donde guardaremos los CVES incluidos en la columna NAME junto con el valor de la columna NAME
cves_names_coincidentes_sector_iotsh=[]
#Vector donde guardaremos los CVES incluidos en la columna NAME junto con el valor de la columna NAME, no duplicados
cves_names_coincidentes_sector_iotsh_def=[]



#Recorremos la columna _NAME_ del fichero de SECTOR IBM IOT
for i in range(0,len(df_sector_iot["name"])):
    #Si el nombre no esta especificado no hago nada
    if(df_sector_iot["name"][i] !='NONE'):
        #Vector donde guardaremos todos los NAMEs de la columna
        NAME_sector_iotsh=[]
        #Compruebo si en cada fila de la columna NAME hay solo un valor o varios
        if((",") in (df_sector_iot["name"][i])):
            #Si hay varios valores de NAME en la misma fila, separo cada uno de los valores
            aux_NAME_sector_iotsh = df_sector_iot["name"][i].split(',')
            #Inserto cada valor de NAME de cada fila en el vector donde estaran todos los valores de NAME, quitando algunos caracteres especiales y espacios
            for j in range(0,len(aux_NAME_sector_iotsh)):
                NAME_sector_iotsh.append(aux_NAME_sector_iotsh[j].replace('[','').replace(']','').replace("'","").replace(" ",""))
        #Si en la fila hay un solo valor de NAME, inserto directamente ese valor
        else:
            NAME_sector_iotsh.append(df_sector_iot["name"][i].replace('[','').replace(']','').replace("'","").replace(" ",""))
            
        #Compruebo en todos los valores que hemos insertado de NAME de la correspondiente fila si en alguno viene la cadena _CVE_, e inserto esos valores de NAME en el siguiente vector de nombres de CVES
        cves_NAME_iotsh=[]   
        for l in range(0,len(NAME_sector_iotsh)):
            if('CVE' in NAME_sector_iotsh[l] or 'cve'in NAME_sector_iotsh[l]):
                cves_NAME_iotsh.append(NAME_sector_iotsh[l])
        
                
        #Si en la fila de la columna NAME hay algun valor que incluye la cadena CVE, la insertamos en el array general de CVES de la columna NAME
        if(len(cves_NAME_iotsh)>0):
            for y in range(0,len(cves_NAME_iotsh)):
                #Si aparte del ID del CVE viene alguna cadena de texto mas
                arrayaux=cves_NAME_iotsh[y].split("-")
                for i in range(0,len(arrayaux)):
                    if(len(arrayaux[i])==4):
                        #Recorremos el string hasta que encontramos el anio que forma parte del ID del CVE
                        if(arrayaux[i][0] == '2' and arrayaux[i][1] == '0' and (arrayaux[i][2] == '2' or arrayaux[i][2] == '1')):
                            #Creamos el string con el id del CVE
                            strax="CVE-"+arrayaux[i]+"-"+arrayaux[i+1]
                            #Comprobamos si la subcadena que viene despues del anio del ID del CVE es de longitud mayor que 4
                            if(len(arrayaux[i+1])>4):

                                #Comprobamos si el caracter siguiente es un numero o una letra
                                if(arrayaux[i+1][4] == '0' or arrayaux[i+1][4] == '1' or arrayaux[i+1][4] == '2' or arrayaux[i+1][4] == '3' or arrayaux[i+1][4] == '4' or arrayaux[i+1][4] == '5' or arrayaux[i+1][4] == '6' or arrayaux[i+1][4] == '7' or arrayaux[i+1][4] == '8' or arrayaux[i+1][4] == '9' ):
                                    #Comprobamos si la subcadena posterior al anio del ID del CVE es de largo mayor que 5
                                    if(len(arrayaux[i+1])>5):
                                        #Comprobamos si el caracter siguiente es un numero o letra
                                        if(arrayaux[i+1][5] == '0' or arrayaux[i+1][5] == '1' or arrayaux[i+1][5] == '2' or arrayaux[i+1][5] == '3' or arrayaux[i+1][5] == '4' or arrayaux[i+1][5] == '5' or arrayaux[i+1][5] == '6' or arrayaux[i+1][5] == '7' or arrayaux[i+1][5] == '8' or arrayaux[i+1][5] == '9' ):
                                            print("@")
                                            print(strax[0:13])
                                        else:
                                            #Si el siguiente caracter es una letra, dejamos de recorrer el string
                                            if(strax[0:14] not in cves_NAME_sector_iotsh):
                                                cves_NAME_sector_iotsh.append(strax[0:14])
                                    else:
                                        if(strax[0:14] not in cves_NAME_sector_iotsh):
                                            cves_NAME_sector_iotsh.append(strax[0:14])
                                else:
                                    #Dejamos de recorrer el string cuando encontremos una letra y no una cifra
                                    if(strax[0:13] not in cves_NAME_sector_iotsh):
                                        cves_NAME_sector_iotsh.append(strax[0:13])
                            else:
                                #Insertamos el ID del CVE si el largo del substring posterior al anio del ID del CVE es de longitud 4 o menor
                                if(strax not in cves_NAME_sector_iotsh):
                                    cves_NAME_sector_iotsh.append(strax)                                   
#Comprobamos los CVES IDS coincidentes entre SECTOR IBM y CVE
if(len(cves_NAME_sector_iotsh)>0) :   
    #Recorro los IDS de la vulnerabilidades en el excel de CVES
    for w in range(0,len(df_cve_sh["CVE_Items.cve.CVE_data_meta.ID"])):
        if((df_cve_sh["CVE_Items.cve.CVE_data_meta.ID"][w].replace('[','').replace(']','').replace("'","").replace("","").replace(" ","")) in cves_NAME_sector_iotsh):
            cves_names_coincidentes_sector_iotsh.append(df_cve_sh["CVE_Items.cve.CVE_data_meta.ID"][w].replace('[','').replace(']','').replace("'","").replace("","").replace(" ",""))


#Si hemos encontrado CVES coincidentes en la columna NAME de SECTOR IBM, los imprimo por pantalla
if(len(cves_names_coincidentes_sector_iotsh)>0):
    print("EXISTEN "+str(len(cves_names_coincidentes_sector_iotsh))+" CVES DE LA RAMA DE SMART HOME CONTENIDOS EN LA COLUMNA NAME DE LA PARTE DE  IOT  :")
    print("\n")
    for t in range(0,len(cves_names_coincidentes_sector_iotsh)):
        print("- "+cves_names_coincidentes_sector_iotsh[t])
        print("\n")
        
else:
    print("NO HAY IDENTIFICADORES DE CVES DE LA PARTE SMART HOME CONTENIDOS O COINCIDENTES EN EL NOMBRE DE OBJETO DE INFORMES DE SECTOR DE IBM LA RAMA IOT")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    


#Vector donde guardaremos los valores de la columna NAME donde se encuentra algun CVE
cves_NAME_sector_shiot=[]
#Vector donde guardaremos los valores no duplicados de la columna NAME donde se encuentra algun CVE
cves_NAME_sector_shiot=[]
#Vector donde guardaremos los CVES incluidos en la columna NAME junto con el valor de la columna NAME
cves_names_coincidentes_sector_shiot=[]
#Vector donde guardaremos los CVES incluidos en la columna NAME junto con el valor de la columna NAME, no duplicados
cves_names_coincidentes_sector_shiot_def=[]



#Recorremos la columna _NAME_ del fichero de SECTOR IBM SMART HOME
for i in range(0,len(df_sector_sh["name"])):
    #Si el nombre no esta especificado no hago nada
    if(df_sector_sh["name"][i] !='NONE'):
        #Vector donde guardaremos todos los NAMEs de la columna
        NAME_sector_shiot=[]
        #Compruebo si en cada fila de la columna NAME hay solo un valor o varios
        if((",") in (df_sector_sh["name"][i])):
            #Si hay varios valores de NAME en la misma fila, separo cada uno de los valores
            aux_NAME_sector_shiot = df_sector_sh["name"][i].split(',')
            #Inserto cada valor de NAME de cada fila en el vector donde estaran todos los valores de NAME, quitando algunos caracteres especiales y espacios
            for j in range(0,len(aux_NAME_sector_shiot)):
                NAME_sector_shiot.append(aux_NAME_sector_shiot[j].replace('[','').replace(']','').replace("'","").replace(" ",""))
        #Si en la fila hay un solo valor de NAME, inserto directamente ese valor
        else:
            NAME_sector_shiot.append(df_sector_sh["name"][i].replace('[','').replace(']','').replace("'","").replace(" ",""))
            
        #Compruebo en todos los valores que hemos insertado de NAME de la correspondiente fila si en alguno viene la cadena _CVE_, e inserto esos valores de NAME en el siguiente vector de nombres de CVES
        cves_NAME_shiot=[]   
        for l in range(0,len(NAME_sector_shiot)):
            if('CVE' in NAME_sector_shiot[l] or 'cve'in NAME_sector_shiot[l]):
                cves_NAME_shiot.append(NAME_sector_shiot[l])
        
                
        #Si en la fila de la columna NAME hay algun valor que incluye la cadena CVE, la insertamos en el array general de CVES de la columna NAME
        if(len(cves_NAME_shiot)>0):
            for y in range(0,len(cves_NAME_shiot)):
                #Si aparte del ID del CVE viene alguna cadena de texto mas
                arrayaux=cves_NAME_shiot[y].split("-")
                for i in range(0,len(arrayaux)):
                    if(len(arrayaux[i])==4):
                        #Recorremos el string hasta que encontramos el anio que forma parte del ID del CVE
                        if(arrayaux[i][0] == '2' and arrayaux[i][1] == '0' and (arrayaux[i][2] == '2' or arrayaux[i][2] == '1')):
                            #Creamos el string con el id del CVE
                            strax="CVE-"+arrayaux[i]+"-"+arrayaux[i+1]
                            #Comprobamos si la subcadena que viene despues del anio del ID del CVE es de longitud mayor que 4
                            if(len(arrayaux[i+1])>4):

                                #Comprobamos si el caracter siguiente es un numero o una letra
                                if(arrayaux[i+1][4] == '0' or arrayaux[i+1][4] == '1' or arrayaux[i+1][4] == '2' or arrayaux[i+1][4] == '3' or arrayaux[i+1][4] == '4' or arrayaux[i+1][4] == '5' or arrayaux[i+1][4] == '6' or arrayaux[i+1][4] == '7' or arrayaux[i+1][4] == '8' or arrayaux[i+1][4] == '9' ):
                                    #Comprobamos si la subcadena posterior al anio del ID del CVE es de largo mayor que 5
                                    if(len(arrayaux[i+1])>5):
                                        #Comprobamos si el caracter siguiente es un numero o letra
                                        if(arrayaux[i+1][5] == '0' or arrayaux[i+1][5] == '1' or arrayaux[i+1][5] == '2' or arrayaux[i+1][5] == '3' or arrayaux[i+1][5] == '4' or arrayaux[i+1][5] == '5' or arrayaux[i+1][5] == '6' or arrayaux[i+1][5] == '7' or arrayaux[i+1][5] == '8' or arrayaux[i+1][5] == '9' ):
                                            print("@")
                                            print(strax[0:13])
                                        else:
                                            #Si el siguiente caracter es una letra, dejamos de recorrer el string
                                            if(strax[0:14] not in cves_NAME_sector_shiot):
                                                cves_NAME_sector_shiot.append(strax[0:14])
                                    else:
                                        if(strax[0:14] not in cves_NAME_sector_shiot):
                                            cves_NAME_sector_shiot.append(strax[0:14])
                                else:
                                    #Dejamos de recorrer el string cuando encontremos una letra y no una cifra
                                    if(strax[0:13] not in cves_NAME_sector_shiot):
                                        cves_NAME_sector_shiot.append(strax[0:13])
                            else:
                                #Insertamos el ID del CVE si el largo del substring posterior al anio del ID del CVE es de longitud 4 o menor
                                if(strax not in cves_NAME_sector_shiot):
                                    cves_NAME_sector_shiot.append(strax)                                   
#Comprobamos los CVES IDS coincidentes entre SECTOR IBM y CVE
if(len(cves_NAME_sector_shiot)>0) :   
    #Recorro los IDS de la vulnerabilidades en el excel de CVES
    for w in range(0,len(df_cve_iot["CVE_Items.cve.CVE_data_meta.ID"])):
        if((df_cve_iot["CVE_Items.cve.CVE_data_meta.ID"][w].replace('[','').replace(']','').replace("'","").replace("","").replace(" ","")) in cves_NAME_sector_shiot):
            cves_names_coincidentes_sector_shiot.append(df_cve_iot["CVE_Items.cve.CVE_data_meta.ID"][w].replace('[','').replace(']','').replace("'","").replace("","").replace(" ",""))


#Si hemos encontrado CVES coincidentes en la columna NAME de SECTOR IBM, los imprimo por pantalla
if(len(cves_names_coincidentes_sector_shiot)>0):
    print("EXISTEN "+str(len(cves_names_coincidentes_sector_shiot))+" CVES DE LA RAMA DE IOT CONTENIDOS EN LA COLUMNA NAME DE LA PARTE DE SMART HOME :")
    print("\n")
    for t in range(0,len(cves_names_coincidentes_sector_shiot)):
        print("- "+cves_names_coincidentes_sector_shiot[t])
        print("\n")
        
else:
    print("NO HAY IDENTIFICADORES DE CVES DE LA PARTE IOT CONTENIDOS O COINCIDENTES EN EL NOMBRE DE OBJETO DE INFORMES DE SECTOR DE IBM LA RAMA SMART HOME")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
   