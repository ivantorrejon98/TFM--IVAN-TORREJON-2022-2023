

import pandas as pd
from datetime import datetime,timedelta

df_vulnibm_iot=pd.read_excel('vulnerabilidades_ibm_iot_2023.xlsx')
df_vulnibm_sh=pd.read_excel('vulnerabilidades_ibm_smart_home_2023.xlsx')
df_malwana_iot=pd.read_excel('ibm_analisis_maliciosos_iot_2023_v2.xlsx')
df_malwana_sh=pd.read_excel('ibm_analisis_maliciosos_smarthome_2023.xlsx')
df_thract_iot=pd.read_excel('ibm_threat_activity_report_iot_2023_v2.xlsx')
df_thract_sh=pd.read_excel('ibm_threat_activity_report_smarthome_2023_v2.xlsx')
df_sector_iot=pd.read_excel('ibm_sector_v2.xlsx')
df_malwgroup_sh=pd.read_excel('ibm_grupo_amenazas_2023.xlsx')





#Abro los ficheros con los que voy a tratar



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
count_vulnibm_iot_namebotnet=0
count_vulnibm_iot_namebackdoor=0
count_vulnibm_iot_namespyware=0
count_vulnibm_iot_namephising=0
count_vulnibm_iot_nameransomware=0
count_vulnibm_iot_nametrojan=0
count_vulnibm_iot_namerootkit=0
count_vulnibm_iot_namespam=0
count_vulnibm_iot_namecryptomining=0
count_vulnibm_iot_namesteal=0
count_vulnibm_iot_namedropper=0
count_vulnibm_iot_nameworm=0


#Comprobamos el contenido de name
for r in range(0,len(df_vulnibm_iot["name"])):
    #Obtengo el valor de nombre y aumento contadores segun el tipo que sea
    aux_str=df_vulnibm_iot["name"][r].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
    if(aux_str!='NONE'):
        count_vulnibm_iot_names+=1
        if('pathtraversal' in aux_str or 'Pathtraversal' in aux_str or 'PathTraversal' in aux_str):
            count_vulnibm_iot_namepathtraversal+=1
        elif('directorytraversal' in aux_str or 'Directorytraversal' in aux_str or 'DirectoryTraversal' in aux_str):
            count_vulnibm_iot_namedirectorytraversal+=1
        elif('privilegeescalation' in aux_str or 'Privilegeescalation' in aux_str):
            count_vulnibm_iot_nameprivilegeescalation+=1
        elif('cross-sitescripting' in aux_str or 'xss'in aux_str or 'crosssitescripting' in aux_str):
            count_vulnibm_iot_namecrosssitescripting+=1                            
        elif('securitybypass' in aux_str or 'Securitybypass' in aux_str or 'SecurityBypass' in aux_str):
            count_vulnibm_iot_namesecuritybypass+=1                           
        elif('information_disclosure' in aux_str or 'informationdisclosure' in aux_str):
            count_vulnibm_iot_namesinformationdisclosure+=1                           
        elif('denialofservice' in aux_str or 'DenialOfService' in aux_str or 'DDoS' in aux_str):
            count_vulnibm_iot_namedenialofservice+=1                           
        elif('codeexecution' in aux_str or 'Codeexecution' in aux_str):
            count_vulnibm_iot_namecodeexecution+=1                           
        elif('maninthemiddle' in aux_str or 'Maninthemiddle' in aux_str or 'ManintheMiddle' in aux_str):
            count_vulnibm_iot_namemaninthemiddle+=1                           
        elif('SQLinjection' in aux_str or 'SQLinjection' in aux_str):
            count_vulnibm_iot_namesqlinjection+=1                           
        elif('cross-siterequestforgery' in aux_str or 'Cross-siterequestforgery' in aux_str or 'crosssiterequestforgery' in aux_str or 'Crosssiterequestforgery' in aux_str):
            count_vulnibm_iot_namecrosssiterequestforgery+=1                           
        elif('moduleexecution' in aux_str or 'Moduleexecution' in aux_str or 'ModuleExecution' in aux_str):
            count_vulnibm_iot_namemoduleexecution+=1                           
        elif('bufferoverflow' in aux_str or 'Bufferoverflow' in aux_str or 'BufferOverflow' in aux_str):
            count_vulnibm_iot_namebufferoverflow+=1                           
        elif('commandexecution' in aux_str or 'Commandexecution' in aux_str or 'CommandExecution' in aux_str):
            count_vulnibm_iot_namecommandexecution+=1                           
        elif('spoofing' in aux_str or 'Spoofing' in aux_str):
            count_vulnibm_iot_namespoofing+=1                           
        elif('clickjacking' in aux_str or 'Clickjacking' in aux_str):
            count_vulnibm_iot_nameclickjacking+=1
        elif('hijacking' in aux_str or 'Hijacking' in aux_str):
            count_vulnibm_iot_namehijacking+=1
        elif('fileinclude' in aux_str or 'Fileinclude' in aux_str or 'FileInclude' in aux_str):
            count_vulnibm_iot_namefileinclude+=1
        elif('bruteforce' in aux_str or 'BruteForce' in aux_str or 'Brute-Force' in aux_str):
            count_vulnibm_iot_namebruteforce+=1
        elif('fileupload' in aux_str or 'Fileupload' in aux_str or 'FileUpload' in aux_str):
            count_vulnibm_iot_namefileupload+=1
        elif('headerinjection' in aux_str or 'Headerinjection' in aux_str or 'HeaderInjection' in aux_str):
            count_vulnibm_iot_nameheaderinjection+=1
        elif('Tampering' in aux_str or 'tampering' in aux_str):
            count_vulnibm_iot_nametampering+=1
        elif('Botnet' in aux_str or 'botnet' in aux_str):
            count_vulnibm_iot_namebotnet+=1
        elif('Backdoor' in aux_str or 'backdoor' in aux_str):
            count_vulnibm_iot_namebackdoor+=1
        elif('Spyware' in aux_str or 'spyware' in aux_str):
            count_vulnibm_iot_namespyware+=1
        elif('Phising' in aux_str or 'phising' in aux_str):
            count_vulnibm_iot_namephising+=1
        elif('Ransomware' in aux_str or 'ransomware' in aux_str):
            count_vulnibm_iot_nameransomware+=1
        elif('Trojan' in aux_str or 'trojan' in aux_str):
            count_vulnibm_iot_nametrojan+=1
        elif('Rootkit' in aux_str or 'rootkit' in aux_str):
            count_vulnibm_iot_namerootkit+=1
        elif('spam' in aux_str or 'Spam' in aux_str):
            count_vulnibm_iot_namespam+=1
        elif('Cryptomining' in aux_str or 'CryptoMining' in aux_str or 'cryptomining' in aux_str):
            count_vulnibm_iot_namecryptomining+=1
        elif('Steal' in aux_str or 'steal' in aux_str):
            count_vulnibm_iot_namesteal+=1
        elif('Dropper' in aux_str or 'dropper' in aux_str):
            count_vulnibm_iot_namedropper+=1
        elif('Worm' in aux_str or 'worm' in aux_str):
            count_vulnibm_iot_nameworm+=1
        else:
            count_vulnibm_iot_nameanother+=1
            
            
            
            
            
            
#Comprobamos el contenido de name
for r in range(0,len(df_thract_iot["name"])):
    #Obtengo el valor de nombre y aumento contadores segun el tipo que sea
    aux_str=df_thract_iot["name"][r].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
    if(aux_str!='NONE'):
        count_vulnibm_iot_names+=1
        if('pathtraversal' in aux_str or 'Pathtraversal' in aux_str or 'PathTraversal' in aux_str):
            count_vulnibm_iot_namepathtraversal+=1
        elif('directorytraversal' in aux_str or 'Directorytraversal' in aux_str or 'DirectoryTraversal' in aux_str):
            count_vulnibm_iot_namedirectorytraversal+=1
        elif('privilegeescalation' in aux_str or 'Privilegeescalation' in aux_str):
            count_vulnibm_iot_nameprivilegeescalation+=1
        elif('cross-sitescripting' in aux_str or 'xss'in aux_str or 'crosssitescripting' in aux_str):
            count_vulnibm_iot_namecrosssitescripting+=1                            
        elif('securitybypass' in aux_str or 'Securitybypass' in aux_str or 'SecurityBypass' in aux_str):
            count_vulnibm_iot_namesecuritybypass+=1                           
        elif('information_disclosure' in aux_str or 'informationdisclosure' in aux_str):
            count_vulnibm_iot_namesinformationdisclosure+=1                           
        elif('denialofservice' in aux_str or 'DenialOfService' in aux_str or 'DDoS' in aux_str):
            count_vulnibm_iot_namedenialofservice+=1                           
        elif('codeexecution' in aux_str or 'Codeexecution' in aux_str):
            count_vulnibm_iot_namecodeexecution+=1                           
        elif('maninthemiddle' in aux_str or 'Maninthemiddle' in aux_str or 'ManintheMiddle' in aux_str):
            count_vulnibm_iot_namemaninthemiddle+=1                           
        elif('SQLinjection' in aux_str or 'SQLinjection' in aux_str):
            count_vulnibm_iot_namesqlinjection+=1                           
        elif('cross-siterequestforgery' in aux_str or 'Cross-siterequestforgery' in aux_str or 'crosssiterequestforgery' in aux_str or 'Crosssiterequestforgery' in aux_str):
            count_vulnibm_iot_namecrosssiterequestforgery+=1                           
        elif('moduleexecution' in aux_str or 'Moduleexecution' in aux_str or 'ModuleExecution' in aux_str):
            count_vulnibm_iot_namemoduleexecution+=1                           
        elif('bufferoverflow' in aux_str or 'Bufferoverflow' in aux_str or 'BufferOverflow' in aux_str):
            count_vulnibm_iot_namebufferoverflow+=1                           
        elif('commandexecution' in aux_str or 'Commandexecution' in aux_str or 'CommandExecution' in aux_str):
            count_vulnibm_iot_namecommandexecution+=1                           
        elif('spoofing' in aux_str or 'Spoofing' in aux_str):
            count_vulnibm_iot_namespoofing+=1                           
        elif('clickjacking' in aux_str or 'Clickjacking' in aux_str):
            count_vulnibm_iot_nameclickjacking+=1
        elif('hijacking' in aux_str or 'Hijacking' in aux_str):
            count_vulnibm_iot_namehijacking+=1
        elif('fileinclude' in aux_str or 'Fileinclude' in aux_str or 'FileInclude' in aux_str):
            count_vulnibm_iot_namefileinclude+=1
        elif('bruteforce' in aux_str or 'BruteForce' in aux_str or 'Brute-Force' in aux_str):
            count_vulnibm_iot_namebruteforce+=1
        elif('fileupload' in aux_str or 'Fileupload' in aux_str or 'FileUpload' in aux_str):
            count_vulnibm_iot_namefileupload+=1
        elif('headerinjection' in aux_str or 'Headerinjection' in aux_str or 'HeaderInjection' in aux_str):
            count_vulnibm_iot_nameheaderinjection+=1
        elif('Tampering' in aux_str or 'tampering' in aux_str):
            count_vulnibm_iot_nametampering+=1
        elif('Botnet' in aux_str or 'botnet' in aux_str):
            count_vulnibm_iot_namebotnet+=1
        elif('Backdoor' in aux_str or 'backdoor' in aux_str):
            count_vulnibm_iot_namebackdoor+=1
        elif('Spyware' in aux_str or 'spyware' in aux_str):
            count_vulnibm_iot_namespyware+=1
        elif('Phising' in aux_str or 'phising' in aux_str):
            count_vulnibm_iot_namephising+=1
        elif('Ransomware' in aux_str or 'ransomware' in aux_str):
            count_vulnibm_iot_nameransomware+=1
        elif('Trojan' in aux_str or 'trojan' in aux_str):
            count_vulnibm_iot_nametrojan+=1
        elif('Rootkit' in aux_str or 'rootkit' in aux_str):
            count_vulnibm_iot_namerootkit+=1
        elif('spam' in aux_str or 'Spam' in aux_str):
            count_vulnibm_iot_namespam+=1
        elif('Cryptomining' in aux_str or 'CryptoMining' in aux_str or 'cryptomining' in aux_str):
            count_vulnibm_iot_namecryptomining+=1
        elif('Steal' in aux_str or 'steal' in aux_str):
            count_vulnibm_iot_namesteal+=1
        elif('Dropper' in aux_str or 'dropper' in aux_str):
            count_vulnibm_iot_namedropper+=1
        elif('Worm' in aux_str or 'worm' in aux_str):
            count_vulnibm_iot_nameworm+=1
        else:
            count_vulnibm_iot_nameanother+=1
            
            
            
            
            
            
            
            
            
            
            
            
            
#Comprobamos el contenido de name
for r in range(0,len(df_vulnibm_sh["name"])):
    #Obtengo el valor de nombre y aumento contadores segun el tipo que sea
    aux_str=df_vulnibm_sh["name"][r].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
    if(aux_str!='NONE'):
        count_vulnibm_iot_names+=1
        if('pathtraversal' in aux_str or 'Pathtraversal' in aux_str or 'PathTraversal' in aux_str):
            count_vulnibm_iot_namepathtraversal+=1
        elif('directorytraversal' in aux_str or 'Directorytraversal' in aux_str or 'DirectoryTraversal' in aux_str):
            count_vulnibm_iot_namedirectorytraversal+=1
        elif('privilegeescalation' in aux_str or 'Privilegeescalation' in aux_str):
            count_vulnibm_iot_nameprivilegeescalation+=1
        elif('cross-sitescripting' in aux_str or 'xss'in aux_str or 'crosssitescripting' in aux_str):
            count_vulnibm_iot_namecrosssitescripting+=1                            
        elif('securitybypass' in aux_str or 'Securitybypass' in aux_str or 'SecurityBypass' in aux_str):
            count_vulnibm_iot_namesecuritybypass+=1                           
        elif('information_disclosure' in aux_str or 'informationdisclosure' in aux_str):
            count_vulnibm_iot_namesinformationdisclosure+=1                           
        elif('denialofservice' in aux_str or 'DenialOfService' in aux_str or 'DDoS' in aux_str):
            count_vulnibm_iot_namedenialofservice+=1                           
        elif('codeexecution' in aux_str or 'Codeexecution' in aux_str):
            count_vulnibm_iot_namecodeexecution+=1                           
        elif('maninthemiddle' in aux_str or 'Maninthemiddle' in aux_str or 'ManintheMiddle' in aux_str):
            count_vulnibm_iot_namemaninthemiddle+=1                           
        elif('SQLinjection' in aux_str or 'SQLinjection' in aux_str):
            count_vulnibm_iot_namesqlinjection+=1                           
        elif('cross-siterequestforgery' in aux_str or 'Cross-siterequestforgery' in aux_str or 'crosssiterequestforgery' in aux_str or 'Crosssiterequestforgery' in aux_str):
            count_vulnibm_iot_namecrosssiterequestforgery+=1                           
        elif('moduleexecution' in aux_str or 'Moduleexecution' in aux_str or 'ModuleExecution' in aux_str):
            count_vulnibm_iot_namemoduleexecution+=1                           
        elif('bufferoverflow' in aux_str or 'Bufferoverflow' in aux_str or 'BufferOverflow' in aux_str):
            count_vulnibm_iot_namebufferoverflow+=1                           
        elif('commandexecution' in aux_str or 'Commandexecution' in aux_str or 'CommandExecution' in aux_str):
            count_vulnibm_iot_namecommandexecution+=1                           
        elif('spoofing' in aux_str or 'Spoofing' in aux_str):
            count_vulnibm_iot_namespoofing+=1                           
        elif('clickjacking' in aux_str or 'Clickjacking' in aux_str):
            count_vulnibm_iot_nameclickjacking+=1
        elif('hijacking' in aux_str or 'Hijacking' in aux_str):
            count_vulnibm_iot_namehijacking+=1
        elif('fileinclude' in aux_str or 'Fileinclude' in aux_str or 'FileInclude' in aux_str):
            count_vulnibm_iot_namefileinclude+=1
        elif('bruteforce' in aux_str or 'BruteForce' in aux_str or 'Brute-Force' in aux_str):
            count_vulnibm_iot_namebruteforce+=1
        elif('fileupload' in aux_str or 'Fileupload' in aux_str or 'FileUpload' in aux_str):
            count_vulnibm_iot_namefileupload+=1
        elif('headerinjection' in aux_str or 'Headerinjection' in aux_str or 'HeaderInjection' in aux_str):
            count_vulnibm_iot_nameheaderinjection+=1
        elif('Tampering' in aux_str or 'tampering' in aux_str):
            count_vulnibm_iot_nametampering+=1
        elif('Botnet' in aux_str or 'botnet' in aux_str):
            count_vulnibm_iot_namebotnet+=1
        elif('Backdoor' in aux_str or 'backdoor' in aux_str):
            count_vulnibm_iot_namebackdoor+=1
        elif('Spyware' in aux_str or 'spyware' in aux_str):
            count_vulnibm_iot_namespyware+=1
        elif('Phising' in aux_str or 'phising' in aux_str):
            count_vulnibm_iot_namephising+=1
        elif('Ransomware' in aux_str or 'ransomware' in aux_str):
            count_vulnibm_iot_nameransomware+=1
        elif('Trojan' in aux_str or 'trojan' in aux_str):
            count_vulnibm_iot_nametrojan+=1
        elif('Rootkit' in aux_str or 'rootkit' in aux_str):
            count_vulnibm_iot_namerootkit+=1
        elif('spam' in aux_str or 'Spam' in aux_str):
            count_vulnibm_iot_namespam+=1
        elif('Cryptomining' in aux_str or 'CryptoMining' in aux_str or 'cryptomining' in aux_str):
            count_vulnibm_iot_namecryptomining+=1
        elif('Steal' in aux_str or 'steal' in aux_str):
            count_vulnibm_iot_namesteal+=1
        elif('Dropper' in aux_str or 'dropper' in aux_str):
            count_vulnibm_iot_namedropper+=1
        elif('Worm' in aux_str or 'worm' in aux_str):
            count_vulnibm_iot_nameworm+=1
        else:
            count_vulnibm_iot_nameanother+=1
            
            
            
            
            
            
            
            
#Comprobamos el contenido de name
for r in range(0,len(df_thract_sh["name"])):
    #Obtengo el valor de nombre y aumento contadores segun el tipo que sea
    aux_str=df_thract_sh["name"][r].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
    if(aux_str!='NONE'):
        count_vulnibm_iot_names+=1
        if('pathtraversal' in aux_str or 'Pathtraversal' in aux_str or 'PathTraversal' in aux_str):
            count_vulnibm_iot_namepathtraversal+=1
        elif('directorytraversal' in aux_str or 'Directorytraversal' in aux_str or 'DirectoryTraversal' in aux_str):
            count_vulnibm_iot_namedirectorytraversal+=1
        elif('privilegeescalation' in aux_str or 'Privilegeescalation' in aux_str):
            count_vulnibm_iot_nameprivilegeescalation+=1
        elif('cross-sitescripting' in aux_str or 'xss'in aux_str or 'crosssitescripting' in aux_str):
            count_vulnibm_iot_namecrosssitescripting+=1                            
        elif('securitybypass' in aux_str or 'Securitybypass' in aux_str or 'SecurityBypass' in aux_str):
            count_vulnibm_iot_namesecuritybypass+=1                           
        elif('information_disclosure' in aux_str or 'informationdisclosure' in aux_str):
            count_vulnibm_iot_namesinformationdisclosure+=1                           
        elif('denialofservice' in aux_str or 'DenialOfService' in aux_str or 'DDoS' in aux_str):
            count_vulnibm_iot_namedenialofservice+=1                           
        elif('codeexecution' in aux_str or 'Codeexecution' in aux_str):
            count_vulnibm_iot_namecodeexecution+=1                           
        elif('maninthemiddle' in aux_str or 'Maninthemiddle' in aux_str or 'ManintheMiddle' in aux_str):
            count_vulnibm_iot_namemaninthemiddle+=1                           
        elif('SQLinjection' in aux_str or 'SQLinjection' in aux_str):
            count_vulnibm_iot_namesqlinjection+=1                           
        elif('cross-siterequestforgery' in aux_str or 'Cross-siterequestforgery' in aux_str or 'crosssiterequestforgery' in aux_str or 'Crosssiterequestforgery' in aux_str):
            count_vulnibm_iot_namecrosssiterequestforgery+=1                           
        elif('moduleexecution' in aux_str or 'Moduleexecution' in aux_str or 'ModuleExecution' in aux_str):
            count_vulnibm_iot_namemoduleexecution+=1                           
        elif('bufferoverflow' in aux_str or 'Bufferoverflow' in aux_str or 'BufferOverflow' in aux_str):
            count_vulnibm_iot_namebufferoverflow+=1                           
        elif('commandexecution' in aux_str or 'Commandexecution' in aux_str or 'CommandExecution' in aux_str):
            count_vulnibm_iot_namecommandexecution+=1                           
        elif('spoofing' in aux_str or 'Spoofing' in aux_str):
            count_vulnibm_iot_namespoofing+=1                           
        elif('clickjacking' in aux_str or 'Clickjacking' in aux_str):
            count_vulnibm_iot_nameclickjacking+=1
        elif('hijacking' in aux_str or 'Hijacking' in aux_str):
            count_vulnibm_iot_namehijacking+=1
        elif('fileinclude' in aux_str or 'Fileinclude' in aux_str or 'FileInclude' in aux_str):
            count_vulnibm_iot_namefileinclude+=1
        elif('bruteforce' in aux_str or 'BruteForce' in aux_str or 'Brute-Force' in aux_str):
            count_vulnibm_iot_namebruteforce+=1
        elif('fileupload' in aux_str or 'Fileupload' in aux_str or 'FileUpload' in aux_str):
            count_vulnibm_iot_namefileupload+=1
        elif('headerinjection' in aux_str or 'Headerinjection' in aux_str or 'HeaderInjection' in aux_str):
            count_vulnibm_iot_nameheaderinjection+=1
        elif('Tampering' in aux_str or 'tampering' in aux_str):
            count_vulnibm_iot_nametampering+=1
        elif('Botnet' in aux_str or 'botnet' in aux_str):
            count_vulnibm_iot_namebotnet+=1
        elif('Backdoor' in aux_str or 'backdoor' in aux_str):
            count_vulnibm_iot_namebackdoor+=1
        elif('Spyware' in aux_str or 'spyware' in aux_str):
            count_vulnibm_iot_namespyware+=1
        elif('Phising' in aux_str or 'phising' in aux_str):
            count_vulnibm_iot_namephising+=1
        elif('Ransomware' in aux_str or 'ransomware' in aux_str):
            count_vulnibm_iot_nameransomware+=1
        elif('Trojan' in aux_str or 'trojan' in aux_str):
            count_vulnibm_iot_nametrojan+=1
        elif('Rootkit' in aux_str or 'rootkit' in aux_str):
            count_vulnibm_iot_namerootkit+=1
        elif('spam' in aux_str or 'Spam' in aux_str):
            count_vulnibm_iot_namespam+=1
        elif('Cryptomining' in aux_str or 'CryptoMining' in aux_str or 'cryptomining' in aux_str):
            count_vulnibm_iot_namecryptomining+=1
        elif('Steal' in aux_str or 'steal' in aux_str):
            count_vulnibm_iot_namesteal+=1
        elif('Dropper' in aux_str or 'dropper' in aux_str):
            count_vulnibm_iot_namedropper+=1
        elif('Worm' in aux_str or 'worm' in aux_str):
            count_vulnibm_iot_nameworm+=1
        else:
            count_vulnibm_iot_nameanother+=1
            
            

print("***********************ESTADÍSTICAS CADENAS DE TEXTO CONTENIDAS EN NOMBRE DE OBJETO IBM ***********************")
print("\n")                            
                
print("\n")
print(" DE UN TOTAL DE "+str(count_vulnibm_iot_names)+" VALORES DE NOMBRE :\n") 
print("\n")
print("   - LAS ESTADISTICAS DE TIPO DE ATAQUE SEGUN EL VALOR DE NOMBRE SON LAS SIGUIENTES:  \n")
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
print("            -    EN  "+str(count_vulnibm_iot_namebotnet)+" VULNERABILIDADES , EL NOMBRE INCLUYE BOTNET")
print("            -    EN  "+str(count_vulnibm_iot_namebackdoor)+" VULNERABILIDADES , EL NOMBRE INCLUYE BACKDOOR")
print("            -    EN  "+str(count_vulnibm_iot_namespyware)+" VULNERABILIDADES , EL NOMBRE INCLUYE SPYWARE")
print("            -    EN  "+str(count_vulnibm_iot_namephising)+" VULNERABILIDADES , EL NOMBRE INCLUYE PHISING")
print("            -    EN  "+str(count_vulnibm_iot_nameransomware)+" VULNERABILIDADES , EL NOMBRE INCLUYE RANSOMWARE")
print("            -    EN  "+str(count_vulnibm_iot_nametrojan)+" VULNERABILIDADES , EL NOMBRE INCLUYE TROJAN")
print("            -    EN  "+str(count_vulnibm_iot_namerootkit)+" VULNERABILIDADES , EL NOMBRE INCLUYE ROOTKIT")
print("            -    EN  "+str(count_vulnibm_iot_namespam)+" VULNERABILIDADES , EL NOMBRE INCLUYE SPAM")
print("            -    EN  "+str(count_vulnibm_iot_namecryptomining)+" VULNERABILIDADES , EL NOMBRE INCLUYE CRYPTOMINING")
print("            -    EN  "+str(count_vulnibm_iot_namesteal)+" VULNERABILIDADES , EL NOMBRE INCLUYE STEAL CREDENTIALS")
print("            -    EN  "+str(count_vulnibm_iot_namedropper)+" VULNERABILIDADES , EL NOMBRE INCLUYE DROPPER")
print("            -    EN  "+str(count_vulnibm_iot_nameworm)+" VULNERABILIDADES , EL NOMBRE INCLUYE WORM")
print("            -    EN  "+str(count_vulnibm_iot_nameanother)+" VULNERABILIDADES , EL NOMBRE INCLUYE UN NOMBRE DISTINTO")
print("\n")
                                    





print("***********************PORCENTAJES CADENAS DE TEXTO CONTENIDAS EN NOMBRE DE OBJETO IBM***********************")
print("\n")                            
                
print("\n")
print(" DE UN TOTAL DE "+str(count_vulnibm_iot_names)+" VALORES DE NOMBRE :\n") 
print("\n")
print("   - LOS PORCENTAJES DE TIPO DE ATAQUE SEGUN EL VALOR DE NOMBRE SON LOS SIGUIENTES:  \n")
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
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namebotnet*100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES , EL NOMBRE INCLUYE BOTNET")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namebackdoor*100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES , EL NOMBRE INCLUYE BACKDOOR")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namespyware*100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES , EL NOMBRE INCLUYE SPYWARE")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namephising*100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES , EL NOMBRE INCLUYE PHISING")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_nameransomware*100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES , EL NOMBRE INCLUYE RANSOMWARE")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_nametrojan*100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES , EL NOMBRE INCLUYE TROJAN")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namerootkit*100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES , EL NOMBRE INCLUYE ROOTKIT")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namespam*100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES , EL NOMBRE INCLUYE SPAM")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namecryptomining*100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES , EL NOMBRE INCLUYE CRYPTOMINING")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namesteal*100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES , EL NOMBRE INCLUYE STEAL CREDENTIALS")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namedropper*100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES , EL NOMBRE INCLUYE DROPPER")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_nameworm*100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES , EL NOMBRE INCLUYE WORM")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_nameanother*100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES , EL NOMBRE INCLUYE UN VALOR DISTINTO")
print("\n")
    






















































