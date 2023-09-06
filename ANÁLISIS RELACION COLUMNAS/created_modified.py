import pandas as pd
from datetime import datetime,timedelta



#Abro los ficheros con los que voy a tratar




df_alienvault_iot = pd.read_excel('alienvault_iot_2023.xlsx')

#Contador total de OBJETOS EN LOS PULSOS de Alienvault
count_alienvault_iot_entries=0
#Contador total de OBJETOS EN LOS PULSOS creados en un anio concreto
count_alienvault_iot_created_2023=0
#Contador total de fecha de modificacion dado un anio cncreto
count_alienvault_iot_created_2023_modifiedsameday=0
count_alienvault_iot_created_2023_modifiedsamemonth=0
count_alienvault_iot_created_2023_modifiedsameyear=0
count_alienvault_iot_created_2023_anotheryear=0

count_alienvault_iot_created_2022=0
count_alienvault_iot_created_2022_modifiedsameday=0
count_alienvault_iot_created_2022_modifiedsamemonth=0
count_alienvault_iot_created_2022_modifiedsameyear=0
count_alienvault_iot_created_2022_anotheryear=0

count_alienvault_iot_created_2021=0
count_alienvault_iot_created_2021_modifiedsameday=0
count_alienvault_iot_created_2021_modifiedsamemonth=0
count_alienvault_iot_created_2021_modifiedsameyear=0
count_alienvault_iot_created_2021_anotheryear=0

count_alienvault_iot_created_2020=0
count_alienvault_iot_created_2020_modifiedsameday=0
count_alienvault_iot_created_2020_modifiedsamemonth=0
count_alienvault_iot_created_2020_modifiedsameyear=0
count_alienvault_iot_created_2020_anotheryear=0

count_alienvault_iot_created_2019=0
count_alienvault_iot_created_2019_modifiedsameday=0
count_alienvault_iot_created_2019_modifiedsamemonth=0
count_alienvault_iot_created_2019_modifiedsameyear=0
count_alienvault_iot_created_2019_anotheryear=0

count_alienvault_iot_created_2018=0
count_alienvault_iot_created_2018_modifiedsameday=0
count_alienvault_iot_created_2018_modifiedsamemonth=0
count_alienvault_iot_created_2018_modifiedsameyear=0
count_alienvault_iot_created_2018_anotheryear=0


#Comprobamos el anio de creacion
for r in range(0,len(df_alienvault_iot["created"])):
    #Si existen varios valores de fecha de creacion para una misma fila
    if('[' in df_alienvault_iot["created"][r]):
        #Obtengo los distintos valores de la fila de fecha de creacion y modificacion
        aux=df_alienvault_iot["created"][r].split(",")
        auxx=df_alienvault_iot["modified"][r].split(",")
        for l in range(0,len(aux)):
            if(len(aux)>0):
                #Si cada valor de creacion tiene un valor de modificacion asignado
                if(len(aux) == len(auxx)):
                    #Obtengo el valor actual de fecha de creacion y modificacion
                    aux_str=aux[l].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","").replace("T"," ")
                    auxx_str=auxx[l].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","").replace("T"," ")
                    #Compruebo que el valor obtenido viene en formato de cadena de tiempo
                    if((aux_str!='NONE' and auxx_str!='NONE') and ('Z' in aux_str and 'Z' in auxx_str)):
                        aux2=aux_str.split(".")
                        #Obtenemos la fecha de creacion
                        creado = datetime.strptime(aux2[0], '%Y-%m-%d %H:%M:%S')
                        aux22=auxx_str.split(".")
                        #Obtenemos la fecha de modificacion
                        modificado = datetime.strptime(aux22[0], '%Y-%m-%d %H:%M:%S')
                        #Calculamos la diferencia entre fecha de creacion y modificacion
                        res=creado-modificado
                        #Obtenemos el anio de creacion
                        str_anio_publishdate_alienvault_iot=aux_str.split("-")
                        anio_publishdate_alienvault_iot=int(str_anio_publishdate_alienvault_iot[0])
                        #Compruebo el anio de creacion
                        if(anio_publishdate_alienvault_iot >= 2023):
                            count_alienvault_iot_entries+=1
                            count_alienvault_iot_created_2023+=1
                            #Compruebo si la diferencia entre fecha de creacion y modificacion es menor de un dia
                            if(((res/ timedelta(days=1))*(-1)) < 1):
                                count_alienvault_iot_created_2023_modifiedsameday+=1
                            #Compruebo si la diferencia entre fecha de creacion y modificacion es menor de un mes
                            elif(((res/ timedelta(days=30))*(-1)) < 1):
                                count_alienvault_iot_created_2023_modifiedsamemonth+=1
                            #Compruebo si la diferencia entre fecha de creacion y modificacion es menor de un anio
                            elif(((res/ timedelta(days=365))*(-1)) < 1):
                                count_alienvault_iot_created_2023_modifiedsameyear+=1
                            #Compruebo si la diferencia entre fecha de creacion y modificacion es mayor de un anio
                            else:
                                count_alienvault_iot_created_2023_anotheryear+=1

                        elif(anio_publishdate_alienvault_iot >= 2022):
                            count_alienvault_iot_entries+=1
                            count_alienvault_iot_created_2022+=1
                            if(((res/ timedelta(days=1))*(-1)) < 1):
                                count_alienvault_iot_created_2022_modifiedsameday+=1

                            elif(((res/ timedelta(days=30))*(-1)) < 1):
                                count_alienvault_iot_created_2022_modifiedsamemonth+=1

                            elif(((res/ timedelta(days=365))*(-1)) < 1):
                                count_alienvault_iot_created_2022_modifiedsameyear+=1

                            else:
                                count_alienvault_iot_created_2022_anotheryear+=1

                        elif(anio_publishdate_alienvault_iot >= 2021):
                            count_alienvault_iot_entries+=1
                            count_alienvault_iot_created_2021+=1
                            if(((res/ timedelta(days=1))*(-1)) < 1):
                                count_alienvault_iot_created_2021_modifiedsameday+=1

                            elif(((res/ timedelta(days=30))*(-1)) < 1):
                                count_alienvault_iot_created_2021_modifiedsamemonth+=1

                            elif(((res/ timedelta(days=365))*(-1)) < 1):
                                count_alienvault_iot_created_2021_modifiedsameyear+=1

                            else:
                                count_alienvault_iot_created_2021_anotheryear+=1

                        elif(anio_publishdate_alienvault_iot >= 2020):
                            count_alienvault_iot_entries+=1
                            count_alienvault_iot_created_2020+=1
                            if(((res/ timedelta(days=1))*(-1)) < 1):
                                count_alienvault_iot_created_2020_modifiedsameday+=1

                            elif(((res/ timedelta(days=30))*(-1)) < 1):
                                count_alienvault_iot_created_2020_modifiedsamemonth+=1

                            elif(((res/ timedelta(days=365))*(-1)) < 1):
                                count_alienvault_iot_created_2020_modifiedsameyear+=1

                            else:
                                count_alienvault_iot_created_2020_anotheryear+=1

                        elif(anio_publishdate_alienvault_iot >= 2019):
                            count_alienvault_iot_entries+=1
                            count_alienvault_iot_created_2019+=1
                            if(((res/ timedelta(days=1))*(-1)) < 1):
                                count_alienvault_iot_created_2019_modifiedsameday+=1

                            elif(((res/ timedelta(days=30))*(-1)) < 1):
                                count_alienvault_iot_created_2019_modifiedsamemonth+=1

                            elif(((res/ timedelta(days=365))*(-1)) < 1):
                                count_alienvault_iot_created_2019_modifiedsameyear+=1

                            else:
                                count_alienvault_iot_created_2019_anotheryear+=1

                        elif(anio_publishdate_alienvault_iot >= 2018):
                            count_alienvault_iot_entries+=1
                            count_alienvault_iot_created_2018+=1
                            if(((res/ timedelta(days=1))*(-1)) < 1):
                                count_alienvault_iot_created_2018_modifiedsameday+=1

                            elif(((res/ timedelta(days=30))*(-1)) < 1):
                                count_alienvault_iot_created_2018_modifiedsamemonth+=1

                            elif(((res/ timedelta(days=365))*(-1)) < 1):
                                count_alienvault_iot_created_2018_modifiedsameyear+=1

                            else:
                                count_alienvault_iot_created_2018_anotheryear+=1

    else:
        #Si existe un unico valor de creacion y modificacion para la fila actual
        #Obtengo los valores
        aux_strr=df_alienvault_iot["created"][r].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","").replace("T"," ")
        auxx_strr=df_alienvault_iot["modified"][r].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","").replace("T"," ")
        if((aux_strr!='NONE' and auxx_strr!='NONE') and ('Z' in aux_strr and 'Z' in auxx_strr)):
            aux22=aux_strr.split(".")
            #Obtenemos fecha de creacion y modificacion
            creado = datetime.strptime(aux22[0], '%Y-%m-%d %H:%M:%S')
            aux222=auxx_strr.split(".")
            modificado = datetime.strptime(aux222[0], '%Y-%m-%d %H:%M:%S')
            #Calculo diferencia temporal
            res=creado-modificado
            str_anio_publishdate_alienvault_iot=auxx_strr.split("-")
            anio_publishdate_alienvault_iot=int(str_anio_publishdate_alienvault_iot[0]) 
            #Compruebo anio de creacion
            if(anio_publishdate_alienvault_iot >= 2023):
                count_alienvault_iot_entries+=1
                count_alienvault_iot_created_2023+=1
                #Compruebo diferencia temporal
                if(((res/ timedelta(days=1))*(-1)) < 1):
                    count_alienvault_iot_created_2023_modifiedsameday+=1

                elif(((res/ timedelta(days=30))*(-1)) < 1):
                    count_alienvault_iot_created_2023_modifiedsamemonth+=1

                elif(((res/ timedelta(days=365))*(-1)) < 1):
                    count_alienvault_iot_created_2023_modifiedsameyear+=1

                else:
                    count_alienvault_iot_created_2023_anotheryear+=1

            elif(anio_publishdate_alienvault_iot >= 2022):
                count_alienvault_iot_entries+=1
                count_alienvault_iot_created_2022+=1
                if(((res/ timedelta(days=1))*(-1)) < 1):
                    count_alienvault_iot_created_2022_modifiedsameday+=1

                elif(((res/ timedelta(days=30))*(-1)) < 1):
                    count_alienvault_iot_created_2022_modifiedsamemonth+=1

                elif(((res/ timedelta(days=365))*(-1)) < 1):
                    count_alienvault_iot_created_2022_modifiedsameyear+=1

                else:
                    count_alienvault_iot_created_2022_anotheryear+=1

            elif(anio_publishdate_alienvault_iot >= 2021):
                count_alienvault_iot_entries+=1
                count_alienvault_iot_created_2021+=1
                if(((res/ timedelta(days=1))*(-1)) < 1):
                    count_alienvault_iot_created_2021_modifiedsameday+=1

                elif(((res/ timedelta(days=30))*(-1)) < 1):
                    count_alienvault_iot_created_2021_modifiedsamemonth+=1

                elif(((res/ timedelta(days=365))*(-1)) < 1):
                    count_alienvault_iot_created_2021_modifiedsameyear+=1

                else:
                    count_alienvault_iot_created_2021_anotheryear+=1

            elif(anio_publishdate_alienvault_iot >= 2020):
                count_alienvault_iot_entries+=1
                count_alienvault_iot_created_2020+=1
                if(((res/ timedelta(days=1))*(-1)) < 1):
                    count_alienvault_iot_created_2020_modifiedsameday+=1

                elif(((res/ timedelta(days=30))*(-1)) < 1):
                    count_alienvault_iot_created_2020_modifiedsamemonth+=1

                elif(((res/ timedelta(days=365))*(-1)) < 1):
                    count_alienvault_iot_created_2020_modifiedsameyear+=1

                else:
                    count_alienvault_iot_created_2020_anotheryear+=1

            elif(anio_publishdate_alienvault_iot >= 2019):
                count_alienvault_iot_entries+=1
                count_alienvault_iot_created_2019+=1
                if(((res/ timedelta(days=1))*(-1)) < 1):
                    count_alienvault_iot_created_2019_modifiedsameday+=1

                elif(((res/ timedelta(days=30))*(-1)) < 1):
                    count_alienvault_iot_created_2019_modifiedsamemonth+=1

                elif(((res/ timedelta(days=365))*(-1)) < 1):
                    count_alienvault_iot_created_2019_modifiedsameyear+=1

                else:
                    count_alienvault_iot_created_2019_anotheryear+=1

            elif(anio_publishdate_alienvault_iot >= 2018):
                count_alienvault_iot_entries+=1
                count_alienvault_iot_created_2018+=1
                if(((res/ timedelta(days=1))*(-1)) < 1):
                    count_alienvault_iot_created_2018_modifiedsameday+=1

                elif(((res/ timedelta(days=30))*(-1)) < 1):
                    count_alienvault_iot_created_2018_modifiedsamemonth+=1

                elif(((res/ timedelta(days=365))*(-1)) < 1):
                    count_alienvault_iot_created_2018_modifiedsameyear+=1

                else:
                    count_alienvault_iot_created_2018_anotheryear+=1        
                            
                    
print("*********************ESTADÍSTICAS FECHA DE CREACION/FECHA DE MODIFICACION ALIENVAULT PARTE IOT*********************")
print("\n")                            
                
print("\n")
print(" DE UN TOTAL DE "+str(count_alienvault_iot_entries)+" OBJETOS EN LOS PULSOS :\n") 
print("\n")
print("   - LAS ESTADISTICAS DE FECHA DE CREACION SON LAS SIGUIENTES:  \n")
print("      -    EN  "+str(count_alienvault_iot_created_2023)+" OBJETOS EN LOS PULSOS LA FECHA DE CREACION ES 2023. LAS ESTADÍSTICAS DE FECHA DE MODIFICACION SON LAS SIGUIENTES :  \n")
print("\n")
print("            -    EN  "+str(count_alienvault_iot_created_2023_modifiedsameday)+" OBJETOS EN LOS PULSOS CREADOS EN 2023, LA ULTIMA MODIFICACIÓN SE PRODUJO ESE MISMO DÍA ")
print("            -    EN  "+str(count_alienvault_iot_created_2023_modifiedsamemonth)+" OBJETOS EN LOS PULSOS CREADOS EN 2023, LA ÚLTIMA MODIFICACIÓN SE PRODUJO ESE MISMO MES")
print("            -    EN  "+str(count_alienvault_iot_created_2023_modifiedsameyear)+" OBJETOS EN LOS PULSOS CREADOS EN 2023, LA ÚLTIMA MODIFICACIÓN SE PRODUJO ESE MISMO AÑO ")
print("            -    EN  "+str(count_alienvault_iot_created_2023_anotheryear)+" OBJETOS EN LOS PULSOS CREADOS EN 2023, LA ÚLTIMA MODIFICACIÓN SE PRODUJO MÁS TARDE DE UN AÑO ")
print("\n")
print("      -    EN  "+str(count_alienvault_iot_created_2022)+" OBJETOS EN LOS PULSOS LA FECHA DE CREACION ES 2022. LAS ESTADÍSTICAS DE FECHA DE MODIFICACION SON LAS SIGUIENTES :  \n")
print("\n")
print("            -    EN  "+str(count_alienvault_iot_created_2022_modifiedsameday)+" OBJETOS EN LOS PULSOS CREADOS EN 2022, LA ULTIMA MODIFICACIÓN SE PRODUJO ESE MISMO DÍA ")
print("            -    EN  "+str(count_alienvault_iot_created_2022_modifiedsamemonth)+" OBJETOS EN LOS PULSOS CREADOS EN 2022, LA ÚLTIMA MODIFICACIÓN SE PRODUJO ESE MISMO MES")
print("            -    EN  "+str(count_alienvault_iot_created_2022_modifiedsameyear)+" OBJETOS EN LOS PULSOS CREADOS EN 2022, LA ÚLTIMA MODIFICACIÓN SE PRODUJO ESE MISMO AÑO ")
print("            -    EN  "+str(count_alienvault_iot_created_2022_anotheryear)+" OBJETOS EN LOS PULSOS CREADOS EN 2022, LA ÚLTIMA MODIFICACIÓN SE PRODUJO MÁS TARDE DE UN AÑO ")
print("\n")
print("      -    EN  "+str(count_alienvault_iot_created_2021)+" OBJETOS EN LOS PULSOS LA FECHA DE CREACION ES 2021. LAS ESTADÍSTICAS DE FECHA DE MODIFICACION SON LAS SIGUIENTES :  \n")
print("\n")
print("            -    EN  "+str(count_alienvault_iot_created_2021_modifiedsameday)+" OBJETOS EN LOS PULSOS CREADOS EN 2021, LA ULTIMA MODIFICACIÓN SE PRODUJO ESE MISMO DÍA ")
print("            -    EN  "+str(count_alienvault_iot_created_2021_modifiedsamemonth)+" OBJETOS EN LOS PULSOS CREADOS EN 2021, LA ÚLTIMA MODIFICACIÓN SE PRODUJO ESE MISMO MES")
print("            -    EN  "+str(count_alienvault_iot_created_2021_modifiedsameyear)+" OBJETOS EN LOS PULSOS CREADOS EN 2021, LA ÚLTIMA MODIFICACIÓN SE PRODUJO ESE MISMO AÑO ")
print("            -    EN  "+str(count_alienvault_iot_created_2021_anotheryear)+" OBJETOS EN LOS PULSOS CREADOS EN 2021, LA ÚLTIMA MODIFICACIÓN SE PRODUJO MÁS TARDE DE UN AÑO ")
print("\n")
print("      -    EN  "+str(count_alienvault_iot_created_2020)+" OBJETOS EN LOS PULSOS LA FECHA DE CREACION ES 2020. LAS ESTADÍSTICAS DE FECHA DE MODIFICACION SON LAS SIGUIENTES :  \n")
print("\n")
print("            -    EN  "+str(count_alienvault_iot_created_2020_modifiedsameday)+" OBJETOS EN LOS PULSOS CREADOS EN 2020, LA ULTIMA MODIFICACIÓN SE PRODUJO ESE MISMO DÍA ")
print("            -    EN  "+str(count_alienvault_iot_created_2020_modifiedsamemonth)+" OBJETOS EN LOS PULSOS CREADOS EN 2020, LA ÚLTIMA MODIFICACIÓN SE PRODUJO ESE MISMO MES")
print("            -    EN  "+str(count_alienvault_iot_created_2020_modifiedsameyear)+" OBJETOS EN LOS PULSOS CREADOS EN 2020, LA ÚLTIMA MODIFICACIÓN SE PRODUJO ESE MISMO AÑO ")
print("            -    EN  "+str(count_alienvault_iot_created_2020_anotheryear)+" OBJETOS EN LOS PULSOS CREADOS EN 2020, LA ÚLTIMA MODIFICACIÓN SE PRODUJO MÁS TARDE DE UN AÑO ")
print("\n")
print("      -    EN  "+str(count_alienvault_iot_created_2019)+" OBJETOS EN LOS PULSOS LA FECHA DE CREACION ES 2019. LAS ESTADÍSTICAS DE FECHA DE MODIFICACION SON LAS SIGUIENTES :  \n")
print("\n")
print("            -    EN  "+str(count_alienvault_iot_created_2019_modifiedsameday)+" OBJETOS EN LOS PULSOS CREADOS EN 2019, LA ULTIMA MODIFICACIÓN SE PRODUJO ESE MISMO DÍA ")
print("            -    EN  "+str(count_alienvault_iot_created_2019_modifiedsamemonth)+" OBJETOS EN LOS PULSOS CREADOS EN 2019, LA ÚLTIMA MODIFICACIÓN SE PRODUJO ESE MISMO MES")
print("            -    EN  "+str(count_alienvault_iot_created_2019_modifiedsameyear)+" OBJETOS EN LOS PULSOS CREADOS EN 2019, LA ÚLTIMA MODIFICACIÓN SE PRODUJO ESE MISMO AÑO ")
print("            -    EN  "+str(count_alienvault_iot_created_2019_anotheryear)+" OBJETOS EN LOS PULSOS CREADOS EN 2019, LA ÚLTIMA MODIFICACIÓN SE PRODUJO MÁS TARDE DE UN AÑO ")
print("\n")
print("      -    EN  "+str(count_alienvault_iot_created_2018)+" OBJETOS EN LOS PULSOS LA FECHA DE CREACION ES 2018 O ANTERIOR. LAS ESTADÍSTICAS DE FECHA DE MODIFICACION SON LAS SIGUIENTES :  \n")
print("\n")
print("            -    EN  "+str(count_alienvault_iot_created_2018_modifiedsameday)+" OBJETOS EN LOS PULSOS CREADOS EN 2018 O ANTERIORMENTE, LA ULTIMA MODIFICACIÓN SE PRODUJO ESE MISMO DÍA ")
print("            -    EN  "+str(count_alienvault_iot_created_2018_modifiedsamemonth)+" OBJETOS EN LOS PULSOS CREADOS EN 2018 O ANTERIORMENTE, LA ÚLTIMA MODIFICACIÓN SE PRODUJO ESE MISMO MES")
print("            -    EN  "+str(count_alienvault_iot_created_2018_modifiedsameyear)+" OBJETOS EN LOS PULSOS CREADOS EN 2018 O ANTERIORMENTE, LA ÚLTIMA MODIFICACIÓN SE PRODUJO ESE MISMO AÑO ")
print("            -    EN  "+str(count_alienvault_iot_created_2018_anotheryear)+" OBJETOS EN LOS PULSOS CREADOS EN 2018 O ANTERIORMENTE, LA ÚLTIMA MODIFICACIÓN SE PRODUJO MÁS TARDE DE UN AÑO ")
print("\n")








print("*********************PORCENTAJE FECHA DE CREACION/FECHA DE MODIFICACION ALIENVAULT PARTE IOT*********************")
print("\n")                            
                
print("\n")
print(" DE UN TOTAL DE "+str(count_alienvault_iot_entries)+" OBJETOS EN LOS PULSOS :\n") 
print("\n")
print("   - LOS PORCENTAJES DE FECHA DE CREACION SON LOS SIGUIENTES:  \n")
if(count_alienvault_iot_created_2023>0):
    print("      -    EN EL  "+str(float(((count_alienvault_iot_created_2023*100)/count_alienvault_iot_entries)))+" % DE OBJETOS EN LOS PULSOS LA FECHA DE CREACION ES 2023. LOS PORCENTAJES DE FECHA DE MODIFICACION SON LOS SIGUIENTES :  \n")
    print("\n")
    print("            -    EN EL  "+str(float(((count_alienvault_iot_created_2023_modifiedsameday*100)/count_alienvault_iot_created_2023)))+" % DE OBJETOS EN LOS PULSOS CREADOS EN 2023, LA ULTIMA MODIFICACIÓN SE PRODUJO ESE MISMO DÍA ")
    print("            -    EN EL  "+str(float(((count_alienvault_iot_created_2023_modifiedsamemonth*100)/count_alienvault_iot_created_2023)))+" % DE OBJETOS EN LOS PULSOS CREADOS EN 2023, LA ULTIMA MODIFICACIÓN SE PRODUJO ESE MISMO MES")
    print("            -    EN EL  "+str(float(((count_alienvault_iot_created_2023_modifiedsameyear*100)/count_alienvault_iot_created_2023)))+" % DE OBJETOS EN LOS PULSOS CREADOS EN 2023, LA ULTIMA MODIFICACIÓN SE PRODUJO ESE MISMO AÑO ")
    print("            -    EN EL  "+str(float(((count_alienvault_iot_created_2023_anotheryear*100)/count_alienvault_iot_created_2023)))+" % DE OBJETOS EN LOS PULSOS CREADOS EN 2023, LA ULTIMA MODIFICACIÓN SE PRODUJO MÁS TARDE DE UN AÑO ")
    print("\n")
if(count_alienvault_iot_created_2022>0):
    print("      -    EN EL  "+str(float(((count_alienvault_iot_created_2022*100)/count_alienvault_iot_entries)))+" % DE OBJETOS EN LOS PULSOS LA FECHA DE CREACION ES 2022. LOS PORCENTAJES DE FECHA DE MODIFICACION SON LOS SIGUIENTES :  \n")
    print("\n")
    print("            -    EN EL  "+str(float(((count_alienvault_iot_created_2022_modifiedsameday*100)/count_alienvault_iot_created_2022)))+" % DE OBJETOS EN LOS PULSOS CREADOS EN 2022, LA ULTIMA MODIFICACIÓN SE PRODUJO ESE MISMO DÍA ")
    print("            -    EN EL  "+str(float(((count_alienvault_iot_created_2022_modifiedsamemonth*100)/count_alienvault_iot_created_2022)))+" % DE OBJETOS EN LOS PULSOS CREADOS EN 2022, LA ULTIMA MODIFICACIÓN SE PRODUJO ESE MISMO MES")
    print("            -    EN EL  "+str(float(((count_alienvault_iot_created_2022_modifiedsameyear*100)/count_alienvault_iot_created_2022)))+" % DE OBJETOS EN LOS PULSOS CREADOS EN 2022, LA ULTIMA MODIFICACIÓN SE PRODUJO ESE MISMO AÑO ")
    print("            -    EN EL  "+str(float(((count_alienvault_iot_created_2022_anotheryear*100)/count_alienvault_iot_created_2022)))+" % DE OBJETOS EN LOS PULSOS CREADOS EN 2022, LA ULTIMA MODIFICACIÓN SE PRODUJO MÁS TARDE DE UN AÑO ")
    print("\n")
if(count_alienvault_iot_created_2021>0):
    print("      -    EN EL  "+str(float(((count_alienvault_iot_created_2021*100)/count_alienvault_iot_entries)))+" % DE OBJETOS EN LOS PULSOS LA FECHA DE CREACION ES 2021. LOS PORCENTAJES DE FECHA DE MODIFICACION SON LOS SIGUIENTES :  \n")
    print("\n")
    print("            -    EN EL  "+str(float(((count_alienvault_iot_created_2021_modifiedsameday*100)/count_alienvault_iot_created_2021)))+" % DE OBJETOS EN LOS PULSOS CREADOS EN 2021, LA ULTIMA MODIFICACIÓN SE PRODUJO ESE MISMO DÍA ")
    print("            -    EN EL  "+str(float(((count_alienvault_iot_created_2021_modifiedsamemonth*100)/count_alienvault_iot_created_2021)))+" % DE OBJETOS EN LOS PULSOS CREADOS EN 2021, LA ULTIMA MODIFICACIÓN SE PRODUJO ESE MISMO MES")
    print("            -    EN EL  "+str(float(((count_alienvault_iot_created_2021_modifiedsameyear*100)/count_alienvault_iot_created_2021)))+" % DE OBJETOS EN LOS PULSOS CREADOS EN 2021, LA ULTIMA MODIFICACIÓN SE PRODUJO ESE MISMO AÑO ")
    print("            -    EN EL  "+str(float(((count_alienvault_iot_created_2021_anotheryear*100)/count_alienvault_iot_created_2021)))+" % DE OBJETOS EN LOS PULSOS CREADOS EN 2021, LA ULTIMA MODIFICACIÓN SE PRODUJO MÁS TARDE DE UN AÑO ")
    print("\n")
if(count_alienvault_iot_created_2020>0):
    print("      -    EN EL  "+str(float(((count_alienvault_iot_created_2020*100)/count_alienvault_iot_entries)))+" % DE OBJETOS EN LOS PULSOS LA FECHA DE CREACION ES 2020. LOS PORCENTAJES DE FECHA DE MODIFICACION SON LOS SIGUIENTES :  \n")
    print("\n")
    print("            -    EN EL  "+str(float(((count_alienvault_iot_created_2020_modifiedsameday*100)/count_alienvault_iot_created_2020)))+" % DE OBJETOS EN LOS PULSOS CREADOS EN 2020, LA ULTIMA MODIFICACIÓN SE PRODUJO ESE MISMO DÍA ")
    print("            -    EN EL  "+str(float(((count_alienvault_iot_created_2020_modifiedsamemonth*100)/count_alienvault_iot_created_2020)))+" % DE OBJETOS EN LOS PULSOS CREADOS EN 2020, LA ULTIMA MODIFICACIÓN SE PRODUJO ESE MISMO MES")
    print("            -    EN EL  "+str(float(((count_alienvault_iot_created_2020_modifiedsameyear*100)/count_alienvault_iot_created_2020)))+" % DE OBJETOS EN LOS PULSOS CREADOS EN 2020, LA ULTIMA MODIFICACIÓN SE PRODUJO ESE MISMO AÑO ")
    print("            -    EN EL  "+str(float(((count_alienvault_iot_created_2020_anotheryear*100)/count_alienvault_iot_created_2020)))+" % DE OBJETOS EN LOS PULSOS CREADOS EN 2020, LA ULTIMA MODIFICACIÓN SE PRODUJO MÁS TARDE DE UN AÑO ")
    print("\n")
if(count_alienvault_iot_created_2019>0):
    print("      -    EN EL  "+str(float(((count_alienvault_iot_created_2019*100)/count_alienvault_iot_entries)))+" % DE OBJETOS EN LOS PULSOS LA FECHA DE CREACION ES 2019. LOS PORCENTAJES DE FECHA DE MODIFICACION SON LOS SIGUIENTES  \n")
    print("\n")
    print("            -    EN EL  "+str(float(((count_alienvault_iot_created_2019_modifiedsameday*100)/count_alienvault_iot_created_2019)))+" % DE OBJETOS EN LOS PULSOS CREADOS EN 2019, LA ULTIMA MODIFICACIÓN SE PRODUJO ESE MISMO DÍA ")
    print("            -    EN EL  "+str(float(((count_alienvault_iot_created_2019_modifiedsamemonth*100)/count_alienvault_iot_created_2019)))+" % DE OBJETOS EN LOS PULSOS CREADOS EN 2019, LA ULTIMA MODIFICACIÓN SE PRODUJO ESE MISMO MES")
    print("            -    EN EL  "+str(float(((count_alienvault_iot_created_2019_modifiedsameyear*100)/count_alienvault_iot_created_2019)))+" % DE OBJETOS EN LOS PULSOS CREADOS EN 2019, LA ULTIMA MODIFICACIÓN SE PRODUJO ESE MISMO AÑO ")
    print("            -    EN EL  "+str(float(((count_alienvault_iot_created_2019_anotheryear*100)/count_alienvault_iot_created_2019)))+" % DE OBJETOS EN LOS PULSOS CREADOS EN 2019, LA ULTIMA MODIFICACIÓN SE PRODUJO MÁS TARDE DE UN AÑO ")
    print("\n")
if(count_alienvault_iot_created_2018>0):
    print("      -    EN EL  "+str(float(((count_alienvault_iot_created_2018*100)/count_alienvault_iot_entries)))+" % DE OBJETOS EN LOS PULSOS LA FECHA DE CREACION ES 2018 O ANTERIOR. LOS PORCENTAJES DE FECHA DE MODIFICACION SON LOS SIGUIENTES :  \n")
    print("\n")
    print("            -    EN EL  "+str(float(((count_alienvault_iot_created_2018_modifiedsameday*100)/count_alienvault_iot_created_2018)))+" % DE OBJETOS EN LOS PULSOS CREADOS EN 2018 O ANTERIORMENTE, LA ULTIMA MODIFICACIÓN SE PRODUJO ESE MISMO DÍA ")
    print("            -    EN EL  "+str(float(((count_alienvault_iot_created_2018_modifiedsamemonth*100)/count_alienvault_iot_created_2018)))+" % DE OBJETOS EN LOS PULSOS CREADOS EN 2018 O ANTERIORMENTE, LA ULTIMA MODIFICACIÓN SE PRODUJO ESE MISMO MES")
    print("            -    EN EL  "+str(float(((count_alienvault_iot_created_2018_modifiedsameyear*100)/count_alienvault_iot_created_2018)))+" % DE OBJETOS EN LOS PULSOS CREADOS EN 2018 O ANTERIORMENTE, LA ULTIMA MODIFICACIÓN SE PRODUJO ESE MISMO AÑO ")
    print("            -    EN EL  "+str(float(((count_alienvault_iot_created_2018_anotheryear*100)/count_alienvault_iot_created_2018)))+" % DE OBJETOS EN LOS PULSOS CREADOS EN 2018 O ANTERIORMENTE, LA ULTIMA MODIFICACIÓN SE PRODUJO MÁS TARDE DE UN AÑO ")
    print("\n")







#Abro los ficheros con los que voy a tratar




df_alienvault_sh = pd.read_excel('alienvault_smart_home_2023.xlsx')

#Contador total de OBJETOS EN LOS PULSOS de Alienvault
count_alienvault_sh_entries=0
#Contador total de OBJETOS EN LOS PULSOS creados en un anio concreto
count_alienvault_sh_created_2023=0
#Contador total de fecha de modificacion dado un anio cncreto
count_alienvault_sh_created_2023_modifiedsameday=0
count_alienvault_sh_created_2023_modifiedsamemonth=0
count_alienvault_sh_created_2023_modifiedsameyear=0
count_alienvault_sh_created_2023_anotheryear=0

count_alienvault_sh_created_2022=0
count_alienvault_sh_created_2022_modifiedsameday=0
count_alienvault_sh_created_2022_modifiedsamemonth=0
count_alienvault_sh_created_2022_modifiedsameyear=0
count_alienvault_sh_created_2022_anotheryear=0

count_alienvault_sh_created_2021=0
count_alienvault_sh_created_2021_modifiedsameday=0
count_alienvault_sh_created_2021_modifiedsamemonth=0
count_alienvault_sh_created_2021_modifiedsameyear=0
count_alienvault_sh_created_2021_anotheryear=0

count_alienvault_sh_created_2020=0
count_alienvault_sh_created_2020_modifiedsameday=0
count_alienvault_sh_created_2020_modifiedsamemonth=0
count_alienvault_sh_created_2020_modifiedsameyear=0
count_alienvault_sh_created_2020_anotheryear=0

count_alienvault_sh_created_2019=0
count_alienvault_sh_created_2019_modifiedsameday=0
count_alienvault_sh_created_2019_modifiedsamemonth=0
count_alienvault_sh_created_2019_modifiedsameyear=0
count_alienvault_sh_created_2019_anotheryear=0

count_alienvault_sh_created_2018=0
count_alienvault_sh_created_2018_modifiedsameday=0
count_alienvault_sh_created_2018_modifiedsamemonth=0
count_alienvault_sh_created_2018_modifiedsameyear=0
count_alienvault_sh_created_2018_anotheryear=0


#Comprobamos el anio de creacion
for r in range(0,len(df_alienvault_sh["created"])):
    #Si existen varios valores de fecha de creacion para una misma fila
    if('[' in df_alienvault_sh["created"][r]):
        #Obtengo los distintos valores de la fila de fecha de creacion y modificacion
        aux=df_alienvault_sh["created"][r].split(",")
        auxx=df_alienvault_sh["modified"][r].split(",")
        for l in range(0,len(aux)):
            if(len(aux)>0):
                #Si cada valor de creacion tiene un valor de modificacion asignado
                if(len(aux) == len(auxx)):
                    #Obtengo el valor actual de fecha de creacion y modificacion
                    aux_str=aux[l].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","").replace("T"," ")
                    auxx_str=auxx[l].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","").replace("T"," ")
                    #Compruebo que el valor obtenido viene en formato de cadena de tiempo
                    if((aux_str!='NONE' and auxx_str!='NONE') and ('Z' in aux_str and 'Z' in auxx_str)):
                        aux2=aux_str.split(".")
                        #Obtenemos la fecha de creacion
                        creado = datetime.strptime(aux2[0], '%Y-%m-%d %H:%M:%S')
                        aux22=auxx_str.split(".")
                        #Obtenemos la fecha de modificacion
                        modificado = datetime.strptime(aux22[0], '%Y-%m-%d %H:%M:%S')
                        #Calculamos la diferencia entre fecha de creacion y modificacion
                        res=creado-modificado
                        #Obtenemos el anio de creacion
                        str_anio_publishdate_alienvault_sh=aux_str.split("-")
                        anio_publishdate_alienvault_sh=int(str_anio_publishdate_alienvault_sh[0])
                        #Compruebo el anio de creacion
                        if(anio_publishdate_alienvault_sh >= 2023):
                            count_alienvault_sh_entries+=1
                            count_alienvault_sh_created_2023+=1
                            #Compruebo si la diferencia entre fecha de creacion y modificacion es menor de un dia
                            if(((res/ timedelta(days=1))*(-1)) < 1):
                                count_alienvault_sh_created_2023_modifiedsameday+=1
                            #Compruebo si la diferencia entre fecha de creacion y modificacion es menor de un mes
                            elif(((res/ timedelta(days=30))*(-1)) < 1):
                                count_alienvault_sh_created_2023_modifiedsamemonth+=1
                            #Compruebo si la diferencia entre fecha de creacion y modificacion es menor de un anio
                            elif(((res/ timedelta(days=365))*(-1)) < 1):
                                count_alienvault_sh_created_2023_modifiedsameyear+=1
                            #Compruebo si la diferencia entre fecha de creacion y modificacion es mayor de un anio
                            else:
                                count_alienvault_sh_created_2023_anotheryear+=1

                        elif(anio_publishdate_alienvault_sh >= 2022):
                            count_alienvault_sh_entries+=1
                            count_alienvault_sh_created_2022+=1
                            if(((res/ timedelta(days=1))*(-1)) < 1):
                                count_alienvault_sh_created_2022_modifiedsameday+=1

                            elif(((res/ timedelta(days=30))*(-1)) < 1):
                                count_alienvault_sh_created_2022_modifiedsamemonth+=1

                            elif(((res/ timedelta(days=365))*(-1)) < 1):
                                count_alienvault_sh_created_2022_modifiedsameyear+=1

                            else:
                                count_alienvault_sh_created_2022_anotheryear+=1

                        elif(anio_publishdate_alienvault_sh >= 2021):
                            count_alienvault_sh_entries+=1
                            count_alienvault_sh_created_2021+=1
                            if(((res/ timedelta(days=1))*(-1)) < 1):
                                count_alienvault_sh_created_2021_modifiedsameday+=1

                            elif(((res/ timedelta(days=30))*(-1)) < 1):
                                count_alienvault_sh_created_2021_modifiedsamemonth+=1

                            elif(((res/ timedelta(days=365))*(-1)) < 1):
                                count_alienvault_sh_created_2021_modifiedsameyear+=1

                            else:
                                count_alienvault_sh_created_2021_anotheryear+=1

                        elif(anio_publishdate_alienvault_sh >= 2020):
                            count_alienvault_sh_entries+=1
                            count_alienvault_sh_created_2020+=1
                            if(((res/ timedelta(days=1))*(-1)) < 1):
                                count_alienvault_sh_created_2020_modifiedsameday+=1

                            elif(((res/ timedelta(days=30))*(-1)) < 1):
                                count_alienvault_sh_created_2020_modifiedsamemonth+=1

                            elif(((res/ timedelta(days=365))*(-1)) < 1):
                                count_alienvault_sh_created_2020_modifiedsameyear+=1

                            else:
                                count_alienvault_sh_created_2020_anotheryear+=1

                        elif(anio_publishdate_alienvault_sh >= 2019):
                            count_alienvault_sh_entries+=1
                            count_alienvault_sh_created_2019+=1
                            if(((res/ timedelta(days=1))*(-1)) < 1):
                                count_alienvault_sh_created_2019_modifiedsameday+=1

                            elif(((res/ timedelta(days=30))*(-1)) < 1):
                                count_alienvault_sh_created_2019_modifiedsamemonth+=1

                            elif(((res/ timedelta(days=365))*(-1)) < 1):
                                count_alienvault_sh_created_2019_modifiedsameyear+=1

                            else:
                                count_alienvault_sh_created_2019_anotheryear+=1

                        elif(anio_publishdate_alienvault_sh >= 2018):
                            count_alienvault_sh_entries+=1
                            count_alienvault_sh_created_2018+=1
                            if(((res/ timedelta(days=1))*(-1)) < 1):
                                count_alienvault_sh_created_2018_modifiedsameday+=1

                            elif(((res/ timedelta(days=30))*(-1)) < 1):
                                count_alienvault_sh_created_2018_modifiedsamemonth+=1

                            elif(((res/ timedelta(days=365))*(-1)) < 1):
                                count_alienvault_sh_created_2018_modifiedsameyear+=1

                            else:
                                count_alienvault_sh_created_2018_anotheryear+=1

    else:
        #Si existe un unico valor de creacion y modificacion para la fila actual
        #Obtengo los valores
        aux_strr=df_alienvault_sh["created"][r].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","").replace("T"," ")
        auxx_strr=df_alienvault_sh["modified"][r].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","").replace("T"," ")
        if((aux_strr!='NONE' and auxx_strr!='NONE') and ('Z' in aux_strr and 'Z' in auxx_strr)):
            aux22=aux_strr.split(".")
            #Obtenemos fecha de creacion y modificacion
            creado = datetime.strptime(aux22[0], '%Y-%m-%d %H:%M:%S')
            aux222=auxx_strr.split(".")
            modificado = datetime.strptime(aux222[0], '%Y-%m-%d %H:%M:%S')
            #Calculo diferencia temporal
            res=creado-modificado
            str_anio_publishdate_alienvault_sh=auxx_strr.split("-")
            anio_publishdate_alienvault_sh=int(str_anio_publishdate_alienvault_sh[0]) 
            #Compruebo anio de creacion
            if(anio_publishdate_alienvault_sh >= 2023):
                count_alienvault_sh_entries+=1
                count_alienvault_sh_created_2023+=1
                #Compruebo diferencia temporal
                if(((res/ timedelta(days=1))*(-1)) < 1):
                    count_alienvault_sh_created_2023_modifiedsameday+=1

                elif(((res/ timedelta(days=30))*(-1)) < 1):
                    count_alienvault_sh_created_2023_modifiedsamemonth+=1

                elif(((res/ timedelta(days=365))*(-1)) < 1):
                    count_alienvault_sh_created_2023_modifiedsameyear+=1

                else:
                    count_alienvault_sh_created_2023_anotheryear+=1

            elif(anio_publishdate_alienvault_sh >= 2022):
                count_alienvault_sh_entries+=1
                count_alienvault_sh_created_2022+=1
                if(((res/ timedelta(days=1))*(-1)) < 1):
                    count_alienvault_sh_created_2022_modifiedsameday+=1

                elif(((res/ timedelta(days=30))*(-1)) < 1):
                    count_alienvault_sh_created_2022_modifiedsamemonth+=1

                elif(((res/ timedelta(days=365))*(-1)) < 1):
                    count_alienvault_sh_created_2022_modifiedsameyear+=1

                else:
                    count_alienvault_sh_created_2022_anotheryear+=1

            elif(anio_publishdate_alienvault_sh >= 2021):
                count_alienvault_sh_entries+=1
                count_alienvault_sh_created_2021+=1
                if(((res/ timedelta(days=1))*(-1)) < 1):
                    count_alienvault_sh_created_2021_modifiedsameday+=1

                elif(((res/ timedelta(days=30))*(-1)) < 1):
                    count_alienvault_sh_created_2021_modifiedsamemonth+=1

                elif(((res/ timedelta(days=365))*(-1)) < 1):
                    count_alienvault_sh_created_2021_modifiedsameyear+=1

                else:
                    count_alienvault_sh_created_2021_anotheryear+=1

            elif(anio_publishdate_alienvault_sh >= 2020):
                count_alienvault_sh_entries+=1
                count_alienvault_sh_created_2020+=1
                if(((res/ timedelta(days=1))*(-1)) < 1):
                    count_alienvault_sh_created_2020_modifiedsameday+=1

                elif(((res/ timedelta(days=30))*(-1)) < 1):
                    count_alienvault_sh_created_2020_modifiedsamemonth+=1

                elif(((res/ timedelta(days=365))*(-1)) < 1):
                    count_alienvault_sh_created_2020_modifiedsameyear+=1

                else:
                    count_alienvault_sh_created_2020_anotheryear+=1

            elif(anio_publishdate_alienvault_sh >= 2019):
                count_alienvault_sh_entries+=1
                count_alienvault_sh_created_2019+=1
                if(((res/ timedelta(days=1))*(-1)) < 1):
                    count_alienvault_sh_created_2019_modifiedsameday+=1

                elif(((res/ timedelta(days=30))*(-1)) < 1):
                    count_alienvault_sh_created_2019_modifiedsamemonth+=1

                elif(((res/ timedelta(days=365))*(-1)) < 1):
                    count_alienvault_sh_created_2019_modifiedsameyear+=1

                else:
                    count_alienvault_sh_created_2019_anotheryear+=1

            elif(anio_publishdate_alienvault_sh >= 2018):
                count_alienvault_sh_entries+=1
                count_alienvault_sh_created_2018+=1
                if(((res/ timedelta(days=1))*(-1)) < 1):
                    count_alienvault_sh_created_2018_modifiedsameday+=1

                elif(((res/ timedelta(days=30))*(-1)) < 1):
                    count_alienvault_sh_created_2018_modifiedsamemonth+=1

                elif(((res/ timedelta(days=365))*(-1)) < 1):
                    count_alienvault_sh_created_2018_modifiedsameyear+=1

                else:
                    count_alienvault_sh_created_2018_anotheryear+=1        
                            
                    
print("*********************ESTADÍSTICAS FECHA DE CREACION/FECHA DE MODIFICACION ALIENVAULT PARTE SMART HOME*********************")
print("\n")                            
                
print("\n")
print(" DE UN TOTAL DE "+str(count_alienvault_sh_entries)+" OBJETOS EN LOS PULSOS :\n") 
print("\n")
print("   - LAS ESTADISTICAS DE FECHA DE CREACION SON LAS SIGUIENTES:  \n")
print("      -    EN  "+str(count_alienvault_sh_created_2023)+" OBJETOS EN LOS PULSOS LA FECHA DE CREACION ES 2023. LAS ESTADÍSTICAS DE FECHA DE MODIFICACION SON LAS SIGUIENTES :  \n")
print("\n")
print("            -    EN  "+str(count_alienvault_sh_created_2023_modifiedsameday)+" OBJETOS EN LOS PULSOS CREADOS EN 2023, LA ULTIMA MODIFICACIÓN SE PRODUJO ESE MISMO DÍA ")
print("            -    EN  "+str(count_alienvault_sh_created_2023_modifiedsamemonth)+" OBJETOS EN LOS PULSOS CREADOS EN 2023, LA ÚLTIMA MODIFICACIÓN SE PRODUJO ESE MISMO MES")
print("            -    EN  "+str(count_alienvault_sh_created_2023_modifiedsameyear)+" OBJETOS EN LOS PULSOS CREADOS EN 2023, LA ÚLTIMA MODIFICACIÓN SE PRODUJO ESE MISMO AÑO ")
print("            -    EN  "+str(count_alienvault_sh_created_2023_anotheryear)+" OBJETOS EN LOS PULSOS CREADOS EN 2023, LA ÚLTIMA MODIFICACIÓN SE PRODUJO MÁS TARDE DE UN AÑO ")
print("\n")
print("      -    EN  "+str(count_alienvault_sh_created_2022)+" OBJETOS EN LOS PULSOS LA FECHA DE CREACION ES 2022. LAS ESTADÍSTICAS DE FECHA DE MODIFICACION SON LAS SIGUIENTES :  \n")
print("\n")
print("            -    EN  "+str(count_alienvault_sh_created_2022_modifiedsameday)+" OBJETOS EN LOS PULSOS CREADOS EN 2022, LA ULTIMA MODIFICACIÓN SE PRODUJO ESE MISMO DÍA ")
print("            -    EN  "+str(count_alienvault_sh_created_2022_modifiedsamemonth)+" OBJETOS EN LOS PULSOS CREADOS EN 2022, LA ÚLTIMA MODIFICACIÓN SE PRODUJO ESE MISMO MES")
print("            -    EN  "+str(count_alienvault_sh_created_2022_modifiedsameyear)+" OBJETOS EN LOS PULSOS CREADOS EN 2022, LA ÚLTIMA MODIFICACIÓN SE PRODUJO ESE MISMO AÑO ")
print("            -    EN  "+str(count_alienvault_sh_created_2022_anotheryear)+" OBJETOS EN LOS PULSOS CREADOS EN 2022, LA ÚLTIMA MODIFICACIÓN SE PRODUJO MÁS TARDE DE UN AÑO ")
print("\n")
print("      -    EN  "+str(count_alienvault_sh_created_2021)+" OBJETOS EN LOS PULSOS LA FECHA DE CREACION ES 2021. LAS ESTADÍSTICAS DE FECHA DE MODIFICACION SON LAS SIGUIENTES :  \n")
print("\n")
print("            -    EN  "+str(count_alienvault_sh_created_2021_modifiedsameday)+" OBJETOS EN LOS PULSOS CREADOS EN 2021, LA ULTIMA MODIFICACIÓN SE PRODUJO ESE MISMO DÍA ")
print("            -    EN  "+str(count_alienvault_sh_created_2021_modifiedsamemonth)+" OBJETOS EN LOS PULSOS CREADOS EN 2021, LA ÚLTIMA MODIFICACIÓN SE PRODUJO ESE MISMO MES")
print("            -    EN  "+str(count_alienvault_sh_created_2021_modifiedsameyear)+" OBJETOS EN LOS PULSOS CREADOS EN 2021, LA ÚLTIMA MODIFICACIÓN SE PRODUJO ESE MISMO AÑO ")
print("            -    EN  "+str(count_alienvault_sh_created_2021_anotheryear)+" OBJETOS EN LOS PULSOS CREADOS EN 2021, LA ÚLTIMA MODIFICACIÓN SE PRODUJO MÁS TARDE DE UN AÑO ")
print("\n")
print("      -    EN  "+str(count_alienvault_sh_created_2020)+" OBJETOS EN LOS PULSOS LA FECHA DE CREACION ES 2020. LAS ESTADÍSTICAS DE FECHA DE MODIFICACION SON LAS SIGUIENTES :  \n")
print("\n")
print("            -    EN  "+str(count_alienvault_sh_created_2020_modifiedsameday)+" OBJETOS EN LOS PULSOS CREADOS EN 2020, LA ULTIMA MODIFICACIÓN SE PRODUJO ESE MISMO DÍA ")
print("            -    EN  "+str(count_alienvault_sh_created_2020_modifiedsamemonth)+" OBJETOS EN LOS PULSOS CREADOS EN 2020, LA ÚLTIMA MODIFICACIÓN SE PRODUJO ESE MISMO MES")
print("            -    EN  "+str(count_alienvault_sh_created_2020_modifiedsameyear)+" OBJETOS EN LOS PULSOS CREADOS EN 2020, LA ÚLTIMA MODIFICACIÓN SE PRODUJO ESE MISMO AÑO ")
print("            -    EN  "+str(count_alienvault_sh_created_2020_anotheryear)+" OBJETOS EN LOS PULSOS CREADOS EN 2020, LA ÚLTIMA MODIFICACIÓN SE PRODUJO MÁS TARDE DE UN AÑO ")
print("\n")
print("      -    EN  "+str(count_alienvault_sh_created_2019)+" OBJETOS EN LOS PULSOS LA FECHA DE CREACION ES 2019. LAS ESTADÍSTICAS DE FECHA DE MODIFICACION SON LAS SIGUIENTES :  \n")
print("\n")
print("            -    EN  "+str(count_alienvault_sh_created_2019_modifiedsameday)+" OBJETOS EN LOS PULSOS CREADOS EN 2019, LA ULTIMA MODIFICACIÓN SE PRODUJO ESE MISMO DÍA ")
print("            -    EN  "+str(count_alienvault_sh_created_2019_modifiedsamemonth)+" OBJETOS EN LOS PULSOS CREADOS EN 2019, LA ÚLTIMA MODIFICACIÓN SE PRODUJO ESE MISMO MES")
print("            -    EN  "+str(count_alienvault_sh_created_2019_modifiedsameyear)+" OBJETOS EN LOS PULSOS CREADOS EN 2019, LA ÚLTIMA MODIFICACIÓN SE PRODUJO ESE MISMO AÑO ")
print("            -    EN  "+str(count_alienvault_sh_created_2019_anotheryear)+" OBJETOS EN LOS PULSOS CREADOS EN 2019, LA ÚLTIMA MODIFICACIÓN SE PRODUJO MÁS TARDE DE UN AÑO ")
print("\n")
print("      -    EN  "+str(count_alienvault_sh_created_2018)+" OBJETOS EN LOS PULSOS LA FECHA DE CREACION ES 2018 O ANTERIOR. LAS ESTADÍSTICAS DE FECHA DE MODIFICACION SON LAS SIGUIENTES :  \n")
print("\n")
print("            -    EN  "+str(count_alienvault_sh_created_2018_modifiedsameday)+" OBJETOS EN LOS PULSOS CREADOS EN 2018 O ANTERIORMENTE, LA ULTIMA MODIFICACIÓN SE PRODUJO ESE MISMO DÍA ")
print("            -    EN  "+str(count_alienvault_sh_created_2018_modifiedsamemonth)+" OBJETOS EN LOS PULSOS CREADOS EN 2018 O ANTERIORMENTE, LA ÚLTIMA MODIFICACIÓN SE PRODUJO ESE MISMO MES")
print("            -    EN  "+str(count_alienvault_sh_created_2018_modifiedsameyear)+" OBJETOS EN LOS PULSOS CREADOS EN 2018 O ANTERIORMENTE, LA ÚLTIMA MODIFICACIÓN SE PRODUJO ESE MISMO AÑO ")
print("            -    EN  "+str(count_alienvault_sh_created_2018_anotheryear)+" OBJETOS EN LOS PULSOS CREADOS EN 2018 O ANTERIORMENTE, LA ÚLTIMA MODIFICACIÓN SE PRODUJO MÁS TARDE DE UN AÑO ")
print("\n")








print("*********************PORCENTAJE FECHA DE CREACION/FECHA DE MODIFICACION ALIENVAULT PARTE SMART HOME*********************")
print("\n")                            
                
print("\n")
print(" DE UN TOTAL DE "+str(count_alienvault_sh_entries)+" OBJETOS EN LOS PULSOS :\n") 
print("\n")
print("   - LOS PORCENTAJES DE FECHA DE CREACION SON LOS SIGUIENTES:  \n")
if(count_alienvault_sh_created_2023>0):
    print("      -    EN EL  "+str(float(((count_alienvault_sh_created_2023*100)/count_alienvault_sh_entries)))+" % DE OBJETOS EN LOS PULSOS LA FECHA DE CREACION ES 2023. LOS PORCENTAJES DE FECHA DE MODIFICACION SON LOS SIGUIENTES :  \n")
    print("\n")
    print("            -    EN EL  "+str(float(((count_alienvault_sh_created_2023_modifiedsameday*100)/count_alienvault_sh_created_2023)))+" % DE OBJETOS EN LOS PULSOS CREADOS EN 2023, LA ULTIMA MODIFICACIÓN SE PRODUJO ESE MISMO DÍA ")
    print("            -    EN EL  "+str(float(((count_alienvault_sh_created_2023_modifiedsamemonth*100)/count_alienvault_sh_created_2023)))+" % DE OBJETOS EN LOS PULSOS CREADOS EN 2023, LA ULTIMA MODIFICACIÓN SE PRODUJO ESE MISMO MES")
    print("            -    EN EL  "+str(float(((count_alienvault_sh_created_2023_modifiedsameyear*100)/count_alienvault_sh_created_2023)))+" % DE OBJETOS EN LOS PULSOS CREADOS EN 2023, LA ULTIMA MODIFICACIÓN SE PRODUJO ESE MISMO AÑO ")
    print("            -    EN EL  "+str(float(((count_alienvault_sh_created_2023_anotheryear*100)/count_alienvault_sh_created_2023)))+" % DE OBJETOS EN LOS PULSOS CREADOS EN 2023, LA ULTIMA MODIFICACIÓN SE PRODUJO MÁS TARDE DE UN AÑO ")
    print("\n")
if(count_alienvault_sh_created_2022>0):
    print("      -    EN EL  "+str(float(((count_alienvault_sh_created_2022*100)/count_alienvault_sh_entries)))+" % DE OBJETOS EN LOS PULSOS LA FECHA DE CREACION ES 2022. LOS PORCENTAJES DE FECHA DE MODIFICACION SON LOS SIGUIENTES :  \n")
    print("\n")
    print("            -    EN EL  "+str(float(((count_alienvault_sh_created_2022_modifiedsameday*100)/count_alienvault_sh_created_2022)))+" % DE OBJETOS EN LOS PULSOS CREADOS EN 2022, LA ULTIMA MODIFICACIÓN SE PRODUJO ESE MISMO DÍA ")
    print("            -    EN EL  "+str(float(((count_alienvault_sh_created_2022_modifiedsamemonth*100)/count_alienvault_sh_created_2022)))+" % DE OBJETOS EN LOS PULSOS CREADOS EN 2022, LA ULTIMA MODIFICACIÓN SE PRODUJO ESE MISMO MES")
    print("            -    EN EL  "+str(float(((count_alienvault_sh_created_2022_modifiedsameyear*100)/count_alienvault_sh_created_2022)))+" % DE OBJETOS EN LOS PULSOS CREADOS EN 2022, LA ULTIMA MODIFICACIÓN SE PRODUJO ESE MISMO AÑO ")
    print("            -    EN EL  "+str(float(((count_alienvault_sh_created_2022_anotheryear*100)/count_alienvault_sh_created_2022)))+" % DE OBJETOS EN LOS PULSOS CREADOS EN 2022, LA ULTIMA MODIFICACIÓN SE PRODUJO MÁS TARDE DE UN AÑO ")
    print("\n")
if(count_alienvault_sh_created_2021>0):
    print("      -    EN EL  "+str(float(((count_alienvault_sh_created_2021*100)/count_alienvault_sh_entries)))+" % DE OBJETOS EN LOS PULSOS LA FECHA DE CREACION ES 2021. LOS PORCENTAJES DE FECHA DE MODIFICACION SON LOS SIGUIENTES :  \n")
    print("\n")
    print("            -    EN EL  "+str(float(((count_alienvault_sh_created_2021_modifiedsameday*100)/count_alienvault_sh_created_2021)))+" % DE OBJETOS EN LOS PULSOS CREADOS EN 2021, LA ULTIMA MODIFICACIÓN SE PRODUJO ESE MISMO DÍA ")
    print("            -    EN EL  "+str(float(((count_alienvault_sh_created_2021_modifiedsamemonth*100)/count_alienvault_sh_created_2021)))+" % DE OBJETOS EN LOS PULSOS CREADOS EN 2021, LA ULTIMA MODIFICACIÓN SE PRODUJO ESE MISMO MES")
    print("            -    EN EL  "+str(float(((count_alienvault_sh_created_2021_modifiedsameyear*100)/count_alienvault_sh_created_2021)))+" % DE OBJETOS EN LOS PULSOS CREADOS EN 2021, LA ULTIMA MODIFICACIÓN SE PRODUJO ESE MISMO AÑO ")
    print("            -    EN EL  "+str(float(((count_alienvault_sh_created_2021_anotheryear*100)/count_alienvault_sh_created_2021)))+" % DE OBJETOS EN LOS PULSOS CREADOS EN 2021, LA ULTIMA MODIFICACIÓN SE PRODUJO MÁS TARDE DE UN AÑO ")
    print("\n")
if(count_alienvault_sh_created_2020>0):
    print("      -    EN EL  "+str(float(((count_alienvault_sh_created_2020*100)/count_alienvault_sh_entries)))+" % DE OBJETOS EN LOS PULSOS LA FECHA DE CREACION ES 2020. LOS PORCENTAJES DE FECHA DE MODIFICACION SON LOS SIGUIENTES :  \n")
    print("\n")
    print("            -    EN EL  "+str(float(((count_alienvault_sh_created_2020_modifiedsameday*100)/count_alienvault_sh_created_2020)))+" % DE OBJETOS EN LOS PULSOS CREADOS EN 2020, LA ULTIMA MODIFICACIÓN SE PRODUJO ESE MISMO DÍA ")
    print("            -    EN EL  "+str(float(((count_alienvault_sh_created_2020_modifiedsamemonth*100)/count_alienvault_sh_created_2020)))+" % DE OBJETOS EN LOS PULSOS CREADOS EN 2020, LA ULTIMA MODIFICACIÓN SE PRODUJO ESE MISMO MES")
    print("            -    EN EL  "+str(float(((count_alienvault_sh_created_2020_modifiedsameyear*100)/count_alienvault_sh_created_2020)))+" % DE OBJETOS EN LOS PULSOS CREADOS EN 2020, LA ULTIMA MODIFICACIÓN SE PRODUJO ESE MISMO AÑO ")
    print("            -    EN EL  "+str(float(((count_alienvault_sh_created_2020_anotheryear*100)/count_alienvault_sh_created_2020)))+" % DE OBJETOS EN LOS PULSOS CREADOS EN 2020, LA ULTIMA MODIFICACIÓN SE PRODUJO MÁS TARDE DE UN AÑO ")
    print("\n")
if(count_alienvault_sh_created_2019>0):
    print("      -    EN EL  "+str(float(((count_alienvault_sh_created_2019*100)/count_alienvault_sh_entries)))+" % DE OBJETOS EN LOS PULSOS LA FECHA DE CREACION ES 2019. LOS PORCENTAJES DE FECHA DE MODIFICACION SON LOS SIGUIENTES  \n")
    print("\n")
    print("            -    EN EL  "+str(float(((count_alienvault_sh_created_2019_modifiedsameday*100)/count_alienvault_sh_created_2019)))+" % DE OBJETOS EN LOS PULSOS CREADOS EN 2019, LA ULTIMA MODIFICACIÓN SE PRODUJO ESE MISMO DÍA ")
    print("            -    EN EL  "+str(float(((count_alienvault_sh_created_2019_modifiedsamemonth*100)/count_alienvault_sh_created_2019)))+" % DE OBJETOS EN LOS PULSOS CREADOS EN 2019, LA ULTIMA MODIFICACIÓN SE PRODUJO ESE MISMO MES")
    print("            -    EN EL  "+str(float(((count_alienvault_sh_created_2019_modifiedsameyear*100)/count_alienvault_sh_created_2019)))+" % DE OBJETOS EN LOS PULSOS CREADOS EN 2019, LA ULTIMA MODIFICACIÓN SE PRODUJO ESE MISMO AÑO ")
    print("            -    EN EL  "+str(float(((count_alienvault_sh_created_2019_anotheryear*100)/count_alienvault_sh_created_2019)))+" % DE OBJETOS EN LOS PULSOS CREADOS EN 2019, LA ULTIMA MODIFICACIÓN SE PRODUJO MÁS TARDE DE UN AÑO ")
    print("\n")
if(count_alienvault_sh_created_2018>0):
    print("      -    EN EL  "+str(float(((count_alienvault_sh_created_2018*100)/count_alienvault_sh_entries)))+" % DE OBJETOS EN LOS PULSOS LA FECHA DE CREACION ES 2018 O ANTERIOR. LOS PORCENTAJES DE FECHA DE MODIFICACION SON LOS SIGUIENTES :  \n")
    print("\n")
    print("            -    EN EL  "+str(float(((count_alienvault_sh_created_2018_modifiedsameday*100)/count_alienvault_sh_created_2018)))+" % DE OBJETOS EN LOS PULSOS CREADOS EN 2018 O ANTERIORMENTE, LA ULTIMA MODIFICACIÓN SE PRODUJO ESE MISMO DÍA ")
    print("            -    EN EL  "+str(float(((count_alienvault_sh_created_2018_modifiedsamemonth*100)/count_alienvault_sh_created_2018)))+" % DE OBJETOS EN LOS PULSOS CREADOS EN 2018 O ANTERIORMENTE, LA ULTIMA MODIFICACIÓN SE PRODUJO ESE MISMO MES")
    print("            -    EN EL  "+str(float(((count_alienvault_sh_created_2018_modifiedsameyear*100)/count_alienvault_sh_created_2018)))+" % DE OBJETOS EN LOS PULSOS CREADOS EN 2018 O ANTERIORMENTE, LA ULTIMA MODIFICACIÓN SE PRODUJO ESE MISMO AÑO ")
    print("            -    EN EL  "+str(float(((count_alienvault_sh_created_2018_anotheryear*100)/count_alienvault_sh_created_2018)))+" % DE OBJETOS EN LOS PULSOS CREADOS EN 2018 O ANTERIORMENTE, LA ULTIMA MODIFICACIÓN SE PRODUJO MÁS TARDE DE UN AÑO ")
    print("\n")






print("*********************ESTADÍSTICAS FECHA DE CREACION/FECHA DE MODIFICACION ALIENVAULT PARTE IOT Y SMART HOME CONJUNTAS*********************")
print("\n")                            
                
print("\n")
print(" DE UN TOTAL DE "+str(count_alienvault_sh_entries+count_alienvault_iot_entries)+" OBJETOS EN LOS PULSOS :\n") 
print("\n")
print("   - LAS ESTADISTICAS DE FECHA DE CREACION SON LAS SIGUIENTES:  \n")
print("      -    EN  "+str(count_alienvault_sh_created_2023+count_alienvault_iot_created_2023)+" OBJETOS EN LOS PULSOS LA FECHA DE CREACION ES 2023. LAS ESTADÍSTICAS DE FECHA DE MODIFICACION SON LAS SIGUIENTES :  \n")
print("\n")
print("            -    EN  "+str(count_alienvault_sh_created_2023_modifiedsameday+count_alienvault_iot_created_2023_modifiedsameday)+" OBJETOS EN LOS PULSOS CREADOS EN 2023, LA ULTIMA MODIFICACIÓN SE PRODUJO ESE MISMO DÍA ")
print("            -    EN  "+str(count_alienvault_sh_created_2023_modifiedsamemonth+count_alienvault_iot_created_2023_modifiedsamemonth)+" OBJETOS EN LOS PULSOS CREADOS EN 2023, LA ÚLTIMA MODIFICACIÓN SE PRODUJO ESE MISMO MES")
print("            -    EN  "+str(count_alienvault_sh_created_2023_modifiedsameyear+count_alienvault_iot_created_2023_modifiedsameyear)+" OBJETOS EN LOS PULSOS CREADOS EN 2023, LA ÚLTIMA MODIFICACIÓN SE PRODUJO ESE MISMO AÑO ")
print("            -    EN  "+str(count_alienvault_sh_created_2023_anotheryear+count_alienvault_iot_created_2023_anotheryear)+" OBJETOS EN LOS PULSOS CREADOS EN 2023, LA ÚLTIMA MODIFICACIÓN SE PRODUJO MÁS TARDE DE UN AÑO ")
print("\n")
print("      -    EN  "+str(count_alienvault_sh_created_2022+count_alienvault_iot_created_2022)+" OBJETOS EN LOS PULSOS LA FECHA DE CREACION ES 2022. LAS ESTADÍSTICAS DE FECHA DE MODIFICACION SON LAS SIGUIENTES :  \n")
print("\n")
print("            -    EN  "+str(count_alienvault_sh_created_2022_modifiedsameday+count_alienvault_iot_created_2022_modifiedsameday)+" OBJETOS EN LOS PULSOS CREADOS EN 2022, LA ULTIMA MODIFICACIÓN SE PRODUJO ESE MISMO DÍA ")
print("            -    EN  "+str(count_alienvault_sh_created_2022_modifiedsamemonth+count_alienvault_iot_created_2022_modifiedsamemonth)+" OBJETOS EN LOS PULSOS CREADOS EN 2022, LA ÚLTIMA MODIFICACIÓN SE PRODUJO ESE MISMO MES")
print("            -    EN  "+str(count_alienvault_sh_created_2022_modifiedsameyear+count_alienvault_iot_created_2022_modifiedsameyear)+" OBJETOS EN LOS PULSOS CREADOS EN 2022, LA ÚLTIMA MODIFICACIÓN SE PRODUJO ESE MISMO AÑO ")
print("            -    EN  "+str(count_alienvault_sh_created_2022_anotheryear+count_alienvault_iot_created_2022_anotheryear)+" OBJETOS EN LOS PULSOS CREADOS EN 2022, LA ÚLTIMA MODIFICACIÓN SE PRODUJO MÁS TARDE DE UN AÑO ")
print("\n")
print("      -    EN  "+str(count_alienvault_sh_created_2021+count_alienvault_iot_created_2021)+" OBJETOS EN LOS PULSOS LA FECHA DE CREACION ES 2021. LAS ESTADÍSTICAS DE FECHA DE MODIFICACION SON LAS SIGUIENTES :  \n")
print("\n")
print("            -    EN  "+str(count_alienvault_sh_created_2021_modifiedsameday+count_alienvault_iot_created_2021_modifiedsameday)+" OBJETOS EN LOS PULSOS CREADOS EN 2021, LA ULTIMA MODIFICACIÓN SE PRODUJO ESE MISMO DÍA ")
print("            -    EN  "+str(count_alienvault_sh_created_2021_modifiedsamemonth+count_alienvault_iot_created_2021_modifiedsamemonth)+" OBJETOS EN LOS PULSOS CREADOS EN 2021, LA ÚLTIMA MODIFICACIÓN SE PRODUJO ESE MISMO MES")
print("            -    EN  "+str(count_alienvault_sh_created_2021_modifiedsameyear+count_alienvault_iot_created_2021_modifiedsameyear)+" OBJETOS EN LOS PULSOS CREADOS EN 2021, LA ÚLTIMA MODIFICACIÓN SE PRODUJO ESE MISMO AÑO ")
print("            -    EN  "+str(count_alienvault_sh_created_2021_anotheryear+count_alienvault_iot_created_2021_anotheryear)+" OBJETOS EN LOS PULSOS CREADOS EN 2021, LA ÚLTIMA MODIFICACIÓN SE PRODUJO MÁS TARDE DE UN AÑO ")
print("\n")
print("      -    EN  "+str(count_alienvault_sh_created_2020+count_alienvault_iot_created_2020)+" OBJETOS EN LOS PULSOS LA FECHA DE CREACION ES 2020. LAS ESTADÍSTICAS DE FECHA DE MODIFICACION SON LAS SIGUIENTES :  \n")
print("\n")
print("            -    EN  "+str(count_alienvault_sh_created_2020_modifiedsameday+count_alienvault_iot_created_2020_modifiedsameday)+" OBJETOS EN LOS PULSOS CREADOS EN 2020, LA ULTIMA MODIFICACIÓN SE PRODUJO ESE MISMO DÍA ")
print("            -    EN  "+str(count_alienvault_sh_created_2020_modifiedsamemonth+count_alienvault_iot_created_2020_modifiedsamemonth)+" OBJETOS EN LOS PULSOS CREADOS EN 2020, LA ÚLTIMA MODIFICACIÓN SE PRODUJO ESE MISMO MES")
print("            -    EN  "+str(count_alienvault_sh_created_2020_modifiedsameyear+count_alienvault_iot_created_2020_modifiedsameyear)+" OBJETOS EN LOS PULSOS CREADOS EN 2020, LA ÚLTIMA MODIFICACIÓN SE PRODUJO ESE MISMO AÑO ")
print("            -    EN  "+str(count_alienvault_sh_created_2020_anotheryear+count_alienvault_iot_created_2020_anotheryear)+" OBJETOS EN LOS PULSOS CREADOS EN 2020, LA ÚLTIMA MODIFICACIÓN SE PRODUJO MÁS TARDE DE UN AÑO ")
print("\n")
print("      -    EN  "+str(count_alienvault_sh_created_2019+count_alienvault_iot_created_2019)+" OBJETOS EN LOS PULSOS LA FECHA DE CREACION ES 2019. LAS ESTADÍSTICAS DE FECHA DE MODIFICACION SON LAS SIGUIENTES :  \n")
print("\n")
print("            -    EN  "+str(count_alienvault_sh_created_2019_modifiedsameday+count_alienvault_iot_created_2019_modifiedsameday)+" OBJETOS EN LOS PULSOS CREADOS EN 2019, LA ULTIMA MODIFICACIÓN SE PRODUJO ESE MISMO DÍA ")
print("            -    EN  "+str(count_alienvault_sh_created_2019_modifiedsamemonth+count_alienvault_iot_created_2019_modifiedsamemonth)+" OBJETOS EN LOS PULSOS CREADOS EN 2019, LA ÚLTIMA MODIFICACIÓN SE PRODUJO ESE MISMO MES")
print("            -    EN  "+str(count_alienvault_sh_created_2019_modifiedsameyear+count_alienvault_iot_created_2019_modifiedsameyear)+" OBJETOS EN LOS PULSOS CREADOS EN 2019, LA ÚLTIMA MODIFICACIÓN SE PRODUJO ESE MISMO AÑO ")
print("            -    EN  "+str(count_alienvault_sh_created_2019_anotheryear+count_alienvault_iot_created_2019_anotheryear)+" OBJETOS EN LOS PULSOS CREADOS EN 2019, LA ÚLTIMA MODIFICACIÓN SE PRODUJO MÁS TARDE DE UN AÑO ")
print("\n")
print("      -    EN  "+str(count_alienvault_sh_created_2018+count_alienvault_iot_created_2018)+" OBJETOS EN LOS PULSOS LA FECHA DE CREACION ES 2018. LAS ESTADÍSTICAS DE FECHA DE MODIFICACION SON LAS SIGUIENTES :  \n")
print("\n")
print("            -    EN  "+str(count_alienvault_sh_created_2018_modifiedsameday+count_alienvault_iot_created_2018_modifiedsameday)+" OBJETOS EN LOS PULSOS CREADOS EN 2018, LA ULTIMA MODIFICACIÓN SE PRODUJO ESE MISMO DÍA ")
print("            -    EN  "+str(count_alienvault_sh_created_2018_modifiedsamemonth+count_alienvault_iot_created_2018_modifiedsamemonth)+" OBJETOS EN LOS PULSOS CREADOS EN 2018, LA ÚLTIMA MODIFICACIÓN SE PRODUJO ESE MISMO MES")
print("            -    EN  "+str(count_alienvault_sh_created_2018_modifiedsameyear+count_alienvault_iot_created_2018_modifiedsameyear)+" OBJETOS EN LOS PULSOS CREADOS EN 2018, LA ÚLTIMA MODIFICACIÓN SE PRODUJO ESE MISMO AÑO ")
print("            -    EN  "+str(count_alienvault_sh_created_2018_anotheryear+count_alienvault_iot_created_2018_anotheryear)+" OBJETOS EN LOS PULSOS CREADOS EN 2018, LA ÚLTIMA MODIFICACIÓN SE PRODUJO MÁS TARDE DE UN AÑO ")
print("\n")













print("*********************PORCENTAJE FECHA DE CREACION/FECHA DE MODIFICACION ALIENVAULT PARTE IOT Y SMART HOME CONJUNTAS*********************")
print("\n")                            
                
print("\n")
print(" DE UN TOTAL DE "+str(count_alienvault_sh_entries+count_alienvault_iot_entries)+" OBJETOS EN LOS PULSOS :\n") 
print("\n")
print("   - LOS PORCENTAJES DE FECHA DE CREACION SON LOS SIGUIENTES:  \n")
print("      -    EN EL  "+str(float(((count_alienvault_sh_created_2023+count_alienvault_iot_created_2023)*100)/(count_alienvault_sh_entries+count_alienvault_iot_entries)))+" % DE OBJETOS EN LOS PULSOS LA FECHA DE CREACION ES 2023. LOS PORCENTAJES DE FECHA DE MODIFICACION SON LOS SIGUIENTES :  \n")
print("\n")
print("            -    EN EL  "+str(float((((count_alienvault_sh_created_2023_modifiedsameday+count_alienvault_iot_created_2023_modifiedsameday)*100)/(count_alienvault_sh_created_2023+count_alienvault_iot_created_2023))))+" % DE OBJETOS EN LOS PULSOS CREADOS EN 2023, LA ULTIMA MODIFICACIÓN SE PRODUJO ESE MISMO DÍA ")
print("            -    EN EL  "+str(float((((count_alienvault_sh_created_2023_modifiedsamemonth+count_alienvault_iot_created_2023_modifiedsamemonth)*100)/(count_alienvault_sh_created_2023+count_alienvault_iot_created_2023))))+" % DE OBJETOS EN LOS PULSOS CREADOS EN 2023, LA ULTIMA MODIFICACIÓN SE PRODUJO ESE MISMO MES")
print("            -    EN EL  "+str(float((((count_alienvault_sh_created_2023_modifiedsameyear+count_alienvault_iot_created_2023_modifiedsameyear)*100)/(count_alienvault_sh_created_2023+count_alienvault_iot_created_2023))))+" % DE OBJETOS EN LOS PULSOS CREADOS EN 2023, LA ULTIMA MODIFICACIÓN SE PRODUJO ESE MISMO AÑO ")
print("            -    EN EL  "+str(float((((count_alienvault_sh_created_2023_anotheryear+count_alienvault_iot_created_2023_anotheryear)*100)/(count_alienvault_sh_created_2023+count_alienvault_iot_created_2023))))+" % DE OBJETOS EN LOS PULSOS CREADOS EN 2023, LA ULTIMA MODIFICACIÓN SE PRODUJO MÁS TARDE DE UN AÑO ")
print("\n")
print("      -    EN EL  "+str(float(((count_alienvault_sh_created_2022+count_alienvault_iot_created_2022)*100)/(count_alienvault_sh_entries+count_alienvault_iot_entries)))+" % DE OBJETOS EN LOS PULSOS LA FECHA DE CREACION ES 2022. LOS PORCENTAJES DE FECHA DE MODIFICACION SON LOS SIGUIENTES :  \n")
print("\n")
print("            -    EN EL  "+str(float((((count_alienvault_sh_created_2022_modifiedsameday+count_alienvault_iot_created_2022_modifiedsameday)*100)/(count_alienvault_sh_created_2022+count_alienvault_iot_created_2022))))+" % DE OBJETOS EN LOS PULSOS CREADOS EN 2022, LA ULTIMA MODIFICACIÓN SE PRODUJO ESE MISMO DÍA ")
print("            -    EN EL  "+str(float((((count_alienvault_sh_created_2022_modifiedsamemonth+count_alienvault_iot_created_2022_modifiedsamemonth)*100)/(count_alienvault_sh_created_2022+count_alienvault_iot_created_2022))))+" % DE OBJETOS EN LOS PULSOS CREADOS EN 2022, LA ULTIMA MODIFICACIÓN SE PRODUJO ESE MISMO MES")
print("            -    EN EL  "+str(float((((count_alienvault_sh_created_2022_modifiedsameyear+count_alienvault_iot_created_2022_modifiedsameyear)*100)/(count_alienvault_sh_created_2022+count_alienvault_iot_created_2022))))+" % DE OBJETOS EN LOS PULSOS CREADOS EN 2022, LA ULTIMA MODIFICACIÓN SE PRODUJO ESE MISMO AÑO ")
print("            -    EN EL  "+str(float((((count_alienvault_sh_created_2022_anotheryear+count_alienvault_iot_created_2022_anotheryear)*100)/(count_alienvault_sh_created_2022+count_alienvault_iot_created_2022))))+" % DE OBJETOS EN LOS PULSOS CREADOS EN 2022, LA ULTIMA MODIFICACIÓN SE PRODUJO MÁS TARDE DE UN AÑO ")
print("\n")
if((count_alienvault_sh_created_2021+count_alienvault_iot_created_2021)>0):
    print("      -    EN EL  "+str(float(((count_alienvault_sh_created_2021+count_alienvault_iot_created_2021)*100)/(count_alienvault_sh_entries+count_alienvault_iot_entries)))+" % DE OBJETOS EN LOS PULSOS LA FECHA DE CREACION ES 2021. LOS PORCENTAJES DE FECHA DE MODIFICACION SON LOS SIGUIENTES  \n")
    print("\n")
    print("            -    EN EL  "+str(float((((count_alienvault_sh_created_2021_modifiedsameday+count_alienvault_iot_created_2021_modifiedsameday)*100)/(count_alienvault_sh_created_2021+count_alienvault_iot_created_2021))))+" % DE OBJETOS EN LOS PULSOS CREADOS EN 2021, LA ULTIMA MODIFICACIÓN SE PRODUJO ESE MISMO DÍA ")
    print("            -    EN EL  "+str(float((((count_alienvault_sh_created_2021_modifiedsamemonth+count_alienvault_iot_created_2021_modifiedsamemonth)*100)/(count_alienvault_sh_created_2021+count_alienvault_iot_created_2021))))+" % DE OBJETOS EN LOS PULSOS CREADOS EN 2021, LA ULTIMA MODIFICACIÓN SE PRODUJO ESE MISMO MES")
    print("            -    EN EL  "+str(float((((count_alienvault_sh_created_2021_modifiedsameyear+count_alienvault_iot_created_2021_modifiedsameyear)*100)/(count_alienvault_sh_created_2021+count_alienvault_iot_created_2021))))+" % DE OBJETOS EN LOS PULSOS CREADOS EN 2021, LA ULTIMA MODIFICACIÓN SE PRODUJO ESE MISMO AÑO ")
    print("            -    EN EL  "+str(float((((count_alienvault_sh_created_2021_anotheryear+count_alienvault_iot_created_2021_anotheryear)*100)/(count_alienvault_sh_created_2021+count_alienvault_iot_created_2021))))+" % DE OBJETOS EN LOS PULSOS CREADOS EN 2021, LA ULTIMA MODIFICACIÓN SE PRODUJO MÁS TARDE DE UN AÑO ")
    print("\n")
if((count_alienvault_sh_created_2020+count_alienvault_iot_created_2020)>0):
    print("      -    EN EL  "+str(float(((count_alienvault_sh_created_2020+count_alienvault_iot_created_2020)*100)/(count_alienvault_sh_entries+count_alienvault_iot_entries)))+" % DE OBJETOS EN LOS PULSOS LA FECHA DE CREACION ES 2020. LOS PORCENTAJES DE FECHA DE MODIFICACION SON LOS SIGUIENTES :  \n")
    print("\n")
    print("            -    EN EL  "+str(float((((count_alienvault_sh_created_2020_modifiedsameday+count_alienvault_iot_created_2020_modifiedsameday)*100)/(count_alienvault_sh_created_2020+count_alienvault_iot_created_2020))))+" % DE OBJETOS EN LOS PULSOS CREADOS EN 2020, LA ULTIMA MODIFICACIÓN SE PRODUJO ESE MISMO DÍA ")
    print("            -    EN EL  "+str(float((((count_alienvault_sh_created_2020_modifiedsamemonth+count_alienvault_iot_created_2020_modifiedsamemonth)*100)/(count_alienvault_sh_created_2020+count_alienvault_iot_created_2020))))+" % DE OBJETOS EN LOS PULSOS CREADOS EN 2020, LA ULTIMA MODIFICACIÓN SE PRODUJO ESE MISMO MES")
    print("            -    EN EL  "+str(float((((count_alienvault_sh_created_2020_modifiedsameyear+count_alienvault_iot_created_2020_modifiedsameyear)*100)/(count_alienvault_sh_created_2020+count_alienvault_iot_created_2020))))+" % DE OBJETOS EN LOS PULSOS CREADOS EN 2020, LA ULTIMA MODIFICACIÓN SE PRODUJO ESE MISMO AÑO ")
    print("            -    EN EL  "+str(float((((count_alienvault_sh_created_2020_anotheryear+count_alienvault_iot_created_2020_anotheryear)*100)/(count_alienvault_sh_created_2020+count_alienvault_iot_created_2020))))+" % DE OBJETOS EN LOS PULSOS CREADOS EN 2020, LA ULTIMA MODIFICACIÓN SE PRODUJO MÁS TARDE DE UN AÑO ")
    print("\n")
if((count_alienvault_sh_created_2019+count_alienvault_iot_created_2019)>0):
    print("      -    EN EL  "+str(float(((count_alienvault_sh_created_2019+count_alienvault_iot_created_2019)*100)/(count_alienvault_sh_entries+count_alienvault_iot_entries)))+" % DE OBJETOS EN LOS PULSOS LA FECHA DE CREACION ES 2019. LOS PORCENTAJES DE FECHA DE MODIFICACION SON LOS SIGUIENTES :  \n")
    print("\n")
    print("            -    EN EL  "+str(float((((count_alienvault_sh_created_2019_modifiedsameday+count_alienvault_iot_created_2019_modifiedsameday)*100)/(count_alienvault_sh_created_2019+count_alienvault_iot_created_2019))))+" % DE OBJETOS EN LOS PULSOS CREADOS EN 2019, LA ULTIMA MODIFICACIÓN SE PRODUJO ESE MISMO DÍA ")
    print("            -    EN EL  "+str(float((((count_alienvault_sh_created_2019_modifiedsamemonth+count_alienvault_iot_created_2019_modifiedsamemonth)*100)/(count_alienvault_sh_created_2019+count_alienvault_iot_created_2019))))+" % DE OBJETOS EN LOS PULSOS CREADOS EN 2019, LA ULTIMA MODIFICACIÓN SE PRODUJO ESE MISMO MES")
    print("            -    EN EL  "+str(float((((count_alienvault_sh_created_2019_modifiedsameyear+count_alienvault_iot_created_2019_modifiedsameyear)*100)/(count_alienvault_sh_created_2019+count_alienvault_iot_created_2019))))+" % DE OBJETOS EN LOS PULSOS CREADOS EN 2019, LA ULTIMA MODIFICACIÓN SE PRODUJO ESE MISMO AÑO ")
    print("            -    EN EL  "+str(float((((count_alienvault_sh_created_2019_anotheryear+count_alienvault_iot_created_2019_anotheryear)*100)/(count_alienvault_sh_created_2019+count_alienvault_iot_created_2019))))+" % DE OBJETOS EN LOS PULSOS CREADOS EN 2019, LA ULTIMA MODIFICACIÓN SE PRODUJO MÁS TARDE DE UN AÑO ")
    print("\n")
if((count_alienvault_sh_created_2018+count_alienvault_iot_created_2018)>0):
    print("      -    EN EL  "+str(float(((count_alienvault_sh_created_2018+count_alienvault_iot_created_2018)*100)/(count_alienvault_sh_entries+count_alienvault_iot_entries)))+" % DE OBJETOS EN LOS PULSOS LA FECHA DE CREACION ES 2018 O ANTERIOR. LOS PORCENTAJES DE FECHA DE MODIFICACION SON LOS SIGUIENTES :  \n")
    print("\n")
    print("            -    EN EL  "+str(float((((count_alienvault_sh_created_2018_modifiedsameday+count_alienvault_iot_created_2018_modifiedsameday)*100)/(count_alienvault_sh_created_2018+count_alienvault_iot_created_2018))))+" % DE OBJETOS EN LOS PULSOS CREADOS EN 2018 O ANTERIORMENTE, LA ULTIMA MODIFICACIÓN SE PRODUJO ESE MISMO DÍA ")
    print("            -    EN EL  "+str(float((((count_alienvault_sh_created_2018_modifiedsamemonth+count_alienvault_iot_created_2018_modifiedsamemonth)*100)/(count_alienvault_sh_created_2018+count_alienvault_iot_created_2018))))+" % DE OBJETOS EN LOS PULSOS CREADOS EN 2018 O ANTERIORMENTE, LA ULTIMA MODIFICACIÓN SE PRODUJO ESE MISMO MES")
    print("            -    EN EL  "+str(float((((count_alienvault_sh_created_2018_modifiedsameyear+count_alienvault_iot_created_2018_modifiedsameyear)*100)/(count_alienvault_sh_created_2018+count_alienvault_iot_created_2018))))+" % DE OBJETOS EN LOS PULSOS CREADOS EN 2018 O ANTERIORMENTE, LA ULTIMA MODIFICACIÓN SE PRODUJO ESE MISMO AÑO ")
    print("            -    EN EL  "+str(float((((count_alienvault_sh_created_2018_anotheryear+count_alienvault_iot_created_2018_anotheryear)*100)/(count_alienvault_sh_created_2018+count_alienvault_iot_created_2018))))+" % DE OBJETOS EN LOS PULSOS CREADOS EN 2018 O ANTERIORMENTE, LA ULTIMA MODIFICACIÓN SE PRODUJO MÁS TARDE DE UN AÑO ")
    print("\n")





	
	
	
	
	
	
	
	
	
	
	