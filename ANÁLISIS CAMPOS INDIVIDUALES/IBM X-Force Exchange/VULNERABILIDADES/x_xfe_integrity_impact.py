
import pandas as pd

#Abro los ficheros con los que voy a tratar

df_vuln_ibm_iot = pd.read_excel('vulnerabilidades_ibm_iot_2023.xlsx')
df_vuln_ibm_sh=pd.read_excel('vulnerabilidades_ibm_smart_home_2023.xlsx')

#Variables donde almacenare el contador de niveles de impacto de integridad
count_high_int_ibm_iot=0
count_low_int_ibm_iot=0
count_none_int_ibm_iot=0


#Recorro los valores de impacto de integridad y aumento los contadores segun su valor

for i in range(0,len(df_vuln_ibm_iot.x_xfe_cvss_integrity_impact)):
    if(df_vuln_ibm_iot.x_xfe_cvss_integrity_impact[i]=='High'):
        count_high_int_ibm_iot+=1
    elif(df_vuln_ibm_iot.x_xfe_cvss_integrity_impact[i]=='Low'):
        count_low_int_ibm_iot+=1
    else:
        count_none_int_ibm_iot+=1
    

print("**************************ESTADÍSTICAS IMPACTO DE INTEGRIDAD EN VULNERABILIDADES IBM IOT********************************")
print("\n")
print("EL IMPACTO DE INTEGRIDAD EN "+str(count_high_int_ibm_iot)+" VULNERABILIDADES ES ALTO \n")
print("EL IMPACTO DE INTEGRIDAD EN "+str(count_low_int_ibm_iot)+" VULNERABILIDADES ES BAJO \n")
print("EN "+str(count_none_int_ibm_iot)+" VULNERABILIDADES NO EXISTE IMPACTO DE INTEGRIDAD \n")
print("\n")
print("**************************PORCENTAJE IMPACTO DE INTEGRIDAD EN VULNERABILIDADES IBM IOT********************************")
print("\n")
print("EL "+str(float(((count_high_int_ibm_iot*100)/len(df_vuln_ibm_iot.x_xfe_cvss_integrity_impact))))+"% DE LAS VULNERABILIDADES TIENE UN ALTO IMPACTO DE INTEGRIDAD \n")
print("EL "+str(float(((count_low_int_ibm_iot*100)/len(df_vuln_ibm_iot.x_xfe_cvss_integrity_impact))))+"% DE LAS VULNERABILIDADES TIENE UN BAJO IMPACTO DE INTEGRIDAD \n")
print("EL "+str(float(((count_none_int_ibm_iot*100)/len(df_vuln_ibm_iot.x_xfe_cvss_integrity_impact))))+"% DE LAS VULNERABILIDADES NO TIENE IMPACTO DE INTEGRIDAD \n")
print("\n")




#Variables donde almacenare el contador de niveles de impacto de integridad
count_high_int_ibm_sh=0
count_low_int_ibm_sh=0
count_none_int_ibm_sh=0

#Recorro los valores de impacto de integridad y aumento los contadores segun su valor

for l in range(0,len(df_vuln_ibm_sh.x_xfe_cvss_integrity_impact)):
    if(df_vuln_ibm_sh.x_xfe_cvss_integrity_impact[l]=='High'):
        count_high_int_ibm_sh+=1
    elif(df_vuln_ibm_sh.x_xfe_cvss_integrity_impact[l]=='Low'):
        count_low_int_ibm_sh+=1
    else:
        count_none_int_ibm_sh+=1
    

print("**************************ESTADÍSTICAS IMPACTO DE INTEGRIDAD EN VULNERABILIDADES IBM SMART HOME********************************")
print("\n")
print("EL IMPACTO DE INTEGRIDAD EN "+str(count_high_int_ibm_sh)+" VULNERABILIDADES ES ALTO \n")
print("EL IMPACTO DE INTEGRIDAD EN "+str(count_low_int_ibm_sh)+" VULNERABILIDADES ES BAJO \n")
print("EN "+str(count_none_int_ibm_sh)+" VULNERABILIDADES NO EXISTE IMPACTO DE INTEGRIDAD \n")
print("\n")
print("**************************PORCENTAJE IMPACTO DE INTEGRIDAD EN VULNERABILIDADES IBM SMART HOME********************************")
print("\n")
print("EL "+str(float(((count_high_int_ibm_sh*100)/len(df_vuln_ibm_sh.x_xfe_cvss_integrity_impact))))+"% DE LAS VULNERABILIDADES TIENE UN ALTO IMPACTO DE INTEGRIDAD \n")
print("EL "+str(float(((count_low_int_ibm_sh*100)/len(df_vuln_ibm_sh.x_xfe_cvss_integrity_impact))))+"% DE LAS VULNERABILIDADES TIENE UN BAJO IMPACTO DE INTEGRIDAD \n")
print("EL "+str(float(((count_none_int_ibm_sh*100)/len(df_vuln_ibm_sh.x_xfe_cvss_integrity_impact))))+"% DE LAS VULNERABILIDADES NO TIENE IMPACTO DE INTEGRIDAD \n")
print("\n")



print("**************************ESTADÍSTICAS IMPACTO DE INTEGRIDAD EN VULNERABILIDADES IBM PARTE IOT Y SMART HOME CONJUNTAS********************************")
print("\n")
print("EL IMPACTO DE INTEGRIDAD EN "+str(count_high_int_ibm_sh+count_high_int_ibm_iot)+" VULNERABILIDADES ES ALTO \n")
print("EL IMPACTO DE INTEGRIDAD EN "+str(count_low_int_ibm_sh+count_low_int_ibm_iot)+" VULNERABILIDADES ES BAJO \n")
print("EN "+str(count_none_int_ibm_sh+count_none_int_ibm_iot)+" VULNERABILIDADES NO EXISTE IMPACTO DE INTEGRIDAD \n")
print("\n")
print("**************************PORCENTAJE IMPACTO DE INTEGRIDAD EN VULNERABILIDADES IBM PARTE IOT Y SMART HOME CONJUNTAS********************************")
print("\n")
print("EL "+str(float((((count_high_int_ibm_sh+count_high_int_ibm_iot)*100)/(len(df_vuln_ibm_sh.x_xfe_cvss_integrity_impact)+len(df_vuln_ibm_iot.x_xfe_cvss_integrity_impact)))))+"% DE LAS VULNERABILIDADES TIENE UN ALTO IMPACTO DE INTEGRIDAD \n")
print("EL "+str(float((((count_low_int_ibm_sh+count_low_int_ibm_iot)*100)/(len(df_vuln_ibm_sh.x_xfe_cvss_integrity_impact)+len(df_vuln_ibm_iot.x_xfe_cvss_integrity_impact)))))+"% DE LAS VULNERABILIDADES TIENE UN BAJO IMPACTO DE INTEGRIDAD \n")
print("EL "+str(float((((count_none_int_ibm_sh+count_none_int_ibm_iot)*100)/(len(df_vuln_ibm_sh.x_xfe_cvss_integrity_impact)+len(df_vuln_ibm_iot.x_xfe_cvss_integrity_impact)))))+"% DE LAS VULNERABILIDADES NO TIENE IMPACTO DE INTEGRIDAD \n")
print("\n")






