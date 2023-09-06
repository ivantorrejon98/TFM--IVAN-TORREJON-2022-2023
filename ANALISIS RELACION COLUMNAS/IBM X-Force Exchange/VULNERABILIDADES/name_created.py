







import pandas as pd
from datetime import datetime,timedelta



#Abro los ficheros con los que voy a tratar




df_vulnibm_iot = pd.read_excel('vulnerabilidades_ibm_iot_2023.xlsx')

#Variable que almacena el contador total de valores de nombres
count_vulnibm_iot_names=0
#Variable que almacena el contador total de valores distintos de nombres
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



#Variables que almacenan el valor concreto de nombre segun valor de fecha de creacion
count_vulnibm_iot_namepathtraversal_created2023=0
count_vulnibm_iot_namedirectorytraversal_created2023=0
count_vulnibm_iot_nameprivilegeescalation_created2023=0
count_vulnibm_iot_namecrosssitescripting_created2023=0
count_vulnibm_iot_namesecuritybypass_created2023=0
count_vulnibm_iot_namesinformationdisclosure_created2023=0
count_vulnibm_iot_namedenialofservice_created2023=0
count_vulnibm_iot_namecodeexecution_created2023=0
count_vulnibm_iot_namemaninthemiddle_created2023=0
count_vulnibm_iot_namesqlinjection_created2023=0
count_vulnibm_iot_namecrosssiterequestforgery_created2023=0
count_vulnibm_iot_namemoduleexecution_created2023=0
count_vulnibm_iot_namebufferoverflow_created2023=0
count_vulnibm_iot_namecommandexecution_created2023=0
count_vulnibm_iot_namespoofing_created2023=0
count_vulnibm_iot_nameclickjacking_created2023=0
count_vulnibm_iot_namehijacking_created2023=0
count_vulnibm_iot_namefileinclude_created2023=0
count_vulnibm_iot_namebruteforce_created2023=0
count_vulnibm_iot_namefileupload_created2023=0
count_vulnibm_iot_nameheaderinjection_created2023=0
count_vulnibm_iot_nametampering_created2023=0
count_vulnibm_iot_nameanother_created2023=0



count_vulnibm_iot_namepathtraversal_created2022=0
count_vulnibm_iot_namedirectorytraversal_created2022=0
count_vulnibm_iot_nameprivilegeescalation_created2022=0
count_vulnibm_iot_namecrosssitescripting_created2022=0
count_vulnibm_iot_namesecuritybypass_created2022=0
count_vulnibm_iot_namesinformationdisclosure_created2022=0
count_vulnibm_iot_namedenialofservice_created2022=0
count_vulnibm_iot_namecodeexecution_created2022=0
count_vulnibm_iot_namemaninthemiddle_created2022=0
count_vulnibm_iot_namesqlinjection_created2022=0
count_vulnibm_iot_namecrosssiterequestforgery_created2022=0
count_vulnibm_iot_namemoduleexecution_created2022=0
count_vulnibm_iot_namebufferoverflow_created2022=0
count_vulnibm_iot_namecommandexecution_created2022=0
count_vulnibm_iot_namespoofing_created2022=0
count_vulnibm_iot_nameclickjacking_created2022=0
count_vulnibm_iot_namehijacking_created2022=0
count_vulnibm_iot_namefileinclude_created2022=0
count_vulnibm_iot_namebruteforce_created2022=0
count_vulnibm_iot_namefileupload_created2022=0
count_vulnibm_iot_nameheaderinjection_created2022=0
count_vulnibm_iot_nametampering_created2022=0
count_vulnibm_iot_nameanother_created2022=0


count_vulnibm_iot_created2023=0
count_vulnibm_iot_created2022=0

count_vulnibm_iot_created=0


#Comprobamos el contenido de name
for r in range(0,len(df_vulnibm_iot["name"])):

     #Si el valor es unico y no un vector
        str_anio_createdate_vuln_ibm_iot=df_vulnibm_iot["created"][r].split("-")
        anio_createdate_vuln_ibm_iot=int(str_anio_createdate_vuln_ibm_iot[0])
        #Obtengo el anio de creacion
        if(anio_createdate_vuln_ibm_iot >= 2023):
            count_vulnibm_iot_created+=1
            count_vulnibm_iot_created2023+=1
            aux_str=df_vulnibm_iot["name"][r].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
            if(aux_str!='NONE'):
                count_vulnibm_iot_names+=1
                if('pathtraversal' in aux_str):
                    count_vulnibm_iot_namepathtraversal_created2023+=1
                elif('directorytraversal' in aux_str):
                    count_vulnibm_iot_namedirectorytraversal_created2023+=1
                elif('privilegeescalation' in aux_str):
                    count_vulnibm_iot_nameprivilegeescalation_created2023+=1
                elif('cross-sitescripting' in aux_str):
                    count_vulnibm_iot_namecrosssitescripting_created2023+=1                            
                elif('securitybypass' in aux_str):
                     count_vulnibm_iot_namesecuritybypass_created2023+=1                           
                elif('information_disclosure' in aux_str or 'informationdisclosure' in aux_str):
                     count_vulnibm_iot_namesinformationdisclosure_created2023+=1                           
                elif('denialofservice' in aux_str):
                     count_vulnibm_iot_namedenialofservice_created2023+=1                           
                elif('codeexecution' in aux_str):
                     count_vulnibm_iot_namecodeexecution_created2023+=1                           
                elif('maninthemiddle' in aux_str):
                     count_vulnibm_iot_namemaninthemiddle_created2023+=1                           
                elif('SQLinjection' in aux_str):
                     count_vulnibm_iot_namesqlinjection_created2023+=1                           
                elif('cross-siterequestforgery' in aux_str):
                     count_vulnibm_iot_namecrosssiterequestforgery_created2023+=1                           
                elif('moduleexecution' in aux_str):
                     count_vulnibm_iot_namemoduleexecution_created2023+=1                           
                elif('bufferoverflow' in aux_str):
                     count_vulnibm_iot_namebufferoverflow_created2023+=1                           
                elif('commandexecution' in aux_str):
                     count_vulnibm_iot_namecommandexecution_created2023+=1                           
                elif('spoofing' in aux_str):
                     count_vulnibm_iot_namespoofing_created2023+=1                           
                elif('clickjacking' in aux_str):
                     count_vulnibm_iot_nameclickjacking_created2023+=1
                elif('hijacking' in aux_str):
                      count_vulnibm_iot_namehijacking_created2023+=1
                elif('fileinclude' in aux_str):
                      count_vulnibm_iot_namefileinclude_created2023+=1
                elif('bruteforce' in aux_str):
                      count_vulnibm_iot_namebruteforce_created2023+=1
                elif('fileupload' in aux_str):
                      count_vulnibm_iot_namefileupload_created2023+=1
                elif('headerinjection' in aux_str):
                      count_vulnibm_iot_nameheaderinjection_created2023+=1
                elif('Tampering' in aux_str):
                       count_vulnibm_iot_nametampering_created2023+=1
                else:
                      count_vulnibm_iot_nameanother_created2023+=1   
            
        elif(anio_createdate_vuln_ibm_iot >= 2022):
            count_vulnibm_iot_created+=1
            count_vulnibm_iot_created2022+=1
            aux_str=df_vulnibm_iot["name"][r].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
            if(aux_str!='NONE'):
                count_vulnibm_iot_names+=1
                if('pathtraversal' in aux_str):
                    count_vulnibm_iot_namepathtraversal_created2022+=1
                elif('directorytraversal' in aux_str):
                    count_vulnibm_iot_namedirectorytraversal_created2022+=1
                elif('privilegeescalation' in aux_str):
                    count_vulnibm_iot_nameprivilegeescalation_created2022+=1
                elif('cross-sitescripting' in aux_str):
                    count_vulnibm_iot_namecrosssitescripting_created2022+=1                            
                elif('securitybypass' in aux_str):
                     count_vulnibm_iot_namesecuritybypass_created2022+=1                           
                elif('information_disclosure' in aux_str or 'informationdisclosure' in aux_str):
                     count_vulnibm_iot_namesinformationdisclosure_created2022+=1                           
                elif('denialofservice' in aux_str):
                     count_vulnibm_iot_namedenialofservice_created2022+=1                           
                elif('codeexecution' in aux_str):
                     count_vulnibm_iot_namecodeexecution_created2022+=1                           
                elif('maninthemiddle' in aux_str):
                     count_vulnibm_iot_namemaninthemiddle_created2022+=1                           
                elif('SQLinjection' in aux_str):
                     count_vulnibm_iot_namesqlinjection_created2022+=1                           
                elif('cross-siterequestforgery' in aux_str):
                     count_vulnibm_iot_namecrosssiterequestforgery_created2022+=1                           
                elif('moduleexecution' in aux_str):
                     count_vulnibm_iot_namemoduleexecution_created2022+=1                           
                elif('bufferoverflow' in aux_str):
                     count_vulnibm_iot_namebufferoverflow_created2022+=1                           
                elif('commandexecution' in aux_str):
                     count_vulnibm_iot_namecommandexecution_created2022+=1                           
                elif('spoofing' in aux_str):
                     count_vulnibm_iot_namespoofing_created2022+=1                           
                elif('clickjacking' in aux_str):
                     count_vulnibm_iot_nameclickjacking_created2022+=1
                elif('hijacking' in aux_str):
                      count_vulnibm_iot_namehijacking_created2022+=1
                elif('fileinclude' in aux_str):
                      count_vulnibm_iot_namefileinclude_created2022+=1
                elif('bruteforce' in aux_str):
                      count_vulnibm_iot_namebruteforce_created2022+=1
                elif('fileupload' in aux_str):
                      count_vulnibm_iot_namefileupload_created2022+=1
                elif('headerinjection' in aux_str):
                      count_vulnibm_iot_nameheaderinjection_created2022+=1
                elif('Tampering' in aux_str):
                       count_vulnibm_iot_nametampering_created2022+=1
                else:
                      count_vulnibm_iot_nameanother_created2022+=1
                  
        
            
print("*****************ESTADÍSTICAS FECHA DE CREACION/NOMBRE VULNERABILIDADES IBM PARTE IOT*****************")
print("\n")                            
                
print("\n")
print(" DE UN TOTAL DE "+str(count_vulnibm_iot_created)+" VULNERABILIDADES:\n") 
print("\n")
print("   - LAS ESTADISTICAS DE FECHA DE CREACION SON LAS SIGUIENTES:  \n")
print("      -    EN  "+str(count_vulnibm_iot_created2023)+" VULNERABILIDADES LA FECHA DE CREACION ES 2023. LAS ESTADÍSTICAS DE TIPO DE ATAQUE SEGUN EL VALOR DE NOMBRE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_namepathtraversal_created2023)+" VULNERABILIDADES , EL NOMBRE INCLUYE PATH TRAVERSAL ")
print("            -    EN  "+str(count_vulnibm_iot_namedirectorytraversal_created2023)+" VULNERABILIDADES , EL NOMBRE INCLUYE DIRECTORY TRAVERSAL")
print("            -    EN  "+str(count_vulnibm_iot_nameprivilegeescalation_created2023)+" VULNERABILIDADES , EL NOMBRE INCLUYE PRIVILEGE ESCALATION")
print("            -    EN  "+str(count_vulnibm_iot_namecrosssitescripting_created2023)+" VULNERABILIDADES , EL NOMBRE INCLUYE CROSS SITE SCRIPTING ")
print("            -    EN  "+str(count_vulnibm_iot_namesecuritybypass_created2023)+" VULNERABILIDADES , EL NOMBRE INCLUYE SECURITY BYPASS ")
print("            -    EN  "+str(count_vulnibm_iot_namesinformationdisclosure_created2023)+" VULNERABILIDADES , EL NOMBRE INCLUYE INFORMATION DISCLOSURE")
print("            -    EN  "+str(count_vulnibm_iot_namedenialofservice_created2023)+" VULNERABILIDADES , EL NOMBRE INCLUYE DENIAL OF SERVICE")
print("            -    EN  "+str(count_vulnibm_iot_namecodeexecution_created2023)+" VULNERABILIDADES , EL NOMBRE INCLUYE CODE EXECUTION ")
print("            -    EN  "+str(count_vulnibm_iot_namemaninthemiddle_created2023)+" VULNERABILIDADES , EL NOMBRE INCLUYE MAN IN THE MIDDLE ")
print("            -    EN  "+str(count_vulnibm_iot_namesqlinjection_created2023)+" VULNERABILIDADES , EL NOMBRE INCLUYE SQL INJECTION")
print("            -    EN  "+str(count_vulnibm_iot_namecrosssiterequestforgery_created2023)+" VULNERABILIDADES , EL NOMBRE INCLUYE CROSS SITE REQUEST FORGERY")
print("            -    EN  "+str(count_vulnibm_iot_namemoduleexecution_created2023)+" VULNERABILIDADES , EL NOMBRE INCLUYE MODULE EXECUTION ")
print("            -    EN  "+str(count_vulnibm_iot_namebufferoverflow_created2023)+" VULNERABILIDADES , EL NOMBRE INCLUYE BUFFER OVERFLOW")
print("            -    EN  "+str(count_vulnibm_iot_namecommandexecution_created2023)+" VULNERABILIDADES , EL NOMBRE INCLUYE COMMAND EXECUTION")
print("            -    EN  "+str(count_vulnibm_iot_namespoofing_created2023)+" VULNERABILIDADES , EL NOMBRE INCLUYE SPOOFING")
print("            -    EN  "+str(count_vulnibm_iot_nameclickjacking_created2023)+" VULNERABILIDADES , EL NOMBRE INCLUYE CLICKJACKING ")
print("            -    EN  "+str(count_vulnibm_iot_namehijacking_created2023)+" VULNERABILIDADES , EL NOMBRE INCLUYE NAME HIJACKING")
print("            -    EN  "+str(count_vulnibm_iot_namefileinclude_created2023)+" VULNERABILIDADES , EL NOMBRE INCLUYE FILE INCLUDE")
print("            -    EN  "+str(count_vulnibm_iot_namebruteforce_created2023)+" VULNERABILIDADES , EL NOMBRE INCLUYE BRUTE FORCE")
print("            -    EN  "+str(count_vulnibm_iot_namefileupload_created2023)+" VULNERABILIDADES , EL NOMBRE INCLUYE FILE UPLOAD ")
print("            -    EN  "+str(count_vulnibm_iot_nameheaderinjection_created2023)+" VULNERABILIDADES , EL NOMBRE INCLUYE HEADER INJECTION")
print("            -    EN  "+str(count_vulnibm_iot_nametampering_created2023)+" VULNERABILIDADES , EL NOMBRE INCLUYE TAMPERING")
print("            -    EN  "+str(count_vulnibm_iot_nameanother_created2023)+" VULNERABILIDADES , EL NOMBRE INCLUYE UN NOMBRE DISTINTO")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_created2022)+" VULNERABILIDADES LA FECHA DE CREACION ES 2022. LAS ESTADÍSTICAS DE TIPO DE ATAQUE SEGUN EL VALOR DE NOMBRE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_namepathtraversal_created2022)+" VULNERABILIDADES , EL NOMBRE INCLUYE PATH TRAVERSAL ")
print("            -    EN  "+str(count_vulnibm_iot_namedirectorytraversal_created2022)+" VULNERABILIDADES , EL NOMBRE INCLUYE DIRECTORY TRAVERSAL")
print("            -    EN  "+str(count_vulnibm_iot_nameprivilegeescalation_created2022)+" VULNERABILIDADES , EL NOMBRE INCLUYE PRIVILEGE ESCALATION")
print("            -    EN  "+str(count_vulnibm_iot_namecrosssitescripting_created2022)+" VULNERABILIDADES , EL NOMBRE INCLUYE CROSS SITE SCRIPTING ")
print("            -    EN  "+str(count_vulnibm_iot_namesecuritybypass_created2022)+" VULNERABILIDADES , EL NOMBRE INCLUYE SECURITY BYPASS ")
print("            -    EN  "+str(count_vulnibm_iot_namesinformationdisclosure_created2022)+" VULNERABILIDADES , EL NOMBRE INCLUYE INFORMATION DISCLOSURE")
print("            -    EN  "+str(count_vulnibm_iot_namedenialofservice_created2022)+" VULNERABILIDADES , EL NOMBRE INCLUYE DENIAL OF SERVICE")
print("            -    EN  "+str(count_vulnibm_iot_namecodeexecution_created2022)+" VULNERABILIDADES , EL NOMBRE INCLUYE CODE EXECUTION ")
print("            -    EN  "+str(count_vulnibm_iot_namemaninthemiddle_created2022)+" VULNERABILIDADES , EL NOMBRE INCLUYE MAN IN THE MIDDLE ")
print("            -    EN  "+str(count_vulnibm_iot_namesqlinjection_created2022)+" VULNERABILIDADES , EL NOMBRE INCLUYE SQL INJECTION")
print("            -    EN  "+str(count_vulnibm_iot_namecrosssiterequestforgery_created2022)+" VULNERABILIDADES , EL NOMBRE INCLUYE CROSS SITE REQUEST FORGERY")
print("            -    EN  "+str(count_vulnibm_iot_namemoduleexecution_created2022)+" VULNERABILIDADES , EL NOMBRE INCLUYE MODULE EXECUTION ")
print("            -    EN  "+str(count_vulnibm_iot_namebufferoverflow_created2022)+" VULNERABILIDADES , EL NOMBRE INCLUYE BUFFER OVERFLOW")
print("            -    EN  "+str(count_vulnibm_iot_namecommandexecution_created2022)+" VULNERABILIDADES , EL NOMBRE INCLUYE COMMAND EXECUTION")
print("            -    EN  "+str(count_vulnibm_iot_namespoofing_created2022)+" VULNERABILIDADES , EL NOMBRE INCLUYE SPOOFING")
print("            -    EN  "+str(count_vulnibm_iot_nameclickjacking_created2022)+" VULNERABILIDADES , EL NOMBRE INCLUYE CLICKJACKING ")
print("            -    EN  "+str(count_vulnibm_iot_namehijacking_created2022)+" VULNERABILIDADES , EL NOMBRE INCLUYE NAME HIJACKING")
print("            -    EN  "+str(count_vulnibm_iot_namefileinclude_created2022)+" VULNERABILIDADES , EL NOMBRE INCLUYE FILE INCLUDE")
print("            -    EN  "+str(count_vulnibm_iot_namebruteforce_created2022)+" VULNERABILIDADES , EL NOMBRE INCLUYE BRUTE FORCE")
print("            -    EN  "+str(count_vulnibm_iot_namefileupload_created2022)+" VULNERABILIDADES , EL NOMBRE INCLUYE FILE UPLOAD ")
print("            -    EN  "+str(count_vulnibm_iot_nameheaderinjection_created2022)+" VULNERABILIDADES , EL NOMBRE INCLUYE HEADER INJECTION")
print("            -    EN  "+str(count_vulnibm_iot_nametampering_created2022)+" VULNERABILIDADES , EL NOMBRE INCLUYE TAMPERING")
print("            -    EN  "+str(count_vulnibm_iot_nameanother_created2022)+" VULNERABILIDADES , EL NOMBRE INCLUYE UN NOMBRE DISTINTO")
print("\n")

print("*****************PORCENTAJE FECHA DE CREACION/NOMBRE VULNERABILIDADES IBM PARTE IOT*****************")
print("\n")                            
                
print("\n")
print(" DE UN TOTAL DE "+str(count_vulnibm_iot_created)+" VULNERABILIDADES :\n") 
print("\n")
print("   - LOS PORCENTAJES DE FECHA DE CREACION SON LOS SIGUIENTES:  \n")
if(count_vulnibm_iot_created2023>0): 
    print("      -    EN EL  "+str(float(((count_vulnibm_iot_created2023*100)/count_vulnibm_iot_created)))+" % DE VULNERABILIDADES LA FECHA DE CREACION ES 2023. LOS PORCENTAJES DE FECHA DE MODIFICACION SON LOS SIGUIENTES :  \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_namepathtraversal_created2023*100)/count_vulnibm_iot_created2023)))+" % DE VULNERABILIDADES CREADAS EN 2023 , EL NOMBRE INCLUYE PATH TRAVERSAL ")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_namedirectorytraversal_created2023*100)/count_vulnibm_iot_created2023)))+" % DE VULNERABILIDADES CREADAS EN 2023 , EL NOMBRE INCLUYE DIRECTORY TRAVERSAL")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_nameprivilegeescalation_created2023*100)/count_vulnibm_iot_created2023)))+" % DE VULNERABILIDADES CREADAS EN 2023 , EL NOMBRE INCLUYE PRIVILEGE ESCALATION ")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_namecrosssitescripting_created2023*100)/count_vulnibm_iot_created2023)))+" % DE VULNERABILIDADES CREADAS EN 2023 , EL NOMBRE INCLUYE CROSS SITE SCRIPTING ")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_namesecuritybypass_created2023*100)/count_vulnibm_iot_created2023)))+" % DE VULNERABILIDADES CREADAS EN 2023 , EL NOMBRE INCLUYE SECURITY BYPASS ")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_namesinformationdisclosure_created2023*100)/count_vulnibm_iot_created2023)))+" % DE VULNERABILIDADES CREADAS EN 2023 , EL NOMBRE INCLUYE INFORMATION DISCLOSURE ")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_namecodeexecution_created2023*100)/count_vulnibm_iot_created2023)))+" % DE VULNERABILIDADES CREADAS EN 2023 , EL NOMBRE INCLUYE CODE EXECUTION ")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_namemaninthemiddle_created2023*100)/count_vulnibm_iot_created2023)))+" % DE VULNERABILIDADES CREADAS EN 2023 , EL NOMBRE INCLUYE MAN IN THE MIDDLE ")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_namesqlinjection_created2023*100)/count_vulnibm_iot_created2023)))+" % DE VULNERABILIDADES CREADAS EN 2023 , EL NOMBRE INCLUYE SQL INJECTION")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_namecrosssiterequestforgery_created2023*100)/count_vulnibm_iot_created2023)))+" % DE VULNERABILIDADES CREADAS EN 2023 , EL NOMBRE INCLUYE CROSS SITE REQUEST FORGERY ")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_namemoduleexecution_created2023*100)/count_vulnibm_iot_created2023)))+" % DE VULNERABILIDADES CREADAS EN 2023 , EL NOMBRE INCLUYE MODULE EXECUTION")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_namebufferoverflow_created2023*100)/count_vulnibm_iot_created2023)))+" % DE VULNERABILIDADES CREADAS EN 2023 , EL NOMBRE INCLUYE BUFFER OVERFLOW")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_namecommandexecution_created2023*100)/count_vulnibm_iot_created2023)))+" % DE VULNERABILIDADES CREADAS EN 2023 , EL NOMBRE INCLUYE COMMAND EXECUTION")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_namespoofing_created2023*100)/count_vulnibm_iot_created2023)))+" % DE VULNERABILIDADES CREADAS EN 2023 , EL NOMBRE INCLUYE SPOOFING")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_nameclickjacking_created2023*100)/count_vulnibm_iot_created2023)))+" % DE VULNERABILIDADES CREADAS EN 2023 , EL NOMBRE INCLUYE CLICKJACKING")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_namehijacking_created2023*100)/count_vulnibm_iot_created2023)))+" % DE VULNERABILIDADES CREADAS EN 2023 , EL NOMBRE INCLUYE HIJACKING")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_namefileinclude_created2023*100)/count_vulnibm_iot_created2023)))+" % DE VULNERABILIDADES CREADAS EN 2023 , EL NOMBRE INCLUYE FILE INCLUDE")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_namebruteforce_created2023*100)/count_vulnibm_iot_created2023)))+" % DE VULNERABILIDADES CREADAS EN 2023 , EL NOMBRE INCLUYE BRUTE FORCE")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_namefileupload_created2023*100)/count_vulnibm_iot_created2023)))+" % DE VULNERABILIDADES CREADAS EN 2023 , EL NOMBRE INCLUYE FILE UPLOAD")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_nameheaderinjection_created2023*100)/count_vulnibm_iot_created2023)))+" % DE VULNERABILIDADES CREADAS EN 2023 , EL NOMBRE INCLUYE HEADER INJECTION")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_nametampering_created2023*100)/count_vulnibm_iot_created2023)))+" % DE VULNERABILIDADES CREADAS EN 2023 , EL NOMBRE INCLUYE TAMPERING")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_nameanother_created2023*100)/count_vulnibm_iot_created2023)))+" % DE VULNERABILIDADES CREADAS EN 2023 , EL NOMBRE INCLUYE UN VALOR DISTINTO")
    print("\n")
if(count_vulnibm_iot_created2022>0): 
    print("      -    EN EL  "+str(float(((count_vulnibm_iot_created2022*100)/count_vulnibm_iot_created)))+" % DE VULNERABILIDADES LA FECHA DE CREACION ES 2022. LOS PORCENTAJES DE FECHA DE MODIFICACION SON LOS SIGUIENTES :  \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_namepathtraversal_created2022*100)/count_vulnibm_iot_created2022)))+" % DE VULNERABILIDADES CREADAS EN 2022 , EL NOMBRE INCLUYE PATH TRAVERSAL ")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_namedirectorytraversal_created2022*100)/count_vulnibm_iot_created2022)))+" % DE VULNERABILIDADES CREADAS EN 2022 , EL NOMBRE INCLUYE DIRECTORY TRAVERSAL")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_nameprivilegeescalation_created2022*100)/count_vulnibm_iot_created2022)))+" % DE VULNERABILIDADES CREADAS EN 2022 , EL NOMBRE INCLUYE PRIVILEGE ESCALATION ")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_namecrosssitescripting_created2022*100)/count_vulnibm_iot_created2022)))+" % DE VULNERABILIDADES CREADAS EN 2022 , EL NOMBRE INCLUYE CROSS SITE SCRIPTING ")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_namesecuritybypass_created2022*100)/count_vulnibm_iot_created2022)))+" % DE VULNERABILIDADES CREADAS EN 2022 , EL NOMBRE INCLUYE SECURITY BYPASS ")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_namesinformationdisclosure_created2022*100)/count_vulnibm_iot_created2022)))+" % DE VULNERABILIDADES CREADAS EN 2022 , EL NOMBRE INCLUYE INFORMATION DISCLOSURE ")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_namecodeexecution_created2022*100)/count_vulnibm_iot_created2022)))+" % DE VULNERABILIDADES CREADAS EN 2022 , EL NOMBRE INCLUYE CODE EXECUTION ")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_namemaninthemiddle_created2022*100)/count_vulnibm_iot_created2022)))+" % DE VULNERABILIDADES CREADAS EN 2022 , EL NOMBRE INCLUYE MAN IN THE MIDDLE ")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_namesqlinjection_created2022*100)/count_vulnibm_iot_created2022)))+" % DE VULNERABILIDADES CREADAS EN 2022 , EL NOMBRE INCLUYE SQL INJECTION")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_namecrosssiterequestforgery_created2022*100)/count_vulnibm_iot_created2022)))+" % DE VULNERABILIDADES CREADAS EN 2022 , EL NOMBRE INCLUYE CROSS SITE REQUEST FORGERY ")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_namemoduleexecution_created2022*100)/count_vulnibm_iot_created2022)))+" % DE VULNERABILIDADES CREADAS EN 2022 , EL NOMBRE INCLUYE MODULE EXECUTION")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_namebufferoverflow_created2022*100)/count_vulnibm_iot_created2022)))+" % DE VULNERABILIDADES CREADAS EN 2022 , EL NOMBRE INCLUYE BUFFER OVERFLOW")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_namecommandexecution_created2022*100)/count_vulnibm_iot_created2022)))+" % DE VULNERABILIDADES CREADAS EN 2022 , EL NOMBRE INCLUYE COMMAND EXECUTION")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_namespoofing_created2022*100)/count_vulnibm_iot_created2022)))+" % DE VULNERABILIDADES CREADAS EN 2022 , EL NOMBRE INCLUYE SPOOFING")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_nameclickjacking_created2022*100)/count_vulnibm_iot_created2022)))+" % DE VULNERABILIDADES CREADAS EN 2022 , EL NOMBRE INCLUYE CLICKJACKING")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_namehijacking_created2022*100)/count_vulnibm_iot_created2022)))+" % DE VULNERABILIDADES CREADAS EN 2022 , EL NOMBRE INCLUYE HIJACKING")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_namefileinclude_created2022*100)/count_vulnibm_iot_created2022)))+" % DE VULNERABILIDADES CREADAS EN 2022 , EL NOMBRE INCLUYE FILE INCLUDE")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_namebruteforce_created2022*100)/count_vulnibm_iot_created2022)))+" % DE VULNERABILIDADES CREADAS EN 2022 , EL NOMBRE INCLUYE BRUTE FORCE")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_namefileupload_created2022*100)/count_vulnibm_iot_created2022)))+" % DE VULNERABILIDADES CREADAS EN 2022 , EL NOMBRE INCLUYE FILE UPLOAD")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_nameheaderinjection_created2022*100)/count_vulnibm_iot_created2022)))+" % DE VULNERABILIDADES CREADAS EN 2022 , EL NOMBRE INCLUYE HEADER INJECTION")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_nametampering_created2022*100)/count_vulnibm_iot_created2022)))+" % DE VULNERABILIDADES CREADAS EN 2022 , EL NOMBRE INCLUYE TAMPERING")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_nameanother_created2022*100)/count_vulnibm_iot_created2022)))+" % DE VULNERABILIDADES CREADAS EN 2022 , EL NOMBRE INCLUYE UN VALOR DISTINTO")
    print("\n")

#Abro los ficheros con los que voy a tratar




df_vulnibm_sh = pd.read_excel('vulnerabilidades_ibm_smart_home_2023.xlsx')
#Variable que almacena el contador total de valores de nombres
count_vulnibm_sh_names=0
#Variable que almacena el contador total de valores distintos de nombres
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



#Variables que almacenan el valor concreto de nombre segun valor de fecha de creacion
count_vulnibm_sh_namepathtraversal_created2023=0
count_vulnibm_sh_namedirectorytraversal_created2023=0
count_vulnibm_sh_nameprivilegeescalation_created2023=0
count_vulnibm_sh_namecrosssitescripting_created2023=0
count_vulnibm_sh_namesecuritybypass_created2023=0
count_vulnibm_sh_namesinformationdisclosure_created2023=0
count_vulnibm_sh_namedenialofservice_created2023=0
count_vulnibm_sh_namecodeexecution_created2023=0
count_vulnibm_sh_namemaninthemiddle_created2023=0
count_vulnibm_sh_namesqlinjection_created2023=0
count_vulnibm_sh_namecrosssiterequestforgery_created2023=0
count_vulnibm_sh_namemoduleexecution_created2023=0
count_vulnibm_sh_namebufferoverflow_created2023=0
count_vulnibm_sh_namecommandexecution_created2023=0
count_vulnibm_sh_namespoofing_created2023=0
count_vulnibm_sh_nameclickjacking_created2023=0
count_vulnibm_sh_namehijacking_created2023=0
count_vulnibm_sh_namefileinclude_created2023=0
count_vulnibm_sh_namebruteforce_created2023=0
count_vulnibm_sh_namefileupload_created2023=0
count_vulnibm_sh_nameheaderinjection_created2023=0
count_vulnibm_sh_nametampering_created2023=0
count_vulnibm_sh_nameanother_created2023=0



count_vulnibm_sh_namepathtraversal_created2022=0
count_vulnibm_sh_namedirectorytraversal_created2022=0
count_vulnibm_sh_nameprivilegeescalation_created2022=0
count_vulnibm_sh_namecrosssitescripting_created2022=0
count_vulnibm_sh_namesecuritybypass_created2022=0
count_vulnibm_sh_namesinformationdisclosure_created2022=0
count_vulnibm_sh_namedenialofservice_created2022=0
count_vulnibm_sh_namecodeexecution_created2022=0
count_vulnibm_sh_namemaninthemiddle_created2022=0
count_vulnibm_sh_namesqlinjection_created2022=0
count_vulnibm_sh_namecrosssiterequestforgery_created2022=0
count_vulnibm_sh_namemoduleexecution_created2022=0
count_vulnibm_sh_namebufferoverflow_created2022=0
count_vulnibm_sh_namecommandexecution_created2022=0
count_vulnibm_sh_namespoofing_created2022=0
count_vulnibm_sh_nameclickjacking_created2022=0
count_vulnibm_sh_namehijacking_created2022=0
count_vulnibm_sh_namefileinclude_created2022=0
count_vulnibm_sh_namebruteforce_created2022=0
count_vulnibm_sh_namefileupload_created2022=0
count_vulnibm_sh_nameheaderinjection_created2022=0
count_vulnibm_sh_nametampering_created2022=0
count_vulnibm_sh_nameanother_created2022=0

count_vulnibm_sh_created2023=0
count_vulnibm_sh_created2022=0
count_vulnibm_sh_created=0


#Comprobamos el contenido de name
for r in range(0,len(df_vulnibm_sh["name"])):

     #Si el valor es unico y no un vector
        str_anio_createdate_vuln_ibm_sh=df_vulnibm_sh["created"][r].split("-")
        anio_createdate_vuln_ibm_sh=int(str_anio_createdate_vuln_ibm_sh[0])
        #Obtengo el anio de creacion
        if(anio_createdate_vuln_ibm_sh >= 2023):
            count_vulnibm_sh_created+=1
            count_vulnibm_sh_created2023+=1
            aux_str=df_vulnibm_sh["name"][r].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
            if(aux_str!='NONE'):
                count_vulnibm_sh_names+=1
                if('pathtraversal' in aux_str):
                    count_vulnibm_sh_namepathtraversal_created2023+=1
                elif('directorytraversal' in aux_str):
                    count_vulnibm_sh_namedirectorytraversal_created2023+=1
                elif('privilegeescalation' in aux_str):
                    count_vulnibm_sh_nameprivilegeescalation_created2023+=1
                elif('cross-sitescripting' in aux_str):
                    count_vulnibm_sh_namecrosssitescripting_created2023+=1                            
                elif('securitybypass' in aux_str):
                     count_vulnibm_sh_namesecuritybypass_created2023+=1                           
                elif('information_disclosure' in aux_str or 'informationdisclosure' in aux_str):
                     count_vulnibm_sh_namesinformationdisclosure_created2023+=1                           
                elif('denialofservice' in aux_str):
                     count_vulnibm_sh_namedenialofservice_created2023+=1                           
                elif('codeexecution' in aux_str):
                     count_vulnibm_sh_namecodeexecution_created2023+=1                           
                elif('maninthemiddle' in aux_str):
                     count_vulnibm_sh_namemaninthemiddle_created2023+=1                           
                elif('SQLinjection' in aux_str):
                     count_vulnibm_sh_namesqlinjection_created2023+=1                           
                elif('cross-siterequestforgery' in aux_str):
                     count_vulnibm_sh_namecrosssiterequestforgery_created2023+=1                           
                elif('moduleexecution' in aux_str):
                     count_vulnibm_sh_namemoduleexecution_created2023+=1                           
                elif('bufferoverflow' in aux_str):
                     count_vulnibm_sh_namebufferoverflow_created2023+=1                           
                elif('commandexecution' in aux_str):
                     count_vulnibm_sh_namecommandexecution_created2023+=1                           
                elif('spoofing' in aux_str):
                     count_vulnibm_sh_namespoofing_created2023+=1                           
                elif('clickjacking' in aux_str):
                     count_vulnibm_sh_nameclickjacking_created2023+=1
                elif('hijacking' in aux_str):
                      count_vulnibm_sh_namehijacking_created2023+=1
                elif('fileinclude' in aux_str):
                      count_vulnibm_sh_namefileinclude_created2023+=1
                elif('bruteforce' in aux_str):
                      count_vulnibm_sh_namebruteforce_created2023+=1
                elif('fileupload' in aux_str):
                      count_vulnibm_sh_namefileupload_created2023+=1
                elif('headerinjection' in aux_str):
                      count_vulnibm_sh_nameheaderinjection_created2023+=1
                elif('Tampering' in aux_str):
                       count_vulnibm_sh_nametampering_created2023+=1
                else:
                      count_vulnibm_sh_nameanother_created2023+=1   
            
        elif(anio_createdate_vuln_ibm_sh >= 2022):
            count_vulnibm_sh_created+=1
            count_vulnibm_sh_created2022+=1
            aux_str=df_vulnibm_sh["name"][r].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
            if(aux_str!='NONE'):
                count_vulnibm_sh_names+=1
                if('pathtraversal' in aux_str):
                    count_vulnibm_sh_namepathtraversal_created2022+=1
                elif('directorytraversal' in aux_str):
                    count_vulnibm_sh_namedirectorytraversal_created2022+=1
                elif('privilegeescalation' in aux_str):
                    count_vulnibm_sh_nameprivilegeescalation_created2022+=1
                elif('cross-sitescripting' in aux_str):
                    count_vulnibm_sh_namecrosssitescripting_created2022+=1                            
                elif('securitybypass' in aux_str):
                     count_vulnibm_sh_namesecuritybypass_created2022+=1                           
                elif('information_disclosure' in aux_str or 'informationdisclosure' in aux_str):
                     count_vulnibm_sh_namesinformationdisclosure_created2022+=1                           
                elif('denialofservice' in aux_str):
                     count_vulnibm_sh_namedenialofservice_created2022+=1                           
                elif('codeexecution' in aux_str):
                     count_vulnibm_sh_namecodeexecution_created2022+=1                           
                elif('maninthemiddle' in aux_str):
                     count_vulnibm_sh_namemaninthemiddle_created2022+=1                           
                elif('SQLinjection' in aux_str):
                     count_vulnibm_sh_namesqlinjection_created2022+=1                           
                elif('cross-siterequestforgery' in aux_str):
                     count_vulnibm_sh_namecrosssiterequestforgery_created2022+=1                           
                elif('moduleexecution' in aux_str):
                     count_vulnibm_sh_namemoduleexecution_created2022+=1                           
                elif('bufferoverflow' in aux_str):
                     count_vulnibm_sh_namebufferoverflow_created2022+=1                           
                elif('commandexecution' in aux_str):
                     count_vulnibm_sh_namecommandexecution_created2022+=1                           
                elif('spoofing' in aux_str):
                     count_vulnibm_sh_namespoofing_created2022+=1                           
                elif('clickjacking' in aux_str):
                     count_vulnibm_sh_nameclickjacking_created2022+=1
                elif('hijacking' in aux_str):
                      count_vulnibm_sh_namehijacking_created2022+=1
                elif('fileinclude' in aux_str):
                      count_vulnibm_sh_namefileinclude_created2022+=1
                elif('bruteforce' in aux_str):
                      count_vulnibm_sh_namebruteforce_created2022+=1
                elif('fileupload' in aux_str):
                      count_vulnibm_sh_namefileupload_created2022+=1
                elif('headerinjection' in aux_str):
                      count_vulnibm_sh_nameheaderinjection_created2022+=1
                elif('Tampering' in aux_str):
                       count_vulnibm_sh_nametampering_created2022+=1
                else:
                      count_vulnibm_sh_nameanother_created2022+=1
                  
        

print("*****************ESTADÍSTICAS FECHA DE CREACION/NOMBRE VULNERABILIDADES IBM PARTE SMART HOME*****************")
print("\n")                            
                
print("\n")
print(" DE UN TOTAL DE "+str(count_vulnibm_sh_created)+" VULNERABILIDADES:\n") 
print("\n")
print("   - LAS ESTADISTICAS DE FECHA DE CREACION SON LAS SIGUIENTES:  \n")
print("      -    EN  "+str(count_vulnibm_sh_created2023)+" VULNERABILIDADES LA FECHA DE CREACION ES 2023. LAS ESTADÍSTICAS DE TIPO DE ATAQUE SEGUN EL VALOR DE NOMBRE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_sh_namepathtraversal_created2023)+" VULNERABILIDADES , EL NOMBRE INCLUYE PATH TRAVERSAL ")
print("            -    EN  "+str(count_vulnibm_sh_namedirectorytraversal_created2023)+" VULNERABILIDADES , EL NOMBRE INCLUYE DIRECTORY TRAVERSAL")
print("            -    EN  "+str(count_vulnibm_sh_nameprivilegeescalation_created2023)+" VULNERABILIDADES , EL NOMBRE INCLUYE PRIVILEGE ESCALATION")
print("            -    EN  "+str(count_vulnibm_sh_namecrosssitescripting_created2023)+" VULNERABILIDADES , EL NOMBRE INCLUYE CROSS SITE SCRIPTING ")
print("            -    EN  "+str(count_vulnibm_sh_namesecuritybypass_created2023)+" VULNERABILIDADES , EL NOMBRE INCLUYE SECURITY BYPASS ")
print("            -    EN  "+str(count_vulnibm_sh_namesinformationdisclosure_created2023)+" VULNERABILIDADES , EL NOMBRE INCLUYE INFORMATION DISCLOSURE")
print("            -    EN  "+str(count_vulnibm_sh_namedenialofservice_created2023)+" VULNERABILIDADES , EL NOMBRE INCLUYE DENIAL OF SERVICE")
print("            -    EN  "+str(count_vulnibm_sh_namecodeexecution_created2023)+" VULNERABILIDADES , EL NOMBRE INCLUYE CODE EXECUTION ")
print("            -    EN  "+str(count_vulnibm_sh_namemaninthemiddle_created2023)+" VULNERABILIDADES , EL NOMBRE INCLUYE MAN IN THE MIDDLE ")
print("            -    EN  "+str(count_vulnibm_sh_namesqlinjection_created2023)+" VULNERABILIDADES , EL NOMBRE INCLUYE SQL INJECTION")
print("            -    EN  "+str(count_vulnibm_sh_namecrosssiterequestforgery_created2023)+" VULNERABILIDADES , EL NOMBRE INCLUYE CROSS SITE REQUEST FORGERY")
print("            -    EN  "+str(count_vulnibm_sh_namemoduleexecution_created2023)+" VULNERABILIDADES , EL NOMBRE INCLUYE MODULE EXECUTION ")
print("            -    EN  "+str(count_vulnibm_sh_namebufferoverflow_created2023)+" VULNERABILIDADES , EL NOMBRE INCLUYE BUFFER OVERFLOW")
print("            -    EN  "+str(count_vulnibm_sh_namecommandexecution_created2023)+" VULNERABILIDADES , EL NOMBRE INCLUYE COMMAND EXECUTION")
print("            -    EN  "+str(count_vulnibm_sh_namespoofing_created2023)+" VULNERABILIDADES , EL NOMBRE INCLUYE SPOOFING")
print("            -    EN  "+str(count_vulnibm_sh_nameclickjacking_created2023)+" VULNERABILIDADES , EL NOMBRE INCLUYE CLICKJACKING ")
print("            -    EN  "+str(count_vulnibm_sh_namehijacking_created2023)+" VULNERABILIDADES , EL NOMBRE INCLUYE NAME HIJACKING")
print("            -    EN  "+str(count_vulnibm_sh_namefileinclude_created2023)+" VULNERABILIDADES , EL NOMBRE INCLUYE FILE INCLUDE")
print("            -    EN  "+str(count_vulnibm_sh_namebruteforce_created2023)+" VULNERABILIDADES , EL NOMBRE INCLUYE BRUTE FORCE")
print("            -    EN  "+str(count_vulnibm_sh_namefileupload_created2023)+" VULNERABILIDADES , EL NOMBRE INCLUYE FILE UPLOAD ")
print("            -    EN  "+str(count_vulnibm_sh_nameheaderinjection_created2023)+" VULNERABILIDADES , EL NOMBRE INCLUYE HEADER INJECTION")
print("            -    EN  "+str(count_vulnibm_sh_nametampering_created2023)+" VULNERABILIDADES , EL NOMBRE INCLUYE TAMPERING")
print("            -    EN  "+str(count_vulnibm_sh_nameanother_created2023)+" VULNERABILIDADES , EL NOMBRE INCLUYE UN NOMBRE DISTINTO")
print("\n")
print("      -    EN  "+str(count_vulnibm_sh_created2022)+" VULNERABILIDADES LA FECHA DE CREACION ES 2022. LAS ESTADÍSTICAS DE TIPO DE ATAQUE SEGUN EL VALOR DE NOMBRE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_sh_namepathtraversal_created2022)+" VULNERABILIDADES , EL NOMBRE INCLUYE PATH TRAVERSAL ")
print("            -    EN  "+str(count_vulnibm_sh_namedirectorytraversal_created2022)+" VULNERABILIDADES , EL NOMBRE INCLUYE DIRECTORY TRAVERSAL")
print("            -    EN  "+str(count_vulnibm_sh_nameprivilegeescalation_created2022)+" VULNERABILIDADES , EL NOMBRE INCLUYE PRIVILEGE ESCALATION")
print("            -    EN  "+str(count_vulnibm_sh_namecrosssitescripting_created2022)+" VULNERABILIDADES , EL NOMBRE INCLUYE CROSS SITE SCRIPTING ")
print("            -    EN  "+str(count_vulnibm_sh_namesecuritybypass_created2022)+" VULNERABILIDADES , EL NOMBRE INCLUYE SECURITY BYPASS ")
print("            -    EN  "+str(count_vulnibm_sh_namesinformationdisclosure_created2022)+" VULNERABILIDADES , EL NOMBRE INCLUYE INFORMATION DISCLOSURE")
print("            -    EN  "+str(count_vulnibm_sh_namedenialofservice_created2022)+" VULNERABILIDADES , EL NOMBRE INCLUYE DENIAL OF SERVICE")
print("            -    EN  "+str(count_vulnibm_sh_namecodeexecution_created2022)+" VULNERABILIDADES , EL NOMBRE INCLUYE CODE EXECUTION ")
print("            -    EN  "+str(count_vulnibm_sh_namemaninthemiddle_created2022)+" VULNERABILIDADES , EL NOMBRE INCLUYE MAN IN THE MIDDLE ")
print("            -    EN  "+str(count_vulnibm_sh_namesqlinjection_created2022)+" VULNERABILIDADES , EL NOMBRE INCLUYE SQL INJECTION")
print("            -    EN  "+str(count_vulnibm_sh_namecrosssiterequestforgery_created2022)+" VULNERABILIDADES , EL NOMBRE INCLUYE CROSS SITE REQUEST FORGERY")
print("            -    EN  "+str(count_vulnibm_sh_namemoduleexecution_created2022)+" VULNERABILIDADES , EL NOMBRE INCLUYE MODULE EXECUTION ")
print("            -    EN  "+str(count_vulnibm_sh_namebufferoverflow_created2022)+" VULNERABILIDADES , EL NOMBRE INCLUYE BUFFER OVERFLOW")
print("            -    EN  "+str(count_vulnibm_sh_namecommandexecution_created2022)+" VULNERABILIDADES , EL NOMBRE INCLUYE COMMAND EXECUTION")
print("            -    EN  "+str(count_vulnibm_sh_namespoofing_created2022)+" VULNERABILIDADES , EL NOMBRE INCLUYE SPOOFING")
print("            -    EN  "+str(count_vulnibm_sh_nameclickjacking_created2022)+" VULNERABILIDADES , EL NOMBRE INCLUYE CLICKJACKING ")
print("            -    EN  "+str(count_vulnibm_sh_namehijacking_created2022)+" VULNERABILIDADES , EL NOMBRE INCLUYE NAME HIJACKING")
print("            -    EN  "+str(count_vulnibm_sh_namefileinclude_created2022)+" VULNERABILIDADES , EL NOMBRE INCLUYE FILE INCLUDE")
print("            -    EN  "+str(count_vulnibm_sh_namebruteforce_created2022)+" VULNERABILIDADES , EL NOMBRE INCLUYE BRUTE FORCE")
print("            -    EN  "+str(count_vulnibm_sh_namefileupload_created2022)+" VULNERABILIDADES , EL NOMBRE INCLUYE FILE UPLOAD ")
print("            -    EN  "+str(count_vulnibm_sh_nameheaderinjection_created2022)+" VULNERABILIDADES , EL NOMBRE INCLUYE HEADER INJECTION")
print("            -    EN  "+str(count_vulnibm_sh_nametampering_created2022)+" VULNERABILIDADES , EL NOMBRE INCLUYE TAMPERING")
print("            -    EN  "+str(count_vulnibm_sh_nameanother_created2022)+" VULNERABILIDADES , EL NOMBRE INCLUYE UN NOMBRE DISTINTO")
print("\n")

 

print("*****************PORCENTAJE FECHA DE CREACION/NOMBRE VULNERABILIDADES IBM PARTE SMART HOME*****************")
print("\n")                            
                
print("\n")
print(" DE UN TOTAL DE "+str(count_vulnibm_sh_created)+" VULNERABILIDADES :\n") 
print("\n")
print("   - LOS PORCENTAJES DE FECHA DE CREACION SON LOS SIGUIENTES:  \n")
if(count_vulnibm_sh_created2023>0): 
    print("      -    EN EL  "+str(float(((count_vulnibm_sh_created2023*100)/count_vulnibm_sh_created)))+" % DE VULNERABILIDADES LA FECHA DE CREACION ES 2023. LOS PORCENTAJES DE FECHA DE MODIFICACION SON LOS SIGUIENTES :  \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namepathtraversal_created2023*100)/count_vulnibm_sh_created2023)))+" % DE VULNERABILIDADES CREADAS EN 2023 , EL NOMBRE INCLUYE PATH TRAVERSAL ")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namedirectorytraversal_created2023*100)/count_vulnibm_sh_created2023)))+" % DE VULNERABILIDADES CREADAS EN 2023 , EL NOMBRE INCLUYE DIRECTORY TRAVERSAL")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_nameprivilegeescalation_created2023*100)/count_vulnibm_sh_created2023)))+" % DE VULNERABILIDADES CREADAS EN 2023 , EL NOMBRE INCLUYE PRIVILEGE ESCALATION ")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namecrosssitescripting_created2023*100)/count_vulnibm_sh_created2023)))+" % DE VULNERABILIDADES CREADAS EN 2023 , EL NOMBRE INCLUYE CROSS SITE SCRIPTING ")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namesecuritybypass_created2023*100)/count_vulnibm_sh_created2023)))+" % DE VULNERABILIDADES CREADAS EN 2023 , EL NOMBRE INCLUYE SECURITY BYPASS ")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namesinformationdisclosure_created2023*100)/count_vulnibm_sh_created2023)))+" % DE VULNERABILIDADES CREADAS EN 2023 , EL NOMBRE INCLUYE INFORMATION DISCLOSURE ")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namecodeexecution_created2023*100)/count_vulnibm_sh_created2023)))+" % DE VULNERABILIDADES CREADAS EN 2023 , EL NOMBRE INCLUYE CODE EXECUTION ")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namemaninthemiddle_created2023*100)/count_vulnibm_sh_created2023)))+" % DE VULNERABILIDADES CREADAS EN 2023 , EL NOMBRE INCLUYE MAN IN THE MIDDLE ")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namesqlinjection_created2023*100)/count_vulnibm_sh_created2023)))+" % DE VULNERABILIDADES CREADAS EN 2023 , EL NOMBRE INCLUYE SQL INJECTION")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namecrosssiterequestforgery_created2023*100)/count_vulnibm_sh_created2023)))+" % DE VULNERABILIDADES CREADAS EN 2023 , EL NOMBRE INCLUYE CROSS SITE REQUEST FORGERY ")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namemoduleexecution_created2023*100)/count_vulnibm_sh_created2023)))+" % DE VULNERABILIDADES CREADAS EN 2023 , EL NOMBRE INCLUYE MODULE EXECUTION")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namebufferoverflow_created2023*100)/count_vulnibm_sh_created2023)))+" % DE VULNERABILIDADES CREADAS EN 2023 , EL NOMBRE INCLUYE BUFFER OVERFLOW")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namecommandexecution_created2023*100)/count_vulnibm_sh_created2023)))+" % DE VULNERABILIDADES CREADAS EN 2023 , EL NOMBRE INCLUYE COMMAND EXECUTION")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namespoofing_created2023*100)/count_vulnibm_sh_created2023)))+" % DE VULNERABILIDADES CREADAS EN 2023 , EL NOMBRE INCLUYE SPOOFING")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_nameclickjacking_created2023*100)/count_vulnibm_sh_created2023)))+" % DE VULNERABILIDADES CREADAS EN 2023 , EL NOMBRE INCLUYE CLICKJACKING")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namehijacking_created2023*100)/count_vulnibm_sh_created2023)))+" % DE VULNERABILIDADES CREADAS EN 2023 , EL NOMBRE INCLUYE HIJACKING")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namefileinclude_created2023*100)/count_vulnibm_sh_created2023)))+" % DE VULNERABILIDADES CREADAS EN 2023 , EL NOMBRE INCLUYE FILE INCLUDE")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namebruteforce_created2023*100)/count_vulnibm_sh_created2023)))+" % DE VULNERABILIDADES CREADAS EN 2023 , EL NOMBRE INCLUYE BRUTE FORCE")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namefileupload_created2023*100)/count_vulnibm_sh_created2023)))+" % DE VULNERABILIDADES CREADAS EN 2023 , EL NOMBRE INCLUYE FILE UPLOAD")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_nameheaderinjection_created2023*100)/count_vulnibm_sh_created2023)))+" % DE VULNERABILIDADES CREADAS EN 2023 , EL NOMBRE INCLUYE HEADER INJECTION")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_nametampering_created2023*100)/count_vulnibm_sh_created2023)))+" % DE VULNERABILIDADES CREADAS EN 2023 , EL NOMBRE INCLUYE TAMPERING")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_nameanother_created2023*100)/count_vulnibm_sh_created2023)))+" % DE VULNERABILIDADES CREADAS EN 2023 , EL NOMBRE INCLUYE UN VALOR DISTINTO")
    print("\n")
if(count_vulnibm_sh_created2022>0): 
    print("      -    EN EL  "+str(float(((count_vulnibm_sh_created2022*100)/count_vulnibm_sh_created)))+" % DE VULNERABILIDADES LA FECHA DE CREACION ES 2022. LOS PORCENTAJES DE FECHA DE MODIFICACION SON LOS SIGUIENTES :  \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namepathtraversal_created2022*100)/count_vulnibm_sh_created2022)))+" % DE VULNERABILIDADES CREADAS EN 2022 , EL NOMBRE INCLUYE PATH TRAVERSAL ")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namedirectorytraversal_created2022*100)/count_vulnibm_sh_created2022)))+" % DE VULNERABILIDADES CREADAS EN 2022 , EL NOMBRE INCLUYE DIRECTORY TRAVERSAL")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_nameprivilegeescalation_created2022*100)/count_vulnibm_sh_created2022)))+" % DE VULNERABILIDADES CREADAS EN 2022 , EL NOMBRE INCLUYE PRIVILEGE ESCALATION ")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namecrosssitescripting_created2022*100)/count_vulnibm_sh_created2022)))+" % DE VULNERABILIDADES CREADAS EN 2022 , EL NOMBRE INCLUYE CROSS SITE SCRIPTING ")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namesecuritybypass_created2022*100)/count_vulnibm_sh_created2022)))+" % DE VULNERABILIDADES CREADAS EN 2022 , EL NOMBRE INCLUYE SECURITY BYPASS ")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namesinformationdisclosure_created2022*100)/count_vulnibm_sh_created2022)))+" % DE VULNERABILIDADES CREADAS EN 2022 , EL NOMBRE INCLUYE INFORMATION DISCLOSURE ")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namecodeexecution_created2022*100)/count_vulnibm_sh_created2022)))+" % DE VULNERABILIDADES CREADAS EN 2022 , EL NOMBRE INCLUYE CODE EXECUTION ")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namemaninthemiddle_created2022*100)/count_vulnibm_sh_created2022)))+" % DE VULNERABILIDADES CREADAS EN 2022 , EL NOMBRE INCLUYE MAN IN THE MIDDLE ")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namesqlinjection_created2022*100)/count_vulnibm_sh_created2022)))+" % DE VULNERABILIDADES CREADAS EN 2022 , EL NOMBRE INCLUYE SQL INJECTION")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namecrosssiterequestforgery_created2022*100)/count_vulnibm_sh_created2022)))+" % DE VULNERABILIDADES CREADAS EN 2022 , EL NOMBRE INCLUYE CROSS SITE REQUEST FORGERY ")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namemoduleexecution_created2022*100)/count_vulnibm_sh_created2022)))+" % DE VULNERABILIDADES CREADAS EN 2022 , EL NOMBRE INCLUYE MODULE EXECUTION")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namebufferoverflow_created2022*100)/count_vulnibm_sh_created2022)))+" % DE VULNERABILIDADES CREADAS EN 2022 , EL NOMBRE INCLUYE BUFFER OVERFLOW")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namecommandexecution_created2022*100)/count_vulnibm_sh_created2022)))+" % DE VULNERABILIDADES CREADAS EN 2022 , EL NOMBRE INCLUYE COMMAND EXECUTION")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namespoofing_created2022*100)/count_vulnibm_sh_created2022)))+" % DE VULNERABILIDADES CREADAS EN 2022 , EL NOMBRE INCLUYE SPOOFING")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_nameclickjacking_created2022*100)/count_vulnibm_sh_created2022)))+" % DE VULNERABILIDADES CREADAS EN 2022 , EL NOMBRE INCLUYE CLICKJACKING")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namehijacking_created2022*100)/count_vulnibm_sh_created2022)))+" % DE VULNERABILIDADES CREADAS EN 2022 , EL NOMBRE INCLUYE HIJACKING")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namefileinclude_created2022*100)/count_vulnibm_sh_created2022)))+" % DE VULNERABILIDADES CREADAS EN 2022 , EL NOMBRE INCLUYE FILE INCLUDE")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namebruteforce_created2022*100)/count_vulnibm_sh_created2022)))+" % DE VULNERABILIDADES CREADAS EN 2022 , EL NOMBRE INCLUYE BRUTE FORCE")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namefileupload_created2022*100)/count_vulnibm_sh_created2022)))+" % DE VULNERABILIDADES CREADAS EN 2022 , EL NOMBRE INCLUYE FILE UPLOAD")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_nameheaderinjection_created2022*100)/count_vulnibm_sh_created2022)))+" % DE VULNERABILIDADES CREADAS EN 2022 , EL NOMBRE INCLUYE HEADER INJECTION")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_nametampering_created2022*100)/count_vulnibm_sh_created2022)))+" % DE VULNERABILIDADES CREADAS EN 2022 , EL NOMBRE INCLUYE TAMPERING")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_nameanother_created2022*100)/count_vulnibm_sh_created2022)))+" % DE VULNERABILIDADES CREADAS EN 2022 , EL NOMBRE INCLUYE UN VALOR DISTINTO")
    print("\n")

print("*****************ESTADÍSTICAS FECHA DE CREACION/NOMBRE VULNERABILIDADES IBM PARTE IOT Y SMART HOME CONJUNTAS*****************")
print("\n")                            
                
print("\n")
print(" DE UN TOTAL DE "+str(count_vulnibm_sh_created+count_vulnibm_iot_created)+" VULNERABILIDADES:\n") 
print("\n")
print("   - LAS ESTADÍSTICAS DE FECHA DE CREACION SON LAS SIGUIENTES:  \n")
print("      -    EN  "+str(count_vulnibm_sh_created2023+count_vulnibm_iot_created2023)+" VULNERABILIDADES LA FECHA DE CREACION ES 2023. LAS ESTADÍSTICAS DE TIPO DE ATAQUE SEGUN EL VALOR DE NOMBRE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_sh_namepathtraversal_created2023+count_vulnibm_iot_namepathtraversal_created2023)+" VULNERABILIDADES CREADAS EN 2023 , EL NOMBRE INCLUYE PATH TRAVERSAL ")
print("            -    EN  "+str(count_vulnibm_sh_namedirectorytraversal_created2023+count_vulnibm_iot_namedirectorytraversal_created2023)+" VULNERABILIDADES CREADAS EN 2023 , EL NOMBRE INCLUYE DIRECTORY TRAVERSAL")
print("            -    EN  "+str(count_vulnibm_sh_nameprivilegeescalation_created2023+count_vulnibm_iot_nameprivilegeescalation_created2023)+" VULNERABILIDADES CREADAS EN 2023 , EL NOMBRE INCLUYE PRIVILEGE ESCALATION")
print("            -    EN  "+str(count_vulnibm_sh_namecrosssitescripting_created2023+count_vulnibm_iot_namecrosssitescripting_created2023)+" VULNERABILIDADES CREADAS EN 2023 , EL NOMBRE INCLUYE CROSS SITE SCRIPTING ")
print("            -    EN  "+str(count_vulnibm_sh_namesecuritybypass_created2023+count_vulnibm_iot_namesecuritybypass_created2023)+" VULNERABILIDADES CREADAS EN 2023 , EL NOMBRE INCLUYE SECURITY BYPASS ")
print("            -    EN  "+str(count_vulnibm_sh_namesinformationdisclosure_created2023+count_vulnibm_iot_namesinformationdisclosure_created2023)+" VULNERABILIDADES CREADAS EN 2023 , EL NOMBRE INCLUYE INFORMATION DISCLOSURE")
print("            -    EN  "+str(count_vulnibm_sh_namedenialofservice_created2023+count_vulnibm_iot_namedenialofservice_created2023)+" VULNERABILIDADES CREADAS EN 2023 , EL NOMBRE INCLUYE DENIAL OF SERVICE")
print("            -    EN  "+str(count_vulnibm_sh_namecodeexecution_created2023+count_vulnibm_iot_namecodeexecution_created2023)+" VULNERABILIDADES CREADAS EN 2023 , EL NOMBRE INCLUYE CODE EXECUTION ")
print("            -    EN  "+str(count_vulnibm_sh_namemaninthemiddle_created2023+count_vulnibm_iot_namemaninthemiddle_created2023)+" VULNERABILIDADES CREADAS EN 2023 , EL NOMBRE INCLUYE MAN IN THE MIDDLE ")
print("            -    EN  "+str(count_vulnibm_sh_namesqlinjection_created2023+count_vulnibm_iot_namesqlinjection_created2023)+" VULNERABILIDADES CREADAS EN 2023 , EL NOMBRE INCLUYE SQL INJECTION")
print("            -    EN  "+str(count_vulnibm_sh_namecrosssiterequestforgery_created2023+count_vulnibm_iot_namecrosssiterequestforgery_created2023)+" VULNERABILIDADES CREADAS EN 2023 , EL NOMBRE INCLUYE CROSS SITE REQUEST FORGERY")
print("            -    EN  "+str(count_vulnibm_sh_namemoduleexecution_created2023+count_vulnibm_iot_namemoduleexecution_created2023)+" VULNERABILIDADES CREADAS EN 2023 , EL NOMBRE INCLUYE MODULE EXECUTION ")
print("            -    EN  "+str(count_vulnibm_sh_namebufferoverflow_created2023+count_vulnibm_iot_namebufferoverflow_created2023)+" VULNERABILIDADES CREADAS EN 2023 , EL NOMBRE INCLUYE BUFFER OVERFLOW")
print("            -    EN  "+str(count_vulnibm_sh_namecommandexecution_created2023+count_vulnibm_iot_namecommandexecution_created2023)+" VULNERABILIDADES CREADAS EN 2023 , EL NOMBRE INCLUYE COMMAND EXECUTION")
print("            -    EN  "+str(count_vulnibm_sh_namespoofing_created2023+count_vulnibm_iot_namespoofing_created2023)+" VULNERABILIDADES CREADAS EN 2023 , EL NOMBRE INCLUYE SPOOFING")
print("            -    EN  "+str(count_vulnibm_sh_nameclickjacking_created2023+count_vulnibm_iot_nameclickjacking_created2023)+" VULNERABILIDADES CREADAS EN 2023 , EL NOMBRE INCLUYE CLICKJACKING ")
print("            -    EN  "+str(count_vulnibm_sh_namehijacking_created2023+count_vulnibm_iot_namehijacking_created2023)+" VULNERABILIDADES CREADAS EN 2023 , EL NOMBRE INCLUYE NAME HIJACKING")
print("            -    EN  "+str(count_vulnibm_sh_namefileinclude_created2023+count_vulnibm_iot_namefileinclude_created2023)+" VULNERABILIDADES CREADAS EN 2023 , EL NOMBRE INCLUYE FILE INCLUDE")
print("            -    EN  "+str(count_vulnibm_sh_namebruteforce_created2023+count_vulnibm_iot_namebruteforce_created2023)+" VULNERABILIDADES CREADAS EN 2023 , EL NOMBRE INCLUYE BRUTE FORCE")
print("            -    EN  "+str(count_vulnibm_sh_namefileupload_created2023+count_vulnibm_iot_namefileupload_created2023)+" VULNERABILIDADES CREADAS EN 2023 , EL NOMBRE INCLUYE FILE UPLOAD ")
print("            -    EN  "+str(count_vulnibm_sh_nameheaderinjection_created2023+count_vulnibm_iot_nameheaderinjection_created2023)+" VULNERABILIDADES CREADAS EN 2023 , EL NOMBRE INCLUYE HEADER INJECTION")
print("            -    EN  "+str(count_vulnibm_sh_nametampering_created2023+count_vulnibm_iot_nametampering_created2023)+" VULNERABILIDADES CREADAS EN 2023 , EL NOMBRE INCLUYE TAMPERING")
print("            -    EN  "+str(count_vulnibm_sh_nameanother_created2023+count_vulnibm_iot_nameanother_created2023)+" VULNERABILIDADES CREADAS EN 2023 , EL NOMBRE INCLUYE UN NOMBRE DISTINTO")
print("\n")
print("      -    EN  "+str(count_vulnibm_sh_created2022+count_vulnibm_iot_created2022)+" VULNERABILIDADES LA FECHA DE CREACION ES 2022. LAS ESTADÍSTICAS DE TIPO DE ATAQUE SEGUN EL VALOR DE NOMBRE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_sh_namepathtraversal_created2022+count_vulnibm_iot_namepathtraversal_created2022)+" VULNERABILIDADES CREADAS EN 2022 , EL NOMBRE INCLUYE PATH TRAVERSAL ")
print("            -    EN  "+str(count_vulnibm_sh_namedirectorytraversal_created2022+count_vulnibm_iot_namedirectorytraversal_created2022)+" VULNERABILIDADES CREADAS EN 2022 , EL NOMBRE INCLUYE DIRECTORY TRAVERSAL")
print("            -    EN  "+str(count_vulnibm_sh_nameprivilegeescalation_created2022+count_vulnibm_iot_nameprivilegeescalation_created2022)+" VULNERABILIDADES CREADAS EN 2022 , EL NOMBRE INCLUYE PRIVILEGE ESCALATION")
print("            -    EN  "+str(count_vulnibm_sh_namecrosssitescripting_created2022+count_vulnibm_iot_namecrosssitescripting_created2022)+" VULNERABILIDADES CREADAS EN 2022 , EL NOMBRE INCLUYE CROSS SITE SCRIPTING ")
print("            -    EN  "+str(count_vulnibm_sh_namesecuritybypass_created2022+count_vulnibm_iot_namesecuritybypass_created2022)+" VULNERABILIDADES CREADAS EN 2022 , EL NOMBRE INCLUYE SECURITY BYPASS ")
print("            -    EN  "+str(count_vulnibm_sh_namesinformationdisclosure_created2022+count_vulnibm_iot_namesinformationdisclosure_created2022)+" VULNERABILIDADES CREADAS EN 2022 , EL NOMBRE INCLUYE INFORMATION DISCLOSURE")
print("            -    EN  "+str(count_vulnibm_sh_namedenialofservice_created2022+count_vulnibm_iot_namedenialofservice_created2022)+" VULNERABILIDADES CREADAS EN 2022 , EL NOMBRE INCLUYE DENIAL OF SERVICE")
print("            -    EN  "+str(count_vulnibm_sh_namecodeexecution_created2022+count_vulnibm_iot_namecodeexecution_created2022)+" VULNERABILIDADES CREADAS EN 2022 , EL NOMBRE INCLUYE CODE EXECUTION ")
print("            -    EN  "+str(count_vulnibm_sh_namemaninthemiddle_created2022+count_vulnibm_iot_namemaninthemiddle_created2022)+" VULNERABILIDADES CREADAS EN 2022 , EL NOMBRE INCLUYE MAN IN THE MIDDLE ")
print("            -    EN  "+str(count_vulnibm_sh_namesqlinjection_created2022+count_vulnibm_iot_namesqlinjection_created2022)+" VULNERABILIDADES CREADAS EN 2022 , EL NOMBRE INCLUYE SQL INJECTION")
print("            -    EN  "+str(count_vulnibm_sh_namecrosssiterequestforgery_created2022+count_vulnibm_iot_namecrosssiterequestforgery_created2022)+" VULNERABILIDADES CREADAS EN 2022 , EL NOMBRE INCLUYE CROSS SITE REQUEST FORGERY")
print("            -    EN  "+str(count_vulnibm_sh_namemoduleexecution_created2022+count_vulnibm_iot_namemoduleexecution_created2022)+" VULNERABILIDADES CREADAS EN 2022 , EL NOMBRE INCLUYE MODULE EXECUTION ")
print("            -    EN  "+str(count_vulnibm_sh_namebufferoverflow_created2022+count_vulnibm_iot_namebufferoverflow_created2022)+" VULNERABILIDADES CREADAS EN 2022 , EL NOMBRE INCLUYE BUFFER OVERFLOW")
print("            -    EN  "+str(count_vulnibm_sh_namecommandexecution_created2022+count_vulnibm_iot_namecommandexecution_created2022)+" VULNERABILIDADES CREADAS EN 2022 , EL NOMBRE INCLUYE COMMAND EXECUTION")
print("            -    EN  "+str(count_vulnibm_sh_namespoofing_created2022+count_vulnibm_iot_namespoofing_created2022)+" VULNERABILIDADES CREADAS EN 2022 , EL NOMBRE INCLUYE SPOOFING")
print("            -    EN  "+str(count_vulnibm_sh_nameclickjacking_created2022+count_vulnibm_iot_nameclickjacking_created2022)+" VULNERABILIDADES CREADAS EN 2022 , EL NOMBRE INCLUYE CLICKJACKING ")
print("            -    EN  "+str(count_vulnibm_sh_namehijacking_created2022+count_vulnibm_iot_namehijacking_created2022)+" VULNERABILIDADES CREADAS EN 2022 , EL NOMBRE INCLUYE NAME HIJACKING")
print("            -    EN  "+str(count_vulnibm_sh_namefileinclude_created2022+count_vulnibm_iot_namefileinclude_created2022)+" VULNERABILIDADES CREADAS EN 2022 , EL NOMBRE INCLUYE FILE INCLUDE")
print("            -    EN  "+str(count_vulnibm_sh_namebruteforce_created2022+count_vulnibm_iot_namebruteforce_created2022)+" VULNERABILIDADES CREADAS EN 2022 , EL NOMBRE INCLUYE BRUTE FORCE")
print("            -    EN  "+str(count_vulnibm_sh_namefileupload_created2022+count_vulnibm_iot_namefileupload_created2022)+" VULNERABILIDADES CREADAS EN 2022 , EL NOMBRE INCLUYE FILE UPLOAD ")
print("            -    EN  "+str(count_vulnibm_sh_nameheaderinjection_created2022+count_vulnibm_iot_nameheaderinjection_created2022)+" VULNERABILIDADES CREADAS EN 2022 , EL NOMBRE INCLUYE HEADER INJECTION")
print("            -    EN  "+str(count_vulnibm_sh_nametampering_created2022+count_vulnibm_iot_nametampering_created2022)+" VULNERABILIDADES CREADAS EN 2022 , EL NOMBRE INCLUYE TAMPERING")
print("            -    EN  "+str(count_vulnibm_sh_nameanother_created2022+count_vulnibm_iot_nameanother_created2022)+" VULNERABILIDADES CREADAS EN 2022 , EL NOMBRE INCLUYE UN NOMBRE DISTINTO")
print("\n")




print("*****************PORCENTAJE FECHA DE CREACION/NOMBRE VULNERABILIDADES IBM PARTE IOT Y SMART HOME CONJUNTAS*****************")
print("\n")                            
                
print("\n")
print(" DE UN TOTAL DE "+str(count_vulnibm_sh_created+count_vulnibm_iot_created)+" VULNERABILIDADES :\n") 
print("\n")
print("   - LOS PORCENTAJES DE FECHA DE CREACION SON LOS SIGUIENTES:  \n")
if((count_vulnibm_sh_created2023+count_vulnibm_iot_created2023)>0): 
    print("      -    EN EL  "+str(float((((count_vulnibm_sh_created2023+count_vulnibm_iot_created2023)*100)/(count_vulnibm_sh_created+count_vulnibm_iot_created))))+" % DE VULNERABILIDADES LA FECHA DE CREACION ES 2023. LOS PORCENTAJES DE TIPO DE ATAQUE SEGUN EL VALOR DE NOMBRE SON  LOS SIGUIENTES :  \n")
    print("            -    EN EL  "+str(float((((count_vulnibm_sh_namepathtraversal_created2023+count_vulnibm_iot_namepathtraversal_created2023)*100)/(count_vulnibm_iot_created2023+count_vulnibm_sh_created2023))))+" % DE VULNERABILIDADES CREADAS EN 2023  EL NOMBRE INCLUYE PATH TRAVERSAL ")
    print("            -    EN EL  "+str(float((((count_vulnibm_sh_namedirectorytraversal_created2023+count_vulnibm_iot_namedirectorytraversal_created2023)*100)/(count_vulnibm_iot_created2023+count_vulnibm_sh_created2023))))+" % DE VULNERABILIDADES CREADAS EN 2023  EL NOMBRE INCLUYE DIRECTORY TRAVERSAL ")
    print("            -    EN EL  "+str(float((((count_vulnibm_sh_nameprivilegeescalation_created2023+count_vulnibm_iot_nameprivilegeescalation_created2023)*100)/(count_vulnibm_iot_created2023+count_vulnibm_sh_created2023))))+" % DE VULNERABILIDADES CREADAS EN 2023  EL NOMBRE INCLUYE PRIVILEGE ESCALATION ")
    print("            -    EN EL  "+str(float((((count_vulnibm_sh_namecrosssitescripting_created2023+count_vulnibm_iot_namecrosssitescripting_created2023)*100)/(count_vulnibm_iot_created2023+count_vulnibm_sh_created2023))))+" % DE VULNERABILIDADES CREADAS EN 2023  EL NOMBRE INCLUYE CROSS SITE SCRIPTING ")
    print("            -    EN EL  "+str(float((((count_vulnibm_sh_namesecuritybypass_created2023+count_vulnibm_iot_namesecuritybypass_created2023)*100)/(count_vulnibm_iot_created2023+count_vulnibm_sh_created2023))))+" % DE VULNERABILIDADES CREADAS EN 2023  EL NOMBRE INCLUYE SECURITY BYPASS ")
    print("            -    EN EL  "+str(float((((count_vulnibm_sh_namesinformationdisclosure_created2023+count_vulnibm_iot_namesinformationdisclosure_created2023)*100)/(count_vulnibm_iot_created2023+count_vulnibm_sh_created2023))))+" % DE VULNERABILIDADES CREADAS EN 2023  EL NOMBRE INCLUYE INFORMATION DISCLOSURE ")
    print("            -    EN EL  "+str(float((((count_vulnibm_sh_namecodeexecution_created2023+count_vulnibm_iot_namecodeexecution_created2023)*100)/(count_vulnibm_iot_created2023+count_vulnibm_sh_created2023))))+" % DE VULNERABILIDADES CREADAS EN 2023  EL NOMBRE INCLUYE CODE EXECUTION ")
    print("            -    EN EL  "+str(float((((count_vulnibm_sh_namemaninthemiddle_created2023+count_vulnibm_iot_namemaninthemiddle_created2023)*100)/(count_vulnibm_iot_created2023+count_vulnibm_sh_created2023))))+" % DE VULNERABILIDADES CREADAS EN 2023  EL NOMBRE INCLUYE MAN IN THE MIDDLE ")
    print("            -    EN EL  "+str(float((((count_vulnibm_sh_namesqlinjection_created2023+count_vulnibm_iot_namesqlinjection_created2023)*100)/(count_vulnibm_iot_created2023+count_vulnibm_sh_created2023))))+" % DE VULNERABILIDADES CREADAS EN 2023  EL NOMBRE INCLUYE SQL INJECTION ")
    print("            -    EN EL  "+str(float((((count_vulnibm_sh_namecrosssiterequestforgery_created2023+count_vulnibm_iot_namecrosssiterequestforgery_created2023)*100)/(count_vulnibm_iot_created2023+count_vulnibm_sh_created2023))))+" % DE VULNERABILIDADES CREADAS EN 2023  EL NOMBRE INCLUYE CROSS SITE REQUEST FORGERY ")
    print("            -    EN EL  "+str(float((((count_vulnibm_sh_namemoduleexecution_created2023+count_vulnibm_iot_namemoduleexecution_created2023)*100)/(count_vulnibm_iot_created2023+count_vulnibm_sh_created2023))))+" % DE VULNERABILIDADES CREADAS EN 2023  EL NOMBRE INCLUYE MODULE EXECUTION ")
    print("            -    EN EL  "+str(float((((count_vulnibm_sh_namebufferoverflow_created2023+count_vulnibm_iot_namebufferoverflow_created2023)*100)/(count_vulnibm_iot_created2023+count_vulnibm_sh_created2023))))+" % DE VULNERABILIDADES CREADAS EN 2023  EL NOMBRE INCLUYE BUFFER OVERFLOW ")
    print("            -    EN EL  "+str(float((((count_vulnibm_sh_namecommandexecution_created2023+count_vulnibm_iot_namecommandexecution_created2023)*100)/(count_vulnibm_iot_created2023+count_vulnibm_sh_created2023))))+" % DE VULNERABILIDADES CREADAS EN 2023  EL NOMBRE INCLUYE COMMAND EXECUTION ")
    print("            -    EN EL  "+str(float((((count_vulnibm_sh_namespoofing_created2023+count_vulnibm_iot_namespoofing_created2023)*100)/(count_vulnibm_iot_created2023+count_vulnibm_sh_created2023))))+" % DE VULNERABILIDADES CREADAS EN 2023  EL NOMBRE INCLUYE SPOOFING ")
    print("            -    EN EL  "+str(float((((count_vulnibm_sh_nameclickjacking_created2023+count_vulnibm_iot_nameclickjacking_created2023)*100)/(count_vulnibm_iot_created2023+count_vulnibm_sh_created2023))))+" % DE VULNERABILIDADES CREADAS EN 2023  EL NOMBRE INCLUYE CLICKJACKING")
    print("            -    EN EL  "+str(float((((count_vulnibm_sh_namehijacking_created2023+count_vulnibm_iot_namehijacking_created2023)*100)/(count_vulnibm_iot_created2023+count_vulnibm_sh_created2023))))+" % DE VULNERABILIDADES CREADAS EN 2023  EL NOMBRE INCLUYE HIJACKING ")
    print("            -    EN EL  "+str(float((((count_vulnibm_sh_namefileinclude_created2023+count_vulnibm_iot_namefileinclude_created2023)*100)/(count_vulnibm_iot_created2023+count_vulnibm_sh_created2023))))+" % DE VULNERABILIDADES CREADAS EN 2023  EL NOMBRE INCLUYE FILE INCLUDE ")
    print("            -    EN EL  "+str(float((((count_vulnibm_sh_namebruteforce_created2023+count_vulnibm_iot_namebruteforce_created2023)*100)/(count_vulnibm_iot_created2023+count_vulnibm_sh_created2023))))+" % DE VULNERABILIDADES CREADAS EN 2023  EL NOMBRE INCLUYE BRUTE FORCE ")
    print("            -    EN EL  "+str(float((((count_vulnibm_sh_namefileupload_created2023+count_vulnibm_iot_namefileupload_created2023)*100)/(count_vulnibm_iot_created2023+count_vulnibm_sh_created2023))))+" % DE VULNERABILIDADES CREADAS EN 2023  EL NOMBRE INCLUYE FILE UPLOAD ")
    print("            -    EN EL  "+str(float((((count_vulnibm_sh_nameheaderinjection_created2023+count_vulnibm_iot_nameheaderinjection_created2023)*100)/(count_vulnibm_iot_created2023+count_vulnibm_sh_created2023))))+" % DE VULNERABILIDADES CREADAS EN 2023  EL NOMBRE INCLUYE HEADER INJECTION ")
    print("            -    EN EL  "+str(float((((count_vulnibm_sh_nametampering_created2023+count_vulnibm_iot_nametampering_created2023)*100)/(count_vulnibm_iot_created2023+count_vulnibm_sh_created2023))))+" % DE VULNERABILIDADES CREADAS EN 2023  EL NOMBRE INCLUYE TAMPERING ")
    print("            -    EN EL  "+str(float((((count_vulnibm_sh_nameanother_created2023+count_vulnibm_iot_nameanother_created2023)*100)/(count_vulnibm_iot_created2023+count_vulnibm_sh_created2023))))+" % DE VULNERABILIDADES CREADAS EN 2023  EL NOMBRE INCLUYE UN VALOR DISTINTO")
    print("\n")
if((count_vulnibm_sh_created2022+count_vulnibm_iot_created2022)>0): 
    print("      -    EN EL  "+str(float((((count_vulnibm_sh_created2022+count_vulnibm_iot_created2022)*100)/(count_vulnibm_sh_created+count_vulnibm_iot_created))))+" % DE VULNERABILIDADES LA FECHA DE CREACION ES 2022. LOS PORCENTAJES DE TIPO DE ATAQUE SEGUN EL VALOR DE NOMBRE SON  LOS SIGUIENTES :  \n")
    print("            -    EN EL  "+str(float((((count_vulnibm_sh_namepathtraversal_created2022+count_vulnibm_iot_namepathtraversal_created2022)*100)/(count_vulnibm_iot_created2022+count_vulnibm_sh_created2022))))+" % DE VULNERABILIDADES CREADAS EN 2022  EL NOMBRE INCLUYE PATH TRAVERSAL ")
    print("            -    EN EL  "+str(float((((count_vulnibm_sh_namedirectorytraversal_created2022+count_vulnibm_iot_namedirectorytraversal_created2022)*100)/(count_vulnibm_iot_created2022+count_vulnibm_sh_created2022))))+" % DE VULNERABILIDADES CREADAS EN 2022  EL NOMBRE INCLUYE DIRECTORY TRAVERSAL ")
    print("            -    EN EL  "+str(float((((count_vulnibm_sh_nameprivilegeescalation_created2022+count_vulnibm_iot_nameprivilegeescalation_created2022)*100)/(count_vulnibm_iot_created2022+count_vulnibm_sh_created2022))))+" % DE VULNERABILIDADES CREADAS EN 2022  EL NOMBRE INCLUYE PRIVILEGE ESCALATION ")
    print("            -    EN EL  "+str(float((((count_vulnibm_sh_namecrosssitescripting_created2022+count_vulnibm_iot_namecrosssitescripting_created2022)*100)/(count_vulnibm_iot_created2022+count_vulnibm_sh_created2022))))+" % DE VULNERABILIDADES CREADAS EN 2022  EL NOMBRE INCLUYE CROSS SITE SCRIPTING ")
    print("            -    EN EL  "+str(float((((count_vulnibm_sh_namesecuritybypass_created2022+count_vulnibm_iot_namesecuritybypass_created2022)*100)/(count_vulnibm_iot_created2022+count_vulnibm_sh_created2022))))+" % DE VULNERABILIDADES CREADAS EN 2022  EL NOMBRE INCLUYE SECURITY BYPASS ")
    print("            -    EN EL  "+str(float((((count_vulnibm_sh_namesinformationdisclosure_created2022+count_vulnibm_iot_namesinformationdisclosure_created2022)*100)/(count_vulnibm_iot_created2022+count_vulnibm_sh_created2022))))+" % DE VULNERABILIDADES CREADAS EN 2022  EL NOMBRE INCLUYE INFORMATION DISCLOSURE ")
    print("            -    EN EL  "+str(float((((count_vulnibm_sh_namecodeexecution_created2022+count_vulnibm_iot_namecodeexecution_created2022)*100)/(count_vulnibm_iot_created2022+count_vulnibm_sh_created2022))))+" % DE VULNERABILIDADES CREADAS EN 2022  EL NOMBRE INCLUYE CODE EXECUTION ")
    print("            -    EN EL  "+str(float((((count_vulnibm_sh_namemaninthemiddle_created2022+count_vulnibm_iot_namemaninthemiddle_created2022)*100)/(count_vulnibm_iot_created2022+count_vulnibm_sh_created2022))))+" % DE VULNERABILIDADES CREADAS EN 2022  EL NOMBRE INCLUYE MAN IN THE MIDDLE ")
    print("            -    EN EL  "+str(float((((count_vulnibm_sh_namesqlinjection_created2022+count_vulnibm_iot_namesqlinjection_created2022)*100)/(count_vulnibm_iot_created2022+count_vulnibm_sh_created2022))))+" % DE VULNERABILIDADES CREADAS EN 2022  EL NOMBRE INCLUYE SQL INJECTION ")
    print("            -    EN EL  "+str(float((((count_vulnibm_sh_namecrosssiterequestforgery_created2022+count_vulnibm_iot_namecrosssiterequestforgery_created2022)*100)/(count_vulnibm_iot_created2022+count_vulnibm_sh_created2022))))+" % DE VULNERABILIDADES CREADAS EN 2022  EL NOMBRE INCLUYE CROSS SITE REQUEST FORGERY ")
    print("            -    EN EL  "+str(float((((count_vulnibm_sh_namemoduleexecution_created2022+count_vulnibm_iot_namemoduleexecution_created2022)*100)/(count_vulnibm_iot_created2022+count_vulnibm_sh_created2022))))+" % DE VULNERABILIDADES CREADAS EN 2022  EL NOMBRE INCLUYE MODULE EXECUTION ")
    print("            -    EN EL  "+str(float((((count_vulnibm_sh_namebufferoverflow_created2022+count_vulnibm_iot_namebufferoverflow_created2022)*100)/(count_vulnibm_iot_created2022+count_vulnibm_sh_created2022))))+" % DE VULNERABILIDADES CREADAS EN 2022  EL NOMBRE INCLUYE BUFFER OVERFLOW ")
    print("            -    EN EL  "+str(float((((count_vulnibm_sh_namecommandexecution_created2022+count_vulnibm_iot_namecommandexecution_created2022)*100)/(count_vulnibm_iot_created2022+count_vulnibm_sh_created2022))))+" % DE VULNERABILIDADES CREADAS EN 2022  EL NOMBRE INCLUYE COMMAND EXECUTION ")
    print("            -    EN EL  "+str(float((((count_vulnibm_sh_namespoofing_created2022+count_vulnibm_iot_namespoofing_created2022)*100)/(count_vulnibm_iot_created2022+count_vulnibm_sh_created2022))))+" % DE VULNERABILIDADES CREADAS EN 2022  EL NOMBRE INCLUYE SPOOFING ")
    print("            -    EN EL  "+str(float((((count_vulnibm_sh_nameclickjacking_created2022+count_vulnibm_iot_nameclickjacking_created2022)*100)/(count_vulnibm_iot_created2022+count_vulnibm_sh_created2022))))+" % DE VULNERABILIDADES CREADAS EN 2022  EL NOMBRE INCLUYE CLICKJACKING")
    print("            -    EN EL  "+str(float((((count_vulnibm_sh_namehijacking_created2022+count_vulnibm_iot_namehijacking_created2022)*100)/(count_vulnibm_iot_created2022+count_vulnibm_sh_created2022))))+" % DE VULNERABILIDADES CREADAS EN 2022  EL NOMBRE INCLUYE HIJACKING ")
    print("            -    EN EL  "+str(float((((count_vulnibm_sh_namefileinclude_created2022+count_vulnibm_iot_namefileinclude_created2022)*100)/(count_vulnibm_iot_created2022+count_vulnibm_sh_created2022))))+" % DE VULNERABILIDADES CREADAS EN 2022  EL NOMBRE INCLUYE FILE INCLUDE ")
    print("            -    EN EL  "+str(float((((count_vulnibm_sh_namebruteforce_created2022+count_vulnibm_iot_namebruteforce_created2022)*100)/(count_vulnibm_iot_created2022+count_vulnibm_sh_created2022))))+" % DE VULNERABILIDADES CREADAS EN 2022  EL NOMBRE INCLUYE BRUTE FORCE ")
    print("            -    EN EL  "+str(float((((count_vulnibm_sh_namefileupload_created2022+count_vulnibm_iot_namefileupload_created2022)*100)/(count_vulnibm_iot_created2022+count_vulnibm_sh_created2022))))+" % DE VULNERABILIDADES CREADAS EN 2022  EL NOMBRE INCLUYE FILE UPLOAD ")
    print("            -    EN EL  "+str(float((((count_vulnibm_sh_nameheaderinjection_created2022+count_vulnibm_iot_nameheaderinjection_created2022)*100)/(count_vulnibm_iot_created2022+count_vulnibm_sh_created2022))))+" % DE VULNERABILIDADES CREADAS EN 2022  EL NOMBRE INCLUYE HEADER INJECTION ")
    print("            -    EN EL  "+str(float((((count_vulnibm_sh_nametampering_created2022+count_vulnibm_iot_nametampering_created2022)*100)/(count_vulnibm_iot_created2022+count_vulnibm_sh_created2022))))+" % DE VULNERABILIDADES CREADAS EN 2022  EL NOMBRE INCLUYE TAMPERING ")
    print("            -    EN EL  "+str(float((((count_vulnibm_sh_nameanother_created2022+count_vulnibm_iot_nameanother_created2022)*100)/(count_vulnibm_iot_created2022+count_vulnibm_sh_created2022))))+" % DE VULNERABILIDADES CREADAS EN 2022  EL NOMBRE INCLUYE UN VALOR DISTINTO")
    print("\n")
