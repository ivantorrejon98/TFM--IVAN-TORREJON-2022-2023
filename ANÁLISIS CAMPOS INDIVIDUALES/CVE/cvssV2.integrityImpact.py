import pandas as pd

#Abro los ficheros con los que voy a tratar


df_cve_iot=pd.read_excel('cves_iot_2023.xlsx')
df_cve_sh=pd.read_excel('cves_smart_home_2023.xlsx')


#Variables donde almacenare el contador de niveles de impacto de INTEGRIDAD
count_partial_int_cvssv2_iot=0
count_complete_int_cvssv2_iot=0
count_none_int_cvssV2_iot=0

#Recorro los valores de impacto de INTEGRIDAD y aumento los contadores segun su valor

for k in range(0,len(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.integrityImpact"])):
    if(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.integrityImpact"][k]=='PARTIAL'):
        count_partial_int_cvssv2_iot+=1
    elif(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.integrityImpact"][k]=='COMPLETE'):
        count_complete_int_cvssv2_iot+=1
    else:
        count_none_int_cvssV2_iot+=1
        

print("**************************IMPACTO DE INTEGRIDAD EN CVE SEGÚN VECTOR CVSSV2 PARTE IOT********************************")
print("\n")
print("EL IMPACTO DE INTEGRIDAD EN "+str(count_partial_int_cvssv2_iot)+" VULNERABILIDADES ES PARCIAL \n")
print("EL IMPACTO DE INTEGRIDAD EN "+str(count_complete_int_cvssv2_iot)+" VULNERABILIDADES ES COMPLETO \n")
print("EN "+str(count_none_int_cvssV2_iot)+" VULNERABILIDADES  NO HAY IMPACTO DE INTEGRIDAD \n")
print("\n")
print("**************************PORCENTAJE IMPACTO DE INTEGRIDAD EN CVE SEGÚN VECTOR CVSSV2 PARTE IOT********************************")
print("\n")
print("EL "+str(float(((count_partial_int_cvssv2_iot*100)/len(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.integrityImpact"]))))+"% DE LAS VULNERABILIDADES TIENE UN IMPACTO DE INTEGRIDAD PARCIAL \n")
print("EL "+str(float(((count_complete_int_cvssv2_iot*100)/len(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.integrityImpact"]))))+"% DE LAS VULNERABILIDADES TIENE UN IMPACTO DE INTEGRIDAD COMPLETO \n")
print("EL "+str(float(((count_none_int_cvssV2_iot*100)/len(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.integrityImpact"]))))+"% DE LAS VULNERABILIDADES NO TIENE IMPACTO DE INTEGRIDAD \n")



#Variables donde almacenare el contador de niveles de impacto de INTEGRIDAD
count_partial_int_cvssv2_sh=0
count_complete_int_cvssv2_sh=0
count_none_int_cvssV2_sh=0

#Recorro los valores de impacto de INTEGRIDAD y aumento los contadores segun su valor

for l in range(0,len(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.integrityImpact"])):
    if(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.integrityImpact"][l]=='PARTIAL'):
        count_partial_int_cvssv2_sh+=1
    elif(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.integrityImpact"][l]=='COMPLETE'):
        count_complete_int_cvssv2_sh+=1
    else:
        count_none_int_cvssV2_sh+=1
        

print("**************************IMPACTO DE INTEGRIDAD EN CVE SEGÚN VECTOR CVSSV2 PARTE SMART HOME********************************")
print("\n")
print("EL IMPACTO DE INTEGRIDAD EN "+str(count_partial_int_cvssv2_sh)+" VULNERABILIDADES ES PARCIAL \n")
print("EL IMPACTO DE INTEGRIDAD EN "+str(count_complete_int_cvssv2_sh)+" VULNERABILIDADES ES COMPLETO \n")
print("EN "+str(count_none_int_cvssV2_sh)+" VULNERABILIDADES NO HAY IMPACTO DE INTEGRIDAD \n")
print("\n")
print("**************************PORCENTAJE IMPACTO DE INTEGRIDAD EN CVE SEGÚN VECTOR CVSSV2 PARTE SMART HOME********************************")
print("\n")
print("EL "+str(float(((count_partial_int_cvssv2_sh*100)/len(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.integrityImpact"]))))+"% DE LAS VULNERABILIDADES TIENE UN IMPACTO DE INTEGRIDAD PARCIAL \n")
print("EL "+str(float(((count_complete_int_cvssv2_sh*100)/len(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.integrityImpact"]))))+"% DE LAS VULNERABILIDADES TIENE UN IMPACTO DE INTEGRIDAD COMPLETO \n")
print("EL "+str(float(((count_none_int_cvssV2_sh*100)/len(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.integrityImpact"]))))+"% DE LAS VULNERABILIDADES NO TIENE IMPACTO DE INTEGRIDAD \n")
print("\n")










print("**************************IMPACTO DE INTEGRIDAD EN CVE SEGÚN VECTOR CVSSV2 PARTE IOT Y SMART HOME CONJUNTAS********************************")
print("\n")
print("\n")
print("EL IMPACTO DE INTEGRIDAD EN "+str(count_partial_int_cvssv2_iot+count_partial_int_cvssv2_sh)+" VULNERABILIDADES ES PARCIAL \n")
print("EL IMPACTO DE INTEGRIDAD EN "+str(count_complete_int_cvssv2_iot+count_complete_int_cvssv2_sh)+" VULNERABILIDADES ES COMPLETO \n")
print("EN "+str(count_none_int_cvssV2_iot+count_none_int_cvssV2_sh)+" VULNERABILIDADES  NO HAY IMPACTO DE INTEGRIDAD \n")
print("\n")
print("\n")
print("**************************PORCENTAJE IMPACTO DE INTEGRIDAD EN CVE SEGÚN VECTOR CVSSV2 PARTE IOT Y SMART HOME CONJUNTAS********************************")
print("\n")
print("\n")
print("EL "+str(float((((count_partial_int_cvssv2_iot+count_partial_int_cvssv2_sh)*100)/(len(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"])+len(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"])))))+"% DE LAS VULNERABILIDADES TIENE UN IMPACTO DE INTEGRIDAD PARCIAL \n")
print("EL "+str(float((((count_complete_int_cvssv2_iot+count_complete_int_cvssv2_sh)*100)/(len(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"])+len(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"])))))+"% DE LAS VULNERABILIDADES TIENE UN IMPACTO DE INTEGRIDAD COMPLETO \n")
print("EL "+str(float((((count_none_int_cvssV2_iot+count_none_int_cvssV2_sh)*100)/(len(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"])+len(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"])))))+"% DE LAS VULNERABILIDADES NO TIENE IMPACTO DE INTEGRIDAD \n")
print("\n")










