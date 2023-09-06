
import pandas as pd
#Abrimos los ficheros con los que vamos a trabajar
df_ali_iot=pd.read_excel('alienvault_iot_2023.xlsx')
df_th_act_rep_ibm_iot=pd.read_excel('ibm_threat_activity_report_iot_2023_v2.xlsx')


#Array para guardar el valor de los patrones de alienvault para IOT
pattern_alienvault_iot=[]
#Array para guardar el valor de los patrones de IBM para IOT
pattern_ibm_iot=[]
#Array para guardar el valor de los patrones coincidentes de IBM y ALIENVAULT para IOT
elementos_coincidentes_pattern_iot=[]


        
#Inserto un separador para los patterns de IBM
pattern_ibm_iot.append("IBM_THREAT_ACTIVITY_REPORT")
pattern_ibm_iot.append("************************")

#Recorro el valor de la columna pattern para el fichero de threat activity report
for t in range(0,len(df_th_act_rep_ibm_iot["pattern"])):
    #Compruebo si la fila tiene o no valor
    if(df_th_act_rep_ibm_iot["pattern"][t] !='NONE'):
        #Compruebo si la fila tiene varios valores de patrones
        if(',' in df_th_act_rep_ibm_iot["pattern"][t]):
            #Guardo los valores de patterns de la fila
            patterns_thractrep_filas_iot = df_th_act_rep_ibm_iot["pattern"][t].split(',')
            #Recorro los valores de patterns de la fila y los inserto en el vector de patrones para IBM
            for j in range(0,len(patterns_thractrep_filas_iot)):
                if((patterns_thractrep_filas_iot[j].replace('[','').replace(']','').replace("'","").replace("","").replace(" ",""))!='NONE'):
                    pattern_ibm_iot.append(patterns_thractrep_filas_iot[j].replace('[','').replace(']','').replace("'","").replace("","").replace(" ",""))
        else:
            #Inserto el unico valor de pattern de la fila en el vector de patterns de IBM
            pattern_ibm_iot.append(df_th_act_rep_ibm_iot["pattern"][t].replace('[','').replace(']','').replace("'","").replace("",""))
        





#Recorro el valor de la columna pattern para el fichero de Alienvault
for k in range(0,len(df_ali_iot["pattern"])):
    #Compruebo si la fila tiene o no valor
    if(df_ali_iot["pattern"][k] !='NONE'):
        #Compruebo si la fila tiene varios valores de patrones
        if(',' in df_ali_iot["pattern"][k]):
            #Guardo los valores de patterns de la fila
            pat_ali_iot = df_ali_iot["pattern"][k].split(',')
            #Recorro los valores de patterns de la fila y los inserto en el vector de patrones para Alienvault
            for j in range(0,len(pat_ali_iot)):
                if((pat_ali_iot[j].replace('[','').replace(']','').replace("'","").replace("","").replace(" ",""))!='NONE'):
                    pattern_alienvault_iot.append(pat_ali_iot[j].replace('[','').replace(']','').replace("'","").replace("","").replace(" ",""))
        else:
            #Inserto el unico valor de pattern de la fila en el vector de patterns de Alienvault
            pattern_alienvault_iot.append(df_ali_iot["pattern"][k].replace('[','').replace(']','').replace("'","").replace("",""))
            

#Busco si hay patrones coincidentes entre IBM y Alienvault            
for patterns_iot in pattern_alienvault_iot:
    if patterns_iot in pattern_ibm_iot:
        elementos_coincidentes_pattern_iot.append(patterns_iot)
        
#Imprimo los resultados        
if(len(elementos_coincidentes_pattern_iot)==0):
    print("NO HAY PATRONES COINCIDENTES ENTRE ALIENVAULT E IBM PARA IOT")
else:
    print("PATRONES COINCIDENTES ENTRE ALIENVAULT E IBM PARA IOT:")
    for g in range(0,len(elementos_coincidentes_pattern_iot)):
        print(elementos_coincidentes_pattern_iot[g])
        print("\n")



#Abrimos los ficheros con los que vamos a trabajar
df_ali_sh=pd.read_excel('alienvault_smart_home_2023.xlsx')
df_th_act_rep_ibm_sh=pd.read_excel('ibm_threat_activity_report_smarthome_2023_v2.xlsx')


#Array para guardar el valor de los patrones de alienvault para SMART HOME
pattern_alienvault_sh=[]
#Array para guardar el valor de los patrones de IBM para SMART HOME
pattern_ibm_sh=[]
#Array para guardar el valor de los patrones coincidentes de IBM y ALIENVAULT para SMART HOME
elementos_coincidentes_pattern_sh=[]


#Inserto un separador para los patterns de IBM
pattern_ibm_sh.append("IBM_THREAT_ACTIVITY_REPORT")
pattern_ibm_sh.append("************************")

#Recorro el valor de la columna pattern para el fichero de threat activity report
for t in range(0,len(df_th_act_rep_ibm_sh["pattern"])):
    #Compruebo si la fila tiene o no valor
    if(df_th_act_rep_ibm_sh["pattern"][t] !='NONE'):
        #Compruebo si la fila tiene varios valores de patrones
        if(',' in df_th_act_rep_ibm_sh["pattern"][t]):
            #Guardo los valores de patterns de la fila
            patterns_thractrep_filas_sh = df_th_act_rep_ibm_sh["pattern"][t].split(',')
            #Recorro los valores de patterns de la fila y los inserto en el vector de patrones para IBM
            for j in range(0,len(patterns_thractrep_filas_sh)):
                if((patterns_thractrep_filas_sh[j].replace('[','').replace(']','').replace("'","").replace("","").replace(" ",""))!='NONE'):
                    pattern_ibm_sh.append(patterns_thractrep_filas_sh[j].replace('[','').replace(']','').replace("'","").replace("","").replace(" ",""))
        else:
            #Inserto el unico valor de pattern de la fila en el vector de patterns de IBM
            pattern_ibm_sh.append(df_th_act_rep_ibm_sh["pattern"][t].replace('[','').replace(']','').replace("'","").replace("",""))
        





#Recorro el valor de la columna pattern para el fichero de Alienvault
for k in range(0,len(df_ali_sh["pattern"])):
    #Compruebo si la fila tiene o no valor
    if(df_ali_sh["pattern"][k] !='NONE'):
        #Compruebo si la fila tiene varios valores de patrones
        if(',' in df_ali_sh["pattern"][k]):
            #Guardo los valores de patterns de la fila
            pat_ali_sh = df_ali_sh["pattern"][k].split(',')
            #Recorro los valores de patterns de la fila y los inserto en el vector de patrones para Alienvault
            for j in range(0,len(pat_ali_sh)):
                if((pat_ali_sh[j].replace('[','').replace(']','').replace("'","").replace("","").replace(" ",""))!='NONE'):
                    pattern_alienvault_sh.append(pat_ali_sh[j].replace('[','').replace(']','').replace("'","").replace("","").replace(" ",""))
        else:
            #Inserto el unico valor de pattern de la fila en el vector de patterns de Alienvault
            pattern_alienvault_sh.append(df_ali_sh["pattern"][k].replace('[','').replace(']','').replace("'","").replace("",""))
            

#Busco si hay patrones coincidentes entre IBM y Alienvault            
for patterns_sh in pattern_alienvault_sh:
    if patterns_sh in pattern_ibm_sh:
        elementos_coincidentes_pattern_sh.append(patterns_sh)
        
#Imprimo los resultados        
if(len(elementos_coincidentes_pattern_sh)==0):
    print("NO HAY PATRONES COINCIDENTES ENTRE ALIENVAULT E IBM PARA SMART HOME")
else:
    print("PATRONES COINCIDENTES ENTRE ALIENVAULT E IBM PARA SMART HOME:")
    for g in range(0,len(elementos_coincidentes_pattern_sh)):
        print(elementos_coincidentes_pattern_sh[g])
        print("\n")










#Compruebo si hay elementos coincidentes entre las partes IOT Y SMART HOME

#Vector donde guardare los elementos coincidentes de ambas partes en Alienvault
patterns_alienvault=[]
#Vector donde guardare los elementos coincidentes de ambas partes en IBM
patterns_ibm=[]
#Vector donde guardare los elementos coincidentes de ALIENVAULT Y SMART HOME
elementos_coincidentes_pattern=[]

#Inserto los elementos de IOT y SMART HOME de las partes de IOT Y ALIENVAULT en el vector correspondiente
for elem_refs in pattern_alienvault_iot:
    patterns_alienvault.append(elem_refs)

for elem_refs_sh in pattern_alienvault_sh:
    patterns_alienvault.append(elem_refs_sh)


for elem_refsibm in pattern_ibm_iot:
    patterns_ibm.append(elem_refsibm)

for elem_refsibm_sh in pattern_ibm_sh:
    patterns_ibm.append(elem_refsibm_sh)


#Busco los elementos coincidentes
for elem_refss in patterns_alienvault:
    if elem_refss in patterns_ibm:
        elementos_coincidentes_pattern.append(elem_refss)

#Imprimo los resultados         
if(len(elementos_coincidentes_id)==0):
    print("NO HAY PATRONES DE ALIENVAULT E IBM COINCIDENTES")
else:
    print("PATRONES DE ALIENVAULT E IBM COINCIDENTES :")
    print("\n")
    for g in range(0,len(elementos_coincidentes_pattern)):
        print(elementos_coincidentes_pattern[g])
        print("\n")
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		