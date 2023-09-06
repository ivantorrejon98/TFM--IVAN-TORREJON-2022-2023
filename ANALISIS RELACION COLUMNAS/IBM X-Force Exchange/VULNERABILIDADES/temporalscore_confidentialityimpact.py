				
import pandas as pd
from datetime import datetime,timedelta



#Abro los ficheros con los que voy a tratar




df_vulnibm_iot = pd.read_excel('vulnerabilidades_ibm_iot_2023.xlsx')

#Variables donde almacenare el contador de puntuacion temporal especifico de IBM para IOT
ibm_temporal_score_9_iot=0
#Variables donde almacenare el contador de impacto de confidencialidad dado un valor especifico de puntuacion temporal
ibm_temporal_score_9_high_confimpact_iot=0
ibm_temporal_score_9_low_confimpact_iot=0
ibm_temporal_score_9_medium_confimpact_iot=0
ibm_temporal_score_9_confimpact_iot=0

ibm_temporal_score_8_iot=0
ibm_temporal_score_8_high_confimpact_iot=0
ibm_temporal_score_8_low_confimpact_iot=0
ibm_temporal_score_8_medium_confimpact_iot=0
ibm_temporal_score_8_confimpact_iot=0

ibm_temporal_score_7_iot=0
ibm_temporal_score_7_high_confimpact_iot=0
ibm_temporal_score_7_low_confimpact_iot=0
ibm_temporal_score_7_medium_confimpact_iot=0
ibm_temporal_score_7_confimpact_iot=0

ibm_temporal_score_6_iot=0
ibm_temporal_score_6_high_confimpact_iot=0
ibm_temporal_score_6_low_confimpact_iot=0
ibm_temporal_score_6_medium_confimpact_iot=0
ibm_temporal_score_6_confimpact_iot=0

ibm_temporal_score_5_iot=0
ibm_temporal_score_5_high_confimpact_iot=0
ibm_temporal_score_5_low_confimpact_iot=0
ibm_temporal_score_5_medium_confimpact_iot=0
ibm_temporal_score_5_confimpact_iot=0


ibm_temporal_score_4_iot=0
ibm_temporal_score_4_high_confimpact_iot=0
ibm_temporal_score_4_low_confimpact_iot=0
ibm_temporal_score_4_medium_confimpact_iot=0
ibm_temporal_score_4_confimpact_iot=0


ibm_temporal_score_3_iot=0
ibm_temporal_score_3_high_confimpact_iot=0
ibm_temporal_score_3_low_confimpact_iot=0
ibm_temporal_score_3_medium_confimpact_iot=0
ibm_temporal_score_3_confimpact_iot=0


ibm_temporal_score_2_iot=0
ibm_temporal_score_2_high_confimpact_iot=0
ibm_temporal_score_2_low_confimpact_iot=0
ibm_temporal_score_2_medium_confimpact_iot=0
ibm_temporal_score_2_confimpact_iot=0


ibm_temporal_score_1_iot=0
ibm_temporal_score_1_high_confimpact_iot=0
ibm_temporal_score_1_low_confimpact_iot=0
ibm_temporal_score_1_medium_confimpact_iot=0
ibm_temporal_score_1_confimpact_iot=0

ibm_temporal_score_0_iot=0
ibm_temporal_score_0_high_confimpact_iot=0
ibm_temporal_score_0_low_confimpact_iot=0
ibm_temporal_score_0_medium_confimpact_iot=0
ibm_temporal_score_0_confimpact_iot=0


ibm_temporal_score_10_iot=0
ibm_temporal_score_10_high_confimpact_iot=0
ibm_temporal_score_10_low_confimpact_iot=0
ibm_temporal_score_10_medium_confimpact_iot=0
ibm_temporal_score_10_confimpact_iot=0

ibm_temporal_score_total=0



#Compruebo la puntuacion temporal en IBM para IOT

for r in range(0,len(df_vulnibm_iot["x_xfe_temporal_score"])):
    #Compruebo la puntuacion temporal
    if(df_vulnibm_iot["x_xfe_temporal_score"][r] !='NONE'):
        if(((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) < 10.0) and ((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) >=9.0)):
            ibm_temporal_score_9_iot+=1
            ibm_temporal_score_total+=1
            #Compruebo el impacto de confidencialidad
            if(df_vulnibm_iot["x_xfe_cvss_confidentiality_impact"][r]=='High'):
                ibm_temporal_score_9_confimpact_iot+=1
                ibm_temporal_score_9_high_confimpact_iot+=1
            elif(df_vulnibm_iot["x_xfe_cvss_confidentiality_impact"][r]=='Low'):
                ibm_temporal_score_9_confimpact_iot+=1
                ibm_temporal_score_9_low_confimpact_iot+=1
            elif(df_vulnibm_iot["x_xfe_cvss_confidentiality_impact"][r]=='Medium'):
                ibm_temporal_score_9_confimpact_iot+=1
                ibm_temporal_score_9_medium_confimpact_iot+=1

        elif(((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) < 9.0) and ((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) >=8.0)):
            ibm_temporal_score_8_iot+=1
            ibm_temporal_score_total+=1
            if(df_vulnibm_iot["x_xfe_cvss_confidentiality_impact"][r]=='High'):
                ibm_temporal_score_8_confimpact_iot+=1
                ibm_temporal_score_8_high_confimpact_iot+=1
            elif(df_vulnibm_iot["x_xfe_cvss_confidentiality_impact"][r]=='Low'):
                ibm_temporal_score_8_confimpact_iot+=1
                ibm_temporal_score_8_low_confimpact_iot+=1
            elif(df_vulnibm_iot["x_xfe_cvss_confidentiality_impact"][r]=='Medium'):
                ibm_temporal_score_8_confimpact_iot+=1
                ibm_temporal_score_8_medium_confimpact_iot+=1
        elif(((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) < 8.0) and ((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) >=7.0)):
            ibm_temporal_score_7_iot+=1
            ibm_temporal_score_total+=1
            if(df_vulnibm_iot["x_xfe_cvss_confidentiality_impact"][r]=='High'):
                ibm_temporal_score_7_confimpact_iot+=1
                ibm_temporal_score_7_high_confimpact_iot+=1
            elif(df_vulnibm_iot["x_xfe_cvss_confidentiality_impact"][r]=='Low'):
                ibm_temporal_score_7_confimpact_iot+=1
                ibm_temporal_score_7_low_confimpact_iot+=1
            elif(df_vulnibm_iot["x_xfe_cvss_confidentiality_impact"][r]=='Medium'):
                ibm_temporal_score_7_confimpact_iot+=1
                ibm_temporal_score_7_medium_confimpact_iot+=1
        elif(((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) < 7.0) and ((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) >=6.0)):
            ibm_temporal_score_6_iot+=1
            ibm_temporal_score_total+=1
            if(df_vulnibm_iot["x_xfe_cvss_confidentiality_impact"][r]=='High'):
                ibm_temporal_score_6_confimpact_iot+=1
                ibm_temporal_score_6_high_confimpact_iot+=1
            elif(df_vulnibm_iot["x_xfe_cvss_confidentiality_impact"][r]=='Low'):
                ibm_temporal_score_6_confimpact_iot+=1
                ibm_temporal_score_6_low_confimpact_iot+=1
            elif(df_vulnibm_iot["x_xfe_cvss_confidentiality_impact"][r]=='Medium'):
                ibm_temporal_score_6_confimpact_iot+=1
                ibm_temporal_score_6_medium_confimpact_iot+=1
        elif(((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) < 6.0) and ((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) >=5.0)):
            ibm_temporal_score_5_iot+=1
            ibm_temporal_score_total+=1
            if(df_vulnibm_iot["x_xfe_cvss_confidentiality_impact"][r]=='High'):
                ibm_temporal_score_5_confimpact_iot+=1
                ibm_temporal_score_5_high_confimpact_iot+=1
            elif(df_vulnibm_iot["x_xfe_cvss_confidentiality_impact"][r]=='Low'):
                ibm_temporal_score_5_confimpact_iot+=1
                ibm_temporal_score_5_low_confimpact_iot+=1
            elif(df_vulnibm_iot["x_xfe_cvss_confidentiality_impact"][r]=='Medium'):
                ibm_temporal_score_5_confimpact_iot+=1
                ibm_temporal_score_5_medium_confimpact_iot+=1
        elif(((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) < 5.0) and ((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) >=4.0)):
            ibm_temporal_score_4_iot+=1
            ibm_temporal_score_total+=1
            if(df_vulnibm_iot["x_xfe_cvss_confidentiality_impact"][r]=='High'):
                ibm_temporal_score_4_confimpact_iot+=1
                ibm_temporal_score_4_high_confimpact_iot+=1
            elif(df_vulnibm_iot["x_xfe_cvss_confidentiality_impact"][r]=='Low'):
                ibm_temporal_score_4_confimpact_iot+=1
                ibm_temporal_score_4_low_confimpact_iot+=1
            elif(df_vulnibm_iot["x_xfe_cvss_confidentiality_impact"][r]=='Medium'):
                ibm_temporal_score_4_confimpact_iot+=1
                ibm_temporal_score_4_medium_confimpact_iot+=1
        elif(((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) < 4.0) and ((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) >=3.0)):
            ibm_temporal_score_3_iot+=1
            ibm_temporal_score_total+=1
            if(df_vulnibm_iot["x_xfe_cvss_confidentiality_impact"][r]=='High'):
                ibm_temporal_score_3_confimpact_iot+=1
                ibm_temporal_score_3_high_confimpact_iot+=1
            elif(df_vulnibm_iot["x_xfe_cvss_confidentiality_impact"][r]=='Low'):
                ibm_temporal_score_3_confimpact_iot+=1
                ibm_temporal_score_3_low_confimpact_iot+=1
            elif(df_vulnibm_iot["x_xfe_cvss_confidentiality_impact"][r]=='Medium'):
                ibm_temporal_score_3_confimpact_iot+=1
                ibm_temporal_score_3_medium_confimpact_iot+=1
        elif(((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) < 3.0) and ((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) >=2.0)):
            ibm_temporal_score_2_iot+=1
            ibm_temporal_score_total+=1
            if(df_vulnibm_iot["x_xfe_cvss_confidentiality_impact"][r]=='High'):
                ibm_temporal_score_2_confimpact_iot+=1
                ibm_temporal_score_2_high_confimpact_iot+=1
            elif(df_vulnibm_iot["x_xfe_cvss_confidentiality_impact"][r]=='Low'):
                ibm_temporal_score_2_confimpact_iot+=1
                ibm_temporal_score_2_low_confimpact_iot+=1
            elif(df_vulnibm_iot["x_xfe_cvss_confidentiality_impact"][r]=='Medium'):
                ibm_temporal_score_2_confimpact_iot+=1
                ibm_temporal_score_2_medium_confimpact_iot+=1
        elif(((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) < 2.0) and ((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) >=1.0)):
            ibm_temporal_score_1_iot+=1
            ibm_temporal_score_total+=1
            if(df_vulnibm_iot["x_xfe_cvss_confidentiality_impact"][r]=='High'):
                ibm_temporal_score_1_confimpact_iot+=1
                ibm_temporal_score_1_high_confimpact_iot+=1
            elif(df_vulnibm_iot["x_xfe_cvss_confidentiality_impact"][r]=='Low'):
                ibm_temporal_score_1_confimpact_iot+=1
                ibm_temporal_score_1_low_confimpact_iot+=1
            elif(df_vulnibm_iot["x_xfe_cvss_confidentiality_impact"][r]=='Medium'):
                ibm_temporal_score_1_confimpact_iot+=1
                ibm_temporal_score_1_medium_confimpact_iot+=1
        elif(((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) < 1.0) and ((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) >=0.0)):
            ibm_temporal_score_0_iot+=0
            ibm_temporal_score_total+=0
            if(df_vulnibm_iot["x_xfe_cvss_confidentiality_impact"][r]=='High'):
                ibm_temporal_score_0_confimpact_iot+=0
                ibm_temporal_score_0_high_confimpact_iot+=0
            elif(df_vulnibm_iot["x_xfe_cvss_confidentiality_impact"][r]=='Low'):
                ibm_temporal_score_0_confimpact_iot+=0
                ibm_temporal_score_0_low_confimpact_iot+=0
            elif(df_vulnibm_iot["x_xfe_cvss_confidentiality_impact"][r]=='Medium'):
                ibm_temporal_score_0_confimpact_iot+=0
                ibm_temporal_score_0_medium_confimpact_iot+=0
        elif(((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) == 10.0)):
            ibm_temporal_score_10_iot+=0
            ibm_temporal_score_total+=0
            if(df_vulnibm_iot["x_xfe_cvss_confidentiality_impact"][r]=='High'):
                ibm_temporal_score_10_confimpact_iot+=0
                ibm_temporal_score_10_high_confimpact_iot+=0
            elif(df_vulnibm_iot["x_xfe_cvss_confidentiality_impact"][r]=='Low'):
                ibm_temporal_score_10_confimpact_iot+=0
                ibm_temporal_score_10_low_confimpact_iot+=0
            elif(df_vulnibm_iot["x_xfe_cvss_confidentiality_impact"][r]=='Medium'):
                ibm_temporal_score_10_confimpact_iot+=0
                ibm_temporal_score_10_medium_confimpact_iot+=0
            
            
            
            
            
            
            
            
            
            
            
print("*********************ESTADÍSTICAS PUNTUACION TEMPORAL/IMPACTO DE CONFIDENCIALIDAD VULNERABILIDADES IBM PARTE IOT*********************")
print("\n")                            
print("\n")
print(" DE UN TOTAL DE "+str(ibm_temporal_score_total)+" VULNERABILIDADES:\n") 
print("\n")
print("   - LAS ESTADISTICAS DE VALORES DE PUNTUACION TEMPORAL SON LAS SIGUIENTES:  \n")
print("      -    EN  "+str(ibm_temporal_score_10_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES 10. EL IMPACTO DE CONFIDENCIALIDAD VIENE ESPECIFICADO EN "+str(ibm_temporal_score_10_confimpact_iot)+" VULNERABILIDADES. LAS ESTADÍSTICAS DE IMPACTO DE CONFIDENCIALIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(ibm_temporal_score_10_high_confimpact_iot)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
print("            -    EN  "+str(ibm_temporal_score_10_low_confimpact_iot)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
print("            -    EN  "+str(ibm_temporal_score_10_medium_confimpact_iot)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO \n")
print("      -    EN  "+str(ibm_temporal_score_9_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 9. EL IMPACTO DE CONFIDENCIALIDAD VIENE ESPECIFICADO EN "+str(ibm_temporal_score_9_confimpact_iot)+" VULNERABILIDADES. LAS ESTADÍSTICAS DE IMPACTO DE CONFIDENCIALIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(ibm_temporal_score_9_high_confimpact_iot)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
print("            -    EN  "+str(ibm_temporal_score_9_low_confimpact_iot)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
print("            -    EN  "+str(ibm_temporal_score_9_medium_confimpact_iot)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO \n")
print("      -    EN  "+str(ibm_temporal_score_8_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 8. EL IMPACTO DE CONFIDENCIALIDAD VIENE ESPECIFICADO EN "+str(ibm_temporal_score_8_confimpact_iot)+" VULNERABILIDADES. LAS ESTADÍSTICAS DE IMPACTO DE CONFIDENCIALIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(ibm_temporal_score_8_high_confimpact_iot)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
print("            -    EN  "+str(ibm_temporal_score_8_low_confimpact_iot)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
print("            -    EN  "+str(ibm_temporal_score_8_medium_confimpact_iot)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO \n")
print("      -    EN  "+str(ibm_temporal_score_7_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 7. EL IMPACTO DE CONFIDENCIALIDAD VIENE ESPECIFICADO EN "+str(ibm_temporal_score_7_confimpact_iot)+" VULNERABILIDADES. LAS ESTADÍSTICAS DE IMPACTO DE CONFIDENCIALIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(ibm_temporal_score_7_high_confimpact_iot)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
print("            -    EN  "+str(ibm_temporal_score_7_low_confimpact_iot)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
print("            -    EN  "+str(ibm_temporal_score_7_medium_confimpact_iot)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO \n")
print("      -    EN  "+str(ibm_temporal_score_6_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 6. EL IMPACTO DE CONFIDENCIALIDAD VIENE ESPECIFICADO EN "+str(ibm_temporal_score_6_confimpact_iot)+" VULNERABILIDADES. LAS ESTADÍSTICAS DE IMPACTO DE CONFIDENCIALIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(ibm_temporal_score_6_high_confimpact_iot)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
print("            -    EN  "+str(ibm_temporal_score_6_low_confimpact_iot)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
print("            -    EN  "+str(ibm_temporal_score_6_medium_confimpact_iot)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO \n")
print("      -    EN  "+str(ibm_temporal_score_5_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 5. EL IMPACTO DE CONFIDENCIALIDAD VIENE ESPECIFICADO EN "+str(ibm_temporal_score_5_confimpact_iot)+" VULNERABILIDADES. LAS ESTADÍSTICAS DE IMPACTO DE CONFIDENCIALIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(ibm_temporal_score_5_high_confimpact_iot)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
print("            -    EN  "+str(ibm_temporal_score_5_low_confimpact_iot)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
print("            -    EN  "+str(ibm_temporal_score_5_medium_confimpact_iot)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO \n")
print("      -    EN  "+str(ibm_temporal_score_4_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 4. EL IMPACTO DE CONFIDENCIALIDAD VIENE ESPECIFICADO EN "+str(ibm_temporal_score_4_confimpact_iot)+" VULNERABILIDADES. LAS ESTADÍSTICAS DE IMPACTO DE CONFIDENCIALIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(ibm_temporal_score_4_high_confimpact_iot)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
print("            -    EN  "+str(ibm_temporal_score_4_low_confimpact_iot)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
print("            -    EN  "+str(ibm_temporal_score_4_medium_confimpact_iot)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO \n")
print("      -    EN  "+str(ibm_temporal_score_3_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 3. EL IMPACTO DE CONFIDENCIALIDAD VIENE ESPECIFICADO EN "+str(ibm_temporal_score_3_confimpact_iot)+" VULNERABILIDADES. LAS ESTADÍSTICAS DE IMPACTO DE CONFIDENCIALIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(ibm_temporal_score_3_high_confimpact_iot)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
print("            -    EN  "+str(ibm_temporal_score_3_low_confimpact_iot)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
print("            -    EN  "+str(ibm_temporal_score_3_medium_confimpact_iot)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO \n")
print("      -    EN  "+str(ibm_temporal_score_2_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 2. EL IMPACTO DE CONFIDENCIALIDAD VIENE ESPECIFICADO EN "+str(ibm_temporal_score_2_confimpact_iot)+" VULNERABILIDADES. LAS ESTADÍSTICAS DE IMPACTO DE CONFIDENCIALIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(ibm_temporal_score_2_high_confimpact_iot)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
print("            -    EN  "+str(ibm_temporal_score_2_low_confimpact_iot)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
print("            -    EN  "+str(ibm_temporal_score_2_medium_confimpact_iot)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO \n")
print("      -    EN  "+str(ibm_temporal_score_1_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 1. EL IMPACTO DE CONFIDENCIALIDAD VIENE ESPECIFICADO EN "+str(ibm_temporal_score_1_confimpact_iot)+" VULNERABILIDADES. LAS ESTADÍSTICAS DE IMPACTO DE CONFIDENCIALIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(ibm_temporal_score_1_high_confimpact_iot)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
print("            -    EN  "+str(ibm_temporal_score_1_low_confimpact_iot)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
print("            -    EN  "+str(ibm_temporal_score_1_medium_confimpact_iot)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO \n")
print("      -    EN  "+str(ibm_temporal_score_0_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 0. EL IMPACTO DE CONFIDENCIALIDAD VIENE ESPECIFICADO EN "+str(ibm_temporal_score_0_confimpact_iot)+" VULNERABILIDADES. LAS ESTADÍSTICAS DE IMPACTO DE CONFIDENCIALIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(ibm_temporal_score_0_high_confimpact_iot)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
print("            -    EN  "+str(ibm_temporal_score_0_low_confimpact_iot)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
print("            -    EN  "+str(ibm_temporal_score_0_medium_confimpact_iot)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO \n")






print("*********************PORCENTAJE PUNTUACION TEMPORAL/IMPACTO DE CONFIDENCIALIDAD VULNERABILIDADES IBM IOT*********************")
print("\n")                            
print("\n")
print(" DE UN TOTAL DE "+str(ibm_temporal_score_total)+" VULNERABILIDADES :\n") 
print("\n")
print("   - LOS PORCENTAJES DE VALORES DE PUNTUACION TEMPORAL SON LOS SIGUIENTES:  \n")
if(ibm_temporal_score_10_confimpact_iot>0):
    print("      -    EN EL  "+str(float(((ibm_temporal_score_10_iot*100)/ibm_temporal_score_total)))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES 10. EL IMPACTO DE CONFIDENCIALIDAD VIENE ESPECIFICADO EN EL "+str(float(((ibm_temporal_score_10_confimpact_iot*100)/ibm_temporal_score_10_iot)))+" % DE ELLAS. LOS PORCENTAJES DE IMPACTO DE CONFIDENCIALIDAD SON LOS SIGUIENTES :  \n")
    print("            -    EN EL  "+str(float(((ibm_temporal_score_10_high_confimpact_iot*100)/ibm_temporal_score_10_confimpact_iot)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
    print("            -    EN EL  "+str(float(((ibm_temporal_score_10_low_confimpact_iot*100)/ibm_temporal_score_10_confimpact_iot)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
    print("            -    EN EL  "+str(float(((ibm_temporal_score_10_medium_confimpact_iot*100)/ibm_temporal_score_10_confimpact_iot)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO \n")
    print("\n")
if(ibm_temporal_score_9_confimpact_iot>0):
    print("      -    EN EL  "+str(float(((ibm_temporal_score_9_iot*100)/ibm_temporal_score_total)))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 9. EL IMPACTO DE CONFIDENCIALIDAD VIENE ESPECIFICADO EN EL "+str(float(((ibm_temporal_score_9_confimpact_iot*100)/ibm_temporal_score_9_iot)))+" % DE ELLAS. LOS PORCENTAJES DE IMPACTO DE CONFIDENCIALIDAD SON LOS SIGUIENTES :  :  \n")
    print("            -    EN EL  "+str(float(((ibm_temporal_score_9_high_confimpact_iot*100)/ibm_temporal_score_9_confimpact_iot)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
    print("            -    EN EL  "+str(float(((ibm_temporal_score_9_low_confimpact_iot*100)/ibm_temporal_score_9_confimpact_iot)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
    print("            -    EN EL  "+str(float(((ibm_temporal_score_9_medium_confimpact_iot*100)/ibm_temporal_score_9_confimpact_iot)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO \n")
    print("\n")
if(ibm_temporal_score_8_confimpact_iot>0):
    print("      -    EN EL  "+str(float(((ibm_temporal_score_8_iot*100)/ibm_temporal_score_total)))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 8. EL IMPACTO DE CONFIDENCIALIDAD VIENE ESPECIFICADO EN EL "+str(float(((ibm_temporal_score_8_confimpact_iot*100)/ibm_temporal_score_8_iot)))+" % DE ELLAS. LOS PORCENTAJES DE IMPACTO DE CONFIDENCIALIDAD SON LOS SIGUIENTES :  :  \n")
    print("            -    EN EL  "+str(float(((ibm_temporal_score_8_high_confimpact_iot*100)/ibm_temporal_score_8_confimpact_iot)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
    print("            -    EN EL  "+str(float(((ibm_temporal_score_8_low_confimpact_iot*100)/ibm_temporal_score_8_confimpact_iot)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
    print("            -    EN EL  "+str(float(((ibm_temporal_score_8_medium_confimpact_iot*100)/ibm_temporal_score_8_confimpact_iot)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO \n")
    print("\n")
if(ibm_temporal_score_7_confimpact_iot>0):
    print("      -    EN EL  "+str(float(((ibm_temporal_score_7_iot*100)/ibm_temporal_score_total)))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 7. EL IMPACTO DE CONFIDENCIALIDAD VIENE ESPECIFICADO EN EL "+str(float(((ibm_temporal_score_7_confimpact_iot*100)/ibm_temporal_score_7_iot)))+" % DE ELLAS. LOS PORCENTAJES DE IMPACTO DE CONFIDENCIALIDAD SON LOS SIGUIENTES :  :  \n")
    print("            -    EN EL  "+str(float(((ibm_temporal_score_7_high_confimpact_iot*100)/ibm_temporal_score_7_confimpact_iot)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
    print("            -    EN EL  "+str(float(((ibm_temporal_score_7_low_confimpact_iot*100)/ibm_temporal_score_7_confimpact_iot)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
    print("            -    EN EL  "+str(float(((ibm_temporal_score_7_medium_confimpact_iot*100)/ibm_temporal_score_7_confimpact_iot)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO \n")
    print("\n")
if(ibm_temporal_score_6_confimpact_iot>0):
    print("      -    EN EL  "+str(float(((ibm_temporal_score_6_iot*100)/ibm_temporal_score_total)))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 6. EL IMPACTO DE CONFIDENCIALIDAD VIENE ESPECIFICADO EN EL "+str(float(((ibm_temporal_score_6_confimpact_iot*100)/ibm_temporal_score_6_iot)))+" % DE ELLAS. LOS PORCENTAJES DE IMPACTO DE CONFIDENCIALIDAD SON LOS SIGUIENTES :  \n")
    print("            -    EN EL  "+str(float(((ibm_temporal_score_6_high_confimpact_iot*100)/ibm_temporal_score_6_confimpact_iot)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
    print("            -    EN EL  "+str(float(((ibm_temporal_score_6_low_confimpact_iot*100)/ibm_temporal_score_6_confimpact_iot)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
    print("            -    EN EL  "+str(float(((ibm_temporal_score_6_medium_confimpact_iot*100)/ibm_temporal_score_6_confimpact_iot)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO \n")
    print("\n")
if(ibm_temporal_score_5_confimpact_iot>0):
    print("      -    EN EL  "+str(float(((ibm_temporal_score_5_iot*100)/ibm_temporal_score_total)))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 5. EL IMPACTO DE CONFIDENCIALIDAD VIENE ESPECIFICADO EN EL "+str(float(((ibm_temporal_score_5_confimpact_iot*100)/ibm_temporal_score_5_iot)))+" % DE ELLAS. LOS PORCENTAJES DE IMPACTO DE CONFIDENCIALIDAD SON LOS SIGUIENTES :  \n")
    print("            -    EN EL  "+str(float(((ibm_temporal_score_5_high_confimpact_iot*100)/ibm_temporal_score_5_confimpact_iot)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
    print("            -    EN EL  "+str(float(((ibm_temporal_score_5_low_confimpact_iot*100)/ibm_temporal_score_5_confimpact_iot)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
    print("            -    EN EL  "+str(float(((ibm_temporal_score_5_medium_confimpact_iot*100)/ibm_temporal_score_5_confimpact_iot)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO \n")
    print("\n")
if(ibm_temporal_score_4_confimpact_iot>0):
    print("      -    EN EL  "+str(float(((ibm_temporal_score_4_iot*100)/ibm_temporal_score_total)))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 4. EL IMPACTO DE CONFIDENCIALIDAD VIENE ESPECIFICADO EN EL "+str(float(((ibm_temporal_score_4_confimpact_iot*100)/ibm_temporal_score_4_iot)))+" % DE ELLAS. LOS PORCENTAJES DE IMPACTO DE CONFIDENCIALIDAD SON LOS SIGUIENTES :  \n")
    print("            -    EN EL  "+str(float(((ibm_temporal_score_4_high_confimpact_iot*100)/ibm_temporal_score_4_confimpact_iot)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
    print("            -    EN EL  "+str(float(((ibm_temporal_score_4_low_confimpact_iot*100)/ibm_temporal_score_4_confimpact_iot)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
    print("            -    EN EL  "+str(float(((ibm_temporal_score_4_medium_confimpact_iot*100)/ibm_temporal_score_4_confimpact_iot)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO \n")
    print("\n")
if(ibm_temporal_score_3_confimpact_iot>0):
    print("      -    EN EL  "+str(float(((ibm_temporal_score_3_iot*100)/ibm_temporal_score_total)))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 3. EL IMPACTO DE CONFIDENCIALIDAD VIENE ESPECIFICADO EN EL "+str(float(((ibm_temporal_score_3_confimpact_iot*100)/ibm_temporal_score_3_iot)))+" % DE ELLAS. LOS PORCENTAJES DE IMPACTO DE CONFIDENCIALIDAD SON LOS SIGUIENTES :  \n")
    print("            -    EN EL  "+str(float(((ibm_temporal_score_3_high_confimpact_iot*100)/ibm_temporal_score_3_confimpact_iot)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
    print("            -    EN EL  "+str(float(((ibm_temporal_score_3_low_confimpact_iot*100)/ibm_temporal_score_3_confimpact_iot)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
    print("            -    EN EL  "+str(float(((ibm_temporal_score_3_medium_confimpact_iot*100)/ibm_temporal_score_3_confimpact_iot)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO \n")
    print("\n")
if(ibm_temporal_score_2_confimpact_iot>0):
    print("      -    EN EL  "+str(float(((ibm_temporal_score_2_iot*100)/ibm_temporal_score_total)))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 2. EL IMPACTO DE CONFIDENCIALIDAD VIENE ESPECIFICADO EN EL "+str(float(((ibm_temporal_score_2_confimpact_iot*100)/ibm_temporal_score_2_iot)))+" % DE ELLAS. LOS PORCENTAJES DE IMPACTO DE CONFIDENCIALIDAD SON LOS SIGUIENTES :  \n")
    print("            -    EN EL  "+str(float(((ibm_temporal_score_2_high_confimpact_iot*100)/ibm_temporal_score_2_confimpact_iot)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
    print("            -    EN EL  "+str(float(((ibm_temporal_score_2_low_confimpact_iot*100)/ibm_temporal_score_2_confimpact_iot)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
    print("            -    EN EL  "+str(float(((ibm_temporal_score_2_medium_confimpact_iot*100)/ibm_temporal_score_2_confimpact_iot)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO \n")
    print("\n")
if(ibm_temporal_score_1_confimpact_iot>0):
    print("      -    EN EL  "+str(float(((ibm_temporal_score_1_iot*100)/ibm_temporal_score_total)))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 1. EL IMPACTO DE CONFIDENCIALIDAD VIENE ESPECIFICADO EN EL "+str(float(((ibm_temporal_score_1_confimpact_iot*100)/ibm_temporal_score_1_iot)))+" % DE ELLAS. LOS PORCENTAJES DE IMPACTO DE CONFIDENCIALIDAD SON LOS SIGUIENTES :  \n")
    print("            -    EN EL  "+str(float(((ibm_temporal_score_1_high_confimpact_iot*100)/ibm_temporal_score_1_confimpact_iot)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
    print("            -    EN EL  "+str(float(((ibm_temporal_score_1_low_confimpact_iot*100)/ibm_temporal_score_1_confimpact_iot)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
    print("            -    EN EL  "+str(float(((ibm_temporal_score_1_medium_confimpact_iot*100)/ibm_temporal_score_1_confimpact_iot)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO \n")
    print("\n")
if(ibm_temporal_score_0_confimpact_iot>0):
    print("      -    EN EL  "+str(float(((ibm_temporal_score_0_iot*100)/ibm_temporal_score_total)))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 0. EL IMPACTO DE CONFIDENCIALIDAD VIENE ESPECIFICADO EN EL "+str(float(((ibm_temporal_score_0_confimpact_iot*100)/ibm_temporal_score_0_iot)))+" % DE ELLAS. LOS PORCENTAJES DE IMPACTO DE CONFIDENCIALIDAD SON LOS SIGUIENTES :  \n")
    print("            -    EN EL  "+str(float(((ibm_temporal_score_0_high_confimpact_iot*100)/ibm_temporal_score_0_confimpact_iot)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
    print("            -    EN EL  "+str(float(((ibm_temporal_score_0_low_confimpact_iot*100)/ibm_temporal_score_0_confimpact_iot)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
    print("            -    EN EL  "+str(float(((ibm_temporal_score_0_medium_confimpact_iot*100)/ibm_temporal_score_0_confimpact_iot)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO \n")
    print("\n")

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

#Abro los ficheros con los que voy a tratar




df_vulnibm_sh = pd.read_excel('vulnerabilidades_ibm_smart_home_2023.xlsx')

#Variables donde almacenare el contador de puntuacion temporal especifico de IBM para SMART HOME
ibm_temporal_score_9_sh=0
#Variables donde almacenare el contador de impacto de confidencialidad dado un valor especifico de puntuacion temporal
ibm_temporal_score_9_high_confimpact_sh=0
ibm_temporal_score_9_low_confimpact_sh=0
ibm_temporal_score_9_medium_confimpact_sh=0
ibm_temporal_score_9_confimpact_sh=0

ibm_temporal_score_8_sh=0
ibm_temporal_score_8_high_confimpact_sh=0
ibm_temporal_score_8_low_confimpact_sh=0
ibm_temporal_score_8_medium_confimpact_sh=0
ibm_temporal_score_8_confimpact_sh=0

ibm_temporal_score_7_sh=0
ibm_temporal_score_7_high_confimpact_sh=0
ibm_temporal_score_7_low_confimpact_sh=0
ibm_temporal_score_7_medium_confimpact_sh=0
ibm_temporal_score_7_confimpact_sh=0

ibm_temporal_score_6_sh=0
ibm_temporal_score_6_high_confimpact_sh=0
ibm_temporal_score_6_low_confimpact_sh=0
ibm_temporal_score_6_medium_confimpact_sh=0
ibm_temporal_score_6_confimpact_sh=0

ibm_temporal_score_5_sh=0
ibm_temporal_score_5_high_confimpact_sh=0
ibm_temporal_score_5_low_confimpact_sh=0
ibm_temporal_score_5_medium_confimpact_sh=0
ibm_temporal_score_5_confimpact_sh=0


ibm_temporal_score_4_sh=0
ibm_temporal_score_4_high_confimpact_sh=0
ibm_temporal_score_4_low_confimpact_sh=0
ibm_temporal_score_4_medium_confimpact_sh=0
ibm_temporal_score_4_confimpact_sh=0


ibm_temporal_score_3_sh=0
ibm_temporal_score_3_high_confimpact_sh=0
ibm_temporal_score_3_low_confimpact_sh=0
ibm_temporal_score_3_medium_confimpact_sh=0
ibm_temporal_score_3_confimpact_sh=0


ibm_temporal_score_2_sh=0
ibm_temporal_score_2_high_confimpact_sh=0
ibm_temporal_score_2_low_confimpact_sh=0
ibm_temporal_score_2_medium_confimpact_sh=0
ibm_temporal_score_2_confimpact_sh=0


ibm_temporal_score_1_sh=0
ibm_temporal_score_1_high_confimpact_sh=0
ibm_temporal_score_1_low_confimpact_sh=0
ibm_temporal_score_1_medium_confimpact_sh=0
ibm_temporal_score_1_confimpact_sh=0

ibm_temporal_score_0_sh=0
ibm_temporal_score_0_high_confimpact_sh=0
ibm_temporal_score_0_low_confimpact_sh=0
ibm_temporal_score_0_medium_confimpact_sh=0
ibm_temporal_score_0_confimpact_sh=0


ibm_temporal_score_10_sh=0
ibm_temporal_score_10_high_confimpact_sh=0
ibm_temporal_score_10_low_confimpact_sh=0
ibm_temporal_score_10_medium_confimpact_sh=0
ibm_temporal_score_10_confimpact_sh=0

ibm_temporal_score_total_sh=0



#Compruebo la puntuacion temporal en IBM para SMART HOME

for r in range(0,len(df_vulnibm_sh["x_xfe_temporal_score"])):
    #Compruebo la puntuacion temporal
    if(df_vulnibm_sh["x_xfe_temporal_score"][r]!='NONE'):
        if(((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) < 10.0) and ((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) >=9.0)):
            ibm_temporal_score_9_sh+=1
            ibm_temporal_score_total_sh+=1
            #Compruebo el impacto de confidencialidad
            if(df_vulnibm_sh["x_xfe_cvss_confidentiality_impact"][r]=='High'):
                ibm_temporal_score_9_confimpact_sh+=1
                ibm_temporal_score_9_high_confimpact_sh+=1
            elif(df_vulnibm_sh["x_xfe_cvss_confidentiality_impact"][r]=='Low'):
                ibm_temporal_score_9_confimpact_sh+=1
                ibm_temporal_score_9_low_confimpact_sh+=1
            elif(df_vulnibm_sh["x_xfe_cvss_confidentiality_impact"][r]=='Medium'):
                ibm_temporal_score_9_confimpact_sh+=1
                ibm_temporal_score_9_medium_confimpact_sh+=1

        elif(((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) < 9.0) and ((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) >=8.0)):
            ibm_temporal_score_8_sh+=1
            ibm_temporal_score_total_sh+=1
            if(df_vulnibm_sh["x_xfe_cvss_confidentiality_impact"][r]=='High'):
                ibm_temporal_score_8_confimpact_sh+=1
                ibm_temporal_score_8_high_confimpact_sh+=1
            elif(df_vulnibm_sh["x_xfe_cvss_confidentiality_impact"][r]=='Low'):
                ibm_temporal_score_8_confimpact_sh+=1
                ibm_temporal_score_8_low_confimpact_sh+=1
            elif(df_vulnibm_sh["x_xfe_cvss_confidentiality_impact"][r]=='Medium'):
                ibm_temporal_score_8_confimpact_sh+=1
                ibm_temporal_score_8_medium_confimpact_sh+=1
        elif(((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) < 8.0) and ((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) >=7.0)):
            ibm_temporal_score_7_sh+=1
            ibm_temporal_score_total_sh+=1
            if(df_vulnibm_sh["x_xfe_cvss_confidentiality_impact"][r]=='High'):
                ibm_temporal_score_7_confimpact_sh+=1
                ibm_temporal_score_7_high_confimpact_sh+=1
            elif(df_vulnibm_sh["x_xfe_cvss_confidentiality_impact"][r]=='Low'):
                ibm_temporal_score_7_confimpact_sh+=1
                ibm_temporal_score_7_low_confimpact_sh+=1
            elif(df_vulnibm_sh["x_xfe_cvss_confidentiality_impact"][r]=='Medium'):
                ibm_temporal_score_7_confimpact_sh+=1
                ibm_temporal_score_7_medium_confimpact_sh+=1
        elif(((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) < 7.0) and ((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) >=6.0)):
            ibm_temporal_score_6_sh+=1
            ibm_temporal_score_total_sh+=1
            if(df_vulnibm_sh["x_xfe_cvss_confidentiality_impact"][r]=='High'):
                ibm_temporal_score_6_confimpact_sh+=1
                ibm_temporal_score_6_high_confimpact_sh+=1
            elif(df_vulnibm_sh["x_xfe_cvss_confidentiality_impact"][r]=='Low'):
                ibm_temporal_score_6_confimpact_sh+=1
                ibm_temporal_score_6_low_confimpact_sh+=1
            elif(df_vulnibm_sh["x_xfe_cvss_confidentiality_impact"][r]=='Medium'):
                ibm_temporal_score_6_confimpact_sh+=1
                ibm_temporal_score_6_medium_confimpact_sh+=1
        elif(((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) < 6.0) and ((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) >=5.0)):
            ibm_temporal_score_5_sh+=1
            ibm_temporal_score_total_sh+=1
            if(df_vulnibm_sh["x_xfe_cvss_confidentiality_impact"][r]=='High'):
                ibm_temporal_score_5_confimpact_sh+=1
                ibm_temporal_score_5_high_confimpact_sh+=1
            elif(df_vulnibm_sh["x_xfe_cvss_confidentiality_impact"][r]=='Low'):
                ibm_temporal_score_5_confimpact_sh+=1
                ibm_temporal_score_5_low_confimpact_sh+=1
            elif(df_vulnibm_sh["x_xfe_cvss_confidentiality_impact"][r]=='Medium'):
                ibm_temporal_score_5_confimpact_sh+=1
                ibm_temporal_score_5_medium_confimpact_sh+=1
        elif(((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) < 5.0) and ((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) >=4.0)):
            ibm_temporal_score_4_sh+=1
            ibm_temporal_score_total_sh+=1
            if(df_vulnibm_sh["x_xfe_cvss_confidentiality_impact"][r]=='High'):
                ibm_temporal_score_4_confimpact_sh+=1
                ibm_temporal_score_4_high_confimpact_sh+=1
            elif(df_vulnibm_sh["x_xfe_cvss_confidentiality_impact"][r]=='Low'):
                ibm_temporal_score_4_confimpact_sh+=1
                ibm_temporal_score_4_low_confimpact_sh+=1
            elif(df_vulnibm_sh["x_xfe_cvss_confidentiality_impact"][r]=='Medium'):
                ibm_temporal_score_4_confimpact_sh+=1
                ibm_temporal_score_4_medium_confimpact_sh+=1
        elif(((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) < 4.0) and ((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) >=3.0)):
            ibm_temporal_score_3_sh+=1
            ibm_temporal_score_total_sh+=1
            if(df_vulnibm_sh["x_xfe_cvss_confidentiality_impact"][r]=='High'):
                ibm_temporal_score_3_confimpact_sh+=1
                ibm_temporal_score_3_high_confimpact_sh+=1
            elif(df_vulnibm_sh["x_xfe_cvss_confidentiality_impact"][r]=='Low'):
                ibm_temporal_score_3_confimpact_sh+=1
                ibm_temporal_score_3_low_confimpact_sh+=1
            elif(df_vulnibm_sh["x_xfe_cvss_confidentiality_impact"][r]=='Medium'):
                ibm_temporal_score_3_confimpact_sh+=1
                ibm_temporal_score_3_medium_confimpact_sh+=1
        elif(((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) < 3.0) and ((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) >=2.0)):
            ibm_temporal_score_2_sh+=1
            ibm_temporal_score_total_sh+=1
            if(df_vulnibm_sh["x_xfe_cvss_confidentiality_impact"][r]=='High'):
                ibm_temporal_score_2_confimpact_sh+=1
                ibm_temporal_score_2_high_confimpact_sh+=1
            elif(df_vulnibm_sh["x_xfe_cvss_confidentiality_impact"][r]=='Low'):
                ibm_temporal_score_2_confimpact_sh+=1
                ibm_temporal_score_2_low_confimpact_sh+=1
            elif(df_vulnibm_sh["x_xfe_cvss_confidentiality_impact"][r]=='Medium'):
                ibm_temporal_score_2_confimpact_sh+=1
                ibm_temporal_score_2_medium_confimpact_sh+=1
        elif(((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) < 2.0) and ((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) >=1.0)):
            ibm_temporal_score_1_sh+=1
            ibm_temporal_score_total_sh+=1
            if(df_vulnibm_sh["x_xfe_cvss_confidentiality_impact"][r]=='High'):
                ibm_temporal_score_1_confimpact_sh+=1
                ibm_temporal_score_1_high_confimpact_sh+=1
            elif(df_vulnibm_sh["x_xfe_cvss_confidentiality_impact"][r]=='Low'):
                ibm_temporal_score_1_confimpact_sh+=1
                ibm_temporal_score_1_low_confimpact_sh+=1
            elif(df_vulnibm_sh["x_xfe_cvss_confidentiality_impact"][r]=='Medium'):
                ibm_temporal_score_1_confimpact_sh+=1
                ibm_temporal_score_1_medium_confimpact_sh+=1
        elif(((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) < 1.0) and ((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) >=0.0)):
            ibm_temporal_score_0_sh+=0
            ibm_temporal_score_total_sh+=0
            if(df_vulnibm_sh["x_xfe_cvss_confidentiality_impact"][r]=='High'):
                ibm_temporal_score_0_confimpact_sh+=0
                ibm_temporal_score_0_high_confimpact_sh+=0
            elif(df_vulnibm_sh["x_xfe_cvss_confidentiality_impact"][r]=='Low'):
                ibm_temporal_score_0_confimpact_sh+=0
                ibm_temporal_score_0_low_confimpact_sh+=0
            elif(df_vulnibm_sh["x_xfe_cvss_confidentiality_impact"][r]=='Medium'):
                ibm_temporal_score_0_confimpact_sh+=0
                ibm_temporal_score_0_medium_confimpact_sh+=0
        elif(((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) == 10.0)):
            ibm_temporal_score_10_sh+=0
            ibm_temporal_score_total_sh+=0
            if(df_vulnibm_sh["x_xfe_cvss_confidentiality_impact"][r]=='High'):
                ibm_temporal_score_10_confimpact_sh+=0
                ibm_temporal_score_10_high_confimpact_sh+=0
            elif(df_vulnibm_sh["x_xfe_cvss_confidentiality_impact"][r]=='Low'):
                ibm_temporal_score_10_confimpact_sh+=0
                ibm_temporal_score_10_low_confimpact_sh+=0
            elif(df_vulnibm_sh["x_xfe_cvss_confidentiality_impact"][r]=='Medium'):
                ibm_temporal_score_10_confimpact_sh+=0
                ibm_temporal_score_10_medium_confimpact_sh+=0
            
            
print("*********************ESTADÍSTICAS PUNTUACION TEMPORAL/IMPACTO DE CONFIDENCIALIDAD VULNERABILIDADES IBM PARTE SMART HOME*********************")
print("\n")                            
print("\n")
print(" DE UN TOTAL DE "+str(ibm_temporal_score_total_sh)+" VULNERABILIDADES:\n") 
print("\n")
print("   - LAS ESTADISTICAS DE VALORES DE PUNTUACION TEMPORAL SON LAS SIGUIENTES:  \n")
print("      -    EN  "+str(ibm_temporal_score_10_sh)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES 10. EL IMPACTO DE CONFIDENCIALIDAD VIENE ESPECIFICADO EN "+str(ibm_temporal_score_10_confimpact_sh)+" VULNERABILIDADES. LAS ESTADÍSTICAS DE IMPACTO DE CONFIDENCIALIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(ibm_temporal_score_10_high_confimpact_sh)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
print("            -    EN  "+str(ibm_temporal_score_10_low_confimpact_sh)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
print("            -    EN  "+str(ibm_temporal_score_10_medium_confimpact_sh)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO \n")
print("      -    EN  "+str(ibm_temporal_score_9_sh)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 9. EL IMPACTO DE CONFIDENCIALIDAD VIENE ESPECIFICADO EN "+str(ibm_temporal_score_9_confimpact_sh)+" VULNERABILIDADES. LAS ESTADÍSTICAS DE IMPACTO DE CONFIDENCIALIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(ibm_temporal_score_9_high_confimpact_sh)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
print("            -    EN  "+str(ibm_temporal_score_9_low_confimpact_sh)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
print("            -    EN  "+str(ibm_temporal_score_9_medium_confimpact_sh)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO \n")
print("      -    EN  "+str(ibm_temporal_score_8_sh)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 8. EL IMPACTO DE CONFIDENCIALIDAD VIENE ESPECIFICADO EN "+str(ibm_temporal_score_8_confimpact_sh)+" VULNERABILIDADES. LAS ESTADÍSTICAS DE IMPACTO DE CONFIDENCIALIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(ibm_temporal_score_8_high_confimpact_sh)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
print("            -    EN  "+str(ibm_temporal_score_8_low_confimpact_sh)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
print("            -    EN  "+str(ibm_temporal_score_8_medium_confimpact_sh)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO \n")
print("      -    EN  "+str(ibm_temporal_score_7_sh)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 7. EL IMPACTO DE CONFIDENCIALIDAD VIENE ESPECIFICADO EN "+str(ibm_temporal_score_7_confimpact_sh)+" VULNERABILIDADES. LAS ESTADÍSTICAS DE IMPACTO DE CONFIDENCIALIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(ibm_temporal_score_7_high_confimpact_sh)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
print("            -    EN  "+str(ibm_temporal_score_7_low_confimpact_sh)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
print("            -    EN  "+str(ibm_temporal_score_7_medium_confimpact_sh)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO \n")
print("      -    EN  "+str(ibm_temporal_score_6_sh)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 6. EL IMPACTO DE CONFIDENCIALIDAD VIENE ESPECIFICADO EN "+str(ibm_temporal_score_6_confimpact_sh)+" VULNERABILIDADES. LAS ESTADÍSTICAS DE IMPACTO DE CONFIDENCIALIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(ibm_temporal_score_6_high_confimpact_sh)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
print("            -    EN  "+str(ibm_temporal_score_6_low_confimpact_sh)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
print("            -    EN  "+str(ibm_temporal_score_6_medium_confimpact_sh)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO \n")
print("      -    EN  "+str(ibm_temporal_score_5_sh)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 5. EL IMPACTO DE CONFIDENCIALIDAD VIENE ESPECIFICADO EN "+str(ibm_temporal_score_5_confimpact_sh)+" VULNERABILIDADES. LAS ESTADÍSTICAS DE IMPACTO DE CONFIDENCIALIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(ibm_temporal_score_5_high_confimpact_sh)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
print("            -    EN  "+str(ibm_temporal_score_5_low_confimpact_sh)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
print("            -    EN  "+str(ibm_temporal_score_5_medium_confimpact_sh)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO \n")
print("      -    EN  "+str(ibm_temporal_score_4_sh)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 4. EL IMPACTO DE CONFIDENCIALIDAD VIENE ESPECIFICADO EN "+str(ibm_temporal_score_4_confimpact_sh)+" VULNERABILIDADES. LAS ESTADÍSTICAS DE IMPACTO DE CONFIDENCIALIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(ibm_temporal_score_4_high_confimpact_sh)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
print("            -    EN  "+str(ibm_temporal_score_4_low_confimpact_sh)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
print("            -    EN  "+str(ibm_temporal_score_4_medium_confimpact_sh)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO \n")
print("      -    EN  "+str(ibm_temporal_score_3_sh)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 3. EL IMPACTO DE CONFIDENCIALIDAD VIENE ESPECIFICADO EN "+str(ibm_temporal_score_3_confimpact_sh)+" VULNERABILIDADES. LAS ESTADÍSTICAS DE IMPACTO DE CONFIDENCIALIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(ibm_temporal_score_3_high_confimpact_sh)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
print("            -    EN  "+str(ibm_temporal_score_3_low_confimpact_sh)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
print("            -    EN  "+str(ibm_temporal_score_3_medium_confimpact_sh)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO \n")
print("      -    EN  "+str(ibm_temporal_score_2_sh)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 2. EL IMPACTO DE CONFIDENCIALIDAD VIENE ESPECIFICADO EN "+str(ibm_temporal_score_2_confimpact_sh)+" VULNERABILIDADES. LAS ESTADÍSTICAS DE IMPACTO DE CONFIDENCIALIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(ibm_temporal_score_2_high_confimpact_sh)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
print("            -    EN  "+str(ibm_temporal_score_2_low_confimpact_sh)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
print("            -    EN  "+str(ibm_temporal_score_2_medium_confimpact_sh)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO \n")
print("      -    EN  "+str(ibm_temporal_score_1_sh)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 1. EL IMPACTO DE CONFIDENCIALIDAD VIENE ESPECIFICADO EN "+str(ibm_temporal_score_1_confimpact_sh)+" VULNERABILIDADES. LAS ESTADÍSTICAS DE IMPACTO DE CONFIDENCIALIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(ibm_temporal_score_1_high_confimpact_sh)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
print("            -    EN  "+str(ibm_temporal_score_1_low_confimpact_sh)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
print("            -    EN  "+str(ibm_temporal_score_1_medium_confimpact_sh)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO \n")
print("      -    EN  "+str(ibm_temporal_score_0_sh)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 0. EL IMPACTO DE CONFIDENCIALIDAD VIENE ESPECIFICADO EN "+str(ibm_temporal_score_0_confimpact_sh)+" VULNERABILIDADES. LAS ESTADÍSTICAS DE IMPACTO DE CONFIDENCIALIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(ibm_temporal_score_0_high_confimpact_sh)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
print("            -    EN  "+str(ibm_temporal_score_0_low_confimpact_sh)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
print("            -    EN  "+str(ibm_temporal_score_0_medium_confimpact_sh)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO \n")






print("*********************PORCENTAJE PUNTUACION TEMPORAL/IMPACTO DE CONFIDENCIALIDAD VULNERABILIDADES IBM SMART HOME*********************")
print("\n")                            
print("\n")
print(" DE UN TOTAL DE "+str(ibm_temporal_score_total_sh)+" VULNERABILIDADES :\n") 
print("\n")
print("   - LOS PORCENTAJES DE VALORES DE PUNTUACION TEMPORAL SON LOS SIGUIENTES:  \n")
if(ibm_temporal_score_10_confimpact_sh>0):
    print("      -    EN EL  "+str(float(((ibm_temporal_score_10_sh*100)/ibm_temporal_score_total_sh)))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES 10. EL IMPACTO DE CONFIDENCIALIDAD VIENE ESPECIFICADO EN EL "+str(float(((ibm_temporal_score_10_confimpact_sh*100)/ibm_temporal_score_10_sh)))+" % DE ELLAS. LOS PORCENTAJES DE IMPACTO DE CONFIDENCIALIDAD SON LOS SIGUIENTES :  \n")
    print("            -    EN EL  "+str(float(((ibm_temporal_score_10_high_confimpact_sh*100)/ibm_temporal_score_10_confimpact_sh)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
    print("            -    EN EL  "+str(float(((ibm_temporal_score_10_low_confimpact_sh*100)/ibm_temporal_score_10_confimpact_sh)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
    print("            -    EN EL  "+str(float(((ibm_temporal_score_10_medium_confimpact_sh*100)/ibm_temporal_score_10_confimpact_sh)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO \n")
    print("\n")
if(ibm_temporal_score_9_confimpact_sh>0):
    print("      -    EN EL  "+str(float(((ibm_temporal_score_9_sh*100)/ibm_temporal_score_total_sh)))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 9. EL IMPACTO DE CONFIDENCIALIDAD VIENE ESPECIFICADO EN EL "+str(float(((ibm_temporal_score_9_confimpact_sh*100)/ibm_temporal_score_9_sh)))+" % DE ELLAS. LOS PORCENTAJES DE IMPACTO DE CONFIDENCIALIDAD SON LOS SIGUIENTES :  :  \n")
    print("            -    EN EL  "+str(float(((ibm_temporal_score_9_high_confimpact_sh*100)/ibm_temporal_score_9_confimpact_sh)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
    print("            -    EN EL  "+str(float(((ibm_temporal_score_9_low_confimpact_sh*100)/ibm_temporal_score_9_confimpact_sh)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
    print("            -    EN EL  "+str(float(((ibm_temporal_score_9_medium_confimpact_sh*100)/ibm_temporal_score_9_confimpact_sh)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO \n")
    print("\n")
if(ibm_temporal_score_8_confimpact_sh>0):
    print("      -    EN EL  "+str(float(((ibm_temporal_score_8_sh*100)/ibm_temporal_score_total_sh)))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 8. EL IMPACTO DE CONFIDENCIALIDAD VIENE ESPECIFICADO EN EL "+str(float(((ibm_temporal_score_8_confimpact_sh*100)/ibm_temporal_score_8_sh)))+" % DE ELLAS. LOS PORCENTAJES DE IMPACTO DE CONFIDENCIALIDAD SON LOS SIGUIENTES :  :  \n")
    print("            -    EN EL  "+str(float(((ibm_temporal_score_8_high_confimpact_sh*100)/ibm_temporal_score_8_confimpact_sh)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
    print("            -    EN EL  "+str(float(((ibm_temporal_score_8_low_confimpact_sh*100)/ibm_temporal_score_8_confimpact_sh)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
    print("            -    EN EL  "+str(float(((ibm_temporal_score_8_medium_confimpact_sh*100)/ibm_temporal_score_8_confimpact_sh)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO \n")
    print("\n")
if(ibm_temporal_score_7_confimpact_sh>0):
    print("      -    EN EL  "+str(float(((ibm_temporal_score_7_sh*100)/ibm_temporal_score_total_sh)))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 7. EL IMPACTO DE CONFIDENCIALIDAD VIENE ESPECIFICADO EN EL "+str(float(((ibm_temporal_score_7_confimpact_sh*100)/ibm_temporal_score_7_sh)))+" % DE ELLAS. LOS PORCENTAJES DE IMPACTO DE CONFIDENCIALIDAD SON LOS SIGUIENTES :  :  \n")
    print("            -    EN EL  "+str(float(((ibm_temporal_score_7_high_confimpact_sh*100)/ibm_temporal_score_7_confimpact_sh)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
    print("            -    EN EL  "+str(float(((ibm_temporal_score_7_low_confimpact_sh*100)/ibm_temporal_score_7_confimpact_sh)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
    print("            -    EN EL  "+str(float(((ibm_temporal_score_7_medium_confimpact_sh*100)/ibm_temporal_score_7_confimpact_sh)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO \n")
    print("\n")
if(ibm_temporal_score_6_confimpact_sh>0):
    print("      -    EN EL  "+str(float(((ibm_temporal_score_6_sh*100)/ibm_temporal_score_total_sh)))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 6. EL IMPACTO DE CONFIDENCIALIDAD VIENE ESPECIFICADO EN EL "+str(float(((ibm_temporal_score_6_confimpact_sh*100)/ibm_temporal_score_6_sh)))+" % DE ELLAS. LOS PORCENTAJES DE IMPACTO DE CONFIDENCIALIDAD SON LOS SIGUIENTES :  \n")
    print("            -    EN EL  "+str(float(((ibm_temporal_score_6_high_confimpact_sh*100)/ibm_temporal_score_6_confimpact_sh)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
    print("            -    EN EL  "+str(float(((ibm_temporal_score_6_low_confimpact_sh*100)/ibm_temporal_score_6_confimpact_sh)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
    print("            -    EN EL  "+str(float(((ibm_temporal_score_6_medium_confimpact_sh*100)/ibm_temporal_score_6_confimpact_sh)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO \n")
    print("\n")
if(ibm_temporal_score_5_confimpact_sh>0):
    print("      -    EN EL  "+str(float(((ibm_temporal_score_5_sh*100)/ibm_temporal_score_total_sh)))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 5. EL IMPACTO DE CONFIDENCIALIDAD VIENE ESPECIFICADO EN EL "+str(float(((ibm_temporal_score_5_confimpact_sh*100)/ibm_temporal_score_5_sh)))+" % DE ELLAS. LOS PORCENTAJES DE IMPACTO DE CONFIDENCIALIDAD SON LOS SIGUIENTES :  \n")
    print("            -    EN EL  "+str(float(((ibm_temporal_score_5_high_confimpact_sh*100)/ibm_temporal_score_5_confimpact_sh)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
    print("            -    EN EL  "+str(float(((ibm_temporal_score_5_low_confimpact_sh*100)/ibm_temporal_score_5_confimpact_sh)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
    print("            -    EN EL  "+str(float(((ibm_temporal_score_5_medium_confimpact_sh*100)/ibm_temporal_score_5_confimpact_sh)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO \n")
    print("\n")
if(ibm_temporal_score_4_confimpact_sh>0):
    print("      -    EN EL  "+str(float(((ibm_temporal_score_4_sh*100)/ibm_temporal_score_total_sh)))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 4. EL IMPACTO DE CONFIDENCIALIDAD VIENE ESPECIFICADO EN EL "+str(float(((ibm_temporal_score_4_confimpact_sh*100)/ibm_temporal_score_4_sh)))+" % DE ELLAS. LOS PORCENTAJES DE IMPACTO DE CONFIDENCIALIDAD SON LOS SIGUIENTES :  \n")
    print("            -    EN EL  "+str(float(((ibm_temporal_score_4_high_confimpact_sh*100)/ibm_temporal_score_4_confimpact_sh)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
    print("            -    EN EL  "+str(float(((ibm_temporal_score_4_low_confimpact_sh*100)/ibm_temporal_score_4_confimpact_sh)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
    print("            -    EN EL  "+str(float(((ibm_temporal_score_4_medium_confimpact_sh*100)/ibm_temporal_score_4_confimpact_sh)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO \n")
    print("\n")
if(ibm_temporal_score_3_confimpact_sh>0):
    print("      -    EN EL  "+str(float(((ibm_temporal_score_3_sh*100)/ibm_temporal_score_total_sh)))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 3. EL IMPACTO DE CONFIDENCIALIDAD VIENE ESPECIFICADO EN EL "+str(float(((ibm_temporal_score_3_confimpact_sh*100)/ibm_temporal_score_3_sh)))+" % DE ELLAS. LOS PORCENTAJES DE IMPACTO DE CONFIDENCIALIDAD SON LOS SIGUIENTES :  \n")
    print("            -    EN EL  "+str(float(((ibm_temporal_score_3_high_confimpact_sh*100)/ibm_temporal_score_3_confimpact_sh)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
    print("            -    EN EL  "+str(float(((ibm_temporal_score_3_low_confimpact_sh*100)/ibm_temporal_score_3_confimpact_sh)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
    print("            -    EN EL  "+str(float(((ibm_temporal_score_3_medium_confimpact_sh*100)/ibm_temporal_score_3_confimpact_sh)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO \n")
    print("\n")
if(ibm_temporal_score_2_confimpact_sh>0):
    print("      -    EN EL  "+str(float(((ibm_temporal_score_2_sh*100)/ibm_temporal_score_total_sh)))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 2. EL IMPACTO DE CONFIDENCIALIDAD VIENE ESPECIFICADO EN EL "+str(float(((ibm_temporal_score_2_confimpact_sh*100)/ibm_temporal_score_2_sh)))+" % DE ELLAS. LOS PORCENTAJES DE IMPACTO DE CONFIDENCIALIDAD SON LOS SIGUIENTES :  \n")
    print("            -    EN EL  "+str(float(((ibm_temporal_score_2_high_confimpact_sh*100)/ibm_temporal_score_2_confimpact_sh)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
    print("            -    EN EL  "+str(float(((ibm_temporal_score_2_low_confimpact_sh*100)/ibm_temporal_score_2_confimpact_sh)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
    print("            -    EN EL  "+str(float(((ibm_temporal_score_2_medium_confimpact_sh*100)/ibm_temporal_score_2_confimpact_sh)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO \n")
    print("\n")
if(ibm_temporal_score_1_confimpact_sh>0):
    print("      -    EN EL  "+str(float(((ibm_temporal_score_1_sh*100)/ibm_temporal_score_total_sh)))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 1. EL IMPACTO DE CONFIDENCIALIDAD VIENE ESPECIFICADO EN EL "+str(float(((ibm_temporal_score_1_confimpact_sh*100)/ibm_temporal_score_1_sh)))+" % DE ELLAS. LOS PORCENTAJES DE IMPACTO DE CONFIDENCIALIDAD SON LOS SIGUIENTES :  \n")
    print("            -    EN EL  "+str(float(((ibm_temporal_score_1_high_confimpact_sh*100)/ibm_temporal_score_1_confimpact_sh)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
    print("            -    EN EL  "+str(float(((ibm_temporal_score_1_low_confimpact_sh*100)/ibm_temporal_score_1_confimpact_sh)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
    print("            -    EN EL  "+str(float(((ibm_temporal_score_1_medium_confimpact_sh*100)/ibm_temporal_score_1_confimpact_sh)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO \n")
    print("\n")
if(ibm_temporal_score_0_confimpact_sh>0):
    print("      -    EN EL  "+str(float(((ibm_temporal_score_0_sh*100)/ibm_temporal_score_total_sh)))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 0. EL IMPACTO DE CONFIDENCIALIDAD VIENE ESPECIFICADO EN EL "+str(float(((ibm_temporal_score_0_confimpact_sh*100)/ibm_temporal_score_0_sh)))+" % DE ELLAS. LOS PORCENTAJES DE IMPACTO DE CONFIDENCIALIDAD SON LOS SIGUIENTES :  \n")
    print("            -    EN EL  "+str(float(((ibm_temporal_score_0_high_confimpact_sh*100)/ibm_temporal_score_0_confimpact_sh)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
    print("            -    EN EL  "+str(float(((ibm_temporal_score_0_low_confimpact_sh*100)/ibm_temporal_score_0_confimpact_sh)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
    print("            -    EN EL  "+str(float(((ibm_temporal_score_0_medium_confimpact_sh*100)/ibm_temporal_score_0_confimpact_sh)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO \n")
    print("\n")

    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
                
            
            
            
            
            
            
            
            

    
print("*********************ESTADÍSTICAS PUNTUACION TEMPORAL/IMPACTO DE CONFIDENCIALIDAD VULNERABILIDADES IBM PARTE IOT Y SMART HOME CONJUNTAS*********************")
print("\n")                            
print("\n")
print(" DE UN TOTAL DE "+str(ibm_temporal_score_total_sh+ibm_temporal_score_total)+" VULNERABILIDADES:\n") 
print("\n")
print("   - LAS ESTADISTICAS DE VALORES DE PUNTUACION TEMPORAL SON LAS SIGUIENTES:  \n")
print("      -    EN  "+str(ibm_temporal_score_10_sh+ibm_temporal_score_10_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES 10. EL IMPACTO DE CONFIDENCIALIDAD VIENE ESPECIFICADO EN "+str(ibm_temporal_score_10_confimpact_sh+ibm_temporal_score_10_confimpact_iot)+" VULNERABILIDADES. LAS ESTADÍSTICAS DE IMPACTO DE CONFIDENCIALIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(ibm_temporal_score_10_high_confimpact_sh+ibm_temporal_score_10_high_confimpact_iot)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
print("            -    EN  "+str(ibm_temporal_score_10_low_confimpact_sh+ibm_temporal_score_10_low_confimpact_iot)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
print("            -    EN  "+str(ibm_temporal_score_10_medium_confimpact_sh+ibm_temporal_score_10_medium_confimpact_iot)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO \n")
print("\n")
print("      -    EN  "+str(ibm_temporal_score_9_sh+ibm_temporal_score_9_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 9. EL IMPACTO DE CONFIDENCIALIDAD VIENE ESPECIFICADO EN "+str(ibm_temporal_score_9_confimpact_sh+ibm_temporal_score_9_confimpact_iot)+" VULNERABILIDADES. LAS ESTADÍSTICAS DE IMPACTO DE CONFIDENCIALIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(ibm_temporal_score_9_high_confimpact_sh+ibm_temporal_score_9_high_confimpact_iot)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
print("            -    EN  "+str(ibm_temporal_score_9_low_confimpact_sh+ibm_temporal_score_9_low_confimpact_iot)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
print("            -    EN  "+str(ibm_temporal_score_9_medium_confimpact_sh+ibm_temporal_score_9_medium_confimpact_iot)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO \n") 
print("\n")
print("      -    EN  "+str(ibm_temporal_score_8_sh+ibm_temporal_score_8_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 8. EL IMPACTO DE CONFIDENCIALIDAD VIENE ESPECIFICADO EN "+str(ibm_temporal_score_8_confimpact_sh+ibm_temporal_score_8_confimpact_iot)+" VULNERABILIDADES. LAS ESTADÍSTICAS DE IMPACTO DE CONFIDENCIALIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(ibm_temporal_score_8_high_confimpact_sh+ibm_temporal_score_8_high_confimpact_iot)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
print("            -    EN  "+str(ibm_temporal_score_8_low_confimpact_sh+ibm_temporal_score_8_low_confimpact_iot)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
print("            -    EN  "+str(ibm_temporal_score_8_medium_confimpact_sh+ibm_temporal_score_8_medium_confimpact_iot)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO \n") 
print("\n")
print("      -    EN  "+str(ibm_temporal_score_7_sh+ibm_temporal_score_7_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 7. EL IMPACTO DE CONFIDENCIALIDAD VIENE ESPECIFICADO EN "+str(ibm_temporal_score_7_confimpact_sh+ibm_temporal_score_7_confimpact_iot)+" VULNERABILIDADES. LAS ESTADÍSTICAS DE IMPACTO DE CONFIDENCIALIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(ibm_temporal_score_7_high_confimpact_sh+ibm_temporal_score_7_high_confimpact_iot)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
print("            -    EN  "+str(ibm_temporal_score_7_low_confimpact_sh+ibm_temporal_score_7_low_confimpact_iot)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
print("            -    EN  "+str(ibm_temporal_score_7_medium_confimpact_sh+ibm_temporal_score_7_medium_confimpact_iot)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO \n") 
print("\n")
print("      -    EN  "+str(ibm_temporal_score_6_sh+ibm_temporal_score_6_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 6. EL IMPACTO DE CONFIDENCIALIDAD VIENE ESPECIFICADO EN "+str(ibm_temporal_score_6_confimpact_sh+ibm_temporal_score_6_confimpact_iot)+" VULNERABILIDADES. LAS ESTADÍSTICAS DE IMPACTO DE CONFIDENCIALIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(ibm_temporal_score_6_high_confimpact_sh+ibm_temporal_score_6_high_confimpact_iot)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
print("            -    EN  "+str(ibm_temporal_score_6_low_confimpact_sh+ibm_temporal_score_6_low_confimpact_iot)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
print("            -    EN  "+str(ibm_temporal_score_6_medium_confimpact_sh+ibm_temporal_score_6_medium_confimpact_iot)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO \n") 
print("\n")
print("      -    EN  "+str(ibm_temporal_score_5_sh+ibm_temporal_score_5_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 5. EL IMPACTO DE CONFIDENCIALIDAD VIENE ESPECIFICADO EN "+str(ibm_temporal_score_5_confimpact_sh+ibm_temporal_score_5_confimpact_iot)+" VULNERABILIDADES. LAS ESTADÍSTICAS DE IMPACTO DE CONFIDENCIALIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(ibm_temporal_score_5_high_confimpact_sh+ibm_temporal_score_5_high_confimpact_iot)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
print("            -    EN  "+str(ibm_temporal_score_5_low_confimpact_sh+ibm_temporal_score_5_low_confimpact_iot)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
print("            -    EN  "+str(ibm_temporal_score_5_medium_confimpact_sh+ibm_temporal_score_5_medium_confimpact_iot)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO \n") 
print("\n")
print("      -    EN  "+str(ibm_temporal_score_4_sh+ibm_temporal_score_4_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 4. EL IMPACTO DE CONFIDENCIALIDAD VIENE ESPECIFICADO EN "+str(ibm_temporal_score_4_confimpact_sh+ibm_temporal_score_4_confimpact_iot)+" VULNERABILIDADES. LAS ESTADÍSTICAS DE IMPACTO DE CONFIDENCIALIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(ibm_temporal_score_4_high_confimpact_sh+ibm_temporal_score_4_high_confimpact_iot)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
print("            -    EN  "+str(ibm_temporal_score_4_low_confimpact_sh+ibm_temporal_score_4_low_confimpact_iot)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
print("            -    EN  "+str(ibm_temporal_score_4_medium_confimpact_sh+ibm_temporal_score_4_medium_confimpact_iot)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO \n") 
print("\n")
print("      -    EN  "+str(ibm_temporal_score_3_sh+ibm_temporal_score_3_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 3. EL IMPACTO DE CONFIDENCIALIDAD VIENE ESPECIFICADO EN "+str(ibm_temporal_score_3_confimpact_sh+ibm_temporal_score_3_confimpact_iot)+" VULNERABILIDADES. LAS ESTADÍSTICAS DE IMPACTO DE CONFIDENCIALIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(ibm_temporal_score_3_high_confimpact_sh+ibm_temporal_score_3_high_confimpact_iot)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
print("            -    EN  "+str(ibm_temporal_score_3_low_confimpact_sh+ibm_temporal_score_3_low_confimpact_iot)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
print("            -    EN  "+str(ibm_temporal_score_3_medium_confimpact_sh+ibm_temporal_score_3_medium_confimpact_iot)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO \n") 
print("\n")
print("      -    EN  "+str(ibm_temporal_score_2_sh+ibm_temporal_score_2_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 2. EL IMPACTO DE CONFIDENCIALIDAD VIENE ESPECIFICADO EN "+str(ibm_temporal_score_2_confimpact_sh+ibm_temporal_score_2_confimpact_iot)+" VULNERABILIDADES. LAS ESTADÍSTICAS DE IMPACTO DE CONFIDENCIALIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(ibm_temporal_score_2_high_confimpact_sh+ibm_temporal_score_2_high_confimpact_iot)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
print("            -    EN  "+str(ibm_temporal_score_2_low_confimpact_sh+ibm_temporal_score_2_low_confimpact_iot)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
print("            -    EN  "+str(ibm_temporal_score_2_medium_confimpact_sh+ibm_temporal_score_2_medium_confimpact_iot)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO \n") 
print("\n")
print("      -    EN  "+str(ibm_temporal_score_1_sh+ibm_temporal_score_1_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 1. EL IMPACTO DE CONFIDENCIALIDAD VIENE ESPECIFICADO EN "+str(ibm_temporal_score_1_confimpact_sh+ibm_temporal_score_1_confimpact_iot)+" VULNERABILIDADES. LAS ESTADÍSTICAS DE IMPACTO DE CONFIDENCIALIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(ibm_temporal_score_1_high_confimpact_sh+ibm_temporal_score_1_high_confimpact_iot)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
print("            -    EN  "+str(ibm_temporal_score_1_low_confimpact_sh+ibm_temporal_score_1_low_confimpact_iot)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
print("            -    EN  "+str(ibm_temporal_score_1_medium_confimpact_sh+ibm_temporal_score_1_medium_confimpact_iot)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO \n") 
print("\n")
print("      -    EN  "+str(ibm_temporal_score_0_sh+ibm_temporal_score_0_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 0. EL IMPACTO DE CONFIDENCIALIDAD VIENE ESPECIFICADO EN "+str(ibm_temporal_score_0_confimpact_sh+ibm_temporal_score_0_confimpact_iot)+" VULNERABILIDADES. LAS ESTADÍSTICAS DE IMPACTO DE CONFIDENCIALIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(ibm_temporal_score_0_high_confimpact_sh+ibm_temporal_score_0_high_confimpact_iot)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
print("            -    EN  "+str(ibm_temporal_score_0_low_confimpact_sh+ibm_temporal_score_0_low_confimpact_iot)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
print("            -    EN  "+str(ibm_temporal_score_0_medium_confimpact_sh+ibm_temporal_score_0_medium_confimpact_iot)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO \n") 
print("\n")









print("*********************PORCENTAJES PUNTUACION TEMPORAL/IMPACTO DE CONFIDENCIALIDAD VULNERABILIDADES IBM PARTE IOT Y SMART HOME CONJUNTAS*********************")
print("\n")                            
print("\n")
print(" DE UN TOTAL DE "+str(ibm_temporal_score_total_sh+ibm_temporal_score_total)+" VULNERABILIDADES :\n") 
print("\n")
print("   - LOS PORCENTAJES DE VALORES DE PUNTUACION TEMPORAL SON LOS SIGUIENTES:  \n")
if((ibm_temporal_score_10_sh+ibm_temporal_score_10_iot)>0):
    print("      -    EN EL "+str(float((((ibm_temporal_score_10_sh+ibm_temporal_score_10_iot)*100)/(ibm_temporal_score_total_sh+ibm_temporal_score_total))))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES 10. EL IMPACTO DE CONFIDENCIALIDAD VIENE ESPECIFICADO EN EL "+str(float((((ibm_temporal_score_10_confimpact_sh+ibm_temporal_score_10_confimpact_iot)*100)/(ibm_temporal_score_10_sh+ibm_temporal_score_10_iot))))+" % DE ELLAS. LOS PORCENTAJES DE IMPACTO DE CONFIDENCIALIDAD SON LOS SIGUIENTES :  \n")
    print("            -    EN EL "+str(float((((ibm_temporal_score_10_high_confimpact_sh+ibm_temporal_score_10_high_confimpact_iot)*100)/(ibm_temporal_score_10_confimpact_sh+ibm_temporal_score_10_confimpact_iot))))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
    print("            -    EN EL "+str(float((((ibm_temporal_score_10_low_confimpact_sh+ibm_temporal_score_10_low_confimpact_iot)*100)/(ibm_temporal_score_10_confimpact_sh+ibm_temporal_score_10_confimpact_iot))))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
    print("            -    EN EL "+str(float((((ibm_temporal_score_10_medium_confimpact_sh+ibm_temporal_score_10_medium_confimpact_iot)*100)/(ibm_temporal_score_10_confimpact_sh+ibm_temporal_score_10_confimpact_iot))))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO  \n")
    print("\n")
if((ibm_temporal_score_9_sh+ibm_temporal_score_9_iot)>0):
    print("      -    EN EL "+str(float((((ibm_temporal_score_9_sh+ibm_temporal_score_9_iot)*100)/(ibm_temporal_score_total_sh+ibm_temporal_score_total))))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 9. EL IMPACTO DE CONFIDENCIALIDAD VIENE ESPECIFICADO EN EL "+str(float((((ibm_temporal_score_9_confimpact_sh+ibm_temporal_score_9_confimpact_iot)*100)/(ibm_temporal_score_9_sh+ibm_temporal_score_9_iot))))+" % DE ELLAS. LOS PORCENTAJES DE IMPACTO DE CONFIDENCIALIDAD SON LOS SIGUIENTES :  \n")
    print("            -    EN EL "+str(float((((ibm_temporal_score_9_high_confimpact_sh+ibm_temporal_score_9_high_confimpact_iot)*100)/(ibm_temporal_score_9_confimpact_sh+ibm_temporal_score_9_confimpact_iot))))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
    print("            -    EN EL "+str(float((((ibm_temporal_score_9_low_confimpact_sh+ibm_temporal_score_9_low_confimpact_iot)*100)/(ibm_temporal_score_9_confimpact_sh+ibm_temporal_score_9_confimpact_iot))))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
    print("            -    EN EL "+str(float((((ibm_temporal_score_9_medium_confimpact_sh+ibm_temporal_score_9_medium_confimpact_iot)*100)/(ibm_temporal_score_9_confimpact_sh+ibm_temporal_score_9_confimpact_iot))))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO  \n")
    print("\n")
if((ibm_temporal_score_8_sh+ibm_temporal_score_8_iot)>0):
    print("      -    EN EL "+str(float((((ibm_temporal_score_8_sh+ibm_temporal_score_8_iot)*100)/(ibm_temporal_score_total_sh+ibm_temporal_score_total))))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 8. EL IMPACTO DE CONFIDENCIALIDAD VIENE ESPECIFICADO EN EL "+str(float((((ibm_temporal_score_8_confimpact_sh+ibm_temporal_score_8_confimpact_iot)*100)/(ibm_temporal_score_8_sh+ibm_temporal_score_8_iot))))+" % DE ELLAS. LOS PORCENTAJES DE IMPACTO DE CONFIDENCIALIDAD SON LOS SIGUIENTES :  \n")
    print("            -    EN EL "+str(float((((ibm_temporal_score_8_high_confimpact_sh+ibm_temporal_score_8_high_confimpact_iot)*100)/(ibm_temporal_score_8_confimpact_sh+ibm_temporal_score_8_confimpact_iot))))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
    print("            -    EN EL "+str(float((((ibm_temporal_score_8_low_confimpact_sh+ibm_temporal_score_8_low_confimpact_iot)*100)/(ibm_temporal_score_8_confimpact_sh+ibm_temporal_score_8_confimpact_iot))))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
    print("            -    EN EL "+str(float((((ibm_temporal_score_8_medium_confimpact_sh+ibm_temporal_score_8_medium_confimpact_iot)*100)/(ibm_temporal_score_8_confimpact_sh+ibm_temporal_score_8_confimpact_iot))))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO  \n")
    print("\n")
if((ibm_temporal_score_7_sh+ibm_temporal_score_7_iot)>0):
    print("      -    EN EL "+str(float((((ibm_temporal_score_7_sh+ibm_temporal_score_7_iot)*100)/(ibm_temporal_score_total_sh+ibm_temporal_score_total))))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 7. EL IMPACTO DE CONFIDENCIALIDAD VIENE ESPECIFICADO EN EL "+str(float((((ibm_temporal_score_7_confimpact_sh+ibm_temporal_score_7_confimpact_iot)*100)/(ibm_temporal_score_7_sh+ibm_temporal_score_7_iot))))+" % DE ELLAS. LOS PORCENTAJES DE IMPACTO DE CONFIDENCIALIDAD SON LOS SIGUIENTES :  \n")
    print("            -    EN EL "+str(float((((ibm_temporal_score_7_high_confimpact_sh+ibm_temporal_score_7_high_confimpact_iot)*100)/(ibm_temporal_score_7_confimpact_sh+ibm_temporal_score_7_confimpact_iot))))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
    print("            -    EN EL "+str(float((((ibm_temporal_score_7_low_confimpact_sh+ibm_temporal_score_7_low_confimpact_iot)*100)/(ibm_temporal_score_7_confimpact_sh+ibm_temporal_score_7_confimpact_iot))))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
    print("            -    EN EL "+str(float((((ibm_temporal_score_7_medium_confimpact_sh+ibm_temporal_score_7_medium_confimpact_iot)*100)/(ibm_temporal_score_7_confimpact_sh+ibm_temporal_score_7_confimpact_iot))))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO  \n")
    print("\n")
if((ibm_temporal_score_6_sh+ibm_temporal_score_6_iot)>0):
    print("      -    EN EL "+str(float((((ibm_temporal_score_6_sh+ibm_temporal_score_6_iot)*100)/(ibm_temporal_score_total_sh+ibm_temporal_score_total))))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 6. EL IMPACTO DE CONFIDENCIALIDAD VIENE ESPECIFICADO EN EL "+str(float((((ibm_temporal_score_6_confimpact_sh+ibm_temporal_score_6_confimpact_iot)*100)/(ibm_temporal_score_6_sh+ibm_temporal_score_6_iot))))+" % DE ELLAS. LOS PORCENTAJES DE IMPACTO DE CONFIDENCIALIDAD SON LOS SIGUIENTES :  \n")
    print("            -    EN EL "+str(float((((ibm_temporal_score_6_high_confimpact_sh+ibm_temporal_score_6_high_confimpact_iot)*100)/(ibm_temporal_score_6_confimpact_sh+ibm_temporal_score_6_confimpact_iot))))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
    print("            -    EN EL "+str(float((((ibm_temporal_score_6_low_confimpact_sh+ibm_temporal_score_6_low_confimpact_iot)*100)/(ibm_temporal_score_6_confimpact_sh+ibm_temporal_score_6_confimpact_iot))))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
    print("            -    EN EL "+str(float((((ibm_temporal_score_6_medium_confimpact_sh+ibm_temporal_score_6_medium_confimpact_iot)*100)/(ibm_temporal_score_6_confimpact_sh+ibm_temporal_score_6_confimpact_iot))))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO  \n")
    print("\n")
if((ibm_temporal_score_5_sh+ibm_temporal_score_5_iot)>0):
    print("      -    EN EL "+str(float((((ibm_temporal_score_5_sh+ibm_temporal_score_5_iot)*100)/(ibm_temporal_score_total_sh+ibm_temporal_score_total))))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 5. EL IMPACTO DE CONFIDENCIALIDAD VIENE ESPECIFICADO EN EL "+str(float((((ibm_temporal_score_5_confimpact_sh+ibm_temporal_score_5_confimpact_iot)*100)/(ibm_temporal_score_5_sh+ibm_temporal_score_5_iot))))+" % DE ELLAS. LOS PORCENTAJES DE IMPACTO DE CONFIDENCIALIDAD SON LOS SIGUIENTES :  \n")
    print("            -    EN EL "+str(float((((ibm_temporal_score_5_high_confimpact_sh+ibm_temporal_score_5_high_confimpact_iot)*100)/(ibm_temporal_score_5_confimpact_sh+ibm_temporal_score_5_confimpact_iot))))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
    print("            -    EN EL "+str(float((((ibm_temporal_score_5_low_confimpact_sh+ibm_temporal_score_5_low_confimpact_iot)*100)/(ibm_temporal_score_5_confimpact_sh+ibm_temporal_score_5_confimpact_iot))))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
    print("            -    EN EL "+str(float((((ibm_temporal_score_5_medium_confimpact_sh+ibm_temporal_score_5_medium_confimpact_iot)*100)/(ibm_temporal_score_5_confimpact_sh+ibm_temporal_score_5_confimpact_iot))))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO  \n")
    print("\n")
if((ibm_temporal_score_4_sh+ibm_temporal_score_4_iot)>0):
    print("      -    EN EL "+str(float((((ibm_temporal_score_4_sh+ibm_temporal_score_4_iot)*100)/(ibm_temporal_score_total_sh+ibm_temporal_score_total))))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 4. EL IMPACTO DE CONFIDENCIALIDAD VIENE ESPECIFICADO EN EL "+str(float((((ibm_temporal_score_4_confimpact_sh+ibm_temporal_score_4_confimpact_iot)*100)/(ibm_temporal_score_4_sh+ibm_temporal_score_4_iot))))+" % DE ELLAS. LOS PORCENTAJES DE IMPACTO DE CONFIDENCIALIDAD SON LOS SIGUIENTES :  \n")
    print("            -    EN EL "+str(float((((ibm_temporal_score_4_high_confimpact_sh+ibm_temporal_score_4_high_confimpact_iot)*100)/(ibm_temporal_score_4_confimpact_sh+ibm_temporal_score_4_confimpact_iot))))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
    print("            -    EN EL "+str(float((((ibm_temporal_score_4_low_confimpact_sh+ibm_temporal_score_4_low_confimpact_iot)*100)/(ibm_temporal_score_4_confimpact_sh+ibm_temporal_score_4_confimpact_iot))))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
    print("            -    EN EL "+str(float((((ibm_temporal_score_4_medium_confimpact_sh+ibm_temporal_score_4_medium_confimpact_iot)*100)/(ibm_temporal_score_4_confimpact_sh+ibm_temporal_score_4_confimpact_iot))))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO  \n")
    print("\n")
if((ibm_temporal_score_3_sh+ibm_temporal_score_3_iot)>0):
    print("      -    EN EL "+str(float((((ibm_temporal_score_3_sh+ibm_temporal_score_3_iot)*100)/(ibm_temporal_score_total_sh+ibm_temporal_score_total))))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 3. EL IMPACTO DE CONFIDENCIALIDAD VIENE ESPECIFICADO EN EL "+str(float((((ibm_temporal_score_3_confimpact_sh+ibm_temporal_score_3_confimpact_iot)*100)/(ibm_temporal_score_3_sh+ibm_temporal_score_3_iot))))+" % DE ELLAS. LOS PORCENTAJES DE IMPACTO DE CONFIDENCIALIDAD SON LOS SIGUIENTES :  \n")
    print("            -    EN EL "+str(float((((ibm_temporal_score_3_high_confimpact_sh+ibm_temporal_score_3_high_confimpact_iot)*100)/(ibm_temporal_score_3_confimpact_sh+ibm_temporal_score_3_confimpact_iot))))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
    print("            -    EN EL "+str(float((((ibm_temporal_score_3_low_confimpact_sh+ibm_temporal_score_3_low_confimpact_iot)*100)/(ibm_temporal_score_3_confimpact_sh+ibm_temporal_score_3_confimpact_iot))))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
    print("            -    EN EL "+str(float((((ibm_temporal_score_3_medium_confimpact_sh+ibm_temporal_score_3_medium_confimpact_iot)*100)/(ibm_temporal_score_3_confimpact_sh+ibm_temporal_score_3_confimpact_iot))))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO  \n")
    print("\n")
if((ibm_temporal_score_2_sh+ibm_temporal_score_2_iot)>0):
    print("      -    EN EL "+str(float((((ibm_temporal_score_2_sh+ibm_temporal_score_2_iot)*100)/(ibm_temporal_score_total_sh+ibm_temporal_score_total))))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 2. EL IMPACTO DE CONFIDENCIALIDAD VIENE ESPECIFICADO EN EL "+str(float((((ibm_temporal_score_2_confimpact_sh+ibm_temporal_score_2_confimpact_iot)*100)/(ibm_temporal_score_2_sh+ibm_temporal_score_2_iot))))+" % DE ELLAS. LOS PORCENTAJES DE IMPACTO DE CONFIDENCIALIDAD SON LOS SIGUIENTES :  \n")
    print("            -    EN EL "+str(float((((ibm_temporal_score_2_high_confimpact_sh+ibm_temporal_score_2_high_confimpact_iot)*100)/(ibm_temporal_score_2_confimpact_sh+ibm_temporal_score_2_confimpact_iot))))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
    print("            -    EN EL "+str(float((((ibm_temporal_score_2_low_confimpact_sh+ibm_temporal_score_2_low_confimpact_iot)*100)/(ibm_temporal_score_2_confimpact_sh+ibm_temporal_score_2_confimpact_iot))))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
    print("            -    EN EL "+str(float((((ibm_temporal_score_2_medium_confimpact_sh+ibm_temporal_score_2_medium_confimpact_iot)*100)/(ibm_temporal_score_2_confimpact_sh+ibm_temporal_score_2_confimpact_iot))))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO  \n")
    print("\n")
if((ibm_temporal_score_1_sh+ibm_temporal_score_1_iot)>0):
    print("      -    EN EL "+str(float((((ibm_temporal_score_1_sh+ibm_temporal_score_1_iot)*100)/(ibm_temporal_score_total_sh+ibm_temporal_score_total))))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 1. EL IMPACTO DE CONFIDENCIALIDAD VIENE ESPECIFICADO EN EL "+str(float((((ibm_temporal_score_1_confimpact_sh+ibm_temporal_score_1_confimpact_iot)*100)/(ibm_temporal_score_1_sh+ibm_temporal_score_1_iot))))+" % DE ELLAS. LOS PORCENTAJES DE IMPACTO DE CONFIDENCIALIDAD SON LOS SIGUIENTES :  \n")
    print("            -    EN EL "+str(float((((ibm_temporal_score_1_high_confimpact_sh+ibm_temporal_score_1_high_confimpact_iot)*100)/(ibm_temporal_score_1_confimpact_sh+ibm_temporal_score_1_confimpact_iot))))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
    print("            -    EN EL "+str(float((((ibm_temporal_score_1_low_confimpact_sh+ibm_temporal_score_1_low_confimpact_iot)*100)/(ibm_temporal_score_1_confimpact_sh+ibm_temporal_score_1_confimpact_iot))))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
    print("            -    EN EL "+str(float((((ibm_temporal_score_1_medium_confimpact_sh+ibm_temporal_score_1_medium_confimpact_iot)*100)/(ibm_temporal_score_1_confimpact_sh+ibm_temporal_score_1_confimpact_iot))))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO  \n")
    print("\n")
if((ibm_temporal_score_0_sh+ibm_temporal_score_0_iot)>0):
    print("      -    EN EL "+str(float((((ibm_temporal_score_0_sh+ibm_temporal_score_0_iot)*100)/(ibm_temporal_score_total_sh+ibm_temporal_score_total))))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 0. EL IMPACTO DE CONFIDENCIALIDAD VIENE ESPECIFICADO EN EL "+str(float((((ibm_temporal_score_0_confimpact_sh+ibm_temporal_score_0_confimpact_iot)*100)/(ibm_temporal_score_0_sh+ibm_temporal_score_0_iot))))+" % DE ELLAS. LOS PORCENTAJES DE IMPACTO DE CONFIDENCIALIDAD SON LOS SIGUIENTES :  \n")
    print("            -    EN EL "+str(float((((ibm_temporal_score_0_high_confimpact_sh+ibm_temporal_score_0_high_confimpact_iot)*100)/(ibm_temporal_score_0_confimpact_sh+ibm_temporal_score_0_confimpact_iot))))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
    print("            -    EN EL "+str(float((((ibm_temporal_score_0_low_confimpact_sh+ibm_temporal_score_0_low_confimpact_iot)*100)/(ibm_temporal_score_0_confimpact_sh+ibm_temporal_score_0_confimpact_iot))))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
    print("            -    EN EL "+str(float((((ibm_temporal_score_0_medium_confimpact_sh+ibm_temporal_score_0_medium_confimpact_iot)*100)/(ibm_temporal_score_0_confimpact_sh+ibm_temporal_score_0_confimpact_iot))))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO  \n")
    print("\n")


	
	
	
	
	
	
	
	
	