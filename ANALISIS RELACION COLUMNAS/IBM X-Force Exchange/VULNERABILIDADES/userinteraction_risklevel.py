




import pandas as pd
from datetime import datetime,timedelta



#Abro los ficheros con los que voy a tratar




df_vulnibm_iot = pd.read_excel('vulnerabilidades_ibm_iot_2023.xlsx')

count_vulnibm_iot_user_interaction=0

count_vulnibm_iot_requireduserinteraction=0
count_vulnibm_iot_requireduserinteraction_risklevel=0
count_vulnibm_iot_requireduserinteraction_risklevel10=0
count_vulnibm_iot_requireduserinteraction_risklevel9=0
count_vulnibm_iot_requireduserinteraction_risklevel8=0
count_vulnibm_iot_requireduserinteraction_risklevel7=0
count_vulnibm_iot_requireduserinteraction_risklevel6=0
count_vulnibm_iot_requireduserinteraction_risklevel5=0
count_vulnibm_iot_requireduserinteraction_risklevel4=0
count_vulnibm_iot_requireduserinteraction_risklevel3=0
count_vulnibm_iot_requireduserinteraction_risklevel2=0
count_vulnibm_iot_requireduserinteraction_risklevel1=0
count_vulnibm_iot_requireduserinteraction_risklevel0=0



count_vulnibm_iot_nonerequireduserinteraction=0
count_vulnibm_iot_nonerequireduserinteraction_risklevel=0
count_vulnibm_iot_nonerequireduserinteraction_risklevel10=0
count_vulnibm_iot_nonerequireduserinteraction_risklevel9=0
count_vulnibm_iot_nonerequireduserinteraction_risklevel8=0
count_vulnibm_iot_nonerequireduserinteraction_risklevel7=0
count_vulnibm_iot_nonerequireduserinteraction_risklevel6=0
count_vulnibm_iot_nonerequireduserinteraction_risklevel5=0
count_vulnibm_iot_nonerequireduserinteraction_risklevel4=0
count_vulnibm_iot_nonerequireduserinteraction_risklevel3=0
count_vulnibm_iot_nonerequireduserinteraction_risklevel2=0
count_vulnibm_iot_nonerequireduserinteraction_risklevel1=0
count_vulnibm_iot_nonerequireduserinteraction_risklevel0=0




#Comprobamos el contenido de INTERACCION DE USUARIO
for r in range(0,len(df_vulnibm_iot["x_xfe_cvss_userinteraction"])):  
    count_vulnibm_iot_user_interaction+=1
    if( (isinstance(df_vulnibm_iot["x_xfe_cvss_userinteraction"][r],str)) and ('Required' in df_vulnibm_iot["x_xfe_cvss_userinteraction"][r])):
        count_vulnibm_iot_requireduserinteraction+=1
        count_vulnibm_iot_requireduserinteraction_risklevel+=float(df_vulnibm_iot["x_xfe_risk_level"][r])
        if(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 10.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=9.0)):
            count_vulnibm_iot_requireduserinteraction_risklevel9+=1
        elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 9.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=8.0)):
            count_vulnibm_iot_requireduserinteraction_risklevel8+=1
        elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 8.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=7.0)):
            count_vulnibm_iot_requireduserinteraction_risklevel7+=1
        elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 7.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=6.0)):
            count_vulnibm_iot_requireduserinteraction_risklevel6+=1
        elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 6.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=5.0)):
            count_vulnibm_iot_requireduserinteraction_risklevel5+=1
        elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 5.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=4.0)):
            count_vulnibm_iot_requireduserinteraction_risklevel4+=1
        elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 4.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=3.0)):
            count_vulnibm_iot_requireduserinteraction_risklevel3+=1
        elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 3.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=2.0)):
            count_vulnibm_iot_requireduserinteraction_risklevel2+=1
        elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 2.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=1.0)):
            count_vulnibm_iot_requireduserinteraction_risklevel1+=1
        elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 1.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=0.0)):
            count_vulnibm_iot_requireduserinteraction_risklevel0+=1
        elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) == 10.0)):
            count_vulnibm_iot_requireduserinteraction_risklevel10+=1

    else:

        count_vulnibm_iot_nonerequireduserinteraction+=1
        count_vulnibm_iot_nonerequireduserinteraction_risklevel+=float(df_vulnibm_iot["x_xfe_risk_level"][r])
        if(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 10.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=9.0)):
            count_vulnibm_iot_nonerequireduserinteraction_risklevel9+=1
        elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 9.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=8.0)):
            count_vulnibm_iot_nonerequireduserinteraction_risklevel8+=1
        elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 8.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=7.0)):
            count_vulnibm_iot_nonerequireduserinteraction_risklevel7+=1
        elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 7.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=6.0)):
            count_vulnibm_iot_nonerequireduserinteraction_risklevel6+=1
        elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 6.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=5.0)):
            count_vulnibm_iot_nonerequireduserinteraction_risklevel5+=1
        elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 5.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=4.0)):
            count_vulnibm_iot_nonerequireduserinteraction_risklevel4+=1
        elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 4.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=3.0)):
            count_vulnibm_iot_nonerequireduserinteraction_risklevel3+=1
        elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 3.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=2.0)):
            count_vulnibm_iot_nonerequireduserinteraction_risklevel2+=1
        elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 2.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=1.0)):
            count_vulnibm_iot_nonerequireduserinteraction_risklevel1+=1
        elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 1.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=0.0)):
            count_vulnibm_iot_nonerequireduserinteraction_risklevel0+=1
        elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) == 10.0)):
            count_vulnibm_iot_nonerequireduserinteraction_risklevel10+=1
            
            
        
        
                
                
                
                
print("********************************ESTADÍSTICAS INTERACCION DE USUARIO/PUNTUACION BASE VULNERABILIDADES IBM PARTE IOT********************************")
print("\n")                            
print("\n")
print(" DE UN TOTAL DE "+str(count_vulnibm_iot_user_interaction)+" VULNERABILIDADES:\n") 
print("\n")
print("   - LAS ESTADISTICAS DE VALORES DE INTERACCION DE USUARIO SON LAS SIGUIENTES:  \n")
print("      -    EN  "+str(count_vulnibm_iot_requireduserinteraction)+" VULNERABILIDADES LA INTERACCION DE USUARIO ES REQUERIDA, LAS ESTADÍSTICAS DE PUNTUACION BASE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_requireduserinteraction_risklevel10)+" VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
print("            -    EN  "+str(count_vulnibm_iot_requireduserinteraction_risklevel9)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN  "+str(count_vulnibm_iot_requireduserinteraction_risklevel8)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN  "+str(count_vulnibm_iot_requireduserinteraction_risklevel7)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN  "+str(count_vulnibm_iot_requireduserinteraction_risklevel6)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN "+str(count_vulnibm_iot_requireduserinteraction_risklevel5)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN "+str(count_vulnibm_iot_requireduserinteraction_risklevel4)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN "+str(count_vulnibm_iot_requireduserinteraction_risklevel3)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN "+str(count_vulnibm_iot_requireduserinteraction_risklevel2)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN "+str(count_vulnibm_iot_requireduserinteraction_risklevel1)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN "+str(count_vulnibm_iot_requireduserinteraction_risklevel0)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_nonerequireduserinteraction)+" VULNERABILIDADES LA INTERACCION DE USUARIO NO SE REQUIERE, LAS ESTADÍSTICAS DE PUNTUACION BASE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_nonerequireduserinteraction_risklevel10)+" VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
print("            -    EN  "+str(count_vulnibm_iot_nonerequireduserinteraction_risklevel9)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN  "+str(count_vulnibm_iot_nonerequireduserinteraction_risklevel8)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN  "+str(count_vulnibm_iot_nonerequireduserinteraction_risklevel7)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN  "+str(count_vulnibm_iot_nonerequireduserinteraction_risklevel6)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN "+str(count_vulnibm_iot_nonerequireduserinteraction_risklevel5)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN "+str(count_vulnibm_iot_nonerequireduserinteraction_risklevel4)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN "+str(count_vulnibm_iot_nonerequireduserinteraction_risklevel3)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN "+str(count_vulnibm_iot_nonerequireduserinteraction_risklevel2)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN "+str(count_vulnibm_iot_nonerequireduserinteraction_risklevel1)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN "+str(count_vulnibm_iot_nonerequireduserinteraction_risklevel0)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("\n")




print("********************************PORCENTAJE INTERACCION DE USUARIO/PUNTUACION BASE VULNERABILIDADES IBM PARTE IOT********************************")
print("\n")                            
print("\n")
print(" DE UN TOTAL DE "+str(count_vulnibm_iot_user_interaction)+" VULNERABILIDADES :\n") 
print("\n")
print("   - LOS PORCENTAJES DE VALORES DE INTERACCION DE USUARIO SON LOS SIGUIENTES:  \n")
print("      -    EN EL  "+str(float(((count_vulnibm_iot_requireduserinteraction*100)/count_vulnibm_iot_user_interaction)))+" % DE VULNERABILIDADES LA INTERACCION DE USUARIO ES REQUERIDA, LAS ESTADÍSTICAS DE PUNTUACION BASE SON LAS SIGUIENTES :  \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_requireduserinteraction_risklevel10*100)/count_vulnibm_iot_requireduserinteraction)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_requireduserinteraction_risklevel9*100)/count_vulnibm_iot_requireduserinteraction)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_requireduserinteraction_risklevel8*100)/count_vulnibm_iot_requireduserinteraction)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_requireduserinteraction_risklevel7*100)/count_vulnibm_iot_requireduserinteraction)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_requireduserinteraction_risklevel6*100)/count_vulnibm_iot_requireduserinteraction)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_requireduserinteraction_risklevel5*100)/count_vulnibm_iot_requireduserinteraction)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_requireduserinteraction_risklevel4*100)/count_vulnibm_iot_requireduserinteraction)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_requireduserinteraction_risklevel3*100)/count_vulnibm_iot_requireduserinteraction)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_requireduserinteraction_risklevel2*100)/count_vulnibm_iot_requireduserinteraction)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_requireduserinteraction_risklevel1*100)/count_vulnibm_iot_requireduserinteraction)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_requireduserinteraction_risklevel0*100)/count_vulnibm_iot_requireduserinteraction)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("            -    EL VALOR MEDIO DE PUNTUACION BASE ES  "+str(float(((count_vulnibm_iot_requireduserinteraction_risklevel)/count_vulnibm_iot_requireduserinteraction)))+"\n")
print("\n")
print("      -    EN EL  "+str(float(((count_vulnibm_iot_nonerequireduserinteraction*100)/count_vulnibm_iot_user_interaction)))+" % DE VULNERABILIDADES LA INTERACCION DE USUARIO NO SE REQUIERE, LAS ESTADÍSTICAS DE PUNTUACION BASE SON LAS SIGUIENTES :  \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_nonerequireduserinteraction_risklevel10*100)/count_vulnibm_iot_nonerequireduserinteraction)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_nonerequireduserinteraction_risklevel9*100)/count_vulnibm_iot_nonerequireduserinteraction)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_nonerequireduserinteraction_risklevel8*100)/count_vulnibm_iot_nonerequireduserinteraction)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_nonerequireduserinteraction_risklevel7*100)/count_vulnibm_iot_nonerequireduserinteraction)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_nonerequireduserinteraction_risklevel6*100)/count_vulnibm_iot_nonerequireduserinteraction)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_nonerequireduserinteraction_risklevel5*100)/count_vulnibm_iot_nonerequireduserinteraction)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_nonerequireduserinteraction_risklevel4*100)/count_vulnibm_iot_nonerequireduserinteraction)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_nonerequireduserinteraction_risklevel3*100)/count_vulnibm_iot_nonerequireduserinteraction)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_nonerequireduserinteraction_risklevel2*100)/count_vulnibm_iot_nonerequireduserinteraction)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_nonerequireduserinteraction_risklevel1*100)/count_vulnibm_iot_nonerequireduserinteraction)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_nonerequireduserinteraction_risklevel0*100)/count_vulnibm_iot_nonerequireduserinteraction)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("            -    EL VALOR MEDIO DE PUNTUACION BASE ES  "+str(float(((count_vulnibm_iot_nonerequireduserinteraction_risklevel)/count_vulnibm_iot_nonerequireduserinteraction)))+"\n")
print("\n")






#Abro los ficheros con los que voy a tratar




df_vulnibm_sh = pd.read_excel('vulnerabilidades_ibm_smart_home_2023.xlsx')

count_vulnibm_sh_user_interaction=0

count_vulnibm_sh_requireduserinteraction=0
count_vulnibm_sh_requireduserinteraction_risklevel=0
count_vulnibm_sh_requireduserinteraction_risklevel10=0
count_vulnibm_sh_requireduserinteraction_risklevel9=0
count_vulnibm_sh_requireduserinteraction_risklevel8=0
count_vulnibm_sh_requireduserinteraction_risklevel7=0
count_vulnibm_sh_requireduserinteraction_risklevel6=0
count_vulnibm_sh_requireduserinteraction_risklevel5=0
count_vulnibm_sh_requireduserinteraction_risklevel4=0
count_vulnibm_sh_requireduserinteraction_risklevel3=0
count_vulnibm_sh_requireduserinteraction_risklevel2=0
count_vulnibm_sh_requireduserinteraction_risklevel1=0
count_vulnibm_sh_requireduserinteraction_risklevel0=0



count_vulnibm_sh_nonerequireduserinteraction=0
count_vulnibm_sh_nonerequireduserinteraction_risklevel=0
count_vulnibm_sh_nonerequireduserinteraction_risklevel10=0
count_vulnibm_sh_nonerequireduserinteraction_risklevel9=0
count_vulnibm_sh_nonerequireduserinteraction_risklevel8=0
count_vulnibm_sh_nonerequireduserinteraction_risklevel7=0
count_vulnibm_sh_nonerequireduserinteraction_risklevel6=0
count_vulnibm_sh_nonerequireduserinteraction_risklevel5=0
count_vulnibm_sh_nonerequireduserinteraction_risklevel4=0
count_vulnibm_sh_nonerequireduserinteraction_risklevel3=0
count_vulnibm_sh_nonerequireduserinteraction_risklevel2=0
count_vulnibm_sh_nonerequireduserinteraction_risklevel1=0
count_vulnibm_sh_nonerequireduserinteraction_risklevel0=0



#Comprobamos el contenido de INTERACCION DE USUARIO
for r in range(0,len(df_vulnibm_sh["x_xfe_cvss_userinteraction"])):                       
    count_vulnibm_sh_user_interaction+=1
    if( (isinstance(df_vulnibm_sh["x_xfe_cvss_userinteraction"][r],str)) and ('Required' in df_vulnibm_sh["x_xfe_cvss_userinteraction"][r])):
        count_vulnibm_sh_requireduserinteraction+=1
        count_vulnibm_sh_requireduserinteraction_risklevel+=float(df_vulnibm_sh["x_xfe_risk_level"][r])
        if(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 10.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=9.0)):
            count_vulnibm_sh_requireduserinteraction_risklevel9+=1
        elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 9.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=8.0)):
            count_vulnibm_sh_requireduserinteraction_risklevel8+=1
        elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 8.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=7.0)):
            count_vulnibm_sh_requireduserinteraction_risklevel7+=1
        elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 7.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=6.0)):
            count_vulnibm_sh_requireduserinteraction_risklevel6+=1
        elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 6.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=5.0)):
            count_vulnibm_sh_requireduserinteraction_risklevel5+=1
        elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 5.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=4.0)):
            count_vulnibm_sh_requireduserinteraction_risklevel4+=1
        elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 4.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=3.0)):
            count_vulnibm_sh_requireduserinteraction_risklevel3+=1
        elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 3.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=2.0)):
            count_vulnibm_sh_requireduserinteraction_risklevel2+=1
        elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 2.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=1.0)):
            count_vulnibm_sh_requireduserinteraction_risklevel1+=1
        elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 1.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=0.0)):
            count_vulnibm_sh_requireduserinteraction_risklevel0+=1
        elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) == 10.0)):
            count_vulnibm_sh_requireduserinteraction_risklevel10+=1

    else:

        count_vulnibm_sh_nonerequireduserinteraction+=1
        count_vulnibm_sh_nonerequireduserinteraction_risklevel+=float(df_vulnibm_sh["x_xfe_risk_level"][r])
        if(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 10.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=9.0)):
            count_vulnibm_sh_nonerequireduserinteraction_risklevel9+=1
        elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 9.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=8.0)):
            count_vulnibm_sh_nonerequireduserinteraction_risklevel8+=1
        elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 8.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=7.0)):
            count_vulnibm_sh_nonerequireduserinteraction_risklevel7+=1
        elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 7.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=6.0)):
            count_vulnibm_sh_nonerequireduserinteraction_risklevel6+=1
        elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 6.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=5.0)):
            count_vulnibm_sh_nonerequireduserinteraction_risklevel5+=1
        elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 5.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=4.0)):
            count_vulnibm_sh_nonerequireduserinteraction_risklevel4+=1
        elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 4.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=3.0)):
            count_vulnibm_sh_nonerequireduserinteraction_risklevel3+=1
        elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 3.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=2.0)):
            count_vulnibm_sh_nonerequireduserinteraction_risklevel2+=1
        elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 2.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=1.0)):
            count_vulnibm_sh_nonerequireduserinteraction_risklevel1+=1
        elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 1.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=0.0)):
            count_vulnibm_sh_nonerequireduserinteraction_risklevel0+=1
        elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) == 10.0)):
            count_vulnibm_sh_nonerequireduserinteraction_risklevel10+=1






                
print("********************************ESTADÍSTICAS INTERACCION DE USUARIO/PUNTUACION BASE VULNERABILIDADES IBM PARTE SMART HOME********************************")
print("\n")                            
print("\n")
print(" DE UN TOTAL DE "+str(count_vulnibm_sh_user_interaction)+" VULNERABILIDADES:\n") 
print("\n")
print("   - LAS ESTADISTICAS DE VALORES DE INTERACCION DE USUARIO SON LAS SIGUIENTES:  \n")
print("      -    EN  "+str(count_vulnibm_sh_requireduserinteraction)+" VULNERABILIDADES LA INTERACCION DE USUARIO ES REQUERIDA, LAS ESTADÍSTICAS DE PUNTUACION BASE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_sh_requireduserinteraction_risklevel10)+" VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
print("            -    EN  "+str(count_vulnibm_sh_requireduserinteraction_risklevel9)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN  "+str(count_vulnibm_sh_requireduserinteraction_risklevel8)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN  "+str(count_vulnibm_sh_requireduserinteraction_risklevel7)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN  "+str(count_vulnibm_sh_requireduserinteraction_risklevel6)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN "+str(count_vulnibm_sh_requireduserinteraction_risklevel5)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN "+str(count_vulnibm_sh_requireduserinteraction_risklevel4)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN "+str(count_vulnibm_sh_requireduserinteraction_risklevel3)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN "+str(count_vulnibm_sh_requireduserinteraction_risklevel2)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN "+str(count_vulnibm_sh_requireduserinteraction_risklevel1)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN "+str(count_vulnibm_sh_requireduserinteraction_risklevel0)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_sh_nonerequireduserinteraction)+" VULNERABILIDADES LA INTERACCION DE USUARIO NO SE REQUIERE, LAS ESTADÍSTICAS DE PUNTUACION BASE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_sh_nonerequireduserinteraction_risklevel10)+" VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
print("            -    EN  "+str(count_vulnibm_sh_nonerequireduserinteraction_risklevel9)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN  "+str(count_vulnibm_sh_nonerequireduserinteraction_risklevel8)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN  "+str(count_vulnibm_sh_nonerequireduserinteraction_risklevel7)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN  "+str(count_vulnibm_sh_nonerequireduserinteraction_risklevel6)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN "+str(count_vulnibm_sh_nonerequireduserinteraction_risklevel5)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN "+str(count_vulnibm_sh_nonerequireduserinteraction_risklevel4)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN "+str(count_vulnibm_sh_nonerequireduserinteraction_risklevel3)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN "+str(count_vulnibm_sh_nonerequireduserinteraction_risklevel2)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN "+str(count_vulnibm_sh_nonerequireduserinteraction_risklevel1)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN "+str(count_vulnibm_sh_nonerequireduserinteraction_risklevel0)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("\n")




print("********************************PORCENTAJE INTERACCION DE USUARIO/PUNTUACION BASE VULNERABILIDADES IBM PARTE SMART HOME********************************")
print("\n")                            
print("\n")
print(" DE UN TOTAL DE "+str(count_vulnibm_sh_user_interaction)+" VULNERABILIDADES :\n") 
print("\n")
print("   - LOS PORCENTAJES DE VALORES DE INTERACCION DE USUARIO SON LOS SIGUIENTES:  \n")
print("      -    EN EL  "+str(float(((count_vulnibm_sh_requireduserinteraction*100)/count_vulnibm_sh_user_interaction)))+" % DE VULNERABILIDADES LA INTERACCION DE USUARIO ES REQUERIDA, LAS ESTADÍSTICAS DE PUNTUACION BASE SON LAS SIGUIENTES :  \n")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_requireduserinteraction_risklevel10*100)/count_vulnibm_sh_requireduserinteraction)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_requireduserinteraction_risklevel9*100)/count_vulnibm_sh_requireduserinteraction)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_requireduserinteraction_risklevel8*100)/count_vulnibm_sh_requireduserinteraction)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_requireduserinteraction_risklevel7*100)/count_vulnibm_sh_requireduserinteraction)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_requireduserinteraction_risklevel6*100)/count_vulnibm_sh_requireduserinteraction)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN EL "+str(float(((count_vulnibm_sh_requireduserinteraction_risklevel5*100)/count_vulnibm_sh_requireduserinteraction)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN EL "+str(float(((count_vulnibm_sh_requireduserinteraction_risklevel4*100)/count_vulnibm_sh_requireduserinteraction)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN EL "+str(float(((count_vulnibm_sh_requireduserinteraction_risklevel3*100)/count_vulnibm_sh_requireduserinteraction)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN EL "+str(float(((count_vulnibm_sh_requireduserinteraction_risklevel2*100)/count_vulnibm_sh_requireduserinteraction)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN EL "+str(float(((count_vulnibm_sh_requireduserinteraction_risklevel1*100)/count_vulnibm_sh_requireduserinteraction)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN EL "+str(float(((count_vulnibm_sh_requireduserinteraction_risklevel0*100)/count_vulnibm_sh_requireduserinteraction)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("            -    EL VALOR MEDIO DE PUNTUACION BASE ES  "+str(float(((count_vulnibm_sh_requireduserinteraction_risklevel)/count_vulnibm_sh_requireduserinteraction)))+"\n")
print("\n")
print("      -    EN EL  "+str(float(((count_vulnibm_sh_nonerequireduserinteraction*100)/count_vulnibm_sh_user_interaction)))+" % DE VULNERABILIDADES LA INTERACCION DE USUARIO NO SE REQUIERE, LAS ESTADÍSTICAS DE PUNTUACION BASE SON LAS SIGUIENTES :  \n")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_nonerequireduserinteraction_risklevel10*100)/count_vulnibm_sh_nonerequireduserinteraction)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_nonerequireduserinteraction_risklevel9*100)/count_vulnibm_sh_nonerequireduserinteraction)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_nonerequireduserinteraction_risklevel8*100)/count_vulnibm_sh_nonerequireduserinteraction)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_nonerequireduserinteraction_risklevel7*100)/count_vulnibm_sh_nonerequireduserinteraction)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_nonerequireduserinteraction_risklevel6*100)/count_vulnibm_sh_nonerequireduserinteraction)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN EL "+str(float(((count_vulnibm_sh_nonerequireduserinteraction_risklevel5*100)/count_vulnibm_sh_nonerequireduserinteraction)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN EL "+str(float(((count_vulnibm_sh_nonerequireduserinteraction_risklevel4*100)/count_vulnibm_sh_nonerequireduserinteraction)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN EL "+str(float(((count_vulnibm_sh_nonerequireduserinteraction_risklevel3*100)/count_vulnibm_sh_nonerequireduserinteraction)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN EL "+str(float(((count_vulnibm_sh_nonerequireduserinteraction_risklevel2*100)/count_vulnibm_sh_nonerequireduserinteraction)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN EL "+str(float(((count_vulnibm_sh_nonerequireduserinteraction_risklevel1*100)/count_vulnibm_sh_nonerequireduserinteraction)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN EL "+str(float(((count_vulnibm_sh_nonerequireduserinteraction_risklevel0*100)/count_vulnibm_sh_nonerequireduserinteraction)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("            -    EL VALOR MEDIO DE PUNTUACION BASE ES  "+str(float(((count_vulnibm_sh_nonerequireduserinteraction_risklevel)/count_vulnibm_sh_nonerequireduserinteraction)))+"\n")
print("\n")

print("********************************ESTADÍSTICAS INTERACCION DE USUARIO/PUNTUACION BASE VULNERABILIDADES IBM PARTE IOT Y SMART HOME CONJUNTAS********************************")
print("\n")                            
print("\n")
print(" DE UN TOTAL DE "+str(count_vulnibm_iot_user_interaction+count_vulnibm_sh_user_interaction)+" VULNERABILIDADES:\n") 
print("\n")
print("   - LAS ESTADISTICAS DE VALORES DE INTERACCION DE USUARIO SON LAS SIGUIENTES:  \n")
print("      -    EN  "+str(count_vulnibm_iot_requireduserinteraction+count_vulnibm_sh_requireduserinteraction)+" VULNERABILIDADES LA INTERACCION DE USUARIO ES REQUERIDA, LAS ESTADÍSTICAS DE PUNTUACION BASE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_requireduserinteraction_risklevel10+count_vulnibm_sh_requireduserinteraction_risklevel10)+" VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
print("            -    EN  "+str(count_vulnibm_iot_requireduserinteraction_risklevel9+count_vulnibm_sh_requireduserinteraction_risklevel9)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN  "+str(count_vulnibm_iot_requireduserinteraction_risklevel8+count_vulnibm_sh_requireduserinteraction_risklevel8)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN  "+str(count_vulnibm_iot_requireduserinteraction_risklevel7+count_vulnibm_sh_requireduserinteraction_risklevel7)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN  "+str(count_vulnibm_iot_requireduserinteraction_risklevel6+count_vulnibm_sh_requireduserinteraction_risklevel6)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN "+str(count_vulnibm_iot_requireduserinteraction_risklevel5+count_vulnibm_sh_requireduserinteraction_risklevel5)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN "+str(count_vulnibm_iot_requireduserinteraction_risklevel4+count_vulnibm_sh_requireduserinteraction_risklevel4)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN "+str(count_vulnibm_iot_requireduserinteraction_risklevel3+count_vulnibm_sh_requireduserinteraction_risklevel3)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN "+str(count_vulnibm_iot_requireduserinteraction_risklevel2+count_vulnibm_sh_requireduserinteraction_risklevel2)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN "+str(count_vulnibm_iot_requireduserinteraction_risklevel1+count_vulnibm_sh_requireduserinteraction_risklevel1)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN "+str(count_vulnibm_iot_requireduserinteraction_risklevel0+count_vulnibm_sh_requireduserinteraction_risklevel0)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_nonerequireduserinteraction+count_vulnibm_sh_nonerequireduserinteraction)+" VULNERABILIDADES LA INTERACCION DE USUARIO NO SE REQUIERE, LAS ESTADÍSTICAS DE PUNTUACION BASE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_nonerequireduserinteraction_risklevel10+count_vulnibm_sh_nonerequireduserinteraction_risklevel10)+" VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
print("            -    EN  "+str(count_vulnibm_iot_nonerequireduserinteraction_risklevel9+count_vulnibm_sh_nonerequireduserinteraction_risklevel9)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN  "+str(count_vulnibm_iot_nonerequireduserinteraction_risklevel8+count_vulnibm_sh_nonerequireduserinteraction_risklevel8)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN  "+str(count_vulnibm_iot_nonerequireduserinteraction_risklevel7+count_vulnibm_sh_nonerequireduserinteraction_risklevel7)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN  "+str(count_vulnibm_iot_nonerequireduserinteraction_risklevel6+count_vulnibm_sh_nonerequireduserinteraction_risklevel6)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN "+str(count_vulnibm_iot_nonerequireduserinteraction_risklevel5+count_vulnibm_sh_nonerequireduserinteraction_risklevel5)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN "+str(count_vulnibm_iot_nonerequireduserinteraction_risklevel4+count_vulnibm_sh_nonerequireduserinteraction_risklevel4)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN "+str(count_vulnibm_iot_nonerequireduserinteraction_risklevel3+count_vulnibm_sh_nonerequireduserinteraction_risklevel3)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN "+str(count_vulnibm_iot_nonerequireduserinteraction_risklevel2+count_vulnibm_sh_nonerequireduserinteraction_risklevel2)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN "+str(count_vulnibm_iot_nonerequireduserinteraction_risklevel1+count_vulnibm_sh_nonerequireduserinteraction_risklevel1)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN "+str(count_vulnibm_iot_nonerequireduserinteraction_risklevel0+count_vulnibm_sh_nonerequireduserinteraction_risklevel0)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("\n")

print("********************************PORCENTAJES INTERACCION DE USUARIO/PUNTUACION BASE VULNERABILIDADES IBM PARTE IOT Y SMART HOME CONJUNTAS********************************")
print("\n")                            
print("\n")
print(" DE UN TOTAL DE "+str(count_vulnibm_iot_user_interaction+count_vulnibm_sh_user_interaction)+" VULNERABILIDADES :\n") 
print("\n")
print("   - LOS PORCENTAJES DE VALORES DE INTERACCION DE USUARIO SON LOS SIGUIENTES:  \n")
print("      -    EN EL "+str(float((((count_vulnibm_iot_requireduserinteraction+count_vulnibm_sh_requireduserinteraction)*100)/(count_vulnibm_iot_user_interaction+count_vulnibm_sh_user_interaction))))+" % DE VULNERABILIDADES LA INTERACCION DE USUARIO ES REQUERIDA, LOS PORCENTAJES DE PUNTUACION BASE SON LOS SIGUIENTES :  \n")
print("            -    EN EL"+str(float((((count_vulnibm_iot_requireduserinteraction_risklevel10+count_vulnibm_sh_requireduserinteraction_risklevel10)*100)/(count_vulnibm_iot_requireduserinteraction+count_vulnibm_sh_requireduserinteraction))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_requireduserinteraction_risklevel9+count_vulnibm_sh_requireduserinteraction_risklevel9)*100)/(count_vulnibm_iot_requireduserinteraction+count_vulnibm_sh_requireduserinteraction))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_requireduserinteraction_risklevel8+count_vulnibm_sh_requireduserinteraction_risklevel8)*100)/(count_vulnibm_iot_requireduserinteraction+count_vulnibm_sh_requireduserinteraction))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_requireduserinteraction_risklevel7+count_vulnibm_sh_requireduserinteraction_risklevel7)*100)/(count_vulnibm_iot_requireduserinteraction+count_vulnibm_sh_requireduserinteraction))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_requireduserinteraction_risklevel6+count_vulnibm_sh_requireduserinteraction_risklevel6)*100)/(count_vulnibm_iot_requireduserinteraction+count_vulnibm_sh_requireduserinteraction))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_requireduserinteraction_risklevel5+count_vulnibm_sh_requireduserinteraction_risklevel5)*100)/(count_vulnibm_iot_requireduserinteraction+count_vulnibm_sh_requireduserinteraction))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_requireduserinteraction_risklevel4+count_vulnibm_sh_requireduserinteraction_risklevel4)*100)/(count_vulnibm_iot_requireduserinteraction+count_vulnibm_sh_requireduserinteraction))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_requireduserinteraction_risklevel3+count_vulnibm_sh_requireduserinteraction_risklevel3)*100)/(count_vulnibm_iot_requireduserinteraction+count_vulnibm_sh_requireduserinteraction))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_requireduserinteraction_risklevel2+count_vulnibm_sh_requireduserinteraction_risklevel2)*100)/(count_vulnibm_iot_requireduserinteraction+count_vulnibm_sh_requireduserinteraction))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_requireduserinteraction_risklevel1+count_vulnibm_sh_requireduserinteraction_risklevel1)*100)/(count_vulnibm_iot_requireduserinteraction+count_vulnibm_sh_requireduserinteraction))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_requireduserinteraction_risklevel0+count_vulnibm_sh_requireduserinteraction_risklevel0)*100)/(count_vulnibm_iot_requireduserinteraction+count_vulnibm_sh_requireduserinteraction))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("            -    EL VALOR MEDIO DE PUNTUACION BASE ES  "+str(float(((count_vulnibm_iot_requireduserinteraction_risklevel+count_vulnibm_sh_requireduserinteraction_risklevel)/(count_vulnibm_iot_requireduserinteraction+count_vulnibm_sh_requireduserinteraction))))+"\n")
print("\n")
print("      -    EN EL "+str(float((((count_vulnibm_iot_nonerequireduserinteraction+count_vulnibm_sh_nonerequireduserinteraction)*100)/(count_vulnibm_iot_user_interaction+count_vulnibm_sh_user_interaction))))+" % DE VULNERABILIDADES LA INTERACCION DE USUARIO NO SE REQUIERE, LOS PORCENTAJES DE PUNTUACION BASE SON LOS SIGUIENTES :  \n")
print("            -    EN EL"+str(float((((count_vulnibm_iot_nonerequireduserinteraction_risklevel10+count_vulnibm_sh_nonerequireduserinteraction_risklevel10)*100)/(count_vulnibm_iot_nonerequireduserinteraction+count_vulnibm_sh_nonerequireduserinteraction))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_nonerequireduserinteraction_risklevel9+count_vulnibm_sh_nonerequireduserinteraction_risklevel9)*100)/(count_vulnibm_iot_nonerequireduserinteraction+count_vulnibm_sh_nonerequireduserinteraction))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_nonerequireduserinteraction_risklevel8+count_vulnibm_sh_nonerequireduserinteraction_risklevel8)*100)/(count_vulnibm_iot_nonerequireduserinteraction+count_vulnibm_sh_nonerequireduserinteraction))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_nonerequireduserinteraction_risklevel7+count_vulnibm_sh_nonerequireduserinteraction_risklevel7)*100)/(count_vulnibm_iot_nonerequireduserinteraction+count_vulnibm_sh_nonerequireduserinteraction))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_nonerequireduserinteraction_risklevel6+count_vulnibm_sh_nonerequireduserinteraction_risklevel6)*100)/(count_vulnibm_iot_nonerequireduserinteraction+count_vulnibm_sh_nonerequireduserinteraction))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_nonerequireduserinteraction_risklevel5+count_vulnibm_sh_nonerequireduserinteraction_risklevel5)*100)/(count_vulnibm_iot_nonerequireduserinteraction+count_vulnibm_sh_nonerequireduserinteraction))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_nonerequireduserinteraction_risklevel4+count_vulnibm_sh_nonerequireduserinteraction_risklevel4)*100)/(count_vulnibm_iot_nonerequireduserinteraction+count_vulnibm_sh_nonerequireduserinteraction))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_nonerequireduserinteraction_risklevel3+count_vulnibm_sh_nonerequireduserinteraction_risklevel3)*100)/(count_vulnibm_iot_nonerequireduserinteraction+count_vulnibm_sh_nonerequireduserinteraction))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_nonerequireduserinteraction_risklevel2+count_vulnibm_sh_nonerequireduserinteraction_risklevel2)*100)/(count_vulnibm_iot_nonerequireduserinteraction+count_vulnibm_sh_nonerequireduserinteraction))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_nonerequireduserinteraction_risklevel1+count_vulnibm_sh_nonerequireduserinteraction_risklevel1)*100)/(count_vulnibm_iot_nonerequireduserinteraction+count_vulnibm_sh_nonerequireduserinteraction))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_nonerequireduserinteraction_risklevel0+count_vulnibm_sh_nonerequireduserinteraction_risklevel0)*100)/(count_vulnibm_iot_nonerequireduserinteraction+count_vulnibm_sh_nonerequireduserinteraction))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("            -    EL VALOR MEDIO DE PUNTUACION BASE ES  "+str(float(((count_vulnibm_iot_nonerequireduserinteraction_risklevel+count_vulnibm_sh_nonerequireduserinteraction_risklevel)/(count_vulnibm_iot_nonerequireduserinteraction+count_vulnibm_sh_nonerequireduserinteraction))))+"\n")
print("\n")






























