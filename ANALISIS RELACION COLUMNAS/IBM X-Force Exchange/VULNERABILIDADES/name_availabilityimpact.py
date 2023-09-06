import pandas as pd
from datetime import datetime,timedelta



#Abro los ficheros con los que voy a tratar




df_vulnibm_iot = pd.read_excel('vulnerabilidades_ibm_iot_2023.xlsx')

#Variable para almacenar el contador total de valores de nombre
count_vulnibm_iot_names=0
#Variable para almacenar el contador total de valores de un nombre concreto
count_vulnibm_iot_namepathtraversal=0
#Variables para almacenar el contador de valores de impacto de DISPONIBILIDAD dato un valor de nombre especifico
count_vulnibm_iot_namepathtraversal_avaimpact=0
count_vulnibm_iot_namepathtraversal_highavaimpact=0
count_vulnibm_iot_namepathtraversal_lowavaimpact=0
count_vulnibm_iot_namepathtraversal_mediumavaimpact=0

count_vulnibm_iot_namedirectorytraversal=0
count_vulnibm_iot_namedirectorytraversal_avaimpact=0
count_vulnibm_iot_namedirectorytraversal_highavaimpact=0
count_vulnibm_iot_namedirectorytraversal_lowavaimpact=0
count_vulnibm_iot_namedirectorytraversal_mediumavaimpact=0

count_vulnibm_iot_nameprivilegeescalation=0
count_vulnibm_iot_nameprivilegeescalation_avaimpact=0
count_vulnibm_iot_nameprivilegeescalation_highavaimpact=0
count_vulnibm_iot_nameprivilegeescalation_lowavaimpact=0
count_vulnibm_iot_nameprivilegeescalation_mediumavaimpact=0

count_vulnibm_iot_namecrosssitescripting=0
count_vulnibm_iot_namecrosssitescripting_avaimpact=0
count_vulnibm_iot_namecrosssitescripting_highavaimpact=0
count_vulnibm_iot_namecrosssitescripting_lowavaimpact=0
count_vulnibm_iot_namecrosssitescripting_mediumavaimpact=0

count_vulnibm_iot_namesecuritybypass=0
count_vulnibm_iot_namesecuritybypass_avaimpact=0
count_vulnibm_iot_namesecuritybypass_highavaimpact=0
count_vulnibm_iot_namesecuritybypass_lowavaimpact=0
count_vulnibm_iot_namesecuritybypass_mediumavaimpact=0

count_vulnibm_iot_nameinformationdisclosure=0
count_vulnibm_iot_nameinformationdisclosure_avaimpact=0
count_vulnibm_iot_nameinformationdisclosure_highavaimpact=0
count_vulnibm_iot_nameinformationdisclosure_lowavaimpact=0
count_vulnibm_iot_nameinformationdisclosure_mediumavaimpact=0

count_vulnibm_iot_namedenialofservice=0
count_vulnibm_iot_namedenialofservice_avaimpact=0
count_vulnibm_iot_namedenialofservice_highavaimpact=0
count_vulnibm_iot_namedenialofservice_lowavaimpact=0
count_vulnibm_iot_namedenialofservice_mediumavaimpact=0

count_vulnibm_iot_namecodeexecution=0
count_vulnibm_iot_namecodeexecution_avaimpact=0
count_vulnibm_iot_namecodeexecution_highavaimpact=0
count_vulnibm_iot_namecodeexecution_lowavaimpact=0
count_vulnibm_iot_namecodeexecution_mediumavaimpact=0

count_vulnibm_iot_namemaninthemiddle=0
count_vulnibm_iot_namemaninthemiddle_avaimpact=0
count_vulnibm_iot_namemaninthemiddle_highavaimpact=0
count_vulnibm_iot_namemaninthemiddle_lowavaimpact=0
count_vulnibm_iot_namemaninthemiddle_mediumavaimpact=0

count_vulnibm_iot_namesqlinjection=0
count_vulnibm_iot_namesqlinjection_avaimpact=0
count_vulnibm_iot_namesqlinjection_highavaimpact=0
count_vulnibm_iot_namesqlinjection_lowavaimpact=0
count_vulnibm_iot_namesqlinjection_mediumavaimpact=0

count_vulnibm_iot_namecrosssiterequestforgery=0
count_vulnibm_iot_namecrosssiterequestforgery_avaimpact=0
count_vulnibm_iot_namecrosssiterequestforgery_highavaimpact=0
count_vulnibm_iot_namecrosssiterequestforgery_lowavaimpact=0
count_vulnibm_iot_namecrosssiterequestforgery_mediumavaimpact=0

count_vulnibm_iot_namemoduleexecution=0
count_vulnibm_iot_namemoduleexecution_avaimpact=0
count_vulnibm_iot_namemoduleexecution_highavaimpact=0
count_vulnibm_iot_namemoduleexecution_lowavaimpact=0
count_vulnibm_iot_namemoduleexecution_mediumavaimpact=0

count_vulnibm_iot_namebufferoverflow=0
count_vulnibm_iot_namebufferoverflow_avaimpact=0
count_vulnibm_iot_namebufferoverflow_highavaimpact=0
count_vulnibm_iot_namebufferoverflow_lowavaimpact=0
count_vulnibm_iot_namebufferoverflow_mediumavaimpact=0

count_vulnibm_iot_namecommandexecution=0
count_vulnibm_iot_namecommandexecution_avaimpact=0
count_vulnibm_iot_namecommandexecution_highavaimpact=0
count_vulnibm_iot_namecommandexecution_lowavaimpact=0
count_vulnibm_iot_namecommandexecution_mediumavaimpact=0

count_vulnibm_iot_namespoofing=0
count_vulnibm_iot_namespoofing_avaimpact=0
count_vulnibm_iot_namespoofing_highavaimpact=0
count_vulnibm_iot_namespoofing_lowavaimpact=0
count_vulnibm_iot_namespoofing_mediumavaimpact=0

count_vulnibm_iot_nameclickjacking=0
count_vulnibm_iot_nameclickjacking_avaimpact=0
count_vulnibm_iot_nameclickjacking_highavaimpact=0
count_vulnibm_iot_nameclickjacking_lowavaimpact=0
count_vulnibm_iot_nameclickjacking_mediumavaimpact=0

count_vulnibm_iot_namehijacking=0
count_vulnibm_iot_namehijacking_avaimpact=0
count_vulnibm_iot_namehijacking_highavaimpact=0
count_vulnibm_iot_namehijacking_lowavaimpact=0
count_vulnibm_iot_namehijacking_mediumavaimpact=0

count_vulnibm_iot_namefileinclude=0
count_vulnibm_iot_namefileinclude_avaimpact=0
count_vulnibm_iot_namefileinclude_highavaimpact=0
count_vulnibm_iot_namefileinclude_lowavaimpact=0
count_vulnibm_iot_namefileinclude_mediumavaimpact=0

count_vulnibm_iot_namebruteforce=0
count_vulnibm_iot_namebruteforce_avaimpact=0
count_vulnibm_iot_namebruteforce_highavaimpact=0
count_vulnibm_iot_namebruteforce_lowavaimpact=0
count_vulnibm_iot_namebruteforce_mediumavaimpact=0

count_vulnibm_iot_namefileupload=0
count_vulnibm_iot_namefileupload_avaimpact=0
count_vulnibm_iot_namefileupload_highavaimpact=0
count_vulnibm_iot_namefileupload_lowavaimpact=0
count_vulnibm_iot_namefileupload_mediumavaimpact=0

count_vulnibm_iot_nameheaderinjection=0
count_vulnibm_iot_nameheaderinjection_avaimpact=0
count_vulnibm_iot_nameheaderinjection_highavaimpact=0
count_vulnibm_iot_nameheaderinjection_lowavaimpact=0
count_vulnibm_iot_nameheaderinjection_mediumavaimpact=0

count_vulnibm_iot_nametampering=0
count_vulnibm_iot_nametampering_avaimpact=0
count_vulnibm_iot_nametampering_highavaimpact=0
count_vulnibm_iot_nametampering_lowavaimpact=0
count_vulnibm_iot_nametampering_mediumavaimpact=0

count_vulnibm_iot_nameanother=0
count_vulnibm_iot_nameanother_avaimpact=0
count_vulnibm_iot_nameanother_highavaimpact=0
count_vulnibm_iot_nameanother_lowavaimpact=0
count_vulnibm_iot_nameanother_mediumavaimpact=0

#Comprobamos el contenido de name
for r in range(0,len(df_vulnibm_iot["name"])):                       
    aux_str=df_vulnibm_iot["name"][r].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
    if(aux_str!='NONE'):
        count_vulnibm_iot_names+=1
        #Compruebo el valor de nombre
        if('pathtraversal' in aux_str):
            count_vulnibm_iot_namepathtraversal+=1
            #Compruebo el valor de impacto de DISPONIBILIDAD
            if(df_vulnibm_iot["x_xfe_cvss_availability_impact"][r]=='High'):
                count_vulnibm_iot_namepathtraversal_avaimpact+=1
                count_vulnibm_iot_namepathtraversal_highavaimpact+=1
            elif(df_vulnibm_iot["x_xfe_cvss_availability_impact"][r]=='Low'):
                count_vulnibm_iot_namepathtraversal_avaimpact+=1
                count_vulnibm_iot_namepathtraversal_lowavaimpact+=1
            elif(df_vulnibm_iot["x_xfe_cvss_availability_impact"][r]=='Medium'):
                count_vulnibm_iot_namepathtraversal_avaimpact+=1
                count_vulnibm_iot_namepathtraversal_mediumavaimpact+=1
    
        elif('directorytraversal' in aux_str):
            
            count_vulnibm_iot_namedirectorytraversal+=1
            if(df_vulnibm_iot["x_xfe_cvss_availability_impact"][r]=='High'):
                count_vulnibm_iot_namedirectorytraversal_avaimpact+=1
                count_vulnibm_iot_namedirectorytraversal_highavaimpact+=1
            elif(df_vulnibm_iot["x_xfe_cvss_availability_impact"][r]=='Low'):
                count_vulnibm_iot_namedirectorytraversal_avaimpact+=1
                count_vulnibm_iot_namedirectorytraversal_lowavaimpact+=1
            elif(df_vulnibm_iot["x_xfe_cvss_availability_impact"][r]=='Medium'):
                count_vulnibm_iot_namedirectorytraversal_avaimpact+=1
                count_vulnibm_iot_namedirectorytraversal_mediumavaimpact+=1
            
            
        elif('privilegeescalation' in aux_str):
        
            count_vulnibm_iot_nameprivilegeescalation+=1
            if(df_vulnibm_iot["x_xfe_cvss_availability_impact"][r]=='High'):
                count_vulnibm_iot_nameprivilegeescalation_avaimpact+=1
                count_vulnibm_iot_nameprivilegeescalation_highavaimpact+=1
            elif(df_vulnibm_iot["x_xfe_cvss_availability_impact"][r]=='Low'):
                count_vulnibm_iot_nameprivilegeescalation_avaimpact+=1
                count_vulnibm_iot_nameprivilegeescalation_lowavaimpact+=1
            elif(df_vulnibm_iot["x_xfe_cvss_availability_impact"][r]=='Medium'):
                count_vulnibm_iot_nameprivilegeescalation_avaimpact+=1
                count_vulnibm_iot_nameprivilegeescalation_mediumavaimpact+=1
            
        elif('cross-sitescripting' in aux_str):
        
            count_vulnibm_iot_namecrosssitescripting+=1
            if(df_vulnibm_iot["x_xfe_cvss_availability_impact"][r]=='High'):
                count_vulnibm_iot_namecrosssitescripting_avaimpact+=1
                count_vulnibm_iot_namecrosssitescripting_highavaimpact+=1
            elif(df_vulnibm_iot["x_xfe_cvss_availability_impact"][r]=='Low'):
                count_vulnibm_iot_namecrosssitescripting_avaimpact+=1
                count_vulnibm_iot_namecrosssitescripting_lowavaimpact+=1
            elif(df_vulnibm_iot["x_xfe_cvss_availability_impact"][r]=='Medium'):
                count_vulnibm_iot_namecrosssitescripting_avaimpact+=1
                count_vulnibm_iot_namecrosssitescripting_mediumavaimpact+=1
                                         
        elif('securitybypass' in aux_str):
        
            count_vulnibm_iot_namesecuritybypass+=1
            if(df_vulnibm_iot["x_xfe_cvss_availability_impact"][r]=='High'):
                count_vulnibm_iot_namesecuritybypass_avaimpact+=1
                count_vulnibm_iot_namesecuritybypass_highavaimpact+=1
            elif(df_vulnibm_iot["x_xfe_cvss_availability_impact"][r]=='Low'):
                count_vulnibm_iot_namesecuritybypass_avaimpact+=1
                count_vulnibm_iot_namesecuritybypass_lowavaimpact+=1
            elif(df_vulnibm_iot["x_xfe_cvss_availability_impact"][r]=='Medium'):
                count_vulnibm_iot_namesecuritybypass_avaimpact+=1
                count_vulnibm_iot_namesecuritybypass_mediumavaimpact+=1
                                         
        elif('information_disclosure' in aux_str or 'informationdisclosure' in aux_str):
        
            count_vulnibm_iot_nameinformationdisclosure+=1
            if(df_vulnibm_iot["x_xfe_cvss_availability_impact"][r]=='High'):
                count_vulnibm_iot_nameinformationdisclosure_avaimpact+=1
                count_vulnibm_iot_nameinformationdisclosure_highavaimpact+=1
            elif(df_vulnibm_iot["x_xfe_cvss_availability_impact"][r]=='Low'):
                count_vulnibm_iot_nameinformationdisclosure_avaimpact+=1
                count_vulnibm_iot_nameinformationdisclosure_lowavaimpact+=1
            elif(df_vulnibm_iot["x_xfe_cvss_availability_impact"][r]=='Medium'):
                count_vulnibm_iot_nameinformationdisclosure_avaimpact+=1
                count_vulnibm_iot_nameinformationdisclosure_mediumavaimpact+=1
                                         
        elif('denialofservice' in aux_str):
            
            count_vulnibm_iot_namedenialofservice+=1
            if(df_vulnibm_iot["x_xfe_cvss_availability_impact"][r]=='High'):
                count_vulnibm_iot_namedenialofservice_avaimpact+=1
                count_vulnibm_iot_namedenialofservice_highavaimpact+=1
            elif(df_vulnibm_iot["x_xfe_cvss_availability_impact"][r]=='Low'):
                count_vulnibm_iot_namedenialofservice_avaimpact+=1
                count_vulnibm_iot_namedenialofservice_lowavaimpact+=1
            elif(df_vulnibm_iot["x_xfe_cvss_availability_impact"][r]=='Medium'):
                count_vulnibm_iot_namedenialofservice_avaimpact+=1
                count_vulnibm_iot_namedenialofservice_mediumavaimpact+=1
            
        elif('codeexecution' in aux_str):
        
        
            count_vulnibm_iot_namecodeexecution+=1
            if(df_vulnibm_iot["x_xfe_cvss_availability_impact"][r]=='High'):
                count_vulnibm_iot_namecodeexecution_avaimpact+=1
                count_vulnibm_iot_namecodeexecution_highavaimpact+=1
            elif(df_vulnibm_iot["x_xfe_cvss_availability_impact"][r]=='Low'):
                count_vulnibm_iot_namecodeexecution_avaimpact+=1
                count_vulnibm_iot_namecodeexecution_lowavaimpact+=1
            elif(df_vulnibm_iot["x_xfe_cvss_availability_impact"][r]=='Medium'):
                count_vulnibm_iot_namecodeexecution_avaimpact+=1
                count_vulnibm_iot_namecodeexecution_mediumavaimpact+=1
                                         
        elif('maninthemiddle' in aux_str):
        
            count_vulnibm_iot_namemaninthemiddle+=1
            if(df_vulnibm_iot["x_xfe_cvss_availability_impact"][r]=='High'):
                count_vulnibm_iot_namemaninthemiddle_avaimpact+=1
                count_vulnibm_iot_namemaninthemiddle_highavaimpact+=1
            elif(df_vulnibm_iot["x_xfe_cvss_availability_impact"][r]=='Low'):
                count_vulnibm_iot_namemaninthemiddle_avaimpact+=1
                count_vulnibm_iot_namemaninthemiddle_lowavaimpact+=1
            elif(df_vulnibm_iot["x_xfe_cvss_availability_impact"][r]=='Medium'):
                count_vulnibm_iot_namemaninthemiddle_avaimpact+=1
                count_vulnibm_iot_namemaninthemiddle_mediumavaimpact+=1
                                         
        elif('SQLinjection' in aux_str):
        
            count_vulnibm_iot_namesqlinjection+=1
            if(df_vulnibm_iot["x_xfe_cvss_availability_impact"][r]=='High'):
                count_vulnibm_iot_namesqlinjection_avaimpact+=1
                count_vulnibm_iot_namesqlinjection_highavaimpact+=1
            elif(df_vulnibm_iot["x_xfe_cvss_availability_impact"][r]=='Low'):
                count_vulnibm_iot_namesqlinjection_avaimpact+=1
                count_vulnibm_iot_namesqlinjection_lowavaimpact+=1
            elif(df_vulnibm_iot["x_xfe_cvss_availability_impact"][r]=='Medium'):
                count_vulnibm_iot_namesqlinjection_avaimpact+=1
                count_vulnibm_iot_namesqlinjection_mediumavaimpact+=1
                                         
        elif('cross-siterequestforgery' in aux_str):
        
            count_vulnibm_iot_namecrosssiterequestforgery+=1
            if(df_vulnibm_iot["x_xfe_cvss_availability_impact"][r]=='High'):
                count_vulnibm_iot_namecrosssiterequestforgery_avaimpact+=1
                count_vulnibm_iot_namecrosssiterequestforgery_highavaimpact+=1
            elif(df_vulnibm_iot["x_xfe_cvss_availability_impact"][r]=='Low'):
                count_vulnibm_iot_namecrosssiterequestforgery_avaimpact+=1
                count_vulnibm_iot_namecrosssiterequestforgery_lowavaimpact+=1
            elif(df_vulnibm_iot["x_xfe_cvss_availability_impact"][r]=='Medium'):
                count_vulnibm_iot_namecrosssiterequestforgery_avaimpact+=1
                count_vulnibm_iot_namecrosssiterequestforgery_mediumavaimpact+=1
                                         
        elif('moduleexecution' in aux_str):
        
            count_vulnibm_iot_namemoduleexecution+=1
            if(df_vulnibm_iot["x_xfe_cvss_availability_impact"][r]=='High'):
                count_vulnibm_iot_namemoduleexecution_avaimpact+=1
                count_vulnibm_iot_namemoduleexecution_highavaimpact+=1
            elif(df_vulnibm_iot["x_xfe_cvss_availability_impact"][r]=='Low'):
                count_vulnibm_iot_namemoduleexecution_avaimpact+=1
                count_vulnibm_iot_namemoduleexecution_lowavaimpact+=1
            elif(df_vulnibm_iot["x_xfe_cvss_availability_impact"][r]=='Medium'):
                count_vulnibm_iot_namemoduleexecution_avaimpact+=1
                count_vulnibm_iot_namemoduleexecution_mediumavaimpact+=1
                                         
        elif('bufferoverflow' in aux_str):
        
            count_vulnibm_iot_namebufferoverflow+=1
            if(df_vulnibm_iot["x_xfe_cvss_availability_impact"][r]=='High'):
                count_vulnibm_iot_namebufferoverflow_avaimpact+=1
                count_vulnibm_iot_namebufferoverflow_highavaimpact+=1
            elif(df_vulnibm_iot["x_xfe_cvss_availability_impact"][r]=='Low'):
                count_vulnibm_iot_namebufferoverflow_avaimpact+=1
                count_vulnibm_iot_namebufferoverflow_lowavaimpact+=1
            elif(df_vulnibm_iot["x_xfe_cvss_availability_impact"][r]=='Medium'):
                count_vulnibm_iot_namebufferoverflow_avaimpact+=1
                count_vulnibm_iot_namebufferoverflow_mediumavaimpact+=1
                                         
        elif('commandexecution' in aux_str):
        
            count_vulnibm_iot_namecommandexecution+=1
            if(df_vulnibm_iot["x_xfe_cvss_availability_impact"][r]=='High'):
                count_vulnibm_iot_namecommandexecution_avaimpact+=1
                count_vulnibm_iot_namecommandexecution_highavaimpact+=1
            elif(df_vulnibm_iot["x_xfe_cvss_availability_impact"][r]=='Low'):
                count_vulnibm_iot_namecommandexecution_avaimpact+=1
                count_vulnibm_iot_namecommandexecution_lowavaimpact+=1
            elif(df_vulnibm_iot["x_xfe_cvss_availability_impact"][r]=='Medium'):
                count_vulnibm_iot_namecommandexecution_avaimpact+=1
                count_vulnibm_iot_namecommandexecution_mediumavaimpact+=1
                                         
        elif('spoofing' in aux_str):
        
            count_vulnibm_iot_namespoofing+=1
            if(df_vulnibm_iot["x_xfe_cvss_availability_impact"][r]=='High'):
                count_vulnibm_iot_namespoofing_avaimpact+=1
                count_vulnibm_iot_namespoofing_highavaimpact+=1
            elif(df_vulnibm_iot["x_xfe_cvss_availability_impact"][r]=='Low'):
                count_vulnibm_iot_namespoofing_avaimpact+=1
                count_vulnibm_iot_namespoofing_lowavaimpact+=1
            elif(df_vulnibm_iot["x_xfe_cvss_availability_impact"][r]=='Medium'):
                count_vulnibm_iot_namespoofing_avaimpact+=1
                count_vulnibm_iot_namespoofing_mediumavaimpact+=1
                                         
        elif('clickjacking' in aux_str):
        
            count_vulnibm_iot_nameclickjacking+=1
            if(df_vulnibm_iot["x_xfe_cvss_availability_impact"][r]=='High'):
                count_vulnibm_iot_nameclickjacking_avaimpact+=1
                count_vulnibm_iot_nameclickjacking_highavaimpact+=1
            elif(df_vulnibm_iot["x_xfe_cvss_availability_impact"][r]=='Low'):
                count_vulnibm_iot_nameclickjacking_avaimpact+=1
                count_vulnibm_iot_nameclickjacking_lowavaimpact+=1
            elif(df_vulnibm_iot["x_xfe_cvss_availability_impact"][r]=='Medium'):
                count_vulnibm_iot_nameclickjacking_avaimpact+=1
                count_vulnibm_iot_nameclickjacking_mediumavaimpact+=1
              
        elif('hijacking' in aux_str):
        
            count_vulnibm_iot_namehijacking+=1
            if(df_vulnibm_iot["x_xfe_cvss_availability_impact"][r]=='High'):
                count_vulnibm_iot_namehijacking_avaimpact+=1
                count_vulnibm_iot_namehijacking_highavaimpact+=1
            elif(df_vulnibm_iot["x_xfe_cvss_availability_impact"][r]=='Low'):
                count_vulnibm_iot_namehijacking_avaimpact+=1
                count_vulnibm_iot_namehijacking_lowavaimpact+=1
            elif(df_vulnibm_iot["x_xfe_cvss_availability_impact"][r]=='Medium'):
                count_vulnibm_iot_namehijacking_avaimpact+=1
                count_vulnibm_iot_namehijacking_mediumavaimpact+=1
               
        elif('fileinclude' in aux_str):
        
            count_vulnibm_iot_namefileinclude+=1
            if(df_vulnibm_iot["x_xfe_cvss_availability_impact"][r]=='High'):
                count_vulnibm_iot_namefileinclude_avaimpact+=1
                count_vulnibm_iot_namefileinclude_highavaimpact+=1
            elif(df_vulnibm_iot["x_xfe_cvss_availability_impact"][r]=='Low'):
                count_vulnibm_iot_namefileinclude_avaimpact+=1
                count_vulnibm_iot_namefileinclude_lowavaimpact+=1
            elif(df_vulnibm_iot["x_xfe_cvss_availability_impact"][r]=='Medium'):
                count_vulnibm_iot_namefileinclude_avaimpact+=1
                count_vulnibm_iot_namefileinclude_mediumavaimpact+=1
                
               
        elif('bruteforce' in aux_str):
        
            count_vulnibm_iot_namebruteforce+=1
            if(df_vulnibm_iot["x_xfe_cvss_availability_impact"][r]=='High'):
                count_vulnibm_iot_namebruteforce_avaimpact+=1
                count_vulnibm_iot_namebruteforce_highavaimpact+=1
            elif(df_vulnibm_iot["x_xfe_cvss_availability_impact"][r]=='Low'):
                count_vulnibm_iot_namebruteforce_avaimpact+=1
                count_vulnibm_iot_namebruteforce_lowavaimpact+=1
            elif(df_vulnibm_iot["x_xfe_cvss_availability_impact"][r]=='Medium'):
                count_vulnibm_iot_namebruteforce_avaimpact+=1
                count_vulnibm_iot_namebruteforce_mediumavaimpact+=1
                
               
        elif('fileupload' in aux_str):
        
            count_vulnibm_iot_namefileupload+=1
            if(df_vulnibm_iot["x_xfe_cvss_availability_impact"][r]=='High'):
                count_vulnibm_iot_namefileupload_avaimpact+=1
                count_vulnibm_iot_namefileupload_highavaimpact+=1
            elif(df_vulnibm_iot["x_xfe_cvss_availability_impact"][r]=='Low'):
                count_vulnibm_iot_namefileupload_avaimpact+=1
                count_vulnibm_iot_namefileupload_lowavaimpact+=1
            elif(df_vulnibm_iot["x_xfe_cvss_availability_impact"][r]=='Medium'):
                count_vulnibm_iot_namefileupload_avaimpact+=1
                count_vulnibm_iot_namefileupload_mediumavaimpact+=1
                
               
        elif('headerinjection' in aux_str):
        
            count_vulnibm_iot_nameheaderinjection+=1
            if(df_vulnibm_iot["x_xfe_cvss_availability_impact"][r]=='High'):
                count_vulnibm_iot_nameheaderinjection_avaimpact+=1
                count_vulnibm_iot_nameheaderinjection_highavaimpact+=1
            elif(df_vulnibm_iot["x_xfe_cvss_availability_impact"][r]=='Low'):
                count_vulnibm_iot_nameheaderinjection_avaimpact+=1
                count_vulnibm_iot_nameheaderinjection_lowavaimpact+=1
            elif(df_vulnibm_iot["x_xfe_cvss_availability_impact"][r]=='Medium'):
                count_vulnibm_iot_nameheaderinjection_avaimpact+=1
                count_vulnibm_iot_nameheaderinjection_mediumavaimpact+=1
               
        elif('Tampering' in aux_str):
        
            count_vulnibm_iot_nametampering+=1
            if(df_vulnibm_iot["x_xfe_cvss_availability_impact"][r]=='High'):
                count_vulnibm_iot_nametampering_avaimpact+=1
                count_vulnibm_iot_nametampering_highavaimpact+=1
            elif(df_vulnibm_iot["x_xfe_cvss_availability_impact"][r]=='Low'):
                count_vulnibm_iot_nametampering_avaimpact+=1
                count_vulnibm_iot_nametampering_lowavaimpact+=1
            elif(df_vulnibm_iot["x_xfe_cvss_availability_impact"][r]=='Medium'):
                count_vulnibm_iot_nametampering_avaimpact+=1
                count_vulnibm_iot_nametampering_mediumavaimpact+=1
    
        else:
        
            count_vulnibm_iot_nameanother+=1
            if(df_vulnibm_iot["x_xfe_cvss_availability_impact"][r]=='High'):
                count_vulnibm_iot_nameanother_avaimpact+=1
                count_vulnibm_iot_nameanother_highavaimpact+=1
            elif(df_vulnibm_iot["x_xfe_cvss_availability_impact"][r]=='Low'):
                count_vulnibm_iot_nameanother_avaimpact+=1
                count_vulnibm_iot_nameanother_lowavaimpact+=1
            elif(df_vulnibm_iot["x_xfe_cvss_availability_impact"][r]=='Medium'):
                count_vulnibm_iot_nameanother_avaimpact+=1
                count_vulnibm_iot_nameanother_mediumavaimpact+=1
                
                
                
                
                
print("**********************************************ESTADÍSTICAS NOMBRE/IMPACTO DE DISPONIBILIDAD VULNERABILIDADES IBM PARTE IOT**********************************************")
print("\n")                            
print("\n")
print(" DE UN TOTAL DE "+str(count_vulnibm_iot_names)+" VULNERABILIDADES:\n") 
print("\n")
print("   - LAS ESTADISTICAS DE VALORES DE NOMBRE SON LAS SIGUIENTES:  \n")
print("      -    EN  "+str(count_vulnibm_iot_namepathtraversal)+" VULNERABILIDADES EL NOMBRE INCLUYE PATH TRAVERSAL, LAS ESTADÍSTICAS DE IMPACTO DE DISPONIBILIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_namepathtraversal_highavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_iot_namepathtraversal_lowavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_iot_namepathtraversal_mediumavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO\n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_namedirectorytraversal)+" VULNERABILIDADES EL NOMBRE INCLUYE DIRECTORY TRAVERSAL, LAS ESTADÍSTICAS DE IMPACTO DE DISPONIBILIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_namedirectorytraversal_highavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_iot_namedirectorytraversal_lowavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_iot_namedirectorytraversal_mediumavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO\n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_nameprivilegeescalation)+" VULNERABILIDADES EL NOMBRE INCLUYE PRIVILEGE ESCALATION, LAS ESTADÍSTICAS DE IMPACTO DE DISPONIBILIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_nameprivilegeescalation_highavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_iot_nameprivilegeescalation_lowavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_iot_nameprivilegeescalation_mediumavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO\n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_namecrosssitescripting)+" VULNERABILIDADES EL NOMBRE INCLUYE CROSS SITE SCRIPTING, LAS ESTADÍSTICAS DE IMPACTO DE DISPONIBILIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_namecrosssitescripting_highavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_iot_namecrosssitescripting_lowavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_iot_namecrosssitescripting_mediumavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO\n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_namesecuritybypass)+" VULNERABILIDADES EL NOMBRE INCLUYE SECURITY BYPASS, LAS ESTADÍSTICAS DE IMPACTO DE DISPONIBILIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_namesecuritybypass_highavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_iot_namesecuritybypass_lowavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_iot_namesecuritybypass_mediumavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO\n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_nameinformationdisclosure)+" VULNERABILIDADES EL NOMBRE INCLUYE INFORMATION DISCLOSURE, LAS ESTADÍSTICAS DE IMPACTO DE DISPONIBILIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_nameinformationdisclosure_highavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_iot_nameinformationdisclosure_lowavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_iot_nameinformationdisclosure_mediumavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO\n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_namedenialofservice)+" VULNERABILIDADES EL NOMBRE INCLUYE DENIAL OF SERVICE, LAS ESTADÍSTICAS DE IMPACTO DE DISPONIBILIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_namedenialofservice_highavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_iot_namedenialofservice_lowavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_iot_namedenialofservice_mediumavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO\n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_namecodeexecution)+" VULNERABILIDADES EL NOMBRE INCLUYE CODE EXECUTION, LAS ESTADÍSTICAS DE IMPACTO DE DISPONIBILIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_namecodeexecution_highavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_iot_namecodeexecution_lowavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_iot_namecodeexecution_mediumavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO\n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_namemaninthemiddle)+" VULNERABILIDADES EL NOMBRE INCLUYE MAN IN THE MIDDLE, LAS ESTADÍSTICAS DE IMPACTO DE DISPONIBILIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_namemaninthemiddle_highavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_iot_namemaninthemiddle_lowavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_iot_namemaninthemiddle_mediumavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO\n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_namesqlinjection)+" VULNERABILIDADES EL NOMBRE INCLUYE SQL INJECTION, LAS ESTADÍSTICAS DE IMPACTO DE DISPONIBILIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_namesqlinjection_highavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_iot_namesqlinjection_lowavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_iot_namesqlinjection_mediumavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO\n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_namecrosssiterequestforgery)+" VULNERABILIDADES EL NOMBRE INCLUYE CROSS SITE REQUEST FORGERY, LAS ESTADÍSTICAS DE IMPACTO DE DISPONIBILIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_namecrosssiterequestforgery_highavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_iot_namecrosssiterequestforgery_lowavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_iot_namecrosssiterequestforgery_mediumavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO\n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_namemoduleexecution)+" VULNERABILIDADES EL NOMBRE INCLUYE MODULE EXECUTION, LAS ESTADÍSTICAS DE IMPACTO DE DISPONIBILIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_namemoduleexecution_highavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_iot_namemoduleexecution_lowavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_iot_namemoduleexecution_mediumavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO\n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_namebufferoverflow)+" VULNERABILIDADES EL NOMBRE INCLUYE BUFFER OVERFLOW, LAS ESTADÍSTICAS DE IMPACTO DE DISPONIBILIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_namebufferoverflow_highavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_iot_namebufferoverflow_lowavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_iot_namebufferoverflow_mediumavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO\n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_namecommandexecution)+" VULNERABILIDADES EL NOMBRE INCLUYE COMMAND EXECUTION, LAS ESTADÍSTICAS DE IMPACTO DE DISPONIBILIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_namecommandexecution_highavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_iot_namecommandexecution_lowavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_iot_namecommandexecution_mediumavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO\n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_namespoofing)+" VULNERABILIDADES EL NOMBRE INCLUYE SPOOFING, LAS ESTADÍSTICAS DE IMPACTO DE DISPONIBILIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_namespoofing_highavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_iot_namespoofing_lowavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_iot_namespoofing_mediumavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO\n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_nameclickjacking)+" VULNERABILIDADES EL NOMBRE INCLUYE CLICKJACKING, LAS ESTADÍSTICAS DE IMPACTO DE DISPONIBILIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_nameclickjacking_highavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_iot_nameclickjacking_lowavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_iot_nameclickjacking_mediumavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO\n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_namehijacking)+" VULNERABILIDADES EL NOMBRE INCLUYE HIJACKING, LAS ESTADÍSTICAS DE IMPACTO DE DISPONIBILIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_namehijacking_highavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_iot_namehijacking_lowavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_iot_namehijacking_mediumavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO\n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_namefileinclude)+" VULNERABILIDADES EL NOMBRE INCLUYE FILEINCLUDE, LAS ESTADÍSTICAS DE IMPACTO DE DISPONIBILIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_namefileinclude_highavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_iot_namefileinclude_lowavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_iot_namefileinclude_mediumavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO\n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_namebruteforce)+" VULNERABILIDADES EL NOMBRE INCLUYE BRUTEFORCE, LAS ESTADÍSTICAS DE IMPACTO DE DISPONIBILIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_namebruteforce_highavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_iot_namebruteforce_lowavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_iot_namebruteforce_mediumavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO\n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_namefileupload)+" VULNERABILIDADES EL NOMBRE INCLUYE FILE UPLOAD, LAS ESTADÍSTICAS DE IMPACTO DE DISPONIBILIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_namefileupload_highavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_iot_namefileupload_lowavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_iot_namefileupload_mediumavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO\n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_nameheaderinjection)+" VULNERABILIDADES EL NOMBRE INCLUYE HEADER INJECTION, LAS ESTADÍSTICAS DE IMPACTO DE DISPONIBILIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_nameheaderinjection_highavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_iot_nameheaderinjection_lowavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_iot_nameheaderinjection_mediumavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO\n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_nametampering)+" VULNERABILIDADES EL NOMBRE INCLUYE TAMPERING, LAS ESTADÍSTICAS DE IMPACTO DE DISPONIBILIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_nametampering_highavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_iot_nametampering_lowavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_iot_nametampering_mediumavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO\n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_nameanother)+" VULNERABILIDADES EL NOMBRE INCLUYE OTRA CADENA, LAS ESTADÍSTICAS DE IMPACTO DE DISPONIBILIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_nameanother_highavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_iot_nameanother_lowavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_iot_nameanother_mediumavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO\n")
print("\n")





print("**********************************************PORCENTAJE NOMBRE/IMPACTO DE DISPONIBILIDAD VULNERABILIDADES IBM PARTE IOT**********************************************")
print("\n")                            
print("\n")
print(" DE UN TOTAL DE "+str(count_vulnibm_iot_names)+" VULNERABILIDADES :\n") 
print("\n")
print("   - LOS PORCENTAJES DE VALORES DE NOMBRE SON LOS SIGUIENTES:  \n")
print("      -    EN EL  "+str(float(((count_vulnibm_iot_namepathtraversal*100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE PATH TRAVERSAL, LOS PORCENTAJES DE IMPACTO DE DISPONIBILIDAD SON LOS SIGUIENTES :  \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namepathtraversal_highavaimpact*100)/count_vulnibm_iot_namepathtraversal)))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namepathtraversal_lowavaimpact*100)/count_vulnibm_iot_namepathtraversal)))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namepathtraversal_mediumavaimpact*100)/count_vulnibm_iot_namepathtraversal)))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO\n")
print("\n")
print("      -    EN EL  "+str(float(((count_vulnibm_iot_namedirectorytraversal*100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE DIRECTORY TRAVERSAL, LOS PORCENTAJES DE IMPACTO DE DISPONIBILIDAD SON LOS SIGUIENTES :  \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namedirectorytraversal_highavaimpact*100)/count_vulnibm_iot_namedirectorytraversal)))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namedirectorytraversal_lowavaimpact*100)/count_vulnibm_iot_namedirectorytraversal)))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namedirectorytraversal_mediumavaimpact*100)/count_vulnibm_iot_namedirectorytraversal)))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO\n")
print("\n")
print("      -    EN EL  "+str(float(((count_vulnibm_iot_nameprivilegeescalation*100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE PRIVILEGE ESCALATION, LOS PORCENTAJES DE IMPACTO DE DISPONIBILIDAD SON LOS SIGUIENTES :  \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_nameprivilegeescalation_highavaimpact*100)/count_vulnibm_iot_nameprivilegeescalation)))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_nameprivilegeescalation_lowavaimpact*100)/count_vulnibm_iot_nameprivilegeescalation)))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_nameprivilegeescalation_mediumavaimpact*100)/count_vulnibm_iot_nameprivilegeescalation)))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO\n")
print("\n")
print("      -    EN EL  "+str(float(((count_vulnibm_iot_namecrosssitescripting*100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE CROSS SITE SCRIPTING, LOS PORCENTAJES DE IMPACTO DE DISPONIBILIDAD SON LOS SIGUIENTES :  \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namecrosssitescripting_highavaimpact*100)/count_vulnibm_iot_namecrosssitescripting)))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namecrosssitescripting_lowavaimpact*100)/count_vulnibm_iot_namecrosssitescripting)))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namecrosssitescripting_mediumavaimpact*100)/count_vulnibm_iot_namecrosssitescripting)))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO\n")
print("\n")
print("      -    EN EL  "+str(float(((count_vulnibm_iot_namesecuritybypass*100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE SECURITY BYPASS, LOS PORCENTAJES DE IMPACTO DE DISPONIBILIDAD SON LOS SIGUIENTES :  \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namesecuritybypass_highavaimpact*100)/count_vulnibm_iot_namesecuritybypass)))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namesecuritybypass_lowavaimpact*100)/count_vulnibm_iot_namesecuritybypass)))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namesecuritybypass_mediumavaimpact*100)/count_vulnibm_iot_namesecuritybypass)))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO\n")
print("\n")
print("      -    EN EL  "+str(float(((count_vulnibm_iot_nameinformationdisclosure*100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE INFORMATION DISCLOSURE, LOS PORCENTAJES DE IMPACTO DE DISPONIBILIDAD SON LOS SIGUIENTES :  \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_nameinformationdisclosure_highavaimpact*100)/count_vulnibm_iot_nameinformationdisclosure)))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_nameinformationdisclosure_lowavaimpact*100)/count_vulnibm_iot_nameinformationdisclosure)))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_nameinformationdisclosure_mediumavaimpact*100)/count_vulnibm_iot_nameinformationdisclosure)))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO\n")
print("\n")
print("      -    EN EL  "+str(float(((count_vulnibm_iot_namedenialofservice*100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE DENIAL OF SERVICE, LOS PORCENTAJES DE IMPACTO DE DISPONIBILIDAD SON LOS SIGUIENTES :  \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namedenialofservice_highavaimpact*100)/count_vulnibm_iot_namedenialofservice)))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namedenialofservice_lowavaimpact*100)/count_vulnibm_iot_namedenialofservice)))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namedenialofservice_mediumavaimpact*100)/count_vulnibm_iot_namedenialofservice)))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO\n")
print("\n")
print("      -    EN EL  "+str(float(((count_vulnibm_iot_namecodeexecution*100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE CODE EXECUTION, LOS PORCENTAJES DE IMPACTO DE DISPONIBILIDAD SON LOS SIGUIENTES :  \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namecodeexecution_highavaimpact*100)/count_vulnibm_iot_namecodeexecution)))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namecodeexecution_lowavaimpact*100)/count_vulnibm_iot_namecodeexecution)))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namecodeexecution_mediumavaimpact*100)/count_vulnibm_iot_namecodeexecution)))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO\n")
print("\n")
print("      -    EN EL  "+str(float(((count_vulnibm_iot_namemaninthemiddle*100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE MAN IN THE MIDDLE, LOS PORCENTAJES DE IMPACTO DE DISPONIBILIDAD SON LOS SIGUIENTES :  \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namemaninthemiddle_highavaimpact*100)/count_vulnibm_iot_namemaninthemiddle)))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namemaninthemiddle_lowavaimpact*100)/count_vulnibm_iot_namemaninthemiddle)))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namemaninthemiddle_mediumavaimpact*100)/count_vulnibm_iot_namemaninthemiddle)))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO\n")
print("\n")
print("      -    EN EL  "+str(float(((count_vulnibm_iot_namesqlinjection*100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE SQL INJECTION, LOS PORCENTAJES DE IMPACTO DE DISPONIBILIDAD SON LOS SIGUIENTES :  \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namesqlinjection_highavaimpact*100)/count_vulnibm_iot_namesqlinjection)))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namesqlinjection_lowavaimpact*100)/count_vulnibm_iot_namesqlinjection)))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namesqlinjection_mediumavaimpact*100)/count_vulnibm_iot_namesqlinjection)))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO\n")
print("\n")
print("      -    EN EL  "+str(float(((count_vulnibm_iot_namecrosssiterequestforgery*100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE CROSS SITE REQUEST FORGERY, LOS PORCENTAJES DE IMPACTO DE DISPONIBILIDAD SON LOS SIGUIENTES :  \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namecrosssiterequestforgery_highavaimpact*100)/count_vulnibm_iot_namecrosssiterequestforgery)))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namecrosssiterequestforgery_lowavaimpact*100)/count_vulnibm_iot_namecrosssiterequestforgery)))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namecrosssiterequestforgery_mediumavaimpact*100)/count_vulnibm_iot_namecrosssiterequestforgery)))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO\n")
print("\n")
print("      -    EN EL  "+str(float(((count_vulnibm_iot_namemoduleexecution*100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE MODULE EXECUTION, LOS PORCENTAJES DE IMPACTO DE DISPONIBILIDAD SON LOS SIGUIENTES :  \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namemoduleexecution_highavaimpact*100)/count_vulnibm_iot_namemoduleexecution)))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namemoduleexecution_lowavaimpact*100)/count_vulnibm_iot_namemoduleexecution)))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namemoduleexecution_mediumavaimpact*100)/count_vulnibm_iot_namemoduleexecution)))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO\n")
print("\n")
print("      -    EN EL  "+str(float(((count_vulnibm_iot_namebufferoverflow*100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE BUFFER OVERFLOW, LOS PORCENTAJES DE IMPACTO DE DISPONIBILIDAD SON LOS SIGUIENTES :  \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namebufferoverflow_highavaimpact*100)/count_vulnibm_iot_namebufferoverflow)))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namebufferoverflow_lowavaimpact*100)/count_vulnibm_iot_namebufferoverflow)))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namebufferoverflow_mediumavaimpact*100)/count_vulnibm_iot_namebufferoverflow)))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO\n")
print("\n")
print("      -    EN EL  "+str(float(((count_vulnibm_iot_namecommandexecution*100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE COMMAND EXECUTION, LOS PORCENTAJES DE IMPACTO DE DISPONIBILIDAD SON LOS SIGUIENTES :  \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namecommandexecution_highavaimpact*100)/count_vulnibm_iot_namecommandexecution)))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namecommandexecution_lowavaimpact*100)/count_vulnibm_iot_namecommandexecution)))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namecommandexecution_mediumavaimpact*100)/count_vulnibm_iot_namecommandexecution)))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO\n")
print("\n")
print("      -    EN EL  "+str(float(((count_vulnibm_iot_namespoofing*100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE SPOOFING, LOS PORCENTAJES DE IMPACTO DE DISPONIBILIDAD SON LOS SIGUIENTES :  \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namespoofing_highavaimpact*100)/count_vulnibm_iot_namespoofing)))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namespoofing_lowavaimpact*100)/count_vulnibm_iot_namespoofing)))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namespoofing_mediumavaimpact*100)/count_vulnibm_iot_namespoofing)))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO\n")
print("\n")
print("      -    EN EL  "+str(float(((count_vulnibm_iot_nameclickjacking*100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE CLICKJACKING, LOS PORCENTAJES DE IMPACTO DE DISPONIBILIDAD SON LOS SIGUIENTES :  \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_nameclickjacking_highavaimpact*100)/count_vulnibm_iot_nameclickjacking)))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_nameclickjacking_lowavaimpact*100)/count_vulnibm_iot_nameclickjacking)))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_nameclickjacking_mediumavaimpact*100)/count_vulnibm_iot_nameclickjacking)))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO\n")
print("\n")
print("      -    EN EL  "+str(float(((count_vulnibm_iot_namehijacking*100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE HIJACKING, LOS PORCENTAJES DE IMPACTO DE DISPONIBILIDAD SON LOS SIGUIENTES :  \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namehijacking_highavaimpact*100)/count_vulnibm_iot_namehijacking)))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namehijacking_lowavaimpact*100)/count_vulnibm_iot_namehijacking)))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namehijacking_mediumavaimpact*100)/count_vulnibm_iot_namehijacking)))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO\n")
print("\n")
print("      -    EN EL  "+str(float(((count_vulnibm_iot_namefileinclude*100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE FILEINCLUDE, LOS PORCENTAJES DE IMPACTO DE DISPONIBILIDAD SON LOS SIGUIENTES :  \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namefileinclude_highavaimpact*100)/count_vulnibm_iot_namefileinclude)))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namefileinclude_lowavaimpact*100)/count_vulnibm_iot_namefileinclude)))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namefileinclude_mediumavaimpact*100)/count_vulnibm_iot_namefileinclude)))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO\n")
print("\n")
print("      -    EN EL  "+str(float(((count_vulnibm_iot_namebruteforce*100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE BRUTEFORCE, LOS PORCENTAJES DE IMPACTO DE DISPONIBILIDAD SON LOS SIGUIENTES :  \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namebruteforce_highavaimpact*100)/count_vulnibm_iot_namebruteforce)))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namebruteforce_lowavaimpact*100)/count_vulnibm_iot_namebruteforce)))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namebruteforce_mediumavaimpact*100)/count_vulnibm_iot_namebruteforce)))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO\n")
print("\n")
print("      -    EN EL  "+str(float(((count_vulnibm_iot_namefileupload*100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE FILE UPLOAD, LOS PORCENTAJES DE IMPACTO DE DISPONIBILIDAD SON LOS SIGUIENTES :  \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namefileupload_highavaimpact*100)/count_vulnibm_iot_namefileupload)))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namefileupload_lowavaimpact*100)/count_vulnibm_iot_namefileupload)))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namefileupload_mediumavaimpact*100)/count_vulnibm_iot_namefileupload)))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO\n")
print("\n")
if(count_vulnibm_iot_nameheaderinjection>0):
    print("      -    EN EL  "+str(float(((count_vulnibm_iot_nameheaderinjection*100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE HEADER INJECTION, LOS PORCENTAJES DE IMPACTO DE DISPONIBILIDAD SON LOS SIGUIENTES :  \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_nameheaderinjection_highavaimpact*100)/count_vulnibm_iot_nameheaderinjection)))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_nameheaderinjection_lowavaimpact*100)/count_vulnibm_iot_nameheaderinjection)))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_nameheaderinjection_mediumavaimpact*100)/count_vulnibm_iot_nameheaderinjection)))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO\n")
    print("\n")
if(count_vulnibm_iot_nametampering>0):
    print("      -    EN EL  "+str(float(((count_vulnibm_iot_nametampering*100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE TAMPERING, LOS PORCENTAJES DE IMPACTO DE DISPONIBILIDAD SON LOS SIGUIENTES :  \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_nametampering_highavaimpact*100)/count_vulnibm_iot_nametampering)))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_nametampering_lowavaimpact*100)/count_vulnibm_iot_nametampering)))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_nametampering_mediumavaimpact*100)/count_vulnibm_iot_nametampering)))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO\n")
    print("\n")
    print("      -    EN EL  "+str(float(((count_vulnibm_iot_nameanother*100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE OTRA CADENA, LOS PORCENTAJES DE IMPACTO DE DISPONIBILIDAD SON LOS SIGUIENTES :  \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_nameanother_highavaimpact*100)/count_vulnibm_iot_nameanother)))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_nameanother_lowavaimpact*100)/count_vulnibm_iot_nameanother)))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_nameanother_mediumavaimpact*100)/count_vulnibm_iot_nameanother)))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO\n")
    print("\n")




    
    
    




#Abro los ficheros con los que voy a tratar




df_vulnibm_sh = pd.read_excel('vulnerabilidades_ibm_smart_home_2023.xlsx')

#Variable para almacenar el contador total de valores de nombre
count_vulnibm_sh_names=0
#Variable para almacenar el contador total de valores de un nombre concreto
count_vulnibm_sh_namepathtraversal=0
#Variables para almacenar el contador de valores de impacto de DISPONIBILIDAD dato un valor de nombre especifico
count_vulnibm_sh_namepathtraversal_avaimpact=0
count_vulnibm_sh_namepathtraversal_highavaimpact=0
count_vulnibm_sh_namepathtraversal_lowavaimpact=0
count_vulnibm_sh_namepathtraversal_mediumavaimpact=0

count_vulnibm_sh_namedirectorytraversal=0
count_vulnibm_sh_namedirectorytraversal_avaimpact=0
count_vulnibm_sh_namedirectorytraversal_highavaimpact=0
count_vulnibm_sh_namedirectorytraversal_lowavaimpact=0
count_vulnibm_sh_namedirectorytraversal_mediumavaimpact=0

count_vulnibm_sh_nameprivilegeescalation=0
count_vulnibm_sh_nameprivilegeescalation_avaimpact=0
count_vulnibm_sh_nameprivilegeescalation_highavaimpact=0
count_vulnibm_sh_nameprivilegeescalation_lowavaimpact=0
count_vulnibm_sh_nameprivilegeescalation_mediumavaimpact=0

count_vulnibm_sh_namecrosssitescripting=0
count_vulnibm_sh_namecrosssitescripting_avaimpact=0
count_vulnibm_sh_namecrosssitescripting_highavaimpact=0
count_vulnibm_sh_namecrosssitescripting_lowavaimpact=0
count_vulnibm_sh_namecrosssitescripting_mediumavaimpact=0

count_vulnibm_sh_namesecuritybypass=0
count_vulnibm_sh_namesecuritybypass_avaimpact=0
count_vulnibm_sh_namesecuritybypass_highavaimpact=0
count_vulnibm_sh_namesecuritybypass_lowavaimpact=0
count_vulnibm_sh_namesecuritybypass_mediumavaimpact=0

count_vulnibm_sh_nameinformationdisclosure=0
count_vulnibm_sh_nameinformationdisclosure_avaimpact=0
count_vulnibm_sh_nameinformationdisclosure_highavaimpact=0
count_vulnibm_sh_nameinformationdisclosure_lowavaimpact=0
count_vulnibm_sh_nameinformationdisclosure_mediumavaimpact=0

count_vulnibm_sh_namedenialofservice=0
count_vulnibm_sh_namedenialofservice_avaimpact=0
count_vulnibm_sh_namedenialofservice_highavaimpact=0
count_vulnibm_sh_namedenialofservice_lowavaimpact=0
count_vulnibm_sh_namedenialofservice_mediumavaimpact=0

count_vulnibm_sh_namecodeexecution=0
count_vulnibm_sh_namecodeexecution_avaimpact=0
count_vulnibm_sh_namecodeexecution_highavaimpact=0
count_vulnibm_sh_namecodeexecution_lowavaimpact=0
count_vulnibm_sh_namecodeexecution_mediumavaimpact=0

count_vulnibm_sh_namemaninthemiddle=0
count_vulnibm_sh_namemaninthemiddle_avaimpact=0
count_vulnibm_sh_namemaninthemiddle_highavaimpact=0
count_vulnibm_sh_namemaninthemiddle_lowavaimpact=0
count_vulnibm_sh_namemaninthemiddle_mediumavaimpact=0

count_vulnibm_sh_namesqlinjection=0
count_vulnibm_sh_namesqlinjection_avaimpact=0
count_vulnibm_sh_namesqlinjection_highavaimpact=0
count_vulnibm_sh_namesqlinjection_lowavaimpact=0
count_vulnibm_sh_namesqlinjection_mediumavaimpact=0

count_vulnibm_sh_namecrosssiterequestforgery=0
count_vulnibm_sh_namecrosssiterequestforgery_avaimpact=0
count_vulnibm_sh_namecrosssiterequestforgery_highavaimpact=0
count_vulnibm_sh_namecrosssiterequestforgery_lowavaimpact=0
count_vulnibm_sh_namecrosssiterequestforgery_mediumavaimpact=0

count_vulnibm_sh_namemoduleexecution=0
count_vulnibm_sh_namemoduleexecution_avaimpact=0
count_vulnibm_sh_namemoduleexecution_highavaimpact=0
count_vulnibm_sh_namemoduleexecution_lowavaimpact=0
count_vulnibm_sh_namemoduleexecution_mediumavaimpact=0

count_vulnibm_sh_namebufferoverflow=0
count_vulnibm_sh_namebufferoverflow_avaimpact=0
count_vulnibm_sh_namebufferoverflow_highavaimpact=0
count_vulnibm_sh_namebufferoverflow_lowavaimpact=0
count_vulnibm_sh_namebufferoverflow_mediumavaimpact=0

count_vulnibm_sh_namecommandexecution=0
count_vulnibm_sh_namecommandexecution_avaimpact=0
count_vulnibm_sh_namecommandexecution_highavaimpact=0
count_vulnibm_sh_namecommandexecution_lowavaimpact=0
count_vulnibm_sh_namecommandexecution_mediumavaimpact=0

count_vulnibm_sh_namespoofing=0
count_vulnibm_sh_namespoofing_avaimpact=0
count_vulnibm_sh_namespoofing_highavaimpact=0
count_vulnibm_sh_namespoofing_lowavaimpact=0
count_vulnibm_sh_namespoofing_mediumavaimpact=0

count_vulnibm_sh_nameclickjacking=0
count_vulnibm_sh_nameclickjacking_avaimpact=0
count_vulnibm_sh_nameclickjacking_highavaimpact=0
count_vulnibm_sh_nameclickjacking_lowavaimpact=0
count_vulnibm_sh_nameclickjacking_mediumavaimpact=0

count_vulnibm_sh_namehijacking=0
count_vulnibm_sh_namehijacking_avaimpact=0
count_vulnibm_sh_namehijacking_highavaimpact=0
count_vulnibm_sh_namehijacking_lowavaimpact=0
count_vulnibm_sh_namehijacking_mediumavaimpact=0

count_vulnibm_sh_namefileinclude=0
count_vulnibm_sh_namefileinclude_avaimpact=0
count_vulnibm_sh_namefileinclude_highavaimpact=0
count_vulnibm_sh_namefileinclude_lowavaimpact=0
count_vulnibm_sh_namefileinclude_mediumavaimpact=0

count_vulnibm_sh_namebruteforce=0
count_vulnibm_sh_namebruteforce_avaimpact=0
count_vulnibm_sh_namebruteforce_highavaimpact=0
count_vulnibm_sh_namebruteforce_lowavaimpact=0
count_vulnibm_sh_namebruteforce_mediumavaimpact=0

count_vulnibm_sh_namefileupload=0
count_vulnibm_sh_namefileupload_avaimpact=0
count_vulnibm_sh_namefileupload_highavaimpact=0
count_vulnibm_sh_namefileupload_lowavaimpact=0
count_vulnibm_sh_namefileupload_mediumavaimpact=0

count_vulnibm_sh_nameheaderinjection=0
count_vulnibm_sh_nameheaderinjection_avaimpact=0
count_vulnibm_sh_nameheaderinjection_highavaimpact=0
count_vulnibm_sh_nameheaderinjection_lowavaimpact=0
count_vulnibm_sh_nameheaderinjection_mediumavaimpact=0

count_vulnibm_sh_nametampering=0
count_vulnibm_sh_nametampering_avaimpact=0
count_vulnibm_sh_nametampering_highavaimpact=0
count_vulnibm_sh_nametampering_lowavaimpact=0
count_vulnibm_sh_nametampering_mediumavaimpact=0

count_vulnibm_sh_nameanother=0
count_vulnibm_sh_nameanother_avaimpact=0
count_vulnibm_sh_nameanother_highavaimpact=0
count_vulnibm_sh_nameanother_lowavaimpact=0
count_vulnibm_sh_nameanother_mediumavaimpact=0

#Comprobamos el contenido de name
for r in range(0,len(df_vulnibm_sh["name"])):                       
    aux_str=df_vulnibm_sh["name"][r].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
    if(aux_str!='NONE'):
        count_vulnibm_sh_names+=1
        #Compruebo el valor de nombre
        if('pathtraversal' in aux_str):
            count_vulnibm_sh_namepathtraversal+=1
            #Compruebo el valor de impacto de DISPONIBILIDAD
            if(df_vulnibm_sh["x_xfe_cvss_availability_impact"][r]=='High'):
                count_vulnibm_sh_namepathtraversal_avaimpact+=1
                count_vulnibm_sh_namepathtraversal_highavaimpact+=1
            elif(df_vulnibm_sh["x_xfe_cvss_availability_impact"][r]=='Low'):
                count_vulnibm_sh_namepathtraversal_avaimpact+=1
                count_vulnibm_sh_namepathtraversal_lowavaimpact+=1
            elif(df_vulnibm_sh["x_xfe_cvss_availability_impact"][r]=='Medium'):
                count_vulnibm_sh_namepathtraversal_avaimpact+=1
                count_vulnibm_sh_namepathtraversal_mediumavaimpact+=1
    
        elif('directorytraversal' in aux_str):
            
            count_vulnibm_sh_namedirectorytraversal+=1
            if(df_vulnibm_sh["x_xfe_cvss_availability_impact"][r]=='High'):
                count_vulnibm_sh_namedirectorytraversal_avaimpact+=1
                count_vulnibm_sh_namedirectorytraversal_highavaimpact+=1
            elif(df_vulnibm_sh["x_xfe_cvss_availability_impact"][r]=='Low'):
                count_vulnibm_sh_namedirectorytraversal_avaimpact+=1
                count_vulnibm_sh_namedirectorytraversal_lowavaimpact+=1
            elif(df_vulnibm_sh["x_xfe_cvss_availability_impact"][r]=='Medium'):
                count_vulnibm_sh_namedirectorytraversal_avaimpact+=1
                count_vulnibm_sh_namedirectorytraversal_mediumavaimpact+=1
            
            
        elif('privilegeescalation' in aux_str):
        
            count_vulnibm_sh_nameprivilegeescalation+=1
            if(df_vulnibm_sh["x_xfe_cvss_availability_impact"][r]=='High'):
                count_vulnibm_sh_nameprivilegeescalation_avaimpact+=1
                count_vulnibm_sh_nameprivilegeescalation_highavaimpact+=1
            elif(df_vulnibm_sh["x_xfe_cvss_availability_impact"][r]=='Low'):
                count_vulnibm_sh_nameprivilegeescalation_avaimpact+=1
                count_vulnibm_sh_nameprivilegeescalation_lowavaimpact+=1
            elif(df_vulnibm_sh["x_xfe_cvss_availability_impact"][r]=='Medium'):
                count_vulnibm_sh_nameprivilegeescalation_avaimpact+=1
                count_vulnibm_sh_nameprivilegeescalation_mediumavaimpact+=1
            
        elif('cross-sitescripting' in aux_str):
        
            count_vulnibm_sh_namecrosssitescripting+=1
            if(df_vulnibm_sh["x_xfe_cvss_availability_impact"][r]=='High'):
                count_vulnibm_sh_namecrosssitescripting_avaimpact+=1
                count_vulnibm_sh_namecrosssitescripting_highavaimpact+=1
            elif(df_vulnibm_sh["x_xfe_cvss_availability_impact"][r]=='Low'):
                count_vulnibm_sh_namecrosssitescripting_avaimpact+=1
                count_vulnibm_sh_namecrosssitescripting_lowavaimpact+=1
            elif(df_vulnibm_sh["x_xfe_cvss_availability_impact"][r]=='Medium'):
                count_vulnibm_sh_namecrosssitescripting_avaimpact+=1
                count_vulnibm_sh_namecrosssitescripting_mediumavaimpact+=1
                                         
        elif('securitybypass' in aux_str):
        
            count_vulnibm_sh_namesecuritybypass+=1
            if(df_vulnibm_sh["x_xfe_cvss_availability_impact"][r]=='High'):
                count_vulnibm_sh_namesecuritybypass_avaimpact+=1
                count_vulnibm_sh_namesecuritybypass_highavaimpact+=1
            elif(df_vulnibm_sh["x_xfe_cvss_availability_impact"][r]=='Low'):
                count_vulnibm_sh_namesecuritybypass_avaimpact+=1
                count_vulnibm_sh_namesecuritybypass_lowavaimpact+=1
            elif(df_vulnibm_sh["x_xfe_cvss_availability_impact"][r]=='Medium'):
                count_vulnibm_sh_namesecuritybypass_avaimpact+=1
                count_vulnibm_sh_namesecuritybypass_mediumavaimpact+=1
                                         
        elif('information_disclosure' in aux_str or 'informationdisclosure' in aux_str):
        
            count_vulnibm_sh_nameinformationdisclosure+=1
            if(df_vulnibm_sh["x_xfe_cvss_availability_impact"][r]=='High'):
                count_vulnibm_sh_nameinformationdisclosure_avaimpact+=1
                count_vulnibm_sh_nameinformationdisclosure_highavaimpact+=1
            elif(df_vulnibm_sh["x_xfe_cvss_availability_impact"][r]=='Low'):
                count_vulnibm_sh_nameinformationdisclosure_avaimpact+=1
                count_vulnibm_sh_nameinformationdisclosure_lowavaimpact+=1
            elif(df_vulnibm_sh["x_xfe_cvss_availability_impact"][r]=='Medium'):
                count_vulnibm_sh_nameinformationdisclosure_avaimpact+=1
                count_vulnibm_sh_nameinformationdisclosure_mediumavaimpact+=1
                                         
        elif('denialofservice' in aux_str):
            
            count_vulnibm_sh_namedenialofservice+=1
            if(df_vulnibm_sh["x_xfe_cvss_availability_impact"][r]=='High'):
                count_vulnibm_sh_namedenialofservice_avaimpact+=1
                count_vulnibm_sh_namedenialofservice_highavaimpact+=1
            elif(df_vulnibm_sh["x_xfe_cvss_availability_impact"][r]=='Low'):
                count_vulnibm_sh_namedenialofservice_avaimpact+=1
                count_vulnibm_sh_namedenialofservice_lowavaimpact+=1
            elif(df_vulnibm_sh["x_xfe_cvss_availability_impact"][r]=='Medium'):
                count_vulnibm_sh_namedenialofservice_avaimpact+=1
                count_vulnibm_sh_namedenialofservice_mediumavaimpact+=1
            
        elif('codeexecution' in aux_str):
        
        
            count_vulnibm_sh_namecodeexecution+=1
            if(df_vulnibm_sh["x_xfe_cvss_availability_impact"][r]=='High'):
                count_vulnibm_sh_namecodeexecution_avaimpact+=1
                count_vulnibm_sh_namecodeexecution_highavaimpact+=1
            elif(df_vulnibm_sh["x_xfe_cvss_availability_impact"][r]=='Low'):
                count_vulnibm_sh_namecodeexecution_avaimpact+=1
                count_vulnibm_sh_namecodeexecution_lowavaimpact+=1
            elif(df_vulnibm_sh["x_xfe_cvss_availability_impact"][r]=='Medium'):
                count_vulnibm_sh_namecodeexecution_avaimpact+=1
                count_vulnibm_sh_namecodeexecution_mediumavaimpact+=1
                                         
        elif('maninthemiddle' in aux_str):
        
            count_vulnibm_sh_namemaninthemiddle+=1
            if(df_vulnibm_sh["x_xfe_cvss_availability_impact"][r]=='High'):
                count_vulnibm_sh_namemaninthemiddle_avaimpact+=1
                count_vulnibm_sh_namemaninthemiddle_highavaimpact+=1
            elif(df_vulnibm_sh["x_xfe_cvss_availability_impact"][r]=='Low'):
                count_vulnibm_sh_namemaninthemiddle_avaimpact+=1
                count_vulnibm_sh_namemaninthemiddle_lowavaimpact+=1
            elif(df_vulnibm_sh["x_xfe_cvss_availability_impact"][r]=='Medium'):
                count_vulnibm_sh_namemaninthemiddle_avaimpact+=1
                count_vulnibm_sh_namemaninthemiddle_mediumavaimpact+=1
                                         
        elif('SQLinjection' in aux_str):
        
            count_vulnibm_sh_namesqlinjection+=1
            if(df_vulnibm_sh["x_xfe_cvss_availability_impact"][r]=='High'):
                count_vulnibm_sh_namesqlinjection_avaimpact+=1
                count_vulnibm_sh_namesqlinjection_highavaimpact+=1
            elif(df_vulnibm_sh["x_xfe_cvss_availability_impact"][r]=='Low'):
                count_vulnibm_sh_namesqlinjection_avaimpact+=1
                count_vulnibm_sh_namesqlinjection_lowavaimpact+=1
            elif(df_vulnibm_sh["x_xfe_cvss_availability_impact"][r]=='Medium'):
                count_vulnibm_sh_namesqlinjection_avaimpact+=1
                count_vulnibm_sh_namesqlinjection_mediumavaimpact+=1
                                         
        elif('cross-siterequestforgery' in aux_str):
        
            count_vulnibm_sh_namecrosssiterequestforgery+=1
            if(df_vulnibm_sh["x_xfe_cvss_availability_impact"][r]=='High'):
                count_vulnibm_sh_namecrosssiterequestforgery_avaimpact+=1
                count_vulnibm_sh_namecrosssiterequestforgery_highavaimpact+=1
            elif(df_vulnibm_sh["x_xfe_cvss_availability_impact"][r]=='Low'):
                count_vulnibm_sh_namecrosssiterequestforgery_avaimpact+=1
                count_vulnibm_sh_namecrosssiterequestforgery_lowavaimpact+=1
            elif(df_vulnibm_sh["x_xfe_cvss_availability_impact"][r]=='Medium'):
                count_vulnibm_sh_namecrosssiterequestforgery_avaimpact+=1
                count_vulnibm_sh_namecrosssiterequestforgery_mediumavaimpact+=1
                                         
        elif('moduleexecution' in aux_str):
        
            count_vulnibm_sh_namemoduleexecution+=1
            if(df_vulnibm_sh["x_xfe_cvss_availability_impact"][r]=='High'):
                count_vulnibm_sh_namemoduleexecution_avaimpact+=1
                count_vulnibm_sh_namemoduleexecution_highavaimpact+=1
            elif(df_vulnibm_sh["x_xfe_cvss_availability_impact"][r]=='Low'):
                count_vulnibm_sh_namemoduleexecution_avaimpact+=1
                count_vulnibm_sh_namemoduleexecution_lowavaimpact+=1
            elif(df_vulnibm_sh["x_xfe_cvss_availability_impact"][r]=='Medium'):
                count_vulnibm_sh_namemoduleexecution_avaimpact+=1
                count_vulnibm_sh_namemoduleexecution_mediumavaimpact+=1
                                         
        elif('bufferoverflow' in aux_str):
        
            count_vulnibm_sh_namebufferoverflow+=1
            if(df_vulnibm_sh["x_xfe_cvss_availability_impact"][r]=='High'):
                count_vulnibm_sh_namebufferoverflow_avaimpact+=1
                count_vulnibm_sh_namebufferoverflow_highavaimpact+=1
            elif(df_vulnibm_sh["x_xfe_cvss_availability_impact"][r]=='Low'):
                count_vulnibm_sh_namebufferoverflow_avaimpact+=1
                count_vulnibm_sh_namebufferoverflow_lowavaimpact+=1
            elif(df_vulnibm_sh["x_xfe_cvss_availability_impact"][r]=='Medium'):
                count_vulnibm_sh_namebufferoverflow_avaimpact+=1
                count_vulnibm_sh_namebufferoverflow_mediumavaimpact+=1
                                         
        elif('commandexecution' in aux_str):
        
            count_vulnibm_sh_namecommandexecution+=1
            if(df_vulnibm_sh["x_xfe_cvss_availability_impact"][r]=='High'):
                count_vulnibm_sh_namecommandexecution_avaimpact+=1
                count_vulnibm_sh_namecommandexecution_highavaimpact+=1
            elif(df_vulnibm_sh["x_xfe_cvss_availability_impact"][r]=='Low'):
                count_vulnibm_sh_namecommandexecution_avaimpact+=1
                count_vulnibm_sh_namecommandexecution_lowavaimpact+=1
            elif(df_vulnibm_sh["x_xfe_cvss_availability_impact"][r]=='Medium'):
                count_vulnibm_sh_namecommandexecution_avaimpact+=1
                count_vulnibm_sh_namecommandexecution_mediumavaimpact+=1
                                         
        elif('spoofing' in aux_str):
        
            count_vulnibm_sh_namespoofing+=1
            if(df_vulnibm_sh["x_xfe_cvss_availability_impact"][r]=='High'):
                count_vulnibm_sh_namespoofing_avaimpact+=1
                count_vulnibm_sh_namespoofing_highavaimpact+=1
            elif(df_vulnibm_sh["x_xfe_cvss_availability_impact"][r]=='Low'):
                count_vulnibm_sh_namespoofing_avaimpact+=1
                count_vulnibm_sh_namespoofing_lowavaimpact+=1
            elif(df_vulnibm_sh["x_xfe_cvss_availability_impact"][r]=='Medium'):
                count_vulnibm_sh_namespoofing_avaimpact+=1
                count_vulnibm_sh_namespoofing_mediumavaimpact+=1
                                         
        elif('clickjacking' in aux_str):
        
            count_vulnibm_sh_nameclickjacking+=1
            if(df_vulnibm_sh["x_xfe_cvss_availability_impact"][r]=='High'):
                count_vulnibm_sh_nameclickjacking_avaimpact+=1
                count_vulnibm_sh_nameclickjacking_highavaimpact+=1
            elif(df_vulnibm_sh["x_xfe_cvss_availability_impact"][r]=='Low'):
                count_vulnibm_sh_nameclickjacking_avaimpact+=1
                count_vulnibm_sh_nameclickjacking_lowavaimpact+=1
            elif(df_vulnibm_sh["x_xfe_cvss_availability_impact"][r]=='Medium'):
                count_vulnibm_sh_nameclickjacking_avaimpact+=1
                count_vulnibm_sh_nameclickjacking_mediumavaimpact+=1
              
        elif('hijacking' in aux_str):
        
            count_vulnibm_sh_namehijacking+=1
            if(df_vulnibm_sh["x_xfe_cvss_availability_impact"][r]=='High'):
                count_vulnibm_sh_namehijacking_avaimpact+=1
                count_vulnibm_sh_namehijacking_highavaimpact+=1
            elif(df_vulnibm_sh["x_xfe_cvss_availability_impact"][r]=='Low'):
                count_vulnibm_sh_namehijacking_avaimpact+=1
                count_vulnibm_sh_namehijacking_lowavaimpact+=1
            elif(df_vulnibm_sh["x_xfe_cvss_availability_impact"][r]=='Medium'):
                count_vulnibm_sh_namehijacking_avaimpact+=1
                count_vulnibm_sh_namehijacking_mediumavaimpact+=1
               
        elif('fileinclude' in aux_str):
        
            count_vulnibm_sh_namefileinclude+=1
            if(df_vulnibm_sh["x_xfe_cvss_availability_impact"][r]=='High'):
                count_vulnibm_sh_namefileinclude_avaimpact+=1
                count_vulnibm_sh_namefileinclude_highavaimpact+=1
            elif(df_vulnibm_sh["x_xfe_cvss_availability_impact"][r]=='Low'):
                count_vulnibm_sh_namefileinclude_avaimpact+=1
                count_vulnibm_sh_namefileinclude_lowavaimpact+=1
            elif(df_vulnibm_sh["x_xfe_cvss_availability_impact"][r]=='Medium'):
                count_vulnibm_sh_namefileinclude_avaimpact+=1
                count_vulnibm_sh_namefileinclude_mediumavaimpact+=1
                
               
        elif('bruteforce' in aux_str):
        
            count_vulnibm_sh_namebruteforce+=1
            if(df_vulnibm_sh["x_xfe_cvss_availability_impact"][r]=='High'):
                count_vulnibm_sh_namebruteforce_avaimpact+=1
                count_vulnibm_sh_namebruteforce_highavaimpact+=1
            elif(df_vulnibm_sh["x_xfe_cvss_availability_impact"][r]=='Low'):
                count_vulnibm_sh_namebruteforce_avaimpact+=1
                count_vulnibm_sh_namebruteforce_lowavaimpact+=1
            elif(df_vulnibm_sh["x_xfe_cvss_availability_impact"][r]=='Medium'):
                count_vulnibm_sh_namebruteforce_avaimpact+=1
                count_vulnibm_sh_namebruteforce_mediumavaimpact+=1
                
               
        elif('fileupload' in aux_str):
        
            count_vulnibm_sh_namefileupload+=1
            if(df_vulnibm_sh["x_xfe_cvss_availability_impact"][r]=='High'):
                count_vulnibm_sh_namefileupload_avaimpact+=1
                count_vulnibm_sh_namefileupload_highavaimpact+=1
            elif(df_vulnibm_sh["x_xfe_cvss_availability_impact"][r]=='Low'):
                count_vulnibm_sh_namefileupload_avaimpact+=1
                count_vulnibm_sh_namefileupload_lowavaimpact+=1
            elif(df_vulnibm_sh["x_xfe_cvss_availability_impact"][r]=='Medium'):
                count_vulnibm_sh_namefileupload_avaimpact+=1
                count_vulnibm_sh_namefileupload_mediumavaimpact+=1
                
               
        elif('headerinjection' in aux_str):
        
            count_vulnibm_sh_nameheaderinjection+=1
            if(df_vulnibm_sh["x_xfe_cvss_availability_impact"][r]=='High'):
                count_vulnibm_sh_nameheaderinjection_avaimpact+=1
                count_vulnibm_sh_nameheaderinjection_highavaimpact+=1
            elif(df_vulnibm_sh["x_xfe_cvss_availability_impact"][r]=='Low'):
                count_vulnibm_sh_nameheaderinjection_avaimpact+=1
                count_vulnibm_sh_nameheaderinjection_lowavaimpact+=1
            elif(df_vulnibm_sh["x_xfe_cvss_availability_impact"][r]=='Medium'):
                count_vulnibm_sh_nameheaderinjection_avaimpact+=1
                count_vulnibm_sh_nameheaderinjection_mediumavaimpact+=1
               
        elif('Tampering' in aux_str):
        
            count_vulnibm_sh_nametampering+=1
            if(df_vulnibm_sh["x_xfe_cvss_availability_impact"][r]=='High'):
                count_vulnibm_sh_nametampering_avaimpact+=1
                count_vulnibm_sh_nametampering_highavaimpact+=1
            elif(df_vulnibm_sh["x_xfe_cvss_availability_impact"][r]=='Low'):
                count_vulnibm_sh_nametampering_avaimpact+=1
                count_vulnibm_sh_nametampering_lowavaimpact+=1
            elif(df_vulnibm_sh["x_xfe_cvss_availability_impact"][r]=='Medium'):
                count_vulnibm_sh_nametampering_avaimpact+=1
                count_vulnibm_sh_nametampering_mediumavaimpact+=1
    
        else:
        
            count_vulnibm_sh_nameanother+=1
            if(df_vulnibm_sh["x_xfe_cvss_availability_impact"][r]=='High'):
                count_vulnibm_sh_nameanother_avaimpact+=1
                count_vulnibm_sh_nameanother_highavaimpact+=1
            elif(df_vulnibm_sh["x_xfe_cvss_availability_impact"][r]=='Low'):
                count_vulnibm_sh_nameanother_avaimpact+=1
                count_vulnibm_sh_nameanother_lowavaimpact+=1
            elif(df_vulnibm_sh["x_xfe_cvss_availability_impact"][r]=='Medium'):
                count_vulnibm_sh_nameanother_avaimpact+=1
                count_vulnibm_sh_nameanother_mediumavaimpact+=1
                
                
                
                
                
print("**********************************************ESTADÍSTICAS NOMBRE/IMPACTO DE DISPONIBILIDAD VULNERABILIDADES IBM PARTE SMART HOME**********************************************")
print("\n")                            
print("\n")
print(" DE UN TOTAL DE "+str(count_vulnibm_sh_names)+" VULNERABILIDADES:\n") 
print("\n")
print("   - LAS ESTADISTICAS DE VALORES DE NOMBRE SON LAS SIGUIENTES:  \n")
print("      -    EN  "+str(count_vulnibm_sh_namepathtraversal)+" VULNERABILIDADES EL NOMBRE INCLUYE PATH TRAVERSAL, LAS ESTADÍSTICAS DE IMPACTO DE DISPONIBILIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_sh_namepathtraversal_highavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_sh_namepathtraversal_lowavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_sh_namepathtraversal_mediumavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO\n")
print("\n")
print("      -    EN  "+str(count_vulnibm_sh_namedirectorytraversal)+" VULNERABILIDADES EL NOMBRE INCLUYE DIRECTORY TRAVERSAL, LAS ESTADÍSTICAS DE IMPACTO DE DISPONIBILIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_sh_namedirectorytraversal_highavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_sh_namedirectorytraversal_lowavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_sh_namedirectorytraversal_mediumavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO\n")
print("\n")
print("      -    EN  "+str(count_vulnibm_sh_nameprivilegeescalation)+" VULNERABILIDADES EL NOMBRE INCLUYE PRIVILEGE ESCALATION, LAS ESTADÍSTICAS DE IMPACTO DE DISPONIBILIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_sh_nameprivilegeescalation_highavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_sh_nameprivilegeescalation_lowavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_sh_nameprivilegeescalation_mediumavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO\n")
print("\n")
print("      -    EN  "+str(count_vulnibm_sh_namecrosssitescripting)+" VULNERABILIDADES EL NOMBRE INCLUYE CROSS SITE SCRIPTING, LAS ESTADÍSTICAS DE IMPACTO DE DISPONIBILIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_sh_namecrosssitescripting_highavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_sh_namecrosssitescripting_lowavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_sh_namecrosssitescripting_mediumavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO\n")
print("\n")
print("      -    EN  "+str(count_vulnibm_sh_namesecuritybypass)+" VULNERABILIDADES EL NOMBRE INCLUYE SECURITY BYPASS, LAS ESTADÍSTICAS DE IMPACTO DE DISPONIBILIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_sh_namesecuritybypass_highavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_sh_namesecuritybypass_lowavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_sh_namesecuritybypass_mediumavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO\n")
print("\n")
print("      -    EN  "+str(count_vulnibm_sh_nameinformationdisclosure)+" VULNERABILIDADES EL NOMBRE INCLUYE INFORMATION DISCLOSURE, LAS ESTADÍSTICAS DE IMPACTO DE DISPONIBILIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_sh_nameinformationdisclosure_highavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_sh_nameinformationdisclosure_lowavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_sh_nameinformationdisclosure_mediumavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO\n")
print("\n")
print("      -    EN  "+str(count_vulnibm_sh_namedenialofservice)+" VULNERABILIDADES EL NOMBRE INCLUYE DENIAL OF SERVICE, LAS ESTADÍSTICAS DE IMPACTO DE DISPONIBILIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_sh_namedenialofservice_highavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_sh_namedenialofservice_lowavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_sh_namedenialofservice_mediumavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO\n")
print("\n")
print("      -    EN  "+str(count_vulnibm_sh_namecodeexecution)+" VULNERABILIDADES EL NOMBRE INCLUYE CODE EXECUTION, LAS ESTADÍSTICAS DE IMPACTO DE DISPONIBILIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_sh_namecodeexecution_highavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_sh_namecodeexecution_lowavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_sh_namecodeexecution_mediumavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO\n")
print("\n")
print("      -    EN  "+str(count_vulnibm_sh_namemaninthemiddle)+" VULNERABILIDADES EL NOMBRE INCLUYE MAN IN THE MIDDLE, LAS ESTADÍSTICAS DE IMPACTO DE DISPONIBILIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_sh_namemaninthemiddle_highavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_sh_namemaninthemiddle_lowavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_sh_namemaninthemiddle_mediumavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO\n")
print("\n")
print("      -    EN  "+str(count_vulnibm_sh_namesqlinjection)+" VULNERABILIDADES EL NOMBRE INCLUYE SQL INJECTION, LAS ESTADÍSTICAS DE IMPACTO DE DISPONIBILIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_sh_namesqlinjection_highavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_sh_namesqlinjection_lowavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_sh_namesqlinjection_mediumavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO\n")
print("\n")
print("      -    EN  "+str(count_vulnibm_sh_namecrosssiterequestforgery)+" VULNERABILIDADES EL NOMBRE INCLUYE CROSS SITE REQUEST FORGERY, LAS ESTADÍSTICAS DE IMPACTO DE DISPONIBILIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_sh_namecrosssiterequestforgery_highavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_sh_namecrosssiterequestforgery_lowavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_sh_namecrosssiterequestforgery_mediumavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO\n")
print("\n")
print("      -    EN  "+str(count_vulnibm_sh_namemoduleexecution)+" VULNERABILIDADES EL NOMBRE INCLUYE MODULE EXECUTION, LAS ESTADÍSTICAS DE IMPACTO DE DISPONIBILIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_sh_namemoduleexecution_highavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_sh_namemoduleexecution_lowavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_sh_namemoduleexecution_mediumavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO\n")
print("\n")
print("      -    EN  "+str(count_vulnibm_sh_namebufferoverflow)+" VULNERABILIDADES EL NOMBRE INCLUYE BUFFER OVERFLOW, LAS ESTADÍSTICAS DE IMPACTO DE DISPONIBILIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_sh_namebufferoverflow_highavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_sh_namebufferoverflow_lowavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_sh_namebufferoverflow_mediumavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO\n")
print("\n")
print("      -    EN  "+str(count_vulnibm_sh_namecommandexecution)+" VULNERABILIDADES EL NOMBRE INCLUYE COMMAND EXECUTION, LAS ESTADÍSTICAS DE IMPACTO DE DISPONIBILIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_sh_namecommandexecution_highavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_sh_namecommandexecution_lowavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_sh_namecommandexecution_mediumavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO\n")
print("\n")
print("      -    EN  "+str(count_vulnibm_sh_namespoofing)+" VULNERABILIDADES EL NOMBRE INCLUYE SPOOFING, LAS ESTADÍSTICAS DE IMPACTO DE DISPONIBILIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_sh_namespoofing_highavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_sh_namespoofing_lowavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_sh_namespoofing_mediumavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO\n")
print("\n")
print("      -    EN  "+str(count_vulnibm_sh_nameclickjacking)+" VULNERABILIDADES EL NOMBRE INCLUYE CLICKJACKING, LAS ESTADÍSTICAS DE IMPACTO DE DISPONIBILIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_sh_nameclickjacking_highavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_sh_nameclickjacking_lowavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_sh_nameclickjacking_mediumavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO\n")
print("\n")
print("      -    EN  "+str(count_vulnibm_sh_namehijacking)+" VULNERABILIDADES EL NOMBRE INCLUYE HIJACKING, LAS ESTADÍSTICAS DE IMPACTO DE DISPONIBILIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_sh_namehijacking_highavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_sh_namehijacking_lowavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_sh_namehijacking_mediumavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO\n")
print("\n")
print("      -    EN  "+str(count_vulnibm_sh_namefileinclude)+" VULNERABILIDADES EL NOMBRE INCLUYE FILEINCLUDE, LAS ESTADÍSTICAS DE IMPACTO DE DISPONIBILIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_sh_namefileinclude_highavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_sh_namefileinclude_lowavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_sh_namefileinclude_mediumavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO\n")
print("\n")
print("      -    EN  "+str(count_vulnibm_sh_namebruteforce)+" VULNERABILIDADES EL NOMBRE INCLUYE BRUTEFORCE, LAS ESTADÍSTICAS DE IMPACTO DE DISPONIBILIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_sh_namebruteforce_highavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_sh_namebruteforce_lowavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_sh_namebruteforce_mediumavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO\n")
print("\n")
print("      -    EN  "+str(count_vulnibm_sh_namefileupload)+" VULNERABILIDADES EL NOMBRE INCLUYE FILE UPLOAD, LAS ESTADÍSTICAS DE IMPACTO DE DISPONIBILIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_sh_namefileupload_highavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_sh_namefileupload_lowavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_sh_namefileupload_mediumavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO\n")
print("\n")
print("      -    EN  "+str(count_vulnibm_sh_nameheaderinjection)+" VULNERABILIDADES EL NOMBRE INCLUYE HEADER INJECTION, LAS ESTADÍSTICAS DE IMPACTO DE DISPONIBILIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_sh_nameheaderinjection_highavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_sh_nameheaderinjection_lowavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_sh_nameheaderinjection_mediumavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO\n")
print("\n")
print("      -    EN  "+str(count_vulnibm_sh_nametampering)+" VULNERABILIDADES EL NOMBRE INCLUYE TAMPERING, LAS ESTADÍSTICAS DE IMPACTO DE DISPONIBILIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_sh_nametampering_highavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_sh_nametampering_lowavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_sh_nametampering_mediumavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO\n")
print("\n")
print("      -    EN  "+str(count_vulnibm_sh_nameanother)+" VULNERABILIDADES EL NOMBRE INCLUYE OTRA CADENA, LAS ESTADÍSTICAS DE IMPACTO DE DISPONIBILIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_sh_nameanother_highavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_sh_nameanother_lowavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_sh_nameanother_mediumavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO\n")
print("\n")





print("**********************************************PORCENTAJE NOMBRE/IMPACTO DE DISPONIBILIDAD VULNERABILIDADES IBM PARTE SMART HOME**********************************************")
print("\n")                            
print("\n")
print(" DE UN TOTAL DE "+str(count_vulnibm_sh_names)+" VULNERABILIDADES :\n") 
print("\n")
print("   - LOS PORCENTAJES DE VALORES DE NOMBRE SON LOS SIGUIENTES:  \n")
if(count_vulnibm_sh_namepathtraversal>0):
    print("      -    EN EL  "+str(float(((count_vulnibm_sh_namepathtraversal*100)/count_vulnibm_sh_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE PATH TRAVERSAL, LOS PORCENTAJES DE IMPACTO DE DISPONIBILIDAD SON LOS SIGUIENTES :  \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namepathtraversal_highavaimpact*100)/count_vulnibm_sh_namepathtraversal)))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namepathtraversal_lowavaimpact*100)/count_vulnibm_sh_namepathtraversal)))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namepathtraversal_mediumavaimpact*100)/count_vulnibm_sh_namepathtraversal)))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO\n")
    print("\n")
if(count_vulnibm_sh_namedirectorytraversal>0):
    print("      -    EN EL  "+str(float(((count_vulnibm_sh_namedirectorytraversal*100)/count_vulnibm_sh_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE DIRECTORY TRAVERSAL, LOS PORCENTAJES DE IMPACTO DE DISPONIBILIDAD SON LOS SIGUIENTES :  \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namedirectorytraversal_highavaimpact*100)/count_vulnibm_sh_namedirectorytraversal)))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namedirectorytraversal_lowavaimpact*100)/count_vulnibm_sh_namedirectorytraversal)))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namedirectorytraversal_mediumavaimpact*100)/count_vulnibm_sh_namedirectorytraversal)))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO\n")
    print("\n")
if(count_vulnibm_sh_nameprivilegeescalation>0):
    print("      -    EN EL  "+str(float(((count_vulnibm_sh_nameprivilegeescalation*100)/count_vulnibm_sh_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE PRIVILEGE ESCALATION, LOS PORCENTAJES DE IMPACTO DE DISPONIBILIDAD SON LOS SIGUIENTES :  \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_nameprivilegeescalation_highavaimpact*100)/count_vulnibm_sh_nameprivilegeescalation)))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_nameprivilegeescalation_lowavaimpact*100)/count_vulnibm_sh_nameprivilegeescalation)))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_nameprivilegeescalation_mediumavaimpact*100)/count_vulnibm_sh_nameprivilegeescalation)))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO\n")
    print("\n")
if(count_vulnibm_sh_namecrosssitescripting>0):
    print("      -    EN EL  "+str(float(((count_vulnibm_sh_namecrosssitescripting*100)/count_vulnibm_sh_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE CROSS SITE SCRIPTING, LOS PORCENTAJES DE IMPACTO DE DISPONIBILIDAD SON LOS SIGUIENTES :  \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namecrosssitescripting_highavaimpact*100)/count_vulnibm_sh_namecrosssitescripting)))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namecrosssitescripting_lowavaimpact*100)/count_vulnibm_sh_namecrosssitescripting)))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namecrosssitescripting_mediumavaimpact*100)/count_vulnibm_sh_namecrosssitescripting)))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO\n")
    print("\n")
if(count_vulnibm_sh_namesecuritybypass>0):
    print("      -    EN EL  "+str(float(((count_vulnibm_sh_namesecuritybypass*100)/count_vulnibm_sh_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE SECURITY BYPASS, LOS PORCENTAJES DE IMPACTO DE DISPONIBILIDAD SON LOS SIGUIENTES :  \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namesecuritybypass_highavaimpact*100)/count_vulnibm_sh_namesecuritybypass)))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namesecuritybypass_lowavaimpact*100)/count_vulnibm_sh_namesecuritybypass)))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namesecuritybypass_mediumavaimpact*100)/count_vulnibm_sh_namesecuritybypass)))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO\n")
    print("\n")
if(count_vulnibm_sh_nameinformationdisclosure>0):
    print("      -    EN EL  "+str(float(((count_vulnibm_sh_nameinformationdisclosure*100)/count_vulnibm_sh_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE INFORMATION DISCLOSURE, LOS PORCENTAJES DE IMPACTO DE DISPONIBILIDAD SON LOS SIGUIENTES :  \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_nameinformationdisclosure_highavaimpact*100)/count_vulnibm_sh_nameinformationdisclosure)))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_nameinformationdisclosure_lowavaimpact*100)/count_vulnibm_sh_nameinformationdisclosure)))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_nameinformationdisclosure_mediumavaimpact*100)/count_vulnibm_sh_nameinformationdisclosure)))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO\n")
    print("\n")
if(count_vulnibm_sh_namedenialofservice>0):
    print("      -    EN EL  "+str(float(((count_vulnibm_sh_namedenialofservice*100)/count_vulnibm_sh_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE DENIAL OF SERVICE, LOS PORCENTAJES DE IMPACTO DE DISPONIBILIDAD SON LOS SIGUIENTES :  \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namedenialofservice_highavaimpact*100)/count_vulnibm_sh_namedenialofservice)))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namedenialofservice_lowavaimpact*100)/count_vulnibm_sh_namedenialofservice)))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namedenialofservice_mediumavaimpact*100)/count_vulnibm_sh_namedenialofservice)))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO\n")
    print("\n")
if(count_vulnibm_sh_namecodeexecution>0):
    print("      -    EN EL  "+str(float(((count_vulnibm_sh_namecodeexecution*100)/count_vulnibm_sh_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE CODE EXECUTION, LOS PORCENTAJES DE IMPACTO DE DISPONIBILIDAD SON LOS SIGUIENTES :  \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namecodeexecution_highavaimpact*100)/count_vulnibm_sh_namecodeexecution)))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namecodeexecution_lowavaimpact*100)/count_vulnibm_sh_namecodeexecution)))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namecodeexecution_mediumavaimpact*100)/count_vulnibm_sh_namecodeexecution)))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO\n")
    print("\n")
if(count_vulnibm_sh_namemaninthemiddle>0):
    print("      -    EN EL  "+str(float(((count_vulnibm_sh_namemaninthemiddle*100)/count_vulnibm_sh_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE MAN IN THE MIDDLE, LOS PORCENTAJES DE IMPACTO DE DISPONIBILIDAD SON LOS SIGUIENTES :  \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namemaninthemiddle_highavaimpact*100)/count_vulnibm_sh_namemaninthemiddle)))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namemaninthemiddle_lowavaimpact*100)/count_vulnibm_sh_namemaninthemiddle)))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namemaninthemiddle_mediumavaimpact*100)/count_vulnibm_sh_namemaninthemiddle)))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO\n")
    print("\n")
if(count_vulnibm_sh_namesqlinjection>0):
    print("      -    EN EL  "+str(float(((count_vulnibm_sh_namesqlinjection*100)/count_vulnibm_sh_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE SQL INJECTION, LOS PORCENTAJES DE IMPACTO DE DISPONIBILIDAD SON LOS SIGUIENTES :  \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namesqlinjection_highavaimpact*100)/count_vulnibm_sh_namesqlinjection)))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namesqlinjection_lowavaimpact*100)/count_vulnibm_sh_namesqlinjection)))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namesqlinjection_mediumavaimpact*100)/count_vulnibm_sh_namesqlinjection)))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO\n")
    print("\n")
if(count_vulnibm_sh_namecrosssiterequestforgery>0):
    print("      -    EN EL  "+str(float(((count_vulnibm_sh_namecrosssiterequestforgery*100)/count_vulnibm_sh_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE CROSS SITE REQUEST FORGERY, LOS PORCENTAJES DE IMPACTO DE DISPONIBILIDAD SON LOS SIGUIENTES :  \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namecrosssiterequestforgery_highavaimpact*100)/count_vulnibm_sh_namecrosssiterequestforgery)))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namecrosssiterequestforgery_lowavaimpact*100)/count_vulnibm_sh_namecrosssiterequestforgery)))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namecrosssiterequestforgery_mediumavaimpact*100)/count_vulnibm_sh_namecrosssiterequestforgery)))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO\n")
    print("\n")
if(count_vulnibm_sh_namemoduleexecution>0):
    print("      -    EN EL  "+str(float(((count_vulnibm_sh_namemoduleexecution*100)/count_vulnibm_sh_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE MODULE EXECUTION, LOS PORCENTAJES DE IMPACTO DE DISPONIBILIDAD SON LOS SIGUIENTES :  \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namemoduleexecution_highavaimpact*100)/count_vulnibm_sh_namemoduleexecution)))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namemoduleexecution_lowavaimpact*100)/count_vulnibm_sh_namemoduleexecution)))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namemoduleexecution_mediumavaimpact*100)/count_vulnibm_sh_namemoduleexecution)))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO\n")
    print("\n")
if(count_vulnibm_sh_namebufferoverflow>0):
    print("      -    EN EL  "+str(float(((count_vulnibm_sh_namebufferoverflow*100)/count_vulnibm_sh_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE BUFFER OVERFLOW, LOS PORCENTAJES DE IMPACTO DE DISPONIBILIDAD SON LOS SIGUIENTES :  \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namebufferoverflow_highavaimpact*100)/count_vulnibm_sh_namebufferoverflow)))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namebufferoverflow_lowavaimpact*100)/count_vulnibm_sh_namebufferoverflow)))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namebufferoverflow_mediumavaimpact*100)/count_vulnibm_sh_namebufferoverflow)))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO\n")
    print("\n")
if(count_vulnibm_sh_namecommandexecution>0):
    print("      -    EN EL  "+str(float(((count_vulnibm_sh_namecommandexecution*100)/count_vulnibm_sh_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE COMMAND EXECUTION, LOS PORCENTAJES DE IMPACTO DE DISPONIBILIDAD SON LOS SIGUIENTES :  \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namecommandexecution_highavaimpact*100)/count_vulnibm_sh_namecommandexecution)))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namecommandexecution_lowavaimpact*100)/count_vulnibm_sh_namecommandexecution)))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namecommandexecution_mediumavaimpact*100)/count_vulnibm_sh_namecommandexecution)))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO\n")
    print("\n")
if(count_vulnibm_sh_namespoofing>0):
    print("      -    EN EL  "+str(float(((count_vulnibm_sh_namespoofing*100)/count_vulnibm_sh_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE SPOOFING, LOS PORCENTAJES DE IMPACTO DE DISPONIBILIDAD SON LOS SIGUIENTES :  \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namespoofing_highavaimpact*100)/count_vulnibm_sh_namespoofing)))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namespoofing_lowavaimpact*100)/count_vulnibm_sh_namespoofing)))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namespoofing_mediumavaimpact*100)/count_vulnibm_sh_namespoofing)))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO\n")
    print("\n")
if(count_vulnibm_sh_nameclickjacking>0):
    print("      -    EN EL  "+str(float(((count_vulnibm_sh_nameclickjacking*100)/count_vulnibm_sh_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE CLICKJACKING, LOS PORCENTAJES DE IMPACTO DE DISPONIBILIDAD SON LOS SIGUIENTES :  \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_nameclickjacking_highavaimpact*100)/count_vulnibm_sh_nameclickjacking)))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_nameclickjacking_lowavaimpact*100)/count_vulnibm_sh_nameclickjacking)))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_nameclickjacking_mediumavaimpact*100)/count_vulnibm_sh_nameclickjacking)))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO\n")
    print("\n")
if(count_vulnibm_sh_namehijacking>0):
    print("      -    EN EL  "+str(float(((count_vulnibm_sh_namehijacking*100)/count_vulnibm_sh_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE HIJACKING, LOS PORCENTAJES DE IMPACTO DE DISPONIBILIDAD SON LOS SIGUIENTES :  \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namehijacking_highavaimpact*100)/count_vulnibm_sh_namehijacking)))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namehijacking_lowavaimpact*100)/count_vulnibm_sh_namehijacking)))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namehijacking_mediumavaimpact*100)/count_vulnibm_sh_namehijacking)))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO\n")
    print("\n")
if(count_vulnibm_sh_namefileinclude>0):
    print("      -    EN EL  "+str(float(((count_vulnibm_sh_namefileinclude*100)/count_vulnibm_sh_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE FILEINCLUDE, LOS PORCENTAJES DE IMPACTO DE DISPONIBILIDAD SON LOS SIGUIENTES :  \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namefileinclude_highavaimpact*100)/count_vulnibm_sh_namefileinclude)))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namefileinclude_lowavaimpact*100)/count_vulnibm_sh_namefileinclude)))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namefileinclude_mediumavaimpact*100)/count_vulnibm_sh_namefileinclude)))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO\n")
    print("\n")
if(count_vulnibm_sh_namebruteforce>0):
    print("      -    EN EL  "+str(float(((count_vulnibm_sh_namebruteforce*100)/count_vulnibm_sh_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE BRUTEFORCE, LOS PORCENTAJES DE IMPACTO DE DISPONIBILIDAD SON LOS SIGUIENTES :  \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namebruteforce_highavaimpact*100)/count_vulnibm_sh_namebruteforce)))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namebruteforce_lowavaimpact*100)/count_vulnibm_sh_namebruteforce)))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namebruteforce_mediumavaimpact*100)/count_vulnibm_sh_namebruteforce)))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO\n")
    print("\n")
if(count_vulnibm_sh_namefileupload>0):
    print("      -    EN EL  "+str(float(((count_vulnibm_sh_namefileupload*100)/count_vulnibm_sh_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE FILE UPLOAD, LOS PORCENTAJES DE IMPACTO DE DISPONIBILIDAD SON LOS SIGUIENTES :  \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namefileupload_highavaimpact*100)/count_vulnibm_sh_namefileupload)))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namefileupload_lowavaimpact*100)/count_vulnibm_sh_namefileupload)))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namefileupload_mediumavaimpact*100)/count_vulnibm_sh_namefileupload)))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO\n")
    print("\n")
if(count_vulnibm_sh_nameheaderinjection>0):
    print("      -    EN EL  "+str(float(((count_vulnibm_sh_nameheaderinjection*100)/count_vulnibm_sh_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE HEADER INJECTION, LOS PORCENTAJES DE IMPACTO DE DISPONIBILIDAD SON LOS SIGUIENTES :  \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_nameheaderinjection_highavaimpact*100)/count_vulnibm_sh_nameheaderinjection)))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_nameheaderinjection_lowavaimpact*100)/count_vulnibm_sh_nameheaderinjection)))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_nameheaderinjection_mediumavaimpact*100)/count_vulnibm_sh_nameheaderinjection)))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO\n")
    print("\n")
if(count_vulnibm_sh_nametampering>0):
    print("      -    EN EL  "+str(float(((count_vulnibm_sh_nametampering*100)/count_vulnibm_sh_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE TAMPERING, LOS PORCENTAJES DE IMPACTO DE DISPONIBILIDAD SON LOS SIGUIENTES :  \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_nametampering_highavaimpact*100)/count_vulnibm_sh_nametampering)))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_nametampering_lowavaimpact*100)/count_vulnibm_sh_nametampering)))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_nametampering_mediumavaimpact*100)/count_vulnibm_sh_nametampering)))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO\n")
    print("\n")
    print("      -    EN EL  "+str(float(((count_vulnibm_sh_nameanother*100)/count_vulnibm_sh_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE OTRA CADENA, LOS PORCENTAJES DE IMPACTO DE DISPONIBILIDAD SON LOS SIGUIENTES :  \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_nameanother_highavaimpact*100)/count_vulnibm_sh_nameanother)))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_nameanother_lowavaimpact*100)/count_vulnibm_sh_nameanother)))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_nameanother_mediumavaimpact*100)/count_vulnibm_sh_nameanother)))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO\n")
    print("\n")



print("**********************************************ESTADÍSTICAS NOMBRE/IMPACTO DE DISPONIBILIDAD VULNERABILIDADES IBM PARTE IOT Y SMART HOME**********************************************")
print("\n")                            
print("\n")
print(" DE UN TOTAL DE "+str(count_vulnibm_iot_names+count_vulnibm_sh_names)+" VULNERABILIDADES:\n") 
print("\n")
print("   - LAS ESTADISTICAS DE VALORES DE NOMBRE SON LAS SIGUIENTES:  \n")
print("      -    EN  "+str(count_vulnibm_iot_namepathtraversal+count_vulnibm_sh_namepathtraversal)+" VULNERABILIDADES EL NOMBRE INCLUYE PATH TRAVERSAL, LOS PORCENTAJES DE IMPACTO DE DISPONIBILIDAD SON LOS SIGUIENTES:  \n")
print("            -    EN  "+str(count_vulnibm_iot_namepathtraversal_highavaimpact+count_vulnibm_sh_namepathtraversal_highavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_iot_namepathtraversal_lowavaimpact+count_vulnibm_sh_namepathtraversal_lowavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_iot_namepathtraversal_mediumavaimpact+count_vulnibm_sh_namepathtraversal_mediumavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_namedirectorytraversal+count_vulnibm_sh_namedirectorytraversal)+" VULNERABILIDADES EL NOMBRE INCLUYE directorytraversal, LOS PORCENTAJES DE IMPACTO DE DISPONIBILIDAD SON LOS SIGUIENTES:  \n")
print("            -    EN  "+str(count_vulnibm_iot_namedirectorytraversal_highavaimpact+count_vulnibm_sh_namedirectorytraversal_highavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_iot_namedirectorytraversal_lowavaimpact+count_vulnibm_sh_namedirectorytraversal_lowavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_iot_namedirectorytraversal_mediumavaimpact+count_vulnibm_sh_namedirectorytraversal_mediumavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_nameprivilegeescalation+count_vulnibm_sh_nameprivilegeescalation)+" VULNERABILIDADES EL NOMBRE INCLUYE privilegeescalation, LOS PORCENTAJES DE IMPACTO DE DISPONIBILIDAD SON LOS SIGUIENTES:  \n")
print("            -    EN  "+str(count_vulnibm_iot_nameprivilegeescalation_highavaimpact+count_vulnibm_sh_nameprivilegeescalation_highavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_iot_nameprivilegeescalation_lowavaimpact+count_vulnibm_sh_nameprivilegeescalation_lowavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_iot_nameprivilegeescalation_mediumavaimpact+count_vulnibm_sh_nameprivilegeescalation_mediumavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_namecrosssitescripting+count_vulnibm_sh_namecrosssitescripting)+" VULNERABILIDADES EL NOMBRE INCLUYE crosssitescripting, LOS PORCENTAJES DE IMPACTO DE DISPONIBILIDAD SON LOS SIGUIENTES:  \n")
print("            -    EN  "+str(count_vulnibm_iot_namecrosssitescripting_highavaimpact+count_vulnibm_sh_namecrosssitescripting_highavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_iot_namecrosssitescripting_lowavaimpact+count_vulnibm_sh_namecrosssitescripting_lowavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_iot_namecrosssitescripting_mediumavaimpact+count_vulnibm_sh_namecrosssitescripting_mediumavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_namesecuritybypass+count_vulnibm_sh_namesecuritybypass)+" VULNERABILIDADES EL NOMBRE INCLUYE securitybypass, LOS PORCENTAJES DE IMPACTO DE DISPONIBILIDAD SON LOS SIGUIENTES:  \n")
print("            -    EN  "+str(count_vulnibm_iot_namesecuritybypass_highavaimpact+count_vulnibm_sh_namesecuritybypass_highavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_iot_namesecuritybypass_lowavaimpact+count_vulnibm_sh_namesecuritybypass_lowavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_iot_namesecuritybypass_mediumavaimpact+count_vulnibm_sh_namesecuritybypass_mediumavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_nameinformationdisclosure+count_vulnibm_sh_nameinformationdisclosure)+" VULNERABILIDADES EL NOMBRE INCLUYE informationdisclosure, LOS PORCENTAJES DE IMPACTO DE DISPONIBILIDAD SON LOS SIGUIENTES:  \n")
print("            -    EN  "+str(count_vulnibm_iot_nameinformationdisclosure_highavaimpact+count_vulnibm_sh_nameinformationdisclosure_highavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_iot_nameinformationdisclosure_lowavaimpact+count_vulnibm_sh_nameinformationdisclosure_lowavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_iot_nameinformationdisclosure_mediumavaimpact+count_vulnibm_sh_nameinformationdisclosure_mediumavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_namedenialofservice+count_vulnibm_sh_namedenialofservice)+" VULNERABILIDADES EL NOMBRE INCLUYE denialofservice, LOS PORCENTAJES DE IMPACTO DE DISPONIBILIDAD SON LOS SIGUIENTES:  \n")
print("            -    EN  "+str(count_vulnibm_iot_namedenialofservice_highavaimpact+count_vulnibm_sh_namedenialofservice_highavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_iot_namedenialofservice_lowavaimpact+count_vulnibm_sh_namedenialofservice_lowavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_iot_namedenialofservice_mediumavaimpact+count_vulnibm_sh_namedenialofservice_mediumavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_namecodeexecution+count_vulnibm_sh_namecodeexecution)+" VULNERABILIDADES EL NOMBRE INCLUYE codeexecution, LOS PORCENTAJES DE IMPACTO DE DISPONIBILIDAD SON LOS SIGUIENTES:  \n")
print("            -    EN  "+str(count_vulnibm_iot_namecodeexecution_highavaimpact+count_vulnibm_sh_namecodeexecution_highavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_iot_namecodeexecution_lowavaimpact+count_vulnibm_sh_namecodeexecution_lowavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_iot_namecodeexecution_mediumavaimpact+count_vulnibm_sh_namecodeexecution_mediumavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_namemaninthemiddle+count_vulnibm_sh_namemaninthemiddle)+" VULNERABILIDADES EL NOMBRE INCLUYE maninthemiddle, LOS PORCENTAJES DE IMPACTO DE DISPONIBILIDAD SON LOS SIGUIENTES:  \n")
print("            -    EN  "+str(count_vulnibm_iot_namemaninthemiddle_highavaimpact+count_vulnibm_sh_namemaninthemiddle_highavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_iot_namemaninthemiddle_lowavaimpact+count_vulnibm_sh_namemaninthemiddle_lowavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_iot_namemaninthemiddle_mediumavaimpact+count_vulnibm_sh_namemaninthemiddle_mediumavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_namesqlinjection+count_vulnibm_sh_namesqlinjection)+" VULNERABILIDADES EL NOMBRE INCLUYE sqlinjection, LOS PORCENTAJES DE IMPACTO DE DISPONIBILIDAD SON LOS SIGUIENTES:  \n")
print("            -    EN  "+str(count_vulnibm_iot_namesqlinjection_highavaimpact+count_vulnibm_sh_namesqlinjection_highavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_iot_namesqlinjection_lowavaimpact+count_vulnibm_sh_namesqlinjection_lowavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_iot_namesqlinjection_mediumavaimpact+count_vulnibm_sh_namesqlinjection_mediumavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_namecrosssiterequestforgery+count_vulnibm_sh_namecrosssiterequestforgery)+" VULNERABILIDADES EL NOMBRE INCLUYE crosssiterequestforgery, LOS PORCENTAJES DE IMPACTO DE DISPONIBILIDAD SON LOS SIGUIENTES:  \n")
print("            -    EN  "+str(count_vulnibm_iot_namecrosssiterequestforgery_highavaimpact+count_vulnibm_sh_namecrosssiterequestforgery_highavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_iot_namecrosssiterequestforgery_lowavaimpact+count_vulnibm_sh_namecrosssiterequestforgery_lowavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_iot_namecrosssiterequestforgery_mediumavaimpact+count_vulnibm_sh_namecrosssiterequestforgery_mediumavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_namemoduleexecution+count_vulnibm_sh_namemoduleexecution)+" VULNERABILIDADES EL NOMBRE INCLUYE moduleexecution, LOS PORCENTAJES DE IMPACTO DE DISPONIBILIDAD SON LOS SIGUIENTES:  \n")
print("            -    EN  "+str(count_vulnibm_iot_namemoduleexecution_highavaimpact+count_vulnibm_sh_namemoduleexecution_highavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_iot_namemoduleexecution_lowavaimpact+count_vulnibm_sh_namemoduleexecution_lowavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_iot_namemoduleexecution_mediumavaimpact+count_vulnibm_sh_namemoduleexecution_mediumavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_namebufferoverflow+count_vulnibm_sh_namebufferoverflow)+" VULNERABILIDADES EL NOMBRE INCLUYE bufferoverflow, LOS PORCENTAJES DE IMPACTO DE DISPONIBILIDAD SON LOS SIGUIENTES:  \n")
print("            -    EN  "+str(count_vulnibm_iot_namebufferoverflow_highavaimpact+count_vulnibm_sh_namebufferoverflow_highavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_iot_namebufferoverflow_lowavaimpact+count_vulnibm_sh_namebufferoverflow_lowavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_iot_namebufferoverflow_mediumavaimpact+count_vulnibm_sh_namebufferoverflow_mediumavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_namecommandexecution+count_vulnibm_sh_namecommandexecution)+" VULNERABILIDADES EL NOMBRE INCLUYE commandexecution, LOS PORCENTAJES DE IMPACTO DE DISPONIBILIDAD SON LOS SIGUIENTES:  \n")
print("            -    EN  "+str(count_vulnibm_iot_namecommandexecution_highavaimpact+count_vulnibm_sh_namecommandexecution_highavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_iot_namecommandexecution_lowavaimpact+count_vulnibm_sh_namecommandexecution_lowavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_iot_namecommandexecution_mediumavaimpact+count_vulnibm_sh_namecommandexecution_mediumavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_namespoofing+count_vulnibm_sh_namespoofing)+" VULNERABILIDADES EL NOMBRE INCLUYE spoofing, LOS PORCENTAJES DE IMPACTO DE DISPONIBILIDAD SON LOS SIGUIENTES:  \n")
print("            -    EN  "+str(count_vulnibm_iot_namespoofing_highavaimpact+count_vulnibm_sh_namespoofing_highavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_iot_namespoofing_lowavaimpact+count_vulnibm_sh_namespoofing_lowavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_iot_namespoofing_mediumavaimpact+count_vulnibm_sh_namespoofing_mediumavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_nameclickjacking+count_vulnibm_sh_nameclickjacking)+" VULNERABILIDADES EL NOMBRE INCLUYE clickjacking, LOS PORCENTAJES DE IMPACTO DE DISPONIBILIDAD SON LOS SIGUIENTES:  \n")
print("            -    EN  "+str(count_vulnibm_iot_nameclickjacking_highavaimpact+count_vulnibm_sh_nameclickjacking_highavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_iot_nameclickjacking_lowavaimpact+count_vulnibm_sh_nameclickjacking_lowavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_iot_nameclickjacking_mediumavaimpact+count_vulnibm_sh_nameclickjacking_mediumavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_namehijacking+count_vulnibm_sh_namehijacking)+" VULNERABILIDADES EL NOMBRE INCLUYE hijacking, LOS PORCENTAJES DE IMPACTO DE DISPONIBILIDAD SON LOS SIGUIENTES:  \n")
print("            -    EN  "+str(count_vulnibm_iot_namehijacking_highavaimpact+count_vulnibm_sh_namehijacking_highavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_iot_namehijacking_lowavaimpact+count_vulnibm_sh_namehijacking_lowavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_iot_namehijacking_mediumavaimpact+count_vulnibm_sh_namehijacking_mediumavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_namefileinclude+count_vulnibm_sh_namefileinclude)+" VULNERABILIDADES EL NOMBRE INCLUYE fileinclude, LOS PORCENTAJES DE IMPACTO DE DISPONIBILIDAD SON LOS SIGUIENTES:  \n")
print("            -    EN  "+str(count_vulnibm_iot_namefileinclude_highavaimpact+count_vulnibm_sh_namefileinclude_highavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_iot_namefileinclude_lowavaimpact+count_vulnibm_sh_namefileinclude_lowavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_iot_namefileinclude_mediumavaimpact+count_vulnibm_sh_namefileinclude_mediumavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_namebruteforce+count_vulnibm_sh_namebruteforce)+" VULNERABILIDADES EL NOMBRE INCLUYE bruteforce, LOS PORCENTAJES DE IMPACTO DE DISPONIBILIDAD SON LOS SIGUIENTES:  \n")
print("            -    EN  "+str(count_vulnibm_iot_namebruteforce_highavaimpact+count_vulnibm_sh_namebruteforce_highavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_iot_namebruteforce_lowavaimpact+count_vulnibm_sh_namebruteforce_lowavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_iot_namebruteforce_mediumavaimpact+count_vulnibm_sh_namebruteforce_mediumavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_namefileupload+count_vulnibm_sh_namefileupload)+" VULNERABILIDADES EL NOMBRE INCLUYE fileupload, LOS PORCENTAJES DE IMPACTO DE DISPONIBILIDAD SON LOS SIGUIENTES:  \n")
print("            -    EN  "+str(count_vulnibm_iot_namefileupload_highavaimpact+count_vulnibm_sh_namefileupload_highavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_iot_namefileupload_lowavaimpact+count_vulnibm_sh_namefileupload_lowavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_iot_namefileupload_mediumavaimpact+count_vulnibm_sh_namefileupload_mediumavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_nameheaderinjection+count_vulnibm_sh_nameheaderinjection)+" VULNERABILIDADES EL NOMBRE INCLUYE headerinjection, LOS PORCENTAJES DE IMPACTO DE DISPONIBILIDAD SON LOS SIGUIENTES:  \n")
print("            -    EN  "+str(count_vulnibm_iot_nameheaderinjection_highavaimpact+count_vulnibm_sh_nameheaderinjection_highavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_iot_nameheaderinjection_lowavaimpact+count_vulnibm_sh_nameheaderinjection_lowavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_iot_nameheaderinjection_mediumavaimpact+count_vulnibm_sh_nameheaderinjection_mediumavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_nametampering+count_vulnibm_sh_nametampering)+" VULNERABILIDADES EL NOMBRE INCLUYE tampering, LOS PORCENTAJES DE IMPACTO DE DISPONIBILIDAD SON LOS SIGUIENTES:  \n")
print("            -    EN  "+str(count_vulnibm_iot_nametampering_highavaimpact+count_vulnibm_sh_nametampering_highavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_iot_nametampering_lowavaimpact+count_vulnibm_sh_nametampering_lowavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_iot_nametampering_mediumavaimpact+count_vulnibm_sh_nametampering_mediumavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_nameanother+count_vulnibm_sh_nameanother)+" VULNERABILIDADES EL NOMBRE INCLUYE OTRO NOMBRE DISTINTO, LOS PORCENTAJES DE IMPACTO DE DISPONIBILIDAD SON LOS SIGUIENTES:  \n")
print("            -    EN  "+str(count_vulnibm_iot_nameanother_highavaimpact+count_vulnibm_sh_nameanother_highavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_iot_nameanother_lowavaimpact+count_vulnibm_sh_nameanother_lowavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_iot_nameanother_mediumavaimpact+count_vulnibm_sh_nameanother_mediumavaimpact)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO \n")
print("\n")









print("**********************************************PORCENTAJES NOMBRE/IMPACTO DE DISPONIBILIDAD VULNERABILIDADES IBM PARTE IOT Y SMART HOME **********************************************")
print("\n")                            
print("\n")
print(" DE UN TOTAL DE "+str(count_vulnibm_iot_names+count_vulnibm_sh_names)+" VULNERABILIDADES:\n") 
print("\n")
print("   - LOS PORCENTAJES DE VALORES DE NOMBRE SON LOS SIGUIENTES:  \n")
print("      -    EN EL "+str(float((((count_vulnibm_iot_namepathtraversal+count_vulnibm_sh_namepathtraversal)*100)/(count_vulnibm_iot_names+count_vulnibm_sh_names))))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE PATHTRAVERSAL, LOS PORCENTAJES DE IMPACTO DE DISPONIBILIDAD SON LOS SIGUIENTES:  \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namepathtraversal_highavaimpact+count_vulnibm_sh_namepathtraversal_highavaimpact)*100)/(count_vulnibm_iot_namepathtraversal+count_vulnibm_sh_namepathtraversal))))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namepathtraversal_lowavaimpact+count_vulnibm_sh_namepathtraversal_lowavaimpact)*100)/(count_vulnibm_iot_namepathtraversal+count_vulnibm_sh_namepathtraversal))))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namepathtraversal_mediumavaimpact+count_vulnibm_sh_namepathtraversal_mediumavaimpact)*100)/(count_vulnibm_iot_namepathtraversal+count_vulnibm_sh_namepathtraversal))))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO \n")
print("\n")
print("      -    EN EL "+str(float((((count_vulnibm_iot_namedirectorytraversal+count_vulnibm_sh_namedirectorytraversal)*100)/(count_vulnibm_iot_names+count_vulnibm_sh_names))))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE DIRECTORY TRAVERSAL, LOS PORCENTAJES DE IMPACTO DE DISPONIBILIDAD SON LOS SIGUIENTES:  \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namedirectorytraversal_highavaimpact+count_vulnibm_sh_namedirectorytraversal_highavaimpact)*100)/(count_vulnibm_iot_namedirectorytraversal+count_vulnibm_sh_namedirectorytraversal))))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namedirectorytraversal_lowavaimpact+count_vulnibm_sh_namedirectorytraversal_lowavaimpact)*100)/(count_vulnibm_iot_namedirectorytraversal+count_vulnibm_sh_namedirectorytraversal))))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namedirectorytraversal_mediumavaimpact+count_vulnibm_sh_namedirectorytraversal_mediumavaimpact)*100)/(count_vulnibm_iot_namedirectorytraversal+count_vulnibm_sh_namedirectorytraversal))))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO \n")
print("\n")
print("      -    EN EL "+str(float((((count_vulnibm_iot_nameprivilegeescalation+count_vulnibm_sh_nameprivilegeescalation)*100)/(count_vulnibm_iot_names+count_vulnibm_sh_names))))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE PRIVILEGE ESCALATION, LOS PORCENTAJES DE IMPACTO DE DISPONIBILIDAD SON LOS SIGUIENTES:  \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_nameprivilegeescalation_highavaimpact+count_vulnibm_sh_nameprivilegeescalation_highavaimpact)*100)/(count_vulnibm_iot_nameprivilegeescalation+count_vulnibm_sh_nameprivilegeescalation))))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_nameprivilegeescalation_lowavaimpact+count_vulnibm_sh_nameprivilegeescalation_lowavaimpact)*100)/(count_vulnibm_iot_nameprivilegeescalation+count_vulnibm_sh_nameprivilegeescalation))))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_nameprivilegeescalation_mediumavaimpact+count_vulnibm_sh_nameprivilegeescalation_mediumavaimpact)*100)/(count_vulnibm_iot_nameprivilegeescalation+count_vulnibm_sh_nameprivilegeescalation))))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO \n")
print("\n")
print("      -    EN EL "+str(float((((count_vulnibm_iot_namecrosssitescripting+count_vulnibm_sh_namecrosssitescripting)*100)/(count_vulnibm_iot_names+count_vulnibm_sh_names))))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE CROSS SITE SCRIPTING, LOS PORCENTAJES DE IMPACTO DE DISPONIBILIDAD SON LOS SIGUIENTES:  \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namecrosssitescripting_highavaimpact+count_vulnibm_sh_namecrosssitescripting_highavaimpact)*100)/(count_vulnibm_iot_namecrosssitescripting+count_vulnibm_sh_namecrosssitescripting))))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namecrosssitescripting_lowavaimpact+count_vulnibm_sh_namecrosssitescripting_lowavaimpact)*100)/(count_vulnibm_iot_namecrosssitescripting+count_vulnibm_sh_namecrosssitescripting))))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namecrosssitescripting_mediumavaimpact+count_vulnibm_sh_namecrosssitescripting_mediumavaimpact)*100)/(count_vulnibm_iot_namecrosssitescripting+count_vulnibm_sh_namecrosssitescripting))))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO \n")
print("\n")
print("      -    EN EL "+str(float((((count_vulnibm_iot_namesecuritybypass+count_vulnibm_sh_namesecuritybypass)*100)/(count_vulnibm_iot_names+count_vulnibm_sh_names))))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE SECURITY BYPASS, LOS PORCENTAJES DE IMPACTO DE DISPONIBILIDAD SON LOS SIGUIENTES:  \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namesecuritybypass_highavaimpact+count_vulnibm_sh_namesecuritybypass_highavaimpact)*100)/(count_vulnibm_iot_namesecuritybypass+count_vulnibm_sh_namesecuritybypass))))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namesecuritybypass_lowavaimpact+count_vulnibm_sh_namesecuritybypass_lowavaimpact)*100)/(count_vulnibm_iot_namesecuritybypass+count_vulnibm_sh_namesecuritybypass))))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namesecuritybypass_mediumavaimpact+count_vulnibm_sh_namesecuritybypass_mediumavaimpact)*100)/(count_vulnibm_iot_namesecuritybypass+count_vulnibm_sh_namesecuritybypass))))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO \n")
print("\n")
print("      -    EN EL "+str(float((((count_vulnibm_iot_nameinformationdisclosure+count_vulnibm_sh_nameinformationdisclosure)*100)/(count_vulnibm_iot_names+count_vulnibm_sh_names))))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE INFORMATION DISCLOSURE, LOS PORCENTAJES DE IMPACTO DE DISPONIBILIDAD SON LOS SIGUIENTES:  \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_nameinformationdisclosure_highavaimpact+count_vulnibm_sh_nameinformationdisclosure_highavaimpact)*100)/(count_vulnibm_iot_nameinformationdisclosure+count_vulnibm_sh_nameinformationdisclosure))))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_nameinformationdisclosure_lowavaimpact+count_vulnibm_sh_nameinformationdisclosure_lowavaimpact)*100)/(count_vulnibm_iot_nameinformationdisclosure+count_vulnibm_sh_nameinformationdisclosure))))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_nameinformationdisclosure_mediumavaimpact+count_vulnibm_sh_nameinformationdisclosure_mediumavaimpact)*100)/(count_vulnibm_iot_nameinformationdisclosure+count_vulnibm_sh_nameinformationdisclosure))))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO \n")
print("\n")
print("      -    EN EL "+str(float((((count_vulnibm_iot_namedenialofservice+count_vulnibm_sh_namedenialofservice)*100)/(count_vulnibm_iot_names+count_vulnibm_sh_names))))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE DENIAL OF SERVICE, LOS PORCENTAJES DE IMPACTO DE DISPONIBILIDAD SON LOS SIGUIENTES:  \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namedenialofservice_highavaimpact+count_vulnibm_sh_namedenialofservice_highavaimpact)*100)/(count_vulnibm_iot_namedenialofservice+count_vulnibm_sh_namedenialofservice))))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namedenialofservice_lowavaimpact+count_vulnibm_sh_namedenialofservice_lowavaimpact)*100)/(count_vulnibm_iot_namedenialofservice+count_vulnibm_sh_namedenialofservice))))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namedenialofservice_mediumavaimpact+count_vulnibm_sh_namedenialofservice_mediumavaimpact)*100)/(count_vulnibm_iot_namedenialofservice+count_vulnibm_sh_namedenialofservice))))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO \n")
print("\n")
print("      -    EN EL "+str(float((((count_vulnibm_iot_namecodeexecution+count_vulnibm_sh_namecodeexecution)*100)/(count_vulnibm_iot_names+count_vulnibm_sh_names))))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE CODE EXECUTION, LOS PORCENTAJES DE IMPACTO DE DISPONIBILIDAD SON LOS SIGUIENTES:  \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namecodeexecution_highavaimpact+count_vulnibm_sh_namecodeexecution_highavaimpact)*100)/(count_vulnibm_iot_namecodeexecution+count_vulnibm_sh_namecodeexecution))))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namecodeexecution_lowavaimpact+count_vulnibm_sh_namecodeexecution_lowavaimpact)*100)/(count_vulnibm_iot_namecodeexecution+count_vulnibm_sh_namecodeexecution))))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namecodeexecution_mediumavaimpact+count_vulnibm_sh_namecodeexecution_mediumavaimpact)*100)/(count_vulnibm_iot_namecodeexecution+count_vulnibm_sh_namecodeexecution))))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO \n")
print("\n")
print("      -    EN EL "+str(float((((count_vulnibm_iot_namemaninthemiddle+count_vulnibm_sh_namemaninthemiddle)*100)/(count_vulnibm_iot_names+count_vulnibm_sh_names))))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE MAN IN THE MIDDLE, LOS PORCENTAJES DE IMPACTO DE DISPONIBILIDAD SON LOS SIGUIENTES:  \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namemaninthemiddle_highavaimpact+count_vulnibm_sh_namemaninthemiddle_highavaimpact)*100)/(count_vulnibm_iot_namemaninthemiddle+count_vulnibm_sh_namemaninthemiddle))))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namemaninthemiddle_lowavaimpact+count_vulnibm_sh_namemaninthemiddle_lowavaimpact)*100)/(count_vulnibm_iot_namemaninthemiddle+count_vulnibm_sh_namemaninthemiddle))))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namemaninthemiddle_mediumavaimpact+count_vulnibm_sh_namemaninthemiddle_mediumavaimpact)*100)/(count_vulnibm_iot_namemaninthemiddle+count_vulnibm_sh_namemaninthemiddle))))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO \n")
print("\n")
print("      -    EN EL "+str(float((((count_vulnibm_iot_namesqlinjection+count_vulnibm_sh_namesqlinjection)*100)/(count_vulnibm_iot_names+count_vulnibm_sh_names))))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE SQL INJECTION, LOS PORCENTAJES DE IMPACTO DE DISPONIBILIDAD SON LOS SIGUIENTES:  \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namesqlinjection_highavaimpact+count_vulnibm_sh_namesqlinjection_highavaimpact)*100)/(count_vulnibm_iot_namesqlinjection+count_vulnibm_sh_namesqlinjection))))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namesqlinjection_lowavaimpact+count_vulnibm_sh_namesqlinjection_lowavaimpact)*100)/(count_vulnibm_iot_namesqlinjection+count_vulnibm_sh_namesqlinjection))))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namesqlinjection_mediumavaimpact+count_vulnibm_sh_namesqlinjection_mediumavaimpact)*100)/(count_vulnibm_iot_namesqlinjection+count_vulnibm_sh_namesqlinjection))))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO \n")
print("\n")
print("      -    EN EL "+str(float((((count_vulnibm_iot_namecrosssiterequestforgery+count_vulnibm_sh_namecrosssiterequestforgery)*100)/(count_vulnibm_iot_names+count_vulnibm_sh_names))))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE CROSS SITE REQUEST FORGERY, LOS PORCENTAJES DE IMPACTO DE DISPONIBILIDAD SON LOS SIGUIENTES:  \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namecrosssiterequestforgery_highavaimpact+count_vulnibm_sh_namecrosssiterequestforgery_highavaimpact)*100)/(count_vulnibm_iot_namecrosssiterequestforgery+count_vulnibm_sh_namecrosssiterequestforgery))))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namecrosssiterequestforgery_lowavaimpact+count_vulnibm_sh_namecrosssiterequestforgery_lowavaimpact)*100)/(count_vulnibm_iot_namecrosssiterequestforgery+count_vulnibm_sh_namecrosssiterequestforgery))))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namecrosssiterequestforgery_mediumavaimpact+count_vulnibm_sh_namecrosssiterequestforgery_mediumavaimpact)*100)/(count_vulnibm_iot_namecrosssiterequestforgery+count_vulnibm_sh_namecrosssiterequestforgery))))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO \n")
print("\n")
print("      -    EN EL "+str(float((((count_vulnibm_iot_namemoduleexecution+count_vulnibm_sh_namemoduleexecution)*100)/(count_vulnibm_iot_names+count_vulnibm_sh_names))))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE MODULE EXECUTION, LOS PORCENTAJES DE IMPACTO DE DISPONIBILIDAD SON LOS SIGUIENTES:  \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namemoduleexecution_highavaimpact+count_vulnibm_sh_namemoduleexecution_highavaimpact)*100)/(count_vulnibm_iot_namemoduleexecution+count_vulnibm_sh_namemoduleexecution))))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namemoduleexecution_lowavaimpact+count_vulnibm_sh_namemoduleexecution_lowavaimpact)*100)/(count_vulnibm_iot_namemoduleexecution+count_vulnibm_sh_namemoduleexecution))))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namemoduleexecution_mediumavaimpact+count_vulnibm_sh_namemoduleexecution_mediumavaimpact)*100)/(count_vulnibm_iot_namemoduleexecution+count_vulnibm_sh_namemoduleexecution))))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO \n")
print("\n")
print("      -    EN EL "+str(float((((count_vulnibm_iot_namebufferoverflow+count_vulnibm_sh_namebufferoverflow)*100)/(count_vulnibm_iot_names+count_vulnibm_sh_names))))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE BUFFER OVERFLOW, LOS PORCENTAJES DE IMPACTO DE DISPONIBILIDAD SON LOS SIGUIENTES:  \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namebufferoverflow_highavaimpact+count_vulnibm_sh_namebufferoverflow_highavaimpact)*100)/(count_vulnibm_iot_namebufferoverflow+count_vulnibm_sh_namebufferoverflow))))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namebufferoverflow_lowavaimpact+count_vulnibm_sh_namebufferoverflow_lowavaimpact)*100)/(count_vulnibm_iot_namebufferoverflow+count_vulnibm_sh_namebufferoverflow))))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namebufferoverflow_mediumavaimpact+count_vulnibm_sh_namebufferoverflow_mediumavaimpact)*100)/(count_vulnibm_iot_namebufferoverflow+count_vulnibm_sh_namebufferoverflow))))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO \n")
print("\n")
print("      -    EN EL "+str(float((((count_vulnibm_iot_namecommandexecution+count_vulnibm_sh_namecommandexecution)*100)/(count_vulnibm_iot_names+count_vulnibm_sh_names))))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE COMMAND EXECUTION, LOS PORCENTAJES DE IMPACTO DE DISPONIBILIDAD SON LOS SIGUIENTES:  \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namecommandexecution_highavaimpact+count_vulnibm_sh_namecommandexecution_highavaimpact)*100)/(count_vulnibm_iot_namecommandexecution+count_vulnibm_sh_namecommandexecution))))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namecommandexecution_lowavaimpact+count_vulnibm_sh_namecommandexecution_lowavaimpact)*100)/(count_vulnibm_iot_namecommandexecution+count_vulnibm_sh_namecommandexecution))))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namecommandexecution_mediumavaimpact+count_vulnibm_sh_namecommandexecution_mediumavaimpact)*100)/(count_vulnibm_iot_namecommandexecution+count_vulnibm_sh_namecommandexecution))))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO \n")
print("\n")
print("      -    EN EL "+str(float((((count_vulnibm_iot_namespoofing+count_vulnibm_sh_namespoofing)*100)/(count_vulnibm_iot_names+count_vulnibm_sh_names))))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE SPOOFING, LOS PORCENTAJES DE IMPACTO DE DISPONIBILIDAD SON LOS SIGUIENTES:  \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namespoofing_highavaimpact+count_vulnibm_sh_namespoofing_highavaimpact)*100)/(count_vulnibm_iot_namespoofing+count_vulnibm_sh_namespoofing))))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namespoofing_lowavaimpact+count_vulnibm_sh_namespoofing_lowavaimpact)*100)/(count_vulnibm_iot_namespoofing+count_vulnibm_sh_namespoofing))))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namespoofing_mediumavaimpact+count_vulnibm_sh_namespoofing_mediumavaimpact)*100)/(count_vulnibm_iot_namespoofing+count_vulnibm_sh_namespoofing))))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO \n")
print("\n")
print("      -    EN EL "+str(float((((count_vulnibm_iot_nameclickjacking+count_vulnibm_sh_nameclickjacking)*100)/(count_vulnibm_iot_names+count_vulnibm_sh_names))))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE CLICKJACKING, LOS PORCENTAJES DE IMPACTO DE DISPONIBILIDAD SON LOS SIGUIENTES:  \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_nameclickjacking_highavaimpact+count_vulnibm_sh_nameclickjacking_highavaimpact)*100)/(count_vulnibm_iot_nameclickjacking+count_vulnibm_sh_nameclickjacking))))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_nameclickjacking_lowavaimpact+count_vulnibm_sh_nameclickjacking_lowavaimpact)*100)/(count_vulnibm_iot_nameclickjacking+count_vulnibm_sh_nameclickjacking))))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_nameclickjacking_mediumavaimpact+count_vulnibm_sh_nameclickjacking_mediumavaimpact)*100)/(count_vulnibm_iot_nameclickjacking+count_vulnibm_sh_nameclickjacking))))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO \n")
print("\n")
print("      -    EN EL "+str(float((((count_vulnibm_iot_namehijacking+count_vulnibm_sh_namehijacking)*100)/(count_vulnibm_iot_names+count_vulnibm_sh_names))))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE HIJACKING, LOS PORCENTAJES DE IMPACTO DE DISPONIBILIDAD SON LOS SIGUIENTES:  \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namehijacking_highavaimpact+count_vulnibm_sh_namehijacking_highavaimpact)*100)/(count_vulnibm_iot_namehijacking+count_vulnibm_sh_namehijacking))))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namehijacking_lowavaimpact+count_vulnibm_sh_namehijacking_lowavaimpact)*100)/(count_vulnibm_iot_namehijacking+count_vulnibm_sh_namehijacking))))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namehijacking_mediumavaimpact+count_vulnibm_sh_namehijacking_mediumavaimpact)*100)/(count_vulnibm_iot_namehijacking+count_vulnibm_sh_namehijacking))))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO \n")
print("\n")
print("      -    EN EL "+str(float((((count_vulnibm_iot_namefileinclude+count_vulnibm_sh_namefileinclude)*100)/(count_vulnibm_iot_names+count_vulnibm_sh_names))))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE FILE INCLUDE, LOS PORCENTAJES DE IMPACTO DE DISPONIBILIDAD SON LOS SIGUIENTES:  \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namefileinclude_highavaimpact+count_vulnibm_sh_namefileinclude_highavaimpact)*100)/(count_vulnibm_iot_namefileinclude+count_vulnibm_sh_namefileinclude))))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namefileinclude_lowavaimpact+count_vulnibm_sh_namefileinclude_lowavaimpact)*100)/(count_vulnibm_iot_namefileinclude+count_vulnibm_sh_namefileinclude))))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namefileinclude_mediumavaimpact+count_vulnibm_sh_namefileinclude_mediumavaimpact)*100)/(count_vulnibm_iot_namefileinclude+count_vulnibm_sh_namefileinclude))))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO \n")
print("\n")
print("      -    EN EL "+str(float((((count_vulnibm_iot_namebruteforce+count_vulnibm_sh_namebruteforce)*100)/(count_vulnibm_iot_names+count_vulnibm_sh_names))))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE BRUTE FORCE, LOS PORCENTAJES DE IMPACTO DE DISPONIBILIDAD SON LOS SIGUIENTES:  \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namebruteforce_highavaimpact+count_vulnibm_sh_namebruteforce_highavaimpact)*100)/(count_vulnibm_iot_namebruteforce+count_vulnibm_sh_namebruteforce))))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namebruteforce_lowavaimpact+count_vulnibm_sh_namebruteforce_lowavaimpact)*100)/(count_vulnibm_iot_namebruteforce+count_vulnibm_sh_namebruteforce))))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namebruteforce_mediumavaimpact+count_vulnibm_sh_namebruteforce_mediumavaimpact)*100)/(count_vulnibm_iot_namebruteforce+count_vulnibm_sh_namebruteforce))))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO \n")
print("\n")
print("      -    EN EL "+str(float((((count_vulnibm_iot_namefileupload+count_vulnibm_sh_namefileupload)*100)/(count_vulnibm_iot_names+count_vulnibm_sh_names))))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE FILE UPLOAD, LOS PORCENTAJES DE IMPACTO DE DISPONIBILIDAD SON LOS SIGUIENTES:  \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namefileupload_highavaimpact+count_vulnibm_sh_namefileupload_highavaimpact)*100)/(count_vulnibm_iot_namefileupload+count_vulnibm_sh_namefileupload))))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namefileupload_lowavaimpact+count_vulnibm_sh_namefileupload_lowavaimpact)*100)/(count_vulnibm_iot_namefileupload+count_vulnibm_sh_namefileupload))))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namefileupload_mediumavaimpact+count_vulnibm_sh_namefileupload_mediumavaimpact)*100)/(count_vulnibm_iot_namefileupload+count_vulnibm_sh_namefileupload))))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO \n")
print("\n")
print("      -    EN EL "+str(float((((count_vulnibm_iot_nameheaderinjection+count_vulnibm_sh_nameheaderinjection)*100)/(count_vulnibm_iot_names+count_vulnibm_sh_names))))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE HEADER INJECTION, LOS PORCENTAJES DE IMPACTO DE DISPONIBILIDAD SON LOS SIGUIENTES:  \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_nameheaderinjection_highavaimpact+count_vulnibm_sh_nameheaderinjection_highavaimpact)*100)/(count_vulnibm_iot_nameheaderinjection+count_vulnibm_sh_nameheaderinjection))))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_nameheaderinjection_lowavaimpact+count_vulnibm_sh_nameheaderinjection_lowavaimpact)*100)/(count_vulnibm_iot_nameheaderinjection+count_vulnibm_sh_nameheaderinjection))))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_nameheaderinjection_mediumavaimpact+count_vulnibm_sh_nameheaderinjection_mediumavaimpact)*100)/(count_vulnibm_iot_nameheaderinjection+count_vulnibm_sh_nameheaderinjection))))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO \n")
print("\n")
print("      -    EN EL "+str(float((((count_vulnibm_iot_nametampering+count_vulnibm_sh_nametampering)*100)/(count_vulnibm_iot_names+count_vulnibm_sh_names))))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE TAMPERING, LOS PORCENTAJES DE IMPACTO DE DISPONIBILIDAD SON LOS SIGUIENTES:  \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_nametampering_highavaimpact+count_vulnibm_sh_nametampering_highavaimpact)*100)/(count_vulnibm_iot_nametampering+count_vulnibm_sh_nametampering))))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_nametampering_lowavaimpact+count_vulnibm_sh_nametampering_lowavaimpact)*100)/(count_vulnibm_iot_nametampering+count_vulnibm_sh_nametampering))))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_nametampering_mediumavaimpact+count_vulnibm_sh_nametampering_mediumavaimpact)*100)/(count_vulnibm_iot_nametampering+count_vulnibm_sh_nametampering))))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO \n")
print("\n")
print("      -    EN EL "+str(float((((count_vulnibm_iot_nameanother+count_vulnibm_sh_nameanother)*100)/(count_vulnibm_iot_names+count_vulnibm_sh_names))))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE UN VALOR DISTINTO, LOS PORCENTAJES DE IMPACTO DE DISPONIBILIDAD SON LOS SIGUIENTES:  \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_nameanother_highavaimpact+count_vulnibm_sh_nameanother_highavaimpact)*100)/(count_vulnibm_iot_nameanother+count_vulnibm_sh_nameanother))))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_nameanother_lowavaimpact+count_vulnibm_sh_nameanother_lowavaimpact)*100)/(count_vulnibm_iot_nameanother+count_vulnibm_sh_nameanother))))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_nameanother_mediumavaimpact+count_vulnibm_sh_nameanother_mediumavaimpact)*100)/(count_vulnibm_iot_nameanother+count_vulnibm_sh_nameanother))))+" % DE VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO \n")
print("\n")
               	










































