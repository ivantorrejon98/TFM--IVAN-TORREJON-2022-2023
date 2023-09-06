import pandas as pd

#Abro los ficheros con los que voy a tratar


df_cve_iot=pd.read_excel('cves_iot_2023.xlsx')
df_cve_sh=pd.read_excel('cves_smart_home_2023.xlsx')



#Variables donde almacenare el contador de niveles de AUTENTICACION DE USUARIO REQUERIDA
count_single_authentication_iot=0
count_multiple_authentication_iot=0
count_none_authentication_iot=0



#Recorro los valores de AUTENTICACION y aumento los contadores segun su valor

for j in range(0,len(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.authentication"])):
    if(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.authentication"][j]=="SINGLE"):
        count_single_authentication_iot+=1
    elif(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.authentication"][j]=="MULTIPLE"):
        count_multiple_authentication_iot+=1
    else:
        count_none_authentication_iot+=1
    


print("**************************ESTADÍSTICAS AUTENTICACION EN CVE SEGÚN VECTOR CVSSV2 PARTE IOT  ********************************")
print("\n")
print(" EN "+str(count_single_authentication_iot)+" VULNERABILIDADES LA AUTENTICATION ES SENCILLA \n")
print(" EN "+str(count_multiple_authentication_iot)+" VULNERABILIDADES LA AUTENTICATION ES MULTIPLE \n")
print(" EN "+str(count_none_authentication_iot)+" VULNERABILIDADES LA AUTENTICACION NO ES REQUERIDA \n")
print("\n")
print("************************** PORCENTAJES AUTENTICACION REQUERIDA EN CVE SEGÚN VECTOR CVSSV2 PARTE IOT********************************")
print("\n")
print("EN EL "+str(float(((count_single_authentication_iot*100)/len(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.authentication"]))))+"% DE LAS VULNERABILIDADES LA AUTENTICACION ES SENCILLA \n")
print("EN EL "+str(float(((count_multiple_authentication_iot*100)/len(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.authentication"]))))+"% DE LAS VULNERABILIDADES LA AUTENTICACION ES MULTIPLE \n")
print("EN EL "+str(float(((count_none_authentication_iot*100)/len(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.authentication"]))))+"% DE LAS VULNERABILIDADES LA AUTENTICACION NO ES REQUERIDA \n")
print("\n")



#Variables donde almacenare el contador de niveles de AUTENTICACION DE USUARIO REQUERIDA
count_single_authentication_sh=0
count_multiple_authentication_sh=0
count_none_authentication_sh=0



#Recorro los valores de AUTENTICACION y aumento los contadores segun su valor

for l in range(0,len(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.authentication"])):
    if(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.authentication"][l]=="SINGLE"):
        count_single_authentication_sh+=1
    elif(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.authentication"][l]=="MULTIPLE"):
        count_multiple_authentication_sh+=1
    else:
        count_none_authentication_sh+=1
    


print("**************************ESTADÍSTICAS AUTENTICACION EN CVE SEGÚN VECTOR CVSSV2 PARTE SMART HOME ********************************")
print("\n")
print(" EN "+str(count_single_authentication_sh)+" VULNERABILIDADES LA AUTENTICATION ES SENCILLA \n")
print(" EN "+str(count_multiple_authentication_sh)+" VULNERABILIDADES LA AUTENTICATION ES MULTIPLE \n")
print(" EN "+str(count_none_authentication_sh)+" VULNERABILIDADES LA AUTENTICACION NO ES REQUERIDA \n")
print("\n")
print("************************** PORCENTAJES AUTENTICACION REQUERIDA EN CVE SEGÚN VECTOR CVSSV2 PARTE SMART HOME ********************************")
print("\n")
print("EN EL "+str(float(((count_single_authentication_sh*100)/len(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.authentication"]))))+"% DE LAS VULNERABILIDADES LA AUTENTICACION ES SENCILLA \n")
print("EN EL "+str(float(((count_multiple_authentication_sh*100)/len(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.authentication"]))))+"% DE LAS VULNERABILIDADES LA AUTENTICACION ES MULTIPLE \n")
print("EN EL "+str(float(((count_none_authentication_sh*100)/len(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.authentication"]))))+"% DE LAS VULNERABILIDADES LA AUTENTICACION NO ES REQUERIDA \n")
print("\n")





print("**************************ESTADÍSTICAS AUTENTICACION EN CVE SEGÚN VECTOR CVSSV2 PARTE IOT Y SMART HOME CONJUNTAS ********************************")
print("\n")
print(" EN "+str(count_single_authentication_sh+count_single_authentication_iot)+" VULNERABILIDADES LA AUTENTICATION ES SENCILLA \n")
print(" EN "+str(count_multiple_authentication_sh+count_multiple_authentication_iot)+" VULNERABILIDADES LA AUTENTICATION ES MULTIPLE \n")
print(" EN "+str(count_none_authentication_sh+count_none_authentication_iot)+" VULNERABILIDADES LA AUTENTICACION NO ES REQUERIDA \n")
print("\n")
print("************************** PORCENTAJES AUTENTICACION REQUERIDA EN CVE SEGÚN VECTOR CVSSV2 PARTE IOT Y SMART HOME CONJUNTAS********************************")
print("\n")
print("EN EL "+str(float((((count_single_authentication_sh+count_single_authentication_iot)*100)/(len(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.authentication"])+len(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.authentication"])))))+"% DE LAS VULNERABILIDADES LA AUTENTICACION ES SENCILLA \n")
print("EN EL "+str(float((((count_multiple_authentication_sh+count_multiple_authentication_iot)*100)/(len(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.authentication"])+len(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.authentication"])))))+"% DE LAS VULNERABILIDADES LA AUTENTICACION ES MULTIPLE \n")
print("EN EL "+str(float((((count_none_authentication_sh+count_none_authentication_iot)*100)/(len(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.authentication"])+len(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.authentication"])))))+"% DE LAS VULNERABILIDADES LA AUTENTICACION NO ES REQUERIDA \n")
print("\n")