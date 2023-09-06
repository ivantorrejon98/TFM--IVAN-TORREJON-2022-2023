import pandas as pd

#Abro los ficheros con los que voy a tratar


df_cve_iot=pd.read_excel('cves_iot_2023.xlsx')
df_cve_sh=pd.read_excel('cves_smart_home_2023.xlsx')



#Variables donde almacenare el contador de niveles de COMPLEJIDAD DE ATAQUE
count_high_comacc_cvssv3_iot=0
count_low_comacc_cvssv3_iot=0
count_none_comacc_cvssV3_iot=0

#Recorro los valores de COMPLEJIDAD DE ATAQUE y aumento los contadores segun su valor

for j in range(0,len(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.attackComplexity"])):
    if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.attackComplexity"][j]=='HIGH'):
        count_high_comacc_cvssv3_iot+=1
    elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.attackComplexity"][j]=='LOW'):
        count_low_comacc_cvssv3_iot+=1
    else:
        count_none_comacc_cvssV3_iot+=1

print("**************************ESTADÍSTICAS COMPLEJIDAD DE ATAQUE EN CVE SEGÚN VECTOR CVSSV3 IOT********************************")
print("\n")
print("LA COMPLEJIDAD DE ATAQUE EN "+str(count_high_comacc_cvssv3_iot)+" VULNERABILIDADES ES ALTA \n")
print("LA COMPLEJIDAD DE ATAQUE EN "+str(count_low_comacc_cvssv3_iot)+" VULNERABILIDADES ES BAJA \n")
print("LA COMPLEJIDAD DE ATAQUE EN "+str(count_none_comacc_cvssV3_iot)+" VULNERABILIDADES NO VIENE ESPECIFICADA \n")
print("\n")
print("**************************PORCENTAJE COMPLEJIDAD DE ATAQUE EN CVE SEGÚN VECTOR CVSSV3 IOT********************************")
print("\n")
print("EL "+str(float(((count_high_comacc_cvssv3_iot*100)/len(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.attackComplexity"]))))+"% DE LAS VULNERABILIDADES TIENE UNA ALTA COMPLEJIDAD DE ATAQUE \n")
print("EL "+str(float(((count_low_comacc_cvssv3_iot*100)/len(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.attackComplexity"]))))+"% DE LAS VULNERABILIDADES TIENE UNA BAJA COMPLEJIDAD DE ATAQUE \n")
print("EL "+str(float(((count_none_comacc_cvssV3_iot*100)/len(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.attackComplexity"]))))+"% DE LAS VULNERABILIDADES NO TIENE COMPLEJIDAD DE ATAQUE ESPECIFICADA \n")
print("\n")


#Variables donde almacenare el contador de niveles de COMPLEJIDAD DE ACCESO
count_high_comacc_cvssv3_sh=0
count_low_comacc_cvssv3_sh=0
count_none_comacc_cvssV3_sh=0

#Recorro los valores de COMPLEJIDAD DE ATAQUE y aumento los contadores segun su valor

for r in range(0,len(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.attackComplexity"])):
    if(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.attackComplexity"][r]=='HIGH'):
        count_high_comacc_cvssv3_sh+=1
    elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.attackComplexity"][r]=='LOW'):
        count_low_comacc_cvssv3_sh+=1
    else:
        count_none_comacc_cvssV3_sh+=1

print("**************************ESTADÍSTICAS COMPLEJIDAD DE ATAQUE EN CVE SEGÚN VECTOR CVSSV3 SMART HOME********************************")
print("\n")
print("LA COMPLEJIDAD DE ATAQUE EN "+str(count_high_comacc_cvssv3_sh)+" VULNERABILIDADES ES ALTA \n")
print("LA COMPLEJIDAD DE ATAQUE EN "+str(count_low_comacc_cvssv3_sh)+" VULNERABILIDADES ES BAJA \n")
print("LA COMPLEJIDAD DE ATAQUE EN "+str(count_none_comacc_cvssV3_sh)+" VULNERABILIDADES NO VIENE ESPECIFICADA \n")
print("\n")
print("**************************PORCENTAJE COMPLEJIDAD DE ATAQUE EN CVE SEGÚN VECTOR CVSSV3 SMART HOME********************************")
print("\n")
print("EL "+str(float(((count_high_comacc_cvssv3_sh*100)/len(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.attackComplexity"]))))+"% DE LAS VULNERABILIDADES TIENE UNA ALTA COMPLEJIDAD DE ATAQUE \n")
print("EL "+str(float(((count_low_comacc_cvssv3_sh*100)/len(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.attackComplexity"]))))+"% DE LAS VULNERABILIDADES TIENE UNA BAJA COMPLEJIDAD DE ATAQUE \n")
print("EL "+str(float(((count_none_comacc_cvssV3_sh*100)/len(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.attackComplexity"]))))+"% DE LAS VULNERABILIDADES NO TIENE COMPLEJIDAD DE ATAQUE ESPECIFICADA \n")
print("\n")



print("**************************ESTADÍSTICAS COMPLEJIDAD DE ATAQUE EN CVE SEGÚN VECTOR CVSSV3 PARTE IOT Y SMART HOME CONJUNTAS********************************")
print("\n")
print("\n")
print("LA COMPLEJIDAD DE ATAQUE EN "+str(count_high_comacc_cvssv3_sh+count_high_comacc_cvssv3_iot)+" VULNERABILIDADES ES ALTA \n")
print("LA COMPLEJIDAD DE ATAQUE EN "+str(count_low_comacc_cvssv3_iot+count_low_comacc_cvssv3_sh)+" VULNERABILIDADES ES BAJA \n")
print("LA COMPLEJIDAD DE ATAQUE EN "+str(count_none_comacc_cvssV3_iot+count_none_comacc_cvssV3_sh)+" VULNERABILIDADES NO VIENE ESPECIFICADA \n")
print("\n")
print("\n")
print("***************************PORCENTAJE COMPLEJIDAD DE ATAQUE EN CVE SEGÚN VECTOR CVSSV3 PARTE IOT Y SMART HOME CONJUNTAS********************************")
print("\n")
print("EL "+str(float((((count_high_comacc_cvssv3_sh+count_high_comacc_cvssv3_iot)*100)/(len(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.attackComplexity"])+len(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.attackComplexity"])))))+"% DE LAS VULNERABILIDADES TIENE UNA ALTA COMPLEJIDAD DE ATAQUE \n")
print("EL "+str(float((((count_low_comacc_cvssv3_sh+count_low_comacc_cvssv3_iot)*100)/(len(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.attackComplexity"])+len(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.attackComplexity"])))))+"% DE LAS VULNERABILIDADES TIENE UNA BAJA COMPLEJIDAD DE ATAQUE \n")
print("EL "+str(float((((count_none_comacc_cvssV3_sh+count_none_comacc_cvssV3_iot)*100)/(len(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.attackComplexity"])+len(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.attackComplexity"])))))+"% DE LAS VULNERABILIDADES NO TIENE COMPLEJIDAD DE ATAQUE ESPECIFICADA \n")
print("\n")
print("\n")
print("\n")