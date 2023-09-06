import pandas as pd

#Abro los ficheros con los que voy a tratar


df_cve_iot=pd.read_excel('cves_iot_2023.xlsx')
df_cve_sh=pd.read_excel('cves_smart_home_2023.xlsx')


#Variables donde almacenare el contador de niveles de PRIVILEGIOS REQUERIDOS
count_high_severity_cvssv2_iot=0
count_low_severity_cvssv2_iot=0
count_medium_severity_cvssv2_iot=0
count_none_severity_cvssv2_iot=0

#Recorro los valores de SEVERIDAD y aumento los contadores segun su valor

for j in range(0,len(df_cve_iot["CVE_Items.impact.baseMetricV2.severity"])):
    if(df_cve_iot["CVE_Items.impact.baseMetricV2.severity"][j]=='HIGH'):
        count_high_severity_cvssv2_iot+=1
    elif(df_cve_iot["CVE_Items.impact.baseMetricV2.severity"][j]=='LOW'):
        count_low_severity_cvssv2_iot+=1
    elif(df_cve_iot["CVE_Items.impact.baseMetricV2.severity"][j]=='MEDIUM'):
        count_medium_severity_cvssv2_iot+=1
    else:
        count_none_severity_cvssv2_iot+=1

print("**************************ESTADÍSTICAS SEVERIDAD EN CVE SEGÚN VECTOR CVSSV2 IOT********************************")
print("\n")
print("LA SEVERIDAD EN "+str(count_high_severity_cvssv2_iot)+" VULNERABILIDADES ES ALTA \n")
print("LA SEVERIDAD EN "+str(count_low_severity_cvssv2_iot)+" VULNERABILIDADES ES BAJA \n")
print("LA SEVERIDAD EN "+str(count_medium_severity_cvssv2_iot)+" VULNERABILIDADES ES MEDIA \n")
print("LA SEVERIDAD EN "+str(count_none_severity_cvssv2_iot)+" VULNERABILIDADES NO VIENE ESPECIFICADA \n")
print("\n")
print("**************************PORCENTAJE SEVERIDAD EN CVE SEGÚN VECTOR CVSSV2 PARTE IOT********************************")
print("\n")
print("EL "+str(float(((count_high_severity_cvssv2_iot*100)/len(df_cve_iot["CVE_Items.impact.baseMetricV2.severity"]))))+"% DE LAS VULNERABILIDADES TIENE UNA SEVERIDAD ALTA \n")
print("EL "+str(float(((count_low_severity_cvssv2_iot*100)/len(df_cve_iot["CVE_Items.impact.baseMetricV2.severity"]))))+"% DE LAS VULNERABILIDADES TIENE UNA SEVERIDAD BAJA \n")
print("EL "+str(float(((count_medium_severity_cvssv2_iot*100)/len(df_cve_iot["CVE_Items.impact.baseMetricV2.severity"]))))+"% DE LAS VULNERABILIDADES TIENE UNA SEVERIDAD MEDIA \n")
print("EL "+str(float(((count_none_severity_cvssv2_iot*100)/len(df_cve_iot["CVE_Items.impact.baseMetricV2.severity"]))))+"% DE LAS VULNERABILIDADES NO TIENE NIVEL DE SEVERIDAD ESPECIFICADO \n")
print("\n")


#Variables donde almacenare el contador de niveles de PRIVILEGIOS REQUERIDOS
count_high_severity_cvssv2_sh=0
count_low_severity_cvssv2_sh=0
count_medium_severity_cvssv2_sh=0
count_none_severity_cvssv2_sh=0

#Recorro los valores de SEVERIDAD y aumento los contadores segun su valor

for j in range(0,len(df_cve_sh["CVE_Items.impact.baseMetricV2.severity"])):
    if(df_cve_sh["CVE_Items.impact.baseMetricV2.severity"][j]=='HIGH'):
        count_high_severity_cvssv2_sh+=1
    elif(df_cve_sh["CVE_Items.impact.baseMetricV2.severity"][j]=='LOW'):
        count_low_severity_cvssv2_sh+=1
    elif(df_cve_sh["CVE_Items.impact.baseMetricV2.severity"][j]=='MEDIUM'):
        count_medium_severity_cvssv2_sh+=1
    else:
        count_none_severity_cvssv2_sh+=1

print("**************************ESTADÍSTICAS SEVERIDAD EN CVE SEGÚN VECTOR CVSSV2 SMART HOME********************************")
print("\n")
print("LA SEVERIDAD EN "+str(count_high_severity_cvssv2_sh)+" VULNERABILIDADES ES ALTA \n")
print("LA SEVERIDAD EN "+str(count_low_severity_cvssv2_sh)+" VULNERABILIDADES ES BAJA \n")
print("LA SEVERIDAD EN "+str(count_medium_severity_cvssv2_sh)+" VULNERABILIDADES ES MEDIA \n")
print("LA SEVERIDAD EN "+str(count_none_severity_cvssv2_sh)+" VULNERABILIDADES NO VIENE ESPECIFICADA \n")
print("\n")
print("**************************PORCENTAJE SEVERIDAD EN CVE SEGÚN VECTOR CVSSV2 PARTE SMART HOME********************************")
print("\n")
print("EL "+str(float(((count_high_severity_cvssv2_sh*100)/len(df_cve_sh["CVE_Items.impact.baseMetricV2.severity"]))))+"% DE LAS VULNERABILIDADES TIENE UNA SEVERIDAD ALTA \n")
print("EL "+str(float(((count_low_severity_cvssv2_sh*100)/len(df_cve_sh["CVE_Items.impact.baseMetricV2.severity"]))))+"% DE LAS VULNERABILIDADES TIENE UNA SEVERIDAD BAJA \n")
print("EL "+str(float(((count_medium_severity_cvssv2_sh*100)/len(df_cve_sh["CVE_Items.impact.baseMetricV2.severity"]))))+"% DE LAS VULNERABILIDADES TIENE UNA SEVERIDAD MEDIA \n")
print("EL "+str(float(((count_none_severity_cvssv2_sh*100)/len(df_cve_sh["CVE_Items.impact.baseMetricV2.severity"]))))+"% DE LAS VULNERABILIDADES NO TIENE NIVEL DE SEVERIDAD ESPECIFICADO \n")
print("\n")


print("**************************ESTADÍSTICAS SEVERIDAD EN CVE SEGÚN VECTOR CVSSV2 PARTE IOT Y SMART HOME CONJUNTAS********************************")
print("\n")
print("LA SEVERIDAD EN "+str(count_high_severity_cvssv2_sh+count_high_severity_cvssv2_iot)+" VULNERABILIDADES ES ALTA \n")
print("LA SEVERIDAD EN "+str(count_low_severity_cvssv2_sh+count_low_severity_cvssv2_iot)+" VULNERABILIDADES ES BAJA \n")
print("LA SEVERIDAD EN "+str(count_medium_severity_cvssv2_sh+count_medium_severity_cvssv2_iot)+" VULNERABILIDADES ES MEDIA \n")
print("LA SEVERIDAD EN "+str(count_none_severity_cvssv2_sh+count_none_severity_cvssv2_iot)+" VULNERABILIDADES NO VIENE ESPECIFICADA \n")
print("\n")
print("**************************PORCENTAJE SEVERIDAD EN CVE SEGÚN VECTOR CVSSV2 PARTE IOT Y SMART HOME CONJUNTAS ********************************")
print("EL "+str(float((((count_high_severity_cvssv2_sh+count_high_severity_cvssv2_iot)*100)/(len(df_cve_sh["CVE_Items.impact.baseMetricV2.severity"])+len(df_cve_iot["CVE_Items.impact.baseMetricV2.severity"])))))+"% DE LAS VULNERABILIDADES TIENE UNA SEVERIDAD ALTA \n")
print("EL "+str(float((((count_low_severity_cvssv2_sh+count_low_severity_cvssv2_iot)*100)/(len(df_cve_sh["CVE_Items.impact.baseMetricV2.severity"])+len(df_cve_iot["CVE_Items.impact.baseMetricV2.severity"])))))+"% DE LAS VULNERABILIDADES TIENE UNA SEVERIDAD BAJA \n")
print("EL "+str(float((((count_medium_severity_cvssv2_sh+count_medium_severity_cvssv2_iot)*100)/(len(df_cve_sh["CVE_Items.impact.baseMetricV2.severity"])+len(df_cve_iot["CVE_Items.impact.baseMetricV2.severity"])))))+"% DE LAS VULNERABILIDADES TIENE UNA SEVERIDAD MEDIA \n")
print("EL "+str(float((((count_none_severity_cvssv2_sh+count_none_severity_cvssv2_iot)*100)/(len(df_cve_sh["CVE_Items.impact.baseMetricV2.severity"])+len(df_cve_iot["CVE_Items.impact.baseMetricV2.severity"])))))+"% DE LAS VULNERABILIDADES NO TIENE SEVERIDAD ESPECIFICADA \n")

