


import pandas as pd
from datetime import datetime,timedelta

df_vulnibm_iot=pd.read_excel('vulnerabilidades_ibm_iot_2023.xlsx')
df_vulnibm_sh=pd.read_excel('vulnerabilidades_ibm_smart_home_2023.xlsx')
df_cve_iot=pd.read_excel('cves_iot_2023.xlsx')
df_cve_sh=pd.read_excel('cves_smart_home_2023.xlsx')
df_cpe_iot=pd.read_excel('cpes_iot_2023.xlsx')
df_cpe_sh=pd.read_excel('cpes_smart_home_2023.xlsx')





#Abro los ficheros con los que voy a tratar



#Variable que almacenara el contador total de valores de fuentes de referencia
count_references=0

#Variables que almacenan el contador de valores especificos de nombre
count_reference_IBM=0
count_reference_GITHUB=0
count_reference_INTEL=0
count_reference_APPLE=0
count_reference_MEND=0
count_reference_CISCO=0
count_reference_MEDIATEK=0
count_reference_MICROSOFT=0
count_reference_LENOVO=0
count_reference_DELL=0
count_reference_MOZILLA=0
count_reference_ADOBE=0
count_reference_SIEMENS=0
count_reference_APACHE=0
count_reference_NPM=0
count_reference_SYNK=0
count_reference_ORACLE=0
count_reference_FORTIGUARD=0
count_reference_CONTEC=0
count_reference_QUALCOMM=0
count_reference_TALOS=0
count_reference_DLINK=0
count_reference_PTC=0
count_reference_SYMBIOTE=0
count_reference_ASUS=0
count_reference_IOTKONKER=0
count_reference_VULNCHECK=0
count_reference_XIONGMAITECH=0
count_reference_RIOT=0
count_reference_ECLIPSE=0
count_reference_BOSCH=0
count_reference_CISAGOV=0
count_reference_CERT=0
count_reference_PACKETSTORM=0
count_reference_CODEAURORA=0
count_reference_ANOTHER=0





#Comprobamos el contenido de nombre de referencia
for r in range(0,len(df_vulnibm_iot["x_xfe_references_link_name"])):
    if((",") in (df_vulnibm_iot["x_xfe_references_link_name"][r])):
        #Si hay varios valores de referencias en la misma fila, separo cada uno de los valores
        aux_refname_vulnibm_iot = df_vulnibm_iot["x_xfe_references_link_name"][r].split(',')
        #Inserto cada valor de name de cada fila en el vector donde estaran todos los valores de name, quitando algunos caracteres especiales y espacios
        for j in range(0,len(aux_refname_vulnibm_iot)):
            aux_str=aux_refname_vulnibm_iot[j].replace('[','').replace(']','').replace("'","").replace("","")
            if(aux_str!='NONE' and 'CVE' not in aux_str):
                count_references+=1
                if('IBM' in aux_str):
                    count_reference_IBM+=1
                elif('GitHub' in aux_str or 'GITHub' in aux_str or 'github' in aux_str):
                    count_reference_GITHUB+=1
                elif('INTEL' in aux_str or 'Intel' in aux_str or 'intel' in aux_str ):
                    count_reference_INTEL+=1
                elif('Apple' in aux_str or 'apple' in aux_str):
                    count_reference_APPLE+=1
                elif('Mend' in aux_str):
                    count_reference_MEND+=1
                elif('Cisco' in aux_str or 'CISCO' in aux_str or 'cisco' in aux_str):
                    count_reference_CISCO+=1
                elif('Mediatek' in aux_str or 'MediaTek' in aux_str):
                    count_reference_MEDIATEK+=1
                elif('Microsoft' in aux_str or 'microsoft' in aux_str):
                    count_reference_MICROSOFT+=1
                elif('Lenovo' in aux_str or 'lenovo' in aux_str):
                    count_reference_LENOVO+=1
                elif('Dell' in aux_str):
                    count_reference_DELL+=1
                elif('Mozilla' in aux_str or 'mozilla' in aux_str):
                    count_reference_MOZILLA+=1
                elif('Adobe' in aux_str or 'adobe' in aux_str):
                    count_reference_ADOBE+=1
                elif('Siemens' in aux_str or 'siemens' in aux_str):
                    count_reference_SIEMENS+=1
                elif('Apache' in aux_str or 'apache' in aux_str):
                    count_reference_APACHE+=1
                elif('NPM' in aux_str):
                    count_reference_NPM+=1
                elif('SNYK' in aux_str):
                    count_reference_SYNK+=1
                elif('Oracle' in aux_str or 'oracle' in aux_str):
                    count_reference_ORACLE+=1
                    
                elif('Fortiguard' in aux_str or 'fortiguard' in aux_str):
                    count_reference_FORTIGUARD+=1
                    
                elif('Contec' in aux_str or 'contec' in aux_str):
                    count_reference_CONTEC+=1
                elif('Qualcomm' in aux_str or 'qualcomm' in aux_str):
                    count_reference_QUALCOMM+=1
                elif('Talos' in aux_str or 'TALOS' in aux_str):
                    count_reference_TALOS+=1
                elif('dlink' in aux_str):
                    count_reference_DLINK+=1
                elif('ptc' in aux_str or 'PTC' in aux_str):
                    count_reference_PTC+=1
                elif('symbiote' in aux_str or 'Symbiote' in aux_str ):
                    count_reference_SYMBIOTE+=1
                elif('asus' in aux_str or 'Asus' in aux_str):
                    count_reference_ASUS+=1
        
                elif('iot.konker' in aux_str):
                    count_reference_IOTKONKER+=1
                elif('vulncheck' in aux_str):
                    count_reference_VULNCHECK+=1
                elif('xiongmaitech' in aux_str):
                    count_reference_XIONGMAITECH+=1
                
                elif('riot' in aux_str):
                    count_reference_RIOT+=1
                elif('eclipse' in aux_str):
                    count_reference_ECLIPSE+=1
                elif('bosch' in aux_str):
                    count_reference_BOSCH+=1
                elif('cisa.gov' in aux_str):
                    count_reference_CISAGOV+=1
                elif('-cert' in aux_str):
                    count_reference_CERT+=1
                elif(('packet' in aux_str or 'Packet' in aux_str) and ('Storm' in aux_str or 'storm' in aux_str)):
                    count_reference_PACKETSTORM+=1
                elif('codeaurora' in aux_str):
                    count_reference_CODEAURORA+=1
                else:
                    count_reference_ANOTHER+=1
                    
                
                    
                
    else:
    
        #Obtengo el valor de nombre de referencia y aumento contadores segun el tipo que sea
        aux_str=df_vulnibm_iot["x_xfe_references_link_name"][r].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
        if(aux_str!='NONE' and 'CVE' not in aux_str):
            count_references+=1
            if('IBM' in aux_str):
                count_reference_IBM+=1
            elif('GitHub' in aux_str or 'GITHub' in aux_str or 'github' in aux_str):
                count_reference_GITHUB+=1
            elif('INTEL' in aux_str or 'Intel' in aux_str or 'intel' in aux_str ):
                count_reference_INTEL+=1
            elif('Apple' in aux_str or 'apple' in aux_str):
                count_reference_APPLE+=1
            elif('Mend' in aux_str):
                count_reference_MEND+=1
            elif('Cisco' in aux_str or 'CISCO' in aux_str or 'cisco' in aux_str):
                count_reference_CISCO+=1
            elif('Mediatek' in aux_str or 'MediaTek' in aux_str):
                count_reference_MEDIATEK+=1
            elif('Microsoft' in aux_str or 'microsoft' in aux_str):
                count_reference_MICROSOFT+=1
            elif('Lenovo' in aux_str or 'lenovo' in aux_str):
                count_reference_LENOVO+=1
            elif('Dell' in aux_str):
                count_reference_DELL+=1
            elif('Mozilla' in aux_str or 'mozilla' in aux_str):
                count_reference_MOZILLA+=1
            elif('Adobe' in aux_str or 'adobe' in aux_str):
                count_reference_ADOBE+=1
            elif('Siemens' in aux_str or 'siemens' in aux_str):
                count_reference_SIEMENS+=1
            elif('Apache' in aux_str or 'apache' in aux_str):
                count_reference_APACHE+=1
            elif('NPM' in aux_str):
                count_reference_NPM+=1
            elif('SNYK' in aux_str):
                count_reference_SYNK+=1
            elif('Oracle' in aux_str or 'oracle' in aux_str):
                count_reference_ORACLE+=1

            elif('Fortiguard' in aux_str or 'fortiguard' in aux_str):
                count_reference_FORTIGUARD+=1

            elif('Contec' in aux_str or 'contec' in aux_str):
                count_reference_CONTEC+=1
            elif('Qualcomm' in aux_str or 'qualcomm' in aux_str):
                count_reference_QUALCOMM+=1
            elif('Talos' in aux_str or 'TALOS' in aux_str):
                count_reference_TALOS+=1
            elif('dlink' in aux_str):
                count_reference_DLINK+=1
            elif('ptc' in aux_str or 'PTC' in aux_str):
                count_reference_PTC+=1
            elif('symbiote' in aux_str or 'Symbiote' in aux_str ):
                count_reference_SYMBIOTE+=1
            elif('asus' in aux_str or 'Asus' in aux_str):
                count_reference_ASUS+=1

            elif('iot.konker' in aux_str):
                count_reference_IOTKONKER+=1
            elif('vulncheck' in aux_str):
                count_reference_VULNCHECK+=1
            elif('xiongmaitech' in aux_str):
                count_reference_XIONGMAITECH+=1

            elif('riot' in aux_str):
                count_reference_RIOT+=1
            elif('eclipse' in aux_str):
                count_reference_ECLIPSE+=1
            elif('bosch' in aux_str):
                count_reference_BOSCH+=1
            elif('cisa.gov' in aux_str):
                count_reference_CISAGOV+=1
            elif('-cert' in aux_str):
                count_reference_CERT+=1
            elif(('packet' in aux_str or 'Packet' in aux_str) and ('Storm' in aux_str or 'storm' in aux_str)):
                count_reference_PACKETSTORM+=1
            elif('codeaurora' in aux_str):
                count_reference_CODEAURORA+=1
            else:
                count_reference_ANOTHER+=1
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
#Comprobamos el contenido de nombre de referencia
for r in range(0,len(df_vulnibm_sh["x_xfe_references_link_name"])):
    if((",") in (df_vulnibm_sh["x_xfe_references_link_name"][r])):
        #Si hay varios valores de referencias en la misma fila, separo cada uno de los valores
        aux_refname_vulnibm_sh = df_vulnibm_sh["x_xfe_references_link_name"][r].split(',')
        #Inserto cada valor de name de cada fila en el vector donde estaran todos los valores de name, quitando algunos caracteres especiales y espacios
        for j in range(0,len(aux_refname_vulnibm_sh)):
            aux_str=aux_refname_vulnibm_sh[j].replace('[','').replace(']','').replace("'","").replace("","")
            if(aux_str!='NONE' and 'CVE' not in aux_str):
                count_references+=1
                if('IBM' in aux_str):
                    count_reference_IBM+=1
                elif('GitHub' in aux_str or 'GITHub' in aux_str or 'github' in aux_str):
                    count_reference_GITHUB+=1
                elif('INTEL' in aux_str or 'Intel' in aux_str or 'intel' in aux_str ):
                    count_reference_INTEL+=1
                elif('Apple' in aux_str or 'apple' in aux_str):
                    count_reference_APPLE+=1
                elif('Mend' in aux_str):
                    count_reference_MEND+=1
                elif('Cisco' in aux_str or 'CISCO' in aux_str or 'cisco' in aux_str):
                    count_reference_CISCO+=1
                elif('Mediatek' in aux_str or 'MediaTek' in aux_str):
                    count_reference_MEDIATEK+=1
                elif('Microsoft' in aux_str or 'microsoft' in aux_str):
                    count_reference_MICROSOFT+=1
                elif('Lenovo' in aux_str or 'lenovo' in aux_str):
                    count_reference_LENOVO+=1
                elif('Dell' in aux_str):
                    count_reference_DELL+=1
                elif('Mozilla' in aux_str or 'mozilla' in aux_str):
                    count_reference_MOZILLA+=1
                elif('Adobe' in aux_str or 'adobe' in aux_str):
                    count_reference_ADOBE+=1
                elif('Siemens' in aux_str or 'siemens' in aux_str):
                    count_reference_SIEMENS+=1
                elif('Apache' in aux_str or 'apache' in aux_str):
                    count_reference_APACHE+=1
                elif('NPM' in aux_str):
                    count_reference_NPM+=1
                elif('SNYK' in aux_str):
                    count_reference_SYNK+=1
                elif('Oracle' in aux_str or 'oracle' in aux_str):
                    count_reference_ORACLE+=1

                elif('Fortiguard' in aux_str or 'fortiguard' in aux_str):
                    count_reference_FORTIGUARD+=1

                elif('Contec' in aux_str or 'contec' in aux_str):
                    count_reference_CONTEC+=1
                elif('Qualcomm' in aux_str or 'qualcomm' in aux_str):
                    count_reference_QUALCOMM+=1
                elif('Talos' in aux_str or 'TALOS' in aux_str):
                    count_reference_TALOS+=1
                elif('dlink' in aux_str):
                    count_reference_DLINK+=1
                elif('ptc' in aux_str or 'PTC' in aux_str):
                    count_reference_PTC+=1
                elif('symbiote' in aux_str or 'Symbiote' in aux_str ):
                    count_reference_SYMBIOTE+=1
                elif('asus' in aux_str or 'Asus' in aux_str):
                    count_reference_ASUS+=1

                elif('iot.konker' in aux_str):
                    count_reference_IOTKONKER+=1
                elif('vulncheck' in aux_str):
                    count_reference_VULNCHECK+=1
                elif('xiongmaitech' in aux_str):
                    count_reference_XIONGMAITECH+=1

                elif('riot' in aux_str):
                    count_reference_RIOT+=1
                elif('eclipse' in aux_str):
                    count_reference_ECLIPSE+=1
                elif('bosch' in aux_str):
                    count_reference_BOSCH+=1
                elif('cisa.gov' in aux_str):
                    count_reference_CISAGOV+=1
                elif('-cert' in aux_str):
                    count_reference_CERT+=1
                elif(('packet' in aux_str or 'Packet' in aux_str) and ('Storm' in aux_str or 'storm' in aux_str)):
                    count_reference_PACKETSTORM+=1
                elif('codeaurora' in aux_str):
                    count_reference_CODEAURORA+=1
                else:
                    count_reference_ANOTHER+=1
                    
                
                    
                
    else:
    
        #Obtengo el valor de nombre de referencia y aumento contadores segun el tipo que sea
        aux_str=df_vulnibm_sh["x_xfe_references_link_name"][r].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
        if(aux_str!='NONE' and 'CVE' not in aux_str):
            count_references+=1
            if('IBM' in aux_str):
                count_reference_IBM+=1
            elif('GitHub' in aux_str or 'GITHub' in aux_str or 'github' in aux_str):
                count_reference_GITHUB+=1
            elif('INTEL' in aux_str or 'Intel' in aux_str or 'intel' in aux_str ):
                count_reference_INTEL+=1
            elif('Apple' in aux_str or 'apple' in aux_str):
                count_reference_APPLE+=1
            elif('Mend' in aux_str):
                count_reference_MEND+=1
            elif('Cisco' in aux_str or 'CISCO' in aux_str or 'cisco' in aux_str):
                count_reference_CISCO+=1
            elif('Mediatek' in aux_str or 'MediaTek' in aux_str):
                count_reference_MEDIATEK+=1
            elif('Microsoft' in aux_str or 'microsoft' in aux_str):
                count_reference_MICROSOFT+=1
            elif('Lenovo' in aux_str or 'lenovo' in aux_str):
                count_reference_LENOVO+=1
            elif('Dell' in aux_str):
                count_reference_DELL+=1
            elif('Mozilla' in aux_str or 'mozilla' in aux_str):
                count_reference_MOZILLA+=1
            elif('Adobe' in aux_str or 'adobe' in aux_str):
                count_reference_ADOBE+=1
            elif('Siemens' in aux_str or 'siemens' in aux_str):
                count_reference_SIEMENS+=1
            elif('Apache' in aux_str or 'apache' in aux_str):
                count_reference_APACHE+=1
            elif('NPM' in aux_str):
                count_reference_NPM+=1
            elif('SNYK' in aux_str):
                count_reference_SYNK+=1
            elif('Oracle' in aux_str or 'oracle' in aux_str):
                count_reference_ORACLE+=1

            elif('Fortiguard' in aux_str or 'fortiguard' in aux_str):
                count_reference_FORTIGUARD+=1

            elif('Contec' in aux_str or 'contec' in aux_str):
                count_reference_CONTEC+=1
            elif('Qualcomm' in aux_str or 'qualcomm' in aux_str):
                count_reference_QUALCOMM+=1
            elif('Talos' in aux_str or 'TALOS' in aux_str):
                count_reference_TALOS+=1
            elif('dlink' in aux_str):
                count_reference_DLINK+=1
            elif('ptc' in aux_str or 'PTC' in aux_str):
                count_reference_PTC+=1
            elif('symbiote' in aux_str or 'Symbiote' in aux_str ):
                count_reference_SYMBIOTE+=1
            elif('asus' in aux_str or 'Asus' in aux_str):
                count_reference_ASUS+=1

            elif('iot.konker' in aux_str):
                count_reference_IOTKONKER+=1
            elif('vulncheck' in aux_str):
                count_reference_VULNCHECK+=1
            elif('xiongmaitech' in aux_str):
                count_reference_XIONGMAITECH+=1

            elif('riot' in aux_str):
                count_reference_RIOT+=1
            elif('eclipse' in aux_str):
                count_reference_ECLIPSE+=1
            elif('bosch' in aux_str):
                count_reference_BOSCH+=1
            elif('cisa.gov' in aux_str):
                count_reference_CISAGOV+=1
            elif('-cert' in aux_str):
                count_reference_CERT+=1
            elif(('packet' in aux_str or 'Packet' in aux_str) and ('Storm' in aux_str or 'storm' in aux_str)):
                count_reference_PACKETSTORM+=1
            elif('codeaurora' in aux_str):
                count_reference_CODEAURORA+=1
            else:
                count_reference_ANOTHER+=1
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
#Comprobamos el contenido de nombre de referencia
for r in range(0,len(df_cve_iot["CVE_Items.cve.references.reference_data.name"])):
    if(isinstance(df_cve_iot["CVE_Items.cve.references.reference_data.name"][r],float) == False):
        if((",") in (df_cve_iot["CVE_Items.cve.references.reference_data.name"][r])):
            #Si hay varios valores de referencias en la misma fila, separo cada uno de los valores
            aux_refname_cve_iot = df_cve_iot["CVE_Items.cve.references.reference_data.name"][r].split(',')
            #Inserto cada valor de name de cada fila en el vector donde estaran todos los valores de name, quitando algunos caracteres especiales y espacios
            for j in range(0,len(aux_refname_cve_iot)):
                aux_str=aux_refname_cve_iot[j].replace('[','').replace(']','').replace("'","").replace("","")
                if(aux_str!='NONE' and 'CVE' not in aux_str):
                    count_references+=1
                    if('IBM' in aux_str):
                        count_reference_IBM+=1
                    elif('GitHub' in aux_str or 'GITHub' in aux_str or 'github' in aux_str):
                        count_reference_GITHUB+=1
                    elif('INTEL' in aux_str or 'Intel' in aux_str or 'intel' in aux_str ):
                        count_reference_INTEL+=1
                    elif('Apple' in aux_str or 'apple' in aux_str):
                        count_reference_APPLE+=1
                    elif('Mend' in aux_str):
                        count_reference_MEND+=1
                    elif('Cisco' in aux_str or 'CISCO' in aux_str or 'cisco' in aux_str):
                        count_reference_CISCO+=1
                    elif('Mediatek' in aux_str or 'MediaTek' in aux_str):
                        count_reference_MEDIATEK+=1
                    elif('Microsoft' in aux_str or 'microsoft' in aux_str):
                        count_reference_MICROSOFT+=1
                    elif('Lenovo' in aux_str or 'lenovo' in aux_str):
                        count_reference_LENOVO+=1
                    elif('Dell' in aux_str):
                        count_reference_DELL+=1
                    elif('Mozilla' in aux_str or 'mozilla' in aux_str):
                        count_reference_MOZILLA+=1
                    elif('Adobe' in aux_str or 'adobe' in aux_str):
                        count_reference_ADOBE+=1
                    elif('Siemens' in aux_str or 'siemens' in aux_str):
                        count_reference_SIEMENS+=1
                    elif('Apache' in aux_str or 'apache' in aux_str):
                        count_reference_APACHE+=1
                    elif('NPM' in aux_str):
                        count_reference_NPM+=1
                    elif('SNYK' in aux_str):
                        count_reference_SYNK+=1
                    elif('Oracle' in aux_str or 'oracle' in aux_str):
                        count_reference_ORACLE+=1

                    elif('Fortiguard' in aux_str or 'fortiguard' in aux_str):
                        count_reference_FORTIGUARD+=1

                    elif('Contec' in aux_str or 'contec' in aux_str):
                        count_reference_CONTEC+=1
                    elif('Qualcomm' in aux_str or 'qualcomm' in aux_str):
                        count_reference_QUALCOMM+=1
                    elif('Talos' in aux_str or 'TALOS' in aux_str):
                        count_reference_TALOS+=1
                    elif('dlink' in aux_str):
                        count_reference_DLINK+=1
                    elif('ptc' in aux_str or 'PTC' in aux_str):
                        count_reference_PTC+=1
                    elif('symbiote' in aux_str or 'Symbiote' in aux_str ):
                        count_reference_SYMBIOTE+=1
                    elif('asus' in aux_str or 'Asus' in aux_str):
                        count_reference_ASUS+=1

                    elif('iot.konker' in aux_str):
                        count_reference_IOTKONKER+=1
                    elif('vulncheck' in aux_str):
                        count_reference_VULNCHECK+=1
                    elif('xiongmaitech' in aux_str):
                        count_reference_XIONGMAITECH+=1

                    elif('riot' in aux_str):
                        count_reference_RIOT+=1
                    elif('eclipse' in aux_str):
                        count_reference_ECLIPSE+=1
                    elif('bosch' in aux_str):
                        count_reference_BOSCH+=1
                    elif('cisa.gov' in aux_str):
                        count_reference_CISAGOV+=1
                    elif('-cert' in aux_str):
                        count_reference_CERT+=1
                    elif(('packet' in aux_str or 'Packet' in aux_str) and ('Storm' in aux_str or 'storm' in aux_str)):
                        count_reference_PACKETSTORM+=1
                    elif('codeaurora' in aux_str):
                        count_reference_CODEAURORA+=1
                    else:
                        count_reference_ANOTHER+=1







        else:

            #Obtengo el valor de nombre de referencia y aumento contadores segun el tipo que sea
            aux_str=df_cve_iot["CVE_Items.cve.references.reference_data.name"][r].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
            if(aux_str!='NONE' and 'CVE' not in aux_str):
                count_references+=1
                if('IBM' in aux_str):
                    count_reference_IBM+=1
                elif('GitHub' in aux_str or 'GITHub' in aux_str or 'github' in aux_str):
                    count_reference_GITHUB+=1
                elif('INTEL' in aux_str or 'Intel' in aux_str or 'intel' in aux_str ):
                    count_reference_INTEL+=1
                elif('Apple' in aux_str or 'apple' in aux_str):
                    count_reference_APPLE+=1
                elif('Mend' in aux_str):
                    count_reference_MEND+=1
                elif('Cisco' in aux_str or 'CISCO' in aux_str or 'cisco' in aux_str):
                    count_reference_CISCO+=1
                elif('Mediatek' in aux_str or 'MediaTek' in aux_str):
                    count_reference_MEDIATEK+=1
                elif('Microsoft' in aux_str or 'microsoft' in aux_str):
                    count_reference_MICROSOFT+=1
                elif('Lenovo' in aux_str or 'lenovo' in aux_str):
                    count_reference_LENOVO+=1
                elif('Dell' in aux_str):
                    count_reference_DELL+=1
                elif('Mozilla' in aux_str or 'mozilla' in aux_str):
                    count_reference_MOZILLA+=1
                elif('Adobe' in aux_str or 'adobe' in aux_str):
                    count_reference_ADOBE+=1
                elif('Siemens' in aux_str or 'siemens' in aux_str):
                    count_reference_SIEMENS+=1
                elif('Apache' in aux_str or 'apache' in aux_str):
                    count_reference_APACHE+=1
                elif('NPM' in aux_str):
                    count_reference_NPM+=1
                elif('SNYK' in aux_str):
                    count_reference_SYNK+=1
                elif('Oracle' in aux_str or 'oracle' in aux_str):
                    count_reference_ORACLE+=1

                elif('Fortiguard' in aux_str or 'fortiguard' in aux_str):
                    count_reference_FORTIGUARD+=1

                elif('Contec' in aux_str or 'contec' in aux_str):
                    count_reference_CONTEC+=1
                elif('Qualcomm' in aux_str or 'qualcomm' in aux_str):
                    count_reference_QUALCOMM+=1
                elif('Talos' in aux_str or 'TALOS' in aux_str):
                    count_reference_TALOS+=1
                elif('dlink' in aux_str):
                    count_reference_DLINK+=1
                elif('ptc' in aux_str or 'PTC' in aux_str):
                    count_reference_PTC+=1
                elif('symbiote' in aux_str or 'Symbiote' in aux_str ):
                    count_reference_SYMBIOTE+=1
                elif('asus' in aux_str or 'Asus' in aux_str):
                    count_reference_ASUS+=1

                elif('iot.konker' in aux_str):
                    count_reference_IOTKONKER+=1
                elif('vulncheck' in aux_str):
                    count_reference_VULNCHECK+=1
                elif('xiongmaitech' in aux_str):
                    count_reference_XIONGMAITECH+=1

                elif('riot' in aux_str):
                    count_reference_RIOT+=1
                elif('eclipse' in aux_str):
                    count_reference_ECLIPSE+=1
                elif('bosch' in aux_str):
                    count_reference_BOSCH+=1
                elif('cisa.gov' in aux_str):
                    count_reference_CISAGOV+=1
                elif('-cert' in aux_str):
                    count_reference_CERT+=1
                elif(('packet' in aux_str or 'Packet' in aux_str) and ('Storm' in aux_str or 'storm' in aux_str)):
                    count_reference_PACKETSTORM+=1
                elif('codeaurora' in aux_str):
                    count_reference_CODEAURORA+=1
                else:
                    count_reference_ANOTHER+=1

    
    
    
    
    
    
    
    
    
    
    
#Comprobamos el contenido de nombre de referencia
for r in range(0,len(df_cve_sh["CVE_Items.cve.references.reference_data.name"])):
    if(isinstance(df_cve_sh["CVE_Items.cve.references.reference_data.name"][r],float) == False):
        if((",") in (df_cve_sh["CVE_Items.cve.references.reference_data.name"][r])):
            #Si hay varios valores de referencias en la misma fila, separo cada uno de los valores
            aux_refname_cve_sh = df_cve_sh["CVE_Items.cve.references.reference_data.name"][r].split(',')
            #Inserto cada valor de name de cada fila en el vector donde estaran todos los valores de name, quitando algunos caracteres especiales y espacios
            for j in range(0,len(aux_refname_cve_sh)):
                aux_str=aux_refname_cve_sh[j].replace('[','').replace(']','').replace("'","").replace("","")
                if(aux_str!='NONE' and 'CVE' not in aux_str):
                    count_references+=1
                    if('IBM' in aux_str):
                        count_reference_IBM+=1
                    elif('GitHub' in aux_str or 'GITHub' in aux_str or 'github' in aux_str):
                        count_reference_GITHUB+=1
                    elif('INTEL' in aux_str or 'Intel' in aux_str or 'intel' in aux_str ):
                        count_reference_INTEL+=1
                    elif('Apple' in aux_str or 'apple' in aux_str):
                        count_reference_APPLE+=1
                    elif('Mend' in aux_str):
                        count_reference_MEND+=1
                    elif('Cisco' in aux_str or 'CISCO' in aux_str or 'cisco' in aux_str):
                        count_reference_CISCO+=1
                    elif('Mediatek' in aux_str or 'MediaTek' in aux_str):
                        count_reference_MEDIATEK+=1
                    elif('Microsoft' in aux_str or 'microsoft' in aux_str):
                        count_reference_MICROSOFT+=1
                    elif('Lenovo' in aux_str or 'lenovo' in aux_str):
                        count_reference_LENOVO+=1
                    elif('Dell' in aux_str):
                        count_reference_DELL+=1
                    elif('Mozilla' in aux_str or 'mozilla' in aux_str):
                        count_reference_MOZILLA+=1
                    elif('Adobe' in aux_str or 'adobe' in aux_str):
                        count_reference_ADOBE+=1
                    elif('Siemens' in aux_str or 'siemens' in aux_str):
                        count_reference_SIEMENS+=1
                    elif('Apache' in aux_str or 'apache' in aux_str):
                        count_reference_APACHE+=1
                    elif('NPM' in aux_str):
                        count_reference_NPM+=1
                    elif('SNYK' in aux_str):
                        count_reference_SYNK+=1
                    elif('Oracle' in aux_str or 'oracle' in aux_str):
                        count_reference_ORACLE+=1

                    elif('Fortiguard' in aux_str or 'fortiguard' in aux_str):
                        count_reference_FORTIGUARD+=1

                    elif('Contec' in aux_str or 'contec' in aux_str):
                        count_reference_CONTEC+=1
                    elif('Qualcomm' in aux_str or 'qualcomm' in aux_str):
                        count_reference_QUALCOMM+=1
                    elif('Talos' in aux_str or 'TALOS' in aux_str):
                        count_reference_TALOS+=1
                    elif('dlink' in aux_str):
                        count_reference_DLINK+=1
                    elif('ptc' in aux_str or 'PTC' in aux_str):
                        count_reference_PTC+=1
                    elif('symbiote' in aux_str or 'Symbiote' in aux_str ):
                        count_reference_SYMBIOTE+=1
                    elif('asus' in aux_str or 'Asus' in aux_str):
                        count_reference_ASUS+=1

                    elif('iot.konker' in aux_str):
                        count_reference_IOTKONKER+=1
                    elif('vulncheck' in aux_str):
                        count_reference_VULNCHECK+=1
                    elif('xiongmaitech' in aux_str):
                        count_reference_XIONGMAITECH+=1

                    elif('riot' in aux_str):
                        count_reference_RIOT+=1
                    elif('eclipse' in aux_str):
                        count_reference_ECLIPSE+=1
                    elif('bosch' in aux_str):
                        count_reference_BOSCH+=1
                    elif('cisa.gov' in aux_str):
                        count_reference_CISAGOV+=1
                    elif('-cert' in aux_str):
                        count_reference_CERT+=1
                    elif(('packet' in aux_str or 'Packet' in aux_str) and ('Storm' in aux_str or 'storm' in aux_str)):
                        count_reference_PACKETSTORM+=1
                    elif('codeaurora' in aux_str):
                        count_reference_CODEAURORA+=1
                    else:
                        count_reference_ANOTHER+=1




        else:

            #Obtengo el valor de nombre de referencia y aumento contadores segun el tipo que sea
            aux_str=df_cve_sh["CVE_Items.cve.references.reference_data.name"][r].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
            if(aux_str!='NONE' and 'CVE' not in aux_str):
                count_references+=1
                if('IBM' in aux_str):
                    count_reference_IBM+=1
                elif('GitHub' in aux_str or 'GITHub' in aux_str or 'github' in aux_str):
                    count_reference_GITHUB+=1
                elif('INTEL' in aux_str or 'Intel' in aux_str or 'intel' in aux_str ):
                    count_reference_INTEL+=1
                elif('Apple' in aux_str or 'apple' in aux_str):
                    count_reference_APPLE+=1
                elif('Mend' in aux_str):
                    count_reference_MEND+=1
                elif('Cisco' in aux_str or 'CISCO' in aux_str or 'cisco' in aux_str):
                    count_reference_CISCO+=1
                elif('Mediatek' in aux_str or 'MediaTek' in aux_str):
                    count_reference_MEDIATEK+=1
                elif('Microsoft' in aux_str or 'microsoft' in aux_str):
                    count_reference_MICROSOFT+=1
                elif('Lenovo' in aux_str or 'lenovo' in aux_str):
                    count_reference_LENOVO+=1
                elif('Dell' in aux_str):
                    count_reference_DELL+=1
                elif('Mozilla' in aux_str or 'mozilla' in aux_str):
                    count_reference_MOZILLA+=1
                elif('Adobe' in aux_str or 'adobe' in aux_str):
                    count_reference_ADOBE+=1
                elif('Siemens' in aux_str or 'siemens' in aux_str):
                    count_reference_SIEMENS+=1
                elif('Apache' in aux_str or 'apache' in aux_str):
                    count_reference_APACHE+=1
                elif('NPM' in aux_str):
                    count_reference_NPM+=1
                elif('SNYK' in aux_str):
                    count_reference_SYNK+=1
                elif('Oracle' in aux_str or 'oracle' in aux_str):
                    count_reference_ORACLE+=1

                elif('Fortiguard' in aux_str or 'fortiguard' in aux_str):
                    count_reference_FORTIGUARD+=1

                elif('Contec' in aux_str or 'contec' in aux_str):
                    count_reference_CONTEC+=1
                elif('Qualcomm' in aux_str or 'qualcomm' in aux_str):
                    count_reference_QUALCOMM+=1
                elif('Talos' in aux_str or 'TALOS' in aux_str):
                    count_reference_TALOS+=1
                elif('dlink' in aux_str):
                    count_reference_DLINK+=1
                elif('ptc' in aux_str or 'PTC' in aux_str):
                    count_reference_PTC+=1
                elif('symbiote' in aux_str or 'Symbiote' in aux_str ):
                    count_reference_SYMBIOTE+=1
                elif('asus' in aux_str or 'Asus' in aux_str):
                    count_reference_ASUS+=1

                elif('iot.konker' in aux_str):
                    count_reference_IOTKONKER+=1
                elif('vulncheck' in aux_str):
                    count_reference_VULNCHECK+=1
                elif('xiongmaitech' in aux_str):
                    count_reference_XIONGMAITECH+=1

                elif('riot' in aux_str):
                    count_reference_RIOT+=1
                elif('eclipse' in aux_str):
                    count_reference_ECLIPSE+=1
                elif('bosch' in aux_str):
                    count_reference_BOSCH+=1
                elif('cisa.gov' in aux_str):
                    count_reference_CISAGOV+=1
                elif('-cert' in aux_str):
                    count_reference_CERT+=1
                elif(('packet' in aux_str or 'Packet' in aux_str) and ('Storm' in aux_str or 'storm' in aux_str)):
                    count_reference_PACKETSTORM+=1
                elif('codeaurora' in aux_str):
                    count_reference_CODEAURORA+=1
                else:
                    count_reference_ANOTHER+=1







                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
#Comprobamos el contenido de nombre de referencia
for r in range(0,len(df_cpe_sh["cpes.refs.ref"])):
    if((",") in (df_cpe_sh["cpes.refs.ref"][r])):
        #Si hay varios valores de referencias en la misma fila, separo cada uno de los valores
        aux_refname_cpe_sh = df_cpe_sh["cpes.refs.ref"][r].split(',')
        #Inserto cada valor de name de cada fila en el vector donde estaran todos los valores de name, quitando algunos caracteres especiales y espacios
        for j in range(0,len(aux_refname_cpe_sh)):
            aux_str=aux_refname_cpe_sh[j].replace('[','').replace(']','').replace("'","").replace("","")
            if(aux_str!='NONE' and 'CVE' not in aux_str):
                count_references+=1
                if('IBM' in aux_str):
                    count_reference_IBM+=1
                elif('GitHub' in aux_str or 'GITHub' in aux_str or 'github' in aux_str):
                    count_reference_GITHUB+=1
                elif('INTEL' in aux_str or 'Intel' in aux_str or 'intel' in aux_str ):
                    count_reference_INTEL+=1
                elif('Apple' in aux_str or 'apple' in aux_str):
                    count_reference_APPLE+=1
                elif('Mend' in aux_str):
                    count_reference_MEND+=1
                elif('Cisco' in aux_str or 'CISCO' in aux_str or 'cisco' in aux_str):
                    count_reference_CISCO+=1
                elif('Mediatek' in aux_str or 'MediaTek' in aux_str):
                    count_reference_MEDIATEK+=1
                elif('Microsoft' in aux_str or 'microsoft' in aux_str):
                    count_reference_MICROSOFT+=1
                elif('Lenovo' in aux_str or 'lenovo' in aux_str):
                    count_reference_LENOVO+=1
                elif('Dell' in aux_str):
                    count_reference_DELL+=1
                elif('Mozilla' in aux_str or 'mozilla' in aux_str):
                    count_reference_MOZILLA+=1
                elif('Adobe' in aux_str or 'adobe' in aux_str):
                    count_reference_ADOBE+=1
                elif('Siemens' in aux_str or 'siemens' in aux_str):
                    count_reference_SIEMENS+=1
                elif('Apache' in aux_str or 'apache' in aux_str):
                    count_reference_APACHE+=1
                elif('NPM' in aux_str):
                    count_reference_NPM+=1
                elif('SNYK' in aux_str):
                    count_reference_SYNK+=1
                elif('Oracle' in aux_str or 'oracle' in aux_str):
                    count_reference_ORACLE+=1

                elif('Fortiguard' in aux_str or 'fortiguard' in aux_str):
                    count_reference_FORTIGUARD+=1

                elif('Contec' in aux_str or 'contec' in aux_str):
                    count_reference_CONTEC+=1
                elif('Qualcomm' in aux_str or 'qualcomm' in aux_str):
                    count_reference_QUALCOMM+=1
                elif('Talos' in aux_str or 'TALOS' in aux_str):
                    count_reference_TALOS+=1
                elif('dlink' in aux_str):
                    count_reference_DLINK+=1
                elif('ptc' in aux_str or 'PTC' in aux_str):
                    count_reference_PTC+=1
                elif('symbiote' in aux_str or 'Symbiote' in aux_str ):
                    count_reference_SYMBIOTE+=1
                elif('asus' in aux_str or 'Asus' in aux_str):
                    count_reference_ASUS+=1

                elif('iot.konker' in aux_str):
                    count_reference_IOTKONKER+=1
                elif('vulncheck' in aux_str):
                    count_reference_VULNCHECK+=1
                elif('xiongmaitech' in aux_str):
                    count_reference_XIONGMAITECH+=1

                elif('riot' in aux_str):
                    count_reference_RIOT+=1
                elif('eclipse' in aux_str):
                    count_reference_ECLIPSE+=1
                elif('bosch' in aux_str):
                    count_reference_BOSCH+=1
                elif('cisa.gov' in aux_str):
                    count_reference_CISAGOV+=1
                elif('-cert' in aux_str):
                    count_reference_CERT+=1
                elif(('packet' in aux_str or 'Packet' in aux_str) and ('Storm' in aux_str or 'storm' in aux_str)):
                    count_reference_PACKETSTORM+=1
                elif('codeaurora' in aux_str):
                    count_reference_CODEAURORA+=1
                else:
                    count_reference_ANOTHER+=1
    else:
    
        #Obtengo el valor de nombre de referencia y aumento contadores segun el tipo que sea
        aux_str=df_cpe_sh["cpes.refs.ref"][r].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
        if(aux_str!='NONE' and 'CVE' not in aux_str):
            count_references+=1
            if('IBM' in aux_str):
                count_reference_IBM+=1
            elif('GitHub' in aux_str or 'GITHub' in aux_str or 'github' in aux_str):
                count_reference_GITHUB+=1
            elif('INTEL' in aux_str or 'Intel' in aux_str or 'intel' in aux_str ):
                count_reference_INTEL+=1
            elif('Apple' in aux_str or 'apple' in aux_str):
                count_reference_APPLE+=1
            elif('Mend' in aux_str):
                count_reference_MEND+=1
            elif('Cisco' in aux_str or 'CISCO' in aux_str or 'cisco' in aux_str):
                count_reference_CISCO+=1
            elif('Mediatek' in aux_str or 'MediaTek' in aux_str):
                count_reference_MEDIATEK+=1
            elif('Microsoft' in aux_str or 'microsoft' in aux_str):
                count_reference_MICROSOFT+=1
            elif('Lenovo' in aux_str or 'lenovo' in aux_str):
                count_reference_LENOVO+=1
            elif('Dell' in aux_str):
                count_reference_DELL+=1
            elif('Mozilla' in aux_str or 'mozilla' in aux_str):
                count_reference_MOZILLA+=1
            elif('Adobe' in aux_str or 'adobe' in aux_str):
                count_reference_ADOBE+=1
            elif('Siemens' in aux_str or 'siemens' in aux_str):
                count_reference_SIEMENS+=1
            elif('Apache' in aux_str or 'apache' in aux_str):
                count_reference_APACHE+=1
            elif('NPM' in aux_str):
                count_reference_NPM+=1
            elif('SNYK' in aux_str):
                count_reference_SYNK+=1
            elif('Oracle' in aux_str or 'oracle' in aux_str):
                count_reference_ORACLE+=1

            elif('Fortiguard' in aux_str or 'fortiguard' in aux_str):
                count_reference_FORTIGUARD+=1

            elif('Contec' in aux_str or 'contec' in aux_str):
                count_reference_CONTEC+=1
            elif('Qualcomm' in aux_str or 'qualcomm' in aux_str):
                count_reference_QUALCOMM+=1
            elif('Talos' in aux_str or 'TALOS' in aux_str):
                count_reference_TALOS+=1
            elif('dlink' in aux_str):
                count_reference_DLINK+=1
            elif('ptc' in aux_str or 'PTC' in aux_str):
                count_reference_PTC+=1
            elif('symbiote' in aux_str or 'Symbiote' in aux_str ):
                count_reference_SYMBIOTE+=1
            elif('asus' in aux_str or 'Asus' in aux_str):
                count_reference_ASUS+=1

            elif('iot.konker' in aux_str):
                count_reference_IOTKONKER+=1
            elif('vulncheck' in aux_str):
                count_reference_VULNCHECK+=1
            elif('xiongmaitech' in aux_str):
                count_reference_XIONGMAITECH+=1

            elif('riot' in aux_str):
                count_reference_RIOT+=1
            elif('eclipse' in aux_str):
                count_reference_ECLIPSE+=1
            elif('bosch' in aux_str):
                count_reference_BOSCH+=1
            elif('cisa.gov' in aux_str):
                count_reference_CISAGOV+=1
            elif('-cert' in aux_str):
                count_reference_CERT+=1
            elif(('packet' in aux_str or 'Packet' in aux_str) and ('Storm' in aux_str or 'storm' in aux_str)):
                count_reference_PACKETSTORM+=1
            elif('codeaurora' in aux_str):
                count_reference_CODEAURORA+=1
            else:
                count_reference_ANOTHER+=1
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
#Comprobamos el contenido de nombre de referencia
for r in range(0,len(df_cpe_iot["cpes.refs.ref"])):
    if((",") in (df_cpe_iot["cpes.refs.ref"][r])):
        #Si hay varios valores de referencias en la misma fila, separo cada uno de los valores
        aux_refname_cpe_iot = df_cpe_iot["cpes.refs.ref"][r].split(',')
        #Inserto cada valor de name de cada fila en el vector donde estaran todos los valores de name, quitando algunos caracteres especiales y espacios
        for j in range(0,len(aux_refname_cpe_iot)):
            aux_str=aux_refname_cpe_iot[j].replace('[','').replace(']','').replace("'","").replace("","")
            if(aux_str!='NONE' and 'CVE' not in aux_str):
                count_references+=1
                if('IBM' in aux_str):
                    count_reference_IBM+=1
                elif('GitHub' in aux_str or 'GITHub' in aux_str or 'github' in aux_str):
                    count_reference_GITHUB+=1
                elif('INTEL' in aux_str or 'Intel' in aux_str or 'intel' in aux_str ):
                    count_reference_INTEL+=1
                elif('Apple' in aux_str or 'apple' in aux_str):
                    count_reference_APPLE+=1
                elif('Mend' in aux_str):
                    count_reference_MEND+=1
                elif('Cisco' in aux_str or 'CISCO' in aux_str or 'cisco' in aux_str):
                    count_reference_CISCO+=1
                elif('Mediatek' in aux_str or 'MediaTek' in aux_str):
                    count_reference_MEDIATEK+=1
                elif('Microsoft' in aux_str or 'microsoft' in aux_str):
                    count_reference_MICROSOFT+=1
                elif('Lenovo' in aux_str or 'lenovo' in aux_str):
                    count_reference_LENOVO+=1
                elif('Dell' in aux_str):
                    count_reference_DELL+=1
                elif('Mozilla' in aux_str or 'mozilla' in aux_str):
                    count_reference_MOZILLA+=1
                elif('Adobe' in aux_str or 'adobe' in aux_str):
                    count_reference_ADOBE+=1
                elif('Siemens' in aux_str or 'siemens' in aux_str):
                    count_reference_SIEMENS+=1
                elif('Apache' in aux_str or 'apache' in aux_str):
                    count_reference_APACHE+=1
                elif('NPM' in aux_str):
                    count_reference_NPM+=1
                elif('SNYK' in aux_str):
                    count_reference_SYNK+=1
                elif('Oracle' in aux_str or 'oracle' in aux_str):
                    count_reference_ORACLE+=1

                elif('Fortiguard' in aux_str or 'fortiguard' in aux_str):
                    count_reference_FORTIGUARD+=1

                elif('Contec' in aux_str or 'contec' in aux_str):
                    count_reference_CONTEC+=1
                elif('Qualcomm' in aux_str or 'qualcomm' in aux_str):
                    count_reference_QUALCOMM+=1
                elif('Talos' in aux_str or 'TALOS' in aux_str):
                    count_reference_TALOS+=1
                elif('dlink' in aux_str):
                    count_reference_DLINK+=1
                elif('ptc' in aux_str or 'PTC' in aux_str):
                    count_reference_PTC+=1
                elif('symbiote' in aux_str or 'Symbiote' in aux_str ):
                    count_reference_SYMBIOTE+=1
                elif('asus' in aux_str or 'Asus' in aux_str):
                    count_reference_ASUS+=1

                elif('iot.konker' in aux_str):
                    count_reference_IOTKONKER+=1
                elif('vulncheck' in aux_str):
                    count_reference_VULNCHECK+=1
                elif('xiongmaitech' in aux_str):
                    count_reference_XIONGMAITECH+=1

                elif('riot' in aux_str):
                    count_reference_RIOT+=1
                elif('eclipse' in aux_str):
                    count_reference_ECLIPSE+=1
                elif('bosch' in aux_str):
                    count_reference_BOSCH+=1
                elif('cisa.gov' in aux_str):
                    count_reference_CISAGOV+=1
                elif('-cert' in aux_str):
                    count_reference_CERT+=1
                elif(('packet' in aux_str or 'Packet' in aux_str) and ('Storm' in aux_str or 'storm' in aux_str)):
                    count_reference_PACKETSTORM+=1
                elif('codeaurora' in aux_str):
                    count_reference_CODEAURORA+=1
                else:
                    count_reference_ANOTHER+=1

                
                    
                
    else:
    
        #Obtengo el valor de nombre de referencia y aumento contadores segun el tipo que sea
        aux_str=df_cpe_iot["cpes.refs.ref"][r].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
        if(aux_str!='NONE' and 'CVE' not in aux_str):
            count_references+=1
            if('IBM' in aux_str):
                count_reference_IBM+=1
            elif('GitHub' in aux_str or 'GITHub' in aux_str or 'github' in aux_str):
                count_reference_GITHUB+=1
            elif('INTEL' in aux_str or 'Intel' in aux_str or 'intel' in aux_str ):
                count_reference_INTEL+=1
            elif('Apple' in aux_str or 'apple' in aux_str):
                count_reference_APPLE+=1
            elif('Mend' in aux_str):
                count_reference_MEND+=1
            elif('Cisco' in aux_str or 'CISCO' in aux_str or 'cisco' in aux_str):
                count_reference_CISCO+=1
            elif('Mediatek' in aux_str or 'MediaTek' in aux_str):
                count_reference_MEDIATEK+=1
            elif('Microsoft' in aux_str or 'microsoft' in aux_str):
                count_reference_MICROSOFT+=1
            elif('Lenovo' in aux_str or 'lenovo' in aux_str):
                count_reference_LENOVO+=1
            elif('Dell' in aux_str):
                count_reference_DELL+=1
            elif('Mozilla' in aux_str or 'mozilla' in aux_str):
                count_reference_MOZILLA+=1
            elif('Adobe' in aux_str or 'adobe' in aux_str):
                count_reference_ADOBE+=1
            elif('Siemens' in aux_str or 'siemens' in aux_str):
                count_reference_SIEMENS+=1
            elif('Apache' in aux_str or 'apache' in aux_str):
                count_reference_APACHE+=1
            elif('NPM' in aux_str):
                count_reference_NPM+=1
            elif('SNYK' in aux_str):
                count_reference_SYNK+=1
            elif('Oracle' in aux_str or 'oracle' in aux_str):
                count_reference_ORACLE+=1

            elif('Fortiguard' in aux_str or 'fortiguard' in aux_str):
                count_reference_FORTIGUARD+=1

            elif('Contec' in aux_str or 'contec' in aux_str):
                count_reference_CONTEC+=1
            elif('Qualcomm' in aux_str or 'qualcomm' in aux_str):
                count_reference_QUALCOMM+=1
            elif('Talos' in aux_str or 'TALOS' in aux_str):
                count_reference_TALOS+=1
            elif('dlink' in aux_str):
                count_reference_DLINK+=1
            elif('ptc' in aux_str or 'PTC' in aux_str):
                count_reference_PTC+=1
            elif('symbiote' in aux_str or 'Symbiote' in aux_str ):
                count_reference_SYMBIOTE+=1
            elif('asus' in aux_str or 'Asus' in aux_str):
                count_reference_ASUS+=1

            elif('iot.konker' in aux_str):
                count_reference_IOTKONKER+=1
            elif('vulncheck' in aux_str):
                count_reference_VULNCHECK+=1
            elif('xiongmaitech' in aux_str):
                count_reference_XIONGMAITECH+=1

            elif('riot' in aux_str):
                count_reference_RIOT+=1
            elif('eclipse' in aux_str):
                count_reference_ECLIPSE+=1
            elif('bosch' in aux_str):
                count_reference_BOSCH+=1
            elif('cisa.gov' in aux_str):
                count_reference_CISAGOV+=1
            elif('-cert' in aux_str):
                count_reference_CERT+=1
            elif(('packet' in aux_str or 'Packet' in aux_str) and ('Storm' in aux_str or 'storm' in aux_str)):
                count_reference_PACKETSTORM+=1
            elif('codeaurora' in aux_str):
                count_reference_CODEAURORA+=1
            else:
                count_reference_ANOTHER+=1

                    
                    
                    
                    
print("******************************ESTADÍSTICAS FUENTE DE REFERENCIAS ******************************")
print("\n")                            
                
print("\n")
print(" DE UN TOTAL DE "+str(count_references)+" VALORES DE FUENTES DE REFERENCIA :\n") 
print("\n")
print("   - LAS ESTADISTICAS DE FUENTE DE REFERENCIA SON LAS SIGUIENTES:  \n")
print("            -    EN  "+str(count_reference_IBM)+" FUENTES DE REFERENCIA , LA FUENTE DE REFERENCIA ES IBM ")
print("            -    EN  "+str(count_reference_GITHUB)+" FUENTES DE REFERENCIA , LA FUENTE DE REFERENCIA ES GITHUB")
print("            -    EN  "+str(count_reference_INTEL)+" FUENTES DE REFERENCIA , LA FUENTE DE REFERENCIA ES INTEL")
print("            -    EN  "+str(count_reference_APPLE)+" FUENTES DE REFERENCIA , LA FUENTE DE REFERENCIA ES APPLE ")
print("            -    EN  "+str(count_reference_MEND)+" FUENTES DE REFERENCIA , LA FUENTE DE REFERENCIA ES MEND VULNERABILITY DATABASE ")
print("            -    EN  "+str(count_reference_CISCO)+" FUENTES DE REFERENCIA , LA FUENTE DE REFERENCIA ES CISCO")
print("            -    EN  "+str(count_reference_MEDIATEK)+" FUENTES DE REFERENCIA , LA FUENTE DE REFERENCIA ES MEDIATEK")
print("            -    EN  "+str(count_reference_MICROSOFT)+" FUENTES DE REFERENCIA , LA FUENTE DE REFERENCIA ES MICROSOFT")
print("            -    EN  "+str(count_reference_LENOVO)+" FUENTES DE REFERENCIA , LA FUENTE DE REFERENCIA ES LENOVO ")
print("            -    EN  "+str(count_reference_DELL)+" FUENTES DE REFERENCIA , LA FUENTE DE REFERENCIA ES DELL")
print("            -    EN  "+str(count_reference_MOZILLA)+" FUENTES DE REFERENCIA , LA FUENTE DE REFERENCIA ES MOZILLA")
print("            -    EN  "+str(count_reference_ADOBE)+" FUENTES DE REFERENCIA , LA FUENTE DE REFERENCIA ES ADOBE ")
print("            -    EN  "+str(count_reference_SIEMENS)+" FUENTES DE REFERENCIA , LA FUENTE DE REFERENCIA ES SIEMENS")
print("            -    EN  "+str(count_reference_APACHE)+" FUENTES DE REFERENCIA , LA FUENTE DE REFERENCIA ES APACHE")
print("            -    EN  "+str(count_reference_NPM)+" FUENTES DE REFERENCIA , LA FUENTE DE REFERENCIA ES NPM")
print("            -    EN  "+str(count_reference_SYNK)+" FUENTES DE REFERENCIA , LA FUENTE DE REFERENCIA ES SYNK ")
print("            -    EN  "+str(count_reference_ORACLE)+" FUENTES DE REFERENCIA , LA FUENTE DE REFERENCIA ES ORACLE")
print("            -    EN  "+str(count_reference_FORTIGUARD)+" FUENTES DE REFERENCIA , LA FUENTE DE REFERENCIA ES FORTIGUARD")
print("            -    EN  "+str(count_reference_CONTEC)+" FUENTES DE REFERENCIA , LA FUENTE DE REFERENCIA ES CONTEC")
print("            -    EN  "+str(count_reference_QUALCOMM)+" FUENTES DE REFERENCIA , LA FUENTE DE REFERENCIA ES QUALCOMM ")
print("            -    EN  "+str(count_reference_TALOS)+" FUENTES DE REFERENCIA , LA FUENTE DE REFERENCIA ES TALOS")
print("            -    EN  "+str(count_reference_DLINK)+" FUENTES DE REFERENCIA , LA FUENTE DE REFERENCIA ES DLINK")
print("            -    EN  "+str(count_reference_PTC)+" FUENTES DE REFERENCIA , LA FUENTE DE REFERENCIA ES PTC")
print("            -    EN  "+str(count_reference_SYMBIOTE)+" FUENTES DE REFERENCIA , LA FUENTE DE REFERENCIA ES SYMBIOTE")
print("            -    EN  "+str(count_reference_ASUS)+" FUENTES DE REFERENCIA , LA FUENTE DE REFERENCIA ES ASUS")
print("            -    EN  "+str(count_reference_IOTKONKER)+" FUENTES DE REFERENCIA , LA FUENTE DE REFERENCIA ES IOT.KONKER")
print("            -    EN  "+str(count_reference_VULNCHECK)+" FUENTES DE REFERENCIA , LA FUENTE DE REFERENCIA ES VULNCHECK")
print("            -    EN  "+str(count_reference_XIONGMAITECH)+" FUENTES DE REFERENCIA , LA FUENTE DE REFERENCIA ES XIONGMAITECH")
print("            -    EN  "+str(count_reference_RIOT)+" FUENTES DE REFERENCIA , LA FUENTE DE REFERENCIA ES RIOT.COM")
print("            -    EN  "+str(count_reference_ECLIPSE)+" FUENTES DE REFERENCIA , LA FUENTE DE REFERENCIA ES ECLIPSE")
print("            -    EN  "+str(count_reference_BOSCH)+" FUENTES DE REFERENCIA , LA FUENTE DE REFERENCIA ES BOSCH")
print("            -    EN  "+str(count_reference_CISAGOV)+" FUENTES DE REFERENCIA , LA FUENTE DE REFERENCIA ES CISA.GOV")
print("            -    EN  "+str(count_reference_CERT)+" FUENTES DE REFERENCIA , LA FUENTE DE REFERENCIA ES US-CERT.GOV")
print("            -    EN  "+str(count_reference_PACKETSTORM)+" FUENTES DE REFERENCIA , LA FUENTE DE REFERENCIA ES PACKET STORM")
print("            -    EN  "+str(count_reference_CODEAURORA)+" FUENTES DE REFERENCIA , LA FUENTE DE REFERENCIA ES CODEAURORA.COM")
print("            -    EN  "+str(count_reference_ANOTHER)+" FUENTES DE REFERENCIA , LA FUENTE DE REFERENCIA ES OTRA DISTINTA")
print("\n")
                                    

    
    
    
    
    
    
    
print("******************************PORCENTAJES FUENTE DE REFERENCIAS ******************************")
print("\n")                            
                
print("\n")
print(" DE UN TOTAL DE "+str(count_references)+" VALORES DE FUENTES DE REFERENCIA :\n") 
print("\n")
print("   - LOS PORCENTAJES DE FUENTE DE REFERENCIA SON LOS SIGUIENTES:  \n")
print("            -    EN  EL "+str(float(((count_reference_IBM*100)/count_references)))+" % DE FUENTES DE REFERENCIA , LA FUENTE DE REFERENCIA ES IBM ")
print("            -    EN  EL "+str(float(((count_reference_GITHUB*100)/count_references)))+" % DE FUENTES DE REFERENCIA , LA FUENTE DE REFERENCIA ES GITHUB")
print("            -    EN  EL "+str(float(((count_reference_INTEL*100)/count_references)))+" % DE FUENTES DE REFERENCIA , LA FUENTE DE REFERENCIA ES INTEL")
print("            -    EN  EL "+str(float(((count_reference_APPLE*100)/count_references)))+" % DE FUENTES DE REFERENCIA , LA FUENTE DE REFERENCIA ES APPLE ")
print("            -    EN  EL "+str(float(((count_reference_MEND*100)/count_references)))+" % DE FUENTES DE REFERENCIA , LA FUENTE DE REFERENCIA ES MEND VULNERABILITY DATABASE ")
print("            -    EN  EL "+str(float(((count_reference_CISCO*100)/count_references)))+" % DE FUENTES DE REFERENCIA , LA FUENTE DE REFERENCIA ES CISCO")
print("            -    EN  EL "+str(float(((count_reference_MEDIATEK*100)/count_references)))+" % DE FUENTES DE REFERENCIA , LA FUENTE DE REFERENCIA ES MEDIATEK")
print("            -    EN  EL "+str(float(((count_reference_MICROSOFT*100)/count_references)))+" % DE FUENTES DE REFERENCIA , LA FUENTE DE REFERENCIA ES MICROSOFT")
print("            -    EN  EL "+str(float(((count_reference_LENOVO*100)/count_references)))+" % DE FUENTES DE REFERENCIA , LA FUENTE DE REFERENCIA ES LENOVO ")
print("            -    EN  EL "+str(float(((count_reference_DELL*100)/count_references)))+" % DE FUENTES DE REFERENCIA , LA FUENTE DE REFERENCIA ES DELL")
print("            -    EN  EL "+str(float(((count_reference_MOZILLA*100)/count_references)))+" % DE FUENTES DE REFERENCIA , LA FUENTE DE REFERENCIA ES MOZILLA")
print("            -    EN  EL "+str(float(((count_reference_ADOBE*100)/count_references)))+" % DE FUENTES DE REFERENCIA , LA FUENTE DE REFERENCIA ES ADOBE ")
print("            -    EN  EL "+str(float(((count_reference_SIEMENS*100)/count_references)))+" % DE FUENTES DE REFERENCIA , LA FUENTE DE REFERENCIA ES SIEMENS")
print("            -    EN  EL "+str(float(((count_reference_APACHE*100)/count_references)))+" % DE FUENTES DE REFERENCIA , LA FUENTE DE REFERENCIA ES APACHE")
print("            -    EN  EL "+str(float(((count_reference_NPM*100)/count_references)))+" % DE FUENTES DE REFERENCIA , LA FUENTE DE REFERENCIA ES NPM")
print("            -    EN  EL "+str(float(((count_reference_SYNK*100)/count_references)))+" % DE FUENTES DE REFERENCIA , LA FUENTE DE REFERENCIA ES SYNK ")
print("            -    EN  EL "+str(float(((count_reference_ORACLE*100)/count_references)))+" % DE FUENTES DE REFERENCIA , LA FUENTE DE REFERENCIA ES ORACLE")
print("            -    EN  EL "+str(float(((count_reference_FORTIGUARD*100)/count_references)))+" % DE FUENTES DE REFERENCIA , LA FUENTE DE REFERENCIA ES FORTIGUARD")
print("            -    EN  EL "+str(float(((count_reference_CONTEC*100)/count_references)))+" % DE FUENTES DE REFERENCIA , LA FUENTE DE REFERENCIA ES CONTEC")
print("            -    EN  EL "+str(float(((count_reference_QUALCOMM*100)/count_references)))+" % DE FUENTES DE REFERENCIA , LA FUENTE DE REFERENCIA ES QUALCOMM ")
print("            -    EN  EL "+str(float(((count_reference_TALOS*100)/count_references)))+" % DE FUENTES DE REFERENCIA , LA FUENTE DE REFERENCIA ES TALOS")
print("            -    EN  EL "+str(float(((count_reference_DLINK*100)/count_references)))+" % DE FUENTES DE REFERENCIA , LA FUENTE DE REFERENCIA ES DLINK")
print("            -    EN  EL "+str(float(((count_reference_PTC*100)/count_references)))+" % DE FUENTES DE REFERENCIA , LA FUENTE DE REFERENCIA ES PTC")
print("            -    EN  EL "+str(float(((count_reference_SYMBIOTE*100)/count_references)))+" % DE FUENTES DE REFERENCIA , LA FUENTE DE REFERENCIA ES SYMBIOTE")
print("            -    EN  EL "+str(float(((count_reference_ASUS*100)/count_references)))+" % DE FUENTES DE REFERENCIA , LA FUENTE DE REFERENCIA ES ASUS")
print("            -    EN  EL "+str(float(((count_reference_IOTKONKER*100)/count_references)))+" % DE FUENTES DE REFERENCIA , LA FUENTE DE REFERENCIA ES IOT.KONKER")
print("            -    EN  EL "+str(float(((count_reference_VULNCHECK*100)/count_references)))+" % DE FUENTES DE REFERENCIA , LA FUENTE DE REFERENCIA ES VULNCHECK")
print("            -    EN  EL "+str(float(((count_reference_XIONGMAITECH*100)/count_references)))+" % DE FUENTES DE REFERENCIA , LA FUENTE DE REFERENCIA ES XIONGMAITECH")
print("            -    EN  EL "+str(float(((count_reference_RIOT*100)/count_references)))+" % DE FUENTES DE REFERENCIA , LA FUENTE DE REFERENCIA ES RIOT.COM")
print("            -    EN  EL "+str(float(((count_reference_ECLIPSE*100)/count_references)))+" % DE FUENTES DE REFERENCIA , LA FUENTE DE REFERENCIA ES ECLIPSE")
print("            -    EN  EL "+str(float(((count_reference_BOSCH*100)/count_references)))+" % DE FUENTES DE REFERENCIA , LA FUENTE DE REFERENCIA ES BOSCH")
print("            -    EN  EL "+str(float(((count_reference_CISAGOV*100)/count_references)))+" % DE FUENTES DE REFERENCIA , LA FUENTE DE REFERENCIA ES CISA.GOV")
print("            -    EN  EL "+str(float(((count_reference_CERT*100)/count_references)))+" % DE FUENTES DE REFERENCIA , LA FUENTE DE REFERENCIA ES US-CERT.GOV")
print("            -    EN  EL "+str(float(((count_reference_PACKETSTORM*100)/count_references)))+" % DE FUENTES DE REFERENCIA , LA FUENTE DE REFERENCIA ES PACKET STORM")
print("            -    EN  EL "+str(float(((count_reference_CODEAURORA*100)/count_references)))+" % DE FUENTES DE REFERENCIA , LA FUENTE DE REFERENCIA ES CODEAURORA.COM")
print("            -    EN  EL "+str(float(((count_reference_ANOTHER*100)/count_references)))+" % DE FUENTES DE REFERENCIA , LA FUENTE DE REFERENCIA ES OTRA DISTINTA")
print("\n")
                                    

    
















































