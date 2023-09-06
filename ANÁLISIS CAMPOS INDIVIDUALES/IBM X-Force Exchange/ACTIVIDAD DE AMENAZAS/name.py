


import pandas as pd
from datetime import datetime,timedelta



#Abro los ficheros con los que voy a tratar




df_vulnibm_iot = pd.read_excel('ibm_threat_activity_report_iot_2023_v2.xlsx')

#Variable que almacenara el contador total de valores de nombre
count_vulnibm_iot_names=0
#Variables que almacenan el contador de valores especificos de nombre
count_vulnibm_iot_namephishing=0
count_vulnibm_iot_namebotnet=0
count_vulnibm_iot_namereconnaissance=0
count_vulnibm_iot_namebackdoor=0
count_vulnibm_iot_namestealer=0
count_vulnibm_iot_namexploit=0
count_vulnibm_iot_namedenialofservice=0
count_vulnibm_iot_namebruteforce=0
count_vulnibm_iot_nameransomware=0
count_vulnibm_iot_nametrojan=0
count_vulnibm_iot_namesandbox=0
count_vulnibm_iot_nameworm=0
count_vulnibm_iot_namespam=0
count_vulnibm_iot_namemalware=0
count_vulnibm_iot_namehijacking=0
count_vulnibm_iot_namesocialengineering=0
count_vulnibm_iot_namespearphishing=0
count_vulnibm_iot_namedropper=0
count_vulnibm_iot_namespyware=0
count_vulnibm_iot_nameloader=0
count_vulnibm_iot_namedownloader=0
count_vulnibm_iot_namedistribution=0
count_vulnibm_iot_namexss=0
count_vulnibm_iot_namefraud=0
count_vulnibm_iot_namebootkit=0
count_vulnibm_iot_namehosting=0
count_vulnibm_iot_namebot=0
count_vulnibm_iot_nameinjection=0
count_vulnibm_iot_nameinfection=0
count_vulnibm_iot_nameimpersonate=0
count_vulnibm_iot_namechain=0
count_vulnibm_iot_namespionage=0
count_vulnibm_iot_namexfiltration=0
count_vulnibm_iot_namemasquerade=0
count_vulnibm_iot_namecontrol=0
count_vulnibm_iot_namecryptojack=0
count_vulnibm_iot_nameremote=0
count_vulnibm_iot_nameanother=0


#Comprobamos el contenido de name
for r in range(0,len(df_vulnibm_iot["name"])):
    #Comprobamos si hay varios objetos en la fila actual
    if('[' in df_vulnibm_iot["name"][r]):
        aux=df_vulnibm_iot["name"][r].split(",")
        for l in range(0,len(aux)):
            if(len(aux)>0):
                #Obtengo el valor de nombre y aumento contadores segun el tipo que sea
                aux_str=aux[l].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
                if(aux_str!='NONE'):
                    count_vulnibm_iot_names+=1
                    if('phishing' in aux_str or 'Phishing' in aux_str):
                        count_vulnibm_iot_namephishing+=1
                    elif('Botnet' in aux_str or 'botnet' in aux_str or 'BotNet' in aux_str):
                        count_vulnibm_iot_namebotnet+=1
                    elif('reconnaissance' in aux_str or 'Reconnaissance' in aux_str):
                        count_vulnibm_iot_namereconnaissance+=1
                    elif('Backdoor' in aux_str or 'backdoor' in aux_str):
                        count_vulnibm_iot_namebackdoor=1                            
                    elif('stealer' in aux_str  or 'Stealer' in aux_str):
                        count_vulnibm_iot_namestealer+=1                           
                    elif('exploit' in aux_str or 'Exploit' in aux_str):
                        count_vulnibm_iot_namexploit+=1                           
                    elif('denialofservice' in aux_str or 'ddos' in aux_str or 'DDoS' in aux_str or 'Denial' in aux_str):
                        count_vulnibm_iot_namedenialofservice+=1                           
                    elif('brute' in aux_str or 'Brute' in aux_str ):
                        count_vulnibm_iot_namebruteforce+=1                           
                    elif('Ransomware' in aux_str or 'ransomware' in aux_str):
                        count_vulnibm_iot_nameransomware+=1                           
                    elif('Trojan' in aux_str or 'Trojans' in aux_str or 'trojan' in aux_str or 'trojans' in aux_str):
                        count_vulnibm_iot_nametrojan+=1                           
                    elif('Sandbox' in aux_str or 'sandbox' in aux_str):
                        count_vulnibm_iot_namesandbox+=1                           
                    elif('worm' in aux_str or 'Worm' in aux_str):
                        count_vulnibm_iot_nameworm+=1                           
                    elif('spam' in aux_str or 'Spam' in aux_str):
                        count_vulnibm_iot_namespam+=1                           
                    elif('Malware' in aux_str or 'malware' in aux_str):
                        count_vulnibm_iot_namemalware+=1  
                    elif('hijacking' in aux_str or 'Hijacking' in aux_str or 'Hijack' in aux_str or 'hijack' in aux_str):
                        count_vulnibm_iot_namehijacking+=1     
                    elif('Social' in aux_str or 'social' in aux_str):
                        count_vulnibm_iot_namesocialengineering+=1 
                    elif('loader' in aux_str or 'Loader' in aux_str):
                        count_vulnibm_iot_nameloader+=1 
                    elif('spearphishing' in aux_str or 'Spearphishing' in aux_str):
                        count_vulnibm_iot_namespearphishing+=1 
                    elif('dropper' in aux_str or 'Dropper' in aux_str):
                        count_vulnibm_iot_namesocialengineering+=1 
                    elif('spyware' in aux_str or 'Spyware' in aux_str):
                        count_vulnibm_iot_namespyware+=1 
                    elif('loader' in aux_str or 'Loader' in aux_str):
                        count_vulnibm_iot_nameloader+=1 
                    elif('downloader' in aux_str or 'Downloader' in aux_str):
                        count_vulnibm_iot_namedownloader+=1 
                    elif('distribu' in aux_str):
                        count_vulnibm_iot_namedistribution+=1
                    elif('cross' in aux_str or 'Cross' in aux_str or 'xss' in aux_str  or 'XSS' in aux_str ):
                        count_vulnibm_iot_namexss+=1
                    elif('fraud' in aux_str or 'Fraud' in aux_str):
                        count_vulnibm_iot_namefraud+=1 
                    elif('bootkit' in aux_str or 'Bootkit' in aux_str):
                        count_vulnibm_iot_namebootkit+=1 
                    elif('hosting' in aux_str or 'Hosting' in aux_str):
                        count_vulnibm_iot_namehosting+=1 
                    elif('bot' in aux_str or 'Bot' in aux_str):
                        count_vulnibm_iot_namebot+=1 
                    elif('injection' in aux_str or 'Injection' in aux_str):
                        count_vulnibm_iot_nameinjection+=1 
                    elif('infection' in aux_str or 'Infection' in aux_str):
                        count_vulnibm_iot_nameinfection+=1 
                    elif('chain' in aux_str or 'Chain' in aux_str):
                        count_vulnibm_iot_namechain+=1 
                    elif('imperson' in aux_str or 'Imperson' in aux_str):
                        count_vulnibm_iot_nameimpersonate+=1 
                    elif('espionage' in aux_str or 'Espionage' in aux_str):
                        count_vulnibm_iot_namespionage+=1 
                    elif('exfilt' in aux_str or 'Exfilt' in aux_str):
                        count_vulnibm_iot_namexfiltration+=1 
                    elif('masquerade' in aux_str or 'Masquerade' in aux_str):
                        count_vulnibm_iot_namemasquerade+=1 
                    elif('control' in aux_str or 'Control' in aux_str):
                        count_vulnibm_iot_namecontrol+=1 
                    elif('cryptojack' in aux_str or 'Cryptojack' in aux_str):
                        count_vulnibm_iot_namecryptojack+=1 
                    elif('remote' in aux_str or 'Remote' in aux_str):
                        count_vulnibm_iot_nameremote+=1 
                    else:
                        count_vulnibm_iot_nameanother+=1
    else:
        #Obtengo el valor de nombre y aumento contadores segun el tipo que sea
        aux_str=df_vulnibm_iot["name"][r].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
        if(aux_str!='NONE'):
            count_vulnibm_iot_names+=1
            if('phishing' in aux_str or 'Phishing' in aux_str):
                count_vulnibm_iot_namephishing+=1
            elif('Botnet' in aux_str or 'botnet' in aux_str or 'BotNet' in aux_str):
                count_vulnibm_iot_namebotnet+=1
            elif('reconnaissance' in aux_str or 'Reconnaissance' in aux_str):
                count_vulnibm_iot_namereconnaissance+=1
            elif('Backdoor' in aux_str or 'backdoor' in aux_str):
                count_vulnibm_iot_namebackdoor=1                            
            elif('stealer' in aux_str  or 'Stealer' in aux_str):
                count_vulnibm_iot_namestealer+=1                           
            elif('exploit' in aux_str or 'Exploit' in aux_str):
                count_vulnibm_iot_namexploit+=1                           
            elif('denialofservice' in aux_str or 'ddos' in aux_str or 'DDoS' in aux_str or 'Denial' in aux_str):
                count_vulnibm_iot_namedenialofservice+=1                           
            elif('brute' in aux_str or 'Brute' in aux_str ):
                count_vulnibm_iot_namebruteforce+=1                           
            elif('Ransomware' in aux_str or 'ransomware' in aux_str):
                count_vulnibm_iot_nameransomware+=1                           
            elif('Trojan' in aux_str or 'Trojans' in aux_str or 'trojan' in aux_str or 'trojans' in aux_str):
                count_vulnibm_iot_nametrojan+=1                           
            elif('Sandbox' in aux_str or 'sandbox' in aux_str):
                count_vulnibm_iot_namesandbox+=1                           
            elif('worm' in aux_str or 'Worm' in aux_str):
                count_vulnibm_iot_nameworm+=1                           
            elif('spam' in aux_str or 'Spam' in aux_str):
                count_vulnibm_iot_namespam+=1                           
            elif('Malware' in aux_str or 'malware' in aux_str):
                count_vulnibm_iot_namemalware+=1  
            elif('hijacking' in aux_str or 'Hijacking' in aux_str or 'Hijack' in aux_str or 'hijack' in aux_str):
                count_vulnibm_iot_namehijacking+=1     
            elif('Social' in aux_str or 'social' in aux_str):
                count_vulnibm_iot_namesocialengineering+=1 
            elif('loader' in aux_str or 'Loader' in aux_str):
                count_vulnibm_iot_nameloader+=1 
            elif('spearphishing' in aux_str or 'Spearphishing' in aux_str):
                count_vulnibm_iot_namespearphishing+=1 
            elif('dropper' in aux_str or 'Dropper' in aux_str):
                count_vulnibm_iot_namesocialengineering+=1 
            elif('spyware' in aux_str or 'Spyware' in aux_str):
                count_vulnibm_iot_namespyware+=1 
            elif('loader' in aux_str or 'Loader' in aux_str):
                count_vulnibm_iot_nameloader+=1 
            elif('downloader' in aux_str or 'Downloader' in aux_str):
                count_vulnibm_iot_namedownloader+=1 
            elif('distribu' in aux_str):
                count_vulnibm_iot_namedistribution+=1
            elif('cross' in aux_str or 'Cross' in aux_str or 'xss' in aux_str  or 'XSS' in aux_str ):
                count_vulnibm_iot_namexss+=1
            elif('fraud' in aux_str or 'Fraud' in aux_str):
                count_vulnibm_iot_namefraud+=1 
            elif('bootkit' in aux_str or 'Bootkit' in aux_str):
                count_vulnibm_iot_namebootkit+=1 
            elif('hosting' in aux_str or 'Hosting' in aux_str):
                count_vulnibm_iot_namehosting+=1 
            elif('bot' in aux_str or 'Bot' in aux_str):
                count_vulnibm_iot_namebot+=1 
            elif('injection' in aux_str or 'Injection' in aux_str):
                count_vulnibm_iot_nameinjection+=1 
            elif('infection' in aux_str or 'Infection' in aux_str):
                count_vulnibm_iot_nameinfection+=1 
            elif('chain' in aux_str or 'Chain' in aux_str):
                count_vulnibm_iot_namechain+=1 
            elif('imperson' in aux_str or 'Imperson' in aux_str):
                count_vulnibm_iot_nameimpersonate+=1 
            elif('espionage' in aux_str or 'Espionage' in aux_str):
                count_vulnibm_iot_namespionage+=1 
            elif('exfilt' in aux_str or 'Exfilt' in aux_str):
                count_vulnibm_iot_namexfiltration+=1 
            elif('masquerade' in aux_str or 'Masquerade' in aux_str):
                count_vulnibm_iot_namemasquerade+=1 
            elif('control' in aux_str or 'Control' in aux_str):
                count_vulnibm_iot_namecontrol+=1 
            elif('cryptojack' in aux_str or 'Cryptojack' in aux_str):
                count_vulnibm_iot_namecryptojack+=1 
            elif('remote' in aux_str or 'Remote' in aux_str):
                count_vulnibm_iot_nameremote+=1 
            else:
                count_vulnibm_iot_nameanother+=1

print("***************************ESTADÍSTICAS NOMBRE VULNERABILIDADES IBM PARTE IOT***************************")
print("\n")                            
print("\n")
print(" DE UN TOTAL DE "+str(count_vulnibm_iot_names)+" VALORES DE NOMBRE :\n") 
print("\n")
print("   - LAS ESTADISTICAS DE CADENAS DE TEXTO ENCONTRADAS EN EL VALOR DE NOMBRE DE OBJETO SON LAS SIGUIENTES:  \n")
print("            -    EN  "+str(count_vulnibm_iot_namephishing)+" VULNERABILIDADES , EL NOMBRE INCLUYE PHISHING ")
print("            -    EN  "+str(count_vulnibm_iot_namebotnet)+" VULNERABILIDADES , EL NOMBRE INCLUYE BOTNET")
print("            -    EN  "+str(count_vulnibm_iot_namereconnaissance)+" VULNERABILIDADES , EL NOMBRE INCLUYE RECONNAISSANCE ")
print("            -    EN  "+str(count_vulnibm_iot_namebackdoor)+" VULNERABILIDADES , EL NOMBRE INCLUYE BACKDOOR ")
print("            -    EN  "+str(count_vulnibm_iot_namestealer)+" VULNERABILIDADES , EL NOMBRE INCLUYE STEALER ")
print("            -    EN  "+str(count_vulnibm_iot_namexploit)+" VULNERABILIDADES , EL NOMBRE INCLUYE EXPLOIT")
print("            -    EN  "+str(count_vulnibm_iot_namedenialofservice)+" VULNERABILIDADES , EL NOMBRE INCLUYE DENIAL OF SERVICE")
print("            -    EN  "+str(count_vulnibm_iot_namebruteforce)+" VULNERABILIDADES , EL NOMBRE INCLUYE BRUTE FORCE")
print("            -    EN  "+str(count_vulnibm_iot_nameransomware)+" VULNERABILIDADES , EL NOMBRE INCLUYE RANSOMWARE ")
print("            -    EN  "+str(count_vulnibm_iot_nametrojan)+" VULNERABILIDADES , EL NOMBRE INCLUYE TROJAN")
print("            -    EN  "+str(count_vulnibm_iot_namesandbox)+" VULNERABILIDADES , EL NOMBRE INCLUYE SANDBOX")
print("            -    EN  "+str(count_vulnibm_iot_nameworm)+" VULNERABILIDADES , EL NOMBRE INCLUYE WORM ")
print("            -    EN  "+str(count_vulnibm_iot_namespam)+" VULNERABILIDADES , EL NOMBRE INCLUYE SPAM")
print("            -    EN  "+str(count_vulnibm_iot_namemalware)+" VULNERABILIDADES , EL NOMBRE INCLUYE MALWARE")
print("            -    EN  "+str(count_vulnibm_iot_namehijacking)+" VULNERABILIDADES , EL NOMBRE INCLUYE HIJACKING")
print("            -    EN  "+str(count_vulnibm_iot_namesocialengineering)+" VULNERABILIDADES , EL NOMBRE INCLUYE SOCIAL ENGINEERING ")
print("            -    EN  "+str(count_vulnibm_iot_nameloader)+" VULNERABILIDADES , EL NOMBRE INCLUYE LOADER")
print("            -    EN  "+str(count_vulnibm_iot_namespearphishing)+" VULNERABILIDADES , EL NOMBRE INCLUYE SPEAR PHISHING")
print("            -    EN  "+str(count_vulnibm_iot_namedropper)+" VULNERABILIDADES , EL NOMBRE INCLUYE DROPPER")
print("            -    EN  "+str(count_vulnibm_iot_namespyware)+" VULNERABILIDADES , EL NOMBRE INCLUYE SPYWARE ")
print("            -    EN  "+str(count_vulnibm_iot_namedownloader)+" VULNERABILIDADES , EL NOMBRE INCLUYE DOWNLOADER")
print("            -    EN  "+str(count_vulnibm_iot_namedistribution)+" VULNERABILIDADES , EL NOMBRE INCLUYE DISTRIBUTION/DISTRIBUTED")
print("            -    EN  "+str(count_vulnibm_iot_namexss)+" VULNERABILIDADES , EL NOMBRE INCLUYE CROSS SITE SCRIPTING")
print("            -    EN  "+str(count_vulnibm_iot_namefraud)+" VULNERABILIDADES , EL NOMBRE INCLUYE FRAUD ")
print("            -    EN  "+str(count_vulnibm_iot_namebootkit)+" VULNERABILIDADES , EL NOMBRE INCLUYE BOOTKIT")
print("            -    EN  "+str(count_vulnibm_iot_namehosting)+" VULNERABILIDADES , EL NOMBRE INCLUYE HOSTING")
print("            -    EN  "+str(count_vulnibm_iot_namebot)+" VULNERABILIDADES , EL NOMBRE INCLUYE BOT")
print("            -    EN  "+str(count_vulnibm_iot_nameinjection)+" VULNERABILIDADES , EL NOMBRE INCLUYE INJECTION ")
print("            -    EN  "+str(count_vulnibm_iot_nameinfection)+" VULNERABILIDADES , EL NOMBRE INCLUYE INFECTION")
print("            -    EN  "+str(count_vulnibm_iot_nameimpersonate)+" VULNERABILIDADES , EL NOMBRE INCLUYE IMPERSONATION")
print("            -    EN  "+str(count_vulnibm_iot_namechain)+" VULNERABILIDADES , EL NOMBRE INCLUYE CHAIN")
print("            -    EN  "+str(count_vulnibm_iot_namespionage)+" VULNERABILIDADES , EL NOMBRE INCLUYE ESPIONAGE")
print("            -    EN  "+str(count_vulnibm_iot_namexfiltration)+" VULNERABILIDADES , EL NOMBRE INCLUYE EXFILTRATION")
print("            -    EN  "+str(count_vulnibm_iot_namemasquerade)+" VULNERABILIDADES , EL NOMBRE INCLUYE MASQUERADE")
print("            -    EN  "+str(count_vulnibm_iot_namecontrol)+" VULNERABILIDADES , EL NOMBRE INCLUYE CONTROL")
print("            -    EN  "+str(count_vulnibm_iot_namecryptojack)+" VULNERABILIDADES , EL NOMBRE INCLUYE CRYPTOJACK")
print("            -    EN  "+str(count_vulnibm_iot_nameremote)+" VULNERABILIDADES , EL NOMBRE INCLUYE REMOTE")
print("            -    EN  "+str(count_vulnibm_iot_nameanother)+" VULNERABILIDADES , EL NOMBRE INCLUYE UNA CADENA DISTINTA")
print("\n")











print("***************************PORCENTAJES NOMBRE VULNERABILIDADES IBM PARTE IOT***************************")
print("\n")                            
                
print("\n")
print(" DE UN TOTAL DE "+str(count_vulnibm_iot_names)+" VALORES DE NOMBRE :\n") 
print("\n")
print("   - LOS PORCENTAJES DE CADENAS DE TEXTO ENCONTRADAS EN EL VALOR DE NOMBRE DE OBJETO SON LOS SIGUIENTES:  \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namephishing*100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES , EL NOMBRE INCLUYE PHISHING ")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namebotnet*100)/count_vulnibm_iot_names)))+" % DE  VULNERABILIDADES , EL NOMBRE INCLUYE BOTNET")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namereconnaissance*100)/count_vulnibm_iot_names)))+" % DE   VULNERABILIDADES , EL NOMBRE INCLUYE RECONNAISSANCE ")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namebackdoor*100)/count_vulnibm_iot_names)))+" % DE  VULNERABILIDADES , EL NOMBRE INCLUYE BACKDOOR ")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namestealer*100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES , EL NOMBRE INCLUYE STEALER ")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namexploit*100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES , EL NOMBRE INCLUYE EXPLOIT")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namedenialofservice*100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES , EL NOMBRE INCLUYE DENIAL OF SERVICE")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namebruteforce*100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES , EL NOMBRE INCLUYE BRUTE FORCE")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_nameransomware*100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES , EL NOMBRE INCLUYE RANSOMWARE ")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_nametrojan*100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES , EL NOMBRE INCLUYE TROJAN")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namesandbox*100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES , EL NOMBRE INCLUYE SANDBOX")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_nameworm*100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES , EL NOMBRE INCLUYE WORM ")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namespam*100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES , EL NOMBRE INCLUYE SPAM")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namemalware*100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES , EL NOMBRE INCLUYE MALWARE")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namehijacking*100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES , EL NOMBRE INCLUYE HIJACKING")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namesocialengineering*100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES , EL NOMBRE INCLUYE SOCIAL ENGINEERING ")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_nameloader*100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES , EL NOMBRE INCLUYE LOADER")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namespearphishing*100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES , EL NOMBRE INCLUYE SPEAR PHISHING")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namedropper*100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES , EL NOMBRE INCLUYE DROPPER")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namespyware*100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES , EL NOMBRE INCLUYE SPYWARE ")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namedownloader*100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES , EL NOMBRE INCLUYE DOWNLOADER")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namedistribution*100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES , EL NOMBRE INCLUYE DISTRIBUTION/DISTRIBUTED")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namexss*100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES , EL NOMBRE INCLUYE CROSS SITE SCRIPTING")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namefraud*100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES , EL NOMBRE INCLUYE FRAUD ")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namebootkit*100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES , EL NOMBRE INCLUYE BOOTKIT")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namehosting*100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES , EL NOMBRE INCLUYE HOSTING")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namebot*100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES , EL NOMBRE INCLUYE BOT")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_nameinjection*100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES , EL NOMBRE INCLUYE INJECTION ")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_nameinfection*100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES , EL NOMBRE INCLUYE INFECTION")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_nameimpersonate*100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES , EL NOMBRE INCLUYE IMPERSONATION")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namechain*100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES , EL NOMBRE INCLUYE CHAIN")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namespionage*100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES , EL NOMBRE INCLUYE ESPIONAGE")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namexfiltration*100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES , EL NOMBRE INCLUYE EXFILTRATION")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namemasquerade *100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES , EL NOMBRE INCLUYE MASQUERADE")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namecontrol *100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES , EL NOMBRE INCLUYE CONTROL")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_namecryptojack*100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES , EL NOMBRE INCLUYE CRYPTOJACK")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_nameremote*100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES , EL NOMBRE INCLUYE REMOTE")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_nameanother *100)/count_vulnibm_iot_names)))+" % DE VULNERABILIDADES , EL NOMBRE INCLUYE UNA CADENA DISTINTA")
print("\n")


















#Abro los ficheros con los que voy a tratar




df_vulnibm_sh = pd.read_excel('ibm_threat_activity_report_smarthome_2023_v2.xlsx')
         
#Variable que almacenara el contador total de valores de nombre
count_vulnibm_sh_names=0
#Variables que almacenan el contador de valores especificos de nombre
count_vulnibm_sh_namephishing=0
count_vulnibm_sh_namebotnet=0
count_vulnibm_sh_namereconnaissance=0
count_vulnibm_sh_namebackdoor=0
count_vulnibm_sh_namestealer=0
count_vulnibm_sh_namexploit=0
count_vulnibm_sh_namedenialofservice=0
count_vulnibm_sh_namebruteforce=0
count_vulnibm_sh_nameransomware=0
count_vulnibm_sh_nametrojan=0
count_vulnibm_sh_namesandbox=0
count_vulnibm_sh_nameworm=0
count_vulnibm_sh_namespam=0
count_vulnibm_sh_namemalware=0
count_vulnibm_sh_namehijacking=0
count_vulnibm_sh_namesocialengineering=0
count_vulnibm_sh_namespearphishing=0
count_vulnibm_sh_namedropper=0
count_vulnibm_sh_namespyware=0
count_vulnibm_sh_nameloader=0
count_vulnibm_sh_namedownloader=0
count_vulnibm_sh_namedistribution=0
count_vulnibm_sh_namexss=0
count_vulnibm_sh_namefraud=0
count_vulnibm_sh_namebootkit=0
count_vulnibm_sh_namehosting=0
count_vulnibm_sh_namebot=0
count_vulnibm_sh_nameinjection=0
count_vulnibm_sh_nameinfection=0
count_vulnibm_sh_nameimpersonate=0
count_vulnibm_sh_namechain=0
count_vulnibm_sh_namespionage=0
count_vulnibm_sh_namexfiltration=0
count_vulnibm_sh_namemasquerade=0
count_vulnibm_sh_namecontrol=0
count_vulnibm_sh_namecryptojack=0
count_vulnibm_sh_nameremote=0
count_vulnibm_sh_nameanother=0


#Comprobamos el contenido de name
for r in range(0,len(df_vulnibm_sh["name"])):
    #Comprobamos si hay varios objetos en la fila actual
    if('[' in df_vulnibm_sh["name"][r]):
        aux=df_vulnibm_sh["name"][r].split(",")
        for l in range(0,len(aux)):
            if(len(aux)>0):
                #Obtengo el valor de nombre y aumento contadores segun el tipo que sea
                aux_str=aux[l].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
                if(aux_str!='NONE'):
                    count_vulnibm_sh_names+=1
                    if('phishing' in aux_str or 'Phishing' in aux_str):
                        count_vulnibm_sh_namephishing+=1
                    elif('Botnet' in aux_str or 'botnet' in aux_str or 'BotNet' in aux_str):
                        count_vulnibm_sh_namebotnet+=1
                    elif('reconnaissance' in aux_str or 'Reconnaissance' in aux_str):
                        count_vulnibm_sh_namereconnaissance+=1
                    elif('Backdoor' in aux_str or 'backdoor' in aux_str):
                        count_vulnibm_sh_namebackdoor=1                            
                    elif('stealer' in aux_str  or 'Stealer' in aux_str):
                        count_vulnibm_sh_namestealer+=1                           
                    elif('exploit' in aux_str or 'Exploit' in aux_str):
                        count_vulnibm_sh_namexploit+=1                           
                    elif('denialofservice' in aux_str or 'ddos' in aux_str or 'DDoS' in aux_str or 'Denial' in aux_str):
                        count_vulnibm_sh_namedenialofservice+=1                           
                    elif('brute' in aux_str or 'Brute' in aux_str ):
                        count_vulnibm_sh_namebruteforce+=1                           
                    elif('Ransomware' in aux_str or 'ransomware' in aux_str):
                        count_vulnibm_sh_nameransomware+=1                           
                    elif('Trojan' in aux_str or 'Trojans' in aux_str or 'trojan' in aux_str or 'trojans' in aux_str):
                        count_vulnibm_sh_nametrojan+=1                           
                    elif('Sandbox' in aux_str or 'sandbox' in aux_str):
                        count_vulnibm_sh_namesandbox+=1                           
                    elif('worm' in aux_str or 'Worm' in aux_str):
                        count_vulnibm_sh_nameworm+=1                           
                    elif('spam' in aux_str or 'Spam' in aux_str):
                        count_vulnibm_sh_namespam+=1                           
                    elif('Malware' in aux_str or 'malware' in aux_str):
                        count_vulnibm_sh_namemalware+=1  
                    elif('hijacking' in aux_str or 'Hijacking' in aux_str or 'Hijack' in aux_str or 'hijack' in aux_str):
                        count_vulnibm_sh_namehijacking+=1     
                    elif('Social' in aux_str or 'social' in aux_str):
                        count_vulnibm_sh_namesocialengineering+=1 
                    elif('loader' in aux_str or 'Loader' in aux_str):
                        count_vulnibm_sh_nameloader+=1 
                    elif('spearphishing' in aux_str or 'Spearphishing' in aux_str):
                        count_vulnibm_sh_namespearphishing+=1 
                    elif('dropper' in aux_str or 'Dropper' in aux_str):
                        count_vulnibm_sh_namesocialengineering+=1 
                    elif('spyware' in aux_str or 'Spyware' in aux_str):
                        count_vulnibm_sh_namespyware+=1 
                    elif('loader' in aux_str or 'Loader' in aux_str):
                        count_vulnibm_sh_nameloader+=1 
                    elif('downloader' in aux_str or 'Downloader' in aux_str):
                        count_vulnibm_sh_namedownloader+=1 
                    elif('distribu' in aux_str):
                        count_vulnibm_sh_namedistribution+=1
                    elif('cross' in aux_str or 'Cross' in aux_str or 'xss' in aux_str  or 'XSS' in aux_str ):
                        count_vulnibm_sh_namexss+=1
                    elif('fraud' in aux_str or 'Fraud' in aux_str):
                        count_vulnibm_sh_namefraud+=1 
                    elif('bootkit' in aux_str or 'Bootkit' in aux_str):
                        count_vulnibm_sh_namebootkit+=1 
                    elif('hosting' in aux_str or 'Hosting' in aux_str):
                        count_vulnibm_sh_namehosting+=1 
                    elif('bot' in aux_str or 'Bot' in aux_str):
                        count_vulnibm_sh_namebot+=1 
                    elif('injection' in aux_str or 'Injection' in aux_str):
                        count_vulnibm_sh_nameinjection+=1 
                    elif('infection' in aux_str or 'Infection' in aux_str):
                        count_vulnibm_sh_nameinfection+=1 
                    elif('chain' in aux_str or 'Chain' in aux_str):
                        count_vulnibm_sh_namechain+=1 
                    elif('imperson' in aux_str or 'Imperson' in aux_str):
                        count_vulnibm_sh_nameimpersonate+=1 
                    elif('espionage' in aux_str or 'Espionage' in aux_str):
                        count_vulnibm_sh_namespionage+=1 
                    elif('exfilt' in aux_str or 'Exfilt' in aux_str):
                        count_vulnibm_sh_namexfiltration+=1 
                    elif('masquerade' in aux_str or 'Masquerade' in aux_str):
                        count_vulnibm_sh_namemasquerade+=1 
                    elif('control' in aux_str or 'Control' in aux_str):
                        count_vulnibm_sh_namecontrol+=1 
                    elif('cryptojack' in aux_str or 'Cryptojack' in aux_str):
                        count_vulnibm_sh_namecryptojack+=1 
                    elif('remote' in aux_str or 'Remote' in aux_str):
                        count_vulnibm_sh_nameremote+=1 
                    else:
                        count_vulnibm_sh_nameanother+=1
    else:
        #Obtengo el valor de nombre y aumento contadores segun el tipo que sea
        aux_str=df_vulnibm_sh["name"][r].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
        if(aux_str!='NONE'):
            count_vulnibm_sh_names+=1
            if('phishing' in aux_str or 'Phishing' in aux_str):
                count_vulnibm_sh_namephishing+=1
            elif('Botnet' in aux_str or 'botnet' in aux_str or 'BotNet' in aux_str):
                count_vulnibm_sh_namebotnet+=1
            elif('reconnaissance' in aux_str or 'Reconnaissance' in aux_str):
                count_vulnibm_sh_namereconnaissance+=1
            elif('Backdoor' in aux_str or 'backdoor' in aux_str):
                count_vulnibm_sh_namebackdoor=1                            
            elif('stealer' in aux_str  or 'Stealer' in aux_str):
                count_vulnibm_sh_namestealer+=1                           
            elif('exploit' in aux_str or 'Exploit' in aux_str):
                count_vulnibm_sh_namexploit+=1                           
            elif('denialofservice' in aux_str or 'ddos' in aux_str or 'DDoS' in aux_str or 'Denial' in aux_str):
                count_vulnibm_sh_namedenialofservice+=1                           
            elif('brute' in aux_str or 'Brute' in aux_str ):
                count_vulnibm_sh_namebruteforce+=1                           
            elif('Ransomware' in aux_str or 'ransomware' in aux_str):
                count_vulnibm_sh_nameransomware+=1                           
            elif('Trojan' in aux_str or 'Trojans' in aux_str or 'trojan' in aux_str or 'trojans' in aux_str):
                count_vulnibm_sh_nametrojan+=1                           
            elif('Sandbox' in aux_str or 'sandbox' in aux_str):
                count_vulnibm_sh_namesandbox+=1                           
            elif('worm' in aux_str or 'Worm' in aux_str):
                count_vulnibm_sh_nameworm+=1                           
            elif('spam' in aux_str or 'Spam' in aux_str):
                count_vulnibm_sh_namespam+=1                           
            elif('Malware' in aux_str or 'malware' in aux_str):
                count_vulnibm_sh_namemalware+=1  
            elif('hijacking' in aux_str or 'Hijacking' in aux_str or 'Hijack' in aux_str or 'hijack' in aux_str):
                count_vulnibm_sh_namehijacking+=1     
            elif('Social' in aux_str or 'social' in aux_str):
                count_vulnibm_sh_namesocialengineering+=1 
            elif('loader' in aux_str or 'Loader' in aux_str):
                count_vulnibm_sh_nameloader+=1 
            elif('spearphishing' in aux_str or 'Spearphishing' in aux_str):
                count_vulnibm_sh_namespearphishing+=1 
            elif('dropper' in aux_str or 'Dropper' in aux_str):
                count_vulnibm_sh_namesocialengineering+=1 
            elif('spyware' in aux_str or 'Spyware' in aux_str):
                count_vulnibm_sh_namespyware+=1 
            elif('loader' in aux_str or 'Loader' in aux_str):
                count_vulnibm_sh_nameloader+=1 
            elif('downloader' in aux_str or 'Downloader' in aux_str):
                count_vulnibm_sh_namedownloader+=1 
            elif('distribu' in aux_str):
                count_vulnibm_sh_namedistribution+=1
            elif('cross' in aux_str or 'Cross' in aux_str or 'xss' in aux_str  or 'XSS' in aux_str ):
                count_vulnibm_sh_namexss+=1
            elif('fraud' in aux_str or 'Fraud' in aux_str):
                count_vulnibm_sh_namefraud+=1 
            elif('bootkit' in aux_str or 'Bootkit' in aux_str):
                count_vulnibm_sh_namebootkit+=1 
            elif('hosting' in aux_str or 'Hosting' in aux_str):
                count_vulnibm_sh_namehosting+=1 
            elif('bot' in aux_str or 'Bot' in aux_str):
                count_vulnibm_sh_namebot+=1 
            elif('injection' in aux_str or 'Injection' in aux_str):
                count_vulnibm_sh_nameinjection+=1 
            elif('infection' in aux_str or 'Infection' in aux_str):
                count_vulnibm_sh_nameinfection+=1 
            elif('chain' in aux_str or 'Chain' in aux_str):
                count_vulnibm_sh_namechain+=1 
            elif('imperson' in aux_str or 'Imperson' in aux_str):
                count_vulnibm_sh_nameimpersonate+=1 
            elif('espionage' in aux_str or 'Espionage' in aux_str):
                count_vulnibm_sh_namespionage+=1 
            elif('exfilt' in aux_str or 'Exfilt' in aux_str):
                count_vulnibm_sh_namexfiltration+=1 
            elif('masquerade' in aux_str or 'Masquerade' in aux_str):
                count_vulnibm_sh_namemasquerade+=1 
            elif('control' in aux_str or 'Control' in aux_str):
                count_vulnibm_sh_namecontrol+=1 
            elif('cryptojack' in aux_str or 'Cryptojack' in aux_str):
                count_vulnibm_sh_namecryptojack+=1 
            elif('remote' in aux_str or 'Remote' in aux_str):
                count_vulnibm_sh_nameremote+=1 
            else:
                count_vulnibm_sh_nameanother+=1
                
                
                
print("***************************ESTADÍSTICAS NOMBRE VULNERABILIDADES IBM PARTE SMART HOME***************************")
print("\n")                            
                
print("\n")
print(" DE UN TOTAL DE "+str(count_vulnibm_sh_names)+" VALORES DE NOMBRE :\n") 
print("\n")
print("   - LAS ESTADISTICAS DE CADENAS DE TEXTO ENCONTRADAS EN EL VALOR DE NOMBRE DE OBJETO SON LAS SIGUIENTES:  \n")
print("            -    EN  "+str(count_vulnibm_sh_namephishing)+" VULNERABILIDADES , EL NOMBRE INCLUYE PHISHING ")
print("            -    EN  "+str(count_vulnibm_sh_namebotnet)+" VULNERABILIDADES , EL NOMBRE INCLUYE BOTNET")
print("            -    EN  "+str(count_vulnibm_sh_namereconnaissance)+" VULNERABILIDADES , EL NOMBRE INCLUYE RECONNAISSANCE ")
print("            -    EN  "+str(count_vulnibm_sh_namebackdoor)+" VULNERABILIDADES , EL NOMBRE INCLUYE BACKDOOR ")
print("            -    EN  "+str(count_vulnibm_sh_namestealer)+" VULNERABILIDADES , EL NOMBRE INCLUYE STEALER ")
print("            -    EN  "+str(count_vulnibm_sh_namexploit)+" VULNERABILIDADES , EL NOMBRE INCLUYE EXPLOIT")
print("            -    EN  "+str(count_vulnibm_sh_namedenialofservice)+" VULNERABILIDADES , EL NOMBRE INCLUYE DENIAL OF SERVICE")
print("            -    EN  "+str(count_vulnibm_sh_namebruteforce)+" VULNERABILIDADES , EL NOMBRE INCLUYE BRUTE FORCE")
print("            -    EN  "+str(count_vulnibm_sh_nameransomware)+" VULNERABILIDADES , EL NOMBRE INCLUYE RANSOMWARE ")
print("            -    EN  "+str(count_vulnibm_sh_nametrojan)+" VULNERABILIDADES , EL NOMBRE INCLUYE TROJAN")
print("            -    EN  "+str(count_vulnibm_sh_namesandbox)+" VULNERABILIDADES , EL NOMBRE INCLUYE SANDBOX")
print("            -    EN  "+str(count_vulnibm_sh_nameworm)+" VULNERABILIDADES , EL NOMBRE INCLUYE WORM ")
print("            -    EN  "+str(count_vulnibm_sh_namespam)+" VULNERABILIDADES , EL NOMBRE INCLUYE SPAM")
print("            -    EN  "+str(count_vulnibm_sh_namemalware)+" VULNERABILIDADES , EL NOMBRE INCLUYE MALWARE")
print("            -    EN  "+str(count_vulnibm_sh_namehijacking)+" VULNERABILIDADES , EL NOMBRE INCLUYE HIJACKING")
print("            -    EN  "+str(count_vulnibm_sh_namesocialengineering)+" VULNERABILIDADES , EL NOMBRE INCLUYE SOCIAL ENGINEERING ")
print("            -    EN  "+str(count_vulnibm_sh_nameloader)+" VULNERABILIDADES , EL NOMBRE INCLUYE LOADER")
print("            -    EN  "+str(count_vulnibm_sh_namespearphishing)+" VULNERABILIDADES , EL NOMBRE INCLUYE SPEAR PHISHING")
print("            -    EN  "+str(count_vulnibm_sh_namedropper)+" VULNERABILIDADES , EL NOMBRE INCLUYE DROPPER")
print("            -    EN  "+str(count_vulnibm_sh_namespyware)+" VULNERABILIDADES , EL NOMBRE INCLUYE SPYWARE ")
print("            -    EN  "+str(count_vulnibm_sh_namedownloader)+" VULNERABILIDADES , EL NOMBRE INCLUYE DOWNLOADER")
print("            -    EN  "+str(count_vulnibm_sh_namedistribution)+" VULNERABILIDADES , EL NOMBRE INCLUYE DISTRIBUTION/DISTRIBUTED")
print("            -    EN  "+str(count_vulnibm_sh_namexss)+" VULNERABILIDADES , EL NOMBRE INCLUYE CROSS SITE SCRIPTING")
print("            -    EN  "+str(count_vulnibm_sh_namefraud)+" VULNERABILIDADES , EL NOMBRE INCLUYE FRAUD ")
print("            -    EN  "+str(count_vulnibm_sh_namebootkit)+" VULNERABILIDADES , EL NOMBRE INCLUYE BOOTKIT")
print("            -    EN  "+str(count_vulnibm_sh_namehosting)+" VULNERABILIDADES , EL NOMBRE INCLUYE HOSTING")
print("            -    EN  "+str(count_vulnibm_sh_namebot)+" VULNERABILIDADES , EL NOMBRE INCLUYE BOT")
print("            -    EN  "+str(count_vulnibm_sh_nameinjection)+" VULNERABILIDADES , EL NOMBRE INCLUYE INJECTION ")
print("            -    EN  "+str(count_vulnibm_sh_nameinfection)+" VULNERABILIDADES , EL NOMBRE INCLUYE INFECTION")
print("            -    EN  "+str(count_vulnibm_sh_nameimpersonate)+" VULNERABILIDADES , EL NOMBRE INCLUYE IMPERSONATION")
print("            -    EN  "+str(count_vulnibm_sh_namechain)+" VULNERABILIDADES , EL NOMBRE INCLUYE CHAIN")
print("            -    EN  "+str(count_vulnibm_sh_namespionage)+" VULNERABILIDADES , EL NOMBRE INCLUYE ESPIONAGE")
print("            -    EN  "+str(count_vulnibm_sh_namexfiltration)+" VULNERABILIDADES , EL NOMBRE INCLUYE EXFILTRATION")
print("            -    EN  "+str(count_vulnibm_sh_namemasquerade )+" VULNERABILIDADES , EL NOMBRE INCLUYE MASQUERADE")
print("            -    EN  "+str(count_vulnibm_sh_namecontrol )+" VULNERABILIDADES , EL NOMBRE INCLUYE CONTROL")
print("            -    EN  "+str(count_vulnibm_sh_namecryptojack)+" VULNERABILIDADES , EL NOMBRE INCLUYE CRYPTOJACK")
print("            -    EN  "+str(count_vulnibm_sh_nameremote)+" VULNERABILIDADES , EL NOMBRE INCLUYE REMOTE")
print("            -    EN  "+str(count_vulnibm_sh_nameanother )+" VULNERABILIDADES , EL NOMBRE INCLUYE UNA CADENA DISTINTA")
print("\n")
                                    





print("***************************PORCENTAJES NOMBRE VULNERABILIDADES IBM PARTE SMART HOME***************************")
print("\n")                            
                
print("\n")
print(" DE UN TOTAL DE "+str(count_vulnibm_sh_names)+" VALORES DE NOMBRE :\n") 
print("\n")
print("   - LOS PORCENTAJES DE CADENAS DE TEXTO ENCONTRADAS EN EL VALOR DE NOMBRE DE OBJETO SON LOS SIGUIENTES:  \n")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_namephishing*100)/count_vulnibm_sh_names)))+" % DE VULNERABILIDADES , EL NOMBRE INCLUYE PHISHING ")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_namebotnet*100)/count_vulnibm_sh_names)))+" % DE  VULNERABILIDADES , EL NOMBRE INCLUYE BOTNET")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_namereconnaissance*100)/count_vulnibm_sh_names)))+" % DE   VULNERABILIDADES , EL NOMBRE INCLUYE RECONNAISSANCE ")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_namebackdoor*100)/count_vulnibm_sh_names)))+" % DE  VULNERABILIDADES , EL NOMBRE INCLUYE BACKDOOR ")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_namestealer*100)/count_vulnibm_sh_names)))+" % DE VULNERABILIDADES , EL NOMBRE INCLUYE STEALER ")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_namexploit*100)/count_vulnibm_sh_names)))+" % DE VULNERABILIDADES , EL NOMBRE INCLUYE EXPLOIT")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_namedenialofservice*100)/count_vulnibm_sh_names)))+" % DE VULNERABILIDADES , EL NOMBRE INCLUYE DENIAL OF SERVICE")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_namebruteforce*100)/count_vulnibm_sh_names)))+" % DE VULNERABILIDADES , EL NOMBRE INCLUYE BRUTE FORCE")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_nameransomware*100)/count_vulnibm_sh_names)))+" % DE VULNERABILIDADES , EL NOMBRE INCLUYE RANSOMWARE ")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_nametrojan*100)/count_vulnibm_sh_names)))+" % DE VULNERABILIDADES , EL NOMBRE INCLUYE TROJAN")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_namesandbox*100)/count_vulnibm_sh_names)))+" % DE VULNERABILIDADES , EL NOMBRE INCLUYE SANDBOX")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_nameworm*100)/count_vulnibm_sh_names)))+" % DE VULNERABILIDADES , EL NOMBRE INCLUYE WORM ")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_namespam*100)/count_vulnibm_sh_names)))+" % DE VULNERABILIDADES , EL NOMBRE INCLUYE SPAM")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_namemalware*100)/count_vulnibm_sh_names)))+" % DE VULNERABILIDADES , EL NOMBRE INCLUYE MALWARE")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_namehijacking*100)/count_vulnibm_sh_names)))+" % DE VULNERABILIDADES , EL NOMBRE INCLUYE HIJACKING")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_namesocialengineering*100)/count_vulnibm_sh_names)))+" % DE VULNERABILIDADES , EL NOMBRE INCLUYE SOCIAL ENGINEERING ")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_nameloader*100)/count_vulnibm_sh_names)))+" % DE VULNERABILIDADES , EL NOMBRE INCLUYE LOADER")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_namespearphishing*100)/count_vulnibm_sh_names)))+" % DE VULNERABILIDADES , EL NOMBRE INCLUYE SPEAR PHISHING")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_namedropper*100)/count_vulnibm_sh_names)))+" % DE VULNERABILIDADES , EL NOMBRE INCLUYE DROPPER")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_namespyware*100)/count_vulnibm_sh_names)))+" % DE VULNERABILIDADES , EL NOMBRE INCLUYE SPYWARE ")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_namedownloader*100)/count_vulnibm_sh_names)))+" % DE VULNERABILIDADES , EL NOMBRE INCLUYE DOWNLOADER")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_namedistribution*100)/count_vulnibm_sh_names)))+" % DE VULNERABILIDADES , EL NOMBRE INCLUYE DISTRIBUTION/DISTRIBUTED")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_namexss*100)/count_vulnibm_sh_names)))+" % DE VULNERABILIDADES , EL NOMBRE INCLUYE CROSS SITE SCRIPTING")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_namefraud*100)/count_vulnibm_sh_names)))+" % DE VULNERABILIDADES , EL NOMBRE INCLUYE FRAUD ")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_namebootkit*100)/count_vulnibm_sh_names)))+" % DE VULNERABILIDADES , EL NOMBRE INCLUYE BOOTKIT")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_namehosting*100)/count_vulnibm_sh_names)))+" % DE VULNERABILIDADES , EL NOMBRE INCLUYE HOSTING")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_namebot*100)/count_vulnibm_sh_names)))+" % DE VULNERABILIDADES , EL NOMBRE INCLUYE BOT")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_nameinjection*100)/count_vulnibm_sh_names)))+" % DE VULNERABILIDADES , EL NOMBRE INCLUYE INJECTION ")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_nameinfection*100)/count_vulnibm_sh_names)))+" % DE VULNERABILIDADES , EL NOMBRE INCLUYE INFECTION")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_nameimpersonate*100)/count_vulnibm_sh_names)))+" % DE VULNERABILIDADES , EL NOMBRE INCLUYE IMPERSONATION")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_namechain*100)/count_vulnibm_sh_names)))+" % DE VULNERABILIDADES , EL NOMBRE INCLUYE CHAIN")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_namespionage*100)/count_vulnibm_sh_names)))+" % DE VULNERABILIDADES , EL NOMBRE INCLUYE ESPIONAGE")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_namexfiltration*100)/count_vulnibm_sh_names)))+" % DE VULNERABILIDADES , EL NOMBRE INCLUYE EXFILTRATION")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_namemasquerade *100)/count_vulnibm_sh_names)))+" % DE VULNERABILIDADES , EL NOMBRE INCLUYE MASQUERADE")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_namecontrol *100)/count_vulnibm_sh_names)))+" % DE VULNERABILIDADES , EL NOMBRE INCLUYE CONTROL")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_namecryptojack*100)/count_vulnibm_sh_names)))+" % DE VULNERABILIDADES , EL NOMBRE INCLUYE CRYPTOJACK")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_nameremote*100)/count_vulnibm_sh_names)))+" % DE VULNERABILIDADES , EL NOMBRE INCLUYE REMOTE")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_nameanother *100)/count_vulnibm_sh_names)))+" % DE VULNERABILIDADES , EL NOMBRE INCLUYE UNA CADENA DISTINTA")
print("\n")

















print("***************************ESTADÍSTICAS NOMBRE VULNERABILIDADES IBM PARTE IOT Y SMART HOME CONJUNTAS***************************")
print("\n")                            
print("\n")
print(" DE UN TOTAL DE "+str(count_vulnibm_sh_names+count_vulnibm_iot_names)+" VALORES DE NOMBRE :\n") 
print("\n")
print("   - LAS ESTADISTICAS DE CADENAS DE TEXTO ENCONTRADAS EN EL VALOR DE NOMBRE DE OBJETO SON LAS SIGUIENTES:  \n")
print("            -    EN  "+str(count_vulnibm_sh_namephishing+count_vulnibm_iot_namephishing)+" VULNERABILIDADES , EL NOMBRE INCLUYE PHISHING ")
print("            -    EN  "+str(count_vulnibm_sh_namebotnet+count_vulnibm_iot_namebotnet)+" VULNERABILIDADES , EL NOMBRE INCLUYE BOTNET")
print("            -    EN  "+str(count_vulnibm_sh_namereconnaissance+count_vulnibm_iot_namereconnaissance)+" VULNERABILIDADES , EL NOMBRE INCLUYE RECONNAISSANCE ")
print("            -    EN  "+str(count_vulnibm_sh_namebackdoor+count_vulnibm_iot_namebackdoor)+" VULNERABILIDADES , EL NOMBRE INCLUYE BACKDOOR ")
print("            -    EN  "+str(count_vulnibm_sh_namestealer+count_vulnibm_iot_namestealer)+" VULNERABILIDADES , EL NOMBRE INCLUYE STEALER ")
print("            -    EN  "+str(count_vulnibm_sh_namexploit+count_vulnibm_iot_namexploit)+" VULNERABILIDADES , EL NOMBRE INCLUYE EXPLOIT")
print("            -    EN  "+str(count_vulnibm_sh_namedenialofservice+count_vulnibm_iot_namedenialofservice)+" VULNERABILIDADES , EL NOMBRE INCLUYE DENIAL OF SERVICE")
print("            -    EN  "+str(count_vulnibm_sh_namebruteforce+count_vulnibm_iot_namebruteforce)+" VULNERABILIDADES , EL NOMBRE INCLUYE BRUTE FORCE")
print("            -    EN  "+str(count_vulnibm_sh_nameransomware+count_vulnibm_iot_nameransomware)+" VULNERABILIDADES , EL NOMBRE INCLUYE RANSOMWARE ")
print("            -    EN  "+str(count_vulnibm_sh_nametrojan+count_vulnibm_iot_nametrojan)+" VULNERABILIDADES , EL NOMBRE INCLUYE TROJAN")
print("            -    EN  "+str(count_vulnibm_sh_namesandbox+count_vulnibm_iot_namesandbox)+" VULNERABILIDADES , EL NOMBRE INCLUYE SANDBOX")
print("            -    EN  "+str(count_vulnibm_sh_nameworm+count_vulnibm_iot_nameworm)+" VULNERABILIDADES , EL NOMBRE INCLUYE WORM ")
print("            -    EN  "+str(count_vulnibm_sh_namespam+count_vulnibm_iot_namespam)+" VULNERABILIDADES , EL NOMBRE INCLUYE SPAM")
print("            -    EN  "+str(count_vulnibm_sh_namemalware+count_vulnibm_iot_namemalware)+" VULNERABILIDADES , EL NOMBRE INCLUYE MALWARE")
print("            -    EN  "+str(count_vulnibm_sh_namehijacking+count_vulnibm_iot_namehijacking)+" VULNERABILIDADES , EL NOMBRE INCLUYE HIJACKING")
print("            -    EN  "+str(count_vulnibm_sh_namesocialengineering+count_vulnibm_iot_namesocialengineering)+" VULNERABILIDADES , EL NOMBRE INCLUYE SOCIAL ENGINEERING ")
print("            -    EN  "+str(count_vulnibm_sh_nameloader+count_vulnibm_iot_nameloader)+" VULNERABILIDADES , EL NOMBRE INCLUYE LOADER")
print("            -    EN  "+str(count_vulnibm_sh_namespearphishing+count_vulnibm_iot_namespearphishing)+" VULNERABILIDADES , EL NOMBRE INCLUYE SPEAR PHISHING")
print("            -    EN  "+str(count_vulnibm_sh_namedropper+count_vulnibm_iot_namedropper)+" VULNERABILIDADES , EL NOMBRE INCLUYE DROPPER")
print("            -    EN  "+str(count_vulnibm_sh_namespyware+count_vulnibm_iot_namespyware)+" VULNERABILIDADES , EL NOMBRE INCLUYE SPYWARE ")
print("            -    EN  "+str(count_vulnibm_sh_namedownloader+count_vulnibm_iot_namedownloader)+" VULNERABILIDADES , EL NOMBRE INCLUYE DOWNLOADER")
print("            -    EN  "+str(count_vulnibm_sh_namedistribution+count_vulnibm_iot_namedistribution)+" VULNERABILIDADES , EL NOMBRE INCLUYE DISTRIBUTION/DISTRIBUTED")
print("            -    EN  "+str(count_vulnibm_sh_namexss+count_vulnibm_iot_namexss)+" VULNERABILIDADES , EL NOMBRE INCLUYE CROSS SITE SCRIPTING")
print("            -    EN  "+str(count_vulnibm_sh_namefraud+count_vulnibm_iot_namefraud)+" VULNERABILIDADES , EL NOMBRE INCLUYE FRAUD ")
print("            -    EN  "+str(count_vulnibm_sh_namebootkit+count_vulnibm_iot_namebootkit)+" VULNERABILIDADES , EL NOMBRE INCLUYE BOOTKIT")
print("            -    EN  "+str(count_vulnibm_sh_namehosting+count_vulnibm_iot_namehosting)+" VULNERABILIDADES , EL NOMBRE INCLUYE HOSTING")
print("            -    EN  "+str(count_vulnibm_sh_namebot+count_vulnibm_iot_namebot)+" VULNERABILIDADES , EL NOMBRE INCLUYE BOT")
print("            -    EN  "+str(count_vulnibm_sh_nameinjection+count_vulnibm_iot_nameinjection)+" VULNERABILIDADES , EL NOMBRE INCLUYE INJECTION ")
print("            -    EN  "+str(count_vulnibm_sh_nameinfection+count_vulnibm_iot_nameinfection)+" VULNERABILIDADES , EL NOMBRE INCLUYE INFECTION")
print("            -    EN  "+str(count_vulnibm_sh_nameimpersonate+count_vulnibm_iot_nameimpersonate)+" VULNERABILIDADES , EL NOMBRE INCLUYE IMPERSONATION")
print("            -    EN  "+str(count_vulnibm_sh_namechain+count_vulnibm_iot_namechain)+" VULNERABILIDADES , EL NOMBRE INCLUYE CHAIN")
print("            -    EN  "+str(count_vulnibm_sh_namespionage+count_vulnibm_iot_namespionage)+" VULNERABILIDADES , EL NOMBRE INCLUYE ESPIONAGE")
print("            -    EN  "+str(count_vulnibm_sh_namexfiltration+count_vulnibm_iot_namexfiltration)+" VULNERABILIDADES , EL NOMBRE INCLUYE EXFILTRATION")
print("            -    EN  "+str(count_vulnibm_sh_namemasquerade+count_vulnibm_iot_namemasquerade)+" VULNERABILIDADES , EL NOMBRE INCLUYE MASQUERADE")
print("            -    EN  "+str(count_vulnibm_sh_namecontrol+count_vulnibm_iot_namecontrol)+" VULNERABILIDADES , EL NOMBRE INCLUYE CONTROL")
print("            -    EN  "+str(count_vulnibm_sh_namecryptojack+count_vulnibm_iot_namecryptojack)+" VULNERABILIDADES , EL NOMBRE INCLUYE CRYPTOJACK")
print("            -    EN  "+str(count_vulnibm_sh_nameremote+count_vulnibm_iot_nameremote)+" VULNERABILIDADES , EL NOMBRE INCLUYE REMOTE")
print("            -    EN  "+str(count_vulnibm_sh_nameanother+count_vulnibm_iot_nameanother)+" VULNERABILIDADES , EL NOMBRE INCLUYE UNA CADENA DISTINTA")
print("\n")
                                    







print("***************************PORCENTAJES NOMBRE VULNERABILIDADES IBM PARTE IOT Y SMART HOME CONJUNTAS***************************")
print("\n")                            
                
print("\n")
print(" DE UN TOTAL DE "+str(count_vulnibm_sh_names+count_vulnibm_iot_names)+" VALORES DE NOMBRE :\n") 
print("\n")
print("   - LOS PORCENTAJES DE CADENAS DE TEXTO ENCONTRADAS EN EL VALOR DE NOMBRE DE OBJETO SON LOS SIGUIENTES:  \n")
print("            -    EN EL  "+str(float((((count_vulnibm_sh_namephishing+count_vulnibm_iot_namephishing)*100)/(count_vulnibm_iot_names+count_vulnibm_sh_names))))+" % DE VULNERABILIDADES , EL NOMBRE INCLUYE PHISHING ")
print("            -    EN EL  "+str(float((((count_vulnibm_sh_namebotnet+count_vulnibm_iot_namebotnet)*100)/(count_vulnibm_iot_names+count_vulnibm_sh_names))))+" % DE VULNERABILIDADES , EL NOMBRE INCLUYE BOTNET")
print("            -    EN EL  "+str(float((((count_vulnibm_sh_namereconnaissance+count_vulnibm_iot_namereconnaissance)*100)/(count_vulnibm_iot_names+count_vulnibm_sh_names))))+" % DE VULNERABILIDADES , EL NOMBRE INCLUYE RECONNAISSANCE ")
print("            -    EN EL  "+str(float((((count_vulnibm_sh_namebackdoor+count_vulnibm_iot_namebackdoor)*100)/(count_vulnibm_iot_names+count_vulnibm_sh_names))))+" % DE VULNERABILIDADES , EL NOMBRE INCLUYE BACKDOOR ")
print("            -    EN EL  "+str(float((((count_vulnibm_sh_namestealer+count_vulnibm_iot_namestealer)*100)/(count_vulnibm_iot_names+count_vulnibm_sh_names))))+" % DE VULNERABILIDADES , EL NOMBRE INCLUYE STEALER ")
print("            -    EN EL  "+str(float((((count_vulnibm_sh_namexploit+count_vulnibm_iot_namexploit)*100)/(count_vulnibm_iot_names+count_vulnibm_sh_names))))+" % DE VULNERABILIDADES , EL NOMBRE INCLUYE EXPLOIT")
print("            -    EN EL  "+str(float((((count_vulnibm_sh_namedenialofservice+count_vulnibm_iot_namedenialofservice)*100)/(count_vulnibm_iot_names+count_vulnibm_sh_names))))+" % DE VULNERABILIDADES , EL NOMBRE INCLUYE DENIAL OF SERVICE")
print("            -    EN EL  "+str(float((((count_vulnibm_sh_namebruteforce+count_vulnibm_iot_namebruteforce)*100)/(count_vulnibm_iot_names+count_vulnibm_sh_names))))+" % DE VULNERABILIDADES , EL NOMBRE INCLUYE BRUTE FORCE")
print("            -    EN EL  "+str(float((((count_vulnibm_sh_nameransomware+count_vulnibm_iot_nameransomware)*100)/(count_vulnibm_iot_names+count_vulnibm_sh_names))))+" % DE VULNERABILIDADES , EL NOMBRE INCLUYE RANSOMWARE ")
print("            -    EN EL  "+str(float((((count_vulnibm_sh_nametrojan+count_vulnibm_iot_nametrojan)*100)/(count_vulnibm_iot_names+count_vulnibm_sh_names))))+" % DE VULNERABILIDADES , EL NOMBRE INCLUYE TROJAN")
print("            -    EN EL  "+str(float((((count_vulnibm_sh_namesandbox+count_vulnibm_iot_namesandbox)*100)/(count_vulnibm_iot_names+count_vulnibm_sh_names))))+" % DE VULNERABILIDADES , EL NOMBRE INCLUYE SANDBOX")
print("            -    EN EL  "+str(float((((count_vulnibm_sh_nameworm+count_vulnibm_iot_nameworm)*100)/(count_vulnibm_iot_names+count_vulnibm_sh_names))))+" % DE VULNERABILIDADES , EL NOMBRE INCLUYE WORM ")
print("            -    EN EL  "+str(float((((count_vulnibm_sh_namespam+count_vulnibm_iot_namespam)*100)/(count_vulnibm_iot_names+count_vulnibm_sh_names))))+" % DE VULNERABILIDADES , EL NOMBRE INCLUYE SPAM")
print("            -    EN EL  "+str(float((((count_vulnibm_sh_namemalware+count_vulnibm_iot_namemalware)*100)/(count_vulnibm_iot_names+count_vulnibm_sh_names))))+" % DE VULNERABILIDADES , EL NOMBRE INCLUYE MALWARE")
print("            -    EN EL  "+str(float((((count_vulnibm_sh_namehijacking+count_vulnibm_iot_namehijacking)*100)/(count_vulnibm_iot_names+count_vulnibm_sh_names))))+" % DE VULNERABILIDADES , EL NOMBRE INCLUYE HIJACKING")
print("            -    EN EL  "+str(float((((count_vulnibm_sh_namesocialengineering+count_vulnibm_iot_namesocialengineering)*100)/(count_vulnibm_iot_names+count_vulnibm_sh_names))))+" % DE VULNERABILIDADES , EL NOMBRE INCLUYE SOCIAL ENGINEERING ")
print("            -    EN EL  "+str(float((((count_vulnibm_sh_nameloader+count_vulnibm_iot_nameloader)*100)/(count_vulnibm_iot_names+count_vulnibm_sh_names))))+" % DE VULNERABILIDADES , EL NOMBRE INCLUYE LOADER")
print("            -    EN EL  "+str(float((((count_vulnibm_sh_namespearphishing+count_vulnibm_iot_namespearphishing)*100)/(count_vulnibm_iot_names+count_vulnibm_sh_names))))+" % DE VULNERABILIDADES , EL NOMBRE INCLUYE SPEAR PHISHING")
print("            -    EN EL  "+str(float((((count_vulnibm_sh_namedropper+count_vulnibm_iot_namedropper)*100)/(count_vulnibm_iot_names+count_vulnibm_sh_names))))+" % DE VULNERABILIDADES , EL NOMBRE INCLUYE DROPPER")
print("            -    EN EL  "+str(float((((count_vulnibm_sh_namespyware+count_vulnibm_iot_namespyware)*100)/(count_vulnibm_iot_names+count_vulnibm_sh_names))))+" % DE VULNERABILIDADES , EL NOMBRE INCLUYE SPYWARE ")
print("            -    EN EL  "+str(float((((count_vulnibm_sh_namedownloader+count_vulnibm_iot_namedownloader)*100)/(count_vulnibm_iot_names+count_vulnibm_sh_names))))+" % DE VULNERABILIDADES , EL NOMBRE INCLUYE DOWNLOADER")
print("            -    EN EL  "+str(float((((count_vulnibm_sh_namedistribution+count_vulnibm_iot_namedistribution)*100)/(count_vulnibm_iot_names+count_vulnibm_sh_names))))+" % DE VULNERABILIDADES , EL NOMBRE INCLUYE DISTRIBUTION/DISTRIBUTED")
print("            -    EN EL  "+str(float((((count_vulnibm_sh_namexss+count_vulnibm_iot_namexss)*100)/(count_vulnibm_iot_names+count_vulnibm_sh_names))))+" % DE VULNERABILIDADES , EL NOMBRE INCLUYE CROSS SITE SCRIPTING")
print("            -    EN EL  "+str(float((((count_vulnibm_sh_namefraud+count_vulnibm_iot_namefraud)*100)/(count_vulnibm_iot_names+count_vulnibm_sh_names))))+" % DE VULNERABILIDADES , EL NOMBRE INCLUYE FRAUD ")
print("            -    EN EL  "+str(float((((count_vulnibm_sh_namebootkit+count_vulnibm_iot_namebootkit)*100)/(count_vulnibm_iot_names+count_vulnibm_sh_names))))+" % DE VULNERABILIDADES , EL NOMBRE INCLUYE BOOTKIT")
print("            -    EN EL  "+str(float((((count_vulnibm_sh_namehosting+count_vulnibm_iot_namehosting)*100)/(count_vulnibm_iot_names+count_vulnibm_sh_names))))+" % DE VULNERABILIDADES , EL NOMBRE INCLUYE HOSTING")
print("            -    EN EL  "+str(float((((count_vulnibm_sh_namebot+count_vulnibm_iot_namebot)*100)/(count_vulnibm_iot_names+count_vulnibm_sh_names))))+" % DE VULNERABILIDADES , EL NOMBRE INCLUYE BOT")
print("            -    EN EL  "+str(float((((count_vulnibm_sh_nameinjection+count_vulnibm_iot_nameinjection)*100)/(count_vulnibm_iot_names+count_vulnibm_sh_names))))+" % DE VULNERABILIDADES , EL NOMBRE INCLUYE INJECTION ")
print("            -    EN EL  "+str(float((((count_vulnibm_sh_nameinfection+count_vulnibm_iot_nameinfection)*100)/(count_vulnibm_iot_names+count_vulnibm_sh_names))))+" % DE VULNERABILIDADES , EL NOMBRE INCLUYE INFECTION")
print("            -    EN EL  "+str(float((((count_vulnibm_sh_nameimpersonate+count_vulnibm_iot_nameimpersonate)*100)/(count_vulnibm_iot_names+count_vulnibm_sh_names))))+" % DE VULNERABILIDADES , EL NOMBRE INCLUYE IMPERSONATION")
print("            -    EN EL  "+str(float((((count_vulnibm_sh_namechain+count_vulnibm_iot_namechain)*100)/(count_vulnibm_iot_names+count_vulnibm_sh_names))))+" % DE VULNERABILIDADES , EL NOMBRE INCLUYE CHAIN")
print("            -    EN EL  "+str(float((((count_vulnibm_sh_namespionage+count_vulnibm_iot_namespionage)*100)/(count_vulnibm_iot_names+count_vulnibm_sh_names))))+" % DE VULNERABILIDADES , EL NOMBRE INCLUYE ESPIONAGE")
print("            -    EN EL  "+str(float((((count_vulnibm_sh_namexfiltration+count_vulnibm_iot_namexfiltration)*100)/(count_vulnibm_iot_names+count_vulnibm_sh_names))))+" % DE VULNERABILIDADES , EL NOMBRE INCLUYE EXFILTRATION")
print("            -    EN EL  "+str(float((((count_vulnibm_sh_namemasquerade+count_vulnibm_iot_namemasquerade)*100)/(count_vulnibm_iot_names+count_vulnibm_sh_names))))+" % DE VULNERABILIDADES , EL NOMBRE INCLUYE MASQUERADE")
print("            -    EN EL  "+str(float((((count_vulnibm_sh_namecontrol+count_vulnibm_iot_namecontrol)*100)/(count_vulnibm_iot_names+count_vulnibm_sh_names))))+" % DE VULNERABILIDADES , EL NOMBRE INCLUYE CONTROL")
print("            -    EN EL  "+str(float((((count_vulnibm_sh_namecryptojack+count_vulnibm_iot_namecryptojack)*100)/(count_vulnibm_iot_names+count_vulnibm_sh_names))))+" % DE VULNERABILIDADES , EL NOMBRE INCLUYE CRYPTOJACK")
print("            -    EN EL  "+str(float((((count_vulnibm_sh_nameremote+count_vulnibm_iot_nameremote)*100)/(count_vulnibm_iot_names+count_vulnibm_sh_names))))+" % DE VULNERABILIDADES , EL NOMBRE INCLUYE REMOTE")
print("            -    EN EL  "+str(float((((count_vulnibm_sh_nameanother+count_vulnibm_iot_nameanother)*100)/(count_vulnibm_iot_names+count_vulnibm_sh_names))))+" % DE VULNERABILIDADES , EL NOMBRE INCLUYE UNA CADENA DISTINTA")
print("\n")
              