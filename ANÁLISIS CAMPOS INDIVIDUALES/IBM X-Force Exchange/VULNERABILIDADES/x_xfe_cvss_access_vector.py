
import pandas as pd

#Abro los ficheros con los que voy a tratar

df_vuln_ibm_iot = pd.read_excel('vulnerabilidades_ibm_iot_2023.xlsx')
df_vuln_ibm_sh=pd.read_excel('vulnerabilidades_ibm_smart_home_2023.xlsx')


#Variables donde almacenare el contador de niveles de VECTOR DE ACCESO
count_network_vecacc_ibm_iot=0
count_Local_vecacc_ibm_iot=0
count_Physical_vecacc_ibm_iot=0
count_Adjnet_vecacc_ibm_iot=0
count_none_vecacc_ibm_iot=0

#Recorro los valores de VECTOR DE ACCESO y aumento los contadores segun su valor

for i in range(0,len(df_vuln_ibm_iot.x_xfe_cvss_access_vector)):
    if(df_vuln_ibm_iot.x_xfe_cvss_access_vector[i]=='Network'):
        count_network_vecacc_ibm_iot+=1
    elif(df_vuln_ibm_iot.x_xfe_cvss_access_vector[i]=='Local'):
        count_Local_vecacc_ibm_iot+=1
    elif(df_vuln_ibm_iot.x_xfe_cvss_access_vector[i]=='Physical'):
        count_Physical_vecacc_ibm_iot+=1
    elif(df_vuln_ibm_iot.x_xfe_cvss_access_vector[i]=='Adjacent Network'):
        count_Adjnet_vecacc_ibm_iot+=1
    else:
        count_none_vecacc_ibm_iot+=1
    

print("**************************ESTADÍSTICAS VECTOR DE ACCESO EN VULNERABILIDADES IBM IOT********************************")
print("\n")
print("EL VECTOR DE ACCESO EN "+str(count_network_vecacc_ibm_iot)+" VULNERABILIDADES ES A TRAVES DE LA RED \n")
print("EL VECTOR DE ACCESO EN "+str(count_Local_vecacc_ibm_iot)+" VULNERABILIDADES ES LOCAL \n")
print("EL VECTOR DE ACCESO EN "+str(count_Physical_vecacc_ibm_iot)+" VULNERABILIDADES ES FISICO \n")
print("EL VECTOR DE ACCESO EN "+str(count_Adjnet_vecacc_ibm_iot)+" VULNERABILIDADES ES A TRAVES DE UNA RED ADYACENTE \n")
print("EL VECTOR DE ACCESO EN "+str(count_none_vecacc_ibm_iot)+" VULNERABILIDADES NO VIENE ESPECIFICADO \n")
print("\n")
print("**************************PORCENTAJE VECTOR DE ACCESO EN VULNERABILIDADES IBM IOT********************************")
print("\n")
print("EL "+str(float(((count_network_vecacc_ibm_iot*100)/len(df_vuln_ibm_iot.x_xfe_cvss_access_vector))))+"% DE LAS VULNERABILIDADES TIENE UN VECTOR DE ACCESO A TRAVES DE LA RED \n")
print("EL "+str(float(((count_Local_vecacc_ibm_iot*100)/len(df_vuln_ibm_iot.x_xfe_cvss_access_vector))))+"% DE LAS VULNERABILIDADES TIENE UN VECTOR DE ACCESO LOCAL \n")
print("EL "+str(float(((count_Physical_vecacc_ibm_iot*100)/len(df_vuln_ibm_iot.x_xfe_cvss_access_vector))))+"% DE LAS VULNERABILIDADES TIENE UNA VECTOR DE ACCESO FISICO \n")
print("EL "+str(float(((count_Adjnet_vecacc_ibm_iot*100)/len(df_vuln_ibm_iot.x_xfe_cvss_access_vector))))+"% DE LAS VULNERABILIDADES TIENE UNA VECTOR DE ACCESO A TRAVES DE UNA RED ADYACENTE \n")
print("EL "+str(float(((count_none_vecacc_ibm_iot*100)/len(df_vuln_ibm_iot.x_xfe_cvss_access_vector))))+"% DE LAS VULNERABILIDADES NO TIENE VECTOR DE ACCESO ESPECIFICADO \n")
print("\n")





#Variables donde almacenare el contador de niveles de VECTOR DE ACCESO
count_network_vecacc_ibm_sh=0
count_Local_vecacc_ibm_sh=0
count_Physical_vecacc_ibm_sh=0
count_Adjnet_vecacc_ibm_sh=0
count_none_vecacc_ibm_sh=0

#Recorro los valores de VECTOR DE ACCESO y aumento los contadores segun su valor

for l in range(0,len(df_vuln_ibm_sh.x_xfe_cvss_access_vector)):
    if(df_vuln_ibm_sh.x_xfe_cvss_access_vector[l]=='Network'):
        count_network_vecacc_ibm_sh+=1
    elif(df_vuln_ibm_sh.x_xfe_cvss_access_vector[l]=='Local'):
        count_Local_vecacc_ibm_sh+=1
    elif(df_vuln_ibm_sh.x_xfe_cvss_access_vector[l]=='Physical'):
        count_Physical_vecacc_ibm_sh+=1
    elif(df_vuln_ibm_sh.x_xfe_cvss_access_vector[l]=='Adjacent Network'):
        count_Adjnet_vecacc_ibm_sh+=1
    else:
        count_none_vecacc_ibm_sh+=1
    

print("**************************ESTADÍSTICAS VECTOR DE ACCESO EN VULNERABILIDADES IBM SMART HOME********************************")
print("\n")
print("EL VECTOR DE ACCESO EN "+str(count_network_vecacc_ibm_sh)+" VULNERABILIDADES ES A TRAVES DE LA RED \n")
print("EL VECTOR DE ACCESO EN "+str(count_Local_vecacc_ibm_sh)+" VULNERABILIDADES ES LOCAL \n")
print("EL VECTOR DE ACCESO EN "+str(count_Physical_vecacc_ibm_sh)+" VULNERABILIDADES ES FISICO \n")
print("EL VECTOR DE ACCESO EN "+str(count_Adjnet_vecacc_ibm_sh)+" VULNERABILIDADES ES A TRAVES DE UNA RED ADYACENTE \n")
print("EL VECTOR DE ACCESO EN "+str(count_none_vecacc_ibm_sh)+" VULNERABILIDADES NO VIENE ESPECIFICADO \n")
print("\n")
print("**************************PORCENTAJE VECTOR DE ACCESO EN VULNERABILIDADES IBM SMART HOME********************************")
print("\n")
print("EL "+str(float(((count_network_vecacc_ibm_sh*100)/len(df_vuln_ibm_sh.x_xfe_cvss_access_vector))))+"% DE LAS VULNERABILIDADES TIENE UN VECTOR DE ACCESO A TRAVES DE LA RED \n")
print("EL "+str(float(((count_Local_vecacc_ibm_sh*100)/len(df_vuln_ibm_sh.x_xfe_cvss_access_vector))))+"% DE LAS VULNERABILIDADES TIENE UN VECTOR DE ACCESO LOCAL \n")
print("EL "+str(float(((count_Physical_vecacc_ibm_sh*100)/len(df_vuln_ibm_sh.x_xfe_cvss_access_vector))))+"% DE LAS VULNERABILIDADES TIENE UNA VECTOR DE ACCESO FISICO \n")
print("EL "+str(float(((count_Adjnet_vecacc_ibm_sh*100)/len(df_vuln_ibm_sh.x_xfe_cvss_access_vector))))+"% DE LAS VULNERABILIDADES TIENE UNA VECTOR DE ACCESO A TRAVES DE UNA RED ADYACENTE \n")
print("EL "+str(float(((count_none_vecacc_ibm_sh*100)/len(df_vuln_ibm_sh.x_xfe_cvss_access_vector))))+"% DE LAS VULNERABILIDADES NO TIENE VECTOR DE ACCESO ESPECIFICADO \n")
print("\n")







print("**************************ESTADÍSTICAS VECTOR DE ACCESO EN VULNERABILIDADES IBM PARTE IOT Y SMART HOME CONJUNTAS********************************")
print("\n")
print("EL VECTOR DE ACCESO EN "+str(count_network_vecacc_ibm_sh+count_network_vecacc_ibm_iot)+" VULNERABILIDADES ES A TRAVES DE LA RED \n")
print("EL VECTOR DE ACCESO EN "+str(count_Local_vecacc_ibm_sh+count_Local_vecacc_ibm_iot)+" VULNERABILIDADES ES LOCAL \n")
print("EL VECTOR DE ACCESO EN "+str(count_Physical_vecacc_ibm_sh+count_Physical_vecacc_ibm_iot)+" VULNERABILIDADES ES FISICO \n")
print("EL VECTOR DE ACCESO EN "+str(count_Adjnet_vecacc_ibm_sh+count_Adjnet_vecacc_ibm_iot)+" VULNERABILIDADES ES A TRAVES DE UNA RED ADYACENTE \n")
print("EL VECTOR DE ACCESO EN "+str(count_none_vecacc_ibm_sh+count_none_vecacc_ibm_iot)+" VULNERABILIDADES NO VIENE ESPECIFICADO \n")
print("\n")
print("**************************PORCENTAJE VECTOR DE ACCESO EN VULNERABILIDADES IBM PARTE IOT Y SMART HOME CONJUNTAS********************************")
print("\n")
print("EL "+str(float((((count_network_vecacc_ibm_sh+count_network_vecacc_ibm_iot)*100)/(len(df_vuln_ibm_sh.x_xfe_cvss_access_vector)+len(df_vuln_ibm_iot.x_xfe_cvss_access_vector)))))+"% DE LAS VULNERABILIDADES TIENE UN VECTOR DE ACCESO A TRAVES DE LA RED \n")
print("EL "+str(float((((count_Local_vecacc_ibm_sh+count_Local_vecacc_ibm_iot)*100)/(len(df_vuln_ibm_sh.x_xfe_cvss_access_vector)+len(df_vuln_ibm_iot.x_xfe_cvss_access_vector)))))+"% DE LAS VULNERABILIDADES TIENE UN VECTOR DE ACCESO LOCAL \n")
print("EL "+str(float((((count_Physical_vecacc_ibm_sh+count_Physical_vecacc_ibm_iot)*100)/(len(df_vuln_ibm_sh.x_xfe_cvss_access_vector)+len(df_vuln_ibm_iot.x_xfe_cvss_access_vector)))))+"% DE LAS VULNERABILIDADES TIENE UNA VECTOR DE ACCESO FISICO \n")
print("EL "+str(float((((count_Adjnet_vecacc_ibm_sh+count_Adjnet_vecacc_ibm_iot)*100)/(len(df_vuln_ibm_sh.x_xfe_cvss_access_vector)+len(df_vuln_ibm_iot.x_xfe_cvss_access_vector)))))+"% DE LAS VULNERABILIDADES TIENE UNA VECTOR DE ACCESO A TRAVES DE UNA RED ADYACENTE \n")
print("EL "+str(float((((count_none_vecacc_ibm_sh+count_none_vecacc_ibm_iot)*100)/(len(df_vuln_ibm_sh.x_xfe_cvss_access_vector)+len(df_vuln_ibm_iot.x_xfe_cvss_access_vector)))))+"% DE LAS VULNERABILIDADES NO TIENE VECTOR DE ACCESO ESPECIFICADO \n")
print("\n")








