
import pandas as pd

#Abro los ficheros con los que voy a tratar

df_vuln_ibm_iot = pd.read_excel('vulnerabilidades_ibm_iot_2023.xlsx')
df_vuln_ibm_sh=pd.read_excel('vulnerabilidades_ibm_smart_home_2023.xlsx')


#Variables donde almacenare el contador de nivel de riesgo IBM para IOT
ibm_risk_level_9_iot=0
ibm_risk_level_8_iot=0
ibm_risk_level_7_iot=0
ibm_risk_level_6_iot=0
ibm_risk_level_5_iot=0
ibm_risk_level_4_iot=0
ibm_risk_level_3_iot=0
ibm_risk_level_2_iot=0
ibm_risk_level_1_iot=0
ibm_risk_level_0_iot=0
ibm_risk_level_10_iot=0
ibm_no_risk_level_iot=0


#Compruebo el nivel de riesgo en IBM para IOT

for i in range(0,len(df_vuln_ibm_iot["x_xfe_risk_level"])):
    if(((float(df_vuln_ibm_iot["x_xfe_risk_level"][i])) < 10.0) and ((float(df_vuln_ibm_iot["x_xfe_risk_level"][i])) >=9.0)):
        ibm_risk_level_9_iot+=1
    elif(((float(df_vuln_ibm_iot["x_xfe_risk_level"][i])) < 9.0) and ((float(df_vuln_ibm_iot["x_xfe_risk_level"][i])) >=8.0)):
        ibm_risk_level_8_iot+=1
    elif(((float(df_vuln_ibm_iot["x_xfe_risk_level"][i])) < 8.0) and ((float(df_vuln_ibm_iot["x_xfe_risk_level"][i])) >=7.0)):
        ibm_risk_level_7_iot+=1
    elif(((float(df_vuln_ibm_iot["x_xfe_risk_level"][i])) < 7.0) and ((float(df_vuln_ibm_iot["x_xfe_risk_level"][i])) >=6.0)):
        ibm_risk_level_6_iot+=1
    elif(((float(df_vuln_ibm_iot["x_xfe_risk_level"][i])) < 6.0) and ((float(df_vuln_ibm_iot["x_xfe_risk_level"][i])) >=5.0)):
        ibm_risk_level_5_iot+=1
    elif(((float(df_vuln_ibm_iot["x_xfe_risk_level"][i])) < 5.0) and ((float(df_vuln_ibm_iot["x_xfe_risk_level"][i])) >=4.0)):
        ibm_risk_level_4_iot+=1
    elif(((float(df_vuln_ibm_iot["x_xfe_risk_level"][i])) < 4.0) and ((float(df_vuln_ibm_iot["x_xfe_risk_level"][i])) >=3.0)):
        ibm_risk_level_3_iot+=1
    elif(((float(df_vuln_ibm_iot["x_xfe_risk_level"][i])) < 3.0) and ((float(df_vuln_ibm_iot["x_xfe_risk_level"][i])) >=2.0)):
        ibm_risk_level_2_iot+=1
    elif(((float(df_vuln_ibm_iot["x_xfe_risk_level"][i])) < 2.0) and ((float(df_vuln_ibm_iot["x_xfe_risk_level"][i])) >=1.0)):
        ibm_risk_level_1_iot+=1
    elif(((float(df_vuln_ibm_iot["x_xfe_risk_level"][i])) < 1.0) and ((float(df_vuln_ibm_iot["x_xfe_risk_level"][i])) >=0.0)):
        ibm_risk_level_0_iot+=1
    elif(((float(df_vuln_ibm_iot["x_xfe_risk_level"][i])) == 10.0)):
        ibm_risk_level_10_iot+=1
    else:
        ibm_no_risk_level_iot+=1
    

print("**************************ESTADÍSTICAS NIVEL DE RIESGO EN VULNERABILIDADES IBM PARTE IOT********************************")
print("\n")
print("EN "+str(ibm_risk_level_10_iot)+" VULNERABILIDADES EL NIVEL DE RIESGO ES 10 \n")
print("EN "+str(ibm_risk_level_9_iot)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 9 \n")
print("EN "+str(ibm_risk_level_8_iot)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 8 \n")
print("EN "+str(ibm_risk_level_7_iot)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 7 \n")
print("EN "+str(ibm_risk_level_6_iot)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 6 \n")
print("EN "+str(ibm_risk_level_5_iot)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 5 \n")
print("EN "+str(ibm_risk_level_4_iot)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 4 \n")
print("EN "+str(ibm_risk_level_3_iot)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 3 \n")
print("EN "+str(ibm_risk_level_2_iot)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 2 \n")
print("EN "+str(ibm_risk_level_1_iot)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 1 \n")
print("EN "+str(ibm_risk_level_0_iot)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 0 \n")
print("EN "+str(ibm_no_risk_level_iot)+" VULNERABILIDADES EL NIVEL DE RIESGO NO VIENE ESPECIFICADO \n")
print("\n")
print("***************************PORCENTAJE NIVEL DE RIESGO EN VULNERABILIDADES IBM PARTE IOT********************************")
print("\n")
print("EN EL "+str(float(((ibm_risk_level_10_iot*100)/len(df_vuln_ibm_iot["x_xfe_risk_level"]))))+"% DE LAS VULNERABILIDADES EL NIVEL DE RIESGO ES 10 \n")
print("EN EL "+str(float(((ibm_risk_level_9_iot*100)/len(df_vuln_ibm_iot["x_xfe_risk_level"]))))+"% DE LAS VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 9 \n")
print("EN EL "+str(float(((ibm_risk_level_8_iot*100)/len(df_vuln_ibm_iot["x_xfe_risk_level"]))))+"% DE LAS VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 8 \n")
print("EN EL "+str(float(((ibm_risk_level_7_iot*100)/len(df_vuln_ibm_iot["x_xfe_risk_level"]))))+"% DE LAS VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 7 \n")
print("EN EL "+str(float(((ibm_risk_level_6_iot*100)/len(df_vuln_ibm_iot["x_xfe_risk_level"]))))+"% DE LAS VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 6 \n")
print("EN EL "+str(float(((ibm_risk_level_5_iot*100)/len(df_vuln_ibm_iot["x_xfe_risk_level"]))))+"% DE LAS VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 5 \n")
print("EN EL "+str(float(((ibm_risk_level_4_iot*100)/len(df_vuln_ibm_iot["x_xfe_risk_level"]))))+"% DE LAS VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 4 \n")
print("EN EL "+str(float(((ibm_risk_level_3_iot*100)/len(df_vuln_ibm_iot["x_xfe_risk_level"]))))+"% DE LAS VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 3 \n")
print("EN EL "+str(float(((ibm_risk_level_2_iot*100)/len(df_vuln_ibm_iot["x_xfe_risk_level"]))))+"% DE LAS VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 2 \n")
print("EN EL "+str(float(((ibm_risk_level_1_iot*100)/len(df_vuln_ibm_iot["x_xfe_risk_level"]))))+"% DE LAS VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 1 \n")
print("EN EL "+str(float(((ibm_risk_level_0_iot*100)/len(df_vuln_ibm_iot["x_xfe_risk_level"]))))+"% DE LAS VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE  \n")
print("EN EL "+str(float(((ibm_no_risk_level_iot*100)/len(df_vuln_ibm_iot["x_xfe_risk_level"]))))+"% DE LAS VULNERABILIDADES EL NIVEL DE RIESGO NO VIENE ESPECIFICADO \n" )
print("\n")


#Variables donde almacenare el contador de nivel de riesgo IBM para SMART HOME
ibm_risk_level_9_sh=0
ibm_risk_level_8_sh=0
ibm_risk_level_7_sh=0
ibm_risk_level_6_sh=0
ibm_risk_level_5_sh=0
ibm_risk_level_4_sh=0
ibm_risk_level_3_sh=0
ibm_risk_level_2_sh=0
ibm_risk_level_1_sh=0
ibm_risk_level_0_sh=0
ibm_risk_level_10_sh=0
ibm_no_risk_level_sh=0


#Compruebo el nivel de riesgo en IBM para sh

for i in range(0,len(df_vuln_ibm_sh["x_xfe_risk_level"])):
    if(((float(df_vuln_ibm_sh["x_xfe_risk_level"][i])) < 10.0) and ((float(df_vuln_ibm_sh["x_xfe_risk_level"][i])) >=9.0)):
        ibm_risk_level_9_sh+=1
    elif(((float(df_vuln_ibm_sh["x_xfe_risk_level"][i])) < 9.0) and ((float(df_vuln_ibm_sh["x_xfe_risk_level"][i])) >=8.0)):
        ibm_risk_level_8_sh+=1
    elif(((float(df_vuln_ibm_sh["x_xfe_risk_level"][i])) < 8.0) and ((float(df_vuln_ibm_sh["x_xfe_risk_level"][i])) >=7.0)):
        ibm_risk_level_7_sh+=1
    elif(((float(df_vuln_ibm_sh["x_xfe_risk_level"][i])) < 7.0) and ((float(df_vuln_ibm_sh["x_xfe_risk_level"][i])) >=6.0)):
        ibm_risk_level_6_sh+=1
    elif(((float(df_vuln_ibm_sh["x_xfe_risk_level"][i])) < 6.0) and ((float(df_vuln_ibm_sh["x_xfe_risk_level"][i])) >=5.0)):
        ibm_risk_level_5_sh+=1
    elif(((float(df_vuln_ibm_sh["x_xfe_risk_level"][i])) < 5.0) and ((float(df_vuln_ibm_sh["x_xfe_risk_level"][i])) >=4.0)):
        ibm_risk_level_4_sh+=1
    elif(((float(df_vuln_ibm_sh["x_xfe_risk_level"][i])) < 4.0) and ((float(df_vuln_ibm_sh["x_xfe_risk_level"][i])) >=3.0)):
        ibm_risk_level_3_sh+=1
    elif(((float(df_vuln_ibm_sh["x_xfe_risk_level"][i])) < 3.0) and ((float(df_vuln_ibm_sh["x_xfe_risk_level"][i])) >=2.0)):
        ibm_risk_level_2_sh+=1
    elif(((float(df_vuln_ibm_sh["x_xfe_risk_level"][i])) < 2.0) and ((float(df_vuln_ibm_sh["x_xfe_risk_level"][i])) >=1.0)):
        ibm_risk_level_1_sh+=1
    elif(((float(df_vuln_ibm_sh["x_xfe_risk_level"][i])) < 1.0) and ((float(df_vuln_ibm_sh["x_xfe_risk_level"][i])) >=0.0)):
        ibm_risk_level_0_sh+=1
    elif(((float(df_vuln_ibm_sh["x_xfe_risk_level"][i])) == 10.0)):
        ibm_risk_level_10_sh+=1
    else:
        ibm_no_risk_level_sh+=1
    

print("**************************ESTADÍSTICAS NIVEL DE RIESGO EN VULNERABILIDADES IBM PARTE SMART HOME********************************")
print("\n")
print("EN "+str(ibm_risk_level_10_sh)+" VULNERABILIDADES EL NIVEL DE RIESGO ES 10 \n")
print("EN "+str(ibm_risk_level_9_sh)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 9 \n")
print("EN "+str(ibm_risk_level_8_sh)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 8 \n")
print("EN "+str(ibm_risk_level_7_sh)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 7 \n")
print("EN "+str(ibm_risk_level_6_sh)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 6 \n")
print("EN "+str(ibm_risk_level_5_sh)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 5 \n")
print("EN "+str(ibm_risk_level_4_sh)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 4 \n")
print("EN "+str(ibm_risk_level_3_sh)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 3 \n")
print("EN "+str(ibm_risk_level_2_sh)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 2 \n")
print("EN "+str(ibm_risk_level_1_sh)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 1 \n")
print("EN "+str(ibm_risk_level_0_sh)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 0 \n")
print("EN "+str(ibm_no_risk_level_sh)+" VULNERABILIDADES EL NIVEL DE RIESGO NO VIENE ESPECIFICADO \n")
print("\n")
print("***************************PORCENTAJE NIVEL DE RIESGO EN VULNERABILIDADES IBM PARTE SMART HOME********************************")
print("\n")
print("EN EL "+str(float(((ibm_risk_level_10_sh*100)/len(df_vuln_ibm_sh["x_xfe_risk_level"]))))+"% DE LAS VULNERABILIDADES EL NIVEL DE RIESGO ES 10 \n")
print("EN EL "+str(float(((ibm_risk_level_9_sh*100)/len(df_vuln_ibm_sh["x_xfe_risk_level"]))))+"% DE LAS VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 9 \n")
print("EN EL "+str(float(((ibm_risk_level_8_sh*100)/len(df_vuln_ibm_sh["x_xfe_risk_level"]))))+"% DE LAS VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 8 \n")
print("EN EL "+str(float(((ibm_risk_level_7_sh*100)/len(df_vuln_ibm_sh["x_xfe_risk_level"]))))+"% DE LAS VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 7 \n")
print("EN EL "+str(float(((ibm_risk_level_6_sh*100)/len(df_vuln_ibm_sh["x_xfe_risk_level"]))))+"% DE LAS VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 6 \n")
print("EN EL "+str(float(((ibm_risk_level_5_sh*100)/len(df_vuln_ibm_sh["x_xfe_risk_level"]))))+"% DE LAS VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 5 \n")
print("EN EL "+str(float(((ibm_risk_level_4_sh*100)/len(df_vuln_ibm_sh["x_xfe_risk_level"]))))+"% DE LAS VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 4 \n")
print("EN EL "+str(float(((ibm_risk_level_3_sh*100)/len(df_vuln_ibm_sh["x_xfe_risk_level"]))))+"% DE LAS VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 3 \n")
print("EN EL "+str(float(((ibm_risk_level_2_sh*100)/len(df_vuln_ibm_sh["x_xfe_risk_level"]))))+"% DE LAS VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 2 \n")
print("EN EL "+str(float(((ibm_risk_level_1_sh*100)/len(df_vuln_ibm_sh["x_xfe_risk_level"]))))+"% DE LAS VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 1 \n")
print("EN EL "+str(float(((ibm_risk_level_0_sh*100)/len(df_vuln_ibm_sh["x_xfe_risk_level"]))))+"% DE LAS VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE  \n")
print("EN EL "+str(float(((ibm_no_risk_level_sh*100)/len(df_vuln_ibm_sh["x_xfe_risk_level"]))))+"% DE LAS VULNERABILIDADES EL NIVEL DE RIESGO NO VIENE ESPECIFICADO \n" )
print("\n")







print("**************************ESTADÍSTICAS NIVEL DE RIESGO EN VULNERABILIDADES IBM PARTE IOT Y SMART HOME CONJUNTAS********************************")
print("\n")
print("EN "+str(ibm_risk_level_10_sh+ibm_risk_level_10_iot)+" VULNERABILIDADES EL NIVEL DE RIESGO ES 10 \n")
print("EN "+str(ibm_risk_level_9_sh+ibm_risk_level_9_iot)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 9 \n")
print("EN "+str(ibm_risk_level_8_sh+ibm_risk_level_8_iot)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 8 \n")
print("EN "+str(ibm_risk_level_7_sh+ibm_risk_level_7_iot)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 7 \n")
print("EN "+str(ibm_risk_level_6_sh+ibm_risk_level_6_iot)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 6 \n")
print("EN "+str(ibm_risk_level_5_sh+ibm_risk_level_5_iot)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 5 \n")
print("EN "+str(ibm_risk_level_4_sh+ibm_risk_level_4_iot)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 4 \n")
print("EN "+str(ibm_risk_level_3_sh+ibm_risk_level_3_iot)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 3 \n")
print("EN "+str(ibm_risk_level_2_sh+ibm_risk_level_2_iot)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 2 \n")
print("EN "+str(ibm_risk_level_1_sh+ibm_risk_level_1_iot)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 1 \n")
print("EN "+str(ibm_risk_level_0_sh+ibm_risk_level_0_iot)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 0 \n")
print("EN "+str(ibm_no_risk_level_sh+ibm_no_risk_level_iot)+" VULNERABILIDADES EL NIVEL DE RIESGO NO VIENE ESPECIFICADO \n")
print("\n")
print("***************************PORCENTAJE NIVEL DE RIESGO EN VULNERABILIDADES IBM PARTE IOT Y SMART HOME CONJUNTAS********************************")
print("\n")
print("EN EL "+str(float((((ibm_risk_level_10_sh+ibm_risk_level_10_iot)*100)/(len(df_vuln_ibm_sh["x_xfe_risk_level"])+len(df_vuln_ibm_iot["x_xfe_risk_level"])))))+"% DE LAS VULNERABILIDADES EL NIVEL DE RIESGO ES 10 \n")
print("EN EL "+str(float((((ibm_risk_level_9_sh+ibm_risk_level_9_iot)*100)/(len(df_vuln_ibm_sh["x_xfe_risk_level"])+len(df_vuln_ibm_iot["x_xfe_risk_level"])))))+"% DE LAS VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 9 \n")
print("EN EL "+str(float((((ibm_risk_level_8_sh+ibm_risk_level_8_iot)*100)/(len(df_vuln_ibm_sh["x_xfe_risk_level"])+len(df_vuln_ibm_iot["x_xfe_risk_level"])))))+"% DE LAS VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 8 \n")
print("EN EL "+str(float((((ibm_risk_level_7_sh+ibm_risk_level_7_iot)*100)/(len(df_vuln_ibm_sh["x_xfe_risk_level"])+len(df_vuln_ibm_iot["x_xfe_risk_level"])))))+"% DE LAS VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 7 \n")
print("EN EL "+str(float((((ibm_risk_level_6_sh+ibm_risk_level_6_iot)*100)/(len(df_vuln_ibm_sh["x_xfe_risk_level"])+len(df_vuln_ibm_iot["x_xfe_risk_level"])))))+"% DE LAS VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 6 \n")
print("EN EL "+str(float((((ibm_risk_level_5_sh+ibm_risk_level_5_iot)*100)/(len(df_vuln_ibm_sh["x_xfe_risk_level"])+len(df_vuln_ibm_iot["x_xfe_risk_level"])))))+"% DE LAS VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 5 \n")
print("EN EL "+str(float((((ibm_risk_level_4_sh+ibm_risk_level_4_iot)*100)/(len(df_vuln_ibm_sh["x_xfe_risk_level"])+len(df_vuln_ibm_iot["x_xfe_risk_level"])))))+"% DE LAS VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 4 \n")
print("EN EL "+str(float((((ibm_risk_level_3_sh+ibm_risk_level_3_iot)*100)/(len(df_vuln_ibm_sh["x_xfe_risk_level"])+len(df_vuln_ibm_iot["x_xfe_risk_level"])))))+"% DE LAS VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 3 \n")
print("EN EL "+str(float((((ibm_risk_level_2_sh+ibm_risk_level_2_iot)*100)/(len(df_vuln_ibm_sh["x_xfe_risk_level"])+len(df_vuln_ibm_iot["x_xfe_risk_level"])))))+"% DE LAS VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 2 \n")
print("EN EL "+str(float((((ibm_risk_level_1_sh+ibm_risk_level_1_iot)*100)/(len(df_vuln_ibm_sh["x_xfe_risk_level"])+len(df_vuln_ibm_iot["x_xfe_risk_level"])))))+"% DE LAS VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 1 \n")
print("EN EL "+str(float((((ibm_risk_level_0_sh+ibm_risk_level_0_iot)*100)/(len(df_vuln_ibm_sh["x_xfe_risk_level"])+len(df_vuln_ibm_iot["x_xfe_risk_level"])))))+"% DE LAS VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE  \n")
print("EN EL "+str(float((((ibm_no_risk_level_sh+ibm_no_risk_level_iot)*100)/(len(df_vuln_ibm_sh["x_xfe_risk_level"])+len(df_vuln_ibm_iot["x_xfe_risk_level"])))))+"% DE LAS VULNERABILIDADES EL NIVEL DE RIESGO NO VIENE ESPECIFICADO \n" )
print("\n")

