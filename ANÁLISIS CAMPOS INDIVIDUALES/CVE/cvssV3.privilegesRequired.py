import pandas as pd


df_cve_iot=pd.read_excel('cves_iot_2023.xlsx')
df_cve_sh=pd.read_excel('cves_smart_home_2023.xlsx')



#Variables donde almacenare el contador de niveles de PRIVILEGIOS REQUERIDOS
count_high_pvgreq_cvssv3_iot=0
count_low_pvgreq_cvssv3_iot=0
count_none_pvgreq_cvssV3_iot=0

#Recorro los valores de PRIVILEGIOS REQUERIDOS y aumento los contadores segun su valor

for j in range(0,len(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.privilegesRequired"])):
    if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.privilegesRequired"][j]=='HIGH'):
        count_high_pvgreq_cvssv3_iot+=1
    elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.privilegesRequired"][j]=='LOW'):
        count_low_pvgreq_cvssv3_iot+=1
    else:
        count_none_pvgreq_cvssV3_iot+=1

print("**************************ESTADÍSTICAS PRIVILEGIOS REQUERIDOS EN CVE SEGÚN VECTOR CVSSV3 PARTE IOT********************************")
print("\n")
print("LOS PRIVILEGIOS REQUERIDOS EN "+str(count_high_pvgreq_cvssv3_iot)+" VULNERABILIDADES SON ALTOS \n")
print("LOS PRIVILEGIOS REQUERIDOS EN "+str(count_low_pvgreq_cvssv3_iot)+" VULNERABILIDADES SON BAJOS \n")
print("EN "+str(count_none_pvgreq_cvssV3_iot)+" VULNERABILIDADES NO SE REQUIEREN PRIVILEGIOS \n")
print("\n")
print("**************************PORCENTAJE PRIVILEGIOS REQUERIDOS EN CVE SEGÚN VECTOR CVSSV3 PARTE IOT********************************")
print("\n")
print("EL "+str(float(((count_high_pvgreq_cvssv3_iot*100)/len(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.privilegesRequired"]))))+"% DE LAS VULNERABILIDADES TIENE UN ALTO NIVEL DE PRIVILEGIOS REQUERIDOS \n")
print("EL "+str(float(((count_low_pvgreq_cvssv3_iot*100)/len(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.privilegesRequired"]))))+"% DE LAS VULNERABILIDADES TIENE UN BAJO NIVEL DE PRIVILEGIOS REQUERIDOS \n")
print("EL "+str(float(((count_none_pvgreq_cvssV3_iot*100)/len(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.privilegesRequired"]))))+"% DE LAS VULNERABILIDADES NO REQUIERE UN NIVEL DE PRIVILEGIOS \n")
print("\n")



#Variables donde almacenare el contador de niveles de PRIVILEGIOS REQUERIDOS
count_high_pvgreq_cvssv3_sh=0
count_low_pvgreq_cvssv3_sh=0
count_none_pvgreq_cvssV3_sh=0

#Recorro los valores de PRIVILEGIOS REQUERIDOS y aumento los contadores segun su valor

for r in range(0,len(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.privilegesRequired"])):
    if(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.privilegesRequired"][r]=='HIGH'):
        count_high_pvgreq_cvssv3_sh+=1
    elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.privilegesRequired"][r]=='LOW'):
        count_low_pvgreq_cvssv3_sh+=1
    elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.privilegesRequired"][r]=='MEDIUM'):
        count_medium_pvgreq_cvssv3_sh+=1
    else:
        count_none_pvgreq_cvssV3_sh+=1

print("**************************ESTADÍSTICAS PRIVILEGIOS REQUERIDOS EN CVE SEGÚN VECTOR CVSSV3 PARTE SMART HOME********************************")
print("\n")
print("LOS PRIVILEGIOS REQUERIDOS EN "+str(count_high_pvgreq_cvssv3_sh)+" VULNERABILIDADES SON ALTOS \n")
print("LOS PRIVILEGIOS REQUERIDOS EN "+str(count_low_pvgreq_cvssv3_sh)+" VULNERABILIDADES SON BAJOS \n")
print("EN "+str(count_none_pvgreq_cvssV3_sh)+" VULNERABILIDADES NO SE REQUIEREN PRIVILEGIOS \n")
print("\n")
print("**************************PORCENTAJE PRIVILEGIOS REQUERIDOS EN CVE SEGÚN VECTOR CVSSV3 PARTE SMART HOME********************************")
print("\n")
print("EL "+str(float(((count_high_pvgreq_cvssv3_sh*100)/len(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.privilegesRequired"]))))+"% DE LAS VULNERABILIDADES TIENE UN ALTO NIVEL DE PRIVILEGIOS REQUERIDOS \n")
print("EL "+str(float(((count_low_pvgreq_cvssv3_sh*100)/len(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.privilegesRequired"]))))+"% DE LAS VULNERABILIDADES TIENE UN BAJO NIVEL DE PRIVILEGIOS REQUERIDOS \n")
print("EL "+str(float(((count_none_pvgreq_cvssV3_sh*100)/len(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.privilegesRequired"]))))+"% DE LAS VULNERABILIDADES NO REQUIERE UN NIVEL DE PRIVILEGIOS \n")
print("\n")







print("**************************PRIVILEGIOS REQUERIDOS EN CVE SEGÚN VECTOR CVSSV3 PARTE IOT Y SMART HOME CONJUNTAS********************************")
print("\n")
print("LOS PRIVILEGIOS REQUERIDOS EN "+str(count_high_pvgreq_cvssv3_sh+count_high_pvgreq_cvssv3_iot)+" VULNERABILIDADES SON ALTOS \n")
print("LOS PRIVILEGIOS REQUERIDOS EN "+str(count_low_pvgreq_cvssv3_sh+count_low_pvgreq_cvssv3_iot)+" VULNERABILIDADES SON BAJOS \n")
print("EN "+str(count_none_pvgreq_cvssV3_sh+count_none_pvgreq_cvssV3_iot)+" VULNERABILIDADES NO SE REQUIEREN PRIVILEGIOS \n")
print("\n")
print("**************************PORCENTAJE PRIVILEGIOS REQUERIDOS EN CVE SEGÚN VECTOR CVSSV3 PARTE IOT Y SMART HOME CONJUNTAS********************************")
print("\n")
print("EL "+str(float((((count_high_pvgreq_cvssv3_sh+count_high_pvgreq_cvssv3_iot)*100)/(len(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.privilegesRequired"])+len(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.privilegesRequired"])))))+"% DE LAS VULNERABILIDADES TIENE UN ALTO NIVEL DE PRIVILEGIOS REQUERIDOS \n")
print("EL "+str(float((((count_low_pvgreq_cvssv3_sh+count_low_pvgreq_cvssv3_iot)*100)/(len(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.privilegesRequired"])+len(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.privilegesRequired"])))))+"% DE LAS VULNERABILIDADES TIENE UN BAJO NIVEL DE PRIVILEGIOS REQUERIDOS \n")
print("EL "+str(float((((count_none_pvgreq_cvssV3_sh+count_none_pvgreq_cvssV3_iot)*100)/(len(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.privilegesRequired"])+len(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.privilegesRequired"])))))+"% DE LAS VULNERABILIDADES NO REQUIERE UN NIVEL DE PRIVILEGIOS \n")
print("\n")






