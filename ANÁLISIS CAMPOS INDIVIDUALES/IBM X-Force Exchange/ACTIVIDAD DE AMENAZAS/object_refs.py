
import pandas as pd
from datetime import datetime

#Abro los ficheros con los que voy a tratar


df_thract_report_iot = pd.read_excel('ibm_threat_activity_report_iot_2023_v2.xlsx')


#Variables donde almacenare el contador de tipo de objeto de referencia de IBM ACTIVIDAD DE AMENAZAS
count_typeref_report_ibm_thract_report_iot=0
count_typeref_markingdef_ibm_thract_report_iot=0
count_typeref_indicator_ibm_thract_report_iot=0
count_noneref_indicator_ibm_thract_report_iot=0

#Variable auxiliar para almacenar el numero de objetos
len_aux_iot=0


#Comprobamos el tipo de objeto de referencia
for r in range(0,len(df_thract_report_iot["object_refs"])):
    #Comprobamos si la fila tiene varios objetos
    if('[' in df_thract_report_iot["object_refs"][r]):
        #Obtenemos los objetos
        aux=df_thract_report_iot["object_refs"][r].split(",")
        for l in range(0,len(aux)):
            if(len(aux)>0):
                aux_str=aux[l].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
                if('report' in aux_str):
                    len_aux_iot+=1
                    count_typeref_report_ibm_thract_report_iot+=1  
                elif('marking-definition' in aux_str):
                    len_aux_iot+=1
                    count_typeref_markingdef_ibm_thract_report_iot+=1 
                elif('indicator' in aux_str):
                    len_aux_iot+=1
                    count_typeref_indicator_ibm_thract_report_iot+=1 
                else:
                    len_aux_iot+=1
                    count_noneref_indicator_ibm_thract_report_iot+=1
    else:
        if('report' in df_thract_report_iot["object_refs"][r]):
            len_aux_iot+=1
            count_typeref_report_ibm_thract_report_iot+=1  
        elif('marking-definition' in df_thract_report_iot["object_refs"][r]):
            len_aux_iot+=1
            count_typeref_markingdef_ibm_thract_report_iot+=1
        elif('indicator' in df_thract_report_iot["object_refs"][r]):
            len_aux_iot+=1
            count_typeref_indicator_ibm_thract_report_iot+=1
        else:
            len_aux_iot+=1
            count_noneref_indicator_ibm_thract_report_iot+=1

print("**************************ESTADÍSTICAS TIPO DE OBJETO DE REFERENCIA IBM ACTIVIDADES DE AMENAZAS PARTE IOT********************************")
print("\n")
print("HAY "+str(count_typeref_report_ibm_thract_report_iot)+" OBJETOS DE REFERENCIA DE TIPO REPORTE \n")
print("HAY "+str(count_typeref_markingdef_ibm_thract_report_iot)+" OBJETOS DE REFERENCIA DE TIPO DEFINICION DE MARCADO \n")
print("HAY "+str(count_typeref_indicator_ibm_thract_report_iot)+" OBJETOS DE REFERENCIA DE TIPO INDICADOR \n")
print("HAY "+str(count_noneref_indicator_ibm_thract_report_iot)+" OBJETOS DE REFERENCIA DE TIPO NO ESPECIFICADO \n")
print("\n")
print("**************************PORCENTAJE TIPO DE OBJETO DE REFERENCIA IBM ACTIVIDADES DE AMENAZAS PARTE IOT********************************")
print("\n")

print("EL "+str(float((((count_typeref_report_ibm_thract_report_iot)*100)/len_aux_iot)))+"% DE LAS REFERENCIAS ES DE TIPO REPORTE \n")
print("EL "+str(float((((count_typeref_markingdef_ibm_thract_report_iot)*100)/len_aux_iot)))+"% DE LAS REFERENCIAS ES DE TIPO DEFINICION DE MARCADO \n")
print("EL "+str(float((((count_typeref_indicator_ibm_thract_report_iot)*100)/len_aux_iot)))+"% DE LAS REFERENCIAS ES DE TIPO INDICADOR \n")
print("EL "+str(float((((count_noneref_indicator_ibm_thract_report_iot)*100)/len_aux_iot)))+"% DE LAS REFERENCIAS NO TIENE TIPO ESPECIFICADO \n")
print("\n")






df_thract_report_sh = pd.read_excel('ibm_threat_activity_report_smarthome_2023_v2.xlsx')



#Variables donde almacenare el contador de tipo de objeto de referencia de IBM ACTIVIDAD DE AMENAZAS
count_typeref_report_ibm_thract_report_sh=0
count_typeref_markingdef_ibm_thract_report_sh=0
count_typeref_indicator_ibm_thract_report_sh=0
count_noneref_indicator_ibm_thract_report_sh=0

#Variable para almacenar el numero de objetos
len_aux_sh=0


#Comprobamos el tipo de objeto referencia 
for k in range(0,len(df_thract_report_sh["object_refs"])):
    #Si existen varios objetos en la fila actual
    if('[' in df_thract_report_sh["object_refs"][k]):
        #Obtenemos los objetos
        aux_sh=df_thract_report_sh["object_refs"][k].split(",")
        for g in range(0,len(aux_sh)):
            if(len(aux_sh)>0):
                aux_str_sh=aux_sh[g].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
                if('report' in aux_str_sh):
                    len_aux_sh+=1
                    count_typeref_report_ibm_thract_report_sh+=1  
                elif('marking-definition' in aux_str_sh):
                    len_aux_sh+=1
                    count_typeref_markingdef_ibm_thract_report_sh+=1  
                elif('indicator' in aux_str_sh):
                    len_aux_sh+=1
                    count_typeref_indicator_ibm_thract_report_sh+=1  
                else:
                    len_aux_sh+=1
                    count_noneref_indicator_ibm_thract_report_sh+=1
    else:
        if('report' in df_thract_report_sh["object_refs"][k]):
            len_aux_sh+=1
            count_typeref_report_ibm_thract_report_sh+=1  
        elif('marking-definition' in df_thract_report_sh["object_refs"][k]):
            len_aux_sh+=1
            count_typeref_markingdef_ibm_thract_report_sh+=1 
        elif('indicator' in df_thract_report_sh["object_refs"][k]):
            len_aux_sh+=1
            count_typeref_indicator_ibm_thract_report_sh+=1 
        else:
            len_aux_sh+=1
            count_noneref_indicator_ibm_thract_report_sh+=1

print("**************************ESTADÍSTICAS TIPO DE OBJETO DE REFERENCIA IBM ACTIVIDADES DE AMENAZAS PARTE SMART HOME********************************")
print("\n")
print("HAY "+str(count_typeref_report_ibm_thract_report_sh)+" OBJETOS DE REFERENCIA DE TIPO REPORTE \n")
print("HAY "+str(count_typeref_markingdef_ibm_thract_report_sh)+" OBJETOS DE REFERENCIA DE TIPO DEFINICION DE MARCADO \n")
print("HAY "+str(count_typeref_indicator_ibm_thract_report_sh)+" OBJETOS DE REFERENCIA DE TIPO INDICADOR \n")
print("HAY "+str(count_noneref_indicator_ibm_thract_report_sh)+" OBJETOS DE REFERENCIA DE TIPO NO ESPECIFICADO \n")
print("\n")
print("**************************PORCENTAJE TIPO DE OBJETO DE REFERENCIA IBM ACTIVIDADES DE AMENAZAS PARTE SMART HOME********************************")
print("\n")

print("EL "+str(float((((count_typeref_report_ibm_thract_report_sh)*100)/len_aux_sh)))+"% DE LAS REFERENCIAS ES DE TIPO REPORTE \n")
print("EL "+str(float((((count_typeref_markingdef_ibm_thract_report_sh)*100)/len_aux_sh)))+"% DE LAS REFERENCIAS ES DE TIPO DEFINICION DE MARCADO \n")
print("EL "+str(float((((count_typeref_indicator_ibm_thract_report_sh)*100)/len_aux_sh)))+"% DE LAS REFERENCIAS ES DE TIPO INDICADOR \n")
print("EL "+str(float((((count_noneref_indicator_ibm_thract_report_sh)*100)/len_aux_sh)))+"% DE LAS REFERENCIAS NO TIENE TIPO ESPECIFICADO \n")

print("\n")






        

print("**************************ESTADÍSTICAS TIPO DE OBJETO DE REFERENCIA IBM ACTIVIDADES DE AMENAZAS PARTE IOT Y SMART HOME CONJUNTAS********************************")
print("\n")
print("HAY "+str(count_typeref_report_ibm_thract_report_sh+count_typeref_report_ibm_thract_report_iot)+" OBJETOS DE REFERENCIA DE TIPO REPORTE \n")
print("HAY "+str(count_typeref_markingdef_ibm_thract_report_sh+count_typeref_markingdef_ibm_thract_report_iot)+" OBJETOS DE REFERENCIA DE TIPO DEFINICION DE MARCADO \n")
print("HAY "+str(count_typeref_indicator_ibm_thract_report_sh+count_typeref_indicator_ibm_thract_report_iot)+" OBJETOS DE REFERENCIA DE TIPO INDICADOR \n")
print("HAY "+str(count_noneref_indicator_ibm_thract_report_sh+count_noneref_indicator_ibm_thract_report_iot)+" REFERENCIAS QUE NO TIENEN TIPO ESPECIFICADO \n")

print("\n")
print("**************************PORCENTAJE TIPO DE OBJETO DE REFERENCIA IBM ACTIVIDADES DE AMENAZAS PARTE IOT Y SMART HOME CONJUNTAS********************************")
print("\n")

print("EL "+str(float((((count_typeref_report_ibm_thract_report_sh+count_typeref_report_ibm_thract_report_iot)*100)/(len_aux_iot+len_aux_sh))))+"% DE LAS REFERENCIAS ES DE TIPO REPORTE \n")
print("EL "+str(float((((count_typeref_markingdef_ibm_thract_report_sh+count_typeref_markingdef_ibm_thract_report_iot)*100)/(len_aux_iot+len_aux_sh))))+" % DE LAS REFERENCIAS ES DE TIPO DEFINICION DE MARCADO\n")
print("EL "+str(float((((count_typeref_indicator_ibm_thract_report_sh+count_typeref_indicator_ibm_thract_report_iot)*100)/(len_aux_iot+len_aux_sh))))+" % DE LAS REFERENCIAS ES DE TIPO INDICADOR \n")
print("EL "+str(float((((count_noneref_indicator_ibm_thract_report_sh+count_noneref_indicator_ibm_thract_report_iot)*100)/(len_aux_iot+len_aux_sh))))+" % DE LAS REFERENCIAS NO TIENE TIPO ESPECIFICADO \n")

print("\n")

















