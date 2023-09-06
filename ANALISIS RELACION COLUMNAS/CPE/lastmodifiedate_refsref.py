
#*********************************************************************RELACION LAST MODIFIED DATE Y REFS REF FICHERO CPE ******************************************************************************





import pandas as pd

#Abro los ficheros con los que voy a tratar


df_cpe_iot=pd.read_excel('cpes_iot_2023.xlsx')
df_cpe_sh=pd.read_excel('cpes_smart_home_2023.xlsx')




print("********************************FECHA DE ULTIMA MODIFICACION DE CPE/FUENTE DE REFERENCIA ASOCIADA A CPE PARTE IOT********************************")
print("\n")
print("\n")

#Contador de referencias existentes
counterrefs_iot=0

#Contador de referencias modificadas en un anio especifico
cpes_lastmodified2023_iot=0
#Contador de distintas referencias segun un anio de modificacion
cpes_lastmodified2023_refgithub_iot=0
cpes_lastmodified2023_refptc_iot=0
cpes_lastmodified2023_refsymbiote_iot=0
cpes_lastmodified2023_refasus_iot=0
cpes_lastmodified2023_refiotkonker_iot=0
cpes_lastmodified2023_refvulncheck_iot=0
cpes_lastmodified2023_refxiongmaitech_iot=0
cpes_lastmodified2023_refmicrosoft_iot=0
cpes_lastmodified2023_refriot_iot=0

cpes_lastmodified2022_iot=0
cpes_lastmodified2022_refgithub_iot=0
cpes_lastmodified2022_refptc_iot=0
cpes_lastmodified2022_refsymbiote_iot=0
cpes_lastmodified2022_refasus_iot=0
cpes_lastmodified2022_refiotkonker_iot=0
cpes_lastmodified2022_refvulncheck_iot=0
cpes_lastmodified2022_refxiongmaitech_iot=0
cpes_lastmodified2022_refmicrosoft_iot=0
cpes_lastmodified2022_refriot_iot=0


cpes_lastmodified2021_iot=0
cpes_lastmodified2021_refgithub_iot=0
cpes_lastmodified2021_refptc_iot=0
cpes_lastmodified2021_refsymbiote_iot=0
cpes_lastmodified2021_refasus_iot=0
cpes_lastmodified2021_refiotkonker_iot=0
cpes_lastmodified2021_refvulncheck_iot=0
cpes_lastmodified2021_refxiongmaitech_iot=0
cpes_lastmodified2021_refmicrosoft_iot=0
cpes_lastmodified2021_refriot_iot=0


cpes_lastmodified2020_iot=0
cpes_lastmodified2020_refgithub_iot=0
cpes_lastmodified2020_refptc_iot=0
cpes_lastmodified2020_refsymbiote_iot=0
cpes_lastmodified2020_refasus_iot=0
cpes_lastmodified2020_refiotkonker_iot=0
cpes_lastmodified2020_refvulncheck_iot=0
cpes_lastmodified2020_refxiongmaitech_iot=0
cpes_lastmodified2020_refmicrosoft_iot=0
cpes_lastmodified2020_refriot_iot=0

cpes_lastmodified2019_iot=0
cpes_lastmodified2019_refgithub_iot=0
cpes_lastmodified2019_refptc_iot=0
cpes_lastmodified2019_refsymbiote_iot=0
cpes_lastmodified2019_refasus_iot=0
cpes_lastmodified2019_refiotkonker_iot=0
cpes_lastmodified2019_refvulncheck_iot=0
cpes_lastmodified2019_refxiongmaitech_iot=0
cpes_lastmodified2019_refmicrosoft_iot=0
cpes_lastmodified2019_refriot_iot=0

cpes_lastmodified2018_iot=0
cpes_lastmodified2018_refgithub_iot=0
cpes_lastmodified2018_refptc_iot=0
cpes_lastmodified2018_refsymbiote_iot=0
cpes_lastmodified2018_refasus_iot=0
cpes_lastmodified2018_refiotkonker_iot=0
cpes_lastmodified2018_refvulncheck_iot=0
cpes_lastmodified2018_refxiongmaitech_iot=0
cpes_lastmodified2018_refmicrosoft_iot=0
cpes_lastmodified2018_refriot_iot=0







#Recorro los valores de fecha de modificacion
for r in range(0,len(df_cpe_iot["cpes.lastModifiedDate"])):
    str_anio_modifdate_cpe_iot=df_cpe_iot["cpes.lastModifiedDate"][r].split("-")
    anio_modifdate_cpe_iot=int(str_anio_modifdate_cpe_iot[0])
    if(anio_modifdate_cpe_iot >= 2023):
        #Si existen varios valores de referencia para una misma fecha de modificacion en una misma fila
        if('[' in df_cpe_iot["cpes.refs.ref"][r]):
            aux=df_cpe_iot["cpes.refs.ref"][r].split(",")
            #Recorro los valores de referencia
            for k in range(0,len(aux)):
                if(len(aux)>0):
                    cpes_lastmodified2023_iot+=1
                    counterrefs_iot+=1
                    #Obtengo el valor de la referencia
                    aux_str=aux[k].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
                    if('github' in aux_str):
                        cpes_lastmodified2023_refgithub_iot+=1   
                    elif('ptc.com' in aux_str):
                        cpes_lastmodified2023_refptc_iot+=1
                    elif('symbiote.com' in aux_str):
                        cpes_lastmodified2023_refsymbiote_iot+=1   
                    elif('asus.com' in aux_str):
                        cpes_lastmodified2023_refasus_iot+=1    
                    elif('iot.konker' in aux_str):
                        cpes_lastmodified2023_refiotkonker_iot+=1    
                    elif('vulncheck' in aux_str):
                        cpes_lastmodified2023_refvulncheck_iot+=1    
                    elif('xiongmaitech' in aux_str):
                        cpes_lastmodified2023_refxiongmaitech_iot+=1    
                    elif('microsoft' in aux_str):
                        cpes_lastmodified2023_refmicrosoft_iot+=1    
                    elif('riot' in aux_str):
                        cpes_lastmodified2023_refriot_iot+=1
        else:
            #Si solamente existe un valor de referencia para la fila actual
            counterrefs_iot+=1
            cpes_lastmodified2023_iot+=1
            if('github' in df_cpe_iot["cpes.refs.ref"][r]):
                cpes_lastmodified2023_refgithub_iot+=1   
            elif('ptc.com' in df_cpe_iot["cpes.refs.ref"][r]):
                cpes_lastmodified2023_refptc_iot+=1
            elif('symbiote.com' in df_cpe_iot["cpes.refs.ref"][r]):
                cpes_lastmodified2023_refsymbiote_iot+=1
            elif('asus.com' in df_cpe_iot["cpes.refs.ref"][r]):
                cpes_lastmodified2023_refasus_iot+=1
            elif('iot.konker' in df_cpe_iot["cpes.refs.ref"][r]):
                cpes_lastmodified2023_refiotkonker_iot+=1
            elif('vulncheck' in df_cpe_iot["cpes.refs.ref"][r]):
                cpes_lastmodified2023_refvulncheck_iot+=1
            elif('xiongmaitech' in df_cpe_iot["cpes.refs.ref"][r]):
                cpes_lastmodified2023_refxiongmaitech_iot+=1
            elif('microsoft' in df_cpe_iot["cpes.refs.ref"][r]):
                cpes_lastmodified2023_refmicrosoft_iot+=1
            elif('riot' in df_cpe_iot["cpes.refs.ref"][r]):
                cpes_lastmodified2023_refriot_iot+=1
        
        
    elif(anio_modifdate_cpe_iot >= 2022):
        if('[' in df_cpe_iot["cpes.refs.ref"][r]):
            aux=df_cpe_iot["cpes.refs.ref"][r].split(",")
            for k in range(0,len(aux)):
                if(len(aux)>0):
                    cpes_lastmodified2022_iot+=1
                    counterrefs_iot+=1
                    aux_str=aux[k].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
                    if('github' in aux_str):
                        cpes_lastmodified2022_refgithub_iot+=1   
                    elif('ptc.com' in aux_str):
                        cpes_lastmodified2022_refptc_iot+=1
                    elif('symbiote.com' in aux_str):
                        cpes_lastmodified2022_refsymbiote_iot+=1   
                    elif('asus.com' in aux_str):
                        cpes_lastmodified2022_refasus_iot+=1    
                    elif('iot.konker' in aux_str):
                        cpes_lastmodified2022_refiotkonker_iot+=1    
                    elif('vulncheck' in aux_str):
                        cpes_lastmodified2022_refvulncheck_iot+=1    
                    elif('xiongmaitech' in aux_str):
                        cpes_lastmodified2022_refxiongmaitech_iot+=1    
                    elif('microsoft' in aux_str):
                        cpes_lastmodified2022_refmicrosoft_iot+=1    
                    elif('riot' in aux_str):
                        cpes_lastmodified2022_refriot_iot+=1
                    
        else:
            counterrefs_iot+=1
            cpes_lastmodified2022_iot+=1
            if('github' in df_cpe_iot["cpes.refs.ref"][r]):
                cpes_lastmodified2022_refgithub_iot+=1   
            elif('ptc.com' in df_cpe_iot["cpes.refs.ref"][r]):
                cpes_lastmodified2022_refptc_iot+=1
            elif('symbiote.com' in df_cpe_iot["cpes.refs.ref"][r]):
                cpes_lastmodified2022_refsymbiote_iot+=1
            elif('asus.com' in df_cpe_iot["cpes.refs.ref"][r]):
                cpes_lastmodified2022_refasus_iot+=1
            elif('iot.konker' in df_cpe_iot["cpes.refs.ref"][r]):
                cpes_lastmodified2022_refiotkonker_iot+=1
            elif('vulncheck' in df_cpe_iot["cpes.refs.ref"][r]):
                cpes_lastmodified2022_refvulncheck_iot+=1
            elif('xiongmaitech' in df_cpe_iot["cpes.refs.ref"][r]):
                cpes_lastmodified2022_refxiongmaitech_iot+=1
            elif('microsoft' in df_cpe_iot["cpes.refs.ref"][r]):
                cpes_lastmodified2022_refmicrosoft_iot+=1
            elif('riot' in df_cpe_iot["cpes.refs.ref"][r]):
                cpes_lastmodified2022_refriot_iot+=1
   
    elif(anio_modifdate_cpe_iot >= 2021):
        if('[' in df_cpe_iot["cpes.refs.ref"][r]):
            aux=df_cpe_iot["cpes.refs.ref"][r].split(",")
            for k in range(0,len(aux)):
                if(len(aux)>0):
                    cpes_lastmodified2021_iot+=1
                    counterrefs_iot+=1
                    aux_str=aux[k].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
                    if('github' in aux_str):
                        cpes_lastmodified2021_refgithub_iot+=1   
                    elif('ptc.com' in aux_str):
                        cpes_lastmodified2021_refptc_iot+=1
                    elif('symbiote.com' in aux_str):
                        cpes_lastmodified2021_refsymbiote_iot+=1   
                    elif('asus.com' in aux_str):
                        cpes_lastmodified2021_refasus_iot+=1    
                    elif('iot.konker' in aux_str):
                        cpes_lastmodified2021_refiotkonker_iot+=1    
                    elif('vulncheck' in aux_str):
                        cpes_lastmodified2021_refvulncheck_iot+=1    
                    elif('xiongmaitech' in aux_str):
                        cpes_lastmodified2021_refxiongmaitech_iot+=1    
                    elif('microsoft' in aux_str):
                        cpes_lastmodified2021_refmicrosoft_iot+=1    
                    elif('riot' in aux_str):
                        cpes_lastmodified2021_refriot_iot+=1
        else:
            counterrefs_iot+=1
            cpes_lastmodified2021_iot+=1
            if('github' in df_cpe_iot["cpes.refs.ref"][r]):
                cpes_lastmodified2021_refgithub_iot+=1   
            elif('ptc.com' in df_cpe_iot["cpes.refs.ref"][r]):
                cpes_lastmodified2021_refptc_iot+=1
            elif('symbiote.com' in df_cpe_iot["cpes.refs.ref"][r]):
                cpes_lastmodified2021_refsymbiote_iot+=1
            elif('asus.com' in df_cpe_iot["cpes.refs.ref"][r]):
                cpes_lastmodified2021_refasus_iot+=1
            elif('iot.konker' in df_cpe_iot["cpes.refs.ref"][r]):
                cpes_lastmodified2021_refiotkonker_iot+=1
            elif('vulncheck' in df_cpe_iot["cpes.refs.ref"][r]):
                cpes_lastmodified2021_refvulncheck_iot+=1
            elif('xiongmaitech' in df_cpe_iot["cpes.refs.ref"][r]):
                cpes_lastmodified2021_refxiongmaitech_iot+=1
            elif('microsoft' in df_cpe_iot["cpes.refs.ref"][r]):
                cpes_lastmodified2021_refmicrosoft_iot+=1
            elif('riot' in df_cpe_iot["cpes.refs.ref"][r]):
                cpes_lastmodified2021_refriot_iot+=1
   
    elif(anio_modifdate_cpe_iot >= 2020):
        if('[' in df_cpe_iot["cpes.refs.ref"][r]):
            aux=df_cpe_iot["cpes.refs.ref"][r].split(",")
            for k in range(0,len(aux)):
                if(len(aux)>0):
                    cpes_lastmodified2020_iot+=1
                    counterrefs_iot+=1
                    aux_str=aux[k].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
                    if('github' in aux_str):
                        cpes_lastmodified2020_refgithub_iot+=1   
                    elif('ptc.com' in aux_str):
                        cpes_lastmodified2020_refptc_iot+=1
                    elif('symbiote.com' in aux_str):
                        cpes_lastmodified2020_refsymbiote_iot+=1   
                    elif('asus.com' in aux_str):
                        cpes_lastmodified2020_refasus_iot+=1    
                    elif('iot.konker' in aux_str):
                        cpes_lastmodified2020_refiotkonker_iot+=1    
                    elif('vulncheck' in aux_str):
                        cpes_lastmodified2020_refvulncheck_iot+=1    
                    elif('xiongmaitech' in aux_str):
                        cpes_lastmodified2020_refxiongmaitech_iot+=1    
                    elif('microsoft' in aux_str):
                        cpes_lastmodified2020_refmicrosoft_iot+=1    
                    elif('riot' in aux_str):
                        cpes_lastmodified2020_refriot_iot+=1
        else:
            counterrefs_iot+=1
            cpes_lastmodified2020_iot+=1
            if('github' in df_cpe_iot["cpes.refs.ref"][r]):
                cpes_lastmodified2020_refgithub_iot+=1   
            elif('ptc.com' in df_cpe_iot["cpes.refs.ref"][r]):
                cpes_lastmodified2020_refptc_iot+=1
            elif('symbiote.com' in df_cpe_iot["cpes.refs.ref"][r]):
                cpes_lastmodified2020_refsymbiote_iot+=1
            elif('asus.com' in df_cpe_iot["cpes.refs.ref"][r]):
                cpes_lastmodified2020_refasus_iot+=1
            elif('iot.konker' in df_cpe_iot["cpes.refs.ref"][r]):
                cpes_lastmodified2020_refiotkonker_iot+=1
            elif('vulncheck' in df_cpe_iot["cpes.refs.ref"][r]):
                cpes_lastmodified2020_refvulncheck_iot+=1
            elif('xiongmaitech' in df_cpe_iot["cpes.refs.ref"][r]):
                cpes_lastmodified2020_refxiongmaitech_iot+=1
            elif('microsoft' in df_cpe_iot["cpes.refs.ref"][r]):
                cpes_lastmodified2020_refmicrosoft_iot+=1
            elif('riot' in df_cpe_iot["cpes.refs.ref"][r]):
                cpes_lastmodified2020_refriot_iot+=1
   
    elif(anio_modifdate_cpe_iot >= 2019):
        if('[' in df_cpe_iot["cpes.refs.ref"][r]):
            aux=df_cpe_iot["cpes.refs.ref"][r].split(",")
            for k in range(0,len(aux)):
                if(len(aux)>0):
                    cpes_lastmodified2019_iot+=1
                    counterrefs_iot+=1
                    aux_str=aux[k].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
                    if('github' in aux_str):
                        cpes_lastmodified2019_refgithub_iot+=1   
                    elif('ptc.com' in aux_str):
                        cpes_lastmodified2019_refptc_iot+=1
                    elif('symbiote.com' in aux_str):
                        cpes_lastmodified2019_refsymbiote_iot+=1   
                    elif('asus.com' in aux_str):
                        cpes_lastmodified2019_refasus_iot+=1    
                    elif('iot.konker' in aux_str):
                        cpes_lastmodified2019_refiotkonker_iot+=1    
                    elif('vulncheck' in aux_str):
                        cpes_lastmodified2019_refvulncheck_iot+=1    
                    elif('xiongmaitech' in aux_str):
                        cpes_lastmodified2019_refxiongmaitech_iot+=1    
                    elif('microsoft' in aux_str):
                        cpes_lastmodified2019_refmicrosoft_iot+=1    
                    elif('riot' in aux_str):
                        cpes_lastmodified2019_refriot_iot+=1
        else:
            counterrefs_iot+=1
            cpes_lastmodified2019_iot+=1
            if('github' in df_cpe_iot["cpes.refs.ref"][r]):
                cpes_lastmodified2019_refgithub_iot+=1   
            elif('ptc.com' in df_cpe_iot["cpes.refs.ref"][r]):
                cpes_lastmodified2019_refptc_iot+=1
            elif('symbiote.com' in df_cpe_iot["cpes.refs.ref"][r]):
                cpes_lastmodified2019_refsymbiote_iot+=1
            elif('asus.com' in df_cpe_iot["cpes.refs.ref"][r]):
                cpes_lastmodified2019_refasus_iot+=1
            elif('iot.konker' in df_cpe_iot["cpes.refs.ref"][r]):
                cpes_lastmodified2019_refiotkonker_iot+=1
            elif('vulncheck' in df_cpe_iot["cpes.refs.ref"][r]):
                cpes_lastmodified2019_refvulncheck_iot+=1
            elif('xiongmaitech' in df_cpe_iot["cpes.refs.ref"][r]):
                cpes_lastmodified2019_refxiongmaitech_iot+=1
            elif('microsoft' in df_cpe_iot["cpes.refs.ref"][r]):
                cpes_lastmodified2019_refmicrosoft_iot+=1
            elif('riot' in df_cpe_iot["cpes.refs.ref"][r]):
                cpes_lastmodified2019_refriot_iot+=1
                
    else:
        if('[' in df_cpe_iot["cpes.refs.ref"][r]):
            aux=df_cpe_iot["cpes.refs.ref"][r].split(",")
            for k in range(0,len(aux)):
                if(len(aux)>0):
                    cpes_lastmodified2018_iot+=1
                    counterrefs_iot+=1
                    aux_str=aux[k].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
                    if('github' in aux_str):
                        cpes_lastmodified2018_refgithub_iot+=1   
                    elif('ptc.com' in aux_str):
                        cpes_lastmodified2018_refptc_iot+=1
                    elif('symbiote.com' in aux_str):
                        cpes_lastmodified2018_refsymbiote_iot+=1   
                    elif('asus.com' in aux_str):
                        cpes_lastmodified2018_refasus_iot+=1    
                    elif('iot.konker' in aux_str):
                        cpes_lastmodified2018_refiotkonker_iot+=1    
                    elif('vulncheck' in aux_str):
                        cpes_lastmodified2018_refvulncheck_iot+=1    
                    elif('xiongmaitech' in aux_str):
                        cpes_lastmodified2018_refxiongmaitech_iot+=1    
                    elif('microsoft' in aux_str):
                        cpes_lastmodified2018_refmicrosoft_iot+=1    
                    elif('riot' in aux_str):
                        cpes_lastmodified2018_refriot_iot+=1
        else:
            counterrefs_iot+=1
            cpes_lastmodified2018_iot+=1
            if('github' in df_cpe_iot["cpes.refs.ref"][r]):
                cpes_lastmodified2018_refgithub_iot+=1   
            elif('ptc.com' in df_cpe_iot["cpes.refs.ref"][r]):
                cpes_lastmodified2018_refptc_iot+=1
            elif('symbiote.com' in df_cpe_iot["cpes.refs.ref"][r]):
                cpes_lastmodified2018_refsymbiote_iot+=1
            elif('asus.com' in df_cpe_iot["cpes.refs.ref"][r]):
                cpes_lastmodified2018_refasus_iot+=1
            elif('iot.konker' in df_cpe_iot["cpes.refs.ref"][r]):
                cpes_lastmodified2018_refiotkonker_iot+=1
            elif('vulncheck' in df_cpe_iot["cpes.refs.ref"][r]):
                cpes_lastmodified2018_refvulncheck_iot+=1
            elif('xiongmaitech' in df_cpe_iot["cpes.refs.ref"][r]):
                cpes_lastmodified2018_refxiongmaitech_iot+=1
            elif('microsoft' in df_cpe_iot["cpes.refs.ref"][r]):
                cpes_lastmodified2018_refmicrosoft_iot+=1
            elif('riot' in df_cpe_iot["cpes.refs.ref"][r]):
                cpes_lastmodified2018_refriot_iot+=1




        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
#Total numero de referencias independientemente del anio   
cpes_refgithub_iot=cpes_lastmodified2023_refgithub_iot+cpes_lastmodified2022_refgithub_iot+cpes_lastmodified2021_refgithub_iot+cpes_lastmodified2020_refgithub_iot+cpes_lastmodified2019_refgithub_iot+cpes_lastmodified2018_refgithub_iot   
cpes_refptc_iot=cpes_lastmodified2023_refptc_iot+cpes_lastmodified2022_refptc_iot+cpes_lastmodified2021_refptc_iot+cpes_lastmodified2020_refptc_iot+cpes_lastmodified2019_refptc_iot+cpes_lastmodified2018_refptc_iot   
cpes_refsymbiote_iot=cpes_lastmodified2023_refsymbiote_iot+cpes_lastmodified2022_refsymbiote_iot+cpes_lastmodified2021_refsymbiote_iot+cpes_lastmodified2020_refsymbiote_iot+cpes_lastmodified2019_refsymbiote_iot+cpes_lastmodified2018_refsymbiote_iot
cpes_refasus_iot=cpes_lastmodified2023_refasus_iot+cpes_lastmodified2022_refasus_iot+cpes_lastmodified2021_refasus_iot+cpes_lastmodified2020_refasus_iot+cpes_lastmodified2019_refasus_iot+cpes_lastmodified2018_refasus_iot
cpes_refiotkonker_iot=cpes_lastmodified2023_refiotkonker_iot+cpes_lastmodified2022_refiotkonker_iot+cpes_lastmodified2021_refiotkonker_iot+cpes_lastmodified2020_refiotkonker_iot+cpes_lastmodified2019_refiotkonker_iot+cpes_lastmodified2018_refiotkonker_iot
cpes_refvulncheck_iot=cpes_lastmodified2023_refvulncheck_iot+cpes_lastmodified2022_refvulncheck_iot+cpes_lastmodified2021_refvulncheck_iot+cpes_lastmodified2020_refvulncheck_iot+cpes_lastmodified2019_refvulncheck_iot+cpes_lastmodified2018_refvulncheck_iot
cpes_refxiongmaitech_iot=cpes_lastmodified2023_refxiongmaitech_iot+cpes_lastmodified2022_refxiongmaitech_iot+cpes_lastmodified2021_refxiongmaitech_iot+cpes_lastmodified2020_refxiongmaitech_iot+cpes_lastmodified2019_refxiongmaitech_iot+cpes_lastmodified2018_refxiongmaitech_iot
cpes_refmicrosoft_iot=cpes_lastmodified2023_refmicrosoft_iot+cpes_lastmodified2022_refmicrosoft_iot+cpes_lastmodified2021_refmicrosoft_iot+cpes_lastmodified2020_refmicrosoft_iot+cpes_lastmodified2019_refmicrosoft_iot+cpes_lastmodified2018_refmicrosoft_iot
cpes_refriot_iot=cpes_lastmodified2023_refriot_iot+cpes_lastmodified2022_refriot_iot+cpes_lastmodified2021_refriot_iot+cpes_lastmodified2020_refriot_iot+cpes_lastmodified2019_refriot_iot+cpes_lastmodified2018_refriot_iot

        


print("********************************ESTADÍSTICAS FECHA DE ULTIMA MODIFICACION CPE/FUENTE DE REFERENCIA CPE PARTE IOT********************************")
print("\n")                            
                
print("\n")
print(" DE UN TOTAL DE "+str(counterrefs_iot)+" REFERENCIAS DE CPES , LAS ESTADISTICAS DE RELACION DE FECHA DE MODIFICACION Y FUENTE DE REFERENCIA SON LAS SIGUIENTES:  \n")
print("\n")
print("      -    EN  "+str(cpes_refgithub_iot)+" REFERENCIAS LA FUENTE ES GITHUB.COM  \n")
print("      -    EN  "+str(cpes_refptc_iot)+" REFERENCIAS LA FUENTE ES PTC.COM  \n")
print("      -    EN  "+str(cpes_refsymbiote_iot)+" REFERENCIAS LA FUENTE ES SYMBIOTE.COM  \n")
print("      -    EN  "+str(cpes_refasus_iot)+" REFERENCIAS LA FUENTE ES ASUS.COM  \n")
print("      -    EN  "+str(cpes_refiotkonker_iot)+" REFERENCIAS LA FUENTE ES IOT.KONKER  \n")
print("      -    EN  "+str(cpes_refvulncheck_iot)+" REFERENCIAS LA FUENTE ES VULNCHECK.COM  \n")
print("      -    EN  "+str(cpes_refxiongmaitech_iot)+" REFERENCIAS LA FUENTE ES XIONGMAITECH.COM  \n")
print("      -    EN  "+str(cpes_refmicrosoft_iot)+" REFERENCIAS LA FUENTE ES MICROSOFT.COM  \n")
print("      -    EN  "+str(cpes_refriot_iot)+" REFERENCIAS LA FUENTE ES RIOT-OS.ORG  \n")
print("\n")
print("      -    EN  "+str(cpes_lastmodified2023_iot)+" REFERENCIAS DE CPES LA FECHA DE MODIFICACION ES 2023. LAS ESTADÍSTICAS DE FUENTE DE REFERENCIA SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(cpes_lastmodified2023_refgithub_iot)+" REFERENCIAS LA FUENTE ES GITHUB.COM ")
print("            -    EN  "+str(cpes_lastmodified2023_refptc_iot)+" REFERENCIAS LA FUENTE ES PTC.COM ")
print("            -    EN  "+str(cpes_lastmodified2023_refsymbiote_iot)+" REFERENCIAS LA FUENTE ES SYMBIOTE.COM ")
print("            -    EN  "+str(cpes_lastmodified2023_refasus_iot)+" REFERENCIAS LA FUENTE ES ASUS.COM ")
print("            -    EN  "+str(cpes_lastmodified2023_refiotkonker_iot)+" REFERENCIAS LA FUENTE ES IOT.KONKER ")
print("            -    EN  "+str(cpes_lastmodified2023_refvulncheck_iot)+" REFERENCIAS LA FUENTE ES VULNCHECK.COM ")
print("            -    EN  "+str(cpes_lastmodified2023_refxiongmaitech_iot)+" REFERENCIAS LA FUENTE ES XIONGMAITECH.COM ")
print("            -    EN  "+str(cpes_lastmodified2023_refmicrosoft_iot)+" REFERENCIAS LA FUENTE ES MICROSOFT.COM ")
print("            -    EN  "+str(cpes_lastmodified2023_refriot_iot)+" REFERENCIAS LA FUENTE ES RIOT-OS.ORG ")
print("\n")
print("      -    EN  "+str(cpes_lastmodified2022_iot)+" REFERENCIAS DE CPES LA FECHA DE MODIFICACION ES 2022. LAS ESTADÍSTICAS DE FUENTE DE REFERENCIA SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(cpes_lastmodified2022_refgithub_iot)+" REFERENCIAS LA FUENTE ES GITHUB.COM ")
print("            -    EN  "+str(cpes_lastmodified2022_refptc_iot)+" REFERENCIAS LA FUENTE ES PTC.COM ")
print("            -    EN  "+str(cpes_lastmodified2022_refsymbiote_iot)+" REFERENCIAS LA FUENTE ES SYMBIOTE.COM ")
print("            -    EN  "+str(cpes_lastmodified2022_refasus_iot)+" REFERENCIAS LA FUENTE ES ASUS.COM ")
print("            -    EN  "+str(cpes_lastmodified2022_refiotkonker_iot)+" REFERENCIAS LA FUENTE ES IOT.KONKER ")
print("            -    EN  "+str(cpes_lastmodified2022_refvulncheck_iot)+" REFERENCIAS LA FUENTE ES VULNCHECK.COM ")
print("            -    EN  "+str(cpes_lastmodified2022_refxiongmaitech_iot)+" REFERENCIAS LA FUENTE ES XIONGMAITECH.COM ")
print("            -    EN  "+str(cpes_lastmodified2022_refmicrosoft_iot)+" REFERENCIAS LA FUENTE ES MICROSOFT.COM ")
print("            -    EN  "+str(cpes_lastmodified2022_refriot_iot)+" REFERENCIAS LA FUENTE ES RIOT-OS.ORG ")
print("\n")
print("      -    EN  "+str(cpes_lastmodified2021_iot)+" REFERENCIAS DE CPES LA FECHA DE MODIFICACION ES 2021. LAS ESTADÍSTICAS DE FUENTE DE REFERENCIA SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(cpes_lastmodified2021_refgithub_iot)+" REFERENCIAS LA FUENTE ES GITHUB.COM ")
print("            -    EN  "+str(cpes_lastmodified2021_refptc_iot)+" REFERENCIAS LA FUENTE ES PTC.COM ")
print("            -    EN  "+str(cpes_lastmodified2021_refsymbiote_iot)+" REFERENCIAS LA FUENTE ES SYMBIOTE.COM ")
print("            -    EN  "+str(cpes_lastmodified2021_refasus_iot)+" REFERENCIAS LA FUENTE ES ASUS.COM ")
print("            -    EN  "+str(cpes_lastmodified2021_refiotkonker_iot)+" REFERENCIAS LA FUENTE ES IOT.KONKER ")
print("            -    EN  "+str(cpes_lastmodified2021_refvulncheck_iot)+" REFERENCIAS LA FUENTE ES VULNCHECK.COM ")
print("            -    EN  "+str(cpes_lastmodified2021_refxiongmaitech_iot)+" REFERENCIAS LA FUENTE ES XIONGMAITECH.COM ")
print("            -    EN  "+str(cpes_lastmodified2021_refmicrosoft_iot)+" REFERENCIAS LA FUENTE ES MICROSOFT.COM ")
print("            -    EN  "+str(cpes_lastmodified2021_refriot_iot)+" REFERENCIAS LA FUENTE ES RIOT-OS.ORG ")
print("\n")
print("      -    EN  "+str(cpes_lastmodified2020_iot)+" REFERENCIAS DE CPES LA FECHA DE MODIFICACION ES 2020. LAS ESTADÍSTICAS DE FUENTE DE REFERENCIA SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(cpes_lastmodified2020_refgithub_iot)+" REFERENCIAS LA FUENTE ES GITHUB.COM ")
print("            -    EN  "+str(cpes_lastmodified2020_refptc_iot)+" REFERENCIAS LA FUENTE ES PTC.COM ")
print("            -    EN  "+str(cpes_lastmodified2020_refsymbiote_iot)+" REFERENCIAS LA FUENTE ES SYMBIOTE.COM ")
print("            -    EN  "+str(cpes_lastmodified2020_refasus_iot)+" REFERENCIAS LA FUENTE ES ASUS.COM ")
print("            -    EN  "+str(cpes_lastmodified2020_refiotkonker_iot)+" REFERENCIAS LA FUENTE ES IOT.KONKER ")
print("            -    EN  "+str(cpes_lastmodified2020_refvulncheck_iot)+" REFERENCIAS LA FUENTE ES VULNCHECK.COM ")
print("            -    EN  "+str(cpes_lastmodified2020_refxiongmaitech_iot)+" REFERENCIAS LA FUENTE ES XIONGMAITECH.COM ")
print("            -    EN  "+str(cpes_lastmodified2020_refmicrosoft_iot)+" REFERENCIAS LA FUENTE ES MICROSOFT.COM ")
print("            -    EN  "+str(cpes_lastmodified2020_refriot_iot)+" REFERENCIAS LA FUENTE ES RIOT-OS.ORG ")
print("\n")
print("      -    EN  "+str(cpes_lastmodified2019_iot)+" REFERENCIAS DE CPES LA FECHA DE MODIFICACION ES 2019. LAS ESTADÍSTICAS DE FUENTE DE REFERENCIA SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(cpes_lastmodified2019_refgithub_iot)+" REFERENCIAS LA FUENTE ES GITHUB.COM ")
print("            -    EN  "+str(cpes_lastmodified2019_refptc_iot)+" REFERENCIAS LA FUENTE ES PTC.COM ")
print("            -    EN  "+str(cpes_lastmodified2019_refsymbiote_iot)+" REFERENCIAS LA FUENTE ES SYMBIOTE.COM ")
print("            -    EN  "+str(cpes_lastmodified2019_refasus_iot)+" REFERENCIAS LA FUENTE ES ASUS.COM ")
print("            -    EN  "+str(cpes_lastmodified2019_refiotkonker_iot)+" REFERENCIAS LA FUENTE ES IOT.KONKER ")
print("            -    EN  "+str(cpes_lastmodified2019_refvulncheck_iot)+" REFERENCIAS LA FUENTE ES VULNCHECK.COM ")
print("            -    EN  "+str(cpes_lastmodified2019_refxiongmaitech_iot)+" REFERENCIAS LA FUENTE ES XIONGMAITECH.COM ")
print("            -    EN  "+str(cpes_lastmodified2019_refmicrosoft_iot)+" REFERENCIAS LA FUENTE ES MICROSOFT.COM ")
print("            -    EN  "+str(cpes_lastmodified2019_refriot_iot)+" REFERENCIAS LA FUENTE ES RIOT-OS.ORG ")
print("\n")
print("      -    EN  "+str(cpes_lastmodified2018_iot)+" REFERENCIAS DE CPES LA FECHA DE MODIFICACION ES 2018 O ANTERIOR. LAS ESTADÍSTICAS DE FUENTE DE REFERENCIA SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(cpes_lastmodified2018_refgithub_iot)+" REFERENCIAS LA FUENTE ES GITHUB.COM ")
print("            -    EN  "+str(cpes_lastmodified2018_refptc_iot)+" REFERENCIAS LA FUENTE ES PTC.COM ")
print("            -    EN  "+str(cpes_lastmodified2018_refsymbiote_iot)+" REFERENCIAS LA FUENTE ES SYMBIOTE.COM ")
print("            -    EN  "+str(cpes_lastmodified2018_refasus_iot)+" REFERENCIAS LA FUENTE ES ASUS.COM ")
print("            -    EN  "+str(cpes_lastmodified2018_refiotkonker_iot)+" REFERENCIAS LA FUENTE ES IOT.KONKER ")
print("            -    EN  "+str(cpes_lastmodified2018_refvulncheck_iot)+" REFERENCIAS LA FUENTE ES VULNCHECK.COM ")
print("            -    EN  "+str(cpes_lastmodified2018_refxiongmaitech_iot)+" REFERENCIAS LA FUENTE ES XIONGMAITECH.COM ")
print("            -    EN  "+str(cpes_lastmodified2018_refmicrosoft_iot)+" REFERENCIAS LA FUENTE ES MICROSOFT.COM ")
print("            -    EN  "+str(cpes_lastmodified2018_refriot_iot)+" REFERENCIAS LA FUENTE ES RIOT-OS.ORG ")
print("\n")










print("********************************PORCENTAJES FECHA DE ULTIMA MODIFICACION CPE/FUENTE DE REFERENCIA CPE PARTE IOT********************************")
print("\n")        
            
          
    
print("\n")
print(" DE UN TOTAL DE "+str(counterrefs_iot)+" REFERENCIAS DE CPES , LOS PORCENTAJES DE RELACION DE FECHA DE MODIFICACION Y FUENTE DE REFERENCIA SON LOS SIGUIENTES:  \n")
print("\n")
print("\n")
print("      -    EN  EL "+str(float(((cpes_refgithub_iot*100)/counterrefs_iot)))+" % DE REFERENCIAS LA FUENTE ES GITHUB.COM  \n")
print("      -    EN  EL "+str(float(((cpes_refptc_iot*100)/counterrefs_iot)))+" % DE REFERENCIAS LA FUENTE ES PTC.COM  \n")
print("      -    EN  EL "+str(float(((cpes_refsymbiote_iot*100)/counterrefs_iot)))+" % DE REFERENCIAS LA FUENTE ES SYMBIOTE.COM  \n")
print("      -    EN  EL "+str(float(((cpes_refasus_iot*100)/counterrefs_iot)))+" % DE REFERENCIAS LA FUENTE ES ASUS.COM  \n")
print("      -    EN  EL "+str(float(((cpes_refiotkonker_iot*100)/counterrefs_iot)))+" % DE REFERENCIAS LA FUENTE ES IOT.KONKER  \n")
print("      -    EN  EL "+str(float(((cpes_refvulncheck_iot*100)/counterrefs_iot)))+" % DE REFERENCIAS LA FUENTE ES VULNCHECK.COM  \n")
print("      -    EN  EL "+str(float(((cpes_refxiongmaitech_iot*100)/counterrefs_iot)))+" % DE REFERENCIAS LA FUENTE ES XIONGMAITECH.COM  \n")
print("      -    EN  EL "+str(float(((cpes_refmicrosoft_iot*100)/counterrefs_iot)))+" % DE REFERENCIAS LA FUENTE ES MICROSOFT.COM  \n")
print("      -    EN  EL "+str(float(((cpes_refriot_iot*100)/counterrefs_iot)))+" % DE REFERENCIAS LA FUENTE ES RIOT-OS.ORG  \n")
print("\n")
print("      -    EN EL "+str(float(((cpes_lastmodified2023_iot*100)/counterrefs_iot)))+" % DE REFERENCIAS DE CPES LA FECHA DE MODIFICACION ES 2023. LOS PORCENTAJES DE FUENTE DE REFERENCIA SON LOS SIGUIENTES:  \n")
print("\n")
print("            -    EN EL "+str(float(((cpes_lastmodified2023_refgithub_iot*100)/cpes_lastmodified2023_iot)))+" % DE REFERENCIAS LA FUENTE ES GITHUB.COM  ")
print("            -    EN EL "+str(float(((cpes_lastmodified2023_refptc_iot*100)/cpes_lastmodified2023_iot)))+" % DE REFERENCIAS LA FUENTE ES PTC.COMO ")
print("            -    EN EL "+str(float(((cpes_lastmodified2023_refsymbiote_iot*100)/cpes_lastmodified2023_iot)))+" % DE REFERENCIAS LA FUENTE ES SYMBIOTE.COM ")
print("            -    EN EL "+str(float(((cpes_lastmodified2023_refasus_iot*100)/cpes_lastmodified2023_iot)))+" % DE REFERENCIAS LA FUENTE ES ASUS.COM ")
print("            -    EN EL "+str(float(((cpes_lastmodified2023_refiotkonker_iot*100)/cpes_lastmodified2023_iot)))+" % DE REFERENCIAS LA FUENTE ES IOT.KONKER ")
print("            -    EN EL "+str(float(((cpes_lastmodified2023_refvulncheck_iot*100)/cpes_lastmodified2023_iot)))+" % DE REFERENCIAS LA FUENTE ES VULNCHECK.COM ")
print("            -    EN EL "+str(float(((cpes_lastmodified2023_refxiongmaitech_iot*100)/cpes_lastmodified2023_iot)))+" % DE REFERENCIAS LA FUENTE ES XIONGMAITECH.COM ")
print("            -    EN EL "+str(float(((cpes_lastmodified2023_refmicrosoft_iot*100)/cpes_lastmodified2023_iot)))+" % DE REFERENCIAS LA FUENTE ES MICROSOFT.COM ")
print("            -    EN EL "+str(float(((cpes_lastmodified2023_refriot_iot*100)/cpes_lastmodified2023_iot)))+" % DE REFERENCIAS LA FUENTE ES RIOT-OS.ORG ")
print("\n")
print("      -    EN EL "+str(float(((cpes_lastmodified2022_iot*100)/counterrefs_iot)))+" % DE REFERENCIAS DE CPES LA FECHA DE MODIFICACION ES 2022. LOS PORCENTAJES DE FUENTE DE REFERENCIA SON LOS SIGUIENTES:  \n")
print("\n")
print("            -    EN EL "+str(float(((cpes_lastmodified2022_refgithub_iot*100)/cpes_lastmodified2022_iot)))+" % DE REFERENCIAS LA FUENTE ES GITHUB.COM  ")
print("            -    EN EL "+str(float(((cpes_lastmodified2022_refptc_iot*100)/cpes_lastmodified2022_iot)))+" % DE REFERENCIAS LA FUENTE ES PTC.COMO ")
print("            -    EN EL "+str(float(((cpes_lastmodified2022_refsymbiote_iot*100)/cpes_lastmodified2022_iot)))+" % DE REFERENCIAS LA FUENTE ES SYMBIOTE.COM ")
print("            -    EN EL "+str(float(((cpes_lastmodified2022_refasus_iot*100)/cpes_lastmodified2022_iot)))+" % DE REFERENCIAS LA FUENTE ES ASUS.COM ")
print("            -    EN EL "+str(float(((cpes_lastmodified2022_refiotkonker_iot*100)/cpes_lastmodified2022_iot)))+" % DE REFERENCIAS LA FUENTE ES IOT.KONKER ")
print("            -    EN EL "+str(float(((cpes_lastmodified2022_refvulncheck_iot*100)/cpes_lastmodified2022_iot)))+" % DE REFERENCIAS LA FUENTE ES VULNCHECK.COM ")
print("            -    EN EL "+str(float(((cpes_lastmodified2022_refxiongmaitech_iot*100)/cpes_lastmodified2022_iot)))+" % DE REFERENCIAS LA FUENTE ES XIONGMAITECH.COM ")
print("            -    EN EL "+str(float(((cpes_lastmodified2022_refmicrosoft_iot*100)/cpes_lastmodified2022_iot)))+" % DE REFERENCIAS LA FUENTE ES MICROSOFT.COM ")
print("            -    EN EL "+str(float(((cpes_lastmodified2022_refriot_iot*100)/cpes_lastmodified2022_iot)))+" % DE REFERENCIAS LA FUENTE ES RIOT-OS.ORG ")
print("\n")
print("      -    EN EL "+str(float(((cpes_lastmodified2021_iot*100)/counterrefs_iot)))+" % DE REFERENCIAS DE CPES LA FECHA DE MODIFICACION ES 2021. LOS PORCENTAJES DE FUENTE DE REFERENCIA SON LOS SIGUIENTES:  \n")
print("\n")
print("            -    EN EL "+str(float(((cpes_lastmodified2021_refgithub_iot*100)/cpes_lastmodified2021_iot)))+" % DE REFERENCIAS LA FUENTE ES GITHUB.COM  ")
print("            -    EN EL "+str(float(((cpes_lastmodified2021_refptc_iot*100)/cpes_lastmodified2021_iot)))+" % DE REFERENCIAS LA FUENTE ES PTC.COMO ")
print("            -    EN EL "+str(float(((cpes_lastmodified2021_refsymbiote_iot*100)/cpes_lastmodified2021_iot)))+" % DE REFERENCIAS LA FUENTE ES SYMBIOTE.COM ")
print("            -    EN EL "+str(float(((cpes_lastmodified2021_refasus_iot*100)/cpes_lastmodified2021_iot)))+" % DE REFERENCIAS LA FUENTE ES ASUS.COM ")
print("            -    EN EL "+str(float(((cpes_lastmodified2021_refiotkonker_iot*100)/cpes_lastmodified2021_iot)))+" % DE REFERENCIAS LA FUENTE ES IOT.KONKER ")
print("            -    EN EL "+str(float(((cpes_lastmodified2021_refvulncheck_iot*100)/cpes_lastmodified2021_iot)))+" % DE REFERENCIAS LA FUENTE ES VULNCHECK.COM ")
print("            -    EN EL "+str(float(((cpes_lastmodified2021_refxiongmaitech_iot*100)/cpes_lastmodified2021_iot)))+" % DE REFERENCIAS LA FUENTE ES XIONGMAITECH.COM ")
print("            -    EN EL "+str(float(((cpes_lastmodified2021_refmicrosoft_iot*100)/cpes_lastmodified2021_iot)))+" % DE REFERENCIAS LA FUENTE ES MICROSOFT.COM ")
print("            -    EN EL "+str(float(((cpes_lastmodified2021_refriot_iot*100)/cpes_lastmodified2021_iot)))+" % DE REFERENCIAS LA FUENTE ES RIOT-OS.ORG ")
print("\n")
print("      -    EN EL "+str(float(((cpes_lastmodified2020_iot*100)/counterrefs_iot)))+" % DE REFERENCIAS DE CPES LA FECHA DE MODIFICACION ES 2020. LOS PORCENTAJES DE FUENTE DE REFERENCIA SON LOS SIGUIENTES:  \n")
print("\n")
print("            -    EN EL "+str(float(((cpes_lastmodified2020_refgithub_iot*100)/cpes_lastmodified2020_iot)))+" % DE REFERENCIAS LA FUENTE ES GITHUB.COM  ")
print("            -    EN EL "+str(float(((cpes_lastmodified2020_refptc_iot*100)/cpes_lastmodified2020_iot)))+" % DE REFERENCIAS LA FUENTE ES PTC.COMO ")
print("            -    EN EL "+str(float(((cpes_lastmodified2020_refsymbiote_iot*100)/cpes_lastmodified2020_iot)))+" % DE REFERENCIAS LA FUENTE ES SYMBIOTE.COM ")
print("            -    EN EL "+str(float(((cpes_lastmodified2020_refasus_iot*100)/cpes_lastmodified2020_iot)))+" % DE REFERENCIAS LA FUENTE ES ASUS.COM ")
print("            -    EN EL "+str(float(((cpes_lastmodified2020_refiotkonker_iot*100)/cpes_lastmodified2020_iot)))+" % DE REFERENCIAS LA FUENTE ES IOT.KONKER ")
print("            -    EN EL "+str(float(((cpes_lastmodified2020_refvulncheck_iot*100)/cpes_lastmodified2020_iot)))+" % DE REFERENCIAS LA FUENTE ES VULNCHECK.COM ")
print("            -    EN EL "+str(float(((cpes_lastmodified2020_refxiongmaitech_iot*100)/cpes_lastmodified2020_iot)))+" % DE REFERENCIAS LA FUENTE ES XIONGMAITECH.COM ")
print("            -    EN EL "+str(float(((cpes_lastmodified2020_refmicrosoft_iot*100)/cpes_lastmodified2020_iot)))+" % DE REFERENCIAS LA FUENTE ES MICROSOFT.COM ")
print("            -    EN EL "+str(float(((cpes_lastmodified2020_refriot_iot*100)/cpes_lastmodified2020_iot)))+" % DE REFERENCIAS LA FUENTE ES RIOT-OS.ORG ")
print("\n")
print("      -    EN EL "+str(float(((cpes_lastmodified2019_iot*100)/counterrefs_iot)))+" % DE REFERENCIAS DE CPES LA FECHA DE MODIFICACION ES 2019. LOS PORCENTAJES DE FUENTE DE REFERENCIA SON LOS SIGUIENTES:  \n")
print("\n")
print("            -    EN EL "+str(float(((cpes_lastmodified2019_refgithub_iot*100)/cpes_lastmodified2019_iot)))+" % DE REFERENCIAS LA FUENTE ES GITHUB.COM  ")
print("            -    EN EL "+str(float(((cpes_lastmodified2019_refptc_iot*100)/cpes_lastmodified2019_iot)))+" % DE REFERENCIAS LA FUENTE ES PTC.COMO ")
print("            -    EN EL "+str(float(((cpes_lastmodified2019_refsymbiote_iot*100)/cpes_lastmodified2019_iot)))+" % DE REFERENCIAS LA FUENTE ES SYMBIOTE.COM ")
print("            -    EN EL "+str(float(((cpes_lastmodified2019_refasus_iot*100)/cpes_lastmodified2019_iot)))+" % DE REFERENCIAS LA FUENTE ES ASUS.COM ")
print("            -    EN EL "+str(float(((cpes_lastmodified2019_refiotkonker_iot*100)/cpes_lastmodified2019_iot)))+" % DE REFERENCIAS LA FUENTE ES IOT.KONKER ")
print("            -    EN EL "+str(float(((cpes_lastmodified2019_refvulncheck_iot*100)/cpes_lastmodified2019_iot)))+" % DE REFERENCIAS LA FUENTE ES VULNCHECK.COM ")
print("            -    EN EL "+str(float(((cpes_lastmodified2019_refxiongmaitech_iot*100)/cpes_lastmodified2019_iot)))+" % DE REFERENCIAS LA FUENTE ES XIONGMAITECH.COM ")
print("            -    EN EL "+str(float(((cpes_lastmodified2019_refmicrosoft_iot*100)/cpes_lastmodified2019_iot)))+" % DE REFERENCIAS LA FUENTE ES MICROSOFT.COM ")
print("            -    EN EL "+str(float(((cpes_lastmodified2019_refriot_iot*100)/cpes_lastmodified2019_iot)))+" % DE REFERENCIAS LA FUENTE ES RIOT-OS.ORG ")
print("\n")
print("      -    EN EL "+str(float(((cpes_lastmodified2018_iot*100)/counterrefs_iot)))+" % DE REFERENCIAS DE CPES LA FECHA DE MODIFICACION ES 2018 O ANTERIOR. LOS PORCENTAJES DE FUENTE DE REFERENCIA SON LOS SIGUIENTES:  \n")
print("\n")
print("            -    EN EL "+str(float(((cpes_lastmodified2018_refgithub_iot*100)/cpes_lastmodified2018_iot)))+" % DE REFERENCIAS LA FUENTE ES GITHUB.COM  ")
print("            -    EN EL "+str(float(((cpes_lastmodified2018_refptc_iot*100)/cpes_lastmodified2018_iot)))+" % DE REFERENCIAS LA FUENTE ES PTC.COMO ")
print("            -    EN EL "+str(float(((cpes_lastmodified2018_refsymbiote_iot*100)/cpes_lastmodified2018_iot)))+" % DE REFERENCIAS LA FUENTE ES SYMBIOTE.COM ")
print("            -    EN EL "+str(float(((cpes_lastmodified2018_refasus_iot*100)/cpes_lastmodified2018_iot)))+" % DE REFERENCIAS LA FUENTE ES ASUS.COM ")
print("            -    EN EL "+str(float(((cpes_lastmodified2018_refiotkonker_iot*100)/cpes_lastmodified2018_iot)))+" % DE REFERENCIAS LA FUENTE ES IOT.KONKER ")
print("            -    EN EL "+str(float(((cpes_lastmodified2018_refvulncheck_iot*100)/cpes_lastmodified2018_iot)))+" % DE REFERENCIAS LA FUENTE ES VULNCHECK.COM ")
print("            -    EN EL "+str(float(((cpes_lastmodified2018_refxiongmaitech_iot*100)/cpes_lastmodified2018_iot)))+" % DE REFERENCIAS LA FUENTE ES XIONGMAITECH.COM ")
print("            -    EN EL "+str(float(((cpes_lastmodified2018_refmicrosoft_iot*100)/cpes_lastmodified2018_iot)))+" % DE REFERENCIAS LA FUENTE ES MICROSOFT.COM ")
print("            -    EN EL "+str(float(((cpes_lastmodified2018_refriot_iot*100)/cpes_lastmodified2018_iot)))+" % DE REFERENCIAS LA FUENTE ES RIOT-OS.ORG ")
print("\n")
















print("********************************FECHA DE ULTIMA MODIFICACION DE CPE/FUENTE DE REFERENCIA ASOCIADA A CPE PARTE SMART HOME********************************")
print("\n")
print("\n")

#Contador de referencias existentes
counterrefs_sh=0
#Contador de referencias modificadas en un anio especifico
cpes_lastmodified2023_sh=0
#Contador de distintas referencias segun un anio de modificacion
cpes_lastmodified2023_refapple_sh=0
cpes_lastmodified2023_refcisco_sh=0
cpes_lastmodified2023_refbosch_sh=0
cpes_lastmodified2023_refcoolkit_sh=0
cpes_lastmodified2023_refinimbiz_sh=0
cpes_lastmodified2023_refidec_sh=0
cpes_lastmodified2023_refgoogle_sh=0
cpes_lastmodified2023_refdocbmc_sh=0


cpes_lastmodified2022_sh=0
cpes_lastmodified2022_refapple_sh=0
cpes_lastmodified2022_refcisco_sh=0
cpes_lastmodified2022_refbosch_sh=0
cpes_lastmodified2022_refcoolkit_sh=0
cpes_lastmodified2022_refinimbiz_sh=0
cpes_lastmodified2022_refidec_sh=0
cpes_lastmodified2022_refgoogle_sh=0
cpes_lastmodified2022_refdocbmc_sh=0



cpes_lastmodified2021_sh=0
cpes_lastmodified2021_refapple_sh=0
cpes_lastmodified2021_refcisco_sh=0
cpes_lastmodified2021_refbosch_sh=0
cpes_lastmodified2021_refcoolkit_sh=0
cpes_lastmodified2021_refinimbiz_sh=0
cpes_lastmodified2021_refidec_sh=0
cpes_lastmodified2021_refgoogle_sh=0
cpes_lastmodified2021_refdocbmc_sh=0



cpes_lastmodified2020_sh=0
cpes_lastmodified2020_refapple_sh=0
cpes_lastmodified2020_refcisco_sh=0
cpes_lastmodified2020_refbosch_sh=0
cpes_lastmodified2020_refcoolkit_sh=0
cpes_lastmodified2020_refinimbiz_sh=0
cpes_lastmodified2020_refidec_sh=0
cpes_lastmodified2020_refgoogle_sh=0
cpes_lastmodified2020_refdocbmc_sh=0


cpes_lastmodified2019_sh=0
cpes_lastmodified2019_refapple_sh=0
cpes_lastmodified2019_refcisco_sh=0
cpes_lastmodified2019_refbosch_sh=0
cpes_lastmodified2019_refcoolkit_sh=0
cpes_lastmodified2019_refinimbiz_sh=0
cpes_lastmodified2019_refidec_sh=0
cpes_lastmodified2019_refgoogle_sh=0
cpes_lastmodified2019_refdocbmc_sh=0


cpes_lastmodified2018_sh=0
cpes_lastmodified2018_refapple_sh=0
cpes_lastmodified2018_refcisco_sh=0
cpes_lastmodified2018_refbosch_sh=0
cpes_lastmodified2018_refcoolkit_sh=0
cpes_lastmodified2018_refinimbiz_sh=0
cpes_lastmodified2018_refidec_sh=0
cpes_lastmodified2018_refgoogle_sh=0
cpes_lastmodified2018_refdocbmc_sh=0








#Recorro los valores de fecha de modificacion
for r in range(0,len(df_cpe_sh["cpes.lastModifiedDate"])):
    str_anio_modifdate_cpe_sh=df_cpe_sh["cpes.lastModifiedDate"][r].split("-")
    anio_modifdate_cpe_sh=int(str_anio_modifdate_cpe_sh[0])
    if(anio_modifdate_cpe_sh >= 2023):
        #Si existen varios valores de referencia para una misma fecha de modificacion en una misma fila
        if('[' in df_cpe_sh["cpes.refs.ref"][r]):
            aux=df_cpe_sh["cpes.refs.ref"][r].split(",")
            #Recorro los valores de referencia
            for k in range(0,len(aux)):
                if(len(aux)>0):
                    cpes_lastmodified2023_sh+=1
                    counterrefs_sh+=1
                    #Obtengo el valor de la referencia
                    aux_str=aux[k].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
                    if('apple' in aux_str):
                        cpes_lastmodified2023_refapple_sh+=1   
                    elif('cisco' in aux_str):
                        cpes_lastmodified2023_refcisco_sh+=1
                    elif('bosch' in aux_str):
                        cpes_lastmodified2023_refbosch_sh+=1   
                    elif('coolkit' in aux_str):
                        cpes_lastmodified2023_refcoolkit_sh+=1    
                    elif('inim.biz' in aux_str):
                        cpes_lastmodified2023_refinimbiz_sh+=1    
                    elif('idec' in aux_str):
                        cpes_lastmodified2023_refidec_sh+=1    
                    elif('google' in aux_str):
                        cpes_lastmodified2023_refgoogle_sh+=1    
                    elif('docs.bmc' in aux_str):
                        cpes_lastmodified2023_refdocbmc_sh+=1    
        else:
            counterrefs_sh+=1
            cpes_lastmodified2023_sh+=1
            if('apple' in df_cpe_sh["cpes.refs.ref"][r]):
                cpes_lastmodified2023_refapple_sh+=1   
            elif('cisco' in df_cpe_sh["cpes.refs.ref"][r]):
                cpes_lastmodified2023_refcisco_sh+=1
            elif('bosch' in df_cpe_sh["cpes.refs.ref"][r]):
                cpes_lastmodified2023_refbosch_sh+=1
            elif('coolkit' in df_cpe_sh["cpes.refs.ref"][r]):
                cpes_lastmodified2023_refcoolkit_sh+=1
            elif('inim.biz' in df_cpe_sh["cpes.refs.ref"][r]):
                cpes_lastmodified2023_refinimbiz_sh+=1
            elif('idec' in df_cpe_sh["cpes.refs.ref"][r]):
                cpes_lastmodified2023_refidec_sh+=1
            elif('google' in df_cpe_sh["cpes.refs.ref"][r]):
                cpes_lastmodified2023_refgoogle_sh+=1
            elif('docs.bmc' in df_cpe_sh["cpes.refs.ref"][r]):
                cpes_lastmodified2023_refdocbmc_sh+=1
        
        
    elif(anio_modifdate_cpe_sh >= 2022):
        if('[' in df_cpe_sh["cpes.refs.ref"][r]):
            aux=df_cpe_sh["cpes.refs.ref"][r].split(",")
            for k in range(0,len(aux)):
                if(len(aux)>0):
                    cpes_lastmodified2022_sh+=1
                    counterrefs_sh+=1
                    aux_str=aux[k].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
                    if('apple' in aux_str):
                        cpes_lastmodified2022_refapple_sh+=1   
                    elif('cisco' in aux_str):
                        cpes_lastmodified2022_refcisco_sh+=1
                    elif('bosch' in aux_str):
                        cpes_lastmodified2022_refbosch_sh+=1   
                    elif('coolkit' in aux_str):
                        cpes_lastmodified2022_refcoolkit_sh+=1    
                    elif('inim.biz' in aux_str):
                        cpes_lastmodified2022_refinimbiz_sh+=1    
                    elif('idec' in aux_str):
                        cpes_lastmodified2022_refidec_sh+=1    
                    elif('google' in aux_str):
                        cpes_lastmodified2022_refgoogle_sh+=1    
                    elif('docs.bmc' in aux_str):
                        cpes_lastmodified2022_refdocbmc_sh+=1    
        else:
            counterrefs_sh+=1
            cpes_lastmodified2022_sh+=1
            if('apple' in df_cpe_sh["cpes.refs.ref"][r]):
                cpes_lastmodified2022_refapple_sh+=1   
            elif('cisco' in df_cpe_sh["cpes.refs.ref"][r]):
                cpes_lastmodified2022_refcisco_sh+=1
            elif('bosch' in df_cpe_sh["cpes.refs.ref"][r]):
                cpes_lastmodified2022_refbosch_sh+=1
            elif('coolkit' in df_cpe_sh["cpes.refs.ref"][r]):
                cpes_lastmodified2022_refcoolkit_sh+=1
            elif('inim.biz' in df_cpe_sh["cpes.refs.ref"][r]):
                cpes_lastmodified2022_refinimbiz_sh+=1
            elif('idec' in df_cpe_sh["cpes.refs.ref"][r]):
                cpes_lastmodified2022_refidec_sh+=1
            elif('google' in df_cpe_sh["cpes.refs.ref"][r]):
                cpes_lastmodified2022_refgoogle_sh+=1
            elif('docs.bmc' in df_cpe_sh["cpes.refs.ref"][r]):
                cpes_lastmodified2022_refdocbmc_sh+=1
   
    elif(anio_modifdate_cpe_sh >= 2021):
        if('[' in df_cpe_sh["cpes.refs.ref"][r]):
            aux=df_cpe_sh["cpes.refs.ref"][r].split(",")
            for k in range(0,len(aux)):
                if(len(aux)>0):
                    cpes_lastmodified2021_sh+=1
                    counterrefs_sh+=1
                    aux_str=aux[k].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
                    if('apple' in aux_str):
                        cpes_lastmodified2021_refapple_sh+=1   
                    elif('cisco' in aux_str):
                        cpes_lastmodified2021_refcisco_sh+=1
                    elif('bosch' in aux_str):
                        cpes_lastmodified2021_refbosch_sh+=1   
                    elif('coolkit' in aux_str):
                        cpes_lastmodified2021_refcoolkit_sh+=1    
                    elif('inim.biz' in aux_str):
                        cpes_lastmodified2021_refinimbiz_sh+=1    
                    elif('idec' in aux_str):
                        cpes_lastmodified2021_refidec_sh+=1    
                    elif('google' in aux_str):
                        cpes_lastmodified2021_refgoogle_sh+=1    
                    elif('docs.bmc' in aux_str):
                        cpes_lastmodified2021_refdocbmc_sh+=1    
        else:
            counterrefs_sh+=1
            cpes_lastmodified2021_sh+=1
            if('apple' in df_cpe_sh["cpes.refs.ref"][r]):
                cpes_lastmodified2021_refapple_sh+=1   
            elif('cisco' in df_cpe_sh["cpes.refs.ref"][r]):
                cpes_lastmodified2021_refcisco_sh+=1
            elif('bosch' in df_cpe_sh["cpes.refs.ref"][r]):
                cpes_lastmodified2021_refbosch_sh+=1
            elif('coolkit' in df_cpe_sh["cpes.refs.ref"][r]):
                cpes_lastmodified2021_refcoolkit_sh+=1
            elif('inim.biz' in df_cpe_sh["cpes.refs.ref"][r]):
                cpes_lastmodified2021_refinimbiz_sh+=1
            elif('idec' in df_cpe_sh["cpes.refs.ref"][r]):
                cpes_lastmodified2021_refidec_sh+=1
            elif('google' in df_cpe_sh["cpes.refs.ref"][r]):
                cpes_lastmodified2021_refgoogle_sh+=1
            elif('docs.bmc' in df_cpe_sh["cpes.refs.ref"][r]):
                cpes_lastmodified2021_refdocbmc_sh+=1
   
    elif(anio_modifdate_cpe_sh >= 2020):
        if('[' in df_cpe_sh["cpes.refs.ref"][r]):
            aux=df_cpe_sh["cpes.refs.ref"][r].split(",")
            for k in range(0,len(aux)):
                if(len(aux)>0):
                    cpes_lastmodified2020_sh+=1
                    counterrefs_sh+=1
                    aux_str=aux[k].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
                    if('apple' in aux_str):
                        cpes_lastmodified2020_refapple_sh+=1   
                    elif('cisco' in aux_str):
                        cpes_lastmodified2020_refcisco_sh+=1
                    elif('bosch' in aux_str):
                        cpes_lastmodified2020_refbosch_sh+=1   
                    elif('coolkit' in aux_str):
                        cpes_lastmodified2020_refcoolkit_sh+=1    
                    elif('inim.biz' in aux_str):
                        cpes_lastmodified2020_refinimbiz_sh+=1    
                    elif('idec' in aux_str):
                        cpes_lastmodified2020_refidec_sh+=1    
                    elif('google' in aux_str):
                        cpes_lastmodified2020_refgoogle_sh+=1    
                    elif('docs.bmc' in aux_str):
                        cpes_lastmodified2020_refdocbmc_sh+=1    
        else:
            counterrefs_sh+=1
            cpes_lastmodified2020_sh+=1
            if('apple' in df_cpe_sh["cpes.refs.ref"][r]):
                cpes_lastmodified2020_refapple_sh+=1   
            elif('cisco' in df_cpe_sh["cpes.refs.ref"][r]):
                cpes_lastmodified2020_refcisco_sh+=1
            elif('bosch' in df_cpe_sh["cpes.refs.ref"][r]):
                cpes_lastmodified2020_refbosch_sh+=1
            elif('coolkit' in df_cpe_sh["cpes.refs.ref"][r]):
                cpes_lastmodified2020_refcoolkit_sh+=1
            elif('inim.biz' in df_cpe_sh["cpes.refs.ref"][r]):
                cpes_lastmodified2020_refinimbiz_sh+=1
            elif('idec' in df_cpe_sh["cpes.refs.ref"][r]):
                cpes_lastmodified2020_refidec_sh+=1
            elif('google' in df_cpe_sh["cpes.refs.ref"][r]):
                cpes_lastmodified2020_refgoogle_sh+=1
            elif('docs.bmc' in df_cpe_sh["cpes.refs.ref"][r]):
                cpes_lastmodified2020_refdocbmc_sh+=1
   
    elif(anio_modifdate_cpe_sh >= 2019):
        if('[' in df_cpe_sh["cpes.refs.ref"][r]):
            aux=df_cpe_sh["cpes.refs.ref"][r].split(",")
            for k in range(0,len(aux)):
                if(len(aux)>0):
                    cpes_lastmodified2019_sh+=1
                    counterrefs_sh+=1
                    aux_str=aux[k].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
                    if('apple' in aux_str):
                        cpes_lastmodified2019_refapple_sh+=1   
                    elif('cisco' in aux_str):
                        cpes_lastmodified2019_refcisco_sh+=1
                    elif('bosch' in aux_str):
                        cpes_lastmodified2019_refbosch_sh+=1   
                    elif('coolkit' in aux_str):
                        cpes_lastmodified2019_refcoolkit_sh+=1    
                    elif('inim.biz' in aux_str):
                        cpes_lastmodified2019_refinimbiz_sh+=1    
                    elif('idec' in aux_str):
                        cpes_lastmodified2019_refidec_sh+=1    
                    elif('google' in aux_str):
                        cpes_lastmodified2019_refgoogle_sh+=1    
                    elif('docs.bmc' in aux_str):
                        cpes_lastmodified2019_refdocbmc_sh+=1    
        else:
            counterrefs_sh+=1
            cpes_lastmodified2019_sh+=1
            if('apple' in df_cpe_sh["cpes.refs.ref"][r]):
                cpes_lastmodified2019_refapple_sh+=1   
            elif('cisco' in df_cpe_sh["cpes.refs.ref"][r]):
                cpes_lastmodified2019_refcisco_sh+=1
            elif('bosch' in df_cpe_sh["cpes.refs.ref"][r]):
                cpes_lastmodified2019_refbosch_sh+=1
            elif('coolkit' in df_cpe_sh["cpes.refs.ref"][r]):
                cpes_lastmodified2019_refcoolkit_sh+=1
            elif('inim.biz' in df_cpe_sh["cpes.refs.ref"][r]):
                cpes_lastmodified2019_refinimbiz_sh+=1
            elif('idec' in df_cpe_sh["cpes.refs.ref"][r]):
                cpes_lastmodified2019_refidec_sh+=1
            elif('google' in df_cpe_sh["cpes.refs.ref"][r]):
                cpes_lastmodified2019_refgoogle_sh+=1
            elif('docs.bmc' in df_cpe_sh["cpes.refs.ref"][r]):
                cpes_lastmodified2019_refdocbmc_sh+=1
                
    else:
        if('[' in df_cpe_sh["cpes.refs.ref"][r]):
            aux=df_cpe_sh["cpes.refs.ref"][r].split(",")
            for k in range(0,len(aux)):
                if(len(aux)>0):
                    cpes_lastmodified2018_sh+=1
                    counterrefs_sh+=1
                    aux_str=aux[k].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
                    if('apple' in aux_str):
                        cpes_lastmodified2018_refapple_sh+=1   
                    elif('cisco' in aux_str):
                        cpes_lastmodified2018_refcisco_sh+=1
                    elif('bosch' in aux_str):
                        cpes_lastmodified2018_refbosch_sh+=1   
                    elif('coolkit' in aux_str):
                        cpes_lastmodified2018_refcoolkit_sh+=1    
                    elif('inim.biz' in aux_str):
                        cpes_lastmodified2018_refinimbiz_sh+=1    
                    elif('idec' in aux_str):
                        cpes_lastmodified2018_refidec_sh+=1    
                    elif('google' in aux_str):
                        cpes_lastmodified2018_refgoogle_sh+=1    
                    elif('docs.bmc' in aux_str):
                        cpes_lastmodified2018_refdocbmc_sh+=1    
        else:
            counterrefs_sh+=1
            cpes_lastmodified2018_sh+=1
            if('apple' in df_cpe_sh["cpes.refs.ref"][r]):
                cpes_lastmodified2018_refapple_sh+=1   
            elif('cisco' in df_cpe_sh["cpes.refs.ref"][r]):
                cpes_lastmodified2018_refcisco_sh+=1
            elif('bosch' in df_cpe_sh["cpes.refs.ref"][r]):
                cpes_lastmodified2018_refbosch_sh+=1
            elif('coolkit' in df_cpe_sh["cpes.refs.ref"][r]):
                cpes_lastmodified2018_refcoolkit_sh+=1
            elif('inim.biz' in df_cpe_sh["cpes.refs.ref"][r]):
                cpes_lastmodified2018_refinimbiz_sh+=1
            elif('idec' in df_cpe_sh["cpes.refs.ref"][r]):
                cpes_lastmodified2018_refidec_sh+=1
            elif('google' in df_cpe_sh["cpes.refs.ref"][r]):
                cpes_lastmodified2018_refgoogle_sh+=1
            elif('docs.bmc' in df_cpe_sh["cpes.refs.ref"][r]):
                cpes_lastmodified2018_refdocbmc_sh+=1




        
    
    
    
    
    
        
#Total numero de referencias independientemente del anio     
cpes_refapple_sh=cpes_lastmodified2023_refapple_sh+cpes_lastmodified2022_refapple_sh+cpes_lastmodified2021_refapple_sh+cpes_lastmodified2020_refapple_sh+cpes_lastmodified2019_refapple_sh+cpes_lastmodified2018_refapple_sh   
cpes_refcisco_sh=cpes_lastmodified2023_refcisco_sh+cpes_lastmodified2022_refcisco_sh+cpes_lastmodified2021_refcisco_sh+cpes_lastmodified2020_refcisco_sh+cpes_lastmodified2019_refcisco_sh+cpes_lastmodified2018_refcisco_sh   
cpes_refbosch_sh=cpes_lastmodified2023_refbosch_sh+cpes_lastmodified2022_refbosch_sh+cpes_lastmodified2021_refbosch_sh+cpes_lastmodified2020_refbosch_sh+cpes_lastmodified2019_refbosch_sh+cpes_lastmodified2018_refbosch_sh
cpes_refcoolkit_sh=cpes_lastmodified2023_refcoolkit_sh+cpes_lastmodified2022_refcoolkit_sh+cpes_lastmodified2021_refcoolkit_sh+cpes_lastmodified2020_refcoolkit_sh+cpes_lastmodified2019_refcoolkit_sh+cpes_lastmodified2018_refcoolkit_sh
cpes_refinimbiz_sh=cpes_lastmodified2023_refinimbiz_sh+cpes_lastmodified2022_refinimbiz_sh+cpes_lastmodified2021_refinimbiz_sh+cpes_lastmodified2020_refinimbiz_sh+cpes_lastmodified2019_refinimbiz_sh+cpes_lastmodified2018_refinimbiz_sh
cpes_refidec_sh=cpes_lastmodified2023_refidec_sh+cpes_lastmodified2022_refidec_sh+cpes_lastmodified2021_refidec_sh+cpes_lastmodified2020_refidec_sh+cpes_lastmodified2019_refidec_sh+cpes_lastmodified2018_refidec_sh
cpes_refgoogle_sh=cpes_lastmodified2023_refgoogle_sh+cpes_lastmodified2022_refgoogle_sh+cpes_lastmodified2021_refgoogle_sh+cpes_lastmodified2020_refgoogle_sh+cpes_lastmodified2019_refgoogle_sh+cpes_lastmodified2018_refgoogle_sh
cpes_refdocbmc_sh=cpes_lastmodified2023_refdocbmc_sh+cpes_lastmodified2022_refdocbmc_sh+cpes_lastmodified2021_refdocbmc_sh+cpes_lastmodified2020_refdocbmc_sh+cpes_lastmodified2019_refdocbmc_sh+cpes_lastmodified2018_refdocbmc_sh


        


print("********************************ESTADÍSTICAS FECHA DE ULTIMA MODIFICACION CPE/FUENTE DE REFERENCIA CPE PARTE SMART HOME********************************")
print("\n")                            
                
print("\n")
print(" DE UN TOTAL DE "+str(counterrefs_sh)+" REFERENCIAS DE CPES , LAS ESTADISTICAS DE RELACION DE FECHA DE MODIFICACION Y FUENTE DE REFERENCIA SON LAS SIGUIENTES:  \n")
print("\n")
print("      -    EN  "+str(cpes_refapple_sh)+" REFERENCIAS LA FUENTE ES APPLE.COM  \n")
print("      -    EN  "+str(cpes_refcisco_sh)+" REFERENCIAS LA FUENTE ES CISCO.COM  \n")
print("      -    EN  "+str(cpes_refbosch_sh)+" REFERENCIAS LA FUENTE ES BOSCH.COM \n")
print("      -    EN  "+str(cpes_refcoolkit_sh)+" REFERENCIAS LA FUENTE ES COOLKIT.CN  \n")
print("      -    EN  "+str(cpes_refinimbiz_sh)+" REFERENCIAS LA FUENTE ES INIM.BIZ  \n")
print("      -    EN  "+str(cpes_refidec_sh)+" REFERENCIAS LA FUENTE ES LP.IDEC.COM  \n")
print("      -    EN  "+str(cpes_refgoogle_sh)+" REFERENCIAS LA FUENTE ES PLAY.GOOGLE  \n")
print("      -    EN  "+str(cpes_refdocbmc_sh)+" REFERENCIAS LA FUENTE ES DOCS.BMC  \n")
print("\n")
print("      -    EN  "+str(cpes_lastmodified2023_sh)+" REFERENCIAS DE CPES LA FECHA DE MODIFICACION ES 2023. LAS ESTADÍSTICAS DE FUENTE DE REFERENCIA SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(cpes_lastmodified2023_refapple_sh)+" REFERENCIAS LA FUENTE ES APPLE.COM ")
print("            -    EN  "+str(cpes_lastmodified2023_refcisco_sh)+" REFERENCIAS LA FUENTE ES CISCO.COM ")
print("            -    EN  "+str(cpes_lastmodified2023_refbosch_sh)+" REFERENCIAS LA FUENTE ES BOSCH.COM")
print("            -    EN  "+str(cpes_lastmodified2023_refcoolkit_sh)+" REFERENCIAS LA FUENTE ES COOLKIT.CN ")
print("            -    EN  "+str(cpes_lastmodified2023_refinimbiz_sh)+" REFERENCIAS LA FUENTE ES INIM.BIZ ")
print("            -    EN  "+str(cpes_lastmodified2023_refidec_sh)+" REFERENCIAS LA FUENTE ES LP.IDEC.COM ")
print("            -    EN  "+str(cpes_lastmodified2023_refgoogle_sh)+" REFERENCIAS LA FUENTE ES PLAY.GOOGLE ")
print("            -    EN  "+str(cpes_lastmodified2023_refdocbmc_sh)+" REFERENCIAS LA FUENTE ES DOCS.BMC ")
print("\n")
print("      -    EN  "+str(cpes_lastmodified2022_sh)+" REFERENCIAS DE CPES LA FECHA DE MODIFICACION ES 2022. LAS ESTADÍSTICAS DE FUENTE DE REFERENCIA SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(cpes_lastmodified2022_refapple_sh)+" REFERENCIAS LA FUENTE ES APPLE.COM ")
print("            -    EN  "+str(cpes_lastmodified2022_refcisco_sh)+" REFERENCIAS LA FUENTE ES CISCO.COM ")
print("            -    EN  "+str(cpes_lastmodified2022_refbosch_sh)+" REFERENCIAS LA FUENTE ES BOSCH.COM")
print("            -    EN  "+str(cpes_lastmodified2022_refcoolkit_sh)+" REFERENCIAS LA FUENTE ES COOLKIT.CN ")
print("            -    EN  "+str(cpes_lastmodified2022_refinimbiz_sh)+" REFERENCIAS LA FUENTE ES INIM.BIZ ")
print("            -    EN  "+str(cpes_lastmodified2022_refidec_sh)+" REFERENCIAS LA FUENTE ES LP.IDEC.COM ")
print("            -    EN  "+str(cpes_lastmodified2022_refgoogle_sh)+" REFERENCIAS LA FUENTE ES PLAY.GOOGLE ")
print("            -    EN  "+str(cpes_lastmodified2022_refdocbmc_sh)+" REFERENCIAS LA FUENTE ES DOCS.BMC ")
print("\n")
print("      -    EN  "+str(cpes_lastmodified2021_sh)+" REFERENCIAS DE CPES LA FECHA DE MODIFICACION ES 2021. LAS ESTADÍSTICAS DE FUENTE DE REFERENCIA SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(cpes_lastmodified2021_refapple_sh)+" REFERENCIAS LA FUENTE ES APPLE.COM ")
print("            -    EN  "+str(cpes_lastmodified2021_refcisco_sh)+" REFERENCIAS LA FUENTE ES CISCO.COM ")
print("            -    EN  "+str(cpes_lastmodified2021_refbosch_sh)+" REFERENCIAS LA FUENTE ES BOSCH.COM")
print("            -    EN  "+str(cpes_lastmodified2021_refcoolkit_sh)+" REFERENCIAS LA FUENTE ES COOLKIT.CN ")
print("            -    EN  "+str(cpes_lastmodified2021_refinimbiz_sh)+" REFERENCIAS LA FUENTE ES INIM.BIZ ")
print("            -    EN  "+str(cpes_lastmodified2021_refidec_sh)+" REFERENCIAS LA FUENTE ES LP.IDEC.COM ")
print("            -    EN  "+str(cpes_lastmodified2021_refgoogle_sh)+" REFERENCIAS LA FUENTE ES PLAY.GOOGLE ")
print("            -    EN  "+str(cpes_lastmodified2021_refdocbmc_sh)+" REFERENCIAS LA FUENTE ES DOCS.BMC ")
print("\n")
print("      -    EN  "+str(cpes_lastmodified2020_sh)+" REFERENCIAS DE CPES LA FECHA DE MODIFICACION ES 2020. LAS ESTADÍSTICAS DE FUENTE DE REFERENCIA SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(cpes_lastmodified2020_refapple_sh)+" REFERENCIAS LA FUENTE ES APPLE.COM ")
print("            -    EN  "+str(cpes_lastmodified2020_refcisco_sh)+" REFERENCIAS LA FUENTE ES CISCO.COM ")
print("            -    EN  "+str(cpes_lastmodified2020_refbosch_sh)+" REFERENCIAS LA FUENTE ES BOSCH.COM")
print("            -    EN  "+str(cpes_lastmodified2020_refcoolkit_sh)+" REFERENCIAS LA FUENTE ES COOLKIT.CN ")
print("            -    EN  "+str(cpes_lastmodified2020_refinimbiz_sh)+" REFERENCIAS LA FUENTE ES INIM.BIZ ")
print("            -    EN  "+str(cpes_lastmodified2020_refidec_sh)+" REFERENCIAS LA FUENTE ES LP.IDEC.COM ")
print("            -    EN  "+str(cpes_lastmodified2020_refgoogle_sh)+" REFERENCIAS LA FUENTE ES PLAY.GOOGLE ")
print("            -    EN  "+str(cpes_lastmodified2020_refdocbmc_sh)+" REFERENCIAS LA FUENTE ES DOCS.BMC ")
print("\n")
print("      -    EN  "+str(cpes_lastmodified2019_sh)+" REFERENCIAS DE CPES LA FECHA DE MODIFICACION ES 2019. LAS ESTADÍSTICAS DE FUENTE DE REFERENCIA SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(cpes_lastmodified2019_refapple_sh)+" REFERENCIAS LA FUENTE ES APPLE.COM ")
print("            -    EN  "+str(cpes_lastmodified2019_refcisco_sh)+" REFERENCIAS LA FUENTE ES CISCO.COM ")
print("            -    EN  "+str(cpes_lastmodified2019_refbosch_sh)+" REFERENCIAS LA FUENTE ES BOSCH.COM")
print("            -    EN  "+str(cpes_lastmodified2019_refcoolkit_sh)+" REFERENCIAS LA FUENTE ES COOLKIT.CN ")
print("            -    EN  "+str(cpes_lastmodified2019_refinimbiz_sh)+" REFERENCIAS LA FUENTE ES INIM.BIZ ")
print("            -    EN  "+str(cpes_lastmodified2019_refidec_sh)+" REFERENCIAS LA FUENTE ES LP.IDEC.COM ")
print("            -    EN  "+str(cpes_lastmodified2019_refgoogle_sh)+" REFERENCIAS LA FUENTE ES PLAY.GOOGLE ")
print("            -    EN  "+str(cpes_lastmodified2019_refdocbmc_sh)+" REFERENCIAS LA FUENTE ES DOCS.BMC ")
print("\n")
print("      -    EN  "+str(cpes_lastmodified2018_sh)+" REFERENCIAS DE CPES LA FECHA DE MODIFICACION ES 2018 O ANTERIOR. LAS ESTADÍSTICAS DE FUENTE DE REFERENCIA SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(cpes_lastmodified2018_refapple_sh)+" REFERENCIAS LA FUENTE ES APPLE.COM ")
print("            -    EN  "+str(cpes_lastmodified2018_refcisco_sh)+" REFERENCIAS LA FUENTE ES CISCO.COM ")
print("            -    EN  "+str(cpes_lastmodified2018_refbosch_sh)+" REFERENCIAS LA FUENTE ES BOSCH.COM")
print("            -    EN  "+str(cpes_lastmodified2018_refcoolkit_sh)+" REFERENCIAS LA FUENTE ES COOLKIT.CN ")
print("            -    EN  "+str(cpes_lastmodified2018_refinimbiz_sh)+" REFERENCIAS LA FUENTE ES INIM.BIZ ")
print("            -    EN  "+str(cpes_lastmodified2018_refidec_sh)+" REFERENCIAS LA FUENTE ES LP.IDEC.COM ")
print("            -    EN  "+str(cpes_lastmodified2018_refgoogle_sh)+" REFERENCIAS LA FUENTE ES PLAY.GOOGLE ")
print("            -    EN  "+str(cpes_lastmodified2018_refdocbmc_sh)+" REFERENCIAS LA FUENTE ES DOCS.BMC ")
print("\n")










print("********************************PORCENTAJES FECHA DE ULTIMA MODIFICACION CPE/FUENTE DE REFERENCIA CPE PARTE SMART HOME********************************")
print("\n")        
            
          
    
print("\n")
print(" DE UN TOTAL DE "+str(counterrefs_sh)+" REFERENCIAS DE CPES , LOS PORCENTAJES DE RELACION DE FECHA DE MODIFICACION Y FUENTE DE REFERENCIA SON LOS SIGUIENTES:  \n")
print("\n")
print("\n")
print("      -    EN  EL "+str(float(((cpes_refapple_sh*100)/counterrefs_sh)))+" % DE REFERENCIAS LA FUENTE ES APPLE.COM  \n")
print("      -    EN  EL "+str(float(((cpes_refcisco_sh*100)/counterrefs_sh)))+" % DE REFERENCIAS LA FUENTE ES CISCO.COM  \n")
print("      -    EN  EL "+str(float(((cpes_refbosch_sh*100)/counterrefs_sh)))+" % DE REFERENCIAS LA FUENTE ES BOSCH.COM \n")
print("      -    EN  EL "+str(float(((cpes_refcoolkit_sh*100)/counterrefs_sh)))+" % DE REFERENCIAS LA FUENTE ES COOLKIT.CN  \n")
print("      -    EN  EL "+str(float(((cpes_refinimbiz_sh*100)/counterrefs_sh)))+" % DE REFERENCIAS LA FUENTE ES INIM.BIZ  \n")
print("      -    EN  EL "+str(float(((cpes_refidec_sh*100)/counterrefs_sh)))+" % DE REFERENCIAS LA FUENTE ES LP.IDEC.COM  \n")
print("      -    EN  EL "+str(float(((cpes_refgoogle_sh*100)/counterrefs_sh)))+" % DE REFERENCIAS LA FUENTE ES PLAY.GOOGLE  \n")
print("      -    EN  EL "+str(float(((cpes_refdocbmc_sh*100)/counterrefs_sh)))+" % DE REFERENCIAS LA FUENTE ES DOCS.BMC  \n")
print("\n")
if(cpes_lastmodified2023_sh>0):
    print("      -    EN EL "+str(float(((cpes_lastmodified2023_sh*100)/counterrefs_sh)))+" % DE REFERENCIAS DE CPES LA FECHA DE MODIFICACION ES 2023. LOS PORCENTAJES DE FUENTE DE REFERENCIA SON LOS SIGUIENTES:  \n")
    print("\n")
    print("            -    EN EL "+str(float(((cpes_lastmodified2023_refapple_sh*100)/cpes_lastmodified2023_sh)))+" % DE REFERENCIAS LA FUENTE ES APPLE.COM  ")
    print("            -    EN EL "+str(float(((cpes_lastmodified2023_refcisco_sh*100)/cpes_lastmodified2023_sh)))+" % DE REFERENCIAS LA FUENTE ES CISCO.COMO ")
    print("            -    EN EL "+str(float(((cpes_lastmodified2023_refbosch_sh*100)/cpes_lastmodified2023_sh)))+" % DE REFERENCIAS LA FUENTE ES BOSCH.COM")
    print("            -    EN EL "+str(float(((cpes_lastmodified2023_refcoolkit_sh*100)/cpes_lastmodified2023_sh)))+" % DE REFERENCIAS LA FUENTE ES COOLKIT.CN ")
    print("            -    EN EL "+str(float(((cpes_lastmodified2023_refinimbiz_sh*100)/cpes_lastmodified2023_sh)))+" % DE REFERENCIAS LA FUENTE ES INIM.BIZ ")
    print("            -    EN EL "+str(float(((cpes_lastmodified2023_refidec_sh*100)/cpes_lastmodified2023_sh)))+" % DE REFERENCIAS LA FUENTE ES LP.IDEC.COM ")
    print("            -    EN EL "+str(float(((cpes_lastmodified2023_refgoogle_sh*100)/cpes_lastmodified2023_sh)))+" % DE REFERENCIAS LA FUENTE ES PLAY.GOOGLE ")
    print("            -    EN EL "+str(float(((cpes_lastmodified2023_refdocbmc_sh*100)/cpes_lastmodified2023_sh)))+" % DE REFERENCIAS LA FUENTE ES DOCS.BMC ")
    print("\n")
print("      -    EN EL "+str(float(((cpes_lastmodified2022_sh*100)/counterrefs_sh)))+" % DE REFERENCIAS DE CPES LA FECHA DE MODIFICACION ES 2022. LOS PORCENTAJES DE FUENTE DE REFERENCIA SON LOS SIGUIENTES:  \n")
print("\n")
print("            -    EN EL "+str(float(((cpes_lastmodified2022_refapple_sh*100)/cpes_lastmodified2022_sh)))+" % DE REFERENCIAS LA FUENTE ES APPLE.COM  ")
print("            -    EN EL "+str(float(((cpes_lastmodified2022_refcisco_sh*100)/cpes_lastmodified2022_sh)))+" % DE REFERENCIAS LA FUENTE ES CISCO.COMO ")
print("            -    EN EL "+str(float(((cpes_lastmodified2022_refbosch_sh*100)/cpes_lastmodified2022_sh)))+" % DE REFERENCIAS LA FUENTE ES BOSCH.COM")
print("            -    EN EL "+str(float(((cpes_lastmodified2022_refcoolkit_sh*100)/cpes_lastmodified2022_sh)))+" % DE REFERENCIAS LA FUENTE ES COOLKIT.CN ")
print("            -    EN EL "+str(float(((cpes_lastmodified2022_refinimbiz_sh*100)/cpes_lastmodified2022_sh)))+" % DE REFERENCIAS LA FUENTE ES INIM.BIZ ")
print("            -    EN EL "+str(float(((cpes_lastmodified2022_refidec_sh*100)/cpes_lastmodified2022_sh)))+" % DE REFERENCIAS LA FUENTE ES LP.IDEC.COM ")
print("            -    EN EL "+str(float(((cpes_lastmodified2022_refgoogle_sh*100)/cpes_lastmodified2022_sh)))+" % DE REFERENCIAS LA FUENTE ES PLAY.GOOGLE ")
print("            -    EN EL "+str(float(((cpes_lastmodified2022_refdocbmc_sh*100)/cpes_lastmodified2022_sh)))+" % DE REFERENCIAS LA FUENTE ES DOCS.BMC ")
print("\n")
print("      -    EN EL "+str(float(((cpes_lastmodified2021_sh*100)/counterrefs_sh)))+" % DE REFERENCIAS DE CPES LA FECHA DE MODIFICACION ES 2021. LOS PORCENTAJES DE FUENTE DE REFERENCIA SON LOS SIGUIENTES:  \n")
print("\n")
print("            -    EN EL "+str(float(((cpes_lastmodified2021_refapple_sh*100)/cpes_lastmodified2021_sh)))+" % DE REFERENCIAS LA FUENTE ES APPLE.COM  ")
print("            -    EN EL "+str(float(((cpes_lastmodified2021_refcisco_sh*100)/cpes_lastmodified2021_sh)))+" % DE REFERENCIAS LA FUENTE ES CISCO.COMO ")
print("            -    EN EL "+str(float(((cpes_lastmodified2021_refbosch_sh*100)/cpes_lastmodified2021_sh)))+" % DE REFERENCIAS LA FUENTE ES BOSCH.COM")
print("            -    EN EL "+str(float(((cpes_lastmodified2021_refcoolkit_sh*100)/cpes_lastmodified2021_sh)))+" % DE REFERENCIAS LA FUENTE ES COOLKIT.CN ")
print("            -    EN EL "+str(float(((cpes_lastmodified2021_refinimbiz_sh*100)/cpes_lastmodified2021_sh)))+" % DE REFERENCIAS LA FUENTE ES INIM.BIZ ")
print("            -    EN EL "+str(float(((cpes_lastmodified2021_refidec_sh*100)/cpes_lastmodified2021_sh)))+" % DE REFERENCIAS LA FUENTE ES LP.IDEC.COM ")
print("            -    EN EL "+str(float(((cpes_lastmodified2021_refgoogle_sh*100)/cpes_lastmodified2021_sh)))+" % DE REFERENCIAS LA FUENTE ES PLAY.GOOGLE ")
print("            -    EN EL "+str(float(((cpes_lastmodified2021_refdocbmc_sh*100)/cpes_lastmodified2021_sh)))+" % DE REFERENCIAS LA FUENTE ES DOCS.BMC ")
print("\n")
print("      -    EN EL "+str(float(((cpes_lastmodified2020_sh*100)/counterrefs_sh)))+" % DE REFERENCIAS DE CPES LA FECHA DE MODIFICACION ES 2020. LOS PORCENTAJES DE FUENTE DE REFERENCIA SON LOS SIGUIENTES:  \n")
print("\n")
print("            -    EN EL "+str(float(((cpes_lastmodified2020_refapple_sh*100)/cpes_lastmodified2020_sh)))+" % DE REFERENCIAS LA FUENTE ES APPLE.COM  ")
print("            -    EN EL "+str(float(((cpes_lastmodified2020_refcisco_sh*100)/cpes_lastmodified2020_sh)))+" % DE REFERENCIAS LA FUENTE ES CISCO.COMO ")
print("            -    EN EL "+str(float(((cpes_lastmodified2020_refbosch_sh*100)/cpes_lastmodified2020_sh)))+" % DE REFERENCIAS LA FUENTE ES BOSCH.COM")
print("            -    EN EL "+str(float(((cpes_lastmodified2020_refcoolkit_sh*100)/cpes_lastmodified2020_sh)))+" % DE REFERENCIAS LA FUENTE ES COOLKIT.CN ")
print("            -    EN EL "+str(float(((cpes_lastmodified2020_refinimbiz_sh*100)/cpes_lastmodified2020_sh)))+" % DE REFERENCIAS LA FUENTE ES INIM.BIZ ")
print("            -    EN EL "+str(float(((cpes_lastmodified2020_refidec_sh*100)/cpes_lastmodified2020_sh)))+" % DE REFERENCIAS LA FUENTE ES LP.IDEC.COM ")
print("            -    EN EL "+str(float(((cpes_lastmodified2020_refgoogle_sh*100)/cpes_lastmodified2020_sh)))+" % DE REFERENCIAS LA FUENTE ES PLAY.GOOGLE ")
print("            -    EN EL "+str(float(((cpes_lastmodified2020_refdocbmc_sh*100)/cpes_lastmodified2020_sh)))+" % DE REFERENCIAS LA FUENTE ES DOCS.BMC ")
print("\n")
print("      -    EN EL "+str(float(((cpes_lastmodified2019_sh*100)/counterrefs_sh)))+" % DE REFERENCIAS DE CPES LA FECHA DE MODIFICACION ES 2019. LOS PORCENTAJES DE FUENTE DE REFERENCIA SON LOS SIGUIENTES:  \n")
print("\n")
print("            -    EN EL "+str(float(((cpes_lastmodified2019_refapple_sh*100)/cpes_lastmodified2019_sh)))+" % DE REFERENCIAS LA FUENTE ES APPLE.COM  ")
print("            -    EN EL "+str(float(((cpes_lastmodified2019_refcisco_sh*100)/cpes_lastmodified2019_sh)))+" % DE REFERENCIAS LA FUENTE ES CISCO.COMO ")
print("            -    EN EL "+str(float(((cpes_lastmodified2019_refbosch_sh*100)/cpes_lastmodified2019_sh)))+" % DE REFERENCIAS LA FUENTE ES BOSCH.COM")
print("            -    EN EL "+str(float(((cpes_lastmodified2019_refcoolkit_sh*100)/cpes_lastmodified2019_sh)))+" % DE REFERENCIAS LA FUENTE ES COOLKIT.CN ")
print("            -    EN EL "+str(float(((cpes_lastmodified2019_refinimbiz_sh*100)/cpes_lastmodified2019_sh)))+" % DE REFERENCIAS LA FUENTE ES INIM.BIZ ")
print("            -    EN EL "+str(float(((cpes_lastmodified2019_refidec_sh*100)/cpes_lastmodified2019_sh)))+" % DE REFERENCIAS LA FUENTE ES LP.IDEC.COM ")
print("            -    EN EL "+str(float(((cpes_lastmodified2019_refgoogle_sh*100)/cpes_lastmodified2019_sh)))+" % DE REFERENCIAS LA FUENTE ES PLAY.GOOGLE ")
print("            -    EN EL "+str(float(((cpes_lastmodified2019_refdocbmc_sh*100)/cpes_lastmodified2019_sh)))+" % DE REFERENCIAS LA FUENTE ES DOCS.BMC ")
print("\n")
print("      -    EN EL "+str(float(((cpes_lastmodified2018_sh*100)/counterrefs_sh)))+" % DE REFERENCIAS DE CPES LA FECHA DE MODIFICACION ES 2018 O ANTERIOR. LOS PORCENTAJES DE FUENTE DE REFERENCIA SON LOS SIGUIENTES:  \n")
print("\n")
print("            -    EN EL "+str(float(((cpes_lastmodified2018_refapple_sh*100)/cpes_lastmodified2018_sh)))+" % DE REFERENCIAS LA FUENTE ES APPLE.COM  ")
print("            -    EN EL "+str(float(((cpes_lastmodified2018_refcisco_sh*100)/cpes_lastmodified2018_sh)))+" % DE REFERENCIAS LA FUENTE ES CISCO.COMO ")
print("            -    EN EL "+str(float(((cpes_lastmodified2018_refbosch_sh*100)/cpes_lastmodified2018_sh)))+" % DE REFERENCIAS LA FUENTE ES BOSCH.COM")
print("            -    EN EL "+str(float(((cpes_lastmodified2018_refcoolkit_sh*100)/cpes_lastmodified2018_sh)))+" % DE REFERENCIAS LA FUENTE ES COOLKIT.CN ")
print("            -    EN EL "+str(float(((cpes_lastmodified2018_refinimbiz_sh*100)/cpes_lastmodified2018_sh)))+" % DE REFERENCIAS LA FUENTE ES INIM.BIZ ")
print("            -    EN EL "+str(float(((cpes_lastmodified2018_refidec_sh*100)/cpes_lastmodified2018_sh)))+" % DE REFERENCIAS LA FUENTE ES LP.IDEC.COM ")
print("            -    EN EL "+str(float(((cpes_lastmodified2018_refgoogle_sh*100)/cpes_lastmodified2018_sh)))+" % DE REFERENCIAS LA FUENTE ES PLAY.GOOGLE ")
print("            -    EN EL "+str(float(((cpes_lastmodified2018_refdocbmc_sh*100)/cpes_lastmodified2018_sh)))+" % DE REFERENCIAS LA FUENTE ES DOCS.BMC ")
print("\n")



























