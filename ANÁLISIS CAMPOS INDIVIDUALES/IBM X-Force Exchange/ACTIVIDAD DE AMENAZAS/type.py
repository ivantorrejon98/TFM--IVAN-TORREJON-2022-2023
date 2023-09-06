
import pandas as pd
from datetime import datetime

#Abro los ficheros con los que voy a tratar


df_thract_report_iot = pd.read_excel('ibm_threat_activity_report_iot_2023_v2.xlsx')

#Variables donde almacenare el contador de tipo de objeto STIX 2.1 de IBM ACTIVIDAD DE AMENAZAS
count_type_report_ibm_thract_reportlysis_iot=0
count_type_markingdef_ibm_thract_reportlysis_iot=0
count_type_indicator_ibm_thract_reportlysis_iot=0

#Variable para almacenar el numero total de objetos
len_aux_iot=0


#Comprobamos el tipo de objeto STIX 2.1 
for r in range(0,len(df_thract_report_iot["type"])):
    #Comprobamos si hay varios objetos en la fila actual
    if('[' in df_thract_report_iot["type"][r]):
        aux=df_thract_report_iot["type"][r].split(",")
        for l in range(0,len(aux)):
            if(len(aux)>0):
                aux_str=aux[l].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
                if(aux_str == 'report'):
                    len_aux_iot+=1
                    count_type_report_ibm_thract_reportlysis_iot+=1  
                elif(aux_str == 'marking-definition'):
                    len_aux_iot+=1
                    count_type_markingdef_ibm_thract_reportlysis_iot+=1 
                elif(aux_str == 'indicator'):
                    len_aux_iot+=1
                    count_type_indicator_ibm_thract_reportlysis_iot+=1 
    else:
        #Si existe un unico objeto en la fila actual
        if(df_thract_report_iot["type"][r] == 'report'):
            len_aux_iot+=1
            count_type_report_ibm_thract_reportlysis_iot+=1  
        elif(df_thract_report_iot["type"][r] == 'marking-definition'):
            len_aux_iot+=1
            count_type_markingdef_ibm_thract_reportlysis_iot+=1
        elif(df_thract_report_iot["type"][r] == 'indicator'):
            len_aux_iot+=1
            count_type_indicator_ibm_thract_reportlysis_iot+=1

print("**************************ESTADÍSTICAS TIPO DE OBJETO IBM ACTIVIDAD DE AMENAZAS PARTE IOT********************************")
print("\n")
print("HAY "+str(count_type_report_ibm_thract_reportlysis_iot)+" OBJETOS DE TIPO REPORTE \n")
print("HAY "+str(count_type_markingdef_ibm_thract_reportlysis_iot)+" OBJETOS DE TIPO DEFINICION DE MARCADO \n")
print("HAY "+str(count_type_indicator_ibm_thract_reportlysis_iot)+" OBJETOS DE TIPO INDICADOR \n")
print("\n")
print("**************************PORCENTAJE TIPO DE OBJETO IBM ACTIVIDAD DE AMENAZAS PARTE IOT********************************")
print("\n")

print("EL "+str(float((((count_type_report_ibm_thract_reportlysis_iot)*100)/len_aux_iot)))+"% DE LOS OBJETOS SON DE TIPO REPORTE \n")
print("EL "+str(float((((count_type_markingdef_ibm_thract_reportlysis_iot)*100)/len_aux_iot)))+"% DE LOS OBJETOS SON DE TIPO DEFINICION DE MARCADO \n")
print("EL "+str(float((((count_type_indicator_ibm_thract_reportlysis_iot)*100)/len_aux_iot)))+"% DE LOS OBJETOS SON DE TIPO INDICADOR \n")
print("\n")




df_thract_report_sh = pd.read_excel('ibm_threat_activity_report_smarthome_2023_v2.xlsx')



#Variables donde almacenare el contador de tipo de objeto STIX 2.1 de IBM ACTIVIDAD DE AMENAZAS
count_type_report_ibm_thract_reportlysis_sh=0
count_type_markingdef_ibm_thract_reportlysis_sh=0
count_type_indicator_ibm_thract_reportlysis_sh=0

#Variable para almacenar el numero de objetos
len_aux_sh=0


#Comprobamos el tipo de objeto STIX 2.1 
for k in range(0,len(df_thract_report_sh["type"])):
    #Comprobamos si hay varios objetos para la fila actual
    if('[' in df_thract_report_sh["type"][k]):
        aux_sh=df_thract_report_sh["type"][k].split(",")
        for g in range(0,len(aux_sh)):
            if(len(aux_sh)>0):
                aux_str_sh=aux_sh[g].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
                if(aux_str_sh == 'report'):
                    len_aux_sh+=1
                    count_type_report_ibm_thract_reportlysis_sh+=1  
                elif(aux_str_sh == 'marking-definition'):
                    len_aux_sh+=1
                    count_type_markingdef_ibm_thract_reportlysis_sh+=1  
                elif(aux_str_sh == 'indicator'):
                    len_aux_sh+=1
                    count_type_indicator_ibm_thract_reportlysis_sh+=1  
    else:
        if(df_thract_report_sh["type"][k] == 'report'):
            len_aux_sh+=1
            count_type_report_ibm_thract_reportlysis_sh+=1  
        elif(df_thract_report_sh["type"][k] == 'marking-definition'):
            len_aux_sh+=1
            count_type_markingdef_ibm_thract_reportlysis_sh+=1 
        elif(df_thract_report_sh["type"][k] == 'indicator'):
            len_aux_sh+=1
            count_type_indicator_ibm_thract_reportlysis_sh+=1 

print("**************************ESTADÍSTICAS TIPO DE OBJETO IBM ACTIVIDAD DE AMENAZAS PARTE SMART HOME********************************")
print("\n")
print("HAY "+str(count_type_report_ibm_thract_reportlysis_sh)+" OBJETOS DE TIPO REPORTE \n")
print("HAY "+str(count_type_markingdef_ibm_thract_reportlysis_sh)+" OBJETOS DE TIPO DEFINICION DE MARCADO \n")
print("HAY "+str(count_type_indicator_ibm_thract_reportlysis_sh)+" OBJETOS DE TIPO INDICADOR \n")
print("\n")
print("**************************PORCENTAJE TIPO DE OBJETO IBM ACTIVIDAD DE AMENAZAS PARTE SMART HOME********************************")
print("\n")

print("EL "+str(float((((count_type_report_ibm_thract_reportlysis_sh)*100)/len_aux_sh)))+"% DE LOS OBJETOS SON DE TIPO REPORTE \n")
print("EL "+str(float((((count_type_markingdef_ibm_thract_reportlysis_sh)*100)/len_aux_sh)))+"% DE LOS OBJETOS SON DE TIPO DEFINICION DE MARCADO \n")
print("EL "+str(float((((count_type_indicator_ibm_thract_reportlysis_sh)*100)/len_aux_sh)))+"% DE LOS OBJETOS SON DE TIPO INDICADOR \n")

print("\n")






        

print("**************************ESTADÍSTICAS TIPO DE OBJETO IBM ACTIVIDAD DE AMENAZAS PARTE IOT Y SMART HOME CONJUNTAS********************************")
print("\n")
print("HAY "+str(count_type_report_ibm_thract_reportlysis_sh+count_type_report_ibm_thract_reportlysis_iot)+" OBJETOS DE TIPO REPORTE \n")
print("HAY "+str(count_type_markingdef_ibm_thract_reportlysis_sh+count_type_markingdef_ibm_thract_reportlysis_iot)+" OBJETOS DE TIPO DEFINICION DE MARCADO \n")
print("HAY "+str(count_type_indicator_ibm_thract_reportlysis_sh+count_type_indicator_ibm_thract_reportlysis_iot)+" OBJETOS DE TIPO INDICADOR \n")

print("\n")
print("**************************PORCENTAJE TIPO DE OBJETO IBM ACTIVIDAD DE AMENAZAS PARTE IOT Y SMART HOME CONJUNTAS********************************")
print("\n")

print("EL "+str(float((((count_type_report_ibm_thract_reportlysis_sh+count_type_report_ibm_thract_reportlysis_iot)*100)/(len_aux_iot+len_aux_sh))))+"% DE LOS OBJETOS SON DE TIPO REPORTE\n")
print("EL "+str(float((((count_type_markingdef_ibm_thract_reportlysis_sh+count_type_markingdef_ibm_thract_reportlysis_iot)*100)/(len_aux_iot+len_aux_sh))))+" % DE LOS OBJETOS SON DE TIPO DEFINICION DE MARCADO \n")
print("EL "+str(float((((count_type_indicator_ibm_thract_reportlysis_sh+count_type_indicator_ibm_thract_reportlysis_iot)*100)/(len_aux_iot+len_aux_sh))))+" % DE LOS OBJETOS SON DE TIPO INDICADOR \n")
print("\n")


















