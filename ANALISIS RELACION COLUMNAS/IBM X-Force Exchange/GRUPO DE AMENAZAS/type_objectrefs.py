	
	
	


import pandas as pd
from datetime import datetime

#Abro los ficheros con los que voy a tratar


df_thgroup= pd.read_excel('ibm_grupo_amenazas_v2.xlsx')

#Variable para almacenar contador total de OBJETOS DE REFERENCIA
count_thgroup_refs=0
#Variable para almacenar contador total de vulnerabilidades
count_thgroup_total=0

#Variables para almacenar cantidad total de vulnerabilidades de un tipo
count_thgroup_typereport=0
#Variables para almacenar cantidad de OBJETOS DE REFERENCIA de un determinado valor, teniendo especificado previamente un tipo
count_thgroup_typereport_refindicator=0
count_thgroup_typereport_refmarkingdefinition=0

count_thgroup_typeindicator=0
count_thgroup_typeindicator_refindicator=0
count_thgroup_typeindicator_refmarkingdefinition=0

count_thgroup_typemarkingdefinition=0
count_thgroup_typemarkingdefinition_refindicator=0
count_thgroup_typemarkingdefinition_refmarkingdefinition=0

#Contador de total de tipos de OBJETOS DE REFERENCIA
count_thgroup_refindicator=0
count_thgroup_refmarkingdefinition=0

#Comprobamos el tipo de entrada
for r in range(0,len(df_thgroup["type"])):
    #Comprobamos si hay distintos valores de tipo en una misma fila
    if('[' in df_thgroup["type"][r]):
        aux=df_thgroup["type"][r].split(",")
        #Recorro los distintos valores de tipo
        for l in range(0,len(aux)):
            if(len(aux)>0):
                #Obtengo las distintas OBJETOS DE REFERENCIA de la fila actual
                auxx=df_thgroup["object_refs"][r].split("]")
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
                    count_thgroup_total+=1
                    if(aux_str == 'report'):
                        count_thgroup_typereport+=1
                        
                        aux4=aux3[l+1].replace("'","").replace("'","")
                        if(aux4!='NONE'):
                            #Si el valor de OBJETOS DE REFERENCIA para el tipo actual tiene varios valores
                            if("," in aux3[l+1]):
                                aux_array=aux3[l+1].split(",")
                                #Obtengo los distintos valores de OBJETOS DE REFERENCIA para un mismo tipo en la fila actual y los recorro
                                for k in range(0,len(aux_array)):
                                    if(len(aux_array)>0):
                                        if('indicator' in aux_array[k]):
                                            count_thgroup_refs+=1
                                            count_thgroup_refindicator+=1
                                            count_thgroup_typereport_refindicator+=1
                                        elif('marking-definition' in aux_array[k]):
                                            count_thgroup_refs+=1
                                            count_thgroup_refmarkingdefinition+=1
                                            count_thgroup_typereport_refmarkingdefinition+=1
                            else:
                                #Si existe un unico valor de referencia para el valor de tipo actual de la fila en la que estamos
                                if('indicator' in aux4):
                                    count_thgroup_refs+=1
                                    count_thgroup_refindicator+=1
                                    count_thgroup_typereport_refindicator+=1
                                elif('marking-definition' in aux4):
                                    count_thgroup_refs+=1
                                    count_thgroup_refmarkingdefinition+=1
                                    count_thgroup_typereport_refmarkingdefinition+=1
        
                    elif(aux_str == 'indicator'):
                        count_thgroup_typeindicator+=1
                        aux44=aux3[l+1].replace("'","").replace("'","")
                        if(aux44!='NONE'):
                            if("," in aux3[l+1]):
                                auxx_array=aux3[l+1].split(",")
                                for p in range(0,len(auxx_array)):
                                    if(len(auxx_array)>0):
                                        if('indicator' in auxx_array[p]):
                                            count_thgroup_refs+=1
                                            count_thgroup_refindicator+=1
                                            count_thgroup_typeindicator_refindicator+=1
                                        elif('marking-definition' in auxx_array[p]):
                                            count_thgroup_refs+=1
                                            count_thgroup_refmarkingdefinition+=1
                                            count_thgroup_typeindicator_refmarkingdefinition+=1
                            else:
                                if('indicator' in aux44):
                                    count_thgroup_refs+=1
                                    count_thgroup_refindicator+=1
                                    count_thgroup_typeindicator_refindicator+=1
                                elif('marking-definition' in aux44):
                                    count_thgroup_refs+=1
                                    count_thgroup_refmarkingdefinition+=1
                                    count_thgroup_typeindicator_refmarkingdefinition+=1                
                                
                    elif(aux_str == 'marking-definition'):
                        count_thgroup_typemarkingdefinition+=1
                        aux444=aux3[l+1].replace("'","").replace("'","")
                        if(aux444!='NONE'):
                            if("," in aux3[l+1]):
                                auxxx_array=aux3[l+1].split(",")
                                for c in range(0,len(auxxx_array)):
                                    if(len(auxxx_array)>0):
                                        if('indicator' in auxxx_array[c]):
                                            count_thgroup_refs+=1
                                            count_thgroup_refindicator+=1
                                            count_thgroup_typemarkingdefinition_refindicator+=1
                                        elif('marking-definition' in auxxx_array[c]):
                                            count_thgroup_refs+=1
                                            count_thgroup_refmarkingdefinition+=1
                                            count_thgroup_typemarkingdefinition_refmarkingdefinition+=1 
                            else:
                                if('indicator' in aux444):
                                    count_thgroup_refs+=1
                                    count_thgroup_refindicator+=1
                                    count_thgroup_typemarkingdefinition_refindicator+=1
                                elif('marking-definition' in aux444):
                                    count_thgroup_refs+=1
                                    count_thgroup_refmarkingdefinition+=1
                                    count_thgroup_typemarkingdefinition_refmarkingdefinition+=1                 
                                            
    else:
        #Si existe un unico valor de tipo para la fila actual
        if(df_thgroup["type"][r] == 'report'):
            count_thgroup_total+=1
            count_thgroup_typereport+=1  
            #Obtenemos las OBJETOS DE REFERENCIA para el valor actual de tipo
            refs_typereport_=df_thgroup["object_refs"][r].split(",")
            if(len(refs_typereport_)>0):
                for b in range(0,len(refs_typereport_)):
                    ref_typereport_=refs_typereport_[b].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
                    if(ref_typereport_!='NONE'):
                        if('indicator' in ref_typereport_):
                            count_thgroup_refs+=1
                            count_thgroup_refindicator+=1
                            count_thgroup_typereport_refindicator+=1
                        elif('marking-definition' in ref_typereport_):
                            count_thgroup_refs+=1
                            count_thgroup_refmarkingdefinition+=1
                            count_thgroup_typereport_refmarkingdefinition+=1
        
        elif(df_thgroup["type"][r] == 'indicator'):
            count_thgroup_total+=1
            count_thgroup_typeindicator+=1  
            refs_typeindicator_=df_thgroup["object_refs"][r].split(",")
            if(len(refs_typeindicator_)>0):
                for b in range(0,len(refs_typeindicator_)):
                    ref_typeindicator_=refs_typeindicator_[b].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
                    if(ref_typeindicator_!='NONE'):
                        if('indicator' in ref_typeindicator_):
                            count_thgroup_refs+=1
                            count_thgroup_refindicator+=1
                            count_thgroup_typeindicator_refindicator+=1
                        elif('marking-definition' in ref_typeindicator_):
                            count_thgroup_refs+=1
                            count_thgroup_refmarkingdefinition+=1
                            count_thgroup_typeindicator_refmarkingdefinition+=1
                            
        elif(df_thgroup["type"][r] == 'marking-definition'):
            count_thgroup_total+=1
            count_thgroup_typemarkingdefinition+=1  
            refs_typemarkingdefinition_=df_thgroup["object_refs"][r].split(",")
            if(len(refs_typemarkingdefinition_)>0):
                for b in range(0,len(refs_typemarkingdefinition_)):
                    ref_typemarkingdefinition_=refs_typemarkingdefinition_[b].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
                    if(ref_typemarkingdefinition_!='NONE'):
                        if('indicator' in ref_typemarkingdefinition_):
                            count_thgroup_refs+=1
                            count_thgroup_refindicator+=1
                            count_thgroup_typemarkingdefinition_refindicator+=1
                        elif('marking-definition' in ref_typemarkingdefinition_):
                            count_thgroup_refs+=1
                            count_thgroup_refmarkingdefinition+=1
                            count_thgroup_typemarkingdefinition_refmarkingdefinition+=1   
       
                    

        
        
print("*************************************ESTADÍSTICAS TIPO DE OBJETO/TIPO DE OBJETOS DE REFERENCIA GRUPO DE AMENAZAS*************************************")
print("\n")                            
                
print("\n")
print(" DE UN TOTAL DE "+str(count_thgroup_total)+" OBJETOS :\n") 
print("\n")
print("   - LAS ESTADISTICAS DE TIPO DE OBJETO SON LAS SIGUIENTES:  \n")
print("      -    EN  "+str(count_thgroup_typereport)+" OBJETOS EL TIPO DE OBJETO ES REPORTE  \n")
print("      -    EN  "+str(count_thgroup_typeindicator)+" OBJETOS EL TIPO DE OBJETO ES INDICADOR  \n")
print("      -    EN  "+str(count_thgroup_typemarkingdefinition)+" OBJETOS EL TIPO DE OBJETO ES DEFINICION DE MARCADO  \n")
print("\n")
print(" DE UN TOTAL DE "+str(count_thgroup_refs)+" OBJETOS DE REFERENCIA DE OBJETOS :\n") 
print("\n")
print("   - LAS ESTADISTICAS DE TIPO DE OBJETO DE REFERENCIA SON LAS SIGUIENTES:  \n")
print("      -    EN  "+str(count_thgroup_refindicator)+" OBJETOS DE REFERENCIA EL TIPO DE OBJETO DE REFERENCIA DE OBJETO ES INDICADOR \n")
print("      -    EN  "+str(count_thgroup_refmarkingdefinition)+" OBJETOS DE REFERENCIA EL TIPO DE OBJETO DE REFERENCIA DE OBJETO ES DEFINICION DE MARCADO  \n")
print("                -    EN  "+str(count_thgroup_typereport_refindicator+count_thgroup_typereport_refmarkingdefinition)+" OBJETOS DE REFERENCIA DONDE EL TIPO DE OBJETO ES REPORTE, LAS ESTADÍSTICAS DE TIPO DE OBJETO DE REFERENCIA SON LAS SIGUIENTES:  \n")
print("                           -    EN  "+str(count_thgroup_typereport_refindicator)+" OBJETOS DE REFERENCIA EL TIPO DE OBJETO DE REFERENCIA ES INDICADOR  \n")
print("                           -    EN  "+str(count_thgroup_typereport_refmarkingdefinition)+" OBJETOS DE REFERENCIA EL TIPO DE OBJETO DE REFERENCIA ES MARKING-DEFINITION \n")
print("\n")
print("                -    EN  "+str(count_thgroup_typeindicator_refindicator+count_thgroup_typeindicator_refmarkingdefinition)+" OBJETOS DE REFERENCIA DONDE EL TIPO DE OBJETO ES INDICADOR, LAS ESTADÍSTICAS DE TIPO DE OBJETO DE REFERENCIA SON LAS SIGUIENTES:  \n")
print("                           -    EN  "+str(count_thgroup_typeindicator_refindicator)+" OBJETOS DE REFERENCIA EL TIPO DE OBJETO DE REFERENCIA ES INDICADOR  \n")
print("                           -    EN  "+str(count_thgroup_typeindicator_refmarkingdefinition)+" OBJETOS DE REFERENCIA EL TIPO DE OBJETO DE REFERENCIA ES MARKING-DEFINITION \n")
print("\n") 
print("                -    EN  "+str(count_thgroup_typemarkingdefinition_refindicator+count_thgroup_typemarkingdefinition_refmarkingdefinition)+" OBJETOS DE REFERENCIA DONDE EL TIPO DE OBJETO ES DEFINICION DE MARCADO, LAS ESTADÍSTICAS DE TIPO DE OBJETO DE REFERENCIA SON LAS SIGUIENTES:  \n")
print("                           -    EN  "+str(count_thgroup_typemarkingdefinition_refindicator)+" OBJETOS DE REFERENCIA EL TIPO DE OBJETO DE REFERENCIA ES INDICADOR  \n")
print("                           -    EN  "+str(count_thgroup_typemarkingdefinition_refmarkingdefinition)+" OBJETOS DE REFERENCIA EL TIPO DE OBJETO DE REFERENCIA ES MARKING-DEFINITION \n")











print("*************************************PORCENTAJE TIPO DE OBJETO/TIPO DE OBJETOS DE REFERENCIA GRUPO DE AMENAZAS*************************************")
print("\n")                            
                
print("\n")
print(" DE UN TOTAL DE "+str(count_thgroup_total)+" OBJETOS :\n") 
print("\n")
print("   - LOS PORCENTAJES DE TIPO DE OBJETO  SON LOS SIGUIENTES:  \n")
print("      -    EN EL  "+str(float(((count_thgroup_typereport*100)/count_thgroup_total)))+" % DE OBJETOS EL TIPO DE OBJETO ES REPORTE  \n")
print("      -    EN EL  "+str(float(((count_thgroup_typeindicator*100)/count_thgroup_total)))+" % DE OBJETOS EL TIPO DE OBJETO ES INDICADOR  \n")
print("      -    EN EL  "+str(float(((count_thgroup_typemarkingdefinition*100)/count_thgroup_total)))+" % DE OBJETOS EL TIPO DE OBJETO ES DEFINICION DE MARCADO  \n")
print("\n")
print("\n")
print(" DE UN TOTAL DE "+str(count_thgroup_refs)+" OBJETOS DE REFERENCIA DE OBJETOS :\n") 
print("\n")
print("   - LOR PORCENTAJES DE TIPO DE OBJETO DE REFERENCIA SON LOS SIGUIENTES:  \n")
print("      -    EN  EL "+str(float(((count_thgroup_refindicator*100)/count_thgroup_refs)))+" % DE OBJETOS DE REFERENCIA EL TIPO DE OBJETO DE REFERENCIA DE OBJETO ES INDICADOR \n")
print("      -    EN  EL "+str(float(((count_thgroup_refmarkingdefinition*100)/count_thgroup_refs)))+" % DE OBJETOS DE REFERENCIA EL TIPO DE OBJETO DE REFERENCIA DE OBJETO ES DEFINICION DE MARCADO  \n")
print("                -    EN  EL "+str(float((((count_thgroup_typereport_refindicator+count_thgroup_typereport_refmarkingdefinition)*100)/count_thgroup_refs)))+" % DE OBJETOS DE REFERENCIA DONDE EL TIPO DE OBJETO ES REPORTE, LOS PORCENTAJES DE TIPO DE OBJETO DE REFERENCIA SON LOS SIGUIENTES:  \n")
print("                           -    EN  EL "+str(float(((count_thgroup_typereport_refindicator*100)/(count_thgroup_typereport_refindicator+count_thgroup_typereport_refmarkingdefinition))))+" % DE OBJETOS DE REFERENCIA EL TIPO DE OBJETO DE REFERENCIA ES INDICADOR  \n")
print("                           -    EN  EL "+str(float(((count_thgroup_typereport_refmarkingdefinition*100)/(count_thgroup_typereport_refindicator+count_thgroup_typereport_refmarkingdefinition))))+" % DE OBJETOS DE REFERENCIA EL TIPO DE OBJETO DE REFERENCIA ES MARKING-DEFINITION \n")
print("\n")
if((count_thgroup_typeindicator_refindicator+count_thgroup_typeindicator_refmarkingdefinition)>0):
    print("                -    EN  EL "+str(float((((count_thgroup_typeindicator_refindicator+count_thgroup_typeindicator_refmarkingdefinition)*100)/count_thgroup_refs)))+" % DE OBJETOS DE REFERENCIA DONDE EL TIPO DE OBJETO ES INDICADOR, LOS PORCENTAJES DE TIPO DE OBJETO DE REFERENCIA SON LOS SIGUIENTES:  \n")
    print("                           -    EN  EL "+str(float(((count_thgroup_typeindicator_refindicator*100)/(count_thgroup_typeindicator_refindicator+count_thgroup_typeindicator_refmarkingdefinition))))+" % DE OBJETOS DE REFERENCIA EL TIPO DE OBJETO DE REFERENCIA ES INDICADOR  \n")
    print("                           -    EN  EL "+str(float(((count_thgroup_typeindicator_refmarkingdefinition*100)/(count_thgroup_typeindicator_refindicator+count_thgroup_typeindicator_refmarkingdefinition))))+" % DE OBJETOS DE REFERENCIA EL TIPO DE OBJETO DE REFERENCIA ES MARKING-DEFINITION \n")
    print("\n")
if((count_thgroup_typemarkingdefinition_refindicator+count_thgroup_typemarkingdefinition_refmarkingdefinition)>0):
    print("                -    EN  EL "+str(float((((count_thgroup_typemarkingdefinition_refindicator+count_thgroup_typemarkingdefinition_refmarkingdefinition)*100)/count_thgroup_refs)))+" % DE OBJETOS DE REFERENCIA DONDE EL TIPO DE OBJETO ES INDICADOR, LOS PORCENTAJES DE TIPO DE OBJETO DE REFERENCIA SON LOS SIGUIENTES:  \n")
    print("                           -    EN  EL "+str(float(((count_thgroup_typemarkingdefinition_refindicator*100)/(count_thgroup_typemarkingdefinition_refindicator+count_thgroup_typemarkingdefinition_refmarkingdefinition))))+" % DE OBJETOS DE REFERENCIA EL TIPO DE OBJETO DE REFERENCIA ES INDICADOR  \n")
    print("                           -    EN  EL "+str(float(((count_thgroup_typemarkingdefinition_refmarkingdefinition*100)/(count_thgroup_typemarkingdefinition_refindicator+count_thgroup_typemarkingdefinition_refmarkingdefinition))))+" % DE OBJETOS DE REFERENCIA EL TIPO DE OBJETO DE REFERENCIA ES MARKING-DEFINITION \n")
    print("\n")

	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	