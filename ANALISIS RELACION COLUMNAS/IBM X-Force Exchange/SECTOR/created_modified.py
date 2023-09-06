
	
	


import pandas as pd
from datetime import datetime,timedelta



#Abro los ficheros con los que voy a tratar




df_sector= pd.read_excel('ibm_sector_v2.xlsx')

#Variables para almacenar el total de entradas del fichero
count_sector_entries=0

#Variables para almacenar entradas creadas en un anio especifico
count_sector_created_2023=0
#Variables para almacenar la diferencia entre fecha de creacion y modificacion para un anio determinado
count_sector_created_2023_modifiedsameday=0
count_sector_created_2023_modifiedsamemonth=0
count_sector_created_2023_modifiedsameyear=0
count_sector_created_2023_anotheryear=0

count_sector_created_2022=0
count_sector_created_2022_modifiedsameday=0
count_sector_created_2022_modifiedsamemonth=0
count_sector_created_2022_modifiedsameyear=0
count_sector_created_2022_anotheryear=0

count_sector_created_2021=0
count_sector_created_2021_modifiedsameday=0
count_sector_created_2021_modifiedsamemonth=0
count_sector_created_2021_modifiedsameyear=0
count_sector_created_2021_anotheryear=0

count_sector_created_2020=0
count_sector_created_2020_modifiedsameday=0
count_sector_created_2020_modifiedsamemonth=0
count_sector_created_2020_modifiedsameyear=0
count_sector_created_2020_anotheryear=0

count_sector_created_2019=0
count_sector_created_2019_modifiedsameday=0
count_sector_created_2019_modifiedsamemonth=0
count_sector_created_2019_modifiedsameyear=0
count_sector_created_2019_anotheryear=0

count_sector_created_2018=0
count_sector_created_2018_modifiedsameday=0
count_sector_created_2018_modifiedsamemonth=0
count_sector_created_2018_modifiedsameyear=0
count_sector_created_2018_anotheryear=0


#Comprobamos el anio de creacion
for r in range(0,len(df_sector["created"])):
    #Si para una misma fila existe mas de un valor de fecha de creacion
    if('[' in df_sector["created"][r]):
        #Obtenemos los valores de creacion y modificacion para la fila actual
        aux=df_sector["created"][r].split(",")
        auxx=df_sector["modified"][r].split(",")
        #Recorremos los distintos valores de fecha de creacion
        for l in range(0,len(aux)):
            if(len(aux)>0):
                #Obtenemos los valores
                aux_str=aux[l].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","").replace("T"," ")
                auxx_str=auxx[l].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","").replace("T"," ")
                #Comprobamos que los valores no sean nulos
                if(aux_str!='NONE' and auxx_str!='NONE'):
                    #Obtenemos la fecha de creacion en formato de texto y la convertimos a formato temporal
                    aux2=aux_str.split(".")
                    creado = datetime.strptime(aux2[0], '%Y-%m-%d %H:%M:%S')
                    #Obtenemos la fecha de modificacion en formato de texto y la convertimos a formato temporal
                    aux22=auxx_str.split(".")
                    modificado = datetime.strptime(aux22[0], '%Y-%m-%d %H:%M:%S')
                    #Obtenemos la diferencia de tiempo entre fecha de creacion y modificacion
                    res=creado-modificado
                    #Obtenemos el anio de creacion
                    str_anio_createdate_sector_=aux_str.split("-")
                    anio_createdate_sector_=int(str_anio_createdate_sector_[0])
                    #Comprobamos el formato de creacion
                    if(anio_createdate_sector_ >= 2023):
                        #Aumentamos el contador de entradas y de entradas creadas en un anio especifico
                        count_sector_entries+=1
                        count_sector_created_2023+=1
                        #Compruebo si la diferencia con la fecha de modificacion es de menos de un dia
                        if(((res/ timedelta(days=1))*(-1)) < 1):
                            count_sector_created_2023_modifiedsameday+=1
                        #Compruebo si la diferencia con la fecha de modificacion es de menos de un mes 
                        elif(((res/ timedelta(days=30))*(-1)) < 1):
                            count_sector_created_2023_modifiedsamemonth+=1
                        #Compruebo si la diferencia con la fecha de modificacion es de menos de un anio  
                        elif(((res/ timedelta(days=365))*(-1)) < 1):
                            count_sector_created_2023_modifiedsameyear+=1
                        #Compruebo si la diferencia con la fecha de modificacion es de mas de un anio 
                        else:
                            count_sector_created_2023_anotheryear+=1
                            
                    elif(anio_createdate_sector_ >= 2022):
                        count_sector_entries+=1
                        count_sector_created_2022+=1
                        if(((res/ timedelta(days=1))*(-1)) < 1):
                            count_sector_created_2022_modifiedsameday+=1
                            
                        elif(((res/ timedelta(days=30))*(-1)) < 1):
                            count_sector_created_2022_modifiedsamemonth+=1
                            
                        elif(((res/ timedelta(days=365))*(-1)) < 1):
                            count_sector_created_2022_modifiedsameyear+=1
                            
                        else:
                            count_sector_created_2022_anotheryear+=1
                            
                    elif(anio_createdate_sector_ >= 2021):
                        count_sector_entries+=1
                        count_sector_created_2021+=1
                        if(((res/ timedelta(days=1))*(-1)) < 1):
                            count_sector_created_2021_modifiedsameday+=1
                            
                        elif(((res/ timedelta(days=30))*(-1)) < 1):
                            count_sector_created_2021_modifiedsamemonth+=1
                            
                        elif(((res/ timedelta(days=365))*(-1)) < 1):
                            count_sector_created_2021_modifiedsameyear+=1
                            
                        else:
                            count_sector_created_2021_anotheryear+=1
                            
                    elif(anio_createdate_sector_ >= 2020):
                        count_sector_entries+=1
                        count_sector_created_2020+=1
                        if(((res/ timedelta(days=1))*(-1)) < 1):
                            count_sector_created_2020_modifiedsameday+=1
                            
                        elif(((res/ timedelta(days=30))*(-1)) < 1):
                            count_sector_created_2020_modifiedsamemonth+=1
                            
                        elif(((res/ timedelta(days=365))*(-1)) < 1):
                            count_sector_created_2020_modifiedsameyear+=1
                            
                        else:
                            count_sector_created_2020_anotheryear+=1
                            
                    elif(anio_createdate_sector_ >= 2019):
                        count_sector_entries+=1
                        count_sector_created_2019+=1
                        if(((res/ timedelta(days=1))*(-1)) < 1):
                            count_sector_created_2019_modifiedsameday+=1
                            
                        elif(((res/ timedelta(days=30))*(-1)) < 1):
                            count_sector_created_2019_modifiedsamemonth+=1
                            
                        elif(((res/ timedelta(days=365))*(-1)) < 1):
                            count_sector_created_2019_modifiedsameyear+=1
                            
                        else:
                            count_sector_created_2019_anotheryear+=1
                            
                    elif(anio_createdate_sector_ >= 2018):
                        count_sector_entries+=1
                        count_sector_created_2018+=1
                        if(((res/ timedelta(days=1))*(-1)) < 1):
                            count_sector_created_2018_modifiedsameday+=1
                            
                        elif(((res/ timedelta(days=30))*(-1)) < 1):
                            count_sector_created_2018_modifiedsamemonth+=1
                            
                        elif(((res/ timedelta(days=365))*(-1)) < 1):
                            count_sector_created_2018_modifiedsameyear+=1
                            
                        else:
                            count_sector_created_2018_anotheryear+=1
                            
    else:
        #Si la fila actual únicamente tiene un valor de fecha de creación y modificacion
        aux_strr=df_sector["created"][r].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","").replace("T"," ")
        auxx_strr=df_sector["modified"][r].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","").replace("T"," ")
        #Comprobamos que los valores de creacion y modificacion no sean nulos para poder compararlos
        if(aux_strr!='NONE' and auxx_strr!='NONE'):
            aux22=aux_strr.split(".")
            creado = datetime.strptime(aux22[0], '%Y-%m-%d %H:%M:%S')
            aux222=auxx_strr.split(".")
            modificado = datetime.strptime(aux222[0], '%Y-%m-%d %H:%M:%S')
            res=creado-modificado
            str_anio_createdate_sector_=auxx_strr.split("-")
            anio_createdate_sector_=int(str_anio_createdate_sector_[0])                    
            if(anio_createdate_sector_ >= 2023):
                count_sector_entries+=1
                count_sector_created_2023+=1
                if(((res/ timedelta(days=1))*(-1)) < 1):
                    count_sector_created_2023_modifiedsameday+=1

                elif(((res/ timedelta(days=30))*(-1)) < 1):
                    count_sector_created_2023_modifiedsamemonth+=1

                elif(((res/ timedelta(days=365))*(-1)) < 1):
                    count_sector_created_2023_modifiedsameyear+=1

                else:
                    count_sector_created_2023_anotheryear+=1

            elif(anio_createdate_sector_ >= 2022):
                count_sector_entries+=1
                count_sector_created_2022+=1
                if(((res/ timedelta(days=1))*(-1)) < 1):
                    count_sector_created_2022_modifiedsameday+=1

                elif(((res/ timedelta(days=30))*(-1)) < 1):
                    count_sector_created_2022_modifiedsamemonth+=1

                elif(((res/ timedelta(days=365))*(-1)) < 1):
                    count_sector_created_2022_modifiedsameyear+=1

                else:
                    count_sector_created_2022_anotheryear+=1

            elif(anio_createdate_sector_ >= 2021):
                count_sector_entries+=1
                count_sector_created_2021+=1
                if(((res/ timedelta(days=1))*(-1)) < 1):
                    count_sector_created_2021_modifiedsameday+=1

                elif(((res/ timedelta(days=30))*(-1)) < 1):
                    count_sector_created_2021_modifiedsamemonth+=1

                elif(((res/ timedelta(days=365))*(-1)) < 1):
                    count_sector_created_2021_modifiedsameyear+=1

                else:
                    count_sector_created_2021_anotheryear+=1

            elif(anio_createdate_sector_ >= 2020):
                count_sector_entries+=1
                count_sector_created_2020+=1
                if(((res/ timedelta(days=1))*(-1)) < 1):
                    count_sector_created_2020_modifiedsameday+=1

                elif(((res/ timedelta(days=30))*(-1)) < 1):
                    count_sector_created_2020_modifiedsamemonth+=1

                elif(((res/ timedelta(days=365))*(-1)) < 1):
                    count_sector_created_2020_modifiedsameyear+=1

                else:
                    count_sector_created_2020_anotheryear+=1

            elif(anio_createdate_sector_ >= 2019):
                count_sector_entries+=1
                count_sector_created_2019+=1
                if(((res/ timedelta(days=1))*(-1)) < 1):
                    count_sector_created_2019_modifiedsameday+=1

                elif(((res/ timedelta(days=30))*(-1)) < 1):
                    count_sector_created_2019_modifiedsamemonth+=1

                elif(((res/ timedelta(days=365))*(-1)) < 1):
                    count_sector_created_2019_modifiedsameyear+=1

                else:
                    count_sector_created_2019_anotheryear+=1

            elif(anio_createdate_sector_ >= 2018):
                count_sector_entries+=1
                count_sector_created_2018+=1
                if(((res/ timedelta(days=1))*(-1)) < 1):
                    count_sector_created_2018_modifiedsameday+=1

                elif(((res/ timedelta(days=30))*(-1)) < 1):
                    count_sector_created_2018_modifiedsamemonth+=1

                elif(((res/ timedelta(days=365))*(-1)) < 1):
                    count_sector_created_2018_modifiedsameyear+=1

                else:
                    count_sector_created_2018_anotheryear+=1        
                            
                    
print("**************ESTADÍSTICAS RELACIÓN FECHA DE CREACIÓN/MODIFICACIÓN  INFORME DE SECTOR IBM **************")
print("\n")                            
                
print("\n")
print(" DE UN TOTAL DE "+str(count_sector_entries)+" OBJETOS :\n") 
print("\n")
print("   - LAS ESTADISTICAS DE FECHA DE CREACION SON LAS SIGUIENTES:  \n")
print("      -    EN  "+str(count_sector_created_2023)+" OBJETOS LA FECHA DE CREACION ES 2023. LAS ESTADÍSTICAS DE FECHA DE MODIFICACION SON LAS SIGUIENTES :  \n")
print("\n")
print("            -    EN  "+str(count_sector_created_2023_modifiedsameday)+" OBJETOS CREADOS EN 2023, LA ULTIMA MODIFICACIÓN SE PRODUJO ESE MISMO DÍA ")
print("            -    EN  "+str(count_sector_created_2023_modifiedsamemonth)+" OBJETOS CREADOS EN 2023, LA ÚLTIMA MODIFICACIÓN SE PRODUJO ESE MISMO MES")
print("            -    EN  "+str(count_sector_created_2023_modifiedsameyear)+" OBJETOS CREADOS EN 2023, LA ÚLTIMA MODIFICACIÓN SE PRODUJO ESE MISMO AÑO ")
print("            -    EN  "+str(count_sector_created_2023_anotheryear)+" OBJETOS CREADOS EN 2023, LA ÚLTIMA MODIFICACIÓN SE PRODUJO MÁS TARDE DE UN AÑO ")
print("\n")
print("      -    EN  "+str(count_sector_created_2022)+" OBJETOS LA FECHA DE CREACION ES 2022. LAS ESTADÍSTICAS DE FECHA DE MODIFICACION SON LAS SIGUIENTES :  \n")
print("\n")
print("            -    EN  "+str(count_sector_created_2022_modifiedsameday)+" OBJETOS CREADOS EN 2022, LA ULTIMA MODIFICACIÓN SE PRODUJO ESE MISMO DÍA ")
print("            -    EN  "+str(count_sector_created_2022_modifiedsamemonth)+" OBJETOS CREADOS EN 2022, LA ÚLTIMA MODIFICACIÓN SE PRODUJO ESE MISMO MES")
print("            -    EN  "+str(count_sector_created_2022_modifiedsameyear)+" OBJETOS CREADOS EN 2022, LA ÚLTIMA MODIFICACIÓN SE PRODUJO ESE MISMO AÑO ")
print("            -    EN  "+str(count_sector_created_2022_anotheryear)+" OBJETOS CREADOS EN 2022, LA ÚLTIMA MODIFICACIÓN SE PRODUJO MÁS TARDE DE UN AÑO ")
print("\n")
print("      -    EN  "+str(count_sector_created_2021)+" OBJETOS LA FECHA DE CREACION ES 2021. LAS ESTADÍSTICAS DE FECHA DE MODIFICACION SON LAS SIGUIENTES :  \n")
print("\n")
print("            -    EN  "+str(count_sector_created_2021_modifiedsameday)+" OBJETOS CREADOS EN 2021, LA ULTIMA MODIFICACIÓN SE PRODUJO ESE MISMO DÍA ")
print("            -    EN  "+str(count_sector_created_2021_modifiedsamemonth)+" OBJETOS CREADOS EN 2021, LA ÚLTIMA MODIFICACIÓN SE PRODUJO ESE MISMO MES")
print("            -    EN  "+str(count_sector_created_2021_modifiedsameyear)+" OBJETOS CREADOS EN 2021, LA ÚLTIMA MODIFICACIÓN SE PRODUJO ESE MISMO AÑO ")
print("            -    EN  "+str(count_sector_created_2021_anotheryear)+" OBJETOS CREADOS EN 2021, LA ÚLTIMA MODIFICACIÓN SE PRODUJO MÁS TARDE DE UN AÑO ")
print("\n")
print("      -    EN  "+str(count_sector_created_2020)+" OBJETOS LA FECHA DE CREACION ES 2020. LAS ESTADÍSTICAS DE FECHA DE MODIFICACION SON LAS SIGUIENTES :  \n")
print("\n")
print("            -    EN  "+str(count_sector_created_2020_modifiedsameday)+" OBJETOS CREADOS EN 2020, LA ULTIMA MODIFICACIÓN SE PRODUJO ESE MISMO DÍA ")
print("            -    EN  "+str(count_sector_created_2020_modifiedsamemonth)+" OBJETOS CREADOS EN 2020, LA ÚLTIMA MODIFICACIÓN SE PRODUJO ESE MISMO MES")
print("            -    EN  "+str(count_sector_created_2020_modifiedsameyear)+" OBJETOS CREADOS EN 2020, LA ÚLTIMA MODIFICACIÓN SE PRODUJO ESE MISMO AÑO ")
print("            -    EN  "+str(count_sector_created_2020_anotheryear)+" OBJETOS CREADOS EN 2020, LA ÚLTIMA MODIFICACIÓN SE PRODUJO MÁS TARDE DE UN AÑO ")
print("\n")
print("      -    EN  "+str(count_sector_created_2019)+" OBJETOS LA FECHA DE CREACION ES 2019. LAS ESTADÍSTICAS DE FECHA DE MODIFICACION SON LAS SIGUIENTES :  \n")
print("\n")
print("            -    EN  "+str(count_sector_created_2019_modifiedsameday)+" OBJETOS CREADOS EN 2019, LA ULTIMA MODIFICACIÓN SE PRODUJO ESE MISMO DÍA ")
print("            -    EN  "+str(count_sector_created_2019_modifiedsamemonth)+" OBJETOS CREADOS EN 2019, LA ÚLTIMA MODIFICACIÓN SE PRODUJO ESE MISMO MES")
print("            -    EN  "+str(count_sector_created_2019_modifiedsameyear)+" OBJETOS CREADOS EN 2019, LA ÚLTIMA MODIFICACIÓN SE PRODUJO ESE MISMO AÑO ")
print("            -    EN  "+str(count_sector_created_2019_anotheryear)+" OBJETOS CREADOS EN 2019, LA ÚLTIMA MODIFICACIÓN SE PRODUJO MÁS TARDE DE UN AÑO ")
print("\n")
print("      -    EN  "+str(count_sector_created_2018)+" OBJETOS LA FECHA DE CREACION ES 2018 O ANTERIOR. LAS ESTADÍSTICAS DE FECHA DE MODIFICACION SON LAS SIGUIENTES :  \n")
print("\n")
print("            -    EN  "+str(count_sector_created_2018_modifiedsameday)+" OBJETOS CREADOS EN 2018 O ANTERIORMENTE, LA ULTIMA MODIFICACIÓN SE PRODUJO ESE MISMO DÍA ")
print("            -    EN  "+str(count_sector_created_2018_modifiedsamemonth)+" OBJETOS CREADOS EN 2018 O ANTERIORMENTE, LA ÚLTIMA MODIFICACIÓN SE PRODUJO ESE MISMO MES")
print("            -    EN  "+str(count_sector_created_2018_modifiedsameyear)+" OBJETOS CREADOS EN 2018 O ANTERIORMENTE, LA ÚLTIMA MODIFICACIÓN SE PRODUJO ESE MISMO AÑO ")
print("            -    EN  "+str(count_sector_created_2018_anotheryear)+" OBJETOS CREADOS EN 2018 O ANTERIORMENTE, LA ÚLTIMA MODIFICACIÓN SE PRODUJO MÁS TARDE DE UN AÑO ")
print("\n")








print("**************PORCENTAJES RELACIÓN FECHA DE CREACIÓN/MODIFICACIÓN  INFORME DE SECTOR IBM **************")
print("\n")                            
                
print("\n")
print(" DE UN TOTAL DE "+str(count_sector_entries)+" OBJETOS :\n") 
print("\n")
print("   - LOS PORCENTAJES DE FECHA DE CREACION SON LOS SIGUIENTES:  \n")
if(count_sector_created_2023>0):
    print("      -    EN EL  "+str(float(((count_sector_created_2023*100)/count_sector_entries)))+" % DE OBJETOS LA FECHA DE CREACION ES 2023. LOS PORCENTAJES DE FECHA DE MODIFICACION SON LOS SIGUIENTES  \n")
    print("\n")
    print("            -    EN EL  "+str(float(((count_sector_created_2023_modifiedsameday*100)/count_sector_created_2023)))+" % DE OBJETOS CREADOS EN 2023, LA ULTIMA MODIFICACIÓN SE PRODUJO ESE MISMO DÍA ")
    print("            -    EN EL  "+str(float(((count_sector_created_2023_modifiedsamemonth*100)/count_sector_created_2023)))+" % DE OBJETOS CREADOS EN 2023, LA ULTIMA MODIFICACIÓN SE PRODUJO ESE MISMO MES")
    print("            -    EN EL  "+str(float(((count_sector_created_2023_modifiedsameyear*100)/count_sector_created_2023)))+" % DE OBJETOS CREADOS EN 2023, LA ULTIMA MODIFICACIÓN SE PRODUJO ESE MISMO AÑO ")
    print("            -    EN EL  "+str(float(((count_sector_created_2023_anotheryear*100)/count_sector_created_2023)))+" % DE OBJETOS CREADOS EN 2023, LA ULTIMA MODIFICACIÓN SE PRODUJO MÁS TARDE DE UN AÑO ")
    print("\n")
if(count_sector_created_2022>0):
    print("      -    EN EL  "+str(float(((count_sector_created_2022*100)/count_sector_entries)))+" % DE OBJETOS LA FECHA DE CREACION ES 2022. LOS PORCENTAJES DE FECHA DE MODIFICACION SON LOS SIGUIENTES  \n")
    print("\n")
    print("            -    EN EL  "+str(float(((count_sector_created_2022_modifiedsameday*100)/count_sector_created_2022)))+" % DE OBJETOS CREADOS EN 2022, LA ULTIMA MODIFICACIÓN SE PRODUJO ESE MISMO DÍA ")
    print("            -    EN EL  "+str(float(((count_sector_created_2022_modifiedsamemonth*100)/count_sector_created_2022)))+" % DE OBJETOS CREADOS EN 2022, LA ULTIMA MODIFICACIÓN SE PRODUJO ESE MISMO MES")
    print("            -    EN EL  "+str(float(((count_sector_created_2022_modifiedsameyear*100)/count_sector_created_2022)))+" % DE OBJETOS CREADOS EN 2022, LA ULTIMA MODIFICACIÓN SE PRODUJO ESE MISMO AÑO ")
    print("            -    EN EL  "+str(float(((count_sector_created_2022_anotheryear*100)/count_sector_created_2022)))+" % DE OBJETOS CREADOS EN 2022, LA ULTIMA MODIFICACIÓN SE PRODUJO MÁS TARDE DE UN AÑO ")
    print("\n")
if(count_sector_created_2021>0):
    print("      -    EN EL  "+str(float(((count_sector_created_2021*100)/count_sector_entries)))+" % DE OBJETOS LA FECHA DE CREACION ES 2021. LOS PORCENTAJES DE FECHA DE MODIFICACION SON LOS SIGUIENTES  \n")
    print("\n")
    print("            -    EN EL  "+str(float(((count_sector_created_2021_modifiedsameday*100)/count_sector_created_2021)))+" % DE OBJETOS CREADOS EN 2021, LA ULTIMA MODIFICACIÓN SE PRODUJO ESE MISMO DÍA ")
    print("            -    EN EL  "+str(float(((count_sector_created_2021_modifiedsamemonth*100)/count_sector_created_2021)))+" % DE OBJETOS CREADOS EN 2021, LA ULTIMA MODIFICACIÓN SE PRODUJO ESE MISMO MES")
    print("            -    EN EL  "+str(float(((count_sector_created_2021_modifiedsameyear*100)/count_sector_created_2021)))+" % DE OBJETOS CREADOS EN 2021, LA ULTIMA MODIFICACIÓN SE PRODUJO ESE MISMO AÑO ")
    print("            -    EN EL  "+str(float(((count_sector_created_2021_anotheryear*100)/count_sector_created_2021)))+" % DE OBJETOS CREADOS EN 2021, LA ULTIMA MODIFICACIÓN SE PRODUJO MÁS TARDE DE UN AÑO ")
    print("\n")
if(count_sector_created_2020>0):
    print("      -    EN EL  "+str(float(((count_sector_created_2020*100)/count_sector_entries)))+" % DE OBJETOS LA FECHA DE CREACION ES 2020. LOS PORCENTAJES DE FECHA DE MODIFICACION SON LOS SIGUIENTES  \n")
    print("\n")
    print("            -    EN EL  "+str(float(((count_sector_created_2020_modifiedsameday*100)/count_sector_created_2020)))+" % DE OBJETOS CREADOS EN 2020, LA ULTIMA MODIFICACIÓN SE PRODUJO ESE MISMO DÍA ")
    print("            -    EN EL  "+str(float(((count_sector_created_2020_modifiedsamemonth*100)/count_sector_created_2020)))+" % DE OBJETOS CREADOS EN 2020, LA ULTIMA MODIFICACIÓN SE PRODUJO ESE MISMO MES")
    print("            -    EN EL  "+str(float(((count_sector_created_2020_modifiedsameyear*100)/count_sector_created_2020)))+" % DE OBJETOS CREADOS EN 2020, LA ULTIMA MODIFICACIÓN SE PRODUJO ESE MISMO AÑO ")
    print("            -    EN EL  "+str(float(((count_sector_created_2020_anotheryear*100)/count_sector_created_2020)))+" % DE OBJETOS CREADOS EN 2020, LA ULTIMA MODIFICACIÓN SE PRODUJO MÁS TARDE DE UN AÑO ")
    print("\n")
if(count_sector_created_2019>0):
    print("      -    EN EL  "+str(float(((count_sector_created_2019*100)/count_sector_entries)))+" % DE OBJETOS LA FECHA DE CREACION ES 2019. LOS PORCENTAJES DE FECHA DE MODIFICACION SON LOS SIGUIENTES  \n")
    print("\n")
    print("            -    EN EL  "+str(float(((count_sector_created_2019_modifiedsameday*100)/count_sector_created_2019)))+" % DE OBJETOS CREADOS EN 2019, LA ULTIMA MODIFICACIÓN SE PRODUJO ESE MISMO DÍA ")
    print("            -    EN EL  "+str(float(((count_sector_created_2019_modifiedsamemonth*100)/count_sector_created_2019)))+" % DE OBJETOS CREADOS EN 2019, LA ULTIMA MODIFICACIÓN SE PRODUJO ESE MISMO MES")
    print("            -    EN EL  "+str(float(((count_sector_created_2019_modifiedsameyear*100)/count_sector_created_2019)))+" % DE OBJETOS CREADOS EN 2019, LA ULTIMA MODIFICACIÓN SE PRODUJO ESE MISMO AÑO ")
    print("            -    EN EL  "+str(float(((count_sector_created_2019_anotheryear*100)/count_sector_created_2019)))+" % DE OBJETOS CREADOS EN 2019, LA ULTIMA MODIFICACIÓN SE PRODUJO MÁS TARDE DE UN AÑO ")
    print("\n")
if(count_sector_created_2018>0):
    print("      -    EN EL  "+str(float(((count_sector_created_2018*100)/count_sector_entries)))+" % DE OBJETOS LA FECHA DE CREACION ES 2018 O ANTERIOR. LOS PORCENTAJES DE FECHA DE MODIFICACION SON LOS SIGUIENTES  \n")
    print("\n")
    print("            -    EN EL  "+str(float(((count_sector_created_2018_modifiedsameday*100)/count_sector_created_2018)))+" % DE OBJETOS CREADOS EN 2018 O ANTERIORMENTE, LA ULTIMA MODIFICACIÓN SE PRODUJO ESE MISMO DÍA ")
    print("            -    EN EL  "+str(float(((count_sector_created_2018_modifiedsamemonth*100)/count_sector_created_2018)))+" % DE OBJETOS CREADOS EN 2018 O ANTERIORMENTE, LA ULTIMA MODIFICACIÓN SE PRODUJO ESE MISMO MES")
    print("            -    EN EL  "+str(float(((count_sector_created_2018_modifiedsameyear*100)/count_sector_created_2018)))+" % DE OBJETOS CREADOS EN 2018 O ANTERIORMENTE, LA ULTIMA MODIFICACIÓN SE PRODUJO ESE MISMO AÑO ")
    print("            -    EN EL  "+str(float(((count_sector_created_2018_anotheryear*100)/count_sector_created_2018)))+" % DE OBJETOS CREADOS EN 2018 O ANTERIORMENTE, LA ULTIMA MODIFICACIÓN SE PRODUJO MÁS TARDE DE UN AÑO ")
    print("\n")










	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	