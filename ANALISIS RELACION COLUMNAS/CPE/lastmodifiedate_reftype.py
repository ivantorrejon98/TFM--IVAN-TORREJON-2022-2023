
import pandas as pd

#Abro los ficheros con los que voy a tratar


df_cpe_iot=pd.read_excel('cpes_iot_2023.xlsx')
df_cpe_sh=pd.read_excel('cpes_smart_home_2023.xlsx')



#Variables para almacenar el tipo de entrada segun el anio en el que fue modificado por ultima vez
cpes_lastmodified2023_typeversion_iot=0
cpes_lastmodified2023_typeproduct_iot=0
cpes_lastmodified2023_typeadvisory_iot=0
cpes_lastmodified2023_typechangelog_iot=0
cpes_lastmodified2023_typenone_iot=0
cpes_lastmodified2023_typevendor_iot=0
cpes_lastmodified2023_iot=0

cpes_lastmodified2022_typeversion_iot=0
cpes_lastmodified2022_typeproduct_iot=0
cpes_lastmodified2022_typeadvisory_iot=0
cpes_lastmodified2022_typechangelog_iot=0
cpes_lastmodified2022_typenone_iot=0
cpes_lastmodified2022_typevendor_iot=0
cpes_lastmodified2022_iot=0

cpes_lastmodified2021_typeversion_iot=0
cpes_lastmodified2021_typeproduct_iot=0
cpes_lastmodified2021_typeadvisory_iot=0
cpes_lastmodified2021_typechangelog_iot=0
cpes_lastmodified2021_typenone_iot=0
cpes_lastmodified2021_typevendor_iot=0
cpes_lastmodified2021_iot=0

cpes_lastmodified2020_typeversion_iot=0
cpes_lastmodified2020_typeproduct_iot=0
cpes_lastmodified2020_typeadvisory_iot=0
cpes_lastmodified2020_typechangelog_iot=0
cpes_lastmodified2020_typenone_iot=0
cpes_lastmodified2020_typevendor_iot=0
cpes_lastmodified2020_iot=0

cpes_lastmodified2019_typeversion_iot=0
cpes_lastmodified2019_typeproduct_iot=0
cpes_lastmodified2019_typeadvisory_iot=0
cpes_lastmodified2019_typechangelog_iot=0
cpes_lastmodified2019_typenone_iot=0
cpes_lastmodified2019_typevendor_iot=0
cpes_lastmodified2019_iot=0

cpes_lastmodified2018_typeversion_iot=0
cpes_lastmodified2018_typeproduct_iot=0
cpes_lastmodified2018_typeadvisory_iot=0
cpes_lastmodified2018_typechangelog_iot=0
cpes_lastmodified2018_typenone_iot=0
cpes_lastmodified2018_typevendor_iot=0
cpes_lastmodified2018_iot=0

#Recorro los valores de fecha de ultima modificacion
for r in range(0,len(df_cpe_iot["cpes.lastModifiedDate"])):
    str_anio_modifdate_cpe_iot=df_cpe_iot["cpes.lastModifiedDate"][r].split("-")
    anio_modifdate_cpe_iot=int(str_anio_modifdate_cpe_iot[0])
    if(anio_modifdate_cpe_iot >= 2023):
        #Compruebo si existen varios valores de tipo de entrada en una misma fila
        if('[' in df_cpe_iot["cpes.refs.type"][r]):
            aux=df_cpe_iot["cpes.refs.type"][r].split(",")
            for k in range(0,len(aux)):
                if(len(aux)>0):
                    #Recorro los valores de tipo de entrada para una misma fila
                    cpes_lastmodified2023_iot+=1
                    aux_str=aux[k].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
                    #Compruebo el tipo de entrada 
                    if(aux_str == 'NONE'):
                        cpes_lastmodified2023_typenone_iot+=1  
                    elif(aux_str == 'Version'):
                        cpes_lastmodified2023_typeversion_iot+=1  
                    elif(aux_str == 'Product'):
                        cpes_lastmodified2023_typeproduct_iot+=1  
                    elif(aux_str == 'Advisory'):
                        cpes_lastmodified2023_typeadvisory_iot+=1  
                    elif((aux_str == 'Change Log') or (aux_str == 'ChangeLog')):
                        cpes_lastmodified2023_typechangelog_iot+=1
                    elif(aux_str == 'Vendor'):
                        cpes_lastmodified2023_typevendor_iot+=1
        else:
            cpes_lastmodified2023_iot+=1
            if(df_cpe_iot["cpes.refs.type"][r] == 'NONE'):
                cpes_lastmodified2023_typenone_iot+=1 
            elif(df_cpe_iot["cpes.refs.type"][r] == 'Version'):
                cpes_lastmodified2023_typeversion_iot+=1 
            elif(df_cpe_iot["cpes.refs.type"][r] == 'Product'):
                cpes_lastmodified2023_typeproduct_iot+=1 
            elif(df_cpe_iot["cpes.refs.type"][r] == 'Advisory'):
                cpes_lastmodified2023_typeadvisory_iot+=1 
            elif((df_cpe_iot["cpes.refs.type"][r] == 'Change Log') or(df_cpe_iot["cpes.refs.type"][r] == 'ChangeLog')):
                cpes_lastmodified2023_typechangelog_iot+=1
            elif(df_cpe_iot["cpes.refs.type"][r] == 'Vendor'):
                cpes_lastmodified2023_typevendor_iot+=1
    elif(anio_modifdate_cpe_iot >= 2022):
        if('[' in df_cpe_iot["cpes.refs.type"][r]):
            aux=df_cpe_iot["cpes.refs.type"][r].split(",")
            for k in range(0,len(aux)):
                if(len(aux)>0):
                    cpes_lastmodified2022_iot+=1
                    aux_str=aux[k].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
                    if(aux_str == 'NONE'):
                        cpes_lastmodified2022_typenone_iot+=1  
                    elif(aux_str == 'Version'):
                        cpes_lastmodified2022_typeversion_iot+=1  
                    elif(aux_str == 'Product'):
                        cpes_lastmodified2022_typeproduct_iot+=1  
                    elif(aux_str == 'Advisory'):
                        cpes_lastmodified2022_typeadvisory_iot+=1  
                    elif((aux_str == 'Change Log') or (aux_str == 'ChangeLog')):
                        cpes_lastmodified2022_typechangelog_iot+=1
                    elif(aux_str == 'Vendor'):
                        cpes_lastmodified2022_typevendor_iot+=1
        else:
            cpes_lastmodified2022_iot+=1
            if(df_cpe_iot["cpes.refs.type"][r] == 'NONE'):
                cpes_lastmodified2022_typenone_iot+=1 
            elif(df_cpe_iot["cpes.refs.type"][r] == 'Version'):
                cpes_lastmodified2022_typeversion_iot+=1 
            elif(df_cpe_iot["cpes.refs.type"][r] == 'Product'):
                cpes_lastmodified2022_typeproduct_iot+=1 
            elif(df_cpe_iot["cpes.refs.type"][r] == 'Advisory'):
                cpes_lastmodified2022_typeadvisory_iot+=1 
            elif((df_cpe_iot["cpes.refs.type"][r] == 'Change Log') or(df_cpe_iot["cpes.refs.type"][r] == 'ChangeLog')):
                cpes_lastmodified2022_typechangelog_iot+=1
            elif(df_cpe_iot["cpes.refs.type"][r] == 'Vendor'):
                cpes_lastmodified2022_typevendor_iot+=1
    elif(anio_modifdate_cpe_iot >= 2021):
        if('[' in df_cpe_iot["cpes.refs.type"][r]):
            aux=df_cpe_iot["cpes.refs.type"][r].split(",")
            for k in range(0,len(aux)):
                if(len(aux)>0):
                    cpes_lastmodified2021_iot+=1
                    aux_str=aux[k].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
                    if(aux_str == 'NONE'):
                        cpes_lastmodified2021_typenone_iot+=1  
                    elif(aux_str == 'Version'):
                        cpes_lastmodified2021_typeversion_iot+=1  
                    elif(aux_str == 'Product'):
                        cpes_lastmodified2021_typeproduct_iot+=1  
                    elif(aux_str == 'Advisory'):
                        cpes_lastmodified2021_typeadvisory_iot+=1  
                    elif((aux_str == 'Change Log') or (aux_str == 'ChangeLog')):
                        cpes_lastmodified2021_typechangelog_iot+=1  
                    elif(aux_str == 'Vendor'):
                        cpes_lastmodified2022_typevendor_iot+=1
        else:
            cpes_lastmodified2021_iot+=1
            if(df_cpe_iot["cpes.refs.type"][r] == 'NONE'):
                cpes_lastmodified2021_typenone_iot+=1 
            elif(df_cpe_iot["cpes.refs.type"][r] == 'Version'):
                cpes_lastmodified2021_typeversion_iot+=1 
            elif(df_cpe_iot["cpes.refs.type"][r] == 'Product'):
                cpes_lastmodified2021_typeproduct_iot+=1 
            elif(df_cpe_iot["cpes.refs.type"][r] == 'Advisory'):
                cpes_lastmodified2021_typeadvisory_iot+=1 
            elif((df_cpe_iot["cpes.refs.type"][r] == 'Change Log') or(df_cpe_iot["cpes.refs.type"][r] == 'ChangeLog')):
                cpes_lastmodified2021_typechangelog_iot+=1
            elif(df_cpe_iot["cpes.refs.type"][r] == 'Vendor'):
                cpes_lastmodified2021_typevendor_iot+=1
    elif(anio_modifdate_cpe_iot >= 2020):
        if('[' in df_cpe_iot["cpes.refs.type"][r]):
            aux=df_cpe_iot["cpes.refs.type"][r].split(",")
            for k in range(0,len(aux)):
                if(len(aux)>0):
                    cpes_lastmodified2020_iot+=1
                    aux_str=aux[k].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
                    if(aux_str == 'NONE'):
                        cpes_lastmodified2020_typenone_iot+=1  
                    elif(aux_str == 'Version'):
                        cpes_lastmodified2020_typeversion_iot+=1  
                    elif(aux_str == 'Product'):
                        cpes_lastmodified2020_typeproduct_iot+=1  
                    elif(aux_str == 'Advisory'):
                        cpes_lastmodified2020_typeadvisory_iot+=1  
                    elif((aux_str == 'Change Log') or (aux_str == 'ChangeLog')):
                        cpes_lastmodified2020_typechangelog_iot+=1 
                    elif(aux_str == 'Vendor'):
                        cpes_lastmodified2020_typevendor_iot+=1
        else:
            cpes_lastmodified2020_iot+=1
            if(df_cpe_iot["cpes.refs.type"][r] == 'NONE'):
                cpes_lastmodified2020_typenone_iot+=1 
            elif(df_cpe_iot["cpes.refs.type"][r] == 'Version'):
                cpes_lastmodified2020_typeversion_iot+=1 
            elif(df_cpe_iot["cpes.refs.type"][r] == 'Product'):
                cpes_lastmodified2020_typeproduct_iot+=1 
            elif(df_cpe_iot["cpes.refs.type"][r] == 'Advisory'):
                cpes_lastmodified2020_typeadvisory_iot+=1 
            elif((df_cpe_iot["cpes.refs.type"][r] == 'Change Log') or(df_cpe_iot["cpes.refs.type"][r] == 'ChangeLog')):
                cpes_lastmodified2020_typechangelog_iot+=1
            elif(df_cpe_iot["cpes.refs.type"][r] == 'Vendor'):
                cpes_lastmodified2020_typevendor_iot+=1
    elif(anio_modifdate_cpe_iot >= 2019):
        if('[' in df_cpe_iot["cpes.refs.type"][r]):
            aux=df_cpe_iot["cpes.refs.type"][r].split(",")
            for k in range(0,len(aux)):
                if(len(aux)>0):
                    cpes_lastmodified2019_iot+=1
                    aux_str=aux[k].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
                    if(aux_str == 'NONE'):
                        cpes_lastmodified2019_typenone_iot+=1  
                    elif(aux_str == 'Version'):
                        cpes_lastmodified2019_typeversion_iot+=1  
                    elif(aux_str == 'Product'):
                        cpes_lastmodified2019_typeproduct_iot+=1  
                    elif(aux_str == 'Advisory'):
                        cpes_lastmodified2019_typeadvisory_iot+=1  
                    elif((aux_str == 'Change Log') or (aux_str == 'ChangeLog')):
                        cpes_lastmodified2019_typechangelog_iot+=1 
                    elif(aux_str == 'Vendor'):
                        cpes_lastmodified2019_typevendor_iot+=1
        else:
            cpes_lastmodified2019_iot+=1
            if(df_cpe_iot["cpes.refs.type"][r] == 'NONE'):
                cpes_lastmodified2019_typenone_iot+=1 
            elif(df_cpe_iot["cpes.refs.type"][r] == 'Version'):
                cpes_lastmodified2019_typeversion_iot+=1 
            elif(df_cpe_iot["cpes.refs.type"][r] == 'Product'):
                cpes_lastmodified2019_typeproduct_iot+=1 
            elif(df_cpe_iot["cpes.refs.type"][r] == 'Advisory'):
                cpes_lastmodified2019_typeadvisory_iot+=1 
            elif((df_cpe_iot["cpes.refs.type"][r] == 'Change Log') or(df_cpe_iot["cpes.refs.type"][r] == 'ChangeLog')):
                cpes_lastmodified2019_typechangelog_iot+=1
            elif(df_cpe_iot["cpes.refs.type"][r] == 'Vendor'):
                cpes_lastmodified2019_typevendor_iot+=1
    else:
        if('[' in df_cpe_iot["cpes.refs.type"][r]):
            aux=df_cpe_iot["cpes.refs.type"][r].split(",")
            for k in range(0,len(aux)):
                if(len(aux)>0):
                    cpes_lastmodified2018_iot+=1
                    aux_str=aux[k].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
                    if(aux_str == 'NONE'):
                        cpes_lastmodified2018_typenone_iot+=1  
                    elif(aux_str == 'Version'):
                        cpes_lastmodified2018_typeversion_iot+=1  
                    elif(aux_str == 'Product'):
                        cpes_lastmodified2018_typeproduct_iot+=1  
                    elif(aux_str == 'Advisory'):
                        cpes_lastmodified2018_typeadvisory_iot+=1  
                    elif((aux_str == 'Change Log') or (aux_str == 'ChangeLog')):
                        cpes_lastmodified2018_typechangelog_iot+=1 
                    elif(aux_str == 'Vendor'):
                        cpes_lastmodified2018_typevendor_iot+=1
        else:
            cpes_lastmodified2018_iot+=1
            if(df_cpe_iot["cpes.refs.type"][r] == 'NONE'):
                cpes_lastmodified2018_typenone_iot+=1 
            elif(df_cpe_iot["cpes.refs.type"][r] == 'Version'):
                cpes_lastmodified2018_typeversion_iot+=1 
            elif(df_cpe_iot["cpes.refs.type"][r] == 'Product'):
                cpes_lastmodified2018_typeproduct_iot+=1 
            elif(df_cpe_iot["cpes.refs.type"][r] == 'Advisory'):
                cpes_lastmodified2018_typeadvisory_iot+=1 
            elif((df_cpe_iot["cpes.refs.type"][r] == 'Change Log') or(df_cpe_iot["cpes.refs.type"][r] == 'ChangeLog')):
                cpes_lastmodified2018_typechangelog_iot+=1
            elif(df_cpe_iot["cpes.refs.type"][r] == 'Vendor'):
                cpes_lastmodified2018_typevendor_iot+=1
                
                
                
                
print("*************************************ESTADÍSTICAS FECHA ULTIMA MODIFICACION/TIPO DE REFERENCIA DE CPE PARTE IOT*************************************")
print("\n")                 
                
total_modified_cpe_iot=cpes_lastmodified2023_iot+cpes_lastmodified2022_iot+cpes_lastmodified2021_iot+cpes_lastmodified2020_iot+cpes_lastmodified2019_iot+cpes_lastmodified2018_iot                
                
print("\n")
print(" DE UN TOTAL DE "+str(total_modified_cpe_iot)+" REFERENCIAS DE CPES , LAS ESTADISTICAS DE RELACION DE FECHA DE MODIFICACION Y TIPO DE REFERENCIA SON LAS SIGUIENTES:  \n")
print("\n")
print("      -    EN  "+str(cpes_lastmodified2023_iot)+" REFERENCIAS DE CPES LA FECHA DE ULTIMA MODIFICACION DEL CPE ES 2023. LAS ESTADÍSTICAS DE TIPO DE REFERENCIA SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(cpes_lastmodified2023_typeversion_iot)+" REFERENCIAS EL TIPO ES VERSION ")
print("            -    EN  "+str(cpes_lastmodified2023_typeproduct_iot)+" REFERENCIAS EL TIPO ES PRODUCTO ")
print("            -    EN  "+str(cpes_lastmodified2023_typeadvisory_iot)+" REFERENCIAS EL TIPO ES AVISO ")
print("            -    EN  "+str(cpes_lastmodified2023_typechangelog_iot)+" REFERENCIAS EL TIPO ES REGISTRO DE CAMBIO ")
print("            -    EN  "+str(cpes_lastmodified2023_typevendor_iot)+" REFERENCIAS EL TIPO ES VENDEDOR ")
print("            -    EN  "+str(cpes_lastmodified2023_typenone_iot)+" REFERENCIAS EL TIPO NO VIENE ESPECIFICADO ")
print("\n")
print("      -    EN  "+str(cpes_lastmodified2022_iot)+" REFERENCIAS DE CPES LA FECHA DE ULTIMA MODIFICACION DEL CPE ES 2022. LAS ESTADÍSTICAS DE TIPO DE REFERENCIA SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(cpes_lastmodified2022_typeversion_iot)+" REFERENCIAS EL TIPO ES VERSION ")
print("            -    EN  "+str(cpes_lastmodified2022_typeproduct_iot)+" REFERENCIAS EL TIPO ES PRODUCTO ")
print("            -    EN  "+str(cpes_lastmodified2022_typeadvisory_iot)+" REFERENCIAS EL TIPO ES AVISO ")
print("            -    EN  "+str(cpes_lastmodified2022_typechangelog_iot)+" REFERENCIAS EL TIPO ES REGISTRO DE CAMBIO ")
print("            -    EN  "+str(cpes_lastmodified2022_typevendor_iot)+" REFERENCIAS EL TIPO ES VENDEDOR ")
print("            -    EN  "+str(cpes_lastmodified2022_typenone_iot)+" REFERENCIAS EL TIPO NO VIENE ESPECIFICADO ")
print("\n")
print("      -    EN  "+str(cpes_lastmodified2021_iot)+" REFERENCIAS DE CPES LA FECHA DE ULTIMA MODIFICACION DEL CPE ES 2021. LAS ESTADÍSTICAS DE TIPO DE REFERENCIA SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(cpes_lastmodified2021_typeversion_iot)+" REFERENCIAS EL TIPO ES VERSION ")
print("            -    EN  "+str(cpes_lastmodified2021_typeproduct_iot)+" REFERENCIAS EL TIPO ES PRODUCTO ")
print("            -    EN  "+str(cpes_lastmodified2021_typeadvisory_iot)+" REFERENCIAS EL TIPO ES AVISO ")
print("            -    EN  "+str(cpes_lastmodified2021_typechangelog_iot)+" REFERENCIAS EL TIPO ES REGISTRO DE CAMBIO ")
print("            -    EN  "+str(cpes_lastmodified2021_typevendor_iot)+" REFERENCIAS EL TIPO ES VENDEDOR ")
print("            -    EN  "+str(cpes_lastmodified2021_typenone_iot)+" REFERENCIAS EL TIPO NO VIENE ESPECIFICADO ")
print("\n")
print("      -    EN  "+str(cpes_lastmodified2020_iot)+" REFERENCIAS DE CPES LA FECHA DE ULTIMA MODIFICACION DEL CPE ES 2020. LAS ESTADÍSTICAS DE TIPO DE REFERENCIA SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(cpes_lastmodified2020_typeversion_iot)+" REFERENCIAS EL TIPO ES VERSION ")
print("            -    EN  "+str(cpes_lastmodified2020_typeproduct_iot)+" REFERENCIAS EL TIPO ES PRODUCTO ")
print("            -    EN  "+str(cpes_lastmodified2020_typeadvisory_iot)+" REFERENCIAS EL TIPO ES AVISO ")
print("            -    EN  "+str(cpes_lastmodified2020_typechangelog_iot)+" REFERENCIAS EL TIPO ES REGISTRO DE CAMBIO ")
print("            -    EN  "+str(cpes_lastmodified2020_typevendor_iot)+" REFERENCIAS EL TIPO ES VENDEDOR ")
print("            -    EN  "+str(cpes_lastmodified2020_typenone_iot)+" REFERENCIAS EL TIPO NO VIENE ESPECIFICADO ")
print("\n")
print("      -    EN  "+str(cpes_lastmodified2019_iot)+" REFERENCIAS DE CPES LA FECHA DE ULTIMA MODIFICACION DEL CPE ES 2019. LAS ESTADÍSTICAS DE TIPO DE REFERENCIA SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(cpes_lastmodified2019_typeversion_iot)+" REFERENCIAS EL TIPO ES VERSION ")
print("            -    EN  "+str(cpes_lastmodified2019_typeproduct_iot)+" REFERENCIAS EL TIPO ES PRODUCTO ")
print("            -    EN  "+str(cpes_lastmodified2019_typeadvisory_iot)+" REFERENCIAS EL TIPO ES AVISO ")
print("            -    EN  "+str(cpes_lastmodified2019_typechangelog_iot)+" REFERENCIAS EL TIPO ES REGISTRO DE CAMBIO ")
print("            -    EN  "+str(cpes_lastmodified2019_typevendor_iot)+" REFERENCIAS EL TIPO ES VENDEDOR ")
print("            -    EN  "+str(cpes_lastmodified2019_typenone_iot)+" REFERENCIAS EL TIPO NO VIENE ESPECIFICADO ")
print("\n")
print("      -    EN  "+str(cpes_lastmodified2018_iot)+" REFERENCIAS DE CPES LA FECHA DE ULTIMA MODIFICACION DEL CPE ES 2018 O ANTERIOR. LAS ESTADÍSTICAS DE TIPO DE REFERENCIA SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(cpes_lastmodified2018_typeversion_iot)+" REFERENCIAS EL TIPO ES VERSION ")
print("            -    EN  "+str(cpes_lastmodified2018_typeproduct_iot)+" REFERENCIAS EL TIPO ES PRODUCTO ")
print("            -    EN  "+str(cpes_lastmodified2018_typeadvisory_iot)+" REFERENCIAS EL TIPO ES AVISO ")
print("            -    EN  "+str(cpes_lastmodified2018_typechangelog_iot)+" REFERENCIAS EL TIPO ES REGISTRO DE CAMBIO ")
print("            -    EN  "+str(cpes_lastmodified2018_typevendor_iot)+" REFERENCIAS EL TIPO ES VENDEDOR ")
print("            -    EN  "+str(cpes_lastmodified2018_typenone_iot)+" REFERENCIAS EL TIPO NO VIENE ESPECIFICADO ")
print("\n")





print("*************************************PORCENTAJES FECHA ULTIMA MODIFICACION/TIPO DE REFERENCIA DE CPE PARTE IOT*************************************")
print("\n")        
            
            
    
print("\n")
print(" DE UN TOTAL DE "+str(total_modified_cpe_iot)+" REFERENCIAS DE CPES , LOS PORCENTAJES DE RELACION DE FECHA DE MODIFICACION Y TIPO DE REFERENCIA SON LOS SIGUIENTES:  \n")
print("\n")
print("      -    EN EL "+str(float(((cpes_lastmodified2023_iot*100)/total_modified_cpe_iot)))+" % DE REFERENCIAS DE CPES LA FECHA DE ULTIMA MODIFICACION DEL CPE ES 2023. LOS PORCENTAJES DE TIPO DE REFERENCIA SON LOS SIGUIENTES:  \n")
print("\n")
print("            -    EN EL "+str(float(((cpes_lastmodified2023_typeversion_iot*100)/cpes_lastmodified2023_iot)))+" % DE REFERENCIAS EL TIPO ES VERSION  ")
print("            -    EN EL "+str(float(((cpes_lastmodified2023_typeproduct_iot*100)/cpes_lastmodified2023_iot)))+" % DE REFERENCIAS EL TIPO ES PRODUCTO ")
print("            -    EN EL "+str(float(((cpes_lastmodified2023_typeadvisory_iot*100)/cpes_lastmodified2023_iot)))+" % DE REFERENCIAS EL TIPO ES AVISO ")
print("            -    EN EL "+str(float(((cpes_lastmodified2023_typechangelog_iot*100)/cpes_lastmodified2023_iot)))+" % DE REFERENCIAS EL TIPO ES REGISTRO DE CAMBIO ")
print("            -    EN EL "+str(float(((cpes_lastmodified2023_typevendor_iot*100)/cpes_lastmodified2023_iot)))+" % DE REFERENCIAS EL TIPO ES VENDEDOR ")
print("            -    EN EL "+str(float(((cpes_lastmodified2023_typenone_iot*100)/cpes_lastmodified2023_iot)))+" % DE REFERENCIAS EL TIPO NO VIENE ESPECIFICADO ")
print("\n")
print("      -    EN EL "+str(float(((cpes_lastmodified2022_iot*100)/total_modified_cpe_iot)))+" % DE REFERENCIAS DE CPES LA FECHA DE ULTIMA MODIFICACION DEL CPE ES 2022. LOS PORCENTAJES DE TIPO DE REFERENCIA SON LOS SIGUIENTES:  \n")
print("\n")
print("            -    EN EL "+str(float(((cpes_lastmodified2022_typeversion_iot*100)/cpes_lastmodified2022_iot)))+" % DE REFERENCIAS EL TIPO ES VERSION  ")
print("            -    EN EL "+str(float(((cpes_lastmodified2022_typeproduct_iot*100)/cpes_lastmodified2022_iot)))+" % DE REFERENCIAS EL TIPO ES PRODUCTO ")
print("            -    EN EL "+str(float(((cpes_lastmodified2022_typeadvisory_iot*100)/cpes_lastmodified2022_iot)))+" % DE REFERENCIAS EL TIPO ES AVISO ")
print("            -    EN EL "+str(float(((cpes_lastmodified2022_typechangelog_iot*100)/cpes_lastmodified2022_iot)))+" % DE REFERENCIAS EL TIPO ES REGISTRO DE CAMBIO ")
print("            -    EN EL "+str(float(((cpes_lastmodified2022_typevendor_iot*100)/cpes_lastmodified2022_iot)))+" % DE REFERENCIAS EL TIPO ES VENDEDOR ")
print("            -    EN EL "+str(float(((cpes_lastmodified2022_typenone_iot*100)/cpes_lastmodified2022_iot)))+" % DE REFERENCIAS EL TIPO NO VIENE ESPECIFICADO ")
print("\n")
print("      -    EN EL "+str(float(((cpes_lastmodified2021_iot*100)/total_modified_cpe_iot)))+" % DE REFERENCIAS DE CPES LA FECHA DE ULTIMA MODIFICACION DEL CPE ES 2021. LOS PORCENTAJES DE TIPO DE REFERENCIA SON LOS SIGUIENTES:  \n")
print("\n")
print("            -    EN EL "+str(float(((cpes_lastmodified2021_typeversion_iot*100)/cpes_lastmodified2021_iot)))+" % DE REFERENCIAS EL TIPO ES VERSION  ")
print("            -    EN EL "+str(float(((cpes_lastmodified2021_typeproduct_iot*100)/cpes_lastmodified2021_iot)))+" % DE REFERENCIAS EL TIPO ES PRODUCTO ")
print("            -    EN EL "+str(float(((cpes_lastmodified2021_typeadvisory_iot*100)/cpes_lastmodified2021_iot)))+" % DE REFERENCIAS EL TIPO ES AVISO ")
print("            -    EN EL "+str(float(((cpes_lastmodified2021_typechangelog_iot*100)/cpes_lastmodified2021_iot)))+" % DE REFERENCIAS EL TIPO ES REGISTRO DE CAMBIO ")
print("            -    EN EL "+str(float(((cpes_lastmodified2021_typevendor_iot*100)/cpes_lastmodified2021_iot)))+" % DE REFERENCIAS EL TIPO ES VENDEDOR ")
print("            -    EN EL "+str(float(((cpes_lastmodified2021_typenone_iot*100)/cpes_lastmodified2021_iot)))+" % DE REFERENCIAS EL TIPO NO VIENE ESPECIFICADO ")
print("\n")
print("      -    EN EL "+str(float(((cpes_lastmodified2020_iot*100)/total_modified_cpe_iot)))+" % DE REFERENCIAS DE CPES LA FECHA DE ULTIMA MODIFICACION DEL CPE ES 2020. LOS PORCENTAJES DE TIPO DE REFERENCIA SON LOS SIGUIENTES:  \n")
print("\n")
print("            -    EN EL "+str(float(((cpes_lastmodified2020_typeversion_iot*100)/cpes_lastmodified2020_iot)))+" % DE REFERENCIAS EL TIPO ES VERSION  ")
print("            -    EN EL "+str(float(((cpes_lastmodified2020_typeproduct_iot*100)/cpes_lastmodified2020_iot)))+" % DE REFERENCIAS EL TIPO ES PRODUCTO ")
print("            -    EN EL "+str(float(((cpes_lastmodified2020_typeadvisory_iot*100)/cpes_lastmodified2020_iot)))+" % DE REFERENCIAS EL TIPO ES AVISO ")
print("            -    EN EL "+str(float(((cpes_lastmodified2020_typechangelog_iot*100)/cpes_lastmodified2020_iot)))+" % DE REFERENCIAS EL TIPO ES REGISTRO DE CAMBIO ")
print("            -    EN EL "+str(float(((cpes_lastmodified2020_typevendor_iot*100)/cpes_lastmodified2020_iot)))+" % DE REFERENCIAS EL TIPO ES VENDEDOR ")
print("            -    EN EL "+str(float(((cpes_lastmodified2020_typenone_iot*100)/cpes_lastmodified2020_iot)))+" % DE REFERENCIAS EL TIPO NO VIENE ESPECIFICADO ")
print("\n")
print("      -    EN EL "+str(float(((cpes_lastmodified2019_iot*100)/total_modified_cpe_iot)))+" % DE REFERENCIAS DE CPES LA FECHA DE ULTIMA MODIFICACION DEL CPE ES 2019. LOS PORCENTAJES DE TIPO DE REFERENCIA SON LOS SIGUIENTES:  \n")
print("\n")
print("            -    EN EL "+str(float(((cpes_lastmodified2019_typeversion_iot*100)/cpes_lastmodified2019_iot)))+" % DE REFERENCIAS EL TIPO ES VERSION  ")
print("            -    EN EL "+str(float(((cpes_lastmodified2019_typeproduct_iot*100)/cpes_lastmodified2019_iot)))+" % DE REFERENCIAS EL TIPO ES PRODUCTO ")
print("            -    EN EL "+str(float(((cpes_lastmodified2019_typeadvisory_iot*100)/cpes_lastmodified2019_iot)))+" % DE REFERENCIAS EL TIPO ES AVISO ")
print("            -    EN EL "+str(float(((cpes_lastmodified2019_typechangelog_iot*100)/cpes_lastmodified2019_iot)))+" % DE REFERENCIAS EL TIPO ES REGISTRO DE CAMBIO ")
print("            -    EN EL "+str(float(((cpes_lastmodified2019_typevendor_iot*100)/cpes_lastmodified2019_iot)))+" % DE REFERENCIAS EL TIPO ES VENDEDOR ")
print("            -    EN EL "+str(float(((cpes_lastmodified2019_typenone_iot*100)/cpes_lastmodified2019_iot)))+" % DE REFERENCIAS EL TIPO NO VIENE ESPECIFICADO ")
print("\n")
print("      -    EN EL "+str(float(((cpes_lastmodified2018_iot*100)/total_modified_cpe_iot)))+" % DE REFERENCIAS DE CPES LA FECHA DE ULTIMA MODIFICACION DEL CPE ES 2018 O ANTERIOR. LOS PORCENTAJES DE TIPO DE REFERENCIA SON LOS SIGUIENTES:  \n")
print("\n")
print("            -    EN EL "+str(float(((cpes_lastmodified2018_typeversion_iot*100)/cpes_lastmodified2018_iot)))+" % DE REFERENCIAS EL TIPO ES VERSION  ")
print("            -    EN EL "+str(float(((cpes_lastmodified2018_typeproduct_iot*100)/cpes_lastmodified2018_iot)))+" % DE REFERENCIAS EL TIPO ES PRODUCTO ")
print("            -    EN EL "+str(float(((cpes_lastmodified2018_typeadvisory_iot*100)/cpes_lastmodified2018_iot)))+" % DE REFERENCIAS EL TIPO ES AVISO ")
print("            -    EN EL "+str(float(((cpes_lastmodified2018_typechangelog_iot*100)/cpes_lastmodified2018_iot)))+" % DE REFERENCIAS EL TIPO ES REGISTRO DE CAMBIO ")
print("            -    EN EL "+str(float(((cpes_lastmodified2018_typevendor_iot*100)/cpes_lastmodified2018_iot)))+" % DE REFERENCIAS EL TIPO ES VENDEDOR ")
print("            -    EN EL "+str(float(((cpes_lastmodified2018_typenone_iot*100)/cpes_lastmodified2018_iot)))+" % DE REFERENCIAS EL TIPO NO VIENE ESPECIFICADO ")
print("\n")















print("*************************************FECHA DE ULTIMA MODIFICACIÓN CPE/TIPO DE REFERENCIA PARTE SMART HOME*************************************")
print("\n")
print("\n")

#Variables para almacenar el tipo de entrada segun el anio en el que fue modificado por ultima vez
cpes_lastmodified2023_typeversion_sh=0
cpes_lastmodified2023_typeproduct_sh=0
cpes_lastmodified2023_typeadvisory_sh=0
cpes_lastmodified2023_typechangelog_sh=0
cpes_lastmodified2023_typenone_sh=0
cpes_lastmodified2023_typevendor_sh=0
cpes_lastmodified2023_sh=0

cpes_lastmodified2022_typeversion_sh=0
cpes_lastmodified2022_typeproduct_sh=0
cpes_lastmodified2022_typeadvisory_sh=0
cpes_lastmodified2022_typechangelog_sh=0
cpes_lastmodified2022_typenone_sh=0
cpes_lastmodified2022_typevendor_sh=0
cpes_lastmodified2022_sh=0

cpes_lastmodified2021_typeversion_sh=0
cpes_lastmodified2021_typeproduct_sh=0
cpes_lastmodified2021_typeadvisory_sh=0
cpes_lastmodified2021_typechangelog_sh=0
cpes_lastmodified2021_typenone_sh=0
cpes_lastmodified2021_typevendor_sh=0
cpes_lastmodified2021_sh=0

cpes_lastmodified2020_typeversion_sh=0
cpes_lastmodified2020_typeproduct_sh=0
cpes_lastmodified2020_typeadvisory_sh=0
cpes_lastmodified2020_typechangelog_sh=0
cpes_lastmodified2020_typenone_sh=0
cpes_lastmodified2020_typevendor_sh=0
cpes_lastmodified2020_sh=0

cpes_lastmodified2019_typeversion_sh=0
cpes_lastmodified2019_typeproduct_sh=0
cpes_lastmodified2019_typeadvisory_sh=0
cpes_lastmodified2019_typechangelog_sh=0
cpes_lastmodified2019_typenone_sh=0
cpes_lastmodified2019_typevendor_sh=0
cpes_lastmodified2019_sh=0

cpes_lastmodified2018_typeversion_sh=0
cpes_lastmodified2018_typeproduct_sh=0
cpes_lastmodified2018_typeadvisory_sh=0
cpes_lastmodified2018_typechangelog_sh=0
cpes_lastmodified2018_typenone_sh=0
cpes_lastmodified2018_typevendor_sh=0
cpes_lastmodified2018_sh=0

#Recorro los valores de fecha de ultima modificacion
for r in range(0,len(df_cpe_sh["cpes.lastModifiedDate"])):
    str_anio_modifdate_cpe_sh=df_cpe_sh["cpes.lastModifiedDate"][r].split("-")
    anio_modifdate_cpe_sh=int(str_anio_modifdate_cpe_sh[0])
    if(anio_modifdate_cpe_sh >= 2023):
        #Compruebo si existen varios valores de tipo de entrada en una misma fila
        if('[' in df_cpe_sh["cpes.refs.type"][r]):
            aux=df_cpe_sh["cpes.refs.type"][r].split(",")
            for k in range(0,len(aux)):
                if(len(aux)>0):
                    #Recorro los valores de tipo de entrada para una misma fila
                    cpes_lastmodified2023_sh+=1
                    aux_str=aux[k].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
                    #Compruebo el tipo de entrada 
                    if(aux_str == 'NONE'):
                        cpes_lastmodified2023_typenone_sh+=1  
                    elif(aux_str == 'Version'):
                        cpes_lastmodified2023_typeversion_sh+=1  
                    elif(aux_str == 'Product'):
                        cpes_lastmodified2023_typeproduct_sh+=1  
                    elif(aux_str == 'Advisory'):
                        cpes_lastmodified2023_typeadvisory_sh+=1  
                    elif((aux_str == 'Change Log') or (aux_str == 'ChangeLog')):
                        cpes_lastmodified2023_typechangelog_sh+=1
                    elif(aux_str == 'Vendor'):
                        cpes_lastmodified2023_typevendor_sh+=1
        else:
            cpes_lastmodified2023_sh+=1
            if(df_cpe_sh["cpes.refs.type"][r] == 'NONE'):
                cpes_lastmodified2023_typenone_sh+=1 
            elif(df_cpe_sh["cpes.refs.type"][r] == 'Version'):
                cpes_lastmodified2023_typeversion_sh+=1 
            elif(df_cpe_sh["cpes.refs.type"][r] == 'Product'):
                cpes_lastmodified2023_typeproduct_sh+=1 
            elif(df_cpe_sh["cpes.refs.type"][r] == 'Advisory'):
                cpes_lastmodified2023_typeadvisory_sh+=1 
            elif((df_cpe_sh["cpes.refs.type"][r] == 'Change Log') or(df_cpe_sh["cpes.refs.type"][r] == 'ChangeLog')):
                cpes_lastmodified2023_typechangelog_sh+=1
            elif(df_cpe_sh["cpes.refs.type"][r] == 'Vendor'):
                cpes_lastmodified2023_typevendor_sh+=1
    elif(anio_modifdate_cpe_sh >= 2022):
        if('[' in df_cpe_sh["cpes.refs.type"][r]):
            aux=df_cpe_sh["cpes.refs.type"][r].split(",")
            for k in range(0,len(aux)):
                if(len(aux)>0):
                    cpes_lastmodified2022_sh+=1
                    aux_str=aux[k].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
                    if(aux_str == 'NONE'):
                        cpes_lastmodified2022_typenone_sh+=1  
                    elif(aux_str == 'Version'):
                        cpes_lastmodified2022_typeversion_sh+=1  
                    elif(aux_str == 'Product'):
                        cpes_lastmodified2022_typeproduct_sh+=1  
                    elif(aux_str == 'Advisory'):
                        cpes_lastmodified2022_typeadvisory_sh+=1  
                    elif((aux_str == 'Change Log') or (aux_str == 'ChangeLog')):
                        cpes_lastmodified2022_typechangelog_sh+=1
                    elif(aux_str == 'Vendor'):
                        cpes_lastmodified2022_typevendor_sh+=1
        else:
            cpes_lastmodified2022_sh+=1
            if(df_cpe_sh["cpes.refs.type"][r] == 'NONE'):
                cpes_lastmodified2022_typenone_sh+=1 
            elif(df_cpe_sh["cpes.refs.type"][r] == 'Version'):
                cpes_lastmodified2022_typeversion_sh+=1 
            elif(df_cpe_sh["cpes.refs.type"][r] == 'Product'):
                cpes_lastmodified2022_typeproduct_sh+=1 
            elif(df_cpe_sh["cpes.refs.type"][r] == 'Advisory'):
                cpes_lastmodified2022_typeadvisory_sh+=1 
            elif((df_cpe_sh["cpes.refs.type"][r] == 'Change Log') or(df_cpe_sh["cpes.refs.type"][r] == 'ChangeLog')):
                cpes_lastmodified2022_typechangelog_sh+=1
            elif(df_cpe_sh["cpes.refs.type"][r] == 'Vendor'):
                cpes_lastmodified2022_typevendor_sh+=1
    elif(anio_modifdate_cpe_sh >= 2021):
        if('[' in df_cpe_sh["cpes.refs.type"][r]):
            aux=df_cpe_sh["cpes.refs.type"][r].split(",")
            for k in range(0,len(aux)):
                if(len(aux)>0):
                    cpes_lastmodified2021_sh+=1
                    aux_str=aux[k].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
                    if(aux_str == 'NONE'):
                        cpes_lastmodified2021_typenone_sh+=1  
                    elif(aux_str == 'Version'):
                        cpes_lastmodified2021_typeversion_sh+=1  
                    elif(aux_str == 'Product'):
                        cpes_lastmodified2021_typeproduct_sh+=1  
                    elif(aux_str == 'Advisory'):
                        cpes_lastmodified2021_typeadvisory_sh+=1  
                    elif((aux_str == 'Change Log') or (aux_str == 'ChangeLog')):
                        cpes_lastmodified2021_typechangelog_sh+=1  
                    elif(aux_str == 'Vendor'):
                        cpes_lastmodified2022_typevendor_sh+=1
        else:
            cpes_lastmodified2021_sh+=1
            if(df_cpe_sh["cpes.refs.type"][r] == 'NONE'):
                cpes_lastmodified2021_typenone_sh+=1 
            elif(df_cpe_sh["cpes.refs.type"][r] == 'Version'):
                cpes_lastmodified2021_typeversion_sh+=1 
            elif(df_cpe_sh["cpes.refs.type"][r] == 'Product'):
                cpes_lastmodified2021_typeproduct_sh+=1 
            elif(df_cpe_sh["cpes.refs.type"][r] == 'Advisory'):
                cpes_lastmodified2021_typeadvisory_sh+=1 
            elif((df_cpe_sh["cpes.refs.type"][r] == 'Change Log') or(df_cpe_sh["cpes.refs.type"][r] == 'ChangeLog')):
                cpes_lastmodified2021_typechangelog_sh+=1
            elif(df_cpe_sh["cpes.refs.type"][r] == 'Vendor'):
                cpes_lastmodified2021_typevendor_sh+=1
    elif(anio_modifdate_cpe_sh >= 2020):
        if('[' in df_cpe_sh["cpes.refs.type"][r]):
            aux=df_cpe_sh["cpes.refs.type"][r].split(",")
            for k in range(0,len(aux)):
                if(len(aux)>0):
                    cpes_lastmodified2020_sh+=1
                    aux_str=aux[k].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
                    if(aux_str == 'NONE'):
                        cpes_lastmodified2020_typenone_sh+=1  
                    elif(aux_str == 'Version'):
                        cpes_lastmodified2020_typeversion_sh+=1  
                    elif(aux_str == 'Product'):
                        cpes_lastmodified2020_typeproduct_sh+=1  
                    elif(aux_str == 'Advisory'):
                        cpes_lastmodified2020_typeadvisory_sh+=1  
                    elif((aux_str == 'Change Log') or (aux_str == 'ChangeLog')):
                        cpes_lastmodified2020_typechangelog_sh+=1 
                    elif(aux_str == 'Vendor'):
                        cpes_lastmodified2020_typevendor_sh+=1
        else:
            cpes_lastmodified2020_sh+=1
            if(df_cpe_sh["cpes.refs.type"][r] == 'NONE'):
                cpes_lastmodified2020_typenone_sh+=1 
            elif(df_cpe_sh["cpes.refs.type"][r] == 'Version'):
                cpes_lastmodified2020_typeversion_sh+=1 
            elif(df_cpe_sh["cpes.refs.type"][r] == 'Product'):
                cpes_lastmodified2020_typeproduct_sh+=1 
            elif(df_cpe_sh["cpes.refs.type"][r] == 'Advisory'):
                cpes_lastmodified2020_typeadvisory_sh+=1 
            elif((df_cpe_sh["cpes.refs.type"][r] == 'Change Log') or(df_cpe_sh["cpes.refs.type"][r] == 'ChangeLog')):
                cpes_lastmodified2020_typechangelog_sh+=1
            elif(df_cpe_sh["cpes.refs.type"][r] == 'Vendor'):
                cpes_lastmodified2020_typevendor_sh+=1
    elif(anio_modifdate_cpe_sh >= 2019):
        if('[' in df_cpe_sh["cpes.refs.type"][r]):
            aux=df_cpe_sh["cpes.refs.type"][r].split(",")
            for k in range(0,len(aux)):
                if(len(aux)>0):
                    cpes_lastmodified2019_sh+=1
                    aux_str=aux[k].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
                    if(aux_str == 'NONE'):
                        cpes_lastmodified2019_typenone_sh+=1  
                    elif(aux_str == 'Version'):
                        cpes_lastmodified2019_typeversion_sh+=1  
                    elif(aux_str == 'Product'):
                        cpes_lastmodified2019_typeproduct_sh+=1  
                    elif(aux_str == 'Advisory'):
                        cpes_lastmodified2019_typeadvisory_sh+=1  
                    elif((aux_str == 'Change Log') or (aux_str == 'ChangeLog')):
                        cpes_lastmodified2019_typechangelog_sh+=1 
                    elif(aux_str == 'Vendor'):
                        cpes_lastmodified2019_typevendor_sh+=1
        else:
            cpes_lastmodified2019_sh+=1
            if(df_cpe_sh["cpes.refs.type"][r] == 'NONE'):
                cpes_lastmodified2019_typenone_sh+=1 
            elif(df_cpe_sh["cpes.refs.type"][r] == 'Version'):
                cpes_lastmodified2019_typeversion_sh+=1 
            elif(df_cpe_sh["cpes.refs.type"][r] == 'Product'):
                cpes_lastmodified2019_typeproduct_sh+=1 
            elif(df_cpe_sh["cpes.refs.type"][r] == 'Advisory'):
                cpes_lastmodified2019_typeadvisory_sh+=1 
            elif((df_cpe_sh["cpes.refs.type"][r] == 'Change Log') or(df_cpe_sh["cpes.refs.type"][r] == 'ChangeLog')):
                cpes_lastmodified2019_typechangelog_sh+=1
            elif(df_cpe_sh["cpes.refs.type"][r] == 'Vendor'):
                cpes_lastmodified2019_typevendor_sh+=1
    else:
        if('[' in df_cpe_sh["cpes.refs.type"][r]):
            aux=df_cpe_sh["cpes.refs.type"][r].split(",")
            for k in range(0,len(aux)):
                if(len(aux)>0):
                    cpes_lastmodified2018_sh+=1
                    aux_str=aux[k].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
                    if(aux_str == 'NONE'):
                        cpes_lastmodified2018_typenone_sh+=1  
                    elif(aux_str == 'Version'):
                        cpes_lastmodified2018_typeversion_sh+=1  
                    elif(aux_str == 'Product'):
                        cpes_lastmodified2018_typeproduct_sh+=1  
                    elif(aux_str == 'Advisory'):
                        cpes_lastmodified2018_typeadvisory_sh+=1  
                    elif((aux_str == 'Change Log') or (aux_str == 'ChangeLog')):
                        cpes_lastmodified2018_typechangelog_sh+=1 
                    elif(aux_str == 'Vendor'):
                        cpes_lastmodified2018_typevendor_sh+=1
        else:
            cpes_lastmodified2018_sh+=1
            if(df_cpe_sh["cpes.refs.type"][r] == 'NONE'):
                cpes_lastmodified2018_typenone_sh+=1 
            elif(df_cpe_sh["cpes.refs.type"][r] == 'Version'):
                cpes_lastmodified2018_typeversion_sh+=1 
            elif(df_cpe_sh["cpes.refs.type"][r] == 'Product'):
                cpes_lastmodified2018_typeproduct_sh+=1 
            elif(df_cpe_sh["cpes.refs.type"][r] == 'Advisory'):
                cpes_lastmodified2018_typeadvisory_sh+=1 
            elif((df_cpe_sh["cpes.refs.type"][r] == 'Change Log') or(df_cpe_sh["cpes.refs.type"][r] == 'ChangeLog')):
                cpes_lastmodified2018_typechangelog_sh+=1
            elif(df_cpe_sh["cpes.refs.type"][r] == 'Vendor'):
                cpes_lastmodified2018_typevendor_sh+=1
                
                
                
                
print("*************************************ESTADÍSTICAS FECHA ULTIMA MODIFICACION/TIPO DE REFERENCIA DE CPE PARTE SMART HOME*************************************")
print("\n")                 
                
total_modified_cpe_sh=cpes_lastmodified2023_sh+cpes_lastmodified2022_sh+cpes_lastmodified2021_sh+cpes_lastmodified2020_sh+cpes_lastmodified2019_sh+cpes_lastmodified2018_sh                
                
print("\n")
print(" DE UN TOTAL DE "+str(total_modified_cpe_sh)+" REFERENCIAS DE CPES , LAS ESTADISTICAS DE RELACION DE FECHA DE MODIFICACION Y TIPO DE REFERENCIA SON LAS SIGUIENTES:  \n")
print("\n")
print("      -    EN  "+str(cpes_lastmodified2023_sh)+" REFERENCIAS DE CPES LA FECHA DE ULTIMA MODIFICACION DEL CPE ES 2023. LAS ESTADÍSTICAS DE TIPO DE REFERENCIA SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(cpes_lastmodified2023_typeversion_sh)+" REFERENCIAS EL TIPO ES VERSION ")
print("            -    EN  "+str(cpes_lastmodified2023_typeproduct_sh)+" REFERENCIAS EL TIPO ES PRODUCTO ")
print("            -    EN  "+str(cpes_lastmodified2023_typeadvisory_sh)+" REFERENCIAS EL TIPO ES AVISO ")
print("            -    EN  "+str(cpes_lastmodified2023_typechangelog_sh)+" REFERENCIAS EL TIPO ES REGISTRO DE CAMBIO ")
print("            -    EN  "+str(cpes_lastmodified2023_typevendor_sh)+" REFERENCIAS EL TIPO ES VENDEDOR ")
print("            -    EN  "+str(cpes_lastmodified2023_typenone_sh)+" REFERENCIAS EL TIPO NO VIENE ESPECIFICADO ")
print("\n")
print("      -    EN  "+str(cpes_lastmodified2022_sh)+" REFERENCIAS DE CPES LA FECHA DE ULTIMA MODIFICACION DEL CPE ES 2022. LAS ESTADÍSTICAS DE TIPO DE REFERENCIA SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(cpes_lastmodified2022_typeversion_sh)+" REFERENCIAS EL TIPO ES VERSION ")
print("            -    EN  "+str(cpes_lastmodified2022_typeproduct_sh)+" REFERENCIAS EL TIPO ES PRODUCTO ")
print("            -    EN  "+str(cpes_lastmodified2022_typeadvisory_sh)+" REFERENCIAS EL TIPO ES AVISO ")
print("            -    EN  "+str(cpes_lastmodified2022_typechangelog_sh)+" REFERENCIAS EL TIPO ES REGISTRO DE CAMBIO ")
print("            -    EN  "+str(cpes_lastmodified2022_typevendor_sh)+" REFERENCIAS EL TIPO ES VENDEDOR ")
print("            -    EN  "+str(cpes_lastmodified2022_typenone_sh)+" REFERENCIAS EL TIPO NO VIENE ESPECIFICADO ")
print("\n")
print("      -    EN  "+str(cpes_lastmodified2021_sh)+" REFERENCIAS DE CPES LA FECHA DE ULTIMA MODIFICACION DEL CPE ES 2021. LAS ESTADÍSTICAS DE TIPO DE REFERENCIA SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(cpes_lastmodified2021_typeversion_sh)+" REFERENCIAS EL TIPO ES VERSION ")
print("            -    EN  "+str(cpes_lastmodified2021_typeproduct_sh)+" REFERENCIAS EL TIPO ES PRODUCTO ")
print("            -    EN  "+str(cpes_lastmodified2021_typeadvisory_sh)+" REFERENCIAS EL TIPO ES AVISO ")
print("            -    EN  "+str(cpes_lastmodified2021_typechangelog_sh)+" REFERENCIAS EL TIPO ES REGISTRO DE CAMBIO ")
print("            -    EN  "+str(cpes_lastmodified2021_typevendor_sh)+" REFERENCIAS EL TIPO ES VENDEDOR ")
print("            -    EN  "+str(cpes_lastmodified2021_typenone_sh)+" REFERENCIAS EL TIPO NO VIENE ESPECIFICADO ")
print("\n")
print("      -    EN  "+str(cpes_lastmodified2020_sh)+" REFERENCIAS DE CPES LA FECHA DE ULTIMA MODIFICACION DEL CPE ES 2020. LAS ESTADÍSTICAS DE TIPO DE REFERENCIA SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(cpes_lastmodified2020_typeversion_sh)+" REFERENCIAS EL TIPO ES VERSION ")
print("            -    EN  "+str(cpes_lastmodified2020_typeproduct_sh)+" REFERENCIAS EL TIPO ES PRODUCTO ")
print("            -    EN  "+str(cpes_lastmodified2020_typeadvisory_sh)+" REFERENCIAS EL TIPO ES AVISO ")
print("            -    EN  "+str(cpes_lastmodified2020_typechangelog_sh)+" REFERENCIAS EL TIPO ES REGISTRO DE CAMBIO ")
print("            -    EN  "+str(cpes_lastmodified2020_typevendor_sh)+" REFERENCIAS EL TIPO ES VENDEDOR ")
print("            -    EN  "+str(cpes_lastmodified2020_typenone_sh)+" REFERENCIAS EL TIPO NO VIENE ESPECIFICADO ")
print("\n")
print("      -    EN  "+str(cpes_lastmodified2019_sh)+" REFERENCIAS DE CPES LA FECHA DE ULTIMA MODIFICACION DEL CPE ES 2019. LAS ESTADÍSTICAS DE TIPO DE REFERENCIA SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(cpes_lastmodified2019_typeversion_sh)+" REFERENCIAS EL TIPO ES VERSION ")
print("            -    EN  "+str(cpes_lastmodified2019_typeproduct_sh)+" REFERENCIAS EL TIPO ES PRODUCTO ")
print("            -    EN  "+str(cpes_lastmodified2019_typeadvisory_sh)+" REFERENCIAS EL TIPO ES AVISO ")
print("            -    EN  "+str(cpes_lastmodified2019_typechangelog_sh)+" REFERENCIAS EL TIPO ES REGISTRO DE CAMBIO ")
print("            -    EN  "+str(cpes_lastmodified2019_typevendor_sh)+" REFERENCIAS EL TIPO ES VENDEDOR ")
print("            -    EN  "+str(cpes_lastmodified2019_typenone_sh)+" REFERENCIAS EL TIPO NO VIENE ESPECIFICADO ")
print("\n")
print("      -    EN  "+str(cpes_lastmodified2018_sh)+" REFERENCIAS DE CPES LA FECHA DE ULTIMA MODIFICACION DEL CPE ES 2018 O ANTERIOR. LAS ESTADÍSTICAS DE TIPO DE REFERENCIA SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(cpes_lastmodified2018_typeversion_sh)+" REFERENCIAS EL TIPO ES VERSION ")
print("            -    EN  "+str(cpes_lastmodified2018_typeproduct_sh)+" REFERENCIAS EL TIPO ES PRODUCTO ")
print("            -    EN  "+str(cpes_lastmodified2018_typeadvisory_sh)+" REFERENCIAS EL TIPO ES AVISO ")
print("            -    EN  "+str(cpes_lastmodified2018_typechangelog_sh)+" REFERENCIAS EL TIPO ES REGISTRO DE CAMBIO ")
print("            -    EN  "+str(cpes_lastmodified2018_typevendor_sh)+" REFERENCIAS EL TIPO ES VENDEDOR ")
print("            -    EN  "+str(cpes_lastmodified2018_typenone_sh)+" REFERENCIAS EL TIPO NO VIENE ESPECIFICADO ")
print("\n")





print("*************************************PORCENTAJES FECHA ULTIMA MODIFICACION/TIPO DE REFERENCIA DE CPE PARTE SMART HOME*************************************")
print("\n")        
            
            
    
print("\n")
print(" DE UN TOTAL DE "+str(total_modified_cpe_sh)+" REFERENCIAS DE CPES , LOS PORCENTAJES DE RELACION DE FECHA DE MODIFICACION Y TIPO DE REFERENCIA SON LOS SIGUIENTES:  \n")
print("\n")
if(cpes_lastmodified2023_sh>0):
    print("      -    EN EL "+str(float(((cpes_lastmodified2023_sh*100)/total_modified_cpe_sh)))+" % DE REFERENCIAS DE CPES LA FECHA DE ULTIMA MODIFICACION DEL CPE ES 2023. LOS PORCENTAJES DE TIPO DE REFERENCIA SON LOS SIGUIENTES:  \n")
    print("\n")
    print("            -    EN EL "+str(float(((cpes_lastmodified2023_typeversion_sh*100)/cpes_lastmodified2023_sh)))+" % DE REFERENCIAS EL TIPO ES VERSION  ")
    print("            -    EN EL "+str(float(((cpes_lastmodified2023_typeproduct_sh*100)/cpes_lastmodified2023_sh)))+" % DE REFERENCIAS EL TIPO ES PRODUCTO ")
    print("            -    EN EL "+str(float(((cpes_lastmodified2023_typeadvisory_sh*100)/cpes_lastmodified2023_sh)))+" % DE REFERENCIAS EL TIPO ES AVISO ")
    print("            -    EN EL "+str(float(((cpes_lastmodified2023_typechangelog_sh*100)/cpes_lastmodified2023_sh)))+" % DE REFERENCIAS EL TIPO ES REGISTRO DE CAMBIO ")
    print("            -    EN EL "+str(float(((cpes_lastmodified2023_typevendor_sh*100)/cpes_lastmodified2023_sh)))+" % DE REFERENCIAS EL TIPO ES VENDEDOR ")
    print("            -    EN EL "+str(float(((cpes_lastmodified2023_typenone_sh*100)/cpes_lastmodified2023_sh)))+" % DE REFERENCIAS EL TIPO NO VIENE ESPECIFICADO ")
    print("\n")
if(cpes_lastmodified2022_sh>0):
    print("      -    EN EL "+str(float(((cpes_lastmodified2022_sh*100)/total_modified_cpe_sh)))+" % DE REFERENCIAS DE CPES LA FECHA DE ULTIMA MODIFICACION DEL CPE ES 2022. LOS PORCENTAJES DE TIPO DE REFERENCIA SON LOS SIGUIENTES:  \n")
    print("\n")
    print("            -    EN EL "+str(float(((cpes_lastmodified2022_typeversion_sh*100)/cpes_lastmodified2022_sh)))+" % DE REFERENCIAS EL TIPO ES VERSION  ")
    print("            -    EN EL "+str(float(((cpes_lastmodified2022_typeproduct_sh*100)/cpes_lastmodified2022_sh)))+" % DE REFERENCIAS EL TIPO ES PRODUCTO ")
    print("            -    EN EL "+str(float(((cpes_lastmodified2022_typeadvisory_sh*100)/cpes_lastmodified2022_sh)))+" % DE REFERENCIAS EL TIPO ES AVISO ")
    print("            -    EN EL "+str(float(((cpes_lastmodified2022_typechangelog_sh*100)/cpes_lastmodified2022_sh)))+" % DE REFERENCIAS EL TIPO ES REGISTRO DE CAMBIO ")
    print("            -    EN EL "+str(float(((cpes_lastmodified2022_typevendor_sh*100)/cpes_lastmodified2022_sh)))+" % DE REFERENCIAS EL TIPO ES VENDEDOR ")
    print("            -    EN EL "+str(float(((cpes_lastmodified2022_typenone_sh*100)/cpes_lastmodified2022_sh)))+" % DE REFERENCIAS EL TIPO NO VIENE ESPECIFICADO ")
    print("\n")
if(cpes_lastmodified2021_sh>0):
    print("      -    EN EL "+str(float(((cpes_lastmodified2021_sh*100)/total_modified_cpe_sh)))+" % DE REFERENCIAS DE CPES LA FECHA DE ULTIMA MODIFICACION DEL CPE ES 2021. LOS PORCENTAJES DE TIPO DE REFERENCIA SON LOS SIGUIENTES:  \n")
    print("\n")
    print("            -    EN EL "+str(float(((cpes_lastmodified2021_typeversion_sh*100)/cpes_lastmodified2021_sh)))+" % DE REFERENCIAS EL TIPO ES VERSION  ")
    print("            -    EN EL "+str(float(((cpes_lastmodified2021_typeproduct_sh*100)/cpes_lastmodified2021_sh)))+" % DE REFERENCIAS EL TIPO ES PRODUCTO ")
    print("            -    EN EL "+str(float(((cpes_lastmodified2021_typeadvisory_sh*100)/cpes_lastmodified2021_sh)))+" % DE REFERENCIAS EL TIPO ES AVISO ")
    print("            -    EN EL "+str(float(((cpes_lastmodified2021_typechangelog_sh*100)/cpes_lastmodified2021_sh)))+" % DE REFERENCIAS EL TIPO ES REGISTRO DE CAMBIO ")
    print("            -    EN EL "+str(float(((cpes_lastmodified2021_typevendor_sh*100)/cpes_lastmodified2021_sh)))+" % DE REFERENCIAS EL TIPO ES VENDEDOR ")
    print("            -    EN EL "+str(float(((cpes_lastmodified2021_typenone_sh*100)/cpes_lastmodified2021_sh)))+" % DE REFERENCIAS EL TIPO NO VIENE ESPECIFICADO ")
    print("\n")
if(cpes_lastmodified2020_sh>0):
    print("      -    EN EL "+str(float(((cpes_lastmodified2020_sh*100)/total_modified_cpe_sh)))+" % DE REFERENCIAS DE CPES LA FECHA DE ULTIMA MODIFICACION DEL CPE ES 2020. LOS PORCENTAJES DE TIPO DE REFERENCIA SON LOS SIGUIENTES:  \n")
    print("\n")
    print("            -    EN EL "+str(float(((cpes_lastmodified2020_typeversion_sh*100)/cpes_lastmodified2020_sh)))+" % DE REFERENCIAS EL TIPO ES VERSION  ")
    print("            -    EN EL "+str(float(((cpes_lastmodified2020_typeproduct_sh*100)/cpes_lastmodified2020_sh)))+" % DE REFERENCIAS EL TIPO ES PRODUCTO ")
    print("            -    EN EL "+str(float(((cpes_lastmodified2020_typeadvisory_sh*100)/cpes_lastmodified2020_sh)))+" % DE REFERENCIAS EL TIPO ES AVISO ")
    print("            -    EN EL "+str(float(((cpes_lastmodified2020_typechangelog_sh*100)/cpes_lastmodified2020_sh)))+" % DE REFERENCIAS EL TIPO ES REGISTRO DE CAMBIO ")
    print("            -    EN EL "+str(float(((cpes_lastmodified2020_typevendor_sh*100)/cpes_lastmodified2020_sh)))+" % DE REFERENCIAS EL TIPO ES VENDEDOR ")
    print("            -    EN EL "+str(float(((cpes_lastmodified2020_typenone_sh*100)/cpes_lastmodified2020_sh)))+" % DE REFERENCIAS EL TIPO NO VIENE ESPECIFICADO ")
    print("\n")
if(cpes_lastmodified2019_sh>0):
    print("      -    EN EL "+str(float(((cpes_lastmodified2019_sh*100)/total_modified_cpe_sh)))+" % DE REFERENCIAS DE CPES LA FECHA DE ULTIMA MODIFICACION DEL CPE ES 2019. LOS PORCENTAJES DE TIPO DE REFERENCIA SON LOS SIGUIENTES:  \n")
    print("\n")
    print("            -    EN EL "+str(float(((cpes_lastmodified2019_typeversion_sh*100)/cpes_lastmodified2019_sh)))+" % DE REFERENCIAS EL TIPO ES VERSION  ")
    print("            -    EN EL "+str(float(((cpes_lastmodified2019_typeproduct_sh*100)/cpes_lastmodified2019_sh)))+" % DE REFERENCIAS EL TIPO ES PRODUCTO ")
    print("            -    EN EL "+str(float(((cpes_lastmodified2019_typeadvisory_sh*100)/cpes_lastmodified2019_sh)))+" % DE REFERENCIAS EL TIPO ES AVISO ")
    print("            -    EN EL "+str(float(((cpes_lastmodified2019_typechangelog_sh*100)/cpes_lastmodified2019_sh)))+" % DE REFERENCIAS EL TIPO ES REGISTRO DE CAMBIO ")
    print("            -    EN EL "+str(float(((cpes_lastmodified2019_typevendor_sh*100)/cpes_lastmodified2019_sh)))+" % DE REFERENCIAS EL TIPO ES VENDEDOR ")
    print("            -    EN EL "+str(float(((cpes_lastmodified2019_typenone_sh*100)/cpes_lastmodified2019_sh)))+" % DE REFERENCIAS EL TIPO NO VIENE ESPECIFICADO ")
    print("\n")
if(cpes_lastmodified2018_sh>0):
    print("      -    EN EL "+str(float(((cpes_lastmodified2018_sh*100)/total_modified_cpe_sh)))+" % DE REFERENCIAS DE CPES LA FECHA DE ULTIMA MODIFICACION DEL CPE ES 2018 O ANTERIOR. LOS PORCENTAJES DE TIPO DE REFERENCIA SON LOS SIGUIENTES:  \n")
    print("\n")
    print("            -    EN EL "+str(float(((cpes_lastmodified2018_typeversion_sh*100)/cpes_lastmodified2018_sh)))+" % DE REFERENCIAS EL TIPO ES VERSION  ")
    print("            -    EN EL "+str(float(((cpes_lastmodified2018_typeproduct_sh*100)/cpes_lastmodified2018_sh)))+" % DE REFERENCIAS EL TIPO ES PRODUCTO ")
    print("            -    EN EL "+str(float(((cpes_lastmodified2018_typeadvisory_sh*100)/cpes_lastmodified2018_sh)))+" % DE REFERENCIAS EL TIPO ES AVISO ")
    print("            -    EN EL "+str(float(((cpes_lastmodified2018_typechangelog_sh*100)/cpes_lastmodified2018_sh)))+" % DE REFERENCIAS EL TIPO ES REGISTRO DE CAMBIO ")
    print("            -    EN EL "+str(float(((cpes_lastmodified2018_typevendor_sh*100)/cpes_lastmodified2018_sh)))+" % DE REFERENCIAS EL TIPO ES VENDEDOR ")
    print("            -    EN EL "+str(float(((cpes_lastmodified2018_typenone_sh*100)/cpes_lastmodified2018_sh)))+" % DE REFERENCIAS EL TIPO NO VIENE ESPECIFICADO ")
    print("\n")





print("*************************************ESTADÍSTICAS FECHA ULTIMA MODIFICACION/TIPO DE REFERENCIA DE CPE PARTE IOT Y SMART HOME CONJUNTAS*************************************")
print("\n")                 
                                
print("\n")
print(" DE UN TOTAL DE "+str(total_modified_cpe_sh+total_modified_cpe_iot)+" REFERENCIAS DE CPES , LAS ESTADISTICAS DE RELACION DE FECHA DE MODIFICACION Y TIPO DE REFERENCIA SON LAS SIGUIENTES:  \n")
print("\n")
print("      -    EN  "+str(cpes_lastmodified2023_sh+cpes_lastmodified2023_iot)+" REFERENCIAS DE CPES LA FECHA DE ULTIMA MODIFICACION DEL CPE ES 2023. LAS ESTADÍSTICAS DE TIPO DE REFERENCIA SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(cpes_lastmodified2023_typeversion_sh+cpes_lastmodified2023_typeversion_iot)+" REFERENCIAS EL TIPO ES VERSION ")
print("            -    EN  "+str(cpes_lastmodified2023_typeproduct_sh+cpes_lastmodified2023_typeproduct_iot)+" REFERENCIAS EL TIPO ES PRODUCTO ")
print("            -    EN  "+str(cpes_lastmodified2023_typeadvisory_sh+cpes_lastmodified2023_typeadvisory_iot)+" REFERENCIAS EL TIPO ES AVISO ")
print("            -    EN  "+str(cpes_lastmodified2023_typechangelog_sh+cpes_lastmodified2023_typechangelog_iot)+" REFERENCIAS EL TIPO ES REGISTRO DE CAMBIO ")
print("            -    EN  "+str(cpes_lastmodified2023_typevendor_sh+cpes_lastmodified2023_typevendor_iot)+" REFERENCIAS EL TIPO ES VENDEDOR ")
print("            -    EN  "+str(cpes_lastmodified2023_typenone_sh+cpes_lastmodified2023_typenone_iot)+" REFERENCIAS EL TIPO NO VIENE ESPECIFICADO ")
print("\n")
print("      -    EN  "+str(cpes_lastmodified2022_sh+cpes_lastmodified2022_iot)+" REFERENCIAS DE CPES LA FECHA DE ULTIMA MODIFICACION DEL CPE ES 2022. LAS ESTADÍSTICAS DE TIPO DE REFERENCIA SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(cpes_lastmodified2022_typeversion_sh+cpes_lastmodified2022_typeversion_iot)+" REFERENCIAS EL TIPO ES VERSION ")
print("            -    EN  "+str(cpes_lastmodified2022_typeproduct_sh+cpes_lastmodified2022_typeproduct_iot)+" REFERENCIAS EL TIPO ES PRODUCTO ")
print("            -    EN  "+str(cpes_lastmodified2022_typeadvisory_sh+cpes_lastmodified2022_typeadvisory_iot)+" REFERENCIAS EL TIPO ES AVISO ")
print("            -    EN  "+str(cpes_lastmodified2022_typechangelog_sh+cpes_lastmodified2022_typechangelog_iot)+" REFERENCIAS EL TIPO ES REGISTRO DE CAMBIO ")
print("            -    EN  "+str(cpes_lastmodified2022_typevendor_sh+cpes_lastmodified2022_typevendor_iot)+" REFERENCIAS EL TIPO ES VENDEDOR ")
print("            -    EN  "+str(cpes_lastmodified2022_typenone_sh+cpes_lastmodified2022_typenone_iot)+" REFERENCIAS EL TIPO NO VIENE ESPECIFICADO ")
print("\n")
print("      -    EN  "+str(cpes_lastmodified2021_sh+cpes_lastmodified2021_iot)+" REFERENCIAS DE CPES LA FECHA DE ULTIMA MODIFICACION DEL CPE ES 2021. LAS ESTADÍSTICAS DE TIPO DE REFERENCIA SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(cpes_lastmodified2021_typeversion_sh+cpes_lastmodified2021_typeversion_iot)+" REFERENCIAS EL TIPO ES VERSION ")
print("            -    EN  "+str(cpes_lastmodified2021_typeproduct_sh+cpes_lastmodified2021_typeproduct_iot)+" REFERENCIAS EL TIPO ES PRODUCTO ")
print("            -    EN  "+str(cpes_lastmodified2021_typeadvisory_sh+cpes_lastmodified2021_typeadvisory_iot)+" REFERENCIAS EL TIPO ES AVISO ")
print("            -    EN  "+str(cpes_lastmodified2021_typechangelog_sh+cpes_lastmodified2021_typechangelog_iot)+" REFERENCIAS EL TIPO ES REGISTRO DE CAMBIO ")
print("            -    EN  "+str(cpes_lastmodified2021_typevendor_sh+cpes_lastmodified2021_typevendor_iot)+" REFERENCIAS EL TIPO ES VENDEDOR ")
print("            -    EN  "+str(cpes_lastmodified2021_typenone_sh+cpes_lastmodified2021_typenone_iot)+" REFERENCIAS EL TIPO NO VIENE ESPECIFICADO ")
print("\n")
print("      -    EN  "+str(cpes_lastmodified2020_sh+cpes_lastmodified2020_iot)+" REFERENCIAS DE CPES LA FECHA DE ULTIMA MODIFICACION DEL CPE ES 2020. LAS ESTADÍSTICAS DE TIPO DE REFERENCIA SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(cpes_lastmodified2020_typeversion_sh+cpes_lastmodified2020_typeversion_iot)+" REFERENCIAS EL TIPO ES VERSION ")
print("            -    EN  "+str(cpes_lastmodified2020_typeproduct_sh+cpes_lastmodified2020_typeproduct_iot)+" REFERENCIAS EL TIPO ES PRODUCTO ")
print("            -    EN  "+str(cpes_lastmodified2020_typeadvisory_sh+cpes_lastmodified2020_typeadvisory_iot)+" REFERENCIAS EL TIPO ES AVISO ")
print("            -    EN  "+str(cpes_lastmodified2020_typechangelog_sh+cpes_lastmodified2020_typechangelog_iot)+" REFERENCIAS EL TIPO ES REGISTRO DE CAMBIO ")
print("            -    EN  "+str(cpes_lastmodified2020_typevendor_sh+cpes_lastmodified2020_typevendor_iot)+" REFERENCIAS EL TIPO ES VENDEDOR ")
print("            -    EN  "+str(cpes_lastmodified2020_typenone_sh+cpes_lastmodified2020_typenone_iot)+" REFERENCIAS EL TIPO NO VIENE ESPECIFICADO ")
print("\n")
print("      -    EN  "+str(cpes_lastmodified2019_sh+cpes_lastmodified2019_iot)+" REFERENCIAS DE CPES LA FECHA DE ULTIMA MODIFICACION DEL CPE ES 2019. LAS ESTADÍSTICAS DE TIPO DE REFERENCIA SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(cpes_lastmodified2019_typeversion_sh+cpes_lastmodified2019_typeversion_iot)+" REFERENCIAS EL TIPO ES VERSION ")
print("            -    EN  "+str(cpes_lastmodified2019_typeproduct_sh+cpes_lastmodified2019_typeproduct_iot)+" REFERENCIAS EL TIPO ES PRODUCTO ")
print("            -    EN  "+str(cpes_lastmodified2019_typeadvisory_sh+cpes_lastmodified2019_typeadvisory_iot)+" REFERENCIAS EL TIPO ES AVISO ")
print("            -    EN  "+str(cpes_lastmodified2019_typechangelog_sh+cpes_lastmodified2019_typechangelog_iot)+" REFERENCIAS EL TIPO ES REGISTRO DE CAMBIO ")
print("            -    EN  "+str(cpes_lastmodified2019_typevendor_sh+cpes_lastmodified2019_typevendor_iot)+" REFERENCIAS EL TIPO ES VENDEDOR ")
print("            -    EN  "+str(cpes_lastmodified2019_typenone_sh+cpes_lastmodified2019_typenone_iot)+" REFERENCIAS EL TIPO NO VIENE ESPECIFICADO ")
print("\n")
print("      -    EN  "+str(cpes_lastmodified2018_sh+cpes_lastmodified2018_iot)+" REFERENCIAS DE CPES LA FECHA DE ULTIMA MODIFICACION DEL CPE ES 2018 O ANTERIOR. LAS ESTADÍSTICAS DE TIPO DE REFERENCIA SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(cpes_lastmodified2018_typeversion_sh+cpes_lastmodified2018_typeversion_iot)+" REFERENCIAS EL TIPO ES VERSION ")
print("            -    EN  "+str(cpes_lastmodified2018_typeproduct_sh+cpes_lastmodified2018_typeproduct_iot)+" REFERENCIAS EL TIPO ES PRODUCTO ")
print("            -    EN  "+str(cpes_lastmodified2018_typeadvisory_sh+cpes_lastmodified2018_typeadvisory_iot)+" REFERENCIAS EL TIPO ES AVISO ")
print("            -    EN  "+str(cpes_lastmodified2018_typechangelog_sh+cpes_lastmodified2018_typechangelog_iot)+" REFERENCIAS EL TIPO ES REGISTRO DE CAMBIO ")
print("            -    EN  "+str(cpes_lastmodified2018_typevendor_sh+cpes_lastmodified2018_typevendor_iot)+" REFERENCIAS EL TIPO ES VENDEDOR ")
print("            -    EN  "+str(cpes_lastmodified2018_typenone_sh+cpes_lastmodified2018_typenone_iot)+" REFERENCIAS EL TIPO NO VIENE ESPECIFICADO ")
print("\n")



















print("*************************************PORCENTAJES FECHA ULTIMA MODIFICACION/TIPO DE REFERENCIA DE CPE PARTE IOT Y SMART HOME CONJUNTAS *************************************")
print("\n")        
                
print("\n")
print(" DE UN TOTAL DE "+str(total_modified_cpe_sh+total_modified_cpe_iot)+" REFERENCIAS DE CPES , LOS PORCENTAJES DE RELACION DE FECHA DE MODIFICACION Y TIPO DE REFERENCIA SON LOS SIGUIENTES:  \n")
print("\n")
print("      -    EN EL "+str(float((((cpes_lastmodified2023_sh+cpes_lastmodified2023_iot)*100)/(total_modified_cpe_sh+total_modified_cpe_iot)))) +" % DE REFERENCIAS DE CPES LA FECHA DE ULTIMA MODIFICACION DEL CPE ES 2023. LOS PORCENTAJES DE TIPO DE REFERENCIA SON LOS SIGUIENTES:  \n")
print("\n")
print("            -    EN EL "+str(float((((cpes_lastmodified2023_typeversion_sh+cpes_lastmodified2023_typeversion_iot)*100)/(total_modified_cpe_sh+total_modified_cpe_iot))))+" % DE REFERENCIAS EL TIPO ES VERSION  ")
print("            -    EN EL "+str(float((((cpes_lastmodified2023_typeproduct_sh+cpes_lastmodified2023_typeproduct_iot)*100)/(total_modified_cpe_sh+total_modified_cpe_iot))))+" % DE REFERENCIAS EL TIPO ES PRODUCTO ")
print("            -    EN EL "+str(float((((cpes_lastmodified2023_typeadvisory_sh+cpes_lastmodified2023_typeadvisory_iot)*100)/(total_modified_cpe_sh+total_modified_cpe_iot))))+" % DE REFERENCIAS EL TIPO ES AVISO ")
print("            -    EN EL "+str(float((((cpes_lastmodified2023_typechangelog_sh+cpes_lastmodified2023_typechangelog_iot)*100)/(total_modified_cpe_sh+total_modified_cpe_iot))))+" % DE REFERENCIAS EL TIPO ES REGISTRO DE CAMBIO ")
print("            -    EN EL "+str(float((((cpes_lastmodified2023_typevendor_sh+cpes_lastmodified2023_typevendor_iot)*100)/(total_modified_cpe_sh+total_modified_cpe_iot))))+" % DE REFERENCIAS EL TIPO ES VENDEDOR ")
print("            -    EN EL "+str(float((((cpes_lastmodified2023_typenone_sh+cpes_lastmodified2023_typenone_iot)*100)/(total_modified_cpe_sh+total_modified_cpe_iot))))+" % DE REFERENCIAS EL TIPO NO VIENE ESPECIFICADO ")
print("\n")

print("      -    EN EL "+str(float((((cpes_lastmodified2022_sh+cpes_lastmodified2022_iot)*100)/(total_modified_cpe_sh+total_modified_cpe_iot)))) +" % DE REFERENCIAS DE CPES LA FECHA DE ULTIMA MODIFICACION DEL CPE ES 2022. LOS PORCENTAJES DE TIPO DE REFERENCIA SON LOS SIGUIENTES:  \n")
print("\n")
print("            -    EN EL "+str(float((((cpes_lastmodified2022_typeversion_sh+cpes_lastmodified2022_typeversion_iot)*100)/(total_modified_cpe_sh+total_modified_cpe_iot))))+" % DE REFERENCIAS EL TIPO ES VERSION  ")
print("            -    EN EL "+str(float((((cpes_lastmodified2022_typeproduct_sh+cpes_lastmodified2022_typeproduct_iot)*100)/(total_modified_cpe_sh+total_modified_cpe_iot))))+" % DE REFERENCIAS EL TIPO ES PRODUCTO ")
print("            -    EN EL "+str(float((((cpes_lastmodified2022_typeadvisory_sh+cpes_lastmodified2022_typeadvisory_iot)*100)/(total_modified_cpe_sh+total_modified_cpe_iot))))+" % DE REFERENCIAS EL TIPO ES AVISO ")
print("            -    EN EL "+str(float((((cpes_lastmodified2022_typechangelog_sh+cpes_lastmodified2022_typechangelog_iot)*100)/(total_modified_cpe_sh+total_modified_cpe_iot))))+" % DE REFERENCIAS EL TIPO ES REGISTRO DE CAMBIO ")
print("            -    EN EL "+str(float((((cpes_lastmodified2022_typevendor_sh+cpes_lastmodified2022_typevendor_iot)*100)/(total_modified_cpe_sh+total_modified_cpe_iot))))+" % DE REFERENCIAS EL TIPO ES VENDEDOR ")
print("            -    EN EL "+str(float((((cpes_lastmodified2022_typenone_sh+cpes_lastmodified2022_typenone_iot)*100)/(total_modified_cpe_sh+total_modified_cpe_iot))))+" % DE REFERENCIAS EL TIPO NO VIENE ESPECIFICADO ")
print("\n")

print("      -    EN EL "+str(float((((cpes_lastmodified2021_sh+cpes_lastmodified2021_iot)*100)/(total_modified_cpe_sh+total_modified_cpe_iot)))) +" % DE REFERENCIAS DE CPES LA FECHA DE ULTIMA MODIFICACION DEL CPE ES 2021. LOS PORCENTAJES DE TIPO DE REFERENCIA SON LOS SIGUIENTES:  \n")
print("\n")
print("            -    EN EL "+str(float((((cpes_lastmodified2021_typeversion_sh+cpes_lastmodified2021_typeversion_iot)*100)/(total_modified_cpe_sh+total_modified_cpe_iot))))+" % DE REFERENCIAS EL TIPO ES VERSION  ")
print("            -    EN EL "+str(float((((cpes_lastmodified2021_typeproduct_sh+cpes_lastmodified2021_typeproduct_iot)*100)/(total_modified_cpe_sh+total_modified_cpe_iot))))+" % DE REFERENCIAS EL TIPO ES PRODUCTO ")
print("            -    EN EL "+str(float((((cpes_lastmodified2021_typeadvisory_sh+cpes_lastmodified2021_typeadvisory_iot)*100)/(total_modified_cpe_sh+total_modified_cpe_iot))))+" % DE REFERENCIAS EL TIPO ES AVISO ")
print("            -    EN EL "+str(float((((cpes_lastmodified2021_typechangelog_sh+cpes_lastmodified2021_typechangelog_iot)*100)/(total_modified_cpe_sh+total_modified_cpe_iot))))+" % DE REFERENCIAS EL TIPO ES REGISTRO DE CAMBIO ")
print("            -    EN EL "+str(float((((cpes_lastmodified2021_typevendor_sh+cpes_lastmodified2021_typevendor_iot)*100)/(total_modified_cpe_sh+total_modified_cpe_iot))))+" % DE REFERENCIAS EL TIPO ES VENDEDOR ")
print("            -    EN EL "+str(float((((cpes_lastmodified2021_typenone_sh+cpes_lastmodified2021_typenone_iot)*100)/(total_modified_cpe_sh+total_modified_cpe_iot))))+" % DE REFERENCIAS EL TIPO NO VIENE ESPECIFICADO ")
print("\n")

print("      -    EN EL "+str(float((((cpes_lastmodified2020_sh+cpes_lastmodified2020_iot)*100)/(total_modified_cpe_sh+total_modified_cpe_iot)))) +" % DE REFERENCIAS DE CPES LA FECHA DE ULTIMA MODIFICACION DEL CPE ES 2020. LOS PORCENTAJES DE TIPO DE REFERENCIA SON LOS SIGUIENTES:  \n")
print("\n")
print("            -    EN EL "+str(float((((cpes_lastmodified2020_typeversion_sh+cpes_lastmodified2020_typeversion_iot)*100)/(total_modified_cpe_sh+total_modified_cpe_iot))))+" % DE REFERENCIAS EL TIPO ES VERSION  ")
print("            -    EN EL "+str(float((((cpes_lastmodified2020_typeproduct_sh+cpes_lastmodified2020_typeproduct_iot)*100)/(total_modified_cpe_sh+total_modified_cpe_iot))))+" % DE REFERENCIAS EL TIPO ES PRODUCTO ")
print("            -    EN EL "+str(float((((cpes_lastmodified2020_typeadvisory_sh+cpes_lastmodified2020_typeadvisory_iot)*100)/(total_modified_cpe_sh+total_modified_cpe_iot))))+" % DE REFERENCIAS EL TIPO ES AVISO ")
print("            -    EN EL "+str(float((((cpes_lastmodified2020_typechangelog_sh+cpes_lastmodified2020_typechangelog_iot)*100)/(total_modified_cpe_sh+total_modified_cpe_iot))))+" % DE REFERENCIAS EL TIPO ES REGISTRO DE CAMBIO ")
print("            -    EN EL "+str(float((((cpes_lastmodified2020_typevendor_sh+cpes_lastmodified2020_typevendor_iot)*100)/(total_modified_cpe_sh+total_modified_cpe_iot))))+" % DE REFERENCIAS EL TIPO ES VENDEDOR ")
print("            -    EN EL "+str(float((((cpes_lastmodified2020_typenone_sh+cpes_lastmodified2020_typenone_iot)*100)/(total_modified_cpe_sh+total_modified_cpe_iot))))+" % DE REFERENCIAS EL TIPO NO VIENE ESPECIFICADO ")
print("\n")

print("      -    EN EL "+str(float((((cpes_lastmodified2019_sh+cpes_lastmodified2019_iot)*100)/(total_modified_cpe_sh+total_modified_cpe_iot)))) +" % DE REFERENCIAS DE CPES LA FECHA DE ULTIMA MODIFICACION DEL CPE ES 2019. LOS PORCENTAJES DE TIPO DE REFERENCIA SON LOS SIGUIENTES:  \n")
print("\n")
print("            -    EN EL "+str(float((((cpes_lastmodified2019_typeversion_sh+cpes_lastmodified2019_typeversion_iot)*100)/(total_modified_cpe_sh+total_modified_cpe_iot))))+" % DE REFERENCIAS EL TIPO ES VERSION  ")
print("            -    EN EL "+str(float((((cpes_lastmodified2019_typeproduct_sh+cpes_lastmodified2019_typeproduct_iot)*100)/(total_modified_cpe_sh+total_modified_cpe_iot))))+" % DE REFERENCIAS EL TIPO ES PRODUCTO ")
print("            -    EN EL "+str(float((((cpes_lastmodified2019_typeadvisory_sh+cpes_lastmodified2019_typeadvisory_iot)*100)/(total_modified_cpe_sh+total_modified_cpe_iot))))+" % DE REFERENCIAS EL TIPO ES AVISO ")
print("            -    EN EL "+str(float((((cpes_lastmodified2019_typechangelog_sh+cpes_lastmodified2019_typechangelog_iot)*100)/(total_modified_cpe_sh+total_modified_cpe_iot))))+" % DE REFERENCIAS EL TIPO ES REGISTRO DE CAMBIO ")
print("            -    EN EL "+str(float((((cpes_lastmodified2019_typevendor_sh+cpes_lastmodified2019_typevendor_iot)*100)/(total_modified_cpe_sh+total_modified_cpe_iot))))+" % DE REFERENCIAS EL TIPO ES VENDEDOR ")
print("            -    EN EL "+str(float((((cpes_lastmodified2019_typenone_sh+cpes_lastmodified2019_typenone_iot)*100)/(total_modified_cpe_sh+total_modified_cpe_iot))))+" % DE REFERENCIAS EL TIPO NO VIENE ESPECIFICADO ")
print("\n")

print("      -    EN EL "+str(float((((cpes_lastmodified2018_sh+cpes_lastmodified2018_iot)*100)/(total_modified_cpe_sh+total_modified_cpe_iot)))) +" % DE REFERENCIAS DE CPES LA FECHA DE ULTIMA MODIFICACION DEL CPE ES 2018 O ANTERIOR. LOS PORCENTAJES DE TIPO DE REFERENCIA SON LOS SIGUIENTES: \n")
print("\n")
print("            -    EN EL "+str(float((((cpes_lastmodified2018_typeversion_sh+cpes_lastmodified2018_typeversion_iot)*100)/(total_modified_cpe_sh+total_modified_cpe_iot))))+" % DE REFERENCIAS EL TIPO ES VERSION  ")
print("            -    EN EL "+str(float((((cpes_lastmodified2018_typeproduct_sh+cpes_lastmodified2018_typeproduct_iot)*100)/(total_modified_cpe_sh+total_modified_cpe_iot))))+" % DE REFERENCIAS EL TIPO ES PRODUCTO ")
print("            -    EN EL "+str(float((((cpes_lastmodified2018_typeadvisory_sh+cpes_lastmodified2018_typeadvisory_iot)*100)/(total_modified_cpe_sh+total_modified_cpe_iot))))+" % DE REFERENCIAS EL TIPO ES AVISO ")
print("            -    EN EL "+str(float((((cpes_lastmodified2018_typechangelog_sh+cpes_lastmodified2018_typechangelog_iot)*100)/(total_modified_cpe_sh+total_modified_cpe_iot))))+" % DE REFERENCIAS EL TIPO ES REGISTRO DE CAMBIO ")
print("            -    EN EL "+str(float((((cpes_lastmodified2018_typevendor_sh+cpes_lastmodified2018_typevendor_iot)*100)/(total_modified_cpe_sh+total_modified_cpe_iot))))+" % DE REFERENCIAS EL TIPO ES VENDEDOR ")
print("            -    EN EL "+str(float((((cpes_lastmodified2018_typenone_sh+cpes_lastmodified2018_typenone_iot)*100)/(total_modified_cpe_sh+total_modified_cpe_iot))))+" % DE REFERENCIAS EL TIPO NO VIENE ESPECIFICADO ")
print("\n")

