

import pandas as pd
from datetime import datetime

#Abro los ficheros con los que voy a tratar

df_ibm_sector = pd.read_excel('ibm_sector_v2.xlsx')





#Variables donde almacenare el contador de tipo de objeto de SECTOR
count_type_report_ibm_sector=0
count_type_markingdef_ibm_sector=0
#Variable auxiliar para almacenar el numero de objetos STIX de la fila actual
len_aux=0


#Comprobamos el tipo de objeto
for r in range(0,len(df_ibm_sector["type"])):
    #Si existen varios objetos STIX en la fila actual
    if('[' in df_ibm_sector["type"][r]):
        aux=df_ibm_sector["type"][r].split(",")
        len_aux+=len(aux)-1
        for l in range(0,len(aux)):
            if(len(aux)>0):
                aux_str=aux[l].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
                if(aux_str == 'report'):
                    count_type_report_ibm_sector+=1  
                elif(aux_str == 'marking-definition'):
                    count_type_markingdef_ibm_sector+=1 
    else:
        #Si existe un unico objeto STIX en la fila actual
        if(df_ibm_sector["type"][r] == 'report'):
            count_type_report_ibm_sector+=1  
        elif(df_ibm_sector["type"][r] == 'marking-definition'):
            count_type_markingdef_ibm_sector+=1
        

print("**************************ESTADÍSTICAS TIPO DE OBJETO IBM SECTOR********************************")
print("\n")
print("HAY "+str(count_type_report_ibm_sector)+" OBJETOS DE TIPO REPORTE \n")
print("HAY "+str(count_type_markingdef_ibm_sector)+" OBJETOS DE TIPO DEFINICION DE MARCADO \n")

print("\n")
print("**************************PORCENTAJE TIPO DE OBJETO IBM SECTOR********************************")
print("\n")

print("EL "+str(float((((count_type_report_ibm_sector)*100)/(len(df_ibm_sector["type"])+int(len_aux)))))+"% DE LOS OBJETOS ES DE TIPO REPORTE \n")
print("EL "+str(float((((count_type_markingdef_ibm_sector)*100)/(len(df_ibm_sector["type"])+int(len_aux)))))+"% DE LOS OBJETOS ES DE TIPO DEFINICION DE MARCADO \n")

print("\n")














