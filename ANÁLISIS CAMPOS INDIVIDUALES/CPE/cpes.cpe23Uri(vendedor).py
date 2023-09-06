
import pandas as pd

#Abro los ficheros con los que voy a tratar


df_cpe_iot=pd.read_excel('cpes_iot_2023.xlsx')
df_cpe_sh=pd.read_excel('cpes_smart_home_2023.xlsx')

#Vector para almacenar el nombre de los vendedores de las CPES
array_iot=[]
#Vector para almacenar el numero de veces que aparece un vendedor de una CPE
arraycounter_iot=[]

for r in range(0,len(df_cpe_iot["cpes.cpe23Uri"])):
    #Si existen varias cpe23Uris en una misma fila
    if('[' in df_cpe_iot["cpes.cpe23Uri"][r]):
        #Obtengo los valores de cpe23Uris
        aux=df_cpe_iot["cpes.cpe23Uri"][r].split(",")
        #Recorro los valores
        for k in range(0,len(aux)):
            if(len(aux)>0):
                aux_str=aux[k].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
                #Obtengo el valor vendedor para la cpe actual
                aux2=aux_str.split(":")
                vendor=aux2[3]
                #Si no existe el vendedor actual lo insertamos en el array y ponemos el contador de apariciones a 1
                if vendor not in array_iot:
                    array_iot.append(vendor)
                    arraycounter_iot.append(1)
                else:
                    #Si ya existe aumentamos su contador de apariciones en una unidad
                    index=array_iot.index(vendor)
                    counter=int(arraycounter_iot[index])
                    counter=counter+1
                    arraycounter_iot[index]=counter
    else:
        #Si existe un unico valor de cpe23Uri en la fila actual
        aux_str=df_cpe_iot["cpes.cpe23Uri"][r].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
        #Obtengo el valor de type/part del cpe23Uri actual
        aux2=aux_str.split(":")
        vendor=aux2[3]
        #Si no existe el vendedor actual lo insertamos en el array y ponemos el contador de apariciones a 1
        if vendor not in array_iot:
            array_iot.append(vendor)
            arraycounter_iot.append(1)
        else:
            #Si ya existe aumentamos su contador de apariciones en una unidad
            index=array_iot.index(vendor)
            counter=int(arraycounter_iot[index])
            counter=counter+1
            arraycounter_iot[index]=counter
            
            



print("**************************ESTADÍSTICAS VENDEDOR CPE IOT********************************")
print("\n")
print("  DE UN TOTAL DE  "+str(len(df_cpe_iot["cpes.cpe23Uri"]))+" CPES, LAS ESTADÍSTICAS DE VENDEDOR SON LAS SIGUIENTES : \n")

for g in range(0,len(array_iot)):
    print("  -  EN UN TOTAL DE  "+str(arraycounter_iot[g])+" CPES EL VENDEDOR ES "+str(array_iot[g].upper())+" \n")


print("\n")
print("**************************PORCENTAJE VENDEDOR CPE IOT********************************")
print("\n")
print("  DE UN TOTAL DE  "+str(len(df_cpe_iot["cpes.cpe23Uri"]))+" CPES, LOS PORCENTAJES DE VENDEDOR SON LOS SIGUIENTES : \n")
for g in range(0,len(array_iot)):
    print("  -  EL "+str(float(((arraycounter_iot[g]*100)/len(df_cpe_iot["cpes.cpe23Uri"]))))+" % DE LOS CPES TIENEN COMO VENDEDOR"+str(array_iot[g].upper())+" \n")

    

#Vector para almacenar el nombre de los vendedores de las CPES
array_sh=[]
#Vector para almacenar el numero de veces que aparece un vendedor de una CPE
arraycounter_sh=[]

for r in range(0,len(df_cpe_sh["cpes.cpe23Uri"])):
    #Si existen varias cpe23Uris en una misma fila
    if('[' in df_cpe_sh["cpes.cpe23Uri"][r]):
        #Obtengo los valores de cpe23Uris
        aux=df_cpe_sh["cpes.cpe23Uri"][r].split(",")
        #Recorro los valores
        for k in range(0,len(aux)):
            if(len(aux)>0):
                aux_str=aux[k].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
                #Obtengo el valor de type/part para la cpe23Uri actual
                aux2=aux_str.split(":")
                vendor=aux2[3]
                #Si no existe el vendedor actual lo insertamos en el array y ponemos el contador de apariciones a 1
                if vendor not in array_sh:
                    array_sh.append(vendor)
                    arraycounter_sh.append(1)
                else:
                    #Si ya existe aumentamos su contador de apariciones en una unidad
                    index=array.index(vendor)
                    counter=int(arraycounter_sh[index])
                    counter=counter+1
                    arraycounter_sh[index]=counter
    else:
        #Si existe un unico valor de cpe23Uri en la fila actual
        aux_str=df_cpe_sh["cpes.cpe23Uri"][r].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
        #Obtengo el valor de type/part del cpe23Uri actual
        aux2=aux_str.split(":")
        vendor=aux2[3]
        #Si no existe el vendedor actual lo insertamos en el array y ponemos el contador de apariciones a 1
        if vendor not in array_sh:
            array_sh.append(vendor)
            arraycounter_sh.append(1)
        else:
            #Si ya existe aumentamos su contador de apariciones en una unidad
            index=array_sh.index(vendor)
            counter=int(arraycounter_sh[index])
            counter=counter+1
            arraycounter_sh[index]=counter
            
            



print("**************************ESTADÍSTICAS VENDEDOR CPE SMART HOME********************************")
print("\n")
print("  DE UN TOTAL DE  "+str(len(df_cpe_sh["cpes.cpe23Uri"]))+" CPES, LAS ESTADÍSTICAS DE VENDEDOR SON : \n")

for g in range(0,len(array_sh)):
    print("  -  EN UN TOTAL DE  "+str(arraycounter_sh[g])+" CPES EL VENDEDOR ES "+str(array_sh[g].upper())+" \n")


print("\n")
print("**************************PORCENTAJE VENDEDOR CPE SMART HOME********************************")
print("\n")
print("  DE UN TOTAL DE  "+str(len(df_cpe_sh["cpes.cpe23Uri"]))+" CPES, LOS PORCENTAJES DE VENDEDOR SON : \n")
for g in range(0,len(array_sh)):
    print("  -  EL "+str(float(((arraycounter_sh[g]*100)/len(df_cpe_sh["cpes.cpe23Uri"]))))+" % DE LOS CPES TIENEN COMO VENDEDOR "+str(array_sh[g].upper())+" \n")
