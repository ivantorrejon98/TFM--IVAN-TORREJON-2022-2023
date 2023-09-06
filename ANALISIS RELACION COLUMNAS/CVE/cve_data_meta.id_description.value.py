

import pandas as pd

#Abro los ficheros con los que voy a tratar


df_cve_iot=pd.read_excel('cves_iot_2023.xlsx')
df_cve_sh=pd.read_excel('cves_smart_home_2023.xlsx')


#Vector donde almacenare los CWES distintos que aparecen para la parte IOT
array_cwes_iot=[]
#Vector donde almacenare las CVES asociadas a un CWE en concreto
array_cwes_cves_iot=[]
#Recorro los valores de DATA DESCRIPTION VALUE para la parte IOT
#Comprobamos el valor de DATA DESCRIPTION VALUE para la parte de IOT
for j in range(0,len(df_cve_iot["CVE_Items.cve.problemtype.problemtype_data.description.value"])):
    #Compruebo si en la fila actual existen varios valores de CWES
    if('[' in df_cve_iot["CVE_Items.cve.problemtype.problemtype_data.description.value"][j]):
        #Obtengo los distintos valores de CWES de la fila actual
        aux=df_cve_iot["CVE_Items.cve.problemtype.problemtype_data.description.value"][j].split(",")
        #Recorro los distintos valores de CWES
        for l in range(0,len(aux)):
            if(len(aux)>0):
                #Elimino caracteres especiales
                aux_str=aux[l].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
                #Almaceno el CWE si no ha sido almacenado ya y si no tiene un valor nulo
                if(aux_str!='NONE' and aux_str!='NVD-CWE-noinfo' and aux_str!='NVD-CWE-Other'):
                    if(aux_str not in array_cwes_iot):
                        array_cwes_iot.append(aux_str)
                    
    else:
        #Si la fila actual solamente tiene un valor de CWE, no es nulo y no ha sido almacenado, lo almaceno
        aux_str=df_cve_iot["CVE_Items.cve.problemtype.problemtype_data.description.value"][j].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
        if(aux_str!='NONE' and aux_str!='NVD-CWE-noinfo' and aux_str!='NVD-CWE-Other'):
            if(aux_str not in array_cwes_iot):
                array_cwes_iot.append(aux_str)  

#Recorro los distintos valores de CWES para la parte de IOT
for r in range(0,len(array_cwes_iot)):
    #Vectores donde almacenare los valores de CVES asociados a cada una de las CWES para la parte IOT
    array_cvesID_iot=[]
    array_cwes_cvesID_iot=[]
    #Recorro las distintas filas del fichero de IOT
    for g in range(0,len(df_cve_iot["CVE_Items.cve.CVE_data_meta.ID"])):
        #Compruebo si en la fila actual existe un solo CWE o varios
        if('[' not in df_cve_iot["CVE_Items.cve.problemtype.problemtype_data.description.value"][g]):
            aux_strr=df_cve_iot["CVE_Items.cve.problemtype.problemtype_data.description.value"][g].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
            #Si el CWE de la fila actual coincide con el CWE que estamos comprobando, insertamos el CVE ID de la fila actual, para que sea relacionado con el CWE actual
            if(aux_strr == array_cwes_iot[r]):
                #Compruebo que no haya insertado anteriormente el CVE ID correspondiente en el vector de CVEs IDS
                if(df_cve_iot["CVE_Items.cve.CVE_data_meta.ID"][g] not in array_cvesID_iot):
                    array_cvesID_iot.append(df_cve_iot["CVE_Items.cve.CVE_data_meta.ID"][g])
        else:
            aux=df_cve_iot["CVE_Items.cve.problemtype.problemtype_data.description.value"][g].split(",")
            for l in range(0,len(aux)):
                if(len(aux)>0):
                    aux_strr=aux[l].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
                    #Si el CWE de la fila actual coincide con el CWE que estamos comprobando, insertamos el CVE ID de la fila actual, para que sea relacionado con el CWE actual
                    if(aux_strr == array_cwes_iot[r]):
                        #Compruebo que no haya insertado anteriormente el CVE ID correspondiente en el vector de CVEs IDS
                        if(df_cve_iot["CVE_Items.cve.CVE_data_meta.ID"][g] not in array_cvesID_iot):
                            array_cvesID_iot.append(df_cve_iot["CVE_Items.cve.CVE_data_meta.ID"][g])
    #Si hemos encontrado algun CVE asociado al actual CWE, insertamos el CWE y sus CVES asociados al vector global
    if(len(array_cvesID_iot) > 0):
        array_cwes_cvesID_iot.insert(0,array_cwes_iot[r])
        array_cwes_cvesID_iot.append(array_cvesID_iot)
        #Insertamos el CWE actual y sus CVES asociados
        array_cwes_cves_iot.append(array_cwes_cvesID_iot)   





#Vector donde almacenare los CWES distintos que aparecen para la parte SMART HOME
array_cwes_sh=[]
#Vector donde almacenare las CVES asociadas a un CWE en concreto
array_cwes_cves_sh=[]
#Recorro los valores de DATA DESCRIPTION VALUE para la parte SMART HOME
#Comprobamos el valor de DATA DESCRIPTION VALUE para la parte de SMART HOME
for j in range(0,len(df_cve_sh["CVE_Items.cve.problemtype.problemtype_data.description.value"])):
    #Compruebo si en la fila actual existen varios valores de CWES
    if('[' in df_cve_sh["CVE_Items.cve.problemtype.problemtype_data.description.value"][j]):
        #Obtengo los distintos valores de CWES de la fila actual
        aux=df_cve_sh["CVE_Items.cve.problemtype.problemtype_data.description.value"][j].split(",")
        #Recorro los distintos valores de CWES
        for l in range(0,len(aux)):
            if(len(aux)>0):
                #Elimino caracteres especiales
                aux_str=aux[l].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
                #Almaceno el CWE si no ha sido almacenado ya y si no tiene un valor nulo
                if(aux_str!='NONE' and aux_str!='NVD-CWE-noinfo' and aux_str!='NVD-CWE-Other'):
                    if(aux_str not in array_cwes_sh):
                        array_cwes_sh.append(aux_str)
                    
    else:
        #Si la fila actual solamente tiene un valor de CWE, no es nulo y no ha sido almacenado, lo almaceno
        aux_str=df_cve_sh["CVE_Items.cve.problemtype.problemtype_data.description.value"][j].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
        if(aux_str!='NONE' and aux_str!='NVD-CWE-noinfo' and aux_str!='NVD-CWE-Other'):
            if(aux_str not in array_cwes_sh):
                array_cwes_sh.append(aux_str)  

#Recorro los distintos valores de CWES para la parte de SMART HOME
for r in range(0,len(array_cwes_sh)):
    #Vectores donde almacenare los valores de CVES asociados a cada una de las CWES para la parte SMART HOME
    array_cvesID_sh=[]
    array_cwes_cvesID_sh=[]
    #Recorro las distintas filas del fichero de SMART HOME
    for g in range(0,len(df_cve_sh["CVE_Items.cve.CVE_data_meta.ID"])):
        #Compruebo si en la fila actual existe un solo CWE o varios
        if('[' not in df_cve_sh["CVE_Items.cve.problemtype.problemtype_data.description.value"][g]):
            aux_strr=df_cve_sh["CVE_Items.cve.problemtype.problemtype_data.description.value"][g].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
            #Si el CWE de la fila actual coincide con el CWE que estamos comprobando, insertamos el CVE ID de la fila actual, para que sea relacionado con el CWE actual
            if(aux_strr == array_cwes_sh[r]):
                #Compruebo que no haya insertado anteriormente el CVE ID correspondiente en el vector de CVEs IDS
                if(df_cve_sh["CVE_Items.cve.CVE_data_meta.ID"][g] not in array_cvesID_sh):
                    array_cvesID_sh.append(df_cve_sh["CVE_Items.cve.CVE_data_meta.ID"][g])
        else:
            aux=df_cve_sh["CVE_Items.cve.problemtype.problemtype_data.description.value"][g].split(",")
            for l in range(0,len(aux)):
                if(len(aux)>0):
                    aux_strr=aux[l].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
                    #Si el CWE de la fila actual coincide con el CWE que estamos comprobando, insertamos el CVE ID de la fila actual, para que sea relacionado con el CWE actual
                    if(aux_strr == array_cwes_sh[r]):
                        #Compruebo que no haya insertado anteriormente el CVE ID correspondiente en el vector de CVEs IDS
                        if(df_cve_sh["CVE_Items.cve.CVE_data_meta.ID"][g] not in array_cvesID_sh):
                            array_cvesID_sh.append(df_cve_sh["CVE_Items.cve.CVE_data_meta.ID"][g])
    #Si hemos encontrado algun CVE asociado al actual CWE, insertamos el CWE y sus CVES asociados al vector global
    if(len(array_cvesID_sh) > 0):
        array_cwes_cvesID_sh.insert(0,array_cwes_sh[r])
        array_cwes_cvesID_sh.append(array_cvesID_sh)
        #Inserto el CWE actual y sus CVES asociados
        array_cwes_cves_sh.append(array_cwes_cvesID_sh)
        
#Vector donde almacenares los CWEs que aparecen tanto en la parte de IOT como SMART HOME        
array_cwes_iot_sh=[]  
#Inserto en el vector los vectores que estan incluidos en las dos partes y que no han sido insertados ya en el vector de CWES
for n in range(0,len(array_cwes_sh)):
    if((array_cwes_sh[n]  in array_cwes_iot) and (array_cwes_sh[n] not in array_cwes_iot_sh)):
        array_cwes_iot_sh.append(array_cwes_sh[n])

        
#Vector donde almacenare los CWES incluidos en la parte IOT y SMART HOME con sus correspondientes CVES
array_cwes_cvesid_iot_sh=[]
#Recorro primeramente el vector de CVES ID y CWES de la parte de smart home e IOT, para insertar los CVES ID asociados al CWE actual de la parte de smart home e IOT, segun corresponda
for b in range(0,len(array_cwes_iot_sh)):
    #Vector donde almaceno la relacion de CWES y CVES ID de CWES coincidentes para la parte IOT y SMART HOME
    cvesid_cwes_iot_sh=[]
    #Inserto primeramente el nombre del CWE actual
    cvesid_cwes_iot_sh.append(array_cwes_iot_sh[b])
    #Vector para almacenar los CVES ID asociados a la CWE actual
    cvesid_iot_sh=[]
    #Almaceno los CVES ID de la parte de IOT asociados a la CWE actual
    for p in range(0,len(array_cwes_cves_iot)):
        if(array_cwes_iot_sh[b] == array_cwes_cves_iot[p][0]):
            for t in range(0,len(array_cwes_cves_iot[p][1])):
                cvesid_iot_sh.append(array_cwes_cves_iot[p][1][t])
    #Almaceno los CVES ID de la parte de SMART HOME asociados a la CWE actual
    for d in range(0,len(array_cwes_cves_sh)):
        if(array_cwes_iot_sh[b] == array_cwes_cves_sh[d][0]):
            for t in range(0,len(array_cwes_cves_sh[d][1])):
                cvesid_iot_sh.append(array_cwes_cves_sh[d][1][t])
    #Inserto los cves id de la cwe actual
    cvesid_cwes_iot_sh.append(cvesid_iot_sh)
    #Inserto el vector de cves id al vector general de la relacion de cves ID y de CWES
    array_cwes_cvesid_iot_sh.append(cvesid_cwes_iot_sh)

#IMPRIMO LOS DISTINTOS CWES Y CVES ID ASOCIADOS SEGUN ESTEN EN LA PARTE IOT, SMART HOME, O EN AMBOS

print("*********************************************************************CWES RELACIONADOS CON CVES PARTE IOT********************************************************************* :")
print("\n")
for t in range(0,len(array_cwes_cves_iot)):
    if(array_cwes_cves_iot[t][0] not in array_cwes_iot_sh):
        print(" - EL CWE CON ID \033[1m"+array_cwes_cves_iot[t][0]+"  \033[0m tiene asociadas las siguientes CVES :")
        print("\n")
        print("      -  "+str(array_cwes_cves_iot[t][1]))
        print("\n")
        
        
print("*********************************************************************CWES RELACIONADOS CON CVES PARTE SMART HOME********************************************************************* :")
print("\n")    
#Imprimo cada CWE con sus respectivos CVES asociados
for t in range(0,len(array_cwes_cves_sh)):
    if(array_cwes_cves_sh[t][0] not in array_cwes_iot_sh):
        print(" - EL CWE CON ID \033[1m"+array_cwes_cves_sh[t][0]+" \033[0m tiene asociadas las siguientes CVES :")
        print("\n")
        print("      -  "+str(array_cwes_cves_sh[t][1]))
        print("\n")
        
print("*********************************************************************CWES COMUNES RELACIONADOS CON CVES PARTE IOT Y SMART HOME ********************************************************************* :")
print("\n") 
for t in range(0,len(array_cwes_cvesid_iot_sh)):
    print(" - EL CWE CON ID \033[1m"+array_cwes_cvesid_iot_sh[t][0]+" \033[0m tiene asociadas las siguientes CVES :")
    print("\n")
    print("      -  "+str(array_cwes_cvesid_iot_sh[t][1]))
    print("\n")

