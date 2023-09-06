




import pandas as pd

#Abro los ficheros con los que voy a tratar

df_vuln_ibm_iot = pd.read_excel('vulnerabilidades_ibm_iot_2023.xlsx')
df_vuln_ibm_sh=pd.read_excel('vulnerabilidades_ibm_smart_home_2023.xlsx')



#Variables donde almacenare el contador de niveles de INTERACCION DE USUARIO REQUERIDA
count_requiredui_ibm_iot=0
count_norequiredui_ibm_iot=0

#Recorro los valores de INTERACCION DE USUARIO REQUERIDA y aumento los contadores segun su valor

for i in range(0,len(df_vuln_ibm_iot["x_xfe_cvss_userinteraction"])):
    if(df_vuln_ibm_iot["x_xfe_cvss_userinteraction"][i] =='Required'):
        count_requiredui_ibm_iot+=1
    else:
        count_norequiredui_ibm_iot+=1
    

print("**************************ESTADÍSTICAS INTERACCION DE USUARIO REQUERIDA EN VULNERABILIDADES IBM IOT********************************")
print("\n")
print(" EN "+str(count_requiredui_ibm_iot)+" VULNERABILIDADES ES REQUERIDA LA INTERACCION DEL USUARIO \n")
print(" EN "+str(count_norequiredui_ibm_iot)+" VULNERABILIDADES NO ES REQUERIDA LA INTERACCION DEL USUARIO \n")
print("\n")
print("************************** PORCENTAJE INTERACCION DE USUARIO REQUERIDA EN VULNERABILIDADES IBM IOT********************************")
print("\n")
print("EL "+str(float(((count_requiredui_ibm_iot*100)/len(df_vuln_ibm_iot["x_xfe_cvss_userinteraction"]))))+"% DE LAS VULNERABILIDADES REQUIERE DE INTERACCION DE USUARIO \n")
print("EL "+str(float(((count_norequiredui_ibm_iot*100)/len(df_vuln_ibm_iot["x_xfe_cvss_userinteraction"]))))+"% DE LAS VULNERABILIDADES NO REQUIERE DE INTERACCION DE USUARIO \n")
print("\n")


#Variables donde almacenare el contador de niveles de INTERACCION DE USUARIO REQUERIDA
count_requiredui_ibm_sh=0
count_norequiredui_ibm_sh=0

#Recorro los valores de INTERACCION DE USUARIO REQUERIDA y aumento los contadores segun su valor

for i in range(0,len(df_vuln_ibm_sh["x_xfe_cvss_userinteraction"])):
    if(df_vuln_ibm_sh["x_xfe_cvss_userinteraction"][i] =='Required'):
        count_requiredui_ibm_sh+=1
    else:
        count_norequiredui_ibm_sh+=1
    

print("**************************INTERACCION DE USUARIO REQUERIDA EN VULNERABILIDADES IBM SMART HOME********************************")
print("\n")
print(" EN "+str(count_requiredui_ibm_sh)+" VULNERABILIDADES ES REQUERIDA LA INTERACCION DEL USUARIO \n")
print(" EN "+str(count_norequiredui_ibm_sh)+" VULNERABILIDADES NO ES REQUERIDA LA INTERACCION DEL USUARIO \n")
print("\n")
print("************************** PORCENTAJE INTERACCION DE USUARIO REQUERIDA EN VULNERABILIDADES IBM SMART HOME********************************")
print("\n")
print("EL "+str(float(((count_requiredui_ibm_sh*100)/len(df_vuln_ibm_sh["x_xfe_cvss_userinteraction"]))))+"% DE LAS VULNERABILIDADES REQUIERE DE INTERACCION DE USUARIO \n")
print("EL "+str(float(((count_norequiredui_ibm_sh*100)/len(df_vuln_ibm_sh["x_xfe_cvss_userinteraction"]))))+"% DE LAS VULNERABILIDADES NO REQUIERE DE INTERACCION DE USUARIO \n")
print("\n")



print("**************************INTERACCION DE USUARIO REQUERIDA EN VULNERABILIDADES IBM PARTE IOT Y SMART HOME CONJUNTAS********************************")
print("\n")
print(" EN "+str(count_requiredui_ibm_sh+count_requiredui_ibm_iot)+" VULNERABILIDADES ES REQUERIDA LA INTERACCION DEL USUARIO \n")
print(" EN "+str(count_norequiredui_ibm_sh+count_norequiredui_ibm_iot)+" VULNERABILIDADES NO ES REQUERIDA LA INTERACCION DEL USUARIO \n")
print("\n")
print("************************** PORCENTAJE INTERACCION DE USUARIO REQUERIDA VULNERABILIDADES IBM PARTE IOT Y SMART HOME CONJUNTAS********************************")
print("\n")
print("EL "+str(float((((count_requiredui_ibm_sh+count_requiredui_ibm_iot)*100)/(len(df_vuln_ibm_sh["x_xfe_cvss_userinteraction"])+len(df_vuln_ibm_iot["x_xfe_cvss_userinteraction"])))))+"% DE LAS VULNERABILIDADES REQUIERE DE INTERACCION DE USUARIO \n")
print("EL "+str(float((((count_norequiredui_ibm_sh+count_norequiredui_ibm_iot)*100)/(len(df_vuln_ibm_sh["x_xfe_cvss_userinteraction"])+len(df_vuln_ibm_iot["x_xfe_cvss_userinteraction"])))))+"% DE LAS VULNERABILIDADES NO REQUIERE DE INTERACCION DE USUARIO \n")
print("\n")


