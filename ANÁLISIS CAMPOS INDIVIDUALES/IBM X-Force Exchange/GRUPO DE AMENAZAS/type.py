


import pandas as pd
from datetime import datetime

#Abro los ficheros con los que voy a tratar

df_ibm_thrgroup = pd.read_excel('ibm_grupo_amenazas_2023.xlsx')

#Variables donde almacenare el contador de tipo de objeto STIX 2-1 para entradas de  IBM GRUPO DE AMENAZAS
count_type_report_ibm_thrgroup=0
count_type_markingdef_ibm_thrgroup=0

#Variable auxiliar para establecer la cantidad de objetos de la entrada actual de IBM GRUPO DE AMENAZAS
len_aux=0


#Comprobamos el anio de modificacion 
for r in range(0,len(df_ibm_thrgroup["type"])):
    #Compruebo si hay varios objetos STIX 2.1 para la entrada actual
    if('[' in df_ibm_thrgroup["type"][r]):
        aux=df_ibm_thrgroup["type"][r].split(",")
        len_aux+=len(aux)-1
        for l in range(0,len(aux)):
            if(len(aux)>0):
                aux_str=aux[l].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
                if(aux_str == 'report'):
                    count_type_report_ibm_thrgroup+=1  
                elif(aux_str == 'marking-definition'):
                    count_type_markingdef_ibm_thrgroup+=1 
    else:
        #Si existe un unico objeto STIX 2.1 para la entrada actual
        if(df_ibm_thrgroup["type"][r] == 'report'):
            count_type_report_ibm_thrgroup+=1  
        elif(df_ibm_thrgroup["type"][r] == 'marking-definition'):
            count_type_markingdef_ibm_thrgroup+=1
        

print("**************************ESTADÍSTICAS TIPO DE OBJETO STIX 2.1 IBM GRUPO DE AMENAZAS********************************")
print("\n")
print("HAY "+str(count_type_report_ibm_thrgroup)+" OBJETOS DE TIPO REPORTE \n")
print("HAY "+str(count_type_markingdef_ibm_thrgroup)+" OBJETOS DE TIPO DEFINICION DE MARCADO \n")

print("\n")
print("**************************PORCENTAJE TIPO DE OBJETO STIX 2.1 IBM GRUPO DE AMENAZAS********************************")
print("\n")

print("EL "+str(float((((count_type_report_ibm_thrgroup)*100)/(len(df_ibm_thrgroup["type"])+int(len_aux)))))+"% DE LOS OBJETOS ES DE TIPO REPORTE \n")
print("EL "+str(float((((count_type_markingdef_ibm_thrgroup)*100)/(len(df_ibm_thrgroup["type"])+int(len_aux)))))+"% DE LOS OBJETOS ES DE TIPO DEFINICION DE MARCADO \n")
print("\n")














