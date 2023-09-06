
import pandas as pd

#Abro los ficheros con los que voy a tratar

df_vuln_ibm_iot = pd.read_excel('vulnerabilidades_ibm_iot_2023.xlsx')
df_vuln_ibm_sh=pd.read_excel('vulnerabilidades_ibm_smart_home_2023.xlsx')


#Variables donde almacenare el contador de informe de confianza para vulnerabilidades IBM 
confirmed_report_confi_iot=0
reasonable_report_confi_iot=0
confirmed_report_confi_sh=0
reasonable_report_confi_sh=0

#Compruebo EL INFORME DE CONFIANZA en vulnerabilidades IBM para IOT

for i in range(0,len(df_vuln_ibm_iot["x_xfe_report_confidence"])):
    if(df_vuln_ibm_iot["x_xfe_report_confidence"][i]=='Confirmed'):
        confirmed_report_confi_iot+=1
    else:
        reasonable_report_confi_iot+=1

print("**************************ESTADÍSTICAS CONFIANZA DEL INFORME EN VULNERABILIDADES IBM IOT********************************")
print("\n")
print("EN "+str(confirmed_report_confi_iot)+" VULNERABILIDADES EL INFORME DE CONFIANZA ESTA CONFIRMADO \n")
print("EN "+str(reasonable_report_confi_iot)+" VULNERABILIDADES EL INFORME DE CONFIANZA ES RAZONABLE \n")
print("\n")
print("***************************PORCENTAJE CONFIANZA DEL INFORME EN VULNERABILIDADES IBM IOT********************************")
print("\n")
print("EN EL "+str(float(((confirmed_report_confi_iot*100)/len(df_vuln_ibm_iot["x_xfe_report_confidence"]))))+"% DE LAS VULNERABILIDADES EL INFORME DE CONFIANZA ESTA CONFIRMADO \n")
print("EN EL "+str(float(((reasonable_report_confi_iot*100)/len(df_vuln_ibm_iot["x_xfe_report_confidence"]))))+"% DE LAS VULNERABILIDADES EL INFORME DE CONFIANZA ES RAZONABLE \n")

print("\n")







#Compruebo EL INFORME DE CONFIANZA en vulnerabilidades IBM para SMART HOME

for j in range(0,len(df_vuln_ibm_sh["x_xfe_report_confidence"])):
    if(df_vuln_ibm_sh["x_xfe_report_confidence"][j]=='Confirmed'):
        confirmed_report_confi_sh+=1
    else:
        reasonable_report_confi_sh+=1






print("**************************ESTADÍSTICAS CONFIANZA DEL INFORME EN VULNERABILIDADES IBM SMART HOME********************************")
print("\n")
print("EN "+str(confirmed_report_confi_sh)+" VULNERABILIDADES EL INFORME DE CONFIANZA ESTA CONFIRMADO \n")
print("EN "+str(reasonable_report_confi_sh)+" VULNERABILIDADES EL INFORME DE CONFIANZA ES RAZONABLE \n")
print("\n")
print("***************************PORCENTAJE CONFIANZA DEL INFORME EN VULNERABILIDADES IBM SMART HOME********************************")
print("\n")
print("EN EL "+str(float(((confirmed_report_confi_sh*100)/len(df_vuln_ibm_sh["x_xfe_report_confidence"]))))+"% DE LAS VULNERABILIDADES EL INFORME DE CONFIANZA ESTA CONFIRMADO \n")
print("EN EL "+str(float(((reasonable_report_confi_sh*100)/len(df_vuln_ibm_sh["x_xfe_report_confidence"]))))+"% DE LAS VULNERABILIDADES EL INFORME DE CONFIANZA ES RAZONABLE \n")

print("\n")






print("**************************ESTADÍSTICAS CONFIANZA DEL INFORME EN VULNERABILIDADES IBM PARTE IOT Y SMART HOME CONJUNTAS ********************************")
print("\n")
print("EN "+str(confirmed_report_confi_sh+confirmed_report_confi_iot)+" VULNERABILIDADES EL INFORME DE CONFIANZA ESTA CONFIRMADO \n")
print("EN "+str(reasonable_report_confi_sh+reasonable_report_confi_iot)+" VULNERABILIDADES EL INFORME DE CONFIANZA ES RAZONABLE \n")
print("\n")
print("***************************PORCENTAJE CONFIANZA DEL INFORME EN VULNERABILIDADES IBM PARTE IOT Y SMART HOME CONJUNTAS********************************")
print("\n")
print("EN EL "+str(float((((confirmed_report_confi_sh+confirmed_report_confi_iot)*100)/(len(df_vuln_ibm_sh["x_xfe_report_confidence"])+len(df_vuln_ibm_iot["x_xfe_report_confidence"])))))+"% DE LAS VULNERABILIDADES EL INFORME DE CONFIANZA ESTA CONFIRMADO \n")
print("EN EL "+str(float((((reasonable_report_confi_sh+reasonable_report_confi_iot)*100)/(len(df_vuln_ibm_sh["x_xfe_report_confidence"])+len(df_vuln_ibm_iot["x_xfe_report_confidence"])))))+"% DE LAS VULNERABILIDADES EL INFORME DE CONFIANZA ES RAZONABLE \n")

print("\n")

