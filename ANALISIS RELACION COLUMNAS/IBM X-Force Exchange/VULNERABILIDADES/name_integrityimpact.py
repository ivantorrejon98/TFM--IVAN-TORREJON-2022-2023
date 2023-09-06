import pandas as pd
from datetime import datetime,timedelta



#Abro los ficheros con los que voy a tratar




df_vulnibm_iot = pd.read_excel('vulnerabilidades_ibm_iot_2023.xlsx')

#Variable para almacenar el contador total de valores de nombre
count_vulnibm_iot_names=0
#Variable para almacenar el contador total de valores de un nombre concreto
count_vulnibm_iot_namepathtraversal=0
#Variables para almacenar el contador de valores de impacto de INTEGRIDAD dato un valor de nombre especifico
count_vulnibm_iot_namepathtraversal_intimpact=0
count_vulnibm_iot_namepathtraversal_highintimpact=0
count_vulnibm_iot_namepathtraversal_lowintimpact=0
count_vulnibm_iot_namepathtraversal_mediumintimpact=0

count_vulnibm_iot_namedirectorytraversal=0
count_vulnibm_iot_namedirectorytraversal_intimpact=0
count_vulnibm_iot_namedirectorytraversal_highintimpact=0
count_vulnibm_iot_namedirectorytraversal_lowintimpact=0
count_vulnibm_iot_namedirectorytraversal_mediumintimpact=0

count_vulnibm_iot_nameprivilegeescalation=0
count_vulnibm_iot_nameprivilegeescalation_intimpact=0
count_vulnibm_iot_nameprivilegeescalation_highintimpact=0
count_vulnibm_iot_nameprivilegeescalation_lowintimpact=0
count_vulnibm_iot_nameprivilegeescalation_mediumintimpact=0

count_vulnibm_iot_namecrosssitescripting=0
count_vulnibm_iot_namecrosssitescripting_intimpact=0
count_vulnibm_iot_namecrosssitescripting_highintimpact=0
count_vulnibm_iot_namecrosssitescripting_lowintimpact=0
count_vulnibm_iot_namecrosssitescripting_mediumintimpact=0

count_vulnibm_iot_namesecuritybypass=0
count_vulnibm_iot_namesecuritybypass_intimpact=0
count_vulnibm_iot_namesecuritybypass_highintimpact=0
count_vulnibm_iot_namesecuritybypass_lowintimpact=0
count_vulnibm_iot_namesecuritybypass_mediumintimpact=0

count_vulnibm_iot_nameinformationdisclosure=0
count_vulnibm_iot_nameinformationdisclosure_intimpact=0
count_vulnibm_iot_nameinformationdisclosure_highintimpact=0
count_vulnibm_iot_nameinformationdisclosure_lowintimpact=0
count_vulnibm_iot_nameinformationdisclosure_mediumintimpact=0

count_vulnibm_iot_namedenialofservice=0
count_vulnibm_iot_namedenialofservice_intimpact=0
count_vulnibm_iot_namedenialofservice_highintimpact=0
count_vulnibm_iot_namedenialofservice_lowintimpact=0
count_vulnibm_iot_namedenialofservice_mediumintimpact=0

count_vulnibm_iot_namecodeexecution=0
count_vulnibm_iot_namecodeexecution_intimpact=0
count_vulnibm_iot_namecodeexecution_highintimpact=0
count_vulnibm_iot_namecodeexecution_lowintimpact=0
count_vulnibm_iot_namecodeexecution_mediumintimpact=0

count_vulnibm_iot_namemaninthemiddle=0
count_vulnibm_iot_namemaninthemiddle_intimpact=0
count_vulnibm_iot_namemaninthemiddle_highintimpact=0
count_vulnibm_iot_namemaninthemiddle_lowintimpact=0
count_vulnibm_iot_namemaninthemiddle_mediumintimpact=0

count_vulnibm_iot_namesqlinjection=0
count_vulnibm_iot_namesqlinjection_intimpact=0
count_vulnibm_iot_namesqlinjection_highintimpact=0
count_vulnibm_iot_namesqlinjection_lowintimpact=0
count_vulnibm_iot_namesqlinjection_mediumintimpact=0

count_vulnibm_iot_namecrosssiterequestforgery=0
count_vulnibm_iot_namecrosssiterequestforgery_intimpact=0
count_vulnibm_iot_namecrosssiterequestforgery_highintimpact=0
count_vulnibm_iot_namecrosssiterequestforgery_lowintimpact=0
count_vulnibm_iot_namecrosssiterequestforgery_mediumintimpact=0

count_vulnibm_iot_namemoduleexecution=0
count_vulnibm_iot_namemoduleexecution_intimpact=0
count_vulnibm_iot_namemoduleexecution_highintimpact=0
count_vulnibm_iot_namemoduleexecution_lowintimpact=0
count_vulnibm_iot_namemoduleexecution_mediumintimpact=0

count_vulnibm_iot_namebufferoverflow=0
count_vulnibm_iot_namebufferoverflow_intimpact=0
count_vulnibm_iot_namebufferoverflow_highintimpact=0
count_vulnibm_iot_namebufferoverflow_lowintimpact=0
count_vulnibm_iot_namebufferoverflow_mediumintimpact=0

count_vulnibm_iot_namecommandexecution=0
count_vulnibm_iot_namecommandexecution_intimpact=0
count_vulnibm_iot_namecommandexecution_highintimpact=0
count_vulnibm_iot_namecommandexecution_lowintimpact=0
count_vulnibm_iot_namecommandexecution_mediumintimpact=0

count_vulnibm_iot_namespoofing=0
count_vulnibm_iot_namespoofing_intimpact=0
count_vulnibm_iot_namespoofing_highintimpact=0
count_vulnibm_iot_namespoofing_lowintimpact=0
count_vulnibm_iot_namespoofing_mediumintimpact=0

count_vulnibm_iot_nameclickjacking=0
count_vulnibm_iot_nameclickjacking_intimpact=0
count_vulnibm_iot_nameclickjacking_highintimpact=0
count_vulnibm_iot_nameclickjacking_lowintimpact=0
count_vulnibm_iot_nameclickjacking_mediumintimpact=0

count_vulnibm_iot_namehijacking=0
count_vulnibm_iot_namehijacking_intimpact=0
count_vulnibm_iot_namehijacking_highintimpact=0
count_vulnibm_iot_namehijacking_lowintimpact=0
count_vulnibm_iot_namehijacking_mediumintimpact=0

count_vulnibm_iot_namefileinclude=0
count_vulnibm_iot_namefileinclude_intimpact=0
count_vulnibm_iot_namefileinclude_highintimpact=0
count_vulnibm_iot_namefileinclude_lowintimpact=0
count_vulnibm_iot_namefileinclude_mediumintimpact=0

count_vulnibm_iot_namebruteforce=0
count_vulnibm_iot_namebruteforce_intimpact=0
count_vulnibm_iot_namebruteforce_highintimpact=0
count_vulnibm_iot_namebruteforce_lowintimpact=0
count_vulnibm_iot_namebruteforce_mediumintimpact=0

count_vulnibm_iot_namefileupload=0
count_vulnibm_iot_namefileupload_intimpact=0
count_vulnibm_iot_namefileupload_highintimpact=0
count_vulnibm_iot_namefileupload_lowintimpact=0
count_vulnibm_iot_namefileupload_mediumintimpact=0

count_vulnibm_iot_nameheaderinjection=0
count_vulnibm_iot_nameheaderinjection_intimpact=0
count_vulnibm_iot_nameheaderinjection_highintimpact=0
count_vulnibm_iot_nameheaderinjection_lowintimpact=0
count_vulnibm_iot_nameheaderinjection_mediumintimpact=0

count_vulnibm_iot_nametampering=0
count_vulnibm_iot_nametampering_intimpact=0
count_vulnibm_iot_nametampering_highintimpact=0
count_vulnibm_iot_nametampering_lowintimpact=0
count_vulnibm_iot_nametampering_mediumintimpact=0

count_vulnibm_iot_nameanother=0
count_vulnibm_iot_nameanother_intimpact=0
count_vulnibm_iot_nameanother_highintimpact=0
count_vulnibm_iot_nameanother_lowintimpact=0
count_vulnibm_iot_nameanother_mediumintimpact=0

#Comprobamos el contenido de name
for r in range(0,len(df_vulnibm_iot["name"])):                       
    aux_str=df_vulnibm_iot["name"][r].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
    if(aux_str!='NONE'):
        count_vulnibm_iot_names+=1
        #Compruebo el valor de nombre
        if('pathtraversal' in aux_str):
            count_vulnibm_iot_namepathtraversal+=1
            #Compruebo el valor de impacto de INTEGRIDAD
            if(df_vulnibm_iot["x_xfe_cvss_integrity_impact"][r]=='High'):
                count_vulnibm_iot_namepathtraversal_intimpact+=1
                count_vulnibm_iot_namepathtraversal_highintimpact+=1
            elif(df_vulnibm_iot["x_xfe_cvss_integrity_impact"][r]=='Low'):
                count_vulnibm_iot_namepathtraversal_intimpact+=1
                count_vulnibm_iot_namepathtraversal_lowintimpact+=1
            elif(df_vulnibm_iot["x_xfe_cvss_integrity_impact"][r]=='Medium'):
                count_vulnibm_iot_namepathtraversal_intimpact+=1
                count_vulnibm_iot_namepathtraversal_mediumintimpact+=1
    
        elif('directorytraversal' in aux_str):
            
            count_vulnibm_iot_namedirectorytraversal+=1
            if(df_vulnibm_iot["x_xfe_cvss_integrity_impact"][r]=='High'):
                count_vulnibm_iot_namedirectorytraversal_intimpact+=1
                count_vulnibm_iot_namedirectorytraversal_highintimpact+=1
            elif(df_vulnibm_iot["x_xfe_cvss_integrity_impact"][r]=='Low'):
                count_vulnibm_iot_namedirectorytraversal_intimpact+=1
                count_vulnibm_iot_namedirectorytraversal_lowintimpact+=1
            elif(df_vulnibm_iot["x_xfe_cvss_integrity_impact"][r]=='Medium'):
                count_vulnibm_iot_namedirectorytraversal_intimpact+=1
                count_vulnibm_iot_namedirectorytraversal_mediumintimpact+=1
            
            
        elif('privilegeescalation' in aux_str):
        
            count_vulnibm_iot_nameprivilegeescalation+=1
            if(df_vulnibm_iot["x_xfe_cvss_integrity_impact"][r]=='High'):
                count_vulnibm_iot_nameprivilegeescalation_intimpact+=1
                count_vulnibm_iot_nameprivilegeescalation_highintimpact+=1
            elif(df_vulnibm_iot["x_xfe_cvss_integrity_impact"][r]=='Low'):
                count_vulnibm_iot_nameprivilegeescalation_intimpact+=1
                count_vulnibm_iot_nameprivilegeescalation_lowintimpact+=1
            elif(df_vulnibm_iot["x_xfe_cvss_integrity_impact"][r]=='Medium'):
                count_vulnibm_iot_nameprivilegeescalation_intimpact+=1
                count_vulnibm_iot_nameprivilegeescalation_mediumintimpact+=1
            
        elif('cross-sitescripting' in aux_str):
        
            count_vulnibm_iot_namecrosssitescripting+=1
            if(df_vulnibm_iot["x_xfe_cvss_integrity_impact"][r]=='High'):
                count_vulnibm_iot_namecrosssitescripting_intimpact+=1
                count_vulnibm_iot_namecrosssitescripting_highintimpact+=1
            elif(df_vulnibm_iot["x_xfe_cvss_integrity_impact"][r]=='Low'):
                count_vulnibm_iot_namecrosssitescripting_intimpact+=1
                count_vulnibm_iot_namecrosssitescripting_lowintimpact+=1
            elif(df_vulnibm_iot["x_xfe_cvss_integrity_impact"][r]=='Medium'):
                count_vulnibm_iot_namecrosssitescripting_intimpact+=1
                count_vulnibm_iot_namecrosssitescripting_mediumintimpact+=1
                                         
        elif('securitybypass' in aux_str):
        
            count_vulnibm_iot_namesecuritybypass+=1
            if(df_vulnibm_iot["x_xfe_cvss_integrity_impact"][r]=='High'):
                count_vulnibm_iot_namesecuritybypass_intimpact+=1
                count_vulnibm_iot_namesecuritybypass_highintimpact+=1
            elif(df_vulnibm_iot["x_xfe_cvss_integrity_impact"][r]=='Low'):
                count_vulnibm_iot_namesecuritybypass_intimpact+=1
                count_vulnibm_iot_namesecuritybypass_lowintimpact+=1
            elif(df_vulnibm_iot["x_xfe_cvss_integrity_impact"][r]=='Medium'):
                count_vulnibm_iot_namesecuritybypass_intimpact+=1
                count_vulnibm_iot_namesecuritybypass_mediumintimpact+=1
                                         
        elif('information_disclosure' in aux_str or 'informationdisclosure' in aux_str):
        
            count_vulnibm_iot_nameinformationdisclosure+=1
            if(df_vulnibm_iot["x_xfe_cvss_integrity_impact"][r]=='High'):
                count_vulnibm_iot_nameinformationdisclosure_intimpact+=1
                count_vulnibm_iot_nameinformationdisclosure_highintimpact+=1
            elif(df_vulnibm_iot["x_xfe_cvss_integrity_impact"][r]=='Low'):
                count_vulnibm_iot_nameinformationdisclosure_intimpact+=1
                count_vulnibm_iot_nameinformationdisclosure_lowintimpact+=1
            elif(df_vulnibm_iot["x_xfe_cvss_integrity_impact"][r]=='Medium'):
                count_vulnibm_iot_nameinformationdisclosure_intimpact+=1
                count_vulnibm_iot_nameinformationdisclosure_mediumintimpact+=1
                                         
        elif('denialofservice' in aux_str):
            
            count_vulnibm_iot_namedenialofservice+=1
            if(df_vulnibm_iot["x_xfe_cvss_integrity_impact"][r]=='High'):
                count_vulnibm_iot_namedenialofservice_intimpact+=1
                count_vulnibm_iot_namedenialofservice_highintimpact+=1
            elif(df_vulnibm_iot["x_xfe_cvss_integrity_impact"][r]=='Low'):
                count_vulnibm_iot_namedenialofservice_intimpact+=1
                count_vulnibm_iot_namedenialofservice_lowintimpact+=1
            elif(df_vulnibm_iot["x_xfe_cvss_integrity_impact"][r]=='Medium'):
                count_vulnibm_iot_namedenialofservice_intimpact+=1
                count_vulnibm_iot_namedenialofservice_mediumintimpact+=1
            
        elif('codeexecution' in aux_str):
        
        
            count_vulnibm_iot_namecodeexecution+=1
            if(df_vulnibm_iot["x_xfe_cvss_integrity_impact"][r]=='High'):
                count_vulnibm_iot_namecodeexecution_intimpact+=1
                count_vulnibm_iot_namecodeexecution_highintimpact+=1
            elif(df_vulnibm_iot["x_xfe_cvss_integrity_impact"][r]=='Low'):
                count_vulnibm_iot_namecodeexecution_intimpact+=1
                count_vulnibm_iot_namecodeexecution_lowintimpact+=1
            elif(df_vulnibm_iot["x_xfe_cvss_integrity_impact"][r]=='Medium'):
                count_vulnibm_iot_namecodeexecution_intimpact+=1
                count_vulnibm_iot_namecodeexecution_mediumintimpact+=1
                                         
        elif('maninthemiddle' in aux_str):
        
            count_vulnibm_iot_namemaninthemiddle+=1
            if(df_vulnibm_iot["x_xfe_cvss_integrity_impact"][r]=='High'):
                count_vulnibm_iot_namemaninthemiddle_intimpact+=1
                count_vulnibm_iot_namemaninthemiddle_highintimpact+=1
            elif(df_vulnibm_iot["x_xfe_cvss_integrity_impact"][r]=='Low'):
                count_vulnibm_iot_namemaninthemiddle_intimpact+=1
                count_vulnibm_iot_namemaninthemiddle_lowintimpact+=1
            elif(df_vulnibm_iot["x_xfe_cvss_integrity_impact"][r]=='Medium'):
                count_vulnibm_iot_namemaninthemiddle_intimpact+=1
                count_vulnibm_iot_namemaninthemiddle_mediumintimpact+=1
                                         
        elif('SQLinjection' in aux_str):
        
            count_vulnibm_iot_namesqlinjection+=1
            if(df_vulnibm_iot["x_xfe_cvss_integrity_impact"][r]=='High'):
                count_vulnibm_iot_namesqlinjection_intimpact+=1
                count_vulnibm_iot_namesqlinjection_highintimpact+=1
            elif(df_vulnibm_iot["x_xfe_cvss_integrity_impact"][r]=='Low'):
                count_vulnibm_iot_namesqlinjection_intimpact+=1
                count_vulnibm_iot_namesqlinjection_lowintimpact+=1
            elif(df_vulnibm_iot["x_xfe_cvss_integrity_impact"][r]=='Medium'):
                count_vulnibm_iot_namesqlinjection_intimpact+=1
                count_vulnibm_iot_namesqlinjection_mediumintimpact+=1
                                         
        elif('cross-siterequestforgery' in aux_str):
        
            count_vulnibm_iot_namecrosssiterequestforgery+=1
            if(df_vulnibm_iot["x_xfe_cvss_integrity_impact"][r]=='High'):
                count_vulnibm_iot_namecrosssiterequestforgery_intimpact+=1
                count_vulnibm_iot_namecrosssiterequestforgery_highintimpact+=1
            elif(df_vulnibm_iot["x_xfe_cvss_integrity_impact"][r]=='Low'):
                count_vulnibm_iot_namecrosssiterequestforgery_intimpact+=1
                count_vulnibm_iot_namecrosssiterequestforgery_lowintimpact+=1
            elif(df_vulnibm_iot["x_xfe_cvss_integrity_impact"][r]=='Medium'):
                count_vulnibm_iot_namecrosssiterequestforgery_intimpact+=1
                count_vulnibm_iot_namecrosssiterequestforgery_mediumintimpact+=1
                                         
        elif('moduleexecution' in aux_str):
        
            count_vulnibm_iot_namemoduleexecution+=1
            if(df_vulnibm_iot["x_xfe_cvss_integrity_impact"][r]=='High'):
                count_vulnibm_iot_namemoduleexecution_intimpact+=1
                count_vulnibm_iot_namemoduleexecution_highintimpact+=1
            elif(df_vulnibm_iot["x_xfe_cvss_integrity_impact"][r]=='Low'):
                count_vulnibm_iot_namemoduleexecution_intimpact+=1
                count_vulnibm_iot_namemoduleexecution_lowintimpact+=1
            elif(df_vulnibm_iot["x_xfe_cvss_integrity_impact"][r]=='Medium'):
                count_vulnibm_iot_namemoduleexecution_intimpact+=1
                count_vulnibm_iot_namemoduleexecution_mediumintimpact+=1
                                         
        elif('bufferoverflow' in aux_str):
        
            count_vulnibm_iot_namebufferoverflow+=1
            if(df_vulnibm_iot["x_xfe_cvss_integrity_impact"][r]=='High'):
                count_vulnibm_iot_namebufferoverflow_intimpact+=1
                count_vulnibm_iot_namebufferoverflow_highintimpact+=1
            elif(df_vulnibm_iot["x_xfe_cvss_integrity_impact"][r]=='Low'):
                count_vulnibm_iot_namebufferoverflow_intimpact+=1
                count_vulnibm_iot_namebufferoverflow_lowintimpact+=1
            elif(df_vulnibm_iot["x_xfe_cvss_integrity_impact"][r]=='Medium'):
                count_vulnibm_iot_namebufferoverflow_intimpact+=1
                count_vulnibm_iot_namebufferoverflow_mediumintimpact+=1
                                         
        elif('commandexecution' in aux_str):
        
            count_vulnibm_iot_namecommandexecution+=1
            if(df_vulnibm_iot["x_xfe_cvss_integrity_impact"][r]=='High'):
                count_vulnibm_iot_namecommandexecution_intimpact+=1
                count_vulnibm_iot_namecommandexecution_highintimpact+=1
            elif(df_vulnibm_iot["x_xfe_cvss_integrity_impact"][r]=='Low'):
                count_vulnibm_iot_namecommandexecution_intimpact+=1
                count_vulnibm_iot_namecommandexecution_lowintimpact+=1
            elif(df_vulnibm_iot["x_xfe_cvss_integrity_impact"][r]=='Medium'):
                count_vulnibm_iot_namecommandexecution_intimpact+=1
                count_vulnibm_iot_namecommandexecution_mediumintimpact+=1
                                         
        elif('spoofing' in aux_str):
        
            count_vulnibm_iot_namespoofing+=1
            if(df_vulnibm_iot["x_xfe_cvss_integrity_impact"][r]=='High'):
                count_vulnibm_iot_namespoofing_intimpact+=1
                count_vulnibm_iot_namespoofing_highintimpact+=1
            elif(df_vulnibm_iot["x_xfe_cvss_integrity_impact"][r]=='Low'):
                count_vulnibm_iot_namespoofing_intimpact+=1
                count_vulnibm_iot_namespoofing_lowintimpact+=1
            elif(df_vulnibm_iot["x_xfe_cvss_integrity_impact"][r]=='Medium'):
                count_vulnibm_iot_namespoofing_intimpact+=1
                count_vulnibm_iot_namespoofing_mediumintimpact+=1
                                         
        elif('clickjacking' in aux_str):
        
            count_vulnibm_iot_nameclickjacking+=1
            if(df_vulnibm_iot["x_xfe_cvss_integrity_impact"][r]=='High'):
                count_vulnibm_iot_nameclickjacking_intimpact+=1
                count_vulnibm_iot_nameclickjacking_highintimpact+=1
            elif(df_vulnibm_iot["x_xfe_cvss_integrity_impact"][r]=='Low'):
                count_vulnibm_iot_nameclickjacking_intimpact+=1
                count_vulnibm_iot_nameclickjacking_lowintimpact+=1
            elif(df_vulnibm_iot["x_xfe_cvss_integrity_impact"][r]=='Medium'):
                count_vulnibm_iot_nameclickjacking_intimpact+=1
                count_vulnibm_iot_nameclickjacking_mediumintimpact+=1
              
        elif('hijacking' in aux_str):
        
            count_vulnibm_iot_namehijacking+=1
            if(df_vulnibm_iot["x_xfe_cvss_integrity_impact"][r]=='High'):
                count_vulnibm_iot_namehijacking_intimpact+=1
                count_vulnibm_iot_namehijacking_highintimpact+=1
            elif(df_vulnibm_iot["x_xfe_cvss_integrity_impact"][r]=='Low'):
                count_vulnibm_iot_namehijacking_intimpact+=1
                count_vulnibm_iot_namehijacking_lowintimpact+=1
            elif(df_vulnibm_iot["x_xfe_cvss_integrity_impact"][r]=='Medium'):
                count_vulnibm_iot_namehijacking_intimpact+=1
                count_vulnibm_iot_namehijacking_mediumintimpact+=1
               
        elif('fileinclude' in aux_str):
        
            count_vulnibm_iot_namefileinclude+=1
            if(df_vulnibm_iot["x_xfe_cvss_integrity_impact"][r]=='High'):
                count_vulnibm_iot_namefileinclude_intimpact+=1
                count_vulnibm_iot_namefileinclude_highintimpact+=1
            elif(df_vulnibm_iot["x_xfe_cvss_integrity_impact"][r]=='Low'):
                count_vulnibm_iot_namefileinclude_intimpact+=1
                count_vulnibm_iot_namefileinclude_lowintimpact+=1
            elif(df_vulnibm_iot["x_xfe_cvss_integrity_impact"][r]=='Medium'):
                count_vulnibm_iot_namefileinclude_intimpact+=1
                count_vulnibm_iot_namefileinclude_mediumintimpact+=1
                
               
        elif('bruteforce' in aux_str):
        
            count_vulnibm_iot_namebruteforce+=1
            if(df_vulnibm_iot["x_xfe_cvss_integrity_impact"][r]=='High'):
                count_vulnibm_iot_namebruteforce_intimpact+=1
                count_vulnibm_iot_namebruteforce_highintimpact+=1
            elif(df_vulnibm_iot["x_xfe_cvss_integrity_impact"][r]=='Low'):
                count_vulnibm_iot_namebruteforce_intimpact+=1
                count_vulnibm_iot_namebruteforce_lowintimpact+=1
            elif(df_vulnibm_iot["x_xfe_cvss_integrity_impact"][r]=='Medium'):
                count_vulnibm_iot_namebruteforce_intimpact+=1
                count_vulnibm_iot_namebruteforce_mediumintimpact+=1
                
               
        elif('fileupload' in aux_str):
        
            count_vulnibm_iot_namefileupload+=1
            if(df_vulnibm_iot["x_xfe_cvss_integrity_impact"][r]=='High'):
                count_vulnibm_iot_namefileupload_intimpact+=1
                count_vulnibm_iot_namefileupload_highintimpact+=1
            elif(df_vulnibm_iot["x_xfe_cvss_integrity_impact"][r]=='Low'):
                count_vulnibm_iot_namefileupload_intimpact+=1
                count_vulnibm_iot_namefileupload_lowintimpact+=1
            elif(df_vulnibm_iot["x_xfe_cvss_integrity_impact"][r]=='Medium'):
                count_vulnibm_iot_namefileupload_intimpact+=1
                count_vulnibm_iot_namefileupload_mediumintimpact+=1
                
               
        elif('headerinjection' in aux_str):
        
            count_vulnibm_iot_nameheaderinjection+=1
            if(df_vulnibm_iot["x_xfe_cvss_integrity_impact"][r]=='High'):
                count_vulnibm_iot_nameheaderinjection_intimpact+=1
                count_vulnibm_iot_nameheaderinjection_highintimpact+=1
            elif(df_vulnibm_iot["x_xfe_cvss_integrity_impact"][r]=='Low'):
                count_vulnibm_iot_nameheaderinjection_intimpact+=1
                count_vulnibm_iot_nameheaderinjection_lowintimpact+=1
            elif(df_vulnibm_iot["x_xfe_cvss_integrity_impact"][r]=='Medium'):
                count_vulnibm_iot_nameheaderinjection_intimpact+=1
                count_vulnibm_iot_nameheaderinjection_mediumintimpact+=1
               
        elif('Tampering' in aux_str):
        
            count_vulnibm_iot_nametampering+=1
            if(df_vulnibm_iot["x_xfe_cvss_integrity_impact"][r]=='High'):
                count_vulnibm_iot_nametampering_intimpact+=1
                count_vulnibm_iot_nametampering_highintimpact+=1
            elif(df_vulnibm_iot["x_xfe_cvss_integrity_impact"][r]=='Low'):
                count_vulnibm_iot_nametampering_intimpact+=1
                count_vulnibm_iot_nametampering_lowintimpact+=1
            elif(df_vulnibm_iot["x_xfe_cvss_integrity_impact"][r]=='Medium'):
                count_vulnibm_iot_nametampering_intimpact+=1
                count_vulnibm_iot_nametampering_mediumintimpact+=1
    
        else:
        
            count_vulnibm_iot_nameanother+=1
            if(df_vulnibm_iot["x_xfe_cvss_integrity_impact"][r]=='High'):
                count_vulnibm_iot_nameanother_intimpact+=1
                count_vulnibm_iot_nameanother_highintimpact+=1
            elif(df_vulnibm_iot["x_xfe_cvss_integrity_impact"][r]=='Low'):
                count_vulnibm_iot_nameanother_intimpact+=1
                count_vulnibm_iot_nameanother_lowintimpact+=1
            elif(df_vulnibm_iot["x_xfe_cvss_integrity_impact"][r]=='Medium'):
                count_vulnibm_iot_nameanother_intimpact+=1
                count_vulnibm_iot_nameanother_mediumintimpact+=1
                
                
                
                
                
print("**********************************************ESTADÍSTICAS NOMBRE/IMPACTO DE INTEGRIDAD VULNERABILIDADES IBM PARTE IOT**********************************************")
print("\n")                            
print("\n")
print(" DE UN TOTAL DE "+str(count_vulnibm_iot_names)+" VULNERABILIDADES:\n") 
print("\n")
print("   - LAS ESTADISTICAS DE VALORES DE NOMBRE SON LAS SIGUIENTES:  \n")
print("      -    EN  "+str(count_vulnibm_iot_namepathtraversal)+" VULNERABILIDADES EL NOMBRE INCLUYE PATH TRAVERSAL, LAS ESTADÍSTICAS DE IMPACTO DE INTEGRIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_namepathtraversal_highintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_iot_namepathtraversal_lowintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_iot_namepathtraversal_mediumintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO\n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_namedirectorytraversal)+" VULNERABILIDADES EL NOMBRE INCLUYE DIRECTORY TRAVERSAL, LAS ESTADÍSTICAS DE IMPACTO DE INTEGRIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_namedirectorytraversal_highintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_iot_namedirectorytraversal_lowintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_iot_namedirectorytraversal_mediumintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO\n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_nameprivilegeescalation)+" VULNERABILIDADES EL NOMBRE INCLUYE PRIVILEGE ESCALATION, LAS ESTADÍSTICAS DE IMPACTO DE INTEGRIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_nameprivilegeescalation_highintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_iot_nameprivilegeescalation_lowintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_iot_nameprivilegeescalation_mediumintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO\n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_namecrosssitescripting)+" VULNERABILIDADES EL NOMBRE INCLUYE CROSS SITE SCRIPTING, LAS ESTADÍSTICAS DE IMPACTO DE INTEGRIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_namecrosssitescripting_highintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_iot_namecrosssitescripting_lowintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_iot_namecrosssitescripting_mediumintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO\n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_namesecuritybypass)+" VULNERABILIDADES EL NOMBRE INCLUYE SECURITY BYPASS, LAS ESTADÍSTICAS DE IMPACTO DE INTEGRIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_namesecuritybypass_highintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_iot_namesecuritybypass_lowintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_iot_namesecuritybypass_mediumintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO\n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_nameinformationdisclosure)+" VULNERABILIDADES EL NOMBRE INCLUYE INFORMATION DISCLOSURE, LAS ESTADÍSTICAS DE IMPACTO DE INTEGRIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_nameinformationdisclosure_highintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_iot_nameinformationdisclosure_lowintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_iot_nameinformationdisclosure_mediumintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO\n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_namedenialofservice)+" VULNERABILIDADES EL NOMBRE INCLUYE DENIAL OF SERVICE, LAS ESTADÍSTICAS DE IMPACTO DE INTEGRIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_namedenialofservice_highintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_iot_namedenialofservice_lowintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_iot_namedenialofservice_mediumintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO\n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_namecodeexecution)+" VULNERABILIDADES EL NOMBRE INCLUYE CODE EXECUTION, LAS ESTADÍSTICAS DE IMPACTO DE INTEGRIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_namecodeexecution_highintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_iot_namecodeexecution_lowintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_iot_namecodeexecution_mediumintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO\n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_namemaninthemiddle)+" VULNERABILIDADES EL NOMBRE INCLUYE MAN IN THE MIDDLE, LAS ESTADÍSTICAS DE IMPACTO DE INTEGRIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_namemaninthemiddle_highintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_iot_namemaninthemiddle_lowintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_iot_namemaninthemiddle_mediumintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO\n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_namesqlinjection)+" VULNERABILIDADES EL NOMBRE INCLUYE SQL INJECTION, LAS ESTADÍSTICAS DE IMPACTO DE INTEGRIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_namesqlinjection_highintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_iot_namesqlinjection_lowintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_iot_namesqlinjection_mediumintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO\n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_namecrosssiterequestforgery)+" VULNERABILIDADES EL NOMBRE INCLUYE CROSS SITE REQUEST FORGERY, LAS ESTADÍSTICAS DE IMPACTO DE INTEGRIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_namecrosssiterequestforgery_highintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_iot_namecrosssiterequestforgery_lowintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_iot_namecrosssiterequestforgery_mediumintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO\n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_namemoduleexecution)+" VULNERABILIDADES EL NOMBRE INCLUYE MODULE EXECUTION, LAS ESTADÍSTICAS DE IMPACTO DE INTEGRIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_namemoduleexecution_highintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_iot_namemoduleexecution_lowintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_iot_namemoduleexecution_mediumintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO\n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_namebufferoverflow)+" VULNERABILIDADES EL NOMBRE INCLUYE BUFFER OVERFLOW, LAS ESTADÍSTICAS DE IMPACTO DE INTEGRIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_namebufferoverflow_highintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_iot_namebufferoverflow_lowintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_iot_namebufferoverflow_mediumintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO\n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_namecommandexecution)+" VULNERABILIDADES EL NOMBRE INCLUYE COMMAND EXECUTION, LAS ESTADÍSTICAS DE IMPACTO DE INTEGRIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_namecommandexecution_highintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_iot_namecommandexecution_lowintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_iot_namecommandexecution_mediumintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO\n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_namespoofing)+" VULNERABILIDADES EL NOMBRE INCLUYE SPOOFING, LAS ESTADÍSTICAS DE IMPACTO DE INTEGRIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_namespoofing_highintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_iot_namespoofing_lowintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_iot_namespoofing_mediumintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO\n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_nameclickjacking)+" VULNERABILIDADES EL NOMBRE INCLUYE CLICKJACKING, LAS ESTADÍSTICAS DE IMPACTO DE INTEGRIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_nameclickjacking_highintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_iot_nameclickjacking_lowintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_iot_nameclickjacking_mediumintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO\n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_namehijacking)+" VULNERABILIDADES EL NOMBRE INCLUYE HIJACKING, LAS ESTADÍSTICAS DE IMPACTO DE INTEGRIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_namehijacking_highintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_iot_namehijacking_lowintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_iot_namehijacking_mediumintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO\n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_namefileinclude)+" VULNERABILIDADES EL NOMBRE INCLUYE FILEINCLUDE, LAS ESTADÍSTICAS DE IMPACTO DE INTEGRIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_namefileinclude_highintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_iot_namefileinclude_lowintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_iot_namefileinclude_mediumintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO\n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_namebruteforce)+" VULNERABILIDADES EL NOMBRE INCLUYE BRUTEFORCE, LAS ESTADÍSTICAS DE IMPACTO DE INTEGRIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_namebruteforce_highintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_iot_namebruteforce_lowintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_iot_namebruteforce_mediumintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO\n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_namefileupload)+" VULNERABILIDADES EL NOMBRE INCLUYE FILE UPLOAD, LAS ESTADÍSTICAS DE IMPACTO DE INTEGRIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_namefileupload_highintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_iot_namefileupload_lowintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_iot_namefileupload_mediumintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO\n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_nameheaderinjection)+" VULNERABILIDADES EL NOMBRE INCLUYE HEADER INJECTION, LAS ESTADÍSTICAS DE IMPACTO DE INTEGRIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_nameheaderinjection_highintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_iot_nameheaderinjection_lowintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_iot_nameheaderinjection_mediumintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO\n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_nametampering)+" VULNERABILIDADES EL NOMBRE INCLUYE TAMPERING, LAS ESTADÍSTICAS DE IMPACTO DE INTEGRIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_nametampering_highintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_iot_nametampering_lowintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_iot_nametampering_mediumintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO\n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_nameanother)+" VULNERABILIDADES EL NOMBRE INCLUYE OTRA CADENA, LAS ESTADÍSTICAS DE IMPACTO DE INTEGRIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_nameanother_highintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_iot_nameanother_lowintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_iot_nameanother_mediumintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO\n")
print("\n")





print("**********************************************PORCENTAJE NOMBRE/IMPACTO DE INTEGRIDAD VULNERABILIDADES IBM PARTE IOT**********************************************")
print("\n")                            
print("\n")
print(" DE UN TOTAL DE "+str(count_vulnibm_iot_names)+" VULNERABILIDADES :\n") 
print("\n")
print("   - LOS PORCENTAJES DE VALORES DE NOMBRE SON LOS SIGUIENTES:  \n")
print("      -    EN EL  "+str(float(((count_vulnibm_iot_namepathtraversal*100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE PATH TRAVERSAL, LOS PORCENTAJES DE IMPACTO DE INTEGRIDAD SON LOS SIGUIENTES :  \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namepathtraversal_highintimpact*100)/count_vulnibm_iot_namepathtraversal)))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namepathtraversal_lowintimpact*100)/count_vulnibm_iot_namepathtraversal)))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namepathtraversal_mediumintimpact*100)/count_vulnibm_iot_namepathtraversal)))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO\n")
print("\n")
print("      -    EN EL  "+str(float(((count_vulnibm_iot_namedirectorytraversal*100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE DIRECTORY TRAVERSAL, LOS PORCENTAJES DE IMPACTO DE INTEGRIDAD SON LOS SIGUIENTES :  \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namedirectorytraversal_highintimpact*100)/count_vulnibm_iot_namedirectorytraversal)))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namedirectorytraversal_lowintimpact*100)/count_vulnibm_iot_namedirectorytraversal)))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namedirectorytraversal_mediumintimpact*100)/count_vulnibm_iot_namedirectorytraversal)))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO\n")
print("\n")
print("      -    EN EL  "+str(float(((count_vulnibm_iot_nameprivilegeescalation*100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE PRIVILEGE ESCALATION, LOS PORCENTAJES DE IMPACTO DE INTEGRIDAD SON LOS SIGUIENTES :  \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_nameprivilegeescalation_highintimpact*100)/count_vulnibm_iot_nameprivilegeescalation)))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_nameprivilegeescalation_lowintimpact*100)/count_vulnibm_iot_nameprivilegeescalation)))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_nameprivilegeescalation_mediumintimpact*100)/count_vulnibm_iot_nameprivilegeescalation)))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO\n")
print("\n")
print("      -    EN EL  "+str(float(((count_vulnibm_iot_namecrosssitescripting*100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE CROSS SITE SCRIPTING, LOS PORCENTAJES DE IMPACTO DE INTEGRIDAD SON LOS SIGUIENTES :  \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namecrosssitescripting_highintimpact*100)/count_vulnibm_iot_namecrosssitescripting)))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namecrosssitescripting_lowintimpact*100)/count_vulnibm_iot_namecrosssitescripting)))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namecrosssitescripting_mediumintimpact*100)/count_vulnibm_iot_namecrosssitescripting)))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO\n")
print("\n")
print("      -    EN EL  "+str(float(((count_vulnibm_iot_namesecuritybypass*100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE SECURITY BYPASS, LOS PORCENTAJES DE IMPACTO DE INTEGRIDAD SON LOS SIGUIENTES :  \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namesecuritybypass_highintimpact*100)/count_vulnibm_iot_namesecuritybypass)))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namesecuritybypass_lowintimpact*100)/count_vulnibm_iot_namesecuritybypass)))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namesecuritybypass_mediumintimpact*100)/count_vulnibm_iot_namesecuritybypass)))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO\n")
print("\n")
print("      -    EN EL  "+str(float(((count_vulnibm_iot_nameinformationdisclosure*100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE INFORMATION DISCLOSURE, LOS PORCENTAJES DE IMPACTO DE INTEGRIDAD SON LOS SIGUIENTES :  \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_nameinformationdisclosure_highintimpact*100)/count_vulnibm_iot_nameinformationdisclosure)))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_nameinformationdisclosure_lowintimpact*100)/count_vulnibm_iot_nameinformationdisclosure)))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_nameinformationdisclosure_mediumintimpact*100)/count_vulnibm_iot_nameinformationdisclosure)))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO\n")
print("\n")
print("      -    EN EL  "+str(float(((count_vulnibm_iot_namedenialofservice*100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE DENIAL OF SERVICE, LOS PORCENTAJES DE IMPACTO DE INTEGRIDAD SON LOS SIGUIENTES :  \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namedenialofservice_highintimpact*100)/count_vulnibm_iot_namedenialofservice)))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namedenialofservice_lowintimpact*100)/count_vulnibm_iot_namedenialofservice)))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namedenialofservice_mediumintimpact*100)/count_vulnibm_iot_namedenialofservice)))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO\n")
print("\n")
print("      -    EN EL  "+str(float(((count_vulnibm_iot_namecodeexecution*100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE CODE EXECUTION, LOS PORCENTAJES DE IMPACTO DE INTEGRIDAD SON LOS SIGUIENTES :  \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namecodeexecution_highintimpact*100)/count_vulnibm_iot_namecodeexecution)))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namecodeexecution_lowintimpact*100)/count_vulnibm_iot_namecodeexecution)))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namecodeexecution_mediumintimpact*100)/count_vulnibm_iot_namecodeexecution)))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO\n")
print("\n")
print("      -    EN EL  "+str(float(((count_vulnibm_iot_namemaninthemiddle*100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE MAN IN THE MIDDLE, LOS PORCENTAJES DE IMPACTO DE INTEGRIDAD SON LOS SIGUIENTES :  \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namemaninthemiddle_highintimpact*100)/count_vulnibm_iot_namemaninthemiddle)))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namemaninthemiddle_lowintimpact*100)/count_vulnibm_iot_namemaninthemiddle)))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namemaninthemiddle_mediumintimpact*100)/count_vulnibm_iot_namemaninthemiddle)))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO\n")
print("\n")
print("      -    EN EL  "+str(float(((count_vulnibm_iot_namesqlinjection*100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE SQL INJECTION, LOS PORCENTAJES DE IMPACTO DE INTEGRIDAD SON LOS SIGUIENTES :  \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namesqlinjection_highintimpact*100)/count_vulnibm_iot_namesqlinjection)))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namesqlinjection_lowintimpact*100)/count_vulnibm_iot_namesqlinjection)))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namesqlinjection_mediumintimpact*100)/count_vulnibm_iot_namesqlinjection)))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO\n")
print("\n")
print("      -    EN EL  "+str(float(((count_vulnibm_iot_namecrosssiterequestforgery*100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE CROSS SITE REQUEST FORGERY, LOS PORCENTAJES DE IMPACTO DE INTEGRIDAD SON LOS SIGUIENTES :  \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namecrosssiterequestforgery_highintimpact*100)/count_vulnibm_iot_namecrosssiterequestforgery)))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namecrosssiterequestforgery_lowintimpact*100)/count_vulnibm_iot_namecrosssiterequestforgery)))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namecrosssiterequestforgery_mediumintimpact*100)/count_vulnibm_iot_namecrosssiterequestforgery)))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO\n")
print("\n")
print("      -    EN EL  "+str(float(((count_vulnibm_iot_namemoduleexecution*100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE MODULE EXECUTION, LOS PORCENTAJES DE IMPACTO DE INTEGRIDAD SON LOS SIGUIENTES :  \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namemoduleexecution_highintimpact*100)/count_vulnibm_iot_namemoduleexecution)))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namemoduleexecution_lowintimpact*100)/count_vulnibm_iot_namemoduleexecution)))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namemoduleexecution_mediumintimpact*100)/count_vulnibm_iot_namemoduleexecution)))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO\n")
print("\n")
print("      -    EN EL  "+str(float(((count_vulnibm_iot_namebufferoverflow*100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE BUFFER OVERFLOW, LOS PORCENTAJES DE IMPACTO DE INTEGRIDAD SON LOS SIGUIENTES :  \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namebufferoverflow_highintimpact*100)/count_vulnibm_iot_namebufferoverflow)))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namebufferoverflow_lowintimpact*100)/count_vulnibm_iot_namebufferoverflow)))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namebufferoverflow_mediumintimpact*100)/count_vulnibm_iot_namebufferoverflow)))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO\n")
print("\n")
print("      -    EN EL  "+str(float(((count_vulnibm_iot_namecommandexecution*100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE COMMAND EXECUTION, LOS PORCENTAJES DE IMPACTO DE INTEGRIDAD SON LOS SIGUIENTES :  \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namecommandexecution_highintimpact*100)/count_vulnibm_iot_namecommandexecution)))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namecommandexecution_lowintimpact*100)/count_vulnibm_iot_namecommandexecution)))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namecommandexecution_mediumintimpact*100)/count_vulnibm_iot_namecommandexecution)))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO\n")
print("\n")
print("      -    EN EL  "+str(float(((count_vulnibm_iot_namespoofing*100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE SPOOFING, LOS PORCENTAJES DE IMPACTO DE INTEGRIDAD SON LOS SIGUIENTES :  \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namespoofing_highintimpact*100)/count_vulnibm_iot_namespoofing)))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namespoofing_lowintimpact*100)/count_vulnibm_iot_namespoofing)))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namespoofing_mediumintimpact*100)/count_vulnibm_iot_namespoofing)))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO\n")
print("\n")
print("      -    EN EL  "+str(float(((count_vulnibm_iot_nameclickjacking*100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE CLICKJACKING, LOS PORCENTAJES DE IMPACTO DE INTEGRIDAD SON LOS SIGUIENTES :  \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_nameclickjacking_highintimpact*100)/count_vulnibm_iot_nameclickjacking)))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_nameclickjacking_lowintimpact*100)/count_vulnibm_iot_nameclickjacking)))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_nameclickjacking_mediumintimpact*100)/count_vulnibm_iot_nameclickjacking)))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO\n")
print("\n")
print("      -    EN EL  "+str(float(((count_vulnibm_iot_namehijacking*100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE HIJACKING, LOS PORCENTAJES DE IMPACTO DE INTEGRIDAD SON LOS SIGUIENTES :  \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namehijacking_highintimpact*100)/count_vulnibm_iot_namehijacking)))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namehijacking_lowintimpact*100)/count_vulnibm_iot_namehijacking)))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namehijacking_mediumintimpact*100)/count_vulnibm_iot_namehijacking)))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO\n")
print("\n")
print("      -    EN EL  "+str(float(((count_vulnibm_iot_namefileinclude*100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE FILEINCLUDE, LOS PORCENTAJES DE IMPACTO DE INTEGRIDAD SON LOS SIGUIENTES :  \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namefileinclude_highintimpact*100)/count_vulnibm_iot_namefileinclude)))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namefileinclude_lowintimpact*100)/count_vulnibm_iot_namefileinclude)))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namefileinclude_mediumintimpact*100)/count_vulnibm_iot_namefileinclude)))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO\n")
print("\n")
print("      -    EN EL  "+str(float(((count_vulnibm_iot_namebruteforce*100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE BRUTEFORCE, LOS PORCENTAJES DE IMPACTO DE INTEGRIDAD SON LOS SIGUIENTES :  \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namebruteforce_highintimpact*100)/count_vulnibm_iot_namebruteforce)))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namebruteforce_lowintimpact*100)/count_vulnibm_iot_namebruteforce)))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namebruteforce_mediumintimpact*100)/count_vulnibm_iot_namebruteforce)))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO\n")
print("\n")
print("      -    EN EL  "+str(float(((count_vulnibm_iot_namefileupload*100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE FILE UPLOAD, LOS PORCENTAJES DE IMPACTO DE INTEGRIDAD SON LOS SIGUIENTES :  \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namefileupload_highintimpact*100)/count_vulnibm_iot_namefileupload)))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namefileupload_lowintimpact*100)/count_vulnibm_iot_namefileupload)))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namefileupload_mediumintimpact*100)/count_vulnibm_iot_namefileupload)))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO\n")
print("\n")
if(count_vulnibm_iot_nameheaderinjection>0):
    print("      -    EN EL  "+str(float(((count_vulnibm_iot_nameheaderinjection*100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE HEADER INJECTION, LOS PORCENTAJES DE IMPACTO DE INTEGRIDAD SON LOS SIGUIENTES :  \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_nameheaderinjection_highintimpact*100)/count_vulnibm_iot_nameheaderinjection)))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_nameheaderinjection_lowintimpact*100)/count_vulnibm_iot_nameheaderinjection)))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_nameheaderinjection_mediumintimpact*100)/count_vulnibm_iot_nameheaderinjection)))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO\n")
    print("\n")
if(count_vulnibm_iot_nametampering>0):
    print("      -    EN EL  "+str(float(((count_vulnibm_iot_nametampering*100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE TAMPERING, LOS PORCENTAJES DE IMPACTO DE INTEGRIDAD SON LOS SIGUIENTES :  \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_nametampering_highintimpact*100)/count_vulnibm_iot_nametampering)))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_nametampering_lowintimpact*100)/count_vulnibm_iot_nametampering)))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_nametampering_mediumintimpact*100)/count_vulnibm_iot_nametampering)))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO\n")
    print("\n")
    print("      -    EN EL  "+str(float(((count_vulnibm_iot_nameanother*100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE OTRA CADENA, LOS PORCENTAJES DE IMPACTO DE INTEGRIDAD SON LOS SIGUIENTES :  \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_nameanother_highintimpact*100)/count_vulnibm_iot_nameanother)))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_nameanother_lowintimpact*100)/count_vulnibm_iot_nameanother)))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_nameanother_mediumintimpact*100)/count_vulnibm_iot_nameanother)))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO\n")
    print("\n")




    
    
    




#Abro los ficheros con los que voy a tratar




df_vulnibm_sh = pd.read_excel('vulnerabilidades_ibm_smart_home_2023.xlsx')

#Variable para almacenar el contador total de valores de nombre
count_vulnibm_sh_names=0
#Variable para almacenar el contador total de valores de un nombre concreto
count_vulnibm_sh_namepathtraversal=0
#Variables para almacenar el contador de valores de impacto de INTEGRIDAD dato un valor de nombre especifico
count_vulnibm_sh_namepathtraversal_intimpact=0
count_vulnibm_sh_namepathtraversal_highintimpact=0
count_vulnibm_sh_namepathtraversal_lowintimpact=0
count_vulnibm_sh_namepathtraversal_mediumintimpact=0

count_vulnibm_sh_namedirectorytraversal=0
count_vulnibm_sh_namedirectorytraversal_intimpact=0
count_vulnibm_sh_namedirectorytraversal_highintimpact=0
count_vulnibm_sh_namedirectorytraversal_lowintimpact=0
count_vulnibm_sh_namedirectorytraversal_mediumintimpact=0

count_vulnibm_sh_nameprivilegeescalation=0
count_vulnibm_sh_nameprivilegeescalation_intimpact=0
count_vulnibm_sh_nameprivilegeescalation_highintimpact=0
count_vulnibm_sh_nameprivilegeescalation_lowintimpact=0
count_vulnibm_sh_nameprivilegeescalation_mediumintimpact=0

count_vulnibm_sh_namecrosssitescripting=0
count_vulnibm_sh_namecrosssitescripting_intimpact=0
count_vulnibm_sh_namecrosssitescripting_highintimpact=0
count_vulnibm_sh_namecrosssitescripting_lowintimpact=0
count_vulnibm_sh_namecrosssitescripting_mediumintimpact=0

count_vulnibm_sh_namesecuritybypass=0
count_vulnibm_sh_namesecuritybypass_intimpact=0
count_vulnibm_sh_namesecuritybypass_highintimpact=0
count_vulnibm_sh_namesecuritybypass_lowintimpact=0
count_vulnibm_sh_namesecuritybypass_mediumintimpact=0

count_vulnibm_sh_nameinformationdisclosure=0
count_vulnibm_sh_nameinformationdisclosure_intimpact=0
count_vulnibm_sh_nameinformationdisclosure_highintimpact=0
count_vulnibm_sh_nameinformationdisclosure_lowintimpact=0
count_vulnibm_sh_nameinformationdisclosure_mediumintimpact=0

count_vulnibm_sh_namedenialofservice=0
count_vulnibm_sh_namedenialofservice_intimpact=0
count_vulnibm_sh_namedenialofservice_highintimpact=0
count_vulnibm_sh_namedenialofservice_lowintimpact=0
count_vulnibm_sh_namedenialofservice_mediumintimpact=0

count_vulnibm_sh_namecodeexecution=0
count_vulnibm_sh_namecodeexecution_intimpact=0
count_vulnibm_sh_namecodeexecution_highintimpact=0
count_vulnibm_sh_namecodeexecution_lowintimpact=0
count_vulnibm_sh_namecodeexecution_mediumintimpact=0

count_vulnibm_sh_namemaninthemiddle=0
count_vulnibm_sh_namemaninthemiddle_intimpact=0
count_vulnibm_sh_namemaninthemiddle_highintimpact=0
count_vulnibm_sh_namemaninthemiddle_lowintimpact=0
count_vulnibm_sh_namemaninthemiddle_mediumintimpact=0

count_vulnibm_sh_namesqlinjection=0
count_vulnibm_sh_namesqlinjection_intimpact=0
count_vulnibm_sh_namesqlinjection_highintimpact=0
count_vulnibm_sh_namesqlinjection_lowintimpact=0
count_vulnibm_sh_namesqlinjection_mediumintimpact=0

count_vulnibm_sh_namecrosssiterequestforgery=0
count_vulnibm_sh_namecrosssiterequestforgery_intimpact=0
count_vulnibm_sh_namecrosssiterequestforgery_highintimpact=0
count_vulnibm_sh_namecrosssiterequestforgery_lowintimpact=0
count_vulnibm_sh_namecrosssiterequestforgery_mediumintimpact=0

count_vulnibm_sh_namemoduleexecution=0
count_vulnibm_sh_namemoduleexecution_intimpact=0
count_vulnibm_sh_namemoduleexecution_highintimpact=0
count_vulnibm_sh_namemoduleexecution_lowintimpact=0
count_vulnibm_sh_namemoduleexecution_mediumintimpact=0

count_vulnibm_sh_namebufferoverflow=0
count_vulnibm_sh_namebufferoverflow_intimpact=0
count_vulnibm_sh_namebufferoverflow_highintimpact=0
count_vulnibm_sh_namebufferoverflow_lowintimpact=0
count_vulnibm_sh_namebufferoverflow_mediumintimpact=0

count_vulnibm_sh_namecommandexecution=0
count_vulnibm_sh_namecommandexecution_intimpact=0
count_vulnibm_sh_namecommandexecution_highintimpact=0
count_vulnibm_sh_namecommandexecution_lowintimpact=0
count_vulnibm_sh_namecommandexecution_mediumintimpact=0

count_vulnibm_sh_namespoofing=0
count_vulnibm_sh_namespoofing_intimpact=0
count_vulnibm_sh_namespoofing_highintimpact=0
count_vulnibm_sh_namespoofing_lowintimpact=0
count_vulnibm_sh_namespoofing_mediumintimpact=0

count_vulnibm_sh_nameclickjacking=0
count_vulnibm_sh_nameclickjacking_intimpact=0
count_vulnibm_sh_nameclickjacking_highintimpact=0
count_vulnibm_sh_nameclickjacking_lowintimpact=0
count_vulnibm_sh_nameclickjacking_mediumintimpact=0

count_vulnibm_sh_namehijacking=0
count_vulnibm_sh_namehijacking_intimpact=0
count_vulnibm_sh_namehijacking_highintimpact=0
count_vulnibm_sh_namehijacking_lowintimpact=0
count_vulnibm_sh_namehijacking_mediumintimpact=0

count_vulnibm_sh_namefileinclude=0
count_vulnibm_sh_namefileinclude_intimpact=0
count_vulnibm_sh_namefileinclude_highintimpact=0
count_vulnibm_sh_namefileinclude_lowintimpact=0
count_vulnibm_sh_namefileinclude_mediumintimpact=0

count_vulnibm_sh_namebruteforce=0
count_vulnibm_sh_namebruteforce_intimpact=0
count_vulnibm_sh_namebruteforce_highintimpact=0
count_vulnibm_sh_namebruteforce_lowintimpact=0
count_vulnibm_sh_namebruteforce_mediumintimpact=0

count_vulnibm_sh_namefileupload=0
count_vulnibm_sh_namefileupload_intimpact=0
count_vulnibm_sh_namefileupload_highintimpact=0
count_vulnibm_sh_namefileupload_lowintimpact=0
count_vulnibm_sh_namefileupload_mediumintimpact=0

count_vulnibm_sh_nameheaderinjection=0
count_vulnibm_sh_nameheaderinjection_intimpact=0
count_vulnibm_sh_nameheaderinjection_highintimpact=0
count_vulnibm_sh_nameheaderinjection_lowintimpact=0
count_vulnibm_sh_nameheaderinjection_mediumintimpact=0

count_vulnibm_sh_nametampering=0
count_vulnibm_sh_nametampering_intimpact=0
count_vulnibm_sh_nametampering_highintimpact=0
count_vulnibm_sh_nametampering_lowintimpact=0
count_vulnibm_sh_nametampering_mediumintimpact=0

count_vulnibm_sh_nameanother=0
count_vulnibm_sh_nameanother_intimpact=0
count_vulnibm_sh_nameanother_highintimpact=0
count_vulnibm_sh_nameanother_lowintimpact=0
count_vulnibm_sh_nameanother_mediumintimpact=0

#Comprobamos el contenido de name
for r in range(0,len(df_vulnibm_sh["name"])):                       
    aux_str=df_vulnibm_sh["name"][r].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
    if(aux_str!='NONE'):
        count_vulnibm_sh_names+=1
        #Compruebo el valor de nombre
        if('pathtraversal' in aux_str):
            count_vulnibm_sh_namepathtraversal+=1
            #Compruebo el valor de impacto de INTEGRIDAD
            if(df_vulnibm_sh["x_xfe_cvss_integrity_impact"][r]=='High'):
                count_vulnibm_sh_namepathtraversal_intimpact+=1
                count_vulnibm_sh_namepathtraversal_highintimpact+=1
            elif(df_vulnibm_sh["x_xfe_cvss_integrity_impact"][r]=='Low'):
                count_vulnibm_sh_namepathtraversal_intimpact+=1
                count_vulnibm_sh_namepathtraversal_lowintimpact+=1
            elif(df_vulnibm_sh["x_xfe_cvss_integrity_impact"][r]=='Medium'):
                count_vulnibm_sh_namepathtraversal_intimpact+=1
                count_vulnibm_sh_namepathtraversal_mediumintimpact+=1
    
        elif('directorytraversal' in aux_str):
            
            count_vulnibm_sh_namedirectorytraversal+=1
            if(df_vulnibm_sh["x_xfe_cvss_integrity_impact"][r]=='High'):
                count_vulnibm_sh_namedirectorytraversal_intimpact+=1
                count_vulnibm_sh_namedirectorytraversal_highintimpact+=1
            elif(df_vulnibm_sh["x_xfe_cvss_integrity_impact"][r]=='Low'):
                count_vulnibm_sh_namedirectorytraversal_intimpact+=1
                count_vulnibm_sh_namedirectorytraversal_lowintimpact+=1
            elif(df_vulnibm_sh["x_xfe_cvss_integrity_impact"][r]=='Medium'):
                count_vulnibm_sh_namedirectorytraversal_intimpact+=1
                count_vulnibm_sh_namedirectorytraversal_mediumintimpact+=1
            
            
        elif('privilegeescalation' in aux_str):
        
            count_vulnibm_sh_nameprivilegeescalation+=1
            if(df_vulnibm_sh["x_xfe_cvss_integrity_impact"][r]=='High'):
                count_vulnibm_sh_nameprivilegeescalation_intimpact+=1
                count_vulnibm_sh_nameprivilegeescalation_highintimpact+=1
            elif(df_vulnibm_sh["x_xfe_cvss_integrity_impact"][r]=='Low'):
                count_vulnibm_sh_nameprivilegeescalation_intimpact+=1
                count_vulnibm_sh_nameprivilegeescalation_lowintimpact+=1
            elif(df_vulnibm_sh["x_xfe_cvss_integrity_impact"][r]=='Medium'):
                count_vulnibm_sh_nameprivilegeescalation_intimpact+=1
                count_vulnibm_sh_nameprivilegeescalation_mediumintimpact+=1
            
        elif('cross-sitescripting' in aux_str):
        
            count_vulnibm_sh_namecrosssitescripting+=1
            if(df_vulnibm_sh["x_xfe_cvss_integrity_impact"][r]=='High'):
                count_vulnibm_sh_namecrosssitescripting_intimpact+=1
                count_vulnibm_sh_namecrosssitescripting_highintimpact+=1
            elif(df_vulnibm_sh["x_xfe_cvss_integrity_impact"][r]=='Low'):
                count_vulnibm_sh_namecrosssitescripting_intimpact+=1
                count_vulnibm_sh_namecrosssitescripting_lowintimpact+=1
            elif(df_vulnibm_sh["x_xfe_cvss_integrity_impact"][r]=='Medium'):
                count_vulnibm_sh_namecrosssitescripting_intimpact+=1
                count_vulnibm_sh_namecrosssitescripting_mediumintimpact+=1
                                         
        elif('securitybypass' in aux_str):
        
            count_vulnibm_sh_namesecuritybypass+=1
            if(df_vulnibm_sh["x_xfe_cvss_integrity_impact"][r]=='High'):
                count_vulnibm_sh_namesecuritybypass_intimpact+=1
                count_vulnibm_sh_namesecuritybypass_highintimpact+=1
            elif(df_vulnibm_sh["x_xfe_cvss_integrity_impact"][r]=='Low'):
                count_vulnibm_sh_namesecuritybypass_intimpact+=1
                count_vulnibm_sh_namesecuritybypass_lowintimpact+=1
            elif(df_vulnibm_sh["x_xfe_cvss_integrity_impact"][r]=='Medium'):
                count_vulnibm_sh_namesecuritybypass_intimpact+=1
                count_vulnibm_sh_namesecuritybypass_mediumintimpact+=1
                                         
        elif('information_disclosure' in aux_str or 'informationdisclosure' in aux_str):
        
            count_vulnibm_sh_nameinformationdisclosure+=1
            if(df_vulnibm_sh["x_xfe_cvss_integrity_impact"][r]=='High'):
                count_vulnibm_sh_nameinformationdisclosure_intimpact+=1
                count_vulnibm_sh_nameinformationdisclosure_highintimpact+=1
            elif(df_vulnibm_sh["x_xfe_cvss_integrity_impact"][r]=='Low'):
                count_vulnibm_sh_nameinformationdisclosure_intimpact+=1
                count_vulnibm_sh_nameinformationdisclosure_lowintimpact+=1
            elif(df_vulnibm_sh["x_xfe_cvss_integrity_impact"][r]=='Medium'):
                count_vulnibm_sh_nameinformationdisclosure_intimpact+=1
                count_vulnibm_sh_nameinformationdisclosure_mediumintimpact+=1
                                         
        elif('denialofservice' in aux_str):
            
            count_vulnibm_sh_namedenialofservice+=1
            if(df_vulnibm_sh["x_xfe_cvss_integrity_impact"][r]=='High'):
                count_vulnibm_sh_namedenialofservice_intimpact+=1
                count_vulnibm_sh_namedenialofservice_highintimpact+=1
            elif(df_vulnibm_sh["x_xfe_cvss_integrity_impact"][r]=='Low'):
                count_vulnibm_sh_namedenialofservice_intimpact+=1
                count_vulnibm_sh_namedenialofservice_lowintimpact+=1
            elif(df_vulnibm_sh["x_xfe_cvss_integrity_impact"][r]=='Medium'):
                count_vulnibm_sh_namedenialofservice_intimpact+=1
                count_vulnibm_sh_namedenialofservice_mediumintimpact+=1
            
        elif('codeexecution' in aux_str):
        
        
            count_vulnibm_sh_namecodeexecution+=1
            if(df_vulnibm_sh["x_xfe_cvss_integrity_impact"][r]=='High'):
                count_vulnibm_sh_namecodeexecution_intimpact+=1
                count_vulnibm_sh_namecodeexecution_highintimpact+=1
            elif(df_vulnibm_sh["x_xfe_cvss_integrity_impact"][r]=='Low'):
                count_vulnibm_sh_namecodeexecution_intimpact+=1
                count_vulnibm_sh_namecodeexecution_lowintimpact+=1
            elif(df_vulnibm_sh["x_xfe_cvss_integrity_impact"][r]=='Medium'):
                count_vulnibm_sh_namecodeexecution_intimpact+=1
                count_vulnibm_sh_namecodeexecution_mediumintimpact+=1
                                         
        elif('maninthemiddle' in aux_str):
        
            count_vulnibm_sh_namemaninthemiddle+=1
            if(df_vulnibm_sh["x_xfe_cvss_integrity_impact"][r]=='High'):
                count_vulnibm_sh_namemaninthemiddle_intimpact+=1
                count_vulnibm_sh_namemaninthemiddle_highintimpact+=1
            elif(df_vulnibm_sh["x_xfe_cvss_integrity_impact"][r]=='Low'):
                count_vulnibm_sh_namemaninthemiddle_intimpact+=1
                count_vulnibm_sh_namemaninthemiddle_lowintimpact+=1
            elif(df_vulnibm_sh["x_xfe_cvss_integrity_impact"][r]=='Medium'):
                count_vulnibm_sh_namemaninthemiddle_intimpact+=1
                count_vulnibm_sh_namemaninthemiddle_mediumintimpact+=1
                                         
        elif('SQLinjection' in aux_str):
        
            count_vulnibm_sh_namesqlinjection+=1
            if(df_vulnibm_sh["x_xfe_cvss_integrity_impact"][r]=='High'):
                count_vulnibm_sh_namesqlinjection_intimpact+=1
                count_vulnibm_sh_namesqlinjection_highintimpact+=1
            elif(df_vulnibm_sh["x_xfe_cvss_integrity_impact"][r]=='Low'):
                count_vulnibm_sh_namesqlinjection_intimpact+=1
                count_vulnibm_sh_namesqlinjection_lowintimpact+=1
            elif(df_vulnibm_sh["x_xfe_cvss_integrity_impact"][r]=='Medium'):
                count_vulnibm_sh_namesqlinjection_intimpact+=1
                count_vulnibm_sh_namesqlinjection_mediumintimpact+=1
                                         
        elif('cross-siterequestforgery' in aux_str):
        
            count_vulnibm_sh_namecrosssiterequestforgery+=1
            if(df_vulnibm_sh["x_xfe_cvss_integrity_impact"][r]=='High'):
                count_vulnibm_sh_namecrosssiterequestforgery_intimpact+=1
                count_vulnibm_sh_namecrosssiterequestforgery_highintimpact+=1
            elif(df_vulnibm_sh["x_xfe_cvss_integrity_impact"][r]=='Low'):
                count_vulnibm_sh_namecrosssiterequestforgery_intimpact+=1
                count_vulnibm_sh_namecrosssiterequestforgery_lowintimpact+=1
            elif(df_vulnibm_sh["x_xfe_cvss_integrity_impact"][r]=='Medium'):
                count_vulnibm_sh_namecrosssiterequestforgery_intimpact+=1
                count_vulnibm_sh_namecrosssiterequestforgery_mediumintimpact+=1
                                         
        elif('moduleexecution' in aux_str):
        
            count_vulnibm_sh_namemoduleexecution+=1
            if(df_vulnibm_sh["x_xfe_cvss_integrity_impact"][r]=='High'):
                count_vulnibm_sh_namemoduleexecution_intimpact+=1
                count_vulnibm_sh_namemoduleexecution_highintimpact+=1
            elif(df_vulnibm_sh["x_xfe_cvss_integrity_impact"][r]=='Low'):
                count_vulnibm_sh_namemoduleexecution_intimpact+=1
                count_vulnibm_sh_namemoduleexecution_lowintimpact+=1
            elif(df_vulnibm_sh["x_xfe_cvss_integrity_impact"][r]=='Medium'):
                count_vulnibm_sh_namemoduleexecution_intimpact+=1
                count_vulnibm_sh_namemoduleexecution_mediumintimpact+=1
                                         
        elif('bufferoverflow' in aux_str):
        
            count_vulnibm_sh_namebufferoverflow+=1
            if(df_vulnibm_sh["x_xfe_cvss_integrity_impact"][r]=='High'):
                count_vulnibm_sh_namebufferoverflow_intimpact+=1
                count_vulnibm_sh_namebufferoverflow_highintimpact+=1
            elif(df_vulnibm_sh["x_xfe_cvss_integrity_impact"][r]=='Low'):
                count_vulnibm_sh_namebufferoverflow_intimpact+=1
                count_vulnibm_sh_namebufferoverflow_lowintimpact+=1
            elif(df_vulnibm_sh["x_xfe_cvss_integrity_impact"][r]=='Medium'):
                count_vulnibm_sh_namebufferoverflow_intimpact+=1
                count_vulnibm_sh_namebufferoverflow_mediumintimpact+=1
                                         
        elif('commandexecution' in aux_str):
        
            count_vulnibm_sh_namecommandexecution+=1
            if(df_vulnibm_sh["x_xfe_cvss_integrity_impact"][r]=='High'):
                count_vulnibm_sh_namecommandexecution_intimpact+=1
                count_vulnibm_sh_namecommandexecution_highintimpact+=1
            elif(df_vulnibm_sh["x_xfe_cvss_integrity_impact"][r]=='Low'):
                count_vulnibm_sh_namecommandexecution_intimpact+=1
                count_vulnibm_sh_namecommandexecution_lowintimpact+=1
            elif(df_vulnibm_sh["x_xfe_cvss_integrity_impact"][r]=='Medium'):
                count_vulnibm_sh_namecommandexecution_intimpact+=1
                count_vulnibm_sh_namecommandexecution_mediumintimpact+=1
                                         
        elif('spoofing' in aux_str):
        
            count_vulnibm_sh_namespoofing+=1
            if(df_vulnibm_sh["x_xfe_cvss_integrity_impact"][r]=='High'):
                count_vulnibm_sh_namespoofing_intimpact+=1
                count_vulnibm_sh_namespoofing_highintimpact+=1
            elif(df_vulnibm_sh["x_xfe_cvss_integrity_impact"][r]=='Low'):
                count_vulnibm_sh_namespoofing_intimpact+=1
                count_vulnibm_sh_namespoofing_lowintimpact+=1
            elif(df_vulnibm_sh["x_xfe_cvss_integrity_impact"][r]=='Medium'):
                count_vulnibm_sh_namespoofing_intimpact+=1
                count_vulnibm_sh_namespoofing_mediumintimpact+=1
                                         
        elif('clickjacking' in aux_str):
        
            count_vulnibm_sh_nameclickjacking+=1
            if(df_vulnibm_sh["x_xfe_cvss_integrity_impact"][r]=='High'):
                count_vulnibm_sh_nameclickjacking_intimpact+=1
                count_vulnibm_sh_nameclickjacking_highintimpact+=1
            elif(df_vulnibm_sh["x_xfe_cvss_integrity_impact"][r]=='Low'):
                count_vulnibm_sh_nameclickjacking_intimpact+=1
                count_vulnibm_sh_nameclickjacking_lowintimpact+=1
            elif(df_vulnibm_sh["x_xfe_cvss_integrity_impact"][r]=='Medium'):
                count_vulnibm_sh_nameclickjacking_intimpact+=1
                count_vulnibm_sh_nameclickjacking_mediumintimpact+=1
              
        elif('hijacking' in aux_str):
        
            count_vulnibm_sh_namehijacking+=1
            if(df_vulnibm_sh["x_xfe_cvss_integrity_impact"][r]=='High'):
                count_vulnibm_sh_namehijacking_intimpact+=1
                count_vulnibm_sh_namehijacking_highintimpact+=1
            elif(df_vulnibm_sh["x_xfe_cvss_integrity_impact"][r]=='Low'):
                count_vulnibm_sh_namehijacking_intimpact+=1
                count_vulnibm_sh_namehijacking_lowintimpact+=1
            elif(df_vulnibm_sh["x_xfe_cvss_integrity_impact"][r]=='Medium'):
                count_vulnibm_sh_namehijacking_intimpact+=1
                count_vulnibm_sh_namehijacking_mediumintimpact+=1
               
        elif('fileinclude' in aux_str):
        
            count_vulnibm_sh_namefileinclude+=1
            if(df_vulnibm_sh["x_xfe_cvss_integrity_impact"][r]=='High'):
                count_vulnibm_sh_namefileinclude_intimpact+=1
                count_vulnibm_sh_namefileinclude_highintimpact+=1
            elif(df_vulnibm_sh["x_xfe_cvss_integrity_impact"][r]=='Low'):
                count_vulnibm_sh_namefileinclude_intimpact+=1
                count_vulnibm_sh_namefileinclude_lowintimpact+=1
            elif(df_vulnibm_sh["x_xfe_cvss_integrity_impact"][r]=='Medium'):
                count_vulnibm_sh_namefileinclude_intimpact+=1
                count_vulnibm_sh_namefileinclude_mediumintimpact+=1
                
               
        elif('bruteforce' in aux_str):
        
            count_vulnibm_sh_namebruteforce+=1
            if(df_vulnibm_sh["x_xfe_cvss_integrity_impact"][r]=='High'):
                count_vulnibm_sh_namebruteforce_intimpact+=1
                count_vulnibm_sh_namebruteforce_highintimpact+=1
            elif(df_vulnibm_sh["x_xfe_cvss_integrity_impact"][r]=='Low'):
                count_vulnibm_sh_namebruteforce_intimpact+=1
                count_vulnibm_sh_namebruteforce_lowintimpact+=1
            elif(df_vulnibm_sh["x_xfe_cvss_integrity_impact"][r]=='Medium'):
                count_vulnibm_sh_namebruteforce_intimpact+=1
                count_vulnibm_sh_namebruteforce_mediumintimpact+=1
                
               
        elif('fileupload' in aux_str):
        
            count_vulnibm_sh_namefileupload+=1
            if(df_vulnibm_sh["x_xfe_cvss_integrity_impact"][r]=='High'):
                count_vulnibm_sh_namefileupload_intimpact+=1
                count_vulnibm_sh_namefileupload_highintimpact+=1
            elif(df_vulnibm_sh["x_xfe_cvss_integrity_impact"][r]=='Low'):
                count_vulnibm_sh_namefileupload_intimpact+=1
                count_vulnibm_sh_namefileupload_lowintimpact+=1
            elif(df_vulnibm_sh["x_xfe_cvss_integrity_impact"][r]=='Medium'):
                count_vulnibm_sh_namefileupload_intimpact+=1
                count_vulnibm_sh_namefileupload_mediumintimpact+=1
                
               
        elif('headerinjection' in aux_str):
        
            count_vulnibm_sh_nameheaderinjection+=1
            if(df_vulnibm_sh["x_xfe_cvss_integrity_impact"][r]=='High'):
                count_vulnibm_sh_nameheaderinjection_intimpact+=1
                count_vulnibm_sh_nameheaderinjection_highintimpact+=1
            elif(df_vulnibm_sh["x_xfe_cvss_integrity_impact"][r]=='Low'):
                count_vulnibm_sh_nameheaderinjection_intimpact+=1
                count_vulnibm_sh_nameheaderinjection_lowintimpact+=1
            elif(df_vulnibm_sh["x_xfe_cvss_integrity_impact"][r]=='Medium'):
                count_vulnibm_sh_nameheaderinjection_intimpact+=1
                count_vulnibm_sh_nameheaderinjection_mediumintimpact+=1
               
        elif('Tampering' in aux_str):
        
            count_vulnibm_sh_nametampering+=1
            if(df_vulnibm_sh["x_xfe_cvss_integrity_impact"][r]=='High'):
                count_vulnibm_sh_nametampering_intimpact+=1
                count_vulnibm_sh_nametampering_highintimpact+=1
            elif(df_vulnibm_sh["x_xfe_cvss_integrity_impact"][r]=='Low'):
                count_vulnibm_sh_nametampering_intimpact+=1
                count_vulnibm_sh_nametampering_lowintimpact+=1
            elif(df_vulnibm_sh["x_xfe_cvss_integrity_impact"][r]=='Medium'):
                count_vulnibm_sh_nametampering_intimpact+=1
                count_vulnibm_sh_nametampering_mediumintimpact+=1
    
        else:
        
            count_vulnibm_sh_nameanother+=1
            if(df_vulnibm_sh["x_xfe_cvss_integrity_impact"][r]=='High'):
                count_vulnibm_sh_nameanother_intimpact+=1
                count_vulnibm_sh_nameanother_highintimpact+=1
            elif(df_vulnibm_sh["x_xfe_cvss_integrity_impact"][r]=='Low'):
                count_vulnibm_sh_nameanother_intimpact+=1
                count_vulnibm_sh_nameanother_lowintimpact+=1
            elif(df_vulnibm_sh["x_xfe_cvss_integrity_impact"][r]=='Medium'):
                count_vulnibm_sh_nameanother_intimpact+=1
                count_vulnibm_sh_nameanother_mediumintimpact+=1
                
                
                
                
                
print("**********************************************ESTADÍSTICAS NOMBRE/IMPACTO DE INTEGRIDAD VULNERABILIDADES IBM PARTE SMART HOME**********************************************")
print("\n")                            
print("\n")
print(" DE UN TOTAL DE "+str(count_vulnibm_sh_names)+" VULNERABILIDADES:\n") 
print("\n")
print("   - LAS ESTADISTICAS DE VALORES DE NOMBRE SON LAS SIGUIENTES:  \n")
print("      -    EN  "+str(count_vulnibm_sh_namepathtraversal)+" VULNERABILIDADES EL NOMBRE INCLUYE PATH TRAVERSAL, LAS ESTADÍSTICAS DE IMPACTO DE INTEGRIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_sh_namepathtraversal_highintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_sh_namepathtraversal_lowintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_sh_namepathtraversal_mediumintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO\n")
print("\n")
print("      -    EN  "+str(count_vulnibm_sh_namedirectorytraversal)+" VULNERABILIDADES EL NOMBRE INCLUYE DIRECTORY TRAVERSAL, LAS ESTADÍSTICAS DE IMPACTO DE INTEGRIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_sh_namedirectorytraversal_highintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_sh_namedirectorytraversal_lowintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_sh_namedirectorytraversal_mediumintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO\n")
print("\n")
print("      -    EN  "+str(count_vulnibm_sh_nameprivilegeescalation)+" VULNERABILIDADES EL NOMBRE INCLUYE PRIVILEGE ESCALATION, LAS ESTADÍSTICAS DE IMPACTO DE INTEGRIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_sh_nameprivilegeescalation_highintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_sh_nameprivilegeescalation_lowintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_sh_nameprivilegeescalation_mediumintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO\n")
print("\n")
print("      -    EN  "+str(count_vulnibm_sh_namecrosssitescripting)+" VULNERABILIDADES EL NOMBRE INCLUYE CROSS SITE SCRIPTING, LAS ESTADÍSTICAS DE IMPACTO DE INTEGRIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_sh_namecrosssitescripting_highintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_sh_namecrosssitescripting_lowintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_sh_namecrosssitescripting_mediumintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO\n")
print("\n")
print("      -    EN  "+str(count_vulnibm_sh_namesecuritybypass)+" VULNERABILIDADES EL NOMBRE INCLUYE SECURITY BYPASS, LAS ESTADÍSTICAS DE IMPACTO DE INTEGRIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_sh_namesecuritybypass_highintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_sh_namesecuritybypass_lowintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_sh_namesecuritybypass_mediumintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO\n")
print("\n")
print("      -    EN  "+str(count_vulnibm_sh_nameinformationdisclosure)+" VULNERABILIDADES EL NOMBRE INCLUYE INFORMATION DISCLOSURE, LAS ESTADÍSTICAS DE IMPACTO DE INTEGRIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_sh_nameinformationdisclosure_highintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_sh_nameinformationdisclosure_lowintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_sh_nameinformationdisclosure_mediumintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO\n")
print("\n")
print("      -    EN  "+str(count_vulnibm_sh_namedenialofservice)+" VULNERABILIDADES EL NOMBRE INCLUYE DENIAL OF SERVICE, LAS ESTADÍSTICAS DE IMPACTO DE INTEGRIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_sh_namedenialofservice_highintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_sh_namedenialofservice_lowintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_sh_namedenialofservice_mediumintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO\n")
print("\n")
print("      -    EN  "+str(count_vulnibm_sh_namecodeexecution)+" VULNERABILIDADES EL NOMBRE INCLUYE CODE EXECUTION, LAS ESTADÍSTICAS DE IMPACTO DE INTEGRIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_sh_namecodeexecution_highintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_sh_namecodeexecution_lowintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_sh_namecodeexecution_mediumintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO\n")
print("\n")
print("      -    EN  "+str(count_vulnibm_sh_namemaninthemiddle)+" VULNERABILIDADES EL NOMBRE INCLUYE MAN IN THE MIDDLE, LAS ESTADÍSTICAS DE IMPACTO DE INTEGRIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_sh_namemaninthemiddle_highintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_sh_namemaninthemiddle_lowintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_sh_namemaninthemiddle_mediumintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO\n")
print("\n")
print("      -    EN  "+str(count_vulnibm_sh_namesqlinjection)+" VULNERABILIDADES EL NOMBRE INCLUYE SQL INJECTION, LAS ESTADÍSTICAS DE IMPACTO DE INTEGRIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_sh_namesqlinjection_highintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_sh_namesqlinjection_lowintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_sh_namesqlinjection_mediumintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO\n")
print("\n")
print("      -    EN  "+str(count_vulnibm_sh_namecrosssiterequestforgery)+" VULNERABILIDADES EL NOMBRE INCLUYE CROSS SITE REQUEST FORGERY, LAS ESTADÍSTICAS DE IMPACTO DE INTEGRIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_sh_namecrosssiterequestforgery_highintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_sh_namecrosssiterequestforgery_lowintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_sh_namecrosssiterequestforgery_mediumintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO\n")
print("\n")
print("      -    EN  "+str(count_vulnibm_sh_namemoduleexecution)+" VULNERABILIDADES EL NOMBRE INCLUYE MODULE EXECUTION, LAS ESTADÍSTICAS DE IMPACTO DE INTEGRIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_sh_namemoduleexecution_highintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_sh_namemoduleexecution_lowintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_sh_namemoduleexecution_mediumintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO\n")
print("\n")
print("      -    EN  "+str(count_vulnibm_sh_namebufferoverflow)+" VULNERABILIDADES EL NOMBRE INCLUYE BUFFER OVERFLOW, LAS ESTADÍSTICAS DE IMPACTO DE INTEGRIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_sh_namebufferoverflow_highintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_sh_namebufferoverflow_lowintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_sh_namebufferoverflow_mediumintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO\n")
print("\n")
print("      -    EN  "+str(count_vulnibm_sh_namecommandexecution)+" VULNERABILIDADES EL NOMBRE INCLUYE COMMAND EXECUTION, LAS ESTADÍSTICAS DE IMPACTO DE INTEGRIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_sh_namecommandexecution_highintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_sh_namecommandexecution_lowintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_sh_namecommandexecution_mediumintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO\n")
print("\n")
print("      -    EN  "+str(count_vulnibm_sh_namespoofing)+" VULNERABILIDADES EL NOMBRE INCLUYE SPOOFING, LAS ESTADÍSTICAS DE IMPACTO DE INTEGRIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_sh_namespoofing_highintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_sh_namespoofing_lowintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_sh_namespoofing_mediumintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO\n")
print("\n")
print("      -    EN  "+str(count_vulnibm_sh_nameclickjacking)+" VULNERABILIDADES EL NOMBRE INCLUYE CLICKJACKING, LAS ESTADÍSTICAS DE IMPACTO DE INTEGRIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_sh_nameclickjacking_highintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_sh_nameclickjacking_lowintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_sh_nameclickjacking_mediumintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO\n")
print("\n")
print("      -    EN  "+str(count_vulnibm_sh_namehijacking)+" VULNERABILIDADES EL NOMBRE INCLUYE HIJACKING, LAS ESTADÍSTICAS DE IMPACTO DE INTEGRIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_sh_namehijacking_highintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_sh_namehijacking_lowintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_sh_namehijacking_mediumintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO\n")
print("\n")
print("      -    EN  "+str(count_vulnibm_sh_namefileinclude)+" VULNERABILIDADES EL NOMBRE INCLUYE FILEINCLUDE, LAS ESTADÍSTICAS DE IMPACTO DE INTEGRIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_sh_namefileinclude_highintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_sh_namefileinclude_lowintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_sh_namefileinclude_mediumintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO\n")
print("\n")
print("      -    EN  "+str(count_vulnibm_sh_namebruteforce)+" VULNERABILIDADES EL NOMBRE INCLUYE BRUTEFORCE, LAS ESTADÍSTICAS DE IMPACTO DE INTEGRIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_sh_namebruteforce_highintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_sh_namebruteforce_lowintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_sh_namebruteforce_mediumintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO\n")
print("\n")
print("      -    EN  "+str(count_vulnibm_sh_namefileupload)+" VULNERABILIDADES EL NOMBRE INCLUYE FILE UPLOAD, LAS ESTADÍSTICAS DE IMPACTO DE INTEGRIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_sh_namefileupload_highintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_sh_namefileupload_lowintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_sh_namefileupload_mediumintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO\n")
print("\n")
print("      -    EN  "+str(count_vulnibm_sh_nameheaderinjection)+" VULNERABILIDADES EL NOMBRE INCLUYE HEADER INJECTION, LAS ESTADÍSTICAS DE IMPACTO DE INTEGRIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_sh_nameheaderinjection_highintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_sh_nameheaderinjection_lowintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_sh_nameheaderinjection_mediumintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO\n")
print("\n")
print("      -    EN  "+str(count_vulnibm_sh_nametampering)+" VULNERABILIDADES EL NOMBRE INCLUYE TAMPERING, LAS ESTADÍSTICAS DE IMPACTO DE INTEGRIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_sh_nametampering_highintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_sh_nametampering_lowintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_sh_nametampering_mediumintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO\n")
print("\n")
print("      -    EN  "+str(count_vulnibm_sh_nameanother)+" VULNERABILIDADES EL NOMBRE INCLUYE OTRA CADENA, LAS ESTADÍSTICAS DE IMPACTO DE INTEGRIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_sh_nameanother_highintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_sh_nameanother_lowintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_sh_nameanother_mediumintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO\n")
print("\n")





print("**********************************************PORCENTAJE NOMBRE/IMPACTO DE INTEGRIDAD VULNERABILIDADES IBM PARTE SMART HOME**********************************************")
print("\n")                            
print("\n")
print(" DE UN TOTAL DE "+str(count_vulnibm_sh_names)+" VULNERABILIDADES :\n") 
print("\n")
print("   - LOS PORCENTAJES DE VALORES DE NOMBRE SON LOS SIGUIENTES:  \n")
if(count_vulnibm_sh_namepathtraversal>0):
    print("      -    EN EL  "+str(float(((count_vulnibm_sh_namepathtraversal*100)/count_vulnibm_sh_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE PATH TRAVERSAL, LOS PORCENTAJES DE IMPACTO DE INTEGRIDAD SON LOS SIGUIENTES :  \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namepathtraversal_highintimpact*100)/count_vulnibm_sh_namepathtraversal)))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namepathtraversal_lowintimpact*100)/count_vulnibm_sh_namepathtraversal)))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namepathtraversal_mediumintimpact*100)/count_vulnibm_sh_namepathtraversal)))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO\n")
    print("\n")
if(count_vulnibm_sh_namedirectorytraversal>0):
    print("      -    EN EL  "+str(float(((count_vulnibm_sh_namedirectorytraversal*100)/count_vulnibm_sh_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE DIRECTORY TRAVERSAL, LOS PORCENTAJES DE IMPACTO DE INTEGRIDAD SON LOS SIGUIENTES :  \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namedirectorytraversal_highintimpact*100)/count_vulnibm_sh_namedirectorytraversal)))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namedirectorytraversal_lowintimpact*100)/count_vulnibm_sh_namedirectorytraversal)))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namedirectorytraversal_mediumintimpact*100)/count_vulnibm_sh_namedirectorytraversal)))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO\n")
    print("\n")
if(count_vulnibm_sh_nameprivilegeescalation>0):
    print("      -    EN EL  "+str(float(((count_vulnibm_sh_nameprivilegeescalation*100)/count_vulnibm_sh_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE PRIVILEGE ESCALATION, LOS PORCENTAJES DE IMPACTO DE INTEGRIDAD SON LOS SIGUIENTES :  \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_nameprivilegeescalation_highintimpact*100)/count_vulnibm_sh_nameprivilegeescalation)))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_nameprivilegeescalation_lowintimpact*100)/count_vulnibm_sh_nameprivilegeescalation)))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_nameprivilegeescalation_mediumintimpact*100)/count_vulnibm_sh_nameprivilegeescalation)))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO\n")
    print("\n")
if(count_vulnibm_sh_namecrosssitescripting>0):
    print("      -    EN EL  "+str(float(((count_vulnibm_sh_namecrosssitescripting*100)/count_vulnibm_sh_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE CROSS SITE SCRIPTING, LOS PORCENTAJES DE IMPACTO DE INTEGRIDAD SON LOS SIGUIENTES :  \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namecrosssitescripting_highintimpact*100)/count_vulnibm_sh_namecrosssitescripting)))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namecrosssitescripting_lowintimpact*100)/count_vulnibm_sh_namecrosssitescripting)))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namecrosssitescripting_mediumintimpact*100)/count_vulnibm_sh_namecrosssitescripting)))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO\n")
    print("\n")
if(count_vulnibm_sh_namesecuritybypass>0):
    print("      -    EN EL  "+str(float(((count_vulnibm_sh_namesecuritybypass*100)/count_vulnibm_sh_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE SECURITY BYPASS, LOS PORCENTAJES DE IMPACTO DE INTEGRIDAD SON LOS SIGUIENTES :  \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namesecuritybypass_highintimpact*100)/count_vulnibm_sh_namesecuritybypass)))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namesecuritybypass_lowintimpact*100)/count_vulnibm_sh_namesecuritybypass)))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namesecuritybypass_mediumintimpact*100)/count_vulnibm_sh_namesecuritybypass)))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO\n")
    print("\n")
if(count_vulnibm_sh_nameinformationdisclosure>0):
    print("      -    EN EL  "+str(float(((count_vulnibm_sh_nameinformationdisclosure*100)/count_vulnibm_sh_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE INFORMATION DISCLOSURE, LOS PORCENTAJES DE IMPACTO DE INTEGRIDAD SON LOS SIGUIENTES :  \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_nameinformationdisclosure_highintimpact*100)/count_vulnibm_sh_nameinformationdisclosure)))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_nameinformationdisclosure_lowintimpact*100)/count_vulnibm_sh_nameinformationdisclosure)))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_nameinformationdisclosure_mediumintimpact*100)/count_vulnibm_sh_nameinformationdisclosure)))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO\n")
    print("\n")
if(count_vulnibm_sh_namedenialofservice>0):
    print("      -    EN EL  "+str(float(((count_vulnibm_sh_namedenialofservice*100)/count_vulnibm_sh_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE DENIAL OF SERVICE, LOS PORCENTAJES DE IMPACTO DE INTEGRIDAD SON LOS SIGUIENTES :  \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namedenialofservice_highintimpact*100)/count_vulnibm_sh_namedenialofservice)))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namedenialofservice_lowintimpact*100)/count_vulnibm_sh_namedenialofservice)))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namedenialofservice_mediumintimpact*100)/count_vulnibm_sh_namedenialofservice)))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO\n")
    print("\n")
if(count_vulnibm_sh_namecodeexecution>0):
    print("      -    EN EL  "+str(float(((count_vulnibm_sh_namecodeexecution*100)/count_vulnibm_sh_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE CODE EXECUTION, LOS PORCENTAJES DE IMPACTO DE INTEGRIDAD SON LOS SIGUIENTES :  \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namecodeexecution_highintimpact*100)/count_vulnibm_sh_namecodeexecution)))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namecodeexecution_lowintimpact*100)/count_vulnibm_sh_namecodeexecution)))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namecodeexecution_mediumintimpact*100)/count_vulnibm_sh_namecodeexecution)))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO\n")
    print("\n")
if(count_vulnibm_sh_namemaninthemiddle>0):
    print("      -    EN EL  "+str(float(((count_vulnibm_sh_namemaninthemiddle*100)/count_vulnibm_sh_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE MAN IN THE MIDDLE, LOS PORCENTAJES DE IMPACTO DE INTEGRIDAD SON LOS SIGUIENTES :  \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namemaninthemiddle_highintimpact*100)/count_vulnibm_sh_namemaninthemiddle)))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namemaninthemiddle_lowintimpact*100)/count_vulnibm_sh_namemaninthemiddle)))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namemaninthemiddle_mediumintimpact*100)/count_vulnibm_sh_namemaninthemiddle)))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO\n")
    print("\n")
if(count_vulnibm_sh_namesqlinjection>0):
    print("      -    EN EL  "+str(float(((count_vulnibm_sh_namesqlinjection*100)/count_vulnibm_sh_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE SQL INJECTION, LOS PORCENTAJES DE IMPACTO DE INTEGRIDAD SON LOS SIGUIENTES :  \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namesqlinjection_highintimpact*100)/count_vulnibm_sh_namesqlinjection)))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namesqlinjection_lowintimpact*100)/count_vulnibm_sh_namesqlinjection)))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namesqlinjection_mediumintimpact*100)/count_vulnibm_sh_namesqlinjection)))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO\n")
    print("\n")
if(count_vulnibm_sh_namecrosssiterequestforgery>0):
    print("      -    EN EL  "+str(float(((count_vulnibm_sh_namecrosssiterequestforgery*100)/count_vulnibm_sh_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE CROSS SITE REQUEST FORGERY, LOS PORCENTAJES DE IMPACTO DE INTEGRIDAD SON LOS SIGUIENTES :  \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namecrosssiterequestforgery_highintimpact*100)/count_vulnibm_sh_namecrosssiterequestforgery)))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namecrosssiterequestforgery_lowintimpact*100)/count_vulnibm_sh_namecrosssiterequestforgery)))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namecrosssiterequestforgery_mediumintimpact*100)/count_vulnibm_sh_namecrosssiterequestforgery)))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO\n")
    print("\n")
if(count_vulnibm_sh_namemoduleexecution>0):
    print("      -    EN EL  "+str(float(((count_vulnibm_sh_namemoduleexecution*100)/count_vulnibm_sh_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE MODULE EXECUTION, LOS PORCENTAJES DE IMPACTO DE INTEGRIDAD SON LOS SIGUIENTES :  \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namemoduleexecution_highintimpact*100)/count_vulnibm_sh_namemoduleexecution)))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namemoduleexecution_lowintimpact*100)/count_vulnibm_sh_namemoduleexecution)))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namemoduleexecution_mediumintimpact*100)/count_vulnibm_sh_namemoduleexecution)))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO\n")
    print("\n")
if(count_vulnibm_sh_namebufferoverflow>0):
    print("      -    EN EL  "+str(float(((count_vulnibm_sh_namebufferoverflow*100)/count_vulnibm_sh_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE BUFFER OVERFLOW, LOS PORCENTAJES DE IMPACTO DE INTEGRIDAD SON LOS SIGUIENTES :  \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namebufferoverflow_highintimpact*100)/count_vulnibm_sh_namebufferoverflow)))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namebufferoverflow_lowintimpact*100)/count_vulnibm_sh_namebufferoverflow)))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namebufferoverflow_mediumintimpact*100)/count_vulnibm_sh_namebufferoverflow)))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO\n")
    print("\n")
if(count_vulnibm_sh_namecommandexecution>0):
    print("      -    EN EL  "+str(float(((count_vulnibm_sh_namecommandexecution*100)/count_vulnibm_sh_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE COMMAND EXECUTION, LOS PORCENTAJES DE IMPACTO DE INTEGRIDAD SON LOS SIGUIENTES :  \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namecommandexecution_highintimpact*100)/count_vulnibm_sh_namecommandexecution)))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namecommandexecution_lowintimpact*100)/count_vulnibm_sh_namecommandexecution)))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namecommandexecution_mediumintimpact*100)/count_vulnibm_sh_namecommandexecution)))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO\n")
    print("\n")
if(count_vulnibm_sh_namespoofing>0):
    print("      -    EN EL  "+str(float(((count_vulnibm_sh_namespoofing*100)/count_vulnibm_sh_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE SPOOFING, LOS PORCENTAJES DE IMPACTO DE INTEGRIDAD SON LOS SIGUIENTES :  \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namespoofing_highintimpact*100)/count_vulnibm_sh_namespoofing)))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namespoofing_lowintimpact*100)/count_vulnibm_sh_namespoofing)))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namespoofing_mediumintimpact*100)/count_vulnibm_sh_namespoofing)))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO\n")
    print("\n")
if(count_vulnibm_sh_nameclickjacking>0):
    print("      -    EN EL  "+str(float(((count_vulnibm_sh_nameclickjacking*100)/count_vulnibm_sh_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE CLICKJACKING, LOS PORCENTAJES DE IMPACTO DE INTEGRIDAD SON LOS SIGUIENTES :  \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_nameclickjacking_highintimpact*100)/count_vulnibm_sh_nameclickjacking)))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_nameclickjacking_lowintimpact*100)/count_vulnibm_sh_nameclickjacking)))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_nameclickjacking_mediumintimpact*100)/count_vulnibm_sh_nameclickjacking)))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO\n")
    print("\n")
if(count_vulnibm_sh_namehijacking>0):
    print("      -    EN EL  "+str(float(((count_vulnibm_sh_namehijacking*100)/count_vulnibm_sh_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE HIJACKING, LOS PORCENTAJES DE IMPACTO DE INTEGRIDAD SON LOS SIGUIENTES :  \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namehijacking_highintimpact*100)/count_vulnibm_sh_namehijacking)))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namehijacking_lowintimpact*100)/count_vulnibm_sh_namehijacking)))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namehijacking_mediumintimpact*100)/count_vulnibm_sh_namehijacking)))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO\n")
    print("\n")
if(count_vulnibm_sh_namefileinclude>0):
    print("      -    EN EL  "+str(float(((count_vulnibm_sh_namefileinclude*100)/count_vulnibm_sh_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE FILEINCLUDE, LOS PORCENTAJES DE IMPACTO DE INTEGRIDAD SON LOS SIGUIENTES :  \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namefileinclude_highintimpact*100)/count_vulnibm_sh_namefileinclude)))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namefileinclude_lowintimpact*100)/count_vulnibm_sh_namefileinclude)))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namefileinclude_mediumintimpact*100)/count_vulnibm_sh_namefileinclude)))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO\n")
    print("\n")
if(count_vulnibm_sh_namebruteforce>0):
    print("      -    EN EL  "+str(float(((count_vulnibm_sh_namebruteforce*100)/count_vulnibm_sh_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE BRUTEFORCE, LOS PORCENTAJES DE IMPACTO DE INTEGRIDAD SON LOS SIGUIENTES :  \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namebruteforce_highintimpact*100)/count_vulnibm_sh_namebruteforce)))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namebruteforce_lowintimpact*100)/count_vulnibm_sh_namebruteforce)))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namebruteforce_mediumintimpact*100)/count_vulnibm_sh_namebruteforce)))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO\n")
    print("\n")
if(count_vulnibm_sh_namefileupload>0):
    print("      -    EN EL  "+str(float(((count_vulnibm_sh_namefileupload*100)/count_vulnibm_sh_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE FILE UPLOAD, LOS PORCENTAJES DE IMPACTO DE INTEGRIDAD SON LOS SIGUIENTES :  \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namefileupload_highintimpact*100)/count_vulnibm_sh_namefileupload)))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namefileupload_lowintimpact*100)/count_vulnibm_sh_namefileupload)))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namefileupload_mediumintimpact*100)/count_vulnibm_sh_namefileupload)))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO\n")
    print("\n")
if(count_vulnibm_sh_nameheaderinjection>0):
    print("      -    EN EL  "+str(float(((count_vulnibm_sh_nameheaderinjection*100)/count_vulnibm_sh_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE HEADER INJECTION, LOS PORCENTAJES DE IMPACTO DE INTEGRIDAD SON LOS SIGUIENTES :  \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_nameheaderinjection_highintimpact*100)/count_vulnibm_sh_nameheaderinjection)))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_nameheaderinjection_lowintimpact*100)/count_vulnibm_sh_nameheaderinjection)))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_nameheaderinjection_mediumintimpact*100)/count_vulnibm_sh_nameheaderinjection)))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO\n")
    print("\n")
if(count_vulnibm_sh_nametampering>0):
    print("      -    EN EL  "+str(float(((count_vulnibm_sh_nametampering*100)/count_vulnibm_sh_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE TAMPERING, LOS PORCENTAJES DE IMPACTO DE INTEGRIDAD SON LOS SIGUIENTES :  \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_nametampering_highintimpact*100)/count_vulnibm_sh_nametampering)))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_nametampering_lowintimpact*100)/count_vulnibm_sh_nametampering)))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_nametampering_mediumintimpact*100)/count_vulnibm_sh_nametampering)))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO\n")
    print("\n")
    print("      -    EN EL  "+str(float(((count_vulnibm_sh_nameanother*100)/count_vulnibm_sh_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE OTRA CADENA, LOS PORCENTAJES DE IMPACTO DE INTEGRIDAD SON LOS SIGUIENTES :  \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_nameanother_highintimpact*100)/count_vulnibm_sh_nameanother)))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_nameanother_lowintimpact*100)/count_vulnibm_sh_nameanother)))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_nameanother_mediumintimpact*100)/count_vulnibm_sh_nameanother)))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO\n")
    print("\n")



print("**********************************************ESTADÍSTICAS NOMBRE/IMPACTO DE INTEGRIDAD VULNERABILIDADES IBM PARTE IOT Y SMART HOME**********************************************")
print("\n")                            
print("\n")
print(" DE UN TOTAL DE "+str(count_vulnibm_iot_names+count_vulnibm_sh_names)+" VULNERABILIDADES:\n") 
print("\n")
print("   - LAS ESTADISTICAS DE VALORES DE NOMBRE SON LAS SIGUIENTES:  \n")
print("      -    EN  "+str(count_vulnibm_iot_namepathtraversal+count_vulnibm_sh_namepathtraversal)+" VULNERABILIDADES EL NOMBRE INCLUYE PATH TRAVERSAL, LOS PORCENTAJES DE IMPACTO DE INTEGRIDAD SON LOS SIGUIENTES:  \n")
print("            -    EN  "+str(count_vulnibm_iot_namepathtraversal_highintimpact+count_vulnibm_sh_namepathtraversal_highintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_iot_namepathtraversal_lowintimpact+count_vulnibm_sh_namepathtraversal_lowintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_iot_namepathtraversal_mediumintimpact+count_vulnibm_sh_namepathtraversal_mediumintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_namedirectorytraversal+count_vulnibm_sh_namedirectorytraversal)+" VULNERABILIDADES EL NOMBRE INCLUYE directorytraversal, LOS PORCENTAJES DE IMPACTO DE INTEGRIDAD SON LOS SIGUIENTES:  \n")
print("            -    EN  "+str(count_vulnibm_iot_namedirectorytraversal_highintimpact+count_vulnibm_sh_namedirectorytraversal_highintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_iot_namedirectorytraversal_lowintimpact+count_vulnibm_sh_namedirectorytraversal_lowintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_iot_namedirectorytraversal_mediumintimpact+count_vulnibm_sh_namedirectorytraversal_mediumintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_nameprivilegeescalation+count_vulnibm_sh_nameprivilegeescalation)+" VULNERABILIDADES EL NOMBRE INCLUYE privilegeescalation, LOS PORCENTAJES DE IMPACTO DE INTEGRIDAD SON LOS SIGUIENTES:  \n")
print("            -    EN  "+str(count_vulnibm_iot_nameprivilegeescalation_highintimpact+count_vulnibm_sh_nameprivilegeescalation_highintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_iot_nameprivilegeescalation_lowintimpact+count_vulnibm_sh_nameprivilegeescalation_lowintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_iot_nameprivilegeescalation_mediumintimpact+count_vulnibm_sh_nameprivilegeescalation_mediumintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_namecrosssitescripting+count_vulnibm_sh_namecrosssitescripting)+" VULNERABILIDADES EL NOMBRE INCLUYE crosssitescripting, LOS PORCENTAJES DE IMPACTO DE INTEGRIDAD SON LOS SIGUIENTES:  \n")
print("            -    EN  "+str(count_vulnibm_iot_namecrosssitescripting_highintimpact+count_vulnibm_sh_namecrosssitescripting_highintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_iot_namecrosssitescripting_lowintimpact+count_vulnibm_sh_namecrosssitescripting_lowintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_iot_namecrosssitescripting_mediumintimpact+count_vulnibm_sh_namecrosssitescripting_mediumintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_namesecuritybypass+count_vulnibm_sh_namesecuritybypass)+" VULNERABILIDADES EL NOMBRE INCLUYE securitybypass, LOS PORCENTAJES DE IMPACTO DE INTEGRIDAD SON LOS SIGUIENTES:  \n")
print("            -    EN  "+str(count_vulnibm_iot_namesecuritybypass_highintimpact+count_vulnibm_sh_namesecuritybypass_highintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_iot_namesecuritybypass_lowintimpact+count_vulnibm_sh_namesecuritybypass_lowintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_iot_namesecuritybypass_mediumintimpact+count_vulnibm_sh_namesecuritybypass_mediumintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_nameinformationdisclosure+count_vulnibm_sh_nameinformationdisclosure)+" VULNERABILIDADES EL NOMBRE INCLUYE informationdisclosure, LOS PORCENTAJES DE IMPACTO DE INTEGRIDAD SON LOS SIGUIENTES:  \n")
print("            -    EN  "+str(count_vulnibm_iot_nameinformationdisclosure_highintimpact+count_vulnibm_sh_nameinformationdisclosure_highintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_iot_nameinformationdisclosure_lowintimpact+count_vulnibm_sh_nameinformationdisclosure_lowintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_iot_nameinformationdisclosure_mediumintimpact+count_vulnibm_sh_nameinformationdisclosure_mediumintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_namedenialofservice+count_vulnibm_sh_namedenialofservice)+" VULNERABILIDADES EL NOMBRE INCLUYE denialofservice, LOS PORCENTAJES DE IMPACTO DE INTEGRIDAD SON LOS SIGUIENTES:  \n")
print("            -    EN  "+str(count_vulnibm_iot_namedenialofservice_highintimpact+count_vulnibm_sh_namedenialofservice_highintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_iot_namedenialofservice_lowintimpact+count_vulnibm_sh_namedenialofservice_lowintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_iot_namedenialofservice_mediumintimpact+count_vulnibm_sh_namedenialofservice_mediumintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_namecodeexecution+count_vulnibm_sh_namecodeexecution)+" VULNERABILIDADES EL NOMBRE INCLUYE codeexecution, LOS PORCENTAJES DE IMPACTO DE INTEGRIDAD SON LOS SIGUIENTES:  \n")
print("            -    EN  "+str(count_vulnibm_iot_namecodeexecution_highintimpact+count_vulnibm_sh_namecodeexecution_highintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_iot_namecodeexecution_lowintimpact+count_vulnibm_sh_namecodeexecution_lowintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_iot_namecodeexecution_mediumintimpact+count_vulnibm_sh_namecodeexecution_mediumintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_namemaninthemiddle+count_vulnibm_sh_namemaninthemiddle)+" VULNERABILIDADES EL NOMBRE INCLUYE maninthemiddle, LOS PORCENTAJES DE IMPACTO DE INTEGRIDAD SON LOS SIGUIENTES:  \n")
print("            -    EN  "+str(count_vulnibm_iot_namemaninthemiddle_highintimpact+count_vulnibm_sh_namemaninthemiddle_highintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_iot_namemaninthemiddle_lowintimpact+count_vulnibm_sh_namemaninthemiddle_lowintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_iot_namemaninthemiddle_mediumintimpact+count_vulnibm_sh_namemaninthemiddle_mediumintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_namesqlinjection+count_vulnibm_sh_namesqlinjection)+" VULNERABILIDADES EL NOMBRE INCLUYE sqlinjection, LOS PORCENTAJES DE IMPACTO DE INTEGRIDAD SON LOS SIGUIENTES:  \n")
print("            -    EN  "+str(count_vulnibm_iot_namesqlinjection_highintimpact+count_vulnibm_sh_namesqlinjection_highintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_iot_namesqlinjection_lowintimpact+count_vulnibm_sh_namesqlinjection_lowintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_iot_namesqlinjection_mediumintimpact+count_vulnibm_sh_namesqlinjection_mediumintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_namecrosssiterequestforgery+count_vulnibm_sh_namecrosssiterequestforgery)+" VULNERABILIDADES EL NOMBRE INCLUYE crosssiterequestforgery, LOS PORCENTAJES DE IMPACTO DE INTEGRIDAD SON LOS SIGUIENTES:  \n")
print("            -    EN  "+str(count_vulnibm_iot_namecrosssiterequestforgery_highintimpact+count_vulnibm_sh_namecrosssiterequestforgery_highintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_iot_namecrosssiterequestforgery_lowintimpact+count_vulnibm_sh_namecrosssiterequestforgery_lowintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_iot_namecrosssiterequestforgery_mediumintimpact+count_vulnibm_sh_namecrosssiterequestforgery_mediumintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_namemoduleexecution+count_vulnibm_sh_namemoduleexecution)+" VULNERABILIDADES EL NOMBRE INCLUYE moduleexecution, LOS PORCENTAJES DE IMPACTO DE INTEGRIDAD SON LOS SIGUIENTES:  \n")
print("            -    EN  "+str(count_vulnibm_iot_namemoduleexecution_highintimpact+count_vulnibm_sh_namemoduleexecution_highintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_iot_namemoduleexecution_lowintimpact+count_vulnibm_sh_namemoduleexecution_lowintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_iot_namemoduleexecution_mediumintimpact+count_vulnibm_sh_namemoduleexecution_mediumintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_namebufferoverflow+count_vulnibm_sh_namebufferoverflow)+" VULNERABILIDADES EL NOMBRE INCLUYE bufferoverflow, LOS PORCENTAJES DE IMPACTO DE INTEGRIDAD SON LOS SIGUIENTES:  \n")
print("            -    EN  "+str(count_vulnibm_iot_namebufferoverflow_highintimpact+count_vulnibm_sh_namebufferoverflow_highintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_iot_namebufferoverflow_lowintimpact+count_vulnibm_sh_namebufferoverflow_lowintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_iot_namebufferoverflow_mediumintimpact+count_vulnibm_sh_namebufferoverflow_mediumintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_namecommandexecution+count_vulnibm_sh_namecommandexecution)+" VULNERABILIDADES EL NOMBRE INCLUYE commandexecution, LOS PORCENTAJES DE IMPACTO DE INTEGRIDAD SON LOS SIGUIENTES:  \n")
print("            -    EN  "+str(count_vulnibm_iot_namecommandexecution_highintimpact+count_vulnibm_sh_namecommandexecution_highintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_iot_namecommandexecution_lowintimpact+count_vulnibm_sh_namecommandexecution_lowintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_iot_namecommandexecution_mediumintimpact+count_vulnibm_sh_namecommandexecution_mediumintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_namespoofing+count_vulnibm_sh_namespoofing)+" VULNERABILIDADES EL NOMBRE INCLUYE spoofing, LOS PORCENTAJES DE IMPACTO DE INTEGRIDAD SON LOS SIGUIENTES:  \n")
print("            -    EN  "+str(count_vulnibm_iot_namespoofing_highintimpact+count_vulnibm_sh_namespoofing_highintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_iot_namespoofing_lowintimpact+count_vulnibm_sh_namespoofing_lowintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_iot_namespoofing_mediumintimpact+count_vulnibm_sh_namespoofing_mediumintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_nameclickjacking+count_vulnibm_sh_nameclickjacking)+" VULNERABILIDADES EL NOMBRE INCLUYE clickjacking, LOS PORCENTAJES DE IMPACTO DE INTEGRIDAD SON LOS SIGUIENTES:  \n")
print("            -    EN  "+str(count_vulnibm_iot_nameclickjacking_highintimpact+count_vulnibm_sh_nameclickjacking_highintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_iot_nameclickjacking_lowintimpact+count_vulnibm_sh_nameclickjacking_lowintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_iot_nameclickjacking_mediumintimpact+count_vulnibm_sh_nameclickjacking_mediumintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_namehijacking+count_vulnibm_sh_namehijacking)+" VULNERABILIDADES EL NOMBRE INCLUYE hijacking, LOS PORCENTAJES DE IMPACTO DE INTEGRIDAD SON LOS SIGUIENTES:  \n")
print("            -    EN  "+str(count_vulnibm_iot_namehijacking_highintimpact+count_vulnibm_sh_namehijacking_highintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_iot_namehijacking_lowintimpact+count_vulnibm_sh_namehijacking_lowintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_iot_namehijacking_mediumintimpact+count_vulnibm_sh_namehijacking_mediumintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_namefileinclude+count_vulnibm_sh_namefileinclude)+" VULNERABILIDADES EL NOMBRE INCLUYE fileinclude, LOS PORCENTAJES DE IMPACTO DE INTEGRIDAD SON LOS SIGUIENTES:  \n")
print("            -    EN  "+str(count_vulnibm_iot_namefileinclude_highintimpact+count_vulnibm_sh_namefileinclude_highintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_iot_namefileinclude_lowintimpact+count_vulnibm_sh_namefileinclude_lowintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_iot_namefileinclude_mediumintimpact+count_vulnibm_sh_namefileinclude_mediumintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_namebruteforce+count_vulnibm_sh_namebruteforce)+" VULNERABILIDADES EL NOMBRE INCLUYE bruteforce, LOS PORCENTAJES DE IMPACTO DE INTEGRIDAD SON LOS SIGUIENTES:  \n")
print("            -    EN  "+str(count_vulnibm_iot_namebruteforce_highintimpact+count_vulnibm_sh_namebruteforce_highintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_iot_namebruteforce_lowintimpact+count_vulnibm_sh_namebruteforce_lowintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_iot_namebruteforce_mediumintimpact+count_vulnibm_sh_namebruteforce_mediumintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_namefileupload+count_vulnibm_sh_namefileupload)+" VULNERABILIDADES EL NOMBRE INCLUYE fileupload, LOS PORCENTAJES DE IMPACTO DE INTEGRIDAD SON LOS SIGUIENTES:  \n")
print("            -    EN  "+str(count_vulnibm_iot_namefileupload_highintimpact+count_vulnibm_sh_namefileupload_highintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_iot_namefileupload_lowintimpact+count_vulnibm_sh_namefileupload_lowintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_iot_namefileupload_mediumintimpact+count_vulnibm_sh_namefileupload_mediumintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_nameheaderinjection+count_vulnibm_sh_nameheaderinjection)+" VULNERABILIDADES EL NOMBRE INCLUYE headerinjection, LOS PORCENTAJES DE IMPACTO DE INTEGRIDAD SON LOS SIGUIENTES:  \n")
print("            -    EN  "+str(count_vulnibm_iot_nameheaderinjection_highintimpact+count_vulnibm_sh_nameheaderinjection_highintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_iot_nameheaderinjection_lowintimpact+count_vulnibm_sh_nameheaderinjection_lowintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_iot_nameheaderinjection_mediumintimpact+count_vulnibm_sh_nameheaderinjection_mediumintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_nametampering+count_vulnibm_sh_nametampering)+" VULNERABILIDADES EL NOMBRE INCLUYE tampering, LOS PORCENTAJES DE IMPACTO DE INTEGRIDAD SON LOS SIGUIENTES:  \n")
print("            -    EN  "+str(count_vulnibm_iot_nametampering_highintimpact+count_vulnibm_sh_nametampering_highintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_iot_nametampering_lowintimpact+count_vulnibm_sh_nametampering_lowintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_iot_nametampering_mediumintimpact+count_vulnibm_sh_nametampering_mediumintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_nameanother+count_vulnibm_sh_nameanother)+" VULNERABILIDADES EL NOMBRE INCLUYE OTRO NOMBRE DISTINTO, LOS PORCENTAJES DE IMPACTO DE INTEGRIDAD SON LOS SIGUIENTES:  \n")
print("            -    EN  "+str(count_vulnibm_iot_nameanother_highintimpact+count_vulnibm_sh_nameanother_highintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_iot_nameanother_lowintimpact+count_vulnibm_sh_nameanother_lowintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_iot_nameanother_mediumintimpact+count_vulnibm_sh_nameanother_mediumintimpact)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO \n")
print("\n")









print("**********************************************PORCENTAJES NOMBRE/IMPACTO DE INTEGRIDAD VULNERABILIDADES IBM PARTE IOT Y SMART HOME **********************************************")
print("\n")                            
print("\n")
print(" DE UN TOTAL DE "+str(count_vulnibm_iot_names+count_vulnibm_sh_names)+" VULNERABILIDADES:\n") 
print("\n")
print("   - LOS PORCENTAJES DE VALORES DE NOMBRE SON LOS SIGUIENTES:  \n")
print("      -    EN EL "+str(float((((count_vulnibm_iot_namepathtraversal+count_vulnibm_sh_namepathtraversal)*100)/(count_vulnibm_iot_names+count_vulnibm_sh_names))))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE PATHTRAVERSAL, LOS PORCENTAJES DE IMPACTO DE INTEGRIDAD SON LOS SIGUIENTES:  \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namepathtraversal_highintimpact+count_vulnibm_sh_namepathtraversal_highintimpact)*100)/(count_vulnibm_iot_namepathtraversal+count_vulnibm_sh_namepathtraversal))))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namepathtraversal_lowintimpact+count_vulnibm_sh_namepathtraversal_lowintimpact)*100)/(count_vulnibm_iot_namepathtraversal+count_vulnibm_sh_namepathtraversal))))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namepathtraversal_mediumintimpact+count_vulnibm_sh_namepathtraversal_mediumintimpact)*100)/(count_vulnibm_iot_namepathtraversal+count_vulnibm_sh_namepathtraversal))))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO \n")
print("\n")
print("      -    EN EL "+str(float((((count_vulnibm_iot_namedirectorytraversal+count_vulnibm_sh_namedirectorytraversal)*100)/(count_vulnibm_iot_names+count_vulnibm_sh_names))))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE DIRECTORY TRAVERSAL, LOS PORCENTAJES DE IMPACTO DE INTEGRIDAD SON LOS SIGUIENTES:  \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namedirectorytraversal_highintimpact+count_vulnibm_sh_namedirectorytraversal_highintimpact)*100)/(count_vulnibm_iot_namedirectorytraversal+count_vulnibm_sh_namedirectorytraversal))))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namedirectorytraversal_lowintimpact+count_vulnibm_sh_namedirectorytraversal_lowintimpact)*100)/(count_vulnibm_iot_namedirectorytraversal+count_vulnibm_sh_namedirectorytraversal))))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namedirectorytraversal_mediumintimpact+count_vulnibm_sh_namedirectorytraversal_mediumintimpact)*100)/(count_vulnibm_iot_namedirectorytraversal+count_vulnibm_sh_namedirectorytraversal))))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO \n")
print("\n")
print("      -    EN EL "+str(float((((count_vulnibm_iot_nameprivilegeescalation+count_vulnibm_sh_nameprivilegeescalation)*100)/(count_vulnibm_iot_names+count_vulnibm_sh_names))))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE PRIVILEGE ESCALATION, LOS PORCENTAJES DE IMPACTO DE INTEGRIDAD SON LOS SIGUIENTES:  \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_nameprivilegeescalation_highintimpact+count_vulnibm_sh_nameprivilegeescalation_highintimpact)*100)/(count_vulnibm_iot_nameprivilegeescalation+count_vulnibm_sh_nameprivilegeescalation))))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_nameprivilegeescalation_lowintimpact+count_vulnibm_sh_nameprivilegeescalation_lowintimpact)*100)/(count_vulnibm_iot_nameprivilegeescalation+count_vulnibm_sh_nameprivilegeescalation))))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_nameprivilegeescalation_mediumintimpact+count_vulnibm_sh_nameprivilegeescalation_mediumintimpact)*100)/(count_vulnibm_iot_nameprivilegeescalation+count_vulnibm_sh_nameprivilegeescalation))))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO \n")
print("\n")
print("      -    EN EL "+str(float((((count_vulnibm_iot_namecrosssitescripting+count_vulnibm_sh_namecrosssitescripting)*100)/(count_vulnibm_iot_names+count_vulnibm_sh_names))))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE CROSS SITE SCRIPTING, LOS PORCENTAJES DE IMPACTO DE INTEGRIDAD SON LOS SIGUIENTES:  \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namecrosssitescripting_highintimpact+count_vulnibm_sh_namecrosssitescripting_highintimpact)*100)/(count_vulnibm_iot_namecrosssitescripting+count_vulnibm_sh_namecrosssitescripting))))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namecrosssitescripting_lowintimpact+count_vulnibm_sh_namecrosssitescripting_lowintimpact)*100)/(count_vulnibm_iot_namecrosssitescripting+count_vulnibm_sh_namecrosssitescripting))))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namecrosssitescripting_mediumintimpact+count_vulnibm_sh_namecrosssitescripting_mediumintimpact)*100)/(count_vulnibm_iot_namecrosssitescripting+count_vulnibm_sh_namecrosssitescripting))))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO \n")
print("\n")
print("      -    EN EL "+str(float((((count_vulnibm_iot_namesecuritybypass+count_vulnibm_sh_namesecuritybypass)*100)/(count_vulnibm_iot_names+count_vulnibm_sh_names))))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE SECURITY BYPASS, LOS PORCENTAJES DE IMPACTO DE INTEGRIDAD SON LOS SIGUIENTES:  \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namesecuritybypass_highintimpact+count_vulnibm_sh_namesecuritybypass_highintimpact)*100)/(count_vulnibm_iot_namesecuritybypass+count_vulnibm_sh_namesecuritybypass))))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namesecuritybypass_lowintimpact+count_vulnibm_sh_namesecuritybypass_lowintimpact)*100)/(count_vulnibm_iot_namesecuritybypass+count_vulnibm_sh_namesecuritybypass))))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namesecuritybypass_mediumintimpact+count_vulnibm_sh_namesecuritybypass_mediumintimpact)*100)/(count_vulnibm_iot_namesecuritybypass+count_vulnibm_sh_namesecuritybypass))))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO \n")
print("\n")
print("      -    EN EL "+str(float((((count_vulnibm_iot_nameinformationdisclosure+count_vulnibm_sh_nameinformationdisclosure)*100)/(count_vulnibm_iot_names+count_vulnibm_sh_names))))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE INFORMATION DISCLOSURE, LOS PORCENTAJES DE IMPACTO DE INTEGRIDAD SON LOS SIGUIENTES:  \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_nameinformationdisclosure_highintimpact+count_vulnibm_sh_nameinformationdisclosure_highintimpact)*100)/(count_vulnibm_iot_nameinformationdisclosure+count_vulnibm_sh_nameinformationdisclosure))))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_nameinformationdisclosure_lowintimpact+count_vulnibm_sh_nameinformationdisclosure_lowintimpact)*100)/(count_vulnibm_iot_nameinformationdisclosure+count_vulnibm_sh_nameinformationdisclosure))))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_nameinformationdisclosure_mediumintimpact+count_vulnibm_sh_nameinformationdisclosure_mediumintimpact)*100)/(count_vulnibm_iot_nameinformationdisclosure+count_vulnibm_sh_nameinformationdisclosure))))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO \n")
print("\n")
print("      -    EN EL "+str(float((((count_vulnibm_iot_namedenialofservice+count_vulnibm_sh_namedenialofservice)*100)/(count_vulnibm_iot_names+count_vulnibm_sh_names))))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE DENIAL OF SERVICE, LOS PORCENTAJES DE IMPACTO DE INTEGRIDAD SON LOS SIGUIENTES:  \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namedenialofservice_highintimpact+count_vulnibm_sh_namedenialofservice_highintimpact)*100)/(count_vulnibm_iot_namedenialofservice+count_vulnibm_sh_namedenialofservice))))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namedenialofservice_lowintimpact+count_vulnibm_sh_namedenialofservice_lowintimpact)*100)/(count_vulnibm_iot_namedenialofservice+count_vulnibm_sh_namedenialofservice))))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namedenialofservice_mediumintimpact+count_vulnibm_sh_namedenialofservice_mediumintimpact)*100)/(count_vulnibm_iot_namedenialofservice+count_vulnibm_sh_namedenialofservice))))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO \n")
print("\n")
print("      -    EN EL "+str(float((((count_vulnibm_iot_namecodeexecution+count_vulnibm_sh_namecodeexecution)*100)/(count_vulnibm_iot_names+count_vulnibm_sh_names))))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE CODE EXECUTION, LOS PORCENTAJES DE IMPACTO DE INTEGRIDAD SON LOS SIGUIENTES:  \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namecodeexecution_highintimpact+count_vulnibm_sh_namecodeexecution_highintimpact)*100)/(count_vulnibm_iot_namecodeexecution+count_vulnibm_sh_namecodeexecution))))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namecodeexecution_lowintimpact+count_vulnibm_sh_namecodeexecution_lowintimpact)*100)/(count_vulnibm_iot_namecodeexecution+count_vulnibm_sh_namecodeexecution))))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namecodeexecution_mediumintimpact+count_vulnibm_sh_namecodeexecution_mediumintimpact)*100)/(count_vulnibm_iot_namecodeexecution+count_vulnibm_sh_namecodeexecution))))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO \n")
print("\n")
print("      -    EN EL "+str(float((((count_vulnibm_iot_namemaninthemiddle+count_vulnibm_sh_namemaninthemiddle)*100)/(count_vulnibm_iot_names+count_vulnibm_sh_names))))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE MAN IN THE MIDDLE, LOS PORCENTAJES DE IMPACTO DE INTEGRIDAD SON LOS SIGUIENTES:  \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namemaninthemiddle_highintimpact+count_vulnibm_sh_namemaninthemiddle_highintimpact)*100)/(count_vulnibm_iot_namemaninthemiddle+count_vulnibm_sh_namemaninthemiddle))))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namemaninthemiddle_lowintimpact+count_vulnibm_sh_namemaninthemiddle_lowintimpact)*100)/(count_vulnibm_iot_namemaninthemiddle+count_vulnibm_sh_namemaninthemiddle))))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namemaninthemiddle_mediumintimpact+count_vulnibm_sh_namemaninthemiddle_mediumintimpact)*100)/(count_vulnibm_iot_namemaninthemiddle+count_vulnibm_sh_namemaninthemiddle))))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO \n")
print("\n")
print("      -    EN EL "+str(float((((count_vulnibm_iot_namesqlinjection+count_vulnibm_sh_namesqlinjection)*100)/(count_vulnibm_iot_names+count_vulnibm_sh_names))))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE SQL INJECTION, LOS PORCENTAJES DE IMPACTO DE INTEGRIDAD SON LOS SIGUIENTES:  \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namesqlinjection_highintimpact+count_vulnibm_sh_namesqlinjection_highintimpact)*100)/(count_vulnibm_iot_namesqlinjection+count_vulnibm_sh_namesqlinjection))))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namesqlinjection_lowintimpact+count_vulnibm_sh_namesqlinjection_lowintimpact)*100)/(count_vulnibm_iot_namesqlinjection+count_vulnibm_sh_namesqlinjection))))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namesqlinjection_mediumintimpact+count_vulnibm_sh_namesqlinjection_mediumintimpact)*100)/(count_vulnibm_iot_namesqlinjection+count_vulnibm_sh_namesqlinjection))))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO \n")
print("\n")
print("      -    EN EL "+str(float((((count_vulnibm_iot_namecrosssiterequestforgery+count_vulnibm_sh_namecrosssiterequestforgery)*100)/(count_vulnibm_iot_names+count_vulnibm_sh_names))))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE CROSS SITE REQUEST FORGERY, LOS PORCENTAJES DE IMPACTO DE INTEGRIDAD SON LOS SIGUIENTES:  \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namecrosssiterequestforgery_highintimpact+count_vulnibm_sh_namecrosssiterequestforgery_highintimpact)*100)/(count_vulnibm_iot_namecrosssiterequestforgery+count_vulnibm_sh_namecrosssiterequestforgery))))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namecrosssiterequestforgery_lowintimpact+count_vulnibm_sh_namecrosssiterequestforgery_lowintimpact)*100)/(count_vulnibm_iot_namecrosssiterequestforgery+count_vulnibm_sh_namecrosssiterequestforgery))))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namecrosssiterequestforgery_mediumintimpact+count_vulnibm_sh_namecrosssiterequestforgery_mediumintimpact)*100)/(count_vulnibm_iot_namecrosssiterequestforgery+count_vulnibm_sh_namecrosssiterequestforgery))))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO \n")
print("\n")
print("      -    EN EL "+str(float((((count_vulnibm_iot_namemoduleexecution+count_vulnibm_sh_namemoduleexecution)*100)/(count_vulnibm_iot_names+count_vulnibm_sh_names))))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE MODULE EXECUTION, LOS PORCENTAJES DE IMPACTO DE INTEGRIDAD SON LOS SIGUIENTES:  \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namemoduleexecution_highintimpact+count_vulnibm_sh_namemoduleexecution_highintimpact)*100)/(count_vulnibm_iot_namemoduleexecution+count_vulnibm_sh_namemoduleexecution))))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namemoduleexecution_lowintimpact+count_vulnibm_sh_namemoduleexecution_lowintimpact)*100)/(count_vulnibm_iot_namemoduleexecution+count_vulnibm_sh_namemoduleexecution))))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namemoduleexecution_mediumintimpact+count_vulnibm_sh_namemoduleexecution_mediumintimpact)*100)/(count_vulnibm_iot_namemoduleexecution+count_vulnibm_sh_namemoduleexecution))))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO \n")
print("\n")
print("      -    EN EL "+str(float((((count_vulnibm_iot_namebufferoverflow+count_vulnibm_sh_namebufferoverflow)*100)/(count_vulnibm_iot_names+count_vulnibm_sh_names))))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE BUFFER OVERFLOW, LOS PORCENTAJES DE IMPACTO DE INTEGRIDAD SON LOS SIGUIENTES:  \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namebufferoverflow_highintimpact+count_vulnibm_sh_namebufferoverflow_highintimpact)*100)/(count_vulnibm_iot_namebufferoverflow+count_vulnibm_sh_namebufferoverflow))))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namebufferoverflow_lowintimpact+count_vulnibm_sh_namebufferoverflow_lowintimpact)*100)/(count_vulnibm_iot_namebufferoverflow+count_vulnibm_sh_namebufferoverflow))))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namebufferoverflow_mediumintimpact+count_vulnibm_sh_namebufferoverflow_mediumintimpact)*100)/(count_vulnibm_iot_namebufferoverflow+count_vulnibm_sh_namebufferoverflow))))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO \n")
print("\n")
print("      -    EN EL "+str(float((((count_vulnibm_iot_namecommandexecution+count_vulnibm_sh_namecommandexecution)*100)/(count_vulnibm_iot_names+count_vulnibm_sh_names))))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE COMMAND EXECUTION, LOS PORCENTAJES DE IMPACTO DE INTEGRIDAD SON LOS SIGUIENTES:  \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namecommandexecution_highintimpact+count_vulnibm_sh_namecommandexecution_highintimpact)*100)/(count_vulnibm_iot_namecommandexecution+count_vulnibm_sh_namecommandexecution))))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namecommandexecution_lowintimpact+count_vulnibm_sh_namecommandexecution_lowintimpact)*100)/(count_vulnibm_iot_namecommandexecution+count_vulnibm_sh_namecommandexecution))))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namecommandexecution_mediumintimpact+count_vulnibm_sh_namecommandexecution_mediumintimpact)*100)/(count_vulnibm_iot_namecommandexecution+count_vulnibm_sh_namecommandexecution))))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO \n")
print("\n")
print("      -    EN EL "+str(float((((count_vulnibm_iot_namespoofing+count_vulnibm_sh_namespoofing)*100)/(count_vulnibm_iot_names+count_vulnibm_sh_names))))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE SPOOFING, LOS PORCENTAJES DE IMPACTO DE INTEGRIDAD SON LOS SIGUIENTES:  \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namespoofing_highintimpact+count_vulnibm_sh_namespoofing_highintimpact)*100)/(count_vulnibm_iot_namespoofing+count_vulnibm_sh_namespoofing))))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namespoofing_lowintimpact+count_vulnibm_sh_namespoofing_lowintimpact)*100)/(count_vulnibm_iot_namespoofing+count_vulnibm_sh_namespoofing))))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namespoofing_mediumintimpact+count_vulnibm_sh_namespoofing_mediumintimpact)*100)/(count_vulnibm_iot_namespoofing+count_vulnibm_sh_namespoofing))))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO \n")
print("\n")
print("      -    EN EL "+str(float((((count_vulnibm_iot_nameclickjacking+count_vulnibm_sh_nameclickjacking)*100)/(count_vulnibm_iot_names+count_vulnibm_sh_names))))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE CLICKJACKING, LOS PORCENTAJES DE IMPACTO DE INTEGRIDAD SON LOS SIGUIENTES:  \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_nameclickjacking_highintimpact+count_vulnibm_sh_nameclickjacking_highintimpact)*100)/(count_vulnibm_iot_nameclickjacking+count_vulnibm_sh_nameclickjacking))))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_nameclickjacking_lowintimpact+count_vulnibm_sh_nameclickjacking_lowintimpact)*100)/(count_vulnibm_iot_nameclickjacking+count_vulnibm_sh_nameclickjacking))))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_nameclickjacking_mediumintimpact+count_vulnibm_sh_nameclickjacking_mediumintimpact)*100)/(count_vulnibm_iot_nameclickjacking+count_vulnibm_sh_nameclickjacking))))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO \n")
print("\n")
print("      -    EN EL "+str(float((((count_vulnibm_iot_namehijacking+count_vulnibm_sh_namehijacking)*100)/(count_vulnibm_iot_names+count_vulnibm_sh_names))))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE HIJACKING, LOS PORCENTAJES DE IMPACTO DE INTEGRIDAD SON LOS SIGUIENTES:  \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namehijacking_highintimpact+count_vulnibm_sh_namehijacking_highintimpact)*100)/(count_vulnibm_iot_namehijacking+count_vulnibm_sh_namehijacking))))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namehijacking_lowintimpact+count_vulnibm_sh_namehijacking_lowintimpact)*100)/(count_vulnibm_iot_namehijacking+count_vulnibm_sh_namehijacking))))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namehijacking_mediumintimpact+count_vulnibm_sh_namehijacking_mediumintimpact)*100)/(count_vulnibm_iot_namehijacking+count_vulnibm_sh_namehijacking))))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO \n")
print("\n")
print("      -    EN EL "+str(float((((count_vulnibm_iot_namefileinclude+count_vulnibm_sh_namefileinclude)*100)/(count_vulnibm_iot_names+count_vulnibm_sh_names))))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE FILE INCLUDE, LOS PORCENTAJES DE IMPACTO DE INTEGRIDAD SON LOS SIGUIENTES:  \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namefileinclude_highintimpact+count_vulnibm_sh_namefileinclude_highintimpact)*100)/(count_vulnibm_iot_namefileinclude+count_vulnibm_sh_namefileinclude))))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namefileinclude_lowintimpact+count_vulnibm_sh_namefileinclude_lowintimpact)*100)/(count_vulnibm_iot_namefileinclude+count_vulnibm_sh_namefileinclude))))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namefileinclude_mediumintimpact+count_vulnibm_sh_namefileinclude_mediumintimpact)*100)/(count_vulnibm_iot_namefileinclude+count_vulnibm_sh_namefileinclude))))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO \n")
print("\n")
print("      -    EN EL "+str(float((((count_vulnibm_iot_namebruteforce+count_vulnibm_sh_namebruteforce)*100)/(count_vulnibm_iot_names+count_vulnibm_sh_names))))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE BRUTE FORCE, LOS PORCENTAJES DE IMPACTO DE INTEGRIDAD SON LOS SIGUIENTES:  \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namebruteforce_highintimpact+count_vulnibm_sh_namebruteforce_highintimpact)*100)/(count_vulnibm_iot_namebruteforce+count_vulnibm_sh_namebruteforce))))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namebruteforce_lowintimpact+count_vulnibm_sh_namebruteforce_lowintimpact)*100)/(count_vulnibm_iot_namebruteforce+count_vulnibm_sh_namebruteforce))))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namebruteforce_mediumintimpact+count_vulnibm_sh_namebruteforce_mediumintimpact)*100)/(count_vulnibm_iot_namebruteforce+count_vulnibm_sh_namebruteforce))))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO \n")
print("\n")
print("      -    EN EL "+str(float((((count_vulnibm_iot_namefileupload+count_vulnibm_sh_namefileupload)*100)/(count_vulnibm_iot_names+count_vulnibm_sh_names))))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE FILE UPLOAD, LOS PORCENTAJES DE IMPACTO DE INTEGRIDAD SON LOS SIGUIENTES:  \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namefileupload_highintimpact+count_vulnibm_sh_namefileupload_highintimpact)*100)/(count_vulnibm_iot_namefileupload+count_vulnibm_sh_namefileupload))))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namefileupload_lowintimpact+count_vulnibm_sh_namefileupload_lowintimpact)*100)/(count_vulnibm_iot_namefileupload+count_vulnibm_sh_namefileupload))))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namefileupload_mediumintimpact+count_vulnibm_sh_namefileupload_mediumintimpact)*100)/(count_vulnibm_iot_namefileupload+count_vulnibm_sh_namefileupload))))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO \n")
print("\n")
print("      -    EN EL "+str(float((((count_vulnibm_iot_nameheaderinjection+count_vulnibm_sh_nameheaderinjection)*100)/(count_vulnibm_iot_names+count_vulnibm_sh_names))))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE HEADER INJECTION, LOS PORCENTAJES DE IMPACTO DE INTEGRIDAD SON LOS SIGUIENTES:  \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_nameheaderinjection_highintimpact+count_vulnibm_sh_nameheaderinjection_highintimpact)*100)/(count_vulnibm_iot_nameheaderinjection+count_vulnibm_sh_nameheaderinjection))))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_nameheaderinjection_lowintimpact+count_vulnibm_sh_nameheaderinjection_lowintimpact)*100)/(count_vulnibm_iot_nameheaderinjection+count_vulnibm_sh_nameheaderinjection))))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_nameheaderinjection_mediumintimpact+count_vulnibm_sh_nameheaderinjection_mediumintimpact)*100)/(count_vulnibm_iot_nameheaderinjection+count_vulnibm_sh_nameheaderinjection))))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO \n")
print("\n")
print("      -    EN EL "+str(float((((count_vulnibm_iot_nametampering+count_vulnibm_sh_nametampering)*100)/(count_vulnibm_iot_names+count_vulnibm_sh_names))))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE TAMPERING, LOS PORCENTAJES DE IMPACTO DE INTEGRIDAD SON LOS SIGUIENTES:  \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_nametampering_highintimpact+count_vulnibm_sh_nametampering_highintimpact)*100)/(count_vulnibm_iot_nametampering+count_vulnibm_sh_nametampering))))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_nametampering_lowintimpact+count_vulnibm_sh_nametampering_lowintimpact)*100)/(count_vulnibm_iot_nametampering+count_vulnibm_sh_nametampering))))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_nametampering_mediumintimpact+count_vulnibm_sh_nametampering_mediumintimpact)*100)/(count_vulnibm_iot_nametampering+count_vulnibm_sh_nametampering))))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO \n")
print("\n")
print("      -    EN EL "+str(float((((count_vulnibm_iot_nameanother+count_vulnibm_sh_nameanother)*100)/(count_vulnibm_iot_names+count_vulnibm_sh_names))))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE UN VALOR DISTINTO, LOS PORCENTAJES DE IMPACTO DE INTEGRIDAD SON LOS SIGUIENTES:  \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_nameanother_highintimpact+count_vulnibm_sh_nameanother_highintimpact)*100)/(count_vulnibm_iot_nameanother+count_vulnibm_sh_nameanother))))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_nameanother_lowintimpact+count_vulnibm_sh_nameanother_lowintimpact)*100)/(count_vulnibm_iot_nameanother+count_vulnibm_sh_nameanother))))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_nameanother_mediumintimpact+count_vulnibm_sh_nameanother_mediumintimpact)*100)/(count_vulnibm_iot_nameanother+count_vulnibm_sh_nameanother))))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO \n")
print("\n")
               	










































