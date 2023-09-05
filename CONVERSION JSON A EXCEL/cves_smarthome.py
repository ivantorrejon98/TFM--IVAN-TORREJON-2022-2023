

import pandas as pd
import json
import math
import openpyxl




####################CODIGO NUEVO DEFINITIVO PARA CVES SMART HOME#################################################
########################################################################################
#################################VARIABLES##############################################


#ARRAYS DONDE GUARDARE EL NOMBRE DE TODAS LAS COLUMNAS Y SU VALOR
final=0
columns=["CVE_data_type","CVE_data_format","CVE_data_version","CVE_data_timestamp","CVE_Items.cve.data_type","CVE_Items.cve.data_format", "CVE_Items.cve.data_version","CVE_Items.cve.CVE_data_meta.ID","CVE_Items.cve.CVE_data_meta.ASSIGNER","CVE_Items.cve.problemtype.problemtype_data.description.lang","CVE_Items.cve.problemtype.problemtype_data.description.value","CVE_Items.cve.references.reference_data.url","CVE_Items.cve.references.reference_data.name","CVE_Items.cve.references.reference_data.refsource","CVE_Items.cve.references.reference_data.tags","CVE_Items.cve.description.description_data.lang","CVE_Items.cve.description.description_data.value","CVE_Items.configurations.CVE_data_version","CVE_Items.configurations.nodes.operator","CVE_Items.configurations.nodes.children.operator","CVE_Items.configurations.nodes.children.cpe_match.vulnerable","CVE_Items.configurations.nodes.children.cpe_match.versionEndIncluding","CVE_Items.configurations.nodes.children.cpe_match.cpe23Uri","CVE_Items.configurations.nodes.children.cpe_match.cpe_name","CVE_Items.configurations.nodes.cpe_match.vulnerable","CVE_Items.configurations.nodes.cpe_match.cpe23Uri","CVE_Items.configurations.nodes.cpe_match.versionEndIncluding","CVE_Items.impact.baseMetricV3.cvssV3.version","CVE_Items.impact.baseMetricV3.cvssV3.vectorString","CVE_Items.impact.baseMetricV3.cvssV3.attackVector","CVE_Items.impact.baseMetricV3.cvssV3.attackComplexity","CVE_Items.impact.baseMetricV3.cvssV3.privilegesRequired","CVE_Items.impact.baseMetricV3.cvssV3.userInteraction","CVE_Items.impact.baseMetricV3.cvssV3.scope","CVE_Items.impact.baseMetricV3.cvssV3.confidentialityImpact","CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact","CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact","CVE_Items.impact.baseMetricV3.cvssV3.baseScore","CVE_Items.impact.baseMetricV3.cvssV3.baseSeverity","CVE_Items.impact.baseMetricV3.exploitabilityScore","CVE_Items.impact.baseMetricV3.impactScore","CVE_Items.impact.baseMetricV2.cvssV2.version", "CVE_Items.impact.baseMetricV2.cvssV2.vectorString", "CVE_Items.impact.baseMetricV2.cvssV2.accessVector","CVE_Items.impact.baseMetricV2.cvssV2.accessComplexity","CVE_Items.impact.baseMetricV2.cvssV2.authentication","CVE_Items.impact.baseMetricV2.cvssV2.confidentialityImpact","CVE_Items.impact.baseMetricV2.cvssV2.integrityImpact","CVE_Items.impact.baseMetricV2.cvssV2.availabilityImpact","CVE_Items.impact.baseMetricV2.cvssV2.baseScore", "CVE_Items.impact.baseMetricV2.severity","CVE_Items.impact.baseMetricV2.exploitabilityScore","CVE_Items.impact.baseMetricV2.impactScore","CVE_Items.impact.baseMetricV2.acInsufInfo","CVE_Items.impact.baseMetricV2.obtainAllPrivilege","CVE_Items.impact.baseMetricV2.obtainUserPrivilege","CVE_Items.impact.baseMetricV2.obtainOtherPrivilege","CVE_Items.impact.baseMetricV2.userInteractionRequired","CVE_Items.publishedDate","CVE_Items.lastModifiedDate"]
values=[]
values_grande=[]

####################################################################################
################################PROBLEM TYPE#############################

#ARRAY PARA GUARDAR LOS VALORES DE LANG SI HAY MAS DE UNA DESCRIPCION
description_lang=[]
#ARRAY PARA GUARDAR LOS VALORES DE LANG SI HAY MAS DE UN PROBLEMTYPE_DATA, INSERTAREMOS LOS ARRAYS DE DESCRIPTION_LANG
problemtype_data_description_lang=[]


#ARRAY PARA GUARDAR LOS VALORES DE VALUE SI HAY MAS DE UNA DESCRIPCION
description_value=[]
#ARRAY PARA GUARDAR LOS VALORES DE VALUE SI HAY MAS DE UN PROBLEMTYPE_DATA, INSERTAREMOS LOS ARRAYS DE DESCRIPTION_VALUE
problemtype_data_description_value=[]
#VARIABLE PARA GUARDAR EL TAMANIO DE DESCRIPTION EN PROBLEMTYPE_DATA
problem_type_data_description_size=0



####################################################################################
################################REFERENCE_DATA#############################
#ARRAY PARA GUARDAR LOS VALORES DE URL DE REFERENCE_DATA
reference_data_url=[]
#ARRAY PARA GUARDAR LOS VALORES DE NAME DE REFERENCE_DATA
reference_data_name=[]
#ARRAY PARA GUARDAR LOS VALORES DE REFSOURCE DE REFERENCE_DATA
reference_data_refsource=[]
#ARRAY PARA GUARDAR LOS VALORES DE TAGS DE REFERENCE_DATA
reference_data_tags=[]
#ARRAY PARA GUARDAR LOS VALORES DE LOS ARRAYS DE TAGS DE REFERENCE_DATA
references_reference_data_tags=[]
#VARIABLE PARA GUARDAR EL TAMANIO O LA CANTIDAD DE REFERENCES QUE HAY
references_size=0





####################################################################################
################################DESCRIPTION_DATA#############################
#ARRAY PARA GUARDAR LOS VALORES DE lANG EN DESCRIPTION_DATA
description_data_lang=[]
#ARRAY PARA GUARDAR LOS VALORES DE VALUE EN DESCRIPTION_DATA
description_data_value=[]








####################################################################################
################################CONFIGURATION NODES#############################

#ARRAY PARA GUARDAR LOS OPERADORES DE LOS NODOS
nodes_operator=[]

############################CHILDRENS########################################################

#ARRAY PARA GUARDAR LOS VALORES DE LOS OPERADORES DE LOS DIFERENTES HIJOS DE CADA UNO DE LOS NODOS, PUEDE SER NULL
children_operator=[]
#ARRAY PARA GUARDAR LOS VALORES DE LOS OPERADORES DE TODOS LOS NODOS
nodes_children_operator=[]

#ARRAY PARA GUARDAR LOS VALORES DE LOS DIFERENTES CPE MATCH VULNERABLE DE CADA CHILDREN,PUEDE SER NULL
cpe_match_vulnerable_children=[]
#ARRAY PARA GUARDAR LOS VALORES DE LOS DIFERENTES CPE MATCH CPE23URI DE CADA CHILDREN,PUEDE SER NULL
cpe_match_cpe23Uri_children=[]
#ARRAY PARA GUARDAR LOS VALORES DE LOS DIFERENTES CPE MATCH VERSIONENDINCLUDING DE CADA CHILDREN,PUEDE SER NULL
cpe_match_versionEndIncluding_children=[]
#ARRAY PARA GUARDAR LOS VALORES DE LOS DIFERENTES CPE MATCH CPENAME DE CADA CHILDREN,PUEDE SER NULL,NORMALMENTE VACIO
cpe_match_cpename_children=[]


#ARRAY PARA GUARDAR LOS VALORES DE LOS ARRAYS DE CPE_MATCH VULNERABLE DE TODOS LOS CHILDREN DE CADA NODO,PUEDE SER NULL
children_cpe_match_vulnerable=[]
#ARRAY PARA GUARDAR LOS VALORES DE LOS ARRAYS DE CPE_MATCH CPE23URI DE TODOS LOS CHILDREN DE CADA NODO,PUEDE SER NULL
children_cpe_match_cpe23Uri=[]
#ARRAY PARA GUARDAR LOS VALORES DE LOS ARRAYS DE CPE_MATCH VERSIONENDINCLUDING DE TODOS LOS CHILDREN DE CADA NODO,PUEDE SER NULL
children_cpe_match_versionEndIncluding=[]
#ARRAY PARA GUARDAR LOS VALORES DE LOS ARRAYS DE CPE_MATCH CPENAME DE TODOS LOS CHILDREN DE CADA NODO,SUELE SER NULL
children_cpe_match_cpename=[]


#ARRAY PARA GUARDAR LOS VALORES DE LOS ARRAYS DE CPE_MATCH VULNERABLE DE TODOS LOS CHILDREN DE TODOS LOS NODOS,PUEDE SER NULL
nodes_children_cpe_match_vulnerable=[]
#ARRAY PARA GUARDAR LOS VALORES DE LOS ARRAYS DE CPE_MATCH CPE23URI DE TODOS LOS CHILDREN DE TODOS LOS NODOS,PUEDE SER NULL
nodes_children_cpe_match_cpe23Uri=[]
#ARRAY PARA GUARDAR LOS VALORES DE LOS ARRAYS DE CPE_MATCH VERSIONENDINCLUDING DE TODOS LOS CHILDREN DE TODOS LOS NODOS,PUEDE SER NULL
nodes_children_cpe_match_versionEndIncluding=[]
#ARRAY PARA GUARDAR LOS VALORES DE LOS ARRAYS DE CPE_MATCH CPENAME DE TODOS LOS CHILDREN DE TODOS LOS NODOS,SUELE SER NULL
nodes_children_cpe_match_cpename=[]



############################CPE_MATCH########################################################

#ARRAY PARA GUARDAR LOS VALORES DE LOS DIFERENTES CPE MATCH VULNERABLE DE CADA NODO,PUEDE SER NULL
cpe_match_vulnerable=[]
#ARRAY PARA GUARDAR LOS VALORES DE LOS DIFERENTES CPE MATCH CPE23URI DE CADA NODO,PUEDE SER NULL
cpe_match_cpe23Uri=[]
#ARRAY PARA GUARDAR LOS VALORES DE LOS DIFERENTES CPE MATCH VERSIONENDINCLUDING DE CADA NODO,PUEDE SER NULL
cpe_match_versionEndIncluding=[]

#ARRAY PARA GUARDAR LOS VALORES DE LOS DIFERENTES CPE MATCH VULNERABLE DE TODOS LOS NODOS,PUEDE SER NULL
nodes_cpe_match_vulnerable=[]
#ARRAY PARA GUARDAR LOS VALORES DE LOS DIFERENTES CPE MATCH CPE23URI DE TODOS LOS NODOS,PUEDE SER NULL
nodes_cpe_match_cpe23Uri=[]
#ARRAY PARA GUARDAR LOS VALORES DE LOS DIFERENTES CPE MATCH VERSIONENDINCLUDING DE TODOS LOS NODOS,PUEDE SER NULL
nodes_cpe_match_versionEndIncluding=[]


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
########################METODOS PARA DESCRIPTION####################################
#METODO PARA INSERTAR LANG Y VALUE CUANDO HAY MAS DE UNA DESCRIPCION EN PROBLEMTYPE_DATA
def insertar_problemtype_data_description(dataframe_dict_traspuesto,filas_tras,columnas_tras):
    
    for g in range(0,len(columnas_tras)):
        for h in range(0,len(filas_tras)):
            #EXTRAIGO EL DATAFRAME DE CADA UNA DE LAS COLUMNAS
            dataframe_dict=pd.DataFrame.from_dict(dataframe_dict_traspuesto[columnas_tras[g]][filas_tras[h]],orient="index")
            description_lang.append(dataframe_dict[0]["lang"])
            description_value.append(dataframe_dict[0]["value"])
            #SI ESTOY EN LA ULTIMA COLUMNA, ES DECIR, LA ULTIMA DESCRIPCION, INSERTO EN LOS VALORES
            if(h==(len(filas_tras)-1)):
                array_aux1=[]
                #INSERTO LANG
                for k in range(0,len(description_lang)):
                    elem1=description_lang.pop()
                    array_aux1.insert(0,elem1)
                index1 = columns.index("CVE_Items.cve.problemtype.problemtype_data.description.lang")
                if(values[index1]==None):
                    values.pop(index1)
                    values.insert(index1,array_aux1)
                array_aux2=[]
                #INSERTO VALORES
                for k in range(0,len(description_value)):
                    elem2=description_value.pop()
                    array_aux2.insert(0,elem2) 
                index2 = columns.index("CVE_Items.cve.problemtype.problemtype_data.description.value")
                if(values[index2]==None):
                    values.pop(index2)
                    values.insert(index2,array_aux2)
                    
                    
                    
                    
####################################################################################
#METODO PARA INSERTAR LANG Y VALUE EN DESCRIPTION_DATA
def insertar_description_data(dataframe_dict,filas,columnas):
    #SI EXISTE UNA UNICA COLUMNA DE DESCRIPTION_DATA SIMPLEMENTE INSERTO LOS VALORES DE LANG Y VALUE, SIN ARRAY
    if(columnas==1):
        index1 = columns.index("CVE_Items.cve.description.description_data.lang")
        if(values[index1]==None):
            values.pop(index1)
            values.insert(index1,dataframe_dict[dataframe_dict.columns.values[0]]["lang"])
        index2 = columns.index("CVE_Items.cve.description.description_data.value")
        if(values[index2]==None):
            values.pop(index2)
            values.insert(index2,dataframe_dict[dataframe_dict.columns.values[0]]["value"])
    #CUANDO HAY MAS DE UNA COLUMNA DE DESCRIPTION_DATA
    else:
        for g in range(0,filas):
            for h in range(0,columnas):
                #SI ESTOY EN LA PRIMERA FILA ESTOY EN LA FILA DE LANGS
                if(g==0):
                    description_data_lang.append(dataframe_dict[dataframe_dict.columns.values[h]][dataframe_dict.index.values[g]])
                    #INSERTO SI ESTOY EN EL ULTIMO VALOR DE LANG
                    if(h==columnas-1):
                        array_aux1=[]
                        for r in range(0,len(description_data_lang)):
                            elem1=description_data_lang.pop()
                            array_aux1.insert(0,elem1)
                        index1_lang = columns.index("CVE_Items.cve.description.description_data.lang")
                        #INSERTO EL ARRAY DE LANG
                        if(values[index1_lang]==None):
                            values.pop(index1_lang)
                            values.insert(index1_lang,description_data_lang)
                else:
                    #SI ESTOY EN LA FILA DE VALUES
                    description_data_value.append(dataframe_dict[dataframe_dict.columns.values[h]][dataframe_dict.index.values[g]])
                    #SI ESTOY EN EL ULTIMO VALOR DE VALUES INSERTO
                    if(h==columnas-1):
                        array_aux2=[]
                        for r in range(0,len(description_data_value)):
                            elem2=description_data_value.pop()
                            array_aux2.insert(0,elem2)
                        index2_lang = columns.index("CVE_Items.cve.description.description_data.value")
                        #INSERTO EL VALOR DE DESCRIPTION_DATA_VALUE
                        if(values[index2_lang]==None):
                            values.pop(index2_lang)
                            values.insert(index2_lang,description_data_value)

######################################################################################                
##########################METODOS PARA INSERTAR METRICAS###############################
#METODO PARA INSERTAR METRICAS
def insertar_metrics(colum_traspuesto,name_completo,filas_tras,datafram_dict_traspuesto):
    if(len(colum_traspuesto)==1):
        for r in range (0,len(datafram_dict_traspuesto[colum_traspuesto[0]].index.values)):
            #print(datafram_dict_traspuesto[colum_traspuesto[0]][filas_tras[r]])
            if ((isinstance(datafram_dict_traspuesto[colum_traspuesto[0]][filas_tras[r]], dict)) or (isinstance(datafram_dict_traspuesto[colum_traspuesto[0]][filas_tras[r]], list)) or (isinstance(datafram_dict_traspuesto[colum_traspuesto[0]][filas_tras[r]], pd.DataFrame))):
                recursiva(datafram_dict_traspuesto[colum_traspuesto[0]][filas_tras[r]],name_completo+colum_traspuesto[0]+".",filas_tras[r],0)
            else:
                #BUSCAMOS LA POSICION DONDE INSERTAR E INSERTAMOS
                index = columns.index(name_completo+colum_traspuesto[0]+"."+filas_tras[r])
                if(values[index]==None):
                    values.pop(index)
                    values.insert(index,datafram_dict_traspuesto[colum_traspuesto[0]][filas_tras[r]])
    else:
        for k in range (0,len(colum_traspuesto)):
            if(k==0):
                #print(len(datafram_dict_traspuesto[colum_traspuesto[k]].index.values))
                #print(datafram_dict_traspuesto[colum_traspuesto[k]].index.values)
                for l in range (0,len(datafram_dict_traspuesto[colum_traspuesto[k]].index.values)):
                    if(isinstance(datafram_dict_traspuesto[colum_traspuesto[k]][datafram_dict_traspuesto[colum_traspuesto[k]].index.values[l]],float)):
                        if(math.isnan(datafram_dict_traspuesto[colum_traspuesto[k]][datafram_dict_traspuesto[colum_traspuesto[k]].index.values[l]])==False):
                            #BUSCAMOS LA POSICION DONDE INSERTAR E INSERTAMOS
                            index = columns.index(name_completo+colum_traspuesto[k]+"."+datafram_dict_traspuesto[colum_traspuesto[k]].index.values[l])
                            if(values[index]==None):
                                values.pop(index)
                                values.insert(index,datafram_dict_traspuesto[colum_traspuesto[k]][datafram_dict_traspuesto[colum_traspuesto[k]].index.values[l]])
                    elif ((isinstance(datafram_dict_traspuesto[colum_traspuesto[k]][filas_tras[l]], dict)) or (isinstance(datafram_dict_traspuesto[colum_traspuesto[k]][filas_tras[l]], list)) or (isinstance(datafram_dict_traspuesto[colum_traspuesto[k]][filas_tras[l]], pd.DataFrame))):
                        recursiva(datafram_dict_traspuesto[colum_traspuesto[k]][filas_tras[l]],name_completo+colum_traspuesto[k]+".",filas_tras[l],k)
                    else:
                        #BUSCAMOS LA POSICION DONDE INSERTAR E INSERTAMOS
                        index = columns.index(name_completo+colum_traspuesto[k]+"."+filas_tras[l])
                        if(values[index]==None):
                            values.pop(index)
                            values.insert(index,datafram_dict_traspuesto[colum_traspuesto[k]][filas_tras[l]])

            else:
                for l in range (0,len(datafram_dict_traspuesto[colum_traspuesto[k]].index.values)):
                    if(isinstance(datafram_dict_traspuesto[colum_traspuesto[k]][datafram_dict_traspuesto[colum_traspuesto[k]].index.values[l]],float)):
                        if(math.isnan(datafram_dict_traspuesto[colum_traspuesto[k]][datafram_dict_traspuesto[colum_traspuesto[k]].index.values[l]])==False):
                            #BUSCAMOS LA POSICION DONDE INSERTAR E INSERTAMOS
                            index = columns.index(name_completo+colum_traspuesto[k]+"."+datafram_dict_traspuesto[colum_traspuesto[k]].index.values[l])
                            if(values[index]==None):
                                values.pop(index)
                                values.insert(index,datafram_dict_traspuesto[colum_traspuesto[k]][datafram_dict_traspuesto[colum_traspuesto[k]].index.values[l]])
                    elif ((isinstance(datafram_dict_traspuesto[colum_traspuesto[k]][filas_tras[l]], dict)) or (isinstance(datafram_dict_traspuesto[colum_traspuesto[k]][filas_tras[l]], list)) or (isinstance(datafram_dict_traspuesto[colum_traspuesto[k]][filas_tras[l]], pd.DataFrame))):
                        recursiva(datafram_dict_traspuesto[colum_traspuesto[k]][filas_tras[l]],name_completo+colum_traspuesto[k]+".",filas_tras[l],k)
                    else:
                        #BUSCAMOS LA POSICION DONDE INSERTAR E INSERTAMOS
                        index = columns.index(name_completo+colum_traspuesto[k]+"."+filas_tras[l])
                        if(values[index]==None):
                            values.pop(index)
                            values.insert(index,datafram_dict_traspuesto[colum_traspuesto[k]][filas_tras[l]])
                        
                        
#############################################################################################               
##########################METODOS PARA INSERTAR REFERENCE_DATA###############################            
def insertar_reference_data(dataframe,columnas):
    #CONSIGO EL DATAFRAME Y EL NUMERO DE COLUMNAS Y FILAS
    datafra=pd.DataFrame.from_dict(dataframe,orient="index")
    num_columns=len(datafra.columns.values)
    num_rows=len(datafra.index.values)
    
    #SI EL NUMERO DE COLUMNAS ES 1, ES DECIR, UNA UNICA REFERENCIA
    if(num_columns==1):
        if(len(reference_data_tags) >0):
            for c in range(0,len(reference_data_tags)):
                reference_data_tags.pop()
        #print("NUMCOLUMNS1")
        #print(reference_data_tags)
        #INSERTO URL , NAME Y REFSOURCE
        index1 = columns.index("CVE_Items.cve.references.reference_data.url")
        if(values[index1]==None):
            values.pop(index1)
            values.insert(index1,datafra[0][0]["url"]) 
        index2 = columns.index("CVE_Items.cve.references.reference_data.name")
        if(values[index2]==None):
            values.pop(index2)
            values.insert(index2,datafra[0][0]["name"]) 
        index3 = columns.index("CVE_Items.cve.references.reference_data.refsource")
        if(values[index3]==None):
            values.pop(index3)
            values.insert(index3,datafra[0][0]["refsource"]) 
            
        #AVERIGUO CUANTOS TAGS HAY
        len_tags=len(datafra[0][0]["tags"])
        #print("TAGS")
        #print(dataframe)
        #print(datafra[0][0]["tags"])
        #print(len_tags)
        #SI SOLO HAY UN TAG INSERTO EL TAG QUE HAY
        if(len_tags==1):
            #print("if1")
            index4 = columns.index("CVE_Items.cve.references.reference_data.tags")
            if(values[index4]==None):
                values.pop(index4)
                values.insert(index4,datafra[0][0]["tags"][0])
                
        #SI HAY MAS DE UN TAG VOY INSERTANDO EN EL ARRAY HASTA QUE LLEGO AL ULTIMO, DONDE INSERTO EL ARRAY EN LOS VALORES
        elif(len_tags>1):
            #print("if2")
            for r in range(0,len_tags):
                if(r<len_tags-1):
                    reference_data_tags.append(datafra[0][0]["tags"][r])
                else:
                    reference_data_tags.append(datafra[0][0]["tags"][r])
                    array_aux1=[]
                    #INSERTO LANG
                    for k in range(0,len(reference_data_tags)):
                        elem1=reference_data_tags.pop()
                        array_aux1.insert(0,elem1)
                    index5 = columns.index("CVE_Items.cve.references.reference_data.tags")
                    if(values[index5]==None):
                        values.pop(index5)
                        values.insert(index5,array_aux1)
                 
                        #print(reference_data_tags)
        #print("VALUES1")
        #print(values)
        #print(len(values))
    
    #SI HAY MAS DE UNA COLUMNA
    else:
        for h in range(0,num_columns):
            if(len(reference_data_tags) >0):
                for c in range(0,len(reference_data_tags)):
                    reference_data_tags.pop()
            #SI AUN NO HEMOS VISITADO TODAS LAS REFERENCIAS
            if (h<num_columns-1):
                #INSERTAMOS URL,NAME Y REFSOURCE
                reference_data_url.append(datafra[h][0]["url"])
                reference_data_name.append(datafra[h][0]["name"])
                reference_data_refsource.append(datafra[h][0]["refsource"])
                
                #CALCULAMOS EL LARGO DEL ARRAY DE TAGS DE ESTA REFERENCIA
                len_tags_dos=len(datafra[h][0]["tags"])
                #print("ENTROOOOOOOOOOOOOO TAAAAAAGS")
                if(len_tags_dos==0):
                    #SI EL ARRAY DE TAGS ESTA VACIO INSERTO NULL EN EL ARRAY GRANDE
                    references_reference_data_tags.append("null")
                else:
                    #RECORREMOS EL ARRAY DE TAGS CORRESPONDIENTE
                    for k in range(0,len_tags_dos):
                        #SI SOLO HAY UN TAG EN ESTA REFERENCIA LO INSERTO DIRECTAMENTE EN EL ARRAY GRANDE
                        if(len_tags_dos==1):
                            references_reference_data_tags.append(datafra[h][0]["tags"][0])
                        #SI HAY MAS DE UN TAG VOY INSERTANDO EN EL ARRAY HASTA QUE LLEGO AL ULTIMO, DONDE INSERTO EL ARRAY EN LOS VALORES
                        elif(len_tags_dos>1):
                            if(k<len_tags_dos-1):
                                reference_data_tags.append(datafra[h][0]["tags"][k])
                                #INSERTO EL ARRAY DE TAGS PEQUENIO EN EL ARRAY GRANDE
                            else:
                                reference_data_tags.append(datafra[h][0]["tags"][k])
                                array_auxiliar=[]
                                for t in range(0,len(reference_data_tags)):
                                    elem=reference_data_tags.pop()
                                    array_auxiliar.insert(0,elem)
                                references_reference_data_tags.append(array_auxiliar)
            else:
                #INSERTAMOS URL,NAME Y REFSOURCE
                reference_data_url.append(datafra[h][0]["url"])
                reference_data_name.append(datafra[h][0]["name"])
                reference_data_refsource.append(datafra[h][0]["refsource"])
                
                #INSERTAMOS URL EN VALORES Y VACIAMOS EL ARRAY
                index6 = columns.index("CVE_Items.cve.references.reference_data.url")
                array_auxiliar_uno=[]
                for e in range(0,len(reference_data_url)):
                    elem_uno=reference_data_url.pop()
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
                index7 = columns.index("CVE_Items.cve.references.reference_data.name")
                array_auxiliar_dos=[]
                for d in range(0,len(reference_data_name)):
                    elem_dos=reference_data_name.pop()
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
                index8 = columns.index("CVE_Items.cve.references.reference_data.refsource")
                array_auxiliar_tres=[]
                for e in range(0,len(reference_data_refsource)):
                    elem_tres=reference_data_refsource.pop()
                    array_auxiliar_tres.insert(0,elem_tres)
                if(array_auxiliar_tres.count("null") == len(array_auxiliar_tres)):
                    if(values[index8]==None):
                        values.pop(index8)
                        values.insert(index8,"null") 
                else:
                    if(values[index8]==None):
                        values.pop(index8)
                        values.insert(index8,array_auxiliar_tres) 
                    
                
                #INSERTAMOS TAGS EN VALORES Y VACIAMOS EL ARRAY
                #CALCULAMOS EL LARGO DEL ARRAY DE TAGS DE ESTA REFERENCIA
                len_tags_tres=len(datafra[h][0]["tags"])
                if(len_tags_tres==0):                    
                    #SI EL ARRAY DE TAGS ESTA VACIO INSERTO NULL EN EL ARRAY GRANDE
                    references_reference_data_tags.append("null")
                else:
                    #RECORREMOS EL ARRAY DE TAGS CORRESPONDIENTE
                    for k in range(0,len_tags_tres):
                        #SI SOLO HAY UN TAG EN ESTA REFERENCIA LO INSERTO DIRECTAMENTE EN EL ARRAY GRANDE
                        if(len_tags_tres==1):
                            references_reference_data_tags.append(datafra[h][0]["tags"][0])
                        #SI HAY MAS DE UN TAG VOY INSERTANDO EN EL ARRAY HASTA QUE LLEGO AL ULTIMO, DONDE INSERTO EL ARRAY EN LOS VALORES
                        elif(len_tags_tres>1):
                            if(k<len_tags_tres-1):
                                reference_data_tags.append(datafra[h][0]["tags"][k])
                                #INSERTO EL ARRAY DE TAGS PEQUENIO EN EL ARRAY GRANDE
                            else:
                                reference_data_tags.append(datafra[h][0]["tags"][k])
                                array_auxiliar=[]
                                for t in range(0,len(reference_data_tags)):
                                    elem=reference_data_tags.pop()
                                    array_auxiliar.insert(0,elem)
                                references_reference_data_tags.append(array_auxiliar)
                        
                #INSERTAMOS TAGS EN VALORES Y VACIAMOS EL ARRAY GRANDE
                index9 = columns.index("CVE_Items.cve.references.reference_data.tags")
                array_auxiliar_cuatro=[]
                for d in range(0,len(references_reference_data_tags)):
                    elem_cuatro=references_reference_data_tags.pop()
                    array_auxiliar_cuatro.insert(0,elem_cuatro)
                if(array_auxiliar_cuatro.count("null") == len(array_auxiliar_cuatro)):
                    if(values[index9]==None):
                        values.pop(index9)
                        values.insert(index9,"null") 
                else:
                    if(values[index9]==None):
                        values.pop(index9)
                        values.insert(index9,array_auxiliar_cuatro) 


                    
######################################################################################
###############################FUNCION PARA INSERTAR CONFIGURACION######################################
def insertar_configurations(datafra,fil,col):
    if isinstance(datafra, list):
        e=[]
        for j in range(0,len(datafra)):
            e.append(str(j))
        dataframe_list=dict(zip(e,datafra))
        dataframe_dict=pd.DataFrame.from_dict(dataframe_list,orient="index")
    if(fil>0):
        insertar_nodes_operator(dataframe_dict["operator"],fil)
        if(fil==1):
            if(len(dataframe_dict["children"][0])!=0):
                insertar_nodes_children(dataframe_dict["children"],fil)
            if(len(dataframe_dict["cpe_match"][0])!=0):
                insertar_nodes_cpe_match(dataframe_dict["cpe_match"],fil)

            #elif(len(dataframe_dict["cpe-match"][0])!=0):
                #insertar_nodes_cpe_match(dataframe_dict["cpe_match"],fil)
            #elif(len(dataframe_dict["cpe_match"][0])==0):

            #elif(len(dataframe_dict["children"][0])>0):

            #elif(len(dataframe_dict["cpe_match"][0])>0):
        else:
            insertar_nodes_children(dataframe_dict["children"],fil)
            insertar_nodes_cpe_match(dataframe_dict["cpe_match"],fil)
    

    
    
###############################FUNCION PARA INSERTAR LOS OPERADORES DE CONFIGURACION######################################
def insertar_nodes_operator(list_operator,lenfil):
    #SI SOLAMENTE HAY UN NODO INSERTO DIRECTAMENTE EL OPERADOR
    if(lenfil==1):
        index9 = columns.index("CVE_Items.configurations.nodes.operator")
        if(values[index9]==None):
            values.pop(index9)
            values.insert(index9,list_operator[0])
    #SI HAY MAS DE UN NODO RECORRO CADA NODO COGIENDO EL OPERADOR
    else:
        for g in range(0,lenfil):
            #SI NO HE RECORRIDO TODOS LOS NODOS INSERTO EN EL ARRAY DE OPERADORES
            if(g!=lenfil-1):
                #SI EL OPERADOR NO ES AND NI OR SIGNIFICA QUE NO EXISTE OPERADOR E INSERTO NULL
                if(len(list_operator[g])<2):
                    nodes_operator.append("null")
                #SI EL OPERADOR NO ES NULL LO INSERTO EN EL ARRAY DE OPERADORES
                else:
                    nodes_operator.append(list_operator[g])
                    
            #SI HE LLEGADO AL ULTIMO NODO
            else:
                #SI EL ULTIMO OPERADOR ES NULL, COMPRUEBO EL ANTEPENULTIMO
                if(len(list_operator[g])<2):
                    #COMO EL ULTIMO OPERADOR ES NULL INSERTO NULL
                    nodes_operator.append("null")
                    #COMPRUEBO SI EL ANTEPENULTIMO OPERADOR ES AND
                    if(list_operator[g-1] =="AND"):
                        #SI NO TODOS LOS OPERADORES SON AND INSERTO EN VALORES LA LISTA DE OPERADORES
                        if("OR" in nodes_operator):
                            #INSERTAMOS TAGS EN VALORES Y VACIAMOS EL ARRAY GRANDE
                            index = columns.index("CVE_Items.configurations.nodes.operator")
                            array_auxiliar=[]
                            for d in range(0,len(nodes_operator)):
                                elem=nodes_operator.pop()
                                array_auxiliar.insert(0,elem)
                            if(values[index]==None):
                                values.pop(index)
                                values.insert(index,array_auxiliar)
                        else:
                            #SI TODOS LOS OPERADORES SON AND INSERTO SOLAMENTE UN VALOR, NO EL ARRAY
                            index2 = columns.index("CVE_Items.configurations.nodes.operator")
                            for d in range(0,len(nodes_operator)):
                                nodes_operator.pop()
                            if(values[index2]==None):
                                values.pop(index2)
                                values.insert(index2,"AND")
                    else:
                        #COMPRUEBO SI TODOS LOS NODOS SON OR
                        #SI NO TODOS LOS NODOS SON OR INSERTO TODO EL ARRAY DE OPERADORES
                        if("AND" in nodes_operator):
                            #INSERTAMOS TAGS EN VALORES Y VACIAMOS EL ARRAY GRANDE
                            index3 = columns.index("CVE_Items.configurations.nodes.operator")
                            array_auxiliar3=[]
                            for d in range(0,len(nodes_operator)):
                                elem3=nodes_operator.pop()
                                array_auxiliar3.insert(0,elem3)
                            if(values[index3]==None):
                                values.pop(index3)
                                values.insert(index3,array_auxiliar3)
                        #SI TODOS LOS NODOS SON OR INSERTO SOLAMENTE EL VALOR OR, NO EL ARRAY DE OPERADORES
                        else:
                            index4 = columns.index("CVE_Items.configurations.nodes.operator")
                            for d in range(0,len(nodes_operator)):
                                nodes_operator.pop()
                            if(values[index4]==None):
                                values.pop(index4)
                                values.insert(index4,"OR")
                #SI EL ULTIMO OPERADOR NO ES NULO
                else:
                    #INSERTO EL ULTIMO OPERADOR
                    nodes_operator.append(list_operator[g])
                    #COMPRUEBO SI TODOS LOS NODOS SON AND
                    #SI NO TODOS LOS NODOS SON AND INSERTO TODO EL ARRAY DE OPERADORES
                    if(list_operator[g] =="AND"):
                        if("OR" in nodes_operator):
                            #INSERTAMOS TAGS EN VALORES Y VACIAMOS EL ARRAY GRANDE
                            index5 = columns.index("CVE_Items.configurations.nodes.operator")
                            array_auxiliar5=[]
                            for d in range(0,len(nodes_operator)):
                                elem5=nodes_operator.pop()
                                array_auxiliar5.insert(0,elem5)
                            if(values[index5]==None):
                                values.pop(index5)
                                values.insert(index5,array_auxiliar5)
                        #SI TODOS LOS NODOS SON AND SIMPLEMENTE INSERTO EL VALOR AND, NO EL ARRAY
                        else:
                            index6 = columns.index("CVE_Items.configurations.nodes.operator")
                            for d in range(0,len(nodes_operator)):
                                nodes_operator.pop()
                            if(values[index6]==None):
                                values.pop(index6)
                                values.insert(index6,"AND")
                                
                    #COMPRUEBO SI TODOS LOS NODOS SON OR
                    #SI NO TODOS LOS NODOS SON OR INSERTO TODO EL ARRAY DE OPERADORES
                    else:
                        if("AND" in nodes_operator):
                            #INSERTAMOS TAGS EN VALORES Y VACIAMOS EL ARRAY GRANDE
                            index7 = columns.index("CVE_Items.configurations.nodes.operator")
                            array_auxiliar7=[]
                            for d in range(0,len(nodes_operator)):
                                elem7=nodes_operator.pop()
                                array_auxiliar7.insert(0,elem7)
                            if(values[index7]==None):
                                values.pop(index7)
                                values.insert(index7,array_auxiliar7)
                        #SI TODOS LOS NODOS SON OR SIMPLEMENTE INSERTO EL VALOR OR, NO EL ARRAY DE OPERADORES
                        else:
                            index8 = columns.index("CVE_Items.configurations.nodes.operator")
                            for d in range(0,len(nodes_operator)):
                                nodes_operator.pop()
                            if(values[index8]==None):
                                values.pop(index8)
                                values.insert(index8,"OR")
                                
def insertar_cpe_match(inde,datafram,len_fil): 
    #SI AUN NO HE RECORRIDO TODOS LOS NODOS
    #print("INSERTAR CPE MATCH")
    if(inde!=len_fil-1):
        #SI EN ESTE NODO NO HAY CPE_MATCH O ESTA VACIO INSERTO NULL EN EL ARRAY GRANDE DE CPE_MATCH PARA VULNERABLE,CPE23,VERSIONENDINCLUDING Y CPENAME
        if(len(datafram)==0):
            #ARRAY PARA GUARDAR LOS VALORES DE LOS ARRAYS DE CPE_MATCH VULNERABLE DE TODOS LOS CHILDREN DE TODOS LOS NODOS,PUEDE SER NULL
            nodes_cpe_match_vulnerable.append("null")
            #ARRAY PARA GUARDAR LOS VALORES DE LOS ARRAYS DE CPE_MATCH CPE23URI DE TODOS LOS CHILDREN DE TODOS LOS NODOS,PUEDE SER NULL
            nodes_cpe_match_cpe23Uri.append("null")
            #ARRAY PARA GUARDAR LOS VALORES DE LOS ARRAYS DE CPE_MATCH VERSIONENDINCLUDING DE TODOS LOS CHILDREN DE TODOS LOS NODOS,PUEDE SER NULL
            nodes_cpe_match_versionEndIncluding.append("null")
        else:
            #print("else")
            #print(datafram)
            if("vulnerable" not in datafram.columns.values):
                #print("1")
                cpe_match_vulnerable.append("null")
            if("cpe23Uri" not in datafram.columns.values):
                #print("2")
                cpe_match_cpe23Uri.append("null")
            if("versionEndIncluding" not in datafram.columns.values):
                #print("3")
                cpe_match_versionEndIncluding.append("null")
            #VEO CUANTOS CPE_MATCH HAY EN CADA NODO
            for l in range(0,len(datafram)):
                if(l!=(len(datafram)-1)):
                    for h in range(0,len(datafram.columns.values)):
                        if(datafram.columns.values[h] == "vulnerable"):
                            #print("11")
                            #print(h)
                            if((datafram["vulnerable"][l] == True) or (datafram["vulnerable"][l] == False)):
                                cpe_match_vulnerable.append(datafram["vulnerable"][l])
                            else:
                                cpe_match_vulnerable.append("null")
                        elif(datafram.columns.values[h] == "cpe23Uri"): 
                            #print("22")
                            #print(h)
                            if(len(datafram["cpe23Uri"][l])>0):
                                 cpe_match_cpe23Uri.append(datafram["cpe23Uri"][l])
                            else:
                                cpe_match_cpe23Uri.append("null")
                        elif(datafram.columns.values[h] == "versionEndIncluding"):
                            #print("33")
                            #print(h)
                            if(datafram["versionEndIncluding"][l] is None):
                                cpe_match_versionEndIncluding.append("null")
                            else:
                                cpe_match_versionEndIncluding.append(datafram["versionEndIncluding"][l])
                else:
                    if("vulnerable" not in datafram.columns.values):
                        cpe_match_vulnerable.append("null")
                    if("cpe23Uri" not in datafram.columns.values):
                        cpe_match_cpe23Uri.append("null")
                    if("versionEndIncluding" not in datafram.columns.values):
                        cpe_match_versionEndIncluding.append("null")

                    for h in range(0,len(datafram.columns.values)):
                        if(datafram.columns.values[h] == "vulnerable"):
                            if((datafram["vulnerable"][l] == True) or (datafram["vulnerable"][l] == False)):
                                cpe_match_vulnerable.append(datafram["vulnerable"][l])
                            else:
                                cpe_match_vulnerable.append("null")
                        elif(datafram.columns.values[h] == "cpe23Uri"): 
                            if(len(datafram["cpe23Uri"][l])>0):
                                 cpe_match_cpe23Uri.append(datafram["cpe23Uri"][l])
                            else:
                                cpe_match_cpe23Uri.append("null")
                        elif(datafram.columns.values[h] == "versionEndIncluding"):
                            if(datafram["versionEndIncluding"][l] is None):
                                cpe_match_versionEndIncluding.append("null")
                            else:
                                cpe_match_versionEndIncluding.append(datafram["versionEndIncluding"][l])
                    array_aux1=[]
                    #INSERTO LANG
                    for k in range(0,len(cpe_match_vulnerable)):
                        elem1=cpe_match_vulnerable.pop()
                        array_aux1.insert(0,elem1)
                    if((False not in array_aux1) and (True not in array_aux1)):
                        nodes_cpe_match_vulnerable.append("null")
                    elif((False not in array_aux1) and (True in array_aux1)):
                        nodes_cpe_match_vulnerable.append(True)
                    elif((False in array_aux1) and (True not in array_aux1)):
                        nodes_cpe_match_vulnerable.append(False)
                    else:
                        nodes_cpe_match_vulnerable.append(array_aux1)
                    array_aux2=[]
                    #INSERTO LANG
                    for d in range(0,len(cpe_match_cpe23Uri)):
                        elem2=cpe_match_cpe23Uri.pop()
                        array_aux2.insert(0,elem2)
                    if(array_aux2.count("null") == len(array_aux2)):
                        nodes_cpe_match_cpe23Uri.append("null")
                    else:
                        nodes_cpe_match_cpe23Uri.append(array_aux2)

                    array_aux3=[]
                    #INSERTO LANG
                    for h in range(0,len(cpe_match_versionEndIncluding)):
                        elem3=cpe_match_versionEndIncluding.pop()
                        array_aux3.insert(0,elem3)
                    if(array_aux3.count("null") == len(array_aux3)):
                        nodes_cpe_match_versionEndIncluding.append("null")
                    else:
                        nodes_cpe_match_versionEndIncluding.append(array_aux3)
    else:
        #SI EN ESTE NODO NO HAY CPE_MATCH O ESTA VACIO INSERTO NULL EN EL ARRAY GRANDE DE CPE_MATCH PARA VULNERABLE,CPE23,VERSIONENDINCLUDING Y CPENAME
        if(len(datafram)==0):
            #ARRAY PARA GUARDAR LOS VALORES DE LOS ARRAYS DE CPE_MATCH VULNERABLE DE TODOS LOS CHILDREN DE TODOS LOS NODOS,PUEDE SER NULL
            nodes_cpe_match_vulnerable.append("null")
            #ARRAY PARA GUARDAR LOS VALORES DE LOS ARRAYS DE CPE_MATCH CPE23URI DE TODOS LOS CHILDREN DE TODOS LOS NODOS,PUEDE SER NULL
            nodes_cpe_match_cpe23Uri.append("null")
            #ARRAY PARA GUARDAR LOS VALORES DE LOS ARRAYS DE CPE_MATCH VERSIONENDINCLUDING DE TODOS LOS CHILDREN DE TODOS LOS NODOS,PUEDE SER NULL
            nodes_cpe_match_versionEndIncluding.append("null")
        else:
            #VEO CUANTOS CPE_MATCH HAY EN CADA NODO
            for l in range(0,len(datafram)):
                if(l!=(len(datafram)-1)):
                    if("vulnerable" not in datafram.columns.values):
                        cpe_match_vulnerable.append("null")
                    if("cpe23Uri" not in datafram.columns.values):
                        cpe_match_cpe23Uri.append("null")
                    if("versionEndIncluding" not in datafram.columns.values):
                        cpe_match_versionEndIncluding.append("null")

                    for h in range(0,len(datafram.columns.values)):
                        if(datafram.columns.values[h] == "vulnerable"):
                            if((datafram["vulnerable"][l] == True) or (datafram["vulnerable"][l] == False)):
                                cpe_match_vulnerable.append(datafram["vulnerable"][l])
                            else:
                                cpe_match_vulnerable.append("null")
                        elif(datafram.columns.values[h] == "cpe23Uri"): 
                            if(len(datafram["cpe23Uri"][l])>0):
                                 cpe_match_cpe23Uri.append(datafram["cpe23Uri"][l])
                            else:
                                cpe_match_cpe23Uri.append("null")
                        elif(datafram.columns.values[h] == "versionEndIncluding"):
                            if(datafram["versionEndIncluding"][l] is None):
                                cpe_match_versionEndIncluding.append("null")
                            else:
                                cpe_match_versionEndIncluding.append(datafram["versionEndIncluding"][l])
                else:
                    if("vulnerable" not in datafram.columns.values):
                        cpe_match_vulnerable.append("null")
                    if("cpe23Uri" not in datafram.columns.values):
                        cpe_match_cpe23Uri.append("null")
                    if("versionEndIncluding" not in datafram.columns.values):
                        cpe_match_versionEndIncluding.append("null")

                    for h in range(0,len(datafram.columns.values)):
                        if(datafram.columns.values[h] == "vulnerable"):
                            if((datafram["vulnerable"][l] == True) or (datafram["vulnerable"][l] == False)):
                                cpe_match_vulnerable.append(datafram["vulnerable"][l])
                            else:
                                cpe_match_vulnerable.append("null")
                        elif(datafram.columns.values[h] == "cpe23Uri"): 
                            if(len(datafram["cpe23Uri"][l])>0):
                                 cpe_match_cpe23Uri.append(datafram["cpe23Uri"][l])
                            else:
                                cpe_match_cpe23Uri.append("null")
                        elif(datafram.columns.values[h] == "versionEndIncluding"):
                            if(datafram["versionEndIncluding"][l] is None):
                                cpe_match_versionEndIncluding.append("null")
                            else:
                                cpe_match_versionEndIncluding.append(datafram["versionEndIncluding"][l])

                    array_aux1=[]
                    #INSERTO LANG
                    for k in range(0,len(cpe_match_vulnerable)):
                        elem1=cpe_match_vulnerable.pop()
                        array_aux1.insert(0,elem1)
                    if((False not in array_aux1) and (True not in array_aux1)):
                        nodes_cpe_match_vulnerable.append("null")
                    elif((False not in array_aux1) and (True in array_aux1)):
                        nodes_cpe_match_vulnerable.append(True)
                    elif((False in array_aux1) and (True not in array_aux1)):
                        nodes_cpe_match_vulnerable.append(False)
                    else:
                        nodes_cpe_match_vulnerable.append(array_aux1)

                    array_aux2=[]
                    #INSERTO LANG
                    for d in range(0,len(cpe_match_cpe23Uri)):
                        elem2=cpe_match_cpe23Uri.pop()
                        array_aux2.insert(0,elem2)
                    if(array_aux2.count("null") == len(array_aux2)):
                        nodes_cpe_match_cpe23Uri.append("null")
                    else:
                        nodes_cpe_match_cpe23Uri.append(array_aux2)

                    array_aux3=[]
                    #INSERTO LANG
                    for h in range(0,len(cpe_match_versionEndIncluding)):
                        elem3=cpe_match_versionEndIncluding.pop()
                        array_aux3.insert(0,elem3)
                    if(array_aux3.count("null") == len(array_aux3)):
                        nodes_cpe_match_versionEndIncluding.append("null")
                    else:
                        nodes_cpe_match_versionEndIncluding.append(array_aux3)
                   
                    
        #INSERTAMOS EL ARRAY DE OPERADORES DE LOS CHILDREN EN LOS VALORES
        index10 = columns.index("CVE_Items.configurations.nodes.cpe_match.vulnerable")
        array_auxiliar10=[]
        #print("VULNERABLEEEEEEEEE")
        if((len(datafram)==1) and (len(nodes_cpe_match_vulnerable) ==1)):
            elem10=nodes_cpe_match_vulnerable.pop()
            array_auxiliar10.insert(0,elem10)
            if(array_auxiliar10.count("null") == len(array_auxiliar10)):
                if(values[index10]==None):
                    values.pop(index10)
                    values.insert(index10,"null")
            elif(array_auxiliar10.count(True) == len(array_auxiliar10)):
                if(values[index10]==None):
                    values.pop(index10)
                    values.insert(index10,True)
            elif(array_auxiliar10.count(False) == len(array_auxiliar10)):
                if(values[index10]==None):
                    values.pop(index10)
                    values.insert(index10,False)
            else:
                if(values[index10]==None):
                    values.pop(index10)
                    values.insert(index10,array_auxiliar10[0][0])

        else:
            #print("AQUI VULNERABLE")
            #print(len(nodes_cpe_match_vulnerable))
            for a in range(0,len(nodes_cpe_match_vulnerable)):
                elem10=nodes_cpe_match_vulnerable.pop()
                array_auxiliar10.insert(0,elem10)
            if(array_auxiliar10.count("null") == len(array_auxiliar10)):
                if(values[index10]==None):
                    values.pop(index10)
                    values.insert(index10,"null")
            elif(array_auxiliar10.count(True) == len(array_auxiliar10)):
                if(values[index10]==None):
                    values.pop(index10)
                    values.insert(index10,True)
            elif(array_auxiliar10.count(False) == len(array_auxiliar10)):
                if(values[index10]==None):
                    values.pop(index10)
                    values.insert(index10,False)
            else:
                if(values[index10]==None):
                    values.pop(index10)
                    values.insert(index10,array_auxiliar10)



        #INSERTAMOS EL ARRAY DE OPERADORES DE LOS CHILDREN EN LOS VALORES
        index11 = columns.index("CVE_Items.configurations.nodes.cpe_match.cpe23Uri")
        array_auxiliar11=[]
        #print("CPE23URIIIIIIIII")
        if((len(datafram)==1) and (len(nodes_cpe_match_cpe23Uri) ==1)):
            elem11=nodes_cpe_match_cpe23Uri.pop()
            array_auxiliar11.insert(0,elem11)
            if(array_auxiliar11.count("null") == len(array_auxiliar11)):
                if(values[index11]==None):
                    values.pop(index11)
                    values.insert(index11,"null")
            else:
                if(values[index11]==None):
                    values.pop(index11)
                    values.insert(index11,array_auxiliar11[0][0])
        else:
            #print("no aqui")
            for z in range(0,len(nodes_cpe_match_cpe23Uri)):
                elem11=nodes_cpe_match_cpe23Uri.pop()
                array_auxiliar11.insert(0,elem11)
            if(array_auxiliar11.count("null") == len(array_auxiliar11)):
                if(values[index11]==None):
                    values.pop(index11)
                    values.insert(index11,"null")
            else:
                if(values[index11]==None):
                    values.pop(index11)
                    values.insert(index11,array_auxiliar11)



        #INSERTAMOS EL ARRAY DE OPERADORES DE LOS CHILDREN EN LOS VALORES
        index12 = columns.index("CVE_Items.configurations.nodes.cpe_match.versionEndIncluding")
        array_auxiliar12=[]
        #print("VERSIONENDINCLUDIIIIIIIIIIING")
        if((len(datafram)==1) and (len(nodes_cpe_match_versionEndIncluding) ==1)):
            elem12=nodes_cpe_match_versionEndIncluding.pop()
            array_auxiliar12.insert(0,elem12)
            if(array_auxiliar12.count("null") == len(array_auxiliar12)):
                if(values[index12]==None):
                    values.pop(index12)
                    values.insert(index12,"null")
            else:
                if(values[index12]==None):
                    values.pop(index12)
                    values.insert(index12,array_auxiliar12[0][0])

        else:           
            for q in range(0,len(nodes_cpe_match_versionEndIncluding)):
                elem12=nodes_cpe_match_versionEndIncluding.pop()
                array_auxiliar12.insert(0,elem12)
            if(array_auxiliar12.count("null") == len(array_auxiliar12)):
                if(values[index12]==None):
                    values.pop(index12)
                    values.insert(index12,"null")
            else:
                if(values[index12]==None):
                    values.pop(index12)
                    values.insert(index12,array_auxiliar12)

                        
        

def insertar_nodes_children_cpe_match(inde,datafram,len_fil):
    #print("INSERTAR NODEEEEEEEEEES CHILDREEEEEEEEEN")
    #print(inde)
    #print(datafram)
    #print(len_fil)
    #SI AUN NO HE RECORRIDO TODOS LOS NODOS
    if(inde!=len_fil-1):
        #SI EN ESTE NODO NO HAY CPE_MATCH O ESTA VACIO INSERTO NULL EN EL ARRAY GRANDE DE CPE_MATCH PARA VULNERABLE,CPE23,VERSIONENDINCLUDING Y CPENAME
        if((isinstance(datafram, str)) and (datafram=="null")):
            #ARRAY PARA GUARDAR LOS VALORES DE LOS ARRAYS DE CPE_MATCH VULNERABLE DE TODOS LOS CHILDREN DE TODOS LOS NODOS,PUEDE SER NULL
            nodes_children_cpe_match_vulnerable.append("null")
            #ARRAY PARA GUARDAR LOS VALORES DE LOS ARRAYS DE CPE_MATCH CPE23URI DE TODOS LOS CHILDREN DE TODOS LOS NODOS,PUEDE SER NULL
            nodes_children_cpe_match_cpe23Uri.append("null")
            #ARRAY PARA GUARDAR LOS VALORES DE LOS ARRAYS DE CPE_MATCH VERSIONENDINCLUDING DE TODOS LOS CHILDREN DE TODOS LOS NODOS,PUEDE SER NULL
            nodes_children_cpe_match_versionEndIncluding.append("null")
            #ARRAY PARA GUARDAR LOS VALORES DE LOS ARRAYS DE CPE_MATCH CPENAME DE TODOS LOS CHILDREN DE TODOS LOS NODOS,SUELE SER NULL
            nodes_children_cpe_match_cpename.append("null")
        else:
            #VEO CUANTOS CPE_MATCH HAY EN CADA NODO
            for l in range(0,len(datafram)):
                #ESTO ES EL NUMERO DE CHILDREN QUE HAY, AHORA HAY QUE INSERTAR LOS ARRAY DE CADA CHILDREN EN EL ARRAY DE NODOS
                ##print(len(datafram))
                ##print("len")
                ##print(l)
                if(l!=(len(datafram)-1)):
                    #Si uno de los children no tiene cpe_match
                    if(len(datafram[l])<1):
                        #ARRAY PARA GUARDAR LOS VALORES DE LOS ARRAYS DE CPE_MATCH VULNERABLE DE TODOS LOS CHILDREN DE CADA NODO,PUEDE SER NULL
                        children_cpe_match_vulnerable.append("null")
                        #ARRAY PARA GUARDAR LOS VALORES DE LOS ARRAYS DE CPE_MATCH CPE23URI DE TODOS LOS CHILDREN DE CADA NODO,PUEDE SER NULL
                        children_cpe_match_cpe23Uri.append("null")
                        #ARRAY PARA GUARDAR LOS VALORES DE LOS ARRAYS DE CPE_MATCH VERSIONENDINCLUDING DE TODOS LOS CHILDREN DE CADA NODO,PUEDE SER NULL
                        children_cpe_match_versionEndIncluding.append("null")
                        #ARRAY PARA GUARDAR LOS VALORES DE LOS ARRAYS DE CPE_MATCH CPENAME DE TODOS LOS CHILDREN DE CADA NODO,SUELE SER NULL
                        children_cpe_match_cpename.append("null")
                    #Si el children en el que estamos tiene uno o mas cpe_match
                    else:
                        for j in range(0,len(datafram[l])):
                            ##print("####################")
                            ##print(len(datafram[0][l]))
                            ##print(len(datafram[l]))
                            if(j!=(len(datafram[l])-1)):
                                ##print("//////////////////")
                                dataframe_dict_child=pd.DataFrame.from_dict(datafram[l][j],orient="index")
                                ##print(dataframe_dict_child.index.values)
                                if("vulnerable" not in dataframe_dict_child.index.values):
                                    cpe_match_vulnerable_children.append("null")

                                if("cpe23Uri" not in dataframe_dict_child.index.values):
                                    cpe_match_cpe23Uri_children.append("null")

                                if("versionEndIncluding" not in dataframe_dict_child.index.values):
                                    cpe_match_versionEndIncluding_children.append("null")

                                for r in range(0,len(dataframe_dict_child.index.values)):
                                    if(dataframe_dict_child.index.values[r] == "vulnerable"):
                                        if(((dataframe_dict_child[0]["vulnerable"]) == True) or ((dataframe_dict_child[0]["vulnerable"]) == False)):
                                            cpe_match_vulnerable_children.append(dataframe_dict_child[0]["vulnerable"])
                                        else:
                                            cpe_match_vulnerable_children.append("null")
                                    elif(dataframe_dict_child.index.values[r] == "cpe23Uri"): 
                                        if(len(dataframe_dict_child[0]["cpe23Uri"])>0):
                                             cpe_match_cpe23Uri_children.append(dataframe_dict_child[0]["cpe23Uri"])
                                        else:
                                            cpe_match_cpe23Uri_children.append("null")
                                    elif(dataframe_dict_child.index.values[r] == "versionEndIncluding"):
                                        if(len(dataframe_dict_child[0]["versionEndIncluding"])>0):
                                            cpe_match_versionEndIncluding_children.append(dataframe_dict_child[0]["versionEndIncluding"])
                                        else:
                                            cpe_match_versionEndIncluding_children.append("null")

                            else:
                                dataframe_dict_child=pd.DataFrame.from_dict(datafram[l][j],orient="index")
                                ##print(dataframe_dict_child.index.values)
                                ##print("¨¨¨¨¨¨")
                                if(("vulnerable") not in (dataframe_dict_child.index.values)):
                                    cpe_match_vulnerable_children.append("null")

                                if(("cpe23Uri") not in (dataframe_dict_child.index.values)):
                                    cpe_match_cpe23Uri_children.append("null")

                                if(("versionEndIncluding") not in (dataframe_dict_child.index.values)):
                                    cpe_match_versionEndIncluding_children.append("null")
                                for r in range(0,len(dataframe_dict_child.index.values)):
                                    if(dataframe_dict_child.index.values[r] == "vulnerable"):
                                        ##print("*")
                                        ##print(dataframe_dict_child[j][r] =='True')
                                        ##print(dataframe_dict_child[j][r])
                                        if((dataframe_dict_child[0][r] ==True) or (dataframe_dict_child[0][r] ==False) ):
                                            ##print("entro vulnerable")
                                            cpe_match_vulnerable_children.append(dataframe_dict_child[0][r])
                                        else:
                                            cpe_match_vulnerable_children.append("null")
                                    elif(dataframe_dict_child.index.values[r] == "cpe23Uri"): 
                                        ##print("cpe23Uri")
                                        if(len(dataframe_dict_child[0][r])>0):
                                            ##print("entro cpe23uri")
                                            cpe_match_cpe23Uri_children.append(dataframe_dict_child[0][r])
                                        else:
                                            cpe_match_cpe23Uri_children.append("null")
                                    elif(dataframe_dict_child.index.values[r] == "versionEndIncluding"):
                                        ##print("VERSIONENDINCLUDING")
                                        if(len(dataframe_dict_child[0][r])>0):
                                            cpe_match_versionEndIncluding_children.append(dataframe_dict_child[0][r])
                                        else:
                                            cpe_match_versionEndIncluding_children.append("null")
                                array_aux1=[]
                                #INSERTO LANG
                                for k in range(0,len(cpe_match_vulnerable_children)):
                                    elem1=cpe_match_vulnerable_children.pop()
                                    array_aux1.insert(0,elem1)
                                if((False not in array_aux1) and (True not in array_aux1)):
                                    children_cpe_match_vulnerable.append("null")
                                elif((False not in array_aux1) and (True in array_aux1)):
                                    children_cpe_match_vulnerable.append(True)
                                elif((False in array_aux1) and (True not in array_aux1)):
                                    children_cpe_match_vulnerable.append(False)
                                else:
                                    children_cpe_match_vulnerable.append(array_aux1)
                                array_aux2=[]
                                #INSERTO LANG
                                for d in range(0,len(cpe_match_cpe23Uri_children)):
                                    elem2=cpe_match_cpe23Uri_children.pop()
                                    array_aux2.insert(0,elem2)
                                if(array_aux2.count("null") == len(array_aux2)):
                                    children_cpe_match_cpe23Uri.append("null")
                                else:
                                    children_cpe_match_cpe23Uri.append(array_aux2)
                                array_aux3=[]
                                #INSERTO LANG
                                for h in range(0,len(cpe_match_versionEndIncluding_children)):
                                    elem3=cpe_match_versionEndIncluding_children.pop()
                                    array_aux3.insert(0,elem3)
                                ##print("%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&")
                                ##print("AQUI")
                                ##print(array_aux3.count("null") == len(array_aux3))
                                ##print(len(array_aux3))
                                if(array_aux3.count("null") == len(array_aux3)):
                                    children_cpe_match_versionEndIncluding.append("null")
                                else:
                                    children_cpe_match_versionEndIncluding.append(array_aux3)
                                

                                #HE ACABADO DE INSERTAR EN EL ARRAY DE CADA CHILDREN LOS VALORES DE CADA CPE MATCH, EL ARRAY PEQUEÑO EN EL ARRAY GRANDE
                else:
                    #Si uno de los children no tiene cpe_match
                    if(len(datafram[l])<1):
                        #ARRAY PARA GUARDAR LOS VALORES DE LOS ARRAYS DE CPE_MATCH VULNERABLE DE TODOS LOS CHILDREN DE CADA NODO,PUEDE SER NULL
                        children_cpe_match_vulnerable.append("null")
                        #ARRAY PARA GUARDAR LOS VALORES DE LOS ARRAYS DE CPE_MATCH CPE23URI DE TODOS LOS CHILDREN DE CADA NODO,PUEDE SER NULL
                        children_cpe_match_cpe23Uri.append("null")
                        #ARRAY PARA GUARDAR LOS VALORES DE LOS ARRAYS DE CPE_MATCH VERSIONENDINCLUDING DE TODOS LOS CHILDREN DE CADA NODO,PUEDE SER NULL
                        children_cpe_match_versionEndIncluding.append("null")
                        #ARRAY PARA GUARDAR LOS VALORES DE LOS ARRAYS DE CPE_MATCH CPENAME DE TODOS LOS CHILDREN DE CADA NODO,SUELE SER NULL
                        children_cpe_match_cpename.append("null")
                    #Si el children en el que estamos tiene uno o mas cpe_match
                    else:
                        for j in range(0,len(datafram[l])):
                            if(j!=(len(datafram[l])-1)):
                                ##print("//////////////////")
                                dataframe_dict_child=pd.DataFrame.from_dict(datafram[l][j],orient="index")
                                ##print(dataframe_dict_child.index.values)
                                if("vulnerable" not in dataframe_dict_child.index.values):
                                    cpe_match_vulnerable_children.append("null")

                                if("cpe23Uri" not in dataframe_dict_child.index.values):
                                    cpe_match_cpe23Uri_children.append("null")

                                if("versionEndIncluding" not in dataframe_dict_child.index.values):
                                    cpe_match_versionEndIncluding_children.append("null")

                                for r in range(0,len(dataframe_dict_child.index.values)):
                                    if(dataframe_dict_child.index.values[r] == "vulnerable"):
                                        if(((dataframe_dict_child[0]["vulnerable"]) == True) or ((dataframe_dict_child[0]["vulnerable"]) == False)):
                                            cpe_match_vulnerable_children.append(dataframe_dict_child[0]["vulnerable"])
                                        else:
                                            cpe_match_vulnerable_children.append("null")
                                    elif(dataframe_dict_child.index.values[r] == "cpe23Uri"): 
                                        if(len(dataframe_dict_child[0]["cpe23Uri"])>0):
                                             cpe_match_cpe23Uri_children.append(dataframe_dict_child[0]["cpe23Uri"])
                                        else:
                                            cpe_match_cpe23Uri_children.append("null")
                                    elif(dataframe_dict_child.index.values[r] == "versionEndIncluding"):
                                        if(len(dataframe_dict_child[0]["versionEndIncluding"])>0):
                                            cpe_match_versionEndIncluding_children.append(dataframe_dict_child[0]["versionEndIncluding"])
                                        else:
                                            cpe_match_versionEndIncluding_children.append("null")

                            else:
                                dataframe_dict_child=pd.DataFrame.from_dict(datafram[l][j],orient="index")
                                ##print(dataframe_dict_child.index.values)
                                if("vulnerable" not in dataframe_dict_child.index.values):
                                    cpe_match_vulnerable_children.append("null")

                                if("cpe23Uri" not in dataframe_dict_child.index.values):
                                    cpe_match_cpe23Uri_children.append("null")

                                if("versionEndIncluding" not in dataframe_dict_child.index.values):
                                    cpe_match_versionEndIncluding_children.append("null")

                                for r in range(0,len(dataframe_dict_child.index.values)):
                                    if(dataframe_dict_child.index.values[r] == "vulnerable"):
                                        if((dataframe_dict_child[0]["vulnerable"] ==True) or (dataframe_dict_child[0]["vulnerable"] ==False) ):
                                            cpe_match_vulnerable_children.append(dataframe_dict_child[0]["vulnerable"])
                                        else:
                                            cpe_match_vulnerable_children.append("null")
                                    elif(dataframe_dict_child.index.values[r] == "cpe23Uri"): 
                                        if(len(dataframe_dict_child[0]["cpe23Uri"])>0):
                                             cpe_match_cpe23Uri_children.append(dataframe_dict_child[0]["cpe23Uri"])
                                        else:
                                            cpe_match_cpe23Uri_children.append("null")
                                    elif(dataframe_dict_child.index.values[r] == "versionEndIncluding"):
                                        if(len(dataframe_dict_child[0]["versionEndIncluding"])>0):
                                            cpe_match_versionEndIncluding_children.append(dataframe_dict_child[0]["versionEndIncluding"])
                                        else:
                                            cpe_match_versionEndIncluding_children.append("null")
                                array_aux1=[]
                                #INSERTO LANG
                                for k in range(0,len(cpe_match_vulnerable_children)):
                                    elem1=cpe_match_vulnerable_children.pop()
                                    array_aux1.insert(0,elem1)
                                
                                if((False not in array_aux1) and (True not in array_aux1)):
                                    children_cpe_match_vulnerable.append("null")
                                elif((False not in array_aux1) and (True in array_aux1)):
                                    children_cpe_match_vulnerable.append(True)
                                elif((False in array_aux1) and (True not in array_aux1)):
                                    children_cpe_match_vulnerable.append(False)
                                else:
                                    children_cpe_match_vulnerable.append(array_aux1)
                                array_aux2=[]
                                #INSERTO LANG
                                for d in range(0,len(cpe_match_cpe23Uri_children)):
                                    elem2=cpe_match_cpe23Uri_children.pop()
                                    array_aux2.insert(0,elem2)
                                if(array_aux2.count("null") == len(array_aux2)):
                                    children_cpe_match_cpe23Uri.append("null")
                                else:
                                    children_cpe_match_cpe23Uri.append(array_aux2)
                                array_aux3=[]
                                #INSERTO LANG
                                for h in range(0,len(cpe_match_versionEndIncluding_children)):
                                    elem3=cpe_match_versionEndIncluding_children.pop()
                                    array_aux3.insert(0,elem3)
                                if(array_aux3.count("null") == len(array_aux3)):
                                    children_cpe_match_versionEndIncluding.append("null")
                                else:
                                    children_cpe_match_versionEndIncluding.append(array_aux3)

                                #HE ACABADO DE INSERTAR EN EL ARRAY DE CADA CHILDREN LOS VALORES DE CADA CPE MATCH, EL ARRAY PEQUEÑO EN EL ARRAY GRANDE
                    #ARRAY PARA GUARDAR LOS VALORES DE LOS ARRAYS DE CPE_MATCH VULNERABLE DE TODOS LOS CHILDREN DE TODOS LOS NODOS,PUEDE SER NULL
                    array_aux7=[]
                    for b in range(0,len(children_cpe_match_vulnerable)):
                        elem7=children_cpe_match_vulnerable.pop()
                        array_aux7.insert(0,elem7)
                    if((False not in array_aux7) and (True not in array_aux7)):
                        nodes_children_cpe_match_vulnerable.append("null")
                    elif((False not in array_aux7) and (True in array_aux7)):
                        nodes_children_cpe_match_vulnerable.append(True)
                    elif((False in array_aux7) and (True not in array_aux7)):
                        nodes_children_cpe_match_vulnerable.append(False)
                    else:
                        nodes_children_cpe_match_vulnerable.append(array_aux7)
                        #print(nodes_children_cpe_match_vulnerable)
                   
                    #ARRAY PARA GUARDAR LOS VALORES DE LOS ARRAYS DE CPE_MATCH CPE23URI DE TODOS LOS CHILDREN DE TODOS LOS NODOS,PUEDE SER NULL
                    array_aux8=[]
                    for c in range(0,len(children_cpe_match_cpe23Uri)):
                        elem8=children_cpe_match_cpe23Uri.pop()
                        array_aux8.insert(0,elem8)
                    nodes_children_cpe_match_cpe23Uri.append(array_aux8)
                    
                    array_aux9=[]
                    for v in range(0,len(children_cpe_match_versionEndIncluding)):
                        elem9=children_cpe_match_versionEndIncluding.pop()
                        array_aux9.insert(0,elem9)
                    if(array_aux9.count("null") == len(array_aux9)):
                        nodes_children_cpe_match_versionEndIncluding.append("null")
                    else:
                        nodes_children_cpe_match_versionEndIncluding.append(array_aux9)
                    
    else:
        #print("ELSEEEEE")
        #print(inde)
        #SI EN ESTE NODO NO HAY CPE_MATCH O ESTA VACIO INSERTO NULL EN EL ARRAY GRANDE DE CPE_MATCH PARA VULNERABLE,CPE23,VERSIONENDINCLUDING Y CPENAME
        if((isinstance(datafram, str)) and (datafram=="null")):
            #ARRAY PARA GUARDAR LOS VALORES DE LOS ARRAYS DE CPE_MATCH VULNERABLE DE TODOS LOS CHILDREN DE TODOS LOS NODOS,PUEDE SER NULL
            nodes_children_cpe_match_vulnerable.append("null")
            #ARRAY PARA GUARDAR LOS VALORES DE LOS ARRAYS DE CPE_MATCH CPE23URI DE TODOS LOS CHILDREN DE TODOS LOS NODOS,PUEDE SER NULL
            nodes_children_cpe_match_cpe23Uri.append("null")
            #ARRAY PARA GUARDAR LOS VALORES DE LOS ARRAYS DE CPE_MATCH VERSIONENDINCLUDING DE TODOS LOS CHILDREN DE TODOS LOS NODOS,PUEDE SER NULL
            nodes_children_cpe_match_versionEndIncluding.append("null")
            #ARRAY PARA GUARDAR LOS VALORES DE LOS ARRAYS DE CPE_MATCH CPENAME DE TODOS LOS CHILDREN DE TODOS LOS NODOS,SUELE SER NULL
            nodes_children_cpe_match_cpename.append("null")
        else:
            #VEO CUANTOS CPE_MATCH HAY EN CADA NODO
            for l in range(0,len(datafram)):
                #ESTO ES EL NUMERO DE CHILDREN QUE HAY, AHORA HAY QUE INSERTAR LOS ARRAY DE CADA CHILDREN EN EL ARRAY DE NODOS
                ##print(len(datafram))
                ##print("len")
                ##print(l)
                if(l!=(len(datafram)-1)):
                    #Si uno de los children no tiene cpe_match
                    if(len(datafram[l])<1):
                        #ARRAY PARA GUARDAR LOS VALORES DE LOS ARRAYS DE CPE_MATCH VULNERABLE DE TODOS LOS CHILDREN DE CADA NODO,PUEDE SER NULL
                        children_cpe_match_vulnerable.append("null")
                        #ARRAY PARA GUARDAR LOS VALORES DE LOS ARRAYS DE CPE_MATCH CPE23URI DE TODOS LOS CHILDREN DE CADA NODO,PUEDE SER NULL
                        children_cpe_match_cpe23Uri.append("null")
                        #ARRAY PARA GUARDAR LOS VALORES DE LOS ARRAYS DE CPE_MATCH VERSIONENDINCLUDING DE TODOS LOS CHILDREN DE CADA NODO,PUEDE SER NULL
                        children_cpe_match_versionEndIncluding.append("null")
                        #ARRAY PARA GUARDAR LOS VALORES DE LOS ARRAYS DE CPE_MATCH CPENAME DE TODOS LOS CHILDREN DE CADA NODO,SUELE SER NULL
                        children_cpe_match_cpename.append("null")
                    #Si el children en el que estamos tiene uno o mas cpe_match
                    else:
                        for j in range(0,len(datafram[l])):
                            if(j!=(len(datafram[l])-1)):
                                dataframe_dict_child=pd.DataFrame.from_dict(datafram[l][j],orient="index")
                                if("vulnerable" not in dataframe_dict_child.index.values):
                                    cpe_match_vulnerable_children.append("null")

                                if("cpe23Uri" not in dataframe_dict_child.index.values):
                                    cpe_match_cpe23Uri_children.append("null")

                                if("versionEndIncluding" not in dataframe_dict_child.index.values):
                                    cpe_match_versionEndIncluding_children.append("null")

                                for r in range(0,len(dataframe_dict_child.index.values)):
                                    if(dataframe_dict_child.index.values[r] == "vulnerable"):
                                        if(((dataframe_dict_child[0]["vulnerable"]) == True) or ((dataframe_dict_child[0]["vulnerable"]) == False)):
                                            cpe_match_vulnerable_children.append(dataframe_dict_child[0]["vulnerable"])
                                        else:
                                            cpe_match_vulnerable_children.append("null")
                                    elif(dataframe_dict_child.index.values[r] == "cpe23Uri"): 
                                        if(len(dataframe_dict_child[0]["cpe23Uri"])>0):
                                             cpe_match_cpe23Uri_children.append(dataframe_dict_child[0]["cpe23Uri"])
                                        else:
                                            cpe_match_cpe23Uri_children.append("null")
                                    elif(dataframe_dict_child.index.values[r] == "versionEndIncluding"):
                                        if(len(dataframe_dict_child[0]["versionEndIncluding"])>0):
                                            cpe_match_versionEndIncluding_children.append(dataframe_dict_child[0]["versionEndIncluding"])
                                        else:
                                            cpe_match_versionEndIncluding_children.append("null")

                            else:
                                dataframe_dict_child=pd.DataFrame.from_dict(datafram[l][j],orient="index")
                                #print(dataframe_dict_child.index.values)
                                if("vulnerable" not in dataframe_dict_child.index.values):
                                    cpe_match_vulnerable_children.append("null")

                                if("cpe23Uri" not in dataframe_dict_child.index.values):
                                    cpe_match_cpe23Uri_children.append("null")

                                if("versionEndIncluding" not in dataframe_dict_child.index.values):
                                    cpe_match_versionEndIncluding_children.append("null")

                                for r in range(0,len(dataframe_dict_child.index.values)):
                                    if(dataframe_dict_child.index.values[r] == "vulnerable"):
                                        if((dataframe_dict_child[0]["vulnerable"] ==True) or (dataframe_dict_child[0]["vulnerable"] ==False) ):
                                            cpe_match_vulnerable_children.append(dataframe_dict_child[0]["vulnerable"])
                                        else:
                                            cpe_match_vulnerable_children.append("null")
                                    elif(dataframe_dict_child.index.values[r] == "cpe23Uri"): 
                                        if(len(dataframe_dict_child[0]["cpe23Uri"])>0):
                                             cpe_match_cpe23Uri_children.append(dataframe_dict_child[0]["cpe23Uri"])
                                        else:
                                            cpe_match_cpe23Uri_children.append("null")
                                    elif(dataframe_dict_child.index.values[r] == "versionEndIncluding"):
                                        if(len(dataframe_dict_child[0]["versionEndIncluding"])>0):
                                            cpe_match_versionEndIncluding_children.append(dataframe_dict_child[0]["versionEndIncluding"])
                                        else:
                                            cpe_match_versionEndIncluding_children.append("null")
                                array_aux1=[]
                                #INSERTO LANG
                                for k in range(0,len(cpe_match_vulnerable_children)):
                                    elem1=cpe_match_vulnerable_children.pop()
                                    array_aux1.insert(0,elem1)
                                if((False not in array_aux1) and (True not in array_aux1)):
                                    children_cpe_match_vulnerable.append("null")
                                elif((False not in array_aux1) and (True in array_aux1)):
                                    children_cpe_match_vulnerable.append(True)
                                elif((False in array_aux1) and (True not in array_aux1)):
                                    children_cpe_match_vulnerable.append(False)
                                else:
                                    children_cpe_match_vulnerable.append(array_aux1)

                                array_aux2=[]
                                #INSERTO LANG
                                for d in range(0,len(cpe_match_cpe23Uri_children)):
                                    elem2=cpe_match_cpe23Uri_children.pop()
                                    array_aux2.insert(0,elem2)
                                children_cpe_match_cpe23Uri.append(array_aux2)

                                array_aux3=[]
                                #INSERTO LANG
                                for h in range(0,len(cpe_match_versionEndIncluding_children)):
                                    elem3=cpe_match_versionEndIncluding_children.pop()
                                    array_aux3.insert(0,elem3)
                                if(array_aux3.count("null") == len(array_aux3)):
                                    children_cpe_match_versionEndIncluding.append("null")
                                else:
                                    children_cpe_match_versionEndIncluding.append(array_aux3)

                                #HE ACABADO DE INSERTAR EN EL ARRAY DE CADA CHILDREN LOS VALORES DE CADA CPE MATCH, EL ARRAY PEQUEÑO EN EL ARRAY GRANDE
                else:
                    #Si uno de los children no tiene cpe_match
                    if(len(datafram[l])<1):
                        #ARRAY PARA GUARDAR LOS VALORES DE LOS ARRAYS DE CPE_MATCH VULNERABLE DE TODOS LOS CHILDREN DE CADA NODO,PUEDE SER NULL
                        children_cpe_match_vulnerable.append("null")
                        #ARRAY PARA GUARDAR LOS VALORES DE LOS ARRAYS DE CPE_MATCH CPE23URI DE TODOS LOS CHILDREN DE CADA NODO,PUEDE SER NULL
                        children_cpe_match_cpe23Uri.append("null")
                        #ARRAY PARA GUARDAR LOS VALORES DE LOS ARRAYS DE CPE_MATCH VERSIONENDINCLUDING DE TODOS LOS CHILDREN DE CADA NODO,PUEDE SER NULL
                        children_cpe_match_versionEndIncluding.append("null")
                        #ARRAY PARA GUARDAR LOS VALORES DE LOS ARRAYS DE CPE_MATCH CPENAME DE TODOS LOS CHILDREN DE CADA NODO,SUELE SER NULL
                        children_cpe_match_cpename.append("null")
                    #Si el children en el que estamos tiene uno o mas cpe_match
                    else:
                        for j in range(0,len(datafram[l])):
                            if(j!=(len(datafram[l])-1)):
                                #print("//////////////////")
                                dataframe_dict_child=pd.DataFrame.from_dict(datafram[l][j],orient="index")
                                ##print(dataframe_dict_child.index.values)
                                if("vulnerable" not in dataframe_dict_child.index.values):
                                    cpe_match_vulnerable_children.append("null")

                                if("cpe23Uri" not in dataframe_dict_child.index.values):
                                    cpe_match_cpe23Uri_children.append("null")

                                if("versionEndIncluding" not in dataframe_dict_child.index.values):
                                    cpe_match_versionEndIncluding_children.append("null")

                                for r in range(0,len(dataframe_dict_child.index.values)):
                                    if(dataframe_dict_child.index.values[r] == "vulnerable"):
                                        if(((dataframe_dict_child[0]["vulnerable"]) == True) or ((dataframe_dict_child[0]["vulnerable"]) == False)):
                                            cpe_match_vulnerable_children.append(dataframe_dict_child[0]["vulnerable"])
                                        else:
                                            cpe_match_vulnerable_children.append("null")
                                    elif(dataframe_dict_child.index.values[r] == "cpe23Uri"): 
                                        if(len(dataframe_dict_child[0]["cpe23Uri"])>0):
                                             cpe_match_cpe23Uri_children.append(dataframe_dict_child[0]["cpe23Uri"])
                                        else:
                                            cpe_match_cpe23Uri_children.append("null")
                                    elif(dataframe_dict_child.index.values[r] == "versionEndIncluding"):
                                        if(len(dataframe_dict_child[0]["versionEndIncluding"])>0):
                                            cpe_match_versionEndIncluding_children.append(dataframe_dict_child[0]["versionEndIncluding"])
                                        else:
                                            cpe_match_versionEndIncluding_children.append("null")

                            else:
                                dataframe_dict_child=pd.DataFrame.from_dict(datafram[l][j],orient="index")
                                #print(dataframe_dict_child.index.values)
                                if("vulnerable" not in dataframe_dict_child.index.values):
                                    cpe_match_vulnerable_children.append("null")

                                if("cpe23Uri" not in dataframe_dict_child.index.values):
                                    cpe_match_cpe23Uri_children.append("null")

                                if("versionEndIncluding" not in dataframe_dict_child.index.values):
                                    cpe_match_versionEndIncluding_children.append("null")

                                for r in range(0,len(dataframe_dict_child.index.values)):
                                    if(dataframe_dict_child.index.values[r] == "vulnerable"):
                                        if((dataframe_dict_child[0]["vulnerable"] ==True) or (dataframe_dict_child[0]["vulnerable"] ==False) ):
                                            cpe_match_vulnerable_children.append(dataframe_dict_child[0]["vulnerable"])
                                        else:
                                            cpe_match_vulnerable_children.append("null")
                                    elif(dataframe_dict_child.index.values[r] == "cpe23Uri"): 
                                        if(len(dataframe_dict_child[0]["cpe23Uri"])>0):
                                             cpe_match_cpe23Uri_children.append(dataframe_dict_child[0]["cpe23Uri"])
                                        else:
                                            cpe_match_cpe23Uri_children.append("null")
                                    elif(dataframe_dict_child.index.values[r] == "versionEndIncluding"):
                                        if(len(dataframe_dict_child[0]["versionEndIncluding"])>0):
                                            cpe_match_versionEndIncluding_children.append(dataframe_dict_child[0]["versionEndIncluding"])
                                        else:
                                            cpe_match_versionEndIncluding_children.append("null")
                                array_aux1=[]
                                #INSERTO LANG
                                for k in range(0,len(cpe_match_vulnerable_children)):
                                    elem1=cpe_match_vulnerable_children.pop()
                                    array_aux1.insert(0,elem1)
                                if((False not in array_aux1) and (True not in array_aux1)):
                                    children_cpe_match_vulnerable.append("null")
                                elif((False not in array_aux1) and (True in array_aux1)):
                                    children_cpe_match_vulnerable.append(True)
                                elif((False in array_aux1) and (True not in array_aux1)):
                                    children_cpe_match_vulnerable.append(False)
                                else:
                                    children_cpe_match_vulnerable.append(array_aux1)

                                array_aux2=[]
                                #INSERTO LANG
                                for d in range(0,len(cpe_match_cpe23Uri_children)):
                                    elem2=cpe_match_cpe23Uri_children.pop()
                                    #ME QUEDO AQUI, TENGO QUE CAMBIAR EN TODOS INSERT(0,ELEM2), POR INSERT(insert(len(cpe_match_vulnerable_children)-1-k,elem1))
                                    array_aux2.insert(0,elem2)
                                    #print(array_aux2)
                                children_cpe_match_cpe23Uri.append(array_aux2)

                                array_aux3=[]
                                #INSERTO LANG
                                for h in range(0,len(cpe_match_versionEndIncluding_children)):
                                    elem3=cpe_match_versionEndIncluding_children.pop()
                                    array_aux3.insert(0,elem3)
                                if(array_aux3.count("null") == len(array_aux3)):
                                    children_cpe_match_versionEndIncluding.append("null")
                                else:
                                    children_cpe_match_versionEndIncluding.append(array_aux3)

                                #HE ACABADO DE INSERTAR EN EL ARRAY DE CADA CHILDREN LOS VALORES DE CADA CPE MATCH, EL ARRAY PEQUEÑO EN EL ARRAY GRANDE
                    #ARRAY PARA GUARDAR LOS VALORES DE LOS ARRAYS DE CPE_MATCH VULNERABLE DE TODOS LOS CHILDREN DE TODOS LOS NODOS,PUEDE SER NULL
                    array_aux7=[]
                    for b in range(0,len(children_cpe_match_vulnerable)):
                        elem7=children_cpe_match_vulnerable.pop()
                        array_aux7.insert(0,elem7)
                    if((False not in array_aux7) and (True not in array_aux7)):
                        nodes_children_cpe_match_vulnerable.append("null")
                    elif((False not in array_aux7) and (True in array_aux7)):
                        nodes_children_cpe_match_vulnerable.append(True)
                    elif((False in array_aux7) and (True not in array_aux7)):
                        nodes_children_cpe_match_vulnerable.append(False)
                    else:
                        nodes_children_cpe_match_vulnerable.append(array_aux7)
                   
                    #ARRAY PARA GUARDAR LOS VALORES DE LOS ARRAYS DE CPE_MATCH CPE23URI DE TODOS LOS CHILDREN DE TODOS LOS NODOS,PUEDE SER NULL
                    array_aux8=[]
                    for c in range(0,len(children_cpe_match_cpe23Uri)):
                        elem8=children_cpe_match_cpe23Uri.pop()
                        array_aux8.insert(0,elem8)
                    nodes_children_cpe_match_cpe23Uri.append(array_aux8)
                    
                    array_aux9=[]
                    for v in range(0,len(children_cpe_match_versionEndIncluding)):
                        elem9=children_cpe_match_versionEndIncluding.pop()
                        array_aux9.insert(0,elem9)
                    if(array_aux9.count("null") == len(array_aux9)):
                        nodes_children_cpe_match_versionEndIncluding.append("null")
                    else:
                        nodes_children_cpe_match_versionEndIncluding.append(array_aux9)
                    
                    
                    
                    
        #INSERTAMOS EL ARRAY DE OPERADORES DE LOS CHILDREN EN LOS VALORES
        index10 = columns.index("CVE_Items.configurations.nodes.children.cpe_match.vulnerable")
        array_auxiliar10=[]
        for a in range(0,len(nodes_children_cpe_match_vulnerable)):
            elem10=nodes_children_cpe_match_vulnerable.pop()
            array_auxiliar10.insert(0,elem10)
        if(array_auxiliar10.count("null") == len(array_auxiliar10)):
            if(values[index10]==None):
                values.pop(index10)
                values.insert(index10,"null")
        else:
            if(values[index10]==None):
                values.pop(index10)
                values.insert(index10,array_auxiliar10)



        #INSERTAMOS EL ARRAY DE OPERADORES DE LOS CHILDREN EN LOS VALORES
        index11 = columns.index("CVE_Items.configurations.nodes.children.cpe_match.cpe23Uri")
        array_auxiliar11=[]
        for z in range(0,len(nodes_children_cpe_match_cpe23Uri)):
            elem11=nodes_children_cpe_match_cpe23Uri.pop()
            array_auxiliar11.insert(0,elem11)
        if(array_auxiliar11.count("null") == len(array_auxiliar11)):
            if(values[index11]==None):
                values.pop(index11)
                values.insert(index11,"null")
        else:
            if(values[index11]==None):
                values.pop(index11)
                values.insert(index11,array_auxiliar11)


        #INSERTAMOS EL ARRAY DE OPERADORES DE LOS CHILDREN EN LOS VALORES
        index12 = columns.index("CVE_Items.configurations.nodes.children.cpe_match.versionEndIncluding")
        array_auxiliar12=[]
        for q in range(0,len(nodes_children_cpe_match_versionEndIncluding)):
            elem12=nodes_children_cpe_match_versionEndIncluding.pop()
            array_auxiliar12.insert(0,elem12)
        if(array_auxiliar12.count("null") == len(array_auxiliar12)):
            if(values[index12]==None):
                values.pop(index12)
                values.insert(index12,"null")
        else:
            if(values[index12]==None):
                values.pop(index12)
                values.insert(index12,array_auxiliar12)


        #HAY QUE COMENTAR TODO, HE INSERTADO LOS VALORES DE CPE_MATCH DE TODOS LOS CHILDREN EN LOS NODOS CORRESPONDIENTES, COMPROBAR



                                    
def insertar_nodes_children_operator(ind,datafr, fila_len):
    #SI AUN NO HE RECORRIDO TODOS LOS NODOS
            if(ind!=fila_len-1):
                #SI EN ESTE NODO NO HAY OPERADOR O ESTA VACIO INSERTO NULL EN EL ARRAY GRANDE DE OPERADORES
                if((isinstance(datafr, str)) and (datafr=="null")):
                    nodes_children_operator.append("null")
                    
                #SI EN ESTE NODO SI QUE HAY OPERADORES
                else:
                    #VEO CUANTOS OPERADORES HAY EN CADA NODO
                    for l in range(0,len(datafr)):
                        #SI AUN NO HE RECORRIDO TODOS LOS OPERADORES DE ESTE NODO
                        if(l!=(len(datafr)-1)):
                            #SI EL ACTUAL OPERADOR ESTA VACIO O NO EXISTE INSERTO NULL EN EL ARRAY PEQUEÑO
                            if(len(datafr[l])<2):
                                children_operator.append("null")
                            #SI EL ACTUAL NODO NO ESTA VACIO INSERTO SU VALOR EN EL ARRAY PEQUEÑO
                            else:
                                children_operator.append(datafr[l])
                        #SI ESTOY EN EL ULTIMO OPERADOR DEL NODO
                        else:
                            #SI EL ACTUAL OPERADOR ESTA VACIO O ES NULO, INSERTO NULL EN EL ARRAY PEQUEÑO E INSERTO EL ARRAY PEQUEÑO EN EL GRANDE
                            if(len(datafr[l])<2):
                                children_operator.append("null")
                                array_auxiliar=[]
                                for d in range(0,len(children_operator)):
                                    elem=children_operator.pop()
                                    array_auxiliar.insert(0,elem)
                                nodes_children_operator.append(array_auxiliar)
                                
                            #SI EL ULTIMO OPERADOR NO ESTA VACIO O NULO
                            else:
                                #INSERTO EL VALOR CORRESPONDIENTE Y COMPRUEBO SI TODOS LOS VALORES DE LOS OPERADORES DE ESTE NODO SON AND
                                #SI TODOS LOS OPERADORES DE ESTE NODO SON AND INSERTO SOLAMENTE AND, SI NO, INSERTO TODO EL ARRAY PEQUEÑO EN EL GRANDE
                                children_operator.append(datafr[l])
                                if(datafr[l] =='AND'):
                                    if(("OR" in children_operator) or ("null" in children_operator)):
                                        array_auxiliar2=[]
                                        for k in range(0,len(children_operator)):
                                            elem2=children_operator.pop()
                                            array_auxiliar2.insert(0,elem2)
                                        nodes_children_operator.append(array_auxiliar2)
                                    else:
                                        for h in range(0,len(children_operator)):
                                            children_operator.pop()
                                        nodes_children_operator.append("AND")
                                #INSERTO EL VALOR CORRESPONDIENTE Y COMPRUEBO SI TODOS LOS VALORES DE LOS OPERADORES DE ESTE NODO SON OR
                                #SI TODOS LOS OPERADORES DE ESTE NODO SON OR INSERTO SOLAMENTE OR, SI NO, INSERTO TODO EL ARRAY PEQUEÑO EN EL GRANDE
                                elif(datafr[l] =='OR'):
                                    if(("AND" in children_operator) or ("null" in children_operator)):
                                        array_auxiliar3=[]
                                        for t in range(0,len(children_operator)):
                                            elem3=children_operator.pop()
                                            array_auxiliar3.insert(0,elem3)
                                        nodes_children_operator.append(array_auxiliar3)
                                    else:
                                        for s in range(0,len(children_operator)):
                                            children_operator.pop()
                                        nodes_children_operator.append("OR")
            #SI HE RECORRIDO TODOS LOS NODOS
            else:
                #SI EN EL ULTIMO NODO NO HAY OPERADOR O ESTA VACIO INSERTO NULL EN EL ARRAY GRANDE DE OPERADORES E INSERTO EL ARRAY GRANDE EN VALORES
                if((isinstance(datafr, str)) and (datafr=="null")):
                    nodes_children_operator.append("null")
                    index5 = columns.index("CVE_Items.configurations.nodes.children.operator")
                    array_auxiliar5=[]
                    for g in range(0,len(nodes_children_operator)):
                        elem5=nodes_children_operator.pop()
                        array_auxiliar5.insert(0,elem5)
                    if(array_auxiliar5.count("null") == len(array_auxiliar5)):
                        if(values[index5]==None):
                            values.pop(index5)
                            values.insert(index5,"null")
                    else:
                        if(values[index5]==None):
                            values.pop(index5)
                            values.insert(index5,array_auxiliar5)
                #SI EN EL ULTIMO NODO SI QUE HAY OPERADORES  
                else:
                    #VEO CUANTOS OPERADORES HAY EN CADA NODO
                    for l in range(0,len(datafr)):
                        #SI NO HE VISITADO TODOS LOS OPERADORES DEL ULTIMO NODO
                        if(l!=(len(datafr)-1)):
                            #SI EL ACTUAL OPERADOR DEL ULTIMO NODO ES NULL INSERTO NULL EN EL ARRAY PEQUEÑO
                            if(len(datafr[l])<2):
                                children_operator.append("null")
                            #SI EL ACTUAL NODO NO ES NULL INSERTO SU VALOR EN EL ARRAY PEQUEÑO
                            else:
                                children_operator.append(datafr[l])
                        #SI HE VISITADO TODOS LOS OPERADORES DEL ULTIMO NODO
                        else:
                            #SI EL ULTIMO OPERADOR DEL ULTIMO NODO ES NULL, INSERTO NULL EN EL ARRAY PEQUEÑO E INSERTO EL ARRAY PEQUEÑO EN EL ARRAY GRANDE
                            if(len(datafr[l])<2):
                                children_operator.append("null")
                                array_auxiliar=[]
                                for d in range(0,len(children_operator)):
                                    elem=children_operator.pop()
                                    array_auxiliar.insert(0,elem)
                                nodes_children_operator.append(array_auxiliar)
                                
                            else:
                                #SI EL ULTIMO OPERADOR DEL ULTIMO NODO NO ES NULL INSERTO SU VALOR EN EL PEQUEÑO
                                children_operator.append(datafr[l])
                                #SI EL ULTIMO OPERADOR DEL ULTIMO NODO ES AND COMPRUEBO SI TODOS SON AND, SI TODOS SON AND INSERTO AND, SI NO, INSERTO TODO EL ARRAY PEQUEÑO EN EL ARRAY GRANDE
                                if(datafr[l] =='AND'):
                                    if(("OR" in children_operator) or ("null" in children_operator)):
                                        array_auxiliar2=[]
                                        for k in range(0,len(children_operator)):
                                            elem2=children_operator.pop()
                                            array_auxiliar2.insert(0,elem2)
                                        nodes_children_operator.append(array_auxiliar2)
                                    else:
                                        for h in range(0,len(children_operator)):
                                            children_operator.pop()
                                        nodes_children_operator.append("AND")
                                #SI EL ULTIMO OPERADOR DEL ULTIMO NODO ES OR COMPRUEBO SI TODOS SON OR, SI TODOS SON OR INSERTO SOLAMENTE OR, SI NO, INSERTO EL ARRAY PEQUEÑO COMPLETO
                                elif(datafr[l] =='OR'):
                                    if(("AND" in children_operator) or ("null" in children_operator)):
                                        array_auxiliar3=[]
                                        for t in range(0,len(children_operator)):
                                            elem3=children_operator.pop()
                                            array_auxiliar3.insert(0,elem3)
                                        nodes_children_operator.append(array_auxiliar3)
                                    else:
                                        for s in range(0,len(children_operator)):
                                            children_operator.pop()
                                        nodes_children_operator.append("OR")
                if("AND" in nodes_children_operator):
                    if(("OR" in nodes_children_operator) or ("null" in nodes_children_operator)):
                        #INSERTAMOS EL ARRAY DE OPERADORES DE LOS CHILDREN EN LOS VALORES
                        index7 = columns.index("CVE_Items.configurations.nodes.children.operator")
                        array_auxiliar7=[]
                        for f in range(0,len(nodes_children_operator)):
                            elem7=nodes_children_operator.pop()
                            array_auxiliar7.insert(0,elem7)
                        if(array_auxiliar7.count("null") == len(array_auxiliar7)):
                            if(values[index7]==None):
                                values.pop(index7)
                                values.insert(index7,"null")
                        else:
                            if(values[index7]==None):
                                values.pop(index7)
                                values.insert(index7,array_auxiliar7)
                    else:
                        #INSERTAMOS EL ARRAY DE OPERADORES DE LOS CHILDREN EN LOS VALORES
                        index7 = columns.index("CVE_Items.configurations.nodes.children.operator")
                        array_auxiliar7=[]
                        for f in range(0,len(nodes_children_operator)):
                            elem7=nodes_children_operator.pop()
                            array_auxiliar7.insert(0,elem7)
                        if(array_auxiliar7.count("null") == len(array_auxiliar7)):
                            if(values[index7]==None):
                                values.pop(index7)
                                values.insert(index7,"null")
                        else:
                            if(values[index7]==None):
                                values.pop(index7)
                                values.insert(index7,"AND")
                elif("OR" in nodes_children_operator):
                    if(("AND" in nodes_children_operator) or ("null" in nodes_children_operator)):
                        #print(nodes_children_operator)
                        #INSERTAMOS EL ARRAY DE OPERADORES DE LOS CHILDREN EN LOS VALORES
                        index7 = columns.index("CVE_Items.configurations.nodes.children.operator")
                        array_auxiliar7=[]
                        for f in range(0,len(nodes_children_operator)):
                            elem7=nodes_children_operator.pop()
                            array_auxiliar7.insert(0,elem7)
                        if(array_auxiliar7.count("null") == len(array_auxiliar7)):
                            if(values[index7]==None):
                                values.pop(index7)
                                values.insert(index7,"null")
                        else:
                            if(values[index7]==None):
                                values.pop(index7)
                                values.insert(index7,array_auxiliar7)
                    else:
                        #INSERTAMOS EL ARRAY DE OPERADORES DE LOS CHILDREN EN LOS VALORES
                        index7 = columns.index("CVE_Items.configurations.nodes.children.operator")
                        array_auxiliar7=[]
                        for f in range(0,len(nodes_children_operator)):
                            elem7=nodes_children_operator.pop()
                            array_auxiliar7.insert(0,elem7)
                        if(array_auxiliar7.count("null") == len(array_auxiliar7)):
                            if(values[index7]==None):
                                values.pop(index7)
                                values.insert(index7,"null")
                        else:
                            if(values[index7]==None):
                                values.pop(index7)
                                values.insert(index7,"OR")
                else:
                    #INSERTAMOS EL ARRAY DE OPERADORES DE LOS CHILDREN EN LOS VALORES
                        index7 = columns.index("CVE_Items.configurations.nodes.children.operator")
                        array_auxiliar7=[]
                        for f in range(0,len(nodes_children_operator)):
                            elem7=nodes_children_operator.pop()
                            array_auxiliar7.insert(0,elem7)
                        if(array_auxiliar7.count("null") == len(array_auxiliar7)):
                            if(values[index7]==None):
                                values.pop(index7)
                                values.insert(index7,"null")
                        else:
                            if(values[index7]==None):
                                values.pop(index7)
                                values.insert(index7,"null")


###############################FUNCION PARA INSERTAR LOS OPERADORES DE CONFIGURACION######################################
def insertar_nodes_children(list_children,filas_len): 
    #print("INSERTAR NODES CHILDREEEEEEEEEEEEEEN")
    #print(list_children)
    for g in range(0,filas_len):
        if isinstance(list_children[g], list):
            #print("AQUICHILDREN")
            #print(list_children[g])
            #EL ELEMENTO ES LIST Y NO DICT
            e=[]
            for j in range(0,len(list_children[g])):
                e.append(str(j))
            dataframe_list=dict(zip(e,list_children[g]))
            #OBTENGO EL DATAFRAME DE LOS OPERADORES DE CHILDRENS
            dataframe_dict=pd.DataFrame.from_dict(dataframe_list,orient="index")
            if(len(dataframe_dict!=0)):
                if("operator" in dataframe_dict.columns.values):
                    insertar_nodes_children_operator(g,dataframe_dict["operator"],filas_len)
                if("cpe_match" in dataframe_dict.columns.values):
                    insertar_nodes_children_cpe_match(g,dataframe_dict["cpe_match"],filas_len)
            else:
                #print("*")
                insertar_nodes_children_operator(g,"null",filas_len)
                insertar_nodes_children_cpe_match(g,"null",filas_len)

def insertar_nodes_cpe_match(list_childre,filas_le):
    #print("INSERTAR MAAAAAAAAAAAAAAATCH")
    #print(list_childre)
    #print(filas_le)
    for h in range(0,filas_le):
        if isinstance(list_childre[h], list):
            #EL ELEMENTO ES LIST Y NO DICT
            e=[]
            for j in range(0,len(list_childre[h])):
                e.append(str(j))
            dataframe_list=dict(zip(e,list_childre[h])) 
            #OBTENGO EL DATAFRAME DE LOS OPERADORES DE CHILDRENS
            dataframe_dict=pd.DataFrame.from_dict(dataframe_list,orient="index")
            insertar_cpe_match(h,dataframe_dict,filas_le)

        
        
        
  
        
######################################################################################
###############################FUNCION RECURSIVA######################################
def recursiva(dataframe,acum,nombre_columna,numero_dataframe):
    ##print("*******")
    ##print(acum)
    ##print(nombre_columna)
    ##print(dataframe)
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
    
    
    if("CVE_Items.cve.problemtype" in acum):
        problem_type_data_description_size=columnas
    
    elif("CVE_Items.configurations" in acum) :
        if(nombre_columna=="nodes"):
            insertar_configurations(dataframe,filas,columnas)
    
    ####################################################################################
    ##########################################AVERIGUO EL TAMANIO DE REFERENCES
    elif("cve" in acum):
        if(nombre_columna == "references"):
            global references_size
            references_size=columnas
            insertar_reference_data(dataframe,columnas)
    #elif("CVE_Items.configurations" in acum):
    #    if(nombre_columna == "nodes"):
    #       global nodes_size
    #        nodes_size=filas
    
    ##print(acum)
    ##print(dataframe)
    ##print(nombre_columna)  
    ##########################################SI EL NUMERO DE COLUMNAS DEL DATAFRAME ES 1
    if(columnas ==1) :
        if("CVE_Items.cve.description.description_data" in nombre_completo):
            insertar_description_data(dataframe_dict,filas,columnas)
        else:
            #COMPROBAMOS SI LA COLUMNA ES DICT, LIST, BOOLEAN ETC
            for l in range (0,len(nombre_filas)):
                if(("CVE_Items.cve.references.reference_data" not in eliminar_numeros_nombre(nombre_completo+nombre_filas[l])) and ("CVE_Items.configurations" not in acum)):
                    if ((isinstance(dataframe_dict[0][nombre_filas[l]], dict)) or (isinstance(dataframe_dict[0][nombre_filas[l]], list)) or (isinstance(dataframe_dict[0][nombre_filas[l]], pd.DataFrame))):
                        recursiva(dataframe_dict[0][nombre_filas[l]],nombre_completo,nombre_filas[l],numero_dataframe)
                    else:
                        #SI ESTAMOS CON CVE_IMPACT
                        if("CVE_Items.impact" in (nombre_completo+nombre_filas[l])):
                            index = columns.index(nombre_completo+nombre_filas[l])
                        else:
                            #DESCRIPTION_LANG_VALUE
                            ##print("AQUI")
                            ##print(acum)
                            ##print(nombre_completo)
                            ##print(nombre_filas[l])
                            index = columns.index(eliminar_numeros_nombre(nombre_completo+nombre_filas[l]))
                            #print("INDEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEX")
                            #print(index)
                        if(values[index]==None):
                            values.pop(index)
                            values.insert(index,dataframe_dict[0][nombre_filas[l]])
    ##########################################SI EL NUMERO DE COLUMNAS DEL DATAFRAME ES MAYOR QUE 1
    else:
        if(("CVE_Items.cve.references" not in eliminar_numeros_nombre(nombre_completo)) and ("CVE_Items.configurations" not in acum)):
            #SI EL NUMERO DE FILAS ES MENOR QUE EL DE COLUMNAS TRANSPONGO LA MATRIZ PARA UN MEJOR MANEJO
            if (filas < columnas):
                ##print("ENTROOO")
                dataframe_dict_traspuesto=dataframe_dict.transpose()
                filas_traspuesto=dataframe_dict_traspuesto.index.values
                columnas_traspuesto=dataframe_dict_traspuesto.columns.values
                ##print(dataframe_dict)
                ##print(filas)
                ##print(columnas)
                ##print(nombre_completo)
                #CASO PARTICULAR DE LAS METRICAS
                if((filas == 2 and ("CVE_Items.impact" in nombre_completo)) or (filas == 1 and ("CVE_Items.impact" in nombre_completo))):
                    insertar_metrics(columnas_traspuesto,nombre_completo,filas_traspuesto,dataframe_dict_traspuesto)
                #OTROS CASOS APARTE DE LAS METRICAS
                #lLAMO AL METODO PARA INSERTAR PROBLEMTYPE_DATA
                elif("CVE_Items.cve.problemtype.problemtype_data" in nombre_completo):
                    insertar_problemtype_data_description(dataframe_dict_traspuesto,filas_traspuesto,columnas_traspuesto)
            
            
            
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
            
            
def transpose2(l1, l2):
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
            




###############################################################################################
#################################COMIENZO DEL PROGRAMA##########################################   



#ABRO DOCUMENTO
with open('List_cve_smart_home_2023.json','r',encoding='utf-8') as f:
    data = json.loads(f.read())

#CONVIERTO A DATAFRAME EL JSON GLOBAL
dataframe_inicial=pd.DataFrame.from_dict(data)
nombres_filas_inicial=dataframe_inicial.index.values

#EMPIEZO A TRABAJAR CON CVE_ITEMS, CONVIRTIENDOLO A DATAFRAME
cve_items=pd.DataFrame(dataframe_inicial.result["CVE_Items"])
cve_items_aux=cve_items.transpose()
nombres_filas_cve_items=cve_items_aux.index.values
acumulado="CVE_Items."

#db_cve_items_aux.shape[1]
#ME QUEDO AQUI, COMPROBAR INSERTAR NODES CHILDREN
for h in range (0,cve_items_aux.shape[1]):
    values=[None] * len(columns)
    
    #Melse:
    #values.pop(0)
    #values.pop(1)
    #values.pop(2)
    #values.pop(3)
    values.insert(0,"CVE")
    values.insert(1,"MITRE")
    values.insert(2,"4.0")
    values.insert(3,"2023-04-11T16:48Z")
  
    #Cogemos el nombre de la vulnerabilidad para llamar al fichero
    nombre_vulnerabilidad_aux=cve_items_aux[h].cve
    nombre_vulnerabilidad=nombre_vulnerabilidad_aux["CVE_data_meta"]["ID"]
           
    #Veo si tenemos que recorrer el dataframe de cada columna o no
    for l in range(0,cve_items_aux.shape[0]):
        if ((isinstance(cve_items_aux[h][nombres_filas_cve_items[l]], dict)) or (isinstance(cve_items_aux[h][nombres_filas_cve_items[l]], list)) or (isinstance(cve_items_aux[h][nombres_filas_cve_items[l]], pd.DataFrame))):
            ##print("hola")
            ##print("")
            recursiva(cve_items_aux[h][nombres_filas_cve_items[l]],acumulado,nombres_filas_cve_items[l],h)
        else:
            #Veo si coincide con algun nombre de columna e inserto el elemento en esa posicion, previamente eliminado el elemento none para no aumentar el tamanio del array
            index = columns.index(acumulado+nombres_filas_cve_items[l])
            if(values[index]==None):
                values.pop(index)
                values.insert(index,cve_items_aux[h][nombres_filas_cve_items[l]])
    dff=pd.DataFrame()
    #for r in range(0,len(columns)):
        ##print("**********************")
        ##print(columns[r])
        ##print(values[r])
    ##print(h)
    
    
        
    array_aux7=[]
    for g in range(0,len(columns)):
        if((values[g] == None) or (values[g]=="null")):
            array_aux7.append("NONE")
        else:
            array_aux7.append(values[g])
    values_grande.append(array_aux7)
    
    #if(h==5):
        #print(values_grande[5])
    #EL FALLO ESTA AQUI, CUANDO INSERTAMOS EN EL ARRAY GRANDE
##print("*********************")
##print(columns)
##print("///////////a////////")
##print(len(values_grande))
    

values_grande_tras = []
valuesdef=transpose2(values_grande, values_grande_tras)




df_excel=pd.DataFrame(valuesdef,columns[0:60])
df_excel2=df_excel.transpose()
df_excel2.to_excel('cves_smart_home_2023.xlsx')

