
import pandas as pd
from datetime import datetime,timedelta



#Abro los ficheros con los que voy a tratar




df_vulnibm_iot = pd.read_excel('vulnerabilidades_ibm_iot_2023.xlsx')

count_vulnibm_iot_access_vector=0

count_vulnibm_iot_networkaccesvector=0
count_vulnibm_iot_networkaccesvector_risklevel=0
count_vulnibm_iot_networkaccesvector_risklevel10=0
count_vulnibm_iot_networkaccesvector_risklevel9=0
count_vulnibm_iot_networkaccesvector_risklevel8=0
count_vulnibm_iot_networkaccesvector_risklevel7=0
count_vulnibm_iot_networkaccesvector_risklevel6=0
count_vulnibm_iot_networkaccesvector_risklevel5=0
count_vulnibm_iot_networkaccesvector_risklevel4=0
count_vulnibm_iot_networkaccesvector_risklevel3=0
count_vulnibm_iot_networkaccesvector_risklevel2=0
count_vulnibm_iot_networkaccesvector_risklevel1=0
count_vulnibm_iot_networkaccesvector_risklevel0=0



count_vulnibm_iot_localaccesvector=0
count_vulnibm_iot_localaccesvector_risklevel=0
count_vulnibm_iot_localaccesvector_risklevel10=0
count_vulnibm_iot_localaccesvector_risklevel9=0
count_vulnibm_iot_localaccesvector_risklevel8=0
count_vulnibm_iot_localaccesvector_risklevel7=0
count_vulnibm_iot_localaccesvector_risklevel6=0
count_vulnibm_iot_localaccesvector_risklevel5=0
count_vulnibm_iot_localaccesvector_risklevel4=0
count_vulnibm_iot_localaccesvector_risklevel3=0
count_vulnibm_iot_localaccesvector_risklevel2=0
count_vulnibm_iot_localaccesvector_risklevel1=0
count_vulnibm_iot_localaccesvector_risklevel0=0


count_vulnibm_iot_adjacentaccesvector=0
count_vulnibm_iot_adjacentaccesvector_risklevel=0
count_vulnibm_iot_adjacentaccesvector_risklevel10=0
count_vulnibm_iot_adjacentaccesvector_risklevel9=0
count_vulnibm_iot_adjacentaccesvector_risklevel8=0
count_vulnibm_iot_adjacentaccesvector_risklevel7=0
count_vulnibm_iot_adjacentaccesvector_risklevel6=0
count_vulnibm_iot_adjacentaccesvector_risklevel5=0
count_vulnibm_iot_adjacentaccesvector_risklevel4=0
count_vulnibm_iot_adjacentaccesvector_risklevel3=0
count_vulnibm_iot_adjacentaccesvector_risklevel2=0
count_vulnibm_iot_adjacentaccesvector_risklevel1=0
count_vulnibm_iot_adjacentaccesvector_risklevel0=0



count_vulnibm_iot_physicalaccesvector=0
count_vulnibm_iot_physicalaccesvector_risklevel=0
count_vulnibm_iot_physicalaccesvector_risklevel10=0
count_vulnibm_iot_physicalaccesvector_risklevel9=0
count_vulnibm_iot_physicalaccesvector_risklevel8=0
count_vulnibm_iot_physicalaccesvector_risklevel7=0
count_vulnibm_iot_physicalaccesvector_risklevel6=0
count_vulnibm_iot_physicalaccesvector_risklevel5=0
count_vulnibm_iot_physicalaccesvector_risklevel4=0
count_vulnibm_iot_physicalaccesvector_risklevel3=0
count_vulnibm_iot_physicalaccesvector_risklevel2=0
count_vulnibm_iot_physicalaccesvector_risklevel1=0
count_vulnibm_iot_physicalaccesvector_risklevel0=0


















#Comprobamos el contenido de VECTOR DE ATAQUE
for r in range(0,len(df_vulnibm_iot["x_xfe_cvss_access_vector"])):                       
    aux_str=df_vulnibm_iot["x_xfe_cvss_access_vector"][r].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
    if(aux_str!='NONE' or aux_str!='None'):
        count_vulnibm_iot_access_vector+=1
        if('Network' == aux_str):
            count_vulnibm_iot_networkaccesvector+=1
            count_vulnibm_iot_networkaccesvector_risklevel+=float(df_vulnibm_iot["x_xfe_risk_level"][r])
            if(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 10.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=9.0)):
                count_vulnibm_iot_networkaccesvector_risklevel9+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 9.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=8.0)):
                count_vulnibm_iot_networkaccesvector_risklevel8+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 8.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=7.0)):
                count_vulnibm_iot_networkaccesvector_risklevel7+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 7.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=6.0)):
                count_vulnibm_iot_networkaccesvector_risklevel6+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 6.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=5.0)):
                count_vulnibm_iot_networkaccesvector_risklevel5+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 5.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=4.0)):
                count_vulnibm_iot_networkaccesvector_risklevel4+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 4.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=3.0)):
                count_vulnibm_iot_networkaccesvector_risklevel3+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 3.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=2.0)):
                count_vulnibm_iot_networkaccesvector_risklevel2+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 2.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=1.0)):
                count_vulnibm_iot_networkaccesvector_risklevel1+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 1.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=0.0)):
                count_vulnibm_iot_networkaccesvector_risklevel0+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) == 10.0)):
                count_vulnibm_iot_networkaccesvector_risklevel10+=1
            
        elif('Local' in aux_str):
            
            count_vulnibm_iot_localaccesvector+=1
            count_vulnibm_iot_localaccesvector_risklevel+=float(df_vulnibm_iot["x_xfe_risk_level"][r])
            if(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 10.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=9.0)):
                count_vulnibm_iot_localaccesvector_risklevel9+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 9.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=8.0)):
                count_vulnibm_iot_localaccesvector_risklevel8+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 8.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=7.0)):
                count_vulnibm_iot_localaccesvector_risklevel7+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 7.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=6.0)):
                count_vulnibm_iot_localaccesvector_risklevel6+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 6.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=5.0)):
                count_vulnibm_iot_localaccesvector_risklevel5+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 5.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=4.0)):
                count_vulnibm_iot_localaccesvector_risklevel4+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 4.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=3.0)):
                count_vulnibm_iot_localaccesvector_risklevel3+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 3.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=2.0)):
                count_vulnibm_iot_localaccesvector_risklevel2+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 2.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=1.0)):
                count_vulnibm_iot_localaccesvector_risklevel1+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 1.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=0.0)):
                count_vulnibm_iot_localaccesvector_risklevel0+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) == 10.0)):
                count_vulnibm_iot_localaccesvector_risklevel10+=1
            
            
        elif('Adjacent' in aux_str):
        
            count_vulnibm_iot_adjacentaccesvector+=1
            count_vulnibm_iot_adjacentaccesvector_risklevel+=float(df_vulnibm_iot["x_xfe_risk_level"][r])
            if(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 10.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=9.0)):
                count_vulnibm_iot_adjacentaccesvector_risklevel9+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 9.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=8.0)):
                count_vulnibm_iot_adjacentaccesvector_risklevel8+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 8.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=7.0)):
                count_vulnibm_iot_adjacentaccesvector_risklevel7+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 7.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=6.0)):
                count_vulnibm_iot_adjacentaccesvector_risklevel6+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 6.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=5.0)):
                count_vulnibm_iot_adjacentaccesvector_risklevel5+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 5.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=4.0)):
                count_vulnibm_iot_adjacentaccesvector_risklevel4+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 4.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=3.0)):
                count_vulnibm_iot_adjacentaccesvector_risklevel3+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 3.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=2.0)):
                count_vulnibm_iot_adjacentaccesvector_risklevel2+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 2.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=1.0)):
                count_vulnibm_iot_adjacentaccesvector_risklevel1+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 1.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=0.0)):
                count_vulnibm_iot_adjacentaccesvector_risklevel0+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) == 10.0)):
                count_vulnibm_iot_adjacentaccesvector_risklevel10+=1
                
        
        
        elif('Physical' in aux_str):
        
            count_vulnibm_iot_physicalaccesvector+=1
            count_vulnibm_iot_physicalaccesvector_risklevel+=float(df_vulnibm_iot["x_xfe_risk_level"][r])
            if(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 10.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=9.0)):
                count_vulnibm_iot_physicalaccesvector_risklevel9+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 9.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=8.0)):
                count_vulnibm_iot_physicalaccesvector_risklevel8+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 8.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=7.0)):
                count_vulnibm_iot_physicalaccesvector_risklevel7+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 7.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=6.0)):
                count_vulnibm_iot_physicalaccesvector_risklevel6+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 6.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=5.0)):
                count_vulnibm_iot_physicalaccesvector_risklevel5+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 5.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=4.0)):
                count_vulnibm_iot_physicalaccesvector_risklevel4+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 4.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=3.0)):
                count_vulnibm_iot_physicalaccesvector_risklevel3+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 3.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=2.0)):
                count_vulnibm_iot_physicalaccesvector_risklevel2+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 2.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=1.0)):
                count_vulnibm_iot_physicalaccesvector_risklevel1+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 1.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=0.0)):
                count_vulnibm_iot_physicalaccesvector_risklevel0+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) == 10.0)):
                count_vulnibm_iot_physicalaccesvector_risklevel10+=1
            
        
                
                
                
                
print("********************************ESTADÍSTICAS VECTOR DE ATAQUE/PUNTUACION BASE VULNERABILIDADES IBM PARTE IOT********************************")
print("\n")                            
print("\n")
print(" DE UN TOTAL DE "+str(count_vulnibm_iot_access_vector)+" VULNERABILIDADES:\n") 
print("\n")
print("   - LAS ESTADISTICAS DE VALORES DE VECTOR DE ATAQUE SON LAS SIGUIENTES:  \n")
print("      -    EN  "+str(count_vulnibm_iot_networkaccesvector)+" VULNERABILIDADES EL VECTOR  DE ACCESO ES LA RED, LAS ESTADÍSTICAS DE PUNTUACION BASE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_networkaccesvector_risklevel10)+" VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
print("            -    EN  "+str(count_vulnibm_iot_networkaccesvector_risklevel9)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN  "+str(count_vulnibm_iot_networkaccesvector_risklevel8)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN  "+str(count_vulnibm_iot_networkaccesvector_risklevel7)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN  "+str(count_vulnibm_iot_networkaccesvector_risklevel6)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN "+str(count_vulnibm_iot_networkaccesvector_risklevel5)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN "+str(count_vulnibm_iot_networkaccesvector_risklevel4)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN "+str(count_vulnibm_iot_networkaccesvector_risklevel3)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN "+str(count_vulnibm_iot_networkaccesvector_risklevel2)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN "+str(count_vulnibm_iot_networkaccesvector_risklevel1)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN "+str(count_vulnibm_iot_networkaccesvector_risklevel0)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_localaccesvector)+" VULNERABILIDADES EL VECTOR  DE ACCESO ES LOCAL, LAS ESTADÍSTICAS DE PUNTUACION BASE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_localaccesvector_risklevel10)+" VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
print("            -    EN  "+str(count_vulnibm_iot_localaccesvector_risklevel9)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN  "+str(count_vulnibm_iot_localaccesvector_risklevel8)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN  "+str(count_vulnibm_iot_localaccesvector_risklevel7)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN  "+str(count_vulnibm_iot_localaccesvector_risklevel6)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN "+str(count_vulnibm_iot_localaccesvector_risklevel5)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN "+str(count_vulnibm_iot_localaccesvector_risklevel4)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN "+str(count_vulnibm_iot_localaccesvector_risklevel3)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN "+str(count_vulnibm_iot_localaccesvector_risklevel2)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN "+str(count_vulnibm_iot_localaccesvector_risklevel1)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN "+str(count_vulnibm_iot_localaccesvector_risklevel0)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_adjacentaccesvector)+" VULNERABILIDADES EL VECTOR  DE ACCESO ES RED ADYACENTE, LAS ESTADÍSTICAS DE PUNTUACION BASE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_adjacentaccesvector_risklevel10)+" VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
print("            -    EN  "+str(count_vulnibm_iot_adjacentaccesvector_risklevel9)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN  "+str(count_vulnibm_iot_adjacentaccesvector_risklevel8)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN  "+str(count_vulnibm_iot_adjacentaccesvector_risklevel7)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN  "+str(count_vulnibm_iot_adjacentaccesvector_risklevel6)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN "+str(count_vulnibm_iot_adjacentaccesvector_risklevel5)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN "+str(count_vulnibm_iot_adjacentaccesvector_risklevel4)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN "+str(count_vulnibm_iot_adjacentaccesvector_risklevel3)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN "+str(count_vulnibm_iot_adjacentaccesvector_risklevel2)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN "+str(count_vulnibm_iot_adjacentaccesvector_risklevel1)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN "+str(count_vulnibm_iot_adjacentaccesvector_risklevel0)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")

print("      -    EN  "+str(count_vulnibm_iot_physicalaccesvector)+" VULNERABILIDADES EL VECTOR  DE ACCESO ES FÍSICO, LAS ESTADÍSTICAS DE PUNTUACION BASE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_physicalaccesvector_risklevel10)+" VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
print("            -    EN  "+str(count_vulnibm_iot_physicalaccesvector_risklevel9)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN  "+str(count_vulnibm_iot_physicalaccesvector_risklevel8)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN  "+str(count_vulnibm_iot_physicalaccesvector_risklevel7)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN  "+str(count_vulnibm_iot_physicalaccesvector_risklevel6)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN "+str(count_vulnibm_iot_physicalaccesvector_risklevel5)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN "+str(count_vulnibm_iot_physicalaccesvector_risklevel4)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN "+str(count_vulnibm_iot_physicalaccesvector_risklevel3)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN "+str(count_vulnibm_iot_physicalaccesvector_risklevel2)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN "+str(count_vulnibm_iot_physicalaccesvector_risklevel1)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN "+str(count_vulnibm_iot_physicalaccesvector_risklevel0)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("\n")




print("********************************PORCENTAJE VECTOR DE ATAQUE/PUNTUACION BASE VULNERABILIDADES IBM PARTE IOT********************************")
print("\n")                            
print("\n")
print(" DE UN TOTAL DE "+str(count_vulnibm_iot_access_vector)+" VULNERABILIDADES :\n") 
print("\n")
print("   - LOS PORCENTAJES DE VALORES DE VECTOR DE ATAQUE SON LOS SIGUIENTES:  \n")
print("      -    EN EL  "+str(float(((count_vulnibm_iot_networkaccesvector*100)/count_vulnibm_iot_access_vector)))+" % DE VULNERABILIDADES EL VECTOR  DE ACCESO ES LA RED, LAS ESTADÍSTICAS DE PUNTUACION BASE SON LAS SIGUIENTES :  \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_networkaccesvector_risklevel10*100)/count_vulnibm_iot_networkaccesvector)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_networkaccesvector_risklevel9*100)/count_vulnibm_iot_networkaccesvector)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_networkaccesvector_risklevel8*100)/count_vulnibm_iot_networkaccesvector)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_networkaccesvector_risklevel7*100)/count_vulnibm_iot_networkaccesvector)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_networkaccesvector_risklevel6*100)/count_vulnibm_iot_networkaccesvector)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_networkaccesvector_risklevel5*100)/count_vulnibm_iot_networkaccesvector)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_networkaccesvector_risklevel4*100)/count_vulnibm_iot_networkaccesvector)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_networkaccesvector_risklevel3*100)/count_vulnibm_iot_networkaccesvector)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_networkaccesvector_risklevel2*100)/count_vulnibm_iot_networkaccesvector)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_networkaccesvector_risklevel1*100)/count_vulnibm_iot_networkaccesvector)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_networkaccesvector_risklevel0*100)/count_vulnibm_iot_networkaccesvector)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("            -    EL VALOR MEDIO DE PUNTUACION BASE ES  "+str(float(((count_vulnibm_iot_networkaccesvector_risklevel)/count_vulnibm_iot_networkaccesvector)))+"\n")
print("\n")
print("      -    EN EL  "+str(float(((count_vulnibm_iot_localaccesvector*100)/count_vulnibm_iot_access_vector)))+" % DE VULNERABILIDADES EL VECTOR  DE ACCESO ES LOCAL, LAS ESTADÍSTICAS DE PUNTUACION BASE SON LAS SIGUIENTES :  \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_localaccesvector_risklevel10*100)/count_vulnibm_iot_localaccesvector)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_localaccesvector_risklevel9*100)/count_vulnibm_iot_localaccesvector)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_localaccesvector_risklevel8*100)/count_vulnibm_iot_localaccesvector)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_localaccesvector_risklevel7*100)/count_vulnibm_iot_localaccesvector)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_localaccesvector_risklevel6*100)/count_vulnibm_iot_localaccesvector)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_localaccesvector_risklevel5*100)/count_vulnibm_iot_localaccesvector)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_localaccesvector_risklevel4*100)/count_vulnibm_iot_localaccesvector)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_localaccesvector_risklevel3*100)/count_vulnibm_iot_localaccesvector)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_localaccesvector_risklevel2*100)/count_vulnibm_iot_localaccesvector)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_localaccesvector_risklevel1*100)/count_vulnibm_iot_localaccesvector)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_localaccesvector_risklevel0*100)/count_vulnibm_iot_localaccesvector)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("            -    EL VALOR MEDIO DE PUNTUACION BASE ES  "+str(float(((count_vulnibm_iot_localaccesvector_risklevel)/count_vulnibm_iot_localaccesvector)))+"\n")
print("\n")
if(count_vulnibm_iot_adjacentaccesvector>0):
    print("      -    EN EL  "+str(float(((count_vulnibm_iot_adjacentaccesvector*100)/count_vulnibm_iot_access_vector)))+" % DE VULNERABILIDADES EL VECTOR  DE ACCESO ES RED ADYACENTE, LAS ESTADÍSTICAS DE PUNTUACION BASE SON LAS SIGUIENTES :  \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_adjacentaccesvector_risklevel10*100)/count_vulnibm_iot_adjacentaccesvector)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_adjacentaccesvector_risklevel9*100)/count_vulnibm_iot_adjacentaccesvector)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_adjacentaccesvector_risklevel8*100)/count_vulnibm_iot_adjacentaccesvector)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_adjacentaccesvector_risklevel7*100)/count_vulnibm_iot_adjacentaccesvector)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_adjacentaccesvector_risklevel6*100)/count_vulnibm_iot_adjacentaccesvector)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_iot_adjacentaccesvector_risklevel5*100)/count_vulnibm_iot_adjacentaccesvector)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_iot_adjacentaccesvector_risklevel4*100)/count_vulnibm_iot_adjacentaccesvector)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_iot_adjacentaccesvector_risklevel3*100)/count_vulnibm_iot_adjacentaccesvector)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_iot_adjacentaccesvector_risklevel2*100)/count_vulnibm_iot_adjacentaccesvector)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_iot_adjacentaccesvector_risklevel1*100)/count_vulnibm_iot_adjacentaccesvector)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_iot_adjacentaccesvector_risklevel0*100)/count_vulnibm_iot_adjacentaccesvector)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
    print("            -    EL VALOR MEDIO DE PUNTUACION BASE ES  "+str(float(((count_vulnibm_iot_adjacentaccesvector_risklevel)/count_vulnibm_iot_adjacentaccesvector)))+"\n")
    print("\n")

if(count_vulnibm_iot_physicalaccesvector>0):
    print("      -    EN EL  "+str(float(((count_vulnibm_iot_physicalaccesvector*100)/count_vulnibm_iot_access_vector)))+" % DE VULNERABILIDADES EL VECTOR  DE ACCESO ES FÍSICO, LAS ESTADÍSTICAS DE PUNTUACION BASE SON LAS SIGUIENTES :  \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_physicalaccesvector_risklevel10*100)/count_vulnibm_iot_physicalaccesvector)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_physicalaccesvector_risklevel9*100)/count_vulnibm_iot_physicalaccesvector)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_physicalaccesvector_risklevel8*100)/count_vulnibm_iot_physicalaccesvector)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_physicalaccesvector_risklevel7*100)/count_vulnibm_iot_physicalaccesvector)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_physicalaccesvector_risklevel6*100)/count_vulnibm_iot_physicalaccesvector)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_iot_physicalaccesvector_risklevel5*100)/count_vulnibm_iot_physicalaccesvector)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_iot_physicalaccesvector_risklevel4*100)/count_vulnibm_iot_physicalaccesvector)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_iot_physicalaccesvector_risklevel3*100)/count_vulnibm_iot_physicalaccesvector)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_iot_physicalaccesvector_risklevel2*100)/count_vulnibm_iot_physicalaccesvector)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_iot_physicalaccesvector_risklevel1*100)/count_vulnibm_iot_physicalaccesvector)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_iot_physicalaccesvector_risklevel0*100)/count_vulnibm_iot_physicalaccesvector)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
    print("            -    EL VALOR MEDIO DE PUNTUACION BASE ES  "+str(float(((count_vulnibm_iot_physicalaccesvector_risklevel)/count_vulnibm_iot_physicalaccesvector)))+"\n")
    print("\n")








#Abro los ficheros con los que voy a tratar




df_vulnibm_sh = pd.read_excel('vulnerabilidades_ibm_smart_home_2023.xlsx')

count_vulnibm_sh_access_vector=0

count_vulnibm_sh_networkaccesvector=0
count_vulnibm_sh_networkaccesvector_risklevel=0
count_vulnibm_sh_networkaccesvector_risklevel10=0
count_vulnibm_sh_networkaccesvector_risklevel9=0
count_vulnibm_sh_networkaccesvector_risklevel8=0
count_vulnibm_sh_networkaccesvector_risklevel7=0
count_vulnibm_sh_networkaccesvector_risklevel6=0
count_vulnibm_sh_networkaccesvector_risklevel5=0
count_vulnibm_sh_networkaccesvector_risklevel4=0
count_vulnibm_sh_networkaccesvector_risklevel3=0
count_vulnibm_sh_networkaccesvector_risklevel2=0
count_vulnibm_sh_networkaccesvector_risklevel1=0
count_vulnibm_sh_networkaccesvector_risklevel0=0



count_vulnibm_sh_localaccesvector=0
count_vulnibm_sh_localaccesvector_risklevel=0
count_vulnibm_sh_localaccesvector_risklevel10=0
count_vulnibm_sh_localaccesvector_risklevel9=0
count_vulnibm_sh_localaccesvector_risklevel8=0
count_vulnibm_sh_localaccesvector_risklevel7=0
count_vulnibm_sh_localaccesvector_risklevel6=0
count_vulnibm_sh_localaccesvector_risklevel5=0
count_vulnibm_sh_localaccesvector_risklevel4=0
count_vulnibm_sh_localaccesvector_risklevel3=0
count_vulnibm_sh_localaccesvector_risklevel2=0
count_vulnibm_sh_localaccesvector_risklevel1=0
count_vulnibm_sh_localaccesvector_risklevel0=0


count_vulnibm_sh_adjacentaccesvector=0
count_vulnibm_sh_adjacentaccesvector_risklevel=0
count_vulnibm_sh_adjacentaccesvector_risklevel10=0
count_vulnibm_sh_adjacentaccesvector_risklevel9=0
count_vulnibm_sh_adjacentaccesvector_risklevel8=0
count_vulnibm_sh_adjacentaccesvector_risklevel7=0
count_vulnibm_sh_adjacentaccesvector_risklevel6=0
count_vulnibm_sh_adjacentaccesvector_risklevel5=0
count_vulnibm_sh_adjacentaccesvector_risklevel4=0
count_vulnibm_sh_adjacentaccesvector_risklevel3=0
count_vulnibm_sh_adjacentaccesvector_risklevel2=0
count_vulnibm_sh_adjacentaccesvector_risklevel1=0
count_vulnibm_sh_adjacentaccesvector_risklevel0=0


count_vulnibm_sh_physicalaccesvector=0
count_vulnibm_sh_physicalaccesvector_risklevel=0
count_vulnibm_sh_physicalaccesvector_risklevel10=0
count_vulnibm_sh_physicalaccesvector_risklevel9=0
count_vulnibm_sh_physicalaccesvector_risklevel8=0
count_vulnibm_sh_physicalaccesvector_risklevel7=0
count_vulnibm_sh_physicalaccesvector_risklevel6=0
count_vulnibm_sh_physicalaccesvector_risklevel5=0
count_vulnibm_sh_physicalaccesvector_risklevel4=0
count_vulnibm_sh_physicalaccesvector_risklevel3=0
count_vulnibm_sh_physicalaccesvector_risklevel2=0
count_vulnibm_sh_physicalaccesvector_risklevel1=0
count_vulnibm_sh_physicalaccesvector_risklevel0=0

#Comprobamos el contenido de VECTOR DE ATAQUE
for r in range(0,len(df_vulnibm_sh["x_xfe_cvss_access_vector"])):                       
    aux_str=df_vulnibm_sh["x_xfe_cvss_access_vector"][r].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
    if(aux_str!='NONE' or aux_str!='None'):
        count_vulnibm_sh_access_vector+=1
        if('Network' == aux_str):
            count_vulnibm_sh_networkaccesvector+=1
            count_vulnibm_sh_networkaccesvector_risklevel+=float(df_vulnibm_sh["x_xfe_risk_level"][r])
            if(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 10.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=9.0)):
                count_vulnibm_sh_networkaccesvector_risklevel9+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 9.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=8.0)):
                count_vulnibm_sh_networkaccesvector_risklevel8+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 8.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=7.0)):
                count_vulnibm_sh_networkaccesvector_risklevel7+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 7.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=6.0)):
                count_vulnibm_sh_networkaccesvector_risklevel6+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 6.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=5.0)):
                count_vulnibm_sh_networkaccesvector_risklevel5+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 5.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=4.0)):
                count_vulnibm_sh_networkaccesvector_risklevel4+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 4.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=3.0)):
                count_vulnibm_sh_networkaccesvector_risklevel3+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 3.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=2.0)):
                count_vulnibm_sh_networkaccesvector_risklevel2+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 2.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=1.0)):
                count_vulnibm_sh_networkaccesvector_risklevel1+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 1.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=0.0)):
                count_vulnibm_sh_networkaccesvector_risklevel0+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) == 10.0)):
                count_vulnibm_sh_networkaccesvector_risklevel10+=1
            
        elif('Local' in aux_str):
            
            count_vulnibm_sh_localaccesvector+=1
            count_vulnibm_sh_localaccesvector_risklevel+=float(df_vulnibm_sh["x_xfe_risk_level"][r])
            if(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 10.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=9.0)):
                count_vulnibm_sh_localaccesvector_risklevel9+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 9.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=8.0)):
                count_vulnibm_sh_localaccesvector_risklevel8+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 8.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=7.0)):
                count_vulnibm_sh_localaccesvector_risklevel7+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 7.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=6.0)):
                count_vulnibm_sh_localaccesvector_risklevel6+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 6.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=5.0)):
                count_vulnibm_sh_localaccesvector_risklevel5+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 5.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=4.0)):
                count_vulnibm_sh_localaccesvector_risklevel4+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 4.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=3.0)):
                count_vulnibm_sh_localaccesvector_risklevel3+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 3.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=2.0)):
                count_vulnibm_sh_localaccesvector_risklevel2+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 2.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=1.0)):
                count_vulnibm_sh_localaccesvector_risklevel1+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 1.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=0.0)):
                count_vulnibm_sh_localaccesvector_risklevel0+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) == 10.0)):
                count_vulnibm_sh_localaccesvector_risklevel10+=1
            
            
        elif('Adjacent' in aux_str):
        
            count_vulnibm_sh_adjacentaccesvector+=1
            count_vulnibm_sh_adjacentaccesvector_risklevel+=float(df_vulnibm_sh["x_xfe_risk_level"][r])
            if(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 10.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=9.0)):
                count_vulnibm_sh_adjacentaccesvector_risklevel9+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 9.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=8.0)):
                count_vulnibm_sh_adjacentaccesvector_risklevel8+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 8.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=7.0)):
                count_vulnibm_sh_adjacentaccesvector_risklevel7+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 7.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=6.0)):
                count_vulnibm_sh_adjacentaccesvector_risklevel6+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 6.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=5.0)):
                count_vulnibm_sh_adjacentaccesvector_risklevel5+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 5.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=4.0)):
                count_vulnibm_sh_adjacentaccesvector_risklevel4+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 4.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=3.0)):
                count_vulnibm_sh_adjacentaccesvector_risklevel3+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 3.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=2.0)):
                count_vulnibm_sh_adjacentaccesvector_risklevel2+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 2.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=1.0)):
                count_vulnibm_sh_adjacentaccesvector_risklevel1+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 1.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=0.0)):
                count_vulnibm_sh_adjacentaccesvector_risklevel0+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) == 10.0)):
                count_vulnibm_sh_adjacentaccesvector_risklevel10+=1
                
                
        elif('Physical' in aux_str):
        
            count_vulnibm_sh_physicalaccesvector+=1
            count_vulnibm_sh_physicalaccesvector_risklevel+=float(df_vulnibm_sh["x_xfe_risk_level"][r])
            if(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 10.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=9.0)):
                count_vulnibm_sh_physicalaccesvector_risklevel9+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 9.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=8.0)):
                count_vulnibm_sh_physicalaccesvector_risklevel8+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 8.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=7.0)):
                count_vulnibm_sh_physicalaccesvector_risklevel7+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 7.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=6.0)):
                count_vulnibm_sh_physicalaccesvector_risklevel6+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 6.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=5.0)):
                count_vulnibm_sh_physicalaccesvector_risklevel5+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 5.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=4.0)):
                count_vulnibm_sh_physicalaccesvector_risklevel4+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 4.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=3.0)):
                count_vulnibm_sh_physicalaccesvector_risklevel3+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 3.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=2.0)):
                count_vulnibm_sh_physicalaccesvector_risklevel2+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 2.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=1.0)):
                count_vulnibm_sh_physicalaccesvector_risklevel1+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 1.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=0.0)):
                count_vulnibm_sh_physicalaccesvector_risklevel0+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) == 10.0)):
                count_vulnibm_sh_physicalaccesvector_risklevel10+=1
            
        
                
                
                
                
print("********************************ESTADÍSTICAS VECTOR DE ATAQUE/PUNTUACION BASE VULNERABILIDADES IBM PARTE SMART HOME********************************")
print("\n")                            
print("\n")
print(" DE UN TOTAL DE "+str(count_vulnibm_sh_access_vector)+" VULNERABILIDADES:\n") 
print("\n")
print("   - LAS ESTADISTICAS DE VALORES DE VECTOR DE ATAQUE SON LAS SIGUIENTES:  \n")
print("      -    EN  "+str(count_vulnibm_sh_networkaccesvector)+" VULNERABILIDADES EL VECTOR  DE ACCESO ES LA RED, LAS ESTADÍSTICAS DE PUNTUACION BASE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_sh_networkaccesvector_risklevel10)+" VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
print("            -    EN  "+str(count_vulnibm_sh_networkaccesvector_risklevel9)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN  "+str(count_vulnibm_sh_networkaccesvector_risklevel8)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN  "+str(count_vulnibm_sh_networkaccesvector_risklevel7)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN  "+str(count_vulnibm_sh_networkaccesvector_risklevel6)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN "+str(count_vulnibm_sh_networkaccesvector_risklevel5)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN "+str(count_vulnibm_sh_networkaccesvector_risklevel4)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN "+str(count_vulnibm_sh_networkaccesvector_risklevel3)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN "+str(count_vulnibm_sh_networkaccesvector_risklevel2)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN "+str(count_vulnibm_sh_networkaccesvector_risklevel1)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN "+str(count_vulnibm_sh_networkaccesvector_risklevel0)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_sh_localaccesvector)+" VULNERABILIDADES EL VECTOR  DE ACCESO ES LOCAL, LAS ESTADÍSTICAS DE PUNTUACION BASE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_sh_localaccesvector_risklevel10)+" VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
print("            -    EN  "+str(count_vulnibm_sh_localaccesvector_risklevel9)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN  "+str(count_vulnibm_sh_localaccesvector_risklevel8)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN  "+str(count_vulnibm_sh_localaccesvector_risklevel7)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN  "+str(count_vulnibm_sh_localaccesvector_risklevel6)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN "+str(count_vulnibm_sh_localaccesvector_risklevel5)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN "+str(count_vulnibm_sh_localaccesvector_risklevel4)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN "+str(count_vulnibm_sh_localaccesvector_risklevel3)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN "+str(count_vulnibm_sh_localaccesvector_risklevel2)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN "+str(count_vulnibm_sh_localaccesvector_risklevel1)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN "+str(count_vulnibm_sh_localaccesvector_risklevel0)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_sh_adjacentaccesvector)+" VULNERABILIDADES EL VECTOR  DE ACCESO ES RED ADYACENTE, LAS ESTADÍSTICAS DE PUNTUACION BASE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_sh_adjacentaccesvector_risklevel10)+" VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
print("            -    EN  "+str(count_vulnibm_sh_adjacentaccesvector_risklevel9)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN  "+str(count_vulnibm_sh_adjacentaccesvector_risklevel8)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN  "+str(count_vulnibm_sh_adjacentaccesvector_risklevel7)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN  "+str(count_vulnibm_sh_adjacentaccesvector_risklevel6)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN "+str(count_vulnibm_sh_adjacentaccesvector_risklevel5)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN "+str(count_vulnibm_sh_adjacentaccesvector_risklevel4)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN "+str(count_vulnibm_sh_adjacentaccesvector_risklevel3)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN "+str(count_vulnibm_sh_adjacentaccesvector_risklevel2)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN "+str(count_vulnibm_sh_adjacentaccesvector_risklevel1)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN "+str(count_vulnibm_sh_adjacentaccesvector_risklevel0)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_sh_physicalaccesvector)+" VULNERABILIDADES EL VECTOR  DE ACCESO ES FÍSICO, LAS ESTADÍSTICAS DE PUNTUACION BASE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_sh_physicalaccesvector_risklevel10)+" VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
print("            -    EN  "+str(count_vulnibm_sh_physicalaccesvector_risklevel9)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN  "+str(count_vulnibm_sh_physicalaccesvector_risklevel8)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN  "+str(count_vulnibm_sh_physicalaccesvector_risklevel7)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN  "+str(count_vulnibm_sh_physicalaccesvector_risklevel6)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN "+str(count_vulnibm_sh_physicalaccesvector_risklevel5)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN "+str(count_vulnibm_sh_physicalaccesvector_risklevel4)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN "+str(count_vulnibm_sh_physicalaccesvector_risklevel3)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN "+str(count_vulnibm_sh_physicalaccesvector_risklevel2)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN "+str(count_vulnibm_sh_physicalaccesvector_risklevel1)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN "+str(count_vulnibm_sh_physicalaccesvector_risklevel0)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("\n")





print("********************************PORCENTAJE VECTOR DE ATAQUE/PUNTUACION BASE VULNERABILIDADES IBM PARTE SMART HOME********************************")
print("\n")                            
print("\n")
print(" DE UN TOTAL DE "+str(count_vulnibm_sh_access_vector)+" VULNERABILIDADES :\n") 
print("\n")
print("   - LOS PORCENTAJES DE VALORES DE VECTOR DE ATAQUE SON LOS SIGUIENTES:  \n")
print("      -    EN EL  "+str(float(((count_vulnibm_sh_networkaccesvector*100)/count_vulnibm_sh_access_vector)))+" % DE VULNERABILIDADES EL VECTOR  DE ACCESO ES LA RED, LAS ESTADÍSTICAS DE PUNTUACION BASE SON LAS SIGUIENTES :  \n")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_networkaccesvector_risklevel10*100)/count_vulnibm_sh_networkaccesvector)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_networkaccesvector_risklevel9*100)/count_vulnibm_sh_networkaccesvector)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_networkaccesvector_risklevel8*100)/count_vulnibm_sh_networkaccesvector)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_networkaccesvector_risklevel7*100)/count_vulnibm_sh_networkaccesvector)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_networkaccesvector_risklevel6*100)/count_vulnibm_sh_networkaccesvector)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN EL "+str(float(((count_vulnibm_sh_networkaccesvector_risklevel5*100)/count_vulnibm_sh_networkaccesvector)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN EL "+str(float(((count_vulnibm_sh_networkaccesvector_risklevel4*100)/count_vulnibm_sh_networkaccesvector)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN EL "+str(float(((count_vulnibm_sh_networkaccesvector_risklevel3*100)/count_vulnibm_sh_networkaccesvector)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN EL "+str(float(((count_vulnibm_sh_networkaccesvector_risklevel2*100)/count_vulnibm_sh_networkaccesvector)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN EL "+str(float(((count_vulnibm_sh_networkaccesvector_risklevel1*100)/count_vulnibm_sh_networkaccesvector)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN EL "+str(float(((count_vulnibm_sh_networkaccesvector_risklevel0*100)/count_vulnibm_sh_networkaccesvector)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("            -    EL VALOR MEDIO DE PUNTUACION BASE ES  "+str(float(((count_vulnibm_sh_networkaccesvector_risklevel)/count_vulnibm_sh_networkaccesvector)))+"\n")
print("\n")
print("      -    EN EL  "+str(float(((count_vulnibm_sh_localaccesvector*100)/count_vulnibm_sh_access_vector)))+" % DE VULNERABILIDADES EL VECTOR  DE ACCESO ES LOCAL, LAS ESTADÍSTICAS DE PUNTUACION BASE SON LAS SIGUIENTES :  \n")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_localaccesvector_risklevel10*100)/count_vulnibm_sh_localaccesvector)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_localaccesvector_risklevel9*100)/count_vulnibm_sh_localaccesvector)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_localaccesvector_risklevel8*100)/count_vulnibm_sh_localaccesvector)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_localaccesvector_risklevel7*100)/count_vulnibm_sh_localaccesvector)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_localaccesvector_risklevel6*100)/count_vulnibm_sh_localaccesvector)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN EL "+str(float(((count_vulnibm_sh_localaccesvector_risklevel5*100)/count_vulnibm_sh_localaccesvector)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN EL "+str(float(((count_vulnibm_sh_localaccesvector_risklevel4*100)/count_vulnibm_sh_localaccesvector)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN EL "+str(float(((count_vulnibm_sh_localaccesvector_risklevel3*100)/count_vulnibm_sh_localaccesvector)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN EL "+str(float(((count_vulnibm_sh_localaccesvector_risklevel2*100)/count_vulnibm_sh_localaccesvector)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN EL "+str(float(((count_vulnibm_sh_localaccesvector_risklevel1*100)/count_vulnibm_sh_localaccesvector)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN EL "+str(float(((count_vulnibm_sh_localaccesvector_risklevel0*100)/count_vulnibm_sh_localaccesvector)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("            -    EL VALOR MEDIO DE PUNTUACION BASE ES  "+str(float(((count_vulnibm_sh_localaccesvector_risklevel)/count_vulnibm_sh_localaccesvector)))+"\n")
print("\n")
if(count_vulnibm_sh_adjacentaccesvector>0):
    print("      -    EN EL  "+str(float(((count_vulnibm_sh_adjacentaccesvector*100)/count_vulnibm_sh_access_vector)))+" % DE VULNERABILIDADES EL VECTOR  DE ACCESO ES RED ADYACENTE, LAS ESTADÍSTICAS DE PUNTUACION BASE SON LAS SIGUIENTES :  \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_adjacentaccesvector_risklevel10*100)/count_vulnibm_sh_adjacentaccesvector)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_adjacentaccesvector_risklevel9*100)/count_vulnibm_sh_adjacentaccesvector)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_adjacentaccesvector_risklevel8*100)/count_vulnibm_sh_adjacentaccesvector)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_adjacentaccesvector_risklevel7*100)/count_vulnibm_sh_adjacentaccesvector)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_adjacentaccesvector_risklevel6*100)/count_vulnibm_sh_adjacentaccesvector)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_sh_adjacentaccesvector_risklevel5*100)/count_vulnibm_sh_adjacentaccesvector)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_sh_adjacentaccesvector_risklevel4*100)/count_vulnibm_sh_adjacentaccesvector)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_sh_adjacentaccesvector_risklevel3*100)/count_vulnibm_sh_adjacentaccesvector)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_sh_adjacentaccesvector_risklevel2*100)/count_vulnibm_sh_adjacentaccesvector)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_sh_adjacentaccesvector_risklevel1*100)/count_vulnibm_sh_adjacentaccesvector)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_sh_adjacentaccesvector_risklevel0*100)/count_vulnibm_sh_adjacentaccesvector)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
    print("            -    EL VALOR MEDIO DE PUNTUACION BASE ES  "+str(float(((count_vulnibm_sh_adjacentaccesvector_risklevel)/count_vulnibm_sh_adjacentaccesvector)))+"\n")
    print("\n")


if(count_vulnibm_sh_physicalaccesvector>0):
    print("      -    EN EL  "+str(float(((count_vulnibm_sh_physicalaccesvector*100)/count_vulnibm_sh_access_vector)))+" % DE VULNERABILIDADES EL VECTOR  DE ACCESO ES FÍSICO, LAS ESTADÍSTICAS DE PUNTUACION BASE SON LAS SIGUIENTES :  \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_physicalaccesvector_risklevel10*100)/count_vulnibm_sh_physicalaccesvector)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_physicalaccesvector_risklevel9*100)/count_vulnibm_sh_physicalaccesvector)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_physicalaccesvector_risklevel8*100)/count_vulnibm_sh_physicalaccesvector)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_physicalaccesvector_risklevel7*100)/count_vulnibm_sh_physicalaccesvector)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_physicalaccesvector_risklevel6*100)/count_vulnibm_sh_physicalaccesvector)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_sh_physicalaccesvector_risklevel5*100)/count_vulnibm_sh_physicalaccesvector)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_sh_physicalaccesvector_risklevel4*100)/count_vulnibm_sh_physicalaccesvector)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_sh_physicalaccesvector_risklevel3*100)/count_vulnibm_sh_physicalaccesvector)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_sh_physicalaccesvector_risklevel2*100)/count_vulnibm_sh_physicalaccesvector)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_sh_physicalaccesvector_risklevel1*100)/count_vulnibm_sh_physicalaccesvector)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_sh_physicalaccesvector_risklevel0*100)/count_vulnibm_sh_physicalaccesvector)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
    print("            -    EL VALOR MEDIO DE PUNTUACION BASE ES  "+str(float(((count_vulnibm_sh_physicalaccesvector_risklevel)/count_vulnibm_sh_physicalaccesvector)))+"\n")
    print("\n")




print("********************************ESTADÍSTICAS VECTOR DE ATAQUE/PUNTUACION BASE VULNERABILIDADES IBM PARTE IOT Y SMART HOME CONJUNTAS********************************")
print("\n")                            
print("\n")
print(" DE UN TOTAL DE "+str(count_vulnibm_iot_access_vector+count_vulnibm_sh_access_vector)+" VULNERABILIDADES:\n") 
print("\n")
print("   - LAS ESTADISTICAS DE VALORES DE VECTOR DE ATAQUE SON LAS SIGUIENTES:  \n")
print("      -    EN  "+str(count_vulnibm_iot_networkaccesvector+count_vulnibm_sh_networkaccesvector)+" VULNERABILIDADES EL VECTOR  DE ACCESO ES LA RED, LAS ESTADÍSTICAS DE PUNTUACION BASE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_networkaccesvector_risklevel10+count_vulnibm_sh_networkaccesvector_risklevel10)+" VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
print("            -    EN  "+str(count_vulnibm_iot_networkaccesvector_risklevel9+count_vulnibm_sh_networkaccesvector_risklevel9)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN  "+str(count_vulnibm_iot_networkaccesvector_risklevel8+count_vulnibm_sh_networkaccesvector_risklevel8)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN  "+str(count_vulnibm_iot_networkaccesvector_risklevel7+count_vulnibm_sh_networkaccesvector_risklevel7)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN  "+str(count_vulnibm_iot_networkaccesvector_risklevel6+count_vulnibm_sh_networkaccesvector_risklevel6)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN "+str(count_vulnibm_iot_networkaccesvector_risklevel5+count_vulnibm_sh_networkaccesvector_risklevel5)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN "+str(count_vulnibm_iot_networkaccesvector_risklevel4+count_vulnibm_sh_networkaccesvector_risklevel4)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN "+str(count_vulnibm_iot_networkaccesvector_risklevel3+count_vulnibm_sh_networkaccesvector_risklevel3)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN "+str(count_vulnibm_iot_networkaccesvector_risklevel2+count_vulnibm_sh_networkaccesvector_risklevel2)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN "+str(count_vulnibm_iot_networkaccesvector_risklevel1+count_vulnibm_sh_networkaccesvector_risklevel1)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN "+str(count_vulnibm_iot_networkaccesvector_risklevel0+count_vulnibm_sh_networkaccesvector_risklevel0)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_localaccesvector+count_vulnibm_sh_localaccesvector)+" VULNERABILIDADES EL VECTOR  DE ACCESO ES LOCAL, LAS ESTADÍSTICAS DE PUNTUACION BASE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_localaccesvector_risklevel10+count_vulnibm_sh_localaccesvector_risklevel10)+" VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
print("            -    EN  "+str(count_vulnibm_iot_localaccesvector_risklevel9+count_vulnibm_sh_localaccesvector_risklevel9)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN  "+str(count_vulnibm_iot_localaccesvector_risklevel8+count_vulnibm_sh_localaccesvector_risklevel8)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN  "+str(count_vulnibm_iot_localaccesvector_risklevel7+count_vulnibm_sh_localaccesvector_risklevel7)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN  "+str(count_vulnibm_iot_localaccesvector_risklevel6+count_vulnibm_sh_localaccesvector_risklevel6)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN "+str(count_vulnibm_iot_localaccesvector_risklevel5+count_vulnibm_sh_localaccesvector_risklevel5)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN "+str(count_vulnibm_iot_localaccesvector_risklevel4+count_vulnibm_sh_localaccesvector_risklevel4)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN "+str(count_vulnibm_iot_localaccesvector_risklevel3+count_vulnibm_sh_localaccesvector_risklevel3)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN "+str(count_vulnibm_iot_localaccesvector_risklevel2+count_vulnibm_sh_localaccesvector_risklevel2)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN "+str(count_vulnibm_iot_localaccesvector_risklevel1+count_vulnibm_sh_localaccesvector_risklevel1)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN "+str(count_vulnibm_iot_localaccesvector_risklevel0+count_vulnibm_sh_localaccesvector_risklevel0)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_adjacentaccesvector+count_vulnibm_sh_adjacentaccesvector)+" VULNERABILIDADES EL VECTOR  DE ACCESO ES RED ADYACENTE, LAS ESTADÍSTICAS DE PUNTUACION BASE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_adjacentaccesvector_risklevel10+count_vulnibm_sh_adjacentaccesvector_risklevel10)+" VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
print("            -    EN  "+str(count_vulnibm_iot_adjacentaccesvector_risklevel9+count_vulnibm_sh_adjacentaccesvector_risklevel9)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN  "+str(count_vulnibm_iot_adjacentaccesvector_risklevel8+count_vulnibm_sh_adjacentaccesvector_risklevel8)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN  "+str(count_vulnibm_iot_adjacentaccesvector_risklevel7+count_vulnibm_sh_adjacentaccesvector_risklevel7)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN  "+str(count_vulnibm_iot_adjacentaccesvector_risklevel6+count_vulnibm_sh_adjacentaccesvector_risklevel6)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN "+str(count_vulnibm_iot_adjacentaccesvector_risklevel5+count_vulnibm_sh_adjacentaccesvector_risklevel5)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN "+str(count_vulnibm_iot_adjacentaccesvector_risklevel4+count_vulnibm_sh_adjacentaccesvector_risklevel4)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN "+str(count_vulnibm_iot_adjacentaccesvector_risklevel3+count_vulnibm_sh_adjacentaccesvector_risklevel3)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN "+str(count_vulnibm_iot_adjacentaccesvector_risklevel2+count_vulnibm_sh_adjacentaccesvector_risklevel2)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN "+str(count_vulnibm_iot_adjacentaccesvector_risklevel1+count_vulnibm_sh_adjacentaccesvector_risklevel1)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN "+str(count_vulnibm_iot_adjacentaccesvector_risklevel0+count_vulnibm_sh_adjacentaccesvector_risklevel0)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("\n")

print("      -    EN  "+str(count_vulnibm_iot_physicalaccesvector+count_vulnibm_sh_physicalaccesvector)+" VULNERABILIDADES EL VECTOR  DE ACCESO ES FÍSICO, LAS ESTADÍSTICAS DE PUNTUACION BASE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_physicalaccesvector_risklevel10+count_vulnibm_sh_physicalaccesvector_risklevel10)+" VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
print("            -    EN  "+str(count_vulnibm_iot_physicalaccesvector_risklevel9+count_vulnibm_sh_physicalaccesvector_risklevel9)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN  "+str(count_vulnibm_iot_physicalaccesvector_risklevel8+count_vulnibm_sh_physicalaccesvector_risklevel8)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN  "+str(count_vulnibm_iot_physicalaccesvector_risklevel7+count_vulnibm_sh_physicalaccesvector_risklevel7)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN  "+str(count_vulnibm_iot_physicalaccesvector_risklevel6+count_vulnibm_sh_physicalaccesvector_risklevel6)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN "+str(count_vulnibm_iot_physicalaccesvector_risklevel5+count_vulnibm_sh_physicalaccesvector_risklevel5)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN "+str(count_vulnibm_iot_physicalaccesvector_risklevel4+count_vulnibm_sh_physicalaccesvector_risklevel4)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN "+str(count_vulnibm_iot_physicalaccesvector_risklevel3+count_vulnibm_sh_physicalaccesvector_risklevel3)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN "+str(count_vulnibm_iot_physicalaccesvector_risklevel2+count_vulnibm_sh_physicalaccesvector_risklevel2)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN "+str(count_vulnibm_iot_physicalaccesvector_risklevel1+count_vulnibm_sh_physicalaccesvector_risklevel1)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN "+str(count_vulnibm_iot_physicalaccesvector_risklevel0+count_vulnibm_sh_physicalaccesvector_risklevel0)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("\n")








print("********************************PORCENTAJES VECTOR DE ATAQUE/PUNTUACION BASE VULNERABILIDADES IBM PARTE IOT Y SMART HOME CONJUNTAS********************************")
print("\n")                            
print("\n")
print(" DE UN TOTAL DE "+str(count_vulnibm_iot_access_vector+count_vulnibm_sh_access_vector)+" VULNERABILIDADES :\n") 
print("\n")
print("   - LOS PORCENTAJES DE VALORES DE VECTOR DE ATAQUE SON LOS SIGUIENTES:  \n")
print("      -    EN EL "+str(float((((count_vulnibm_iot_networkaccesvector+count_vulnibm_sh_networkaccesvector)*100)/(count_vulnibm_iot_access_vector+count_vulnibm_sh_access_vector))))+" % DE VULNERABILIDADES EL VECTOR  DE ACCESO ES LA RED, LOS PORCENTAJES DE PUNTUACION BASE SON LOS SIGUIENTES :  \n")
print("            -    EN EL"+str(float((((count_vulnibm_iot_networkaccesvector_risklevel10+count_vulnibm_sh_networkaccesvector_risklevel10)*100)/(count_vulnibm_iot_networkaccesvector+count_vulnibm_sh_networkaccesvector))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_networkaccesvector_risklevel9+count_vulnibm_sh_networkaccesvector_risklevel9)*100)/(count_vulnibm_iot_networkaccesvector+count_vulnibm_sh_networkaccesvector))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_networkaccesvector_risklevel8+count_vulnibm_sh_networkaccesvector_risklevel8)*100)/(count_vulnibm_iot_networkaccesvector+count_vulnibm_sh_networkaccesvector))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_networkaccesvector_risklevel7+count_vulnibm_sh_networkaccesvector_risklevel7)*100)/(count_vulnibm_iot_networkaccesvector+count_vulnibm_sh_networkaccesvector))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_networkaccesvector_risklevel6+count_vulnibm_sh_networkaccesvector_risklevel6)*100)/(count_vulnibm_iot_networkaccesvector+count_vulnibm_sh_networkaccesvector))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_networkaccesvector_risklevel5+count_vulnibm_sh_networkaccesvector_risklevel5)*100)/(count_vulnibm_iot_networkaccesvector+count_vulnibm_sh_networkaccesvector))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_networkaccesvector_risklevel4+count_vulnibm_sh_networkaccesvector_risklevel4)*100)/(count_vulnibm_iot_networkaccesvector+count_vulnibm_sh_networkaccesvector))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_networkaccesvector_risklevel3+count_vulnibm_sh_networkaccesvector_risklevel3)*100)/(count_vulnibm_iot_networkaccesvector+count_vulnibm_sh_networkaccesvector))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_networkaccesvector_risklevel2+count_vulnibm_sh_networkaccesvector_risklevel2)*100)/(count_vulnibm_iot_networkaccesvector+count_vulnibm_sh_networkaccesvector))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_networkaccesvector_risklevel1+count_vulnibm_sh_networkaccesvector_risklevel1)*100)/(count_vulnibm_iot_networkaccesvector+count_vulnibm_sh_networkaccesvector))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_networkaccesvector_risklevel0+count_vulnibm_sh_networkaccesvector_risklevel0)*100)/(count_vulnibm_iot_networkaccesvector+count_vulnibm_sh_networkaccesvector))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("            -    EL VALOR MEDIO DE PUNTUACION BASE ES  "+str(float(((count_vulnibm_iot_networkaccesvector_risklevel+count_vulnibm_sh_networkaccesvector_risklevel)/(count_vulnibm_iot_networkaccesvector+count_vulnibm_sh_networkaccesvector))))+"\n")
print("\n")
print("      -    EN EL "+str(float((((count_vulnibm_iot_localaccesvector+count_vulnibm_sh_localaccesvector)*100)/(count_vulnibm_iot_access_vector+count_vulnibm_sh_access_vector))))+" % DE VULNERABILIDADES EL VECTOR  DE ACCESO ES LOCAL, LOS PORCENTAJES DE PUNTUACION BASE SON LOS SIGUIENTES :  \n")
print("            -    EN EL"+str(float((((count_vulnibm_iot_localaccesvector_risklevel10+count_vulnibm_sh_localaccesvector_risklevel10)*100)/(count_vulnibm_iot_localaccesvector+count_vulnibm_sh_localaccesvector))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_localaccesvector_risklevel9+count_vulnibm_sh_localaccesvector_risklevel9)*100)/(count_vulnibm_iot_localaccesvector+count_vulnibm_sh_localaccesvector))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_localaccesvector_risklevel8+count_vulnibm_sh_localaccesvector_risklevel8)*100)/(count_vulnibm_iot_localaccesvector+count_vulnibm_sh_localaccesvector))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_localaccesvector_risklevel7+count_vulnibm_sh_localaccesvector_risklevel7)*100)/(count_vulnibm_iot_localaccesvector+count_vulnibm_sh_localaccesvector))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_localaccesvector_risklevel6+count_vulnibm_sh_localaccesvector_risklevel6)*100)/(count_vulnibm_iot_localaccesvector+count_vulnibm_sh_localaccesvector))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_localaccesvector_risklevel5+count_vulnibm_sh_localaccesvector_risklevel5)*100)/(count_vulnibm_iot_localaccesvector+count_vulnibm_sh_localaccesvector))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_localaccesvector_risklevel4+count_vulnibm_sh_localaccesvector_risklevel4)*100)/(count_vulnibm_iot_localaccesvector+count_vulnibm_sh_localaccesvector))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_localaccesvector_risklevel3+count_vulnibm_sh_localaccesvector_risklevel3)*100)/(count_vulnibm_iot_localaccesvector+count_vulnibm_sh_localaccesvector))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_localaccesvector_risklevel2+count_vulnibm_sh_localaccesvector_risklevel2)*100)/(count_vulnibm_iot_localaccesvector+count_vulnibm_sh_localaccesvector))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_localaccesvector_risklevel1+count_vulnibm_sh_localaccesvector_risklevel1)*100)/(count_vulnibm_iot_localaccesvector+count_vulnibm_sh_localaccesvector))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_localaccesvector_risklevel0+count_vulnibm_sh_localaccesvector_risklevel0)*100)/(count_vulnibm_iot_localaccesvector+count_vulnibm_sh_localaccesvector))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("            -    EL VALOR MEDIO DE PUNTUACION BASE ES  "+str(float(((count_vulnibm_iot_localaccesvector_risklevel+count_vulnibm_sh_localaccesvector_risklevel)/(count_vulnibm_iot_localaccesvector+count_vulnibm_sh_localaccesvector))))+"\n")
print("\n")
if((count_vulnibm_iot_adjacentaccesvector+count_vulnibm_sh_adjacentaccesvector)>0):
    print("      -    EN EL "+str(float((((count_vulnibm_iot_adjacentaccesvector+count_vulnibm_sh_adjacentaccesvector)*100)/(count_vulnibm_iot_access_vector+count_vulnibm_sh_access_vector))))+" % DE VULNERABILIDADES EL VECTOR  DE ACCESO ES RED ADYACENTE, LOS PORCENTAJES DE PUNTUACION BASE SON LOS SIGUIENTES :  \n")
    print("            -    EN EL"+str(float((((count_vulnibm_iot_adjacentaccesvector_risklevel10+count_vulnibm_sh_adjacentaccesvector_risklevel10)*100)/(count_vulnibm_iot_adjacentaccesvector+count_vulnibm_sh_adjacentaccesvector))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
    print("            -    EN EL "+str(float((((count_vulnibm_iot_adjacentaccesvector_risklevel9+count_vulnibm_sh_adjacentaccesvector_risklevel9)*100)/(count_vulnibm_iot_adjacentaccesvector+count_vulnibm_sh_adjacentaccesvector))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
    print("            -    EN EL "+str(float((((count_vulnibm_iot_adjacentaccesvector_risklevel8+count_vulnibm_sh_adjacentaccesvector_risklevel8)*100)/(count_vulnibm_iot_adjacentaccesvector+count_vulnibm_sh_adjacentaccesvector))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
    print("            -    EN EL "+str(float((((count_vulnibm_iot_adjacentaccesvector_risklevel7+count_vulnibm_sh_adjacentaccesvector_risklevel7)*100)/(count_vulnibm_iot_adjacentaccesvector+count_vulnibm_sh_adjacentaccesvector))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
    print("            -    EN EL "+str(float((((count_vulnibm_iot_adjacentaccesvector_risklevel6+count_vulnibm_sh_adjacentaccesvector_risklevel6)*100)/(count_vulnibm_iot_adjacentaccesvector+count_vulnibm_sh_adjacentaccesvector))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
    print("            -    EN EL "+str(float((((count_vulnibm_iot_adjacentaccesvector_risklevel5+count_vulnibm_sh_adjacentaccesvector_risklevel5)*100)/(count_vulnibm_iot_adjacentaccesvector+count_vulnibm_sh_adjacentaccesvector))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
    print("            -    EN EL "+str(float((((count_vulnibm_iot_adjacentaccesvector_risklevel4+count_vulnibm_sh_adjacentaccesvector_risklevel4)*100)/(count_vulnibm_iot_adjacentaccesvector+count_vulnibm_sh_adjacentaccesvector))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
    print("            -    EN EL "+str(float((((count_vulnibm_iot_adjacentaccesvector_risklevel3+count_vulnibm_sh_adjacentaccesvector_risklevel3)*100)/(count_vulnibm_iot_adjacentaccesvector+count_vulnibm_sh_adjacentaccesvector))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
    print("            -    EN EL "+str(float((((count_vulnibm_iot_adjacentaccesvector_risklevel2+count_vulnibm_sh_adjacentaccesvector_risklevel2)*100)/(count_vulnibm_iot_adjacentaccesvector+count_vulnibm_sh_adjacentaccesvector))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
    print("            -    EN EL "+str(float((((count_vulnibm_iot_adjacentaccesvector_risklevel1+count_vulnibm_sh_adjacentaccesvector_risklevel1)*100)/(count_vulnibm_iot_adjacentaccesvector+count_vulnibm_sh_adjacentaccesvector))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
    print("            -    EN EL "+str(float((((count_vulnibm_iot_adjacentaccesvector_risklevel0+count_vulnibm_sh_adjacentaccesvector_risklevel0)*100)/(count_vulnibm_iot_adjacentaccesvector+count_vulnibm_sh_adjacentaccesvector))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
    print("            -    EL VALOR MEDIO DE PUNTUACION BASE ES  "+str(float(((count_vulnibm_iot_adjacentaccesvector_risklevel+count_vulnibm_sh_adjacentaccesvector_risklevel)/(count_vulnibm_iot_adjacentaccesvector+count_vulnibm_sh_adjacentaccesvector))))+"\n")
    print("\n")


if((count_vulnibm_iot_physicalaccesvector+count_vulnibm_sh_physicalaccesvector)>0):
    print("      -    EN EL "+str(float((((count_vulnibm_iot_physicalaccesvector+count_vulnibm_sh_physicalaccesvector)*100)/(count_vulnibm_iot_access_vector+count_vulnibm_sh_access_vector))))+" % DE VULNERABILIDADES EL VECTOR  DE ACCESO ES FÍSICO, LOS PORCENTAJES DE PUNTUACION BASE SON LOS SIGUIENTES :  \n")
    print("            -    EN EL"+str(float((((count_vulnibm_iot_physicalaccesvector_risklevel10+count_vulnibm_sh_physicalaccesvector_risklevel10)*100)/(count_vulnibm_iot_physicalaccesvector+count_vulnibm_sh_physicalaccesvector))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
    print("            -    EN EL "+str(float((((count_vulnibm_iot_physicalaccesvector_risklevel9+count_vulnibm_sh_physicalaccesvector_risklevel9)*100)/(count_vulnibm_iot_physicalaccesvector+count_vulnibm_sh_physicalaccesvector))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
    print("            -    EN EL "+str(float((((count_vulnibm_iot_physicalaccesvector_risklevel8+count_vulnibm_sh_physicalaccesvector_risklevel8)*100)/(count_vulnibm_iot_physicalaccesvector+count_vulnibm_sh_physicalaccesvector))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
    print("            -    EN EL "+str(float((((count_vulnibm_iot_physicalaccesvector_risklevel7+count_vulnibm_sh_physicalaccesvector_risklevel7)*100)/(count_vulnibm_iot_physicalaccesvector+count_vulnibm_sh_physicalaccesvector))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
    print("            -    EN EL "+str(float((((count_vulnibm_iot_physicalaccesvector_risklevel6+count_vulnibm_sh_physicalaccesvector_risklevel6)*100)/(count_vulnibm_iot_physicalaccesvector+count_vulnibm_sh_physicalaccesvector))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
    print("            -    EN EL "+str(float((((count_vulnibm_iot_physicalaccesvector_risklevel5+count_vulnibm_sh_physicalaccesvector_risklevel5)*100)/(count_vulnibm_iot_physicalaccesvector+count_vulnibm_sh_physicalaccesvector))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
    print("            -    EN EL "+str(float((((count_vulnibm_iot_physicalaccesvector_risklevel4+count_vulnibm_sh_physicalaccesvector_risklevel4)*100)/(count_vulnibm_iot_physicalaccesvector+count_vulnibm_sh_physicalaccesvector))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
    print("            -    EN EL "+str(float((((count_vulnibm_iot_physicalaccesvector_risklevel3+count_vulnibm_sh_physicalaccesvector_risklevel3)*100)/(count_vulnibm_iot_physicalaccesvector+count_vulnibm_sh_physicalaccesvector))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
    print("            -    EN EL "+str(float((((count_vulnibm_iot_physicalaccesvector_risklevel2+count_vulnibm_sh_physicalaccesvector_risklevel2)*100)/(count_vulnibm_iot_physicalaccesvector+count_vulnibm_sh_physicalaccesvector))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
    print("            -    EN EL "+str(float((((count_vulnibm_iot_physicalaccesvector_risklevel1+count_vulnibm_sh_physicalaccesvector_risklevel1)*100)/(count_vulnibm_iot_physicalaccesvector+count_vulnibm_sh_physicalaccesvector))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
    print("            -    EN EL "+str(float((((count_vulnibm_iot_physicalaccesvector_risklevel0+count_vulnibm_sh_physicalaccesvector_risklevel0)*100)/(count_vulnibm_iot_physicalaccesvector+count_vulnibm_sh_physicalaccesvector))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
    print("            -    EL VALOR MEDIO DE PUNTUACION BASE ES  "+str(float(((count_vulnibm_iot_physicalaccesvector_risklevel+count_vulnibm_sh_physicalaccesvector_risklevel)/(count_vulnibm_iot_physicalaccesvector+count_vulnibm_sh_physicalaccesvector))))+"\n")
    print("\n")

















