import pandas as pd

#Abro los ficheros con los que voy a tratar


df_cpe_iot=pd.read_excel('cpes_iot_2023.xlsx')
df_cpe_sh=pd.read_excel('cpes_smart_home_2023.xlsx')

#Variables donde almacenare el contador de tipo de CPE23URI para IOT
#Contador de cpe23uris de tipo hardware
count_hardwareuri_iot=0
#Contador de cpe23uris de tipo application
count_applicationuri_iot=0
#Contador de cpe23uris de tipo operatingsystem
count_operatingsystemuri_iot=0
#Contador total de cpe23uris
count_totaluri_iot=0

for r in range(0,len(df_cpe_iot["cpes.cpe23Uri"])):
    #Si existen varias cpe23Uris en una misma fila
    if('[' in df_cpe_iot["cpes.cpe23Uri"][r]):
        #Obtengo los valores de cpe23Uris
        aux=df_cpe_iot["cpes.cpe23Uri"][r].split(",")
        #Recorro los valores
        for k in range(0,len(aux)):
            if(len(aux)>0):
                aux_str=aux[k].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
                #Obtengo el valor de type/part para la cpe23Uri actual
                aux2=aux_str.split("cpe:2.3:")
                if(aux2[1][0] == 'h'):
                    count_totaluri_iot+=1
                    count_hardwareuri_iot+=1  
                elif(aux2[1][0] == 'o'):
                    count_totaluri_iot+=1
                    count_operatingsystemuri_iot+=1 
                elif(aux2[1][0] == 'a'):
                    count_totaluri_iot+=1
                    count_applicationuri_iot+=1 
                else:
                    count_totaluri_iot+=1
    else:
        #Si existe un unico valor de cpe23Uri en la fila actual
        aux_str=df_cpe_iot["cpes.cpe23Uri"][r].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
        #Obtengo el valor de type/part del cpe23Uri actual
        aux2=aux_str.split("cpe:2.3:")
        if(aux2[1][0] == 'h'):
            count_totaluri_iot+=1
            count_hardwareuri_iot+=1  
        elif(aux2[1][0] == 'o'):
            count_totaluri_iot+=1
            count_operatingsystemuri_iot+=1 
        elif(aux2[1][0] == 'a'):
            count_totaluri_iot+=1
            count_applicationuri_iot+=1 
        else:
            count_totaluri_iot+=1
            
print("**************************ESTADÍSTICAS TIPOS DE URI/PARTE CPE PARTE IOT********************************")
print("\n")
print("  DE UN TOTAL DE  "+str(count_totaluri_iot)+" CPES, LAS ESTADÍSTICAS DE PARTE/TIPO SON : \n")
print("  -  EXISTEN "+str(count_hardwareuri_iot)+" CPES QUE HACEN REFERENCIA A HARDWARE \n")
print("  -  EXISTEN "+str(count_applicationuri_iot)+" CPES QUE HACEN REFERENCIA A UNA APLICACIÓN \n")
print("  -  EXISTEN "+str(count_operatingsystemuri_iot)+" CPES QUE HACEN REFERENCIA AL SISTEMA OPERATIVO \n")

print("\n")
print("**************************PORCENTAJE TIPO DE URI/PARTE CPE PARTE IOT********************************")
print("\n")
print("  DE UN TOTAL DE  "+str(count_totaluri_iot)+" CPES, LOS PORCENTAJES DE PARTE/TIPO SON : \n")
print("  -  EL "+str(float(((count_hardwareuri_iot*100)/count_totaluri_iot)))+" % DE LOS CPES HACEN REFERENCIA A HARDWARE \n")
print("  -  EL "+str(float(((count_applicationuri_iot*100)/count_totaluri_iot)))+" % DE LOS CPES HACEN REFERENCIA A UNA APLICACIÓN \n")
print("  -  EL "+str(float(((count_operatingsystemuri_iot*100)/count_totaluri_iot)))+" % DE LOS CPES HACEN REFERENCIA AL SISTEMA OPERATIVO \n")
print("\n")









#Variables donde almacenare el contador de tipo de CPE23URI para SMART HOME
#Contador de cpe23uris de tipo hardware
count_hardwareuri_sh=0
#Contador de cpe23uris de tipo application
count_applicationuri_sh=0
#Contador de cpe23uris de tipo operatingsystem
count_operatingsystemuri_sh=0
#Contador total de cpe23uris
count_totaluri_sh=0

for r in range(0,len(df_cpe_sh["cpes.cpe23Uri"])):
    if('[' in df_cpe_sh["cpes.cpe23Uri"][r]):
        aux=df_cpe_sh["cpes.cpe23Uri"][r].split(",")
        for k in range(0,len(aux)):
            if(len(aux)>0):
                aux_str=aux[k].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
                aux2=aux_str.split("cpe:2.3:")
                if(aux2[1][0] == 'h'):
                    count_totaluri_sh+=1
                    count_hardwareuri_sh+=1  
                elif(aux2[1][0] == 'o'):
                    count_totaluri_sh+=1
                    count_operatingsystemuri_sh+=1 
                elif(aux2[1][0] == 'a'):
                    count_totaluri_sh+=1
                    count_applicationuri_sh+=1 
                else:
                    count_totaluri_sh+=1
    else:
        aux_str=df_cpe_sh["cpes.cpe23Uri"][r].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
        aux2=aux_str.split("cpe:2.3:")
        if(aux2[1][0] == 'h'):
            count_totaluri_sh+=1
            count_hardwareuri_sh+=1  
        elif(aux2[1][0] == 'o'):
            count_totaluri_sh+=1
            count_operatingsystemuri_sh+=1 
        elif(aux2[1][0] == 'a'):
            count_totaluri_sh+=1
            count_applicationuri_sh+=1 
        else:
            count_totaluri_sh+=1
            
print("**************************ESTADÍSTICAS TIPOS DE URI/PARTE CPE PARTE SMART HOME********************************")
print("\n")
print("  DE UN TOTAL DE  "+str(count_totaluri_sh)+" CPES, LAS ESTADÍSTICAS DE PARTE/TIPO SON : \n")
print("  -  EXISTEN "+str(count_hardwareuri_sh)+" CPES QUE HACEN REFERENCIA A HARDWARE \n")
print("  -  EXISTEN "+str(count_applicationuri_sh)+" CPES QUE HACEN REFERENCIA A UNA APLICACIÓN \n")
print("  -  EXISTEN "+str(count_operatingsystemuri_sh)+" CPES QUE HACEN REFERENCIA AL SISTEMA OPERATIVO \n")

print("\n")
print("**************************PORCENTAJE TIPO DE URI/PARTE CPE PARTE SMART HOME********************************")
print("\n")
print("  DE UN TOTAL DE  "+str(count_totaluri_sh)+" CPES, LOS PORCENTAJES DE PARTE/TIPO SON : \n")
print("  -  EL "+str(float(((count_hardwareuri_sh*100)/count_totaluri_sh)))+" % DE LOS CPES HACEN REFERENCIA A HARDWARE \n")
print("  -  EL "+str(float(((count_applicationuri_sh*100)/count_totaluri_sh)))+" % DE LOS CPES HACEN REFERENCIA A UNA APLICACIÓN \n")
print("  -  EL "+str(float(((count_operatingsystemuri_sh*100)/count_totaluri_sh)))+" % DE LOS CPES HACEN REFERENCIA AL SISTEMA OPERATIVO \n")
print("\n")









print("**************************ESTADÍSTICAS TIPOS DE URI/PARTE CPE PARTE IOT Y SMART HOME CONJUNTAS********************************")
print("\n")
print("  DE UN TOTAL DE  "+str(count_totaluri_sh+count_totaluri_iot)+" CPES, LAS ESTADÍSTICAS DE PARTE/TIPO SON : \n")
print("  -  EXISTEN "+str(count_hardwareuri_sh+count_hardwareuri_iot)+" CPES QUE HACEN REFERENCIA A HARDWARE \n")
print("  -  EXISTEN "+str(count_applicationuri_sh+count_applicationuri_iot)+" CPES QUE HACEN REFERENCIA A UNA APLICACIÓN \n")
print("  -  EXISTEN "+str(count_operatingsystemuri_sh+count_operatingsystemuri_iot)+" CPES QUE HACEN REFERENCIA AL SISTEMA OPERATIVO \n")

print("\n")
print("**************************PORCENTAJE TIPO DE URI/PARTE CPE PARTE IOT Y SMART HOME CONJUNTAS********************************")
print("\n")
print("  DE UN TOTAL DE  "+str(count_totaluri_sh+count_totaluri_iot)+" CPES, LOS PORCENTAJES DE PARTE/TIPO SON : \n")
print("  -  EL "+str(float((((count_hardwareuri_sh+count_hardwareuri_iot)*100)/(count_totaluri_sh+count_totaluri_iot))))+" % DE LOS CPES HACEN REFERENCIA A HARDWARE \n")
print("  -  EL "+str(float((((count_applicationuri_sh+count_applicationuri_iot)*100)/(count_totaluri_sh+count_totaluri_iot))))+" % DE LOS CPES HACEN REFERENCIA A UNA APLICACIÓN \n")
print("  -  EL "+str(float((((count_operatingsystemuri_sh+count_operatingsystemuri_iot)*100)/(count_totaluri_sh+count_totaluri_iot))))+" % DE LOS CPES HACEN REFERENCIA AL SISTEMA OPERATIVO \n")
print("\n")

































