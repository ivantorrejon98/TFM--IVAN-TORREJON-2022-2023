import pandas as pd

#Abro los ficheros con los que voy a tratar


df_cve_iot=pd.read_excel('cves_iot_2023.xlsx')
df_cve_sh=pd.read_excel('cves_smart_home_2023.xlsx')


#Variables donde almacenare el contador de niveles de impacto de confidencialidad
count_high_conf_cvssv3_iot=0
count_low_conf_cvssv3_iot=0
count_none_conf_cvssV3_iot=0

#Recorro los valores de impacto de confidencialidad y aumento los contadores segun su valor

for j in range(0,len(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.confidentialityImpact"])):
    if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.confidentialityImpact"][j]=='HIGH'):
        count_high_conf_cvssv3_iot+=1
    elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.confidentialityImpact"][j]=='LOW'):
        count_low_conf_cvssv3_iot+=1
    else:
        count_none_conf_cvssV3_iot+=1

print("**************************ESTADISTICAS IMPACTO DE CONFIDENCIALIDAD EN CVE SEGUN VECTOR CVSSV3 PARTE IOT********************************")
print("\n")
print("EL IMPACTO DE CONFIDENCIALIDAD EN "+str(count_high_conf_cvssv3_iot)+" VULNERABILIDADES ES ALTO \n")
print("EL IMPACTO DE CONFIDENCIALIDAD EN "+str(count_low_conf_cvssv3_iot)+" VULNERABILIDADES ES BAJO \n")
print("NO HAY NINGÚN IMPACTO DE CONFIDENCIALIDAD EN "+str(count_none_conf_cvssV3_iot)+" VULNERABILIDADES \n")
print("\n")
print("**************************PORCENTAJE IMPACTO DE CONFIDENCIALIDAD EN CVE SEGUN VECTOR CVSSV3 PARTE IOT********************************")
print("\n")
print("EL "+str(float(((count_high_conf_cvssv3_iot*100)/len(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.confidentialityImpact"]))))+"% DE LAS VULNERABILIDADES TIENE UN ALTO IMPACTO DE CONFIDENCIALIDAD \n")
print("EL "+str(float(((count_low_conf_cvssv3_iot*100)/len(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.confidentialityImpact"]))))+"% DE LAS VULNERABILIDADES TIENE UN BAJO IMPACTO DE CONFIDENCIALIDAD \n")
print("EL "+str(float(((count_none_conf_cvssV3_iot*100)/len(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.confidentialityImpact"]))))+"% DE LAS VULNERABILIDADES NO TIENE IMPACTO DE CONFIDENCIALIDAD \n")
print("\n")



#Variables donde almacenare el contador de niveles de impacto de confidencialidad
count_high_conf_cvssv3_sh=0
count_low_conf_cvssv3_sh=0
count_none_conf_cvssV3_sh=0

#Recorro los valores de impacto de confidencialidad y aumento los contadores segun su valor

for r in range(0,len(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.confidentialityImpact"])):
    if(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.confidentialityImpact"][r]=='HIGH'):
        count_high_conf_cvssv3_sh+=1
    elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.confidentialityImpact"][r]=='LOW'):
        count_low_conf_cvssv3_sh+=1
    else:
        count_none_conf_cvssV3_sh+=1

print("**************************ESTADISTICAS IMPACTO DE CONFIDENCIALIDAD EN CVE SEGUN VECTOR CVSSV3 PARTE SMART HOME********************************")
print("\n")
print("EL IMPACTO DE CONFIDENCIALIDAD EN "+str(count_high_conf_cvssv3_sh)+" VULNERABILIDADES ES ALTO \n")
print("EL IMPACTO DE CONFIDENCIALIDAD EN "+str(count_low_conf_cvssv3_sh)+" VULNERABILIDADES ES BAJO \n")
print("NO HAY NINGÚN IMPACTO DE CONFIDENCIALIDAD EN "+str(count_none_conf_cvssV3_sh)+" VULNERABILIDADES \n")
print("\n")
print("**************************PORCENTAJE IMPACTO DE CONFIDENCIALIDAD EN CVE SEGUN VECTOR CVSSV3 PARTE HOME********************************")
print("\n")
print("EL "+str(float(((count_high_conf_cvssv3_sh*100)/len(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.confidentialityImpact"]))))+"% DE LAS VULNERABILIDADES TIENE UN ALTO IMPACTO DE CONFIDENCIALIDAD \n")
print("EL "+str(float(((count_low_conf_cvssv3_sh*100)/len(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.confidentialityImpact"]))))+"% DE LAS VULNERABILIDADES TIENE UN BAJO IMPACTO DE CONFIDENCIALIDAD \n")
print("EL "+str(float(((count_none_conf_cvssV3_sh*100)/len(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.confidentialityImpact"]))))+"% DE LAS VULNERABILIDADES NO TIENE IMPACTO DE CONFIDENCIALIDAD \n")
print("\n")


print("**************************ESTADISTICAS IMPACTO DE CONFIDENCIALIDAD EN CVE SEGUN VECTOR CVSSV3 PARTE IOT Y SMART HOME CONJUNTAS********************************")
print("\n")
print("EL IMPACTO DE CONFIDENCIALIDAD EN "+str(count_high_conf_cvssv3_iot+count_high_conf_cvssv3_sh)+" VULNERABILIDADES ES ALTO \n")
print("EL IMPACTO DE CONFIDENCIALIDAD EN "+str(count_low_conf_cvssv3_iot+count_low_conf_cvssv3_sh)+" VULNERABILIDADES ES BAJO \n")
print("NO HAY NINGÚN IMPACTO DE CONFIDENCIALIDAD EN "+str(count_none_conf_cvssV3_iot+count_none_conf_cvssV3_sh)+" VULNERABILIDADES \n")
print("\n")
print("**************************PORCENTAJE IMPACTO DE CONFIDENCIALIDAD EN CVE SEGUN VECTOR CVSSV3 PARTE IOT Y SMART HOME CONJUNTAS ********************************")
print("\n")
print("EL "+str(float((((count_high_conf_cvssv3_iot+count_high_conf_cvssv3_sh)*100)/(len(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.confidentialityImpact"])+len(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.confidentialityImpact"])))))+"% DE LAS VULNERABILIDADES TIENE UN IMPACTO DE CONFIDENCIALIDAD PARCIAL \n")
print("EL "+str(float((((count_low_conf_cvssv3_iot+count_low_conf_cvssv3_sh)*100)/(len(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.confidentialityImpact"])+len(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.confidentialityImpact"])))))+"% DE LAS VULNERABILIDADES TIENE UN IMPACTO DE CONFIDENCIALIDAD COMPLETO \n")
print("EL "+str(float((((count_none_conf_cvssV3_iot+count_none_conf_cvssV3_sh)*100)/(len(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.confidentialityImpact"])+len(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.confidentialityImpact"])))))+"% DE LAS VULNERABILIDADES NO TIENE IMPACTO DE CONFIDENCIALIDAD \n")
print("\n")
print("\n")
print("\n")

