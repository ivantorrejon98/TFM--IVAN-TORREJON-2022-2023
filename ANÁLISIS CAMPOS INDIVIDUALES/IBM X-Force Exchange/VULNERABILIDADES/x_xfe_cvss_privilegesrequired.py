
import pandas as pd

#Abro los ficheros con los que voy a tratar

df_vuln_ibm_iot = pd.read_excel('vulnerabilidades_ibm_iot_2023.xlsx')
df_vuln_ibm_sh=pd.read_excel('vulnerabilidades_ibm_smart_home_2023.xlsx')


#Variables donde almacenare el contador de niveles de PRIVILEGIOS REQUERIDOS
count_high_pvgreq_ibm_iot=0
count_low_pvgreq_ibm_iot=0
count_none_pvgreq_ibm_iot=0

#Recorro los valores de PRIVILEGIOS REQUERIDOS y aumento los contadores segun su valor

for i in range(0,len(df_vuln_ibm_iot.x_xfe_cvss_privilegesrequired)):
    if(df_vuln_ibm_iot.x_xfe_cvss_privilegesrequired[i]=='High'):
        count_high_pvgreq_ibm_iot+=1
    elif(df_vuln_ibm_iot.x_xfe_cvss_privilegesrequired[i]=='Low'):
        count_low_pvgreq_ibm_iot+=1
    else:
        count_none_pvgreq_ibm_iot+=1
    

print("**************************ESTADÍSTICAS PRIVILEGIOS REQUERIDOS EN VULNERABILIDADES IBM PARTE IOT********************************")
print("\n")
print("LOS PRIVILEGIOS REQUERIDOS EN "+str(count_high_pvgreq_ibm_iot)+" VULNERABILIDADES SON ALTOS \n")
print("LOS PRIVILEGIOS REQUERIDOS EN "+str(count_low_pvgreq_ibm_iot)+" VULNERABILIDADES SON BAJOS \n")
print("EN "+str(count_none_pvgreq_ibm_iot)+" VULNERABILIDADES NO SE REQUIEREN PRIVILEGIOS ESPECIFICOS \n")
print("\n")
print("**************************PORCENTAJE PRIVILEGIOS REQUERIDOS EN VULNERABILIDADES IBM PARTE IOT********************************")
print("\n")
print("EL "+str(float(((count_high_pvgreq_ibm_iot*100)/len(df_vuln_ibm_iot.x_xfe_cvss_privilegesrequired))))+"% DE LAS VULNERABILIDADES TIENE UN ALTO NIVEL DE PRIVILEGIOS REQUERIDOS \n")
print("EL "+str(float(((count_low_pvgreq_ibm_iot*100)/len(df_vuln_ibm_iot.x_xfe_cvss_privilegesrequired))))+"% DE LAS VULNERABILIDADES TIENE UN BAJO NIVEL DE  PRIVILEGIOS REQUERIDOS \n")
print("EL "+str(float(((count_none_pvgreq_ibm_iot*100)/len(df_vuln_ibm_iot.x_xfe_cvss_privilegesrequired))))+"% DE LAS VULNERABILIDADES NO REQUIERE NIVEL DE PRIVILEGIOS ESPECIFICO \n")
print("\n")


#Variables donde almacenare el contador de niveles de PRIVILEGIOS REQUERIDOS
count_high_pvgreq_ibm_sh=0
count_low_pvgreq_ibm_sh=0
count_none_pvgreq_ibm_sh=0

#Recorro los valores de PRIVILEGIOS REQUERIDOS y aumento los contadores segun su valor

for l in range(0,len(df_vuln_ibm_sh.x_xfe_cvss_privilegesrequired)):
    if(df_vuln_ibm_sh.x_xfe_cvss_privilegesrequired[l]=='High'):
        count_high_pvgreq_ibm_sh+=1
    elif(df_vuln_ibm_sh.x_xfe_cvss_privilegesrequired[l]=='Low'):
        count_low_pvgreq_ibm_sh+=1
    else:
        count_none_pvgreq_ibm_sh+=1
    

print("**************************PRIVILEGIOS REQUERIDOS EN VULNERABILIDADES IBM PARTE SMART HOME********************************")
print("\n")
print("LOS PRIVILEGIOS REQUERIDOS EN "+str(count_high_pvgreq_ibm_sh)+" VULNERABILIDADES SON ALTOS \n")
print("LOS PRIVILEGIOS REQUERIDOS EN "+str(count_low_pvgreq_ibm_sh)+" VULNERABILIDADES SON BAJOS \n")
print("EN "+str(count_none_pvgreq_ibm_sh)+" VULNERABILIDADES NO SE REQUIEREN PRIVILEGIOS ESPECIFICOS \n")
print("\n")
print("**************************PORCENTAJE PRIVILEGIOS REQUERIDOS EN VULNERABILIDADES IBM PARTE SMART HOME********************************")
print("\n")
print("EL "+str(float(((count_high_pvgreq_ibm_sh*100)/len(df_vuln_ibm_sh.x_xfe_cvss_privilegesrequired))))+"% DE LAS VULNERABILIDADES TIENE UN ALTO NIVEL DE PRIVILEGIOS REQUERIDOS \n")
print("EL "+str(float(((count_low_pvgreq_ibm_sh*100)/len(df_vuln_ibm_sh.x_xfe_cvss_privilegesrequired))))+"% DE LAS VULNERABILIDADES TIENE UN BAJO NIVEL DE  PRIVILEGIOS REQUERIDOS \n")
print("EL "+str(float(((count_none_pvgreq_ibm_sh*100)/len(df_vuln_ibm_sh.x_xfe_cvss_privilegesrequired))))+"% DE LAS VULNERABILIDADES NO REQUIERE NIVEL DE PRIVILEGIOS ESPECIFICO \n")
print("\n")





print("**************************ESTADÍSTICAS PRIVILEGIOS REQUERIDOS EN VULNERABILIDADES IBM PARTE IOT Y SMART HOME CONJUNTAS*******************************")
print("\n")
print("LOS PRIVILEGIOS REQUERIDOS EN "+str(count_high_pvgreq_ibm_sh+count_high_pvgreq_ibm_iot)+" VULNERABILIDADES SON ALTOS \n")
print("LOS PRIVILEGIOS REQUERIDOS EN "+str(count_low_pvgreq_ibm_sh+count_low_pvgreq_ibm_iot)+" VULNERABILIDADES SON BAJOS \n")
print("EN "+str(count_none_pvgreq_ibm_sh+count_none_pvgreq_ibm_iot)+" VULNERABILIDADES NO SE REQUIEREN PRIVILEGIOS ESPECIFICOS \n")
print("\n")
print("**************************PORCENTAJE PRIVILEGIOS REQUERIDOS EN VULNERABILIDADES IBM PARTE IOT Y SMART HOME CONJUNTAS********************************")
print("\n")

print("EL "+str(float((((count_high_pvgreq_ibm_sh+count_high_pvgreq_ibm_iot)*100)/(len(df_vuln_ibm_sh.x_xfe_cvss_privilegesrequired)+len(df_vuln_ibm_iot.x_xfe_cvss_privilegesrequired)))))+"% DE LAS VULNERABILIDADES TIENE UN ALTO NIVEL DE PRIVILEGIOS REQUERIDOS \n")
print("EL "+str(float((((count_low_pvgreq_ibm_sh+count_low_pvgreq_ibm_iot)*100)/(len(df_vuln_ibm_sh.x_xfe_cvss_privilegesrequired)+len(df_vuln_ibm_iot.x_xfe_cvss_privilegesrequired)))))+"% DE LAS VULNERABILIDADES TIENE UN BAJO NIVEL DE  PRIVILEGIOS REQUERIDOS \n")
print("EL "+str(float((((count_none_pvgreq_ibm_sh+count_none_pvgreq_ibm_iot)*100)/(len(df_vuln_ibm_sh.x_xfe_cvss_privilegesrequired)+len(df_vuln_ibm_iot.x_xfe_cvss_privilegesrequired)))))+"% DE LAS VULNERABILIDADES NO REQUIERE NIVEL DE PRIVILEGIOS ESPECIFICO \n")
print("\n")




