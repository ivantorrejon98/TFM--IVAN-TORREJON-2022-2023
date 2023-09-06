

import pandas as pd

df_vuln_ibm_iot = pd.read_excel('vulnerabilidades_ibm_iot_2023.xlsx')
df_vuln_ibm_sh=pd.read_excel('vulnerabilidades_ibm_smart_home_2023.xlsx')






#Variables donde almacenare el contador de tipos de alcance
ibm_scope_changed_iot=0
ibm_scope_unchanged_iot=0
ibm_no_scope_iot=0

#Recorro los valores de alcance y  aumento los contadores segun su valor

for i in range(0,len(df_vuln_ibm_iot["x_xfe_cvss_scope"])):
    if(df_vuln_ibm_iot["x_xfe_cvss_scope"][i] =='Changed'):
        ibm_scope_changed_iot+=1
    elif(df_vuln_ibm_iot["x_xfe_cvss_scope"][i] =='Unchanged'):
        ibm_scope_unchanged_iot+=1
    else:
        ibm_no_scope_iot+=1


print("**************************ESTADÍSTICAS ALCANCE EN VULNERABILIDADES IBM IOT********************************")
print("\n")
print("EN "+str(ibm_scope_changed_iot)+" VULNERABILIDADES EL ALCANCE ES CAMBIADO \n")
print("EN "+str(ibm_scope_unchanged_iot)+" VULNERABILIDADES EL ALCANCE NO ES CAMBIADO \n")
print("EN "+str(ibm_no_scope_iot)+" VULNERABILIDADES NO VIENE ESPECIFICADO EL ALCANCE")
print("\n")
print("**************************PORCENTAJE ALCANCE EN VULNERABILIDADES IBM IO********************************")
print("\n")
print("EN EL "+str(float(((ibm_scope_changed_iot*100)/len(df_vuln_ibm_iot["x_xfe_cvss_scope"]))))+"% DE LAS VULNERABILIDADES EL ALCANCE ES CAMBIADO \n")
print("EN EL "+str(float(((ibm_scope_unchanged_iot*100)/len(df_vuln_ibm_iot["x_xfe_cvss_scope"]))))+"% DE LAS VULNERABILIDADES EL ALCANCE NO ES CAMBIADO \n")
print("EN EL "+str(float(((ibm_no_scope_iot*100)/len(df_vuln_ibm_iot["x_xfe_cvss_scope"]))))+"% DE LAS VULNERABILIDADES EL ALCANCE NO VIENE ESPECIFICADO")
print("\n")




#Variables donde almacenare el contador de tipos de alcance
ibm_scope_changed_sh=0
ibm_scope_unchanged_sh=0
ibm_no_scope_sh=0

#Recorro los valores de alcance y  aumento los contadores segun su valor

for i in range(0,len(df_vuln_ibm_sh["x_xfe_cvss_scope"])):
    if(df_vuln_ibm_sh["x_xfe_cvss_scope"][i] =='Changed'):
        ibm_scope_changed_sh+=1
    elif(df_vuln_ibm_sh["x_xfe_cvss_scope"][i] =='Unchanged'):
        ibm_scope_unchanged_sh+=1
    else:
        ibm_no_scope_sh+=1


print("**************************ESTADÍSTICAS ALCANCE EN VULNERABILIDADES IBM SMART HOME********************************")
print("\n")
print("EN "+str(ibm_scope_changed_sh)+" VULNERABILIDADES EL ALCANCE ES CAMBIADO \n")
print("EN "+str(ibm_scope_unchanged_sh)+" VULNERABILIDADES EL ALCANCE NO ES CAMBIADO \n")
print("EN "+str(ibm_no_scope_sh)+" VULNERABILIDADES NO VIENE ESPECIFICADO EL ALCANCE")
print("\n")
print("**************************PORCENTAJE ALCANCE EN VULNERABILIDADES IBM SMART HOME********************************")
print("\n")
print("EN EL "+str(float(((ibm_scope_changed_sh*100)/len(df_vuln_ibm_sh["x_xfe_cvss_scope"]))))+"% DE LAS VULNERABILIDADES EL ALCANCE ES CAMBIADO \n")
print("EN EL "+str(float(((ibm_scope_unchanged_sh*100)/len(df_vuln_ibm_sh["x_xfe_cvss_scope"]))))+"% DE LAS VULNERABILIDADES EL ALCANCE NO ES CAMBIADO \n")
print("EN EL "+str(float(((ibm_no_scope_sh*100)/len(df_vuln_ibm_sh["x_xfe_cvss_scope"]))))+"% DE LAS VULNERABILIDADES EL ALCANCE NO VIENE ESPECIFICADO \n")
print("\n")







print("**************************ESTADÍSTICAS ALCANCE EN VULNERABILIDADES IBM PARTE IOT Y SMART HOME CONJUNTAS********************************")
print("\n")
print("EN "+str(ibm_scope_changed_sh+ibm_scope_changed_iot)+" VULNERABILIDADES EL ALCANCE ES CAMBIADO \n")
print("EN "+str(ibm_scope_unchanged_sh+ibm_scope_unchanged_iot)+" VULNERABILIDADES EL ALCANCE NO ES CAMBIADO \n")
print("EN "+str(ibm_no_scope_sh+ibm_no_scope_iot)+" VULNERABILIDADES NO VIENE ESPECIFICADO EL ALCANCE")
print("\n")
print("**************************PORCENTAJE ALCANCE EN VULNERABILIDADES IBM PARTE IOT Y SMART HOME CONJUNTAS********************************")
print("\n")
print("EL "+str(float((((ibm_scope_changed_sh+ibm_scope_changed_iot)*100)/(len(df_vuln_ibm_sh["x_xfe_cvss_scope"])+len(df_vuln_ibm_iot["x_xfe_cvss_scope"])))))+"% DE LAS VULNERABILIDADES EL ALCANCE ES CAMBIADO \n")
print("EL "+str(float((((ibm_scope_unchanged_sh+ibm_scope_unchanged_iot)*100)/(len(df_vuln_ibm_sh["x_xfe_cvss_scope"])+len(df_vuln_ibm_iot["x_xfe_cvss_scope"])))))+"% DE LAS VULNERABILIDADES EL ALCANCE NO ES CAMBIADO \n")
print("EL "+str(float((((ibm_no_scope_sh+ibm_no_scope_iot)*100)/(len(df_vuln_ibm_sh["x_xfe_cvss_scope"])+len(df_vuln_ibm_iot["x_xfe_cvss_scope"])))))+"% DE LAS VULNERABILIDADES EL ALCANCE ES NO ESTA DEFINIDO \n")
print("\n")











