import pandas as pd
from datetime import datetime,timedelta



#Abro los ficheros con los que voy a tratar




df_alienvault_iot = pd.read_excel('alienvault_iot_2023.xlsx')
#Variable donde almaceno el contador total de entradas
count_alienvault_iot_entries=0
#Variable donde almaceno el contador total de entradas validas desde un anio especifico
count_alienvault_iot_valid_from_2023=0
#Variable donde almaceno el tiempo de validez de una entrada dado un anio especifico
count_alienvault_iot_valid_from_2023_valid_until_sameday=0
count_alienvault_iot_valid_from_2023_valid_until_samemonth=0
count_alienvault_iot_valid_from_2023_valid_until_sameyear=0
count_alienvault_iot_valid_from_2023_anotheryear=0

count_alienvault_iot_valid_from_2022=0
count_alienvault_iot_valid_from_2022_valid_until_sameday=0
count_alienvault_iot_valid_from_2022_valid_until_samemonth=0
count_alienvault_iot_valid_from_2022_valid_until_sameyear=0
count_alienvault_iot_valid_from_2022_anotheryear=0

count_alienvault_iot_valid_from_2021=0
count_alienvault_iot_valid_from_2021_valid_until_sameday=0
count_alienvault_iot_valid_from_2021_valid_until_samemonth=0
count_alienvault_iot_valid_from_2021_valid_until_sameyear=0
count_alienvault_iot_valid_from_2021_anotheryear=0

count_alienvault_iot_valid_from_2020=0
count_alienvault_iot_valid_from_2020_valid_until_sameday=0
count_alienvault_iot_valid_from_2020_valid_until_samemonth=0
count_alienvault_iot_valid_from_2020_valid_until_sameyear=0
count_alienvault_iot_valid_from_2020_anotheryear=0

count_alienvault_iot_valid_from_2019=0
count_alienvault_iot_valid_from_2019_valid_until_sameday=0
count_alienvault_iot_valid_from_2019_valid_until_samemonth=0
count_alienvault_iot_valid_from_2019_valid_until_sameyear=0
count_alienvault_iot_valid_from_2019_anotheryear=0

count_alienvault_iot_valid_from_2018=0
count_alienvault_iot_valid_from_2018_valid_until_sameday=0
count_alienvault_iot_valid_from_2018_valid_until_samemonth=0
count_alienvault_iot_valid_from_2018_valid_until_sameyear=0
count_alienvault_iot_valid_from_2018_anotheryear=0


#Comprobamos el comienzo de validez
for r in range(0,len(df_alienvault_iot["valid_from"])):
    #Si existen varios valores de INICIO VALIDEZ en una misma fila
    if('[' in df_alienvault_iot["valid_from"][r]):
        #Obtengo los valores de INICIO VALIDEZ y FIN DE VALIDEZ de la fila actual
        aux=df_alienvault_iot["valid_from"][r].split(",")
        auxx=df_alienvault_iot["valid_until"][r].split(",")
        for l in range(0,len(aux)):
            if((len(aux)>0) and (len(auxx) == len(aux))):
                #Obtengo el valor actual de INICIO VALIDEZ y FIN DE VALIDEZ
                aux_str=aux[l].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","").replace("T"," ")
                auxx_str=auxx[l].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","").replace("T"," ")
                #Compruebo que los valores no sean nulos
                if((aux_str!='NONE' and auxx_str!='NONE') and ('Z' in aux_str and 'Z' in auxx_str)):
                    aux2=aux_str.split(".")
                    validfrom = datetime.strptime(aux2[0], '%Y-%m-%d %H:%M:%S')
                    aux22=auxx_str.split(".")
                    validuntil = datetime.strptime(aux22[0], '%Y-%m-%d %H:%M:%S')
                    #Obtengo ambos valores y calculo su diferencia
                    res=validfrom-validuntil
                    #Obtengo el anio de INICIO VALIDEZ
                    str_anio_validfrom_alienvault_iot=aux_str.split("-")
                    anio_validfrom_alienvault_iot=int(str_anio_validfrom_alienvault_iot[0])
                    #Compruebo el anio desde el que es valido la entrada
                    if(anio_validfrom_alienvault_iot >= 2023):
                        count_alienvault_iot_entries+=1
                        count_alienvault_iot_valid_from_2023+=1
                        #Compruebo si la diferencia entre ambas es menor de un dia
                        if(((res/ timedelta(days=1))*(-1)) < 1):
                            count_alienvault_iot_valid_from_2023_valid_until_sameday+=1
                        #Compruebo si la diferencia entre ambas es menor de un mes    
                        elif(((res/ timedelta(days=30))*(-1)) < 1):
                            count_alienvault_iot_valid_from_2023_valid_until_samemonth+=1
                         #Compruebo si la diferencia entre ambas es menor de un anio  
                        elif(((res/ timedelta(days=365))*(-1)) < 1):
                            count_alienvault_iot_valid_from_2023_valid_until_sameyear+=1
                            
                        else:
                            #Compruebo si la diferencia entre ambas es mayor de un anio
                            count_alienvault_iot_valid_from_2023_anotheryear+=1
                            
                    elif(anio_validfrom_alienvault_iot >= 2022):
                        count_alienvault_iot_entries+=1
                        count_alienvault_iot_valid_from_2022+=1
                        if(((res/ timedelta(days=1))*(-1)) < 1):
                            count_alienvault_iot_valid_from_2022_valid_until_sameday+=1
                            
                        elif(((res/ timedelta(days=30))*(-1)) < 1):
                            count_alienvault_iot_valid_from_2022_valid_until_samemonth+=1
                            
                        elif(((res/ timedelta(days=365))*(-1)) < 1):
                            count_alienvault_iot_valid_from_2022_valid_until_sameyear+=1
                            
                        else:
                            count_alienvault_iot_valid_from_2022_anotheryear+=1
                            
                    elif(anio_validfrom_alienvault_iot >= 2021):
                        count_alienvault_iot_entries+=1
                        count_alienvault_iot_valid_from_2021+=1
                        if(((res/ timedelta(days=1))*(-1)) < 1):
                            count_alienvault_iot_valid_from_2021_valid_until_sameday+=1
                            
                        elif(((res/ timedelta(days=30))*(-1)) < 1):
                            count_alienvault_iot_valid_from_2021_valid_until_samemonth+=1
                            
                        elif(((res/ timedelta(days=365))*(-1)) < 1):
                            count_alienvault_iot_valid_from_2021_valid_until_sameyear+=1
                            
                        else:
                            count_alienvault_iot_valid_from_2021_anotheryear+=1
                            
                    elif(anio_validfrom_alienvault_iot >= 2020):
                        count_alienvault_iot_entries+=1
                        count_alienvault_iot_valid_from_2020+=1
                        if(((res/ timedelta(days=1))*(-1)) < 1):
                            count_alienvault_iot_valid_from_2020_valid_until_sameday+=1
                            
                        elif(((res/ timedelta(days=30))*(-1)) < 1):
                            count_alienvault_iot_valid_from_2020_valid_until_samemonth+=1
                            
                        elif(((res/ timedelta(days=365))*(-1)) < 1):
                            count_alienvault_iot_valid_from_2020_valid_until_sameyear+=1
                            
                        else:
                            count_alienvault_iot_valid_from_2020_anotheryear+=1
                            
                    elif(anio_validfrom_alienvault_iot >= 2019):
                        count_alienvault_iot_entries+=1
                        count_alienvault_iot_valid_from_2019+=1
                        if(((res/ timedelta(days=1))*(-1)) < 1):
                            count_alienvault_iot_valid_from_2019_valid_until_sameday+=1
                            
                        elif(((res/ timedelta(days=30))*(-1)) < 1):
                            count_alienvault_iot_valid_from_2019_valid_until_samemonth+=1
                            
                        elif(((res/ timedelta(days=365))*(-1)) < 1):
                            count_alienvault_iot_valid_from_2019_valid_until_sameyear+=1
                            
                        else:
                            count_alienvault_iot_valid_from_2019_anotheryear+=1
                            
                    elif(anio_validfrom_alienvault_iot >= 2018):
                        count_alienvault_iot_entries+=1
                        count_alienvault_iot_valid_from_2018+=1
                        if(((res/ timedelta(days=1))*(-1)) < 1):
                            count_alienvault_iot_valid_from_2018_valid_until_sameday+=1
                            
                        elif(((res/ timedelta(days=30))*(-1)) < 1):
                            count_alienvault_iot_valid_from_2018_valid_until_samemonth+=1
                            
                        elif(((res/ timedelta(days=365))*(-1)) < 1):
                            count_alienvault_iot_valid_from_2018_valid_until_sameyear+=1
                            
                        else:
                            count_alienvault_iot_valid_from_2018_anotheryear+=1
                            
    else:
        #Si existe un unico valor de INICIO VALIDEZ y FIN DE VALIDEZ para fila actual
        aux_strr=df_alienvault_iot["valid_from"][r].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","").replace("T"," ")
        auxx_strr=df_alienvault_iot["valid_until"][r].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","").replace("T"," ")
        if((aux_strr!='NONE' and auxx_strr!='NONE') and ('Z' in aux_strr and 'Z' in auxx_strr)):
            aux22=aux_strr.split(".")
            validfrom = datetime.strptime(aux22[0], '%Y-%m-%d %H:%M:%S')
            aux222=auxx_strr.split(".")
            validuntil = datetime.strptime(aux222[0], '%Y-%m-%d %H:%M:%S')
            res=validfrom-validuntil
            str_anio_validfrom_alienvault_iot=auxx_strr.split("-")
            anio_validfrom_alienvault_iot=int(str_anio_validfrom_alienvault_iot[0]) 
            #Compruebo el anio desde el que es valida la entrada, una vez hemos calculado la diferencia anteriormente
            if(anio_validfrom_alienvault_iot >= 2023):
                count_alienvault_iot_entries+=1
                count_alienvault_iot_valid_from_2023+=1
                if(((res/ timedelta(days=1))*(-1)) < 1):
                    count_alienvault_iot_valid_from_2023_valid_until_sameday+=1

                elif(((res/ timedelta(days=30))*(-1)) < 1):
                    count_alienvault_iot_valid_from_2023_valid_until_samemonth+=1

                elif(((res/ timedelta(days=365))*(-1)) < 1):
                    count_alienvault_iot_valid_from_2023_valid_until_sameyear+=1

                else:
                    count_alienvault_iot_valid_from_2023_anotheryear+=1

            elif(anio_validfrom_alienvault_iot >= 2022):
                count_alienvault_iot_entries+=1
                count_alienvault_iot_valid_from_2022+=1
                if(((res/ timedelta(days=1))*(-1)) < 1):
                    count_alienvault_iot_valid_from_2022_valid_until_sameday+=1

                elif(((res/ timedelta(days=30))*(-1)) < 1):
                    count_alienvault_iot_valid_from_2022_valid_until_samemonth+=1

                elif(((res/ timedelta(days=365))*(-1)) < 1):
                    count_alienvault_iot_valid_from_2022_valid_until_sameyear+=1

                else:
                    count_alienvault_iot_valid_from_2022_anotheryear+=1

            elif(anio_validfrom_alienvault_iot >= 2021):
                count_alienvault_iot_entries+=1
                count_alienvault_iot_valid_from_2021+=1
                if(((res/ timedelta(days=1))*(-1)) < 1):
                    count_alienvault_iot_valid_from_2021_valid_until_sameday+=1

                elif(((res/ timedelta(days=30))*(-1)) < 1):
                    count_alienvault_iot_valid_from_2021_valid_until_samemonth+=1

                elif(((res/ timedelta(days=365))*(-1)) < 1):
                    count_alienvault_iot_valid_from_2021_valid_until_sameyear+=1

                else:
                    count_alienvault_iot_valid_from_2021_anotheryear+=1

            elif(anio_validfrom_alienvault_iot >= 2020):
                count_alienvault_iot_entries+=1
                count_alienvault_iot_valid_from_2020+=1
                if(((res/ timedelta(days=1))*(-1)) < 1):
                    count_alienvault_iot_valid_from_2020_valid_until_sameday+=1

                elif(((res/ timedelta(days=30))*(-1)) < 1):
                    count_alienvault_iot_valid_from_2020_valid_until_samemonth+=1

                elif(((res/ timedelta(days=365))*(-1)) < 1):
                    count_alienvault_iot_valid_from_2020_valid_until_sameyear+=1

                else:
                    count_alienvault_iot_valid_from_2020_anotheryear+=1

            elif(anio_validfrom_alienvault_iot >= 2019):
                count_alienvault_iot_entries+=1
                count_alienvault_iot_valid_from_2019+=1
                if(((res/ timedelta(days=1))*(-1)) < 1):
                    count_alienvault_iot_valid_from_2019_valid_until_sameday+=1

                elif(((res/ timedelta(days=30))*(-1)) < 1):
                    count_alienvault_iot_valid_from_2019_valid_until_samemonth+=1

                elif(((res/ timedelta(days=365))*(-1)) < 1):
                    count_alienvault_iot_valid_from_2019_valid_until_sameyear+=1

                else:
                    count_alienvault_iot_valid_from_2019_anotheryear+=1

            elif(anio_validfrom_alienvault_iot >= 2018):
                count_alienvault_iot_entries+=1
                count_alienvault_iot_valid_from_2018+=1
                if(((res/ timedelta(days=1))*(-1)) < 1):
                    count_alienvault_iot_valid_from_2018_valid_until_sameday+=1

                elif(((res/ timedelta(days=30))*(-1)) < 1):
                    count_alienvault_iot_valid_from_2018_valid_until_samemonth+=1

                elif(((res/ timedelta(days=365))*(-1)) < 1):
                    count_alienvault_iot_valid_from_2018_valid_until_sameyear+=1

                else:
                    count_alienvault_iot_valid_from_2018_anotheryear+=1        
                            
                    
print("***************************ESTADÍSTICAS INICIO VALIDEZ/FIN DE VALIDEZ DATE ALIENVAULT PARTE IOT***************************")
print("\n")                            
                
print("\n")
print(" DE UN TOTAL DE "+str(count_alienvault_iot_entries)+" OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ :\n") 
print("\n")
print("   - LAS ESTADISTICAS DE INICIO DE VALIDEZ SON LAS SIGUIENTES:  \n")
print("      -    EN  "+str(count_alienvault_iot_valid_from_2023)+" OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ EL COMIENZO DE VALIDEZ ES 2023. LAS ESTADÍSTICAS DE FIN DE VALIDEZ SON LAS SIGUIENTES :  \n")
print("\n")
print("            -    EN  "+str(count_alienvault_iot_valid_from_2023_valid_until_sameday)+" OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ VALIDOS DESDE 2023, LA VALIDEZ FINALIZA ESE MISMO DÍA ")
print("            -    EN  "+str(count_alienvault_iot_valid_from_2023_valid_until_samemonth)+" OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ VALIDOS DESDE 2023, EL FIN DE PERIODO DE VALIDEZ ES ESE MISMO MES")
print("            -    EN  "+str(count_alienvault_iot_valid_from_2023_valid_until_sameyear)+" OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ VALIDOS DESDE 2023, EL FIN DE PERIODO DE VALIDEZ ES ESE MISMO AÑO ")
print("            -    EN  "+str(count_alienvault_iot_valid_from_2023_anotheryear)+" OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ VALIDOS DESDE 2023, EL FIN DE PERIODO DE VALIDEZ ES MÁS TARDE DE UN AÑO ")
print("\n")
print("      -    EN  "+str(count_alienvault_iot_valid_from_2022)+" OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ EL COMIENZO DE VALIDEZ ES 2022. LAS ESTADÍSTICAS DE FIN DE VALIDEZ SON LAS SIGUIENTES :  \n")
print("\n")
print("            -    EN  "+str(count_alienvault_iot_valid_from_2022_valid_until_sameday)+" OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ VALIDOS DESDE 2022, LA VALIDEZ FINALIZA ESE MISMO DÍA ")
print("            -    EN  "+str(count_alienvault_iot_valid_from_2022_valid_until_samemonth)+" OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ VALIDOS DESDE 2022, EL FIN DE PERIODO DE VALIDEZ ES ESE MISMO MES")
print("            -    EN  "+str(count_alienvault_iot_valid_from_2022_valid_until_sameyear)+" OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ VALIDOS DESDE 2022, EL FIN DE PERIODO DE VALIDEZ ES ESE MISMO AÑO ")
print("            -    EN  "+str(count_alienvault_iot_valid_from_2022_anotheryear)+" OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ VALIDOS DESDE 2022, EL FIN DE PERIODO DE VALIDEZ ES MÁS TARDE DE UN AÑO ")
print("\n")
print("      -    EN  "+str(count_alienvault_iot_valid_from_2021)+" OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ EL COMIENZO DE VALIDEZ ES 2021. LAS ESTADÍSTICAS DE FIN DE VALIDEZ SON LAS SIGUIENTES :  \n")
print("\n")
print("            -    EN  "+str(count_alienvault_iot_valid_from_2021_valid_until_sameday)+" OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ VALIDOS DESDE 2021, LA VALIDEZ FINALIZA ESE MISMO DÍA ")
print("            -    EN  "+str(count_alienvault_iot_valid_from_2021_valid_until_samemonth)+" OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ VALIDOS DESDE 2021, EL FIN DE PERIODO DE VALIDEZ ES ESE MISMO MES")
print("            -    EN  "+str(count_alienvault_iot_valid_from_2021_valid_until_sameyear)+" OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ VALIDOS DESDE 2021, EL FIN DE PERIODO DE VALIDEZ ES ESE MISMO AÑO ")
print("            -    EN  "+str(count_alienvault_iot_valid_from_2021_anotheryear)+" OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ VALIDOS DESDE 2021, EL FIN DE PERIODO DE VALIDEZ ES MÁS TARDE DE UN AÑO ")
print("\n")
print("      -    EN  "+str(count_alienvault_iot_valid_from_2020)+" OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ EL COMIENZO DE VALIDEZ ES 2020. LAS ESTADÍSTICAS DE FIN DE VALIDEZ SON LAS SIGUIENTES :  \n")
print("\n")
print("            -    EN  "+str(count_alienvault_iot_valid_from_2020_valid_until_sameday)+" OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ VALIDOS DESDE 2020, LA VALIDEZ FINALIZA ESE MISMO DÍA ")
print("            -    EN  "+str(count_alienvault_iot_valid_from_2020_valid_until_samemonth)+" OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ VALIDOS DESDE 2020, EL FIN DE PERIODO DE VALIDEZ ES ESE MISMO MES")
print("            -    EN  "+str(count_alienvault_iot_valid_from_2020_valid_until_sameyear)+" OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ VALIDOS DESDE 2020, EL FIN DE PERIODO DE VALIDEZ ES ESE MISMO AÑO ")
print("            -    EN  "+str(count_alienvault_iot_valid_from_2020_anotheryear)+" OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ VALIDOS DESDE 2020, EL FIN DE PERIODO DE VALIDEZ ES MÁS TARDE DE UN AÑO ")
print("\n")
print("      -    EN  "+str(count_alienvault_iot_valid_from_2019)+" OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ EL COMIENZO DE VALIDEZ ES 2019. LAS ESTADÍSTICAS DE FIN DE VALIDEZ SON LAS SIGUIENTES :  \n")
print("\n")
print("            -    EN  "+str(count_alienvault_iot_valid_from_2019_valid_until_sameday)+" OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ VALIDOS DESDE 2019, LA VALIDEZ FINALIZA ESE MISMO DÍA ")
print("            -    EN  "+str(count_alienvault_iot_valid_from_2019_valid_until_samemonth)+" OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ VALIDOS DESDE 2019, EL FIN DE PERIODO DE VALIDEZ ES ESE MISMO MES")
print("            -    EN  "+str(count_alienvault_iot_valid_from_2019_valid_until_sameyear)+" OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ VALIDOS DESDE 2019, EL FIN DE PERIODO DE VALIDEZ ES ESE MISMO AÑO ")
print("            -    EN  "+str(count_alienvault_iot_valid_from_2019_anotheryear)+" OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ VALIDOS DESDE 2019, EL FIN DE PERIODO DE VALIDEZ ES MÁS TARDE DE UN AÑO ")
print("\n")
print("      -    EN  "+str(count_alienvault_iot_valid_from_2018)+" OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ EL COMIENZO DE VALIDEZ ES 2018 O ANTERIOR. LAS ESTADÍSTICAS DE FIN DE VALIDEZ SON LAS SIGUIENTES :  \n")
print("\n")
print("            -    EN  "+str(count_alienvault_iot_valid_from_2018_valid_until_sameday)+" OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ VALIDOS DESDE 2018 O ANTERIORMENTE, LA VALIDEZ FINALIZA ESE MISMO DÍA ")
print("            -    EN  "+str(count_alienvault_iot_valid_from_2018_valid_until_samemonth)+" OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ VALIDOS DESDE 2018 O ANTERIORMENTE, EL FIN DE PERIODO DE VALIDEZ ES ESE MISMO MES")
print("            -    EN  "+str(count_alienvault_iot_valid_from_2018_valid_until_sameyear)+" OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ VALIDOS DESDE 2018 O ANTERIORMENTE, EL FIN DE PERIODO DE VALIDEZ ES ESE MISMO AÑO ")
print("            -    EN  "+str(count_alienvault_iot_valid_from_2018_anotheryear)+" OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ VALIDOS DESDE 2018 O ANTERIORMENTE, EL FIN DE PERIODO DE VALIDEZ ES MÁS TARDE DE UN AÑO ")
print("\n")








print("***************************PORCENTAJE INICIO VALIDEZ/FIN DE VALIDEZ DATE ALIENVAULT PARTE IOT***************************")
print("\n")                            
                
print("\n")
print(" DE UN TOTAL DE "+str(count_alienvault_iot_entries)+" OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ :\n") 
print("\n")
print("   - LOS PORCENTAJES DE INICIO DE VALIDEZ SON LOS SIGUIENTES:  \n")
if(count_alienvault_iot_valid_from_2023>0):
    print("      -    EN EL  "+str(float(((count_alienvault_iot_valid_from_2023*100)/count_alienvault_iot_entries)))+" % DE OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ EL COMIENZO DE VALIDEZ ES 2023. LOS PORCENTAJES DE FIN DE VALIDEZ SON LOS SIGUIENTES  :\n")
    print("\n")
    print("            -    EN EL  "+str(float(((count_alienvault_iot_valid_from_2023_valid_until_sameday*100)/count_alienvault_iot_valid_from_2023)))+" % DE OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ VALIDOS DESDE 2023, LA VALIDEZ FINALIZA ESE MISMO DÍA ")
    print("            -    EN EL  "+str(float(((count_alienvault_iot_valid_from_2023_valid_until_samemonth*100)/count_alienvault_iot_valid_from_2023)))+" % DE OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ VALIDOS DESDE 2023, LA VALIDEZ FINALIZA ESE MISMO MES")
    print("            -    EN EL  "+str(float(((count_alienvault_iot_valid_from_2023_valid_until_sameyear*100)/count_alienvault_iot_valid_from_2023)))+" % DE OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ VALIDOS DESDE 2023, LA VALIDEZ FINALIZA ESE MISMO AÑO ")
    print("            -    EN EL  "+str(float(((count_alienvault_iot_valid_from_2023_anotheryear*100)/count_alienvault_iot_valid_from_2023)))+" % DE OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ VALIDOS DESDE 2023, LA VALIDEZ FINALIZA MÁS TARDE DE UN AÑO ")
    print("\n")
if(count_alienvault_iot_valid_from_2022>0):
    print("      -    EN EL  "+str(float(((count_alienvault_iot_valid_from_2022*100)/count_alienvault_iot_entries)))+" % DE OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ EL COMIENZO DE VALIDEZ ES 2022. LOS PORCENTAJES DE FIN DE VALIDEZ SON LOS SIGUIENTES  :\n")
    print("\n")
    print("            -    EN EL  "+str(float(((count_alienvault_iot_valid_from_2022_valid_until_sameday*100)/count_alienvault_iot_valid_from_2022)))+" % DE OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ VALIDOS DESDE 2022, LA VALIDEZ FINALIZA ESE MISMO DÍA ")
    print("            -    EN EL  "+str(float(((count_alienvault_iot_valid_from_2022_valid_until_samemonth*100)/count_alienvault_iot_valid_from_2022)))+" % DE OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ VALIDOS DESDE 2022, LA VALIDEZ FINALIZA ESE MISMO MES")
    print("            -    EN EL  "+str(float(((count_alienvault_iot_valid_from_2022_valid_until_sameyear*100)/count_alienvault_iot_valid_from_2022)))+" % DE OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ VALIDOS DESDE 2022, LA VALIDEZ FINALIZA ESE MISMO AÑO ")
    print("            -    EN EL  "+str(float(((count_alienvault_iot_valid_from_2022_anotheryear*100)/count_alienvault_iot_valid_from_2022)))+" % DE OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ VALIDOS DESDE 2022, LA VALIDEZ FINALIZA MÁS TARDE DE UN AÑO ")
    print("\n")
if(count_alienvault_iot_valid_from_2021>0):
    print("      -    EN EL  "+str(float(((count_alienvault_iot_valid_from_2021*100)/count_alienvault_iot_entries)))+" % DE OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ EL COMIENZO DE VALIDEZ ES 2021. LOS PORCENTAJES DE FIN DE VALIDEZ SON LOS SIGUIENTES  :\n")
    print("\n")
    print("            -    EN EL  "+str(float(((count_alienvault_iot_valid_from_2021_valid_until_sameday*100)/count_alienvault_iot_valid_from_2021)))+" % DE OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ VALIDOS DESDE 2021, LA VALIDEZ FINALIZA ESE MISMO DÍA ")
    print("            -    EN EL  "+str(float(((count_alienvault_iot_valid_from_2021_valid_until_samemonth*100)/count_alienvault_iot_valid_from_2021)))+" % DE OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ VALIDOS DESDE 2021, LA VALIDEZ FINALIZA ESE MISMO MES")
    print("            -    EN EL  "+str(float(((count_alienvault_iot_valid_from_2021_valid_until_sameyear*100)/count_alienvault_iot_valid_from_2021)))+" % DE OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ VALIDOS DESDE 2021, LA VALIDEZ FINALIZA ESE MISMO AÑO ")
    print("            -    EN EL  "+str(float(((count_alienvault_iot_valid_from_2021_anotheryear*100)/count_alienvault_iot_valid_from_2021)))+" % DE OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ VALIDOS DESDE 2021, LA VALIDEZ FINALIZA MÁS TARDE DE UN AÑO ")
    print("\n")
if(count_alienvault_iot_valid_from_2020>0):
    print("      -    EN EL  "+str(float(((count_alienvault_iot_valid_from_2020*100)/count_alienvault_iot_entries)))+" % DE OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ EL COMIENZO DE VALIDEZ ES 2020. LOS PORCENTAJES DE FIN DE VALIDEZ SON LOS SIGUIENTES  :\n")
    print("\n")
    print("            -    EN EL  "+str(float(((count_alienvault_iot_valid_from_2020_valid_until_sameday*100)/count_alienvault_iot_valid_from_2020)))+" % DE OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ VALIDOS DESDE 2020, LA VALIDEZ FINALIZA ESE MISMO DÍA ")
    print("            -    EN EL  "+str(float(((count_alienvault_iot_valid_from_2020_valid_until_samemonth*100)/count_alienvault_iot_valid_from_2020)))+" % DE OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ VALIDOS DESDE 2020, LA VALIDEZ FINALIZA ESE MISMO MES")
    print("            -    EN EL  "+str(float(((count_alienvault_iot_valid_from_2020_valid_until_sameyear*100)/count_alienvault_iot_valid_from_2020)))+" % DE OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ VALIDOS DESDE 2020, LA VALIDEZ FINALIZA ESE MISMO AÑO ")
    print("            -    EN EL  "+str(float(((count_alienvault_iot_valid_from_2020_anotheryear*100)/count_alienvault_iot_valid_from_2020)))+" % DE OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ VALIDOS DESDE 2020, LA VALIDEZ FINALIZA MÁS TARDE DE UN AÑO ")
    print("\n")
if(count_alienvault_iot_valid_from_2019>0):
    print("      -    EN EL  "+str(float(((count_alienvault_iot_valid_from_2019*100)/count_alienvault_iot_entries)))+" % DE OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ EL COMIENZO DE VALIDEZ ES 2019. LOS PORCENTAJES DE FIN DE VALIDEZ SON LOS SIGUIENTES  :\n")
    print("\n")
    print("            -    EN EL  "+str(float(((count_alienvault_iot_valid_from_2019_valid_until_sameday*100)/count_alienvault_iot_valid_from_2019)))+" % DE OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ VALIDOS DESDE 2019, LA VALIDEZ FINALIZA ESE MISMO DÍA ")
    print("            -    EN EL  "+str(float(((count_alienvault_iot_valid_from_2019_valid_until_samemonth*100)/count_alienvault_iot_valid_from_2019)))+" % DE OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ VALIDOS DESDE 2019, LA VALIDEZ FINALIZA ESE MISMO MES")
    print("            -    EN EL  "+str(float(((count_alienvault_iot_valid_from_2019_valid_until_sameyear*100)/count_alienvault_iot_valid_from_2019)))+" % DE OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ VALIDOS DESDE 2019, LA VALIDEZ FINALIZA ESE MISMO AÑO ")
    print("            -    EN EL  "+str(float(((count_alienvault_iot_valid_from_2019_anotheryear*100)/count_alienvault_iot_valid_from_2019)))+" % DE OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ VALIDOS DESDE 2019, LA VALIDEZ FINALIZA MÁS TARDE DE UN AÑO ")
    print("\n")
if(count_alienvault_iot_valid_from_2018>0):
    print("      -    EN EL  "+str(float(((count_alienvault_iot_valid_from_2018*100)/count_alienvault_iot_entries)))+" % DE OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ EL COMIENZO DE VALIDEZ ES 2018 O ANTERIOR. LOS PORCENTAJES DE FIN DE VALIDEZ SON LOS SIGUIENTES  :\n")
    print("\n")
    print("            -    EN EL  "+str(float(((count_alienvault_iot_valid_from_2018_valid_until_sameday*100)/count_alienvault_iot_valid_from_2018)))+" % DE OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ VALIDOS DESDE 2018 O ANTERIORMENTE, LA VALIDEZ FINALIZA ESE MISMO DÍA ")
    print("            -    EN EL  "+str(float(((count_alienvault_iot_valid_from_2018_valid_until_samemonth*100)/count_alienvault_iot_valid_from_2018)))+" % DE OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ VALIDOS DESDE 2018 O ANTERIORMENTE, LA VALIDEZ FINALIZA ESE MISMO MES")
    print("            -    EN EL  "+str(float(((count_alienvault_iot_valid_from_2018_valid_until_sameyear*100)/count_alienvault_iot_valid_from_2018)))+" % DE OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ VALIDOS DESDE 2018 O ANTERIORMENTE, LA VALIDEZ FINALIZA ESE MISMO AÑO ")
    print("            -    EN EL  "+str(float(((count_alienvault_iot_valid_from_2018_anotheryear*100)/count_alienvault_iot_valid_from_2018)))+" % DE OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ VALIDOS DESDE 2018 O ANTERIORMENTE, LA VALIDEZ FINALIZA MÁS TARDE DE UN AÑO ")
    print("\n")









#Abro los ficheros con los que voy a tratar




df_alienvault_sh = pd.read_excel('alienvault_smart_home_2023.xlsx')
#Variable donde almaceno el contador total de entradas
count_alienvault_sh_entries=0
#Variable donde almaceno el contador total de entradas validas desde un anio especifico
count_alienvault_sh_valid_from_2023=0
#Variable donde almaceno el tiempo de validez de una entrada dado un anio especifico
count_alienvault_sh_valid_from_2023_valid_until_sameday=0
count_alienvault_sh_valid_from_2023_valid_until_samemonth=0
count_alienvault_sh_valid_from_2023_valid_until_sameyear=0
count_alienvault_sh_valid_from_2023_anotheryear=0

count_alienvault_sh_valid_from_2022=0
count_alienvault_sh_valid_from_2022_valid_until_sameday=0
count_alienvault_sh_valid_from_2022_valid_until_samemonth=0
count_alienvault_sh_valid_from_2022_valid_until_sameyear=0
count_alienvault_sh_valid_from_2022_anotheryear=0

count_alienvault_sh_valid_from_2021=0
count_alienvault_sh_valid_from_2021_valid_until_sameday=0
count_alienvault_sh_valid_from_2021_valid_until_samemonth=0
count_alienvault_sh_valid_from_2021_valid_until_sameyear=0
count_alienvault_sh_valid_from_2021_anotheryear=0

count_alienvault_sh_valid_from_2020=0
count_alienvault_sh_valid_from_2020_valid_until_sameday=0
count_alienvault_sh_valid_from_2020_valid_until_samemonth=0
count_alienvault_sh_valid_from_2020_valid_until_sameyear=0
count_alienvault_sh_valid_from_2020_anotheryear=0

count_alienvault_sh_valid_from_2019=0
count_alienvault_sh_valid_from_2019_valid_until_sameday=0
count_alienvault_sh_valid_from_2019_valid_until_samemonth=0
count_alienvault_sh_valid_from_2019_valid_until_sameyear=0
count_alienvault_sh_valid_from_2019_anotheryear=0

count_alienvault_sh_valid_from_2018=0
count_alienvault_sh_valid_from_2018_valid_until_sameday=0
count_alienvault_sh_valid_from_2018_valid_until_samemonth=0
count_alienvault_sh_valid_from_2018_valid_until_sameyear=0
count_alienvault_sh_valid_from_2018_anotheryear=0


#Comprobamos el comienzo de validez
for r in range(0,len(df_alienvault_sh["valid_from"])):
    #Si existen varios valores de INICIO VALIDEZ en una misma fila
    if('[' in df_alienvault_sh["valid_from"][r]):
        #Obtengo los valores de INICIO VALIDEZ y FIN DE VALIDEZ de la fila actual
        aux=df_alienvault_sh["valid_from"][r].split(",")
        auxx=df_alienvault_sh["valid_until"][r].split(",")
        for l in range(0,len(aux)):
            if((len(aux)>0) and (len(auxx) == len(aux))):
                #Obtengo el valor actual de INICIO VALIDEZ y FIN DE VALIDEZ
                aux_str=aux[l].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","").replace("T"," ")
                auxx_str=auxx[l].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","").replace("T"," ")
                #Compruebo que los valores no sean nulos
                if((aux_str!='NONE' and auxx_str!='NONE') and ('Z' in aux_str and 'Z' in auxx_str)):
                    aux2=aux_str.split(".")
                    validfrom = datetime.strptime(aux2[0], '%Y-%m-%d %H:%M:%S')
                    aux22=auxx_str.split(".")
                    validuntil = datetime.strptime(aux22[0], '%Y-%m-%d %H:%M:%S')
                    #Obtengo ambos valores y calculo su diferencia
                    res=validfrom-validuntil
                    #Obtengo el anio de INICIO VALIDEZ
                    str_anio_validfrom_alienvault_sh=aux_str.split("-")
                    anio_validfrom_alienvault_sh=int(str_anio_validfrom_alienvault_sh[0])
                    #Compruebo el anio desde el que es valido la entrada
                    if(anio_validfrom_alienvault_sh >= 2023):
                        count_alienvault_sh_entries+=1
                        count_alienvault_sh_valid_from_2023+=1
                        #Compruebo si la diferencia entre ambas es menor de un dia
                        if(((res/ timedelta(days=1))*(-1)) < 1):
                            count_alienvault_sh_valid_from_2023_valid_until_sameday+=1
                        #Compruebo si la diferencia entre ambas es menor de un mes    
                        elif(((res/ timedelta(days=30))*(-1)) < 1):
                            count_alienvault_sh_valid_from_2023_valid_until_samemonth+=1
                         #Compruebo si la diferencia entre ambas es menor de un anio  
                        elif(((res/ timedelta(days=365))*(-1)) < 1):
                            count_alienvault_sh_valid_from_2023_valid_until_sameyear+=1
                            
                        else:
                            #Compruebo si la diferencia entre ambas es mayor de un anio
                            count_alienvault_sh_valid_from_2023_anotheryear+=1
                            
                    elif(anio_validfrom_alienvault_sh >= 2022):
                        count_alienvault_sh_entries+=1
                        count_alienvault_sh_valid_from_2022+=1
                        if(((res/ timedelta(days=1))*(-1)) < 1):
                            count_alienvault_sh_valid_from_2022_valid_until_sameday+=1
                            
                        elif(((res/ timedelta(days=30))*(-1)) < 1):
                            count_alienvault_sh_valid_from_2022_valid_until_samemonth+=1
                            
                        elif(((res/ timedelta(days=365))*(-1)) < 1):
                            count_alienvault_sh_valid_from_2022_valid_until_sameyear+=1
                            
                        else:
                            count_alienvault_sh_valid_from_2022_anotheryear+=1
                            
                    elif(anio_validfrom_alienvault_sh >= 2021):
                        count_alienvault_sh_entries+=1
                        count_alienvault_sh_valid_from_2021+=1
                        if(((res/ timedelta(days=1))*(-1)) < 1):
                            count_alienvault_sh_valid_from_2021_valid_until_sameday+=1
                            
                        elif(((res/ timedelta(days=30))*(-1)) < 1):
                            count_alienvault_sh_valid_from_2021_valid_until_samemonth+=1
                            
                        elif(((res/ timedelta(days=365))*(-1)) < 1):
                            count_alienvault_sh_valid_from_2021_valid_until_sameyear+=1
                            
                        else:
                            count_alienvault_sh_valid_from_2021_anotheryear+=1
                            
                    elif(anio_validfrom_alienvault_sh >= 2020):
                        count_alienvault_sh_entries+=1
                        count_alienvault_sh_valid_from_2020+=1
                        if(((res/ timedelta(days=1))*(-1)) < 1):
                            count_alienvault_sh_valid_from_2020_valid_until_sameday+=1
                            
                        elif(((res/ timedelta(days=30))*(-1)) < 1):
                            count_alienvault_sh_valid_from_2020_valid_until_samemonth+=1
                            
                        elif(((res/ timedelta(days=365))*(-1)) < 1):
                            count_alienvault_sh_valid_from_2020_valid_until_sameyear+=1
                            
                        else:
                            count_alienvault_sh_valid_from_2020_anotheryear+=1
                            
                    elif(anio_validfrom_alienvault_sh >= 2019):
                        count_alienvault_sh_entries+=1
                        count_alienvault_sh_valid_from_2019+=1
                        if(((res/ timedelta(days=1))*(-1)) < 1):
                            count_alienvault_sh_valid_from_2019_valid_until_sameday+=1
                            
                        elif(((res/ timedelta(days=30))*(-1)) < 1):
                            count_alienvault_sh_valid_from_2019_valid_until_samemonth+=1
                            
                        elif(((res/ timedelta(days=365))*(-1)) < 1):
                            count_alienvault_sh_valid_from_2019_valid_until_sameyear+=1
                            
                        else:
                            count_alienvault_sh_valid_from_2019_anotheryear+=1
                            
                    elif(anio_validfrom_alienvault_sh >= 2018):
                        count_alienvault_sh_entries+=1
                        count_alienvault_sh_valid_from_2018+=1
                        if(((res/ timedelta(days=1))*(-1)) < 1):
                            count_alienvault_sh_valid_from_2018_valid_until_sameday+=1
                            
                        elif(((res/ timedelta(days=30))*(-1)) < 1):
                            count_alienvault_sh_valid_from_2018_valid_until_samemonth+=1
                            
                        elif(((res/ timedelta(days=365))*(-1)) < 1):
                            count_alienvault_sh_valid_from_2018_valid_until_sameyear+=1
                            
                        else:
                            count_alienvault_sh_valid_from_2018_anotheryear+=1
                            
    else:
        #Si existe un unico valor de INICIO VALIDEZ y FIN DE VALIDEZ para fila actual
        aux_strr=df_alienvault_sh["valid_from"][r].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","").replace("T"," ")
        auxx_strr=df_alienvault_sh["valid_until"][r].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","").replace("T"," ")
        if((aux_strr!='NONE' and auxx_strr!='NONE') and ('Z' in aux_strr and 'Z' in auxx_strr)):
            aux22=aux_strr.split(".")
            validfrom = datetime.strptime(aux22[0], '%Y-%m-%d %H:%M:%S')
            aux222=auxx_strr.split(".")
            validuntil = datetime.strptime(aux222[0], '%Y-%m-%d %H:%M:%S')
            res=validfrom-validuntil
            str_anio_validfrom_alienvault_sh=auxx_strr.split("-")
            anio_validfrom_alienvault_sh=int(str_anio_validfrom_alienvault_sh[0]) 
            #Compruebo el anio desde el que es valida la entrada, una vez hemos calculado la diferencia anteriormente
            if(anio_validfrom_alienvault_sh >= 2023):
                count_alienvault_sh_entries+=1
                count_alienvault_sh_valid_from_2023+=1
                if(((res/ timedelta(days=1))*(-1)) < 1):
                    count_alienvault_sh_valid_from_2023_valid_until_sameday+=1

                elif(((res/ timedelta(days=30))*(-1)) < 1):
                    count_alienvault_sh_valid_from_2023_valid_until_samemonth+=1

                elif(((res/ timedelta(days=365))*(-1)) < 1):
                    count_alienvault_sh_valid_from_2023_valid_until_sameyear+=1

                else:
                    count_alienvault_sh_valid_from_2023_anotheryear+=1

            elif(anio_validfrom_alienvault_sh >= 2022):
                count_alienvault_sh_entries+=1
                count_alienvault_sh_valid_from_2022+=1
                if(((res/ timedelta(days=1))*(-1)) < 1):
                    count_alienvault_sh_valid_from_2022_valid_until_sameday+=1

                elif(((res/ timedelta(days=30))*(-1)) < 1):
                    count_alienvault_sh_valid_from_2022_valid_until_samemonth+=1

                elif(((res/ timedelta(days=365))*(-1)) < 1):
                    count_alienvault_sh_valid_from_2022_valid_until_sameyear+=1

                else:
                    count_alienvault_sh_valid_from_2022_anotheryear+=1

            elif(anio_validfrom_alienvault_sh >= 2021):
                count_alienvault_sh_entries+=1
                count_alienvault_sh_valid_from_2021+=1
                if(((res/ timedelta(days=1))*(-1)) < 1):
                    count_alienvault_sh_valid_from_2021_valid_until_sameday+=1

                elif(((res/ timedelta(days=30))*(-1)) < 1):
                    count_alienvault_sh_valid_from_2021_valid_until_samemonth+=1

                elif(((res/ timedelta(days=365))*(-1)) < 1):
                    count_alienvault_sh_valid_from_2021_valid_until_sameyear+=1

                else:
                    count_alienvault_sh_valid_from_2021_anotheryear+=1

            elif(anio_validfrom_alienvault_sh >= 2020):
                count_alienvault_sh_entries+=1
                count_alienvault_sh_valid_from_2020+=1
                if(((res/ timedelta(days=1))*(-1)) < 1):
                    count_alienvault_sh_valid_from_2020_valid_until_sameday+=1

                elif(((res/ timedelta(days=30))*(-1)) < 1):
                    count_alienvault_sh_valid_from_2020_valid_until_samemonth+=1

                elif(((res/ timedelta(days=365))*(-1)) < 1):
                    count_alienvault_sh_valid_from_2020_valid_until_sameyear+=1

                else:
                    count_alienvault_sh_valid_from_2020_anotheryear+=1

            elif(anio_validfrom_alienvault_sh >= 2019):
                count_alienvault_sh_entries+=1
                count_alienvault_sh_valid_from_2019+=1
                if(((res/ timedelta(days=1))*(-1)) < 1):
                    count_alienvault_sh_valid_from_2019_valid_until_sameday+=1

                elif(((res/ timedelta(days=30))*(-1)) < 1):
                    count_alienvault_sh_valid_from_2019_valid_until_samemonth+=1

                elif(((res/ timedelta(days=365))*(-1)) < 1):
                    count_alienvault_sh_valid_from_2019_valid_until_sameyear+=1

                else:
                    count_alienvault_sh_valid_from_2019_anotheryear+=1

            elif(anio_validfrom_alienvault_sh >= 2018):
                count_alienvault_sh_entries+=1
                count_alienvault_sh_valid_from_2018+=1
                if(((res/ timedelta(days=1))*(-1)) < 1):
                    count_alienvault_sh_valid_from_2018_valid_until_sameday+=1

                elif(((res/ timedelta(days=30))*(-1)) < 1):
                    count_alienvault_sh_valid_from_2018_valid_until_samemonth+=1

                elif(((res/ timedelta(days=365))*(-1)) < 1):
                    count_alienvault_sh_valid_from_2018_valid_until_sameyear+=1

                else:
                    count_alienvault_sh_valid_from_2018_anotheryear+=1        
                            
                    
print("***************************ESTADÍSTICAS INICIO VALIDEZ/FIN DE VALIDEZ DATE ALIENVAULT PARTE SMART HOME***************************")
print("\n")                            
                
print("\n")
print(" DE UN TOTAL DE "+str(count_alienvault_sh_entries)+" OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ :\n") 
print("\n")
print("   - LAS ESTADISTICAS DE INICIO DE VALIDEZ SON LAS SIGUIENTES:  \n")
print("      -    EN  "+str(count_alienvault_sh_valid_from_2023)+" OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ EL COMIENZO DE VALIDEZ ES 2023. LAS ESTADÍSTICAS DE FIN DE VALIDEZ SON LAS SIGUIENTES :  \n")
print("\n")
print("            -    EN  "+str(count_alienvault_sh_valid_from_2023_valid_until_sameday)+" OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ VALIDOS DESDE 2023, LA VALIDEZ FINALIZA ESE MISMO DÍA ")
print("            -    EN  "+str(count_alienvault_sh_valid_from_2023_valid_until_samemonth)+" OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ VALIDOS DESDE 2023, EL FIN DE PERIODO DE VALIDEZ ES ESE MISMO MES")
print("            -    EN  "+str(count_alienvault_sh_valid_from_2023_valid_until_sameyear)+" OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ VALIDOS DESDE 2023, EL FIN DE PERIODO DE VALIDEZ ES ESE MISMO AÑO ")
print("            -    EN  "+str(count_alienvault_sh_valid_from_2023_anotheryear)+" OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ VALIDOS DESDE 2023, EL FIN DE PERIODO DE VALIDEZ ES MÁS TARDE DE UN AÑO ")
print("\n")
print("      -    EN  "+str(count_alienvault_sh_valid_from_2022)+" OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ EL COMIENZO DE VALIDEZ ES 2022. LAS ESTADÍSTICAS DE FIN DE VALIDEZ SON LAS SIGUIENTES :  \n")
print("\n")
print("            -    EN  "+str(count_alienvault_sh_valid_from_2022_valid_until_sameday)+" OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ VALIDOS DESDE 2022, LA VALIDEZ FINALIZA ESE MISMO DÍA ")
print("            -    EN  "+str(count_alienvault_sh_valid_from_2022_valid_until_samemonth)+" OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ VALIDOS DESDE 2022, EL FIN DE PERIODO DE VALIDEZ ES ESE MISMO MES")
print("            -    EN  "+str(count_alienvault_sh_valid_from_2022_valid_until_sameyear)+" OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ VALIDOS DESDE 2022, EL FIN DE PERIODO DE VALIDEZ ES ESE MISMO AÑO ")
print("            -    EN  "+str(count_alienvault_sh_valid_from_2022_anotheryear)+" OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ VALIDOS DESDE 2022, EL FIN DE PERIODO DE VALIDEZ ES MÁS TARDE DE UN AÑO ")
print("\n")
print("      -    EN  "+str(count_alienvault_sh_valid_from_2021)+" OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ EL COMIENZO DE VALIDEZ ES 2021. LAS ESTADÍSTICAS DE FIN DE VALIDEZ SON LAS SIGUIENTES :  \n")
print("\n")
print("            -    EN  "+str(count_alienvault_sh_valid_from_2021_valid_until_sameday)+" OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ VALIDOS DESDE 2021, LA VALIDEZ FINALIZA ESE MISMO DÍA ")
print("            -    EN  "+str(count_alienvault_sh_valid_from_2021_valid_until_samemonth)+" OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ VALIDOS DESDE 2021, EL FIN DE PERIODO DE VALIDEZ ES ESE MISMO MES")
print("            -    EN  "+str(count_alienvault_sh_valid_from_2021_valid_until_sameyear)+" OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ VALIDOS DESDE 2021, EL FIN DE PERIODO DE VALIDEZ ES ESE MISMO AÑO ")
print("            -    EN  "+str(count_alienvault_sh_valid_from_2021_anotheryear)+" OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ VALIDOS DESDE 2021, EL FIN DE PERIODO DE VALIDEZ ES MÁS TARDE DE UN AÑO ")
print("\n")
print("      -    EN  "+str(count_alienvault_sh_valid_from_2020)+" OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ EL COMIENZO DE VALIDEZ ES 2020. LAS ESTADÍSTICAS DE FIN DE VALIDEZ SON LAS SIGUIENTES :  \n")
print("\n")
print("            -    EN  "+str(count_alienvault_sh_valid_from_2020_valid_until_sameday)+" OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ VALIDOS DESDE 2020, LA VALIDEZ FINALIZA ESE MISMO DÍA ")
print("            -    EN  "+str(count_alienvault_sh_valid_from_2020_valid_until_samemonth)+" OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ VALIDOS DESDE 2020, EL FIN DE PERIODO DE VALIDEZ ES ESE MISMO MES")
print("            -    EN  "+str(count_alienvault_sh_valid_from_2020_valid_until_sameyear)+" OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ VALIDOS DESDE 2020, EL FIN DE PERIODO DE VALIDEZ ES ESE MISMO AÑO ")
print("            -    EN  "+str(count_alienvault_sh_valid_from_2020_anotheryear)+" OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ VALIDOS DESDE 2020, EL FIN DE PERIODO DE VALIDEZ ES MÁS TARDE DE UN AÑO ")
print("\n")
print("      -    EN  "+str(count_alienvault_sh_valid_from_2019)+" OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ EL COMIENZO DE VALIDEZ ES 2019. LAS ESTADÍSTICAS DE FIN DE VALIDEZ SON LAS SIGUIENTES :  \n")
print("\n")
print("            -    EN  "+str(count_alienvault_sh_valid_from_2019_valid_until_sameday)+" OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ VALIDOS DESDE 2019, LA VALIDEZ FINALIZA ESE MISMO DÍA ")
print("            -    EN  "+str(count_alienvault_sh_valid_from_2019_valid_until_samemonth)+" OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ VALIDOS DESDE 2019, EL FIN DE PERIODO DE VALIDEZ ES ESE MISMO MES")
print("            -    EN  "+str(count_alienvault_sh_valid_from_2019_valid_until_sameyear)+" OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ VALIDOS DESDE 2019, EL FIN DE PERIODO DE VALIDEZ ES ESE MISMO AÑO ")
print("            -    EN  "+str(count_alienvault_sh_valid_from_2019_anotheryear)+" OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ VALIDOS DESDE 2019, EL FIN DE PERIODO DE VALIDEZ ES MÁS TARDE DE UN AÑO ")
print("\n")
print("      -    EN  "+str(count_alienvault_sh_valid_from_2018)+" OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ EL COMIENZO DE VALIDEZ ES 2018 O ANTERIOR. LAS ESTADÍSTICAS DE FIN DE VALIDEZ SON LAS SIGUIENTES :  \n")
print("\n")
print("            -    EN  "+str(count_alienvault_sh_valid_from_2018_valid_until_sameday)+" OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ VALIDOS DESDE 2018 O ANTERIORMENTE, LA VALIDEZ FINALIZA ESE MISMO DÍA ")
print("            -    EN  "+str(count_alienvault_sh_valid_from_2018_valid_until_samemonth)+" OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ VALIDOS DESDE 2018 O ANTERIORMENTE, EL FIN DE PERIODO DE VALIDEZ ES ESE MISMO MES")
print("            -    EN  "+str(count_alienvault_sh_valid_from_2018_valid_until_sameyear)+" OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ VALIDOS DESDE 2018 O ANTERIORMENTE, EL FIN DE PERIODO DE VALIDEZ ES ESE MISMO AÑO ")
print("            -    EN  "+str(count_alienvault_sh_valid_from_2018_anotheryear)+" OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ VALIDOS DESDE 2018 O ANTERIORMENTE, EL FIN DE PERIODO DE VALIDEZ ES MÁS TARDE DE UN AÑO ")
print("\n")








print("***************************PORCENTAJE INICIO VALIDEZ/FIN DE VALIDEZ DATE ALIENVAULT PARTE SMART HOME***************************")
print("\n")                            
                
print("\n")
print(" DE UN TOTAL DE "+str(count_alienvault_sh_entries)+" OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ :\n") 
print("\n")
print("   - LOS PORCENTAJES DE INICIO DE VALIDEZ SON LOS SIGUIENTES:  \n")
if(count_alienvault_sh_valid_from_2023>0):
    print("      -    EN EL  "+str(float(((count_alienvault_sh_valid_from_2023*100)/count_alienvault_sh_entries)))+" % DE OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ EL COMIENZO DE VALIDEZ ES 2023. LOS PORCENTAJES DE FIN DE VALIDEZ SON LOS SIGUIENTES  :\n")
    print("\n")
    print("            -    EN EL  "+str(float(((count_alienvault_sh_valid_from_2023_valid_until_sameday*100)/count_alienvault_sh_valid_from_2023)))+" % DE OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ VALIDOS DESDE 2023, LA VALIDEZ FINALIZA ESE MISMO DÍA ")
    print("            -    EN EL  "+str(float(((count_alienvault_sh_valid_from_2023_valid_until_samemonth*100)/count_alienvault_sh_valid_from_2023)))+" % DE OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ VALIDOS DESDE 2023, LA VALIDEZ FINALIZA ESE MISMO MES")
    print("            -    EN EL  "+str(float(((count_alienvault_sh_valid_from_2023_valid_until_sameyear*100)/count_alienvault_sh_valid_from_2023)))+" % DE OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ VALIDOS DESDE 2023, LA VALIDEZ FINALIZA ESE MISMO AÑO ")
    print("            -    EN EL  "+str(float(((count_alienvault_sh_valid_from_2023_anotheryear*100)/count_alienvault_sh_valid_from_2023)))+" % DE OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ VALIDOS DESDE 2023, LA VALIDEZ FINALIZA MÁS TARDE DE UN AÑO ")
    print("\n")
if(count_alienvault_sh_valid_from_2022>0):
    print("      -    EN EL  "+str(float(((count_alienvault_sh_valid_from_2022*100)/count_alienvault_sh_entries)))+" % DE OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ EL COMIENZO DE VALIDEZ ES 2022. LOS PORCENTAJES DE FIN DE VALIDEZ SON LOS SIGUIENTES  :\n")
    print("\n")
    print("            -    EN EL  "+str(float(((count_alienvault_sh_valid_from_2022_valid_until_sameday*100)/count_alienvault_sh_valid_from_2022)))+" % DE OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ VALIDOS DESDE 2022, LA VALIDEZ FINALIZA ESE MISMO DÍA ")
    print("            -    EN EL  "+str(float(((count_alienvault_sh_valid_from_2022_valid_until_samemonth*100)/count_alienvault_sh_valid_from_2022)))+" % DE OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ VALIDOS DESDE 2022, LA VALIDEZ FINALIZA ESE MISMO MES")
    print("            -    EN EL  "+str(float(((count_alienvault_sh_valid_from_2022_valid_until_sameyear*100)/count_alienvault_sh_valid_from_2022)))+" % DE OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ VALIDOS DESDE 2022, LA VALIDEZ FINALIZA ESE MISMO AÑO ")
    print("            -    EN EL  "+str(float(((count_alienvault_sh_valid_from_2022_anotheryear*100)/count_alienvault_sh_valid_from_2022)))+" % DE OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ VALIDOS DESDE 2022, LA VALIDEZ FINALIZA MÁS TARDE DE UN AÑO ")
    print("\n")
if(count_alienvault_sh_valid_from_2021>0):
    print("      -    EN EL  "+str(float(((count_alienvault_sh_valid_from_2021*100)/count_alienvault_sh_entries)))+" % DE OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ EL COMIENZO DE VALIDEZ ES 2021. LOS PORCENTAJES DE FIN DE VALIDEZ SON LOS SIGUIENTES  :\n")
    print("\n")
    print("            -    EN EL  "+str(float(((count_alienvault_sh_valid_from_2021_valid_until_sameday*100)/count_alienvault_sh_valid_from_2021)))+" % DE OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ VALIDOS DESDE 2021, LA VALIDEZ FINALIZA ESE MISMO DÍA ")
    print("            -    EN EL  "+str(float(((count_alienvault_sh_valid_from_2021_valid_until_samemonth*100)/count_alienvault_sh_valid_from_2021)))+" % DE OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ VALIDOS DESDE 2021, LA VALIDEZ FINALIZA ESE MISMO MES")
    print("            -    EN EL  "+str(float(((count_alienvault_sh_valid_from_2021_valid_until_sameyear*100)/count_alienvault_sh_valid_from_2021)))+" % DE OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ VALIDOS DESDE 2021, LA VALIDEZ FINALIZA ESE MISMO AÑO ")
    print("            -    EN EL  "+str(float(((count_alienvault_sh_valid_from_2021_anotheryear*100)/count_alienvault_sh_valid_from_2021)))+" % DE OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ VALIDOS DESDE 2021, LA VALIDEZ FINALIZA MÁS TARDE DE UN AÑO ")
    print("\n")
if(count_alienvault_sh_valid_from_2020>0):
    print("      -    EN EL  "+str(float(((count_alienvault_sh_valid_from_2020*100)/count_alienvault_sh_entries)))+" % DE OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ EL COMIENZO DE VALIDEZ ES 2020. LOS PORCENTAJES DE FIN DE VALIDEZ SON LOS SIGUIENTES  :\n")
    print("\n")
    print("            -    EN EL  "+str(float(((count_alienvault_sh_valid_from_2020_valid_until_sameday*100)/count_alienvault_sh_valid_from_2020)))+" % DE OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ VALIDOS DESDE 2020, LA VALIDEZ FINALIZA ESE MISMO DÍA ")
    print("            -    EN EL  "+str(float(((count_alienvault_sh_valid_from_2020_valid_until_samemonth*100)/count_alienvault_sh_valid_from_2020)))+" % DE OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ VALIDOS DESDE 2020, LA VALIDEZ FINALIZA ESE MISMO MES")
    print("            -    EN EL  "+str(float(((count_alienvault_sh_valid_from_2020_valid_until_sameyear*100)/count_alienvault_sh_valid_from_2020)))+" % DE OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ VALIDOS DESDE 2020, LA VALIDEZ FINALIZA ESE MISMO AÑO ")
    print("            -    EN EL  "+str(float(((count_alienvault_sh_valid_from_2020_anotheryear*100)/count_alienvault_sh_valid_from_2020)))+" % DE OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ VALIDOS DESDE 2020, LA VALIDEZ FINALIZA MÁS TARDE DE UN AÑO ")
    print("\n")
if(count_alienvault_sh_valid_from_2019>0):
    print("      -    EN EL  "+str(float(((count_alienvault_sh_valid_from_2019*100)/count_alienvault_sh_entries)))+" % DE OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ EL COMIENZO DE VALIDEZ ES 2019. LOS PORCENTAJES DE FIN DE VALIDEZ SON LOS SIGUIENTES  :\n")
    print("\n")
    print("            -    EN EL  "+str(float(((count_alienvault_sh_valid_from_2019_valid_until_sameday*100)/count_alienvault_sh_valid_from_2019)))+" % DE OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ VALIDOS DESDE 2019, LA VALIDEZ FINALIZA ESE MISMO DÍA ")
    print("            -    EN EL  "+str(float(((count_alienvault_sh_valid_from_2019_valid_until_samemonth*100)/count_alienvault_sh_valid_from_2019)))+" % DE OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ VALIDOS DESDE 2019, LA VALIDEZ FINALIZA ESE MISMO MES")
    print("            -    EN EL  "+str(float(((count_alienvault_sh_valid_from_2019_valid_until_sameyear*100)/count_alienvault_sh_valid_from_2019)))+" % DE OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ VALIDOS DESDE 2019, LA VALIDEZ FINALIZA ESE MISMO AÑO ")
    print("            -    EN EL  "+str(float(((count_alienvault_sh_valid_from_2019_anotheryear*100)/count_alienvault_sh_valid_from_2019)))+" % DE OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ VALIDOS DESDE 2019, LA VALIDEZ FINALIZA MÁS TARDE DE UN AÑO ")
    print("\n")
if(count_alienvault_sh_valid_from_2018>0):
    print("      -    EN EL  "+str(float(((count_alienvault_sh_valid_from_2018*100)/count_alienvault_sh_entries)))+" % DE OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ EL COMIENZO DE VALIDEZ ES 2018 O ANTERIOR. LOS PORCENTAJES DE FIN DE VALIDEZ SON LOS SIGUIENTES  :\n")
    print("\n")
    print("            -    EN EL  "+str(float(((count_alienvault_sh_valid_from_2018_valid_until_sameday*100)/count_alienvault_sh_valid_from_2018)))+" % DE OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ VALIDOS DESDE 2018 O ANTERIORMENTE, LA VALIDEZ FINALIZA ESE MISMO DÍA ")
    print("            -    EN EL  "+str(float(((count_alienvault_sh_valid_from_2018_valid_until_samemonth*100)/count_alienvault_sh_valid_from_2018)))+" % DE OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ VALIDOS DESDE 2018 O ANTERIORMENTE, LA VALIDEZ FINALIZA ESE MISMO MES")
    print("            -    EN EL  "+str(float(((count_alienvault_sh_valid_from_2018_valid_until_sameyear*100)/count_alienvault_sh_valid_from_2018)))+" % DE OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ VALIDOS DESDE 2018 O ANTERIORMENTE, LA VALIDEZ FINALIZA ESE MISMO AÑO ")
    print("            -    EN EL  "+str(float(((count_alienvault_sh_valid_from_2018_anotheryear*100)/count_alienvault_sh_valid_from_2018)))+" % DE OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ VALIDOS DESDE 2018 O ANTERIORMENTE, LA VALIDEZ FINALIZA MÁS TARDE DE UN AÑO ")
    print("\n")







    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
print("***************************ESTADÍSTICAS INICIO VALIDEZ/FIN DE VALIDEZ DATE ALIENVAULT PARTE IOT Y SMART HOME CONJUNTAS***************************")
print("\n")                            
                
print("\n")
print(" DE UN TOTAL DE "+str(count_alienvault_sh_entries+count_alienvault_iot_entries)+" OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ :\n") 
print("\n")
print("   - LAS ESTADISTICAS DE INICIO DE VALIDEZ SON LAS SIGUIENTES:  \n")
print("      -    EN  "+str(count_alienvault_sh_valid_from_2023+count_alienvault_iot_valid_from_2023)+" OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ EL COMIENZO DE VALIDEZ ES 2023. LAS ESTADÍSTICAS DE FIN DE VALIDEZ SON LAS SIGUIENTES :  \n")
print("\n")
print("            -    EN  "+str(count_alienvault_sh_valid_from_2023_valid_until_sameday+count_alienvault_iot_valid_from_2023_valid_until_sameday)+" OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ VALIDOS DESDE 2023, LA VALIDEZ FINALIZA ESE MISMO DÍA ")
print("            -    EN  "+str(count_alienvault_sh_valid_from_2023_valid_until_samemonth+count_alienvault_iot_valid_from_2023_valid_until_samemonth)+" OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ VALIDOS DESDE 2023, EL FIN DE PERIODO DE VALIDEZ ES ESE MISMO MES")
print("            -    EN  "+str(count_alienvault_sh_valid_from_2023_valid_until_sameyear+count_alienvault_iot_valid_from_2023_valid_until_sameyear)+" OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ VALIDOS DESDE 2023, EL FIN DE PERIODO DE VALIDEZ ES ESE MISMO AÑO ")
print("            -    EN  "+str(count_alienvault_sh_valid_from_2023_anotheryear+count_alienvault_iot_valid_from_2023_anotheryear)+" OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ VALIDOS DESDE 2023, EL FIN DE PERIODO DE VALIDEZ ES MÁS TARDE DE UN AÑO ")
print("\n")
print("      -    EN  "+str(count_alienvault_sh_valid_from_2022+count_alienvault_iot_valid_from_2022)+" OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ EL COMIENZO DE VALIDEZ ES 2022. LAS ESTADÍSTICAS DE FIN DE VALIDEZ SON LAS SIGUIENTES :  \n")
print("\n")
print("            -    EN  "+str(count_alienvault_sh_valid_from_2022_valid_until_sameday+count_alienvault_iot_valid_from_2022_valid_until_sameday)+" OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ VALIDOS DESDE 2022, LA VALIDEZ FINALIZA ESE MISMO DÍA ")
print("            -    EN  "+str(count_alienvault_sh_valid_from_2022_valid_until_samemonth+count_alienvault_iot_valid_from_2022_valid_until_samemonth)+" OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ VALIDOS DESDE 2022, EL FIN DE PERIODO DE VALIDEZ ES ESE MISMO MES")
print("            -    EN  "+str(count_alienvault_sh_valid_from_2022_valid_until_sameyear+count_alienvault_iot_valid_from_2022_valid_until_sameyear)+" OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ VALIDOS DESDE 2022, EL FIN DE PERIODO DE VALIDEZ ES ESE MISMO AÑO ")
print("            -    EN  "+str(count_alienvault_sh_valid_from_2022_anotheryear+count_alienvault_iot_valid_from_2022_anotheryear)+" OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ VALIDOS DESDE 2022, EL FIN DE PERIODO DE VALIDEZ ES MÁS TARDE DE UN AÑO ")
print("\n")
print("      -    EN  "+str(count_alienvault_sh_valid_from_2021+count_alienvault_iot_valid_from_2021)+" OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ EL COMIENZO DE VALIDEZ ES 2021. LAS ESTADÍSTICAS DE FIN DE VALIDEZ SON LAS SIGUIENTES :  \n")
print("\n")
print("            -    EN  "+str(count_alienvault_sh_valid_from_2021_valid_until_sameday+count_alienvault_iot_valid_from_2021_valid_until_sameday)+" OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ VALIDOS DESDE 2021, LA VALIDEZ FINALIZA ESE MISMO DÍA ")
print("            -    EN  "+str(count_alienvault_sh_valid_from_2021_valid_until_samemonth+count_alienvault_iot_valid_from_2021_valid_until_samemonth)+" OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ VALIDOS DESDE 2021, EL FIN DE PERIODO DE VALIDEZ ES ESE MISMO MES")
print("            -    EN  "+str(count_alienvault_sh_valid_from_2021_valid_until_sameyear+count_alienvault_iot_valid_from_2021_valid_until_sameyear)+" OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ VALIDOS DESDE 2021, EL FIN DE PERIODO DE VALIDEZ ES ESE MISMO AÑO ")
print("            -    EN  "+str(count_alienvault_sh_valid_from_2021_anotheryear+count_alienvault_iot_valid_from_2021_anotheryear)+" OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ VALIDOS DESDE 2021, EL FIN DE PERIODO DE VALIDEZ ES MÁS TARDE DE UN AÑO ")
print("\n")
print("      -    EN  "+str(count_alienvault_sh_valid_from_2020+count_alienvault_iot_valid_from_2020)+" OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ EL COMIENZO DE VALIDEZ ES 2020. LAS ESTADÍSTICAS DE FIN DE VALIDEZ SON LAS SIGUIENTES :  \n")
print("\n")
print("            -    EN  "+str(count_alienvault_sh_valid_from_2020_valid_until_sameday+count_alienvault_iot_valid_from_2020_valid_until_sameday)+" OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ VALIDOS DESDE 2020, LA VALIDEZ FINALIZA ESE MISMO DÍA ")
print("            -    EN  "+str(count_alienvault_sh_valid_from_2020_valid_until_samemonth+count_alienvault_iot_valid_from_2020_valid_until_samemonth)+" OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ VALIDOS DESDE 2020, EL FIN DE PERIODO DE VALIDEZ ES ESE MISMO MES")
print("            -    EN  "+str(count_alienvault_sh_valid_from_2020_valid_until_sameyear+count_alienvault_iot_valid_from_2020_valid_until_sameyear)+" OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ VALIDOS DESDE 2020, EL FIN DE PERIODO DE VALIDEZ ES ESE MISMO AÑO ")
print("            -    EN  "+str(count_alienvault_sh_valid_from_2020_anotheryear+count_alienvault_iot_valid_from_2020_anotheryear)+" OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ VALIDOS DESDE 2020, EL FIN DE PERIODO DE VALIDEZ ES MÁS TARDE DE UN AÑO ")
print("\n")
print("      -    EN  "+str(count_alienvault_sh_valid_from_2019+count_alienvault_iot_valid_from_2019)+" OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ EL COMIENZO DE VALIDEZ ES 2019. LAS ESTADÍSTICAS DE FIN DE VALIDEZ SON LAS SIGUIENTES :  \n")
print("\n")
print("            -    EN  "+str(count_alienvault_sh_valid_from_2019_valid_until_sameday+count_alienvault_iot_valid_from_2019_valid_until_sameday)+" OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ VALIDOS DESDE 2019, LA VALIDEZ FINALIZA ESE MISMO DÍA ")
print("            -    EN  "+str(count_alienvault_sh_valid_from_2019_valid_until_samemonth+count_alienvault_iot_valid_from_2019_valid_until_samemonth)+" OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ VALIDOS DESDE 2019, EL FIN DE PERIODO DE VALIDEZ ES ESE MISMO MES")
print("            -    EN  "+str(count_alienvault_sh_valid_from_2019_valid_until_sameyear+count_alienvault_iot_valid_from_2019_valid_until_sameyear)+" OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ VALIDOS DESDE 2019, EL FIN DE PERIODO DE VALIDEZ ES ESE MISMO AÑO ")
print("            -    EN  "+str(count_alienvault_sh_valid_from_2019_anotheryear+count_alienvault_iot_valid_from_2019_anotheryear)+" OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ VALIDOS DESDE 2019, EL FIN DE PERIODO DE VALIDEZ ES MÁS TARDE DE UN AÑO ")
print("\n")
print("      -    EN  "+str(count_alienvault_sh_valid_from_2018+count_alienvault_iot_valid_from_2018)+" OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ EL COMIENZO DE VALIDEZ ES 2018. LAS ESTADÍSTICAS DE FIN DE VALIDEZ SON LAS SIGUIENTES :  \n")
print("\n")
print("            -    EN  "+str(count_alienvault_sh_valid_from_2018_valid_until_sameday+count_alienvault_iot_valid_from_2018_valid_until_sameday)+" OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ VALIDOS DESDE 2018, LA VALIDEZ FINALIZA ESE MISMO DÍA ")
print("            -    EN  "+str(count_alienvault_sh_valid_from_2018_valid_until_samemonth+count_alienvault_iot_valid_from_2018_valid_until_samemonth)+" OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ VALIDOS DESDE 2018, EL FIN DE PERIODO DE VALIDEZ ES ESE MISMO MES")
print("            -    EN  "+str(count_alienvault_sh_valid_from_2018_valid_until_sameyear+count_alienvault_iot_valid_from_2018_valid_until_sameyear)+" OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ VALIDOS DESDE 2018, EL FIN DE PERIODO DE VALIDEZ ES ESE MISMO AÑO ")
print("            -    EN  "+str(count_alienvault_sh_valid_from_2018_anotheryear+count_alienvault_iot_valid_from_2018_anotheryear)+" OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ VALIDOS DESDE 2018, EL FIN DE PERIODO DE VALIDEZ ES MÁS TARDE DE UN AÑO ")
print("\n")













print("***************************PORCENTAJE INICIO VALIDEZ/FIN DE VALIDEZ DATE ALIENVAULT PARTE IOT Y SMART HOME CONJUNTAS***************************")
print("\n")                            
                
print("\n")
print(" DE UN TOTAL DE "+str(count_alienvault_sh_entries+count_alienvault_iot_entries)+" OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ :\n") 
print("\n")
print("   - LOS PORCENTAJES DE INICIO DE VALIDEZ SON LOS SIGUIENTES:  \n")
print("      -    EN EL  "+str(float(((count_alienvault_sh_valid_from_2023+count_alienvault_iot_valid_from_2023)*100)/(count_alienvault_sh_entries+count_alienvault_iot_entries)))+" % DE OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ EL COMIENZO DE VALIDEZ ES 2023. LOS PORCENTAJES DE FIN DE VALIDEZ SON LOS SIGUIENTES  :\n")
print("\n")
print("            -    EN EL  "+str(float((((count_alienvault_sh_valid_from_2023_valid_until_sameday+count_alienvault_iot_valid_from_2023_valid_until_sameday)*100)/(count_alienvault_sh_valid_from_2023+count_alienvault_iot_valid_from_2023))))+" % DE OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ VALIDOS DESDE 2023, LA VALIDEZ FINALIZA ESE MISMO DÍA ")
print("            -    EN EL  "+str(float((((count_alienvault_sh_valid_from_2023_valid_until_samemonth+count_alienvault_iot_valid_from_2023_valid_until_samemonth)*100)/(count_alienvault_sh_valid_from_2023+count_alienvault_iot_valid_from_2023))))+" % DE OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ VALIDOS DESDE 2023, LA VALIDEZ FINALIZA ESE MISMO MES")
print("            -    EN EL  "+str(float((((count_alienvault_sh_valid_from_2023_valid_until_sameyear+count_alienvault_iot_valid_from_2023_valid_until_sameyear)*100)/(count_alienvault_sh_valid_from_2023+count_alienvault_iot_valid_from_2023))))+" % DE OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ VALIDOS DESDE 2023, LA VALIDEZ FINALIZA ESE MISMO AÑO ")
print("            -    EN EL  "+str(float((((count_alienvault_sh_valid_from_2023_anotheryear+count_alienvault_iot_valid_from_2023_anotheryear)*100)/(count_alienvault_sh_valid_from_2023+count_alienvault_iot_valid_from_2023))))+" % DE OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ VALIDOS DESDE 2023, LA VALIDEZ FINALIZA MÁS TARDE DE UN AÑO ")
print("\n")
print("      -    EN EL  "+str(float(((count_alienvault_sh_valid_from_2022+count_alienvault_iot_valid_from_2022)*100)/(count_alienvault_sh_entries+count_alienvault_iot_entries)))+" % DE OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ EL COMIENZO DE VALIDEZ ES 2022. LOS PORCENTAJES DE FIN DE VALIDEZ SON LOS SIGUIENTES  :\n")
print("\n")
print("            -    EN EL  "+str(float((((count_alienvault_sh_valid_from_2022_valid_until_sameday+count_alienvault_iot_valid_from_2022_valid_until_sameday)*100)/(count_alienvault_sh_valid_from_2022+count_alienvault_iot_valid_from_2022))))+" % DE OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ VALIDOS DESDE 2022, LA VALIDEZ FINALIZA ESE MISMO DÍA ")
print("            -    EN EL  "+str(float((((count_alienvault_sh_valid_from_2022_valid_until_samemonth+count_alienvault_iot_valid_from_2022_valid_until_samemonth)*100)/(count_alienvault_sh_valid_from_2022+count_alienvault_iot_valid_from_2022))))+" % DE OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ VALIDOS DESDE 2022, LA VALIDEZ FINALIZA ESE MISMO MES")
print("            -    EN EL  "+str(float((((count_alienvault_sh_valid_from_2022_valid_until_sameyear+count_alienvault_iot_valid_from_2022_valid_until_sameyear)*100)/(count_alienvault_sh_valid_from_2022+count_alienvault_iot_valid_from_2022))))+" % DE OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ VALIDOS DESDE 2022, LA VALIDEZ FINALIZA ESE MISMO AÑO ")
print("            -    EN EL  "+str(float((((count_alienvault_sh_valid_from_2022_anotheryear+count_alienvault_iot_valid_from_2022_anotheryear)*100)/(count_alienvault_sh_valid_from_2022+count_alienvault_iot_valid_from_2022))))+" % DE OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ VALIDOS DESDE 2022, LA VALIDEZ FINALIZA MÁS TARDE DE UN AÑO ")
print("\n")
if((count_alienvault_sh_valid_from_2021+count_alienvault_iot_valid_from_2021)>0):
    print("      -    EN EL  "+str(float(((count_alienvault_sh_valid_from_2021+count_alienvault_iot_valid_from_2021)*100)/(count_alienvault_sh_entries+count_alienvault_iot_entries)))+" % DE OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ EL COMIENZO DE VALIDEZ ES 2021. LOS PORCENTAJES DE FIN DE VALIDEZ SON LOS SIGUIENTES  :\n")
    print("\n")
    print("            -    EN EL  "+str(float((((count_alienvault_sh_valid_from_2021_valid_until_sameday+count_alienvault_iot_valid_from_2021_valid_until_sameday)*100)/(count_alienvault_sh_valid_from_2021+count_alienvault_iot_valid_from_2021))))+" % DE OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ VALIDOS DESDE 2021, LA VALIDEZ FINALIZA ESE MISMO DÍA ")
    print("            -    EN EL  "+str(float((((count_alienvault_sh_valid_from_2021_valid_until_samemonth+count_alienvault_iot_valid_from_2021_valid_until_samemonth)*100)/(count_alienvault_sh_valid_from_2021+count_alienvault_iot_valid_from_2021))))+" % DE OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ VALIDOS DESDE 2021, LA VALIDEZ FINALIZA ESE MISMO MES")
    print("            -    EN EL  "+str(float((((count_alienvault_sh_valid_from_2021_valid_until_sameyear+count_alienvault_iot_valid_from_2021_valid_until_sameyear)*100)/(count_alienvault_sh_valid_from_2021+count_alienvault_iot_valid_from_2021))))+" % DE OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ VALIDOS DESDE 2021, LA VALIDEZ FINALIZA ESE MISMO AÑO ")
    print("            -    EN EL  "+str(float((((count_alienvault_sh_valid_from_2021_anotheryear+count_alienvault_iot_valid_from_2021_anotheryear)*100)/(count_alienvault_sh_valid_from_2021+count_alienvault_iot_valid_from_2021))))+" % DE OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ VALIDOS DESDE 2021, LA VALIDEZ FINALIZA MÁS TARDE DE UN AÑO ")
    print("\n")
if((count_alienvault_sh_valid_from_2020+count_alienvault_iot_valid_from_2020)>0):
    print("      -    EN EL  "+str(float(((count_alienvault_sh_valid_from_2020+count_alienvault_iot_valid_from_2020)*100)/(count_alienvault_sh_entries+count_alienvault_iot_entries)))+" % DE OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ EL COMIENZO DE VALIDEZ ES 2020. LOS PORCENTAJES DE FIN DE VALIDEZ SON LOS SIGUIENTES  :\n")
    print("\n")
    print("            -    EN EL  "+str(float((((count_alienvault_sh_valid_from_2020_valid_until_sameday+count_alienvault_iot_valid_from_2020_valid_until_sameday)*100)/(count_alienvault_sh_valid_from_2020+count_alienvault_iot_valid_from_2020))))+" % DE OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ VALIDOS DESDE 2020, LA VALIDEZ FINALIZA ESE MISMO DÍA ")
    print("            -    EN EL  "+str(float((((count_alienvault_sh_valid_from_2020_valid_until_samemonth+count_alienvault_iot_valid_from_2020_valid_until_samemonth)*100)/(count_alienvault_sh_valid_from_2020+count_alienvault_iot_valid_from_2020))))+" % DE OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ VALIDOS DESDE 2020, LA VALIDEZ FINALIZA ESE MISMO MES")
    print("            -    EN EL  "+str(float((((count_alienvault_sh_valid_from_2020_valid_until_sameyear+count_alienvault_iot_valid_from_2020_valid_until_sameyear)*100)/(count_alienvault_sh_valid_from_2020+count_alienvault_iot_valid_from_2020))))+" % DE OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ VALIDOS DESDE 2020, LA VALIDEZ FINALIZA ESE MISMO AÑO ")
    print("            -    EN EL  "+str(float((((count_alienvault_sh_valid_from_2020_anotheryear+count_alienvault_iot_valid_from_2020_anotheryear)*100)/(count_alienvault_sh_valid_from_2020+count_alienvault_iot_valid_from_2020))))+" % DE OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ VALIDOS DESDE 2020, LA VALIDEZ FINALIZA MÁS TARDE DE UN AÑO ")
    print("\n")
if((count_alienvault_sh_valid_from_2019+count_alienvault_iot_valid_from_2019)>0):
    print("      -    EN EL  "+str(float(((count_alienvault_sh_valid_from_2019+count_alienvault_iot_valid_from_2019)*100)/(count_alienvault_sh_entries+count_alienvault_iot_entries)))+" % DE OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ EL COMIENZO DE VALIDEZ ES 2019. LOS PORCENTAJES DE FIN DE VALIDEZ SON LOS SIGUIENTES  :\n")
    print("\n")
    print("            -    EN EL  "+str(float((((count_alienvault_sh_valid_from_2019_valid_until_sameday+count_alienvault_iot_valid_from_2019_valid_until_sameday)*100)/(count_alienvault_sh_valid_from_2019+count_alienvault_iot_valid_from_2019))))+" % DE OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ VALIDOS DESDE 2019, LA VALIDEZ FINALIZA ESE MISMO DÍA ")
    print("            -    EN EL  "+str(float((((count_alienvault_sh_valid_from_2019_valid_until_samemonth+count_alienvault_iot_valid_from_2019_valid_until_samemonth)*100)/(count_alienvault_sh_valid_from_2019+count_alienvault_iot_valid_from_2019))))+" % DE OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ VALIDOS DESDE 2019, LA VALIDEZ FINALIZA ESE MISMO MES")
    print("            -    EN EL  "+str(float((((count_alienvault_sh_valid_from_2019_valid_until_sameyear+count_alienvault_iot_valid_from_2019_valid_until_sameyear)*100)/(count_alienvault_sh_valid_from_2019+count_alienvault_iot_valid_from_2019))))+" % DE OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ VALIDOS DESDE 2019, LA VALIDEZ FINALIZA ESE MISMO AÑO ")
    print("            -    EN EL  "+str(float((((count_alienvault_sh_valid_from_2019_anotheryear+count_alienvault_iot_valid_from_2019_anotheryear)*100)/(count_alienvault_sh_valid_from_2019+count_alienvault_iot_valid_from_2019))))+" % DE OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ VALIDOS DESDE 2019, LA VALIDEZ FINALIZA MÁS TARDE DE UN AÑO ")
    print("\n")
if((count_alienvault_sh_valid_from_2018+count_alienvault_iot_valid_from_2018)>0):
    print("      -    EN EL  "+str(float(((count_alienvault_sh_valid_from_2018+count_alienvault_iot_valid_from_2018)*100)/(count_alienvault_sh_entries+count_alienvault_iot_entries)))+" % DE OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ EL COMIENZO DE VALIDEZ ES 2018 O ANTERIOR. LOS PORCENTAJES DE FIN DE VALIDEZ SON LOS SIGUIENTES  :\n")
    print("\n")
    print("            -    EN EL  "+str(float((((count_alienvault_sh_valid_from_2018_valid_until_sameday+count_alienvault_iot_valid_from_2018_valid_until_sameday)*100)/(count_alienvault_sh_valid_from_2018+count_alienvault_iot_valid_from_2018))))+" % DE OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ VALIDOS DESDE 2018 O ANTERIORMENTE, LA VALIDEZ FINALIZA ESE MISMO DÍA ")
    print("            -    EN EL  "+str(float((((count_alienvault_sh_valid_from_2018_valid_until_samemonth+count_alienvault_iot_valid_from_2018_valid_until_samemonth)*100)/(count_alienvault_sh_valid_from_2018+count_alienvault_iot_valid_from_2018))))+" % DE OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ VALIDOS DESDE 2018 O ANTERIORMENTE, LA VALIDEZ FINALIZA ESE MISMO MES")
    print("            -    EN EL  "+str(float((((count_alienvault_sh_valid_from_2018_valid_until_sameyear+count_alienvault_iot_valid_from_2018_valid_until_sameyear)*100)/(count_alienvault_sh_valid_from_2018+count_alienvault_iot_valid_from_2018))))+" % DE OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ VALIDOS DESDE 2018 O ANTERIORMENTE, LA VALIDEZ FINALIZA ESE MISMO AÑO ")
    print("            -    EN EL  "+str(float((((count_alienvault_sh_valid_from_2018_anotheryear+count_alienvault_iot_valid_from_2018_anotheryear)*100)/(count_alienvault_sh_valid_from_2018+count_alienvault_iot_valid_from_2018))))+" % DE OBJETOS PARA LOS QUE SE ENCUENTRA FIN DE PERIODO DE VALIDEZ VALIDOS DESDE 2018 O ANTERIORMENTE, LA VALIDEZ FINALIZA MÁS TARDE DE UN AÑO ")
    print("\n")
	
	






	
	
	
	

























