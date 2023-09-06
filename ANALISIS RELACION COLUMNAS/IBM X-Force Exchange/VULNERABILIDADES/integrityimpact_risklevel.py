

import pandas as pd
from datetime import datetime,timedelta



#Abro los ficheros con los que voy a tratar




df_vulnibm_iot = pd.read_excel('vulnerabilidades_ibm_iot_2023.xlsx')
#Variables para almacenar el contador total de valores de INTEGRIDAD
count_vulnibm_iot_integrity_impact=0
#Variables para almacenar el contador de un valor concreto de impacto de INTEGRIDAD
count_vulnibm_iot_highintimpact=0
#Variable para almacenar la suma de valores de nivel de riesgo para calcular despues la media para un valor de INTEGRIDAD dado
count_vulnibm_iot_highintimpact_risklevel=0
#Contador de valores de nivel de riesgo dado un nivel de impacto de INTEGRIDAD concreto
count_vulnibm_iot_highintimpact_risklevel10=0
count_vulnibm_iot_highintimpact_risklevel9=0
count_vulnibm_iot_highintimpact_risklevel8=0
count_vulnibm_iot_highintimpact_risklevel7=0
count_vulnibm_iot_highintimpact_risklevel6=0
count_vulnibm_iot_highintimpact_risklevel5=0
count_vulnibm_iot_highintimpact_risklevel4=0
count_vulnibm_iot_highintimpact_risklevel3=0
count_vulnibm_iot_highintimpact_risklevel2=0
count_vulnibm_iot_highintimpact_risklevel1=0
count_vulnibm_iot_highintimpact_risklevel0=0



count_vulnibm_iot_lowintimpact=0
count_vulnibm_iot_lowintimpact_risklevel=0
count_vulnibm_iot_lowintimpact_risklevel10=0
count_vulnibm_iot_lowintimpact_risklevel9=0
count_vulnibm_iot_lowintimpact_risklevel8=0
count_vulnibm_iot_lowintimpact_risklevel7=0
count_vulnibm_iot_lowintimpact_risklevel6=0
count_vulnibm_iot_lowintimpact_risklevel5=0
count_vulnibm_iot_lowintimpact_risklevel4=0
count_vulnibm_iot_lowintimpact_risklevel3=0
count_vulnibm_iot_lowintimpact_risklevel2=0
count_vulnibm_iot_lowintimpact_risklevel1=0
count_vulnibm_iot_lowintimpact_risklevel0=0



#Comprobamos el valor de impacto de INTEGRIDAD
for r in range(0,len(df_vulnibm_iot["x_xfe_cvss_integrity_impact"])):
    if(isinstance(df_vulnibm_iot["x_xfe_cvss_integrity_impact"][r],str)):
        aux_str=df_vulnibm_iot["x_xfe_cvss_integrity_impact"][r].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
        if(aux_str!='NONE' or aux_str!='None'):
            count_vulnibm_iot_integrity_impact+=1
            #Comprobamos el valor de impacto de INTEGRIDAD
            if('High' in aux_str):
                count_vulnibm_iot_highintimpact+=1
                #Sumamos el valor de nivel de riesgo para posteriormente calcular la media
                count_vulnibm_iot_highintimpact_risklevel+=float(df_vulnibm_iot["x_xfe_risk_level"][r])
                #Comprobamos el valor de nivel de riesgo
                if(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 10.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=9.0)):
                    count_vulnibm_iot_highintimpact_risklevel9+=1
                elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 9.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=8.0)):
                    count_vulnibm_iot_highintimpact_risklevel8+=1
                elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 8.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=7.0)):
                    count_vulnibm_iot_highintimpact_risklevel7+=1
                elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 7.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=6.0)):
                    count_vulnibm_iot_highintimpact_risklevel6+=1
                elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 6.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=5.0)):
                    count_vulnibm_iot_highintimpact_risklevel5+=1
                elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 5.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=4.0)):
                    count_vulnibm_iot_highintimpact_risklevel4+=1
                elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 4.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=3.0)):
                    count_vulnibm_iot_highintimpact_risklevel3+=1
                elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 3.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=2.0)):
                    count_vulnibm_iot_highintimpact_risklevel2+=1
                elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 2.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=1.0)):
                    count_vulnibm_iot_highintimpact_risklevel1+=1
                elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 1.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=0.0)):
                    count_vulnibm_iot_highintimpact_risklevel0+=1
                elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) == 10.0)):
                    count_vulnibm_iot_highintimpact_risklevel10+=1

            elif('Low' in aux_str):

                count_vulnibm_iot_lowintimpact+=1
                count_vulnibm_iot_lowintimpact_risklevel+=float(df_vulnibm_iot["x_xfe_risk_level"][r])
                if(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 10.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=9.0)):
                    count_vulnibm_iot_lowintimpact_risklevel9+=1
                elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 9.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=8.0)):
                    count_vulnibm_iot_lowintimpact_risklevel8+=1
                elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 8.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=7.0)):
                    count_vulnibm_iot_lowintimpact_risklevel7+=1
                elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 7.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=6.0)):
                    count_vulnibm_iot_lowintimpact_risklevel6+=1
                elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 6.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=5.0)):
                    count_vulnibm_iot_lowintimpact_risklevel5+=1
                elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 5.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=4.0)):
                    count_vulnibm_iot_lowintimpact_risklevel4+=1
                elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 4.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=3.0)):
                    count_vulnibm_iot_lowintimpact_risklevel3+=1
                elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 3.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=2.0)):
                    count_vulnibm_iot_lowintimpact_risklevel2+=1
                elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 2.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=1.0)):
                    count_vulnibm_iot_lowintimpact_risklevel1+=1
                elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 1.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=0.0)):
                    count_vulnibm_iot_lowintimpact_risklevel0+=1
                elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) == 10.0)):
                    count_vulnibm_iot_lowintimpact_risklevel10+=1


            
print("*******************************ESTADÍSTICAS RELACION DE IMPACTO DE INTEGRIDAD/PUNTUACION BASE PARA OBJETOS DE TIPO VULNERABILIDAD IBM PARTE IOT*******************************")
print("\n")                            
print("\n")
print(" DE UN TOTAL DE "+str(count_vulnibm_iot_integrity_impact)+" VULNERABILIDADES CON VALOR DE INTEGRIDAD ESPECIFICADO:\n") 
print("\n")
print("   - LAS ESTADISTICAS DE VALORES DE IMPACTO DE INTEGRIDAD SON LAS SIGUIENTES:  \n")
print("      -    EN  "+str(count_vulnibm_iot_highintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO, LAS ESTADÍSTICAS DE NIVEL DE RIESGO SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_highintimpact_risklevel10)+" VULNERABILIDADES EL NIVEL DE RIESGO ES 10 \n")
print("            -    EN  "+str(count_vulnibm_iot_highintimpact_risklevel9)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN  "+str(count_vulnibm_iot_highintimpact_risklevel8)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN  "+str(count_vulnibm_iot_highintimpact_risklevel7)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN  "+str(count_vulnibm_iot_highintimpact_risklevel6)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN "+str(count_vulnibm_iot_highintimpact_risklevel5)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN "+str(count_vulnibm_iot_highintimpact_risklevel4)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN "+str(count_vulnibm_iot_highintimpact_risklevel3)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN "+str(count_vulnibm_iot_highintimpact_risklevel2)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN "+str(count_vulnibm_iot_highintimpact_risklevel1)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN "+str(count_vulnibm_iot_highintimpact_risklevel0)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 0 \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_lowintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO, LAS ESTADÍSTICAS DE NIVEL DE RIESGO SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_lowintimpact_risklevel10)+" VULNERABILIDADES EL NIVEL DE RIESGO ES 10 \n")
print("            -    EN  "+str(count_vulnibm_iot_lowintimpact_risklevel9)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN  "+str(count_vulnibm_iot_lowintimpact_risklevel8)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN  "+str(count_vulnibm_iot_lowintimpact_risklevel7)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN  "+str(count_vulnibm_iot_lowintimpact_risklevel6)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN "+str(count_vulnibm_iot_lowintimpact_risklevel5)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN "+str(count_vulnibm_iot_lowintimpact_risklevel4)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN "+str(count_vulnibm_iot_lowintimpact_risklevel3)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN "+str(count_vulnibm_iot_lowintimpact_risklevel2)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN "+str(count_vulnibm_iot_lowintimpact_risklevel1)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN "+str(count_vulnibm_iot_lowintimpact_risklevel0)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 0 \n")
print("\n")


print("*******************************PORCENTAJE RELACION DE IMPACTO DE INTEGRIDAD/PUNTUACION BASE PARA OBJETOS DE TIPO VULNERABILIDAD IBM PARTE IOT*******************************")
print("\n")                            
print("\n")
print(" DE UN TOTAL DE "+str(count_vulnibm_iot_integrity_impact)+" VULNERABILIDADES CON VALOR DE INTEGRIDAD ESPECIFICADO:\n") 
print("\n")
print("   - LOS PORCENTAJES DE VALORES DE IMPACTO DE INTEGRIDAD SON LOS SIGUIENTES:  \n")
print("      -    EN EL  "+str(float(((count_vulnibm_iot_highintimpact*100)/count_vulnibm_iot_integrity_impact)))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO, LOS PORCENTAJES DE NIVEL DE RIESGO SON LOS SIGUIENTES :  \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_highintimpact_risklevel10*100)/count_vulnibm_iot_highintimpact)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES 10 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_highintimpact_risklevel9*100)/count_vulnibm_iot_highintimpact)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_highintimpact_risklevel8*100)/count_vulnibm_iot_highintimpact)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_highintimpact_risklevel7*100)/count_vulnibm_iot_highintimpact)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_highintimpact_risklevel6*100)/count_vulnibm_iot_highintimpact)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_highintimpact_risklevel5*100)/count_vulnibm_iot_highintimpact)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_highintimpact_risklevel4*100)/count_vulnibm_iot_highintimpact)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_highintimpact_risklevel3*100)/count_vulnibm_iot_highintimpact)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_highintimpact_risklevel2*100)/count_vulnibm_iot_highintimpact)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_highintimpact_risklevel1*100)/count_vulnibm_iot_highintimpact)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_highintimpact_risklevel0*100)/count_vulnibm_iot_highintimpact)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 0 \n")
print("            -    EL VALOR MEDIO DE PUNTUACION BASE ES  "+str(float(((count_vulnibm_iot_highintimpact_risklevel)/count_vulnibm_iot_highintimpact)))+"\n")
print("\n")
print("      -    EN EL  "+str(float(((count_vulnibm_iot_lowintimpact*100)/count_vulnibm_iot_integrity_impact)))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO, LOS PORCENTAJES DE NIVEL DE RIESGO SON LOS SIGUIENTES :  \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_lowintimpact_risklevel10*100)/count_vulnibm_iot_lowintimpact)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES 10 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_lowintimpact_risklevel9*100)/count_vulnibm_iot_lowintimpact)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_lowintimpact_risklevel8*100)/count_vulnibm_iot_lowintimpact)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_lowintimpact_risklevel7*100)/count_vulnibm_iot_lowintimpact)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_lowintimpact_risklevel6*100)/count_vulnibm_iot_lowintimpact)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_lowintimpact_risklevel5*100)/count_vulnibm_iot_lowintimpact)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_lowintimpact_risklevel4*100)/count_vulnibm_iot_lowintimpact)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_lowintimpact_risklevel3*100)/count_vulnibm_iot_lowintimpact)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_lowintimpact_risklevel2*100)/count_vulnibm_iot_lowintimpact)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_lowintimpact_risklevel1*100)/count_vulnibm_iot_lowintimpact)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_lowintimpact_risklevel0*100)/count_vulnibm_iot_lowintimpact)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 0 \n")
print("            -    EL VALOR MEDIO DE PUNTUACION BASE ES  "+str(float(((count_vulnibm_iot_lowintimpact_risklevel)/count_vulnibm_iot_lowintimpact)))+"\n")
print("\n")



#Abro los ficheros con los que voy a tratar




df_vulnibm_sh = pd.read_excel('vulnerabilidades_ibm_smart_home_2023.xlsx')

#Variables para almacenar el contador total de valores de INTEGRIDAD
count_vulnibm_sh_integrity_impact=0
#Variables para almacenar el contador de un valor concreto de impacto de INTEGRIDAD
count_vulnibm_sh_highintimpact=0
#Variable para almacenar la suma de valores de nivel de riesgo para calcular despues la media para un valor de INTEGRIDAD dado
count_vulnibm_sh_highintimpact_risklevel=0
#Contador de valores de nivel de riesgo dado un nivel de impacto de INTEGRIDAD concreto
count_vulnibm_sh_highintimpact_risklevel10=0
count_vulnibm_sh_highintimpact_risklevel9=0
count_vulnibm_sh_highintimpact_risklevel8=0
count_vulnibm_sh_highintimpact_risklevel7=0
count_vulnibm_sh_highintimpact_risklevel6=0
count_vulnibm_sh_highintimpact_risklevel5=0
count_vulnibm_sh_highintimpact_risklevel4=0
count_vulnibm_sh_highintimpact_risklevel3=0
count_vulnibm_sh_highintimpact_risklevel2=0
count_vulnibm_sh_highintimpact_risklevel1=0
count_vulnibm_sh_highintimpact_risklevel0=0



count_vulnibm_sh_lowintimpact=0
count_vulnibm_sh_lowintimpact_risklevel=0
count_vulnibm_sh_lowintimpact_risklevel10=0
count_vulnibm_sh_lowintimpact_risklevel9=0
count_vulnibm_sh_lowintimpact_risklevel8=0
count_vulnibm_sh_lowintimpact_risklevel7=0
count_vulnibm_sh_lowintimpact_risklevel6=0
count_vulnibm_sh_lowintimpact_risklevel5=0
count_vulnibm_sh_lowintimpact_risklevel4=0
count_vulnibm_sh_lowintimpact_risklevel3=0
count_vulnibm_sh_lowintimpact_risklevel2=0
count_vulnibm_sh_lowintimpact_risklevel1=0
count_vulnibm_sh_lowintimpact_risklevel0=0



#Comprobamos el valor de impacto de INTEGRIDAD
for r in range(0,len(df_vulnibm_sh["x_xfe_cvss_integrity_impact"])):  
    if(isinstance(df_vulnibm_sh["x_xfe_cvss_integrity_impact"][r],str)):
        aux_str=df_vulnibm_sh["x_xfe_cvss_integrity_impact"][r].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
        if(aux_str!='NONE' or aux_str!='None'):
            count_vulnibm_sh_integrity_impact+=1
            #Comprobamos el valor de impacto de INTEGRIDAD
            if('High' in aux_str):
                count_vulnibm_sh_highintimpact+=1
                #Sumamos el valor de nivel de riesgo para posteriormente calcular la media
                count_vulnibm_sh_highintimpact_risklevel+=float(df_vulnibm_sh["x_xfe_risk_level"][r])
                #Comprobamos el valor de nivel de riesgo
                if(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 10.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=9.0)):
                    count_vulnibm_sh_highintimpact_risklevel9+=1
                elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 9.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=8.0)):
                    count_vulnibm_sh_highintimpact_risklevel8+=1
                elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 8.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=7.0)):
                    count_vulnibm_sh_highintimpact_risklevel7+=1
                elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 7.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=6.0)):
                    count_vulnibm_sh_highintimpact_risklevel6+=1
                elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 6.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=5.0)):
                    count_vulnibm_sh_highintimpact_risklevel5+=1
                elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 5.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=4.0)):
                    count_vulnibm_sh_highintimpact_risklevel4+=1
                elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 4.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=3.0)):
                    count_vulnibm_sh_highintimpact_risklevel3+=1
                elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 3.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=2.0)):
                    count_vulnibm_sh_highintimpact_risklevel2+=1
                elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 2.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=1.0)):
                    count_vulnibm_sh_highintimpact_risklevel1+=1
                elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 1.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=0.0)):
                    count_vulnibm_sh_highintimpact_risklevel0+=1
                elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) == 10.0)):
                    count_vulnibm_sh_highintimpact_risklevel10+=1

            elif('Low' in aux_str):

                count_vulnibm_sh_lowintimpact+=1
                count_vulnibm_sh_lowintimpact_risklevel+=float(df_vulnibm_sh["x_xfe_risk_level"][r])
                if(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 10.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=9.0)):
                    count_vulnibm_sh_lowintimpact_risklevel9+=1
                elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 9.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=8.0)):
                    count_vulnibm_sh_lowintimpact_risklevel8+=1
                elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 8.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=7.0)):
                    count_vulnibm_sh_lowintimpact_risklevel7+=1
                elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 7.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=6.0)):
                    count_vulnibm_sh_lowintimpact_risklevel6+=1
                elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 6.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=5.0)):
                    count_vulnibm_sh_lowintimpact_risklevel5+=1
                elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 5.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=4.0)):
                    count_vulnibm_sh_lowintimpact_risklevel4+=1
                elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 4.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=3.0)):
                    count_vulnibm_sh_lowintimpact_risklevel3+=1
                elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 3.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=2.0)):
                    count_vulnibm_sh_lowintimpact_risklevel2+=1
                elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 2.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=1.0)):
                    count_vulnibm_sh_lowintimpact_risklevel1+=1
                elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 1.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=0.0)):
                    count_vulnibm_sh_lowintimpact_risklevel0+=1
                elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) == 10.0)):
                    count_vulnibm_sh_lowintimpact_risklevel10+=1


            
                
print("*******************************ESTADÍSTICAS RELACION DE IMPACTO DE INTEGRIDAD/PUNTUACION BASE PARA OBJETOS DE TIPO VULNERABILIDAD IBM PARTE SMART HOME*******************************")
print("\n")                            
print("\n")
print(" DE UN TOTAL DE "+str(count_vulnibm_sh_integrity_impact)+" VULNERABILIDADES CON VALOR DE INTEGRIDAD ESPECIFICADO:\n") 
print("\n")
print("   - LAS ESTADISTICAS DE VALORES DE IMPACTO DE INTEGRIDAD SON LAS SIGUIENTES:  \n")
print("      -    EN  "+str(count_vulnibm_sh_highintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO, LAS ESTADÍSTICAS DE NIVEL DE RIESGO SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_sh_highintimpact_risklevel10)+" VULNERABILIDADES EL NIVEL DE RIESGO ES 10 \n")
print("            -    EN  "+str(count_vulnibm_sh_highintimpact_risklevel9)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN  "+str(count_vulnibm_sh_highintimpact_risklevel8)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN  "+str(count_vulnibm_sh_highintimpact_risklevel7)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN  "+str(count_vulnibm_sh_highintimpact_risklevel6)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN "+str(count_vulnibm_sh_highintimpact_risklevel5)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN "+str(count_vulnibm_sh_highintimpact_risklevel4)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN "+str(count_vulnibm_sh_highintimpact_risklevel3)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN "+str(count_vulnibm_sh_highintimpact_risklevel2)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN "+str(count_vulnibm_sh_highintimpact_risklevel1)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN "+str(count_vulnibm_sh_highintimpact_risklevel0)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 0 \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_sh_lowintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO, LAS ESTADÍSTICAS DE NIVEL DE RIESGO SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_sh_lowintimpact_risklevel10)+" VULNERABILIDADES EL NIVEL DE RIESGO ES 10 \n")
print("            -    EN  "+str(count_vulnibm_sh_lowintimpact_risklevel9)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN  "+str(count_vulnibm_sh_lowintimpact_risklevel8)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN  "+str(count_vulnibm_sh_lowintimpact_risklevel7)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN  "+str(count_vulnibm_sh_lowintimpact_risklevel6)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN "+str(count_vulnibm_sh_lowintimpact_risklevel5)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN "+str(count_vulnibm_sh_lowintimpact_risklevel4)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN "+str(count_vulnibm_sh_lowintimpact_risklevel3)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN "+str(count_vulnibm_sh_lowintimpact_risklevel2)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN "+str(count_vulnibm_sh_lowintimpact_risklevel1)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN "+str(count_vulnibm_sh_lowintimpact_risklevel0)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 0 \n")
print("\n")




print("*******************************PORCENTAJE RELACION DE IMPACTO DE INTEGRIDAD/PUNTUACION BASE PARA OBJETOS DE TIPO VULNERABILIDAD IBM PARTE SMART HOME*******************************")
print("\n")                            
print("\n")
print(" DE UN TOTAL DE "+str(count_vulnibm_sh_integrity_impact)+" VULNERABILIDADES CON VALOR DE INTEGRIDAD ESPECIFICADO:\n") 
print("\n")
print("   - LOS PORCENTAJES DE VALORES DE IMPACTO DE INTEGRIDAD SON LOS SIGUIENTES:  \n")
print("      -    EN EL  "+str(float(((count_vulnibm_sh_highintimpact*100)/count_vulnibm_sh_integrity_impact)))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO, LOS PORCENTAJES DE NIVEL DE RIESGO SON LOS SIGUIENTES :  \n")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_highintimpact_risklevel10*100)/count_vulnibm_sh_highintimpact)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES 10 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_highintimpact_risklevel9*100)/count_vulnibm_sh_highintimpact)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_highintimpact_risklevel8*100)/count_vulnibm_sh_highintimpact)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_highintimpact_risklevel7*100)/count_vulnibm_sh_highintimpact)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_highintimpact_risklevel6*100)/count_vulnibm_sh_highintimpact)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN EL "+str(float(((count_vulnibm_sh_highintimpact_risklevel5*100)/count_vulnibm_sh_highintimpact)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN EL "+str(float(((count_vulnibm_sh_highintimpact_risklevel4*100)/count_vulnibm_sh_highintimpact)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN EL "+str(float(((count_vulnibm_sh_highintimpact_risklevel3*100)/count_vulnibm_sh_highintimpact)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN EL "+str(float(((count_vulnibm_sh_highintimpact_risklevel2*100)/count_vulnibm_sh_highintimpact)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN EL "+str(float(((count_vulnibm_sh_highintimpact_risklevel1*100)/count_vulnibm_sh_highintimpact)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN EL "+str(float(((count_vulnibm_sh_highintimpact_risklevel0*100)/count_vulnibm_sh_highintimpact)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 0 \n")
print("            -    EL VALOR MEDIO DE PUNTUACION BASE ES  "+str(float(((count_vulnibm_sh_highintimpact_risklevel)/count_vulnibm_sh_highintimpact)))+"\n")
print("\n")
print("      -    EN EL  "+str(float(((count_vulnibm_sh_lowintimpact*100)/count_vulnibm_sh_integrity_impact)))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO, LOS PORCENTAJES DE NIVEL DE RIESGO SON LOS SIGUIENTES :  \n")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_lowintimpact_risklevel10*100)/count_vulnibm_sh_lowintimpact)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES 10 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_lowintimpact_risklevel9*100)/count_vulnibm_sh_lowintimpact)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_lowintimpact_risklevel8*100)/count_vulnibm_sh_lowintimpact)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_lowintimpact_risklevel7*100)/count_vulnibm_sh_lowintimpact)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_lowintimpact_risklevel6*100)/count_vulnibm_sh_lowintimpact)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN EL "+str(float(((count_vulnibm_sh_lowintimpact_risklevel5*100)/count_vulnibm_sh_lowintimpact)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN EL "+str(float(((count_vulnibm_sh_lowintimpact_risklevel4*100)/count_vulnibm_sh_lowintimpact)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN EL "+str(float(((count_vulnibm_sh_lowintimpact_risklevel3*100)/count_vulnibm_sh_lowintimpact)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN EL "+str(float(((count_vulnibm_sh_lowintimpact_risklevel2*100)/count_vulnibm_sh_lowintimpact)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN EL "+str(float(((count_vulnibm_sh_lowintimpact_risklevel1*100)/count_vulnibm_sh_lowintimpact)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN EL "+str(float(((count_vulnibm_sh_lowintimpact_risklevel0*100)/count_vulnibm_sh_lowintimpact)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 0 \n")
print("            -    EL VALOR MEDIO DE PUNTUACION BASE ES  "+str(float(((count_vulnibm_sh_lowintimpact_risklevel)/count_vulnibm_sh_lowintimpact)))+"\n")
print("\n")





print("*******************************ESTADÍSTICAS RELACION DE IMPACTO DE INTEGRIDAD/PUNTUACION BASE PARA OBJETOS DE TIPO VULNERABILIDAD IBM PARTE IOT Y SMART HOME CONJUNTAS*******************************")
print("\n")                            
print("\n")
print(" DE UN TOTAL DE "+str(count_vulnibm_iot_integrity_impact+count_vulnibm_sh_integrity_impact)+" VULNERABILIDADES CON VALOR DE INTEGRIDAD ESPECIFICADO:\n") 
print("\n")
print("   - LAS ESTADISTICAS DE VALORES DE IMPACTO DE INTEGRIDAD SON LAS SIGUIENTES:  \n")
print("      -    EN  "+str(count_vulnibm_iot_highintimpact+count_vulnibm_sh_highintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO, LAS ESTADÍSTICAS DE NIVEL DE RIESGO SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_highintimpact_risklevel10+count_vulnibm_sh_highintimpact_risklevel10)+" VULNERABILIDADES EL NIVEL DE RIESGO ES 10 \n")
print("            -    EN  "+str(count_vulnibm_iot_highintimpact_risklevel9+count_vulnibm_sh_highintimpact_risklevel9)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN  "+str(count_vulnibm_iot_highintimpact_risklevel8+count_vulnibm_sh_highintimpact_risklevel8)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN  "+str(count_vulnibm_iot_highintimpact_risklevel7+count_vulnibm_sh_highintimpact_risklevel7)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN  "+str(count_vulnibm_iot_highintimpact_risklevel6+count_vulnibm_sh_highintimpact_risklevel6)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN "+str(count_vulnibm_iot_highintimpact_risklevel5+count_vulnibm_sh_highintimpact_risklevel5)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN "+str(count_vulnibm_iot_highintimpact_risklevel4+count_vulnibm_sh_highintimpact_risklevel4)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN "+str(count_vulnibm_iot_highintimpact_risklevel3+count_vulnibm_sh_highintimpact_risklevel3)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN "+str(count_vulnibm_iot_highintimpact_risklevel2+count_vulnibm_sh_highintimpact_risklevel2)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN "+str(count_vulnibm_iot_highintimpact_risklevel1+count_vulnibm_sh_highintimpact_risklevel1)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN "+str(count_vulnibm_iot_highintimpact_risklevel0+count_vulnibm_sh_highintimpact_risklevel0)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 0 \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_lowintimpact+count_vulnibm_sh_lowintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO, LAS ESTADÍSTICAS DE NIVEL DE RIESGO SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_lowintimpact_risklevel10+count_vulnibm_sh_lowintimpact_risklevel10)+" VULNERABILIDADES EL NIVEL DE RIESGO ES 10 \n")
print("            -    EN  "+str(count_vulnibm_iot_lowintimpact_risklevel9+count_vulnibm_sh_lowintimpact_risklevel9)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN  "+str(count_vulnibm_iot_lowintimpact_risklevel8+count_vulnibm_sh_lowintimpact_risklevel8)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN  "+str(count_vulnibm_iot_lowintimpact_risklevel7+count_vulnibm_sh_lowintimpact_risklevel7)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN  "+str(count_vulnibm_iot_lowintimpact_risklevel6+count_vulnibm_sh_lowintimpact_risklevel6)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN "+str(count_vulnibm_iot_lowintimpact_risklevel5+count_vulnibm_sh_lowintimpact_risklevel5)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN "+str(count_vulnibm_iot_lowintimpact_risklevel4+count_vulnibm_sh_lowintimpact_risklevel4)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN "+str(count_vulnibm_iot_lowintimpact_risklevel3+count_vulnibm_sh_lowintimpact_risklevel3)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN "+str(count_vulnibm_iot_lowintimpact_risklevel2+count_vulnibm_sh_lowintimpact_risklevel2)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN "+str(count_vulnibm_iot_lowintimpact_risklevel1+count_vulnibm_sh_lowintimpact_risklevel1)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN "+str(count_vulnibm_iot_lowintimpact_risklevel0+count_vulnibm_sh_lowintimpact_risklevel0)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 0 \n")
print("\n")


print("*******************************PORCENTAJES RELACION DE IMPACTO DE INTEGRIDAD/PUNTUACION BASE PARA OBJETOS DE TIPO VULNERABILIDAD IBM PARTE IOT Y SMART HOME CONJUNTAS*******************************")
print("\n")                            
print("\n")
print(" DE UN TOTAL DE "+str(count_vulnibm_iot_integrity_impact+count_vulnibm_sh_integrity_impact)+" VULNERABILIDADES CON VALOR DE INTEGRIDAD ESPECIFICADO:\n") 
print("\n")
print("   - LOS PORCENTAJES DE VALORES DE IMPACTO DE INTEGRIDAD SON LOS SIGUIENTES:  \n")
print("      -    EN EL "+str(float((((count_vulnibm_iot_highintimpact+count_vulnibm_sh_highintimpact)*100)/(count_vulnibm_iot_integrity_impact+count_vulnibm_sh_integrity_impact))))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO, LOS PORCENTAJES DE NIVEL DE RIESGO SON LOS SIGUIENTES :  \n")
print("            -    EN EL"+str(float((((count_vulnibm_iot_highintimpact_risklevel10+count_vulnibm_sh_highintimpact_risklevel10)*100)/(count_vulnibm_iot_highintimpact+count_vulnibm_sh_highintimpact))))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES 10 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_highintimpact_risklevel9+count_vulnibm_sh_highintimpact_risklevel9)*100)/(count_vulnibm_iot_highintimpact+count_vulnibm_sh_highintimpact))))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_highintimpact_risklevel8+count_vulnibm_sh_highintimpact_risklevel8)*100)/(count_vulnibm_iot_highintimpact+count_vulnibm_sh_highintimpact))))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_highintimpact_risklevel7+count_vulnibm_sh_highintimpact_risklevel7)*100)/(count_vulnibm_iot_highintimpact+count_vulnibm_sh_highintimpact))))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_highintimpact_risklevel6+count_vulnibm_sh_highintimpact_risklevel6)*100)/(count_vulnibm_iot_highintimpact+count_vulnibm_sh_highintimpact))))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_highintimpact_risklevel5+count_vulnibm_sh_highintimpact_risklevel5)*100)/(count_vulnibm_iot_highintimpact+count_vulnibm_sh_highintimpact))))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_highintimpact_risklevel4+count_vulnibm_sh_highintimpact_risklevel4)*100)/(count_vulnibm_iot_highintimpact+count_vulnibm_sh_highintimpact))))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_highintimpact_risklevel3+count_vulnibm_sh_highintimpact_risklevel3)*100)/(count_vulnibm_iot_highintimpact+count_vulnibm_sh_highintimpact))))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_highintimpact_risklevel2+count_vulnibm_sh_highintimpact_risklevel2)*100)/(count_vulnibm_iot_highintimpact+count_vulnibm_sh_highintimpact))))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_highintimpact_risklevel1+count_vulnibm_sh_highintimpact_risklevel1)*100)/(count_vulnibm_iot_highintimpact+count_vulnibm_sh_highintimpact))))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_highintimpact_risklevel0+count_vulnibm_sh_highintimpact_risklevel0)*100)/(count_vulnibm_iot_highintimpact+count_vulnibm_sh_highintimpact))))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 0 \n")
print("            -    EL VALOR MEDIO DE PUNTUACION BASE ES  "+str(float(((count_vulnibm_iot_highintimpact_risklevel+count_vulnibm_sh_highintimpact_risklevel)/(count_vulnibm_iot_highintimpact+count_vulnibm_sh_highintimpact))))+"\n")
print("\n")
print("      -    EN EL "+str(float((((count_vulnibm_iot_lowintimpact+count_vulnibm_sh_lowintimpact)*100)/(count_vulnibm_iot_integrity_impact+count_vulnibm_sh_integrity_impact))))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO, LOS PORCENTAJES DE NIVEL DE RIESGO SON LOS SIGUIENTES :  \n")
print("            -    EN EL"+str(float((((count_vulnibm_iot_lowintimpact_risklevel10+count_vulnibm_sh_lowintimpact_risklevel10)*100)/(count_vulnibm_iot_lowintimpact+count_vulnibm_sh_lowintimpact))))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES 10 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_lowintimpact_risklevel9+count_vulnibm_sh_lowintimpact_risklevel9)*100)/(count_vulnibm_iot_lowintimpact+count_vulnibm_sh_lowintimpact))))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_lowintimpact_risklevel8+count_vulnibm_sh_lowintimpact_risklevel8)*100)/(count_vulnibm_iot_lowintimpact+count_vulnibm_sh_lowintimpact))))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_lowintimpact_risklevel7+count_vulnibm_sh_lowintimpact_risklevel7)*100)/(count_vulnibm_iot_lowintimpact+count_vulnibm_sh_lowintimpact))))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_lowintimpact_risklevel6+count_vulnibm_sh_lowintimpact_risklevel6)*100)/(count_vulnibm_iot_lowintimpact+count_vulnibm_sh_lowintimpact))))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_lowintimpact_risklevel5+count_vulnibm_sh_lowintimpact_risklevel5)*100)/(count_vulnibm_iot_lowintimpact+count_vulnibm_sh_lowintimpact))))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_lowintimpact_risklevel4+count_vulnibm_sh_lowintimpact_risklevel4)*100)/(count_vulnibm_iot_lowintimpact+count_vulnibm_sh_lowintimpact))))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_lowintimpact_risklevel3+count_vulnibm_sh_lowintimpact_risklevel3)*100)/(count_vulnibm_iot_lowintimpact+count_vulnibm_sh_lowintimpact))))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_lowintimpact_risklevel2+count_vulnibm_sh_lowintimpact_risklevel2)*100)/(count_vulnibm_iot_lowintimpact+count_vulnibm_sh_lowintimpact))))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_lowintimpact_risklevel1+count_vulnibm_sh_lowintimpact_risklevel1)*100)/(count_vulnibm_iot_lowintimpact+count_vulnibm_sh_lowintimpact))))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_lowintimpact_risklevel0+count_vulnibm_sh_lowintimpact_risklevel0)*100)/(count_vulnibm_iot_lowintimpact+count_vulnibm_sh_lowintimpact))))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 0 \n")
print("            -    EL VALOR MEDIO DE PUNTUACION BASE ES  "+str(float(((count_vulnibm_iot_lowintimpact_risklevel+count_vulnibm_sh_lowintimpact_risklevel)/(count_vulnibm_iot_lowintimpact+count_vulnibm_sh_lowintimpact))))+"\n")
print("\n")




