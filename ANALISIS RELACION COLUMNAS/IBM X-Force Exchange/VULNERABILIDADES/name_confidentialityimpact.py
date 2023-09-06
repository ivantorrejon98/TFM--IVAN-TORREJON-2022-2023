import pandas as pd
from datetime import datetime,timedelta



#Abro los ficheros con los que voy a tratar




df_vulnibm_iot = pd.read_excel('vulnerabilidades_ibm_iot_2023.xlsx')

#Variable para almacenar el contador total de valores de nombre
count_vulnibm_iot_names=0
#Variable para almacenar el contador total de valores de un nombre concreto
count_vulnibm_iot_namepathtraversal=0
#Variables para almacenar el contador de valores de impacto de confidencialidad dato un valor de nombre especifico
count_vulnibm_iot_namepathtraversal_confimpact=0
count_vulnibm_iot_namepathtraversal_highconfimpact=0
count_vulnibm_iot_namepathtraversal_lowconfimpact=0
count_vulnibm_iot_namepathtraversal_mediumconfimpact=0

count_vulnibm_iot_namedirectorytraversal=0
count_vulnibm_iot_namedirectorytraversal_confimpact=0
count_vulnibm_iot_namedirectorytraversal_highconfimpact=0
count_vulnibm_iot_namedirectorytraversal_lowconfimpact=0
count_vulnibm_iot_namedirectorytraversal_mediumconfimpact=0

count_vulnibm_iot_nameprivilegeescalation=0
count_vulnibm_iot_nameprivilegeescalation_confimpact=0
count_vulnibm_iot_nameprivilegeescalation_highconfimpact=0
count_vulnibm_iot_nameprivilegeescalation_lowconfimpact=0
count_vulnibm_iot_nameprivilegeescalation_mediumconfimpact=0

count_vulnibm_iot_namecrosssitescripting=0
count_vulnibm_iot_namecrosssitescripting_confimpact=0
count_vulnibm_iot_namecrosssitescripting_highconfimpact=0
count_vulnibm_iot_namecrosssitescripting_lowconfimpact=0
count_vulnibm_iot_namecrosssitescripting_mediumconfimpact=0

count_vulnibm_iot_namesecuritybypass=0
count_vulnibm_iot_namesecuritybypass_confimpact=0
count_vulnibm_iot_namesecuritybypass_highconfimpact=0
count_vulnibm_iot_namesecuritybypass_lowconfimpact=0
count_vulnibm_iot_namesecuritybypass_mediumconfimpact=0

count_vulnibm_iot_nameinformationdisclosure=0
count_vulnibm_iot_nameinformationdisclosure_confimpact=0
count_vulnibm_iot_nameinformationdisclosure_highconfimpact=0
count_vulnibm_iot_nameinformationdisclosure_lowconfimpact=0
count_vulnibm_iot_nameinformationdisclosure_mediumconfimpact=0

count_vulnibm_iot_namedenialofservice=0
count_vulnibm_iot_namedenialofservice_confimpact=0
count_vulnibm_iot_namedenialofservice_highconfimpact=0
count_vulnibm_iot_namedenialofservice_lowconfimpact=0
count_vulnibm_iot_namedenialofservice_mediumconfimpact=0

count_vulnibm_iot_namecodeexecution=0
count_vulnibm_iot_namecodeexecution_confimpact=0
count_vulnibm_iot_namecodeexecution_highconfimpact=0
count_vulnibm_iot_namecodeexecution_lowconfimpact=0
count_vulnibm_iot_namecodeexecution_mediumconfimpact=0

count_vulnibm_iot_namemaninthemiddle=0
count_vulnibm_iot_namemaninthemiddle_confimpact=0
count_vulnibm_iot_namemaninthemiddle_highconfimpact=0
count_vulnibm_iot_namemaninthemiddle_lowconfimpact=0
count_vulnibm_iot_namemaninthemiddle_mediumconfimpact=0

count_vulnibm_iot_namesqlinjection=0
count_vulnibm_iot_namesqlinjection_confimpact=0
count_vulnibm_iot_namesqlinjection_highconfimpact=0
count_vulnibm_iot_namesqlinjection_lowconfimpact=0
count_vulnibm_iot_namesqlinjection_mediumconfimpact=0

count_vulnibm_iot_namecrosssiterequestforgery=0
count_vulnibm_iot_namecrosssiterequestforgery_confimpact=0
count_vulnibm_iot_namecrosssiterequestforgery_highconfimpact=0
count_vulnibm_iot_namecrosssiterequestforgery_lowconfimpact=0
count_vulnibm_iot_namecrosssiterequestforgery_mediumconfimpact=0

count_vulnibm_iot_namemoduleexecution=0
count_vulnibm_iot_namemoduleexecution_confimpact=0
count_vulnibm_iot_namemoduleexecution_highconfimpact=0
count_vulnibm_iot_namemoduleexecution_lowconfimpact=0
count_vulnibm_iot_namemoduleexecution_mediumconfimpact=0

count_vulnibm_iot_namebufferoverflow=0
count_vulnibm_iot_namebufferoverflow_confimpact=0
count_vulnibm_iot_namebufferoverflow_highconfimpact=0
count_vulnibm_iot_namebufferoverflow_lowconfimpact=0
count_vulnibm_iot_namebufferoverflow_mediumconfimpact=0

count_vulnibm_iot_namecommandexecution=0
count_vulnibm_iot_namecommandexecution_confimpact=0
count_vulnibm_iot_namecommandexecution_highconfimpact=0
count_vulnibm_iot_namecommandexecution_lowconfimpact=0
count_vulnibm_iot_namecommandexecution_mediumconfimpact=0

count_vulnibm_iot_namespoofing=0
count_vulnibm_iot_namespoofing_confimpact=0
count_vulnibm_iot_namespoofing_highconfimpact=0
count_vulnibm_iot_namespoofing_lowconfimpact=0
count_vulnibm_iot_namespoofing_mediumconfimpact=0

count_vulnibm_iot_nameclickjacking=0
count_vulnibm_iot_nameclickjacking_confimpact=0
count_vulnibm_iot_nameclickjacking_highconfimpact=0
count_vulnibm_iot_nameclickjacking_lowconfimpact=0
count_vulnibm_iot_nameclickjacking_mediumconfimpact=0

count_vulnibm_iot_namehijacking=0
count_vulnibm_iot_namehijacking_confimpact=0
count_vulnibm_iot_namehijacking_highconfimpact=0
count_vulnibm_iot_namehijacking_lowconfimpact=0
count_vulnibm_iot_namehijacking_mediumconfimpact=0

count_vulnibm_iot_namefileinclude=0
count_vulnibm_iot_namefileinclude_confimpact=0
count_vulnibm_iot_namefileinclude_highconfimpact=0
count_vulnibm_iot_namefileinclude_lowconfimpact=0
count_vulnibm_iot_namefileinclude_mediumconfimpact=0

count_vulnibm_iot_namebruteforce=0
count_vulnibm_iot_namebruteforce_confimpact=0
count_vulnibm_iot_namebruteforce_highconfimpact=0
count_vulnibm_iot_namebruteforce_lowconfimpact=0
count_vulnibm_iot_namebruteforce_mediumconfimpact=0

count_vulnibm_iot_namefileupload=0
count_vulnibm_iot_namefileupload_confimpact=0
count_vulnibm_iot_namefileupload_highconfimpact=0
count_vulnibm_iot_namefileupload_lowconfimpact=0
count_vulnibm_iot_namefileupload_mediumconfimpact=0

count_vulnibm_iot_nameheaderinjection=0
count_vulnibm_iot_nameheaderinjection_confimpact=0
count_vulnibm_iot_nameheaderinjection_highconfimpact=0
count_vulnibm_iot_nameheaderinjection_lowconfimpact=0
count_vulnibm_iot_nameheaderinjection_mediumconfimpact=0

count_vulnibm_iot_nametampering=0
count_vulnibm_iot_nametampering_confimpact=0
count_vulnibm_iot_nametampering_highconfimpact=0
count_vulnibm_iot_nametampering_lowconfimpact=0
count_vulnibm_iot_nametampering_mediumconfimpact=0

count_vulnibm_iot_nameanother=0
count_vulnibm_iot_nameanother_confimpact=0
count_vulnibm_iot_nameanother_highconfimpact=0
count_vulnibm_iot_nameanother_lowconfimpact=0
count_vulnibm_iot_nameanother_mediumconfimpact=0

#Comprobamos el contenido de name
for r in range(0,len(df_vulnibm_iot["name"])):                       
    aux_str=df_vulnibm_iot["name"][r].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
    if(aux_str!='NONE'):
        count_vulnibm_iot_names+=1
        #Compruebo el valor de nombre
        if('pathtraversal' in aux_str):
            count_vulnibm_iot_namepathtraversal+=1
            #Compruebo el valor de impacto de confidencialidad
            if(df_vulnibm_iot["x_xfe_cvss_confidentiality_impact"][r]=='High'):
                count_vulnibm_iot_namepathtraversal_confimpact+=1
                count_vulnibm_iot_namepathtraversal_highconfimpact+=1
            elif(df_vulnibm_iot["x_xfe_cvss_confidentiality_impact"][r]=='Low'):
                count_vulnibm_iot_namepathtraversal_confimpact+=1
                count_vulnibm_iot_namepathtraversal_lowconfimpact+=1
            elif(df_vulnibm_iot["x_xfe_cvss_confidentiality_impact"][r]=='Medium'):
                count_vulnibm_iot_namepathtraversal_confimpact+=1
                count_vulnibm_iot_namepathtraversal_mediumconfimpact+=1
    
        elif('directorytraversal' in aux_str):
            
            count_vulnibm_iot_namedirectorytraversal+=1
            if(df_vulnibm_iot["x_xfe_cvss_confidentiality_impact"][r]=='High'):
                count_vulnibm_iot_namedirectorytraversal_confimpact+=1
                count_vulnibm_iot_namedirectorytraversal_highconfimpact+=1
            elif(df_vulnibm_iot["x_xfe_cvss_confidentiality_impact"][r]=='Low'):
                count_vulnibm_iot_namedirectorytraversal_confimpact+=1
                count_vulnibm_iot_namedirectorytraversal_lowconfimpact+=1
            elif(df_vulnibm_iot["x_xfe_cvss_confidentiality_impact"][r]=='Medium'):
                count_vulnibm_iot_namedirectorytraversal_confimpact+=1
                count_vulnibm_iot_namedirectorytraversal_mediumconfimpact+=1
            
            
        elif('privilegeescalation' in aux_str):
        
            count_vulnibm_iot_nameprivilegeescalation+=1
            if(df_vulnibm_iot["x_xfe_cvss_confidentiality_impact"][r]=='High'):
                count_vulnibm_iot_nameprivilegeescalation_confimpact+=1
                count_vulnibm_iot_nameprivilegeescalation_highconfimpact+=1
            elif(df_vulnibm_iot["x_xfe_cvss_confidentiality_impact"][r]=='Low'):
                count_vulnibm_iot_nameprivilegeescalation_confimpact+=1
                count_vulnibm_iot_nameprivilegeescalation_lowconfimpact+=1
            elif(df_vulnibm_iot["x_xfe_cvss_confidentiality_impact"][r]=='Medium'):
                count_vulnibm_iot_nameprivilegeescalation_confimpact+=1
                count_vulnibm_iot_nameprivilegeescalation_mediumconfimpact+=1
            
        elif('cross-sitescripting' in aux_str):
        
            count_vulnibm_iot_namecrosssitescripting+=1
            if(df_vulnibm_iot["x_xfe_cvss_confidentiality_impact"][r]=='High'):
                count_vulnibm_iot_namecrosssitescripting_confimpact+=1
                count_vulnibm_iot_namecrosssitescripting_highconfimpact+=1
            elif(df_vulnibm_iot["x_xfe_cvss_confidentiality_impact"][r]=='Low'):
                count_vulnibm_iot_namecrosssitescripting_confimpact+=1
                count_vulnibm_iot_namecrosssitescripting_lowconfimpact+=1
            elif(df_vulnibm_iot["x_xfe_cvss_confidentiality_impact"][r]=='Medium'):
                count_vulnibm_iot_namecrosssitescripting_confimpact+=1
                count_vulnibm_iot_namecrosssitescripting_mediumconfimpact+=1
                                         
        elif('securitybypass' in aux_str):
        
            count_vulnibm_iot_namesecuritybypass+=1
            if(df_vulnibm_iot["x_xfe_cvss_confidentiality_impact"][r]=='High'):
                count_vulnibm_iot_namesecuritybypass_confimpact+=1
                count_vulnibm_iot_namesecuritybypass_highconfimpact+=1
            elif(df_vulnibm_iot["x_xfe_cvss_confidentiality_impact"][r]=='Low'):
                count_vulnibm_iot_namesecuritybypass_confimpact+=1
                count_vulnibm_iot_namesecuritybypass_lowconfimpact+=1
            elif(df_vulnibm_iot["x_xfe_cvss_confidentiality_impact"][r]=='Medium'):
                count_vulnibm_iot_namesecuritybypass_confimpact+=1
                count_vulnibm_iot_namesecuritybypass_mediumconfimpact+=1
                                         
        elif('information_disclosure' in aux_str or 'informationdisclosure' in aux_str):
        
            count_vulnibm_iot_nameinformationdisclosure+=1
            if(df_vulnibm_iot["x_xfe_cvss_confidentiality_impact"][r]=='High'):
                count_vulnibm_iot_nameinformationdisclosure_confimpact+=1
                count_vulnibm_iot_nameinformationdisclosure_highconfimpact+=1
            elif(df_vulnibm_iot["x_xfe_cvss_confidentiality_impact"][r]=='Low'):
                count_vulnibm_iot_nameinformationdisclosure_confimpact+=1
                count_vulnibm_iot_nameinformationdisclosure_lowconfimpact+=1
            elif(df_vulnibm_iot["x_xfe_cvss_confidentiality_impact"][r]=='Medium'):
                count_vulnibm_iot_nameinformationdisclosure_confimpact+=1
                count_vulnibm_iot_nameinformationdisclosure_mediumconfimpact+=1
                                         
        elif('denialofservice' in aux_str):
            
            count_vulnibm_iot_namedenialofservice+=1
            if(df_vulnibm_iot["x_xfe_cvss_confidentiality_impact"][r]=='High'):
                count_vulnibm_iot_namedenialofservice_confimpact+=1
                count_vulnibm_iot_namedenialofservice_highconfimpact+=1
            elif(df_vulnibm_iot["x_xfe_cvss_confidentiality_impact"][r]=='Low'):
                count_vulnibm_iot_namedenialofservice_confimpact+=1
                count_vulnibm_iot_namedenialofservice_lowconfimpact+=1
            elif(df_vulnibm_iot["x_xfe_cvss_confidentiality_impact"][r]=='Medium'):
                count_vulnibm_iot_namedenialofservice_confimpact+=1
                count_vulnibm_iot_namedenialofservice_mediumconfimpact+=1
            
        elif('codeexecution' in aux_str):
        
        
            count_vulnibm_iot_namecodeexecution+=1
            if(df_vulnibm_iot["x_xfe_cvss_confidentiality_impact"][r]=='High'):
                count_vulnibm_iot_namecodeexecution_confimpact+=1
                count_vulnibm_iot_namecodeexecution_highconfimpact+=1
            elif(df_vulnibm_iot["x_xfe_cvss_confidentiality_impact"][r]=='Low'):
                count_vulnibm_iot_namecodeexecution_confimpact+=1
                count_vulnibm_iot_namecodeexecution_lowconfimpact+=1
            elif(df_vulnibm_iot["x_xfe_cvss_confidentiality_impact"][r]=='Medium'):
                count_vulnibm_iot_namecodeexecution_confimpact+=1
                count_vulnibm_iot_namecodeexecution_mediumconfimpact+=1
                                         
        elif('maninthemiddle' in aux_str):
        
            count_vulnibm_iot_namemaninthemiddle+=1
            if(df_vulnibm_iot["x_xfe_cvss_confidentiality_impact"][r]=='High'):
                count_vulnibm_iot_namemaninthemiddle_confimpact+=1
                count_vulnibm_iot_namemaninthemiddle_highconfimpact+=1
            elif(df_vulnibm_iot["x_xfe_cvss_confidentiality_impact"][r]=='Low'):
                count_vulnibm_iot_namemaninthemiddle_confimpact+=1
                count_vulnibm_iot_namemaninthemiddle_lowconfimpact+=1
            elif(df_vulnibm_iot["x_xfe_cvss_confidentiality_impact"][r]=='Medium'):
                count_vulnibm_iot_namemaninthemiddle_confimpact+=1
                count_vulnibm_iot_namemaninthemiddle_mediumconfimpact+=1
                                         
        elif('SQLinjection' in aux_str):
        
            count_vulnibm_iot_namesqlinjection+=1
            if(df_vulnibm_iot["x_xfe_cvss_confidentiality_impact"][r]=='High'):
                count_vulnibm_iot_namesqlinjection_confimpact+=1
                count_vulnibm_iot_namesqlinjection_highconfimpact+=1
            elif(df_vulnibm_iot["x_xfe_cvss_confidentiality_impact"][r]=='Low'):
                count_vulnibm_iot_namesqlinjection_confimpact+=1
                count_vulnibm_iot_namesqlinjection_lowconfimpact+=1
            elif(df_vulnibm_iot["x_xfe_cvss_confidentiality_impact"][r]=='Medium'):
                count_vulnibm_iot_namesqlinjection_confimpact+=1
                count_vulnibm_iot_namesqlinjection_mediumconfimpact+=1
                                         
        elif('cross-siterequestforgery' in aux_str):
        
            count_vulnibm_iot_namecrosssiterequestforgery+=1
            if(df_vulnibm_iot["x_xfe_cvss_confidentiality_impact"][r]=='High'):
                count_vulnibm_iot_namecrosssiterequestforgery_confimpact+=1
                count_vulnibm_iot_namecrosssiterequestforgery_highconfimpact+=1
            elif(df_vulnibm_iot["x_xfe_cvss_confidentiality_impact"][r]=='Low'):
                count_vulnibm_iot_namecrosssiterequestforgery_confimpact+=1
                count_vulnibm_iot_namecrosssiterequestforgery_lowconfimpact+=1
            elif(df_vulnibm_iot["x_xfe_cvss_confidentiality_impact"][r]=='Medium'):
                count_vulnibm_iot_namecrosssiterequestforgery_confimpact+=1
                count_vulnibm_iot_namecrosssiterequestforgery_mediumconfimpact+=1
                                         
        elif('moduleexecution' in aux_str):
        
            count_vulnibm_iot_namemoduleexecution+=1
            if(df_vulnibm_iot["x_xfe_cvss_confidentiality_impact"][r]=='High'):
                count_vulnibm_iot_namemoduleexecution_confimpact+=1
                count_vulnibm_iot_namemoduleexecution_highconfimpact+=1
            elif(df_vulnibm_iot["x_xfe_cvss_confidentiality_impact"][r]=='Low'):
                count_vulnibm_iot_namemoduleexecution_confimpact+=1
                count_vulnibm_iot_namemoduleexecution_lowconfimpact+=1
            elif(df_vulnibm_iot["x_xfe_cvss_confidentiality_impact"][r]=='Medium'):
                count_vulnibm_iot_namemoduleexecution_confimpact+=1
                count_vulnibm_iot_namemoduleexecution_mediumconfimpact+=1
                                         
        elif('bufferoverflow' in aux_str):
        
            count_vulnibm_iot_namebufferoverflow+=1
            if(df_vulnibm_iot["x_xfe_cvss_confidentiality_impact"][r]=='High'):
                count_vulnibm_iot_namebufferoverflow_confimpact+=1
                count_vulnibm_iot_namebufferoverflow_highconfimpact+=1
            elif(df_vulnibm_iot["x_xfe_cvss_confidentiality_impact"][r]=='Low'):
                count_vulnibm_iot_namebufferoverflow_confimpact+=1
                count_vulnibm_iot_namebufferoverflow_lowconfimpact+=1
            elif(df_vulnibm_iot["x_xfe_cvss_confidentiality_impact"][r]=='Medium'):
                count_vulnibm_iot_namebufferoverflow_confimpact+=1
                count_vulnibm_iot_namebufferoverflow_mediumconfimpact+=1
                                         
        elif('commandexecution' in aux_str):
        
            count_vulnibm_iot_namecommandexecution+=1
            if(df_vulnibm_iot["x_xfe_cvss_confidentiality_impact"][r]=='High'):
                count_vulnibm_iot_namecommandexecution_confimpact+=1
                count_vulnibm_iot_namecommandexecution_highconfimpact+=1
            elif(df_vulnibm_iot["x_xfe_cvss_confidentiality_impact"][r]=='Low'):
                count_vulnibm_iot_namecommandexecution_confimpact+=1
                count_vulnibm_iot_namecommandexecution_lowconfimpact+=1
            elif(df_vulnibm_iot["x_xfe_cvss_confidentiality_impact"][r]=='Medium'):
                count_vulnibm_iot_namecommandexecution_confimpact+=1
                count_vulnibm_iot_namecommandexecution_mediumconfimpact+=1
                                         
        elif('spoofing' in aux_str):
        
            count_vulnibm_iot_namespoofing+=1
            if(df_vulnibm_iot["x_xfe_cvss_confidentiality_impact"][r]=='High'):
                count_vulnibm_iot_namespoofing_confimpact+=1
                count_vulnibm_iot_namespoofing_highconfimpact+=1
            elif(df_vulnibm_iot["x_xfe_cvss_confidentiality_impact"][r]=='Low'):
                count_vulnibm_iot_namespoofing_confimpact+=1
                count_vulnibm_iot_namespoofing_lowconfimpact+=1
            elif(df_vulnibm_iot["x_xfe_cvss_confidentiality_impact"][r]=='Medium'):
                count_vulnibm_iot_namespoofing_confimpact+=1
                count_vulnibm_iot_namespoofing_mediumconfimpact+=1
                                         
        elif('clickjacking' in aux_str):
        
            count_vulnibm_iot_nameclickjacking+=1
            if(df_vulnibm_iot["x_xfe_cvss_confidentiality_impact"][r]=='High'):
                count_vulnibm_iot_nameclickjacking_confimpact+=1
                count_vulnibm_iot_nameclickjacking_highconfimpact+=1
            elif(df_vulnibm_iot["x_xfe_cvss_confidentiality_impact"][r]=='Low'):
                count_vulnibm_iot_nameclickjacking_confimpact+=1
                count_vulnibm_iot_nameclickjacking_lowconfimpact+=1
            elif(df_vulnibm_iot["x_xfe_cvss_confidentiality_impact"][r]=='Medium'):
                count_vulnibm_iot_nameclickjacking_confimpact+=1
                count_vulnibm_iot_nameclickjacking_mediumconfimpact+=1
              
        elif('hijacking' in aux_str):
        
            count_vulnibm_iot_namehijacking+=1
            if(df_vulnibm_iot["x_xfe_cvss_confidentiality_impact"][r]=='High'):
                count_vulnibm_iot_namehijacking_confimpact+=1
                count_vulnibm_iot_namehijacking_highconfimpact+=1
            elif(df_vulnibm_iot["x_xfe_cvss_confidentiality_impact"][r]=='Low'):
                count_vulnibm_iot_namehijacking_confimpact+=1
                count_vulnibm_iot_namehijacking_lowconfimpact+=1
            elif(df_vulnibm_iot["x_xfe_cvss_confidentiality_impact"][r]=='Medium'):
                count_vulnibm_iot_namehijacking_confimpact+=1
                count_vulnibm_iot_namehijacking_mediumconfimpact+=1
               
        elif('fileinclude' in aux_str):
        
            count_vulnibm_iot_namefileinclude+=1
            if(df_vulnibm_iot["x_xfe_cvss_confidentiality_impact"][r]=='High'):
                count_vulnibm_iot_namefileinclude_confimpact+=1
                count_vulnibm_iot_namefileinclude_highconfimpact+=1
            elif(df_vulnibm_iot["x_xfe_cvss_confidentiality_impact"][r]=='Low'):
                count_vulnibm_iot_namefileinclude_confimpact+=1
                count_vulnibm_iot_namefileinclude_lowconfimpact+=1
            elif(df_vulnibm_iot["x_xfe_cvss_confidentiality_impact"][r]=='Medium'):
                count_vulnibm_iot_namefileinclude_confimpact+=1
                count_vulnibm_iot_namefileinclude_mediumconfimpact+=1
                
               
        elif('bruteforce' in aux_str):
        
            count_vulnibm_iot_namebruteforce+=1
            if(df_vulnibm_iot["x_xfe_cvss_confidentiality_impact"][r]=='High'):
                count_vulnibm_iot_namebruteforce_confimpact+=1
                count_vulnibm_iot_namebruteforce_highconfimpact+=1
            elif(df_vulnibm_iot["x_xfe_cvss_confidentiality_impact"][r]=='Low'):
                count_vulnibm_iot_namebruteforce_confimpact+=1
                count_vulnibm_iot_namebruteforce_lowconfimpact+=1
            elif(df_vulnibm_iot["x_xfe_cvss_confidentiality_impact"][r]=='Medium'):
                count_vulnibm_iot_namebruteforce_confimpact+=1
                count_vulnibm_iot_namebruteforce_mediumconfimpact+=1
                
               
        elif('fileupload' in aux_str):
        
            count_vulnibm_iot_namefileupload+=1
            if(df_vulnibm_iot["x_xfe_cvss_confidentiality_impact"][r]=='High'):
                count_vulnibm_iot_namefileupload_confimpact+=1
                count_vulnibm_iot_namefileupload_highconfimpact+=1
            elif(df_vulnibm_iot["x_xfe_cvss_confidentiality_impact"][r]=='Low'):
                count_vulnibm_iot_namefileupload_confimpact+=1
                count_vulnibm_iot_namefileupload_lowconfimpact+=1
            elif(df_vulnibm_iot["x_xfe_cvss_confidentiality_impact"][r]=='Medium'):
                count_vulnibm_iot_namefileupload_confimpact+=1
                count_vulnibm_iot_namefileupload_mediumconfimpact+=1
                
               
        elif('headerinjection' in aux_str):
        
            count_vulnibm_iot_nameheaderinjection+=1
            if(df_vulnibm_iot["x_xfe_cvss_confidentiality_impact"][r]=='High'):
                count_vulnibm_iot_nameheaderinjection_confimpact+=1
                count_vulnibm_iot_nameheaderinjection_highconfimpact+=1
            elif(df_vulnibm_iot["x_xfe_cvss_confidentiality_impact"][r]=='Low'):
                count_vulnibm_iot_nameheaderinjection_confimpact+=1
                count_vulnibm_iot_nameheaderinjection_lowconfimpact+=1
            elif(df_vulnibm_iot["x_xfe_cvss_confidentiality_impact"][r]=='Medium'):
                count_vulnibm_iot_nameheaderinjection_confimpact+=1
                count_vulnibm_iot_nameheaderinjection_mediumconfimpact+=1
               
        elif('Tampering' in aux_str):
        
            count_vulnibm_iot_nametampering+=1
            if(df_vulnibm_iot["x_xfe_cvss_confidentiality_impact"][r]=='High'):
                count_vulnibm_iot_nametampering_confimpact+=1
                count_vulnibm_iot_nametampering_highconfimpact+=1
            elif(df_vulnibm_iot["x_xfe_cvss_confidentiality_impact"][r]=='Low'):
                count_vulnibm_iot_nametampering_confimpact+=1
                count_vulnibm_iot_nametampering_lowconfimpact+=1
            elif(df_vulnibm_iot["x_xfe_cvss_confidentiality_impact"][r]=='Medium'):
                count_vulnibm_iot_nametampering_confimpact+=1
                count_vulnibm_iot_nametampering_mediumconfimpact+=1
    
        else:
        
            count_vulnibm_iot_nameanother+=1
            if(df_vulnibm_iot["x_xfe_cvss_confidentiality_impact"][r]=='High'):
                count_vulnibm_iot_nameanother_confimpact+=1
                count_vulnibm_iot_nameanother_highconfimpact+=1
            elif(df_vulnibm_iot["x_xfe_cvss_confidentiality_impact"][r]=='Low'):
                count_vulnibm_iot_nameanother_confimpact+=1
                count_vulnibm_iot_nameanother_lowconfimpact+=1
            elif(df_vulnibm_iot["x_xfe_cvss_confidentiality_impact"][r]=='Medium'):
                count_vulnibm_iot_nameanother_confimpact+=1
                count_vulnibm_iot_nameanother_mediumconfimpact+=1
                
                
                
                
                
print("**********************************************ESTADÍSTICAS NOMBRE/IMPACTO DE CONFIDENCIALIDAD VULNERABILIDADES IBM PARTE IOT**********************************************")
print("\n")                            
print("\n")
print(" DE UN TOTAL DE "+str(count_vulnibm_iot_names)+" VULNERABILIDADES:\n") 
print("\n")
print("   - LAS ESTADISTICAS DE VALORES DE NOMBRE SON LAS SIGUIENTES:  \n")
print("      -    EN  "+str(count_vulnibm_iot_namepathtraversal)+" VULNERABILIDADES EL NOMBRE INCLUYE PATH TRAVERSAL, LAS ESTADÍSTICAS DE IMPACTO DE CONFIDENCIALIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_namepathtraversal_highconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_iot_namepathtraversal_lowconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_iot_namepathtraversal_mediumconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO\n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_namedirectorytraversal)+" VULNERABILIDADES EL NOMBRE INCLUYE DIRECTORY TRAVERSAL, LAS ESTADÍSTICAS DE IMPACTO DE CONFIDENCIALIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_namedirectorytraversal_highconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_iot_namedirectorytraversal_lowconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_iot_namedirectorytraversal_mediumconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO\n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_nameprivilegeescalation)+" VULNERABILIDADES EL NOMBRE INCLUYE PRIVILEGE ESCALATION, LAS ESTADÍSTICAS DE IMPACTO DE CONFIDENCIALIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_nameprivilegeescalation_highconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_iot_nameprivilegeescalation_lowconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_iot_nameprivilegeescalation_mediumconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO\n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_namecrosssitescripting)+" VULNERABILIDADES EL NOMBRE INCLUYE CROSS SITE SCRIPTING, LAS ESTADÍSTICAS DE IMPACTO DE CONFIDENCIALIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_namecrosssitescripting_highconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_iot_namecrosssitescripting_lowconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_iot_namecrosssitescripting_mediumconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO\n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_namesecuritybypass)+" VULNERABILIDADES EL NOMBRE INCLUYE SECURITY BYPASS, LAS ESTADÍSTICAS DE IMPACTO DE CONFIDENCIALIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_namesecuritybypass_highconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_iot_namesecuritybypass_lowconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_iot_namesecuritybypass_mediumconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO\n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_nameinformationdisclosure)+" VULNERABILIDADES EL NOMBRE INCLUYE INFORMATION DISCLOSURE, LAS ESTADÍSTICAS DE IMPACTO DE CONFIDENCIALIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_nameinformationdisclosure_highconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_iot_nameinformationdisclosure_lowconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_iot_nameinformationdisclosure_mediumconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO\n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_namedenialofservice)+" VULNERABILIDADES EL NOMBRE INCLUYE DENIAL OF SERVICE, LAS ESTADÍSTICAS DE IMPACTO DE CONFIDENCIALIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_namedenialofservice_highconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_iot_namedenialofservice_lowconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_iot_namedenialofservice_mediumconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO\n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_namecodeexecution)+" VULNERABILIDADES EL NOMBRE INCLUYE CODE EXECUTION, LAS ESTADÍSTICAS DE IMPACTO DE CONFIDENCIALIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_namecodeexecution_highconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_iot_namecodeexecution_lowconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_iot_namecodeexecution_mediumconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO\n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_namemaninthemiddle)+" VULNERABILIDADES EL NOMBRE INCLUYE MAN IN THE MIDDLE, LAS ESTADÍSTICAS DE IMPACTO DE CONFIDENCIALIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_namemaninthemiddle_highconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_iot_namemaninthemiddle_lowconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_iot_namemaninthemiddle_mediumconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO\n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_namesqlinjection)+" VULNERABILIDADES EL NOMBRE INCLUYE SQL INJECTION, LAS ESTADÍSTICAS DE IMPACTO DE CONFIDENCIALIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_namesqlinjection_highconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_iot_namesqlinjection_lowconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_iot_namesqlinjection_mediumconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO\n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_namecrosssiterequestforgery)+" VULNERABILIDADES EL NOMBRE INCLUYE CROSS SITE REQUEST FORGERY, LAS ESTADÍSTICAS DE IMPACTO DE CONFIDENCIALIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_namecrosssiterequestforgery_highconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_iot_namecrosssiterequestforgery_lowconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_iot_namecrosssiterequestforgery_mediumconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO\n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_namemoduleexecution)+" VULNERABILIDADES EL NOMBRE INCLUYE MODULE EXECUTION, LAS ESTADÍSTICAS DE IMPACTO DE CONFIDENCIALIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_namemoduleexecution_highconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_iot_namemoduleexecution_lowconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_iot_namemoduleexecution_mediumconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO\n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_namebufferoverflow)+" VULNERABILIDADES EL NOMBRE INCLUYE BUFFER OVERFLOW, LAS ESTADÍSTICAS DE IMPACTO DE CONFIDENCIALIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_namebufferoverflow_highconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_iot_namebufferoverflow_lowconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_iot_namebufferoverflow_mediumconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO\n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_namecommandexecution)+" VULNERABILIDADES EL NOMBRE INCLUYE COMMAND EXECUTION, LAS ESTADÍSTICAS DE IMPACTO DE CONFIDENCIALIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_namecommandexecution_highconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_iot_namecommandexecution_lowconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_iot_namecommandexecution_mediumconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO\n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_namespoofing)+" VULNERABILIDADES EL NOMBRE INCLUYE SPOOFING, LAS ESTADÍSTICAS DE IMPACTO DE CONFIDENCIALIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_namespoofing_highconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_iot_namespoofing_lowconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_iot_namespoofing_mediumconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO\n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_nameclickjacking)+" VULNERABILIDADES EL NOMBRE INCLUYE CLICKJACKING, LAS ESTADÍSTICAS DE IMPACTO DE CONFIDENCIALIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_nameclickjacking_highconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_iot_nameclickjacking_lowconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_iot_nameclickjacking_mediumconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO\n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_namehijacking)+" VULNERABILIDADES EL NOMBRE INCLUYE HIJACKING, LAS ESTADÍSTICAS DE IMPACTO DE CONFIDENCIALIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_namehijacking_highconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_iot_namehijacking_lowconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_iot_namehijacking_mediumconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO\n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_namefileinclude)+" VULNERABILIDADES EL NOMBRE INCLUYE FILEINCLUDE, LAS ESTADÍSTICAS DE IMPACTO DE CONFIDENCIALIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_namefileinclude_highconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_iot_namefileinclude_lowconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_iot_namefileinclude_mediumconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO\n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_namebruteforce)+" VULNERABILIDADES EL NOMBRE INCLUYE BRUTEFORCE, LAS ESTADÍSTICAS DE IMPACTO DE CONFIDENCIALIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_namebruteforce_highconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_iot_namebruteforce_lowconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_iot_namebruteforce_mediumconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO\n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_namefileupload)+" VULNERABILIDADES EL NOMBRE INCLUYE FILE UPLOAD, LAS ESTADÍSTICAS DE IMPACTO DE CONFIDENCIALIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_namefileupload_highconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_iot_namefileupload_lowconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_iot_namefileupload_mediumconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO\n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_nameheaderinjection)+" VULNERABILIDADES EL NOMBRE INCLUYE HEADER INJECTION, LAS ESTADÍSTICAS DE IMPACTO DE CONFIDENCIALIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_nameheaderinjection_highconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_iot_nameheaderinjection_lowconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_iot_nameheaderinjection_mediumconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO\n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_nametampering)+" VULNERABILIDADES EL NOMBRE INCLUYE TAMPERING, LAS ESTADÍSTICAS DE IMPACTO DE CONFIDENCIALIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_nametampering_highconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_iot_nametampering_lowconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_iot_nametampering_mediumconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO\n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_nameanother)+" VULNERABILIDADES EL NOMBRE INCLUYE OTRA CADENA, LAS ESTADÍSTICAS DE IMPACTO DE CONFIDENCIALIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_nameanother_highconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_iot_nameanother_lowconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_iot_nameanother_mediumconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO\n")
print("\n")





print("**********************************************PORCENTAJE NOMBRE/IMPACTO DE CONFIDENCIALIDAD VULNERABILIDADES IBM PARTE IOT**********************************************")
print("\n")                            
print("\n")
print(" DE UN TOTAL DE "+str(count_vulnibm_iot_names)+" VULNERABILIDADES :\n") 
print("\n")
print("   - LOS PORCENTAJES DE VALORES DE NOMBRE SON LOS SIGUIENTES:  \n")
print("      -    EN EL  "+str(float(((count_vulnibm_iot_namepathtraversal*100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE PATH TRAVERSAL, LOS PORCENTAJES DE IMPACTO DE CONFIDENCIALIDAD SON LOS SIGUIENTES :  \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namepathtraversal_highconfimpact*100)/count_vulnibm_iot_namepathtraversal)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namepathtraversal_lowconfimpact*100)/count_vulnibm_iot_namepathtraversal)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namepathtraversal_mediumconfimpact*100)/count_vulnibm_iot_namepathtraversal)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO\n")
print("\n")
print("      -    EN EL  "+str(float(((count_vulnibm_iot_namedirectorytraversal*100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE DIRECTORY TRAVERSAL, LOS PORCENTAJES DE IMPACTO DE CONFIDENCIALIDAD SON LOS SIGUIENTES :  \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namedirectorytraversal_highconfimpact*100)/count_vulnibm_iot_namedirectorytraversal)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namedirectorytraversal_lowconfimpact*100)/count_vulnibm_iot_namedirectorytraversal)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namedirectorytraversal_mediumconfimpact*100)/count_vulnibm_iot_namedirectorytraversal)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO\n")
print("\n")
print("      -    EN EL  "+str(float(((count_vulnibm_iot_nameprivilegeescalation*100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE PRIVILEGE ESCALATION, LOS PORCENTAJES DE IMPACTO DE CONFIDENCIALIDAD SON LOS SIGUIENTES :  \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_nameprivilegeescalation_highconfimpact*100)/count_vulnibm_iot_nameprivilegeescalation)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_nameprivilegeescalation_lowconfimpact*100)/count_vulnibm_iot_nameprivilegeescalation)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_nameprivilegeescalation_mediumconfimpact*100)/count_vulnibm_iot_nameprivilegeescalation)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO\n")
print("\n")
print("      -    EN EL  "+str(float(((count_vulnibm_iot_namecrosssitescripting*100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE CROSS SITE SCRIPTING, LOS PORCENTAJES DE IMPACTO DE CONFIDENCIALIDAD SON LOS SIGUIENTES :  \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namecrosssitescripting_highconfimpact*100)/count_vulnibm_iot_namecrosssitescripting)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namecrosssitescripting_lowconfimpact*100)/count_vulnibm_iot_namecrosssitescripting)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namecrosssitescripting_mediumconfimpact*100)/count_vulnibm_iot_namecrosssitescripting)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO\n")
print("\n")
print("      -    EN EL  "+str(float(((count_vulnibm_iot_namesecuritybypass*100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE SECURITY BYPASS, LOS PORCENTAJES DE IMPACTO DE CONFIDENCIALIDAD SON LOS SIGUIENTES :  \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namesecuritybypass_highconfimpact*100)/count_vulnibm_iot_namesecuritybypass)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namesecuritybypass_lowconfimpact*100)/count_vulnibm_iot_namesecuritybypass)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namesecuritybypass_mediumconfimpact*100)/count_vulnibm_iot_namesecuritybypass)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO\n")
print("\n")
print("      -    EN EL  "+str(float(((count_vulnibm_iot_nameinformationdisclosure*100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE INFORMATION DISCLOSURE, LOS PORCENTAJES DE IMPACTO DE CONFIDENCIALIDAD SON LOS SIGUIENTES :  \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_nameinformationdisclosure_highconfimpact*100)/count_vulnibm_iot_nameinformationdisclosure)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_nameinformationdisclosure_lowconfimpact*100)/count_vulnibm_iot_nameinformationdisclosure)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_nameinformationdisclosure_mediumconfimpact*100)/count_vulnibm_iot_nameinformationdisclosure)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO\n")
print("\n")
print("      -    EN EL  "+str(float(((count_vulnibm_iot_namedenialofservice*100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE DENIAL OF SERVICE, LOS PORCENTAJES DE IMPACTO DE CONFIDENCIALIDAD SON LOS SIGUIENTES :  \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namedenialofservice_highconfimpact*100)/count_vulnibm_iot_namedenialofservice)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namedenialofservice_lowconfimpact*100)/count_vulnibm_iot_namedenialofservice)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namedenialofservice_mediumconfimpact*100)/count_vulnibm_iot_namedenialofservice)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO\n")
print("\n")
print("      -    EN EL  "+str(float(((count_vulnibm_iot_namecodeexecution*100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE CODE EXECUTION, LOS PORCENTAJES DE IMPACTO DE CONFIDENCIALIDAD SON LOS SIGUIENTES :  \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namecodeexecution_highconfimpact*100)/count_vulnibm_iot_namecodeexecution)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namecodeexecution_lowconfimpact*100)/count_vulnibm_iot_namecodeexecution)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namecodeexecution_mediumconfimpact*100)/count_vulnibm_iot_namecodeexecution)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO\n")
print("\n")
print("      -    EN EL  "+str(float(((count_vulnibm_iot_namemaninthemiddle*100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE MAN IN THE MIDDLE, LOS PORCENTAJES DE IMPACTO DE CONFIDENCIALIDAD SON LOS SIGUIENTES :  \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namemaninthemiddle_highconfimpact*100)/count_vulnibm_iot_namemaninthemiddle)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namemaninthemiddle_lowconfimpact*100)/count_vulnibm_iot_namemaninthemiddle)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namemaninthemiddle_mediumconfimpact*100)/count_vulnibm_iot_namemaninthemiddle)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO\n")
print("\n")
print("      -    EN EL  "+str(float(((count_vulnibm_iot_namesqlinjection*100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE SQL INJECTION, LOS PORCENTAJES DE IMPACTO DE CONFIDENCIALIDAD SON LOS SIGUIENTES :  \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namesqlinjection_highconfimpact*100)/count_vulnibm_iot_namesqlinjection)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namesqlinjection_lowconfimpact*100)/count_vulnibm_iot_namesqlinjection)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namesqlinjection_mediumconfimpact*100)/count_vulnibm_iot_namesqlinjection)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO\n")
print("\n")
print("      -    EN EL  "+str(float(((count_vulnibm_iot_namecrosssiterequestforgery*100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE CROSS SITE REQUEST FORGERY, LOS PORCENTAJES DE IMPACTO DE CONFIDENCIALIDAD SON LOS SIGUIENTES :  \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namecrosssiterequestforgery_highconfimpact*100)/count_vulnibm_iot_namecrosssiterequestforgery)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namecrosssiterequestforgery_lowconfimpact*100)/count_vulnibm_iot_namecrosssiterequestforgery)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namecrosssiterequestforgery_mediumconfimpact*100)/count_vulnibm_iot_namecrosssiterequestforgery)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO\n")
print("\n")
print("      -    EN EL  "+str(float(((count_vulnibm_iot_namemoduleexecution*100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE MODULE EXECUTION, LOS PORCENTAJES DE IMPACTO DE CONFIDENCIALIDAD SON LOS SIGUIENTES :  \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namemoduleexecution_highconfimpact*100)/count_vulnibm_iot_namemoduleexecution)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namemoduleexecution_lowconfimpact*100)/count_vulnibm_iot_namemoduleexecution)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namemoduleexecution_mediumconfimpact*100)/count_vulnibm_iot_namemoduleexecution)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO\n")
print("\n")
print("      -    EN EL  "+str(float(((count_vulnibm_iot_namebufferoverflow*100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE BUFFER OVERFLOW, LOS PORCENTAJES DE IMPACTO DE CONFIDENCIALIDAD SON LOS SIGUIENTES :  \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namebufferoverflow_highconfimpact*100)/count_vulnibm_iot_namebufferoverflow)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namebufferoverflow_lowconfimpact*100)/count_vulnibm_iot_namebufferoverflow)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namebufferoverflow_mediumconfimpact*100)/count_vulnibm_iot_namebufferoverflow)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO\n")
print("\n")
print("      -    EN EL  "+str(float(((count_vulnibm_iot_namecommandexecution*100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE COMMAND EXECUTION, LOS PORCENTAJES DE IMPACTO DE CONFIDENCIALIDAD SON LOS SIGUIENTES :  \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namecommandexecution_highconfimpact*100)/count_vulnibm_iot_namecommandexecution)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namecommandexecution_lowconfimpact*100)/count_vulnibm_iot_namecommandexecution)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namecommandexecution_mediumconfimpact*100)/count_vulnibm_iot_namecommandexecution)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO\n")
print("\n")
print("      -    EN EL  "+str(float(((count_vulnibm_iot_namespoofing*100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE SPOOFING, LOS PORCENTAJES DE IMPACTO DE CONFIDENCIALIDAD SON LOS SIGUIENTES :  \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namespoofing_highconfimpact*100)/count_vulnibm_iot_namespoofing)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namespoofing_lowconfimpact*100)/count_vulnibm_iot_namespoofing)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namespoofing_mediumconfimpact*100)/count_vulnibm_iot_namespoofing)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO\n")
print("\n")
print("      -    EN EL  "+str(float(((count_vulnibm_iot_nameclickjacking*100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE CLICKJACKING, LOS PORCENTAJES DE IMPACTO DE CONFIDENCIALIDAD SON LOS SIGUIENTES :  \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_nameclickjacking_highconfimpact*100)/count_vulnibm_iot_nameclickjacking)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_nameclickjacking_lowconfimpact*100)/count_vulnibm_iot_nameclickjacking)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_nameclickjacking_mediumconfimpact*100)/count_vulnibm_iot_nameclickjacking)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO\n")
print("\n")
print("      -    EN EL  "+str(float(((count_vulnibm_iot_namehijacking*100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE HIJACKING, LOS PORCENTAJES DE IMPACTO DE CONFIDENCIALIDAD SON LOS SIGUIENTES :  \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namehijacking_highconfimpact*100)/count_vulnibm_iot_namehijacking)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namehijacking_lowconfimpact*100)/count_vulnibm_iot_namehijacking)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namehijacking_mediumconfimpact*100)/count_vulnibm_iot_namehijacking)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO\n")
print("\n")
print("      -    EN EL  "+str(float(((count_vulnibm_iot_namefileinclude*100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE FILEINCLUDE, LOS PORCENTAJES DE IMPACTO DE CONFIDENCIALIDAD SON LOS SIGUIENTES :  \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namefileinclude_highconfimpact*100)/count_vulnibm_iot_namefileinclude)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namefileinclude_lowconfimpact*100)/count_vulnibm_iot_namefileinclude)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namefileinclude_mediumconfimpact*100)/count_vulnibm_iot_namefileinclude)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO\n")
print("\n")
print("      -    EN EL  "+str(float(((count_vulnibm_iot_namebruteforce*100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE BRUTEFORCE, LOS PORCENTAJES DE IMPACTO DE CONFIDENCIALIDAD SON LOS SIGUIENTES :  \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namebruteforce_highconfimpact*100)/count_vulnibm_iot_namebruteforce)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namebruteforce_lowconfimpact*100)/count_vulnibm_iot_namebruteforce)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namebruteforce_mediumconfimpact*100)/count_vulnibm_iot_namebruteforce)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO\n")
print("\n")
print("      -    EN EL  "+str(float(((count_vulnibm_iot_namefileupload*100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE FILE UPLOAD, LOS PORCENTAJES DE IMPACTO DE CONFIDENCIALIDAD SON LOS SIGUIENTES :  \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namefileupload_highconfimpact*100)/count_vulnibm_iot_namefileupload)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namefileupload_lowconfimpact*100)/count_vulnibm_iot_namefileupload)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namefileupload_mediumconfimpact*100)/count_vulnibm_iot_namefileupload)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO\n")
print("\n")
if(count_vulnibm_iot_nameheaderinjection>0):
    print("      -    EN EL  "+str(float(((count_vulnibm_iot_nameheaderinjection*100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE HEADER INJECTION, LOS PORCENTAJES DE IMPACTO DE CONFIDENCIALIDAD SON LOS SIGUIENTES :  \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_nameheaderinjection_highconfimpact*100)/count_vulnibm_iot_nameheaderinjection)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_nameheaderinjection_lowconfimpact*100)/count_vulnibm_iot_nameheaderinjection)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_nameheaderinjection_mediumconfimpact*100)/count_vulnibm_iot_nameheaderinjection)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO\n")
    print("\n")
if(count_vulnibm_iot_nametampering>0):
    print("      -    EN EL  "+str(float(((count_vulnibm_iot_nametampering*100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE TAMPERING, LOS PORCENTAJES DE IMPACTO DE CONFIDENCIALIDAD SON LOS SIGUIENTES :  \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_nametampering_highconfimpact*100)/count_vulnibm_iot_nametampering)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_nametampering_lowconfimpact*100)/count_vulnibm_iot_nametampering)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_nametampering_mediumconfimpact*100)/count_vulnibm_iot_nametampering)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO\n")
    print("\n")
    print("      -    EN EL  "+str(float(((count_vulnibm_iot_nameanother*100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE OTRA CADENA, LOS PORCENTAJES DE IMPACTO DE CONFIDENCIALIDAD SON LOS SIGUIENTES :  \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_nameanother_highconfimpact*100)/count_vulnibm_iot_nameanother)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_nameanother_lowconfimpact*100)/count_vulnibm_iot_nameanother)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_nameanother_mediumconfimpact*100)/count_vulnibm_iot_nameanother)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO\n")
    print("\n")




    
    
    




#Abro los ficheros con los que voy a tratar




df_vulnibm_sh = pd.read_excel('vulnerabilidades_ibm_smart_home_2023.xlsx')

#Variable para almacenar el contador total de valores de nombre
count_vulnibm_sh_names=0
#Variable para almacenar el contador total de valores de un nombre concreto
count_vulnibm_sh_namepathtraversal=0
#Variables para almacenar el contador de valores de impacto de confidencialidad dato un valor de nombre especifico
count_vulnibm_sh_namepathtraversal_confimpact=0
count_vulnibm_sh_namepathtraversal_highconfimpact=0
count_vulnibm_sh_namepathtraversal_lowconfimpact=0
count_vulnibm_sh_namepathtraversal_mediumconfimpact=0

count_vulnibm_sh_namedirectorytraversal=0
count_vulnibm_sh_namedirectorytraversal_confimpact=0
count_vulnibm_sh_namedirectorytraversal_highconfimpact=0
count_vulnibm_sh_namedirectorytraversal_lowconfimpact=0
count_vulnibm_sh_namedirectorytraversal_mediumconfimpact=0

count_vulnibm_sh_nameprivilegeescalation=0
count_vulnibm_sh_nameprivilegeescalation_confimpact=0
count_vulnibm_sh_nameprivilegeescalation_highconfimpact=0
count_vulnibm_sh_nameprivilegeescalation_lowconfimpact=0
count_vulnibm_sh_nameprivilegeescalation_mediumconfimpact=0

count_vulnibm_sh_namecrosssitescripting=0
count_vulnibm_sh_namecrosssitescripting_confimpact=0
count_vulnibm_sh_namecrosssitescripting_highconfimpact=0
count_vulnibm_sh_namecrosssitescripting_lowconfimpact=0
count_vulnibm_sh_namecrosssitescripting_mediumconfimpact=0

count_vulnibm_sh_namesecuritybypass=0
count_vulnibm_sh_namesecuritybypass_confimpact=0
count_vulnibm_sh_namesecuritybypass_highconfimpact=0
count_vulnibm_sh_namesecuritybypass_lowconfimpact=0
count_vulnibm_sh_namesecuritybypass_mediumconfimpact=0

count_vulnibm_sh_nameinformationdisclosure=0
count_vulnibm_sh_nameinformationdisclosure_confimpact=0
count_vulnibm_sh_nameinformationdisclosure_highconfimpact=0
count_vulnibm_sh_nameinformationdisclosure_lowconfimpact=0
count_vulnibm_sh_nameinformationdisclosure_mediumconfimpact=0

count_vulnibm_sh_namedenialofservice=0
count_vulnibm_sh_namedenialofservice_confimpact=0
count_vulnibm_sh_namedenialofservice_highconfimpact=0
count_vulnibm_sh_namedenialofservice_lowconfimpact=0
count_vulnibm_sh_namedenialofservice_mediumconfimpact=0

count_vulnibm_sh_namecodeexecution=0
count_vulnibm_sh_namecodeexecution_confimpact=0
count_vulnibm_sh_namecodeexecution_highconfimpact=0
count_vulnibm_sh_namecodeexecution_lowconfimpact=0
count_vulnibm_sh_namecodeexecution_mediumconfimpact=0

count_vulnibm_sh_namemaninthemiddle=0
count_vulnibm_sh_namemaninthemiddle_confimpact=0
count_vulnibm_sh_namemaninthemiddle_highconfimpact=0
count_vulnibm_sh_namemaninthemiddle_lowconfimpact=0
count_vulnibm_sh_namemaninthemiddle_mediumconfimpact=0

count_vulnibm_sh_namesqlinjection=0
count_vulnibm_sh_namesqlinjection_confimpact=0
count_vulnibm_sh_namesqlinjection_highconfimpact=0
count_vulnibm_sh_namesqlinjection_lowconfimpact=0
count_vulnibm_sh_namesqlinjection_mediumconfimpact=0

count_vulnibm_sh_namecrosssiterequestforgery=0
count_vulnibm_sh_namecrosssiterequestforgery_confimpact=0
count_vulnibm_sh_namecrosssiterequestforgery_highconfimpact=0
count_vulnibm_sh_namecrosssiterequestforgery_lowconfimpact=0
count_vulnibm_sh_namecrosssiterequestforgery_mediumconfimpact=0

count_vulnibm_sh_namemoduleexecution=0
count_vulnibm_sh_namemoduleexecution_confimpact=0
count_vulnibm_sh_namemoduleexecution_highconfimpact=0
count_vulnibm_sh_namemoduleexecution_lowconfimpact=0
count_vulnibm_sh_namemoduleexecution_mediumconfimpact=0

count_vulnibm_sh_namebufferoverflow=0
count_vulnibm_sh_namebufferoverflow_confimpact=0
count_vulnibm_sh_namebufferoverflow_highconfimpact=0
count_vulnibm_sh_namebufferoverflow_lowconfimpact=0
count_vulnibm_sh_namebufferoverflow_mediumconfimpact=0

count_vulnibm_sh_namecommandexecution=0
count_vulnibm_sh_namecommandexecution_confimpact=0
count_vulnibm_sh_namecommandexecution_highconfimpact=0
count_vulnibm_sh_namecommandexecution_lowconfimpact=0
count_vulnibm_sh_namecommandexecution_mediumconfimpact=0

count_vulnibm_sh_namespoofing=0
count_vulnibm_sh_namespoofing_confimpact=0
count_vulnibm_sh_namespoofing_highconfimpact=0
count_vulnibm_sh_namespoofing_lowconfimpact=0
count_vulnibm_sh_namespoofing_mediumconfimpact=0

count_vulnibm_sh_nameclickjacking=0
count_vulnibm_sh_nameclickjacking_confimpact=0
count_vulnibm_sh_nameclickjacking_highconfimpact=0
count_vulnibm_sh_nameclickjacking_lowconfimpact=0
count_vulnibm_sh_nameclickjacking_mediumconfimpact=0

count_vulnibm_sh_namehijacking=0
count_vulnibm_sh_namehijacking_confimpact=0
count_vulnibm_sh_namehijacking_highconfimpact=0
count_vulnibm_sh_namehijacking_lowconfimpact=0
count_vulnibm_sh_namehijacking_mediumconfimpact=0

count_vulnibm_sh_namefileinclude=0
count_vulnibm_sh_namefileinclude_confimpact=0
count_vulnibm_sh_namefileinclude_highconfimpact=0
count_vulnibm_sh_namefileinclude_lowconfimpact=0
count_vulnibm_sh_namefileinclude_mediumconfimpact=0

count_vulnibm_sh_namebruteforce=0
count_vulnibm_sh_namebruteforce_confimpact=0
count_vulnibm_sh_namebruteforce_highconfimpact=0
count_vulnibm_sh_namebruteforce_lowconfimpact=0
count_vulnibm_sh_namebruteforce_mediumconfimpact=0

count_vulnibm_sh_namefileupload=0
count_vulnibm_sh_namefileupload_confimpact=0
count_vulnibm_sh_namefileupload_highconfimpact=0
count_vulnibm_sh_namefileupload_lowconfimpact=0
count_vulnibm_sh_namefileupload_mediumconfimpact=0

count_vulnibm_sh_nameheaderinjection=0
count_vulnibm_sh_nameheaderinjection_confimpact=0
count_vulnibm_sh_nameheaderinjection_highconfimpact=0
count_vulnibm_sh_nameheaderinjection_lowconfimpact=0
count_vulnibm_sh_nameheaderinjection_mediumconfimpact=0

count_vulnibm_sh_nametampering=0
count_vulnibm_sh_nametampering_confimpact=0
count_vulnibm_sh_nametampering_highconfimpact=0
count_vulnibm_sh_nametampering_lowconfimpact=0
count_vulnibm_sh_nametampering_mediumconfimpact=0

count_vulnibm_sh_nameanother=0
count_vulnibm_sh_nameanother_confimpact=0
count_vulnibm_sh_nameanother_highconfimpact=0
count_vulnibm_sh_nameanother_lowconfimpact=0
count_vulnibm_sh_nameanother_mediumconfimpact=0

#Comprobamos el contenido de name
for r in range(0,len(df_vulnibm_sh["name"])):                       
    aux_str=df_vulnibm_sh["name"][r].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
    if(aux_str!='NONE'):
        count_vulnibm_sh_names+=1
        #Compruebo el valor de nombre
        if('pathtraversal' in aux_str):
            count_vulnibm_sh_namepathtraversal+=1
            #Compruebo el valor de impacto de confidencialidad
            if(df_vulnibm_sh["x_xfe_cvss_confidentiality_impact"][r]=='High'):
                count_vulnibm_sh_namepathtraversal_confimpact+=1
                count_vulnibm_sh_namepathtraversal_highconfimpact+=1
            elif(df_vulnibm_sh["x_xfe_cvss_confidentiality_impact"][r]=='Low'):
                count_vulnibm_sh_namepathtraversal_confimpact+=1
                count_vulnibm_sh_namepathtraversal_lowconfimpact+=1
            elif(df_vulnibm_sh["x_xfe_cvss_confidentiality_impact"][r]=='Medium'):
                count_vulnibm_sh_namepathtraversal_confimpact+=1
                count_vulnibm_sh_namepathtraversal_mediumconfimpact+=1
    
        elif('directorytraversal' in aux_str):
            
            count_vulnibm_sh_namedirectorytraversal+=1
            if(df_vulnibm_sh["x_xfe_cvss_confidentiality_impact"][r]=='High'):
                count_vulnibm_sh_namedirectorytraversal_confimpact+=1
                count_vulnibm_sh_namedirectorytraversal_highconfimpact+=1
            elif(df_vulnibm_sh["x_xfe_cvss_confidentiality_impact"][r]=='Low'):
                count_vulnibm_sh_namedirectorytraversal_confimpact+=1
                count_vulnibm_sh_namedirectorytraversal_lowconfimpact+=1
            elif(df_vulnibm_sh["x_xfe_cvss_confidentiality_impact"][r]=='Medium'):
                count_vulnibm_sh_namedirectorytraversal_confimpact+=1
                count_vulnibm_sh_namedirectorytraversal_mediumconfimpact+=1
            
            
        elif('privilegeescalation' in aux_str):
        
            count_vulnibm_sh_nameprivilegeescalation+=1
            if(df_vulnibm_sh["x_xfe_cvss_confidentiality_impact"][r]=='High'):
                count_vulnibm_sh_nameprivilegeescalation_confimpact+=1
                count_vulnibm_sh_nameprivilegeescalation_highconfimpact+=1
            elif(df_vulnibm_sh["x_xfe_cvss_confidentiality_impact"][r]=='Low'):
                count_vulnibm_sh_nameprivilegeescalation_confimpact+=1
                count_vulnibm_sh_nameprivilegeescalation_lowconfimpact+=1
            elif(df_vulnibm_sh["x_xfe_cvss_confidentiality_impact"][r]=='Medium'):
                count_vulnibm_sh_nameprivilegeescalation_confimpact+=1
                count_vulnibm_sh_nameprivilegeescalation_mediumconfimpact+=1
            
        elif('cross-sitescripting' in aux_str):
        
            count_vulnibm_sh_namecrosssitescripting+=1
            if(df_vulnibm_sh["x_xfe_cvss_confidentiality_impact"][r]=='High'):
                count_vulnibm_sh_namecrosssitescripting_confimpact+=1
                count_vulnibm_sh_namecrosssitescripting_highconfimpact+=1
            elif(df_vulnibm_sh["x_xfe_cvss_confidentiality_impact"][r]=='Low'):
                count_vulnibm_sh_namecrosssitescripting_confimpact+=1
                count_vulnibm_sh_namecrosssitescripting_lowconfimpact+=1
            elif(df_vulnibm_sh["x_xfe_cvss_confidentiality_impact"][r]=='Medium'):
                count_vulnibm_sh_namecrosssitescripting_confimpact+=1
                count_vulnibm_sh_namecrosssitescripting_mediumconfimpact+=1
                                         
        elif('securitybypass' in aux_str):
        
            count_vulnibm_sh_namesecuritybypass+=1
            if(df_vulnibm_sh["x_xfe_cvss_confidentiality_impact"][r]=='High'):
                count_vulnibm_sh_namesecuritybypass_confimpact+=1
                count_vulnibm_sh_namesecuritybypass_highconfimpact+=1
            elif(df_vulnibm_sh["x_xfe_cvss_confidentiality_impact"][r]=='Low'):
                count_vulnibm_sh_namesecuritybypass_confimpact+=1
                count_vulnibm_sh_namesecuritybypass_lowconfimpact+=1
            elif(df_vulnibm_sh["x_xfe_cvss_confidentiality_impact"][r]=='Medium'):
                count_vulnibm_sh_namesecuritybypass_confimpact+=1
                count_vulnibm_sh_namesecuritybypass_mediumconfimpact+=1
                                         
        elif('information_disclosure' in aux_str or 'informationdisclosure' in aux_str):
        
            count_vulnibm_sh_nameinformationdisclosure+=1
            if(df_vulnibm_sh["x_xfe_cvss_confidentiality_impact"][r]=='High'):
                count_vulnibm_sh_nameinformationdisclosure_confimpact+=1
                count_vulnibm_sh_nameinformationdisclosure_highconfimpact+=1
            elif(df_vulnibm_sh["x_xfe_cvss_confidentiality_impact"][r]=='Low'):
                count_vulnibm_sh_nameinformationdisclosure_confimpact+=1
                count_vulnibm_sh_nameinformationdisclosure_lowconfimpact+=1
            elif(df_vulnibm_sh["x_xfe_cvss_confidentiality_impact"][r]=='Medium'):
                count_vulnibm_sh_nameinformationdisclosure_confimpact+=1
                count_vulnibm_sh_nameinformationdisclosure_mediumconfimpact+=1
                                         
        elif('denialofservice' in aux_str):
            
            count_vulnibm_sh_namedenialofservice+=1
            if(df_vulnibm_sh["x_xfe_cvss_confidentiality_impact"][r]=='High'):
                count_vulnibm_sh_namedenialofservice_confimpact+=1
                count_vulnibm_sh_namedenialofservice_highconfimpact+=1
            elif(df_vulnibm_sh["x_xfe_cvss_confidentiality_impact"][r]=='Low'):
                count_vulnibm_sh_namedenialofservice_confimpact+=1
                count_vulnibm_sh_namedenialofservice_lowconfimpact+=1
            elif(df_vulnibm_sh["x_xfe_cvss_confidentiality_impact"][r]=='Medium'):
                count_vulnibm_sh_namedenialofservice_confimpact+=1
                count_vulnibm_sh_namedenialofservice_mediumconfimpact+=1
            
        elif('codeexecution' in aux_str):
        
        
            count_vulnibm_sh_namecodeexecution+=1
            if(df_vulnibm_sh["x_xfe_cvss_confidentiality_impact"][r]=='High'):
                count_vulnibm_sh_namecodeexecution_confimpact+=1
                count_vulnibm_sh_namecodeexecution_highconfimpact+=1
            elif(df_vulnibm_sh["x_xfe_cvss_confidentiality_impact"][r]=='Low'):
                count_vulnibm_sh_namecodeexecution_confimpact+=1
                count_vulnibm_sh_namecodeexecution_lowconfimpact+=1
            elif(df_vulnibm_sh["x_xfe_cvss_confidentiality_impact"][r]=='Medium'):
                count_vulnibm_sh_namecodeexecution_confimpact+=1
                count_vulnibm_sh_namecodeexecution_mediumconfimpact+=1
                                         
        elif('maninthemiddle' in aux_str):
        
            count_vulnibm_sh_namemaninthemiddle+=1
            if(df_vulnibm_sh["x_xfe_cvss_confidentiality_impact"][r]=='High'):
                count_vulnibm_sh_namemaninthemiddle_confimpact+=1
                count_vulnibm_sh_namemaninthemiddle_highconfimpact+=1
            elif(df_vulnibm_sh["x_xfe_cvss_confidentiality_impact"][r]=='Low'):
                count_vulnibm_sh_namemaninthemiddle_confimpact+=1
                count_vulnibm_sh_namemaninthemiddle_lowconfimpact+=1
            elif(df_vulnibm_sh["x_xfe_cvss_confidentiality_impact"][r]=='Medium'):
                count_vulnibm_sh_namemaninthemiddle_confimpact+=1
                count_vulnibm_sh_namemaninthemiddle_mediumconfimpact+=1
                                         
        elif('SQLinjection' in aux_str):
        
            count_vulnibm_sh_namesqlinjection+=1
            if(df_vulnibm_sh["x_xfe_cvss_confidentiality_impact"][r]=='High'):
                count_vulnibm_sh_namesqlinjection_confimpact+=1
                count_vulnibm_sh_namesqlinjection_highconfimpact+=1
            elif(df_vulnibm_sh["x_xfe_cvss_confidentiality_impact"][r]=='Low'):
                count_vulnibm_sh_namesqlinjection_confimpact+=1
                count_vulnibm_sh_namesqlinjection_lowconfimpact+=1
            elif(df_vulnibm_sh["x_xfe_cvss_confidentiality_impact"][r]=='Medium'):
                count_vulnibm_sh_namesqlinjection_confimpact+=1
                count_vulnibm_sh_namesqlinjection_mediumconfimpact+=1
                                         
        elif('cross-siterequestforgery' in aux_str):
        
            count_vulnibm_sh_namecrosssiterequestforgery+=1
            if(df_vulnibm_sh["x_xfe_cvss_confidentiality_impact"][r]=='High'):
                count_vulnibm_sh_namecrosssiterequestforgery_confimpact+=1
                count_vulnibm_sh_namecrosssiterequestforgery_highconfimpact+=1
            elif(df_vulnibm_sh["x_xfe_cvss_confidentiality_impact"][r]=='Low'):
                count_vulnibm_sh_namecrosssiterequestforgery_confimpact+=1
                count_vulnibm_sh_namecrosssiterequestforgery_lowconfimpact+=1
            elif(df_vulnibm_sh["x_xfe_cvss_confidentiality_impact"][r]=='Medium'):
                count_vulnibm_sh_namecrosssiterequestforgery_confimpact+=1
                count_vulnibm_sh_namecrosssiterequestforgery_mediumconfimpact+=1
                                         
        elif('moduleexecution' in aux_str):
        
            count_vulnibm_sh_namemoduleexecution+=1
            if(df_vulnibm_sh["x_xfe_cvss_confidentiality_impact"][r]=='High'):
                count_vulnibm_sh_namemoduleexecution_confimpact+=1
                count_vulnibm_sh_namemoduleexecution_highconfimpact+=1
            elif(df_vulnibm_sh["x_xfe_cvss_confidentiality_impact"][r]=='Low'):
                count_vulnibm_sh_namemoduleexecution_confimpact+=1
                count_vulnibm_sh_namemoduleexecution_lowconfimpact+=1
            elif(df_vulnibm_sh["x_xfe_cvss_confidentiality_impact"][r]=='Medium'):
                count_vulnibm_sh_namemoduleexecution_confimpact+=1
                count_vulnibm_sh_namemoduleexecution_mediumconfimpact+=1
                                         
        elif('bufferoverflow' in aux_str):
        
            count_vulnibm_sh_namebufferoverflow+=1
            if(df_vulnibm_sh["x_xfe_cvss_confidentiality_impact"][r]=='High'):
                count_vulnibm_sh_namebufferoverflow_confimpact+=1
                count_vulnibm_sh_namebufferoverflow_highconfimpact+=1
            elif(df_vulnibm_sh["x_xfe_cvss_confidentiality_impact"][r]=='Low'):
                count_vulnibm_sh_namebufferoverflow_confimpact+=1
                count_vulnibm_sh_namebufferoverflow_lowconfimpact+=1
            elif(df_vulnibm_sh["x_xfe_cvss_confidentiality_impact"][r]=='Medium'):
                count_vulnibm_sh_namebufferoverflow_confimpact+=1
                count_vulnibm_sh_namebufferoverflow_mediumconfimpact+=1
                                         
        elif('commandexecution' in aux_str):
        
            count_vulnibm_sh_namecommandexecution+=1
            if(df_vulnibm_sh["x_xfe_cvss_confidentiality_impact"][r]=='High'):
                count_vulnibm_sh_namecommandexecution_confimpact+=1
                count_vulnibm_sh_namecommandexecution_highconfimpact+=1
            elif(df_vulnibm_sh["x_xfe_cvss_confidentiality_impact"][r]=='Low'):
                count_vulnibm_sh_namecommandexecution_confimpact+=1
                count_vulnibm_sh_namecommandexecution_lowconfimpact+=1
            elif(df_vulnibm_sh["x_xfe_cvss_confidentiality_impact"][r]=='Medium'):
                count_vulnibm_sh_namecommandexecution_confimpact+=1
                count_vulnibm_sh_namecommandexecution_mediumconfimpact+=1
                                         
        elif('spoofing' in aux_str):
        
            count_vulnibm_sh_namespoofing+=1
            if(df_vulnibm_sh["x_xfe_cvss_confidentiality_impact"][r]=='High'):
                count_vulnibm_sh_namespoofing_confimpact+=1
                count_vulnibm_sh_namespoofing_highconfimpact+=1
            elif(df_vulnibm_sh["x_xfe_cvss_confidentiality_impact"][r]=='Low'):
                count_vulnibm_sh_namespoofing_confimpact+=1
                count_vulnibm_sh_namespoofing_lowconfimpact+=1
            elif(df_vulnibm_sh["x_xfe_cvss_confidentiality_impact"][r]=='Medium'):
                count_vulnibm_sh_namespoofing_confimpact+=1
                count_vulnibm_sh_namespoofing_mediumconfimpact+=1
                                         
        elif('clickjacking' in aux_str):
        
            count_vulnibm_sh_nameclickjacking+=1
            if(df_vulnibm_sh["x_xfe_cvss_confidentiality_impact"][r]=='High'):
                count_vulnibm_sh_nameclickjacking_confimpact+=1
                count_vulnibm_sh_nameclickjacking_highconfimpact+=1
            elif(df_vulnibm_sh["x_xfe_cvss_confidentiality_impact"][r]=='Low'):
                count_vulnibm_sh_nameclickjacking_confimpact+=1
                count_vulnibm_sh_nameclickjacking_lowconfimpact+=1
            elif(df_vulnibm_sh["x_xfe_cvss_confidentiality_impact"][r]=='Medium'):
                count_vulnibm_sh_nameclickjacking_confimpact+=1
                count_vulnibm_sh_nameclickjacking_mediumconfimpact+=1
              
        elif('hijacking' in aux_str):
        
            count_vulnibm_sh_namehijacking+=1
            if(df_vulnibm_sh["x_xfe_cvss_confidentiality_impact"][r]=='High'):
                count_vulnibm_sh_namehijacking_confimpact+=1
                count_vulnibm_sh_namehijacking_highconfimpact+=1
            elif(df_vulnibm_sh["x_xfe_cvss_confidentiality_impact"][r]=='Low'):
                count_vulnibm_sh_namehijacking_confimpact+=1
                count_vulnibm_sh_namehijacking_lowconfimpact+=1
            elif(df_vulnibm_sh["x_xfe_cvss_confidentiality_impact"][r]=='Medium'):
                count_vulnibm_sh_namehijacking_confimpact+=1
                count_vulnibm_sh_namehijacking_mediumconfimpact+=1
               
        elif('fileinclude' in aux_str):
        
            count_vulnibm_sh_namefileinclude+=1
            if(df_vulnibm_sh["x_xfe_cvss_confidentiality_impact"][r]=='High'):
                count_vulnibm_sh_namefileinclude_confimpact+=1
                count_vulnibm_sh_namefileinclude_highconfimpact+=1
            elif(df_vulnibm_sh["x_xfe_cvss_confidentiality_impact"][r]=='Low'):
                count_vulnibm_sh_namefileinclude_confimpact+=1
                count_vulnibm_sh_namefileinclude_lowconfimpact+=1
            elif(df_vulnibm_sh["x_xfe_cvss_confidentiality_impact"][r]=='Medium'):
                count_vulnibm_sh_namefileinclude_confimpact+=1
                count_vulnibm_sh_namefileinclude_mediumconfimpact+=1
                
               
        elif('bruteforce' in aux_str):
        
            count_vulnibm_sh_namebruteforce+=1
            if(df_vulnibm_sh["x_xfe_cvss_confidentiality_impact"][r]=='High'):
                count_vulnibm_sh_namebruteforce_confimpact+=1
                count_vulnibm_sh_namebruteforce_highconfimpact+=1
            elif(df_vulnibm_sh["x_xfe_cvss_confidentiality_impact"][r]=='Low'):
                count_vulnibm_sh_namebruteforce_confimpact+=1
                count_vulnibm_sh_namebruteforce_lowconfimpact+=1
            elif(df_vulnibm_sh["x_xfe_cvss_confidentiality_impact"][r]=='Medium'):
                count_vulnibm_sh_namebruteforce_confimpact+=1
                count_vulnibm_sh_namebruteforce_mediumconfimpact+=1
                
               
        elif('fileupload' in aux_str):
        
            count_vulnibm_sh_namefileupload+=1
            if(df_vulnibm_sh["x_xfe_cvss_confidentiality_impact"][r]=='High'):
                count_vulnibm_sh_namefileupload_confimpact+=1
                count_vulnibm_sh_namefileupload_highconfimpact+=1
            elif(df_vulnibm_sh["x_xfe_cvss_confidentiality_impact"][r]=='Low'):
                count_vulnibm_sh_namefileupload_confimpact+=1
                count_vulnibm_sh_namefileupload_lowconfimpact+=1
            elif(df_vulnibm_sh["x_xfe_cvss_confidentiality_impact"][r]=='Medium'):
                count_vulnibm_sh_namefileupload_confimpact+=1
                count_vulnibm_sh_namefileupload_mediumconfimpact+=1
                
               
        elif('headerinjection' in aux_str):
        
            count_vulnibm_sh_nameheaderinjection+=1
            if(df_vulnibm_sh["x_xfe_cvss_confidentiality_impact"][r]=='High'):
                count_vulnibm_sh_nameheaderinjection_confimpact+=1
                count_vulnibm_sh_nameheaderinjection_highconfimpact+=1
            elif(df_vulnibm_sh["x_xfe_cvss_confidentiality_impact"][r]=='Low'):
                count_vulnibm_sh_nameheaderinjection_confimpact+=1
                count_vulnibm_sh_nameheaderinjection_lowconfimpact+=1
            elif(df_vulnibm_sh["x_xfe_cvss_confidentiality_impact"][r]=='Medium'):
                count_vulnibm_sh_nameheaderinjection_confimpact+=1
                count_vulnibm_sh_nameheaderinjection_mediumconfimpact+=1
               
        elif('Tampering' in aux_str):
        
            count_vulnibm_sh_nametampering+=1
            if(df_vulnibm_sh["x_xfe_cvss_confidentiality_impact"][r]=='High'):
                count_vulnibm_sh_nametampering_confimpact+=1
                count_vulnibm_sh_nametampering_highconfimpact+=1
            elif(df_vulnibm_sh["x_xfe_cvss_confidentiality_impact"][r]=='Low'):
                count_vulnibm_sh_nametampering_confimpact+=1
                count_vulnibm_sh_nametampering_lowconfimpact+=1
            elif(df_vulnibm_sh["x_xfe_cvss_confidentiality_impact"][r]=='Medium'):
                count_vulnibm_sh_nametampering_confimpact+=1
                count_vulnibm_sh_nametampering_mediumconfimpact+=1
    
        else:
        
            count_vulnibm_sh_nameanother+=1
            if(df_vulnibm_sh["x_xfe_cvss_confidentiality_impact"][r]=='High'):
                count_vulnibm_sh_nameanother_confimpact+=1
                count_vulnibm_sh_nameanother_highconfimpact+=1
            elif(df_vulnibm_sh["x_xfe_cvss_confidentiality_impact"][r]=='Low'):
                count_vulnibm_sh_nameanother_confimpact+=1
                count_vulnibm_sh_nameanother_lowconfimpact+=1
            elif(df_vulnibm_sh["x_xfe_cvss_confidentiality_impact"][r]=='Medium'):
                count_vulnibm_sh_nameanother_confimpact+=1
                count_vulnibm_sh_nameanother_mediumconfimpact+=1
                
                
                
                
                
print("**********************************************ESTADÍSTICAS NOMBRE/IMPACTO DE CONFIDENCIALIDAD VULNERABILIDADES IBM PARTE SMART HOME**********************************************")
print("\n")                            
print("\n")
print(" DE UN TOTAL DE "+str(count_vulnibm_sh_names)+" VULNERABILIDADES:\n") 
print("\n")
print("   - LAS ESTADISTICAS DE VALORES DE NOMBRE SON LAS SIGUIENTES:  \n")
print("      -    EN  "+str(count_vulnibm_sh_namepathtraversal)+" VULNERABILIDADES EL NOMBRE INCLUYE PATH TRAVERSAL, LAS ESTADÍSTICAS DE IMPACTO DE CONFIDENCIALIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_sh_namepathtraversal_highconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_sh_namepathtraversal_lowconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_sh_namepathtraversal_mediumconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO\n")
print("\n")
print("      -    EN  "+str(count_vulnibm_sh_namedirectorytraversal)+" VULNERABILIDADES EL NOMBRE INCLUYE DIRECTORY TRAVERSAL, LAS ESTADÍSTICAS DE IMPACTO DE CONFIDENCIALIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_sh_namedirectorytraversal_highconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_sh_namedirectorytraversal_lowconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_sh_namedirectorytraversal_mediumconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO\n")
print("\n")
print("      -    EN  "+str(count_vulnibm_sh_nameprivilegeescalation)+" VULNERABILIDADES EL NOMBRE INCLUYE PRIVILEGE ESCALATION, LAS ESTADÍSTICAS DE IMPACTO DE CONFIDENCIALIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_sh_nameprivilegeescalation_highconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_sh_nameprivilegeescalation_lowconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_sh_nameprivilegeescalation_mediumconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO\n")
print("\n")
print("      -    EN  "+str(count_vulnibm_sh_namecrosssitescripting)+" VULNERABILIDADES EL NOMBRE INCLUYE CROSS SITE SCRIPTING, LAS ESTADÍSTICAS DE IMPACTO DE CONFIDENCIALIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_sh_namecrosssitescripting_highconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_sh_namecrosssitescripting_lowconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_sh_namecrosssitescripting_mediumconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO\n")
print("\n")
print("      -    EN  "+str(count_vulnibm_sh_namesecuritybypass)+" VULNERABILIDADES EL NOMBRE INCLUYE SECURITY BYPASS, LAS ESTADÍSTICAS DE IMPACTO DE CONFIDENCIALIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_sh_namesecuritybypass_highconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_sh_namesecuritybypass_lowconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_sh_namesecuritybypass_mediumconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO\n")
print("\n")
print("      -    EN  "+str(count_vulnibm_sh_nameinformationdisclosure)+" VULNERABILIDADES EL NOMBRE INCLUYE INFORMATION DISCLOSURE, LAS ESTADÍSTICAS DE IMPACTO DE CONFIDENCIALIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_sh_nameinformationdisclosure_highconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_sh_nameinformationdisclosure_lowconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_sh_nameinformationdisclosure_mediumconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO\n")
print("\n")
print("      -    EN  "+str(count_vulnibm_sh_namedenialofservice)+" VULNERABILIDADES EL NOMBRE INCLUYE DENIAL OF SERVICE, LAS ESTADÍSTICAS DE IMPACTO DE CONFIDENCIALIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_sh_namedenialofservice_highconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_sh_namedenialofservice_lowconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_sh_namedenialofservice_mediumconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO\n")
print("\n")
print("      -    EN  "+str(count_vulnibm_sh_namecodeexecution)+" VULNERABILIDADES EL NOMBRE INCLUYE CODE EXECUTION, LAS ESTADÍSTICAS DE IMPACTO DE CONFIDENCIALIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_sh_namecodeexecution_highconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_sh_namecodeexecution_lowconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_sh_namecodeexecution_mediumconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO\n")
print("\n")
print("      -    EN  "+str(count_vulnibm_sh_namemaninthemiddle)+" VULNERABILIDADES EL NOMBRE INCLUYE MAN IN THE MIDDLE, LAS ESTADÍSTICAS DE IMPACTO DE CONFIDENCIALIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_sh_namemaninthemiddle_highconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_sh_namemaninthemiddle_lowconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_sh_namemaninthemiddle_mediumconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO\n")
print("\n")
print("      -    EN  "+str(count_vulnibm_sh_namesqlinjection)+" VULNERABILIDADES EL NOMBRE INCLUYE SQL INJECTION, LAS ESTADÍSTICAS DE IMPACTO DE CONFIDENCIALIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_sh_namesqlinjection_highconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_sh_namesqlinjection_lowconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_sh_namesqlinjection_mediumconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO\n")
print("\n")
print("      -    EN  "+str(count_vulnibm_sh_namecrosssiterequestforgery)+" VULNERABILIDADES EL NOMBRE INCLUYE CROSS SITE REQUEST FORGERY, LAS ESTADÍSTICAS DE IMPACTO DE CONFIDENCIALIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_sh_namecrosssiterequestforgery_highconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_sh_namecrosssiterequestforgery_lowconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_sh_namecrosssiterequestforgery_mediumconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO\n")
print("\n")
print("      -    EN  "+str(count_vulnibm_sh_namemoduleexecution)+" VULNERABILIDADES EL NOMBRE INCLUYE MODULE EXECUTION, LAS ESTADÍSTICAS DE IMPACTO DE CONFIDENCIALIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_sh_namemoduleexecution_highconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_sh_namemoduleexecution_lowconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_sh_namemoduleexecution_mediumconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO\n")
print("\n")
print("      -    EN  "+str(count_vulnibm_sh_namebufferoverflow)+" VULNERABILIDADES EL NOMBRE INCLUYE BUFFER OVERFLOW, LAS ESTADÍSTICAS DE IMPACTO DE CONFIDENCIALIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_sh_namebufferoverflow_highconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_sh_namebufferoverflow_lowconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_sh_namebufferoverflow_mediumconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO\n")
print("\n")
print("      -    EN  "+str(count_vulnibm_sh_namecommandexecution)+" VULNERABILIDADES EL NOMBRE INCLUYE COMMAND EXECUTION, LAS ESTADÍSTICAS DE IMPACTO DE CONFIDENCIALIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_sh_namecommandexecution_highconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_sh_namecommandexecution_lowconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_sh_namecommandexecution_mediumconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO\n")
print("\n")
print("      -    EN  "+str(count_vulnibm_sh_namespoofing)+" VULNERABILIDADES EL NOMBRE INCLUYE SPOOFING, LAS ESTADÍSTICAS DE IMPACTO DE CONFIDENCIALIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_sh_namespoofing_highconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_sh_namespoofing_lowconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_sh_namespoofing_mediumconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO\n")
print("\n")
print("      -    EN  "+str(count_vulnibm_sh_nameclickjacking)+" VULNERABILIDADES EL NOMBRE INCLUYE CLICKJACKING, LAS ESTADÍSTICAS DE IMPACTO DE CONFIDENCIALIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_sh_nameclickjacking_highconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_sh_nameclickjacking_lowconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_sh_nameclickjacking_mediumconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO\n")
print("\n")
print("      -    EN  "+str(count_vulnibm_sh_namehijacking)+" VULNERABILIDADES EL NOMBRE INCLUYE HIJACKING, LAS ESTADÍSTICAS DE IMPACTO DE CONFIDENCIALIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_sh_namehijacking_highconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_sh_namehijacking_lowconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_sh_namehijacking_mediumconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO\n")
print("\n")
print("      -    EN  "+str(count_vulnibm_sh_namefileinclude)+" VULNERABILIDADES EL NOMBRE INCLUYE FILEINCLUDE, LAS ESTADÍSTICAS DE IMPACTO DE CONFIDENCIALIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_sh_namefileinclude_highconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_sh_namefileinclude_lowconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_sh_namefileinclude_mediumconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO\n")
print("\n")
print("      -    EN  "+str(count_vulnibm_sh_namebruteforce)+" VULNERABILIDADES EL NOMBRE INCLUYE BRUTEFORCE, LAS ESTADÍSTICAS DE IMPACTO DE CONFIDENCIALIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_sh_namebruteforce_highconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_sh_namebruteforce_lowconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_sh_namebruteforce_mediumconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO\n")
print("\n")
print("      -    EN  "+str(count_vulnibm_sh_namefileupload)+" VULNERABILIDADES EL NOMBRE INCLUYE FILE UPLOAD, LAS ESTADÍSTICAS DE IMPACTO DE CONFIDENCIALIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_sh_namefileupload_highconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_sh_namefileupload_lowconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_sh_namefileupload_mediumconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO\n")
print("\n")
print("      -    EN  "+str(count_vulnibm_sh_nameheaderinjection)+" VULNERABILIDADES EL NOMBRE INCLUYE HEADER INJECTION, LAS ESTADÍSTICAS DE IMPACTO DE CONFIDENCIALIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_sh_nameheaderinjection_highconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_sh_nameheaderinjection_lowconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_sh_nameheaderinjection_mediumconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO\n")
print("\n")
print("      -    EN  "+str(count_vulnibm_sh_nametampering)+" VULNERABILIDADES EL NOMBRE INCLUYE TAMPERING, LAS ESTADÍSTICAS DE IMPACTO DE CONFIDENCIALIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_sh_nametampering_highconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_sh_nametampering_lowconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_sh_nametampering_mediumconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO\n")
print("\n")
print("      -    EN  "+str(count_vulnibm_sh_nameanother)+" VULNERABILIDADES EL NOMBRE INCLUYE OTRA CADENA, LAS ESTADÍSTICAS DE IMPACTO DE CONFIDENCIALIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_sh_nameanother_highconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_sh_nameanother_lowconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_sh_nameanother_mediumconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO\n")
print("\n")





print("**********************************************PORCENTAJE NOMBRE/IMPACTO DE CONFIDENCIALIDAD VULNERABILIDADES IBM PARTE SMART HOME**********************************************")
print("\n")                            
print("\n")
print(" DE UN TOTAL DE "+str(count_vulnibm_sh_names)+" VULNERABILIDADES :\n") 
print("\n")
print("   - LOS PORCENTAJES DE VALORES DE NOMBRE SON LOS SIGUIENTES:  \n")
if(count_vulnibm_sh_namepathtraversal>0):
    print("      -    EN EL  "+str(float(((count_vulnibm_sh_namepathtraversal*100)/count_vulnibm_sh_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE PATH TRAVERSAL, LOS PORCENTAJES DE IMPACTO DE CONFIDENCIALIDAD SON LOS SIGUIENTES :  \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namepathtraversal_highconfimpact*100)/count_vulnibm_sh_namepathtraversal)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namepathtraversal_lowconfimpact*100)/count_vulnibm_sh_namepathtraversal)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namepathtraversal_mediumconfimpact*100)/count_vulnibm_sh_namepathtraversal)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO\n")
    print("\n")
if(count_vulnibm_sh_namedirectorytraversal>0):
    print("      -    EN EL  "+str(float(((count_vulnibm_sh_namedirectorytraversal*100)/count_vulnibm_sh_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE DIRECTORY TRAVERSAL, LOS PORCENTAJES DE IMPACTO DE CONFIDENCIALIDAD SON LOS SIGUIENTES :  \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namedirectorytraversal_highconfimpact*100)/count_vulnibm_sh_namedirectorytraversal)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namedirectorytraversal_lowconfimpact*100)/count_vulnibm_sh_namedirectorytraversal)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namedirectorytraversal_mediumconfimpact*100)/count_vulnibm_sh_namedirectorytraversal)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO\n")
    print("\n")
if(count_vulnibm_sh_nameprivilegeescalation>0):
    print("      -    EN EL  "+str(float(((count_vulnibm_sh_nameprivilegeescalation*100)/count_vulnibm_sh_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE PRIVILEGE ESCALATION, LOS PORCENTAJES DE IMPACTO DE CONFIDENCIALIDAD SON LOS SIGUIENTES :  \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_nameprivilegeescalation_highconfimpact*100)/count_vulnibm_sh_nameprivilegeescalation)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_nameprivilegeescalation_lowconfimpact*100)/count_vulnibm_sh_nameprivilegeescalation)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_nameprivilegeescalation_mediumconfimpact*100)/count_vulnibm_sh_nameprivilegeescalation)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO\n")
    print("\n")
if(count_vulnibm_sh_namecrosssitescripting>0):
    print("      -    EN EL  "+str(float(((count_vulnibm_sh_namecrosssitescripting*100)/count_vulnibm_sh_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE CROSS SITE SCRIPTING, LOS PORCENTAJES DE IMPACTO DE CONFIDENCIALIDAD SON LOS SIGUIENTES :  \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namecrosssitescripting_highconfimpact*100)/count_vulnibm_sh_namecrosssitescripting)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namecrosssitescripting_lowconfimpact*100)/count_vulnibm_sh_namecrosssitescripting)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namecrosssitescripting_mediumconfimpact*100)/count_vulnibm_sh_namecrosssitescripting)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO\n")
    print("\n")
if(count_vulnibm_sh_namesecuritybypass>0):
    print("      -    EN EL  "+str(float(((count_vulnibm_sh_namesecuritybypass*100)/count_vulnibm_sh_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE SECURITY BYPASS, LOS PORCENTAJES DE IMPACTO DE CONFIDENCIALIDAD SON LOS SIGUIENTES :  \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namesecuritybypass_highconfimpact*100)/count_vulnibm_sh_namesecuritybypass)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namesecuritybypass_lowconfimpact*100)/count_vulnibm_sh_namesecuritybypass)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namesecuritybypass_mediumconfimpact*100)/count_vulnibm_sh_namesecuritybypass)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO\n")
    print("\n")
if(count_vulnibm_sh_nameinformationdisclosure>0):
    print("      -    EN EL  "+str(float(((count_vulnibm_sh_nameinformationdisclosure*100)/count_vulnibm_sh_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE INFORMATION DISCLOSURE, LOS PORCENTAJES DE IMPACTO DE CONFIDENCIALIDAD SON LOS SIGUIENTES :  \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_nameinformationdisclosure_highconfimpact*100)/count_vulnibm_sh_nameinformationdisclosure)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_nameinformationdisclosure_lowconfimpact*100)/count_vulnibm_sh_nameinformationdisclosure)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_nameinformationdisclosure_mediumconfimpact*100)/count_vulnibm_sh_nameinformationdisclosure)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO\n")
    print("\n")
if(count_vulnibm_sh_namedenialofservice>0):
    print("      -    EN EL  "+str(float(((count_vulnibm_sh_namedenialofservice*100)/count_vulnibm_sh_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE DENIAL OF SERVICE, LOS PORCENTAJES DE IMPACTO DE CONFIDENCIALIDAD SON LOS SIGUIENTES :  \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namedenialofservice_highconfimpact*100)/count_vulnibm_sh_namedenialofservice)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namedenialofservice_lowconfimpact*100)/count_vulnibm_sh_namedenialofservice)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namedenialofservice_mediumconfimpact*100)/count_vulnibm_sh_namedenialofservice)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO\n")
    print("\n")
if(count_vulnibm_sh_namecodeexecution>0):
    print("      -    EN EL  "+str(float(((count_vulnibm_sh_namecodeexecution*100)/count_vulnibm_sh_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE CODE EXECUTION, LOS PORCENTAJES DE IMPACTO DE CONFIDENCIALIDAD SON LOS SIGUIENTES :  \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namecodeexecution_highconfimpact*100)/count_vulnibm_sh_namecodeexecution)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namecodeexecution_lowconfimpact*100)/count_vulnibm_sh_namecodeexecution)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namecodeexecution_mediumconfimpact*100)/count_vulnibm_sh_namecodeexecution)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO\n")
    print("\n")
if(count_vulnibm_sh_namemaninthemiddle>0):
    print("      -    EN EL  "+str(float(((count_vulnibm_sh_namemaninthemiddle*100)/count_vulnibm_sh_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE MAN IN THE MIDDLE, LOS PORCENTAJES DE IMPACTO DE CONFIDENCIALIDAD SON LOS SIGUIENTES :  \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namemaninthemiddle_highconfimpact*100)/count_vulnibm_sh_namemaninthemiddle)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namemaninthemiddle_lowconfimpact*100)/count_vulnibm_sh_namemaninthemiddle)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namemaninthemiddle_mediumconfimpact*100)/count_vulnibm_sh_namemaninthemiddle)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO\n")
    print("\n")
if(count_vulnibm_sh_namesqlinjection>0):
    print("      -    EN EL  "+str(float(((count_vulnibm_sh_namesqlinjection*100)/count_vulnibm_sh_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE SQL INJECTION, LOS PORCENTAJES DE IMPACTO DE CONFIDENCIALIDAD SON LOS SIGUIENTES :  \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namesqlinjection_highconfimpact*100)/count_vulnibm_sh_namesqlinjection)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namesqlinjection_lowconfimpact*100)/count_vulnibm_sh_namesqlinjection)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namesqlinjection_mediumconfimpact*100)/count_vulnibm_sh_namesqlinjection)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO\n")
    print("\n")
if(count_vulnibm_sh_namecrosssiterequestforgery>0):
    print("      -    EN EL  "+str(float(((count_vulnibm_sh_namecrosssiterequestforgery*100)/count_vulnibm_sh_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE CROSS SITE REQUEST FORGERY, LOS PORCENTAJES DE IMPACTO DE CONFIDENCIALIDAD SON LOS SIGUIENTES :  \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namecrosssiterequestforgery_highconfimpact*100)/count_vulnibm_sh_namecrosssiterequestforgery)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namecrosssiterequestforgery_lowconfimpact*100)/count_vulnibm_sh_namecrosssiterequestforgery)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namecrosssiterequestforgery_mediumconfimpact*100)/count_vulnibm_sh_namecrosssiterequestforgery)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO\n")
    print("\n")
if(count_vulnibm_sh_namemoduleexecution>0):
    print("      -    EN EL  "+str(float(((count_vulnibm_sh_namemoduleexecution*100)/count_vulnibm_sh_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE MODULE EXECUTION, LOS PORCENTAJES DE IMPACTO DE CONFIDENCIALIDAD SON LOS SIGUIENTES :  \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namemoduleexecution_highconfimpact*100)/count_vulnibm_sh_namemoduleexecution)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namemoduleexecution_lowconfimpact*100)/count_vulnibm_sh_namemoduleexecution)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namemoduleexecution_mediumconfimpact*100)/count_vulnibm_sh_namemoduleexecution)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO\n")
    print("\n")
if(count_vulnibm_sh_namebufferoverflow>0):
    print("      -    EN EL  "+str(float(((count_vulnibm_sh_namebufferoverflow*100)/count_vulnibm_sh_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE BUFFER OVERFLOW, LOS PORCENTAJES DE IMPACTO DE CONFIDENCIALIDAD SON LOS SIGUIENTES :  \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namebufferoverflow_highconfimpact*100)/count_vulnibm_sh_namebufferoverflow)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namebufferoverflow_lowconfimpact*100)/count_vulnibm_sh_namebufferoverflow)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namebufferoverflow_mediumconfimpact*100)/count_vulnibm_sh_namebufferoverflow)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO\n")
    print("\n")
if(count_vulnibm_sh_namecommandexecution>0):
    print("      -    EN EL  "+str(float(((count_vulnibm_sh_namecommandexecution*100)/count_vulnibm_sh_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE COMMAND EXECUTION, LOS PORCENTAJES DE IMPACTO DE CONFIDENCIALIDAD SON LOS SIGUIENTES :  \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namecommandexecution_highconfimpact*100)/count_vulnibm_sh_namecommandexecution)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namecommandexecution_lowconfimpact*100)/count_vulnibm_sh_namecommandexecution)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namecommandexecution_mediumconfimpact*100)/count_vulnibm_sh_namecommandexecution)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO\n")
    print("\n")
if(count_vulnibm_sh_namespoofing>0):
    print("      -    EN EL  "+str(float(((count_vulnibm_sh_namespoofing*100)/count_vulnibm_sh_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE SPOOFING, LOS PORCENTAJES DE IMPACTO DE CONFIDENCIALIDAD SON LOS SIGUIENTES :  \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namespoofing_highconfimpact*100)/count_vulnibm_sh_namespoofing)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namespoofing_lowconfimpact*100)/count_vulnibm_sh_namespoofing)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namespoofing_mediumconfimpact*100)/count_vulnibm_sh_namespoofing)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO\n")
    print("\n")
if(count_vulnibm_sh_nameclickjacking>0):
    print("      -    EN EL  "+str(float(((count_vulnibm_sh_nameclickjacking*100)/count_vulnibm_sh_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE CLICKJACKING, LOS PORCENTAJES DE IMPACTO DE CONFIDENCIALIDAD SON LOS SIGUIENTES :  \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_nameclickjacking_highconfimpact*100)/count_vulnibm_sh_nameclickjacking)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_nameclickjacking_lowconfimpact*100)/count_vulnibm_sh_nameclickjacking)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_nameclickjacking_mediumconfimpact*100)/count_vulnibm_sh_nameclickjacking)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO\n")
    print("\n")
if(count_vulnibm_sh_namehijacking>0):
    print("      -    EN EL  "+str(float(((count_vulnibm_sh_namehijacking*100)/count_vulnibm_sh_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE HIJACKING, LOS PORCENTAJES DE IMPACTO DE CONFIDENCIALIDAD SON LOS SIGUIENTES :  \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namehijacking_highconfimpact*100)/count_vulnibm_sh_namehijacking)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namehijacking_lowconfimpact*100)/count_vulnibm_sh_namehijacking)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namehijacking_mediumconfimpact*100)/count_vulnibm_sh_namehijacking)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO\n")
    print("\n")
if(count_vulnibm_sh_namefileinclude>0):
    print("      -    EN EL  "+str(float(((count_vulnibm_sh_namefileinclude*100)/count_vulnibm_sh_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE FILEINCLUDE, LOS PORCENTAJES DE IMPACTO DE CONFIDENCIALIDAD SON LOS SIGUIENTES :  \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namefileinclude_highconfimpact*100)/count_vulnibm_sh_namefileinclude)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namefileinclude_lowconfimpact*100)/count_vulnibm_sh_namefileinclude)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namefileinclude_mediumconfimpact*100)/count_vulnibm_sh_namefileinclude)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO\n")
    print("\n")
if(count_vulnibm_sh_namebruteforce>0):
    print("      -    EN EL  "+str(float(((count_vulnibm_sh_namebruteforce*100)/count_vulnibm_sh_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE BRUTEFORCE, LOS PORCENTAJES DE IMPACTO DE CONFIDENCIALIDAD SON LOS SIGUIENTES :  \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namebruteforce_highconfimpact*100)/count_vulnibm_sh_namebruteforce)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namebruteforce_lowconfimpact*100)/count_vulnibm_sh_namebruteforce)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namebruteforce_mediumconfimpact*100)/count_vulnibm_sh_namebruteforce)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO\n")
    print("\n")
if(count_vulnibm_sh_namefileupload>0):
    print("      -    EN EL  "+str(float(((count_vulnibm_sh_namefileupload*100)/count_vulnibm_sh_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE FILE UPLOAD, LOS PORCENTAJES DE IMPACTO DE CONFIDENCIALIDAD SON LOS SIGUIENTES :  \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namefileupload_highconfimpact*100)/count_vulnibm_sh_namefileupload)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namefileupload_lowconfimpact*100)/count_vulnibm_sh_namefileupload)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namefileupload_mediumconfimpact*100)/count_vulnibm_sh_namefileupload)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO\n")
    print("\n")
if(count_vulnibm_sh_nameheaderinjection>0):
    print("      -    EN EL  "+str(float(((count_vulnibm_sh_nameheaderinjection*100)/count_vulnibm_sh_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE HEADER INJECTION, LOS PORCENTAJES DE IMPACTO DE CONFIDENCIALIDAD SON LOS SIGUIENTES :  \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_nameheaderinjection_highconfimpact*100)/count_vulnibm_sh_nameheaderinjection)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_nameheaderinjection_lowconfimpact*100)/count_vulnibm_sh_nameheaderinjection)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_nameheaderinjection_mediumconfimpact*100)/count_vulnibm_sh_nameheaderinjection)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO\n")
    print("\n")
if(count_vulnibm_sh_nametampering>0):
    print("      -    EN EL  "+str(float(((count_vulnibm_sh_nametampering*100)/count_vulnibm_sh_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE TAMPERING, LOS PORCENTAJES DE IMPACTO DE CONFIDENCIALIDAD SON LOS SIGUIENTES :  \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_nametampering_highconfimpact*100)/count_vulnibm_sh_nametampering)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_nametampering_lowconfimpact*100)/count_vulnibm_sh_nametampering)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_nametampering_mediumconfimpact*100)/count_vulnibm_sh_nametampering)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO\n")
    print("\n")
    print("      -    EN EL  "+str(float(((count_vulnibm_sh_nameanother*100)/count_vulnibm_sh_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE OTRA CADENA, LOS PORCENTAJES DE IMPACTO DE CONFIDENCIALIDAD SON LOS SIGUIENTES :  \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_nameanother_highconfimpact*100)/count_vulnibm_sh_nameanother)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_nameanother_lowconfimpact*100)/count_vulnibm_sh_nameanother)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_nameanother_mediumconfimpact*100)/count_vulnibm_sh_nameanother)))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO\n")
    print("\n")



print("**********************************************ESTADÍSTICAS NOMBRE/IMPACTO DE CONFIDENCIALIDAD VULNERABILIDADES IBM PARTE IOT Y SMART HOME**********************************************")
print("\n")                            
print("\n")
print(" DE UN TOTAL DE "+str(count_vulnibm_iot_names+count_vulnibm_sh_names)+" VULNERABILIDADES:\n") 
print("\n")
print("   - LAS ESTADISTICAS DE VALORES DE NOMBRE SON LAS SIGUIENTES:  \n")
print("      -    EN  "+str(count_vulnibm_iot_namepathtraversal+count_vulnibm_sh_namepathtraversal)+" VULNERABILIDADES EL NOMBRE INCLUYE PATH TRAVERSAL, LOS PORCENTAJES DE IMPACTO DE CONFIDENCIALIDAD SON LOS SIGUIENTES:  \n")
print("            -    EN  "+str(count_vulnibm_iot_namepathtraversal_highconfimpact+count_vulnibm_sh_namepathtraversal_highconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_iot_namepathtraversal_lowconfimpact+count_vulnibm_sh_namepathtraversal_lowconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_iot_namepathtraversal_mediumconfimpact+count_vulnibm_sh_namepathtraversal_mediumconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_namedirectorytraversal+count_vulnibm_sh_namedirectorytraversal)+" VULNERABILIDADES EL NOMBRE INCLUYE directorytraversal, LOS PORCENTAJES DE IMPACTO DE CONFIDENCIALIDAD SON LOS SIGUIENTES:  \n")
print("            -    EN  "+str(count_vulnibm_iot_namedirectorytraversal_highconfimpact+count_vulnibm_sh_namedirectorytraversal_highconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_iot_namedirectorytraversal_lowconfimpact+count_vulnibm_sh_namedirectorytraversal_lowconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_iot_namedirectorytraversal_mediumconfimpact+count_vulnibm_sh_namedirectorytraversal_mediumconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_nameprivilegeescalation+count_vulnibm_sh_nameprivilegeescalation)+" VULNERABILIDADES EL NOMBRE INCLUYE privilegeescalation, LOS PORCENTAJES DE IMPACTO DE CONFIDENCIALIDAD SON LOS SIGUIENTES:  \n")
print("            -    EN  "+str(count_vulnibm_iot_nameprivilegeescalation_highconfimpact+count_vulnibm_sh_nameprivilegeescalation_highconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_iot_nameprivilegeescalation_lowconfimpact+count_vulnibm_sh_nameprivilegeescalation_lowconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_iot_nameprivilegeescalation_mediumconfimpact+count_vulnibm_sh_nameprivilegeescalation_mediumconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_namecrosssitescripting+count_vulnibm_sh_namecrosssitescripting)+" VULNERABILIDADES EL NOMBRE INCLUYE crosssitescripting, LOS PORCENTAJES DE IMPACTO DE CONFIDENCIALIDAD SON LOS SIGUIENTES:  \n")
print("            -    EN  "+str(count_vulnibm_iot_namecrosssitescripting_highconfimpact+count_vulnibm_sh_namecrosssitescripting_highconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_iot_namecrosssitescripting_lowconfimpact+count_vulnibm_sh_namecrosssitescripting_lowconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_iot_namecrosssitescripting_mediumconfimpact+count_vulnibm_sh_namecrosssitescripting_mediumconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_namesecuritybypass+count_vulnibm_sh_namesecuritybypass)+" VULNERABILIDADES EL NOMBRE INCLUYE securitybypass, LOS PORCENTAJES DE IMPACTO DE CONFIDENCIALIDAD SON LOS SIGUIENTES:  \n")
print("            -    EN  "+str(count_vulnibm_iot_namesecuritybypass_highconfimpact+count_vulnibm_sh_namesecuritybypass_highconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_iot_namesecuritybypass_lowconfimpact+count_vulnibm_sh_namesecuritybypass_lowconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_iot_namesecuritybypass_mediumconfimpact+count_vulnibm_sh_namesecuritybypass_mediumconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_nameinformationdisclosure+count_vulnibm_sh_nameinformationdisclosure)+" VULNERABILIDADES EL NOMBRE INCLUYE informationdisclosure, LOS PORCENTAJES DE IMPACTO DE CONFIDENCIALIDAD SON LOS SIGUIENTES:  \n")
print("            -    EN  "+str(count_vulnibm_iot_nameinformationdisclosure_highconfimpact+count_vulnibm_sh_nameinformationdisclosure_highconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_iot_nameinformationdisclosure_lowconfimpact+count_vulnibm_sh_nameinformationdisclosure_lowconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_iot_nameinformationdisclosure_mediumconfimpact+count_vulnibm_sh_nameinformationdisclosure_mediumconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_namedenialofservice+count_vulnibm_sh_namedenialofservice)+" VULNERABILIDADES EL NOMBRE INCLUYE denialofservice, LOS PORCENTAJES DE IMPACTO DE CONFIDENCIALIDAD SON LOS SIGUIENTES:  \n")
print("            -    EN  "+str(count_vulnibm_iot_namedenialofservice_highconfimpact+count_vulnibm_sh_namedenialofservice_highconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_iot_namedenialofservice_lowconfimpact+count_vulnibm_sh_namedenialofservice_lowconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_iot_namedenialofservice_mediumconfimpact+count_vulnibm_sh_namedenialofservice_mediumconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_namecodeexecution+count_vulnibm_sh_namecodeexecution)+" VULNERABILIDADES EL NOMBRE INCLUYE codeexecution, LOS PORCENTAJES DE IMPACTO DE CONFIDENCIALIDAD SON LOS SIGUIENTES:  \n")
print("            -    EN  "+str(count_vulnibm_iot_namecodeexecution_highconfimpact+count_vulnibm_sh_namecodeexecution_highconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_iot_namecodeexecution_lowconfimpact+count_vulnibm_sh_namecodeexecution_lowconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_iot_namecodeexecution_mediumconfimpact+count_vulnibm_sh_namecodeexecution_mediumconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_namemaninthemiddle+count_vulnibm_sh_namemaninthemiddle)+" VULNERABILIDADES EL NOMBRE INCLUYE maninthemiddle, LOS PORCENTAJES DE IMPACTO DE CONFIDENCIALIDAD SON LOS SIGUIENTES:  \n")
print("            -    EN  "+str(count_vulnibm_iot_namemaninthemiddle_highconfimpact+count_vulnibm_sh_namemaninthemiddle_highconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_iot_namemaninthemiddle_lowconfimpact+count_vulnibm_sh_namemaninthemiddle_lowconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_iot_namemaninthemiddle_mediumconfimpact+count_vulnibm_sh_namemaninthemiddle_mediumconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_namesqlinjection+count_vulnibm_sh_namesqlinjection)+" VULNERABILIDADES EL NOMBRE INCLUYE sqlinjection, LOS PORCENTAJES DE IMPACTO DE CONFIDENCIALIDAD SON LOS SIGUIENTES:  \n")
print("            -    EN  "+str(count_vulnibm_iot_namesqlinjection_highconfimpact+count_vulnibm_sh_namesqlinjection_highconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_iot_namesqlinjection_lowconfimpact+count_vulnibm_sh_namesqlinjection_lowconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_iot_namesqlinjection_mediumconfimpact+count_vulnibm_sh_namesqlinjection_mediumconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_namecrosssiterequestforgery+count_vulnibm_sh_namecrosssiterequestforgery)+" VULNERABILIDADES EL NOMBRE INCLUYE crosssiterequestforgery, LOS PORCENTAJES DE IMPACTO DE CONFIDENCIALIDAD SON LOS SIGUIENTES:  \n")
print("            -    EN  "+str(count_vulnibm_iot_namecrosssiterequestforgery_highconfimpact+count_vulnibm_sh_namecrosssiterequestforgery_highconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_iot_namecrosssiterequestforgery_lowconfimpact+count_vulnibm_sh_namecrosssiterequestforgery_lowconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_iot_namecrosssiterequestforgery_mediumconfimpact+count_vulnibm_sh_namecrosssiterequestforgery_mediumconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_namemoduleexecution+count_vulnibm_sh_namemoduleexecution)+" VULNERABILIDADES EL NOMBRE INCLUYE moduleexecution, LOS PORCENTAJES DE IMPACTO DE CONFIDENCIALIDAD SON LOS SIGUIENTES:  \n")
print("            -    EN  "+str(count_vulnibm_iot_namemoduleexecution_highconfimpact+count_vulnibm_sh_namemoduleexecution_highconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_iot_namemoduleexecution_lowconfimpact+count_vulnibm_sh_namemoduleexecution_lowconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_iot_namemoduleexecution_mediumconfimpact+count_vulnibm_sh_namemoduleexecution_mediumconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_namebufferoverflow+count_vulnibm_sh_namebufferoverflow)+" VULNERABILIDADES EL NOMBRE INCLUYE bufferoverflow, LOS PORCENTAJES DE IMPACTO DE CONFIDENCIALIDAD SON LOS SIGUIENTES:  \n")
print("            -    EN  "+str(count_vulnibm_iot_namebufferoverflow_highconfimpact+count_vulnibm_sh_namebufferoverflow_highconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_iot_namebufferoverflow_lowconfimpact+count_vulnibm_sh_namebufferoverflow_lowconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_iot_namebufferoverflow_mediumconfimpact+count_vulnibm_sh_namebufferoverflow_mediumconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_namecommandexecution+count_vulnibm_sh_namecommandexecution)+" VULNERABILIDADES EL NOMBRE INCLUYE commandexecution, LOS PORCENTAJES DE IMPACTO DE CONFIDENCIALIDAD SON LOS SIGUIENTES:  \n")
print("            -    EN  "+str(count_vulnibm_iot_namecommandexecution_highconfimpact+count_vulnibm_sh_namecommandexecution_highconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_iot_namecommandexecution_lowconfimpact+count_vulnibm_sh_namecommandexecution_lowconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_iot_namecommandexecution_mediumconfimpact+count_vulnibm_sh_namecommandexecution_mediumconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_namespoofing+count_vulnibm_sh_namespoofing)+" VULNERABILIDADES EL NOMBRE INCLUYE spoofing, LOS PORCENTAJES DE IMPACTO DE CONFIDENCIALIDAD SON LOS SIGUIENTES:  \n")
print("            -    EN  "+str(count_vulnibm_iot_namespoofing_highconfimpact+count_vulnibm_sh_namespoofing_highconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_iot_namespoofing_lowconfimpact+count_vulnibm_sh_namespoofing_lowconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_iot_namespoofing_mediumconfimpact+count_vulnibm_sh_namespoofing_mediumconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_nameclickjacking+count_vulnibm_sh_nameclickjacking)+" VULNERABILIDADES EL NOMBRE INCLUYE clickjacking, LOS PORCENTAJES DE IMPACTO DE CONFIDENCIALIDAD SON LOS SIGUIENTES:  \n")
print("            -    EN  "+str(count_vulnibm_iot_nameclickjacking_highconfimpact+count_vulnibm_sh_nameclickjacking_highconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_iot_nameclickjacking_lowconfimpact+count_vulnibm_sh_nameclickjacking_lowconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_iot_nameclickjacking_mediumconfimpact+count_vulnibm_sh_nameclickjacking_mediumconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_namehijacking+count_vulnibm_sh_namehijacking)+" VULNERABILIDADES EL NOMBRE INCLUYE hijacking, LOS PORCENTAJES DE IMPACTO DE CONFIDENCIALIDAD SON LOS SIGUIENTES:  \n")
print("            -    EN  "+str(count_vulnibm_iot_namehijacking_highconfimpact+count_vulnibm_sh_namehijacking_highconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_iot_namehijacking_lowconfimpact+count_vulnibm_sh_namehijacking_lowconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_iot_namehijacking_mediumconfimpact+count_vulnibm_sh_namehijacking_mediumconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_namefileinclude+count_vulnibm_sh_namefileinclude)+" VULNERABILIDADES EL NOMBRE INCLUYE fileinclude, LOS PORCENTAJES DE IMPACTO DE CONFIDENCIALIDAD SON LOS SIGUIENTES:  \n")
print("            -    EN  "+str(count_vulnibm_iot_namefileinclude_highconfimpact+count_vulnibm_sh_namefileinclude_highconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_iot_namefileinclude_lowconfimpact+count_vulnibm_sh_namefileinclude_lowconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_iot_namefileinclude_mediumconfimpact+count_vulnibm_sh_namefileinclude_mediumconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_namebruteforce+count_vulnibm_sh_namebruteforce)+" VULNERABILIDADES EL NOMBRE INCLUYE bruteforce, LOS PORCENTAJES DE IMPACTO DE CONFIDENCIALIDAD SON LOS SIGUIENTES:  \n")
print("            -    EN  "+str(count_vulnibm_iot_namebruteforce_highconfimpact+count_vulnibm_sh_namebruteforce_highconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_iot_namebruteforce_lowconfimpact+count_vulnibm_sh_namebruteforce_lowconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_iot_namebruteforce_mediumconfimpact+count_vulnibm_sh_namebruteforce_mediumconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_namefileupload+count_vulnibm_sh_namefileupload)+" VULNERABILIDADES EL NOMBRE INCLUYE fileupload, LOS PORCENTAJES DE IMPACTO DE CONFIDENCIALIDAD SON LOS SIGUIENTES:  \n")
print("            -    EN  "+str(count_vulnibm_iot_namefileupload_highconfimpact+count_vulnibm_sh_namefileupload_highconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_iot_namefileupload_lowconfimpact+count_vulnibm_sh_namefileupload_lowconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_iot_namefileupload_mediumconfimpact+count_vulnibm_sh_namefileupload_mediumconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_nameheaderinjection+count_vulnibm_sh_nameheaderinjection)+" VULNERABILIDADES EL NOMBRE INCLUYE headerinjection, LOS PORCENTAJES DE IMPACTO DE CONFIDENCIALIDAD SON LOS SIGUIENTES:  \n")
print("            -    EN  "+str(count_vulnibm_iot_nameheaderinjection_highconfimpact+count_vulnibm_sh_nameheaderinjection_highconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_iot_nameheaderinjection_lowconfimpact+count_vulnibm_sh_nameheaderinjection_lowconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_iot_nameheaderinjection_mediumconfimpact+count_vulnibm_sh_nameheaderinjection_mediumconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_nametampering+count_vulnibm_sh_nametampering)+" VULNERABILIDADES EL NOMBRE INCLUYE tampering, LOS PORCENTAJES DE IMPACTO DE CONFIDENCIALIDAD SON LOS SIGUIENTES:  \n")
print("            -    EN  "+str(count_vulnibm_iot_nametampering_highconfimpact+count_vulnibm_sh_nametampering_highconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_iot_nametampering_lowconfimpact+count_vulnibm_sh_nametampering_lowconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_iot_nametampering_mediumconfimpact+count_vulnibm_sh_nametampering_mediumconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_nameanother+count_vulnibm_sh_nameanother)+" VULNERABILIDADES EL NOMBRE INCLUYE OTRO NOMBRE DISTINTO, LOS PORCENTAJES DE IMPACTO DE CONFIDENCIALIDAD SON LOS SIGUIENTES:  \n")
print("            -    EN  "+str(count_vulnibm_iot_nameanother_highconfimpact+count_vulnibm_sh_nameanother_highconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
print("            -    EN  "+str(count_vulnibm_iot_nameanother_lowconfimpact+count_vulnibm_sh_nameanother_lowconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
print("            -    EN  "+str(count_vulnibm_iot_nameanother_mediumconfimpact+count_vulnibm_sh_nameanother_mediumconfimpact)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO \n")
print("\n")









print("**********************************************PORCENTAJES NOMBRE/IMPACTO DE CONFIDENCIALIDAD VULNERABILIDADES IBM PARTE IOT Y SMART HOME **********************************************")
print("\n")                            
print("\n")
print(" DE UN TOTAL DE "+str(count_vulnibm_iot_names+count_vulnibm_sh_names)+" VULNERABILIDADES:\n") 
print("\n")
print("   - LOS PORCENTAJES DE VALORES DE NOMBRE SON LOS SIGUIENTES:  \n")
print("      -    EN EL "+str(float((((count_vulnibm_iot_namepathtraversal+count_vulnibm_sh_namepathtraversal)*100)/(count_vulnibm_iot_names+count_vulnibm_sh_names))))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE PATHTRAVERSAL, LOS PORCENTAJES DE IMPACTO DE CONFIDENCIALIDAD SON LOS SIGUIENTES:  \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namepathtraversal_highconfimpact+count_vulnibm_sh_namepathtraversal_highconfimpact)*100)/(count_vulnibm_iot_namepathtraversal+count_vulnibm_sh_namepathtraversal))))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namepathtraversal_lowconfimpact+count_vulnibm_sh_namepathtraversal_lowconfimpact)*100)/(count_vulnibm_iot_namepathtraversal+count_vulnibm_sh_namepathtraversal))))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namepathtraversal_mediumconfimpact+count_vulnibm_sh_namepathtraversal_mediumconfimpact)*100)/(count_vulnibm_iot_namepathtraversal+count_vulnibm_sh_namepathtraversal))))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO \n")
print("\n")
print("      -    EN EL "+str(float((((count_vulnibm_iot_namedirectorytraversal+count_vulnibm_sh_namedirectorytraversal)*100)/(count_vulnibm_iot_names+count_vulnibm_sh_names))))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE DIRECTORY TRAVERSAL, LOS PORCENTAJES DE IMPACTO DE CONFIDENCIALIDAD SON LOS SIGUIENTES:  \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namedirectorytraversal_highconfimpact+count_vulnibm_sh_namedirectorytraversal_highconfimpact)*100)/(count_vulnibm_iot_namedirectorytraversal+count_vulnibm_sh_namedirectorytraversal))))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namedirectorytraversal_lowconfimpact+count_vulnibm_sh_namedirectorytraversal_lowconfimpact)*100)/(count_vulnibm_iot_namedirectorytraversal+count_vulnibm_sh_namedirectorytraversal))))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namedirectorytraversal_mediumconfimpact+count_vulnibm_sh_namedirectorytraversal_mediumconfimpact)*100)/(count_vulnibm_iot_namedirectorytraversal+count_vulnibm_sh_namedirectorytraversal))))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO \n")
print("\n")
print("      -    EN EL "+str(float((((count_vulnibm_iot_nameprivilegeescalation+count_vulnibm_sh_nameprivilegeescalation)*100)/(count_vulnibm_iot_names+count_vulnibm_sh_names))))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE PRIVILEGE ESCALATION, LOS PORCENTAJES DE IMPACTO DE CONFIDENCIALIDAD SON LOS SIGUIENTES:  \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_nameprivilegeescalation_highconfimpact+count_vulnibm_sh_nameprivilegeescalation_highconfimpact)*100)/(count_vulnibm_iot_nameprivilegeescalation+count_vulnibm_sh_nameprivilegeescalation))))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_nameprivilegeescalation_lowconfimpact+count_vulnibm_sh_nameprivilegeescalation_lowconfimpact)*100)/(count_vulnibm_iot_nameprivilegeescalation+count_vulnibm_sh_nameprivilegeescalation))))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_nameprivilegeescalation_mediumconfimpact+count_vulnibm_sh_nameprivilegeescalation_mediumconfimpact)*100)/(count_vulnibm_iot_nameprivilegeescalation+count_vulnibm_sh_nameprivilegeescalation))))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO \n")
print("\n")
print("      -    EN EL "+str(float((((count_vulnibm_iot_namecrosssitescripting+count_vulnibm_sh_namecrosssitescripting)*100)/(count_vulnibm_iot_names+count_vulnibm_sh_names))))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE CROSS SITE SCRIPTING, LOS PORCENTAJES DE IMPACTO DE CONFIDENCIALIDAD SON LOS SIGUIENTES:  \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namecrosssitescripting_highconfimpact+count_vulnibm_sh_namecrosssitescripting_highconfimpact)*100)/(count_vulnibm_iot_namecrosssitescripting+count_vulnibm_sh_namecrosssitescripting))))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namecrosssitescripting_lowconfimpact+count_vulnibm_sh_namecrosssitescripting_lowconfimpact)*100)/(count_vulnibm_iot_namecrosssitescripting+count_vulnibm_sh_namecrosssitescripting))))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namecrosssitescripting_mediumconfimpact+count_vulnibm_sh_namecrosssitescripting_mediumconfimpact)*100)/(count_vulnibm_iot_namecrosssitescripting+count_vulnibm_sh_namecrosssitescripting))))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO \n")
print("\n")
print("      -    EN EL "+str(float((((count_vulnibm_iot_namesecuritybypass+count_vulnibm_sh_namesecuritybypass)*100)/(count_vulnibm_iot_names+count_vulnibm_sh_names))))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE SECURITY BYPASS, LOS PORCENTAJES DE IMPACTO DE CONFIDENCIALIDAD SON LOS SIGUIENTES:  \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namesecuritybypass_highconfimpact+count_vulnibm_sh_namesecuritybypass_highconfimpact)*100)/(count_vulnibm_iot_namesecuritybypass+count_vulnibm_sh_namesecuritybypass))))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namesecuritybypass_lowconfimpact+count_vulnibm_sh_namesecuritybypass_lowconfimpact)*100)/(count_vulnibm_iot_namesecuritybypass+count_vulnibm_sh_namesecuritybypass))))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namesecuritybypass_mediumconfimpact+count_vulnibm_sh_namesecuritybypass_mediumconfimpact)*100)/(count_vulnibm_iot_namesecuritybypass+count_vulnibm_sh_namesecuritybypass))))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO \n")
print("\n")
print("      -    EN EL "+str(float((((count_vulnibm_iot_nameinformationdisclosure+count_vulnibm_sh_nameinformationdisclosure)*100)/(count_vulnibm_iot_names+count_vulnibm_sh_names))))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE INFORMATION DISCLOSURE, LOS PORCENTAJES DE IMPACTO DE CONFIDENCIALIDAD SON LOS SIGUIENTES:  \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_nameinformationdisclosure_highconfimpact+count_vulnibm_sh_nameinformationdisclosure_highconfimpact)*100)/(count_vulnibm_iot_nameinformationdisclosure+count_vulnibm_sh_nameinformationdisclosure))))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_nameinformationdisclosure_lowconfimpact+count_vulnibm_sh_nameinformationdisclosure_lowconfimpact)*100)/(count_vulnibm_iot_nameinformationdisclosure+count_vulnibm_sh_nameinformationdisclosure))))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_nameinformationdisclosure_mediumconfimpact+count_vulnibm_sh_nameinformationdisclosure_mediumconfimpact)*100)/(count_vulnibm_iot_nameinformationdisclosure+count_vulnibm_sh_nameinformationdisclosure))))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO \n")
print("\n")
print("      -    EN EL "+str(float((((count_vulnibm_iot_namedenialofservice+count_vulnibm_sh_namedenialofservice)*100)/(count_vulnibm_iot_names+count_vulnibm_sh_names))))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE DENIAL OF SERVICE, LOS PORCENTAJES DE IMPACTO DE CONFIDENCIALIDAD SON LOS SIGUIENTES:  \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namedenialofservice_highconfimpact+count_vulnibm_sh_namedenialofservice_highconfimpact)*100)/(count_vulnibm_iot_namedenialofservice+count_vulnibm_sh_namedenialofservice))))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namedenialofservice_lowconfimpact+count_vulnibm_sh_namedenialofservice_lowconfimpact)*100)/(count_vulnibm_iot_namedenialofservice+count_vulnibm_sh_namedenialofservice))))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namedenialofservice_mediumconfimpact+count_vulnibm_sh_namedenialofservice_mediumconfimpact)*100)/(count_vulnibm_iot_namedenialofservice+count_vulnibm_sh_namedenialofservice))))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO \n")
print("\n")
print("      -    EN EL "+str(float((((count_vulnibm_iot_namecodeexecution+count_vulnibm_sh_namecodeexecution)*100)/(count_vulnibm_iot_names+count_vulnibm_sh_names))))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE CODE EXECUTION, LOS PORCENTAJES DE IMPACTO DE CONFIDENCIALIDAD SON LOS SIGUIENTES:  \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namecodeexecution_highconfimpact+count_vulnibm_sh_namecodeexecution_highconfimpact)*100)/(count_vulnibm_iot_namecodeexecution+count_vulnibm_sh_namecodeexecution))))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namecodeexecution_lowconfimpact+count_vulnibm_sh_namecodeexecution_lowconfimpact)*100)/(count_vulnibm_iot_namecodeexecution+count_vulnibm_sh_namecodeexecution))))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namecodeexecution_mediumconfimpact+count_vulnibm_sh_namecodeexecution_mediumconfimpact)*100)/(count_vulnibm_iot_namecodeexecution+count_vulnibm_sh_namecodeexecution))))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO \n")
print("\n")
print("      -    EN EL "+str(float((((count_vulnibm_iot_namemaninthemiddle+count_vulnibm_sh_namemaninthemiddle)*100)/(count_vulnibm_iot_names+count_vulnibm_sh_names))))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE MAN IN THE MIDDLE, LOS PORCENTAJES DE IMPACTO DE CONFIDENCIALIDAD SON LOS SIGUIENTES:  \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namemaninthemiddle_highconfimpact+count_vulnibm_sh_namemaninthemiddle_highconfimpact)*100)/(count_vulnibm_iot_namemaninthemiddle+count_vulnibm_sh_namemaninthemiddle))))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namemaninthemiddle_lowconfimpact+count_vulnibm_sh_namemaninthemiddle_lowconfimpact)*100)/(count_vulnibm_iot_namemaninthemiddle+count_vulnibm_sh_namemaninthemiddle))))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namemaninthemiddle_mediumconfimpact+count_vulnibm_sh_namemaninthemiddle_mediumconfimpact)*100)/(count_vulnibm_iot_namemaninthemiddle+count_vulnibm_sh_namemaninthemiddle))))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO \n")
print("\n")
print("      -    EN EL "+str(float((((count_vulnibm_iot_namesqlinjection+count_vulnibm_sh_namesqlinjection)*100)/(count_vulnibm_iot_names+count_vulnibm_sh_names))))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE SQL INJECTION, LOS PORCENTAJES DE IMPACTO DE CONFIDENCIALIDAD SON LOS SIGUIENTES:  \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namesqlinjection_highconfimpact+count_vulnibm_sh_namesqlinjection_highconfimpact)*100)/(count_vulnibm_iot_namesqlinjection+count_vulnibm_sh_namesqlinjection))))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namesqlinjection_lowconfimpact+count_vulnibm_sh_namesqlinjection_lowconfimpact)*100)/(count_vulnibm_iot_namesqlinjection+count_vulnibm_sh_namesqlinjection))))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namesqlinjection_mediumconfimpact+count_vulnibm_sh_namesqlinjection_mediumconfimpact)*100)/(count_vulnibm_iot_namesqlinjection+count_vulnibm_sh_namesqlinjection))))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO \n")
print("\n")
print("      -    EN EL "+str(float((((count_vulnibm_iot_namecrosssiterequestforgery+count_vulnibm_sh_namecrosssiterequestforgery)*100)/(count_vulnibm_iot_names+count_vulnibm_sh_names))))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE CROSS SITE REQUEST FORGERY, LOS PORCENTAJES DE IMPACTO DE CONFIDENCIALIDAD SON LOS SIGUIENTES:  \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namecrosssiterequestforgery_highconfimpact+count_vulnibm_sh_namecrosssiterequestforgery_highconfimpact)*100)/(count_vulnibm_iot_namecrosssiterequestforgery+count_vulnibm_sh_namecrosssiterequestforgery))))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namecrosssiterequestforgery_lowconfimpact+count_vulnibm_sh_namecrosssiterequestforgery_lowconfimpact)*100)/(count_vulnibm_iot_namecrosssiterequestforgery+count_vulnibm_sh_namecrosssiterequestforgery))))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namecrosssiterequestforgery_mediumconfimpact+count_vulnibm_sh_namecrosssiterequestforgery_mediumconfimpact)*100)/(count_vulnibm_iot_namecrosssiterequestforgery+count_vulnibm_sh_namecrosssiterequestforgery))))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO \n")
print("\n")
print("      -    EN EL "+str(float((((count_vulnibm_iot_namemoduleexecution+count_vulnibm_sh_namemoduleexecution)*100)/(count_vulnibm_iot_names+count_vulnibm_sh_names))))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE MODULE EXECUTION, LOS PORCENTAJES DE IMPACTO DE CONFIDENCIALIDAD SON LOS SIGUIENTES:  \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namemoduleexecution_highconfimpact+count_vulnibm_sh_namemoduleexecution_highconfimpact)*100)/(count_vulnibm_iot_namemoduleexecution+count_vulnibm_sh_namemoduleexecution))))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namemoduleexecution_lowconfimpact+count_vulnibm_sh_namemoduleexecution_lowconfimpact)*100)/(count_vulnibm_iot_namemoduleexecution+count_vulnibm_sh_namemoduleexecution))))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namemoduleexecution_mediumconfimpact+count_vulnibm_sh_namemoduleexecution_mediumconfimpact)*100)/(count_vulnibm_iot_namemoduleexecution+count_vulnibm_sh_namemoduleexecution))))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO \n")
print("\n")
print("      -    EN EL "+str(float((((count_vulnibm_iot_namebufferoverflow+count_vulnibm_sh_namebufferoverflow)*100)/(count_vulnibm_iot_names+count_vulnibm_sh_names))))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE BUFFER OVERFLOW, LOS PORCENTAJES DE IMPACTO DE CONFIDENCIALIDAD SON LOS SIGUIENTES:  \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namebufferoverflow_highconfimpact+count_vulnibm_sh_namebufferoverflow_highconfimpact)*100)/(count_vulnibm_iot_namebufferoverflow+count_vulnibm_sh_namebufferoverflow))))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namebufferoverflow_lowconfimpact+count_vulnibm_sh_namebufferoverflow_lowconfimpact)*100)/(count_vulnibm_iot_namebufferoverflow+count_vulnibm_sh_namebufferoverflow))))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namebufferoverflow_mediumconfimpact+count_vulnibm_sh_namebufferoverflow_mediumconfimpact)*100)/(count_vulnibm_iot_namebufferoverflow+count_vulnibm_sh_namebufferoverflow))))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO \n")
print("\n")
print("      -    EN EL "+str(float((((count_vulnibm_iot_namecommandexecution+count_vulnibm_sh_namecommandexecution)*100)/(count_vulnibm_iot_names+count_vulnibm_sh_names))))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE COMMAND EXECUTION, LOS PORCENTAJES DE IMPACTO DE CONFIDENCIALIDAD SON LOS SIGUIENTES:  \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namecommandexecution_highconfimpact+count_vulnibm_sh_namecommandexecution_highconfimpact)*100)/(count_vulnibm_iot_namecommandexecution+count_vulnibm_sh_namecommandexecution))))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namecommandexecution_lowconfimpact+count_vulnibm_sh_namecommandexecution_lowconfimpact)*100)/(count_vulnibm_iot_namecommandexecution+count_vulnibm_sh_namecommandexecution))))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namecommandexecution_mediumconfimpact+count_vulnibm_sh_namecommandexecution_mediumconfimpact)*100)/(count_vulnibm_iot_namecommandexecution+count_vulnibm_sh_namecommandexecution))))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO \n")
print("\n")
print("      -    EN EL "+str(float((((count_vulnibm_iot_namespoofing+count_vulnibm_sh_namespoofing)*100)/(count_vulnibm_iot_names+count_vulnibm_sh_names))))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE SPOOFING, LOS PORCENTAJES DE IMPACTO DE CONFIDENCIALIDAD SON LOS SIGUIENTES:  \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namespoofing_highconfimpact+count_vulnibm_sh_namespoofing_highconfimpact)*100)/(count_vulnibm_iot_namespoofing+count_vulnibm_sh_namespoofing))))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namespoofing_lowconfimpact+count_vulnibm_sh_namespoofing_lowconfimpact)*100)/(count_vulnibm_iot_namespoofing+count_vulnibm_sh_namespoofing))))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namespoofing_mediumconfimpact+count_vulnibm_sh_namespoofing_mediumconfimpact)*100)/(count_vulnibm_iot_namespoofing+count_vulnibm_sh_namespoofing))))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO \n")
print("\n")
print("      -    EN EL "+str(float((((count_vulnibm_iot_nameclickjacking+count_vulnibm_sh_nameclickjacking)*100)/(count_vulnibm_iot_names+count_vulnibm_sh_names))))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE CLICKJACKING, LOS PORCENTAJES DE IMPACTO DE CONFIDENCIALIDAD SON LOS SIGUIENTES:  \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_nameclickjacking_highconfimpact+count_vulnibm_sh_nameclickjacking_highconfimpact)*100)/(count_vulnibm_iot_nameclickjacking+count_vulnibm_sh_nameclickjacking))))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_nameclickjacking_lowconfimpact+count_vulnibm_sh_nameclickjacking_lowconfimpact)*100)/(count_vulnibm_iot_nameclickjacking+count_vulnibm_sh_nameclickjacking))))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_nameclickjacking_mediumconfimpact+count_vulnibm_sh_nameclickjacking_mediumconfimpact)*100)/(count_vulnibm_iot_nameclickjacking+count_vulnibm_sh_nameclickjacking))))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO \n")
print("\n")
print("      -    EN EL "+str(float((((count_vulnibm_iot_namehijacking+count_vulnibm_sh_namehijacking)*100)/(count_vulnibm_iot_names+count_vulnibm_sh_names))))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE HIJACKING, LOS PORCENTAJES DE IMPACTO DE CONFIDENCIALIDAD SON LOS SIGUIENTES:  \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namehijacking_highconfimpact+count_vulnibm_sh_namehijacking_highconfimpact)*100)/(count_vulnibm_iot_namehijacking+count_vulnibm_sh_namehijacking))))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namehijacking_lowconfimpact+count_vulnibm_sh_namehijacking_lowconfimpact)*100)/(count_vulnibm_iot_namehijacking+count_vulnibm_sh_namehijacking))))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namehijacking_mediumconfimpact+count_vulnibm_sh_namehijacking_mediumconfimpact)*100)/(count_vulnibm_iot_namehijacking+count_vulnibm_sh_namehijacking))))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO \n")
print("\n")
print("      -    EN EL "+str(float((((count_vulnibm_iot_namefileinclude+count_vulnibm_sh_namefileinclude)*100)/(count_vulnibm_iot_names+count_vulnibm_sh_names))))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE FILE INCLUDE, LOS PORCENTAJES DE IMPACTO DE CONFIDENCIALIDAD SON LOS SIGUIENTES:  \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namefileinclude_highconfimpact+count_vulnibm_sh_namefileinclude_highconfimpact)*100)/(count_vulnibm_iot_namefileinclude+count_vulnibm_sh_namefileinclude))))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namefileinclude_lowconfimpact+count_vulnibm_sh_namefileinclude_lowconfimpact)*100)/(count_vulnibm_iot_namefileinclude+count_vulnibm_sh_namefileinclude))))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namefileinclude_mediumconfimpact+count_vulnibm_sh_namefileinclude_mediumconfimpact)*100)/(count_vulnibm_iot_namefileinclude+count_vulnibm_sh_namefileinclude))))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO \n")
print("\n")
print("      -    EN EL "+str(float((((count_vulnibm_iot_namebruteforce+count_vulnibm_sh_namebruteforce)*100)/(count_vulnibm_iot_names+count_vulnibm_sh_names))))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE BRUTE FORCE, LOS PORCENTAJES DE IMPACTO DE CONFIDENCIALIDAD SON LOS SIGUIENTES:  \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namebruteforce_highconfimpact+count_vulnibm_sh_namebruteforce_highconfimpact)*100)/(count_vulnibm_iot_namebruteforce+count_vulnibm_sh_namebruteforce))))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namebruteforce_lowconfimpact+count_vulnibm_sh_namebruteforce_lowconfimpact)*100)/(count_vulnibm_iot_namebruteforce+count_vulnibm_sh_namebruteforce))))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namebruteforce_mediumconfimpact+count_vulnibm_sh_namebruteforce_mediumconfimpact)*100)/(count_vulnibm_iot_namebruteforce+count_vulnibm_sh_namebruteforce))))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO \n")
print("\n")
print("      -    EN EL "+str(float((((count_vulnibm_iot_namefileupload+count_vulnibm_sh_namefileupload)*100)/(count_vulnibm_iot_names+count_vulnibm_sh_names))))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE FILE UPLOAD, LOS PORCENTAJES DE IMPACTO DE CONFIDENCIALIDAD SON LOS SIGUIENTES:  \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namefileupload_highconfimpact+count_vulnibm_sh_namefileupload_highconfimpact)*100)/(count_vulnibm_iot_namefileupload+count_vulnibm_sh_namefileupload))))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namefileupload_lowconfimpact+count_vulnibm_sh_namefileupload_lowconfimpact)*100)/(count_vulnibm_iot_namefileupload+count_vulnibm_sh_namefileupload))))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namefileupload_mediumconfimpact+count_vulnibm_sh_namefileupload_mediumconfimpact)*100)/(count_vulnibm_iot_namefileupload+count_vulnibm_sh_namefileupload))))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO \n")
print("\n")
print("      -    EN EL "+str(float((((count_vulnibm_iot_nameheaderinjection+count_vulnibm_sh_nameheaderinjection)*100)/(count_vulnibm_iot_names+count_vulnibm_sh_names))))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE HEADER INJECTION, LOS PORCENTAJES DE IMPACTO DE CONFIDENCIALIDAD SON LOS SIGUIENTES:  \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_nameheaderinjection_highconfimpact+count_vulnibm_sh_nameheaderinjection_highconfimpact)*100)/(count_vulnibm_iot_nameheaderinjection+count_vulnibm_sh_nameheaderinjection))))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_nameheaderinjection_lowconfimpact+count_vulnibm_sh_nameheaderinjection_lowconfimpact)*100)/(count_vulnibm_iot_nameheaderinjection+count_vulnibm_sh_nameheaderinjection))))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_nameheaderinjection_mediumconfimpact+count_vulnibm_sh_nameheaderinjection_mediumconfimpact)*100)/(count_vulnibm_iot_nameheaderinjection+count_vulnibm_sh_nameheaderinjection))))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO \n")
print("\n")
print("      -    EN EL "+str(float((((count_vulnibm_iot_nametampering+count_vulnibm_sh_nametampering)*100)/(count_vulnibm_iot_names+count_vulnibm_sh_names))))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE TAMPERING, LOS PORCENTAJES DE IMPACTO DE CONFIDENCIALIDAD SON LOS SIGUIENTES:  \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_nametampering_highconfimpact+count_vulnibm_sh_nametampering_highconfimpact)*100)/(count_vulnibm_iot_nametampering+count_vulnibm_sh_nametampering))))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_nametampering_lowconfimpact+count_vulnibm_sh_nametampering_lowconfimpact)*100)/(count_vulnibm_iot_nametampering+count_vulnibm_sh_nametampering))))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_nametampering_mediumconfimpact+count_vulnibm_sh_nametampering_mediumconfimpact)*100)/(count_vulnibm_iot_nametampering+count_vulnibm_sh_nametampering))))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO \n")
print("\n")
print("      -    EN EL "+str(float((((count_vulnibm_iot_nameanother+count_vulnibm_sh_nameanother)*100)/(count_vulnibm_iot_names+count_vulnibm_sh_names))))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE UN VALOR DISTINTO, LOS PORCENTAJES DE IMPACTO DE CONFIDENCIALIDAD SON LOS SIGUIENTES:  \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_nameanother_highconfimpact+count_vulnibm_sh_nameanother_highconfimpact)*100)/(count_vulnibm_iot_nameanother+count_vulnibm_sh_nameanother))))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_nameanother_lowconfimpact+count_vulnibm_sh_nameanother_lowconfimpact)*100)/(count_vulnibm_iot_nameanother+count_vulnibm_sh_nameanother))))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_nameanother_mediumconfimpact+count_vulnibm_sh_nameanother_mediumconfimpact)*100)/(count_vulnibm_iot_nameanother+count_vulnibm_sh_nameanother))))+" % DE VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO \n")
print("\n")
               	










































