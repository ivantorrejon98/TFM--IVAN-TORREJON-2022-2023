import pandas as pd

#Abro los ficheros con los que voy a tratar


df_cve_iot=pd.read_excel('cves_iot_2023.xlsx')
df_cve_sh=pd.read_excel('cves_smart_home_2023.xlsx')


#Variables donde almacenare el contador de niveles de impacto de confidencialidad
count_partial_conf_cvssv2_iot=0
count_complete_conf_cvssv2_iot=0
count_none_conf_cvssV2_iot=0

#Recorro los valores de impacto de confidencialidad y aumento los contadores segun su valor

for k in range(0,len(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.confidentialityImpact"])):
    if(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.confidentialityImpact"][k]=='PARTIAL'):
        count_partial_conf_cvssv2_iot+=1
    elif(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.confidentialityImpact"][k]=='COMPLETE'):
        count_complete_conf_cvssv2_iot+=1
    else:
        count_none_conf_cvssV2_iot+=1
        

print("**************************ESTADÍSTICAS IMPACTO DE CONFIDENCIALIDAD EN CVE SEGÚN VECTOR CVSSV2 PARTE IOT********************************")
print("\n")
print("EL IMPACTO DE CONFIDENCIALIDAD EN "+str(count_partial_conf_cvssv2_iot)+" VULNERABILIDADES ES PARCIAL \n")
print("EL IMPACTO DE CONFIDENCIALIDAD EN "+str(count_complete_conf_cvssv2_iot)+" VULNERABILIDADES ES COMPLETO \n")
print(" EN "+str(count_none_conf_cvssV2_iot)+" VULNERABILIDADES NO EXISTE IMPACTO DE CONFIDENCIALIDAD \n")
print("\n")
print("**************************PORCENTAJE IMPACTO DE CONFIDENCIALIDAD EN CVE SEGÚN VECTOR CVSSV2 PARTE IOT********************************")
print("\n")
print("EL "+str(float(((count_partial_conf_cvssv2_iot*100)/len(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.confidentialityImpact"]))))+"% DE LAS VULNERABILIDADES TIENE UN IMPACTO DE CONFIDENCIALIDAD PARCIAL \n")
print("EL "+str(float(((count_complete_conf_cvssv2_iot*100)/len(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.confidentialityImpact"]))))+"% DE LAS VULNERABILIDADES TIENE UN IMPACTO DE CONFIDENCIALIDAD COMPLETO \n")
print("EL "+str(float(((count_none_conf_cvssV2_iot*100)/len(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.confidentialityImpact"]))))+"% DE LAS VULNERABILIDADES NO TIENE IMPACTO DE CONFIDENCIALIDAD  \n")



#Variables donde almacenare el contador de niveles de impacto de confidencialidad
count_partial_conf_cvssv2_sh=0
count_complete_conf_cvssv2_sh=0
count_none_conf_cvssV2_sh=0

#Recorro los valores de impacto de confidencialidad y aumento los contadores segun su valor

for l in range(0,len(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.confidentialityImpact"])):
    if(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.confidentialityImpact"][l]=='PARTIAL'):
        count_partial_conf_cvssv2_sh+=1
    elif(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.confidentialityImpact"][l]=='COMPLETE'):
        count_complete_conf_cvssv2_sh+=1
    else:
        count_none_conf_cvssV2_sh+=1
        

print("**************************ESTADÍSTICAS IMPACTO DE CONFIDENCIALIDAD EN CVE SEGÚN VECTOR CVSSV2 PARTE SMART HOME********************************")
print("\n")
print("EL IMPACTO DE CONFIDENCIALIDAD EN "+str(count_partial_conf_cvssv2_sh)+" VULNERABILIDADES ES PARCIAL \n")
print("EL IMPACTO DE CONFIDENCIALIDAD EN "+str(count_complete_conf_cvssv2_sh)+" VULNERABILIDADES ES COMPLETO \n")
print("EN "+str(count_none_conf_cvssV2_sh)+" VULNERABILIDADES NO HAY IMPACTO DE CONFIDENCIALIDAD \n")
print("\n")
print("**************************PORCENTAJE IMPACTO DE CONFIDENCIALIDAD EN CVE SEGÚN VECTOR CVSSV2 PARTE SMART HOME********************************")
print("\n")
print("EL "+str(float(((count_partial_conf_cvssv2_sh*100)/len(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.confidentialityImpact"]))))+"% DE LAS VULNERABILIDADES TIENE UN IMPACTO DE CONFIDENCIALIDAD PARCIAL \n")
print("EL "+str(float(((count_complete_conf_cvssv2_sh*100)/len(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.confidentialityImpact"]))))+"% DE LAS VULNERABILIDADES TIENE UN IMPACTO DE CONFIDENCIALIDAD COMPLETO \n")
print("EL "+str(float(((count_none_conf_cvssV2_sh*100)/len(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.confidentialityImpact"]))))+"% DE LAS VULNERABILIDADES NO TIENE IMPACTO DE CONFIDENCIALIDAD \n")
print("\n")



print("**************************ESTADÍSTICAS IMPACTO DE CONFIDENCIALIDAD EN CVE SEGÚN VECTOR CVSSV2 PARTE IOT Y SMART HOME CONJUNTAS********************************")
print("\n")
print("\n")
print("EL IMPACTO DE CONFIDENCIALIDAD EN "+str(count_partial_conf_cvssv2_iot+count_partial_conf_cvssv2_sh)+" VULNERABILIDADES ES PARCIAL \n")
print("EL IMPACTO DE CONFIDENCIALIDAD EN "+str(count_complete_conf_cvssv2_iot+count_complete_conf_cvssv2_sh)+" VULNERABILIDADES ES COMPLETO \n")
print("EN "+str(count_none_conf_cvssV2_iot+count_none_conf_cvssV2_sh)+" VULNERABILIDADES NO HAY IMPACTO DE CONFIDENCIALIDAD \n")
print("\n")
print("\n")
print("**************************PORCENTAJE IMPACTO DE CONFIDENCIALIDAD EN CVE SEGÚN VECTOR CVSSV2 PARTE IOT Y SMART HOME CONJUNTAS********************************")
print("\n")
print("\n")
print("EL "+str(float((((count_partial_conf_cvssv2_iot+count_partial_conf_cvssv2_sh)*100)/(len(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.confidentialityImpact"])+len(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.confidentialityImpact"])))))+"% DE LAS VULNERABILIDADES TIENE UN IMPACTO DE CONFIDENCIALIDAD PARCIAL \n")
print("EL "+str(float((((count_complete_conf_cvssv2_iot+count_complete_conf_cvssv2_sh)*100)/(len(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.confidentialityImpact"])+len(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.confidentialityImpact"])))))+"% DE LAS VULNERABILIDADES TIENE UN IMPACTO DE CONFIDENCIALIDAD COMPLETO \n")
print("EL "+str(float((((count_none_conf_cvssV2_iot+count_none_conf_cvssV2_sh)*100)/(len(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.confidentialityImpact"])+len(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.confidentialityImpact"])))))+"% DE LAS VULNERABILIDADES NO TIENE IMPACTO DE CONFIDENCIALIDAD  \n")
print("\n")


