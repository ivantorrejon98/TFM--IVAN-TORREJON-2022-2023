
import pandas as pd
from datetime import datetime,timedelta



#Abro los ficheros con los que voy a tratar
df_vulnibm_iot = pd.read_excel('vulnerabilidades_ibm_iot_2023.xlsx')

#Variable donde almacenare el contador total de vulnerabilidades
count_total_ibm_iot=0
#Variables donde almacenare el contador total de valores de un valor especifico de complejidad de ATAQUE
count_high_comacc_ibm_iot=0
#Variables donde almacenare el contador de valores de VECTOR DE ATAQUE para un valor de complejidad de ATAQUE especifico
count_high_comacc_network_vecacc_ibm_iot=0
count_high_comacc_Local_vecacc_ibm_iot=0
count_high_comacc_Physical_vecacc_ibm_iot=0
count_high_comacc_Adjnet_vecacc_ibm_iot=0
count_high_comacc_none_vecacc_ibm_iot=0


count_low_comacc_ibm_iot=0
count_low_comacc_network_vecacc_ibm_iot=0
count_low_comacc_Local_vecacc_ibm_iot=0
count_low_comacc_Physical_vecacc_ibm_iot=0
count_low_comacc_Adjnet_vecacc_ibm_iot=0
count_low_comacc_none_vecacc_ibm_iot=0


#Recorro los valores de COMPLEJIDAD DE ATAQUE y aumento los contadores segun su valor

for r in range(0,len(df_vulnibm_iot["x_xfe_cvss_access_complexity"])):
    #Compruebo el nivel de complejidad de ATAQUE
    if(df_vulnibm_iot["x_xfe_cvss_access_complexity"][r]=='High'):
        count_total_ibm_iot+=1
        count_high_comacc_ibm_iot+=1
        #Compruebo el VECTOR DE ATAQUE
        if(df_vulnibm_iot["x_xfe_cvss_access_vector"][r]=='Network'):
            count_high_comacc_network_vecacc_ibm_iot+=1
        elif(df_vulnibm_iot["x_xfe_cvss_access_vector"][r]=='Local'):
            count_high_comacc_Local_vecacc_ibm_iot+=1
        elif(df_vulnibm_iot["x_xfe_cvss_access_vector"][r]=='Physical'):
            count_high_comacc_Physical_vecacc_ibm_iot+=1
        elif(df_vulnibm_iot["x_xfe_cvss_access_vector"][r]=='Adjacent Network'):
            count_high_comacc_Adjnet_vecacc_ibm_iot+=1
        else:
            count_high_comacc_none_vecacc_ibm_iot+=1
    elif(df_vulnibm_iot["x_xfe_cvss_access_complexity"][r]=='Low'):
        count_total_ibm_iot+=1
        count_low_comacc_ibm_iot+=1
        if(df_vulnibm_iot["x_xfe_cvss_access_vector"][r]=='Network'):
            count_low_comacc_network_vecacc_ibm_iot+=1
        elif(df_vulnibm_iot["x_xfe_cvss_access_vector"][r]=='Local'):
            count_low_comacc_Local_vecacc_ibm_iot+=1
        elif(df_vulnibm_iot["x_xfe_cvss_access_vector"][r]=='Physical'):
            count_low_comacc_Physical_vecacc_ibm_iot+=1
        elif(df_vulnibm_iot["x_xfe_cvss_access_vector"][r]=='Adjacent Network'):
            count_low_comacc_Adjnet_vecacc_ibm_iot+=1
        else:
            count_low_comacc_none_vecacc_ibm_iot+=1
         
            
            
print("********************ESTADÍSTICAS COMPLEJIDAD DE ATAQUE/VECTOR DE ATAQUE IBM PARTE IOT********************")
print("\n")                            
print("\n")
print(" DE UN TOTAL DE "+str(count_total_ibm_iot)+" VULNERABILIDADES:\n") 
print("\n")
print("   - LAS ESTADISTICAS DE VALORES DE COMPLEJIDAD DE ATAQUE SON LAS SIGUIENTES:  \n")
print("      -    EN  "+str(count_high_comacc_ibm_iot)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA, LAS ESTADÍSTICAS DE VECTOR DE ATAQUE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_high_comacc_network_vecacc_ibm_iot)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES LA RED \n")
print("            -    EN  "+str(count_high_comacc_Local_vecacc_ibm_iot)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES LOCAL \n")
print("            -    EN  "+str(count_high_comacc_Physical_vecacc_ibm_iot)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES FÍSICO \n")
print("            -    EN  "+str(count_high_comacc_Adjnet_vecacc_ibm_iot)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES UNA RED ADYACENTE \n")
print("            -    EN  "+str(count_high_comacc_none_vecacc_ibm_iot)+" VULNERABILIDADES EL VECTOR DE ATAQUE NO VIENE ESPECIFICADO \n")
print("      -    EN  "+str(count_low_comacc_ibm_iot)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA, LAS ESTADÍSTICAS DE VECTOR DE ATAQUE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_low_comacc_network_vecacc_ibm_iot)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES LA RED \n")
print("            -    EN  "+str(count_low_comacc_Local_vecacc_ibm_iot)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES LOCAL \n")
print("            -    EN  "+str(count_low_comacc_Physical_vecacc_ibm_iot)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES FÍSICO \n")
print("            -    EN  "+str(count_low_comacc_Adjnet_vecacc_ibm_iot)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES UNA RED ADYACENTE \n")
print("            -    EN  "+str(count_low_comacc_none_vecacc_ibm_iot)+" VULNERABILIDADES EL VECTOR DE ATAQUE NO VIENE ESPECIFICADO \n")


print("********************PORCENTAJE COMPLEJIDAD DE ATAQUE/VECTOR DE ATAQUE VULNERABILIDADES IBM PARTE IOT********************")
print("\n")                            
print("\n")
print(" DE UN TOTAL DE "+str(count_total_ibm_iot)+" VULNERABILIDADES :\n") 
print("\n")
print("   - LOS PORCENTAJES DE VALORES DE COMPLEJIDAD DE ATAQUE SON LOS SIGUIENTES:  \n")
print("      -    EN EL  "+str(float(((count_high_comacc_ibm_iot*100)/count_total_ibm_iot)))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA, LOS PORCENTAJES DE VECTOR DE ATAQUE SON LOS SIGUIENTES :  \n")
print("            -    EN EL  "+str(float(((count_high_comacc_network_vecacc_ibm_iot*100)/count_high_comacc_ibm_iot)))+" % DE VULNERABILIDADES EL VECTOR DE ATAQUE ES LA RED \n")
print("            -    EN EL  "+str(float(((count_high_comacc_Local_vecacc_ibm_iot*100)/count_high_comacc_ibm_iot)))+" % DE VULNERABILIDADES EL VECTOR DE ATAQUE ES LOCAL \n")
print("            -    EN EL  "+str(float(((count_high_comacc_Physical_vecacc_ibm_iot*100)/count_high_comacc_ibm_iot)))+" % DE VULNERABILIDADES EL VECTOR DE ATAQUE ES FÍSICO \n")
print("            -    EN EL  "+str(float(((count_high_comacc_Adjnet_vecacc_ibm_iot*100)/count_high_comacc_ibm_iot)))+" % DE VULNERABILIDADES EL VECTOR DE ATAQUE ES UNA RED ADYACENTE \n")
print("            -    EN EL  "+str(float(((count_high_comacc_none_vecacc_ibm_iot*100)/count_high_comacc_ibm_iot)))+" % DE VULNERABILIDADES EL VECTOR DE ATAQUE NO VIENE ESPECIFICADO \n")
print("      -    EN EL  "+str(float(((count_low_comacc_ibm_iot*100)/count_total_ibm_iot)))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA, LOS PORCENTAJES  DE VECTOR DE ATAQUE SON LOS SIGUIENTES :  \n")
print("            -    EN EL  "+str(float(((count_low_comacc_network_vecacc_ibm_iot*100)/count_low_comacc_ibm_iot)))+" % DE VULNERABILIDADES EL VECTOR DE ATAQUE ES LA RED \n")
print("            -    EN EL  "+str(float(((count_low_comacc_Local_vecacc_ibm_iot*100)/count_low_comacc_ibm_iot)))+" % DE VULNERABILIDADES EL VECTOR DE ATAQUE ES LOCAL \n")
print("            -    EN EL  "+str(float(((count_low_comacc_Physical_vecacc_ibm_iot*100)/count_low_comacc_ibm_iot)))+" % DE VULNERABILIDADES EL VECTOR DE ATAQUE ES FÍSICO \n")
print("            -    EN EL  "+str(float(((count_low_comacc_Adjnet_vecacc_ibm_iot*100)/count_low_comacc_ibm_iot)))+" % DE VULNERABILIDADES EL VECTOR DE ATAQUE ES UNA RED ADYACENTE \n")
print("            -    EN EL  "+str(float(((count_low_comacc_none_vecacc_ibm_iot*100)/count_low_comacc_ibm_iot)))+" % DE VULNERABILIDADES EL VECTOR DE ATAQUE NO VIENE ESPECIFICADO \n")

    
    
    
    
    
    
    
    
    



df_vulnibm_sh = pd.read_excel('vulnerabilidades_ibm_smart_home_2023.xlsx')

#Variable donde almacenare el contador total de vulnerabilidades
count_total_ibm_sh=0
#Variables donde almacenare el contador total de valores de un valor especifico de complejidad de ATAQUE
count_high_comacc_ibm_sh=0
#Variables donde almacenare el contador de valores de VECTOR DE ATAQUE para un valor de complejidad de ATAQUE especifico
count_high_comacc_network_vecacc_ibm_sh=0
count_high_comacc_Local_vecacc_ibm_sh=0
count_high_comacc_Physical_vecacc_ibm_sh=0
count_high_comacc_Adjnet_vecacc_ibm_sh=0
count_high_comacc_none_vecacc_ibm_sh=0


count_low_comacc_ibm_sh=0
count_low_comacc_network_vecacc_ibm_sh=0
count_low_comacc_Local_vecacc_ibm_sh=0
count_low_comacc_Physical_vecacc_ibm_sh=0
count_low_comacc_Adjnet_vecacc_ibm_sh=0
count_low_comacc_none_vecacc_ibm_sh=0



#Recorro los valores de COMPLEJIDAD DE ATAQUE y aumento los contadores segun su valor

for r in range(0,len(df_vulnibm_sh["x_xfe_cvss_access_complexity"])):
    if(df_vulnibm_sh["x_xfe_cvss_access_complexity"][r]=='High'):
        count_total_ibm_sh+=1
        count_high_comacc_ibm_sh+=1
        if(df_vulnibm_sh["x_xfe_cvss_access_vector"][r]=='Network'):
            count_high_comacc_network_vecacc_ibm_sh+=1
        elif(df_vulnibm_sh["x_xfe_cvss_access_vector"][r]=='Local'):
            count_high_comacc_Local_vecacc_ibm_sh+=1
        elif(df_vulnibm_sh["x_xfe_cvss_access_vector"][r]=='Physical'):
            count_high_comacc_Physical_vecacc_ibm_sh+=1
        elif(df_vulnibm_sh["x_xfe_cvss_access_vector"][r]=='Adjacent Network'):
            count_high_comacc_Adjnet_vecacc_ibm_sh+=1
        else:
            count_high_comacc_none_vecacc_ibm_sh+=1
    elif(df_vulnibm_sh["x_xfe_cvss_access_complexity"][r]=='Low'):
        count_total_ibm_sh+=1
        count_low_comacc_ibm_sh+=1
        if(df_vulnibm_sh["x_xfe_cvss_access_vector"][r]=='Network'):
            count_low_comacc_network_vecacc_ibm_sh+=1
        elif(df_vulnibm_sh["x_xfe_cvss_access_vector"][r]=='Local'):
            count_low_comacc_Local_vecacc_ibm_sh+=1
        elif(df_vulnibm_sh["x_xfe_cvss_access_vector"][r]=='Physical'):
            count_low_comacc_Physical_vecacc_ibm_sh+=1
        elif(df_vulnibm_sh["x_xfe_cvss_access_vector"][r]=='Adjacent Network'):
            count_low_comacc_Adjnet_vecacc_ibm_sh+=1
        else:
            count_low_comacc_none_vecacc_ibm_sh+=1
           
            
print("********************ESTADÍSTICAS COMPLEJIDAD DE ATAQUE/VECTOR DE ATAQUE IBM PARTE SMART HOME********************")
print("\n")                            
print("\n")
print(" DE UN TOTAL DE "+str(count_total_ibm_sh)+" VULNERABILIDADES:\n") 
print("\n")
print("   - LAS ESTADISTICAS DE VALORES DE COMPLEJIDAD DE ATAQUE SON LAS SIGUIENTES:  \n")
print("      -    EN  "+str(count_high_comacc_ibm_sh)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA, LAS ESTADÍSTICAS DE VECTOR DE ATAQUE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_high_comacc_network_vecacc_ibm_sh)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES LA RED \n")
print("            -    EN  "+str(count_high_comacc_Local_vecacc_ibm_sh)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES LOCAL \n")
print("            -    EN  "+str(count_high_comacc_Physical_vecacc_ibm_sh)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES FÍSICO \n")
print("            -    EN  "+str(count_high_comacc_Adjnet_vecacc_ibm_sh)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES UNA RED ADYACENTE \n")
print("            -    EN  "+str(count_high_comacc_none_vecacc_ibm_sh)+" VULNERABILIDADES EL VECTOR DE ATAQUE NO VIENE ESPECIFICADO \n")
print("      -    EN  "+str(count_low_comacc_ibm_sh)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA, LAS ESTADÍSTICAS DE VECTOR DE ATAQUE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_low_comacc_network_vecacc_ibm_sh)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES LA RED \n")
print("            -    EN  "+str(count_low_comacc_Local_vecacc_ibm_sh)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES LOCAL \n")
print("            -    EN  "+str(count_low_comacc_Physical_vecacc_ibm_sh)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES FÍSICO \n")
print("            -    EN  "+str(count_low_comacc_Adjnet_vecacc_ibm_sh)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES UNA RED ADYACENTE \n")
print("            -    EN  "+str(count_low_comacc_none_vecacc_ibm_sh)+" VULNERABILIDADES EL VECTOR DE ATAQUE NO VIENE ESPECIFICADO \n")


print("********************PORCENTAJE COMPLEJIDAD DE ATAQUE/VECTOR DE ATAQUE VULNERABILIDADES IBM PARTE SMART HOME********************")
print("\n")                            
print("\n")
print(" DE UN TOTAL DE "+str(count_total_ibm_sh)+" VULNERABILIDADES :\n") 
print("\n")
print("   - LOS PORCENTAJES DE VALORES DE COMPLEJIDAD DE ATAQUE SON LOS SIGUIENTES:  \n")
print("      -    EN EL  "+str(float(((count_high_comacc_ibm_sh*100)/count_total_ibm_sh)))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA, LOS PORCENTAJES  DE VECTOR DE ATAQUE SON LOS SIGUIENTES :  \n")
print("            -    EN EL  "+str(float(((count_high_comacc_network_vecacc_ibm_sh*100)/count_high_comacc_ibm_sh)))+" % DE VULNERABILIDADES EL VECTOR DE ATAQUE ES LA RED \n")
print("            -    EN EL  "+str(float(((count_high_comacc_Local_vecacc_ibm_sh*100)/count_high_comacc_ibm_sh)))+" % DE VULNERABILIDADES EL VECTOR DE ATAQUE ES LOCAL \n")
print("            -    EN EL  "+str(float(((count_high_comacc_Physical_vecacc_ibm_sh*100)/count_high_comacc_ibm_sh)))+" % DE VULNERABILIDADES EL VECTOR DE ATAQUE ES FÍSICO \n")
print("            -    EN EL  "+str(float(((count_high_comacc_Adjnet_vecacc_ibm_sh*100)/count_high_comacc_ibm_sh)))+" % DE VULNERABILIDADES EL VECTOR DE ATAQUE ES UNA RED ADYACENTE \n")
print("            -    EN EL  "+str(float(((count_high_comacc_none_vecacc_ibm_sh*100)/count_high_comacc_ibm_sh)))+" % DE VULNERABILIDADES EL VECTOR DE ATAQUE NO VIENE ESPECIFICADO \n")
print("      -    EN EL  "+str(float(((count_low_comacc_ibm_sh*100)/count_total_ibm_sh)))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA, LOS PORCENTAJES  DE VECTOR DE ATAQUE SON LOS SIGUIENTES :  \n")
print("            -    EN EL  "+str(float(((count_low_comacc_network_vecacc_ibm_sh*100)/count_low_comacc_ibm_sh)))+" % DE VULNERABILIDADES EL VECTOR DE ATAQUE ES LA RED \n")
print("            -    EN EL  "+str(float(((count_low_comacc_Local_vecacc_ibm_sh*100)/count_low_comacc_ibm_sh)))+" % DE VULNERABILIDADES EL VECTOR DE ATAQUE ES LOCAL \n")
print("            -    EN EL  "+str(float(((count_low_comacc_Physical_vecacc_ibm_sh*100)/count_low_comacc_ibm_sh)))+" % DE VULNERABILIDADES EL VECTOR DE ATAQUE ES FÍSICO \n")
print("            -    EN EL  "+str(float(((count_low_comacc_Adjnet_vecacc_ibm_sh*100)/count_low_comacc_ibm_sh)))+" % DE VULNERABILIDADES EL VECTOR DE ATAQUE ES UNA RED ADYACENTE \n")
print("            -    EN EL  "+str(float(((count_low_comacc_none_vecacc_ibm_sh*100)/count_low_comacc_ibm_sh)))+" % DE VULNERABILIDADES EL VECTOR DE ATAQUE NO VIENE ESPECIFICADO \n")
 
    
    
print("********************ESTADÍSTICAS COMPLEJIDAD DE ATAQUE/ACCES VECTOR VULNERABILIDADES IBM PARTE IOT Y SMART HOME CONJUNTAS********************")
print("\n")                            
print("\n")
print(" DE UN TOTAL DE "+str(count_total_ibm_sh+count_total_ibm_iot)+" VULNERABILIDADES:\n") 
print("\n")
print("   - LAS ESTADISTICAS DE VALORES DE COMPLEJIDAD DE ATAQUE SON LAS SIGUIENTES:  \n")
print("      -    EN  "+str(count_high_comacc_ibm_sh+count_high_comacc_ibm_iot)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA, LAS ESTADÍSTICAS DE VECTOR DE ATAQUE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_high_comacc_network_vecacc_ibm_sh+count_high_comacc_network_vecacc_ibm_iot)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES LA RED \n")
print("            -    EN  "+str(count_high_comacc_Local_vecacc_ibm_sh+count_high_comacc_Local_vecacc_ibm_iot)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES LOCAL \n")
print("            -    EN  "+str(count_high_comacc_Physical_vecacc_ibm_sh+count_high_comacc_Physical_vecacc_ibm_iot)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES FÍSICO \n")
print("            -    EN  "+str(count_high_comacc_Adjnet_vecacc_ibm_sh+count_high_comacc_Adjnet_vecacc_ibm_iot)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES UNA RED ADYACENTE \n")
print("            -    EN  "+str(count_high_comacc_none_vecacc_ibm_sh+count_high_comacc_none_vecacc_ibm_iot)+" VULNERABILIDADES EL VECTOR DE ATAQUE NO VIENE ESPECIFICADO \n")    
print("      -    EN  "+str(count_low_comacc_ibm_sh+count_low_comacc_ibm_iot)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA, LAS ESTADÍSTICAS DE VECTOR DE ATAQUE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_low_comacc_network_vecacc_ibm_sh+count_low_comacc_network_vecacc_ibm_iot)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES LA RED \n")
print("            -    EN  "+str(count_low_comacc_Local_vecacc_ibm_sh+count_low_comacc_Local_vecacc_ibm_iot)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES LOCAL \n")
print("            -    EN  "+str(count_low_comacc_Physical_vecacc_ibm_sh+count_low_comacc_Physical_vecacc_ibm_iot)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES FÍSICO \n")
print("            -    EN  "+str(count_low_comacc_Adjnet_vecacc_ibm_sh+count_low_comacc_Adjnet_vecacc_ibm_iot)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES UNA RED ADYACENTE \n")
print("            -    EN  "+str(count_low_comacc_none_vecacc_ibm_sh+count_low_comacc_none_vecacc_ibm_iot)+" VULNERABILIDADES EL VECTOR DE ATAQUE NO VIENE ESPECIFICADO \n")    

print("********************PORCENTAJES COMPLEJIDAD DE ATAQUE/VECTOR DE ATAQUE VULNERABILIDADES IBM PARTE IOT Y SMART HOME********************")
print("\n")                            
print("\n")
print(" DE UN TOTAL DE "+str(count_total_ibm_sh+count_total_ibm_iot)+" VULNERABILIDADES :\n") 
print("\n")
print("   - LOS PORCENTAJES DE VALORES DE COMPLEJIDAD DE ATAQUE SON LOS SIGUIENTES:  \n")
print("      -    EN EL "+str(float((((count_high_comacc_ibm_sh+count_high_comacc_ibm_iot)*100)/(count_total_ibm_sh+count_total_ibm_iot))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA, LOS PORCENTAJES DE VECTOR DE ATAQUE SON LOS SIGUIENTES :  \n")
print("            -    EN EL"+str(float((((count_high_comacc_network_vecacc_ibm_sh+count_high_comacc_network_vecacc_ibm_iot)*100)/(count_high_comacc_ibm_sh+count_high_comacc_ibm_iot))))+" % DE VULNERABILIDADES EL VECTOR DE ATAQUE ES LA RED \n")
print("            -    EN EL "+str(float((((count_high_comacc_Local_vecacc_ibm_sh+count_high_comacc_Local_vecacc_ibm_iot)*100)/(count_high_comacc_ibm_sh+count_high_comacc_ibm_iot))))+" % DE VULNERABILIDADES EL VECTOR DE ATAQUE ES LOCAL \n")
print("            -    EN EL "+str(float((((count_high_comacc_Physical_vecacc_ibm_sh+count_high_comacc_Physical_vecacc_ibm_iot)*100)/(count_high_comacc_ibm_sh+count_high_comacc_ibm_iot))))+" % DE VULNERABILIDADES EL VECTOR DE ATAQUE ES FÍSICO \n")
print("            -    EN EL "+str(float((((count_high_comacc_Adjnet_vecacc_ibm_sh+count_high_comacc_Adjnet_vecacc_ibm_iot)*100)/(count_high_comacc_ibm_sh+count_high_comacc_ibm_iot))))+" % DE VULNERABILIDADES EL VECTOR DE ATAQUE ES UNA RED ADYACENTE \n")
print("            -    EN EL "+str(float((((count_high_comacc_none_vecacc_ibm_sh+count_high_comacc_none_vecacc_ibm_iot)*100)/(count_high_comacc_ibm_sh+count_high_comacc_ibm_iot))))+" % DE VULNERABILIDADES EL VECTOR DE ATAQUE NO VIENE ESPECIFICADO \n")
print("      -    EN EL "+str(float((((count_low_comacc_ibm_sh+count_low_comacc_ibm_iot)*100)/(count_total_ibm_sh+count_total_ibm_iot))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA, LOS PORCENTAJES DE VECTOR DE ATAQUE SON LOS SIGUIENTES :  \n")
print("            -    EN EL"+str(float((((count_low_comacc_network_vecacc_ibm_sh+count_low_comacc_network_vecacc_ibm_iot)*100)/(count_low_comacc_ibm_sh+count_low_comacc_ibm_iot))))+" % DE VULNERABILIDADES EL VECTOR DE ATAQUE ES LA RED \n")
print("            -    EN EL "+str(float((((count_low_comacc_Local_vecacc_ibm_sh+count_low_comacc_Local_vecacc_ibm_iot)*100)/(count_low_comacc_ibm_sh+count_low_comacc_ibm_iot))))+" % DE VULNERABILIDADES EL VECTOR DE ATAQUE ES LOCAL \n")
print("            -    EN EL "+str(float((((count_low_comacc_Physical_vecacc_ibm_sh+count_low_comacc_Physical_vecacc_ibm_iot)*100)/(count_low_comacc_ibm_sh+count_low_comacc_ibm_iot))))+" % DE VULNERABILIDADES EL VECTOR DE ATAQUE ES FÍSICO \n")
print("            -    EN EL "+str(float((((count_low_comacc_Adjnet_vecacc_ibm_sh+count_low_comacc_Adjnet_vecacc_ibm_iot)*100)/(count_low_comacc_ibm_sh+count_low_comacc_ibm_iot))))+" % DE VULNERABILIDADES EL VECTOR DE ATAQUE ES UNA RED ADYACENTE \n")
print("            -    EN EL "+str(float((((count_low_comacc_none_vecacc_ibm_sh+count_low_comacc_none_vecacc_ibm_iot)*100)/(count_low_comacc_ibm_sh+count_low_comacc_ibm_iot))))+" % DE VULNERABILIDADES EL VECTOR DE ATAQUE NO VIENE ESPECIFICADO \n")

















































