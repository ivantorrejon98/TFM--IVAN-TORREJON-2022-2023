import pandas as pd
from datetime import datetime,timedelta



#Abro los ficheros con los que voy a tratar




df_vulnibm_iot = pd.read_excel('vulnerabilidades_ibm_iot_2023.xlsx')

#Variable para almacenar el contador total de valores para complejidad de acceso
count_vulnibm_iot_access_complexity=0

#Variables para almacenar el contador de valores para una complejidad de acceso determinada
count_vulnibm_iot_highaccescomplex=0
#Variable para almacenar la suma de nivel de riesgo para un determinado valor de complejidad de acceso
count_vulnibm_iot_highaccescomplex_risklevel=0
#Variable para almacenar el contador de valores de nivel de riesgo para una complejidad de acceso determinada
count_vulnibm_iot_highaccescomplex_risklevel10=0
count_vulnibm_iot_highaccescomplex_risklevel9=0
count_vulnibm_iot_highaccescomplex_risklevel8=0
count_vulnibm_iot_highaccescomplex_risklevel7=0
count_vulnibm_iot_highaccescomplex_risklevel6=0
count_vulnibm_iot_highaccescomplex_risklevel5=0
count_vulnibm_iot_highaccescomplex_risklevel4=0
count_vulnibm_iot_highaccescomplex_risklevel3=0
count_vulnibm_iot_highaccescomplex_risklevel2=0
count_vulnibm_iot_highaccescomplex_risklevel1=0
count_vulnibm_iot_highaccescomplex_risklevel0=0



count_vulnibm_iot_lowaccescomplex=0
count_vulnibm_iot_lowaccescomplex_risklevel=0
count_vulnibm_iot_lowaccescomplex_risklevel10=0
count_vulnibm_iot_lowaccescomplex_risklevel9=0
count_vulnibm_iot_lowaccescomplex_risklevel8=0
count_vulnibm_iot_lowaccescomplex_risklevel7=0
count_vulnibm_iot_lowaccescomplex_risklevel6=0
count_vulnibm_iot_lowaccescomplex_risklevel5=0
count_vulnibm_iot_lowaccescomplex_risklevel4=0
count_vulnibm_iot_lowaccescomplex_risklevel3=0
count_vulnibm_iot_lowaccescomplex_risklevel2=0
count_vulnibm_iot_lowaccescomplex_risklevel1=0
count_vulnibm_iot_lowaccescomplex_risklevel0=0


count_vulnibm_iot_mediumaccescomplex=0
count_vulnibm_iot_mediumaccescomplex_risklevel=0
count_vulnibm_iot_mediumaccescomplex_risklevel10=0
count_vulnibm_iot_mediumaccescomplex_risklevel9=0
count_vulnibm_iot_mediumaccescomplex_risklevel8=0
count_vulnibm_iot_mediumaccescomplex_risklevel7=0
count_vulnibm_iot_mediumaccescomplex_risklevel6=0
count_vulnibm_iot_mediumaccescomplex_risklevel5=0
count_vulnibm_iot_mediumaccescomplex_risklevel4=0
count_vulnibm_iot_mediumaccescomplex_risklevel3=0
count_vulnibm_iot_mediumaccescomplex_risklevel2=0
count_vulnibm_iot_mediumaccescomplex_risklevel1=0
count_vulnibm_iot_mediumaccescomplex_risklevel0=0





















#Comprobamos el valor de COMPLEJIDAD DE ACCESO
for r in range(0,len(df_vulnibm_iot["x_xfe_cvss_access_complexity"])):   
    #Obtenemos el valor de complejidad de acceso
    aux_str=df_vulnibm_iot["x_xfe_cvss_access_complexity"][r].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
    if(aux_str!='NONE' or aux_str!='None'):
        count_vulnibm_iot_access_complexity+=1
        #Comprobamos el nivel de complejidad de acceso
        if('High' in aux_str):
            count_vulnibm_iot_highaccescomplex+=1
            #Aumentamos la suma de valores de nivel de riesgo
            count_vulnibm_iot_highaccescomplex_risklevel+=float(df_vulnibm_iot["x_xfe_risk_level"][r])
            #Comprobamos el valor de nivel de riesgo
            if(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 10.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=9.0)):
                count_vulnibm_iot_highaccescomplex_risklevel9+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 9.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=8.0)):
                count_vulnibm_iot_highaccescomplex_risklevel8+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 8.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=7.0)):
                count_vulnibm_iot_highaccescomplex_risklevel7+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 7.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=6.0)):
                count_vulnibm_iot_highaccescomplex_risklevel6+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 6.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=5.0)):
                count_vulnibm_iot_highaccescomplex_risklevel5+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 5.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=4.0)):
                count_vulnibm_iot_highaccescomplex_risklevel4+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 4.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=3.0)):
                count_vulnibm_iot_highaccescomplex_risklevel3+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 3.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=2.0)):
                count_vulnibm_iot_highaccescomplex_risklevel2+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 2.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=1.0)):
                count_vulnibm_iot_highaccescomplex_risklevel1+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 1.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=0.0)):
                count_vulnibm_iot_highaccescomplex_risklevel0+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) == 10.0)):
                count_vulnibm_iot_highaccescomplex_risklevel10+=1
            
        elif('Low' in aux_str):
            
            count_vulnibm_iot_lowaccescomplex+=1
            count_vulnibm_iot_lowaccescomplex_risklevel+=float(df_vulnibm_iot["x_xfe_risk_level"][r])
            if(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 10.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=9.0)):
                count_vulnibm_iot_lowaccescomplex_risklevel9+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 9.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=8.0)):
                count_vulnibm_iot_lowaccescomplex_risklevel8+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 8.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=7.0)):
                count_vulnibm_iot_lowaccescomplex_risklevel7+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 7.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=6.0)):
                count_vulnibm_iot_lowaccescomplex_risklevel6+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 6.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=5.0)):
                count_vulnibm_iot_lowaccescomplex_risklevel5+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 5.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=4.0)):
                count_vulnibm_iot_lowaccescomplex_risklevel4+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 4.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=3.0)):
                count_vulnibm_iot_lowaccescomplex_risklevel3+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 3.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=2.0)):
                count_vulnibm_iot_lowaccescomplex_risklevel2+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 2.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=1.0)):
                count_vulnibm_iot_lowaccescomplex_risklevel1+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 1.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=0.0)):
                count_vulnibm_iot_lowaccescomplex_risklevel0+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) == 10.0)):
                count_vulnibm_iot_lowaccescomplex_risklevel10+=1
            
            
        elif('Medium' in aux_str):
        
            count_vulnibm_iot_mediumaccescomplex+=1
            count_vulnibm_iot_mediumaccescomplex_risklevel+=float(df_vulnibm_iot["x_xfe_risk_level"][r])
            if(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 10.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=9.0)):
                count_vulnibm_iot_mediumaccescomplex_risklevel9+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 9.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=8.0)):
                count_vulnibm_iot_mediumaccescomplex_risklevel8+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 8.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=7.0)):
                count_vulnibm_iot_mediumaccescomplex_risklevel7+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 7.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=6.0)):
                count_vulnibm_iot_mediumaccescomplex_risklevel6+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 6.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=5.0)):
                count_vulnibm_iot_mediumaccescomplex_risklevel5+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 5.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=4.0)):
                count_vulnibm_iot_mediumaccescomplex_risklevel4+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 4.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=3.0)):
                count_vulnibm_iot_mediumaccescomplex_risklevel3+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 3.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=2.0)):
                count_vulnibm_iot_mediumaccescomplex_risklevel2+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 2.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=1.0)):
                count_vulnibm_iot_mediumaccescomplex_risklevel1+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 1.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=0.0)):
                count_vulnibm_iot_mediumaccescomplex_risklevel0+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) == 10.0)):
                count_vulnibm_iot_mediumaccescomplex_risklevel10+=1
            
        
                
                
                
                
print("*****************************ESTADÍSTICAS COMPLEJIDAD DE ACCESO/PUNTUACION BASE VULNERABILIDADES IBM PARTE IOT*****************************")
print("\n")                            
print("\n")
print(" DE UN TOTAL DE "+str(count_vulnibm_iot_access_complexity)+" VULNERABILIDADES:\n") 
print("\n")
print("   - LAS ESTADISTICAS DE VALORES DE COMPLEJIDAD DE ACCESO SON LAS SIGUIENTES:  \n")
print("      -    EN  "+str(count_vulnibm_iot_highaccescomplex)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES ALTA, LAS ESTADÍSTICAS DE NIVEL DE RIESGO SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_highaccescomplex_risklevel10)+" VULNERABILIDADES EL NIVEL DE RIESGO ES 10 \n")
print("            -    EN  "+str(count_vulnibm_iot_highaccescomplex_risklevel9)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN  "+str(count_vulnibm_iot_highaccescomplex_risklevel8)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN  "+str(count_vulnibm_iot_highaccescomplex_risklevel7)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN  "+str(count_vulnibm_iot_highaccescomplex_risklevel6)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN "+str(count_vulnibm_iot_highaccescomplex_risklevel5)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN "+str(count_vulnibm_iot_highaccescomplex_risklevel4)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN "+str(count_vulnibm_iot_highaccescomplex_risklevel3)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN "+str(count_vulnibm_iot_highaccescomplex_risklevel2)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN "+str(count_vulnibm_iot_highaccescomplex_risklevel1)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN "+str(count_vulnibm_iot_highaccescomplex_risklevel0)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 0 \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_lowaccescomplex)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES BAJA, LAS ESTADÍSTICAS DE NIVEL DE RIESGO SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_lowaccescomplex_risklevel10)+" VULNERABILIDADES EL NIVEL DE RIESGO ES 10 \n")
print("            -    EN  "+str(count_vulnibm_iot_lowaccescomplex_risklevel9)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN  "+str(count_vulnibm_iot_lowaccescomplex_risklevel8)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN  "+str(count_vulnibm_iot_lowaccescomplex_risklevel7)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN  "+str(count_vulnibm_iot_lowaccescomplex_risklevel6)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN "+str(count_vulnibm_iot_lowaccescomplex_risklevel5)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN "+str(count_vulnibm_iot_lowaccescomplex_risklevel4)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN "+str(count_vulnibm_iot_lowaccescomplex_risklevel3)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN "+str(count_vulnibm_iot_lowaccescomplex_risklevel2)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN "+str(count_vulnibm_iot_lowaccescomplex_risklevel1)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN "+str(count_vulnibm_iot_lowaccescomplex_risklevel0)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 0 \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_mediumaccescomplex)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES MEDIA, LAS ESTADÍSTICAS DE NIVEL DE RIESGO SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_mediumaccescomplex_risklevel10)+" VULNERABILIDADES EL NIVEL DE RIESGO ES 10 \n")
print("            -    EN  "+str(count_vulnibm_iot_mediumaccescomplex_risklevel9)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN  "+str(count_vulnibm_iot_mediumaccescomplex_risklevel8)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN  "+str(count_vulnibm_iot_mediumaccescomplex_risklevel7)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN  "+str(count_vulnibm_iot_mediumaccescomplex_risklevel6)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN "+str(count_vulnibm_iot_mediumaccescomplex_risklevel5)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN "+str(count_vulnibm_iot_mediumaccescomplex_risklevel4)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN "+str(count_vulnibm_iot_mediumaccescomplex_risklevel3)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN "+str(count_vulnibm_iot_mediumaccescomplex_risklevel2)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN "+str(count_vulnibm_iot_mediumaccescomplex_risklevel1)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN "+str(count_vulnibm_iot_mediumaccescomplex_risklevel0)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 0 \n")






print("*****************************PORCENTAJE COMPLEJIDAD DE ACCESO/PUNTUACION BASE VULNERABILIDADES IBM PARTE IOT*****************************")
print("\n")                            
print("\n")
print(" DE UN TOTAL DE "+str(count_vulnibm_iot_access_complexity)+" VULNERABILIDADES :\n") 
print("\n")
print("   - LOS PORCENTAJES DE VALORES DE COMPLEJIDAD DE ACCESO SON LOS SIGUIENTES:  \n")
print("      -    EN EL  "+str(float(((count_vulnibm_iot_highaccescomplex*100)/count_vulnibm_iot_access_complexity)))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES ALTA, LOS PORCENTAJES DE NIVEL DE RIESGO SON LOS SIGUIENTES :  \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_highaccescomplex_risklevel10*100)/count_vulnibm_iot_highaccescomplex)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES 10 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_highaccescomplex_risklevel9*100)/count_vulnibm_iot_highaccescomplex)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_highaccescomplex_risklevel8*100)/count_vulnibm_iot_highaccescomplex)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_highaccescomplex_risklevel7*100)/count_vulnibm_iot_highaccescomplex)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_highaccescomplex_risklevel6*100)/count_vulnibm_iot_highaccescomplex)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_highaccescomplex_risklevel5*100)/count_vulnibm_iot_highaccescomplex)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_highaccescomplex_risklevel4*100)/count_vulnibm_iot_highaccescomplex)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_highaccescomplex_risklevel3*100)/count_vulnibm_iot_highaccescomplex)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_highaccescomplex_risklevel2*100)/count_vulnibm_iot_highaccescomplex)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_highaccescomplex_risklevel1*100)/count_vulnibm_iot_highaccescomplex)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_highaccescomplex_risklevel0*100)/count_vulnibm_iot_highaccescomplex)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 0 \n")
print("            -    EL VALOR MEDIO DE PUNTUACION BASE ES  "+str(float(((count_vulnibm_iot_highaccescomplex_risklevel)/count_vulnibm_iot_highaccescomplex)))+"\n")
print("\n")
print("      -    EN EL  "+str(float(((count_vulnibm_iot_lowaccescomplex*100)/count_vulnibm_iot_access_complexity)))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES BAJA, LOS PORCENTAJES DE NIVEL DE RIESGO SON LOS SIGUIENTES :  \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_lowaccescomplex_risklevel10*100)/count_vulnibm_iot_lowaccescomplex)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES 10 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_lowaccescomplex_risklevel9*100)/count_vulnibm_iot_lowaccescomplex)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_lowaccescomplex_risklevel8*100)/count_vulnibm_iot_lowaccescomplex)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_lowaccescomplex_risklevel7*100)/count_vulnibm_iot_lowaccescomplex)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_lowaccescomplex_risklevel6*100)/count_vulnibm_iot_lowaccescomplex)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_lowaccescomplex_risklevel5*100)/count_vulnibm_iot_lowaccescomplex)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_lowaccescomplex_risklevel4*100)/count_vulnibm_iot_lowaccescomplex)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_lowaccescomplex_risklevel3*100)/count_vulnibm_iot_lowaccescomplex)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_lowaccescomplex_risklevel2*100)/count_vulnibm_iot_lowaccescomplex)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_lowaccescomplex_risklevel1*100)/count_vulnibm_iot_lowaccescomplex)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_lowaccescomplex_risklevel0*100)/count_vulnibm_iot_lowaccescomplex)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 0 \n")
print("            -    EL VALOR MEDIO DE PUNTUACION BASE ES  "+str(float(((count_vulnibm_iot_lowaccescomplex_risklevel)/count_vulnibm_iot_lowaccescomplex)))+"\n")
print("\n")
if(count_vulnibm_iot_mediumaccescomplex>0):
    print("      -    EN EL  "+str(float(((count_vulnibm_iot_mediumaccescomplex*100)/count_vulnibm_iot_access_complexity)))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES MEDIA, LOS PORCENTAJES DE NIVEL DE RIESGO SON LOS SIGUIENTES :  \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_mediumaccescomplex_risklevel10*100)/count_vulnibm_iot_mediumaccescomplex)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES 10 \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_mediumaccescomplex_risklevel9*100)/count_vulnibm_iot_mediumaccescomplex)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 9 \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_mediumaccescomplex_risklevel8*100)/count_vulnibm_iot_mediumaccescomplex)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 8 \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_mediumaccescomplex_risklevel7*100)/count_vulnibm_iot_mediumaccescomplex)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 7 \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_mediumaccescomplex_risklevel6*100)/count_vulnibm_iot_mediumaccescomplex)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 6 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_iot_mediumaccescomplex_risklevel5*100)/count_vulnibm_iot_mediumaccescomplex)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 5 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_iot_mediumaccescomplex_risklevel4*100)/count_vulnibm_iot_mediumaccescomplex)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 4 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_iot_mediumaccescomplex_risklevel3*100)/count_vulnibm_iot_mediumaccescomplex)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 3 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_iot_mediumaccescomplex_risklevel2*100)/count_vulnibm_iot_mediumaccescomplex)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 2 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_iot_mediumaccescomplex_risklevel1*100)/count_vulnibm_iot_mediumaccescomplex)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 1 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_iot_mediumaccescomplex_risklevel0*100)/count_vulnibm_iot_mediumaccescomplex)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 0 \n")
    print("            -    EL VALOR MEDIO DE PUNTUACION BASE ES  "+str(float(((count_vulnibm_iot_mediumaccescomplex_risklevel)/count_vulnibm_iot_mediumaccescomplex)))+"\n")
    print("\n")


    
    
    
    
    
    
    
    
    
    
    
#Abro los ficheros con los que voy a tratar




df_vulnibm_sh = pd.read_excel('vulnerabilidades_ibm_smart_home_2023.xlsx')

#Variable para almacenar el contador total de valores para complejidad de acceso
count_vulnibm_sh_access_complexity=0

#Variables para almacenar el contador de valores para una complejidad de acceso determinada
count_vulnibm_sh_highaccescomplex=0
#Variable para almacenar la suma de nivel de riesgo para un determinado valor de complejidad de acceso
count_vulnibm_sh_highaccescomplex_risklevel=0
#Variable para almacenar el contador de valores de nivel de riesgo para una complejidad de acceso determinada
count_vulnibm_sh_highaccescomplex_risklevel10=0
count_vulnibm_sh_highaccescomplex_risklevel9=0
count_vulnibm_sh_highaccescomplex_risklevel8=0
count_vulnibm_sh_highaccescomplex_risklevel7=0
count_vulnibm_sh_highaccescomplex_risklevel6=0
count_vulnibm_sh_highaccescomplex_risklevel5=0
count_vulnibm_sh_highaccescomplex_risklevel4=0
count_vulnibm_sh_highaccescomplex_risklevel3=0
count_vulnibm_sh_highaccescomplex_risklevel2=0
count_vulnibm_sh_highaccescomplex_risklevel1=0
count_vulnibm_sh_highaccescomplex_risklevel0=0



count_vulnibm_sh_lowaccescomplex=0
count_vulnibm_sh_lowaccescomplex_risklevel=0
count_vulnibm_sh_lowaccescomplex_risklevel10=0
count_vulnibm_sh_lowaccescomplex_risklevel9=0
count_vulnibm_sh_lowaccescomplex_risklevel8=0
count_vulnibm_sh_lowaccescomplex_risklevel7=0
count_vulnibm_sh_lowaccescomplex_risklevel6=0
count_vulnibm_sh_lowaccescomplex_risklevel5=0
count_vulnibm_sh_lowaccescomplex_risklevel4=0
count_vulnibm_sh_lowaccescomplex_risklevel3=0
count_vulnibm_sh_lowaccescomplex_risklevel2=0
count_vulnibm_sh_lowaccescomplex_risklevel1=0
count_vulnibm_sh_lowaccescomplex_risklevel0=0


count_vulnibm_sh_mediumaccescomplex=0
count_vulnibm_sh_mediumaccescomplex_risklevel=0
count_vulnibm_sh_mediumaccescomplex_risklevel10=0
count_vulnibm_sh_mediumaccescomplex_risklevel9=0
count_vulnibm_sh_mediumaccescomplex_risklevel8=0
count_vulnibm_sh_mediumaccescomplex_risklevel7=0
count_vulnibm_sh_mediumaccescomplex_risklevel6=0
count_vulnibm_sh_mediumaccescomplex_risklevel5=0
count_vulnibm_sh_mediumaccescomplex_risklevel4=0
count_vulnibm_sh_mediumaccescomplex_risklevel3=0
count_vulnibm_sh_mediumaccescomplex_risklevel2=0
count_vulnibm_sh_mediumaccescomplex_risklevel1=0
count_vulnibm_sh_mediumaccescomplex_risklevel0=0





















#Comprobamos el valor de COMPLEJIDAD DE ACCESO
for r in range(0,len(df_vulnibm_sh["x_xfe_cvss_access_complexity"])):   
    #Obtenemos el valor de complejidad de acceso
    aux_str=df_vulnibm_sh["x_xfe_cvss_access_complexity"][r].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
    if(aux_str!='NONE' or aux_str!='None'):
        count_vulnibm_sh_access_complexity+=1
        #Comprobamos el nivel de complejidad de acceso
        if('High' in aux_str):
            count_vulnibm_sh_highaccescomplex+=1
            #Aumentamos la suma de valores de nivel de riesgo
            count_vulnibm_sh_highaccescomplex_risklevel+=float(df_vulnibm_sh["x_xfe_risk_level"][r])
            #Comprobamos el valor de nivel de riesgo
            if(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 10.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=9.0)):
                count_vulnibm_sh_highaccescomplex_risklevel9+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 9.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=8.0)):
                count_vulnibm_sh_highaccescomplex_risklevel8+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 8.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=7.0)):
                count_vulnibm_sh_highaccescomplex_risklevel7+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 7.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=6.0)):
                count_vulnibm_sh_highaccescomplex_risklevel6+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 6.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=5.0)):
                count_vulnibm_sh_highaccescomplex_risklevel5+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 5.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=4.0)):
                count_vulnibm_sh_highaccescomplex_risklevel4+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 4.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=3.0)):
                count_vulnibm_sh_highaccescomplex_risklevel3+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 3.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=2.0)):
                count_vulnibm_sh_highaccescomplex_risklevel2+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 2.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=1.0)):
                count_vulnibm_sh_highaccescomplex_risklevel1+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 1.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=0.0)):
                count_vulnibm_sh_highaccescomplex_risklevel0+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) == 10.0)):
                count_vulnibm_sh_highaccescomplex_risklevel10+=1
            
        elif('Low' in aux_str):
            
            count_vulnibm_sh_lowaccescomplex+=1
            count_vulnibm_sh_lowaccescomplex_risklevel+=float(df_vulnibm_sh["x_xfe_risk_level"][r])
            if(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 10.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=9.0)):
                count_vulnibm_sh_lowaccescomplex_risklevel9+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 9.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=8.0)):
                count_vulnibm_sh_lowaccescomplex_risklevel8+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 8.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=7.0)):
                count_vulnibm_sh_lowaccescomplex_risklevel7+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 7.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=6.0)):
                count_vulnibm_sh_lowaccescomplex_risklevel6+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 6.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=5.0)):
                count_vulnibm_sh_lowaccescomplex_risklevel5+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 5.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=4.0)):
                count_vulnibm_sh_lowaccescomplex_risklevel4+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 4.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=3.0)):
                count_vulnibm_sh_lowaccescomplex_risklevel3+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 3.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=2.0)):
                count_vulnibm_sh_lowaccescomplex_risklevel2+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 2.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=1.0)):
                count_vulnibm_sh_lowaccescomplex_risklevel1+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 1.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=0.0)):
                count_vulnibm_sh_lowaccescomplex_risklevel0+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) == 10.0)):
                count_vulnibm_sh_lowaccescomplex_risklevel10+=1
            
            
        elif('Medium' in aux_str):
        
            count_vulnibm_sh_mediumaccescomplex+=1
            count_vulnibm_sh_mediumaccescomplex_risklevel+=float(df_vulnibm_sh["x_xfe_risk_level"][r])
            if(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 10.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=9.0)):
                count_vulnibm_sh_mediumaccescomplex_risklevel9+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 9.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=8.0)):
                count_vulnibm_sh_mediumaccescomplex_risklevel8+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 8.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=7.0)):
                count_vulnibm_sh_mediumaccescomplex_risklevel7+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 7.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=6.0)):
                count_vulnibm_sh_mediumaccescomplex_risklevel6+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 6.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=5.0)):
                count_vulnibm_sh_mediumaccescomplex_risklevel5+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 5.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=4.0)):
                count_vulnibm_sh_mediumaccescomplex_risklevel4+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 4.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=3.0)):
                count_vulnibm_sh_mediumaccescomplex_risklevel3+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 3.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=2.0)):
                count_vulnibm_sh_mediumaccescomplex_risklevel2+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 2.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=1.0)):
                count_vulnibm_sh_mediumaccescomplex_risklevel1+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 1.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=0.0)):
                count_vulnibm_sh_mediumaccescomplex_risklevel0+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) == 10.0)):
                count_vulnibm_sh_mediumaccescomplex_risklevel10+=1
            
        
                
                
                
                
print("*****************************ESTADÍSTICAS COMPLEJIDAD DE ACCESO/PUNTUACION BASE VULNERABILIDADES IBM PARTE SMART HOME*****************************")
print("\n")                            
print("\n")
print(" DE UN TOTAL DE "+str(count_vulnibm_sh_access_complexity)+" VULNERABILIDADES:\n") 
print("\n")
print("   - LAS ESTADISTICAS DE VALORES DE COMPLEJIDAD DE ACCESO SON LAS SIGUIENTES:  \n")
print("      -    EN  "+str(count_vulnibm_sh_highaccescomplex)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES ALTA, LAS ESTADÍSTICAS DE NIVEL DE RIESGO SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_sh_highaccescomplex_risklevel10)+" VULNERABILIDADES EL NIVEL DE RIESGO ES 10 \n")
print("            -    EN  "+str(count_vulnibm_sh_highaccescomplex_risklevel9)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN  "+str(count_vulnibm_sh_highaccescomplex_risklevel8)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN  "+str(count_vulnibm_sh_highaccescomplex_risklevel7)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN  "+str(count_vulnibm_sh_highaccescomplex_risklevel6)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN "+str(count_vulnibm_sh_highaccescomplex_risklevel5)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN "+str(count_vulnibm_sh_highaccescomplex_risklevel4)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN "+str(count_vulnibm_sh_highaccescomplex_risklevel3)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN "+str(count_vulnibm_sh_highaccescomplex_risklevel2)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN "+str(count_vulnibm_sh_highaccescomplex_risklevel1)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN "+str(count_vulnibm_sh_highaccescomplex_risklevel0)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 0 \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_sh_lowaccescomplex)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES BAJA, LAS ESTADÍSTICAS DE NIVEL DE RIESGO SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_sh_lowaccescomplex_risklevel10)+" VULNERABILIDADES EL NIVEL DE RIESGO ES 10 \n")
print("            -    EN  "+str(count_vulnibm_sh_lowaccescomplex_risklevel9)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN  "+str(count_vulnibm_sh_lowaccescomplex_risklevel8)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN  "+str(count_vulnibm_sh_lowaccescomplex_risklevel7)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN  "+str(count_vulnibm_sh_lowaccescomplex_risklevel6)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN "+str(count_vulnibm_sh_lowaccescomplex_risklevel5)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN "+str(count_vulnibm_sh_lowaccescomplex_risklevel4)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN "+str(count_vulnibm_sh_lowaccescomplex_risklevel3)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN "+str(count_vulnibm_sh_lowaccescomplex_risklevel2)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN "+str(count_vulnibm_sh_lowaccescomplex_risklevel1)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN "+str(count_vulnibm_sh_lowaccescomplex_risklevel0)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 0 \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_sh_mediumaccescomplex)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES MEDIA, LAS ESTADÍSTICAS DE NIVEL DE RIESGO SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_sh_mediumaccescomplex_risklevel10)+" VULNERABILIDADES EL NIVEL DE RIESGO ES 10 \n")
print("            -    EN  "+str(count_vulnibm_sh_mediumaccescomplex_risklevel9)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN  "+str(count_vulnibm_sh_mediumaccescomplex_risklevel8)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN  "+str(count_vulnibm_sh_mediumaccescomplex_risklevel7)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN  "+str(count_vulnibm_sh_mediumaccescomplex_risklevel6)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN "+str(count_vulnibm_sh_mediumaccescomplex_risklevel5)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN "+str(count_vulnibm_sh_mediumaccescomplex_risklevel4)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN "+str(count_vulnibm_sh_mediumaccescomplex_risklevel3)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN "+str(count_vulnibm_sh_mediumaccescomplex_risklevel2)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN "+str(count_vulnibm_sh_mediumaccescomplex_risklevel1)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN "+str(count_vulnibm_sh_mediumaccescomplex_risklevel0)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 0 \n")






print("*****************************PORCENTAJE COMPLEJIDAD DE ACCESO/PUNTUACION BASE VULNERABILIDADES IBM PARTE SMART HOME*****************************")
print("\n")                            
print("\n")
print(" DE UN TOTAL DE "+str(count_vulnibm_sh_access_complexity)+" VULNERABILIDADES :\n") 
print("\n")
print("   - LOS PORCENTAJES DE VALORES DE COMPLEJIDAD DE ACCESO SON LOS SIGUIENTES:  \n")
print("      -    EN EL  "+str(float(((count_vulnibm_sh_highaccescomplex*100)/count_vulnibm_sh_access_complexity)))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES ALTA, LOS PORCENTAJES DE NIVEL DE RIESGO SON LOS SIGUIENTES :  \n")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_highaccescomplex_risklevel10*100)/count_vulnibm_sh_highaccescomplex)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES 10 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_highaccescomplex_risklevel9*100)/count_vulnibm_sh_highaccescomplex)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_highaccescomplex_risklevel8*100)/count_vulnibm_sh_highaccescomplex)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_highaccescomplex_risklevel7*100)/count_vulnibm_sh_highaccescomplex)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_highaccescomplex_risklevel6*100)/count_vulnibm_sh_highaccescomplex)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN EL "+str(float(((count_vulnibm_sh_highaccescomplex_risklevel5*100)/count_vulnibm_sh_highaccescomplex)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN EL "+str(float(((count_vulnibm_sh_highaccescomplex_risklevel4*100)/count_vulnibm_sh_highaccescomplex)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN EL "+str(float(((count_vulnibm_sh_highaccescomplex_risklevel3*100)/count_vulnibm_sh_highaccescomplex)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN EL "+str(float(((count_vulnibm_sh_highaccescomplex_risklevel2*100)/count_vulnibm_sh_highaccescomplex)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN EL "+str(float(((count_vulnibm_sh_highaccescomplex_risklevel1*100)/count_vulnibm_sh_highaccescomplex)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN EL "+str(float(((count_vulnibm_sh_highaccescomplex_risklevel0*100)/count_vulnibm_sh_highaccescomplex)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 0 \n")
print("            -    EL VALOR MEDIO DE PUNTUACION BASE ES  "+str(float(((count_vulnibm_sh_highaccescomplex_risklevel)/count_vulnibm_sh_highaccescomplex)))+"\n")
print("\n")
print("      -    EN EL  "+str(float(((count_vulnibm_sh_lowaccescomplex*100)/count_vulnibm_sh_access_complexity)))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES BAJA, LOS PORCENTAJES DE NIVEL DE RIESGO SON LOS SIGUIENTES :  \n")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_lowaccescomplex_risklevel10*100)/count_vulnibm_sh_lowaccescomplex)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES 10 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_lowaccescomplex_risklevel9*100)/count_vulnibm_sh_lowaccescomplex)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_lowaccescomplex_risklevel8*100)/count_vulnibm_sh_lowaccescomplex)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_lowaccescomplex_risklevel7*100)/count_vulnibm_sh_lowaccescomplex)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_lowaccescomplex_risklevel6*100)/count_vulnibm_sh_lowaccescomplex)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN EL "+str(float(((count_vulnibm_sh_lowaccescomplex_risklevel5*100)/count_vulnibm_sh_lowaccescomplex)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN EL "+str(float(((count_vulnibm_sh_lowaccescomplex_risklevel4*100)/count_vulnibm_sh_lowaccescomplex)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN EL "+str(float(((count_vulnibm_sh_lowaccescomplex_risklevel3*100)/count_vulnibm_sh_lowaccescomplex)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN EL "+str(float(((count_vulnibm_sh_lowaccescomplex_risklevel2*100)/count_vulnibm_sh_lowaccescomplex)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN EL "+str(float(((count_vulnibm_sh_lowaccescomplex_risklevel1*100)/count_vulnibm_sh_lowaccescomplex)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN EL "+str(float(((count_vulnibm_sh_lowaccescomplex_risklevel0*100)/count_vulnibm_sh_lowaccescomplex)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 0 \n")
print("            -    EL VALOR MEDIO DE PUNTUACION BASE ES  "+str(float(((count_vulnibm_sh_lowaccescomplex_risklevel)/count_vulnibm_sh_lowaccescomplex)))+"\n")
print("\n")
if(count_vulnibm_sh_mediumaccescomplex>0):
    print("      -    EN EL  "+str(float(((count_vulnibm_sh_mediumaccescomplex*100)/count_vulnibm_sh_access_complexity)))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES MEDIA, LOS PORCENTAJES DE NIVEL DE RIESGO SON LOS SIGUIENTES :  \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_mediumaccescomplex_risklevel10*100)/count_vulnibm_sh_mediumaccescomplex)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES 10 \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_mediumaccescomplex_risklevel9*100)/count_vulnibm_sh_mediumaccescomplex)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 9 \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_mediumaccescomplex_risklevel8*100)/count_vulnibm_sh_mediumaccescomplex)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 8 \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_mediumaccescomplex_risklevel7*100)/count_vulnibm_sh_mediumaccescomplex)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 7 \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_mediumaccescomplex_risklevel6*100)/count_vulnibm_sh_mediumaccescomplex)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 6 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_sh_mediumaccescomplex_risklevel5*100)/count_vulnibm_sh_mediumaccescomplex)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 5 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_sh_mediumaccescomplex_risklevel4*100)/count_vulnibm_sh_mediumaccescomplex)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 4 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_sh_mediumaccescomplex_risklevel3*100)/count_vulnibm_sh_mediumaccescomplex)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 3 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_sh_mediumaccescomplex_risklevel2*100)/count_vulnibm_sh_mediumaccescomplex)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 2 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_sh_mediumaccescomplex_risklevel1*100)/count_vulnibm_sh_mediumaccescomplex)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 1 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_sh_mediumaccescomplex_risklevel0*100)/count_vulnibm_sh_mediumaccescomplex)))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 0 \n")
    print("            -    EL VALOR MEDIO DE PUNTUACION BASE ES  "+str(float(((count_vulnibm_sh_mediumaccescomplex_risklevel)/count_vulnibm_sh_mediumaccescomplex)))+"\n")
    print("\n")


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
print("*****************************ESTADÍSTICAS COMPLEJIDAD DE ACCESO/PUNTUACION BASE VULNERABILIDADES IBM PARTE IOT Y SMART HOME*****************************")
print("\n")                            
print("\n")
print(" DE UN TOTAL DE "+str(count_vulnibm_iot_access_complexity+count_vulnibm_sh_access_complexity)+" VULNERABILIDADES:\n") 
print("\n")
print("   - LAS ESTADISTICAS DE VALORES DE COMPLEJIDAD DE ACCESO SON LAS SIGUIENTES:  \n")
print("      -    EN  "+str(count_vulnibm_iot_highaccescomplex+count_vulnibm_sh_highaccescomplex)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES ALTA, LAS ESTADÍSTICAS DE NIVEL DE RIESGO SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_highaccescomplex_risklevel10+count_vulnibm_sh_highaccescomplex_risklevel10)+" VULNERABILIDADES EL NIVEL DE RIESGO ES 10 \n")
print("            -    EN  "+str(count_vulnibm_iot_highaccescomplex_risklevel9+count_vulnibm_sh_highaccescomplex_risklevel9)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN  "+str(count_vulnibm_iot_highaccescomplex_risklevel8+count_vulnibm_sh_highaccescomplex_risklevel8)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN  "+str(count_vulnibm_iot_highaccescomplex_risklevel7+count_vulnibm_sh_highaccescomplex_risklevel7)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN  "+str(count_vulnibm_iot_highaccescomplex_risklevel6+count_vulnibm_sh_highaccescomplex_risklevel6)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN "+str(count_vulnibm_iot_highaccescomplex_risklevel5+count_vulnibm_sh_highaccescomplex_risklevel5)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN "+str(count_vulnibm_iot_highaccescomplex_risklevel4+count_vulnibm_sh_highaccescomplex_risklevel4)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN "+str(count_vulnibm_iot_highaccescomplex_risklevel3+count_vulnibm_sh_highaccescomplex_risklevel3)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN "+str(count_vulnibm_iot_highaccescomplex_risklevel2+count_vulnibm_sh_highaccescomplex_risklevel2)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN "+str(count_vulnibm_iot_highaccescomplex_risklevel1+count_vulnibm_sh_highaccescomplex_risklevel1)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN "+str(count_vulnibm_iot_highaccescomplex_risklevel0+count_vulnibm_sh_highaccescomplex_risklevel0)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 0 \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_lowaccescomplex+count_vulnibm_sh_lowaccescomplex)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES BAJA, LAS ESTADÍSTICAS DE NIVEL DE RIESGO SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_lowaccescomplex_risklevel10+count_vulnibm_sh_lowaccescomplex_risklevel10)+" VULNERABILIDADES EL NIVEL DE RIESGO ES 10 \n")
print("            -    EN  "+str(count_vulnibm_iot_lowaccescomplex_risklevel9+count_vulnibm_sh_lowaccescomplex_risklevel9)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN  "+str(count_vulnibm_iot_lowaccescomplex_risklevel8+count_vulnibm_sh_lowaccescomplex_risklevel8)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN  "+str(count_vulnibm_iot_lowaccescomplex_risklevel7+count_vulnibm_sh_lowaccescomplex_risklevel7)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN  "+str(count_vulnibm_iot_lowaccescomplex_risklevel6+count_vulnibm_sh_lowaccescomplex_risklevel6)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN "+str(count_vulnibm_iot_lowaccescomplex_risklevel5+count_vulnibm_sh_lowaccescomplex_risklevel5)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN "+str(count_vulnibm_iot_lowaccescomplex_risklevel4+count_vulnibm_sh_lowaccescomplex_risklevel4)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN "+str(count_vulnibm_iot_lowaccescomplex_risklevel3+count_vulnibm_sh_lowaccescomplex_risklevel3)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN "+str(count_vulnibm_iot_lowaccescomplex_risklevel2+count_vulnibm_sh_lowaccescomplex_risklevel2)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN "+str(count_vulnibm_iot_lowaccescomplex_risklevel1+count_vulnibm_sh_lowaccescomplex_risklevel1)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN "+str(count_vulnibm_iot_lowaccescomplex_risklevel0+count_vulnibm_sh_lowaccescomplex_risklevel0)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 0 \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_mediumaccescomplex+count_vulnibm_sh_mediumaccescomplex)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES MEDIA, LAS ESTADÍSTICAS DE NIVEL DE RIESGO SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_mediumaccescomplex_risklevel10+count_vulnibm_sh_mediumaccescomplex_risklevel10)+" VULNERABILIDADES EL NIVEL DE RIESGO ES 10 \n")
print("            -    EN  "+str(count_vulnibm_iot_mediumaccescomplex_risklevel9+count_vulnibm_sh_mediumaccescomplex_risklevel9)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN  "+str(count_vulnibm_iot_mediumaccescomplex_risklevel8+count_vulnibm_sh_mediumaccescomplex_risklevel8)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN  "+str(count_vulnibm_iot_mediumaccescomplex_risklevel7+count_vulnibm_sh_mediumaccescomplex_risklevel7)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN  "+str(count_vulnibm_iot_mediumaccescomplex_risklevel6+count_vulnibm_sh_mediumaccescomplex_risklevel6)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN "+str(count_vulnibm_iot_mediumaccescomplex_risklevel5+count_vulnibm_sh_mediumaccescomplex_risklevel5)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN "+str(count_vulnibm_iot_mediumaccescomplex_risklevel4+count_vulnibm_sh_mediumaccescomplex_risklevel4)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN "+str(count_vulnibm_iot_mediumaccescomplex_risklevel3+count_vulnibm_sh_mediumaccescomplex_risklevel3)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN "+str(count_vulnibm_iot_mediumaccescomplex_risklevel2+count_vulnibm_sh_mediumaccescomplex_risklevel2)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN "+str(count_vulnibm_iot_mediumaccescomplex_risklevel1+count_vulnibm_sh_mediumaccescomplex_risklevel1)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN "+str(count_vulnibm_iot_mediumaccescomplex_risklevel0+count_vulnibm_sh_mediumaccescomplex_risklevel0)+" VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 0 \n")
print("\n")










print("*****************************PORCENTAJES COMPLEJIDAD DE ACCESO/PUNTUACION BASE VULNERABILIDADES IBM PARTE IOT Y SMART HOME*****************************")
print("\n")                            
print("\n")
print(" DE UN TOTAL DE "+str(count_vulnibm_iot_access_complexity+count_vulnibm_sh_access_complexity)+" VULNERABILIDADES :\n") 
print("\n")
print("   - LOS PORCENTAJES DE VALORES DE COMPLEJIDAD DE ACCESO SON LOS SIGUIENTES:  \n")
print("      -    EN EL "+str(float((((count_vulnibm_iot_highaccescomplex+count_vulnibm_sh_highaccescomplex)*100)/(count_vulnibm_iot_access_complexity+count_vulnibm_sh_access_complexity))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES ALTA, LOS PORCENTAJES DE NIVEL DE RIESGO SON LOS SIGUIENTES :  \n")
print("            -    EN EL"+str(float((((count_vulnibm_iot_highaccescomplex_risklevel10+count_vulnibm_sh_highaccescomplex_risklevel10)*100)/(count_vulnibm_iot_highaccescomplex+count_vulnibm_sh_highaccescomplex))))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES 10 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_highaccescomplex_risklevel9+count_vulnibm_sh_highaccescomplex_risklevel9)*100)/(count_vulnibm_iot_highaccescomplex+count_vulnibm_sh_highaccescomplex))))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_highaccescomplex_risklevel8+count_vulnibm_sh_highaccescomplex_risklevel8)*100)/(count_vulnibm_iot_highaccescomplex+count_vulnibm_sh_highaccescomplex))))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_highaccescomplex_risklevel7+count_vulnibm_sh_highaccescomplex_risklevel7)*100)/(count_vulnibm_iot_highaccescomplex+count_vulnibm_sh_highaccescomplex))))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_highaccescomplex_risklevel6+count_vulnibm_sh_highaccescomplex_risklevel6)*100)/(count_vulnibm_iot_highaccescomplex+count_vulnibm_sh_highaccescomplex))))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_highaccescomplex_risklevel5+count_vulnibm_sh_highaccescomplex_risklevel5)*100)/(count_vulnibm_iot_highaccescomplex+count_vulnibm_sh_highaccescomplex))))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_highaccescomplex_risklevel4+count_vulnibm_sh_highaccescomplex_risklevel4)*100)/(count_vulnibm_iot_highaccescomplex+count_vulnibm_sh_highaccescomplex))))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_highaccescomplex_risklevel3+count_vulnibm_sh_highaccescomplex_risklevel3)*100)/(count_vulnibm_iot_highaccescomplex+count_vulnibm_sh_highaccescomplex))))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_highaccescomplex_risklevel2+count_vulnibm_sh_highaccescomplex_risklevel2)*100)/(count_vulnibm_iot_highaccescomplex+count_vulnibm_sh_highaccescomplex))))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_highaccescomplex_risklevel1+count_vulnibm_sh_highaccescomplex_risklevel1)*100)/(count_vulnibm_iot_highaccescomplex+count_vulnibm_sh_highaccescomplex))))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_highaccescomplex_risklevel0+count_vulnibm_sh_highaccescomplex_risklevel0)*100)/(count_vulnibm_iot_highaccescomplex+count_vulnibm_sh_highaccescomplex))))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 0 \n")
print("            -    EL VALOR MEDIO DE PUNTUACION BASE ES  "+str(float(((count_vulnibm_iot_highaccescomplex_risklevel+count_vulnibm_sh_highaccescomplex_risklevel)/(count_vulnibm_iot_highaccescomplex+count_vulnibm_sh_highaccescomplex))))+"\n")
print("\n")
print("      -    EN EL "+str(float((((count_vulnibm_iot_lowaccescomplex+count_vulnibm_sh_lowaccescomplex)*100)/(count_vulnibm_iot_access_complexity+count_vulnibm_sh_access_complexity))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES BAJA, LOS PORCENTAJES DE NIVEL DE RIESGO SON LOS SIGUIENTES :  \n")
print("            -    EN EL"+str(float((((count_vulnibm_iot_lowaccescomplex_risklevel10+count_vulnibm_sh_lowaccescomplex_risklevel10)*100)/(count_vulnibm_iot_lowaccescomplex+count_vulnibm_sh_lowaccescomplex))))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES 10 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_lowaccescomplex_risklevel9+count_vulnibm_sh_lowaccescomplex_risklevel9)*100)/(count_vulnibm_iot_lowaccescomplex+count_vulnibm_sh_lowaccescomplex))))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_lowaccescomplex_risklevel8+count_vulnibm_sh_lowaccescomplex_risklevel8)*100)/(count_vulnibm_iot_lowaccescomplex+count_vulnibm_sh_lowaccescomplex))))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_lowaccescomplex_risklevel7+count_vulnibm_sh_lowaccescomplex_risklevel7)*100)/(count_vulnibm_iot_lowaccescomplex+count_vulnibm_sh_lowaccescomplex))))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_lowaccescomplex_risklevel6+count_vulnibm_sh_lowaccescomplex_risklevel6)*100)/(count_vulnibm_iot_lowaccescomplex+count_vulnibm_sh_lowaccescomplex))))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_lowaccescomplex_risklevel5+count_vulnibm_sh_lowaccescomplex_risklevel5)*100)/(count_vulnibm_iot_lowaccescomplex+count_vulnibm_sh_lowaccescomplex))))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_lowaccescomplex_risklevel4+count_vulnibm_sh_lowaccescomplex_risklevel4)*100)/(count_vulnibm_iot_lowaccescomplex+count_vulnibm_sh_lowaccescomplex))))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_lowaccescomplex_risklevel3+count_vulnibm_sh_lowaccescomplex_risklevel3)*100)/(count_vulnibm_iot_lowaccescomplex+count_vulnibm_sh_lowaccescomplex))))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_lowaccescomplex_risklevel2+count_vulnibm_sh_lowaccescomplex_risklevel2)*100)/(count_vulnibm_iot_lowaccescomplex+count_vulnibm_sh_lowaccescomplex))))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_lowaccescomplex_risklevel1+count_vulnibm_sh_lowaccescomplex_risklevel1)*100)/(count_vulnibm_iot_lowaccescomplex+count_vulnibm_sh_lowaccescomplex))))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_lowaccescomplex_risklevel0+count_vulnibm_sh_lowaccescomplex_risklevel0)*100)/(count_vulnibm_iot_lowaccescomplex+count_vulnibm_sh_lowaccescomplex))))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 0 \n")
print("            -    EL VALOR MEDIO DE PUNTUACION BASE ES  "+str(float(((count_vulnibm_iot_lowaccescomplex_risklevel+count_vulnibm_sh_lowaccescomplex_risklevel)/(count_vulnibm_iot_lowaccescomplex+count_vulnibm_sh_lowaccescomplex))))+"\n")
print("\n")
if((count_vulnibm_iot_mediumaccescomplex+count_vulnibm_sh_mediumaccescomplex)>0):
    print("      -    EN EL "+str(float((((count_vulnibm_iot_mediumaccescomplex+count_vulnibm_sh_mediumaccescomplex)*100)/(count_vulnibm_iot_access_complexity+count_vulnibm_sh_access_complexity))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES MEDIA, LOS PORCENTAJES DE NIVEL DE RIESGO SON LOS SIGUIENTES :  \n")
    print("            -    EN EL"+str(float((((count_vulnibm_iot_mediumaccescomplex_risklevel10+count_vulnibm_sh_mediumaccescomplex_risklevel10)*100)/(count_vulnibm_iot_mediumaccescomplex+count_vulnibm_sh_mediumaccescomplex))))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES 10 \n")
    print("            -    EN EL "+str(float((((count_vulnibm_iot_mediumaccescomplex_risklevel9+count_vulnibm_sh_mediumaccescomplex_risklevel9)*100)/(count_vulnibm_iot_mediumaccescomplex+count_vulnibm_sh_mediumaccescomplex))))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 9 \n")
    print("            -    EN EL "+str(float((((count_vulnibm_iot_mediumaccescomplex_risklevel8+count_vulnibm_sh_mediumaccescomplex_risklevel8)*100)/(count_vulnibm_iot_mediumaccescomplex+count_vulnibm_sh_mediumaccescomplex))))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 8 \n")
    print("            -    EN EL "+str(float((((count_vulnibm_iot_mediumaccescomplex_risklevel7+count_vulnibm_sh_mediumaccescomplex_risklevel7)*100)/(count_vulnibm_iot_mediumaccescomplex+count_vulnibm_sh_mediumaccescomplex))))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 7 \n")
    print("            -    EN EL "+str(float((((count_vulnibm_iot_mediumaccescomplex_risklevel6+count_vulnibm_sh_mediumaccescomplex_risklevel6)*100)/(count_vulnibm_iot_mediumaccescomplex+count_vulnibm_sh_mediumaccescomplex))))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 6 \n")
    print("            -    EN EL "+str(float((((count_vulnibm_iot_mediumaccescomplex_risklevel5+count_vulnibm_sh_mediumaccescomplex_risklevel5)*100)/(count_vulnibm_iot_mediumaccescomplex+count_vulnibm_sh_mediumaccescomplex))))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 5 \n")
    print("            -    EN EL "+str(float((((count_vulnibm_iot_mediumaccescomplex_risklevel4+count_vulnibm_sh_mediumaccescomplex_risklevel4)*100)/(count_vulnibm_iot_mediumaccescomplex+count_vulnibm_sh_mediumaccescomplex))))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 4 \n")
    print("            -    EN EL "+str(float((((count_vulnibm_iot_mediumaccescomplex_risklevel3+count_vulnibm_sh_mediumaccescomplex_risklevel3)*100)/(count_vulnibm_iot_mediumaccescomplex+count_vulnibm_sh_mediumaccescomplex))))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 3 \n")
    print("            -    EN EL "+str(float((((count_vulnibm_iot_mediumaccescomplex_risklevel2+count_vulnibm_sh_mediumaccescomplex_risklevel2)*100)/(count_vulnibm_iot_mediumaccescomplex+count_vulnibm_sh_mediumaccescomplex))))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 2 \n")
    print("            -    EN EL "+str(float((((count_vulnibm_iot_mediumaccescomplex_risklevel1+count_vulnibm_sh_mediumaccescomplex_risklevel1)*100)/(count_vulnibm_iot_mediumaccescomplex+count_vulnibm_sh_mediumaccescomplex))))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 1 \n")
    print("            -    EN EL "+str(float((((count_vulnibm_iot_mediumaccescomplex_risklevel0+count_vulnibm_sh_mediumaccescomplex_risklevel0)*100)/(count_vulnibm_iot_mediumaccescomplex+count_vulnibm_sh_mediumaccescomplex))))+" % DE VULNERABILIDADES EL NIVEL DE RIESGO ES MAYOR O IGUAL QUE 0 \n")
    print("            -    EL VALOR MEDIO DE PUNTUACION BASE ES  "+str(float(((count_vulnibm_iot_mediumaccescomplex_risklevel+count_vulnibm_sh_mediumaccescomplex_risklevel)/(count_vulnibm_iot_mediumaccescomplex+count_vulnibm_sh_mediumaccescomplex))))+"\n")
    print("\n") 


































