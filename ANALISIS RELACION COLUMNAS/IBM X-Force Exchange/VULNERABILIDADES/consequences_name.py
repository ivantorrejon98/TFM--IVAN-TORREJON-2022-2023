
import pandas as pd
from datetime import datetime,timedelta



#Abro los ficheros con los que voy a tratar




df_vulnibm_iot = pd.read_excel('vulnerabilidades_ibm_iot_2023.xlsx')

#Variables donde almacenare el contador total de valores de consecuencias
count_conseq_vulnibm_iot=0

#Variables para almacenador el contador total de valores de nombre dada una consecuencia especifica
count_obtaininfoconseq_namepathtraversal_vulnibm_iot=0
count_obtaininfoconseq_namedirectorytraversal_vulnibm_iot=0
count_obtaininfoconseq_nameprivilegeescalation_vulnibm_iot=0
count_obtaininfoconseq_namecrosssitescripting_vulnibm_iot=0
count_obtaininfoconseq_namesecuritybypass_vulnibm_iot=0
count_obtaininfoconseq_namesinformationdisclosure_vulnibm_iot=0
count_obtaininfoconseq_namedenialofservice_vulnibm_iot=0
count_obtaininfoconseq_namecodeexecution_vulnibm_iot=0
count_obtaininfoconseq_namemaninthemiddle_vulnibm_iot=0
count_obtaininfoconseq_namesqlinjection_vulnibm_iot=0
count_obtaininfoconseq_namecrosssiterequestforgery_vulnibm_iot=0
count_obtaininfoconseq_namemoduleexecution_vulnibm_iot=0
count_obtaininfoconseq_namebufferoverflow_vulnibm_iot=0
count_obtaininfoconseq_namecommandexecution_vulnibm_iot=0
count_obtaininfoconseq_namespoofing_vulnibm_iot=0
count_obtaininfoconseq_nameclickjacking_vulnibm_iot=0
count_obtaininfoconseq_namehijacking_vulnibm_iot=0
count_obtaininfoconseq_namefileinclude_vulnibm_iot=0
count_obtaininfoconseq_namebruteforce_vulnibm_iot=0
count_obtaininfoconseq_namefileupload_vulnibm_iot=0
count_obtaininfoconseq_nameheaderinjection_vulnibm_iot=0
count_obtaininfoconseq_nametampering_vulnibm_iot=0
count_obtaininfoconseq_nameanother_vulnibm_iot=0
#Variable donde almacenamos el contador total de valores de nombre para una consecuencia especifica
count_obtaininfoconseq_vulnibm_iot=0
#Variable donde almacenamos el contador total de valores especificados de nombre para una consecuencia especifica
count_obtaininfoconseq_vulnibm_iot_specified=0


count_xss_conseq_namepathtraversal_vulnibm_iot=0
count_xss_conseq_namedirectorytraversal_vulnibm_iot=0
count_xss_conseq_nameprivilegeescalation_vulnibm_iot=0
count_xss_conseq_namecrosssitescripting_vulnibm_iot=0
count_xss_conseq_namesecuritybypass_vulnibm_iot=0
count_xss_conseq_namesinformationdisclosure_vulnibm_iot=0
count_xss_conseq_namedenialofservice_vulnibm_iot=0
count_xss_conseq_namecodeexecution_vulnibm_iot=0
count_xss_conseq_namemaninthemiddle_vulnibm_iot=0
count_xss_conseq_namesqlinjection_vulnibm_iot=0
count_xss_conseq_namecrosssiterequestforgery_vulnibm_iot=0
count_xss_conseq_namemoduleexecution_vulnibm_iot=0
count_xss_conseq_namebufferoverflow_vulnibm_iot=0
count_xss_conseq_namecommandexecution_vulnibm_iot=0
count_xss_conseq_namespoofing_vulnibm_iot=0
count_xss_conseq_nameclickjacking_vulnibm_iot=0
count_xss_conseq_namehijacking_vulnibm_iot=0
count_xss_conseq_namefileinclude_vulnibm_iot=0
count_xss_conseq_namebruteforce_vulnibm_iot=0
count_xss_conseq_namefileupload_vulnibm_iot=0
count_xss_conseq_nameheaderinjection_vulnibm_iot=0
count_xss_conseq_nametampering_vulnibm_iot=0
count_xss_conseq_nameanother_vulnibm_iot=0
count_xss_conseq_vulnibm_iot=0
count_xss_conseq_vulnibm_iot_specified=0

count_gainacc_conseq_namepathtraversal_vulnibm_iot=0
count_gainacc_conseq_namedirectorytraversal_vulnibm_iot=0
count_gainacc_conseq_nameprivilegeescalation_vulnibm_iot=0
count_gainacc_conseq_namecrosssitescripting_vulnibm_iot=0
count_gainacc_conseq_namesecuritybypass_vulnibm_iot=0
count_gainacc_conseq_namesinformationdisclosure_vulnibm_iot=0
count_gainacc_conseq_namedenialofservice_vulnibm_iot=0
count_gainacc_conseq_namecodeexecution_vulnibm_iot=0
count_gainacc_conseq_namemaninthemiddle_vulnibm_iot=0
count_gainacc_conseq_namesqlinjection_vulnibm_iot=0
count_gainacc_conseq_namecrosssiterequestforgery_vulnibm_iot=0
count_gainacc_conseq_namemoduleexecution_vulnibm_iot=0
count_gainacc_conseq_namebufferoverflow_vulnibm_iot=0
count_gainacc_conseq_namecommandexecution_vulnibm_iot=0
count_gainacc_conseq_namespoofing_vulnibm_iot=0
count_gainacc_conseq_nameclickjacking_vulnibm_iot=0
count_gainacc_conseq_namehijacking_vulnibm_iot=0
count_gainacc_conseq_namefileinclude_vulnibm_iot=0
count_gainacc_conseq_namebruteforce_vulnibm_iot=0
count_gainacc_conseq_namefileupload_vulnibm_iot=0
count_gainacc_conseq_nameheaderinjection_vulnibm_iot=0
count_gainacc_conseq_nametampering_vulnibm_iot=0
count_gainacc_conseq_nameanother_vulnibm_iot=0
count_gainacc_conseq_vulnibm_iot=0
count_gainacc_conseq_vulnibm_iot_specified=0

count_gainpriv_conseq_namepathtraversal_vulnibm_iot=0
count_gainpriv_conseq_namedirectorytraversal_vulnibm_iot=0
count_gainpriv_conseq_nameprivilegeescalation_vulnibm_iot=0
count_gainpriv_conseq_namecrosssitescripting_vulnibm_iot=0
count_gainpriv_conseq_namesecuritybypass_vulnibm_iot=0
count_gainpriv_conseq_namesinformationdisclosure_vulnibm_iot=0
count_gainpriv_conseq_namedenialofservice_vulnibm_iot=0
count_gainpriv_conseq_namecodeexecution_vulnibm_iot=0
count_gainpriv_conseq_namemaninthemiddle_vulnibm_iot=0
count_gainpriv_conseq_namesqlinjection_vulnibm_iot=0
count_gainpriv_conseq_namecrosssiterequestforgery_vulnibm_iot=0
count_gainpriv_conseq_namemoduleexecution_vulnibm_iot=0
count_gainpriv_conseq_namebufferoverflow_vulnibm_iot=0
count_gainpriv_conseq_namecommandexecution_vulnibm_iot=0
count_gainpriv_conseq_namespoofing_vulnibm_iot=0
count_gainpriv_conseq_nameclickjacking_vulnibm_iot=0
count_gainpriv_conseq_namehijacking_vulnibm_iot=0
count_gainpriv_conseq_namefileinclude_vulnibm_iot=0
count_gainpriv_conseq_namebruteforce_vulnibm_iot=0
count_gainpriv_conseq_namefileupload_vulnibm_iot=0
count_gainpriv_conseq_nameheaderinjection_vulnibm_iot=0
count_gainpriv_conseq_nametampering_vulnibm_iot=0
count_gainpriv_conseq_nameanother_vulnibm_iot=0
count_gainpriv_conseq_vulnibm_iot=0
count_gainpriv_conseq_vulnibm_iot_specified=0

count_denialofserv_conseq_namepathtraversal_vulnibm_iot=0
count_denialofserv_conseq_namedirectorytraversal_vulnibm_iot=0
count_denialofserv_conseq_nameprivilegeescalation_vulnibm_iot=0
count_denialofserv_conseq_namecrosssitescripting_vulnibm_iot=0
count_denialofserv_conseq_namesecuritybypass_vulnibm_iot=0
count_denialofserv_conseq_namesinformationdisclosure_vulnibm_iot=0
count_denialofserv_conseq_namedenialofservice_vulnibm_iot=0
count_denialofserv_conseq_namecodeexecution_vulnibm_iot=0
count_denialofserv_conseq_namemaninthemiddle_vulnibm_iot=0
count_denialofserv_conseq_namesqlinjection_vulnibm_iot=0
count_denialofserv_conseq_namecrosssiterequestforgery_vulnibm_iot=0
count_denialofserv_conseq_namemoduleexecution_vulnibm_iot=0
count_denialofserv_conseq_namebufferoverflow_vulnibm_iot=0
count_denialofserv_conseq_namecommandexecution_vulnibm_iot=0
count_denialofserv_conseq_namespoofing_vulnibm_iot=0
count_denialofserv_conseq_nameclickjacking_vulnibm_iot=0
count_denialofserv_conseq_namehijacking_vulnibm_iot=0
count_denialofserv_conseq_namefileinclude_vulnibm_iot=0
count_denialofserv_conseq_namebruteforce_vulnibm_iot=0
count_denialofserv_conseq_namefileupload_vulnibm_iot=0
count_denialofserv_conseq_nameheaderinjection_vulnibm_iot=0
count_denialofserv_conseq_nametampering_vulnibm_iot=0
count_denialofserv_conseq_nameanother_vulnibm_iot=0
count_denialofserv_conseq_vulnibm_iot=0
count_denialofserv_conseq_vulnibm_iot_specified=0

count_bypassec_conseq_namepathtraversal_vulnibm_iot=0
count_bypassec_conseq_namedirectorytraversal_vulnibm_iot=0
count_bypassec_conseq_nameprivilegeescalation_vulnibm_iot=0
count_bypassec_conseq_namecrosssitescripting_vulnibm_iot=0
count_bypassec_conseq_namesecuritybypass_vulnibm_iot=0
count_bypassec_conseq_namesinformationdisclosure_vulnibm_iot=0
count_bypassec_conseq_namedenialofservice_vulnibm_iot=0
count_bypassec_conseq_namecodeexecution_vulnibm_iot=0
count_bypassec_conseq_namemaninthemiddle_vulnibm_iot=0
count_bypassec_conseq_namesqlinjection_vulnibm_iot=0
count_bypassec_conseq_namecrosssiterequestforgery_vulnibm_iot=0
count_bypassec_conseq_namemoduleexecution_vulnibm_iot=0
count_bypassec_conseq_namebufferoverflow_vulnibm_iot=0
count_bypassec_conseq_namecommandexecution_vulnibm_iot=0
count_bypassec_conseq_namespoofing_vulnibm_iot=0
count_bypassec_conseq_nameclickjacking_vulnibm_iot=0
count_bypassec_conseq_namehijacking_vulnibm_iot=0
count_bypassec_conseq_namefileinclude_vulnibm_iot=0
count_bypassec_conseq_namebruteforce_vulnibm_iot=0
count_bypassec_conseq_namefileupload_vulnibm_iot=0
count_bypassec_conseq_nameheaderinjection_vulnibm_iot=0
count_bypassec_conseq_nametampering_vulnibm_iot=0
count_bypassec_conseq_nameanother_vulnibm_iot=0
count_bypassec_conseq_vulnibm_iot=0
count_bypassec_conseq_vulnibm_iot_specified=0

count_filemani_conseq_namepathtraversal_vulnibm_iot=0
count_filemani_conseq_namedirectorytraversal_vulnibm_iot=0
count_filemani_conseq_nameprivilegeescalation_vulnibm_iot=0
count_filemani_conseq_namecrosssitescripting_vulnibm_iot=0
count_filemani_conseq_namesecuritybypass_vulnibm_iot=0
count_filemani_conseq_namesinformationdisclosure_vulnibm_iot=0
count_filemani_conseq_namedenialofservice_vulnibm_iot=0
count_filemani_conseq_namecodeexecution_vulnibm_iot=0
count_filemani_conseq_namemaninthemiddle_vulnibm_iot=0
count_filemani_conseq_namesqlinjection_vulnibm_iot=0
count_filemani_conseq_namecrosssiterequestforgery_vulnibm_iot=0
count_filemani_conseq_namemoduleexecution_vulnibm_iot=0
count_filemani_conseq_namebufferoverflow_vulnibm_iot=0
count_filemani_conseq_namecommandexecution_vulnibm_iot=0
count_filemani_conseq_namespoofing_vulnibm_iot=0
count_filemani_conseq_nameclickjacking_vulnibm_iot=0
count_filemani_conseq_namehijacking_vulnibm_iot=0
count_filemani_conseq_namefileinclude_vulnibm_iot=0
count_filemani_conseq_namebruteforce_vulnibm_iot=0
count_filemani_conseq_namefileupload_vulnibm_iot=0
count_filemani_conseq_nameheaderinjection_vulnibm_iot=0
count_filemani_conseq_nametampering_vulnibm_iot=0
count_filemani_conseq_nameanother_vulnibm_iot=0
count_filemani_conseq_vulnibm_iot=0
count_filemani_conseq_vulnibm_iot_specified=0


count_other_conseq_namepathtraversal_vulnibm_iot=0
count_other_conseq_namedirectorytraversal_vulnibm_iot=0
count_other_conseq_nameprivilegeescalation_vulnibm_iot=0
count_other_conseq_namecrosssitescripting_vulnibm_iot=0
count_other_conseq_namesecuritybypass_vulnibm_iot=0
count_other_conseq_namesinformationdisclosure_vulnibm_iot=0
count_other_conseq_namedenialofservice_vulnibm_iot=0
count_other_conseq_namecodeexecution_vulnibm_iot=0
count_other_conseq_namemaninthemiddle_vulnibm_iot=0
count_other_conseq_namesqlinjection_vulnibm_iot=0
count_other_conseq_namecrosssiterequestforgery_vulnibm_iot=0
count_other_conseq_namemoduleexecution_vulnibm_iot=0
count_other_conseq_namebufferoverflow_vulnibm_iot=0
count_other_conseq_namecommandexecution_vulnibm_iot=0
count_other_conseq_namespoofing_vulnibm_iot=0
count_other_conseq_nameclickjacking_vulnibm_iot=0
count_other_conseq_namehijacking_vulnibm_iot=0
count_other_conseq_namefileinclude_vulnibm_iot=0
count_other_conseq_namebruteforce_vulnibm_iot=0
count_other_conseq_namefileupload_vulnibm_iot=0
count_other_conseq_nameheaderinjection_vulnibm_iot=0
count_other_conseq_nametampering_vulnibm_iot=0
count_other_conseq_nameanother_vulnibm_iot=0
count_other_conseq_vulnibm_iot=0
count_other_conseq_vulnibm_iot_specified=0

#Recorro los valores de CONSECUENCIAS y aumento los contadores segun su valor

for r in range(0,len(df_vulnibm_iot["x_xfe_consequences"])): 
    #Obtengo el valor de la consecuencia
    aux_str=df_vulnibm_iot["x_xfe_consequences"][r].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
    if(aux_str!='NONE' or aux_str!='None'):
        count_conseq_vulnibm_iot+=1
        #Compruebo el valor de la consecuencia
        if(('ObtainInformation' in aux_str) or ('Obtain Information' in aux_str)):
            count_obtaininfoconseq_vulnibm_iot+=1
            #Obtengo el valor de nombre para la fila actual
            auxx_str=df_vulnibm_iot["name"][r].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
            if(auxx_str!='NONE'):
                count_obtaininfoconseq_vulnibm_iot_specified+=1
                if('pathtraversal' in auxx_str):
                    count_obtaininfoconseq_namepathtraversal_vulnibm_iot+=1
                elif('directorytraversal' in auxx_str):
                    count_obtaininfoconseq_namedirectorytraversal_vulnibm_iot+=1
                elif('privilegeescalation' in auxx_str):
                    count_obtaininfoconseq_nameprivilegeescalation_vulnibm_iot+=1
                elif('cross-sitescripting' in auxx_str):
                    count_obtaininfoconseq_namecrosssitescripting_vulnibm_iot+=1                            
                elif('securitybypass' in auxx_str):
                    count_obtaininfoconseq_namesecuritybypass_vulnibm_iot+=1                           
                elif('information_disclosure' in auxx_str or 'informationdisclosure' in auxx_str):
                    count_obtaininfoconseq_namesinformationdisclosure_vulnibm_iot+=1                           
                elif('denialofservice' in auxx_str):
                    count_obtaininfoconseq_namedenialofservice_vulnibm_iot+=1                           
                elif('codeexecution' in auxx_str):
                    count_obtaininfoconseq_namecodeexecution_vulnibm_iot+=1                           
                elif('maninthemiddle' in auxx_str):
                    count_obtaininfoconseq_namemaninthemiddle_vulnibm_iot+=1                           
                elif('SQLinjection' in auxx_str):
                    count_obtaininfoconseq_namesqlinjection_vulnibm_iot+=1                           
                elif('cross-siterequestforgery' in auxx_str):
                    count_obtaininfoconseq_namecrosssiterequestforgery_vulnibm_iot+=1                           
                elif('moduleexecution' in auxx_str):
                    count_obtaininfoconseq_namemoduleexecution_vulnibm_iot+=1                           
                elif('bufferoverflow' in auxx_str):
                    count_obtaininfoconseq_namebufferoverflow_vulnibm_iot+=1                           
                elif('commandexecution' in auxx_str):
                    count_obtaininfoconseq_namecommandexecution_vulnibm_iot+=1                           
                elif('spoofing' in auxx_str):
                    count_obtaininfoconseq_namespoofing_vulnibm_iot+=1                           
                elif('clickjacking' in auxx_str):
                    count_obtaininfoconseq_nameclickjacking_vulnibm_iot+=1
                elif('hijacking' in auxx_str):
                    count_obtaininfoconseq_namehijacking_vulnibm_iot+=1
                elif('fileinclude' in auxx_str):
                    count_obtaininfoconseq_namefileinclude_vulnibm_iot+=1
                elif('bruteforce' in auxx_str):
                    count_obtaininfoconseq_namebruteforce_vulnibm_iot+=1
                elif('fileupload' in auxx_str):
                    count_obtaininfoconseq_namefileupload_vulnibm_iot+=1
                elif('headerinjection' in auxx_str):
                    count_obtaininfoconseq_nameheaderinjection_vulnibm_iot+=1
                elif('Tampering' in auxx_str):
                    count_obtaininfoconseq_nametampering_vulnibm_iot+=1
                else:
                    count_obtaininfoconseq_nameanother_vulnibm_iot+=1
                
        elif('Scripting' in aux_str):
            count_xss_conseq_vulnibm_iot+=1
            auxx_str=df_vulnibm_iot["name"][r].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
            if(auxx_str!='NONE'):
                count_xss_conseq_vulnibm_iot_specified+=1
                if('pathtraversal' in auxx_str):
                    count_xss_conseq_namepathtraversal_vulnibm_iot+=1
                elif('directorytraversal' in auxx_str):
                    count_xss_conseq_namedirectorytraversal_vulnibm_iot+=1
                elif('privilegeescalation' in auxx_str):
                    count_xss_conseq_nameprivilegeescalation_vulnibm_iot+=1
                elif('cross-sitescripting' in auxx_str):
                    count_xss_conseq_namecrosssitescripting_vulnibm_iot+=1                            
                elif('securitybypass' in auxx_str):
                    count_xss_conseq_namesecuritybypass_vulnibm_iot+=1                           
                elif('information_disclosure' in auxx_str or 'informationdisclosure' in auxx_str):
                    count_xss_conseq_namesinformationdisclosure_vulnibm_iot+=1                           
                elif('denialofservice' in auxx_str):
                    count_xss_conseq_namedenialofservice_vulnibm_iot+=1                           
                elif('codeexecution' in auxx_str):
                    count_xss_conseq_namecodeexecution_vulnibm_iot+=1                           
                elif('maninthemiddle' in auxx_str):
                    count_xss_conseq_namemaninthemiddle_vulnibm_iot+=1                           
                elif('SQLinjection' in auxx_str):
                    count_xss_conseq_namesqlinjection_vulnibm_iot+=1                           
                elif('cross-siterequestforgery' in auxx_str):
                    count_xss_conseq_namecrosssiterequestforgery_vulnibm_iot+=1                           
                elif('moduleexecution' in auxx_str):
                    count_xss_conseq_namemoduleexecution_vulnibm_iot+=1                           
                elif('bufferoverflow' in auxx_str):
                    count_xss_conseq_namebufferoverflow_vulnibm_iot+=1                           
                elif('commandexecution' in auxx_str):
                    count_xss_conseq_namecommandexecution_vulnibm_iot+=1                           
                elif('spoofing' in auxx_str):
                    count_xss_conseq_namespoofing_vulnibm_iot+=1                           
                elif('clickjacking' in auxx_str):
                    count_xss_conseq_nameclickjacking_vulnibm_iot+=1
                elif('hijacking' in auxx_str):
                    count_xss_conseq_namehijacking_vulnibm_iot+=1
                elif('fileinclude' in auxx_str):
                    count_xss_conseq_namefileinclude_vulnibm_iot+=1
                elif('bruteforce' in auxx_str):
                    count_xss_conseq_namebruteforce_vulnibm_iot+=1
                elif('fileupload' in auxx_str):
                    count_xss_conseq_namefileupload_vulnibm_iot+=1
                elif('headerinjection' in auxx_str):
                    count_xss_conseq_nameheaderinjection_vulnibm_iot+=1
                elif('Tampering' in auxx_str):
                    count_xss_conseq_nametampering_vulnibm_iot+=1
                else:
                    count_xss_conseq_nameanother_vulnibm_iot+=1
                
        elif('Access' in aux_str):
            count_gainacc_conseq_vulnibm_iot+=1
            auxx_str=df_vulnibm_iot["name"][r].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
            if(auxx_str!='NONE'):
                count_gainacc_conseq_vulnibm_iot_specified+=1
                if('pathtraversal' in auxx_str):
                    count_gainacc_conseq_namepathtraversal_vulnibm_iot+=1
                elif('directorytraversal' in auxx_str):
                    count_gainacc_conseq_namedirectorytraversal_vulnibm_iot+=1
                elif('privilegeescalation' in auxx_str):
                    count_gainacc_conseq_nameprivilegeescalation_vulnibm_iot+=1
                elif('cross-sitescripting' in auxx_str):
                    count_gainacc_conseq_namecrosssitescripting_vulnibm_iot+=1                            
                elif('securitybypass' in auxx_str):
                    count_gainacc_conseq_namesecuritybypass_vulnibm_iot+=1                           
                elif('information_disclosure' in auxx_str or 'informationdisclosure' in auxx_str):
                    count_gainacc_conseq_namesinformationdisclosure_vulnibm_iot+=1                           
                elif('denialofservice' in auxx_str):
                    count_gainacc_conseq_namedenialofservice_vulnibm_iot+=1                           
                elif('codeexecution' in auxx_str):
                    count_gainacc_conseq_namecodeexecution_vulnibm_iot+=1                           
                elif('maninthemiddle' in auxx_str):
                    count_gainacc_conseq_namemaninthemiddle_vulnibm_iot+=1                           
                elif('SQLinjection' in auxx_str):
                    count_gainacc_conseq_namesqlinjection_vulnibm_iot+=1                           
                elif('cross-siterequestforgery' in auxx_str):
                    count_gainacc_conseq_namecrosssiterequestforgery_vulnibm_iot+=1                           
                elif('moduleexecution' in auxx_str):
                    count_gainacc_conseq_namemoduleexecution_vulnibm_iot+=1                           
                elif('bufferoverflow' in auxx_str):
                    count_gainacc_conseq_namebufferoverflow_vulnibm_iot+=1                           
                elif('commandexecution' in auxx_str):
                    count_gainacc_conseq_namecommandexecution_vulnibm_iot+=1                           
                elif('spoofing' in auxx_str):
                    count_gainacc_conseq_namespoofing_vulnibm_iot+=1                           
                elif('clickjacking' in auxx_str):
                    count_gainacc_conseq_nameclickjacking_vulnibm_iot+=1
                elif('hijacking' in auxx_str):
                    count_gainacc_conseq_namehijacking_vulnibm_iot+=1
                elif('fileinclude' in auxx_str):
                    count_gainacc_conseq_namefileinclude_vulnibm_iot+=1
                elif('bruteforce' in auxx_str):
                    count_gainacc_conseq_namebruteforce_vulnibm_iot+=1
                elif('fileupload' in auxx_str):
                    count_gainacc_conseq_namefileupload_vulnibm_iot+=1
                elif('headerinjection' in auxx_str):
                    count_gainacc_conseq_nameheaderinjection_vulnibm_iot+=1
                elif('Tampering' in auxx_str):
                    count_gainacc_conseq_nametampering_vulnibm_iot+=1
                else:
                    count_gainacc_conseq_nameanother_vulnibm_iot+=1
                
        elif('Privilege' in aux_str):
            count_gainpriv_conseq_vulnibm_iot+=1
            auxx_str=df_vulnibm_iot["name"][r].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
            if(auxx_str!='NONE'):
                count_gainpriv_conseq_vulnibm_iot_specified+=1
                if('pathtraversal' in auxx_str):
                    count_gainpriv_conseq_namepathtraversal_vulnibm_iot+=1
                elif('directorytraversal' in auxx_str):
                    count_gainpriv_conseq_namedirectorytraversal_vulnibm_iot+=1
                elif('privilegeescalation' in auxx_str):
                    count_gainpriv_conseq_nameprivilegeescalation_vulnibm_iot+=1
                elif('cross-sitescripting' in auxx_str):
                    count_gainpriv_conseq_namecrosssitescripting_vulnibm_iot+=1                            
                elif('securitybypass' in auxx_str):
                    count_gainpriv_conseq_namesecuritybypass_vulnibm_iot+=1                           
                elif('information_disclosure' in auxx_str or 'informationdisclosure' in auxx_str):
                    count_gainpriv_conseq_namesinformationdisclosure_vulnibm_iot+=1                           
                elif('denialofservice' in auxx_str):
                    count_gainpriv_conseq_namedenialofservice_vulnibm_iot+=1                           
                elif('codeexecution' in auxx_str):
                    count_gainpriv_conseq_namecodeexecution_vulnibm_iot+=1                           
                elif('maninthemiddle' in auxx_str):
                    count_gainpriv_conseq_namemaninthemiddle_vulnibm_iot+=1                           
                elif('SQLinjection' in auxx_str):
                    count_gainpriv_conseq_namesqlinjection_vulnibm_iot+=1                           
                elif('cross-siterequestforgery' in auxx_str):
                    count_gainpriv_conseq_namecrosssiterequestforgery_vulnibm_iot+=1                           
                elif('moduleexecution' in auxx_str):
                    count_gainpriv_conseq_namemoduleexecution_vulnibm_iot+=1                           
                elif('bufferoverflow' in auxx_str):
                    count_gainpriv_conseq_namebufferoverflow_vulnibm_iot+=1                           
                elif('commandexecution' in auxx_str):
                    count_gainpriv_conseq_namecommandexecution_vulnibm_iot+=1                           
                elif('spoofing' in auxx_str):
                    count_gainpriv_conseq_namespoofing_vulnibm_iot+=1                           
                elif('clickjacking' in auxx_str):
                    count_gainpriv_conseq_nameclickjacking_vulnibm_iot+=1
                elif('hijacking' in auxx_str):
                    count_gainpriv_conseq_namehijacking_vulnibm_iot+=1
                elif('fileinclude' in auxx_str):
                    count_gainpriv_conseq_namefileinclude_vulnibm_iot+=1
                elif('bruteforce' in auxx_str):
                    count_gainpriv_conseq_namebruteforce_vulnibm_iot+=1
                elif('fileupload' in auxx_str):
                    count_gainpriv_conseq_namefileupload_vulnibm_iot+=1
                elif('headerinjection' in auxx_str):
                    count_gainpriv_conseq_nameheaderinjection_vulnibm_iot+=1
                elif('Tampering' in auxx_str):
                    count_gainpriv_conseq_nametampering_vulnibm_iot+=1
                else:
                    count_gainpriv_conseq_nameanother_vulnibm_iot+=1
                
        elif('Denial' in aux_str):
            count_denialofserv_conseq_vulnibm_iot+=1
            auxx_str=df_vulnibm_iot["name"][r].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
            if(auxx_str!='NONE'):
                count_denialofserv_conseq_vulnibm_iot_specified+=1
                if('pathtraversal' in auxx_str):
                    count_denialofserv_conseq_namepathtraversal_vulnibm_iot+=1
                elif('directorytraversal' in auxx_str):
                    count_denialofserv_conseq_namedirectorytraversal_vulnibm_iot+=1
                elif('privilegeescalation' in auxx_str):
                    count_denialofserv_conseq_nameprivilegeescalation_vulnibm_iot+=1
                elif('cross-sitescripting' in auxx_str):
                    count_denialofserv_conseq_namecrosssitescripting_vulnibm_iot+=1                            
                elif('securitybypass' in auxx_str):
                    count_denialofserv_conseq_namesecuritybypass_vulnibm_iot+=1                           
                elif('information_disclosure' in auxx_str or 'informationdisclosure' in auxx_str):
                    count_denialofserv_conseq_namesinformationdisclosure_vulnibm_iot+=1                           
                elif('denialofservice' in auxx_str):
                    count_denialofserv_conseq_namedenialofservice_vulnibm_iot+=1                           
                elif('codeexecution' in auxx_str):
                    count_denialofserv_conseq_namecodeexecution_vulnibm_iot+=1                           
                elif('maninthemiddle' in auxx_str):
                    count_denialofserv_conseq_namemaninthemiddle_vulnibm_iot+=1                           
                elif('SQLinjection' in auxx_str):
                    count_denialofserv_conseq_namesqlinjection_vulnibm_iot+=1                           
                elif('cross-siterequestforgery' in auxx_str):
                    count_denialofserv_conseq_namecrosssiterequestforgery_vulnibm_iot+=1                           
                elif('moduleexecution' in auxx_str):
                    count_denialofserv_conseq_namemoduleexecution_vulnibm_iot+=1                           
                elif('bufferoverflow' in auxx_str):
                    count_denialofserv_conseq_namebufferoverflow_vulnibm_iot+=1                           
                elif('commandexecution' in auxx_str):
                    count_denialofserv_conseq_namecommandexecution_vulnibm_iot+=1                           
                elif('spoofing' in auxx_str):
                    count_denialofserv_conseq_namespoofing_vulnibm_iot+=1                           
                elif('clickjacking' in auxx_str):
                    count_denialofserv_conseq_nameclickjacking_vulnibm_iot+=1
                elif('hijacking' in auxx_str):
                    count_denialofserv_conseq_namehijacking_vulnibm_iot+=1
                elif('fileinclude' in auxx_str):
                    count_denialofserv_conseq_namefileinclude_vulnibm_iot+=1
                elif('bruteforce' in auxx_str):
                    count_denialofserv_conseq_namebruteforce_vulnibm_iot+=1
                elif('fileupload' in auxx_str):
                    count_denialofserv_conseq_namefileupload_vulnibm_iot+=1
                elif('headerinjection' in auxx_str):
                    count_denialofserv_conseq_nameheaderinjection_vulnibm_iot+=1
                elif('Tampering' in auxx_str):
                    count_denialofserv_conseq_nametampering_vulnibm_iot+=1
                else:
                    count_denialofserv_conseq_nameanother_vulnibm_iot+=1
        
        elif('Bypass' in aux_str):
            count_bypassec_conseq_vulnibm_iot+=1
            auxx_str=df_vulnibm_iot["name"][r].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
            if(auxx_str!='NONE'):
                count_bypassec_conseq_vulnibm_iot_specified+=1
                if('pathtraversal' in auxx_str):
                    count_bypassec_conseq_namepathtraversal_vulnibm_iot+=1
                elif('directorytraversal' in auxx_str):
                    count_bypassec_conseq_namedirectorytraversal_vulnibm_iot+=1
                elif('privilegeescalation' in auxx_str):
                    count_bypassec_conseq_nameprivilegeescalation_vulnibm_iot+=1
                elif('cross-sitescripting' in auxx_str):
                    count_bypassec_conseq_namecrosssitescripting_vulnibm_iot+=1                            
                elif('securitybypass' in auxx_str):
                    count_bypassec_conseq_namesecuritybypass_vulnibm_iot+=1                           
                elif('information_disclosure' in auxx_str or 'informationdisclosure' in auxx_str):
                    count_bypassec_conseq_namesinformationdisclosure_vulnibm_iot+=1                           
                elif('denialofservice' in auxx_str):
                    count_bypassec_conseq_namedenialofservice_vulnibm_iot+=1                           
                elif('codeexecution' in auxx_str):
                    count_bypassec_conseq_namecodeexecution_vulnibm_iot+=1                           
                elif('maninthemiddle' in auxx_str):
                    count_bypassec_conseq_namemaninthemiddle_vulnibm_iot+=1                           
                elif('SQLinjection' in auxx_str):
                    count_bypassec_conseq_namesqlinjection_vulnibm_iot+=1                           
                elif('cross-siterequestforgery' in auxx_str):
                    count_bypassec_conseq_namecrosssiterequestforgery_vulnibm_iot+=1                           
                elif('moduleexecution' in auxx_str):
                    count_bypassec_conseq_namemoduleexecution_vulnibm_iot+=1                           
                elif('bufferoverflow' in auxx_str):
                    count_bypassec_conseq_namebufferoverflow_vulnibm_iot+=1                           
                elif('commandexecution' in auxx_str):
                    count_bypassec_conseq_namecommandexecution_vulnibm_iot+=1                           
                elif('spoofing' in auxx_str):
                    count_bypassec_conseq_namespoofing_vulnibm_iot+=1                           
                elif('clickjacking' in auxx_str):
                    count_bypassec_conseq_nameclickjacking_vulnibm_iot+=1
                elif('hijacking' in auxx_str):
                    count_bypassec_conseq_namehijacking_vulnibm_iot+=1
                elif('fileinclude' in auxx_str):
                    count_bypassec_conseq_namefileinclude_vulnibm_iot+=1
                elif('bruteforce' in auxx_str):
                    count_bypassec_conseq_namebruteforce_vulnibm_iot+=1
                elif('fileupload' in auxx_str):
                    count_bypassec_conseq_namefileupload_vulnibm_iot+=1
                elif('headerinjection' in auxx_str):
                    count_bypassec_conseq_nameheaderinjection_vulnibm_iot+=1
                elif('Tampering' in auxx_str):
                    count_bypassec_conseq_nametampering_vulnibm_iot+=1
                else:
                    count_bypassec_conseq_nameanother_vulnibm_iot+=1
                
        elif('Manipulation' in aux_str):
            count_filemani_conseq_vulnibm_iot+=1
            auxx_str=df_vulnibm_iot["name"][r].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
            if(auxx_str!='NONE'):
                count_filemani_conseq_vulnibm_iot_specified+=1
                if('pathtraversal' in auxx_str):
                    count_filemani_conseq_namepathtraversal_vulnibm_iot+=1
                elif('directorytraversal' in auxx_str):
                    count_filemani_conseq_namedirectorytraversal_vulnibm_iot+=1
                elif('privilegeescalation' in auxx_str):
                    count_filemani_conseq_nameprivilegeescalation_vulnibm_iot+=1
                elif('cross-sitescripting' in auxx_str):
                    count_filemani_conseq_namecrosssitescripting_vulnibm_iot+=1                            
                elif('securitybypass' in auxx_str):
                    count_filemani_conseq_namesecuritybypass_vulnibm_iot+=1                           
                elif('information_disclosure' in auxx_str or 'informationdisclosure' in auxx_str):
                    count_filemani_conseq_namesinformationdisclosure_vulnibm_iot+=1                           
                elif('filemaniice' in auxx_str):
                    count_filemani_conseq_namedenialofservice_vulnibm_iot+=1                           
                elif('codeexecution' in auxx_str):
                    count_filemani_conseq_namecodeexecution_vulnibm_iot+=1                           
                elif('maninthemiddle' in auxx_str):
                    count_filemani_conseq_namemaninthemiddle_vulnibm_iot+=1                           
                elif('SQLinjection' in auxx_str):
                    count_filemani_conseq_namesqlinjection_vulnibm_iot+=1                           
                elif('cross-siterequestforgery' in auxx_str):
                    count_filemani_conseq_namecrosssiterequestforgery_vulnibm_iot+=1                           
                elif('moduleexecution' in auxx_str):
                    count_filemani_conseq_namemoduleexecution_vulnibm_iot+=1                           
                elif('bufferoverflow' in auxx_str):
                    count_filemani_conseq_namebufferoverflow_vulnibm_iot+=1                           
                elif('commandexecution' in auxx_str):
                    count_filemani_conseq_namecommandexecution_vulnibm_iot+=1                           
                elif('spoofing' in auxx_str):
                    count_filemani_conseq_namespoofing_vulnibm_iot+=1                           
                elif('clickjacking' in auxx_str):
                    count_filemani_conseq_nameclickjacking_vulnibm_iot+=1
                elif('hijacking' in auxx_str):
                    count_filemani_conseq_namehijacking_vulnibm_iot+=1
                elif('fileinclude' in auxx_str):
                    count_filemani_conseq_namefileinclude_vulnibm_iot+=1
                elif('bruteforce' in auxx_str):
                    count_filemani_conseq_namebruteforce_vulnibm_iot+=1
                elif('fileupload' in auxx_str):
                    count_filemani_conseq_namefileupload_vulnibm_iot+=1
                elif('headerinjection' in auxx_str):
                    count_filemani_conseq_nameheaderinjection_vulnibm_iot+=1
                elif('Tampering' in auxx_str):
                    count_filemani_conseq_nametampering_vulnibm_iot+=1
                else:
                    count_filemani_conseq_nameanother_vulnibm_iot+=1
                
        elif('Other' in aux_str):
            count_other_conseq_vulnibm_iot+=1
            auxx_str=df_vulnibm_iot["name"][r].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
            if(auxx_str!='NONE'):
                count_other_conseq_vulnibm_iot_specified+=1
                if('pathtraversal' in auxx_str):
                    count_other_conseq_namepathtraversal_vulnibm_iot+=1
                elif('directorytraversal' in auxx_str):
                    count_other_conseq_namedirectorytraversal_vulnibm_iot+=1
                elif('privilegeescalation' in auxx_str):
                    count_other_conseq_nameprivilegeescalation_vulnibm_iot+=1
                elif('cross-sitescripting' in auxx_str):
                    count_other_conseq_namecrosssitescripting_vulnibm_iot+=1                            
                elif('securitybypass' in auxx_str):
                    count_other_conseq_namesecuritybypass_vulnibm_iot+=1                           
                elif('information_disclosure' in auxx_str or 'informationdisclosure' in auxx_str):
                    count_other_conseq_namesinformationdisclosure_vulnibm_iot+=1                           
                elif('otherice' in auxx_str):
                    count_other_conseq_namedenialofservice_vulnibm_iot+=1                           
                elif('codeexecution' in auxx_str):
                    count_other_conseq_namecodeexecution_vulnibm_iot+=1                           
                elif('maninthemiddle' in auxx_str):
                    count_other_conseq_namemaninthemiddle_vulnibm_iot+=1                           
                elif('SQLinjection' in auxx_str):
                    count_other_conseq_namesqlinjection_vulnibm_iot+=1                           
                elif('cross-siterequestforgery' in auxx_str):
                    count_other_conseq_namecrosssiterequestforgery_vulnibm_iot+=1                           
                elif('moduleexecution' in auxx_str):
                    count_other_conseq_namemoduleexecution_vulnibm_iot+=1                           
                elif('bufferoverflow' in auxx_str):
                    count_other_conseq_namebufferoverflow_vulnibm_iot+=1                           
                elif('commandexecution' in auxx_str):
                    count_other_conseq_namecommandexecution_vulnibm_iot+=1                           
                elif('spoofing' in auxx_str):
                    count_other_conseq_namespoofing_vulnibm_iot+=1                           
                elif('clickjacking' in auxx_str):
                    count_other_conseq_nameclickjacking_vulnibm_iot+=1
                elif('hijacking' in auxx_str):
                    count_other_conseq_namehijacking_vulnibm_iot+=1
                elif('fileinclude' in auxx_str):
                    count_other_conseq_namefileinclude_vulnibm_iot+=1
                elif('bruteforce' in auxx_str):
                    count_other_conseq_namebruteforce_vulnibm_iot+=1
                elif('fileupload' in auxx_str):
                    count_other_conseq_namefileupload_vulnibm_iot+=1
                elif('headerinjection' in auxx_str):
                    count_other_conseq_nameheaderinjection_vulnibm_iot+=1
                elif('Tampering' in auxx_str):
                    count_other_conseq_nametampering_vulnibm_iot+=1
                else:
                    count_other_conseq_nameanother_vulnibm_iot+=1
        
                
                
                
                
                
                
                
                
                
                
                
print("**********************ESTADÍSTICAS CONSECUENCIAS DE ATAQUE/NOMBRE VULNERABILIDADES IBM PARTE IOT**********************")
print("\n")                            
print("\n")
print(" DE UN TOTAL DE "+str(count_conseq_vulnibm_iot)+" VULNERABILIDADES DONDE LAS CONSECUENCIAS VIENEN ESPECIFICADAS:\n") 
print("\n")
print("   - LAS ESTADISTICAS DE CONSECUENCIAS SON LAS SIGUIENTES:  \n")
print("      -    EN  "+str(count_obtaininfoconseq_vulnibm_iot)+" VULNERABILIDADES LA CONSECUENCIA ES LA OBTENCION DE INFORMACION. EL NOMBRE VIENE ESPECIFICADO EN "+str(count_obtaininfoconseq_vulnibm_iot_specified)+" VULNERABILIDADES. LAS ESTADÍSTICAS DE VALORES DE NOMBRE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_obtaininfoconseq_namepathtraversal_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE PATH TRAVERSAL \n")
print("            -    EN  "+str(count_obtaininfoconseq_namedirectorytraversal_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE DIRECTORY TRAVERSAL \n")
print("            -    EN  "+str(count_obtaininfoconseq_nameprivilegeescalation_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE PRIVILEGE ESCALATION \n")
print("            -    EN  "+str(count_obtaininfoconseq_namecrosssitescripting_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE CROSS-SITE SCRIPTING \n")
print("            -    EN  "+str(count_obtaininfoconseq_namesecuritybypass_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE SECURITY BYPASS \n")
print("            -    EN  "+str(count_obtaininfoconseq_namesinformationdisclosure_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE INFORMATION DISCLOSURE \n")
print("            -    EN  "+str(count_obtaininfoconseq_namedenialofservice_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE DENIAL OF SERVICE \n")
print("            -    EN  "+str(count_obtaininfoconseq_namecodeexecution_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE CODE EXECUTION \n")
print("            -    EN  "+str(count_obtaininfoconseq_namemaninthemiddle_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE MAN IN THE MIDDLE \n")
print("            -    EN  "+str(count_obtaininfoconseq_namesqlinjection_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE SQL INJECTION \n")
print("            -    EN  "+str(count_obtaininfoconseq_namemoduleexecution_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE MODULE EXECUTION \n")
print("            -    EN  "+str(count_obtaininfoconseq_namecrosssiterequestforgery_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE CROSS SITE REQUEST FORGERY \n")
print("            -    EN  "+str(count_obtaininfoconseq_namebufferoverflow_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE BUFFER OVERFLOW \n")
print("            -    EN  "+str(count_obtaininfoconseq_namecommandexecution_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE COMMAND EXECUTION \n")
print("            -    EN  "+str(count_obtaininfoconseq_namespoofing_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE SPOOFING \n")
print("            -    EN  "+str(count_obtaininfoconseq_nameclickjacking_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE CLICKJACKING \n")
print("            -    EN  "+str(count_obtaininfoconseq_namehijacking_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE HIJACKING \n")
print("            -    EN  "+str(count_obtaininfoconseq_namefileinclude_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE FILE INCLUDE \n")
print("            -    EN  "+str(count_obtaininfoconseq_namebruteforce_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE BRUTE FORCE \n")
print("            -    EN  "+str(count_obtaininfoconseq_namefileupload_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE FILE UPLOAD \n")
print("            -    EN  "+str(count_obtaininfoconseq_nameheaderinjection_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE HEADER INJECTION \n")
print("            -    EN  "+str(count_obtaininfoconseq_nametampering_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE TAMPERING \n")
print("            -    EN  "+str(count_obtaininfoconseq_nameanother_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE OTRO VALOR DISTINTO A LOS ANTERIORES \n")
print("\n")
print("      -    EN  "+str(count_xss_conseq_vulnibm_iot)+" VULNERABILIDADES LA CONSECUENCIA ES CROSS-SITE SCRIPTING. EL NOMBRE VIENE ESPECIFICADO EN "+str(count_xss_conseq_vulnibm_iot_specified)+" VULNERABILIDADES. LAS ESTADÍSTICAS DE VALORES DE NOMBRE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_xss_conseq_namepathtraversal_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE PATH TRAVERSAL \n")
print("            -    EN  "+str(count_xss_conseq_namedirectorytraversal_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE DIRECTORY TRAVERSAL \n")
print("            -    EN  "+str(count_xss_conseq_nameprivilegeescalation_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE PRIVILEGE ESCALATION \n")
print("            -    EN  "+str(count_xss_conseq_namecrosssitescripting_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE CROSS-SITE SCRIPTING \n")
print("            -    EN  "+str(count_xss_conseq_namesecuritybypass_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE SECURITY BYPASS \n")
print("            -    EN  "+str(count_xss_conseq_namesinformationdisclosure_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE INFORMATION DISCLOSURE \n")
print("            -    EN  "+str(count_xss_conseq_namedenialofservice_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE DENIAL OF SERVICE \n")
print("            -    EN  "+str(count_xss_conseq_namecodeexecution_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE CODE EXECUTION \n")
print("            -    EN  "+str(count_xss_conseq_namemaninthemiddle_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE MAN IN THE MIDDLE \n")
print("            -    EN  "+str(count_xss_conseq_namesqlinjection_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE SQL INJECTION \n")
print("            -    EN  "+str(count_xss_conseq_namemoduleexecution_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE MODULE EXECUTION \n")
print("            -    EN  "+str(count_xss_conseq_namecrosssiterequestforgery_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE CROSS SITE REQUEST FORGERY \n")
print("            -    EN  "+str(count_xss_conseq_namebufferoverflow_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE BUFFER OVERFLOW \n")
print("            -    EN  "+str(count_xss_conseq_namecommandexecution_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE COMMAND EXECUTION \n")
print("            -    EN  "+str(count_xss_conseq_namespoofing_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE SPOOFING \n")
print("            -    EN  "+str(count_xss_conseq_nameclickjacking_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE CLICKJACKING \n")
print("            -    EN  "+str(count_xss_conseq_namehijacking_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE HIJACKING \n")
print("            -    EN  "+str(count_xss_conseq_namefileinclude_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE FILE INCLUDE \n")
print("            -    EN  "+str(count_xss_conseq_namebruteforce_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE BRUTE FORCE \n")
print("            -    EN  "+str(count_xss_conseq_namefileupload_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE FILE UPLOAD \n")
print("            -    EN  "+str(count_xss_conseq_nameheaderinjection_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE HEADER INJECTION \n")
print("            -    EN  "+str(count_xss_conseq_nametampering_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE TAMPERING \n")
print("            -    EN  "+str(count_xss_conseq_nameanother_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE OTRO VALOR DISTINTO A LOS ANTERIORES \n")
print("\n")
print("      -    EN  "+str(count_gainacc_conseq_vulnibm_iot)+" VULNERABILIDADES LA CONSECUENCIA ES LA GANANCIA DE ACCESO. EL NOMBRE VIENE ESPECIFICADO EN "+str(count_gainacc_conseq_vulnibm_iot_specified)+" VULNERABILIDADES. LAS ESTADÍSTICAS DE VALORES DE NOMBRE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_gainacc_conseq_namepathtraversal_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE PATH TRAVERSAL \n")
print("            -    EN  "+str(count_gainacc_conseq_namedirectorytraversal_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE DIRECTORY TRAVERSAL \n")
print("            -    EN  "+str(count_gainacc_conseq_nameprivilegeescalation_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE PRIVILEGE ESCALATION \n")
print("            -    EN  "+str(count_gainacc_conseq_namecrosssitescripting_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE CROSS-SITE SCRIPTING \n")
print("            -    EN  "+str(count_gainacc_conseq_namesecuritybypass_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE SECURITY BYPASS \n")
print("            -    EN  "+str(count_gainacc_conseq_namesinformationdisclosure_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE INFORMATION DISCLOSURE \n")
print("            -    EN  "+str(count_gainacc_conseq_namedenialofservice_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE DENIAL OF SERVICE \n")
print("            -    EN  "+str(count_gainacc_conseq_namecodeexecution_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE CODE EXECUTION \n")
print("            -    EN  "+str(count_gainacc_conseq_namemaninthemiddle_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE MAN IN THE MIDDLE \n")
print("            -    EN  "+str(count_gainacc_conseq_namesqlinjection_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE SQL INJECTION \n")
print("            -    EN  "+str(count_gainacc_conseq_namemoduleexecution_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE MODULE EXECUTION \n")
print("            -    EN  "+str(count_gainacc_conseq_namecrosssiterequestforgery_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE CROSS SITE REQUEST FORGERY \n")
print("            -    EN  "+str(count_gainacc_conseq_namebufferoverflow_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE BUFFER OVERFLOW \n")
print("            -    EN  "+str(count_gainacc_conseq_namecommandexecution_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE COMMAND EXECUTION \n")
print("            -    EN  "+str(count_gainacc_conseq_namespoofing_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE SPOOFING \n")
print("            -    EN  "+str(count_gainacc_conseq_nameclickjacking_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE CLICKJACKING \n")
print("            -    EN  "+str(count_gainacc_conseq_namehijacking_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE HIJACKING \n")
print("            -    EN  "+str(count_gainacc_conseq_namefileinclude_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE FILE INCLUDE \n")
print("            -    EN  "+str(count_gainacc_conseq_namebruteforce_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE BRUTE FORCE \n")
print("            -    EN  "+str(count_gainacc_conseq_namefileupload_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE FILE UPLOAD \n")
print("            -    EN  "+str(count_gainacc_conseq_nameheaderinjection_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE HEADER INJECTION \n")
print("            -    EN  "+str(count_gainacc_conseq_nametampering_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE TAMPERING \n")
print("            -    EN  "+str(count_gainacc_conseq_nameanother_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE OTRO VALOR DISTINTO A LOS ANTERIORES \n")
print("\n")
print("      -    EN  "+str(count_gainpriv_conseq_vulnibm_iot)+" VULNERABILIDADES LA CONSECUENCIA ES LA GANANCIA DE PRIVILEGIOS. EL NOMBRE VIENE ESPECIFICADO EN "+str(count_gainpriv_conseq_vulnibm_iot_specified)+" VULNERABILIDADES. LAS ESTADÍSTICAS DE VALORES DE NOMBRE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_gainpriv_conseq_namepathtraversal_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE PATH TRAVERSAL \n")
print("            -    EN  "+str(count_gainpriv_conseq_namedirectorytraversal_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE DIRECTORY TRAVERSAL \n")
print("            -    EN  "+str(count_gainpriv_conseq_nameprivilegeescalation_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE PRIVILEGE ESCALATION \n")
print("            -    EN  "+str(count_gainpriv_conseq_namecrosssitescripting_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE CROSS-SITE SCRIPTING \n")
print("            -    EN  "+str(count_gainpriv_conseq_namesecuritybypass_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE SECURITY BYPASS \n")
print("            -    EN  "+str(count_gainpriv_conseq_namesinformationdisclosure_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE INFORMATION DISCLOSURE \n")
print("            -    EN  "+str(count_gainpriv_conseq_namedenialofservice_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE DENIAL OF SERVICE \n")
print("            -    EN  "+str(count_gainpriv_conseq_namecodeexecution_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE CODE EXECUTION \n")
print("            -    EN  "+str(count_gainpriv_conseq_namemaninthemiddle_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE MAN IN THE MIDDLE \n")
print("            -    EN  "+str(count_gainpriv_conseq_namesqlinjection_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE SQL INJECTION \n")
print("            -    EN  "+str(count_gainpriv_conseq_namemoduleexecution_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE MODULE EXECUTION \n")
print("            -    EN  "+str(count_gainpriv_conseq_namecrosssiterequestforgery_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE CROSS SITE REQUEST FORGERY \n")
print("            -    EN  "+str(count_gainpriv_conseq_namebufferoverflow_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE BUFFER OVERFLOW \n")
print("            -    EN  "+str(count_gainpriv_conseq_namecommandexecution_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE COMMAND EXECUTION \n")
print("            -    EN  "+str(count_gainpriv_conseq_namespoofing_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE SPOOFING \n")
print("            -    EN  "+str(count_gainpriv_conseq_nameclickjacking_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE CLICKJACKING \n")
print("            -    EN  "+str(count_gainpriv_conseq_namehijacking_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE HIJACKING \n")
print("            -    EN  "+str(count_gainpriv_conseq_namefileinclude_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE FILE INCLUDE \n")
print("            -    EN  "+str(count_gainpriv_conseq_namebruteforce_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE BRUTE FORCE \n")
print("            -    EN  "+str(count_gainpriv_conseq_namefileupload_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE FILE UPLOAD \n")
print("            -    EN  "+str(count_gainpriv_conseq_nameheaderinjection_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE HEADER INJECTION \n")
print("            -    EN  "+str(count_gainpriv_conseq_nametampering_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE TAMPERING \n")
print("            -    EN  "+str(count_gainpriv_conseq_nameanother_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE OTRO VALOR DISTINTO A LOS ANTERIORES \n")
print("\n")
print("      -    EN  "+str(count_denialofserv_conseq_vulnibm_iot)+" VULNERABILIDADES LA CONSECUENCIA ES UNA DENEGACION DE SERVICIO. EL NOMBRE VIENE ESPECIFICADO EN "+str(count_denialofserv_conseq_vulnibm_iot_specified)+" VULNERABILIDADES. LAS ESTADÍSTICAS DE VALORES DE NOMBRE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_denialofserv_conseq_namepathtraversal_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE PATH TRAVERSAL \n")
print("            -    EN  "+str(count_denialofserv_conseq_namedirectorytraversal_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE DIRECTORY TRAVERSAL \n")
print("            -    EN  "+str(count_denialofserv_conseq_nameprivilegeescalation_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE PRIVILEGE ESCALATION \n")
print("            -    EN  "+str(count_denialofserv_conseq_namecrosssitescripting_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE CROSS-SITE SCRIPTING \n")
print("            -    EN  "+str(count_denialofserv_conseq_namesecuritybypass_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE SECURITY BYPASS \n")
print("            -    EN  "+str(count_denialofserv_conseq_namesinformationdisclosure_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE INFORMATION DISCLOSURE \n")
print("            -    EN  "+str(count_denialofserv_conseq_namedenialofservice_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE DENIAL OF SERVICE \n")
print("            -    EN  "+str(count_denialofserv_conseq_namecodeexecution_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE CODE EXECUTION \n")
print("            -    EN  "+str(count_denialofserv_conseq_namemaninthemiddle_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE MAN IN THE MIDDLE \n")
print("            -    EN  "+str(count_denialofserv_conseq_namesqlinjection_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE SQL INJECTION \n")
print("            -    EN  "+str(count_denialofserv_conseq_namemoduleexecution_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE MODULE EXECUTION \n")
print("            -    EN  "+str(count_denialofserv_conseq_namecrosssiterequestforgery_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE CROSS SITE REQUEST FORGERY \n")
print("            -    EN  "+str(count_denialofserv_conseq_namebufferoverflow_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE BUFFER OVERFLOW \n")
print("            -    EN  "+str(count_denialofserv_conseq_namecommandexecution_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE COMMAND EXECUTION \n")
print("            -    EN  "+str(count_denialofserv_conseq_namespoofing_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE SPOOFING \n")
print("            -    EN  "+str(count_denialofserv_conseq_nameclickjacking_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE CLICKJACKING \n")
print("            -    EN  "+str(count_denialofserv_conseq_namehijacking_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE HIJACKING \n")
print("            -    EN  "+str(count_denialofserv_conseq_namefileinclude_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE FILE INCLUDE \n")
print("            -    EN  "+str(count_denialofserv_conseq_namebruteforce_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE BRUTE FORCE \n")
print("            -    EN  "+str(count_denialofserv_conseq_namefileupload_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE FILE UPLOAD \n")
print("            -    EN  "+str(count_denialofserv_conseq_nameheaderinjection_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE HEADER INJECTION \n")
print("            -    EN  "+str(count_denialofserv_conseq_nametampering_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE TAMPERING \n")
print("            -    EN  "+str(count_denialofserv_conseq_nameanother_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE OTRO VALOR DISTINTO A LOS ANTERIORES \n")
print("\n")
print("      -    EN  "+str(count_filemani_conseq_vulnibm_iot)+" VULNERABILIDADES LA CONSECUENCIA ES LA MANIPULACION DE FICHEROS. EL NOMBRE VIENE ESPECIFICADO EN "+str(count_filemani_conseq_vulnibm_iot_specified)+" VULNERABILIDADES. LAS ESTADÍSTICAS DE VALORES DE NOMBRE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_filemani_conseq_namepathtraversal_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE PATH TRAVERSAL \n")
print("            -    EN  "+str(count_filemani_conseq_namedirectorytraversal_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE DIRECTORY TRAVERSAL \n")
print("            -    EN  "+str(count_filemani_conseq_nameprivilegeescalation_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE PRIVILEGE ESCALATION \n")
print("            -    EN  "+str(count_filemani_conseq_namecrosssitescripting_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE CROSS-SITE SCRIPTING \n")
print("            -    EN  "+str(count_filemani_conseq_namesecuritybypass_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE SECURITY BYPASS \n")
print("            -    EN  "+str(count_filemani_conseq_namesinformationdisclosure_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE INFORMATION DISCLOSURE \n")
print("            -    EN  "+str(count_filemani_conseq_namedenialofservice_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE DENIAL OF SERVICE \n")
print("            -    EN  "+str(count_filemani_conseq_namecodeexecution_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE CODE EXECUTION \n")
print("            -    EN  "+str(count_filemani_conseq_namemaninthemiddle_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE MAN IN THE MIDDLE \n")
print("            -    EN  "+str(count_filemani_conseq_namesqlinjection_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE SQL INJECTION \n")
print("            -    EN  "+str(count_filemani_conseq_namemoduleexecution_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE MODULE EXECUTION \n")
print("            -    EN  "+str(count_filemani_conseq_namecrosssiterequestforgery_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE CROSS SITE REQUEST FORGERY \n")
print("            -    EN  "+str(count_filemani_conseq_namebufferoverflow_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE BUFFER OVERFLOW \n")
print("            -    EN  "+str(count_filemani_conseq_namecommandexecution_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE COMMAND EXECUTION \n")
print("            -    EN  "+str(count_filemani_conseq_namespoofing_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE SPOOFING \n")
print("            -    EN  "+str(count_filemani_conseq_nameclickjacking_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE CLICKJACKING \n")
print("            -    EN  "+str(count_filemani_conseq_namehijacking_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE HIJACKING \n")
print("            -    EN  "+str(count_filemani_conseq_namefileinclude_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE FILE INCLUDE \n")
print("            -    EN  "+str(count_filemani_conseq_namebruteforce_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE BRUTE FORCE \n")
print("            -    EN  "+str(count_filemani_conseq_namefileupload_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE FILE UPLOAD \n")
print("            -    EN  "+str(count_filemani_conseq_nameheaderinjection_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE HEADER INJECTION \n")
print("            -    EN  "+str(count_filemani_conseq_nametampering_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE TAMPERING \n")
print("            -    EN  "+str(count_filemani_conseq_nameanother_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE OTRO VALOR DISTINTO A LOS ANTERIORES \n")
print("\n")
print("      -    EN  "+str(count_other_conseq_vulnibm_iot)+" VULNERABILIDADES LA CONSECUENCIA ES OTRA DISTINTA A LAS ANTERIORES. EL NOMBRE VIENE ESPECIFICADO EN "+str(count_other_conseq_vulnibm_iot_specified)+" VULNERABILIDADES. LAS ESTADÍSTICAS DE VALORES DE NOMBRE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_other_conseq_namepathtraversal_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE PATH TRAVERSAL \n")
print("            -    EN  "+str(count_other_conseq_namedirectorytraversal_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE DIRECTORY TRAVERSAL \n")
print("            -    EN  "+str(count_other_conseq_nameprivilegeescalation_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE PRIVILEGE ESCALATION \n")
print("            -    EN  "+str(count_other_conseq_namecrosssitescripting_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE CROSS-SITE SCRIPTING \n")
print("            -    EN  "+str(count_other_conseq_namesecuritybypass_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE SECURITY BYPASS \n")
print("            -    EN  "+str(count_other_conseq_namesinformationdisclosure_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE INFORMATION DISCLOSURE \n")
print("            -    EN  "+str(count_other_conseq_namedenialofservice_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE DENIAL OF SERVICE \n")
print("            -    EN  "+str(count_other_conseq_namecodeexecution_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE CODE EXECUTION \n")
print("            -    EN  "+str(count_other_conseq_namemaninthemiddle_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE MAN IN THE MIDDLE \n")
print("            -    EN  "+str(count_other_conseq_namesqlinjection_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE SQL INJECTION \n")
print("            -    EN  "+str(count_other_conseq_namemoduleexecution_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE MODULE EXECUTION \n")
print("            -    EN  "+str(count_other_conseq_namecrosssiterequestforgery_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE CROSS SITE REQUEST FORGERY \n")
print("            -    EN  "+str(count_other_conseq_namebufferoverflow_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE BUFFER OVERFLOW \n")
print("            -    EN  "+str(count_other_conseq_namecommandexecution_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE COMMAND EXECUTION \n")
print("            -    EN  "+str(count_other_conseq_namespoofing_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE SPOOFING \n")
print("            -    EN  "+str(count_other_conseq_nameclickjacking_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE CLICKJACKING \n")
print("            -    EN  "+str(count_other_conseq_namehijacking_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE HIJACKING \n")
print("            -    EN  "+str(count_other_conseq_namefileinclude_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE FILE INCLUDE \n")
print("            -    EN  "+str(count_other_conseq_namebruteforce_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE BRUTE FORCE \n")
print("            -    EN  "+str(count_other_conseq_namefileupload_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE FILE UPLOAD \n")
print("            -    EN  "+str(count_other_conseq_nameheaderinjection_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE HEADER INJECTION \n")
print("            -    EN  "+str(count_other_conseq_nametampering_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE TAMPERING \n")
print("            -    EN  "+str(count_other_conseq_nameanother_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE OTRO VALOR DISTINTO A LOS ANTERIORES \n")
print("\n")






print("**********************PORCENTAJES CONSECUENCIAS DE ATAQUE/NOMBRE VULNERABILIDADES IBM IOT **********************")
print("\n")                            
print("\n")
print(" DE UN TOTAL DE "+str(count_conseq_vulnibm_iot)+" VULNERABILIDADES :\n") 
print("\n")
print("   - LOS PORCENTAJES DE CONSECUENCIAS SON LOS SIGUIENTES:  \n")
if(count_obtaininfoconseq_vulnibm_iot>0):
    print("      -    EN EL "+str(float((count_obtaininfoconseq_vulnibm_iot*100)/count_conseq_vulnibm_iot))+" % DE VULNERABILIDADES LA CONSECUENCIA ES LA OBTENCION DE INFORMACION. EL NOMBRE VIENE ESPECIFICADO EN EL "+str(float((count_obtaininfoconseq_vulnibm_iot_specified*100)/count_obtaininfoconseq_vulnibm_iot))+" % DE ELLAS. LOS PORCENTAJES DE VALOR DE NOMBRE SON LOS SIGUIENTES :  \n")
    print("            -    EN EL "+str(float((count_obtaininfoconseq_namepathtraversal_vulnibm_iot*100)/count_obtaininfoconseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE PATH TRAVERSAL \n")
    print("            -    EN EL "+str(float((count_obtaininfoconseq_namedirectorytraversal_vulnibm_iot*100)/count_obtaininfoconseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE DIRECTORY TRAVERSAL \n")
    print("            -    EN EL "+str(float((count_obtaininfoconseq_nameprivilegeescalation_vulnibm_iot*100)/count_obtaininfoconseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE PRIVILEGE ESCALATION \n") 
    print("            -    EN EL "+str(float((count_obtaininfoconseq_namecrosssitescripting_vulnibm_iot*100)/count_obtaininfoconseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE CROSS-SITE SCRIPTING  \n")
    print("            -    EN EL "+str(float((count_obtaininfoconseq_namesecuritybypass_vulnibm_iot*100)/count_obtaininfoconseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE SECURITY BYPASS  \n")
    print("            -    EN EL "+str(float((count_obtaininfoconseq_namesinformationdisclosure_vulnibm_iot*100)/count_obtaininfoconseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE INFORMATION DISCLOSURE \n")
    print("            -    EN EL "+str(float((count_obtaininfoconseq_namedenialofservice_vulnibm_iot*100)/count_obtaininfoconseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE DENIAL OF SERVICE  \n")
    print("            -    EN EL "+str(float((count_obtaininfoconseq_namecodeexecution_vulnibm_iot*100)/count_obtaininfoconseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE CODE EXECUTION  \n")
    print("            -    EN EL "+str(float((count_obtaininfoconseq_namemaninthemiddle_vulnibm_iot*100)/count_obtaininfoconseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE MAN IN THE MIDDLE  \n")
    print("            -    EN EL "+str(float((count_obtaininfoconseq_namesqlinjection_vulnibm_iot*100)/count_obtaininfoconseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE SQL INJECTION  \n")
    print("            -    EN EL "+str(float((count_obtaininfoconseq_namecrosssiterequestforgery_vulnibm_iot*100)/count_obtaininfoconseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE MODULE EXECUTION  \n")
    print("            -    EN EL "+str(float((count_obtaininfoconseq_namemoduleexecution_vulnibm_iot*100)/count_obtaininfoconseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE CROSS SITE REQUEST FORGERY  \n")
    print("            -    EN EL "+str(float((count_obtaininfoconseq_namebufferoverflow_vulnibm_iot*100)/count_obtaininfoconseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE BUFFER OVERFLOW \n")
    print("            -    EN EL "+str(float((count_obtaininfoconseq_namecommandexecution_vulnibm_iot*100)/count_obtaininfoconseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE COMMAND EXECUTION  \n")
    print("            -    EN EL "+str(float((count_obtaininfoconseq_namespoofing_vulnibm_iot*100)/count_obtaininfoconseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE SPOOFING  \n")
    print("            -    EN EL "+str(float((count_obtaininfoconseq_nameclickjacking_vulnibm_iot*100)/count_obtaininfoconseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE CLICKJACKING  \n")
    print("            -    EN EL "+str(float((count_obtaininfoconseq_namehijacking_vulnibm_iot*100)/count_obtaininfoconseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE HIJACKING  \n")
    print("            -    EN EL "+str(float((count_obtaininfoconseq_namefileinclude_vulnibm_iot*100)/count_obtaininfoconseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE FILE INCLUDE  \n")
    print("            -    EN EL "+str(float((count_obtaininfoconseq_namebruteforce_vulnibm_iot*100)/count_obtaininfoconseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE BRUTE FORCE  \n")
    print("            -    EN EL "+str(float((count_obtaininfoconseq_namefileupload_vulnibm_iot*100)/count_obtaininfoconseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE FILE UPLOAD  \n")
    print("            -    EN EL "+str(float((count_obtaininfoconseq_nameheaderinjection_vulnibm_iot*100)/count_obtaininfoconseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE HEADER INJECTION \n")
    print("            -    EN EL "+str(float((count_obtaininfoconseq_nametampering_vulnibm_iot*100)/count_obtaininfoconseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE TAMPERING  \n")
    print("            -    EN EL "+str(float((count_obtaininfoconseq_nameanother_vulnibm_iot*100)/count_obtaininfoconseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE OTRO VALOR DISTINTO A LOS ANTERIORES  \n")
    print("\n")
if(count_xss_conseq_vulnibm_iot>0):
    print("      -    EN EL "+str(float((count_xss_conseq_vulnibm_iot*100)/count_conseq_vulnibm_iot))+" % DE VULNERABILIDADES LA CONSECUENCIA ES CROSS SITE SCRIPTING. EL NOMBRE VIENE ESPECIFICADO EN EL "+str(float((count_xss_conseq_vulnibm_iot_specified*100)/count_xss_conseq_vulnibm_iot))+" % DE ELLAS. LOS PORCENTAJES DE VALOR DE NOMBRE SON LOS SIGUIENTES :  \n")
    print("            -    EN EL "+str(float((count_xss_conseq_namepathtraversal_vulnibm_iot*100)/count_xss_conseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE PATH TRAVERSAL \n")
    print("            -    EN EL "+str(float((count_xss_conseq_namedirectorytraversal_vulnibm_iot*100)/count_xss_conseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE DIRECTORY TRAVERSAL \n")
    print("            -    EN EL "+str(float((count_xss_conseq_nameprivilegeescalation_vulnibm_iot*100)/count_xss_conseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE PRIVILEGE ESCALATION \n") 
    print("            -    EN EL "+str(float((count_xss_conseq_namecrosssitescripting_vulnibm_iot*100)/count_xss_conseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE CROSS-SITE SCRIPTING  \n")
    print("            -    EN EL "+str(float((count_xss_conseq_namesecuritybypass_vulnibm_iot*100)/count_xss_conseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE SECURITY BYPASS  \n")
    print("            -    EN EL "+str(float((count_xss_conseq_namesinformationdisclosure_vulnibm_iot*100)/count_xss_conseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE INFORMATION DISCLOSURE \n")
    print("            -    EN EL "+str(float((count_xss_conseq_namedenialofservice_vulnibm_iot*100)/count_xss_conseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE DENIAL OF SERVICE  \n")
    print("            -    EN EL "+str(float((count_xss_conseq_namecodeexecution_vulnibm_iot*100)/count_xss_conseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE CODE EXECUTION  \n")
    print("            -    EN EL "+str(float((count_xss_conseq_namemaninthemiddle_vulnibm_iot*100)/count_xss_conseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE MAN IN THE MIDDLE  \n")
    print("            -    EN EL "+str(float((count_xss_conseq_namesqlinjection_vulnibm_iot*100)/count_xss_conseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE SQL INJECTION  \n")
    print("            -    EN EL "+str(float((count_xss_conseq_namecrosssiterequestforgery_vulnibm_iot*100)/count_xss_conseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE MODULE EXECUTION  \n")
    print("            -    EN EL "+str(float((count_xss_conseq_namemoduleexecution_vulnibm_iot*100)/count_xss_conseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE CROSS SITE REQUEST FORGERY  \n")
    print("            -    EN EL "+str(float((count_xss_conseq_namebufferoverflow_vulnibm_iot*100)/count_xss_conseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE BUFFER OVERFLOW \n")
    print("            -    EN EL "+str(float((count_xss_conseq_namecommandexecution_vulnibm_iot*100)/count_xss_conseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE COMMAND EXECUTION  \n")
    print("            -    EN EL "+str(float((count_xss_conseq_namespoofing_vulnibm_iot*100)/count_xss_conseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE SPOOFING  \n")
    print("            -    EN EL "+str(float((count_xss_conseq_nameclickjacking_vulnibm_iot*100)/count_xss_conseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE CLICKJACKING  \n")
    print("            -    EN EL "+str(float((count_xss_conseq_namehijacking_vulnibm_iot*100)/count_xss_conseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE HIJACKING  \n")
    print("            -    EN EL "+str(float((count_xss_conseq_namefileinclude_vulnibm_iot*100)/count_xss_conseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE FILE INCLUDE  \n")
    print("            -    EN EL "+str(float((count_xss_conseq_namebruteforce_vulnibm_iot*100)/count_xss_conseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE BRUTE FORCE  \n")
    print("            -    EN EL "+str(float((count_xss_conseq_namefileupload_vulnibm_iot*100)/count_xss_conseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE FILE UPLOAD  \n")
    print("            -    EN EL "+str(float((count_xss_conseq_nameheaderinjection_vulnibm_iot*100)/count_xss_conseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE HEADER INJECTION \n")
    print("            -    EN EL "+str(float((count_xss_conseq_nametampering_vulnibm_iot*100)/count_xss_conseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE TAMPERING  \n")
    print("            -    EN EL "+str(float((count_xss_conseq_nameanother_vulnibm_iot*100)/count_xss_conseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE OTRO VALOR DISTINTO A LOS ANTERIORES  \n")
    print("\n")
if(count_gainacc_conseq_vulnibm_iot>0):
    print("      -    EN EL "+str(float((count_gainacc_conseq_vulnibm_iot*100)/count_conseq_vulnibm_iot))+" % DE VULNERABILIDADES LA CONSECUENCIA ES LA OBTENCION ACCESO. EL NOMBRE VIENE ESPECIFICADO EN EL "+str(float((count_gainacc_conseq_vulnibm_iot_specified*100)/count_gainacc_conseq_vulnibm_iot))+" % DE ELLAS. LOS PORCENTAJES DE VALOR DE NOMBRE SON LOS SIGUIENTES :  \n")
    print("            -    EN EL "+str(float((count_gainacc_conseq_namepathtraversal_vulnibm_iot*100)/count_gainacc_conseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE PATH TRAVERSAL \n")
    print("            -    EN EL "+str(float((count_gainacc_conseq_namedirectorytraversal_vulnibm_iot*100)/count_gainacc_conseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE DIRECTORY TRAVERSAL \n")
    print("            -    EN EL "+str(float((count_gainacc_conseq_nameprivilegeescalation_vulnibm_iot*100)/count_gainacc_conseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE PRIVILEGE ESCALATION \n") 
    print("            -    EN EL "+str(float((count_gainacc_conseq_namecrosssitescripting_vulnibm_iot*100)/count_gainacc_conseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE CROSS-SITE SCRIPTING  \n")
    print("            -    EN EL "+str(float((count_gainacc_conseq_namesecuritybypass_vulnibm_iot*100)/count_gainacc_conseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE SECURITY BYPASS  \n")
    print("            -    EN EL "+str(float((count_gainacc_conseq_namesinformationdisclosure_vulnibm_iot*100)/count_gainacc_conseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE INFORMATION DISCLOSURE \n")
    print("            -    EN EL "+str(float((count_gainacc_conseq_namedenialofservice_vulnibm_iot*100)/count_gainacc_conseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE DENIAL OF SERVICE  \n")
    print("            -    EN EL "+str(float((count_gainacc_conseq_namecodeexecution_vulnibm_iot*100)/count_gainacc_conseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE CODE EXECUTION  \n")
    print("            -    EN EL "+str(float((count_gainacc_conseq_namemaninthemiddle_vulnibm_iot*100)/count_gainacc_conseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE MAN IN THE MIDDLE  \n")
    print("            -    EN EL "+str(float((count_gainacc_conseq_namesqlinjection_vulnibm_iot*100)/count_gainacc_conseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE SQL INJECTION  \n")
    print("            -    EN EL "+str(float((count_gainacc_conseq_namecrosssiterequestforgery_vulnibm_iot*100)/count_gainacc_conseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE MODULE EXECUTION  \n")
    print("            -    EN EL "+str(float((count_gainacc_conseq_namemoduleexecution_vulnibm_iot*100)/count_gainacc_conseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE CROSS SITE REQUEST FORGERY  \n")
    print("            -    EN EL "+str(float((count_gainacc_conseq_namebufferoverflow_vulnibm_iot*100)/count_gainacc_conseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE BUFFER OVERFLOW \n")
    print("            -    EN EL "+str(float((count_gainacc_conseq_namecommandexecution_vulnibm_iot*100)/count_gainacc_conseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE COMMAND EXECUTION  \n")
    print("            -    EN EL "+str(float((count_gainacc_conseq_namespoofing_vulnibm_iot*100)/count_gainacc_conseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE SPOOFING  \n")
    print("            -    EN EL "+str(float((count_gainacc_conseq_nameclickjacking_vulnibm_iot*100)/count_gainacc_conseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE CLICKJACKING  \n")
    print("            -    EN EL "+str(float((count_gainacc_conseq_namehijacking_vulnibm_iot*100)/count_gainacc_conseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE HIJACKING  \n")
    print("            -    EN EL "+str(float((count_gainacc_conseq_namefileinclude_vulnibm_iot*100)/count_gainacc_conseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE FILE INCLUDE  \n")
    print("            -    EN EL "+str(float((count_gainacc_conseq_namebruteforce_vulnibm_iot*100)/count_gainacc_conseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE BRUTE FORCE  \n")
    print("            -    EN EL "+str(float((count_gainacc_conseq_namefileupload_vulnibm_iot*100)/count_gainacc_conseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE FILE UPLOAD  \n")
    print("            -    EN EL "+str(float((count_gainacc_conseq_nameheaderinjection_vulnibm_iot*100)/count_gainacc_conseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE HEADER INJECTION \n")
    print("            -    EN EL "+str(float((count_gainacc_conseq_nametampering_vulnibm_iot*100)/count_gainacc_conseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE TAMPERING  \n")
    print("            -    EN EL "+str(float((count_gainacc_conseq_nameanother_vulnibm_iot*100)/count_gainacc_conseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE OTRO VALOR DISTINTO A LOS ANTERIORES  \n")
    print("\n")
if(count_gainpriv_conseq_vulnibm_iot>0):
    print("      -    EN EL "+str(float((count_gainpriv_conseq_vulnibm_iot*100)/count_conseq_vulnibm_iot))+" % DE VULNERABILIDADES LA CONSECUENCIA ES LA OBTENCION DE PRIVILEGIOS. EL NOMBRE VIENE ESPECIFICADO EN EL "+str(float((count_gainpriv_conseq_vulnibm_iot_specified*100)/count_gainpriv_conseq_vulnibm_iot))+" % DE ELLAS. LOS PORCENTAJES DE VALOR DE NOMBRE SON LOS SIGUIENTES :  \n")
    print("            -    EN EL "+str(float((count_gainpriv_conseq_namepathtraversal_vulnibm_iot*100)/count_gainpriv_conseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE PATH TRAVERSAL \n")
    print("            -    EN EL "+str(float((count_gainpriv_conseq_namedirectorytraversal_vulnibm_iot*100)/count_gainpriv_conseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE DIRECTORY TRAVERSAL \n")
    print("            -    EN EL "+str(float((count_gainpriv_conseq_nameprivilegeescalation_vulnibm_iot*100)/count_gainpriv_conseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE PRIVILEGE ESCALATION \n") 
    print("            -    EN EL "+str(float((count_gainpriv_conseq_namecrosssitescripting_vulnibm_iot*100)/count_gainpriv_conseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE CROSS-SITE SCRIPTING  \n")
    print("            -    EN EL "+str(float((count_gainpriv_conseq_namesecuritybypass_vulnibm_iot*100)/count_gainpriv_conseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE SECURITY BYPASS  \n")
    print("            -    EN EL "+str(float((count_gainpriv_conseq_namesinformationdisclosure_vulnibm_iot*100)/count_gainpriv_conseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE INFORMATION DISCLOSURE \n")
    print("            -    EN EL "+str(float((count_gainpriv_conseq_namedenialofservice_vulnibm_iot*100)/count_gainpriv_conseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE DENIAL OF SERVICE  \n")
    print("            -    EN EL "+str(float((count_gainpriv_conseq_namecodeexecution_vulnibm_iot*100)/count_gainpriv_conseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE CODE EXECUTION  \n")
    print("            -    EN EL "+str(float((count_gainpriv_conseq_namemaninthemiddle_vulnibm_iot*100)/count_gainpriv_conseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE MAN IN THE MIDDLE  \n")
    print("            -    EN EL "+str(float((count_gainpriv_conseq_namesqlinjection_vulnibm_iot*100)/count_gainpriv_conseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE SQL INJECTION  \n")
    print("            -    EN EL "+str(float((count_gainpriv_conseq_namecrosssiterequestforgery_vulnibm_iot*100)/count_gainpriv_conseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE MODULE EXECUTION  \n")
    print("            -    EN EL "+str(float((count_gainpriv_conseq_namemoduleexecution_vulnibm_iot*100)/count_gainpriv_conseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE CROSS SITE REQUEST FORGERY  \n")
    print("            -    EN EL "+str(float((count_gainpriv_conseq_namebufferoverflow_vulnibm_iot*100)/count_gainpriv_conseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE BUFFER OVERFLOW \n")
    print("            -    EN EL "+str(float((count_gainpriv_conseq_namecommandexecution_vulnibm_iot*100)/count_gainpriv_conseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE COMMAND EXECUTION  \n")
    print("            -    EN EL "+str(float((count_gainpriv_conseq_namespoofing_vulnibm_iot*100)/count_gainpriv_conseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE SPOOFING  \n")
    print("            -    EN EL "+str(float((count_gainpriv_conseq_nameclickjacking_vulnibm_iot*100)/count_gainpriv_conseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE CLICKJACKING  \n")
    print("            -    EN EL "+str(float((count_gainpriv_conseq_namehijacking_vulnibm_iot*100)/count_gainpriv_conseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE HIJACKING  \n")
    print("            -    EN EL "+str(float((count_gainpriv_conseq_namefileinclude_vulnibm_iot*100)/count_gainpriv_conseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE FILE INCLUDE  \n")
    print("            -    EN EL "+str(float((count_gainpriv_conseq_namebruteforce_vulnibm_iot*100)/count_gainpriv_conseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE BRUTE FORCE  \n")
    print("            -    EN EL "+str(float((count_gainpriv_conseq_namefileupload_vulnibm_iot*100)/count_gainpriv_conseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE FILE UPLOAD  \n")
    print("            -    EN EL "+str(float((count_gainpriv_conseq_nameheaderinjection_vulnibm_iot*100)/count_gainpriv_conseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE HEADER INJECTION \n")
    print("            -    EN EL "+str(float((count_gainpriv_conseq_nametampering_vulnibm_iot*100)/count_gainpriv_conseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE TAMPERING  \n")
    print("            -    EN EL "+str(float((count_gainpriv_conseq_nameanother_vulnibm_iot*100)/count_gainpriv_conseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE OTRO VALOR DISTINTO A LOS ANTERIORES  \n")
    print("\n")

if(count_denialofserv_conseq_vulnibm_iot>0):
    print("      -    EN EL "+str(float((count_denialofserv_conseq_vulnibm_iot*100)/count_conseq_vulnibm_iot))+" % DE VULNERABILIDADES LA CONSECUENCIA ES UNA DENEGACION DE SERVICIO. EL NOMBRE VIENE ESPECIFICADO EN EL "+str(float((count_denialofserv_conseq_vulnibm_iot_specified*100)/count_denialofserv_conseq_vulnibm_iot))+" % DE ELLAS. LOS PORCENTAJES DE VALOR DE NOMBRE SON LOS SIGUIENTES :  \n")
    print("            -    EN EL "+str(float((count_denialofserv_conseq_namepathtraversal_vulnibm_iot*100)/count_denialofserv_conseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE PATH TRAVERSAL \n")
    print("            -    EN EL "+str(float((count_denialofserv_conseq_namedirectorytraversal_vulnibm_iot*100)/count_denialofserv_conseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE DIRECTORY TRAVERSAL \n")
    print("            -    EN EL "+str(float((count_denialofserv_conseq_nameprivilegeescalation_vulnibm_iot*100)/count_denialofserv_conseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE PRIVILEGE ESCALATION \n") 
    print("            -    EN EL "+str(float((count_denialofserv_conseq_namecrosssitescripting_vulnibm_iot*100)/count_denialofserv_conseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE CROSS-SITE SCRIPTING  \n")
    print("            -    EN EL "+str(float((count_denialofserv_conseq_namesecuritybypass_vulnibm_iot*100)/count_denialofserv_conseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE SECURITY BYPASS  \n")
    print("            -    EN EL "+str(float((count_denialofserv_conseq_namesinformationdisclosure_vulnibm_iot*100)/count_denialofserv_conseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE INFORMATION DISCLOSURE \n")
    print("            -    EN EL "+str(float((count_denialofserv_conseq_namedenialofservice_vulnibm_iot*100)/count_denialofserv_conseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE DENIAL OF SERVICE  \n")
    print("            -    EN EL "+str(float((count_denialofserv_conseq_namecodeexecution_vulnibm_iot*100)/count_denialofserv_conseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE CODE EXECUTION  \n")
    print("            -    EN EL "+str(float((count_denialofserv_conseq_namemaninthemiddle_vulnibm_iot*100)/count_denialofserv_conseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE MAN IN THE MIDDLE  \n")
    print("            -    EN EL "+str(float((count_denialofserv_conseq_namesqlinjection_vulnibm_iot*100)/count_denialofserv_conseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE SQL INJECTION  \n")
    print("            -    EN EL "+str(float((count_denialofserv_conseq_namecrosssiterequestforgery_vulnibm_iot*100)/count_denialofserv_conseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE MODULE EXECUTION  \n")
    print("            -    EN EL "+str(float((count_denialofserv_conseq_namemoduleexecution_vulnibm_iot*100)/count_denialofserv_conseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE CROSS SITE REQUEST FORGERY  \n")
    print("            -    EN EL "+str(float((count_denialofserv_conseq_namebufferoverflow_vulnibm_iot*100)/count_denialofserv_conseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE BUFFER OVERFLOW \n")
    print("            -    EN EL "+str(float((count_denialofserv_conseq_namecommandexecution_vulnibm_iot*100)/count_denialofserv_conseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE COMMAND EXECUTION  \n")
    print("            -    EN EL "+str(float((count_denialofserv_conseq_namespoofing_vulnibm_iot*100)/count_denialofserv_conseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE SPOOFING  \n")
    print("            -    EN EL "+str(float((count_denialofserv_conseq_nameclickjacking_vulnibm_iot*100)/count_denialofserv_conseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE CLICKJACKING  \n")
    print("            -    EN EL "+str(float((count_denialofserv_conseq_namehijacking_vulnibm_iot*100)/count_denialofserv_conseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE HIJACKING  \n")
    print("            -    EN EL "+str(float((count_denialofserv_conseq_namefileinclude_vulnibm_iot*100)/count_denialofserv_conseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE FILE INCLUDE  \n")
    print("            -    EN EL "+str(float((count_denialofserv_conseq_namebruteforce_vulnibm_iot*100)/count_denialofserv_conseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE BRUTE FORCE  \n")
    print("            -    EN EL "+str(float((count_denialofserv_conseq_namefileupload_vulnibm_iot*100)/count_denialofserv_conseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE FILE UPLOAD  \n")
    print("            -    EN EL "+str(float((count_denialofserv_conseq_nameheaderinjection_vulnibm_iot*100)/count_denialofserv_conseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE HEADER INJECTION \n")
    print("            -    EN EL "+str(float((count_denialofserv_conseq_nametampering_vulnibm_iot*100)/count_denialofserv_conseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE TAMPERING  \n")
    print("            -    EN EL "+str(float((count_denialofserv_conseq_nameanother_vulnibm_iot*100)/count_denialofserv_conseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE OTRO VALOR DISTINTO A LOS ANTERIORES  \n")
    print("\n")
    
if(count_bypassec_conseq_vulnibm_iot>0):
    print("      -    EN EL "+str(float((count_bypassec_conseq_vulnibm_iot*100)/count_conseq_vulnibm_iot))+" % DE VULNERABILIDADES LA CONSECUENCIA ES SOBREPASAR LA SEGURIDAD. EL NOMBRE VIENE ESPECIFICADO EN EL "+str(float((count_bypassec_conseq_vulnibm_iot_specified*100)/count_bypassec_conseq_vulnibm_iot))+" % DE ELLAS. LOS PORCENTAJES DE VALOR DE NOMBRE SON LOS SIGUIENTES :  \n")
    print("            -    EN EL "+str(float((count_bypassec_conseq_namepathtraversal_vulnibm_iot*100)/count_bypassec_conseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE PATH TRAVERSAL \n")
    print("            -    EN EL "+str(float((count_bypassec_conseq_namedirectorytraversal_vulnibm_iot*100)/count_bypassec_conseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE DIRECTORY TRAVERSAL \n")
    print("            -    EN EL "+str(float((count_bypassec_conseq_nameprivilegeescalation_vulnibm_iot*100)/count_bypassec_conseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE PRIVILEGE ESCALATION \n") 
    print("            -    EN EL "+str(float((count_bypassec_conseq_namecrosssitescripting_vulnibm_iot*100)/count_bypassec_conseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE CROSS-SITE SCRIPTING  \n")
    print("            -    EN EL "+str(float((count_bypassec_conseq_namesecuritybypass_vulnibm_iot*100)/count_bypassec_conseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE SECURITY BYPASS  \n")
    print("            -    EN EL "+str(float((count_bypassec_conseq_namesinformationdisclosure_vulnibm_iot*100)/count_bypassec_conseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE INFORMATION DISCLOSURE \n")
    print("            -    EN EL "+str(float((count_bypassec_conseq_namedenialofservice_vulnibm_iot*100)/count_bypassec_conseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE DENIAL OF SERVICE  \n")
    print("            -    EN EL "+str(float((count_bypassec_conseq_namecodeexecution_vulnibm_iot*100)/count_bypassec_conseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE CODE EXECUTION  \n")
    print("            -    EN EL "+str(float((count_bypassec_conseq_namemaninthemiddle_vulnibm_iot*100)/count_bypassec_conseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE MAN IN THE MIDDLE  \n")
    print("            -    EN EL "+str(float((count_bypassec_conseq_namesqlinjection_vulnibm_iot*100)/count_bypassec_conseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE SQL INJECTION  \n")
    print("            -    EN EL "+str(float((count_bypassec_conseq_namecrosssiterequestforgery_vulnibm_iot*100)/count_bypassec_conseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE MODULE EXECUTION  \n")
    print("            -    EN EL "+str(float((count_bypassec_conseq_namemoduleexecution_vulnibm_iot*100)/count_bypassec_conseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE CROSS SITE REQUEST FORGERY  \n")
    print("            -    EN EL "+str(float((count_bypassec_conseq_namebufferoverflow_vulnibm_iot*100)/count_bypassec_conseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE BUFFER OVERFLOW \n")
    print("            -    EN EL "+str(float((count_bypassec_conseq_namecommandexecution_vulnibm_iot*100)/count_bypassec_conseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE COMMAND EXECUTION  \n")
    print("            -    EN EL "+str(float((count_bypassec_conseq_namespoofing_vulnibm_iot*100)/count_bypassec_conseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE SPOOFING  \n")
    print("            -    EN EL "+str(float((count_bypassec_conseq_nameclickjacking_vulnibm_iot*100)/count_bypassec_conseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE CLICKJACKING  \n")
    print("            -    EN EL "+str(float((count_bypassec_conseq_namehijacking_vulnibm_iot*100)/count_bypassec_conseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE HIJACKING  \n")
    print("            -    EN EL "+str(float((count_bypassec_conseq_namefileinclude_vulnibm_iot*100)/count_bypassec_conseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE FILE INCLUDE  \n")
    print("            -    EN EL "+str(float((count_bypassec_conseq_namebruteforce_vulnibm_iot*100)/count_bypassec_conseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE BRUTE FORCE  \n")
    print("            -    EN EL "+str(float((count_bypassec_conseq_namefileupload_vulnibm_iot*100)/count_bypassec_conseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE FILE UPLOAD  \n")
    print("            -    EN EL "+str(float((count_bypassec_conseq_nameheaderinjection_vulnibm_iot*100)/count_bypassec_conseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE HEADER INJECTION \n")
    print("            -    EN EL "+str(float((count_bypassec_conseq_nametampering_vulnibm_iot*100)/count_bypassec_conseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE TAMPERING  \n")
    print("            -    EN EL "+str(float((count_bypassec_conseq_nameanother_vulnibm_iot*100)/count_bypassec_conseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE OTRO VALOR DISTINTO A LOS ANTERIORES  \n")
    print("\n")  

if(count_filemani_conseq_vulnibm_iot>0):
    print("      -    EN EL "+str(float((count_filemani_conseq_vulnibm_iot*100)/count_conseq_vulnibm_iot))+" % DE VULNERABILIDADES LA CONSECUENCIA ES MANIPULACION DE FICHEROS. EL NOMBRE VIENE ESPECIFICADO EN EL "+str(float((count_filemani_conseq_vulnibm_iot_specified*100)/count_filemani_conseq_vulnibm_iot))+" % DE ELLAS. LOS PORCENTAJES DE VALOR DE NOMBRE SON LOS SIGUIENTES :  \n")
    print("            -    EN EL "+str(float((count_filemani_conseq_namepathtraversal_vulnibm_iot*100)/count_filemani_conseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE PATH TRAVERSAL \n")
    print("            -    EN EL "+str(float((count_filemani_conseq_namedirectorytraversal_vulnibm_iot*100)/count_filemani_conseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE DIRECTORY TRAVERSAL \n")
    print("            -    EN EL "+str(float((count_filemani_conseq_nameprivilegeescalation_vulnibm_iot*100)/count_filemani_conseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE PRIVILEGE ESCALATION \n") 
    print("            -    EN EL "+str(float((count_filemani_conseq_namecrosssitescripting_vulnibm_iot*100)/count_filemani_conseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE CROSS-SITE SCRIPTING  \n")
    print("            -    EN EL "+str(float((count_filemani_conseq_namesecuritybypass_vulnibm_iot*100)/count_filemani_conseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE SECURITY BYPASS  \n")
    print("            -    EN EL "+str(float((count_filemani_conseq_namesinformationdisclosure_vulnibm_iot*100)/count_filemani_conseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE INFORMATION DISCLOSURE \n")
    print("            -    EN EL "+str(float((count_filemani_conseq_namedenialofservice_vulnibm_iot*100)/count_filemani_conseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE DENIAL OF SERVICE  \n")
    print("            -    EN EL "+str(float((count_filemani_conseq_namecodeexecution_vulnibm_iot*100)/count_filemani_conseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE CODE EXECUTION  \n")
    print("            -    EN EL "+str(float((count_filemani_conseq_namemaninthemiddle_vulnibm_iot*100)/count_filemani_conseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE MAN IN THE MIDDLE  \n")
    print("            -    EN EL "+str(float((count_filemani_conseq_namesqlinjection_vulnibm_iot*100)/count_filemani_conseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE SQL INJECTION  \n")
    print("            -    EN EL "+str(float((count_filemani_conseq_namecrosssiterequestforgery_vulnibm_iot*100)/count_filemani_conseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE MODULE EXECUTION  \n")
    print("            -    EN EL "+str(float((count_filemani_conseq_namemoduleexecution_vulnibm_iot*100)/count_filemani_conseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE CROSS SITE REQUEST FORGERY  \n")
    print("            -    EN EL "+str(float((count_filemani_conseq_namebufferoverflow_vulnibm_iot*100)/count_filemani_conseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE BUFFER OVERFLOW \n")
    print("            -    EN EL "+str(float((count_filemani_conseq_namecommandexecution_vulnibm_iot*100)/count_filemani_conseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE COMMAND EXECUTION  \n")
    print("            -    EN EL "+str(float((count_filemani_conseq_namespoofing_vulnibm_iot*100)/count_filemani_conseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE SPOOFING  \n")
    print("            -    EN EL "+str(float((count_filemani_conseq_nameclickjacking_vulnibm_iot*100)/count_filemani_conseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE CLICKJACKING  \n")
    print("            -    EN EL "+str(float((count_filemani_conseq_namehijacking_vulnibm_iot*100)/count_filemani_conseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE HIJACKING  \n")
    print("            -    EN EL "+str(float((count_filemani_conseq_namefileinclude_vulnibm_iot*100)/count_filemani_conseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE FILE INCLUDE  \n")
    print("            -    EN EL "+str(float((count_filemani_conseq_namebruteforce_vulnibm_iot*100)/count_filemani_conseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE BRUTE FORCE  \n")
    print("            -    EN EL "+str(float((count_filemani_conseq_namefileupload_vulnibm_iot*100)/count_filemani_conseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE FILE UPLOAD  \n")
    print("            -    EN EL "+str(float((count_filemani_conseq_nameheaderinjection_vulnibm_iot*100)/count_filemani_conseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE HEADER INJECTION \n")
    print("            -    EN EL "+str(float((count_filemani_conseq_nametampering_vulnibm_iot*100)/count_filemani_conseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE TAMPERING  \n")
    print("            -    EN EL "+str(float((count_filemani_conseq_nameanother_vulnibm_iot*100)/count_filemani_conseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE OTRO VALOR DISTINTO A LOS ANTERIORES  \n")
    print("\n")
    
if(count_other_conseq_vulnibm_iot>0):
    print("      -    EN EL "+str(float((count_other_conseq_vulnibm_iot*100)/count_conseq_vulnibm_iot))+" % DE VULNERABILIDADES LA CONSECUENCIA ES OTRA DISTINTA A LAS ANTERIORES. EL NOMBRE VIENE ESPECIFICADO EN EL "+str(float((count_other_conseq_vulnibm_iot_specified*100)/count_other_conseq_vulnibm_iot))+" % DE ELLAS. LOS PORCENTAJES DE VALOR DE NOMBRE SON LOS SIGUIENTES :  \n")
    print("            -    EN EL "+str(float((count_other_conseq_namepathtraversal_vulnibm_iot*100)/count_other_conseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE PATH TRAVERSAL \n")
    print("            -    EN EL "+str(float((count_other_conseq_namedirectorytraversal_vulnibm_iot*100)/count_other_conseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE DIRECTORY TRAVERSAL \n")
    print("            -    EN EL "+str(float((count_other_conseq_nameprivilegeescalation_vulnibm_iot*100)/count_other_conseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE PRIVILEGE ESCALATION \n") 
    print("            -    EN EL "+str(float((count_other_conseq_namecrosssitescripting_vulnibm_iot*100)/count_other_conseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE CROSS-SITE SCRIPTING  \n")
    print("            -    EN EL "+str(float((count_other_conseq_namesecuritybypass_vulnibm_iot*100)/count_other_conseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE SECURITY BYPASS  \n")
    print("            -    EN EL "+str(float((count_other_conseq_namesinformationdisclosure_vulnibm_iot*100)/count_other_conseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE INFORMATION DISCLOSURE \n")
    print("            -    EN EL "+str(float((count_other_conseq_namedenialofservice_vulnibm_iot*100)/count_other_conseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE DENIAL OF SERVICE  \n")
    print("            -    EN EL "+str(float((count_other_conseq_namecodeexecution_vulnibm_iot*100)/count_other_conseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE CODE EXECUTION  \n")
    print("            -    EN EL "+str(float((count_other_conseq_namemaninthemiddle_vulnibm_iot*100)/count_other_conseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE MAN IN THE MIDDLE  \n")
    print("            -    EN EL "+str(float((count_other_conseq_namesqlinjection_vulnibm_iot*100)/count_other_conseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE SQL INJECTION  \n")
    print("            -    EN EL "+str(float((count_other_conseq_namecrosssiterequestforgery_vulnibm_iot*100)/count_other_conseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE MODULE EXECUTION  \n")
    print("            -    EN EL "+str(float((count_other_conseq_namemoduleexecution_vulnibm_iot*100)/count_other_conseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE CROSS SITE REQUEST FORGERY  \n")
    print("            -    EN EL "+str(float((count_other_conseq_namebufferoverflow_vulnibm_iot*100)/count_other_conseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE BUFFER OVERFLOW \n")
    print("            -    EN EL "+str(float((count_other_conseq_namecommandexecution_vulnibm_iot*100)/count_other_conseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE COMMAND EXECUTION  \n")
    print("            -    EN EL "+str(float((count_other_conseq_namespoofing_vulnibm_iot*100)/count_other_conseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE SPOOFING  \n")
    print("            -    EN EL "+str(float((count_other_conseq_nameclickjacking_vulnibm_iot*100)/count_other_conseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE CLICKJACKING  \n")
    print("            -    EN EL "+str(float((count_other_conseq_namehijacking_vulnibm_iot*100)/count_other_conseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE HIJACKING  \n")
    print("            -    EN EL "+str(float((count_other_conseq_namefileinclude_vulnibm_iot*100)/count_other_conseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE FILE INCLUDE  \n")
    print("            -    EN EL "+str(float((count_other_conseq_namebruteforce_vulnibm_iot*100)/count_other_conseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE BRUTE FORCE  \n")
    print("            -    EN EL "+str(float((count_other_conseq_namefileupload_vulnibm_iot*100)/count_other_conseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE FILE UPLOAD  \n")
    print("            -    EN EL "+str(float((count_other_conseq_nameheaderinjection_vulnibm_iot*100)/count_other_conseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE HEADER INJECTION \n")
    print("            -    EN EL "+str(float((count_other_conseq_nametampering_vulnibm_iot*100)/count_other_conseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE TAMPERING  \n")
    print("            -    EN EL "+str(float((count_other_conseq_nameanother_vulnibm_iot*100)/count_other_conseq_vulnibm_iot))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE OTRO VALOR DISTINTO A LOS ANTERIORES  \n")
    print("\n")
    
  
    
    
    
    
    
df_vulnibm_sh = pd.read_excel('vulnerabilidades_ibm_smart_home_2023.xlsx')    
    
    

#Variables donde almacenare el contador total de valores de consecuencias
count_conseq_vulnibm_sh=0

#Variables para almacenador el contador total de valores de nombre dada una consecuencia especifica
count_obtaininfoconseq_namepathtraversal_vulnibm_sh=0
count_obtaininfoconseq_namedirectorytraversal_vulnibm_sh=0
count_obtaininfoconseq_nameprivilegeescalation_vulnibm_sh=0
count_obtaininfoconseq_namecrosssitescripting_vulnibm_sh=0
count_obtaininfoconseq_namesecuritybypass_vulnibm_sh=0
count_obtaininfoconseq_namesinformationdisclosure_vulnibm_sh=0
count_obtaininfoconseq_namedenialofservice_vulnibm_sh=0
count_obtaininfoconseq_namecodeexecution_vulnibm_sh=0
count_obtaininfoconseq_namemaninthemiddle_vulnibm_sh=0
count_obtaininfoconseq_namesqlinjection_vulnibm_sh=0
count_obtaininfoconseq_namecrosssiterequestforgery_vulnibm_sh=0
count_obtaininfoconseq_namemoduleexecution_vulnibm_sh=0
count_obtaininfoconseq_namebufferoverflow_vulnibm_sh=0
count_obtaininfoconseq_namecommandexecution_vulnibm_sh=0
count_obtaininfoconseq_namespoofing_vulnibm_sh=0
count_obtaininfoconseq_nameclickjacking_vulnibm_sh=0
count_obtaininfoconseq_namehijacking_vulnibm_sh=0
count_obtaininfoconseq_namefileinclude_vulnibm_sh=0
count_obtaininfoconseq_namebruteforce_vulnibm_sh=0
count_obtaininfoconseq_namefileupload_vulnibm_sh=0
count_obtaininfoconseq_nameheaderinjection_vulnibm_sh=0
count_obtaininfoconseq_nametampering_vulnibm_sh=0
count_obtaininfoconseq_nameanother_vulnibm_sh=0
#Variable donde almacenamos el contador total de valores de nombre para una consecuencia especifica
count_obtaininfoconseq_vulnibm_sh=0
#Variable donde almacenamos el contador total de valores especificados de nombre para una consecuencia especifica
count_obtaininfoconseq_vulnibm_sh_specified=0


count_xss_conseq_namepathtraversal_vulnibm_sh=0
count_xss_conseq_namedirectorytraversal_vulnibm_sh=0
count_xss_conseq_nameprivilegeescalation_vulnibm_sh=0
count_xss_conseq_namecrosssitescripting_vulnibm_sh=0
count_xss_conseq_namesecuritybypass_vulnibm_sh=0
count_xss_conseq_namesinformationdisclosure_vulnibm_sh=0
count_xss_conseq_namedenialofservice_vulnibm_sh=0
count_xss_conseq_namecodeexecution_vulnibm_sh=0
count_xss_conseq_namemaninthemiddle_vulnibm_sh=0
count_xss_conseq_namesqlinjection_vulnibm_sh=0
count_xss_conseq_namecrosssiterequestforgery_vulnibm_sh=0
count_xss_conseq_namemoduleexecution_vulnibm_sh=0
count_xss_conseq_namebufferoverflow_vulnibm_sh=0
count_xss_conseq_namecommandexecution_vulnibm_sh=0
count_xss_conseq_namespoofing_vulnibm_sh=0
count_xss_conseq_nameclickjacking_vulnibm_sh=0
count_xss_conseq_namehijacking_vulnibm_sh=0
count_xss_conseq_namefileinclude_vulnibm_sh=0
count_xss_conseq_namebruteforce_vulnibm_sh=0
count_xss_conseq_namefileupload_vulnibm_sh=0
count_xss_conseq_nameheaderinjection_vulnibm_sh=0
count_xss_conseq_nametampering_vulnibm_sh=0
count_xss_conseq_nameanother_vulnibm_sh=0
count_xss_conseq_vulnibm_sh=0
count_xss_conseq_vulnibm_sh_specified=0

count_gainacc_conseq_namepathtraversal_vulnibm_sh=0
count_gainacc_conseq_namedirectorytraversal_vulnibm_sh=0
count_gainacc_conseq_nameprivilegeescalation_vulnibm_sh=0
count_gainacc_conseq_namecrosssitescripting_vulnibm_sh=0
count_gainacc_conseq_namesecuritybypass_vulnibm_sh=0
count_gainacc_conseq_namesinformationdisclosure_vulnibm_sh=0
count_gainacc_conseq_namedenialofservice_vulnibm_sh=0
count_gainacc_conseq_namecodeexecution_vulnibm_sh=0
count_gainacc_conseq_namemaninthemiddle_vulnibm_sh=0
count_gainacc_conseq_namesqlinjection_vulnibm_sh=0
count_gainacc_conseq_namecrosssiterequestforgery_vulnibm_sh=0
count_gainacc_conseq_namemoduleexecution_vulnibm_sh=0
count_gainacc_conseq_namebufferoverflow_vulnibm_sh=0
count_gainacc_conseq_namecommandexecution_vulnibm_sh=0
count_gainacc_conseq_namespoofing_vulnibm_sh=0
count_gainacc_conseq_nameclickjacking_vulnibm_sh=0
count_gainacc_conseq_namehijacking_vulnibm_sh=0
count_gainacc_conseq_namefileinclude_vulnibm_sh=0
count_gainacc_conseq_namebruteforce_vulnibm_sh=0
count_gainacc_conseq_namefileupload_vulnibm_sh=0
count_gainacc_conseq_nameheaderinjection_vulnibm_sh=0
count_gainacc_conseq_nametampering_vulnibm_sh=0
count_gainacc_conseq_nameanother_vulnibm_sh=0
count_gainacc_conseq_vulnibm_sh=0
count_gainacc_conseq_vulnibm_sh_specified=0

count_gainpriv_conseq_namepathtraversal_vulnibm_sh=0
count_gainpriv_conseq_namedirectorytraversal_vulnibm_sh=0
count_gainpriv_conseq_nameprivilegeescalation_vulnibm_sh=0
count_gainpriv_conseq_namecrosssitescripting_vulnibm_sh=0
count_gainpriv_conseq_namesecuritybypass_vulnibm_sh=0
count_gainpriv_conseq_namesinformationdisclosure_vulnibm_sh=0
count_gainpriv_conseq_namedenialofservice_vulnibm_sh=0
count_gainpriv_conseq_namecodeexecution_vulnibm_sh=0
count_gainpriv_conseq_namemaninthemiddle_vulnibm_sh=0
count_gainpriv_conseq_namesqlinjection_vulnibm_sh=0
count_gainpriv_conseq_namecrosssiterequestforgery_vulnibm_sh=0
count_gainpriv_conseq_namemoduleexecution_vulnibm_sh=0
count_gainpriv_conseq_namebufferoverflow_vulnibm_sh=0
count_gainpriv_conseq_namecommandexecution_vulnibm_sh=0
count_gainpriv_conseq_namespoofing_vulnibm_sh=0
count_gainpriv_conseq_nameclickjacking_vulnibm_sh=0
count_gainpriv_conseq_namehijacking_vulnibm_sh=0
count_gainpriv_conseq_namefileinclude_vulnibm_sh=0
count_gainpriv_conseq_namebruteforce_vulnibm_sh=0
count_gainpriv_conseq_namefileupload_vulnibm_sh=0
count_gainpriv_conseq_nameheaderinjection_vulnibm_sh=0
count_gainpriv_conseq_nametampering_vulnibm_sh=0
count_gainpriv_conseq_nameanother_vulnibm_sh=0
count_gainpriv_conseq_vulnibm_sh=0
count_gainpriv_conseq_vulnibm_sh_specified=0

count_denialofserv_conseq_namepathtraversal_vulnibm_sh=0
count_denialofserv_conseq_namedirectorytraversal_vulnibm_sh=0
count_denialofserv_conseq_nameprivilegeescalation_vulnibm_sh=0
count_denialofserv_conseq_namecrosssitescripting_vulnibm_sh=0
count_denialofserv_conseq_namesecuritybypass_vulnibm_sh=0
count_denialofserv_conseq_namesinformationdisclosure_vulnibm_sh=0
count_denialofserv_conseq_namedenialofservice_vulnibm_sh=0
count_denialofserv_conseq_namecodeexecution_vulnibm_sh=0
count_denialofserv_conseq_namemaninthemiddle_vulnibm_sh=0
count_denialofserv_conseq_namesqlinjection_vulnibm_sh=0
count_denialofserv_conseq_namecrosssiterequestforgery_vulnibm_sh=0
count_denialofserv_conseq_namemoduleexecution_vulnibm_sh=0
count_denialofserv_conseq_namebufferoverflow_vulnibm_sh=0
count_denialofserv_conseq_namecommandexecution_vulnibm_sh=0
count_denialofserv_conseq_namespoofing_vulnibm_sh=0
count_denialofserv_conseq_nameclickjacking_vulnibm_sh=0
count_denialofserv_conseq_namehijacking_vulnibm_sh=0
count_denialofserv_conseq_namefileinclude_vulnibm_sh=0
count_denialofserv_conseq_namebruteforce_vulnibm_sh=0
count_denialofserv_conseq_namefileupload_vulnibm_sh=0
count_denialofserv_conseq_nameheaderinjection_vulnibm_sh=0
count_denialofserv_conseq_nametampering_vulnibm_sh=0
count_denialofserv_conseq_nameanother_vulnibm_sh=0
count_denialofserv_conseq_vulnibm_sh=0
count_denialofserv_conseq_vulnibm_sh_specified=0

count_bypassec_conseq_namepathtraversal_vulnibm_sh=0
count_bypassec_conseq_namedirectorytraversal_vulnibm_sh=0
count_bypassec_conseq_nameprivilegeescalation_vulnibm_sh=0
count_bypassec_conseq_namecrosssitescripting_vulnibm_sh=0
count_bypassec_conseq_namesecuritybypass_vulnibm_sh=0
count_bypassec_conseq_namesinformationdisclosure_vulnibm_sh=0
count_bypassec_conseq_namedenialofservice_vulnibm_sh=0
count_bypassec_conseq_namecodeexecution_vulnibm_sh=0
count_bypassec_conseq_namemaninthemiddle_vulnibm_sh=0
count_bypassec_conseq_namesqlinjection_vulnibm_sh=0
count_bypassec_conseq_namecrosssiterequestforgery_vulnibm_sh=0
count_bypassec_conseq_namemoduleexecution_vulnibm_sh=0
count_bypassec_conseq_namebufferoverflow_vulnibm_sh=0
count_bypassec_conseq_namecommandexecution_vulnibm_sh=0
count_bypassec_conseq_namespoofing_vulnibm_sh=0
count_bypassec_conseq_nameclickjacking_vulnibm_sh=0
count_bypassec_conseq_namehijacking_vulnibm_sh=0
count_bypassec_conseq_namefileinclude_vulnibm_sh=0
count_bypassec_conseq_namebruteforce_vulnibm_sh=0
count_bypassec_conseq_namefileupload_vulnibm_sh=0
count_bypassec_conseq_nameheaderinjection_vulnibm_sh=0
count_bypassec_conseq_nametampering_vulnibm_sh=0
count_bypassec_conseq_nameanother_vulnibm_sh=0
count_bypassec_conseq_vulnibm_sh=0
count_bypassec_conseq_vulnibm_sh_specified=0

count_filemani_conseq_namepathtraversal_vulnibm_sh=0
count_filemani_conseq_namedirectorytraversal_vulnibm_sh=0
count_filemani_conseq_nameprivilegeescalation_vulnibm_sh=0
count_filemani_conseq_namecrosssitescripting_vulnibm_sh=0
count_filemani_conseq_namesecuritybypass_vulnibm_sh=0
count_filemani_conseq_namesinformationdisclosure_vulnibm_sh=0
count_filemani_conseq_namedenialofservice_vulnibm_sh=0
count_filemani_conseq_namecodeexecution_vulnibm_sh=0
count_filemani_conseq_namemaninthemiddle_vulnibm_sh=0
count_filemani_conseq_namesqlinjection_vulnibm_sh=0
count_filemani_conseq_namecrosssiterequestforgery_vulnibm_sh=0
count_filemani_conseq_namemoduleexecution_vulnibm_sh=0
count_filemani_conseq_namebufferoverflow_vulnibm_sh=0
count_filemani_conseq_namecommandexecution_vulnibm_sh=0
count_filemani_conseq_namespoofing_vulnibm_sh=0
count_filemani_conseq_nameclickjacking_vulnibm_sh=0
count_filemani_conseq_namehijacking_vulnibm_sh=0
count_filemani_conseq_namefileinclude_vulnibm_sh=0
count_filemani_conseq_namebruteforce_vulnibm_sh=0
count_filemani_conseq_namefileupload_vulnibm_sh=0
count_filemani_conseq_nameheaderinjection_vulnibm_sh=0
count_filemani_conseq_nametampering_vulnibm_sh=0
count_filemani_conseq_nameanother_vulnibm_sh=0
count_filemani_conseq_vulnibm_sh=0
count_filemani_conseq_vulnibm_sh_specified=0


count_other_conseq_namepathtraversal_vulnibm_sh=0
count_other_conseq_namedirectorytraversal_vulnibm_sh=0
count_other_conseq_nameprivilegeescalation_vulnibm_sh=0
count_other_conseq_namecrosssitescripting_vulnibm_sh=0
count_other_conseq_namesecuritybypass_vulnibm_sh=0
count_other_conseq_namesinformationdisclosure_vulnibm_sh=0
count_other_conseq_namedenialofservice_vulnibm_sh=0
count_other_conseq_namecodeexecution_vulnibm_sh=0
count_other_conseq_namemaninthemiddle_vulnibm_sh=0
count_other_conseq_namesqlinjection_vulnibm_sh=0
count_other_conseq_namecrosssiterequestforgery_vulnibm_sh=0
count_other_conseq_namemoduleexecution_vulnibm_sh=0
count_other_conseq_namebufferoverflow_vulnibm_sh=0
count_other_conseq_namecommandexecution_vulnibm_sh=0
count_other_conseq_namespoofing_vulnibm_sh=0
count_other_conseq_nameclickjacking_vulnibm_sh=0
count_other_conseq_namehijacking_vulnibm_sh=0
count_other_conseq_namefileinclude_vulnibm_sh=0
count_other_conseq_namebruteforce_vulnibm_sh=0
count_other_conseq_namefileupload_vulnibm_sh=0
count_other_conseq_nameheaderinjection_vulnibm_sh=0
count_other_conseq_nametampering_vulnibm_sh=0
count_other_conseq_nameanother_vulnibm_sh=0
count_other_conseq_vulnibm_sh=0
count_other_conseq_vulnibm_sh_specified=0

#Recorro los valores de CONSECUENCIAS y aumento los contadores segun su valor

for r in range(0,len(df_vulnibm_sh["x_xfe_consequences"])): 
    #Obtengo el valor de la consecuencia
    aux_str=df_vulnibm_sh["x_xfe_consequences"][r].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
    if(aux_str!='NONE' or aux_str!='None'):
        count_conseq_vulnibm_sh+=1
        #Compruebo el valor de la consecuencia
        if(('ObtainInformation' in aux_str) or ('Obtain Information' in aux_str)):
            count_obtaininfoconseq_vulnibm_sh+=1
            #Obtengo el valor de nombre para la fila actual
            auxx_str=df_vulnibm_sh["name"][r].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
            if(auxx_str!='NONE'):
                count_obtaininfoconseq_vulnibm_sh_specified+=1
                if('pathtraversal' in auxx_str):
                    count_obtaininfoconseq_namepathtraversal_vulnibm_sh+=1
                elif('directorytraversal' in auxx_str):
                    count_obtaininfoconseq_namedirectorytraversal_vulnibm_sh+=1
                elif('privilegeescalation' in auxx_str):
                    count_obtaininfoconseq_nameprivilegeescalation_vulnibm_sh+=1
                elif('cross-sitescripting' in auxx_str):
                    count_obtaininfoconseq_namecrosssitescripting_vulnibm_sh+=1                            
                elif('securitybypass' in auxx_str):
                    count_obtaininfoconseq_namesecuritybypass_vulnibm_sh+=1                           
                elif('information_disclosure' in auxx_str or 'informationdisclosure' in auxx_str):
                    count_obtaininfoconseq_namesinformationdisclosure_vulnibm_sh+=1                           
                elif('denialofservice' in auxx_str):
                    count_obtaininfoconseq_namedenialofservice_vulnibm_sh+=1                           
                elif('codeexecution' in auxx_str):
                    count_obtaininfoconseq_namecodeexecution_vulnibm_sh+=1                           
                elif('maninthemiddle' in auxx_str):
                    count_obtaininfoconseq_namemaninthemiddle_vulnibm_sh+=1                           
                elif('SQLinjection' in auxx_str):
                    count_obtaininfoconseq_namesqlinjection_vulnibm_sh+=1                           
                elif('cross-siterequestforgery' in auxx_str):
                    count_obtaininfoconseq_namecrosssiterequestforgery_vulnibm_sh+=1                           
                elif('moduleexecution' in auxx_str):
                    count_obtaininfoconseq_namemoduleexecution_vulnibm_sh+=1                           
                elif('bufferoverflow' in auxx_str):
                    count_obtaininfoconseq_namebufferoverflow_vulnibm_sh+=1                           
                elif('commandexecution' in auxx_str):
                    count_obtaininfoconseq_namecommandexecution_vulnibm_sh+=1                           
                elif('spoofing' in auxx_str):
                    count_obtaininfoconseq_namespoofing_vulnibm_sh+=1                           
                elif('clickjacking' in auxx_str):
                    count_obtaininfoconseq_nameclickjacking_vulnibm_sh+=1
                elif('hijacking' in auxx_str):
                    count_obtaininfoconseq_namehijacking_vulnibm_sh+=1
                elif('fileinclude' in auxx_str):
                    count_obtaininfoconseq_namefileinclude_vulnibm_sh+=1
                elif('bruteforce' in auxx_str):
                    count_obtaininfoconseq_namebruteforce_vulnibm_sh+=1
                elif('fileupload' in auxx_str):
                    count_obtaininfoconseq_namefileupload_vulnibm_sh+=1
                elif('headerinjection' in auxx_str):
                    count_obtaininfoconseq_nameheaderinjection_vulnibm_sh+=1
                elif('Tampering' in auxx_str):
                    count_obtaininfoconseq_nametampering_vulnibm_sh+=1
                else:
                    count_obtaininfoconseq_nameanother_vulnibm_sh+=1
                
        elif('Scripting' in aux_str):
            count_xss_conseq_vulnibm_sh+=1
            auxx_str=df_vulnibm_sh["name"][r].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
            if(auxx_str!='NONE'):
                count_xss_conseq_vulnibm_sh_specified+=1
                if('pathtraversal' in auxx_str):
                    count_xss_conseq_namepathtraversal_vulnibm_sh+=1
                elif('directorytraversal' in auxx_str):
                    count_xss_conseq_namedirectorytraversal_vulnibm_sh+=1
                elif('privilegeescalation' in auxx_str):
                    count_xss_conseq_nameprivilegeescalation_vulnibm_sh+=1
                elif('cross-sitescripting' in auxx_str):
                    count_xss_conseq_namecrosssitescripting_vulnibm_sh+=1                            
                elif('securitybypass' in auxx_str):
                    count_xss_conseq_namesecuritybypass_vulnibm_sh+=1                           
                elif('information_disclosure' in auxx_str or 'informationdisclosure' in auxx_str):
                    count_xss_conseq_namesinformationdisclosure_vulnibm_sh+=1                           
                elif('denialofservice' in auxx_str):
                    count_xss_conseq_namedenialofservice_vulnibm_sh+=1                           
                elif('codeexecution' in auxx_str):
                    count_xss_conseq_namecodeexecution_vulnibm_sh+=1                           
                elif('maninthemiddle' in auxx_str):
                    count_xss_conseq_namemaninthemiddle_vulnibm_sh+=1                           
                elif('SQLinjection' in auxx_str):
                    count_xss_conseq_namesqlinjection_vulnibm_sh+=1                           
                elif('cross-siterequestforgery' in auxx_str):
                    count_xss_conseq_namecrosssiterequestforgery_vulnibm_sh+=1                           
                elif('moduleexecution' in auxx_str):
                    count_xss_conseq_namemoduleexecution_vulnibm_sh+=1                           
                elif('bufferoverflow' in auxx_str):
                    count_xss_conseq_namebufferoverflow_vulnibm_sh+=1                           
                elif('commandexecution' in auxx_str):
                    count_xss_conseq_namecommandexecution_vulnibm_sh+=1                           
                elif('spoofing' in auxx_str):
                    count_xss_conseq_namespoofing_vulnibm_sh+=1                           
                elif('clickjacking' in auxx_str):
                    count_xss_conseq_nameclickjacking_vulnibm_sh+=1
                elif('hijacking' in auxx_str):
                    count_xss_conseq_namehijacking_vulnibm_sh+=1
                elif('fileinclude' in auxx_str):
                    count_xss_conseq_namefileinclude_vulnibm_sh+=1
                elif('bruteforce' in auxx_str):
                    count_xss_conseq_namebruteforce_vulnibm_sh+=1
                elif('fileupload' in auxx_str):
                    count_xss_conseq_namefileupload_vulnibm_sh+=1
                elif('headerinjection' in auxx_str):
                    count_xss_conseq_nameheaderinjection_vulnibm_sh+=1
                elif('Tampering' in auxx_str):
                    count_xss_conseq_nametampering_vulnibm_sh+=1
                else:
                    count_xss_conseq_nameanother_vulnibm_sh+=1
                
        elif('Access' in aux_str):
            count_gainacc_conseq_vulnibm_sh+=1
            auxx_str=df_vulnibm_sh["name"][r].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
            if(auxx_str!='NONE'):
                count_gainacc_conseq_vulnibm_sh_specified+=1
                if('pathtraversal' in auxx_str):
                    count_gainacc_conseq_namepathtraversal_vulnibm_sh+=1
                elif('directorytraversal' in auxx_str):
                    count_gainacc_conseq_namedirectorytraversal_vulnibm_sh+=1
                elif('privilegeescalation' in auxx_str):
                    count_gainacc_conseq_nameprivilegeescalation_vulnibm_sh+=1
                elif('cross-sitescripting' in auxx_str):
                    count_gainacc_conseq_namecrosssitescripting_vulnibm_sh+=1                            
                elif('securitybypass' in auxx_str):
                    count_gainacc_conseq_namesecuritybypass_vulnibm_sh+=1                           
                elif('information_disclosure' in auxx_str or 'informationdisclosure' in auxx_str):
                    count_gainacc_conseq_namesinformationdisclosure_vulnibm_sh+=1                           
                elif('denialofservice' in auxx_str):
                    count_gainacc_conseq_namedenialofservice_vulnibm_sh+=1                           
                elif('codeexecution' in auxx_str):
                    count_gainacc_conseq_namecodeexecution_vulnibm_sh+=1                           
                elif('maninthemiddle' in auxx_str):
                    count_gainacc_conseq_namemaninthemiddle_vulnibm_sh+=1                           
                elif('SQLinjection' in auxx_str):
                    count_gainacc_conseq_namesqlinjection_vulnibm_sh+=1                           
                elif('cross-siterequestforgery' in auxx_str):
                    count_gainacc_conseq_namecrosssiterequestforgery_vulnibm_sh+=1                           
                elif('moduleexecution' in auxx_str):
                    count_gainacc_conseq_namemoduleexecution_vulnibm_sh+=1                           
                elif('bufferoverflow' in auxx_str):
                    count_gainacc_conseq_namebufferoverflow_vulnibm_sh+=1                           
                elif('commandexecution' in auxx_str):
                    count_gainacc_conseq_namecommandexecution_vulnibm_sh+=1                           
                elif('spoofing' in auxx_str):
                    count_gainacc_conseq_namespoofing_vulnibm_sh+=1                           
                elif('clickjacking' in auxx_str):
                    count_gainacc_conseq_nameclickjacking_vulnibm_sh+=1
                elif('hijacking' in auxx_str):
                    count_gainacc_conseq_namehijacking_vulnibm_sh+=1
                elif('fileinclude' in auxx_str):
                    count_gainacc_conseq_namefileinclude_vulnibm_sh+=1
                elif('bruteforce' in auxx_str):
                    count_gainacc_conseq_namebruteforce_vulnibm_sh+=1
                elif('fileupload' in auxx_str):
                    count_gainacc_conseq_namefileupload_vulnibm_sh+=1
                elif('headerinjection' in auxx_str):
                    count_gainacc_conseq_nameheaderinjection_vulnibm_sh+=1
                elif('Tampering' in auxx_str):
                    count_gainacc_conseq_nametampering_vulnibm_sh+=1
                else:
                    count_gainacc_conseq_nameanother_vulnibm_sh+=1
                
        elif('Privilege' in aux_str):
            count_gainpriv_conseq_vulnibm_sh+=1
            auxx_str=df_vulnibm_sh["name"][r].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
            if(auxx_str!='NONE'):
                count_gainpriv_conseq_vulnibm_sh_specified+=1
                if('pathtraversal' in auxx_str):
                    count_gainpriv_conseq_namepathtraversal_vulnibm_sh+=1
                elif('directorytraversal' in auxx_str):
                    count_gainpriv_conseq_namedirectorytraversal_vulnibm_sh+=1
                elif('privilegeescalation' in auxx_str):
                    count_gainpriv_conseq_nameprivilegeescalation_vulnibm_sh+=1
                elif('cross-sitescripting' in auxx_str):
                    count_gainpriv_conseq_namecrosssitescripting_vulnibm_sh+=1                            
                elif('securitybypass' in auxx_str):
                    count_gainpriv_conseq_namesecuritybypass_vulnibm_sh+=1                           
                elif('information_disclosure' in auxx_str or 'informationdisclosure' in auxx_str):
                    count_gainpriv_conseq_namesinformationdisclosure_vulnibm_sh+=1                           
                elif('denialofservice' in auxx_str):
                    count_gainpriv_conseq_namedenialofservice_vulnibm_sh+=1                           
                elif('codeexecution' in auxx_str):
                    count_gainpriv_conseq_namecodeexecution_vulnibm_sh+=1                           
                elif('maninthemiddle' in auxx_str):
                    count_gainpriv_conseq_namemaninthemiddle_vulnibm_sh+=1                           
                elif('SQLinjection' in auxx_str):
                    count_gainpriv_conseq_namesqlinjection_vulnibm_sh+=1                           
                elif('cross-siterequestforgery' in auxx_str):
                    count_gainpriv_conseq_namecrosssiterequestforgery_vulnibm_sh+=1                           
                elif('moduleexecution' in auxx_str):
                    count_gainpriv_conseq_namemoduleexecution_vulnibm_sh+=1                           
                elif('bufferoverflow' in auxx_str):
                    count_gainpriv_conseq_namebufferoverflow_vulnibm_sh+=1                           
                elif('commandexecution' in auxx_str):
                    count_gainpriv_conseq_namecommandexecution_vulnibm_sh+=1                           
                elif('spoofing' in auxx_str):
                    count_gainpriv_conseq_namespoofing_vulnibm_sh+=1                           
                elif('clickjacking' in auxx_str):
                    count_gainpriv_conseq_nameclickjacking_vulnibm_sh+=1
                elif('hijacking' in auxx_str):
                    count_gainpriv_conseq_namehijacking_vulnibm_sh+=1
                elif('fileinclude' in auxx_str):
                    count_gainpriv_conseq_namefileinclude_vulnibm_sh+=1
                elif('bruteforce' in auxx_str):
                    count_gainpriv_conseq_namebruteforce_vulnibm_sh+=1
                elif('fileupload' in auxx_str):
                    count_gainpriv_conseq_namefileupload_vulnibm_sh+=1
                elif('headerinjection' in auxx_str):
                    count_gainpriv_conseq_nameheaderinjection_vulnibm_sh+=1
                elif('Tampering' in auxx_str):
                    count_gainpriv_conseq_nametampering_vulnibm_sh+=1
                else:
                    count_gainpriv_conseq_nameanother_vulnibm_sh+=1
                
        elif('Denial' in aux_str):
            count_denialofserv_conseq_vulnibm_sh+=1
            auxx_str=df_vulnibm_sh["name"][r].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
            if(auxx_str!='NONE'):
                count_denialofserv_conseq_vulnibm_sh_specified+=1
                if('pathtraversal' in auxx_str):
                    count_denialofserv_conseq_namepathtraversal_vulnibm_sh+=1
                elif('directorytraversal' in auxx_str):
                    count_denialofserv_conseq_namedirectorytraversal_vulnibm_sh+=1
                elif('privilegeescalation' in auxx_str):
                    count_denialofserv_conseq_nameprivilegeescalation_vulnibm_sh+=1
                elif('cross-sitescripting' in auxx_str):
                    count_denialofserv_conseq_namecrosssitescripting_vulnibm_sh+=1                            
                elif('securitybypass' in auxx_str):
                    count_denialofserv_conseq_namesecuritybypass_vulnibm_sh+=1                           
                elif('information_disclosure' in auxx_str or 'informationdisclosure' in auxx_str):
                    count_denialofserv_conseq_namesinformationdisclosure_vulnibm_sh+=1                           
                elif('denialofservice' in auxx_str):
                    count_denialofserv_conseq_namedenialofservice_vulnibm_sh+=1                           
                elif('codeexecution' in auxx_str):
                    count_denialofserv_conseq_namecodeexecution_vulnibm_sh+=1                           
                elif('maninthemiddle' in auxx_str):
                    count_denialofserv_conseq_namemaninthemiddle_vulnibm_sh+=1                           
                elif('SQLinjection' in auxx_str):
                    count_denialofserv_conseq_namesqlinjection_vulnibm_sh+=1                           
                elif('cross-siterequestforgery' in auxx_str):
                    count_denialofserv_conseq_namecrosssiterequestforgery_vulnibm_sh+=1                           
                elif('moduleexecution' in auxx_str):
                    count_denialofserv_conseq_namemoduleexecution_vulnibm_sh+=1                           
                elif('bufferoverflow' in auxx_str):
                    count_denialofserv_conseq_namebufferoverflow_vulnibm_sh+=1                           
                elif('commandexecution' in auxx_str):
                    count_denialofserv_conseq_namecommandexecution_vulnibm_sh+=1                           
                elif('spoofing' in auxx_str):
                    count_denialofserv_conseq_namespoofing_vulnibm_sh+=1                           
                elif('clickjacking' in auxx_str):
                    count_denialofserv_conseq_nameclickjacking_vulnibm_sh+=1
                elif('hijacking' in auxx_str):
                    count_denialofserv_conseq_namehijacking_vulnibm_sh+=1
                elif('fileinclude' in auxx_str):
                    count_denialofserv_conseq_namefileinclude_vulnibm_sh+=1
                elif('bruteforce' in auxx_str):
                    count_denialofserv_conseq_namebruteforce_vulnibm_sh+=1
                elif('fileupload' in auxx_str):
                    count_denialofserv_conseq_namefileupload_vulnibm_sh+=1
                elif('headerinjection' in auxx_str):
                    count_denialofserv_conseq_nameheaderinjection_vulnibm_sh+=1
                elif('Tampering' in auxx_str):
                    count_denialofserv_conseq_nametampering_vulnibm_sh+=1
                else:
                    count_denialofserv_conseq_nameanother_vulnibm_sh+=1
        
        elif('Bypass' in aux_str):
            count_bypassec_conseq_vulnibm_sh+=1
            auxx_str=df_vulnibm_sh["name"][r].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
            if(auxx_str!='NONE'):
                count_bypassec_conseq_vulnibm_sh_specified+=1
                if('pathtraversal' in auxx_str):
                    count_bypassec_conseq_namepathtraversal_vulnibm_sh+=1
                elif('directorytraversal' in auxx_str):
                    count_bypassec_conseq_namedirectorytraversal_vulnibm_sh+=1
                elif('privilegeescalation' in auxx_str):
                    count_bypassec_conseq_nameprivilegeescalation_vulnibm_sh+=1
                elif('cross-sitescripting' in auxx_str):
                    count_bypassec_conseq_namecrosssitescripting_vulnibm_sh+=1                            
                elif('securitybypass' in auxx_str):
                    count_bypassec_conseq_namesecuritybypass_vulnibm_sh+=1                           
                elif('information_disclosure' in auxx_str or 'informationdisclosure' in auxx_str):
                    count_bypassec_conseq_namesinformationdisclosure_vulnibm_sh+=1                           
                elif('denialofservice' in auxx_str):
                    count_bypassec_conseq_namedenialofservice_vulnibm_sh+=1                           
                elif('codeexecution' in auxx_str):
                    count_bypassec_conseq_namecodeexecution_vulnibm_sh+=1                           
                elif('maninthemiddle' in auxx_str):
                    count_bypassec_conseq_namemaninthemiddle_vulnibm_sh+=1                           
                elif('SQLinjection' in auxx_str):
                    count_bypassec_conseq_namesqlinjection_vulnibm_sh+=1                           
                elif('cross-siterequestforgery' in auxx_str):
                    count_bypassec_conseq_namecrosssiterequestforgery_vulnibm_sh+=1                           
                elif('moduleexecution' in auxx_str):
                    count_bypassec_conseq_namemoduleexecution_vulnibm_sh+=1                           
                elif('bufferoverflow' in auxx_str):
                    count_bypassec_conseq_namebufferoverflow_vulnibm_sh+=1                           
                elif('commandexecution' in auxx_str):
                    count_bypassec_conseq_namecommandexecution_vulnibm_sh+=1                           
                elif('spoofing' in auxx_str):
                    count_bypassec_conseq_namespoofing_vulnibm_sh+=1                           
                elif('clickjacking' in auxx_str):
                    count_bypassec_conseq_nameclickjacking_vulnibm_sh+=1
                elif('hijacking' in auxx_str):
                    count_bypassec_conseq_namehijacking_vulnibm_sh+=1
                elif('fileinclude' in auxx_str):
                    count_bypassec_conseq_namefileinclude_vulnibm_sh+=1
                elif('bruteforce' in auxx_str):
                    count_bypassec_conseq_namebruteforce_vulnibm_sh+=1
                elif('fileupload' in auxx_str):
                    count_bypassec_conseq_namefileupload_vulnibm_sh+=1
                elif('headerinjection' in auxx_str):
                    count_bypassec_conseq_nameheaderinjection_vulnibm_sh+=1
                elif('Tampering' in auxx_str):
                    count_bypassec_conseq_nametampering_vulnibm_sh+=1
                else:
                    count_bypassec_conseq_nameanother_vulnibm_sh+=1
                
        elif('Manipulation' in aux_str):
            count_filemani_conseq_vulnibm_sh+=1
            auxx_str=df_vulnibm_sh["name"][r].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
            if(auxx_str!='NONE'):
                count_filemani_conseq_vulnibm_sh_specified+=1
                if('pathtraversal' in auxx_str):
                    count_filemani_conseq_namepathtraversal_vulnibm_sh+=1
                elif('directorytraversal' in auxx_str):
                    count_filemani_conseq_namedirectorytraversal_vulnibm_sh+=1
                elif('privilegeescalation' in auxx_str):
                    count_filemani_conseq_nameprivilegeescalation_vulnibm_sh+=1
                elif('cross-sitescripting' in auxx_str):
                    count_filemani_conseq_namecrosssitescripting_vulnibm_sh+=1                            
                elif('securitybypass' in auxx_str):
                    count_filemani_conseq_namesecuritybypass_vulnibm_sh+=1                           
                elif('information_disclosure' in auxx_str or 'informationdisclosure' in auxx_str):
                    count_filemani_conseq_namesinformationdisclosure_vulnibm_sh+=1                           
                elif('filemaniice' in auxx_str):
                    count_filemani_conseq_namedenialofservice_vulnibm_sh+=1                           
                elif('codeexecution' in auxx_str):
                    count_filemani_conseq_namecodeexecution_vulnibm_sh+=1                           
                elif('maninthemiddle' in auxx_str):
                    count_filemani_conseq_namemaninthemiddle_vulnibm_sh+=1                           
                elif('SQLinjection' in auxx_str):
                    count_filemani_conseq_namesqlinjection_vulnibm_sh+=1                           
                elif('cross-siterequestforgery' in auxx_str):
                    count_filemani_conseq_namecrosssiterequestforgery_vulnibm_sh+=1                           
                elif('moduleexecution' in auxx_str):
                    count_filemani_conseq_namemoduleexecution_vulnibm_sh+=1                           
                elif('bufferoverflow' in auxx_str):
                    count_filemani_conseq_namebufferoverflow_vulnibm_sh+=1                           
                elif('commandexecution' in auxx_str):
                    count_filemani_conseq_namecommandexecution_vulnibm_sh+=1                           
                elif('spoofing' in auxx_str):
                    count_filemani_conseq_namespoofing_vulnibm_sh+=1                           
                elif('clickjacking' in auxx_str):
                    count_filemani_conseq_nameclickjacking_vulnibm_sh+=1
                elif('hijacking' in auxx_str):
                    count_filemani_conseq_namehijacking_vulnibm_sh+=1
                elif('fileinclude' in auxx_str):
                    count_filemani_conseq_namefileinclude_vulnibm_sh+=1
                elif('bruteforce' in auxx_str):
                    count_filemani_conseq_namebruteforce_vulnibm_sh+=1
                elif('fileupload' in auxx_str):
                    count_filemani_conseq_namefileupload_vulnibm_sh+=1
                elif('headerinjection' in auxx_str):
                    count_filemani_conseq_nameheaderinjection_vulnibm_sh+=1
                elif('Tampering' in auxx_str):
                    count_filemani_conseq_nametampering_vulnibm_sh+=1
                else:
                    count_filemani_conseq_nameanother_vulnibm_sh+=1
                
        elif('Other' in aux_str):
            count_other_conseq_vulnibm_sh+=1
            auxx_str=df_vulnibm_sh["name"][r].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
            if(auxx_str!='NONE'):
                count_other_conseq_vulnibm_sh_specified+=1
                if('pathtraversal' in auxx_str):
                    count_other_conseq_namepathtraversal_vulnibm_sh+=1
                elif('directorytraversal' in auxx_str):
                    count_other_conseq_namedirectorytraversal_vulnibm_sh+=1
                elif('privilegeescalation' in auxx_str):
                    count_other_conseq_nameprivilegeescalation_vulnibm_sh+=1
                elif('cross-sitescripting' in auxx_str):
                    count_other_conseq_namecrosssitescripting_vulnibm_sh+=1                            
                elif('securitybypass' in auxx_str):
                    count_other_conseq_namesecuritybypass_vulnibm_sh+=1                           
                elif('information_disclosure' in auxx_str or 'informationdisclosure' in auxx_str):
                    count_other_conseq_namesinformationdisclosure_vulnibm_sh+=1                           
                elif('otherice' in auxx_str):
                    count_other_conseq_namedenialofservice_vulnibm_sh+=1                           
                elif('codeexecution' in auxx_str):
                    count_other_conseq_namecodeexecution_vulnibm_sh+=1                           
                elif('maninthemiddle' in auxx_str):
                    count_other_conseq_namemaninthemiddle_vulnibm_sh+=1                           
                elif('SQLinjection' in auxx_str):
                    count_other_conseq_namesqlinjection_vulnibm_sh+=1                           
                elif('cross-siterequestforgery' in auxx_str):
                    count_other_conseq_namecrosssiterequestforgery_vulnibm_sh+=1                           
                elif('moduleexecution' in auxx_str):
                    count_other_conseq_namemoduleexecution_vulnibm_sh+=1                           
                elif('bufferoverflow' in auxx_str):
                    count_other_conseq_namebufferoverflow_vulnibm_sh+=1                           
                elif('commandexecution' in auxx_str):
                    count_other_conseq_namecommandexecution_vulnibm_sh+=1                           
                elif('spoofing' in auxx_str):
                    count_other_conseq_namespoofing_vulnibm_sh+=1                           
                elif('clickjacking' in auxx_str):
                    count_other_conseq_nameclickjacking_vulnibm_sh+=1
                elif('hijacking' in auxx_str):
                    count_other_conseq_namehijacking_vulnibm_sh+=1
                elif('fileinclude' in auxx_str):
                    count_other_conseq_namefileinclude_vulnibm_sh+=1
                elif('bruteforce' in auxx_str):
                    count_other_conseq_namebruteforce_vulnibm_sh+=1
                elif('fileupload' in auxx_str):
                    count_other_conseq_namefileupload_vulnibm_sh+=1
                elif('headerinjection' in auxx_str):
                    count_other_conseq_nameheaderinjection_vulnibm_sh+=1
                elif('Tampering' in auxx_str):
                    count_other_conseq_nametampering_vulnibm_sh+=1
                else:
                    count_other_conseq_nameanother_vulnibm_sh+=1
        
                
                
                
                
                
                
                
                
                
                
                
print("**********************ESTADÍSTICAS CONSECUENCIAS DE ATAQUE/NOMBRE VULNERABILIDADES IBM PARTE SMART HOME**********************")
print("\n")                            
print("\n")
print(" DE UN TOTAL DE "+str(count_conseq_vulnibm_sh)+" VULNERABILIDADES DONDE LAS CONSECUENCIAS VIENEN ESPECIFICADAS:\n") 
print("\n")
print("   - LAS ESTADISTICAS DE CONSECUENCIAS SON LAS SIGUIENTES:  \n")
print("      -    EN  "+str(count_obtaininfoconseq_vulnibm_sh)+" VULNERABILIDADES LA CONSECUENCIA ES LA OBTENCION DE INFORMACION. EL NOMBRE VIENE ESPECIFICADO EN "+str(count_obtaininfoconseq_vulnibm_sh_specified)+" VULNERABILIDADES. LAS ESTADÍSTICAS DE VALORES DE NOMBRE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_obtaininfoconseq_namepathtraversal_vulnibm_sh)+" VULNERABILIDADES EL NOMBRE INCLUYE PATH TRAVERSAL \n")
print("            -    EN  "+str(count_obtaininfoconseq_namedirectorytraversal_vulnibm_sh)+" VULNERABILIDADES EL NOMBRE INCLUYE DIRECTORY TRAVERSAL \n")
print("            -    EN  "+str(count_obtaininfoconseq_nameprivilegeescalation_vulnibm_sh)+" VULNERABILIDADES EL NOMBRE INCLUYE PRIVILEGE ESCALATION \n")
print("            -    EN  "+str(count_obtaininfoconseq_namecrosssitescripting_vulnibm_sh)+" VULNERABILIDADES EL NOMBRE INCLUYE CROSS-SITE SCRIPTING \n")
print("            -    EN  "+str(count_obtaininfoconseq_namesecuritybypass_vulnibm_sh)+" VULNERABILIDADES EL NOMBRE INCLUYE SECURITY BYPASS \n")
print("            -    EN  "+str(count_obtaininfoconseq_namesinformationdisclosure_vulnibm_sh)+" VULNERABILIDADES EL NOMBRE INCLUYE INFORMATION DISCLOSURE \n")
print("            -    EN  "+str(count_obtaininfoconseq_namedenialofservice_vulnibm_sh)+" VULNERABILIDADES EL NOMBRE INCLUYE DENIAL OF SERVICE \n")
print("            -    EN  "+str(count_obtaininfoconseq_namecodeexecution_vulnibm_sh)+" VULNERABILIDADES EL NOMBRE INCLUYE CODE EXECUTION \n")
print("            -    EN  "+str(count_obtaininfoconseq_namemaninthemiddle_vulnibm_sh)+" VULNERABILIDADES EL NOMBRE INCLUYE MAN IN THE MIDDLE \n")
print("            -    EN  "+str(count_obtaininfoconseq_namesqlinjection_vulnibm_sh)+" VULNERABILIDADES EL NOMBRE INCLUYE SQL INJECTION \n")
print("            -    EN  "+str(count_obtaininfoconseq_namemoduleexecution_vulnibm_sh)+" VULNERABILIDADES EL NOMBRE INCLUYE MODULE EXECUTION \n")
print("            -    EN  "+str(count_obtaininfoconseq_namecrosssiterequestforgery_vulnibm_sh)+" VULNERABILIDADES EL NOMBRE INCLUYE CROSS SITE REQUEST FORGERY \n")
print("            -    EN  "+str(count_obtaininfoconseq_namebufferoverflow_vulnibm_sh)+" VULNERABILIDADES EL NOMBRE INCLUYE BUFFER OVERFLOW \n")
print("            -    EN  "+str(count_obtaininfoconseq_namecommandexecution_vulnibm_sh)+" VULNERABILIDADES EL NOMBRE INCLUYE COMMAND EXECUTION \n")
print("            -    EN  "+str(count_obtaininfoconseq_namespoofing_vulnibm_sh)+" VULNERABILIDADES EL NOMBRE INCLUYE SPOOFING \n")
print("            -    EN  "+str(count_obtaininfoconseq_nameclickjacking_vulnibm_sh)+" VULNERABILIDADES EL NOMBRE INCLUYE CLICKJACKING \n")
print("            -    EN  "+str(count_obtaininfoconseq_namehijacking_vulnibm_sh)+" VULNERABILIDADES EL NOMBRE INCLUYE HIJACKING \n")
print("            -    EN  "+str(count_obtaininfoconseq_namefileinclude_vulnibm_sh)+" VULNERABILIDADES EL NOMBRE INCLUYE FILE INCLUDE \n")
print("            -    EN  "+str(count_obtaininfoconseq_namebruteforce_vulnibm_sh)+" VULNERABILIDADES EL NOMBRE INCLUYE BRUTE FORCE \n")
print("            -    EN  "+str(count_obtaininfoconseq_namefileupload_vulnibm_sh)+" VULNERABILIDADES EL NOMBRE INCLUYE FILE UPLOAD \n")
print("            -    EN  "+str(count_obtaininfoconseq_nameheaderinjection_vulnibm_sh)+" VULNERABILIDADES EL NOMBRE INCLUYE HEADER INJECTION \n")
print("            -    EN  "+str(count_obtaininfoconseq_nametampering_vulnibm_sh)+" VULNERABILIDADES EL NOMBRE INCLUYE TAMPERING \n")
print("            -    EN  "+str(count_obtaininfoconseq_nameanother_vulnibm_sh)+" VULNERABILIDADES EL NOMBRE INCLUYE OTRO VALOR DISTINTO A LOS ANTERIORES \n")
print("\n")
print("      -    EN  "+str(count_xss_conseq_vulnibm_sh)+" VULNERABILIDADES LA CONSECUENCIA ES CROSS-SITE SCRIPTING. EL NOMBRE VIENE ESPECIFICADO EN "+str(count_xss_conseq_vulnibm_sh_specified)+" VULNERABILIDADES. LAS ESTADÍSTICAS DE VALORES DE NOMBRE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_xss_conseq_namepathtraversal_vulnibm_sh)+" VULNERABILIDADES EL NOMBRE INCLUYE PATH TRAVERSAL \n")
print("            -    EN  "+str(count_xss_conseq_namedirectorytraversal_vulnibm_sh)+" VULNERABILIDADES EL NOMBRE INCLUYE DIRECTORY TRAVERSAL \n")
print("            -    EN  "+str(count_xss_conseq_nameprivilegeescalation_vulnibm_sh)+" VULNERABILIDADES EL NOMBRE INCLUYE PRIVILEGE ESCALATION \n")
print("            -    EN  "+str(count_xss_conseq_namecrosssitescripting_vulnibm_sh)+" VULNERABILIDADES EL NOMBRE INCLUYE CROSS-SITE SCRIPTING \n")
print("            -    EN  "+str(count_xss_conseq_namesecuritybypass_vulnibm_sh)+" VULNERABILIDADES EL NOMBRE INCLUYE SECURITY BYPASS \n")
print("            -    EN  "+str(count_xss_conseq_namesinformationdisclosure_vulnibm_sh)+" VULNERABILIDADES EL NOMBRE INCLUYE INFORMATION DISCLOSURE \n")
print("            -    EN  "+str(count_xss_conseq_namedenialofservice_vulnibm_sh)+" VULNERABILIDADES EL NOMBRE INCLUYE DENIAL OF SERVICE \n")
print("            -    EN  "+str(count_xss_conseq_namecodeexecution_vulnibm_sh)+" VULNERABILIDADES EL NOMBRE INCLUYE CODE EXECUTION \n")
print("            -    EN  "+str(count_xss_conseq_namemaninthemiddle_vulnibm_sh)+" VULNERABILIDADES EL NOMBRE INCLUYE MAN IN THE MIDDLE \n")
print("            -    EN  "+str(count_xss_conseq_namesqlinjection_vulnibm_sh)+" VULNERABILIDADES EL NOMBRE INCLUYE SQL INJECTION \n")
print("            -    EN  "+str(count_xss_conseq_namemoduleexecution_vulnibm_sh)+" VULNERABILIDADES EL NOMBRE INCLUYE MODULE EXECUTION \n")
print("            -    EN  "+str(count_xss_conseq_namecrosssiterequestforgery_vulnibm_sh)+" VULNERABILIDADES EL NOMBRE INCLUYE CROSS SITE REQUEST FORGERY \n")
print("            -    EN  "+str(count_xss_conseq_namebufferoverflow_vulnibm_sh)+" VULNERABILIDADES EL NOMBRE INCLUYE BUFFER OVERFLOW \n")
print("            -    EN  "+str(count_xss_conseq_namecommandexecution_vulnibm_sh)+" VULNERABILIDADES EL NOMBRE INCLUYE COMMAND EXECUTION \n")
print("            -    EN  "+str(count_xss_conseq_namespoofing_vulnibm_sh)+" VULNERABILIDADES EL NOMBRE INCLUYE SPOOFING \n")
print("            -    EN  "+str(count_xss_conseq_nameclickjacking_vulnibm_sh)+" VULNERABILIDADES EL NOMBRE INCLUYE CLICKJACKING \n")
print("            -    EN  "+str(count_xss_conseq_namehijacking_vulnibm_sh)+" VULNERABILIDADES EL NOMBRE INCLUYE HIJACKING \n")
print("            -    EN  "+str(count_xss_conseq_namefileinclude_vulnibm_sh)+" VULNERABILIDADES EL NOMBRE INCLUYE FILE INCLUDE \n")
print("            -    EN  "+str(count_xss_conseq_namebruteforce_vulnibm_sh)+" VULNERABILIDADES EL NOMBRE INCLUYE BRUTE FORCE \n")
print("            -    EN  "+str(count_xss_conseq_namefileupload_vulnibm_sh)+" VULNERABILIDADES EL NOMBRE INCLUYE FILE UPLOAD \n")
print("            -    EN  "+str(count_xss_conseq_nameheaderinjection_vulnibm_sh)+" VULNERABILIDADES EL NOMBRE INCLUYE HEADER INJECTION \n")
print("            -    EN  "+str(count_xss_conseq_nametampering_vulnibm_sh)+" VULNERABILIDADES EL NOMBRE INCLUYE TAMPERING \n")
print("            -    EN  "+str(count_xss_conseq_nameanother_vulnibm_sh)+" VULNERABILIDADES EL NOMBRE INCLUYE OTRO VALOR DISTINTO A LOS ANTERIORES \n")
print("\n")
print("      -    EN  "+str(count_gainacc_conseq_vulnibm_sh)+" VULNERABILIDADES LA CONSECUENCIA ES LA GANANCIA DE ACCESO. EL NOMBRE VIENE ESPECIFICADO EN "+str(count_gainacc_conseq_vulnibm_sh_specified)+" VULNERABILIDADES. LAS ESTADÍSTICAS DE VALORES DE NOMBRE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_gainacc_conseq_namepathtraversal_vulnibm_sh)+" VULNERABILIDADES EL NOMBRE INCLUYE PATH TRAVERSAL \n")
print("            -    EN  "+str(count_gainacc_conseq_namedirectorytraversal_vulnibm_sh)+" VULNERABILIDADES EL NOMBRE INCLUYE DIRECTORY TRAVERSAL \n")
print("            -    EN  "+str(count_gainacc_conseq_nameprivilegeescalation_vulnibm_sh)+" VULNERABILIDADES EL NOMBRE INCLUYE PRIVILEGE ESCALATION \n")
print("            -    EN  "+str(count_gainacc_conseq_namecrosssitescripting_vulnibm_sh)+" VULNERABILIDADES EL NOMBRE INCLUYE CROSS-SITE SCRIPTING \n")
print("            -    EN  "+str(count_gainacc_conseq_namesecuritybypass_vulnibm_sh)+" VULNERABILIDADES EL NOMBRE INCLUYE SECURITY BYPASS \n")
print("            -    EN  "+str(count_gainacc_conseq_namesinformationdisclosure_vulnibm_sh)+" VULNERABILIDADES EL NOMBRE INCLUYE INFORMATION DISCLOSURE \n")
print("            -    EN  "+str(count_gainacc_conseq_namedenialofservice_vulnibm_sh)+" VULNERABILIDADES EL NOMBRE INCLUYE DENIAL OF SERVICE \n")
print("            -    EN  "+str(count_gainacc_conseq_namecodeexecution_vulnibm_sh)+" VULNERABILIDADES EL NOMBRE INCLUYE CODE EXECUTION \n")
print("            -    EN  "+str(count_gainacc_conseq_namemaninthemiddle_vulnibm_sh)+" VULNERABILIDADES EL NOMBRE INCLUYE MAN IN THE MIDDLE \n")
print("            -    EN  "+str(count_gainacc_conseq_namesqlinjection_vulnibm_sh)+" VULNERABILIDADES EL NOMBRE INCLUYE SQL INJECTION \n")
print("            -    EN  "+str(count_gainacc_conseq_namemoduleexecution_vulnibm_sh)+" VULNERABILIDADES EL NOMBRE INCLUYE MODULE EXECUTION \n")
print("            -    EN  "+str(count_gainacc_conseq_namecrosssiterequestforgery_vulnibm_sh)+" VULNERABILIDADES EL NOMBRE INCLUYE CROSS SITE REQUEST FORGERY \n")
print("            -    EN  "+str(count_gainacc_conseq_namebufferoverflow_vulnibm_sh)+" VULNERABILIDADES EL NOMBRE INCLUYE BUFFER OVERFLOW \n")
print("            -    EN  "+str(count_gainacc_conseq_namecommandexecution_vulnibm_sh)+" VULNERABILIDADES EL NOMBRE INCLUYE COMMAND EXECUTION \n")
print("            -    EN  "+str(count_gainacc_conseq_namespoofing_vulnibm_sh)+" VULNERABILIDADES EL NOMBRE INCLUYE SPOOFING \n")
print("            -    EN  "+str(count_gainacc_conseq_nameclickjacking_vulnibm_sh)+" VULNERABILIDADES EL NOMBRE INCLUYE CLICKJACKING \n")
print("            -    EN  "+str(count_gainacc_conseq_namehijacking_vulnibm_sh)+" VULNERABILIDADES EL NOMBRE INCLUYE HIJACKING \n")
print("            -    EN  "+str(count_gainacc_conseq_namefileinclude_vulnibm_sh)+" VULNERABILIDADES EL NOMBRE INCLUYE FILE INCLUDE \n")
print("            -    EN  "+str(count_gainacc_conseq_namebruteforce_vulnibm_sh)+" VULNERABILIDADES EL NOMBRE INCLUYE BRUTE FORCE \n")
print("            -    EN  "+str(count_gainacc_conseq_namefileupload_vulnibm_sh)+" VULNERABILIDADES EL NOMBRE INCLUYE FILE UPLOAD \n")
print("            -    EN  "+str(count_gainacc_conseq_nameheaderinjection_vulnibm_sh)+" VULNERABILIDADES EL NOMBRE INCLUYE HEADER INJECTION \n")
print("            -    EN  "+str(count_gainacc_conseq_nametampering_vulnibm_sh)+" VULNERABILIDADES EL NOMBRE INCLUYE TAMPERING \n")
print("            -    EN  "+str(count_gainacc_conseq_nameanother_vulnibm_sh)+" VULNERABILIDADES EL NOMBRE INCLUYE OTRO VALOR DISTINTO A LOS ANTERIORES \n")
print("\n")
print("      -    EN  "+str(count_gainpriv_conseq_vulnibm_sh)+" VULNERABILIDADES LA CONSECUENCIA ES LA GANANCIA DE PRIVILEGIOS. EL NOMBRE VIENE ESPECIFICADO EN "+str(count_gainpriv_conseq_vulnibm_sh_specified)+" VULNERABILIDADES. LAS ESTADÍSTICAS DE VALORES DE NOMBRE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_gainpriv_conseq_namepathtraversal_vulnibm_sh)+" VULNERABILIDADES EL NOMBRE INCLUYE PATH TRAVERSAL \n")
print("            -    EN  "+str(count_gainpriv_conseq_namedirectorytraversal_vulnibm_sh)+" VULNERABILIDADES EL NOMBRE INCLUYE DIRECTORY TRAVERSAL \n")
print("            -    EN  "+str(count_gainpriv_conseq_nameprivilegeescalation_vulnibm_sh)+" VULNERABILIDADES EL NOMBRE INCLUYE PRIVILEGE ESCALATION \n")
print("            -    EN  "+str(count_gainpriv_conseq_namecrosssitescripting_vulnibm_sh)+" VULNERABILIDADES EL NOMBRE INCLUYE CROSS-SITE SCRIPTING \n")
print("            -    EN  "+str(count_gainpriv_conseq_namesecuritybypass_vulnibm_sh)+" VULNERABILIDADES EL NOMBRE INCLUYE SECURITY BYPASS \n")
print("            -    EN  "+str(count_gainpriv_conseq_namesinformationdisclosure_vulnibm_sh)+" VULNERABILIDADES EL NOMBRE INCLUYE INFORMATION DISCLOSURE \n")
print("            -    EN  "+str(count_gainpriv_conseq_namedenialofservice_vulnibm_sh)+" VULNERABILIDADES EL NOMBRE INCLUYE DENIAL OF SERVICE \n")
print("            -    EN  "+str(count_gainpriv_conseq_namecodeexecution_vulnibm_sh)+" VULNERABILIDADES EL NOMBRE INCLUYE CODE EXECUTION \n")
print("            -    EN  "+str(count_gainpriv_conseq_namemaninthemiddle_vulnibm_sh)+" VULNERABILIDADES EL NOMBRE INCLUYE MAN IN THE MIDDLE \n")
print("            -    EN  "+str(count_gainpriv_conseq_namesqlinjection_vulnibm_sh)+" VULNERABILIDADES EL NOMBRE INCLUYE SQL INJECTION \n")
print("            -    EN  "+str(count_gainpriv_conseq_namemoduleexecution_vulnibm_sh)+" VULNERABILIDADES EL NOMBRE INCLUYE MODULE EXECUTION \n")
print("            -    EN  "+str(count_gainpriv_conseq_namecrosssiterequestforgery_vulnibm_sh)+" VULNERABILIDADES EL NOMBRE INCLUYE CROSS SITE REQUEST FORGERY \n")
print("            -    EN  "+str(count_gainpriv_conseq_namebufferoverflow_vulnibm_sh)+" VULNERABILIDADES EL NOMBRE INCLUYE BUFFER OVERFLOW \n")
print("            -    EN  "+str(count_gainpriv_conseq_namecommandexecution_vulnibm_sh)+" VULNERABILIDADES EL NOMBRE INCLUYE COMMAND EXECUTION \n")
print("            -    EN  "+str(count_gainpriv_conseq_namespoofing_vulnibm_sh)+" VULNERABILIDADES EL NOMBRE INCLUYE SPOOFING \n")
print("            -    EN  "+str(count_gainpriv_conseq_nameclickjacking_vulnibm_sh)+" VULNERABILIDADES EL NOMBRE INCLUYE CLICKJACKING \n")
print("            -    EN  "+str(count_gainpriv_conseq_namehijacking_vulnibm_sh)+" VULNERABILIDADES EL NOMBRE INCLUYE HIJACKING \n")
print("            -    EN  "+str(count_gainpriv_conseq_namefileinclude_vulnibm_sh)+" VULNERABILIDADES EL NOMBRE INCLUYE FILE INCLUDE \n")
print("            -    EN  "+str(count_gainpriv_conseq_namebruteforce_vulnibm_sh)+" VULNERABILIDADES EL NOMBRE INCLUYE BRUTE FORCE \n")
print("            -    EN  "+str(count_gainpriv_conseq_namefileupload_vulnibm_sh)+" VULNERABILIDADES EL NOMBRE INCLUYE FILE UPLOAD \n")
print("            -    EN  "+str(count_gainpriv_conseq_nameheaderinjection_vulnibm_sh)+" VULNERABILIDADES EL NOMBRE INCLUYE HEADER INJECTION \n")
print("            -    EN  "+str(count_gainpriv_conseq_nametampering_vulnibm_sh)+" VULNERABILIDADES EL NOMBRE INCLUYE TAMPERING \n")
print("            -    EN  "+str(count_gainpriv_conseq_nameanother_vulnibm_sh)+" VULNERABILIDADES EL NOMBRE INCLUYE OTRO VALOR DISTINTO A LOS ANTERIORES \n")
print("\n")
print("      -    EN  "+str(count_denialofserv_conseq_vulnibm_sh)+" VULNERABILIDADES LA CONSECUENCIA ES UNA DENEGACION DE SERVICIO. EL NOMBRE VIENE ESPECIFICADO EN "+str(count_denialofserv_conseq_vulnibm_sh_specified)+" VULNERABILIDADES. LAS ESTADÍSTICAS DE VALORES DE NOMBRE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_denialofserv_conseq_namepathtraversal_vulnibm_sh)+" VULNERABILIDADES EL NOMBRE INCLUYE PATH TRAVERSAL \n")
print("            -    EN  "+str(count_denialofserv_conseq_namedirectorytraversal_vulnibm_sh)+" VULNERABILIDADES EL NOMBRE INCLUYE DIRECTORY TRAVERSAL \n")
print("            -    EN  "+str(count_denialofserv_conseq_nameprivilegeescalation_vulnibm_sh)+" VULNERABILIDADES EL NOMBRE INCLUYE PRIVILEGE ESCALATION \n")
print("            -    EN  "+str(count_denialofserv_conseq_namecrosssitescripting_vulnibm_sh)+" VULNERABILIDADES EL NOMBRE INCLUYE CROSS-SITE SCRIPTING \n")
print("            -    EN  "+str(count_denialofserv_conseq_namesecuritybypass_vulnibm_sh)+" VULNERABILIDADES EL NOMBRE INCLUYE SECURITY BYPASS \n")
print("            -    EN  "+str(count_denialofserv_conseq_namesinformationdisclosure_vulnibm_sh)+" VULNERABILIDADES EL NOMBRE INCLUYE INFORMATION DISCLOSURE \n")
print("            -    EN  "+str(count_denialofserv_conseq_namedenialofservice_vulnibm_sh)+" VULNERABILIDADES EL NOMBRE INCLUYE DENIAL OF SERVICE \n")
print("            -    EN  "+str(count_denialofserv_conseq_namecodeexecution_vulnibm_sh)+" VULNERABILIDADES EL NOMBRE INCLUYE CODE EXECUTION \n")
print("            -    EN  "+str(count_denialofserv_conseq_namemaninthemiddle_vulnibm_sh)+" VULNERABILIDADES EL NOMBRE INCLUYE MAN IN THE MIDDLE \n")
print("            -    EN  "+str(count_denialofserv_conseq_namesqlinjection_vulnibm_sh)+" VULNERABILIDADES EL NOMBRE INCLUYE SQL INJECTION \n")
print("            -    EN  "+str(count_denialofserv_conseq_namemoduleexecution_vulnibm_sh)+" VULNERABILIDADES EL NOMBRE INCLUYE MODULE EXECUTION \n")
print("            -    EN  "+str(count_denialofserv_conseq_namecrosssiterequestforgery_vulnibm_sh)+" VULNERABILIDADES EL NOMBRE INCLUYE CROSS SITE REQUEST FORGERY \n")
print("            -    EN  "+str(count_denialofserv_conseq_namebufferoverflow_vulnibm_sh)+" VULNERABILIDADES EL NOMBRE INCLUYE BUFFER OVERFLOW \n")
print("            -    EN  "+str(count_denialofserv_conseq_namecommandexecution_vulnibm_sh)+" VULNERABILIDADES EL NOMBRE INCLUYE COMMAND EXECUTION \n")
print("            -    EN  "+str(count_denialofserv_conseq_namespoofing_vulnibm_sh)+" VULNERABILIDADES EL NOMBRE INCLUYE SPOOFING \n")
print("            -    EN  "+str(count_denialofserv_conseq_nameclickjacking_vulnibm_sh)+" VULNERABILIDADES EL NOMBRE INCLUYE CLICKJACKING \n")
print("            -    EN  "+str(count_denialofserv_conseq_namehijacking_vulnibm_sh)+" VULNERABILIDADES EL NOMBRE INCLUYE HIJACKING \n")
print("            -    EN  "+str(count_denialofserv_conseq_namefileinclude_vulnibm_sh)+" VULNERABILIDADES EL NOMBRE INCLUYE FILE INCLUDE \n")
print("            -    EN  "+str(count_denialofserv_conseq_namebruteforce_vulnibm_sh)+" VULNERABILIDADES EL NOMBRE INCLUYE BRUTE FORCE \n")
print("            -    EN  "+str(count_denialofserv_conseq_namefileupload_vulnibm_sh)+" VULNERABILIDADES EL NOMBRE INCLUYE FILE UPLOAD \n")
print("            -    EN  "+str(count_denialofserv_conseq_nameheaderinjection_vulnibm_sh)+" VULNERABILIDADES EL NOMBRE INCLUYE HEADER INJECTION \n")
print("            -    EN  "+str(count_denialofserv_conseq_nametampering_vulnibm_sh)+" VULNERABILIDADES EL NOMBRE INCLUYE TAMPERING \n")
print("            -    EN  "+str(count_denialofserv_conseq_nameanother_vulnibm_sh)+" VULNERABILIDADES EL NOMBRE INCLUYE OTRO VALOR DISTINTO A LOS ANTERIORES \n")
print("\n")
print("      -    EN  "+str(count_filemani_conseq_vulnibm_sh)+" VULNERABILIDADES LA CONSECUENCIA ES LA MANIPULACION DE FICHEROS. EL NOMBRE VIENE ESPECIFICADO EN "+str(count_filemani_conseq_vulnibm_sh_specified)+" VULNERABILIDADES. LAS ESTADÍSTICAS DE VALORES DE NOMBRE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_filemani_conseq_namepathtraversal_vulnibm_sh)+" VULNERABILIDADES EL NOMBRE INCLUYE PATH TRAVERSAL \n")
print("            -    EN  "+str(count_filemani_conseq_namedirectorytraversal_vulnibm_sh)+" VULNERABILIDADES EL NOMBRE INCLUYE DIRECTORY TRAVERSAL \n")
print("            -    EN  "+str(count_filemani_conseq_nameprivilegeescalation_vulnibm_sh)+" VULNERABILIDADES EL NOMBRE INCLUYE PRIVILEGE ESCALATION \n")
print("            -    EN  "+str(count_filemani_conseq_namecrosssitescripting_vulnibm_sh)+" VULNERABILIDADES EL NOMBRE INCLUYE CROSS-SITE SCRIPTING \n")
print("            -    EN  "+str(count_filemani_conseq_namesecuritybypass_vulnibm_sh)+" VULNERABILIDADES EL NOMBRE INCLUYE SECURITY BYPASS \n")
print("            -    EN  "+str(count_filemani_conseq_namesinformationdisclosure_vulnibm_sh)+" VULNERABILIDADES EL NOMBRE INCLUYE INFORMATION DISCLOSURE \n")
print("            -    EN  "+str(count_filemani_conseq_namedenialofservice_vulnibm_sh)+" VULNERABILIDADES EL NOMBRE INCLUYE DENIAL OF SERVICE \n")
print("            -    EN  "+str(count_filemani_conseq_namecodeexecution_vulnibm_sh)+" VULNERABILIDADES EL NOMBRE INCLUYE CODE EXECUTION \n")
print("            -    EN  "+str(count_filemani_conseq_namemaninthemiddle_vulnibm_sh)+" VULNERABILIDADES EL NOMBRE INCLUYE MAN IN THE MIDDLE \n")
print("            -    EN  "+str(count_filemani_conseq_namesqlinjection_vulnibm_sh)+" VULNERABILIDADES EL NOMBRE INCLUYE SQL INJECTION \n")
print("            -    EN  "+str(count_filemani_conseq_namemoduleexecution_vulnibm_sh)+" VULNERABILIDADES EL NOMBRE INCLUYE MODULE EXECUTION \n")
print("            -    EN  "+str(count_filemani_conseq_namecrosssiterequestforgery_vulnibm_sh)+" VULNERABILIDADES EL NOMBRE INCLUYE CROSS SITE REQUEST FORGERY \n")
print("            -    EN  "+str(count_filemani_conseq_namebufferoverflow_vulnibm_sh)+" VULNERABILIDADES EL NOMBRE INCLUYE BUFFER OVERFLOW \n")
print("            -    EN  "+str(count_filemani_conseq_namecommandexecution_vulnibm_sh)+" VULNERABILIDADES EL NOMBRE INCLUYE COMMAND EXECUTION \n")
print("            -    EN  "+str(count_filemani_conseq_namespoofing_vulnibm_sh)+" VULNERABILIDADES EL NOMBRE INCLUYE SPOOFING \n")
print("            -    EN  "+str(count_filemani_conseq_nameclickjacking_vulnibm_sh)+" VULNERABILIDADES EL NOMBRE INCLUYE CLICKJACKING \n")
print("            -    EN  "+str(count_filemani_conseq_namehijacking_vulnibm_sh)+" VULNERABILIDADES EL NOMBRE INCLUYE HIJACKING \n")
print("            -    EN  "+str(count_filemani_conseq_namefileinclude_vulnibm_sh)+" VULNERABILIDADES EL NOMBRE INCLUYE FILE INCLUDE \n")
print("            -    EN  "+str(count_filemani_conseq_namebruteforce_vulnibm_sh)+" VULNERABILIDADES EL NOMBRE INCLUYE BRUTE FORCE \n")
print("            -    EN  "+str(count_filemani_conseq_namefileupload_vulnibm_sh)+" VULNERABILIDADES EL NOMBRE INCLUYE FILE UPLOAD \n")
print("            -    EN  "+str(count_filemani_conseq_nameheaderinjection_vulnibm_sh)+" VULNERABILIDADES EL NOMBRE INCLUYE HEADER INJECTION \n")
print("            -    EN  "+str(count_filemani_conseq_nametampering_vulnibm_sh)+" VULNERABILIDADES EL NOMBRE INCLUYE TAMPERING \n")
print("            -    EN  "+str(count_filemani_conseq_nameanother_vulnibm_sh)+" VULNERABILIDADES EL NOMBRE INCLUYE OTRO VALOR DISTINTO A LOS ANTERIORES \n")
print("\n")
print("      -    EN  "+str(count_other_conseq_vulnibm_sh)+" VULNERABILIDADES LA CONSECUENCIA ES OTRA DISTINTA A LAS ANTERIORES. EL NOMBRE VIENE ESPECIFICADO EN "+str(count_other_conseq_vulnibm_sh_specified)+" VULNERABILIDADES. LAS ESTADÍSTICAS DE VALORES DE NOMBRE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_other_conseq_namepathtraversal_vulnibm_sh)+" VULNERABILIDADES EL NOMBRE INCLUYE PATH TRAVERSAL \n")
print("            -    EN  "+str(count_other_conseq_namedirectorytraversal_vulnibm_sh)+" VULNERABILIDADES EL NOMBRE INCLUYE DIRECTORY TRAVERSAL \n")
print("            -    EN  "+str(count_other_conseq_nameprivilegeescalation_vulnibm_sh)+" VULNERABILIDADES EL NOMBRE INCLUYE PRIVILEGE ESCALATION \n")
print("            -    EN  "+str(count_other_conseq_namecrosssitescripting_vulnibm_sh)+" VULNERABILIDADES EL NOMBRE INCLUYE CROSS-SITE SCRIPTING \n")
print("            -    EN  "+str(count_other_conseq_namesecuritybypass_vulnibm_sh)+" VULNERABILIDADES EL NOMBRE INCLUYE SECURITY BYPASS \n")
print("            -    EN  "+str(count_other_conseq_namesinformationdisclosure_vulnibm_sh)+" VULNERABILIDADES EL NOMBRE INCLUYE INFORMATION DISCLOSURE \n")
print("            -    EN  "+str(count_other_conseq_namedenialofservice_vulnibm_sh)+" VULNERABILIDADES EL NOMBRE INCLUYE DENIAL OF SERVICE \n")
print("            -    EN  "+str(count_other_conseq_namecodeexecution_vulnibm_sh)+" VULNERABILIDADES EL NOMBRE INCLUYE CODE EXECUTION \n")
print("            -    EN  "+str(count_other_conseq_namemaninthemiddle_vulnibm_sh)+" VULNERABILIDADES EL NOMBRE INCLUYE MAN IN THE MIDDLE \n")
print("            -    EN  "+str(count_other_conseq_namesqlinjection_vulnibm_sh)+" VULNERABILIDADES EL NOMBRE INCLUYE SQL INJECTION \n")
print("            -    EN  "+str(count_other_conseq_namemoduleexecution_vulnibm_sh)+" VULNERABILIDADES EL NOMBRE INCLUYE MODULE EXECUTION \n")
print("            -    EN  "+str(count_other_conseq_namecrosssiterequestforgery_vulnibm_sh)+" VULNERABILIDADES EL NOMBRE INCLUYE CROSS SITE REQUEST FORGERY \n")
print("            -    EN  "+str(count_other_conseq_namebufferoverflow_vulnibm_sh)+" VULNERABILIDADES EL NOMBRE INCLUYE BUFFER OVERFLOW \n")
print("            -    EN  "+str(count_other_conseq_namecommandexecution_vulnibm_sh)+" VULNERABILIDADES EL NOMBRE INCLUYE COMMAND EXECUTION \n")
print("            -    EN  "+str(count_other_conseq_namespoofing_vulnibm_sh)+" VULNERABILIDADES EL NOMBRE INCLUYE SPOOFING \n")
print("            -    EN  "+str(count_other_conseq_nameclickjacking_vulnibm_sh)+" VULNERABILIDADES EL NOMBRE INCLUYE CLICKJACKING \n")
print("            -    EN  "+str(count_other_conseq_namehijacking_vulnibm_sh)+" VULNERABILIDADES EL NOMBRE INCLUYE HIJACKING \n")
print("            -    EN  "+str(count_other_conseq_namefileinclude_vulnibm_sh)+" VULNERABILIDADES EL NOMBRE INCLUYE FILE INCLUDE \n")
print("            -    EN  "+str(count_other_conseq_namebruteforce_vulnibm_sh)+" VULNERABILIDADES EL NOMBRE INCLUYE BRUTE FORCE \n")
print("            -    EN  "+str(count_other_conseq_namefileupload_vulnibm_sh)+" VULNERABILIDADES EL NOMBRE INCLUYE FILE UPLOAD \n")
print("            -    EN  "+str(count_other_conseq_nameheaderinjection_vulnibm_sh)+" VULNERABILIDADES EL NOMBRE INCLUYE HEADER INJECTION \n")
print("            -    EN  "+str(count_other_conseq_nametampering_vulnibm_sh)+" VULNERABILIDADES EL NOMBRE INCLUYE TAMPERING \n")
print("            -    EN  "+str(count_other_conseq_nameanother_vulnibm_sh)+" VULNERABILIDADES EL NOMBRE INCLUYE OTRO VALOR DISTINTO A LOS ANTERIORES \n")
print("\n")






print("**********************PORCENTAJES CONSECUENCIAS DE ATAQUE/NOMBRE VULNERABILIDADES IBM SMART HOME **********************")
print("\n")                            
print("\n")
print(" DE UN TOTAL DE "+str(count_conseq_vulnibm_sh)+" VULNERABILIDADES :\n") 
print("\n")
print("   - LOS PORCENTAJES DE CONSECUENCIAS SON LOS SIGUIENTES:  \n")
if(count_obtaininfoconseq_vulnibm_sh>0):
    print("      -    EN EL "+str(float((count_obtaininfoconseq_vulnibm_sh*100)/count_conseq_vulnibm_sh))+" % DE VULNERABILIDADES LA CONSECUENCIA ES LA OBTENCION DE INFORMACION. EL NOMBRE VIENE ESPECIFICADO EN EL "+str(float((count_obtaininfoconseq_vulnibm_sh_specified*100)/count_obtaininfoconseq_vulnibm_sh))+" % DE ELLAS. LOS PORCENTAJES DE VALOR DE NOMBRE SON LOS SIGUIENTES :  \n")
    print("            -    EN EL "+str(float((count_obtaininfoconseq_namepathtraversal_vulnibm_sh*100)/count_obtaininfoconseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE PATH TRAVERSAL \n")
    print("            -    EN EL "+str(float((count_obtaininfoconseq_namedirectorytraversal_vulnibm_sh*100)/count_obtaininfoconseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE DIRECTORY TRAVERSAL \n")
    print("            -    EN EL "+str(float((count_obtaininfoconseq_nameprivilegeescalation_vulnibm_sh*100)/count_obtaininfoconseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE PRIVILEGE ESCALATION \n") 
    print("            -    EN EL "+str(float((count_obtaininfoconseq_namecrosssitescripting_vulnibm_sh*100)/count_obtaininfoconseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE CROSS-SITE SCRIPTING  \n")
    print("            -    EN EL "+str(float((count_obtaininfoconseq_namesecuritybypass_vulnibm_sh*100)/count_obtaininfoconseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE SECURITY BYPASS  \n")
    print("            -    EN EL "+str(float((count_obtaininfoconseq_namesinformationdisclosure_vulnibm_sh*100)/count_obtaininfoconseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE INFORMATION DISCLOSURE \n")
    print("            -    EN EL "+str(float((count_obtaininfoconseq_namedenialofservice_vulnibm_sh*100)/count_obtaininfoconseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE DENIAL OF SERVICE  \n")
    print("            -    EN EL "+str(float((count_obtaininfoconseq_namecodeexecution_vulnibm_sh*100)/count_obtaininfoconseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE CODE EXECUTION  \n")
    print("            -    EN EL "+str(float((count_obtaininfoconseq_namemaninthemiddle_vulnibm_sh*100)/count_obtaininfoconseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE MAN IN THE MIDDLE  \n")
    print("            -    EN EL "+str(float((count_obtaininfoconseq_namesqlinjection_vulnibm_sh*100)/count_obtaininfoconseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE SQL INJECTION  \n")
    print("            -    EN EL "+str(float((count_obtaininfoconseq_namecrosssiterequestforgery_vulnibm_sh*100)/count_obtaininfoconseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE MODULE EXECUTION  \n")
    print("            -    EN EL "+str(float((count_obtaininfoconseq_namemoduleexecution_vulnibm_sh*100)/count_obtaininfoconseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE CROSS SITE REQUEST FORGERY  \n")
    print("            -    EN EL "+str(float((count_obtaininfoconseq_namebufferoverflow_vulnibm_sh*100)/count_obtaininfoconseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE BUFFER OVERFLOW \n")
    print("            -    EN EL "+str(float((count_obtaininfoconseq_namecommandexecution_vulnibm_sh*100)/count_obtaininfoconseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE COMMAND EXECUTION  \n")
    print("            -    EN EL "+str(float((count_obtaininfoconseq_namespoofing_vulnibm_sh*100)/count_obtaininfoconseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE SPOOFING  \n")
    print("            -    EN EL "+str(float((count_obtaininfoconseq_nameclickjacking_vulnibm_sh*100)/count_obtaininfoconseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE CLICKJACKING  \n")
    print("            -    EN EL "+str(float((count_obtaininfoconseq_namehijacking_vulnibm_sh*100)/count_obtaininfoconseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE HIJACKING  \n")
    print("            -    EN EL "+str(float((count_obtaininfoconseq_namefileinclude_vulnibm_sh*100)/count_obtaininfoconseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE FILE INCLUDE  \n")
    print("            -    EN EL "+str(float((count_obtaininfoconseq_namebruteforce_vulnibm_sh*100)/count_obtaininfoconseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE BRUTE FORCE  \n")
    print("            -    EN EL "+str(float((count_obtaininfoconseq_namefileupload_vulnibm_sh*100)/count_obtaininfoconseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE FILE UPLOAD  \n")
    print("            -    EN EL "+str(float((count_obtaininfoconseq_nameheaderinjection_vulnibm_sh*100)/count_obtaininfoconseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE HEADER INJECTION \n")
    print("            -    EN EL "+str(float((count_obtaininfoconseq_nametampering_vulnibm_sh*100)/count_obtaininfoconseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE TAMPERING  \n")
    print("            -    EN EL "+str(float((count_obtaininfoconseq_nameanother_vulnibm_sh*100)/count_obtaininfoconseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE OTRO VALOR DISTINTO A LOS ANTERIORES  \n")
    print("\n")
if(count_xss_conseq_vulnibm_sh>0):
    print("      -    EN EL "+str(float((count_xss_conseq_vulnibm_sh*100)/count_conseq_vulnibm_sh))+" % DE VULNERABILIDADES LA CONSECUENCIA ES CROSS SITE SCRIPTING. EL NOMBRE VIENE ESPECIFICADO EN EL "+str(float((count_xss_conseq_vulnibm_sh_specified*100)/count_xss_conseq_vulnibm_sh))+" % DE ELLAS. LOS PORCENTAJES DE VALOR DE NOMBRE SON LOS SIGUIENTES :  \n")
    print("            -    EN EL "+str(float((count_xss_conseq_namepathtraversal_vulnibm_sh*100)/count_xss_conseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE PATH TRAVERSAL \n")
    print("            -    EN EL "+str(float((count_xss_conseq_namedirectorytraversal_vulnibm_sh*100)/count_xss_conseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE DIRECTORY TRAVERSAL \n")
    print("            -    EN EL "+str(float((count_xss_conseq_nameprivilegeescalation_vulnibm_sh*100)/count_xss_conseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE PRIVILEGE ESCALATION \n") 
    print("            -    EN EL "+str(float((count_xss_conseq_namecrosssitescripting_vulnibm_sh*100)/count_xss_conseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE CROSS-SITE SCRIPTING  \n")
    print("            -    EN EL "+str(float((count_xss_conseq_namesecuritybypass_vulnibm_sh*100)/count_xss_conseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE SECURITY BYPASS  \n")
    print("            -    EN EL "+str(float((count_xss_conseq_namesinformationdisclosure_vulnibm_sh*100)/count_xss_conseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE INFORMATION DISCLOSURE \n")
    print("            -    EN EL "+str(float((count_xss_conseq_namedenialofservice_vulnibm_sh*100)/count_xss_conseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE DENIAL OF SERVICE  \n")
    print("            -    EN EL "+str(float((count_xss_conseq_namecodeexecution_vulnibm_sh*100)/count_xss_conseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE CODE EXECUTION  \n")
    print("            -    EN EL "+str(float((count_xss_conseq_namemaninthemiddle_vulnibm_sh*100)/count_xss_conseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE MAN IN THE MIDDLE  \n")
    print("            -    EN EL "+str(float((count_xss_conseq_namesqlinjection_vulnibm_sh*100)/count_xss_conseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE SQL INJECTION  \n")
    print("            -    EN EL "+str(float((count_xss_conseq_namecrosssiterequestforgery_vulnibm_sh*100)/count_xss_conseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE MODULE EXECUTION  \n")
    print("            -    EN EL "+str(float((count_xss_conseq_namemoduleexecution_vulnibm_sh*100)/count_xss_conseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE CROSS SITE REQUEST FORGERY  \n")
    print("            -    EN EL "+str(float((count_xss_conseq_namebufferoverflow_vulnibm_sh*100)/count_xss_conseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE BUFFER OVERFLOW \n")
    print("            -    EN EL "+str(float((count_xss_conseq_namecommandexecution_vulnibm_sh*100)/count_xss_conseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE COMMAND EXECUTION  \n")
    print("            -    EN EL "+str(float((count_xss_conseq_namespoofing_vulnibm_sh*100)/count_xss_conseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE SPOOFING  \n")
    print("            -    EN EL "+str(float((count_xss_conseq_nameclickjacking_vulnibm_sh*100)/count_xss_conseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE CLICKJACKING  \n")
    print("            -    EN EL "+str(float((count_xss_conseq_namehijacking_vulnibm_sh*100)/count_xss_conseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE HIJACKING  \n")
    print("            -    EN EL "+str(float((count_xss_conseq_namefileinclude_vulnibm_sh*100)/count_xss_conseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE FILE INCLUDE  \n")
    print("            -    EN EL "+str(float((count_xss_conseq_namebruteforce_vulnibm_sh*100)/count_xss_conseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE BRUTE FORCE  \n")
    print("            -    EN EL "+str(float((count_xss_conseq_namefileupload_vulnibm_sh*100)/count_xss_conseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE FILE UPLOAD  \n")
    print("            -    EN EL "+str(float((count_xss_conseq_nameheaderinjection_vulnibm_sh*100)/count_xss_conseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE HEADER INJECTION \n")
    print("            -    EN EL "+str(float((count_xss_conseq_nametampering_vulnibm_sh*100)/count_xss_conseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE TAMPERING  \n")
    print("            -    EN EL "+str(float((count_xss_conseq_nameanother_vulnibm_sh*100)/count_xss_conseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE OTRO VALOR DISTINTO A LOS ANTERIORES  \n")
    print("\n")
if(count_gainacc_conseq_vulnibm_sh>0):
    print("      -    EN EL "+str(float((count_gainacc_conseq_vulnibm_sh*100)/count_conseq_vulnibm_sh))+" % DE VULNERABILIDADES LA CONSECUENCIA ES LA OBTENCION ACCESO. EL NOMBRE VIENE ESPECIFICADO EN EL "+str(float((count_gainacc_conseq_vulnibm_sh_specified*100)/count_gainacc_conseq_vulnibm_sh))+" % DE ELLAS. LOS PORCENTAJES DE VALOR DE NOMBRE SON LOS SIGUIENTES :  \n")
    print("            -    EN EL "+str(float((count_gainacc_conseq_namepathtraversal_vulnibm_sh*100)/count_gainacc_conseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE PATH TRAVERSAL \n")
    print("            -    EN EL "+str(float((count_gainacc_conseq_namedirectorytraversal_vulnibm_sh*100)/count_gainacc_conseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE DIRECTORY TRAVERSAL \n")
    print("            -    EN EL "+str(float((count_gainacc_conseq_nameprivilegeescalation_vulnibm_sh*100)/count_gainacc_conseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE PRIVILEGE ESCALATION \n") 
    print("            -    EN EL "+str(float((count_gainacc_conseq_namecrosssitescripting_vulnibm_sh*100)/count_gainacc_conseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE CROSS-SITE SCRIPTING  \n")
    print("            -    EN EL "+str(float((count_gainacc_conseq_namesecuritybypass_vulnibm_sh*100)/count_gainacc_conseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE SECURITY BYPASS  \n")
    print("            -    EN EL "+str(float((count_gainacc_conseq_namesinformationdisclosure_vulnibm_sh*100)/count_gainacc_conseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE INFORMATION DISCLOSURE \n")
    print("            -    EN EL "+str(float((count_gainacc_conseq_namedenialofservice_vulnibm_sh*100)/count_gainacc_conseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE DENIAL OF SERVICE  \n")
    print("            -    EN EL "+str(float((count_gainacc_conseq_namecodeexecution_vulnibm_sh*100)/count_gainacc_conseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE CODE EXECUTION  \n")
    print("            -    EN EL "+str(float((count_gainacc_conseq_namemaninthemiddle_vulnibm_sh*100)/count_gainacc_conseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE MAN IN THE MIDDLE  \n")
    print("            -    EN EL "+str(float((count_gainacc_conseq_namesqlinjection_vulnibm_sh*100)/count_gainacc_conseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE SQL INJECTION  \n")
    print("            -    EN EL "+str(float((count_gainacc_conseq_namecrosssiterequestforgery_vulnibm_sh*100)/count_gainacc_conseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE MODULE EXECUTION  \n")
    print("            -    EN EL "+str(float((count_gainacc_conseq_namemoduleexecution_vulnibm_sh*100)/count_gainacc_conseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE CROSS SITE REQUEST FORGERY  \n")
    print("            -    EN EL "+str(float((count_gainacc_conseq_namebufferoverflow_vulnibm_sh*100)/count_gainacc_conseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE BUFFER OVERFLOW \n")
    print("            -    EN EL "+str(float((count_gainacc_conseq_namecommandexecution_vulnibm_sh*100)/count_gainacc_conseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE COMMAND EXECUTION  \n")
    print("            -    EN EL "+str(float((count_gainacc_conseq_namespoofing_vulnibm_sh*100)/count_gainacc_conseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE SPOOFING  \n")
    print("            -    EN EL "+str(float((count_gainacc_conseq_nameclickjacking_vulnibm_sh*100)/count_gainacc_conseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE CLICKJACKING  \n")
    print("            -    EN EL "+str(float((count_gainacc_conseq_namehijacking_vulnibm_sh*100)/count_gainacc_conseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE HIJACKING  \n")
    print("            -    EN EL "+str(float((count_gainacc_conseq_namefileinclude_vulnibm_sh*100)/count_gainacc_conseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE FILE INCLUDE  \n")
    print("            -    EN EL "+str(float((count_gainacc_conseq_namebruteforce_vulnibm_sh*100)/count_gainacc_conseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE BRUTE FORCE  \n")
    print("            -    EN EL "+str(float((count_gainacc_conseq_namefileupload_vulnibm_sh*100)/count_gainacc_conseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE FILE UPLOAD  \n")
    print("            -    EN EL "+str(float((count_gainacc_conseq_nameheaderinjection_vulnibm_sh*100)/count_gainacc_conseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE HEADER INJECTION \n")
    print("            -    EN EL "+str(float((count_gainacc_conseq_nametampering_vulnibm_sh*100)/count_gainacc_conseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE TAMPERING  \n")
    print("            -    EN EL "+str(float((count_gainacc_conseq_nameanother_vulnibm_sh*100)/count_gainacc_conseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE OTRO VALOR DISTINTO A LOS ANTERIORES  \n")
    print("\n")
if(count_gainpriv_conseq_vulnibm_sh>0):
    print("      -    EN EL "+str(float((count_gainpriv_conseq_vulnibm_sh*100)/count_conseq_vulnibm_sh))+" % DE VULNERABILIDADES LA CONSECUENCIA ES LA OBTENCION DE PRIVILEGIOS. EL NOMBRE VIENE ESPECIFICADO EN EL "+str(float((count_gainpriv_conseq_vulnibm_sh_specified*100)/count_gainpriv_conseq_vulnibm_sh))+" % DE ELLAS. LOS PORCENTAJES DE VALOR DE NOMBRE SON LOS SIGUIENTES :  \n")
    print("            -    EN EL "+str(float((count_gainpriv_conseq_namepathtraversal_vulnibm_sh*100)/count_gainpriv_conseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE PATH TRAVERSAL \n")
    print("            -    EN EL "+str(float((count_gainpriv_conseq_namedirectorytraversal_vulnibm_sh*100)/count_gainpriv_conseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE DIRECTORY TRAVERSAL \n")
    print("            -    EN EL "+str(float((count_gainpriv_conseq_nameprivilegeescalation_vulnibm_sh*100)/count_gainpriv_conseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE PRIVILEGE ESCALATION \n") 
    print("            -    EN EL "+str(float((count_gainpriv_conseq_namecrosssitescripting_vulnibm_sh*100)/count_gainpriv_conseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE CROSS-SITE SCRIPTING  \n")
    print("            -    EN EL "+str(float((count_gainpriv_conseq_namesecuritybypass_vulnibm_sh*100)/count_gainpriv_conseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE SECURITY BYPASS  \n")
    print("            -    EN EL "+str(float((count_gainpriv_conseq_namesinformationdisclosure_vulnibm_sh*100)/count_gainpriv_conseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE INFORMATION DISCLOSURE \n")
    print("            -    EN EL "+str(float((count_gainpriv_conseq_namedenialofservice_vulnibm_sh*100)/count_gainpriv_conseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE DENIAL OF SERVICE  \n")
    print("            -    EN EL "+str(float((count_gainpriv_conseq_namecodeexecution_vulnibm_sh*100)/count_gainpriv_conseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE CODE EXECUTION  \n")
    print("            -    EN EL "+str(float((count_gainpriv_conseq_namemaninthemiddle_vulnibm_sh*100)/count_gainpriv_conseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE MAN IN THE MIDDLE  \n")
    print("            -    EN EL "+str(float((count_gainpriv_conseq_namesqlinjection_vulnibm_sh*100)/count_gainpriv_conseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE SQL INJECTION  \n")
    print("            -    EN EL "+str(float((count_gainpriv_conseq_namecrosssiterequestforgery_vulnibm_sh*100)/count_gainpriv_conseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE MODULE EXECUTION  \n")
    print("            -    EN EL "+str(float((count_gainpriv_conseq_namemoduleexecution_vulnibm_sh*100)/count_gainpriv_conseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE CROSS SITE REQUEST FORGERY  \n")
    print("            -    EN EL "+str(float((count_gainpriv_conseq_namebufferoverflow_vulnibm_sh*100)/count_gainpriv_conseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE BUFFER OVERFLOW \n")
    print("            -    EN EL "+str(float((count_gainpriv_conseq_namecommandexecution_vulnibm_sh*100)/count_gainpriv_conseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE COMMAND EXECUTION  \n")
    print("            -    EN EL "+str(float((count_gainpriv_conseq_namespoofing_vulnibm_sh*100)/count_gainpriv_conseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE SPOOFING  \n")
    print("            -    EN EL "+str(float((count_gainpriv_conseq_nameclickjacking_vulnibm_sh*100)/count_gainpriv_conseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE CLICKJACKING  \n")
    print("            -    EN EL "+str(float((count_gainpriv_conseq_namehijacking_vulnibm_sh*100)/count_gainpriv_conseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE HIJACKING  \n")
    print("            -    EN EL "+str(float((count_gainpriv_conseq_namefileinclude_vulnibm_sh*100)/count_gainpriv_conseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE FILE INCLUDE  \n")
    print("            -    EN EL "+str(float((count_gainpriv_conseq_namebruteforce_vulnibm_sh*100)/count_gainpriv_conseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE BRUTE FORCE  \n")
    print("            -    EN EL "+str(float((count_gainpriv_conseq_namefileupload_vulnibm_sh*100)/count_gainpriv_conseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE FILE UPLOAD  \n")
    print("            -    EN EL "+str(float((count_gainpriv_conseq_nameheaderinjection_vulnibm_sh*100)/count_gainpriv_conseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE HEADER INJECTION \n")
    print("            -    EN EL "+str(float((count_gainpriv_conseq_nametampering_vulnibm_sh*100)/count_gainpriv_conseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE TAMPERING  \n")
    print("            -    EN EL "+str(float((count_gainpriv_conseq_nameanother_vulnibm_sh*100)/count_gainpriv_conseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE OTRO VALOR DISTINTO A LOS ANTERIORES  \n")
    print("\n")

if(count_denialofserv_conseq_vulnibm_sh>0):
    print("      -    EN EL "+str(float((count_denialofserv_conseq_vulnibm_sh*100)/count_conseq_vulnibm_sh))+" % DE VULNERABILIDADES LA CONSECUENCIA ES UNA DENEGACION DE SERVICIO. EL NOMBRE VIENE ESPECIFICADO EN EL "+str(float((count_denialofserv_conseq_vulnibm_sh_specified*100)/count_denialofserv_conseq_vulnibm_sh))+" % DE ELLAS. LOS PORCENTAJES DE VALOR DE NOMBRE SON LOS SIGUIENTES :  \n")
    print("            -    EN EL "+str(float((count_denialofserv_conseq_namepathtraversal_vulnibm_sh*100)/count_denialofserv_conseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE PATH TRAVERSAL \n")
    print("            -    EN EL "+str(float((count_denialofserv_conseq_namedirectorytraversal_vulnibm_sh*100)/count_denialofserv_conseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE DIRECTORY TRAVERSAL \n")
    print("            -    EN EL "+str(float((count_denialofserv_conseq_nameprivilegeescalation_vulnibm_sh*100)/count_denialofserv_conseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE PRIVILEGE ESCALATION \n") 
    print("            -    EN EL "+str(float((count_denialofserv_conseq_namecrosssitescripting_vulnibm_sh*100)/count_denialofserv_conseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE CROSS-SITE SCRIPTING  \n")
    print("            -    EN EL "+str(float((count_denialofserv_conseq_namesecuritybypass_vulnibm_sh*100)/count_denialofserv_conseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE SECURITY BYPASS  \n")
    print("            -    EN EL "+str(float((count_denialofserv_conseq_namesinformationdisclosure_vulnibm_sh*100)/count_denialofserv_conseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE INFORMATION DISCLOSURE \n")
    print("            -    EN EL "+str(float((count_denialofserv_conseq_namedenialofservice_vulnibm_sh*100)/count_denialofserv_conseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE DENIAL OF SERVICE  \n")
    print("            -    EN EL "+str(float((count_denialofserv_conseq_namecodeexecution_vulnibm_sh*100)/count_denialofserv_conseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE CODE EXECUTION  \n")
    print("            -    EN EL "+str(float((count_denialofserv_conseq_namemaninthemiddle_vulnibm_sh*100)/count_denialofserv_conseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE MAN IN THE MIDDLE  \n")
    print("            -    EN EL "+str(float((count_denialofserv_conseq_namesqlinjection_vulnibm_sh*100)/count_denialofserv_conseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE SQL INJECTION  \n")
    print("            -    EN EL "+str(float((count_denialofserv_conseq_namecrosssiterequestforgery_vulnibm_sh*100)/count_denialofserv_conseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE MODULE EXECUTION  \n")
    print("            -    EN EL "+str(float((count_denialofserv_conseq_namemoduleexecution_vulnibm_sh*100)/count_denialofserv_conseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE CROSS SITE REQUEST FORGERY  \n")
    print("            -    EN EL "+str(float((count_denialofserv_conseq_namebufferoverflow_vulnibm_sh*100)/count_denialofserv_conseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE BUFFER OVERFLOW \n")
    print("            -    EN EL "+str(float((count_denialofserv_conseq_namecommandexecution_vulnibm_sh*100)/count_denialofserv_conseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE COMMAND EXECUTION  \n")
    print("            -    EN EL "+str(float((count_denialofserv_conseq_namespoofing_vulnibm_sh*100)/count_denialofserv_conseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE SPOOFING  \n")
    print("            -    EN EL "+str(float((count_denialofserv_conseq_nameclickjacking_vulnibm_sh*100)/count_denialofserv_conseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE CLICKJACKING  \n")
    print("            -    EN EL "+str(float((count_denialofserv_conseq_namehijacking_vulnibm_sh*100)/count_denialofserv_conseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE HIJACKING  \n")
    print("            -    EN EL "+str(float((count_denialofserv_conseq_namefileinclude_vulnibm_sh*100)/count_denialofserv_conseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE FILE INCLUDE  \n")
    print("            -    EN EL "+str(float((count_denialofserv_conseq_namebruteforce_vulnibm_sh*100)/count_denialofserv_conseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE BRUTE FORCE  \n")
    print("            -    EN EL "+str(float((count_denialofserv_conseq_namefileupload_vulnibm_sh*100)/count_denialofserv_conseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE FILE UPLOAD  \n")
    print("            -    EN EL "+str(float((count_denialofserv_conseq_nameheaderinjection_vulnibm_sh*100)/count_denialofserv_conseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE HEADER INJECTION \n")
    print("            -    EN EL "+str(float((count_denialofserv_conseq_nametampering_vulnibm_sh*100)/count_denialofserv_conseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE TAMPERING  \n")
    print("            -    EN EL "+str(float((count_denialofserv_conseq_nameanother_vulnibm_sh*100)/count_denialofserv_conseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE OTRO VALOR DISTINTO A LOS ANTERIORES  \n")
    print("\n")
    
if(count_bypassec_conseq_vulnibm_sh>0):
    print("      -    EN EL "+str(float((count_bypassec_conseq_vulnibm_sh*100)/count_conseq_vulnibm_sh))+" % DE VULNERABILIDADES LA CONSECUENCIA ES SOBREPASAR LA SEGURIDAD. EL NOMBRE VIENE ESPECIFICADO EN EL "+str(float((count_bypassec_conseq_vulnibm_sh_specified*100)/count_bypassec_conseq_vulnibm_sh))+" % DE ELLAS. LOS PORCENTAJES DE VALOR DE NOMBRE SON LOS SIGUIENTES :  \n")
    print("            -    EN EL "+str(float((count_bypassec_conseq_namepathtraversal_vulnibm_sh*100)/count_bypassec_conseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE PATH TRAVERSAL \n")
    print("            -    EN EL "+str(float((count_bypassec_conseq_namedirectorytraversal_vulnibm_sh*100)/count_bypassec_conseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE DIRECTORY TRAVERSAL \n")
    print("            -    EN EL "+str(float((count_bypassec_conseq_nameprivilegeescalation_vulnibm_sh*100)/count_bypassec_conseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE PRIVILEGE ESCALATION \n") 
    print("            -    EN EL "+str(float((count_bypassec_conseq_namecrosssitescripting_vulnibm_sh*100)/count_bypassec_conseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE CROSS-SITE SCRIPTING  \n")
    print("            -    EN EL "+str(float((count_bypassec_conseq_namesecuritybypass_vulnibm_sh*100)/count_bypassec_conseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE SECURITY BYPASS  \n")
    print("            -    EN EL "+str(float((count_bypassec_conseq_namesinformationdisclosure_vulnibm_sh*100)/count_bypassec_conseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE INFORMATION DISCLOSURE \n")
    print("            -    EN EL "+str(float((count_bypassec_conseq_namedenialofservice_vulnibm_sh*100)/count_bypassec_conseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE DENIAL OF SERVICE  \n")
    print("            -    EN EL "+str(float((count_bypassec_conseq_namecodeexecution_vulnibm_sh*100)/count_bypassec_conseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE CODE EXECUTION  \n")
    print("            -    EN EL "+str(float((count_bypassec_conseq_namemaninthemiddle_vulnibm_sh*100)/count_bypassec_conseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE MAN IN THE MIDDLE  \n")
    print("            -    EN EL "+str(float((count_bypassec_conseq_namesqlinjection_vulnibm_sh*100)/count_bypassec_conseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE SQL INJECTION  \n")
    print("            -    EN EL "+str(float((count_bypassec_conseq_namecrosssiterequestforgery_vulnibm_sh*100)/count_bypassec_conseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE MODULE EXECUTION  \n")
    print("            -    EN EL "+str(float((count_bypassec_conseq_namemoduleexecution_vulnibm_sh*100)/count_bypassec_conseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE CROSS SITE REQUEST FORGERY  \n")
    print("            -    EN EL "+str(float((count_bypassec_conseq_namebufferoverflow_vulnibm_sh*100)/count_bypassec_conseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE BUFFER OVERFLOW \n")
    print("            -    EN EL "+str(float((count_bypassec_conseq_namecommandexecution_vulnibm_sh*100)/count_bypassec_conseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE COMMAND EXECUTION  \n")
    print("            -    EN EL "+str(float((count_bypassec_conseq_namespoofing_vulnibm_sh*100)/count_bypassec_conseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE SPOOFING  \n")
    print("            -    EN EL "+str(float((count_bypassec_conseq_nameclickjacking_vulnibm_sh*100)/count_bypassec_conseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE CLICKJACKING  \n")
    print("            -    EN EL "+str(float((count_bypassec_conseq_namehijacking_vulnibm_sh*100)/count_bypassec_conseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE HIJACKING  \n")
    print("            -    EN EL "+str(float((count_bypassec_conseq_namefileinclude_vulnibm_sh*100)/count_bypassec_conseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE FILE INCLUDE  \n")
    print("            -    EN EL "+str(float((count_bypassec_conseq_namebruteforce_vulnibm_sh*100)/count_bypassec_conseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE BRUTE FORCE  \n")
    print("            -    EN EL "+str(float((count_bypassec_conseq_namefileupload_vulnibm_sh*100)/count_bypassec_conseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE FILE UPLOAD  \n")
    print("            -    EN EL "+str(float((count_bypassec_conseq_nameheaderinjection_vulnibm_sh*100)/count_bypassec_conseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE HEADER INJECTION \n")
    print("            -    EN EL "+str(float((count_bypassec_conseq_nametampering_vulnibm_sh*100)/count_bypassec_conseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE TAMPERING  \n")
    print("            -    EN EL "+str(float((count_bypassec_conseq_nameanother_vulnibm_sh*100)/count_bypassec_conseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE OTRO VALOR DISTINTO A LOS ANTERIORES  \n")
    print("\n")  

if(count_filemani_conseq_vulnibm_sh>0):
    print("      -    EN EL "+str(float((count_filemani_conseq_vulnibm_sh*100)/count_conseq_vulnibm_sh))+" % DE VULNERABILIDADES LA CONSECUENCIA ES MANIPULACION DE FICHEROS. EL NOMBRE VIENE ESPECIFICADO EN EL "+str(float((count_filemani_conseq_vulnibm_sh_specified*100)/count_filemani_conseq_vulnibm_sh))+" % DE ELLAS. LOS PORCENTAJES DE VALOR DE NOMBRE SON LOS SIGUIENTES :  \n")
    print("            -    EN EL "+str(float((count_filemani_conseq_namepathtraversal_vulnibm_sh*100)/count_filemani_conseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE PATH TRAVERSAL \n")
    print("            -    EN EL "+str(float((count_filemani_conseq_namedirectorytraversal_vulnibm_sh*100)/count_filemani_conseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE DIRECTORY TRAVERSAL \n")
    print("            -    EN EL "+str(float((count_filemani_conseq_nameprivilegeescalation_vulnibm_sh*100)/count_filemani_conseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE PRIVILEGE ESCALATION \n") 
    print("            -    EN EL "+str(float((count_filemani_conseq_namecrosssitescripting_vulnibm_sh*100)/count_filemani_conseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE CROSS-SITE SCRIPTING  \n")
    print("            -    EN EL "+str(float((count_filemani_conseq_namesecuritybypass_vulnibm_sh*100)/count_filemani_conseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE SECURITY BYPASS  \n")
    print("            -    EN EL "+str(float((count_filemani_conseq_namesinformationdisclosure_vulnibm_sh*100)/count_filemani_conseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE INFORMATION DISCLOSURE \n")
    print("            -    EN EL "+str(float((count_filemani_conseq_namedenialofservice_vulnibm_sh*100)/count_filemani_conseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE DENIAL OF SERVICE  \n")
    print("            -    EN EL "+str(float((count_filemani_conseq_namecodeexecution_vulnibm_sh*100)/count_filemani_conseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE CODE EXECUTION  \n")
    print("            -    EN EL "+str(float((count_filemani_conseq_namemaninthemiddle_vulnibm_sh*100)/count_filemani_conseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE MAN IN THE MIDDLE  \n")
    print("            -    EN EL "+str(float((count_filemani_conseq_namesqlinjection_vulnibm_sh*100)/count_filemani_conseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE SQL INJECTION  \n")
    print("            -    EN EL "+str(float((count_filemani_conseq_namecrosssiterequestforgery_vulnibm_sh*100)/count_filemani_conseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE MODULE EXECUTION  \n")
    print("            -    EN EL "+str(float((count_filemani_conseq_namemoduleexecution_vulnibm_sh*100)/count_filemani_conseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE CROSS SITE REQUEST FORGERY  \n")
    print("            -    EN EL "+str(float((count_filemani_conseq_namebufferoverflow_vulnibm_sh*100)/count_filemani_conseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE BUFFER OVERFLOW \n")
    print("            -    EN EL "+str(float((count_filemani_conseq_namecommandexecution_vulnibm_sh*100)/count_filemani_conseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE COMMAND EXECUTION  \n")
    print("            -    EN EL "+str(float((count_filemani_conseq_namespoofing_vulnibm_sh*100)/count_filemani_conseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE SPOOFING  \n")
    print("            -    EN EL "+str(float((count_filemani_conseq_nameclickjacking_vulnibm_sh*100)/count_filemani_conseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE CLICKJACKING  \n")
    print("            -    EN EL "+str(float((count_filemani_conseq_namehijacking_vulnibm_sh*100)/count_filemani_conseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE HIJACKING  \n")
    print("            -    EN EL "+str(float((count_filemani_conseq_namefileinclude_vulnibm_sh*100)/count_filemani_conseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE FILE INCLUDE  \n")
    print("            -    EN EL "+str(float((count_filemani_conseq_namebruteforce_vulnibm_sh*100)/count_filemani_conseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE BRUTE FORCE  \n")
    print("            -    EN EL "+str(float((count_filemani_conseq_namefileupload_vulnibm_sh*100)/count_filemani_conseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE FILE UPLOAD  \n")
    print("            -    EN EL "+str(float((count_filemani_conseq_nameheaderinjection_vulnibm_sh*100)/count_filemani_conseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE HEADER INJECTION \n")
    print("            -    EN EL "+str(float((count_filemani_conseq_nametampering_vulnibm_sh*100)/count_filemani_conseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE TAMPERING  \n")
    print("            -    EN EL "+str(float((count_filemani_conseq_nameanother_vulnibm_sh*100)/count_filemani_conseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE OTRO VALOR DISTINTO A LOS ANTERIORES  \n")
    print("\n")
    
if(count_other_conseq_vulnibm_sh>0):
    print("      -    EN EL "+str(float((count_other_conseq_vulnibm_sh*100)/count_conseq_vulnibm_sh))+" % DE VULNERABILIDADES LA CONSECUENCIA ES OTRA DISTINTA A LAS ANTERIORES. EL NOMBRE VIENE ESPECIFICADO EN EL "+str(float((count_other_conseq_vulnibm_sh_specified*100)/count_other_conseq_vulnibm_sh))+" % DE ELLAS. LOS PORCENTAJES DE VALOR DE NOMBRE SON LOS SIGUIENTES :  \n")
    print("            -    EN EL "+str(float((count_other_conseq_namepathtraversal_vulnibm_sh*100)/count_other_conseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE PATH TRAVERSAL \n")
    print("            -    EN EL "+str(float((count_other_conseq_namedirectorytraversal_vulnibm_sh*100)/count_other_conseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE DIRECTORY TRAVERSAL \n")
    print("            -    EN EL "+str(float((count_other_conseq_nameprivilegeescalation_vulnibm_sh*100)/count_other_conseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE PRIVILEGE ESCALATION \n") 
    print("            -    EN EL "+str(float((count_other_conseq_namecrosssitescripting_vulnibm_sh*100)/count_other_conseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE CROSS-SITE SCRIPTING  \n")
    print("            -    EN EL "+str(float((count_other_conseq_namesecuritybypass_vulnibm_sh*100)/count_other_conseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE SECURITY BYPASS  \n")
    print("            -    EN EL "+str(float((count_other_conseq_namesinformationdisclosure_vulnibm_sh*100)/count_other_conseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE INFORMATION DISCLOSURE \n")
    print("            -    EN EL "+str(float((count_other_conseq_namedenialofservice_vulnibm_sh*100)/count_other_conseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE DENIAL OF SERVICE  \n")
    print("            -    EN EL "+str(float((count_other_conseq_namecodeexecution_vulnibm_sh*100)/count_other_conseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE CODE EXECUTION  \n")
    print("            -    EN EL "+str(float((count_other_conseq_namemaninthemiddle_vulnibm_sh*100)/count_other_conseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE MAN IN THE MIDDLE  \n")
    print("            -    EN EL "+str(float((count_other_conseq_namesqlinjection_vulnibm_sh*100)/count_other_conseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE SQL INJECTION  \n")
    print("            -    EN EL "+str(float((count_other_conseq_namecrosssiterequestforgery_vulnibm_sh*100)/count_other_conseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE MODULE EXECUTION  \n")
    print("            -    EN EL "+str(float((count_other_conseq_namemoduleexecution_vulnibm_sh*100)/count_other_conseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE CROSS SITE REQUEST FORGERY  \n")
    print("            -    EN EL "+str(float((count_other_conseq_namebufferoverflow_vulnibm_sh*100)/count_other_conseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE BUFFER OVERFLOW \n")
    print("            -    EN EL "+str(float((count_other_conseq_namecommandexecution_vulnibm_sh*100)/count_other_conseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE COMMAND EXECUTION  \n")
    print("            -    EN EL "+str(float((count_other_conseq_namespoofing_vulnibm_sh*100)/count_other_conseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE SPOOFING  \n")
    print("            -    EN EL "+str(float((count_other_conseq_nameclickjacking_vulnibm_sh*100)/count_other_conseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE CLICKJACKING  \n")
    print("            -    EN EL "+str(float((count_other_conseq_namehijacking_vulnibm_sh*100)/count_other_conseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE HIJACKING  \n")
    print("            -    EN EL "+str(float((count_other_conseq_namefileinclude_vulnibm_sh*100)/count_other_conseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE FILE INCLUDE  \n")
    print("            -    EN EL "+str(float((count_other_conseq_namebruteforce_vulnibm_sh*100)/count_other_conseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE BRUTE FORCE  \n")
    print("            -    EN EL "+str(float((count_other_conseq_namefileupload_vulnibm_sh*100)/count_other_conseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE FILE UPLOAD  \n")
    print("            -    EN EL "+str(float((count_other_conseq_nameheaderinjection_vulnibm_sh*100)/count_other_conseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE HEADER INJECTION \n")
    print("            -    EN EL "+str(float((count_other_conseq_nametampering_vulnibm_sh*100)/count_other_conseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE TAMPERING  \n")
    print("            -    EN EL "+str(float((count_other_conseq_nameanother_vulnibm_sh*100)/count_other_conseq_vulnibm_sh))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE OTRO VALOR DISTINTO A LOS ANTERIORES  \n")
    print("\n")
    
    
    
    
    
    
    
    
    
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
print("**********************ESTADÍSTICAS CONSECUENCIAS DE ATAQUE/NOMBRE VULNERABILIDADES IBM PARTE IOT Y SMART HOME CONJUNTAS**********************")
print("\n")                            
print("\n")
print(" DE UN TOTAL DE "+str(count_conseq_vulnibm_sh+count_conseq_vulnibm_iot)+" VULNERABILIDADES DONDE LAS CONSECUENCIAS VIENEN ESPECIFICADASS:\n") 
print("\n")
print("   - LAS ESTADISTICAS DE CONSECUENCIAS SON LAS SIGUIENTES:  \n")
print("      -    EN  "+str(count_obtaininfoconseq_vulnibm_sh+count_obtaininfoconseq_vulnibm_iot)+" VULNERABILIDADES LA CONSECUENCIA ES LA OBTENCION DE INFORMACION. EL NOMBRE VIENE ESPECIFICADO EN "+str(count_obtaininfoconseq_vulnibm_sh_specified+count_obtaininfoconseq_vulnibm_iot_specified)+" VULNERABILIDADES. LAS ESTADÍSTICAS DE VALORES DE NOMBRE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_obtaininfoconseq_namepathtraversal_vulnibm_sh+count_obtaininfoconseq_namepathtraversal_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE PATH TRAVERSAL \n")
print("            -    EN  "+str(count_obtaininfoconseq_namedirectorytraversal_vulnibm_sh+count_obtaininfoconseq_namedirectorytraversal_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE DIRECTORY TRAVERSAL \n")
print("            -    EN  "+str(count_obtaininfoconseq_nameprivilegeescalation_vulnibm_sh+count_obtaininfoconseq_nameprivilegeescalation_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE PRIVILEGE ESCALATION \n")
print("            -    EN  "+str(count_obtaininfoconseq_namecrosssitescripting_vulnibm_sh+count_obtaininfoconseq_namecrosssitescripting_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE CROSS-SITE SCRIPTING \n")
print("            -    EN  "+str(count_obtaininfoconseq_namesecuritybypass_vulnibm_sh+count_obtaininfoconseq_namesecuritybypass_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE SECURITY BYPASS \n")
print("            -    EN  "+str(count_obtaininfoconseq_namesinformationdisclosure_vulnibm_sh+count_obtaininfoconseq_namesinformationdisclosure_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE INFORMATION DISCLOSURE \n")
print("            -    EN  "+str(count_obtaininfoconseq_namedenialofservice_vulnibm_sh+count_obtaininfoconseq_namedenialofservice_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE DENIAL OF SERVICE \n")
print("            -    EN  "+str(count_obtaininfoconseq_namecodeexecution_vulnibm_sh+count_obtaininfoconseq_namecodeexecution_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE CODE EXECUTION \n")
print("            -    EN  "+str(count_obtaininfoconseq_namemaninthemiddle_vulnibm_sh+count_obtaininfoconseq_namemaninthemiddle_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE MAN IN THE MIDDLE \n")
print("            -    EN  "+str(count_obtaininfoconseq_namesqlinjection_vulnibm_sh+count_obtaininfoconseq_namesqlinjection_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE SQL INJECTION \n")
print("            -    EN  "+str(count_obtaininfoconseq_namemoduleexecution_vulnibm_sh+count_obtaininfoconseq_namemoduleexecution_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE MODULE EXECUTION \n")
print("            -    EN  "+str(count_obtaininfoconseq_namecrosssiterequestforgery_vulnibm_sh+count_obtaininfoconseq_namecrosssiterequestforgery_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE CROSS SITE REQUEST FORGERY \n")
print("            -    EN  "+str(count_obtaininfoconseq_namebufferoverflow_vulnibm_sh+count_obtaininfoconseq_namebufferoverflow_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE BUFFER OVERFLOW \n")
print("            -    EN  "+str(count_obtaininfoconseq_namecommandexecution_vulnibm_sh+count_obtaininfoconseq_namecommandexecution_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE COMMAND EXECUTION \n")
print("            -    EN  "+str(count_obtaininfoconseq_namespoofing_vulnibm_sh+count_obtaininfoconseq_namespoofing_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE SPOOFING \n")
print("            -    EN  "+str(count_obtaininfoconseq_nameclickjacking_vulnibm_sh+count_obtaininfoconseq_nameclickjacking_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE CLICKJACKING \n")
print("            -    EN  "+str(count_obtaininfoconseq_namehijacking_vulnibm_sh+count_obtaininfoconseq_namehijacking_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE HIJACKING \n")
print("            -    EN  "+str(count_obtaininfoconseq_namefileinclude_vulnibm_sh+count_obtaininfoconseq_namefileinclude_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE FILE INCLUDE \n")
print("            -    EN  "+str(count_obtaininfoconseq_namebruteforce_vulnibm_sh+count_obtaininfoconseq_namebruteforce_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE BRUTE FORCE \n")
print("            -    EN  "+str(count_obtaininfoconseq_namefileupload_vulnibm_sh+count_obtaininfoconseq_namefileupload_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE FILE UPLOAD \n")
print("            -    EN  "+str(count_obtaininfoconseq_nameheaderinjection_vulnibm_sh+count_obtaininfoconseq_nameheaderinjection_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE HEADER INJECTION \n")
print("            -    EN  "+str(count_obtaininfoconseq_nametampering_vulnibm_sh+count_obtaininfoconseq_nametampering_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE TAMPERING \n")
print("            -    EN  "+str(count_obtaininfoconseq_nameanother_vulnibm_sh+count_obtaininfoconseq_nameanother_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE OTRO VALOR DISTINTO A LOS ANTERIORES \n")
print("\n")
print("      -    EN  "+str(count_xss_conseq_vulnibm_sh+count_xss_conseq_vulnibm_iot)+" VULNERABILIDADES LA CONSECUENCIA ES CROSS-SITE SCRIPTING. EL NOMBRE VIENE ESPECIFICADO EN "+str(count_xss_conseq_vulnibm_sh_specified+count_xss_conseq_vulnibm_iot_specified)+" VULNERABILIDADES. LAS ESTADÍSTICAS DE VALORES DE NOMBRE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_xss_conseq_namepathtraversal_vulnibm_sh+count_xss_conseq_namepathtraversal_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE PATH TRAVERSAL \n")
print("            -    EN  "+str(count_xss_conseq_namedirectorytraversal_vulnibm_sh+count_xss_conseq_namedirectorytraversal_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE DIRECTORY TRAVERSAL \n")
print("            -    EN  "+str(count_xss_conseq_nameprivilegeescalation_vulnibm_sh+count_xss_conseq_nameprivilegeescalation_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE PRIVILEGE ESCALATION \n")
print("            -    EN  "+str(count_xss_conseq_namecrosssitescripting_vulnibm_sh+count_xss_conseq_namecrosssitescripting_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE CROSS-SITE SCRIPTING \n")
print("            -    EN  "+str(count_xss_conseq_namesecuritybypass_vulnibm_sh+count_xss_conseq_namesecuritybypass_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE SECURITY BYPASS \n")
print("            -    EN  "+str(count_xss_conseq_namesinformationdisclosure_vulnibm_sh+count_xss_conseq_namesinformationdisclosure_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE INFORMATION DISCLOSURE \n")
print("            -    EN  "+str(count_xss_conseq_namedenialofservice_vulnibm_sh+count_xss_conseq_namedenialofservice_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE DENIAL OF SERVICE \n")
print("            -    EN  "+str(count_xss_conseq_namecodeexecution_vulnibm_sh+count_xss_conseq_namecodeexecution_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE CODE EXECUTION \n")
print("            -    EN  "+str(count_xss_conseq_namemaninthemiddle_vulnibm_sh+count_xss_conseq_namemaninthemiddle_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE MAN IN THE MIDDLE \n")
print("            -    EN  "+str(count_xss_conseq_namesqlinjection_vulnibm_sh+count_xss_conseq_namesqlinjection_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE SQL INJECTION \n")
print("            -    EN  "+str(count_xss_conseq_namemoduleexecution_vulnibm_sh+count_xss_conseq_namemoduleexecution_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE MODULE EXECUTION \n")
print("            -    EN  "+str(count_xss_conseq_namecrosssiterequestforgery_vulnibm_sh+count_xss_conseq_namecrosssiterequestforgery_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE CROSS SITE REQUEST FORGERY \n")
print("            -    EN  "+str(count_xss_conseq_namebufferoverflow_vulnibm_sh+count_xss_conseq_namebufferoverflow_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE BUFFER OVERFLOW \n")
print("            -    EN  "+str(count_xss_conseq_namecommandexecution_vulnibm_sh+count_xss_conseq_namecommandexecution_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE COMMAND EXECUTION \n")
print("            -    EN  "+str(count_xss_conseq_namespoofing_vulnibm_sh+count_xss_conseq_namespoofing_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE SPOOFING \n")
print("            -    EN  "+str(count_xss_conseq_nameclickjacking_vulnibm_sh+count_xss_conseq_nameclickjacking_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE CLICKJACKING \n")
print("            -    EN  "+str(count_xss_conseq_namehijacking_vulnibm_sh+count_xss_conseq_namehijacking_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE HIJACKING \n")
print("            -    EN  "+str(count_xss_conseq_namefileinclude_vulnibm_sh+count_xss_conseq_namefileinclude_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE FILE INCLUDE \n")
print("            -    EN  "+str(count_xss_conseq_namebruteforce_vulnibm_sh+count_xss_conseq_namebruteforce_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE BRUTE FORCE \n")
print("            -    EN  "+str(count_xss_conseq_namefileupload_vulnibm_sh+count_xss_conseq_namefileupload_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE FILE UPLOAD \n")
print("            -    EN  "+str(count_xss_conseq_nameheaderinjection_vulnibm_sh+count_xss_conseq_nameheaderinjection_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE HEADER INJECTION \n")
print("            -    EN  "+str(count_xss_conseq_nametampering_vulnibm_sh+count_xss_conseq_nametampering_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE TAMPERING \n")
print("            -    EN  "+str(count_xss_conseq_nameanother_vulnibm_sh+count_xss_conseq_nameanother_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE OTRO VALOR DISTINTO A LOS ANTERIORES \n")
print("\n")
print("      -    EN  "+str(count_gainacc_conseq_vulnibm_sh+count_gainacc_conseq_vulnibm_iot)+" VULNERABILIDADES LA CONSECUENCIA ES LA OBTENCION DE ACCESO. EL NOMBRE VIENE ESPECIFICADO EN "+str(count_gainacc_conseq_vulnibm_sh_specified+count_gainacc_conseq_vulnibm_iot_specified)+" VULNERABILIDADES. LAS ESTADÍSTICAS DE VALORES DE NOMBRE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_gainacc_conseq_namepathtraversal_vulnibm_sh+count_gainacc_conseq_namepathtraversal_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE PATH TRAVERSAL \n")
print("            -    EN  "+str(count_gainacc_conseq_namedirectorytraversal_vulnibm_sh+count_gainacc_conseq_namedirectorytraversal_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE DIRECTORY TRAVERSAL \n")
print("            -    EN  "+str(count_gainacc_conseq_nameprivilegeescalation_vulnibm_sh+count_gainacc_conseq_nameprivilegeescalation_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE PRIVILEGE ESCALATION \n")
print("            -    EN  "+str(count_gainacc_conseq_namecrosssitescripting_vulnibm_sh+count_gainacc_conseq_namecrosssitescripting_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE CROSS-SITE SCRIPTING \n")
print("            -    EN  "+str(count_gainacc_conseq_namesecuritybypass_vulnibm_sh+count_gainacc_conseq_namesecuritybypass_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE SECURITY BYPASS \n")
print("            -    EN  "+str(count_gainacc_conseq_namesinformationdisclosure_vulnibm_sh+count_gainacc_conseq_namesinformationdisclosure_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE INFORMATION DISCLOSURE \n")
print("            -    EN  "+str(count_gainacc_conseq_namedenialofservice_vulnibm_sh+count_gainacc_conseq_namedenialofservice_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE DENIAL OF SERVICE \n")
print("            -    EN  "+str(count_gainacc_conseq_namecodeexecution_vulnibm_sh+count_gainacc_conseq_namecodeexecution_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE CODE EXECUTION \n")
print("            -    EN  "+str(count_gainacc_conseq_namemaninthemiddle_vulnibm_sh+count_gainacc_conseq_namemaninthemiddle_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE MAN IN THE MIDDLE \n")
print("            -    EN  "+str(count_gainacc_conseq_namesqlinjection_vulnibm_sh+count_gainacc_conseq_namesqlinjection_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE SQL INJECTION \n")
print("            -    EN  "+str(count_gainacc_conseq_namemoduleexecution_vulnibm_sh+count_gainacc_conseq_namemoduleexecution_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE MODULE EXECUTION \n")
print("            -    EN  "+str(count_gainacc_conseq_namecrosssiterequestforgery_vulnibm_sh+count_gainacc_conseq_namecrosssiterequestforgery_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE CROSS SITE REQUEST FORGERY \n")
print("            -    EN  "+str(count_gainacc_conseq_namebufferoverflow_vulnibm_sh+count_gainacc_conseq_namebufferoverflow_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE BUFFER OVERFLOW \n")
print("            -    EN  "+str(count_gainacc_conseq_namecommandexecution_vulnibm_sh+count_gainacc_conseq_namecommandexecution_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE COMMAND EXECUTION \n")
print("            -    EN  "+str(count_gainacc_conseq_namespoofing_vulnibm_sh+count_gainacc_conseq_namespoofing_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE SPOOFING \n")
print("            -    EN  "+str(count_gainacc_conseq_nameclickjacking_vulnibm_sh+count_gainacc_conseq_nameclickjacking_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE CLICKJACKING \n")
print("            -    EN  "+str(count_gainacc_conseq_namehijacking_vulnibm_sh+count_gainacc_conseq_namehijacking_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE HIJACKING \n")
print("            -    EN  "+str(count_gainacc_conseq_namefileinclude_vulnibm_sh+count_gainacc_conseq_namefileinclude_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE FILE INCLUDE \n")
print("            -    EN  "+str(count_gainacc_conseq_namebruteforce_vulnibm_sh+count_gainacc_conseq_namebruteforce_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE BRUTE FORCE \n")
print("            -    EN  "+str(count_gainacc_conseq_namefileupload_vulnibm_sh+count_gainacc_conseq_namefileupload_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE FILE UPLOAD \n")
print("            -    EN  "+str(count_gainacc_conseq_nameheaderinjection_vulnibm_sh+count_gainacc_conseq_nameheaderinjection_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE HEADER INJECTION \n")
print("            -    EN  "+str(count_gainacc_conseq_nametampering_vulnibm_sh+count_gainacc_conseq_nametampering_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE TAMPERING \n")
print("            -    EN  "+str(count_gainacc_conseq_nameanother_vulnibm_sh+count_gainacc_conseq_nameanother_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE OTRO VALOR DISTINTO A LOS ANTERIORES \n")
print("\n")
print("      -    EN  "+str(count_gainpriv_conseq_vulnibm_sh+count_gainpriv_conseq_vulnibm_iot)+" VULNERABILIDADES LA CONSECUENCIA ES LA OBTENCION DE PRIVILEGIOS. EL NOMBRE VIENE ESPECIFICADO EN "+str(count_gainpriv_conseq_vulnibm_sh_specified+count_gainpriv_conseq_vulnibm_iot_specified)+" VULNERABILIDADES. LAS ESTADÍSTICAS DE VALORES DE NOMBRE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_gainpriv_conseq_namepathtraversal_vulnibm_sh+count_gainpriv_conseq_namepathtraversal_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE PATH TRAVERSAL \n")
print("            -    EN  "+str(count_gainpriv_conseq_namedirectorytraversal_vulnibm_sh+count_gainpriv_conseq_namedirectorytraversal_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE DIRECTORY TRAVERSAL \n")
print("            -    EN  "+str(count_gainpriv_conseq_nameprivilegeescalation_vulnibm_sh+count_gainpriv_conseq_nameprivilegeescalation_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE PRIVILEGE ESCALATION \n")
print("            -    EN  "+str(count_gainpriv_conseq_namecrosssitescripting_vulnibm_sh+count_gainpriv_conseq_namecrosssitescripting_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE CROSS-SITE SCRIPTING \n")
print("            -    EN  "+str(count_gainpriv_conseq_namesecuritybypass_vulnibm_sh+count_gainpriv_conseq_namesecuritybypass_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE SECURITY BYPASS \n")
print("            -    EN  "+str(count_gainpriv_conseq_namesinformationdisclosure_vulnibm_sh+count_gainpriv_conseq_namesinformationdisclosure_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE INFORMATION DISCLOSURE \n")
print("            -    EN  "+str(count_gainpriv_conseq_namedenialofservice_vulnibm_sh+count_gainpriv_conseq_namedenialofservice_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE DENIAL OF SERVICE \n")
print("            -    EN  "+str(count_gainpriv_conseq_namecodeexecution_vulnibm_sh+count_gainpriv_conseq_namecodeexecution_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE CODE EXECUTION \n")
print("            -    EN  "+str(count_gainpriv_conseq_namemaninthemiddle_vulnibm_sh+count_gainpriv_conseq_namemaninthemiddle_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE MAN IN THE MIDDLE \n")
print("            -    EN  "+str(count_gainpriv_conseq_namesqlinjection_vulnibm_sh+count_gainpriv_conseq_namesqlinjection_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE SQL INJECTION \n")
print("            -    EN  "+str(count_gainpriv_conseq_namemoduleexecution_vulnibm_sh+count_gainpriv_conseq_namemoduleexecution_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE MODULE EXECUTION \n")
print("            -    EN  "+str(count_gainpriv_conseq_namecrosssiterequestforgery_vulnibm_sh+count_gainpriv_conseq_namecrosssiterequestforgery_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE CROSS SITE REQUEST FORGERY \n")
print("            -    EN  "+str(count_gainpriv_conseq_namebufferoverflow_vulnibm_sh+count_gainpriv_conseq_namebufferoverflow_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE BUFFER OVERFLOW \n")
print("            -    EN  "+str(count_gainpriv_conseq_namecommandexecution_vulnibm_sh+count_gainpriv_conseq_namecommandexecution_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE COMMAND EXECUTION \n")
print("            -    EN  "+str(count_gainpriv_conseq_namespoofing_vulnibm_sh+count_gainpriv_conseq_namespoofing_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE SPOOFING \n")
print("            -    EN  "+str(count_gainpriv_conseq_nameclickjacking_vulnibm_sh+count_gainpriv_conseq_nameclickjacking_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE CLICKJACKING \n")
print("            -    EN  "+str(count_gainpriv_conseq_namehijacking_vulnibm_sh+count_gainpriv_conseq_namehijacking_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE HIJACKING \n")
print("            -    EN  "+str(count_gainpriv_conseq_namefileinclude_vulnibm_sh+count_gainpriv_conseq_namefileinclude_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE FILE INCLUDE \n")
print("            -    EN  "+str(count_gainpriv_conseq_namebruteforce_vulnibm_sh+count_gainpriv_conseq_namebruteforce_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE BRUTE FORCE \n")
print("            -    EN  "+str(count_gainpriv_conseq_namefileupload_vulnibm_sh+count_gainpriv_conseq_namefileupload_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE FILE UPLOAD \n")
print("            -    EN  "+str(count_gainpriv_conseq_nameheaderinjection_vulnibm_sh+count_gainpriv_conseq_nameheaderinjection_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE HEADER INJECTION \n")
print("            -    EN  "+str(count_gainpriv_conseq_nametampering_vulnibm_sh+count_gainpriv_conseq_nametampering_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE TAMPERING \n")
print("            -    EN  "+str(count_gainpriv_conseq_nameanother_vulnibm_sh+count_gainpriv_conseq_nameanother_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE OTRO VALOR DISTINTO A LOS ANTERIORES \n")
print("\n")
print("      -    EN  "+str(count_denialofserv_conseq_vulnibm_sh+count_denialofserv_conseq_vulnibm_iot)+" VULNERABILIDADES LA CONSECUENCIA ES UNA DENEGACION DE SERVICIO. EL NOMBRE VIENE ESPECIFICADO EN "+str(count_denialofserv_conseq_vulnibm_sh_specified+count_denialofserv_conseq_vulnibm_iot_specified)+" VULNERABILIDADES. LAS ESTADÍSTICAS DE VALORES DE NOMBRE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_denialofserv_conseq_namepathtraversal_vulnibm_sh+count_denialofserv_conseq_namepathtraversal_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE PATH TRAVERSAL \n")
print("            -    EN  "+str(count_denialofserv_conseq_namedirectorytraversal_vulnibm_sh+count_denialofserv_conseq_namedirectorytraversal_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE DIRECTORY TRAVERSAL \n")
print("            -    EN  "+str(count_denialofserv_conseq_nameprivilegeescalation_vulnibm_sh+count_denialofserv_conseq_nameprivilegeescalation_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE PRIVILEGE ESCALATION \n")
print("            -    EN  "+str(count_denialofserv_conseq_namecrosssitescripting_vulnibm_sh+count_denialofserv_conseq_namecrosssitescripting_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE CROSS-SITE SCRIPTING \n")
print("            -    EN  "+str(count_denialofserv_conseq_namesecuritybypass_vulnibm_sh+count_denialofserv_conseq_namesecuritybypass_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE SECURITY BYPASS \n")
print("            -    EN  "+str(count_denialofserv_conseq_namesinformationdisclosure_vulnibm_sh+count_denialofserv_conseq_namesinformationdisclosure_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE INFORMATION DISCLOSURE \n")
print("            -    EN  "+str(count_denialofserv_conseq_namedenialofservice_vulnibm_sh+count_denialofserv_conseq_namedenialofservice_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE DENIAL OF SERVICE \n")
print("            -    EN  "+str(count_denialofserv_conseq_namecodeexecution_vulnibm_sh+count_denialofserv_conseq_namecodeexecution_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE CODE EXECUTION \n")
print("            -    EN  "+str(count_denialofserv_conseq_namemaninthemiddle_vulnibm_sh+count_denialofserv_conseq_namemaninthemiddle_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE MAN IN THE MIDDLE \n")
print("            -    EN  "+str(count_denialofserv_conseq_namesqlinjection_vulnibm_sh+count_denialofserv_conseq_namesqlinjection_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE SQL INJECTION \n")
print("            -    EN  "+str(count_denialofserv_conseq_namemoduleexecution_vulnibm_sh+count_denialofserv_conseq_namemoduleexecution_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE MODULE EXECUTION \n")
print("            -    EN  "+str(count_denialofserv_conseq_namecrosssiterequestforgery_vulnibm_sh+count_denialofserv_conseq_namecrosssiterequestforgery_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE CROSS SITE REQUEST FORGERY \n")
print("            -    EN  "+str(count_denialofserv_conseq_namebufferoverflow_vulnibm_sh+count_denialofserv_conseq_namebufferoverflow_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE BUFFER OVERFLOW \n")
print("            -    EN  "+str(count_denialofserv_conseq_namecommandexecution_vulnibm_sh+count_denialofserv_conseq_namecommandexecution_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE COMMAND EXECUTION \n")
print("            -    EN  "+str(count_denialofserv_conseq_namespoofing_vulnibm_sh+count_denialofserv_conseq_namespoofing_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE SPOOFING \n")
print("            -    EN  "+str(count_denialofserv_conseq_nameclickjacking_vulnibm_sh+count_denialofserv_conseq_nameclickjacking_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE CLICKJACKING \n")
print("            -    EN  "+str(count_denialofserv_conseq_namehijacking_vulnibm_sh+count_denialofserv_conseq_namehijacking_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE HIJACKING \n")
print("            -    EN  "+str(count_denialofserv_conseq_namefileinclude_vulnibm_sh+count_denialofserv_conseq_namefileinclude_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE FILE INCLUDE \n")
print("            -    EN  "+str(count_denialofserv_conseq_namebruteforce_vulnibm_sh+count_denialofserv_conseq_namebruteforce_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE BRUTE FORCE \n")
print("            -    EN  "+str(count_denialofserv_conseq_namefileupload_vulnibm_sh+count_denialofserv_conseq_namefileupload_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE FILE UPLOAD \n")
print("            -    EN  "+str(count_denialofserv_conseq_nameheaderinjection_vulnibm_sh+count_denialofserv_conseq_nameheaderinjection_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE HEADER INJECTION \n")
print("            -    EN  "+str(count_denialofserv_conseq_nametampering_vulnibm_sh+count_denialofserv_conseq_nametampering_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE TAMPERING \n")
print("            -    EN  "+str(count_denialofserv_conseq_nameanother_vulnibm_sh+count_denialofserv_conseq_nameanother_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE OTRO VALOR DISTINTO A LOS ANTERIORES \n")
print("\n")
print("      -    EN  "+str(count_bypassec_conseq_vulnibm_sh+count_bypassec_conseq_vulnibm_iot)+" VULNERABILIDADES LA CONSECUENCIA ES SOBREPASAR LA SEGURIDAD. EL NOMBRE VIENE ESPECIFICADO EN "+str(count_bypassec_conseq_vulnibm_sh_specified+count_bypassec_conseq_vulnibm_iot_specified)+" VULNERABILIDADES. LAS ESTADÍSTICAS DE VALORES DE NOMBRE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_bypassec_conseq_namepathtraversal_vulnibm_sh+count_bypassec_conseq_namepathtraversal_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE PATH TRAVERSAL \n")
print("            -    EN  "+str(count_bypassec_conseq_namedirectorytraversal_vulnibm_sh+count_bypassec_conseq_namedirectorytraversal_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE DIRECTORY TRAVERSAL \n")
print("            -    EN  "+str(count_bypassec_conseq_nameprivilegeescalation_vulnibm_sh+count_bypassec_conseq_nameprivilegeescalation_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE PRIVILEGE ESCALATION \n")
print("            -    EN  "+str(count_bypassec_conseq_namecrosssitescripting_vulnibm_sh+count_bypassec_conseq_namecrosssitescripting_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE CROSS-SITE SCRIPTING \n")
print("            -    EN  "+str(count_bypassec_conseq_namesecuritybypass_vulnibm_sh+count_bypassec_conseq_namesecuritybypass_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE SECURITY BYPASS \n")
print("            -    EN  "+str(count_bypassec_conseq_namesinformationdisclosure_vulnibm_sh+count_bypassec_conseq_namesinformationdisclosure_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE INFORMATION DISCLOSURE \n")
print("            -    EN  "+str(count_bypassec_conseq_namedenialofservice_vulnibm_sh+count_bypassec_conseq_namedenialofservice_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE DENIAL OF SERVICE \n")
print("            -    EN  "+str(count_bypassec_conseq_namecodeexecution_vulnibm_sh+count_bypassec_conseq_namecodeexecution_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE CODE EXECUTION \n")
print("            -    EN  "+str(count_bypassec_conseq_namemaninthemiddle_vulnibm_sh+count_bypassec_conseq_namemaninthemiddle_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE MAN IN THE MIDDLE \n")
print("            -    EN  "+str(count_bypassec_conseq_namesqlinjection_vulnibm_sh+count_bypassec_conseq_namesqlinjection_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE SQL INJECTION \n")
print("            -    EN  "+str(count_bypassec_conseq_namemoduleexecution_vulnibm_sh+count_bypassec_conseq_namemoduleexecution_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE MODULE EXECUTION \n")
print("            -    EN  "+str(count_bypassec_conseq_namecrosssiterequestforgery_vulnibm_sh+count_bypassec_conseq_namecrosssiterequestforgery_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE CROSS SITE REQUEST FORGERY \n")
print("            -    EN  "+str(count_bypassec_conseq_namebufferoverflow_vulnibm_sh+count_bypassec_conseq_namebufferoverflow_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE BUFFER OVERFLOW \n")
print("            -    EN  "+str(count_bypassec_conseq_namecommandexecution_vulnibm_sh+count_bypassec_conseq_namecommandexecution_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE COMMAND EXECUTION \n")
print("            -    EN  "+str(count_bypassec_conseq_namespoofing_vulnibm_sh+count_bypassec_conseq_namespoofing_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE SPOOFING \n")
print("            -    EN  "+str(count_bypassec_conseq_nameclickjacking_vulnibm_sh+count_bypassec_conseq_nameclickjacking_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE CLICKJACKING \n")
print("            -    EN  "+str(count_bypassec_conseq_namehijacking_vulnibm_sh+count_bypassec_conseq_namehijacking_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE HIJACKING \n")
print("            -    EN  "+str(count_bypassec_conseq_namefileinclude_vulnibm_sh+count_bypassec_conseq_namefileinclude_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE FILE INCLUDE \n")
print("            -    EN  "+str(count_bypassec_conseq_namebruteforce_vulnibm_sh+count_bypassec_conseq_namebruteforce_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE BRUTE FORCE \n")
print("            -    EN  "+str(count_bypassec_conseq_namefileupload_vulnibm_sh+count_bypassec_conseq_namefileupload_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE FILE UPLOAD \n")
print("            -    EN  "+str(count_bypassec_conseq_nameheaderinjection_vulnibm_sh+count_bypassec_conseq_nameheaderinjection_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE HEADER INJECTION \n")
print("            -    EN  "+str(count_bypassec_conseq_nametampering_vulnibm_sh+count_bypassec_conseq_nametampering_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE TAMPERING \n")
print("            -    EN  "+str(count_bypassec_conseq_nameanother_vulnibm_sh+count_bypassec_conseq_nameanother_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE OTRO VALOR DISTINTO A LOS ANTERIORES \n")
print("\n")
print("      -    EN  "+str(count_filemani_conseq_vulnibm_sh+count_filemani_conseq_vulnibm_iot)+" VULNERABILIDADES LA CONSECUENCIA ES LA MANIPULACION DE FICHEROS. EL NOMBRE VIENE ESPECIFICADO EN "+str(count_filemani_conseq_vulnibm_sh_specified+count_filemani_conseq_vulnibm_iot_specified)+" VULNERABILIDADES. LAS ESTADÍSTICAS DE VALORES DE NOMBRE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_filemani_conseq_namepathtraversal_vulnibm_sh+count_filemani_conseq_namepathtraversal_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE PATH TRAVERSAL \n")
print("            -    EN  "+str(count_filemani_conseq_namedirectorytraversal_vulnibm_sh+count_filemani_conseq_namedirectorytraversal_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE DIRECTORY TRAVERSAL \n")
print("            -    EN  "+str(count_filemani_conseq_nameprivilegeescalation_vulnibm_sh+count_filemani_conseq_nameprivilegeescalation_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE PRIVILEGE ESCALATION \n")
print("            -    EN  "+str(count_filemani_conseq_namecrosssitescripting_vulnibm_sh+count_filemani_conseq_namecrosssitescripting_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE CROSS-SITE SCRIPTING \n")
print("            -    EN  "+str(count_filemani_conseq_namesecuritybypass_vulnibm_sh+count_filemani_conseq_namesecuritybypass_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE SECURITY BYPASS \n")
print("            -    EN  "+str(count_filemani_conseq_namesinformationdisclosure_vulnibm_sh+count_filemani_conseq_namesinformationdisclosure_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE INFORMATION DISCLOSURE \n")
print("            -    EN  "+str(count_filemani_conseq_namedenialofservice_vulnibm_sh+count_filemani_conseq_namedenialofservice_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE DENIAL OF SERVICE \n")
print("            -    EN  "+str(count_filemani_conseq_namecodeexecution_vulnibm_sh+count_filemani_conseq_namecodeexecution_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE CODE EXECUTION \n")
print("            -    EN  "+str(count_filemani_conseq_namemaninthemiddle_vulnibm_sh+count_filemani_conseq_namemaninthemiddle_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE MAN IN THE MIDDLE \n")
print("            -    EN  "+str(count_filemani_conseq_namesqlinjection_vulnibm_sh+count_filemani_conseq_namesqlinjection_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE SQL INJECTION \n")
print("            -    EN  "+str(count_filemani_conseq_namemoduleexecution_vulnibm_sh+count_filemani_conseq_namemoduleexecution_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE MODULE EXECUTION \n")
print("            -    EN  "+str(count_filemani_conseq_namecrosssiterequestforgery_vulnibm_sh+count_filemani_conseq_namecrosssiterequestforgery_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE CROSS SITE REQUEST FORGERY \n")
print("            -    EN  "+str(count_filemani_conseq_namebufferoverflow_vulnibm_sh+count_filemani_conseq_namebufferoverflow_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE BUFFER OVERFLOW \n")
print("            -    EN  "+str(count_filemani_conseq_namecommandexecution_vulnibm_sh+count_filemani_conseq_namecommandexecution_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE COMMAND EXECUTION \n")
print("            -    EN  "+str(count_filemani_conseq_namespoofing_vulnibm_sh+count_filemani_conseq_namespoofing_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE SPOOFING \n")
print("            -    EN  "+str(count_filemani_conseq_nameclickjacking_vulnibm_sh+count_filemani_conseq_nameclickjacking_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE CLICKJACKING \n")
print("            -    EN  "+str(count_filemani_conseq_namehijacking_vulnibm_sh+count_filemani_conseq_namehijacking_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE HIJACKING \n")
print("            -    EN  "+str(count_filemani_conseq_namefileinclude_vulnibm_sh+count_filemani_conseq_namefileinclude_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE FILE INCLUDE \n")
print("            -    EN  "+str(count_filemani_conseq_namebruteforce_vulnibm_sh+count_filemani_conseq_namebruteforce_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE BRUTE FORCE \n")
print("            -    EN  "+str(count_filemani_conseq_namefileupload_vulnibm_sh+count_filemani_conseq_namefileupload_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE FILE UPLOAD \n")
print("            -    EN  "+str(count_filemani_conseq_nameheaderinjection_vulnibm_sh+count_filemani_conseq_nameheaderinjection_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE HEADER INJECTION \n")
print("            -    EN  "+str(count_filemani_conseq_nametampering_vulnibm_sh+count_filemani_conseq_nametampering_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE TAMPERING \n")
print("            -    EN  "+str(count_filemani_conseq_nameanother_vulnibm_sh+count_filemani_conseq_nameanother_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE OTRO VALOR DISTINTO A LOS ANTERIORES \n")
print("\n")
print("      -    EN  "+str(count_other_conseq_vulnibm_sh+count_other_conseq_vulnibm_iot)+" VULNERABILIDADES LA CONSECUENCIA ES OTRA DISTINTA A LAS ANTERIORES. EL NOMBRE VIENE ESPECIFICADO EN "+str(count_other_conseq_vulnibm_sh_specified+count_other_conseq_vulnibm_iot_specified)+" VULNERABILIDADES. LAS ESTADÍSTICAS DE VALORES DE NOMBRE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_other_conseq_namepathtraversal_vulnibm_sh+count_other_conseq_namepathtraversal_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE PATH TRAVERSAL \n")
print("            -    EN  "+str(count_other_conseq_namedirectorytraversal_vulnibm_sh+count_other_conseq_namedirectorytraversal_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE DIRECTORY TRAVERSAL \n")
print("            -    EN  "+str(count_other_conseq_nameprivilegeescalation_vulnibm_sh+count_other_conseq_nameprivilegeescalation_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE PRIVILEGE ESCALATION \n")
print("            -    EN  "+str(count_other_conseq_namecrosssitescripting_vulnibm_sh+count_other_conseq_namecrosssitescripting_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE CROSS-SITE SCRIPTING \n")
print("            -    EN  "+str(count_other_conseq_namesecuritybypass_vulnibm_sh+count_other_conseq_namesecuritybypass_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE SECURITY BYPASS \n")
print("            -    EN  "+str(count_other_conseq_namesinformationdisclosure_vulnibm_sh+count_other_conseq_namesinformationdisclosure_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE INFORMATION DISCLOSURE \n")
print("            -    EN  "+str(count_other_conseq_namedenialofservice_vulnibm_sh+count_other_conseq_namedenialofservice_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE DENIAL OF SERVICE \n")
print("            -    EN  "+str(count_other_conseq_namecodeexecution_vulnibm_sh+count_other_conseq_namecodeexecution_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE CODE EXECUTION \n")
print("            -    EN  "+str(count_other_conseq_namemaninthemiddle_vulnibm_sh+count_other_conseq_namemaninthemiddle_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE MAN IN THE MIDDLE \n")
print("            -    EN  "+str(count_other_conseq_namesqlinjection_vulnibm_sh+count_other_conseq_namesqlinjection_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE SQL INJECTION \n")
print("            -    EN  "+str(count_other_conseq_namemoduleexecution_vulnibm_sh+count_other_conseq_namemoduleexecution_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE MODULE EXECUTION \n")
print("            -    EN  "+str(count_other_conseq_namecrosssiterequestforgery_vulnibm_sh+count_other_conseq_namecrosssiterequestforgery_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE CROSS SITE REQUEST FORGERY \n")
print("            -    EN  "+str(count_other_conseq_namebufferoverflow_vulnibm_sh+count_other_conseq_namebufferoverflow_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE BUFFER OVERFLOW \n")
print("            -    EN  "+str(count_other_conseq_namecommandexecution_vulnibm_sh+count_other_conseq_namecommandexecution_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE COMMAND EXECUTION \n")
print("            -    EN  "+str(count_other_conseq_namespoofing_vulnibm_sh+count_other_conseq_namespoofing_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE SPOOFING \n")
print("            -    EN  "+str(count_other_conseq_nameclickjacking_vulnibm_sh+count_other_conseq_nameclickjacking_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE CLICKJACKING \n")
print("            -    EN  "+str(count_other_conseq_namehijacking_vulnibm_sh+count_other_conseq_namehijacking_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE HIJACKING \n")
print("            -    EN  "+str(count_other_conseq_namefileinclude_vulnibm_sh+count_other_conseq_namefileinclude_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE FILE INCLUDE \n")
print("            -    EN  "+str(count_other_conseq_namebruteforce_vulnibm_sh+count_other_conseq_namebruteforce_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE BRUTE FORCE \n")
print("            -    EN  "+str(count_other_conseq_namefileupload_vulnibm_sh+count_other_conseq_namefileupload_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE FILE UPLOAD \n")
print("            -    EN  "+str(count_other_conseq_nameheaderinjection_vulnibm_sh+count_other_conseq_nameheaderinjection_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE HEADER INJECTION \n")
print("            -    EN  "+str(count_other_conseq_nametampering_vulnibm_sh+count_other_conseq_nametampering_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE TAMPERING \n")
print("            -    EN  "+str(count_other_conseq_nameanother_vulnibm_sh+count_other_conseq_nameanother_vulnibm_iot)+" VULNERABILIDADES EL NOMBRE INCLUYE OTRO VALOR DISTINTO A LOS ANTERIORES \n")
print("\n")
















    
    
print("**********************PORCENTAJES CONSECUENCIAS DE ATAQUE/NOMBRE VULNERABILIDADES PARTE IOT Y SMART HOME CONJUNTAS**********************")
print("\n")                            
print("\n")
print(" DE UN TOTAL DE "+str(count_conseq_vulnibm_sh+count_conseq_vulnibm_iot)+" VULNERABILIDADES :\n") 
print("\n")
print("   - LOS PORCENTAJES DE CONSECUENCIAS SON LOS SIGUIENTES:  \n")
if((count_obtaininfoconseq_vulnibm_sh+count_obtaininfoconseq_vulnibm_iot)>0):
    print("      -    EN EL "+str(float((count_obtaininfoconseq_vulnibm_sh+count_obtaininfoconseq_vulnibm_iot)*100)/(count_conseq_vulnibm_sh+count_conseq_vulnibm_iot))+" % DE VULNERABILIDADES LA CONSECUENCIA ES LA OBTENCION DE INFORMACION. EL NOMBRE VIENE ESPECIFICADO EN EL "+str(float(((count_obtaininfoconseq_vulnibm_sh_specified+count_obtaininfoconseq_vulnibm_iot_specified)*100)/(count_obtaininfoconseq_vulnibm_sh+count_obtaininfoconseq_vulnibm_iot)))+" % DE ELLAS. LOS PORCENTAJES DE VALOR DE NOMBRE SON LOS SIGUIENTES :  \n")
    print("            -    EN EL "+str(float(((count_obtaininfoconseq_namepathtraversal_vulnibm_sh+count_obtaininfoconseq_namepathtraversal_vulnibm_iot)*100)/(count_obtaininfoconseq_vulnibm_sh+count_obtaininfoconseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE PATH TRAVERSAL \n")
    print("            -    EN EL "+str(float(((count_obtaininfoconseq_namedirectorytraversal_vulnibm_sh+count_obtaininfoconseq_namedirectorytraversal_vulnibm_iot)*100)/(count_obtaininfoconseq_vulnibm_sh+count_obtaininfoconseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE DIRECTORY TRAVERSAL \n")
    print("            -    EN EL "+str(float(((count_obtaininfoconseq_nameprivilegeescalation_vulnibm_sh+count_obtaininfoconseq_nameprivilegeescalation_vulnibm_iot)*100)/(count_obtaininfoconseq_vulnibm_sh+count_obtaininfoconseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE PRIVILEGE ESCALATION \n") 
    print("            -    EN EL "+str(float(((count_obtaininfoconseq_namecrosssitescripting_vulnibm_sh+count_obtaininfoconseq_namecrosssitescripting_vulnibm_iot)*100)/(count_obtaininfoconseq_vulnibm_sh+count_obtaininfoconseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE CROSS-SITE SCRIPTING  \n")
    print("            -    EN EL "+str(float(((count_obtaininfoconseq_namesecuritybypass_vulnibm_sh+count_obtaininfoconseq_namesecuritybypass_vulnibm_iot)*100)/(count_obtaininfoconseq_vulnibm_sh+count_obtaininfoconseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE SECURITY BYPASS  \n")
    print("            -    EN EL "+str(float(((count_obtaininfoconseq_namesinformationdisclosure_vulnibm_sh+count_obtaininfoconseq_namesinformationdisclosure_vulnibm_iot)*100)/(count_obtaininfoconseq_vulnibm_sh+count_obtaininfoconseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE INFORMATION DISCLOSURE \n")
    print("            -    EN EL "+str(float(((count_obtaininfoconseq_namedenialofservice_vulnibm_sh+count_obtaininfoconseq_namedenialofservice_vulnibm_iot)*100)/(count_obtaininfoconseq_vulnibm_sh+count_obtaininfoconseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE DENIAL OF SERVICE  \n")
    print("            -    EN EL "+str(float(((count_obtaininfoconseq_namecodeexecution_vulnibm_sh+count_obtaininfoconseq_namecodeexecution_vulnibm_iot)*100)/(count_obtaininfoconseq_vulnibm_sh+count_obtaininfoconseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE CODE EXECUTION  \n")
    print("            -    EN EL "+str(float(((count_obtaininfoconseq_namemaninthemiddle_vulnibm_sh+count_obtaininfoconseq_namemaninthemiddle_vulnibm_iot)*100)/(count_obtaininfoconseq_vulnibm_sh+count_obtaininfoconseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE MAN IN THE MIDDLE  \n")
    print("            -    EN EL "+str(float(((count_obtaininfoconseq_namesqlinjection_vulnibm_sh+count_obtaininfoconseq_namesqlinjection_vulnibm_iot)*100)/(count_obtaininfoconseq_vulnibm_sh+count_obtaininfoconseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE SQL INJECTION  \n")
    print("            -    EN EL "+str(float(((count_obtaininfoconseq_namecrosssiterequestforgery_vulnibm_sh+count_obtaininfoconseq_namecrosssiterequestforgery_vulnibm_iot)*100)/(count_obtaininfoconseq_vulnibm_sh+count_obtaininfoconseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE MODULE EXECUTION  \n")
    print("            -    EN EL "+str(float(((count_obtaininfoconseq_namemoduleexecution_vulnibm_sh+count_obtaininfoconseq_namemoduleexecution_vulnibm_iot)*100)/(count_obtaininfoconseq_vulnibm_sh+count_obtaininfoconseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE CROSS SITE REQUEST FORGERY  \n")
    print("            -    EN EL "+str(float(((count_obtaininfoconseq_namebufferoverflow_vulnibm_sh+count_obtaininfoconseq_namebufferoverflow_vulnibm_iot)*100)/(count_obtaininfoconseq_vulnibm_sh+count_obtaininfoconseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE BUFFER OVERFLOW \n")
    print("            -    EN EL "+str(float(((count_obtaininfoconseq_namecommandexecution_vulnibm_sh+count_obtaininfoconseq_namecommandexecution_vulnibm_iot)*100)/(count_obtaininfoconseq_vulnibm_sh+count_obtaininfoconseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE COMMAND EXECUTION  \n")
    print("            -    EN EL "+str(float(((count_obtaininfoconseq_namespoofing_vulnibm_sh+count_obtaininfoconseq_namespoofing_vulnibm_iot)*100)/(count_obtaininfoconseq_vulnibm_sh+count_obtaininfoconseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE SPOOFING  \n")
    print("            -    EN EL "+str(float(((count_obtaininfoconseq_nameclickjacking_vulnibm_sh+count_obtaininfoconseq_nameclickjacking_vulnibm_iot)*100)/(count_obtaininfoconseq_vulnibm_sh+count_obtaininfoconseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE CLICKJACKING  \n")
    print("            -    EN EL "+str(float(((count_obtaininfoconseq_namehijacking_vulnibm_sh+count_obtaininfoconseq_namehijacking_vulnibm_iot)*100)/(count_obtaininfoconseq_vulnibm_sh+count_obtaininfoconseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE HIJACKING  \n")
    print("            -    EN EL "+str(float(((count_obtaininfoconseq_namefileinclude_vulnibm_sh+count_obtaininfoconseq_namefileinclude_vulnibm_iot)*100)/(count_obtaininfoconseq_vulnibm_sh+count_obtaininfoconseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE FILE INCLUDE  \n")
    print("            -    EN EL "+str(float(((count_obtaininfoconseq_namebruteforce_vulnibm_sh+count_obtaininfoconseq_namebruteforce_vulnibm_iot)*100)/(count_obtaininfoconseq_vulnibm_sh+count_obtaininfoconseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE BRUTE FORCE  \n")
    print("            -    EN EL "+str(float(((count_obtaininfoconseq_namefileupload_vulnibm_sh+count_obtaininfoconseq_namefileupload_vulnibm_iot)*100)/(count_obtaininfoconseq_vulnibm_sh+count_obtaininfoconseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE FILE UPLOAD  \n")
    print("            -    EN EL "+str(float(((count_obtaininfoconseq_nameheaderinjection_vulnibm_sh+count_obtaininfoconseq_nameheaderinjection_vulnibm_iot)*100)/(count_obtaininfoconseq_vulnibm_sh+count_obtaininfoconseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE HEADER INJECTION \n")
    print("            -    EN EL "+str(float(((count_obtaininfoconseq_nametampering_vulnibm_sh+count_obtaininfoconseq_nametampering_vulnibm_iot)*100)/(count_obtaininfoconseq_vulnibm_sh+count_obtaininfoconseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE TAMPERING  \n")
    print("            -    EN EL "+str(float(((count_obtaininfoconseq_nameanother_vulnibm_sh+count_obtaininfoconseq_nameanother_vulnibm_iot)*100)/(count_obtaininfoconseq_vulnibm_sh+count_obtaininfoconseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE OTRO VALOR DISTINTO A LOS ANTERIORES  \n")
    print("\n") 

if((count_xss_conseq_vulnibm_sh+count_xss_conseq_vulnibm_iot)>0):
    print("      -    EN EL "+str(float((count_xss_conseq_vulnibm_sh+count_xss_conseq_vulnibm_iot)*100)/(count_conseq_vulnibm_sh+count_conseq_vulnibm_iot))+" % DE VULNERABILIDADES LA CONSECUENCIA ES CROSS-SITE SCRIPTING. EL NOMBRE VIENE ESPECIFICADO EN EL "+str(float(((count_xss_conseq_vulnibm_sh_specified+count_xss_conseq_vulnibm_iot_specified)*100)/(count_xss_conseq_vulnibm_sh+count_xss_conseq_vulnibm_iot)))+" % DE ELLAS. LOS PORCENTAJES DE VALOR DE NOMBRE SON LOS SIGUIENTES :  \n")
    print("            -    EN EL "+str(float(((count_xss_conseq_namepathtraversal_vulnibm_sh+count_xss_conseq_namepathtraversal_vulnibm_iot)*100)/(count_xss_conseq_vulnibm_sh+count_xss_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE PATH TRAVERSAL \n")
    print("            -    EN EL "+str(float(((count_xss_conseq_namedirectorytraversal_vulnibm_sh+count_xss_conseq_namedirectorytraversal_vulnibm_iot)*100)/(count_xss_conseq_vulnibm_sh+count_xss_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE DIRECTORY TRAVERSAL \n")
    print("            -    EN EL "+str(float(((count_xss_conseq_nameprivilegeescalation_vulnibm_sh+count_xss_conseq_nameprivilegeescalation_vulnibm_iot)*100)/(count_xss_conseq_vulnibm_sh+count_xss_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE PRIVILEGE ESCALATION \n") 
    print("            -    EN EL "+str(float(((count_xss_conseq_namecrosssitescripting_vulnibm_sh+count_xss_conseq_namecrosssitescripting_vulnibm_iot)*100)/(count_xss_conseq_vulnibm_sh+count_xss_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE CROSS-SITE SCRIPTING  \n")
    print("            -    EN EL "+str(float(((count_xss_conseq_namesecuritybypass_vulnibm_sh+count_xss_conseq_namesecuritybypass_vulnibm_iot)*100)/(count_xss_conseq_vulnibm_sh+count_xss_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE SECURITY BYPASS  \n")
    print("            -    EN EL "+str(float(((count_xss_conseq_namesinformationdisclosure_vulnibm_sh+count_xss_conseq_namesinformationdisclosure_vulnibm_iot)*100)/(count_xss_conseq_vulnibm_sh+count_xss_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE INFORMATION DISCLOSURE \n")
    print("            -    EN EL "+str(float(((count_xss_conseq_namedenialofservice_vulnibm_sh+count_xss_conseq_namedenialofservice_vulnibm_iot)*100)/(count_xss_conseq_vulnibm_sh+count_xss_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE DENIAL OF SERVICE  \n")
    print("            -    EN EL "+str(float(((count_xss_conseq_namecodeexecution_vulnibm_sh+count_xss_conseq_namecodeexecution_vulnibm_iot)*100)/(count_xss_conseq_vulnibm_sh+count_xss_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE CODE EXECUTION  \n")
    print("            -    EN EL "+str(float(((count_xss_conseq_namemaninthemiddle_vulnibm_sh+count_xss_conseq_namemaninthemiddle_vulnibm_iot)*100)/(count_xss_conseq_vulnibm_sh+count_xss_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE MAN IN THE MIDDLE  \n")
    print("            -    EN EL "+str(float(((count_xss_conseq_namesqlinjection_vulnibm_sh+count_xss_conseq_namesqlinjection_vulnibm_iot)*100)/(count_xss_conseq_vulnibm_sh+count_xss_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE SQL INJECTION  \n")
    print("            -    EN EL "+str(float(((count_xss_conseq_namecrosssiterequestforgery_vulnibm_sh+count_xss_conseq_namecrosssiterequestforgery_vulnibm_iot)*100)/(count_xss_conseq_vulnibm_sh+count_xss_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE MODULE EXECUTION  \n")
    print("            -    EN EL "+str(float(((count_xss_conseq_namemoduleexecution_vulnibm_sh+count_xss_conseq_namemoduleexecution_vulnibm_iot)*100)/(count_xss_conseq_vulnibm_sh+count_xss_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE CROSS SITE REQUEST FORGERY  \n")
    print("            -    EN EL "+str(float(((count_xss_conseq_namebufferoverflow_vulnibm_sh+count_xss_conseq_namebufferoverflow_vulnibm_iot)*100)/(count_xss_conseq_vulnibm_sh+count_xss_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE BUFFER OVERFLOW \n")
    print("            -    EN EL "+str(float(((count_xss_conseq_namecommandexecution_vulnibm_sh+count_xss_conseq_namecommandexecution_vulnibm_iot)*100)/(count_xss_conseq_vulnibm_sh+count_xss_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE COMMAND EXECUTION  \n")
    print("            -    EN EL "+str(float(((count_xss_conseq_namespoofing_vulnibm_sh+count_xss_conseq_namespoofing_vulnibm_iot)*100)/(count_xss_conseq_vulnibm_sh+count_xss_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE SPOOFING  \n")
    print("            -    EN EL "+str(float(((count_xss_conseq_nameclickjacking_vulnibm_sh+count_xss_conseq_nameclickjacking_vulnibm_iot)*100)/(count_xss_conseq_vulnibm_sh+count_xss_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE CLICKJACKING  \n")
    print("            -    EN EL "+str(float(((count_xss_conseq_namehijacking_vulnibm_sh+count_xss_conseq_namehijacking_vulnibm_iot)*100)/(count_xss_conseq_vulnibm_sh+count_xss_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE HIJACKING  \n")
    print("            -    EN EL "+str(float(((count_xss_conseq_namefileinclude_vulnibm_sh+count_xss_conseq_namefileinclude_vulnibm_iot)*100)/(count_xss_conseq_vulnibm_sh+count_xss_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE FILE INCLUDE  \n")
    print("            -    EN EL "+str(float(((count_xss_conseq_namebruteforce_vulnibm_sh+count_xss_conseq_namebruteforce_vulnibm_iot)*100)/(count_xss_conseq_vulnibm_sh+count_xss_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE BRUTE FORCE  \n")
    print("            -    EN EL "+str(float(((count_xss_conseq_namefileupload_vulnibm_sh+count_xss_conseq_namefileupload_vulnibm_iot)*100)/(count_xss_conseq_vulnibm_sh+count_xss_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE FILE UPLOAD  \n")
    print("            -    EN EL "+str(float(((count_xss_conseq_nameheaderinjection_vulnibm_sh+count_xss_conseq_nameheaderinjection_vulnibm_iot)*100)/(count_xss_conseq_vulnibm_sh+count_xss_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE HEADER INJECTION \n")
    print("            -    EN EL "+str(float(((count_xss_conseq_nametampering_vulnibm_sh+count_xss_conseq_nametampering_vulnibm_iot)*100)/(count_xss_conseq_vulnibm_sh+count_xss_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE TAMPERING  \n")
    print("            -    EN EL "+str(float(((count_xss_conseq_nameanother_vulnibm_sh+count_xss_conseq_nameanother_vulnibm_iot)*100)/(count_xss_conseq_vulnibm_sh+count_xss_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE OTRO VALOR DISTINTO A LOS ANTERIORES  \n")
    print("\n")
if((count_gainacc_conseq_vulnibm_sh+count_gainacc_conseq_vulnibm_iot)>0):
    print("      -    EN EL "+str(float((count_gainacc_conseq_vulnibm_sh+count_gainacc_conseq_vulnibm_iot)*100)/(count_conseq_vulnibm_sh+count_conseq_vulnibm_iot))+" % DE VULNERABILIDADES LA CONSECUENCIA ES LA OBTENCION DE ACCESO. EL NOMBRE VIENE ESPECIFICADO EN EL "+str(float(((count_gainacc_conseq_vulnibm_sh_specified+count_gainacc_conseq_vulnibm_iot_specified)*100)/(count_gainacc_conseq_vulnibm_sh+count_gainacc_conseq_vulnibm_iot)))+" % DE ELLAS. LOS PORCENTAJES DE VALOR DE NOMBRE SON LOS SIGUIENTES :  \n")
    print("            -    EN EL "+str(float(((count_gainacc_conseq_namepathtraversal_vulnibm_sh+count_gainacc_conseq_namepathtraversal_vulnibm_iot)*100)/(count_gainacc_conseq_vulnibm_sh+count_gainacc_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE PATH TRAVERSAL \n")
    print("            -    EN EL "+str(float(((count_gainacc_conseq_namedirectorytraversal_vulnibm_sh+count_gainacc_conseq_namedirectorytraversal_vulnibm_iot)*100)/(count_gainacc_conseq_vulnibm_sh+count_gainacc_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE DIRECTORY TRAVERSAL \n")
    print("            -    EN EL "+str(float(((count_gainacc_conseq_nameprivilegeescalation_vulnibm_sh+count_gainacc_conseq_nameprivilegeescalation_vulnibm_iot)*100)/(count_gainacc_conseq_vulnibm_sh+count_gainacc_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE PRIVILEGE ESCALATION \n") 
    print("            -    EN EL "+str(float(((count_gainacc_conseq_namecrosssitescripting_vulnibm_sh+count_gainacc_conseq_namecrosssitescripting_vulnibm_iot)*100)/(count_gainacc_conseq_vulnibm_sh+count_gainacc_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE CROSS-SITE SCRIPTING  \n")
    print("            -    EN EL "+str(float(((count_gainacc_conseq_namesecuritybypass_vulnibm_sh+count_gainacc_conseq_namesecuritybypass_vulnibm_iot)*100)/(count_gainacc_conseq_vulnibm_sh+count_gainacc_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE SECURITY BYPASS  \n")
    print("            -    EN EL "+str(float(((count_gainacc_conseq_namesinformationdisclosure_vulnibm_sh+count_gainacc_conseq_namesinformationdisclosure_vulnibm_iot)*100)/(count_gainacc_conseq_vulnibm_sh+count_gainacc_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE INFORMATION DISCLOSURE \n")
    print("            -    EN EL "+str(float(((count_gainacc_conseq_namedenialofservice_vulnibm_sh+count_gainacc_conseq_namedenialofservice_vulnibm_iot)*100)/(count_gainacc_conseq_vulnibm_sh+count_gainacc_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE DENIAL OF SERVICE  \n")
    print("            -    EN EL "+str(float(((count_gainacc_conseq_namecodeexecution_vulnibm_sh+count_gainacc_conseq_namecodeexecution_vulnibm_iot)*100)/(count_gainacc_conseq_vulnibm_sh+count_gainacc_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE CODE EXECUTION  \n")
    print("            -    EN EL "+str(float(((count_gainacc_conseq_namemaninthemiddle_vulnibm_sh+count_gainacc_conseq_namemaninthemiddle_vulnibm_iot)*100)/(count_gainacc_conseq_vulnibm_sh+count_gainacc_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE MAN IN THE MIDDLE  \n")
    print("            -    EN EL "+str(float(((count_gainacc_conseq_namesqlinjection_vulnibm_sh+count_gainacc_conseq_namesqlinjection_vulnibm_iot)*100)/(count_gainacc_conseq_vulnibm_sh+count_gainacc_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE SQL INJECTION  \n")
    print("            -    EN EL "+str(float(((count_gainacc_conseq_namecrosssiterequestforgery_vulnibm_sh+count_gainacc_conseq_namecrosssiterequestforgery_vulnibm_iot)*100)/(count_gainacc_conseq_vulnibm_sh+count_gainacc_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE MODULE EXECUTION  \n")
    print("            -    EN EL "+str(float(((count_gainacc_conseq_namemoduleexecution_vulnibm_sh+count_gainacc_conseq_namemoduleexecution_vulnibm_iot)*100)/(count_gainacc_conseq_vulnibm_sh+count_gainacc_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE CROSS SITE REQUEST FORGERY  \n")
    print("            -    EN EL "+str(float(((count_gainacc_conseq_namebufferoverflow_vulnibm_sh+count_gainacc_conseq_namebufferoverflow_vulnibm_iot)*100)/(count_gainacc_conseq_vulnibm_sh+count_gainacc_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE BUFFER OVERFLOW \n")
    print("            -    EN EL "+str(float(((count_gainacc_conseq_namecommandexecution_vulnibm_sh+count_gainacc_conseq_namecommandexecution_vulnibm_iot)*100)/(count_gainacc_conseq_vulnibm_sh+count_gainacc_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE COMMAND EXECUTION  \n")
    print("            -    EN EL "+str(float(((count_gainacc_conseq_namespoofing_vulnibm_sh+count_gainacc_conseq_namespoofing_vulnibm_iot)*100)/(count_gainacc_conseq_vulnibm_sh+count_gainacc_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE SPOOFING  \n")
    print("            -    EN EL "+str(float(((count_gainacc_conseq_nameclickjacking_vulnibm_sh+count_gainacc_conseq_nameclickjacking_vulnibm_iot)*100)/(count_gainacc_conseq_vulnibm_sh+count_gainacc_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE CLICKJACKING  \n")
    print("            -    EN EL "+str(float(((count_gainacc_conseq_namehijacking_vulnibm_sh+count_gainacc_conseq_namehijacking_vulnibm_iot)*100)/(count_gainacc_conseq_vulnibm_sh+count_gainacc_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE HIJACKING  \n")
    print("            -    EN EL "+str(float(((count_gainacc_conseq_namefileinclude_vulnibm_sh+count_gainacc_conseq_namefileinclude_vulnibm_iot)*100)/(count_gainacc_conseq_vulnibm_sh+count_gainacc_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE FILE INCLUDE  \n")
    print("            -    EN EL "+str(float(((count_gainacc_conseq_namebruteforce_vulnibm_sh+count_gainacc_conseq_namebruteforce_vulnibm_iot)*100)/(count_gainacc_conseq_vulnibm_sh+count_gainacc_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE BRUTE FORCE  \n")
    print("            -    EN EL "+str(float(((count_gainacc_conseq_namefileupload_vulnibm_sh+count_gainacc_conseq_namefileupload_vulnibm_iot)*100)/(count_gainacc_conseq_vulnibm_sh+count_gainacc_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE FILE UPLOAD  \n")
    print("            -    EN EL "+str(float(((count_gainacc_conseq_nameheaderinjection_vulnibm_sh+count_gainacc_conseq_nameheaderinjection_vulnibm_iot)*100)/(count_gainacc_conseq_vulnibm_sh+count_gainacc_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE HEADER INJECTION \n")
    print("            -    EN EL "+str(float(((count_gainacc_conseq_nametampering_vulnibm_sh+count_gainacc_conseq_nametampering_vulnibm_iot)*100)/(count_gainacc_conseq_vulnibm_sh+count_gainacc_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE TAMPERING  \n")
    print("            -    EN EL "+str(float(((count_gainacc_conseq_nameanother_vulnibm_sh+count_gainacc_conseq_nameanother_vulnibm_iot)*100)/(count_gainacc_conseq_vulnibm_sh+count_gainacc_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE OTRO VALOR DISTINTO A LOS ANTERIORES  \n")
    print("\n")
    
if((count_gainpriv_conseq_vulnibm_sh+count_gainpriv_conseq_vulnibm_iot)>0):
    print("      -    EN EL "+str(float((count_gainpriv_conseq_vulnibm_sh+count_gainpriv_conseq_vulnibm_iot)*100)/(count_conseq_vulnibm_sh+count_conseq_vulnibm_iot))+" % DE VULNERABILIDADES LA CONSECUENCIA ES LA OBTENCION DE PRIVILEGIOS. EL NOMBRE VIENE ESPECIFICADO EN EL "+str(float(((count_gainpriv_conseq_vulnibm_sh_specified+count_gainpriv_conseq_vulnibm_iot_specified)*100)/(count_gainpriv_conseq_vulnibm_sh+count_gainpriv_conseq_vulnibm_iot)))+" % DE ELLAS. LOS PORCENTAJES DE VALOR DE NOMBRE SON LOS SIGUIENTES :  \n")
    print("            -    EN EL "+str(float(((count_gainpriv_conseq_namepathtraversal_vulnibm_sh+count_gainpriv_conseq_namepathtraversal_vulnibm_iot)*100)/(count_gainpriv_conseq_vulnibm_sh+count_gainpriv_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE PATH TRAVERSAL \n")
    print("            -    EN EL "+str(float(((count_gainpriv_conseq_namedirectorytraversal_vulnibm_sh+count_gainpriv_conseq_namedirectorytraversal_vulnibm_iot)*100)/(count_gainpriv_conseq_vulnibm_sh+count_gainpriv_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE DIRECTORY TRAVERSAL \n")
    print("            -    EN EL "+str(float(((count_gainpriv_conseq_nameprivilegeescalation_vulnibm_sh+count_gainpriv_conseq_nameprivilegeescalation_vulnibm_iot)*100)/(count_gainpriv_conseq_vulnibm_sh+count_gainpriv_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE PRIVILEGE ESCALATION \n") 
    print("            -    EN EL "+str(float(((count_gainpriv_conseq_namecrosssitescripting_vulnibm_sh+count_gainpriv_conseq_namecrosssitescripting_vulnibm_iot)*100)/(count_gainpriv_conseq_vulnibm_sh+count_gainpriv_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE CROSS-SITE SCRIPTING  \n")
    print("            -    EN EL "+str(float(((count_gainpriv_conseq_namesecuritybypass_vulnibm_sh+count_gainpriv_conseq_namesecuritybypass_vulnibm_iot)*100)/(count_gainpriv_conseq_vulnibm_sh+count_gainpriv_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE SECURITY BYPASS  \n")
    print("            -    EN EL "+str(float(((count_gainpriv_conseq_namesinformationdisclosure_vulnibm_sh+count_gainpriv_conseq_namesinformationdisclosure_vulnibm_iot)*100)/(count_gainpriv_conseq_vulnibm_sh+count_gainpriv_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE INFORMATION DISCLOSURE \n")
    print("            -    EN EL "+str(float(((count_gainpriv_conseq_namedenialofservice_vulnibm_sh+count_gainpriv_conseq_namedenialofservice_vulnibm_iot)*100)/(count_gainpriv_conseq_vulnibm_sh+count_gainpriv_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE DENIAL OF SERVICE  \n")
    print("            -    EN EL "+str(float(((count_gainpriv_conseq_namecodeexecution_vulnibm_sh+count_gainpriv_conseq_namecodeexecution_vulnibm_iot)*100)/(count_gainpriv_conseq_vulnibm_sh+count_gainpriv_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE CODE EXECUTION  \n")
    print("            -    EN EL "+str(float(((count_gainpriv_conseq_namemaninthemiddle_vulnibm_sh+count_gainpriv_conseq_namemaninthemiddle_vulnibm_iot)*100)/(count_gainpriv_conseq_vulnibm_sh+count_gainpriv_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE MAN IN THE MIDDLE  \n")
    print("            -    EN EL "+str(float(((count_gainpriv_conseq_namesqlinjection_vulnibm_sh+count_gainpriv_conseq_namesqlinjection_vulnibm_iot)*100)/(count_gainpriv_conseq_vulnibm_sh+count_gainpriv_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE SQL INJECTION  \n")
    print("            -    EN EL "+str(float(((count_gainpriv_conseq_namecrosssiterequestforgery_vulnibm_sh+count_gainpriv_conseq_namecrosssiterequestforgery_vulnibm_iot)*100)/(count_gainpriv_conseq_vulnibm_sh+count_gainpriv_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE MODULE EXECUTION  \n")
    print("            -    EN EL "+str(float(((count_gainpriv_conseq_namemoduleexecution_vulnibm_sh+count_gainpriv_conseq_namemoduleexecution_vulnibm_iot)*100)/(count_gainpriv_conseq_vulnibm_sh+count_gainpriv_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE CROSS SITE REQUEST FORGERY  \n")
    print("            -    EN EL "+str(float(((count_gainpriv_conseq_namebufferoverflow_vulnibm_sh+count_gainpriv_conseq_namebufferoverflow_vulnibm_iot)*100)/(count_gainpriv_conseq_vulnibm_sh+count_gainpriv_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE BUFFER OVERFLOW \n")
    print("            -    EN EL "+str(float(((count_gainpriv_conseq_namecommandexecution_vulnibm_sh+count_gainpriv_conseq_namecommandexecution_vulnibm_iot)*100)/(count_gainpriv_conseq_vulnibm_sh+count_gainpriv_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE COMMAND EXECUTION  \n")
    print("            -    EN EL "+str(float(((count_gainpriv_conseq_namespoofing_vulnibm_sh+count_gainpriv_conseq_namespoofing_vulnibm_iot)*100)/(count_gainpriv_conseq_vulnibm_sh+count_gainpriv_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE SPOOFING  \n")
    print("            -    EN EL "+str(float(((count_gainpriv_conseq_nameclickjacking_vulnibm_sh+count_gainpriv_conseq_nameclickjacking_vulnibm_iot)*100)/(count_gainpriv_conseq_vulnibm_sh+count_gainpriv_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE CLICKJACKING  \n")
    print("            -    EN EL "+str(float(((count_gainpriv_conseq_namehijacking_vulnibm_sh+count_gainpriv_conseq_namehijacking_vulnibm_iot)*100)/(count_gainpriv_conseq_vulnibm_sh+count_gainpriv_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE HIJACKING  \n")
    print("            -    EN EL "+str(float(((count_gainpriv_conseq_namefileinclude_vulnibm_sh+count_gainpriv_conseq_namefileinclude_vulnibm_iot)*100)/(count_gainpriv_conseq_vulnibm_sh+count_gainpriv_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE FILE INCLUDE  \n")
    print("            -    EN EL "+str(float(((count_gainpriv_conseq_namebruteforce_vulnibm_sh+count_gainpriv_conseq_namebruteforce_vulnibm_iot)*100)/(count_gainpriv_conseq_vulnibm_sh+count_gainpriv_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE BRUTE FORCE  \n")
    print("            -    EN EL "+str(float(((count_gainpriv_conseq_namefileupload_vulnibm_sh+count_gainpriv_conseq_namefileupload_vulnibm_iot)*100)/(count_gainpriv_conseq_vulnibm_sh+count_gainpriv_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE FILE UPLOAD  \n")
    print("            -    EN EL "+str(float(((count_gainpriv_conseq_nameheaderinjection_vulnibm_sh+count_gainpriv_conseq_nameheaderinjection_vulnibm_iot)*100)/(count_gainpriv_conseq_vulnibm_sh+count_gainpriv_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE HEADER INJECTION \n")
    print("            -    EN EL "+str(float(((count_gainpriv_conseq_nametampering_vulnibm_sh+count_gainpriv_conseq_nametampering_vulnibm_iot)*100)/(count_gainpriv_conseq_vulnibm_sh+count_gainpriv_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE TAMPERING  \n")
    print("            -    EN EL "+str(float(((count_gainpriv_conseq_nameanother_vulnibm_sh+count_gainpriv_conseq_nameanother_vulnibm_iot)*100)/(count_gainpriv_conseq_vulnibm_sh+count_gainpriv_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE OTRO VALOR DISTINTO A LOS ANTERIORES  \n")
    print("\n")
    

if((count_denialofserv_conseq_vulnibm_sh+count_denialofserv_conseq_vulnibm_iot)>0):
    print("      -    EN EL "+str(float((count_denialofserv_conseq_vulnibm_sh+count_denialofserv_conseq_vulnibm_iot)*100)/(count_conseq_vulnibm_sh+count_conseq_vulnibm_iot))+" % DE VULNERABILIDADES LA CONSECUENCIA ES UNA DENEGACION DE SERVICIO. EL NOMBRE VIENE ESPECIFICADO EN EL "+str(float(((count_denialofserv_conseq_vulnibm_sh_specified+count_denialofserv_conseq_vulnibm_iot_specified)*100)/(count_denialofserv_conseq_vulnibm_sh+count_denialofserv_conseq_vulnibm_iot)))+" % DE ELLAS. LOS PORCENTAJES DE VALOR DE NOMBRE SON LOS SIGUIENTES :  \n")
    print("            -    EN EL "+str(float(((count_denialofserv_conseq_namepathtraversal_vulnibm_sh+count_denialofserv_conseq_namepathtraversal_vulnibm_iot)*100)/(count_denialofserv_conseq_vulnibm_sh+count_denialofserv_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE PATH TRAVERSAL \n")
    print("            -    EN EL "+str(float(((count_denialofserv_conseq_namedirectorytraversal_vulnibm_sh+count_denialofserv_conseq_namedirectorytraversal_vulnibm_iot)*100)/(count_denialofserv_conseq_vulnibm_sh+count_denialofserv_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE DIRECTORY TRAVERSAL \n")
    print("            -    EN EL "+str(float(((count_denialofserv_conseq_nameprivilegeescalation_vulnibm_sh+count_denialofserv_conseq_nameprivilegeescalation_vulnibm_iot)*100)/(count_denialofserv_conseq_vulnibm_sh+count_denialofserv_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE PRIVILEGE ESCALATION \n") 
    print("            -    EN EL "+str(float(((count_denialofserv_conseq_namecrosssitescripting_vulnibm_sh+count_denialofserv_conseq_namecrosssitescripting_vulnibm_iot)*100)/(count_denialofserv_conseq_vulnibm_sh+count_denialofserv_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE CROSS-SITE SCRIPTING  \n")
    print("            -    EN EL "+str(float(((count_denialofserv_conseq_namesecuritybypass_vulnibm_sh+count_denialofserv_conseq_namesecuritybypass_vulnibm_iot)*100)/(count_denialofserv_conseq_vulnibm_sh+count_denialofserv_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE SECURITY BYPASS  \n")
    print("            -    EN EL "+str(float(((count_denialofserv_conseq_namesinformationdisclosure_vulnibm_sh+count_denialofserv_conseq_namesinformationdisclosure_vulnibm_iot)*100)/(count_denialofserv_conseq_vulnibm_sh+count_denialofserv_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE INFORMATION DISCLOSURE \n")
    print("            -    EN EL "+str(float(((count_denialofserv_conseq_namedenialofservice_vulnibm_sh+count_denialofserv_conseq_namedenialofservice_vulnibm_iot)*100)/(count_denialofserv_conseq_vulnibm_sh+count_denialofserv_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE DENIAL OF SERVICE  \n")
    print("            -    EN EL "+str(float(((count_denialofserv_conseq_namecodeexecution_vulnibm_sh+count_denialofserv_conseq_namecodeexecution_vulnibm_iot)*100)/(count_denialofserv_conseq_vulnibm_sh+count_denialofserv_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE CODE EXECUTION  \n")
    print("            -    EN EL "+str(float(((count_denialofserv_conseq_namemaninthemiddle_vulnibm_sh+count_denialofserv_conseq_namemaninthemiddle_vulnibm_iot)*100)/(count_denialofserv_conseq_vulnibm_sh+count_denialofserv_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE MAN IN THE MIDDLE  \n")
    print("            -    EN EL "+str(float(((count_denialofserv_conseq_namesqlinjection_vulnibm_sh+count_denialofserv_conseq_namesqlinjection_vulnibm_iot)*100)/(count_denialofserv_conseq_vulnibm_sh+count_denialofserv_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE SQL INJECTION  \n")
    print("            -    EN EL "+str(float(((count_denialofserv_conseq_namecrosssiterequestforgery_vulnibm_sh+count_denialofserv_conseq_namecrosssiterequestforgery_vulnibm_iot)*100)/(count_denialofserv_conseq_vulnibm_sh+count_denialofserv_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE MODULE EXECUTION  \n")
    print("            -    EN EL "+str(float(((count_denialofserv_conseq_namemoduleexecution_vulnibm_sh+count_denialofserv_conseq_namemoduleexecution_vulnibm_iot)*100)/(count_denialofserv_conseq_vulnibm_sh+count_denialofserv_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE CROSS SITE REQUEST FORGERY  \n")
    print("            -    EN EL "+str(float(((count_denialofserv_conseq_namebufferoverflow_vulnibm_sh+count_denialofserv_conseq_namebufferoverflow_vulnibm_iot)*100)/(count_denialofserv_conseq_vulnibm_sh+count_denialofserv_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE BUFFER OVERFLOW \n")
    print("            -    EN EL "+str(float(((count_denialofserv_conseq_namecommandexecution_vulnibm_sh+count_denialofserv_conseq_namecommandexecution_vulnibm_iot)*100)/(count_denialofserv_conseq_vulnibm_sh+count_denialofserv_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE COMMAND EXECUTION  \n")
    print("            -    EN EL "+str(float(((count_denialofserv_conseq_namespoofing_vulnibm_sh+count_denialofserv_conseq_namespoofing_vulnibm_iot)*100)/(count_denialofserv_conseq_vulnibm_sh+count_denialofserv_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE SPOOFING  \n")
    print("            -    EN EL "+str(float(((count_denialofserv_conseq_nameclickjacking_vulnibm_sh+count_denialofserv_conseq_nameclickjacking_vulnibm_iot)*100)/(count_denialofserv_conseq_vulnibm_sh+count_denialofserv_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE CLICKJACKING  \n")
    print("            -    EN EL "+str(float(((count_denialofserv_conseq_namehijacking_vulnibm_sh+count_denialofserv_conseq_namehijacking_vulnibm_iot)*100)/(count_denialofserv_conseq_vulnibm_sh+count_denialofserv_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE HIJACKING  \n")
    print("            -    EN EL "+str(float(((count_denialofserv_conseq_namefileinclude_vulnibm_sh+count_denialofserv_conseq_namefileinclude_vulnibm_iot)*100)/(count_denialofserv_conseq_vulnibm_sh+count_denialofserv_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE FILE INCLUDE  \n")
    print("            -    EN EL "+str(float(((count_denialofserv_conseq_namebruteforce_vulnibm_sh+count_denialofserv_conseq_namebruteforce_vulnibm_iot)*100)/(count_denialofserv_conseq_vulnibm_sh+count_denialofserv_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE BRUTE FORCE  \n")
    print("            -    EN EL "+str(float(((count_denialofserv_conseq_namefileupload_vulnibm_sh+count_denialofserv_conseq_namefileupload_vulnibm_iot)*100)/(count_denialofserv_conseq_vulnibm_sh+count_denialofserv_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE FILE UPLOAD  \n")
    print("            -    EN EL "+str(float(((count_denialofserv_conseq_nameheaderinjection_vulnibm_sh+count_denialofserv_conseq_nameheaderinjection_vulnibm_iot)*100)/(count_denialofserv_conseq_vulnibm_sh+count_denialofserv_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE HEADER INJECTION \n")
    print("            -    EN EL "+str(float(((count_denialofserv_conseq_nametampering_vulnibm_sh+count_denialofserv_conseq_nametampering_vulnibm_iot)*100)/(count_denialofserv_conseq_vulnibm_sh+count_denialofserv_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE TAMPERING  \n")
    print("            -    EN EL "+str(float(((count_denialofserv_conseq_nameanother_vulnibm_sh+count_denialofserv_conseq_nameanother_vulnibm_iot)*100)/(count_denialofserv_conseq_vulnibm_sh+count_denialofserv_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE OTRO VALOR DISTINTO A LOS ANTERIORES  \n")
    print("\n")
    
if((count_bypassec_conseq_vulnibm_sh+count_bypassec_conseq_vulnibm_iot)>0):
    print("      -    EN EL "+str(float((count_bypassec_conseq_vulnibm_sh+count_bypassec_conseq_vulnibm_iot)*100)/(count_conseq_vulnibm_sh+count_conseq_vulnibm_iot))+" % DE VULNERABILIDADES LA CONSECUENCIA ES SOBREPASAR LA SEGURIDAD. EL NOMBRE VIENE ESPECIFICADO EN EL "+str(float(((count_bypassec_conseq_vulnibm_sh_specified+count_bypassec_conseq_vulnibm_iot_specified)*100)/(count_bypassec_conseq_vulnibm_sh+count_bypassec_conseq_vulnibm_iot)))+" % DE ELLAS. LOS PORCENTAJES DE VALOR DE NOMBRE SON LOS SIGUIENTES :  \n")
    print("            -    EN EL "+str(float(((count_bypassec_conseq_namepathtraversal_vulnibm_sh+count_bypassec_conseq_namepathtraversal_vulnibm_iot)*100)/(count_bypassec_conseq_vulnibm_sh+count_bypassec_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE PATH TRAVERSAL \n")
    print("            -    EN EL "+str(float(((count_bypassec_conseq_namedirectorytraversal_vulnibm_sh+count_bypassec_conseq_namedirectorytraversal_vulnibm_iot)*100)/(count_bypassec_conseq_vulnibm_sh+count_bypassec_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE DIRECTORY TRAVERSAL \n")
    print("            -    EN EL "+str(float(((count_bypassec_conseq_nameprivilegeescalation_vulnibm_sh+count_bypassec_conseq_nameprivilegeescalation_vulnibm_iot)*100)/(count_bypassec_conseq_vulnibm_sh+count_bypassec_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE PRIVILEGE ESCALATION \n") 
    print("            -    EN EL "+str(float(((count_bypassec_conseq_namecrosssitescripting_vulnibm_sh+count_bypassec_conseq_namecrosssitescripting_vulnibm_iot)*100)/(count_bypassec_conseq_vulnibm_sh+count_bypassec_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE CROSS-SITE SCRIPTING  \n")
    print("            -    EN EL "+str(float(((count_bypassec_conseq_namesecuritybypass_vulnibm_sh+count_bypassec_conseq_namesecuritybypass_vulnibm_iot)*100)/(count_bypassec_conseq_vulnibm_sh+count_bypassec_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE SECURITY BYPASS  \n")
    print("            -    EN EL "+str(float(((count_bypassec_conseq_namesinformationdisclosure_vulnibm_sh+count_bypassec_conseq_namesinformationdisclosure_vulnibm_iot)*100)/(count_bypassec_conseq_vulnibm_sh+count_bypassec_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE INFORMATION DISCLOSURE \n")
    print("            -    EN EL "+str(float(((count_bypassec_conseq_namedenialofservice_vulnibm_sh+count_bypassec_conseq_namedenialofservice_vulnibm_iot)*100)/(count_bypassec_conseq_vulnibm_sh+count_bypassec_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE DENIAL OF SERVICE  \n")
    print("            -    EN EL "+str(float(((count_bypassec_conseq_namecodeexecution_vulnibm_sh+count_bypassec_conseq_namecodeexecution_vulnibm_iot)*100)/(count_bypassec_conseq_vulnibm_sh+count_bypassec_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE CODE EXECUTION  \n")
    print("            -    EN EL "+str(float(((count_bypassec_conseq_namemaninthemiddle_vulnibm_sh+count_bypassec_conseq_namemaninthemiddle_vulnibm_iot)*100)/(count_bypassec_conseq_vulnibm_sh+count_bypassec_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE MAN IN THE MIDDLE  \n")
    print("            -    EN EL "+str(float(((count_bypassec_conseq_namesqlinjection_vulnibm_sh+count_bypassec_conseq_namesqlinjection_vulnibm_iot)*100)/(count_bypassec_conseq_vulnibm_sh+count_bypassec_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE SQL INJECTION  \n")
    print("            -    EN EL "+str(float(((count_bypassec_conseq_namecrosssiterequestforgery_vulnibm_sh+count_bypassec_conseq_namecrosssiterequestforgery_vulnibm_iot)*100)/(count_bypassec_conseq_vulnibm_sh+count_bypassec_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE MODULE EXECUTION  \n")
    print("            -    EN EL "+str(float(((count_bypassec_conseq_namemoduleexecution_vulnibm_sh+count_bypassec_conseq_namemoduleexecution_vulnibm_iot)*100)/(count_bypassec_conseq_vulnibm_sh+count_bypassec_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE CROSS SITE REQUEST FORGERY  \n")
    print("            -    EN EL "+str(float(((count_bypassec_conseq_namebufferoverflow_vulnibm_sh+count_bypassec_conseq_namebufferoverflow_vulnibm_iot)*100)/(count_bypassec_conseq_vulnibm_sh+count_bypassec_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE BUFFER OVERFLOW \n")
    print("            -    EN EL "+str(float(((count_bypassec_conseq_namecommandexecution_vulnibm_sh+count_bypassec_conseq_namecommandexecution_vulnibm_iot)*100)/(count_bypassec_conseq_vulnibm_sh+count_bypassec_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE COMMAND EXECUTION  \n")
    print("            -    EN EL "+str(float(((count_bypassec_conseq_namespoofing_vulnibm_sh+count_bypassec_conseq_namespoofing_vulnibm_iot)*100)/(count_bypassec_conseq_vulnibm_sh+count_bypassec_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE SPOOFING  \n")
    print("            -    EN EL "+str(float(((count_bypassec_conseq_nameclickjacking_vulnibm_sh+count_bypassec_conseq_nameclickjacking_vulnibm_iot)*100)/(count_bypassec_conseq_vulnibm_sh+count_bypassec_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE CLICKJACKING  \n")
    print("            -    EN EL "+str(float(((count_bypassec_conseq_namehijacking_vulnibm_sh+count_bypassec_conseq_namehijacking_vulnibm_iot)*100)/(count_bypassec_conseq_vulnibm_sh+count_bypassec_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE HIJACKING  \n")
    print("            -    EN EL "+str(float(((count_bypassec_conseq_namefileinclude_vulnibm_sh+count_bypassec_conseq_namefileinclude_vulnibm_iot)*100)/(count_bypassec_conseq_vulnibm_sh+count_bypassec_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE FILE INCLUDE  \n")
    print("            -    EN EL "+str(float(((count_bypassec_conseq_namebruteforce_vulnibm_sh+count_bypassec_conseq_namebruteforce_vulnibm_iot)*100)/(count_bypassec_conseq_vulnibm_sh+count_bypassec_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE BRUTE FORCE  \n")
    print("            -    EN EL "+str(float(((count_bypassec_conseq_namefileupload_vulnibm_sh+count_bypassec_conseq_namefileupload_vulnibm_iot)*100)/(count_bypassec_conseq_vulnibm_sh+count_bypassec_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE FILE UPLOAD  \n")
    print("            -    EN EL "+str(float(((count_bypassec_conseq_nameheaderinjection_vulnibm_sh+count_bypassec_conseq_nameheaderinjection_vulnibm_iot)*100)/(count_bypassec_conseq_vulnibm_sh+count_bypassec_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE HEADER INJECTION \n")
    print("            -    EN EL "+str(float(((count_bypassec_conseq_nametampering_vulnibm_sh+count_bypassec_conseq_nametampering_vulnibm_iot)*100)/(count_bypassec_conseq_vulnibm_sh+count_bypassec_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE TAMPERING  \n")
    print("            -    EN EL "+str(float(((count_bypassec_conseq_nameanother_vulnibm_sh+count_bypassec_conseq_nameanother_vulnibm_iot)*100)/(count_bypassec_conseq_vulnibm_sh+count_bypassec_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE OTRO VALOR DISTINTO A LOS ANTERIORES  \n")
    print("\n")
    
if((count_filemani_conseq_vulnibm_sh+count_filemani_conseq_vulnibm_iot)>0):
    print("      -    EN EL "+str(float((count_filemani_conseq_vulnibm_sh+count_filemani_conseq_vulnibm_iot)*100)/(count_conseq_vulnibm_sh+count_conseq_vulnibm_iot))+" % DE VULNERABILIDADES LA CONSECUENCIA ES LA MANIPULACION DE FICHEROS. EL NOMBRE VIENE ESPECIFICADO EN EL "+str(float(((count_filemani_conseq_vulnibm_sh_specified+count_filemani_conseq_vulnibm_iot_specified)*100)/(count_filemani_conseq_vulnibm_sh+count_filemani_conseq_vulnibm_iot)))+" % DE ELLAS. LOS PORCENTAJES DE VALOR DE NOMBRE SON LOS SIGUIENTES :  \n")
    print("            -    EN EL "+str(float(((count_filemani_conseq_namepathtraversal_vulnibm_sh+count_filemani_conseq_namepathtraversal_vulnibm_iot)*100)/(count_filemani_conseq_vulnibm_sh+count_filemani_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE PATH TRAVERSAL \n")
    print("            -    EN EL "+str(float(((count_filemani_conseq_namedirectorytraversal_vulnibm_sh+count_filemani_conseq_namedirectorytraversal_vulnibm_iot)*100)/(count_filemani_conseq_vulnibm_sh+count_filemani_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE DIRECTORY TRAVERSAL \n")
    print("            -    EN EL "+str(float(((count_filemani_conseq_nameprivilegeescalation_vulnibm_sh+count_filemani_conseq_nameprivilegeescalation_vulnibm_iot)*100)/(count_filemani_conseq_vulnibm_sh+count_filemani_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE PRIVILEGE ESCALATION \n") 
    print("            -    EN EL "+str(float(((count_filemani_conseq_namecrosssitescripting_vulnibm_sh+count_filemani_conseq_namecrosssitescripting_vulnibm_iot)*100)/(count_filemani_conseq_vulnibm_sh+count_filemani_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE CROSS-SITE SCRIPTING  \n")
    print("            -    EN EL "+str(float(((count_filemani_conseq_namesecuritybypass_vulnibm_sh+count_filemani_conseq_namesecuritybypass_vulnibm_iot)*100)/(count_filemani_conseq_vulnibm_sh+count_filemani_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE SECURITY BYPASS  \n")
    print("            -    EN EL "+str(float(((count_filemani_conseq_namesinformationdisclosure_vulnibm_sh+count_filemani_conseq_namesinformationdisclosure_vulnibm_iot)*100)/(count_filemani_conseq_vulnibm_sh+count_filemani_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE INFORMATION DISCLOSURE \n")
    print("            -    EN EL "+str(float(((count_filemani_conseq_namedenialofservice_vulnibm_sh+count_filemani_conseq_namedenialofservice_vulnibm_iot)*100)/(count_filemani_conseq_vulnibm_sh+count_filemani_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE DENIAL OF SERVICE  \n")
    print("            -    EN EL "+str(float(((count_filemani_conseq_namecodeexecution_vulnibm_sh+count_filemani_conseq_namecodeexecution_vulnibm_iot)*100)/(count_filemani_conseq_vulnibm_sh+count_filemani_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE CODE EXECUTION  \n")
    print("            -    EN EL "+str(float(((count_filemani_conseq_namemaninthemiddle_vulnibm_sh+count_filemani_conseq_namemaninthemiddle_vulnibm_iot)*100)/(count_filemani_conseq_vulnibm_sh+count_filemani_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE MAN IN THE MIDDLE  \n")
    print("            -    EN EL "+str(float(((count_filemani_conseq_namesqlinjection_vulnibm_sh+count_filemani_conseq_namesqlinjection_vulnibm_iot)*100)/(count_filemani_conseq_vulnibm_sh+count_filemani_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE SQL INJECTION  \n")
    print("            -    EN EL "+str(float(((count_filemani_conseq_namecrosssiterequestforgery_vulnibm_sh+count_filemani_conseq_namecrosssiterequestforgery_vulnibm_iot)*100)/(count_filemani_conseq_vulnibm_sh+count_filemani_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE MODULE EXECUTION  \n")
    print("            -    EN EL "+str(float(((count_filemani_conseq_namemoduleexecution_vulnibm_sh+count_filemani_conseq_namemoduleexecution_vulnibm_iot)*100)/(count_filemani_conseq_vulnibm_sh+count_filemani_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE CROSS SITE REQUEST FORGERY  \n")
    print("            -    EN EL "+str(float(((count_filemani_conseq_namebufferoverflow_vulnibm_sh+count_filemani_conseq_namebufferoverflow_vulnibm_iot)*100)/(count_filemani_conseq_vulnibm_sh+count_filemani_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE BUFFER OVERFLOW \n")
    print("            -    EN EL "+str(float(((count_filemani_conseq_namecommandexecution_vulnibm_sh+count_filemani_conseq_namecommandexecution_vulnibm_iot)*100)/(count_filemani_conseq_vulnibm_sh+count_filemani_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE COMMAND EXECUTION  \n")
    print("            -    EN EL "+str(float(((count_filemani_conseq_namespoofing_vulnibm_sh+count_filemani_conseq_namespoofing_vulnibm_iot)*100)/(count_filemani_conseq_vulnibm_sh+count_filemani_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE SPOOFING  \n")
    print("            -    EN EL "+str(float(((count_filemani_conseq_nameclickjacking_vulnibm_sh+count_filemani_conseq_nameclickjacking_vulnibm_iot)*100)/(count_filemani_conseq_vulnibm_sh+count_filemani_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE CLICKJACKING  \n")
    print("            -    EN EL "+str(float(((count_filemani_conseq_namehijacking_vulnibm_sh+count_filemani_conseq_namehijacking_vulnibm_iot)*100)/(count_filemani_conseq_vulnibm_sh+count_filemani_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE HIJACKING  \n")
    print("            -    EN EL "+str(float(((count_filemani_conseq_namefileinclude_vulnibm_sh+count_filemani_conseq_namefileinclude_vulnibm_iot)*100)/(count_filemani_conseq_vulnibm_sh+count_filemani_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE FILE INCLUDE  \n")
    print("            -    EN EL "+str(float(((count_filemani_conseq_namebruteforce_vulnibm_sh+count_filemani_conseq_namebruteforce_vulnibm_iot)*100)/(count_filemani_conseq_vulnibm_sh+count_filemani_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE BRUTE FORCE  \n")
    print("            -    EN EL "+str(float(((count_filemani_conseq_namefileupload_vulnibm_sh+count_filemani_conseq_namefileupload_vulnibm_iot)*100)/(count_filemani_conseq_vulnibm_sh+count_filemani_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE FILE UPLOAD  \n")
    print("            -    EN EL "+str(float(((count_filemani_conseq_nameheaderinjection_vulnibm_sh+count_filemani_conseq_nameheaderinjection_vulnibm_iot)*100)/(count_filemani_conseq_vulnibm_sh+count_filemani_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE HEADER INJECTION \n")
    print("            -    EN EL "+str(float(((count_filemani_conseq_nametampering_vulnibm_sh+count_filemani_conseq_nametampering_vulnibm_iot)*100)/(count_filemani_conseq_vulnibm_sh+count_filemani_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE TAMPERING  \n")
    print("            -    EN EL "+str(float(((count_filemani_conseq_nameanother_vulnibm_sh+count_filemani_conseq_nameanother_vulnibm_iot)*100)/(count_filemani_conseq_vulnibm_sh+count_filemani_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE OTRO VALOR DISTINTO A LOS ANTERIORES  \n")
    print("\n")
    
if((count_other_conseq_vulnibm_sh+count_other_conseq_vulnibm_iot)>0):
    print("      -    EN EL "+str(float((count_other_conseq_vulnibm_sh+count_other_conseq_vulnibm_iot)*100)/(count_conseq_vulnibm_sh+count_conseq_vulnibm_iot))+" % DE VULNERABILIDADES LA CONSECUENCIA ES OTRA DISTINTA A LAS ANTERIORES. EL NOMBRE VIENE ESPECIFICADO EN EL "+str(float(((count_other_conseq_vulnibm_sh_specified+count_other_conseq_vulnibm_iot_specified)*100)/(count_other_conseq_vulnibm_sh+count_other_conseq_vulnibm_iot)))+" % DE ELLAS. LOS PORCENTAJES DE VALOR DE NOMBRE SON LOS SIGUIENTES :  \n")
    print("            -    EN EL "+str(float(((count_other_conseq_namepathtraversal_vulnibm_sh+count_other_conseq_namepathtraversal_vulnibm_iot)*100)/(count_other_conseq_vulnibm_sh+count_other_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE PATH TRAVERSAL \n")
    print("            -    EN EL "+str(float(((count_other_conseq_namedirectorytraversal_vulnibm_sh+count_other_conseq_namedirectorytraversal_vulnibm_iot)*100)/(count_other_conseq_vulnibm_sh+count_other_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE DIRECTORY TRAVERSAL \n")
    print("            -    EN EL "+str(float(((count_other_conseq_nameprivilegeescalation_vulnibm_sh+count_other_conseq_nameprivilegeescalation_vulnibm_iot)*100)/(count_other_conseq_vulnibm_sh+count_other_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE PRIVILEGE ESCALATION \n") 
    print("            -    EN EL "+str(float(((count_other_conseq_namecrosssitescripting_vulnibm_sh+count_other_conseq_namecrosssitescripting_vulnibm_iot)*100)/(count_other_conseq_vulnibm_sh+count_other_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE CROSS-SITE SCRIPTING  \n")
    print("            -    EN EL "+str(float(((count_other_conseq_namesecuritybypass_vulnibm_sh+count_other_conseq_namesecuritybypass_vulnibm_iot)*100)/(count_other_conseq_vulnibm_sh+count_other_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE SECURITY BYPASS  \n")
    print("            -    EN EL "+str(float(((count_other_conseq_namesinformationdisclosure_vulnibm_sh+count_other_conseq_namesinformationdisclosure_vulnibm_iot)*100)/(count_other_conseq_vulnibm_sh+count_other_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE INFORMATION DISCLOSURE \n")
    print("            -    EN EL "+str(float(((count_other_conseq_namedenialofservice_vulnibm_sh+count_other_conseq_namedenialofservice_vulnibm_iot)*100)/(count_other_conseq_vulnibm_sh+count_other_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE DENIAL OF SERVICE  \n")
    print("            -    EN EL "+str(float(((count_other_conseq_namecodeexecution_vulnibm_sh+count_other_conseq_namecodeexecution_vulnibm_iot)*100)/(count_other_conseq_vulnibm_sh+count_other_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE CODE EXECUTION  \n")
    print("            -    EN EL "+str(float(((count_other_conseq_namemaninthemiddle_vulnibm_sh+count_other_conseq_namemaninthemiddle_vulnibm_iot)*100)/(count_other_conseq_vulnibm_sh+count_other_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE MAN IN THE MIDDLE  \n")
    print("            -    EN EL "+str(float(((count_other_conseq_namesqlinjection_vulnibm_sh+count_other_conseq_namesqlinjection_vulnibm_iot)*100)/(count_other_conseq_vulnibm_sh+count_other_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE SQL INJECTION  \n")
    print("            -    EN EL "+str(float(((count_other_conseq_namecrosssiterequestforgery_vulnibm_sh+count_other_conseq_namecrosssiterequestforgery_vulnibm_iot)*100)/(count_other_conseq_vulnibm_sh+count_other_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE MODULE EXECUTION  \n")
    print("            -    EN EL "+str(float(((count_other_conseq_namemoduleexecution_vulnibm_sh+count_other_conseq_namemoduleexecution_vulnibm_iot)*100)/(count_other_conseq_vulnibm_sh+count_other_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE CROSS SITE REQUEST FORGERY  \n")
    print("            -    EN EL "+str(float(((count_other_conseq_namebufferoverflow_vulnibm_sh+count_other_conseq_namebufferoverflow_vulnibm_iot)*100)/(count_other_conseq_vulnibm_sh+count_other_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE BUFFER OVERFLOW \n")
    print("            -    EN EL "+str(float(((count_other_conseq_namecommandexecution_vulnibm_sh+count_other_conseq_namecommandexecution_vulnibm_iot)*100)/(count_other_conseq_vulnibm_sh+count_other_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE COMMAND EXECUTION  \n")
    print("            -    EN EL "+str(float(((count_other_conseq_namespoofing_vulnibm_sh+count_other_conseq_namespoofing_vulnibm_iot)*100)/(count_other_conseq_vulnibm_sh+count_other_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE SPOOFING  \n")
    print("            -    EN EL "+str(float(((count_other_conseq_nameclickjacking_vulnibm_sh+count_other_conseq_nameclickjacking_vulnibm_iot)*100)/(count_other_conseq_vulnibm_sh+count_other_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE CLICKJACKING  \n")
    print("            -    EN EL "+str(float(((count_other_conseq_namehijacking_vulnibm_sh+count_other_conseq_namehijacking_vulnibm_iot)*100)/(count_other_conseq_vulnibm_sh+count_other_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE HIJACKING  \n")
    print("            -    EN EL "+str(float(((count_other_conseq_namefileinclude_vulnibm_sh+count_other_conseq_namefileinclude_vulnibm_iot)*100)/(count_other_conseq_vulnibm_sh+count_other_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE FILE INCLUDE  \n")
    print("            -    EN EL "+str(float(((count_other_conseq_namebruteforce_vulnibm_sh+count_other_conseq_namebruteforce_vulnibm_iot)*100)/(count_other_conseq_vulnibm_sh+count_other_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE BRUTE FORCE  \n")
    print("            -    EN EL "+str(float(((count_other_conseq_namefileupload_vulnibm_sh+count_other_conseq_namefileupload_vulnibm_iot)*100)/(count_other_conseq_vulnibm_sh+count_other_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE FILE UPLOAD  \n")
    print("            -    EN EL "+str(float(((count_other_conseq_nameheaderinjection_vulnibm_sh+count_other_conseq_nameheaderinjection_vulnibm_iot)*100)/(count_other_conseq_vulnibm_sh+count_other_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE HEADER INJECTION \n")
    print("            -    EN EL "+str(float(((count_other_conseq_nametampering_vulnibm_sh+count_other_conseq_nametampering_vulnibm_iot)*100)/(count_other_conseq_vulnibm_sh+count_other_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE TAMPERING  \n")
    print("            -    EN EL "+str(float(((count_other_conseq_nameanother_vulnibm_sh+count_other_conseq_nameanother_vulnibm_iot)*100)/(count_other_conseq_vulnibm_sh+count_other_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE OTRO VALOR DISTINTO A LOS ANTERIORES  \n")
    print("\n")

	
	
	
	
	
	
	
	




























	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	