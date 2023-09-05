
####################CODIGO NUEVO DEFINITIVO PARA CPES IOT#################################################

import pandas as pd
import json
import math
import openpyxl
########################################################################################
#################################VARIABLES##############################################


#ARRAYS DONDE GUARDARE EL NOMBRE DE TODAS LAS COLUMNAS Y SU VALOR
final=0
columns=["dataType","feedVersion","cpeCount","feedTimestamp","cpes.deprecated","cpes.cpe23Uri", "cpes.lastModifiedDate","cpes.titles.title","cpes.titles.lang","cpes.refs.ref","cpes.refs.type"]
values=[None] * len(columns)
values_grande=[]

####################################################################################
################################TITLES#############################

#ARRAY PARA GUARDAR LOS VALORES DE TITLE SI HAY MAS DE UN TITLE
titles_title=[]
#ARRAY PARA GUARDAR LOS VALORES DE LANG SI HAY MAS DE UN TITLE
titles_lang=[]

titles_size=0
################################REFS#############################

#ARRAY PARA GUARDAR LOS VALORES DE REF SI HAY MAS DE UNA REF
refs_ref=[]
#ARRAY PARA GUARDAR LOS VALORES DE TYPE SI HAY MAS DE UNA REF
refs_type=[]

refs_size=0

####################################################################################
####################################METODOS#########################################

#Metodo para eliminar los numeros del nombre
def eliminar_numeros_nombre(nombre_colum):
    string_devolver = ""
    string_devolver_final=""
    #Recorremos el string que pasamos por parametro
    for m in nombre_colum:
        #Si el caracter no es un numero lo insertamos en el array a devolver
        if (m.isdigit() ==False):
            string_devolver = string_devolver + m
            
    #Hemos eliminado los numeros, ahora eliminamos los puntos
    for s in range(0,len(string_devolver)):
        if(string_devolver[s]!="."):
            string_devolver_final = string_devolver_final + string_devolver[s] 
        else:
            if((s!=(len(string_devolver)-1)) and (s!=0)):
                if(string_devolver[s-1]!="."):
                    string_devolver_final = string_devolver_final + string_devolver[s]         
    return string_devolver_final




####################################################################################
#METODO PARA INSERTAR TITLES Y LANG EN TITLES
def insertar_titles(dataframe_dict,filas,columnas):
    #print("HOLAAAAAAAAA")
    #print(dataframe_dict)
    #print(filas)
    #print(columnas)
    #SI EXISTE UNA UNICA COLUMNA DE DESCRIPTION_DATA SIMPLEMENTE INSERTO LOS VALORES DE LANG Y VALUE, SIN ARRAY
    if(filas==1):
        index1 = columns.index("cpes.titles.title")
        if(values[index1]==None):
            values.pop(index1)
            values.insert(index1,dataframe_dict[dataframe_dict.columns.values[0]][0])
        index2 = columns.index("cpes.titles.lang")
        if(values[index2]==None):
            values.pop(index2)
            values.insert(index2,dataframe_dict[dataframe_dict.columns.values[1]][0])
    #CUANDO HAY MAS DE UNA COLUMNA DE DESCRIPTION_DATA
    else:
        
        #print("HOLA2")
        for g in range(0,columnas):
            for h in range(0,filas):
                #SI ESTOY EN LA PRIMERA FILA ESTOY EN LA FILA DE LANGS
                if(g==0):
                    titles_title.append(dataframe_dict[dataframe_dict.columns.values[g]][dataframe_dict.index.values[h]])
                    #INSERTO SI ESTOY EN EL ULTIMO VALOR DE LANG
                    if(h==filas-1):
                        array_aux1=[]
                        for r in range(0,len(titles_title)):
                            elem1=titles_title.pop()
                            array_aux1.insert(0,elem1)
                        index1_title = columns.index("cpes.titles.title")
                        #INSERTO EL ARRAY DE LANG
                        if(values[index1_title]==None):
                            values.pop(index1_title)
                            values.insert(index1_title,titles_title)
                else:
                    #SI ESTOY EN LA FILA DE VALUES
                    titles_lang.append(dataframe_dict[dataframe_dict.columns.values[g]][dataframe_dict.index.values[h]])
                    #SI ESTOY EN EL ULTIMO VALOR DE VALUES INSERTO
                    if(h==filas-1):
                        array_aux2=[]
                        for r in range(0,len(titles_lang)):
                            elem2=titles_lang.pop()
                            array_aux2.insert(0,elem2)
                        index2_lang = columns.index("cpes.titles.lang")
                        #INSERTO EL VALOR DE DESCRIPTION_DATA_VALUE
                        if(values[index2_lang]==None):
                            values.pop(index2_lang)
                            values.insert(index2_lang,titles_lang)       
        

#############################################################################################               
##########################METODOS PARA INSERTAR REFERENCE_DATA###############################            
def insertar_refs(dataframe,columnas):
    #print("INSERTAR_REFS")
    #print(dataframe)
    #print(type(dataframe))
    #CONSIGO EL DATAFRAME Y EL NUMERO DE COLUMNAS Y FILAS
    datafra=pd.DataFrame(dataframe)
    num_columns=len(datafra.columns.values)
    num_rows=len(datafra.index.values)
    
    #print("DATAFRAME")
    #print(datafra)
    #print(datafra.columns.values)
    #print(datafra.index.values)
    #SI EL NUMERO DE COLUMNAS ES 1, ES DECIR, UNA UNICA REFERENCIA
    if(num_rows==1):
        #print("AQUI")
        #print(datafra["ref"]["0"])
        #INSERTO URL , NAME Y REFSOURCE
        index1 = columns.index("cpes.refs.ref")
        if((values[index1]==None) and (datafra["ref"]["0"]!=None)):
                values.pop(index1)
                values.insert(index1,datafra["ref"]["0"]) 
        index2 = columns.index("cpes.refs.type")
        if('type' in datafra.columns.values):
            if((values[index2]==None) and (datafra["type"]["0"]!=None)):
                values.pop(index2)
                values.insert(index2,datafra["type"]["0"]) 
            
        
    
    #SI HAY MAS DE UNA COLUMNA
    else:
        for h in range(0,num_columns):
            #SI AUN NO HEMOS VISITADO TODAS LAS REFERENCIAS
            if (h<num_columns-1):
                #INSERTAMOS URL,NAME Y REFSOURCE
                refs_ref.append(datafra["ref"][datafra.index.values[h]])
                if('type' in datafra.columns.values):
                    refs_type.append(datafra["type"][datafra.index.values[h]])
            else:
                #INSERTAMOS URL,NAME Y REFSOURCE
                refs_ref.append(datafra["ref"][datafra.index.values[h]])
                if('type' in datafra.columns.values):
                    refs_type.append(datafra["type"][datafra.index.values[h]])
                
                #INSERTAMOS URL EN VALORES Y VACIAMOS EL ARRAY
                index6 = columns.index("cpes.refs.ref")
                array_auxiliar_uno=[]
                for e in range(0,len(refs_ref)):
                    elem_uno=refs_ref.pop()
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
                index7 = columns.index("cpes.refs.type")
                array_auxiliar_dos=[]
                for d in range(0,len(refs_type)):
                    elem_dos=refs_type.pop()
                    array_auxiliar_dos.insert(0,elem_dos)
                if(array_auxiliar_dos.count("null") == len(array_auxiliar_dos)):
                    if(values[index7]==None):
                        values.pop(index7)
                        values.insert(index7,"null") 
                else:
                    if(values[index7]==None):
                        values.pop(index7)
                        values.insert(index7,array_auxiliar_dos) 
        
######################################################################################
###############################FUNCION RECURSIVA######################################
def recursiva(dataframe,acum,nombre_columna,numero_dataframe):
    #print("*******")
    #print(acum)
    #print(nombre_columna)
    #print(dataframe)
    #print("RECURSIVA")
    
    if nombre_columna is not str:
        nombre_completo=acum+str(nombre_columna)+"."
    else:
        nombre_completo=acum+nombre_columna+"."
        
    
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
    #print("HOLAAAAAAAAA")
    #print(numero_dataframe)
    #print(nombre_completo)
    #print(filas)
    if(filas ==1) :
        if("cpes.titles" in nombre_completo):
            insertar_titles(dataframe_dict,filas,columnas)
        elif("cpes.refs" in nombre_completo):
            insertar_refs(dataframe_dict,columnas)
    else:
        if("cpes.refs" in nombre_completo):
            insertar_refs(dataframe_dict,columnas)
        
            
            
            
def transpose(l1, l2):

    # iterate over list l1 to the length of an item
    for i in range(len(l1[0])):
        # print(i)
        row =[]
        for item in l1:
            # appending to new list with values and index positions
            # i contains index position and item contains values
            row.append(item[i])
        l2.append(row)
    return l2           
            
            
            
            




###############################################################################################
#################################COMIENZO DEL PROGRAMA##########################################   



#ABRO DOCUMENTO
with open('List_cpes_smarthome_2023.json','r',encoding='utf-8') as f:
    data = json.loads(f.read())

#CONVIERTO A DATAFRAME EL JSON GLOBAL
dataframe_inicial=pd.DataFrame.from_dict(data)

nombres_filas_inicial=dataframe_inicial.index.values



#EMPIEZO A TRABAJAR CON CVE_ITEMS, CONVIRTIENDOLO A DATAFRAME
cpe_items=pd.DataFrame(dataframe_inicial.result["cpes"])
cpe_items_aux=cpe_items.transpose()

acumulado="cpes."

#db_cve_items_aux.shape[1]
#ME QUEDO AQUI, COMPROBAR INSERTAR NODES CHILDREN
for h in range (0,cpe_items_aux.shape[1]):
    #Vacio valores
    if((len(values) >0) and (values[0]!=None)):
        for n in range(0,len(values)):
            values[n]=None
    values.pop(0)
    values.pop(1)
    values.pop(2)
    values.pop(3)
    values.insert(0,"CPE")
    values.insert(1,"1.0")
    values.insert(2,241)
    values.insert(3,"2023-04-11T21:11Z")
    
    nombre_vulnerabilidad="cpe"+str(h)
           
    #Veo si tenemos que recorrer el dataframe de cada columna o no
    for l in range(0,cpe_items_aux.shape[0]):
        if ((isinstance(cpe_items_aux[h][nombres_filas_cpe_items[l]], dict)) or (isinstance(cpe_items_aux[h][nombres_filas_cpe_items[l]], list)) or (isinstance(cpe_items_aux[h][nombres_filas_cpe_items[l]], pd.DataFrame))):
            #print("hola")
            #print("")
            recursiva(cpe_items_aux[h][nombres_filas_cpe_items[l]],acumulado,nombres_filas_cpe_items[l],h)
        else:
            #Veo si coincide con algun nombre de columna e inserto el elemento en esa posicion, previamente eliminado el elemento none para no aumentar el tamanio del array
            index = columns.index(acumulado+nombres_filas_cpe_items[l])
            if(values[index]==None):
                values.pop(index)
                values.insert(index,cpe_items_aux[h][nombres_filas_cpe_items[l]])
    dff=pd.DataFrame()
    #print("/////////////////")
    #print(h)
    #print(values)
    #for r in range(0,len(columns)):
        #print("**********************")
        #print(columns[r])
        #print(values[r])
    #print(h)
    
    array_aux7=[]
    for g in range(0,len(columns)):
        if((values[g] == None) or (values[g]=="null")):
            array_aux7.append("NONE")
        else:
            array_aux7.append(values[g])
    values_grande.append(array_aux7)
    
    #print("*********************")
    #print(columns)
    #print("///////////////////")
    #print(values)
#print(len(values_grande))


 

values_grande_tras = []
valuesdef=transpose(values_grande, values_grande_tras)



df_excel=pd.DataFrame(valuesdef,columns[0:11])
df_excel2=df_excel.transpose()
df_excel2.to_excel('cpes_smart_home_2023.xlsx')

