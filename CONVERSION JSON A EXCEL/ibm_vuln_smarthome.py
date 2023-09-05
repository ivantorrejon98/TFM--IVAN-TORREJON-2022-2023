

######CODIGO PARA PASAR A EXCEL VULNERABILIDADES IOT EN IBM********************************
import pandas as pd
import json
import math
import os


#ARRAYS DONDE GUARDARE EL NOMBRE DE TODAS LAS COLUMNAS Y SU VALOR
final=0
columns=["id","type","created","modified","name","description","external_references_source_name","external_references_external_id","labels","x_xfe_risk_level","x_xfe_cvss_version","x_xfe_cvss_privilegesrequired","x_xfe_cvss_userinteraction","x_xfe_cvss_scope","x_xfe_cvss_access_vector","x_xfe_cvss_access_complexity","x_xfe_cvss_confidentiality_impact","x_xfe_cvss_integrity_impact","x_xfe_cvss_availability_impact","x_xfe_cvss_remediation_level","x_xfe_temporal_score","x_xfe_remedy","x_xfe_platforms_affected","x_xfe_exploitability","x_xfe_consequences","x_xfe_report_confidence","x_xfe_references_link_target","x_xfe_references_link_name","x_xfe_references_description"]
values=[None] * len(columns)


####################################################################################
################################EXTERNAL REFERENCES#############################
#ARRAY PARA GUARDAR LOS VALORES DE SOURCE NAME DE EXTERNAL REFERENCES
external_references_source_name=[]
#ARRAY PARA GUARDAR LOS VALORES DE SOURCE NAME DE EXTERNAL ID DE EXTERNAL REFERENCES
external_references_external_id=[]

labels=[]


x_xfe_platforms_affected=[]


xfe_references_link_target=[]
xfe_references_link_name=[]
xfe_references_description=[]


values_grande=[]

def insertar_labels(dataframe,columnas):
    #print("INSERTAR_LABELS")
    #print(dataframe)
    #print("*")
    #print(len(dataframe))
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
        
    
def insertar_platforms_affected(dataframe,columnas):
    #print("PLATFORMS_AFFECTED")
    #print(dataframe)
    #print("*")
    #print(len(dataframe))
    if(len(dataframe)==1):
        index1 = columns.index("x_xfe_platforms_affected")
        if(values[index1]==None):
            values.pop(index1)
            values.insert(index1,dataframe[0])
    else:
        for g in range(0,len(dataframe)):
            if(g!=(len(dataframe)-1)):
                x_xfe_platforms_affected.append(dataframe[g])
            else:
                x_xfe_platforms_affected.append(dataframe[g])
                index7 = columns.index("x_xfe_platforms_affected")
                array_auxiliar_dos=[]
                for d in range(0,len(x_xfe_platforms_affected)):
                    elem_dos=x_xfe_platforms_affected.pop()
                    array_auxiliar_dos.insert(0,elem_dos)
                if(array_auxiliar_dos.count("null") == len(array_auxiliar_dos)):
                    if(values[index7]==None):
                        values.pop(index7)
                        values.insert(index7,"NONE") 
                else:
                    if(values[index7]==None):
                        values.pop(index7)
                        values.insert(index7,array_auxiliar_dos) 

#############################################################################################               
##########################METODOS PARA INSERTAR REFERENCE_DATA###############################            
def insertar_xfe_references(dataframe,columnas):
    #print("INSERTAR_XFE_REFERENCES")
    if isinstance(dataframe, list):
        #EL ELEMENTO ES LIST Y NO DICT
        e=[]
        for j in range(0,len(dataframe)):
            e.append(str(j))
            dataframe_list=dict(zip(e,dataframe))
        #CONSIGO EL DATAFRAME Y EL NUMERO DE COLUMNAS Y FILAS
        datafram=pd.DataFrame.from_dict(dataframe_list,orient="index")
    else:
        datafram=pd.DataFrame.from_dict(dataframe,orient="index")
    num_columns=len(datafram.columns.values)
    num_rows=len(datafram.index.values)
    
    datafra=datafram.transpose()
    #print(datafra.index.values)
    #print(datafra.columns.values)
    #SI EL NUMERO DE COLUMNAS ES 1, ES DECIR, UNA UNICA REFERENCIA
    if(num_rows==1):
        #INSERTO URL , NAME Y REFSOURCE
        index1 = columns.index("x_xfe_references_link_target")
        if(values[index1]==None):
            values.pop(index1)
            values.insert(index1,datafra["0"]["link_target"]) 
        index2 = columns.index("x_xfe_references_link_name")
        if(values[index2]==None):
            values.pop(index2)
            values.insert(index2,datafra["0"]["link_name"]) 
        index3 = columns.index("x_xfe_references_description")
        if(values[index3]==None):
            values.pop(index3)
            values.insert(index3,datafra["0"]["description"]) 
            
    #SI HAY MAS DE UNA COLUMNA
    else:
        for h in range(0,num_rows):
            #SI AUN NO HEMOS VISITADO TODAS LAS REFERENCIAS
            if (h<num_rows-1):
                #INSERTAMOS URL,NAME Y REFSOURCE
                xfe_references_link_target.append(datafra[datafra.columns.values[h]]["link_target"])
                xfe_references_link_name.append(datafra[datafra.columns.values[h]]["link_name"])
                xfe_references_description.append(datafra[datafra.columns.values[h]]["description"])
            else:
                #INSERTAMOS URL,NAME Y REFSOURCE
                xfe_references_link_target.append(datafra[datafra.columns.values[h]]["link_target"])
                xfe_references_link_name.append(datafra[datafra.columns.values[h]]["link_name"])
                xfe_references_description.append(datafra[datafra.columns.values[h]]["description"])
                
                #INSERTAMOS URL EN VALORES Y VACIAMOS EL ARRAY
                index6 = columns.index("x_xfe_references_link_target")
                array_auxiliar_uno=[]
                for e in range(0,len(xfe_references_link_target)):
                    elem_uno=xfe_references_link_target.pop()
                    array_auxiliar_uno.insert(0,elem_uno)
                if(array_auxiliar_uno.count("null") == len(array_auxiliar_uno)):
                    if(values[index6]==None):
                        values.pop(index6)
                        values.insert(index6,"null") 
                else:
                    if(values[index6]==None):
                        values.pop(index6)
                        values.insert(index6,array_auxiliar_uno) 
                    
                #INSERTAMOS NAME EN VALORES Y VACIAMOS EL ARRAY   
                index7 = columns.index("x_xfe_references_link_name")
                array_auxiliar_dos=[]
                for d in range(0,len(xfe_references_link_name)):
                    elem_dos=xfe_references_link_name.pop()
                    array_auxiliar_dos.insert(0,elem_dos)
                if(array_auxiliar_dos.count("null") == len(array_auxiliar_dos)):
                    if(values[index7]==None):
                        values.pop(index7)
                        values.insert(index7,"null") 
                else:
                    if(values[index7]==None):
                        values.pop(index7)
                        values.insert(index7,array_auxiliar_dos) 
                
                #INSERTAMOS REFSOURCE EN VALORES Y VACIAMOS EL ARRAY
                index8 = columns.index("x_xfe_references_description")
                array_auxiliar_tres=[]
                for e in range(0,len(xfe_references_description)):
                    elem_tres=xfe_references_description.pop()
                    array_auxiliar_tres.insert(0,elem_tres)
                if(array_auxiliar_tres.count("null") == len(array_auxiliar_tres)):
                    if(values[index8]==None):
                        values.pop(index8)
                        values.insert(index8,"null") 
                else:
                    if(values[index8]==None):
                        values.pop(index8)
                        values.insert(index8,array_auxiliar_tres) 
                    
                
##############################################################################################              
##########################METODOS PARA INSERTAR REFERENCE_DATA###############################            
def insertar_external_references(dataframe,columnas):
    if isinstance(dataframe, list):
        #EL ELEMENTO ES LIST Y NO DICT
        e=[]
        for j in range(0,len(dataframe)):
            e.append(str(j))
            dataframe_list=dict(zip(e,dataframe))
        #CONSIGO EL DATAFRAME Y EL NUMERO DE COLUMNAS Y FILAS
        datafram=pd.DataFrame.from_dict(dataframe_list,orient="index")
    else:
        datafram=pd.DataFrame.from_dict(dataframe,orient="index")
    num_columns=len(datafram.columns.values)
    num_rows=len(datafram.index.values)
    
    datafra=datafram.transpose()
    #SI EL NUMERO DE COLUMNAS ES 1, ES DECIR, UNA UNICA REFERENCIA
    if(num_rows==1):
        #INSERTO URL , NAME Y REFSOURCE
        index1 = columns.index("external_references_source_name")
        if(values[index1]==None):
            values.pop(index1)
            values.insert(index1,datafra["0"]["source_name"]) 
        index2 = columns.index("external_references_external_id")
        if(values[index2]==None):
            values.pop(index2)
            values.insert(index2,datafra["0"]["external_id"]) 
        
    #SI HAY MAS DE UNA COLUMNA
    else:
        for h in range(0,num_rows):
            #SI AUN NO HEMOS VISITADO TODAS LAS REFERENCIAS
            if (h<num_rows-1):
                #INSERTAMOS URL,NAME Y REFSOURCE
                external_references_source_name.append(datafra[datafra.columns.values[h]]["source_name"])
                external_references_external_id.append(datafra[datafra.columns.values[h]]["external_id"])
                
            else:
                #INSERTAMOS URL,NAME Y REFSOURCE
                external_references_source_name.append(datafra[datafra.columns.values[h]]["source_name"])
                external_references_external_id.append(datafra[datafra.columns.values[h]]["external_id"])
                
                #INSERTAMOS URL EN VALORES Y VACIAMOS EL ARRAY
                index6 = columns.index("external_references_source_name")
                array_auxiliar_uno=[]
                for e in range(0,len(external_references_source_name)):
                    elem_uno=external_references_source_name.pop()
                    array_auxiliar_uno.insert(0,elem_uno)
                if(array_auxiliar_uno.count("null") == len(array_auxiliar_uno)):
                    if(values[index6]==None):
                        values.pop(index6)
                        values.insert(index6,"null") 
                else:
                    if(values[index6]==None):
                        values.pop(index6)
                        values.insert(index6,array_auxiliar_uno) 
                    
                #INSERTAMOS NAME EN VALORES Y VACIAMOS EL ARRAY   
                index7 = columns.index("external_references_external_id")
                array_auxiliar_dos=[]
                for d in range(0,len(external_references_external_id)):
                    elem_dos=external_references_external_id.pop()
                    array_auxiliar_dos.insert(0,elem_dos)
                if(array_auxiliar_dos.count("null") == len(array_auxiliar_dos)):
                    if(values[index7]==None):
                        values.pop(index7)
                        values.insert(index7,"null") 
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
    
    #print("RECURSIVA")
    #print(nombre_columna)
    #print(dataframe)
    
    if("external_references" in nombre_columna):
        insertar_external_references(dataframe,columnas)
    elif("labels" in nombre_columna):
        insertar_labels(dataframe,columnas)
    elif("x_xfe_platforms_affected" in nombre_columna):
        insertar_platforms_affected(dataframe,columnas)
    elif("x_xfe_references" in nombre_columna):
        insertar_xfe_references(dataframe,columnas)                                         
    

ejemplo_dir = 'IBM\VULNERABILIDADES\SMART HOME\FICHEROS SMART HOME/'
contenido = os.listdir(ejemplo_dir)
for fichero in contenido:
    with open("IBM\VULNERABILIDADES\SMART HOME\FICHEROS SMART HOME/"+fichero,'r',encoding="utf-8") as f:
        data = json.loads(f.read())

    #CONVIERTO A DATAFRAME EL JSON
    db=pd.DataFrame.from_dict(data)
    row_names1=db.index.values


    #EMPIEZO A TRABAJAR CON CVE_ITEMS, CONVIRTIENDOLO A DATAFRAME
    db_objects=pd.DataFrame(db["objects"])
    db_objects_aux=db_objects.transpose()
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
        if((values[g] == None) or (values[g]=="null")):
            array_aux7.append("NONE")
        else:
            array_aux7.append(values[g])
    values_grande.append(array_aux7)

#print(columns)
#print(len(values_grande))


dff=pd.DataFrame()

values_grande_tras = []
valuesdef=transpose(values_grande, values_grande_tras)



df_excel=pd.DataFrame(valuesdef,columns[0:29])
df_excel2=df_excel.transpose()
df_excel2.to_excel('vulnerabilidades_ibm_smart_home_2023.xlsx')