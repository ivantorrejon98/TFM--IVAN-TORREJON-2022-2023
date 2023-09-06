

import pandas as pd

#Abro los ficheros con los que voy a tratar

df_vuln_ibm_iot = pd.read_excel('vulnerabilidades_ibm_iot_2023.xlsx')
df_vuln_ibm_sh=pd.read_excel('vulnerabilidades_ibm_smart_home_2023.xlsx')




#Variables donde almacenare el contador de puntuacion temporal IBM para IOT
ibm_temporal_score_9_iot=0
ibm_temporal_score_8_iot=0
ibm_temporal_score_7_iot=0
ibm_temporal_score_6_iot=0
ibm_temporal_score_5_iot=0
ibm_temporal_score_4_iot=0
ibm_temporal_score_3_iot=0
ibm_temporal_score_2_iot=0
ibm_temporal_score_1_iot=0
ibm_temporal_score_0_iot=0
ibm_temporal_score_10_iot=0
ibm_no_temporal_score_iot=0


#Compruebo la puntuacion temporal en IBM para VULNERABILIDADES IOT

for i in range(0,len(df_vuln_ibm_iot["x_xfe_temporal_score"])):
    if(((float(df_vuln_ibm_iot["x_xfe_temporal_score"][i])) < 10.0) and ((float(df_vuln_ibm_iot["x_xfe_temporal_score"][i])) >=9.0)):
        ibm_temporal_score_9_iot+=1
    elif(((float(df_vuln_ibm_iot["x_xfe_temporal_score"][i])) < 9.0) and ((float(df_vuln_ibm_iot["x_xfe_temporal_score"][i])) >=8.0)):
        ibm_temporal_score_8_iot+=1
    elif(((float(df_vuln_ibm_iot["x_xfe_temporal_score"][i])) < 8.0) and ((float(df_vuln_ibm_iot["x_xfe_temporal_score"][i])) >=7.0)):
        ibm_temporal_score_7_iot+=1
    elif(((float(df_vuln_ibm_iot["x_xfe_temporal_score"][i])) < 7.0) and ((float(df_vuln_ibm_iot["x_xfe_temporal_score"][i])) >=6.0)):
        ibm_temporal_score_6_iot+=1
    elif(((float(df_vuln_ibm_iot["x_xfe_temporal_score"][i])) < 6.0) and ((float(df_vuln_ibm_iot["x_xfe_temporal_score"][i])) >=5.0)):
        ibm_temporal_score_5_iot+=1
    elif(((float(df_vuln_ibm_iot["x_xfe_temporal_score"][i])) < 5.0) and ((float(df_vuln_ibm_iot["x_xfe_temporal_score"][i])) >=4.0)):
        ibm_temporal_score_4_iot+=1
    elif(((float(df_vuln_ibm_iot["x_xfe_temporal_score"][i])) < 4.0) and ((float(df_vuln_ibm_iot["x_xfe_temporal_score"][i])) >=3.0)):
        ibm_temporal_score_3_iot+=1
    elif(((float(df_vuln_ibm_iot["x_xfe_temporal_score"][i])) < 3.0) and ((float(df_vuln_ibm_iot["x_xfe_temporal_score"][i])) >=2.0)):
        ibm_temporal_score_2_iot+=1
    elif(((float(df_vuln_ibm_iot["x_xfe_temporal_score"][i])) < 2.0) and ((float(df_vuln_ibm_iot["x_xfe_temporal_score"][i])) >=1.0)):
        ibm_temporal_score_1_iot+=1
    elif(((float(df_vuln_ibm_iot["x_xfe_temporal_score"][i])) < 1.0) and ((float(df_vuln_ibm_iot["x_xfe_temporal_score"][i])) >=0.0)):
        ibm_temporal_score_0_iot+=1
    elif(((float(df_vuln_ibm_iot["x_xfe_temporal_score"][i])) == 10.0)):
        ibm_temporal_score_10_iot+=1
    else:
        ibm_no_temporal_score_iot+=1
    

print("**************************ESTADÍSTICAS PUNTUACIÓN TEMPORAL EN VULNERABILIDADES IBM IOT********************************")
print("\n")
print("EN "+str(ibm_temporal_score_10_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES 10 \n")
print("EN "+str(ibm_temporal_score_9_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 9 \n")
print("EN "+str(ibm_temporal_score_8_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 8 \n")
print("EN "+str(ibm_temporal_score_7_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 7 \n")
print("EN "+str(ibm_temporal_score_6_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 6 \n")
print("EN "+str(ibm_temporal_score_5_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 5 \n")
print("EN "+str(ibm_temporal_score_4_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 4 \n")
print("EN "+str(ibm_temporal_score_3_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 3 \n")
print("EN "+str(ibm_temporal_score_2_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 2 \n")
print("EN "+str(ibm_temporal_score_1_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 1 \n")
print("EN "+str(ibm_temporal_score_0_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 0 \n")
print("EN "+str(ibm_no_temporal_score_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL NO VIENE ESPECIFICADA \n")
print("\n")
print("***************************PORCENTAJE PUNTUACION TEMPORAL EN VULNERABILIDADES IBM IOT********************************")
print("\n")
print("EN EL "+str(float(((ibm_temporal_score_10_iot*100)/len(df_vuln_ibm_iot["x_xfe_temporal_score"]))))+"% DE LAS VULNERABILIDADES LA PUNTUACION TEMPORAL ES 10 \n")
print("EN EL "+str(float(((ibm_temporal_score_9_iot*100)/len(df_vuln_ibm_iot["x_xfe_temporal_score"]))))+"% DE LAS VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 9 \n")
print("EN EL "+str(float(((ibm_temporal_score_8_iot*100)/len(df_vuln_ibm_iot["x_xfe_temporal_score"]))))+"% DE LAS VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 8 \n")
print("EN EL "+str(float(((ibm_temporal_score_7_iot*100)/len(df_vuln_ibm_iot["x_xfe_temporal_score"]))))+"% DE LAS VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 7 \n")
print("EN EL "+str(float(((ibm_temporal_score_6_iot*100)/len(df_vuln_ibm_iot["x_xfe_temporal_score"]))))+"% DE LAS VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 6 \n")
print("EN EL "+str(float(((ibm_temporal_score_5_iot*100)/len(df_vuln_ibm_iot["x_xfe_temporal_score"]))))+"% DE LAS VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 5 \n")
print("EN EL "+str(float(((ibm_temporal_score_4_iot*100)/len(df_vuln_ibm_iot["x_xfe_temporal_score"]))))+"% DE LAS VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 4 \n")
print("EN EL "+str(float(((ibm_temporal_score_3_iot*100)/len(df_vuln_ibm_iot["x_xfe_temporal_score"]))))+"% DE LAS VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 3 \n")
print("EN EL "+str(float(((ibm_temporal_score_2_iot*100)/len(df_vuln_ibm_iot["x_xfe_temporal_score"]))))+"% DE LAS VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 2 \n")
print("EN EL "+str(float(((ibm_temporal_score_1_iot*100)/len(df_vuln_ibm_iot["x_xfe_temporal_score"]))))+"% DE LAS VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 1 \n")
print("EN EL "+str(float(((ibm_temporal_score_0_iot*100)/len(df_vuln_ibm_iot["x_xfe_temporal_score"]))))+"% DE LAS VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE  \n")
print("EN EL "+str(float(((ibm_no_temporal_score_iot*100)/len(df_vuln_ibm_iot["x_xfe_temporal_score"]))))+"% DE LAS VULNERABILIDADES LA PUNTUACION TEMPORAL NO VIENE ESPECIFICADA \n" )
print("\n")







#Variables donde almacenare el contador de puntuacion temporal IBM para VULNERABILIDADES SMART HOME
ibm_temporal_score_9_sh=0
ibm_temporal_score_8_sh=0
ibm_temporal_score_7_sh=0
ibm_temporal_score_6_sh=0
ibm_temporal_score_5_sh=0
ibm_temporal_score_4_sh=0
ibm_temporal_score_3_sh=0
ibm_temporal_score_2_sh=0
ibm_temporal_score_1_sh=0
ibm_temporal_score_0_sh=0
ibm_temporal_score_10_sh=0
ibm_no_temporal_score_sh=0


#Compruebo la puntuacion temporal en IBM para VULNERABILIDADES SMART HOME

for l in range(0,len(df_vuln_ibm_sh["x_xfe_temporal_score"])):
    if(df_vuln_ibm_sh["x_xfe_temporal_score"][l]!='NONE'):
        if(((float(df_vuln_ibm_sh["x_xfe_temporal_score"][l])) < 10.0) and ((float(df_vuln_ibm_sh["x_xfe_temporal_score"][l])) >=9.0)):
            ibm_temporal_score_9_sh+=1
        elif(((float(df_vuln_ibm_sh["x_xfe_temporal_score"][l])) < 9.0) and ((float(df_vuln_ibm_sh["x_xfe_temporal_score"][l])) >=8.0)):
            ibm_temporal_score_8_sh+=1
        elif(((float(df_vuln_ibm_sh["x_xfe_temporal_score"][l])) < 8.0) and ((float(df_vuln_ibm_sh["x_xfe_temporal_score"][l])) >=7.0)):
            ibm_temporal_score_7_sh+=1
        elif(((float(df_vuln_ibm_sh["x_xfe_temporal_score"][l])) < 7.0) and ((float(df_vuln_ibm_sh["x_xfe_temporal_score"][l])) >=6.0)):
            ibm_temporal_score_6_sh+=1
        elif(((float(df_vuln_ibm_sh["x_xfe_temporal_score"][l])) < 6.0) and ((float(df_vuln_ibm_sh["x_xfe_temporal_score"][l])) >=5.0)):
            ibm_temporal_score_5_sh+=1
        elif(((float(df_vuln_ibm_sh["x_xfe_temporal_score"][l])) < 5.0) and ((float(df_vuln_ibm_sh["x_xfe_temporal_score"][l])) >=4.0)):
            ibm_temporal_score_4_sh+=1
        elif(((float(df_vuln_ibm_sh["x_xfe_temporal_score"][l])) < 4.0) and ((float(df_vuln_ibm_sh["x_xfe_temporal_score"][l])) >=3.0)):
            ibm_temporal_score_3_sh+=1
        elif(((float(df_vuln_ibm_sh["x_xfe_temporal_score"][l])) < 3.0) and ((float(df_vuln_ibm_sh["x_xfe_temporal_score"][l])) >=2.0)):
            ibm_temporal_score_2_sh+=1
        elif(((float(df_vuln_ibm_sh["x_xfe_temporal_score"][l])) < 2.0) and ((float(df_vuln_ibm_sh["x_xfe_temporal_score"][l])) >=1.0)):
            ibm_temporal_score_1_sh+=1
        elif(((float(df_vuln_ibm_sh["x_xfe_temporal_score"][l])) < 1.0) and ((float(df_vuln_ibm_sh["x_xfe_temporal_score"][l])) >=0.0)):
            ibm_temporal_score_0_sh+=1
        elif(((float(df_vuln_ibm_sh["x_xfe_temporal_score"][l])) == 10.0)):
            ibm_temporal_score_10_sh+=1
        else:
            ibm_no_temporal_score_sh+=1
    

print("**************************ESTADÍSTICAS PUNTUACIÓN TEMPORAL EN VULNERABILIDADES IBM SMART HOME********************************")
print("\n")
print("EN "+str(ibm_temporal_score_10_sh)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES 10 \n")
print("EN "+str(ibm_temporal_score_9_sh)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 9 \n")
print("EN "+str(ibm_temporal_score_8_sh)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 8 \n")
print("EN "+str(ibm_temporal_score_7_sh)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 7 \n")
print("EN "+str(ibm_temporal_score_6_sh)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 6 \n")
print("EN "+str(ibm_temporal_score_5_sh)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 5 \n")
print("EN "+str(ibm_temporal_score_4_sh)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 4 \n")
print("EN "+str(ibm_temporal_score_3_sh)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 3 \n")
print("EN "+str(ibm_temporal_score_2_sh)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 2 \n")
print("EN "+str(ibm_temporal_score_1_sh)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 1 \n")
print("EN "+str(ibm_temporal_score_0_sh)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 0 \n")
print("EN "+str(ibm_no_temporal_score_sh)+" VULNERABILIDADES LA PUNTUACION TEMPORAL NO VIENE ESPECIFICADA \n")
print("\n")
print("***************************PORCENTAJE PUNTUACION TEMPORAL EN VULNERABILIDADES IBM SMART HOME********************************")
print("\n")
print("EN EL "+str(float(((ibm_temporal_score_10_sh*100)/len(df_vuln_ibm_sh["x_xfe_temporal_score"]))))+"% DE LAS VULNERABILIDADES LA PUNTUACION TEMPORAL ES 10 \n")
print("EN EL "+str(float(((ibm_temporal_score_9_sh*100)/len(df_vuln_ibm_sh["x_xfe_temporal_score"]))))+"% DE LAS VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 9 \n")
print("EN EL "+str(float(((ibm_temporal_score_8_sh*100)/len(df_vuln_ibm_sh["x_xfe_temporal_score"]))))+"% DE LAS VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 8 \n")
print("EN EL "+str(float(((ibm_temporal_score_7_sh*100)/len(df_vuln_ibm_sh["x_xfe_temporal_score"]))))+"% DE LAS VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 7 \n")
print("EN EL "+str(float(((ibm_temporal_score_6_sh*100)/len(df_vuln_ibm_sh["x_xfe_temporal_score"]))))+"% DE LAS VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 6 \n")
print("EN EL "+str(float(((ibm_temporal_score_5_sh*100)/len(df_vuln_ibm_sh["x_xfe_temporal_score"]))))+"% DE LAS VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 5 \n")
print("EN EL "+str(float(((ibm_temporal_score_4_sh*100)/len(df_vuln_ibm_sh["x_xfe_temporal_score"]))))+"% DE LAS VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 4 \n")
print("EN EL "+str(float(((ibm_temporal_score_3_sh*100)/len(df_vuln_ibm_sh["x_xfe_temporal_score"]))))+"% DE LAS VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 3 \n")
print("EN EL "+str(float(((ibm_temporal_score_2_sh*100)/len(df_vuln_ibm_sh["x_xfe_temporal_score"]))))+"% DE LAS VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 2 \n")
print("EN EL "+str(float(((ibm_temporal_score_1_sh*100)/len(df_vuln_ibm_sh["x_xfe_temporal_score"]))))+"% DE LAS VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 1 \n")
print("EN EL "+str(float(((ibm_temporal_score_0_sh*100)/len(df_vuln_ibm_sh["x_xfe_temporal_score"]))))+"% DE LAS VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE  \n")
print("EN EL "+str(float(((ibm_no_temporal_score_sh*100)/len(df_vuln_ibm_sh["x_xfe_temporal_score"]))))+"% DE LAS VULNERABILIDADES LA PUNTUACION TEMPORAL NO VIENE ESPECIFICADA \n" )
print("\n")














print("**************************ESTADÍSTICAS PUNTUACIÓN TEMPORAL EN VULNERABILIDADES IBM PARTE IOT Y SMART HOME CONJUNTAS********************************")
print("\n")
print("EN "+str(ibm_temporal_score_10_sh+ibm_temporal_score_10_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES 10 \n")
print("EN "+str(ibm_temporal_score_9_sh+ibm_temporal_score_9_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 9 \n")
print("EN "+str(ibm_temporal_score_8_sh+ibm_temporal_score_8_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 8 \n")
print("EN "+str(ibm_temporal_score_7_sh+ibm_temporal_score_7_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 7 \n")
print("EN "+str(ibm_temporal_score_6_sh+ibm_temporal_score_6_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 6 \n")
print("EN "+str(ibm_temporal_score_5_sh+ibm_temporal_score_5_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 5 \n")
print("EN "+str(ibm_temporal_score_4_sh+ibm_temporal_score_4_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 4 \n")
print("EN "+str(ibm_temporal_score_3_sh+ibm_temporal_score_3_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 3 \n")
print("EN "+str(ibm_temporal_score_2_sh+ibm_temporal_score_2_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 2 \n")
print("EN "+str(ibm_temporal_score_1_sh+ibm_temporal_score_1_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 1 \n")
print("EN "+str(ibm_temporal_score_0_sh+ibm_temporal_score_0_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 0 \n")
print("EN "+str(ibm_no_temporal_score_sh+ibm_no_temporal_score_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL NO VIENE ESPECIFICADA \n")
print("\n")
print("***************************PORCENTAJE PUNTUACION TEMPORAL EN VULNERABILIDADES IBM PARTE IOT Y SMART HOME CONJUNTAS********************************")
print("\n")
print("EN EL "+str(float((((ibm_temporal_score_10_sh+ibm_temporal_score_10_iot)*100)/(len(df_vuln_ibm_sh["x_xfe_temporal_score"])+len(df_vuln_ibm_iot["x_xfe_temporal_score"])))))+"% DE LAS VULNERABILIDADES LA PUNTUACION TEMPORAL ES 10 \n")
print("EN EL "+str(float((((ibm_temporal_score_9_sh+ibm_temporal_score_9_iot)*100)/(len(df_vuln_ibm_sh["x_xfe_temporal_score"])+len(df_vuln_ibm_iot["x_xfe_temporal_score"])))))+"% DE LAS VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 9 \n")
print("EN EL "+str(float((((ibm_temporal_score_8_sh+ibm_temporal_score_8_iot)*100)/(len(df_vuln_ibm_sh["x_xfe_temporal_score"])+len(df_vuln_ibm_iot["x_xfe_temporal_score"])))))+"% DE LAS VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 8 \n")
print("EN EL "+str(float((((ibm_temporal_score_7_sh+ibm_temporal_score_7_iot)*100)/(len(df_vuln_ibm_sh["x_xfe_temporal_score"])+len(df_vuln_ibm_iot["x_xfe_temporal_score"])))))+"% DE LAS VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 7 \n")
print("EN EL "+str(float((((ibm_temporal_score_6_sh+ibm_temporal_score_6_iot)*100)/(len(df_vuln_ibm_sh["x_xfe_temporal_score"])+len(df_vuln_ibm_iot["x_xfe_temporal_score"])))))+"% DE LAS VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 6 \n")
print("EN EL "+str(float((((ibm_temporal_score_5_sh+ibm_temporal_score_5_iot)*100)/(len(df_vuln_ibm_sh["x_xfe_temporal_score"])+len(df_vuln_ibm_iot["x_xfe_temporal_score"])))))+"% DE LAS VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 5 \n")
print("EN EL "+str(float((((ibm_temporal_score_4_sh+ibm_temporal_score_4_iot)*100)/(len(df_vuln_ibm_sh["x_xfe_temporal_score"])+len(df_vuln_ibm_iot["x_xfe_temporal_score"])))))+"% DE LAS VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 4 \n")
print("EN EL "+str(float((((ibm_temporal_score_3_sh+ibm_temporal_score_3_iot)*100)/(len(df_vuln_ibm_sh["x_xfe_temporal_score"])+len(df_vuln_ibm_iot["x_xfe_temporal_score"])))))+"% DE LAS VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 3 \n")
print("EN EL "+str(float((((ibm_temporal_score_2_sh+ibm_temporal_score_2_iot)*100)/(len(df_vuln_ibm_sh["x_xfe_temporal_score"])+len(df_vuln_ibm_iot["x_xfe_temporal_score"])))))+"% DE LAS VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 2 \n")
print("EN EL "+str(float((((ibm_temporal_score_1_sh+ibm_temporal_score_1_iot)*100)/(len(df_vuln_ibm_sh["x_xfe_temporal_score"])+len(df_vuln_ibm_iot["x_xfe_temporal_score"])))))+"% DE LAS VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 1 \n")
print("EN EL "+str(float((((ibm_temporal_score_0_sh+ibm_temporal_score_0_iot)*100)/(len(df_vuln_ibm_sh["x_xfe_temporal_score"])+len(df_vuln_ibm_iot["x_xfe_temporal_score"])))))+"% DE LAS VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE  \n")
print("EN EL "+str(float((((ibm_no_temporal_score_sh+ibm_no_temporal_score_iot)*100)/(len(df_vuln_ibm_sh["x_xfe_temporal_score"])+len(df_vuln_ibm_iot["x_xfe_temporal_score"])))))+"% DE LAS VULNERABILIDADES LA PUNTUACION TEMPORAL NO VIENE ESPECIFICADA \n" )
print("\n")















