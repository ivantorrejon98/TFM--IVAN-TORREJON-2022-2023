	
import pandas as pd
from datetime import datetime,timedelta



#Abro los ficheros con los que voy a tratar




df_vulnibm_iot = pd.read_excel('vulnerabilidades_ibm_iot_2023.xlsx')

#Variables donde almacenare el contador total de valores de complejidad de ATAQUE

count_comacc_vulnibm_iot=0

#Variables donde almacenare el contador de valores de impacto de INTEGRIDAD dado un valor especifico de complejidad de ATAQUE
count_high_comacc_highintimpact_vulnibm_iot=0
count_high_comacc_lowintimpact_vulnibm_iot=0
#Variable para almacenar el contador total de valores de una complejidad de ATAQUE especifica
count_high_comacc_vulnibm_iot=0
#Variable para almacenar el contador total de valores especificados para una complejidad de ATAQUE especifica
count_high_comacc_vulnibm_iot_specified=0


count_low_comacc_highintimpact_vulnibm_iot=0
count_low_comacc_lowintimpact_vulnibm_iot=0
count_low_comacc_vulnibm_iot=0
count_low_comacc_vulnibm_iot_specified=0


#Recorro los valores de COMPLEJIDAD DE ATAQUE y aumento los contadores segun su valor

for r in range(0,len(df_vulnibm_iot["x_xfe_cvss_access_complexity"])):                       
    aux_str=df_vulnibm_iot["x_xfe_cvss_access_complexity"][r].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
    if(aux_str!='NONE' or aux_str!='None'):
        count_comacc_vulnibm_iot+=1
        #Compruebo el valor de complejidad de ATAQUE
        if('High' in aux_str):
            count_high_comacc_vulnibm_iot+=1
            #Compruebo el valor de impacto de INTEGRIDAD
            if(df_vulnibm_iot["x_xfe_cvss_integrity_impact"][r]=='High'):
                count_high_comacc_vulnibm_iot_specified+=1
                count_high_comacc_highintimpact_vulnibm_iot+=1
            elif(df_vulnibm_iot["x_xfe_cvss_integrity_impact"][r]=='Low'):
                count_high_comacc_vulnibm_iot_specified+=1
                count_high_comacc_lowintimpact_vulnibm_iot+=1

        elif('Low' in aux_str):
            count_low_comacc_vulnibm_iot+=1
            if(df_vulnibm_iot["x_xfe_cvss_integrity_impact"][r]=='High'):
                count_low_comacc_vulnibm_iot_specified+=1
                count_low_comacc_highintimpact_vulnibm_iot+=1
            elif(df_vulnibm_iot["x_xfe_cvss_integrity_impact"][r]=='Low'):
                count_low_comacc_vulnibm_iot_specified+=1
                count_low_comacc_lowintimpact_vulnibm_iot+=1

    
                
                
                
                
                
                
                
                
print("**************************ESTADÍSTICAS COMPLEJIDAD DE ATAQUE/IMPACTO DE INTEGRIDAD VULNERABILIDADES IBM PARTE IOT**************************")
print("\n")                            
print("\n")
print(" DE UN TOTAL DE "+str(count_comacc_vulnibm_iot)+" VULNERABILIDADES DONDE LA COMPLEJIDAD DE ATAQUE VIENE ESPECIFICADA:\n") 
print("\n")
print("   - LAS ESTADISTICAS DE COMPLEJIDAD DE ATAQUE SON LAS SIGUIENTES:  \n")
print("      -    EN  "+str(count_high_comacc_vulnibm_iot)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA. EL IMPACTO DE INTEGRIDAD VIENE ESPECIFICADO ES  "+str(count_high_comacc_vulnibm_iot_specified)+" VULNERABILIDADES. LAS ESTADÍSTICAS DE IMPACTO DE INTEGRIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_high_comacc_highintimpact_vulnibm_iot)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
print("            -    EN  "+str(count_high_comacc_lowintimpact_vulnibm_iot)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
print("\n")
print("      -    EN  "+str(count_low_comacc_vulnibm_iot)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA. EL IMPACTO DE INTEGRIDAD VIENE ESPECIFICADO ES  "+str(count_low_comacc_vulnibm_iot_specified)+" VULNERABILIDADES. LAS ESTADÍSTICAS DE IMPACTO DE INTEGRIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_low_comacc_highintimpact_vulnibm_iot)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
print("            -    EN  "+str(count_low_comacc_lowintimpact_vulnibm_iot)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
print("\n")
print("\n")
print("\n")




print("**************************PORCENTAJES COMPLEJIDAD DE ATAQUE/IMPACTO DE INTEGRIDAD VULNERABILIDADES IBM PARTE IOT  **************************")
print("\n")                            
print("\n")
print(" DE UN TOTAL DE "+str(count_comacc_vulnibm_iot)+" VULNERABILIDADES :\n") 
print("\n")
print("   - LOS PORCENTAJES DE COMPLEJIDAD DE ATAQUE SON LOS SIGUIENTES:  \n")
if(count_high_comacc_vulnibm_iot>0):
    print("      -    EN EL "+str(float((count_high_comacc_vulnibm_iot*100)/count_comacc_vulnibm_iot))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA. EL IMPACTO DE INTEGRIDAD VIENE ESPECIFICADO EN EL "+str(float((count_high_comacc_vulnibm_iot_specified*100)/count_high_comacc_vulnibm_iot))+" % DE ELLAS. LOS PORCENTAJES DE IMPACTO DE INTEGRIDAD SON LOS SIGUIENTES :  \n")
    print("            -    EN EL "+str(float((count_high_comacc_highintimpact_vulnibm_iot*100)/count_high_comacc_vulnibm_iot))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
    print("            -    EN EL "+str(float((count_high_comacc_lowintimpact_vulnibm_iot*100)/count_high_comacc_vulnibm_iot))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
    print("\n")
if(count_low_comacc_vulnibm_iot>0):
    print("      -    EN EL "+str(float((count_low_comacc_vulnibm_iot*100)/count_comacc_vulnibm_iot))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA. EL IMPACTO DE INTEGRIDAD VIENE ESPECIFICADO EN EL "+str(float((count_low_comacc_vulnibm_iot_specified*100)/count_low_comacc_vulnibm_iot))+" % DE ELLAS. LOS PORCENTAJES DE IMPACTO DE INTEGRIDAD SON LOS SIGUIENTES :  \n")
    print("            -    EN EL "+str(float((count_low_comacc_highintimpact_vulnibm_iot*100)/count_low_comacc_vulnibm_iot))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
    print("            -    EN EL "+str(float((count_low_comacc_lowintimpact_vulnibm_iot*100)/count_low_comacc_vulnibm_iot))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")

    print("\n")

    
    
    
    
    
    
    
    
    
#Abro los ficheros con los que voy a tratar




df_vulnibm_sh = pd.read_excel('vulnerabilidades_ibm_smart_home_2023.xlsx')



#Variables donde almacenare el contador total de valores de complejidad de ATAQUE

count_comacc_vulnibm_sh=0

#Variables donde almacenare el contador de valores de impacto de INTEGRIDAD dado un valor especifico de complejidad de ATAQUE
count_high_comacc_highintimpact_vulnibm_sh=0
count_high_comacc_lowintimpact_vulnibm_sh=0
#Variable para almacenar el contador total de valores de una complejidad de ATAQUE especifica
count_high_comacc_vulnibm_sh=0
#Variable para almacenar el contador total de valores especificados para una complejidad de ATAQUE especifica
count_high_comacc_vulnibm_sh_specified=0


count_low_comacc_highintimpact_vulnibm_sh=0
count_low_comacc_lowintimpact_vulnibm_sh=0
count_low_comacc_vulnibm_sh=0
count_low_comacc_vulnibm_sh_specified=0


#Recorro los valores de COMPLEJIDAD DE ATAQUE y aumento los contadores segun su valor

for r in range(0,len(df_vulnibm_sh["x_xfe_cvss_access_complexity"])):                       
    aux_str=df_vulnibm_sh["x_xfe_cvss_access_complexity"][r].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
    if(aux_str!='NONE' or aux_str!='None'):
        count_comacc_vulnibm_sh+=1
        #Compruebo el valor de complejidad de ATAQUE
        if('High' in aux_str):
            count_high_comacc_vulnibm_sh+=1
            #Compruebo el valor de impacto de INTEGRIDAD
            if(df_vulnibm_sh["x_xfe_cvss_integrity_impact"][r]=='High'):
                count_high_comacc_vulnibm_sh_specified+=1
                count_high_comacc_highintimpact_vulnibm_sh+=1
            elif(df_vulnibm_sh["x_xfe_cvss_integrity_impact"][r]=='Low'):
                count_high_comacc_vulnibm_sh_specified+=1
                count_high_comacc_lowintimpact_vulnibm_sh+=1
        elif('Low' in aux_str):
            count_low_comacc_vulnibm_sh+=1
            if(df_vulnibm_sh["x_xfe_cvss_integrity_impact"][r]=='High'):
                count_low_comacc_vulnibm_sh_specified+=1
                count_low_comacc_highintimpact_vulnibm_sh+=1
            elif(df_vulnibm_sh["x_xfe_cvss_integrity_impact"][r]=='Low'):
                count_low_comacc_vulnibm_sh_specified+=1
                count_low_comacc_lowintimpact_vulnibm_sh+=1

                
                
                
                
                
                
print("**************************ESTADÍSTICAS COMPLEJIDAD DE ATAQUE/IMPACTO DE INTEGRIDAD VULNERABILIDADES IBM PARTE SMART HOME**************************")
print("\n")                            
print("\n")
print(" DE UN TOTAL DE "+str(count_comacc_vulnibm_sh)+" VULNERABILIDADES DONDE LA COMPLEJIDAD DE ATAQUE VIENE ESPECIFICADA:\n") 
print("\n")
print("   - LAS ESTADISTICAS DE COMPLEJIDAD DE ATAQUE SON LAS SIGUIENTES:  \n")
print("      -    EN  "+str(count_high_comacc_vulnibm_sh)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA. EL IMPACTO DE INTEGRIDAD VIENE ESPECIFICADO ES  "+str(count_high_comacc_vulnibm_sh_specified)+" VULNERABILIDADES. LAS ESTADÍSTICAS DE IMPACTO DE INTEGRIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_high_comacc_highintimpact_vulnibm_sh)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
print("            -    EN  "+str(count_high_comacc_lowintimpact_vulnibm_sh)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
print("\n")
print("      -    EN  "+str(count_low_comacc_vulnibm_sh)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA. EL IMPACTO DE INTEGRIDAD VIENE ESPECIFICADO ES  "+str(count_low_comacc_vulnibm_sh_specified)+" VULNERABILIDADES. LAS ESTADÍSTICAS DE IMPACTO DE INTEGRIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_low_comacc_highintimpact_vulnibm_sh)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
print("            -    EN  "+str(count_low_comacc_lowintimpact_vulnibm_sh)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
print("\n")
print("\n")
print("\n")





print("**************************PORCENTAJES COMPLEJIDAD DE ATAQUE/IMPACTO DE INTEGRIDAD VULNERABILIDADES IBM PARTE SMART HOME**************************")
print("\n")                            
print("\n")
print(" DE UN TOTAL DE "+str(count_comacc_vulnibm_sh)+" VULNERABILIDADES :\n") 
print("\n")
print("   - LOS PORCENTAJES DE COMPLEJIDAD DE ATAQUE SON LOS SIGUIENTES:  \n")
if(count_high_comacc_vulnibm_sh>0):
    print("      -    EN EL "+str(float((count_high_comacc_vulnibm_sh*100)/count_comacc_vulnibm_sh))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA. EL IMPACTO DE INTEGRIDAD VIENE ESPECIFICADO EN EL "+str(float((count_high_comacc_vulnibm_sh_specified*100)/count_high_comacc_vulnibm_sh))+" % DE ELLAS. LOS PORCENTAJES DE IMPACTO DE INTEGRIDAD SON LOS SIGUIENTES :  \n")
    print("            -    EN EL "+str(float((count_high_comacc_highintimpact_vulnibm_sh*100)/count_high_comacc_vulnibm_sh))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
    print("            -    EN EL "+str(float((count_high_comacc_lowintimpact_vulnibm_sh*100)/count_high_comacc_vulnibm_sh))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
    print("\n")
if(count_low_comacc_vulnibm_sh>0):
    print("      -    EN EL "+str(float((count_low_comacc_vulnibm_sh*100)/count_comacc_vulnibm_sh))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA. EL IMPACTO DE INTEGRIDAD VIENE ESPECIFICADO EN EL "+str(float((count_low_comacc_vulnibm_sh_specified*100)/count_low_comacc_vulnibm_sh))+" % DE ELLAS. LOS PORCENTAJES DE IMPACTO DE INTEGRIDAD SON LOS SIGUIENTES :  \n")
    print("            -    EN EL "+str(float((count_low_comacc_highintimpact_vulnibm_sh*100)/count_low_comacc_vulnibm_sh))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
    print("            -    EN EL "+str(float((count_low_comacc_lowintimpact_vulnibm_sh*100)/count_low_comacc_vulnibm_sh))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")

print("\n")
print("\n")
print("\n")

    
    
    
    
    
    
print("**************************ESTADÍSTICAS COMPLEJIDAD DE ATAQUE/IMPACTO DE INTEGRIDAD VULNERABILIDADES IBM PARTE IOT Y SMART HOME CONJUNTAS**************************")
print("\n")                            
print("\n")
print(" DE UN TOTAL DE "+str(count_comacc_vulnibm_sh+count_comacc_vulnibm_iot)+" VULNERABILIDADES DONDE LA COMPLEJIDAD DE ATAQUE VIENE ESPECIFICADA:\n") 
print("\n")
print("   - LAS ESTADISTICAS DE COMPLEJIDAD DE ATAQUE SON LAS SIGUIENTES:  \n")
print("      -    EN  "+str(count_high_comacc_vulnibm_sh+count_high_comacc_vulnibm_iot)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA. EL IMPACTO DE INTEGRIDAD VIENE ESPECIFICADO ES  "+str(count_high_comacc_vulnibm_sh_specified+count_high_comacc_vulnibm_iot_specified)+" VULNERABILIDADES. LAS ESTADÍSTICAS DE IMPACTO DE INTEGRIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_high_comacc_highintimpact_vulnibm_sh+count_high_comacc_highintimpact_vulnibm_iot)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
print("            -    EN  "+str(count_high_comacc_lowintimpact_vulnibm_sh+count_high_comacc_lowintimpact_vulnibm_iot)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
print("\n")
print("      -    EN  "+str(count_low_comacc_vulnibm_sh+count_low_comacc_vulnibm_iot)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA. EL IMPACTO DE INTEGRIDAD VIENE ESPECIFICADO ES  "+str(count_low_comacc_vulnibm_sh_specified+count_low_comacc_vulnibm_iot_specified)+" VULNERABILIDADES. LAS ESTADÍSTICAS DE IMPACTO DE INTEGRIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_low_comacc_highintimpact_vulnibm_sh+count_low_comacc_highintimpact_vulnibm_iot)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
print("            -    EN  "+str(count_low_comacc_lowintimpact_vulnibm_sh+count_low_comacc_lowintimpact_vulnibm_iot)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
print("\n")
print("\n")
print("\n")





print("**************************PORCENTAJES COMPLEJIDAD DE ATAQUE/IMPACTO DE INTEGRIDAD VULNERABILIDADES IBM PARTE IOT Y SMART HOME CONJUNTAS**************************")
print("\n")                            
print("\n")
print(" DE UN TOTAL DE "+str(count_comacc_vulnibm_sh+count_comacc_vulnibm_iot)+" VULNERABILIDADES :\n") 
print("\n")
print("   - LOS PORCENTAJES DE COMPLEJIDAD DE ATAQUE SON LOS SIGUIENTES:  \n")
if((count_high_comacc_vulnibm_sh+count_high_comacc_vulnibm_iot)>0):
    print("      -    EN EL "+str(float(((count_high_comacc_vulnibm_sh+count_high_comacc_vulnibm_iot)*100)/(count_comacc_vulnibm_sh+count_comacc_vulnibm_iot)))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA. EL IMPACTO DE INTEGRIDAD VIENE ESPECIFICADO EN EL "+str(float(((count_high_comacc_vulnibm_sh_specified+count_high_comacc_vulnibm_iot_specified)*100)/(count_high_comacc_vulnibm_sh+count_high_comacc_vulnibm_iot)))+" % DE ELLAS. LOS PORCENTAJES DE IMPACTO DE INTEGRIDAD SON LOS SIGUIENTES :  \n")
    print("            -    EN EL "+str(float(((count_high_comacc_highintimpact_vulnibm_sh+count_high_comacc_highintimpact_vulnibm_iot)*100)/(count_high_comacc_vulnibm_sh+count_high_comacc_vulnibm_iot)))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
    print("            -    EN EL "+str(float(((count_high_comacc_lowintimpact_vulnibm_sh+count_high_comacc_lowintimpact_vulnibm_iot)*100)/(count_high_comacc_vulnibm_sh+count_high_comacc_vulnibm_iot)))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")

    print("\n")
if((count_low_comacc_vulnibm_sh+count_low_comacc_vulnibm_iot)>0):
    print("      -    EN EL "+str(float(((count_low_comacc_vulnibm_sh+count_low_comacc_vulnibm_iot)*100)/(count_comacc_vulnibm_sh+count_comacc_vulnibm_iot)))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA. EL IMPACTO DE INTEGRIDAD VIENE ESPECIFICADO EN EL "+str(float(((count_low_comacc_vulnibm_sh_specified+count_low_comacc_vulnibm_iot_specified)*100)/(count_low_comacc_vulnibm_sh+count_low_comacc_vulnibm_iot)))+" % DE ELLAS. LOS PORCENTAJES DE IMPACTO DE INTEGRIDAD SON LOS SIGUIENTES :  \n")
    print("            -    EN EL "+str(float(((count_low_comacc_highintimpact_vulnibm_sh+count_low_comacc_highintimpact_vulnibm_iot)*100)/(count_low_comacc_vulnibm_sh+count_low_comacc_vulnibm_iot)))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
    print("            -    EN EL "+str(float(((count_low_comacc_lowintimpact_vulnibm_sh+count_low_comacc_lowintimpact_vulnibm_iot)*100)/(count_low_comacc_vulnibm_sh+count_low_comacc_vulnibm_iot)))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
    print("\n")

    
    
