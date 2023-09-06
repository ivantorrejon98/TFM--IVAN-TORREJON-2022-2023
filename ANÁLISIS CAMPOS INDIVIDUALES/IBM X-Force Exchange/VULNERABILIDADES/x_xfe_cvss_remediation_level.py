

import pandas as pd

#Abro los ficheros con los que voy a tratar

df_vuln_ibm_iot = pd.read_excel('vulnerabilidades_ibm_iot_2023.xlsx')
df_vuln_ibm_sh=pd.read_excel('vulnerabilidades_ibm_smart_home_2023.xlsx')




#Variables donde almacenare el contador de nivel de remediacion para vulnerabilidades IBM 
official_fix_remed_level_iot=0
unavailable_remed_level_iot=0
official_fix_remed_level_sh=0
unavailable_remed_level_sh=0

#Compruebo el nivel de remediacion en vulnerabilidades IBM para IOT

for i in range(0,len(df_vuln_ibm_iot["x_xfe_cvss_remediation_level"])):
    if(df_vuln_ibm_iot["x_xfe_cvss_remediation_level"][i]=='Official Fix'):
        official_fix_remed_level_iot+=1
    else:
        unavailable_remed_level_iot+=1

print("**************************ESTADÍSTICAS NIVEL DE REMEDIACION EN VULNERABILIDADES IBM IOT********************************")
print("\n")
print("EN "+str(official_fix_remed_level_iot)+" VULNERABILIDADES EL NIVEL DE REMEDIACION ESTA TOTALMENTE ARREGLADO \n")
print("EN "+str(unavailable_remed_level_iot)+" VULNERABILIDADES EL NIVEL DE REMEDIACION NO ESTA DISPONIBLE \n")
print("\n")
print("***************************PORCENTAJE NIVEL DE REMEDIACION EN VULNERABILIDADES IBM IOT********************************")
print("\n")
print("EN EL "+str(float(((official_fix_remed_level_iot*100)/len(df_vuln_ibm_iot["x_xfe_cvss_remediation_level"]))))+"% DE LAS VULNERABILIDADES EL NIVEL DE REMEDIACION ES TOTALMENTE ARREGLADO \n")
print("EN EL "+str(float(((unavailable_remed_level_iot*100)/len(df_vuln_ibm_iot["x_xfe_cvss_remediation_level"]))))+"% DE LAS VULNERABILIDADES EL NIVEL DE REMEDIACION NO ESTA DISPONIBLE \n")

print("\n")







#Compruebo el nivel de remediacion en vulnerabilidades IBM para SMART HOME

for j in range(0,len(df_vuln_ibm_sh["x_xfe_cvss_remediation_level"])):
    if(df_vuln_ibm_sh["x_xfe_cvss_remediation_level"][j]=='Official Fix'):
        official_fix_remed_level_sh+=1
    else:
        unavailable_remed_level_sh+=1


print("**************************ESTADÍSTICAS NIVEL DE REMEDIACION EN VULNERABILIDADES IBM SMART HOME********************************")
print("\n")
print("EN "+str(official_fix_remed_level_sh)+" VULNERABILIDADES EL NIVEL DE REMEDIACION ESTA TOTALMENTE ARREGLADO \n")
print("EN "+str(unavailable_remed_level_sh)+" VULNERABILIDADES EL NIVEL DE REMEDIACION NO ESTA DISPONIBLE \n")
print("\n")
print("***************************PORCENTAJE NIVEL DE REMEDIACION EN VULNERABILIDADES IBM SMART HOME********************************")
print("\n")
print("EN EL "+str(float(((official_fix_remed_level_sh*100)/len(df_vuln_ibm_sh["x_xfe_cvss_remediation_level"]))))+"% DE LAS VULNERABILIDADES EL NIVEL DE REMEDIACION ES TOTALMENTE ARREGLADO \n")
print("EN EL "+str(float(((unavailable_remed_level_sh*100)/len(df_vuln_ibm_sh["x_xfe_cvss_remediation_level"]))))+"% DE LAS VULNERABILIDADES EL NIVEL DE REMEDIACION NO ESTA DISPONIBLE \n")

print("\n")






print("**************************ESTADÍSTICAS NIVEL DE REMEDIACION EN VULNERABILIDADES IBM PARTE IOT Y SMART HOME CONJUNTAS********************************")
print("\n")
print("EN "+str(official_fix_remed_level_sh+official_fix_remed_level_iot)+" VULNERABILIDADES EL NIVEL DE REMEDIACION ESTA TOTALMENTE ARREGLADO \n")
print("EN "+str(unavailable_remed_level_sh+unavailable_remed_level_iot)+" VULNERABILIDADES EL NIVEL DE REMEDIACION NO ESTA DISPONIBLE \n")
print("\n")
print("***************************PORCENTAJE NIVEL DE REMEDIACION EN VULNERABILIDADES IBM PARTE IOT Y SMART HOME CONJUNTAS********************************")
print("\n")
print("EN EL "+str(float((((official_fix_remed_level_sh+official_fix_remed_level_iot)*100)/(len(df_vuln_ibm_sh["x_xfe_cvss_remediation_level"])+len(df_vuln_ibm_iot["x_xfe_cvss_remediation_level"])))))+"% DE LAS VULNERABILIDADES EL NIVEL DE REMEDIACION ES TOTALMENTE ARREGLADO \n")
print("EN EL "+str(float((((unavailable_remed_level_sh+unavailable_remed_level_iot)*100)/(len(df_vuln_ibm_sh["x_xfe_cvss_remediation_level"])+len(df_vuln_ibm_iot["x_xfe_cvss_remediation_level"])))))+"% DE LAS VULNERABILIDADES EL NIVEL DE REMEDIACION NO ESTA DISPONIBLE \n")

print("\n")




