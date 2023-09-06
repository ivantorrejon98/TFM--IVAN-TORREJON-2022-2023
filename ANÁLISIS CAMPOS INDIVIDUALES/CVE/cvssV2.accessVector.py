import pandas as pd

#Abro los ficheros con los que voy a tratar


df_cve_iot=pd.read_excel('cves_iot_2023.xlsx')
df_cve_sh=pd.read_excel('cves_smart_home_2023.xlsx')

#Variables donde almacenare el contador de niveles de VECTOR DE ACCESO
count_network_vecacc_cvssv2_iot=0
count_Local_vecacc_cvssv2_iot=0
count_adjnet_vecacc_cvssv2_iot=0
count_none_vecacc_cvssV2_iot=0

#Recorro los valores de VECTOR ACCESO y aumento los contadores segun su valor

for k in range(0,len(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.accessVector"])):
    if(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.accessVector"][k]=='NETWORK'):
        count_network_vecacc_cvssv2_iot+=1
    elif(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.accessVector"][k]=='LOCAL'):
        count_Local_vecacc_cvssv2_iot+=1
    elif(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.accessVector"][k]=='ADJACENT_NETWORK'):
        count_adjnet_vecacc_cvssv2_iot+=1
    else:
        count_none_vecacc_cvssV2_iot+=1

print("**************************ESTADÍSTICAS VECTOR DE ACCESO EN CVE SEGÚN VECTOR CVSSV2 PARTE IOT ********************************")
print("\n")
print("EL VECTOR DE ACCESO EN "+str(count_network_vecacc_cvssv2_iot)+" VULNERABILIDADES ES A TRAVES DE LA RED \n")
print("EL VECTOR DE ACCESO EN "+str(count_Local_vecacc_cvssv2_iot)+" VULNERABILIDADES ES LOCAL \n")
print("EL VECTOR DE ACCESO EN "+str(count_adjnet_vecacc_cvssv2_iot)+" VULNERABILIDADES ES A TRAVES DE UNA RED ADYACENTE \n")
print("EL VECTOR DE ACCESO EN "+str(count_none_vecacc_cvssV2_iot)+" VULNERABILIDADES NO VIENE ESPECIFICADO \n")
print("\n")
print("**************************PORCENTAJE VECTOR DE ACCESO EN CVE SEGÚN VECTOR CVSSV2 PARTE IOT ********************************")
print("\n")
print("EL "+str(float(((count_network_vecacc_cvssv2_iot*100)/len(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.accessVector"]))))+"% DE LAS VULNERABILIDADES TIENE UN VECTOR DE ACCESO A TRAVES DE LA RED \n")
print("EL "+str(float(((count_Local_vecacc_cvssv2_iot*100)/len(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.accessVector"]))))+"% DE LAS VULNERABILIDADES TIENE UN VECTOR DE ACCESO LOCAL \n")
print("EL "+str(float(((count_adjnet_vecacc_cvssv2_iot*100)/len(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.accessVector"]))))+"% DE LAS VULNERABILIDADES TIENE UN VECTOR DE ACCESO A TRAVES DE UNA RED ADYACENTE \n")
print("EL "+str(float(((count_none_vecacc_cvssV2_iot*100)/len(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.accessVector"]))))+"% DE LAS VULNERABILIDADES NO TIENE VECTOR DE ACCESO ESPECIFICADO \n")
print("\n")



#Variables donde almacenare el contador de niveles de VECTOR DE ACCESO
count_network_vecacc_cvssv2_sh=0
count_Local_vecacc_cvssv2_sh=0
count_Physical_vecacc_cvssv2_sh=0
count_adjnet_vecacc_cvssv2_sh=0
count_none_vecacc_cvssV2_sh=0

#Recorro los valores de VECTOR DE ACCESO y aumento los contadores segun su valor

for g in range(0,len(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.accessVector"])):
    if(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.accessVector"][g]=='NETWORK'):
        count_network_vecacc_cvssv2_sh+=1
    elif(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.accessVector"][g]=='LOCAL'):
        count_Local_vecacc_cvssv2_sh+=1
    elif(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.accessVector"][g]=='ADJACENT_NETWORK'):
        count_adjnet_vecacc_cvssv2_sh+=1
    else:
        count_none_vecacc_cvssV2_sh+=1

print("**************************ESTADÍSTICAS VECTOR DE ACCESO EN EN CVE SEGÚN VECTOR CVSSV2 PARTE SMART HOME********************************")
print("\n")
print("EL VECTOR DE ACCESO EN "+str(count_network_vecacc_cvssv2_sh)+" VULNERABILIDADES ES A TRAVES DE LA RED \n")
print("EL VECTOR DE ACCESO EN "+str(count_Local_vecacc_cvssv2_sh)+" VULNERABILIDADES ES LOCAL \n")
print("EL VECTOR DE ACCESO EN "+str(count_adjnet_vecacc_cvssv2_sh)+" VULNERABILIDADES ES A TRAVES DE UNA RED ADYACENTE \n")
print("EL VECTOR DE ACCESO EN "+str(count_none_vecacc_cvssV2_sh)+" VULNERABILIDADES NO VIENE ESPECIFICADO \n")
print("\n")
print("**************************PORCENTAJE VECTOR DE ACCESO EN CVE SEGÚN VECTOR CVSSV2 PARTE SMART HOME********************************")
print("\n")
print("EL "+str(float(((count_network_vecacc_cvssv2_sh*100)/len(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.accessVector"]))))+"% DE LAS VULNERABILIDADES TIENE UN VECTOR DE ACCESO A TRAVES DE LA RED \n")
print("EL "+str(float(((count_Local_vecacc_cvssv2_sh*100)/len(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.accessVector"]))))+"% DE LAS VULNERABILIDADES TIENE UN VECTOR DE ACCESO LOCAL \n")
print("EL "+str(float(((count_adjnet_vecacc_cvssv2_sh*100)/len(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.accessVector"]))))+"% DE LAS VULNERABILIDADES TIENE UN VECTOR DE ACCESO A TRAVES DE UNA RED ADYACENTE \n")
print("EL "+str(float(((count_none_vecacc_cvssV2_sh*100)/len(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.accessVector"]))))+"% DE LAS VULNERABILIDADES NO TIENE VECTOR DE ACCESO ESPECIFICADO \n")
print("\n")




print("**************************ESTADÍSTICAS VECTOR DE ACCESO EN CVE SEGÚN VECTOR CVSSV2 PARTE IOT Y SMART HOME CONJUNTAS********************************")
print("\n")
print("EL VECTOR DE ACCESO EN "+str(count_network_vecacc_cvssv2_sh+count_network_vecacc_cvssv2_iot)+" VULNERABILIDADES ES A TRAVES DE LA RED \n")
print("EL VECTOR DE ACCESO EN "+str(count_Local_vecacc_cvssv2_sh+count_Local_vecacc_cvssv2_iot)+" VULNERABILIDADES ES LOCAL \n")
print("EL VECTOR DE ACCESO EN "+str(count_adjnet_vecacc_cvssv2_sh+count_adjnet_vecacc_cvssv2_iot)+" VULNERABILIDADES ES A TRAVES DE UNA RED ADYACENTE \n")
print("EL VECTOR DE ACCESO EN "+str(count_none_vecacc_cvssV2_sh+count_none_vecacc_cvssV2_iot)+" VULNERABILIDADES NO VIENE ESPECIFICADO \n")
print("\n")
print("**************************PORCENTAJE VECTOR DE ACCESO EN CVE SEGÚN VECTOR CVSSV2 PARTE IOT Y SMART HOME CONJUNTAS********************************")
print("\n")
print("EL "+str(float((((count_network_vecacc_cvssv2_sh+count_network_vecacc_cvssv2_iot)*100)/(len(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.accessVector"])+len(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.accessVector"])))))+"% DE LAS VULNERABILIDADES TIENE UN VECTOR DE ACCESO A TRAVES DE LA RED \n")
print("EL "+str(float((((count_Local_vecacc_cvssv2_sh+count_Local_vecacc_cvssv2_iot)*100)/(len(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.accessVector"])+len(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.accessVector"])))))+"% DE LAS VULNERABILIDADES TIENE UN VECTOR DE ACCESO LOCAL \n")
print("EL "+str(float((((count_adjnet_vecacc_cvssv2_sh+count_adjnet_vecacc_cvssv2_iot)*100)/(len(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.accessVector"])+len(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.accessVector"])))))+"% DE LAS VULNERABILIDADES TIENE UN VECTOR DE ACCESO A TRAVES DE UNA RED ADYACENTE \n")
print("EL "+str(float((((count_none_vecacc_cvssV2_sh+count_none_vecacc_cvssV2_iot)*100)/(len(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.accessVector"])+len(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.accessVector"])))))+"% DE LAS VULNERABILIDADES NO TIENE VECTOR DE ACCESO ESPECIFICADO \n")
print("\n")
