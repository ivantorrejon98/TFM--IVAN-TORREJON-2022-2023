import pandas as pd


df_cve_iot=pd.read_excel('cves_iot_2023.xlsx')
df_cve_sh=pd.read_excel('cves_smart_home_2023.xlsx')

#Recorro los valores de SCOPE y aumento los contadores segun su valor
cve_scope_changed__cvssv3_iot=0
cve_scope_unchanged__cvssv3_iot=0
cve_no_scope_cvssv3_iot=0


#Recorro los valores de SCOPE y aumento los contadores segun su valor
for j in range(0,len(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.scope"])):
    if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.scope"][j] =='CHANGED'):
        cve_scope_changed__cvssv3_iot+=1
    elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.scope"][j] =='UNCHANGED'):
        cve_scope_unchanged__cvssv3_iot+=1
    else:
        cve_no_scope_cvssv3_iot+=1
    
print("**************************ESTADÍSTICAS ALCANCE CVE SEGÚN VECTOR CVSSV3 PARTE IOT********************************")
print("\n")
print("EN "+str(cve_scope_changed__cvssv3_iot)+" VULNERABILIDADES EL ALCANCE ES MODIFICADO \n")
print("EN "+str(cve_scope_unchanged__cvssv3_iot)+" VULNERABILIDADES EL ALCANCE ES NO MODIFICADO \n")
print("EN "+str(cve_no_scope_cvssv3_iot)+" VULNERABILIDADES EL ALCANCE NO ESTÁ ESPECIFICADO")
print("\n")
print("**************************PORCENTAJE ALCANCE CVE SEGÚN VECTOR CVSSV3 PARTE IOT********************************")
print("\n")

print("EN EL "+str(float(((cve_scope_changed__cvssv3_iot*100)/len(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.scope"]))))+"% DE LAS VULNERABILIDADES EL ALCANCE ES MODIFICADO \n")
print("EN EL "+str(float(((cve_scope_unchanged__cvssv3_iot*100)/len(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.scope"]))))+"% DE LAS VULNERABILIDADES EL ALCANCE ES NO MODIFICADO \n")
print("EN EL "+str(float(((cve_no_scope_cvssv3_iot*100)/len(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.scope"]))))+"% DE LAS VULNERABILIDADES NO HAY ALCANCE ESPECIFICADO \n")
print("\n")



#Recorro los valores de SCOPE y aumento los contadores segun su valor
cve_scope_changed__cvssv3_sh=0
cve_scope_unchanged__cvssv3_sh=0
cve_no_scope_cvssv3_sh=0


#Recorro los valores de SCOPE y aumento los contadores segun su valor
for r in range(0,len(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.scope"])):
    if(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.scope"][r] =='CHANGED'):
        cve_scope_changed__cvssv3_sh+=1
    elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.scope"][r] =='UNCHANGED'):
        cve_scope_unchanged__cvssv3_sh+=1
    else:
        cve_no_scope_cvssv3_sh+=1
    
print("**************************ESTADÍSTICAS ALCANCE CVE SEGUN VECTOR CVSSV3 PARTE SMART HOME********************************")
print("\n")
print("EN "+str(cve_scope_changed__cvssv3_sh)+" VULNERABILIDADES EL ALCANCE ES MODIFICADO \n")
print("EN "+str(cve_scope_unchanged__cvssv3_sh)+" VULNERABILIDADES EL ALCANCE ES NO MODIFICADO \n")
print("EN "+str(cve_no_scope_cvssv3_sh)+" VULNERABILIDADES EL ALCANCE NO ESTÁ ESPECIFICADO")
print("\n")
print("**************************PORCENTAJE ALCANCE CVE SEGUN VECTOR CVSSV3 PARTE SMART HOME********************************")
print("\n")

print("EN EL "+str(float(((cve_scope_changed__cvssv3_sh*100)/len(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.scope"]))))+"% DE LAS VULNERABILIDADES EL ALCANCE ES MODIFICADO \n")
print("EN EL "+str(float(((cve_scope_unchanged__cvssv3_sh*100)/len(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.scope"]))))+"% DE LAS VULNERABILIDADES EL ALCANCE ES NO MODIFICADO \n")
print("EN EL "+str(float(((cve_no_scope_cvssv3_sh*100)/len(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.scope"]))))+"% DE LAS VULNERABILIDADES NO HAY SCOPE ESPECIFICADO \n")









print("**************************ESTADÍSTICAS ALCANCE CVE SEGUN VECTOR CVSSV3 PARTE IOT Y SMART HOME CONJUNTAS********************************")
print("\n")
print("EN "+str(cve_scope_changed__cvssv3_sh+cve_scope_changed__cvssv3_iot)+" VULNERABILIDADES EL ALCANCE ES MODIFICADO \n")
print("EN "+str(cve_scope_unchanged__cvssv3_sh+cve_scope_unchanged__cvssv3_iot)+" VULNERABILIDADES EL ALCANCE ES NO MODIFICADO \n")
print("EN "+str(cve_no_scope_cvssv3_sh+cve_no_scope_cvssv3_iot)+" VULNERABILIDADES EL ALCANCE NO ESTÁ ESPECIFICADO")
print("\n")
print("**************************PORCENTAJE ALCANCE CVE SEGUN VECTOR CVSSV3 PARTE IOT Y SMART HOME CONJUNTAS********************************")
print("\n")

print("EN EL "+str(float((((cve_scope_changed__cvssv3_sh+cve_scope_changed__cvssv3_iot)*100)/(len(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.scope"])+len(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.scope"])))))+"% DE LAS VULNERABILIDADES EL ALCANCE ES MODIFICADO \n")
print("EN EL "+str(float((((cve_scope_unchanged__cvssv3_sh+cve_scope_unchanged__cvssv3_iot)*100)/(len(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.scope"])+len(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.scope"])))))+"% DE LAS VULNERABILIDADES EL ALCANCE ES NO MODIFICADO \n")
print("EN EL "+str(float((((cve_no_scope_cvssv3_sh+cve_no_scope_cvssv3_iot)*100)/(len(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.scope"])+len(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.scope"])))))+"% DE LAS VULNERABILIDADES NO HAY SCOPE ESPECIFICADO \n")












