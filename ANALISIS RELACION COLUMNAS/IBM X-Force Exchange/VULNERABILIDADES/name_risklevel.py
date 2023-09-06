
import pandas as pd
from datetime import datetime,timedelta



#Abro los ficheros con los que voy a tratar




df_vulnibm_iot = pd.read_excel('vulnerabilidades_ibm_iot_2023.xlsx')
#Contador de valores total de name
count_vulnibm_iot_names=0
#Variables que almacena el contador de valor de nombre concreto
count_vulnibm_iot_namepathtraversal=0
#Variable que almacena la puntuacion de  PUNTUACION BASE para posteriormente calcular la media del valor de PUNTUACION BASE
count_vulnibm_iot_namepathtraversal_risklevel=0
#Variables que almacenan el contador de PUNTUACION BASE segun valor de nombre concreto
count_vulnibm_iot_namepathtraversal_risklevel10=0
count_vulnibm_iot_namepathtraversal_risklevel9=0
count_vulnibm_iot_namepathtraversal_risklevel8=0
count_vulnibm_iot_namepathtraversal_risklevel7=0
count_vulnibm_iot_namepathtraversal_risklevel6=0
count_vulnibm_iot_namepathtraversal_risklevel5=0
count_vulnibm_iot_namepathtraversal_risklevel4=0
count_vulnibm_iot_namepathtraversal_risklevel3=0
count_vulnibm_iot_namepathtraversal_risklevel2=0
count_vulnibm_iot_namepathtraversal_risklevel1=0
count_vulnibm_iot_namepathtraversal_risklevel0=0



count_vulnibm_iot_namedirectorytraversal=0
count_vulnibm_iot_namedirectorytraversal_risklevel=0
count_vulnibm_iot_namedirectorytraversal_risklevel10=0
count_vulnibm_iot_namedirectorytraversal_risklevel9=0
count_vulnibm_iot_namedirectorytraversal_risklevel8=0
count_vulnibm_iot_namedirectorytraversal_risklevel7=0
count_vulnibm_iot_namedirectorytraversal_risklevel6=0
count_vulnibm_iot_namedirectorytraversal_risklevel5=0
count_vulnibm_iot_namedirectorytraversal_risklevel4=0
count_vulnibm_iot_namedirectorytraversal_risklevel3=0
count_vulnibm_iot_namedirectorytraversal_risklevel2=0
count_vulnibm_iot_namedirectorytraversal_risklevel1=0
count_vulnibm_iot_namedirectorytraversal_risklevel0=0


count_vulnibm_iot_nameprivilegeescalation=0
count_vulnibm_iot_nameprivilegeescalation_risklevel=0
count_vulnibm_iot_nameprivilegeescalation_risklevel10=0
count_vulnibm_iot_nameprivilegeescalation_risklevel9=0
count_vulnibm_iot_nameprivilegeescalation_risklevel8=0
count_vulnibm_iot_nameprivilegeescalation_risklevel7=0
count_vulnibm_iot_nameprivilegeescalation_risklevel6=0
count_vulnibm_iot_nameprivilegeescalation_risklevel5=0
count_vulnibm_iot_nameprivilegeescalation_risklevel4=0
count_vulnibm_iot_nameprivilegeescalation_risklevel3=0
count_vulnibm_iot_nameprivilegeescalation_risklevel2=0
count_vulnibm_iot_nameprivilegeescalation_risklevel1=0
count_vulnibm_iot_nameprivilegeescalation_risklevel0=0

count_vulnibm_iot_namecrosssitescripting=0
count_vulnibm_iot_namecrosssitescripting_risklevel=0
count_vulnibm_iot_namecrosssitescripting_risklevel10=0
count_vulnibm_iot_namecrosssitescripting_risklevel9=0
count_vulnibm_iot_namecrosssitescripting_risklevel8=0
count_vulnibm_iot_namecrosssitescripting_risklevel7=0
count_vulnibm_iot_namecrosssitescripting_risklevel6=0
count_vulnibm_iot_namecrosssitescripting_risklevel5=0
count_vulnibm_iot_namecrosssitescripting_risklevel4=0
count_vulnibm_iot_namecrosssitescripting_risklevel3=0
count_vulnibm_iot_namecrosssitescripting_risklevel2=0
count_vulnibm_iot_namecrosssitescripting_risklevel1=0
count_vulnibm_iot_namecrosssitescripting_risklevel0=0


count_vulnibm_iot_namesecuritybypass=0
count_vulnibm_iot_namesecuritybypass_risklevel=0
count_vulnibm_iot_namesecuritybypass_risklevel10=0
count_vulnibm_iot_namesecuritybypass_risklevel9=0
count_vulnibm_iot_namesecuritybypass_risklevel8=0
count_vulnibm_iot_namesecuritybypass_risklevel7=0
count_vulnibm_iot_namesecuritybypass_risklevel6=0
count_vulnibm_iot_namesecuritybypass_risklevel5=0
count_vulnibm_iot_namesecuritybypass_risklevel4=0
count_vulnibm_iot_namesecuritybypass_risklevel3=0
count_vulnibm_iot_namesecuritybypass_risklevel2=0
count_vulnibm_iot_namesecuritybypass_risklevel1=0
count_vulnibm_iot_namesecuritybypass_risklevel0=0


count_vulnibm_iot_nameinformationdisclosure=0
count_vulnibm_iot_nameinformationdisclosure_risklevel=0
count_vulnibm_iot_nameinformationdisclosure_risklevel10=0
count_vulnibm_iot_nameinformationdisclosure_risklevel9=0
count_vulnibm_iot_nameinformationdisclosure_risklevel8=0
count_vulnibm_iot_nameinformationdisclosure_risklevel7=0
count_vulnibm_iot_nameinformationdisclosure_risklevel6=0
count_vulnibm_iot_nameinformationdisclosure_risklevel5=0
count_vulnibm_iot_nameinformationdisclosure_risklevel4=0
count_vulnibm_iot_nameinformationdisclosure_risklevel3=0
count_vulnibm_iot_nameinformationdisclosure_risklevel2=0
count_vulnibm_iot_nameinformationdisclosure_risklevel1=0
count_vulnibm_iot_nameinformationdisclosure_risklevel0=0


count_vulnibm_iot_namedenialofservice=0
count_vulnibm_iot_namedenialofservice_risklevel=0
count_vulnibm_iot_namedenialofservice_risklevel10=0
count_vulnibm_iot_namedenialofservice_risklevel9=0
count_vulnibm_iot_namedenialofservice_risklevel8=0
count_vulnibm_iot_namedenialofservice_risklevel7=0
count_vulnibm_iot_namedenialofservice_risklevel6=0
count_vulnibm_iot_namedenialofservice_risklevel5=0
count_vulnibm_iot_namedenialofservice_risklevel4=0
count_vulnibm_iot_namedenialofservice_risklevel3=0
count_vulnibm_iot_namedenialofservice_risklevel2=0
count_vulnibm_iot_namedenialofservice_risklevel1=0
count_vulnibm_iot_namedenialofservice_risklevel0=0

count_vulnibm_iot_namecodeexecution=0
count_vulnibm_iot_namecodeexecution_risklevel=0
count_vulnibm_iot_namecodeexecution_risklevel10=0
count_vulnibm_iot_namecodeexecution_risklevel9=0
count_vulnibm_iot_namecodeexecution_risklevel8=0
count_vulnibm_iot_namecodeexecution_risklevel7=0
count_vulnibm_iot_namecodeexecution_risklevel6=0
count_vulnibm_iot_namecodeexecution_risklevel5=0
count_vulnibm_iot_namecodeexecution_risklevel4=0
count_vulnibm_iot_namecodeexecution_risklevel3=0
count_vulnibm_iot_namecodeexecution_risklevel2=0
count_vulnibm_iot_namecodeexecution_risklevel1=0
count_vulnibm_iot_namecodeexecution_risklevel0=0


count_vulnibm_iot_namemaninthemiddle=0
count_vulnibm_iot_namemaninthemiddle_risklevel=0
count_vulnibm_iot_namemaninthemiddle_risklevel10=0
count_vulnibm_iot_namemaninthemiddle_risklevel9=0
count_vulnibm_iot_namemaninthemiddle_risklevel8=0
count_vulnibm_iot_namemaninthemiddle_risklevel7=0
count_vulnibm_iot_namemaninthemiddle_risklevel6=0
count_vulnibm_iot_namemaninthemiddle_risklevel5=0
count_vulnibm_iot_namemaninthemiddle_risklevel4=0
count_vulnibm_iot_namemaninthemiddle_risklevel3=0
count_vulnibm_iot_namemaninthemiddle_risklevel2=0
count_vulnibm_iot_namemaninthemiddle_risklevel1=0
count_vulnibm_iot_namemaninthemiddle_risklevel0=0

count_vulnibm_iot_namesqlinjection=0
count_vulnibm_iot_namesqlinjection_risklevel=0
count_vulnibm_iot_namesqlinjection_risklevel10=0
count_vulnibm_iot_namesqlinjection_risklevel9=0
count_vulnibm_iot_namesqlinjection_risklevel8=0
count_vulnibm_iot_namesqlinjection_risklevel7=0
count_vulnibm_iot_namesqlinjection_risklevel6=0
count_vulnibm_iot_namesqlinjection_risklevel5=0
count_vulnibm_iot_namesqlinjection_risklevel4=0
count_vulnibm_iot_namesqlinjection_risklevel3=0
count_vulnibm_iot_namesqlinjection_risklevel2=0
count_vulnibm_iot_namesqlinjection_risklevel1=0
count_vulnibm_iot_namesqlinjection_risklevel0=0

count_vulnibm_iot_namecrosssiterequestforgery=0
count_vulnibm_iot_namecrosssiterequestforgery_risklevel=0
count_vulnibm_iot_namecrosssiterequestforgery_risklevel10=0
count_vulnibm_iot_namecrosssiterequestforgery_risklevel9=0
count_vulnibm_iot_namecrosssiterequestforgery_risklevel8=0
count_vulnibm_iot_namecrosssiterequestforgery_risklevel7=0
count_vulnibm_iot_namecrosssiterequestforgery_risklevel6=0
count_vulnibm_iot_namecrosssiterequestforgery_risklevel5=0
count_vulnibm_iot_namecrosssiterequestforgery_risklevel4=0
count_vulnibm_iot_namecrosssiterequestforgery_risklevel3=0
count_vulnibm_iot_namecrosssiterequestforgery_risklevel2=0
count_vulnibm_iot_namecrosssiterequestforgery_risklevel1=0
count_vulnibm_iot_namecrosssiterequestforgery_risklevel0=0

count_vulnibm_iot_namemoduleexecution=0
count_vulnibm_iot_namemoduleexecution_risklevel=0
count_vulnibm_iot_namemoduleexecution_risklevel10=0
count_vulnibm_iot_namemoduleexecution_risklevel9=0
count_vulnibm_iot_namemoduleexecution_risklevel8=0
count_vulnibm_iot_namemoduleexecution_risklevel7=0
count_vulnibm_iot_namemoduleexecution_risklevel6=0
count_vulnibm_iot_namemoduleexecution_risklevel5=0
count_vulnibm_iot_namemoduleexecution_risklevel4=0
count_vulnibm_iot_namemoduleexecution_risklevel3=0
count_vulnibm_iot_namemoduleexecution_risklevel2=0
count_vulnibm_iot_namemoduleexecution_risklevel1=0
count_vulnibm_iot_namemoduleexecution_risklevel0=0

count_vulnibm_iot_namebufferoverflow=0
count_vulnibm_iot_namebufferoverflow_risklevel=0
count_vulnibm_iot_namebufferoverflow_risklevel10=0
count_vulnibm_iot_namebufferoverflow_risklevel9=0
count_vulnibm_iot_namebufferoverflow_risklevel8=0
count_vulnibm_iot_namebufferoverflow_risklevel7=0
count_vulnibm_iot_namebufferoverflow_risklevel6=0
count_vulnibm_iot_namebufferoverflow_risklevel5=0
count_vulnibm_iot_namebufferoverflow_risklevel4=0
count_vulnibm_iot_namebufferoverflow_risklevel3=0
count_vulnibm_iot_namebufferoverflow_risklevel2=0
count_vulnibm_iot_namebufferoverflow_risklevel1=0
count_vulnibm_iot_namebufferoverflow_risklevel0=0

count_vulnibm_iot_namecommandexecution=0
count_vulnibm_iot_namecommandexecution_risklevel=0
count_vulnibm_iot_namecommandexecution_risklevel10=0
count_vulnibm_iot_namecommandexecution_risklevel9=0
count_vulnibm_iot_namecommandexecution_risklevel8=0
count_vulnibm_iot_namecommandexecution_risklevel7=0
count_vulnibm_iot_namecommandexecution_risklevel6=0
count_vulnibm_iot_namecommandexecution_risklevel5=0
count_vulnibm_iot_namecommandexecution_risklevel4=0
count_vulnibm_iot_namecommandexecution_risklevel3=0
count_vulnibm_iot_namecommandexecution_risklevel2=0
count_vulnibm_iot_namecommandexecution_risklevel1=0
count_vulnibm_iot_namecommandexecution_risklevel0=0

count_vulnibm_iot_namespoofing=0
count_vulnibm_iot_namespoofing_risklevel=0
count_vulnibm_iot_namespoofing_risklevel10=0
count_vulnibm_iot_namespoofing_risklevel9=0
count_vulnibm_iot_namespoofing_risklevel8=0
count_vulnibm_iot_namespoofing_risklevel7=0
count_vulnibm_iot_namespoofing_risklevel6=0
count_vulnibm_iot_namespoofing_risklevel5=0
count_vulnibm_iot_namespoofing_risklevel4=0
count_vulnibm_iot_namespoofing_risklevel3=0
count_vulnibm_iot_namespoofing_risklevel2=0
count_vulnibm_iot_namespoofing_risklevel1=0
count_vulnibm_iot_namespoofing_risklevel0=0

count_vulnibm_iot_nameclickjacking=0
count_vulnibm_iot_nameclickjacking_risklevel=0
count_vulnibm_iot_nameclickjacking_risklevel10=0
count_vulnibm_iot_nameclickjacking_risklevel9=0
count_vulnibm_iot_nameclickjacking_risklevel8=0
count_vulnibm_iot_nameclickjacking_risklevel7=0
count_vulnibm_iot_nameclickjacking_risklevel6=0
count_vulnibm_iot_nameclickjacking_risklevel5=0
count_vulnibm_iot_nameclickjacking_risklevel4=0
count_vulnibm_iot_nameclickjacking_risklevel3=0
count_vulnibm_iot_nameclickjacking_risklevel2=0
count_vulnibm_iot_nameclickjacking_risklevel1=0
count_vulnibm_iot_nameclickjacking_risklevel0=0

count_vulnibm_iot_namehijacking=0
count_vulnibm_iot_namehijacking_risklevel=0
count_vulnibm_iot_namehijacking_risklevel10=0
count_vulnibm_iot_namehijacking_risklevel9=0
count_vulnibm_iot_namehijacking_risklevel8=0
count_vulnibm_iot_namehijacking_risklevel7=0
count_vulnibm_iot_namehijacking_risklevel6=0
count_vulnibm_iot_namehijacking_risklevel5=0
count_vulnibm_iot_namehijacking_risklevel4=0
count_vulnibm_iot_namehijacking_risklevel3=0
count_vulnibm_iot_namehijacking_risklevel2=0
count_vulnibm_iot_namehijacking_risklevel1=0
count_vulnibm_iot_namehijacking_risklevel0=0

count_vulnibm_iot_namefileinclude=0
count_vulnibm_iot_namefileinclude_risklevel=0
count_vulnibm_iot_namefileinclude_risklevel10=0
count_vulnibm_iot_namefileinclude_risklevel9=0
count_vulnibm_iot_namefileinclude_risklevel8=0
count_vulnibm_iot_namefileinclude_risklevel7=0
count_vulnibm_iot_namefileinclude_risklevel6=0
count_vulnibm_iot_namefileinclude_risklevel5=0
count_vulnibm_iot_namefileinclude_risklevel4=0
count_vulnibm_iot_namefileinclude_risklevel3=0
count_vulnibm_iot_namefileinclude_risklevel2=0
count_vulnibm_iot_namefileinclude_risklevel1=0
count_vulnibm_iot_namefileinclude_risklevel0=0

count_vulnibm_iot_namebruteforce=0
count_vulnibm_iot_namebruteforce_risklevel=0
count_vulnibm_iot_namebruteforce_risklevel10=0
count_vulnibm_iot_namebruteforce_risklevel9=0
count_vulnibm_iot_namebruteforce_risklevel8=0
count_vulnibm_iot_namebruteforce_risklevel7=0
count_vulnibm_iot_namebruteforce_risklevel6=0
count_vulnibm_iot_namebruteforce_risklevel5=0
count_vulnibm_iot_namebruteforce_risklevel4=0
count_vulnibm_iot_namebruteforce_risklevel3=0
count_vulnibm_iot_namebruteforce_risklevel2=0
count_vulnibm_iot_namebruteforce_risklevel1=0
count_vulnibm_iot_namebruteforce_risklevel0=0

count_vulnibm_iot_namefileupload=0
count_vulnibm_iot_namefileupload_risklevel=0
count_vulnibm_iot_namefileupload_risklevel10=0
count_vulnibm_iot_namefileupload_risklevel9=0
count_vulnibm_iot_namefileupload_risklevel8=0
count_vulnibm_iot_namefileupload_risklevel7=0
count_vulnibm_iot_namefileupload_risklevel6=0
count_vulnibm_iot_namefileupload_risklevel5=0
count_vulnibm_iot_namefileupload_risklevel4=0
count_vulnibm_iot_namefileupload_risklevel3=0
count_vulnibm_iot_namefileupload_risklevel2=0
count_vulnibm_iot_namefileupload_risklevel1=0
count_vulnibm_iot_namefileupload_risklevel0=0

count_vulnibm_iot_nameheaderinjection=0
count_vulnibm_iot_nameheaderinjection_risklevel=0
count_vulnibm_iot_nameheaderinjection_risklevel10=0
count_vulnibm_iot_nameheaderinjection_risklevel9=0
count_vulnibm_iot_nameheaderinjection_risklevel8=0
count_vulnibm_iot_nameheaderinjection_risklevel7=0
count_vulnibm_iot_nameheaderinjection_risklevel6=0
count_vulnibm_iot_nameheaderinjection_risklevel5=0
count_vulnibm_iot_nameheaderinjection_risklevel4=0
count_vulnibm_iot_nameheaderinjection_risklevel3=0
count_vulnibm_iot_nameheaderinjection_risklevel2=0
count_vulnibm_iot_nameheaderinjection_risklevel1=0
count_vulnibm_iot_nameheaderinjection_risklevel0=0

count_vulnibm_iot_nametampering=0
count_vulnibm_iot_nametampering_risklevel=0
count_vulnibm_iot_nametampering_risklevel10=0
count_vulnibm_iot_nametampering_risklevel9=0
count_vulnibm_iot_nametampering_risklevel8=0
count_vulnibm_iot_nametampering_risklevel7=0
count_vulnibm_iot_nametampering_risklevel6=0
count_vulnibm_iot_nametampering_risklevel5=0
count_vulnibm_iot_nametampering_risklevel4=0
count_vulnibm_iot_nametampering_risklevel3=0
count_vulnibm_iot_nametampering_risklevel2=0
count_vulnibm_iot_nametampering_risklevel1=0
count_vulnibm_iot_nametampering_risklevel0=0

count_vulnibm_iot_nameanother=0
count_vulnibm_iot_nameanother_risklevel=0
count_vulnibm_iot_nameanother_risklevel10=0
count_vulnibm_iot_nameanother_risklevel9=0
count_vulnibm_iot_nameanother_risklevel8=0
count_vulnibm_iot_nameanother_risklevel7=0
count_vulnibm_iot_nameanother_risklevel6=0
count_vulnibm_iot_nameanother_risklevel5=0
count_vulnibm_iot_nameanother_risklevel4=0
count_vulnibm_iot_nameanother_risklevel3=0
count_vulnibm_iot_nameanother_risklevel2=0
count_vulnibm_iot_nameanother_risklevel1=0
count_vulnibm_iot_nameanother_risklevel0=0



















#Comprobamos el contenido de name
for r in range(0,len(df_vulnibm_iot["name"])):                       
    aux_str=df_vulnibm_iot["name"][r].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
    if(aux_str!='NONE'):
        count_vulnibm_iot_names+=1
        if('pathtraversal' in aux_str):
            count_vulnibm_iot_namepathtraversal+=1
            #Obtenemos el valor de PUNTUACION BASE y comprobamos, ademas almacenamos la suma para despues calcular la media de PUNTUACION BASE
            count_vulnibm_iot_namepathtraversal_risklevel+=float(df_vulnibm_iot["x_xfe_risk_level"][r])
            if(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 10.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=9.0)):
                count_vulnibm_iot_namepathtraversal_risklevel9+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 9.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=8.0)):
                count_vulnibm_iot_namepathtraversal_risklevel8+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 8.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=7.0)):
                count_vulnibm_iot_namepathtraversal_risklevel7+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 7.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=6.0)):
                count_vulnibm_iot_namepathtraversal_risklevel6+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 6.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=5.0)):
                count_vulnibm_iot_namepathtraversal_risklevel5+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 5.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=4.0)):
                count_vulnibm_iot_namepathtraversal_risklevel4+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 4.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=3.0)):
                count_vulnibm_iot_namepathtraversal_risklevel3+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 3.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=2.0)):
                count_vulnibm_iot_namepathtraversal_risklevel2+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 2.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=1.0)):
                count_vulnibm_iot_namepathtraversal_risklevel1+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 1.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=0.0)):
                count_vulnibm_iot_namepathtraversal_risklevel0+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) == 10.0)):
                count_vulnibm_iot_namepathtraversal_risklevel10+=1
            
        elif('directorytraversal' in aux_str):
            
            count_vulnibm_iot_namedirectorytraversal+=1
            count_vulnibm_iot_namedirectorytraversal_risklevel+=float(df_vulnibm_iot["x_xfe_risk_level"][r])
            if(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 10.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=9.0)):
                count_vulnibm_iot_namedirectorytraversal_risklevel9+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 9.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=8.0)):
                count_vulnibm_iot_namedirectorytraversal_risklevel8+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 8.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=7.0)):
                count_vulnibm_iot_namedirectorytraversal_risklevel7+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 7.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=6.0)):
                count_vulnibm_iot_namedirectorytraversal_risklevel6+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 6.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=5.0)):
                count_vulnibm_iot_namedirectorytraversal_risklevel5+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 5.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=4.0)):
                count_vulnibm_iot_namedirectorytraversal_risklevel4+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 4.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=3.0)):
                count_vulnibm_iot_namedirectorytraversal_risklevel3+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 3.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=2.0)):
                count_vulnibm_iot_namedirectorytraversal_risklevel2+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 2.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=1.0)):
                count_vulnibm_iot_namedirectorytraversal_risklevel1+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 1.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=0.0)):
                count_vulnibm_iot_namedirectorytraversal_risklevel0+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) == 10.0)):
                count_vulnibm_iot_namedirectorytraversal_risklevel10+=1
            
            
        elif('privilegeescalation' in aux_str):
        
            count_vulnibm_iot_nameprivilegeescalation+=1
            count_vulnibm_iot_nameprivilegeescalation_risklevel+=float(df_vulnibm_iot["x_xfe_risk_level"][r])
            if(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 10.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=9.0)):
                count_vulnibm_iot_nameprivilegeescalation_risklevel9+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 9.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=8.0)):
                count_vulnibm_iot_nameprivilegeescalation_risklevel8+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 8.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=7.0)):
                count_vulnibm_iot_nameprivilegeescalation_risklevel7+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 7.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=6.0)):
                count_vulnibm_iot_nameprivilegeescalation_risklevel6+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 6.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=5.0)):
                count_vulnibm_iot_nameprivilegeescalation_risklevel5+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 5.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=4.0)):
                count_vulnibm_iot_nameprivilegeescalation_risklevel4+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 4.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=3.0)):
                count_vulnibm_iot_nameprivilegeescalation_risklevel3+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 3.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=2.0)):
                count_vulnibm_iot_nameprivilegeescalation_risklevel2+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 2.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=1.0)):
                count_vulnibm_iot_nameprivilegeescalation_risklevel1+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 1.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=0.0)):
                count_vulnibm_iot_nameprivilegeescalation_risklevel0+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) == 10.0)):
                count_vulnibm_iot_nameprivilegeescalation_risklevel10+=1
            
        elif('cross-sitescripting' in aux_str):
        
            count_vulnibm_iot_namecrosssitescripting+=1
            count_vulnibm_iot_namecrosssitescripting_risklevel+=float(df_vulnibm_iot["x_xfe_risk_level"][r])
            if(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 10.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=9.0)):
                count_vulnibm_iot_namecrosssitescripting_risklevel9+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 9.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=8.0)):
                count_vulnibm_iot_namecrosssitescripting_risklevel8+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 8.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=7.0)):
                count_vulnibm_iot_namecrosssitescripting_risklevel7+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 7.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=6.0)):
                count_vulnibm_iot_namecrosssitescripting_risklevel6+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 6.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=5.0)):
                count_vulnibm_iot_namecrosssitescripting_risklevel5+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 5.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=4.0)):
                count_vulnibm_iot_namecrosssitescripting_risklevel4+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 4.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=3.0)):
                count_vulnibm_iot_namecrosssitescripting_risklevel3+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 3.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=2.0)):
                count_vulnibm_iot_namecrosssitescripting_risklevel2+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 2.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=1.0)):
                count_vulnibm_iot_namecrosssitescripting_risklevel1+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 1.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=0.0)):
                count_vulnibm_iot_namecrosssitescripting_risklevel0+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) == 10.0)):
                count_vulnibm_iot_namecrosssitescripting_risklevel10+=1
                                         
        elif('securitybypass' in aux_str):
        
            count_vulnibm_iot_namesecuritybypass+=1
            count_vulnibm_iot_namesecuritybypass_risklevel+=float(df_vulnibm_iot["x_xfe_risk_level"][r])
            if(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 10.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=9.0)):
                count_vulnibm_iot_namesecuritybypass_risklevel9+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 9.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=8.0)):
                count_vulnibm_iot_namesecuritybypass_risklevel8+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 8.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=7.0)):
                count_vulnibm_iot_namesecuritybypass_risklevel7+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 7.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=6.0)):
                count_vulnibm_iot_namesecuritybypass_risklevel6+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 6.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=5.0)):
                count_vulnibm_iot_namesecuritybypass_risklevel5+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 5.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=4.0)):
                count_vulnibm_iot_namesecuritybypass_risklevel4+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 4.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=3.0)):
                count_vulnibm_iot_namesecuritybypass_risklevel3+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 3.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=2.0)):
                count_vulnibm_iot_namesecuritybypass_risklevel2+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 2.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=1.0)):
                count_vulnibm_iot_namesecuritybypass_risklevel1+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 1.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=0.0)):
                count_vulnibm_iot_namesecuritybypass_risklevel0+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) == 10.0)):
                count_vulnibm_iot_namesecuritybypass_risklevel10+=1
                                         
        elif('information_disclosure' in aux_str or 'informationdisclosure' in aux_str):
        
            count_vulnibm_iot_nameinformationdisclosure+=1
            count_vulnibm_iot_nameinformationdisclosure_risklevel+=float(df_vulnibm_iot["x_xfe_risk_level"][r])
            if(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 10.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=9.0)):
                count_vulnibm_iot_nameinformationdisclosure_risklevel9+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 9.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=8.0)):
                count_vulnibm_iot_nameinformationdisclosure_risklevel8+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 8.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=7.0)):
                count_vulnibm_iot_nameinformationdisclosure_risklevel7+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 7.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=6.0)):
                count_vulnibm_iot_nameinformationdisclosure_risklevel6+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 6.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=5.0)):
                count_vulnibm_iot_nameinformationdisclosure_risklevel5+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 5.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=4.0)):
                count_vulnibm_iot_nameinformationdisclosure_risklevel4+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 4.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=3.0)):
                count_vulnibm_iot_nameinformationdisclosure_risklevel3+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 3.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=2.0)):
                count_vulnibm_iot_nameinformationdisclosure_risklevel2+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 2.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=1.0)):
                count_vulnibm_iot_nameinformationdisclosure_risklevel1+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 1.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=0.0)):
                count_vulnibm_iot_nameinformationdisclosure_risklevel0+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) == 10.0)):
                count_vulnibm_iot_nameinformationdisclosure_risklevel10+=1
                                         
        elif('denialofservice' in aux_str):
            
            count_vulnibm_iot_namedenialofservice+=1
            count_vulnibm_iot_namedenialofservice_risklevel+=float(df_vulnibm_iot["x_xfe_risk_level"][r])
            if(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 10.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=9.0)):
                count_vulnibm_iot_namedenialofservice_risklevel9+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 9.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=8.0)):
                count_vulnibm_iot_namedenialofservice_risklevel8+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 8.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=7.0)):
                count_vulnibm_iot_namedenialofservice_risklevel7+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 7.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=6.0)):
                count_vulnibm_iot_namedenialofservice_risklevel6+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 6.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=5.0)):
                count_vulnibm_iot_namedenialofservice_risklevel5+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 5.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=4.0)):
                count_vulnibm_iot_namedenialofservice_risklevel4+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 4.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=3.0)):
                count_vulnibm_iot_namedenialofservice_risklevel3+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 3.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=2.0)):
                count_vulnibm_iot_namedenialofservice_risklevel2+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 2.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=1.0)):
                count_vulnibm_iot_namedenialofservice_risklevel1+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 1.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=0.0)):
                count_vulnibm_iot_namedenialofservice_risklevel0+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) == 10.0)):
                count_vulnibm_iot_namedenialofservice_risklevel10+=1
            
        elif('codeexecution' in aux_str):
        
        
            count_vulnibm_iot_namecodeexecution+=1
            count_vulnibm_iot_namecodeexecution_risklevel+=float(df_vulnibm_iot["x_xfe_risk_level"][r])
            if(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 10.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=9.0)):
                count_vulnibm_iot_namecodeexecution_risklevel9+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 9.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=8.0)):
                count_vulnibm_iot_namecodeexecution_risklevel8+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 8.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=7.0)):
                count_vulnibm_iot_namecodeexecution_risklevel7+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 7.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=6.0)):
                count_vulnibm_iot_namecodeexecution_risklevel6+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 6.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=5.0)):
                count_vulnibm_iot_namecodeexecution_risklevel5+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 5.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=4.0)):
                count_vulnibm_iot_namecodeexecution_risklevel4+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 4.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=3.0)):
                count_vulnibm_iot_namecodeexecution_risklevel3+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 3.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=2.0)):
                count_vulnibm_iot_namecodeexecution_risklevel2+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 2.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=1.0)):
                count_vulnibm_iot_namecodeexecution_risklevel1+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 1.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=0.0)):
                count_vulnibm_iot_namecodeexecution_risklevel0+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) == 10.0)):
                count_vulnibm_iot_namecodeexecution_risklevel10+=1
                                         
        elif('maninthemiddle' in aux_str):
        
            count_vulnibm_iot_namemaninthemiddle+=1
            count_vulnibm_iot_namemaninthemiddle_risklevel+=float(df_vulnibm_iot["x_xfe_risk_level"][r])
            if(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 10.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=9.0)):
                count_vulnibm_iot_namemaninthemiddle_risklevel9+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 9.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=8.0)):
                count_vulnibm_iot_namemaninthemiddle_risklevel8+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 8.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=7.0)):
                count_vulnibm_iot_namemaninthemiddle_risklevel7+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 7.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=6.0)):
                count_vulnibm_iot_namemaninthemiddle_risklevel6+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 6.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=5.0)):
                count_vulnibm_iot_namemaninthemiddle_risklevel5+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 5.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=4.0)):
                count_vulnibm_iot_namemaninthemiddle_risklevel4+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 4.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=3.0)):
                count_vulnibm_iot_namemaninthemiddle_risklevel3+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 3.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=2.0)):
                count_vulnibm_iot_namemaninthemiddle_risklevel2+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 2.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=1.0)):
                count_vulnibm_iot_namemaninthemiddle_risklevel1+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 1.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=0.0)):
                count_vulnibm_iot_namemaninthemiddle_risklevel0+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) == 10.0)):
                count_vulnibm_iot_namemaninthemiddle_risklevel10+=1
                                         
        elif('SQLinjection' in aux_str):
        
            count_vulnibm_iot_namesqlinjection+=1
            count_vulnibm_iot_namesqlinjection_risklevel+=float(df_vulnibm_iot["x_xfe_risk_level"][r])
            if(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 10.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=9.0)):
                count_vulnibm_iot_namesqlinjection_risklevel9+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 9.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=8.0)):
                count_vulnibm_iot_namesqlinjection_risklevel8+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 8.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=7.0)):
                count_vulnibm_iot_namesqlinjection_risklevel7+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 7.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=6.0)):
                count_vulnibm_iot_namesqlinjection_risklevel6+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 6.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=5.0)):
                count_vulnibm_iot_namesqlinjection_risklevel5+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 5.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=4.0)):
                count_vulnibm_iot_namesqlinjection_risklevel4+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 4.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=3.0)):
                count_vulnibm_iot_namesqlinjection_risklevel3+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 3.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=2.0)):
                count_vulnibm_iot_namesqlinjection_risklevel2+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 2.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=1.0)):
                count_vulnibm_iot_namesqlinjection_risklevel1+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 1.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=0.0)):
                count_vulnibm_iot_namesqlinjection_risklevel0+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) == 10.0)):
                count_vulnibm_iot_namesqlinjection_risklevel10+=1
                                         
        elif('cross-siterequestforgery' in aux_str):
        
            count_vulnibm_iot_namecrosssiterequestforgery+=1
            count_vulnibm_iot_namecrosssiterequestforgery_risklevel+=float(df_vulnibm_iot["x_xfe_risk_level"][r])
            if(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 10.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=9.0)):
                count_vulnibm_iot_namecrosssiterequestforgery_risklevel9+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 9.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=8.0)):
                count_vulnibm_iot_namecrosssiterequestforgery_risklevel8+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 8.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=7.0)):
                count_vulnibm_iot_namecrosssiterequestforgery_risklevel7+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 7.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=6.0)):
                count_vulnibm_iot_namecrosssiterequestforgery_risklevel6+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 6.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=5.0)):
                count_vulnibm_iot_namecrosssiterequestforgery_risklevel5+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 5.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=4.0)):
                count_vulnibm_iot_namecrosssiterequestforgery_risklevel4+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 4.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=3.0)):
                count_vulnibm_iot_namecrosssiterequestforgery_risklevel3+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 3.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=2.0)):
                count_vulnibm_iot_namecrosssiterequestforgery_risklevel2+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 2.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=1.0)):
                count_vulnibm_iot_namecrosssiterequestforgery_risklevel1+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 1.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=0.0)):
                count_vulnibm_iot_namecrosssiterequestforgery_risklevel0+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) == 10.0)):
                count_vulnibm_iot_namecrosssiterequestforgery_risklevel10+=1
                                         
        elif('moduleexecution' in aux_str):
        
            count_vulnibm_iot_namemoduleexecution+=1
            count_vulnibm_iot_namemoduleexecution_risklevel+=float(df_vulnibm_iot["x_xfe_risk_level"][r])
            if(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 10.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=9.0)):
                count_vulnibm_iot_namemoduleexecution_risklevel9+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 9.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=8.0)):
                count_vulnibm_iot_namemoduleexecution_risklevel8+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 8.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=7.0)):
                count_vulnibm_iot_namemoduleexecution_risklevel7+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 7.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=6.0)):
                count_vulnibm_iot_namemoduleexecution_risklevel6+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 6.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=5.0)):
                count_vulnibm_iot_namemoduleexecution_risklevel5+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 5.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=4.0)):
                count_vulnibm_iot_namemoduleexecution_risklevel4+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 4.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=3.0)):
                count_vulnibm_iot_namemoduleexecution_risklevel3+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 3.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=2.0)):
                count_vulnibm_iot_namemoduleexecution_risklevel2+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 2.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=1.0)):
                count_vulnibm_iot_namemoduleexecution_risklevel1+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 1.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=0.0)):
                count_vulnibm_iot_namemoduleexecution_risklevel0+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) == 10.0)):
                count_vulnibm_iot_namemoduleexecution_risklevel10+=1
                                         
        elif('bufferoverflow' in aux_str):
        
            count_vulnibm_iot_namebufferoverflow+=1
            count_vulnibm_iot_namebufferoverflow_risklevel+=float(df_vulnibm_iot["x_xfe_risk_level"][r])
            if(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 10.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=9.0)):
                count_vulnibm_iot_namebufferoverflow_risklevel9+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 9.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=8.0)):
                count_vulnibm_iot_namebufferoverflow_risklevel8+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 8.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=7.0)):
                count_vulnibm_iot_namebufferoverflow_risklevel7+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 7.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=6.0)):
                count_vulnibm_iot_namebufferoverflow_risklevel6+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 6.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=5.0)):
                count_vulnibm_iot_namebufferoverflow_risklevel5+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 5.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=4.0)):
                count_vulnibm_iot_namebufferoverflow_risklevel4+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 4.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=3.0)):
                count_vulnibm_iot_namebufferoverflow_risklevel3+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 3.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=2.0)):
                count_vulnibm_iot_namebufferoverflow_risklevel2+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 2.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=1.0)):
                count_vulnibm_iot_namebufferoverflow_risklevel1+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 1.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=0.0)):
                count_vulnibm_iot_namebufferoverflow_risklevel0+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) == 10.0)):
                count_vulnibm_iot_namebufferoverflow_risklevel10+=1
                                         
        elif('commandexecution' in aux_str):
        
            count_vulnibm_iot_namecommandexecution+=1
            count_vulnibm_iot_namecommandexecution_risklevel+=float(df_vulnibm_iot["x_xfe_risk_level"][r])
            if(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 10.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=9.0)):
                count_vulnibm_iot_namecommandexecution_risklevel9+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 9.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=8.0)):
                count_vulnibm_iot_namecommandexecution_risklevel8+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 8.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=7.0)):
                count_vulnibm_iot_namecommandexecution_risklevel7+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 7.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=6.0)):
                count_vulnibm_iot_namecommandexecution_risklevel6+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 6.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=5.0)):
                count_vulnibm_iot_namecommandexecution_risklevel5+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 5.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=4.0)):
                count_vulnibm_iot_namecommandexecution_risklevel4+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 4.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=3.0)):
                count_vulnibm_iot_namecommandexecution_risklevel3+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 3.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=2.0)):
                count_vulnibm_iot_namecommandexecution_risklevel2+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 2.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=1.0)):
                count_vulnibm_iot_namecommandexecution_risklevel1+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 1.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=0.0)):
                count_vulnibm_iot_namecommandexecution_risklevel0+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) == 10.0)):
                count_vulnibm_iot_namecommandexecution_risklevel10+=1
                                         
        elif('spoofing' in aux_str):
        
            count_vulnibm_iot_namespoofing+=1
            count_vulnibm_iot_namespoofing_risklevel+=float(df_vulnibm_iot["x_xfe_risk_level"][r])
            if(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 10.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=9.0)):
                count_vulnibm_iot_namespoofing_risklevel9+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 9.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=8.0)):
                count_vulnibm_iot_namespoofing_risklevel8+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 8.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=7.0)):
                count_vulnibm_iot_namespoofing_risklevel7+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 7.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=6.0)):
                count_vulnibm_iot_namespoofing_risklevel6+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 6.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=5.0)):
                count_vulnibm_iot_namespoofing_risklevel5+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 5.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=4.0)):
                count_vulnibm_iot_namespoofing_risklevel4+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 4.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=3.0)):
                count_vulnibm_iot_namespoofing_risklevel3+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 3.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=2.0)):
                count_vulnibm_iot_namespoofing_risklevel2+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 2.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=1.0)):
                count_vulnibm_iot_namespoofing_risklevel1+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 1.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=0.0)):
                count_vulnibm_iot_namespoofing_risklevel0+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) == 10.0)):
                count_vulnibm_iot_namespoofing_risklevel10+=1
                                         
        elif('clickjacking' in aux_str):
        
            count_vulnibm_iot_nameclickjacking+=1
            count_vulnibm_iot_nameclickjacking_risklevel+=float(df_vulnibm_iot["x_xfe_risk_level"][r])
            if(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 10.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=9.0)):
                count_vulnibm_iot_nameclickjacking_risklevel9+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 9.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=8.0)):
                count_vulnibm_iot_nameclickjacking_risklevel8+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 8.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=7.0)):
                count_vulnibm_iot_nameclickjacking_risklevel7+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 7.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=6.0)):
                count_vulnibm_iot_nameclickjacking_risklevel6+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 6.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=5.0)):
                count_vulnibm_iot_nameclickjacking_risklevel5+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 5.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=4.0)):
                count_vulnibm_iot_nameclickjacking_risklevel4+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 4.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=3.0)):
                count_vulnibm_iot_nameclickjacking_risklevel3+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 3.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=2.0)):
                count_vulnibm_iot_nameclickjacking_risklevel2+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 2.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=1.0)):
                count_vulnibm_iot_nameclickjacking_risklevel1+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 1.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=0.0)):
                count_vulnibm_iot_nameclickjacking_risklevel0+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) == 10.0)):
                count_vulnibm_iot_nameclickjacking_risklevel10+=1
              
        elif('hijacking' in aux_str):
        
            count_vulnibm_iot_namehijacking+=1
            count_vulnibm_iot_namehijacking_risklevel+=float(df_vulnibm_iot["x_xfe_risk_level"][r])
            if(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 10.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=9.0)):
                count_vulnibm_iot_namehijacking_risklevel9+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 9.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=8.0)):
                count_vulnibm_iot_namehijacking_risklevel8+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 8.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=7.0)):
                count_vulnibm_iot_namehijacking_risklevel7+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 7.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=6.0)):
                count_vulnibm_iot_namehijacking_risklevel6+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 6.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=5.0)):
                count_vulnibm_iot_namehijacking_risklevel5+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 5.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=4.0)):
                count_vulnibm_iot_namehijacking_risklevel4+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 4.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=3.0)):
                count_vulnibm_iot_namehijacking_risklevel3+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 3.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=2.0)):
                count_vulnibm_iot_namehijacking_risklevel2+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 2.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=1.0)):
                count_vulnibm_iot_namehijacking_risklevel1+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 1.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=0.0)):
                count_vulnibm_iot_namehijacking_risklevel0+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) == 10.0)):
                count_vulnibm_iot_namehijacking_risklevel10+=1
               
        elif('fileinclude' in aux_str):
        
            count_vulnibm_iot_namefileinclude+=1
            count_vulnibm_iot_namefileinclude_risklevel+=float(df_vulnibm_iot["x_xfe_risk_level"][r])
            if(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 10.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=9.0)):
                count_vulnibm_iot_namefileinclude_risklevel9+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 9.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=8.0)):
                count_vulnibm_iot_namefileinclude_risklevel8+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 8.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=7.0)):
                count_vulnibm_iot_namefileinclude_risklevel7+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 7.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=6.0)):
                count_vulnibm_iot_namefileinclude_risklevel6+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 6.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=5.0)):
                count_vulnibm_iot_namefileinclude_risklevel5+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 5.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=4.0)):
                count_vulnibm_iot_namefileinclude_risklevel4+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 4.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=3.0)):
                count_vulnibm_iot_namefileinclude_risklevel3+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 3.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=2.0)):
                count_vulnibm_iot_namefileinclude_risklevel2+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 2.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=1.0)):
                count_vulnibm_iot_namefileinclude_risklevel1+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 1.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=0.0)):
                count_vulnibm_iot_namefileinclude_risklevel0+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) == 10.0)):
                count_vulnibm_iot_namefileinclude_risklevel10+=1
                
               
        elif('bruteforce' in aux_str):
        
            count_vulnibm_iot_namebruteforce+=1
            count_vulnibm_iot_namebruteforce_risklevel+=float(df_vulnibm_iot["x_xfe_risk_level"][r])
            if(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 10.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=9.0)):
                count_vulnibm_iot_namebruteforce_risklevel9+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 9.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=8.0)):
                count_vulnibm_iot_namebruteforce_risklevel8+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 8.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=7.0)):
                count_vulnibm_iot_namebruteforce_risklevel7+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 7.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=6.0)):
                count_vulnibm_iot_namebruteforce_risklevel6+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 6.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=5.0)):
                count_vulnibm_iot_namebruteforce_risklevel5+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 5.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=4.0)):
                count_vulnibm_iot_namebruteforce_risklevel4+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 4.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=3.0)):
                count_vulnibm_iot_namebruteforce_risklevel3+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 3.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=2.0)):
                count_vulnibm_iot_namebruteforce_risklevel2+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 2.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=1.0)):
                count_vulnibm_iot_namebruteforce_risklevel1+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 1.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=0.0)):
                count_vulnibm_iot_namebruteforce_risklevel0+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) == 10.0)):
                count_vulnibm_iot_namebruteforce_risklevel10+=1
                
               
        elif('fileupload' in aux_str):
        
            count_vulnibm_iot_namefileupload+=1
            count_vulnibm_iot_namefileupload_risklevel+=float(df_vulnibm_iot["x_xfe_risk_level"][r])
            if(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 10.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=9.0)):
                count_vulnibm_iot_namefileupload_risklevel9+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 9.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=8.0)):
                count_vulnibm_iot_namefileupload_risklevel8+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 8.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=7.0)):
                count_vulnibm_iot_namefileupload_risklevel7+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 7.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=6.0)):
                count_vulnibm_iot_namefileupload_risklevel6+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 6.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=5.0)):
                count_vulnibm_iot_namefileupload_risklevel5+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 5.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=4.0)):
                count_vulnibm_iot_namefileupload_risklevel4+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 4.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=3.0)):
                count_vulnibm_iot_namefileupload_risklevel3+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 3.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=2.0)):
                count_vulnibm_iot_namefileupload_risklevel2+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 2.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=1.0)):
                count_vulnibm_iot_namefileupload_risklevel1+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 1.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=0.0)):
                count_vulnibm_iot_namefileupload_risklevel0+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) == 10.0)):
                count_vulnibm_iot_namefileupload_risklevel10+=1
                
               
        elif('headerinjection' in aux_str):
        
            count_vulnibm_iot_nameheaderinjection+=1
            count_vulnibm_iot_nameheaderinjection_risklevel+=float(df_vulnibm_iot["x_xfe_risk_level"][r])
            if(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 10.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=9.0)):
                count_vulnibm_iot_nameheaderinjection_risklevel9+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 9.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=8.0)):
                count_vulnibm_iot_nameheaderinjection_risklevel8+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 8.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=7.0)):
                count_vulnibm_iot_nameheaderinjection_risklevel7+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 7.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=6.0)):
                count_vulnibm_iot_nameheaderinjection_risklevel6+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 6.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=5.0)):
                count_vulnibm_iot_nameheaderinjection_risklevel5+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 5.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=4.0)):
                count_vulnibm_iot_nameheaderinjection_risklevel4+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 4.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=3.0)):
                count_vulnibm_iot_nameheaderinjection_risklevel3+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 3.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=2.0)):
                count_vulnibm_iot_nameheaderinjection_risklevel2+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 2.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=1.0)):
                count_vulnibm_iot_nameheaderinjection_risklevel1+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 1.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=0.0)):
                count_vulnibm_iot_nameheaderinjection_risklevel0+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) == 10.0)):
                count_vulnibm_iot_nameheaderinjection_risklevel10+=1
               
        elif('Tampering' in aux_str):
        
            count_vulnibm_iot_nametampering+=1
            count_vulnibm_iot_nametampering_risklevel+=float(df_vulnibm_iot["x_xfe_risk_level"][r])
            if(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 10.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=9.0)):
                count_vulnibm_iot_nametampering_risklevel9+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 9.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=8.0)):
                count_vulnibm_iot_nametampering_risklevel8+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 8.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=7.0)):
                count_vulnibm_iot_nametampering_risklevel7+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 7.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=6.0)):
                count_vulnibm_iot_nametampering_risklevel6+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 6.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=5.0)):
                count_vulnibm_iot_nametampering_risklevel5+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 5.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=4.0)):
                count_vulnibm_iot_nametampering_risklevel4+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 4.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=3.0)):
                count_vulnibm_iot_nametampering_risklevel3+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 3.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=2.0)):
                count_vulnibm_iot_nametampering_risklevel2+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 2.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=1.0)):
                count_vulnibm_iot_nametampering_risklevel1+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 1.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=0.0)):
                count_vulnibm_iot_nametampering_risklevel0+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) == 10.0)):
                count_vulnibm_iot_nametampering_risklevel10+=1    
        else:
        
            count_vulnibm_iot_nameanother+=1
            count_vulnibm_iot_nameanother_risklevel+=float(df_vulnibm_iot["x_xfe_risk_level"][r])
            if(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 10.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=9.0)):
                count_vulnibm_iot_nameanother_risklevel9+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 9.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=8.0)):
                count_vulnibm_iot_nameanother_risklevel8+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 8.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=7.0)):
                count_vulnibm_iot_nameanother_risklevel7+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 7.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=6.0)):
                count_vulnibm_iot_nameanother_risklevel6+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 6.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=5.0)):
                count_vulnibm_iot_nameanother_risklevel5+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 5.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=4.0)):
                count_vulnibm_iot_nameanother_risklevel4+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 4.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=3.0)):
                count_vulnibm_iot_nameanother_risklevel3+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 3.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=2.0)):
                count_vulnibm_iot_nameanother_risklevel2+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 2.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=1.0)):
                count_vulnibm_iot_nameanother_risklevel1+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 1.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=0.0)):
                count_vulnibm_iot_nameanother_risklevel0+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) == 10.0)):
                count_vulnibm_iot_nameanother_risklevel10+=1
                
                
                
                
                
print("*********************ESTADÍSTICAS NOMBRE/PUNTUACION BASE OBJETOS DE TIPO VULNERABILIDAD IBM PARTE IOT*********************")
print("\n")                            
print("\n")
print(" DE UN TOTAL DE "+str(count_vulnibm_iot_names)+" VULNERABILIDADES:\n") 
print("\n")
print("   - LAS ESTADISTICAS DE VALORES DE NOMBRE SON LAS SIGUIENTES:  \n")
print("      -    EN  "+str(count_vulnibm_iot_namepathtraversal)+" VULNERABILIDADES EL NOMBRE INCLUYE PATH TRAVERSAL, LAS ESTADÍSTICAS DE PUNTUACION BASE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_namepathtraversal_risklevel10)+" VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
print("            -    EN  "+str(count_vulnibm_iot_namepathtraversal_risklevel9)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN  "+str(count_vulnibm_iot_namepathtraversal_risklevel8)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN  "+str(count_vulnibm_iot_namepathtraversal_risklevel7)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN  "+str(count_vulnibm_iot_namepathtraversal_risklevel6)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN "+str(count_vulnibm_iot_namepathtraversal_risklevel5)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN "+str(count_vulnibm_iot_namepathtraversal_risklevel4)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN "+str(count_vulnibm_iot_namepathtraversal_risklevel3)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN "+str(count_vulnibm_iot_namepathtraversal_risklevel2)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN "+str(count_vulnibm_iot_namepathtraversal_risklevel1)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN "+str(count_vulnibm_iot_namepathtraversal_risklevel0)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_namedirectorytraversal)+" VULNERABILIDADES EL NOMBRE INCLUYE DIRECTORY TRAVERSAL, LAS ESTADÍSTICAS DE PUNTUACION BASE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_namedirectorytraversal_risklevel10)+" VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
print("            -    EN  "+str(count_vulnibm_iot_namedirectorytraversal_risklevel9)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN  "+str(count_vulnibm_iot_namedirectorytraversal_risklevel8)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN  "+str(count_vulnibm_iot_namedirectorytraversal_risklevel7)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN  "+str(count_vulnibm_iot_namedirectorytraversal_risklevel6)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN "+str(count_vulnibm_iot_namedirectorytraversal_risklevel5)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN "+str(count_vulnibm_iot_namedirectorytraversal_risklevel4)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN "+str(count_vulnibm_iot_namedirectorytraversal_risklevel3)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN "+str(count_vulnibm_iot_namedirectorytraversal_risklevel2)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN "+str(count_vulnibm_iot_namedirectorytraversal_risklevel1)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN "+str(count_vulnibm_iot_namedirectorytraversal_risklevel0)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_nameprivilegeescalation)+" VULNERABILIDADES EL NOMBRE INCLUYE PRIVILEGE ESCALATION, LAS ESTADÍSTICAS DE PUNTUACION BASE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_nameprivilegeescalation_risklevel10)+" VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
print("            -    EN  "+str(count_vulnibm_iot_nameprivilegeescalation_risklevel9)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN  "+str(count_vulnibm_iot_nameprivilegeescalation_risklevel8)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN  "+str(count_vulnibm_iot_nameprivilegeescalation_risklevel7)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN  "+str(count_vulnibm_iot_nameprivilegeescalation_risklevel6)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN "+str(count_vulnibm_iot_nameprivilegeescalation_risklevel5)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN "+str(count_vulnibm_iot_nameprivilegeescalation_risklevel4)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN "+str(count_vulnibm_iot_nameprivilegeescalation_risklevel3)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN "+str(count_vulnibm_iot_nameprivilegeescalation_risklevel2)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN "+str(count_vulnibm_iot_nameprivilegeescalation_risklevel1)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN "+str(count_vulnibm_iot_nameprivilegeescalation_risklevel0)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_namecrosssitescripting)+" VULNERABILIDADES EL NOMBRE INCLUYE CROSS SITE SCRIPTING, LAS ESTADÍSTICAS DE PUNTUACION BASE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_namecrosssitescripting_risklevel10)+" VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
print("            -    EN  "+str(count_vulnibm_iot_namecrosssitescripting_risklevel9)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN  "+str(count_vulnibm_iot_namecrosssitescripting_risklevel8)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN  "+str(count_vulnibm_iot_namecrosssitescripting_risklevel7)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN  "+str(count_vulnibm_iot_namecrosssitescripting_risklevel6)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN "+str(count_vulnibm_iot_namecrosssitescripting_risklevel5)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN "+str(count_vulnibm_iot_namecrosssitescripting_risklevel4)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN "+str(count_vulnibm_iot_namecrosssitescripting_risklevel3)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN "+str(count_vulnibm_iot_namecrosssitescripting_risklevel2)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN "+str(count_vulnibm_iot_namecrosssitescripting_risklevel1)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN "+str(count_vulnibm_iot_namecrosssitescripting_risklevel0)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_namesecuritybypass)+" VULNERABILIDADES EL NOMBRE INCLUYE SECURITY BYPASS, LAS ESTADÍSTICAS DE PUNTUACION BASE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_namesecuritybypass_risklevel10)+" VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
print("            -    EN  "+str(count_vulnibm_iot_namesecuritybypass_risklevel9)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN  "+str(count_vulnibm_iot_namesecuritybypass_risklevel8)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN  "+str(count_vulnibm_iot_namesecuritybypass_risklevel7)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN  "+str(count_vulnibm_iot_namesecuritybypass_risklevel6)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN "+str(count_vulnibm_iot_namesecuritybypass_risklevel5)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN "+str(count_vulnibm_iot_namesecuritybypass_risklevel4)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN "+str(count_vulnibm_iot_namesecuritybypass_risklevel3)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN "+str(count_vulnibm_iot_namesecuritybypass_risklevel2)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN "+str(count_vulnibm_iot_namesecuritybypass_risklevel1)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN "+str(count_vulnibm_iot_namesecuritybypass_risklevel0)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_nameinformationdisclosure)+" VULNERABILIDADES EL NOMBRE INCLUYE INFORMATION DISCLOSURE, LAS ESTADÍSTICAS DE PUNTUACION BASE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_nameinformationdisclosure_risklevel10)+" VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
print("            -    EN  "+str(count_vulnibm_iot_nameinformationdisclosure_risklevel9)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN  "+str(count_vulnibm_iot_nameinformationdisclosure_risklevel8)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN  "+str(count_vulnibm_iot_nameinformationdisclosure_risklevel7)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN  "+str(count_vulnibm_iot_nameinformationdisclosure_risklevel6)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN "+str(count_vulnibm_iot_nameinformationdisclosure_risklevel5)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN "+str(count_vulnibm_iot_nameinformationdisclosure_risklevel4)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN "+str(count_vulnibm_iot_nameinformationdisclosure_risklevel3)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN "+str(count_vulnibm_iot_nameinformationdisclosure_risklevel2)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN "+str(count_vulnibm_iot_nameinformationdisclosure_risklevel1)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN "+str(count_vulnibm_iot_nameinformationdisclosure_risklevel0)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_namedenialofservice)+" VULNERABILIDADES EL NOMBRE INCLUYE DENIAL OF SERVICE, LAS ESTADÍSTICAS DE PUNTUACION BASE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_namedenialofservice_risklevel10)+" VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
print("            -    EN  "+str(count_vulnibm_iot_namedenialofservice_risklevel9)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN  "+str(count_vulnibm_iot_namedenialofservice_risklevel8)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN  "+str(count_vulnibm_iot_namedenialofservice_risklevel7)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN  "+str(count_vulnibm_iot_namedenialofservice_risklevel6)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN "+str(count_vulnibm_iot_namedenialofservice_risklevel5)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN "+str(count_vulnibm_iot_namedenialofservice_risklevel4)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN "+str(count_vulnibm_iot_namedenialofservice_risklevel3)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN "+str(count_vulnibm_iot_namedenialofservice_risklevel2)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN "+str(count_vulnibm_iot_namedenialofservice_risklevel1)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN "+str(count_vulnibm_iot_namedenialofservice_risklevel0)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_namecodeexecution)+" VULNERABILIDADES EL NOMBRE INCLUYE CODE EXECUTION, LAS ESTADÍSTICAS DE PUNTUACION BASE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_namecodeexecution_risklevel10)+" VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
print("            -    EN  "+str(count_vulnibm_iot_namecodeexecution_risklevel9)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN  "+str(count_vulnibm_iot_namecodeexecution_risklevel8)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN  "+str(count_vulnibm_iot_namecodeexecution_risklevel7)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN  "+str(count_vulnibm_iot_namecodeexecution_risklevel6)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN "+str(count_vulnibm_iot_namecodeexecution_risklevel5)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN "+str(count_vulnibm_iot_namecodeexecution_risklevel4)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN "+str(count_vulnibm_iot_namecodeexecution_risklevel3)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN "+str(count_vulnibm_iot_namecodeexecution_risklevel2)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN "+str(count_vulnibm_iot_namecodeexecution_risklevel1)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN "+str(count_vulnibm_iot_namecodeexecution_risklevel0)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_namemaninthemiddle)+" VULNERABILIDADES EL NOMBRE INCLUYE MAN IN THE MIDDLE, LAS ESTADÍSTICAS DE PUNTUACION BASE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_namemaninthemiddle_risklevel10)+" VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
print("            -    EN  "+str(count_vulnibm_iot_namemaninthemiddle_risklevel9)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN  "+str(count_vulnibm_iot_namemaninthemiddle_risklevel8)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN  "+str(count_vulnibm_iot_namemaninthemiddle_risklevel7)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN  "+str(count_vulnibm_iot_namemaninthemiddle_risklevel6)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN "+str(count_vulnibm_iot_namemaninthemiddle_risklevel5)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN "+str(count_vulnibm_iot_namemaninthemiddle_risklevel4)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN "+str(count_vulnibm_iot_namemaninthemiddle_risklevel3)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN "+str(count_vulnibm_iot_namemaninthemiddle_risklevel2)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN "+str(count_vulnibm_iot_namemaninthemiddle_risklevel1)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN "+str(count_vulnibm_iot_namemaninthemiddle_risklevel0)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_namesqlinjection)+" VULNERABILIDADES EL NOMBRE INCLUYE SQL INJECTION, LAS ESTADÍSTICAS DE PUNTUACION BASE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_namesqlinjection_risklevel10)+" VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
print("            -    EN  "+str(count_vulnibm_iot_namesqlinjection_risklevel9)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN  "+str(count_vulnibm_iot_namesqlinjection_risklevel8)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN  "+str(count_vulnibm_iot_namesqlinjection_risklevel7)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN  "+str(count_vulnibm_iot_namesqlinjection_risklevel6)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN "+str(count_vulnibm_iot_namesqlinjection_risklevel5)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN "+str(count_vulnibm_iot_namesqlinjection_risklevel4)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN "+str(count_vulnibm_iot_namesqlinjection_risklevel3)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN "+str(count_vulnibm_iot_namesqlinjection_risklevel2)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN "+str(count_vulnibm_iot_namesqlinjection_risklevel1)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN "+str(count_vulnibm_iot_namesqlinjection_risklevel0)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_namecrosssiterequestforgery)+" VULNERABILIDADES EL NOMBRE INCLUYE CROSS SITE REQUEST FORGERY, LAS ESTADÍSTICAS DE PUNTUACION BASE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_namecrosssiterequestforgery_risklevel10)+" VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
print("            -    EN  "+str(count_vulnibm_iot_namecrosssiterequestforgery_risklevel9)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN  "+str(count_vulnibm_iot_namecrosssiterequestforgery_risklevel8)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN  "+str(count_vulnibm_iot_namecrosssiterequestforgery_risklevel7)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN  "+str(count_vulnibm_iot_namecrosssiterequestforgery_risklevel6)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN "+str(count_vulnibm_iot_namecrosssiterequestforgery_risklevel5)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN "+str(count_vulnibm_iot_namecrosssiterequestforgery_risklevel4)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN "+str(count_vulnibm_iot_namecrosssiterequestforgery_risklevel3)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN "+str(count_vulnibm_iot_namecrosssiterequestforgery_risklevel2)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN "+str(count_vulnibm_iot_namecrosssiterequestforgery_risklevel1)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN "+str(count_vulnibm_iot_namecrosssiterequestforgery_risklevel0)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_namemoduleexecution)+" VULNERABILIDADES EL NOMBRE INCLUYE MODULE EXECUTION, LAS ESTADÍSTICAS DE PUNTUACION BASE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_namemoduleexecution_risklevel10)+" VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
print("            -    EN  "+str(count_vulnibm_iot_namemoduleexecution_risklevel9)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN  "+str(count_vulnibm_iot_namemoduleexecution_risklevel8)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN  "+str(count_vulnibm_iot_namemoduleexecution_risklevel7)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN  "+str(count_vulnibm_iot_namemoduleexecution_risklevel6)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN "+str(count_vulnibm_iot_namemoduleexecution_risklevel5)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN "+str(count_vulnibm_iot_namemoduleexecution_risklevel4)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN "+str(count_vulnibm_iot_namemoduleexecution_risklevel3)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN "+str(count_vulnibm_iot_namemoduleexecution_risklevel2)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN "+str(count_vulnibm_iot_namemoduleexecution_risklevel1)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN "+str(count_vulnibm_iot_namemoduleexecution_risklevel0)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_namebufferoverflow)+" VULNERABILIDADES EL NOMBRE INCLUYE BUFFER OVERFLOW, LAS ESTADÍSTICAS DE PUNTUACION BASE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_namebufferoverflow_risklevel10)+" VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
print("            -    EN  "+str(count_vulnibm_iot_namebufferoverflow_risklevel9)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN  "+str(count_vulnibm_iot_namebufferoverflow_risklevel8)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN  "+str(count_vulnibm_iot_namebufferoverflow_risklevel7)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN  "+str(count_vulnibm_iot_namebufferoverflow_risklevel6)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN "+str(count_vulnibm_iot_namebufferoverflow_risklevel5)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN "+str(count_vulnibm_iot_namebufferoverflow_risklevel4)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN "+str(count_vulnibm_iot_namebufferoverflow_risklevel3)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN "+str(count_vulnibm_iot_namebufferoverflow_risklevel2)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN "+str(count_vulnibm_iot_namebufferoverflow_risklevel1)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN "+str(count_vulnibm_iot_namebufferoverflow_risklevel0)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_namecommandexecution)+" VULNERABILIDADES EL NOMBRE INCLUYE COMMAND EXECUTION, LAS ESTADÍSTICAS DE PUNTUACION BASE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_namecommandexecution_risklevel10)+" VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
print("            -    EN  "+str(count_vulnibm_iot_namecommandexecution_risklevel9)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN  "+str(count_vulnibm_iot_namecommandexecution_risklevel8)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN  "+str(count_vulnibm_iot_namecommandexecution_risklevel7)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN  "+str(count_vulnibm_iot_namecommandexecution_risklevel6)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN "+str(count_vulnibm_iot_namecommandexecution_risklevel5)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN "+str(count_vulnibm_iot_namecommandexecution_risklevel4)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN "+str(count_vulnibm_iot_namecommandexecution_risklevel3)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN "+str(count_vulnibm_iot_namecommandexecution_risklevel2)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN "+str(count_vulnibm_iot_namecommandexecution_risklevel1)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN "+str(count_vulnibm_iot_namecommandexecution_risklevel0)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_namespoofing)+" VULNERABILIDADES EL NOMBRE INCLUYE SPOOFING, LAS ESTADÍSTICAS DE PUNTUACION BASE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_namespoofing_risklevel10)+" VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
print("            -    EN  "+str(count_vulnibm_iot_namespoofing_risklevel9)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN  "+str(count_vulnibm_iot_namespoofing_risklevel8)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN  "+str(count_vulnibm_iot_namespoofing_risklevel7)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN  "+str(count_vulnibm_iot_namespoofing_risklevel6)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN "+str(count_vulnibm_iot_namespoofing_risklevel5)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN "+str(count_vulnibm_iot_namespoofing_risklevel4)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN "+str(count_vulnibm_iot_namespoofing_risklevel3)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN "+str(count_vulnibm_iot_namespoofing_risklevel2)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN "+str(count_vulnibm_iot_namespoofing_risklevel1)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN "+str(count_vulnibm_iot_namespoofing_risklevel0)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_nameclickjacking)+" VULNERABILIDADES EL NOMBRE INCLUYE CLICKJACKING, LAS ESTADÍSTICAS DE PUNTUACION BASE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_nameclickjacking_risklevel10)+" VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
print("            -    EN  "+str(count_vulnibm_iot_nameclickjacking_risklevel9)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN  "+str(count_vulnibm_iot_nameclickjacking_risklevel8)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN  "+str(count_vulnibm_iot_nameclickjacking_risklevel7)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN  "+str(count_vulnibm_iot_nameclickjacking_risklevel6)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN "+str(count_vulnibm_iot_nameclickjacking_risklevel5)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN "+str(count_vulnibm_iot_nameclickjacking_risklevel4)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN "+str(count_vulnibm_iot_nameclickjacking_risklevel3)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN "+str(count_vulnibm_iot_nameclickjacking_risklevel2)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN "+str(count_vulnibm_iot_nameclickjacking_risklevel1)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN "+str(count_vulnibm_iot_nameclickjacking_risklevel0)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_namehijacking)+" VULNERABILIDADES EL NOMBRE INCLUYE HIJACKING, LAS ESTADÍSTICAS DE PUNTUACION BASE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_namehijacking_risklevel10)+" VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
print("            -    EN  "+str(count_vulnibm_iot_namehijacking_risklevel9)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN  "+str(count_vulnibm_iot_namehijacking_risklevel8)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN  "+str(count_vulnibm_iot_namehijacking_risklevel7)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN  "+str(count_vulnibm_iot_namehijacking_risklevel6)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN "+str(count_vulnibm_iot_namehijacking_risklevel5)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN "+str(count_vulnibm_iot_namehijacking_risklevel4)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN "+str(count_vulnibm_iot_namehijacking_risklevel3)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN "+str(count_vulnibm_iot_namehijacking_risklevel2)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN "+str(count_vulnibm_iot_namehijacking_risklevel1)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN "+str(count_vulnibm_iot_namehijacking_risklevel0)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_namefileinclude)+" VULNERABILIDADES EL NOMBRE INCLUYE FILEINCLUDE, LAS ESTADÍSTICAS DE PUNTUACION BASE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_namefileinclude_risklevel10)+" VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
print("            -    EN  "+str(count_vulnibm_iot_namefileinclude_risklevel9)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN  "+str(count_vulnibm_iot_namefileinclude_risklevel8)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN  "+str(count_vulnibm_iot_namefileinclude_risklevel7)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN  "+str(count_vulnibm_iot_namefileinclude_risklevel6)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN "+str(count_vulnibm_iot_namefileinclude_risklevel5)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN "+str(count_vulnibm_iot_namefileinclude_risklevel4)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN "+str(count_vulnibm_iot_namefileinclude_risklevel3)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN "+str(count_vulnibm_iot_namefileinclude_risklevel2)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN "+str(count_vulnibm_iot_namefileinclude_risklevel1)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN "+str(count_vulnibm_iot_namefileinclude_risklevel0)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_namebruteforce)+" VULNERABILIDADES EL NOMBRE INCLUYE BRUTEFORCE, LAS ESTADÍSTICAS DE PUNTUACION BASE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_namebruteforce_risklevel10)+" VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
print("            -    EN  "+str(count_vulnibm_iot_namebruteforce_risklevel9)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN  "+str(count_vulnibm_iot_namebruteforce_risklevel8)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN  "+str(count_vulnibm_iot_namebruteforce_risklevel7)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN  "+str(count_vulnibm_iot_namebruteforce_risklevel6)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN "+str(count_vulnibm_iot_namebruteforce_risklevel5)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN "+str(count_vulnibm_iot_namebruteforce_risklevel4)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN "+str(count_vulnibm_iot_namebruteforce_risklevel3)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN "+str(count_vulnibm_iot_namebruteforce_risklevel2)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN "+str(count_vulnibm_iot_namebruteforce_risklevel1)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN "+str(count_vulnibm_iot_namebruteforce_risklevel0)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_namefileupload)+" VULNERABILIDADES EL NOMBRE INCLUYE FILE UPLOAD, LAS ESTADÍSTICAS DE PUNTUACION BASE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_namefileupload_risklevel10)+" VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
print("            -    EN  "+str(count_vulnibm_iot_namefileupload_risklevel9)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN  "+str(count_vulnibm_iot_namefileupload_risklevel8)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN  "+str(count_vulnibm_iot_namefileupload_risklevel7)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN  "+str(count_vulnibm_iot_namefileupload_risklevel6)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN "+str(count_vulnibm_iot_namefileupload_risklevel5)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN "+str(count_vulnibm_iot_namefileupload_risklevel4)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN "+str(count_vulnibm_iot_namefileupload_risklevel3)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN "+str(count_vulnibm_iot_namefileupload_risklevel2)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN "+str(count_vulnibm_iot_namefileupload_risklevel1)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN "+str(count_vulnibm_iot_namefileupload_risklevel0)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_nameheaderinjection)+" VULNERABILIDADES EL NOMBRE INCLUYE HEADER INJECTION, LAS ESTADÍSTICAS DE PUNTUACION BASE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_nameheaderinjection_risklevel10)+" VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
print("            -    EN  "+str(count_vulnibm_iot_nameheaderinjection_risklevel9)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN  "+str(count_vulnibm_iot_nameheaderinjection_risklevel8)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN  "+str(count_vulnibm_iot_nameheaderinjection_risklevel7)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN  "+str(count_vulnibm_iot_nameheaderinjection_risklevel6)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN "+str(count_vulnibm_iot_nameheaderinjection_risklevel5)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN "+str(count_vulnibm_iot_nameheaderinjection_risklevel4)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN "+str(count_vulnibm_iot_nameheaderinjection_risklevel3)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN "+str(count_vulnibm_iot_nameheaderinjection_risklevel2)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN "+str(count_vulnibm_iot_nameheaderinjection_risklevel1)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN "+str(count_vulnibm_iot_nameheaderinjection_risklevel0)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_nametampering)+" VULNERABILIDADES EL NOMBRE INCLUYE TAMPERING, LAS ESTADÍSTICAS DE PUNTUACION BASE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_nametampering_risklevel10)+" VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
print("            -    EN  "+str(count_vulnibm_iot_nametampering_risklevel9)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN  "+str(count_vulnibm_iot_nametampering_risklevel8)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN  "+str(count_vulnibm_iot_nametampering_risklevel7)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN  "+str(count_vulnibm_iot_nametampering_risklevel6)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN "+str(count_vulnibm_iot_nametampering_risklevel5)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN "+str(count_vulnibm_iot_nametampering_risklevel4)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN "+str(count_vulnibm_iot_nametampering_risklevel3)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN "+str(count_vulnibm_iot_nametampering_risklevel2)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN "+str(count_vulnibm_iot_nametampering_risklevel1)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN "+str(count_vulnibm_iot_nametampering_risklevel0)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_nameanother)+" VULNERABILIDADES EL NOMBRE INCLUYE OTRA CADENA, LAS ESTADÍSTICAS DE PUNTUACION BASE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_nameanother_risklevel10)+" VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
print("            -    EN  "+str(count_vulnibm_iot_nameanother_risklevel9)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN  "+str(count_vulnibm_iot_nameanother_risklevel8)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN  "+str(count_vulnibm_iot_nameanother_risklevel7)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN  "+str(count_vulnibm_iot_nameanother_risklevel6)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN "+str(count_vulnibm_iot_nameanother_risklevel5)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN "+str(count_vulnibm_iot_nameanother_risklevel4)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN "+str(count_vulnibm_iot_nameanother_risklevel3)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN "+str(count_vulnibm_iot_nameanother_risklevel2)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN "+str(count_vulnibm_iot_nameanother_risklevel1)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN "+str(count_vulnibm_iot_nameanother_risklevel0)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("\n")





print("*********************PORCENTAJE NOMBRE/PUNTUACION BASE OBJETOS DE TIPO VULNERABILIDAD IBM PARTE IOT*********************")
print("\n")                            
print("\n")
print(" DE UN TOTAL DE "+str(count_vulnibm_iot_names)+" VULNERABILIDADES :\n") 
print("\n")
print("   - LOS PORCENTAJES DE VALORES DE NOMBRE SON LOS SIGUIENTES:  \n")
print("      -    EN EL  "+str(float(((count_vulnibm_iot_namepathtraversal*100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE PATH TRAVERSAL, LOS PORCENTAJES DE PUNTUACION BASE SON LOS SIGUIENTES :  \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namepathtraversal_risklevel10*100)/count_vulnibm_iot_namepathtraversal)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namepathtraversal_risklevel9*100)/count_vulnibm_iot_namepathtraversal)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namepathtraversal_risklevel8*100)/count_vulnibm_iot_namepathtraversal)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namepathtraversal_risklevel7*100)/count_vulnibm_iot_namepathtraversal)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namepathtraversal_risklevel6*100)/count_vulnibm_iot_namepathtraversal)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_namepathtraversal_risklevel5*100)/count_vulnibm_iot_namepathtraversal)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_namepathtraversal_risklevel4*100)/count_vulnibm_iot_namepathtraversal)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_namepathtraversal_risklevel3*100)/count_vulnibm_iot_namepathtraversal)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_namepathtraversal_risklevel2*100)/count_vulnibm_iot_namepathtraversal)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_namepathtraversal_risklevel1*100)/count_vulnibm_iot_namepathtraversal)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_namepathtraversal_risklevel0*100)/count_vulnibm_iot_namepathtraversal)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("            -    EL VALOR MEDIO DE PUNTUACION BASE ES  "+str(float(((count_vulnibm_iot_namepathtraversal_risklevel)/count_vulnibm_iot_namepathtraversal)))+"\n")
print("\n")
print("      -    EN EL  "+str(float(((count_vulnibm_iot_namedirectorytraversal*100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE DIRECTORY TRAVERSAL, LOS PORCENTAJES DE PUNTUACION BASE SON LOS SIGUIENTES :  \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namedirectorytraversal_risklevel10*100)/count_vulnibm_iot_namedirectorytraversal)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namedirectorytraversal_risklevel9*100)/count_vulnibm_iot_namedirectorytraversal)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namedirectorytraversal_risklevel8*100)/count_vulnibm_iot_namedirectorytraversal)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namedirectorytraversal_risklevel7*100)/count_vulnibm_iot_namedirectorytraversal)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namedirectorytraversal_risklevel6*100)/count_vulnibm_iot_namedirectorytraversal)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_namedirectorytraversal_risklevel5*100)/count_vulnibm_iot_namedirectorytraversal)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_namedirectorytraversal_risklevel4*100)/count_vulnibm_iot_namedirectorytraversal)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_namedirectorytraversal_risklevel3*100)/count_vulnibm_iot_namedirectorytraversal)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_namedirectorytraversal_risklevel2*100)/count_vulnibm_iot_namedirectorytraversal)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_namedirectorytraversal_risklevel1*100)/count_vulnibm_iot_namedirectorytraversal)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_namedirectorytraversal_risklevel0*100)/count_vulnibm_iot_namedirectorytraversal)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("            -    EL VALOR MEDIO DE PUNTUACION BASE ES  "+str(float(((count_vulnibm_iot_namedirectorytraversal_risklevel)/count_vulnibm_iot_namedirectorytraversal)))+"\n")
print("\n")
print("      -    EN EL  "+str(float(((count_vulnibm_iot_nameprivilegeescalation*100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE PRIVILEGE ESCALATION, LLOS PORCENTAJES DE PUNTUACION BASE SON LOS SIGUIENTES :  \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_nameprivilegeescalation_risklevel10*100)/count_vulnibm_iot_nameprivilegeescalation)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_nameprivilegeescalation_risklevel9*100)/count_vulnibm_iot_nameprivilegeescalation)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_nameprivilegeescalation_risklevel8*100)/count_vulnibm_iot_nameprivilegeescalation)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_nameprivilegeescalation_risklevel7*100)/count_vulnibm_iot_nameprivilegeescalation)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_nameprivilegeescalation_risklevel6*100)/count_vulnibm_iot_nameprivilegeescalation)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_nameprivilegeescalation_risklevel5*100)/count_vulnibm_iot_nameprivilegeescalation)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_nameprivilegeescalation_risklevel4*100)/count_vulnibm_iot_nameprivilegeescalation)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_nameprivilegeescalation_risklevel3*100)/count_vulnibm_iot_nameprivilegeescalation)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_nameprivilegeescalation_risklevel2*100)/count_vulnibm_iot_nameprivilegeescalation)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_nameprivilegeescalation_risklevel1*100)/count_vulnibm_iot_nameprivilegeescalation)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_nameprivilegeescalation_risklevel0*100)/count_vulnibm_iot_nameprivilegeescalation)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("            -    EL VALOR MEDIO DE PUNTUACION BASE ES  "+str(float(((count_vulnibm_iot_nameprivilegeescalation_risklevel)/count_vulnibm_iot_nameprivilegeescalation)))+"\n")
print("\n")
print("      -    EN EL  "+str(float(((count_vulnibm_iot_namecrosssitescripting*100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE CROSS SITE SCRIPTING, LOS PORCENTAJES DE PUNTUACION BASE SON LOS SIGUIENTES :  \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namecrosssitescripting_risklevel10*100)/count_vulnibm_iot_namecrosssitescripting)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namecrosssitescripting_risklevel9*100)/count_vulnibm_iot_namecrosssitescripting)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namecrosssitescripting_risklevel8*100)/count_vulnibm_iot_namecrosssitescripting)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namecrosssitescripting_risklevel7*100)/count_vulnibm_iot_namecrosssitescripting)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namecrosssitescripting_risklevel6*100)/count_vulnibm_iot_namecrosssitescripting)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_namecrosssitescripting_risklevel5*100)/count_vulnibm_iot_namecrosssitescripting)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_namecrosssitescripting_risklevel4*100)/count_vulnibm_iot_namecrosssitescripting)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_namecrosssitescripting_risklevel3*100)/count_vulnibm_iot_namecrosssitescripting)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_namecrosssitescripting_risklevel2*100)/count_vulnibm_iot_namecrosssitescripting)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_namecrosssitescripting_risklevel1*100)/count_vulnibm_iot_namecrosssitescripting)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_namecrosssitescripting_risklevel0*100)/count_vulnibm_iot_namecrosssitescripting)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("            -    EL VALOR MEDIO DE PUNTUACION BASE ES  "+str(float(((count_vulnibm_iot_namecrosssitescripting_risklevel)/count_vulnibm_iot_namecrosssitescripting)))+"\n")
print("\n")
print("      -    EN EL  "+str(float(((count_vulnibm_iot_namesecuritybypass*100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE SECURITY BYPASS, LOS PORCENTAJES DE PUNTUACION BASE SON LOS SIGUIENTES :  \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namesecuritybypass_risklevel10*100)/count_vulnibm_iot_namesecuritybypass)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namesecuritybypass_risklevel9*100)/count_vulnibm_iot_namesecuritybypass)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namesecuritybypass_risklevel8*100)/count_vulnibm_iot_namesecuritybypass)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namesecuritybypass_risklevel7*100)/count_vulnibm_iot_namesecuritybypass)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namesecuritybypass_risklevel6*100)/count_vulnibm_iot_namesecuritybypass)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_namesecuritybypass_risklevel5*100)/count_vulnibm_iot_namesecuritybypass)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_namesecuritybypass_risklevel4*100)/count_vulnibm_iot_namesecuritybypass)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_namesecuritybypass_risklevel3*100)/count_vulnibm_iot_namesecuritybypass)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_namesecuritybypass_risklevel2*100)/count_vulnibm_iot_namesecuritybypass)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_namesecuritybypass_risklevel1*100)/count_vulnibm_iot_namesecuritybypass)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_namesecuritybypass_risklevel0*100)/count_vulnibm_iot_namesecuritybypass)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("            -    EL VALOR MEDIO DE PUNTUACION BASE ES  "+str(float(((count_vulnibm_iot_namesecuritybypass_risklevel)/count_vulnibm_iot_namesecuritybypass)))+"\n")
print("\n")
print("      -    EN EL  "+str(float(((count_vulnibm_iot_nameinformationdisclosure*100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE INFORMATION DISCLOSURE, LOS PORCENTAJES DE PUNTUACION BASE SON LOS SIGUIENTES :  \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_nameinformationdisclosure_risklevel10*100)/count_vulnibm_iot_nameinformationdisclosure)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_nameinformationdisclosure_risklevel9*100)/count_vulnibm_iot_nameinformationdisclosure)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_nameinformationdisclosure_risklevel8*100)/count_vulnibm_iot_nameinformationdisclosure)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_nameinformationdisclosure_risklevel7*100)/count_vulnibm_iot_nameinformationdisclosure)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_nameinformationdisclosure_risklevel6*100)/count_vulnibm_iot_nameinformationdisclosure)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_nameinformationdisclosure_risklevel5*100)/count_vulnibm_iot_nameinformationdisclosure)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_nameinformationdisclosure_risklevel4*100)/count_vulnibm_iot_nameinformationdisclosure)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_nameinformationdisclosure_risklevel3*100)/count_vulnibm_iot_nameinformationdisclosure)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_nameinformationdisclosure_risklevel2*100)/count_vulnibm_iot_nameinformationdisclosure)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_nameinformationdisclosure_risklevel1*100)/count_vulnibm_iot_nameinformationdisclosure)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_nameinformationdisclosure_risklevel0*100)/count_vulnibm_iot_nameinformationdisclosure)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("            -    EL VALOR MEDIO DE PUNTUACION BASE ES  "+str(float(((count_vulnibm_iot_nameinformationdisclosure_risklevel)/count_vulnibm_iot_nameinformationdisclosure)))+"\n")
print("\n")
print("      -    EN EL  "+str(float(((count_vulnibm_iot_namedenialofservice*100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE DENIAL OF SERVICE, LOS PORCENTAJES DE PUNTUACION BASE SON LOS SIGUIENTESS :  \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namedenialofservice_risklevel10*100)/count_vulnibm_iot_namedenialofservice)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namedenialofservice_risklevel9*100)/count_vulnibm_iot_namedenialofservice)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namedenialofservice_risklevel8*100)/count_vulnibm_iot_namedenialofservice)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namedenialofservice_risklevel7*100)/count_vulnibm_iot_namedenialofservice)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namedenialofservice_risklevel6*100)/count_vulnibm_iot_namedenialofservice)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_namedenialofservice_risklevel5*100)/count_vulnibm_iot_namedenialofservice)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_namedenialofservice_risklevel4*100)/count_vulnibm_iot_namedenialofservice)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_namedenialofservice_risklevel3*100)/count_vulnibm_iot_namedenialofservice)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_namedenialofservice_risklevel2*100)/count_vulnibm_iot_namedenialofservice)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_namedenialofservice_risklevel1*100)/count_vulnibm_iot_namedenialofservice)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_namedenialofservice_risklevel0*100)/count_vulnibm_iot_namedenialofservice)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("            -    EL VALOR MEDIO DE PUNTUACION BASE ES  "+str(float(((count_vulnibm_iot_namedenialofservice_risklevel)/count_vulnibm_iot_namedenialofservice)))+"\n")
print("\n")
print("      -    EN EL  "+str(float(((count_vulnibm_iot_namecodeexecution*100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE CODE EXECUTION, LOS PORCENTAJES DE PUNTUACION BASE SON LOS SIGUIENTES :  \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namecodeexecution_risklevel10*100)/count_vulnibm_iot_namecodeexecution)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namecodeexecution_risklevel9*100)/count_vulnibm_iot_namecodeexecution)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namecodeexecution_risklevel8*100)/count_vulnibm_iot_namecodeexecution)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namecodeexecution_risklevel7*100)/count_vulnibm_iot_namecodeexecution)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namecodeexecution_risklevel6*100)/count_vulnibm_iot_namecodeexecution)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_namecodeexecution_risklevel5*100)/count_vulnibm_iot_namecodeexecution)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_namecodeexecution_risklevel4*100)/count_vulnibm_iot_namecodeexecution)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_namecodeexecution_risklevel3*100)/count_vulnibm_iot_namecodeexecution)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_namecodeexecution_risklevel2*100)/count_vulnibm_iot_namecodeexecution)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_namecodeexecution_risklevel1*100)/count_vulnibm_iot_namecodeexecution)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_namecodeexecution_risklevel0*100)/count_vulnibm_iot_namecodeexecution)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("            -    EL VALOR MEDIO DE PUNTUACION BASE ES  "+str(float(((count_vulnibm_iot_namecodeexecution_risklevel)/count_vulnibm_iot_namecodeexecution)))+"\n")
print("\n")
print("      -    EN EL  "+str(float(((count_vulnibm_iot_namemaninthemiddle*100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE MAN IN THE MIDDLE, LOS PORCENTAJES DE PUNTUACION BASE SON LOS SIGUIENTES :  \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namemaninthemiddle_risklevel10*100)/count_vulnibm_iot_namemaninthemiddle)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namemaninthemiddle_risklevel9*100)/count_vulnibm_iot_namemaninthemiddle)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namemaninthemiddle_risklevel8*100)/count_vulnibm_iot_namemaninthemiddle)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namemaninthemiddle_risklevel7*100)/count_vulnibm_iot_namemaninthemiddle)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namemaninthemiddle_risklevel6*100)/count_vulnibm_iot_namemaninthemiddle)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_namemaninthemiddle_risklevel5*100)/count_vulnibm_iot_namemaninthemiddle)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_namemaninthemiddle_risklevel4*100)/count_vulnibm_iot_namemaninthemiddle)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_namemaninthemiddle_risklevel3*100)/count_vulnibm_iot_namemaninthemiddle)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_namemaninthemiddle_risklevel2*100)/count_vulnibm_iot_namemaninthemiddle)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_namemaninthemiddle_risklevel1*100)/count_vulnibm_iot_namemaninthemiddle)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_namemaninthemiddle_risklevel0*100)/count_vulnibm_iot_namemaninthemiddle)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("            -    EL VALOR MEDIO DE PUNTUACION BASE ES  "+str(float(((count_vulnibm_iot_namemaninthemiddle_risklevel)/count_vulnibm_iot_namemaninthemiddle)))+"\n")
print("\n")
print("      -    EN EL  "+str(float(((count_vulnibm_iot_namesqlinjection*100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE SQL INJECTION, LOS PORCENTAJES DE PUNTUACION BASE SON LOS SIGUIENTES :  \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namesqlinjection_risklevel10*100)/count_vulnibm_iot_namesqlinjection)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namesqlinjection_risklevel9*100)/count_vulnibm_iot_namesqlinjection)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namesqlinjection_risklevel8*100)/count_vulnibm_iot_namesqlinjection)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namesqlinjection_risklevel7*100)/count_vulnibm_iot_namesqlinjection)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namesqlinjection_risklevel6*100)/count_vulnibm_iot_namesqlinjection)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_namesqlinjection_risklevel5*100)/count_vulnibm_iot_namesqlinjection)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_namesqlinjection_risklevel4*100)/count_vulnibm_iot_namesqlinjection)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_namesqlinjection_risklevel3*100)/count_vulnibm_iot_namesqlinjection)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_namesqlinjection_risklevel2*100)/count_vulnibm_iot_namesqlinjection)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_namesqlinjection_risklevel1*100)/count_vulnibm_iot_namesqlinjection)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_namesqlinjection_risklevel0*100)/count_vulnibm_iot_namesqlinjection)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("            -    EL VALOR MEDIO DE PUNTUACION BASE ES  "+str(float(((count_vulnibm_iot_namesqlinjection_risklevel)/count_vulnibm_iot_namesqlinjection)))+"\n")
print("\n")
print("      -    EN EL  "+str(float(((count_vulnibm_iot_namecrosssiterequestforgery*100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE CROSS SITE REQUEST FORGERY, LOS PORCENTAJES DE PUNTUACION BASE SON LOS SIGUIENTES :  \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namecrosssiterequestforgery_risklevel10*100)/count_vulnibm_iot_namecrosssiterequestforgery)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namecrosssiterequestforgery_risklevel9*100)/count_vulnibm_iot_namecrosssiterequestforgery)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namecrosssiterequestforgery_risklevel8*100)/count_vulnibm_iot_namecrosssiterequestforgery)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namecrosssiterequestforgery_risklevel7*100)/count_vulnibm_iot_namecrosssiterequestforgery)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namecrosssiterequestforgery_risklevel6*100)/count_vulnibm_iot_namecrosssiterequestforgery)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_namecrosssiterequestforgery_risklevel5*100)/count_vulnibm_iot_namecrosssiterequestforgery)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_namecrosssiterequestforgery_risklevel4*100)/count_vulnibm_iot_namecrosssiterequestforgery)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_namecrosssiterequestforgery_risklevel3*100)/count_vulnibm_iot_namecrosssiterequestforgery)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_namecrosssiterequestforgery_risklevel2*100)/count_vulnibm_iot_namecrosssiterequestforgery)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_namecrosssiterequestforgery_risklevel1*100)/count_vulnibm_iot_namecrosssiterequestforgery)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_namecrosssiterequestforgery_risklevel0*100)/count_vulnibm_iot_namecrosssiterequestforgery)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("            -    EL VALOR MEDIO DE PUNTUACION BASE ES  "+str(float(((count_vulnibm_iot_namecrosssiterequestforgery_risklevel)/count_vulnibm_iot_namecrosssiterequestforgery)))+"\n")
print("\n")
print("      -    EN EL  "+str(float(((count_vulnibm_iot_namemoduleexecution*100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE MODULE EXECUTION, LOS PORCENTAJES DE PUNTUACION BASE SON LOS SIGUIENTES :  \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namemoduleexecution_risklevel10*100)/count_vulnibm_iot_namemoduleexecution)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namemoduleexecution_risklevel9*100)/count_vulnibm_iot_namemoduleexecution)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namemoduleexecution_risklevel8*100)/count_vulnibm_iot_namemoduleexecution)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namemoduleexecution_risklevel7*100)/count_vulnibm_iot_namemoduleexecution)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namemoduleexecution_risklevel6*100)/count_vulnibm_iot_namemoduleexecution)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_namemoduleexecution_risklevel5*100)/count_vulnibm_iot_namemoduleexecution)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_namemoduleexecution_risklevel4*100)/count_vulnibm_iot_namemoduleexecution)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_namemoduleexecution_risklevel3*100)/count_vulnibm_iot_namemoduleexecution)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_namemoduleexecution_risklevel2*100)/count_vulnibm_iot_namemoduleexecution)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_namemoduleexecution_risklevel1*100)/count_vulnibm_iot_namemoduleexecution)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_namemoduleexecution_risklevel0*100)/count_vulnibm_iot_namemoduleexecution)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("            -    EL VALOR MEDIO DE PUNTUACION BASE ES  "+str(float(((count_vulnibm_iot_namemoduleexecution_risklevel)/count_vulnibm_iot_namemoduleexecution)))+"\n")
print("\n")
print("      -    EN EL  "+str(float(((count_vulnibm_iot_namebufferoverflow*100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE BUFFER OVERFLOW, LOS PORCENTAJES DE PUNTUACION BASE SON LOS SIGUIENTES :  \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namebufferoverflow_risklevel10*100)/count_vulnibm_iot_namebufferoverflow)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namebufferoverflow_risklevel9*100)/count_vulnibm_iot_namebufferoverflow)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namebufferoverflow_risklevel8*100)/count_vulnibm_iot_namebufferoverflow)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namebufferoverflow_risklevel7*100)/count_vulnibm_iot_namebufferoverflow)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namebufferoverflow_risklevel6*100)/count_vulnibm_iot_namebufferoverflow)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_namebufferoverflow_risklevel5*100)/count_vulnibm_iot_namebufferoverflow)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_namebufferoverflow_risklevel4*100)/count_vulnibm_iot_namebufferoverflow)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_namebufferoverflow_risklevel3*100)/count_vulnibm_iot_namebufferoverflow)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_namebufferoverflow_risklevel2*100)/count_vulnibm_iot_namebufferoverflow)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_namebufferoverflow_risklevel1*100)/count_vulnibm_iot_namebufferoverflow)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_namebufferoverflow_risklevel0*100)/count_vulnibm_iot_namebufferoverflow)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("            -    EL VALOR MEDIO DE PUNTUACION BASE ES  "+str(float(((count_vulnibm_iot_namebufferoverflow_risklevel)/count_vulnibm_iot_namebufferoverflow)))+"\n")
print("\n")
print("      -    EN EL  "+str(float(((count_vulnibm_iot_namecommandexecution*100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE COMMAND EXECUTION, LOS PORCENTAJES DE PUNTUACION BASE SON LOS SIGUIENTES :  \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namecommandexecution_risklevel10*100)/count_vulnibm_iot_namecommandexecution)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namecommandexecution_risklevel9*100)/count_vulnibm_iot_namecommandexecution)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namecommandexecution_risklevel8*100)/count_vulnibm_iot_namecommandexecution)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namecommandexecution_risklevel7*100)/count_vulnibm_iot_namecommandexecution)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namecommandexecution_risklevel6*100)/count_vulnibm_iot_namecommandexecution)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_namecommandexecution_risklevel5*100)/count_vulnibm_iot_namecommandexecution)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_namecommandexecution_risklevel4*100)/count_vulnibm_iot_namecommandexecution)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_namecommandexecution_risklevel3*100)/count_vulnibm_iot_namecommandexecution)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_namecommandexecution_risklevel2*100)/count_vulnibm_iot_namecommandexecution)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_namecommandexecution_risklevel1*100)/count_vulnibm_iot_namecommandexecution)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_namecommandexecution_risklevel0*100)/count_vulnibm_iot_namecommandexecution)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("            -    EL VALOR MEDIO DE PUNTUACION BASE ES  "+str(float(((count_vulnibm_iot_namecommandexecution_risklevel)/count_vulnibm_iot_namecommandexecution)))+"\n")
print("\n")
print("      -    EN EL  "+str(float(((count_vulnibm_iot_namespoofing*100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE SPOOFING, LOS PORCENTAJES DE PUNTUACION BASE SON LOS SIGUIENTES :  \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namespoofing_risklevel10*100)/count_vulnibm_iot_namespoofing)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namespoofing_risklevel9*100)/count_vulnibm_iot_namespoofing)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namespoofing_risklevel8*100)/count_vulnibm_iot_namespoofing)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namespoofing_risklevel7*100)/count_vulnibm_iot_namespoofing)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namespoofing_risklevel6*100)/count_vulnibm_iot_namespoofing)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_namespoofing_risklevel5*100)/count_vulnibm_iot_namespoofing)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_namespoofing_risklevel4*100)/count_vulnibm_iot_namespoofing)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_namespoofing_risklevel3*100)/count_vulnibm_iot_namespoofing)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_namespoofing_risklevel2*100)/count_vulnibm_iot_namespoofing)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_namespoofing_risklevel1*100)/count_vulnibm_iot_namespoofing)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_namespoofing_risklevel0*100)/count_vulnibm_iot_namespoofing)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("            -    EL VALOR MEDIO DE PUNTUACION BASE ES  "+str(float(((count_vulnibm_iot_namespoofing_risklevel)/count_vulnibm_iot_namespoofing)))+"\n")
print("\n")
print("      -    EN EL  "+str(float(((count_vulnibm_iot_nameclickjacking*100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE CLICKJACKING, LOS PORCENTAJES DE PUNTUACION BASE SON LOS SIGUIENTES :  \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_nameclickjacking_risklevel10*100)/count_vulnibm_iot_nameclickjacking)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_nameclickjacking_risklevel9*100)/count_vulnibm_iot_nameclickjacking)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_nameclickjacking_risklevel8*100)/count_vulnibm_iot_nameclickjacking)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_nameclickjacking_risklevel7*100)/count_vulnibm_iot_nameclickjacking)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_nameclickjacking_risklevel6*100)/count_vulnibm_iot_nameclickjacking)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_nameclickjacking_risklevel5*100)/count_vulnibm_iot_nameclickjacking)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_nameclickjacking_risklevel4*100)/count_vulnibm_iot_nameclickjacking)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_nameclickjacking_risklevel3*100)/count_vulnibm_iot_nameclickjacking)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_nameclickjacking_risklevel2*100)/count_vulnibm_iot_nameclickjacking)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_nameclickjacking_risklevel1*100)/count_vulnibm_iot_nameclickjacking)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_nameclickjacking_risklevel0*100)/count_vulnibm_iot_nameclickjacking)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("            -    EL VALOR MEDIO DE PUNTUACION BASE ES  "+str(float(((count_vulnibm_iot_nameclickjacking_risklevel)/count_vulnibm_iot_nameclickjacking)))+"\n")
print("\n")
print("      -    EN EL  "+str(float(((count_vulnibm_iot_namehijacking*100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE HIJACKING, LOS PORCENTAJES DE PUNTUACION BASE SON LOS SIGUIENTES :  \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namehijacking_risklevel10*100)/count_vulnibm_iot_namehijacking)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namehijacking_risklevel9*100)/count_vulnibm_iot_namehijacking)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namehijacking_risklevel8*100)/count_vulnibm_iot_namehijacking)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namehijacking_risklevel7*100)/count_vulnibm_iot_namehijacking)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namehijacking_risklevel6*100)/count_vulnibm_iot_namehijacking)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_namehijacking_risklevel5*100)/count_vulnibm_iot_namehijacking)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_namehijacking_risklevel4*100)/count_vulnibm_iot_namehijacking)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_namehijacking_risklevel3*100)/count_vulnibm_iot_namehijacking)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_namehijacking_risklevel2*100)/count_vulnibm_iot_namehijacking)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_namehijacking_risklevel1*100)/count_vulnibm_iot_namehijacking)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_namehijacking_risklevel0*100)/count_vulnibm_iot_namehijacking)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("            -    EL VALOR MEDIO DE PUNTUACION BASE ES  "+str(float(((count_vulnibm_iot_namehijacking_risklevel)/count_vulnibm_iot_namehijacking)))+"\n")
print("\n")
print("      -    EN EL  "+str(float(((count_vulnibm_iot_namefileinclude*100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE FILEINCLUDE, LOS PORCENTAJES DE PUNTUACION BASE SON LOS SIGUIENTES :  \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namefileinclude_risklevel10*100)/count_vulnibm_iot_namefileinclude)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namefileinclude_risklevel9*100)/count_vulnibm_iot_namefileinclude)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namefileinclude_risklevel8*100)/count_vulnibm_iot_namefileinclude)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namefileinclude_risklevel7*100)/count_vulnibm_iot_namefileinclude)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namefileinclude_risklevel6*100)/count_vulnibm_iot_namefileinclude)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_namefileinclude_risklevel5*100)/count_vulnibm_iot_namefileinclude)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_namefileinclude_risklevel4*100)/count_vulnibm_iot_namefileinclude)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_namefileinclude_risklevel3*100)/count_vulnibm_iot_namefileinclude)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_namefileinclude_risklevel2*100)/count_vulnibm_iot_namefileinclude)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_namefileinclude_risklevel1*100)/count_vulnibm_iot_namefileinclude)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_namefileinclude_risklevel0*100)/count_vulnibm_iot_namefileinclude)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("            -    EL VALOR MEDIO DE PUNTUACION BASE ES  "+str(float(((count_vulnibm_iot_namefileinclude_risklevel)/count_vulnibm_iot_namefileinclude)))+"\n")
print("\n")
print("      -    EN EL  "+str(float(((count_vulnibm_iot_namebruteforce*100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE BRUTEFORCE, LOS PORCENTAJES DE PUNTUACION BASE SON LOS SIGUIENTES :  \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namebruteforce_risklevel10*100)/count_vulnibm_iot_namebruteforce)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namebruteforce_risklevel9*100)/count_vulnibm_iot_namebruteforce)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namebruteforce_risklevel8*100)/count_vulnibm_iot_namebruteforce)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namebruteforce_risklevel7*100)/count_vulnibm_iot_namebruteforce)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namebruteforce_risklevel6*100)/count_vulnibm_iot_namebruteforce)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_namebruteforce_risklevel5*100)/count_vulnibm_iot_namebruteforce)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_namebruteforce_risklevel4*100)/count_vulnibm_iot_namebruteforce)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_namebruteforce_risklevel3*100)/count_vulnibm_iot_namebruteforce)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_namebruteforce_risklevel2*100)/count_vulnibm_iot_namebruteforce)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_namebruteforce_risklevel1*100)/count_vulnibm_iot_namebruteforce)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_namebruteforce_risklevel0*100)/count_vulnibm_iot_namebruteforce)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("            -    EL VALOR MEDIO DE PUNTUACION BASE ES  "+str(float(((count_vulnibm_iot_namebruteforce_risklevel)/count_vulnibm_iot_namebruteforce)))+"\n")
print("\n")
print("      -    EN EL  "+str(float(((count_vulnibm_iot_namefileupload*100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE FILE UPLOAD, LOS PORCENTAJES DE PUNTUACION BASE SON LOS SIGUIENTES :  \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namefileupload_risklevel10*100)/count_vulnibm_iot_namefileupload)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namefileupload_risklevel9*100)/count_vulnibm_iot_namefileupload)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namefileupload_risklevel8*100)/count_vulnibm_iot_namefileupload)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namefileupload_risklevel7*100)/count_vulnibm_iot_namefileupload)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namefileupload_risklevel6*100)/count_vulnibm_iot_namefileupload)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_namefileupload_risklevel5*100)/count_vulnibm_iot_namefileupload)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_namefileupload_risklevel4*100)/count_vulnibm_iot_namefileupload)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_namefileupload_risklevel3*100)/count_vulnibm_iot_namefileupload)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_namefileupload_risklevel2*100)/count_vulnibm_iot_namefileupload)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_namefileupload_risklevel1*100)/count_vulnibm_iot_namefileupload)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_namefileupload_risklevel0*100)/count_vulnibm_iot_namefileupload)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("            -    EL VALOR MEDIO DE PUNTUACION BASE ES  "+str(float(((count_vulnibm_iot_namefileupload_risklevel)/count_vulnibm_iot_namefileupload)))+"\n")
print("\n")
if(count_vulnibm_iot_nameheaderinjection>0):
    print("      -    EN EL  "+str(float(((count_vulnibm_iot_nameheaderinjection*100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE HEADER INJECTION, LOS PORCENTAJES DE PUNTUACION BASE SON LOS SIGUIENTES :  \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_nameheaderinjection_risklevel10*100)/count_vulnibm_iot_nameheaderinjection)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_nameheaderinjection_risklevel9*100)/count_vulnibm_iot_nameheaderinjection)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_nameheaderinjection_risklevel8*100)/count_vulnibm_iot_nameheaderinjection)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_nameheaderinjection_risklevel7*100)/count_vulnibm_iot_nameheaderinjection)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_nameheaderinjection_risklevel6*100)/count_vulnibm_iot_nameheaderinjection)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_iot_nameheaderinjection_risklevel5*100)/count_vulnibm_iot_nameheaderinjection)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_iot_nameheaderinjection_risklevel4*100)/count_vulnibm_iot_nameheaderinjection)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_iot_nameheaderinjection_risklevel3*100)/count_vulnibm_iot_nameheaderinjection)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_iot_nameheaderinjection_risklevel2*100)/count_vulnibm_iot_nameheaderinjection)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_iot_nameheaderinjection_risklevel1*100)/count_vulnibm_iot_nameheaderinjection)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_iot_nameheaderinjection_risklevel0*100)/count_vulnibm_iot_nameheaderinjection)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
    print("            -    EL VALOR MEDIO DE PUNTUACION BASE ES  "+str(float(((count_vulnibm_iot_nameheaderinjection_risklevel)/count_vulnibm_iot_nameheaderinjection)))+"\n")
    print("\n")
if(count_vulnibm_iot_nametampering>0):
    print("      -    EN EL  "+str(float(((count_vulnibm_iot_nametampering*100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE TAMPERING, LOS PORCENTAJES DE PUNTUACION BASE SON LOS SIGUIENTES :  \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_nametampering_risklevel10*100)/count_vulnibm_iot_nametampering)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_nametampering_risklevel9*100)/count_vulnibm_iot_nametampering)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_nametampering_risklevel8*100)/count_vulnibm_iot_nametampering)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_nametampering_risklevel7*100)/count_vulnibm_iot_nametampering)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_nametampering_risklevel6*100)/count_vulnibm_iot_nametampering)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_iot_nametampering_risklevel5*100)/count_vulnibm_iot_nametampering)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_iot_nametampering_risklevel4*100)/count_vulnibm_iot_nametampering)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_iot_nametampering_risklevel3*100)/count_vulnibm_iot_nametampering)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_iot_nametampering_risklevel2*100)/count_vulnibm_iot_nametampering)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_iot_nametampering_risklevel1*100)/count_vulnibm_iot_nametampering)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_iot_nametampering_risklevel0*100)/count_vulnibm_iot_nametampering)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
    print("            -    EL VALOR MEDIO DE PUNTUACION BASE ES  "+str(float(((count_vulnibm_iot_nametampering_risklevel)/count_vulnibm_iot_nametampering)))+"\n")
    print("\n")
print("      -    EN EL  "+str(float(((count_vulnibm_iot_nameanother*100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE OTRA CADENA, LOS PORCENTAJES DE PUNTUACION BASE SON LOS SIGUIENTES :  \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_nameanother_risklevel10*100)/count_vulnibm_iot_nameanother)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_nameanother_risklevel9*100)/count_vulnibm_iot_nameanother)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_nameanother_risklevel8*100)/count_vulnibm_iot_nameanother)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_nameanother_risklevel7*100)/count_vulnibm_iot_nameanother)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_nameanother_risklevel6*100)/count_vulnibm_iot_nameanother)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_nameanother_risklevel5*100)/count_vulnibm_iot_nameanother)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_nameanother_risklevel4*100)/count_vulnibm_iot_nameanother)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_nameanother_risklevel3*100)/count_vulnibm_iot_nameanother)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_nameanother_risklevel2*100)/count_vulnibm_iot_nameanother)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_nameanother_risklevel1*100)/count_vulnibm_iot_nameanother)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN EL "+str(float(((count_vulnibm_iot_nameanother_risklevel0*100)/count_vulnibm_iot_nameanother)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("            -    EL VALOR MEDIO DE PUNTUACION BASE ES  "+str(float(((count_vulnibm_iot_nameanother_risklevel)/count_vulnibm_iot_nameanother)))+"\n")
print("\n")
















#Abro los ficheros con los que voy a tratar




df_vulnibm_sh = pd.read_excel('vulnerabilidades_ibm_smart_home_2023.xlsx')
#Contador de valores total de name
count_vulnibm_sh_names=0
#Variable que almacena el contador de valor de nombre concreto
count_vulnibm_sh_namepathtraversal=0
#Variable que almacena la puntuacion de  PUNTUACION BASE para posteriormente calcular la media del valor de PUNTUACION BASE
count_vulnibm_sh_namepathtraversal_risklevel=0
#Variables que almacenan el contador de PUNTUACION BASE segun valor de nombre concreto
count_vulnibm_sh_namepathtraversal_risklevel10=0
count_vulnibm_sh_namepathtraversal_risklevel9=0
count_vulnibm_sh_namepathtraversal_risklevel8=0
count_vulnibm_sh_namepathtraversal_risklevel7=0
count_vulnibm_sh_namepathtraversal_risklevel6=0
count_vulnibm_sh_namepathtraversal_risklevel5=0
count_vulnibm_sh_namepathtraversal_risklevel4=0
count_vulnibm_sh_namepathtraversal_risklevel3=0
count_vulnibm_sh_namepathtraversal_risklevel2=0
count_vulnibm_sh_namepathtraversal_risklevel1=0
count_vulnibm_sh_namepathtraversal_risklevel0=0



count_vulnibm_sh_namedirectorytraversal=0
count_vulnibm_sh_namedirectorytraversal_risklevel=0
count_vulnibm_sh_namedirectorytraversal_risklevel10=0
count_vulnibm_sh_namedirectorytraversal_risklevel9=0
count_vulnibm_sh_namedirectorytraversal_risklevel8=0
count_vulnibm_sh_namedirectorytraversal_risklevel7=0
count_vulnibm_sh_namedirectorytraversal_risklevel6=0
count_vulnibm_sh_namedirectorytraversal_risklevel5=0
count_vulnibm_sh_namedirectorytraversal_risklevel4=0
count_vulnibm_sh_namedirectorytraversal_risklevel3=0
count_vulnibm_sh_namedirectorytraversal_risklevel2=0
count_vulnibm_sh_namedirectorytraversal_risklevel1=0
count_vulnibm_sh_namedirectorytraversal_risklevel0=0


count_vulnibm_sh_nameprivilegeescalation=0
count_vulnibm_sh_nameprivilegeescalation_risklevel=0
count_vulnibm_sh_nameprivilegeescalation_risklevel10=0
count_vulnibm_sh_nameprivilegeescalation_risklevel9=0
count_vulnibm_sh_nameprivilegeescalation_risklevel8=0
count_vulnibm_sh_nameprivilegeescalation_risklevel7=0
count_vulnibm_sh_nameprivilegeescalation_risklevel6=0
count_vulnibm_sh_nameprivilegeescalation_risklevel5=0
count_vulnibm_sh_nameprivilegeescalation_risklevel4=0
count_vulnibm_sh_nameprivilegeescalation_risklevel3=0
count_vulnibm_sh_nameprivilegeescalation_risklevel2=0
count_vulnibm_sh_nameprivilegeescalation_risklevel1=0
count_vulnibm_sh_nameprivilegeescalation_risklevel0=0

count_vulnibm_sh_namecrosssitescripting=0
count_vulnibm_sh_namecrosssitescripting_risklevel=0
count_vulnibm_sh_namecrosssitescripting_risklevel10=0
count_vulnibm_sh_namecrosssitescripting_risklevel9=0
count_vulnibm_sh_namecrosssitescripting_risklevel8=0
count_vulnibm_sh_namecrosssitescripting_risklevel7=0
count_vulnibm_sh_namecrosssitescripting_risklevel6=0
count_vulnibm_sh_namecrosssitescripting_risklevel5=0
count_vulnibm_sh_namecrosssitescripting_risklevel4=0
count_vulnibm_sh_namecrosssitescripting_risklevel3=0
count_vulnibm_sh_namecrosssitescripting_risklevel2=0
count_vulnibm_sh_namecrosssitescripting_risklevel1=0
count_vulnibm_sh_namecrosssitescripting_risklevel0=0


count_vulnibm_sh_namesecuritybypass=0
count_vulnibm_sh_namesecuritybypass_risklevel=0
count_vulnibm_sh_namesecuritybypass_risklevel10=0
count_vulnibm_sh_namesecuritybypass_risklevel9=0
count_vulnibm_sh_namesecuritybypass_risklevel8=0
count_vulnibm_sh_namesecuritybypass_risklevel7=0
count_vulnibm_sh_namesecuritybypass_risklevel6=0
count_vulnibm_sh_namesecuritybypass_risklevel5=0
count_vulnibm_sh_namesecuritybypass_risklevel4=0
count_vulnibm_sh_namesecuritybypass_risklevel3=0
count_vulnibm_sh_namesecuritybypass_risklevel2=0
count_vulnibm_sh_namesecuritybypass_risklevel1=0
count_vulnibm_sh_namesecuritybypass_risklevel0=0


count_vulnibm_sh_nameinformationdisclosure=0
count_vulnibm_sh_nameinformationdisclosure_risklevel=0
count_vulnibm_sh_nameinformationdisclosure_risklevel10=0
count_vulnibm_sh_nameinformationdisclosure_risklevel9=0
count_vulnibm_sh_nameinformationdisclosure_risklevel8=0
count_vulnibm_sh_nameinformationdisclosure_risklevel7=0
count_vulnibm_sh_nameinformationdisclosure_risklevel6=0
count_vulnibm_sh_nameinformationdisclosure_risklevel5=0
count_vulnibm_sh_nameinformationdisclosure_risklevel4=0
count_vulnibm_sh_nameinformationdisclosure_risklevel3=0
count_vulnibm_sh_nameinformationdisclosure_risklevel2=0
count_vulnibm_sh_nameinformationdisclosure_risklevel1=0
count_vulnibm_sh_nameinformationdisclosure_risklevel0=0


count_vulnibm_sh_namedenialofservice=0
count_vulnibm_sh_namedenialofservice_risklevel=0
count_vulnibm_sh_namedenialofservice_risklevel10=0
count_vulnibm_sh_namedenialofservice_risklevel9=0
count_vulnibm_sh_namedenialofservice_risklevel8=0
count_vulnibm_sh_namedenialofservice_risklevel7=0
count_vulnibm_sh_namedenialofservice_risklevel6=0
count_vulnibm_sh_namedenialofservice_risklevel5=0
count_vulnibm_sh_namedenialofservice_risklevel4=0
count_vulnibm_sh_namedenialofservice_risklevel3=0
count_vulnibm_sh_namedenialofservice_risklevel2=0
count_vulnibm_sh_namedenialofservice_risklevel1=0
count_vulnibm_sh_namedenialofservice_risklevel0=0

count_vulnibm_sh_namecodeexecution=0
count_vulnibm_sh_namecodeexecution_risklevel=0
count_vulnibm_sh_namecodeexecution_risklevel10=0
count_vulnibm_sh_namecodeexecution_risklevel9=0
count_vulnibm_sh_namecodeexecution_risklevel8=0
count_vulnibm_sh_namecodeexecution_risklevel7=0
count_vulnibm_sh_namecodeexecution_risklevel6=0
count_vulnibm_sh_namecodeexecution_risklevel5=0
count_vulnibm_sh_namecodeexecution_risklevel4=0
count_vulnibm_sh_namecodeexecution_risklevel3=0
count_vulnibm_sh_namecodeexecution_risklevel2=0
count_vulnibm_sh_namecodeexecution_risklevel1=0
count_vulnibm_sh_namecodeexecution_risklevel0=0


count_vulnibm_sh_namemaninthemiddle=0
count_vulnibm_sh_namemaninthemiddle_risklevel=0
count_vulnibm_sh_namemaninthemiddle_risklevel10=0
count_vulnibm_sh_namemaninthemiddle_risklevel9=0
count_vulnibm_sh_namemaninthemiddle_risklevel8=0
count_vulnibm_sh_namemaninthemiddle_risklevel7=0
count_vulnibm_sh_namemaninthemiddle_risklevel6=0
count_vulnibm_sh_namemaninthemiddle_risklevel5=0
count_vulnibm_sh_namemaninthemiddle_risklevel4=0
count_vulnibm_sh_namemaninthemiddle_risklevel3=0
count_vulnibm_sh_namemaninthemiddle_risklevel2=0
count_vulnibm_sh_namemaninthemiddle_risklevel1=0
count_vulnibm_sh_namemaninthemiddle_risklevel0=0

count_vulnibm_sh_namesqlinjection=0
count_vulnibm_sh_namesqlinjection_risklevel=0
count_vulnibm_sh_namesqlinjection_risklevel10=0
count_vulnibm_sh_namesqlinjection_risklevel9=0
count_vulnibm_sh_namesqlinjection_risklevel8=0
count_vulnibm_sh_namesqlinjection_risklevel7=0
count_vulnibm_sh_namesqlinjection_risklevel6=0
count_vulnibm_sh_namesqlinjection_risklevel5=0
count_vulnibm_sh_namesqlinjection_risklevel4=0
count_vulnibm_sh_namesqlinjection_risklevel3=0
count_vulnibm_sh_namesqlinjection_risklevel2=0
count_vulnibm_sh_namesqlinjection_risklevel1=0
count_vulnibm_sh_namesqlinjection_risklevel0=0

count_vulnibm_sh_namecrosssiterequestforgery=0
count_vulnibm_sh_namecrosssiterequestforgery_risklevel=0
count_vulnibm_sh_namecrosssiterequestforgery_risklevel10=0
count_vulnibm_sh_namecrosssiterequestforgery_risklevel9=0
count_vulnibm_sh_namecrosssiterequestforgery_risklevel8=0
count_vulnibm_sh_namecrosssiterequestforgery_risklevel7=0
count_vulnibm_sh_namecrosssiterequestforgery_risklevel6=0
count_vulnibm_sh_namecrosssiterequestforgery_risklevel5=0
count_vulnibm_sh_namecrosssiterequestforgery_risklevel4=0
count_vulnibm_sh_namecrosssiterequestforgery_risklevel3=0
count_vulnibm_sh_namecrosssiterequestforgery_risklevel2=0
count_vulnibm_sh_namecrosssiterequestforgery_risklevel1=0
count_vulnibm_sh_namecrosssiterequestforgery_risklevel0=0

count_vulnibm_sh_namemoduleexecution=0
count_vulnibm_sh_namemoduleexecution_risklevel=0
count_vulnibm_sh_namemoduleexecution_risklevel10=0
count_vulnibm_sh_namemoduleexecution_risklevel9=0
count_vulnibm_sh_namemoduleexecution_risklevel8=0
count_vulnibm_sh_namemoduleexecution_risklevel7=0
count_vulnibm_sh_namemoduleexecution_risklevel6=0
count_vulnibm_sh_namemoduleexecution_risklevel5=0
count_vulnibm_sh_namemoduleexecution_risklevel4=0
count_vulnibm_sh_namemoduleexecution_risklevel3=0
count_vulnibm_sh_namemoduleexecution_risklevel2=0
count_vulnibm_sh_namemoduleexecution_risklevel1=0
count_vulnibm_sh_namemoduleexecution_risklevel0=0

count_vulnibm_sh_namebufferoverflow=0
count_vulnibm_sh_namebufferoverflow_risklevel=0
count_vulnibm_sh_namebufferoverflow_risklevel10=0
count_vulnibm_sh_namebufferoverflow_risklevel9=0
count_vulnibm_sh_namebufferoverflow_risklevel8=0
count_vulnibm_sh_namebufferoverflow_risklevel7=0
count_vulnibm_sh_namebufferoverflow_risklevel6=0
count_vulnibm_sh_namebufferoverflow_risklevel5=0
count_vulnibm_sh_namebufferoverflow_risklevel4=0
count_vulnibm_sh_namebufferoverflow_risklevel3=0
count_vulnibm_sh_namebufferoverflow_risklevel2=0
count_vulnibm_sh_namebufferoverflow_risklevel1=0
count_vulnibm_sh_namebufferoverflow_risklevel0=0

count_vulnibm_sh_namecommandexecution=0
count_vulnibm_sh_namecommandexecution_risklevel=0
count_vulnibm_sh_namecommandexecution_risklevel10=0
count_vulnibm_sh_namecommandexecution_risklevel9=0
count_vulnibm_sh_namecommandexecution_risklevel8=0
count_vulnibm_sh_namecommandexecution_risklevel7=0
count_vulnibm_sh_namecommandexecution_risklevel6=0
count_vulnibm_sh_namecommandexecution_risklevel5=0
count_vulnibm_sh_namecommandexecution_risklevel4=0
count_vulnibm_sh_namecommandexecution_risklevel3=0
count_vulnibm_sh_namecommandexecution_risklevel2=0
count_vulnibm_sh_namecommandexecution_risklevel1=0
count_vulnibm_sh_namecommandexecution_risklevel0=0

count_vulnibm_sh_namespoofing=0
count_vulnibm_sh_namespoofing_risklevel=0
count_vulnibm_sh_namespoofing_risklevel10=0
count_vulnibm_sh_namespoofing_risklevel9=0
count_vulnibm_sh_namespoofing_risklevel8=0
count_vulnibm_sh_namespoofing_risklevel7=0
count_vulnibm_sh_namespoofing_risklevel6=0
count_vulnibm_sh_namespoofing_risklevel5=0
count_vulnibm_sh_namespoofing_risklevel4=0
count_vulnibm_sh_namespoofing_risklevel3=0
count_vulnibm_sh_namespoofing_risklevel2=0
count_vulnibm_sh_namespoofing_risklevel1=0
count_vulnibm_sh_namespoofing_risklevel0=0

count_vulnibm_sh_nameclickjacking=0
count_vulnibm_sh_nameclickjacking_risklevel=0
count_vulnibm_sh_nameclickjacking_risklevel10=0
count_vulnibm_sh_nameclickjacking_risklevel9=0
count_vulnibm_sh_nameclickjacking_risklevel8=0
count_vulnibm_sh_nameclickjacking_risklevel7=0
count_vulnibm_sh_nameclickjacking_risklevel6=0
count_vulnibm_sh_nameclickjacking_risklevel5=0
count_vulnibm_sh_nameclickjacking_risklevel4=0
count_vulnibm_sh_nameclickjacking_risklevel3=0
count_vulnibm_sh_nameclickjacking_risklevel2=0
count_vulnibm_sh_nameclickjacking_risklevel1=0
count_vulnibm_sh_nameclickjacking_risklevel0=0

count_vulnibm_sh_namehijacking=0
count_vulnibm_sh_namehijacking_risklevel=0
count_vulnibm_sh_namehijacking_risklevel10=0
count_vulnibm_sh_namehijacking_risklevel9=0
count_vulnibm_sh_namehijacking_risklevel8=0
count_vulnibm_sh_namehijacking_risklevel7=0
count_vulnibm_sh_namehijacking_risklevel6=0
count_vulnibm_sh_namehijacking_risklevel5=0
count_vulnibm_sh_namehijacking_risklevel4=0
count_vulnibm_sh_namehijacking_risklevel3=0
count_vulnibm_sh_namehijacking_risklevel2=0
count_vulnibm_sh_namehijacking_risklevel1=0
count_vulnibm_sh_namehijacking_risklevel0=0

count_vulnibm_sh_namefileinclude=0
count_vulnibm_sh_namefileinclude_risklevel=0
count_vulnibm_sh_namefileinclude_risklevel10=0
count_vulnibm_sh_namefileinclude_risklevel9=0
count_vulnibm_sh_namefileinclude_risklevel8=0
count_vulnibm_sh_namefileinclude_risklevel7=0
count_vulnibm_sh_namefileinclude_risklevel6=0
count_vulnibm_sh_namefileinclude_risklevel5=0
count_vulnibm_sh_namefileinclude_risklevel4=0
count_vulnibm_sh_namefileinclude_risklevel3=0
count_vulnibm_sh_namefileinclude_risklevel2=0
count_vulnibm_sh_namefileinclude_risklevel1=0
count_vulnibm_sh_namefileinclude_risklevel0=0

count_vulnibm_sh_namebruteforce=0
count_vulnibm_sh_namebruteforce_risklevel=0
count_vulnibm_sh_namebruteforce_risklevel10=0
count_vulnibm_sh_namebruteforce_risklevel9=0
count_vulnibm_sh_namebruteforce_risklevel8=0
count_vulnibm_sh_namebruteforce_risklevel7=0
count_vulnibm_sh_namebruteforce_risklevel6=0
count_vulnibm_sh_namebruteforce_risklevel5=0
count_vulnibm_sh_namebruteforce_risklevel4=0
count_vulnibm_sh_namebruteforce_risklevel3=0
count_vulnibm_sh_namebruteforce_risklevel2=0
count_vulnibm_sh_namebruteforce_risklevel1=0
count_vulnibm_sh_namebruteforce_risklevel0=0

count_vulnibm_sh_namefileupload=0
count_vulnibm_sh_namefileupload_risklevel=0
count_vulnibm_sh_namefileupload_risklevel10=0
count_vulnibm_sh_namefileupload_risklevel9=0
count_vulnibm_sh_namefileupload_risklevel8=0
count_vulnibm_sh_namefileupload_risklevel7=0
count_vulnibm_sh_namefileupload_risklevel6=0
count_vulnibm_sh_namefileupload_risklevel5=0
count_vulnibm_sh_namefileupload_risklevel4=0
count_vulnibm_sh_namefileupload_risklevel3=0
count_vulnibm_sh_namefileupload_risklevel2=0
count_vulnibm_sh_namefileupload_risklevel1=0
count_vulnibm_sh_namefileupload_risklevel0=0

count_vulnibm_sh_nameheaderinjection=0
count_vulnibm_sh_nameheaderinjection_risklevel=0
count_vulnibm_sh_nameheaderinjection_risklevel10=0
count_vulnibm_sh_nameheaderinjection_risklevel9=0
count_vulnibm_sh_nameheaderinjection_risklevel8=0
count_vulnibm_sh_nameheaderinjection_risklevel7=0
count_vulnibm_sh_nameheaderinjection_risklevel6=0
count_vulnibm_sh_nameheaderinjection_risklevel5=0
count_vulnibm_sh_nameheaderinjection_risklevel4=0
count_vulnibm_sh_nameheaderinjection_risklevel3=0
count_vulnibm_sh_nameheaderinjection_risklevel2=0
count_vulnibm_sh_nameheaderinjection_risklevel1=0
count_vulnibm_sh_nameheaderinjection_risklevel0=0

count_vulnibm_sh_nametampering=0
count_vulnibm_sh_nametampering_risklevel=0
count_vulnibm_sh_nametampering_risklevel10=0
count_vulnibm_sh_nametampering_risklevel9=0
count_vulnibm_sh_nametampering_risklevel8=0
count_vulnibm_sh_nametampering_risklevel7=0
count_vulnibm_sh_nametampering_risklevel6=0
count_vulnibm_sh_nametampering_risklevel5=0
count_vulnibm_sh_nametampering_risklevel4=0
count_vulnibm_sh_nametampering_risklevel3=0
count_vulnibm_sh_nametampering_risklevel2=0
count_vulnibm_sh_nametampering_risklevel1=0
count_vulnibm_sh_nametampering_risklevel0=0

count_vulnibm_sh_nameanother=0
count_vulnibm_sh_nameanother_risklevel=0
count_vulnibm_sh_nameanother_risklevel10=0
count_vulnibm_sh_nameanother_risklevel9=0
count_vulnibm_sh_nameanother_risklevel8=0
count_vulnibm_sh_nameanother_risklevel7=0
count_vulnibm_sh_nameanother_risklevel6=0
count_vulnibm_sh_nameanother_risklevel5=0
count_vulnibm_sh_nameanother_risklevel4=0
count_vulnibm_sh_nameanother_risklevel3=0
count_vulnibm_sh_nameanother_risklevel2=0
count_vulnibm_sh_nameanother_risklevel1=0
count_vulnibm_sh_nameanother_risklevel0=0



















#Comprobamos el contenido de name
for r in range(0,len(df_vulnibm_sh["name"])):                       
    aux_str=df_vulnibm_sh["name"][r].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
    if(aux_str!='NONE'):
        count_vulnibm_sh_names+=1
        if('pathtraversal' in aux_str):
            count_vulnibm_sh_namepathtraversal+=1
            #Obtenemos el valor de PUNTUACION BASE y comprobamos, ademas almacenamos la suma para despues calcular la media de PUNTUACION BASE
            count_vulnibm_sh_namepathtraversal_risklevel+=float(df_vulnibm_sh["x_xfe_risk_level"][r])
            if(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 10.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=9.0)):
                count_vulnibm_sh_namepathtraversal_risklevel9+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 9.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=8.0)):
                count_vulnibm_sh_namepathtraversal_risklevel8+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 8.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=7.0)):
                count_vulnibm_sh_namepathtraversal_risklevel7+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 7.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=6.0)):
                count_vulnibm_sh_namepathtraversal_risklevel6+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 6.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=5.0)):
                count_vulnibm_sh_namepathtraversal_risklevel5+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 5.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=4.0)):
                count_vulnibm_sh_namepathtraversal_risklevel4+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 4.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=3.0)):
                count_vulnibm_sh_namepathtraversal_risklevel3+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 3.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=2.0)):
                count_vulnibm_sh_namepathtraversal_risklevel2+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 2.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=1.0)):
                count_vulnibm_sh_namepathtraversal_risklevel1+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 1.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=0.0)):
                count_vulnibm_sh_namepathtraversal_risklevel0+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) == 10.0)):
                count_vulnibm_sh_namepathtraversal_risklevel10+=1
            
        elif('directorytraversal' in aux_str):
            
            count_vulnibm_sh_namedirectorytraversal+=1
            count_vulnibm_sh_namedirectorytraversal_risklevel+=float(df_vulnibm_sh["x_xfe_risk_level"][r])
            if(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 10.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=9.0)):
                count_vulnibm_sh_namedirectorytraversal_risklevel9+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 9.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=8.0)):
                count_vulnibm_sh_namedirectorytraversal_risklevel8+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 8.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=7.0)):
                count_vulnibm_sh_namedirectorytraversal_risklevel7+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 7.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=6.0)):
                count_vulnibm_sh_namedirectorytraversal_risklevel6+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 6.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=5.0)):
                count_vulnibm_sh_namedirectorytraversal_risklevel5+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 5.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=4.0)):
                count_vulnibm_sh_namedirectorytraversal_risklevel4+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 4.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=3.0)):
                count_vulnibm_sh_namedirectorytraversal_risklevel3+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 3.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=2.0)):
                count_vulnibm_sh_namedirectorytraversal_risklevel2+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 2.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=1.0)):
                count_vulnibm_sh_namedirectorytraversal_risklevel1+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 1.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=0.0)):
                count_vulnibm_sh_namedirectorytraversal_risklevel0+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) == 10.0)):
                count_vulnibm_sh_namedirectorytraversal_risklevel10+=1
            
            
        elif('privilegeescalation' in aux_str):
        
            count_vulnibm_sh_nameprivilegeescalation+=1
            count_vulnibm_sh_nameprivilegeescalation_risklevel+=float(df_vulnibm_sh["x_xfe_risk_level"][r])
            if(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 10.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=9.0)):
                count_vulnibm_sh_nameprivilegeescalation_risklevel9+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 9.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=8.0)):
                count_vulnibm_sh_nameprivilegeescalation_risklevel8+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 8.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=7.0)):
                count_vulnibm_sh_nameprivilegeescalation_risklevel7+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 7.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=6.0)):
                count_vulnibm_sh_nameprivilegeescalation_risklevel6+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 6.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=5.0)):
                count_vulnibm_sh_nameprivilegeescalation_risklevel5+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 5.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=4.0)):
                count_vulnibm_sh_nameprivilegeescalation_risklevel4+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 4.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=3.0)):
                count_vulnibm_sh_nameprivilegeescalation_risklevel3+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 3.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=2.0)):
                count_vulnibm_sh_nameprivilegeescalation_risklevel2+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 2.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=1.0)):
                count_vulnibm_sh_nameprivilegeescalation_risklevel1+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 1.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=0.0)):
                count_vulnibm_sh_nameprivilegeescalation_risklevel0+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) == 10.0)):
                count_vulnibm_sh_nameprivilegeescalation_risklevel10+=1
            
        elif('cross-sitescripting' in aux_str):
        
            count_vulnibm_sh_namecrosssitescripting+=1
            count_vulnibm_sh_namecrosssitescripting_risklevel+=float(df_vulnibm_sh["x_xfe_risk_level"][r])
            if(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 10.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=9.0)):
                count_vulnibm_sh_namecrosssitescripting_risklevel9+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 9.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=8.0)):
                count_vulnibm_sh_namecrosssitescripting_risklevel8+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 8.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=7.0)):
                count_vulnibm_sh_namecrosssitescripting_risklevel7+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 7.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=6.0)):
                count_vulnibm_sh_namecrosssitescripting_risklevel6+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 6.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=5.0)):
                count_vulnibm_sh_namecrosssitescripting_risklevel5+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 5.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=4.0)):
                count_vulnibm_sh_namecrosssitescripting_risklevel4+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 4.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=3.0)):
                count_vulnibm_sh_namecrosssitescripting_risklevel3+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 3.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=2.0)):
                count_vulnibm_sh_namecrosssitescripting_risklevel2+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 2.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=1.0)):
                count_vulnibm_sh_namecrosssitescripting_risklevel1+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 1.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=0.0)):
                count_vulnibm_sh_namecrosssitescripting_risklevel0+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) == 10.0)):
                count_vulnibm_sh_namecrosssitescripting_risklevel10+=1
                                         
        elif('securitybypass' in aux_str):
        
            count_vulnibm_sh_namesecuritybypass+=1
            count_vulnibm_sh_namesecuritybypass_risklevel+=float(df_vulnibm_sh["x_xfe_risk_level"][r])
            if(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 10.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=9.0)):
                count_vulnibm_sh_namesecuritybypass_risklevel9+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 9.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=8.0)):
                count_vulnibm_sh_namesecuritybypass_risklevel8+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 8.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=7.0)):
                count_vulnibm_sh_namesecuritybypass_risklevel7+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 7.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=6.0)):
                count_vulnibm_sh_namesecuritybypass_risklevel6+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 6.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=5.0)):
                count_vulnibm_sh_namesecuritybypass_risklevel5+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 5.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=4.0)):
                count_vulnibm_sh_namesecuritybypass_risklevel4+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 4.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=3.0)):
                count_vulnibm_sh_namesecuritybypass_risklevel3+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 3.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=2.0)):
                count_vulnibm_sh_namesecuritybypass_risklevel2+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 2.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=1.0)):
                count_vulnibm_sh_namesecuritybypass_risklevel1+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 1.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=0.0)):
                count_vulnibm_sh_namesecuritybypass_risklevel0+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) == 10.0)):
                count_vulnibm_sh_namesecuritybypass_risklevel10+=1
                                         
        elif('information_disclosure' in aux_str or 'informationdisclosure' in aux_str):
        
            count_vulnibm_sh_nameinformationdisclosure+=1
            count_vulnibm_sh_nameinformationdisclosure_risklevel+=float(df_vulnibm_sh["x_xfe_risk_level"][r])
            if(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 10.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=9.0)):
                count_vulnibm_sh_nameinformationdisclosure_risklevel9+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 9.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=8.0)):
                count_vulnibm_sh_nameinformationdisclosure_risklevel8+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 8.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=7.0)):
                count_vulnibm_sh_nameinformationdisclosure_risklevel7+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 7.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=6.0)):
                count_vulnibm_sh_nameinformationdisclosure_risklevel6+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 6.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=5.0)):
                count_vulnibm_sh_nameinformationdisclosure_risklevel5+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 5.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=4.0)):
                count_vulnibm_sh_nameinformationdisclosure_risklevel4+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 4.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=3.0)):
                count_vulnibm_sh_nameinformationdisclosure_risklevel3+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 3.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=2.0)):
                count_vulnibm_sh_nameinformationdisclosure_risklevel2+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 2.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=1.0)):
                count_vulnibm_sh_nameinformationdisclosure_risklevel1+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 1.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=0.0)):
                count_vulnibm_sh_nameinformationdisclosure_risklevel0+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) == 10.0)):
                count_vulnibm_sh_nameinformationdisclosure_risklevel10+=1
                                         
        elif('denialofservice' in aux_str):
            
            count_vulnibm_sh_namedenialofservice+=1
            count_vulnibm_sh_namedenialofservice_risklevel+=float(df_vulnibm_sh["x_xfe_risk_level"][r])
            if(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 10.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=9.0)):
                count_vulnibm_sh_namedenialofservice_risklevel9+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 9.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=8.0)):
                count_vulnibm_sh_namedenialofservice_risklevel8+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 8.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=7.0)):
                count_vulnibm_sh_namedenialofservice_risklevel7+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 7.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=6.0)):
                count_vulnibm_sh_namedenialofservice_risklevel6+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 6.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=5.0)):
                count_vulnibm_sh_namedenialofservice_risklevel5+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 5.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=4.0)):
                count_vulnibm_sh_namedenialofservice_risklevel4+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 4.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=3.0)):
                count_vulnibm_sh_namedenialofservice_risklevel3+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 3.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=2.0)):
                count_vulnibm_sh_namedenialofservice_risklevel2+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 2.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=1.0)):
                count_vulnibm_sh_namedenialofservice_risklevel1+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 1.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=0.0)):
                count_vulnibm_sh_namedenialofservice_risklevel0+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) == 10.0)):
                count_vulnibm_sh_namedenialofservice_risklevel10+=1
            
        elif('codeexecution' in aux_str):
        
        
            count_vulnibm_sh_namecodeexecution+=1
            count_vulnibm_sh_namecodeexecution_risklevel+=float(df_vulnibm_sh["x_xfe_risk_level"][r])
            if(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 10.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=9.0)):
                count_vulnibm_sh_namecodeexecution_risklevel9+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 9.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=8.0)):
                count_vulnibm_sh_namecodeexecution_risklevel8+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 8.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=7.0)):
                count_vulnibm_sh_namecodeexecution_risklevel7+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 7.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=6.0)):
                count_vulnibm_sh_namecodeexecution_risklevel6+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 6.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=5.0)):
                count_vulnibm_sh_namecodeexecution_risklevel5+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 5.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=4.0)):
                count_vulnibm_sh_namecodeexecution_risklevel4+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 4.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=3.0)):
                count_vulnibm_sh_namecodeexecution_risklevel3+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 3.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=2.0)):
                count_vulnibm_sh_namecodeexecution_risklevel2+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 2.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=1.0)):
                count_vulnibm_sh_namecodeexecution_risklevel1+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 1.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=0.0)):
                count_vulnibm_sh_namecodeexecution_risklevel0+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) == 10.0)):
                count_vulnibm_sh_namecodeexecution_risklevel10+=1
                                         
        elif('maninthemiddle' in aux_str):
        
            count_vulnibm_sh_namemaninthemiddle+=1
            count_vulnibm_sh_namemaninthemiddle_risklevel+=float(df_vulnibm_sh["x_xfe_risk_level"][r])
            if(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 10.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=9.0)):
                count_vulnibm_sh_namemaninthemiddle_risklevel9+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 9.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=8.0)):
                count_vulnibm_sh_namemaninthemiddle_risklevel8+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 8.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=7.0)):
                count_vulnibm_sh_namemaninthemiddle_risklevel7+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 7.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=6.0)):
                count_vulnibm_sh_namemaninthemiddle_risklevel6+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 6.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=5.0)):
                count_vulnibm_sh_namemaninthemiddle_risklevel5+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 5.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=4.0)):
                count_vulnibm_sh_namemaninthemiddle_risklevel4+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 4.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=3.0)):
                count_vulnibm_sh_namemaninthemiddle_risklevel3+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 3.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=2.0)):
                count_vulnibm_sh_namemaninthemiddle_risklevel2+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 2.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=1.0)):
                count_vulnibm_sh_namemaninthemiddle_risklevel1+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 1.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=0.0)):
                count_vulnibm_sh_namemaninthemiddle_risklevel0+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) == 10.0)):
                count_vulnibm_sh_namemaninthemiddle_risklevel10+=1
                                         
        elif('SQLinjection' in aux_str):
        
            count_vulnibm_sh_namesqlinjection+=1
            count_vulnibm_sh_namesqlinjection_risklevel+=float(df_vulnibm_sh["x_xfe_risk_level"][r])
            if(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 10.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=9.0)):
                count_vulnibm_sh_namesqlinjection_risklevel9+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 9.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=8.0)):
                count_vulnibm_sh_namesqlinjection_risklevel8+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 8.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=7.0)):
                count_vulnibm_sh_namesqlinjection_risklevel7+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 7.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=6.0)):
                count_vulnibm_sh_namesqlinjection_risklevel6+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 6.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=5.0)):
                count_vulnibm_sh_namesqlinjection_risklevel5+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 5.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=4.0)):
                count_vulnibm_sh_namesqlinjection_risklevel4+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 4.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=3.0)):
                count_vulnibm_sh_namesqlinjection_risklevel3+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 3.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=2.0)):
                count_vulnibm_sh_namesqlinjection_risklevel2+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 2.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=1.0)):
                count_vulnibm_sh_namesqlinjection_risklevel1+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 1.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=0.0)):
                count_vulnibm_sh_namesqlinjection_risklevel0+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) == 10.0)):
                count_vulnibm_sh_namesqlinjection_risklevel10+=1
                                         
        elif('cross-siterequestforgery' in aux_str):
        
            count_vulnibm_sh_namecrosssiterequestforgery+=1
            count_vulnibm_sh_namecrosssiterequestforgery_risklevel+=float(df_vulnibm_sh["x_xfe_risk_level"][r])
            if(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 10.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=9.0)):
                count_vulnibm_sh_namecrosssiterequestforgery_risklevel9+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 9.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=8.0)):
                count_vulnibm_sh_namecrosssiterequestforgery_risklevel8+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 8.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=7.0)):
                count_vulnibm_sh_namecrosssiterequestforgery_risklevel7+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 7.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=6.0)):
                count_vulnibm_sh_namecrosssiterequestforgery_risklevel6+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 6.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=5.0)):
                count_vulnibm_sh_namecrosssiterequestforgery_risklevel5+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 5.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=4.0)):
                count_vulnibm_sh_namecrosssiterequestforgery_risklevel4+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 4.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=3.0)):
                count_vulnibm_sh_namecrosssiterequestforgery_risklevel3+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 3.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=2.0)):
                count_vulnibm_sh_namecrosssiterequestforgery_risklevel2+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 2.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=1.0)):
                count_vulnibm_sh_namecrosssiterequestforgery_risklevel1+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 1.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=0.0)):
                count_vulnibm_sh_namecrosssiterequestforgery_risklevel0+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) == 10.0)):
                count_vulnibm_sh_namecrosssiterequestforgery_risklevel10+=1
                                         
        elif('moduleexecution' in aux_str):
        
            count_vulnibm_sh_namemoduleexecution+=1
            count_vulnibm_sh_namemoduleexecution_risklevel+=float(df_vulnibm_sh["x_xfe_risk_level"][r])
            if(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 10.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=9.0)):
                count_vulnibm_sh_namemoduleexecution_risklevel9+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 9.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=8.0)):
                count_vulnibm_sh_namemoduleexecution_risklevel8+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 8.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=7.0)):
                count_vulnibm_sh_namemoduleexecution_risklevel7+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 7.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=6.0)):
                count_vulnibm_sh_namemoduleexecution_risklevel6+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 6.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=5.0)):
                count_vulnibm_sh_namemoduleexecution_risklevel5+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 5.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=4.0)):
                count_vulnibm_sh_namemoduleexecution_risklevel4+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 4.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=3.0)):
                count_vulnibm_sh_namemoduleexecution_risklevel3+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 3.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=2.0)):
                count_vulnibm_sh_namemoduleexecution_risklevel2+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 2.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=1.0)):
                count_vulnibm_sh_namemoduleexecution_risklevel1+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 1.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=0.0)):
                count_vulnibm_sh_namemoduleexecution_risklevel0+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) == 10.0)):
                count_vulnibm_sh_namemoduleexecution_risklevel10+=1
                                         
        elif('bufferoverflow' in aux_str):
        
            count_vulnibm_sh_namebufferoverflow+=1
            count_vulnibm_sh_namebufferoverflow_risklevel+=float(df_vulnibm_sh["x_xfe_risk_level"][r])
            if(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 10.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=9.0)):
                count_vulnibm_sh_namebufferoverflow_risklevel9+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 9.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=8.0)):
                count_vulnibm_sh_namebufferoverflow_risklevel8+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 8.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=7.0)):
                count_vulnibm_sh_namebufferoverflow_risklevel7+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 7.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=6.0)):
                count_vulnibm_sh_namebufferoverflow_risklevel6+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 6.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=5.0)):
                count_vulnibm_sh_namebufferoverflow_risklevel5+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 5.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=4.0)):
                count_vulnibm_sh_namebufferoverflow_risklevel4+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 4.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=3.0)):
                count_vulnibm_sh_namebufferoverflow_risklevel3+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 3.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=2.0)):
                count_vulnibm_sh_namebufferoverflow_risklevel2+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 2.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=1.0)):
                count_vulnibm_sh_namebufferoverflow_risklevel1+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 1.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=0.0)):
                count_vulnibm_sh_namebufferoverflow_risklevel0+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) == 10.0)):
                count_vulnibm_sh_namebufferoverflow_risklevel10+=1
                                         
        elif('commandexecution' in aux_str):
        
            count_vulnibm_sh_namecommandexecution+=1
            count_vulnibm_sh_namecommandexecution_risklevel+=float(df_vulnibm_sh["x_xfe_risk_level"][r])
            if(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 10.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=9.0)):
                count_vulnibm_sh_namecommandexecution_risklevel9+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 9.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=8.0)):
                count_vulnibm_sh_namecommandexecution_risklevel8+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 8.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=7.0)):
                count_vulnibm_sh_namecommandexecution_risklevel7+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 7.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=6.0)):
                count_vulnibm_sh_namecommandexecution_risklevel6+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 6.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=5.0)):
                count_vulnibm_sh_namecommandexecution_risklevel5+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 5.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=4.0)):
                count_vulnibm_sh_namecommandexecution_risklevel4+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 4.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=3.0)):
                count_vulnibm_sh_namecommandexecution_risklevel3+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 3.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=2.0)):
                count_vulnibm_sh_namecommandexecution_risklevel2+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 2.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=1.0)):
                count_vulnibm_sh_namecommandexecution_risklevel1+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 1.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=0.0)):
                count_vulnibm_sh_namecommandexecution_risklevel0+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) == 10.0)):
                count_vulnibm_sh_namecommandexecution_risklevel10+=1
                                         
        elif('spoofing' in aux_str):
        
            count_vulnibm_sh_namespoofing+=1
            count_vulnibm_sh_namespoofing_risklevel+=float(df_vulnibm_sh["x_xfe_risk_level"][r])
            if(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 10.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=9.0)):
                count_vulnibm_sh_namespoofing_risklevel9+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 9.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=8.0)):
                count_vulnibm_sh_namespoofing_risklevel8+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 8.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=7.0)):
                count_vulnibm_sh_namespoofing_risklevel7+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 7.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=6.0)):
                count_vulnibm_sh_namespoofing_risklevel6+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 6.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=5.0)):
                count_vulnibm_sh_namespoofing_risklevel5+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 5.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=4.0)):
                count_vulnibm_sh_namespoofing_risklevel4+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 4.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=3.0)):
                count_vulnibm_sh_namespoofing_risklevel3+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 3.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=2.0)):
                count_vulnibm_sh_namespoofing_risklevel2+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 2.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=1.0)):
                count_vulnibm_sh_namespoofing_risklevel1+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 1.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=0.0)):
                count_vulnibm_sh_namespoofing_risklevel0+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) == 10.0)):
                count_vulnibm_sh_namespoofing_risklevel10+=1
                                         
        elif('clickjacking' in aux_str):
        
            count_vulnibm_sh_nameclickjacking+=1
            count_vulnibm_sh_nameclickjacking_risklevel+=float(df_vulnibm_sh["x_xfe_risk_level"][r])
            if(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 10.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=9.0)):
                count_vulnibm_sh_nameclickjacking_risklevel9+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 9.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=8.0)):
                count_vulnibm_sh_nameclickjacking_risklevel8+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 8.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=7.0)):
                count_vulnibm_sh_nameclickjacking_risklevel7+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 7.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=6.0)):
                count_vulnibm_sh_nameclickjacking_risklevel6+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 6.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=5.0)):
                count_vulnibm_sh_nameclickjacking_risklevel5+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 5.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=4.0)):
                count_vulnibm_sh_nameclickjacking_risklevel4+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 4.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=3.0)):
                count_vulnibm_sh_nameclickjacking_risklevel3+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 3.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=2.0)):
                count_vulnibm_sh_nameclickjacking_risklevel2+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 2.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=1.0)):
                count_vulnibm_sh_nameclickjacking_risklevel1+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 1.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=0.0)):
                count_vulnibm_sh_nameclickjacking_risklevel0+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) == 10.0)):
                count_vulnibm_sh_nameclickjacking_risklevel10+=1
              
        elif('hijacking' in aux_str):
        
            count_vulnibm_sh_namehijacking+=1
            count_vulnibm_sh_namehijacking_risklevel+=float(df_vulnibm_sh["x_xfe_risk_level"][r])
            if(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 10.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=9.0)):
                count_vulnibm_sh_namehijacking_risklevel9+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 9.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=8.0)):
                count_vulnibm_sh_namehijacking_risklevel8+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 8.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=7.0)):
                count_vulnibm_sh_namehijacking_risklevel7+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 7.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=6.0)):
                count_vulnibm_sh_namehijacking_risklevel6+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 6.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=5.0)):
                count_vulnibm_sh_namehijacking_risklevel5+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 5.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=4.0)):
                count_vulnibm_sh_namehijacking_risklevel4+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 4.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=3.0)):
                count_vulnibm_sh_namehijacking_risklevel3+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 3.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=2.0)):
                count_vulnibm_sh_namehijacking_risklevel2+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 2.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=1.0)):
                count_vulnibm_sh_namehijacking_risklevel1+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 1.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=0.0)):
                count_vulnibm_sh_namehijacking_risklevel0+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) == 10.0)):
                count_vulnibm_sh_namehijacking_risklevel10+=1
               
        elif('fileinclude' in aux_str):
        
            count_vulnibm_sh_namefileinclude+=1
            count_vulnibm_sh_namefileinclude_risklevel+=float(df_vulnibm_sh["x_xfe_risk_level"][r])
            if(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 10.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=9.0)):
                count_vulnibm_sh_namefileinclude_risklevel9+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 9.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=8.0)):
                count_vulnibm_sh_namefileinclude_risklevel8+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 8.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=7.0)):
                count_vulnibm_sh_namefileinclude_risklevel7+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 7.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=6.0)):
                count_vulnibm_sh_namefileinclude_risklevel6+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 6.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=5.0)):
                count_vulnibm_sh_namefileinclude_risklevel5+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 5.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=4.0)):
                count_vulnibm_sh_namefileinclude_risklevel4+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 4.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=3.0)):
                count_vulnibm_sh_namefileinclude_risklevel3+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 3.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=2.0)):
                count_vulnibm_sh_namefileinclude_risklevel2+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 2.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=1.0)):
                count_vulnibm_sh_namefileinclude_risklevel1+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 1.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=0.0)):
                count_vulnibm_sh_namefileinclude_risklevel0+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) == 10.0)):
                count_vulnibm_sh_namefileinclude_risklevel10+=1
                
               
        elif('bruteforce' in aux_str):
        
            count_vulnibm_sh_namebruteforce+=1
            count_vulnibm_sh_namebruteforce_risklevel+=float(df_vulnibm_sh["x_xfe_risk_level"][r])
            if(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 10.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=9.0)):
                count_vulnibm_sh_namebruteforce_risklevel9+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 9.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=8.0)):
                count_vulnibm_sh_namebruteforce_risklevel8+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 8.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=7.0)):
                count_vulnibm_sh_namebruteforce_risklevel7+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 7.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=6.0)):
                count_vulnibm_sh_namebruteforce_risklevel6+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 6.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=5.0)):
                count_vulnibm_sh_namebruteforce_risklevel5+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 5.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=4.0)):
                count_vulnibm_sh_namebruteforce_risklevel4+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 4.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=3.0)):
                count_vulnibm_sh_namebruteforce_risklevel3+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 3.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=2.0)):
                count_vulnibm_sh_namebruteforce_risklevel2+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 2.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=1.0)):
                count_vulnibm_sh_namebruteforce_risklevel1+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 1.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=0.0)):
                count_vulnibm_sh_namebruteforce_risklevel0+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) == 10.0)):
                count_vulnibm_sh_namebruteforce_risklevel10+=1
                
               
        elif('fileupload' in aux_str):
        
            count_vulnibm_sh_namefileupload+=1
            count_vulnibm_sh_namefileupload_risklevel+=float(df_vulnibm_sh["x_xfe_risk_level"][r])
            if(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 10.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=9.0)):
                count_vulnibm_sh_namefileupload_risklevel9+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 9.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=8.0)):
                count_vulnibm_sh_namefileupload_risklevel8+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 8.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=7.0)):
                count_vulnibm_sh_namefileupload_risklevel7+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 7.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=6.0)):
                count_vulnibm_sh_namefileupload_risklevel6+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 6.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=5.0)):
                count_vulnibm_sh_namefileupload_risklevel5+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 5.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=4.0)):
                count_vulnibm_sh_namefileupload_risklevel4+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 4.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=3.0)):
                count_vulnibm_sh_namefileupload_risklevel3+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 3.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=2.0)):
                count_vulnibm_sh_namefileupload_risklevel2+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 2.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=1.0)):
                count_vulnibm_sh_namefileupload_risklevel1+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 1.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=0.0)):
                count_vulnibm_sh_namefileupload_risklevel0+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) == 10.0)):
                count_vulnibm_sh_namefileupload_risklevel10+=1
                
               
        elif('headerinjection' in aux_str):
        
            count_vulnibm_sh_nameheaderinjection+=1
            count_vulnibm_sh_nameheaderinjection_risklevel+=float(df_vulnibm_sh["x_xfe_risk_level"][r])
            if(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 10.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=9.0)):
                count_vulnibm_sh_nameheaderinjection_risklevel9+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 9.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=8.0)):
                count_vulnibm_sh_nameheaderinjection_risklevel8+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 8.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=7.0)):
                count_vulnibm_sh_nameheaderinjection_risklevel7+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 7.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=6.0)):
                count_vulnibm_sh_nameheaderinjection_risklevel6+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 6.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=5.0)):
                count_vulnibm_sh_nameheaderinjection_risklevel5+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 5.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=4.0)):
                count_vulnibm_sh_nameheaderinjection_risklevel4+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 4.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=3.0)):
                count_vulnibm_sh_nameheaderinjection_risklevel3+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 3.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=2.0)):
                count_vulnibm_sh_nameheaderinjection_risklevel2+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 2.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=1.0)):
                count_vulnibm_sh_nameheaderinjection_risklevel1+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 1.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=0.0)):
                count_vulnibm_sh_nameheaderinjection_risklevel0+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) == 10.0)):
                count_vulnibm_sh_nameheaderinjection_risklevel10+=1
               
        elif('Tampering' in aux_str):
        
            count_vulnibm_sh_nametampering+=1
            count_vulnibm_sh_nametampering_risklevel+=float(df_vulnibm_sh["x_xfe_risk_level"][r])
            if(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 10.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=9.0)):
                count_vulnibm_sh_nametampering_risklevel9+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 9.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=8.0)):
                count_vulnibm_sh_nametampering_risklevel8+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 8.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=7.0)):
                count_vulnibm_sh_nametampering_risklevel7+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 7.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=6.0)):
                count_vulnibm_sh_nametampering_risklevel6+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 6.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=5.0)):
                count_vulnibm_sh_nametampering_risklevel5+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 5.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=4.0)):
                count_vulnibm_sh_nametampering_risklevel4+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 4.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=3.0)):
                count_vulnibm_sh_nametampering_risklevel3+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 3.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=2.0)):
                count_vulnibm_sh_nametampering_risklevel2+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 2.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=1.0)):
                count_vulnibm_sh_nametampering_risklevel1+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 1.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=0.0)):
                count_vulnibm_sh_nametampering_risklevel0+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) == 10.0)):
                count_vulnibm_sh_nametampering_risklevel10+=1    
        else:
        
            count_vulnibm_sh_nameanother+=1
            count_vulnibm_sh_nameanother_risklevel+=float(df_vulnibm_sh["x_xfe_risk_level"][r])
            if(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 10.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=9.0)):
                count_vulnibm_sh_nameanother_risklevel9+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 9.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=8.0)):
                count_vulnibm_sh_nameanother_risklevel8+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 8.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=7.0)):
                count_vulnibm_sh_nameanother_risklevel7+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 7.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=6.0)):
                count_vulnibm_sh_nameanother_risklevel6+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 6.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=5.0)):
                count_vulnibm_sh_nameanother_risklevel5+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 5.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=4.0)):
                count_vulnibm_sh_nameanother_risklevel4+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 4.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=3.0)):
                count_vulnibm_sh_nameanother_risklevel3+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 3.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=2.0)):
                count_vulnibm_sh_nameanother_risklevel2+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 2.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=1.0)):
                count_vulnibm_sh_nameanother_risklevel1+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 1.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=0.0)):
                count_vulnibm_sh_nameanother_risklevel0+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) == 10.0)):
                count_vulnibm_sh_nameanother_risklevel10+=1
                
                
                
                
                
print("*********************ESTADÍSTICAS NOMBRE/PUNTUACION BASE OBJETOS DE TIPO VULNERABILIDAD IBM PARTE SMART HOME*********************")
print("\n")                            
print("\n")
print(" DE UN TOTAL DE "+str(count_vulnibm_sh_names)+" VULNERABILIDADES:\n") 
print("\n")
print("   - LAS ESTADISTICAS DE VALORES DE NOMBRE SON LAS SIGUIENTES:  \n")
print("      -    EN  "+str(count_vulnibm_sh_namepathtraversal)+" VULNERABILIDADES EL NOMBRE INCLUYE PATH TRAVERSAL, LAS ESTADÍSTICAS DE PUNTUACION BASE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_sh_namepathtraversal_risklevel10)+" VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
print("            -    EN  "+str(count_vulnibm_sh_namepathtraversal_risklevel9)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN  "+str(count_vulnibm_sh_namepathtraversal_risklevel8)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN  "+str(count_vulnibm_sh_namepathtraversal_risklevel7)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN  "+str(count_vulnibm_sh_namepathtraversal_risklevel6)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN "+str(count_vulnibm_sh_namepathtraversal_risklevel5)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN "+str(count_vulnibm_sh_namepathtraversal_risklevel4)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN "+str(count_vulnibm_sh_namepathtraversal_risklevel3)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN "+str(count_vulnibm_sh_namepathtraversal_risklevel2)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN "+str(count_vulnibm_sh_namepathtraversal_risklevel1)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN "+str(count_vulnibm_sh_namepathtraversal_risklevel0)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_sh_namedirectorytraversal)+" VULNERABILIDADES EL NOMBRE INCLUYE DIRECTORY TRAVERSAL, LAS ESTADÍSTICAS DE PUNTUACION BASE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_sh_namedirectorytraversal_risklevel10)+" VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
print("            -    EN  "+str(count_vulnibm_sh_namedirectorytraversal_risklevel9)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN  "+str(count_vulnibm_sh_namedirectorytraversal_risklevel8)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN  "+str(count_vulnibm_sh_namedirectorytraversal_risklevel7)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN  "+str(count_vulnibm_sh_namedirectorytraversal_risklevel6)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN "+str(count_vulnibm_sh_namedirectorytraversal_risklevel5)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN "+str(count_vulnibm_sh_namedirectorytraversal_risklevel4)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN "+str(count_vulnibm_sh_namedirectorytraversal_risklevel3)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN "+str(count_vulnibm_sh_namedirectorytraversal_risklevel2)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN "+str(count_vulnibm_sh_namedirectorytraversal_risklevel1)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN "+str(count_vulnibm_sh_namedirectorytraversal_risklevel0)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_sh_nameprivilegeescalation)+" VULNERABILIDADES EL NOMBRE INCLUYE PRIVILEGE ESCALATION, LAS ESTADÍSTICAS DE PUNTUACION BASE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_sh_nameprivilegeescalation_risklevel10)+" VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
print("            -    EN  "+str(count_vulnibm_sh_nameprivilegeescalation_risklevel9)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN  "+str(count_vulnibm_sh_nameprivilegeescalation_risklevel8)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN  "+str(count_vulnibm_sh_nameprivilegeescalation_risklevel7)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN  "+str(count_vulnibm_sh_nameprivilegeescalation_risklevel6)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN "+str(count_vulnibm_sh_nameprivilegeescalation_risklevel5)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN "+str(count_vulnibm_sh_nameprivilegeescalation_risklevel4)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN "+str(count_vulnibm_sh_nameprivilegeescalation_risklevel3)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN "+str(count_vulnibm_sh_nameprivilegeescalation_risklevel2)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN "+str(count_vulnibm_sh_nameprivilegeescalation_risklevel1)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN "+str(count_vulnibm_sh_nameprivilegeescalation_risklevel0)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_sh_namecrosssitescripting)+" VULNERABILIDADES EL NOMBRE INCLUYE CROSS SITE SCRIPTING, LAS ESTADÍSTICAS DE PUNTUACION BASE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_sh_namecrosssitescripting_risklevel10)+" VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
print("            -    EN  "+str(count_vulnibm_sh_namecrosssitescripting_risklevel9)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN  "+str(count_vulnibm_sh_namecrosssitescripting_risklevel8)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN  "+str(count_vulnibm_sh_namecrosssitescripting_risklevel7)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN  "+str(count_vulnibm_sh_namecrosssitescripting_risklevel6)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN "+str(count_vulnibm_sh_namecrosssitescripting_risklevel5)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN "+str(count_vulnibm_sh_namecrosssitescripting_risklevel4)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN "+str(count_vulnibm_sh_namecrosssitescripting_risklevel3)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN "+str(count_vulnibm_sh_namecrosssitescripting_risklevel2)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN "+str(count_vulnibm_sh_namecrosssitescripting_risklevel1)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN "+str(count_vulnibm_sh_namecrosssitescripting_risklevel0)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_sh_namesecuritybypass)+" VULNERABILIDADES EL NOMBRE INCLUYE SECURITY BYPASS, LAS ESTADÍSTICAS DE PUNTUACION BASE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_sh_namesecuritybypass_risklevel10)+" VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
print("            -    EN  "+str(count_vulnibm_sh_namesecuritybypass_risklevel9)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN  "+str(count_vulnibm_sh_namesecuritybypass_risklevel8)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN  "+str(count_vulnibm_sh_namesecuritybypass_risklevel7)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN  "+str(count_vulnibm_sh_namesecuritybypass_risklevel6)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN "+str(count_vulnibm_sh_namesecuritybypass_risklevel5)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN "+str(count_vulnibm_sh_namesecuritybypass_risklevel4)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN "+str(count_vulnibm_sh_namesecuritybypass_risklevel3)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN "+str(count_vulnibm_sh_namesecuritybypass_risklevel2)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN "+str(count_vulnibm_sh_namesecuritybypass_risklevel1)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN "+str(count_vulnibm_sh_namesecuritybypass_risklevel0)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_sh_nameinformationdisclosure)+" VULNERABILIDADES EL NOMBRE INCLUYE INFORMATION DISCLOSURE, LAS ESTADÍSTICAS DE PUNTUACION BASE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_sh_nameinformationdisclosure_risklevel10)+" VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
print("            -    EN  "+str(count_vulnibm_sh_nameinformationdisclosure_risklevel9)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN  "+str(count_vulnibm_sh_nameinformationdisclosure_risklevel8)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN  "+str(count_vulnibm_sh_nameinformationdisclosure_risklevel7)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN  "+str(count_vulnibm_sh_nameinformationdisclosure_risklevel6)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN "+str(count_vulnibm_sh_nameinformationdisclosure_risklevel5)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN "+str(count_vulnibm_sh_nameinformationdisclosure_risklevel4)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN "+str(count_vulnibm_sh_nameinformationdisclosure_risklevel3)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN "+str(count_vulnibm_sh_nameinformationdisclosure_risklevel2)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN "+str(count_vulnibm_sh_nameinformationdisclosure_risklevel1)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN "+str(count_vulnibm_sh_nameinformationdisclosure_risklevel0)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_sh_namedenialofservice)+" VULNERABILIDADES EL NOMBRE INCLUYE DENIAL OF SERVICE, LAS ESTADÍSTICAS DE PUNTUACION BASE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_sh_namedenialofservice_risklevel10)+" VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
print("            -    EN  "+str(count_vulnibm_sh_namedenialofservice_risklevel9)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN  "+str(count_vulnibm_sh_namedenialofservice_risklevel8)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN  "+str(count_vulnibm_sh_namedenialofservice_risklevel7)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN  "+str(count_vulnibm_sh_namedenialofservice_risklevel6)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN "+str(count_vulnibm_sh_namedenialofservice_risklevel5)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN "+str(count_vulnibm_sh_namedenialofservice_risklevel4)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN "+str(count_vulnibm_sh_namedenialofservice_risklevel3)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN "+str(count_vulnibm_sh_namedenialofservice_risklevel2)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN "+str(count_vulnibm_sh_namedenialofservice_risklevel1)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN "+str(count_vulnibm_sh_namedenialofservice_risklevel0)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_sh_namecodeexecution)+" VULNERABILIDADES EL NOMBRE INCLUYE CODE EXECUTION, LAS ESTADÍSTICAS DE PUNTUACION BASE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_sh_namecodeexecution_risklevel10)+" VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
print("            -    EN  "+str(count_vulnibm_sh_namecodeexecution_risklevel9)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN  "+str(count_vulnibm_sh_namecodeexecution_risklevel8)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN  "+str(count_vulnibm_sh_namecodeexecution_risklevel7)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN  "+str(count_vulnibm_sh_namecodeexecution_risklevel6)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN "+str(count_vulnibm_sh_namecodeexecution_risklevel5)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN "+str(count_vulnibm_sh_namecodeexecution_risklevel4)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN "+str(count_vulnibm_sh_namecodeexecution_risklevel3)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN "+str(count_vulnibm_sh_namecodeexecution_risklevel2)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN "+str(count_vulnibm_sh_namecodeexecution_risklevel1)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN "+str(count_vulnibm_sh_namecodeexecution_risklevel0)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_sh_namemaninthemiddle)+" VULNERABILIDADES EL NOMBRE INCLUYE MAN IN THE MIDDLE, LAS ESTADÍSTICAS DE PUNTUACION BASE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_sh_namemaninthemiddle_risklevel10)+" VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
print("            -    EN  "+str(count_vulnibm_sh_namemaninthemiddle_risklevel9)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN  "+str(count_vulnibm_sh_namemaninthemiddle_risklevel8)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN  "+str(count_vulnibm_sh_namemaninthemiddle_risklevel7)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN  "+str(count_vulnibm_sh_namemaninthemiddle_risklevel6)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN "+str(count_vulnibm_sh_namemaninthemiddle_risklevel5)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN "+str(count_vulnibm_sh_namemaninthemiddle_risklevel4)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN "+str(count_vulnibm_sh_namemaninthemiddle_risklevel3)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN "+str(count_vulnibm_sh_namemaninthemiddle_risklevel2)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN "+str(count_vulnibm_sh_namemaninthemiddle_risklevel1)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN "+str(count_vulnibm_sh_namemaninthemiddle_risklevel0)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_sh_namesqlinjection)+" VULNERABILIDADES EL NOMBRE INCLUYE SQL INJECTION, LAS ESTADÍSTICAS DE PUNTUACION BASE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_sh_namesqlinjection_risklevel10)+" VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
print("            -    EN  "+str(count_vulnibm_sh_namesqlinjection_risklevel9)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN  "+str(count_vulnibm_sh_namesqlinjection_risklevel8)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN  "+str(count_vulnibm_sh_namesqlinjection_risklevel7)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN  "+str(count_vulnibm_sh_namesqlinjection_risklevel6)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN "+str(count_vulnibm_sh_namesqlinjection_risklevel5)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN "+str(count_vulnibm_sh_namesqlinjection_risklevel4)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN "+str(count_vulnibm_sh_namesqlinjection_risklevel3)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN "+str(count_vulnibm_sh_namesqlinjection_risklevel2)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN "+str(count_vulnibm_sh_namesqlinjection_risklevel1)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN "+str(count_vulnibm_sh_namesqlinjection_risklevel0)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_sh_namecrosssiterequestforgery)+" VULNERABILIDADES EL NOMBRE INCLUYE CROSS SITE REQUEST FORGERY, LAS ESTADÍSTICAS DE PUNTUACION BASE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_sh_namecrosssiterequestforgery_risklevel10)+" VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
print("            -    EN  "+str(count_vulnibm_sh_namecrosssiterequestforgery_risklevel9)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN  "+str(count_vulnibm_sh_namecrosssiterequestforgery_risklevel8)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN  "+str(count_vulnibm_sh_namecrosssiterequestforgery_risklevel7)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN  "+str(count_vulnibm_sh_namecrosssiterequestforgery_risklevel6)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN "+str(count_vulnibm_sh_namecrosssiterequestforgery_risklevel5)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN "+str(count_vulnibm_sh_namecrosssiterequestforgery_risklevel4)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN "+str(count_vulnibm_sh_namecrosssiterequestforgery_risklevel3)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN "+str(count_vulnibm_sh_namecrosssiterequestforgery_risklevel2)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN "+str(count_vulnibm_sh_namecrosssiterequestforgery_risklevel1)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN "+str(count_vulnibm_sh_namecrosssiterequestforgery_risklevel0)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_sh_namemoduleexecution)+" VULNERABILIDADES EL NOMBRE INCLUYE MODULE EXECUTION, LAS ESTADÍSTICAS DE PUNTUACION BASE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_sh_namemoduleexecution_risklevel10)+" VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
print("            -    EN  "+str(count_vulnibm_sh_namemoduleexecution_risklevel9)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN  "+str(count_vulnibm_sh_namemoduleexecution_risklevel8)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN  "+str(count_vulnibm_sh_namemoduleexecution_risklevel7)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN  "+str(count_vulnibm_sh_namemoduleexecution_risklevel6)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN "+str(count_vulnibm_sh_namemoduleexecution_risklevel5)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN "+str(count_vulnibm_sh_namemoduleexecution_risklevel4)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN "+str(count_vulnibm_sh_namemoduleexecution_risklevel3)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN "+str(count_vulnibm_sh_namemoduleexecution_risklevel2)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN "+str(count_vulnibm_sh_namemoduleexecution_risklevel1)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN "+str(count_vulnibm_sh_namemoduleexecution_risklevel0)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_sh_namebufferoverflow)+" VULNERABILIDADES EL NOMBRE INCLUYE BUFFER OVERFLOW, LAS ESTADÍSTICAS DE PUNTUACION BASE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_sh_namebufferoverflow_risklevel10)+" VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
print("            -    EN  "+str(count_vulnibm_sh_namebufferoverflow_risklevel9)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN  "+str(count_vulnibm_sh_namebufferoverflow_risklevel8)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN  "+str(count_vulnibm_sh_namebufferoverflow_risklevel7)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN  "+str(count_vulnibm_sh_namebufferoverflow_risklevel6)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN "+str(count_vulnibm_sh_namebufferoverflow_risklevel5)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN "+str(count_vulnibm_sh_namebufferoverflow_risklevel4)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN "+str(count_vulnibm_sh_namebufferoverflow_risklevel3)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN "+str(count_vulnibm_sh_namebufferoverflow_risklevel2)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN "+str(count_vulnibm_sh_namebufferoverflow_risklevel1)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN "+str(count_vulnibm_sh_namebufferoverflow_risklevel0)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_sh_namecommandexecution)+" VULNERABILIDADES EL NOMBRE INCLUYE COMMAND EXECUTION, LAS ESTADÍSTICAS DE PUNTUACION BASE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_sh_namecommandexecution_risklevel10)+" VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
print("            -    EN  "+str(count_vulnibm_sh_namecommandexecution_risklevel9)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN  "+str(count_vulnibm_sh_namecommandexecution_risklevel8)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN  "+str(count_vulnibm_sh_namecommandexecution_risklevel7)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN  "+str(count_vulnibm_sh_namecommandexecution_risklevel6)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN "+str(count_vulnibm_sh_namecommandexecution_risklevel5)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN "+str(count_vulnibm_sh_namecommandexecution_risklevel4)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN "+str(count_vulnibm_sh_namecommandexecution_risklevel3)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN "+str(count_vulnibm_sh_namecommandexecution_risklevel2)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN "+str(count_vulnibm_sh_namecommandexecution_risklevel1)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN "+str(count_vulnibm_sh_namecommandexecution_risklevel0)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_sh_namespoofing)+" VULNERABILIDADES EL NOMBRE INCLUYE SPOOFING, LAS ESTADÍSTICAS DE PUNTUACION BASE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_sh_namespoofing_risklevel10)+" VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
print("            -    EN  "+str(count_vulnibm_sh_namespoofing_risklevel9)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN  "+str(count_vulnibm_sh_namespoofing_risklevel8)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN  "+str(count_vulnibm_sh_namespoofing_risklevel7)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN  "+str(count_vulnibm_sh_namespoofing_risklevel6)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN "+str(count_vulnibm_sh_namespoofing_risklevel5)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN "+str(count_vulnibm_sh_namespoofing_risklevel4)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN "+str(count_vulnibm_sh_namespoofing_risklevel3)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN "+str(count_vulnibm_sh_namespoofing_risklevel2)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN "+str(count_vulnibm_sh_namespoofing_risklevel1)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN "+str(count_vulnibm_sh_namespoofing_risklevel0)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_sh_nameclickjacking)+" VULNERABILIDADES EL NOMBRE INCLUYE CLICKJACKING, LAS ESTADÍSTICAS DE PUNTUACION BASE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_sh_nameclickjacking_risklevel10)+" VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
print("            -    EN  "+str(count_vulnibm_sh_nameclickjacking_risklevel9)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN  "+str(count_vulnibm_sh_nameclickjacking_risklevel8)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN  "+str(count_vulnibm_sh_nameclickjacking_risklevel7)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN  "+str(count_vulnibm_sh_nameclickjacking_risklevel6)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN "+str(count_vulnibm_sh_nameclickjacking_risklevel5)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN "+str(count_vulnibm_sh_nameclickjacking_risklevel4)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN "+str(count_vulnibm_sh_nameclickjacking_risklevel3)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN "+str(count_vulnibm_sh_nameclickjacking_risklevel2)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN "+str(count_vulnibm_sh_nameclickjacking_risklevel1)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN "+str(count_vulnibm_sh_nameclickjacking_risklevel0)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_sh_namehijacking)+" VULNERABILIDADES EL NOMBRE INCLUYE HIJACKING, LAS ESTADÍSTICAS DE PUNTUACION BASE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_sh_namehijacking_risklevel10)+" VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
print("            -    EN  "+str(count_vulnibm_sh_namehijacking_risklevel9)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN  "+str(count_vulnibm_sh_namehijacking_risklevel8)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN  "+str(count_vulnibm_sh_namehijacking_risklevel7)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN  "+str(count_vulnibm_sh_namehijacking_risklevel6)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN "+str(count_vulnibm_sh_namehijacking_risklevel5)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN "+str(count_vulnibm_sh_namehijacking_risklevel4)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN "+str(count_vulnibm_sh_namehijacking_risklevel3)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN "+str(count_vulnibm_sh_namehijacking_risklevel2)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN "+str(count_vulnibm_sh_namehijacking_risklevel1)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN "+str(count_vulnibm_sh_namehijacking_risklevel0)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_sh_namefileinclude)+" VULNERABILIDADES EL NOMBRE INCLUYE FILEINCLUDE, LAS ESTADÍSTICAS DE PUNTUACION BASE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_sh_namefileinclude_risklevel10)+" VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
print("            -    EN  "+str(count_vulnibm_sh_namefileinclude_risklevel9)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN  "+str(count_vulnibm_sh_namefileinclude_risklevel8)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN  "+str(count_vulnibm_sh_namefileinclude_risklevel7)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN  "+str(count_vulnibm_sh_namefileinclude_risklevel6)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN "+str(count_vulnibm_sh_namefileinclude_risklevel5)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN "+str(count_vulnibm_sh_namefileinclude_risklevel4)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN "+str(count_vulnibm_sh_namefileinclude_risklevel3)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN "+str(count_vulnibm_sh_namefileinclude_risklevel2)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN "+str(count_vulnibm_sh_namefileinclude_risklevel1)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN "+str(count_vulnibm_sh_namefileinclude_risklevel0)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_sh_namebruteforce)+" VULNERABILIDADES EL NOMBRE INCLUYE BRUTEFORCE, LAS ESTADÍSTICAS DE PUNTUACION BASE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_sh_namebruteforce_risklevel10)+" VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
print("            -    EN  "+str(count_vulnibm_sh_namebruteforce_risklevel9)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN  "+str(count_vulnibm_sh_namebruteforce_risklevel8)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN  "+str(count_vulnibm_sh_namebruteforce_risklevel7)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN  "+str(count_vulnibm_sh_namebruteforce_risklevel6)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN "+str(count_vulnibm_sh_namebruteforce_risklevel5)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN "+str(count_vulnibm_sh_namebruteforce_risklevel4)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN "+str(count_vulnibm_sh_namebruteforce_risklevel3)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN "+str(count_vulnibm_sh_namebruteforce_risklevel2)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN "+str(count_vulnibm_sh_namebruteforce_risklevel1)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN "+str(count_vulnibm_sh_namebruteforce_risklevel0)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_sh_namefileupload)+" VULNERABILIDADES EL NOMBRE INCLUYE FILE UPLOAD, LAS ESTADÍSTICAS DE PUNTUACION BASE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_sh_namefileupload_risklevel10)+" VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
print("            -    EN  "+str(count_vulnibm_sh_namefileupload_risklevel9)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN  "+str(count_vulnibm_sh_namefileupload_risklevel8)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN  "+str(count_vulnibm_sh_namefileupload_risklevel7)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN  "+str(count_vulnibm_sh_namefileupload_risklevel6)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN "+str(count_vulnibm_sh_namefileupload_risklevel5)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN "+str(count_vulnibm_sh_namefileupload_risklevel4)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN "+str(count_vulnibm_sh_namefileupload_risklevel3)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN "+str(count_vulnibm_sh_namefileupload_risklevel2)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN "+str(count_vulnibm_sh_namefileupload_risklevel1)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN "+str(count_vulnibm_sh_namefileupload_risklevel0)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_sh_nameheaderinjection)+" VULNERABILIDADES EL NOMBRE INCLUYE HEADER INJECTION, LAS ESTADÍSTICAS DE PUNTUACION BASE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_sh_nameheaderinjection_risklevel10)+" VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
print("            -    EN  "+str(count_vulnibm_sh_nameheaderinjection_risklevel9)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN  "+str(count_vulnibm_sh_nameheaderinjection_risklevel8)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN  "+str(count_vulnibm_sh_nameheaderinjection_risklevel7)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN  "+str(count_vulnibm_sh_nameheaderinjection_risklevel6)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN "+str(count_vulnibm_sh_nameheaderinjection_risklevel5)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN "+str(count_vulnibm_sh_nameheaderinjection_risklevel4)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN "+str(count_vulnibm_sh_nameheaderinjection_risklevel3)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN "+str(count_vulnibm_sh_nameheaderinjection_risklevel2)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN "+str(count_vulnibm_sh_nameheaderinjection_risklevel1)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN "+str(count_vulnibm_sh_nameheaderinjection_risklevel0)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_sh_nametampering)+" VULNERABILIDADES EL NOMBRE INCLUYE TAMPERING, LAS ESTADÍSTICAS DE PUNTUACION BASE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_sh_nametampering_risklevel10)+" VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
print("            -    EN  "+str(count_vulnibm_sh_nametampering_risklevel9)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN  "+str(count_vulnibm_sh_nametampering_risklevel8)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN  "+str(count_vulnibm_sh_nametampering_risklevel7)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN  "+str(count_vulnibm_sh_nametampering_risklevel6)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN "+str(count_vulnibm_sh_nametampering_risklevel5)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN "+str(count_vulnibm_sh_nametampering_risklevel4)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN "+str(count_vulnibm_sh_nametampering_risklevel3)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN "+str(count_vulnibm_sh_nametampering_risklevel2)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN "+str(count_vulnibm_sh_nametampering_risklevel1)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN "+str(count_vulnibm_sh_nametampering_risklevel0)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_sh_nameanother)+" VULNERABILIDADES EL NOMBRE INCLUYE OTRA CADENA, LAS ESTADÍSTICAS DE PUNTUACION BASE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_sh_nameanother_risklevel10)+" VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
print("            -    EN  "+str(count_vulnibm_sh_nameanother_risklevel9)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN  "+str(count_vulnibm_sh_nameanother_risklevel8)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN  "+str(count_vulnibm_sh_nameanother_risklevel7)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN  "+str(count_vulnibm_sh_nameanother_risklevel6)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN "+str(count_vulnibm_sh_nameanother_risklevel5)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN "+str(count_vulnibm_sh_nameanother_risklevel4)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN "+str(count_vulnibm_sh_nameanother_risklevel3)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN "+str(count_vulnibm_sh_nameanother_risklevel2)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN "+str(count_vulnibm_sh_nameanother_risklevel1)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN "+str(count_vulnibm_sh_nameanother_risklevel0)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("\n")





print("*********************PORCENTAJE NOMBRE/PUNTUACION BASE OBJETOS DE TIPO VULNERABILIDAD IBM PARTE SMART HOME*********************")
print("\n")                            
print("\n")
print(" DE UN TOTAL DE "+str(count_vulnibm_sh_names)+" VULNERABILIDADES :\n") 
print("\n")
print("   - LOS PORCENTAJES DE VALORES DE NOMBRE SON LOS SIGUIENTES:  \n")
if(count_vulnibm_sh_namepathtraversal>0):
    print("      -    EN EL  "+str(float(((count_vulnibm_sh_namepathtraversal*100)/count_vulnibm_sh_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE PATH TRAVERSAL, LOS PORCENTAJES DE PUNTUACION BASE SON LOS SIGUIENTES :  \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namepathtraversal_risklevel10*100)/count_vulnibm_sh_namepathtraversal)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namepathtraversal_risklevel9*100)/count_vulnibm_sh_namepathtraversal)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namepathtraversal_risklevel8*100)/count_vulnibm_sh_namepathtraversal)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namepathtraversal_risklevel7*100)/count_vulnibm_sh_namepathtraversal)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namepathtraversal_risklevel6*100)/count_vulnibm_sh_namepathtraversal)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_sh_namepathtraversal_risklevel5*100)/count_vulnibm_sh_namepathtraversal)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_sh_namepathtraversal_risklevel4*100)/count_vulnibm_sh_namepathtraversal)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_sh_namepathtraversal_risklevel3*100)/count_vulnibm_sh_namepathtraversal)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_sh_namepathtraversal_risklevel2*100)/count_vulnibm_sh_namepathtraversal)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_sh_namepathtraversal_risklevel1*100)/count_vulnibm_sh_namepathtraversal)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_sh_namepathtraversal_risklevel0*100)/count_vulnibm_sh_namepathtraversal)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
    print("            -    EL VALOR MEDIO DE PUNTUACION BASE ES  "+str(float(((count_vulnibm_sh_namepathtraversal_risklevel)/count_vulnibm_sh_namepathtraversal)))+"\n")
    print("\n")
print("      -    EN EL  "+str(float(((count_vulnibm_sh_namedirectorytraversal*100)/count_vulnibm_sh_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE DIRECTORY TRAVERSAL, LOS PORCENTAJES DE PUNTUACION BASE SON LOS SIGUIENTES :  \n")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_namedirectorytraversal_risklevel10*100)/count_vulnibm_sh_namedirectorytraversal)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_namedirectorytraversal_risklevel9*100)/count_vulnibm_sh_namedirectorytraversal)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_namedirectorytraversal_risklevel8*100)/count_vulnibm_sh_namedirectorytraversal)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_namedirectorytraversal_risklevel7*100)/count_vulnibm_sh_namedirectorytraversal)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_namedirectorytraversal_risklevel6*100)/count_vulnibm_sh_namedirectorytraversal)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN EL "+str(float(((count_vulnibm_sh_namedirectorytraversal_risklevel5*100)/count_vulnibm_sh_namedirectorytraversal)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN EL "+str(float(((count_vulnibm_sh_namedirectorytraversal_risklevel4*100)/count_vulnibm_sh_namedirectorytraversal)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN EL "+str(float(((count_vulnibm_sh_namedirectorytraversal_risklevel3*100)/count_vulnibm_sh_namedirectorytraversal)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN EL "+str(float(((count_vulnibm_sh_namedirectorytraversal_risklevel2*100)/count_vulnibm_sh_namedirectorytraversal)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN EL "+str(float(((count_vulnibm_sh_namedirectorytraversal_risklevel1*100)/count_vulnibm_sh_namedirectorytraversal)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN EL "+str(float(((count_vulnibm_sh_namedirectorytraversal_risklevel0*100)/count_vulnibm_sh_namedirectorytraversal)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("            -    EL VALOR MEDIO DE PUNTUACION BASE ES  "+str(float(((count_vulnibm_sh_namedirectorytraversal_risklevel)/count_vulnibm_sh_namedirectorytraversal)))+"\n")
print("\n")
print("      -    EN EL  "+str(float(((count_vulnibm_sh_nameprivilegeescalation*100)/count_vulnibm_sh_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE PRIVILEGE ESCALATION, LOS PORCENTAJES DE PUNTUACION BASE SON LOS SIGUIENTES :  \n")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_nameprivilegeescalation_risklevel10*100)/count_vulnibm_sh_nameprivilegeescalation)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_nameprivilegeescalation_risklevel9*100)/count_vulnibm_sh_nameprivilegeescalation)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_nameprivilegeescalation_risklevel8*100)/count_vulnibm_sh_nameprivilegeescalation)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_nameprivilegeescalation_risklevel7*100)/count_vulnibm_sh_nameprivilegeescalation)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_nameprivilegeescalation_risklevel6*100)/count_vulnibm_sh_nameprivilegeescalation)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN EL "+str(float(((count_vulnibm_sh_nameprivilegeescalation_risklevel5*100)/count_vulnibm_sh_nameprivilegeescalation)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN EL "+str(float(((count_vulnibm_sh_nameprivilegeescalation_risklevel4*100)/count_vulnibm_sh_nameprivilegeescalation)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN EL "+str(float(((count_vulnibm_sh_nameprivilegeescalation_risklevel3*100)/count_vulnibm_sh_nameprivilegeescalation)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN EL "+str(float(((count_vulnibm_sh_nameprivilegeescalation_risklevel2*100)/count_vulnibm_sh_nameprivilegeescalation)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN EL "+str(float(((count_vulnibm_sh_nameprivilegeescalation_risklevel1*100)/count_vulnibm_sh_nameprivilegeescalation)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN EL "+str(float(((count_vulnibm_sh_nameprivilegeescalation_risklevel0*100)/count_vulnibm_sh_nameprivilegeescalation)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("            -    EL VALOR MEDIO DE PUNTUACION BASE ES  "+str(float(((count_vulnibm_sh_nameprivilegeescalation_risklevel)/count_vulnibm_sh_nameprivilegeescalation)))+"\n")
print("\n")
print("      -    EN EL  "+str(float(((count_vulnibm_sh_namecrosssitescripting*100)/count_vulnibm_sh_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE CROSS SITE SCRIPTING, LOS PORCENTAJES DE PUNTUACION BASE SON LOS SIGUIENTES :  \n")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_namecrosssitescripting_risklevel10*100)/count_vulnibm_sh_namecrosssitescripting)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_namecrosssitescripting_risklevel9*100)/count_vulnibm_sh_namecrosssitescripting)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_namecrosssitescripting_risklevel8*100)/count_vulnibm_sh_namecrosssitescripting)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_namecrosssitescripting_risklevel7*100)/count_vulnibm_sh_namecrosssitescripting)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_namecrosssitescripting_risklevel6*100)/count_vulnibm_sh_namecrosssitescripting)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN EL "+str(float(((count_vulnibm_sh_namecrosssitescripting_risklevel5*100)/count_vulnibm_sh_namecrosssitescripting)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN EL "+str(float(((count_vulnibm_sh_namecrosssitescripting_risklevel4*100)/count_vulnibm_sh_namecrosssitescripting)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN EL "+str(float(((count_vulnibm_sh_namecrosssitescripting_risklevel3*100)/count_vulnibm_sh_namecrosssitescripting)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN EL "+str(float(((count_vulnibm_sh_namecrosssitescripting_risklevel2*100)/count_vulnibm_sh_namecrosssitescripting)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN EL "+str(float(((count_vulnibm_sh_namecrosssitescripting_risklevel1*100)/count_vulnibm_sh_namecrosssitescripting)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN EL "+str(float(((count_vulnibm_sh_namecrosssitescripting_risklevel0*100)/count_vulnibm_sh_namecrosssitescripting)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("            -    EL VALOR MEDIO DE PUNTUACION BASE ES  "+str(float(((count_vulnibm_sh_namecrosssitescripting_risklevel)/count_vulnibm_sh_namecrosssitescripting)))+"\n")
print("\n")
print("      -    EN EL  "+str(float(((count_vulnibm_sh_namesecuritybypass*100)/count_vulnibm_sh_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE SECURITY BYPASS, LOS PORCENTAJES DE PUNTUACION BASE SON LOS SIGUIENTES :  \n")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_namesecuritybypass_risklevel10*100)/count_vulnibm_sh_namesecuritybypass)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_namesecuritybypass_risklevel9*100)/count_vulnibm_sh_namesecuritybypass)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_namesecuritybypass_risklevel8*100)/count_vulnibm_sh_namesecuritybypass)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_namesecuritybypass_risklevel7*100)/count_vulnibm_sh_namesecuritybypass)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_namesecuritybypass_risklevel6*100)/count_vulnibm_sh_namesecuritybypass)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN EL "+str(float(((count_vulnibm_sh_namesecuritybypass_risklevel5*100)/count_vulnibm_sh_namesecuritybypass)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN EL "+str(float(((count_vulnibm_sh_namesecuritybypass_risklevel4*100)/count_vulnibm_sh_namesecuritybypass)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN EL "+str(float(((count_vulnibm_sh_namesecuritybypass_risklevel3*100)/count_vulnibm_sh_namesecuritybypass)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN EL "+str(float(((count_vulnibm_sh_namesecuritybypass_risklevel2*100)/count_vulnibm_sh_namesecuritybypass)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN EL "+str(float(((count_vulnibm_sh_namesecuritybypass_risklevel1*100)/count_vulnibm_sh_namesecuritybypass)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN EL "+str(float(((count_vulnibm_sh_namesecuritybypass_risklevel0*100)/count_vulnibm_sh_namesecuritybypass)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("            -    EL VALOR MEDIO DE PUNTUACION BASE ES  "+str(float(((count_vulnibm_sh_namesecuritybypass_risklevel)/count_vulnibm_sh_namesecuritybypass)))+"\n")
print("\n")
print("      -    EN EL  "+str(float(((count_vulnibm_sh_nameinformationdisclosure*100)/count_vulnibm_sh_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE INFORMATION DISCLOSURE, LOS PORCENTAJES DE PUNTUACION BASE SON LOS SIGUIENTESS :  \n")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_nameinformationdisclosure_risklevel10*100)/count_vulnibm_sh_nameinformationdisclosure)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_nameinformationdisclosure_risklevel9*100)/count_vulnibm_sh_nameinformationdisclosure)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_nameinformationdisclosure_risklevel8*100)/count_vulnibm_sh_nameinformationdisclosure)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_nameinformationdisclosure_risklevel7*100)/count_vulnibm_sh_nameinformationdisclosure)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_nameinformationdisclosure_risklevel6*100)/count_vulnibm_sh_nameinformationdisclosure)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN EL "+str(float(((count_vulnibm_sh_nameinformationdisclosure_risklevel5*100)/count_vulnibm_sh_nameinformationdisclosure)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN EL "+str(float(((count_vulnibm_sh_nameinformationdisclosure_risklevel4*100)/count_vulnibm_sh_nameinformationdisclosure)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN EL "+str(float(((count_vulnibm_sh_nameinformationdisclosure_risklevel3*100)/count_vulnibm_sh_nameinformationdisclosure)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN EL "+str(float(((count_vulnibm_sh_nameinformationdisclosure_risklevel2*100)/count_vulnibm_sh_nameinformationdisclosure)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN EL "+str(float(((count_vulnibm_sh_nameinformationdisclosure_risklevel1*100)/count_vulnibm_sh_nameinformationdisclosure)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN EL "+str(float(((count_vulnibm_sh_nameinformationdisclosure_risklevel0*100)/count_vulnibm_sh_nameinformationdisclosure)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("            -    EL VALOR MEDIO DE PUNTUACION BASE ES  "+str(float(((count_vulnibm_sh_nameinformationdisclosure_risklevel)/count_vulnibm_sh_nameinformationdisclosure)))+"\n")
print("\n")
print("      -    EN EL  "+str(float(((count_vulnibm_sh_namedenialofservice*100)/count_vulnibm_sh_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE DENIAL OF SERVICE, LOS PORCENTAJES DE PUNTUACION BASE SON LOS SIGUIENTES :  \n")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_namedenialofservice_risklevel10*100)/count_vulnibm_sh_namedenialofservice)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_namedenialofservice_risklevel9*100)/count_vulnibm_sh_namedenialofservice)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_namedenialofservice_risklevel8*100)/count_vulnibm_sh_namedenialofservice)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_namedenialofservice_risklevel7*100)/count_vulnibm_sh_namedenialofservice)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_namedenialofservice_risklevel6*100)/count_vulnibm_sh_namedenialofservice)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN EL "+str(float(((count_vulnibm_sh_namedenialofservice_risklevel5*100)/count_vulnibm_sh_namedenialofservice)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN EL "+str(float(((count_vulnibm_sh_namedenialofservice_risklevel4*100)/count_vulnibm_sh_namedenialofservice)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN EL "+str(float(((count_vulnibm_sh_namedenialofservice_risklevel3*100)/count_vulnibm_sh_namedenialofservice)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN EL "+str(float(((count_vulnibm_sh_namedenialofservice_risklevel2*100)/count_vulnibm_sh_namedenialofservice)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN EL "+str(float(((count_vulnibm_sh_namedenialofservice_risklevel1*100)/count_vulnibm_sh_namedenialofservice)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN EL "+str(float(((count_vulnibm_sh_namedenialofservice_risklevel0*100)/count_vulnibm_sh_namedenialofservice)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("            -    EL VALOR MEDIO DE PUNTUACION BASE ES  "+str(float(((count_vulnibm_sh_namedenialofservice_risklevel)/count_vulnibm_sh_namedenialofservice)))+"\n")
print("\n")
print("      -    EN EL  "+str(float(((count_vulnibm_sh_namecodeexecution*100)/count_vulnibm_sh_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE CODE EXECUTION, LOS PORCENTAJES DE PUNTUACION BASE SON LOS SIGUIENTES :  \n")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_namecodeexecution_risklevel10*100)/count_vulnibm_sh_namecodeexecution)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_namecodeexecution_risklevel9*100)/count_vulnibm_sh_namecodeexecution)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_namecodeexecution_risklevel8*100)/count_vulnibm_sh_namecodeexecution)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_namecodeexecution_risklevel7*100)/count_vulnibm_sh_namecodeexecution)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_namecodeexecution_risklevel6*100)/count_vulnibm_sh_namecodeexecution)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN EL "+str(float(((count_vulnibm_sh_namecodeexecution_risklevel5*100)/count_vulnibm_sh_namecodeexecution)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN EL "+str(float(((count_vulnibm_sh_namecodeexecution_risklevel4*100)/count_vulnibm_sh_namecodeexecution)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN EL "+str(float(((count_vulnibm_sh_namecodeexecution_risklevel3*100)/count_vulnibm_sh_namecodeexecution)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN EL "+str(float(((count_vulnibm_sh_namecodeexecution_risklevel2*100)/count_vulnibm_sh_namecodeexecution)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN EL "+str(float(((count_vulnibm_sh_namecodeexecution_risklevel1*100)/count_vulnibm_sh_namecodeexecution)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN EL "+str(float(((count_vulnibm_sh_namecodeexecution_risklevel0*100)/count_vulnibm_sh_namecodeexecution)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("            -    EL VALOR MEDIO DE PUNTUACION BASE ES  "+str(float(((count_vulnibm_sh_namecodeexecution_risklevel)/count_vulnibm_sh_namecodeexecution)))+"\n")
print("\n")
if(count_vulnibm_sh_namemaninthemiddle>0):
    print("      -    EN EL  "+str(float(((count_vulnibm_sh_namemaninthemiddle*100)/count_vulnibm_sh_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE MAN IN THE MIDDLE, LOS PORCENTAJES DE PUNTUACION BASE SON LOS SIGUIENTES :  \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namemaninthemiddle_risklevel10*100)/count_vulnibm_sh_namemaninthemiddle)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namemaninthemiddle_risklevel9*100)/count_vulnibm_sh_namemaninthemiddle)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namemaninthemiddle_risklevel8*100)/count_vulnibm_sh_namemaninthemiddle)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namemaninthemiddle_risklevel7*100)/count_vulnibm_sh_namemaninthemiddle)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namemaninthemiddle_risklevel6*100)/count_vulnibm_sh_namemaninthemiddle)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_sh_namemaninthemiddle_risklevel5*100)/count_vulnibm_sh_namemaninthemiddle)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_sh_namemaninthemiddle_risklevel4*100)/count_vulnibm_sh_namemaninthemiddle)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_sh_namemaninthemiddle_risklevel3*100)/count_vulnibm_sh_namemaninthemiddle)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_sh_namemaninthemiddle_risklevel2*100)/count_vulnibm_sh_namemaninthemiddle)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_sh_namemaninthemiddle_risklevel1*100)/count_vulnibm_sh_namemaninthemiddle)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_sh_namemaninthemiddle_risklevel0*100)/count_vulnibm_sh_namemaninthemiddle)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
    print("            -    EL VALOR MEDIO DE PUNTUACION BASE ES  "+str(float(((count_vulnibm_sh_namemaninthemiddle_risklevel)/count_vulnibm_sh_namemaninthemiddle)))+"\n")
    print("\n")
if(count_vulnibm_sh_namesqlinjection>0):
    print("      -    EN EL  "+str(float(((count_vulnibm_sh_namesqlinjection*100)/count_vulnibm_sh_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE SQL INJECTION, LOS PORCENTAJES DE PUNTUACION BASE SON LOS SIGUIENTES :  \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namesqlinjection_risklevel10*100)/count_vulnibm_sh_namesqlinjection)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namesqlinjection_risklevel9*100)/count_vulnibm_sh_namesqlinjection)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namesqlinjection_risklevel8*100)/count_vulnibm_sh_namesqlinjection)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namesqlinjection_risklevel7*100)/count_vulnibm_sh_namesqlinjection)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namesqlinjection_risklevel6*100)/count_vulnibm_sh_namesqlinjection)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_sh_namesqlinjection_risklevel5*100)/count_vulnibm_sh_namesqlinjection)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_sh_namesqlinjection_risklevel4*100)/count_vulnibm_sh_namesqlinjection)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_sh_namesqlinjection_risklevel3*100)/count_vulnibm_sh_namesqlinjection)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_sh_namesqlinjection_risklevel2*100)/count_vulnibm_sh_namesqlinjection)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_sh_namesqlinjection_risklevel1*100)/count_vulnibm_sh_namesqlinjection)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_sh_namesqlinjection_risklevel0*100)/count_vulnibm_sh_namesqlinjection)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
    print("            -    EL VALOR MEDIO DE PUNTUACION BASE ES  "+str(float(((count_vulnibm_sh_namesqlinjection_risklevel)/count_vulnibm_sh_namesqlinjection)))+"\n")
    print("\n")
print("      -    EN EL  "+str(float(((count_vulnibm_sh_namecrosssiterequestforgery*100)/count_vulnibm_sh_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE CROSS SITE REQUEST FORGERY, LOS PORCENTAJES DE PUNTUACION BASE SON LOS SIGUIENTES :  \n")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_namecrosssiterequestforgery_risklevel10*100)/count_vulnibm_sh_namecrosssiterequestforgery)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_namecrosssiterequestforgery_risklevel9*100)/count_vulnibm_sh_namecrosssiterequestforgery)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_namecrosssiterequestforgery_risklevel8*100)/count_vulnibm_sh_namecrosssiterequestforgery)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_namecrosssiterequestforgery_risklevel7*100)/count_vulnibm_sh_namecrosssiterequestforgery)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_namecrosssiterequestforgery_risklevel6*100)/count_vulnibm_sh_namecrosssiterequestforgery)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN EL "+str(float(((count_vulnibm_sh_namecrosssiterequestforgery_risklevel5*100)/count_vulnibm_sh_namecrosssiterequestforgery)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN EL "+str(float(((count_vulnibm_sh_namecrosssiterequestforgery_risklevel4*100)/count_vulnibm_sh_namecrosssiterequestforgery)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN EL "+str(float(((count_vulnibm_sh_namecrosssiterequestforgery_risklevel3*100)/count_vulnibm_sh_namecrosssiterequestforgery)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN EL "+str(float(((count_vulnibm_sh_namecrosssiterequestforgery_risklevel2*100)/count_vulnibm_sh_namecrosssiterequestforgery)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN EL "+str(float(((count_vulnibm_sh_namecrosssiterequestforgery_risklevel1*100)/count_vulnibm_sh_namecrosssiterequestforgery)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN EL "+str(float(((count_vulnibm_sh_namecrosssiterequestforgery_risklevel0*100)/count_vulnibm_sh_namecrosssiterequestforgery)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("            -    EL VALOR MEDIO DE PUNTUACION BASE ES  "+str(float(((count_vulnibm_sh_namecrosssiterequestforgery_risklevel)/count_vulnibm_sh_namecrosssiterequestforgery)))+"\n")
print("\n")
if(count_vulnibm_sh_namemoduleexecution>0):
    print("      -    EN EL  "+str(float(((count_vulnibm_sh_namemoduleexecution*100)/count_vulnibm_sh_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE MODULE EXECUTION, LOS PORCENTAJES DE PUNTUACION BASE SON LOS SIGUIENTES :  \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namemoduleexecution_risklevel10*100)/count_vulnibm_sh_namemoduleexecution)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namemoduleexecution_risklevel9*100)/count_vulnibm_sh_namemoduleexecution)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namemoduleexecution_risklevel8*100)/count_vulnibm_sh_namemoduleexecution)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namemoduleexecution_risklevel7*100)/count_vulnibm_sh_namemoduleexecution)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namemoduleexecution_risklevel6*100)/count_vulnibm_sh_namemoduleexecution)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_sh_namemoduleexecution_risklevel5*100)/count_vulnibm_sh_namemoduleexecution)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_sh_namemoduleexecution_risklevel4*100)/count_vulnibm_sh_namemoduleexecution)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_sh_namemoduleexecution_risklevel3*100)/count_vulnibm_sh_namemoduleexecution)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_sh_namemoduleexecution_risklevel2*100)/count_vulnibm_sh_namemoduleexecution)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_sh_namemoduleexecution_risklevel1*100)/count_vulnibm_sh_namemoduleexecution)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_sh_namemoduleexecution_risklevel0*100)/count_vulnibm_sh_namemoduleexecution)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
    print("            -    EL VALOR MEDIO DE PUNTUACION BASE ES  "+str(float(((count_vulnibm_sh_namemoduleexecution_risklevel)/count_vulnibm_sh_namemoduleexecution)))+"\n")
    print("\n")
print("      -    EN EL  "+str(float(((count_vulnibm_sh_namebufferoverflow*100)/count_vulnibm_sh_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE BUFFER OVERFLOW, LOS PORCENTAJES DE PUNTUACION BASE SON LOS SIGUIENTES :  \n")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_namebufferoverflow_risklevel10*100)/count_vulnibm_sh_namebufferoverflow)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_namebufferoverflow_risklevel9*100)/count_vulnibm_sh_namebufferoverflow)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_namebufferoverflow_risklevel8*100)/count_vulnibm_sh_namebufferoverflow)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_namebufferoverflow_risklevel7*100)/count_vulnibm_sh_namebufferoverflow)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_namebufferoverflow_risklevel6*100)/count_vulnibm_sh_namebufferoverflow)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN EL "+str(float(((count_vulnibm_sh_namebufferoverflow_risklevel5*100)/count_vulnibm_sh_namebufferoverflow)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN EL "+str(float(((count_vulnibm_sh_namebufferoverflow_risklevel4*100)/count_vulnibm_sh_namebufferoverflow)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN EL "+str(float(((count_vulnibm_sh_namebufferoverflow_risklevel3*100)/count_vulnibm_sh_namebufferoverflow)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN EL "+str(float(((count_vulnibm_sh_namebufferoverflow_risklevel2*100)/count_vulnibm_sh_namebufferoverflow)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN EL "+str(float(((count_vulnibm_sh_namebufferoverflow_risklevel1*100)/count_vulnibm_sh_namebufferoverflow)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN EL "+str(float(((count_vulnibm_sh_namebufferoverflow_risklevel0*100)/count_vulnibm_sh_namebufferoverflow)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("            -    EL VALOR MEDIO DE PUNTUACION BASE ES  "+str(float(((count_vulnibm_sh_namebufferoverflow_risklevel)/count_vulnibm_sh_namebufferoverflow)))+"\n")
print("\n")
print("      -    EN EL  "+str(float(((count_vulnibm_sh_namecommandexecution*100)/count_vulnibm_sh_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE COMMAND EXECUTION, LOS PORCENTAJES DE PUNTUACION BASE SON LOS SIGUIENTES :  \n")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_namecommandexecution_risklevel10*100)/count_vulnibm_sh_namecommandexecution)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_namecommandexecution_risklevel9*100)/count_vulnibm_sh_namecommandexecution)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_namecommandexecution_risklevel8*100)/count_vulnibm_sh_namecommandexecution)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_namecommandexecution_risklevel7*100)/count_vulnibm_sh_namecommandexecution)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_namecommandexecution_risklevel6*100)/count_vulnibm_sh_namecommandexecution)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN EL "+str(float(((count_vulnibm_sh_namecommandexecution_risklevel5*100)/count_vulnibm_sh_namecommandexecution)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN EL "+str(float(((count_vulnibm_sh_namecommandexecution_risklevel4*100)/count_vulnibm_sh_namecommandexecution)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN EL "+str(float(((count_vulnibm_sh_namecommandexecution_risklevel3*100)/count_vulnibm_sh_namecommandexecution)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN EL "+str(float(((count_vulnibm_sh_namecommandexecution_risklevel2*100)/count_vulnibm_sh_namecommandexecution)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN EL "+str(float(((count_vulnibm_sh_namecommandexecution_risklevel1*100)/count_vulnibm_sh_namecommandexecution)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN EL "+str(float(((count_vulnibm_sh_namecommandexecution_risklevel0*100)/count_vulnibm_sh_namecommandexecution)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("            -    EL VALOR MEDIO DE PUNTUACION BASE ES  "+str(float(((count_vulnibm_sh_namecommandexecution_risklevel)/count_vulnibm_sh_namecommandexecution)))+"\n")
print("\n")
if(count_vulnibm_sh_namespoofing>0):
    print("      -    EN EL  "+str(float(((count_vulnibm_sh_namespoofing*100)/count_vulnibm_sh_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE SPOOFING, LOS PORCENTAJES DE PUNTUACION BASE SON LOS SIGUIENTES :  \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namespoofing_risklevel10*100)/count_vulnibm_sh_namespoofing)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namespoofing_risklevel9*100)/count_vulnibm_sh_namespoofing)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namespoofing_risklevel8*100)/count_vulnibm_sh_namespoofing)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namespoofing_risklevel7*100)/count_vulnibm_sh_namespoofing)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namespoofing_risklevel6*100)/count_vulnibm_sh_namespoofing)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_sh_namespoofing_risklevel5*100)/count_vulnibm_sh_namespoofing)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_sh_namespoofing_risklevel4*100)/count_vulnibm_sh_namespoofing)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_sh_namespoofing_risklevel3*100)/count_vulnibm_sh_namespoofing)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_sh_namespoofing_risklevel2*100)/count_vulnibm_sh_namespoofing)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_sh_namespoofing_risklevel1*100)/count_vulnibm_sh_namespoofing)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_sh_namespoofing_risklevel0*100)/count_vulnibm_sh_namespoofing)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
    print("            -    EL VALOR MEDIO DE PUNTUACION BASE ES  "+str(float(((count_vulnibm_sh_namespoofing_risklevel)/count_vulnibm_sh_namespoofing)))+"\n")
    print("\n")
if(count_vulnibm_sh_nameclickjacking>0):
    print("      -    EN EL  "+str(float(((count_vulnibm_sh_nameclickjacking*100)/count_vulnibm_sh_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE CLICKJACKING, LOS PORCENTAJES DE PUNTUACION BASE SON LOS SIGUIENTESS :  \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_nameclickjacking_risklevel10*100)/count_vulnibm_sh_nameclickjacking)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_nameclickjacking_risklevel9*100)/count_vulnibm_sh_nameclickjacking)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_nameclickjacking_risklevel8*100)/count_vulnibm_sh_nameclickjacking)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_nameclickjacking_risklevel7*100)/count_vulnibm_sh_nameclickjacking)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_nameclickjacking_risklevel6*100)/count_vulnibm_sh_nameclickjacking)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_sh_nameclickjacking_risklevel5*100)/count_vulnibm_sh_nameclickjacking)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_sh_nameclickjacking_risklevel4*100)/count_vulnibm_sh_nameclickjacking)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_sh_nameclickjacking_risklevel3*100)/count_vulnibm_sh_nameclickjacking)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_sh_nameclickjacking_risklevel2*100)/count_vulnibm_sh_nameclickjacking)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_sh_nameclickjacking_risklevel1*100)/count_vulnibm_sh_nameclickjacking)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_sh_nameclickjacking_risklevel0*100)/count_vulnibm_sh_nameclickjacking)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
    print("            -    EL VALOR MEDIO DE PUNTUACION BASE ES  "+str(float(((count_vulnibm_sh_nameclickjacking_risklevel)/count_vulnibm_sh_nameclickjacking)))+"\n")
    print("\n")
if(count_vulnibm_sh_namehijacking>0):
    print("      -    EN EL  "+str(float(((count_vulnibm_sh_namehijacking*100)/count_vulnibm_sh_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE HIJACKING, LOS PORCENTAJES DE PUNTUACION BASE SON LOS SIGUIENTES :  \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namehijacking_risklevel10*100)/count_vulnibm_sh_namehijacking)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namehijacking_risklevel9*100)/count_vulnibm_sh_namehijacking)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namehijacking_risklevel8*100)/count_vulnibm_sh_namehijacking)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namehijacking_risklevel7*100)/count_vulnibm_sh_namehijacking)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namehijacking_risklevel6*100)/count_vulnibm_sh_namehijacking)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_sh_namehijacking_risklevel5*100)/count_vulnibm_sh_namehijacking)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_sh_namehijacking_risklevel4*100)/count_vulnibm_sh_namehijacking)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_sh_namehijacking_risklevel3*100)/count_vulnibm_sh_namehijacking)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_sh_namehijacking_risklevel2*100)/count_vulnibm_sh_namehijacking)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_sh_namehijacking_risklevel1*100)/count_vulnibm_sh_namehijacking)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_sh_namehijacking_risklevel0*100)/count_vulnibm_sh_namehijacking)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
    print("            -    EL VALOR MEDIO DE PUNTUACION BASE ES  "+str(float(((count_vulnibm_sh_namehijacking_risklevel)/count_vulnibm_sh_namehijacking)))+"\n")
    print("\n")
if(count_vulnibm_sh_namefileinclude):
    print("      -    EN EL  "+str(float(((count_vulnibm_sh_namefileinclude*100)/count_vulnibm_sh_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE FILEINCLUDE, LOS PORCENTAJES DE PUNTUACION BASE SON LOS SIGUIENTES :  \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namefileinclude_risklevel10*100)/count_vulnibm_sh_namefileinclude)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namefileinclude_risklevel9*100)/count_vulnibm_sh_namefileinclude)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namefileinclude_risklevel8*100)/count_vulnibm_sh_namefileinclude)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namefileinclude_risklevel7*100)/count_vulnibm_sh_namefileinclude)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namefileinclude_risklevel6*100)/count_vulnibm_sh_namefileinclude)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_sh_namefileinclude_risklevel5*100)/count_vulnibm_sh_namefileinclude)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_sh_namefileinclude_risklevel4*100)/count_vulnibm_sh_namefileinclude)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_sh_namefileinclude_risklevel3*100)/count_vulnibm_sh_namefileinclude)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_sh_namefileinclude_risklevel2*100)/count_vulnibm_sh_namefileinclude)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_sh_namefileinclude_risklevel1*100)/count_vulnibm_sh_namefileinclude)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_sh_namefileinclude_risklevel0*100)/count_vulnibm_sh_namefileinclude)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
    print("            -    EL VALOR MEDIO DE PUNTUACION BASE ES  "+str(float(((count_vulnibm_sh_namefileinclude_risklevel)/count_vulnibm_sh_namefileinclude)))+"\n")
    print("\n")
if(count_vulnibm_sh_namebruteforce>0):
    print("      -    EN EL  "+str(float(((count_vulnibm_sh_namebruteforce*100)/count_vulnibm_sh_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE BRUTEFORCE, LOS PORCENTAJES DE PUNTUACION BASE SON LOS SIGUIENTES :  \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namebruteforce_risklevel10*100)/count_vulnibm_sh_namebruteforce)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namebruteforce_risklevel9*100)/count_vulnibm_sh_namebruteforce)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namebruteforce_risklevel8*100)/count_vulnibm_sh_namebruteforce)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namebruteforce_risklevel7*100)/count_vulnibm_sh_namebruteforce)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namebruteforce_risklevel6*100)/count_vulnibm_sh_namebruteforce)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_sh_namebruteforce_risklevel5*100)/count_vulnibm_sh_namebruteforce)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_sh_namebruteforce_risklevel4*100)/count_vulnibm_sh_namebruteforce)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_sh_namebruteforce_risklevel3*100)/count_vulnibm_sh_namebruteforce)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_sh_namebruteforce_risklevel2*100)/count_vulnibm_sh_namebruteforce)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_sh_namebruteforce_risklevel1*100)/count_vulnibm_sh_namebruteforce)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_sh_namebruteforce_risklevel0*100)/count_vulnibm_sh_namebruteforce)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
    print("            -    EL VALOR MEDIO DE PUNTUACION BASE ES  "+str(float(((count_vulnibm_sh_namebruteforce_risklevel)/count_vulnibm_sh_namebruteforce)))+"\n")
    print("\n")
if(count_vulnibm_sh_namefileupload>0):
    print("      -    EN EL  "+str(float(((count_vulnibm_sh_namefileupload*100)/count_vulnibm_sh_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE FILE UPLOAD, LOS PORCENTAJES DE PUNTUACION BASE SON LOS SIGUIENTES :  \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namefileupload_risklevel10*100)/count_vulnibm_sh_namefileupload)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namefileupload_risklevel9*100)/count_vulnibm_sh_namefileupload)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namefileupload_risklevel8*100)/count_vulnibm_sh_namefileupload)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namefileupload_risklevel7*100)/count_vulnibm_sh_namefileupload)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_namefileupload_risklevel6*100)/count_vulnibm_sh_namefileupload)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_sh_namefileupload_risklevel5*100)/count_vulnibm_sh_namefileupload)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_sh_namefileupload_risklevel4*100)/count_vulnibm_sh_namefileupload)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_sh_namefileupload_risklevel3*100)/count_vulnibm_sh_namefileupload)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_sh_namefileupload_risklevel2*100)/count_vulnibm_sh_namefileupload)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_sh_namefileupload_risklevel1*100)/count_vulnibm_sh_namefileupload)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_sh_namefileupload_risklevel0*100)/count_vulnibm_sh_namefileupload)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
    print("            -    EL VALOR MEDIO DE PUNTUACION BASE ES  "+str(float(((count_vulnibm_sh_namefileupload_risklevel)/count_vulnibm_sh_namefileupload)))+"\n")
    print("\n")
print("      -    EN EL  "+str(float(((count_vulnibm_sh_nameheaderinjection*100)/count_vulnibm_sh_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE HEADER INJECTION, LOS PORCENTAJES DE PUNTUACION BASE SON LOS SIGUIENTES :  \n")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_nameheaderinjection_risklevel10*100)/count_vulnibm_sh_nameheaderinjection)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_nameheaderinjection_risklevel9*100)/count_vulnibm_sh_nameheaderinjection)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_nameheaderinjection_risklevel8*100)/count_vulnibm_sh_nameheaderinjection)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_nameheaderinjection_risklevel7*100)/count_vulnibm_sh_nameheaderinjection)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_nameheaderinjection_risklevel6*100)/count_vulnibm_sh_nameheaderinjection)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN EL "+str(float(((count_vulnibm_sh_nameheaderinjection_risklevel5*100)/count_vulnibm_sh_nameheaderinjection)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN EL "+str(float(((count_vulnibm_sh_nameheaderinjection_risklevel4*100)/count_vulnibm_sh_nameheaderinjection)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN EL "+str(float(((count_vulnibm_sh_nameheaderinjection_risklevel3*100)/count_vulnibm_sh_nameheaderinjection)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN EL "+str(float(((count_vulnibm_sh_nameheaderinjection_risklevel2*100)/count_vulnibm_sh_nameheaderinjection)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN EL "+str(float(((count_vulnibm_sh_nameheaderinjection_risklevel1*100)/count_vulnibm_sh_nameheaderinjection)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN EL "+str(float(((count_vulnibm_sh_nameheaderinjection_risklevel0*100)/count_vulnibm_sh_nameheaderinjection)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("            -    EL VALOR MEDIO DE PUNTUACION BASE ES  "+str(float(((count_vulnibm_sh_nameheaderinjection_risklevel)/count_vulnibm_sh_nameheaderinjection)))+"\n")
print("\n")
if(count_vulnibm_sh_nametampering>0):
    print("      -    EN EL  "+str(float(((count_vulnibm_sh_nametampering*100)/count_vulnibm_sh_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE TAMPERING, LOS PORCENTAJES DE PUNTUACION BASE SON LOS SIGUIENTES :  \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_nametampering_risklevel10*100)/count_vulnibm_sh_nametampering)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_nametampering_risklevel9*100)/count_vulnibm_sh_nametampering)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_nametampering_risklevel8*100)/count_vulnibm_sh_nametampering)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_nametampering_risklevel7*100)/count_vulnibm_sh_nametampering)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_nametampering_risklevel6*100)/count_vulnibm_sh_nametampering)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_sh_nametampering_risklevel5*100)/count_vulnibm_sh_nametampering)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_sh_nametampering_risklevel4*100)/count_vulnibm_sh_nametampering)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_sh_nametampering_risklevel3*100)/count_vulnibm_sh_nametampering)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_sh_nametampering_risklevel2*100)/count_vulnibm_sh_nametampering)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_sh_nametampering_risklevel1*100)/count_vulnibm_sh_nametampering)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_sh_nametampering_risklevel0*100)/count_vulnibm_sh_nametampering)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
    print("            -    EL VALOR MEDIO DE PUNTUACION BASE ES  "+str(float(((count_vulnibm_sh_nametampering_risklevel)/count_vulnibm_sh_nametampering)))+"\n")
    print("\n")
if(count_vulnibm_sh_nameanother>0):
    print("      -    EN EL  "+str(float(((count_vulnibm_sh_nameanother*100)/count_vulnibm_sh_names)))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE OTRA CADENA, LOS PORCENTAJES DE PUNTUACION BASE SON LOS SIGUIENTES :  \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_nameanother_risklevel10*100)/count_vulnibm_sh_nameanother)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_nameanother_risklevel9*100)/count_vulnibm_sh_nameanother)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_nameanother_risklevel8*100)/count_vulnibm_sh_nameanother)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_nameanother_risklevel7*100)/count_vulnibm_sh_nameanother)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_nameanother_risklevel6*100)/count_vulnibm_sh_nameanother)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_sh_nameanother_risklevel5*100)/count_vulnibm_sh_nameanother)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_sh_nameanother_risklevel4*100)/count_vulnibm_sh_nameanother)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_sh_nameanother_risklevel3*100)/count_vulnibm_sh_nameanother)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_sh_nameanother_risklevel2*100)/count_vulnibm_sh_nameanother)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_sh_nameanother_risklevel1*100)/count_vulnibm_sh_nameanother)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_sh_nameanother_risklevel0*100)/count_vulnibm_sh_nameanother)))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
    print("            -    EL VALOR MEDIO DE PUNTUACION BASE ES  "+str(float(((count_vulnibm_sh_nameanother_risklevel)/count_vulnibm_sh_nameanother)))+"\n")
    print("\n")














print("*********************ESTADÍSTICAS NOMBRE/PUNTUACION BASE OBJETOS DE TIPO VULNERABILIDAD IBM PARTE IOT Y SMART HOME*********************")
print("\n")                            
print("\n")
print(" DE UN TOTAL DE "+str(count_vulnibm_iot_names+count_vulnibm_sh_names)+" VULNERABILIDADES:\n") 
print("\n")
print("   - LAS ESTADISTICAS DE VALORES DE NOMBRE SON LAS SIGUIENTES:  \n")
print("      -    EN  "+str(count_vulnibm_iot_namepathtraversal+count_vulnibm_sh_namepathtraversal)+" VULNERABILIDADES EL NOMBRE INCLUYE PATH TRAVERSAL, LAS ESTADÍSTICAS DE PUNTUACION BASE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_namepathtraversal_risklevel10+count_vulnibm_sh_namepathtraversal_risklevel10)+" VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
print("            -    EN  "+str(count_vulnibm_iot_namepathtraversal_risklevel9+count_vulnibm_sh_namepathtraversal_risklevel9)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN  "+str(count_vulnibm_iot_namepathtraversal_risklevel8+count_vulnibm_sh_namepathtraversal_risklevel8)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN  "+str(count_vulnibm_iot_namepathtraversal_risklevel7+count_vulnibm_sh_namepathtraversal_risklevel7)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN  "+str(count_vulnibm_iot_namepathtraversal_risklevel6+count_vulnibm_sh_namepathtraversal_risklevel6)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN "+str(count_vulnibm_iot_namepathtraversal_risklevel5+count_vulnibm_sh_namepathtraversal_risklevel5)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN "+str(count_vulnibm_iot_namepathtraversal_risklevel4+count_vulnibm_sh_namepathtraversal_risklevel4)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN "+str(count_vulnibm_iot_namepathtraversal_risklevel3+count_vulnibm_sh_namepathtraversal_risklevel3)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN "+str(count_vulnibm_iot_namepathtraversal_risklevel2+count_vulnibm_sh_namepathtraversal_risklevel2)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN "+str(count_vulnibm_iot_namepathtraversal_risklevel1+count_vulnibm_sh_namepathtraversal_risklevel1)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN "+str(count_vulnibm_iot_namepathtraversal_risklevel0+count_vulnibm_sh_namepathtraversal_risklevel0)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_namedirectorytraversal+count_vulnibm_sh_namedirectorytraversal)+" VULNERABILIDADES EL NOMBRE INCLUYE DIRECTORY TRAVERSAL, LAS ESTADÍSTICAS DE PUNTUACION BASE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_namedirectorytraversal_risklevel10+count_vulnibm_sh_namedirectorytraversal_risklevel10)+" VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
print("            -    EN  "+str(count_vulnibm_iot_namedirectorytraversal_risklevel9+count_vulnibm_sh_namedirectorytraversal_risklevel9)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN  "+str(count_vulnibm_iot_namedirectorytraversal_risklevel8+count_vulnibm_sh_namedirectorytraversal_risklevel8)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN  "+str(count_vulnibm_iot_namedirectorytraversal_risklevel7+count_vulnibm_sh_namedirectorytraversal_risklevel7)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN  "+str(count_vulnibm_iot_namedirectorytraversal_risklevel6+count_vulnibm_sh_namedirectorytraversal_risklevel6)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN "+str(count_vulnibm_iot_namedirectorytraversal_risklevel5+count_vulnibm_sh_namedirectorytraversal_risklevel5)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN "+str(count_vulnibm_iot_namedirectorytraversal_risklevel4+count_vulnibm_sh_namedirectorytraversal_risklevel4)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN "+str(count_vulnibm_iot_namedirectorytraversal_risklevel3+count_vulnibm_sh_namedirectorytraversal_risklevel3)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN "+str(count_vulnibm_iot_namedirectorytraversal_risklevel2+count_vulnibm_sh_namedirectorytraversal_risklevel2)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN "+str(count_vulnibm_iot_namedirectorytraversal_risklevel1+count_vulnibm_sh_namedirectorytraversal_risklevel1)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN "+str(count_vulnibm_iot_namedirectorytraversal_risklevel0+count_vulnibm_sh_namedirectorytraversal_risklevel0)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_nameprivilegeescalation+count_vulnibm_sh_nameprivilegeescalation)+" VULNERABILIDADES EL NOMBRE INCLUYE PRIVILEGE ESCALATION, LAS ESTADÍSTICAS DE PUNTUACION BASE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_nameprivilegeescalation_risklevel10+count_vulnibm_sh_nameprivilegeescalation_risklevel10)+" VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
print("            -    EN  "+str(count_vulnibm_iot_nameprivilegeescalation_risklevel9+count_vulnibm_sh_nameprivilegeescalation_risklevel9)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN  "+str(count_vulnibm_iot_nameprivilegeescalation_risklevel8+count_vulnibm_sh_nameprivilegeescalation_risklevel8)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN  "+str(count_vulnibm_iot_nameprivilegeescalation_risklevel7+count_vulnibm_sh_nameprivilegeescalation_risklevel7)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN  "+str(count_vulnibm_iot_nameprivilegeescalation_risklevel6+count_vulnibm_sh_nameprivilegeescalation_risklevel6)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN "+str(count_vulnibm_iot_nameprivilegeescalation_risklevel5+count_vulnibm_sh_nameprivilegeescalation_risklevel5)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN "+str(count_vulnibm_iot_nameprivilegeescalation_risklevel4+count_vulnibm_sh_nameprivilegeescalation_risklevel4)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN "+str(count_vulnibm_iot_nameprivilegeescalation_risklevel3+count_vulnibm_sh_nameprivilegeescalation_risklevel3)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN "+str(count_vulnibm_iot_nameprivilegeescalation_risklevel2+count_vulnibm_sh_nameprivilegeescalation_risklevel2)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN "+str(count_vulnibm_iot_nameprivilegeescalation_risklevel1+count_vulnibm_sh_nameprivilegeescalation_risklevel1)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN "+str(count_vulnibm_iot_nameprivilegeescalation_risklevel0+count_vulnibm_sh_nameprivilegeescalation_risklevel0)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_namecrosssitescripting+count_vulnibm_sh_namecrosssitescripting)+" VULNERABILIDADES EL NOMBRE INCLUYE CROSS SITE SCRIPTING, LAS ESTADÍSTICAS DE PUNTUACION BASE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_namecrosssitescripting_risklevel10+count_vulnibm_sh_namecrosssitescripting_risklevel10)+" VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
print("            -    EN  "+str(count_vulnibm_iot_namecrosssitescripting_risklevel9+count_vulnibm_sh_namecrosssitescripting_risklevel9)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN  "+str(count_vulnibm_iot_namecrosssitescripting_risklevel8+count_vulnibm_sh_namecrosssitescripting_risklevel8)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN  "+str(count_vulnibm_iot_namecrosssitescripting_risklevel7+count_vulnibm_sh_namecrosssitescripting_risklevel7)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN  "+str(count_vulnibm_iot_namecrosssitescripting_risklevel6+count_vulnibm_sh_namecrosssitescripting_risklevel6)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN "+str(count_vulnibm_iot_namecrosssitescripting_risklevel5+count_vulnibm_sh_namecrosssitescripting_risklevel5)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN "+str(count_vulnibm_iot_namecrosssitescripting_risklevel4+count_vulnibm_sh_namecrosssitescripting_risklevel4)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN "+str(count_vulnibm_iot_namecrosssitescripting_risklevel3+count_vulnibm_sh_namecrosssitescripting_risklevel3)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN "+str(count_vulnibm_iot_namecrosssitescripting_risklevel2+count_vulnibm_sh_namecrosssitescripting_risklevel2)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN "+str(count_vulnibm_iot_namecrosssitescripting_risklevel1+count_vulnibm_sh_namecrosssitescripting_risklevel1)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN "+str(count_vulnibm_iot_namecrosssitescripting_risklevel0+count_vulnibm_sh_namecrosssitescripting_risklevel0)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_namesecuritybypass+count_vulnibm_sh_namesecuritybypass)+" VULNERABILIDADES EL NOMBRE INCLUYE SECURITY BYPASS, LAS ESTADÍSTICAS DE PUNTUACION BASE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_namesecuritybypass_risklevel10+count_vulnibm_sh_namesecuritybypass_risklevel10)+" VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
print("            -    EN  "+str(count_vulnibm_iot_namesecuritybypass_risklevel9+count_vulnibm_sh_namesecuritybypass_risklevel9)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN  "+str(count_vulnibm_iot_namesecuritybypass_risklevel8+count_vulnibm_sh_namesecuritybypass_risklevel8)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN  "+str(count_vulnibm_iot_namesecuritybypass_risklevel7+count_vulnibm_sh_namesecuritybypass_risklevel7)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN  "+str(count_vulnibm_iot_namesecuritybypass_risklevel6+count_vulnibm_sh_namesecuritybypass_risklevel6)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN "+str(count_vulnibm_iot_namesecuritybypass_risklevel5+count_vulnibm_sh_namesecuritybypass_risklevel5)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN "+str(count_vulnibm_iot_namesecuritybypass_risklevel4+count_vulnibm_sh_namesecuritybypass_risklevel4)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN "+str(count_vulnibm_iot_namesecuritybypass_risklevel3+count_vulnibm_sh_namesecuritybypass_risklevel3)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN "+str(count_vulnibm_iot_namesecuritybypass_risklevel2+count_vulnibm_sh_namesecuritybypass_risklevel2)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN "+str(count_vulnibm_iot_namesecuritybypass_risklevel1+count_vulnibm_sh_namesecuritybypass_risklevel1)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN "+str(count_vulnibm_iot_namesecuritybypass_risklevel0+count_vulnibm_sh_namesecuritybypass_risklevel0)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_nameinformationdisclosure+count_vulnibm_sh_nameinformationdisclosure)+" VULNERABILIDADES EL NOMBRE INCLUYE INFORMATION DISCLOSURE, LAS ESTADÍSTICAS DE PUNTUACION BASE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_nameinformationdisclosure_risklevel10+count_vulnibm_sh_nameinformationdisclosure_risklevel10)+" VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
print("            -    EN  "+str(count_vulnibm_iot_nameinformationdisclosure_risklevel9+count_vulnibm_sh_nameinformationdisclosure_risklevel9)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN  "+str(count_vulnibm_iot_nameinformationdisclosure_risklevel8+count_vulnibm_sh_nameinformationdisclosure_risklevel8)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN  "+str(count_vulnibm_iot_nameinformationdisclosure_risklevel7+count_vulnibm_sh_nameinformationdisclosure_risklevel7)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN  "+str(count_vulnibm_iot_nameinformationdisclosure_risklevel6+count_vulnibm_sh_nameinformationdisclosure_risklevel6)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN "+str(count_vulnibm_iot_nameinformationdisclosure_risklevel5+count_vulnibm_sh_nameinformationdisclosure_risklevel5)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN "+str(count_vulnibm_iot_nameinformationdisclosure_risklevel4+count_vulnibm_sh_nameinformationdisclosure_risklevel4)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN "+str(count_vulnibm_iot_nameinformationdisclosure_risklevel3+count_vulnibm_sh_nameinformationdisclosure_risklevel3)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN "+str(count_vulnibm_iot_nameinformationdisclosure_risklevel2+count_vulnibm_sh_nameinformationdisclosure_risklevel2)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN "+str(count_vulnibm_iot_nameinformationdisclosure_risklevel1+count_vulnibm_sh_nameinformationdisclosure_risklevel1)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN "+str(count_vulnibm_iot_nameinformationdisclosure_risklevel0+count_vulnibm_sh_nameinformationdisclosure_risklevel0)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_namedenialofservice+count_vulnibm_sh_namedenialofservice)+" VULNERABILIDADES EL NOMBRE INCLUYE DENIAL OF SERVICE, LAS ESTADÍSTICAS DE PUNTUACION BASE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_namedenialofservice_risklevel10+count_vulnibm_sh_namedenialofservice_risklevel10)+" VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
print("            -    EN  "+str(count_vulnibm_iot_namedenialofservice_risklevel9+count_vulnibm_sh_namedenialofservice_risklevel9)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN  "+str(count_vulnibm_iot_namedenialofservice_risklevel8+count_vulnibm_sh_namedenialofservice_risklevel8)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN  "+str(count_vulnibm_iot_namedenialofservice_risklevel7+count_vulnibm_sh_namedenialofservice_risklevel7)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN  "+str(count_vulnibm_iot_namedenialofservice_risklevel6+count_vulnibm_sh_namedenialofservice_risklevel6)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN "+str(count_vulnibm_iot_namedenialofservice_risklevel5+count_vulnibm_sh_namedenialofservice_risklevel5)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN "+str(count_vulnibm_iot_namedenialofservice_risklevel4+count_vulnibm_sh_namedenialofservice_risklevel4)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN "+str(count_vulnibm_iot_namedenialofservice_risklevel3+count_vulnibm_sh_namedenialofservice_risklevel3)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN "+str(count_vulnibm_iot_namedenialofservice_risklevel2+count_vulnibm_sh_namedenialofservice_risklevel2)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN "+str(count_vulnibm_iot_namedenialofservice_risklevel1+count_vulnibm_sh_namedenialofservice_risklevel1)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN "+str(count_vulnibm_iot_namedenialofservice_risklevel0+count_vulnibm_sh_namedenialofservice_risklevel0)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_namecodeexecution+count_vulnibm_sh_namecodeexecution)+" VULNERABILIDADES EL NOMBRE INCLUYE CODE EXECUTION, LAS ESTADÍSTICAS DE PUNTUACION BASE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_namecodeexecution_risklevel10+count_vulnibm_sh_namecodeexecution_risklevel10)+" VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
print("            -    EN  "+str(count_vulnibm_iot_namecodeexecution_risklevel9+count_vulnibm_sh_namecodeexecution_risklevel9)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN  "+str(count_vulnibm_iot_namecodeexecution_risklevel8+count_vulnibm_sh_namecodeexecution_risklevel8)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN  "+str(count_vulnibm_iot_namecodeexecution_risklevel7+count_vulnibm_sh_namecodeexecution_risklevel7)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN  "+str(count_vulnibm_iot_namecodeexecution_risklevel6+count_vulnibm_sh_namecodeexecution_risklevel6)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN "+str(count_vulnibm_iot_namecodeexecution_risklevel5+count_vulnibm_sh_namecodeexecution_risklevel5)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN "+str(count_vulnibm_iot_namecodeexecution_risklevel4+count_vulnibm_sh_namecodeexecution_risklevel4)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN "+str(count_vulnibm_iot_namecodeexecution_risklevel3+count_vulnibm_sh_namecodeexecution_risklevel3)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN "+str(count_vulnibm_iot_namecodeexecution_risklevel2+count_vulnibm_sh_namecodeexecution_risklevel2)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN "+str(count_vulnibm_iot_namecodeexecution_risklevel1+count_vulnibm_sh_namecodeexecution_risklevel1)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN "+str(count_vulnibm_iot_namecodeexecution_risklevel0+count_vulnibm_sh_namecodeexecution_risklevel0)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_namemaninthemiddle+count_vulnibm_sh_namemaninthemiddle)+" VULNERABILIDADES EL NOMBRE INCLUYE MAN IN THE MIDDLE, LAS ESTADÍSTICAS DE PUNTUACION BASE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_namemaninthemiddle_risklevel10+count_vulnibm_sh_namemaninthemiddle_risklevel10)+" VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
print("            -    EN  "+str(count_vulnibm_iot_namemaninthemiddle_risklevel9+count_vulnibm_sh_namemaninthemiddle_risklevel9)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN  "+str(count_vulnibm_iot_namemaninthemiddle_risklevel8+count_vulnibm_sh_namemaninthemiddle_risklevel8)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN  "+str(count_vulnibm_iot_namemaninthemiddle_risklevel7+count_vulnibm_sh_namemaninthemiddle_risklevel7)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN  "+str(count_vulnibm_iot_namemaninthemiddle_risklevel6+count_vulnibm_sh_namemaninthemiddle_risklevel6)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN "+str(count_vulnibm_iot_namemaninthemiddle_risklevel5+count_vulnibm_sh_namemaninthemiddle_risklevel5)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN "+str(count_vulnibm_iot_namemaninthemiddle_risklevel4+count_vulnibm_sh_namemaninthemiddle_risklevel4)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN "+str(count_vulnibm_iot_namemaninthemiddle_risklevel3+count_vulnibm_sh_namemaninthemiddle_risklevel3)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN "+str(count_vulnibm_iot_namemaninthemiddle_risklevel2+count_vulnibm_sh_namemaninthemiddle_risklevel2)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN "+str(count_vulnibm_iot_namemaninthemiddle_risklevel1+count_vulnibm_sh_namemaninthemiddle_risklevel1)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN "+str(count_vulnibm_iot_namemaninthemiddle_risklevel0+count_vulnibm_sh_namemaninthemiddle_risklevel0)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_namesqlinjection+count_vulnibm_sh_namesqlinjection)+" VULNERABILIDADES EL NOMBRE INCLUYE SQL INJECTION, LAS ESTADÍSTICAS DE PUNTUACION BASE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_namesqlinjection_risklevel10+count_vulnibm_sh_namesqlinjection_risklevel10)+" VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
print("            -    EN  "+str(count_vulnibm_iot_namesqlinjection_risklevel9+count_vulnibm_sh_namesqlinjection_risklevel9)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN  "+str(count_vulnibm_iot_namesqlinjection_risklevel8+count_vulnibm_sh_namesqlinjection_risklevel8)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN  "+str(count_vulnibm_iot_namesqlinjection_risklevel7+count_vulnibm_sh_namesqlinjection_risklevel7)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN  "+str(count_vulnibm_iot_namesqlinjection_risklevel6+count_vulnibm_sh_namesqlinjection_risklevel6)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN "+str(count_vulnibm_iot_namesqlinjection_risklevel5+count_vulnibm_sh_namesqlinjection_risklevel5)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN "+str(count_vulnibm_iot_namesqlinjection_risklevel4+count_vulnibm_sh_namesqlinjection_risklevel4)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN "+str(count_vulnibm_iot_namesqlinjection_risklevel3+count_vulnibm_sh_namesqlinjection_risklevel3)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN "+str(count_vulnibm_iot_namesqlinjection_risklevel2+count_vulnibm_sh_namesqlinjection_risklevel2)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN "+str(count_vulnibm_iot_namesqlinjection_risklevel1+count_vulnibm_sh_namesqlinjection_risklevel1)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN "+str(count_vulnibm_iot_namesqlinjection_risklevel0+count_vulnibm_sh_namesqlinjection_risklevel0)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_namecrosssiterequestforgery+count_vulnibm_sh_namecrosssiterequestforgery)+" VULNERABILIDADES EL NOMBRE INCLUYE CROSS SITE REQUEST FORGERY, LAS ESTADÍSTICAS DE PUNTUACION BASE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_namecrosssiterequestforgery_risklevel10+count_vulnibm_sh_namecrosssiterequestforgery_risklevel10)+" VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
print("            -    EN  "+str(count_vulnibm_iot_namecrosssiterequestforgery_risklevel9+count_vulnibm_sh_namecrosssiterequestforgery_risklevel9)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN  "+str(count_vulnibm_iot_namecrosssiterequestforgery_risklevel8+count_vulnibm_sh_namecrosssiterequestforgery_risklevel8)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN  "+str(count_vulnibm_iot_namecrosssiterequestforgery_risklevel7+count_vulnibm_sh_namecrosssiterequestforgery_risklevel7)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN  "+str(count_vulnibm_iot_namecrosssiterequestforgery_risklevel6+count_vulnibm_sh_namecrosssiterequestforgery_risklevel6)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN "+str(count_vulnibm_iot_namecrosssiterequestforgery_risklevel5+count_vulnibm_sh_namecrosssiterequestforgery_risklevel5)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN "+str(count_vulnibm_iot_namecrosssiterequestforgery_risklevel4+count_vulnibm_sh_namecrosssiterequestforgery_risklevel4)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN "+str(count_vulnibm_iot_namecrosssiterequestforgery_risklevel3+count_vulnibm_sh_namecrosssiterequestforgery_risklevel3)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN "+str(count_vulnibm_iot_namecrosssiterequestforgery_risklevel2+count_vulnibm_sh_namecrosssiterequestforgery_risklevel2)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN "+str(count_vulnibm_iot_namecrosssiterequestforgery_risklevel1+count_vulnibm_sh_namecrosssiterequestforgery_risklevel1)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN "+str(count_vulnibm_iot_namecrosssiterequestforgery_risklevel0+count_vulnibm_sh_namecrosssiterequestforgery_risklevel0)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_namemoduleexecution+count_vulnibm_sh_namemoduleexecution)+" VULNERABILIDADES EL NOMBRE INCLUYE MODULE EXECUTION, LAS ESTADÍSTICAS DE PUNTUACION BASE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_namemoduleexecution_risklevel10+count_vulnibm_sh_namemoduleexecution_risklevel10)+" VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
print("            -    EN  "+str(count_vulnibm_iot_namemoduleexecution_risklevel9+count_vulnibm_sh_namemoduleexecution_risklevel9)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN  "+str(count_vulnibm_iot_namemoduleexecution_risklevel8+count_vulnibm_sh_namemoduleexecution_risklevel8)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN  "+str(count_vulnibm_iot_namemoduleexecution_risklevel7+count_vulnibm_sh_namemoduleexecution_risklevel7)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN  "+str(count_vulnibm_iot_namemoduleexecution_risklevel6+count_vulnibm_sh_namemoduleexecution_risklevel6)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN "+str(count_vulnibm_iot_namemoduleexecution_risklevel5+count_vulnibm_sh_namemoduleexecution_risklevel5)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN "+str(count_vulnibm_iot_namemoduleexecution_risklevel4+count_vulnibm_sh_namemoduleexecution_risklevel4)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN "+str(count_vulnibm_iot_namemoduleexecution_risklevel3+count_vulnibm_sh_namemoduleexecution_risklevel3)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN "+str(count_vulnibm_iot_namemoduleexecution_risklevel2+count_vulnibm_sh_namemoduleexecution_risklevel2)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN "+str(count_vulnibm_iot_namemoduleexecution_risklevel1+count_vulnibm_sh_namemoduleexecution_risklevel1)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN "+str(count_vulnibm_iot_namemoduleexecution_risklevel0+count_vulnibm_sh_namemoduleexecution_risklevel0)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_namebufferoverflow+count_vulnibm_sh_namebufferoverflow)+" VULNERABILIDADES EL NOMBRE INCLUYE BUFFER OVERFLOW, LAS ESTADÍSTICAS DE PUNTUACION BASE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_namebufferoverflow_risklevel10+count_vulnibm_sh_namebufferoverflow_risklevel10)+" VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
print("            -    EN  "+str(count_vulnibm_iot_namebufferoverflow_risklevel9+count_vulnibm_sh_namebufferoverflow_risklevel9)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN  "+str(count_vulnibm_iot_namebufferoverflow_risklevel8+count_vulnibm_sh_namebufferoverflow_risklevel8)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN  "+str(count_vulnibm_iot_namebufferoverflow_risklevel7+count_vulnibm_sh_namebufferoverflow_risklevel7)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN  "+str(count_vulnibm_iot_namebufferoverflow_risklevel6+count_vulnibm_sh_namebufferoverflow_risklevel6)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN "+str(count_vulnibm_iot_namebufferoverflow_risklevel5+count_vulnibm_sh_namebufferoverflow_risklevel5)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN "+str(count_vulnibm_iot_namebufferoverflow_risklevel4+count_vulnibm_sh_namebufferoverflow_risklevel4)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN "+str(count_vulnibm_iot_namebufferoverflow_risklevel3+count_vulnibm_sh_namebufferoverflow_risklevel3)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN "+str(count_vulnibm_iot_namebufferoverflow_risklevel2+count_vulnibm_sh_namebufferoverflow_risklevel2)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN "+str(count_vulnibm_iot_namebufferoverflow_risklevel1+count_vulnibm_sh_namebufferoverflow_risklevel1)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN "+str(count_vulnibm_iot_namebufferoverflow_risklevel0+count_vulnibm_sh_namebufferoverflow_risklevel0)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_namecommandexecution+count_vulnibm_sh_namecommandexecution)+" VULNERABILIDADES EL NOMBRE INCLUYE COMMAND EXECUTION, LAS ESTADÍSTICAS DE PUNTUACION BASE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_namecommandexecution_risklevel10+count_vulnibm_sh_namecommandexecution_risklevel10)+" VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
print("            -    EN  "+str(count_vulnibm_iot_namecommandexecution_risklevel9+count_vulnibm_sh_namecommandexecution_risklevel9)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN  "+str(count_vulnibm_iot_namecommandexecution_risklevel8+count_vulnibm_sh_namecommandexecution_risklevel8)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN  "+str(count_vulnibm_iot_namecommandexecution_risklevel7+count_vulnibm_sh_namecommandexecution_risklevel7)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN  "+str(count_vulnibm_iot_namecommandexecution_risklevel6+count_vulnibm_sh_namecommandexecution_risklevel6)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN "+str(count_vulnibm_iot_namecommandexecution_risklevel5+count_vulnibm_sh_namecommandexecution_risklevel5)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN "+str(count_vulnibm_iot_namecommandexecution_risklevel4+count_vulnibm_sh_namecommandexecution_risklevel4)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN "+str(count_vulnibm_iot_namecommandexecution_risklevel3+count_vulnibm_sh_namecommandexecution_risklevel3)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN "+str(count_vulnibm_iot_namecommandexecution_risklevel2+count_vulnibm_sh_namecommandexecution_risklevel2)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN "+str(count_vulnibm_iot_namecommandexecution_risklevel1+count_vulnibm_sh_namecommandexecution_risklevel1)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN "+str(count_vulnibm_iot_namecommandexecution_risklevel0+count_vulnibm_sh_namecommandexecution_risklevel0)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_namespoofing+count_vulnibm_sh_namespoofing)+" VULNERABILIDADES EL NOMBRE INCLUYE SPOOFING, LAS ESTADÍSTICAS DE PUNTUACION BASE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_namespoofing_risklevel10+count_vulnibm_sh_namespoofing_risklevel10)+" VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
print("            -    EN  "+str(count_vulnibm_iot_namespoofing_risklevel9+count_vulnibm_sh_namespoofing_risklevel9)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN  "+str(count_vulnibm_iot_namespoofing_risklevel8+count_vulnibm_sh_namespoofing_risklevel8)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN  "+str(count_vulnibm_iot_namespoofing_risklevel7+count_vulnibm_sh_namespoofing_risklevel7)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN  "+str(count_vulnibm_iot_namespoofing_risklevel6+count_vulnibm_sh_namespoofing_risklevel6)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN "+str(count_vulnibm_iot_namespoofing_risklevel5+count_vulnibm_sh_namespoofing_risklevel5)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN "+str(count_vulnibm_iot_namespoofing_risklevel4+count_vulnibm_sh_namespoofing_risklevel4)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN "+str(count_vulnibm_iot_namespoofing_risklevel3+count_vulnibm_sh_namespoofing_risklevel3)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN "+str(count_vulnibm_iot_namespoofing_risklevel2+count_vulnibm_sh_namespoofing_risklevel2)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN "+str(count_vulnibm_iot_namespoofing_risklevel1+count_vulnibm_sh_namespoofing_risklevel1)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN "+str(count_vulnibm_iot_namespoofing_risklevel0+count_vulnibm_sh_namespoofing_risklevel0)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_nameclickjacking+count_vulnibm_sh_nameclickjacking)+" VULNERABILIDADES EL NOMBRE INCLUYE CLICKJACKING, LAS ESTADÍSTICAS DE PUNTUACION BASE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_nameclickjacking_risklevel10+count_vulnibm_sh_nameclickjacking_risklevel10)+" VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
print("            -    EN  "+str(count_vulnibm_iot_nameclickjacking_risklevel9+count_vulnibm_sh_nameclickjacking_risklevel9)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN  "+str(count_vulnibm_iot_nameclickjacking_risklevel8+count_vulnibm_sh_nameclickjacking_risklevel8)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN  "+str(count_vulnibm_iot_nameclickjacking_risklevel7+count_vulnibm_sh_nameclickjacking_risklevel7)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN  "+str(count_vulnibm_iot_nameclickjacking_risklevel6+count_vulnibm_sh_nameclickjacking_risklevel6)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN "+str(count_vulnibm_iot_nameclickjacking_risklevel5+count_vulnibm_sh_nameclickjacking_risklevel5)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN "+str(count_vulnibm_iot_nameclickjacking_risklevel4+count_vulnibm_sh_nameclickjacking_risklevel4)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN "+str(count_vulnibm_iot_nameclickjacking_risklevel3+count_vulnibm_sh_nameclickjacking_risklevel3)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN "+str(count_vulnibm_iot_nameclickjacking_risklevel2+count_vulnibm_sh_nameclickjacking_risklevel2)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN "+str(count_vulnibm_iot_nameclickjacking_risklevel1+count_vulnibm_sh_nameclickjacking_risklevel1)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN "+str(count_vulnibm_iot_nameclickjacking_risklevel0+count_vulnibm_sh_nameclickjacking_risklevel0)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_namehijacking+count_vulnibm_sh_namehijacking)+" VULNERABILIDADES EL NOMBRE INCLUYE HIJACKING, LAS ESTADÍSTICAS DE PUNTUACION BASE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_namehijacking_risklevel10+count_vulnibm_sh_namehijacking_risklevel10)+" VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
print("            -    EN  "+str(count_vulnibm_iot_namehijacking_risklevel9+count_vulnibm_sh_namehijacking_risklevel9)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN  "+str(count_vulnibm_iot_namehijacking_risklevel8+count_vulnibm_sh_namehijacking_risklevel8)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN  "+str(count_vulnibm_iot_namehijacking_risklevel7+count_vulnibm_sh_namehijacking_risklevel7)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN  "+str(count_vulnibm_iot_namehijacking_risklevel6+count_vulnibm_sh_namehijacking_risklevel6)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN "+str(count_vulnibm_iot_namehijacking_risklevel5+count_vulnibm_sh_namehijacking_risklevel5)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN "+str(count_vulnibm_iot_namehijacking_risklevel4+count_vulnibm_sh_namehijacking_risklevel4)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN "+str(count_vulnibm_iot_namehijacking_risklevel3+count_vulnibm_sh_namehijacking_risklevel3)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN "+str(count_vulnibm_iot_namehijacking_risklevel2+count_vulnibm_sh_namehijacking_risklevel2)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN "+str(count_vulnibm_iot_namehijacking_risklevel1+count_vulnibm_sh_namehijacking_risklevel1)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN "+str(count_vulnibm_iot_namehijacking_risklevel0+count_vulnibm_sh_namehijacking_risklevel0)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_namefileinclude+count_vulnibm_sh_namefileinclude)+" VULNERABILIDADES EL NOMBRE INCLUYE FILE INCLUDE, LAS ESTADÍSTICAS DE PUNTUACION BASE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_namefileinclude_risklevel10+count_vulnibm_sh_namefileinclude_risklevel10)+" VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
print("            -    EN  "+str(count_vulnibm_iot_namefileinclude_risklevel9+count_vulnibm_sh_namefileinclude_risklevel9)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN  "+str(count_vulnibm_iot_namefileinclude_risklevel8+count_vulnibm_sh_namefileinclude_risklevel8)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN  "+str(count_vulnibm_iot_namefileinclude_risklevel7+count_vulnibm_sh_namefileinclude_risklevel7)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN  "+str(count_vulnibm_iot_namefileinclude_risklevel6+count_vulnibm_sh_namefileinclude_risklevel6)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN "+str(count_vulnibm_iot_namefileinclude_risklevel5+count_vulnibm_sh_namefileinclude_risklevel5)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN "+str(count_vulnibm_iot_namefileinclude_risklevel4+count_vulnibm_sh_namefileinclude_risklevel4)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN "+str(count_vulnibm_iot_namefileinclude_risklevel3+count_vulnibm_sh_namefileinclude_risklevel3)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN "+str(count_vulnibm_iot_namefileinclude_risklevel2+count_vulnibm_sh_namefileinclude_risklevel2)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN "+str(count_vulnibm_iot_namefileinclude_risklevel1+count_vulnibm_sh_namefileinclude_risklevel1)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN "+str(count_vulnibm_iot_namefileinclude_risklevel0+count_vulnibm_sh_namefileinclude_risklevel0)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_namebruteforce+count_vulnibm_sh_namebruteforce)+" VULNERABILIDADES EL NOMBRE INCLUYE BRUTE FORCE, LAS ESTADÍSTICAS DE PUNTUACION BASE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_namebruteforce_risklevel10+count_vulnibm_sh_namebruteforce_risklevel10)+" VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
print("            -    EN  "+str(count_vulnibm_iot_namebruteforce_risklevel9+count_vulnibm_sh_namebruteforce_risklevel9)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN  "+str(count_vulnibm_iot_namebruteforce_risklevel8+count_vulnibm_sh_namebruteforce_risklevel8)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN  "+str(count_vulnibm_iot_namebruteforce_risklevel7+count_vulnibm_sh_namebruteforce_risklevel7)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN  "+str(count_vulnibm_iot_namebruteforce_risklevel6+count_vulnibm_sh_namebruteforce_risklevel6)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN "+str(count_vulnibm_iot_namebruteforce_risklevel5+count_vulnibm_sh_namebruteforce_risklevel5)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN "+str(count_vulnibm_iot_namebruteforce_risklevel4+count_vulnibm_sh_namebruteforce_risklevel4)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN "+str(count_vulnibm_iot_namebruteforce_risklevel3+count_vulnibm_sh_namebruteforce_risklevel3)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN "+str(count_vulnibm_iot_namebruteforce_risklevel2+count_vulnibm_sh_namebruteforce_risklevel2)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN "+str(count_vulnibm_iot_namebruteforce_risklevel1+count_vulnibm_sh_namebruteforce_risklevel1)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN "+str(count_vulnibm_iot_namebruteforce_risklevel0+count_vulnibm_sh_namebruteforce_risklevel0)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_namefileupload+count_vulnibm_sh_namefileupload)+" VULNERABILIDADES EL NOMBRE INCLUYE FILE UPLOAD, LAS ESTADÍSTICAS DE PUNTUACION BASE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_namefileupload_risklevel10+count_vulnibm_sh_namefileupload_risklevel10)+" VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
print("            -    EN  "+str(count_vulnibm_iot_namefileupload_risklevel9+count_vulnibm_sh_namefileupload_risklevel9)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN  "+str(count_vulnibm_iot_namefileupload_risklevel8+count_vulnibm_sh_namefileupload_risklevel8)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN  "+str(count_vulnibm_iot_namefileupload_risklevel7+count_vulnibm_sh_namefileupload_risklevel7)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN  "+str(count_vulnibm_iot_namefileupload_risklevel6+count_vulnibm_sh_namefileupload_risklevel6)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN "+str(count_vulnibm_iot_namefileupload_risklevel5+count_vulnibm_sh_namefileupload_risklevel5)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN "+str(count_vulnibm_iot_namefileupload_risklevel4+count_vulnibm_sh_namefileupload_risklevel4)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN "+str(count_vulnibm_iot_namefileupload_risklevel3+count_vulnibm_sh_namefileupload_risklevel3)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN "+str(count_vulnibm_iot_namefileupload_risklevel2+count_vulnibm_sh_namefileupload_risklevel2)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN "+str(count_vulnibm_iot_namefileupload_risklevel1+count_vulnibm_sh_namefileupload_risklevel1)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN "+str(count_vulnibm_iot_namefileupload_risklevel0+count_vulnibm_sh_namefileupload_risklevel0)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_nameheaderinjection+count_vulnibm_sh_nameheaderinjection)+" VULNERABILIDADES EL NOMBRE INCLUYE HEADER INJECTION, LAS ESTADÍSTICAS DE PUNTUACION BASE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_nameheaderinjection_risklevel10+count_vulnibm_sh_nameheaderinjection_risklevel10)+" VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
print("            -    EN  "+str(count_vulnibm_iot_nameheaderinjection_risklevel9+count_vulnibm_sh_nameheaderinjection_risklevel9)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN  "+str(count_vulnibm_iot_nameheaderinjection_risklevel8+count_vulnibm_sh_nameheaderinjection_risklevel8)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN  "+str(count_vulnibm_iot_nameheaderinjection_risklevel7+count_vulnibm_sh_nameheaderinjection_risklevel7)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN  "+str(count_vulnibm_iot_nameheaderinjection_risklevel6+count_vulnibm_sh_nameheaderinjection_risklevel6)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN "+str(count_vulnibm_iot_nameheaderinjection_risklevel5+count_vulnibm_sh_nameheaderinjection_risklevel5)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN "+str(count_vulnibm_iot_nameheaderinjection_risklevel4+count_vulnibm_sh_nameheaderinjection_risklevel4)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN "+str(count_vulnibm_iot_nameheaderinjection_risklevel3+count_vulnibm_sh_nameheaderinjection_risklevel3)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN "+str(count_vulnibm_iot_nameheaderinjection_risklevel2+count_vulnibm_sh_nameheaderinjection_risklevel2)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN "+str(count_vulnibm_iot_nameheaderinjection_risklevel1+count_vulnibm_sh_nameheaderinjection_risklevel1)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN "+str(count_vulnibm_iot_nameheaderinjection_risklevel0+count_vulnibm_sh_nameheaderinjection_risklevel0)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_nametampering+count_vulnibm_sh_nametampering)+" VULNERABILIDADES EL NOMBRE INCLUYE TAMPERING, LAS ESTADÍSTICAS DE PUNTUACION BASE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_nametampering_risklevel10+count_vulnibm_sh_nametampering_risklevel10)+" VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
print("            -    EN  "+str(count_vulnibm_iot_nametampering_risklevel9+count_vulnibm_sh_nametampering_risklevel9)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN  "+str(count_vulnibm_iot_nametampering_risklevel8+count_vulnibm_sh_nametampering_risklevel8)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN  "+str(count_vulnibm_iot_nametampering_risklevel7+count_vulnibm_sh_nametampering_risklevel7)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN  "+str(count_vulnibm_iot_nametampering_risklevel6+count_vulnibm_sh_nametampering_risklevel6)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN "+str(count_vulnibm_iot_nametampering_risklevel5+count_vulnibm_sh_nametampering_risklevel5)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN "+str(count_vulnibm_iot_nametampering_risklevel4+count_vulnibm_sh_nametampering_risklevel4)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN "+str(count_vulnibm_iot_nametampering_risklevel3+count_vulnibm_sh_nametampering_risklevel3)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN "+str(count_vulnibm_iot_nametampering_risklevel2+count_vulnibm_sh_nametampering_risklevel2)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN "+str(count_vulnibm_iot_nametampering_risklevel1+count_vulnibm_sh_nametampering_risklevel1)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN "+str(count_vulnibm_iot_nametampering_risklevel0+count_vulnibm_sh_nametampering_risklevel0)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_nameanother+count_vulnibm_sh_nameanother)+" VULNERABILIDADES EL NOMBRE INCLUYE OTRO NOMBRE DISTINTO, LAS ESTADÍSTICAS DE PUNTUACION BASE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_nameanother_risklevel10+count_vulnibm_sh_nameanother_risklevel10)+" VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
print("            -    EN  "+str(count_vulnibm_iot_nameanother_risklevel9+count_vulnibm_sh_nameanother_risklevel9)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN  "+str(count_vulnibm_iot_nameanother_risklevel8+count_vulnibm_sh_nameanother_risklevel8)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN  "+str(count_vulnibm_iot_nameanother_risklevel7+count_vulnibm_sh_nameanother_risklevel7)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN  "+str(count_vulnibm_iot_nameanother_risklevel6+count_vulnibm_sh_nameanother_risklevel6)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN "+str(count_vulnibm_iot_nameanother_risklevel5+count_vulnibm_sh_nameanother_risklevel5)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN "+str(count_vulnibm_iot_nameanother_risklevel4+count_vulnibm_sh_nameanother_risklevel4)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN "+str(count_vulnibm_iot_nameanother_risklevel3+count_vulnibm_sh_nameanother_risklevel3)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN "+str(count_vulnibm_iot_nameanother_risklevel2+count_vulnibm_sh_nameanother_risklevel2)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN "+str(count_vulnibm_iot_nameanother_risklevel1+count_vulnibm_sh_nameanother_risklevel1)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN "+str(count_vulnibm_iot_nameanother_risklevel0+count_vulnibm_sh_nameanother_risklevel0)+" VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("\n")














print("*********************PORCENTAJES NOMBRE/PUNTUACION BASE OBJETOS DE TIPO VULNERABILIDAD IBM PARTE IOT Y SMART HOME*********************")
print("\n")                            
print("\n")
print(" DE UN TOTAL DE "+str(count_vulnibm_iot_names+count_vulnibm_sh_names)+" VULNERABILIDADES:\n")
print("\n")
print("   - LOS PORCENTAJES DE VALORES DE NOMBRE SON LOS SIGUIENTES:  \n")
print("      -    EN EL "+str(float((((count_vulnibm_iot_namepathtraversal+count_vulnibm_sh_namepathtraversal)*100)/(count_vulnibm_iot_names+count_vulnibm_sh_names))))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE PATHTRAVERSAL, LOS PORCENTAJES DE PUNTUACION BASE SON LOS SIGUIENTES :  \n")
print("            -    EN EL"+str(float((((count_vulnibm_iot_namepathtraversal_risklevel10+count_vulnibm_sh_namepathtraversal_risklevel10)*100)/(count_vulnibm_iot_namepathtraversal+count_vulnibm_sh_namepathtraversal))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namepathtraversal_risklevel9+count_vulnibm_sh_namepathtraversal_risklevel9)*100)/(count_vulnibm_iot_namepathtraversal+count_vulnibm_sh_namepathtraversal))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namepathtraversal_risklevel8+count_vulnibm_sh_namepathtraversal_risklevel8)*100)/(count_vulnibm_iot_namepathtraversal+count_vulnibm_sh_namepathtraversal))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namepathtraversal_risklevel7+count_vulnibm_sh_namepathtraversal_risklevel7)*100)/(count_vulnibm_iot_namepathtraversal+count_vulnibm_sh_namepathtraversal))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namepathtraversal_risklevel6+count_vulnibm_sh_namepathtraversal_risklevel6)*100)/(count_vulnibm_iot_namepathtraversal+count_vulnibm_sh_namepathtraversal))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namepathtraversal_risklevel5+count_vulnibm_sh_namepathtraversal_risklevel5)*100)/(count_vulnibm_iot_namepathtraversal+count_vulnibm_sh_namepathtraversal))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namepathtraversal_risklevel4+count_vulnibm_sh_namepathtraversal_risklevel4)*100)/(count_vulnibm_iot_namepathtraversal+count_vulnibm_sh_namepathtraversal))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namepathtraversal_risklevel3+count_vulnibm_sh_namepathtraversal_risklevel3)*100)/(count_vulnibm_iot_namepathtraversal+count_vulnibm_sh_namepathtraversal))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namepathtraversal_risklevel2+count_vulnibm_sh_namepathtraversal_risklevel2)*100)/(count_vulnibm_iot_namepathtraversal+count_vulnibm_sh_namepathtraversal))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namepathtraversal_risklevel1+count_vulnibm_sh_namepathtraversal_risklevel1)*100)/(count_vulnibm_iot_namepathtraversal+count_vulnibm_sh_namepathtraversal))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namepathtraversal_risklevel0+count_vulnibm_sh_namepathtraversal_risklevel0)*100)/(count_vulnibm_iot_namepathtraversal+count_vulnibm_sh_namepathtraversal))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("            -    EL VALOR MEDIO DE PUNTUACION BASE ES  "+str(float(((count_vulnibm_iot_namepathtraversal_risklevel+count_vulnibm_sh_namepathtraversal_risklevel)/(count_vulnibm_iot_namepathtraversal+count_vulnibm_sh_namepathtraversal))))+"\n")
print("\n")
print("      -    EN EL "+str(float((((count_vulnibm_iot_namedirectorytraversal+count_vulnibm_sh_namedirectorytraversal)*100)/(count_vulnibm_iot_names+count_vulnibm_sh_names))))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE DIRECTORY TRAVERSAL, LOS PORCENTAJES DE PUNTUACION BASE SON LOS SIGUIENTES :  \n")
print("            -    EN EL"+str(float((((count_vulnibm_iot_namedirectorytraversal_risklevel10+count_vulnibm_sh_namedirectorytraversal_risklevel10)*100)/(count_vulnibm_iot_namedirectorytraversal+count_vulnibm_sh_namedirectorytraversal))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namedirectorytraversal_risklevel9+count_vulnibm_sh_namedirectorytraversal_risklevel9)*100)/(count_vulnibm_iot_namedirectorytraversal+count_vulnibm_sh_namedirectorytraversal))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namedirectorytraversal_risklevel8+count_vulnibm_sh_namedirectorytraversal_risklevel8)*100)/(count_vulnibm_iot_namedirectorytraversal+count_vulnibm_sh_namedirectorytraversal))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namedirectorytraversal_risklevel7+count_vulnibm_sh_namedirectorytraversal_risklevel7)*100)/(count_vulnibm_iot_namedirectorytraversal+count_vulnibm_sh_namedirectorytraversal))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namedirectorytraversal_risklevel6+count_vulnibm_sh_namedirectorytraversal_risklevel6)*100)/(count_vulnibm_iot_namedirectorytraversal+count_vulnibm_sh_namedirectorytraversal))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namedirectorytraversal_risklevel5+count_vulnibm_sh_namedirectorytraversal_risklevel5)*100)/(count_vulnibm_iot_namedirectorytraversal+count_vulnibm_sh_namedirectorytraversal))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namedirectorytraversal_risklevel4+count_vulnibm_sh_namedirectorytraversal_risklevel4)*100)/(count_vulnibm_iot_namedirectorytraversal+count_vulnibm_sh_namedirectorytraversal))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namedirectorytraversal_risklevel3+count_vulnibm_sh_namedirectorytraversal_risklevel3)*100)/(count_vulnibm_iot_namedirectorytraversal+count_vulnibm_sh_namedirectorytraversal))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namedirectorytraversal_risklevel2+count_vulnibm_sh_namedirectorytraversal_risklevel2)*100)/(count_vulnibm_iot_namedirectorytraversal+count_vulnibm_sh_namedirectorytraversal))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namedirectorytraversal_risklevel1+count_vulnibm_sh_namedirectorytraversal_risklevel1)*100)/(count_vulnibm_iot_namedirectorytraversal+count_vulnibm_sh_namedirectorytraversal))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namedirectorytraversal_risklevel0+count_vulnibm_sh_namedirectorytraversal_risklevel0)*100)/(count_vulnibm_iot_namedirectorytraversal+count_vulnibm_sh_namedirectorytraversal))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("            -    EL VALOR MEDIO DE PUNTUACION BASE ES  "+str(float(((count_vulnibm_iot_namedirectorytraversal_risklevel+count_vulnibm_sh_namedirectorytraversal_risklevel)/(count_vulnibm_iot_namedirectorytraversal+count_vulnibm_sh_namedirectorytraversal))))+"\n")
print("\n")
print("      -    EN EL "+str(float((((count_vulnibm_iot_nameprivilegeescalation+count_vulnibm_sh_nameprivilegeescalation)*100)/(count_vulnibm_iot_names+count_vulnibm_sh_names))))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE PRIVILEGE ESCALATION, LOS PORCENTAJES DE PUNTUACION BASE SON LOS SIGUIENTES :  \n")
print("            -    EN EL"+str(float((((count_vulnibm_iot_nameprivilegeescalation_risklevel10+count_vulnibm_sh_nameprivilegeescalation_risklevel10)*100)/(count_vulnibm_iot_nameprivilegeescalation+count_vulnibm_sh_nameprivilegeescalation))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_nameprivilegeescalation_risklevel9+count_vulnibm_sh_nameprivilegeescalation_risklevel9)*100)/(count_vulnibm_iot_nameprivilegeescalation+count_vulnibm_sh_nameprivilegeescalation))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_nameprivilegeescalation_risklevel8+count_vulnibm_sh_nameprivilegeescalation_risklevel8)*100)/(count_vulnibm_iot_nameprivilegeescalation+count_vulnibm_sh_nameprivilegeescalation))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_nameprivilegeescalation_risklevel7+count_vulnibm_sh_nameprivilegeescalation_risklevel7)*100)/(count_vulnibm_iot_nameprivilegeescalation+count_vulnibm_sh_nameprivilegeescalation))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_nameprivilegeescalation_risklevel6+count_vulnibm_sh_nameprivilegeescalation_risklevel6)*100)/(count_vulnibm_iot_nameprivilegeescalation+count_vulnibm_sh_nameprivilegeescalation))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_nameprivilegeescalation_risklevel5+count_vulnibm_sh_nameprivilegeescalation_risklevel5)*100)/(count_vulnibm_iot_nameprivilegeescalation+count_vulnibm_sh_nameprivilegeescalation))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_nameprivilegeescalation_risklevel4+count_vulnibm_sh_nameprivilegeescalation_risklevel4)*100)/(count_vulnibm_iot_nameprivilegeescalation+count_vulnibm_sh_nameprivilegeescalation))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_nameprivilegeescalation_risklevel3+count_vulnibm_sh_nameprivilegeescalation_risklevel3)*100)/(count_vulnibm_iot_nameprivilegeescalation+count_vulnibm_sh_nameprivilegeescalation))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_nameprivilegeescalation_risklevel2+count_vulnibm_sh_nameprivilegeescalation_risklevel2)*100)/(count_vulnibm_iot_nameprivilegeescalation+count_vulnibm_sh_nameprivilegeescalation))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_nameprivilegeescalation_risklevel1+count_vulnibm_sh_nameprivilegeescalation_risklevel1)*100)/(count_vulnibm_iot_nameprivilegeescalation+count_vulnibm_sh_nameprivilegeescalation))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_nameprivilegeescalation_risklevel0+count_vulnibm_sh_nameprivilegeescalation_risklevel0)*100)/(count_vulnibm_iot_nameprivilegeescalation+count_vulnibm_sh_nameprivilegeescalation))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("            -    EL VALOR MEDIO DE PUNTUACION BASE ES  "+str(float(((count_vulnibm_iot_nameprivilegeescalation_risklevel+count_vulnibm_sh_nameprivilegeescalation_risklevel)/(count_vulnibm_iot_nameprivilegeescalation+count_vulnibm_sh_nameprivilegeescalation))))+"\n")
print("\n")
print("      -    EN EL "+str(float((((count_vulnibm_iot_namecrosssitescripting+count_vulnibm_sh_namecrosssitescripting)*100)/(count_vulnibm_iot_names+count_vulnibm_sh_names))))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE CROSS SITE SCRIPTING, LOS PORCENTAJES DE PUNTUACION BASE SON LOS SIGUIENTES :  \n")
print("            -    EN EL"+str(float((((count_vulnibm_iot_namecrosssitescripting_risklevel10+count_vulnibm_sh_namecrosssitescripting_risklevel10)*100)/(count_vulnibm_iot_namecrosssitescripting+count_vulnibm_sh_namecrosssitescripting))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namecrosssitescripting_risklevel9+count_vulnibm_sh_namecrosssitescripting_risklevel9)*100)/(count_vulnibm_iot_namecrosssitescripting+count_vulnibm_sh_namecrosssitescripting))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namecrosssitescripting_risklevel8+count_vulnibm_sh_namecrosssitescripting_risklevel8)*100)/(count_vulnibm_iot_namecrosssitescripting+count_vulnibm_sh_namecrosssitescripting))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namecrosssitescripting_risklevel7+count_vulnibm_sh_namecrosssitescripting_risklevel7)*100)/(count_vulnibm_iot_namecrosssitescripting+count_vulnibm_sh_namecrosssitescripting))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namecrosssitescripting_risklevel6+count_vulnibm_sh_namecrosssitescripting_risklevel6)*100)/(count_vulnibm_iot_namecrosssitescripting+count_vulnibm_sh_namecrosssitescripting))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namecrosssitescripting_risklevel5+count_vulnibm_sh_namecrosssitescripting_risklevel5)*100)/(count_vulnibm_iot_namecrosssitescripting+count_vulnibm_sh_namecrosssitescripting))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namecrosssitescripting_risklevel4+count_vulnibm_sh_namecrosssitescripting_risklevel4)*100)/(count_vulnibm_iot_namecrosssitescripting+count_vulnibm_sh_namecrosssitescripting))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namecrosssitescripting_risklevel3+count_vulnibm_sh_namecrosssitescripting_risklevel3)*100)/(count_vulnibm_iot_namecrosssitescripting+count_vulnibm_sh_namecrosssitescripting))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namecrosssitescripting_risklevel2+count_vulnibm_sh_namecrosssitescripting_risklevel2)*100)/(count_vulnibm_iot_namecrosssitescripting+count_vulnibm_sh_namecrosssitescripting))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namecrosssitescripting_risklevel1+count_vulnibm_sh_namecrosssitescripting_risklevel1)*100)/(count_vulnibm_iot_namecrosssitescripting+count_vulnibm_sh_namecrosssitescripting))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namecrosssitescripting_risklevel0+count_vulnibm_sh_namecrosssitescripting_risklevel0)*100)/(count_vulnibm_iot_namecrosssitescripting+count_vulnibm_sh_namecrosssitescripting))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("            -    EL VALOR MEDIO DE PUNTUACION BASE ES  "+str(float(((count_vulnibm_iot_namecrosssitescripting_risklevel+count_vulnibm_sh_namecrosssitescripting_risklevel)/(count_vulnibm_iot_namecrosssitescripting+count_vulnibm_sh_namecrosssitescripting))))+"\n")
print("\n")
print("      -    EN EL "+str(float((((count_vulnibm_iot_namesecuritybypass+count_vulnibm_sh_namesecuritybypass)*100)/(count_vulnibm_iot_names+count_vulnibm_sh_names))))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE SECURITY BYPASS, LOS PORCENTAJES DE PUNTUACION BASE SON LOS SIGUIENTES :  \n")
print("            -    EN EL"+str(float((((count_vulnibm_iot_namesecuritybypass_risklevel10+count_vulnibm_sh_namesecuritybypass_risklevel10)*100)/(count_vulnibm_iot_namesecuritybypass+count_vulnibm_sh_namesecuritybypass))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namesecuritybypass_risklevel9+count_vulnibm_sh_namesecuritybypass_risklevel9)*100)/(count_vulnibm_iot_namesecuritybypass+count_vulnibm_sh_namesecuritybypass))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namesecuritybypass_risklevel8+count_vulnibm_sh_namesecuritybypass_risklevel8)*100)/(count_vulnibm_iot_namesecuritybypass+count_vulnibm_sh_namesecuritybypass))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namesecuritybypass_risklevel7+count_vulnibm_sh_namesecuritybypass_risklevel7)*100)/(count_vulnibm_iot_namesecuritybypass+count_vulnibm_sh_namesecuritybypass))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namesecuritybypass_risklevel6+count_vulnibm_sh_namesecuritybypass_risklevel6)*100)/(count_vulnibm_iot_namesecuritybypass+count_vulnibm_sh_namesecuritybypass))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namesecuritybypass_risklevel5+count_vulnibm_sh_namesecuritybypass_risklevel5)*100)/(count_vulnibm_iot_namesecuritybypass+count_vulnibm_sh_namesecuritybypass))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namesecuritybypass_risklevel4+count_vulnibm_sh_namesecuritybypass_risklevel4)*100)/(count_vulnibm_iot_namesecuritybypass+count_vulnibm_sh_namesecuritybypass))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namesecuritybypass_risklevel3+count_vulnibm_sh_namesecuritybypass_risklevel3)*100)/(count_vulnibm_iot_namesecuritybypass+count_vulnibm_sh_namesecuritybypass))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namesecuritybypass_risklevel2+count_vulnibm_sh_namesecuritybypass_risklevel2)*100)/(count_vulnibm_iot_namesecuritybypass+count_vulnibm_sh_namesecuritybypass))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namesecuritybypass_risklevel1+count_vulnibm_sh_namesecuritybypass_risklevel1)*100)/(count_vulnibm_iot_namesecuritybypass+count_vulnibm_sh_namesecuritybypass))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namesecuritybypass_risklevel0+count_vulnibm_sh_namesecuritybypass_risklevel0)*100)/(count_vulnibm_iot_namesecuritybypass+count_vulnibm_sh_namesecuritybypass))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("            -    EL VALOR MEDIO DE PUNTUACION BASE ES  "+str(float(((count_vulnibm_iot_namesecuritybypass_risklevel+count_vulnibm_sh_namesecuritybypass_risklevel)/(count_vulnibm_iot_namesecuritybypass+count_vulnibm_sh_namesecuritybypass))))+"\n")
print("\n")
print("      -    EN EL "+str(float((((count_vulnibm_iot_nameinformationdisclosure+count_vulnibm_sh_nameinformationdisclosure)*100)/(count_vulnibm_iot_names+count_vulnibm_sh_names))))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE INFORMATION DISCLOSURE, LOS PORCENTAJES DE PUNTUACION BASE SON LOS SIGUIENTES :  \n")
print("            -    EN EL"+str(float((((count_vulnibm_iot_nameinformationdisclosure_risklevel10+count_vulnibm_sh_nameinformationdisclosure_risklevel10)*100)/(count_vulnibm_iot_nameinformationdisclosure+count_vulnibm_sh_nameinformationdisclosure))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_nameinformationdisclosure_risklevel9+count_vulnibm_sh_nameinformationdisclosure_risklevel9)*100)/(count_vulnibm_iot_nameinformationdisclosure+count_vulnibm_sh_nameinformationdisclosure))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_nameinformationdisclosure_risklevel8+count_vulnibm_sh_nameinformationdisclosure_risklevel8)*100)/(count_vulnibm_iot_nameinformationdisclosure+count_vulnibm_sh_nameinformationdisclosure))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_nameinformationdisclosure_risklevel7+count_vulnibm_sh_nameinformationdisclosure_risklevel7)*100)/(count_vulnibm_iot_nameinformationdisclosure+count_vulnibm_sh_nameinformationdisclosure))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_nameinformationdisclosure_risklevel6+count_vulnibm_sh_nameinformationdisclosure_risklevel6)*100)/(count_vulnibm_iot_nameinformationdisclosure+count_vulnibm_sh_nameinformationdisclosure))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_nameinformationdisclosure_risklevel5+count_vulnibm_sh_nameinformationdisclosure_risklevel5)*100)/(count_vulnibm_iot_nameinformationdisclosure+count_vulnibm_sh_nameinformationdisclosure))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_nameinformationdisclosure_risklevel4+count_vulnibm_sh_nameinformationdisclosure_risklevel4)*100)/(count_vulnibm_iot_nameinformationdisclosure+count_vulnibm_sh_nameinformationdisclosure))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_nameinformationdisclosure_risklevel3+count_vulnibm_sh_nameinformationdisclosure_risklevel3)*100)/(count_vulnibm_iot_nameinformationdisclosure+count_vulnibm_sh_nameinformationdisclosure))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_nameinformationdisclosure_risklevel2+count_vulnibm_sh_nameinformationdisclosure_risklevel2)*100)/(count_vulnibm_iot_nameinformationdisclosure+count_vulnibm_sh_nameinformationdisclosure))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_nameinformationdisclosure_risklevel1+count_vulnibm_sh_nameinformationdisclosure_risklevel1)*100)/(count_vulnibm_iot_nameinformationdisclosure+count_vulnibm_sh_nameinformationdisclosure))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_nameinformationdisclosure_risklevel0+count_vulnibm_sh_nameinformationdisclosure_risklevel0)*100)/(count_vulnibm_iot_nameinformationdisclosure+count_vulnibm_sh_nameinformationdisclosure))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("            -    EL VALOR MEDIO DE PUNTUACION BASE ES  "+str(float(((count_vulnibm_iot_nameinformationdisclosure_risklevel+count_vulnibm_sh_nameinformationdisclosure_risklevel)/(count_vulnibm_iot_nameinformationdisclosure+count_vulnibm_sh_nameinformationdisclosure))))+"\n")
print("\n")
print("      -    EN EL "+str(float((((count_vulnibm_iot_namedenialofservice+count_vulnibm_sh_namedenialofservice)*100)/(count_vulnibm_iot_names+count_vulnibm_sh_names))))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE DENIAL OF SERVICE, LOS PORCENTAJES DE PUNTUACION BASE SON LOS SIGUIENTES :  \n")
print("            -    EN EL"+str(float((((count_vulnibm_iot_namedenialofservice_risklevel10+count_vulnibm_sh_namedenialofservice_risklevel10)*100)/(count_vulnibm_iot_namedenialofservice+count_vulnibm_sh_namedenialofservice))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namedenialofservice_risklevel9+count_vulnibm_sh_namedenialofservice_risklevel9)*100)/(count_vulnibm_iot_namedenialofservice+count_vulnibm_sh_namedenialofservice))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namedenialofservice_risklevel8+count_vulnibm_sh_namedenialofservice_risklevel8)*100)/(count_vulnibm_iot_namedenialofservice+count_vulnibm_sh_namedenialofservice))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namedenialofservice_risklevel7+count_vulnibm_sh_namedenialofservice_risklevel7)*100)/(count_vulnibm_iot_namedenialofservice+count_vulnibm_sh_namedenialofservice))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namedenialofservice_risklevel6+count_vulnibm_sh_namedenialofservice_risklevel6)*100)/(count_vulnibm_iot_namedenialofservice+count_vulnibm_sh_namedenialofservice))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namedenialofservice_risklevel5+count_vulnibm_sh_namedenialofservice_risklevel5)*100)/(count_vulnibm_iot_namedenialofservice+count_vulnibm_sh_namedenialofservice))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namedenialofservice_risklevel4+count_vulnibm_sh_namedenialofservice_risklevel4)*100)/(count_vulnibm_iot_namedenialofservice+count_vulnibm_sh_namedenialofservice))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namedenialofservice_risklevel3+count_vulnibm_sh_namedenialofservice_risklevel3)*100)/(count_vulnibm_iot_namedenialofservice+count_vulnibm_sh_namedenialofservice))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namedenialofservice_risklevel2+count_vulnibm_sh_namedenialofservice_risklevel2)*100)/(count_vulnibm_iot_namedenialofservice+count_vulnibm_sh_namedenialofservice))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namedenialofservice_risklevel1+count_vulnibm_sh_namedenialofservice_risklevel1)*100)/(count_vulnibm_iot_namedenialofservice+count_vulnibm_sh_namedenialofservice))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namedenialofservice_risklevel0+count_vulnibm_sh_namedenialofservice_risklevel0)*100)/(count_vulnibm_iot_namedenialofservice+count_vulnibm_sh_namedenialofservice))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("            -    EL VALOR MEDIO DE PUNTUACION BASE ES  "+str(float(((count_vulnibm_iot_namedenialofservice_risklevel+count_vulnibm_sh_namedenialofservice_risklevel)/(count_vulnibm_iot_namedenialofservice+count_vulnibm_sh_namedenialofservice))))+"\n")
print("\n")
print("      -    EN EL "+str(float((((count_vulnibm_iot_namecodeexecution+count_vulnibm_sh_namecodeexecution)*100)/(count_vulnibm_iot_names+count_vulnibm_sh_names))))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE CODE EXECUTION, LOS PORCENTAJES DE PUNTUACION BASE SON LOS SIGUIENTES :  \n")
print("            -    EN EL"+str(float((((count_vulnibm_iot_namecodeexecution_risklevel10+count_vulnibm_sh_namecodeexecution_risklevel10)*100)/(count_vulnibm_iot_namecodeexecution+count_vulnibm_sh_namecodeexecution))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namecodeexecution_risklevel9+count_vulnibm_sh_namecodeexecution_risklevel9)*100)/(count_vulnibm_iot_namecodeexecution+count_vulnibm_sh_namecodeexecution))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namecodeexecution_risklevel8+count_vulnibm_sh_namecodeexecution_risklevel8)*100)/(count_vulnibm_iot_namecodeexecution+count_vulnibm_sh_namecodeexecution))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namecodeexecution_risklevel7+count_vulnibm_sh_namecodeexecution_risklevel7)*100)/(count_vulnibm_iot_namecodeexecution+count_vulnibm_sh_namecodeexecution))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namecodeexecution_risklevel6+count_vulnibm_sh_namecodeexecution_risklevel6)*100)/(count_vulnibm_iot_namecodeexecution+count_vulnibm_sh_namecodeexecution))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namecodeexecution_risklevel5+count_vulnibm_sh_namecodeexecution_risklevel5)*100)/(count_vulnibm_iot_namecodeexecution+count_vulnibm_sh_namecodeexecution))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namecodeexecution_risklevel4+count_vulnibm_sh_namecodeexecution_risklevel4)*100)/(count_vulnibm_iot_namecodeexecution+count_vulnibm_sh_namecodeexecution))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namecodeexecution_risklevel3+count_vulnibm_sh_namecodeexecution_risklevel3)*100)/(count_vulnibm_iot_namecodeexecution+count_vulnibm_sh_namecodeexecution))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namecodeexecution_risklevel2+count_vulnibm_sh_namecodeexecution_risklevel2)*100)/(count_vulnibm_iot_namecodeexecution+count_vulnibm_sh_namecodeexecution))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namecodeexecution_risklevel1+count_vulnibm_sh_namecodeexecution_risklevel1)*100)/(count_vulnibm_iot_namecodeexecution+count_vulnibm_sh_namecodeexecution))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namecodeexecution_risklevel0+count_vulnibm_sh_namecodeexecution_risklevel0)*100)/(count_vulnibm_iot_namecodeexecution+count_vulnibm_sh_namecodeexecution))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("            -    EL VALOR MEDIO DE PUNTUACION BASE ES  "+str(float(((count_vulnibm_iot_namecodeexecution_risklevel+count_vulnibm_sh_namecodeexecution_risklevel)/(count_vulnibm_iot_namecodeexecution+count_vulnibm_sh_namecodeexecution))))+"\n")
print("\n")
print("      -    EN EL "+str(float((((count_vulnibm_iot_namemaninthemiddle+count_vulnibm_sh_namemaninthemiddle)*100)/(count_vulnibm_iot_names+count_vulnibm_sh_names))))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE MAN IN THE MIDDLE, LOS PORCENTAJES DE PUNTUACION BASE SON LOS SIGUIENTES :  \n")
print("            -    EN EL"+str(float((((count_vulnibm_iot_namemaninthemiddle_risklevel10+count_vulnibm_sh_namemaninthemiddle_risklevel10)*100)/(count_vulnibm_iot_namemaninthemiddle+count_vulnibm_sh_namemaninthemiddle))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namemaninthemiddle_risklevel9+count_vulnibm_sh_namemaninthemiddle_risklevel9)*100)/(count_vulnibm_iot_namemaninthemiddle+count_vulnibm_sh_namemaninthemiddle))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namemaninthemiddle_risklevel8+count_vulnibm_sh_namemaninthemiddle_risklevel8)*100)/(count_vulnibm_iot_namemaninthemiddle+count_vulnibm_sh_namemaninthemiddle))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namemaninthemiddle_risklevel7+count_vulnibm_sh_namemaninthemiddle_risklevel7)*100)/(count_vulnibm_iot_namemaninthemiddle+count_vulnibm_sh_namemaninthemiddle))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namemaninthemiddle_risklevel6+count_vulnibm_sh_namemaninthemiddle_risklevel6)*100)/(count_vulnibm_iot_namemaninthemiddle+count_vulnibm_sh_namemaninthemiddle))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namemaninthemiddle_risklevel5+count_vulnibm_sh_namemaninthemiddle_risklevel5)*100)/(count_vulnibm_iot_namemaninthemiddle+count_vulnibm_sh_namemaninthemiddle))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namemaninthemiddle_risklevel4+count_vulnibm_sh_namemaninthemiddle_risklevel4)*100)/(count_vulnibm_iot_namemaninthemiddle+count_vulnibm_sh_namemaninthemiddle))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namemaninthemiddle_risklevel3+count_vulnibm_sh_namemaninthemiddle_risklevel3)*100)/(count_vulnibm_iot_namemaninthemiddle+count_vulnibm_sh_namemaninthemiddle))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namemaninthemiddle_risklevel2+count_vulnibm_sh_namemaninthemiddle_risklevel2)*100)/(count_vulnibm_iot_namemaninthemiddle+count_vulnibm_sh_namemaninthemiddle))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namemaninthemiddle_risklevel1+count_vulnibm_sh_namemaninthemiddle_risklevel1)*100)/(count_vulnibm_iot_namemaninthemiddle+count_vulnibm_sh_namemaninthemiddle))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namemaninthemiddle_risklevel0+count_vulnibm_sh_namemaninthemiddle_risklevel0)*100)/(count_vulnibm_iot_namemaninthemiddle+count_vulnibm_sh_namemaninthemiddle))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("            -    EL VALOR MEDIO DE PUNTUACION BASE ES  "+str(float(((count_vulnibm_iot_namemaninthemiddle_risklevel+count_vulnibm_sh_namemaninthemiddle_risklevel)/(count_vulnibm_iot_namemaninthemiddle+count_vulnibm_sh_namemaninthemiddle))))+"\n")
print("\n")
print("      -    EN EL "+str(float((((count_vulnibm_iot_namesqlinjection+count_vulnibm_sh_namesqlinjection)*100)/(count_vulnibm_iot_names+count_vulnibm_sh_names))))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE SQL INJECTION, LOS PORCENTAJES DE PUNTUACION BASE SON LOS SIGUIENTES :  \n")
print("            -    EN EL"+str(float((((count_vulnibm_iot_namesqlinjection_risklevel10+count_vulnibm_sh_namesqlinjection_risklevel10)*100)/(count_vulnibm_iot_namesqlinjection+count_vulnibm_sh_namesqlinjection))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namesqlinjection_risklevel9+count_vulnibm_sh_namesqlinjection_risklevel9)*100)/(count_vulnibm_iot_namesqlinjection+count_vulnibm_sh_namesqlinjection))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namesqlinjection_risklevel8+count_vulnibm_sh_namesqlinjection_risklevel8)*100)/(count_vulnibm_iot_namesqlinjection+count_vulnibm_sh_namesqlinjection))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namesqlinjection_risklevel7+count_vulnibm_sh_namesqlinjection_risklevel7)*100)/(count_vulnibm_iot_namesqlinjection+count_vulnibm_sh_namesqlinjection))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namesqlinjection_risklevel6+count_vulnibm_sh_namesqlinjection_risklevel6)*100)/(count_vulnibm_iot_namesqlinjection+count_vulnibm_sh_namesqlinjection))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namesqlinjection_risklevel5+count_vulnibm_sh_namesqlinjection_risklevel5)*100)/(count_vulnibm_iot_namesqlinjection+count_vulnibm_sh_namesqlinjection))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namesqlinjection_risklevel4+count_vulnibm_sh_namesqlinjection_risklevel4)*100)/(count_vulnibm_iot_namesqlinjection+count_vulnibm_sh_namesqlinjection))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namesqlinjection_risklevel3+count_vulnibm_sh_namesqlinjection_risklevel3)*100)/(count_vulnibm_iot_namesqlinjection+count_vulnibm_sh_namesqlinjection))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namesqlinjection_risklevel2+count_vulnibm_sh_namesqlinjection_risklevel2)*100)/(count_vulnibm_iot_namesqlinjection+count_vulnibm_sh_namesqlinjection))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namesqlinjection_risklevel1+count_vulnibm_sh_namesqlinjection_risklevel1)*100)/(count_vulnibm_iot_namesqlinjection+count_vulnibm_sh_namesqlinjection))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namesqlinjection_risklevel0+count_vulnibm_sh_namesqlinjection_risklevel0)*100)/(count_vulnibm_iot_namesqlinjection+count_vulnibm_sh_namesqlinjection))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("            -    EL VALOR MEDIO DE PUNTUACION BASE ES  "+str(float(((count_vulnibm_iot_namesqlinjection_risklevel+count_vulnibm_sh_namesqlinjection_risklevel)/(count_vulnibm_iot_namesqlinjection+count_vulnibm_sh_namesqlinjection))))+"\n")
print("\n")
print("      -    EN EL "+str(float((((count_vulnibm_iot_namecrosssiterequestforgery+count_vulnibm_sh_namecrosssiterequestforgery)*100)/(count_vulnibm_iot_names+count_vulnibm_sh_names))))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE CROSS SITE REQUEST FORGERY, LOS PORCENTAJES DE PUNTUACION BASE SON LOS SIGUIENTES :  \n")
print("            -    EN EL"+str(float((((count_vulnibm_iot_namecrosssiterequestforgery_risklevel10+count_vulnibm_sh_namecrosssiterequestforgery_risklevel10)*100)/(count_vulnibm_iot_namecrosssiterequestforgery+count_vulnibm_sh_namecrosssiterequestforgery))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namecrosssiterequestforgery_risklevel9+count_vulnibm_sh_namecrosssiterequestforgery_risklevel9)*100)/(count_vulnibm_iot_namecrosssiterequestforgery+count_vulnibm_sh_namecrosssiterequestforgery))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namecrosssiterequestforgery_risklevel8+count_vulnibm_sh_namecrosssiterequestforgery_risklevel8)*100)/(count_vulnibm_iot_namecrosssiterequestforgery+count_vulnibm_sh_namecrosssiterequestforgery))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namecrosssiterequestforgery_risklevel7+count_vulnibm_sh_namecrosssiterequestforgery_risklevel7)*100)/(count_vulnibm_iot_namecrosssiterequestforgery+count_vulnibm_sh_namecrosssiterequestforgery))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namecrosssiterequestforgery_risklevel6+count_vulnibm_sh_namecrosssiterequestforgery_risklevel6)*100)/(count_vulnibm_iot_namecrosssiterequestforgery+count_vulnibm_sh_namecrosssiterequestforgery))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namecrosssiterequestforgery_risklevel5+count_vulnibm_sh_namecrosssiterequestforgery_risklevel5)*100)/(count_vulnibm_iot_namecrosssiterequestforgery+count_vulnibm_sh_namecrosssiterequestforgery))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namecrosssiterequestforgery_risklevel4+count_vulnibm_sh_namecrosssiterequestforgery_risklevel4)*100)/(count_vulnibm_iot_namecrosssiterequestforgery+count_vulnibm_sh_namecrosssiterequestforgery))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namecrosssiterequestforgery_risklevel3+count_vulnibm_sh_namecrosssiterequestforgery_risklevel3)*100)/(count_vulnibm_iot_namecrosssiterequestforgery+count_vulnibm_sh_namecrosssiterequestforgery))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namecrosssiterequestforgery_risklevel2+count_vulnibm_sh_namecrosssiterequestforgery_risklevel2)*100)/(count_vulnibm_iot_namecrosssiterequestforgery+count_vulnibm_sh_namecrosssiterequestforgery))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namecrosssiterequestforgery_risklevel1+count_vulnibm_sh_namecrosssiterequestforgery_risklevel1)*100)/(count_vulnibm_iot_namecrosssiterequestforgery+count_vulnibm_sh_namecrosssiterequestforgery))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namecrosssiterequestforgery_risklevel0+count_vulnibm_sh_namecrosssiterequestforgery_risklevel0)*100)/(count_vulnibm_iot_namecrosssiterequestforgery+count_vulnibm_sh_namecrosssiterequestforgery))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("            -    EL VALOR MEDIO DE PUNTUACION BASE ES  "+str(float(((count_vulnibm_iot_namecrosssiterequestforgery_risklevel+count_vulnibm_sh_namecrosssiterequestforgery_risklevel)/(count_vulnibm_iot_namecrosssiterequestforgery+count_vulnibm_sh_namecrosssiterequestforgery))))+"\n")
print("\n")
print("      -    EN EL "+str(float((((count_vulnibm_iot_namemoduleexecution+count_vulnibm_sh_namemoduleexecution)*100)/(count_vulnibm_iot_names+count_vulnibm_sh_names))))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE MODULE EXECUTION, LOS PORCENTAJES DE PUNTUACION BASE SON LOS SIGUIENTES :  \n")
print("            -    EN EL"+str(float((((count_vulnibm_iot_namemoduleexecution_risklevel10+count_vulnibm_sh_namemoduleexecution_risklevel10)*100)/(count_vulnibm_iot_namemoduleexecution+count_vulnibm_sh_namemoduleexecution))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namemoduleexecution_risklevel9+count_vulnibm_sh_namemoduleexecution_risklevel9)*100)/(count_vulnibm_iot_namemoduleexecution+count_vulnibm_sh_namemoduleexecution))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namemoduleexecution_risklevel8+count_vulnibm_sh_namemoduleexecution_risklevel8)*100)/(count_vulnibm_iot_namemoduleexecution+count_vulnibm_sh_namemoduleexecution))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namemoduleexecution_risklevel7+count_vulnibm_sh_namemoduleexecution_risklevel7)*100)/(count_vulnibm_iot_namemoduleexecution+count_vulnibm_sh_namemoduleexecution))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namemoduleexecution_risklevel6+count_vulnibm_sh_namemoduleexecution_risklevel6)*100)/(count_vulnibm_iot_namemoduleexecution+count_vulnibm_sh_namemoduleexecution))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namemoduleexecution_risklevel5+count_vulnibm_sh_namemoduleexecution_risklevel5)*100)/(count_vulnibm_iot_namemoduleexecution+count_vulnibm_sh_namemoduleexecution))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namemoduleexecution_risklevel4+count_vulnibm_sh_namemoduleexecution_risklevel4)*100)/(count_vulnibm_iot_namemoduleexecution+count_vulnibm_sh_namemoduleexecution))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namemoduleexecution_risklevel3+count_vulnibm_sh_namemoduleexecution_risklevel3)*100)/(count_vulnibm_iot_namemoduleexecution+count_vulnibm_sh_namemoduleexecution))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namemoduleexecution_risklevel2+count_vulnibm_sh_namemoduleexecution_risklevel2)*100)/(count_vulnibm_iot_namemoduleexecution+count_vulnibm_sh_namemoduleexecution))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namemoduleexecution_risklevel1+count_vulnibm_sh_namemoduleexecution_risklevel1)*100)/(count_vulnibm_iot_namemoduleexecution+count_vulnibm_sh_namemoduleexecution))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namemoduleexecution_risklevel0+count_vulnibm_sh_namemoduleexecution_risklevel0)*100)/(count_vulnibm_iot_namemoduleexecution+count_vulnibm_sh_namemoduleexecution))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("            -    EL VALOR MEDIO DE PUNTUACION BASE ES  "+str(float(((count_vulnibm_iot_namemoduleexecution_risklevel+count_vulnibm_sh_namemoduleexecution_risklevel)/(count_vulnibm_iot_namemoduleexecution+count_vulnibm_sh_namemoduleexecution))))+"\n")
print("\n")
print("      -    EN EL "+str(float((((count_vulnibm_iot_namebufferoverflow+count_vulnibm_sh_namebufferoverflow)*100)/(count_vulnibm_iot_names+count_vulnibm_sh_names))))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE BUFFER OVERFLOW, LOS PORCENTAJES DE PUNTUACION BASE SON LOS SIGUIENTES :  \n")
print("            -    EN EL"+str(float((((count_vulnibm_iot_namebufferoverflow_risklevel10+count_vulnibm_sh_namebufferoverflow_risklevel10)*100)/(count_vulnibm_iot_namebufferoverflow+count_vulnibm_sh_namebufferoverflow))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namebufferoverflow_risklevel9+count_vulnibm_sh_namebufferoverflow_risklevel9)*100)/(count_vulnibm_iot_namebufferoverflow+count_vulnibm_sh_namebufferoverflow))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namebufferoverflow_risklevel8+count_vulnibm_sh_namebufferoverflow_risklevel8)*100)/(count_vulnibm_iot_namebufferoverflow+count_vulnibm_sh_namebufferoverflow))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namebufferoverflow_risklevel7+count_vulnibm_sh_namebufferoverflow_risklevel7)*100)/(count_vulnibm_iot_namebufferoverflow+count_vulnibm_sh_namebufferoverflow))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namebufferoverflow_risklevel6+count_vulnibm_sh_namebufferoverflow_risklevel6)*100)/(count_vulnibm_iot_namebufferoverflow+count_vulnibm_sh_namebufferoverflow))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namebufferoverflow_risklevel5+count_vulnibm_sh_namebufferoverflow_risklevel5)*100)/(count_vulnibm_iot_namebufferoverflow+count_vulnibm_sh_namebufferoverflow))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namebufferoverflow_risklevel4+count_vulnibm_sh_namebufferoverflow_risklevel4)*100)/(count_vulnibm_iot_namebufferoverflow+count_vulnibm_sh_namebufferoverflow))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namebufferoverflow_risklevel3+count_vulnibm_sh_namebufferoverflow_risklevel3)*100)/(count_vulnibm_iot_namebufferoverflow+count_vulnibm_sh_namebufferoverflow))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namebufferoverflow_risklevel2+count_vulnibm_sh_namebufferoverflow_risklevel2)*100)/(count_vulnibm_iot_namebufferoverflow+count_vulnibm_sh_namebufferoverflow))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namebufferoverflow_risklevel1+count_vulnibm_sh_namebufferoverflow_risklevel1)*100)/(count_vulnibm_iot_namebufferoverflow+count_vulnibm_sh_namebufferoverflow))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namebufferoverflow_risklevel0+count_vulnibm_sh_namebufferoverflow_risklevel0)*100)/(count_vulnibm_iot_namebufferoverflow+count_vulnibm_sh_namebufferoverflow))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("            -    EL VALOR MEDIO DE PUNTUACION BASE ES  "+str(float(((count_vulnibm_iot_namebufferoverflow_risklevel+count_vulnibm_sh_namebufferoverflow_risklevel)/(count_vulnibm_iot_namebufferoverflow+count_vulnibm_sh_namebufferoverflow))))+"\n")
print("\n")
print("      -    EN EL "+str(float((((count_vulnibm_iot_namecommandexecution+count_vulnibm_sh_namecommandexecution)*100)/(count_vulnibm_iot_names+count_vulnibm_sh_names))))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE COMMAND EXECUTION, LOS PORCENTAJES DE PUNTUACION BASE SON LOS SIGUIENTES :  \n")
print("            -    EN EL"+str(float((((count_vulnibm_iot_namecommandexecution_risklevel10+count_vulnibm_sh_namecommandexecution_risklevel10)*100)/(count_vulnibm_iot_namecommandexecution+count_vulnibm_sh_namecommandexecution))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namecommandexecution_risklevel9+count_vulnibm_sh_namecommandexecution_risklevel9)*100)/(count_vulnibm_iot_namecommandexecution+count_vulnibm_sh_namecommandexecution))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namecommandexecution_risklevel8+count_vulnibm_sh_namecommandexecution_risklevel8)*100)/(count_vulnibm_iot_namecommandexecution+count_vulnibm_sh_namecommandexecution))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namecommandexecution_risklevel7+count_vulnibm_sh_namecommandexecution_risklevel7)*100)/(count_vulnibm_iot_namecommandexecution+count_vulnibm_sh_namecommandexecution))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namecommandexecution_risklevel6+count_vulnibm_sh_namecommandexecution_risklevel6)*100)/(count_vulnibm_iot_namecommandexecution+count_vulnibm_sh_namecommandexecution))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namecommandexecution_risklevel5+count_vulnibm_sh_namecommandexecution_risklevel5)*100)/(count_vulnibm_iot_namecommandexecution+count_vulnibm_sh_namecommandexecution))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namecommandexecution_risklevel4+count_vulnibm_sh_namecommandexecution_risklevel4)*100)/(count_vulnibm_iot_namecommandexecution+count_vulnibm_sh_namecommandexecution))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namecommandexecution_risklevel3+count_vulnibm_sh_namecommandexecution_risklevel3)*100)/(count_vulnibm_iot_namecommandexecution+count_vulnibm_sh_namecommandexecution))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namecommandexecution_risklevel2+count_vulnibm_sh_namecommandexecution_risklevel2)*100)/(count_vulnibm_iot_namecommandexecution+count_vulnibm_sh_namecommandexecution))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namecommandexecution_risklevel1+count_vulnibm_sh_namecommandexecution_risklevel1)*100)/(count_vulnibm_iot_namecommandexecution+count_vulnibm_sh_namecommandexecution))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namecommandexecution_risklevel0+count_vulnibm_sh_namecommandexecution_risklevel0)*100)/(count_vulnibm_iot_namecommandexecution+count_vulnibm_sh_namecommandexecution))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("            -    EL VALOR MEDIO DE PUNTUACION BASE ES  "+str(float(((count_vulnibm_iot_namecommandexecution_risklevel+count_vulnibm_sh_namecommandexecution_risklevel)/(count_vulnibm_iot_namecommandexecution+count_vulnibm_sh_namecommandexecution))))+"\n")
print("\n")
print("      -    EN EL "+str(float((((count_vulnibm_iot_namespoofing+count_vulnibm_sh_namespoofing)*100)/(count_vulnibm_iot_names+count_vulnibm_sh_names))))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE SPOOFING, LOS PORCENTAJES DE PUNTUACION BASE SON LOS SIGUIENTES :  \n")
print("            -    EN EL"+str(float((((count_vulnibm_iot_namespoofing_risklevel10+count_vulnibm_sh_namespoofing_risklevel10)*100)/(count_vulnibm_iot_namespoofing+count_vulnibm_sh_namespoofing))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namespoofing_risklevel9+count_vulnibm_sh_namespoofing_risklevel9)*100)/(count_vulnibm_iot_namespoofing+count_vulnibm_sh_namespoofing))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namespoofing_risklevel8+count_vulnibm_sh_namespoofing_risklevel8)*100)/(count_vulnibm_iot_namespoofing+count_vulnibm_sh_namespoofing))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namespoofing_risklevel7+count_vulnibm_sh_namespoofing_risklevel7)*100)/(count_vulnibm_iot_namespoofing+count_vulnibm_sh_namespoofing))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namespoofing_risklevel6+count_vulnibm_sh_namespoofing_risklevel6)*100)/(count_vulnibm_iot_namespoofing+count_vulnibm_sh_namespoofing))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namespoofing_risklevel5+count_vulnibm_sh_namespoofing_risklevel5)*100)/(count_vulnibm_iot_namespoofing+count_vulnibm_sh_namespoofing))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namespoofing_risklevel4+count_vulnibm_sh_namespoofing_risklevel4)*100)/(count_vulnibm_iot_namespoofing+count_vulnibm_sh_namespoofing))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namespoofing_risklevel3+count_vulnibm_sh_namespoofing_risklevel3)*100)/(count_vulnibm_iot_namespoofing+count_vulnibm_sh_namespoofing))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namespoofing_risklevel2+count_vulnibm_sh_namespoofing_risklevel2)*100)/(count_vulnibm_iot_namespoofing+count_vulnibm_sh_namespoofing))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namespoofing_risklevel1+count_vulnibm_sh_namespoofing_risklevel1)*100)/(count_vulnibm_iot_namespoofing+count_vulnibm_sh_namespoofing))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namespoofing_risklevel0+count_vulnibm_sh_namespoofing_risklevel0)*100)/(count_vulnibm_iot_namespoofing+count_vulnibm_sh_namespoofing))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("            -    EL VALOR MEDIO DE PUNTUACION BASE ES  "+str(float(((count_vulnibm_iot_namespoofing_risklevel+count_vulnibm_sh_namespoofing_risklevel)/(count_vulnibm_iot_namespoofing+count_vulnibm_sh_namespoofing))))+"\n")
print("\n")
print("      -    EN EL "+str(float((((count_vulnibm_iot_nameclickjacking+count_vulnibm_sh_nameclickjacking)*100)/(count_vulnibm_iot_names+count_vulnibm_sh_names))))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE CLICKJACKING, LOS PORCENTAJES DE PUNTUACION BASE SON LOS SIGUIENTES :  \n")
print("            -    EN EL"+str(float((((count_vulnibm_iot_nameclickjacking_risklevel10+count_vulnibm_sh_nameclickjacking_risklevel10)*100)/(count_vulnibm_iot_nameclickjacking+count_vulnibm_sh_nameclickjacking))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_nameclickjacking_risklevel9+count_vulnibm_sh_nameclickjacking_risklevel9)*100)/(count_vulnibm_iot_nameclickjacking+count_vulnibm_sh_nameclickjacking))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_nameclickjacking_risklevel8+count_vulnibm_sh_nameclickjacking_risklevel8)*100)/(count_vulnibm_iot_nameclickjacking+count_vulnibm_sh_nameclickjacking))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_nameclickjacking_risklevel7+count_vulnibm_sh_nameclickjacking_risklevel7)*100)/(count_vulnibm_iot_nameclickjacking+count_vulnibm_sh_nameclickjacking))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_nameclickjacking_risklevel6+count_vulnibm_sh_nameclickjacking_risklevel6)*100)/(count_vulnibm_iot_nameclickjacking+count_vulnibm_sh_nameclickjacking))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_nameclickjacking_risklevel5+count_vulnibm_sh_nameclickjacking_risklevel5)*100)/(count_vulnibm_iot_nameclickjacking+count_vulnibm_sh_nameclickjacking))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_nameclickjacking_risklevel4+count_vulnibm_sh_nameclickjacking_risklevel4)*100)/(count_vulnibm_iot_nameclickjacking+count_vulnibm_sh_nameclickjacking))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_nameclickjacking_risklevel3+count_vulnibm_sh_nameclickjacking_risklevel3)*100)/(count_vulnibm_iot_nameclickjacking+count_vulnibm_sh_nameclickjacking))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_nameclickjacking_risklevel2+count_vulnibm_sh_nameclickjacking_risklevel2)*100)/(count_vulnibm_iot_nameclickjacking+count_vulnibm_sh_nameclickjacking))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_nameclickjacking_risklevel1+count_vulnibm_sh_nameclickjacking_risklevel1)*100)/(count_vulnibm_iot_nameclickjacking+count_vulnibm_sh_nameclickjacking))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_nameclickjacking_risklevel0+count_vulnibm_sh_nameclickjacking_risklevel0)*100)/(count_vulnibm_iot_nameclickjacking+count_vulnibm_sh_nameclickjacking))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("            -    EL VALOR MEDIO DE PUNTUACION BASE ES  "+str(float(((count_vulnibm_iot_nameclickjacking_risklevel+count_vulnibm_sh_nameclickjacking_risklevel)/(count_vulnibm_iot_nameclickjacking+count_vulnibm_sh_nameclickjacking))))+"\n")
print("\n")
print("      -    EN EL "+str(float((((count_vulnibm_iot_namehijacking+count_vulnibm_sh_namehijacking)*100)/(count_vulnibm_iot_names+count_vulnibm_sh_names))))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE HIJACKING, LOS PORCENTAJES DE PUNTUACION BASE SON LOS SIGUIENTES :  \n")
print("            -    EN EL"+str(float((((count_vulnibm_iot_namehijacking_risklevel10+count_vulnibm_sh_namehijacking_risklevel10)*100)/(count_vulnibm_iot_namehijacking+count_vulnibm_sh_namehijacking))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namehijacking_risklevel9+count_vulnibm_sh_namehijacking_risklevel9)*100)/(count_vulnibm_iot_namehijacking+count_vulnibm_sh_namehijacking))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namehijacking_risklevel8+count_vulnibm_sh_namehijacking_risklevel8)*100)/(count_vulnibm_iot_namehijacking+count_vulnibm_sh_namehijacking))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namehijacking_risklevel7+count_vulnibm_sh_namehijacking_risklevel7)*100)/(count_vulnibm_iot_namehijacking+count_vulnibm_sh_namehijacking))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namehijacking_risklevel6+count_vulnibm_sh_namehijacking_risklevel6)*100)/(count_vulnibm_iot_namehijacking+count_vulnibm_sh_namehijacking))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namehijacking_risklevel5+count_vulnibm_sh_namehijacking_risklevel5)*100)/(count_vulnibm_iot_namehijacking+count_vulnibm_sh_namehijacking))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namehijacking_risklevel4+count_vulnibm_sh_namehijacking_risklevel4)*100)/(count_vulnibm_iot_namehijacking+count_vulnibm_sh_namehijacking))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namehijacking_risklevel3+count_vulnibm_sh_namehijacking_risklevel3)*100)/(count_vulnibm_iot_namehijacking+count_vulnibm_sh_namehijacking))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namehijacking_risklevel2+count_vulnibm_sh_namehijacking_risklevel2)*100)/(count_vulnibm_iot_namehijacking+count_vulnibm_sh_namehijacking))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namehijacking_risklevel1+count_vulnibm_sh_namehijacking_risklevel1)*100)/(count_vulnibm_iot_namehijacking+count_vulnibm_sh_namehijacking))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namehijacking_risklevel0+count_vulnibm_sh_namehijacking_risklevel0)*100)/(count_vulnibm_iot_namehijacking+count_vulnibm_sh_namehijacking))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("            -    EL VALOR MEDIO DE PUNTUACION BASE ES  "+str(float(((count_vulnibm_iot_namehijacking_risklevel+count_vulnibm_sh_namehijacking_risklevel)/(count_vulnibm_iot_namehijacking+count_vulnibm_sh_namehijacking))))+"\n")
print("\n")
print("      -    EN EL "+str(float((((count_vulnibm_iot_namefileinclude+count_vulnibm_sh_namefileinclude)*100)/(count_vulnibm_iot_names+count_vulnibm_sh_names))))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE FILE INCLUDE, LOS PORCENTAJES DE PUNTUACION BASE SON LOS SIGUIENTES :  \n")
print("            -    EN EL"+str(float((((count_vulnibm_iot_namefileinclude_risklevel10+count_vulnibm_sh_namefileinclude_risklevel10)*100)/(count_vulnibm_iot_namefileinclude+count_vulnibm_sh_namefileinclude))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namefileinclude_risklevel9+count_vulnibm_sh_namefileinclude_risklevel9)*100)/(count_vulnibm_iot_namefileinclude+count_vulnibm_sh_namefileinclude))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namefileinclude_risklevel8+count_vulnibm_sh_namefileinclude_risklevel8)*100)/(count_vulnibm_iot_namefileinclude+count_vulnibm_sh_namefileinclude))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namefileinclude_risklevel7+count_vulnibm_sh_namefileinclude_risklevel7)*100)/(count_vulnibm_iot_namefileinclude+count_vulnibm_sh_namefileinclude))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namefileinclude_risklevel6+count_vulnibm_sh_namefileinclude_risklevel6)*100)/(count_vulnibm_iot_namefileinclude+count_vulnibm_sh_namefileinclude))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namefileinclude_risklevel5+count_vulnibm_sh_namefileinclude_risklevel5)*100)/(count_vulnibm_iot_namefileinclude+count_vulnibm_sh_namefileinclude))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namefileinclude_risklevel4+count_vulnibm_sh_namefileinclude_risklevel4)*100)/(count_vulnibm_iot_namefileinclude+count_vulnibm_sh_namefileinclude))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namefileinclude_risklevel3+count_vulnibm_sh_namefileinclude_risklevel3)*100)/(count_vulnibm_iot_namefileinclude+count_vulnibm_sh_namefileinclude))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namefileinclude_risklevel2+count_vulnibm_sh_namefileinclude_risklevel2)*100)/(count_vulnibm_iot_namefileinclude+count_vulnibm_sh_namefileinclude))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namefileinclude_risklevel1+count_vulnibm_sh_namefileinclude_risklevel1)*100)/(count_vulnibm_iot_namefileinclude+count_vulnibm_sh_namefileinclude))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namefileinclude_risklevel0+count_vulnibm_sh_namefileinclude_risklevel0)*100)/(count_vulnibm_iot_namefileinclude+count_vulnibm_sh_namefileinclude))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("            -    EL VALOR MEDIO DE PUNTUACION BASE ES  "+str(float(((count_vulnibm_iot_namefileinclude_risklevel+count_vulnibm_sh_namefileinclude_risklevel)/(count_vulnibm_iot_namefileinclude+count_vulnibm_sh_namefileinclude))))+"\n")
print("\n")
print("      -    EN EL "+str(float((((count_vulnibm_iot_namebruteforce+count_vulnibm_sh_namebruteforce)*100)/(count_vulnibm_iot_names+count_vulnibm_sh_names))))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE BRUTE FORCE, LOS PORCENTAJES DE PUNTUACION BASE SON LOS SIGUIENTES :  \n")
print("            -    EN EL"+str(float((((count_vulnibm_iot_namebruteforce_risklevel10+count_vulnibm_sh_namebruteforce_risklevel10)*100)/(count_vulnibm_iot_namebruteforce+count_vulnibm_sh_namebruteforce))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namebruteforce_risklevel9+count_vulnibm_sh_namebruteforce_risklevel9)*100)/(count_vulnibm_iot_namebruteforce+count_vulnibm_sh_namebruteforce))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namebruteforce_risklevel8+count_vulnibm_sh_namebruteforce_risklevel8)*100)/(count_vulnibm_iot_namebruteforce+count_vulnibm_sh_namebruteforce))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namebruteforce_risklevel7+count_vulnibm_sh_namebruteforce_risklevel7)*100)/(count_vulnibm_iot_namebruteforce+count_vulnibm_sh_namebruteforce))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namebruteforce_risklevel6+count_vulnibm_sh_namebruteforce_risklevel6)*100)/(count_vulnibm_iot_namebruteforce+count_vulnibm_sh_namebruteforce))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namebruteforce_risklevel5+count_vulnibm_sh_namebruteforce_risklevel5)*100)/(count_vulnibm_iot_namebruteforce+count_vulnibm_sh_namebruteforce))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namebruteforce_risklevel4+count_vulnibm_sh_namebruteforce_risklevel4)*100)/(count_vulnibm_iot_namebruteforce+count_vulnibm_sh_namebruteforce))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namebruteforce_risklevel3+count_vulnibm_sh_namebruteforce_risklevel3)*100)/(count_vulnibm_iot_namebruteforce+count_vulnibm_sh_namebruteforce))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namebruteforce_risklevel2+count_vulnibm_sh_namebruteforce_risklevel2)*100)/(count_vulnibm_iot_namebruteforce+count_vulnibm_sh_namebruteforce))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namebruteforce_risklevel1+count_vulnibm_sh_namebruteforce_risklevel1)*100)/(count_vulnibm_iot_namebruteforce+count_vulnibm_sh_namebruteforce))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namebruteforce_risklevel0+count_vulnibm_sh_namebruteforce_risklevel0)*100)/(count_vulnibm_iot_namebruteforce+count_vulnibm_sh_namebruteforce))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("            -    EL VALOR MEDIO DE PUNTUACION BASE ES  "+str(float(((count_vulnibm_iot_namebruteforce_risklevel+count_vulnibm_sh_namebruteforce_risklevel)/(count_vulnibm_iot_namebruteforce+count_vulnibm_sh_namebruteforce))))+"\n")
print("\n")
print("      -    EN EL "+str(float((((count_vulnibm_iot_namefileupload+count_vulnibm_sh_namefileupload)*100)/(count_vulnibm_iot_names+count_vulnibm_sh_names))))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE FILE UPLOAD, LOS PORCENTAJES DE PUNTUACION BASE SON LOS SIGUIENTES :  \n")
print("            -    EN EL"+str(float((((count_vulnibm_iot_namefileupload_risklevel10+count_vulnibm_sh_namefileupload_risklevel10)*100)/(count_vulnibm_iot_namefileupload+count_vulnibm_sh_namefileupload))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namefileupload_risklevel9+count_vulnibm_sh_namefileupload_risklevel9)*100)/(count_vulnibm_iot_namefileupload+count_vulnibm_sh_namefileupload))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namefileupload_risklevel8+count_vulnibm_sh_namefileupload_risklevel8)*100)/(count_vulnibm_iot_namefileupload+count_vulnibm_sh_namefileupload))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namefileupload_risklevel7+count_vulnibm_sh_namefileupload_risklevel7)*100)/(count_vulnibm_iot_namefileupload+count_vulnibm_sh_namefileupload))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namefileupload_risklevel6+count_vulnibm_sh_namefileupload_risklevel6)*100)/(count_vulnibm_iot_namefileupload+count_vulnibm_sh_namefileupload))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namefileupload_risklevel5+count_vulnibm_sh_namefileupload_risklevel5)*100)/(count_vulnibm_iot_namefileupload+count_vulnibm_sh_namefileupload))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namefileupload_risklevel4+count_vulnibm_sh_namefileupload_risklevel4)*100)/(count_vulnibm_iot_namefileupload+count_vulnibm_sh_namefileupload))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namefileupload_risklevel3+count_vulnibm_sh_namefileupload_risklevel3)*100)/(count_vulnibm_iot_namefileupload+count_vulnibm_sh_namefileupload))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namefileupload_risklevel2+count_vulnibm_sh_namefileupload_risklevel2)*100)/(count_vulnibm_iot_namefileupload+count_vulnibm_sh_namefileupload))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namefileupload_risklevel1+count_vulnibm_sh_namefileupload_risklevel1)*100)/(count_vulnibm_iot_namefileupload+count_vulnibm_sh_namefileupload))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_namefileupload_risklevel0+count_vulnibm_sh_namefileupload_risklevel0)*100)/(count_vulnibm_iot_namefileupload+count_vulnibm_sh_namefileupload))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("            -    EL VALOR MEDIO DE PUNTUACION BASE ES  "+str(float(((count_vulnibm_iot_namefileupload_risklevel+count_vulnibm_sh_namefileupload_risklevel)/(count_vulnibm_iot_namefileupload+count_vulnibm_sh_namefileupload))))+"\n")
print("\n")
print("      -    EN EL "+str(float((((count_vulnibm_iot_nameheaderinjection+count_vulnibm_sh_nameheaderinjection)*100)/(count_vulnibm_iot_names+count_vulnibm_sh_names))))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE HEADER INJECTION, LOS PORCENTAJES DE PUNTUACION BASE SON LOS SIGUIENTES :  \n")
print("            -    EN EL"+str(float((((count_vulnibm_iot_nameheaderinjection_risklevel10+count_vulnibm_sh_nameheaderinjection_risklevel10)*100)/(count_vulnibm_iot_nameheaderinjection+count_vulnibm_sh_nameheaderinjection))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_nameheaderinjection_risklevel9+count_vulnibm_sh_nameheaderinjection_risklevel9)*100)/(count_vulnibm_iot_nameheaderinjection+count_vulnibm_sh_nameheaderinjection))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_nameheaderinjection_risklevel8+count_vulnibm_sh_nameheaderinjection_risklevel8)*100)/(count_vulnibm_iot_nameheaderinjection+count_vulnibm_sh_nameheaderinjection))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_nameheaderinjection_risklevel7+count_vulnibm_sh_nameheaderinjection_risklevel7)*100)/(count_vulnibm_iot_nameheaderinjection+count_vulnibm_sh_nameheaderinjection))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_nameheaderinjection_risklevel6+count_vulnibm_sh_nameheaderinjection_risklevel6)*100)/(count_vulnibm_iot_nameheaderinjection+count_vulnibm_sh_nameheaderinjection))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_nameheaderinjection_risklevel5+count_vulnibm_sh_nameheaderinjection_risklevel5)*100)/(count_vulnibm_iot_nameheaderinjection+count_vulnibm_sh_nameheaderinjection))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_nameheaderinjection_risklevel4+count_vulnibm_sh_nameheaderinjection_risklevel4)*100)/(count_vulnibm_iot_nameheaderinjection+count_vulnibm_sh_nameheaderinjection))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_nameheaderinjection_risklevel3+count_vulnibm_sh_nameheaderinjection_risklevel3)*100)/(count_vulnibm_iot_nameheaderinjection+count_vulnibm_sh_nameheaderinjection))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_nameheaderinjection_risklevel2+count_vulnibm_sh_nameheaderinjection_risklevel2)*100)/(count_vulnibm_iot_nameheaderinjection+count_vulnibm_sh_nameheaderinjection))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_nameheaderinjection_risklevel1+count_vulnibm_sh_nameheaderinjection_risklevel1)*100)/(count_vulnibm_iot_nameheaderinjection+count_vulnibm_sh_nameheaderinjection))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_nameheaderinjection_risklevel0+count_vulnibm_sh_nameheaderinjection_risklevel0)*100)/(count_vulnibm_iot_nameheaderinjection+count_vulnibm_sh_nameheaderinjection))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("            -    EL VALOR MEDIO DE PUNTUACION BASE ES  "+str(float(((count_vulnibm_iot_nameheaderinjection_risklevel+count_vulnibm_sh_nameheaderinjection_risklevel)/(count_vulnibm_iot_nameheaderinjection+count_vulnibm_sh_nameheaderinjection))))+"\n")
print("\n")
print("      -    EN EL "+str(float((((count_vulnibm_iot_nametampering+count_vulnibm_sh_nametampering)*100)/(count_vulnibm_iot_names+count_vulnibm_sh_names))))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE TAMPERING, LOS PORCENTAJES DE PUNTUACION BASE SON LOS SIGUIENTES :  \n")
print("            -    EN EL"+str(float((((count_vulnibm_iot_nametampering_risklevel10+count_vulnibm_sh_nametampering_risklevel10)*100)/(count_vulnibm_iot_nametampering+count_vulnibm_sh_nametampering))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_nametampering_risklevel9+count_vulnibm_sh_nametampering_risklevel9)*100)/(count_vulnibm_iot_nametampering+count_vulnibm_sh_nametampering))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_nametampering_risklevel8+count_vulnibm_sh_nametampering_risklevel8)*100)/(count_vulnibm_iot_nametampering+count_vulnibm_sh_nametampering))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_nametampering_risklevel7+count_vulnibm_sh_nametampering_risklevel7)*100)/(count_vulnibm_iot_nametampering+count_vulnibm_sh_nametampering))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_nametampering_risklevel6+count_vulnibm_sh_nametampering_risklevel6)*100)/(count_vulnibm_iot_nametampering+count_vulnibm_sh_nametampering))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_nametampering_risklevel5+count_vulnibm_sh_nametampering_risklevel5)*100)/(count_vulnibm_iot_nametampering+count_vulnibm_sh_nametampering))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_nametampering_risklevel4+count_vulnibm_sh_nametampering_risklevel4)*100)/(count_vulnibm_iot_nametampering+count_vulnibm_sh_nametampering))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_nametampering_risklevel3+count_vulnibm_sh_nametampering_risklevel3)*100)/(count_vulnibm_iot_nametampering+count_vulnibm_sh_nametampering))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_nametampering_risklevel2+count_vulnibm_sh_nametampering_risklevel2)*100)/(count_vulnibm_iot_nametampering+count_vulnibm_sh_nametampering))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_nametampering_risklevel1+count_vulnibm_sh_nametampering_risklevel1)*100)/(count_vulnibm_iot_nametampering+count_vulnibm_sh_nametampering))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_nametampering_risklevel0+count_vulnibm_sh_nametampering_risklevel0)*100)/(count_vulnibm_iot_nametampering+count_vulnibm_sh_nametampering))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("            -    EL VALOR MEDIO DE PUNTUACION BASE ES  "+str(float(((count_vulnibm_iot_nametampering_risklevel+count_vulnibm_sh_nametampering_risklevel)/(count_vulnibm_iot_nametampering+count_vulnibm_sh_nametampering))))+"\n")
print("\n")
print("      -    EN EL "+str(float((((count_vulnibm_iot_nameanother+count_vulnibm_sh_nameanother)*100)/(count_vulnibm_iot_names+count_vulnibm_sh_names))))+" % DE VULNERABILIDADES EL NOMBRE INCLUYE UN VALOR DISTINTO, LOS PORCENTAJES DE PUNTUACION BASE SON LOS SIGUIENTES :  \n")
print("            -    EN EL"+str(float((((count_vulnibm_iot_nameanother_risklevel10+count_vulnibm_sh_nameanother_risklevel10)*100)/(count_vulnibm_iot_nameanother+count_vulnibm_sh_nameanother))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_nameanother_risklevel9+count_vulnibm_sh_nameanother_risklevel9)*100)/(count_vulnibm_iot_nameanother+count_vulnibm_sh_nameanother))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_nameanother_risklevel8+count_vulnibm_sh_nameanother_risklevel8)*100)/(count_vulnibm_iot_nameanother+count_vulnibm_sh_nameanother))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_nameanother_risklevel7+count_vulnibm_sh_nameanother_risklevel7)*100)/(count_vulnibm_iot_nameanother+count_vulnibm_sh_nameanother))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_nameanother_risklevel6+count_vulnibm_sh_nameanother_risklevel6)*100)/(count_vulnibm_iot_nameanother+count_vulnibm_sh_nameanother))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_nameanother_risklevel5+count_vulnibm_sh_nameanother_risklevel5)*100)/(count_vulnibm_iot_nameanother+count_vulnibm_sh_nameanother))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_nameanother_risklevel4+count_vulnibm_sh_nameanother_risklevel4)*100)/(count_vulnibm_iot_nameanother+count_vulnibm_sh_nameanother))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_nameanother_risklevel3+count_vulnibm_sh_nameanother_risklevel3)*100)/(count_vulnibm_iot_nameanother+count_vulnibm_sh_nameanother))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_nameanother_risklevel2+count_vulnibm_sh_nameanother_risklevel2)*100)/(count_vulnibm_iot_nameanother+count_vulnibm_sh_nameanother))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_nameanother_risklevel1+count_vulnibm_sh_nameanother_risklevel1)*100)/(count_vulnibm_iot_nameanother+count_vulnibm_sh_nameanother))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_nameanother_risklevel0+count_vulnibm_sh_nameanother_risklevel0)*100)/(count_vulnibm_iot_nameanother+count_vulnibm_sh_nameanother))))+" % DE VULNERABILIDADES LA PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("            -    EL VALOR MEDIO DE PUNTUACION BASE ES  "+str(float(((count_vulnibm_iot_nameanother_risklevel+count_vulnibm_sh_nameanother_risklevel)/(count_vulnibm_iot_nameanother+count_vulnibm_sh_nameanother))))+"\n")
print("\n")
               	













