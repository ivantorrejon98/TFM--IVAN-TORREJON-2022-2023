
import pandas as pd
from datetime import datetime

#Abro los ficheros con los que voy a tratar


df_alienvault_iot = pd.read_excel('alienvault_iot_2023.xlsx')


#Variables donde almacenare el contador de tipo de objeto de referencia de pulsos ALIENVAULT
count_type_indicatoref_alienvault_iot=0
count_type_identityref_alienvault_iot=0
count_type_anotheref_alienvault_iot=0
count_type_vulnerabilityref_alienvault_iot=0
count_type_threatactoref_alienvault_iot=0

#Variable auxiliar para almacenar el numero de objetos
len_aux_iot=0


#Comprobamos el tipo de objeto de referencia
for r in range(0,len(df_alienvault_iot["object_refs"])):
    #Comprobamos si la fila tiene varios objetos
    if('[' in df_alienvault_iot["object_refs"][r]):
        #Obtenemos los objetos
        aux=df_alienvault_iot["object_refs"][r].split(",")
        for l in range(0,len(aux)):
            if(len(aux)>0):
                aux_str=aux[l].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
                if('identity' in aux_str):
                    len_aux_iot+=1
                    count_type_identityref_alienvault_iot+=1 
                elif('indicator' in aux_str):
                    len_aux_iot+=1
                    count_type_indicatoref_alienvault_iot+=1 
                elif('vulnerability' in aux_str):
                    len_aux_iot+=1
                    count_type_vulnerabilityref_alienvault_iot+=1 
                elif('threat' in aux_str):
                    len_aux_iot+=1
                    count_type_threatactoref_alienvault_iot+=1
                else:
                    if(aux_str!='NONE'):
                        len_aux_iot+=1
                        count_type_anotheref_alienvault_iot+=1
    else:
        if('identity' in df_alienvault_iot["object_refs"][r]):
            len_aux_iot+=1
            count_type_identityref_alienvault_iot+=1
        elif('indicator' in df_alienvault_iot["object_refs"][r]):
            len_aux_iot+=1
            count_type_indicatoref_alienvault_iot+=1
        elif('vulnerability' in df_alienvault_iot["object_refs"][r]):
            len_aux_iot+=1
            count_type_vulnerabilityref_alienvault_iot+=1 
        elif('threat' in df_alienvault_iot["object_refs"][r]):
            len_aux_iot+=1
            count_type_threatactoref_alienvault_iot+=1
        else:
            if(df_alienvault_iot["object_refs"][r]!='NONE'):
                len_aux_iot+=1
                count_type_anotheref_alienvault_iot+=1

print("**************************ESTADÍSTICAS TIPO DE OBJETO DE REFERENCIA PULSOS ALIENVAULT PARTE IOT********************************")
print("\n")
print("HAY "+str(count_type_identityref_alienvault_iot)+" OBJETOS DE REFERENCIA DE TIPO IDENTIDAD \n")
print("HAY "+str(count_type_indicatoref_alienvault_iot)+" OBJETOS DE REFERENCIA DE TIPO INDICADOR \n")
print("HAY "+str(count_type_vulnerabilityref_alienvault_iot)+" OBJETOS DE REFERENCIA DE TIPO VULNERABILIDAD \n")
print("HAY "+str(count_type_threatactoref_alienvault_iot)+" OBJETOS DE REFERENCIA DE TIPO ACTOR DE AMENAZAS \n")
print("HAY "+str(count_type_anotheref_alienvault_iot)+" OBJETOS DE REFERENCIA DE TIPO NO ESPECIFICADO \n")
print("\n")
print("**************************PORCENTAJE TIPO DE OBJETO DE REFERENCIA PULSOS ALIENVAULT PARTE IOT********************************")
print("\n")

print("EL "+str(float((((count_type_identityref_alienvault_iot)*100)/len_aux_iot)))+"% DE LOS OBJETOS DE REFERENCIA ES DE TIPO IDENTIDAD \n")
print("EL "+str(float((((count_type_indicatoref_alienvault_iot)*100)/len_aux_iot)))+"% DE LOS OBJETOS DE REFERENCIA ES DE TIPO INDICADOR \n")
print("EL "+str(float((((count_type_vulnerabilityref_alienvault_iot)*100)/len_aux_iot)))+"% DE LOS OBJETOS DE REFERENCIA ES DE TIPO VULNERABILIDAD \n")
print("EL "+str(float((((count_type_threatactoref_alienvault_iot)*100)/len_aux_iot)))+"% DE LOS OBJETOS DE REFERENCIA ES DE TIPO ACTOR DE AMENAZAS \n")
print("EL "+str(float((((count_type_anotheref_alienvault_iot)*100)/len_aux_iot)))+"% DE LOS OBJETOS DE REFERENCIA NO TIENE TIPO ESPECIFICADO \n")
print("\n")






df_alienvault_sh = pd.read_excel('alienvault_smart_home_2023.xlsx')


#Variables donde almacenare el contador de tipo de objeto de referencia de pulsos ALIENVAULT
count_type_indicatoref_alienvault_sh=0
count_type_identityref_alienvault_sh=0
count_type_anotheref_alienvault_sh=0
count_type_vulnerabilityref_alienvault_sh=0
count_type_threatactoref_alienvault_sh=0

#Variable auxiliar para almacenar el numero de objetos
len_aux_sh=0


#Comprobamos el tipo de objeto de referencia
for r in range(0,len(df_alienvault_sh["object_refs"])):
    #Comprobamos si la fila tiene varios objetos
    if('[' in df_alienvault_sh["object_refs"][r]):
        #Obtenemos los objetos
        aux=df_alienvault_sh["object_refs"][r].split(",")
        for l in range(0,len(aux)):
            if(len(aux)>0):
                aux_str=aux[l].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
                if('identity' in aux_str):
                    len_aux_sh+=1
                    count_type_identityref_alienvault_sh+=1 
                elif('indicator' in aux_str):
                    len_aux_sh+=1
                    count_type_indicatoref_alienvault_sh+=1 
                elif('vulnerability' in aux_str):
                    len_aux_sh+=1
                    count_type_vulnerabilityref_alienvault_sh+=1 
                elif('threat' in aux_str):
                    len_aux_sh+=1
                    count_type_threatactoref_alienvault_sh+=1
                else:
                    if(aux_str!='NONE'):
                        len_aux_sh+=1
                        count_type_anotheref_alienvault_sh+=1
    else:
        if('identity' in df_alienvault_sh["object_refs"][r]):
            len_aux_sh+=1
            count_type_identityref_alienvault_sh+=1
        elif('indicator' in df_alienvault_sh["object_refs"][r]):
            len_aux_sh+=1
            count_type_indicatoref_alienvault_sh+=1
        elif('vulnerability' in df_alienvault_sh["object_refs"][r]):
            len_aux_sh+=1
            count_type_vulnerabilityref_alienvault_sh+=1 
        elif('threat' in df_alienvault_sh["object_refs"][r]):
            len_aux_sh+=1
            count_type_threatactoref_alienvault_sh+=1
        else:
            if(df_alienvault_sh["object_refs"][r]!='NONE'):
                len_aux_sh+=1
                count_type_anotheref_alienvault_sh+=1

print("**************************ESTADÍSTICAS TIPO DE OBJETO DE REFERENCIA PULSOS ALIENVAULT PARTE SMART HOME********************************")
print("\n")
print("HAY "+str(count_type_identityref_alienvault_sh)+" OBJETOS DE REFERENCIA DE TIPO IDENTIDAD \n")
print("HAY "+str(count_type_indicatoref_alienvault_sh)+" OBJETOS DE REFERENCIA DE TIPO INDICADOR \n")
print("HAY "+str(count_type_vulnerabilityref_alienvault_sh)+" OBJETOS DE REFERENCIA DE TIPO VULNERABILIDAD \n")
print("HAY "+str(count_type_threatactoref_alienvault_sh)+" OBJETOS DE REFERENCIA DE TIPO ACTOR DE AMENAZAS \n")
print("HAY "+str(count_type_anotheref_alienvault_sh)+" OBJETOS DE REFERENCIA DE TIPO NO ESPECIFICADO \n")
print("\n")
print("**************************PORCENTAJE TIPO DE OBJETO DE REFERENCIA PULSOS ALIENVAULT PARTE SMART HOME********************************")
print("\n")

print("EL "+str(float((((count_type_identityref_alienvault_sh)*100)/len_aux_sh)))+"% DE LOS OBJETOS DE REFERENCIA ES DE TIPO IDENTIDAD \n")
print("EL "+str(float((((count_type_indicatoref_alienvault_sh)*100)/len_aux_sh)))+"% DE LOS OBJETOS DE REFERENCIA ES DE TIPO INDICADOR \n")
print("EL "+str(float((((count_type_vulnerabilityref_alienvault_sh)*100)/len_aux_sh)))+"% DE LOS OBJETOS DE REFERENCIA ES DE TIPO VULNERABILIDAD \n")
print("EL "+str(float((((count_type_threatactoref_alienvault_sh)*100)/len_aux_sh)))+"% DE LOS OBJETOS DE REFERENCIA ES DE TIPO ACTOR DE AMENAZAS \n")
print("EL "+str(float((((count_type_anotheref_alienvault_sh)*100)/len_aux_sh)))+"% DE LOS OBJETOS DE REFERENCIA NO TIENE TIPO ESPECIFICADO \n")
print("\n")





        

print("**************************ESTADÍSTICAS TIPO DE OBJETO DE REFERENCIA PULSOS ALIENVAULT PARTE IOT Y SMART HOME CONJUNTAS********************************")
print("\n")
print("HAY "+str(count_type_identityref_alienvault_sh+count_type_identityref_alienvault_iot)+" OBJETOS DE REFERENCIA DE TIPO IDENTIDAD \n")
print("HAY "+str(count_type_indicatoref_alienvault_sh+count_type_indicatoref_alienvault_iot)+" OBJETOS DE REFERENCIA DE TIPO INDICADOR \n")
print("HAY "+str(count_type_vulnerabilityref_alienvault_sh+count_type_vulnerabilityref_alienvault_iot)+" OBJETOS DE REFERENCIA DE TIPO VULNERABILIDAD \n")
print("HAY "+str(count_type_threatactoref_alienvault_sh+count_type_threatactoref_alienvault_iot)+" OBJETOS DE REFERENCIA DE TIPO ACTOR DE AMENAZAS \n")
print("HAY "+str(count_type_anotheref_alienvault_sh+count_type_anotheref_alienvault_iot)+" OBJETOS DE REFERENCIA SIN TIPO ESPECIFICADO \n")

print("\n")
print("**************************PORCENTAJE TIPO DE OBJETO DE REFERENCIA PULSOS ALIENVAULT PARTE IOT Y SMART HOME CONJUNTAS********************************")
print("\n")

print("EL "+str(float((((count_type_identityref_alienvault_sh+count_type_identityref_alienvault_iot)*100)/(len_aux_iot+len_aux_sh))))+"% DE LOS OBJETOS DE REFERENCIA ES DE TIPO IDENTIDAD \n")
print("EL "+str(float((((count_type_indicatoref_alienvault_sh+count_type_indicatoref_alienvault_iot)*100)/(len_aux_iot+len_aux_sh))))+" % DE LOS OBJETOS DE REFERENCIA ES DE TIPO INDICADOR \n")
print("EL "+str(float((((count_type_vulnerabilityref_alienvault_sh+count_type_vulnerabilityref_alienvault_iot)*100)/(len_aux_iot+len_aux_sh))))+" % DE LOS OBJETOS DE REFERENCIA ES DE TIPO VULNERABILIDAD \n")
print("EL "+str(float((((count_type_threatactoref_alienvault_sh+count_type_threatactoref_alienvault_iot)*100)/(len_aux_iot+len_aux_sh))))+" % DE LOS OBJETOS DE REFERENCIA ES DE TIPO ACTOR DE AMENAZAS \n")
print("EL "+str(float((((count_type_anotheref_alienvault_sh+count_type_anotheref_alienvault_iot)*100)/(len_aux_iot+len_aux_sh))))+" % DE LOS OBJETOS DE REFERENCIA NO TIENE TIPO ESPECIFICADO  \n")
print("\n")

















