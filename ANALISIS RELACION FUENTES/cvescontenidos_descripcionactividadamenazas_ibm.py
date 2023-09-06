
import pandas as pd

df_thactrep_iot=pd.read_excel('ibm_threat_activity_report_iot_2023_v2.xlsx')
df_cve_iot=pd.read_excel('cves_iot_2023.xlsx')


#Vector donde guardaremos los valores de la columna DESCRIPTION donde se encuentra algun CVE
cves_DESCRIPTION_thactrep_iot=[]
#Vector donde guardaremos los valores no duplicados de la columna DESCRIPTION donde se encuentra algun CVE
cves_DESCRIPTION_thactrep_iot=[]
#Vector donde guardaremos los CVES incluidos en la columna DESCRIPTION junto con el valor de la columna DESCRIPTION
cves_description_coincidentes_thactrep_iot=[]
#Vector donde guardaremos los CVES incluidos en la columna DESCRIPTION junto con el valor de la columna DESCRIPTION, no duplicados
cves_description_coincidentes_thactrep_iot_def=[]



#Recorremos la columna _DESCRIPTION_ del fichero de THREAT ACTIVITY REPORT IBM iot
for i in range(0,len(df_thactrep_iot["description"])):
    #Si el nombre no esta especificado no hago nada
    if(df_thactrep_iot["description"][i] !='NONE'):
        #Vector donde guardaremos todos los DESCRIPTIONs de la columna
        DESCRIPTION_thactrep_iot=[]
        #Compruebo si en cada fila de la columna DESCRIPTION hay solo un valor o varios
        if(isinstance(df_thactrep_iot["description"][i],float) == False):
            if((",") in (df_thactrep_iot["description"][i])):
                #Si hay varios valores de DESCRIPTION en la misma fila, separo cada uno de los valores
                aux_DESCRIPTION_thactrep_iot = df_thactrep_iot["description"][i].split(',')
                #Inserto cada valor de DESCRIPTION de cada fila en el vector donde estaran todos los valores de DESCRIPTION, quitando algunos caracteres especiales y espacios
                for j in range(0,len(aux_DESCRIPTION_thactrep_iot)):
                    DESCRIPTION_thactrep_iot.append(aux_DESCRIPTION_thactrep_iot[j].replace('[','').replace(']','').replace("'","").replace(" ",""))
            #Si en la fila hay un solo valor de DESCRIPTION, inserto directamente ese valor
            else:
                DESCRIPTION_thactrep_iot.append(df_thactrep_iot["description"][i].replace('[','').replace(']','').replace("'","").replace(" ",""))

            #Compruebo en todos los valores que hemos insertado de DESCRIPTION de la correspondiente fila si en alguno viene la cadena _CVE_, e inserto esos valores de DESCRIPTION en el siguiente vector de nombres de CVES
            cves_DESCRIPTION_iot=[]   
            for l in range(0,len(DESCRIPTION_thactrep_iot)):
                if('CVE' in DESCRIPTION_thactrep_iot[l] or 'cve'in DESCRIPTION_thactrep_iot[l]):
                    cves_DESCRIPTION_iot.append(DESCRIPTION_thactrep_iot[l])


            #Si en la fila de la columna DESCRIPTION hay algun valor que incluye la cadena CVE, la insertamos en el array general de CVES de la columna DESCRIPTION
            if(len(cves_DESCRIPTION_iot)>0):
                for y in range(0,len(cves_DESCRIPTION_iot)):
                    #Si aparte del ID del CVE viene alguna cadena de texto mas
                    arrayaux=cves_DESCRIPTION_iot[y].split("-")
                    for i in range(0,len(arrayaux)):

                        if(len(arrayaux[i]) == 4):
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
                                                if(strax[0:14] not in cves_DESCRIPTION_thactrep_iot):
                                                    cves_DESCRIPTION_thactrep_iot.append(strax[0:14])
                                        else:
                                            if(strax[0:14] not in cves_DESCRIPTION_thactrep_iot):
                                                cves_DESCRIPTION_thactrep_iot.append(strax[0:14])
                                    else:
                                        #Dejamos de recorrer el string cuando encontremos una letra y no una cifra
                                        if(strax[0:13] not in cves_DESCRIPTION_thactrep_iot):
                                            cves_DESCRIPTION_thactrep_iot.append(strax[0:13])
                                else:
                                    #Insertamos el ID del CVE si el largo del substring posterior al anio del ID del CVE es de longitud 4 o menor
                                    if(strax not in cves_DESCRIPTION_thactrep_iot):
                                        cves_DESCRIPTION_thactrep_iot.append(strax) 

#Comprobamos los CVES IDS coincidentes entre THREAT ACTIVITY REPORT IBM y CVE
if(len(cves_DESCRIPTION_thactrep_iot)>0) :   
    #Recorro los IDS de la vulnerabilidades en el excel de CVES
    for w in range(0,len(df_cve_iot["CVE_Items.cve.CVE_data_meta.ID"])):
        if((df_cve_iot["CVE_Items.cve.CVE_data_meta.ID"][w].replace('[','').replace(']','').replace("'","").replace("","").replace(" ","")) in cves_DESCRIPTION_thactrep_iot):
            cves_description_coincidentes_thactrep_iot.append(df_cve_iot["CVE_Items.cve.CVE_data_meta.ID"][w].replace('[','').replace(']','').replace("'","").replace("","").replace(" ",""))

print("\n")
#Si hemos encontrado CVES coincidentes en la columna DESCRIPTION de THREAT ACTIVITY REPORT IBM, los imprimo por pantalla
if(len(cves_description_coincidentes_thactrep_iot)>0):
    print("EXISTEN "+str(len(cves_description_coincidentes_thactrep_iot))+" IDENTIFICADORES DE CVES COINCIDENTES O CONTENIDOS EN LA COLUMNA DESCRIPCIÓN DE INFORMES DE ACTIVIDAD DE AMENAZAS IBM  PARA LA PARTE IOT:")
    print("\n")
    for t in range(0,len(cves_description_coincidentes_thactrep_iot)):
        print("- "+cves_description_coincidentes_thactrep_iot[t])
        print("\n")
        
else:
    print("NO HAY IDENTIFICADORES DE CVES COINCIDENTES O CONTENIDOS EN LA COLUMNA DESCRIPCIÓN DE INFORMES DE ACTIVIDAD DE AMENAZAS IBM PARA LA PARTE IOT")
    
    
    
    
    
    
    


df_thactrep_sh=pd.read_excel('ibm_threat_activity_report_smarthome_2023_v2.xlsx')
df_cve_sh=pd.read_excel('cves_smart_home_2023.xlsx')


#Vector donde guardaremos los valores de la columna DESCRIPTION donde se encuentra algun CVE
cves_DESCRIPTION_thactrep_sh=[]
#Vector donde guardaremos los valores no duplicados de la columna DESCRIPTION donde se encuentra algun CVE
cves_DESCRIPTION_thactrep_sh=[]
#Vector donde guardaremos los CVES incluidos en la columna DESCRIPTION junto con el valor de la columna DESCRIPTION
cves_description_coincidentes_thactrep_sh=[]
#Vector donde guardaremos los CVES incluidos en la columna DESCRIPTION junto con el valor de la columna DESCRIPTION, no duplicados
cves_description_coincidentes_thactrep_sh_def=[]



#Recorremos la columna _DESCRIPTION_ del fichero de THREAT ACTIVITY REPORT IBM SMART HOME
for i in range(0,len(df_thactrep_sh["description"])):
    #Si el nombre no esta especificado no hago nada
    if(df_thactrep_sh["description"][i] !='NONE'):
        #Vector donde guardaremos todos los DESCRIPTIONs de la columna
        DESCRIPTION_thactrep_sh=[]
        #Compruebo si en cada fila de la columna DESCRIPTION hay solo un valor o varios
        if(isinstance(df_thactrep_sh["description"][i],float) == False):
            if((",") in (df_thactrep_sh["description"][i])):
                #Si hay varios valores de DESCRIPTION en la misma fila, separo cada uno de los valores
                aux_DESCRIPTION_thactrep_sh = df_thactrep_sh["description"][i].split(',')
                #Inserto cada valor de DESCRIPTION de cada fila en el vector donde estaran todos los valores de DESCRIPTION, quitando algunos caracteres especiales y espacios
                for j in range(0,len(aux_DESCRIPTION_thactrep_sh)):
                    DESCRIPTION_thactrep_sh.append(aux_DESCRIPTION_thactrep_sh[j].replace('[','').replace(']','').replace("'","").replace(" ",""))
            #Si en la fila hay un solo valor de DESCRIPTION, inserto directamente ese valor
            else:
                DESCRIPTION_thactrep_sh.append(df_thactrep_sh["description"][i].replace('[','').replace(']','').replace("'","").replace(" ",""))

            #Compruebo en todos los valores que hemos insertado de DESCRIPTION de la correspondiente fila si en alguno viene la cadena _CVE_, e inserto esos valores de DESCRIPTION en el siguiente vector de nombres de CVES
            cves_DESCRIPTION_sh=[]   
            for l in range(0,len(DESCRIPTION_thactrep_sh)):
                if('CVE' in DESCRIPTION_thactrep_sh[l] or 'cve'in DESCRIPTION_thactrep_sh[l]):
                    cves_DESCRIPTION_sh.append(DESCRIPTION_thactrep_sh[l])


            #Si en la fila de la columna DESCRIPTION hay algun valor que incluye la cadena CVE, la insertamos en el array general de CVES de la columna DESCRIPTION
            if(len(cves_DESCRIPTION_sh)>0):
                for y in range(0,len(cves_DESCRIPTION_sh)):
                    #Si aparte del ID del CVE viene alguna cadena de texto mas
                    arrayaux=cves_DESCRIPTION_sh[y].split("-")
                    for i in range(0,len(arrayaux)):
                        if(len(arrayaux[i]) == 4):
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
                                                if(strax[0:14] not in cves_DESCRIPTION_thactrep_sh):
                                                    cves_DESCRIPTION_thactrep_sh.append(strax[0:14])
                                        else:
                                            if(strax[0:14] not in cves_DESCRIPTION_thactrep_sh):
                                                cves_DESCRIPTION_thactrep_sh.append(strax[0:14])
                                    else:
                                        #Dejamos de recorrer el string cuando encontremos una letra y no una cifra
                                        if(strax[0:13] not in cves_DESCRIPTION_thactrep_sh):
                                            cves_DESCRIPTION_thactrep_sh.append(strax[0:13])
                                else:
                                    #Insertamos el ID del CVE si el largo del substring posterior al anio del ID del CVE es de longitud 4 o menor
                                    if(strax not in cves_DESCRIPTION_thactrep_sh):
                                        cves_DESCRIPTION_thactrep_sh.append(strax)                                   
#Comprobamos los CVES IDS coincidentes entre THREAT ACTIVITY REPORT IBM y CVE
if(len(cves_DESCRIPTION_thactrep_sh)>0) :   
    #Recorro los IDS de la vulnerabilidades en el excel de CVES
    for w in range(0,len(df_cve_sh["CVE_Items.cve.CVE_data_meta.ID"])):
        if((df_cve_sh["CVE_Items.cve.CVE_data_meta.ID"][w].replace('[','').replace(']','').replace("'","").replace("","").replace(" ","")) in cves_DESCRIPTION_thactrep_sh):
            cves_description_coincidentes_thactrep_sh.append(df_cve_sh["CVE_Items.cve.CVE_data_meta.ID"][w].replace('[','').replace(']','').replace("'","").replace("","").replace(" ",""))

print("\n")
print("\n")
#Si hemos encontrado CVES coincidentes en la columna DESCRIPTION de THREAT ACTIVITY REPORT IBM, los imprimo por pantalla
if(len(cves_description_coincidentes_thactrep_sh)>0):
    print("EXISTEN "+str(len(cves_description_coincidentes_thactrep_sh))+"IDENTIFICADORES DE CVES CONTENIDOS O COINCIDENTES EN LA COLUMNA DESCRIPCIÓN DE INFORMES DE ACTIVIDAD DE AMENAZAS IBM  PARA LA PARTE SMART HOME :")
    print("\n")
    for t in range(0,len(cves_description_coincidentes_thactrep_sh)):
        print("- "+cves_description_coincidentes_thactrep_sh[t])
        print("\n")

else:
    print("NO HAY IDENTIFICADORES DE CVES COINCIDENTES O CONTENIDOS EN LA COLUMNA DESCRIPCIÓN DE INFORMES DE ACTIVIDAD DE AMENAZAS IBM PARA LA PARTE SMART HOME")










#Vector donde guardaremos los valores de la columna DESCRIPTION donde se encuentra algun CVE
cves_DESCRIPTION_thactrep_iotsh=[]
#Vector donde guardaremos los valores no duplicados de la columna DESCRIPTION donde se encuentra algun CVE
cves_DESCRIPTION_thactrep_iotsh=[]
#Vector donde guardaremos los CVES incluidos en la columna DESCRIPTION junto con el valor de la columna DESCRIPTION
cves_description_coincidentes_thactrep_iotsh=[]
#Vector donde guardaremos los CVES incluidos en la columna DESCRIPTION junto con el valor de la columna DESCRIPTION, no duplicados
cves_description_coincidentes_thactrep_iotsh_def=[]



#Recorremos la columna _DESCRIPTION_ del fichero de THREAT ACTIVITY REPORT IBM IOT
for i in range(0,len(df_thactrep_iot["description"])):
    #Si el nombre no esta especificado no hago nada
    if(df_thactrep_iot["description"][i] !='NONE'):
        #Vector donde guardaremos todos los DESCRIPTIONs de la columna
        DESCRIPTION_thactrep_iotsh=[]
        #Compruebo si en cada fila de la columna DESCRIPTION hay solo un valor o varios
        if(isinstance(df_thactrep_iot["description"][i],float) == False):
            if((",") in (df_thactrep_iot["description"][i])):
                #Si hay varios valores de DESCRIPTION en la misma fila, separo cada uno de los valores
                aux_DESCRIPTION_thactrep_iotsh = df_thactrep_iot["description"][i].split(',')
                #Inserto cada valor de DESCRIPTION de cada fila en el vector donde estaran todos los valores de DESCRIPTION, quitando algunos caracteres especiales y espacios
                for j in range(0,len(aux_DESCRIPTION_thactrep_iotsh)):
                    DESCRIPTION_thactrep_iotsh.append(aux_DESCRIPTION_thactrep_iotsh[j].replace('[','').replace(']','').replace("'","").replace(" ",""))
            #Si en la fila hay un solo valor de DESCRIPTION, inserto directamente ese valor
            else:
                DESCRIPTION_thactrep_iotsh.append(df_thactrep_iot["description"][i].replace('[','').replace(']','').replace("'","").replace(" ",""))

            #Compruebo en todos los valores que hemos insertado de DESCRIPTION de la correspondiente fila si en alguno viene la cadena _CVE_, e inserto esos valores de DESCRIPTION en el siguiente vector de nombres de CVES
            cves_DESCRIPTION_iotsh=[]   
            for l in range(0,len(DESCRIPTION_thactrep_iotsh)):
                if('CVE' in DESCRIPTION_thactrep_iotsh[l] or 'cve'in DESCRIPTION_thactrep_iotsh[l]):
                    cves_DESCRIPTION_iotsh.append(DESCRIPTION_thactrep_iotsh[l])


            #Si en la fila de la columna DESCRIPTION hay algun valor que incluye la cadena CVE, la insertamos en el array general de CVES de la columna DESCRIPTION
            if(len(cves_DESCRIPTION_iotsh)>0):
                for y in range(0,len(cves_DESCRIPTION_iotsh)):
                    #Si aparte del ID del CVE viene alguna cadena de texto mas
                    arrayaux=cves_DESCRIPTION_iotsh[y].split("-")
                    for i in range(0,len(arrayaux)):
                        if(len(arrayaux[i]) == 4):
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
                                                if(strax[0:14] not in cves_DESCRIPTION_thactrep_iotsh):
                                                    cves_DESCRIPTION_thactrep_iotsh.append(strax[0:14])
                                        else:
                                            if(strax[0:14] not in cves_DESCRIPTION_thactrep_iotsh):
                                                cves_DESCRIPTION_thactrep_iotsh.append(strax[0:14])
                                    else:
                                        #Dejamos de recorrer el string cuando encontremos una letra y no una cifra
                                        if(strax[0:13] not in cves_DESCRIPTION_thactrep_iotsh):
                                            cves_DESCRIPTION_thactrep_iotsh.append(strax[0:13])
                                else:
                                    #Insertamos el ID del CVE si el largo del substring posterior al anio del ID del CVE es de longitud 4 o menor
                                    if(strax not in cves_DESCRIPTION_thactrep_iotsh):
                                        cves_DESCRIPTION_thactrep_iotsh.append(strax)                                   
#Comprobamos los CVES IDS coincidentes entre THREAT ACTIVITY REPORT IBM y CVE
if(len(cves_DESCRIPTION_thactrep_iotsh)>0) :   
    #Recorro los IDS de la vulnerabilidades en el excel de CVES
    for w in range(0,len(df_cve_sh["CVE_Items.cve.CVE_data_meta.ID"])):
        if((df_cve_sh["CVE_Items.cve.CVE_data_meta.ID"][w].replace('[','').replace(']','').replace("'","").replace("","").replace(" ","")) in cves_DESCRIPTION_thactrep_iotsh):
            cves_description_coincidentes_thactrep_iotsh.append(df_cve_sh["CVE_Items.cve.CVE_data_meta.ID"][w].replace('[','').replace(']','').replace("'","").replace("","").replace(" ",""))

print("\n")
print("\n")
#Si hemos encontrado CVES coincidentes en la columna DESCRIPTION de THREAT ACTIVITY REPORT IBM, los imprimo por pantalla
if(len(cves_description_coincidentes_thactrep_iotsh)>0):
    print("EXISTEN "+str(len(cves_description_coincidentes_thactrep_iotsh))+"IDENTIFICADORES DE CVES DE LA PARTE SMART HOME CONTENIDOS EN LA COLUMNA DESCRIPCIÓN DE INFORMES DE ACTIVIDAD DE AMENAZAS IBM  PARA LA PARTE IOT :")
    print("\n")
    for t in range(0,len(cves_description_coincidentes_thactrep_iotsh)):
        print("- "+cves_description_coincidentes_thactrep_iotsh[t])
        print("\n")
        
else:
    print("NO HAY IDENTIFICADORES DE CVES DE LA PARTE SMART HOME COINCIDENTES O CONTENIDOS EN LA COLUMNA DESCRIPCIÓN DE INFORMES DE ACTIVIDAD DE AMENAZAS IBM PARA LA PARTE IOT")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    


#Vector donde guardaremos los valores de la columna DESCRIPTION donde se encuentra algun CVE
cves_DESCRIPTION_thactrep_shiot=[]
#Vector donde guardaremos los valores no duplicados de la columna DESCRIPTION donde se encuentra algun CVE
cves_DESCRIPTION_thactrep_shiot=[]
#Vector donde guardaremos los CVES incluidos en la columna DESCRIPTION junto con el valor de la columna DESCRIPTION
cves_description_coincidentes_thactrep_shiot=[]
#Vector donde guardaremos los CVES incluidos en la columna DESCRIPTION junto con el valor de la columna DESCRIPTION, no duplicados
cves_description_coincidentes_thactrep_shiot_def=[]



#Recorremos la columna _DESCRIPTION_ del fichero de THREAT ACTIVITY REPORT IBM SMART HOME
for i in range(0,len(df_thactrep_sh["description"])):
    #Si el nombre no esta especificado no hago nada
    if(df_thactrep_sh["description"][i] !='NONE'):
        #Vector donde guardaremos todos los DESCRIPTIONs de la columna
        DESCRIPTION_thactrep_shiot=[]
        #Compruebo si en cada fila de la columna DESCRIPTION hay solo un valor o varios
        if(isinstance(df_thactrep_sh["description"][i],float) == False):
            if((",") in (df_thactrep_sh["description"][i])):
                #Si hay varios valores de DESCRIPTION en la misma fila, separo cada uno de los valores
                aux_DESCRIPTION_thactrep_shiot = df_thactrep_sh["description"][i].split(',')
                #Inserto cada valor de DESCRIPTION de cada fila en el vector donde estaran todos los valores de DESCRIPTION, quitando algunos caracteres especiales y espacios
                for j in range(0,len(aux_DESCRIPTION_thactrep_shiot)):
                    DESCRIPTION_thactrep_shiot.append(aux_DESCRIPTION_thactrep_shiot[j].replace('[','').replace(']','').replace("'","").replace(" ",""))
            #Si en la fila hay un solo valor de DESCRIPTION, inserto directamente ese valor
            else:
                DESCRIPTION_thactrep_shiot.append(df_thactrep_sh["description"][i].replace('[','').replace(']','').replace("'","").replace(" ",""))

            #Compruebo en todos los valores que hemos insertado de DESCRIPTION de la correspondiente fila si en alguno viene la cadena _CVE_, e inserto esos valores de DESCRIPTION en el siguiente vector de nombres de CVES
            cves_DESCRIPTION_shiot=[]   
            for l in range(0,len(DESCRIPTION_thactrep_shiot)):
                if('CVE' in DESCRIPTION_thactrep_shiot[l] or 'cve'in DESCRIPTION_thactrep_shiot[l]):
                    cves_DESCRIPTION_shiot.append(DESCRIPTION_thactrep_shiot[l])


            #Si en la fila de la columna DESCRIPTION hay algun valor que incluye la cadena CVE, la insertamos en el array general de CVES de la columna DESCRIPTION
            if(len(cves_DESCRIPTION_shiot)>0):
                for y in range(0,len(cves_DESCRIPTION_shiot)):
                    #Si aparte del ID del CVE viene alguna cadena de texto mas
                    arrayaux=cves_DESCRIPTION_shiot[y].split("-")
                    for i in range(0,len(arrayaux)):
                        if(len(arrayaux[i]) == 4):
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
                                                if(strax[0:14] not in cves_DESCRIPTION_thactrep_shiot):
                                                    cves_DESCRIPTION_thactrep_shiot.append(strax[0:14])
                                        else:
                                            if(strax[0:14] not in cves_DESCRIPTION_thactrep_shiot):
                                                cves_DESCRIPTION_thactrep_shiot.append(strax[0:14])
                                    else:
                                        #Dejamos de recorrer el string cuando encontremos una letra y no una cifra
                                        if(strax[0:13] not in cves_DESCRIPTION_thactrep_shiot):
                                            cves_DESCRIPTION_thactrep_shiot.append(strax[0:13])
                                else:
                                    #Insertamos el ID del CVE si el largo del substring posterior al anio del ID del CVE es de longitud 4 o menor
                                    if(strax not in cves_DESCRIPTION_thactrep_shiot):
                                        cves_DESCRIPTION_thactrep_shiot.append(strax)                                   
#Comprobamos los CVES IDS coincidentes entre THREAT ACTIVITY REPORT IBM y CVE
if(len(cves_DESCRIPTION_thactrep_shiot)>0) :   
    #Recorro los IDS de la vulnerabilidades en el excel de CVES
    for w in range(0,len(df_cve_iot["CVE_Items.cve.CVE_data_meta.ID"])):
        if((df_cve_iot["CVE_Items.cve.CVE_data_meta.ID"][w].replace('[','').replace(']','').replace("'","").replace("","").replace(" ","")) in cves_DESCRIPTION_thactrep_shiot):
            cves_description_coincidentes_thactrep_shiot.append(df_cve_iot["CVE_Items.cve.CVE_data_meta.ID"][w].replace('[','').replace(']','').replace("'","").replace("","").replace(" ",""))

print("\n")
print("\n")
#Si hemos encontrado CVES coincidentes en la columna DESCRIPTION de THREAT ACTIVITY REPORT IBM, los imprimo por pantalla
if(len(cves_description_coincidentes_thactrep_shiot)>0):
    print("EXISTEN "+str(len(cves_description_coincidentes_thactrep_shiot))+"IDENTIFICADORES DE CVES DE LA PARTE IOT CONTENIDOS EN LA COLUMNA DESCRIPCIÓN DE INFORMES DE ACTIVIDAD DE AMENAZAS IBM  PARA LA PARTE SMART HOME :")
    print("\n")
    for t in range(0,len(cves_description_coincidentes_thactrep_shiot)):
        print("- "+cves_description_coincidentes_thactrep_shiot[t])
        print("\n")
        
else:
    print("NO HAY IDENTIFICADORES DE CVES DE LA PARTE IOT COINCIDENTES O CONTENIDOS EN LA COLUMNA DESCRIPCIÓN DE INFORMES DE ACTIVIDAD DE AMENAZAS IBM PARA LA PARTE SMART HOME")
    
    
    