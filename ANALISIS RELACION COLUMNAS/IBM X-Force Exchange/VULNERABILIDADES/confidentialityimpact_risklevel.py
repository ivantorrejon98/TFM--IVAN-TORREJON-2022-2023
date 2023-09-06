

import pandas as pd
from datetime import datetime,timedelta



#Abro los ficheros con los que voy a tratar




df_vulnibm_iot = pd.read_excel('vulnerabilidades_ibm_iot_2023.xlsx')
#Variables para almacenar el contador total de valores de confidencialidad
count_vulnibm_iot_confidentiality_impact=0
#Variables para almacenar el contador de un valor concreto de impacto de confidencialidad
count_vulnibm_iot_highconfimpact=0
#Variable para almacenar la suma de valores de nivel de riesgo para calcular despues la media para un valor de confidencialidad dado
count_vulnibm_iot_highconfimpact_risklevel=0
#Contador de valores de nivel de riesgo dado un nivel de impacto de confidencialidad concreto
count_vulnibm_iot_highconfimpact_risklevel10=0
count_vulnibm_iot_highconfimpact_risklevel9=0
count_vulnibm_iot_highconfimpact_risklevel8=0
count_vulnibm_iot_highconfimpact_risklevel7=0
count_vulnibm_iot_highconfimpact_risklevel6=0
count_vulnibm_iot_highconfimpact_risklevel5=0
count_vulnibm_iot_highconfimpact_risklevel4=0
count_vulnibm_iot_highconfimpact_risklevel3=0
count_vulnibm_iot_highconfimpact_risklevel2=0
count_vulnibm_iot_highconfimpact_risklevel1=0
count_vulnibm_iot_highconfimpact_risklevel0=0



count_vulnibm_iot_lowconfimpact=0
count_vulnibm_iot_lowconfimpact_risklevel=0
count_vulnibm_iot_lowconfimpact_risklevel10=0
count_vulnibm_iot_lowconfimpact_risklevel9=0
count_vulnibm_iot_lowconfimpact_risklevel8=0
count_vulnibm_iot_lowconfimpact_risklevel7=0
count_vulnibm_iot_lowconfimpact_risklevel6=0
count_vulnibm_iot_lowconfimpact_risklevel5=0
count_vulnibm_iot_lowconfimpact_risklevel4=0
count_vulnibm_iot_lowconfimpact_risklevel3=0
count_vulnibm_iot_lowconfimpact_risklevel2=0
count_vulnibm_iot_lowconfimpact_risklevel1=0
count_vulnibm_iot_lowconfimpact_risklevel0=0



#Comprobamos el valor de impacto de confidencialidad
for r in range(0,len(df_vulnibm_iot["x_xfe_cvss_confidentiality_impact"])):
    if(isinstance(df_vulnibm_iot["x_xfe_cvss_confidentiality_impact"][r],str)):
        aux_str=df_vulnibm_iot["x_xfe_cvss_confidentiality_impact"][r].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
        if(aux_str!='NONE' or aux_str!='None'):
            count_vulnibm_iot_confidentiality_impact+=1
            #Comprobamos el valor de impacto de confidencialidad
            if('High' in aux_str):
                count_vulnibm_iot_highconfimpact+=1
                #Sumamos el valor de nivel de riesgo para posteriormente calcular la media
                count_vulnibm_iot_highconfimpact_risklevel+=float(df_vulnibm_iot["x_xfe_risk_level"][r])
                #Comprobamos el valor de nivel de riesgo
                if(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 10.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=9.0)):
                    count_vulnibm_iot_highconfimpact_risklevel9+=1
                elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 9.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=8.0)):
                    count_vulnibm_iot_highconfimpact_risklevel8+=1
                elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 8.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=7.0)):
                    count_vulnibm_iot_highconfimpact_risklevel7+=1
                elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 7.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=6.0)):
                    count_vulnibm_iot_highconfimpact_risklevel6+=1
                elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 6.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=5.0)):
                    count_vulnibm_iot_highconfimpact_risklevel5+=1
                elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 5.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=4.0)):
                    count_vulnibm_iot_highconfimpact_risklevel4+=1
                elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 4.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=3.0)):
                    count_vulnibm_iot_highconfimpact_risklevel3+=1
                elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 3.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=2.0)):
                    count_vulnibm_iot_highconfimpact_risklevel2+=1
                elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 2.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=1.0)):
                    count_vulnibm_iot_highconfimpact_risklevel1+=1
                elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 1.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=0.0)):
                    count_vulnibm_iot_highconfimpact_risklevel0+=1
                elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) == 10.0)):
                    count_vulnibm_iot_highconfimpact_risklevel10+=1

            elif('Low' in aux_str):

                count_vulnibm_iot_lowconfimpact+=1
                count_vulnibm_iot_lowconfimpact_risklevel+=float(df_vulnibm_iot["x_xfe_risk_level"][r])
                if(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 10.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=9.0)):
                    count_vulnibm_iot_lowconfimpact_risklevel9+=1
                elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 9.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=8.0)):
                    count_vulnibm_iot_lowconfimpact_risklevel8+=1
                elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 8.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=7.0)):
                    count_vulnibm_iot_lowconfimpact_risklevel7+=1
                elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 7.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=6.0)):
                    count_vulnibm_iot_lowconfimpact_risklevel6+=1
                elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 6.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=5.0)):
                    count_vulnibm_iot_lowconfimpact_risklevel5+=1
                elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 5.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=4.0)):
                    count_vulnibm_iot_lowconfimpact_risklevel4+=1
                elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 4.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=3.0)):
                    count_vulnibm_iot_lowconfimpact_risklevel3+=1
                elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 3.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=2.0)):
                    count_vulnibm_iot_lowconfimpact_risklevel2+=1
                elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 2.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=1.0)):
                    count_vulnibm_iot_lowconfimpact_risklevel1+=1
                elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 1.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=0.0)):
                    count_vulnibm_iot_lowconfimpact_risklevel0+=1
                elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) == 10.0)):
                    count_vulnibm_iot_lowconfimpact_risklevel10+=1


            
print("*******************************ESTADÍSTICAS RELACION DE IMPACTO DE CONFIDENCIALIDAD/PUNTUACION BASE PARA OBJETOS DE TIPO VULNERABILIDAD IBM PARTE IOT*******************************")
print("\n")                            
print("\n")
print(" DE UN TOTAL DE "+str(count_vulnibm_iot_confidentiality_impact)+" VULNERABILIDADES CON VALOR DE CONFIDENCIALIDAD ESPECIFICADO:\n") 
print("\n")
print("   - LAS ESTADISTICAS DE VALORES DE IMPACTO DE CONFIDENCIALIDAD SON LAS SIGUIENTES:  \n")
print("      -    EN  "+str(count_vulnibm_iot_highconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO, LAS ESTADÍSTICAS DE NIVEL DE RIESGO SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_highconfimpact_risklevel10)+" VULNERABILIDADES EL NIVEL DE RIESGO ES 10 \n")
print("            -    EN  "+str(count_vulnibm_iot_highconfimpact_risklevel9)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN  "+str(count_vulnibm_iot_highconfimpact_risklevel8)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN  "+str(count_vulnibm_iot_highconfimpact_risklevel7)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN  "+str(count_vulnibm_iot_highconfimpact_risklevel6)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN "+str(count_vulnibm_iot_highconfimpact_risklevel5)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN "+str(count_vulnibm_iot_highconfimpact_risklevel4)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN "+str(count_vulnibm_iot_highconfimpact_risklevel3)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN "+str(count_vulnibm_iot_highconfimpact_risklevel2)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN "+str(count_vulnibm_iot_highconfimpact_risklevel1)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN "+str(count_vulnibm_iot_highconfimpact_risklevel0)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 0 \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_lowconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO, LAS ESTADÍSTICAS DE NIVEL DE RIESGO SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_lowconfimpact_risklevel10)+" VULNERABILIDADES EL NIVEL DE RIESGO ES 10 \n")
print("            -    EN  "+str(count_vulnibm_iot_lowconfimpact_risklevel9)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN  "+str(count_vulnibm_iot_lowconfimpact_risklevel8)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN  "+str(count_vulnibm_iot_lowconfimpact_risklevel7)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN  "+str(count_vulnibm_iot_lowconfimpact_risklevel6)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN "+str(count_vulnibm_iot_lowconfimpact_risklevel5)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN "+str(count_vulnibm_iot_lowconfimpact_risklevel4)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN "+str(count_vulnibm_iot_lowconfimpact_risklevel3)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN "+str(count_vulnibm_iot_lowconfimpact_risklevel2)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN "+str(count_vulnibm_iot_lowconfimpact_risklevel1)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN "+str(count_vulnibm_iot_lowconfimpact_risklevel0)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 0 \n")
print("\n")


print("*******************************PORCENTAJE RELACION DE IMPACTO DE CONFIDENCIALIDAD/PUNTUACION BASE PARA OBJETOS DE TIPO VULNERABILIDAD IBM PARTE IOT*******************************")
print("\n")                            
print("\n")
print(" DE UN TOTAL DE "+str(count_vulnibm_iot_confidentiality_impact)+" VULNERABILIDADES CON VALOR DE CONFIDENCIALIDAD ESPECIFICADO:\n") 
print("\n")
print("   - LOS PORCENTAJES DE VALORES DE IMPACTO DE CONFIDENCIALIDAD SON LOS SIGUIENTES:  \n")
print("      -    EN EL  "+str(float(((count_vulnibm_iot_highconfimpact*100)/count_vulnibm_iot_confidentiality_impact)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO, LOS PORCENTAJES DE NIVEL DE RIESGO SON LOS SIGUIENTES :  \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_highconfimpact_risklevel10*100)/count_vulnibm_iot_highconfimpact)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES 10 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_highconfimpact_risklevel9*100)/count_vulnibm_iot_highconfimpact)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_highconfimpact_risklevel8*100)/count_vulnibm_iot_highconfimpact)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_highconfimpact_risklevel7*100)/count_vulnibm_iot_highconfimpact)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_highconfimpact_risklevel6*100)/count_vulnibm_iot_highconfimpact)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_highconfimpact_risklevel5*100)/count_vulnibm_iot_highconfimpact)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_highconfimpact_risklevel4*100)/count_vulnibm_iot_highconfimpact)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_highconfimpact_risklevel3*100)/count_vulnibm_iot_highconfimpact)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_highconfimpact_risklevel2*100)/count_vulnibm_iot_highconfimpact)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_highconfimpact_risklevel1*100)/count_vulnibm_iot_highconfimpact)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_highconfimpact_risklevel0*100)/count_vulnibm_iot_highconfimpact)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 0 \n")
print("            -    EL VALOR MEDIO DE PUNTUACION BASE ES  "+str(float(((count_vulnibm_iot_highconfimpact_risklevel)/count_vulnibm_iot_highconfimpact)))+"\n")
print("\n")
print("      -    EN EL  "+str(float(((count_vulnibm_iot_lowconfimpact*100)/count_vulnibm_iot_confidentiality_impact)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO, LOS PORCENTAJES DE NIVEL DE RIESGO SON LOS SIGUIENTES :  \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_lowconfimpact_risklevel10*100)/count_vulnibm_iot_lowconfimpact)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES 10 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_lowconfimpact_risklevel9*100)/count_vulnibm_iot_lowconfimpact)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_lowconfimpact_risklevel8*100)/count_vulnibm_iot_lowconfimpact)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_lowconfimpact_risklevel7*100)/count_vulnibm_iot_lowconfimpact)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_lowconfimpact_risklevel6*100)/count_vulnibm_iot_lowconfimpact)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_lowconfimpact_risklevel5*100)/count_vulnibm_iot_lowconfimpact)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_lowconfimpact_risklevel4*100)/count_vulnibm_iot_lowconfimpact)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_lowconfimpact_risklevel3*100)/count_vulnibm_iot_lowconfimpact)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_lowconfimpact_risklevel2*100)/count_vulnibm_iot_lowconfimpact)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_lowconfimpact_risklevel1*100)/count_vulnibm_iot_lowconfimpact)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_lowconfimpact_risklevel0*100)/count_vulnibm_iot_lowconfimpact)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 0 \n")
print("            -    EL VALOR MEDIO DE PUNTUACION BASE ES  "+str(float(((count_vulnibm_iot_lowconfimpact_risklevel)/count_vulnibm_iot_lowconfimpact)))+"\n")
print("\n")



#Abro los ficheros con los que voy a tratar




df_vulnibm_sh = pd.read_excel('vulnerabilidades_ibm_smart_home_2023.xlsx')

#Variables para almacenar el contador total de valores de confidencialidad
count_vulnibm_sh_confidentiality_impact=0
#Variables para almacenar el contador de un valor concreto de impacto de confidencialidad
count_vulnibm_sh_highconfimpact=0
#Variable para almacenar la suma de valores de nivel de riesgo para calcular despues la media para un valor de confidencialidad dado
count_vulnibm_sh_highconfimpact_risklevel=0
#Contador de valores de nivel de riesgo dado un nivel de impacto de confidencialidad concreto
count_vulnibm_sh_highconfimpact_risklevel10=0
count_vulnibm_sh_highconfimpact_risklevel9=0
count_vulnibm_sh_highconfimpact_risklevel8=0
count_vulnibm_sh_highconfimpact_risklevel7=0
count_vulnibm_sh_highconfimpact_risklevel6=0
count_vulnibm_sh_highconfimpact_risklevel5=0
count_vulnibm_sh_highconfimpact_risklevel4=0
count_vulnibm_sh_highconfimpact_risklevel3=0
count_vulnibm_sh_highconfimpact_risklevel2=0
count_vulnibm_sh_highconfimpact_risklevel1=0
count_vulnibm_sh_highconfimpact_risklevel0=0



count_vulnibm_sh_lowconfimpact=0
count_vulnibm_sh_lowconfimpact_risklevel=0
count_vulnibm_sh_lowconfimpact_risklevel10=0
count_vulnibm_sh_lowconfimpact_risklevel9=0
count_vulnibm_sh_lowconfimpact_risklevel8=0
count_vulnibm_sh_lowconfimpact_risklevel7=0
count_vulnibm_sh_lowconfimpact_risklevel6=0
count_vulnibm_sh_lowconfimpact_risklevel5=0
count_vulnibm_sh_lowconfimpact_risklevel4=0
count_vulnibm_sh_lowconfimpact_risklevel3=0
count_vulnibm_sh_lowconfimpact_risklevel2=0
count_vulnibm_sh_lowconfimpact_risklevel1=0
count_vulnibm_sh_lowconfimpact_risklevel0=0



#Comprobamos el valor de impacto de confidencialidad
for r in range(0,len(df_vulnibm_sh["x_xfe_cvss_confidentiality_impact"])):  
    if(isinstance(df_vulnibm_sh["x_xfe_cvss_confidentiality_impact"][r],str)):
        aux_str=df_vulnibm_sh["x_xfe_cvss_confidentiality_impact"][r].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
        if(aux_str!='NONE' or aux_str!='None'):
            count_vulnibm_sh_confidentiality_impact+=1
            #Comprobamos el valor de impacto de confidencialidad
            if('High' in aux_str):
                count_vulnibm_sh_highconfimpact+=1
                #Sumamos el valor de nivel de riesgo para posteriormente calcular la media
                count_vulnibm_sh_highconfimpact_risklevel+=float(df_vulnibm_sh["x_xfe_risk_level"][r])
                #Comprobamos el valor de nivel de riesgo
                if(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 10.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=9.0)):
                    count_vulnibm_sh_highconfimpact_risklevel9+=1
                elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 9.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=8.0)):
                    count_vulnibm_sh_highconfimpact_risklevel8+=1
                elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 8.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=7.0)):
                    count_vulnibm_sh_highconfimpact_risklevel7+=1
                elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 7.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=6.0)):
                    count_vulnibm_sh_highconfimpact_risklevel6+=1
                elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 6.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=5.0)):
                    count_vulnibm_sh_highconfimpact_risklevel5+=1
                elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 5.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=4.0)):
                    count_vulnibm_sh_highconfimpact_risklevel4+=1
                elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 4.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=3.0)):
                    count_vulnibm_sh_highconfimpact_risklevel3+=1
                elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 3.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=2.0)):
                    count_vulnibm_sh_highconfimpact_risklevel2+=1
                elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 2.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=1.0)):
                    count_vulnibm_sh_highconfimpact_risklevel1+=1
                elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 1.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=0.0)):
                    count_vulnibm_sh_highconfimpact_risklevel0+=1
                elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) == 10.0)):
                    count_vulnibm_sh_highconfimpact_risklevel10+=1

            elif('Low' in aux_str):

                count_vulnibm_sh_lowconfimpact+=1
                count_vulnibm_sh_lowconfimpact_risklevel+=float(df_vulnibm_sh["x_xfe_risk_level"][r])
                if(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 10.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=9.0)):
                    count_vulnibm_sh_lowconfimpact_risklevel9+=1
                elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 9.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=8.0)):
                    count_vulnibm_sh_lowconfimpact_risklevel8+=1
                elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 8.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=7.0)):
                    count_vulnibm_sh_lowconfimpact_risklevel7+=1
                elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 7.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=6.0)):
                    count_vulnibm_sh_lowconfimpact_risklevel6+=1
                elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 6.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=5.0)):
                    count_vulnibm_sh_lowconfimpact_risklevel5+=1
                elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 5.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=4.0)):
                    count_vulnibm_sh_lowconfimpact_risklevel4+=1
                elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 4.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=3.0)):
                    count_vulnibm_sh_lowconfimpact_risklevel3+=1
                elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 3.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=2.0)):
                    count_vulnibm_sh_lowconfimpact_risklevel2+=1
                elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 2.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=1.0)):
                    count_vulnibm_sh_lowconfimpact_risklevel1+=1
                elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 1.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=0.0)):
                    count_vulnibm_sh_lowconfimpact_risklevel0+=1
                elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) == 10.0)):
                    count_vulnibm_sh_lowconfimpact_risklevel10+=1


            
                
print("*******************************ESTADÍSTICAS RELACION DE IMPACTO DE CONFIDENCIALIDAD/PUNTUACION BASE PARA OBJETOS DE TIPO VULNERABILIDAD IBM PARTE SMART HOME*******************************")
print("\n")                            
print("\n")
print(" DE UN TOTAL DE "+str(count_vulnibm_sh_confidentiality_impact)+" VULNERABILIDADES CON VALOR DE CONFIDENCIALIDAD ESPECIFICADO:\n") 
print("\n")
print("   - LAS ESTADISTICAS DE VALORES DE IMPACTO DE CONFIDENCIALIDAD SON LAS SIGUIENTES:  \n")
print("      -    EN  "+str(count_vulnibm_sh_highconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO, LAS ESTADÍSTICAS DE NIVEL DE RIESGO SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_sh_highconfimpact_risklevel10)+" VULNERABILIDADES EL NIVEL DE RIESGO ES 10 \n")
print("            -    EN  "+str(count_vulnibm_sh_highconfimpact_risklevel9)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN  "+str(count_vulnibm_sh_highconfimpact_risklevel8)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN  "+str(count_vulnibm_sh_highconfimpact_risklevel7)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN  "+str(count_vulnibm_sh_highconfimpact_risklevel6)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN "+str(count_vulnibm_sh_highconfimpact_risklevel5)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN "+str(count_vulnibm_sh_highconfimpact_risklevel4)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN "+str(count_vulnibm_sh_highconfimpact_risklevel3)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN "+str(count_vulnibm_sh_highconfimpact_risklevel2)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN "+str(count_vulnibm_sh_highconfimpact_risklevel1)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN "+str(count_vulnibm_sh_highconfimpact_risklevel0)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 0 \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_sh_lowconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO, LAS ESTADÍSTICAS DE NIVEL DE RIESGO SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_sh_lowconfimpact_risklevel10)+" VULNERABILIDADES EL NIVEL DE RIESGO ES 10 \n")
print("            -    EN  "+str(count_vulnibm_sh_lowconfimpact_risklevel9)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN  "+str(count_vulnibm_sh_lowconfimpact_risklevel8)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN  "+str(count_vulnibm_sh_lowconfimpact_risklevel7)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN  "+str(count_vulnibm_sh_lowconfimpact_risklevel6)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN "+str(count_vulnibm_sh_lowconfimpact_risklevel5)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN "+str(count_vulnibm_sh_lowconfimpact_risklevel4)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN "+str(count_vulnibm_sh_lowconfimpact_risklevel3)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN "+str(count_vulnibm_sh_lowconfimpact_risklevel2)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN "+str(count_vulnibm_sh_lowconfimpact_risklevel1)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN "+str(count_vulnibm_sh_lowconfimpact_risklevel0)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 0 \n")
print("\n")




print("*******************************PORCENTAJE RELACION DE IMPACTO DE CONFIDENCIALIDAD/PUNTUACION BASE PARA OBJETOS DE TIPO VULNERABILIDAD IBM PARTE SMART HOME*******************************")
print("\n")                            
print("\n")
print(" DE UN TOTAL DE "+str(count_vulnibm_sh_confidentiality_impact)+" VULNERABILIDADES CON VALOR DE CONFIDENCIALIDAD ESPECIFICADO:\n") 
print("\n")
print("   - LOS PORCENTAJES DE VALORES DE IMPACTO DE CONFIDENCIALIDAD SON LOS SIGUIENTES:  \n")
print("      -    EN EL  "+str(float(((count_vulnibm_sh_highconfimpact*100)/count_vulnibm_sh_confidentiality_impact)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO, LOS PORCENTAJES DE NIVEL DE RIESGO SON LOS SIGUIENTES :  \n")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_highconfimpact_risklevel10*100)/count_vulnibm_sh_highconfimpact)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES 10 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_highconfimpact_risklevel9*100)/count_vulnibm_sh_highconfimpact)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_highconfimpact_risklevel8*100)/count_vulnibm_sh_highconfimpact)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_highconfimpact_risklevel7*100)/count_vulnibm_sh_highconfimpact)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_highconfimpact_risklevel6*100)/count_vulnibm_sh_highconfimpact)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN EL "+str(float(((count_vulnibm_sh_highconfimpact_risklevel5*100)/count_vulnibm_sh_highconfimpact)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN EL "+str(float(((count_vulnibm_sh_highconfimpact_risklevel4*100)/count_vulnibm_sh_highconfimpact)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN EL "+str(float(((count_vulnibm_sh_highconfimpact_risklevel3*100)/count_vulnibm_sh_highconfimpact)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN EL "+str(float(((count_vulnibm_sh_highconfimpact_risklevel2*100)/count_vulnibm_sh_highconfimpact)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN EL "+str(float(((count_vulnibm_sh_highconfimpact_risklevel1*100)/count_vulnibm_sh_highconfimpact)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN EL "+str(float(((count_vulnibm_sh_highconfimpact_risklevel0*100)/count_vulnibm_sh_highconfimpact)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 0 \n")
print("            -    EL VALOR MEDIO DE PUNTUACION BASE ES  "+str(float(((count_vulnibm_sh_highconfimpact_risklevel)/count_vulnibm_sh_highconfimpact)))+"\n")
print("\n")
print("      -    EN EL  "+str(float(((count_vulnibm_sh_lowconfimpact*100)/count_vulnibm_sh_confidentiality_impact)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO, LOS PORCENTAJES DE NIVEL DE RIESGO SON LOS SIGUIENTES :  \n")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_lowconfimpact_risklevel10*100)/count_vulnibm_sh_lowconfimpact)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES 10 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_lowconfimpact_risklevel9*100)/count_vulnibm_sh_lowconfimpact)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_lowconfimpact_risklevel8*100)/count_vulnibm_sh_lowconfimpact)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_lowconfimpact_risklevel7*100)/count_vulnibm_sh_lowconfimpact)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_lowconfimpact_risklevel6*100)/count_vulnibm_sh_lowconfimpact)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN EL "+str(float(((count_vulnibm_sh_lowconfimpact_risklevel5*100)/count_vulnibm_sh_lowconfimpact)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN EL "+str(float(((count_vulnibm_sh_lowconfimpact_risklevel4*100)/count_vulnibm_sh_lowconfimpact)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN EL "+str(float(((count_vulnibm_sh_lowconfimpact_risklevel3*100)/count_vulnibm_sh_lowconfimpact)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN EL "+str(float(((count_vulnibm_sh_lowconfimpact_risklevel2*100)/count_vulnibm_sh_lowconfimpact)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN EL "+str(float(((count_vulnibm_sh_lowconfimpact_risklevel1*100)/count_vulnibm_sh_lowconfimpact)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN EL "+str(float(((count_vulnibm_sh_lowconfimpact_risklevel0*100)/count_vulnibm_sh_lowconfimpact)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 0 \n")
print("            -    EL VALOR MEDIO DE PUNTUACION BASE ES  "+str(float(((count_vulnibm_sh_lowconfimpact_risklevel)/count_vulnibm_sh_lowconfimpact)))+"\n")
print("\n")





print("*******************************ESTADÍSTICAS RELACION DE IMPACTO DE CONFIDENCIALIDAD/PUNTUACION BASE PARA OBJETOS DE TIPO VULNERABILIDAD IBM PARTE IOT Y SMART HOME CONJUNTAS*******************************")
print("\n")                            
print("\n")
print(" DE UN TOTAL DE "+str(count_vulnibm_iot_confidentiality_impact+count_vulnibm_sh_confidentiality_impact)+" VULNERABILIDADES CON VALOR DE CONFIDENCIALIDAD ESPECIFICADO:\n") 
print("\n")
print("   - LAS ESTADISTICAS DE VALORES DE IMPACTO DE CONFIDENCIALIDAD SON LAS SIGUIENTES:  \n")
print("      -    EN  "+str(count_vulnibm_iot_highconfimpact+count_vulnibm_sh_highconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO, LAS ESTADÍSTICAS DE NIVEL DE RIESGO SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_highconfimpact_risklevel10+count_vulnibm_sh_highconfimpact_risklevel10)+" VULNERABILIDADES EL NIVEL DE RIESGO ES 10 \n")
print("            -    EN  "+str(count_vulnibm_iot_highconfimpact_risklevel9+count_vulnibm_sh_highconfimpact_risklevel9)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN  "+str(count_vulnibm_iot_highconfimpact_risklevel8+count_vulnibm_sh_highconfimpact_risklevel8)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN  "+str(count_vulnibm_iot_highconfimpact_risklevel7+count_vulnibm_sh_highconfimpact_risklevel7)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN  "+str(count_vulnibm_iot_highconfimpact_risklevel6+count_vulnibm_sh_highconfimpact_risklevel6)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN "+str(count_vulnibm_iot_highconfimpact_risklevel5+count_vulnibm_sh_highconfimpact_risklevel5)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN "+str(count_vulnibm_iot_highconfimpact_risklevel4+count_vulnibm_sh_highconfimpact_risklevel4)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN "+str(count_vulnibm_iot_highconfimpact_risklevel3+count_vulnibm_sh_highconfimpact_risklevel3)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN "+str(count_vulnibm_iot_highconfimpact_risklevel2+count_vulnibm_sh_highconfimpact_risklevel2)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN "+str(count_vulnibm_iot_highconfimpact_risklevel1+count_vulnibm_sh_highconfimpact_risklevel1)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN "+str(count_vulnibm_iot_highconfimpact_risklevel0+count_vulnibm_sh_highconfimpact_risklevel0)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 0 \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_lowconfimpact+count_vulnibm_sh_lowconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO, LAS ESTADÍSTICAS DE NIVEL DE RIESGO SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_lowconfimpact_risklevel10+count_vulnibm_sh_lowconfimpact_risklevel10)+" VULNERABILIDADES EL NIVEL DE RIESGO ES 10 \n")
print("            -    EN  "+str(count_vulnibm_iot_lowconfimpact_risklevel9+count_vulnibm_sh_lowconfimpact_risklevel9)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN  "+str(count_vulnibm_iot_lowconfimpact_risklevel8+count_vulnibm_sh_lowconfimpact_risklevel8)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN  "+str(count_vulnibm_iot_lowconfimpact_risklevel7+count_vulnibm_sh_lowconfimpact_risklevel7)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN  "+str(count_vulnibm_iot_lowconfimpact_risklevel6+count_vulnibm_sh_lowconfimpact_risklevel6)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN "+str(count_vulnibm_iot_lowconfimpact_risklevel5+count_vulnibm_sh_lowconfimpact_risklevel5)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN "+str(count_vulnibm_iot_lowconfimpact_risklevel4+count_vulnibm_sh_lowconfimpact_risklevel4)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN "+str(count_vulnibm_iot_lowconfimpact_risklevel3+count_vulnibm_sh_lowconfimpact_risklevel3)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN "+str(count_vulnibm_iot_lowconfimpact_risklevel2+count_vulnibm_sh_lowconfimpact_risklevel2)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN "+str(count_vulnibm_iot_lowconfimpact_risklevel1+count_vulnibm_sh_lowconfimpact_risklevel1)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN "+str(count_vulnibm_iot_lowconfimpact_risklevel0+count_vulnibm_sh_lowconfimpact_risklevel0)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 0 \n")
print("\n")


print("*******************************PORCENTAJES RELACION DE IMPACTO DE CONFIDENCIALIDAD/PUNTUACION BASE PARA OBJETOS DE TIPO VULNERABILIDAD IBM PARTE IOT Y SMART HOME CONJUNTAS*******************************")
print("\n")                            
print("\n")
print(" DE UN TOTAL DE "+str(count_vulnibm_iot_confidentiality_impact+count_vulnibm_sh_confidentiality_impact)+" VULNERABILIDADES CON VALOR DE CONFIDENCIALIDAD ESPECIFICADO:\n") 
print("\n")
print("   - LOS PORCENTAJES DE VALORES DE IMPACTO DE CONFIDENCIALIDAD SON LOS SIGUIENTES:  \n")
print("      -    EN EL "+str(float((((count_vulnibm_iot_highconfimpact+count_vulnibm_sh_highconfimpact)*100)/(count_vulnibm_iot_confidentiality_impact+count_vulnibm_sh_confidentiality_impact))))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO, LOS PORCENTAJES DE NIVEL DE RIESGO SON LOS SIGUIENTES :  \n")
print("            -    EN EL"+str(float((((count_vulnibm_iot_highconfimpact_risklevel10+count_vulnibm_sh_highconfimpact_risklevel10)*100)/(count_vulnibm_iot_highconfimpact+count_vulnibm_sh_highconfimpact))))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES 10 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_highconfimpact_risklevel9+count_vulnibm_sh_highconfimpact_risklevel9)*100)/(count_vulnibm_iot_highconfimpact+count_vulnibm_sh_highconfimpact))))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_highconfimpact_risklevel8+count_vulnibm_sh_highconfimpact_risklevel8)*100)/(count_vulnibm_iot_highconfimpact+count_vulnibm_sh_highconfimpact))))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_highconfimpact_risklevel7+count_vulnibm_sh_highconfimpact_risklevel7)*100)/(count_vulnibm_iot_highconfimpact+count_vulnibm_sh_highconfimpact))))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_highconfimpact_risklevel6+count_vulnibm_sh_highconfimpact_risklevel6)*100)/(count_vulnibm_iot_highconfimpact+count_vulnibm_sh_highconfimpact))))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_highconfimpact_risklevel5+count_vulnibm_sh_highconfimpact_risklevel5)*100)/(count_vulnibm_iot_highconfimpact+count_vulnibm_sh_highconfimpact))))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_highconfimpact_risklevel4+count_vulnibm_sh_highconfimpact_risklevel4)*100)/(count_vulnibm_iot_highconfimpact+count_vulnibm_sh_highconfimpact))))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_highconfimpact_risklevel3+count_vulnibm_sh_highconfimpact_risklevel3)*100)/(count_vulnibm_iot_highconfimpact+count_vulnibm_sh_highconfimpact))))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_highconfimpact_risklevel2+count_vulnibm_sh_highconfimpact_risklevel2)*100)/(count_vulnibm_iot_highconfimpact+count_vulnibm_sh_highconfimpact))))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_highconfimpact_risklevel1+count_vulnibm_sh_highconfimpact_risklevel1)*100)/(count_vulnibm_iot_highconfimpact+count_vulnibm_sh_highconfimpact))))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_highconfimpact_risklevel0+count_vulnibm_sh_highconfimpact_risklevel0)*100)/(count_vulnibm_iot_highconfimpact+count_vulnibm_sh_highconfimpact))))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 0 \n")
print("            -    EL VALOR MEDIO DE PUNTUACION BASE ES  "+str(float(((count_vulnibm_iot_highconfimpact_risklevel+count_vulnibm_sh_highconfimpact_risklevel)/(count_vulnibm_iot_highconfimpact+count_vulnibm_sh_highconfimpact))))+"\n")
print("\n")
print("      -    EN EL "+str(float((((count_vulnibm_iot_lowconfimpact+count_vulnibm_sh_lowconfimpact)*100)/(count_vulnibm_iot_confidentiality_impact+count_vulnibm_sh_confidentiality_impact))))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO, LOS PORCENTAJES DE NIVEL DE RIESGO SON LOS SIGUIENTES :  \n")
print("            -    EN EL"+str(float((((count_vulnibm_iot_lowconfimpact_risklevel10+count_vulnibm_sh_lowconfimpact_risklevel10)*100)/(count_vulnibm_iot_lowconfimpact+count_vulnibm_sh_lowconfimpact))))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES 10 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_lowconfimpact_risklevel9+count_vulnibm_sh_lowconfimpact_risklevel9)*100)/(count_vulnibm_iot_lowconfimpact+count_vulnibm_sh_lowconfimpact))))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_lowconfimpact_risklevel8+count_vulnibm_sh_lowconfimpact_risklevel8)*100)/(count_vulnibm_iot_lowconfimpact+count_vulnibm_sh_lowconfimpact))))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_lowconfimpact_risklevel7+count_vulnibm_sh_lowconfimpact_risklevel7)*100)/(count_vulnibm_iot_lowconfimpact+count_vulnibm_sh_lowconfimpact))))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_lowconfimpact_risklevel6+count_vulnibm_sh_lowconfimpact_risklevel6)*100)/(count_vulnibm_iot_lowconfimpact+count_vulnibm_sh_lowconfimpact))))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_lowconfimpact_risklevel5+count_vulnibm_sh_lowconfimpact_risklevel5)*100)/(count_vulnibm_iot_lowconfimpact+count_vulnibm_sh_lowconfimpact))))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_lowconfimpact_risklevel4+count_vulnibm_sh_lowconfimpact_risklevel4)*100)/(count_vulnibm_iot_lowconfimpact+count_vulnibm_sh_lowconfimpact))))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_lowconfimpact_risklevel3+count_vulnibm_sh_lowconfimpact_risklevel3)*100)/(count_vulnibm_iot_lowconfimpact+count_vulnibm_sh_lowconfimpact))))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_lowconfimpact_risklevel2+count_vulnibm_sh_lowconfimpact_risklevel2)*100)/(count_vulnibm_iot_lowconfimpact+count_vulnibm_sh_lowconfimpact))))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_lowconfimpact_risklevel1+count_vulnibm_sh_lowconfimpact_risklevel1)*100)/(count_vulnibm_iot_lowconfimpact+count_vulnibm_sh_lowconfimpact))))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_lowconfimpact_risklevel0+count_vulnibm_sh_lowconfimpact_risklevel0)*100)/(count_vulnibm_iot_lowconfimpact+count_vulnibm_sh_lowconfimpact))))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 0 \n")
print("            -    EL VALOR MEDIO DE PUNTUACION BASE ES  "+str(float(((count_vulnibm_iot_lowconfimpact_risklevel+count_vulnibm_sh_lowconfimpact_risklevel)/(count_vulnibm_iot_lowconfimpact+count_vulnibm_sh_lowconfimpact))))+"\n")
print("\n")




