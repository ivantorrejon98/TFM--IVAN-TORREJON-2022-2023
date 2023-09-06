#Variables donde almacenare el contador de niveles de COMPLEJIDAD DE ACCESO
count_high_comacc_cvssv2_iot=0
count_low_comacc_cvssv2_iot=0
count_medium_comacc_cvssv2_iot=0
count_none_comacc_cvssV2_iot=0

#Recorro los valores de ACCESO y aumento los contadores segun su valor

for k in range(0,len(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.accessComplexity"])):
    if(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.accessComplexity"][k]=='HIGH'):
        count_high_comacc_cvssv2_iot+=1
    elif(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.accessComplexity"][k]=='LOW'):
        count_low_comacc_cvssv2_iot+=1
    elif(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.accessComplexity"][k]=='MEDIUM'):
        count_medium_comacc_cvssv2_iot+=1
    else:
        count_none_comacc_cvssV2_iot+=1

print("**************************ESTADÍSTICAS COMPLEJIDAD DE ACCESO EN CVE SEGÚN VECTOR DE ACCESO CVSSV2 IOT********************************")
print("\n")
print("LA COMPLEJIDAD DE ACCESO EN "+str(count_high_comacc_cvssv2_iot)+" VULNERABILIDADES ES ALTA \n")
print("LA COMPLEJIDAD DE ACCESO EN "+str(count_low_comacc_cvssv2_iot)+" VULNERABILIDADES ES BAJA \n")
print("LA COMPLEJIDAD DE ACCESO EN "+str(count_medium_comacc_cvssv2_iot)+" VULNERABILIDADES ES MEDIA \n")
print("LA COMPLEJIDAD DE ACCESO EN "+str(count_none_comacc_cvssV2_iot)+" VULNERABILIDADES NO VIENE ESPECIFICADA \n")
print("\n")
print("**************************PORCENTAJE COMPLEJIDAD DE ACCESO EN CVE SEGÚN VECTOR CVSSV2 IOT********************************")
print("\n")
print("EL "+str(float(((count_high_comacc_cvssv2_iot*100)/len(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.accessComplexity"]))))+"% DE LAS VULNERABILIDADES TIENE UNA ALTA COMPLEJIDAD DE ACCESO \n")
print("EL "+str(float(((count_low_comacc_cvssv2_iot*100)/len(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.accessComplexity"]))))+"% DE LAS VULNERABILIDADES TIENE UNA BAJA COMPLEJIDAD DE ACCESO \n")
print("EL "+str(float(((count_medium_comacc_cvssv2_iot*100)/len(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.accessComplexity"]))))+"% DE LAS VULNERABILIDADES TIENE UNA COMPLEJIDAD DE ACCESO MEDIA \n")
print("EL "+str(float(((count_none_comacc_cvssV2_iot*100)/len(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.accessComplexity"]))))+"% DE LAS VULNERABILIDADES NO TIENE COMPLEJIDAD DE ACCESO ESPECIFICADA \n")
print("\n")


#Variables donde almacenare el contador de niveles de COMPLEJIDAD DE ACCESO
count_high_comacc_cvssv2_sh=0
count_low_comacc_cvssv2_sh=0
count_medium_comacc_cvssv2_sh=0
count_none_comacc_cvssV2_sh=0

#Recorro los valores de ACCESO y aumento los contadores segun su valor

for l in range(0,len(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.accessComplexity"])):
    if(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.accessComplexity"][l]=='HIGH'):
        count_high_comacc_cvssv2_sh+=1
    elif(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.accessComplexity"][l]=='LOW'):
        count_low_comacc_cvssv2_sh+=1
    elif(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.accessComplexity"][l]=='MEDIUM'):
        count_medium_comacc_cvssv2_sh+=1
    else:
        count_none_comacc_cvssV2_sh+=1

print("**************************ESTADÍSTICAS COMPLEJIDAD DE ACCESO EN CVE SEGÚN VECTOR CVSSV2 SMART HOME********************************")
print("\n")
print("LA COMPLEJIDAD DE ACCESO EN "+str(count_high_comacc_cvssv2_sh)+" VULNERABILIDADES ES ALTA \n")
print("LA COMPLEJIDAD DE ACCESO EN "+str(count_low_comacc_cvssv2_sh)+" VULNERABILIDADES ES BAJA \n")
print("LA COMPLEJIDAD DE ACCESO EN "+str(count_medium_comacc_cvssv2_sh)+" VULNERABILIDADES ES MEDIA \n")
print("LA COMPLEJIDAD DE ACCESO EN "+str(count_none_comacc_cvssV2_sh)+" VULNERABILIDADES NO VIENE ESPECIFICADA \n")
print("\n")
print("**************************PORCENTAJE COMPLEJIDAD DE ACCESO EN CVE SEGÚN VECTOR CVSSV2 SMART HOME********************************")
print("\n")
print("EL "+str(float(((count_high_comacc_cvssv2_sh*100)/len(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.accessComplexity"]))))+"% DE LAS VULNERABILIDADES TIENE UNA ALTA COMPLEJIDAD DE ACCESO \n")
print("EL "+str(float(((count_low_comacc_cvssv2_sh*100)/len(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.accessComplexity"]))))+"% DE LAS VULNERABILIDADES TIENE UNA BAJA COMPLEJIDAD DE ACCESO \n")
print("EL "+str(float(((count_medium_comacc_cvssv2_sh*100)/len(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.accessComplexity"]))))+"% DE LAS VULNERABILIDADES TIENE UNA COMPLEJIDAD DE ACCESO MEDIA \n")
print("EL "+str(float(((count_none_comacc_cvssV2_sh*100)/len(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.accessComplexity"]))))+"% DE LAS VULNERABILIDADES NO TIENE COMPLEJIDAD DE ACCESO ESPECIFICADA \n")
print("\n")
print("\n")
print("\n")


print("**************************ESTADÍSTICAS COMPLEJIDAD DE ACCESO EN CVE SEGÚN VECTOR CVSSV2 PARTE IOT Y SMART HOME CONJUNTAS********************************")
print("\n")
print("\n")
print("LA COMPLEJIDAD DE ACCESO EN "+str(count_high_comacc_cvssv2_sh+count_high_comacc_cvssv2_iot)+" VULNERABILIDADES ES ALTA \n")
print("LA COMPLEJIDAD DE ACCESO EN "+str(count_low_comacc_cvssv2_iot+count_low_comacc_cvssv2_sh)+" VULNERABILIDADES ES BAJA \n")
print("LA COMPLEJIDAD DE ACCESO EN "+str(count_medium_comacc_cvssv2_iot+count_medium_comacc_cvssv2_sh)+" VULNERABILIDADES ES MEDIA \n")
print("LA COMPLEJIDAD DE ACCESO EN "+str(count_none_comacc_cvssV2_iot+count_none_comacc_cvssV2_sh)+" VULNERABILIDADES NO VIENE ESPECIFICADA \n")
print("\n")
print("\n")
print("***************************PORCENTAJE COMPLEJIDAD DE ACCESO EN CVE SEGÚN VECTOR CVSSV2 PARTE IOT Y SMART HOME CONJUNTAS********************************")
print("\n")
print("\n")
print("EL "+str(float((((count_high_comacc_cvssv2_sh+count_high_comacc_cvssv2_iot)*100)/(len(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.accessComplexity"])+len(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.accessComplexity"])))))+"% DE LAS VULNERABILIDADES TIENE UNA ALTA COMPLEJIDAD DE ACCESO \n")
print("EL "+str(float((((count_low_comacc_cvssv2_sh+count_low_comacc_cvssv2_iot)*100)/(len(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.accessComplexity"])+len(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.accessComplexity"])))))+"% DE LAS VULNERABILIDADES TIENE UNA BAJA COMPLEJIDAD DE ACCESO \n")
print("EL "+str(float((((count_medium_comacc_cvssv2_sh+count_medium_comacc_cvssv2_iot)*100)/(len(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.accessComplexity"])+len(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.accessComplexity"])))))+"% DE LAS VULNERABILIDADES TIENE UNA COMPLEJIDAD DE ACCESO MEDIA \n")
print("EL "+str(float((((count_none_comacc_cvssV2_sh+count_none_comacc_cvssV2_iot)*100)/(len(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.accessComplexity"])+len(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.accessComplexity"])))))+"% DE LAS VULNERABILIDADES NO TIENE COMPLEJIDAD DE ACCESO ESPECIFICADA \n")
print("\n")
