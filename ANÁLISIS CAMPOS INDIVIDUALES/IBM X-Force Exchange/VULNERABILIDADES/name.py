


import pandas as pd
from datetime import datetime,timedelta



#Abro los ficheros con los que voy a tratar




df_vulnibm_iot = pd.read_excel('vulnerabilidades_ibm_iot_2023.xlsx')

#Variable que almacenara el contador total de valores de nombre
count_vulnibm_iot_names=0
#Variables que almacenan el contador de valores especificos de nombre
count_vulnibm_iot_namepathtraversal=0
count_vulnibm_iot_namedirectorytraversal=0
count_vulnibm_iot_nameprivilegeescalation=0
count_vulnibm_iot_namecrosssitescripting=0
count_vulnibm_iot_namesecuritybypass=0
count_vulnibm_iot_namesinformationdisclosure=0
count_vulnibm_iot_namedenialofservice=0
count_vulnibm_iot_namecodeexecution=0
count_vulnibm_iot_namemaninthemiddle=0
count_vulnibm_iot_namesqlinjection=0
count_vulnibm_iot_namecrosssiterequestforgery=0
count_vulnibm_iot_namemoduleexecution=0
count_vulnibm_iot_namebufferoverflow=0
count_vulnibm_iot_namecommandexecution=0
count_vulnibm_iot_namespoofing=0
count_vulnibm_iot_nameclickjacking=0
count_vulnibm_iot_namehijacking=0
count_vulnibm_iot_namefileinclude=0
count_vulnibm_iot_namebruteforce=0
count_vulnibm_iot_namefileupload=0
count_vulnibm_iot_nameheaderinjection=0
count_vulnibm_iot_nametampering=0
count_vulnibm_iot_nameanother=0


#Comprobamos el contenido de name
for r in range(0,len(df_vulnibm_iot["name"])):
    #Obtengo el valor de nombre y aumento contadores segun el tipo que sea
    aux_str=df_vulnibm_iot["name"][r].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
    if(aux_str!='NONE'):
        count_vulnibm_iot_names+=1
        if('pathtraversal' in aux_str):
            count_vulnibm_iot_namepathtraversal+=1
        elif('directorytraversal' in aux_str):
            count_vulnibm_iot_namedirectorytraversal+=1
        elif('privilegeescalation' in aux_str):
            count_vulnibm_iot_nameprivilegeescalation+=1
        elif('cross-sitescripting' in aux_str):
            count_vulnibm_iot_namecrosssitescripting+=1                            
        elif('securitybypass' in aux_str):
            count_vulnibm_iot_namesecuritybypass+=1                           
        elif('information_disclosure' in aux_str or 'informationdisclosure' in aux_str):
            count_vulnibm_iot_namesinformationdisclosure+=1                           
        elif('denialofservice' in aux_str):
            count_vulnibm_iot_namedenialofservice+=1                           
        elif('codeexecution' in aux_str):
            count_vulnibm_iot_namecodeexecution+=1                           
        elif('maninthemiddle' in aux_str):
            count_vulnibm_iot_namemaninthemiddle+=1                           
        elif('SQLinjection' in aux_str):
            count_vulnibm_iot_namesqlinjection+=1                           
        elif('cross-siterequestforgery' in aux_str):
            count_vulnibm_iot_namecrosssiterequestforgery+=1                           
        elif('moduleexecution' in aux_str):
            count_vulnibm_iot_namemoduleexecution+=1                           
        elif('bufferoverflow' in aux_str):
            count_vulnibm_iot_namebufferoverflow+=1                           
        elif('commandexecution' in aux_str):
            count_vulnibm_iot_namecommandexecution+=1                           
        elif('spoofing' in aux_str):
            count_vulnibm_iot_namespoofing+=1                           
        elif('clickjacking' in aux_str):
            count_vulnibm_iot_nameclickjacking+=1
        elif('hijacking' in aux_str):
            count_vulnibm_iot_namehijacking+=1
        elif('fileinclude' in aux_str):
            count_vulnibm_iot_namefileinclude+=1
        elif('bruteforce' in aux_str):
            count_vulnibm_iot_namebruteforce+=1
        elif('fileupload' in aux_str):
            count_vulnibm_iot_namefileupload+=1
        elif('headerinjection' in aux_str):
            count_vulnibm_iot_nameheaderinjection+=1
        elif('Tampering' in aux_str):
            count_vulnibm_iot_nametampering+=1
        else:
            count_vulnibm_iot_nameanother+=1

print("***************************ESTADÍSTICAS NOMBRE VULNERABILIDADES IBM PARTE IOT***************************")
print("\n")                            
                
print("\n")
print(" DE UN TOTAL DE "+str(count_vulnibm_iot_names)+" VALORES DE NOMBRE :\n") 
print("\n")
print("   - LAS ESTADISTICAS DE CADENAS DE TEXTO ENCONTRADAS EN EL VALOR DE NOMBRE DE OBJETO SON LAS SIGUIENTES:  \n")
print("            -    EN  "+str(count_vulnibm_iot_namepathtraversal)+" VULNERABILIDADES , EL NOMBRE INCLUYE PATH TRAVERSAL ")
print("            -    EN  "+str(count_vulnibm_iot_namedirectorytraversal)+" VULNERABILIDADES , EL NOMBRE INCLUYE DIRECTORY TRAVERSAL")
print("            -    EN  "+str(count_vulnibm_iot_nameprivilegeescalation)+" VULNERABILIDADES , EL NOMBRE INCLUYE PRIVILEGE ESCALATION")
print("            -    EN  "+str(count_vulnibm_iot_namecrosssitescripting)+" VULNERABILIDADES , EL NOMBRE INCLUYE CROSS SITE SCRIPTING ")
print("            -    EN  "+str(count_vulnibm_iot_namesecuritybypass)+" VULNERABILIDADES , EL NOMBRE INCLUYE SECURITY BYPASS ")
print("            -    EN  "+str(count_vulnibm_iot_namesinformationdisclosure)+" VULNERABILIDADES , EL NOMBRE INCLUYE INFORMATION DISCLOSURE")
print("            -    EN  "+str(count_vulnibm_iot_namedenialofservice)+" VULNERABILIDADES , EL NOMBRE INCLUYE DENIAL OF SERVICE")
print("            -    EN  "+str(count_vulnibm_iot_namecodeexecution)+" VULNERABILIDADES , EL NOMBRE INCLUYE CODE EXECUTION ")
print("            -    EN  "+str(count_vulnibm_iot_namemaninthemiddle)+" VULNERABILIDADES , EL NOMBRE INCLUYE MAN IN THE MIDDLE ")
print("            -    EN  "+str(count_vulnibm_iot_namesqlinjection)+" VULNERABILIDADES , EL NOMBRE INCLUYE SQL INJECTION")
print("            -    EN  "+str(count_vulnibm_iot_namecrosssiterequestforgery)+" VULNERABILIDADES , EL NOMBRE INCLUYE CROSS SITE REQUEST FORGERY")
print("            -    EN  "+str(count_vulnibm_iot_namemoduleexecution)+" VULNERABILIDADES , EL NOMBRE INCLUYE MODULE EXECUTION ")
print("            -    EN  "+str(count_vulnibm_iot_namebufferoverflow)+" VULNERABILIDADES , EL NOMBRE INCLUYE BUFFER OVERFLOW")
print("            -    EN  "+str(count_vulnibm_iot_namecommandexecution)+" VULNERABILIDADES , EL NOMBRE INCLUYE COMMAND EXECUTION")
print("            -    EN  "+str(count_vulnibm_iot_namespoofing)+" VULNERABILIDADES , EL NOMBRE INCLUYE SPOOFING")
print("            -    EN  "+str(count_vulnibm_iot_nameclickjacking)+" VULNERABILIDADES , EL NOMBRE INCLUYE CLICKJACKING ")
print("            -    EN  "+str(count_vulnibm_iot_namehijacking)+" VULNERABILIDADES , EL NOMBRE INCLUYE NAME HIJACKING")
print("            -    EN  "+str(count_vulnibm_iot_namefileinclude)+" VULNERABILIDADES , EL NOMBRE INCLUYE FILE INCLUDE")
print("            -    EN  "+str(count_vulnibm_iot_namebruteforce)+" VULNERABILIDADES , EL NOMBRE INCLUYE BRUTE FORCE")
print("            -    EN  "+str(count_vulnibm_iot_namefileupload)+" VULNERABILIDADES , EL NOMBRE INCLUYE FILE UPLOAD ")
print("            -    EN  "+str(count_vulnibm_iot_nameheaderinjection)+" VULNERABILIDADES , EL NOMBRE INCLUYE HEADER INJECTION")
print("            -    EN  "+str(count_vulnibm_iot_nametampering)+" VULNERABILIDADES , EL NOMBRE INCLUYE TAMPERING")
print("            -    EN  "+str(count_vulnibm_iot_nameanother)+" VULNERABILIDADES , EL NOMBRE INCLUYE UNA CADENA DISTINTA")
print("\n")
                                    





print("***************************PORCENTAJES NAME VULNERABILIDADES IBM PARTE IOT***************************")
print("\n")                            
                
print("\n")
print(" DE UN TOTAL DE "+str(count_vulnibm_iot_names)+" VALORES DE NOMBRE :\n") 
print("\n")
print("   - LOS PORCENTAJES DE CADENAS DE TEXTO ENCONTRADAS EN EL VALOR DE NOMBRE DE OBJETO SON LOS SIGUIENTES:  \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namepathtraversal*100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES , EL NOMBRE INCLUYE PATH TRAVERSAL ")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namedirectorytraversal*100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES , EL NOMBRE INCLUYE DIRECTORY TRAVERSAL")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_nameprivilegeescalation*100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES , EL NOMBRE INCLUYE PRIVILEGE ESCALATION ")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namecrosssitescripting*100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES , EL NOMBRE INCLUYE CROSS SITE SCRIPTING ")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namesecuritybypass*100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES , EL NOMBRE INCLUYE SECURITY BYPASS ")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namesinformationdisclosure*100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES , EL NOMBRE INCLUYE INFORMATION DISCLOSURE ")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namecodeexecution*100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES , EL NOMBRE INCLUYE CODE EXECUTION ")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namemaninthemiddle*100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES , EL NOMBRE INCLUYE MAN IN THE MIDDLE ")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namesqlinjection*100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES , EL NOMBRE INCLUYE SQL INJECTION")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namecrosssiterequestforgery*100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES , EL NOMBRE INCLUYE CROSS SITE REQUEST FORGERY ")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namemoduleexecution*100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES , EL NOMBRE INCLUYE MODULE EXECUTION")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namebufferoverflow*100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES , EL NOMBRE INCLUYE BUFFER OVERFLOW")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namecommandexecution*100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES , EL NOMBRE INCLUYE COMMAND EXECUTION")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namespoofing*100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES , EL NOMBRE INCLUYE SPOOFING")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_nameclickjacking*100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES , EL NOMBRE INCLUYE CLICKJACKING")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namehijacking*100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES , EL NOMBRE INCLUYE HIJACKING")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namefileinclude*100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES , EL NOMBRE INCLUYE FILE INCLUDE")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namebruteforce*100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES , EL NOMBRE INCLUYE BRUTE FORCE")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namefileupload*100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES , EL NOMBRE INCLUYE FILE UPLOAD")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_nameheaderinjection*100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES , EL NOMBRE INCLUYE HEADER INJECTION")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_nametampering*100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES , EL NOMBRE INCLUYE TAMPERING")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_nameanother*100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES , EL NOMBRE INCLUYE UN VALOR DISTINTO")
print("\n")
    














#Abro los ficheros con los que voy a tratar




df_vulnibm_sh = pd.read_excel('vulnerabilidades_ibm_smart_home_2023.xlsx')
#Variable que almacenara el contador total de valores de nombre
count_vulnibm_sh_names=0
#Variables que almacenan el contador de valores especificos de nombre
count_vulnibm_sh_namepathtraversal=0
count_vulnibm_sh_namedirectorytraversal=0
count_vulnibm_sh_nameprivilegeescalation=0
count_vulnibm_sh_namecrosssitescripting=0
count_vulnibm_sh_namesecuritybypass=0
count_vulnibm_sh_namesinformationdisclosure=0
count_vulnibm_sh_namedenialofservice=0
count_vulnibm_sh_namecodeexecution=0
count_vulnibm_sh_namemaninthemiddle=0
count_vulnibm_sh_namesqlinjection=0
count_vulnibm_sh_namecrosssiterequestforgery=0
count_vulnibm_sh_namemoduleexecution=0
count_vulnibm_sh_namebufferoverflow=0
count_vulnibm_sh_namecommandexecution=0
count_vulnibm_sh_namespoofing=0
count_vulnibm_sh_nameclickjacking=0
count_vulnibm_sh_namehijacking=0
count_vulnibm_sh_namefileinclude=0
count_vulnibm_sh_namebruteforce=0
count_vulnibm_sh_namefileupload=0
count_vulnibm_sh_nameheaderinjection=0
count_vulnibm_sh_nametampering=0
count_vulnibm_sh_nameanother=0


#Comprobamos el contenido de name
for r in range(0,len(df_vulnibm_sh["name"])): 
    #Obtengo el valor de name , lo compruebo y aumento contadores segun el valor que sea
    aux_str=df_vulnibm_sh["name"][r].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
    if(aux_str!='NONE'):
        count_vulnibm_sh_names+=1
        if('pathtraversal' in aux_str):
            count_vulnibm_sh_namepathtraversal+=1
        elif('directorytraversal' in aux_str):
            count_vulnibm_sh_namedirectorytraversal+=1
        elif('privilegeescalation' in aux_str):
            count_vulnibm_sh_nameprivilegeescalation+=1
        elif('cross-sitescripting' in aux_str):
            count_vulnibm_sh_namecrosssitescripting+=1                            
        elif('securitybypass' in aux_str):
            count_vulnibm_sh_namesecuritybypass+=1                           
        elif('information_disclosure' in aux_str or 'informationdisclosure' in aux_str):
            count_vulnibm_sh_namesinformationdisclosure+=1                           
        elif('denialofservice' in aux_str):
            count_vulnibm_sh_namedenialofservice+=1                           
        elif('codeexecution' in aux_str):
            count_vulnibm_sh_namecodeexecution+=1                           
        elif('maninthemiddle' in aux_str):
            count_vulnibm_sh_namemaninthemiddle+=1                           
        elif('SQLinjection' in aux_str):
            count_vulnibm_sh_namesqlinjection+=1                           
        elif('cross-siterequestforgery' in aux_str):
            count_vulnibm_sh_namecrosssiterequestforgery+=1                           
        elif('moduleexecution' in aux_str):
            count_vulnibm_sh_namemoduleexecution+=1                           
        elif('bufferoverflow' in aux_str):
            count_vulnibm_sh_namebufferoverflow+=1                           
        elif('commandexecution' in aux_str):
            count_vulnibm_sh_namecommandexecution+=1                           
        elif('spoofing' in aux_str):
            count_vulnibm_sh_namespoofing+=1                           
        elif('clickjacking' in aux_str):
            count_vulnibm_sh_nameclickjacking+=1
        elif('hijacking' in aux_str):
            count_vulnibm_sh_namehijacking+=1
        elif('fileinclude' in aux_str):
            count_vulnibm_sh_namefileinclude+=1
        elif('bruteforce' in aux_str):
            count_vulnibm_sh_namebruteforce+=1
        elif('fileupload' in aux_str):
            count_vulnibm_sh_namefileupload+=1
        elif('headerinjection' in aux_str):
            count_vulnibm_sh_nameheaderinjection+=1
        elif('Tampering' in aux_str):
            count_vulnibm_sh_nametampering+=1
        else:
            count_vulnibm_sh_nameanother+=1
 
  
print("***************************ESTADÍSTICAS NOMBRE VULNERABILIDADES IBM PARTE SMART HOME***************************")
print("\n")                            
                
print("\n")
print(" DE UN TOTAL DE "+str(count_vulnibm_sh_names)+" VALORES DE NOMBRE :\n") 
print("\n")
print("   - LAS ESTADISTICAS DE CADENAS DE TEXTO ENCONTRADAS EN EL VALOR DE NOMBRE DE OBJETO SON LAS SIGUIENTES:  \n")
print("            -    EN  "+str(count_vulnibm_sh_namepathtraversal)+" VULNERABILIDADES , EL NOMBRE INCLUYE PATH TRAVERSAL ")
print("            -    EN  "+str(count_vulnibm_sh_namedirectorytraversal)+" VULNERABILIDADES , EL NOMBRE INCLUYE DIRECTORY TRAVERSAL")
print("            -    EN  "+str(count_vulnibm_sh_nameprivilegeescalation)+" VULNERABILIDADES , EL NOMBRE INCLUYE PRIVILEGE ESCALATION")
print("            -    EN  "+str(count_vulnibm_sh_namecrosssitescripting)+" VULNERABILIDADES , EL NOMBRE INCLUYE CROSS SITE SCRIPTING ")
print("            -    EN  "+str(count_vulnibm_sh_namesecuritybypass)+" VULNERABILIDADES , EL NOMBRE INCLUYE SECURITY BYPASS ")
print("            -    EN  "+str(count_vulnibm_sh_namesinformationdisclosure)+" VULNERABILIDADES , EL NOMBRE INCLUYE INFORMATION DISCLOSURE")
print("            -    EN  "+str(count_vulnibm_sh_namedenialofservice)+" VULNERABILIDADES , EL NOMBRE INCLUYE DENIAL OF SERVICE")
print("            -    EN  "+str(count_vulnibm_sh_namecodeexecution)+" VULNERABILIDADES , EL NOMBRE INCLUYE CODE EXECUTION ")
print("            -    EN  "+str(count_vulnibm_sh_namemaninthemiddle)+" VULNERABILIDADES , EL NOMBRE INCLUYE MAN IN THE MIDDLE ")
print("            -    EN  "+str(count_vulnibm_sh_namesqlinjection)+" VULNERABILIDADES , EL NOMBRE INCLUYE SQL INJECTION")
print("            -    EN  "+str(count_vulnibm_sh_namecrosssiterequestforgery)+" VULNERABILIDADES , EL NOMBRE INCLUYE CROSS SITE REQUEST FORGERY")
print("            -    EN  "+str(count_vulnibm_sh_namemoduleexecution)+" VULNERABILIDADES , EL NOMBRE INCLUYE MODULE EXECUTION ")
print("            -    EN  "+str(count_vulnibm_sh_namebufferoverflow)+" VULNERABILIDADES , EL NOMBRE INCLUYE BUFFER OVERFLOW")
print("            -    EN  "+str(count_vulnibm_sh_namecommandexecution)+" VULNERABILIDADES , EL NOMBRE INCLUYE COMMAND EXECUTION")
print("            -    EN  "+str(count_vulnibm_sh_namespoofing)+" VULNERABILIDADES , EL NOMBRE INCLUYE SPOOFING")
print("            -    EN  "+str(count_vulnibm_sh_nameclickjacking)+" VULNERABILIDADES , EL NOMBRE INCLUYE CLICKJACKING ")
print("            -    EN  "+str(count_vulnibm_sh_namehijacking)+" VULNERABILIDADES , EL NOMBRE INCLUYE NAME HIJACKING")
print("            -    EN  "+str(count_vulnibm_sh_namefileinclude)+" VULNERABILIDADES , EL NOMBRE INCLUYE FILE INCLUDE")
print("            -    EN  "+str(count_vulnibm_sh_namebruteforce)+" VULNERABILIDADES , EL NOMBRE INCLUYE BRUTE FORCE")
print("            -    EN  "+str(count_vulnibm_sh_namefileupload)+" VULNERABILIDADES , EL NOMBRE INCLUYE FILE UPLOAD ")
print("            -    EN  "+str(count_vulnibm_sh_nameheaderinjection)+" VULNERABILIDADES , EL NOMBRE INCLUYE HEADER INJECTION")
print("            -    EN  "+str(count_vulnibm_sh_nametampering)+" VULNERABILIDADES , EL NOMBRE INCLUYE TAMPERING")
print("            -    EN  "+str(count_vulnibm_sh_nameanother)+" VULNERABILIDADES , EL NOMBRE INCLUYE UNA CADENA DISTINTA")
print("\n")
                                    





print("***************************PORCENTAJES NAME VULNERABILIDADES IBM PARTE SMART HOME***************************")
print("\n")                            
                
print("\n")
print(" DE UN TOTAL DE "+str(count_vulnibm_sh_names)+" VALORES DE NOMBRE :\n") 
print("\n")
print("   - LOS PORCENTAJES DE CADENAS DE TEXTO ENCONTRADAS EN EL VALOR DE NOMBRE DE OBJETO SON LOS SIGUIENTES:  \n")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_namepathtraversal*100)/count_vulnibm_sh_names)))+" % DE VULNERABILIDADES , EL NOMBRE INCLUYE PATH TRAVERSAL ")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_namedirectorytraversal*100)/count_vulnibm_sh_names)))+" % DE VULNERABILIDADES , EL NOMBRE INCLUYE DIRECTORY TRAVERSAL")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_nameprivilegeescalation*100)/count_vulnibm_sh_names)))+" % DE VULNERABILIDADES , EL NOMBRE INCLUYE PRIVILEGE ESCALATION ")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_namecrosssitescripting*100)/count_vulnibm_sh_names)))+" % DE VULNERABILIDADES , EL NOMBRE INCLUYE CROSS SITE SCRIPTING ")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_namesecuritybypass*100)/count_vulnibm_sh_names)))+" % DE VULNERABILIDADES , EL NOMBRE INCLUYE SECURITY BYPASS ")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_namesinformationdisclosure*100)/count_vulnibm_sh_names)))+" % DE VULNERABILIDADES , EL NOMBRE INCLUYE INFORMATION DISCLOSURE ")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_namecodeexecution*100)/count_vulnibm_sh_names)))+" % DE VULNERABILIDADES , EL NOMBRE INCLUYE CODE EXECUTION ")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_namemaninthemiddle*100)/count_vulnibm_sh_names)))+" % DE VULNERABILIDADES , EL NOMBRE INCLUYE MAN IN THE MIDDLE ")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_namesqlinjection*100)/count_vulnibm_sh_names)))+" % DE VULNERABILIDADES , EL NOMBRE INCLUYE SQL INJECTION")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_namecrosssiterequestforgery*100)/count_vulnibm_sh_names)))+" % DE VULNERABILIDADES , EL NOMBRE INCLUYE CROSS SITE REQUEST FORGERY ")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_namemoduleexecution*100)/count_vulnibm_sh_names)))+" % DE VULNERABILIDADES , EL NOMBRE INCLUYE MODULE EXECUTION")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_namebufferoverflow*100)/count_vulnibm_sh_names)))+" % DE VULNERABILIDADES , EL NOMBRE INCLUYE BUFFER OVERFLOW")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_namecommandexecution*100)/count_vulnibm_sh_names)))+" % DE VULNERABILIDADES , EL NOMBRE INCLUYE COMMAND EXECUTION")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_namespoofing*100)/count_vulnibm_sh_names)))+" % DE VULNERABILIDADES , EL NOMBRE INCLUYE SPOOFING")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_nameclickjacking*100)/count_vulnibm_sh_names)))+" % DE VULNERABILIDADES , EL NOMBRE INCLUYE CLICKJACKING")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_namehijacking*100)/count_vulnibm_sh_names)))+" % DE VULNERABILIDADES , EL NOMBRE INCLUYE HIJACKING")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_namefileinclude*100)/count_vulnibm_sh_names)))+" % DE VULNERABILIDADES , EL NOMBRE INCLUYE FILE INCLUDE")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_namebruteforce*100)/count_vulnibm_sh_names)))+" % DE VULNERABILIDADES , EL NOMBRE INCLUYE BRUTE FORCE")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_namefileupload*100)/count_vulnibm_sh_names)))+" % DE VULNERABILIDADES , EL NOMBRE INCLUYE FILE UPLOAD")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_nameheaderinjection*100)/count_vulnibm_sh_names)))+" % DE VULNERABILIDADES , EL NOMBRE INCLUYE HEADER INJECTION")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_nametampering*100)/count_vulnibm_sh_names)))+" % DE VULNERABILIDADES , EL NOMBRE INCLUYE TAMPERING")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_nameanother*100)/count_vulnibm_sh_names)))+" % DE VULNERABILIDADES , EL NOMBRE INCLUYE UN VALOR DISTINTO")
print("\n")
    

print("***************************ESTADÍSTICAS NOMBRE VULNERABILIDADES IBM PARTE IOT Y SMART HOME CONJUNTAS***************************")
print("\n")                            
                
print("\n")
print(" DE UN TOTAL DE "+str(count_vulnibm_sh_names+count_vulnibm_iot_names)+" VALORES DE NOMBRE :\n") 
print("\n")
print("   - LAS ESTADISTICAS DE CADENAS DE TEXTO ENCONTRADAS EN EL VALOR DE NOMBRE DE OBJETO SON LAS SIGUIENTES:  \n")
print("            -    EN  "+str(count_vulnibm_sh_namepathtraversal+count_vulnibm_iot_namepathtraversal)+" VULNERABILIDADES , EL NOMBRE INCLUYE PATH TRAVERSAL ")
print("            -    EN  "+str(count_vulnibm_sh_namedirectorytraversal+count_vulnibm_iot_namedirectorytraversal)+" VULNERABILIDADES , EL NOMBRE INCLUYE DIRECTORY TRAVERSAL")
print("            -    EN  "+str(count_vulnibm_sh_nameprivilegeescalation+count_vulnibm_iot_nameprivilegeescalation)+" VULNERABILIDADES , EL NOMBRE INCLUYE PRIVILEGE ESCALATION")
print("            -    EN  "+str(count_vulnibm_sh_namecrosssitescripting+count_vulnibm_iot_namecrosssitescripting)+" VULNERABILIDADES , EL NOMBRE INCLUYE CROSS SITE SCRIPTING ")
print("            -    EN  "+str(count_vulnibm_sh_namesecuritybypass+count_vulnibm_iot_namesecuritybypass)+" VULNERABILIDADES , EL NOMBRE INCLUYE SECURITY BYPASS ")
print("            -    EN  "+str(count_vulnibm_sh_namesinformationdisclosure+count_vulnibm_iot_namesinformationdisclosure)+" VULNERABILIDADES , EL NOMBRE INCLUYE INFORMATION DISCLOSURE")
print("            -    EN  "+str(count_vulnibm_sh_namedenialofservice+count_vulnibm_iot_namedenialofservice)+" VULNERABILIDADES , EL NOMBRE INCLUYE DENIAL OF SERVICE")
print("            -    EN  "+str(count_vulnibm_sh_namecodeexecution+count_vulnibm_iot_namecodeexecution)+" VULNERABILIDADES , EL NOMBRE INCLUYE CODE EXECUTION ")
print("            -    EN  "+str(count_vulnibm_sh_namemaninthemiddle+count_vulnibm_iot_namemaninthemiddle)+" VULNERABILIDADES , EL NOMBRE INCLUYE MAN IN THE MIDDLE ")
print("            -    EN  "+str(count_vulnibm_sh_namesqlinjection+count_vulnibm_iot_namesqlinjection)+" VULNERABILIDADES , EL NOMBRE INCLUYE SQL INJECTION")
print("            -    EN  "+str(count_vulnibm_sh_namecrosssiterequestforgery+count_vulnibm_iot_namecrosssiterequestforgery)+" VULNERABILIDADES , EL NOMBRE INCLUYE CROSS SITE REQUEST FORGERY")
print("            -    EN  "+str(count_vulnibm_sh_namemoduleexecution+count_vulnibm_iot_namemoduleexecution)+" VULNERABILIDADES , EL NOMBRE INCLUYE MODULE EXECUTION ")
print("            -    EN  "+str(count_vulnibm_sh_namebufferoverflow+count_vulnibm_iot_namebufferoverflow)+" VULNERABILIDADES , EL NOMBRE INCLUYE BUFFER OVERFLOW")
print("            -    EN  "+str(count_vulnibm_sh_namecommandexecution+count_vulnibm_iot_namecommandexecution)+" VULNERABILIDADES , EL NOMBRE INCLUYE COMMAND EXECUTION")
print("            -    EN  "+str(count_vulnibm_sh_namespoofing+count_vulnibm_iot_namespoofing)+" VULNERABILIDADES , EL NOMBRE INCLUYE SPOOFING")
print("            -    EN  "+str(count_vulnibm_sh_nameclickjacking+count_vulnibm_iot_nameclickjacking)+" VULNERABILIDADES , EL NOMBRE INCLUYE CLICKJACKING ")
print("            -    EN  "+str(count_vulnibm_sh_namehijacking+count_vulnibm_iot_namehijacking)+" VULNERABILIDADES , EL NOMBRE INCLUYE NAME HIJACKING")
print("            -    EN  "+str(count_vulnibm_sh_namefileinclude+count_vulnibm_iot_namefileinclude)+" VULNERABILIDADES , EL NOMBRE INCLUYE FILE INCLUDE")
print("            -    EN  "+str(count_vulnibm_sh_namebruteforce+count_vulnibm_iot_namebruteforce)+" VULNERABILIDADES , EL NOMBRE INCLUYE BRUTE FORCE")
print("            -    EN  "+str(count_vulnibm_sh_namefileupload+count_vulnibm_iot_namefileupload)+" VULNERABILIDADES , EL NOMBRE INCLUYE FILE UPLOAD ")
print("            -    EN  "+str(count_vulnibm_sh_nameheaderinjection+count_vulnibm_iot_nameheaderinjection)+" VULNERABILIDADES , EL NOMBRE INCLUYE HEADER INJECTION")
print("            -    EN  "+str(count_vulnibm_sh_nametampering+count_vulnibm_iot_nametampering)+" VULNERABILIDADES , EL NOMBRE INCLUYE TAMPERING")
print("            -    EN  "+str(count_vulnibm_sh_nameanother+count_vulnibm_iot_nameanother)+" VULNERABILIDADES , EL NOMBRE INCLUYE UNA CADENA DISTINTA")
print("\n")



















print("***************************PORCENTAJES NOMBRE VULNERABILIDADES IBM PARTE IOT Y SMART HOME CONJUNTAS***************************")
print("\n")                            
                
print("\n")
print(" DE UN TOTAL DE "+str(count_vulnibm_sh_names+count_vulnibm_iot_names)+" VALORES DE NOMBRE :\n") 
print("\n")
print("   - LOS PORCENTAJES DE CADENAS DE TEXTO ENCONTRADAS EN EL VALOR DE NOMBRE DE OBJETO SON LOS SIGUIENTES:  \n")
print("            -    EN EL  "+str(float((((count_vulnibm_sh_namepathtraversal+count_vulnibm_iot_namepathtraversal)*100)/(count_vulnibm_iot_names+count_vulnibm_sh_names))))+" % DE VULNERABILIDADES  EL NOMBRE INCLUYE PATH TRAVERSAL ")
print("            -    EN EL  "+str(float((((count_vulnibm_sh_namedirectorytraversal+count_vulnibm_iot_namedirectorytraversal)*100)/(count_vulnibm_iot_names+count_vulnibm_sh_names))))+" % DE VULNERABILIDADES  EL NOMBRE INCLUYE DIRECTORY TRAVERSAL ")
print("            -    EN EL  "+str(float((((count_vulnibm_sh_nameprivilegeescalation+count_vulnibm_iot_nameprivilegeescalation)*100)/(count_vulnibm_iot_names+count_vulnibm_sh_names))))+" % DE VULNERABILIDADES  EL NOMBRE INCLUYE PRIVILEGE ESCALATION ")
print("            -    EN EL  "+str(float((((count_vulnibm_sh_namecrosssitescripting+count_vulnibm_iot_namecrosssitescripting)*100)/(count_vulnibm_iot_names+count_vulnibm_sh_names))))+" % DE VULNERABILIDADES  EL NOMBRE INCLUYE CROSS SITE SCRIPTING ")
print("            -    EN EL  "+str(float((((count_vulnibm_sh_namesecuritybypass+count_vulnibm_iot_namesecuritybypass)*100)/(count_vulnibm_iot_names+count_vulnibm_sh_names))))+" % DE VULNERABILIDADES  EL NOMBRE INCLUYE SECURITY BYPASS ")
print("            -    EN EL  "+str(float((((count_vulnibm_sh_namesinformationdisclosure+count_vulnibm_iot_namesinformationdisclosure)*100)/(count_vulnibm_iot_names+count_vulnibm_sh_names))))+" % DE VULNERABILIDADES  EL NOMBRE INCLUYE INFORMATION DISCLOSURE ")
print("            -    EN EL  "+str(float((((count_vulnibm_sh_namecodeexecution+count_vulnibm_iot_namecodeexecution)*100)/(count_vulnibm_iot_names+count_vulnibm_sh_names))))+" % DE VULNERABILIDADES  EL NOMBRE INCLUYE CODE EXECUTION ")
print("            -    EN EL  "+str(float((((count_vulnibm_sh_namemaninthemiddle+count_vulnibm_iot_namemaninthemiddle)*100)/(count_vulnibm_iot_names+count_vulnibm_sh_names))))+" % DE VULNERABILIDADES  EL NOMBRE INCLUYE MAN IN THE MIDDLE ")
print("            -    EN EL  "+str(float((((count_vulnibm_sh_namesqlinjection+count_vulnibm_iot_namesqlinjection)*100)/(count_vulnibm_iot_names+count_vulnibm_sh_names))))+" % DE VULNERABILIDADES  EL NOMBRE INCLUYE SQL INJECTION ")
print("            -    EN EL  "+str(float((((count_vulnibm_sh_namecrosssiterequestforgery+count_vulnibm_iot_namecrosssiterequestforgery)*100)/(count_vulnibm_iot_names+count_vulnibm_sh_names))))+" % DE VULNERABILIDADES  EL NOMBRE INCLUYE CROSS SITE REQUEST FORGERY ")
print("            -    EN EL  "+str(float((((count_vulnibm_sh_namemoduleexecution+count_vulnibm_iot_namemoduleexecution)*100)/(count_vulnibm_iot_names+count_vulnibm_sh_names))))+" % DE VULNERABILIDADES  EL NOMBRE INCLUYE MODULE EXECUTION ")
print("            -    EN EL  "+str(float((((count_vulnibm_sh_namebufferoverflow+count_vulnibm_iot_namebufferoverflow)*100)/(count_vulnibm_iot_names+count_vulnibm_sh_names))))+" % DE VULNERABILIDADES  EL NOMBRE INCLUYE BUFFER OVERFLOW ")
print("            -    EN EL  "+str(float((((count_vulnibm_sh_namecommandexecution+count_vulnibm_iot_namecommandexecution)*100)/(count_vulnibm_iot_names+count_vulnibm_sh_names))))+" % DE VULNERABILIDADES  EL NOMBRE INCLUYE COMMAND EXECUTION ")
print("            -    EN EL  "+str(float((((count_vulnibm_sh_namespoofing+count_vulnibm_iot_namespoofing)*100)/(count_vulnibm_iot_names+count_vulnibm_sh_names))))+" % DE VULNERABILIDADES  EL NOMBRE INCLUYE SPOOFING ")
print("            -    EN EL  "+str(float((((count_vulnibm_sh_nameclickjacking+count_vulnibm_iot_nameclickjacking)*100)/(count_vulnibm_iot_names+count_vulnibm_sh_names))))+" % DE VULNERABILIDADES  EL NOMBRE INCLUYE CLICKJACKING")
print("            -    EN EL  "+str(float((((count_vulnibm_sh_namehijacking+count_vulnibm_iot_namehijacking)*100)/(count_vulnibm_iot_names+count_vulnibm_sh_names))))+" % DE VULNERABILIDADES  EL NOMBRE INCLUYE HIJACKING ")
print("            -    EN EL  "+str(float((((count_vulnibm_sh_namefileinclude+count_vulnibm_iot_namefileinclude)*100)/(count_vulnibm_iot_names+count_vulnibm_sh_names))))+" % DE VULNERABILIDADES  EL NOMBRE INCLUYE FILE INCLUDE ")
print("            -    EN EL  "+str(float((((count_vulnibm_sh_namebruteforce+count_vulnibm_iot_namebruteforce)*100)/(count_vulnibm_iot_names+count_vulnibm_sh_names))))+" % DE VULNERABILIDADES  EL NOMBRE INCLUYE BRUTE FORCE ")
print("            -    EN EL  "+str(float((((count_vulnibm_sh_namefileupload+count_vulnibm_iot_namefileupload)*100)/(count_vulnibm_iot_names+count_vulnibm_sh_names))))+" % DE VULNERABILIDADES  EL NOMBRE INCLUYE FILE UPLOAD ")
print("            -    EN EL  "+str(float((((count_vulnibm_sh_nameheaderinjection+count_vulnibm_iot_nameheaderinjection)*100)/(count_vulnibm_iot_names+count_vulnibm_sh_names))))+" % DE VULNERABILIDADES  EL NOMBRE INCLUYE HEADER INJECTION ")
print("            -    EN EL  "+str(float((((count_vulnibm_sh_nametampering+count_vulnibm_iot_nametampering)*100)/(count_vulnibm_iot_names+count_vulnibm_sh_names))))+" % DE VULNERABILIDADES  EL NOMBRE INCLUYE TAMPERING ")
print("            -    EN EL  "+str(float((((count_vulnibm_sh_nameanother+count_vulnibm_iot_nameanother)*100)/(count_vulnibm_iot_names+count_vulnibm_sh_names))))+" % DE VULNERABILIDADES  EL NOMBRE INCLUYE UN VALOR DISTINTO")
print("\n")