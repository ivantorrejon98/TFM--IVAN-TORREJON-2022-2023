

import pandas as pd
from datetime import datetime,timedelta



#Abro los ficheros con los que voy a tratar




df_vulnibm_iot = pd.read_excel('vulnerabilidades_ibm_iot_2023.xlsx')

count_vulnibm_iot_scope=0

count_vulnibm_iot_changedscope=0
count_vulnibm_iot_changedscope_risklevel=0
count_vulnibm_iot_changedscope_risklevel10=0
count_vulnibm_iot_changedscope_risklevel9=0
count_vulnibm_iot_changedscope_risklevel8=0
count_vulnibm_iot_changedscope_risklevel7=0
count_vulnibm_iot_changedscope_risklevel6=0
count_vulnibm_iot_changedscope_risklevel5=0
count_vulnibm_iot_changedscope_risklevel4=0
count_vulnibm_iot_changedscope_risklevel3=0
count_vulnibm_iot_changedscope_risklevel2=0
count_vulnibm_iot_changedscope_risklevel1=0
count_vulnibm_iot_changedscope_risklevel0=0



count_vulnibm_iot_unchangedscope=0
count_vulnibm_iot_unchangedscope_risklevel=0
count_vulnibm_iot_unchangedscope_risklevel10=0
count_vulnibm_iot_unchangedscope_risklevel9=0
count_vulnibm_iot_unchangedscope_risklevel8=0
count_vulnibm_iot_unchangedscope_risklevel7=0
count_vulnibm_iot_unchangedscope_risklevel6=0
count_vulnibm_iot_unchangedscope_risklevel5=0
count_vulnibm_iot_unchangedscope_risklevel4=0
count_vulnibm_iot_unchangedscope_risklevel3=0
count_vulnibm_iot_unchangedscope_risklevel2=0
count_vulnibm_iot_unchangedscope_risklevel1=0
count_vulnibm_iot_unchangedscope_risklevel0=0




#Comprobamos el contenido de SCOPE
for r in range(0,len(df_vulnibm_iot["x_xfe_cvss_scope"])):  
    count_vulnibm_iot_scope+=1
    if( (isinstance(df_vulnibm_iot["x_xfe_cvss_scope"][r],str)) and ('Changed' in df_vulnibm_iot["x_xfe_cvss_scope"][r])):
        count_vulnibm_iot_changedscope+=1
        count_vulnibm_iot_changedscope_risklevel+=float(df_vulnibm_iot["x_xfe_risk_level"][r])
        if(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 10.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=9.0)):
            count_vulnibm_iot_changedscope_risklevel9+=1
        elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 9.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=8.0)):
            count_vulnibm_iot_changedscope_risklevel8+=1
        elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 8.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=7.0)):
            count_vulnibm_iot_changedscope_risklevel7+=1
        elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 7.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=6.0)):
            count_vulnibm_iot_changedscope_risklevel6+=1
        elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 6.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=5.0)):
            count_vulnibm_iot_changedscope_risklevel5+=1
        elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 5.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=4.0)):
            count_vulnibm_iot_changedscope_risklevel4+=1
        elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 4.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=3.0)):
            count_vulnibm_iot_changedscope_risklevel3+=1
        elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 3.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=2.0)):
            count_vulnibm_iot_changedscope_risklevel2+=1
        elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 2.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=1.0)):
            count_vulnibm_iot_changedscope_risklevel1+=1
        elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 1.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=0.0)):
            count_vulnibm_iot_changedscope_risklevel0+=1
        elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) == 10.0)):
            count_vulnibm_iot_changedscope_risklevel10+=1

    elif( (isinstance(df_vulnibm_iot["x_xfe_cvss_scope"][r],str)) and ('Unchanged' in df_vulnibm_iot["x_xfe_cvss_scope"][r])):

        count_vulnibm_iot_unchangedscope+=1
        count_vulnibm_iot_unchangedscope_risklevel+=float(df_vulnibm_iot["x_xfe_risk_level"][r])
        if(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 10.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=9.0)):
            count_vulnibm_iot_unchangedscope_risklevel9+=1
        elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 9.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=8.0)):
            count_vulnibm_iot_unchangedscope_risklevel8+=1
        elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 8.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=7.0)):
            count_vulnibm_iot_unchangedscope_risklevel7+=1
        elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 7.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=6.0)):
            count_vulnibm_iot_unchangedscope_risklevel6+=1
        elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 6.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=5.0)):
            count_vulnibm_iot_unchangedscope_risklevel5+=1
        elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 5.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=4.0)):
            count_vulnibm_iot_unchangedscope_risklevel4+=1
        elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 4.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=3.0)):
            count_vulnibm_iot_unchangedscope_risklevel3+=1
        elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 3.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=2.0)):
            count_vulnibm_iot_unchangedscope_risklevel2+=1
        elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 2.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=1.0)):
            count_vulnibm_iot_unchangedscope_risklevel1+=1
        elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 1.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=0.0)):
            count_vulnibm_iot_unchangedscope_risklevel0+=1
        elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) == 10.0)):
            count_vulnibm_iot_unchangedscope_risklevel10+=1
            
            
        
        
                
                
                
                
print("***************************ESTADÍSTICAS ALCANCE/PUNTUACION BASE VULNERABILIDADES IBM PARTE IOT***************************")
print("\n")                            
print("\n")
print(" DE UN TOTAL DE "+str(count_vulnibm_iot_scope)+" VULNERABILIDADES:\n") 
print("\n")
print("   - LAS ESTADISTICAS DE VALORES DE SCOPE SON LAS SIGUIENTES:  \n")
print("      -    EN  "+str(count_vulnibm_iot_changedscope)+" VULNERABILIDADES EL ALCANCE ES CAMBIADO, LAS ESTADÍSTICAS DE PUNTUACIÓN BASE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_changedscope_risklevel10)+" VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
print("            -    EN  "+str(count_vulnibm_iot_changedscope_risklevel9)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN  "+str(count_vulnibm_iot_changedscope_risklevel8)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN  "+str(count_vulnibm_iot_changedscope_risklevel7)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN  "+str(count_vulnibm_iot_changedscope_risklevel6)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN "+str(count_vulnibm_iot_changedscope_risklevel5)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN "+str(count_vulnibm_iot_changedscope_risklevel4)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN "+str(count_vulnibm_iot_changedscope_risklevel3)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN "+str(count_vulnibm_iot_changedscope_risklevel2)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN "+str(count_vulnibm_iot_changedscope_risklevel1)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN "+str(count_vulnibm_iot_changedscope_risklevel0)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_unchangedscope)+" VULNERABILIDADES EL ALCANCE ES NO CAMBIADO, LAS ESTADÍSTICAS DE PUNTUACIÓN BASE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_unchangedscope_risklevel10)+" VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
print("            -    EN  "+str(count_vulnibm_iot_unchangedscope_risklevel9)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN  "+str(count_vulnibm_iot_unchangedscope_risklevel8)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN  "+str(count_vulnibm_iot_unchangedscope_risklevel7)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN  "+str(count_vulnibm_iot_unchangedscope_risklevel6)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN "+str(count_vulnibm_iot_unchangedscope_risklevel5)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN "+str(count_vulnibm_iot_unchangedscope_risklevel4)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN "+str(count_vulnibm_iot_unchangedscope_risklevel3)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN "+str(count_vulnibm_iot_unchangedscope_risklevel2)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN "+str(count_vulnibm_iot_unchangedscope_risklevel1)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN "+str(count_vulnibm_iot_unchangedscope_risklevel0)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("\n")




print("***************************PORCENTAJE ALCANCE/PUNTUACION BASE VULNERABILIDADES IBM PARTE IOT***************************")
print("\n")                            
print("\n")
print(" DE UN TOTAL DE "+str(count_vulnibm_iot_scope)+" VULNERABILIDADES :\n") 
print("\n")
print("   - LOS PORCENTAJES DE VALORES DE SCOPE SON LOS SIGUIENTES:  \n")
print("      -    EN EL  "+str(float(((count_vulnibm_iot_changedscope*100)/count_vulnibm_iot_scope)))+" % DE VULNERABILIDADES EL ALCANCE ES CAMBIADO, LAS ESTADÍSTICAS DE PUNTUACIÓN BASE SON LAS SIGUIENTES :  \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_changedscope_risklevel10*100)/count_vulnibm_iot_changedscope)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_changedscope_risklevel9*100)/count_vulnibm_iot_changedscope)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_changedscope_risklevel8*100)/count_vulnibm_iot_changedscope)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_changedscope_risklevel7*100)/count_vulnibm_iot_changedscope)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_changedscope_risklevel6*100)/count_vulnibm_iot_changedscope)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_changedscope_risklevel5*100)/count_vulnibm_iot_changedscope)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_changedscope_risklevel4*100)/count_vulnibm_iot_changedscope)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_changedscope_risklevel3*100)/count_vulnibm_iot_changedscope)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_changedscope_risklevel2*100)/count_vulnibm_iot_changedscope)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_changedscope_risklevel1*100)/count_vulnibm_iot_changedscope)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_changedscope_risklevel0*100)/count_vulnibm_iot_changedscope)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("            -    EL VALOR MEDIO DE PUNTUACION BASE ES  "+str(float(((count_vulnibm_iot_changedscope_risklevel)/count_vulnibm_iot_changedscope)))+"\n")
print("\n")
print("      -    EN EL  "+str(float(((count_vulnibm_iot_unchangedscope*100)/count_vulnibm_iot_scope)))+" % DE VULNERABILIDADES EL ALCANCE ES NO CAMBIADO, LAS ESTADÍSTICAS DE PUNTUACIÓN BASE SON LAS SIGUIENTES :  \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_unchangedscope_risklevel10*100)/count_vulnibm_iot_unchangedscope)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_unchangedscope_risklevel9*100)/count_vulnibm_iot_unchangedscope)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_unchangedscope_risklevel8*100)/count_vulnibm_iot_unchangedscope)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_unchangedscope_risklevel7*100)/count_vulnibm_iot_unchangedscope)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_unchangedscope_risklevel6*100)/count_vulnibm_iot_unchangedscope)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_unchangedscope_risklevel5*100)/count_vulnibm_iot_unchangedscope)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_unchangedscope_risklevel4*100)/count_vulnibm_iot_unchangedscope)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_unchangedscope_risklevel3*100)/count_vulnibm_iot_unchangedscope)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_unchangedscope_risklevel2*100)/count_vulnibm_iot_unchangedscope)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_unchangedscope_risklevel1*100)/count_vulnibm_iot_unchangedscope)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_unchangedscope_risklevel0*100)/count_vulnibm_iot_unchangedscope)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("            -    EL VALOR MEDIO DE PUNTUACION BASE ES  "+str(float(((count_vulnibm_iot_unchangedscope_risklevel)/count_vulnibm_iot_unchangedscope)))+"\n")
print("\n")






#Abro los ficheros con los que voy a tratar




df_vulnibm_sh = pd.read_excel('vulnerabilidades_ibm_smart_home_2023.xlsx')

count_vulnibm_sh_scope=0

count_vulnibm_sh_changedscope=0
count_vulnibm_sh_changedscope_risklevel=0
count_vulnibm_sh_changedscope_risklevel10=0
count_vulnibm_sh_changedscope_risklevel9=0
count_vulnibm_sh_changedscope_risklevel8=0
count_vulnibm_sh_changedscope_risklevel7=0
count_vulnibm_sh_changedscope_risklevel6=0
count_vulnibm_sh_changedscope_risklevel5=0
count_vulnibm_sh_changedscope_risklevel4=0
count_vulnibm_sh_changedscope_risklevel3=0
count_vulnibm_sh_changedscope_risklevel2=0
count_vulnibm_sh_changedscope_risklevel1=0
count_vulnibm_sh_changedscope_risklevel0=0



count_vulnibm_sh_unchangedscope=0
count_vulnibm_sh_unchangedscope_risklevel=0
count_vulnibm_sh_unchangedscope_risklevel10=0
count_vulnibm_sh_unchangedscope_risklevel9=0
count_vulnibm_sh_unchangedscope_risklevel8=0
count_vulnibm_sh_unchangedscope_risklevel7=0
count_vulnibm_sh_unchangedscope_risklevel6=0
count_vulnibm_sh_unchangedscope_risklevel5=0
count_vulnibm_sh_unchangedscope_risklevel4=0
count_vulnibm_sh_unchangedscope_risklevel3=0
count_vulnibm_sh_unchangedscope_risklevel2=0
count_vulnibm_sh_unchangedscope_risklevel1=0
count_vulnibm_sh_unchangedscope_risklevel0=0



#Comprobamos el contenido de SCOPE
for r in range(0,len(df_vulnibm_sh["x_xfe_cvss_scope"])):                       
    count_vulnibm_sh_scope+=1
    if( (isinstance(df_vulnibm_sh["x_xfe_cvss_scope"][r],str)) and ('Changed' in df_vulnibm_sh["x_xfe_cvss_scope"][r])):
        count_vulnibm_sh_changedscope+=1
        count_vulnibm_sh_changedscope_risklevel+=float(df_vulnibm_sh["x_xfe_risk_level"][r])
        if(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 10.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=9.0)):
            count_vulnibm_sh_changedscope_risklevel9+=1
        elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 9.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=8.0)):
            count_vulnibm_sh_changedscope_risklevel8+=1
        elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 8.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=7.0)):
            count_vulnibm_sh_changedscope_risklevel7+=1
        elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 7.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=6.0)):
            count_vulnibm_sh_changedscope_risklevel6+=1
        elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 6.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=5.0)):
            count_vulnibm_sh_changedscope_risklevel5+=1
        elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 5.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=4.0)):
            count_vulnibm_sh_changedscope_risklevel4+=1
        elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 4.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=3.0)):
            count_vulnibm_sh_changedscope_risklevel3+=1
        elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 3.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=2.0)):
            count_vulnibm_sh_changedscope_risklevel2+=1
        elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 2.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=1.0)):
            count_vulnibm_sh_changedscope_risklevel1+=1
        elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 1.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=0.0)):
            count_vulnibm_sh_changedscope_risklevel0+=1
        elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) == 10.0)):
            count_vulnibm_sh_changedscope_risklevel10+=1

    elif( (isinstance(df_vulnibm_sh["x_xfe_cvss_scope"][r],str)) and ('Unchanged' in df_vulnibm_sh["x_xfe_cvss_scope"][r])):

        count_vulnibm_sh_unchangedscope+=1
        count_vulnibm_sh_unchangedscope_risklevel+=float(df_vulnibm_sh["x_xfe_risk_level"][r])
        if(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 10.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=9.0)):
            count_vulnibm_sh_unchangedscope_risklevel9+=1
        elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 9.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=8.0)):
            count_vulnibm_sh_unchangedscope_risklevel8+=1
        elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 8.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=7.0)):
            count_vulnibm_sh_unchangedscope_risklevel7+=1
        elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 7.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=6.0)):
            count_vulnibm_sh_unchangedscope_risklevel6+=1
        elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 6.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=5.0)):
            count_vulnibm_sh_unchangedscope_risklevel5+=1
        elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 5.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=4.0)):
            count_vulnibm_sh_unchangedscope_risklevel4+=1
        elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 4.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=3.0)):
            count_vulnibm_sh_unchangedscope_risklevel3+=1
        elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 3.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=2.0)):
            count_vulnibm_sh_unchangedscope_risklevel2+=1
        elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 2.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=1.0)):
            count_vulnibm_sh_unchangedscope_risklevel1+=1
        elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 1.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=0.0)):
            count_vulnibm_sh_unchangedscope_risklevel0+=1
        elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) == 10.0)):
            count_vulnibm_sh_unchangedscope_risklevel10+=1






                
print("***************************ESTADÍSTICAS ALCANCE/PUNTUACION BASE VULNERABILIDADES IBM PARTE SMART HOME***************************")
print("\n")                            
print("\n")
print(" DE UN TOTAL DE "+str(count_vulnibm_sh_scope)+" VULNERABILIDADES:\n") 
print("\n")
print("   - LAS ESTADISTICAS DE VALORES DE SCOPE SON LAS SIGUIENTES:  \n")
print("      -    EN  "+str(count_vulnibm_sh_changedscope)+" VULNERABILIDADES EL ALCANCE ES CAMBIADO, LAS ESTADÍSTICAS DE PUNTUACIÓN BASE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_sh_changedscope_risklevel10)+" VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
print("            -    EN  "+str(count_vulnibm_sh_changedscope_risklevel9)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN  "+str(count_vulnibm_sh_changedscope_risklevel8)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN  "+str(count_vulnibm_sh_changedscope_risklevel7)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN  "+str(count_vulnibm_sh_changedscope_risklevel6)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN "+str(count_vulnibm_sh_changedscope_risklevel5)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN "+str(count_vulnibm_sh_changedscope_risklevel4)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN "+str(count_vulnibm_sh_changedscope_risklevel3)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN "+str(count_vulnibm_sh_changedscope_risklevel2)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN "+str(count_vulnibm_sh_changedscope_risklevel1)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN "+str(count_vulnibm_sh_changedscope_risklevel0)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_sh_unchangedscope)+" VULNERABILIDADES EL ALCANCE ES NO CAMBIADO, LAS ESTADÍSTICAS DE PUNTUACIÓN BASE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_sh_unchangedscope_risklevel10)+" VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
print("            -    EN  "+str(count_vulnibm_sh_unchangedscope_risklevel9)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN  "+str(count_vulnibm_sh_unchangedscope_risklevel8)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN  "+str(count_vulnibm_sh_unchangedscope_risklevel7)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN  "+str(count_vulnibm_sh_unchangedscope_risklevel6)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN "+str(count_vulnibm_sh_unchangedscope_risklevel5)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN "+str(count_vulnibm_sh_unchangedscope_risklevel4)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN "+str(count_vulnibm_sh_unchangedscope_risklevel3)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN "+str(count_vulnibm_sh_unchangedscope_risklevel2)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN "+str(count_vulnibm_sh_unchangedscope_risklevel1)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN "+str(count_vulnibm_sh_unchangedscope_risklevel0)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("\n")




print("***************************PORCENTAJE ALCANCE/PUNTUACION BASE VULNERABILIDADES IBM PARTE SMART HOME***************************")
print("\n")                            
print("\n")
print(" DE UN TOTAL DE "+str(count_vulnibm_sh_scope)+" VULNERABILIDADES :\n") 
print("\n")
print("   - LOS PORCENTAJES DE VALORES DE SCOPE SON LOS SIGUIENTES:  \n")
print("      -    EN EL  "+str(float(((count_vulnibm_sh_changedscope*100)/count_vulnibm_sh_scope)))+" % DE VULNERABILIDADES EL ALCANCE ES CAMBIADO, LAS ESTADÍSTICAS DE PUNTUACIÓN BASE SON LAS SIGUIENTES :  \n")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_changedscope_risklevel10*100)/count_vulnibm_sh_changedscope)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_changedscope_risklevel9*100)/count_vulnibm_sh_changedscope)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_changedscope_risklevel8*100)/count_vulnibm_sh_changedscope)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_changedscope_risklevel7*100)/count_vulnibm_sh_changedscope)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_changedscope_risklevel6*100)/count_vulnibm_sh_changedscope)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN EL "+str(float(((count_vulnibm_sh_changedscope_risklevel5*100)/count_vulnibm_sh_changedscope)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN EL "+str(float(((count_vulnibm_sh_changedscope_risklevel4*100)/count_vulnibm_sh_changedscope)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN EL "+str(float(((count_vulnibm_sh_changedscope_risklevel3*100)/count_vulnibm_sh_changedscope)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN EL "+str(float(((count_vulnibm_sh_changedscope_risklevel2*100)/count_vulnibm_sh_changedscope)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN EL "+str(float(((count_vulnibm_sh_changedscope_risklevel1*100)/count_vulnibm_sh_changedscope)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN EL "+str(float(((count_vulnibm_sh_changedscope_risklevel0*100)/count_vulnibm_sh_changedscope)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("            -    EL VALOR MEDIO DE PUNTUACION BASE ES  "+str(float(((count_vulnibm_sh_changedscope_risklevel)/count_vulnibm_sh_changedscope)))+"\n")
print("\n")
print("      -    EN EL  "+str(float(((count_vulnibm_sh_unchangedscope*100)/count_vulnibm_sh_scope)))+" % DE VULNERABILIDADES EL ALCANCE ES NO CAMBIADO, LAS ESTADÍSTICAS DE PUNTUACIÓN BASE SON LAS SIGUIENTES :  \n")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_unchangedscope_risklevel10*100)/count_vulnibm_sh_unchangedscope)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_unchangedscope_risklevel9*100)/count_vulnibm_sh_unchangedscope)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_unchangedscope_risklevel8*100)/count_vulnibm_sh_unchangedscope)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_unchangedscope_risklevel7*100)/count_vulnibm_sh_unchangedscope)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_unchangedscope_risklevel6*100)/count_vulnibm_sh_unchangedscope)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN EL "+str(float(((count_vulnibm_sh_unchangedscope_risklevel5*100)/count_vulnibm_sh_unchangedscope)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN EL "+str(float(((count_vulnibm_sh_unchangedscope_risklevel4*100)/count_vulnibm_sh_unchangedscope)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN EL "+str(float(((count_vulnibm_sh_unchangedscope_risklevel3*100)/count_vulnibm_sh_unchangedscope)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN EL "+str(float(((count_vulnibm_sh_unchangedscope_risklevel2*100)/count_vulnibm_sh_unchangedscope)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN EL "+str(float(((count_vulnibm_sh_unchangedscope_risklevel1*100)/count_vulnibm_sh_unchangedscope)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN EL "+str(float(((count_vulnibm_sh_unchangedscope_risklevel0*100)/count_vulnibm_sh_unchangedscope)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("            -    EL VALOR MEDIO DE PUNTUACION BASE ES  "+str(float(((count_vulnibm_sh_unchangedscope_risklevel)/count_vulnibm_sh_unchangedscope)))+"\n")
print("\n")

print("***************************ESTADÍSTICAS ALCANCE/PUNTUACION BASE VULNERABILIDADES IBM PARTE IOT Y SMART HOME CONJUNTAS***************************")
print("\n")                            
print("\n")
print(" DE UN TOTAL DE "+str(count_vulnibm_iot_scope+count_vulnibm_sh_scope)+" VULNERABILIDADES:\n") 
print("\n")
print("   - LAS ESTADISTICAS DE VALORES DE SCOPE SON LAS SIGUIENTES:  \n")
print("      -    EN  "+str(count_vulnibm_iot_changedscope+count_vulnibm_sh_changedscope)+" VULNERABILIDADES EL ALCANCE ES CAMBIADO, LAS ESTADÍSTICAS DE PUNTUACIÓN BASE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_changedscope_risklevel10+count_vulnibm_sh_changedscope_risklevel10)+" VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
print("            -    EN  "+str(count_vulnibm_iot_changedscope_risklevel9+count_vulnibm_sh_changedscope_risklevel9)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN  "+str(count_vulnibm_iot_changedscope_risklevel8+count_vulnibm_sh_changedscope_risklevel8)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN  "+str(count_vulnibm_iot_changedscope_risklevel7+count_vulnibm_sh_changedscope_risklevel7)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN  "+str(count_vulnibm_iot_changedscope_risklevel6+count_vulnibm_sh_changedscope_risklevel6)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN "+str(count_vulnibm_iot_changedscope_risklevel5+count_vulnibm_sh_changedscope_risklevel5)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN "+str(count_vulnibm_iot_changedscope_risklevel4+count_vulnibm_sh_changedscope_risklevel4)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN "+str(count_vulnibm_iot_changedscope_risklevel3+count_vulnibm_sh_changedscope_risklevel3)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN "+str(count_vulnibm_iot_changedscope_risklevel2+count_vulnibm_sh_changedscope_risklevel2)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN "+str(count_vulnibm_iot_changedscope_risklevel1+count_vulnibm_sh_changedscope_risklevel1)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN "+str(count_vulnibm_iot_changedscope_risklevel0+count_vulnibm_sh_changedscope_risklevel0)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_unchangedscope+count_vulnibm_sh_unchangedscope)+" VULNERABILIDADES EL ALCANCE ES NO CAMBIADO, LAS ESTADÍSTICAS DE PUNTUACIÓN BASE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_unchangedscope_risklevel10+count_vulnibm_sh_unchangedscope_risklevel10)+" VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
print("            -    EN  "+str(count_vulnibm_iot_unchangedscope_risklevel9+count_vulnibm_sh_unchangedscope_risklevel9)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN  "+str(count_vulnibm_iot_unchangedscope_risklevel8+count_vulnibm_sh_unchangedscope_risklevel8)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN  "+str(count_vulnibm_iot_unchangedscope_risklevel7+count_vulnibm_sh_unchangedscope_risklevel7)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN  "+str(count_vulnibm_iot_unchangedscope_risklevel6+count_vulnibm_sh_unchangedscope_risklevel6)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN "+str(count_vulnibm_iot_unchangedscope_risklevel5+count_vulnibm_sh_unchangedscope_risklevel5)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN "+str(count_vulnibm_iot_unchangedscope_risklevel4+count_vulnibm_sh_unchangedscope_risklevel4)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN "+str(count_vulnibm_iot_unchangedscope_risklevel3+count_vulnibm_sh_unchangedscope_risklevel3)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN "+str(count_vulnibm_iot_unchangedscope_risklevel2+count_vulnibm_sh_unchangedscope_risklevel2)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN "+str(count_vulnibm_iot_unchangedscope_risklevel1+count_vulnibm_sh_unchangedscope_risklevel1)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN "+str(count_vulnibm_iot_unchangedscope_risklevel0+count_vulnibm_sh_unchangedscope_risklevel0)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("\n")

print("***************************PORCENTAJES ALCANCE/PUNTUACION BASE VULNERABILIDADES IBM PARTE IOT Y SMART HOME CONJUNTAS***************************")
print("\n")                            
print("\n")
print(" DE UN TOTAL DE "+str(count_vulnibm_iot_scope+count_vulnibm_sh_scope)+" VULNERABILIDADES :\n") 
print("\n")
print("   - LOS PORCENTAJES DE VALORES DE SCOPE SON LOS SIGUIENTES:  \n")
print("      -    EN EL "+str(float((((count_vulnibm_iot_changedscope+count_vulnibm_sh_changedscope)*100)/(count_vulnibm_iot_scope+count_vulnibm_sh_scope))))+" % DE VULNERABILIDADES EL ALCANCE ES CAMBIADO, LOS PORCENTAJES DE PUNTUACIÓN BASE SON LOS SIGUIENTES :  \n")
print("            -    EN EL"+str(float((((count_vulnibm_iot_changedscope_risklevel10+count_vulnibm_sh_changedscope_risklevel10)*100)/(count_vulnibm_iot_changedscope+count_vulnibm_sh_changedscope))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_changedscope_risklevel9+count_vulnibm_sh_changedscope_risklevel9)*100)/(count_vulnibm_iot_changedscope+count_vulnibm_sh_changedscope))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_changedscope_risklevel8+count_vulnibm_sh_changedscope_risklevel8)*100)/(count_vulnibm_iot_changedscope+count_vulnibm_sh_changedscope))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_changedscope_risklevel7+count_vulnibm_sh_changedscope_risklevel7)*100)/(count_vulnibm_iot_changedscope+count_vulnibm_sh_changedscope))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_changedscope_risklevel6+count_vulnibm_sh_changedscope_risklevel6)*100)/(count_vulnibm_iot_changedscope+count_vulnibm_sh_changedscope))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_changedscope_risklevel5+count_vulnibm_sh_changedscope_risklevel5)*100)/(count_vulnibm_iot_changedscope+count_vulnibm_sh_changedscope))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_changedscope_risklevel4+count_vulnibm_sh_changedscope_risklevel4)*100)/(count_vulnibm_iot_changedscope+count_vulnibm_sh_changedscope))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_changedscope_risklevel3+count_vulnibm_sh_changedscope_risklevel3)*100)/(count_vulnibm_iot_changedscope+count_vulnibm_sh_changedscope))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_changedscope_risklevel2+count_vulnibm_sh_changedscope_risklevel2)*100)/(count_vulnibm_iot_changedscope+count_vulnibm_sh_changedscope))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_changedscope_risklevel1+count_vulnibm_sh_changedscope_risklevel1)*100)/(count_vulnibm_iot_changedscope+count_vulnibm_sh_changedscope))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_changedscope_risklevel0+count_vulnibm_sh_changedscope_risklevel0)*100)/(count_vulnibm_iot_changedscope+count_vulnibm_sh_changedscope))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("            -    EL VALOR MEDIO DE PUNTUACION BASE ES  "+str(float(((count_vulnibm_iot_changedscope_risklevel+count_vulnibm_sh_changedscope_risklevel)/(count_vulnibm_iot_changedscope+count_vulnibm_sh_changedscope))))+"\n")
print("\n")
print("      -    EN EL "+str(float((((count_vulnibm_iot_unchangedscope+count_vulnibm_sh_unchangedscope)*100)/(count_vulnibm_iot_scope+count_vulnibm_sh_scope))))+" % DE VULNERABILIDADES EL ALCANCE ES NO CAMBIADO, LOS PORCENTAJES DE PUNTUACIÓN BASE SON LOS SIGUIENTES :  \n")
print("            -    EN EL"+str(float((((count_vulnibm_iot_unchangedscope_risklevel10+count_vulnibm_sh_unchangedscope_risklevel10)*100)/(count_vulnibm_iot_unchangedscope+count_vulnibm_sh_unchangedscope))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_unchangedscope_risklevel9+count_vulnibm_sh_unchangedscope_risklevel9)*100)/(count_vulnibm_iot_unchangedscope+count_vulnibm_sh_unchangedscope))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_unchangedscope_risklevel8+count_vulnibm_sh_unchangedscope_risklevel8)*100)/(count_vulnibm_iot_unchangedscope+count_vulnibm_sh_unchangedscope))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_unchangedscope_risklevel7+count_vulnibm_sh_unchangedscope_risklevel7)*100)/(count_vulnibm_iot_unchangedscope+count_vulnibm_sh_unchangedscope))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_unchangedscope_risklevel6+count_vulnibm_sh_unchangedscope_risklevel6)*100)/(count_vulnibm_iot_unchangedscope+count_vulnibm_sh_unchangedscope))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_unchangedscope_risklevel5+count_vulnibm_sh_unchangedscope_risklevel5)*100)/(count_vulnibm_iot_unchangedscope+count_vulnibm_sh_unchangedscope))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_unchangedscope_risklevel4+count_vulnibm_sh_unchangedscope_risklevel4)*100)/(count_vulnibm_iot_unchangedscope+count_vulnibm_sh_unchangedscope))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_unchangedscope_risklevel3+count_vulnibm_sh_unchangedscope_risklevel3)*100)/(count_vulnibm_iot_unchangedscope+count_vulnibm_sh_unchangedscope))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_unchangedscope_risklevel2+count_vulnibm_sh_unchangedscope_risklevel2)*100)/(count_vulnibm_iot_unchangedscope+count_vulnibm_sh_unchangedscope))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_unchangedscope_risklevel1+count_vulnibm_sh_unchangedscope_risklevel1)*100)/(count_vulnibm_iot_unchangedscope+count_vulnibm_sh_unchangedscope))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_unchangedscope_risklevel0+count_vulnibm_sh_unchangedscope_risklevel0)*100)/(count_vulnibm_iot_unchangedscope+count_vulnibm_sh_unchangedscope))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("            -    EL VALOR MEDIO DE PUNTUACION BASE ES  "+str(float(((count_vulnibm_iot_unchangedscope_risklevel+count_vulnibm_sh_unchangedscope_risklevel)/(count_vulnibm_iot_unchangedscope+count_vulnibm_sh_unchangedscope))))+"\n")
print("\n")










