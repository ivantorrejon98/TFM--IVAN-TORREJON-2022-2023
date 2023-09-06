import pandas as pd

#Abro los ficheros con los que voy a tratar

df_cve_iot=pd.read_excel('cves_iot_2023.xlsx')
df_cve_sh=pd.read_excel('cves_smart_home_2023.xlsx')

#Variables donde almacenare el contador de versiones cvss CVE CVSSV3 para IOT
cve_cvssv3_version_3_0_iot=0
cve_cvssv3_version_3_1_iot=0
cve_cvssv3_no_version_iot=0



#Compruebo la version cvss CVE CVSSV3 para IOT
for j in range(0,len(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.version"])):
    if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.version"][j] =='3.1'):
        cve_cvssv3_version_3_1_iot+=1
    elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.version"][j] =='3.0'):
        cve_cvssv3_version_3_0_iot+=1
    else:
        cve_cvssv3_no_version_iot+=1
        
        
print("**************************ESTADÍSTICAS CVE VERSION VECTOR CVSSV3 PARTE IOT********************************")
print("\n")
print(" EN "+str(cve_cvssv3_version_3_0_iot)+" VULNERABILIDADES LA VERSION CVSS ES 3.0 \n")
print(" EN "+str(cve_cvssv3_version_3_1_iot)+" VULNERABILIDADES LA VERSION CVSS ES 3.1 \n")
print(" EN "+str(cve_cvssv3_no_version_iot)+" VULNERABILIDADES NO SE ESPECIFICA LA VERSION CVSS \n")
print("\n")
print("************************** PORCENTAJE ESTADÍSTICAS CVE VERSION VECTOR CVSSV3 PARTE IOT********************************")
print("\n")
print("EN EL "+str(float(((cve_cvssv3_version_3_0_iot*100)/len(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.version"]))))+"% DE LAS VULNERABILIDADES LA VERSION CVSS ES 3.0 \n")
print("EN EL "+str(float(((cve_cvssv3_version_3_1_iot*100)/len(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.version"]))))+"% DE LAS VULNERABILIDADES LA VERSION CVSS ES 3.1 \n")
print("EN EL "+str(float(((cve_cvssv3_no_version_iot*100)/len(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.version"]))))+"% DE LAS VULNERABILIDADES NO SE ESPECIFICA LA VERSION CVSS \n")
print("\n")        
        

#Variables donde almacenare el contador de versiones cvss CVE CVSSV3 para SMART HOME
cve_cvssv3_version_3_0_sh=0
cve_cvssv3_version_3_1_sh=0
cve_cvssv3_no_version_sh=0



#Compruebo la version cvss CVE CVSSV3 para SMART HOME
for r in range(0,len(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.version"])):
    if(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.version"][r] =='3.1'):
        cve_cvssv3_version_3_1_sh+=1
    elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.version"][r] =='3.0'):
        cve_cvssv3_version_3_0_sh+=1
    else:
        cve_cvssv3_no_version_sh+=1
        
        
print("**************************ESTADÍSTICAS CVE VERSION VECTOR CVSSV3 PARTE SMART HOME********************************")
print("\n")
print(" EN "+str(cve_cvssv3_version_3_0_sh)+" VULNERABILIDADES LA VERSION CVSS ES 3.0 \n")
print(" EN "+str(cve_cvssv3_version_3_1_sh)+" VULNERABILIDADES LA VERSION CVSS ES 3.1 \n")
print(" EN "+str(cve_cvssv3_no_version_sh)+" VULNERABILIDADES NO SE ESPECIFICA LA VERSION CVSS \n")
print("\n")
print("************************** PORCENTAJE CVE VERSION VECTOR CVSSV3 PARTE SMART HOME********************************")
print("\n")
print("EN EL "+str(float(((cve_cvssv3_version_3_0_sh*100)/len(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.version"]))))+"% DE LAS VULNERABILIDADES LA VERSION CVSS ES 3.0 \n")
print("EN EL "+str(float(((cve_cvssv3_version_3_1_sh*100)/len(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.version"]))))+"% DE LAS VULNERABILIDADES LA VERSION CVSS ES 3.1 \n")
print("EN EL "+str(float(((cve_cvssv3_no_version_sh*100)/len(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.version"]))))+"% DE LAS VULNERABILIDADES NO SE ESPECIFICA LA VERSION CVSS \n")
print("\n")        
        
    

print("**************************ESTADÍSTICAS CVE VERSION VECTOR CVSSV3 PARTE IOT Y SMART HOME CONJUNTAS ********************************")
print("\n")
print("\n")
print(" EN "+str(cve_cvssv3_version_3_0_sh+cve_cvssv3_version_3_0_iot)+" VULNERABILIDADES LA VERSION CVSS ES 3.0 \n")
print(" EN "+str(cve_cvssv3_version_3_1_sh+cve_cvssv3_version_3_1_iot)+" VULNERABILIDADES LA VERSION CVSS ES 3.1 \n")
print(" EN "+str(cve_cvssv3_no_version_sh+cve_cvssv3_no_version_iot)+" VULNERABILIDADES LA VERSIONNO VIENE ESPECIFICADA \n")

print("\n")
print("\n")
print("***************************PORCENTAJE CVE VERSION VECTOR CVSSV3 PARTE IOT Y SMART HOME CONJUNTAS********************************")
print("\n")
print("EN EL "+str(float((((cve_cvssv3_version_3_0_sh+cve_cvssv3_version_3_0_iot)*100)/(len(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.version"])+len(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.version"])))))+"% DE LAS VULNERABILIDADES LA VERSION CVSS ES 3.0 \n")
print("EN EL "+str(float((((cve_cvssv3_version_3_1_sh+cve_cvssv3_version_3_1_iot)*100)/(len(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.version"])+len(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.version"])))))+"% DE LAS VULNERABILIDADES LA VERSION CVSS ES 3.1 \n")
print("EN EL "+str(float((((cve_cvssv3_no_version_sh+cve_cvssv3_no_version_iot)*100)/(len(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.version"])+len(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.version"])))))+"% DE LAS VULNERABILIDADES NO VIENE LA VERSION ESPECIFICADA \n")
print("\n")
print("\n")
print("\n")
