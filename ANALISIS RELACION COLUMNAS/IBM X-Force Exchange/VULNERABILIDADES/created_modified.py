import pandas as pd
from datetime import datetime,timedelta



#Abro los ficheros con los que voy a tratar




df_vulnibm_iot = pd.read_excel('vulnerabilidades_ibm_iot_2023.xlsx')

#Contador total de entradas
count_vulnibm_iot_entries=0

#Variable que almacena el numero de entradas creadas en un anio especifico
count_vulnibm_iot_created_2023=0
#Variable que almacena la diferencia entre fecha de creacion y modificacion dado un anio de creacion especifico
count_vulnibm_iot_created_2023_modifiedsameday=0
count_vulnibm_iot_created_2023_modifiedsamemonth=0
count_vulnibm_iot_created_2023_modifiedsameyear=0
count_vulnibm_iot_created_2023_anotheryear=0

count_vulnibm_iot_created_2022=0
count_vulnibm_iot_created_2022_modifiedsameday=0
count_vulnibm_iot_created_2022_modifiedsamemonth=0
count_vulnibm_iot_created_2022_modifiedsameyear=0
count_vulnibm_iot_created_2022_anotheryear=0

count_vulnibm_iot_created_2021=0
count_vulnibm_iot_created_2021_modifiedsameday=0
count_vulnibm_iot_created_2021_modifiedsamemonth=0
count_vulnibm_iot_created_2021_modifiedsameyear=0
count_vulnibm_iot_created_2021_anotheryear=0

count_vulnibm_iot_created_2020=0
count_vulnibm_iot_created_2020_modifiedsameday=0
count_vulnibm_iot_created_2020_modifiedsamemonth=0
count_vulnibm_iot_created_2020_modifiedsameyear=0
count_vulnibm_iot_created_2020_anotheryear=0

count_vulnibm_iot_created_2019=0
count_vulnibm_iot_created_2019_modifiedsameday=0
count_vulnibm_iot_created_2019_modifiedsamemonth=0
count_vulnibm_iot_created_2019_modifiedsameyear=0
count_vulnibm_iot_created_2019_anotheryear=0

count_vulnibm_iot_created_2018=0
count_vulnibm_iot_created_2018_modifiedsameday=0
count_vulnibm_iot_created_2018_modifiedsamemonth=0
count_vulnibm_iot_created_2018_modifiedsameyear=0
count_vulnibm_iot_created_2018_anotheryear=0


#Comprobamos el anio de creacion
for r in range(0,len(df_vulnibm_iot["created"])):
    #Si existen varios valores de fecha de creacion para la fila actual
    if('[' in df_vulnibm_iot["created"][r]):
        #Obtenemos los valores de creacion y modificacion para la fila actual
        aux=df_vulnibm_iot["created"][r].split(",")
        auxx=df_vulnibm_iot["modified"][r].split(",")
        #Recorremos los distintos valores de fecha de creacion
        for l in range(0,len(aux)):
            if(len(aux)>0):
                #Obtenemos el valor actual de fecha de creacion y modificacion
                aux_str=aux[l].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","").replace("T"," ")
                auxx_str=auxx[l].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","").replace("T"," ")
                #En caso de que existan la fecha de creacion y modificacion
                if(aux_str!='NONE' and auxx_str!='NONE'):
                    #Obtenemos la fecha de creacion y lo transformamos a formato de tiempo
                    aux2=aux_str.split(".")
                    creado = datetime.strptime(aux2[0], '%Y-%m-%d %H:%M:%S')
                    #Obtenemos la fecha de modificacion y lo transformamos a formato de tiempo
                    aux22=auxx_str.split(".")
                    modificado = datetime.strptime(aux22[0], '%Y-%m-%d %H:%M:%S')
                    #Diferencia entre fecha de modificacion y creacion
                    res=creado-modificado
                    #Obtenemos fecha de creacion
                    str_anio_createdate_vulnibm_iot=aux_str.split("-")
                    anio_createdate_vulnibm_iot=int(str_anio_createdate_vulnibm_iot[0])
                    #Comprobamos anio de creacion
                    if(anio_createdate_vulnibm_iot >= 2023):
                        count_vulnibm_iot_entries+=1
                        count_vulnibm_iot_created_2023+=1
                        #Comprobamos si la diferencia entre fecha de creacion y modificacion es menor de un dia
                        if(((res/ timedelta(days=1))*(-1)) < 1):
                            count_vulnibm_iot_created_2023_modifiedsameday+=1
                        #Comprobamos si la diferencia entre fecha de creacion y modificacion es menor de un mes    
                        elif(((res/ timedelta(days=30))*(-1)) < 1):
                            count_vulnibm_iot_created_2023_modifiedsamemonth+=1
                        #Comprobamos si la diferencia entre fecha de creacion y modificacion es menor de un anio    
                        elif(((res/ timedelta(days=365))*(-1)) < 1):
                            count_vulnibm_iot_created_2023_modifiedsameyear+=1
                        #Comprobamos si la diferencia entre fecha de creacion y modificacion es mayor de un dia   
                        else:
                            count_vulnibm_iot_created_2023_anotheryear+=1
                            
                    elif(anio_createdate_vulnibm_iot >= 2022):
                        count_vulnibm_iot_entries+=1
                        count_vulnibm_iot_created_2022+=1
                        if(((res/ timedelta(days=1))*(-1)) < 1):
                            count_vulnibm_iot_created_2022_modifiedsameday+=1
                            
                        elif(((res/ timedelta(days=30))*(-1)) < 1):
                            count_vulnibm_iot_created_2022_modifiedsamemonth+=1
                            
                        elif(((res/ timedelta(days=365))*(-1)) < 1):
                            count_vulnibm_iot_created_2022_modifiedsameyear+=1
                            
                        else:
                            count_vulnibm_iot_created_2022_anotheryear+=1
                            
                    elif(anio_createdate_vulnibm_iot >= 2021):
                        count_vulnibm_iot_entries+=1
                        count_vulnibm_iot_created_2021+=1
                        if(((res/ timedelta(days=1))*(-1)) < 1):
                            count_vulnibm_iot_created_2021_modifiedsameday+=1
                            
                        elif(((res/ timedelta(days=30))*(-1)) < 1):
                            count_vulnibm_iot_created_2021_modifiedsamemonth+=1
                            
                        elif(((res/ timedelta(days=365))*(-1)) < 1):
                            count_vulnibm_iot_created_2021_modifiedsameyear+=1
                            
                        else:
                            count_vulnibm_iot_created_2021_anotheryear+=1
                            
                    elif(anio_createdate_vulnibm_iot >= 2020):
                        count_vulnibm_iot_entries+=1
                        count_vulnibm_iot_created_2020+=1
                        if(((res/ timedelta(days=1))*(-1)) < 1):
                            count_vulnibm_iot_created_2020_modifiedsameday+=1
                            
                        elif(((res/ timedelta(days=30))*(-1)) < 1):
                            count_vulnibm_iot_created_2020_modifiedsamemonth+=1
                            
                        elif(((res/ timedelta(days=365))*(-1)) < 1):
                            count_vulnibm_iot_created_2020_modifiedsameyear+=1
                            
                        else:
                            count_vulnibm_iot_created_2020_anotheryear+=1
                            
                    elif(anio_createdate_vulnibm_iot >= 2019):
                        count_vulnibm_iot_entries+=1
                        count_vulnibm_iot_created_2019+=1
                        if(((res/ timedelta(days=1))*(-1)) < 1):
                            count_vulnibm_iot_created_2019_modifiedsameday+=1
                            
                        elif(((res/ timedelta(days=30))*(-1)) < 1):
                            count_vulnibm_iot_created_2019_modifiedsamemonth+=1
                            
                        elif(((res/ timedelta(days=365))*(-1)) < 1):
                            count_vulnibm_iot_created_2019_modifiedsameyear+=1
                            
                        else:
                            count_vulnibm_iot_created_2019_anotheryear+=1
                            
                    elif(anio_createdate_vulnibm_iot >= 2018):
                        count_vulnibm_iot_entries+=1
                        count_vulnibm_iot_created_2018+=1
                        if(((res/ timedelta(days=1))*(-1)) < 1):
                            count_vulnibm_iot_created_2018_modifiedsameday+=1
                            
                        elif(((res/ timedelta(days=30))*(-1)) < 1):
                            count_vulnibm_iot_created_2018_modifiedsamemonth+=1
                            
                        elif(((res/ timedelta(days=365))*(-1)) < 1):
                            count_vulnibm_iot_created_2018_modifiedsameyear+=1
                            
                        else:
                            count_vulnibm_iot_created_2018_anotheryear+=1
                            
    else:
        #Si existe un unico valor de creacion y modificacion para la fila actual
        aux_strr=df_vulnibm_iot["created"][r].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","").replace("T"," ")
        auxx_strr=df_vulnibm_iot["modified"][r].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","").replace("T"," ")
        if(aux_strr!='NONE' and auxx_strr!='NONE'):
            aux22=aux_strr.split(".")
            creado = datetime.strptime(aux22[0], '%Y-%m-%d %H:%M:%S')
            aux222=auxx_strr.split(".")
            modificado = datetime.strptime(aux222[0], '%Y-%m-%d %H:%M:%S')
            res=creado-modificado
            str_anio_createdate_vulnibm_iot=auxx_strr.split("-")
            anio_createdate_vulnibm_iot=int(str_anio_createdate_vulnibm_iot[0])                    
            if(anio_createdate_vulnibm_iot >= 2023):
                count_vulnibm_iot_entries+=1
                count_vulnibm_iot_created_2023+=1
                if(((res/ timedelta(days=1))*(-1)) < 1):
                    count_vulnibm_iot_created_2023_modifiedsameday+=1

                elif(((res/ timedelta(days=30))*(-1)) < 1):
                    count_vulnibm_iot_created_2023_modifiedsamemonth+=1

                elif(((res/ timedelta(days=365))*(-1)) < 1):
                    count_vulnibm_iot_created_2023_modifiedsameyear+=1

                else:
                    count_vulnibm_iot_created_2023_anotheryear+=1

            elif(anio_createdate_vulnibm_iot >= 2022):
                count_vulnibm_iot_entries+=1
                count_vulnibm_iot_created_2022+=1
                if(((res/ timedelta(days=1))*(-1)) < 1):
                    count_vulnibm_iot_created_2022_modifiedsameday+=1

                elif(((res/ timedelta(days=30))*(-1)) < 1):
                    count_vulnibm_iot_created_2022_modifiedsamemonth+=1

                elif(((res/ timedelta(days=365))*(-1)) < 1):
                    count_vulnibm_iot_created_2022_modifiedsameyear+=1

                else:
                    count_vulnibm_iot_created_2022_anotheryear+=1

            elif(anio_createdate_vulnibm_iot >= 2021):
                count_vulnibm_iot_entries+=1
                count_vulnibm_iot_created_2021+=1
                if(((res/ timedelta(days=1))*(-1)) < 1):
                    count_vulnibm_iot_created_2021_modifiedsameday+=1

                elif(((res/ timedelta(days=30))*(-1)) < 1):
                    count_vulnibm_iot_created_2021_modifiedsamemonth+=1

                elif(((res/ timedelta(days=365))*(-1)) < 1):
                    count_vulnibm_iot_created_2021_modifiedsameyear+=1

                else:
                    count_vulnibm_iot_created_2021_anotheryear+=1

            elif(anio_createdate_vulnibm_iot >= 2020):
                count_vulnibm_iot_entries+=1
                count_vulnibm_iot_created_2020+=1
                if(((res/ timedelta(days=1))*(-1)) < 1):
                    count_vulnibm_iot_created_2020_modifiedsameday+=1

                elif(((res/ timedelta(days=30))*(-1)) < 1):
                    count_vulnibm_iot_created_2020_modifiedsamemonth+=1

                elif(((res/ timedelta(days=365))*(-1)) < 1):
                    count_vulnibm_iot_created_2020_modifiedsameyear+=1

                else:
                    count_vulnibm_iot_created_2020_anotheryear+=1

            elif(anio_createdate_vulnibm_iot >= 2019):
                count_vulnibm_iot_entries+=1
                count_vulnibm_iot_created_2019+=1
                if(((res/ timedelta(days=1))*(-1)) < 1):
                    count_vulnibm_iot_created_2019_modifiedsameday+=1

                elif(((res/ timedelta(days=30))*(-1)) < 1):
                    count_vulnibm_iot_created_2019_modifiedsamemonth+=1

                elif(((res/ timedelta(days=365))*(-1)) < 1):
                    count_vulnibm_iot_created_2019_modifiedsameyear+=1

                else:
                    count_vulnibm_iot_created_2019_anotheryear+=1

            elif(anio_createdate_vulnibm_iot >= 2018):
                count_vulnibm_iot_entries+=1
                count_vulnibm_iot_created_2018+=1
                if(((res/ timedelta(days=1))*(-1)) < 1):
                    count_vulnibm_iot_created_2018_modifiedsameday+=1

                elif(((res/ timedelta(days=30))*(-1)) < 1):
                    count_vulnibm_iot_created_2018_modifiedsamemonth+=1

                elif(((res/ timedelta(days=365))*(-1)) < 1):
                    count_vulnibm_iot_created_2018_modifiedsameyear+=1

                else:
                    count_vulnibm_iot_created_2018_anotheryear+=1        
                            
                    
print("********************ESTADÍSTICAS FECHA DE CREACIÓN/FECHA DE MODIFICACION VULNERABILIDADES IBM PARTE IOT********************")
print("\n")                            
                
print("\n")
print(" DE UN TOTAL DE "+str(count_vulnibm_iot_entries)+" VULNERABILIDADES :\n") 
print("\n")
print("   - LAS ESTADISTICAS DE FECHA DE CREACION SON LAS SIGUIENTES:  \n")
print("      -    EN  "+str(count_vulnibm_iot_created_2023)+" VULNERABILIDADES LA FECHA DE CREACION ES 2023. LAS ESTADÍSTICAS DE FECHA DE MODIFICACION SON LAS SIGUIENTES :  \n")
print("\n")
print("            -    EN  "+str(count_vulnibm_iot_created_2023_modifiedsameday)+" VULNERABILIDADES CREADAS EN 2023, LA ULTIMA MODIFICACIÓN SE PRODUJO ESE MISMO DÍA ")
print("            -    EN  "+str(count_vulnibm_iot_created_2023_modifiedsamemonth)+" VULNERABILIDADES CREADAS EN 2023, LA ÚLTIMA MODIFICACIÓN SE PRODUJO ESE MISMO MES")
print("            -    EN  "+str(count_vulnibm_iot_created_2023_modifiedsameyear)+" VULNERABILIDADES CREADAS EN 2023, LA ÚLTIMA MODIFICACIÓN SE PRODUJO ESE MISMO AÑO ")
print("            -    EN  "+str(count_vulnibm_iot_created_2023_anotheryear)+" VULNERABILIDADES CREADAS EN 2023, LA ÚLTIMA MODIFICACIÓN SE PRODUJO MÁS TARDE DE UN AÑO ")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_created_2022)+" VULNERABILIDADES LA FECHA DE CREACION ES 2022. LAS ESTADÍSTICAS DE FECHA DE MODIFICACION SON LAS SIGUIENTES :  \n")
print("\n")
print("            -    EN  "+str(count_vulnibm_iot_created_2022_modifiedsameday)+" VULNERABILIDADES CREADAS EN 2022, LA ULTIMA MODIFICACIÓN SE PRODUJO ESE MISMO DÍA ")
print("            -    EN  "+str(count_vulnibm_iot_created_2022_modifiedsamemonth)+" VULNERABILIDADES CREADAS EN 2022, LA ÚLTIMA MODIFICACIÓN SE PRODUJO ESE MISMO MES")
print("            -    EN  "+str(count_vulnibm_iot_created_2022_modifiedsameyear)+" VULNERABILIDADES CREADAS EN 2022, LA ÚLTIMA MODIFICACIÓN SE PRODUJO ESE MISMO AÑO ")
print("            -    EN  "+str(count_vulnibm_iot_created_2022_anotheryear)+" VULNERABILIDADES CREADAS EN 2022, LA ÚLTIMA MODIFICACIÓN SE PRODUJO MÁS TARDE DE UN AÑO ")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_created_2021)+" VULNERABILIDADES LA FECHA DE CREACION ES 2021. LAS ESTADÍSTICAS DE FECHA DE MODIFICACION SON LAS SIGUIENTES :  \n")
print("\n")
print("            -    EN  "+str(count_vulnibm_iot_created_2021_modifiedsameday)+" VULNERABILIDADES CREADAS EN 2021, LA ULTIMA MODIFICACIÓN SE PRODUJO ESE MISMO DÍA ")
print("            -    EN  "+str(count_vulnibm_iot_created_2021_modifiedsamemonth)+" VULNERABILIDADES CREADAS EN 2021, LA ÚLTIMA MODIFICACIÓN SE PRODUJO ESE MISMO MES")
print("            -    EN  "+str(count_vulnibm_iot_created_2021_modifiedsameyear)+" VULNERABILIDADES CREADAS EN 2021, LA ÚLTIMA MODIFICACIÓN SE PRODUJO ESE MISMO AÑO ")
print("            -    EN  "+str(count_vulnibm_iot_created_2021_anotheryear)+" VULNERABILIDADES CREADAS EN 2021, LA ÚLTIMA MODIFICACIÓN SE PRODUJO MÁS TARDE DE UN AÑO ")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_created_2020)+" VULNERABILIDADES LA FECHA DE CREACION ES 2020. LAS ESTADÍSTICAS DE FECHA DE MODIFICACION SON LAS SIGUIENTES :  \n")
print("\n")
print("            -    EN  "+str(count_vulnibm_iot_created_2020_modifiedsameday)+" VULNERABILIDADES CREADAS EN 2020, LA ULTIMA MODIFICACIÓN SE PRODUJO ESE MISMO DÍA ")
print("            -    EN  "+str(count_vulnibm_iot_created_2020_modifiedsamemonth)+" VULNERABILIDADES CREADAS EN 2020, LA ÚLTIMA MODIFICACIÓN SE PRODUJO ESE MISMO MES")
print("            -    EN  "+str(count_vulnibm_iot_created_2020_modifiedsameyear)+" VULNERABILIDADES CREADAS EN 2020, LA ÚLTIMA MODIFICACIÓN SE PRODUJO ESE MISMO AÑO ")
print("            -    EN  "+str(count_vulnibm_iot_created_2020_anotheryear)+" VULNERABILIDADES CREADAS EN 2020, LA ÚLTIMA MODIFICACIÓN SE PRODUJO MÁS TARDE DE UN AÑO ")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_created_2019)+" VULNERABILIDADES LA FECHA DE CREACION ES 2019. LAS ESTADÍSTICAS DE FECHA DE MODIFICACION SON LAS SIGUIENTES :  \n")
print("\n")
print("            -    EN  "+str(count_vulnibm_iot_created_2019_modifiedsameday)+" VULNERABILIDADES CREADAS EN 2019, LA ULTIMA MODIFICACIÓN SE PRODUJO ESE MISMO DÍA ")
print("            -    EN  "+str(count_vulnibm_iot_created_2019_modifiedsamemonth)+" VULNERABILIDADES CREADAS EN 2019, LA ÚLTIMA MODIFICACIÓN SE PRODUJO ESE MISMO MES")
print("            -    EN  "+str(count_vulnibm_iot_created_2019_modifiedsameyear)+" VULNERABILIDADES CREADAS EN 2019, LA ÚLTIMA MODIFICACIÓN SE PRODUJO ESE MISMO AÑO ")
print("            -    EN  "+str(count_vulnibm_iot_created_2019_anotheryear)+" VULNERABILIDADES CREADAS EN 2019, LA ÚLTIMA MODIFICACIÓN SE PRODUJO MÁS TARDE DE UN AÑO ")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_created_2018)+" VULNERABILIDADES LA FECHA DE CREACION ES 2018 O ANTERIOR. LAS ESTADÍSTICAS DE FECHA DE MODIFICACION SON LAS SIGUIENTES :  \n")
print("\n")
print("            -    EN  "+str(count_vulnibm_iot_created_2018_modifiedsameday)+" VULNERABILIDADES CREADAS EN 2018 O ANTERIORMENTE, LA ULTIMA MODIFICACIÓN SE PRODUJO ESE MISMO DÍA ")
print("            -    EN  "+str(count_vulnibm_iot_created_2018_modifiedsamemonth)+" VULNERABILIDADES CREADAS EN 2018 O ANTERIORMENTE, LA ÚLTIMA MODIFICACIÓN SE PRODUJO ESE MISMO MES")
print("            -    EN  "+str(count_vulnibm_iot_created_2018_modifiedsameyear)+" VULNERABILIDADES CREADAS EN 2018 O ANTERIORMENTE, LA ÚLTIMA MODIFICACIÓN SE PRODUJO ESE MISMO AÑO ")
print("            -    EN  "+str(count_vulnibm_iot_created_2018_anotheryear)+" VULNERABILIDADES CREADAS EN 2018 O ANTERIORMENTE, LA ÚLTIMA MODIFICACIÓN SE PRODUJO MÁS TARDE DE UN AÑO ")
print("\n")








print("********************PORCENTAJE FECHA DE CREACIÓN/FECHA DE MODIFICACION VULNERABILIDADES IBM PARTE IOT********************")
print("\n")                            
                
print("\n")
print(" DE UN TOTAL DE "+str(count_vulnibm_iot_entries)+" VULNERABILIDADES :\n") 
print("\n")
print("   - LOS PORCENTAJES DE FECHA DE CREACION SON LOS SIGUIENTES:  \n")
if(count_vulnibm_iot_created_2023>0):
    print("      -    EN EL  "+str(float(((count_vulnibm_iot_created_2023*100)/count_vulnibm_iot_entries)))+" % DE VULNERABILIDADES LA FECHA DE CREACION ES 2023. LOS PORCENTAJES DE FECHA DE MODIFICACION SON LOS SIGUIENTES  \n")
    print("\n")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_created_2023_modifiedsameday*100)/count_vulnibm_iot_created_2023)))+" % DE VULNERABILIDADES CREADAS EN 2023, LA ULTIMA MODIFICACIÓN SE PRODUJO ESE MISMO DÍA ")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_created_2023_modifiedsamemonth*100)/count_vulnibm_iot_created_2023)))+" % DE VULNERABILIDADES CREADAS EN 2023, LA ULTIMA MODIFICACIÓN SE PRODUJO ESE MISMO MES")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_created_2023_modifiedsameyear*100)/count_vulnibm_iot_created_2023)))+" % DE VULNERABILIDADES CREADAS EN 2023, LA ULTIMA MODIFICACIÓN SE PRODUJO ESE MISMO AÑO ")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_created_2023_anotheryear*100)/count_vulnibm_iot_created_2023)))+" % DE VULNERABILIDADES CREADAS EN 2023, LA ULTIMA MODIFICACIÓN SE PRODUJO MÁS TARDE DE UN AÑO ")
    print("\n")
if(count_vulnibm_iot_created_2022>0):
    print("      -    EN EL  "+str(float(((count_vulnibm_iot_created_2022*100)/count_vulnibm_iot_entries)))+" % DE VULNERABILIDADES LA FECHA DE CREACION ES 2022. LOS PORCENTAJES DE FECHA DE MODIFICACION SON LOS SIGUIENTES  \n")
    print("\n")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_created_2022_modifiedsameday*100)/count_vulnibm_iot_created_2022)))+" % DE VULNERABILIDADES CREADAS EN 2022, LA ULTIMA MODIFICACIÓN SE PRODUJO ESE MISMO DÍA ")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_created_2022_modifiedsamemonth*100)/count_vulnibm_iot_created_2022)))+" % DE VULNERABILIDADES CREADAS EN 2022, LA ULTIMA MODIFICACIÓN SE PRODUJO ESE MISMO MES")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_created_2022_modifiedsameyear*100)/count_vulnibm_iot_created_2022)))+" % DE VULNERABILIDADES CREADAS EN 2022, LA ULTIMA MODIFICACIÓN SE PRODUJO ESE MISMO AÑO ")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_created_2022_anotheryear*100)/count_vulnibm_iot_created_2022)))+" % DE VULNERABILIDADES CREADAS EN 2022, LA ULTIMA MODIFICACIÓN SE PRODUJO MÁS TARDE DE UN AÑO ")
    print("\n")
if(count_vulnibm_iot_created_2021>0):
    print("      -    EN EL  "+str(float(((count_vulnibm_iot_created_2021*100)/count_vulnibm_iot_entries)))+" % DE VULNERABILIDADES LA FECHA DE CREACION ES 2021. LOS PORCENTAJES DE FECHA DE MODIFICACION SON LOS SIGUIENTES  \n")
    print("\n")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_created_2021_modifiedsameday*100)/count_vulnibm_iot_created_2021)))+" % DE VULNERABILIDADES CREADAS EN 2021, LA ULTIMA MODIFICACIÓN SE PRODUJO ESE MISMO DÍA ")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_created_2021_modifiedsamemonth*100)/count_vulnibm_iot_created_2021)))+" % DE VULNERABILIDADES CREADAS EN 2021, LA ULTIMA MODIFICACIÓN SE PRODUJO ESE MISMO MES")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_created_2021_modifiedsameyear*100)/count_vulnibm_iot_created_2021)))+" % DE VULNERABILIDADES CREADAS EN 2021, LA ULTIMA MODIFICACIÓN SE PRODUJO ESE MISMO AÑO ")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_created_2021_anotheryear*100)/count_vulnibm_iot_created_2021)))+" % DE VULNERABILIDADES CREADAS EN 2021, LA ULTIMA MODIFICACIÓN SE PRODUJO MÁS TARDE DE UN AÑO ")
    print("\n")
if(count_vulnibm_iot_created_2020>0):
    print("      -    EN EL  "+str(float(((count_vulnibm_iot_created_2020*100)/count_vulnibm_iot_entries)))+" % DE VULNERABILIDADES LA FECHA DE CREACION ES 2020. LOS PORCENTAJES DE FECHA DE MODIFICACION SON LOS SIGUIENTES  \n")
    print("\n")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_created_2020_modifiedsameday*100)/count_vulnibm_iot_created_2020)))+" % DE VULNERABILIDADES CREADAS EN 2020, LA ULTIMA MODIFICACIÓN SE PRODUJO ESE MISMO DÍA ")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_created_2020_modifiedsamemonth*100)/count_vulnibm_iot_created_2020)))+" % DE VULNERABILIDADES CREADAS EN 2020, LA ULTIMA MODIFICACIÓN SE PRODUJO ESE MISMO MES")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_created_2020_modifiedsameyear*100)/count_vulnibm_iot_created_2020)))+" % DE VULNERABILIDADES CREADAS EN 2020, LA ULTIMA MODIFICACIÓN SE PRODUJO ESE MISMO AÑO ")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_created_2020_anotheryear*100)/count_vulnibm_iot_created_2020)))+" % DE VULNERABILIDADES CREADAS EN 2020, LA ULTIMA MODIFICACIÓN SE PRODUJO MÁS TARDE DE UN AÑO ")
    print("\n")
if(count_vulnibm_iot_created_2019>0):
    print("      -    EN EL  "+str(float(((count_vulnibm_iot_created_2019*100)/count_vulnibm_iot_entries)))+" % DE VULNERABILIDADES LA FECHA DE CREACION ES 2019. LOS PORCENTAJES DE FECHA DE MODIFICACION SON LOS SIGUIENTES  \n")
    print("\n")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_created_2019_modifiedsameday*100)/count_vulnibm_iot_created_2019)))+" % DE VULNERABILIDADES CREADAS EN 2019, LA ULTIMA MODIFICACIÓN SE PRODUJO ESE MISMO DÍA ")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_created_2019_modifiedsamemonth*100)/count_vulnibm_iot_created_2019)))+" % DE VULNERABILIDADES CREADAS EN 2019, LA ULTIMA MODIFICACIÓN SE PRODUJO ESE MISMO MES")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_created_2019_modifiedsameyear*100)/count_vulnibm_iot_created_2019)))+" % DE VULNERABILIDADES CREADAS EN 2019, LA ULTIMA MODIFICACIÓN SE PRODUJO ESE MISMO AÑO ")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_created_2019_anotheryear*100)/count_vulnibm_iot_created_2019)))+" % DE VULNERABILIDADES CREADAS EN 2019, LA ULTIMA MODIFICACIÓN SE PRODUJO MÁS TARDE DE UN AÑO ")
    print("\n")
if(count_vulnibm_iot_created_2018>0):
    print("      -    EN EL  "+str(float(((count_vulnibm_iot_created_2018*100)/count_vulnibm_iot_entries)))+" % DE VULNERABILIDADES LA FECHA DE CREACION ES 2018 O ANTERIOR. LOS PORCENTAJES DE FECHA DE MODIFICACION SON LOS SIGUIENTES  \n")
    print("\n")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_created_2018_modifiedsameday*100)/count_vulnibm_iot_created_2018)))+" % DE VULNERABILIDADES CREADAS EN 2018 O ANTERIORMENTE, LA ULTIMA MODIFICACIÓN SE PRODUJO ESE MISMO DÍA ")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_created_2018_modifiedsamemonth*100)/count_vulnibm_iot_created_2018)))+" % DE VULNERABILIDADES CREADAS EN 2018 O ANTERIORMENTE, LA ULTIMA MODIFICACIÓN SE PRODUJO ESE MISMO MES")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_created_2018_modifiedsameyear*100)/count_vulnibm_iot_created_2018)))+" % DE VULNERABILIDADES CREADAS EN 2018 O ANTERIORMENTE, LA ULTIMA MODIFICACIÓN SE PRODUJO ESE MISMO AÑO ")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_created_2018_anotheryear*100)/count_vulnibm_iot_created_2018)))+" % DE VULNERABILIDADES CREADAS EN 2018 O ANTERIORMENTE, LA ULTIMA MODIFICACIÓN SE PRODUJO MÁS TARDE DE UN AÑO ")
    print("\n")





    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
import pandas as pd
from datetime import datetime,timedelta



#Abro los ficheros con los que voy a tratar




df_vulnibm_sh = pd.read_excel('vulnerabilidades_ibm_smart_home_2023.xlsx')

#Contador total de entradas
count_vulnibm_sh_entries=0

#Variable que almacena el numero de entradas creadas en un anio especifico
count_vulnibm_sh_created_2023=0
#Variable que almacena la diferencia entre fecha de creacion y modificacion dado un anio de creacion especifico
count_vulnibm_sh_created_2023_modifiedsameday=0
count_vulnibm_sh_created_2023_modifiedsamemonth=0
count_vulnibm_sh_created_2023_modifiedsameyear=0
count_vulnibm_sh_created_2023_anotheryear=0

count_vulnibm_sh_created_2022=0
count_vulnibm_sh_created_2022_modifiedsameday=0
count_vulnibm_sh_created_2022_modifiedsamemonth=0
count_vulnibm_sh_created_2022_modifiedsameyear=0
count_vulnibm_sh_created_2022_anotheryear=0

count_vulnibm_sh_created_2021=0
count_vulnibm_sh_created_2021_modifiedsameday=0
count_vulnibm_sh_created_2021_modifiedsamemonth=0
count_vulnibm_sh_created_2021_modifiedsameyear=0
count_vulnibm_sh_created_2021_anotheryear=0

count_vulnibm_sh_created_2020=0
count_vulnibm_sh_created_2020_modifiedsameday=0
count_vulnibm_sh_created_2020_modifiedsamemonth=0
count_vulnibm_sh_created_2020_modifiedsameyear=0
count_vulnibm_sh_created_2020_anotheryear=0

count_vulnibm_sh_created_2019=0
count_vulnibm_sh_created_2019_modifiedsameday=0
count_vulnibm_sh_created_2019_modifiedsamemonth=0
count_vulnibm_sh_created_2019_modifiedsameyear=0
count_vulnibm_sh_created_2019_anotheryear=0

count_vulnibm_sh_created_2018=0
count_vulnibm_sh_created_2018_modifiedsameday=0
count_vulnibm_sh_created_2018_modifiedsamemonth=0
count_vulnibm_sh_created_2018_modifiedsameyear=0
count_vulnibm_sh_created_2018_anotheryear=0


#Comprobamos el anio de creacion
for r in range(0,len(df_vulnibm_sh["created"])):
    #Si existen varios valores de fecha de creacion para la fila actual
    if('[' in df_vulnibm_sh["created"][r]):
        #Obtenemos los valores de creacion y modificacion para la fila actual
        aux=df_vulnibm_sh["created"][r].split(",")
        auxx=df_vulnibm_sh["modified"][r].split(",")
        #Recorremos los distintos valores de fecha de creacion
        for l in range(0,len(aux)):
            if(len(aux)>0):
                #Obtenemos el valor actual de fecha de creacion y modificacion
                aux_str=aux[l].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","").replace("T"," ")
                auxx_str=auxx[l].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","").replace("T"," ")
                #En caso de que existan la fecha de creacion y modificacion
                if(aux_str!='NONE' and auxx_str!='NONE'):
                    #Obtenemos la fecha de creacion y lo transformamos a formato de tiempo
                    aux2=aux_str.split(".")
                    creado = datetime.strptime(aux2[0], '%Y-%m-%d %H:%M:%S')
                    #Obtenemos la fecha de modificacion y lo transformamos a formato de tiempo
                    aux22=auxx_str.split(".")
                    modificado = datetime.strptime(aux22[0], '%Y-%m-%d %H:%M:%S')
                    #Diferencia entre fecha de modificacion y creacion
                    res=creado-modificado
                    #Obtenemos fecha de creacion
                    str_anio_createdate_vulnibm_sh=aux_str.split("-")
                    anio_createdate_vulnibm_sh=int(str_anio_createdate_vulnibm_sh[0])
                    #Comprobamos anio de creacion
                    if(anio_createdate_vulnibm_sh >= 2023):
                        count_vulnibm_sh_entries+=1
                        count_vulnibm_sh_created_2023+=1
                        #Comprobamos si la diferencia entre fecha de creacion y modificacion es menor de un dia
                        if(((res/ timedelta(days=1))*(-1)) < 1):
                            count_vulnibm_sh_created_2023_modifiedsameday+=1
                        #Comprobamos si la diferencia entre fecha de creacion y modificacion es menor de un mes    
                        elif(((res/ timedelta(days=30))*(-1)) < 1):
                            count_vulnibm_sh_created_2023_modifiedsamemonth+=1
                        #Comprobamos si la diferencia entre fecha de creacion y modificacion es menor de un anio    
                        elif(((res/ timedelta(days=365))*(-1)) < 1):
                            count_vulnibm_sh_created_2023_modifiedsameyear+=1
                        #Comprobamos si la diferencia entre fecha de creacion y modificacion es mayor de un dia   
                        else:
                            count_vulnibm_sh_created_2023_anotheryear+=1
                            
                    elif(anio_createdate_vulnibm_sh >= 2022):
                        count_vulnibm_sh_entries+=1
                        count_vulnibm_sh_created_2022+=1
                        if(((res/ timedelta(days=1))*(-1)) < 1):
                            count_vulnibm_sh_created_2022_modifiedsameday+=1
                            
                        elif(((res/ timedelta(days=30))*(-1)) < 1):
                            count_vulnibm_sh_created_2022_modifiedsamemonth+=1
                            
                        elif(((res/ timedelta(days=365))*(-1)) < 1):
                            count_vulnibm_sh_created_2022_modifiedsameyear+=1
                            
                        else:
                            count_vulnibm_sh_created_2022_anotheryear+=1
                            
                    elif(anio_createdate_vulnibm_sh >= 2021):
                        count_vulnibm_sh_entries+=1
                        count_vulnibm_sh_created_2021+=1
                        if(((res/ timedelta(days=1))*(-1)) < 1):
                            count_vulnibm_sh_created_2021_modifiedsameday+=1
                            
                        elif(((res/ timedelta(days=30))*(-1)) < 1):
                            count_vulnibm_sh_created_2021_modifiedsamemonth+=1
                            
                        elif(((res/ timedelta(days=365))*(-1)) < 1):
                            count_vulnibm_sh_created_2021_modifiedsameyear+=1
                            
                        else:
                            count_vulnibm_sh_created_2021_anotheryear+=1
                            
                    elif(anio_createdate_vulnibm_sh >= 2020):
                        count_vulnibm_sh_entries+=1
                        count_vulnibm_sh_created_2020+=1
                        if(((res/ timedelta(days=1))*(-1)) < 1):
                            count_vulnibm_sh_created_2020_modifiedsameday+=1
                            
                        elif(((res/ timedelta(days=30))*(-1)) < 1):
                            count_vulnibm_sh_created_2020_modifiedsamemonth+=1
                            
                        elif(((res/ timedelta(days=365))*(-1)) < 1):
                            count_vulnibm_sh_created_2020_modifiedsameyear+=1
                            
                        else:
                            count_vulnibm_sh_created_2020_anotheryear+=1
                            
                    elif(anio_createdate_vulnibm_sh >= 2019):
                        count_vulnibm_sh_entries+=1
                        count_vulnibm_sh_created_2019+=1
                        if(((res/ timedelta(days=1))*(-1)) < 1):
                            count_vulnibm_sh_created_2019_modifiedsameday+=1
                            
                        elif(((res/ timedelta(days=30))*(-1)) < 1):
                            count_vulnibm_sh_created_2019_modifiedsamemonth+=1
                            
                        elif(((res/ timedelta(days=365))*(-1)) < 1):
                            count_vulnibm_sh_created_2019_modifiedsameyear+=1
                            
                        else:
                            count_vulnibm_sh_created_2019_anotheryear+=1
                            
                    elif(anio_createdate_vulnibm_sh >= 2018):
                        count_vulnibm_sh_entries+=1
                        count_vulnibm_sh_created_2018+=1
                        if(((res/ timedelta(days=1))*(-1)) < 1):
                            count_vulnibm_sh_created_2018_modifiedsameday+=1
                            
                        elif(((res/ timedelta(days=30))*(-1)) < 1):
                            count_vulnibm_sh_created_2018_modifiedsamemonth+=1
                            
                        elif(((res/ timedelta(days=365))*(-1)) < 1):
                            count_vulnibm_sh_created_2018_modifiedsameyear+=1
                            
                        else:
                            count_vulnibm_sh_created_2018_anotheryear+=1
                            
    else:
        #Si existe un unico valor de creacion y modificacion para la fila actual
        aux_strr=df_vulnibm_sh["created"][r].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","").replace("T"," ")
        auxx_strr=df_vulnibm_sh["modified"][r].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","").replace("T"," ")
        if(aux_strr!='NONE' and auxx_strr!='NONE'):
            aux22=aux_strr.split(".")
            creado = datetime.strptime(aux22[0], '%Y-%m-%d %H:%M:%S')
            aux222=auxx_strr.split(".")
            modificado = datetime.strptime(aux222[0], '%Y-%m-%d %H:%M:%S')
            res=creado-modificado
            str_anio_createdate_vulnibm_sh=auxx_strr.split("-")
            anio_createdate_vulnibm_sh=int(str_anio_createdate_vulnibm_sh[0])                    
            if(anio_createdate_vulnibm_sh >= 2023):
                count_vulnibm_sh_entries+=1
                count_vulnibm_sh_created_2023+=1
                if(((res/ timedelta(days=1))*(-1)) < 1):
                    count_vulnibm_sh_created_2023_modifiedsameday+=1

                elif(((res/ timedelta(days=30))*(-1)) < 1):
                    count_vulnibm_sh_created_2023_modifiedsamemonth+=1

                elif(((res/ timedelta(days=365))*(-1)) < 1):
                    count_vulnibm_sh_created_2023_modifiedsameyear+=1

                else:
                    count_vulnibm_sh_created_2023_anotheryear+=1

            elif(anio_createdate_vulnibm_sh >= 2022):
                count_vulnibm_sh_entries+=1
                count_vulnibm_sh_created_2022+=1
                if(((res/ timedelta(days=1))*(-1)) < 1):
                    count_vulnibm_sh_created_2022_modifiedsameday+=1

                elif(((res/ timedelta(days=30))*(-1)) < 1):
                    count_vulnibm_sh_created_2022_modifiedsamemonth+=1

                elif(((res/ timedelta(days=365))*(-1)) < 1):
                    count_vulnibm_sh_created_2022_modifiedsameyear+=1

                else:
                    count_vulnibm_sh_created_2022_anotheryear+=1

            elif(anio_createdate_vulnibm_sh >= 2021):
                count_vulnibm_sh_entries+=1
                count_vulnibm_sh_created_2021+=1
                if(((res/ timedelta(days=1))*(-1)) < 1):
                    count_vulnibm_sh_created_2021_modifiedsameday+=1

                elif(((res/ timedelta(days=30))*(-1)) < 1):
                    count_vulnibm_sh_created_2021_modifiedsamemonth+=1

                elif(((res/ timedelta(days=365))*(-1)) < 1):
                    count_vulnibm_sh_created_2021_modifiedsameyear+=1

                else:
                    count_vulnibm_sh_created_2021_anotheryear+=1

            elif(anio_createdate_vulnibm_sh >= 2020):
                count_vulnibm_sh_entries+=1
                count_vulnibm_sh_created_2020+=1
                if(((res/ timedelta(days=1))*(-1)) < 1):
                    count_vulnibm_sh_created_2020_modifiedsameday+=1

                elif(((res/ timedelta(days=30))*(-1)) < 1):
                    count_vulnibm_sh_created_2020_modifiedsamemonth+=1

                elif(((res/ timedelta(days=365))*(-1)) < 1):
                    count_vulnibm_sh_created_2020_modifiedsameyear+=1

                else:
                    count_vulnibm_sh_created_2020_anotheryear+=1

            elif(anio_createdate_vulnibm_sh >= 2019):
                count_vulnibm_sh_entries+=1
                count_vulnibm_sh_created_2019+=1
                if(((res/ timedelta(days=1))*(-1)) < 1):
                    count_vulnibm_sh_created_2019_modifiedsameday+=1

                elif(((res/ timedelta(days=30))*(-1)) < 1):
                    count_vulnibm_sh_created_2019_modifiedsamemonth+=1

                elif(((res/ timedelta(days=365))*(-1)) < 1):
                    count_vulnibm_sh_created_2019_modifiedsameyear+=1

                else:
                    count_vulnibm_sh_created_2019_anotheryear+=1

            elif(anio_createdate_vulnibm_sh >= 2018):
                count_vulnibm_sh_entries+=1
                count_vulnibm_sh_created_2018+=1
                if(((res/ timedelta(days=1))*(-1)) < 1):
                    count_vulnibm_sh_created_2018_modifiedsameday+=1

                elif(((res/ timedelta(days=30))*(-1)) < 1):
                    count_vulnibm_sh_created_2018_modifiedsamemonth+=1

                elif(((res/ timedelta(days=365))*(-1)) < 1):
                    count_vulnibm_sh_created_2018_modifiedsameyear+=1

                else:
                    count_vulnibm_sh_created_2018_anotheryear+=1        
                            
                    
print("********************ESTADÍSTICAS FECHA DE CREACIÓN/FECHA DE MODIFICACION VULNERABILIDADES IBM PARTE SMART HOME********************")
print("\n")                            
                
print("\n")
print(" DE UN TOTAL DE "+str(count_vulnibm_sh_entries)+" VULNERABILIDADES :\n") 
print("\n")
print("   - LAS ESTADISTICAS DE FECHA DE CREACION SON LAS SIGUIENTES:  \n")
print("      -    EN  "+str(count_vulnibm_sh_created_2023)+" VULNERABILIDADES LA FECHA DE CREACION ES 2023. LAS ESTADÍSTICAS DE FECHA DE MODIFICACION SON LAS SIGUIENTES :  \n")
print("\n")
print("            -    EN  "+str(count_vulnibm_sh_created_2023_modifiedsameday)+" VULNERABILIDADES CREADAS EN 2023, LA ULTIMA MODIFICACIÓN SE PRODUJO ESE MISMO DÍA ")
print("            -    EN  "+str(count_vulnibm_sh_created_2023_modifiedsamemonth)+" VULNERABILIDADES CREADAS EN 2023, LA ÚLTIMA MODIFICACIÓN SE PRODUJO ESE MISMO MES")
print("            -    EN  "+str(count_vulnibm_sh_created_2023_modifiedsameyear)+" VULNERABILIDADES CREADAS EN 2023, LA ÚLTIMA MODIFICACIÓN SE PRODUJO ESE MISMO AÑO ")
print("            -    EN  "+str(count_vulnibm_sh_created_2023_anotheryear)+" VULNERABILIDADES CREADAS EN 2023, LA ÚLTIMA MODIFICACIÓN SE PRODUJO MÁS TARDE DE UN AÑO ")
print("\n")
print("      -    EN  "+str(count_vulnibm_sh_created_2022)+" VULNERABILIDADES LA FECHA DE CREACION ES 2022. LAS ESTADÍSTICAS DE FECHA DE MODIFICACION SON LAS SIGUIENTES :  \n")
print("\n")
print("            -    EN  "+str(count_vulnibm_sh_created_2022_modifiedsameday)+" VULNERABILIDADES CREADAS EN 2022, LA ULTIMA MODIFICACIÓN SE PRODUJO ESE MISMO DÍA ")
print("            -    EN  "+str(count_vulnibm_sh_created_2022_modifiedsamemonth)+" VULNERABILIDADES CREADAS EN 2022, LA ÚLTIMA MODIFICACIÓN SE PRODUJO ESE MISMO MES")
print("            -    EN  "+str(count_vulnibm_sh_created_2022_modifiedsameyear)+" VULNERABILIDADES CREADAS EN 2022, LA ÚLTIMA MODIFICACIÓN SE PRODUJO ESE MISMO AÑO ")
print("            -    EN  "+str(count_vulnibm_sh_created_2022_anotheryear)+" VULNERABILIDADES CREADAS EN 2022, LA ÚLTIMA MODIFICACIÓN SE PRODUJO MÁS TARDE DE UN AÑO ")
print("\n")
print("      -    EN  "+str(count_vulnibm_sh_created_2021)+" VULNERABILIDADES LA FECHA DE CREACION ES 2021. LAS ESTADÍSTICAS DE FECHA DE MODIFICACION SON LAS SIGUIENTES :  \n")
print("\n")
print("            -    EN  "+str(count_vulnibm_sh_created_2021_modifiedsameday)+" VULNERABILIDADES CREADAS EN 2021, LA ULTIMA MODIFICACIÓN SE PRODUJO ESE MISMO DÍA ")
print("            -    EN  "+str(count_vulnibm_sh_created_2021_modifiedsamemonth)+" VULNERABILIDADES CREADAS EN 2021, LA ÚLTIMA MODIFICACIÓN SE PRODUJO ESE MISMO MES")
print("            -    EN  "+str(count_vulnibm_sh_created_2021_modifiedsameyear)+" VULNERABILIDADES CREADAS EN 2021, LA ÚLTIMA MODIFICACIÓN SE PRODUJO ESE MISMO AÑO ")
print("            -    EN  "+str(count_vulnibm_sh_created_2021_anotheryear)+" VULNERABILIDADES CREADAS EN 2021, LA ÚLTIMA MODIFICACIÓN SE PRODUJO MÁS TARDE DE UN AÑO ")
print("\n")
print("      -    EN  "+str(count_vulnibm_sh_created_2020)+" VULNERABILIDADES LA FECHA DE CREACION ES 2020. LAS ESTADÍSTICAS DE FECHA DE MODIFICACION SON LAS SIGUIENTES :  \n")
print("\n")
print("            -    EN  "+str(count_vulnibm_sh_created_2020_modifiedsameday)+" VULNERABILIDADES CREADAS EN 2020, LA ULTIMA MODIFICACIÓN SE PRODUJO ESE MISMO DÍA ")
print("            -    EN  "+str(count_vulnibm_sh_created_2020_modifiedsamemonth)+" VULNERABILIDADES CREADAS EN 2020, LA ÚLTIMA MODIFICACIÓN SE PRODUJO ESE MISMO MES")
print("            -    EN  "+str(count_vulnibm_sh_created_2020_modifiedsameyear)+" VULNERABILIDADES CREADAS EN 2020, LA ÚLTIMA MODIFICACIÓN SE PRODUJO ESE MISMO AÑO ")
print("            -    EN  "+str(count_vulnibm_sh_created_2020_anotheryear)+" VULNERABILIDADES CREADAS EN 2020, LA ÚLTIMA MODIFICACIÓN SE PRODUJO MÁS TARDE DE UN AÑO ")
print("\n")
print("      -    EN  "+str(count_vulnibm_sh_created_2019)+" VULNERABILIDADES LA FECHA DE CREACION ES 2019. LAS ESTADÍSTICAS DE FECHA DE MODIFICACION SON LAS SIGUIENTES :  \n")
print("\n")
print("            -    EN  "+str(count_vulnibm_sh_created_2019_modifiedsameday)+" VULNERABILIDADES CREADAS EN 2019, LA ULTIMA MODIFICACIÓN SE PRODUJO ESE MISMO DÍA ")
print("            -    EN  "+str(count_vulnibm_sh_created_2019_modifiedsamemonth)+" VULNERABILIDADES CREADAS EN 2019, LA ÚLTIMA MODIFICACIÓN SE PRODUJO ESE MISMO MES")
print("            -    EN  "+str(count_vulnibm_sh_created_2019_modifiedsameyear)+" VULNERABILIDADES CREADAS EN 2019, LA ÚLTIMA MODIFICACIÓN SE PRODUJO ESE MISMO AÑO ")
print("            -    EN  "+str(count_vulnibm_sh_created_2019_anotheryear)+" VULNERABILIDADES CREADAS EN 2019, LA ÚLTIMA MODIFICACIÓN SE PRODUJO MÁS TARDE DE UN AÑO ")
print("\n")
print("      -    EN  "+str(count_vulnibm_sh_created_2018)+" VULNERABILIDADES LA FECHA DE CREACION ES 2018 O ANTERIOR. LAS ESTADÍSTICAS DE FECHA DE MODIFICACION SON LAS SIGUIENTES :  \n")
print("\n")
print("            -    EN  "+str(count_vulnibm_sh_created_2018_modifiedsameday)+" VULNERABILIDADES CREADAS EN 2018 O ANTERIORMENTE, LA ULTIMA MODIFICACIÓN SE PRODUJO ESE MISMO DÍA ")
print("            -    EN  "+str(count_vulnibm_sh_created_2018_modifiedsamemonth)+" VULNERABILIDADES CREADAS EN 2018 O ANTERIORMENTE, LA ÚLTIMA MODIFICACIÓN SE PRODUJO ESE MISMO MES")
print("            -    EN  "+str(count_vulnibm_sh_created_2018_modifiedsameyear)+" VULNERABILIDADES CREADAS EN 2018 O ANTERIORMENTE, LA ÚLTIMA MODIFICACIÓN SE PRODUJO ESE MISMO AÑO ")
print("            -    EN  "+str(count_vulnibm_sh_created_2018_anotheryear)+" VULNERABILIDADES CREADAS EN 2018 O ANTERIORMENTE, LA ÚLTIMA MODIFICACIÓN SE PRODUJO MÁS TARDE DE UN AÑO ")
print("\n")








print("********************PORCENTAJE FECHA DE CREACIÓN/FECHA DE MODIFICACION VULNERABILIDADES IBM PARTE SMART HOME********************")
print("\n")                            
                
print("\n")
print(" DE UN TOTAL DE "+str(count_vulnibm_sh_entries)+" VULNERABILIDADES :\n") 
print("\n")
print("   - LOS PORCENTAJES DE FECHA DE CREACION SON LOS SIGUIENTES:  \n")
if(count_vulnibm_sh_created_2023>0):
    print("      -    EN EL  "+str(float(((count_vulnibm_sh_created_2023*100)/count_vulnibm_sh_entries)))+" % DE VULNERABILIDADES LA FECHA DE CREACION ES 2023. LOS PORCENTAJES DE FECHA DE MODIFICACION SON LOS SIGUIENTES  \n")
    print("\n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_created_2023_modifiedsameday*100)/count_vulnibm_sh_created_2023)))+" % DE VULNERABILIDADES CREADAS EN 2023, LA ULTIMA MODIFICACIÓN SE PRODUJO ESE MISMO DÍA ")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_created_2023_modifiedsamemonth*100)/count_vulnibm_sh_created_2023)))+" % DE VULNERABILIDADES CREADAS EN 2023, LA ULTIMA MODIFICACIÓN SE PRODUJO ESE MISMO MES")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_created_2023_modifiedsameyear*100)/count_vulnibm_sh_created_2023)))+" % DE VULNERABILIDADES CREADAS EN 2023, LA ULTIMA MODIFICACIÓN SE PRODUJO ESE MISMO AÑO ")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_created_2023_anotheryear*100)/count_vulnibm_sh_created_2023)))+" % DE VULNERABILIDADES CREADAS EN 2023, LA ULTIMA MODIFICACIÓN SE PRODUJO MÁS TARDE DE UN AÑO ")
    print("\n")
if(count_vulnibm_sh_created_2022>0):
    print("      -    EN EL  "+str(float(((count_vulnibm_sh_created_2022*100)/count_vulnibm_sh_entries)))+" % DE VULNERABILIDADES LA FECHA DE CREACION ES 2022. LOS PORCENTAJES DE FECHA DE MODIFICACION SON LOS SIGUIENTES  \n")
    print("\n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_created_2022_modifiedsameday*100)/count_vulnibm_sh_created_2022)))+" % DE VULNERABILIDADES CREADAS EN 2022, LA ULTIMA MODIFICACIÓN SE PRODUJO ESE MISMO DÍA ")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_created_2022_modifiedsamemonth*100)/count_vulnibm_sh_created_2022)))+" % DE VULNERABILIDADES CREADAS EN 2022, LA ULTIMA MODIFICACIÓN SE PRODUJO ESE MISMO MES")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_created_2022_modifiedsameyear*100)/count_vulnibm_sh_created_2022)))+" % DE VULNERABILIDADES CREADAS EN 2022, LA ULTIMA MODIFICACIÓN SE PRODUJO ESE MISMO AÑO ")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_created_2022_anotheryear*100)/count_vulnibm_sh_created_2022)))+" % DE VULNERABILIDADES CREADAS EN 2022, LA ULTIMA MODIFICACIÓN SE PRODUJO MÁS TARDE DE UN AÑO ")
    print("\n")
if(count_vulnibm_sh_created_2021>0):
    print("      -    EN EL  "+str(float(((count_vulnibm_sh_created_2021*100)/count_vulnibm_sh_entries)))+" % DE VULNERABILIDADES LA FECHA DE CREACION ES 2021. LOS PORCENTAJES DE FECHA DE MODIFICACION SON LOS SIGUIENTES  \n")
    print("\n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_created_2021_modifiedsameday*100)/count_vulnibm_sh_created_2021)))+" % DE VULNERABILIDADES CREADAS EN 2021, LA ULTIMA MODIFICACIÓN SE PRODUJO ESE MISMO DÍA ")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_created_2021_modifiedsamemonth*100)/count_vulnibm_sh_created_2021)))+" % DE VULNERABILIDADES CREADAS EN 2021, LA ULTIMA MODIFICACIÓN SE PRODUJO ESE MISMO MES")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_created_2021_modifiedsameyear*100)/count_vulnibm_sh_created_2021)))+" % DE VULNERABILIDADES CREADAS EN 2021, LA ULTIMA MODIFICACIÓN SE PRODUJO ESE MISMO AÑO ")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_created_2021_anotheryear*100)/count_vulnibm_sh_created_2021)))+" % DE VULNERABILIDADES CREADAS EN 2021, LA ULTIMA MODIFICACIÓN SE PRODUJO MÁS TARDE DE UN AÑO ")
    print("\n")
if(count_vulnibm_sh_created_2020>0):
    print("      -    EN EL  "+str(float(((count_vulnibm_sh_created_2020*100)/count_vulnibm_sh_entries)))+" % DE VULNERABILIDADES LA FECHA DE CREACION ES 2020. LOS PORCENTAJES DE FECHA DE MODIFICACION SON LOS SIGUIENTES  \n")
    print("\n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_created_2020_modifiedsameday*100)/count_vulnibm_sh_created_2020)))+" % DE VULNERABILIDADES CREADAS EN 2020, LA ULTIMA MODIFICACIÓN SE PRODUJO ESE MISMO DÍA ")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_created_2020_modifiedsamemonth*100)/count_vulnibm_sh_created_2020)))+" % DE VULNERABILIDADES CREADAS EN 2020, LA ULTIMA MODIFICACIÓN SE PRODUJO ESE MISMO MES")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_created_2020_modifiedsameyear*100)/count_vulnibm_sh_created_2020)))+" % DE VULNERABILIDADES CREADAS EN 2020, LA ULTIMA MODIFICACIÓN SE PRODUJO ESE MISMO AÑO ")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_created_2020_anotheryear*100)/count_vulnibm_sh_created_2020)))+" % DE VULNERABILIDADES CREADAS EN 2020, LA ULTIMA MODIFICACIÓN SE PRODUJO MÁS TARDE DE UN AÑO ")
    print("\n")
if(count_vulnibm_sh_created_2019>0):
    print("      -    EN EL  "+str(float(((count_vulnibm_sh_created_2019*100)/count_vulnibm_sh_entries)))+" % DE VULNERABILIDADES LA FECHA DE CREACION ES 2019. LOS PORCENTAJES DE FECHA DE MODIFICACION SON LOS SIGUIENTES  \n")
    print("\n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_created_2019_modifiedsameday*100)/count_vulnibm_sh_created_2019)))+" % DE VULNERABILIDADES CREADAS EN 2019, LA ULTIMA MODIFICACIÓN SE PRODUJO ESE MISMO DÍA ")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_created_2019_modifiedsamemonth*100)/count_vulnibm_sh_created_2019)))+" % DE VULNERABILIDADES CREADAS EN 2019, LA ULTIMA MODIFICACIÓN SE PRODUJO ESE MISMO MES")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_created_2019_modifiedsameyear*100)/count_vulnibm_sh_created_2019)))+" % DE VULNERABILIDADES CREADAS EN 2019, LA ULTIMA MODIFICACIÓN SE PRODUJO ESE MISMO AÑO ")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_created_2019_anotheryear*100)/count_vulnibm_sh_created_2019)))+" % DE VULNERABILIDADES CREADAS EN 2019, LA ULTIMA MODIFICACIÓN SE PRODUJO MÁS TARDE DE UN AÑO ")
    print("\n")
if(count_vulnibm_sh_created_2018>0):
    print("      -    EN EL  "+str(float(((count_vulnibm_sh_created_2018*100)/count_vulnibm_sh_entries)))+" % DE VULNERABILIDADES LA FECHA DE CREACION ES 2018 O ANTERIOR. LOS PORCENTAJES DE FECHA DE MODIFICACION SON LOS SIGUIENTES  \n")
    print("\n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_created_2018_modifiedsameday*100)/count_vulnibm_sh_created_2018)))+" % DE VULNERABILIDADES CREADAS EN 2018 O ANTERIORMENTE, LA ULTIMA MODIFICACIÓN SE PRODUJO ESE MISMO DÍA ")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_created_2018_modifiedsamemonth*100)/count_vulnibm_sh_created_2018)))+" % DE VULNERABILIDADES CREADAS EN 2018 O ANTERIORMENTE, LA ULTIMA MODIFICACIÓN SE PRODUJO ESE MISMO MES")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_created_2018_modifiedsameyear*100)/count_vulnibm_sh_created_2018)))+" % DE VULNERABILIDADES CREADAS EN 2018 O ANTERIORMENTE, LA ULTIMA MODIFICACIÓN SE PRODUJO ESE MISMO AÑO ")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_created_2018_anotheryear*100)/count_vulnibm_sh_created_2018)))+" % DE VULNERABILIDADES CREADAS EN 2018 O ANTERIORMENTE, LA ULTIMA MODIFICACIÓN SE PRODUJO MÁS TARDE DE UN AÑO ")
    print("\n")





    
    
    
    
    
    
    
print("********************ESTADÍSTICAS FECHA DE CREACIÓN/FECHA DE MODIFICACION VULNERABILITIES IBM PARTE IOT Y SMART HOME CONJUNTAS********************")
print("\n")                            
                
print("\n")
print(" DE UN TOTAL DE "+str(count_vulnibm_sh_entries+count_vulnibm_iot_entries)+" VULNERABILIDADES :\n") 
print("\n")
print("   - LAS ESTADISTICAS DE FECHA DE CREACION SON LAS SIGUIENTES:  \n")
print("      -    EN  "+str(count_vulnibm_sh_created_2023+count_vulnibm_iot_created_2023)+" VULNERABILIDADES LA FECHA DE CREACION ES 2023. LAS ESTADÍSTICAS DE FECHA DE MODIFICACION SON LAS SIGUIENTES :  \n")
print("\n")
print("            -    EN  "+str(count_vulnibm_sh_created_2023_modifiedsameday+count_vulnibm_iot_created_2023_modifiedsameday)+" VULNERABILIDADES CREADAS EN 2023, LA ULTIMA MODIFICACIÓN SE PRODUJO ESE MISMO DÍA ")
print("            -    EN  "+str(count_vulnibm_sh_created_2023_modifiedsamemonth+count_vulnibm_iot_created_2023_modifiedsamemonth)+" VULNERABILIDADES CREADAS EN 2023, LA ÚLTIMA MODIFICACIÓN SE PRODUJO ESE MISMO MES")
print("            -    EN  "+str(count_vulnibm_sh_created_2023_modifiedsameyear+count_vulnibm_iot_created_2023_modifiedsameyear)+" VULNERABILIDADES CREADAS EN 2023, LA ÚLTIMA MODIFICACIÓN SE PRODUJO ESE MISMO AÑO ")
print("            -    EN  "+str(count_vulnibm_sh_created_2023_anotheryear+count_vulnibm_iot_created_2023_anotheryear)+" VULNERABILIDADES CREADAS EN 2023, LA ÚLTIMA MODIFICACIÓN SE PRODUJO MÁS TARDE DE UN AÑO ")
print("\n")
print("      -    EN  "+str(count_vulnibm_sh_created_2022+count_vulnibm_iot_created_2022)+" VULNERABILIDADES LA FECHA DE CREACION ES 2022. LAS ESTADÍSTICAS DE FECHA DE MODIFICACION SON LAS SIGUIENTES :  \n")
print("\n")
print("            -    EN  "+str(count_vulnibm_sh_created_2022_modifiedsameday+count_vulnibm_iot_created_2022_modifiedsameday)+" VULNERABILIDADES CREADAS EN 2022, LA ULTIMA MODIFICACIÓN SE PRODUJO ESE MISMO DÍA ")
print("            -    EN  "+str(count_vulnibm_sh_created_2022_modifiedsamemonth+count_vulnibm_iot_created_2022_modifiedsamemonth)+" VULNERABILIDADES CREADAS EN 2022, LA ÚLTIMA MODIFICACIÓN SE PRODUJO ESE MISMO MES")
print("            -    EN  "+str(count_vulnibm_sh_created_2022_modifiedsameyear+count_vulnibm_iot_created_2022_modifiedsameyear)+" VULNERABILIDADES CREADAS EN 2022, LA ÚLTIMA MODIFICACIÓN SE PRODUJO ESE MISMO AÑO ")
print("            -    EN  "+str(count_vulnibm_sh_created_2022_anotheryear+count_vulnibm_iot_created_2022_anotheryear)+" VULNERABILIDADES CREADAS EN 2022, LA ÚLTIMA MODIFICACIÓN SE PRODUJO MÁS TARDE DE UN AÑO ")
print("\n")
print("      -    EN  "+str(count_vulnibm_sh_created_2021+count_vulnibm_iot_created_2021)+" VULNERABILIDADES LA FECHA DE CREACION ES 2021. LAS ESTADÍSTICAS DE FECHA DE MODIFICACION SON LAS SIGUIENTES :  \n")
print("\n")
print("            -    EN  "+str(count_vulnibm_sh_created_2021_modifiedsameday+count_vulnibm_iot_created_2021_modifiedsameday)+" VULNERABILIDADES CREADAS EN 2021, LA ULTIMA MODIFICACIÓN SE PRODUJO ESE MISMO DÍA ")
print("            -    EN  "+str(count_vulnibm_sh_created_2021_modifiedsamemonth+count_vulnibm_iot_created_2021_modifiedsamemonth)+" VULNERABILIDADES CREADAS EN 2021, LA ÚLTIMA MODIFICACIÓN SE PRODUJO ESE MISMO MES")
print("            -    EN  "+str(count_vulnibm_sh_created_2021_modifiedsameyear+count_vulnibm_iot_created_2021_modifiedsameyear)+" VULNERABILIDADES CREADAS EN 2021, LA ÚLTIMA MODIFICACIÓN SE PRODUJO ESE MISMO AÑO ")
print("            -    EN  "+str(count_vulnibm_sh_created_2021_anotheryear+count_vulnibm_iot_created_2021_anotheryear)+" VULNERABILIDADES CREADAS EN 2021, LA ÚLTIMA MODIFICACIÓN SE PRODUJO MÁS TARDE DE UN AÑO ")
print("\n")
print("      -    EN  "+str(count_vulnibm_sh_created_2020+count_vulnibm_iot_created_2020)+" VULNERABILIDADES LA FECHA DE CREACION ES 2020. LAS ESTADÍSTICAS DE FECHA DE MODIFICACION SON LAS SIGUIENTES :  \n")
print("\n")
print("            -    EN  "+str(count_vulnibm_sh_created_2020_modifiedsameday+count_vulnibm_iot_created_2020_modifiedsameday)+" VULNERABILIDADES CREADAS EN 2020, LA ULTIMA MODIFICACIÓN SE PRODUJO ESE MISMO DÍA ")
print("            -    EN  "+str(count_vulnibm_sh_created_2020_modifiedsamemonth+count_vulnibm_iot_created_2020_modifiedsamemonth)+" VULNERABILIDADES CREADAS EN 2020, LA ÚLTIMA MODIFICACIÓN SE PRODUJO ESE MISMO MES")
print("            -    EN  "+str(count_vulnibm_sh_created_2020_modifiedsameyear+count_vulnibm_iot_created_2020_modifiedsameyear)+" VULNERABILIDADES CREADAS EN 2020, LA ÚLTIMA MODIFICACIÓN SE PRODUJO ESE MISMO AÑO ")
print("            -    EN  "+str(count_vulnibm_sh_created_2020_anotheryear+count_vulnibm_iot_created_2020_anotheryear)+" VULNERABILIDADES CREADAS EN 2020, LA ÚLTIMA MODIFICACIÓN SE PRODUJO MÁS TARDE DE UN AÑO ")
print("\n")
print("      -    EN  "+str(count_vulnibm_sh_created_2019+count_vulnibm_iot_created_2019)+" VULNERABILIDADES LA FECHA DE CREACION ES 2019. LAS ESTADÍSTICAS DE FECHA DE MODIFICACION SON LAS SIGUIENTES :  \n")
print("\n")
print("            -    EN  "+str(count_vulnibm_sh_created_2019_modifiedsameday+count_vulnibm_iot_created_2019_modifiedsameday)+" VULNERABILIDADES CREADAS EN 2019, LA ULTIMA MODIFICACIÓN SE PRODUJO ESE MISMO DÍA ")
print("            -    EN  "+str(count_vulnibm_sh_created_2019_modifiedsamemonth+count_vulnibm_iot_created_2019_modifiedsamemonth)+" VULNERABILIDADES CREADAS EN 2019, LA ÚLTIMA MODIFICACIÓN SE PRODUJO ESE MISMO MES")
print("            -    EN  "+str(count_vulnibm_sh_created_2019_modifiedsameyear+count_vulnibm_iot_created_2019_modifiedsameyear)+" VULNERABILIDADES CREADAS EN 2019, LA ÚLTIMA MODIFICACIÓN SE PRODUJO ESE MISMO AÑO ")
print("            -    EN  "+str(count_vulnibm_sh_created_2019_anotheryear+count_vulnibm_iot_created_2019_anotheryear)+" VULNERABILIDADES CREADAS EN 2019, LA ÚLTIMA MODIFICACIÓN SE PRODUJO MÁS TARDE DE UN AÑO ")
print("\n")
print("      -    EN  "+str(count_vulnibm_sh_created_2018+count_vulnibm_iot_created_2018)+" VULNERABILIDADES LA FECHA DE CREACION ES 2018. LAS ESTADÍSTICAS DE FECHA DE MODIFICACION SON LAS SIGUIENTES :  \n")
print("\n")
print("            -    EN  "+str(count_vulnibm_sh_created_2018_modifiedsameday+count_vulnibm_iot_created_2018_modifiedsameday)+" VULNERABILIDADES CREADAS EN 2018, LA ULTIMA MODIFICACIÓN SE PRODUJO ESE MISMO DÍA ")
print("            -    EN  "+str(count_vulnibm_sh_created_2018_modifiedsamemonth+count_vulnibm_iot_created_2018_modifiedsamemonth)+" VULNERABILIDADES CREADAS EN 2018, LA ÚLTIMA MODIFICACIÓN SE PRODUJO ESE MISMO MES")
print("            -    EN  "+str(count_vulnibm_sh_created_2018_modifiedsameyear+count_vulnibm_iot_created_2018_modifiedsameyear)+" VULNERABILIDADES CREADAS EN 2018, LA ÚLTIMA MODIFICACIÓN SE PRODUJO ESE MISMO AÑO ")
print("            -    EN  "+str(count_vulnibm_sh_created_2018_anotheryear+count_vulnibm_iot_created_2018_anotheryear)+" VULNERABILIDADES CREADAS EN 2018, LA ÚLTIMA MODIFICACIÓN SE PRODUJO MÁS TARDE DE UN AÑO ")
print("\n")













print("********************PORCENTAJE FECHA DE CREACIÓN/FECHA DE MODIFICACION VULNERABILITIES IBM PARTE IOT Y SMART HOME CONJUNTAS********************")
print("\n")                            
                
print("\n")
print(" DE UN TOTAL DE "+str(count_vulnibm_sh_entries+count_vulnibm_iot_entries)+" VULNERABILIDADES :\n") 
print("\n")
print("   - LOS PORCENTAJES DE FECHA DE CREACION SON LOS SIGUIENTES:  \n")
print("      -    EN EL  "+str(float(((count_vulnibm_sh_created_2023+count_vulnibm_iot_created_2023)*100)/(count_vulnibm_sh_entries+count_vulnibm_iot_entries)))+" % DE VULNERABILIDADES LA FECHA DE CREACION ES 2023. LOS PORCENTAJES DE FECHA DE MODIFICACION SON LOS SIGUIENTES  \n")
print("\n")
print("            -    EN EL  "+str(float((((count_vulnibm_sh_created_2023_modifiedsameday+count_vulnibm_iot_created_2023_modifiedsameday)*100)/(count_vulnibm_sh_created_2023+count_vulnibm_iot_created_2023))))+" % DE VULNERABILIDADES CREADAS EN 2023, LA ULTIMA MODIFICACIÓN SE PRODUJO ESE MISMO DÍA ")
print("            -    EN EL  "+str(float((((count_vulnibm_sh_created_2023_modifiedsamemonth+count_vulnibm_iot_created_2023_modifiedsamemonth)*100)/(count_vulnibm_sh_created_2023+count_vulnibm_iot_created_2023))))+" % DE VULNERABILIDADES CREADAS EN 2023, LA ULTIMA MODIFICACIÓN SE PRODUJO ESE MISMO MES")
print("            -    EN EL  "+str(float((((count_vulnibm_sh_created_2023_modifiedsameyear+count_vulnibm_iot_created_2023_modifiedsameyear)*100)/(count_vulnibm_sh_created_2023+count_vulnibm_iot_created_2023))))+" % DE VULNERABILIDADES CREADAS EN 2023, LA ULTIMA MODIFICACIÓN SE PRODUJO ESE MISMO AÑO ")
print("            -    EN EL  "+str(float((((count_vulnibm_sh_created_2023_anotheryear+count_vulnibm_iot_created_2023_anotheryear)*100)/(count_vulnibm_sh_created_2023+count_vulnibm_iot_created_2023))))+" % DE VULNERABILIDADES CREADAS EN 2023, LA ULTIMA MODIFICACIÓN SE PRODUJO MÁS TARDE DE UN AÑO ")
print("\n")
print("      -    EN EL  "+str(float(((count_vulnibm_sh_created_2022+count_vulnibm_iot_created_2022)*100)/(count_vulnibm_sh_entries+count_vulnibm_iot_entries)))+" % DE VULNERABILIDADES LA FECHA DE CREACION ES 2022. LOS PORCENTAJES DE FECHA DE MODIFICACION SON LOS SIGUIENTES  \n")
print("\n")
print("            -    EN EL  "+str(float((((count_vulnibm_sh_created_2022_modifiedsameday+count_vulnibm_iot_created_2022_modifiedsameday)*100)/(count_vulnibm_sh_created_2022+count_vulnibm_iot_created_2022))))+" % DE VULNERABILIDADES CREADAS EN 2022, LA ULTIMA MODIFICACIÓN SE PRODUJO ESE MISMO DÍA ")
print("            -    EN EL  "+str(float((((count_vulnibm_sh_created_2022_modifiedsamemonth+count_vulnibm_iot_created_2022_modifiedsamemonth)*100)/(count_vulnibm_sh_created_2022+count_vulnibm_iot_created_2022))))+" % DE VULNERABILIDADES CREADAS EN 2022, LA ULTIMA MODIFICACIÓN SE PRODUJO ESE MISMO MES")
print("            -    EN EL  "+str(float((((count_vulnibm_sh_created_2022_modifiedsameyear+count_vulnibm_iot_created_2022_modifiedsameyear)*100)/(count_vulnibm_sh_created_2022+count_vulnibm_iot_created_2022))))+" % DE VULNERABILIDADES CREADAS EN 2022, LA ULTIMA MODIFICACIÓN SE PRODUJO ESE MISMO AÑO ")
print("            -    EN EL  "+str(float((((count_vulnibm_sh_created_2022_anotheryear+count_vulnibm_iot_created_2022_anotheryear)*100)/(count_vulnibm_sh_created_2022+count_vulnibm_iot_created_2022))))+" % DE VULNERABILIDADES CREADAS EN 2022, LA ULTIMA MODIFICACIÓN SE PRODUJO MÁS TARDE DE UN AÑO ")
print("\n")
if((count_vulnibm_sh_created_2021+count_vulnibm_iot_created_2021)>0):
    print("      -    EN EL  "+str(float(((count_vulnibm_sh_created_2021+count_vulnibm_iot_created_2021)*100)/(count_vulnibm_sh_entries+count_vulnibm_iot_entries)))+" % DE VULNERABILIDADES LA FECHA DE CREACION ES 2021. LOS PORCENTAJES DE FECHA DE MODIFICACION SON LOS SIGUIENTES  \n")
    print("\n")
    print("            -    EN EL  "+str(float((((count_vulnibm_sh_created_2021_modifiedsameday+count_vulnibm_iot_created_2021_modifiedsameday)*100)/(count_vulnibm_sh_created_2021+count_vulnibm_iot_created_2021))))+" % DE VULNERABILIDADES CREADAS EN 2021, LA ULTIMA MODIFICACIÓN SE PRODUJO ESE MISMO DÍA ")
    print("            -    EN EL  "+str(float((((count_vulnibm_sh_created_2021_modifiedsamemonth+count_vulnibm_iot_created_2021_modifiedsamemonth)*100)/(count_vulnibm_sh_created_2021+count_vulnibm_iot_created_2021))))+" % DE VULNERABILIDADES CREADAS EN 2021, LA ULTIMA MODIFICACIÓN SE PRODUJO ESE MISMO MES")
    print("            -    EN EL  "+str(float((((count_vulnibm_sh_created_2021_modifiedsameyear+count_vulnibm_iot_created_2021_modifiedsameyear)*100)/(count_vulnibm_sh_created_2021+count_vulnibm_iot_created_2021))))+" % DE VULNERABILIDADES CREADAS EN 2021, LA ULTIMA MODIFICACIÓN SE PRODUJO ESE MISMO AÑO ")
    print("            -    EN EL  "+str(float((((count_vulnibm_sh_created_2021_anotheryear+count_vulnibm_iot_created_2021_anotheryear)*100)/(count_vulnibm_sh_created_2021+count_vulnibm_iot_created_2021))))+" % DE VULNERABILIDADES CREADAS EN 2021, LA ULTIMA MODIFICACIÓN SE PRODUJO MÁS TARDE DE UN AÑO ")
    print("\n")
if((count_vulnibm_sh_created_2020+count_vulnibm_iot_created_2020)>0):
    print("      -    EN EL  "+str(float(((count_vulnibm_sh_created_2020+count_vulnibm_iot_created_2020)*100)/(count_vulnibm_sh_entries+count_vulnibm_iot_entries)))+" % DE VULNERABILIDADES LA FECHA DE CREACION ES 2020. LOS PORCENTAJES DE FECHA DE MODIFICACION SON LOS SIGUIENTES  \n")
    print("\n")
    print("            -    EN EL  "+str(float((((count_vulnibm_sh_created_2020_modifiedsameday+count_vulnibm_iot_created_2020_modifiedsameday)*100)/(count_vulnibm_sh_created_2020+count_vulnibm_iot_created_2020))))+" % DE VULNERABILIDADES CREADAS EN 2020, LA ULTIMA MODIFICACIÓN SE PRODUJO ESE MISMO DÍA ")
    print("            -    EN EL  "+str(float((((count_vulnibm_sh_created_2020_modifiedsamemonth+count_vulnibm_iot_created_2020_modifiedsamemonth)*100)/(count_vulnibm_sh_created_2020+count_vulnibm_iot_created_2020))))+" % DE VULNERABILIDADES CREADAS EN 2020, LA ULTIMA MODIFICACIÓN SE PRODUJO ESE MISMO MES")
    print("            -    EN EL  "+str(float((((count_vulnibm_sh_created_2020_modifiedsameyear+count_vulnibm_iot_created_2020_modifiedsameyear)*100)/(count_vulnibm_sh_created_2020+count_vulnibm_iot_created_2020))))+" % DE VULNERABILIDADES CREADAS EN 2020, LA ULTIMA MODIFICACIÓN SE PRODUJO ESE MISMO AÑO ")
    print("            -    EN EL  "+str(float((((count_vulnibm_sh_created_2020_anotheryear+count_vulnibm_iot_created_2020_anotheryear)*100)/(count_vulnibm_sh_created_2020+count_vulnibm_iot_created_2020))))+" % DE VULNERABILIDADES CREADAS EN 2020, LA ULTIMA MODIFICACIÓN SE PRODUJO MÁS TARDE DE UN AÑO ")
    print("\n")
if((count_vulnibm_sh_created_2019+count_vulnibm_iot_created_2019)>0):
    print("      -    EN EL  "+str(float(((count_vulnibm_sh_created_2019+count_vulnibm_iot_created_2019)*100)/(count_vulnibm_sh_entries+count_vulnibm_iot_entries)))+" % DE VULNERABILIDADES LA FECHA DE CREACION ES 2019. LOS PORCENTAJES DE FECHA DE MODIFICACION SON LOS SIGUIENTES  \n")
    print("\n")
    print("            -    EN EL  "+str(float((((count_vulnibm_sh_created_2019_modifiedsameday+count_vulnibm_iot_created_2019_modifiedsameday)*100)/(count_vulnibm_sh_created_2019+count_vulnibm_iot_created_2019))))+" % DE VULNERABILIDADES CREADAS EN 2019, LA ULTIMA MODIFICACIÓN SE PRODUJO ESE MISMO DÍA ")
    print("            -    EN EL  "+str(float((((count_vulnibm_sh_created_2019_modifiedsamemonth+count_vulnibm_iot_created_2019_modifiedsamemonth)*100)/(count_vulnibm_sh_created_2019+count_vulnibm_iot_created_2019))))+" % DE VULNERABILIDADES CREADAS EN 2019, LA ULTIMA MODIFICACIÓN SE PRODUJO ESE MISMO MES")
    print("            -    EN EL  "+str(float((((count_vulnibm_sh_created_2019_modifiedsameyear+count_vulnibm_iot_created_2019_modifiedsameyear)*100)/(count_vulnibm_sh_created_2019+count_vulnibm_iot_created_2019))))+" % DE VULNERABILIDADES CREADAS EN 2019, LA ULTIMA MODIFICACIÓN SE PRODUJO ESE MISMO AÑO ")
    print("            -    EN EL  "+str(float((((count_vulnibm_sh_created_2019_anotheryear+count_vulnibm_iot_created_2019_anotheryear)*100)/(count_vulnibm_sh_created_2019+count_vulnibm_iot_created_2019))))+" % DE VULNERABILIDADES CREADAS EN 2019, LA ULTIMA MODIFICACIÓN SE PRODUJO MÁS TARDE DE UN AÑO ")
    print("\n")
if((count_vulnibm_sh_created_2018+count_vulnibm_iot_created_2018)>0):
    print("      -    EN EL  "+str(float(((count_vulnibm_sh_created_2018+count_vulnibm_iot_created_2018)*100)/(count_vulnibm_sh_entries+count_vulnibm_iot_entries)))+" % DE VULNERABILIDADES LA FECHA DE CREACION ES 2018 O ANTERIOR. LOS PORCENTAJES DE FECHA DE MODIFICACION SON LOS SIGUIENTES  \n")
    print("\n")
    print("            -    EN EL  "+str(float((((count_vulnibm_sh_created_2018_modifiedsameday+count_vulnibm_iot_created_2018_modifiedsameday)*100)/(count_vulnibm_sh_created_2018+count_vulnibm_iot_created_2018))))+" % DE VULNERABILIDADES CREADAS EN 2018 O ANTERIORMENTE, LA ULTIMA MODIFICACIÓN SE PRODUJO ESE MISMO DÍA ")
    print("            -    EN EL  "+str(float((((count_vulnibm_sh_created_2018_modifiedsamemonth+count_vulnibm_iot_created_2018_modifiedsamemonth)*100)/(count_vulnibm_sh_created_2018+count_vulnibm_iot_created_2018))))+" % DE VULNERABILIDADES CREADAS EN 2018 O ANTERIORMENTE, LA ULTIMA MODIFICACIÓN SE PRODUJO ESE MISMO MES")
    print("            -    EN EL  "+str(float((((count_vulnibm_sh_created_2018_modifiedsameyear+count_vulnibm_iot_created_2018_modifiedsameyear)*100)/(count_vulnibm_sh_created_2018+count_vulnibm_iot_created_2018))))+" % DE VULNERABILIDADES CREADAS EN 2018 O ANTERIORMENTE, LA ULTIMA MODIFICACIÓN SE PRODUJO ESE MISMO AÑO ")
    print("            -    EN EL  "+str(float((((count_vulnibm_sh_created_2018_anotheryear+count_vulnibm_iot_created_2018_anotheryear)*100)/(count_vulnibm_sh_created_2018+count_vulnibm_iot_created_2018))))+" % DE VULNERABILIDADES CREADAS EN 2018 O ANTERIORMENTE, LA ULTIMA MODIFICACIÓN SE PRODUJO MÁS TARDE DE UN AÑO ")
    print("\n")