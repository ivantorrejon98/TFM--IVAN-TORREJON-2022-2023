

import pandas as pd
from datetime import datetime

#Abro los ficheros con los que voy a tratar


df_thgroup_ = pd.read_excel('ibm_grupo_amenazas_v2.xlsx')

#Contador de total de valores DE NOMBRE DE OBJETO
count_thgroup_refs=0
#Contador total de valores de tipo distintos
count_thgroup_total=0

#Contador total de valores concretos de un tipo de OBJETO
count_thgroup_typereport=0
#Contador de distintos valores DE NOMBRE DE OBJETO dado un valor concreto de tipo de OBJETO
count_thgroup_typereport_nameprofile=0
count_thgroup_typereport_namereport=0

count_thgroup_typeindicator=0
count_thgroup_typeindicator_nameprofile=0
count_thgroup_typeindicator_namereport=0

count_thgroup_typemarkingdefinition=0
count_thgroup_typemarkingdefinition_nameprofile=0
count_thgroup_typemarkingdefinition_namereport=0

count_thgroup_nameprofile=0
count_thgroup_namereport=0

#Comprobamos el tipo de OBJETO 
for r in range(0,len(df_thgroup_["type"])):
    #Si la fila actual contiene más de un valor para el tipo de OBJETO
    if('[' in df_thgroup_["type"][r]):
        #Obtengo los valores de la columna tipo
        aux=df_thgroup_["type"][r].split(",")
        #Recorro los valores de la columna tipo para la fila actual
        for l in range(0,len(aux)):
            if(len(aux)>0):
                #Obtengo los valores de nombre para la fila actual
                auxx=df_thgroup_["name"][r].split("]")
                straux=""
                for t in range(0,len(auxx)):
                    if(auxx[t]!=""):
                        aux2=auxx[t].replace(', [', '').replace(']', '').replace(" ",'').replace('[','')
                        straux+="/"+aux2
                #Obtengo los distintos valores DE NOMBRE DE OBJETO para la fila actual
                aux3=straux.split("/")
                #Obtengo el valor actual de la columna tipo en la fila en la que nos encontramos
                aux_str=aux[l].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
                if(aux_str!='NONE'):
                    count_thgroup_total+=1
                    #Comprobamos el tipo de OBJETO en la fila actual
                    if(aux_str == 'report'):
                        count_thgroup_typereport+=1
                        #Obtenemos el valor de nombre que corresponde con el valor de tipo en la columna actual
                        aux4=aux3[l+1].replace("'","").replace("'","")
                        if(aux4!='NONE'):
                            #Si existen varios valores DE NOMBRE DE OBJETO para un mismo tipo
                            if("," in aux3[l+1]):
                                aux_array=aux3[l+1].split(",")
                                #Recorro los distintos valores DE NOMBRE DE OBJETO para un mismo tipo
                                for k in range(0,len(aux_array)):
                                    if(len(aux_array)>0):
                                        #Compruebo el valor de nombre actual y aumento contador
                                        if('Profile' in aux_array[k]):
                                            count_thgroup_refs+=1
                                            count_thgroup_nameprofile+=1
                                            count_thgroup_typereport_nameprofile+=1
                                        elif('Report' in aux_array[k]):
                                            count_thgroup_refs+=1
                                            count_thgroup_namereport+=1
                                            count_thgroup_typereport_namereport+=1
                            else:
                                #Si existe un unico valor de nombre para el valor de tipo actual en la columna en la que nos encontramos
                                if('Profile' in aux4):
                                    count_thgroup_refs+=1
                                    count_thgroup_nameprofile+=1
                                    count_thgroup_typereport_nameprofile+=1
                                elif('Report' in aux4):
                                    count_thgroup_refs+=1
                                    count_thgroup_namereport+=1
                                    count_thgroup_typereport_namereport+=1
        
                    elif(aux_str == 'indicator'):
                        count_thgroup_typeindicator+=1
                        aux44=aux3[l+1].replace("'","").replace("'","")
                        if(aux44!='NONE'):
                            if("," in aux3[l+1]):
                                auxx_array=aux3[l+1].split(",")
                                for p in range(0,len(auxx_array)):
                                    if(len(auxx_array)>0):
                                        if('Profile' in auxx_array[p]):
                                            count_thgroup_refs+=1
                                            count_thgroup_nameprofile+=1
                                            count_thgroup_typeindicator_nameprofile+=1
                                        elif('Report' in auxx_array[p]):
                                            count_thgroup_refs+=1
                                            count_thgroup_namereport+=1
                                            count_thgroup_typeindicator_namereport+=1
                            else:
                                if('Profile' in aux44):
                                    count_thgroup_refs+=1
                                    count_thgroup_nameprofile+=1
                                    count_thgroup_typeindicator_nameprofile+=1
                                elif('Report' in aux44):
                                    count_thgroup_refs+=1
                                    count_thgroup_namereport+=1
                                    count_thgroup_typeindicator_namereport+=1                
                                
                    elif(aux_str == 'marking-definition'):
                        count_thgroup_typemarkingdefinition+=1
                        aux444=aux3[l+1].replace("'","").replace("'","")
                        if(aux444!='NONE'):
                            if("," in aux3[l+1]):
                                auxxx_array=aux3[l+1].split(",")
                                for c in range(0,len(auxxx_array)):
                                    if(len(auxxx_array)>0):
                                        if('Profile' in auxxx_array[c]):
                                            count_thgroup_refs+=1
                                            count_thgroup_nameprofile+=1
                                            count_thgroup_typemarkingdefinition_nameprofile+=1
                                        elif('Report' in auxxx_array[c]):
                                            count_thgroup_refs+=1
                                            count_thgroup_namereport+=1
                                            count_thgroup_typemarkingdefinition_namereport+=1 
                            else:
                                if('Profile' in aux444):
                                    count_thgroup_refs+=1
                                    count_thgroup_nameprofile+=1
                                    count_thgroup_typemarkingdefinition_nameprofile+=1
                                elif('Report' in aux444):
                                    count_thgroup_refs+=1
                                    count_thgroup_namereport+=1
                                    count_thgroup_typemarkingdefinition_namereport+=1                 
                                            
    else:
        #Si existe unicamente un valor de tipo para la fila actual
        if(df_thgroup_["type"][r] == 'report'):
            count_thgroup_total+=1
            count_thgroup_typereport+=1  
            refs_typereport_=df_thgroup_["name"][r].split(",")
            #Obtengo los valores de nombre para el valor de tipo actual en la fila en la que nos encontrmaos
            if(len(refs_typereport_)>0):
                for b in range(0,len(refs_typereport_)):
                    ref_typereport_=refs_typereport_[b].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
                    if(ref_typereport_!='NONE'):
                        #Compruebo el valor de nombre actual
                        if('Profile' in ref_typereport_):
                            count_thgroup_refs+=1
                            count_thgroup_nameprofile+=1
                            count_thgroup_typereport_nameprofile+=1
                        elif('Report' in ref_typereport_):
                            count_thgroup_refs+=1
                            count_thgroup_namereport+=1
                            count_thgroup_typereport_namereport+=1
        
        elif(df_thgroup_["type"][r] == 'indicator'):
            count_thgroup_total+=1
            count_thgroup_typeindicator+=1  
            refs_typeindicator_=df_thgroup_["name"][r].split(",")
            if(len(refs_typeindicator_)>0):
                for b in range(0,len(refs_typeindicator_)):
                    ref_typeindicator_=refs_typeindicator_[b].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
                    if(ref_typeindicator_!='NONE'):
                        if('Profile' in ref_typeindicator_):
                            count_thgroup_refs+=1
                            count_thgroup_nameprofile+=1
                            count_thgroup_typeindicator_nameprofile+=1
                        elif('Report' in ref_typeindicator_):
                            count_thgroup_refs+=1
                            count_thgroup_namereport+=1
                            count_thgroup_typeindicator_namereport+=1
                            
        elif(df_thgroup_["type"][r] == 'marking-definition'):
            count_thgroup_total+=1
            count_thgroup_typemarkingdefinition+=1  
            refs_typemarkingdefinition_=df_thgroup_["name"][r].split(",")
            if(len(refs_typemarkingdefinition_)>0):
                for b in range(0,len(refs_typemarkingdefinition_)):
                    ref_typemarkingdefinition_=refs_typemarkingdefinition_[b].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
                    if(ref_typemarkingdefinition_!='NONE'):
                        if('Profile' in ref_typemarkingdefinition_):
                            count_thgroup_refs+=1
                            count_thgroup_nameprofile+=1
                            count_thgroup_typemarkingdefinition_nameprofile+=1
                        elif('Report' in ref_typemarkingdefinition_):
                            count_thgroup_refs+=1
                            count_thgroup_namereport+=1
                            count_thgroup_typemarkingdefinition_namereport+=1   
       
                    

        
        
print("*************ESTADÍSTICAS TIPO DE OBJETO/NOMBRE DE OBJETO PERFIL GRUPO DE AMENAZAS*************")
print("\n")                            
                
print("\n")
print(" DE UN TOTAL DE "+str(count_thgroup_total)+" OBJETOS :\n") 
print("\n")
print("   - LAS ESTADISTICAS DE TIPO DE OBJETO SON LAS SIGUIENTES:  \n")
print("      -    EN  "+str(count_thgroup_typereport)+" OBJETOS EL TIPO DE OBJETO ES REPORTE  \n")
print("      -    EN  "+str(count_thgroup_typeindicator)+" OBJETOS EL TIPO DE OBJETO ES INDICADOR  \n")
print("      -    EN  "+str(count_thgroup_typemarkingdefinition)+" OBJETOS EL TIPO DE OBJETO ES DEFINICION DE MARCADO  \n")
print("\n")
print(" DE UN TOTAL DE "+str(count_thgroup_refs)+" VALORES DE NOMBRE DE OBJETO :\n") 
print("\n")
print("   - LAS ESTADISTICAS DE PALABRA INCLUIDA EN EL NOMBRE SON LAS SIGUIENTES:  \n")
print("      -    EN  "+str(count_thgroup_nameprofile)+" REFERENCIAS EL NOMBRE INCLUYE LA PALABRA PROFILE \n")
print("      -    EN  "+str(count_thgroup_namereport)+" REFERENCIAS EL NOMBRE INCLUYE LA PALABRA REPORT \n")
print("                -    EN  "+str(count_thgroup_typereport_nameprofile+count_thgroup_typereport_namereport)+" REFERENCIAS DONDE EL TIPO DE OBJETO ES REPORTE, LAS ESTADÍSTICAS DE PALABRA INCLUIDA EN EL NOMBRE SON LAS SIGUIENTES:  \n")
print("                           -    EN  "+str(count_thgroup_typereport_nameprofile)+" REFERENCIAS EL NOMBRE INCLUYE LA PALABRA PROFILE  \n")
print("                           -    EN  "+str(count_thgroup_typereport_namereport)+" REFERENCIAS EL NOMBRE INCLUYE LA PALABRA REPORT \n")
print("\n")
print("                -    EN  "+str(count_thgroup_typeindicator_nameprofile+count_thgroup_typeindicator_namereport)+" REFERENCIAS DONDE EL TIPO DE OBJETO ES INDICADOR, LAS ESTADÍSTICAS DE PALABRA INCLUIDA EN EL NOMBRE SON LAS SIGUIENTES:  \n")
print("                           -    EN  "+str(count_thgroup_typeindicator_nameprofile)+" REFERENCIAS EL NOMBRE INCLUYE LA PALABRA PROFILE  \n")
print("                           -    EN  "+str(count_thgroup_typeindicator_namereport)+" REFERENCIAS EL NOMBRE INCLUYE LA PALABRA REPORT \n")
print("\n") 
print("                -    EN  "+str(count_thgroup_typemarkingdefinition_nameprofile+count_thgroup_typemarkingdefinition_namereport)+" REFERENCIAS DONDE EL TIPO DE OBJETO ES DEFINICION DE MARCADO, LAS ESTADÍSTICAS DE PALABRA INCLUIDA EN EL NOMBRE SON LAS SIGUIENTES:  \n")
print("                           -    EN  "+str(count_thgroup_typemarkingdefinition_nameprofile)+" REFERENCIAS EL NOMBRE INCLUYE LA PALABRA PROFILE  \n")
print("                           -    EN  "+str(count_thgroup_typemarkingdefinition_namereport)+" REFERENCIAS EL NOMBRE INCLUYE LA PALABRA REPORT \n")











print("*************PORCENTAJE TIPO DE OBJETO/NOMBRE DE OBJETO PERFIL GRUPO DE AMENAZAS*************")
print("\n")                            
                
print("\n")
print(" DE UN TOTAL DE "+str(count_thgroup_total)+" OBJETOS :\n") 
print("\n")
print("   - LOS PORCENTAJES DE TIPO DE OBJETO  SON LOS SIGUIENTES:  \n")
print("      -    EN EL  "+str(float(((count_thgroup_typereport*100)/count_thgroup_total)))+" % DE OBJETOS EL TIPO DE OBJETO ES REPORTE  \n")
print("      -    EN EL  "+str(float(((count_thgroup_typeindicator*100)/count_thgroup_total)))+" % DE OBJETOS EL TIPO DE OBJETO ES INDICADOR  \n")
print("      -    EN EL  "+str(float(((count_thgroup_typemarkingdefinition*100)/count_thgroup_total)))+" % DE OBJETOS EL TIPO DE OBJETO ES DEFINICION DE MARCADO:  \n")
print("\n")
print("\n")
print(" DE UN TOTAL DE "+str(count_thgroup_refs)+" VALORES DE NOMBRE DE OBJETO :\n") 
print("\n")
print("   - LOR PORCENTAJES DE PALABRA INCLUIDA EN EL NOMBRE SON LOS SIGUIENTES:  \n")
print("      -    EN  EL "+str(float(((count_thgroup_nameprofile*100)/count_thgroup_refs)))+" % DE OBJETOS EL NOMBRE INCLUYE LA PALABRA PROFILE \n")
print("      -    EN  EL "+str(float(((count_thgroup_namereport*100)/count_thgroup_refs)))+" % DE OBJETOS EL NOMBRE INCLUYE LA PALABRA REPORT \n")
print("                -    EN  EL "+str(float((((count_thgroup_typereport_nameprofile+count_thgroup_typereport_namereport)*100)/count_thgroup_refs)))+" % DE OBJETOS DONDE EL TIPO DE OBJETO ES REPORTE, LOS PORCENTAJES DE PALABRA INCLUIDA EN EL NOMBRE SON LOS SIGUIENTES:  \n")
print("                           -    EN  EL "+str(float(((count_thgroup_typereport_nameprofile*100)/(count_thgroup_typereport_nameprofile+count_thgroup_typereport_namereport))))+" % DE OBJETOS EL NOMBRE INCLUYE LA PALABRA PROFILE  \n")
print("                           -    EN  EL "+str(float(((count_thgroup_typereport_namereport*100)/(count_thgroup_typereport_nameprofile+count_thgroup_typereport_namereport))))+" % DE OBJETOS EL NOMBRE INCLUYE LA PALABRA REPORT \n")
print("\n")
if((count_thgroup_typeindicator_nameprofile+count_thgroup_typeindicator_namereport)>0):
    print("                -    EN  EL "+str(float((((count_thgroup_typeindicator_nameprofile+count_thgroup_typeindicator_namereport)*100)/count_thgroup_refs)))+" % DE OBJETOS DONDE EL TIPO DE OBJETO ES INDICADOR, LOS PORCENTAJES DE PALABRA INCLUIDA EN EL NOMBRE SON LOS SIGUIENTES:  \n")
    print("                           -    EN  EL "+str(float(((count_thgroup_typeindicator_nameprofile*100)/(count_thgroup_typeindicator_nameprofile+count_thgroup_typeindicator_namereport))))+" % DE OBJETOS EL NOMBRE INCLUYE LA PALABRA PROFILE  \n")
    print("                           -    EN  EL "+str(float(((count_thgroup_typeindicator_namereport*100)/(count_thgroup_typeindicator_nameprofile+count_thgroup_typeindicator_namereport))))+" % DE OBJETOS EL NOMBRE INCLUYE LA PALABRA REPORT \n")
    print("\n")
if((count_thgroup_typemarkingdefinition_nameprofile+count_thgroup_typemarkingdefinition_namereport)>0):
    print("                -    EN  EL "+str(float((((count_thgroup_typemarkingdefinition_nameprofile+count_thgroup_typemarkingdefinition_namereport)*100)/count_thgroup_refs)))+" % DE OBJETOS DONDE EL TIPO DE OBJETO ES INDICADOR, LOS PORCENTAJES DE PALABRA INCLUIDA EN EL NOMBRE SON LOS SIGUIENTES:  \n")
    print("                           -    EN  EL "+str(float(((count_thgroup_typemarkingdefinition_nameprofile*100)/(count_thgroup_typemarkingdefinition_nameprofile+count_thgroup_typemarkingdefinition_namereport))))+" % DE OBJETOS EL NOMBRE INCLUYE LA PALABRA PROFILE  \n")
    print("                           -    EN  EL "+str(float(((count_thgroup_typemarkingdefinition_namereport*100)/(count_thgroup_typemarkingdefinition_nameprofile+count_thgroup_typemarkingdefinition_namereport))))+" % DE OBJETOS EL NOMBRE INCLUYE LA PALABRA REPORT \n")
    print("\n")

