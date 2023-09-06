				
import pandas as pd
from datetime import datetime,timedelta



#Abro los ficheros con los que voy a tratar




df_vulnibm_iot = pd.read_excel('vulnerabilidades_ibm_iot_2023.xlsx')
#Variable para almacenar el contador total de valores de nombre
count_vulnibm_iot_names=0
#Variable para almacenar el contador total de valores de un nombre especifico
count_vulnibm_iot_namepathtraversal=0
#Variable para almacenar el contador de valores de complejidad de ATAQUE dado un valor especifico de nombre
count_vulnibm_iot_namepathtraversal_accesscom=0
count_vulnibm_iot_namepathtraversal_highaccesscom=0
count_vulnibm_iot_namepathtraversal_lowaccesscom=0
count_vulnibm_iot_namepathtraversal_mediumaccesscom=0

count_vulnibm_iot_namedirectorytraversal=0
count_vulnibm_iot_namedirectorytraversal_accesscom=0
count_vulnibm_iot_namedirectorytraversal_highaccesscom=0
count_vulnibm_iot_namedirectorytraversal_lowaccesscom=0
count_vulnibm_iot_namedirectorytraversal_mediumaccesscom=0

count_vulnibm_iot_nameprivilegeescalation=0
count_vulnibm_iot_nameprivilegeescalation_accesscom=0
count_vulnibm_iot_nameprivilegeescalation_highaccesscom=0
count_vulnibm_iot_nameprivilegeescalation_lowaccesscom=0
count_vulnibm_iot_nameprivilegeescalation_mediumaccesscom=0

count_vulnibm_iot_namecrosssitescripting=0
count_vulnibm_iot_namecrosssitescripting_accesscom=0
count_vulnibm_iot_namecrosssitescripting_highaccesscom=0
count_vulnibm_iot_namecrosssitescripting_lowaccesscom=0
count_vulnibm_iot_namecrosssitescripting_mediumaccesscom=0

count_vulnibm_iot_namesecuritybypass=0
count_vulnibm_iot_namesecuritybypass_accesscom=0
count_vulnibm_iot_namesecuritybypass_highaccesscom=0
count_vulnibm_iot_namesecuritybypass_lowaccesscom=0
count_vulnibm_iot_namesecuritybypass_mediumaccesscom=0

count_vulnibm_iot_nameinformationdisclosure=0
count_vulnibm_iot_nameinformationdisclosure_accesscom=0
count_vulnibm_iot_nameinformationdisclosure_highaccesscom=0
count_vulnibm_iot_nameinformationdisclosure_lowaccesscom=0
count_vulnibm_iot_nameinformationdisclosure_mediumaccesscom=0

count_vulnibm_iot_namedenialofservice=0
count_vulnibm_iot_namedenialofservice_accesscom=0
count_vulnibm_iot_namedenialofservice_highaccesscom=0
count_vulnibm_iot_namedenialofservice_lowaccesscom=0
count_vulnibm_iot_namedenialofservice_mediumaccesscom=0

count_vulnibm_iot_namecodeexecution=0
count_vulnibm_iot_namecodeexecution_accesscom=0
count_vulnibm_iot_namecodeexecution_highaccesscom=0
count_vulnibm_iot_namecodeexecution_lowaccesscom=0
count_vulnibm_iot_namecodeexecution_mediumaccesscom=0

count_vulnibm_iot_namemaninthemiddle=0
count_vulnibm_iot_namemaninthemiddle_accesscom=0
count_vulnibm_iot_namemaninthemiddle_highaccesscom=0
count_vulnibm_iot_namemaninthemiddle_lowaccesscom=0
count_vulnibm_iot_namemaninthemiddle_mediumaccesscom=0

count_vulnibm_iot_namesqlinjection=0
count_vulnibm_iot_namesqlinjection_accesscom=0
count_vulnibm_iot_namesqlinjection_highaccesscom=0
count_vulnibm_iot_namesqlinjection_lowaccesscom=0
count_vulnibm_iot_namesqlinjection_mediumaccesscom=0

count_vulnibm_iot_namecrosssiterequestforgery=0
count_vulnibm_iot_namecrosssiterequestforgery_accesscom=0
count_vulnibm_iot_namecrosssiterequestforgery_highaccesscom=0
count_vulnibm_iot_namecrosssiterequestforgery_lowaccesscom=0
count_vulnibm_iot_namecrosssiterequestforgery_mediumaccesscom=0

count_vulnibm_iot_namemoduleexecution=0
count_vulnibm_iot_namemoduleexecution_accesscom=0
count_vulnibm_iot_namemoduleexecution_highaccesscom=0
count_vulnibm_iot_namemoduleexecution_lowaccesscom=0
count_vulnibm_iot_namemoduleexecution_mediumaccesscom=0

count_vulnibm_iot_namebufferoverflow=0
count_vulnibm_iot_namebufferoverflow_accesscom=0
count_vulnibm_iot_namebufferoverflow_highaccesscom=0
count_vulnibm_iot_namebufferoverflow_lowaccesscom=0
count_vulnibm_iot_namebufferoverflow_mediumaccesscom=0

count_vulnibm_iot_namecommandexecution=0
count_vulnibm_iot_namecommandexecution_accesscom=0
count_vulnibm_iot_namecommandexecution_highaccesscom=0
count_vulnibm_iot_namecommandexecution_lowaccesscom=0
count_vulnibm_iot_namecommandexecution_mediumaccesscom=0

count_vulnibm_iot_namespoofing=0
count_vulnibm_iot_namespoofing_accesscom=0
count_vulnibm_iot_namespoofing_highaccesscom=0
count_vulnibm_iot_namespoofing_lowaccesscom=0
count_vulnibm_iot_namespoofing_mediumaccesscom=0

count_vulnibm_iot_nameclickjacking=0
count_vulnibm_iot_nameclickjacking_accesscom=0
count_vulnibm_iot_nameclickjacking_highaccesscom=0
count_vulnibm_iot_nameclickjacking_lowaccesscom=0
count_vulnibm_iot_nameclickjacking_mediumaccesscom=0

count_vulnibm_iot_namehijacking=0
count_vulnibm_iot_namehijacking_accesscom=0
count_vulnibm_iot_namehijacking_highaccesscom=0
count_vulnibm_iot_namehijacking_lowaccesscom=0
count_vulnibm_iot_namehijacking_mediumaccesscom=0

count_vulnibm_iot_namefileinclude=0
count_vulnibm_iot_namefileinclude_accesscom=0
count_vulnibm_iot_namefileinclude_highaccesscom=0
count_vulnibm_iot_namefileinclude_lowaccesscom=0
count_vulnibm_iot_namefileinclude_mediumaccesscom=0

count_vulnibm_iot_namebruteforce=0
count_vulnibm_iot_namebruteforce_accesscom=0
count_vulnibm_iot_namebruteforce_highaccesscom=0
count_vulnibm_iot_namebruteforce_lowaccesscom=0
count_vulnibm_iot_namebruteforce_mediumaccesscom=0

count_vulnibm_iot_namefileupload=0
count_vulnibm_iot_namefileupload_accesscom=0
count_vulnibm_iot_namefileupload_highaccesscom=0
count_vulnibm_iot_namefileupload_lowaccesscom=0
count_vulnibm_iot_namefileupload_mediumaccesscom=0

count_vulnibm_iot_nameheaderinjection=0
count_vulnibm_iot_nameheaderinjection_accesscom=0
count_vulnibm_iot_nameheaderinjection_highaccesscom=0
count_vulnibm_iot_nameheaderinjection_lowaccesscom=0
count_vulnibm_iot_nameheaderinjection_mediumaccesscom=0

count_vulnibm_iot_nametampering=0
count_vulnibm_iot_nametampering_accesscom=0
count_vulnibm_iot_nametampering_highaccesscom=0
count_vulnibm_iot_nametampering_lowaccesscom=0
count_vulnibm_iot_nametampering_mediumaccesscom=0

count_vulnibm_iot_nameanother=0
count_vulnibm_iot_nameanother_accesscom=0
count_vulnibm_iot_nameanother_highaccesscom=0
count_vulnibm_iot_nameanother_lowaccesscom=0
count_vulnibm_iot_nameanother_mediumaccesscom=0

#Comprobamos el contenido de name
for r in range(0,len(df_vulnibm_iot["name"])):                       
    aux_str=df_vulnibm_iot["name"][r].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
    if(aux_str!='NONE'):
        count_vulnibm_iot_names+=1
        #Compruebo el valor de name
        if('pathtraversal' in aux_str):
            count_vulnibm_iot_namepathtraversal+=1
            #Compruebo el valor de complejidad de ATAQUE
            if(df_vulnibm_iot["x_xfe_cvss_access_complexity"][r]=='High'):
                count_vulnibm_iot_namepathtraversal_accesscom+=1
                count_vulnibm_iot_namepathtraversal_highaccesscom+=1
            elif(df_vulnibm_iot["x_xfe_cvss_access_complexity"][r]=='Low'):
                count_vulnibm_iot_namepathtraversal_accesscom+=1
                count_vulnibm_iot_namepathtraversal_lowaccesscom+=1
            elif(df_vulnibm_iot["x_xfe_cvss_access_complexity"][r]=='Medium'):
                count_vulnibm_iot_namepathtraversal_accesscom+=1
                count_vulnibm_iot_namepathtraversal_mediumaccesscom+=1
    
        elif('directorytraversal' in aux_str):
            
            count_vulnibm_iot_namedirectorytraversal+=1
            if(df_vulnibm_iot["x_xfe_cvss_access_complexity"][r]=='High'):
                count_vulnibm_iot_namedirectorytraversal_accesscom+=1
                count_vulnibm_iot_namedirectorytraversal_highaccesscom+=1
            elif(df_vulnibm_iot["x_xfe_cvss_access_complexity"][r]=='Low'):
                count_vulnibm_iot_namedirectorytraversal_accesscom+=1
                count_vulnibm_iot_namedirectorytraversal_lowaccesscom+=1
            elif(df_vulnibm_iot["x_xfe_cvss_access_complexity"][r]=='Medium'):
                count_vulnibm_iot_namedirectorytraversal_accesscom+=1
                count_vulnibm_iot_namedirectorytraversal_mediumaccesscom+=1
            
            
        elif('privilegeescalation' in aux_str):
        
            count_vulnibm_iot_nameprivilegeescalation+=1
            if(df_vulnibm_iot["x_xfe_cvss_access_complexity"][r]=='High'):
                count_vulnibm_iot_nameprivilegeescalation_accesscom+=1
                count_vulnibm_iot_nameprivilegeescalation_highaccesscom+=1
            elif(df_vulnibm_iot["x_xfe_cvss_access_complexity"][r]=='Low'):
                count_vulnibm_iot_nameprivilegeescalation_accesscom+=1
                count_vulnibm_iot_nameprivilegeescalation_lowaccesscom+=1
            elif(df_vulnibm_iot["x_xfe_cvss_access_complexity"][r]=='Medium'):
                count_vulnibm_iot_nameprivilegeescalation_accesscom+=1
                count_vulnibm_iot_nameprivilegeescalation_mediumaccesscom+=1
            
        elif('cross-sitescripting' in aux_str):
        
            count_vulnibm_iot_namecrosssitescripting+=1
            if(df_vulnibm_iot["x_xfe_cvss_access_complexity"][r]=='High'):
                count_vulnibm_iot_namecrosssitescripting_accesscom+=1
                count_vulnibm_iot_namecrosssitescripting_highaccesscom+=1
            elif(df_vulnibm_iot["x_xfe_cvss_access_complexity"][r]=='Low'):
                count_vulnibm_iot_namecrosssitescripting_accesscom+=1
                count_vulnibm_iot_namecrosssitescripting_lowaccesscom+=1
            elif(df_vulnibm_iot["x_xfe_cvss_access_complexity"][r]=='Medium'):
                count_vulnibm_iot_namecrosssitescripting_accesscom+=1
                count_vulnibm_iot_namecrosssitescripting_mediumaccesscom+=1
                                         
        elif('securitybypass' in aux_str):
        
            count_vulnibm_iot_namesecuritybypass+=1
            if(df_vulnibm_iot["x_xfe_cvss_access_complexity"][r]=='High'):
                count_vulnibm_iot_namesecuritybypass_accesscom+=1
                count_vulnibm_iot_namesecuritybypass_highaccesscom+=1
            elif(df_vulnibm_iot["x_xfe_cvss_access_complexity"][r]=='Low'):
                count_vulnibm_iot_namesecuritybypass_accesscom+=1
                count_vulnibm_iot_namesecuritybypass_lowaccesscom+=1
            elif(df_vulnibm_iot["x_xfe_cvss_access_complexity"][r]=='Medium'):
                count_vulnibm_iot_namesecuritybypass_accesscom+=1
                count_vulnibm_iot_namesecuritybypass_mediumaccesscom+=1
                                         
        elif('information_disclosure' in aux_str or 'informationdisclosure' in aux_str):
        
            count_vulnibm_iot_nameinformationdisclosure+=1
            if(df_vulnibm_iot["x_xfe_cvss_access_complexity"][r]=='High'):
                count_vulnibm_iot_nameinformationdisclosure_accesscom+=1
                count_vulnibm_iot_nameinformationdisclosure_highaccesscom+=1
            elif(df_vulnibm_iot["x_xfe_cvss_access_complexity"][r]=='Low'):
                count_vulnibm_iot_nameinformationdisclosure_accesscom+=1
                count_vulnibm_iot_nameinformationdisclosure_lowaccesscom+=1
            elif(df_vulnibm_iot["x_xfe_cvss_access_complexity"][r]=='Medium'):
                count_vulnibm_iot_nameinformationdisclosure_accesscom+=1
                count_vulnibm_iot_nameinformationdisclosure_mediumaccesscom+=1
                                         
        elif('denialofservice' in aux_str):
            
            count_vulnibm_iot_namedenialofservice+=1
            if(df_vulnibm_iot["x_xfe_cvss_access_complexity"][r]=='High'):
                count_vulnibm_iot_namedenialofservice_accesscom+=1
                count_vulnibm_iot_namedenialofservice_highaccesscom+=1
            elif(df_vulnibm_iot["x_xfe_cvss_access_complexity"][r]=='Low'):
                count_vulnibm_iot_namedenialofservice_accesscom+=1
                count_vulnibm_iot_namedenialofservice_lowaccesscom+=1
            elif(df_vulnibm_iot["x_xfe_cvss_access_complexity"][r]=='Medium'):
                count_vulnibm_iot_namedenialofservice_accesscom+=1
                count_vulnibm_iot_namedenialofservice_mediumaccesscom+=1
            
        elif('codeexecution' in aux_str):
        
        
            count_vulnibm_iot_namecodeexecution+=1
            if(df_vulnibm_iot["x_xfe_cvss_access_complexity"][r]=='High'):
                count_vulnibm_iot_namecodeexecution_accesscom+=1
                count_vulnibm_iot_namecodeexecution_highaccesscom+=1
            elif(df_vulnibm_iot["x_xfe_cvss_access_complexity"][r]=='Low'):
                count_vulnibm_iot_namecodeexecution_accesscom+=1
                count_vulnibm_iot_namecodeexecution_lowaccesscom+=1
            elif(df_vulnibm_iot["x_xfe_cvss_access_complexity"][r]=='Medium'):
                count_vulnibm_iot_namecodeexecution_accesscom+=1
                count_vulnibm_iot_namecodeexecution_mediumaccesscom+=1
                                         
        elif('maninthemiddle' in aux_str):
        
            count_vulnibm_iot_namemaninthemiddle+=1
            if(df_vulnibm_iot["x_xfe_cvss_access_complexity"][r]=='High'):
                count_vulnibm_iot_namemaninthemiddle_accesscom+=1
                count_vulnibm_iot_namemaninthemiddle_highaccesscom+=1
            elif(df_vulnibm_iot["x_xfe_cvss_access_complexity"][r]=='Low'):
                count_vulnibm_iot_namemaninthemiddle_accesscom+=1
                count_vulnibm_iot_namemaninthemiddle_lowaccesscom+=1
            elif(df_vulnibm_iot["x_xfe_cvss_access_complexity"][r]=='Medium'):
                count_vulnibm_iot_namemaninthemiddle_accesscom+=1
                count_vulnibm_iot_namemaninthemiddle_mediumaccesscom+=1
                                         
        elif('SQLinjection' in aux_str):
        
            count_vulnibm_iot_namesqlinjection+=1
            if(df_vulnibm_iot["x_xfe_cvss_access_complexity"][r]=='High'):
                count_vulnibm_iot_namesqlinjection_accesscom+=1
                count_vulnibm_iot_namesqlinjection_highaccesscom+=1
            elif(df_vulnibm_iot["x_xfe_cvss_access_complexity"][r]=='Low'):
                count_vulnibm_iot_namesqlinjection_accesscom+=1
                count_vulnibm_iot_namesqlinjection_lowaccesscom+=1
            elif(df_vulnibm_iot["x_xfe_cvss_access_complexity"][r]=='Medium'):
                count_vulnibm_iot_namesqlinjection_accesscom+=1
                count_vulnibm_iot_namesqlinjection_mediumaccesscom+=1
                                         
        elif('cross-siterequestforgery' in aux_str):
        
            count_vulnibm_iot_namecrosssiterequestforgery+=1
            if(df_vulnibm_iot["x_xfe_cvss_access_complexity"][r]=='High'):
                count_vulnibm_iot_namecrosssiterequestforgery_accesscom+=1
                count_vulnibm_iot_namecrosssiterequestforgery_highaccesscom+=1
            elif(df_vulnibm_iot["x_xfe_cvss_access_complexity"][r]=='Low'):
                count_vulnibm_iot_namecrosssiterequestforgery_accesscom+=1
                count_vulnibm_iot_namecrosssiterequestforgery_lowaccesscom+=1
            elif(df_vulnibm_iot["x_xfe_cvss_access_complexity"][r]=='Medium'):
                count_vulnibm_iot_namecrosssiterequestforgery_accesscom+=1
                count_vulnibm_iot_namecrosssiterequestforgery_mediumaccesscom+=1
                                         
        elif('moduleexecution' in aux_str):
        
            count_vulnibm_iot_namemoduleexecution+=1
            if(df_vulnibm_iot["x_xfe_cvss_access_complexity"][r]=='High'):
                count_vulnibm_iot_namemoduleexecution_accesscom+=1
                count_vulnibm_iot_namemoduleexecution_highaccesscom+=1
            elif(df_vulnibm_iot["x_xfe_cvss_access_complexity"][r]=='Low'):
                count_vulnibm_iot_namemoduleexecution_accesscom+=1
                count_vulnibm_iot_namemoduleexecution_lowaccesscom+=1
            elif(df_vulnibm_iot["x_xfe_cvss_access_complexity"][r]=='Medium'):
                count_vulnibm_iot_namemoduleexecution_accesscom+=1
                count_vulnibm_iot_namemoduleexecution_mediumaccesscom+=1
                                         
        elif('bufferoverflow' in aux_str):
        
            count_vulnibm_iot_namebufferoverflow+=1
            if(df_vulnibm_iot["x_xfe_cvss_access_complexity"][r]=='High'):
                count_vulnibm_iot_namebufferoverflow_accesscom+=1
                count_vulnibm_iot_namebufferoverflow_highaccesscom+=1
            elif(df_vulnibm_iot["x_xfe_cvss_access_complexity"][r]=='Low'):
                count_vulnibm_iot_namebufferoverflow_accesscom+=1
                count_vulnibm_iot_namebufferoverflow_lowaccesscom+=1
            elif(df_vulnibm_iot["x_xfe_cvss_access_complexity"][r]=='Medium'):
                count_vulnibm_iot_namebufferoverflow_accesscom+=1
                count_vulnibm_iot_namebufferoverflow_mediumaccesscom+=1
                                         
        elif('commandexecution' in aux_str):
        
            count_vulnibm_iot_namecommandexecution+=1
            if(df_vulnibm_iot["x_xfe_cvss_access_complexity"][r]=='High'):
                count_vulnibm_iot_namecommandexecution_accesscom+=1
                count_vulnibm_iot_namecommandexecution_highaccesscom+=1
            elif(df_vulnibm_iot["x_xfe_cvss_access_complexity"][r]=='Low'):
                count_vulnibm_iot_namecommandexecution_accesscom+=1
                count_vulnibm_iot_namecommandexecution_lowaccesscom+=1
            elif(df_vulnibm_iot["x_xfe_cvss_access_complexity"][r]=='Medium'):
                count_vulnibm_iot_namecommandexecution_accesscom+=1
                count_vulnibm_iot_namecommandexecution_mediumaccesscom+=1
                                         
        elif('spoofing' in aux_str):
        
            count_vulnibm_iot_namespoofing+=1
            if(df_vulnibm_iot["x_xfe_cvss_access_complexity"][r]=='High'):
                count_vulnibm_iot_namespoofing_accesscom+=1
                count_vulnibm_iot_namespoofing_highaccesscom+=1
            elif(df_vulnibm_iot["x_xfe_cvss_access_complexity"][r]=='Low'):
                count_vulnibm_iot_namespoofing_accesscom+=1
                count_vulnibm_iot_namespoofing_lowaccesscom+=1
            elif(df_vulnibm_iot["x_xfe_cvss_access_complexity"][r]=='Medium'):
                count_vulnibm_iot_namespoofing_accesscom+=1
                count_vulnibm_iot_namespoofing_mediumaccesscom+=1
                                         
        elif('clickjacking' in aux_str):
        
            count_vulnibm_iot_nameclickjacking+=1
            if(df_vulnibm_iot["x_xfe_cvss_access_complexity"][r]=='High'):
                count_vulnibm_iot_nameclickjacking_accesscom+=1
                count_vulnibm_iot_nameclickjacking_highaccesscom+=1
            elif(df_vulnibm_iot["x_xfe_cvss_access_complexity"][r]=='Low'):
                count_vulnibm_iot_nameclickjacking_accesscom+=1
                count_vulnibm_iot_nameclickjacking_lowaccesscom+=1
            elif(df_vulnibm_iot["x_xfe_cvss_access_complexity"][r]=='Medium'):
                count_vulnibm_iot_nameclickjacking_accesscom+=1
                count_vulnibm_iot_nameclickjacking_mediumaccesscom+=1
              
        elif('hijacking' in aux_str):
        
            count_vulnibm_iot_namehijacking+=1
            if(df_vulnibm_iot["x_xfe_cvss_access_complexity"][r]=='High'):
                count_vulnibm_iot_namehijacking_accesscom+=1
                count_vulnibm_iot_namehijacking_highaccesscom+=1
            elif(df_vulnibm_iot["x_xfe_cvss_access_complexity"][r]=='Low'):
                count_vulnibm_iot_namehijacking_accesscom+=1
                count_vulnibm_iot_namehijacking_lowaccesscom+=1
            elif(df_vulnibm_iot["x_xfe_cvss_access_complexity"][r]=='Medium'):
                count_vulnibm_iot_namehijacking_accesscom+=1
                count_vulnibm_iot_namehijacking_mediumaccesscom+=1
               
        elif('fileinclude' in aux_str):
        
            count_vulnibm_iot_namefileinclude+=1
            if(df_vulnibm_iot["x_xfe_cvss_access_complexity"][r]=='High'):
                count_vulnibm_iot_namefileinclude_accesscom+=1
                count_vulnibm_iot_namefileinclude_highaccesscom+=1
            elif(df_vulnibm_iot["x_xfe_cvss_access_complexity"][r]=='Low'):
                count_vulnibm_iot_namefileinclude_accesscom+=1
                count_vulnibm_iot_namefileinclude_lowaccesscom+=1
            elif(df_vulnibm_iot["x_xfe_cvss_access_complexity"][r]=='Medium'):
                count_vulnibm_iot_namefileinclude_accesscom+=1
                count_vulnibm_iot_namefileinclude_mediumaccesscom+=1
                
               
        elif('bruteforce' in aux_str):
        
            count_vulnibm_iot_namebruteforce+=1
            if(df_vulnibm_iot["x_xfe_cvss_access_complexity"][r]=='High'):
                count_vulnibm_iot_namebruteforce_accesscom+=1
                count_vulnibm_iot_namebruteforce_highaccesscom+=1
            elif(df_vulnibm_iot["x_xfe_cvss_access_complexity"][r]=='Low'):
                count_vulnibm_iot_namebruteforce_accesscom+=1
                count_vulnibm_iot_namebruteforce_lowaccesscom+=1
            elif(df_vulnibm_iot["x_xfe_cvss_access_complexity"][r]=='Medium'):
                count_vulnibm_iot_namebruteforce_accesscom+=1
                count_vulnibm_iot_namebruteforce_mediumaccesscom+=1
                
               
        elif('fileupload' in aux_str):
        
            count_vulnibm_iot_namefileupload+=1
            if(df_vulnibm_iot["x_xfe_cvss_access_complexity"][r]=='High'):
                count_vulnibm_iot_namefileupload_accesscom+=1
                count_vulnibm_iot_namefileupload_highaccesscom+=1
            elif(df_vulnibm_iot["x_xfe_cvss_access_complexity"][r]=='Low'):
                count_vulnibm_iot_namefileupload_accesscom+=1
                count_vulnibm_iot_namefileupload_lowaccesscom+=1
            elif(df_vulnibm_iot["x_xfe_cvss_access_complexity"][r]=='Medium'):
                count_vulnibm_iot_namefileupload_accesscom+=1
                count_vulnibm_iot_namefileupload_mediumaccesscom+=1
                
               
        elif('headerinjection' in aux_str):
        
            count_vulnibm_iot_nameheaderinjection+=1
            if(df_vulnibm_iot["x_xfe_cvss_access_complexity"][r]=='High'):
                count_vulnibm_iot_nameheaderinjection_accesscom+=1
                count_vulnibm_iot_nameheaderinjection_highaccesscom+=1
            elif(df_vulnibm_iot["x_xfe_cvss_access_complexity"][r]=='Low'):
                count_vulnibm_iot_nameheaderinjection_accesscom+=1
                count_vulnibm_iot_nameheaderinjection_lowaccesscom+=1
            elif(df_vulnibm_iot["x_xfe_cvss_access_complexity"][r]=='Medium'):
                count_vulnibm_iot_nameheaderinjection_accesscom+=1
                count_vulnibm_iot_nameheaderinjection_mediumaccesscom+=1
               
        elif('Tampering' in aux_str):
        
            count_vulnibm_iot_nametampering+=1
            if(df_vulnibm_iot["x_xfe_cvss_access_complexity"][r]=='High'):
                count_vulnibm_iot_nametampering_accesscom+=1
                count_vulnibm_iot_nametampering_highaccesscom+=1
            elif(df_vulnibm_iot["x_xfe_cvss_access_complexity"][r]=='Low'):
                count_vulnibm_iot_nametampering_accesscom+=1
                count_vulnibm_iot_nametampering_lowaccesscom+=1
            elif(df_vulnibm_iot["x_xfe_cvss_access_complexity"][r]=='Medium'):
                count_vulnibm_iot_nametampering_accesscom+=1
                count_vulnibm_iot_nametampering_mediumaccesscom+=1
    
        else:
        
            count_vulnibm_iot_nameanother+=1
            if(df_vulnibm_iot["x_xfe_cvss_access_complexity"][r]=='High'):
                count_vulnibm_iot_nameanother_accesscom+=1
                count_vulnibm_iot_nameanother_highaccesscom+=1
            elif(df_vulnibm_iot["x_xfe_cvss_access_complexity"][r]=='Low'):
                count_vulnibm_iot_nameanother_accesscom+=1
                count_vulnibm_iot_nameanother_lowaccesscom+=1
            elif(df_vulnibm_iot["x_xfe_cvss_access_complexity"][r]=='Medium'):
                count_vulnibm_iot_nameanother_accesscom+=1
                count_vulnibm_iot_nameanother_mediumaccesscom+=1
                
                
                
                
                
print("************************ESTADÍSTICAS NOMBRE/COMPLEJIDAD DE ATAQUE VULNERABILIDADES IBM PARTE IOT************************")
print("\n")                            
print("\n")
print(" DE UN TOTAL DE "+str(count_vulnibm_iot_names)+" VULNERABILIDADES:\n") 
print("\n")
print("   - LAS ESTADISTICAS DE VALORES DE NOMBRE SON LAS SIGUIENTES:  \n")
print("      -    EN  "+str(count_vulnibm_iot_namepathtraversal)+" VULNERABILIDADES EL NOMBRE INCLUYE PATH TRAVERSAL, LAS ESTADÍSTICAS DE COMPLEJIDAD DE ATAQUE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_namepathtraversal_highaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
print("            -    EN  "+str(count_vulnibm_iot_namepathtraversal_lowaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
print("            -    EN  "+str(count_vulnibm_iot_namepathtraversal_mediumaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA\n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_namedirectorytraversal)+" VULNERABILIDADES EL NOMBRE INCLUYE DIRECTORY TRAVERSAL, LAS ESTADÍSTICAS DE COMPLEJIDAD DE ATAQUE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_namedirectorytraversal_highaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
print("            -    EN  "+str(count_vulnibm_iot_namedirectorytraversal_lowaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
print("            -    EN  "+str(count_vulnibm_iot_namedirectorytraversal_mediumaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA\n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_nameprivilegeescalation)+" VULNERABILIDADES EL NOMBRE INCLUYE PRIVILEGE ESCALATION, LAS ESTADÍSTICAS DE COMPLEJIDAD DE ATAQUE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_nameprivilegeescalation_highaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
print("            -    EN  "+str(count_vulnibm_iot_nameprivilegeescalation_lowaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
print("            -    EN  "+str(count_vulnibm_iot_nameprivilegeescalation_mediumaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA\n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_namecrosssitescripting)+" VULNERABILIDADES EL NOMBRE INCLUYE CROSS SITE SCRIPTING, LAS ESTADÍSTICAS DE COMPLEJIDAD DE ATAQUE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_namecrosssitescripting_highaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
print("            -    EN  "+str(count_vulnibm_iot_namecrosssitescripting_lowaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
print("            -    EN  "+str(count_vulnibm_iot_namecrosssitescripting_mediumaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA\n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_namesecuritybypass)+" VULNERABILIDADES EL NOMBRE INCLUYE SECURITY BYPASS, LAS ESTADÍSTICAS DE COMPLEJIDAD DE ATAQUE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_namesecuritybypass_highaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
print("            -    EN  "+str(count_vulnibm_iot_namesecuritybypass_lowaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
print("            -    EN  "+str(count_vulnibm_iot_namesecuritybypass_mediumaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA\n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_nameinformationdisclosure)+" VULNERABILIDADES EL NOMBRE INCLUYE INFORMATION DISCLOSURE, LAS ESTADÍSTICAS DE COMPLEJIDAD DE ATAQUE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_nameinformationdisclosure_highaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
print("            -    EN  "+str(count_vulnibm_iot_nameinformationdisclosure_lowaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
print("            -    EN  "+str(count_vulnibm_iot_nameinformationdisclosure_mediumaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA\n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_namedenialofservice)+" VULNERABILIDADES EL NOMBRE INCLUYE DENIAL OF SERVICE, LAS ESTADÍSTICAS DE COMPLEJIDAD DE ATAQUE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_namedenialofservice_highaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
print("            -    EN  "+str(count_vulnibm_iot_namedenialofservice_lowaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
print("            -    EN  "+str(count_vulnibm_iot_namedenialofservice_mediumaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA\n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_namecodeexecution)+" VULNERABILIDADES EL NOMBRE INCLUYE CODE EXECUTION, LAS ESTADÍSTICAS DE COMPLEJIDAD DE ATAQUE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_namecodeexecution_highaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
print("            -    EN  "+str(count_vulnibm_iot_namecodeexecution_lowaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
print("            -    EN  "+str(count_vulnibm_iot_namecodeexecution_mediumaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA\n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_namemaninthemiddle)+" VULNERABILIDADES EL NOMBRE INCLUYE MAN IN THE MIDDLE, LAS ESTADÍSTICAS DE COMPLEJIDAD DE ATAQUE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_namemaninthemiddle_highaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
print("            -    EN  "+str(count_vulnibm_iot_namemaninthemiddle_lowaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
print("            -    EN  "+str(count_vulnibm_iot_namemaninthemiddle_mediumaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA\n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_namesqlinjection)+" VULNERABILIDADES EL NOMBRE INCLUYE SQL INJECTION, LAS ESTADÍSTICAS DE COMPLEJIDAD DE ATAQUE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_namesqlinjection_highaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
print("            -    EN  "+str(count_vulnibm_iot_namesqlinjection_lowaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
print("            -    EN  "+str(count_vulnibm_iot_namesqlinjection_mediumaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA\n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_namecrosssiterequestforgery)+" VULNERABILIDADES EL NOMBRE INCLUYE CROSS SITE REQUEST FORGERY, LAS ESTADÍSTICAS DE COMPLEJIDAD DE ATAQUE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_namecrosssiterequestforgery_highaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
print("            -    EN  "+str(count_vulnibm_iot_namecrosssiterequestforgery_lowaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
print("            -    EN  "+str(count_vulnibm_iot_namecrosssiterequestforgery_mediumaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA\n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_namemoduleexecution)+" VULNERABILIDADES EL NOMBRE INCLUYE MODULE EXECUTION, LAS ESTADÍSTICAS DE COMPLEJIDAD DE ATAQUE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_namemoduleexecution_highaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
print("            -    EN  "+str(count_vulnibm_iot_namemoduleexecution_lowaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
print("            -    EN  "+str(count_vulnibm_iot_namemoduleexecution_mediumaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA\n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_namebufferoverflow)+" VULNERABILIDADES EL NOMBRE INCLUYE BUFFER OVERFLOW, LAS ESTADÍSTICAS DE COMPLEJIDAD DE ATAQUE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_namebufferoverflow_highaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
print("            -    EN  "+str(count_vulnibm_iot_namebufferoverflow_lowaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
print("            -    EN  "+str(count_vulnibm_iot_namebufferoverflow_mediumaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA\n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_namecommandexecution)+" VULNERABILIDADES EL NOMBRE INCLUYE COMMAND EXECUTION, LAS ESTADÍSTICAS DE COMPLEJIDAD DE ATAQUE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_namecommandexecution_highaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
print("            -    EN  "+str(count_vulnibm_iot_namecommandexecution_lowaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
print("            -    EN  "+str(count_vulnibm_iot_namecommandexecution_mediumaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA\n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_namespoofing)+" VULNERABILIDADES EL NOMBRE INCLUYE SPOOFING, LAS ESTADÍSTICAS DE COMPLEJIDAD DE ATAQUE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_namespoofing_highaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
print("            -    EN  "+str(count_vulnibm_iot_namespoofing_lowaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
print("            -    EN  "+str(count_vulnibm_iot_namespoofing_mediumaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA\n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_nameclickjacking)+" VULNERABILIDADES EL NOMBRE INCLUYE CLICKJACKING, LAS ESTADÍSTICAS DE COMPLEJIDAD DE ATAQUE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_nameclickjacking_highaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
print("            -    EN  "+str(count_vulnibm_iot_nameclickjacking_lowaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
print("            -    EN  "+str(count_vulnibm_iot_nameclickjacking_mediumaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA\n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_namehijacking)+" VULNERABILIDADES EL NOMBRE INCLUYE HIJACKING, LAS ESTADÍSTICAS DE COMPLEJIDAD DE ATAQUE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_namehijacking_highaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
print("            -    EN  "+str(count_vulnibm_iot_namehijacking_lowaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
print("            -    EN  "+str(count_vulnibm_iot_namehijacking_mediumaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA\n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_namefileinclude)+" VULNERABILIDADES EL NOMBRE INCLUYE FILEINCLUDE, LAS ESTADÍSTICAS DE COMPLEJIDAD DE ATAQUE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_namefileinclude_highaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
print("            -    EN  "+str(count_vulnibm_iot_namefileinclude_lowaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
print("            -    EN  "+str(count_vulnibm_iot_namefileinclude_mediumaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA\n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_namebruteforce)+" VULNERABILIDADES EL NOMBRE INCLUYE BRUTEFORCE, LAS ESTADÍSTICAS DE COMPLEJIDAD DE ATAQUE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_namebruteforce_highaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
print("            -    EN  "+str(count_vulnibm_iot_namebruteforce_lowaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
print("            -    EN  "+str(count_vulnibm_iot_namebruteforce_mediumaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA\n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_namefileupload)+" VULNERABILIDADES EL NOMBRE INCLUYE FILE UPLOAD, LAS ESTADÍSTICAS DE COMPLEJIDAD DE ATAQUE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_namefileupload_highaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
print("            -    EN  "+str(count_vulnibm_iot_namefileupload_lowaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
print("            -    EN  "+str(count_vulnibm_iot_namefileupload_mediumaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA\n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_nameheaderinjection)+" VULNERABILIDADES EL NOMBRE INCLUYE HEADER INJECTION, LAS ESTADÍSTICAS DE COMPLEJIDAD DE ATAQUE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_nameheaderinjection_highaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
print("            -    EN  "+str(count_vulnibm_iot_nameheaderinjection_lowaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
print("            -    EN  "+str(count_vulnibm_iot_nameheaderinjection_mediumaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA\n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_nametampering)+" VULNERABILIDADES EL NOMBRE INCLUYE TAMPERING, LAS ESTADÍSTICAS DE COMPLEJIDAD DE ATAQUE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_nametampering_highaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
print("            -    EN  "+str(count_vulnibm_iot_nametampering_lowaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
print("            -    EN  "+str(count_vulnibm_iot_nametampering_mediumaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA\n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_nameanother)+" VULNERABILIDADES EL NOMBRE INCLUYE OTRA CADENA, LAS ESTADÍSTICAS DE COMPLEJIDAD DE ATAQUE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_nameanother_highaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
print("            -    EN  "+str(count_vulnibm_iot_nameanother_lowaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
print("            -    EN  "+str(count_vulnibm_iot_nameanother_mediumaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA\n")
print("\n")





print("************************PORCENTAJE NOMBRE/COMPLEJIDAD DE ATAQUE VULNERABILIDADES IBM PARTE IOT************************")
print("\n")                            
print("\n")
print(" DE UN TOTAL DE "+str(count_vulnibm_iot_names)+" VULNERABILIDADES :\n") 
print("\n")
print("   - LOS PORCENTAJES DE VALORES DE NOMBRE SON LOS SIGUIENTES:  \n")
print("      -    EN EL  "+str(float(((count_vulnibm_iot_namepathtraversal*100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE PATH TRAVERSAL, LOS PORCENTAJES DE COMPLEJIDAD DE ATAQUE SON LOS SIGUIENTES :  \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namepathtraversal_highaccesscom*100)/count_vulnibm_iot_namepathtraversal)))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namepathtraversal_lowaccesscom*100)/count_vulnibm_iot_namepathtraversal)))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namepathtraversal_mediumaccesscom*100)/count_vulnibm_iot_namepathtraversal)))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA\n")
print("\n")
print("      -    EN EL  "+str(float(((count_vulnibm_iot_namedirectorytraversal*100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE DIRECTORY TRAVERSAL, LOS PORCENTAJES DE COMPLEJIDAD DE ATAQUE SON LOS SIGUIENTES :  \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namedirectorytraversal_highaccesscom*100)/count_vulnibm_iot_namedirectorytraversal)))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namedirectorytraversal_lowaccesscom*100)/count_vulnibm_iot_namedirectorytraversal)))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namedirectorytraversal_mediumaccesscom*100)/count_vulnibm_iot_namedirectorytraversal)))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA\n")
print("\n")
print("      -    EN EL  "+str(float(((count_vulnibm_iot_nameprivilegeescalation*100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE PRIVILEGE ESCALATION, LOS PORCENTAJES DE COMPLEJIDAD DE ATAQUE SON LOS SIGUIENTES :  \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_nameprivilegeescalation_highaccesscom*100)/count_vulnibm_iot_nameprivilegeescalation)))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_nameprivilegeescalation_lowaccesscom*100)/count_vulnibm_iot_nameprivilegeescalation)))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_nameprivilegeescalation_mediumaccesscom*100)/count_vulnibm_iot_nameprivilegeescalation)))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA\n")
print("\n")
print("      -    EN EL  "+str(float(((count_vulnibm_iot_namecrosssitescripting*100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE CROSS SITE SCRIPTING, LOS PORCENTAJES DE COMPLEJIDAD DE ATAQUE SON LOS SIGUIENTES :  \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namecrosssitescripting_highaccesscom*100)/count_vulnibm_iot_namecrosssitescripting)))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namecrosssitescripting_lowaccesscom*100)/count_vulnibm_iot_namecrosssitescripting)))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namecrosssitescripting_mediumaccesscom*100)/count_vulnibm_iot_namecrosssitescripting)))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA\n")
print("\n")
print("      -    EN EL  "+str(float(((count_vulnibm_iot_namesecuritybypass*100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE SECURITY BYPASS, LOS PORCENTAJES DE COMPLEJIDAD DE ATAQUE SON LOS SIGUIENTES :  \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namesecuritybypass_highaccesscom*100)/count_vulnibm_iot_namesecuritybypass)))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namesecuritybypass_lowaccesscom*100)/count_vulnibm_iot_namesecuritybypass)))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namesecuritybypass_mediumaccesscom*100)/count_vulnibm_iot_namesecuritybypass)))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA\n")
print("\n")
print("      -    EN EL  "+str(float(((count_vulnibm_iot_nameinformationdisclosure*100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE INFORMATION DISCLOSURE, LOS PORCENTAJES DE COMPLEJIDAD DE ATAQUE SON LOS SIGUIENTES :  \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_nameinformationdisclosure_highaccesscom*100)/count_vulnibm_iot_nameinformationdisclosure)))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_nameinformationdisclosure_lowaccesscom*100)/count_vulnibm_iot_nameinformationdisclosure)))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_nameinformationdisclosure_mediumaccesscom*100)/count_vulnibm_iot_nameinformationdisclosure)))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA\n")
print("\n")
print("      -    EN EL  "+str(float(((count_vulnibm_iot_namedenialofservice*100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE DENIAL OF SERVICE, LOS PORCENTAJES DE COMPLEJIDAD DE ATAQUE SON LOS SIGUIENTES :  \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namedenialofservice_highaccesscom*100)/count_vulnibm_iot_namedenialofservice)))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namedenialofservice_lowaccesscom*100)/count_vulnibm_iot_namedenialofservice)))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namedenialofservice_mediumaccesscom*100)/count_vulnibm_iot_namedenialofservice)))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA\n")
print("\n")
print("      -    EN EL  "+str(float(((count_vulnibm_iot_namecodeexecution*100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE CODE EXECUTION, LOS PORCENTAJES DE COMPLEJIDAD DE ATAQUE SON LOS SIGUIENTES :  \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namecodeexecution_highaccesscom*100)/count_vulnibm_iot_namecodeexecution)))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namecodeexecution_lowaccesscom*100)/count_vulnibm_iot_namecodeexecution)))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namecodeexecution_mediumaccesscom*100)/count_vulnibm_iot_namecodeexecution)))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA\n")
print("\n")
print("      -    EN EL  "+str(float(((count_vulnibm_iot_namemaninthemiddle*100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE MAN IN THE MIDDLE, LOS PORCENTAJES DE COMPLEJIDAD DE ATAQUE SON LOS SIGUIENTES :  \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namemaninthemiddle_highaccesscom*100)/count_vulnibm_iot_namemaninthemiddle)))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namemaninthemiddle_lowaccesscom*100)/count_vulnibm_iot_namemaninthemiddle)))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namemaninthemiddle_mediumaccesscom*100)/count_vulnibm_iot_namemaninthemiddle)))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA\n")
print("\n")
print("      -    EN EL  "+str(float(((count_vulnibm_iot_namesqlinjection*100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE SQL INJECTION, LOS PORCENTAJES DE COMPLEJIDAD DE ATAQUE SON LOS SIGUIENTES :  \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namesqlinjection_highaccesscom*100)/count_vulnibm_iot_namesqlinjection)))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namesqlinjection_lowaccesscom*100)/count_vulnibm_iot_namesqlinjection)))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namesqlinjection_mediumaccesscom*100)/count_vulnibm_iot_namesqlinjection)))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA\n")
print("\n")
print("      -    EN EL  "+str(float(((count_vulnibm_iot_namecrosssiterequestforgery*100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE CROSS SITE REQUEST FORGERY, LOS PORCENTAJES DE COMPLEJIDAD DE ATAQUE SON LOS SIGUIENTES :  \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namecrosssiterequestforgery_highaccesscom*100)/count_vulnibm_iot_namecrosssiterequestforgery)))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namecrosssiterequestforgery_lowaccesscom*100)/count_vulnibm_iot_namecrosssiterequestforgery)))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namecrosssiterequestforgery_mediumaccesscom*100)/count_vulnibm_iot_namecrosssiterequestforgery)))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA\n")
print("\n")
print("      -    EN EL  "+str(float(((count_vulnibm_iot_namemoduleexecution*100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE MODULE EXECUTION, LOS PORCENTAJES DE COMPLEJIDAD DE ATAQUE SON LOS SIGUIENTES :  \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namemoduleexecution_highaccesscom*100)/count_vulnibm_iot_namemoduleexecution)))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namemoduleexecution_lowaccesscom*100)/count_vulnibm_iot_namemoduleexecution)))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namemoduleexecution_mediumaccesscom*100)/count_vulnibm_iot_namemoduleexecution)))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA\n")
print("\n")
print("      -    EN EL  "+str(float(((count_vulnibm_iot_namebufferoverflow*100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE BUFFER OVERFLOW, LOS PORCENTAJES DE COMPLEJIDAD DE ATAQUE SON LOS SIGUIENTES :  \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namebufferoverflow_highaccesscom*100)/count_vulnibm_iot_namebufferoverflow)))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namebufferoverflow_lowaccesscom*100)/count_vulnibm_iot_namebufferoverflow)))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namebufferoverflow_mediumaccesscom*100)/count_vulnibm_iot_namebufferoverflow)))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA\n")
print("\n")
print("      -    EN EL  "+str(float(((count_vulnibm_iot_namecommandexecution*100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE COMMAND EXECUTION, LOS PORCENTAJES DE COMPLEJIDAD DE ATAQUE SON LOS SIGUIENTES :  \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namecommandexecution_highaccesscom*100)/count_vulnibm_iot_namecommandexecution)))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namecommandexecution_lowaccesscom*100)/count_vulnibm_iot_namecommandexecution)))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namecommandexecution_mediumaccesscom*100)/count_vulnibm_iot_namecommandexecution)))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA\n")
print("\n")
print("      -    EN EL  "+str(float(((count_vulnibm_iot_namespoofing*100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE SPOOFING, LOS PORCENTAJES DE COMPLEJIDAD DE ATAQUE SON LOS SIGUIENTES :  \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namespoofing_highaccesscom*100)/count_vulnibm_iot_namespoofing)))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namespoofing_lowaccesscom*100)/count_vulnibm_iot_namespoofing)))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namespoofing_mediumaccesscom*100)/count_vulnibm_iot_namespoofing)))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA\n")
print("\n")
print("      -    EN EL  "+str(float(((count_vulnibm_iot_nameclickjacking*100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE CLICKJACKING, LOS PORCENTAJES DE COMPLEJIDAD DE ATAQUE SON LOS SIGUIENTES :  \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_nameclickjacking_highaccesscom*100)/count_vulnibm_iot_nameclickjacking)))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_nameclickjacking_lowaccesscom*100)/count_vulnibm_iot_nameclickjacking)))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_nameclickjacking_mediumaccesscom*100)/count_vulnibm_iot_nameclickjacking)))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA\n")
print("\n")
print("      -    EN EL  "+str(float(((count_vulnibm_iot_namehijacking*100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE HIJACKING, LOS PORCENTAJES DE COMPLEJIDAD DE ATAQUE SON LOS SIGUIENTES :  \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namehijacking_highaccesscom*100)/count_vulnibm_iot_namehijacking)))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namehijacking_lowaccesscom*100)/count_vulnibm_iot_namehijacking)))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namehijacking_mediumaccesscom*100)/count_vulnibm_iot_namehijacking)))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA\n")
print("\n")
print("      -    EN EL  "+str(float(((count_vulnibm_iot_namefileinclude*100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE FILEINCLUDE, LOS PORCENTAJES DE COMPLEJIDAD DE ATAQUE SON LOS SIGUIENTES :  \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namefileinclude_highaccesscom*100)/count_vulnibm_iot_namefileinclude)))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namefileinclude_lowaccesscom*100)/count_vulnibm_iot_namefileinclude)))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namefileinclude_mediumaccesscom*100)/count_vulnibm_iot_namefileinclude)))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA\n")
print("\n")
print("      -    EN EL  "+str(float(((count_vulnibm_iot_namebruteforce*100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE BRUTEFORCE, LOS PORCENTAJES DE COMPLEJIDAD DE ATAQUE SON LOS SIGUIENTES :  \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namebruteforce_highaccesscom*100)/count_vulnibm_iot_namebruteforce)))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namebruteforce_lowaccesscom*100)/count_vulnibm_iot_namebruteforce)))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namebruteforce_mediumaccesscom*100)/count_vulnibm_iot_namebruteforce)))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA\n")
print("\n")
print("      -    EN EL  "+str(float(((count_vulnibm_iot_namefileupload*100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE FILE UPLOAD, LOS PORCENTAJES DE COMPLEJIDAD DE ATAQUE SON LOS SIGUIENTES :  \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namefileupload_highaccesscom*100)/count_vulnibm_iot_namefileupload)))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namefileupload_lowaccesscom*100)/count_vulnibm_iot_namefileupload)))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namefileupload_mediumaccesscom*100)/count_vulnibm_iot_namefileupload)))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA\n")
print("\n")
if(count_vulnibm_iot_nameheaderinjection>0):
    print("      -    EN EL  "+str(float(((count_vulnibm_iot_nameheaderinjection*100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE HEADER INJECTION, LOS PORCENTAJES DE COMPLEJIDAD DE ATAQUE SON LOS SIGUIENTES :  \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_nameheaderinjection_highaccesscom*100)/count_vulnibm_iot_nameheaderinjection)))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_nameheaderinjection_lowaccesscom*100)/count_vulnibm_iot_nameheaderinjection)))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_nameheaderinjection_mediumaccesscom*100)/count_vulnibm_iot_nameheaderinjection)))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA\n")
    print("\n")
if(count_vulnibm_iot_nametampering>0):
    print("      -    EN EL  "+str(float(((count_vulnibm_iot_nametampering*100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE TAMPERING, LOS PORCENTAJES DE COMPLEJIDAD DE ATAQUE SON LOS SIGUIENTES :  \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_nametampering_highaccesscom*100)/count_vulnibm_iot_nametampering)))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_nametampering_lowaccesscom*100)/count_vulnibm_iot_nametampering)))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_nametampering_mediumaccesscom*100)/count_vulnibm_iot_nametampering)))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA\n")
    print("\n")
    print("      -    EN EL  "+str(float(((count_vulnibm_iot_nameanother*100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE OTRA CADENA, LOS PORCENTAJES DE COMPLEJIDAD DE ATAQUE SON LOS SIGUIENTES :  \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_nameanother_highaccesscom*100)/count_vulnibm_iot_nameanother)))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_nameanother_lowaccesscom*100)/count_vulnibm_iot_nameanother)))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_nameanother_mediumaccesscom*100)/count_vulnibm_iot_nameanother)))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA\n")
    print("\n")




    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
import pandas as pd
from datetime import datetime,timedelta



#Abro los ficheros con los que voy a tratar




df_vulnibm_sh = pd.read_excel('vulnerabilidades_ibm_smart_home_2023.xlsx')

#Variable para almacenar el contador total de valores de nombres
count_vulnibm_sh_names=0
#Variable para almacenar el contador total de valores de un nombre especifico
count_vulnibm_sh_namepathtraversal=0
#Variable para almacenar el contador de valores de complejidad de ATAQUE dado un nombre especifico
count_vulnibm_sh_namepathtraversal_accesscom=0
count_vulnibm_sh_namepathtraversal_highaccesscom=0
count_vulnibm_sh_namepathtraversal_lowaccesscom=0
count_vulnibm_sh_namepathtraversal_mediumaccesscom=0

count_vulnibm_sh_namedirectorytraversal=0
count_vulnibm_sh_namedirectorytraversal_accesscom=0
count_vulnibm_sh_namedirectorytraversal_highaccesscom=0
count_vulnibm_sh_namedirectorytraversal_lowaccesscom=0
count_vulnibm_sh_namedirectorytraversal_mediumaccesscom=0

count_vulnibm_sh_nameprivilegeescalation=0
count_vulnibm_sh_nameprivilegeescalation_accesscom=0
count_vulnibm_sh_nameprivilegeescalation_highaccesscom=0
count_vulnibm_sh_nameprivilegeescalation_lowaccesscom=0
count_vulnibm_sh_nameprivilegeescalation_mediumaccesscom=0

count_vulnibm_sh_namecrosssitescripting=0
count_vulnibm_sh_namecrosssitescripting_accesscom=0
count_vulnibm_sh_namecrosssitescripting_highaccesscom=0
count_vulnibm_sh_namecrosssitescripting_lowaccesscom=0
count_vulnibm_sh_namecrosssitescripting_mediumaccesscom=0

count_vulnibm_sh_namesecuritybypass=0
count_vulnibm_sh_namesecuritybypass_accesscom=0
count_vulnibm_sh_namesecuritybypass_highaccesscom=0
count_vulnibm_sh_namesecuritybypass_lowaccesscom=0
count_vulnibm_sh_namesecuritybypass_mediumaccesscom=0

count_vulnibm_sh_nameinformationdisclosure=0
count_vulnibm_sh_nameinformationdisclosure_accesscom=0
count_vulnibm_sh_nameinformationdisclosure_highaccesscom=0
count_vulnibm_sh_nameinformationdisclosure_lowaccesscom=0
count_vulnibm_sh_nameinformationdisclosure_mediumaccesscom=0

count_vulnibm_sh_namedenialofservice=0
count_vulnibm_sh_namedenialofservice_accesscom=0
count_vulnibm_sh_namedenialofservice_highaccesscom=0
count_vulnibm_sh_namedenialofservice_lowaccesscom=0
count_vulnibm_sh_namedenialofservice_mediumaccesscom=0

count_vulnibm_sh_namecodeexecution=0
count_vulnibm_sh_namecodeexecution_accesscom=0
count_vulnibm_sh_namecodeexecution_highaccesscom=0
count_vulnibm_sh_namecodeexecution_lowaccesscom=0
count_vulnibm_sh_namecodeexecution_mediumaccesscom=0

count_vulnibm_sh_namemaninthemiddle=0
count_vulnibm_sh_namemaninthemiddle_accesscom=0
count_vulnibm_sh_namemaninthemiddle_highaccesscom=0
count_vulnibm_sh_namemaninthemiddle_lowaccesscom=0
count_vulnibm_sh_namemaninthemiddle_mediumaccesscom=0

count_vulnibm_sh_namesqlinjection=0
count_vulnibm_sh_namesqlinjection_accesscom=0
count_vulnibm_sh_namesqlinjection_highaccesscom=0
count_vulnibm_sh_namesqlinjection_lowaccesscom=0
count_vulnibm_sh_namesqlinjection_mediumaccesscom=0

count_vulnibm_sh_namecrosssiterequestforgery=0
count_vulnibm_sh_namecrosssiterequestforgery_accesscom=0
count_vulnibm_sh_namecrosssiterequestforgery_highaccesscom=0
count_vulnibm_sh_namecrosssiterequestforgery_lowaccesscom=0
count_vulnibm_sh_namecrosssiterequestforgery_mediumaccesscom=0

count_vulnibm_sh_namemoduleexecution=0
count_vulnibm_sh_namemoduleexecution_accesscom=0
count_vulnibm_sh_namemoduleexecution_highaccesscom=0
count_vulnibm_sh_namemoduleexecution_lowaccesscom=0
count_vulnibm_sh_namemoduleexecution_mediumaccesscom=0

count_vulnibm_sh_namebufferoverflow=0
count_vulnibm_sh_namebufferoverflow_accesscom=0
count_vulnibm_sh_namebufferoverflow_highaccesscom=0
count_vulnibm_sh_namebufferoverflow_lowaccesscom=0
count_vulnibm_sh_namebufferoverflow_mediumaccesscom=0

count_vulnibm_sh_namecommandexecution=0
count_vulnibm_sh_namecommandexecution_accesscom=0
count_vulnibm_sh_namecommandexecution_highaccesscom=0
count_vulnibm_sh_namecommandexecution_lowaccesscom=0
count_vulnibm_sh_namecommandexecution_mediumaccesscom=0

count_vulnibm_sh_namespoofing=0
count_vulnibm_sh_namespoofing_accesscom=0
count_vulnibm_sh_namespoofing_highaccesscom=0
count_vulnibm_sh_namespoofing_lowaccesscom=0
count_vulnibm_sh_namespoofing_mediumaccesscom=0

count_vulnibm_sh_nameclickjacking=0
count_vulnibm_sh_nameclickjacking_accesscom=0
count_vulnibm_sh_nameclickjacking_highaccesscom=0
count_vulnibm_sh_nameclickjacking_lowaccesscom=0
count_vulnibm_sh_nameclickjacking_mediumaccesscom=0

count_vulnibm_sh_namehijacking=0
count_vulnibm_sh_namehijacking_accesscom=0
count_vulnibm_sh_namehijacking_highaccesscom=0
count_vulnibm_sh_namehijacking_lowaccesscom=0
count_vulnibm_sh_namehijacking_mediumaccesscom=0

count_vulnibm_sh_namefileinclude=0
count_vulnibm_sh_namefileinclude_accesscom=0
count_vulnibm_sh_namefileinclude_highaccesscom=0
count_vulnibm_sh_namefileinclude_lowaccesscom=0
count_vulnibm_sh_namefileinclude_mediumaccesscom=0

count_vulnibm_sh_namebruteforce=0
count_vulnibm_sh_namebruteforce_accesscom=0
count_vulnibm_sh_namebruteforce_highaccesscom=0
count_vulnibm_sh_namebruteforce_lowaccesscom=0
count_vulnibm_sh_namebruteforce_mediumaccesscom=0

count_vulnibm_sh_namefileupload=0
count_vulnibm_sh_namefileupload_accesscom=0
count_vulnibm_sh_namefileupload_highaccesscom=0
count_vulnibm_sh_namefileupload_lowaccesscom=0
count_vulnibm_sh_namefileupload_mediumaccesscom=0

count_vulnibm_sh_nameheaderinjection=0
count_vulnibm_sh_nameheaderinjection_accesscom=0
count_vulnibm_sh_nameheaderinjection_highaccesscom=0
count_vulnibm_sh_nameheaderinjection_lowaccesscom=0
count_vulnibm_sh_nameheaderinjection_mediumaccesscom=0

count_vulnibm_sh_nametampering=0
count_vulnibm_sh_nametampering_accesscom=0
count_vulnibm_sh_nametampering_highaccesscom=0
count_vulnibm_sh_nametampering_lowaccesscom=0
count_vulnibm_sh_nametampering_mediumaccesscom=0

count_vulnibm_sh_nameanother=0
count_vulnibm_sh_nameanother_accesscom=0
count_vulnibm_sh_nameanother_highaccesscom=0
count_vulnibm_sh_nameanother_lowaccesscom=0
count_vulnibm_sh_nameanother_mediumaccesscom=0

#Comprobamos el contenido de name
for r in range(0,len(df_vulnibm_sh["name"])):                       
    aux_str=df_vulnibm_sh["name"][r].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
    if(aux_str!='NONE'):
        count_vulnibm_sh_names+=1
        #Compruebo el valor de name
        if('pathtraversal' in aux_str):
            count_vulnibm_sh_namepathtraversal+=1
            #Compruebo el valor de complejidad de ATAQUE
            if(df_vulnibm_sh["x_xfe_cvss_access_complexity"][r]=='High'):
                count_vulnibm_sh_namepathtraversal_accesscom+=1
                count_vulnibm_sh_namepathtraversal_highaccesscom+=1
            elif(df_vulnibm_sh["x_xfe_cvss_access_complexity"][r]=='Low'):
                count_vulnibm_sh_namepathtraversal_accesscom+=1
                count_vulnibm_sh_namepathtraversal_lowaccesscom+=1
            elif(df_vulnibm_sh["x_xfe_cvss_access_complexity"][r]=='Medium'):
                count_vulnibm_sh_namepathtraversal_accesscom+=1
                count_vulnibm_sh_namepathtraversal_mediumaccesscom+=1
    
        elif('directorytraversal' in aux_str):
            
            count_vulnibm_sh_namedirectorytraversal+=1
            if(df_vulnibm_sh["x_xfe_cvss_access_complexity"][r]=='High'):
                count_vulnibm_sh_namedirectorytraversal_accesscom+=1
                count_vulnibm_sh_namedirectorytraversal_highaccesscom+=1
            elif(df_vulnibm_sh["x_xfe_cvss_access_complexity"][r]=='Low'):
                count_vulnibm_sh_namedirectorytraversal_accesscom+=1
                count_vulnibm_sh_namedirectorytraversal_lowaccesscom+=1
            elif(df_vulnibm_sh["x_xfe_cvss_access_complexity"][r]=='Medium'):
                count_vulnibm_sh_namedirectorytraversal_accesscom+=1
                count_vulnibm_sh_namedirectorytraversal_mediumaccesscom+=1
            
            
        elif('privilegeescalation' in aux_str):
        
            count_vulnibm_sh_nameprivilegeescalation+=1
            if(df_vulnibm_sh["x_xfe_cvss_access_complexity"][r]=='High'):
                count_vulnibm_sh_nameprivilegeescalation_accesscom+=1
                count_vulnibm_sh_nameprivilegeescalation_highaccesscom+=1
            elif(df_vulnibm_sh["x_xfe_cvss_access_complexity"][r]=='Low'):
                count_vulnibm_sh_nameprivilegeescalation_accesscom+=1
                count_vulnibm_sh_nameprivilegeescalation_lowaccesscom+=1
            elif(df_vulnibm_sh["x_xfe_cvss_access_complexity"][r]=='Medium'):
                count_vulnibm_sh_nameprivilegeescalation_accesscom+=1
                count_vulnibm_sh_nameprivilegeescalation_mediumaccesscom+=1
            
        elif('cross-sitescripting' in aux_str):
        
            count_vulnibm_sh_namecrosssitescripting+=1
            if(df_vulnibm_sh["x_xfe_cvss_access_complexity"][r]=='High'):
                count_vulnibm_sh_namecrosssitescripting_accesscom+=1
                count_vulnibm_sh_namecrosssitescripting_highaccesscom+=1
            elif(df_vulnibm_sh["x_xfe_cvss_access_complexity"][r]=='Low'):
                count_vulnibm_sh_namecrosssitescripting_accesscom+=1
                count_vulnibm_sh_namecrosssitescripting_lowaccesscom+=1
            elif(df_vulnibm_sh["x_xfe_cvss_access_complexity"][r]=='Medium'):
                count_vulnibm_sh_namecrosssitescripting_accesscom+=1
                count_vulnibm_sh_namecrosssitescripting_mediumaccesscom+=1
                                         
        elif('securitybypass' in aux_str):
        
            count_vulnibm_sh_namesecuritybypass+=1
            if(df_vulnibm_sh["x_xfe_cvss_access_complexity"][r]=='High'):
                count_vulnibm_sh_namesecuritybypass_accesscom+=1
                count_vulnibm_sh_namesecuritybypass_highaccesscom+=1
            elif(df_vulnibm_sh["x_xfe_cvss_access_complexity"][r]=='Low'):
                count_vulnibm_sh_namesecuritybypass_accesscom+=1
                count_vulnibm_sh_namesecuritybypass_lowaccesscom+=1
            elif(df_vulnibm_sh["x_xfe_cvss_access_complexity"][r]=='Medium'):
                count_vulnibm_sh_namesecuritybypass_accesscom+=1
                count_vulnibm_sh_namesecuritybypass_mediumaccesscom+=1
                                         
        elif('information_disclosure' in aux_str or 'informationdisclosure' in aux_str):
        
            count_vulnibm_sh_nameinformationdisclosure+=1
            if(df_vulnibm_sh["x_xfe_cvss_access_complexity"][r]=='High'):
                count_vulnibm_sh_nameinformationdisclosure_accesscom+=1
                count_vulnibm_sh_nameinformationdisclosure_highaccesscom+=1
            elif(df_vulnibm_sh["x_xfe_cvss_access_complexity"][r]=='Low'):
                count_vulnibm_sh_nameinformationdisclosure_accesscom+=1
                count_vulnibm_sh_nameinformationdisclosure_lowaccesscom+=1
            elif(df_vulnibm_sh["x_xfe_cvss_access_complexity"][r]=='Medium'):
                count_vulnibm_sh_nameinformationdisclosure_accesscom+=1
                count_vulnibm_sh_nameinformationdisclosure_mediumaccesscom+=1
                                         
        elif('denialofservice' in aux_str):
            
            count_vulnibm_sh_namedenialofservice+=1
            if(df_vulnibm_sh["x_xfe_cvss_access_complexity"][r]=='High'):
                count_vulnibm_sh_namedenialofservice_accesscom+=1
                count_vulnibm_sh_namedenialofservice_highaccesscom+=1
            elif(df_vulnibm_sh["x_xfe_cvss_access_complexity"][r]=='Low'):
                count_vulnibm_sh_namedenialofservice_accesscom+=1
                count_vulnibm_sh_namedenialofservice_lowaccesscom+=1
            elif(df_vulnibm_sh["x_xfe_cvss_access_complexity"][r]=='Medium'):
                count_vulnibm_sh_namedenialofservice_accesscom+=1
                count_vulnibm_sh_namedenialofservice_mediumaccesscom+=1
            
        elif('codeexecution' in aux_str):
        
        
            count_vulnibm_sh_namecodeexecution+=1
            if(df_vulnibm_sh["x_xfe_cvss_access_complexity"][r]=='High'):
                count_vulnibm_sh_namecodeexecution_accesscom+=1
                count_vulnibm_sh_namecodeexecution_highaccesscom+=1
            elif(df_vulnibm_sh["x_xfe_cvss_access_complexity"][r]=='Low'):
                count_vulnibm_sh_namecodeexecution_accesscom+=1
                count_vulnibm_sh_namecodeexecution_lowaccesscom+=1
            elif(df_vulnibm_sh["x_xfe_cvss_access_complexity"][r]=='Medium'):
                count_vulnibm_sh_namecodeexecution_accesscom+=1
                count_vulnibm_sh_namecodeexecution_mediumaccesscom+=1
                                         
        elif('maninthemiddle' in aux_str):
        
            count_vulnibm_sh_namemaninthemiddle+=1
            if(df_vulnibm_sh["x_xfe_cvss_access_complexity"][r]=='High'):
                count_vulnibm_sh_namemaninthemiddle_accesscom+=1
                count_vulnibm_sh_namemaninthemiddle_highaccesscom+=1
            elif(df_vulnibm_sh["x_xfe_cvss_access_complexity"][r]=='Low'):
                count_vulnibm_sh_namemaninthemiddle_accesscom+=1
                count_vulnibm_sh_namemaninthemiddle_lowaccesscom+=1
            elif(df_vulnibm_sh["x_xfe_cvss_access_complexity"][r]=='Medium'):
                count_vulnibm_sh_namemaninthemiddle_accesscom+=1
                count_vulnibm_sh_namemaninthemiddle_mediumaccesscom+=1
                                         
        elif('SQLinjection' in aux_str):
        
            count_vulnibm_sh_namesqlinjection+=1
            if(df_vulnibm_sh["x_xfe_cvss_access_complexity"][r]=='High'):
                count_vulnibm_sh_namesqlinjection_accesscom+=1
                count_vulnibm_sh_namesqlinjection_highaccesscom+=1
            elif(df_vulnibm_sh["x_xfe_cvss_access_complexity"][r]=='Low'):
                count_vulnibm_sh_namesqlinjection_accesscom+=1
                count_vulnibm_sh_namesqlinjection_lowaccesscom+=1
            elif(df_vulnibm_sh["x_xfe_cvss_access_complexity"][r]=='Medium'):
                count_vulnibm_sh_namesqlinjection_accesscom+=1
                count_vulnibm_sh_namesqlinjection_mediumaccesscom+=1
                                         
        elif('cross-siterequestforgery' in aux_str):
        
            count_vulnibm_sh_namecrosssiterequestforgery+=1
            if(df_vulnibm_sh["x_xfe_cvss_access_complexity"][r]=='High'):
                count_vulnibm_sh_namecrosssiterequestforgery_accesscom+=1
                count_vulnibm_sh_namecrosssiterequestforgery_highaccesscom+=1
            elif(df_vulnibm_sh["x_xfe_cvss_access_complexity"][r]=='Low'):
                count_vulnibm_sh_namecrosssiterequestforgery_accesscom+=1
                count_vulnibm_sh_namecrosssiterequestforgery_lowaccesscom+=1
            elif(df_vulnibm_sh["x_xfe_cvss_access_complexity"][r]=='Medium'):
                count_vulnibm_sh_namecrosssiterequestforgery_accesscom+=1
                count_vulnibm_sh_namecrosssiterequestforgery_mediumaccesscom+=1
                                         
        elif('moduleexecution' in aux_str):
        
            count_vulnibm_sh_namemoduleexecution+=1
            if(df_vulnibm_sh["x_xfe_cvss_access_complexity"][r]=='High'):
                count_vulnibm_sh_namemoduleexecution_accesscom+=1
                count_vulnibm_sh_namemoduleexecution_highaccesscom+=1
            elif(df_vulnibm_sh["x_xfe_cvss_access_complexity"][r]=='Low'):
                count_vulnibm_sh_namemoduleexecution_accesscom+=1
                count_vulnibm_sh_namemoduleexecution_lowaccesscom+=1
            elif(df_vulnibm_sh["x_xfe_cvss_access_complexity"][r]=='Medium'):
                count_vulnibm_sh_namemoduleexecution_accesscom+=1
                count_vulnibm_sh_namemoduleexecution_mediumaccesscom+=1
                                         
        elif('bufferoverflow' in aux_str):
        
            count_vulnibm_sh_namebufferoverflow+=1
            if(df_vulnibm_sh["x_xfe_cvss_access_complexity"][r]=='High'):
                count_vulnibm_sh_namebufferoverflow_accesscom+=1
                count_vulnibm_sh_namebufferoverflow_highaccesscom+=1
            elif(df_vulnibm_sh["x_xfe_cvss_access_complexity"][r]=='Low'):
                count_vulnibm_sh_namebufferoverflow_accesscom+=1
                count_vulnibm_sh_namebufferoverflow_lowaccesscom+=1
            elif(df_vulnibm_sh["x_xfe_cvss_access_complexity"][r]=='Medium'):
                count_vulnibm_sh_namebufferoverflow_accesscom+=1
                count_vulnibm_sh_namebufferoverflow_mediumaccesscom+=1
                                         
        elif('commandexecution' in aux_str):
        
            count_vulnibm_sh_namecommandexecution+=1
            if(df_vulnibm_sh["x_xfe_cvss_access_complexity"][r]=='High'):
                count_vulnibm_sh_namecommandexecution_accesscom+=1
                count_vulnibm_sh_namecommandexecution_highaccesscom+=1
            elif(df_vulnibm_sh["x_xfe_cvss_access_complexity"][r]=='Low'):
                count_vulnibm_sh_namecommandexecution_accesscom+=1
                count_vulnibm_sh_namecommandexecution_lowaccesscom+=1
            elif(df_vulnibm_sh["x_xfe_cvss_access_complexity"][r]=='Medium'):
                count_vulnibm_sh_namecommandexecution_accesscom+=1
                count_vulnibm_sh_namecommandexecution_mediumaccesscom+=1
                                         
        elif('spoofing' in aux_str):
        
            count_vulnibm_sh_namespoofing+=1
            if(df_vulnibm_sh["x_xfe_cvss_access_complexity"][r]=='High'):
                count_vulnibm_sh_namespoofing_accesscom+=1
                count_vulnibm_sh_namespoofing_highaccesscom+=1
            elif(df_vulnibm_sh["x_xfe_cvss_access_complexity"][r]=='Low'):
                count_vulnibm_sh_namespoofing_accesscom+=1
                count_vulnibm_sh_namespoofing_lowaccesscom+=1
            elif(df_vulnibm_sh["x_xfe_cvss_access_complexity"][r]=='Medium'):
                count_vulnibm_sh_namespoofing_accesscom+=1
                count_vulnibm_sh_namespoofing_mediumaccesscom+=1
                                         
        elif('clickjacking' in aux_str):
        
            count_vulnibm_sh_nameclickjacking+=1
            if(df_vulnibm_sh["x_xfe_cvss_access_complexity"][r]=='High'):
                count_vulnibm_sh_nameclickjacking_accesscom+=1
                count_vulnibm_sh_nameclickjacking_highaccesscom+=1
            elif(df_vulnibm_sh["x_xfe_cvss_access_complexity"][r]=='Low'):
                count_vulnibm_sh_nameclickjacking_accesscom+=1
                count_vulnibm_sh_nameclickjacking_lowaccesscom+=1
            elif(df_vulnibm_sh["x_xfe_cvss_access_complexity"][r]=='Medium'):
                count_vulnibm_sh_nameclickjacking_accesscom+=1
                count_vulnibm_sh_nameclickjacking_mediumaccesscom+=1
              
        elif('hijacking' in aux_str):
        
            count_vulnibm_sh_namehijacking+=1
            if(df_vulnibm_sh["x_xfe_cvss_access_complexity"][r]=='High'):
                count_vulnibm_sh_namehijacking_accesscom+=1
                count_vulnibm_sh_namehijacking_highaccesscom+=1
            elif(df_vulnibm_sh["x_xfe_cvss_access_complexity"][r]=='Low'):
                count_vulnibm_sh_namehijacking_accesscom+=1
                count_vulnibm_sh_namehijacking_lowaccesscom+=1
            elif(df_vulnibm_sh["x_xfe_cvss_access_complexity"][r]=='Medium'):
                count_vulnibm_sh_namehijacking_accesscom+=1
                count_vulnibm_sh_namehijacking_mediumaccesscom+=1
               
        elif('fileinclude' in aux_str):
        
            count_vulnibm_sh_namefileinclude+=1
            if(df_vulnibm_sh["x_xfe_cvss_access_complexity"][r]=='High'):
                count_vulnibm_sh_namefileinclude_accesscom+=1
                count_vulnibm_sh_namefileinclude_highaccesscom+=1
            elif(df_vulnibm_sh["x_xfe_cvss_access_complexity"][r]=='Low'):
                count_vulnibm_sh_namefileinclude_accesscom+=1
                count_vulnibm_sh_namefileinclude_lowaccesscom+=1
            elif(df_vulnibm_sh["x_xfe_cvss_access_complexity"][r]=='Medium'):
                count_vulnibm_sh_namefileinclude_accesscom+=1
                count_vulnibm_sh_namefileinclude_mediumaccesscom+=1
                
               
        elif('bruteforce' in aux_str):
        
            count_vulnibm_sh_namebruteforce+=1
            if(df_vulnibm_sh["x_xfe_cvss_access_complexity"][r]=='High'):
                count_vulnibm_sh_namebruteforce_accesscom+=1
                count_vulnibm_sh_namebruteforce_highaccesscom+=1
            elif(df_vulnibm_sh["x_xfe_cvss_access_complexity"][r]=='Low'):
                count_vulnibm_sh_namebruteforce_accesscom+=1
                count_vulnibm_sh_namebruteforce_lowaccesscom+=1
            elif(df_vulnibm_sh["x_xfe_cvss_access_complexity"][r]=='Medium'):
                count_vulnibm_sh_namebruteforce_accesscom+=1
                count_vulnibm_sh_namebruteforce_mediumaccesscom+=1
                
               
        elif('fileupload' in aux_str):
        
            count_vulnibm_sh_namefileupload+=1
            if(df_vulnibm_sh["x_xfe_cvss_access_complexity"][r]=='High'):
                count_vulnibm_sh_namefileupload_accesscom+=1
                count_vulnibm_sh_namefileupload_highaccesscom+=1
            elif(df_vulnibm_sh["x_xfe_cvss_access_complexity"][r]=='Low'):
                count_vulnibm_sh_namefileupload_accesscom+=1
                count_vulnibm_sh_namefileupload_lowaccesscom+=1
            elif(df_vulnibm_sh["x_xfe_cvss_access_complexity"][r]=='Medium'):
                count_vulnibm_sh_namefileupload_accesscom+=1
                count_vulnibm_sh_namefileupload_mediumaccesscom+=1
                
               
        elif('headerinjection' in aux_str):
        
            count_vulnibm_sh_nameheaderinjection+=1
            if(df_vulnibm_sh["x_xfe_cvss_access_complexity"][r]=='High'):
                count_vulnibm_sh_nameheaderinjection_accesscom+=1
                count_vulnibm_sh_nameheaderinjection_highaccesscom+=1
            elif(df_vulnibm_sh["x_xfe_cvss_access_complexity"][r]=='Low'):
                count_vulnibm_sh_nameheaderinjection_accesscom+=1
                count_vulnibm_sh_nameheaderinjection_lowaccesscom+=1
            elif(df_vulnibm_sh["x_xfe_cvss_access_complexity"][r]=='Medium'):
                count_vulnibm_sh_nameheaderinjection_accesscom+=1
                count_vulnibm_sh_nameheaderinjection_mediumaccesscom+=1
               
        elif('Tampering' in aux_str):
        
            count_vulnibm_sh_nametampering+=1
            if(df_vulnibm_sh["x_xfe_cvss_access_complexity"][r]=='High'):
                count_vulnibm_sh_nametampering_accesscom+=1
                count_vulnibm_sh_nametampering_highaccesscom+=1
            elif(df_vulnibm_sh["x_xfe_cvss_access_complexity"][r]=='Low'):
                count_vulnibm_sh_nametampering_accesscom+=1
                count_vulnibm_sh_nametampering_lowaccesscom+=1
            elif(df_vulnibm_sh["x_xfe_cvss_access_complexity"][r]=='Medium'):
                count_vulnibm_sh_nametampering_accesscom+=1
                count_vulnibm_sh_nametampering_mediumaccesscom+=1
    
        else:
        
            count_vulnibm_sh_nameanother+=1
            if(df_vulnibm_sh["x_xfe_cvss_access_complexity"][r]=='High'):
                count_vulnibm_sh_nameanother_accesscom+=1
                count_vulnibm_sh_nameanother_highaccesscom+=1
            elif(df_vulnibm_sh["x_xfe_cvss_access_complexity"][r]=='Low'):
                count_vulnibm_sh_nameanother_accesscom+=1
                count_vulnibm_sh_nameanother_lowaccesscom+=1
            elif(df_vulnibm_sh["x_xfe_cvss_access_complexity"][r]=='Medium'):
                count_vulnibm_sh_nameanother_accesscom+=1
                count_vulnibm_sh_nameanother_mediumaccesscom+=1
                
                
                
                
                
print("************************ESTADÍSTICAS NOMBRE/COMPLEJIDAD DE ATAQUE VULNERABILIDADES IBM PARTE SMART HOME************************")
print("\n")                            
print("\n")
print(" DE UN TOTAL DE "+str(count_vulnibm_sh_names)+" VULNERABILIDADES:\n") 
print("\n")
print("   - LAS ESTADISTICAS DE VALORES DE NOMBRE SON LAS SIGUIENTES:  \n")
print("      -    EN  "+str(count_vulnibm_sh_namepathtraversal)+" VULNERABILIDADES EL NOMBRE INCLUYE PATH TRAVERSAL, LAS ESTADÍSTICAS DE COMPLEJIDAD DE ATAQUE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_sh_namepathtraversal_highaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
print("            -    EN  "+str(count_vulnibm_sh_namepathtraversal_lowaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
print("            -    EN  "+str(count_vulnibm_sh_namepathtraversal_mediumaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA\n")
print("\n")
print("      -    EN  "+str(count_vulnibm_sh_namedirectorytraversal)+" VULNERABILIDADES EL NOMBRE INCLUYE DIRECTORY TRAVERSAL, LAS ESTADÍSTICAS DE COMPLEJIDAD DE ATAQUE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_sh_namedirectorytraversal_highaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
print("            -    EN  "+str(count_vulnibm_sh_namedirectorytraversal_lowaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
print("            -    EN  "+str(count_vulnibm_sh_namedirectorytraversal_mediumaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA\n")
print("\n")
print("      -    EN  "+str(count_vulnibm_sh_nameprivilegeescalation)+" VULNERABILIDADES EL NOMBRE INCLUYE PRIVILEGE ESCALATION, LAS ESTADÍSTICAS DE COMPLEJIDAD DE ATAQUE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_sh_nameprivilegeescalation_highaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
print("            -    EN  "+str(count_vulnibm_sh_nameprivilegeescalation_lowaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
print("            -    EN  "+str(count_vulnibm_sh_nameprivilegeescalation_mediumaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA\n")
print("\n")
print("      -    EN  "+str(count_vulnibm_sh_namecrosssitescripting)+" VULNERABILIDADES EL NOMBRE INCLUYE CROSS SITE SCRIPTING, LAS ESTADÍSTICAS DE COMPLEJIDAD DE ATAQUE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_sh_namecrosssitescripting_highaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
print("            -    EN  "+str(count_vulnibm_sh_namecrosssitescripting_lowaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
print("            -    EN  "+str(count_vulnibm_sh_namecrosssitescripting_mediumaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA\n")
print("\n")
print("      -    EN  "+str(count_vulnibm_sh_namesecuritybypass)+" VULNERABILIDADES EL NOMBRE INCLUYE SECURITY BYPASS, LAS ESTADÍSTICAS DE COMPLEJIDAD DE ATAQUE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_sh_namesecuritybypass_highaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
print("            -    EN  "+str(count_vulnibm_sh_namesecuritybypass_lowaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
print("            -    EN  "+str(count_vulnibm_sh_namesecuritybypass_mediumaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA\n")
print("\n")
print("      -    EN  "+str(count_vulnibm_sh_nameinformationdisclosure)+" VULNERABILIDADES EL NOMBRE INCLUYE INFORMATION DISCLOSURE, LAS ESTADÍSTICAS DE COMPLEJIDAD DE ATAQUE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_sh_nameinformationdisclosure_highaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
print("            -    EN  "+str(count_vulnibm_sh_nameinformationdisclosure_lowaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
print("            -    EN  "+str(count_vulnibm_sh_nameinformationdisclosure_mediumaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA\n")
print("\n")
print("      -    EN  "+str(count_vulnibm_sh_namedenialofservice)+" VULNERABILIDADES EL NOMBRE INCLUYE DENIAL OF SERVICE, LAS ESTADÍSTICAS DE COMPLEJIDAD DE ATAQUE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_sh_namedenialofservice_highaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
print("            -    EN  "+str(count_vulnibm_sh_namedenialofservice_lowaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
print("            -    EN  "+str(count_vulnibm_sh_namedenialofservice_mediumaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA\n")
print("\n")
print("      -    EN  "+str(count_vulnibm_sh_namecodeexecution)+" VULNERABILIDADES EL NOMBRE INCLUYE CODE EXECUTION, LAS ESTADÍSTICAS DE COMPLEJIDAD DE ATAQUE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_sh_namecodeexecution_highaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
print("            -    EN  "+str(count_vulnibm_sh_namecodeexecution_lowaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
print("            -    EN  "+str(count_vulnibm_sh_namecodeexecution_mediumaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA\n")
print("\n")
print("      -    EN  "+str(count_vulnibm_sh_namemaninthemiddle)+" VULNERABILIDADES EL NOMBRE INCLUYE MAN IN THE MIDDLE, LAS ESTADÍSTICAS DE COMPLEJIDAD DE ATAQUE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_sh_namemaninthemiddle_highaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
print("            -    EN  "+str(count_vulnibm_sh_namemaninthemiddle_lowaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
print("            -    EN  "+str(count_vulnibm_sh_namemaninthemiddle_mediumaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA\n")
print("\n")
print("      -    EN  "+str(count_vulnibm_sh_namesqlinjection)+" VULNERABILIDADES EL NOMBRE INCLUYE SQL INJECTION, LAS ESTADÍSTICAS DE COMPLEJIDAD DE ATAQUE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_sh_namesqlinjection_highaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
print("            -    EN  "+str(count_vulnibm_sh_namesqlinjection_lowaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
print("            -    EN  "+str(count_vulnibm_sh_namesqlinjection_mediumaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA\n")
print("\n")
print("      -    EN  "+str(count_vulnibm_sh_namecrosssiterequestforgery)+" VULNERABILIDADES EL NOMBRE INCLUYE CROSS SITE REQUEST FORGERY, LAS ESTADÍSTICAS DE COMPLEJIDAD DE ATAQUE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_sh_namecrosssiterequestforgery_highaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
print("            -    EN  "+str(count_vulnibm_sh_namecrosssiterequestforgery_lowaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
print("            -    EN  "+str(count_vulnibm_sh_namecrosssiterequestforgery_mediumaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA\n")
print("\n")
print("      -    EN  "+str(count_vulnibm_sh_namemoduleexecution)+" VULNERABILIDADES EL NOMBRE INCLUYE MODULE EXECUTION, LAS ESTADÍSTICAS DE COMPLEJIDAD DE ATAQUE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_sh_namemoduleexecution_highaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
print("            -    EN  "+str(count_vulnibm_sh_namemoduleexecution_lowaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
print("            -    EN  "+str(count_vulnibm_sh_namemoduleexecution_mediumaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA\n")
print("\n")
print("      -    EN  "+str(count_vulnibm_sh_namebufferoverflow)+" VULNERABILIDADES EL NOMBRE INCLUYE BUFFER OVERFLOW, LAS ESTADÍSTICAS DE COMPLEJIDAD DE ATAQUE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_sh_namebufferoverflow_highaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
print("            -    EN  "+str(count_vulnibm_sh_namebufferoverflow_lowaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
print("            -    EN  "+str(count_vulnibm_sh_namebufferoverflow_mediumaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA\n")
print("\n")
print("      -    EN  "+str(count_vulnibm_sh_namecommandexecution)+" VULNERABILIDADES EL NOMBRE INCLUYE COMMAND EXECUTION, LAS ESTADÍSTICAS DE COMPLEJIDAD DE ATAQUE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_sh_namecommandexecution_highaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
print("            -    EN  "+str(count_vulnibm_sh_namecommandexecution_lowaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
print("            -    EN  "+str(count_vulnibm_sh_namecommandexecution_mediumaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA\n")
print("\n")
print("      -    EN  "+str(count_vulnibm_sh_namespoofing)+" VULNERABILIDADES EL NOMBRE INCLUYE SPOOFING, LAS ESTADÍSTICAS DE COMPLEJIDAD DE ATAQUE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_sh_namespoofing_highaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
print("            -    EN  "+str(count_vulnibm_sh_namespoofing_lowaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
print("            -    EN  "+str(count_vulnibm_sh_namespoofing_mediumaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA\n")
print("\n")
print("      -    EN  "+str(count_vulnibm_sh_nameclickjacking)+" VULNERABILIDADES EL NOMBRE INCLUYE CLICKJACKING, LAS ESTADÍSTICAS DE COMPLEJIDAD DE ATAQUE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_sh_nameclickjacking_highaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
print("            -    EN  "+str(count_vulnibm_sh_nameclickjacking_lowaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
print("            -    EN  "+str(count_vulnibm_sh_nameclickjacking_mediumaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA\n")
print("\n")
print("      -    EN  "+str(count_vulnibm_sh_namehijacking)+" VULNERABILIDADES EL NOMBRE INCLUYE HIJACKING, LAS ESTADÍSTICAS DE COMPLEJIDAD DE ATAQUE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_sh_namehijacking_highaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
print("            -    EN  "+str(count_vulnibm_sh_namehijacking_lowaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
print("            -    EN  "+str(count_vulnibm_sh_namehijacking_mediumaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA\n")
print("\n")
print("      -    EN  "+str(count_vulnibm_sh_namefileinclude)+" VULNERABILIDADES EL NOMBRE INCLUYE FILEINCLUDE, LAS ESTADÍSTICAS DE COMPLEJIDAD DE ATAQUE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_sh_namefileinclude_highaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
print("            -    EN  "+str(count_vulnibm_sh_namefileinclude_lowaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
print("            -    EN  "+str(count_vulnibm_sh_namefileinclude_mediumaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA\n")
print("\n")
print("      -    EN  "+str(count_vulnibm_sh_namebruteforce)+" VULNERABILIDADES EL NOMBRE INCLUYE BRUTEFORCE, LAS ESTADÍSTICAS DE COMPLEJIDAD DE ATAQUE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_sh_namebruteforce_highaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
print("            -    EN  "+str(count_vulnibm_sh_namebruteforce_lowaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
print("            -    EN  "+str(count_vulnibm_sh_namebruteforce_mediumaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA\n")
print("\n")
print("      -    EN  "+str(count_vulnibm_sh_namefileupload)+" VULNERABILIDADES EL NOMBRE INCLUYE FILE UPLOAD, LAS ESTADÍSTICAS DE COMPLEJIDAD DE ATAQUE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_sh_namefileupload_highaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
print("            -    EN  "+str(count_vulnibm_sh_namefileupload_lowaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
print("            -    EN  "+str(count_vulnibm_sh_namefileupload_mediumaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA\n")
print("\n")
print("      -    EN  "+str(count_vulnibm_sh_nameheaderinjection)+" VULNERABILIDADES EL NOMBRE INCLUYE HEADER INJECTION, LAS ESTADÍSTICAS DE COMPLEJIDAD DE ATAQUE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_sh_nameheaderinjection_highaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
print("            -    EN  "+str(count_vulnibm_sh_nameheaderinjection_lowaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
print("            -    EN  "+str(count_vulnibm_sh_nameheaderinjection_mediumaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA\n")
print("\n")
print("      -    EN  "+str(count_vulnibm_sh_nametampering)+" VULNERABILIDADES EL NOMBRE INCLUYE TAMPERING, LAS ESTADÍSTICAS DE COMPLEJIDAD DE ATAQUE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_sh_nametampering_highaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
print("            -    EN  "+str(count_vulnibm_sh_nametampering_lowaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
print("            -    EN  "+str(count_vulnibm_sh_nametampering_mediumaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA\n")
print("\n")
print("      -    EN  "+str(count_vulnibm_sh_nameanother)+" VULNERABILIDADES EL NOMBRE INCLUYE OTRA CADENA, LAS ESTADÍSTICAS DE COMPLEJIDAD DE ATAQUE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_sh_nameanother_highaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
print("            -    EN  "+str(count_vulnibm_sh_nameanother_lowaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
print("            -    EN  "+str(count_vulnibm_sh_nameanother_mediumaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA\n")
print("\n")





print("************************PORCENTAJE NOMBRE/COMPLEJIDAD DE ATAQUE VULNERABILIDADES IBM PARTE SMART HOME************************")
print("\n")                            
print("\n")
print(" DE UN TOTAL DE "+str(count_vulnibm_sh_names)+" VULNERABILIDADES :\n") 
print("\n")
print("   - LOS PORCENTAJES DE VALORES DE NOMBRE SON LOS SIGUIENTES:  \n")
if(count_vulnibm_sh_namepathtraversal>0):
    print("      -    EN EL  "+str(float(((count_vulnibm_sh_namepathtraversal*100)/count_vulnibm_sh_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE PATH TRAVERSAL,LOS PORCENTAJES DE COMPLEJIDAD DE ATAQUE SON LOS SIGUIENTES :  \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namepathtraversal_highaccesscom*100)/count_vulnibm_sh_namepathtraversal)))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namepathtraversal_lowaccesscom*100)/count_vulnibm_sh_namepathtraversal)))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namepathtraversal_mediumaccesscom*100)/count_vulnibm_sh_namepathtraversal)))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA\n")
    print("\n")
print("      -    EN EL  "+str(float(((count_vulnibm_sh_namedirectorytraversal*100)/count_vulnibm_sh_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE DIRECTORY TRAVERSAL,LOS PORCENTAJES DE COMPLEJIDAD DE ATAQUE SON LOS SIGUIENTES :  \n")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_namedirectorytraversal_highaccesscom*100)/count_vulnibm_sh_namedirectorytraversal)))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_namedirectorytraversal_lowaccesscom*100)/count_vulnibm_sh_namedirectorytraversal)))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_namedirectorytraversal_mediumaccesscom*100)/count_vulnibm_sh_namedirectorytraversal)))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA\n")
print("\n")
print("      -    EN EL  "+str(float(((count_vulnibm_sh_nameprivilegeescalation*100)/count_vulnibm_sh_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE PRIVILEGE ESCALATION,LOS PORCENTAJES DE COMPLEJIDAD DE ATAQUE SON LOS SIGUIENTES :  \n")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_nameprivilegeescalation_highaccesscom*100)/count_vulnibm_sh_nameprivilegeescalation)))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_nameprivilegeescalation_lowaccesscom*100)/count_vulnibm_sh_nameprivilegeescalation)))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_nameprivilegeescalation_mediumaccesscom*100)/count_vulnibm_sh_nameprivilegeescalation)))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA\n")
print("\n")
print("      -    EN EL  "+str(float(((count_vulnibm_sh_namecrosssitescripting*100)/count_vulnibm_sh_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE CROSS SITE SCRIPTING,LOS PORCENTAJES DE COMPLEJIDAD DE ATAQUE SON LOS SIGUIENTES :  \n")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_namecrosssitescripting_highaccesscom*100)/count_vulnibm_sh_namecrosssitescripting)))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_namecrosssitescripting_lowaccesscom*100)/count_vulnibm_sh_namecrosssitescripting)))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_namecrosssitescripting_mediumaccesscom*100)/count_vulnibm_sh_namecrosssitescripting)))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA\n")
print("\n")
print("      -    EN EL  "+str(float(((count_vulnibm_sh_namesecuritybypass*100)/count_vulnibm_sh_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE SECURITY BYPASS,LOS PORCENTAJES DE COMPLEJIDAD DE ATAQUE SON LOS SIGUIENTES :  \n")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_namesecuritybypass_highaccesscom*100)/count_vulnibm_sh_namesecuritybypass)))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_namesecuritybypass_lowaccesscom*100)/count_vulnibm_sh_namesecuritybypass)))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_namesecuritybypass_mediumaccesscom*100)/count_vulnibm_sh_namesecuritybypass)))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA\n")
print("\n")
print("      -    EN EL  "+str(float(((count_vulnibm_sh_nameinformationdisclosure*100)/count_vulnibm_sh_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE INFORMATION DISCLOSURE,LOS PORCENTAJES DE COMPLEJIDAD DE ATAQUE SON LOS SIGUIENTES :  \n")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_nameinformationdisclosure_highaccesscom*100)/count_vulnibm_sh_nameinformationdisclosure)))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_nameinformationdisclosure_lowaccesscom*100)/count_vulnibm_sh_nameinformationdisclosure)))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_nameinformationdisclosure_mediumaccesscom*100)/count_vulnibm_sh_nameinformationdisclosure)))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA\n")
print("\n")
print("      -    EN EL  "+str(float(((count_vulnibm_sh_namedenialofservice*100)/count_vulnibm_sh_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE DENIAL OF SERVICE,LOS PORCENTAJES DE COMPLEJIDAD DE ATAQUE SON LOS SIGUIENTES :  \n")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_namedenialofservice_highaccesscom*100)/count_vulnibm_sh_namedenialofservice)))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_namedenialofservice_lowaccesscom*100)/count_vulnibm_sh_namedenialofservice)))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_namedenialofservice_mediumaccesscom*100)/count_vulnibm_sh_namedenialofservice)))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA\n")
print("\n")
print("      -    EN EL  "+str(float(((count_vulnibm_sh_namecodeexecution*100)/count_vulnibm_sh_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE CODE EXECUTION,LOS PORCENTAJES DE COMPLEJIDAD DE ATAQUE SON LOS SIGUIENTES :  \n")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_namecodeexecution_highaccesscom*100)/count_vulnibm_sh_namecodeexecution)))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_namecodeexecution_lowaccesscom*100)/count_vulnibm_sh_namecodeexecution)))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_namecodeexecution_mediumaccesscom*100)/count_vulnibm_sh_namecodeexecution)))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA\n")
print("\n")
if(count_vulnibm_sh_namemaninthemiddle>0):
    print("      -    EN EL  "+str(float(((count_vulnibm_sh_namemaninthemiddle*100)/count_vulnibm_sh_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE MAN IN THE MIDDLE,LOS PORCENTAJES DE COMPLEJIDAD DE ATAQUE SON LOS SIGUIENTES :  \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namemaninthemiddle_highaccesscom*100)/count_vulnibm_sh_namemaninthemiddle)))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namemaninthemiddle_lowaccesscom*100)/count_vulnibm_sh_namemaninthemiddle)))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namemaninthemiddle_mediumaccesscom*100)/count_vulnibm_sh_namemaninthemiddle)))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA\n")
    print("\n")
if(count_vulnibm_sh_namesqlinjection>0):
    print("      -    EN EL  "+str(float(((count_vulnibm_sh_namesqlinjection*100)/count_vulnibm_sh_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE SQL INJECTION,LOS PORCENTAJES DE COMPLEJIDAD DE ATAQUE SON LOS SIGUIENTES :  \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namesqlinjection_highaccesscom*100)/count_vulnibm_sh_namesqlinjection)))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namesqlinjection_lowaccesscom*100)/count_vulnibm_sh_namesqlinjection)))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namesqlinjection_mediumaccesscom*100)/count_vulnibm_sh_namesqlinjection)))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA\n")
    print("\n")
print("      -    EN EL  "+str(float(((count_vulnibm_sh_namecrosssiterequestforgery*100)/count_vulnibm_sh_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE CROSS SITE REQUEST FORGERY,LOS PORCENTAJES DE COMPLEJIDAD DE ATAQUE SON LOS SIGUIENTES :  \n")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_namecrosssiterequestforgery_highaccesscom*100)/count_vulnibm_sh_namecrosssiterequestforgery)))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_namecrosssiterequestforgery_lowaccesscom*100)/count_vulnibm_sh_namecrosssiterequestforgery)))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_namecrosssiterequestforgery_mediumaccesscom*100)/count_vulnibm_sh_namecrosssiterequestforgery)))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA\n")
print("\n")
if(count_vulnibm_sh_namemoduleexecution>0):
    print("      -    EN EL  "+str(float(((count_vulnibm_sh_namemoduleexecution*100)/count_vulnibm_sh_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE MODULE EXECUTION,LOS PORCENTAJES DE COMPLEJIDAD DE ATAQUE SON LOS SIGUIENTES :  \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namemoduleexecution_highaccesscom*100)/count_vulnibm_sh_namemoduleexecution)))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namemoduleexecution_lowaccesscom*100)/count_vulnibm_sh_namemoduleexecution)))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namemoduleexecution_mediumaccesscom*100)/count_vulnibm_sh_namemoduleexecution)))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA\n")
    print("\n")
print("      -    EN EL  "+str(float(((count_vulnibm_sh_namebufferoverflow*100)/count_vulnibm_sh_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE BUFFER OVERFLOW,LOS PORCENTAJES DE COMPLEJIDAD DE ATAQUE SON LOS SIGUIENTES :  \n")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_namebufferoverflow_highaccesscom*100)/count_vulnibm_sh_namebufferoverflow)))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_namebufferoverflow_lowaccesscom*100)/count_vulnibm_sh_namebufferoverflow)))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_namebufferoverflow_mediumaccesscom*100)/count_vulnibm_sh_namebufferoverflow)))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA\n")
print("\n")
print("      -    EN EL  "+str(float(((count_vulnibm_sh_namecommandexecution*100)/count_vulnibm_sh_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE COMMAND EXECUTION,LOS PORCENTAJES DE COMPLEJIDAD DE ATAQUE SON LOS SIGUIENTES :  \n")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_namecommandexecution_highaccesscom*100)/count_vulnibm_sh_namecommandexecution)))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_namecommandexecution_lowaccesscom*100)/count_vulnibm_sh_namecommandexecution)))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_namecommandexecution_mediumaccesscom*100)/count_vulnibm_sh_namecommandexecution)))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA\n")
print("\n")
if(count_vulnibm_sh_namespoofing>0):
    print("      -    EN EL  "+str(float(((count_vulnibm_sh_namespoofing*100)/count_vulnibm_sh_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE SPOOFING,LOS PORCENTAJES DE COMPLEJIDAD DE ATAQUE SON LOS SIGUIENTES :  \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namespoofing_highaccesscom*100)/count_vulnibm_sh_namespoofing)))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namespoofing_lowaccesscom*100)/count_vulnibm_sh_namespoofing)))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namespoofing_mediumaccesscom*100)/count_vulnibm_sh_namespoofing)))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA\n")
    print("\n")
if(count_vulnibm_sh_nameclickjacking>0):
    print("      -    EN EL  "+str(float(((count_vulnibm_sh_nameclickjacking*100)/count_vulnibm_sh_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE CLICKJACKING,LOS PORCENTAJES DE COMPLEJIDAD DE ATAQUE SON LOS SIGUIENTES :  \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_nameclickjacking_highaccesscom*100)/count_vulnibm_sh_nameclickjacking)))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_nameclickjacking_lowaccesscom*100)/count_vulnibm_sh_nameclickjacking)))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_nameclickjacking_mediumaccesscom*100)/count_vulnibm_sh_nameclickjacking)))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA\n")
    print("\n")
if(count_vulnibm_sh_namehijacking>0):
    print("      -    EN EL  "+str(float(((count_vulnibm_sh_namehijacking*100)/count_vulnibm_sh_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE HIJACKING,LOS PORCENTAJES DE COMPLEJIDAD DE ATAQUE SON LOS SIGUIENTES :  \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namehijacking_highaccesscom*100)/count_vulnibm_sh_namehijacking)))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namehijacking_lowaccesscom*100)/count_vulnibm_sh_namehijacking)))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namehijacking_mediumaccesscom*100)/count_vulnibm_sh_namehijacking)))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA\n")
    print("\n")
if(count_vulnibm_sh_namefileinclude>0):
    print("      -    EN EL  "+str(float(((count_vulnibm_sh_namefileinclude*100)/count_vulnibm_sh_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE FILEINCLUDE,LOS PORCENTAJES DE COMPLEJIDAD DE ATAQUE SON LOS SIGUIENTES :  \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namefileinclude_highaccesscom*100)/count_vulnibm_sh_namefileinclude)))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namefileinclude_lowaccesscom*100)/count_vulnibm_sh_namefileinclude)))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namefileinclude_mediumaccesscom*100)/count_vulnibm_sh_namefileinclude)))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA\n")
    print("\n")
if(count_vulnibm_sh_namebruteforce>0):
    print("      -    EN EL  "+str(float(((count_vulnibm_sh_namebruteforce*100)/count_vulnibm_sh_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE BRUTEFORCE,LOS PORCENTAJES DE COMPLEJIDAD DE ATAQUE SON LOS SIGUIENTES :  \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namebruteforce_highaccesscom*100)/count_vulnibm_sh_namebruteforce)))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namebruteforce_lowaccesscom*100)/count_vulnibm_sh_namebruteforce)))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namebruteforce_mediumaccesscom*100)/count_vulnibm_sh_namebruteforce)))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA\n")
    print("\n")
print("      -    EN EL  "+str(float(((count_vulnibm_sh_namefileupload*100)/count_vulnibm_sh_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE FILE UPLOAD,LOS PORCENTAJES DE COMPLEJIDAD DE ATAQUE SON LOS SIGUIENTES :  \n")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_namefileupload_highaccesscom*100)/count_vulnibm_sh_namefileupload)))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_namefileupload_lowaccesscom*100)/count_vulnibm_sh_namefileupload)))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_namefileupload_mediumaccesscom*100)/count_vulnibm_sh_namefileupload)))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA\n")
print("\n")
if(count_vulnibm_sh_nameheaderinjection>0):
    print("      -    EN EL  "+str(float(((count_vulnibm_sh_nameheaderinjection*100)/count_vulnibm_sh_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE HEADER INJECTION,LOS PORCENTAJES DE COMPLEJIDAD DE ATAQUE SON LOS SIGUIENTES :  \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_nameheaderinjection_highaccesscom*100)/count_vulnibm_sh_nameheaderinjection)))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_nameheaderinjection_lowaccesscom*100)/count_vulnibm_sh_nameheaderinjection)))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_nameheaderinjection_mediumaccesscom*100)/count_vulnibm_sh_nameheaderinjection)))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA\n")
    print("\n")
if(count_vulnibm_sh_nametampering>0):
    print("      -    EN EL  "+str(float(((count_vulnibm_sh_nametampering*100)/count_vulnibm_sh_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE TAMPERING,LOS PORCENTAJES DE COMPLEJIDAD DE ATAQUE SON LOS SIGUIENTES :  \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_nametampering_highaccesscom*100)/count_vulnibm_sh_nametampering)))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_nametampering_lowaccesscom*100)/count_vulnibm_sh_nametampering)))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_nametampering_mediumaccesscom*100)/count_vulnibm_sh_nametampering)))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA\n")
    print("\n")
    print("      -    EN EL  "+str(float(((count_vulnibm_sh_nameanother*100)/count_vulnibm_sh_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE OTRA CADENA,LOS PORCENTAJES DE COMPLEJIDAD DE ATAQUE SON LOS SIGUIENTES :  \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_nameanother_highaccesscom*100)/count_vulnibm_sh_nameanother)))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_nameanother_lowaccesscom*100)/count_vulnibm_sh_nameanother)))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_nameanother_mediumaccesscom*100)/count_vulnibm_sh_nameanother)))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA\n")
    print("\n")








print("************************ESTADÍSTICAS NOMBRE/COMPLEJIDAD DE ATAQUE VULNERABILIDADES IBM PARTE IOT Y SMART HOME ************************")
print("\n")                            
print("\n")
print(" DE UN TOTAL DE "+str(count_vulnibm_iot_names+count_vulnibm_sh_names)+" VULNERABILIDADES:\n") 
print("\n")
print("   - LAS ESTADISTICAS DE VALORES DE NOMBRE SON LAS SIGUIENTES:  \n")
print("      -    EN  "+str(count_vulnibm_iot_namepathtraversal+count_vulnibm_sh_namepathtraversal)+" VULNERABILIDADES EL NOMBRE INCLUYE PATH TRAVERSAL, LAS ESTADÍSTICAS DE COMPLEJIDAD DE ATAQUE SON LAS SIGUIENTES:  \n")
print("            -    EN  "+str(count_vulnibm_iot_namepathtraversal_highaccesscom+count_vulnibm_sh_namepathtraversal_highaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
print("            -    EN  "+str(count_vulnibm_iot_namepathtraversal_lowaccesscom+count_vulnibm_sh_namepathtraversal_lowaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
print("            -    EN  "+str(count_vulnibm_iot_namepathtraversal_mediumaccesscom+count_vulnibm_sh_namepathtraversal_mediumaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_namedirectorytraversal+count_vulnibm_sh_namedirectorytraversal)+" VULNERABILIDADES EL NOMBRE INCLUYE DIRECTORY TRAVERSAL, LAS ESTADÍSTICAS DE COMPLEJIDAD DE ATAQUE SON LAS SIGUIENTES:  \n")
print("            -    EN  "+str(count_vulnibm_iot_namedirectorytraversal_highaccesscom+count_vulnibm_sh_namedirectorytraversal_highaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
print("            -    EN  "+str(count_vulnibm_iot_namedirectorytraversal_lowaccesscom+count_vulnibm_sh_namedirectorytraversal_lowaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
print("            -    EN  "+str(count_vulnibm_iot_namedirectorytraversal_mediumaccesscom+count_vulnibm_sh_namedirectorytraversal_mediumaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_nameprivilegeescalation+count_vulnibm_sh_nameprivilegeescalation)+" VULNERABILIDADES EL NOMBRE INCLUYE PRIVILEGE ESCALATION, LAS ESTADÍSTICAS DE COMPLEJIDAD DE ATAQUE SON LAS SIGUIENTES:  \n")
print("            -    EN  "+str(count_vulnibm_iot_nameprivilegeescalation_highaccesscom+count_vulnibm_sh_nameprivilegeescalation_highaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
print("            -    EN  "+str(count_vulnibm_iot_nameprivilegeescalation_lowaccesscom+count_vulnibm_sh_nameprivilegeescalation_lowaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
print("            -    EN  "+str(count_vulnibm_iot_nameprivilegeescalation_mediumaccesscom+count_vulnibm_sh_nameprivilegeescalation_mediumaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_namecrosssitescripting+count_vulnibm_sh_namecrosssitescripting)+" VULNERABILIDADES EL NOMBRE INCLUYE CROSS SITE SCRIPTING, LAS ESTADÍSTICAS DE COMPLEJIDAD DE ATAQUE SON LAS SIGUIENTES:  \n")
print("            -    EN  "+str(count_vulnibm_iot_namecrosssitescripting_highaccesscom+count_vulnibm_sh_namecrosssitescripting_highaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
print("            -    EN  "+str(count_vulnibm_iot_namecrosssitescripting_lowaccesscom+count_vulnibm_sh_namecrosssitescripting_lowaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
print("            -    EN  "+str(count_vulnibm_iot_namecrosssitescripting_mediumaccesscom+count_vulnibm_sh_namecrosssitescripting_mediumaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_namesecuritybypass+count_vulnibm_sh_namesecuritybypass)+" VULNERABILIDADES EL NOMBRE INCLUYE SECURITY BYPASS, LAS ESTADÍSTICAS DE COMPLEJIDAD DE ATAQUE SON LAS SIGUIENTES:  \n")
print("            -    EN  "+str(count_vulnibm_iot_namesecuritybypass_highaccesscom+count_vulnibm_sh_namesecuritybypass_highaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
print("            -    EN  "+str(count_vulnibm_iot_namesecuritybypass_lowaccesscom+count_vulnibm_sh_namesecuritybypass_lowaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
print("            -    EN  "+str(count_vulnibm_iot_namesecuritybypass_mediumaccesscom+count_vulnibm_sh_namesecuritybypass_mediumaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_nameinformationdisclosure+count_vulnibm_sh_nameinformationdisclosure)+" VULNERABILIDADES EL NOMBRE INCLUYE INFORMATION DISCLOSURE, LAS ESTADÍSTICAS DE COMPLEJIDAD DE ATAQUE SON LAS SIGUIENTES:  \n")
print("            -    EN  "+str(count_vulnibm_iot_nameinformationdisclosure_highaccesscom+count_vulnibm_sh_nameinformationdisclosure_highaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
print("            -    EN  "+str(count_vulnibm_iot_nameinformationdisclosure_lowaccesscom+count_vulnibm_sh_nameinformationdisclosure_lowaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
print("            -    EN  "+str(count_vulnibm_iot_nameinformationdisclosure_mediumaccesscom+count_vulnibm_sh_nameinformationdisclosure_mediumaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_namedenialofservice+count_vulnibm_sh_namedenialofservice)+" VULNERABILIDADES EL NOMBRE INCLUYE DENIAL OF SERVICE, LAS ESTADÍSTICAS DE COMPLEJIDAD DE ATAQUE SON LAS SIGUIENTES:  \n")
print("            -    EN  "+str(count_vulnibm_iot_namedenialofservice_highaccesscom+count_vulnibm_sh_namedenialofservice_highaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
print("            -    EN  "+str(count_vulnibm_iot_namedenialofservice_lowaccesscom+count_vulnibm_sh_namedenialofservice_lowaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
print("            -    EN  "+str(count_vulnibm_iot_namedenialofservice_mediumaccesscom+count_vulnibm_sh_namedenialofservice_mediumaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_namecodeexecution+count_vulnibm_sh_namecodeexecution)+" VULNERABILIDADES EL NOMBRE INCLUYE CODE EXECUTION, LAS ESTADÍSTICAS DE COMPLEJIDAD DE ATAQUE SON LAS SIGUIENTES:  \n")
print("            -    EN  "+str(count_vulnibm_iot_namecodeexecution_highaccesscom+count_vulnibm_sh_namecodeexecution_highaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
print("            -    EN  "+str(count_vulnibm_iot_namecodeexecution_lowaccesscom+count_vulnibm_sh_namecodeexecution_lowaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
print("            -    EN  "+str(count_vulnibm_iot_namecodeexecution_mediumaccesscom+count_vulnibm_sh_namecodeexecution_mediumaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_namemaninthemiddle+count_vulnibm_sh_namemaninthemiddle)+" VULNERABILIDADES EL NOMBRE INCLUYE MAN IN THE MIDDLE, LAS ESTADÍSTICAS DE COMPLEJIDAD DE ATAQUE SON LAS SIGUIENTES:  \n")
print("            -    EN  "+str(count_vulnibm_iot_namemaninthemiddle_highaccesscom+count_vulnibm_sh_namemaninthemiddle_highaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
print("            -    EN  "+str(count_vulnibm_iot_namemaninthemiddle_lowaccesscom+count_vulnibm_sh_namemaninthemiddle_lowaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
print("            -    EN  "+str(count_vulnibm_iot_namemaninthemiddle_mediumaccesscom+count_vulnibm_sh_namemaninthemiddle_mediumaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_namesqlinjection+count_vulnibm_sh_namesqlinjection)+" VULNERABILIDADES EL NOMBRE INCLUYE SQL INJECTION, LAS ESTADÍSTICAS DE COMPLEJIDAD DE ATAQUE SON LAS SIGUIENTES:  \n")
print("            -    EN  "+str(count_vulnibm_iot_namesqlinjection_highaccesscom+count_vulnibm_sh_namesqlinjection_highaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
print("            -    EN  "+str(count_vulnibm_iot_namesqlinjection_lowaccesscom+count_vulnibm_sh_namesqlinjection_lowaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
print("            -    EN  "+str(count_vulnibm_iot_namesqlinjection_mediumaccesscom+count_vulnibm_sh_namesqlinjection_mediumaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_namecrosssiterequestforgery+count_vulnibm_sh_namecrosssiterequestforgery)+" VULNERABILIDADES EL NOMBRE INCLUYE CROSS SITE REQUEST FORGERY, LAS ESTADÍSTICAS DE COMPLEJIDAD DE ATAQUE SON LAS SIGUIENTES:  \n")
print("            -    EN  "+str(count_vulnibm_iot_namecrosssiterequestforgery_highaccesscom+count_vulnibm_sh_namecrosssiterequestforgery_highaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
print("            -    EN  "+str(count_vulnibm_iot_namecrosssiterequestforgery_lowaccesscom+count_vulnibm_sh_namecrosssiterequestforgery_lowaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
print("            -    EN  "+str(count_vulnibm_iot_namecrosssiterequestforgery_mediumaccesscom+count_vulnibm_sh_namecrosssiterequestforgery_mediumaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_namemoduleexecution+count_vulnibm_sh_namemoduleexecution)+" VULNERABILIDADES EL NOMBRE INCLUYE MODULE EXECUTION, LAS ESTADÍSTICAS DE COMPLEJIDAD DE ATAQUE SON LAS SIGUIENTES:  \n")
print("            -    EN  "+str(count_vulnibm_iot_namemoduleexecution_highaccesscom+count_vulnibm_sh_namemoduleexecution_highaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
print("            -    EN  "+str(count_vulnibm_iot_namemoduleexecution_lowaccesscom+count_vulnibm_sh_namemoduleexecution_lowaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
print("            -    EN  "+str(count_vulnibm_iot_namemoduleexecution_mediumaccesscom+count_vulnibm_sh_namemoduleexecution_mediumaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_namebufferoverflow+count_vulnibm_sh_namebufferoverflow)+" VULNERABILIDADES EL NOMBRE INCLUYE BUFFER OVERFLOW, LAS ESTADÍSTICAS DE COMPLEJIDAD DE ATAQUE SON LAS SIGUIENTES:  \n")
print("            -    EN  "+str(count_vulnibm_iot_namebufferoverflow_highaccesscom+count_vulnibm_sh_namebufferoverflow_highaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
print("            -    EN  "+str(count_vulnibm_iot_namebufferoverflow_lowaccesscom+count_vulnibm_sh_namebufferoverflow_lowaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
print("            -    EN  "+str(count_vulnibm_iot_namebufferoverflow_mediumaccesscom+count_vulnibm_sh_namebufferoverflow_mediumaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_namecommandexecution+count_vulnibm_sh_namecommandexecution)+" VULNERABILIDADES EL NOMBRE INCLUYE COMMAND EXECUTION, LAS ESTADÍSTICAS DE COMPLEJIDAD DE ATAQUE SON LAS SIGUIENTES:  \n")
print("            -    EN  "+str(count_vulnibm_iot_namecommandexecution_highaccesscom+count_vulnibm_sh_namecommandexecution_highaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
print("            -    EN  "+str(count_vulnibm_iot_namecommandexecution_lowaccesscom+count_vulnibm_sh_namecommandexecution_lowaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
print("            -    EN  "+str(count_vulnibm_iot_namecommandexecution_mediumaccesscom+count_vulnibm_sh_namecommandexecution_mediumaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_namespoofing+count_vulnibm_sh_namespoofing)+" VULNERABILIDADES EL NOMBRE INCLUYE SPOOFING, LAS ESTADÍSTICAS DE COMPLEJIDAD DE ATAQUE SON LAS SIGUIENTES:  \n")
print("            -    EN  "+str(count_vulnibm_iot_namespoofing_highaccesscom+count_vulnibm_sh_namespoofing_highaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
print("            -    EN  "+str(count_vulnibm_iot_namespoofing_lowaccesscom+count_vulnibm_sh_namespoofing_lowaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
print("            -    EN  "+str(count_vulnibm_iot_namespoofing_mediumaccesscom+count_vulnibm_sh_namespoofing_mediumaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_nameclickjacking+count_vulnibm_sh_nameclickjacking)+" VULNERABILIDADES EL NOMBRE INCLUYE CLICKJACKING, LAS ESTADÍSTICAS DE COMPLEJIDAD DE ATAQUE SON LAS SIGUIENTES:  \n")
print("            -    EN  "+str(count_vulnibm_iot_nameclickjacking_highaccesscom+count_vulnibm_sh_nameclickjacking_highaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
print("            -    EN  "+str(count_vulnibm_iot_nameclickjacking_lowaccesscom+count_vulnibm_sh_nameclickjacking_lowaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
print("            -    EN  "+str(count_vulnibm_iot_nameclickjacking_mediumaccesscom+count_vulnibm_sh_nameclickjacking_mediumaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_namehijacking+count_vulnibm_sh_namehijacking)+" VULNERABILIDADES EL NOMBRE INCLUYE HIJACKING, LAS ESTADÍSTICAS DE COMPLEJIDAD DE ATAQUE SON LAS SIGUIENTES:  \n")
print("            -    EN  "+str(count_vulnibm_iot_namehijacking_highaccesscom+count_vulnibm_sh_namehijacking_highaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
print("            -    EN  "+str(count_vulnibm_iot_namehijacking_lowaccesscom+count_vulnibm_sh_namehijacking_lowaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
print("            -    EN  "+str(count_vulnibm_iot_namehijacking_mediumaccesscom+count_vulnibm_sh_namehijacking_mediumaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_namefileinclude+count_vulnibm_sh_namefileinclude)+" VULNERABILIDADES EL NOMBRE INCLUYE FILE INCLUDE, LAS ESTADÍSTICAS DE COMPLEJIDAD DE ATAQUE SON LAS SIGUIENTES:  \n")
print("            -    EN  "+str(count_vulnibm_iot_namefileinclude_highaccesscom+count_vulnibm_sh_namefileinclude_highaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
print("            -    EN  "+str(count_vulnibm_iot_namefileinclude_lowaccesscom+count_vulnibm_sh_namefileinclude_lowaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
print("            -    EN  "+str(count_vulnibm_iot_namefileinclude_mediumaccesscom+count_vulnibm_sh_namefileinclude_mediumaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_namebruteforce+count_vulnibm_sh_namebruteforce)+" VULNERABILIDADES EL NOMBRE INCLUYE BRUTE FORCE, LAS ESTADÍSTICAS DE COMPLEJIDAD DE ATAQUE SON LAS SIGUIENTES:  \n")
print("            -    EN  "+str(count_vulnibm_iot_namebruteforce_highaccesscom+count_vulnibm_sh_namebruteforce_highaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
print("            -    EN  "+str(count_vulnibm_iot_namebruteforce_lowaccesscom+count_vulnibm_sh_namebruteforce_lowaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
print("            -    EN  "+str(count_vulnibm_iot_namebruteforce_mediumaccesscom+count_vulnibm_sh_namebruteforce_mediumaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_namefileupload+count_vulnibm_sh_namefileupload)+" VULNERABILIDADES EL NOMBRE INCLUYE FILE UPLOAD, LAS ESTADÍSTICAS DE COMPLEJIDAD DE ATAQUE SON LAS SIGUIENTES:  \n")
print("            -    EN  "+str(count_vulnibm_iot_namefileupload_highaccesscom+count_vulnibm_sh_namefileupload_highaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
print("            -    EN  "+str(count_vulnibm_iot_namefileupload_lowaccesscom+count_vulnibm_sh_namefileupload_lowaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
print("            -    EN  "+str(count_vulnibm_iot_namefileupload_mediumaccesscom+count_vulnibm_sh_namefileupload_mediumaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_nameheaderinjection+count_vulnibm_sh_nameheaderinjection)+" VULNERABILIDADES EL NOMBRE INCLUYE HEADER INJECTION, LAS ESTADÍSTICAS DE COMPLEJIDAD DE ATAQUE SON LAS SIGUIENTES:  \n")
print("            -    EN  "+str(count_vulnibm_iot_nameheaderinjection_highaccesscom+count_vulnibm_sh_nameheaderinjection_highaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
print("            -    EN  "+str(count_vulnibm_iot_nameheaderinjection_lowaccesscom+count_vulnibm_sh_nameheaderinjection_lowaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
print("            -    EN  "+str(count_vulnibm_iot_nameheaderinjection_mediumaccesscom+count_vulnibm_sh_nameheaderinjection_mediumaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_nametampering+count_vulnibm_sh_nametampering)+" VULNERABILIDADES EL NOMBRE INCLUYE TAMPERING, LAS ESTADÍSTICAS DE COMPLEJIDAD DE ATAQUE SON LAS SIGUIENTES:  \n")
print("            -    EN  "+str(count_vulnibm_iot_nametampering_highaccesscom+count_vulnibm_sh_nametampering_highaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
print("            -    EN  "+str(count_vulnibm_iot_nametampering_lowaccesscom+count_vulnibm_sh_nametampering_lowaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
print("            -    EN  "+str(count_vulnibm_iot_nametampering_mediumaccesscom+count_vulnibm_sh_nametampering_mediumaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_nameanother+count_vulnibm_sh_nameanother)+" VULNERABILIDADES EL NOMBRE INCLUYE OTRO NOMBRE DISTINTO, LAS ESTADÍSTICAS DE COMPLEJIDAD DE ATAQUE SON LAS SIGUIENTES:  \n")
print("            -    EN  "+str(count_vulnibm_iot_nameanother_highaccesscom+count_vulnibm_sh_nameanother_highaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
print("            -    EN  "+str(count_vulnibm_iot_nameanother_lowaccesscom+count_vulnibm_sh_nameanother_lowaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
print("            -    EN  "+str(count_vulnibm_iot_nameanother_mediumaccesscom+count_vulnibm_sh_nameanother_mediumaccesscom)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA \n")
print("\n")









print("************************PORCENTAJES NOMBRE/COMPLEJIDAD DE ATAQUE VULNERABILIDADES IBM PARTE IOT Y SMART HOME************************")
print("\n")                            
print("\n")
print(" DE UN TOTAL DE "+str(count_vulnibm_iot_names+count_vulnibm_sh_names)+" VULNERABILIDADES:\n") 
print("\n")
print("   - LOS PORCENTAJES DE VALORES DE NOMBRE SON LOS SIGUIENTES:  \n")
print("      -    EN EL "+str(float((((count_vulnibm_iot_namepathtraversal+count_vulnibm_sh_namepathtraversal)*100)/(count_vulnibm_iot_names+count_vulnibm_sh_names))))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE PATHTRAVERSAL, LOS PORCENTAJES DE COMPLEJIDAD DE ATAQUE SON LOS SIGUIENTES:  \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namepathtraversal_highaccesscom+count_vulnibm_sh_namepathtraversal_highaccesscom)*100)/(count_vulnibm_iot_namepathtraversal+count_vulnibm_sh_namepathtraversal))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namepathtraversal_lowaccesscom+count_vulnibm_sh_namepathtraversal_lowaccesscom)*100)/(count_vulnibm_iot_namepathtraversal+count_vulnibm_sh_namepathtraversal))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namepathtraversal_mediumaccesscom+count_vulnibm_sh_namepathtraversal_mediumaccesscom)*100)/(count_vulnibm_iot_namepathtraversal+count_vulnibm_sh_namepathtraversal))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA \n")
print("\n")
print("      -    EN EL "+str(float((((count_vulnibm_iot_namedirectorytraversal+count_vulnibm_sh_namedirectorytraversal)*100)/(count_vulnibm_iot_names+count_vulnibm_sh_names))))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE directorytraversal, LOS PORCENTAJES DE COMPLEJIDAD DE ATAQUE SON LOS SIGUIENTES:  \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namedirectorytraversal_highaccesscom+count_vulnibm_sh_namedirectorytraversal_highaccesscom)*100)/(count_vulnibm_iot_namedirectorytraversal+count_vulnibm_sh_namedirectorytraversal))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namedirectorytraversal_lowaccesscom+count_vulnibm_sh_namedirectorytraversal_lowaccesscom)*100)/(count_vulnibm_iot_namedirectorytraversal+count_vulnibm_sh_namedirectorytraversal))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namedirectorytraversal_mediumaccesscom+count_vulnibm_sh_namedirectorytraversal_mediumaccesscom)*100)/(count_vulnibm_iot_namedirectorytraversal+count_vulnibm_sh_namedirectorytraversal))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA \n")
print("\n")
print("      -    EN EL "+str(float((((count_vulnibm_iot_nameprivilegeescalation+count_vulnibm_sh_nameprivilegeescalation)*100)/(count_vulnibm_iot_names+count_vulnibm_sh_names))))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE privilegeescalation, LOS PORCENTAJES DE COMPLEJIDAD DE ATAQUE SON LOS SIGUIENTES:  \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_nameprivilegeescalation_highaccesscom+count_vulnibm_sh_nameprivilegeescalation_highaccesscom)*100)/(count_vulnibm_iot_nameprivilegeescalation+count_vulnibm_sh_nameprivilegeescalation))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_nameprivilegeescalation_lowaccesscom+count_vulnibm_sh_nameprivilegeescalation_lowaccesscom)*100)/(count_vulnibm_iot_nameprivilegeescalation+count_vulnibm_sh_nameprivilegeescalation))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_nameprivilegeescalation_mediumaccesscom+count_vulnibm_sh_nameprivilegeescalation_mediumaccesscom)*100)/(count_vulnibm_iot_nameprivilegeescalation+count_vulnibm_sh_nameprivilegeescalation))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA \n")
print("\n")
print("      -    EN EL "+str(float((((count_vulnibm_iot_namecrosssitescripting+count_vulnibm_sh_namecrosssitescripting)*100)/(count_vulnibm_iot_names+count_vulnibm_sh_names))))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE crosssitescripting, LOS PORCENTAJES DE COMPLEJIDAD DE ATAQUE SON LOS SIGUIENTES:  \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namecrosssitescripting_highaccesscom+count_vulnibm_sh_namecrosssitescripting_highaccesscom)*100)/(count_vulnibm_iot_namecrosssitescripting+count_vulnibm_sh_namecrosssitescripting))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namecrosssitescripting_lowaccesscom+count_vulnibm_sh_namecrosssitescripting_lowaccesscom)*100)/(count_vulnibm_iot_namecrosssitescripting+count_vulnibm_sh_namecrosssitescripting))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namecrosssitescripting_mediumaccesscom+count_vulnibm_sh_namecrosssitescripting_mediumaccesscom)*100)/(count_vulnibm_iot_namecrosssitescripting+count_vulnibm_sh_namecrosssitescripting))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA \n")
print("\n")
print("      -    EN EL "+str(float((((count_vulnibm_iot_namesecuritybypass+count_vulnibm_sh_namesecuritybypass)*100)/(count_vulnibm_iot_names+count_vulnibm_sh_names))))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE securitybypass, LOS PORCENTAJES DE COMPLEJIDAD DE ATAQUE SON LOS SIGUIENTES:  \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namesecuritybypass_highaccesscom+count_vulnibm_sh_namesecuritybypass_highaccesscom)*100)/(count_vulnibm_iot_namesecuritybypass+count_vulnibm_sh_namesecuritybypass))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namesecuritybypass_lowaccesscom+count_vulnibm_sh_namesecuritybypass_lowaccesscom)*100)/(count_vulnibm_iot_namesecuritybypass+count_vulnibm_sh_namesecuritybypass))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namesecuritybypass_mediumaccesscom+count_vulnibm_sh_namesecuritybypass_mediumaccesscom)*100)/(count_vulnibm_iot_namesecuritybypass+count_vulnibm_sh_namesecuritybypass))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA \n")
print("\n")
print("      -    EN EL "+str(float((((count_vulnibm_iot_nameinformationdisclosure+count_vulnibm_sh_nameinformationdisclosure)*100)/(count_vulnibm_iot_names+count_vulnibm_sh_names))))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE informationdisclosure, LOS PORCENTAJES DE COMPLEJIDAD DE ATAQUE SON LOS SIGUIENTES:  \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_nameinformationdisclosure_highaccesscom+count_vulnibm_sh_nameinformationdisclosure_highaccesscom)*100)/(count_vulnibm_iot_nameinformationdisclosure+count_vulnibm_sh_nameinformationdisclosure))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_nameinformationdisclosure_lowaccesscom+count_vulnibm_sh_nameinformationdisclosure_lowaccesscom)*100)/(count_vulnibm_iot_nameinformationdisclosure+count_vulnibm_sh_nameinformationdisclosure))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_nameinformationdisclosure_mediumaccesscom+count_vulnibm_sh_nameinformationdisclosure_mediumaccesscom)*100)/(count_vulnibm_iot_nameinformationdisclosure+count_vulnibm_sh_nameinformationdisclosure))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA \n")
print("\n")
print("      -    EN EL "+str(float((((count_vulnibm_iot_namedenialofservice+count_vulnibm_sh_namedenialofservice)*100)/(count_vulnibm_iot_names+count_vulnibm_sh_names))))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE denialofservice, LOS PORCENTAJES DE COMPLEJIDAD DE ATAQUE SON LOS SIGUIENTES:  \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namedenialofservice_highaccesscom+count_vulnibm_sh_namedenialofservice_highaccesscom)*100)/(count_vulnibm_iot_namedenialofservice+count_vulnibm_sh_namedenialofservice))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namedenialofservice_lowaccesscom+count_vulnibm_sh_namedenialofservice_lowaccesscom)*100)/(count_vulnibm_iot_namedenialofservice+count_vulnibm_sh_namedenialofservice))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namedenialofservice_mediumaccesscom+count_vulnibm_sh_namedenialofservice_mediumaccesscom)*100)/(count_vulnibm_iot_namedenialofservice+count_vulnibm_sh_namedenialofservice))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA \n")
print("\n")
print("      -    EN EL "+str(float((((count_vulnibm_iot_namecodeexecution+count_vulnibm_sh_namecodeexecution)*100)/(count_vulnibm_iot_names+count_vulnibm_sh_names))))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE codeexecution, LOS PORCENTAJES DE COMPLEJIDAD DE ATAQUE SON LOS SIGUIENTES:  \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namecodeexecution_highaccesscom+count_vulnibm_sh_namecodeexecution_highaccesscom)*100)/(count_vulnibm_iot_namecodeexecution+count_vulnibm_sh_namecodeexecution))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namecodeexecution_lowaccesscom+count_vulnibm_sh_namecodeexecution_lowaccesscom)*100)/(count_vulnibm_iot_namecodeexecution+count_vulnibm_sh_namecodeexecution))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namecodeexecution_mediumaccesscom+count_vulnibm_sh_namecodeexecution_mediumaccesscom)*100)/(count_vulnibm_iot_namecodeexecution+count_vulnibm_sh_namecodeexecution))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA \n")
print("\n")
print("      -    EN EL "+str(float((((count_vulnibm_iot_namemaninthemiddle+count_vulnibm_sh_namemaninthemiddle)*100)/(count_vulnibm_iot_names+count_vulnibm_sh_names))))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE maninthemiddle, LOS PORCENTAJES DE COMPLEJIDAD DE ATAQUE SON LOS SIGUIENTES:  \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namemaninthemiddle_highaccesscom+count_vulnibm_sh_namemaninthemiddle_highaccesscom)*100)/(count_vulnibm_iot_namemaninthemiddle+count_vulnibm_sh_namemaninthemiddle))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namemaninthemiddle_lowaccesscom+count_vulnibm_sh_namemaninthemiddle_lowaccesscom)*100)/(count_vulnibm_iot_namemaninthemiddle+count_vulnibm_sh_namemaninthemiddle))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namemaninthemiddle_mediumaccesscom+count_vulnibm_sh_namemaninthemiddle_mediumaccesscom)*100)/(count_vulnibm_iot_namemaninthemiddle+count_vulnibm_sh_namemaninthemiddle))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA \n")
print("\n")
print("      -    EN EL "+str(float((((count_vulnibm_iot_namesqlinjection+count_vulnibm_sh_namesqlinjection)*100)/(count_vulnibm_iot_names+count_vulnibm_sh_names))))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE sqlinjection, LOS PORCENTAJES DE COMPLEJIDAD DE ATAQUE SON LOS SIGUIENTES:  \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namesqlinjection_highaccesscom+count_vulnibm_sh_namesqlinjection_highaccesscom)*100)/(count_vulnibm_iot_namesqlinjection+count_vulnibm_sh_namesqlinjection))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namesqlinjection_lowaccesscom+count_vulnibm_sh_namesqlinjection_lowaccesscom)*100)/(count_vulnibm_iot_namesqlinjection+count_vulnibm_sh_namesqlinjection))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namesqlinjection_mediumaccesscom+count_vulnibm_sh_namesqlinjection_mediumaccesscom)*100)/(count_vulnibm_iot_namesqlinjection+count_vulnibm_sh_namesqlinjection))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA \n")
print("\n")
print("      -    EN EL "+str(float((((count_vulnibm_iot_namecrosssiterequestforgery+count_vulnibm_sh_namecrosssiterequestforgery)*100)/(count_vulnibm_iot_names+count_vulnibm_sh_names))))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE crosssiterequestforgery, LOS PORCENTAJES DE COMPLEJIDAD DE ATAQUE SON LOS SIGUIENTES:  \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namecrosssiterequestforgery_highaccesscom+count_vulnibm_sh_namecrosssiterequestforgery_highaccesscom)*100)/(count_vulnibm_iot_namecrosssiterequestforgery+count_vulnibm_sh_namecrosssiterequestforgery))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namecrosssiterequestforgery_lowaccesscom+count_vulnibm_sh_namecrosssiterequestforgery_lowaccesscom)*100)/(count_vulnibm_iot_namecrosssiterequestforgery+count_vulnibm_sh_namecrosssiterequestforgery))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namecrosssiterequestforgery_mediumaccesscom+count_vulnibm_sh_namecrosssiterequestforgery_mediumaccesscom)*100)/(count_vulnibm_iot_namecrosssiterequestforgery+count_vulnibm_sh_namecrosssiterequestforgery))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA \n")
print("\n")
print("      -    EN EL "+str(float((((count_vulnibm_iot_namemoduleexecution+count_vulnibm_sh_namemoduleexecution)*100)/(count_vulnibm_iot_names+count_vulnibm_sh_names))))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE moduleexecution, LOS PORCENTAJES DE COMPLEJIDAD DE ATAQUE SON LOS SIGUIENTES:  \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namemoduleexecution_highaccesscom+count_vulnibm_sh_namemoduleexecution_highaccesscom)*100)/(count_vulnibm_iot_namemoduleexecution+count_vulnibm_sh_namemoduleexecution))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namemoduleexecution_lowaccesscom+count_vulnibm_sh_namemoduleexecution_lowaccesscom)*100)/(count_vulnibm_iot_namemoduleexecution+count_vulnibm_sh_namemoduleexecution))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namemoduleexecution_mediumaccesscom+count_vulnibm_sh_namemoduleexecution_mediumaccesscom)*100)/(count_vulnibm_iot_namemoduleexecution+count_vulnibm_sh_namemoduleexecution))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA \n")
print("\n")
print("      -    EN EL "+str(float((((count_vulnibm_iot_namebufferoverflow+count_vulnibm_sh_namebufferoverflow)*100)/(count_vulnibm_iot_names+count_vulnibm_sh_names))))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE bufferoverflow, LOS PORCENTAJES DE COMPLEJIDAD DE ATAQUE SON LOS SIGUIENTES:  \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namebufferoverflow_highaccesscom+count_vulnibm_sh_namebufferoverflow_highaccesscom)*100)/(count_vulnibm_iot_namebufferoverflow+count_vulnibm_sh_namebufferoverflow))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namebufferoverflow_lowaccesscom+count_vulnibm_sh_namebufferoverflow_lowaccesscom)*100)/(count_vulnibm_iot_namebufferoverflow+count_vulnibm_sh_namebufferoverflow))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namebufferoverflow_mediumaccesscom+count_vulnibm_sh_namebufferoverflow_mediumaccesscom)*100)/(count_vulnibm_iot_namebufferoverflow+count_vulnibm_sh_namebufferoverflow))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA \n")
print("\n")
print("      -    EN EL "+str(float((((count_vulnibm_iot_namecommandexecution+count_vulnibm_sh_namecommandexecution)*100)/(count_vulnibm_iot_names+count_vulnibm_sh_names))))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE commandexecution, LOS PORCENTAJES DE COMPLEJIDAD DE ATAQUE SON LOS SIGUIENTES:  \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namecommandexecution_highaccesscom+count_vulnibm_sh_namecommandexecution_highaccesscom)*100)/(count_vulnibm_iot_namecommandexecution+count_vulnibm_sh_namecommandexecution))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namecommandexecution_lowaccesscom+count_vulnibm_sh_namecommandexecution_lowaccesscom)*100)/(count_vulnibm_iot_namecommandexecution+count_vulnibm_sh_namecommandexecution))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namecommandexecution_mediumaccesscom+count_vulnibm_sh_namecommandexecution_mediumaccesscom)*100)/(count_vulnibm_iot_namecommandexecution+count_vulnibm_sh_namecommandexecution))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA \n")
print("\n")
print("      -    EN EL "+str(float((((count_vulnibm_iot_namespoofing+count_vulnibm_sh_namespoofing)*100)/(count_vulnibm_iot_names+count_vulnibm_sh_names))))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE spoofing, LOS PORCENTAJES DE COMPLEJIDAD DE ATAQUE SON LOS SIGUIENTES:  \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namespoofing_highaccesscom+count_vulnibm_sh_namespoofing_highaccesscom)*100)/(count_vulnibm_iot_namespoofing+count_vulnibm_sh_namespoofing))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namespoofing_lowaccesscom+count_vulnibm_sh_namespoofing_lowaccesscom)*100)/(count_vulnibm_iot_namespoofing+count_vulnibm_sh_namespoofing))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namespoofing_mediumaccesscom+count_vulnibm_sh_namespoofing_mediumaccesscom)*100)/(count_vulnibm_iot_namespoofing+count_vulnibm_sh_namespoofing))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA \n")
print("\n")
print("      -    EN EL "+str(float((((count_vulnibm_iot_nameclickjacking+count_vulnibm_sh_nameclickjacking)*100)/(count_vulnibm_iot_names+count_vulnibm_sh_names))))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE clickjacking, LOS PORCENTAJES DE COMPLEJIDAD DE ATAQUE SON LOS SIGUIENTES:  \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_nameclickjacking_highaccesscom+count_vulnibm_sh_nameclickjacking_highaccesscom)*100)/(count_vulnibm_iot_nameclickjacking+count_vulnibm_sh_nameclickjacking))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_nameclickjacking_lowaccesscom+count_vulnibm_sh_nameclickjacking_lowaccesscom)*100)/(count_vulnibm_iot_nameclickjacking+count_vulnibm_sh_nameclickjacking))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_nameclickjacking_mediumaccesscom+count_vulnibm_sh_nameclickjacking_mediumaccesscom)*100)/(count_vulnibm_iot_nameclickjacking+count_vulnibm_sh_nameclickjacking))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA \n")
print("\n")
print("      -    EN EL "+str(float((((count_vulnibm_iot_namehijacking+count_vulnibm_sh_namehijacking)*100)/(count_vulnibm_iot_names+count_vulnibm_sh_names))))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE hijacking, LOS PORCENTAJES DE COMPLEJIDAD DE ATAQUE SON LOS SIGUIENTES:  \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namehijacking_highaccesscom+count_vulnibm_sh_namehijacking_highaccesscom)*100)/(count_vulnibm_iot_namehijacking+count_vulnibm_sh_namehijacking))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namehijacking_lowaccesscom+count_vulnibm_sh_namehijacking_lowaccesscom)*100)/(count_vulnibm_iot_namehijacking+count_vulnibm_sh_namehijacking))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namehijacking_mediumaccesscom+count_vulnibm_sh_namehijacking_mediumaccesscom)*100)/(count_vulnibm_iot_namehijacking+count_vulnibm_sh_namehijacking))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA \n")
print("\n")
print("      -    EN EL "+str(float((((count_vulnibm_iot_namefileinclude+count_vulnibm_sh_namefileinclude)*100)/(count_vulnibm_iot_names+count_vulnibm_sh_names))))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE fileinclude, LOS PORCENTAJES DE COMPLEJIDAD DE ATAQUE SON LOS SIGUIENTES:  \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namefileinclude_highaccesscom+count_vulnibm_sh_namefileinclude_highaccesscom)*100)/(count_vulnibm_iot_namefileinclude+count_vulnibm_sh_namefileinclude))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namefileinclude_lowaccesscom+count_vulnibm_sh_namefileinclude_lowaccesscom)*100)/(count_vulnibm_iot_namefileinclude+count_vulnibm_sh_namefileinclude))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namefileinclude_mediumaccesscom+count_vulnibm_sh_namefileinclude_mediumaccesscom)*100)/(count_vulnibm_iot_namefileinclude+count_vulnibm_sh_namefileinclude))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA \n")
print("\n")
print("      -    EN EL "+str(float((((count_vulnibm_iot_namebruteforce+count_vulnibm_sh_namebruteforce)*100)/(count_vulnibm_iot_names+count_vulnibm_sh_names))))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE bruteforce, LOS PORCENTAJES DE COMPLEJIDAD DE ATAQUE SON LOS SIGUIENTES:  \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namebruteforce_highaccesscom+count_vulnibm_sh_namebruteforce_highaccesscom)*100)/(count_vulnibm_iot_namebruteforce+count_vulnibm_sh_namebruteforce))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namebruteforce_lowaccesscom+count_vulnibm_sh_namebruteforce_lowaccesscom)*100)/(count_vulnibm_iot_namebruteforce+count_vulnibm_sh_namebruteforce))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namebruteforce_mediumaccesscom+count_vulnibm_sh_namebruteforce_mediumaccesscom)*100)/(count_vulnibm_iot_namebruteforce+count_vulnibm_sh_namebruteforce))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA \n")
print("\n")
print("      -    EN EL "+str(float((((count_vulnibm_iot_namefileupload+count_vulnibm_sh_namefileupload)*100)/(count_vulnibm_iot_names+count_vulnibm_sh_names))))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE fileupload, LOS PORCENTAJES DE COMPLEJIDAD DE ATAQUE SON LOS SIGUIENTES:  \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namefileupload_highaccesscom+count_vulnibm_sh_namefileupload_highaccesscom)*100)/(count_vulnibm_iot_namefileupload+count_vulnibm_sh_namefileupload))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namefileupload_lowaccesscom+count_vulnibm_sh_namefileupload_lowaccesscom)*100)/(count_vulnibm_iot_namefileupload+count_vulnibm_sh_namefileupload))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namefileupload_mediumaccesscom+count_vulnibm_sh_namefileupload_mediumaccesscom)*100)/(count_vulnibm_iot_namefileupload+count_vulnibm_sh_namefileupload))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA \n")
print("\n")
print("      -    EN EL "+str(float((((count_vulnibm_iot_nameheaderinjection+count_vulnibm_sh_nameheaderinjection)*100)/(count_vulnibm_iot_names+count_vulnibm_sh_names))))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE headerinjection, LOS PORCENTAJES DE COMPLEJIDAD DE ATAQUE SON LOS SIGUIENTES:  \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_nameheaderinjection_highaccesscom+count_vulnibm_sh_nameheaderinjection_highaccesscom)*100)/(count_vulnibm_iot_nameheaderinjection+count_vulnibm_sh_nameheaderinjection))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_nameheaderinjection_lowaccesscom+count_vulnibm_sh_nameheaderinjection_lowaccesscom)*100)/(count_vulnibm_iot_nameheaderinjection+count_vulnibm_sh_nameheaderinjection))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_nameheaderinjection_mediumaccesscom+count_vulnibm_sh_nameheaderinjection_mediumaccesscom)*100)/(count_vulnibm_iot_nameheaderinjection+count_vulnibm_sh_nameheaderinjection))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA \n")
print("\n")
print("      -    EN EL "+str(float((((count_vulnibm_iot_nametampering+count_vulnibm_sh_nametampering)*100)/(count_vulnibm_iot_names+count_vulnibm_sh_names))))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE tampering, LOS PORCENTAJES DE COMPLEJIDAD DE ATAQUE SON LOS SIGUIENTES:  \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_nametampering_highaccesscom+count_vulnibm_sh_nametampering_highaccesscom)*100)/(count_vulnibm_iot_nametampering+count_vulnibm_sh_nametampering))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_nametampering_lowaccesscom+count_vulnibm_sh_nametampering_lowaccesscom)*100)/(count_vulnibm_iot_nametampering+count_vulnibm_sh_nametampering))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_nametampering_mediumaccesscom+count_vulnibm_sh_nametampering_mediumaccesscom)*100)/(count_vulnibm_iot_nametampering+count_vulnibm_sh_nametampering))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA \n")
print("\n")
print("      -    EN EL "+str(float((((count_vulnibm_iot_nameanother+count_vulnibm_sh_nameanother)*100)/(count_vulnibm_iot_names+count_vulnibm_sh_names))))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE UN VALOR DISTINTO, LOS PORCENTAJES DE COMPLEJIDAD DE ATAQUE SON LOS SIGUIENTES:  \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_nameanother_highaccesscom+count_vulnibm_sh_nameanother_highaccesscom)*100)/(count_vulnibm_iot_nameanother+count_vulnibm_sh_nameanother))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_nameanother_lowaccesscom+count_vulnibm_sh_nameanother_lowaccesscom)*100)/(count_vulnibm_iot_nameanother+count_vulnibm_sh_nameanother))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_nameanother_mediumaccesscom+count_vulnibm_sh_nameanother_mediumaccesscom)*100)/(count_vulnibm_iot_nameanother+count_vulnibm_sh_nameanother))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA \n")
print("\n")
               	



