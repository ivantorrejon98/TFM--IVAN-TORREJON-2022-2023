import pandas as pd

#Abro los ficheros con los que voy a tratar


df_cve_iot=pd.read_excel('cves_iot_2023.xlsx')
df_cve_sh=pd.read_excel('cves_smart_home_2023.xlsx')

#Variables donde almacenare el contador de niveles de impacto de INTEGRIDAD
count_high_int_cvssv3_iot=0
count_low_int_cvssv3_iot=0
count_none_int_cvssV3_iot=0

#Recorro los valores de impacto de INTEGRIDAD y aumento los contadores segun su valor

for j in range(0,len(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"])):
    if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"][j]=='HIGH'):
        count_high_int_cvssv3_iot+=1
    elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"][j]=='LOW'):
        count_low_int_cvssv3_iot+=1
    else:
        count_none_int_cvssV3_iot+=1

print("**************************ESTADISTICAS IMPACTO DE INTEGRIDAD EN CVE SEGUN VECTOR CVSSV3 PARTE IOT********************************")
print("\n")
print("EL IMPACTO DE INTEGRIDAD EN "+str(count_high_int_cvssv3_iot)+" VULNERABILIDADES ES ALTO \n")
print("EL IMPACTO DE INTEGRIDAD EN "+str(count_low_int_cvssv3_iot)+" VULNERABILIDADES ES BAJO \n")
print("EN "+str(count_none_int_cvssV3_iot)+" VULNERABILIDADES NO HAY IMPACTO DE INTEGRIDAD  \n")
print("\n")
print("**************************PORCENTAJE IMPACTO DE INTEGRIDAD EN CVE SEGUN VECTOR CVSSV3 PARTE IOT********************************")
print("\n")
print("EL "+str(float(((count_high_int_cvssv3_iot*100)/len(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"]))))+"% DE LAS VULNERABILIDADES TIENE UN ALTO IMPACTO DE INTEGRIDAD \n")
print("EL "+str(float(((count_low_int_cvssv3_iot*100)/len(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"]))))+"% DE LAS VULNERABILIDADES TIENE UN BAJO IMPACTO DE INTEGRIDAD \n")
print("EL "+str(float(((count_none_int_cvssV3_iot*100)/len(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"]))))+"% DE LAS VULNERABILIDADES NO TIENE IMPACTO DE INTEGRIDAD  \n")
print("\n")



#Variables donde almacenare el contador de niveles de impacto de INTEGRIDAD
count_high_int_cvssv3_sh=0
count_low_int_cvssv3_sh=0
count_none_int_cvssV3_sh=0

#Recorro los valores de impacto de INTEGRIDAD y aumento los contadores segun su valor

for r in range(0,len(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"])):
    if(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"][r]=='HIGH'):
        count_high_int_cvssv3_sh+=1
    elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"][r]=='LOW'):
        count_low_int_cvssv3_sh+=1
    else:
        count_none_int_cvssV3_sh+=1

print("**************************ESTADISTICAS IMPACTO DE INTEGRIDAD EN CVE SEGUN VECTOR CVSSV3 PARTE SMART HOME********************************")
print("\n")
print("EL IMPACTO DE INTEGRIDAD EN "+str(count_high_int_cvssv3_sh)+" VULNERABILIDADES ES ALTO \n")
print("EL IMPACTO DE INTEGRIDAD EN "+str(count_low_int_cvssv3_sh)+" VULNERABILIDADES ES BAJO \n")
print(" EN "+str(count_none_int_cvssV3_sh)+" VULNERABILIDADES NO HAY IMPACTO DE INTEGRIDAD \n")
print("\n")
print("**************************PORCENTAJE IMPACTO DE INTEGRIDAD EN CVE SEGUN VECTOR CVSSV3 PARTE SMART HOME********************************")
print("\n")
print("EL "+str(float(((count_high_int_cvssv3_sh*100)/len(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"]))))+"% DE LAS VULNERABILIDADES TIENE UN ALTO IMPACTO DE INTEGRIDAD \n")
print("EL "+str(float(((count_low_int_cvssv3_sh*100)/len(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"]))))+"% DE LAS VULNERABILIDADES TIENE UN BAJO IMPACTO DE INTEGRIDAD \n")
print("EL "+str(float(((count_none_int_cvssV3_sh*100)/len(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"]))))+"% DE LAS VULNERABILIDADES NO TIENE IMPACTO DE INTEGRIDAD  \n")
print("\n")



print("**************************ESTADISTICAS IMPACTO DE INTEGRIDAD EN CVE SEGUN VECTOR CVSSV3 PARTE IOT Y SMART HOME CONJUNTAS********************************")
print("\n")
print("EL IMPACTO DE INTEGRIDAD EN "+str(count_high_int_cvssv3_iot+count_high_int_cvssv3_sh)+" VULNERABILIDADES ES ALTO \n")
print("EL IMPACTO DE INTEGRIDAD EN "+str(count_low_int_cvssv3_iot+count_low_int_cvssv3_sh)+" VULNERABILIDADES ES BAJO \n")
print("EN "+str(count_none_int_cvssV3_iot+count_none_int_cvssV3_sh)+" VULNERABILIDADES NO HAY IMPACTO DE INTEGRIDAD \n")
print("\n")
print("**************************PORCENTAJE IMPACTO DE INTEGRIDAD EN CVE SEGUN VECTOR CVSSV3 PARTE IOT Y SMART HOME CONJUNTAS ********************************")
print("\n")
print("EL "+str(float((((count_high_int_cvssv3_iot+count_high_int_cvssv3_sh)*100)/(len(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"])+len(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"])))))+"% DE LAS VULNERABILIDADES TIENE UN IMPACTO DE INTEGRIDAD PARCIAL \n")
print("EL "+str(float((((count_low_int_cvssv3_iot+count_low_int_cvssv3_sh)*100)/(len(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"])+len(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"])))))+"% DE LAS VULNERABILIDADES TIENE UN IMPACTO DE INTEGRIDAD COMPLETO \n")
print("EL "+str(float((((count_none_int_cvssV3_iot+count_none_int_cvssV3_sh)*100)/(len(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"])+len(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"])))))+"% DE LAS VULNERABILIDADES NO TIENE IMPACTO DE INTEGRIDAD  \n")
print("\n")
print("\n")
print("\n")












