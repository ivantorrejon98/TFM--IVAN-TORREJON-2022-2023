

import pandas as pd
from datetime import datetime,timedelta



#Abro los ficheros con los que voy a tratar




df_vulnibm_iot = pd.read_excel('vulnerabilidades_ibm_iot_2023.xlsx')
#Contador de valores total de privilegios requeridos
count_vulnibm_iot_privileges_required=0
#Contador de valores de un nivel especifico de privilegios requeridos
count_vulnibm_iot_highprivreq=0
#Variable para almacenar la suma de niveles de PUNTUACION BASE para calcular la media despues
count_vulnibm_iot_highprivreq_risklevel=0
#Variables para almacenar LA PUNTUACION BASE segun un nivel de privilegios requeridos especifico
count_vulnibm_iot_highprivreq_risklevel10=0
count_vulnibm_iot_highprivreq_risklevel9=0
count_vulnibm_iot_highprivreq_risklevel8=0
count_vulnibm_iot_highprivreq_risklevel7=0
count_vulnibm_iot_highprivreq_risklevel6=0
count_vulnibm_iot_highprivreq_risklevel5=0
count_vulnibm_iot_highprivreq_risklevel4=0
count_vulnibm_iot_highprivreq_risklevel3=0
count_vulnibm_iot_highprivreq_risklevel2=0
count_vulnibm_iot_highprivreq_risklevel1=0
count_vulnibm_iot_highprivreq_risklevel0=0



count_vulnibm_iot_lowprivreq=0
count_vulnibm_iot_lowprivreq_risklevel=0
count_vulnibm_iot_lowprivreq_risklevel10=0
count_vulnibm_iot_lowprivreq_risklevel9=0
count_vulnibm_iot_lowprivreq_risklevel8=0
count_vulnibm_iot_lowprivreq_risklevel7=0
count_vulnibm_iot_lowprivreq_risklevel6=0
count_vulnibm_iot_lowprivreq_risklevel5=0
count_vulnibm_iot_lowprivreq_risklevel4=0
count_vulnibm_iot_lowprivreq_risklevel3=0
count_vulnibm_iot_lowprivreq_risklevel2=0
count_vulnibm_iot_lowprivreq_risklevel1=0
count_vulnibm_iot_lowprivreq_risklevel0=0



#Comprobamos el contenido de PRIVILEGIOS REQUERIDOS POR EL ATACANTE
for r in range(0,len(df_vulnibm_iot["x_xfe_cvss_privilegesrequired"])):  
    if(isinstance(df_vulnibm_iot["x_xfe_cvss_privilegesrequired"][r],float) == False ):
        aux_str=df_vulnibm_iot["x_xfe_cvss_privilegesrequired"][r].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
        if(aux_str!='NONE' or aux_str!='None'):
            count_vulnibm_iot_privileges_required+=1
            if('High' in aux_str):
                count_vulnibm_iot_highprivreq+=1
                #Aumento la suma de valores de PUNTUACION BASE
                count_vulnibm_iot_highprivreq_risklevel+=float(df_vulnibm_iot["x_xfe_risk_level"][r])
                if(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 10.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=9.0)):
                    count_vulnibm_iot_highprivreq_risklevel9+=1
                elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 9.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=8.0)):
                    count_vulnibm_iot_highprivreq_risklevel8+=1
                elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 8.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=7.0)):
                    count_vulnibm_iot_highprivreq_risklevel7+=1
                elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 7.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=6.0)):
                    count_vulnibm_iot_highprivreq_risklevel6+=1
                elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 6.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=5.0)):
                    count_vulnibm_iot_highprivreq_risklevel5+=1
                elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 5.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=4.0)):
                    count_vulnibm_iot_highprivreq_risklevel4+=1
                elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 4.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=3.0)):
                    count_vulnibm_iot_highprivreq_risklevel3+=1
                elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 3.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=2.0)):
                    count_vulnibm_iot_highprivreq_risklevel2+=1
                elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 2.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=1.0)):
                    count_vulnibm_iot_highprivreq_risklevel1+=1
                elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 1.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=0.0)):
                    count_vulnibm_iot_highprivreq_risklevel0+=1
                elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) == 10.0)):
                    count_vulnibm_iot_highprivreq_risklevel10+=1

            elif('Low' in aux_str):

                count_vulnibm_iot_lowprivreq+=1
                count_vulnibm_iot_lowprivreq_risklevel+=float(df_vulnibm_iot["x_xfe_risk_level"][r])
                if(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 10.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=9.0)):
                    count_vulnibm_iot_lowprivreq_risklevel9+=1
                elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 9.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=8.0)):
                    count_vulnibm_iot_lowprivreq_risklevel8+=1
                elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 8.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=7.0)):
                    count_vulnibm_iot_lowprivreq_risklevel7+=1
                elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 7.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=6.0)):
                    count_vulnibm_iot_lowprivreq_risklevel6+=1
                elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 6.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=5.0)):
                    count_vulnibm_iot_lowprivreq_risklevel5+=1
                elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 5.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=4.0)):
                    count_vulnibm_iot_lowprivreq_risklevel4+=1
                elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 4.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=3.0)):
                    count_vulnibm_iot_lowprivreq_risklevel3+=1
                elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 3.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=2.0)):
                    count_vulnibm_iot_lowprivreq_risklevel2+=1
                elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 2.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=1.0)):
                    count_vulnibm_iot_lowprivreq_risklevel1+=1
                elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 1.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=0.0)):
                    count_vulnibm_iot_lowprivreq_risklevel0+=1
                elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) == 10.0)):
                    count_vulnibm_iot_lowprivreq_risklevel10+=1

print("***************************ESTADÍSTICAS PRIVILEGIOS REQUERIDOS POR EL ATACANTE/PUNTUACION BASE VULNERABILIDADES IBM PARTE IOT***************************")
print("\n")                            
print("\n")
print(" DE UN TOTAL DE "+str(count_vulnibm_iot_privileges_required)+" VULNERABILIDADES:\n") 
print("\n")
print("   - LAS ESTADISTICAS DE VALORES DE PRIVILEGIOS REQUERIDOS SON LAS SIGUIENTES:  \n")
print("      -    EN  "+str(count_vulnibm_iot_highprivreq)+" VULNERABILIDADES SE REQUIERE UN NIVEL ALTO DE PRIVILEGIOS, LAS ESTADÍSTICAS DE PUNTUACION BASE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_highprivreq_risklevel10)+" VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
print("            -    EN  "+str(count_vulnibm_iot_highprivreq_risklevel9)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN  "+str(count_vulnibm_iot_highprivreq_risklevel8)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN  "+str(count_vulnibm_iot_highprivreq_risklevel7)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN  "+str(count_vulnibm_iot_highprivreq_risklevel6)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN "+str(count_vulnibm_iot_highprivreq_risklevel5)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN "+str(count_vulnibm_iot_highprivreq_risklevel4)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN "+str(count_vulnibm_iot_highprivreq_risklevel3)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN "+str(count_vulnibm_iot_highprivreq_risklevel2)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN "+str(count_vulnibm_iot_highprivreq_risklevel1)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN "+str(count_vulnibm_iot_highprivreq_risklevel0)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_lowprivreq)+" VULNERABILIDADES SE REQUIERE UN NIVEL BAJO DE PRIVILEGIOS, LAS ESTADÍSTICAS DE PUNTUACION BASE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_lowprivreq_risklevel10)+" VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
print("            -    EN  "+str(count_vulnibm_iot_lowprivreq_risklevel9)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN  "+str(count_vulnibm_iot_lowprivreq_risklevel8)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN  "+str(count_vulnibm_iot_lowprivreq_risklevel7)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN  "+str(count_vulnibm_iot_lowprivreq_risklevel6)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN "+str(count_vulnibm_iot_lowprivreq_risklevel5)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN "+str(count_vulnibm_iot_lowprivreq_risklevel4)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN "+str(count_vulnibm_iot_lowprivreq_risklevel3)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN "+str(count_vulnibm_iot_lowprivreq_risklevel2)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN "+str(count_vulnibm_iot_lowprivreq_risklevel1)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN "+str(count_vulnibm_iot_lowprivreq_risklevel0)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("\n")

print("***************************PORCENTAJE PRIVILEGIOS REQUERIDOS POR EL ATACANTE/PUNTUACION BASE VULNERABILIDADES IBM PARTE SMART HOME***************************")
print("\n")                            
print("\n")
print(" DE UN TOTAL DE "+str(count_vulnibm_iot_privileges_required)+" VULNERABILIDADES :\n") 
print("\n")
print("   - LOS PORCENTAJES DE VALORES DE PRIVILEGIOS REQUERIDOS SON LOS SIGUIENTES:  \n")
print("      -    EN EL  "+str(float(((count_vulnibm_iot_highprivreq*100)/count_vulnibm_iot_privileges_required)))+" % DE VULNERABILIDADES SE REQUIERE UN NIVEL ALTO DE PRIVILEGIOS, LOS PORCENTAJES DE PUNTUACION BASE SON LOS SIGUIENTES :  \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_highprivreq_risklevel10*100)/count_vulnibm_iot_highprivreq)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_highprivreq_risklevel9*100)/count_vulnibm_iot_highprivreq)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_highprivreq_risklevel8*100)/count_vulnibm_iot_highprivreq)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_highprivreq_risklevel7*100)/count_vulnibm_iot_highprivreq)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_highprivreq_risklevel6*100)/count_vulnibm_iot_highprivreq)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_highprivreq_risklevel5*100)/count_vulnibm_iot_highprivreq)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_highprivreq_risklevel4*100)/count_vulnibm_iot_highprivreq)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_highprivreq_risklevel3*100)/count_vulnibm_iot_highprivreq)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_highprivreq_risklevel2*100)/count_vulnibm_iot_highprivreq)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_highprivreq_risklevel1*100)/count_vulnibm_iot_highprivreq)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_highprivreq_risklevel0*100)/count_vulnibm_iot_highprivreq)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("            -    EL VALOR MEDIO DE PUNTUACION BASE ES  "+str(float(((count_vulnibm_iot_highprivreq_risklevel)/count_vulnibm_iot_highprivreq)))+"\n")
print("\n")
print("      -    EN EL  "+str(float(((count_vulnibm_iot_lowprivreq*100)/count_vulnibm_iot_privileges_required)))+" % DE VULNERABILIDADES SE REQUIERE UN NIVEL BAJO DE PRIVILEGIOS, LOS PORCENTAJES DE PUNTUACION BASE SON LOS SIGUIENTES :  \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_lowprivreq_risklevel10*100)/count_vulnibm_iot_lowprivreq)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_lowprivreq_risklevel9*100)/count_vulnibm_iot_lowprivreq)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_lowprivreq_risklevel8*100)/count_vulnibm_iot_lowprivreq)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_lowprivreq_risklevel7*100)/count_vulnibm_iot_lowprivreq)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_lowprivreq_risklevel6*100)/count_vulnibm_iot_lowprivreq)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_lowprivreq_risklevel5*100)/count_vulnibm_iot_lowprivreq)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_lowprivreq_risklevel4*100)/count_vulnibm_iot_lowprivreq)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_lowprivreq_risklevel3*100)/count_vulnibm_iot_lowprivreq)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_lowprivreq_risklevel2*100)/count_vulnibm_iot_lowprivreq)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_lowprivreq_risklevel1*100)/count_vulnibm_iot_lowprivreq)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_lowprivreq_risklevel0*100)/count_vulnibm_iot_lowprivreq)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("            -    EL VALOR MEDIO DE PUNTUACION BASE ES  "+str(float(((count_vulnibm_iot_lowprivreq_risklevel)/count_vulnibm_iot_lowprivreq)))+"\n")
print("\n")


#Abro los ficheros con los que voy a tratar




df_vulnibm_sh = pd.read_excel('vulnerabilidades_ibm_smart_home_2023.xlsx')
#Contador de valores total de privilegios requeridos
count_vulnibm_sh_privileges_required=0
#Contador de valores de un nivel especifico de privilegios requeridos
count_vulnibm_sh_highprivreq=0
#Variables para almacenar la suma de valores de PUNTUACION BASE
count_vulnibm_sh_highprivreq_risklevel=0
#Variables para almacenar LA PUNTUACION BASE segun un nivel de privilegios requeridos especifico
count_vulnibm_sh_highprivreq_risklevel10=0
count_vulnibm_sh_highprivreq_risklevel9=0
count_vulnibm_sh_highprivreq_risklevel8=0
count_vulnibm_sh_highprivreq_risklevel7=0
count_vulnibm_sh_highprivreq_risklevel6=0
count_vulnibm_sh_highprivreq_risklevel5=0
count_vulnibm_sh_highprivreq_risklevel4=0
count_vulnibm_sh_highprivreq_risklevel3=0
count_vulnibm_sh_highprivreq_risklevel2=0
count_vulnibm_sh_highprivreq_risklevel1=0
count_vulnibm_sh_highprivreq_risklevel0=0



count_vulnibm_sh_lowprivreq=0
count_vulnibm_sh_lowprivreq_risklevel=0
count_vulnibm_sh_lowprivreq_risklevel10=0
count_vulnibm_sh_lowprivreq_risklevel9=0
count_vulnibm_sh_lowprivreq_risklevel8=0
count_vulnibm_sh_lowprivreq_risklevel7=0
count_vulnibm_sh_lowprivreq_risklevel6=0
count_vulnibm_sh_lowprivreq_risklevel5=0
count_vulnibm_sh_lowprivreq_risklevel4=0
count_vulnibm_sh_lowprivreq_risklevel3=0
count_vulnibm_sh_lowprivreq_risklevel2=0
count_vulnibm_sh_lowprivreq_risklevel1=0
count_vulnibm_sh_lowprivreq_risklevel0=0




#Comprobamos el contenido de PRIVILEGIOS REQUERIDOS POR EL ATACANTE
for r in range(0,len(df_vulnibm_sh["x_xfe_cvss_privilegesrequired"])):
    if(isinstance(df_vulnibm_sh["x_xfe_cvss_privilegesrequired"][r],float) == False ):
        aux_str=df_vulnibm_sh["x_xfe_cvss_privilegesrequired"][r].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
        if(aux_str!='NONE' or aux_str!='None'):
            count_vulnibm_sh_privileges_required+=1
            if('High' in aux_str):
                count_vulnibm_sh_highprivreq+=1
                #Aumento la suma de valores de PUNTUACION BASE
                count_vulnibm_sh_highprivreq_risklevel+=float(df_vulnibm_sh["x_xfe_risk_level"][r])
                if(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 10.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=9.0)):
                    count_vulnibm_sh_highprivreq_risklevel9+=1
                elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 9.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=8.0)):
                    count_vulnibm_sh_highprivreq_risklevel8+=1
                elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 8.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=7.0)):
                    count_vulnibm_sh_highprivreq_risklevel7+=1
                elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 7.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=6.0)):
                    count_vulnibm_sh_highprivreq_risklevel6+=1
                elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 6.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=5.0)):
                    count_vulnibm_sh_highprivreq_risklevel5+=1
                elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 5.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=4.0)):
                    count_vulnibm_sh_highprivreq_risklevel4+=1
                elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 4.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=3.0)):
                    count_vulnibm_sh_highprivreq_risklevel3+=1
                elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 3.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=2.0)):
                    count_vulnibm_sh_highprivreq_risklevel2+=1
                elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 2.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=1.0)):
                    count_vulnibm_sh_highprivreq_risklevel1+=1
                elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 1.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=0.0)):
                    count_vulnibm_sh_highprivreq_risklevel0+=1
                elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) == 10.0)):
                    count_vulnibm_sh_highprivreq_risklevel10+=1

            elif('Low' in aux_str):

                count_vulnibm_sh_lowprivreq+=1
                count_vulnibm_sh_lowprivreq_risklevel+=float(df_vulnibm_sh["x_xfe_risk_level"][r])
                if(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 10.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=9.0)):
                    count_vulnibm_sh_lowprivreq_risklevel9+=1
                elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 9.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=8.0)):
                    count_vulnibm_sh_lowprivreq_risklevel8+=1
                elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 8.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=7.0)):
                    count_vulnibm_sh_lowprivreq_risklevel7+=1
                elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 7.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=6.0)):
                    count_vulnibm_sh_lowprivreq_risklevel6+=1
                elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 6.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=5.0)):
                    count_vulnibm_sh_lowprivreq_risklevel5+=1
                elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 5.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=4.0)):
                    count_vulnibm_sh_lowprivreq_risklevel4+=1
                elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 4.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=3.0)):
                    count_vulnibm_sh_lowprivreq_risklevel3+=1
                elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 3.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=2.0)):
                    count_vulnibm_sh_lowprivreq_risklevel2+=1
                elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 2.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=1.0)):
                    count_vulnibm_sh_lowprivreq_risklevel1+=1
                elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 1.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=0.0)):
                    count_vulnibm_sh_lowprivreq_risklevel0+=1
                elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) == 10.0)):
                    count_vulnibm_sh_lowprivreq_risklevel10+=1

                
                
print("***************************ESTADÍSTICAS PRIVILEGIOS REQUERIDOS POR EL ATACANTE/PUNTUACION BASE VULNERABILIDADES IBM PARTE SMART HOME***************************")
print("\n")                            
print("\n")
print(" DE UN TOTAL DE "+str(count_vulnibm_sh_privileges_required)+" VULNERABILIDADES:\n") 
print("\n")
print("   - LAS ESTADISTICAS DE VALORES DE PRIVILEGIOS REQUERIDOS SON LAS SIGUIENTES:  \n")
print("      -    EN  "+str(count_vulnibm_sh_highprivreq)+" VULNERABILIDADES SE REQUIERE UN NIVEL ALTO DE PRIVILEGIOS, LAS ESTADÍSTICAS DE PUNTUACION BASE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_sh_highprivreq_risklevel10)+" VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
print("            -    EN  "+str(count_vulnibm_sh_highprivreq_risklevel9)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN  "+str(count_vulnibm_sh_highprivreq_risklevel8)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN  "+str(count_vulnibm_sh_highprivreq_risklevel7)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN  "+str(count_vulnibm_sh_highprivreq_risklevel6)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN "+str(count_vulnibm_sh_highprivreq_risklevel5)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN "+str(count_vulnibm_sh_highprivreq_risklevel4)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN "+str(count_vulnibm_sh_highprivreq_risklevel3)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN "+str(count_vulnibm_sh_highprivreq_risklevel2)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN "+str(count_vulnibm_sh_highprivreq_risklevel1)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN "+str(count_vulnibm_sh_highprivreq_risklevel0)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_sh_lowprivreq)+" VULNERABILIDADES SE REQUIERE UN NIVEL BAJO DE PRIVILEGIOS, LAS ESTADÍSTICAS DE PUNTUACION BASE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_sh_lowprivreq_risklevel10)+" VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
print("            -    EN  "+str(count_vulnibm_sh_lowprivreq_risklevel9)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN  "+str(count_vulnibm_sh_lowprivreq_risklevel8)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN  "+str(count_vulnibm_sh_lowprivreq_risklevel7)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN  "+str(count_vulnibm_sh_lowprivreq_risklevel6)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN "+str(count_vulnibm_sh_lowprivreq_risklevel5)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN "+str(count_vulnibm_sh_lowprivreq_risklevel4)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN "+str(count_vulnibm_sh_lowprivreq_risklevel3)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN "+str(count_vulnibm_sh_lowprivreq_risklevel2)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN "+str(count_vulnibm_sh_lowprivreq_risklevel1)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN "+str(count_vulnibm_sh_lowprivreq_risklevel0)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("\n")




print("***************************PORCENTAJE PRIVILEGIOS REQUERIDOS POR EL ATACANTE/PUNTUACION BASE VULNERABILIDADES IBM PARTE SMART HOME***************************")
print("\n")                            
print("\n")
print(" DE UN TOTAL DE "+str(count_vulnibm_sh_privileges_required)+" VULNERABILIDADES :\n") 
print("\n")
print("   - LOS PORCENTAJES DE VALORES DE PRIVILEGIOS REQUERIDOS SON LOS SIGUIENTES:  \n")
print("      -    EN EL  "+str(float(((count_vulnibm_sh_highprivreq*100)/count_vulnibm_sh_privileges_required)))+" % DE VULNERABILIDADES SE REQUIERE UN NIVEL ALTO DE PRIVILEGIOS, LOS PORCENTAJES DE PUNTUACION BASE SON LOS SIGUIENTES :  \n")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_highprivreq_risklevel10*100)/count_vulnibm_sh_highprivreq)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_highprivreq_risklevel9*100)/count_vulnibm_sh_highprivreq)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_highprivreq_risklevel8*100)/count_vulnibm_sh_highprivreq)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_highprivreq_risklevel7*100)/count_vulnibm_sh_highprivreq)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_highprivreq_risklevel6*100)/count_vulnibm_sh_highprivreq)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN EL "+str(float(((count_vulnibm_sh_highprivreq_risklevel5*100)/count_vulnibm_sh_highprivreq)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN EL "+str(float(((count_vulnibm_sh_highprivreq_risklevel4*100)/count_vulnibm_sh_highprivreq)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN EL "+str(float(((count_vulnibm_sh_highprivreq_risklevel3*100)/count_vulnibm_sh_highprivreq)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN EL "+str(float(((count_vulnibm_sh_highprivreq_risklevel2*100)/count_vulnibm_sh_highprivreq)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN EL "+str(float(((count_vulnibm_sh_highprivreq_risklevel1*100)/count_vulnibm_sh_highprivreq)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN EL "+str(float(((count_vulnibm_sh_highprivreq_risklevel0*100)/count_vulnibm_sh_highprivreq)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("            -    EL VALOR MEDIO DE PUNTUACION BASE ES  "+str(float(((count_vulnibm_sh_highprivreq_risklevel)/count_vulnibm_sh_highprivreq)))+"\n")
print("\n")
print("      -    EN EL  "+str(float(((count_vulnibm_sh_lowprivreq*100)/count_vulnibm_sh_privileges_required)))+" % DE VULNERABILIDADES SE REQUIERE UN NIVEL BAJO DE PRIVILEGIOS, LOS PORCENTAJES DE PUNTUACION BASE SON LOS SIGUIENTES :  \n")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_lowprivreq_risklevel10*100)/count_vulnibm_sh_lowprivreq)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_lowprivreq_risklevel9*100)/count_vulnibm_sh_lowprivreq)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_lowprivreq_risklevel8*100)/count_vulnibm_sh_lowprivreq)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_lowprivreq_risklevel7*100)/count_vulnibm_sh_lowprivreq)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_lowprivreq_risklevel6*100)/count_vulnibm_sh_lowprivreq)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN EL "+str(float(((count_vulnibm_sh_lowprivreq_risklevel5*100)/count_vulnibm_sh_lowprivreq)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN EL "+str(float(((count_vulnibm_sh_lowprivreq_risklevel4*100)/count_vulnibm_sh_lowprivreq)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN EL "+str(float(((count_vulnibm_sh_lowprivreq_risklevel3*100)/count_vulnibm_sh_lowprivreq)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN EL "+str(float(((count_vulnibm_sh_lowprivreq_risklevel2*100)/count_vulnibm_sh_lowprivreq)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN EL "+str(float(((count_vulnibm_sh_lowprivreq_risklevel1*100)/count_vulnibm_sh_lowprivreq)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN EL "+str(float(((count_vulnibm_sh_lowprivreq_risklevel0*100)/count_vulnibm_sh_lowprivreq)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("            -    EL VALOR MEDIO DE PUNTUACION BASE ES  "+str(float(((count_vulnibm_sh_lowprivreq_risklevel)/count_vulnibm_sh_lowprivreq)))+"\n")
print("\n")

print("***************************ESTADÍSTICAS PRIVILEGIOS REQUERIDOS POR EL ATACANTE/PUNTUACION BASE VULNERABILIDADES IBM PARTE IOT Y SMART HOME CONJUNTAS***************************")
print("\n")                            
print("\n")
print(" DE UN TOTAL DE "+str(count_vulnibm_iot_privileges_required+count_vulnibm_sh_privileges_required)+" VULNERABILIDADES:\n") 
print("\n")
print("   - LAS ESTADISTICAS DE VALORES DE PRIVILEGIOS REQUERIDOS SON LAS SIGUIENTES:  \n")
print("      -    EN  "+str(count_vulnibm_iot_highprivreq+count_vulnibm_sh_highprivreq)+" VULNERABILIDADES SE REQUIERE UN NIVEL ALTO DE PRIVILEGIOS, LAS ESTADÍSTICAS DE PUNTUACION BASE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_highprivreq_risklevel10+count_vulnibm_sh_highprivreq_risklevel10)+" VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
print("            -    EN  "+str(count_vulnibm_iot_highprivreq_risklevel9+count_vulnibm_sh_highprivreq_risklevel9)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN  "+str(count_vulnibm_iot_highprivreq_risklevel8+count_vulnibm_sh_highprivreq_risklevel8)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN  "+str(count_vulnibm_iot_highprivreq_risklevel7+count_vulnibm_sh_highprivreq_risklevel7)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN  "+str(count_vulnibm_iot_highprivreq_risklevel6+count_vulnibm_sh_highprivreq_risklevel6)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN "+str(count_vulnibm_iot_highprivreq_risklevel5+count_vulnibm_sh_highprivreq_risklevel5)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN "+str(count_vulnibm_iot_highprivreq_risklevel4+count_vulnibm_sh_highprivreq_risklevel4)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN "+str(count_vulnibm_iot_highprivreq_risklevel3+count_vulnibm_sh_highprivreq_risklevel3)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN "+str(count_vulnibm_iot_highprivreq_risklevel2+count_vulnibm_sh_highprivreq_risklevel2)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN "+str(count_vulnibm_iot_highprivreq_risklevel1+count_vulnibm_sh_highprivreq_risklevel1)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN "+str(count_vulnibm_iot_highprivreq_risklevel0+count_vulnibm_sh_highprivreq_risklevel0)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_lowprivreq+count_vulnibm_sh_lowprivreq)+" VULNERABILIDADES EL NIVEL DE PRIVILEGIOS REQUERIDOS ES BAJO, LAS ESTADÍSTICAS DE PUNTUACION BASE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_lowprivreq_risklevel10+count_vulnibm_sh_lowprivreq_risklevel10)+" VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
print("            -    EN  "+str(count_vulnibm_iot_lowprivreq_risklevel9+count_vulnibm_sh_lowprivreq_risklevel9)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN  "+str(count_vulnibm_iot_lowprivreq_risklevel8+count_vulnibm_sh_lowprivreq_risklevel8)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN  "+str(count_vulnibm_iot_lowprivreq_risklevel7+count_vulnibm_sh_lowprivreq_risklevel7)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN  "+str(count_vulnibm_iot_lowprivreq_risklevel6+count_vulnibm_sh_lowprivreq_risklevel6)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN "+str(count_vulnibm_iot_lowprivreq_risklevel5+count_vulnibm_sh_lowprivreq_risklevel5)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN "+str(count_vulnibm_iot_lowprivreq_risklevel4+count_vulnibm_sh_lowprivreq_risklevel4)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN "+str(count_vulnibm_iot_lowprivreq_risklevel3+count_vulnibm_sh_lowprivreq_risklevel3)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN "+str(count_vulnibm_iot_lowprivreq_risklevel2+count_vulnibm_sh_lowprivreq_risklevel2)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN "+str(count_vulnibm_iot_lowprivreq_risklevel1+count_vulnibm_sh_lowprivreq_risklevel1)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN "+str(count_vulnibm_iot_lowprivreq_risklevel0+count_vulnibm_sh_lowprivreq_risklevel0)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("\n")









print("***************************PORCENTAJES PRIVILEGIOS REQUERIDOS POR EL ATACANTE/PUNTUACION BASE VULNERABILIDADES IBM PARTE IOT Y SMART HOME CONJUNTAS***************************")
print("\n")                            
print("\n")
print(" DE UN TOTAL DE "+str(count_vulnibm_iot_privileges_required+count_vulnibm_sh_privileges_required)+" VULNERABILIDADES:\n")
print("\n")
print("   - LOS PORCENTAJES DE VALORES DE PRIVILEGIOS REQUERIDOS SON LOS SIGUIENTES:  \n")
print("      -    EN EL "+str(float((((count_vulnibm_iot_highprivreq+count_vulnibm_sh_highprivreq)*100)/(count_vulnibm_iot_privileges_required+count_vulnibm_sh_privileges_required))))+" % DE VULNERABILIDADES EL NIVEL DE PRIVILEGIOS REQUERIDOS ES ALTO, LOS PORCENTAJES DE PUNTUACION BASE SON LOS SIGUIENTES :  \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_highprivreq_risklevel10+count_vulnibm_sh_highprivreq_risklevel10)*100)/(count_vulnibm_iot_highprivreq+count_vulnibm_sh_highprivreq))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_highprivreq_risklevel9+count_vulnibm_sh_highprivreq_risklevel9)*100)/(count_vulnibm_iot_highprivreq+count_vulnibm_sh_highprivreq))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_highprivreq_risklevel8+count_vulnibm_sh_highprivreq_risklevel8)*100)/(count_vulnibm_iot_highprivreq+count_vulnibm_sh_highprivreq))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_highprivreq_risklevel7+count_vulnibm_sh_highprivreq_risklevel7)*100)/(count_vulnibm_iot_highprivreq+count_vulnibm_sh_highprivreq))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_highprivreq_risklevel6+count_vulnibm_sh_highprivreq_risklevel6)*100)/(count_vulnibm_iot_highprivreq+count_vulnibm_sh_highprivreq))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_highprivreq_risklevel5+count_vulnibm_sh_highprivreq_risklevel5)*100)/(count_vulnibm_iot_highprivreq+count_vulnibm_sh_highprivreq))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_highprivreq_risklevel4+count_vulnibm_sh_highprivreq_risklevel4)*100)/(count_vulnibm_iot_highprivreq+count_vulnibm_sh_highprivreq))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_highprivreq_risklevel3+count_vulnibm_sh_highprivreq_risklevel3)*100)/(count_vulnibm_iot_highprivreq+count_vulnibm_sh_highprivreq))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_highprivreq_risklevel2+count_vulnibm_sh_highprivreq_risklevel2)*100)/(count_vulnibm_iot_highprivreq+count_vulnibm_sh_highprivreq))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_highprivreq_risklevel1+count_vulnibm_sh_highprivreq_risklevel1)*100)/(count_vulnibm_iot_highprivreq+count_vulnibm_sh_highprivreq))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_highprivreq_risklevel0+count_vulnibm_sh_highprivreq_risklevel0)*100)/(count_vulnibm_iot_highprivreq+count_vulnibm_sh_highprivreq))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("            -    EL VALOR MEDIO DE PUNTUACION BASE ES  "+str(float(((count_vulnibm_iot_highprivreq_risklevel+count_vulnibm_sh_highprivreq_risklevel)/(count_vulnibm_iot_highprivreq+count_vulnibm_sh_highprivreq))))+"\n")
print("\n")
print("      -    EN EL "+str(float((((count_vulnibm_iot_lowprivreq+count_vulnibm_sh_lowprivreq)*100)/(count_vulnibm_iot_privileges_required+count_vulnibm_sh_privileges_required))))+" % DE VULNERABILIDADES EL NIVEL DE PRIVILEGIOS REQUERIDOS ES BAJO, LOS PORCENTAJES DE PUNTUACION BASE SON LOS SIGUIENTES :  \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_lowprivreq_risklevel10+count_vulnibm_sh_lowprivreq_risklevel10)*100)/(count_vulnibm_iot_lowprivreq+count_vulnibm_sh_lowprivreq))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_lowprivreq_risklevel9+count_vulnibm_sh_lowprivreq_risklevel9)*100)/(count_vulnibm_iot_lowprivreq+count_vulnibm_sh_lowprivreq))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_lowprivreq_risklevel8+count_vulnibm_sh_lowprivreq_risklevel8)*100)/(count_vulnibm_iot_lowprivreq+count_vulnibm_sh_lowprivreq))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_lowprivreq_risklevel7+count_vulnibm_sh_lowprivreq_risklevel7)*100)/(count_vulnibm_iot_lowprivreq+count_vulnibm_sh_lowprivreq))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_lowprivreq_risklevel6+count_vulnibm_sh_lowprivreq_risklevel6)*100)/(count_vulnibm_iot_lowprivreq+count_vulnibm_sh_lowprivreq))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_lowprivreq_risklevel5+count_vulnibm_sh_lowprivreq_risklevel5)*100)/(count_vulnibm_iot_lowprivreq+count_vulnibm_sh_lowprivreq))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_lowprivreq_risklevel4+count_vulnibm_sh_lowprivreq_risklevel4)*100)/(count_vulnibm_iot_lowprivreq+count_vulnibm_sh_lowprivreq))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_lowprivreq_risklevel3+count_vulnibm_sh_lowprivreq_risklevel3)*100)/(count_vulnibm_iot_lowprivreq+count_vulnibm_sh_lowprivreq))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_lowprivreq_risklevel2+count_vulnibm_sh_lowprivreq_risklevel2)*100)/(count_vulnibm_iot_lowprivreq+count_vulnibm_sh_lowprivreq))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_lowprivreq_risklevel1+count_vulnibm_sh_lowprivreq_risklevel1)*100)/(count_vulnibm_iot_lowprivreq+count_vulnibm_sh_lowprivreq))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_lowprivreq_risklevel0+count_vulnibm_sh_lowprivreq_risklevel0)*100)/(count_vulnibm_iot_lowprivreq+count_vulnibm_sh_lowprivreq))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("            -    EL VALOR MEDIO DE PUNTUACION BASE ES  "+str(float(((count_vulnibm_iot_lowprivreq_risklevel+count_vulnibm_sh_lowprivreq_risklevel)/(count_vulnibm_iot_lowprivreq+count_vulnibm_sh_lowprivreq))))+"\n")
print("\n")


