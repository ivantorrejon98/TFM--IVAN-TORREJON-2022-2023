import pandas as pd

#Abro los ficheros con los que voy a tratar


df_cve_iot=pd.read_excel('cves_iot_2023.xlsx')
df_cve_sh=pd.read_excel('cves_smart_home_2023.xlsx')


#Variables donde almacenare el contador de niveles de impacto de DISPONIBILIDAD
count_partial_ava_cvssv2_iot=0
count_complete_ava_cvssv2_iot=0
count_none_ava_cvssV2_iot=0

#Recorro los valores de impacto de DISPONIBILIDAD y aumento los contadores segun su valor

for k in range(0,len(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.availabilityImpact"])):
    if(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.availabilityImpact"][k]=='PARTIAL'):
        count_partial_ava_cvssv2_iot+=1
    elif(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.availabilityImpact"][k]=='COMPLETE'):
        count_complete_ava_cvssv2_iot+=1
    else:
        count_none_ava_cvssV2_iot+=1
        

print("**************************ESTADÍSTICAS IMPACTO DE DISPONIBILIDAD EN CVE SEGÚN VECTOR CVSSV2 PARTE IOT********************************")
print("\n")
print("EL IMPACTO DE DISPONIBILIDAD EN "+str(count_partial_ava_cvssv2_iot)+" VULNERABILIDADES ES PARCIAL \n")
print("EL IMPACTO DE DISPONIBILIDAD EN "+str(count_complete_ava_cvssv2_iot)+" VULNERABILIDADES ES COMPLETO \n")
print("EN "+str(count_none_ava_cvssV2_iot)+" VULNERABILIDADES NO HAY IMPACTO DE DISPONIBILIDAD \n")
print("\n")
print("**************************PORCENTAJE IMPACTO DE DISPONIBILIDAD EN CVE SEGÚN VECTOR CVSSV2 PARTE IOT********************************")
print("\n")
print("EL "+str(float(((count_partial_ava_cvssv2_iot*100)/len(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.availabilityImpact"]))))+"% DE LAS VULNERABILIDADES TIENE UN IMPACTO DE DISPONIBILIDAD PARCIAL \n")
print("EL "+str(float(((count_complete_ava_cvssv2_iot*100)/len(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.availabilityImpact"]))))+"% DE LAS VULNERABILIDADES TIENE UN IMPACTO DE DISPONIBILIDAD COMPLETO \n")
print("EL "+str(float(((count_none_ava_cvssV2_iot*100)/len(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.availabilityImpact"]))))+"% DE LAS VULNERABILIDADES NO TIENE IMPACTO DE DISPONIBILIDAD \n")



#Variables donde almacenare el contador de niveles de impacto de DISPONIBILIDAD
count_partial_ava_cvssv2_sh=0
count_complete_ava_cvssv2_sh=0
count_none_ava_cvssV2_sh=0

#Recorro los valores de impacto de DISPONIBILIDAD y aumento los contadores segun su valor

for l in range(0,len(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.availabilityImpact"])):
    if(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.availabilityImpact"][l]=='PARTIAL'):
        count_partial_ava_cvssv2_sh+=1
    elif(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.availabilityImpact"][l]=='COMPLETE'):
        count_complete_ava_cvssv2_sh+=1
    else:
        count_none_ava_cvssV2_sh+=1
        
print("**************************IMPACTO DE DISPONIBILIDAD EN CVE CVSSV2 SMART HOME********************************")
print("\n")
print("EL IMPACTO DE DISPONIBILIDAD EN "+str(count_partial_ava_cvssv2_sh)+" VULNERABILIDADES ES PARCIAL \n")
print("EL IMPACTO DE DISPONIBILIDAD EN "+str(count_complete_ava_cvssv2_sh)+" VULNERABILIDADES ES COMPLETO \n")
print("EN "+str(count_none_ava_cvssV2_sh)+" VULNERABILIDADES NO HAY IMPACTO DE DISPONIBILIDAD \n")
print("\n")
print("**************************PORCENTAJE IMPACTO DE DISPONIBILIDAD EN CVE CVSSV2 SMART HOME********************************")
print("\n")
print("EL "+str(float(((count_partial_ava_cvssv2_sh*100)/len(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.availabilityImpact"]))))+"% DE LAS VULNERABILIDADES TIENE UN IMPACTO DE DISPONIBILIDAD PARCIAL \n")
print("EL "+str(float(((count_complete_ava_cvssv2_sh*100)/len(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.availabilityImpact"]))))+"% DE LAS VULNERABILIDADES TIENE UN IMPACTO DE DISPONIBILIDAD COMPLETO \n")
print("EL "+str(float(((count_none_ava_cvssV2_sh*100)/len(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.availabilityImpact"]))))+"% DE LAS VULNERABILIDADES NO TIENE IMPACTO DE DISPONIBILIDAD \n")
print("\n")



print("**************************ESTADÍSTICAS IMPACTO DE DISPONIBILIDAD EN CVE SEGÚN VECTOR CVSSV2 PARTE IOT Y SMART HOME CONJUNTAS********************************")
print("\n")
print("EL IMPACTO DE DISPONIBILIDAD EN "+str(count_partial_ava_cvssv2_sh+count_partial_ava_cvssv2_iot)+" VULNERABILIDADES ES PARCIAL \n")
print("EL IMPACTO DE DISPONIBILIDAD EN "+str(count_complete_ava_cvssv2_sh+count_complete_ava_cvssv2_iot)+" VULNERABILIDADES ES COMPLETO \n")
print("EN "+str(count_none_ava_cvssV2_sh+count_none_ava_cvssV2_iot)+" VULNERABILIDADES NO HAY IMPACTO DE DISPONIBILIDAD \n")
print("\n")
print("**************************PORCENTAJE IMPACTO DE DISPONIBILIDAD EN CVE SEGÚN VECTOR CVSSV2 PARTE IOT Y SMART HOME CONJUNTAS********************************")
print("\n")
print("EL "+str(float((((count_partial_ava_cvssv2_sh+count_partial_ava_cvssv2_iot)*100)/(len(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.availabilityImpact"])+len(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.availabilityImpact"])))))+"% DE LAS VULNERABILIDADES TIENE UN IMPACTO DE DISPONIBILIDAD PARCIAL \n")
print("EL "+str(float((((count_complete_ava_cvssv2_sh+count_complete_ava_cvssv2_iot)*100)/(len(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.availabilityImpact"])+len(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.availabilityImpact"])))))+"% DE LAS VULNERABILIDADES TIENE UN IMPACTO DE DISPONIBILIDAD COMPLETO \n")
print("EL "+str(float((((count_none_ava_cvssV2_sh+count_none_ava_cvssV2_iot)*100)/(len(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.availabilityImpact"])+len(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.availabilityImpact"])))))+"% DE LAS VULNERABILIDADES NO TIENE IMPACTO DE DISPONIBILIDAD \n")
print("\n")

