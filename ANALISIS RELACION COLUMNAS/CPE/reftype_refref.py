


#*********************************************************************RELACION REF REF Y REF TYPE FICHERO CPE ******************************************************************************

import pandas as pd

#Abro los ficheros con los que voy a tratar


df_cpe_iot=pd.read_excel('cpes_iot_2023.xlsx')
df_cpe_sh=pd.read_excel('cpes_smart_home_2023.xlsx')



print("******************************TIPO DE REFERENCIA CPE/FUENTE DE REFERENCIA CPE PARTE IOT******************************")
print("\n")
print("\n")

#Contador total de referencias
counterrefs_iot=0
#Contador tipo de referencia segun la referencia dada
cpes_refgithub_iot=0
cpes_refgithub_typevendor_iot=0
cpes_refgithub_typeversion_iot=0
cpes_refgithub_typeproduct_iot=0
cpes_refgithub_typeadvisory_iot=0
cpes_refgithub_typechangelog_iot=0
cpes_refgithub_typenone_iot=0


cpes_refptc_iot=0
cpes_refptc_typevendor_iot=0
cpes_refptc_typeversion_iot=0
cpes_refptc_typeproduct_iot=0
cpes_refptc_typeadvisory_iot=0
cpes_refptc_typechangelog_iot=0
cpes_refptc_typenone_iot=0


cpes_refsymbiote_iot=0
cpes_refsymbiote_typevendor_iot=0
cpes_refsymbiote_typeversion_iot=0
cpes_refsymbiote_typeproduct_iot=0
cpes_refsymbiote_typeadvisory_iot=0
cpes_refsymbiote_typechangelog_iot=0
cpes_refsymbiote_typenone_iot=0

cpes_refasus_iot=0
cpes_refasus_typevendor_iot=0
cpes_refasus_typeversion_iot=0
cpes_refasus_typeproduct_iot=0
cpes_refasus_typeadvisory_iot=0
cpes_refasus_typechangelog_iot=0
cpes_refasus_typenone_iot=0

cpes_refiotkonker_iot=0
cpes_refiotkonker_typevendor_iot=0
cpes_refiotkonker_typeversion_iot=0
cpes_refiotkonker_typeproduct_iot=0
cpes_refiotkonker_typeadvisory_iot=0
cpes_refiotkonker_typechangelog_iot=0
cpes_refiotkonker_typenone_iot=0

cpes_refvulncheck_iot=0
cpes_refvulncheck_typevendor_iot=0
cpes_refvulncheck_typeversion_iot=0
cpes_refvulncheck_typeproduct_iot=0
cpes_refvulncheck_typeadvisory_iot=0
cpes_refvulncheck_typechangelog_iot=0
cpes_refvulncheck_typenone_iot=0

cpes_refxiongmaitech_iot=0
cpes_refxiongmaitech_typevendor_iot=0
cpes_refxiongmaitech_typeversion_iot=0
cpes_refxiongmaitech_typeproduct_iot=0
cpes_refxiongmaitech_typeadvisory_iot=0
cpes_refxiongmaitech_typechangelog_iot=0
cpes_refxiongmaitech_typenone_iot=0

cpes_refmicrosoft_iot=0
cpes_refmicrosoft_typevendor_iot=0
cpes_refmicrosoft_typeversion_iot=0
cpes_refmicrosoft_typeproduct_iot=0
cpes_refmicrosoft_typeadvisory_iot=0
cpes_refmicrosoft_typechangelog_iot=0
cpes_refmicrosoft_typenone_iot=0

cpes_refriot_iot=0
cpes_refriot_typevendor_iot=0
cpes_refriot_typeversion_iot=0
cpes_refriot_typeproduct_iot=0
cpes_refriot_typeadvisory_iot=0
cpes_refriot_typechangelog_iot=0
cpes_refriot_typenone_iot=0



#Recorro los valores de referencias
for r in range(0,len(df_cpe_iot["cpes.lastModifiedDate"])):
    if('[' in df_cpe_iot["cpes.refs.ref"][r]):
        #Obtengo los valores de referencia y tipo de referencia
        aux=df_cpe_iot["cpes.refs.ref"][r].split(",")
        auxx=df_cpe_iot["cpes.refs.type"][r].split(",")
        #Recorro los distintos valores de referencias
        for k in range(0,len(aux)):
            if(len(aux)>0):
                counterrefs_iot+=1
                #Obtengo los valores de referencia y tipo de referencia
                aux_str=aux[k].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
                auxx_str=auxx[k].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
                #Valor de referencia
                if('github' in aux_str):
                    cpes_refgithub_iot+=1  
                    #Compruebo valor de tipo de referencia
                    if(auxx_str == 'NONE'):
                        cpes_refgithub_typenone_iot+=1  
                    elif(auxx_str == 'Version'):
                        cpes_refgithub_typeversion_iot+=1  
                    elif(auxx_str == 'Product'):
                        cpes_refgithub_typeproduct_iot+=1  
                    elif(auxx_str == 'Advisory'):
                        cpes_refgithub_typeadvisory_iot+=1  
                    elif((auxx_str == 'Change Log') or (auxx_str == 'ChangeLog')):
                        cpes_refgithub_typechangelog_iot+=1  
                    elif(auxx_str == 'Vendor'):
                        cpes_refgithub_typevendor_iot+=1
                elif('ptc' in aux_str):
                    cpes_refptc_iot+=1  
                    if(auxx_str == 'NONE'):
                        cpes_refptc_typenone_iot+=1  
                    elif(auxx_str == 'Version'):
                        cpes_refptc_typeversion_iot+=1  
                    elif(auxx_str == 'Product'):
                        cpes_refptc_typeproduct_iot+=1  
                    elif(auxx_str == 'Advisory'):
                        cpes_refptc_typeadvisory_iot+=1  
                    elif((auxx_str == 'Change Log') or (auxx_str == 'ChangeLog')):
                        cpes_refptc_typechangelog_iot+=1  
                    elif(auxx_str == 'Vendor'):
                        cpes_refptc_typevendor_iot+=1    
               
                elif('symbiote.com' in aux_str):
                    cpes_refsymbiote_iot+=1  
                    if(auxx_str == 'NONE'):
                        cpes_refsymbiote_typenone_iot+=1  
                    elif(auxx_str == 'Version'):
                        cpes_refsymbiote_typeversion_iot+=1  
                    elif(auxx_str == 'Product'):
                        cpes_refsymbiote_typeproduct_iot+=1  
                    elif(auxx_str == 'Advisory'):
                        cpes_refsymbiote_typeadvisory_iot+=1  
                    elif((auxx_str == 'Change Log') or (auxx_str == 'ChangeLog')):
                        cpes_refsymbiote_typechangelog_iot+=1  
                    elif(auxx_str == 'Vendor'):
                        cpes_refsymbiote_typevendor_iot+=1   
                elif('asus.com' in aux_str):
                    cpes_refasus_iot+=1  
                    if(auxx_str == 'NONE'):
                        cpes_refasus_typenone_iot+=1  
                    elif(auxx_str == 'Version'):
                        cpes_refasus_typeversion_iot+=1  
                    elif(auxx_str == 'Product'):
                        cpes_refasus_typeproduct_iot+=1  
                    elif(auxx_str == 'Advisory'):
                        cpes_refasus_typeadvisory_iot+=1  
                    elif((auxx_str == 'Change Log') or (auxx_str == 'ChangeLog')):
                        cpes_refasus_typechangelog_iot+=1  
                    elif(auxx_str == 'Vendor'):
                        cpes_refasus_typevendor_iot+=1  
                elif('iot.konker' in aux_str):
                    cpes_refiotkonker_iot+=1  
                    if(auxx_str == 'NONE'):
                        cpes_refiotkonker_typenone_iot+=1  
                    elif(auxx_str == 'Version'):
                        cpes_refiotkonker_typeversion_iot+=1  
                    elif(auxx_str == 'Product'):
                        cpes_refiotkonker_typeproduct_iot+=1  
                    elif(auxx_str == 'Advisory'):
                        cpes_refiotkonker_typeadvisory_iot+=1  
                    elif((auxx_str == 'Change Log') or (auxx_str == 'ChangeLog')):
                        cpes_refiotkonker_typechangelog_iot+=1  
                    elif(auxx_str == 'Vendor'):
                        cpes_refiotkonker_typevendor_iot+=1    
                elif('vulncheck' in aux_str):
                    cpes_refvulncheck_iot+=1  
                    if(auxx_str == 'NONE'):
                        cpes_refvulncheck_typenone_iot+=1  
                    elif(auxx_str == 'Version'):
                        cpes_refvulncheck_typeversion_iot+=1  
                    elif(auxx_str == 'Product'):
                        cpes_refvulncheck_typeproduct_iot+=1  
                    elif(auxx_str == 'Advisory'):
                        cpes_refvulncheck_typeadvisory_iot+=1  
                    elif((auxx_str == 'Change Log') or (auxx_str == 'ChangeLog')):
                        cpes_refvulncheck_typechangelog_iot+=1  
                    elif(auxx_str == 'Vendor'):
                        cpes_refvulncheck_typevendor_iot+=1    
                elif('xiongmaitech' in aux_str):
                    cpes_refxiongmaitech_iot+=1  
                    if(auxx_str == 'NONE'):
                        cpes_refxiongmaitech_typenone_iot+=1  
                    elif(auxx_str == 'Version'):
                        cpes_refxiongmaitech_typeversion_iot+=1  
                    elif(auxx_str == 'Product'):
                        cpes_refxiongmaitech_typeproduct_iot+=1  
                    elif(auxx_str == 'Advisory'):
                        cpes_refxiongmaitech_typeadvisory_iot+=1  
                    elif((auxx_str == 'Change Log') or (auxx_str == 'ChangeLog')):
                        cpes_refxiongmaitech_typechangelog_iot+=1  
                    elif(auxx_str == 'Vendor'):
                        cpes_refxiongmaitech_typevendor_iot+=1    
                elif('microsoft' in aux_str):
                    cpes_refmicrosoft_iot+=1  
                    if(auxx_str == 'NONE'):
                        cpes_refmicrosoft_typenone_iot+=1  
                    elif(auxx_str == 'Version'):
                        cpes_refmicrosoft_typeversion_iot+=1  
                    elif(auxx_str == 'Product'):
                        cpes_refmicrosoft_typeproduct_iot+=1  
                    elif(auxx_str == 'Advisory'):
                        cpes_refmicrosoft_typeadvisory_iot+=1  
                    elif((auxx_str == 'Change Log') or (auxx_str == 'ChangeLog')):
                        cpes_refmicrosoft_typechangelog_iot+=1  
                    elif(auxx_str == 'Vendor'):
                        cpes_refmicrosoft_typevendor_iot+=1    
                elif('riot' in aux_str):
                    cpes_refriot_iot+=1  
                    if(auxx_str == 'NONE'):
                        cpes_refriot_typenone_iot+=1  
                    elif(auxx_str == 'Version'):
                        cpes_refriot_typeversion_iot+=1  
                    elif(auxx_str == 'Product'):
                        cpes_refriot_typeproduct_iot+=1  
                    elif(auxx_str == 'Advisory'):
                        cpes_refriot_typeadvisory_iot+=1  
                    elif((auxx_str == 'Change Log') or (auxx_str == 'ChangeLog')):
                        cpes_refriot_typechangelog_iot+=1  
                    elif(auxx_str == 'Vendor'):
                        cpes_refriot_typevendor_iot+=1
                
    else:
        counterrefs_iot+=1
        if('github' in df_cpe_iot["cpes.refs.ref"][r]):
            cpes_refgithub_iot+=1  
            if(df_cpe_iot["cpes.refs.type"][r] == 'NONE'):
                cpes_refgithub_typenone_iot+=1  
            elif(df_cpe_iot["cpes.refs.type"][r] == 'Version'):
                cpes_refgithub_typeversion_iot+=1  
            elif(df_cpe_iot["cpes.refs.type"][r] == 'Product'):
                cpes_refgithub_typeproduct_iot+=1  
            elif(df_cpe_iot["cpes.refs.type"][r] == 'Advisory'):
                cpes_refgithub_typeadvisory_iot+=1  
            elif((df_cpe_iot["cpes.refs.type"][r] == 'Change Log') or (df_cpe_iot["cpes.refs.type"][r] == 'ChangeLog')):
                cpes_refgithub_typechangelog_iot+=1  
            elif(df_cpe_iot["cpes.refs.type"][r] == 'Vendor'):
                cpes_refgithub_typevendor_iot+=1
        elif('ptc' in df_cpe_iot["cpes.refs.ref"][r]):
            cpes_refptc_iot+=1  
            if(df_cpe_iot["cpes.refs.type"][r] == 'NONE'):
                cpes_refptc_typenone_iot+=1  
            elif(df_cpe_iot["cpes.refs.type"][r] == 'Version'):
                cpes_refptc_typeversion_iot+=1  
            elif(df_cpe_iot["cpes.refs.type"][r] == 'Product'):
                cpes_refptc_typeproduct_iot+=1  
            elif(df_cpe_iot["cpes.refs.type"][r] == 'Advisory'):
                cpes_refptc_typeadvisory_iot+=1  
            elif((df_cpe_iot["cpes.refs.type"][r] == 'Change Log') or (df_cpe_iot["cpes.refs.type"][r] == 'ChangeLog')):
                cpes_refptc_typechangelog_iot+=1  
            elif(df_cpe_iot["cpes.refs.type"][r] == 'Vendor'):
                cpes_refptc_typevendor_iot+=1    

        elif('symbiote.com' in df_cpe_iot["cpes.refs.ref"][r]):
            cpes_refsymbiote_iot+=1  
            if(df_cpe_iot["cpes.refs.type"][r] == 'NONE'):
                cpes_refsymbiote_typenone_iot+=1  
            elif(df_cpe_iot["cpes.refs.type"][r] == 'Version'):
                cpes_refsymbiote_typeversion_iot+=1  
            elif(df_cpe_iot["cpes.refs.type"][r] == 'Product'):
                cpes_refsymbiote_typeproduct_iot+=1  
            elif(df_cpe_iot["cpes.refs.type"][r] == 'Advisory'):
                cpes_refsymbiote_typeadvisory_iot+=1  
            elif((df_cpe_iot["cpes.refs.type"][r] == 'Change Log') or (df_cpe_iot["cpes.refs.type"][r] == 'ChangeLog')):
                cpes_refsymbiote_typechangelog_iot+=1  
            elif(df_cpe_iot["cpes.refs.type"][r] == 'Vendor'):
                cpes_refsymbiote_typevendor_iot+=1   
        elif('asus.com' in df_cpe_iot["cpes.refs.ref"][r]):
            cpes_refasus_iot+=1  
            if(df_cpe_iot["cpes.refs.type"][r] == 'NONE'):
                cpes_refasus_typenone_iot+=1  
            elif(df_cpe_iot["cpes.refs.type"][r] == 'Version'):
                cpes_refasus_typeversion_iot+=1  
            elif(df_cpe_iot["cpes.refs.type"][r] == 'Product'):
                cpes_refasus_typeproduct_iot+=1  
            elif(df_cpe_iot["cpes.refs.type"][r] == 'Advisory'):
                cpes_refasus_typeadvisory_iot+=1  
            elif((df_cpe_iot["cpes.refs.type"][r] == 'Change Log') or (df_cpe_iot["cpes.refs.type"][r] == 'ChangeLog')):
                cpes_refasus_typechangelog_iot+=1  
            elif(df_cpe_iot["cpes.refs.type"][r] == 'Vendor'):
                cpes_refasus_typevendor_iot+=1  
        elif('iot.konker' in df_cpe_iot["cpes.refs.ref"][r]):
            cpes_refiotkonker_iot+=1  
            if(df_cpe_iot["cpes.refs.type"][r] == 'NONE'):
                cpes_refiotkonker_typenone_iot+=1  
            elif(df_cpe_iot["cpes.refs.type"][r] == 'Version'):
                cpes_refiotkonker_typeversion_iot+=1  
            elif(df_cpe_iot["cpes.refs.type"][r] == 'Product'):
                cpes_refiotkonker_typeproduct_iot+=1  
            elif(df_cpe_iot["cpes.refs.type"][r] == 'Advisory'):
                cpes_refiotkonker_typeadvisory_iot+=1  
            elif((df_cpe_iot["cpes.refs.type"][r] == 'Change Log') or (df_cpe_iot["cpes.refs.type"][r] == 'ChangeLog')):
                cpes_refiotkonker_typechangelog_iot+=1  
            elif(df_cpe_iot["cpes.refs.type"][r] == 'Vendor'):
                cpes_refiotkonker_typevendor_iot+=1    
        elif('vulncheck' in df_cpe_iot["cpes.refs.ref"][r]):
            cpes_refvulncheck_iot+=1  
            if(df_cpe_iot["cpes.refs.type"][r] == 'NONE'):
                cpes_refvulncheck_typenone_iot+=1  
            elif(df_cpe_iot["cpes.refs.type"][r] == 'Version'):
                cpes_refvulncheck_typeversion_iot+=1  
            elif(df_cpe_iot["cpes.refs.type"][r] == 'Product'):
                cpes_refvulncheck_typeproduct_iot+=1  
            elif(df_cpe_iot["cpes.refs.type"][r] == 'Advisory'):
                cpes_refvulncheck_typeadvisory_iot+=1  
            elif((df_cpe_iot["cpes.refs.type"][r] == 'Change Log') or (df_cpe_iot["cpes.refs.type"][r] == 'ChangeLog')):
                cpes_refvulncheck_typechangelog_iot+=1  
            elif(df_cpe_iot["cpes.refs.type"][r] == 'Vendor'):
                cpes_refvulncheck_typevendor_iot+=1    
        elif('xiongmaitech' in df_cpe_iot["cpes.refs.ref"][r]):
            cpes_refxiongmaitech_iot+=1  
            if(df_cpe_iot["cpes.refs.type"][r] == 'NONE'):
                cpes_refxiongmaitech_typenone_iot+=1  
            elif(df_cpe_iot["cpes.refs.type"][r] == 'Version'):
                cpes_refxiongmaitech_typeversion_iot+=1  
            elif(df_cpe_iot["cpes.refs.type"][r] == 'Product'):
                cpes_refxiongmaitech_typeproduct_iot+=1  
            elif(df_cpe_iot["cpes.refs.type"][r] == 'Advisory'):
                cpes_refxiongmaitech_typeadvisory_iot+=1  
            elif((df_cpe_iot["cpes.refs.type"][r] == 'Change Log') or (df_cpe_iot["cpes.refs.type"][r] == 'ChangeLog')):
                cpes_refxiongmaitech_typechangelog_iot+=1  
            elif(df_cpe_iot["cpes.refs.type"][r] == 'Vendor'):
                cpes_refxiongmaitech_typevendor_iot+=1    
        elif('microsoft' in df_cpe_iot["cpes.refs.ref"][r]):
            cpes_refmicrosoft_iot+=1  
            if(df_cpe_iot["cpes.refs.type"][r] == 'NONE'):
                cpes_refmicrosoft_typenone_iot+=1  
            elif(df_cpe_iot["cpes.refs.type"][r] == 'Version'):
                cpes_refmicrosoft_typeversion_iot+=1  
            elif(df_cpe_iot["cpes.refs.type"][r] == 'Product'):
                cpes_refmicrosoft_typeproduct_iot+=1  
            elif(df_cpe_iot["cpes.refs.type"][r] == 'Advisory'):
                cpes_refmicrosoft_typeadvisory_iot+=1  
            elif((df_cpe_iot["cpes.refs.type"][r] == 'Change Log') or (df_cpe_iot["cpes.refs.type"][r] == 'ChangeLog')):
                cpes_refmicrosoft_typechangelog_iot+=1  
            elif(df_cpe_iot["cpes.refs.type"][r] == 'Vendor'):
                cpes_refmicrosoft_typevendor_iot+=1    
        elif('riot' in df_cpe_iot["cpes.refs.ref"][r]):
            cpes_refriot_iot+=1  
            if(df_cpe_iot["cpes.refs.type"][r] == 'NONE'):
                cpes_refriot_typenone_iot+=1  
            elif(df_cpe_iot["cpes.refs.type"][r] == 'Version'):
                cpes_refriot_typeversion_iot+=1  
            elif(df_cpe_iot["cpes.refs.type"][r] == 'Product'):
                cpes_refriot_typeproduct_iot+=1  
            elif(df_cpe_iot["cpes.refs.type"][r] == 'Advisory'):
                cpes_refriot_typeadvisory_iot+=1  
            elif((df_cpe_iot["cpes.refs.type"][r] == 'Change Log') or (df_cpe_iot["cpes.refs.type"][r] == 'ChangeLog')):
                cpes_refriot_typechangelog_iot+=1  
            elif(df_cpe_iot["cpes.refs.type"][r] == 'Vendor'):
                cpes_refriot_typevendor_iot+=1

print("******************************ESTADÍSTICAS RELACION FUENTE Y TIPO DE REFERENCIA CPE PARTE IOT******************************")
print("\n")                            
                
print("\n")
print(" DE UN TOTAL DE "+str(counterrefs_iot)+" REFERENCIAS DE CPES , LAS ESTADISTICAS DE RELACION DE TIPO DE REFERENCIA Y FUENTE DE REFERENCIA SON LAS SIGUIENTES:  \n")
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
print("      -    EN  "+str(cpes_refgithub_iot)+" REFERENCIAS LA FUENTE DE REFERENCIA ES GITHUB.COM. LAS ESTADÍSTICAS DE TIPO DE REFERENCIA SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(cpes_refgithub_typevendor_iot)+" REFERENCIAS EL TIPO ES VENDEDOR ")
print("            -    EN  "+str(cpes_refgithub_typeversion_iot)+" REFERENCIAS EL TIPO ES VERSION ")
print("            -    EN  "+str(cpes_refgithub_typeproduct_iot)+" REFERENCIAS EL TIPO ES PRODUCTO ")
print("            -    EN  "+str(cpes_refgithub_typeadvisory_iot)+" REFERENCIAS EL TIPO ES AVISO ")
print("            -    EN  "+str(cpes_refgithub_typechangelog_iot)+" REFERENCIAS EL TIPO ES REGISTRO DE CAMBIO ")
print("            -    EN  "+str(cpes_refgithub_typenone_iot)+" REFERENCIAS EL TIPO NO VIENE ESPECIFICADO")
print("\n")
print("      -    EN  "+str(cpes_refptc_iot)+" REFERENCIAS LA FUENTE DE REFERENCIA ES PTC. LAS ESTADÍSTICAS DE TIPO DE REFERENCIA SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(cpes_refptc_typevendor_iot)+" REFERENCIAS EL TIPO ES VENDEDOR ")
print("            -    EN  "+str(cpes_refptc_typeversion_iot)+" REFERENCIAS EL TIPO ES VERSION ")
print("            -    EN  "+str(cpes_refptc_typeproduct_iot)+" REFERENCIAS EL TIPO ES PRODUCTO ")
print("            -    EN  "+str(cpes_refptc_typeadvisory_iot)+" REFERENCIAS EL TIPO ES AVISO ")
print("            -    EN  "+str(cpes_refptc_typechangelog_iot)+" REFERENCIAS EL TIPO ES REGISTRO DE CAMBIO ")
print("            -    EN  "+str(cpes_refptc_typenone_iot)+" REFERENCIAS EL TIPO NO VIENE ESPECIFICADO")
print("\n")
print("      -    EN  "+str(cpes_refsymbiote_iot)+" REFERENCIAS LA FUENTE DE REFERENCIA ES SYMBIOTE.COM. LAS ESTADÍSTICAS DE TIPO DE REFERENCIA SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(cpes_refsymbiote_typevendor_iot)+" REFERENCIAS EL TIPO ES VENDEDOR ")
print("            -    EN  "+str(cpes_refsymbiote_typeversion_iot)+" REFERENCIAS EL TIPO ES VERSION ")
print("            -    EN  "+str(cpes_refsymbiote_typeproduct_iot)+" REFERENCIAS EL TIPO ES PRODUCTO ")
print("            -    EN  "+str(cpes_refsymbiote_typeadvisory_iot)+" REFERENCIAS EL TIPO ES AVISO ")
print("            -    EN  "+str(cpes_refsymbiote_typechangelog_iot)+" REFERENCIAS EL TIPO ES REGISTRO DE CAMBIO ")
print("            -    EN  "+str(cpes_refsymbiote_typenone_iot)+" REFERENCIAS EL TIPO NO VIENE ESPECIFICADO")
print("\n")
print("      -    EN  "+str(cpes_refasus_iot)+" REFERENCIAS LA FUENTE DE REFERENCIA ES ASUS.COM. LAS ESTADÍSTICAS DE TIPO DE REFERENCIA SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(cpes_refasus_typevendor_iot)+" REFERENCIAS EL TIPO ES VENDEDOR ")
print("            -    EN  "+str(cpes_refasus_typeversion_iot)+" REFERENCIAS EL TIPO ES VERSION ")
print("            -    EN  "+str(cpes_refasus_typeproduct_iot)+" REFERENCIAS EL TIPO ES PRODUCTO ")
print("            -    EN  "+str(cpes_refasus_typeadvisory_iot)+" REFERENCIAS EL TIPO ES AVISO ")
print("            -    EN  "+str(cpes_refasus_typechangelog_iot)+" REFERENCIAS EL TIPO ES REGISTRO DE CAMBIO ")
print("            -    EN  "+str(cpes_refasus_typenone_iot)+" REFERENCIAS EL TIPO NO VIENE ESPECIFICADO")
print("\n")
print("      -    EN  "+str(cpes_refiotkonker_iot)+" REFERENCIAS LA FUENTE DE REFERENCIA ES IOT.KONKER. LAS ESTADÍSTICAS DE TIPO DE REFERENCIA SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(cpes_refiotkonker_typevendor_iot)+" REFERENCIAS EL TIPO ES VENDEDOR ")
print("            -    EN  "+str(cpes_refiotkonker_typeversion_iot)+" REFERENCIAS EL TIPO ES VERSION ")
print("            -    EN  "+str(cpes_refiotkonker_typeproduct_iot)+" REFERENCIAS EL TIPO ES PRODUCTO ")
print("            -    EN  "+str(cpes_refiotkonker_typeadvisory_iot)+" REFERENCIAS EL TIPO ES AVISO ")
print("            -    EN  "+str(cpes_refiotkonker_typechangelog_iot)+" REFERENCIAS EL TIPO ES REGISTRO DE CAMBIO ")
print("            -    EN  "+str(cpes_refiotkonker_typenone_iot)+" REFERENCIAS EL TIPO NO VIENE ESPECIFICADO")
print("\n")
print("      -    EN  "+str(cpes_refvulncheck_iot)+" REFERENCIAS LA FUENTE DE REFERENCIA ES VULNCHECK.COM. LAS ESTADÍSTICAS DE TIPO DE REFERENCIA SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(cpes_refvulncheck_typevendor_iot)+" REFERENCIAS EL TIPO ES VENDEDOR ")
print("            -    EN  "+str(cpes_refvulncheck_typeversion_iot)+" REFERENCIAS EL TIPO ES VERSION ")
print("            -    EN  "+str(cpes_refvulncheck_typeproduct_iot)+" REFERENCIAS EL TIPO ES PRODUCTO ")
print("            -    EN  "+str(cpes_refvulncheck_typeadvisory_iot)+" REFERENCIAS EL TIPO ES AVISO ")
print("            -    EN  "+str(cpes_refvulncheck_typechangelog_iot)+" REFERENCIAS EL TIPO ES REGISTRO DE CAMBIO ")
print("            -    EN  "+str(cpes_refvulncheck_typenone_iot)+" REFERENCIAS EL TIPO NO VIENE ESPECIFICADO")
print("\n")
print("      -    EN  "+str(cpes_refxiongmaitech_iot)+" REFERENCIAS LA FUENTE DE REFERENCIA ES XIONGMAITECH.COM. LAS ESTADÍSTICAS DE TIPO DE REFERENCIA SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(cpes_refxiongmaitech_typevendor_iot)+" REFERENCIAS EL TIPO ES VENDEDOR ")
print("            -    EN  "+str(cpes_refxiongmaitech_typeversion_iot)+" REFERENCIAS EL TIPO ES VERSION ")
print("            -    EN  "+str(cpes_refxiongmaitech_typeproduct_iot)+" REFERENCIAS EL TIPO ES PRODUCTO ")
print("            -    EN  "+str(cpes_refxiongmaitech_typeadvisory_iot)+" REFERENCIAS EL TIPO ES AVISO ")
print("            -    EN  "+str(cpes_refxiongmaitech_typechangelog_iot)+" REFERENCIAS EL TIPO ES REGISTRO DE CAMBIO ")
print("            -    EN  "+str(cpes_refxiongmaitech_typenone_iot)+" REFERENCIAS EL TIPO NO VIENE ESPECIFICADO")
print("\n")
print("      -    EN  "+str(cpes_refmicrosoft_iot)+" REFERENCIAS LA FUENTE DE REFERENCIA ES MICROSOFT.COM. LAS ESTADÍSTICAS DE TIPO DE REFERENCIA SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(cpes_refmicrosoft_typevendor_iot)+" REFERENCIAS EL TIPO ES VENDEDOR ")
print("            -    EN  "+str(cpes_refmicrosoft_typeversion_iot)+" REFERENCIAS EL TIPO ES VERSION ")
print("            -    EN  "+str(cpes_refmicrosoft_typeproduct_iot)+" REFERENCIAS EL TIPO ES PRODUCTO ")
print("            -    EN  "+str(cpes_refmicrosoft_typeadvisory_iot)+" REFERENCIAS EL TIPO ES AVISO ")
print("            -    EN  "+str(cpes_refmicrosoft_typechangelog_iot)+" REFERENCIAS EL TIPO ES REGISTRO DE CAMBIO ")
print("            -    EN  "+str(cpes_refmicrosoft_typenone_iot)+" REFERENCIAS EL TIPO NO VIENE ESPECIFICADO")
print("\n")
print("      -    EN  "+str(cpes_refriot_iot)+" REFERENCIAS LA FUENTE DE REFERENCIA ES RIOT-OS.ORG. LAS ESTADÍSTICAS DE TIPO DE REFERENCIA SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(cpes_refriot_typevendor_iot)+" REFERENCIAS EL TIPO ES VENDEDOR ")
print("            -    EN  "+str(cpes_refriot_typeversion_iot)+" REFERENCIAS EL TIPO ES VERSION ")
print("            -    EN  "+str(cpes_refriot_typeproduct_iot)+" REFERENCIAS EL TIPO ES PRODUCTO ")
print("            -    EN  "+str(cpes_refriot_typeadvisory_iot)+" REFERENCIAS EL TIPO ES AVISO ")
print("            -    EN  "+str(cpes_refriot_typechangelog_iot)+" REFERENCIAS EL TIPO ES REGISTRO DE CAMBIO ")
print("            -    EN  "+str(cpes_refriot_typenone_iot)+" REFERENCIAS EL TIPO NO VIENE ESPECIFICADO")
print("\n")
print("\n")









print("******************************PORCENTAJES RELACION TIPO Y FUENTE DE REFERENCIA CPES PARTE IOT******************************")
print("\n")        
            
          
    
print("\n")
print(" DE UN TOTAL DE "+str(counterrefs_iot)+" REFERENCIAS DE CPES , LOS PORCENTAJES DE TIPO DE REFERENCIA Y FUENTE DE REFERENCIA SON LOS SIGUIENTES:  \n")
print("\n")
print("\n")
print("      -    EN  EL "+str(float(((cpes_refgithub_iot*100)/counterrefs_iot)))+" % DE REFERENCIAS LA FUENTE ES GITHUB.COM  \n")
print("      -    EN  EL "+str(float(((cpes_refptc_iot*100)/counterrefs_iot)))+" % DE REFERENCIAS LA FUENTE ES PTC.COM  \n")
print("      -    EN  EL "+str(float(((cpes_refsymbiote_iot*100)/counterrefs_iot)))+" % DE REFERENCIAS LA FUENTE ES SYMBIOTE.COM.COM  \n")
print("      -    EN  EL "+str(float(((cpes_refasus_iot*100)/counterrefs_iot)))+" % DE REFERENCIAS LA FUENTE ES ASUS.COM.COM  \n")
print("      -    EN  EL "+str(float(((cpes_refiotkonker_iot*100)/counterrefs_iot)))+" % DE REFERENCIAS LA FUENTE ES IOT.KONKER  \n")
print("      -    EN  EL "+str(float(((cpes_refvulncheck_iot*100)/counterrefs_iot)))+" % DE REFERENCIAS LA FUENTE ES VULNCHECK.COM  \n")
print("      -    EN  EL "+str(float(((cpes_refxiongmaitech_iot*100)/counterrefs_iot)))+" % DE REFERENCIAS LA FUENTE ES XIONGMAITECH.COM  \n")
print("      -    EN  EL "+str(float(((cpes_refmicrosoft_iot*100)/counterrefs_iot)))+" % DE REFERENCIAS LA FUENTE ES MICROSOFT.COM  \n")
print("      -    EN  EL "+str(float(((cpes_refriot_iot*100)/counterrefs_iot)))+" % DE REFERENCIAS LA FUENTE ES RIOT-OS.ORG  \n")
print("\n")
print("      -    EN EL "+str(float(((cpes_refgithub_iot*100)/counterrefs_iot)))+" % DE REFERENCIAS DE CPES DONDE LA FUENTE DE REFERENCIA ES GITHUB.COM, LOS PORCENTAJES DE TIPO DE REFERENCIA SON LOS SIGUIENTES:  \n")
print("\n")
print("            -    EN EL "+str(float(((cpes_refgithub_typevendor_iot*100)/cpes_refgithub_iot)))+" % DE REFERENCIAS EL TIPO ES VENDEDOR  ")
print("            -    EN EL "+str(float(((cpes_refgithub_typeversion_iot*100)/cpes_refgithub_iot)))+" % DE REFERENCIAS EL TIPO ES VERSION ")
print("            -    EN EL "+str(float(((cpes_refgithub_typeproduct_iot*100)/cpes_refgithub_iot)))+" % DE REFERENCIAS EL TIPO ES PRODUCTO ")
print("            -    EN EL "+str(float(((cpes_refgithub_typeadvisory_iot*100)/cpes_refgithub_iot)))+" % DE REFERENCIAS EL TIPO ES AVISO ")
print("            -    EN EL "+str(float(((cpes_refgithub_typechangelog_iot*100)/cpes_refgithub_iot)))+" % DE REFERENCIAS EL TIPO ES REGISTRO DE CAMBIO ")
print("            -    EN EL "+str(float(((cpes_refgithub_typenone_iot*100)/cpes_refgithub_iot)))+" % DE REFERENCIAS EL TIPO NO VIENE ESPECIFICADO ")
print("\n")
print("      -    EN EL "+str(float(((cpes_refptc_iot*100)/counterrefs_iot)))+" % DE REFERENCIAS DE CPES DONDE LA FUENTE DE REFERENCIA ES PTC, LOS PORCENTAJES DE TIPO DE REFERENCIA SON LOS SIGUIENTES:   \n")
print("\n")
print("            -    EN EL "+str(float(((cpes_refptc_typevendor_iot*100)/cpes_refptc_iot)))+" % DE REFERENCIAS EL TIPO ES VENDEDOR  ")
print("            -    EN EL "+str(float(((cpes_refptc_typeversion_iot*100)/cpes_refptc_iot)))+" % DE REFERENCIAS EL TIPO ES VERSION ")
print("            -    EN EL "+str(float(((cpes_refptc_typeproduct_iot*100)/cpes_refptc_iot)))+" % DE REFERENCIAS EL TIPO ES PRODUCTO ")
print("            -    EN EL "+str(float(((cpes_refptc_typeadvisory_iot*100)/cpes_refptc_iot)))+" % DE REFERENCIAS EL TIPO ES AVISO ")
print("            -    EN EL "+str(float(((cpes_refptc_typechangelog_iot*100)/cpes_refptc_iot)))+" % DE REFERENCIAS EL TIPO ES REGISTRO DE CAMBIO ")
print("            -    EN EL "+str(float(((cpes_refptc_typenone_iot*100)/cpes_refptc_iot)))+" % DE REFERENCIAS EL TIPO NO VIENE ESPECIFICADO ")
print("\n")
print("      -    EN EL "+str(float(((cpes_refsymbiote_iot*100)/counterrefs_iot)))+" % DE REFERENCIAS DE CPES DONDE LA FUENTE DE REFERENCIA ES SYMBIOTE.COM, LOS PORCENTAJES DE TIPO DE REFERENCIA SON LOS SIGUIENTES:   \n")
print("\n")
print("            -    EN EL "+str(float(((cpes_refsymbiote_typevendor_iot*100)/cpes_refsymbiote_iot)))+" % DE REFERENCIAS EL TIPO ES VENDEDOR  ")
print("            -    EN EL "+str(float(((cpes_refsymbiote_typeversion_iot*100)/cpes_refsymbiote_iot)))+" % DE REFERENCIAS EL TIPO ES VERSION ")
print("            -    EN EL "+str(float(((cpes_refsymbiote_typeproduct_iot*100)/cpes_refsymbiote_iot)))+" % DE REFERENCIAS EL TIPO ES PRODUCTO ")
print("            -    EN EL "+str(float(((cpes_refsymbiote_typeadvisory_iot*100)/cpes_refsymbiote_iot)))+" % DE REFERENCIAS EL TIPO ES AVISO ")
print("            -    EN EL "+str(float(((cpes_refsymbiote_typechangelog_iot*100)/cpes_refsymbiote_iot)))+" % DE REFERENCIAS EL TIPO ES REGISTRO DE CAMBIO ")
print("            -    EN EL "+str(float(((cpes_refsymbiote_typenone_iot*100)/cpes_refsymbiote_iot)))+" % DE REFERENCIAS EL TIPO NO VIENE ESPECIFICADO ")
print("\n")
print("      -    EN EL "+str(float(((cpes_refasus_iot*100)/counterrefs_iot)))+" % DE REFERENCIAS DE CPES DONDE LA FUENTE DE REFERENCIA ES ASUS.COM, LOS PORCENTAJES DE TIPO DE REFERENCIA SON LOS SIGUIENTES:   \n")
print("\n")
print("            -    EN EL "+str(float(((cpes_refasus_typevendor_iot*100)/cpes_refasus_iot)))+" % DE REFERENCIAS EL TIPO ES VENDEDOR  ")
print("            -    EN EL "+str(float(((cpes_refasus_typeversion_iot*100)/cpes_refasus_iot)))+" % DE REFERENCIAS EL TIPO ES VERSION ")
print("            -    EN EL "+str(float(((cpes_refasus_typeproduct_iot*100)/cpes_refasus_iot)))+" % DE REFERENCIAS EL TIPO ES PRODUCTO ")
print("            -    EN EL "+str(float(((cpes_refasus_typeadvisory_iot*100)/cpes_refasus_iot)))+" % DE REFERENCIAS EL TIPO ES AVISO ")
print("            -    EN EL "+str(float(((cpes_refasus_typechangelog_iot*100)/cpes_refasus_iot)))+" % DE REFERENCIAS EL TIPO ES REGISTRO DE CAMBIO ")
print("            -    EN EL "+str(float(((cpes_refasus_typenone_iot*100)/cpes_refasus_iot)))+" % DE REFERENCIAS EL TIPO NO VIENE ESPECIFICADO ")
print("\n")
print("      -    EN EL "+str(float(((cpes_refiotkonker_iot*100)/counterrefs_iot)))+" % DE REFERENCIAS DE CPES DONDE LA FUENTE DE REFERENCIA ES IOTKONKER, LOS PORCENTAJES DE TIPO DE REFERENCIA SON LOS SIGUIENTES:   \n")
print("\n")
print("            -    EN EL "+str(float(((cpes_refiotkonker_typevendor_iot*100)/cpes_refiotkonker_iot)))+" % DE REFERENCIAS EL TIPO ES VENDEDOR  ")
print("            -    EN EL "+str(float(((cpes_refiotkonker_typeversion_iot*100)/cpes_refiotkonker_iot)))+" % DE REFERENCIAS EL TIPO ES VERSION ")
print("            -    EN EL "+str(float(((cpes_refiotkonker_typeproduct_iot*100)/cpes_refiotkonker_iot)))+" % DE REFERENCIAS EL TIPO ES PRODUCTO ")
print("            -    EN EL "+str(float(((cpes_refiotkonker_typeadvisory_iot*100)/cpes_refiotkonker_iot)))+" % DE REFERENCIAS EL TIPO ES AVISO ")
print("            -    EN EL "+str(float(((cpes_refiotkonker_typechangelog_iot*100)/cpes_refiotkonker_iot)))+" % DE REFERENCIAS EL TIPO ES REGISTRO DE CAMBIO ")
print("            -    EN EL "+str(float(((cpes_refiotkonker_typenone_iot*100)/cpes_refiotkonker_iot)))+" % DE REFERENCIAS EL TIPO NO VIENE ESPECIFICADO ")
print("\n")
print("      -    EN EL "+str(float(((cpes_refvulncheck_iot*100)/counterrefs_iot)))+" % DE REFERENCIAS DE CPES DONDE LA FUENTE DE REFERENCIA ES VULNCHECK.COM, LOS PORCENTAJES DE TIPO DE REFERENCIA SON LOS SIGUIENTES:   \n")
print("\n")
print("            -    EN EL "+str(float(((cpes_refvulncheck_typevendor_iot*100)/cpes_refvulncheck_iot)))+" % DE REFERENCIAS EL TIPO ES VENDEDOR  ")
print("            -    EN EL "+str(float(((cpes_refvulncheck_typeversion_iot*100)/cpes_refvulncheck_iot)))+" % DE REFERENCIAS EL TIPO ES VERSION ")
print("            -    EN EL "+str(float(((cpes_refvulncheck_typeproduct_iot*100)/cpes_refvulncheck_iot)))+" % DE REFERENCIAS EL TIPO ES PRODUCTO ")
print("            -    EN EL "+str(float(((cpes_refvulncheck_typeadvisory_iot*100)/cpes_refvulncheck_iot)))+" % DE REFERENCIAS EL TIPO ES AVISO ")
print("            -    EN EL "+str(float(((cpes_refvulncheck_typechangelog_iot*100)/cpes_refvulncheck_iot)))+" % DE REFERENCIAS EL TIPO ES REGISTRO DE CAMBIO ")
print("            -    EN EL "+str(float(((cpes_refvulncheck_typenone_iot*100)/cpes_refvulncheck_iot)))+" % DE REFERENCIAS EL TIPO NO VIENE ESPECIFICADO ")
print("\n")
print("      -    EN EL "+str(float(((cpes_refxiongmaitech_iot*100)/counterrefs_iot)))+" % DE REFERENCIAS DE CPES DONDE LA FUENTE DE REFERENCIA ES XIONGMAITECH.COM, LOS PORCENTAJES DE TIPO DE REFERENCIA SON LOS SIGUIENTES:   \n")
print("\n")
print("            -    EN EL "+str(float(((cpes_refxiongmaitech_typevendor_iot*100)/cpes_refxiongmaitech_iot)))+" % DE REFERENCIAS EL TIPO ES VENDEDOR  ")
print("            -    EN EL "+str(float(((cpes_refxiongmaitech_typeversion_iot*100)/cpes_refxiongmaitech_iot)))+" % DE REFERENCIAS EL TIPO ES VERSION ")
print("            -    EN EL "+str(float(((cpes_refxiongmaitech_typeproduct_iot*100)/cpes_refxiongmaitech_iot)))+" % DE REFERENCIAS EL TIPO ES PRODUCTO ")
print("            -    EN EL "+str(float(((cpes_refxiongmaitech_typeadvisory_iot*100)/cpes_refxiongmaitech_iot)))+" % DE REFERENCIAS EL TIPO ES AVISO ")
print("            -    EN EL "+str(float(((cpes_refxiongmaitech_typechangelog_iot*100)/cpes_refxiongmaitech_iot)))+" % DE REFERENCIAS EL TIPO ES REGISTRO DE CAMBIO ")
print("            -    EN EL "+str(float(((cpes_refxiongmaitech_typenone_iot*100)/cpes_refxiongmaitech_iot)))+" % DE REFERENCIAS EL TIPO NO VIENE ESPECIFICADO ")
print("\n")
print("      -    EN EL "+str(float(((cpes_refmicrosoft_iot*100)/counterrefs_iot)))+" % DE REFERENCIAS DE CPES DONDE LA FUENTE DE REFERENCIA ES MICROSOFT.COM, LOS PORCENTAJES DE TIPO DE REFERENCIA SON LOS SIGUIENTES:   \n")
print("\n")
print("            -    EN EL "+str(float(((cpes_refmicrosoft_typevendor_iot*100)/cpes_refmicrosoft_iot)))+" % DE REFERENCIAS EL TIPO ES VENDEDOR  ")
print("            -    EN EL "+str(float(((cpes_refmicrosoft_typeversion_iot*100)/cpes_refmicrosoft_iot)))+" % DE REFERENCIAS EL TIPO ES VERSION ")
print("            -    EN EL "+str(float(((cpes_refmicrosoft_typeproduct_iot*100)/cpes_refmicrosoft_iot)))+" % DE REFERENCIAS EL TIPO ES PRODUCTO ")
print("            -    EN EL "+str(float(((cpes_refmicrosoft_typeadvisory_iot*100)/cpes_refmicrosoft_iot)))+" % DE REFERENCIAS EL TIPO ES AVISO ")
print("            -    EN EL "+str(float(((cpes_refmicrosoft_typechangelog_iot*100)/cpes_refmicrosoft_iot)))+" % DE REFERENCIAS EL TIPO ES REGISTRO DE CAMBIO ")
print("            -    EN EL "+str(float(((cpes_refmicrosoft_typenone_iot*100)/cpes_refmicrosoft_iot)))+" % DE REFERENCIAS EL TIPO NO VIENE ESPECIFICADO ")
print("\n")
print("      -    EN EL "+str(float(((cpes_refriot_iot*100)/counterrefs_iot)))+" % DE REFERENCIAS DE CPES DONDE LA FUENTE DE REFERENCIA ES RIOT-OS.ORG, LOS PORCENTAJES DE TIPO DE REFERENCIA SON LOS SIGUIENTES:   \n")
print("\n")
print("            -    EN EL "+str(float(((cpes_refriot_typevendor_iot*100)/cpes_refriot_iot)))+" % DE REFERENCIAS EL TIPO ES VENDEDOR  ")
print("            -    EN EL "+str(float(((cpes_refriot_typeversion_iot*100)/cpes_refriot_iot)))+" % DE REFERENCIAS EL TIPO ES VERSION ")
print("            -    EN EL "+str(float(((cpes_refriot_typeproduct_iot*100)/cpes_refriot_iot)))+" % DE REFERENCIAS EL TIPO ES PRODUCTO ")
print("            -    EN EL "+str(float(((cpes_refriot_typeadvisory_iot*100)/cpes_refriot_iot)))+" % DE REFERENCIAS EL TIPO ES AVISO ")
print("            -    EN EL "+str(float(((cpes_refriot_typechangelog_iot*100)/cpes_refriot_iot)))+" % DE REFERENCIAS EL TIPO ES REGISTRO DE CAMBIO ")
print("            -    EN EL "+str(float(((cpes_refriot_typenone_iot*100)/cpes_refriot_iot)))+" % DE REFERENCIAS EL TIPO NO VIENE ESPECIFICADO ")
print("\n")









print("******************************TIPO DE REFERENCIA CPE/FUENTE DE REFERENCIA CPE PARTE SMART HOME******************************")
print("\n")
print("\n")

#Contador total de referencias
counterrefs_sh=0

cpes_refapple_sh=0
cpes_refapple_typevendor_sh=0
cpes_refapple_typeversion_sh=0
cpes_refapple_typeproduct_sh=0
cpes_refapple_typeadvisory_sh=0
cpes_refapple_typechangelog_sh=0
cpes_refapple_typenone_sh=0


cpes_refcisco_sh=0
cpes_refcisco_typevendor_sh=0
cpes_refcisco_typeversion_sh=0
cpes_refcisco_typeproduct_sh=0
cpes_refcisco_typeadvisory_sh=0
cpes_refcisco_typechangelog_sh=0
cpes_refcisco_typenone_sh=0


cpes_refbosch_sh=0
cpes_refbosch_typevendor_sh=0
cpes_refbosch_typeversion_sh=0
cpes_refbosch_typeproduct_sh=0
cpes_refbosch_typeadvisory_sh=0
cpes_refbosch_typechangelog_sh=0
cpes_refbosch_typenone_sh=0

cpes_refcoolkit_sh=0
cpes_refcoolkit_typevendor_sh=0
cpes_refcoolkit_typeversion_sh=0
cpes_refcoolkit_typeproduct_sh=0
cpes_refcoolkit_typeadvisory_sh=0
cpes_refcoolkit_typechangelog_sh=0
cpes_refcoolkit_typenone_sh=0

cpes_refinimbiz_sh=0
cpes_refinimbiz_typevendor_sh=0
cpes_refinimbiz_typeversion_sh=0
cpes_refinimbiz_typeproduct_sh=0
cpes_refinimbiz_typeadvisory_sh=0
cpes_refinimbiz_typechangelog_sh=0
cpes_refinimbiz_typenone_sh=0

cpes_refidec_sh=0
cpes_refidec_typevendor_sh=0
cpes_refidec_typeversion_sh=0
cpes_refidec_typeproduct_sh=0
cpes_refidec_typeadvisory_sh=0
cpes_refidec_typechangelog_sh=0
cpes_refidec_typenone_sh=0

cpes_refgoogle_sh=0
cpes_refgoogle_typevendor_sh=0
cpes_refgoogle_typeversion_sh=0
cpes_refgoogle_typeproduct_sh=0
cpes_refgoogle_typeadvisory_sh=0
cpes_refgoogle_typechangelog_sh=0
cpes_refgoogle_typenone_sh=0

cpes_refdocbmc_sh=0
cpes_refdocbmc_typevendor_sh=0
cpes_refdocbmc_typeversion_sh=0
cpes_refdocbmc_typeproduct_sh=0
cpes_refdocbmc_typeadvisory_sh=0
cpes_refdocbmc_typechangelog_sh=0
cpes_refdocbmc_typenone_sh=0




#Recorro los valores de referencias
for r in range(0,len(df_cpe_sh["cpes.lastModifiedDate"])):
    if('[' in df_cpe_sh["cpes.refs.ref"][r]):
        aux=df_cpe_sh["cpes.refs.ref"][r].split(",")
        auxx=df_cpe_sh["cpes.refs.type"][r].split(",")
        for k in range(0,len(aux)):
            if(len(aux)>0):
                counterrefs_sh+=1
                #Obtengo los valores de referencia y tipo de referencia
                aux_str=aux[k].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
                auxx_str=auxx[k].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
                if('apple' in aux_str):
                    cpes_refapple_sh+=1 
                    #Compruebo valor de tipo de referencia
                    if(auxx_str == 'NONE'):
                        cpes_refapple_typenone_sh+=1  
                    elif(auxx_str == 'Version'):
                        cpes_refapple_typeversion_sh+=1  
                    elif(auxx_str == 'Product'):
                        cpes_refapple_typeproduct_sh+=1  
                    elif(auxx_str == 'Advisory'):
                        cpes_refapple_typeadvisory_sh+=1  
                    elif((auxx_str == 'Change Log') or (auxx_str == 'ChangeLog')):
                        cpes_refapple_typechangelog_sh+=1  
                    elif(auxx_str == 'Vendor'):
                        cpes_refapple_typevendor_sh+=1
                elif('cisco' in aux_str):
                    cpes_refcisco_sh+=1  
                    if(auxx_str == 'NONE'):
                        cpes_refcisco_typenone_sh+=1  
                    elif(auxx_str == 'Version'):
                        cpes_refcisco_typeversion_sh+=1  
                    elif(auxx_str == 'Product'):
                        cpes_refcisco_typeproduct_sh+=1  
                    elif(auxx_str == 'Advisory'):
                        cpes_refcisco_typeadvisory_sh+=1  
                    elif((auxx_str == 'Change Log') or (auxx_str == 'ChangeLog')):
                        cpes_refcisco_typechangelog_sh+=1  
                    elif(auxx_str == 'Vendor'):
                        cpes_refcisco_typevendor_sh+=1    
               
                elif('bosch' in aux_str):
                    cpes_refbosch_sh+=1  
                    if(auxx_str == 'NONE'):
                        cpes_refbosch_typenone_sh+=1  
                    elif(auxx_str == 'Version'):
                        cpes_refbosch_typeversion_sh+=1  
                    elif(auxx_str == 'Product'):
                        cpes_refbosch_typeproduct_sh+=1  
                    elif(auxx_str == 'Advisory'):
                        cpes_refbosch_typeadvisory_sh+=1  
                    elif((auxx_str == 'Change Log') or (auxx_str == 'ChangeLog')):
                        cpes_refbosch_typechangelog_sh+=1  
                    elif(auxx_str == 'Vendor'):
                        cpes_refbosch_typevendor_sh+=1   
                elif('coolkit' in aux_str):
                    cpes_refcoolkit_sh+=1  
                    if(auxx_str == 'NONE'):
                        cpes_refcoolkit_typenone_sh+=1  
                    elif(auxx_str == 'Version'):
                        cpes_refcoolkit_typeversion_sh+=1  
                    elif(auxx_str == 'Product'):
                        cpes_refcoolkit_typeproduct_sh+=1  
                    elif(auxx_str == 'Advisory'):
                        cpes_refcoolkit_typeadvisory_sh+=1  
                    elif((auxx_str == 'Change Log') or (auxx_str == 'ChangeLog')):
                        cpes_refcoolkit_typechangelog_sh+=1  
                    elif(auxx_str == 'Vendor'):
                        cpes_refcoolkit_typevendor_sh+=1  
                elif('inim.biz' in aux_str):
                    cpes_refinimbiz_sh+=1  
                    if(auxx_str == 'NONE'):
                        cpes_refinimbiz_typenone_sh+=1  
                    elif(auxx_str == 'Version'):
                        cpes_refinimbiz_typeversion_sh+=1  
                    elif(auxx_str == 'Product'):
                        cpes_refinimbiz_typeproduct_sh+=1  
                    elif(auxx_str == 'Advisory'):
                        cpes_refinimbiz_typeadvisory_sh+=1  
                    elif((auxx_str == 'Change Log') or (auxx_str == 'ChangeLog')):
                        cpes_refinimbiz_typechangelog_sh+=1  
                    elif(auxx_str == 'Vendor'):
                        cpes_refinimbiz_typevendor_sh+=1    
                elif('idec' in aux_str):
                    cpes_refidec_sh+=1  
                    if(auxx_str == 'NONE'):
                        cpes_refidec_typenone_sh+=1  
                    elif(auxx_str == 'Version'):
                        cpes_refidec_typeversion_sh+=1  
                    elif(auxx_str == 'Product'):
                        cpes_refidec_typeproduct_sh+=1  
                    elif(auxx_str == 'Advisory'):
                        cpes_refidec_typeadvisory_sh+=1  
                    elif((auxx_str == 'Change Log') or (auxx_str == 'ChangeLog')):
                        cpes_refidec_typechangelog_sh+=1  
                    elif(auxx_str == 'Vendor'):
                        cpes_refidec_typevendor_sh+=1    
                elif('google' in aux_str):
                    cpes_refgoogle_sh+=1  
                    if(auxx_str == 'NONE'):
                        cpes_refgoogle_typenone_sh+=1  
                    elif(auxx_str == 'Version'):
                        cpes_refgoogle_typeversion_sh+=1  
                    elif(auxx_str == 'Product'):
                        cpes_refgoogle_typeproduct_sh+=1  
                    elif(auxx_str == 'Advisory'):
                        cpes_refgoogle_typeadvisory_sh+=1  
                    elif((auxx_str == 'Change Log') or (auxx_str == 'ChangeLog')):
                        cpes_refgoogle_typechangelog_sh+=1  
                    elif(auxx_str == 'Vendor'):
                        cpes_refgoogle_typevendor_sh+=1    
                elif('docs.bmc' in aux_str):
                    cpes_refdocbmc_sh+=1  
                    if(auxx_str == 'NONE'):
                        cpes_refdocbmc_typenone_sh+=1  
                    elif(auxx_str == 'Version'):
                        cpes_refdocbmc_typeversion_sh+=1  
                    elif(auxx_str == 'Product'):
                        cpes_refdocbmc_typeproduct_sh+=1  
                    elif(auxx_str == 'Advisory'):
                        cpes_refdocbmc_typeadvisory_sh+=1  
                    elif((auxx_str == 'Change Log') or (auxx_str == 'ChangeLog')):
                        cpes_refdocbmc_typechangelog_sh+=1  
                    elif(auxx_str == 'Vendor'):
                        cpes_refdocbmc_typevendor_sh+=1    
                
    else:
        counterrefs_sh+=1
        if('apple' in df_cpe_sh["cpes.refs.ref"][r]):
            cpes_refapple_sh+=1  
            if(df_cpe_sh["cpes.refs.type"][r] == 'NONE'):
                cpes_refapple_typenone_sh+=1  
            elif(df_cpe_sh["cpes.refs.type"][r] == 'Version'):
                cpes_refapple_typeversion_sh+=1  
            elif(df_cpe_sh["cpes.refs.type"][r] == 'Product'):
                cpes_refapple_typeproduct_sh+=1  
            elif(df_cpe_sh["cpes.refs.type"][r] == 'Advisory'):
                cpes_refapple_typeadvisory_sh+=1  
            elif((df_cpe_sh["cpes.refs.type"][r] == 'Change Log') or (df_cpe_sh["cpes.refs.type"][r] == 'ChangeLog')):
                cpes_refapple_typechangelog_sh+=1  
            elif(df_cpe_sh["cpes.refs.type"][r] == 'Vendor'):
                cpes_refapple_typevendor_sh+=1
        elif('cisco' in df_cpe_sh["cpes.refs.ref"][r]):
            cpes_refcisco_sh+=1  
            if(df_cpe_sh["cpes.refs.type"][r] == 'NONE'):
                cpes_refcisco_typenone_sh+=1  
            elif(df_cpe_sh["cpes.refs.type"][r] == 'Version'):
                cpes_refcisco_typeversion_sh+=1  
            elif(df_cpe_sh["cpes.refs.type"][r] == 'Product'):
                cpes_refcisco_typeproduct_sh+=1  
            elif(df_cpe_sh["cpes.refs.type"][r] == 'Advisory'):
                cpes_refcisco_typeadvisory_sh+=1  
            elif((df_cpe_sh["cpes.refs.type"][r] == 'Change Log') or (df_cpe_sh["cpes.refs.type"][r] == 'ChangeLog')):
                cpes_refcisco_typechangelog_sh+=1  
            elif(df_cpe_sh["cpes.refs.type"][r] == 'Vendor'):
                cpes_refcisco_typevendor_sh+=1    

        elif('bosch' in df_cpe_sh["cpes.refs.ref"][r]):
            cpes_refbosch_sh+=1  
            if(df_cpe_sh["cpes.refs.type"][r] == 'NONE'):
                cpes_refbosch_typenone_sh+=1  
            elif(df_cpe_sh["cpes.refs.type"][r] == 'Version'):
                cpes_refbosch_typeversion_sh+=1  
            elif(df_cpe_sh["cpes.refs.type"][r] == 'Product'):
                cpes_refbosch_typeproduct_sh+=1  
            elif(df_cpe_sh["cpes.refs.type"][r] == 'Advisory'):
                cpes_refbosch_typeadvisory_sh+=1  
            elif((df_cpe_sh["cpes.refs.type"][r] == 'Change Log') or (df_cpe_sh["cpes.refs.type"][r] == 'ChangeLog')):
                cpes_refbosch_typechangelog_sh+=1  
            elif(df_cpe_sh["cpes.refs.type"][r] == 'Vendor'):
                cpes_refbosch_typevendor_sh+=1   
        elif('coolkit' in df_cpe_sh["cpes.refs.ref"][r]):
            cpes_refcoolkit_sh+=1  
            if(df_cpe_sh["cpes.refs.type"][r] == 'NONE'):
                cpes_refcoolkit_typenone_sh+=1  
            elif(df_cpe_sh["cpes.refs.type"][r] == 'Version'):
                cpes_refcoolkit_typeversion_sh+=1  
            elif(df_cpe_sh["cpes.refs.type"][r] == 'Product'):
                cpes_refcoolkit_typeproduct_sh+=1  
            elif(df_cpe_sh["cpes.refs.type"][r] == 'Advisory'):
                cpes_refcoolkit_typeadvisory_sh+=1  
            elif((df_cpe_sh["cpes.refs.type"][r] == 'Change Log') or (df_cpe_sh["cpes.refs.type"][r] == 'ChangeLog')):
                cpes_refcoolkit_typechangelog_sh+=1  
            elif(df_cpe_sh["cpes.refs.type"][r] == 'Vendor'):
                cpes_refcoolkit_typevendor_sh+=1  
        elif('inim.biz' in df_cpe_sh["cpes.refs.ref"][r]):
            cpes_refinimbiz_sh+=1  
            if(df_cpe_sh["cpes.refs.type"][r] == 'NONE'):
                cpes_refinimbiz_typenone_sh+=1  
            elif(df_cpe_sh["cpes.refs.type"][r] == 'Version'):
                cpes_refinimbiz_typeversion_sh+=1  
            elif(df_cpe_sh["cpes.refs.type"][r] == 'Product'):
                cpes_refinimbiz_typeproduct_sh+=1  
            elif(df_cpe_sh["cpes.refs.type"][r] == 'Advisory'):
                cpes_refinimbiz_typeadvisory_sh+=1  
            elif((df_cpe_sh["cpes.refs.type"][r] == 'Change Log') or (df_cpe_sh["cpes.refs.type"][r] == 'ChangeLog')):
                cpes_refinimbiz_typechangelog_sh+=1  
            elif(df_cpe_sh["cpes.refs.type"][r] == 'Vendor'):
                cpes_refinimbiz_typevendor_sh+=1    
        elif('idec' in df_cpe_sh["cpes.refs.ref"][r]):
            cpes_refidec_sh+=1  
            if(df_cpe_sh["cpes.refs.type"][r] == 'NONE'):
                cpes_refidec_typenone_sh+=1  
            elif(df_cpe_sh["cpes.refs.type"][r] == 'Version'):
                cpes_refidec_typeversion_sh+=1  
            elif(df_cpe_sh["cpes.refs.type"][r] == 'Product'):
                cpes_refidec_typeproduct_sh+=1  
            elif(df_cpe_sh["cpes.refs.type"][r] == 'Advisory'):
                cpes_refidec_typeadvisory_sh+=1  
            elif((df_cpe_sh["cpes.refs.type"][r] == 'Change Log') or (df_cpe_sh["cpes.refs.type"][r] == 'ChangeLog')):
                cpes_refidec_typechangelog_sh+=1  
            elif(df_cpe_sh["cpes.refs.type"][r] == 'Vendor'):
                cpes_refidec_typevendor_sh+=1    
        elif('google' in df_cpe_sh["cpes.refs.ref"][r]):
            cpes_refgoogle_sh+=1  
            if(df_cpe_sh["cpes.refs.type"][r] == 'NONE'):
                cpes_refgoogle_typenone_sh+=1  
            elif(df_cpe_sh["cpes.refs.type"][r] == 'Version'):
                cpes_refgoogle_typeversion_sh+=1  
            elif(df_cpe_sh["cpes.refs.type"][r] == 'Product'):
                cpes_refgoogle_typeproduct_sh+=1  
            elif(df_cpe_sh["cpes.refs.type"][r] == 'Advisory'):
                cpes_refgoogle_typeadvisory_sh+=1  
            elif((df_cpe_sh["cpes.refs.type"][r] == 'Change Log') or (df_cpe_sh["cpes.refs.type"][r] == 'ChangeLog')):
                cpes_refgoogle_typechangelog_sh+=1  
            elif(df_cpe_sh["cpes.refs.type"][r] == 'Vendor'):
                cpes_refgoogle_typevendor_sh+=1    
        elif('docs.bmc' in df_cpe_sh["cpes.refs.ref"][r]):
            cpes_refdocbmc_sh+=1  
            if(df_cpe_sh["cpes.refs.type"][r] == 'NONE'):
                cpes_refdocbmc_typenone_sh+=1  
            elif(df_cpe_sh["cpes.refs.type"][r] == 'Version'):
                cpes_refdocbmc_typeversion_sh+=1  
            elif(df_cpe_sh["cpes.refs.type"][r] == 'Product'):
                cpes_refdocbmc_typeproduct_sh+=1  
            elif(df_cpe_sh["cpes.refs.type"][r] == 'Advisory'):
                cpes_refdocbmc_typeadvisory_sh+=1  
            elif((df_cpe_sh["cpes.refs.type"][r] == 'Change Log') or (df_cpe_sh["cpes.refs.type"][r] == 'ChangeLog')):
                cpes_refdocbmc_typechangelog_sh+=1  
            elif(df_cpe_sh["cpes.refs.type"][r] == 'Vendor'):
                cpes_refdocbmc_typevendor_sh+=1    
        
                
                
                
                
                
                
print("******************************ESTADÍSTICAS RELACION FUENTE Y TIPO DE REFERENCIA CPE PARTE SMART HOME******************************")
print("\n")                            
                
print("\n")
print(" DE UN TOTAL DE "+str(counterrefs_sh)+" REFERENCIAS DE CPES , LAS ESTADISTICAS DE RELACION DE TIPO DE REFERENCIA Y FUENTE DE REFERENCIA SON LAS SIGUIENTES:  \n")
print("\n")
print("      -    EN  "+str(cpes_refapple_sh)+" REFERENCIAS LA FUENTE ES APPLE.COM  \n")
print("      -    EN  "+str(cpes_refcisco_sh)+" REFERENCIAS LA FUENTE ES CISCO.COM  \n")
print("      -    EN  "+str(cpes_refbosch_sh)+" REFERENCIAS LA FUENTE ES BOSCH.COM  \n")
print("      -    EN  "+str(cpes_refcoolkit_sh)+" REFERENCIAS LA FUENTE ES COOLKIT.CN  \n")
print("      -    EN  "+str(cpes_refinimbiz_sh)+" REFERENCIAS LA FUENTE ES INIM.BIZ  \n")
print("      -    EN  "+str(cpes_refidec_sh)+" REFERENCIAS LA FUENTE ES LP.IDEC.COM  \n")
print("      -    EN  "+str(cpes_refgoogle_sh)+" REFERENCIAS LA FUENTE ES GOOGLE.COM  \n")
print("      -    EN  "+str(cpes_refdocbmc_sh)+" REFERENCIAS LA FUENTE ES DOCS.BMC  \n")
print("\n")
print("      -    EN  "+str(cpes_refapple_sh)+" REFERENCIAS LA FUENTE DE REFERENCIA ES APPLE.COM. LAS ESTADÍSTICAS DE TIPO DE REFERENCIA SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(cpes_refapple_typevendor_sh)+" REFERENCIAS EL TIPO ES VENDEDOR ")
print("            -    EN  "+str(cpes_refapple_typeversion_sh)+" REFERENCIAS EL TIPO ES VERSION ")
print("            -    EN  "+str(cpes_refapple_typeproduct_sh)+" REFERENCIAS EL TIPO ES PRODUCTO ")
print("            -    EN  "+str(cpes_refapple_typeadvisory_sh)+" REFERENCIAS EL TIPO ES AVISO ")
print("            -    EN  "+str(cpes_refapple_typechangelog_sh)+" REFERENCIAS EL TIPO ES REGISTRO DE CAMBIO ")
print("            -    EN  "+str(cpes_refapple_typenone_sh)+" REFERENCIAS EL TIPO NO VIENE ESPECIFICADO")
print("\n")
print("      -    EN  "+str(cpes_refcisco_sh)+" REFERENCIAS LA FUENTE DE REFERENCIA ES CISCO.COM. LAS ESTADÍSTICAS DE TIPO DE REFERENCIA SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(cpes_refcisco_typevendor_sh)+" REFERENCIAS EL TIPO ES VENDEDOR ")
print("            -    EN  "+str(cpes_refcisco_typeversion_sh)+" REFERENCIAS EL TIPO ES VERSION ")
print("            -    EN  "+str(cpes_refcisco_typeproduct_sh)+" REFERENCIAS EL TIPO ES PRODUCTO ")
print("            -    EN  "+str(cpes_refcisco_typeadvisory_sh)+" REFERENCIAS EL TIPO ES AVISO ")
print("            -    EN  "+str(cpes_refcisco_typechangelog_sh)+" REFERENCIAS EL TIPO ES REGISTRO DE CAMBIO ")
print("            -    EN  "+str(cpes_refcisco_typenone_sh)+" REFERENCIAS EL TIPO NO VIENE ESPECIFICADO")
print("\n")
print("      -    EN  "+str(cpes_refbosch_sh)+" REFERENCIAS LA FUENTE DE REFERENCIA ES BOSCH.COM. LAS ESTADÍSTICAS DE TIPO DE REFERENCIA SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(cpes_refbosch_typevendor_sh)+" REFERENCIAS EL TIPO ES VENDEDOR ")
print("            -    EN  "+str(cpes_refbosch_typeversion_sh)+" REFERENCIAS EL TIPO ES VERSION ")
print("            -    EN  "+str(cpes_refbosch_typeproduct_sh)+" REFERENCIAS EL TIPO ES PRODUCTO ")
print("            -    EN  "+str(cpes_refbosch_typeadvisory_sh)+" REFERENCIAS EL TIPO ES AVISO ")
print("            -    EN  "+str(cpes_refbosch_typechangelog_sh)+" REFERENCIAS EL TIPO ES REGISTRO DE CAMBIO ")
print("            -    EN  "+str(cpes_refbosch_typenone_sh)+" REFERENCIAS EL TIPO NO VIENE ESPECIFICADO")
print("\n")
print("      -    EN  "+str(cpes_refcoolkit_sh)+" REFERENCIAS LA FUENTE DE REFERENCIA ES COOLKIT.CN. LAS ESTADÍSTICAS DE TIPO DE REFERENCIA SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(cpes_refcoolkit_typevendor_sh)+" REFERENCIAS EL TIPO ES VENDEDOR ")
print("            -    EN  "+str(cpes_refcoolkit_typeversion_sh)+" REFERENCIAS EL TIPO ES VERSION ")
print("            -    EN  "+str(cpes_refcoolkit_typeproduct_sh)+" REFERENCIAS EL TIPO ES PRODUCTO ")
print("            -    EN  "+str(cpes_refcoolkit_typeadvisory_sh)+" REFERENCIAS EL TIPO ES AVISO ")
print("            -    EN  "+str(cpes_refcoolkit_typechangelog_sh)+" REFERENCIAS EL TIPO ES REGISTRO DE CAMBIO ")
print("            -    EN  "+str(cpes_refcoolkit_typenone_sh)+" REFERENCIAS EL TIPO NO VIENE ESPECIFICADO")
print("\n")
print("      -    EN  "+str(cpes_refinimbiz_sh)+" REFERENCIAS LA FUENTE DE REFERENCIA ES INIM.BIZ. LAS ESTADÍSTICAS DE TIPO DE REFERENCIA SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(cpes_refinimbiz_typevendor_sh)+" REFERENCIAS EL TIPO ES VENDEDOR ")
print("            -    EN  "+str(cpes_refinimbiz_typeversion_sh)+" REFERENCIAS EL TIPO ES VERSION ")
print("            -    EN  "+str(cpes_refinimbiz_typeproduct_sh)+" REFERENCIAS EL TIPO ES PRODUCTO ")
print("            -    EN  "+str(cpes_refinimbiz_typeadvisory_sh)+" REFERENCIAS EL TIPO ES AVISO ")
print("            -    EN  "+str(cpes_refinimbiz_typechangelog_sh)+" REFERENCIAS EL TIPO ES REGISTRO DE CAMBIO ")
print("            -    EN  "+str(cpes_refinimbiz_typenone_sh)+" REFERENCIAS EL TIPO NO VIENE ESPECIFICADO")
print("\n")
print("      -    EN  "+str(cpes_refidec_sh)+" REFERENCIAS LA FUENTE DE REFERENCIA ES LP.IDEC.COM. LAS ESTADÍSTICAS DE TIPO DE REFERENCIA SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(cpes_refidec_typevendor_sh)+" REFERENCIAS EL TIPO ES VENDEDOR ")
print("            -    EN  "+str(cpes_refidec_typeversion_sh)+" REFERENCIAS EL TIPO ES VERSION ")
print("            -    EN  "+str(cpes_refidec_typeproduct_sh)+" REFERENCIAS EL TIPO ES PRODUCTO ")
print("            -    EN  "+str(cpes_refidec_typeadvisory_sh)+" REFERENCIAS EL TIPO ES AVISO ")
print("            -    EN  "+str(cpes_refidec_typechangelog_sh)+" REFERENCIAS EL TIPO ES REGISTRO DE CAMBIO ")
print("            -    EN  "+str(cpes_refidec_typenone_sh)+" REFERENCIAS EL TIPO NO VIENE ESPECIFICADO")
print("\n")
print("      -    EN  "+str(cpes_refgoogle_sh)+" REFERENCIAS LA FUENTE DE REFERENCIA ES GOOGLE.COM. LAS ESTADÍSTICAS DE TIPO DE REFERENCIA SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(cpes_refgoogle_typevendor_sh)+" REFERENCIAS EL TIPO ES VENDEDOR ")
print("            -    EN  "+str(cpes_refgoogle_typeversion_sh)+" REFERENCIAS EL TIPO ES VERSION ")
print("            -    EN  "+str(cpes_refgoogle_typeproduct_sh)+" REFERENCIAS EL TIPO ES PRODUCTO ")
print("            -    EN  "+str(cpes_refgoogle_typeadvisory_sh)+" REFERENCIAS EL TIPO ES AVISO ")
print("            -    EN  "+str(cpes_refgoogle_typechangelog_sh)+" REFERENCIAS EL TIPO ES REGISTRO DE CAMBIO ")
print("            -    EN  "+str(cpes_refgoogle_typenone_sh)+" REFERENCIAS EL TIPO NO VIENE ESPECIFICADO")
print("\n")
print("      -    EN  "+str(cpes_refdocbmc_sh)+" REFERENCIAS LA FUENTE DE REFERENCIA ES DOCS.BMC. LAS ESTADÍSTICAS DE TIPO DE REFERENCIA SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(cpes_refdocbmc_typevendor_sh)+" REFERENCIAS EL TIPO ES VENDEDOR ")
print("            -    EN  "+str(cpes_refdocbmc_typeversion_sh)+" REFERENCIAS EL TIPO ES VERSION ")
print("            -    EN  "+str(cpes_refdocbmc_typeproduct_sh)+" REFERENCIAS EL TIPO ES PRODUCTO ")
print("            -    EN  "+str(cpes_refdocbmc_typeadvisory_sh)+" REFERENCIAS EL TIPO ES AVISO ")
print("            -    EN  "+str(cpes_refdocbmc_typechangelog_sh)+" REFERENCIAS EL TIPO ES REGISTRO DE CAMBIO ")
print("            -    EN  "+str(cpes_refdocbmc_typenone_sh)+" REFERENCIAS EL TIPO NO VIENE ESPECIFICADO")
print("\n")


print("******************************PORCENTAJES RELACION TIPO Y FUENTE DE REFERENCIA CPES PARTE SMART HOME******************************")
print("\n")        
            
          
    
print("\n")
print(" DE UN TOTAL DE "+str(counterrefs_sh)+" REFERENCIAS DE CPES , LOS PORCENTAJES DE TIPO DE REFERENCIA Y FUENTE DE REFERENCIA SON LOS SIGUIENTES:  \n")
print("\n")
print("\n")
print("      -    EN  EL "+str(float(((cpes_refapple_sh*100)/counterrefs_sh)))+" % DE REFERENCIAS LA FUENTE ES APPLE.COM  \n")
print("      -    EN  EL "+str(float(((cpes_refcisco_sh*100)/counterrefs_sh)))+" % DE REFERENCIAS LA FUENTE ES CISCO.COM  \n")
print("      -    EN  EL "+str(float(((cpes_refbosch_sh*100)/counterrefs_sh)))+" % DE REFERENCIAS LA FUENTE ES BOSCH.COM  \n")
print("      -    EN  EL "+str(float(((cpes_refcoolkit_sh*100)/counterrefs_sh)))+" % DE REFERENCIAS LA FUENTE ES COOLKIT.CN  \n")
print("      -    EN  EL "+str(float(((cpes_refinimbiz_sh*100)/counterrefs_sh)))+" % DE REFERENCIAS LA FUENTE ES INIM.BIZ  \n")
print("      -    EN  EL "+str(float(((cpes_refidec_sh*100)/counterrefs_sh)))+" % DE REFERENCIAS LA FUENTE ES LP.IDEC.COM  \n")
print("      -    EN  EL "+str(float(((cpes_refgoogle_sh*100)/counterrefs_sh)))+" % DE REFERENCIAS LA FUENTE ES GOOGLE.COM  \n")
print("      -    EN  EL "+str(float(((cpes_refdocbmc_sh*100)/counterrefs_sh)))+" % DE REFERENCIAS LA FUENTE ES DOCS.BMC  \n")
print("\n")
print("      -    EN EL "+str(float(((cpes_refapple_sh*100)/counterrefs_sh)))+" % DE REFERENCIAS DE CPES DONDE LA FUENTE DE REFERENCIA ES APPLE.COM, LOS PORCENTAJES DE TIPO DE REFERENCIA SON LOS SIGUIENTES:  \n")
print("\n")
print("            -    EN EL "+str(float(((cpes_refapple_typevendor_sh*100)/cpes_refapple_sh)))+" % DE REFERENCIAS EL TIPO ES VENDEDOR  ")
print("            -    EN EL "+str(float(((cpes_refapple_typeversion_sh*100)/cpes_refapple_sh)))+" % DE REFERENCIAS EL TIPO ES VERSION ")
print("            -    EN EL "+str(float(((cpes_refapple_typeproduct_sh*100)/cpes_refapple_sh)))+" % DE REFERENCIAS EL TIPO ES PRODUCTO ")
print("            -    EN EL "+str(float(((cpes_refapple_typeadvisory_sh*100)/cpes_refapple_sh)))+" % DE REFERENCIAS EL TIPO ES AVISO ")
print("            -    EN EL "+str(float(((cpes_refapple_typechangelog_sh*100)/cpes_refapple_sh)))+" % DE REFERENCIAS EL TIPO ES REGISTRO DE CAMBIO ")
print("            -    EN EL "+str(float(((cpes_refapple_typenone_sh*100)/cpes_refapple_sh)))+" % DE REFERENCIAS EL TIPO NO VIENE ESPECIFICADO ")
print("\n")
print("      -    EN EL "+str(float(((cpes_refcisco_sh*100)/counterrefs_sh)))+" % DE REFERENCIAS DE CPES DONDE LA FUENTE DE REFERENCIA ES CISCO.COM, LOS PORCENTAJES DE TIPO DE REFERENCIA SON LOS SIGUIENTES:  \n")
print("\n")
print("            -    EN EL "+str(float(((cpes_refcisco_typevendor_sh*100)/cpes_refcisco_sh)))+" % DE REFERENCIAS EL TIPO ES VENDEDOR  ")
print("            -    EN EL "+str(float(((cpes_refcisco_typeversion_sh*100)/cpes_refcisco_sh)))+" % DE REFERENCIAS EL TIPO ES VERSION ")
print("            -    EN EL "+str(float(((cpes_refcisco_typeproduct_sh*100)/cpes_refcisco_sh)))+" % DE REFERENCIAS EL TIPO ES PRODUCTO ")
print("            -    EN EL "+str(float(((cpes_refcisco_typeadvisory_sh*100)/cpes_refcisco_sh)))+" % DE REFERENCIAS EL TIPO ES AVISO ")
print("            -    EN EL "+str(float(((cpes_refcisco_typechangelog_sh*100)/cpes_refcisco_sh)))+" % DE REFERENCIAS EL TIPO ES REGISTRO DE CAMBIO ")
print("            -    EN EL "+str(float(((cpes_refcisco_typenone_sh*100)/cpes_refcisco_sh)))+" % DE REFERENCIAS EL TIPO NO VIENE ESPECIFICADO ")
print("\n")
print("      -    EN EL "+str(float(((cpes_refbosch_sh*100)/counterrefs_sh)))+" % DE REFERENCIAS DE CPES DONDE LA FUENTE DE REFERENCIA ES SYMBIOTE.COM, LOS PORCENTAJES DE TIPO DE REFERENCIA SON LOS SIGUIENTES:  \n")
print("\n")
print("            -    EN EL "+str(float(((cpes_refbosch_typevendor_sh*100)/cpes_refbosch_sh)))+" % DE REFERENCIAS EL TIPO ES VENDEDOR  ")
print("            -    EN EL "+str(float(((cpes_refbosch_typeversion_sh*100)/cpes_refbosch_sh)))+" % DE REFERENCIAS EL TIPO ES VERSION ")
print("            -    EN EL "+str(float(((cpes_refbosch_typeproduct_sh*100)/cpes_refbosch_sh)))+" % DE REFERENCIAS EL TIPO ES PRODUCTO ")
print("            -    EN EL "+str(float(((cpes_refbosch_typeadvisory_sh*100)/cpes_refbosch_sh)))+" % DE REFERENCIAS EL TIPO ES AVISO ")
print("            -    EN EL "+str(float(((cpes_refbosch_typechangelog_sh*100)/cpes_refbosch_sh)))+" % DE REFERENCIAS EL TIPO ES REGISTRO DE CAMBIO ")
print("            -    EN EL "+str(float(((cpes_refbosch_typenone_sh*100)/cpes_refbosch_sh)))+" % DE REFERENCIAS EL TIPO NO VIENE ESPECIFICADO ")
print("\n")
print("      -    EN EL "+str(float(((cpes_refcoolkit_sh*100)/counterrefs_sh)))+" % DE REFERENCIAS DE CPES DONDE LA FUENTE DE REFERENCIA ES ASUS.COM, LOS PORCENTAJES DE TIPO DE REFERENCIA SON LOS SIGUIENTES:  \n")
print("\n")
print("            -    EN EL "+str(float(((cpes_refcoolkit_typevendor_sh*100)/cpes_refcoolkit_sh)))+" % DE REFERENCIAS EL TIPO ES VENDEDOR  ")
print("            -    EN EL "+str(float(((cpes_refcoolkit_typeversion_sh*100)/cpes_refcoolkit_sh)))+" % DE REFERENCIAS EL TIPO ES VERSION ")
print("            -    EN EL "+str(float(((cpes_refcoolkit_typeproduct_sh*100)/cpes_refcoolkit_sh)))+" % DE REFERENCIAS EL TIPO ES PRODUCTO ")
print("            -    EN EL "+str(float(((cpes_refcoolkit_typeadvisory_sh*100)/cpes_refcoolkit_sh)))+" % DE REFERENCIAS EL TIPO ES AVISO ")
print("            -    EN EL "+str(float(((cpes_refcoolkit_typechangelog_sh*100)/cpes_refcoolkit_sh)))+" % DE REFERENCIAS EL TIPO ES REGISTRO DE CAMBIO ")
print("            -    EN EL "+str(float(((cpes_refcoolkit_typenone_sh*100)/cpes_refcoolkit_sh)))+" % DE REFERENCIAS EL TIPO NO VIENE ESPECIFICADO ")
print("\n")
print("      -    EN EL "+str(float(((cpes_refinimbiz_sh*100)/counterrefs_sh)))+" % DE REFERENCIAS DE CPES DONDE LA FUENTE DE REFERENCIA ES IOTKONKER, LOS PORCENTAJES DE TIPO DE REFERENCIA SON LOS SIGUIENTES:  \n")
print("\n")
print("            -    EN EL "+str(float(((cpes_refinimbiz_typevendor_sh*100)/cpes_refinimbiz_sh)))+" % DE REFERENCIAS EL TIPO ES VENDEDOR  ")
print("            -    EN EL "+str(float(((cpes_refinimbiz_typeversion_sh*100)/cpes_refinimbiz_sh)))+" % DE REFERENCIAS EL TIPO ES VERSION ")
print("            -    EN EL "+str(float(((cpes_refinimbiz_typeproduct_sh*100)/cpes_refinimbiz_sh)))+" % DE REFERENCIAS EL TIPO ES PRODUCTO ")
print("            -    EN EL "+str(float(((cpes_refinimbiz_typeadvisory_sh*100)/cpes_refinimbiz_sh)))+" % DE REFERENCIAS EL TIPO ES AVISO ")
print("            -    EN EL "+str(float(((cpes_refinimbiz_typechangelog_sh*100)/cpes_refinimbiz_sh)))+" % DE REFERENCIAS EL TIPO ES REGISTRO DE CAMBIO ")
print("            -    EN EL "+str(float(((cpes_refinimbiz_typenone_sh*100)/cpes_refinimbiz_sh)))+" % DE REFERENCIAS EL TIPO NO VIENE ESPECIFICADO ")
print("\n")
print("      -    EN EL "+str(float(((cpes_refidec_sh*100)/counterrefs_sh)))+" % DE REFERENCIAS DE CPES DONDE LA FUENTE DE REFERENCIA ES LP.IDEC.COM, LOS PORCENTAJES DE TIPO DE REFERENCIA SON LOS SIGUIENTES:  \n")
print("\n")
print("            -    EN EL "+str(float(((cpes_refidec_typevendor_sh*100)/cpes_refidec_sh)))+" % DE REFERENCIAS EL TIPO ES VENDEDOR  ")
print("            -    EN EL "+str(float(((cpes_refidec_typeversion_sh*100)/cpes_refidec_sh)))+" % DE REFERENCIAS EL TIPO ES VERSION ")
print("            -    EN EL "+str(float(((cpes_refidec_typeproduct_sh*100)/cpes_refidec_sh)))+" % DE REFERENCIAS EL TIPO ES PRODUCTO ")
print("            -    EN EL "+str(float(((cpes_refidec_typeadvisory_sh*100)/cpes_refidec_sh)))+" % DE REFERENCIAS EL TIPO ES AVISO ")
print("            -    EN EL "+str(float(((cpes_refidec_typechangelog_sh*100)/cpes_refidec_sh)))+" % DE REFERENCIAS EL TIPO ES REGISTRO DE CAMBIO ")
print("            -    EN EL "+str(float(((cpes_refidec_typenone_sh*100)/cpes_refidec_sh)))+" % DE REFERENCIAS EL TIPO NO VIENE ESPECIFICADO ")
print("\n")
print("      -    EN EL "+str(float(((cpes_refgoogle_sh*100)/counterrefs_sh)))+" % DE REFERENCIAS DE CPES DONDE LA FUENTE DE REFERENCIA ES GOOGLE.COM, LOS PORCENTAJES DE TIPO DE REFERENCIA SON LOS SIGUIENTES:  \n")
print("\n")
print("            -    EN EL "+str(float(((cpes_refgoogle_typevendor_sh*100)/cpes_refgoogle_sh)))+" % DE REFERENCIAS EL TIPO ES VENDEDOR  ")
print("            -    EN EL "+str(float(((cpes_refgoogle_typeversion_sh*100)/cpes_refgoogle_sh)))+" % DE REFERENCIAS EL TIPO ES VERSION ")
print("            -    EN EL "+str(float(((cpes_refgoogle_typeproduct_sh*100)/cpes_refgoogle_sh)))+" % DE REFERENCIAS EL TIPO ES PRODUCTO ")
print("            -    EN EL "+str(float(((cpes_refgoogle_typeadvisory_sh*100)/cpes_refgoogle_sh)))+" % DE REFERENCIAS EL TIPO ES AVISO ")
print("            -    EN EL "+str(float(((cpes_refgoogle_typechangelog_sh*100)/cpes_refgoogle_sh)))+" % DE REFERENCIAS EL TIPO ES REGISTRO DE CAMBIO ")
print("            -    EN EL "+str(float(((cpes_refgoogle_typenone_sh*100)/cpes_refgoogle_sh)))+" % DE REFERENCIAS EL TIPO NO VIENE ESPECIFICADO ")
print("\n")
print("      -    EN EL "+str(float(((cpes_refdocbmc_sh*100)/counterrefs_sh)))+" % DE REFERENCIAS DE CPES DONDE LA FUENTE DE REFERENCIA ES DOCS.BMC, LOS PORCENTAJES DE TIPO DE REFERENCIA SON LOS SIGUIENTES:  \n")
print("\n")
print("            -    EN EL "+str(float(((cpes_refdocbmc_typevendor_sh*100)/cpes_refdocbmc_sh)))+" % DE REFERENCIAS EL TIPO ES VENDEDOR  ")
print("            -    EN EL "+str(float(((cpes_refdocbmc_typeversion_sh*100)/cpes_refdocbmc_sh)))+" % DE REFERENCIAS EL TIPO ES VERSION ")
print("            -    EN EL "+str(float(((cpes_refdocbmc_typeproduct_sh*100)/cpes_refdocbmc_sh)))+" % DE REFERENCIAS EL TIPO ES PRODUCTO ")
print("            -    EN EL "+str(float(((cpes_refdocbmc_typeadvisory_sh*100)/cpes_refdocbmc_sh)))+" % DE REFERENCIAS EL TIPO ES AVISO ")
print("            -    EN EL "+str(float(((cpes_refdocbmc_typechangelog_sh*100)/cpes_refdocbmc_sh)))+" % DE REFERENCIAS EL TIPO ES REGISTRO DE CAMBIO ")
print("            -    EN EL "+str(float(((cpes_refdocbmc_typenone_sh*100)/cpes_refdocbmc_sh)))+" % DE REFERENCIAS EL TIPO NO VIENE ESPECIFICADO ")
print("\n")




























