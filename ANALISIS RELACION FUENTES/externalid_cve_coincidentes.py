import pandas as pd 

#Abro los distintos ficheros con los que trabajare 
df_vuln_ibm_iot = pd.read_excel('vulnerabilidades_ibm_iot_2023.xlsx')
df_cve_iot = pd.read_excel('cves_iot_2023.xlsx')
df_vuln_ibm_sh = pd.read_excel('vulnerabilidades_ibm_smart_home_2023.xlsx')
df_cve_sh = pd.read_excel('cves_smart_home_2023.xlsx')


#Vector donde guardare las external_references_id del fichero de vulnerabilidades IBM para IOT
external_references_external_id_iot=[]
#Vector donde guardare las external_references_id del fichero de vulnerabilidades IBM para SMART HOME
external_references_external_id_sh=[]
#Vector donde guardare los ids de CVEs para IOT
cves_id_iot=[]
#Vector donde guardare los ids de CVEs para SMART HOME
cves_id_sh=[]

#Vectores donde guardare las external references y los cves coincidentes para IOT
ext_ref_id_cves_coinc_iot=[]
#Vectores donde guardare las external references y los cves coincidentes para SMART HOME
ext_ref_id_cves_coinc_sh=[]
#Vectores donde guardare las external references DE IOT y los cves coincidentes para SMART HOME
ext_ref_id_cves_coinc_iotsh=[]
#Vectores donde guardare las external references SMART HOME y los cves coincidentes para IOT
ext_ref_id_cves_coinc_shiot=[]


#Almaceno todas las external references ID de IBM en su vector para IOT
for i in range(0,len(df_vuln_ibm_iot["external_references_external_id"])):
    if(df_vuln_ibm_iot["external_references_external_id"][i] !='NONE'):
        external_references_external_id_iot.append(df_vuln_ibm_iot["external_references_external_id"][i])
        
#Almaceno todas las external references ID de IBM en su vector para SMART HOME  
for j in range(0,len(df_vuln_ibm_sh["external_references_external_id"])):
    if(df_vuln_ibm_sh["external_references_external_id"][j] !='NONE'):
        external_references_external_id_sh.append(df_vuln_ibm_sh["external_references_external_id"][j]) 

#Almaceno todas los ids de las CVES en su vector para IOT 
for h in range(0,len(df_cve_iot["CVE_Items.cve.CVE_data_meta.ID"])):
    if(df_cve_iot["CVE_Items.cve.CVE_data_meta.ID"][h] !='NONE'):
        cves_id_iot.append(df_cve_iot["CVE_Items.cve.CVE_data_meta.ID"][h])         

#Almaceno todas los ids de las CVES en su vector para SMART HOME
for k in range(0,len(df_cve_sh["CVE_Items.cve.CVE_data_meta.ID"])):
    if(df_cve_sh["CVE_Items.cve.CVE_data_meta.ID"][k] !='NONE'):
        cves_id_sh.append(df_cve_sh["CVE_Items.cve.CVE_data_meta.ID"][k]) 
        
#Busco si hay IDS de CVES y external_references ID de IBM para la parte de IOT coincidentes
for elem in external_references_external_id_iot:
    if elem in cves_id_iot:
        ext_ref_id_cves_coinc_iot.append(elem)

#Busco si hay IDS de CVES y external_references ID de IBM para la parte de SMART HOME coincidentes
for elem_sh in external_references_external_id_sh:
    if elem_sh in cves_id_sh:
        ext_ref_id_cves_coinc_sh.append(elem_sh)

        
#Busco si hay IDS de CVES para la parte SMART HOME y external_references ID de IBM para la parte de IOT coincidentes
for elem_iotsh in external_references_external_id_iot:
    if elem_iotsh in cves_id_sh:
        ext_ref_id_cves_coinc_iotsh.append(elem_iotsh)
        
        
#Busco si hay IDS de CVES para la parte IOT y external_references ID de IBM para la parte de SMART HOME coincidentes
for elem_shiot in external_references_external_id_sh:
    if elem_shiot in cves_id_iot:
        ext_ref_id_cves_coinc_shiot.append(elem_shiot)
        
#Imprimo si existen los resultados coincidentes para IOT 
if(len(ext_ref_id_cves_coinc_iot)>0):
    print("- EXISTEN "+str(len(ext_ref_id_cves_coinc_iot))+" IDENTIFICADORES DE CVES COINCIDENTES CON IDS DE REFERENCIAS EXTERNAS DE INFORMES DE ACTIVIDAD DE AMENAZAS IBM  PARA LA PARTE IOT :")
    print("\n")
    for x in range(0,len(ext_ref_id_cves_coinc_iot)):
        print("     -  "+ext_ref_id_cves_coinc_iot[x]+"\n")
else:
    print("NO HAY IDENTIFICADORES DE CVES COINCIDENTES CON IDS DE REFERENCIAS EXTERNAS EN INFORMES DE ACTIVIDAD DE AMENAZAS IBM PARA LA PARTE IOT")
print("\n")

#Imprimo si existen los resultados coincidentes para SMART HOME
if(len(ext_ref_id_cves_coinc_sh)>0):
    print("- EXISTEN "+str(len(ext_ref_id_cves_coinc_sh))+" IDENTIFICADORES DE CVES COINCIDENTES CON IDS DE REFERENCIAS EXTERNAS DE INFORMES DE ACTIVIDAD DE AMENAZAS IBM  PARA LA PARTE SMART HOME :")
    print("\n")
    for x in range(0,len(ext_ref_id_cves_coinc_sh)):
        print("     -  "+ext_ref_id_cves_coinc_sh[x]+"\n")
else:
    print("NO HAY IDENTIFICADORES DE CVES COINCIDENTES CON IDS DE REFERENCIAS EXTERNAS EN INFORMES DE ACTIVIDAD DE AMENAZAS IBM PARA LA PARTE SMART HOME")
print("\n")







#Imprimo si existen los resultados coincidentes para IBM parte IOT y CVE parte SMART HOME
if(len(ext_ref_id_cves_coinc_iotsh)>0):
    print("- EXISTEN "+str(len(ext_ref_id_cves_coinc_iotsh))+" IDENTIFICADORES DE CVES DE LA PARTE SMART HOME COINCIDENTES CON IDS DE REFERENCIAS EXTERNAS DE INFORMES DE ACTIVIDAD DE AMENAZAS IBM  PARA LA PARTE IOT :")
    print("\n")
    for x in range(0,len(ext_ref_id_cves_coinc_iotsh)):
        print("     -  "+ext_ref_id_cves_coinc_iotsh[x]+"\n")
else:
    print("NO HAY IDENTIFICADORES DE CVES DE LA PARTE SMART HOME COINCIDENTES CON IDS DE REFERENCIAS EXTERNAS EN INFORMES DE ACTIVIDAD DE AMENAZAS IBM PARA LA PARTE IOT")
print("\n")







#Imprimo si existen los resultados coincidentes para IBM parte SMART HOME y CVE parte IOT
if(len(ext_ref_id_cves_coinc_shiot)>0):
    print("- EXISTEN "+str(len(ext_ref_id_cves_coinc_shiot))+" IDENTIFICADORES DE CVES DE LA PARTE SMART IOT COINCIDENTES CON IDS DE REFERENCIAS EXTERNAS DE INFORMES DE ACTIVIDAD DE AMENAZAS IBM  PARA LA PARTE SMART HOME :")
    print("\n")
    for x in range(0,len(ext_ref_id_cves_coinc_shiot)):
        print("     -  "+ext_ref_id_cves_coinc_shiot[x]+"\n")
else:
    print("NO HAY IDENTIFICADORES DE CVES DE LA PARTE IOT COINCIDENTES CON IDS DE REFERENCIAS EXTERNAS EN INFORMES DE ACTIVIDAD DE AMENAZAS IBM PARA LA PARTE SMART HOME")
print("\n")

