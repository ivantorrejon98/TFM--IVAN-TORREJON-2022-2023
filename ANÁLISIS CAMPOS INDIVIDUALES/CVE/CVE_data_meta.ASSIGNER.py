#*******************************************************ASIGNADOR CVE****************************************************************


import pandas as pd

#Abro los ficheros con los que voy a tratar


df_cve_iot=pd.read_excel('cves_iot_2023.xlsx')
df_cve_sh=pd.read_excel('cves_smart_home_2023.xlsx')


#Variables donde almacenare el contador de ASIGNADOR CVE para la parte de IOT
jpcert_iot=0
mitre_iot=0
cisco_iot=0
github_iot=0
redhat_iot=0
qualcomm_iot=0
apache_iot=0
oracle_iot=0
microsoft_iot=0
cert_iot=0
trendmicro_iot=0
nozomi_iot=0
hq_iot=0
kaspersky_iot=0
schneider_iot=0
apple_iot=0
android_iot=0
bitdefender_iot=0
mcafee_iot=0
mozilla_iot=0
hpe_iot=0
fsecure_iot=0
rapid7_iot=0
other_assigner_iot=0




#Recorro los valores de ASIGNADOR CVE para la parte IOT

for j in range(0,len(df_cve_iot["CVE_Items.cve.CVE_data_meta.ASSIGNER"])):
    if("jpcert" in df_cve_iot["CVE_Items.cve.CVE_data_meta.ASSIGNER"][j]):
        jpcert_iot+=1
    elif("@mitre" in df_cve_iot["CVE_Items.cve.CVE_data_meta.ASSIGNER"][j]):
        mitre_iot+=1
    elif("@cisco" in df_cve_iot["CVE_Items.cve.CVE_data_meta.ASSIGNER"][j]):
        cisco_iot+=1
    elif("@github" in df_cve_iot["CVE_Items.cve.CVE_data_meta.ASSIGNER"][j]):
        github_iot+=1
    elif("@redhat" in df_cve_iot["CVE_Items.cve.CVE_data_meta.ASSIGNER"][j]):
        redhat_iot+=1
    elif("@qualcomm" in df_cve_iot["CVE_Items.cve.CVE_data_meta.ASSIGNER"][j]):
        qualcomm_iot+=1
    elif("@apache" in df_cve_iot["CVE_Items.cve.CVE_data_meta.ASSIGNER"][j]):
        apache_iot+=1
    elif("@oracle" in df_cve_iot["CVE_Items.cve.CVE_data_meta.ASSIGNER"][j]):
        oracle_iot+=1
    elif("@microsoft" in df_cve_iot["CVE_Items.cve.CVE_data_meta.ASSIGNER"][j]):
        microsoft_iot+=1
    elif("@cert" in df_cve_iot["CVE_Items.cve.CVE_data_meta.ASSIGNER"][j]):
        cert_iot+=1
    elif("@trendmicro" in df_cve_iot["CVE_Items.cve.CVE_data_meta.ASSIGNER"][j]):
        trendmicro_iot+=1
    elif("@nozomi" in df_cve_iot["CVE_Items.cve.CVE_data_meta.ASSIGNER"][j]):
        nozomi_iot+=1
    elif("@hq" in df_cve_iot["CVE_Items.cve.CVE_data_meta.ASSIGNER"][j]):
        hq_iot+=1
    elif("@kaspersky" in df_cve_iot["CVE_Items.cve.CVE_data_meta.ASSIGNER"][j]):
        kaspersky_iot+=1
    elif("@schneider" in df_cve_iot["CVE_Items.cve.CVE_data_meta.ASSIGNER"][j]):
        schneider_iot+=1 
    elif("@apple" in df_cve_iot["CVE_Items.cve.CVE_data_meta.ASSIGNER"][j]):
        apple_iot+=1
    elif("@android" in df_cve_iot["CVE_Items.cve.CVE_data_meta.ASSIGNER"][j]):
        android_iot+=1
    elif("@bitdefender" in df_cve_iot["CVE_Items.cve.CVE_data_meta.ASSIGNER"][j]):
        bitdefender_iot+=1 
    elif("@mcafee" in df_cve_iot["CVE_Items.cve.CVE_data_meta.ASSIGNER"][j]):
        mcafee_iot+=1  
    elif("@mozilla" in df_cve_iot["CVE_Items.cve.CVE_data_meta.ASSIGNER"][j]):
        mozilla_iot+=1
    elif("@hpe" in df_cve_iot["CVE_Items.cve.CVE_data_meta.ASSIGNER"][j]):
        hpe_iot+=1 
    elif("@f-secure" in df_cve_iot["CVE_Items.cve.CVE_data_meta.ASSIGNER"][j]):
        fsecure_iot+=1 
    elif("@rapid7" in df_cve_iot["CVE_Items.cve.CVE_data_meta.ASSIGNER"][j]):
        rapid7_iot+=1  
    else:
        other_assigner_iot+=1
    

print("**************************ESTADÍSTICAS ASIGNADOR CVE IOT********************************")
print("\n")
print("DE UN TOTAL DE "+str(len(df_cve_iot["CVE_Items.cve.CVE_data_meta.ASSIGNER"]))+" VULNERABILIDADES, LAS ESTADÍSTICAS DE ASIGNADOR CVE SON LAS SIGUIENTES : ")
print("\n")
print("     -    EN "+str(jpcert_iot)+" VULNERABILIDADES EL ASIGNADOR DE LA CVE ES VULTURES@JPCERT \n")
print("     -    EN "+str(mitre_iot)+" VULNERABILIDADES EL ASIGNADOR DE LA CVE ES CVE@MITRE \n")
print("     -    EN "+str(cisco_iot)+" VULNERABILIDADES EL ASIGNADOR DE LA CVE ES TALOS-CNA@CISCO \n")
print("     -    EN "+str(github_iot)+" VULNERABILIDADES EL ASIGNADOR DE LA CVE ES SECURITY-ADVISORIES@GITHUB \n")
print("     -    EN "+str(redhat_iot)+" VULNERABILIDADES EL ASIGNADOR DE LA CVE ES SECALERT@REDHAT \n")
print("     -    EN "+str(qualcomm_iot)+" VULNERABILIDADES EL ASIGNADOR DE LA CVE ES SECURITY.CNA@QUALCOMM \n")
print("     -    EN "+str(apache_iot)+" VULNERABILIDADES EL ASIGNADOR DE LA CVE ES SECURITY@APACHE.ORG \n")
print("     -    EN "+str(oracle_iot)+" VULNERABILIDADES EL ASIGNADOR DE LA CVE ES SECALERT_US@ORACLE \n")
print("     -    EN "+str(microsoft_iot)+" VULNERABILIDADES EL ASIGNADOR DE LA CVE ES SECURE@MICROSOFT \n")
print("     -    EN "+str(cert_iot)+" VULNERABILIDADES EL ASIGNADOR DE LA CVE ES INFO@CERT.VDE \n")
print("     -    EN "+str(trendmicro_iot)+" VULNERABILIDADES EL ASIGNADOR DE LA CVE ES SECURITY@TRENDMICRO \n")
print("     -    EN "+str(nozomi_iot)+" VULNERABILIDADES EL ASIGNADOR DE LA CVE ES PRODSEC@NOZOMINETWORKS \n")
print("     -    EN "+str(hq_iot)+" VULNERABILIDADES EL ASIGNADOR DE LA CVE ES ICS-CERT@HQ.DHS.GOV \n")
print("     -    EN "+str(kaspersky_iot)+" VULNERABILIDADES EL ASIGNADOR DE LA CVE ES VULNERABILITY@KASPERSKY \n")
print("     -    EN "+str(schneider_iot)+" VULNERABILIDADES EL ASIGNADOR DE LA CVE ES CYBERSECURITY@SCHNEIDER-ELECTRIC \n")
print("     -    EN "+str(apple_iot)+" VULNERABILIDADES EL ASIGNADOR DE LA CVE ES PRODUCT-SECURITY@APPLE \n")
print("     -    EN "+str(android_iot)+" VULNERABILIDADES EL ASIGNADOR DE LA CVE ES SECURITY@ANDROID \n")
print("     -    EN "+str(bitdefender_iot)+" VULNERABILIDADES EL ASIGNADOR DE LA CVE ES CVE-REQUESTS@BITDEFENDER \n")
print("     -    EN "+str(mcafee_iot)+" VULNERABILIDADES EL ASIGNADOR DE LA CVE ES PSIRT@MCAFEE \n")
print("     -    EN "+str(mozilla_iot)+" VULNERABILIDADES EL ASIGNADOR DE LA CVE ES SECURITY@MOZILLA \n")
print("     -    EN "+str(hpe_iot)+" VULNERABILIDADES EL ASIGNADOR DE LA CVE ES SECURITY-ALERT@HPE \n")
print("     -    EN "+str(fsecure_iot)+" VULNERABILIDADES EL ASIGNADOR DE LA CVE ES CVE-NOTIFICATIONS-US@F-SECURE \n")
print("     -    EN "+str(rapid7_iot)+" VULNERABILIDADES EL ASIGNADOR DE LA CVE ES CVE@RAPID7 \n")
print("     -    EN "+str(other_assigner_iot)+" VULNERABILIDADES EL ASIGNADOR DE LA CVE ES DISTINTO DE LOS ANTERIORES \n")





print("************************** PORCENTAJES ASIGNADOR CVE IOT********************************")
print("\n")
print("DE UN TOTAL DE "+str(len(df_cve_iot["CVE_Items.cve.CVE_data_meta.ASSIGNER"]))+" VULNERABILIDADES, LOS PORCENTAJES DE ASIGNADOR CVE SON LOS SIGUIENTES : ")
print("\n")
print("    -    EN EL "+str(float(((jpcert_iot*100)/len(df_cve_iot["CVE_Items.cve.CVE_data_meta.ASSIGNER"]))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE LA CVE ES VULTURES@JPCERT \n")
print("    -    EN EL "+str(float(((mitre_iot*100)/len(df_cve_iot["CVE_Items.cve.CVE_data_meta.ASSIGNER"]))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE LA CVE ES CVE@MITRE \n")
print("    -    EN EL "+str(float(((cisco_iot*100)/len(df_cve_iot["CVE_Items.cve.CVE_data_meta.ASSIGNER"]))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE LA CVE ES TALOS-CNA@CISCO \n")
print("    -    EN EL "+str(float(((github_iot*100)/len(df_cve_iot["CVE_Items.cve.CVE_data_meta.ASSIGNER"]))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE LA CVE ES SECURITY-ADVISORIES@GITHUB \n")
print("    -    EN EL "+str(float(((redhat_iot*100)/len(df_cve_iot["CVE_Items.cve.CVE_data_meta.ASSIGNER"]))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE LA CVE ES SECALERT@REDHAT\n")
print("    -    EN EL "+str(float(((qualcomm_iot*100)/len(df_cve_iot["CVE_Items.cve.CVE_data_meta.ASSIGNER"]))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE LA CVE ES SECURITY.CNA@QUALCOMM \n")
print("    -    EN EL "+str(float(((apache_iot*100)/len(df_cve_iot["CVE_Items.cve.CVE_data_meta.ASSIGNER"]))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE LA CVE ES SECURITY@APACHE.ORG \n")
print("    -    EN EL "+str(float(((oracle_iot*100)/len(df_cve_iot["CVE_Items.cve.CVE_data_meta.ASSIGNER"]))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE LA CVE ES SECALERT_US@ORACLE \n")
print("    -    EN EL "+str(float(((microsoft_iot*100)/len(df_cve_iot["CVE_Items.cve.CVE_data_meta.ASSIGNER"]))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE LA CVE ES SECURE@MICROSOFT \n")
print("    -    EN EL "+str(float(((cert_iot*100)/len(df_cve_iot["CVE_Items.cve.CVE_data_meta.ASSIGNER"]))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE LA CVE ES INFO@CERT.VDE \n")
print("    -    EN EL "+str(float(((trendmicro_iot*100)/len(df_cve_iot["CVE_Items.cve.CVE_data_meta.ASSIGNER"]))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE LA CVE ES SECURITY@TRENDMICRO \n")
print("    -    EN EL "+str(float(((nozomi_iot*100)/len(df_cve_iot["CVE_Items.cve.CVE_data_meta.ASSIGNER"]))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE LA CVE ES PRODSEC@NOZOMINETWORKS \n")
print("    -    EN EL "+str(float(((hq_iot*100)/len(df_cve_iot["CVE_Items.cve.CVE_data_meta.ASSIGNER"]))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE LA CVE ES ICS-CERT@HQ.DHS.GOV \n")
print("    -    EN EL "+str(float(((kaspersky_iot*100)/len(df_cve_iot["CVE_Items.cve.CVE_data_meta.ASSIGNER"]))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE LA CVE ES VULNERABILITY@KASPERSKY \n")
print("    -    EN EL "+str(float(((schneider_iot*100)/len(df_cve_iot["CVE_Items.cve.CVE_data_meta.ASSIGNER"]))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE LA CVE ES CYBERSECURITY@SCHNEIDER-ELECTRIC \n")
print("    -    EN EL "+str(float(((apple_iot*100)/len(df_cve_iot["CVE_Items.cve.CVE_data_meta.ASSIGNER"]))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE LA CVE ES PRODUCT-SECURITY@APPLE \n")
print("    -    EN EL "+str(float(((android_iot*100)/len(df_cve_iot["CVE_Items.cve.CVE_data_meta.ASSIGNER"]))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE LA CVE ES SECURITY@ANDROID \n")
print("    -    EN EL "+str(float(((bitdefender_iot*100)/len(df_cve_iot["CVE_Items.cve.CVE_data_meta.ASSIGNER"]))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE LA CVE ES CVE-REQUESTS@BITDEFENDER \n")
print("    -    EN EL "+str(float(((mcafee_iot*100)/len(df_cve_iot["CVE_Items.cve.CVE_data_meta.ASSIGNER"]))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE LA CVE ES PSIRT@MCAFEE \n")
print("    -    EN EL "+str(float(((mozilla_iot*100)/len(df_cve_iot["CVE_Items.cve.CVE_data_meta.ASSIGNER"]))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE LA CVE ES SECURITY@MOZILLA \n")
print("    -    EN EL "+str(float(((hpe_iot*100)/len(df_cve_iot["CVE_Items.cve.CVE_data_meta.ASSIGNER"]))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE LA CVE ES SECURITY-ALERT@HPE \n")
print("    -    EN EL "+str(float(((fsecure_iot*100)/len(df_cve_iot["CVE_Items.cve.CVE_data_meta.ASSIGNER"]))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE LA CVE ES FSECURE \n")
print("    -    EN EL "+str(float(((rapid7_iot*100)/len(df_cve_iot["CVE_Items.cve.CVE_data_meta.ASSIGNER"]))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE LA CVE ES CVE@RAPID7 \n")
print("    -    EN EL "+str(float(((other_assigner_iot*100)/len(df_cve_iot["CVE_Items.cve.CVE_data_meta.ASSIGNER"]))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE LA CVE ES DISTINTO A LOS ANTERIORES \n")
print("\n")
print("\n") 


#Variables donde almacenare el contador de ASIGNADOR CVE para la parte de SMART HOME
jpcert_sh=0
mitre_sh=0
cisco_sh=0
github_sh=0
cert_sh=0
hq_sh=0
kaspersky_sh=0
mcafee_sh=0
hpe_sh=0
rapid7_sh=0
bosch_sh=0
synopsys_sh=0
other_assigner_sh=0




#Recorro los valores de ASIGNADOR CVE para la parte SMART HOME

for j in range(0,len(df_cve_sh["CVE_Items.cve.CVE_data_meta.ASSIGNER"])):
    if("jpcert" in df_cve_sh["CVE_Items.cve.CVE_data_meta.ASSIGNER"][j]):
        jpcert_sh+=1
    elif("@mitre" in df_cve_sh["CVE_Items.cve.CVE_data_meta.ASSIGNER"][j]):
        mitre_sh+=1
    elif("@cisco" in df_cve_sh["CVE_Items.cve.CVE_data_meta.ASSIGNER"][j]):
        cisco_sh+=1
    elif("@github" in df_cve_sh["CVE_Items.cve.CVE_data_meta.ASSIGNER"][j]):
        github_sh+=1
    elif("@cert" in df_cve_sh["CVE_Items.cve.CVE_data_meta.ASSIGNER"][j]):
        cert_sh+=1
    elif("@hq" in df_cve_sh["CVE_Items.cve.CVE_data_meta.ASSIGNER"][j]):
        hq_sh+=1
    elif("@kaspersky" in df_cve_sh["CVE_Items.cve.CVE_data_meta.ASSIGNER"][j]):
        kaspersky_sh+=1
    elif("@mcafee" in df_cve_sh["CVE_Items.cve.CVE_data_meta.ASSIGNER"][j]):
        mcafee_sh+=1  
    elif("@hpe" in df_cve_sh["CVE_Items.cve.CVE_data_meta.ASSIGNER"][j]):
        hpe_sh+=1 
    elif("@rapid7" in df_cve_sh["CVE_Items.cve.CVE_data_meta.ASSIGNER"][j]):
        rapid7_sh+=1
    elif("@bosch" in df_cve_sh["CVE_Items.cve.CVE_data_meta.ASSIGNER"][j]):
        bosch_sh+=1  
    elif("@synopsys" in df_cve_sh["CVE_Items.cve.CVE_data_meta.ASSIGNER"][j]):
        synopsys_sh+=1   
    else:
        other_assigner_sh+=1
    

print("**************************ESTADÍSTICAS ASIGNADOR CVE SMART HOME********************************")
print("\n")
print("DE UN TOTAL DE "+str(len(df_cve_sh["CVE_Items.cve.CVE_data_meta.ASSIGNER"]))+" VULNERABILIDADES, LAS ESTADÍSTICAS DE ASIGNADOR CVE SON LAS SIGUIENTES : ")
print("\n")            
print("     -    EN "+str(jpcert_sh)+" VULNERABILIDADES EL ASIGNADOR DE LA CVE ES VULTURES@JPCERT \n")
print("     -    EN "+str(mitre_sh)+" VULNERABILIDADES EL ASIGNADOR DE LA CVE ES CVE@MITRE \n")
print("     -    EN "+str(cisco_sh)+" VULNERABILIDADES EL ASIGNADOR DE LA CVE ES TALOS-CNA/PSIRT@CISCO \n")
print("     -    EN "+str(github_sh)+" VULNERABILIDADES EL ASIGNADOR DE LA CVE ES SECURITY-ADVISORIES@GITHUB \n")
print("     -    EN "+str(cert_sh)+" VULNERABILIDADES EL ASIGNADOR DE LA CVE ES INFO@CERT.VDE \n")
print("     -    EN "+str(hq_sh)+" VULNERABILIDADES EL ASIGNADOR DE LA CVE ES ICS-CERT@HQ.DHS.GOV \n")
print("     -    EN "+str(kaspersky_sh)+" VULNERABILIDADES EL ASIGNADOR DE LA CVE ES VULNERABILITY@KASPERSKY \n")
print("     -    EN "+str(mcafee_sh)+" VULNERABILIDADES EL ASIGNADOR DE LA CVE ES PSIRT@MCAFEE \n")
print("     -    EN "+str(hpe_sh)+" VULNERABILIDADES EL ASIGNADOR DE LA CVE ES SECURITY-ALERT@HPE \n")
print("     -    EN "+str(rapid7_sh)+" VULNERABILIDADES EL ASIGNADOR DE LA CVE ES CVE@RAPID7 \n")
print("     -    EN "+str(bosch_sh)+" VULNERABILIDADES EL ASIGNADOR DE LA CVE ES PSIRT@BOSCH \n")
print("     -    EN "+str(synopsys_sh)+" VULNERABILIDADES EL ASIGNADOR DE LA CVE ES DISCLOSURE@SYNOPSYS \n")
print("     -    EN "+str(other_assigner_sh)+" VULNERABILIDADES EL ASIGNADOR DE LA CVE ES DISTINTO DE LOS ANTERIORES \n")









print("************************** PORCENTAJE ASIGNADOR CVE SMART HOME********************************")
print("\n")
print("DE UN TOTAL DE "+str(len(df_cve_sh["CVE_Items.cve.CVE_data_meta.ASSIGNER"]))+" VULNERABILIDADES, LOS PORCENTAJES DE ASIGNADOR CVE SON LOS SIGUIENTES : ")
print("\n")
print("    -    EN EL "+str(float(((jpcert_sh*100)/len(df_cve_sh["CVE_Items.cve.CVE_data_meta.ASSIGNER"]))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE LA CVE ES VULTURES@JPCERT.OR.JP \n")
print("    -    EN EL "+str(float(((mitre_sh*100)/len(df_cve_sh["CVE_Items.cve.CVE_data_meta.ASSIGNER"]))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE LA CVE ES CVE@MITRE \n")
print("    -    EN EL "+str(float(((cisco_sh*100)/len(df_cve_sh["CVE_Items.cve.CVE_data_meta.ASSIGNER"]))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE LA CVE ES TALOS-CNA@CISCO \n")
print("    -    EN EL "+str(float(((github_sh*100)/len(df_cve_sh["CVE_Items.cve.CVE_data_meta.ASSIGNER"]))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE LA CVE ES SECURITY-ADVISORIES@GITHUB \n")
print("    -    EN EL "+str(float(((cert_sh*100)/len(df_cve_sh["CVE_Items.cve.CVE_data_meta.ASSIGNER"]))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE LA CVE ES INFO@CERT.VDE \n")
print("    -    EN EL "+str(float(((hq_sh*100)/len(df_cve_sh["CVE_Items.cve.CVE_data_meta.ASSIGNER"]))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE LA CVE ES ICS-CERT@HQ.DHS.GOV \n")
print("    -    EN EL "+str(float(((kaspersky_sh*100)/len(df_cve_sh["CVE_Items.cve.CVE_data_meta.ASSIGNER"]))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE LA CVE ES VULNERABILITY@KASPERSKY \n")
print("    -    EN EL "+str(float(((mcafee_sh*100)/len(df_cve_sh["CVE_Items.cve.CVE_data_meta.ASSIGNER"]))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE LA CVE ES PSIRT@MCAFEE \n")
print("    -    EN EL "+str(float(((hpe_sh*100)/len(df_cve_sh["CVE_Items.cve.CVE_data_meta.ASSIGNER"]))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE LA CVE ES SECURITY-ALERT@HPE \n")
print("    -    EN EL "+str(float(((rapid7_sh*100)/len(df_cve_sh["CVE_Items.cve.CVE_data_meta.ASSIGNER"]))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE LA CVE ES CVE@RAPID7 \n")
print("    -    EN EL "+str(float(((bosch_sh*100)/len(df_cve_sh["CVE_Items.cve.CVE_data_meta.ASSIGNER"]))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE LA CVE ES PSIRT@BOSCH \n")
print("    -    EN EL "+str(float(((synopsys_sh*100)/len(df_cve_sh["CVE_Items.cve.CVE_data_meta.ASSIGNER"]))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE LA CVE ES DISCLOSURE@SYNOPSYS \n")
print("    -    EN EL "+str(float(((other_assigner_sh*100)/len(df_cve_sh["CVE_Items.cve.CVE_data_meta.ASSIGNER"]))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE LA CVE ES DISTINTO A LOS ANTERIORES \n")
print("\n")
print("\n")


print("************************** ESTADÍSTICAS ASIGNADOR CVES COMUNES IOT Y SMART HOME ********************************")
print("\n")
print("\n")
print("DE UN TOTAL DE "+str(len(df_cve_iot["CVE_Items.cve.CVE_data_meta.ASSIGNER"])+len(df_cve_sh["CVE_Items.cve.CVE_data_meta.ASSIGNER"]))+" VULNERABILIDADES, LAS ESTADÍSTICAS DE ASIGNADOR CVES COMUNES ENTRE LA PARTE DE IOT Y SMART HOME SON LAS SIGUIENTES : ")
print("\n")
print("    -    EN "+str(jpcert_iot+jpcert_sh)+" VULNERABILIDADES EL ASIGNADOR DE LA CVE ES VULTURES@JPCERT.OR.JP \n")
print("    -    EN "+str(mitre_sh+mitre_iot)+" VULNERABILIDADES EL ASIGNADOR DE LA CVE ES CVE@MITRE \n")
print("    -    EN "+str(cisco_sh+cisco_iot)+" VULNERABILIDADES EL ASIGNADOR DE LA CVE ES TALOS-CNA@CISCO \n")
print("    -    EN "+str(github_sh+github_iot)+" VULNERABILIDADES EL ASIGNADOR DE LA CVE ES SECURITY-ADVISORIES@GITHUB \n")
print("    -    EN "+str(cert_iot+cert_sh)+" VULNERABILIDADES EL ASIGNADOR DE LA CVE ES INFO@CERT.VDE \n")
print("    -    EN "+str(hq_iot+hq_sh)+" VULNERABILIDADES EL ASIGNADOR DE LA CVE ES ICS-CERT@HQ.DHS.GOV \n")
print("    -    EN "+str(kaspersky_iot+kaspersky_sh)+" VULNERABILIDADES EL ASIGNADOR DE LA CVE ES VULNERABILITY@KASPERSKY \n")
print("    -    EN "+str(mcafee_sh+mcafee_iot)+" VULNERABILIDADES EL ASIGNADOR DE LA CVE ES PSIRT@MCAFEE \n")
print("    -    EN "+str(hpe_sh+hpe_iot)+" VULNERABILIDADES EL ASIGNADOR DE LA CVE ES SECURITY-ALERT@HPE \n")
print("    -    EN "+str(rapid7_sh+rapid7_iot)+" VULNERABILIDADES EL ASIGNADOR DE LA CVE ES CVE@RAPID7 \n")
print("\n")


print("************************** ESTADÍSTICAS ASIGNADORES CVES NO COMUNES IOT Y SMART HOME ********************************")
print("\n")
print("\n")
print("DE UN TOTAL DE "+str(len(df_cve_iot["CVE_Items.cve.CVE_data_meta.ASSIGNER"])+len(df_cve_sh["CVE_Items.cve.CVE_data_meta.ASSIGNER"]))+" VULNERABILIDADES, LOS PORCENTAJES DE ASIGNADOR CVES NO COMUNES ENTRE LA PARTE DE IOT Y SMART HOME SON LOS SIGUIENTES : ")
print("\n")
print("    -    EN  "+str(bosch_sh)+" VULNERABILIDADES EL ASIGNADOR DE LA CVE ES PSIRT@BOSCH \n")
print("    -    EN  "+str(synopsys_sh)+" VULNERABILIDADES EL ASIGNADOR DE LA CVE ES SYNOPSIS \n")
print("    -    EN  "+str(redhat_iot)+" VULNERABILIDADES EL ASIGNADOR DE LA CVE ES SECALERT@REDHAT \n")
print("    -    EN  "+str(qualcomm_iot)+" VULNERABILIDADES EL ASIGNADOR DE LA CVE ES SECURITY.CNA@QUALCOMM \n")
print("    -    EN  "+str(apache_iot)+" VULNERABILIDADES EL ASIGNADOR DE LA CVE ES SECURITY@APACHE.ORG \n")
print("    -    EN  "+str(oracle_iot)+" VULNERABILIDADES EL ASIGNADOR DE LA CVE ES SECALERT_US@ORACLE \n")
print("    -    EN  "+str(microsoft_iot)+" VULNERABILIDADES EL ASIGNADOR DE LA CVE ES SECURE@MICROSOFT \n")
print("    -    EN  "+str(trendmicro_iot)+" VULNERABILIDADES EL ASIGNADOR DE LA CVE ES SECURITY@TRENDMICRO \n")
print("    -    EN  "+str(nozomi_iot)+" VULNERABILIDADES EL ASIGNADOR DE LA CVE ES PRODSEC@NOZOMINETWORKS \n")
print("    -    EN  "+str(schneider_iot)+" VULNERABILIDADES EL ASIGNADOR DE LA CVE ES CYBERSECURITY@SCHNEIDER-ELECTRIC \n")
print("    -    EN  "+str(apple_iot)+" VULNERABILIDADES EL ASIGNADOR DE LA CVE ES PRODUCT-SECURITY@APPLE \n")
print("    -    EN  "+str(android_iot)+" VULNERABILIDADES EL ASIGNADOR DE LA CVE ES SECURITY@ANDROID \n")
print("    -    EN  "+str(bitdefender_iot)+" VULNERABILIDADES EL ASIGNADOR DE LA CVE ES CVE-REQUESTS@BITDEFENDER \n")
print("    -    EN  "+str(mozilla_iot)+" VULNERABILIDADES EL ASIGNADOR DE LA CVE ES SECURITY@MOZILLA \n")
print("    -    EN  "+str(fsecure_iot)+" VULNERABILIDADES EL ASIGNADOR DE LA CVE ES FSECURE \n")
print("    -    EN  "+str(other_assigner_sh+other_assigner_iot)+" VULNERABILIDADES EL ASIGNADOR DE LA CVE ES DISTINTO A LOS ANTERIORES \n")



print("************************** PORCENTAJES ASIGNADORES CVES COMUNES IOT Y SMART HOME ********************************")
print("\n")
print("\n")
print("DE UN TOTAL DE "+str(len(df_cve_iot["CVE_Items.cve.CVE_data_meta.ASSIGNER"])+len(df_cve_sh["CVE_Items.cve.CVE_data_meta.ASSIGNER"]))+" VULNERABILIDADES, LOS PORCENTAJES DE ASIGNADOR CVES COMUNES ENTRE LA PARTE DE IOT Y SMART HOME SON LOS SIGUIENTES : ")
print("\n")
print("    -    EN EL "+str(float((((jpcert_iot+jpcert_sh)*100)/(len(df_cve_iot["CVE_Items.cve.CVE_data_meta.ASSIGNER"])+len(df_cve_sh["CVE_Items.cve.CVE_data_meta.ASSIGNER"])))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE LA CVE ES VULTURES@JPCERT.OR.JP \n")
print("    -    EN EL "+str(float((((mitre_sh+mitre_iot)*100)/(len(df_cve_iot["CVE_Items.cve.CVE_data_meta.ASSIGNER"])+len(df_cve_sh["CVE_Items.cve.CVE_data_meta.ASSIGNER"])))))+"  % DE LAS VULNERABILIDADES EL ASIGNADOR DE LA CVE ES CVE@MITRE \n")
print("    -    EN EL "+str(float((((cisco_sh+cisco_iot)*100)/(len(df_cve_iot["CVE_Items.cve.CVE_data_meta.ASSIGNER"])+len(df_cve_sh["CVE_Items.cve.CVE_data_meta.ASSIGNER"])))))+"  % DE LAS VULNERABILIDADES EL ASIGNADOR DE LA CVE ES TALOS-CNA@CISCO \n")
print("    -    EN EL "+str(float((((github_sh+github_iot)*100)/(len(df_cve_iot["CVE_Items.cve.CVE_data_meta.ASSIGNER"])+len(df_cve_sh["CVE_Items.cve.CVE_data_meta.ASSIGNER"])))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE LA CVE ES SECURITY-ADVISORIES@GITHUB \n")
print("    -    EN EL "+str(float((((cert_iot+cert_sh)*100)/(len(df_cve_iot["CVE_Items.cve.CVE_data_meta.ASSIGNER"])+len(df_cve_sh["CVE_Items.cve.CVE_data_meta.ASSIGNER"])))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE LA CVE ES INFO@CERT.VDE \n")
print("    -    EN EL "+str(float((((hq_iot+hq_sh)*100)/(len(df_cve_iot["CVE_Items.cve.CVE_data_meta.ASSIGNER"])+len(df_cve_sh["CVE_Items.cve.CVE_data_meta.ASSIGNER"])))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE LA CVE ES ICS-CERT@HQ.DHS.GOV \n")
print("    -    EN EL "+str(float((((kaspersky_iot+kaspersky_sh)*100)/(len(df_cve_iot["CVE_Items.cve.CVE_data_meta.ASSIGNER"])+len(df_cve_sh["CVE_Items.cve.CVE_data_meta.ASSIGNER"])))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE LA CVE ES VULNERABILITY@KASPERSKY \n")
print("    -    EN EL "+str(float((((mcafee_sh+mcafee_iot)*100)/(len(df_cve_iot["CVE_Items.cve.CVE_data_meta.ASSIGNER"])+len(df_cve_sh["CVE_Items.cve.CVE_data_meta.ASSIGNER"])))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE LA CVE ES PSIRT@MCAFEE \n")
print("    -    EN EL "+str(float((((hpe_sh+hpe_iot)*100)/(len(df_cve_iot["CVE_Items.cve.CVE_data_meta.ASSIGNER"])+len(df_cve_sh["CVE_Items.cve.CVE_data_meta.ASSIGNER"])))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE LA CVE ES SECURITY-ALERT@HPE \n")
print("    -    EN EL "+str(float((((rapid7_sh+rapid7_iot)*100)/(len(df_cve_iot["CVE_Items.cve.CVE_data_meta.ASSIGNER"])+len(df_cve_sh["CVE_Items.cve.CVE_data_meta.ASSIGNER"])))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE LA CVE ES CVE@RAPID7 \n")
print("\n")
print("************************** PORCENTAJES ASIGNADORES CVE NO COMUNES IOT Y SMART HOME ********************************")
print("\n")
print("\n")
print("DE UN TOTAL DE "+str(len(df_cve_iot["CVE_Items.cve.CVE_data_meta.ASSIGNER"])+len(df_cve_sh["CVE_Items.cve.CVE_data_meta.ASSIGNER"]))+" VULNERABILIDADES, LOS PORCENTAJES DE ASIGNADOR CVES NO COMUNES ENTRE LA PARTE DE IOT Y SMART HOME SON LOS SIGUIENTES : ")
print("\n")
print("    -    EN EL "+str(float((((bosch_sh)*100)/(len(df_cve_iot["CVE_Items.cve.CVE_data_meta.ASSIGNER"])+len(df_cve_sh["CVE_Items.cve.CVE_data_meta.ASSIGNER"])))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE LA CVE ES PSIRT@BOSCH \n")
print("    -    EN EL "+str(float((((synopsys_sh)*100)/(len(df_cve_iot["CVE_Items.cve.CVE_data_meta.ASSIGNER"])+len(df_cve_sh["CVE_Items.cve.CVE_data_meta.ASSIGNER"])))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE LA CVE ES SYNOPSIS \n")
print("    -    EN EL "+str(float((((redhat_iot)*100)/(len(df_cve_iot["CVE_Items.cve.CVE_data_meta.ASSIGNER"])+len(df_cve_sh["CVE_Items.cve.CVE_data_meta.ASSIGNER"])))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE LA CVE ES SECALERT@REDHAT \n")
print("    -    EN EL "+str(float((((qualcomm_iot)*100)/(len(df_cve_iot["CVE_Items.cve.CVE_data_meta.ASSIGNER"])+len(df_cve_sh["CVE_Items.cve.CVE_data_meta.ASSIGNER"])))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE LA CVE ES SECURITY.CNA@QUALCOMM \n")
print("    -    EN EL "+str(float((((apache_iot)*100)/(len(df_cve_iot["CVE_Items.cve.CVE_data_meta.ASSIGNER"])+len(df_cve_sh["CVE_Items.cve.CVE_data_meta.ASSIGNER"])))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE LA CVE ES SECURITY@APACHE.ORG \n")
print("    -    EN EL "+str(float((((oracle_iot)*100)/(len(df_cve_iot["CVE_Items.cve.CVE_data_meta.ASSIGNER"])+len(df_cve_sh["CVE_Items.cve.CVE_data_meta.ASSIGNER"])))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE LA CVE ES SECALERT_US@ORACLE \n")
print("    -    EN EL "+str(float((((microsoft_iot)*100)/(len(df_cve_iot["CVE_Items.cve.CVE_data_meta.ASSIGNER"])+len(df_cve_sh["CVE_Items.cve.CVE_data_meta.ASSIGNER"])))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE LA CVE ES SECURE@MICROSOFT \n")
print("    -    EN EL "+str(float((((trendmicro_iot)*100)/(len(df_cve_iot["CVE_Items.cve.CVE_data_meta.ASSIGNER"])+len(df_cve_sh["CVE_Items.cve.CVE_data_meta.ASSIGNER"])))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE LA CVE ES SECURITY@TRENDMICRO \n")
print("    -    EN EL "+str(float((((nozomi_iot)*100)/(len(df_cve_iot["CVE_Items.cve.CVE_data_meta.ASSIGNER"])+len(df_cve_sh["CVE_Items.cve.CVE_data_meta.ASSIGNER"])))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE LA CVE ES PRODSEC@NOZOMINETWORKS \n")
print("    -    EN EL "+str(float((((schneider_iot)*100)/(len(df_cve_iot["CVE_Items.cve.CVE_data_meta.ASSIGNER"])+len(df_cve_sh["CVE_Items.cve.CVE_data_meta.ASSIGNER"])))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE LA CVE ES CYBERSECURITY@SCHNEIDER-ELECTRIC \n")
print("    -    EN EL "+str(float((((apple_iot)*100)/(len(df_cve_iot["CVE_Items.cve.CVE_data_meta.ASSIGNER"])+len(df_cve_sh["CVE_Items.cve.CVE_data_meta.ASSIGNER"])))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE LA CVE ES PRODUCT-SECURITY@APPLE \n")
print("    -    EN EL "+str(float((((android_iot)*100)/(len(df_cve_iot["CVE_Items.cve.CVE_data_meta.ASSIGNER"])+len(df_cve_sh["CVE_Items.cve.CVE_data_meta.ASSIGNER"])))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE LA CVE ES SECURITY@ANDROID \n")
print("    -    EN EL "+str(float((((bitdefender_iot)*100)/(len(df_cve_iot["CVE_Items.cve.CVE_data_meta.ASSIGNER"])+len(df_cve_sh["CVE_Items.cve.CVE_data_meta.ASSIGNER"])))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE LA CVE ES CVE-REQUESTS@BITDEFENDER \n")
print("    -    EN EL "+str(float((((mozilla_iot)*100)/(len(df_cve_iot["CVE_Items.cve.CVE_data_meta.ASSIGNER"])+len(df_cve_sh["CVE_Items.cve.CVE_data_meta.ASSIGNER"])))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE LA CVE ES SECURITY@MOZILLA \n")
print("    -    EN EL "+str(float((((fsecure_iot)*100)/(len(df_cve_iot["CVE_Items.cve.CVE_data_meta.ASSIGNER"])+len(df_cve_sh["CVE_Items.cve.CVE_data_meta.ASSIGNER"])))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE LA CVE ES FSECURE \n")
print("    -    EN EL "+str(float((((other_assigner_sh+other_assigner_iot)*100)/(len(df_cve_iot["CVE_Items.cve.CVE_data_meta.ASSIGNER"])+len(df_cve_sh["CVE_Items.cve.CVE_data_meta.ASSIGNER"])))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE LA CVE ES DISTINTO A LOS ANTERIORES \n")






