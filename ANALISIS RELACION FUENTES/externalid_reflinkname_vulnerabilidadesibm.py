import pandas as pd

df_vulnibm_iot=pd.read_excel('vulnerabilidades_ibm_iot_2023.xlsx')
df_cve_iot=pd.read_excel('cves_iot_2023.xlsx')


#Vector donde guardaremos los valores de la columna REFERENCES LINK NAME donde se encuentra algun CVE
cves_referenceslinkname_vulnibm_iot=[]
#Vector donde guardaremos los valores no duplicados de la columna REFERENCES LINK NAME donde se encuentra algun CVE
cves_referenceslinkname_vulnibm_iot=[]
#Vector donde guardaremos los CVES incluidos en la columna REFERENCES LINK NAME junto con el valor de la columna REFERENCES LINK NAME
cves_referenceslinkname_coincidentes_vulnibm_iot=[]
#Vector donde guardaremos los CVES incluidos en la columna REFERENCES LINK NAME junto con el valor de la columna REFERENCES LINK NAME, no duplicados
cves_referenceslinkname_coincidentes_vulnibm_iot_def=[]



#Recorremos la columna _referenceslinkname_ del fichero de VULNERABILIDADES  IBM iot
for i in range(0,len(df_vulnibm_iot["x_xfe_references_link_name"])):
    #Si el nombre no esta especificado no hago nada
    if(df_vulnibm_iot["x_xfe_references_link_name"][i] !='NONE'):
        #Vector donde guardaremos todos los REFERENCE_LINK_NAMEs de la columna
        referenceslinkname_vulnibm_iot=[]
        #Compruebo si en cada fila de la columna REFERENCES LINK NAME hay solo un valor o varios
        if(isinstance(df_vulnibm_iot["x_xfe_references_link_name"][i],float) == False):
            if((",") in (df_vulnibm_iot["x_xfe_references_link_name"][i])):
                #Si hay varios valores de REFERENCE_LINK_NAME en la misma fila, separo cada uno de los valores
                aux_referenceslinkname_vulnibm_iot = df_vulnibm_iot["x_xfe_references_link_name"][i].split(',')
                #Inserto cada valor de REFERENCE_LINK_NAME de cada fila en el vector donde estaran todos los valores de REFERENCE_LINK_NAME, quitando algunos caracteres especiales y espacios
                for j in range(0,len(aux_referenceslinkname_vulnibm_iot)):
                    referenceslinkname_vulnibm_iot.append(aux_referenceslinkname_vulnibm_iot[j].replace('[','').replace(']','').replace("'","").replace(" ",""))
            #Si en la fila hay un solo valor de REFERENCE_LINK_NAME, inserto directamente ese valor
            else:
                referenceslinkname_vulnibm_iot.append(df_vulnibm_iot["x_xfe_references_link_name"][i].replace('[','').replace(']','').replace("'","").replace(" ",""))

            #Compruebo en todos los valores que hemos insertado de REFERENCE_LINK_NAME de la correspondiente fila si en alguno viene la cadena _CVE_, e inserto esos valores de REFERENCE_LINK_NAME en el siguiente vector de nombres de CVES
            cves_referenceslinkname_iot=[]   
            for l in range(0,len(referenceslinkname_vulnibm_iot)):
                if('CVE' in referenceslinkname_vulnibm_iot[l] or 'cve'in referenceslinkname_vulnibm_iot[l]):
                    cves_referenceslinkname_iot.append(referenceslinkname_vulnibm_iot[l])


            #Si en la fila de la columna REFERENCES LINK NAME hay algun valor que incluye la cadena CVE, la insertamos en el array general de CVES de la columna REFERENCES LINK NAME
            if(len(cves_referenceslinkname_iot)>0):
                for y in range(0,len(cves_referenceslinkname_iot)):
                    #Si aparte del ID del CVE viene alguna cadena de texto mas
                    arrayaux=cves_referenceslinkname_iot[y].split("-")
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
                                                if(strax[0:14] not in cves_referenceslinkname_vulnibm_iot):
                                                    cves_referenceslinkname_vulnibm_iot.append(strax[0:14])
                                        else:
                                            if(strax[0:14] not in cves_referenceslinkname_vulnibm_iot):
                                                cves_referenceslinkname_vulnibm_iot.append(strax[0:14])
                                    else:
                                        #Dejamos de recorrer el string cuando encontremos una letra y no una cifra
                                        if(strax[0:13] not in cves_referenceslinkname_vulnibm_iot):
                                            cves_referenceslinkname_vulnibm_iot.append(strax[0:13])
                                else:
                                    #Insertamos el ID del CVE si el largo del substring posterior al anio del ID del CVE es de longitud 4 o menor
                                    if(strax not in cves_referenceslinkname_vulnibm_iot):
                                        cves_referenceslinkname_vulnibm_iot.append(strax) 

#Comprobamos los CVES IDS coincidentes entre VULNERABILIDADES  IBM y CVE
if(len(cves_referenceslinkname_vulnibm_iot)>0) :   
    #Recorro los IDS de la vulnerabilidades en el excel de CVES
    for w in range(0,len(df_cve_iot["CVE_Items.cve.CVE_data_meta.ID"])):
        if((df_cve_iot["CVE_Items.cve.CVE_data_meta.ID"][w].replace('[','').replace(']','').replace("'","").replace("","").replace(" ","")) in cves_referenceslinkname_vulnibm_iot):
            cves_referenceslinkname_coincidentes_vulnibm_iot.append(df_cve_iot["CVE_Items.cve.CVE_data_meta.ID"][w].replace('[','').replace(']','').replace("'","").replace("","").replace(" ",""))

print("\n")
#Si hemos encontrado CVES coincidentes en la columna REFERENCES LINK NAME de VULNERABILIDADES  IBM, los imprimo por pantalla
if(len(cves_referenceslinkname_coincidentes_vulnibm_iot)>0):
    print("EXISTEN "+str(len(cves_referenceslinkname_coincidentes_vulnibm_iot))+" IDENTIFICADORES DE CVES COINCIDENTES O CONTENIDOS EN EL NOMBRE DE ENLACE DE REFERENCIAS PARA VULNERABILDIADES IBM DE LA PARTE DE IOT :")
    print("\n")
    for t in range(0,len(cves_referenceslinkname_coincidentes_vulnibm_iot)):
        print("- "+cves_referenceslinkname_coincidentes_vulnibm_iot[t])
        print("\n")
        
else:
    print("NO HAY IDENTIFICADORES DE CVES COINCIDENTES O CONTENIDOS EN EL NOMBRE DE ENLACE DE REFERENCIAS PARA VULNERABILDIADES IBM DE LA PARTE DE IOT")
    
    
    
    
    
    
    


df_vulnibm_sh=pd.read_excel('vulnerabilidades_ibm_smart_home_2023.xlsx')
df_cve_sh=pd.read_excel('cves_smart_home_2023.xlsx')


#Vector donde guardaremos los valores de la columna REFERENCES LINK NAME donde se encuentra algun CVE
cves_referenceslinkname_vulnibm_sh=[]
#Vector donde guardaremos los valores no duplicados de la columna REFERENCES LINK NAME donde se encuentra algun CVE
cves_referenceslinkname_vulnibm_sh=[]
#Vector donde guardaremos los CVES incluidos en la columna REFERENCES LINK NAME junto con el valor de la columna REFERENCES LINK NAME
cves_referenceslinkname_coincidentes_vulnibm_sh=[]
#Vector donde guardaremos los CVES incluidos en la columna REFERENCES LINK NAME junto con el valor de la columna REFERENCES LINK NAME, no duplicados
cves_referenceslinkname_coincidentes_vulnibm_sh_def=[]



#Recorremos la columna _referenceslinkname_ del fichero de VULNERABILIDADES  IBM SMART HOME
for i in range(0,len(df_vulnibm_sh["x_xfe_references_link_name"])):
    #Si el nombre no esta especificado no hago nada
    if(df_vulnibm_sh["x_xfe_references_link_name"][i] !='NONE'):
        #Vector donde guardaremos todos los REFERENCE_LINK_NAMEs de la columna
        referenceslinkname_vulnibm_sh=[]
        #Compruebo si en cada fila de la columna REFERENCES LINK NAME hay solo un valor o varios
        if(isinstance(df_vulnibm_sh["x_xfe_references_link_name"][i],float) == False):
            if((",") in (df_vulnibm_sh["x_xfe_references_link_name"][i])):
                #Si hay varios valores de REFERENCE_LINK_NAME en la misma fila, separo cada uno de los valores
                aux_referenceslinkname_vulnibm_sh = df_vulnibm_sh["x_xfe_references_link_name"][i].split(',')
                #Inserto cada valor de REFERENCE_LINK_NAME de cada fila en el vector donde estaran todos los valores de REFERENCE_LINK_NAME, quitando algunos caracteres especiales y espacios
                for j in range(0,len(aux_referenceslinkname_vulnibm_sh)):
                    referenceslinkname_vulnibm_sh.append(aux_referenceslinkname_vulnibm_sh[j].replace('[','').replace(']','').replace("'","").replace(" ",""))
            #Si en la fila hay un solo valor de REFERENCE_LINK_NAME, inserto directamente ese valor
            else:
                referenceslinkname_vulnibm_sh.append(df_vulnibm_sh["x_xfe_references_link_name"][i].replace('[','').replace(']','').replace("'","").replace(" ",""))

            #Compruebo en todos los valores que hemos insertado de REFERENCE_LINK_NAME de la correspondiente fila si en alguno viene la cadena _CVE_, e inserto esos valores de REFERENCE_LINK_NAME en el siguiente vector de nombres de CVES
            cves_referenceslinkname_sh=[]   
            for l in range(0,len(referenceslinkname_vulnibm_sh)):
                if('CVE' in referenceslinkname_vulnibm_sh[l] or 'cve'in referenceslinkname_vulnibm_sh[l]):
                    cves_referenceslinkname_sh.append(referenceslinkname_vulnibm_sh[l])


            #Si en la fila de la columna REFERENCES LINK NAME hay algun valor que incluye la cadena CVE, la insertamos en el array general de CVES de la columna REFERENCES LINK NAME
            if(len(cves_referenceslinkname_sh)>0):
                for y in range(0,len(cves_referenceslinkname_sh)):
                    #Si aparte del ID del CVE viene alguna cadena de texto mas
                    arrayaux=cves_referenceslinkname_sh[y].split("-")
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
                                                if(strax[0:14] not in cves_referenceslinkname_vulnibm_sh):
                                                    cves_referenceslinkname_vulnibm_sh.append(strax[0:14])
                                        else:
                                            if(strax[0:14] not in cves_referenceslinkname_vulnibm_sh):
                                                cves_referenceslinkname_vulnibm_sh.append(strax[0:14])
                                    else:
                                        #Dejamos de recorrer el string cuando encontremos una letra y no una cifra
                                        if(strax[0:13] not in cves_referenceslinkname_vulnibm_sh):
                                            cves_referenceslinkname_vulnibm_sh.append(strax[0:13])
                                else:
                                    #Insertamos el ID del CVE si el largo del substring posterior al anio del ID del CVE es de longitud 4 o menor
                                    if(strax not in cves_referenceslinkname_vulnibm_sh):
                                        cves_referenceslinkname_vulnibm_sh.append(strax)                                   
#Comprobamos los CVES IDS coincidentes entre VULNERABILIDADES  IBM y CVE
if(len(cves_referenceslinkname_vulnibm_sh)>0) :   
    #Recorro los IDS de la vulnerabilidades en el excel de CVES
    for w in range(0,len(df_cve_sh["CVE_Items.cve.CVE_data_meta.ID"])):
        if((df_cve_sh["CVE_Items.cve.CVE_data_meta.ID"][w].replace('[','').replace(']','').replace("'","").replace("","").replace(" ","")) in cves_referenceslinkname_vulnibm_sh):
            cves_referenceslinkname_coincidentes_vulnibm_sh.append(df_cve_sh["CVE_Items.cve.CVE_data_meta.ID"][w].replace('[','').replace(']','').replace("'","").replace("","").replace(" ",""))

print("\n")
print("\n")
#Si hemos encontrado CVES coincidentes en la columna REFERENCES LINK NAME de VULNERABILIDADES  IBM, los imprimo por pantalla
if(len(cves_referenceslinkname_coincidentes_vulnibm_sh)>0):
    print("EXISTEN "+str(len(cves_referenceslinkname_coincidentes_vulnibm_sh))+" IDENTIFICADORES DE CVES COINCIDENTES O CONTENIDOS EN EL NOMBRE DE ENLACE DE REFERENCIAS PARA VULNERABILDIADES IBM DE LA PARTE DE SMART HOME :")
    print("\n")
    for t in range(0,len(cves_referenceslinkname_coincidentes_vulnibm_sh)):
        print("- "+cves_referenceslinkname_coincidentes_vulnibm_sh[t])
        print("\n")

else:
    print("NO HAY IDENTIFICADORES DE CVES COINCIDENTES O CONTENIDOS EN EL NOMBRE DE ENLACE DE REFERENCIAS PARA VULNERABILDIADES IBM DE LA PARTE DE SMART HOME")










#Vector donde guardaremos los valores de la columna REFERENCES LINK NAME donde se encuentra algun CVE
cves_referenceslinkname_vulnibm_iotsh=[]
#Vector donde guardaremos los valores no duplicados de la columna REFERENCES LINK NAME donde se encuentra algun CVE
cves_referenceslinkname_vulnibm_iotsh=[]
#Vector donde guardaremos los CVES incluidos en la columna REFERENCES LINK NAME junto con el valor de la columna REFERENCES LINK NAME
cves_referenceslinkname_coincidentes_vulnibm_iotsh=[]
#Vector donde guardaremos los CVES incluidos en la columna REFERENCES LINK NAME junto con el valor de la columna REFERENCES LINK NAME, no duplicados
cves_referenceslinkname_coincidentes_vulnibm_iotsh_def=[]



#Recorremos la columna _referenceslinkname_ del fichero de VULNERABILIDADES  IBM IOT
for i in range(0,len(df_vulnibm_iot["x_xfe_references_link_name"])):
    #Si el nombre no esta especificado no hago nada
    if(df_vulnibm_iot["x_xfe_references_link_name"][i] !='NONE'):
        #Vector donde guardaremos todos los REFERENCE_LINK_NAMEs de la columna
        referenceslinkname_vulnibm_iotsh=[]
        #Compruebo si en cada fila de la columna REFERENCES LINK NAME hay solo un valor o varios
        if(isinstance(df_vulnibm_iot["x_xfe_references_link_name"][i],float) == False):
            if((",") in (df_vulnibm_iot["x_xfe_references_link_name"][i])):
                #Si hay varios valores de REFERENCE_LINK_NAME en la misma fila, separo cada uno de los valores
                aux_referenceslinkname_vulnibm_iotsh = df_vulnibm_iot["x_xfe_references_link_name"][i].split(',')
                #Inserto cada valor de REFERENCE_LINK_NAME de cada fila en el vector donde estaran todos los valores de REFERENCE_LINK_NAME, quitando algunos caracteres especiales y espacios
                for j in range(0,len(aux_referenceslinkname_vulnibm_iotsh)):
                    referenceslinkname_vulnibm_iotsh.append(aux_referenceslinkname_vulnibm_iotsh[j].replace('[','').replace(']','').replace("'","").replace(" ",""))
            #Si en la fila hay un solo valor de REFERENCE_LINK_NAME, inserto directamente ese valor
            else:
                referenceslinkname_vulnibm_iotsh.append(df_vulnibm_iot["x_xfe_references_link_name"][i].replace('[','').replace(']','').replace("'","").replace(" ",""))

            #Compruebo en todos los valores que hemos insertado de REFERENCE_LINK_NAME de la correspondiente fila si en alguno viene la cadena _CVE_, e inserto esos valores de REFERENCE_LINK_NAME en el siguiente vector de nombres de CVES
            cves_referenceslinkname_iotsh=[]   
            for l in range(0,len(referenceslinkname_vulnibm_iotsh)):
                if('CVE' in referenceslinkname_vulnibm_iotsh[l] or 'cve'in referenceslinkname_vulnibm_iotsh[l]):
                    cves_referenceslinkname_iotsh.append(referenceslinkname_vulnibm_iotsh[l])


            #Si en la fila de la columna REFERENCES LINK NAME hay algun valor que incluye la cadena CVE, la insertamos en el array general de CVES de la columna REFERENCES LINK NAME
            if(len(cves_referenceslinkname_iotsh)>0):
                for y in range(0,len(cves_referenceslinkname_iotsh)):
                    #Si aparte del ID del CVE viene alguna cadena de texto mas
                    arrayaux=cves_referenceslinkname_iotsh[y].split("-")
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
                                                if(strax[0:14] not in cves_referenceslinkname_vulnibm_iotsh):
                                                    cves_referenceslinkname_vulnibm_iotsh.append(strax[0:14])
                                        else:
                                            if(strax[0:14] not in cves_referenceslinkname_vulnibm_iotsh):
                                                cves_referenceslinkname_vulnibm_iotsh.append(strax[0:14])
                                    else:
                                        #Dejamos de recorrer el string cuando encontremos una letra y no una cifra
                                        if(strax[0:13] not in cves_referenceslinkname_vulnibm_iotsh):
                                            cves_referenceslinkname_vulnibm_iotsh.append(strax[0:13])
                                else:
                                    #Insertamos el ID del CVE si el largo del substring posterior al anio del ID del CVE es de longitud 4 o menor
                                    if(strax not in cves_referenceslinkname_vulnibm_iotsh):
                                        cves_referenceslinkname_vulnibm_iotsh.append(strax)                                   
#Comprobamos los CVES IDS coincidentes entre VULNERABILIDADES  IBM y CVE
if(len(cves_referenceslinkname_vulnibm_iotsh)>0) :   
    #Recorro los IDS de la vulnerabilidades en el excel de CVES
    for w in range(0,len(df_cve_sh["CVE_Items.cve.CVE_data_meta.ID"])):
        if((df_cve_sh["CVE_Items.cve.CVE_data_meta.ID"][w].replace('[','').replace(']','').replace("'","").replace("","").replace(" ","")) in cves_referenceslinkname_vulnibm_iotsh):
            cves_referenceslinkname_coincidentes_vulnibm_iotsh.append(df_cve_sh["CVE_Items.cve.CVE_data_meta.ID"][w].replace('[','').replace(']','').replace("'","").replace("","").replace(" ",""))

print("\n")
print("\n")
#Si hemos encontrado CVES coincidentes en la columna REFERENCES LINK NAME de VULNERABILIDADES  IBM, los imprimo por pantalla
if(len(cves_referenceslinkname_coincidentes_vulnibm_iotsh)>0):
    print("EXISTEN "+str(len(cves_referenceslinkname_coincidentes_vulnibm_iotsh))+" IDENTIFICADORES DE CVES DE LA PARTE SMART HOME COINCIDENTES O CONTENIDOS EN EL NOMBRE DE ENLACE DE REFERENCIAS PARA VULNERABILDIADES IBM DE LA PARTE DE  IOT  :")
    print("\n")
    for t in range(0,len(cves_referenceslinkname_coincidentes_vulnibm_iotsh)):
        print("- "+cves_referenceslinkname_coincidentes_vulnibm_iotsh[t])
        print("\n")
        
else:
    print("NO HAY IDENTIFICADORES DE CVES DE LA PARTE SMART HOME COINCIDENTES O CONTENIDOS EN EL NOMBRE DE ENLACE DE REFERENCIAS PARA VULNERABILDIADES IBM DE LA PARTE DE  IOT ")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    


#Vector donde guardaremos los valores de la columna REFERENCES LINK NAME donde se encuentra algun CVE
cves_referenceslinkname_vulnibm_shiot=[]
#Vector donde guardaremos los valores no duplicados de la columna REFERENCES LINK NAME donde se encuentra algun CVE
cves_referenceslinkname_vulnibm_shiot=[]
#Vector donde guardaremos los CVES incluidos en la columna REFERENCES LINK NAME junto con el valor de la columna REFERENCES LINK NAME
cves_referenceslinkname_coincidentes_vulnibm_shiot=[]
#Vector donde guardaremos los CVES incluidos en la columna REFERENCES LINK NAME junto con el valor de la columna REFERENCES LINK NAME, no duplicados
cves_referenceslinkname_coincidentes_vulnibm_shiot_def=[]



#Recorremos la columna _referenceslinkname_ del fichero de VULNERABILIDADES  IBM SMART HOME
for i in range(0,len(df_vulnibm_sh["x_xfe_references_link_name"])):
    #Si el nombre no esta especificado no hago nada
    if(df_vulnibm_sh["x_xfe_references_link_name"][i] !='NONE'):
        #Vector donde guardaremos todos los REFERENCE_LINK_NAMEs de la columna
        referenceslinkname_vulnibm_shiot=[]
        #Compruebo si en cada fila de la columna REFERENCES LINK NAME hay solo un valor o varios
        if(isinstance(df_vulnibm_sh["x_xfe_references_link_name"][i],float) == False):
            if((",") in (df_vulnibm_sh["x_xfe_references_link_name"][i])):
                #Si hay varios valores de REFERENCE_LINK_NAME en la misma fila, separo cada uno de los valores
                aux_referenceslinkname_vulnibm_shiot = df_vulnibm_sh["x_xfe_references_link_name"][i].split(',')
                #Inserto cada valor de REFERENCE_LINK_NAME de cada fila en el vector donde estaran todos los valores de REFERENCE_LINK_NAME, quitando algunos caracteres especiales y espacios
                for j in range(0,len(aux_referenceslinkname_vulnibm_shiot)):
                    referenceslinkname_vulnibm_shiot.append(aux_referenceslinkname_vulnibm_shiot[j].replace('[','').replace(']','').replace("'","").replace(" ",""))
            #Si en la fila hay un solo valor de REFERENCE_LINK_NAME, inserto directamente ese valor
            else:
                referenceslinkname_vulnibm_shiot.append(df_vulnibm_sh["x_xfe_references_link_name"][i].replace('[','').replace(']','').replace("'","").replace(" ",""))

            #Compruebo en todos los valores que hemos insertado de REFERENCE_LINK_NAME de la correspondiente fila si en alguno viene la cadena _CVE_, e inserto esos valores de REFERENCE_LINK_NAME en el siguiente vector de nombres de CVES
            cves_referenceslinkname_shiot=[]   
            for l in range(0,len(referenceslinkname_vulnibm_shiot)):
                if('CVE' in referenceslinkname_vulnibm_shiot[l] or 'cve'in referenceslinkname_vulnibm_shiot[l]):
                    cves_referenceslinkname_shiot.append(referenceslinkname_vulnibm_shiot[l])


            #Si en la fila de la columna REFERENCES LINK NAME hay algun valor que incluye la cadena CVE, la insertamos en el array general de CVES de la columna REFERENCES LINK NAME
            if(len(cves_referenceslinkname_shiot)>0):
                for y in range(0,len(cves_referenceslinkname_shiot)):
                    #Si aparte del ID del CVE viene alguna cadena de texto mas
                    arrayaux=cves_referenceslinkname_shiot[y].split("-")
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
                                                if(strax[0:14] not in cves_referenceslinkname_vulnibm_shiot):
                                                    cves_referenceslinkname_vulnibm_shiot.append(strax[0:14])
                                        else:
                                            if(strax[0:14] not in cves_referenceslinkname_vulnibm_shiot):
                                                cves_referenceslinkname_vulnibm_shiot.append(strax[0:14])
                                    else:
                                        #Dejamos de recorrer el string cuando encontremos una letra y no una cifra
                                        if(strax[0:13] not in cves_referenceslinkname_vulnibm_shiot):
                                            cves_referenceslinkname_vulnibm_shiot.append(strax[0:13])
                                else:
                                    #Insertamos el ID del CVE si el largo del substring posterior al anio del ID del CVE es de longitud 4 o menor
                                    if(strax not in cves_referenceslinkname_vulnibm_shiot):
                                        cves_referenceslinkname_vulnibm_shiot.append(strax)                                   
#Comprobamos los CVES IDS coincidentes entre VULNERABILIDADES  IBM y CVE
if(len(cves_referenceslinkname_vulnibm_shiot)>0) :   
    #Recorro los IDS de la vulnerabilidades en el excel de CVES
    for w in range(0,len(df_cve_iot["CVE_Items.cve.CVE_data_meta.ID"])):
        if((df_cve_iot["CVE_Items.cve.CVE_data_meta.ID"][w].replace('[','').replace(']','').replace("'","").replace("","").replace(" ","")) in cves_referenceslinkname_vulnibm_shiot):
            cves_referenceslinkname_coincidentes_vulnibm_shiot.append(df_cve_iot["CVE_Items.cve.CVE_data_meta.ID"][w].replace('[','').replace(']','').replace("'","").replace("","").replace(" ",""))

print("\n")
print("\n")
#Si hemos encontrado CVES coincidentes en la columna REFERENCES LINK NAME de VULNERABILIDADES  IBM, los imprimo por pantalla
if(len(cves_referenceslinkname_coincidentes_vulnibm_shiot)>0):
    print("EXISTEN "+str(len(cves_referenceslinkname_coincidentes_vulnibm_shiot))+" IDENTIFICADORES DE CVES DE LA PARTE IOT COINCIDENTES O CONTENIDOS EN EL NOMBRE DE ENLACE DE REFERENCIAS PARA VULNERABILDIADES IBM DE LA PARTE DE  SMART HOME")
    print("\n")
    for t in range(0,len(cves_referenceslinkname_coincidentes_vulnibm_shiot)):
        print("- "+cves_referenceslinkname_coincidentes_vulnibm_shiot[t])
        print("\n")
        
else:
    print("NO HAY IDENTIFICADORES DE CVES DE LA PARTE IOT COINCIDENTES O CONTENIDOS EN EL NOMBRE DE ENLACE DE REFERENCIAS PARA VULNERABILDIADES IBM DE LA PARTE DE  SMART HOME ")
    
    