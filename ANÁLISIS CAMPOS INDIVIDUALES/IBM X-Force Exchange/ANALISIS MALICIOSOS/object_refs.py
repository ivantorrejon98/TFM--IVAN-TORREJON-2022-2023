

import pandas as pd
from datetime import datetime


#Abro los ficheros con los que voy a tratar


df_malw_ana_iot = pd.read_excel('ibm_analisis_maliciosos_iot_2023_v2.xlsx')

#Variables donde almacenare el contador de tipo de objeto de referencia de IBM ANALISIS MALICIOSOS
count_type_indicatoref_ibm_malw_analysis_iot=0
count_type_markingref_ibm_malw_analysis_iot=0
count_type_anotheref_ibm_malw_analysis_iot=0

#Variables auxiliares para almacenar la cantidad de objetos STIX 2.1 de cada fila
len_aux_sh=0
len_aux_iot=0

#Comprobamos el tipo de objeto de referencia 
for r in range(0,len(df_malw_ana_iot["object_refs"])):
    #Comprobamos si existen varios objetos STIX 2.1 para una misma fila
    if('[' in df_malw_ana_iot["object_refs"][r]):
        #Obtenemos los distintos objetos
        aux=df_malw_ana_iot["object_refs"][r].split(",")
        len_aux_iot+=len(aux)-1
        for l in range(0,len(aux)):
            if(len(aux)>0):
                aux_str=aux[l].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
                if('indicator' in aux_str):
                    count_type_indicatoref_ibm_malw_analysis_iot+=1
                elif('marking' in aux_str):
                    count_type_markingref_ibm_malw_analysis_iot+=1
                else:
                    if('NONE' not in aux_str):
                        count_type_anotheref_ibm_malw_analysis_iot+=1
    else:
        #Si existe un unico objeto en la fila actual
        if('indicator' in df_malw_ana_iot["object_refs"][r]):
            count_type_indicatoref_ibm_malw_analysis_iot+=1
        elif('marking' in df_malw_ana_iot["object_refs"][r]):
            count_type_markingref_ibm_malw_analysis_iot+=1
        else:
            if('NONE' not in df_malw_ana_iot["object_refs"][r]):
                print(df_malw_ana_iot["object_refs"][r])
                count_type_anotheref_ibm_malw_analysis_iot+=1
        

print("**************************ESTADISTICAS TIPO DE OBJETO DE REFERENCIA INFORMES IBM ANALISIS MALICIOSOS PARTE IOT********************************")
print("\n")
print("HAY "+str(count_type_indicatoref_ibm_malw_analysis_iot)+" OBJETOS DE REFERENCIA DE TIPO INDICADOR \n")
print("HAY "+str(count_type_markingref_ibm_malw_analysis_iot)+" OBJETOS DE REFERENCIA DE TIPO DEFINICION DE MARCADO \n")
print("HAY "+str(count_type_anotheref_ibm_malw_analysis_iot)+" REFERENCIAS DE OTROS TIPOS \n")



print("**************************PORCENTAJE TIPO DE OBJETO DE REFERENCIA INFORMES IBM ANALISIS MALICIOSOS PARTE IOT********************************")
print("\n")

print("EL "+str(float((((count_type_indicatoref_ibm_malw_analysis_iot)*100)/(len(df_malw_ana_iot["object_refs"])+int(len_aux_iot)))))+"% DE LOS OBJETOS DE REFERENCIA ES DE TIPO INDICADOR \n")
print("EL "+str(float((((count_type_markingref_ibm_malw_analysis_iot)*100)/(len(df_malw_ana_iot["object_refs"])+int(len_aux_iot)))))+"% DE LOS OBJETOS DE REFERENCIA ES DE TIPO DEFINICION DE MARCADO \n")
print("EL "+str(float((((count_type_anotheref_ibm_malw_analysis_iot)*100)/(len(df_malw_ana_iot["object_refs"])+int(len_aux_iot)))))+"% DE LOS OBJETOS DE REFERENCIA ES DE OTRO TIPO DISTINTO \n")
print("\n")


#Abro los ficheros con los que voy a tratar


df_malw_ana_sh = pd.read_excel('ibm_analisis_maliciosos_smarthome_2023.xlsx')




#Variables donde almacenare el contador de tipo de objeto de referencia de ANALISIS MALICIOSOS
count_type_indicatoref_ibm_malw_analysis_sh=0
count_type_markingref_ibm_malw_analysis_sh=0
count_type_anotheref_ibm_malw_analysis_sh=0


#Comprobamos el tipo de objeto de referencia 
for r in range(0,len(df_malw_ana_sh["object_refs"])):
    #Comprobamos si hay varios objetos en la fila actual
    if('[' in df_malw_ana_sh["object_refs"][r]):
        #Obtenemos los objetos
        aux=df_malw_ana_sh["object_refs"][r].split(",")
        len_aux_sh+=len(aux)-1
        for l in range(0,len(aux)):
            if(len(aux)>0):
                aux_str=aux[l].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
                if('indicator' in aux_str):
                    count_type_indicatoref_ibm_malw_analysis_sh+=1
                elif('marking' in aux_str):
                    count_type_markingref_ibm_malw_analysis_sh+=1
                else:
                    if('NONE' not in aux_str):
                        count_type_anotheref_ibm_malw_analysis_sh+=1
    else:
        #Si existe un unico objeto para la fila actual
        if('indicator' in df_malw_ana_sh["object_refs"][r]):
            count_type_indicatoref_ibm_malw_analysis_sh+=1
        elif('marking' in df_malw_ana_sh["object_refs"][r]):
            count_type_markingref_ibm_malw_analysis_sh+=1
        else:
            if('NONE' not in df_malw_ana_sh["object_refs"][r]):
                print(df_malw_ana_sh["object_refs"][r])
                count_type_anotheref_ibm_malw_analysis_sh+=1

                
print("**************************ESTADISTICAS TIPO DE OBJETO DE REFERENCIA INFORMES IBM ANALISIS MALICIOSOS PARTE SMART HOME********************************")
print("\n")
print("\n")
print("HAY "+str(count_type_indicatoref_ibm_malw_analysis_sh)+" OBJETOS DE REFERENCIA DE TIPO INDICADOR \n")
print("HAY "+str(count_type_markingref_ibm_malw_analysis_sh)+" OBJETOS DE REFERENCIA DE TIPO DEFINICION DE MARCADO \n")
print("HAY "+str(count_type_anotheref_ibm_malw_analysis_sh)+" REFERENCIAS DE OTROS TIPOS \n")




print("**************************PORCENTAJE TIPO DE OBJETO DE REFERENCIA INFORMES IBM ANALISIS MALICIOSOS PARTE SMART HOME********************************")
print("\n")
print("\n")
print("EL "+str(float((((count_type_indicatoref_ibm_malw_analysis_sh)*100)/(len(df_malw_ana_sh["object_refs"])+int(len_aux_sh)))))+"% DE LOS OBJETOS DE REFERENCIA ES DE TIPO INDICADOR \n")
print("EL "+str(float((((count_type_markingref_ibm_malw_analysis_sh)*100)/(len(df_malw_ana_sh["object_refs"])+int(len_aux_sh)))))+"% DE LOS OBJETOS DE REFERENCIA ES DE TIPO DEFINICION DE MARCADO \n")
print("EL "+str(float((((count_type_anotheref_ibm_malw_analysis_sh)*100)/(len(df_malw_ana_sh["object_refs"])+int(len_aux_sh)))))+"% DE LOS OBJETOS DE REFERENCIA ES DE OTRO TIPO DISTINTO \n")
print("\n")               
                
                
                
                
                
                
                
                
                
                
                
                

print("**************************ESTADISTICAS TIPO DE OBJETO DE REFERENCIA INFORMES IBM ANALISIS MALICIOSOS PARTE IOT Y SMART HOME CONJUNTAS********************************")
print("\n")
print("HAY "+str(count_type_indicatoref_ibm_malw_analysis_sh+count_type_indicatoref_ibm_malw_analysis_iot)+" OBJETOS DE REFERENCIA DE TIPO INDICADOR \n")
print("HAY "+str(count_type_markingref_ibm_malw_analysis_sh+count_type_markingref_ibm_malw_analysis_iot)+" OBJETOS DE REFERENCIA DE TIPO DEFINICION DE MARCADO \n")
print("HAY "+str(count_type_anotheref_ibm_malw_analysis_sh+count_type_anotheref_ibm_malw_analysis_iot)+" REFERENCIAS DE OTROS TIPOS \n")
print("\n")


print("**************************PORCENTAJE ESTADISTICAS TIPO DE OBJETO DE REFERENCIA INFORMES IBM ANALISIS MALICIOSOS PARTE IOT Y SMART HOME CONJUNTAS********************************")
print("\n")
print("EL "+str(float((((count_type_indicatoref_ibm_malw_analysis_sh+count_type_indicatoref_ibm_malw_analysis_iot)*100)/(len(df_malw_ana_sh["object_refs"])+int(len_aux_sh)+len(df_malw_ana_iot["object_refs"])+int(len_aux_iot)))))+"% DE LOS OBJETOS DE REFERENCIA ES DE TIPO INDICADOR \n")
print("EL "+str(float((((count_type_markingref_ibm_malw_analysis_sh+count_type_markingref_ibm_malw_analysis_iot)*100)/(len(df_malw_ana_sh["object_refs"])+int(len_aux_sh)+len(df_malw_ana_iot["object_refs"])+int(len_aux_iot)))))+"% DE LOS OBJETOS DE REFERENCIA ES DE TIPO DEFINICION DE MARCADO \n")
print("EL "+str(float((((count_type_anotheref_ibm_malw_analysis_sh+count_type_anotheref_ibm_malw_analysis_iot)*100)/(len(df_malw_ana_sh["object_refs"])+int(len_aux_sh)+len(df_malw_ana_iot["object_refs"])+int(len_aux_iot)))))+"% DE LOS OBJETOS DE REFERENCIA ES DE OTRO TIPO \n")






















