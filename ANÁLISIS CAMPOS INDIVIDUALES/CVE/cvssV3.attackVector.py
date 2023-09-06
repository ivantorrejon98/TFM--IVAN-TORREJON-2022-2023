import pandas as pd

#Abro los ficheros con los que voy a tratar


df_cve_iot=pd.read_excel('cves_iot_2023.xlsx')
df_cve_sh=pd.read_excel('cves_smart_home_2023.xlsx')


#Variables donde almacenare el contador de niveles de VECTOR DE ATAQUE
count_network_vecacc_cvssv3_iot=0
count_Local_vecacc_cvssv3_iot=0
count_Physical_vecacc_cvssv3_iot=0
count_adjnet_vecacc_cvssv3_iot=0
count_none_vecacc_cvssV3_iot=0

#Recorro los valores de VECTOR DE ATAQUE y aumento los contadores segun su valor

for j in range(0,len(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.attackVector"])):
    if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.attackVector"][j]=='NETWORK'):
        count_network_vecacc_cvssv3_iot+=1
    elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.attackVector"][j]=='LOCAL'):
        count_Local_vecacc_cvssv3_iot+=1
    elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.attackVector"][j]=='PHYSICAL'):
        count_Physical_vecacc_cvssv3_iot+=1
    elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.attackVector"][j]=='ADJACENT_NETWORK'):
        count_adjnet_vecacc_cvssv3_iot+=1
    else:
        count_none_vecacc_cvssV3_iot+=1

print("**************************ESTADÍSTICAS VECTOR DE ATAQUE EN CVE SEGÚN VECTOR CVSSV3 PARTE IOT********************************")
print("\n")
print("EL VECTOR DE ATAQUE EN "+str(count_network_vecacc_cvssv3_iot)+" VULNERABILIDADES ES A TRAVES DE LA RED \n")
print("EL VECTOR DE ATAQUE EN "+str(count_Local_vecacc_cvssv3_iot)+" VULNERABILIDADES ES LOCAL \n")
print("EL VECTOR DE ATAQUE EN "+str(count_Physical_vecacc_cvssv3_iot)+" VULNERABILIDADES ES FISICO \n")
print("EL VECTOR DE ATAQUE EN "+str(count_adjnet_vecacc_cvssv3_iot)+" VULNERABILIDADES ES A TRAVES DE UNA RED ADYACENTE \n")
print("EL VECTOR DE ATAQUE EN "+str(count_none_vecacc_cvssV3_iot)+" VULNERABILIDADES NO VIENE ESPECIFICADO \n")
print("\n")
print("**************************PORCENTAJE VECTOR DE ATAQUE EN CVE SEGÚN VECTOR CVSSV3 PARTE IOT********************************")
print("\n")
print("EN EL "+str(float(((count_network_vecacc_cvssv3_iot*100)/len(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.attackVector"]))))+"% DE LAS VULNERABILIDADES EL VECTOR DE ATAQUE ES A TRAVES DE LA RED \n")
print("EN EL "+str(float(((count_Local_vecacc_cvssv3_iot*100)/len(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.attackVector"]))))+"% DE LAS VULNERABILIDADES EL VECTOR DE ATAQUE ES LOCAL \n")
print("EN EL "+str(float(((count_Physical_vecacc_cvssv3_iot*100)/len(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.attackVector"]))))+"% DE LAS VULNERABILIDADES EL VECTOR DE ATAQUE ES FISICO \n")
print("EN EL "+str(float(((count_adjnet_vecacc_cvssv3_iot*100)/len(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.attackVector"]))))+"% DE LAS VULNERABILIDADES EL VECTOR DE ATAQUE ES A TRAVES DE UNA RED ADYACENTE \n")
print("EN EL "+str(float(((count_none_vecacc_cvssV3_iot*100)/len(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.attackVector"]))))+"% DE LAS VULNERABILIDADES NO ESTÁ EL VECTOR DE ATAQUE ESPECIFICADO \n")
print("\n")



#Variables donde almacenare el contador de niveles de VECTOR DE ATAQUE
count_network_vecacc_cvssv3_sh=0
count_Local_vecacc_cvssv3_sh=0
count_Physical_vecacc_cvssv3_sh=0
count_adjnet_vecacc_cvssv3_sh=0
count_none_vecacc_cvssV3_sh=0

#Recorro los valores de VECTOR DE ATAQUE y aumento los contadores segun su valor

for r in range(0,len(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.attackVector"])):
    if(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.attackVector"][r]=='NETWORK'):
        count_network_vecacc_cvssv3_sh+=1
    elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.attackVector"][r]=='LOCAL'):
        count_Local_vecacc_cvssv3_sh+=1
    elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.attackVector"][r]=='PHYSICAL'):
        count_Physical_vecacc_cvssv3_sh+=1
    elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.attackVector"][r]=='ADJACENT_NETWORK'):
        count_adjnet_vecacc_cvssv3_sh+=1
    else:
        count_none_vecacc_cvssV3_sh+=1

print("**************************ESTADÍSTICAS VECTOR DE ATAQUE EN CVE SEGÚN VECTOR CVSSV3 PARTE SMART HOME********************************")
print("\n")
print("EL VECTOR DE ATAQUE EN "+str(count_network_vecacc_cvssv3_sh)+" VULNERABILIDADES ES A TRAVES DE LA RED \n")
print("EL VECTOR DE ATAQUE EN "+str(count_Local_vecacc_cvssv3_sh)+" VULNERABILIDADES ES LOCAL \n")
print("EL VECTOR DE ATAQUE EN "+str(count_Physical_vecacc_cvssv3_sh)+" VULNERABILIDADES ES FISICO \n")
print("EL VECTOR DE ATAQUE EN "+str(count_adjnet_vecacc_cvssv3_sh)+" VULNERABILIDADES ES A TRAVES DE UNA RED ADYACENTE \n")
print("EL VECTOR DE ATAQUE EN "+str(count_none_vecacc_cvssV3_sh)+" VULNERABILIDADES NO VIENE ESPECIFICADO \n")
print("\n")
print("**************************PORCENTAJE VECTOR DE ATAQUE EN CVE SEGÚN VECTOR CVSSV3 PARTE SMART HOME********************************")
print("\n")
print("EN EL "+str(float(((count_network_vecacc_cvssv3_sh*100)/len(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.attackVector"]))))+"% DE LAS VULNERABILIDADES EL VECTOR DE ATAQUE ES A TRAVES DE LA RED \n")
print("EN EL "+str(float(((count_Local_vecacc_cvssv3_sh*100)/len(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.attackVector"]))))+"% DE LAS VULNERABILIDADES EL VECTOR DE ATAQUE ES LOCAL \n")
print("EN EL "+str(float(((count_Physical_vecacc_cvssv3_sh*100)/len(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.attackVector"]))))+"% DE LAS VULNERABILIDADES EL VECTOR DE ATAQUE ES FISICO \n")
print("EN EL "+str(float(((count_adjnet_vecacc_cvssv3_sh*100)/len(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.attackVector"]))))+"% DE LAS VULNERABILIDADES EL VECTOR DE ATAQUE ES A TRAVES DE UNA RED ADYACENTE \n")
print("EN EL "+str(float(((count_none_vecacc_cvssV3_sh*100)/len(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.attackVector"]))))+"% DE LAS VULNERABILIDADES EL VECTOR DE ATAQUE NO VIENE ESPECIFICADO \n")
print("\n")



print("**************************ESTADÍSTICAS VECTOR DE ATAQUE EN CVE SEGÚN VECTOR CVSSV3 PARTE IOT Y SMART HOME CONJUNTAS ********************************")
print("\n")
print("EL VECTOR DE ATAQUE EN "+str(count_network_vecacc_cvssv3_sh+count_network_vecacc_cvssv3_iot)+" VULNERABILIDADES ES A TRAVES DE LA RED \n")
print("EL VECTOR DE ATAQUE EN "+str(count_Local_vecacc_cvssv3_sh+count_Local_vecacc_cvssv3_iot)+" VULNERABILIDADES ES LOCAL \n")
print("EL VECTOR DE ATAQUE EN "+str(count_Physical_vecacc_cvssv3_sh+count_Physical_vecacc_cvssv3_iot)+" VULNERABILIDADES ES FISICO \n")
print("EL VECTOR DE ATAQUE EN "+str(count_adjnet_vecacc_cvssv3_sh+count_adjnet_vecacc_cvssv3_iot)+" VULNERABILIDADES ES A TRAVES DE UNA RED ADYACENTE \n")
print("EL VECTOR DE ATAQUE EN "+str(count_none_vecacc_cvssV3_sh+count_none_vecacc_cvssV3_iot)+" VULNERABILIDADES NO VIENE ESPECIFICADO \n")
print("\n")
print("**************************PORCENTAJE VECTOR DE ATAQUE EN CVE SEGÚN VECTOR CVSSV3 PARTE IOT Y SMART HOME CONJUNTAS********************************")
print("\n")
print(" EN EL "+str(float((((count_network_vecacc_cvssv3_sh+count_network_vecacc_cvssv3_iot)*100)/(len(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.attackVector"])+len(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.attackVector"])))))+"% DE LAS VULNERABILIDADES EL VECTOR DE ATAQUE ES A TRAVES DE LA RED \n")
print("EN EL "+str(float((((count_Local_vecacc_cvssv3_sh+count_Local_vecacc_cvssv3_iot)*100)/(len(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.attackVector"])+len(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.attackVector"])))))+"% DE LAS VULNERABILIDADES EL VECTOR DE ATAQUE ES LOCAL \n")
print("EN EL "+str(float((((count_Physical_vecacc_cvssv3_sh+count_Physical_vecacc_cvssv3_iot)*100)/(len(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.attackVector"])+len(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.attackVector"])))))+"% DE LAS VULNERABILIDADES EL VECTOR DE ATAQUE ES FISICO \n")
print("EN EL "+str(float((((count_adjnet_vecacc_cvssv3_sh+count_adjnet_vecacc_cvssv3_iot)*100)/(len(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.attackVector"])+len(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.attackVector"])))))+"% DE LAS VULNERABILIDADES EL VECTOR DE ATAQUE ES A TRAVES DE UNA RED ADYACENTE \n")
print("EN EL "+str(float((((count_none_vecacc_cvssV3_sh+count_none_vecacc_cvssV3_iot)*100)/(len(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.attackVector"])+len(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.attackVector"])))))+"% DE LAS VULNERABILIDADES NO VIENE EL VECTOR DE ATAQUE ESPECIFICADO \n")
print("\n")