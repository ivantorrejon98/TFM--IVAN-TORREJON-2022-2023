import pandas as pd

#Abro los ficheros con los que voy a tratar


df_cve_iot=pd.read_excel('cves_iot_2023.xlsx')
df_cve_sh=pd.read_excel('cves_smart_home_2023.xlsx')


#Variables donde almacenare el contador de niveles de INTERACCION DE USUARIO REQUERIDA
count_requiredui_cvev3_iot=0
count_norequiredui_cvev3_iot=0

#Recorro los valores de INTERACCION DE USUARIO REQUERIDA y aumento los contadores segun su valor

for j in range(0,len(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.userInteraction"])):
    if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.userInteraction"][j]=='REQUIRED'):
        count_requiredui_cvev3_iot+=1
    else:
        count_norequiredui_cvev3_iot+=1
    

print("**************************ESTADÍSTICAS INTERACCION DE USUARIO REQUERIDA EN CVE SEGÚN VECTOR CVSSV3 PARTE IOT********************************")
print("\n")
print(" EN "+str(count_requiredui_cvev3_iot)+" VULNERABILIDADES ES REQUERIDA LA INTERACCION DEL USUARIO \n")
print(" EN "+str(count_norequiredui_cvev3_iot)+" VULNERABILIDADES NO ES REQUERIDA LA INTERACCION DEL USUARIO \n")
print("\n")

print("************************** PORCENTAJE INTERACCION DE USUARIO REQUERIDA EN CVE SEGÚN VECTOR CVSSV3 PARTE IOT********************************")
print("\n")
print("EL "+str(float(((count_requiredui_cvev3_iot*100)/len(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.userInteraction"]))))+"% DE LAS VULNERABILIDADES REQUIERE DE INTERACCION DE USUARIO \n")
print("EL "+str(float(((count_norequiredui_cvev3_iot*100)/len(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.userInteraction"]))))+"% DE LAS VULNERABILIDADES NO REQUIERE DE INTERACCION DE USUARIO \n")
print("\n")
print("\n") 
print("\n")
print("\n")

#Variables donde almacenare el contador de niveles de INTERACCION DE USUARIO REQUERIDA
count_requiredui_cvev3_sh=0
count_norequiredui_cvev3_sh=0



#Recorro los valores de INTERACCION DE USUARIO REQUERIDA y aumento los contadores segun su valor

for r in range(0,len(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.userInteraction"])):
    if(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.userInteraction"][r]=='REQUIRED'):
        count_requiredui_cvev3_sh+=1
    else:
        count_norequiredui_cvev3_sh+=1
    

print("**************************ESTADÍSTICAS INTERACCION DE USUARIO REQUERIDA EN CVE SEGÚN VECTOR CVSSV3 PARTE SMART HOME ********************************")
print("\n")

print(" EN "+str(count_requiredui_cvev3_sh)+" VULNERABILIDADES ES REQUERIDA LA INTERACCION DEL USUARIO \n")
print(" EN "+str(count_norequiredui_cvev3_sh)+" VULNERABILIDADES NO ES REQUERIDA LA INTERACCION DEL USUARIO \n")
print("\n")

print("************************** PORCENTAJE INTERACCION DE USUARIO REQUERIDA EN CVE SEGÚN VECTOR CVSSV3 PARTE SMART HOME*******************************")
print("\n")
print("EL "+str(float(((count_requiredui_cvev3_sh*100)/len(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.userInteraction"]))))+"% DE LAS VULNERABILIDADES REQUIERE DE INTERACCION DE USUARIO \n")
print("EL "+str(float(((count_norequiredui_cvev3_sh*100)/len(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.userInteraction"]))))+"% DE LAS VULNERABILIDADES NO REQUIERE DE INTERACCION DE USUARIO \n")
print("\n")
print("\n")
print("\n")
print("\n")




print("**************************ESTADÍSTICAS INTERACCION DE USUARIO REQUERIDA EN CVE SEGÚN VECTOR CVSSV3 PARTE IOT Y SMART HOME CONJUNTAS********************************")
print("\n")

print(" EN "+str(count_requiredui_cvev3_iot+count_requiredui_cvev3_sh)+" VULNERABILIDADES ES REQUERIDA LA INTERACCION DEL USUARIO \n")
print(" EN "+str(count_norequiredui_cvev3_iot+count_norequiredui_cvev3_sh)+" VULNERABILIDADES NO ES REQUERIDA LA INTERACCION DEL USUARIO \n")
print("\n")
print("************************** PORCENTAJE INTERACCION DE USUARIO REQUERIDA EN CVE SEGÚN VECTOR CVSSV3 PARTE IOT Y SMART HOME CONJUNTAS********************************")
print("\n")
print("\n")
print("EL "+str(float((((count_requiredui_cvev3_iot+count_requiredui_cvev3_sh)*100)/(len(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.userInteraction"])+len(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.userInteraction"])))))+"% DE LAS VULNERABILIDADES REQUIERE DE INTERACCION DE USUARIO \n")
print("EL "+str(float((((count_norequiredui_cvev3_iot+count_norequiredui_cvev3_sh)*100)/(len(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.userInteraction"])+len(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.userInteraction"])))))+"% DE LAS VULNERABILIDADES NO REQUIERE DE INTERACCION DE USUARIO \n")
print("\n")
print("\n")
print("\n")
print("\n")


