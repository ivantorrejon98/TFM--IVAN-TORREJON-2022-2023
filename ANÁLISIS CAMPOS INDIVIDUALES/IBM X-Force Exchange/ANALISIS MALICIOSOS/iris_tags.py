
import pandas as pd
from datetime import datetime


#Abro los ficheros con los que voy a tratar


df_malw_ana_iot = pd.read_excel('ibm_analisis_maliciosos_iot_2023_v2.xlsx')

#Variable donde almaceno el numero de filas DE NOMBRE
count_total_name_malwareanalysis_iot=len(df_malw_ana_iot["name"])
#Variable para almacenar el contador de entradas DE NOMBRE donde aparece (IRIS)
count_total_name_malwareanalysis_iot_IRIS=0

#Comprobamos si el valor de nombre incluye la cadena IRIS
for r in range(0,len(df_malw_ana_iot["name"])):
    if('IRIS' in df_malw_ana_iot["name"][r] ):  
        count_total_name_malwareanalysis_iot_IRIS+=1
          
                      
print("**************************ESTADÍSTICAS NOMBRE OBJETOS INFORMES ANALISIS MALICIOSOS IBM  PARTE IOT**************************")
print("\n")                            
                
print("\n")
print(" DE UN TOTAL DE "+str(count_total_name_malwareanalysis_iot)+" REGISTROS DE NOMBRE :\n") 
print("\n")
print("      -    UN TOTAL DE  "+str(count_total_name_malwareanalysis_iot_IRIS+1)+" REGISTROS TIENEN COMO FUENTE IRIS   \n")

print("**************************PORCENTAJE NOMBRE OBJETOS INFORMES ANALISIS MALICIOSOS IBM  PARTE IOT**************************")
print("\n")                            
                
print("\n")
print(" DE UN TOTAL DE "+str(count_total_name_malwareanalysis_iot)+" REGISTROS DE NOMBRE:\n") 
print("\n")
print("      -    UN  "+str(float((((count_total_name_malwareanalysis_iot_IRIS+1)*100)/count_total_name_malwareanalysis_iot)))+" % DE REGISTROS TIENEN COMO FUENTE IRIS  \n")













#Abro los ficheros con los que voy a tratar


df_malw_ana_sh = pd.read_excel('ibm_analisis_maliciosos_smarthome_2023.xlsx')
#Variable donde almaceno el numero de filas DE NOMBRE
count_total_name_malwareanalysis_sh=len(df_malw_ana_sh["name"])
#Variable para almacenar el contador de entradas DE NOMBRE donde aparece (IRIS)
count_total_name_malwareanalysis_sh_IRIS=0

#Comprobamos si el valor de nombre incluye la cadena IRIS
for r in range(0,len(df_malw_ana_sh["name"])):
    if('IRIS' in df_malw_ana_sh["name"][r] ):  
        count_total_name_malwareanalysis_sh_IRIS+=1
          
       
                    

        
        
print("**************************ESTADÍSTICAS NOMBRE OBJETOS INFORMES ANALISIS MALICIOSOS IBM  PARTE SMART HOME**************************")
print("\n")                            
                
print("\n")
print(" DE UN TOTAL DE "+str(count_total_name_malwareanalysis_sh)+" REGISTROS DE NOMBRE :\n") 
print("\n")
print("      -    UN TOTAL DE  "+str(count_total_name_malwareanalysis_sh_IRIS)+" REGISTROS TIENEN COMO FUENTE IRIS   \n")

print("**************************PORCENTAJE NOMBRE OBJETOS INFORMES ANALISIS MALICIOSOS IBM  PARTE SMART HOME**************************")
print("\n")                            
                
print("\n")
print(" DE UN TOTAL DE "+str(count_total_name_malwareanalysis_sh)+" REGISTROS DE NOMBRE:\n") 
print("\n")
print("      -    UN "+str(float(((count_total_name_malwareanalysis_sh_IRIS*100)/count_total_name_malwareanalysis_sh)))+" % DE REGISTROS TIENEN COMO FUENTE IRIS  \n")






print("**************************ESTADÍSTICAS NOMBRE OBJETOS INFORMES ANALISIS MALICIOSOS IBM PARTE IOT Y SMART HOME CONJUNTAS  **************************")
print("\n")                            
                
print("\n")
print(" DE UN TOTAL DE "+str(count_total_name_malwareanalysis_sh+count_total_name_malwareanalysis_iot)+" REGISTROS DE NOMBRE :\n") 
print("\n")
print("      -    UN TOTAL DE  "+str(count_total_name_malwareanalysis_sh_IRIS+count_total_name_malwareanalysis_iot_IRIS+1)+" REGISTROS TIENEN COMO FUENTE IRIS   \n")

print("**************************PORCENTAJE NOMBRE OBJETOS INFORMES ANALISIS MALICIOSOS IBM PARTE IOT Y SMART HOME CONJUNTAS **************************")
print("\n")                            
                
print("\n")
print(" DE UN TOTAL DE "+str(count_total_name_malwareanalysis_sh+count_total_name_malwareanalysis_iot)+" REGISTROS DE NOMBRE:\n") 
print("\n")
print("      -    UN "+str(float((((count_total_name_malwareanalysis_sh_IRIS+count_total_name_malwareanalysis_iot_IRIS+1)*100)/(count_total_name_malwareanalysis_sh+count_total_name_malwareanalysis_iot))))+" % DE REGISTROS TIENEN COMO FUENTE IRIS  \n")