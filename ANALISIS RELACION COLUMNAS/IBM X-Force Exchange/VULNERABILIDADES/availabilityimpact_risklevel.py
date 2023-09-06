

import pandas as pd
from datetime import datetime,timedelta



#Abro los ficheros con los que voy a tratar




df_vulnibm_iot = pd.read_excel('vulnerabilidades_ibm_iot_2023.xlsx')
#Variables para almacenar el contador total de valores de DISPONIBILIDAD
count_vulnibm_iot_availability_impact=0
#Variables para almacenar el contador de un valor concreto de impacto de DISPONIBILIDAD
count_vulnibm_iot_highavaimpact=0
#Variable para almacenar la suma de valores de nivel de riesgo para calcular despues la media para un valor de DISPONIBILIDAD dado
count_vulnibm_iot_highavaimpact_risklevel=0
#Contador de valores de nivel de riesgo dado un nivel de impacto de DISPONIBILIDAD concreto
count_vulnibm_iot_highavaimpact_risklevel10=0
count_vulnibm_iot_highavaimpact_risklevel9=0
count_vulnibm_iot_highavaimpact_risklevel8=0
count_vulnibm_iot_highavaimpact_risklevel7=0
count_vulnibm_iot_highavaimpact_risklevel6=0
count_vulnibm_iot_highavaimpact_risklevel5=0
count_vulnibm_iot_highavaimpact_risklevel4=0
count_vulnibm_iot_highavaimpact_risklevel3=0
count_vulnibm_iot_highavaimpact_risklevel2=0
count_vulnibm_iot_highavaimpact_risklevel1=0
count_vulnibm_iot_highavaimpact_risklevel0=0



count_vulnibm_iot_lowavaimpact=0
count_vulnibm_iot_lowavaimpact_risklevel=0
count_vulnibm_iot_lowavaimpact_risklevel10=0
count_vulnibm_iot_lowavaimpact_risklevel9=0
count_vulnibm_iot_lowavaimpact_risklevel8=0
count_vulnibm_iot_lowavaimpact_risklevel7=0
count_vulnibm_iot_lowavaimpact_risklevel6=0
count_vulnibm_iot_lowavaimpact_risklevel5=0
count_vulnibm_iot_lowavaimpact_risklevel4=0
count_vulnibm_iot_lowavaimpact_risklevel3=0
count_vulnibm_iot_lowavaimpact_risklevel2=0
count_vulnibm_iot_lowavaimpact_risklevel1=0
count_vulnibm_iot_lowavaimpact_risklevel0=0



#Comprobamos el valor de impacto de DISPONIBILIDAD
for r in range(0,len(df_vulnibm_iot["x_xfe_cvss_availability_impact"])):
    if(isinstance(df_vulnibm_iot["x_xfe_cvss_availability_impact"][r],str)):
        aux_str=df_vulnibm_iot["x_xfe_cvss_availability_impact"][r].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
        if(aux_str!='NONE' or aux_str!='None'):
            count_vulnibm_iot_availability_impact+=1
            #Comprobamos el valor de impacto de DISPONIBILIDAD
            if('High' in aux_str):
                count_vulnibm_iot_highavaimpact+=1
                #Sumamos el valor de nivel de riesgo para posteriormente calcular la media
                count_vulnibm_iot_highavaimpact_risklevel+=float(df_vulnibm_iot["x_xfe_risk_level"][r])
                #Comprobamos el valor de nivel de riesgo
                if(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 10.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=9.0)):
                    count_vulnibm_iot_highavaimpact_risklevel9+=1
                elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 9.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=8.0)):
                    count_vulnibm_iot_highavaimpact_risklevel8+=1
                elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 8.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=7.0)):
                    count_vulnibm_iot_highavaimpact_risklevel7+=1
                elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 7.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=6.0)):
                    count_vulnibm_iot_highavaimpact_risklevel6+=1
                elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 6.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=5.0)):
                    count_vulnibm_iot_highavaimpact_risklevel5+=1
                elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 5.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=4.0)):
                    count_vulnibm_iot_highavaimpact_risklevel4+=1
                elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 4.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=3.0)):
                    count_vulnibm_iot_highavaimpact_risklevel3+=1
                elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 3.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=2.0)):
                    count_vulnibm_iot_highavaimpact_risklevel2+=1
                elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 2.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=1.0)):
                    count_vulnibm_iot_highavaimpact_risklevel1+=1
                elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 1.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=0.0)):
                    count_vulnibm_iot_highavaimpact_risklevel0+=1
                elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) == 10.0)):
                    count_vulnibm_iot_highavaimpact_risklevel10+=1

            elif('Low' in aux_str):

                count_vulnibm_iot_lowavaimpact+=1
                count_vulnibm_iot_lowavaimpact_risklevel+=float(df_vulnibm_iot["x_xfe_risk_level"][r])
                if(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 10.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=9.0)):
                    count_vulnibm_iot_lowavaimpact_risklevel9+=1
                elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 9.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=8.0)):
                    count_vulnibm_iot_lowavaimpact_risklevel8+=1
                elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 8.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=7.0)):
                    count_vulnibm_iot_lowavaimpact_risklevel7+=1
                elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 7.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=6.0)):
                    count_vulnibm_iot_lowavaimpact_risklevel6+=1
                elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 6.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=5.0)):
                    count_vulnibm_iot_lowavaimpact_risklevel5+=1
                elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 5.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=4.0)):
                    count_vulnibm_iot_lowavaimpact_risklevel4+=1
                elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 4.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=3.0)):
                    count_vulnibm_iot_lowavaimpact_risklevel3+=1
                elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 3.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=2.0)):
                    count_vulnibm_iot_lowavaimpact_risklevel2+=1
                elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 2.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=1.0)):
                    count_vulnibm_iot_lowavaimpact_risklevel1+=1
                elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 1.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=0.0)):
                    count_vulnibm_iot_lowavaimpact_risklevel0+=1
                elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) == 10.0)):
                    count_vulnibm_iot_lowavaimpact_risklevel10+=1


            
print("*******************************ESTADÍSTICAS RELACION DE IMPACTO DE DISPONIBILIDAD/PUNTUACION BASE PARA OBJETOS DE TIPO VULNERABILIDAD IBM PARTE IOT*******************************")
print("\n")                            
print("\n")
print(" DE UN TOTAL DE "+str(count_vulnibm_iot_availability_impact)+" VULNERABILIDADES CON VALOR DE DISPONIBILIDAD ESPECIFICADO:\n") 
print("\n")
print("   - LAS ESTADISTICAS DE VALORES DE IMPACTO DE DISPONIBILIDAD SON LAS SIGUIENTES:  \n")
print("      -    EN  "+str(count_vulnibm_iot_highavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO, LAS ESTADÍSTICAS DE NIVEL DE RIESGO SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_highavaimpact_risklevel10)+" VULNERABILIDADES EL NIVEL DE RIESGO ES 10 \n")
print("            -    EN  "+str(count_vulnibm_iot_highavaimpact_risklevel9)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN  "+str(count_vulnibm_iot_highavaimpact_risklevel8)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN  "+str(count_vulnibm_iot_highavaimpact_risklevel7)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN  "+str(count_vulnibm_iot_highavaimpact_risklevel6)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN "+str(count_vulnibm_iot_highavaimpact_risklevel5)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN "+str(count_vulnibm_iot_highavaimpact_risklevel4)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN "+str(count_vulnibm_iot_highavaimpact_risklevel3)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN "+str(count_vulnibm_iot_highavaimpact_risklevel2)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN "+str(count_vulnibm_iot_highavaimpact_risklevel1)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN "+str(count_vulnibm_iot_highavaimpact_risklevel0)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 0 \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_lowavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO, LAS ESTADÍSTICAS DE NIVEL DE RIESGO SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_lowavaimpact_risklevel10)+" VULNERABILIDADES EL NIVEL DE RIESGO ES 10 \n")
print("            -    EN  "+str(count_vulnibm_iot_lowavaimpact_risklevel9)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN  "+str(count_vulnibm_iot_lowavaimpact_risklevel8)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN  "+str(count_vulnibm_iot_lowavaimpact_risklevel7)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN  "+str(count_vulnibm_iot_lowavaimpact_risklevel6)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN "+str(count_vulnibm_iot_lowavaimpact_risklevel5)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN "+str(count_vulnibm_iot_lowavaimpact_risklevel4)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN "+str(count_vulnibm_iot_lowavaimpact_risklevel3)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN "+str(count_vulnibm_iot_lowavaimpact_risklevel2)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN "+str(count_vulnibm_iot_lowavaimpact_risklevel1)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN "+str(count_vulnibm_iot_lowavaimpact_risklevel0)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 0 \n")
print("\n")


print("*******************************PORCENTAJE RELACION DE IMPACTO DE DISPONIBILIDAD/PUNTUACION BASE PARA OBJETOS DE TIPO VULNERABILIDAD IBM PARTE IOT*******************************")
print("\n")                            
print("\n")
print(" DE UN TOTAL DE "+str(count_vulnibm_iot_availability_impact)+" VULNERABILIDADES CON VALOR DE DISPONIBILIDAD ESPECIFICADO:\n") 
print("\n")
print("   - LOS PORCENTAJES DE VALORES DE IMPACTO DE DISPONIBILIDAD SON LOS SIGUIENTES:  \n")
print("      -    EN EL  "+str(float(((count_vulnibm_iot_highavaimpact*100)/count_vulnibm_iot_availability_impact)))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO, LOS PORCENTAJES DE NIVEL DE RIESGO SON LOS SIGUIENTES :  \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_highavaimpact_risklevel10*100)/count_vulnibm_iot_highavaimpact)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES 10 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_highavaimpact_risklevel9*100)/count_vulnibm_iot_highavaimpact)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_highavaimpact_risklevel8*100)/count_vulnibm_iot_highavaimpact)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_highavaimpact_risklevel7*100)/count_vulnibm_iot_highavaimpact)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_highavaimpact_risklevel6*100)/count_vulnibm_iot_highavaimpact)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_highavaimpact_risklevel5*100)/count_vulnibm_iot_highavaimpact)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_highavaimpact_risklevel4*100)/count_vulnibm_iot_highavaimpact)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_highavaimpact_risklevel3*100)/count_vulnibm_iot_highavaimpact)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_highavaimpact_risklevel2*100)/count_vulnibm_iot_highavaimpact)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_highavaimpact_risklevel1*100)/count_vulnibm_iot_highavaimpact)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_highavaimpact_risklevel0*100)/count_vulnibm_iot_highavaimpact)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 0 \n")
print("            -    EL VALOR MEDIO DE PUNTUACION BASE ES  "+str(float(((count_vulnibm_iot_highavaimpact_risklevel)/count_vulnibm_iot_highavaimpact)))+"\n")
print("\n")
print("      -    EN EL  "+str(float(((count_vulnibm_iot_lowavaimpact*100)/count_vulnibm_iot_availability_impact)))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO, LOS PORCENTAJES DE NIVEL DE RIESGO SON LOS SIGUIENTES :  \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_lowavaimpact_risklevel10*100)/count_vulnibm_iot_lowavaimpact)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES 10 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_lowavaimpact_risklevel9*100)/count_vulnibm_iot_lowavaimpact)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_lowavaimpact_risklevel8*100)/count_vulnibm_iot_lowavaimpact)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_lowavaimpact_risklevel7*100)/count_vulnibm_iot_lowavaimpact)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_lowavaimpact_risklevel6*100)/count_vulnibm_iot_lowavaimpact)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_lowavaimpact_risklevel5*100)/count_vulnibm_iot_lowavaimpact)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_lowavaimpact_risklevel4*100)/count_vulnibm_iot_lowavaimpact)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_lowavaimpact_risklevel3*100)/count_vulnibm_iot_lowavaimpact)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_lowavaimpact_risklevel2*100)/count_vulnibm_iot_lowavaimpact)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_lowavaimpact_risklevel1*100)/count_vulnibm_iot_lowavaimpact)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_lowavaimpact_risklevel0*100)/count_vulnibm_iot_lowavaimpact)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 0 \n")
print("            -    EL VALOR MEDIO DE PUNTUACION BASE ES  "+str(float(((count_vulnibm_iot_lowavaimpact_risklevel)/count_vulnibm_iot_lowavaimpact)))+"\n")
print("\n")



#Abro los ficheros con los que voy a tratar




df_vulnibm_sh = pd.read_excel('vulnerabilidades_ibm_smart_home_2023.xlsx')

#Variables para almacenar el contador total de valores de DISPONIBILIDAD
count_vulnibm_sh_availability_impact=0
#Variables para almacenar el contador de un valor concreto de impacto de DISPONIBILIDAD
count_vulnibm_sh_highavaimpact=0
#Variable para almacenar la suma de valores de nivel de riesgo para calcular despues la media para un valor de DISPONIBILIDAD dado
count_vulnibm_sh_highavaimpact_risklevel=0
#Contador de valores de nivel de riesgo dado un nivel de impacto de DISPONIBILIDAD concreto
count_vulnibm_sh_highavaimpact_risklevel10=0
count_vulnibm_sh_highavaimpact_risklevel9=0
count_vulnibm_sh_highavaimpact_risklevel8=0
count_vulnibm_sh_highavaimpact_risklevel7=0
count_vulnibm_sh_highavaimpact_risklevel6=0
count_vulnibm_sh_highavaimpact_risklevel5=0
count_vulnibm_sh_highavaimpact_risklevel4=0
count_vulnibm_sh_highavaimpact_risklevel3=0
count_vulnibm_sh_highavaimpact_risklevel2=0
count_vulnibm_sh_highavaimpact_risklevel1=0
count_vulnibm_sh_highavaimpact_risklevel0=0



count_vulnibm_sh_lowavaimpact=0
count_vulnibm_sh_lowavaimpact_risklevel=0
count_vulnibm_sh_lowavaimpact_risklevel10=0
count_vulnibm_sh_lowavaimpact_risklevel9=0
count_vulnibm_sh_lowavaimpact_risklevel8=0
count_vulnibm_sh_lowavaimpact_risklevel7=0
count_vulnibm_sh_lowavaimpact_risklevel6=0
count_vulnibm_sh_lowavaimpact_risklevel5=0
count_vulnibm_sh_lowavaimpact_risklevel4=0
count_vulnibm_sh_lowavaimpact_risklevel3=0
count_vulnibm_sh_lowavaimpact_risklevel2=0
count_vulnibm_sh_lowavaimpact_risklevel1=0
count_vulnibm_sh_lowavaimpact_risklevel0=0



#Comprobamos el valor de impacto de DISPONIBILIDAD
for r in range(0,len(df_vulnibm_sh["x_xfe_cvss_availability_impact"])):  
    if(isinstance(df_vulnibm_sh["x_xfe_cvss_availability_impact"][r],str)):
        aux_str=df_vulnibm_sh["x_xfe_cvss_availability_impact"][r].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
        if(aux_str!='NONE' or aux_str!='None'):
            count_vulnibm_sh_availability_impact+=1
            #Comprobamos el valor de impacto de DISPONIBILIDAD
            if('High' in aux_str):
                count_vulnibm_sh_highavaimpact+=1
                #Sumamos el valor de nivel de riesgo para posteriormente calcular la media
                count_vulnibm_sh_highavaimpact_risklevel+=float(df_vulnibm_sh["x_xfe_risk_level"][r])
                #Comprobamos el valor de nivel de riesgo
                if(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 10.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=9.0)):
                    count_vulnibm_sh_highavaimpact_risklevel9+=1
                elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 9.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=8.0)):
                    count_vulnibm_sh_highavaimpact_risklevel8+=1
                elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 8.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=7.0)):
                    count_vulnibm_sh_highavaimpact_risklevel7+=1
                elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 7.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=6.0)):
                    count_vulnibm_sh_highavaimpact_risklevel6+=1
                elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 6.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=5.0)):
                    count_vulnibm_sh_highavaimpact_risklevel5+=1
                elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 5.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=4.0)):
                    count_vulnibm_sh_highavaimpact_risklevel4+=1
                elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 4.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=3.0)):
                    count_vulnibm_sh_highavaimpact_risklevel3+=1
                elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 3.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=2.0)):
                    count_vulnibm_sh_highavaimpact_risklevel2+=1
                elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 2.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=1.0)):
                    count_vulnibm_sh_highavaimpact_risklevel1+=1
                elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 1.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=0.0)):
                    count_vulnibm_sh_highavaimpact_risklevel0+=1
                elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) == 10.0)):
                    count_vulnibm_sh_highavaimpact_risklevel10+=1

            elif('Low' in aux_str):

                count_vulnibm_sh_lowavaimpact+=1
                count_vulnibm_sh_lowavaimpact_risklevel+=float(df_vulnibm_sh["x_xfe_risk_level"][r])
                if(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 10.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=9.0)):
                    count_vulnibm_sh_lowavaimpact_risklevel9+=1
                elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 9.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=8.0)):
                    count_vulnibm_sh_lowavaimpact_risklevel8+=1
                elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 8.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=7.0)):
                    count_vulnibm_sh_lowavaimpact_risklevel7+=1
                elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 7.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=6.0)):
                    count_vulnibm_sh_lowavaimpact_risklevel6+=1
                elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 6.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=5.0)):
                    count_vulnibm_sh_lowavaimpact_risklevel5+=1
                elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 5.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=4.0)):
                    count_vulnibm_sh_lowavaimpact_risklevel4+=1
                elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 4.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=3.0)):
                    count_vulnibm_sh_lowavaimpact_risklevel3+=1
                elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 3.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=2.0)):
                    count_vulnibm_sh_lowavaimpact_risklevel2+=1
                elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 2.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=1.0)):
                    count_vulnibm_sh_lowavaimpact_risklevel1+=1
                elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 1.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=0.0)):
                    count_vulnibm_sh_lowavaimpact_risklevel0+=1
                elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) == 10.0)):
                    count_vulnibm_sh_lowavaimpact_risklevel10+=1


            
                
print("*******************************ESTADÍSTICAS RELACION DE IMPACTO DE DISPONIBILIDAD/PUNTUACION BASE PARA OBJETOS DE TIPO VULNERABILIDAD IBM PARTE SMART HOME*******************************")
print("\n")                            
print("\n")
print(" DE UN TOTAL DE "+str(count_vulnibm_sh_availability_impact)+" VULNERABILIDADES CON VALOR DE DISPONIBILIDAD ESPECIFICADO:\n") 
print("\n")
print("   - LAS ESTADISTICAS DE VALORES DE IMPACTO DE DISPONIBILIDAD SON LAS SIGUIENTES:  \n")
print("      -    EN  "+str(count_vulnibm_sh_highavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO, LAS ESTADÍSTICAS DE NIVEL DE RIESGO SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_sh_highavaimpact_risklevel10)+" VULNERABILIDADES EL NIVEL DE RIESGO ES 10 \n")
print("            -    EN  "+str(count_vulnibm_sh_highavaimpact_risklevel9)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN  "+str(count_vulnibm_sh_highavaimpact_risklevel8)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN  "+str(count_vulnibm_sh_highavaimpact_risklevel7)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN  "+str(count_vulnibm_sh_highavaimpact_risklevel6)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN "+str(count_vulnibm_sh_highavaimpact_risklevel5)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN "+str(count_vulnibm_sh_highavaimpact_risklevel4)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN "+str(count_vulnibm_sh_highavaimpact_risklevel3)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN "+str(count_vulnibm_sh_highavaimpact_risklevel2)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN "+str(count_vulnibm_sh_highavaimpact_risklevel1)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN "+str(count_vulnibm_sh_highavaimpact_risklevel0)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 0 \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_sh_lowavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO, LAS ESTADÍSTICAS DE NIVEL DE RIESGO SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_sh_lowavaimpact_risklevel10)+" VULNERABILIDADES EL NIVEL DE RIESGO ES 10 \n")
print("            -    EN  "+str(count_vulnibm_sh_lowavaimpact_risklevel9)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN  "+str(count_vulnibm_sh_lowavaimpact_risklevel8)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN  "+str(count_vulnibm_sh_lowavaimpact_risklevel7)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN  "+str(count_vulnibm_sh_lowavaimpact_risklevel6)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN "+str(count_vulnibm_sh_lowavaimpact_risklevel5)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN "+str(count_vulnibm_sh_lowavaimpact_risklevel4)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN "+str(count_vulnibm_sh_lowavaimpact_risklevel3)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN "+str(count_vulnibm_sh_lowavaimpact_risklevel2)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN "+str(count_vulnibm_sh_lowavaimpact_risklevel1)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN "+str(count_vulnibm_sh_lowavaimpact_risklevel0)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 0 \n")
print("\n")




print("*******************************PORCENTAJE RELACION DE IMPACTO DE DISPONIBILIDAD/PUNTUACION BASE PARA OBJETOS DE TIPO VULNERABILIDAD IBM PARTE SMART HOME*******************************")
print("\n")                            
print("\n")
print(" DE UN TOTAL DE "+str(count_vulnibm_sh_availability_impact)+" VULNERABILIDADES CON VALOR DE DISPONIBILIDAD ESPECIFICADO:\n") 
print("\n")
print("   - LOS PORCENTAJES DE VALORES DE IMPACTO DE DISPONIBILIDAD SON LOS SIGUIENTES:  \n")
print("      -    EN EL  "+str(float(((count_vulnibm_sh_highavaimpact*100)/count_vulnibm_sh_availability_impact)))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO, LOS PORCENTAJES DE NIVEL DE RIESGO SON LOS SIGUIENTES :  \n")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_highavaimpact_risklevel10*100)/count_vulnibm_sh_highavaimpact)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES 10 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_highavaimpact_risklevel9*100)/count_vulnibm_sh_highavaimpact)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_highavaimpact_risklevel8*100)/count_vulnibm_sh_highavaimpact)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_highavaimpact_risklevel7*100)/count_vulnibm_sh_highavaimpact)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_highavaimpact_risklevel6*100)/count_vulnibm_sh_highavaimpact)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN EL "+str(float(((count_vulnibm_sh_highavaimpact_risklevel5*100)/count_vulnibm_sh_highavaimpact)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN EL "+str(float(((count_vulnibm_sh_highavaimpact_risklevel4*100)/count_vulnibm_sh_highavaimpact)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN EL "+str(float(((count_vulnibm_sh_highavaimpact_risklevel3*100)/count_vulnibm_sh_highavaimpact)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN EL "+str(float(((count_vulnibm_sh_highavaimpact_risklevel2*100)/count_vulnibm_sh_highavaimpact)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN EL "+str(float(((count_vulnibm_sh_highavaimpact_risklevel1*100)/count_vulnibm_sh_highavaimpact)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN EL "+str(float(((count_vulnibm_sh_highavaimpact_risklevel0*100)/count_vulnibm_sh_highavaimpact)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 0 \n")
print("            -    EL VALOR MEDIO DE PUNTUACION BASE ES  "+str(float(((count_vulnibm_sh_highavaimpact_risklevel)/count_vulnibm_sh_highavaimpact)))+"\n")
print("\n")
print("      -    EN EL  "+str(float(((count_vulnibm_sh_lowavaimpact*100)/count_vulnibm_sh_availability_impact)))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO, LOS PORCENTAJES DE NIVEL DE RIESGO SON LOS SIGUIENTES :  \n")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_lowavaimpact_risklevel10*100)/count_vulnibm_sh_lowavaimpact)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES 10 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_lowavaimpact_risklevel9*100)/count_vulnibm_sh_lowavaimpact)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_lowavaimpact_risklevel8*100)/count_vulnibm_sh_lowavaimpact)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_lowavaimpact_risklevel7*100)/count_vulnibm_sh_lowavaimpact)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_lowavaimpact_risklevel6*100)/count_vulnibm_sh_lowavaimpact)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN EL "+str(float(((count_vulnibm_sh_lowavaimpact_risklevel5*100)/count_vulnibm_sh_lowavaimpact)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN EL "+str(float(((count_vulnibm_sh_lowavaimpact_risklevel4*100)/count_vulnibm_sh_lowavaimpact)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN EL "+str(float(((count_vulnibm_sh_lowavaimpact_risklevel3*100)/count_vulnibm_sh_lowavaimpact)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN EL "+str(float(((count_vulnibm_sh_lowavaimpact_risklevel2*100)/count_vulnibm_sh_lowavaimpact)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN EL "+str(float(((count_vulnibm_sh_lowavaimpact_risklevel1*100)/count_vulnibm_sh_lowavaimpact)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN EL "+str(float(((count_vulnibm_sh_lowavaimpact_risklevel0*100)/count_vulnibm_sh_lowavaimpact)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 0 \n")
print("            -    EL VALOR MEDIO DE PUNTUACION BASE ES  "+str(float(((count_vulnibm_sh_lowavaimpact_risklevel)/count_vulnibm_sh_lowavaimpact)))+"\n")
print("\n")





print("*******************************ESTADÍSTICAS RELACION DE IMPACTO DE DISPONIBILIDAD/PUNTUACION BASE PARA OBJETOS DE TIPO VULNERABILIDAD IBM PARTE IOT Y SMART HOME CONJUNTAS*******************************")
print("\n")                            
print("\n")
print(" DE UN TOTAL DE "+str(count_vulnibm_iot_availability_impact+count_vulnibm_sh_availability_impact)+" VULNERABILIDADES CON VALOR DE DISPONIBILIDAD ESPECIFICADO:\n") 
print("\n")
print("   - LAS ESTADISTICAS DE VALORES DE IMPACTO DE DISPONIBILIDAD SON LAS SIGUIENTES:  \n")
print("      -    EN  "+str(count_vulnibm_iot_highavaimpact+count_vulnibm_sh_highavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO, LAS ESTADÍSTICAS DE NIVEL DE RIESGO SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_highavaimpact_risklevel10+count_vulnibm_sh_highavaimpact_risklevel10)+" VULNERABILIDADES EL NIVEL DE RIESGO ES 10 \n")
print("            -    EN  "+str(count_vulnibm_iot_highavaimpact_risklevel9+count_vulnibm_sh_highavaimpact_risklevel9)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN  "+str(count_vulnibm_iot_highavaimpact_risklevel8+count_vulnibm_sh_highavaimpact_risklevel8)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN  "+str(count_vulnibm_iot_highavaimpact_risklevel7+count_vulnibm_sh_highavaimpact_risklevel7)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN  "+str(count_vulnibm_iot_highavaimpact_risklevel6+count_vulnibm_sh_highavaimpact_risklevel6)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN "+str(count_vulnibm_iot_highavaimpact_risklevel5+count_vulnibm_sh_highavaimpact_risklevel5)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN "+str(count_vulnibm_iot_highavaimpact_risklevel4+count_vulnibm_sh_highavaimpact_risklevel4)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN "+str(count_vulnibm_iot_highavaimpact_risklevel3+count_vulnibm_sh_highavaimpact_risklevel3)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN "+str(count_vulnibm_iot_highavaimpact_risklevel2+count_vulnibm_sh_highavaimpact_risklevel2)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN "+str(count_vulnibm_iot_highavaimpact_risklevel1+count_vulnibm_sh_highavaimpact_risklevel1)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN "+str(count_vulnibm_iot_highavaimpact_risklevel0+count_vulnibm_sh_highavaimpact_risklevel0)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 0 \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_lowavaimpact+count_vulnibm_sh_lowavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO, LAS ESTADÍSTICAS DE NIVEL DE RIESGO SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_lowavaimpact_risklevel10+count_vulnibm_sh_lowavaimpact_risklevel10)+" VULNERABILIDADES EL NIVEL DE RIESGO ES 10 \n")
print("            -    EN  "+str(count_vulnibm_iot_lowavaimpact_risklevel9+count_vulnibm_sh_lowavaimpact_risklevel9)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN  "+str(count_vulnibm_iot_lowavaimpact_risklevel8+count_vulnibm_sh_lowavaimpact_risklevel8)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN  "+str(count_vulnibm_iot_lowavaimpact_risklevel7+count_vulnibm_sh_lowavaimpact_risklevel7)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN  "+str(count_vulnibm_iot_lowavaimpact_risklevel6+count_vulnibm_sh_lowavaimpact_risklevel6)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN "+str(count_vulnibm_iot_lowavaimpact_risklevel5+count_vulnibm_sh_lowavaimpact_risklevel5)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN "+str(count_vulnibm_iot_lowavaimpact_risklevel4+count_vulnibm_sh_lowavaimpact_risklevel4)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN "+str(count_vulnibm_iot_lowavaimpact_risklevel3+count_vulnibm_sh_lowavaimpact_risklevel3)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN "+str(count_vulnibm_iot_lowavaimpact_risklevel2+count_vulnibm_sh_lowavaimpact_risklevel2)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN "+str(count_vulnibm_iot_lowavaimpact_risklevel1+count_vulnibm_sh_lowavaimpact_risklevel1)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN "+str(count_vulnibm_iot_lowavaimpact_risklevel0+count_vulnibm_sh_lowavaimpact_risklevel0)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 0 \n")
print("\n")


print("*******************************PORCENTAJES RELACION DE IMPACTO DE DISPONIBILIDAD/PUNTUACION BASE PARA OBJETOS DE TIPO VULNERABILIDAD IBM PARTE IOT Y SMART HOME CONJUNTAS*******************************")
print("\n")                            
print("\n")
print(" DE UN TOTAL DE "+str(count_vulnibm_iot_availability_impact+count_vulnibm_sh_availability_impact)+" VULNERABILIDADES CON VALOR DE DISPONIBILIDAD ESPECIFICADO:\n") 
print("\n")
print("   - LOS PORCENTAJES DE VALORES DE IMPACTO DE DISPONIBILIDAD SON LOS SIGUIENTES:  \n")
print("      -    EN EL "+str(float((((count_vulnibm_iot_highavaimpact+count_vulnibm_sh_highavaimpact)*100)/(count_vulnibm_iot_availability_impact+count_vulnibm_sh_availability_impact))))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO, LOS PORCENTAJES DE NIVEL DE RIESGO SON LOS SIGUIENTES :  \n")
print("            -    EN EL"+str(float((((count_vulnibm_iot_highavaimpact_risklevel10+count_vulnibm_sh_highavaimpact_risklevel10)*100)/(count_vulnibm_iot_highavaimpact+count_vulnibm_sh_highavaimpact))))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES 10 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_highavaimpact_risklevel9+count_vulnibm_sh_highavaimpact_risklevel9)*100)/(count_vulnibm_iot_highavaimpact+count_vulnibm_sh_highavaimpact))))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_highavaimpact_risklevel8+count_vulnibm_sh_highavaimpact_risklevel8)*100)/(count_vulnibm_iot_highavaimpact+count_vulnibm_sh_highavaimpact))))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_highavaimpact_risklevel7+count_vulnibm_sh_highavaimpact_risklevel7)*100)/(count_vulnibm_iot_highavaimpact+count_vulnibm_sh_highavaimpact))))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_highavaimpact_risklevel6+count_vulnibm_sh_highavaimpact_risklevel6)*100)/(count_vulnibm_iot_highavaimpact+count_vulnibm_sh_highavaimpact))))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_highavaimpact_risklevel5+count_vulnibm_sh_highavaimpact_risklevel5)*100)/(count_vulnibm_iot_highavaimpact+count_vulnibm_sh_highavaimpact))))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_highavaimpact_risklevel4+count_vulnibm_sh_highavaimpact_risklevel4)*100)/(count_vulnibm_iot_highavaimpact+count_vulnibm_sh_highavaimpact))))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_highavaimpact_risklevel3+count_vulnibm_sh_highavaimpact_risklevel3)*100)/(count_vulnibm_iot_highavaimpact+count_vulnibm_sh_highavaimpact))))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_highavaimpact_risklevel2+count_vulnibm_sh_highavaimpact_risklevel2)*100)/(count_vulnibm_iot_highavaimpact+count_vulnibm_sh_highavaimpact))))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_highavaimpact_risklevel1+count_vulnibm_sh_highavaimpact_risklevel1)*100)/(count_vulnibm_iot_highavaimpact+count_vulnibm_sh_highavaimpact))))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_highavaimpact_risklevel0+count_vulnibm_sh_highavaimpact_risklevel0)*100)/(count_vulnibm_iot_highavaimpact+count_vulnibm_sh_highavaimpact))))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 0 \n")
print("            -    EL VALOR MEDIO DE PUNTUACION BASE ES  "+str(float(((count_vulnibm_iot_highavaimpact_risklevel+count_vulnibm_sh_highavaimpact_risklevel)/(count_vulnibm_iot_highavaimpact+count_vulnibm_sh_highavaimpact))))+"\n")
print("\n")
print("      -    EN EL "+str(float((((count_vulnibm_iot_lowavaimpact+count_vulnibm_sh_lowavaimpact)*100)/(count_vulnibm_iot_availability_impact+count_vulnibm_sh_availability_impact))))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO, LOS PORCENTAJES DE NIVEL DE RIESGO SON LOS SIGUIENTES :  \n")
print("            -    EN EL"+str(float((((count_vulnibm_iot_lowavaimpact_risklevel10+count_vulnibm_sh_lowavaimpact_risklevel10)*100)/(count_vulnibm_iot_lowavaimpact+count_vulnibm_sh_lowavaimpact))))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES 10 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_lowavaimpact_risklevel9+count_vulnibm_sh_lowavaimpact_risklevel9)*100)/(count_vulnibm_iot_lowavaimpact+count_vulnibm_sh_lowavaimpact))))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_lowavaimpact_risklevel8+count_vulnibm_sh_lowavaimpact_risklevel8)*100)/(count_vulnibm_iot_lowavaimpact+count_vulnibm_sh_lowavaimpact))))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_lowavaimpact_risklevel7+count_vulnibm_sh_lowavaimpact_risklevel7)*100)/(count_vulnibm_iot_lowavaimpact+count_vulnibm_sh_lowavaimpact))))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_lowavaimpact_risklevel6+count_vulnibm_sh_lowavaimpact_risklevel6)*100)/(count_vulnibm_iot_lowavaimpact+count_vulnibm_sh_lowavaimpact))))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_lowavaimpact_risklevel5+count_vulnibm_sh_lowavaimpact_risklevel5)*100)/(count_vulnibm_iot_lowavaimpact+count_vulnibm_sh_lowavaimpact))))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_lowavaimpact_risklevel4+count_vulnibm_sh_lowavaimpact_risklevel4)*100)/(count_vulnibm_iot_lowavaimpact+count_vulnibm_sh_lowavaimpact))))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_lowavaimpact_risklevel3+count_vulnibm_sh_lowavaimpact_risklevel3)*100)/(count_vulnibm_iot_lowavaimpact+count_vulnibm_sh_lowavaimpact))))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_lowavaimpact_risklevel2+count_vulnibm_sh_lowavaimpact_risklevel2)*100)/(count_vulnibm_iot_lowavaimpact+count_vulnibm_sh_lowavaimpact))))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_lowavaimpact_risklevel1+count_vulnibm_sh_lowavaimpact_risklevel1)*100)/(count_vulnibm_iot_lowavaimpact+count_vulnibm_sh_lowavaimpact))))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_lowavaimpact_risklevel0+count_vulnibm_sh_lowavaimpact_risklevel0)*100)/(count_vulnibm_iot_lowavaimpact+count_vulnibm_sh_lowavaimpact))))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 0 \n")
print("            -    EL VALOR MEDIO DE PUNTUACION BASE ES  "+str(float(((count_vulnibm_iot_lowavaimpact_risklevel+count_vulnibm_sh_lowavaimpact_risklevel)/(count_vulnibm_iot_lowavaimpact+count_vulnibm_sh_lowavaimpact))))+"\n")
print("\n")




