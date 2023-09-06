import pandas as pd
from datetime import datetime

#Abro los ficheros con los que voy a tratar


df_malw_ana_iot = pd.read_excel('ibm_analisis_maliciosos_iot_2023_v2.xlsx')

#Variable para almacenar contador total de OBJETOS DE REFERENCIA
count_malw_ana_iot_refs=0
#Variable para almacenar contador total de vulnerabilidades
count_malw_ana_iot_total=0
#Variables para almacenar cantidad total de vulnerabilidades de un tipo
count_malw_ana_iot_typereport=0
#Variables para almacenar cantidad de OBJETOS DE REFERENCIA de un determinado valor, teniendo especificado previamente un tipo
count_malw_ana_iot_typereport_refindicator=0
count_malw_ana_iot_typereport_refmarkingdefinition=0

count_malw_ana_iot_typeindicator=0
count_malw_ana_iot_typeindicator_refindicator=0
count_malw_ana_iot_typeindicator_refmarkingdefinition=0

count_malw_ana_iot_typemarkingdefinition=0
count_malw_ana_iot_typemarkingdefinition_refindicator=0
count_malw_ana_iot_typemarkingdefinition_refmarkingdefinition=0
#Contador de total de tipos de OBJETOS DE REFERENCIA
count_malw_ana_iot_refindicator=0
count_malw_ana_iot_refmarkingdefinition=0

#Comprobamos el tipo de OBJETO
for r in range(0,len(df_malw_ana_iot["type"])):
    #Comprobamos si hay distintos valores de tipo en una misma fila
    if('[' in df_malw_ana_iot["type"][r]):
        aux=df_malw_ana_iot["type"][r].split(",")
        #Recorro los distintos valores de tipo
        for l in range(0,len(aux)):
            if(len(aux)>0):
                #Obtengo las distintas OBJETOS DE REFERENCIA de la fila actual
                auxx=df_malw_ana_iot["object_refs"][r].split("]")
                #String donde almacenare las distintas OBJETOS DE REFERENCIA para un tipo de una misma fila
                straux=""
                for t in range(0,len(auxx)):
                    if(auxx[t]!=""):
                        aux2=auxx[t].replace(', [', '').replace(']', '').replace(" ",'').replace('[','')
                        straux+="/"+aux2
                aux3=straux.split("/")
                #Obtengo el valor de tipo actual de la fila que estamos recorriendo
                aux_str=aux[l].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
                if(aux_str!='NONE'):
                    count_malw_ana_iot_total+=1
                    if(aux_str == 'report'):
                        count_malw_ana_iot_typereport+=1
                        aux4=aux3[l+1].replace("'","").replace("'","")
                        if(aux4!='NONE'):
                            #Si el valor de OBJETOS DE REFERENCIA para el tipo actual tiene varios valores
                            if("," in aux3[l+1]):
                                aux_array=aux3[l+1].split(",")
                                #Obtengo los distintos valores de OBJETOS DE REFERENCIA para un mismo tipo en la fila actual y los recorro
                                for k in range(0,len(aux_array)):
                                    if(len(aux_array)>0):
                                        if('indicator' in aux_array[k]):
                                            count_malw_ana_iot_refs+=1
                                            count_malw_ana_iot_refindicator+=1
                                            count_malw_ana_iot_typereport_refindicator+=1
                                        elif('marking-definition' in aux_array[k]):
                                            count_malw_ana_iot_refs+=1
                                            count_malw_ana_iot_refmarkingdefinition+=1
                                            count_malw_ana_iot_typereport_refmarkingdefinition+=1
                            else:
                                #Si existe un unico valor de referencia para el valor de tipo actual de la fila en la que estamos
                                if('indicator' in aux4):
                                    count_malw_ana_iot_refs+=1
                                    count_malw_ana_iot_refindicator+=1
                                    count_malw_ana_iot_typereport_refindicator+=1
                                elif('marking-definition' in aux4):
                                    count_malw_ana_iot_refs+=1
                                    count_malw_ana_iot_refmarkingdefinition+=1
                                    count_malw_ana_iot_typereport_refmarkingdefinition+=1
        
                    elif(aux_str == 'indicator'):
                        count_malw_ana_iot_typeindicator+=1
                        aux44=aux3[l+1].replace("'","").replace("'","")
                        if(aux44!='NONE'):
                            if("," in aux3[l+1]):
                                auxx_array=aux3[l+1].split(",")
                                for p in range(0,len(auxx_array)):
                                    if(len(auxx_array)>0):
                                        if('indicator' in auxx_array[p]):
                                            count_malw_ana_iot_refs+=1
                                            count_malw_ana_iot_refindicator+=1
                                            count_malw_ana_iot_typeindicator_refindicator+=1
                                        elif('marking-definition' in auxx_array[p]):
                                            count_malw_ana_iot_refs+=1
                                            count_malw_ana_iot_refmarkingdefinition+=1
                                            count_malw_ana_iot_typeindicator_refmarkingdefinition+=1
                                            
                            else:
                                #Si existe un unico valor de referencia para el valor de tipo actual de la fila en la que estamos
                                if('indicator' in aux44):
                                    count_malw_ana_iot_refs+=1
                                    count_malw_ana_iot_refindicator+=1
                                    count_malw_ana_iot_typeindicator_refindicator+=1
                                elif('marking-definition' in aux44):
                                    count_malw_ana_iot_refs+=1
                                    count_malw_ana_iot_refmarkingdefinition+=1
                                    count_malw_ana_iot_typeindicator_refmarkingdefinition+=1
                    elif(aux_str == 'marking-definition'):
                        count_malw_ana_iot_typemarkingdefinition+=1
                        aux444=aux3[l+1].replace("'","").replace("'","")
                        if(aux444!='NONE'):
                            if("," in aux3[l+1]):
                                auxxx_array=aux3[l+1].split(",")
                                for c in range(0,len(auxxx_array)):
                                    if(len(auxxx_array)>0):
                                        if('indicator' in auxxx_array[c]):
                                            count_malw_ana_iot_refs+=1
                                            count_malw_ana_iot_refindicator+=1
                                            count_malw_ana_iot_typemarkingdefinition_refindicator+=1
                                        elif('marking-definition' in auxxx_array[c]):
                                            count_malw_ana_iot_refs+=1
                                            count_malw_ana_iot_refmarkingdefinition+=1
                                            count_malw_ana_iot_typemarkingdefinition_refmarkingdefinition+=1 
                            else:
                                #Si existe un unico valor de referencia para el valor de tipo actual de la fila en la que estamos
                                if('indicator' in aux444):
                                    count_malw_ana_iot_refs+=1
                                    count_malw_ana_iot_refindicator+=1
                                    count_malw_ana_iot_typemarkingdefinition_refindicator+=1
                                elif('marking-definition' in aux444):
                                    count_malw_ana_iot_refs+=1
                                    count_malw_ana_iot_refmarkingdefinition+=1
                                    count_malw_ana_iot_typemarkingdefinition_refmarkingdefinition+=1
    else:
        #Si existe un unico valor de tipo para la fila actual
        if(df_malw_ana_iot["type"][r] == 'report'):
            count_malw_ana_iot_total+=1
            count_malw_ana_iot_typereport+=1  
            refs_typereport_iot=df_malw_ana_iot["object_refs"][r].split(",")
            if(len(refs_typereport_iot)>0):
                for b in range(0,len(refs_typereport_iot)):
                    ref_typereport_iot=refs_typereport_iot[b].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
                    if(ref_typereport_iot!='NONE'):
                        if('indicator' in ref_typereport_iot):
                            count_malw_ana_iot_refs+=1
                            count_malw_ana_iot_refindicator+=1
                            count_malw_ana_iot_typereport_refindicator+=1
                        elif('marking-definition' in ref_typereport_iot):
                            count_malw_ana_iot_refs+=1
                            count_malw_ana_iot_refmarkingdefinition+=1
                            count_malw_ana_iot_typereport_refmarkingdefinition+=1
        
        elif(df_malw_ana_iot["type"][r] == 'indicator'):
            count_malw_ana_iot_total+=1
            count_malw_ana_iot_typeindicator+=1  
            refs_typeindicator_iot=df_malw_ana_iot["object_refs"][r].split(",")
            if(len(refs_typeindicator_iot)>0):
                for b in range(0,len(refs_typeindicator_iot)):
                    ref_typeindicator_iot=refs_typeindicator_iot[b].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
                    if(ref_typeindicator_iot!='NONE'):
                        if('indicator' in ref_typeindicator_iot):
                            count_malw_ana_iot_refs+=1
                            count_malw_ana_iot_refindicator+=1
                            count_malw_ana_iot_typeindicator_refindicator+=1
                        elif('marking-definition' in ref_typeindicator_iot):
                            count_malw_ana_iot_refs+=1
                            count_malw_ana_iot_refmarkingdefinition+=1
                            count_malw_ana_iot_typeindicator_refmarkingdefinition+=1
                            
        elif(df_malw_ana_iot["type"][r] == 'marking-definition'):
            count_malw_ana_iot_total+=1
            count_malw_ana_iot_typemarkingdefinition+=1  
            refs_typemarkingdefinition_iot=df_malw_ana_iot["object_refs"][r].split(",")
            if(len(refs_typemarkingdefinition_iot)>0):
                for b in range(0,len(refs_typemarkingdefinition_iot)):
                    ref_typemarkingdefinition_iot=refs_typemarkingdefinition_iot[b].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
                    if(ref_typemarkingdefinition_iot!='NONE'):
                        if('indicator' in ref_typemarkingdefinition_iot):
                            count_malw_ana_iot_refs+=1
                            count_malw_ana_iot_refindicator+=1
                            count_malw_ana_iot_typemarkingdefinition_refindicator+=1
                        elif('marking-definition' in ref_typemarkingdefinition_iot):
                            count_malw_ana_iot_refs+=1
                            count_malw_ana_iot_refmarkingdefinition+=1
                            count_malw_ana_iot_typemarkingdefinition_refmarkingdefinition+=1   
       
                    

        
        
print("*************ESTADÍSTICAS TIPO DE OBJETO/TIPO DE OBJETO DE REFERENCIA INFORMES ANALISIS MALICIOSOS IBM PARTE IOT*************")
print("\n")                            
                
print("\n")
print(" DE UN TOTAL DE "+str(count_malw_ana_iot_total)+" OBJETOS :\n") 
print("\n")
print("   - LAS ESTADISTICAS DE TIPO DE OBJETO SON LAS SIGUIENTES:  \n")
print("      -    EN  "+str(count_malw_ana_iot_typereport)+" OBJETOS EL TIPO DE OBJETO ES REPORTE  \n")
print("      -    EN  "+str(count_malw_ana_iot_typeindicator)+" OBJETOS EL TIPO DE OBJETO ES INDICADOR  \n")
print("      -    EN  "+str(count_malw_ana_iot_typemarkingdefinition)+" OBJETOS EL TIPO DE OBJETO ES DEFINICION DE MARCADO  \n")
print("\n")
print(" DE UN TOTAL DE "+str(count_malw_ana_iot_refs)+" OBJETOS DE REFERENCIA DE OBJETOS :\n") 
print("\n")
print("   - LAS ESTADISTICAS DE TIPO DE OBJETO DE REFERENCIA SON LAS SIGUIENTES:  \n")
print("      -    EN  "+str(count_malw_ana_iot_refindicator)+" OBJETOS DE REFERENCIA EL TIPO DE OBJETOS DE REFERENCIA ES INDICADOR \n")
print("      -    EN  "+str(count_malw_ana_iot_refmarkingdefinition)+" OBJETOS DE REFERENCIA EL TIPO DE OBJETOS DE REFERENCIA ES DEFINICION DE MARCADO  \n")
print("                -    EN  "+str(count_malw_ana_iot_typereport_refindicator+count_malw_ana_iot_typereport_refmarkingdefinition)+" OBJETOS DE REFERENCIA DONDE EL TIPO DE OBJETO ES REPORTE, LAS ESTADÍSTICAS DE TIPO DE OBJETO DE REFERENCIA SON LAS SIGUIENTES:  \n")
print("                           -    EN  "+str(count_malw_ana_iot_typereport_refindicator)+" OBJETOS DE REFERENCIA EL TIPO DE OBJETO DE REFERENCIA ES INDICADOR  \n")
print("                           -    EN  "+str(count_malw_ana_iot_typereport_refmarkingdefinition)+" OBJETOS DE REFERENCIA EL TIPO DE OBJETO DE REFERENCIA ES DEFINICION DE MARCADO \n")
print("\n")
print("                -    EN  "+str(count_malw_ana_iot_typeindicator_refindicator+count_malw_ana_iot_typeindicator_refmarkingdefinition)+" OBJETOS DE REFERENCIA DONDE EL TIPO DE OBJETO ES INDICADOR, LAS ESTADÍSTICAS DE TIPO DE OBJETO DE REFERENCIA SON LAS SIGUIENTES:  \n")
print("                           -    EN  "+str(count_malw_ana_iot_typeindicator_refindicator)+" OBJETOS DE REFERENCIA EL TIPO DE OBJETO DE REFERENCIA ES INDICADOR  \n")
print("                           -    EN  "+str(count_malw_ana_iot_typeindicator_refmarkingdefinition)+" OBJETOS DE REFERENCIA EL TIPO DE OBJETO DE REFERENCIA ES DEFINICION DE MARCADO \n")
print("\n") 
print("                -    EN  "+str(count_malw_ana_iot_typemarkingdefinition_refindicator+count_malw_ana_iot_typemarkingdefinition_refmarkingdefinition)+" OBJETOS DE REFERENCIA DONDE EL TIPO DE OBJETO ES DEFINICION DE MARCADO, LAS ESTADÍSTICAS DE TIPO DE OBJETO DE REFERENCIA SON LAS SIGUIENTES:  \n")
print("                           -    EN  "+str(count_malw_ana_iot_typemarkingdefinition_refindicator)+" OBJETOS DE REFERENCIA EL TIPO DE OBJETO DE REFERENCIA ES INDICADOR  \n")
print("                           -    EN  "+str(count_malw_ana_iot_typemarkingdefinition_refmarkingdefinition)+" OBJETOS DE REFERENCIA EL TIPO DE OBJETO DE REFERENCIA ES DEFINICION DE MARCADO \n")











print("*************PORCENTAJE TIPO DE OBJETO/TIPO DE OBJETO DE REFERENCIA INFORMES ANALISIS MALICIOSOS IBM PARTE IOT*************")
print("\n")                            
                
print("\n")
print(" DE UN TOTAL DE "+str(count_malw_ana_iot_total)+" OBJETOS :\n") 
print("\n")
print("   - LOS PORCENTAJES DE TIPO DE OBJETO  SON LOS SIGUIENTES:  \n")
print("      -    EN EL  "+str(float(((count_malw_ana_iot_typereport*100)/count_malw_ana_iot_total)))+" % DE OBJETOS EL TIPO DE OBJETO ES REPORTE  \n")
print("      -    EN EL  "+str(float(((count_malw_ana_iot_typeindicator*100)/count_malw_ana_iot_total)))+" % DE OBJETOS EL TIPO DE OBJETO ES INDICADOR  \n")
print("      -    EN EL  "+str(float(((count_malw_ana_iot_typemarkingdefinition*100)/count_malw_ana_iot_total)))+" % DE OBJETOS EL TIPO DE OBJETO ES DEFINICION DE MARCADO  \n")
print("\n")
print("\n")
print(" DE UN TOTAL DE "+str(count_malw_ana_iot_refs)+" OBJETOS DE REFERENCIA DE OBJETOS :\n") 
print("\n")
print("   - LOS PORCENTAJES DE TIPO DE OBJETO DE REFERENCIA SON LOS SIGUIENTES:  \n")
print("      -    EN  EL "+str(float(((count_malw_ana_iot_refindicator*100)/count_malw_ana_iot_refs)))+" % DE OBJETOS DE REFERENCIA EL TIPO DE OBJETOS DE REFERENCIA ES INDICADOR \n")
print("      -    EN  EL "+str(float(((count_malw_ana_iot_refmarkingdefinition*100)/count_malw_ana_iot_refs)))+" % DE OBJETOS DE REFERENCIA EL TIPO DE OBJETOS DE REFERENCIA ES DEFINICION DE MARCADO  \n")
print("                -    EN  EL "+str(float((((count_malw_ana_iot_typereport_refindicator+count_malw_ana_iot_typereport_refmarkingdefinition)*100)/count_malw_ana_iot_refs)))+" % DE OBJETOS DE REFERENCIA DONDE EL TIPO DE OBJETO ES REPORTE, LOS PORCENTAJES DE TIPO DE OBJETO DE REFERENCIA SON LOS SIGUIENTES:  \n")
print("                           -    EN  EL "+str(float(((count_malw_ana_iot_typereport_refindicator*100)/(count_malw_ana_iot_typereport_refindicator+count_malw_ana_iot_typereport_refmarkingdefinition))))+" % DE OBJETOS DE REFERENCIA EL TIPO DE OBJETO DE REFERENCIA ES INDICADOR  \n")
print("                           -    EN  EL "+str(float(((count_malw_ana_iot_typereport_refmarkingdefinition*100)/(count_malw_ana_iot_typereport_refindicator+count_malw_ana_iot_typereport_refmarkingdefinition))))+" % DE OBJETOS DE REFERENCIA EL TIPO DE OBJETO DE REFERENCIA ES DEFINICION DE MARCADO \n")
print("\n")
if((count_malw_ana_iot_typeindicator_refindicator+count_malw_ana_iot_typeindicator_refmarkingdefinition)>0):
    print("                -    EN  EL "+str(float((((count_malw_ana_iot_typeindicator_refindicator+count_malw_ana_iot_typeindicator_refmarkingdefinition)*100)/count_malw_ana_iot_refs)))+" % DE OBJETOS DE REFERENCIA DONDE EL TIPO DE OBJETO ES INDICADOR, LOS PORCENTAJES DE TIPO DE OBJETO DE REFERENCIA SON LOS SIGUIENTES:   \n")
    print("                           -    EN  EL "+str(float(((count_malw_ana_iot_typeindicator_refindicator*100)/(count_malw_ana_iot_typeindicator_refindicator+count_malw_ana_iot_typeindicator_refmarkingdefinition))))+" % DE OBJETOS DE REFERENCIA EL TIPO DE OBJETO DE REFERENCIA ES INDICADOR  \n")
    print("                           -    EN  EL "+str(float(((count_malw_ana_iot_typeindicator_refmarkingdefinition*100)/(count_malw_ana_iot_typeindicator_refindicator+count_malw_ana_iot_typeindicator_refmarkingdefinition))))+" % DE OBJETOS DE REFERENCIA EL TIPO DE OBJETO DE REFERENCIA ES DEFINICION DE MARCADO \n")
    print("\n")
if((count_malw_ana_iot_typemarkingdefinition_refindicator+count_malw_ana_iot_typemarkingdefinition_refmarkingdefinition)>0):
    print("                -    EN  EL "+str(float((((count_malw_ana_iot_typemarkingdefinition_refindicator+count_malw_ana_iot_typemarkingdefinition_refmarkingdefinition)*100)/count_malw_ana_iot_refs)))+" % DE OBJETOS DE REFERENCIA DONDE EL TIPO DE OBJETO ES INDICADOR, LOS PORCENTAJES DE TIPO DE OBJETO DE REFERENCIA SON LOS SIGUIENTES:   \n")
    print("                           -    EN  EL "+str(float(((count_malw_ana_iot_typemarkingdefinition_refindicator*100)/(count_malw_ana_iot_typemarkingdefinition_refindicator+count_malw_ana_iot_typemarkingdefinition_refmarkingdefinition))))+" % DE OBJETOS DE REFERENCIA EL TIPO DE OBJETO DE REFERENCIA ES INDICADOR  \n")
    print("                           -    EN  EL "+str(float(((count_malw_ana_iot_typemarkingdefinition_refmarkingdefinition*100)/(count_malw_ana_iot_typemarkingdefinition_refindicator+count_malw_ana_iot_typemarkingdefinition_refmarkingdefinition))))+" % DE OBJETOS DE REFERENCIA EL TIPO DE OBJETO DE REFERENCIA ES DEFINICION DE MARCADO \n")
    print("\n")

    
    
    
    
    
    
    




df_malw_ana_sh = pd.read_excel('ibm_analisis_maliciosos_smarthome_2023.xlsx')

#Variable para almacenar contador total de OBJETOS DE REFERENCIA
count_malw_ana_sh_refs=0
#Variable para almacenar contador total de vulnerabilidades
count_malw_ana_sh_total=0
#Variables para almacenar cantidad total de vulnerabilidades de un tipo
count_malw_ana_sh_typereport=0
#Variables para almacenar cantidad de OBJETOS DE REFERENCIA de un determinado valor, teniendo especificado previamente un tipo
count_malw_ana_sh_typereport_refindicator=0
count_malw_ana_sh_typereport_refmarkingdefinition=0

count_malw_ana_sh_typeindicator=0
count_malw_ana_sh_typeindicator_refindicator=0
count_malw_ana_sh_typeindicator_refmarkingdefinition=0

count_malw_ana_sh_typemarkingdefinition=0
count_malw_ana_sh_typemarkingdefinition_refindicator=0
count_malw_ana_sh_typemarkingdefinition_refmarkingdefinition=0
#Contador de total de tipos de OBJETOS DE REFERENCIA
count_malw_ana_sh_refindicator=0
count_malw_ana_sh_refmarkingdefinition=0

#Comprobamos el tipo de OBJETO
for r in range(0,len(df_malw_ana_sh["type"])):
    #Comprobamos si hay distintos valores de tipo en una misma fila
    if('[' in df_malw_ana_sh["type"][r]):
        aux=df_malw_ana_sh["type"][r].split(",")
        #Recorro los distintos valores de tipo
        for l in range(0,len(aux)):
            if(len(aux)>0):
                #Obtengo las distintas OBJETOS DE REFERENCIA de la fila actual
                auxx=df_malw_ana_sh["object_refs"][r].split("]")
                #String donde almacenare las distintas OBJETOS DE REFERENCIA para un tipo de una misma fila
                straux=""
                for t in range(0,len(auxx)):
                    if(auxx[t]!=""):
                        aux2=auxx[t].replace(', [', '').replace(']', '').replace(" ",'').replace('[','')
                        straux+="/"+aux2
                aux3=straux.split("/")
                #Obtengo el valor de tipo actual de la fila que estamos recorriendo
                aux_str=aux[l].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
                if(aux_str!='NONE'):
                    count_malw_ana_sh_total+=1
                    if(aux_str == 'report'):
                        count_malw_ana_sh_typereport+=1
                        aux4=aux3[l+1].replace("'","").replace("'","")
                        if(aux4!='NONE'):
                            #Si el valor de OBJETOS DE REFERENCIA para el tipo actual tiene varios valores
                            if("," in aux3[l+1]):
                                aux_array=aux3[l+1].split(",")
                                #Obtengo los distintos valores de OBJETOS DE REFERENCIA para un mismo tipo en la fila actual y los recorro
                                for k in range(0,len(aux_array)):
                                    if(len(aux_array)>0):
                                        if('indicator' in aux_array[k]):
                                            count_malw_ana_sh_refs+=1
                                            count_malw_ana_sh_refindicator+=1
                                            count_malw_ana_sh_typereport_refindicator+=1
                                        elif('marking-definition' in aux_array[k]):
                                            count_malw_ana_sh_refs+=1
                                            count_malw_ana_sh_refmarkingdefinition+=1
                                            count_malw_ana_sh_typereport_refmarkingdefinition+=1
                            else:
                                #Si existe un unico valor de referencia para el valor de tipo actual de la fila en la que estamos
                                if('indicator' in aux4):
                                    count_malw_ana_sh_refs+=1
                                    count_malw_ana_sh_refindicator+=1
                                    count_malw_ana_sh_typereport_refindicator+=1
                                elif('marking-definition' in aux4):
                                    count_malw_ana_sh_refs+=1
                                    count_malw_ana_sh_refmarkingdefinition+=1
                                    count_malw_ana_sh_typereport_refmarkingdefinition+=1
        
                    elif(aux_str == 'indicator'):
                        count_malw_ana_sh_typeindicator+=1
                        aux44=aux3[l+1].replace("'","").replace("'","")
                        if(aux44!='NONE'):
                            if("," in aux3[l+1]):
                                auxx_array=aux3[l+1].split(",")
                                for p in range(0,len(auxx_array)):
                                    if(len(auxx_array)>0):
                                        if('indicator' in auxx_array[p]):
                                            count_malw_ana_sh_refs+=1
                                            count_malw_ana_sh_refindicator+=1
                                            count_malw_ana_sh_typeindicator_refindicator+=1
                                        elif('marking-definition' in auxx_array[p]):
                                            count_malw_ana_sh_refs+=1
                                            count_malw_ana_sh_refmarkingdefinition+=1
                                            count_malw_ana_sh_typeindicator_refmarkingdefinition+=1
                                            
                            else:
                                #Si existe un unico valor de referencia para el valor de tipo actual de la fila en la que estamos
                                if('indicator' in aux44):
                                    count_malw_ana_sh_refs+=1
                                    count_malw_ana_sh_refindicator+=1
                                    count_malw_ana_sh_typeindicator_refindicator+=1
                                elif('marking-definition' in aux44):
                                    count_malw_ana_sh_refs+=1
                                    count_malw_ana_sh_refmarkingdefinition+=1
                                    count_malw_ana_sh_typeindicator_refmarkingdefinition+=1
                    elif(aux_str == 'marking-definition'):
                        count_malw_ana_sh_typemarkingdefinition+=1
                        aux444=aux3[l+1].replace("'","").replace("'","")
                        if(aux444!='NONE'):
                            if("," in aux3[l+1]):
                                auxxx_array=aux3[l+1].split(",")
                                for c in range(0,len(auxxx_array)):
                                    if(len(auxxx_array)>0):
                                        if('indicator' in auxxx_array[c]):
                                            count_malw_ana_sh_refs+=1
                                            count_malw_ana_sh_refindicator+=1
                                            count_malw_ana_sh_typemarkingdefinition_refindicator+=1
                                        elif('marking-definition' in auxxx_array[c]):
                                            count_malw_ana_sh_refs+=1
                                            count_malw_ana_sh_refmarkingdefinition+=1
                                            count_malw_ana_sh_typemarkingdefinition_refmarkingdefinition+=1 
                            else:
                                #Si existe un unico valor de referencia para el valor de tipo actual de la fila en la que estamos
                                if('indicator' in aux444):
                                    count_malw_ana_sh_refs+=1
                                    count_malw_ana_sh_refindicator+=1
                                    count_malw_ana_sh_typemarkingdefinition_refindicator+=1
                                elif('marking-definition' in aux444):
                                    count_malw_ana_sh_refs+=1
                                    count_malw_ana_sh_refmarkingdefinition+=1
                                    count_malw_ana_sh_typemarkingdefinition_refmarkingdefinition+=1
    else:
        #Si existe un unico valor de tipo para la fila actual
        if(df_malw_ana_sh["type"][r] == 'report'):
            count_malw_ana_sh_total+=1
            count_malw_ana_sh_typereport+=1  
            refs_typereport_sh=df_malw_ana_sh["object_refs"][r].split(",")
            if(len(refs_typereport_sh)>0):
                for b in range(0,len(refs_typereport_sh)):
                    ref_typereport_sh=refs_typereport_sh[b].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
                    if(ref_typereport_sh!='NONE'):
                        if('indicator' in ref_typereport_sh):
                            count_malw_ana_sh_refs+=1
                            count_malw_ana_sh_refindicator+=1
                            count_malw_ana_sh_typereport_refindicator+=1
                        elif('marking-definition' in ref_typereport_sh):
                            count_malw_ana_sh_refs+=1
                            count_malw_ana_sh_refmarkingdefinition+=1
                            count_malw_ana_sh_typereport_refmarkingdefinition+=1
        
        elif(df_malw_ana_sh["type"][r] == 'indicator'):
            count_malw_ana_sh_total+=1
            count_malw_ana_sh_typeindicator+=1  
            refs_typeindicator_sh=df_malw_ana_sh["object_refs"][r].split(",")
            if(len(refs_typeindicator_sh)>0):
                for b in range(0,len(refs_typeindicator_sh)):
                    ref_typeindicator_sh=refs_typeindicator_sh[b].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
                    if(ref_typeindicator_sh!='NONE'):
                        if('indicator' in ref_typeindicator_sh):
                            count_malw_ana_sh_refs+=1
                            count_malw_ana_sh_refindicator+=1
                            count_malw_ana_sh_typeindicator_refindicator+=1
                        elif('marking-definition' in ref_typeindicator_sh):
                            count_malw_ana_sh_refs+=1
                            count_malw_ana_sh_refmarkingdefinition+=1
                            count_malw_ana_sh_typeindicator_refmarkingdefinition+=1
                            
        elif(df_malw_ana_sh["type"][r] == 'marking-definition'):
            count_malw_ana_sh_total+=1
            count_malw_ana_sh_typemarkingdefinition+=1  
            refs_typemarkingdefinition_sh=df_malw_ana_sh["object_refs"][r].split(",")
            if(len(refs_typemarkingdefinition_sh)>0):
                for b in range(0,len(refs_typemarkingdefinition_sh)):
                    ref_typemarkingdefinition_sh=refs_typemarkingdefinition_sh[b].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
                    if(ref_typemarkingdefinition_sh!='NONE'):
                        if('indicator' in ref_typemarkingdefinition_sh):
                            count_malw_ana_sh_refs+=1
                            count_malw_ana_sh_refindicator+=1
                            count_malw_ana_sh_typemarkingdefinition_refindicator+=1
                        elif('marking-definition' in ref_typemarkingdefinition_sh):
                            count_malw_ana_sh_refs+=1
                            count_malw_ana_sh_refmarkingdefinition+=1
                            count_malw_ana_sh_typemarkingdefinition_refmarkingdefinition+=1   
       
                    

        
        
print("*************ESTADÍSTICAS TIPO DE OBJETO/TIPO DE OBJETO DE REFERENCIA INFORMES ANALISIS MALICIOSOS IBM PARTE SMART HOME*************")
print("\n")                            
                
print("\n")
print(" DE UN TOTAL DE "+str(count_malw_ana_sh_total)+" OBJETOS :\n") 
print("\n")
print("   - LAS ESTADISTICAS DE TIPO DE OBJETO SON LAS SIGUIENTES:  \n")
print("      -    EN  "+str(count_malw_ana_sh_typereport)+" OBJETOS EL TIPO DE OBJETO ES REPORTE  \n")
print("      -    EN  "+str(count_malw_ana_sh_typeindicator)+" OBJETOS EL TIPO DE OBJETO ES INDICADOR  \n")
print("      -    EN  "+str(count_malw_ana_sh_typemarkingdefinition)+" OBJETOS EL TIPO DE OBJETO ES DEFINICION DE MARCADO  \n")
print("\n")
print(" DE UN TOTAL DE "+str(count_malw_ana_sh_refs)+" OBJETOS DE REFERENCIA DE OBJETOS :\n") 
print("\n")
print("   - LAS ESTADISTICAS DE TIPO DE OBJETO DE REFERENCIA SON LAS SIGUIENTES:  \n")
print("      -    EN  "+str(count_malw_ana_sh_refindicator)+" OBJETOS DE REFERENCIA EL TIPO DE OBJETOS DE REFERENCIA ES INDICADOR \n")
print("      -    EN  "+str(count_malw_ana_sh_refmarkingdefinition)+" OBJETOS DE REFERENCIA EL TIPO DE OBJETOS DE REFERENCIA ES DEFINICION DE MARCADO  \n")
print("                -    EN  "+str(count_malw_ana_sh_typereport_refindicator+count_malw_ana_sh_typereport_refmarkingdefinition)+" OBJETOS DE REFERENCIA DONDE EL TIPO DE OBJETO ES REPORTE, LAS ESTADÍSTICAS DE TIPO DE OBJETO DE REFERENCIA SON LAS SIGUIENTES:  \n")
print("                           -    EN  "+str(count_malw_ana_sh_typereport_refindicator)+" OBJETOS DE REFERENCIA EL TIPO DE OBJETO DE REFERENCIA ES INDICADOR  \n")
print("                           -    EN  "+str(count_malw_ana_sh_typereport_refmarkingdefinition)+" OBJETOS DE REFERENCIA EL TIPO DE OBJETO DE REFERENCIA ES DEFINICION DE MARCADO \n")
print("\n")
print("                -    EN  "+str(count_malw_ana_sh_typeindicator_refindicator+count_malw_ana_sh_typeindicator_refmarkingdefinition)+" OBJETOS DE REFERENCIA DONDE EL TIPO DE OBJETO ES INDICADOR, LAS ESTADÍSTICAS DE TIPO DE OBJETO DE REFERENCIA SON LAS SIGUIENTES:  \n")
print("                           -    EN  "+str(count_malw_ana_sh_typeindicator_refindicator)+" OBJETOS DE REFERENCIA EL TIPO DE OBJETO DE REFERENCIA ES INDICADOR  \n")
print("                           -    EN  "+str(count_malw_ana_sh_typeindicator_refmarkingdefinition)+" OBJETOS DE REFERENCIA EL TIPO DE OBJETO DE REFERENCIA ES DEFINICION DE MARCADO \n")
print("\n") 
print("                -    EN  "+str(count_malw_ana_sh_typemarkingdefinition_refindicator+count_malw_ana_sh_typemarkingdefinition_refmarkingdefinition)+" OBJETOS DE REFERENCIA DONDE EL TIPO DE OBJETO ES DEFINICION DE MARCADO, LAS ESTADÍSTICAS DE TIPO DE OBJETO DE REFERENCIA SON LAS SIGUIENTES:  \n")
print("                           -    EN  "+str(count_malw_ana_sh_typemarkingdefinition_refindicator)+" OBJETOS DE REFERENCIA EL TIPO DE OBJETO DE REFERENCIA ES INDICADOR  \n")
print("                           -    EN  "+str(count_malw_ana_sh_typemarkingdefinition_refmarkingdefinition)+" OBJETOS DE REFERENCIA EL TIPO DE OBJETO DE REFERENCIA ES DEFINICION DE MARCADO \n")











print("*************PORCENTAJE TIPO DE OBJETO/TIPO DE OBJETO DE REFERENCIA INFORMES ANALISIS MALICIOSOS IBM PARTE SMART HOME*************")
print("\n")                            
                
print("\n")
print(" DE UN TOTAL DE "+str(count_malw_ana_sh_total)+" OBJETOS :\n") 
print("\n")
print("   - LOS PORCENTAJES DE TIPO DE OBJETO  SON LOS SIGUIENTES:  \n")
print("      -    EN EL  "+str(float(((count_malw_ana_sh_typereport*100)/count_malw_ana_sh_total)))+" % DE OBJETOS EL TIPO DE OBJETO ES REPORTE  \n")
print("      -    EN EL  "+str(float(((count_malw_ana_sh_typeindicator*100)/count_malw_ana_sh_total)))+" % DE OBJETOS EL TIPO DE OBJETO ES INDICADOR  \n")
print("      -    EN EL  "+str(float(((count_malw_ana_sh_typemarkingdefinition*100)/count_malw_ana_sh_total)))+" % DE OBJETOS EL TIPO DE OBJETO ES DEFINICION DE MARCADO  \n")
print("\n")
print("\n")
print(" DE UN TOTAL DE "+str(count_malw_ana_sh_refs)+" OBJETOS DE REFERENCIA DE OBJETOS :\n") 
print("\n")
print("   - LOS PORCENTAJES DE TIPO DE OBJETO DE REFERENCIA SON LOS SIGUIENTES:  \n")
print("      -    EN  EL "+str(float(((count_malw_ana_sh_refindicator*100)/count_malw_ana_sh_refs)))+" % DE OBJETOS DE REFERENCIA EL TIPO DE OBJETOS DE REFERENCIA ES INDICADOR \n")
print("      -    EN  EL "+str(float(((count_malw_ana_sh_refmarkingdefinition*100)/count_malw_ana_sh_refs)))+" % DE OBJETOS DE REFERENCIA EL TIPO DE OBJETOS DE REFERENCIA ES DEFINICION DE MARCADO  \n")
print("                -    EN  EL "+str(float((((count_malw_ana_sh_typereport_refindicator+count_malw_ana_sh_typereport_refmarkingdefinition)*100)/count_malw_ana_sh_refs)))+" % DE OBJETOS DE REFERENCIA DONDE EL TIPO DE OBJETO ES REPORTE, LOS PORCENTAJES DE TIPO DE OBJETO DE REFERENCIA SON LOS SIGUIENTES:  \n")
print("                           -    EN  EL "+str(float(((count_malw_ana_sh_typereport_refindicator*100)/(count_malw_ana_sh_typereport_refindicator+count_malw_ana_sh_typereport_refmarkingdefinition))))+" % DE OBJETOS DE REFERENCIA EL TIPO DE OBJETO DE REFERENCIA ES INDICADOR  \n")
print("                           -    EN  EL "+str(float(((count_malw_ana_sh_typereport_refmarkingdefinition*100)/(count_malw_ana_sh_typereport_refindicator+count_malw_ana_sh_typereport_refmarkingdefinition))))+" % DE OBJETOS DE REFERENCIA EL TIPO DE OBJETO DE REFERENCIA ES DEFINICION DE MARCADO \n")
print("\n")
if((count_malw_ana_sh_typeindicator_refindicator+count_malw_ana_sh_typeindicator_refmarkingdefinition)>0):
    print("                -    EN  EL "+str(float((((count_malw_ana_sh_typeindicator_refindicator+count_malw_ana_sh_typeindicator_refmarkingdefinition)*100)/count_malw_ana_sh_refs)))+" % DE OBJETOS DE REFERENCIA DONDE EL TIPO DE OBJETO ES INDICADOR, LOS PORCENTAJES DE TIPO DE OBJETO DE REFERENCIA SON LOS SIGUIENTES:   \n")
    print("                           -    EN  EL "+str(float(((count_malw_ana_sh_typeindicator_refindicator*100)/(count_malw_ana_sh_typeindicator_refindicator+count_malw_ana_sh_typeindicator_refmarkingdefinition))))+" % DE OBJETOS DE REFERENCIA EL TIPO DE OBJETO DE REFERENCIA ES INDICADOR  \n")
    print("                           -    EN  EL "+str(float(((count_malw_ana_sh_typeindicator_refmarkingdefinition*100)/(count_malw_ana_sh_typeindicator_refindicator+count_malw_ana_sh_typeindicator_refmarkingdefinition))))+" % DE OBJETOS DE REFERENCIA EL TIPO DE OBJETO DE REFERENCIA ES DEFINICION DE MARCADO \n")
    print("\n")
if((count_malw_ana_sh_typemarkingdefinition_refindicator+count_malw_ana_sh_typemarkingdefinition_refmarkingdefinition)>0):
    print("                -    EN  EL "+str(float((((count_malw_ana_sh_typemarkingdefinition_refindicator+count_malw_ana_sh_typemarkingdefinition_refmarkingdefinition)*100)/count_malw_ana_sh_refs)))+" % DE OBJETOS DE REFERENCIA DONDE EL TIPO DE OBJETO ES INDICADOR, LOS PORCENTAJES DE TIPO DE OBJETO DE REFERENCIA SON LOS SIGUIENTES:   \n")
    print("                           -    EN  EL "+str(float(((count_malw_ana_sh_typemarkingdefinition_refindicator*100)/(count_malw_ana_sh_typemarkingdefinition_refindicator+count_malw_ana_sh_typemarkingdefinition_refmarkingdefinition))))+" % DE OBJETOS DE REFERENCIA EL TIPO DE OBJETO DE REFERENCIA ES INDICADOR  \n")
    print("                           -    EN  EL "+str(float(((count_malw_ana_sh_typemarkingdefinition_refmarkingdefinition*100)/(count_malw_ana_sh_typemarkingdefinition_refindicator+count_malw_ana_sh_typemarkingdefinition_refmarkingdefinition))))+" % DE OBJETOS DE REFERENCIA EL TIPO DE OBJETO DE REFERENCIA ES DEFINICION DE MARCADO \n")
    print("\n")

    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
print("*************ESTADÍSTICAS TIPO DE OBJETO/TIPO DE OBJETO DE REFERENCIA INFORMES ANALISIS MALICIOSOS IBM PARTE IOT Y SMART HOME CONJUNTAS*************")
print("\n")                            
                
print("\n")
print(" DE UN TOTAL DE "+str(count_malw_ana_sh_total+count_malw_ana_iot_total)+" OBJETOS :\n") 
print("\n")
print("   - LAS ESTADISTICAS DE TIPO DE OBJETO SON LAS SIGUIENTES:  \n")
print("      -    EN  "+str(count_malw_ana_sh_typereport+count_malw_ana_iot_typereport)+" OBJETOS EL TIPO DE OBJETO ES REPORTE  \n")
print("      -    EN  "+str(count_malw_ana_sh_typeindicator+count_malw_ana_iot_typeindicator)+" OBJETOS EL TIPO DE OBJETO ES INDICADOR  \n")
print("      -    EN  "+str(count_malw_ana_sh_typemarkingdefinition+count_malw_ana_iot_typemarkingdefinition)+" OBJETOS EL TIPO DE OBJETO ES DEFINICION DE MARCADO  \n")
print("\n")
print(" DE UN TOTAL DE "+str(count_malw_ana_sh_refs+count_malw_ana_iot_refs)+" OBJETOS DE REFERENCIA DE OBJETOS :\n") 
print("\n")
print("   - LAS ESTADISTICAS DE TIPO DE OBJETO DE REFERENCIA SON LAS SIGUIENTES:  \n")
print("      -    EN  "+str(count_malw_ana_sh_refindicator+count_malw_ana_iot_refindicator)+" OBJETOS DE REFERENCIA EL TIPO DE OBJETOS DE REFERENCIA ES INDICADOR \n")
print("      -    EN  "+str(count_malw_ana_sh_refmarkingdefinition+count_malw_ana_iot_refmarkingdefinition)+" OBJETOS DE REFERENCIA EL TIPO DE OBJETOS DE REFERENCIA ES DEFINICION DE MARCADO  \n")
print("                -    EN  "+str(count_malw_ana_sh_typereport_refindicator+count_malw_ana_sh_typereport_refmarkingdefinition+count_malw_ana_iot_typereport_refindicator+count_malw_ana_iot_typereport_refmarkingdefinition)+" OBJETOS DE REFERENCIA DONDE EL TIPO DE OBJETO ES REPORTE, LAS ESTADÍSTICAS DE TIPO DE OBJETO DE REFERENCIA SON LAS SIGUIENTES:  \n")
print("                           -    EN  "+str(count_malw_ana_sh_typereport_refindicator+count_malw_ana_iot_typereport_refindicator)+" OBJETOS DE REFERENCIA EL TIPO DE OBJETO DE REFERENCIA ES INDICADOR  \n")
print("                           -    EN  "+str(count_malw_ana_sh_typereport_refmarkingdefinition+count_malw_ana_iot_typereport_refmarkingdefinition)+" OBJETOS DE REFERENCIA EL TIPO DE OBJETO DE REFERENCIA ES DEFINICION DE MARCADO \n")
print("\n")
print("                -    EN  "+str(count_malw_ana_sh_typeindicator_refindicator+count_malw_ana_sh_typeindicator_refmarkingdefinition+count_malw_ana_iot_typeindicator_refindicator+count_malw_ana_iot_typeindicator_refmarkingdefinition)+" OBJETOS DE REFERENCIA DONDE EL TIPO DE OBJETO ES INDICADOR, LAS ESTADÍSTICAS DE TIPO DE OBJETO DE REFERENCIA SON LAS SIGUIENTES:  \n")
print("                           -    EN  "+str(count_malw_ana_sh_typeindicator_refindicator+count_malw_ana_iot_typeindicator_refindicator)+" OBJETOS DE REFERENCIA EL TIPO DE OBJETO DE REFERENCIA ES INDICADOR  \n")
print("                           -    EN  "+str(count_malw_ana_sh_typeindicator_refmarkingdefinition+count_malw_ana_iot_typeindicator_refmarkingdefinition)+" OBJETOS DE REFERENCIA EL TIPO DE OBJETO DE REFERENCIA ES DEFINICION DE MARCADO \n")
print("\n") 
print("                -    EN  "+str(count_malw_ana_sh_typemarkingdefinition_refindicator+count_malw_ana_sh_typemarkingdefinition_refmarkingdefinition+count_malw_ana_iot_typemarkingdefinition_refindicator+count_malw_ana_iot_typemarkingdefinition_refmarkingdefinition)+" OBJETOS DE REFERENCIA DONDE EL TIPO DE OBJETO ES DEFINICION DE MARCADO, LAS ESTADÍSTICAS DE TIPO DE OBJETO DE REFERENCIA SON LAS SIGUIENTES:  \n")
print("                           -    EN  "+str(count_malw_ana_sh_typemarkingdefinition_refindicator+count_malw_ana_iot_typemarkingdefinition_refindicator)+" OBJETOS DE REFERENCIA EL TIPO DE OBJETO DE REFERENCIA ES INDICADOR  \n")
print("                           -    EN  "+str(count_malw_ana_sh_typemarkingdefinition_refmarkingdefinition+count_malw_ana_iot_typemarkingdefinition_refmarkingdefinition)+" OBJETOS DE REFERENCIA EL TIPO DE OBJETO DE REFERENCIA ES DEFINICION DE MARCADO \n")
















print("*************PORCENTAJE TIPO DE OBJETO/TIPO DE OBJETO DE REFERENCIA INFORMES ANALISIS MALICIOSOS IBM PARTE SMART HOME CONJUNTAS*************")
print("\n")                            
                
print("\n")
print(" DE UN TOTAL DE "+str(count_malw_ana_sh_total+count_malw_ana_iot_total)+" OBJETOS :\n") 
print("\n")
print("   - LOS PORCENTAJES DE TIPO DE OBJETO  SON LOS SIGUIENTES:  \n")
print("      -    EN EL  "+str(float((((count_malw_ana_sh_typereport+count_malw_ana_iot_typereport)*100)/(count_malw_ana_sh_total+count_malw_ana_iot_total))))+" % DE OBJETOS EL TIPO DE OBJETO ES REPORTE  \n")
print("      -    EN EL  "+str(float((((count_malw_ana_sh_typeindicator+count_malw_ana_iot_typeindicator)*100)/(count_malw_ana_sh_total+count_malw_ana_iot_total))))+" % DE OBJETOS EL TIPO DE OBJETO ES INDICADOR  \n")
print("      -    EN EL  "+str(float((((count_malw_ana_sh_typemarkingdefinition+count_malw_ana_iot_typemarkingdefinition)*100)/(count_malw_ana_sh_total+count_malw_ana_iot_total))))+" % DE OBJETOS EL TIPO DE OBJETO ES DEFINICION DE MARCADO:  \n")
print("\n")
print("\n")
print(" DE UN TOTAL DE "+str(count_malw_ana_sh_refs+count_malw_ana_iot_refs)+" OBJETOS DE REFERENCIA DE OBJETOS :\n") 
print("\n")
print("   - LOS PORCENTAJES DE TIPO DE OBJETO DE REFERENCIA SON LOS SIGUIENTES:  \n")
print("      -    EN  EL "+str(float((((count_malw_ana_sh_refindicator+count_malw_ana_iot_refindicator)*100)/(count_malw_ana_sh_refs+count_malw_ana_iot_refs))))+" % DE OBJETOS DE REFERENCIA EL TIPO DE OBJETOS DE REFERENCIA ES INDICADOR \n")
print("      -    EN  EL "+str(float((((count_malw_ana_sh_refmarkingdefinition+count_malw_ana_iot_refmarkingdefinition)*100)/(count_malw_ana_sh_refs+count_malw_ana_iot_refs))))+" % DE OBJETOS DE REFERENCIA EL TIPO DE OBJETOS DE REFERENCIA ES DEFINICION DE MARCADO  \n")
print("                -    EN  EL "+str(float((((count_malw_ana_sh_typereport_refindicator+count_malw_ana_sh_typereport_refmarkingdefinition+count_malw_ana_iot_typereport_refindicator+count_malw_ana_iot_typereport_refmarkingdefinition)*100)/(count_malw_ana_sh_refs+count_malw_ana_iot_refs))))+" % DE OBJETOS DE REFERENCIA DONDE EL TIPO DE OBJETO ES REPORTE, LOS PORCENTAJES DE TIPO DE OBJETO DE REFERENCIA SON LOS SIGUIENTES:  \n")
print("                           -    EN  EL "+str(float((((count_malw_ana_sh_typereport_refindicator+count_malw_ana_iot_typereport_refindicator)*100)/(count_malw_ana_sh_typereport_refindicator+count_malw_ana_sh_typereport_refmarkingdefinition+count_malw_ana_iot_typereport_refindicator+count_malw_ana_iot_typereport_refmarkingdefinition))))+" % DE OBJETOS DE REFERENCIA EL TIPO DE OBJETO DE REFERENCIA ES INDICADOR  \n")
print("                           -    EN  EL "+str(float((((count_malw_ana_sh_typereport_refmarkingdefinition+count_malw_ana_iot_typereport_refmarkingdefinition)*100)/(count_malw_ana_sh_typereport_refindicator+count_malw_ana_sh_typereport_refmarkingdefinition+count_malw_ana_iot_typereport_refindicator+count_malw_ana_iot_typereport_refmarkingdefinition))))+" % DE OBJETOS DE REFERENCIA EL TIPO DE OBJETO DE REFERENCIA ES DEFINICION DE MARCADO \n")
print("\n")
if((count_malw_ana_sh_typeindicator_refindicator+count_malw_ana_sh_typeindicator_refmarkingdefinition+count_malw_ana_iot_typeindicator_refindicator+count_malw_ana_iot_typeindicator_refmarkingdefinition)>0):
    print("                -    EN  EL "+str(float((((count_malw_ana_sh_typeindicator_refindicator+count_malw_ana_sh_typeindicator_refmarkingdefinition+count_malw_ana_iot_typeindicator_refindicator+count_malw_ana_iot_typeindicator_refmarkingdefinition)*100)/(count_malw_ana_sh_refs+count_malw_ana_iot_refs))))+" % DE OBJETOS DE REFERENCIA DONDE EL TIPO DE OBJETO ES REPORTE, LOS PORCENTAJES DE TIPO DE OBJETO DE REFERENCIA SON LOS SIGUIENTES:  \n")
    print("                           -    EN  EL "+str(float((((count_malw_ana_sh_typeindicator_refindicator+count_malw_ana_iot_typeindicator_refindicator)*100)/(count_malw_ana_sh_typeindicator_refindicator+count_malw_ana_sh_typeindicator_refmarkingdefinition+count_malw_ana_iot_typeindicator_refindicator+count_malw_ana_iot_typeindicator_refmarkingdefinition))))+" % DE OBJETOS DE REFERENCIA EL TIPO DE OBJETO DE REFERENCIA ES INDICADOR  \n")
    print("                           -    EN  EL "+str(float((((count_malw_ana_sh_typeindicator_refmarkingdefinition+count_malw_ana_iot_typeindicator_refmarkingdefinition)*100)/(count_malw_ana_sh_typeindicator_refindicator+count_malw_ana_sh_typeindicator_refmarkingdefinition+count_malw_ana_iot_typeindicator_refindicator+count_malw_ana_iot_typeindicator_refmarkingdefinition))))+" % DE OBJETOS DE REFERENCIA EL TIPO DE OBJETO DE REFERENCIA ES DEFINICION DE MARCADO \n")
    print("\n")
if((count_malw_ana_sh_typemarkingdefinition_refindicator+count_malw_ana_sh_typemarkingdefinition_refmarkingdefinition+count_malw_ana_iot_typemarkingdefinition_refindicator+count_malw_ana_iot_typemarkingdefinition_refmarkingdefinition)>0):
    print("                -    EN  EL "+str(float((((count_malw_ana_sh_typemarkingdefinition_refindicator+count_malw_ana_sh_typemarkingdefinition_refmarkingdefinition+count_malw_ana_iot_typemarkingdefinition_refindicator+count_malw_ana_iot_typemarkingdefinition_refmarkingdefinition)*100)/(count_malw_ana_sh_refs+count_malw_ana_iot_refs))))+" % DE OBJETOS DE REFERENCIA DONDE EL TIPO DE OBJETO ES REPORTE, LOS PORCENTAJES DE TIPO DE OBJETO DE REFERENCIA SON LOS SIGUIENTES:  \n")
    print("                           -    EN  EL "+str(float((((count_malw_ana_sh_typemarkingdefinition_refindicator+count_malw_ana_iot_typemarkingdefinition_refindicator)*100)/(count_malw_ana_sh_typemarkingdefinition_refindicator+count_malw_ana_sh_typemarkingdefinition_refmarkingdefinition+count_malw_ana_iot_typemarkingdefinition_refindicator+count_malw_ana_iot_typemarkingdefinition_refmarkingdefinition))))+" % DE OBJETOS DE REFERENCIA EL TIPO DE OBJETO DE REFERENCIA ES INDICADOR  \n")
    print("                           -    EN  EL "+str(float((((count_malw_ana_sh_typemarkingdefinition_refmarkingdefinition+count_malw_ana_iot_typemarkingdefinition_refmarkingdefinition)*100)/(count_malw_ana_sh_typemarkingdefinition_refindicator+count_malw_ana_sh_typemarkingdefinition_refmarkingdefinition+count_malw_ana_iot_typemarkingdefinition_refindicator+count_malw_ana_iot_typemarkingdefinition_refmarkingdefinition))))+" % DE OBJETOS DE REFERENCIA EL TIPO DE OBJETO DE REFERENCIA ES DEFINICION DE MARCADO \n")
    print("\n")



	
	