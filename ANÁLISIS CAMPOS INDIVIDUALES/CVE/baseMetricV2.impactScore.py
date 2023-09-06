
import pandas as pd

#Abro los ficheros con los que voy a tratar


df_cve_iot=pd.read_excel('cves_iot_2023.xlsx')
df_cve_sh=pd.read_excel('cves_smart_home_2023.xlsx')



#Variables donde almacenare el contador de puntuacion de impacto CVE CVSS3 para IOT

CV2_IMPACT_score_9_iot=0
CV2_IMPACT_score_8_iot=0
CV2_IMPACT_score_7_iot=0
CV2_IMPACT_score_6_iot=0
CV2_IMPACT_score_5_iot=0
CV2_IMPACT_score_4_iot=0
CV2_IMPACT_score_3_iot=0
CV2_IMPACT_score_2_iot=0
CV2_IMPACT_score_1_iot=0
CV2_IMPACT_score_0_iot=0
CV2_IMPACT_score_10_iot=0
CV2_no_IMPACT_score_iot=0

#Compruebo LA PUNTUACION DE IMPACTO CVE CVSS3 para IOT

for j in range(0,len(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"])):
    if(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"][j] =='NONE'):
        CV2_no_IMPACT_score_iot+=1
    elif(((float(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"][j])) < 10.0) and ((float(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"][j])) >=9.0)):
        CV2_IMPACT_score_9_iot+=1
    elif(((float(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"][j])) < 9.0) and ((float(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"][j])) >=8.0)):
        CV2_IMPACT_score_8_iot+=1
    elif(((float(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"][j])) < 8.0) and ((float(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"][j])) >=7.0)):
        CV2_IMPACT_score_7_iot+=1
    elif(((float(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"][j])) < 7.0) and ((float(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"][j])) >=6.0)):
        CV2_IMPACT_score_6_iot+=1
    elif(((float(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"][j])) < 6.0) and ((float(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"][j])) >=5.0)):
        CV2_IMPACT_score_5_iot+=1
    elif(((float(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"][j])) < 5.0) and ((float(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"][j])) >=4.0)):
        CV2_IMPACT_score_4_iot+=1
    elif(((float(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"][j])) < 4.0) and ((float(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"][j])) >=3.0)):
        CV2_IMPACT_score_3_iot+=1
    elif(((float(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"][j])) < 3.0) and ((float(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"][j])) >=2.0)):
        CV2_IMPACT_score_2_iot+=1
    elif(((float(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"][j])) < 2.0) and ((float(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"][j])) >=1.0)):
        CV2_IMPACT_score_1_iot+=1
    elif(((float(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"][j])) < 1.0) and ((float(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"][j])) >=0.0)):
        CV2_IMPACT_score_0_iot+=1
    elif(((float(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"][j])) == 10.0)):
        CV2_IMPACT_score_10_iot+=1
    
print("***************************ESTADÍSTICAS PUNTUACIÓN DE IMPACTO EN CVE SEGÚN VECTOR CVSSV2 PARTE IOT********************************")
print("\n")
print("EN "+str(CV2_IMPACT_score_10_iot)+" VULNERABILIDADES LA PUNTUACION DE IMPACTO ES 10 \n")
print("EN "+str(CV2_IMPACT_score_9_iot)+" VULNERABILIDADES LA PUNTUACION DE IMPACTO ES MAYOR O IGUAL QUE 9 \n")
print("EN "+str(CV2_IMPACT_score_8_iot)+" VULNERABILIDADES LA PUNTUACION DE IMPACTO ES MAYOR O IGUAL QUE 8 \n")
print("EN "+str(CV2_IMPACT_score_7_iot)+" VULNERABILIDADES LA PUNTUACION DE IMPACTO ES MAYOR O IGUAL QUE 7 \n")
print("EN "+str(CV2_IMPACT_score_6_iot)+" VULNERABILIDADES LA PUNTUACION DE IMPACTO ES MAYOR O IGUAL QUE 6 \n")
print("EN "+str(CV2_IMPACT_score_5_iot)+" VULNERABILIDADES LA PUNTUACION DE IMPACTO ES MAYOR O IGUAL QUE 5 \n")
print("EN "+str(CV2_IMPACT_score_4_iot)+" VULNERABILIDADES LA PUNTUACION DE IMPACTO ES MAYOR O IGUAL QUE 4 \n")
print("EN "+str(CV2_IMPACT_score_3_iot)+" VULNERABILIDADES LA PUNTUACION DE IMPACTO ES MAYOR O IGUAL QUE 3 \n")
print("EN "+str(CV2_IMPACT_score_2_iot)+" VULNERABILIDADES LA PUNTUACION DE IMPACTO ES MAYOR O IGUAL QUE 2 \n")
print("EN "+str(CV2_IMPACT_score_1_iot)+" VULNERABILIDADES LA PUNTUACION DE IMPACTO ES MAYOR O IGUAL QUE 1 \n")
print("EN "+str(CV2_IMPACT_score_0_iot)+" VULNERABILIDADES LA PUNTUACION DE IMPACTO ES MAYOR O IGUAL QUE 0 \n")
print("EN "+str(CV2_no_IMPACT_score_iot)+" VULNERABILIDADES LA PUNTUACION DE IMPACTO NO VIENE ESPECIFICADA \n")
print("\n")
print("***************************PORCENTAJE PUNTUACIÓN DE IMPACTO EN CVE SEGÚN VECTOR CVSSV2 PARTE IOT********************************")
print("\n")
print("EN EL "+str(float(((CV2_IMPACT_score_10_iot*100)/len(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"]))))+"% DE LAS VULNERABILIDADES LA PUNTUACION DE IMPACTO ES 10 \n")
print("EN EL "+str(float(((CV2_IMPACT_score_9_iot*100)/len(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"]))))+"% DE LAS VULNERABILIDADES LA PUNTUACION DE IMPACTO ES MAYOR O IGUAL QUE 9 \n")
print("EN EL "+str(float(((CV2_IMPACT_score_8_iot*100)/len(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"]))))+"% DE LAS VULNERABILIDADES LA PUNTUACION DE IMPACTO ES MAYOR O IGUAL QUE 8 \n")
print("EN EL "+str(float(((CV2_IMPACT_score_7_iot*100)/len(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"]))))+"% DE LAS VULNERABILIDADES LA PUNTUACION DE IMPACTO ES MAYOR O IGUAL QUE 7 \n")
print("EN EL "+str(float(((CV2_IMPACT_score_6_iot*100)/len(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"]))))+"% DE LAS VULNERABILIDADES LA PUNTUACION DE IMPACTO ES MAYOR O IGUAL QUE 6 \n")
print("EN EL "+str(float(((CV2_IMPACT_score_5_iot*100)/len(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"]))))+"% DE LAS VULNERABILIDADES LA PUNTUACION DE IMPACTO ES MAYOR O IGUAL QUE 5 \n")
print("EN EL "+str(float(((CV2_IMPACT_score_4_iot*100)/len(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"]))))+"% DE LAS VULNERABILIDADES LA PUNTUACION DE IMPACTO ES MAYOR O IGUAL QUE 4 \n")
print("EN EL "+str(float(((CV2_IMPACT_score_3_iot*100)/len(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"]))))+"% DE LAS VULNERABILIDADES LA PUNTUACION DE IMPACTO ES MAYOR O IGUAL QUE 3 \n")
print("EN EL "+str(float(((CV2_IMPACT_score_2_iot*100)/len(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"]))))+"% DE LAS VULNERABILIDADES LA PUNTUACION DE IMPACTO ES MAYOR O IGUAL QUE 2 \n")
print("EN EL "+str(float(((CV2_IMPACT_score_1_iot*100)/len(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"]))))+"% DE LAS VULNERABILIDADES LA PUNTUACION DE IMPACTO ES MAYOR O IGUAL QUE 1 \n")
print("EN EL "+str(float(((CV2_IMPACT_score_0_iot*100)/len(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"]))))+"% DE LAS VULNERABILIDADES LA PUNTUACION DE IMPACTO ES MAYOR O IGUAL QUE 0 \n")
print("EN EL "+str(float(((CV2_no_IMPACT_score_iot*100)/len(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"]))))+"% DE LAS VULNERABILIDADES LA PUNTUACION DE IMPACTO NO VIENE ESPECIFICADA \n")
print("\n")








#Variables donde almacenare el contador de puntuacion de impacto CVE CVSS3 para SMART HOME

CV2_IMPACT_score_9_sh=0
CV2_IMPACT_score_8_sh=0
CV2_IMPACT_score_7_sh=0
CV2_IMPACT_score_6_sh=0
CV2_IMPACT_score_5_sh=0
CV2_IMPACT_score_4_sh=0
CV2_IMPACT_score_3_sh=0
CV2_IMPACT_score_2_sh=0
CV2_IMPACT_score_1_sh=0
CV2_IMPACT_score_0_sh=0
CV2_IMPACT_score_10_sh=0
CV2_no_IMPACT_score_sh=0

#Compruebo LA PUNTUACION DE IMPACTO CVE CVSS3 para SMART HOME

for j in range(0,len(df_cve_sh["CVE_Items.impact.baseMetricV2.impactScore"])):
    if(df_cve_sh["CVE_Items.impact.baseMetricV2.impactScore"][j] =='NONE'):
        CV2_no_IMPACT_score_sh+=1
    elif(((float(df_cve_sh["CVE_Items.impact.baseMetricV2.impactScore"][j])) < 10.0) and ((float(df_cve_sh["CVE_Items.impact.baseMetricV2.impactScore"][j])) >=9.0)):
        CV2_IMPACT_score_9_sh+=1
    elif(((float(df_cve_sh["CVE_Items.impact.baseMetricV2.impactScore"][j])) < 9.0) and ((float(df_cve_sh["CVE_Items.impact.baseMetricV2.impactScore"][j])) >=8.0)):
        CV2_IMPACT_score_8_sh+=1
    elif(((float(df_cve_sh["CVE_Items.impact.baseMetricV2.impactScore"][j])) < 8.0) and ((float(df_cve_sh["CVE_Items.impact.baseMetricV2.impactScore"][j])) >=7.0)):
        CV2_IMPACT_score_7_sh+=1
    elif(((float(df_cve_sh["CVE_Items.impact.baseMetricV2.impactScore"][j])) < 7.0) and ((float(df_cve_sh["CVE_Items.impact.baseMetricV2.impactScore"][j])) >=6.0)):
        CV2_IMPACT_score_6_sh+=1
    elif(((float(df_cve_sh["CVE_Items.impact.baseMetricV2.impactScore"][j])) < 6.0) and ((float(df_cve_sh["CVE_Items.impact.baseMetricV2.impactScore"][j])) >=5.0)):
        CV2_IMPACT_score_5_sh+=1
    elif(((float(df_cve_sh["CVE_Items.impact.baseMetricV2.impactScore"][j])) < 5.0) and ((float(df_cve_sh["CVE_Items.impact.baseMetricV2.impactScore"][j])) >=4.0)):
        CV2_IMPACT_score_4_sh+=1
    elif(((float(df_cve_sh["CVE_Items.impact.baseMetricV2.impactScore"][j])) < 4.0) and ((float(df_cve_sh["CVE_Items.impact.baseMetricV2.impactScore"][j])) >=3.0)):
        CV2_IMPACT_score_3_sh+=1
    elif(((float(df_cve_sh["CVE_Items.impact.baseMetricV2.impactScore"][j])) < 3.0) and ((float(df_cve_sh["CVE_Items.impact.baseMetricV2.impactScore"][j])) >=2.0)):
        CV2_IMPACT_score_2_sh+=1
    elif(((float(df_cve_sh["CVE_Items.impact.baseMetricV2.impactScore"][j])) < 2.0) and ((float(df_cve_sh["CVE_Items.impact.baseMetricV2.impactScore"][j])) >=1.0)):
        CV2_IMPACT_score_1_sh+=1
    elif(((float(df_cve_sh["CVE_Items.impact.baseMetricV2.impactScore"][j])) < 1.0) and ((float(df_cve_sh["CVE_Items.impact.baseMetricV2.impactScore"][j])) >=0.0)):
        CV2_IMPACT_score_0_sh+=1
    elif(((float(df_cve_sh["CVE_Items.impact.baseMetricV2.impactScore"][j])) == 10.0)):
        CV2_IMPACT_score_10_sh+=1
    
print("***************************ESTADÍSTICAS PUNTUACIÓN DE IMPACTO EN CVE SEGÚN VECTOR CVSSV2 PARTE SMART HOME ********************************")
print("\n")
print("EN "+str(CV2_IMPACT_score_10_sh)+" VULNERABILIDADES LA PUNTUACION DE IMPACTO ES 10 \n")
print("EN "+str(CV2_IMPACT_score_9_sh)+" VULNERABILIDADES LA PUNTUACION DE IMPACTO ES MAYOR O IGUAL QUE 9 \n")
print("EN "+str(CV2_IMPACT_score_8_sh)+" VULNERABILIDADES LA PUNTUACION DE IMPACTO ES MAYOR O IGUAL QUE 8 \n")
print("EN "+str(CV2_IMPACT_score_7_sh)+" VULNERABILIDADES LA PUNTUACION DE IMPACTO ES MAYOR O IGUAL QUE 7 \n")
print("EN "+str(CV2_IMPACT_score_6_sh)+" VULNERABILIDADES LA PUNTUACION DE IMPACTO ES MAYOR O IGUAL QUE 6 \n")
print("EN "+str(CV2_IMPACT_score_5_sh)+" VULNERABILIDADES LA PUNTUACION DE IMPACTO ES MAYOR O IGUAL QUE 5 \n")
print("EN "+str(CV2_IMPACT_score_4_sh)+" VULNERABILIDADES LA PUNTUACION DE IMPACTO ES MAYOR O IGUAL QUE 4 \n")
print("EN "+str(CV2_IMPACT_score_3_sh)+" VULNERABILIDADES LA PUNTUACION DE IMPACTO ES MAYOR O IGUAL QUE 3 \n")
print("EN "+str(CV2_IMPACT_score_2_sh)+" VULNERABILIDADES LA PUNTUACION DE IMPACTO ES MAYOR O IGUAL QUE 2 \n")
print("EN "+str(CV2_IMPACT_score_1_sh)+" VULNERABILIDADES LA PUNTUACION DE IMPACTO ES MAYOR O IGUAL QUE 1 \n")
print("EN "+str(CV2_IMPACT_score_0_sh)+" VULNERABILIDADES LA PUNTUACION DE IMPACTO ES MAYOR O IGUAL QUE 0 \n")
print("EN "+str(CV2_no_IMPACT_score_sh)+" VULNERABILIDADES LA PUNTUACION DE IMPACTO NO VIENE ESPECIFICADA \n")
print("\n")
print("***************************PORCENTAJE PUNTUACIÓN DE IMPACTO EN CVE SEGÚN VECTOR CVSSV2 PARTE SMART HOME********************************")
print("\n")
print("EN EL "+str(float(((CV2_IMPACT_score_10_sh*100)/len(df_cve_sh["CVE_Items.impact.baseMetricV2.impactScore"]))))+"% DE LAS VULNERABILIDADES LA PUNTUACION DE IMPACTO ES 10 \n")
print("EN EL "+str(float(((CV2_IMPACT_score_9_sh*100)/len(df_cve_sh["CVE_Items.impact.baseMetricV2.impactScore"]))))+"% DE LAS VULNERABILIDADES LA PUNTUACION DE IMPACTO ES MAYOR O IGUAL QUE 9 \n")
print("EN EL "+str(float(((CV2_IMPACT_score_8_sh*100)/len(df_cve_sh["CVE_Items.impact.baseMetricV2.impactScore"]))))+"% DE LAS VULNERABILIDADES LA PUNTUACION DE IMPACTO ES MAYOR O IGUAL QUE 8 \n")
print("EN EL "+str(float(((CV2_IMPACT_score_7_sh*100)/len(df_cve_sh["CVE_Items.impact.baseMetricV2.impactScore"]))))+"% DE LAS VULNERABILIDADES LA PUNTUACION DE IMPACTO ES MAYOR O IGUAL QUE 7 \n")
print("EN EL "+str(float(((CV2_IMPACT_score_6_sh*100)/len(df_cve_sh["CVE_Items.impact.baseMetricV2.impactScore"]))))+"% DE LAS VULNERABILIDADES LA PUNTUACION DE IMPACTO ES MAYOR O IGUAL QUE 6 \n")
print("EN EL "+str(float(((CV2_IMPACT_score_5_sh*100)/len(df_cve_sh["CVE_Items.impact.baseMetricV2.impactScore"]))))+"% DE LAS VULNERABILIDADES LA PUNTUACION DE IMPACTO ES MAYOR O IGUAL QUE 5 \n")
print("EN EL "+str(float(((CV2_IMPACT_score_4_sh*100)/len(df_cve_sh["CVE_Items.impact.baseMetricV2.impactScore"]))))+"% DE LAS VULNERABILIDADES LA PUNTUACION DE IMPACTO ES MAYOR O IGUAL QUE 4 \n")
print("EN EL "+str(float(((CV2_IMPACT_score_3_sh*100)/len(df_cve_sh["CVE_Items.impact.baseMetricV2.impactScore"]))))+"% DE LAS VULNERABILIDADES LA PUNTUACION DE IMPACTO ES MAYOR O IGUAL QUE 3 \n")
print("EN EL "+str(float(((CV2_IMPACT_score_2_sh*100)/len(df_cve_sh["CVE_Items.impact.baseMetricV2.impactScore"]))))+"% DE LAS VULNERABILIDADES LA PUNTUACION DE IMPACTO ES MAYOR O IGUAL QUE 2 \n")
print("EN EL "+str(float(((CV2_IMPACT_score_1_sh*100)/len(df_cve_sh["CVE_Items.impact.baseMetricV2.impactScore"]))))+"% DE LAS VULNERABILIDADES LA PUNTUACION DE IMPACTO ES MAYOR O IGUAL QUE 1 \n")
print("EN EL "+str(float(((CV2_IMPACT_score_0_sh*100)/len(df_cve_sh["CVE_Items.impact.baseMetricV2.impactScore"]))))+"% DE LAS VULNERABILIDADES LA PUNTUACION DE IMPACTO ES MAYOR O IGUAL QUE 0 \n")
print("EN EL "+str(float(((CV2_no_IMPACT_score_sh*100)/len(df_cve_sh["CVE_Items.impact.baseMetricV2.impactScore"]))))+"% DE LAS VULNERABILIDADES LA PUNTUACION DE IMPACTO NO VIENE ESPECIFICADA \n")
print("\n")







print("***************************ESTADÍSTICAS PUNTUACIÓN DE IMPACTO EN CVE SEGÚN VECTOR CVSSV2 PARTE IOT Y SMART HOME CONJUNTAS********************************")
print("\n")
print("EN "+str(CV2_IMPACT_score_10_sh+CV2_IMPACT_score_10_iot)+" VULNERABILIDADES LA PUNTUACION DE IMPACTO ES 10 \n")
print("EN "+str(CV2_IMPACT_score_9_sh+CV2_IMPACT_score_9_iot)+" VULNERABILIDADES LA PUNTUACION DE IMPACTO ES MAYOR O IGUAL QUE 9 \n")
print("EN "+str(CV2_IMPACT_score_8_sh+CV2_IMPACT_score_8_iot)+" VULNERABILIDADES LA PUNTUACION DE IMPACTO ES MAYOR O IGUAL QUE 8 \n")
print("EN "+str(CV2_IMPACT_score_7_sh+CV2_IMPACT_score_7_iot)+" VULNERABILIDADES LA PUNTUACION DE IMPACTO ES MAYOR O IGUAL QUE 7 \n")
print("EN "+str(CV2_IMPACT_score_6_sh+CV2_IMPACT_score_6_iot)+" VULNERABILIDADES LA PUNTUACION DE IMPACTO ES MAYOR O IGUAL QUE 6 \n")
print("EN "+str(CV2_IMPACT_score_5_sh+CV2_IMPACT_score_5_iot)+" VULNERABILIDADES LA PUNTUACION DE IMPACTO ES MAYOR O IGUAL QUE 5 \n")
print("EN "+str(CV2_IMPACT_score_4_sh+CV2_IMPACT_score_4_iot)+" VULNERABILIDADES LA PUNTUACION DE IMPACTO ES MAYOR O IGUAL QUE 4 \n")
print("EN "+str(CV2_IMPACT_score_3_sh+CV2_IMPACT_score_3_iot)+" VULNERABILIDADES LA PUNTUACION DE IMPACTO ES MAYOR O IGUAL QUE 3 \n")
print("EN "+str(CV2_IMPACT_score_2_sh+CV2_IMPACT_score_2_iot)+" VULNERABILIDADES LA PUNTUACION DE IMPACTO ES MAYOR O IGUAL QUE 2 \n")
print("EN "+str(CV2_IMPACT_score_1_sh+CV2_IMPACT_score_1_iot)+" VULNERABILIDADES LA PUNTUACION DE IMPACTO ES MAYOR O IGUAL QUE 1 \n")
print("EN "+str(CV2_IMPACT_score_0_sh+CV2_IMPACT_score_0_iot)+" VULNERABILIDADES LA PUNTUACION DE IMPACTO ES MAYOR O IGUAL QUE 0 \n")
print("EN "+str(CV2_no_IMPACT_score_sh+CV2_no_IMPACT_score_iot)+" VULNERABILIDADES LA PUNTUACION DE IMPACTO NO VIENE ESPECIFICADA \n")
print("\n")
print("***************************PORCENTAJE PUNTUACIÓN DE IMPACTO EN CVE SEGÚN VECTOR CVSSV2 PARTE IOT Y SMART HOME CONJUNTAS********************************")
print("\n")
print("EN EL "+str(float((((CV2_IMPACT_score_10_sh+CV2_IMPACT_score_10_iot)*100)/(len(df_cve_sh["CVE_Items.impact.baseMetricV2.impactScore"])+len(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"])))))+"% DE LAS VULNERABILIDADES LA PUNTUACION DE IMPACTO ES 10 \n")
print("EN EL "+str(float((((CV2_IMPACT_score_9_sh+CV2_IMPACT_score_9_iot)*100)/(len(df_cve_sh["CVE_Items.impact.baseMetricV2.impactScore"])+len(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"])))))+"% DE LAS VULNERABILIDADES LA PUNTUACION DE IMPACTO ES MAYOR O IGUAL QUE 9 \n")
print("EN EL "+str(float((((CV2_IMPACT_score_8_sh+CV2_IMPACT_score_8_iot)*100)/(len(df_cve_sh["CVE_Items.impact.baseMetricV2.impactScore"])+len(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"])))))+"% DE LAS VULNERABILIDADES LA PUNTUACION DE IMPACTO ES MAYOR O IGUAL QUE 8 \n")
print("EN EL "+str(float((((CV2_IMPACT_score_7_sh+CV2_IMPACT_score_7_iot)*100)/(len(df_cve_sh["CVE_Items.impact.baseMetricV2.impactScore"])+len(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"])))))+"% DE LAS VULNERABILIDADES LA PUNTUACION DE IMPACTO ES MAYOR O IGUAL QUE 7 \n")
print("EN EL "+str(float((((CV2_IMPACT_score_6_sh+CV2_IMPACT_score_6_iot)*100)/(len(df_cve_sh["CVE_Items.impact.baseMetricV2.impactScore"])+len(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"])))))+"% DE LAS VULNERABILIDADES LA PUNTUACION DE IMPACTO ES MAYOR O IGUAL QUE 6 \n")
print("EN EL "+str(float((((CV2_IMPACT_score_5_sh+CV2_IMPACT_score_5_iot)*100)/(len(df_cve_sh["CVE_Items.impact.baseMetricV2.impactScore"])+len(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"])))))+"% DE LAS VULNERABILIDADES LA PUNTUACION DE IMPACTO ES MAYOR O IGUAL QUE 5 \n")
print("EN EL "+str(float((((CV2_IMPACT_score_4_sh+CV2_IMPACT_score_4_iot)*100)/(len(df_cve_sh["CVE_Items.impact.baseMetricV2.impactScore"])+len(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"])))))+"% DE LAS VULNERABILIDADES LA PUNTUACION DE IMPACTO ES MAYOR O IGUAL QUE 4 \n")
print("EN EL "+str(float((((CV2_IMPACT_score_3_sh+CV2_IMPACT_score_3_iot)*100)/(len(df_cve_sh["CVE_Items.impact.baseMetricV2.impactScore"])+len(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"])))))+"% DE LAS VULNERABILIDADES LA PUNTUACION DE IMPACTO ES MAYOR O IGUAL QUE 3 \n")
print("EN EL "+str(float((((CV2_IMPACT_score_2_sh+CV2_IMPACT_score_2_iot)*100)/(len(df_cve_sh["CVE_Items.impact.baseMetricV2.impactScore"])+len(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"])))))+"% DE LAS VULNERABILIDADES LA PUNTUACION DE IMPACTO ES MAYOR O IGUAL QUE 2 \n")
print("EN EL "+str(float((((CV2_IMPACT_score_1_sh+CV2_IMPACT_score_1_iot)*100)/(len(df_cve_sh["CVE_Items.impact.baseMetricV2.impactScore"])+len(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"])))))+"% DE LAS VULNERABILIDADES LA PUNTUACION DE IMPACTO ES MAYOR O IGUAL QUE 1 \n")
print("EN EL "+str(float((((CV2_IMPACT_score_0_sh+CV2_IMPACT_score_0_iot)*100)/(len(df_cve_sh["CVE_Items.impact.baseMetricV2.impactScore"])+len(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"])))))+"% DE LAS VULNERABILIDADES LA PUNTUACION DE IMPACTO ES MAYOR O IGUAL QUE 0 \n")
print("EN EL "+str(float((((CV2_no_IMPACT_score_sh+CV2_no_IMPACT_score_iot)*100)/(len(df_cve_sh["CVE_Items.impact.baseMetricV2.impactScore"])+len(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"])))))+"% DE LAS VULNERABILIDADES LA PUNTUACION DE IMPACTO NO VIENE ESPECIFICADA \n")
print("\n")
