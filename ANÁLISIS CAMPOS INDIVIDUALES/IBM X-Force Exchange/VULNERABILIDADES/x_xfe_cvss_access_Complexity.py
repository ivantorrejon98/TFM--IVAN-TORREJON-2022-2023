
import pandas as pd

#Abro los ficheros con los que voy a tratar

df_vuln_ibm_iot = pd.read_excel('vulnerabilidades_ibm_iot_2023.xlsx')
df_vuln_ibm_sh=pd.read_excel('vulnerabilidades_ibm_smart_home_2023.xlsx')


#Variables donde almacenare el contador de niveles de COMPLEJIDAD DE ACCESO
count_high_comacc_ibm_iot=0
count_low_comacc_ibm_iot=0
count_none_comacc_ibm_iot=0

#Recorro los valores de COMPLEJIDAD DE ACCESO y aumento los contadores segun su valor

for i in range(0,len(df_vuln_ibm_iot.x_xfe_cvss_access_complexity)):
    if(df_vuln_ibm_iot.x_xfe_cvss_access_complexity[i]=='High'):
        count_high_comacc_ibm_iot+=1
    elif(df_vuln_ibm_iot.x_xfe_cvss_access_complexity[i]=='Low'):
        count_low_comacc_ibm_iot+=1
    else:
        count_none_comacc_ibm_iot+=1
    

print("**************************ESTADÍSTICAS COMPLEJIDAD DE ACCESO EN VULNERABILIDADES IBM IOT********************************")
print("\n")
print("LA COMPLEJIDAD DE ACCESO EN "+str(count_high_comacc_ibm_iot)+" VULNERABILIDADES ES ALTA \n")
print("LA COMPLEJIDAD DE ACCESO EN "+str(count_low_comacc_ibm_iot)+" VULNERABILIDADES ES BAJA \n")
print("LA COMPLEJIDAD DE ACCESO EN "+str(count_none_comacc_ibm_iot)+" VULNERABILIDADES NO VIENE ESPECIFICADA \n")
print("\n")
print("**************************PORCENTAJE COMPLEJIDAD DE ACCESO EN VULNERABILIDADES IBM IOT********************************")
print("\n")
print("EL "+str(float(((count_high_comacc_ibm_iot*100)/len(df_vuln_ibm_iot.x_xfe_cvss_access_complexity))))+"% DE LAS VULNERABILIDADES TIENE UNA BAJA COMPLEJIDAD DE ACCESO \n")
print("EL "+str(float(((count_low_comacc_ibm_iot*100)/len(df_vuln_ibm_iot.x_xfe_cvss_access_complexity))))+"% DE LAS VULNERABILIDADES TIENE UNA BAJA COMPLEJIDAD DE ACCESO \n")
print("EL "+str(float(((count_none_comacc_ibm_iot*100)/len(df_vuln_ibm_iot.x_xfe_cvss_access_complexity))))+"% DE LAS VULNERABILIDADES NO TIENE COMPLEJIDAD DE ACCESO ESPECIFICADA \n")
print("\n")




#Variables donde almacenare el contador de niveles de COMPLEJIDAD DE ACCESO
count_high_comacc_ibm_sh=0
count_low_comacc_ibm_sh=0
count_none_comacc_ibm_sh=0

#Recorro los valores de COMPLEJIDAD DE ACCESO y aumento los contadores segun su valor

for l in range(0,len(df_vuln_ibm_sh.x_xfe_cvss_access_complexity)):
    if(df_vuln_ibm_sh.x_xfe_cvss_access_complexity[l]=='High'):
        count_high_comacc_ibm_sh+=1
    elif(df_vuln_ibm_sh.x_xfe_cvss_access_complexity[l]=='Low'):
        count_low_comacc_ibm_sh+=1
    else:
        count_none_comacc_ibm_sh+=1
    

print("**************************COMPLEJIDAD DE ACCESO EN VULNERABILIDADES IBM SMART HOME********************************")
print("\n")
print("LA COMPLEJIDAD DE ACCESO EN "+str(count_high_comacc_ibm_sh)+" VULNERABILIDADES ES ALTA \n")
print("LA COMPLEJIDAD DE ACCESO EN "+str(count_low_comacc_ibm_sh)+" VULNERABILIDADES ES BAJA \n")
print("LA COMPLEJIDAD DE ACCESO EN "+str(count_none_comacc_ibm_sh)+" VULNERABILIDADES NO VIENE ESPECIFICADA \n")
print("\n")
print("**************************PORCENTAJE COMPLEJIDAD DE ACCESO EN VULNERABILIDADES IBM SMART HOME********************************")
print("\n")
print("EL "+str(float(((count_high_comacc_ibm_sh*100)/len(df_vuln_ibm_sh.x_xfe_cvss_access_complexity))))+"% DE LAS VULNERABILIDADES TIENE UNA BAJA COMPLEJIDAD DE ACCESO \n")
print("EL "+str(float(((count_low_comacc_ibm_sh*100)/len(df_vuln_ibm_sh.x_xfe_cvss_access_complexity))))+"% DE LAS VULNERABILIDADES TIENE UNA BAJA COMPLEJIDAD DE ACCESO \n")
print("EL "+str(float(((count_none_comacc_ibm_sh*100)/len(df_vuln_ibm_sh.x_xfe_cvss_access_complexity))))+"% DE LAS VULNERABILIDADES NO TIENE COMPLEJIDAD DE ACCESO ESPECIFICADA \n")
print("\n")




print("**************************ESTADÍSTICAS COMPLEJIDAD DE ACCESO EN VULNERABILIDADES IBM PARTE IOT Y SMART HOME CONJUNTAS********************************")
print("\n")
print("LA COMPLEJIDAD DE ACCESO EN "+str(count_high_comacc_ibm_sh+count_high_comacc_ibm_iot)+" VULNERABILIDADES ES ALTA \n")
print("LA COMPLEJIDAD DE ACCESO EN "+str(count_low_comacc_ibm_sh+count_low_comacc_ibm_iot)+" VULNERABILIDADES ES BAJA \n")
print("LA COMPLEJIDAD DE ACCESO EN "+str(count_none_comacc_ibm_sh+count_none_comacc_ibm_iot)+" VULNERABILIDADES NO VIENE ESPECIFICADA \n")
print("\n")
print("**************************PORCENTAJE COMPLEJIDAD DE ACCESO EN VULNERABILIDADES IBM PARTE IOT Y SMART HOME CONJUNTAS********************************")
print("\n")
print("EL "+str(float((((count_high_comacc_ibm_sh+count_high_comacc_ibm_iot)*100)/(len(df_vuln_ibm_sh.x_xfe_cvss_access_complexity)+len(df_vuln_ibm_iot.x_xfe_cvss_access_complexity)))))+"% DE LAS VULNERABILIDADES TIENE UNA BAJA COMPLEJIDAD DE ACCESO \n")
print("EL "+str(float((((count_low_comacc_ibm_sh+count_low_comacc_ibm_iot)*100)/(len(df_vuln_ibm_sh.x_xfe_cvss_access_complexity)+len(df_vuln_ibm_iot.x_xfe_cvss_access_complexity)))))+"% DE LAS VULNERABILIDADES TIENE UNA BAJA COMPLEJIDAD DE ACCESO \n")
print("EL "+str(float((((count_none_comacc_ibm_sh+count_none_comacc_ibm_iot)*100)/(len(df_vuln_ibm_sh.x_xfe_cvss_access_complexity)+len(df_vuln_ibm_iot.x_xfe_cvss_access_complexity)))))+"% DE LAS VULNERABILIDADES NO TIENE COMPLEJIDAD DE ACCESO ESPECIFICADA \n")
print("\n")



