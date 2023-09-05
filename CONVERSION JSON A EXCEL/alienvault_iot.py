

import pandas as pd
import json
import math
import os


#ARRAYS DONDE GUARDARE EL NOMBRE DE TODAS LAS COLUMNAS Y SU VALOR
final=0
columns=["created","created_by_ref","description","id","labels","modified","name","object_refs","published","spec_version","type","contact_information","identity_class","pattern","pattern_type","valid_from","pattern_version","aliases","valid_until"]
values=[None] * len(columns)



#ARRAY PARA GUARDAR LAS LABELS
labels=[]
#ARRAY PARA GUARDAR LAS LABELS CUANDO HAY VARIOS OBJETOS
labels_grande=[]

#ARRAY PARA GUARDAR LOS VALORES DE OBJECT_REFS
object_refs=[]
#ARRAY PARA GUARDAR LAS OBJECT_REFS CUANDO HAY VARIOS OBJECTS
object_refs_grande=[]

x_com_ibm_iris_tags=[]
x_com_ibm_iris_tags_grande=[]

#VALORES A INSERTAR
values_grande=[]

type_array=[]
names=[]
published=[]
x_com_ibm_short_description=[]
ids=[]
created=[]
modified=[]
definition_type=[]
valid_from=[]
pattern=[]
x_com_ibm_short_description=[]
x_com_ibm_html_content=[]
x_com_ibm_source_pdf=[]
x_com_ibm_source=[]
description=[]


def insertar_labels2(dataframe,columnas,filas):
    ##print("INSERTAR_LABELS2")
    ##print(dataframe)
    ##print(filas)
    ##print(columnas)
    ##print("************************")
    if(filas==1):
        if(len(dataframe[0][0])==0):
            index = columns.index("labels")
            if(values_aux[index]==None):
                values_aux.pop(index)
                values_aux.insert(index,"NONE")
        else:
            index = columns.index("labels")
            if(values_aux[index]==None):
                values_aux.pop(index)
                values_aux.insert(index,dataframe[0][0])
    elif(filas==0):
        index = columns.index("labels")
        if(values_aux[index]==None):
            values_aux.pop(index)
            values_aux.insert(index,"NONE")
    else:
        ##print("ELSEEEEEEEEEEEEEEEEE LABES2")
        array_aux=[]
        for r in range(0,filas):
            array_aux.append(dataframe[0][r])
        index = columns.index("labels")
        if(values_aux[index]==None):
            values_aux.pop(index)
            values_aux.insert(index,array_aux)
            
            
    ##print(len(dataframe[0][0]))
    

def insertar_objects_refs2(dataframe,columnas,filas):
    ##print("INSERTAR_OBJECTS REFS")
    ##print(dataframe)
    ##print(filas)
    ##print(columnas)
    ##print("************************")
    if(filas==1):
        if(len(dataframe[0][0])==0):
            index = columns.index("object_refs")
            if(values_aux[index]==None):
                values_aux.pop(index)
                values_aux.insert(index,"NONE")
        else:
            index = columns.index("object_refs")
            if(values_aux[index]==None):
                values_aux.pop(index)
                values_aux.insert(index,dataframe[0][0])
    else:
        if(filas>20):
            ##print("ELSEEEEEEEEEEEEEEEEE LABES2")
            array_aux=[]
            for r in range(0,20):
                array_aux.append(dataframe[0][r])
            index = columns.index("object_refs")
            if(values_aux[index]==None):
                values_aux.pop(index)
                values_aux.insert(index,array_aux)
        else:
            ##print("ELSEEEEEEEEEEEEEEEEE LABES2")
            array_aux=[]
            for r in range(0,filas):
                array_aux.append(dataframe[0][r])
            index = columns.index("object_refs")
            if(values_aux[index]==None):
                values_aux.pop(index)
                values_aux.insert(index,array_aux)

    
def insertar_iris_tags(dataframe,columnas,filas):
    ##print("INSERTAR_IRIS TAGS")
    ##print(dataframe)
    ##print(filas)
    ##print(columnas)
    ##print("************************")
    if(filas==1):
        if(len(dataframe[0][0])==0):
            index = columns.index("x_com_ibm_iris_tags")
            if(values_aux[index]==None):
                values_aux.pop(index)
                values_aux.insert(index,"NONE")
        else:
            index = columns.index("x_com_ibm_iris_tags")
            if(values_aux[index]==None):
                values_aux.pop(index)
                values_aux.insert(index,dataframe[0][0])
    else:
        ##print("ELSEEEEEEEEEEEEEEEEE IRIS TAGS")
        array_aux=[]
        for r in range(0,filas):
            array_aux.append(dataframe[0][r])
        index = columns.index("x_com_ibm_iris_tags")
        if(values_aux[index]==None):
            values_aux.pop(index)
            values_aux.insert(index,array_aux)
            
        
            
            
    ##print(len(dataframe[0][0]))
        

def insertar_labels(dataframe,columnas):
    ##print("INSERTAR_LABELS")
    ##print(dataframe)
    ##print("*")
    ##print(len(dataframe))
    if(len(dataframe)==1):
        index1 = columns.index("labels")
        if(values[index1]==None):
            values.pop(index1)
            values.insert(index1,dataframe[0])
    else:
        for g in range(0,len(dataframe)):
            if(g!=(len(dataframe)-1)):
                labels.append(dataframe[g])
            else:
                labels.append(dataframe[g])
                index7 = columns.index("labels")
                array_auxiliar_dos=[]
                for d in range(0,len(labels)):
                    elem_dos=labels.pop()
                    array_auxiliar_dos.insert(0,elem_dos)
                if(array_auxiliar_dos.count("null") == len(array_auxiliar_dos)):
                    if(values[index7]==None):
                        values.pop(index7)
                        values.insert(index7,"NONE") 
                else:
                    if(values[index7]==None):
                        values.pop(index7)
                        values.insert(index7,array_auxiliar_dos) 
        
    
def insertar_object_refs(dataframe,columnas):
    ##print("INSERTAR_LABELS")
    ##print(dataframe)
    ##print("*")
    ##print(len(dataframe))
    if(len(dataframe)==1):
        index1 = columns.index("object_refs")
        if(values[index1]==None):
            values.pop(index1)
            values.insert(index1,dataframe[0])
    else:
        if(len(dataframe)>20):
            for g in range(0,20):
                if(g!=19):
                    object_refs.append(dataframe[g])
                else:
                    object_refs.append(dataframe[g])
                    index7 = columns.index("object_refs")
                    array_auxiliar_dos=[]
                    for d in range(0,len(object_refs)):
                        elem_dos=object_refs.pop()
                        array_auxiliar_dos.insert(0,elem_dos)
                    if(array_auxiliar_dos.count("null") == len(array_auxiliar_dos)):
                        if(values[index7]==None):
                            values.pop(index7)
                            values.insert(index7,"NONE") 
                    else:
                        if(values[index7]==None):
                            values.pop(index7)
                            values.insert(index7,array_auxiliar_dos) 
        else:
            for g in range(0,len(dataframe)):
                if(g!=(len(dataframe)-1)):
                    object_refs.append(dataframe[g])
                else:
                    object_refs.append(dataframe[g])
                    index7 = columns.index("object_refs")
                    array_auxiliar_dos=[]
                    for d in range(0,len(object_refs)):
                        elem_dos=object_refs.pop()
                        array_auxiliar_dos.insert(0,elem_dos)
                    if(array_auxiliar_dos.count("null") == len(array_auxiliar_dos)):
                        if(values[index7]==None):
                            values.pop(index7)
                            values.insert(index7,"NONE") 
                    else:
                        if(values[index7]==None):
                            values.pop(index7)
                            values.insert(index7,array_auxiliar_dos)
                
def transpose(l1, l2):

    # iterate over list l1 to the length of an item
    for i in range(len(l1[0])):
        # #print(i)
        row =[]
        for item in l1:
            # appending to new list with values and index positions
            # i contains index position and item contains values
            row.append(item[i])
        l2.append(row)
    return l2      
                        
######################################################################################
###############################FUNCION RECURSIVA######################################
def recursiva(dataframe,nombre_columna,numero_dataframe):
    ##print("*******")
    ##print(acum)
    ##print(nombre_columna)
    ##print(dataframe)
    if nombre_columna is not str:
        nombre_completo=str(nombre_columna)+"."
    else:
        nombre_completo=nombre_columna+"."
    if isinstance(dataframe, list):
        #EL ELEMENTO ES LIST Y NO DICT
        e=[]
        for j in range(0,len(dataframe)):
            e.append(str(j))
        dataframe_list=dict(zip(e,dataframe))
        dataframe_dict=pd.DataFrame.from_dict(dataframe_list,orient="index")
        
    else:
        dataframe_dict=pd.DataFrame.from_dict(dataframe,orient="index")
    nombre_filas=dataframe_dict.index.values
    tamanio_dataframe=dataframe_dict.shape 
    
    filas=tamanio_dataframe[0]
    columnas=tamanio_dataframe[1]
    
    ##print("RECURSIVA")
    ##print(nombre_columna)
    ##print(dataframe)
    
    if("labels" in nombre_columna):
        insertar_labels(dataframe,columnas)
    elif("object_refs" in nombre_columna):
        insertar_object_refs(dataframe,columnas)
        
        
######################################################################################
###############################FUNCION RECURSIVA######################################
def recursiva2(dataframe,nombre_columna,numero_dataframe):
    ##print("RECURSIVA2")
    ##print(dataframe)
    ##print(nombre_columna)
    ##print(numero_dataframe)
    
    
    if nombre_columna is not str:
        nombre_completo=str(nombre_columna)+"."
    else:
        nombre_completo=nombre_columna+"."
    if isinstance(dataframe, list):
        #EL ELEMENTO ES LIST Y NO DICT
        e=[]
        for j in range(0,len(dataframe)):
            e.append(str(j))
        dataframe_list=dict(zip(e,dataframe))
        dataframe_dict=pd.DataFrame.from_dict(dataframe_list,orient="index")
        
    else:
        dataframe_dict=pd.DataFrame.from_dict(dataframe,orient="index")
    nombre_filas=dataframe_dict.index.values
    tamanio_dataframe=dataframe_dict.shape 
    
    filas=tamanio_dataframe[0]
    columnas=tamanio_dataframe[1]
    
    ##print("FILAS")
    ##print(filas)
    ##print("COLUMNAS")
    ##print(columnas)
    
    
    if("labels" in nombre_columna):
        insertar_labels2(dataframe_dict,columnas,filas)
    elif("object_refs" in nombre_columna):
        insertar_objects_refs2(dataframe_dict,columnas,filas)
                                             
ejemplo_dir = 'ALIENVAULT/FICHEROS IOT ALIENVAULT/'
contenido = os.listdir(ejemplo_dir)
for fichero in contenido:
    with open("ALIENVAULT/FICHEROS IOT ALIENVAULT/"+fichero,'r',encoding="utf-8") as f:
        data = json.loads(f.read())
    ##print("FICHEROOOOOOOOOOOOOOOOOO")
    ##print(fichero)
    #CONVIERTO A DATAFRAME EL JSON
    db=pd.DataFrame.from_dict(data)
    row_names1=db.index.values


    #EMPIEZO A TRABAJAR CON CVE_ITEMS, CONVIRTIENDOLO A DATAFRAME
    db_objects=pd.DataFrame(db["objects"])
    db_objects_aux=db_objects.transpose()

    if(db_objects_aux.shape[1]==1):
        #print("IFFFFFFFFFFFFFFFFFFFFFFFFFFF")
        #OBTENGO EL DATAFRAME CON EL QUE TRABAJARE
        db_objects2=pd.DataFrame.from_dict(db_objects_aux[0]["objects"],orient="index")
        nombres_filas=db_objects2.index.values

        #Vacio valores
        if((len(values) >0) and (values[0]!=None)):
            for n in range(0,len(values)):
                values[n]=None

        #ITERACCION 1
        for l in range (0,len(nombres_filas)):
            if ((isinstance(db_objects2[0][nombres_filas[l]], dict)) or (isinstance(db_objects2[0][nombres_filas[l]], list)) or (isinstance(db_objects2[0][nombres_filas[l]], pd.DataFrame))):
                recursiva(db_objects2[0][nombres_filas[l]],nombres_filas[l],0)
            else:
                #Veo si coincide con algun nombre de columna e inserto el elemento en esa posicion, previamente eliminado el elemento none para no aumentar el tamanio del array
                index = columns.index(nombres_filas[l])
                if(values[index]==None):
                    values.pop(index)
                    values.insert(index,db_objects2[0][nombres_filas[l]])

        array_aux7=[]
        for g in range(0,len(columns)):
            if((values[g] == None) or (values[g]=="null") or (len(values[g])==0)):
                array_aux7.append("NONE")
            else:
                array_aux7.append(values[g])
        array_aux7.append(fichero)
        values_grande.append(array_aux7)
    else:
        #print("ELSEEEEEEEEEEEEEEEEEEEEEEEEEE")
        ##print("SHAPEEEEEEEEEEEEEEEEEEEEE")
        ##print(db_objects_aux.shape[1])
        ##print("FICHERO")
        ##print(fichero)

        #print("FICHEROOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO")
        #print(fichero)
        ##print(db_objects_aux.shape[1])
        values_aux_grande=[]

        if((len(values_aux_grande) >0)):
            for n in range(0,len(values_aux_grande)):
                    values_aux_grande.pop()
        if(db_objects_aux.shape[1]>50):
            #print("ELSEEEEEEEEEEEEEEEEEEE1")
            for h in range (0,50):
                values_aux=[None] * len(columns)
                #OBTENGO EL DATAFRAME CON EL QUE TRABAJARE
                db_objects2=pd.DataFrame.from_dict(db_objects_aux[h]["objects"],orient="index")
                nombres_filas=db_objects2.index.values

                #Vacio valores
                #if((len(values_aux) >0) and (values_aux[0]!=None)):
                    ##print("ENTROOOOOOOOOOOOOOOOOOOOOOOOOOOO")
                    #for n in range(0,len(values_aux)):
                        #values_aux[n]=None

                #ITERACCION 1
                for l in range (0,len(nombres_filas)):
                    if ((isinstance(db_objects2[0][nombres_filas[l]], dict)) or (isinstance(db_objects2[0][nombres_filas[l]], list)) or (isinstance(db_objects2[0][nombres_filas[l]], pd.DataFrame))):
                        recursiva2(db_objects2[0][nombres_filas[l]],nombres_filas[l],h)
                    else:
                        #Veo si coincide con algun nombre de columna e inserto el elemento en esa posicion, previamente eliminado el elemento none para no aumentar el tamanio del array
                        index = columns.index(nombres_filas[l])
                        if(values_aux[index]==None):
                            values_aux.pop(index)
                            values_aux.insert(index,db_objects2[0][nombres_filas[l]])
                ##print("H")
                ##print(h)
                ##print(values_aux)
                array_aux12=[]
                for i in range(0,len(columns)):
                    elem=values_aux.pop()
                    if((elem == None) or (elem=="null") or (len(elem)==0)):
                        array_aux12.insert(0,"NONE")
                    else:
                        array_aux12.insert(0,elem)

                values_aux_grande.append(array_aux12)
                #print("VALUES_AUX_GRANDE")
                #print(values_aux_grande)
                #print(len(values_aux_grande))


                if(h==49):
                    array_aux13=[]
                    for j in range(0,len(columns)):
                        #print(j)
                        list1=[]
                        for k in range(0,50):
                            list1.append(values_aux_grande[k][j])
                            if(k==49):
                                if(list1.count("NONE") == len(list1)):
                                    array_aux13.append("NONE")
                                else:
                                    array_aux13.append(list1)
                    array_aux14=[]
                    for c in range(0,len(columns)):
                        if((array_aux13[c] == None) or (array_aux13[c]=="null") or(len(array_aux13[c])==0)):
                            array_aux14.append("NONE")
                        else:
                            if(c==1):
                                array_aux14.append(array_aux13[1][0])
                            elif(c==2):
                                if((array_aux13[2].count("NONE")) == (len(array_aux13[2])-1)):
                                    for z in range(0,len(array_aux13[2])):
                                        if(array_aux13[2][z]!='NONE'):
                                            array_aux14.append(array_aux13[2][z])
                                else:
                                    array_aux14.append(array_aux13[2])    
                            elif(c==4):
                                if((array_aux13[4].count("NONE")) == (len(array_aux13[4])-1)):
                                    for z in range(0,len(array_aux13[4])):
                                        if(array_aux13[4][z]!='NONE'):
                                            array_aux14.append(array_aux13[4][z])
                                else:
                                    array_aux14.append(array_aux13[4])  
                            elif(c==8):
                                array_aux14.append(array_aux13[8][0])
                            elif(c==9):
                                array_aux14.append(array_aux13[9][0])
                            elif(c==11):
                                array_aux14.append(array_aux13[11][1])
                            elif(c==12):
                                array_aux14.append("organization")
                            elif(c==14):
                                array_aux14.append("stix")
                            elif(c==16):
                                array_aux14.append("2.1")
                            elif(c==17):
                                if((array_aux13[17].count("NONE")) == (len(array_aux13[17])-1)):
                                    for z in range(0,len(array_aux13[17])):
                                        if(array_aux13[17][z]!='NONE'):
                                            array_aux14.append(array_aux13[17][z])
                                else:
                                    array_aux14.append(array_aux13[17]) 
                            else:
                                array_aux14.append(array_aux13[c])
                    array_aux14.append(fichero)
                    values_grande.append(array_aux14)
        else:
            #print("ELSEEEEEEEEEEEEEEEEEEEEEEEEE2")
            for h in range (0,db_objects_aux.shape[1]):
                values_aux=[None] * len(columns)
                #OBTENGO EL DATAFRAME CON EL QUE TRABAJARE
                db_objects2=pd.DataFrame.from_dict(db_objects_aux[h]["objects"],orient="index")
                nombres_filas=db_objects2.index.values

                #Vacio valores
                #if((len(values_aux) >0) and (values_aux[0]!=None)):
                    ##print("ENTROOOOOOOOOOOOOOOOOOOOOOOOOOOO")
                    #for n in range(0,len(values_aux)):
                        #values_aux[n]=None

                #ITERACCION 1
                for l in range (0,len(nombres_filas)):
                    if ((isinstance(db_objects2[0][nombres_filas[l]], dict)) or (isinstance(db_objects2[0][nombres_filas[l]], list)) or (isinstance(db_objects2[0][nombres_filas[l]], pd.DataFrame))):
                        recursiva2(db_objects2[0][nombres_filas[l]],nombres_filas[l],h)
                    else:
                        #Veo si coincide con algun nombre de columna e inserto el elemento en esa posicion, previamente eliminado el elemento none para no aumentar el tamanio del array
                        index = columns.index(nombres_filas[l])
                        if(values_aux[index]==None):
                            values_aux.pop(index)
                            values_aux.insert(index,db_objects2[0][nombres_filas[l]])
                ##print("H")
                ##print(h)
                ##print(values_aux)
                array_aux12=[]
                for i in range(0,len(columns)):
                    elem=values_aux.pop()
                    if((elem==None) or (elem=="null") or (elem=="")):
                        array_aux12.insert(0,"NONE")
                    else:
                        array_aux12.insert(0,elem)

                values_aux_grande.append(array_aux12)


                if(h==db_objects_aux.shape[1]-1):
                    array_aux13=[]
                    for j in range(0,len(columns)):
                        list1=[]
                        for k in range(0,db_objects_aux.shape[1]):
                            list1.append(values_aux_grande[k][j])
                            if(k==(db_objects_aux.shape[1]-1)):
                                if(list1.count("NONE") == len(list1)):
                                    array_aux13.append("NONE")
                                else:
                                    array_aux13.append(list1)
                    ##print("ARRAY_AUX13")
                    ##print(array_aux13)



                    array_aux14=[]
                    for c in range(0,len(columns)):
                        if((array_aux13[c] == None) or (array_aux13[c]=="null") or(len(array_aux13)==0)):
                            array_aux14.append("NONE")
                        else:
                            if(c==1):
                                array_aux14.append(array_aux13[1][0])
                            elif(c==2):
                                if((array_aux13[2].count("NONE")) == (len(array_aux13[2])-1)):
                                    for z in range(0,len(array_aux13[2])):
                                        if(array_aux13[2][z]!='NONE'):
                                            array_aux14.append(array_aux13[2][z])
                                else:
                                    array_aux14.append(array_aux13[2])    
                            elif(c==4):
                                if((array_aux13[4].count("NONE")) == (len(array_aux13[4])-1)):
                                    for z in range(0,len(array_aux13[4])):
                                        if(array_aux13[4][z]!='NONE'):
                                            array_aux14.append(array_aux13[4][z])
                                else:
                                    array_aux14.append(array_aux13[4])  
                            elif(c==8):
                                array_aux14.append(array_aux13[8][0])
                            elif(c==9):
                                array_aux14.append(array_aux13[9][0])
                            elif(c==11):
                                array_aux14.append(array_aux13[11][1])
                            elif(c==12):
                                array_aux14.append("organization")
                            elif(c==14):
                                array_aux14.append("stix")
                            elif(c==16):
                                array_aux14.append("2.1")
                            elif(c==17):
                                if((array_aux13[17].count("NONE")) == (len(array_aux13[17])-1)):
                                    for z in range(0,len(array_aux13[17])):
                                        if(array_aux13[17][z]!='NONE'):
                                            array_aux14.append(array_aux13[17][z])
                                else:
                                    array_aux14.append(array_aux13[17]) 
                            else:
                                array_aux14.append(array_aux13[c])
                    array_aux14.append(fichero)
                    values_grande.append(array_aux14)
    ##print("FINAAAAAAAAAAAAAAAAAL")
    ##print(len(values_grande))
    #for t in range(0,len(values_grande)):
        ##print("***********************")
        ##print(t)
        ##print(values_grande[t])
        ##print("___________________________") 
columns.append("Filename")    
dff=pd.DataFrame()

values_grande_tras = []
valuesdef=transpose(values_grande, values_grande_tras)



df_excel=pd.DataFrame(valuesdef,columns[0:20])
df_excel2=df_excel.transpose()
df_excel2.to_excel('alienvault_iot_2023.xlsx')