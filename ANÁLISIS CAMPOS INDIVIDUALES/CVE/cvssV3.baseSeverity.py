import pandas as pd

#Abro los ficheros con los que voy a tratar


df_cve_iot=pd.read_excel('cves_iot_2023.xlsx')
df_cve_sh=pd.read_excel('cves_smart_home_2023.xlsx')


#Variables donde almacenare el contador de niveles de SEVERIDAD BASE
count_high_severity_cvssv3_iot=0
count_low_severity_cvssv3_iot=0
count_medium_severity_cvssv3_iot=0
count_critical_severity_cvssv3_iot=0
count_none_severity_cvssV3_iot=0

#Recorro los valores de SEVERIDAD BASE y aumento los contadores segun su valor

for j in range(0,len(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.baseSeverity"])):
    if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.baseSeverity"][j]=='HIGH'):
        count_high_severity_cvssv3_iot+=1
    elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.baseSeverity"][j]=='LOW'):
        count_low_severity_cvssv3_iot+=1
    elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.baseSeverity"][j]=='MEDIUM'):
        count_medium_severity_cvssv3_iot+=1
    elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.baseSeverity"][j]=='CRITICAL'):
        count_critical_severity_cvssv3_iot+=1
    else:
        count_none_severity_cvssV3_iot+=1

print("**************************ESTADÍSTICAS SEVERIDAD BASE CVE SEGÚN VECTOR CVSSV3 PARTE IOT********************************")
print("\n")
print("LA SEVERIDAD BASE EN "+str(count_high_severity_cvssv3_iot)+" VULNERABILIDADES ES ALTA \n")
print("LA SEVERIDAD BASE EN "+str(count_low_severity_cvssv3_iot)+" VULNERABILIDADES ES BAJA \n")
print("LA SEVERIDAD BASE EN "+str(count_medium_severity_cvssv3_iot)+" VULNERABILIDADES ES MEDIA \n")
print("LA SEVERIDAD BASE EN "+str(count_critical_severity_cvssv3_iot)+" VULNERABILIDADES ES CRITICA \n")
print("EN "+str(count_none_severity_cvssV3_iot)+" VULNERABILIDADES NO HAY SEVERIDAD BASE \n")
print("\n")
print("**************************PORCENTAJE SEVERIDAD BASE CVE SEGÚN VECTOR CVSSV3 PARTE IOT********************************")
print("\n")
print("EL "+str(float(((count_high_severity_cvssv3_iot*100)/len(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.baseSeverity"]))))+"% DE LAS VULNERABILIDADES TIENE UNA SEVERIDAD BASE ALTA \n")
print("EL "+str(float(((count_low_severity_cvssv3_iot*100)/len(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.baseSeverity"]))))+"% DE LAS VULNERABILIDADES TIENE UNA SEVERIDAD BASE BAJA \n")
print("EL "+str(float(((count_medium_severity_cvssv3_iot*100)/len(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.baseSeverity"]))))+"% DE LAS VULNERABILIDADES TIENE UNA SEVERIDAD BASE MEDIA \n")
print("EL "+str(float(((count_critical_severity_cvssv3_iot*100)/len(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.baseSeverity"]))))+"% DE LAS VULNERABILIDADES TIENE UNA SEVERIDAD BASE CRITICA \n")
print("EL "+str(float(((count_none_severity_cvssV3_iot*100)/len(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.baseSeverity"]))))+"% DE LAS VULNERABILIDADES NO TIENE NIVEL DE SEVERIDAD ESPECIFICADO \n")
print("\n")


#Variables donde almacenare el contador de niveles de SEVERIDAD BASE
count_high_severity_cvssv3_sh=0
count_low_severity_cvssv3_sh=0
count_medium_severity_cvssv3_sh=0
count_critical_severity_cvssv3_sh=0
count_none_severity_cvssV3_sh=0

#Recorro los valores de SEVERIDAD BASE y aumento los contadores segun su valor

for j in range(0,len(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.baseSeverity"])):
    if(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.baseSeverity"][j]=='HIGH'):
        count_high_severity_cvssv3_sh+=1
    elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.baseSeverity"][j]=='LOW'):
        count_low_severity_cvssv3_sh+=1
    elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.baseSeverity"][j]=='MEDIUM'):
        count_medium_severity_cvssv3_sh+=1
    elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.baseSeverity"][j]=='CRITICAL'):
        count_critical_severity_cvssv3_sh+=1
    else:
        count_none_severity_cvssV3_sh+=1

print("**************************SEVERIDAD BASE EN CVE SEGÚN VECTOR CVSSV3 PARTE SMART HOME********************************")
print("\n")
print("LA SEVERIDAD BASE EN "+str(count_high_severity_cvssv3_sh)+" VULNERABILIDADES ES ALTA \n")
print("LA SEVERIDAD BASE EN "+str(count_low_severity_cvssv3_sh)+" VULNERABILIDADES ES BAJA \n")
print("LA SEVERIDAD BASE EN "+str(count_medium_severity_cvssv3_sh)+" VULNERABILIDADES ES MEDIA \n")
print("LA SEVERIDAD BASE EN "+str(count_critical_severity_cvssv3_sh)+" VULNERABILIDADES ES CRITICA \n")
print("EN "+str(count_none_severity_cvssV3_sh)+" VULNERABILIDADES NO HAY SEVERIDAD BASE  \n")
print("\n")
print("**************************PORCENTAJE SEVERIDAD BASE EN CVE SEGÚN VECTOR CVSSV3 PARTE SMART HOME********************************")
print("\n")
print("EL "+str(float(((count_high_severity_cvssv3_sh*100)/len(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.baseSeverity"]))))+"% DE LAS VULNERABILIDADES TIENE UNA SEVERIDAD BASE ALTA \n")
print("EL "+str(float(((count_low_severity_cvssv3_sh*100)/len(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.baseSeverity"]))))+"% DE LAS VULNERABILIDADES TIENE UNA SEVERIDAD BASE BAJA \n")
print("EL "+str(float(((count_medium_severity_cvssv3_sh*100)/len(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.baseSeverity"]))))+"% DE LAS VULNERABILIDADES TIENE UNA SEVERIDAD BASE MEDIA \n")
print("EL "+str(float(((count_critical_severity_cvssv3_sh*100)/len(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.baseSeverity"]))))+"% DE LAS VULNERABILIDADES TIENE UNA SEVERIDAD BASE CRITICA \n")
print("EL "+str(float(((count_none_severity_cvssV3_sh*100)/len(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.baseSeverity"]))))+"% DE LAS VULNERABILIDADES NO TIENE NIVEL DE SEVERIDAD BASE \n")
print("\n")


print("**************************ESTADÍSTICAS SEVERIDAD BASE EN CVE SEGÚN VECTOR CVSSV3 PARTE IOT Y SMART HOME CONJUNTAS********************************")
print("\n")
print("LA SEVERIDAD BASE EN "+str(count_high_severity_cvssv3_sh+count_high_severity_cvssv3_iot)+" VULNERABILIDADES ES ALTA \n")
print("LA SEVERIDAD BASE EN "+str(count_low_severity_cvssv3_sh+count_low_severity_cvssv3_iot)+" VULNERABILIDADES ES BAJA \n")
print("LA SEVERIDAD BASE EN "+str(count_medium_severity_cvssv3_sh+count_medium_severity_cvssv3_iot)+" VULNERABILIDADES ES MEDIA \n")
print("LA SEVERIDAD BASE EN "+str(count_critical_severity_cvssv3_sh+count_critical_severity_cvssv3_iot)+" VULNERABILIDADES ES CRITICA \n")
print("EN "+str(count_none_severity_cvssV3_sh+count_none_severity_cvssV3_iot)+" VULNERABILIDADES NO HAY SEVERIDAD BASE \n")
print("\n")
print("**************************PORCENTAJE SEVERIDAD BASE EN CVE SEGÚN VECTOR CVSSV3 PARTE IOT Y SMART HOME CONJUNTAS********************************")
print("EL "+str(float((((count_high_severity_cvssv3_sh+count_high_severity_cvssv3_iot)*100)/(len(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.baseSeverity"])+len(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.baseSeverity"])))))+"% DE LAS VULNERABILIDADES TIENE UNA SEVERIDAD BASE ALTA \n")
print("EL "+str(float((((count_low_severity_cvssv3_sh+count_low_severity_cvssv3_iot)*100)/(len(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.baseSeverity"])+len(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.baseSeverity"])))))+"% DE LAS VULNERABILIDADES TIENE UNA SEVERIDAD BASE BAJA \n")
print("EL "+str(float((((count_medium_severity_cvssv3_sh+count_medium_severity_cvssv3_iot)*100)/(len(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.baseSeverity"])+len(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.baseSeverity"])))))+"% DE LAS VULNERABILIDADES TIENE UNA SEVERIDAD BASE MEDIA \n")
print("EL "+str(float((((count_critical_severity_cvssv3_sh+count_critical_severity_cvssv3_iot)*100)/(len(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.baseSeverity"])+len(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.baseSeverity"])))))+"% DE LAS VULNERABILIDADES TIENE UNA SEVERIDAD BASE CRITICA \n")
print("EL "+str(float((((count_none_severity_cvssV3_sh+count_none_severity_cvssV3_iot)*100)/(len(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.baseSeverity"])+len(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.baseSeverity"])))))+"% DE LAS VULNERABILIDADES NO TIENE SEVERIDAD BASE  \n")
