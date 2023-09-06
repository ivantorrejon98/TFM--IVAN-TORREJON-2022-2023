import pandas as pd

#Abro los ficheros con los que voy a tratar


df_cve_iot=pd.read_excel('cves_iot_2023.xlsx')
df_cve_sh=pd.read_excel('cves_smart_home_2023.xlsx')


#Variables donde almacenare el contador de niveles de impacto de DISPONIBILIDAD
count_high_ava_cvssv3_iot=0
count_low_ava_cvssv3_iot=0
count_none_ava_cvssV3_iot=0

#Recorro los valores de impacto de DISPONIBILIDAD y aumento los contadores segun su valor

for j in range(0,len(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"])):
    if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"][j]=='HIGH'):
        count_high_ava_cvssv3_iot+=1
    elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"][j]=='LOW'):
        count_low_ava_cvssv3_iot+=1
    else:
        count_none_ava_cvssV3_iot+=1

print("**************************ESTADISTICAS IMPACTO DE DISPONIBILIDAD EN CVE SEGUN VECTOR CVSSV3 PARTE IOT********************************")
print("\n")
print("EL IMPACTO DE DISPONIBILIDAD EN "+str(count_high_ava_cvssv3_iot)+" VULNERABILIDADES ES ALTO \n")
print("EL IMPACTO DE DISPONIBILIDAD EN "+str(count_low_ava_cvssv3_iot)+" VULNERABILIDADES ES BAJO \n")
print("EN "+str(count_none_ava_cvssV3_iot)+" VULNERABILIDADES NO HAY IMPACTO DE DISPONIBILIDAD \n")
print("\n")
print("**************************PORCENTAJE IMPACTO DE DISPONIBILIDAD EN CVE SEGUN VECTOR CVSSV3 PARTE IOT********************************")
print("\n")
print("EL "+str(float(((count_high_ava_cvssv3_iot*100)/len(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"]))))+"% DE LAS VULNERABILIDADES TIENE UN ALTO IMPACTO DE DISPONIBILIDAD \n")
print("EL "+str(float(((count_low_ava_cvssv3_iot*100)/len(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"]))))+"% DE LAS VULNERABILIDADES TIENE UN BAJO IMPACTO DE DISPONIBILIDAD \n")
print("EL "+str(float(((count_none_ava_cvssV3_iot*100)/len(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"]))))+"% DE LAS VULNERABILIDADES NO TIENE IMPACTO DE DISPONIBILIDAD \n")
print("\n")

#Variables donde almacenare el contador de niveles de impacto de DISPONIBILIDAD
count_high_ava_cvssv3_sh=0
count_low_ava_cvssv3_sh=0
count_none_ava_cvssV3_sh=0

#Recorro los valores de impacto de DISPONIBILIDAD y aumento los contadores segun su valor

for r in range(0,len(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"])):
    if(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"][r]=='HIGH'):
        count_high_ava_cvssv3_sh+=1
    elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"][r]=='LOW'):
        count_low_ava_cvssv3_sh+=1
    else:
        count_none_ava_cvssV3_sh+=1

print("**************************ESTADÍSTICAS IMPACTO DE DISPONIBILIDAD EN CVE SEGUN VECTOR CVSSV3 PARTE SMART HOME********************************")
print("\n")
print("EL IMPACTO DE DISPONIBILIDAD EN "+str(count_high_ava_cvssv3_sh)+" VULNERABILIDADES ES ALTO \n")
print("EL IMPACTO DE DISPONIBILIDAD EN "+str(count_low_ava_cvssv3_sh)+" VULNERABILIDADES ES BAJO \n")
print(" EN "+str(count_none_ava_cvssV3_sh)+" VULNERABILIDADES NO HAY IMPACTO DE DISPONIBILIDAD \n")
print("\n")
print("**************************PORCENTAJE IMPACTO DE DISPONIBILIDAD EN CVE SEGUN VECTOR CVSSV3 PARTE SMART HOME********************************")
print("\n")
print("EL "+str(float(((count_high_ava_cvssv3_sh*100)/len(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"]))))+"% DE LAS VULNERABILIDADES TIENE UN ALTO IMPACTO DE DISPONIBILIDAD \n")
print("EL "+str(float(((count_low_ava_cvssv3_sh*100)/len(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"]))))+"% DE LAS VULNERABILIDADES TIENE UN BAJO IMPACTO DE DISPONIBILIDAD \n")
print("EL "+str(float(((count_none_ava_cvssV3_sh*100)/len(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"]))))+"% DE LAS VULNERABILIDADES NO TIENE IMPACTO DE DISPONIBILIDAD  \n")
print("\n")



print("**************************ESTADÍSTICAS IMPACTO DE DISPONIBILIDAD EN CVE SEGUN VECTOR CVSSV3 PARTE IOT Y SMART HOME CONJUNTAS********************************")
print("\n")
print("EL IMPACTO DE DISPONIBILIDAD EN "+str(count_high_ava_cvssv3_sh+count_high_ava_cvssv3_iot)+" VULNERABILIDADES ES ALTO \n")
print("EL IMPACTO DE DISPONIBILIDAD EN "+str(count_low_ava_cvssv3_sh+count_low_ava_cvssv3_iot)+" VULNERABILIDADES ES BAJO \n")
print("EN "+str(count_none_ava_cvssV3_sh+count_none_ava_cvssV3_iot)+" VULNERABILIDADES NO HAY IMPACTO DE DISPONIBILIDAD \n")
print("\n")
print("**************************PORCENTAJE IMPACTO DE DISPONIBILIDAD EN CVE SEGUN VECTOR CVSSV3 PARTE IOT Y SMART HOME CONJUNTAS********************************")
print("\n")
print("EL "+str(float((((count_high_ava_cvssv3_sh+count_high_ava_cvssv3_iot)*100)/(len(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"])+len(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"])))))+"% DE LAS VULNERABILIDADES TIENE UN ALTO IMPACTO DE DISPONIBILIDAD \n")
print("EL "+str(float((((count_low_ava_cvssv3_sh+count_low_ava_cvssv3_iot)*100)/(len(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"])+len(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"])))))+"% DE LAS VULNERABILIDADES TIENE UN BAJO IMPACTO DE DISPONIBILIDAD \n")
print("EL "+str(float((((count_none_ava_cvssV3_sh+count_none_ava_cvssV3_iot)*100)/(len(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"])+len(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"])))))+"% DE LAS VULNERABILIDADES NO TIENE IMPACTO DE DISPONIBILIDAD  \n")
print("\n")