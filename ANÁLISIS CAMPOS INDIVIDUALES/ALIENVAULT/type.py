
import pandas as pd
from datetime import datetime

#Abro los ficheros con los que voy a tratar


df_alienvault_iot = pd.read_excel('alienvault_iot_2023.xlsx')




#Variables donde almacenare el contador de tipo de objeto de Alienvault IOT
count_type_report_alienvault_iot=0
count_type_identity_alienvault_iot=0
count_type_indicator_alienvault_iot=0
count_type_vulnerability_alienvault_iot=0
count_type_another_alienvault_iot=0

#Variable auxiliar para almacenar el numero de objetos
len_aux_iot=0


#Comprobamos el tipo de objeto
for r in range(0,len(df_alienvault_iot["type"])):
    if('[' in df_alienvault_iot["type"][r]):
        aux=df_alienvault_iot["type"][r].split(",")
        for l in range(0,len(aux)):
            if(len(aux)>0):
                len_aux_iot+=1
                aux_str=aux[l].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
                if(aux_str == 'report'):
                    count_type_report_alienvault_iot+=1  
                elif(aux_str == 'identity'):
                    count_type_identity_alienvault_iot+=1  
                elif(aux_str == 'indicator'):
                    count_type_indicator_alienvault_iot+=1  
                elif(aux_str == 'vulnerability'):
                    count_type_vulnerability_alienvault_iot+=1  
                else:
                    if(aux_str!='t'):
                        count_type_another_alienvault_iot+=1
    else:
        len_aux_iot+=1
        if(df_alienvault_iot["type"][r] == 'report'):
            count_type_report_alienvault_iot+=1  
        elif(df_alienvault_iot["type"][r] == 'identity'):
            count_type_identity_alienvault_iot+=1  
        elif(df_alienvault_iot["type"][r] == 'indicator'):
            count_type_indicator_alienvault_iot+=1  
        elif(df_alienvault_iot["type"][r] == 'vulnerability'):
            count_type_vulnerability_alienvault_iot+=1 
        else:
            if(df_alienvault_iot["type"][r]!='t'):
                count_type_another_alienvault_iot+=1
        

print("**************************ESTADÍSTICAS TIPO DE OBJETO ALIENVAULT IOT ********************************")
print("\n")
print("HAY "+str(count_type_report_alienvault_iot)+" OBJETOS DE TIPO REPORTE \n")
print("HAY "+str(count_type_identity_alienvault_iot)+" OBJETOS DE TIPO IDENTIDAD \n")
print("HAY "+str(count_type_indicator_alienvault_iot)+" OBJETOS DE TIPO INDICADOR \n")
print("HAY "+str(count_type_vulnerability_alienvault_iot)+" OBJETOS DE TIPO VULNERABILIDAD \n")
print("HAY "+str(count_type_another_alienvault_iot)+" OBJETOS DE OTRO TIPO DISTINTO \n")

print("\n")
print("**************************PORCENTAJE TIPO DE OBJETO ALIENVAULT IOT ********************************")
print("\n")

print("EL "+str(float((count_type_report_alienvault_iot*100)/(len_aux_iot)))+"% DE LOS OBJETOS ES DE TIPO REPORTE \n")
print("EL "+str(float((count_type_identity_alienvault_iot*100)/(len_aux_iot)))+"% DE LOS OBJETOS ES DE TIPO IDENTIDAD \n")
print("EL "+str(float((count_type_indicator_alienvault_iot*100)/(len_aux_iot)))+"% DE LOS OBJETOS ES DE TIPO INDICADOR \n")
print("EL "+str(float((count_type_vulnerability_alienvault_iot*100)/(len_aux_iot)))+"% DE LOS OBJETOS ES DE TIPO VULNERABILIDAD \n")
print("EL "+str(float((count_type_another_alienvault_iot*100)/(len_aux_iot)))+"% DE LOS OBJETOS ES DE OTRO TIPO DISTINTO \n")

print("\n")






df_alienvault_sh = pd.read_excel('alienvault_smart_home_2023.xlsx')



#Variables donde almacenare el contador de tipo de objeto de Alienvault SMART HOME
count_type_report_alienvault_sh=0
count_type_identity_alienvault_sh=0
count_type_indicator_alienvault_sh=0
count_type_vulnerability_alienvault_sh=0
count_type_another_alienvault_sh=0
#Variable auxiliar para almacenar el numero de objetos
len_aux_sh=0


#Comprobamos el tipo de objeto
for r in range(0,len(df_alienvault_sh["type"])):
    #Si existen varios objetos en la fila actual
    if('[' in df_alienvault_sh["type"][r]):
        aux=df_alienvault_sh["type"][r].split(",")
        for l in range(0,len(aux)):
            if(len(aux)>0):
                len_aux_sh+=1
                aux_str=aux[l].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
                if(aux_str == 'report'):
                    count_type_report_alienvault_sh+=1  
                elif(aux_str == 'identity'):
                    count_type_identity_alienvault_sh+=1  
                elif(aux_str == 'indicator'):
                    count_type_indicator_alienvault_sh+=1  
                elif(aux_str == 'vulnerability'):
                    count_type_vulnerability_alienvault_sh+=1  
                else:
                    if(aux_str!='t'):
                        count_type_another_alienvault_sh+=1
    else:
        #Si existe un unico objeto en la fila actual
        len_aux_sh+=1
        if(df_alienvault_sh["type"][r] == 'report'):
            count_type_report_alienvault_sh+=1  
        elif(df_alienvault_sh["type"][r] == 'identity'):
            count_type_identity_alienvault_sh+=1  
        elif(df_alienvault_sh["type"][r] == 'indicator'):
            count_type_indicator_alienvault_sh+=1 
        elif(df_alienvault_sh["type"][r] == 'vulnerability'):
            count_type_vulnerability_alienvault_sh+=1 
        else:
            if(df_alienvault_sh["type"][r]!='t'):
                count_type_another_alienvault_sh+=1
        

print("**************************ESTADÍSTICAS TIPO DE OBJETO ALIENVAULT SMART HOME ********************************")
print("\n")
print("HAY "+str(count_type_report_alienvault_sh)+" OBJETOS DE TIPO REPORTE \n")
print("HAY "+str(count_type_identity_alienvault_sh)+" OBJETOS DE TIPO IDENTIDAD \n")
print("HAY "+str(count_type_indicator_alienvault_sh)+" OBJETOS DE TIPO INDICADOR \n")
print("HAY "+str(count_type_vulnerability_alienvault_sh)+" OBJETOS DE TIPO VULNERABILIDAD \n")
print("HAY "+str(count_type_another_alienvault_sh)+" OBJETOS DE OTRO TIPO DISTINTO \n")

print("\n")
print("**************************PORCENTAJE TIPO DE OBJETO ALIENVAULT SMART HOME ********************************")
print("\n")

print("EL "+str(float((count_type_report_alienvault_sh*100)/(len_aux_sh)))+"% DE LOS OBJETOS ES DE TIPO REPORTE \n")
print("EL "+str(float((count_type_identity_alienvault_sh*100)/(len_aux_sh)))+"% DE LOS OBJETOS ES DE TIPO IDENTIDAD \n")
print("EL "+str(float((count_type_indicator_alienvault_sh*100)/(len_aux_sh)))+"% DE LOS OBJETOS ES DE TIPO INDICADOR \n")
print("EL "+str(float((count_type_vulnerability_alienvault_sh*100)/(len_aux_sh)))+"% DE LOS OBJETOS ES DE TIPO VULNERABILIDAD \n")
print("EL "+str(float((count_type_another_alienvault_sh*100)/(len_aux_sh)))+"% DE LOS OBJETOS ES DE OTRO TIPO DISTINTO \n")

print("\n")






        

print("**************************ESTADÍSTICAS TIPO DE OBJETO ALIENVAULT PARTE IOT Y SMART HOME CONJUNTAS********************************")
print("\n")
print("HAY "+str(count_type_report_alienvault_sh+count_type_report_alienvault_iot)+" OBJETOS DE TIPO REPORTE \n")
print("HAY "+str(count_type_identity_alienvault_sh+count_type_identity_alienvault_iot)+" OBJETOS DE TIPO IDENTIDAD \n")
print("HAY "+str(count_type_indicator_alienvault_sh+count_type_indicator_alienvault_iot)+" OBJETOS DE TIPO INDICADOR \n")
print("HAY "+str(count_type_vulnerability_alienvault_sh+count_type_vulnerability_alienvault_iot)+" OBJETOS DE TIPO VULNERABILIDAD \n")
print("HAY "+str(count_type_another_alienvault_sh+count_type_another_alienvault_iot)+" OBJETOS DE OTRO TIPO DISTINTO \n")

print("\n")
print("**************************PORCENTAJE TIPO DE OBJETO ALIENVAULT PARTE IOT Y SMART HOME CONJUNTAS********************************")
print("\n")

print("EL "+str(float((((count_type_report_alienvault_sh+count_type_report_alienvault_iot)*100)/(len_aux_iot+len_aux_sh))))+" % DE LOS OBJETOS ES DE TIPO REPORTE \n")
print("EL "+str(float((((count_type_identity_alienvault_sh+count_type_identity_alienvault_iot)*100)/(len_aux_iot+len_aux_sh))))+" % DE LOS OBJETOS ES DE TIPO IDENTIDAD \n")
print("EL "+str(float((((count_type_indicator_alienvault_sh+count_type_indicator_alienvault_iot)*100)/(len_aux_iot+len_aux_sh))))+" % DE LOS OBJETOS ES DE TIPO INDICADOR \n")
print("EL "+str(float((((count_type_vulnerability_alienvault_sh+count_type_vulnerability_alienvault_iot)*100)/(len_aux_iot+len_aux_sh))))+" % DE LOS OBJETOS ES DE TIPO VULNERABILIDAD \n")
print("EL "+str(float((((count_type_another_alienvault_sh+count_type_another_alienvault_iot)*100)/(len_aux_iot+len_aux_sh))))+" % DE LOS OBJETOS ES DE OTRO TIPO DISTINTO \n")
print("\n")









