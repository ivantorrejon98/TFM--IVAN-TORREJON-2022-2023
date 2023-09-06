
import pandas as pd

#Abro los ficheros con los que voy a tratar


df_cve_iot=pd.read_excel('cves_iot_2023.xlsx')
df_cve_sh=pd.read_excel('cves_smart_home_2023.xlsx')


#Variables donde almacenare el contador de asignador de CVE para la parte de IOT
jpcert_iot=0
jpcert_iot_2023=0
jpcert_iot_2022=0
jpcert_iot_2021=0
jpcert_iot_2020=0
jpcert_iot_2019=0
jpcert_iot_2018=0

mitre_iot=0
mitre_iot_2023=0
mitre_iot_2022=0
mitre_iot_2021=0
mitre_iot_2020=0
mitre_iot_2019=0
mitre_iot_2018=0

cisco_iot=0
cisco_iot_2023=0
cisco_iot_2022=0
cisco_iot_2021=0
cisco_iot_2020=0
cisco_iot_2019=0
cisco_iot_2018=0

github_iot=0
github_iot_2023=0
github_iot_2022=0
github_iot_2021=0
github_iot_2020=0
github_iot_2019=0
github_iot_2018=0

redhat_iot=0
redhat_iot_2023=0
redhat_iot_2022=0
redhat_iot_2021=0
redhat_iot_2020=0
redhat_iot_2019=0
redhat_iot_2018=0

qualcomm_iot=0
qualcomm_iot_2023=0
qualcomm_iot_2022=0
qualcomm_iot_2021=0
qualcomm_iot_2020=0
qualcomm_iot_2019=0
qualcomm_iot_2018=0

apache_iot=0
apache_iot_2023=0
apache_iot_2022=0
apache_iot_2021=0
apache_iot_2020=0
apache_iot_2019=0
apache_iot_2018=0

oracle_iot=0
oracle_iot_2023=0
oracle_iot_2022=0
oracle_iot_2021=0
oracle_iot_2020=0
oracle_iot_2019=0
oracle_iot_2018=0

microsoft_iot=0
microsoft_iot_2023=0
microsoft_iot_2022=0
microsoft_iot_2021=0
microsoft_iot_2020=0
microsoft_iot_2019=0
microsoft_iot_2018=0

cert_iot=0
cert_iot_2023=0
cert_iot_2022=0
cert_iot_2021=0
cert_iot_2020=0
cert_iot_2019=0
cert_iot_2018=0

trendmicro_iot=0
trendmicro_iot_2023=0
trendmicro_iot_2022=0
trendmicro_iot_2021=0
trendmicro_iot_2020=0
trendmicro_iot_2019=0
trendmicro_iot_2018=0

nozomi_iot=0
nozomi_iot_2023=0
nozomi_iot_2022=0
nozomi_iot_2021=0
nozomi_iot_2020=0
nozomi_iot_2019=0
nozomi_iot_2018=0

hq_iot=0
hq_iot_2023=0
hq_iot_2022=0
hq_iot_2021=0
hq_iot_2020=0
hq_iot_2019=0
hq_iot_2018=0

kaspersky_iot=0
kaspersky_iot_2023=0
kaspersky_iot_2022=0
kaspersky_iot_2021=0
kaspersky_iot_2020=0
kaspersky_iot_2019=0
kaspersky_iot_2018=0

schneider_iot=0
schneider_iot_2023=0
schneider_iot_2022=0
schneider_iot_2021=0
schneider_iot_2020=0
schneider_iot_2019=0
schneider_iot_2018=0

apple_iot=0
apple_iot_2023=0
apple_iot_2022=0
apple_iot_2021=0
apple_iot_2020=0
apple_iot_2019=0
apple_iot_2018=0

android_iot=0
android_iot_2023=0
android_iot_2022=0
android_iot_2021=0
android_iot_2020=0
android_iot_2019=0
android_iot_2018=0

bitdefender_iot=0
bitdefender_iot_2023=0
bitdefender_iot_2022=0
bitdefender_iot_2021=0
bitdefender_iot_2020=0
bitdefender_iot_2019=0
bitdefender_iot_2018=0

mcafee_iot=0
mcafee_iot_2023=0
mcafee_iot_2022=0
mcafee_iot_2021=0
mcafee_iot_2020=0
mcafee_iot_2019=0
mcafee_iot_2018=0

mozilla_iot=0
mozilla_iot_2023=0
mozilla_iot_2022=0
mozilla_iot_2021=0
mozilla_iot_2020=0
mozilla_iot_2019=0
mozilla_iot_2018=0

hpe_iot=0
hpe_iot_2023=0
hpe_iot_2022=0
hpe_iot_2021=0
hpe_iot_2020=0
hpe_iot_2019=0
hpe_iot_2018=0

fsecure_iot=0
fsecure_iot_2023=0
fsecure_iot_2022=0
fsecure_iot_2021=0
fsecure_iot_2020=0
fsecure_iot_2019=0
fsecure_iot_2018=0

rapid7_iot=0
rapid7_iot_2023=0
rapid7_iot_2022=0
rapid7_iot_2021=0
rapid7_iot_2020=0
rapid7_iot_2019=0
rapid7_iot_2018=0

other_assigner_iot=0
other_assigner_iot_2023=0
other_assigner_iot_2022=0
other_assigner_iot_2021=0
other_assigner_iot_2020=0
other_assigner_iot_2019=0
other_assigner_iot_2018=0
#Variables donde almaceno la cantidad de assigner en los distintos anios
assigner_iot_2023=0
assigner_iot_2022=0
assigner_iot_2021=0
assigner_iot_2020=0
assigner_iot_2019=0
assigner_iot_2018=0

#Contador de total DE ASIGNADORES CVE con valores no nulos
total_assigner_iot=0


#Recorro los valores de ASIGNADOR CVE para la parte IOT y despues consulto la fecha de publicacion

for j in range(0,len(df_cve_iot["CVE_Items.cve.CVE_data_meta.ASSIGNER"])):
    if(df_cve_iot["CVE_Items.cve.CVE_data_meta.ASSIGNER"][j] !='NONE'):
        total_assigner_iot+=1
        if("jpcert" in df_cve_iot["CVE_Items.cve.CVE_data_meta.ASSIGNER"][j]):
            jpcert_iot+=1
            str_anio_publidate_cve_iot=df_cve_iot["CVE_Items.publishedDate"][j].split("-")
            anio_publidate_cve_iot=int(str_anio_publidate_cve_iot[0])
            if(anio_publidate_cve_iot >= 2023):
                jpcert_iot_2023+=1
                assigner_iot_2023+=1
            elif(anio_publidate_cve_iot >= 2022):
                jpcert_iot_2022+=1
                assigner_iot_2022+=1
            elif(anio_publidate_cve_iot >= 2021):
                jpcert_iot_2021+=1
                assigner_iot_2021+=1
            elif(anio_publidate_cve_iot >= 2020):
                jpcert_iot_2020+=1
                assigner_iot_2020+=1
            elif(anio_publidate_cve_iot >= 2019):
                jpcert_iot_2019+=1
                assigner_iot_2019+=1
            else:
                assigner_iot_2018+=1
                jpcert_iot_2018+=1

        elif("@mitre" in df_cve_iot["CVE_Items.cve.CVE_data_meta.ASSIGNER"][j]):
            mitre_iot+=1
            str_anio_publidate_cve_iot=df_cve_iot["CVE_Items.publishedDate"][j].split("-")
            anio_publidate_cve_iot=int(str_anio_publidate_cve_iot[0])
            if(anio_publidate_cve_iot >= 2023):
                mitre_iot_2023+=1
                assigner_iot_2023+=1
            elif(anio_publidate_cve_iot >= 2022):
                mitre_iot_2022+=1
                assigner_iot_2022+=1
            elif(anio_publidate_cve_iot >= 2021):
                mitre_iot_2021+=1
                assigner_iot_2021+=1
            elif(anio_publidate_cve_iot >= 2020):
                mitre_iot_2020+=1
                assigner_iot_2020+=1
            elif(anio_publidate_cve_iot >= 2019):
                mitre_iot_2019+=1
                assigner_iot_2019+=1
            else:
                mitre_iot_2018+=1
                assigner_iot_2018+=1
        elif("@cisco" in df_cve_iot["CVE_Items.cve.CVE_data_meta.ASSIGNER"][j]):
            cisco_iot+=1
            str_anio_publidate_cve_iot=df_cve_iot["CVE_Items.publishedDate"][j].split("-")
            anio_publidate_cve_iot=int(str_anio_publidate_cve_iot[0])
            if(anio_publidate_cve_iot >= 2023):
                cisco_iot_2023+=1
                assigner_iot_2023+=1
            elif(anio_publidate_cve_iot >= 2022):
                cisco_iot_2022+=1
                assigner_iot_2022+=1
            elif(anio_publidate_cve_iot >= 2021):
                cisco_iot_2021+=1
                assigner_iot_2021+=1
            elif(anio_publidate_cve_iot >= 2020):
                cisco_iot_2020+=1
                assigner_iot_2020+=1
            elif(anio_publidate_cve_iot >= 2019):
                cisco_iot_2019+=1
                assigner_iot_2019+=1
            else:
                cisco_iot_2018+=1
                assigner_iot_2018+=1
        elif("@github" in df_cve_iot["CVE_Items.cve.CVE_data_meta.ASSIGNER"][j]):
            github_iot+=1
            str_anio_publidate_cve_iot=df_cve_iot["CVE_Items.publishedDate"][j].split("-")
            anio_publidate_cve_iot=int(str_anio_publidate_cve_iot[0])
            if(anio_publidate_cve_iot >= 2023):
                github_iot_2023+=1
                assigner_iot_2023+=1
            elif(anio_publidate_cve_iot >= 2022):
                github_iot_2022+=1
                assigner_iot_2022+=1
            elif(anio_publidate_cve_iot >= 2021):
                github_iot_2021+=1
                assigner_iot_2021+=1
            elif(anio_publidate_cve_iot >= 2020):
                github_iot_2020+=1
                assigner_iot_2020+=1
            elif(anio_publidate_cve_iot >= 2019):
                github_iot_2019+=1
                assigner_iot_2019+=1
            else:
                github_iot_2018+=1
                assigner_iot_2018+=1
        elif("@redhat" in df_cve_iot["CVE_Items.cve.CVE_data_meta.ASSIGNER"][j]):
            redhat_iot+=1
            str_anio_publidate_cve_iot=df_cve_iot["CVE_Items.publishedDate"][j].split("-")
            anio_publidate_cve_iot=int(str_anio_publidate_cve_iot[0])
            if(anio_publidate_cve_iot >= 2023):
                redhat_iot_2023+=1
                assigner_iot_2023+=1
            elif(anio_publidate_cve_iot >= 2022):
                redhat_iot_2022+=1
                assigner_iot_2022+=1
            elif(anio_publidate_cve_iot >= 2021):
                redhat_iot_2021+=1
                assigner_iot_2021+=1
            elif(anio_publidate_cve_iot >= 2020):
                redhat_iot_2020+=1
                assigner_iot_2020+=1
            elif(anio_publidate_cve_iot >= 2019):
                redhat_iot_2019+=1
                assigner_iot_2019+=1
            else:
                redhat_iot_2018+=1
                assigner_iot_2018+=1
        elif("@qualcomm" in df_cve_iot["CVE_Items.cve.CVE_data_meta.ASSIGNER"][j]):
            qualcomm_iot+=1
            str_anio_publidate_cve_iot=df_cve_iot["CVE_Items.publishedDate"][j].split("-")
            anio_publidate_cve_iot=int(str_anio_publidate_cve_iot[0])
            if(anio_publidate_cve_iot >= 2023):
                qualcomm_iot_2023+=1
                assigner_iot_2023+=1
            elif(anio_publidate_cve_iot >= 2022):
                qualcomm_iot_2022+=1
                assigner_iot_2022+=1
            elif(anio_publidate_cve_iot >= 2021):
                qualcomm_iot_2021+=1
                assigner_iot_2021+=1
            elif(anio_publidate_cve_iot >= 2020):
                qualcomm_iot_2020+=1
                assigner_iot_2020+=1
            elif(anio_publidate_cve_iot >= 2019):
                qualcomm_iot_2019+=1
                assigner_iot_2019+=1
            else:
                qualcomm_iot_2018+=1
                assigner_iot_2018+=1
        elif("@apache" in df_cve_iot["CVE_Items.cve.CVE_data_meta.ASSIGNER"][j]):
            apache_iot+=1
            str_anio_publidate_cve_iot=df_cve_iot["CVE_Items.publishedDate"][j].split("-")
            anio_publidate_cve_iot=int(str_anio_publidate_cve_iot[0])
            if(anio_publidate_cve_iot >= 2023):
                apache_iot_2023+=1
                assigner_iot_2023+=1
            elif(anio_publidate_cve_iot >= 2022):
                apache_iot_2022+=1
                assigner_iot_2022+=1
            elif(anio_publidate_cve_iot >= 2021):
                apache_iot_2021+=1
                assigner_iot_2021+=1
            elif(anio_publidate_cve_iot >= 2020):
                apache_iot_2020+=1
                assigner_iot_2020+=1
            elif(anio_publidate_cve_iot >= 2019):
                apache_iot_2019+=1
                assigner_iot_2019+=1
            else:
                apache_iot_2018+=1
                assigner_iot_2018+=1
        elif("@oracle" in df_cve_iot["CVE_Items.cve.CVE_data_meta.ASSIGNER"][j]):
            oracle_iot+=1
            str_anio_publidate_cve_iot=df_cve_iot["CVE_Items.publishedDate"][j].split("-")
            anio_publidate_cve_iot=int(str_anio_publidate_cve_iot[0])
            if(anio_publidate_cve_iot >= 2023):
                oracle_iot_2023+=1
                assigner_iot_2023+=1
            elif(anio_publidate_cve_iot >= 2022):
                oracle_iot_2022+=1
                assigner_iot_2022+=1
            elif(anio_publidate_cve_iot >= 2021):
                oracle_iot_2021+=1
                assigner_iot_2021+=1
            elif(anio_publidate_cve_iot >= 2020):
                oracle_iot_2020+=1
                assigner_iot_2020+=1
            elif(anio_publidate_cve_iot >= 2019):
                oracle_iot_2019+=1
                assigner_iot_2019+=1
            else:
                oracle_iot_2018+=1
                assigner_iot_2018+=1
        elif("@microsoft" in df_cve_iot["CVE_Items.cve.CVE_data_meta.ASSIGNER"][j]):
            microsoft_iot+=1
            str_anio_publidate_cve_iot=df_cve_iot["CVE_Items.publishedDate"][j].split("-")
            anio_publidate_cve_iot=int(str_anio_publidate_cve_iot[0])
            if(anio_publidate_cve_iot >= 2023):
                microsoft_iot_2023+=1
                assigner_iot_2023+=1
            elif(anio_publidate_cve_iot >= 2022):
                microsoft_iot_2022+=1
                assigner_iot_2022+=1
            elif(anio_publidate_cve_iot >= 2021):
                microsoft_iot_2021+=1
                assigner_iot_2021+=1
            elif(anio_publidate_cve_iot >= 2020):
                microsoft_iot_2020+=1
                assigner_iot_2020+=1
            elif(anio_publidate_cve_iot >= 2019):
                microsoft_iot_2019+=1
                assigner_iot_2019+=1
            else:
                microsoft_iot_2018+=1
                assigner_iot_2018+=1
        elif("@cert" in df_cve_iot["CVE_Items.cve.CVE_data_meta.ASSIGNER"][j]):
            cert_iot+=1
            str_anio_publidate_cve_iot=df_cve_iot["CVE_Items.publishedDate"][j].split("-")
            anio_publidate_cve_iot=int(str_anio_publidate_cve_iot[0])
            if(anio_publidate_cve_iot >= 2023):
                cert_iot_2023+=1
                assigner_iot_2023+=1
            elif(anio_publidate_cve_iot >= 2022):
                cert_iot_2022+=1
                assigner_iot_2022+=1
            elif(anio_publidate_cve_iot >= 2021):
                cert_iot_2021+=1
                assigner_iot_2021+=1
            elif(anio_publidate_cve_iot >= 2020):
                cert_iot_2020+=1
                assigner_iot_2020+=1
            elif(anio_publidate_cve_iot >= 2019):
                cert_iot_2019+=1
                assigner_iot_2019+=1
            else:
                cert_iot_2018+=1
                assigner_iot_2018+=1
        elif("@trendmicro" in df_cve_iot["CVE_Items.cve.CVE_data_meta.ASSIGNER"][j]):
            trendmicro_iot+=1
            str_anio_publidate_cve_iot=df_cve_iot["CVE_Items.publishedDate"][j].split("-")
            anio_publidate_cve_iot=int(str_anio_publidate_cve_iot[0])
            if(anio_publidate_cve_iot >= 2023):
                trendmicro_iot_2023+=1
                assigner_iot_2023+=1
            elif(anio_publidate_cve_iot >= 2022):
                trendmicro_iot_2022+=1
                assigner_iot_2022+=1
            elif(anio_publidate_cve_iot >= 2021):
                trendmicro_iot_2021+=1
                assigner_iot_2021+=1
            elif(anio_publidate_cve_iot >= 2020):
                trendmicro_iot_2020+=1
                assigner_iot_2020+=1
            elif(anio_publidate_cve_iot >= 2019):
                trendmicro_iot_2019+=1
                assigner_iot_2019+=1
            else:
                trendmicro_iot_2018+=1
                assigner_iot_2018+=1
        elif("@nozomi" in df_cve_iot["CVE_Items.cve.CVE_data_meta.ASSIGNER"][j]):
            nozomi_iot+=1
            str_anio_publidate_cve_iot=df_cve_iot["CVE_Items.publishedDate"][j].split("-")
            anio_publidate_cve_iot=int(str_anio_publidate_cve_iot[0])
            if(anio_publidate_cve_iot >= 2023):
                nozomi_iot_2023+=1
                assigner_iot_2023+=1
            elif(anio_publidate_cve_iot >= 2022):
                nozomi_iot_2022+=1
                assigner_iot_2022+=1
            elif(anio_publidate_cve_iot >= 2021):
                nozomi_iot_2021+=1
                assigner_iot_2021+=1
            elif(anio_publidate_cve_iot >= 2020):
                nozomi_iot_2020+=1
                assigner_iot_2020+=1
            elif(anio_publidate_cve_iot >= 2019):
                nozomi_iot_2019+=1
                assigner_iot_2019+=1
            else:
                nozomi_iot_2018+=1
                assigner_iot_2018+=1
        elif("@hq" in df_cve_iot["CVE_Items.cve.CVE_data_meta.ASSIGNER"][j]):
            hq_iot+=1
            str_anio_publidate_cve_iot=df_cve_iot["CVE_Items.publishedDate"][j].split("-")
            anio_publidate_cve_iot=int(str_anio_publidate_cve_iot[0])
            if(anio_publidate_cve_iot >= 2023):
                hq_iot_2023+=1
                assigner_iot_2023+=1
            elif(anio_publidate_cve_iot >= 2022):
                hq_iot_2022+=1
                assigner_iot_2022+=1
            elif(anio_publidate_cve_iot >= 2021):
                hq_iot_2021+=1
                assigner_iot_2021+=1
            elif(anio_publidate_cve_iot >= 2020):
                hq_iot_2020+=1
                assigner_iot_2020+=1
            elif(anio_publidate_cve_iot >= 2019):
                hq_iot_2019+=1
                assigner_iot_2019+=1
            else:
                hq_iot_2018+=1
                assigner_iot_2018+=1
        elif("@kaspersky" in df_cve_iot["CVE_Items.cve.CVE_data_meta.ASSIGNER"][j]):
            kaspersky_iot+=1
            str_anio_publidate_cve_iot=df_cve_iot["CVE_Items.publishedDate"][j].split("-")
            anio_publidate_cve_iot=int(str_anio_publidate_cve_iot[0])
            if(anio_publidate_cve_iot >= 2023):
                kaspersky_iot_2023+=1
                assigner_iot_2023+=1
            elif(anio_publidate_cve_iot >= 2022):
                kaspersky_iot_2022+=1
                assigner_iot_2022+=1
            elif(anio_publidate_cve_iot >= 2021):
                kaspersky_iot_2021+=1
                assigner_iot_2021+=1
            elif(anio_publidate_cve_iot >= 2020):
                kaspersky_iot_2020+=1
                assigner_iot_2020+=1
            elif(anio_publidate_cve_iot >= 2019):
                kaspersky_iot_2019+=1
                assigner_iot_2019+=1
            else:
                kaspersky_iot_2018+=1
                assigner_iot_2018+=1
        elif("@schneider" in df_cve_iot["CVE_Items.cve.CVE_data_meta.ASSIGNER"][j]):
            schneider_iot+=1
            str_anio_publidate_cve_iot=df_cve_iot["CVE_Items.publishedDate"][j].split("-")
            anio_publidate_cve_iot=int(str_anio_publidate_cve_iot[0])
            if(anio_publidate_cve_iot >= 2023):
                schneider_iot_2023+=1
                assigner_iot_2023+=1
            elif(anio_publidate_cve_iot >= 2022):
                schneider_iot_2022+=1
                assigner_iot_2022+=1
            elif(anio_publidate_cve_iot >= 2021):
                schneider_iot_2021+=1
                assigner_iot_2021+=1
            elif(anio_publidate_cve_iot >= 2020):
                schneider_iot_2020+=1
                assigner_iot_2020+=1
            elif(anio_publidate_cve_iot >= 2019):
                schneider_iot_2019+=1
                assigner_iot_2019+=1
            else:
                schneider_iot_2018+=1
                assigner_iot_2018+=1
        elif("@apple" in df_cve_iot["CVE_Items.cve.CVE_data_meta.ASSIGNER"][j]):
            apple_iot+=1
            str_anio_publidate_cve_iot=df_cve_iot["CVE_Items.publishedDate"][j].split("-")
            anio_publidate_cve_iot=int(str_anio_publidate_cve_iot[0])
            if(anio_publidate_cve_iot >= 2023):
                apple_iot_2023+=1
                assigner_iot_2023+=1
            elif(anio_publidate_cve_iot >= 2022):
                apple_iot_2022+=1
                assigner_iot_2022+=1
            elif(anio_publidate_cve_iot >= 2021):
                apple_iot_2021+=1
                assigner_iot_2021+=1
            elif(anio_publidate_cve_iot >= 2020):
                apple_iot_2020+=1
                assigner_iot_2020+=1
            elif(anio_publidate_cve_iot >= 2019):
                apple_iot_2019+=1
                assigner_iot_2019+=1
            else:
                apple_iot_2018+=1
                assigner_iot_2018+=1
        elif("@android" in df_cve_iot["CVE_Items.cve.CVE_data_meta.ASSIGNER"][j]):
            android_iot+=1
            str_anio_publidate_cve_iot=df_cve_iot["CVE_Items.publishedDate"][j].split("-")
            anio_publidate_cve_iot=int(str_anio_publidate_cve_iot[0])
            if(anio_publidate_cve_iot >= 2023):
                android_iot_2023+=1
                assigner_iot_2023+=1
            elif(anio_publidate_cve_iot >= 2022):
                android_iot_2022+=1
                assigner_iot_2022+=1
            elif(anio_publidate_cve_iot >= 2021):
                android_iot_2021+=1
                assigner_iot_2021+=1
            elif(anio_publidate_cve_iot >= 2020):
                android_iot_2020+=1
                assigner_iot_2020+=1
            elif(anio_publidate_cve_iot >= 2019):
                android_iot_2019+=1
                assigner_iot_2019+=1
            else:
                android_iot_2018+=1
                assigner_iot_2018+=1
        elif("@bitdefender" in df_cve_iot["CVE_Items.cve.CVE_data_meta.ASSIGNER"][j]):
            bitdefender_iot+=1
            str_anio_publidate_cve_iot=df_cve_iot["CVE_Items.publishedDate"][j].split("-")
            anio_publidate_cve_iot=int(str_anio_publidate_cve_iot[0])
            if(anio_publidate_cve_iot >= 2023):
                bitdefender_iot_2023+=1
                assigner_iot_2023+=1
            elif(anio_publidate_cve_iot >= 2022):
                bitdefender_iot_2022+=1
                assigner_iot_2022+=1
            elif(anio_publidate_cve_iot >= 2021):
                bitdefender_iot_2021+=1
                assigner_iot_2021+=1
            elif(anio_publidate_cve_iot >= 2020):
                bitdefender_iot_2020+=1
                assigner_iot_2020+=1
            elif(anio_publidate_cve_iot >= 2019):
                bitdefender_iot_2019+=1
                assigner_iot_2019+=1
            else:
                bitdefender_iot_2018+=1
                assigner_iot_2018+=1
        elif("@mcafee" in df_cve_iot["CVE_Items.cve.CVE_data_meta.ASSIGNER"][j]):
            mcafee_iot+=1
            str_anio_publidate_cve_iot=df_cve_iot["CVE_Items.publishedDate"][j].split("-")
            anio_publidate_cve_iot=int(str_anio_publidate_cve_iot[0])
            if(anio_publidate_cve_iot >= 2023):
                mcafee_iot_2023+=1
                assigner_iot_2023+=1
            elif(anio_publidate_cve_iot >= 2022):
                mcafee_iot_2022+=1
                assigner_iot_2022+=1
            elif(anio_publidate_cve_iot >= 2021):
                mcafee_iot_2021+=1
                assigner_iot_2021+=1
            elif(anio_publidate_cve_iot >= 2020):
                mcafee_iot_2020+=1
                assigner_iot_2020+=1
            elif(anio_publidate_cve_iot >= 2019):
                mcafee_iot_2019+=1
                assigner_iot_2019+=1
            else:
                mcafee_iot_2018+=1  
                assigner_iot_2018+=1
        elif("@mozilla" in df_cve_iot["CVE_Items.cve.CVE_data_meta.ASSIGNER"][j]):
            mozilla_iot+=1
            str_anio_publidate_cve_iot=df_cve_iot["CVE_Items.publishedDate"][j].split("-")
            anio_publidate_cve_iot=int(str_anio_publidate_cve_iot[0])
            if(anio_publidate_cve_iot >= 2023):
                mozilla_iot_2023+=1
                assigner_iot_2023+=1
            elif(anio_publidate_cve_iot >= 2022):
                mozilla_iot_2022+=1
                assigner_iot_2022+=1
            elif(anio_publidate_cve_iot >= 2021):
                mozilla_iot_2021+=1
                assigner_iot_2021+=1
            elif(anio_publidate_cve_iot >= 2020):
                mozilla_iot_2020+=1
                assigner_iot_2020+=1
            elif(anio_publidate_cve_iot >= 2019):
                mozilla_iot_2019+=1
                assigner_iot_2019+=1
            else:
                mozilla_iot_2018+=1
                assigner_iot_2018+=1
        elif("@hpe" in df_cve_iot["CVE_Items.cve.CVE_data_meta.ASSIGNER"][j]):
            hpe_iot+=1
            str_anio_publidate_cve_iot=df_cve_iot["CVE_Items.publishedDate"][j].split("-")
            anio_publidate_cve_iot=int(str_anio_publidate_cve_iot[0])
            if(anio_publidate_cve_iot >= 2023):
                hpe_iot_2023+=1
                assigner_iot_2023+=1
            elif(anio_publidate_cve_iot >= 2022):
                hpe_iot_2022+=1
                assigner_iot_2022+=1
            elif(anio_publidate_cve_iot >= 2021):
                hpe_iot_2021+=1
                assigner_iot_2021+=1
            elif(anio_publidate_cve_iot >= 2020):
                hpe_iot_2020+=1
                assigner_iot_2020+=1
            elif(anio_publidate_cve_iot >= 2019):
                hpe_iot_2019+=1
                assigner_iot_2019+=1
            else:
                hpe_iot_2018+=1 
                assigner_iot_2018+=1
        elif("@f-secure" in df_cve_iot["CVE_Items.cve.CVE_data_meta.ASSIGNER"][j]):
            fsecure_iot+=1
            str_anio_publidate_cve_iot=df_cve_iot["CVE_Items.publishedDate"][j].split("-")
            anio_publidate_cve_iot=int(str_anio_publidate_cve_iot[0])
            if(anio_publidate_cve_iot >= 2023):
                fsecure_iot_2023+=1
                assigner_iot_2023+=1
            elif(anio_publidate_cve_iot >= 2022):
                fsecure_iot_2022+=1
                assigner_iot_2022+=1
            elif(anio_publidate_cve_iot >= 2021):
                fsecure_iot_2021+=1
                assigner_iot_2021+=1
            elif(anio_publidate_cve_iot >= 2020):
                fsecure_iot_2020+=1
                assigner_iot_2020+=1
            elif(anio_publidate_cve_iot >= 2019):
                fsecure_iot_2019+=1
                assigner_iot_2019+=1
            else:
                fsecure_iot_2018+=1 
                assigner_iot_2018+=1
        elif("@rapid7" in df_cve_iot["CVE_Items.cve.CVE_data_meta.ASSIGNER"][j]):
            rapid7_iot+=1
            str_anio_publidate_cve_iot=df_cve_iot["CVE_Items.publishedDate"][j].split("-")
            anio_publidate_cve_iot=int(str_anio_publidate_cve_iot[0])
            if(anio_publidate_cve_iot >= 2023):
                rapid7_iot_2023+=1
                assigner_iot_2023+=1
            elif(anio_publidate_cve_iot >= 2022):
                rapid7_iot_2022+=1
                assigner_iot_2022+=1
            elif(anio_publidate_cve_iot >= 2021):
                rapid7_iot_2021+=1
                assigner_iot_2021+=1
            elif(anio_publidate_cve_iot >= 2020):
                rapid7_iot_2020+=1
                assigner_iot_2020+=1
            elif(anio_publidate_cve_iot >= 2019):
                rapid7_iot_2019+=1
                assigner_iot_2019+=1
            else:
                rapid7_iot_2018+=1 
                assigner_iot_2018+=1
        else:
            other_assigner_iot+=1
            str_anio_publidate_cve_iot=df_cve_iot["CVE_Items.publishedDate"][j].split("-")
            anio_publidate_cve_iot=int(str_anio_publidate_cve_iot[0])
            if(anio_publidate_cve_iot >= 2023):
                other_assigner_iot_2023+=1
                assigner_iot_2023+=1
            elif(anio_publidate_cve_iot >= 2022):
                other_assigner_iot_2022+=1
                assigner_iot_2022+=1
            elif(anio_publidate_cve_iot >= 2021):
                other_assigner_iot_2021+=1
                assigner_iot_2021+=1
            elif(anio_publidate_cve_iot >= 2020):
                other_assigner_iot_2020+=1
                assigner_iot_2020+=1
            elif(anio_publidate_cve_iot >= 2019):
                other_assigner_iot_2019+=1
                assigner_iot_2019+=1
            else:
                other_assigner_iot_2018+=1
                assigner_iot_2018+=1
    

print("**************************ESTADÍSTICAS CVE RELACION FECHA DE PUBLICACION Y ASIGNADOR CVE PARTE IOT********************************")
print("\n")
print(" -  DE UN TOTAL DE "+str(total_assigner_iot)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ESTÁ DEFINIDO, LAS ESTADÍSTICAS DE ASSIGNER Y FECHA DE PUBLICACION SON LAS SIGUIENTES  : \n")
print("\n")
print(" -  DE UN TOTAL DE "+str(assigner_iot_2023)+" VULNERABILIDADES PUBLICADAS EN 2023, LAS ESTADÍSTICAS DE ASIGNADORES CVE SON LAS SIGUIENTES : \n")
print("     -      EN "+str(jpcert_iot_2023)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES VULTURES@JPCERT\n")
print("     -      EN "+str(mitre_iot_2023)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES CVE@MITRE \n")
print("     -      EN "+str(cisco_iot_2023)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES TALOS-CNA@CISCO \n")
print("     -      EN "+str(github_iot_2023)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY-ADVISORIES@GITHUB \n")
print("     -      EN "+str(redhat_iot_2023)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES SECALERT@REDHAT \n")
print("     -      EN "+str(qualcomm_iot_2023)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY.CNA@QUALCOMM \n")
print("     -      EN "+str(apache_iot_2023)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY@APACHE.ORG \n")
print("     -      EN "+str(oracle_iot_2023)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES SECALERT_US@ORACLE \n")
print("     -      EN "+str(microsoft_iot_2023)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURE@MICROSOFT \n")
print("     -      EN "+str(cert_iot_2023)+" VULNERABILIDADES EL ASIGNADOR DE CVE INFO@CERT.VDE \n")
print("     -      EN "+str(trendmicro_iot_2023)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY@TRENDMICRO \n")
print("     -      EN "+str(nozomi_iot_2023)+" VULNERABILIDADES EL ASIGNADOR DE CVE PRODSEC@NOZOMINETWORKS \n")
print("     -      EN "+str(hq_iot_2023)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES ICS-CERT@HQ.DHS.GOV \n")
print("     -      EN "+str(kaspersky_iot_2023)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES VULNERABILITY@KASPERSKY \n")
print("     -      EN "+str(schneider_iot_2023)+" VULNERABILIDADES EL ASIGNADOR DE CVE CYBERSECURITY@SCHNEIDER-ELECTRIC \n")
print("     -      EN "+str(apple_iot_2023)+" VULNERABILIDADES EL ASIGNADOR DE CVE PRODUCT-SECURITY@APPLE \n")
print("     -      EN "+str(android_iot_2023)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY@ANDROID \n")
print("     -      EN "+str(bitdefender_iot_2023)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES CVE-REQUESTS@BITDEFENDER \n")
print("     -      EN "+str(mcafee_iot_2023)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES PSIRT@MCAFEE \n")
print("     -      EN "+str(mozilla_iot_2023)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY@MOZILLA \n")
print("     -      EN "+str(hpe_iot_2023)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY-ALERT@HPE \n")
print("     -      EN "+str(fsecure_iot_2023)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES CVE-NOTIFICATIONS-US@F-SECURE.COM \n")
print("     -      EN "+str(rapid7_iot_2023)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES CVE@RAPID7 \n")
print("     -      EN "+str(other_assigner_iot_2023)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES DISTINTO DE LOS ANTERIORES \n")
print("\n")
print("\n")
print(" DE UN TOTAL DE "+str(assigner_iot_2022)+" VULNERABILIDADES PUBLICADAS EN 2022, LAS ESTADÍSTICAS DE ASIGNADORES CVE SON LAS SIGUIENTES : \n")
print("     -      EN "+str(jpcert_iot_2022)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES VULTURES@JPCERT\n")
print("     -      EN "+str(mitre_iot_2022)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES CVE@MITRE \n")
print("     -      EN "+str(cisco_iot_2022)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES TALOS-CNA@CISCO \n")
print("     -      EN "+str(github_iot_2022)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY-ADVISORIES@GITHUB \n")
print("     -      EN "+str(redhat_iot_2022)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES SECALERT@REDHAT \n")
print("     -      EN "+str(qualcomm_iot_2022)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY.CNA@QUALCOMM \n")
print("     -      EN "+str(apache_iot_2022)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY@APACHE.ORG \n")
print("     -      EN "+str(oracle_iot_2022)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES SECALERT_US@ORACLE \n")
print("     -      EN "+str(microsoft_iot_2022)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURE@MICROSOFT \n")
print("     -      EN "+str(cert_iot_2022)+" VULNERABILIDADES EL ASIGNADOR DE CVE INFO@CERT.VDE \n")
print("     -      EN "+str(trendmicro_iot_2022)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY@TRENDMICRO \n")
print("     -      EN "+str(nozomi_iot_2022)+" VULNERABILIDADES EL ASIGNADOR DE CVE PRODSEC@NOZOMINETWORKS \n")
print("     -      EN "+str(hq_iot_2022)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES ICS-CERT@HQ.DHS.GOV \n")
print("     -      EN "+str(kaspersky_iot_2022)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES VULNERABILITY@KASPERSKY \n")
print("     -      EN "+str(schneider_iot_2022)+" VULNERABILIDADES EL ASIGNADOR DE CVE CYBERSECURITY@SCHNEIDER-ELECTRIC \n")
print("     -      EN "+str(apple_iot_2022)+" VULNERABILIDADES EL ASIGNADOR DE CVE PRODUCT-SECURITY@APPLE \n")
print("     -      EN "+str(android_iot_2022)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY@ANDROID \n")
print("     -      EN "+str(bitdefender_iot_2022)+" VULNERABILIDADES EL ASIGNADOR DE CVE CVE-REQUESTS@BITDEFENDER \n")
print("     -      EN "+str(mcafee_iot_2022)+" VULNERABILIDADES EL ASIGNADOR DE CVE PSIRT@MCAFEE \n")
print("     -      EN "+str(mozilla_iot_2022)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY@MOZILLA \n")
print("     -      EN "+str(hpe_iot_2022)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY-ALERT@HPE \n")
print("     -      EN "+str(fsecure_iot_2022)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES CVE-NOTIFICATIONS-US@F-SECURE.COM \n")
print("     -      EN "+str(rapid7_iot_2022)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES CVE@RAPID7 \n")
print("     -      EN "+str(other_assigner_iot_2022)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES DISTINTO DE LOS ANTERIORES \n")
print("\n")
print("\n")
print(" DE UN TOTAL DE "+str(assigner_iot_2021)+" VULNERABILIDADES PUBLICADAS EN 2021, LAS ESTADÍSTICAS DE ASIGNADORES CVE SON LAS SIGUIENTES : \n")
print("     -      EN "+str(jpcert_iot_2021)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES VULTURES@JPCERT\n")
print("     -      EN "+str(mitre_iot_2021)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES CVE@MITRE \n")
print("     -      EN "+str(cisco_iot_2021)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES TALOS-CNA@CISCO \n")
print("     -      EN "+str(github_iot_2021)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY-ADVISORIES@GITHUB \n")
print("     -      EN "+str(redhat_iot_2021)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES SECALERT@REDHAT \n")
print("     -      EN "+str(qualcomm_iot_2021)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY.CNA@QUALCOMM \n")
print("     -      EN "+str(apache_iot_2021)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY@APACHE.ORG \n")
print("     -      EN "+str(oracle_iot_2021)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES SECALERT_US@ORACLE \n")
print("     -      EN "+str(microsoft_iot_2021)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURE@MICROSOFT \n")
print("     -      EN "+str(cert_iot_2021)+" VULNERABILIDADES EL ASIGNADOR DE CVE INFO@CERT.VDE \n")
print("     -      EN "+str(trendmicro_iot_2021)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY@TRENDMICRO \n")
print("     -      EN "+str(nozomi_iot_2021)+" VULNERABILIDADES EL ASIGNADOR DE CVE PRODSEC@NOZOMINETWORKS \n")
print("     -      EN "+str(hq_iot_2021)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES ICS-CERT@HQ.DHS.GOV \n")
print("     -      EN "+str(kaspersky_iot_2021)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES VULNERABILITY@KASPERSKY \n")
print("     -      EN "+str(schneider_iot_2021)+" VULNERABILIDADES EL ASIGNADOR DE CVE CYBERSECURITY@SCHNEIDER-ELECTRIC \n")
print("     -      EN "+str(apple_iot_2021)+" VULNERABILIDADES EL ASIGNADOR DE CVE PRODUCT-SECURITY@APPLE \n")
print("     -      EN "+str(android_iot_2021)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY@ANDROID \n")
print("     -      EN "+str(bitdefender_iot_2021)+" VULNERABILIDADES EL ASIGNADOR DE CVE CVE-REQUESTS@BITDEFENDER \n")
print("     -      EN "+str(mcafee_iot_2021)+" VULNERABILIDADES EL ASIGNADOR DE CVE PSIRT@MCAFEE \n")
print("     -      EN "+str(mozilla_iot_2021)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY@MOZILLA \n")
print("     -      EN "+str(hpe_iot_2021)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY-ALERT@HPE \n")
print("     -      EN "+str(fsecure_iot_2021)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES CVE-NOTIFICATIONS-US@F-SECURE.COM \n")
print("     -      EN "+str(rapid7_iot_2021)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES CVE@RAPID7 \n")
print("     -      EN "+str(other_assigner_iot_2021)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES DISTINTO DE LOS ANTERIORES \n")
print("\n")
print("\n")
print(" DE UN TOTAL DE "+str(assigner_iot_2020)+" VULNERABILIDADES PUBLICADAS EN 2020, LAS ESTADÍSTICAS DE ASIGNADORES CVE SON LAS SIGUIENTES : \n")
print("     -      EN "+str(jpcert_iot_2020)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES VULTURES@JPCERT\n")
print("     -      EN "+str(mitre_iot_2020)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES CVE@MITRE \n")
print("     -      EN "+str(cisco_iot_2020)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES TALOS-CNA@CISCO \n")
print("     -      EN "+str(github_iot_2020)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY-ADVISORIES@GITHUB \n")
print("     -      EN "+str(redhat_iot_2020)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES SECALERT@REDHAT \n")
print("     -      EN "+str(qualcomm_iot_2020)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY.CNA@QUALCOMM \n")
print("     -      EN "+str(apache_iot_2020)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY@APACHE.ORG \n")
print("     -      EN "+str(oracle_iot_2020)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES SECALERT_US@ORACLE \n")
print("     -      EN "+str(microsoft_iot_2020)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURE@MICROSOFT \n")
print("     -      EN "+str(cert_iot_2020)+" VULNERABILIDADES EL ASIGNADOR DE CVE INFO@CERT.VDE \n")
print("     -      EN "+str(trendmicro_iot_2020)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY@TRENDMICRO \n")
print("     -      EN "+str(nozomi_iot_2020)+" VULNERABILIDADES EL ASIGNADOR DE CVE PRODSEC@NOZOMINETWORKS \n")
print("     -      EN "+str(hq_iot_2020)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES ICS-CERT@HQ.DHS.GOV \n")
print("     -      EN "+str(kaspersky_iot_2020)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES VULNERABILITY@KASPERSKY \n")
print("     -      EN "+str(schneider_iot_2020)+" VULNERABILIDADES EL ASIGNADOR DE CVE CYBERSECURITY@SCHNEIDER-ELECTRIC \n")
print("     -      EN "+str(apple_iot_2020)+" VULNERABILIDADES EL ASIGNADOR DE CVE PRODUCT-SECURITY@APPLE \n")
print("     -      EN "+str(android_iot_2020)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY@ANDROID \n")
print("     -      EN "+str(bitdefender_iot_2020)+" VULNERABILIDADES EL ASIGNADOR DE CVE CVE-REQUESTS@BITDEFENDER \n")
print("     -      EN "+str(mcafee_iot_2020)+" VULNERABILIDADES EL ASIGNADOR DE CVE PSIRT@MCAFEE \n")
print("     -      EN "+str(mozilla_iot_2020)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY@MOZILLA \n")
print("     -      EN "+str(hpe_iot_2020)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY-ALERT@HPE \n")
print("     -      EN "+str(fsecure_iot_2020)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES CVE-NOTIFICATIONS-US@F-SECURE.COM \n")
print("     -      EN "+str(rapid7_iot_2020)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES CVE@RAPID7 \n")
print("     -      EN "+str(other_assigner_iot_2020)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES DISTINTO DE LOS ANTERIORES \n")
print("\n")
print("\n")
print(" DE UN TOTAL DE "+str(assigner_iot_2019)+" VULNERABILIDADES PUBLICADAS EN 2019, LAS ESTADÍSTICAS DE ASIGNADORES CVE SON LAS SIGUIENTES : \n")
print("     -      EN "+str(jpcert_iot_2019)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES VULTURES@JPCERT\n")
print("     -      EN "+str(mitre_iot_2019)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES CVE@MITRE \n")
print("     -      EN "+str(cisco_iot_2019)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES TALOS-CNA@CISCO \n")
print("     -      EN "+str(github_iot_2019)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY-ADVISORIES@GITHUB \n")
print("     -      EN "+str(redhat_iot_2019)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES SECALERT@REDHAT \n")
print("     -      EN "+str(qualcomm_iot_2019)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY.CNA@QUALCOMM \n")
print("     -      EN "+str(apache_iot_2019)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY@APACHE.ORG \n")
print("     -      EN "+str(oracle_iot_2019)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES SECALERT_US@ORACLE \n")
print("     -      EN "+str(microsoft_iot_2019)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURE@MICROSOFT \n")
print("     -      EN "+str(cert_iot_2019)+" VULNERABILIDADES EL ASIGNADOR DE CVE INFO@CERT.VDE \n")
print("     -      EN "+str(trendmicro_iot_2019)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY@TRENDMICRO \n")
print("     -      EN "+str(nozomi_iot_2019)+" VULNERABILIDADES EL ASIGNADOR DE CVE PRODSEC@NOZOMINETWORKS \n")
print("     -      EN "+str(hq_iot_2019)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES ICS-CERT@HQ.DHS.GOV \n")
print("     -      EN "+str(kaspersky_iot_2019)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES VULNERABILITY@KASPERSKY \n")
print("     -      EN "+str(schneider_iot_2019)+" VULNERABILIDADES EL ASIGNADOR DE CVE CYBERSECURITY@SCHNEIDER-ELECTRIC \n")
print("     -      EN "+str(apple_iot_2019)+" VULNERABILIDADES EL ASIGNADOR DE CVE PRODUCT-SECURITY@APPLE \n")
print("     -      EN "+str(android_iot_2019)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY@ANDROID \n")
print("     -      EN "+str(bitdefender_iot_2019)+" VULNERABILIDADES EL ASIGNADOR DE CVE CVE-REQUESTS@BITDEFENDER \n")
print("     -      EN "+str(mcafee_iot_2019)+" VULNERABILIDADES EL ASIGNADOR DE CVE PSIRT@MCAFEE \n")
print("     -      EN "+str(mozilla_iot_2019)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY@MOZILLA \n")
print("     -      EN "+str(hpe_iot_2019)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY-ALERT@HPE \n")
print("     -      EN "+str(fsecure_iot_2019)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES CVE-NOTIFICATIONS-US@F-SECURE.COM \n")
print("     -      EN "+str(rapid7_iot_2019)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES CVE@RAPID7 \n")
print("     -      EN "+str(other_assigner_iot_2019)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES DISTINTO DE LOS ANTERIORES \n")
print("\n")
print("\n")
print(" DE UN TOTAL DE "+str(assigner_iot_2018)+" VULNERABILIDADES PUBLICADAS EN 2018 O ANTERIORMENTE, LAS ESTADÍSTICAS DE ASIGNADORES CVE SON LAS SIGUIENTES : \n")
print("     -      EN "+str(jpcert_iot_2018)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES VULTURES@JPCERT\n")
print("     -      EN "+str(mitre_iot_2018)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES CVE@MITRE \n")
print("     -      EN "+str(cisco_iot_2018)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES TALOS-CNA@CISCO \n")
print("     -      EN "+str(github_iot_2018)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY-ADVISORIES@GITHUB \n")
print("     -      EN "+str(redhat_iot_2018)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES SECALERT@REDHAT \n")
print("     -      EN "+str(qualcomm_iot_2018)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY.CNA@QUALCOMM \n")
print("     -      EN "+str(apache_iot_2018)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY@APACHE.ORG \n")
print("     -      EN "+str(oracle_iot_2018)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES SECALERT_US@ORACLE \n")
print("     -      EN "+str(microsoft_iot_2018)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURE@MICROSOFT \n")
print("     -      EN "+str(cert_iot_2018)+" VULNERABILIDADES EL ASIGNADOR DE CVE INFO@CERT.VDE \n")
print("     -      EN "+str(trendmicro_iot_2018)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY@TRENDMICRO \n")
print("     -      EN "+str(nozomi_iot_2018)+" VULNERABILIDADES EL ASIGNADOR DE CVE PRODSEC@NOZOMINETWORKS \n")
print("     -      EN "+str(hq_iot_2018)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES ICS-CERT@HQ.DHS.GOV \n")
print("     -      EN "+str(kaspersky_iot_2018)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES VULNERABILITY@KASPERSKY \n")
print("     -      EN "+str(schneider_iot_2018)+" VULNERABILIDADES EL ASIGNADOR DE CVE CYBERSECURITY@SCHNEIDER-ELECTRIC \n")
print("     -      EN "+str(apple_iot_2018)+" VULNERABILIDADES EL ASIGNADOR DE CVE PRODUCT-SECURITY@APPLE \n")
print("     -      EN "+str(android_iot_2018)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY@ANDROID \n")
print("     -      EN "+str(bitdefender_iot_2018)+" VULNERABILIDADES EL ASIGNADOR DE CVE CVE-REQUESTS@BITDEFENDER \n")
print("     -      EN "+str(mcafee_iot_2018)+" VULNERABILIDADES EL ASIGNADOR DE CVE PSIRT@MCAFEE \n")
print("     -      EN "+str(mozilla_iot_2018)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY@MOZILLA \n")
print("     -      EN "+str(hpe_iot_2018)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY-ALERT@HPE \n")
print("     -      EN "+str(fsecure_iot_2018)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES CVE-NOTIFICATIONS-US@F-SECURE.COM \n")
print("     -      EN "+str(rapid7_iot_2018)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES CVE@RAPID7 \n")
print("     -      EN "+str(other_assigner_iot_2018)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES DISTINTO DE LOS ANTERIORES \n")
print("\n")



print("************************** ESTADÍSTICAS ASIGNADOR CVE SEGÚN FECHA DE PUBLICACIÓN PARTE IOT********************************")
print("\n")
print("\n")
print(" DE UN TOTAL DE "+str(total_assigner_iot)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ESTÁ DEFINIDO, LAS ESTADÍSTICAS DE ASSIGNER SEGUN FECHA DE PUBLICACION SON LAS SIGUIENTES  : \n")
print("\n")
print("  -  EN  "+str(jpcert_iot)+" VULNERABILIDADES DONDE EL ASIGNADOR ES VULTURES@JPCERT, LAS ESTADÍSTICAS SEGUN FECHA DE PUBLICACION SON LAS SIGUIENTES : \n")
print("     -      UN TOTAL DE "+str(jpcert_iot_2023)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES VULTURES@JPCERT, FUERON PUBLICADAS EN 2023 \n")
print("     -      UN TOTAL DE "+str(jpcert_iot_2022)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES VULTURES@JPCERT, FUERON PUBLICADAS EN 2022 \n")
print("     -      UN TOTAL DE "+str(jpcert_iot_2021)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES VULTURES@JPCERT, FUERON PUBLICADAS EN 2021 \n")
print("     -      UN TOTAL DE "+str(jpcert_iot_2020)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES VULTURES@JPCERT, FUERON PUBLICADAS EN 2020 \n")
print("     -      UN TOTAL DE "+str(jpcert_iot_2019)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES VULTURES@JPCERT, FUERON PUBLICADAS EN 2019 \n")
print("     -      UN TOTAL DE "+str(jpcert_iot_2018)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES VULTURES@JPCERT, FUERON PUBLICADAS EN 2018 O ANTERIORMENTE \n")
print("\n")
print("  -  EN  "+str(mitre_iot)+" VULNERABILIDADES DONDE EL ASIGNADOR ES CVE@MITRE, LAS ESTADÍSTICAS SEGUN FECHA DE PUBLICACION SON LAS SIGUIENTES : \n")
print("     -      UN TOTAL DE "+str(mitre_iot_2023)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES CVE@MITRE, FUERON PUBLICADAS EN 2023 \n")
print("     -      UN TOTAL DE "+str(mitre_iot_2022)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES CVE@MITRE, FUERON PUBLICADAS EN 2022 \n")
print("     -      UN TOTAL DE "+str(mitre_iot_2021)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES CVE@MITRE, FUERON PUBLICADAS EN 2021 \n")
print("     -      UN TOTAL DE "+str(mitre_iot_2020)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES CVE@MITRE, FUERON PUBLICADAS EN 2020 \n")
print("     -      UN TOTAL DE "+str(mitre_iot_2019)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES CVE@MITRE, FUERON PUBLICADAS EN 2019 \n")
print("     -      UN TOTAL DE "+str(mitre_iot_2018)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES CVE@MITRE, FUERON PUBLICADAS EN 2018 O ANTERIORMENTE \n")
print("\n")
print("  -  EN  "+str(cisco_iot)+" VULNERABILIDADES DONDE EL ASIGNADOR ES TALOS-CNA@CISCO, LAS ESTADÍSTICAS SEGUN FECHA DE PUBLICACION SON LAS SIGUIENTES : \n")
print("     -      UN TOTAL DE "+str(cisco_iot_2023)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES TALOS-CNA@CISCO, FUERON PUBLICADAS EN 2023 \n")
print("     -      UN TOTAL DE "+str(cisco_iot_2022)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES TALOS-CNA@CISCO, FUERON PUBLICADAS EN 2022 \n")
print("     -      UN TOTAL DE "+str(cisco_iot_2021)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES TALOS-CNA@CISCO, FUERON PUBLICADAS EN 2021 \n")
print("     -      UN TOTAL DE "+str(cisco_iot_2020)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES TALOS-CNA@CISCO, FUERON PUBLICADAS EN 2020 \n")
print("     -      UN TOTAL DE "+str(cisco_iot_2019)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES TALOS-CNA@CISCO, FUERON PUBLICADAS EN 2019 \n")
print("     -      UN TOTAL DE "+str(cisco_iot_2018)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES TALOS-CNA@CISCO, FUERON PUBLICADAS EN 2018 O ANTERIORMENTE \n")
print("\n")
print("  -  EN  "+str(github_iot)+" VULNERABILIDADES DONDE EL ASIGNADOR ES SECURITY-ADVISORIES@GITHUB, LAS ESTADÍSTICAS SEGUN FECHA DE PUBLICACION SON LAS SIGUIENTES : \n")
print("     -      UN TOTAL DE "+str(github_iot_2023)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY-ADVISORIES@GITHUB, FUERON PUBLICADAS EN 2023 \n")
print("     -      UN TOTAL DE "+str(github_iot_2022)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY-ADVISORIES@GITHUB, FUERON PUBLICADAS EN 2022 \n")
print("     -      UN TOTAL DE "+str(github_iot_2021)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY-ADVISORIES@GITHUB, FUERON PUBLICADAS EN 2021 \n")
print("     -      UN TOTAL DE "+str(github_iot_2020)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY-ADVISORIES@GITHUB, FUERON PUBLICADAS EN 2020 \n")
print("     -      UN TOTAL DE "+str(github_iot_2019)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY-ADVISORIES@GITHUB, FUERON PUBLICADAS EN 2019 \n")
print("     -      UN TOTAL DE "+str(github_iot_2018)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY-ADVISORIES@GITHUB, FUERON PUBLICADAS EN 2018 O ANTERIORMENTE \n")
print("\n")
print("  -  EN  "+str(redhat_iot)+" VULNERABILIDADES DONDE EL ASIGNADOR ES SECALERT@REDHAT, LAS ESTADÍSTICAS SEGUN FECHA DE PUBLICACION SON LAS SIGUIENTES : \n")
print("     -      UN TOTAL DE "+str(redhat_iot_2023)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECALERT@REDHAT, FUERON PUBLICADAS EN 2023 \n")
print("     -      UN TOTAL DE "+str(redhat_iot_2022)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECALERT@REDHAT, FUERON PUBLICADAS EN 2022 \n")
print("     -      UN TOTAL DE "+str(redhat_iot_2021)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECALERT@REDHAT, FUERON PUBLICADAS EN 2021 \n")
print("     -      UN TOTAL DE "+str(redhat_iot_2020)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECALERT@REDHAT, FUERON PUBLICADAS EN 2020 \n")
print("     -      UN TOTAL DE "+str(redhat_iot_2019)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECALERT@REDHAT, FUERON PUBLICADAS EN 2019 \n")
print("     -      UN TOTAL DE "+str(redhat_iot_2018)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECALERT@REDHAT, FUERON PUBLICADAS EN 2018 O ANTERIORMENTE \n")
print("\n")
print("  -  EN  "+str(qualcomm_iot)+" VULNERABILIDADES DONDE EL ASIGNADOR ES SECURITY.CNA@QUALCOMM, LAS ESTADÍSTICAS SEGUN FECHA DE PUBLICACION SON LAS SIGUIENTES : \n")
print("     -      UN TOTAL DE "+str(qualcomm_iot_2023)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY.CNA@QUALCOMM, FUERON PUBLICADAS EN 2023 \n")
print("     -      UN TOTAL DE "+str(qualcomm_iot_2022)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY.CNA@QUALCOMM, FUERON PUBLICADAS EN 2022 \n")
print("     -      UN TOTAL DE "+str(qualcomm_iot_2021)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY.CNA@QUALCOMM, FUERON PUBLICADAS EN 2021 \n")
print("     -      UN TOTAL DE "+str(qualcomm_iot_2020)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY.CNA@QUALCOMM, FUERON PUBLICADAS EN 2020 \n")
print("     -      UN TOTAL DE "+str(qualcomm_iot_2019)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY.CNA@QUALCOMM, FUERON PUBLICADAS EN 2019 \n")
print("     -      UN TOTAL DE "+str(qualcomm_iot_2018)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY.CNA@QUALCOMM, FUERON PUBLICADAS EN 2018 O ANTERIORMENTE \n")
print("\n")
print("  -  EN  "+str(apache_iot)+" VULNERABILIDADES DONDE EL ASIGNADOR ES SECURITY@APACHE.ORG, LAS ESTADÍSTICAS SEGUN FECHA DE PUBLICACION SON LAS SIGUIENTES : \n")
print("     -      UN TOTAL DE "+str(apache_iot_2023)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY@APACHE.ORG, FUERON PUBLICADAS EN 2023 \n")
print("     -      UN TOTAL DE "+str(apache_iot_2022)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY@APACHE.ORG, FUERON PUBLICADAS EN 2022 \n")
print("     -      UN TOTAL DE "+str(apache_iot_2021)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY@APACHE.ORG, FUERON PUBLICADAS EN 2021 \n")
print("     -      UN TOTAL DE "+str(apache_iot_2020)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY@APACHE.ORG, FUERON PUBLICADAS EN 2020 \n")
print("     -      UN TOTAL DE "+str(apache_iot_2019)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY@APACHE.ORG, FUERON PUBLICADAS EN 2019 \n")
print("     -      UN TOTAL DE "+str(apache_iot_2018)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY@APACHE.ORG, FUERON PUBLICADAS EN 2018 O ANTERIORMENTE \n")
print("\n")
print("  -  EN  "+str(oracle_iot)+" VULNERABILIDADES DONDE EL ASIGNADOR ES SECALERT_US@ORACLE, LAS ESTADÍSTICAS SEGUN FECHA DE PUBLICACION SON LAS SIGUIENTES : \n")
print("     -      UN TOTAL DE "+str(oracle_iot_2023)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECALERT_US@ORACLE, FUERON PUBLICADAS EN 2023 \n")
print("     -      UN TOTAL DE "+str(oracle_iot_2022)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECALERT_US@ORACLE, FUERON PUBLICADAS EN 2022 \n")
print("     -      UN TOTAL DE "+str(oracle_iot_2021)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECALERT_US@ORACLE, FUERON PUBLICADAS EN 2021 \n")
print("     -      UN TOTAL DE "+str(oracle_iot_2020)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECALERT_US@ORACLE, FUERON PUBLICADAS EN 2020 \n")
print("     -      UN TOTAL DE "+str(oracle_iot_2019)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECALERT_US@ORACLE, FUERON PUBLICADAS EN 2019 \n")
print("     -      UN TOTAL DE "+str(oracle_iot_2018)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECALERT_US@ORACLE, FUERON PUBLICADAS EN 2018 O ANTERIORMENTE \n")
print("\n")
print("  -  EN  "+str(microsoft_iot)+" VULNERABILIDADES DONDE EL ASIGNADOR ES SECURE@MICROSOFT, LAS ESTADÍSTICAS SEGUN FECHA DE PUBLICACION SON LAS SIGUIENTES : \n")
print("     -      UN TOTAL DE "+str(microsoft_iot_2023)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURE@MICROSOFT, FUERON PUBLICADAS EN 2023 \n")
print("     -      UN TOTAL DE "+str(microsoft_iot_2022)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURE@MICROSOFT, FUERON PUBLICADAS EN 2022 \n")
print("     -      UN TOTAL DE "+str(microsoft_iot_2021)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURE@MICROSOFT, FUERON PUBLICADAS EN 2021 \n")
print("     -      UN TOTAL DE "+str(microsoft_iot_2020)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURE@MICROSOFT, FUERON PUBLICADAS EN 2020 \n")
print("     -      UN TOTAL DE "+str(microsoft_iot_2019)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURE@MICROSOFT, FUERON PUBLICADAS EN 2019 \n")
print("     -      UN TOTAL DE "+str(microsoft_iot_2018)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURE@MICROSOFT, FUERON PUBLICADAS EN 2018 O ANTERIORMENTE \n")
print("\n")
print("  -  EN  "+str(cert_iot)+" VULNERABILIDADES DONDE EL ASIGNADOR ES INFO@CERT.VDE, LAS ESTADÍSTICAS SEGUN FECHA DE PUBLICACION SON LAS SIGUIENTES : \n")
print("     -      UN TOTAL DE "+str(cert_iot_2023)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES INFO@CERT.VDE, FUERON PUBLICADAS EN 2023 \n")
print("     -      UN TOTAL DE "+str(cert_iot_2022)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES INFO@CERT.VDE, FUERON PUBLICADAS EN 2022 \n")
print("     -      UN TOTAL DE "+str(cert_iot_2021)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES INFO@CERT.VDE, FUERON PUBLICADAS EN 2021 \n")
print("     -      UN TOTAL DE "+str(cert_iot_2020)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES INFO@CERT.VDE, FUERON PUBLICADAS EN 2020 \n")
print("     -      UN TOTAL DE "+str(cert_iot_2019)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES INFO@CERT.VDE, FUERON PUBLICADAS EN 2019 \n")
print("     -      UN TOTAL DE "+str(cert_iot_2018)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES INFO@CERT.VDE, FUERON PUBLICADAS EN 2018 O ANTERIORMENTE \n")
print("\n")
print("  -  EN  "+str(trendmicro_iot)+" VULNERABILIDADES DONDE EL ASIGNADOR ES SECURITY@TRENDMICRO, LAS ESTADÍSTICAS SEGUN FECHA DE PUBLICACION SON LAS SIGUIENTES : \n")
print("     -      UN TOTAL DE "+str(trendmicro_iot_2023)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY@TRENDMICRO, FUERON PUBLICADAS EN 2023 \n")
print("     -      UN TOTAL DE "+str(trendmicro_iot_2022)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY@TRENDMICRO, FUERON PUBLICADAS EN 2022 \n")
print("     -      UN TOTAL DE "+str(trendmicro_iot_2021)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY@TRENDMICRO, FUERON PUBLICADAS EN 2021 \n")
print("     -      UN TOTAL DE "+str(trendmicro_iot_2020)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY@TRENDMICRO, FUERON PUBLICADAS EN 2020 \n")
print("     -      UN TOTAL DE "+str(trendmicro_iot_2019)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY@TRENDMICRO, FUERON PUBLICADAS EN 2019 \n")
print("     -      UN TOTAL DE "+str(trendmicro_iot_2018)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY@TRENDMICRO, FUERON PUBLICADAS EN 2018 O ANTERIORMENTE \n")
print("\n")
print("  -  EN  "+str(nozomi_iot)+" VULNERABILIDADES DONDE EL ASIGNADOR ES PRODSEC@NOZOMINETWORKS, LAS ESTADÍSTICAS SEGUN FECHA DE PUBLICACION SON LAS SIGUIENTES : \n")
print("     -      UN TOTAL DE "+str(nozomi_iot_2023)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES PRODSEC@NOZOMINETWORKS, FUERON PUBLICADAS EN 2023 \n")
print("     -      UN TOTAL DE "+str(nozomi_iot_2022)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES PRODSEC@NOZOMINETWORKS, FUERON PUBLICADAS EN 2022 \n")
print("     -      UN TOTAL DE "+str(nozomi_iot_2021)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES PRODSEC@NOZOMINETWORKS, FUERON PUBLICADAS EN 2021 \n")
print("     -      UN TOTAL DE "+str(nozomi_iot_2020)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES PRODSEC@NOZOMINETWORKS, FUERON PUBLICADAS EN 2020 \n")
print("     -      UN TOTAL DE "+str(nozomi_iot_2019)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES PRODSEC@NOZOMINETWORKS, FUERON PUBLICADAS EN 2019 \n")
print("     -      UN TOTAL DE "+str(nozomi_iot_2018)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES PRODSEC@NOZOMINETWORKS, FUERON PUBLICADAS EN 2018 O ANTERIORMENTE \n")
print("\n")
print("  -  EN  "+str(hq_iot)+" VULNERABILIDADES DONDE EL ASIGNADOR ES ICS-CERT@HQ.DHS.GOV, LAS ESTADÍSTICAS SEGUN FECHA DE PUBLICACION SON LAS SIGUIENTES : \n")
print("     -      UN TOTAL DE "+str(hq_iot_2023)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES ICS-CERT@HQ.DHS.GOV, FUERON PUBLICADAS EN 2023 \n")
print("     -      UN TOTAL DE "+str(hq_iot_2022)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES ICS-CERT@HQ.DHS.GOV, FUERON PUBLICADAS EN 2022 \n")
print("     -      UN TOTAL DE "+str(hq_iot_2021)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES ICS-CERT@HQ.DHS.GOV, FUERON PUBLICADAS EN 2021 \n")
print("     -      UN TOTAL DE "+str(hq_iot_2020)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES ICS-CERT@HQ.DHS.GOV, FUERON PUBLICADAS EN 2020 \n")
print("     -      UN TOTAL DE "+str(hq_iot_2019)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES ICS-CERT@HQ.DHS.GOV, FUERON PUBLICADAS EN 2019 \n")
print("     -      UN TOTAL DE "+str(hq_iot_2018)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES ICS-CERT@HQ.DHS.GOV, FUERON PUBLICADAS EN 2018 O ANTERIORMENTE \n")
print("\n")
print("  -  EN  "+str(kaspersky_iot)+" VULNERABILIDADES DONDE EL ASIGNADOR ES VULNERABILITY@KASPERSKY, LAS ESTADÍSTICAS SEGUN FECHA DE PUBLICACION SON LAS SIGUIENTES : \n")
print("     -      UN TOTAL DE "+str(kaspersky_iot_2023)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES VULNERABILITY@KASPERSKY, FUERON PUBLICADAS EN 2023 \n")
print("     -      UN TOTAL DE "+str(kaspersky_iot_2022)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES VULNERABILITY@KASPERSKY, FUERON PUBLICADAS EN 2022 \n")
print("     -      UN TOTAL DE "+str(kaspersky_iot_2021)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES VULNERABILITY@KASPERSKY, FUERON PUBLICADAS EN 2021 \n")
print("     -      UN TOTAL DE "+str(kaspersky_iot_2020)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES VULNERABILITY@KASPERSKY, FUERON PUBLICADAS EN 2020 \n")
print("     -      UN TOTAL DE "+str(kaspersky_iot_2019)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES VULNERABILITY@KASPERSKY, FUERON PUBLICADAS EN 2019 \n")
print("     -      UN TOTAL DE "+str(kaspersky_iot_2018)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES VULNERABILITY@KASPERSKY, FUERON PUBLICADAS EN 2018 O ANTERIORMENTE \n")
print("\n")
print("  -  EN  "+str(schneider_iot)+" VULNERABILIDADES DONDE EL ASIGNADOR ES CYBERSECURITY@SCHNEIDER-ELECTRIC, LAS ESTADÍSTICAS SEGUN FECHA DE PUBLICACION SON LAS SIGUIENTES : \n")
print("     -      UN TOTAL DE "+str(schneider_iot_2023)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES CYBERSECURITY@SCHNEIDER-ELECTRIC, FUERON PUBLICADAS EN 2023 \n")
print("     -      UN TOTAL DE "+str(schneider_iot_2022)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES CYBERSECURITY@SCHNEIDER-ELECTRIC, FUERON PUBLICADAS EN 2022 \n")
print("     -      UN TOTAL DE "+str(schneider_iot_2021)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES CYBERSECURITY@SCHNEIDER-ELECTRIC, FUERON PUBLICADAS EN 2021 \n")
print("     -      UN TOTAL DE "+str(schneider_iot_2020)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES CYBERSECURITY@SCHNEIDER-ELECTRIC, FUERON PUBLICADAS EN 2020 \n")
print("     -      UN TOTAL DE "+str(schneider_iot_2019)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES CYBERSECURITY@SCHNEIDER-ELECTRIC, FUERON PUBLICADAS EN 2019 \n")
print("     -      UN TOTAL DE "+str(schneider_iot_2018)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES CYBERSECURITY@SCHNEIDER-ELECTRIC, FUERON PUBLICADAS EN 2018 O ANTERIORMENTE \n")
print("\n")
print("  -  EN  "+str(apple_iot)+" VULNERABILIDADES DONDE EL ASIGNADOR ES PRODUCT-SECURITY@APPLE, LAS ESTADÍSTICAS SEGUN FECHA DE PUBLICACION SON LAS SIGUIENTES : \n")
print("     -      UN TOTAL DE "+str(apple_iot_2023)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES PRODUCT-SECURITY@APPLE, FUERON PUBLICADAS EN 2023 \n")
print("     -      UN TOTAL DE "+str(apple_iot_2022)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES PRODUCT-SECURITY@APPLE, FUERON PUBLICADAS EN 2022 \n")
print("     -      UN TOTAL DE "+str(apple_iot_2021)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES PRODUCT-SECURITY@APPLE, FUERON PUBLICADAS EN 2021 \n")
print("     -      UN TOTAL DE "+str(apple_iot_2020)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES PRODUCT-SECURITY@APPLE, FUERON PUBLICADAS EN 2020 \n")
print("     -      UN TOTAL DE "+str(apple_iot_2019)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES PRODUCT-SECURITY@APPLE, FUERON PUBLICADAS EN 2019 \n")
print("     -      UN TOTAL DE "+str(apple_iot_2018)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES PRODUCT-SECURITY@APPLE, FUERON PUBLICADAS EN 2018 O ANTERIORMENTE \n")
print("\n")
print("  -  EN  "+str(android_iot)+" VULNERABILIDADES DONDE EL ASIGNADOR ES SECURITY@ANDROID, LAS ESTADÍSTICAS SEGUN FECHA DE PUBLICACION SON LAS SIGUIENTES : \n")
print("     -      UN TOTAL DE "+str(android_iot_2023)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY@ANDROID, FUERON PUBLICADAS EN 2023 \n")
print("     -      UN TOTAL DE "+str(android_iot_2022)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY@ANDROID, FUERON PUBLICADAS EN 2022 \n")
print("     -      UN TOTAL DE "+str(android_iot_2021)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY@ANDROID, FUERON PUBLICADAS EN 2021 \n")
print("     -      UN TOTAL DE "+str(android_iot_2020)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY@ANDROID, FUERON PUBLICADAS EN 2020 \n")
print("     -      UN TOTAL DE "+str(android_iot_2019)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY@ANDROID, FUERON PUBLICADAS EN 2019 \n")
print("     -      UN TOTAL DE "+str(android_iot_2018)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY@ANDROID, FUERON PUBLICADAS EN 2018 O ANTERIORMENTE \n")
print("\n")
print("  -  EN  "+str(bitdefender_iot)+" VULNERABILIDADES DONDE EL ASIGNADOR ES CVE-REQUESTS@BITDEFENDER, LAS ESTADÍSTICAS SEGUN FECHA DE PUBLICACION SON LAS SIGUIENTES : \n")
print("     -      UN TOTAL DE "+str(bitdefender_iot_2023)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES CVE-REQUESTS@BITDEFENDER, FUERON PUBLICADAS EN 2023 \n")
print("     -      UN TOTAL DE "+str(bitdefender_iot_2022)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES CVE-REQUESTS@BITDEFENDER, FUERON PUBLICADAS EN 2022 \n")
print("     -      UN TOTAL DE "+str(bitdefender_iot_2021)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES CVE-REQUESTS@BITDEFENDER, FUERON PUBLICADAS EN 2021 \n")
print("     -      UN TOTAL DE "+str(bitdefender_iot_2020)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES CVE-REQUESTS@BITDEFENDER, FUERON PUBLICADAS EN 2020 \n")
print("     -      UN TOTAL DE "+str(bitdefender_iot_2019)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES CVE-REQUESTS@BITDEFENDER, FUERON PUBLICADAS EN 2019 \n")
print("     -      UN TOTAL DE "+str(bitdefender_iot_2018)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES CVE-REQUESTS@BITDEFENDER, FUERON PUBLICADAS EN 2018 O ANTERIORMENTE \n")
print("\n")
print("  -  EN  "+str(mcafee_iot)+" VULNERABILIDADES DONDE EL ASIGNADOR ES PSIRT@MCAFEE, LAS ESTADÍSTICAS SEGUN FECHA DE PUBLICACION SON LAS SIGUIENTES : \n")
print("     -      UN TOTAL DE "+str(mcafee_iot_2023)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES PSIRT@MCAFEE, FUERON PUBLICADAS EN 2023 \n")
print("     -      UN TOTAL DE "+str(mcafee_iot_2022)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES PSIRT@MCAFEE, FUERON PUBLICADAS EN 2022 \n")
print("     -      UN TOTAL DE "+str(mcafee_iot_2021)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES PSIRT@MCAFEE, FUERON PUBLICADAS EN 2021 \n")
print("     -      UN TOTAL DE "+str(mcafee_iot_2020)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES PSIRT@MCAFEE, FUERON PUBLICADAS EN 2020 \n")
print("     -      UN TOTAL DE "+str(mcafee_iot_2019)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES PSIRT@MCAFEE, FUERON PUBLICADAS EN 2019 \n")
print("     -      UN TOTAL DE "+str(mcafee_iot_2018)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES PSIRT@MCAFEE, FUERON PUBLICADAS EN 2018 O ANTERIORMENTE \n")
print("\n")
print("  -  EN  "+str(mozilla_iot)+" VULNERABILIDADES DONDE EL ASIGNADOR ES SECURITY@MOZILLA, LAS ESTADÍSTICAS SEGUN FECHA DE PUBLICACION SON LAS SIGUIENTES : \n")
print("     -      UN TOTAL DE "+str(mozilla_iot_2023)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY@MOZILLA, FUERON PUBLICADAS EN 2023 \n")
print("     -      UN TOTAL DE "+str(mozilla_iot_2022)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY@MOZILLA, FUERON PUBLICADAS EN 2022 \n")
print("     -      UN TOTAL DE "+str(mozilla_iot_2021)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY@MOZILLA, FUERON PUBLICADAS EN 2021 \n")
print("     -      UN TOTAL DE "+str(mozilla_iot_2020)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY@MOZILLA, FUERON PUBLICADAS EN 2020 \n")
print("     -      UN TOTAL DE "+str(mozilla_iot_2019)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY@MOZILLA, FUERON PUBLICADAS EN 2019 \n")
print("     -      UN TOTAL DE "+str(mozilla_iot_2018)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY@MOZILLA, FUERON PUBLICADAS EN 2018 O ANTERIORMENTE \n")
print("\n")
print("  -  EN  "+str(hpe_iot)+" VULNERABILIDADES DONDE EL ASIGNADOR ES SECURITY-ALERT@HPE, LAS ESTADÍSTICAS SEGUN FECHA DE PUBLICACION SON LAS SIGUIENTES : \n")
print("     -      UN TOTAL DE "+str(hpe_iot_2023)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY-ADVISORIES@HPE, FUERON PUBLICADAS EN 2023 \n")
print("     -      UN TOTAL DE "+str(hpe_iot_2022)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY-ADVISORIES@HPE, FUERON PUBLICADAS EN 2022 \n")
print("     -      UN TOTAL DE "+str(hpe_iot_2021)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY-ADVISORIES@HPE, FUERON PUBLICADAS EN 2021 \n")
print("     -      UN TOTAL DE "+str(hpe_iot_2020)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY-ADVISORIES@HPE, FUERON PUBLICADAS EN 2020 \n")
print("     -      UN TOTAL DE "+str(hpe_iot_2019)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY-ADVISORIES@HPE, FUERON PUBLICADAS EN 2019 \n")
print("     -      UN TOTAL DE "+str(hpe_iot_2018)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY-ADVISORIES@HPE, FUERON PUBLICADAS EN 2018 O ANTERIORMENTE \n")
print("\n")
print("  -  EN  "+str(rapid7_iot)+" VULNERABILIDADES DONDE EL ASIGNADOR ES CVE@RAPID7, LAS ESTADÍSTICAS SEGUN FECHA DE PUBLICACION SON LAS SIGUIENTES : \n")
print("     -      UN TOTAL DE "+str(rapid7_iot_2023)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES CVE@RAPID7, FUERON PUBLICADAS EN 2023 \n")
print("     -      UN TOTAL DE "+str(rapid7_iot_2022)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES CVE@RAPID7, FUERON PUBLICADAS EN 2022 \n")
print("     -      UN TOTAL DE "+str(rapid7_iot_2021)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES CVE@RAPID7, FUERON PUBLICADAS EN 2021 \n")
print("     -      UN TOTAL DE "+str(rapid7_iot_2020)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES CVE@RAPID7, FUERON PUBLICADAS EN 2020 \n")
print("     -      UN TOTAL DE "+str(rapid7_iot_2019)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES CVE@RAPID7, FUERON PUBLICADAS EN 2019 \n")
print("     -      UN TOTAL DE "+str(rapid7_iot_2018)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES CVE@RAPID7, FUERON PUBLICADAS EN 2018 O ANTERIORMENTE \n")
print("\n")
print("  -  EN  "+str(fsecure_iot)+" VULNERABILIDADES DONDE EL ASIGNADOR ES CVE-NOTIFICATIONS-US@F-SECURE, LAS ESTADÍSTICAS SEGUN FECHA DE PUBLICACION SON LAS SIGUIENTES : \n")
print("     -      UN TOTAL DE "+str(fsecure_iot_2023)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES CVE-NOTIFICATIONS-US@F-SECURE, FUERON PUBLICADAS EN 2023 \n")
print("     -      UN TOTAL DE "+str(fsecure_iot_2022)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES CVE-NOTIFICATIONS-US@F-SECURE, FUERON PUBLICADAS EN 2022 \n")
print("     -      UN TOTAL DE "+str(fsecure_iot_2021)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES CVE-NOTIFICATIONS-US@F-SECURE, FUERON PUBLICADAS EN 2021 \n")
print("     -      UN TOTAL DE "+str(fsecure_iot_2020)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES CVE-NOTIFICATIONS-US@F-SECURE, FUERON PUBLICADAS EN 2020 \n")
print("     -      UN TOTAL DE "+str(fsecure_iot_2019)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES CVE-NOTIFICATIONS-US@F-SECURE, FUERON PUBLICADAS EN 2019 \n")
print("     -      UN TOTAL DE "+str(fsecure_iot_2018)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES CVE-NOTIFICATIONS-US@F-SECURE, FUERON PUBLICADAS EN 2018 O ANTERIORMENTE \n")
print("\n")
print("  -  EN  "+str(other_assigner_iot)+" VULNERABILIDADES DONDE EL ASIGNADOR ES OTRO DISTINTO A  LOS ANTERIORES, LAS ESTADÍSTICAS SEGUN FECHA DE PUBLICACION SON LAS SIGUIENTES : \n")
print("     -      UN TOTAL DE "+str(other_assigner_iot_2023)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES OTRO DISTINTO A LOS ANTERIORES, FUERON PUBLICADAS EN 2023 \n")
print("     -      UN TOTAL DE "+str(other_assigner_iot_2022)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES OTRO DISTINTO A LOS ANTERIORES, FUERON PUBLICADAS EN 2022 \n")
print("     -      UN TOTAL DE "+str(other_assigner_iot_2021)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES OTRO DISTINTO A LOS ANTERIORES, FUERON PUBLICADAS EN 2021 \n")
print("     -      UN TOTAL DE "+str(other_assigner_iot_2020)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES OTRO DISTINTO A LOS ANTERIORES, FUERON PUBLICADAS EN 2020 \n")
print("     -      UN TOTAL DE "+str(other_assigner_iot_2019)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES OTRO DISTINTO A LOS ANTERIORES, FUERON PUBLICADAS EN 2019 \n")
print("     -      UN TOTAL DE "+str(other_assigner_iot_2018)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES OTRO DISTINTO A LOS ANTERIORES, FUERON PUBLICADAS EN 2018 O ANTERIORMENTE \n")
print("\n")




print("************************** PORCENTAJE FECHA DE PUBLICACION Y CVE ASIGNADOR CVE PARTE IOT********************************")
print("\n")
print("\n")
print(" -  DE UN TOTAL DE "+str(total_assigner_iot)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ESTÁ DEFINIDO, LOS PORCENTAJES DE ASSIGNER Y FECHA DE PUBLICACION SON LOS SIGUIENTES  : \n")
print("\n")
print("EN EL "+str(float(((assigner_iot_2023*100)/(assigner_iot_2023+assigner_iot_2022+assigner_iot_2021+assigner_iot_2020+assigner_iot_2019+assigner_iot_2018))))+" % DE LAS VULNERABILIDADES PUBLICADAS EN EL 2023, LOS PORCENTAJES DE ASIGNADORES CVE SON LOS SIGUIENTES : \n")
print("     -      EN EL "+str(float(((jpcert_iot_2023*100)/(assigner_iot_2023))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES VULTURES@JPCERT\n")
print("     -      EN EL "+str(float(((mitre_iot_2023*100)/(assigner_iot_2023))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES CVE@MITRE \n")
print("     -      EN EL "+str(float(((cisco_iot_2023*100)/(assigner_iot_2023))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES TALOS-CNA@CISCO \n")
print("     -      EN EL "+str(float(((github_iot_2023*100)/(assigner_iot_2023))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY-ADVISORIES@GITHUB \n")
print("     -      EN EL "+str(float(((redhat_iot_2023*100)/(assigner_iot_2023))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES SECALERT@REDHAT\n")
print("     -      EN EL "+str(float(((qualcomm_iot_2023*100)/(assigner_iot_2023))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY.CNA@QUALCOMM \n")
print("     -      EN EL "+str(float(((apache_iot_2023*100)/(assigner_iot_2023))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY@APACHE.ORG \n")
print("     -      EN EL "+str(float(((oracle_iot_2023*100)/(assigner_iot_2023))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES SECALERT_US@ORACLE \n")
print("     -      EN EL "+str(float(((microsoft_iot_2023*100)/(assigner_iot_2023))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURE@MICROSOFT \n")
print("     -      EN EL "+str(float(((cert_iot_2023*100)/(assigner_iot_2023))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE INFO@CERT.VDE \n")
print("     -      EN EL "+str(float(((trendmicro_iot_2023*100)/(assigner_iot_2023))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY@TRENDMICRO \n")
print("     -      EN EL "+str(float(((nozomi_iot_2023*100)/(assigner_iot_2023))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE PRODSEC@NOZOMINETWORKS \n")
print("     -      EN EL "+str(float(((hq_iot_2023*100)/(assigner_iot_2023))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES ICS-CERT@HQ.DHS.GOV \n")
print("     -      EN EL "+str(float(((kaspersky_iot_2023*100)/(assigner_iot_2023))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES VULNERABILITY@KASPERSKY \n")
print("     -      EN EL "+str(float(((schneider_iot_2023*100)/(assigner_iot_2023))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE CYBERSECURITY@SCHNEIDER-ELECTRIC \n")
print("     -      EN EL "+str(float(((apple_iot_2023*100)/(assigner_iot_2023))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE PRODUCT-SECURITY@APPLE \n")
print("     -      EN EL "+str(float(((android_iot_2023*100)/(assigner_iot_2023))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY@ANDROID \n")
print("     -      EN EL "+str(float(((bitdefender_iot_2023*100)/(assigner_iot_2023))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE CVE-REQUESTS@BITDEFENDER \n")
print("     -      EN EL "+str(float(((mcafee_iot_2023*100)/(assigner_iot_2023))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE PSIRT@MCAFEE \n")
print("     -      EN EL "+str(float(((mozilla_iot_2023*100)/(assigner_iot_2023))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY@MOZILLA \n")
print("     -      EN EL "+str(float(((hpe_iot_2023*100)/(assigner_iot_2023))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY-ALERT@HPE \n")
print("     -      EN EL "+str(float(((fsecure_iot_2023*100)/(assigner_iot_2023))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES CVE-NOTIFICATIONS-US@F-SECURE \n")
print("     -      EN EL "+str(float(((rapid7_iot_2023*100)/(assigner_iot_2023))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES CVE@RAPID7 \n")
print("     -      EN EL "+str(float(((other_assigner_iot_2023*100)/(assigner_iot_2023))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES DISTINTO A LOS ANTERIORES \n")
print("\n")

print("EN EL "+str(float(((assigner_iot_2022*100)/(assigner_iot_2023+assigner_iot_2022+assigner_iot_2021+assigner_iot_2020+assigner_iot_2019+assigner_iot_2018))))+" % DE LAS VULNERABILIDADES PUBLICADAS EN EL 2022, LOS PORCENTAJES DE ASIGNADORES CVE SON LOS SIGUIENTES : \n")
print("     -      EN EL "+str(float(((jpcert_iot_2022*100)/(assigner_iot_2022))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES VULTURES@JPCERT\n")
print("     -      EN EL "+str(float(((mitre_iot_2022*100)/(assigner_iot_2022))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES CVE@MITRE \n")
print("     -      EN EL "+str(float(((cisco_iot_2022*100)/(assigner_iot_2022))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES TALOS-CNA@CISCO \n")
print("     -      EN EL "+str(float(((github_iot_2022*100)/(assigner_iot_2022))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY-ADVISORIES@GITHUB \n")
print("     -      EN EL "+str(float(((redhat_iot_2022*100)/(assigner_iot_2022))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES SECALERT@REDHAT\n")
print("     -      EN EL "+str(float(((qualcomm_iot_2022*100)/(assigner_iot_2022))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY.CNA@QUALCOMM \n")
print("     -      EN EL "+str(float(((apache_iot_2022*100)/(assigner_iot_2022))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY@APACHE.ORG \n")
print("     -      EN EL "+str(float(((oracle_iot_2022*100)/(assigner_iot_2022))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES SECALERT_US@ORACLE \n")
print("     -      EN EL "+str(float(((microsoft_iot_2022*100)/(assigner_iot_2022))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURE@MICROSOFT \n")
print("     -      EN EL "+str(float(((cert_iot_2022*100)/(assigner_iot_2022))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE INFO@CERT.VDE \n")
print("     -      EN EL "+str(float(((trendmicro_iot_2022*100)/(assigner_iot_2022))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY@TRENDMICRO \n")
print("     -      EN EL "+str(float(((nozomi_iot_2022*100)/(assigner_iot_2022))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE PRODSEC@NOZOMINETWORKS \n")
print("     -      EN EL "+str(float(((hq_iot_2022*100)/(assigner_iot_2022))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES ICS-CERT@HQ.DHS.GOV \n")
print("     -      EN EL "+str(float(((kaspersky_iot_2022*100)/(assigner_iot_2022))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES VULNERABILITY@KASPERSKY \n")
print("     -      EN EL "+str(float(((schneider_iot_2022*100)/(assigner_iot_2022))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE CYBERSECURITY@SCHNEIDER-ELECTRIC \n")
print("     -      EN EL "+str(float(((apple_iot_2022*100)/(assigner_iot_2022))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE PRODUCT-SECURITY@APPLE \n")
print("     -      EN EL "+str(float(((android_iot_2022*100)/(assigner_iot_2022))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY@ANDROID \n")
print("     -      EN EL "+str(float(((bitdefender_iot_2022*100)/(assigner_iot_2022))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE CVE-REQUESTS@BITDEFENDER \n")
print("     -      EN EL "+str(float(((mcafee_iot_2022*100)/(assigner_iot_2022))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE PSIRT@MCAFEE \n")
print("     -      EN EL "+str(float(((mozilla_iot_2022*100)/(assigner_iot_2022))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY@MOZILLA \n")
print("     -      EN EL "+str(float(((hpe_iot_2022*100)/(assigner_iot_2022))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY-ALERT@HPE \n")
print("     -      EN EL "+str(float(((fsecure_iot_2022*100)/(assigner_iot_2022))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES CVE-NOTIFICATIONS-US@F-SECURE \n")
print("     -      EN EL "+str(float(((rapid7_iot_2022*100)/(assigner_iot_2022))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES CVE@RAPID7 \n")
print("     -      EN EL "+str(float(((other_assigner_iot_2022*100)/(assigner_iot_2022))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES DISTINTO A LOS ANTERIORES \n")
print("\n")

print("EN EL "+str(float(((assigner_iot_2021*100)/(assigner_iot_2023+assigner_iot_2022+assigner_iot_2021+assigner_iot_2020+assigner_iot_2019+assigner_iot_2018))))+" % DE LAS VULNERABILIDADES PUBLICADAS EN EL 2021, LOS PORCENTAJES DE ASIGNADORES CVE SON LOS SIGUIENTES : \n")
print("     -      EN EL "+str(float(((jpcert_iot_2021*100)/(assigner_iot_2021))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES VULTURES@JPCERT\n")
print("     -      EN EL "+str(float(((mitre_iot_2021*100)/(assigner_iot_2021))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES CVE@MITRE \n")
print("     -      EN EL "+str(float(((cisco_iot_2021*100)/(assigner_iot_2021))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES TALOS-CNA@CISCO \n")
print("     -      EN EL "+str(float(((github_iot_2021*100)/(assigner_iot_2021))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY-ADVISORIES@GITHUB \n")
print("     -      EN EL "+str(float(((redhat_iot_2021*100)/(assigner_iot_2021))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES SECALERT@REDHAT\n")
print("     -      EN EL "+str(float(((qualcomm_iot_2021*100)/(assigner_iot_2021))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY.CNA@QUALCOMM \n")
print("     -      EN EL "+str(float(((apache_iot_2021*100)/(assigner_iot_2021))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY@APACHE.ORG \n")
print("     -      EN EL "+str(float(((oracle_iot_2021*100)/(assigner_iot_2021))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES SECALERT_US@ORACLE \n")
print("     -      EN EL "+str(float(((microsoft_iot_2021*100)/(assigner_iot_2021))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURE@MICROSOFT \n")
print("     -      EN EL "+str(float(((cert_iot_2021*100)/(assigner_iot_2021))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE INFO@CERT.VDE \n")
print("     -      EN EL "+str(float(((trendmicro_iot_2021*100)/(assigner_iot_2021))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY@TRENDMICRO \n")
print("     -      EN EL "+str(float(((nozomi_iot_2021*100)/(assigner_iot_2021))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE PRODSEC@NOZOMINETWORKS \n")
print("     -      EN EL "+str(float(((hq_iot_2021*100)/(assigner_iot_2021))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES ICS-CERT@HQ.DHS.GOV \n")
print("     -      EN EL "+str(float(((kaspersky_iot_2021*100)/(assigner_iot_2021))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES VULNERABILITY@KASPERSKY \n")
print("     -      EN EL "+str(float(((schneider_iot_2021*100)/(assigner_iot_2021))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE CYBERSECURITY@SCHNEIDER-ELECTRIC \n")
print("     -      EN EL "+str(float(((apple_iot_2021*100)/(assigner_iot_2021))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE PRODUCT-SECURITY@APPLE \n")
print("     -      EN EL "+str(float(((android_iot_2021*100)/(assigner_iot_2021))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY@ANDROID \n")
print("     -      EN EL "+str(float(((bitdefender_iot_2021*100)/(assigner_iot_2021))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE CVE-REQUESTS@BITDEFENDER \n")
print("     -      EN EL "+str(float(((mcafee_iot_2021*100)/(assigner_iot_2021))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE PSIRT@MCAFEE \n")
print("     -      EN EL "+str(float(((mozilla_iot_2021*100)/(assigner_iot_2021))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY@MOZILLA \n")
print("     -      EN EL "+str(float(((hpe_iot_2021*100)/(assigner_iot_2021))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY-ALERT@HPE \n")
print("     -      EN EL "+str(float(((fsecure_iot_2021*100)/(assigner_iot_2021))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES CVE-NOTIFICATIONS-US@F-SECURE \n")
print("     -      EN EL "+str(float(((rapid7_iot_2021*100)/(assigner_iot_2021))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES CVE@RAPID7 \n")
print("     -      EN EL "+str(float(((other_assigner_iot_2021*100)/(assigner_iot_2021))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES DISTINTO A LOS ANTERIORES \n")
print("\n")

print("EN EL "+str(float(((assigner_iot_2020*100)/(assigner_iot_2023+assigner_iot_2022+assigner_iot_2021+assigner_iot_2020+assigner_iot_2019+assigner_iot_2018))))+" % DE LAS VULNERABILIDADES PUBLICADAS EN EL 2020, LOS PORCENTAJES DE ASIGNADORES CVE SON LOS SIGUIENTES : \n")
print("     -      EN EL "+str(float(((jpcert_iot_2020*100)/(assigner_iot_2020))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES VULTURES@JPCERT\n")
print("     -      EN EL "+str(float(((mitre_iot_2020*100)/(assigner_iot_2020))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES CVE@MITRE \n")
print("     -      EN EL "+str(float(((cisco_iot_2020*100)/(assigner_iot_2020))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES TALOS-CNA@CISCO \n")
print("     -      EN EL "+str(float(((github_iot_2020*100)/(assigner_iot_2020))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY-ADVISORIES@GITHUB \n")
print("     -      EN EL "+str(float(((redhat_iot_2020*100)/(assigner_iot_2020))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES SECALERT@REDHAT\n")
print("     -      EN EL "+str(float(((qualcomm_iot_2020*100)/(assigner_iot_2020))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY.CNA@QUALCOMM \n")
print("     -      EN EL "+str(float(((apache_iot_2020*100)/(assigner_iot_2020))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY@APACHE.ORG \n")
print("     -      EN EL "+str(float(((oracle_iot_2020*100)/(assigner_iot_2020))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES SECALERT_US@ORACLE \n")
print("     -      EN EL "+str(float(((microsoft_iot_2020*100)/(assigner_iot_2020))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURE@MICROSOFT \n")
print("     -      EN EL "+str(float(((cert_iot_2020*100)/(assigner_iot_2020))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE INFO@CERT.VDE \n")
print("     -      EN EL "+str(float(((trendmicro_iot_2020*100)/(assigner_iot_2020))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY@TRENDMICRO \n")
print("     -      EN EL "+str(float(((nozomi_iot_2020*100)/(assigner_iot_2020))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE PRODSEC@NOZOMINETWORKS \n")
print("     -      EN EL "+str(float(((hq_iot_2020*100)/(assigner_iot_2020))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES ICS-CERT@HQ.DHS.GOV \n")
print("     -      EN EL "+str(float(((kaspersky_iot_2020*100)/(assigner_iot_2020))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES VULNERABILITY@KASPERSKY \n")
print("     -      EN EL "+str(float(((schneider_iot_2020*100)/(assigner_iot_2020))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE CYBERSECURITY@SCHNEIDER-ELECTRIC \n")
print("     -      EN EL "+str(float(((apple_iot_2020*100)/(assigner_iot_2020))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE PRODUCT-SECURITY@APPLE \n")
print("     -      EN EL "+str(float(((android_iot_2020*100)/(assigner_iot_2020))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY@ANDROID \n")
print("     -      EN EL "+str(float(((bitdefender_iot_2020*100)/(assigner_iot_2020))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE CVE-REQUESTS@BITDEFENDER \n")
print("     -      EN EL "+str(float(((mcafee_iot_2020*100)/(assigner_iot_2020))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE PSIRT@MCAFEE \n")
print("     -      EN EL "+str(float(((mozilla_iot_2020*100)/(assigner_iot_2020))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY@MOZILLA \n")
print("     -      EN EL "+str(float(((hpe_iot_2020*100)/(assigner_iot_2020))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY-ALERT@HPE \n")
print("     -      EN EL "+str(float(((fsecure_iot_2020*100)/(assigner_iot_2020))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES CVE-NOTIFICATIONS-US@F-SECURE \n")
print("     -      EN EL "+str(float(((rapid7_iot_2020*100)/(assigner_iot_2020))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES CVE@RAPID7 \n")
print("     -      EN EL "+str(float(((other_assigner_iot_2020*100)/(assigner_iot_2020))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES DISTINTO A LOS ANTERIORES \n")
print("\n")

print("EN EL "+str(float(((assigner_iot_2019*100)/(assigner_iot_2023+assigner_iot_2022+assigner_iot_2021+assigner_iot_2020+assigner_iot_2019+assigner_iot_2018))))+" % DE LAS VULNERABILIDADES PUBLICADAS EN EL 2019, LOS PORCENTAJES DE ASIGNADORES CVE SON LOS SIGUIENTES : \n")
print("     -      EN EL "+str(float(((jpcert_iot_2019*100)/(assigner_iot_2019))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES VULTURES@JPCERT\n")
print("     -      EN EL "+str(float(((mitre_iot_2019*100)/(assigner_iot_2019))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES CVE@MITRE \n")
print("     -      EN EL "+str(float(((cisco_iot_2019*100)/(assigner_iot_2019))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES TALOS-CNA@CISCO \n")
print("     -      EN EL "+str(float(((github_iot_2019*100)/(assigner_iot_2019))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY-ADVISORIES@GITHUB \n")
print("     -      EN EL "+str(float(((redhat_iot_2019*100)/(assigner_iot_2019))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES SECALERT@REDHAT\n")
print("     -      EN EL "+str(float(((qualcomm_iot_2019*100)/(assigner_iot_2019))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY.CNA@QUALCOMM \n")
print("     -      EN EL "+str(float(((apache_iot_2019*100)/(assigner_iot_2019))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY@APACHE.ORG \n")
print("     -      EN EL "+str(float(((oracle_iot_2019*100)/(assigner_iot_2019))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES SECALERT_US@ORACLE \n")
print("     -      EN EL "+str(float(((microsoft_iot_2019*100)/(assigner_iot_2019))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURE@MICROSOFT \n")
print("     -      EN EL "+str(float(((cert_iot_2019*100)/(assigner_iot_2019))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE INFO@CERT.VDE \n")
print("     -      EN EL "+str(float(((trendmicro_iot_2019*100)/(assigner_iot_2019))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY@TRENDMICRO \n")
print("     -      EN EL "+str(float(((nozomi_iot_2019*100)/(assigner_iot_2019))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE PRODSEC@NOZOMINETWORKS \n")
print("     -      EN EL "+str(float(((hq_iot_2019*100)/(assigner_iot_2019))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES ICS-CERT@HQ.DHS.GOV \n")
print("     -      EN EL "+str(float(((kaspersky_iot_2019*100)/(assigner_iot_2019))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES VULNERABILITY@KASPERSKY \n")
print("     -      EN EL "+str(float(((schneider_iot_2019*100)/(assigner_iot_2019))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE CYBERSECURITY@SCHNEIDER-ELECTRIC \n")
print("     -      EN EL "+str(float(((apple_iot_2019*100)/(assigner_iot_2019))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE PRODUCT-SECURITY@APPLE \n")
print("     -      EN EL "+str(float(((android_iot_2019*100)/(assigner_iot_2019))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY@ANDROID \n")
print("     -      EN EL "+str(float(((bitdefender_iot_2019*100)/(assigner_iot_2019))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE CVE-REQUESTS@BITDEFENDER \n")
print("     -      EN EL "+str(float(((mcafee_iot_2019*100)/(assigner_iot_2019))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE PSIRT@MCAFEE \n")
print("     -      EN EL "+str(float(((mozilla_iot_2019*100)/(assigner_iot_2019))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY@MOZILLA \n")
print("     -      EN EL "+str(float(((hpe_iot_2019*100)/(assigner_iot_2019))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY-ALERT@HPE \n")
print("     -      EN EL "+str(float(((fsecure_iot_2019*100)/(assigner_iot_2019))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES CVE-NOTIFICATIONS-US@F-SECURE \n")
print("     -      EN EL "+str(float(((rapid7_iot_2019*100)/(assigner_iot_2019))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES CVE@RAPID7 \n")
print("     -      EN EL "+str(float(((other_assigner_iot_2019*100)/(assigner_iot_2019))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES DISTINTO A LOS ANTERIORES \n")
print("\n")

print("EN EL "+str(float(((assigner_iot_2018*100)/(assigner_iot_2023+assigner_iot_2022+assigner_iot_2021+assigner_iot_2020+assigner_iot_2019+assigner_iot_2018))))+" % DE LAS VULNERABILIDADES PUBLICADAS EN EL 2018 O ANTERIORMENTE, LOS PORCENTAJES DE ASIGNADORES CVE SON LOS SIGUIENTES : \n")
print("     -      EN EL "+str(float(((jpcert_iot_2018*100)/(assigner_iot_2018))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES VULTURES@JPCERT\n")
print("     -      EN EL "+str(float(((mitre_iot_2018*100)/(assigner_iot_2018))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES CVE@MITRE \n")
print("     -      EN EL "+str(float(((cisco_iot_2018*100)/(assigner_iot_2018))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES TALOS-CNA@CISCO \n")
print("     -      EN EL "+str(float(((github_iot_2018*100)/(assigner_iot_2018))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY-ADVISORIES@GITHUB \n")
print("     -      EN EL "+str(float(((redhat_iot_2018*100)/(assigner_iot_2018))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES SECALERT@REDHAT\n")
print("     -      EN EL "+str(float(((qualcomm_iot_2018*100)/(assigner_iot_2018))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY.CNA@QUALCOMM \n")
print("     -      EN EL "+str(float(((apache_iot_2018*100)/(assigner_iot_2018))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY@APACHE.ORG \n")
print("     -      EN EL "+str(float(((oracle_iot_2018*100)/(assigner_iot_2018))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES SECALERT_US@ORACLE \n")
print("     -      EN EL "+str(float(((microsoft_iot_2018*100)/(assigner_iot_2018))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURE@MICROSOFT \n")
print("     -      EN EL "+str(float(((cert_iot_2018*100)/(assigner_iot_2018))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE INFO@CERT.VDE \n")
print("     -      EN EL "+str(float(((trendmicro_iot_2018*100)/(assigner_iot_2018))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY@TRENDMICRO \n")
print("     -      EN EL "+str(float(((nozomi_iot_2018*100)/(assigner_iot_2018))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE PRODSEC@NOZOMINETWORKS \n")
print("     -      EN EL "+str(float(((hq_iot_2018*100)/(assigner_iot_2018))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES ICS-CERT@HQ.DHS.GOV \n")
print("     -      EN EL "+str(float(((kaspersky_iot_2018*100)/(assigner_iot_2018))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES VULNERABILITY@KASPERSKY \n")
print("     -      EN EL "+str(float(((schneider_iot_2018*100)/(assigner_iot_2018))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE CYBERSECURITY@SCHNEIDER-ELECTRIC \n")
print("     -      EN EL "+str(float(((apple_iot_2018*100)/(assigner_iot_2018))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE PRODUCT-SECURITY@APPLE \n")
print("     -      EN EL "+str(float(((android_iot_2018*100)/(assigner_iot_2018))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY@ANDROID \n")
print("     -      EN EL "+str(float(((bitdefender_iot_2018*100)/(assigner_iot_2018))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE CVE-REQUESTS@BITDEFENDER \n")
print("     -      EN EL "+str(float(((mcafee_iot_2018*100)/(assigner_iot_2018))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE PSIRT@MCAFEE \n")
print("     -      EN EL "+str(float(((mozilla_iot_2018*100)/(assigner_iot_2018))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY@MOZILLA \n")
print("     -      EN EL "+str(float(((hpe_iot_2018*100)/(assigner_iot_2018))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY-ALERT@HPE \n")
print("     -      EN EL "+str(float(((fsecure_iot_2018*100)/(assigner_iot_2018))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES CVE-NOTIFICATIONS-US@F-SECURE \n")
print("     -      EN EL "+str(float(((rapid7_iot_2018*100)/(assigner_iot_2018))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES CVE@RAPID7 \n")
print("     -      EN EL "+str(float(((other_assigner_iot_2018*100)/(assigner_iot_2018))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES DISTINTO A LOS ANTERIORES \n")
print("\n")








print("************************** PORCENTAJE ASIGNADOR CVE SEGÚN FECHA DE PUBLICACIÓN PARTE IOT********************************")
print("\n")
print("\n")
print(" -  DE UN TOTAL DE "+str(total_assigner_iot)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ESTÁ DEFINIDO, LOS PORCENTAJES DE ASSIGNER SEGUN FECHA DE PUBLICACION SON LOS SIGUIENTES  : \n")
print("\n")
print("EN EL "+str(float(((jpcert_iot*100)/total_assigner_iot)))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR ES VULTURES@JPCERT, LOS PORCENTAJES SEGUN FECHA DE PUBLICACION SON LOS SIGUIENTES : \n")
print("     -      EL "+str(float(((jpcert_iot_2023*100)/(jpcert_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES VULTURES@JPCERT, FUERON PUBLICADAS EN 2023 \n")
print("     -      EL "+str(float(((jpcert_iot_2022*100)/(jpcert_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES VULTURES@JPCERT, FUERON PUBLICADAS EN 2022 \n")
print("     -      EL "+str(float(((jpcert_iot_2021*100)/(jpcert_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES VULTURES@JPCERT, FUERON PUBLICADAS EN 2021 \n")
print("     -      EL "+str(float(((jpcert_iot_2020*100)/(jpcert_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES VULTURES@JPCERT, FUERON PUBLICADAS EN 2020 \n")
print("     -      EL "+str(float(((jpcert_iot_2019*100)/(jpcert_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES VULTURES@JPCERT, FUERON PUBLICADAS EN 2019 \n")
print("     -      EL "+str(float(((jpcert_iot_2018*100)/(jpcert_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES VULTURES@JPCERT, FUERON PUBLICADAS EN 2018 O ANTERIORMENTE \n")
print("\n")
print("\n")
print("EN EL "+str(float(((mitre_iot*100)/total_assigner_iot)))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR ES CVE@MITRE, LOS PORCENTAJES SEGUN FECHA DE PUBLICACION SON LOS SIGUIENTES : \n")
print("     -      EL "+str(float(((mitre_iot_2023*100)/(mitre_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES CVE@MITRE, FUERON PUBLICADAS EN 2023 \n")
print("     -      EL "+str(float(((mitre_iot_2022*100)/(mitre_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES CVE@MITRE, FUERON PUBLICADAS EN 2022 \n")
print("     -      EL "+str(float(((mitre_iot_2021*100)/(mitre_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES CVE@MITRE, FUERON PUBLICADAS EN 2021 \n")
print("     -      EL "+str(float(((mitre_iot_2020*100)/(mitre_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES CVE@MITRE, FUERON PUBLICADAS EN 2020 \n")
print("     -      EL "+str(float(((mitre_iot_2019*100)/(mitre_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES CVE@MITRE, FUERON PUBLICADAS EN 2019 \n")
print("     -      EL "+str(float(((mitre_iot_2018*100)/(mitre_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES CVE@MITRE, FUERON PUBLICADAS EN 2018 O ANTERIORMENTE \n")
print("\n")
print("\n")
print("EN EL "+str(float(((cisco_iot*100)/total_assigner_iot)))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR ES TALOS-CNA@CISCO, LOS PORCENTAJES SEGUN FECHA DE PUBLICACION SON LOS SIGUIENTES : \n")
print("     -      EL "+str(float(((cisco_iot_2023*100)/(cisco_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES TALOS-CNA@CISCO, FUERON PUBLICADAS EN 2023 \n")
print("     -      EL "+str(float(((cisco_iot_2022*100)/(cisco_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES TALOS-CNA@CISCO, FUERON PUBLICADAS EN 2022 \n")
print("     -      EL "+str(float(((cisco_iot_2021*100)/(cisco_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES TALOS-CNA@CISCO, FUERON PUBLICADAS EN 2021 \n")
print("     -      EL "+str(float(((cisco_iot_2020*100)/(cisco_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES TALOS-CNA@CISCO, FUERON PUBLICADAS EN 2020 \n")
print("     -      EL "+str(float(((cisco_iot_2019*100)/(cisco_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES TALOS-CNA@CISCO, FUERON PUBLICADAS EN 2019 \n")
print("     -      EL "+str(float(((cisco_iot_2018*100)/(cisco_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES TALOS-CNA@CISCO, FUERON PUBLICADAS EN 2018 O ANTERIORMENTE \n")
print("\n")
print("\n")
print("EN EL "+str(float(((github_iot*100)/total_assigner_iot)))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR ES SECURITY-ADVISORIES@GITHUB, LOS PORCENTAJES SEGUN FECHA DE PUBLICACION SON LOS SIGUIENTES : \n")
print("     -      EL "+str(float(((github_iot_2023*100)/(github_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY-ADVISORIES@GITHUB, FUERON PUBLICADAS EN 2023 \n")
print("     -      EL "+str(float(((github_iot_2022*100)/(github_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY-ADVISORIES@GITHUB, FUERON PUBLICADAS EN 2022 \n")
print("     -      EL "+str(float(((github_iot_2021*100)/(github_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY-ADVISORIES@GITHUB, FUERON PUBLICADAS EN 2021 \n")
print("     -      EL "+str(float(((github_iot_2020*100)/(github_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY-ADVISORIES@GITHUB, FUERON PUBLICADAS EN 2020 \n")
print("     -      EL "+str(float(((github_iot_2019*100)/(github_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY-ADVISORIES@GITHUB, FUERON PUBLICADAS EN 2019 \n")
print("     -      EL "+str(float(((github_iot_2018*100)/(github_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY-ADVISORIES@GITHUB, FUERON PUBLICADAS EN 2018 O ANTERIORMENTE \n")
print("\n")
print("\n")
print("EN EL "+str(float(((redhat_iot*100)/total_assigner_iot)))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR ES SECALERT@REDHAT, LOS PORCENTAJES SEGUN FECHA DE PUBLICACION SON LOS SIGUIENTES : \n")
print("     -      EL "+str(float(((redhat_iot_2023*100)/(redhat_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECALERT@REDHAT, FUERON PUBLICADAS EN 2023 \n")
print("     -      EL "+str(float(((redhat_iot_2022*100)/(redhat_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECALERT@REDHAT, FUERON PUBLICADAS EN 2022 \n")
print("     -      EL "+str(float(((redhat_iot_2021*100)/(redhat_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECALERT@REDHAT, FUERON PUBLICADAS EN 2021 \n")
print("     -      EL "+str(float(((redhat_iot_2020*100)/(redhat_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECALERT@REDHAT, FUERON PUBLICADAS EN 2020 \n")
print("     -      EL "+str(float(((redhat_iot_2019*100)/(redhat_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECALERT@REDHAT, FUERON PUBLICADAS EN 2019 \n")
print("     -      EL "+str(float(((redhat_iot_2018*100)/(redhat_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECALERT@REDHAT, FUERON PUBLICADAS EN 2018 O ANTERIORMENTE \n")
print("\n")
print("\n")
print("EN EL "+str(float(((qualcomm_iot*100)/total_assigner_iot)))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR ES SECURITY.CNA@QUALCOMM, LOS PORCENTAJES SEGUN FECHA DE PUBLICACION SON LOS SIGUIENTES : \n")
print("     -      EL "+str(float(((qualcomm_iot_2023*100)/(qualcomm_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY.CNA@QUALCOMM, FUERON PUBLICADAS EN 2023 \n")
print("     -      EL "+str(float(((qualcomm_iot_2022*100)/(qualcomm_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY.CNA@QUALCOMM, FUERON PUBLICADAS EN 2022 \n")
print("     -      EL "+str(float(((qualcomm_iot_2021*100)/(qualcomm_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY.CNA@QUALCOMM, FUERON PUBLICADAS EN 2021 \n")
print("     -      EL "+str(float(((qualcomm_iot_2020*100)/(qualcomm_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY.CNA@QUALCOMM, FUERON PUBLICADAS EN 2020 \n")
print("     -      EL "+str(float(((qualcomm_iot_2019*100)/(qualcomm_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY.CNA@QUALCOMM, FUERON PUBLICADAS EN 2019 \n")
print("     -      EL "+str(float(((qualcomm_iot_2018*100)/(qualcomm_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY.CNA@QUALCOMM, FUERON PUBLICADAS EN 2018 O ANTERIORMENTE \n")
print("\n")
print("\n")
print("EN EL "+str(float(((apache_iot*100)/total_assigner_iot)))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR ES SECURITY@APACHE.ORG, LOS PORCENTAJES SEGUN FECHA DE PUBLICACION SON LOS SIGUIENTES : \n")
print("     -      EL "+str(float(((apache_iot_2023*100)/(apache_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY@APACHE.ORG, FUERON PUBLICADAS EN 2023 \n")
print("     -      EL "+str(float(((apache_iot_2022*100)/(apache_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY@APACHE.ORG, FUERON PUBLICADAS EN 2022 \n")
print("     -      EL "+str(float(((apache_iot_2021*100)/(apache_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY@APACHE.ORG, FUERON PUBLICADAS EN 2021 \n")
print("     -      EL "+str(float(((apache_iot_2020*100)/(apache_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY@APACHE.ORG, FUERON PUBLICADAS EN 2020 \n")
print("     -      EL "+str(float(((apache_iot_2019*100)/(apache_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY@APACHE.ORG, FUERON PUBLICADAS EN 2019 \n")
print("     -      EL "+str(float(((apache_iot_2018*100)/(apache_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY@APACHE.ORG, FUERON PUBLICADAS EN 2018 O ANTERIORMENTE \n")
print("\n")
print("\n")
print("EN EL "+str(float(((oracle_iot*100)/total_assigner_iot)))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR ES SECALERT_US@ORACLE, LOS PORCENTAJES SEGUN FECHA DE PUBLICACION SON LOS SIGUIENTES : \n")
print("     -      EL "+str(float(((oracle_iot_2023*100)/(oracle_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECALERT_US@ORACLE, FUERON PUBLICADAS EN 2023 \n")
print("     -      EL "+str(float(((oracle_iot_2022*100)/(oracle_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECALERT_US@ORACLE, FUERON PUBLICADAS EN 2022 \n")
print("     -      EL "+str(float(((oracle_iot_2021*100)/(oracle_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECALERT_US@ORACLE, FUERON PUBLICADAS EN 2021 \n")
print("     -      EL "+str(float(((oracle_iot_2020*100)/(oracle_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECALERT_US@ORACLE, FUERON PUBLICADAS EN 2020 \n")
print("     -      EL "+str(float(((oracle_iot_2019*100)/(oracle_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECALERT_US@ORACLE, FUERON PUBLICADAS EN 2019 \n")
print("     -      EL "+str(float(((oracle_iot_2018*100)/(oracle_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECALERT_US@ORACLE, FUERON PUBLICADAS EN 2018 O ANTERIORMENTE \n")
print("\n")
print("\n")
print("EN EL "+str(float(((microsoft_iot*100)/total_assigner_iot)))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR ES SECURE@MICROSOFT, LOS PORCENTAJES SEGUN FECHA DE PUBLICACION SON LOS SIGUIENTES : \n")
print("     -      EL "+str(float(((microsoft_iot_2023*100)/(microsoft_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURE@MICROSOFT, FUERON PUBLICADAS EN 2023 \n")
print("     -      EL "+str(float(((microsoft_iot_2022*100)/(microsoft_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURE@MICROSOFT, FUERON PUBLICADAS EN 2022 \n")
print("     -      EL "+str(float(((microsoft_iot_2021*100)/(microsoft_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURE@MICROSOFT, FUERON PUBLICADAS EN 2021 \n")
print("     -      EL "+str(float(((microsoft_iot_2020*100)/(microsoft_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURE@MICROSOFT, FUERON PUBLICADAS EN 2020 \n")
print("     -      EL "+str(float(((microsoft_iot_2019*100)/(microsoft_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURE@MICROSOFT, FUERON PUBLICADAS EN 2019 \n")
print("     -      EL "+str(float(((microsoft_iot_2018*100)/(microsoft_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURE@MICROSOFT, FUERON PUBLICADAS EN 2018 O ANTERIORMENTE \n")
print("\n")
print("\n")
print("EN EL "+str(float(((cert_iot*100)/total_assigner_iot)))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR INFO@CERT.VDE, LOS PORCENTAJES SEGUN FECHA DE PUBLICACION SON LOS SIGUIENTES : \n")
print("     -      EL "+str(float(((cert_iot_2023*100)/(cert_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE INFO@CERT.VDE, FUERON PUBLICADAS EN 2023 \n")
print("     -      EL "+str(float(((cert_iot_2022*100)/(cert_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE INFO@CERT.VDE, FUERON PUBLICADAS EN 2022 \n")
print("     -      EL "+str(float(((cert_iot_2021*100)/(cert_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE INFO@CERT.VDE, FUERON PUBLICADAS EN 2021 \n")
print("     -      EL "+str(float(((cert_iot_2020*100)/(cert_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE INFO@CERT.VDE, FUERON PUBLICADAS EN 2020 \n")
print("     -      EL "+str(float(((cert_iot_2019*100)/(cert_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE INFO@CERT.VDE, FUERON PUBLICADAS EN 2019 \n")
print("     -      EL "+str(float(((cert_iot_2018*100)/(cert_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE INFO@CERT.VDE, FUERON PUBLICADAS EN 2018 O ANTERIORMENTE \n")
print("\n")
print("\n")
print("EN EL "+str(float(((trendmicro_iot*100)/total_assigner_iot)))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR ES SECURITY@TRENDMICRO, LOS PORCENTAJES SEGUN FECHA DE PUBLICACION SON LOS SIGUIENTES : \n")
print("     -      EL "+str(float(((trendmicro_iot_2023*100)/(trendmicro_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY@TRENDMICRO, FUERON PUBLICADAS EN 2023 \n")
print("     -      EL "+str(float(((trendmicro_iot_2022*100)/(trendmicro_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY@TRENDMICRO, FUERON PUBLICADAS EN 2022 \n")
print("     -      EL "+str(float(((trendmicro_iot_2021*100)/(trendmicro_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY@TRENDMICRO, FUERON PUBLICADAS EN 2021 \n")
print("     -      EL "+str(float(((trendmicro_iot_2020*100)/(trendmicro_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY@TRENDMICRO, FUERON PUBLICADAS EN 2020 \n")
print("     -      EL "+str(float(((trendmicro_iot_2019*100)/(trendmicro_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY@TRENDMICRO, FUERON PUBLICADAS EN 2019 \n")
print("     -      EL "+str(float(((trendmicro_iot_2018*100)/(trendmicro_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY@TRENDMICRO, FUERON PUBLICADAS EN 2018 O ANTERIORMENTE \n")
print("\n")
print("\n")
print("EN EL "+str(float(((nozomi_iot*100)/total_assigner_iot)))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR PRODSEC@NOZOMINETWORKS, LOS PORCENTAJES SEGUN FECHA DE PUBLICACION SON LOS SIGUIENTES : \n")
print("     -      EL "+str(float(((nozomi_iot_2023*100)/(nozomi_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE PRODSEC@NOZOMINETWORKS, FUERON PUBLICADAS EN 2023 \n")
print("     -      EL "+str(float(((nozomi_iot_2022*100)/(nozomi_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE PRODSEC@NOZOMINETWORKS, FUERON PUBLICADAS EN 2022 \n")
print("     -      EL "+str(float(((nozomi_iot_2021*100)/(nozomi_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE PRODSEC@NOZOMINETWORKS, FUERON PUBLICADAS EN 2021 \n")
print("     -      EL "+str(float(((nozomi_iot_2020*100)/(nozomi_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE PRODSEC@NOZOMINETWORKS, FUERON PUBLICADAS EN 2020 \n")
print("     -      EL "+str(float(((nozomi_iot_2019*100)/(nozomi_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE PRODSEC@NOZOMINETWORKS, FUERON PUBLICADAS EN 2019 \n")
print("     -      EL "+str(float(((nozomi_iot_2018*100)/(nozomi_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE PRODSEC@NOZOMINETWORKS, FUERON PUBLICADAS EN 2018 O ANTERIORMENTE \n")
print("\n")
print("\n")
print("EN EL "+str(float(((hq_iot*100)/total_assigner_iot)))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR ES ICS-CERT@HQ.DHS.GOV, LOS PORCENTAJES SEGUN FECHA DE PUBLICACION SON LOS SIGUIENTES : \n")
print("     -      EL "+str(float(((hq_iot_2023*100)/(hq_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES ICS-CERT@HQ.DHS.GOV, FUERON PUBLICADAS EN 2023 \n")
print("     -      EL "+str(float(((hq_iot_2022*100)/(hq_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES ICS-CERT@HQ.DHS.GOV, FUERON PUBLICADAS EN 2022 \n")
print("     -      EL "+str(float(((hq_iot_2021*100)/(hq_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES ICS-CERT@HQ.DHS.GOV, FUERON PUBLICADAS EN 2021 \n")
print("     -      EL "+str(float(((hq_iot_2020*100)/(hq_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES ICS-CERT@HQ.DHS.GOV, FUERON PUBLICADAS EN 2020 \n")
print("     -      EL "+str(float(((hq_iot_2019*100)/(hq_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES ICS-CERT@HQ.DHS.GOV, FUERON PUBLICADAS EN 2019 \n")
print("     -      EL "+str(float(((hq_iot_2018*100)/(hq_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES ICS-CERT@HQ.DHS.GOV, FUERON PUBLICADAS EN 2018 O ANTERIORMENTE \n")
print("\n")
print("\n")
print("EN EL "+str(float(((kaspersky_iot*100)/total_assigner_iot)))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR ES VULNERABILITY@KASPERSKY, LOS PORCENTAJES SEGUN FECHA DE PUBLICACION SON LOS SIGUIENTES : \n")
print("     -      EL "+str(float(((kaspersky_iot_2023*100)/(kaspersky_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES VULNERABILITY@KASPERSKY, FUERON PUBLICADAS EN 2023 \n")
print("     -      EL "+str(float(((kaspersky_iot_2022*100)/(kaspersky_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES VULNERABILITY@KASPERSKY, FUERON PUBLICADAS EN 2022 \n")
print("     -      EL "+str(float(((kaspersky_iot_2021*100)/(kaspersky_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES VULNERABILITY@KASPERSKY, FUERON PUBLICADAS EN 2021 \n")
print("     -      EL "+str(float(((kaspersky_iot_2020*100)/(kaspersky_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES VULNERABILITY@KASPERSKY, FUERON PUBLICADAS EN 2020 \n")
print("     -      EL "+str(float(((kaspersky_iot_2019*100)/(kaspersky_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES VULNERABILITY@KASPERSKY, FUERON PUBLICADAS EN 2019 \n")
print("     -      EL "+str(float(((kaspersky_iot_2018*100)/(kaspersky_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES VULNERABILITY@KASPERSKY, FUERON PUBLICADAS EN 2018 O ANTERIORMENTE \n")
print("\n")
print("\n")
print("EN EL "+str(float(((schneider_iot*100)/total_assigner_iot)))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR CYBERSECURITY@SCHNEIDER-ELECTRIC, LOS PORCENTAJES SEGUN FECHA DE PUBLICACION SON LOS SIGUIENTES : \n")
print("     -      EL "+str(float(((schneider_iot_2023*100)/(schneider_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE CYBERSECURITY@SCHNEIDER-ELECTRIC, FUERON PUBLICADAS EN 2023 \n")
print("     -      EL "+str(float(((schneider_iot_2022*100)/(schneider_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE CYBERSECURITY@SCHNEIDER-ELECTRIC, FUERON PUBLICADAS EN 2022 \n")
print("     -      EL "+str(float(((schneider_iot_2021*100)/(schneider_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE CYBERSECURITY@SCHNEIDER-ELECTRIC, FUERON PUBLICADAS EN 2021 \n")
print("     -      EL "+str(float(((schneider_iot_2020*100)/(schneider_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE CYBERSECURITY@SCHNEIDER-ELECTRIC, FUERON PUBLICADAS EN 2020 \n")
print("     -      EL "+str(float(((schneider_iot_2019*100)/(schneider_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE CYBERSECURITY@SCHNEIDER-ELECTRIC, FUERON PUBLICADAS EN 2019 \n")
print("     -      EL "+str(float(((schneider_iot_2018*100)/(schneider_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE CYBERSECURITY@SCHNEIDER-ELECTRIC, FUERON PUBLICADAS EN 2018 O ANTERIORMENTE \n")
print("\n")
print("\n")
print("EN EL "+str(float(((apple_iot*100)/total_assigner_iot)))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR PRODUCT-SECURITY@APPLE, LOS PORCENTAJES SEGUN FECHA DE PUBLICACION SON LOS SIGUIENTES : \n")
print("     -      EL "+str(float(((apple_iot_2023*100)/(apple_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE PRODUCT-SECURITY@APPLE, FUERON PUBLICADAS EN 2023 \n")
print("     -      EL "+str(float(((apple_iot_2022*100)/(apple_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE PRODUCT-SECURITY@APPLE, FUERON PUBLICADAS EN 2022 \n")
print("     -      EL "+str(float(((apple_iot_2021*100)/(apple_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE PRODUCT-SECURITY@APPLE, FUERON PUBLICADAS EN 2021 \n")
print("     -      EL "+str(float(((apple_iot_2020*100)/(apple_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE PRODUCT-SECURITY@APPLE, FUERON PUBLICADAS EN 2020 \n")
print("     -      EL "+str(float(((apple_iot_2019*100)/(apple_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE PRODUCT-SECURITY@APPLE, FUERON PUBLICADAS EN 2019 \n")
print("     -      EL "+str(float(((apple_iot_2018*100)/(apple_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE PRODUCT-SECURITY@APPLE, FUERON PUBLICADAS EN 2018 O ANTERIORMENTE \n")
print("\n")
print("\n")
print("EN EL "+str(float(((android_iot*100)/total_assigner_iot)))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR ES SECURITY@ANDROID, LOS PORCENTAJES SEGUN FECHA DE PUBLICACION SON LOS SIGUIENTES : \n")
print("     -      EL "+str(float(((android_iot_2023*100)/(android_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY@ANDROID, FUERON PUBLICADAS EN 2023 \n")
print("     -      EL "+str(float(((android_iot_2022*100)/(android_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY@ANDROID, FUERON PUBLICADAS EN 2022 \n")
print("     -      EL "+str(float(((android_iot_2021*100)/(android_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY@ANDROID, FUERON PUBLICADAS EN 2021 \n")
print("     -      EL "+str(float(((android_iot_2020*100)/(android_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY@ANDROID, FUERON PUBLICADAS EN 2020 \n")
print("     -      EL "+str(float(((android_iot_2019*100)/(android_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY@ANDROID, FUERON PUBLICADAS EN 2019 \n")
print("     -      EL "+str(float(((android_iot_2018*100)/(android_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY@ANDROID, FUERON PUBLICADAS EN 2018 O ANTERIORMENTE \n")
print("\n")
print("\n")
print("EN EL "+str(float(((bitdefender_iot*100)/total_assigner_iot)))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR CVE-REQUESTS@BITDEFENDER, LOS PORCENTAJES SEGUN FECHA DE PUBLICACION SON LOS SIGUIENTES : \n")
print("     -      EL "+str(float(((bitdefender_iot_2023*100)/(bitdefender_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE CVE-REQUESTS@BITDEFENDER, FUERON PUBLICADAS EN 2023 \n")
print("     -      EL "+str(float(((bitdefender_iot_2022*100)/(bitdefender_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE CVE-REQUESTS@BITDEFENDER, FUERON PUBLICADAS EN 2022 \n")
print("     -      EL "+str(float(((bitdefender_iot_2021*100)/(bitdefender_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE CVE-REQUESTS@BITDEFENDER, FUERON PUBLICADAS EN 2021 \n")
print("     -      EL "+str(float(((bitdefender_iot_2020*100)/(bitdefender_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE CVE-REQUESTS@BITDEFENDER, FUERON PUBLICADAS EN 2020 \n")
print("     -      EL "+str(float(((bitdefender_iot_2019*100)/(bitdefender_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE CVE-REQUESTS@BITDEFENDER, FUERON PUBLICADAS EN 2019 \n")
print("     -      EL "+str(float(((bitdefender_iot_2018*100)/(bitdefender_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE CVE-REQUESTS@BITDEFENDER, FUERON PUBLICADAS EN 2018 O ANTERIORMENTE \n")
print("\n")
print("\n")
print("EN EL "+str(float(((mcafee_iot*100)/total_assigner_iot)))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR PSIRT@MCAFEE, LOS PORCENTAJES SEGUN FECHA DE PUBLICACION SON LOS SIGUIENTES : \n")
print("     -      EL "+str(float(((mcafee_iot_2023*100)/(mcafee_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE PSIRT@MCAFEE, FUERON PUBLICADAS EN 2023 \n")
print("     -      EL "+str(float(((mcafee_iot_2022*100)/(mcafee_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE PSIRT@MCAFEE, FUERON PUBLICADAS EN 2022 \n")
print("     -      EL "+str(float(((mcafee_iot_2021*100)/(mcafee_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE PSIRT@MCAFEE, FUERON PUBLICADAS EN 2021 \n")
print("     -      EL "+str(float(((mcafee_iot_2020*100)/(mcafee_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE PSIRT@MCAFEE, FUERON PUBLICADAS EN 2020 \n")
print("     -      EL "+str(float(((mcafee_iot_2019*100)/(mcafee_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE PSIRT@MCAFEE, FUERON PUBLICADAS EN 2019 \n")
print("     -      EL "+str(float(((mcafee_iot_2018*100)/(mcafee_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE PSIRT@MCAFEE, FUERON PUBLICADAS EN 2018 O ANTERIORMENTE \n")
print("\n")
print("\n")
print("EN EL "+str(float(((mozilla_iot*100)/total_assigner_iot)))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR ES SECURITY@MOZILLA, LOS PORCENTAJES SEGUN FECHA DE PUBLICACION SON LOS SIGUIENTES : \n")
print("     -      EL "+str(float(((mozilla_iot_2023*100)/(mozilla_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY@MOZILLA, FUERON PUBLICADAS EN 2023 \n")
print("     -      EL "+str(float(((mozilla_iot_2022*100)/(mozilla_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY@MOZILLA, FUERON PUBLICADAS EN 2022 \n")
print("     -      EL "+str(float(((mozilla_iot_2021*100)/(mozilla_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY@MOZILLA, FUERON PUBLICADAS EN 2021 \n")
print("     -      EL "+str(float(((mozilla_iot_2020*100)/(mozilla_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY@MOZILLA, FUERON PUBLICADAS EN 2020 \n")
print("     -      EL "+str(float(((mozilla_iot_2019*100)/(mozilla_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY@MOZILLA, FUERON PUBLICADAS EN 2019 \n")
print("     -      EL "+str(float(((mozilla_iot_2018*100)/(mozilla_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY@MOZILLA, FUERON PUBLICADAS EN 2018 O ANTERIORMENTE \n")
print("\n")
print("\n")
print("EN EL "+str(float(((hpe_iot*100)/total_assigner_iot)))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR ES SECURITY-ALERT@HPE, LOS PORCENTAJES SEGUN FECHA DE PUBLICACION SON LOS SIGUIENTES : \n")
print("     -      EL "+str(float(((hpe_iot_2023*100)/(hpe_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY-ALERT@HPE, FUERON PUBLICADAS EN 2023 \n")
print("     -      EL "+str(float(((hpe_iot_2022*100)/(hpe_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY-ALERT@HPE, FUERON PUBLICADAS EN 2022 \n")
print("     -      EL "+str(float(((hpe_iot_2021*100)/(hpe_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY-ALERT@HPE, FUERON PUBLICADAS EN 2021 \n")
print("     -      EL "+str(float(((hpe_iot_2020*100)/(hpe_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY-ALERT@HPE, FUERON PUBLICADAS EN 2020 \n")
print("     -      EL "+str(float(((hpe_iot_2019*100)/(hpe_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY-ALERT@HPE, FUERON PUBLICADAS EN 2019 \n")
print("     -      EL "+str(float(((hpe_iot_2018*100)/(hpe_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY-ALERT@HPE, FUERON PUBLICADAS EN 2018 O ANTERIORMENTE \n")
print("\n")
print("\n")
print("EN EL "+str(float(((rapid7_iot*100)/total_assigner_iot)))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR ES CVE@RAPID7, LOS PORCENTAJES SEGUN FECHA DE PUBLICACION SON LOS SIGUIENTES : \n")
print("     -      EL "+str(float(((rapid7_iot_2023*100)/(rapid7_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES CVE@RAPID7, FUERON PUBLICADAS EN 2023 \n")
print("     -      EL "+str(float(((rapid7_iot_2022*100)/(rapid7_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES CVE@RAPID7, FUERON PUBLICADAS EN 2022 \n")
print("     -      EL "+str(float(((rapid7_iot_2021*100)/(rapid7_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES CVE@RAPID7, FUERON PUBLICADAS EN 2021 \n")
print("     -      EL "+str(float(((rapid7_iot_2020*100)/(rapid7_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES CVE@RAPID7, FUERON PUBLICADAS EN 2020 \n")
print("     -      EL "+str(float(((rapid7_iot_2019*100)/(rapid7_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES CVE@RAPID7, FUERON PUBLICADAS EN 2019 \n")
print("     -      EL "+str(float(((rapid7_iot_2018*100)/(rapid7_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES CVE@RAPID7, FUERON PUBLICADAS EN 2018 O ANTERIORMENTE \n")
print("\n")
print("\n")
print("EN EL "+str(float(((fsecure_iot*100)/total_assigner_iot)))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR ES CVE-NOTIFICATIONS-US@F-SECURE, LOS PORCENTAJES SEGUN FECHA DE PUBLICACION SON LOS SIGUIENTES : \n")
print("     -      EL "+str(float(((fsecure_iot_2023*100)/(fsecure_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES CVE-NOTIFICATIONS-US@F-SECURE, FUERON PUBLICADAS EN 2023 \n")
print("     -      EL "+str(float(((fsecure_iot_2022*100)/(fsecure_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES CVE-NOTIFICATIONS-US@F-SECURE, FUERON PUBLICADAS EN 2022 \n")
print("     -      EL "+str(float(((fsecure_iot_2021*100)/(fsecure_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES CVE-NOTIFICATIONS-US@F-SECURE, FUERON PUBLICADAS EN 2021 \n")
print("     -      EL "+str(float(((fsecure_iot_2020*100)/(fsecure_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES CVE-NOTIFICATIONS-US@F-SECURE, FUERON PUBLICADAS EN 2020 \n")
print("     -      EL "+str(float(((fsecure_iot_2019*100)/(fsecure_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES CVE-NOTIFICATIONS-US@F-SECURE, FUERON PUBLICADAS EN 2019 \n")
print("     -      EL "+str(float(((fsecure_iot_2018*100)/(fsecure_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES CVE-NOTIFICATIONS-US@F-SECURE, FUERON PUBLICADAS EN 2018 O ANTERIORMENTE \n")
print("\n")
print("\n")
print("EN EL "+str(float(((other_assigner_iot*100)/total_assigner_iot)))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR OTRO DISTINTO A LOS ANTERIORES, LOS PORCENTAJES SEGUN FECHA DE PUBLICACION SON LOS SIGUIENTES : \n")
print("     -      EL "+str(float(((other_assigner_iot_2023*100)/(other_assigner_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE OTRO DISTINTO A LOS ANTERIORES, FUERON PUBLICADAS EN 2023 \n")
print("     -      EL "+str(float(((other_assigner_iot_2022*100)/(other_assigner_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE OTRO DISTINTO A LOS ANTERIORES, FUERON PUBLICADAS EN 2022 \n")
print("     -      EL "+str(float(((other_assigner_iot_2021*100)/(other_assigner_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE OTRO DISTINTO A LOS ANTERIORES, FUERON PUBLICADAS EN 2021 \n")
print("     -      EL "+str(float(((other_assigner_iot_2020*100)/(other_assigner_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE OTRO DISTINTO A LOS ANTERIORES, FUERON PUBLICADAS EN 2020 \n")
print("     -      EL "+str(float(((other_assigner_iot_2019*100)/(other_assigner_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE OTRO DISTINTO A LOS ANTERIORES, FUERON PUBLICADAS EN 2019 \n")
print("     -      EL "+str(float(((other_assigner_iot_2018*100)/(other_assigner_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE OTRO DISTINTO A LOS ANTERIORES, FUERON PUBLICADAS EN 2018 O ANTERIORMENTE \n")
print("\n")














print("________________________CVE ASIGNADOR CVE PARTE SMART HOME________________________")
print("\n")
print("\n")



#Variables donde almacenare el contador  ASIGNADOR CVE para la parte de SMART HOME
jpcert_sh=0
jpcert_sh_2023=0
jpcert_sh_2022=0
jpcert_sh_2021=0
jpcert_sh_2020=0
jpcert_sh_2019=0
jpcert_sh_2018=0

mitre_sh=0
mitre_sh_2023=0
mitre_sh_2022=0
mitre_sh_2021=0
mitre_sh_2020=0
mitre_sh_2019=0
mitre_sh_2018=0

cisco_sh=0
cisco_sh_2023=0
cisco_sh_2022=0
cisco_sh_2021=0
cisco_sh_2020=0
cisco_sh_2019=0
cisco_sh_2018=0

github_sh=0
github_sh_2023=0
github_sh_2022=0
github_sh_2021=0
github_sh_2020=0
github_sh_2019=0
github_sh_2018=0

redhat_sh=0
redhat_sh_2023=0
redhat_sh_2022=0
redhat_sh_2021=0
redhat_sh_2020=0
redhat_sh_2019=0
redhat_sh_2018=0

qualcomm_sh=0
qualcomm_sh_2023=0
qualcomm_sh_2022=0
qualcomm_sh_2021=0
qualcomm_sh_2020=0
qualcomm_sh_2019=0
qualcomm_sh_2018=0

apache_sh=0
apache_sh_2023=0
apache_sh_2022=0
apache_sh_2021=0
apache_sh_2020=0
apache_sh_2019=0
apache_sh_2018=0

oracle_sh=0
oracle_sh_2023=0
oracle_sh_2022=0
oracle_sh_2021=0
oracle_sh_2020=0
oracle_sh_2019=0
oracle_sh_2018=0

microsoft_sh=0
microsoft_sh_2023=0
microsoft_sh_2022=0
microsoft_sh_2021=0
microsoft_sh_2020=0
microsoft_sh_2019=0
microsoft_sh_2018=0

cert_sh=0
cert_sh_2023=0
cert_sh_2022=0
cert_sh_2021=0
cert_sh_2020=0
cert_sh_2019=0
cert_sh_2018=0

trendmicro_sh=0
trendmicro_sh_2023=0
trendmicro_sh_2022=0
trendmicro_sh_2021=0
trendmicro_sh_2020=0
trendmicro_sh_2019=0
trendmicro_sh_2018=0

nozomi_sh=0
nozomi_sh_2023=0
nozomi_sh_2022=0
nozomi_sh_2021=0
nozomi_sh_2020=0
nozomi_sh_2019=0
nozomi_sh_2018=0

hq_sh=0
hq_sh_2023=0
hq_sh_2022=0
hq_sh_2021=0
hq_sh_2020=0
hq_sh_2019=0
hq_sh_2018=0

kaspersky_sh=0
kaspersky_sh_2023=0
kaspersky_sh_2022=0
kaspersky_sh_2021=0
kaspersky_sh_2020=0
kaspersky_sh_2019=0
kaspersky_sh_2018=0

schneider_sh=0
schneider_sh_2023=0
schneider_sh_2022=0
schneider_sh_2021=0
schneider_sh_2020=0
schneider_sh_2019=0
schneider_sh_2018=0

apple_sh=0
apple_sh_2023=0
apple_sh_2022=0
apple_sh_2021=0
apple_sh_2020=0
apple_sh_2019=0
apple_sh_2018=0

android_sh=0
android_sh_2023=0
android_sh_2022=0
android_sh_2021=0
android_sh_2020=0
android_sh_2019=0
android_sh_2018=0

bitdefender_sh=0
bitdefender_sh_2023=0
bitdefender_sh_2022=0
bitdefender_sh_2021=0
bitdefender_sh_2020=0
bitdefender_sh_2019=0
bitdefender_sh_2018=0

mcafee_sh=0
mcafee_sh_2023=0
mcafee_sh_2022=0
mcafee_sh_2021=0
mcafee_sh_2020=0
mcafee_sh_2019=0
mcafee_sh_2018=0

mozilla_sh=0
mozilla_sh_2023=0
mozilla_sh_2022=0
mozilla_sh_2021=0
mozilla_sh_2020=0
mozilla_sh_2019=0
mozilla_sh_2018=0

hpe_sh=0
hpe_sh_2023=0
hpe_sh_2022=0
hpe_sh_2021=0
hpe_sh_2020=0
hpe_sh_2019=0
hpe_sh_2018=0

fsecure_sh=0
fsecure_sh_2023=0
fsecure_sh_2022=0
fsecure_sh_2021=0
fsecure_sh_2020=0
fsecure_sh_2019=0
fsecure_sh_2018=0

rapid7_sh=0
rapid7_sh_2023=0
rapid7_sh_2022=0
rapid7_sh_2021=0
rapid7_sh_2020=0
rapid7_sh_2019=0
rapid7_sh_2018=0

other_assigner_sh=0
other_assigner_sh_2023=0
other_assigner_sh_2022=0
other_assigner_sh_2021=0
other_assigner_sh_2020=0
other_assigner_sh_2019=0
other_assigner_sh_2018=0
#Variables donde almaceno la cantidad de assigner en los distintos anios
assigner_sh_2023=0
assigner_sh_2022=0
assigner_sh_2021=0
assigner_sh_2020=0
assigner_sh_2019=0
assigner_sh_2018=0

#Contador de total DE ASIGNADORES CVE con valores no nulos
total_assigner_sh=0


#Recorro los valores de ASIGNADOR CVE para la parte SMART HOME y despues consulto la fecha de publicacion

for j in range(0,len(df_cve_sh["CVE_Items.cve.CVE_data_meta.ASSIGNER"])):
    if(df_cve_sh["CVE_Items.cve.CVE_data_meta.ASSIGNER"][j] !='NONE'):
        total_assigner_sh+=1
        if("jpcert" in df_cve_sh["CVE_Items.cve.CVE_data_meta.ASSIGNER"][j]):
            jpcert_sh+=1
            str_anio_publidate_cve_sh=df_cve_sh["CVE_Items.publishedDate"][j].split("-")
            anio_publidate_cve_sh=int(str_anio_publidate_cve_sh[0])
            if(anio_publidate_cve_sh >= 2023):
                jpcert_sh_2023+=1
                assigner_sh_2023+=1
            elif(anio_publidate_cve_sh >= 2022):
                jpcert_sh_2022+=1
                assigner_sh_2022+=1
            elif(anio_publidate_cve_sh >= 2021):
                jpcert_sh_2021+=1
                assigner_sh_2021+=1
            elif(anio_publidate_cve_sh >= 2020):
                jpcert_sh_2020+=1
                assigner_sh_2020+=1
            elif(anio_publidate_cve_sh >= 2019):
                jpcert_sh_2019+=1
                assigner_sh_2019+=1
            else:
                assigner_sh_2018+=1
                jpcert_sh_2018+=1

        elif("@mitre" in df_cve_sh["CVE_Items.cve.CVE_data_meta.ASSIGNER"][j]):
            mitre_sh+=1
            str_anio_publidate_cve_sh=df_cve_sh["CVE_Items.publishedDate"][j].split("-")
            anio_publidate_cve_sh=int(str_anio_publidate_cve_sh[0])
            if(anio_publidate_cve_sh >= 2023):
                mitre_sh_2023+=1
                assigner_sh_2023+=1
            elif(anio_publidate_cve_sh >= 2022):
                mitre_sh_2022+=1
                assigner_sh_2022+=1
            elif(anio_publidate_cve_sh >= 2021):
                mitre_sh_2021+=1
                assigner_sh_2021+=1
            elif(anio_publidate_cve_sh >= 2020):
                mitre_sh_2020+=1
                assigner_sh_2020+=1
            elif(anio_publidate_cve_sh >= 2019):
                mitre_sh_2019+=1
                assigner_sh_2019+=1
            else:
                mitre_sh_2018+=1
                assigner_sh_2018+=1
        elif("@cisco" in df_cve_sh["CVE_Items.cve.CVE_data_meta.ASSIGNER"][j]):
            cisco_sh+=1
            str_anio_publidate_cve_sh=df_cve_sh["CVE_Items.publishedDate"][j].split("-")
            anio_publidate_cve_sh=int(str_anio_publidate_cve_sh[0])
            if(anio_publidate_cve_sh >= 2023):
                cisco_sh_2023+=1
                assigner_sh_2023+=1
            elif(anio_publidate_cve_sh >= 2022):
                cisco_sh_2022+=1
                assigner_sh_2022+=1
            elif(anio_publidate_cve_sh >= 2021):
                cisco_sh_2021+=1
                assigner_sh_2021+=1
            elif(anio_publidate_cve_sh >= 2020):
                cisco_sh_2020+=1
                assigner_sh_2020+=1
            elif(anio_publidate_cve_sh >= 2019):
                cisco_sh_2019+=1
                assigner_sh_2019+=1
            else:
                cisco_sh_2018+=1
                assigner_sh_2018+=1
        elif("@github" in df_cve_sh["CVE_Items.cve.CVE_data_meta.ASSIGNER"][j]):
            github_sh+=1
            str_anio_publidate_cve_sh=df_cve_sh["CVE_Items.publishedDate"][j].split("-")
            anio_publidate_cve_sh=int(str_anio_publidate_cve_sh[0])
            if(anio_publidate_cve_sh >= 2023):
                github_sh_2023+=1
                assigner_sh_2023+=1
            elif(anio_publidate_cve_sh >= 2022):
                github_sh_2022+=1
                assigner_sh_2022+=1
            elif(anio_publidate_cve_sh >= 2021):
                github_sh_2021+=1
                assigner_sh_2021+=1
            elif(anio_publidate_cve_sh >= 2020):
                github_sh_2020+=1
                assigner_sh_2020+=1
            elif(anio_publidate_cve_sh >= 2019):
                github_sh_2019+=1
                assigner_sh_2019+=1
            else:
                github_sh_2018+=1
                assigner_sh_2018+=1
        elif("@redhat" in df_cve_sh["CVE_Items.cve.CVE_data_meta.ASSIGNER"][j]):
            redhat_sh+=1
            str_anio_publidate_cve_sh=df_cve_sh["CVE_Items.publishedDate"][j].split("-")
            anio_publidate_cve_sh=int(str_anio_publidate_cve_sh[0])
            if(anio_publidate_cve_sh >= 2023):
                redhat_sh_2023+=1
                assigner_sh_2023+=1
            elif(anio_publidate_cve_sh >= 2022):
                redhat_sh_2022+=1
                assigner_sh_2022+=1
            elif(anio_publidate_cve_sh >= 2021):
                redhat_sh_2021+=1
                assigner_sh_2021+=1
            elif(anio_publidate_cve_sh >= 2020):
                redhat_sh_2020+=1
                assigner_sh_2020+=1
            elif(anio_publidate_cve_sh >= 2019):
                redhat_sh_2019+=1
                assigner_sh_2019+=1
            else:
                redhat_sh_2018+=1
                assigner_sh_2018+=1
        elif("@qualcomm" in df_cve_sh["CVE_Items.cve.CVE_data_meta.ASSIGNER"][j]):
            qualcomm_sh+=1
            str_anio_publidate_cve_sh=df_cve_sh["CVE_Items.publishedDate"][j].split("-")
            anio_publidate_cve_sh=int(str_anio_publidate_cve_sh[0])
            if(anio_publidate_cve_sh >= 2023):
                qualcomm_sh_2023+=1
                assigner_sh_2023+=1
            elif(anio_publidate_cve_sh >= 2022):
                qualcomm_sh_2022+=1
                assigner_sh_2022+=1
            elif(anio_publidate_cve_sh >= 2021):
                qualcomm_sh_2021+=1
                assigner_sh_2021+=1
            elif(anio_publidate_cve_sh >= 2020):
                qualcomm_sh_2020+=1
                assigner_sh_2020+=1
            elif(anio_publidate_cve_sh >= 2019):
                qualcomm_sh_2019+=1
                assigner_sh_2019+=1
            else:
                qualcomm_sh_2018+=1
                assigner_sh_2018+=1
        elif("@apache" in df_cve_sh["CVE_Items.cve.CVE_data_meta.ASSIGNER"][j]):
            apache_sh+=1
            str_anio_publidate_cve_sh=df_cve_sh["CVE_Items.publishedDate"][j].split("-")
            anio_publidate_cve_sh=int(str_anio_publidate_cve_sh[0])
            if(anio_publidate_cve_sh >= 2023):
                apache_sh_2023+=1
                assigner_sh_2023+=1
            elif(anio_publidate_cve_sh >= 2022):
                apache_sh_2022+=1
                assigner_sh_2022+=1
            elif(anio_publidate_cve_sh >= 2021):
                apache_sh_2021+=1
                assigner_sh_2021+=1
            elif(anio_publidate_cve_sh >= 2020):
                apache_sh_2020+=1
                assigner_sh_2020+=1
            elif(anio_publidate_cve_sh >= 2019):
                apache_sh_2019+=1
                assigner_sh_2019+=1
            else:
                apache_sh_2018+=1
                assigner_sh_2018+=1
        elif("@oracle" in df_cve_sh["CVE_Items.cve.CVE_data_meta.ASSIGNER"][j]):
            oracle_sh+=1
            str_anio_publidate_cve_sh=df_cve_sh["CVE_Items.publishedDate"][j].split("-")
            anio_publidate_cve_sh=int(str_anio_publidate_cve_sh[0])
            if(anio_publidate_cve_sh >= 2023):
                oracle_sh_2023+=1
                assigner_sh_2023+=1
            elif(anio_publidate_cve_sh >= 2022):
                oracle_sh_2022+=1
                assigner_sh_2022+=1
            elif(anio_publidate_cve_sh >= 2021):
                oracle_sh_2021+=1
                assigner_sh_2021+=1
            elif(anio_publidate_cve_sh >= 2020):
                oracle_sh_2020+=1
                assigner_sh_2020+=1
            elif(anio_publidate_cve_sh >= 2019):
                oracle_sh_2019+=1
                assigner_sh_2019+=1
            else:
                oracle_sh_2018+=1
                assigner_sh_2018+=1
        elif("@microsoft" in df_cve_sh["CVE_Items.cve.CVE_data_meta.ASSIGNER"][j]):
            microsoft_sh+=1
            str_anio_publidate_cve_sh=df_cve_sh["CVE_Items.publishedDate"][j].split("-")
            anio_publidate_cve_sh=int(str_anio_publidate_cve_sh[0])
            if(anio_publidate_cve_sh >= 2023):
                microsoft_sh_2023+=1
                assigner_sh_2023+=1
            elif(anio_publidate_cve_sh >= 2022):
                microsoft_sh_2022+=1
                assigner_sh_2022+=1
            elif(anio_publidate_cve_sh >= 2021):
                microsoft_sh_2021+=1
                assigner_sh_2021+=1
            elif(anio_publidate_cve_sh >= 2020):
                microsoft_sh_2020+=1
                assigner_sh_2020+=1
            elif(anio_publidate_cve_sh >= 2019):
                microsoft_sh_2019+=1
                assigner_sh_2019+=1
            else:
                microsoft_sh_2018+=1
                assigner_sh_2018+=1
        elif("@cert" in df_cve_sh["CVE_Items.cve.CVE_data_meta.ASSIGNER"][j]):
            cert_sh+=1
            str_anio_publidate_cve_sh=df_cve_sh["CVE_Items.publishedDate"][j].split("-")
            anio_publidate_cve_sh=int(str_anio_publidate_cve_sh[0])
            if(anio_publidate_cve_sh >= 2023):
                cert_sh_2023+=1
                assigner_sh_2023+=1
            elif(anio_publidate_cve_sh >= 2022):
                cert_sh_2022+=1
                assigner_sh_2022+=1
            elif(anio_publidate_cve_sh >= 2021):
                cert_sh_2021+=1
                assigner_sh_2021+=1
            elif(anio_publidate_cve_sh >= 2020):
                cert_sh_2020+=1
                assigner_sh_2020+=1
            elif(anio_publidate_cve_sh >= 2019):
                cert_sh_2019+=1
                assigner_sh_2019+=1
            else:
                cert_sh_2018+=1
                assigner_sh_2018+=1
        elif("@trendmicro" in df_cve_sh["CVE_Items.cve.CVE_data_meta.ASSIGNER"][j]):
            trendmicro_sh+=1
            str_anio_publidate_cve_sh=df_cve_sh["CVE_Items.publishedDate"][j].split("-")
            anio_publidate_cve_sh=int(str_anio_publidate_cve_sh[0])
            if(anio_publidate_cve_sh >= 2023):
                trendmicro_sh_2023+=1
                assigner_sh_2023+=1
            elif(anio_publidate_cve_sh >= 2022):
                trendmicro_sh_2022+=1
                assigner_sh_2022+=1
            elif(anio_publidate_cve_sh >= 2021):
                trendmicro_sh_2021+=1
                assigner_sh_2021+=1
            elif(anio_publidate_cve_sh >= 2020):
                trendmicro_sh_2020+=1
                assigner_sh_2020+=1
            elif(anio_publidate_cve_sh >= 2019):
                trendmicro_sh_2019+=1
                assigner_sh_2019+=1
            else:
                trendmicro_sh_2018+=1
                assigner_sh_2018+=1
        elif("@nozomi" in df_cve_sh["CVE_Items.cve.CVE_data_meta.ASSIGNER"][j]):
            nozomi_sh+=1
            str_anio_publidate_cve_sh=df_cve_sh["CVE_Items.publishedDate"][j].split("-")
            anio_publidate_cve_sh=int(str_anio_publidate_cve_sh[0])
            if(anio_publidate_cve_sh >= 2023):
                nozomi_sh_2023+=1
                assigner_sh_2023+=1
            elif(anio_publidate_cve_sh >= 2022):
                nozomi_sh_2022+=1
                assigner_sh_2022+=1
            elif(anio_publidate_cve_sh >= 2021):
                nozomi_sh_2021+=1
                assigner_sh_2021+=1
            elif(anio_publidate_cve_sh >= 2020):
                nozomi_sh_2020+=1
                assigner_sh_2020+=1
            elif(anio_publidate_cve_sh >= 2019):
                nozomi_sh_2019+=1
                assigner_sh_2019+=1
            else:
                nozomi_sh_2018+=1
                assigner_sh_2018+=1
        elif("@hq" in df_cve_sh["CVE_Items.cve.CVE_data_meta.ASSIGNER"][j]):
            hq_sh+=1
            str_anio_publidate_cve_sh=df_cve_sh["CVE_Items.publishedDate"][j].split("-")
            anio_publidate_cve_sh=int(str_anio_publidate_cve_sh[0])
            if(anio_publidate_cve_sh >= 2023):
                hq_sh_2023+=1
                assigner_sh_2023+=1
            elif(anio_publidate_cve_sh >= 2022):
                hq_sh_2022+=1
                assigner_sh_2022+=1
            elif(anio_publidate_cve_sh >= 2021):
                hq_sh_2021+=1
                assigner_sh_2021+=1
            elif(anio_publidate_cve_sh >= 2020):
                hq_sh_2020+=1
                assigner_sh_2020+=1
            elif(anio_publidate_cve_sh >= 2019):
                hq_sh_2019+=1
                assigner_sh_2019+=1
            else:
                hq_sh_2018+=1
                assigner_sh_2018+=1
        elif("@kaspersky" in df_cve_sh["CVE_Items.cve.CVE_data_meta.ASSIGNER"][j]):
            kaspersky_sh+=1
            str_anio_publidate_cve_sh=df_cve_sh["CVE_Items.publishedDate"][j].split("-")
            anio_publidate_cve_sh=int(str_anio_publidate_cve_sh[0])
            if(anio_publidate_cve_sh >= 2023):
                kaspersky_sh_2023+=1
                assigner_sh_2023+=1
            elif(anio_publidate_cve_sh >= 2022):
                kaspersky_sh_2022+=1
                assigner_sh_2022+=1
            elif(anio_publidate_cve_sh >= 2021):
                kaspersky_sh_2021+=1
                assigner_sh_2021+=1
            elif(anio_publidate_cve_sh >= 2020):
                kaspersky_sh_2020+=1
                assigner_sh_2020+=1
            elif(anio_publidate_cve_sh >= 2019):
                kaspersky_sh_2019+=1
                assigner_sh_2019+=1
            else:
                kaspersky_sh_2018+=1
                assigner_sh_2018+=1
        elif("@schneider" in df_cve_sh["CVE_Items.cve.CVE_data_meta.ASSIGNER"][j]):
            schneider_sh+=1
            str_anio_publidate_cve_sh=df_cve_sh["CVE_Items.publishedDate"][j].split("-")
            anio_publidate_cve_sh=int(str_anio_publidate_cve_sh[0])
            if(anio_publidate_cve_sh >= 2023):
                schneider_sh_2023+=1
                assigner_sh_2023+=1
            elif(anio_publidate_cve_sh >= 2022):
                schneider_sh_2022+=1
                assigner_sh_2022+=1
            elif(anio_publidate_cve_sh >= 2021):
                schneider_sh_2021+=1
                assigner_sh_2021+=1
            elif(anio_publidate_cve_sh >= 2020):
                schneider_sh_2020+=1
                assigner_sh_2020+=1
            elif(anio_publidate_cve_sh >= 2019):
                schneider_sh_2019+=1
                assigner_sh_2019+=1
            else:
                schneider_sh_2018+=1
                assigner_sh_2018+=1
        elif("@apple" in df_cve_sh["CVE_Items.cve.CVE_data_meta.ASSIGNER"][j]):
            apple_sh+=1
            str_anio_publidate_cve_sh=df_cve_sh["CVE_Items.publishedDate"][j].split("-")
            anio_publidate_cve_sh=int(str_anio_publidate_cve_sh[0])
            if(anio_publidate_cve_sh >= 2023):
                apple_sh_2023+=1
                assigner_sh_2023+=1
            elif(anio_publidate_cve_sh >= 2022):
                apple_sh_2022+=1
                assigner_sh_2022+=1
            elif(anio_publidate_cve_sh >= 2021):
                apple_sh_2021+=1
                assigner_sh_2021+=1
            elif(anio_publidate_cve_sh >= 2020):
                apple_sh_2020+=1
                assigner_sh_2020+=1
            elif(anio_publidate_cve_sh >= 2019):
                apple_sh_2019+=1
                assigner_sh_2019+=1
            else:
                apple_sh_2018+=1
                assigner_sh_2018+=1
        elif("@android" in df_cve_sh["CVE_Items.cve.CVE_data_meta.ASSIGNER"][j]):
            android_sh+=1
            str_anio_publidate_cve_sh=df_cve_sh["CVE_Items.publishedDate"][j].split("-")
            anio_publidate_cve_sh=int(str_anio_publidate_cve_sh[0])
            if(anio_publidate_cve_sh >= 2023):
                android_sh_2023+=1
                assigner_sh_2023+=1
            elif(anio_publidate_cve_sh >= 2022):
                android_sh_2022+=1
                assigner_sh_2022+=1
            elif(anio_publidate_cve_sh >= 2021):
                android_sh_2021+=1
                assigner_sh_2021+=1
            elif(anio_publidate_cve_sh >= 2020):
                android_sh_2020+=1
                assigner_sh_2020+=1
            elif(anio_publidate_cve_sh >= 2019):
                android_sh_2019+=1
                assigner_sh_2019+=1
            else:
                android_sh_2018+=1
                assigner_sh_2018+=1
        elif("@bitdefender" in df_cve_sh["CVE_Items.cve.CVE_data_meta.ASSIGNER"][j]):
            bitdefender_sh+=1
            str_anio_publidate_cve_sh=df_cve_sh["CVE_Items.publishedDate"][j].split("-")
            anio_publidate_cve_sh=int(str_anio_publidate_cve_sh[0])
            if(anio_publidate_cve_sh >= 2023):
                bitdefender_sh_2023+=1
                assigner_sh_2023+=1
            elif(anio_publidate_cve_sh >= 2022):
                bitdefender_sh_2022+=1
                assigner_sh_2022+=1
            elif(anio_publidate_cve_sh >= 2021):
                bitdefender_sh_2021+=1
                assigner_sh_2021+=1
            elif(anio_publidate_cve_sh >= 2020):
                bitdefender_sh_2020+=1
                assigner_sh_2020+=1
            elif(anio_publidate_cve_sh >= 2019):
                bitdefender_sh_2019+=1
                assigner_sh_2019+=1
            else:
                bitdefender_sh_2018+=1
                assigner_sh_2018+=1
        elif("@mcafee" in df_cve_sh["CVE_Items.cve.CVE_data_meta.ASSIGNER"][j]):
            mcafee_sh+=1
            str_anio_publidate_cve_sh=df_cve_sh["CVE_Items.publishedDate"][j].split("-")
            anio_publidate_cve_sh=int(str_anio_publidate_cve_sh[0])
            if(anio_publidate_cve_sh >= 2023):
                mcafee_sh_2023+=1
                assigner_sh_2023+=1
            elif(anio_publidate_cve_sh >= 2022):
                mcafee_sh_2022+=1
                assigner_sh_2022+=1
            elif(anio_publidate_cve_sh >= 2021):
                mcafee_sh_2021+=1
                assigner_sh_2021+=1
            elif(anio_publidate_cve_sh >= 2020):
                mcafee_sh_2020+=1
                assigner_sh_2020+=1
            elif(anio_publidate_cve_sh >= 2019):
                mcafee_sh_2019+=1
                assigner_sh_2019+=1
            else:
                mcafee_sh_2018+=1  
                assigner_sh_2018+=1
        elif("@mozilla" in df_cve_sh["CVE_Items.cve.CVE_data_meta.ASSIGNER"][j]):
            mozilla_sh+=1
            str_anio_publidate_cve_sh=df_cve_sh["CVE_Items.publishedDate"][j].split("-")
            anio_publidate_cve_sh=int(str_anio_publidate_cve_sh[0])
            if(anio_publidate_cve_sh >= 2023):
                mozilla_sh_2023+=1
                assigner_sh_2023+=1
            elif(anio_publidate_cve_sh >= 2022):
                mozilla_sh_2022+=1
                assigner_sh_2022+=1
            elif(anio_publidate_cve_sh >= 2021):
                mozilla_sh_2021+=1
                assigner_sh_2021+=1
            elif(anio_publidate_cve_sh >= 2020):
                mozilla_sh_2020+=1
                assigner_sh_2020+=1
            elif(anio_publidate_cve_sh >= 2019):
                mozilla_sh_2019+=1
                assigner_sh_2019+=1
            else:
                mozilla_sh_2018+=1
                assigner_sh_2018+=1
        elif("@hpe" in df_cve_sh["CVE_Items.cve.CVE_data_meta.ASSIGNER"][j]):
            hpe_sh+=1
            str_anio_publidate_cve_sh=df_cve_sh["CVE_Items.publishedDate"][j].split("-")
            anio_publidate_cve_sh=int(str_anio_publidate_cve_sh[0])
            if(anio_publidate_cve_sh >= 2023):
                hpe_sh_2023+=1
                assigner_sh_2023+=1
            elif(anio_publidate_cve_sh >= 2022):
                hpe_sh_2022+=1
                assigner_sh_2022+=1
            elif(anio_publidate_cve_sh >= 2021):
                hpe_sh_2021+=1
                assigner_sh_2021+=1
            elif(anio_publidate_cve_sh >= 2020):
                hpe_sh_2020+=1
                assigner_sh_2020+=1
            elif(anio_publidate_cve_sh >= 2019):
                hpe_sh_2019+=1
                assigner_sh_2019+=1
            else:
                hpe_sh_2018+=1 
                assigner_sh_2018+=1
        elif("@f-secure" in df_cve_sh["CVE_Items.cve.CVE_data_meta.ASSIGNER"][j]):
            fsecure_sh+=1
            str_anio_publidate_cve_sh=df_cve_sh["CVE_Items.publishedDate"][j].split("-")
            anio_publidate_cve_sh=int(str_anio_publidate_cve_sh[0])
            if(anio_publidate_cve_sh >= 2023):
                fsecure_sh_2023+=1
                assigner_sh_2023+=1
            elif(anio_publidate_cve_sh >= 2022):
                fsecure_sh_2022+=1
                assigner_sh_2022+=1
            elif(anio_publidate_cve_sh >= 2021):
                fsecure_sh_2021+=1
                assigner_sh_2021+=1
            elif(anio_publidate_cve_sh >= 2020):
                fsecure_sh_2020+=1
                assigner_sh_2020+=1
            elif(anio_publidate_cve_sh >= 2019):
                fsecure_sh_2019+=1
                assigner_sh_2019+=1
            else:
                fsecure_sh_2018+=1 
                assigner_sh_2018+=1
        elif("@rapid7" in df_cve_sh["CVE_Items.cve.CVE_data_meta.ASSIGNER"][j]):
            rapid7_sh+=1
            str_anio_publidate_cve_sh=df_cve_sh["CVE_Items.publishedDate"][j].split("-")
            anio_publidate_cve_sh=int(str_anio_publidate_cve_sh[0])
            if(anio_publidate_cve_sh >= 2023):
                rapid7_sh_2023+=1
                assigner_sh_2023+=1
            elif(anio_publidate_cve_sh >= 2022):
                rapid7_sh_2022+=1
                assigner_sh_2022+=1
            elif(anio_publidate_cve_sh >= 2021):
                rapid7_sh_2021+=1
                assigner_sh_2021+=1
            elif(anio_publidate_cve_sh >= 2020):
                rapid7_sh_2020+=1
                assigner_sh_2020+=1
            elif(anio_publidate_cve_sh >= 2019):
                rapid7_sh_2019+=1
                assigner_sh_2019+=1
            else:
                rapid7_sh_2018+=1 
                assigner_sh_2018+=1
        else:
            other_assigner_sh+=1
            str_anio_publidate_cve_sh=df_cve_sh["CVE_Items.publishedDate"][j].split("-")
            anio_publidate_cve_sh=int(str_anio_publidate_cve_sh[0])
            if(anio_publidate_cve_sh >= 2023):
                other_assigner_sh_2023+=1
                assigner_sh_2023+=1
            elif(anio_publidate_cve_sh >= 2022):
                other_assigner_sh_2022+=1
                assigner_sh_2022+=1
            elif(anio_publidate_cve_sh >= 2021):
                other_assigner_sh_2021+=1
                assigner_sh_2021+=1
            elif(anio_publidate_cve_sh >= 2020):
                other_assigner_sh_2020+=1
                assigner_sh_2020+=1
            elif(anio_publidate_cve_sh >= 2019):
                other_assigner_sh_2019+=1
                assigner_sh_2019+=1
            else:
                other_assigner_sh_2018+=1
                assigner_sh_2018+=1
    

print("************************** ESTADÍSTICAS CVE RELACION FECHA DE PUBLICACION Y ASIGNADOR CVE PARTE SMART HOME********************************")
print("\n")
print(" -  DE UN TOTAL DE "+str(total_assigner_sh)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ESTÁ DEFINIDO, LAS ESTADÍSTICAS DE ASSIGNER Y FECHA DE PUBLICACION SON LAS SIGUIENTES  : \n")
print("\n")
print(" -  DE UN TOTAL DE "+str(assigner_sh_2023)+" VULNERABILIDADES PUBLICADAS EN 2023, LAS ESTADÍSTICAS DE ASIGNADORES CVE SON LAS SIGUIENTES : \n")
print("     -      EN "+str(jpcert_sh_2023)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES VULTURES@JPCERT\n")
print("     -      EN "+str(mitre_sh_2023)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES CVE@MITRE \n")
print("     -      EN "+str(cisco_sh_2023)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES TALOS-CNA@CISCO \n")
print("     -      EN "+str(github_sh_2023)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY-ADVISORIES@GITHUB \n")
print("     -      EN "+str(redhat_sh_2023)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES SECALERT@REDHAT \n")
print("     -      EN "+str(qualcomm_sh_2023)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY.CNA@QUALCOMM \n")
print("     -      EN "+str(apache_sh_2023)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY@APACHE.ORG \n")
print("     -      EN "+str(oracle_sh_2023)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES SECALERT_US@ORACLE \n")
print("     -      EN "+str(microsoft_sh_2023)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURE@MICROSOFT \n")
print("     -      EN "+str(cert_sh_2023)+" VULNERABILIDADES EL ASIGNADOR DE CVE INFO@CERT.VDE \n")
print("     -      EN "+str(trendmicro_sh_2023)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY@TRENDMICRO \n")
print("     -      EN "+str(nozomi_sh_2023)+" VULNERABILIDADES EL ASIGNADOR DE CVE PRODSEC@NOZOMINETWORKS \n")
print("     -      EN "+str(hq_sh_2023)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES ICS-CERT@HQ.DHS.GOV \n")
print("     -      EN "+str(kaspersky_sh_2023)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES VULNERABILITY@KASPERSKY \n")
print("     -      EN "+str(schneider_sh_2023)+" VULNERABILIDADES EL ASIGNADOR DE CVE CYBERSECURITY@SCHNEIDER-ELECTRIC \n")
print("     -      EN "+str(apple_sh_2023)+" VULNERABILIDADES EL ASIGNADOR DE CVE PRODUCT-SECURITY@APPLE \n")
print("     -      EN "+str(android_sh_2023)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY@ANDROID \n")
print("     -      EN "+str(bitdefender_sh_2023)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES CVE-REQUESTS@BITDEFENDER \n")
print("     -      EN "+str(mcafee_sh_2023)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES PSIRT@MCAFEE \n")
print("     -      EN "+str(mozilla_sh_2023)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY@MOZILLA \n")
print("     -      EN "+str(hpe_sh_2023)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY-ALERT@HPE \n")
print("     -      EN "+str(fsecure_sh_2023)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES CVE-NOTIFICATIONS-US@F-SECURE.COM \n")
print("     -      EN "+str(rapid7_sh_2023)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES CVE@RAPID7 \n")
print("     -      EN "+str(other_assigner_sh_2023)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES DISTINTO DE LOS ANTERIORES \n")
print("\n")
print("\n")
print(" DE UN TOTAL DE "+str(assigner_sh_2022)+" VULNERABILIDADES PUBLICADAS EN 2022, LAS ESTADÍSTICAS DE ASIGNADORES CVE SON LAS SIGUIENTES : \n")
print("     -      EN "+str(jpcert_sh_2022)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES VULTURES@JPCERT\n")
print("     -      EN "+str(mitre_sh_2022)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES CVE@MITRE \n")
print("     -      EN "+str(cisco_sh_2022)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES TALOS-CNA@CISCO \n")
print("     -      EN "+str(github_sh_2022)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY-ADVISORIES@GITHUB \n")
print("     -      EN "+str(redhat_sh_2022)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES SECALERT@REDHAT \n")
print("     -      EN "+str(qualcomm_sh_2022)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY.CNA@QUALCOMM \n")
print("     -      EN "+str(apache_sh_2022)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY@APACHE.ORG \n")
print("     -      EN "+str(oracle_sh_2022)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES SECALERT_US@ORACLE \n")
print("     -      EN "+str(microsoft_sh_2022)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURE@MICROSOFT \n")
print("     -      EN "+str(cert_sh_2022)+" VULNERABILIDADES EL ASIGNADOR DE CVE INFO@CERT.VDE \n")
print("     -      EN "+str(trendmicro_sh_2022)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY@TRENDMICRO \n")
print("     -      EN "+str(nozomi_sh_2022)+" VULNERABILIDADES EL ASIGNADOR DE CVE PRODSEC@NOZOMINETWORKS \n")
print("     -      EN "+str(hq_sh_2022)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES ICS-CERT@HQ.DHS.GOV \n")
print("     -      EN "+str(kaspersky_sh_2022)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES VULNERABILITY@KASPERSKY \n")
print("     -      EN "+str(schneider_sh_2022)+" VULNERABILIDADES EL ASIGNADOR DE CVE CYBERSECURITY@SCHNEIDER-ELECTRIC \n")
print("     -      EN "+str(apple_sh_2022)+" VULNERABILIDADES EL ASIGNADOR DE CVE PRODUCT-SECURITY@APPLE \n")
print("     -      EN "+str(android_sh_2022)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY@ANDROID \n")
print("     -      EN "+str(bitdefender_sh_2022)+" VULNERABILIDADES EL ASIGNADOR DE CVE CVE-REQUESTS@BITDEFENDER \n")
print("     -      EN "+str(mcafee_sh_2022)+" VULNERABILIDADES EL ASIGNADOR DE CVE PSIRT@MCAFEE \n")
print("     -      EN "+str(mozilla_sh_2022)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY@MOZILLA \n")
print("     -      EN "+str(hpe_sh_2022)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY-ALERT@HPE \n")
print("     -      EN "+str(fsecure_sh_2022)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES CVE-NOTIFICATIONS-US@F-SECURE.COM \n")
print("     -      EN "+str(rapid7_sh_2022)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES CVE@RAPID7 \n")
print("     -      EN "+str(other_assigner_sh_2022)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES DISTINTO DE LOS ANTERIORES \n")
print("\n")
print("\n")
print(" DE UN TOTAL DE "+str(assigner_sh_2021)+" VULNERABILIDADES PUBLICADAS EN 2021, LAS ESTADÍSTICAS DE ASIGNADORES CVE SON LAS SIGUIENTES : \n")
print("     -      EN "+str(jpcert_sh_2021)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES VULTURES@JPCERT\n")
print("     -      EN "+str(mitre_sh_2021)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES CVE@MITRE \n")
print("     -      EN "+str(cisco_sh_2021)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES TALOS-CNA@CISCO \n")
print("     -      EN "+str(github_sh_2021)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY-ADVISORIES@GITHUB \n")
print("     -      EN "+str(redhat_sh_2021)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES SECALERT@REDHAT \n")
print("     -      EN "+str(qualcomm_sh_2021)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY.CNA@QUALCOMM \n")
print("     -      EN "+str(apache_sh_2021)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY@APACHE.ORG \n")
print("     -      EN "+str(oracle_sh_2021)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES SECALERT_US@ORACLE \n")
print("     -      EN "+str(microsoft_sh_2021)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURE@MICROSOFT \n")
print("     -      EN "+str(cert_sh_2021)+" VULNERABILIDADES EL ASIGNADOR DE CVE INFO@CERT.VDE \n")
print("     -      EN "+str(trendmicro_sh_2021)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY@TRENDMICRO \n")
print("     -      EN "+str(nozomi_sh_2021)+" VULNERABILIDADES EL ASIGNADOR DE CVE PRODSEC@NOZOMINETWORKS \n")
print("     -      EN "+str(hq_sh_2021)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES ICS-CERT@HQ.DHS.GOV \n")
print("     -      EN "+str(kaspersky_sh_2021)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES VULNERABILITY@KASPERSKY \n")
print("     -      EN "+str(schneider_sh_2021)+" VULNERABILIDADES EL ASIGNADOR DE CVE CYBERSECURITY@SCHNEIDER-ELECTRIC \n")
print("     -      EN "+str(apple_sh_2021)+" VULNERABILIDADES EL ASIGNADOR DE CVE PRODUCT-SECURITY@APPLE \n")
print("     -      EN "+str(android_sh_2021)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY@ANDROID \n")
print("     -      EN "+str(bitdefender_sh_2021)+" VULNERABILIDADES EL ASIGNADOR DE CVE CVE-REQUESTS@BITDEFENDER \n")
print("     -      EN "+str(mcafee_sh_2021)+" VULNERABILIDADES EL ASIGNADOR DE CVE PSIRT@MCAFEE \n")
print("     -      EN "+str(mozilla_sh_2021)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY@MOZILLA \n")
print("     -      EN "+str(hpe_sh_2021)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY-ALERT@HPE \n")
print("     -      EN "+str(fsecure_sh_2021)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES CVE-NOTIFICATIONS-US@F-SECURE.COM \n")
print("     -      EN "+str(rapid7_sh_2021)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES CVE@RAPID7 \n")
print("     -      EN "+str(other_assigner_sh_2021)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES DISTINTO DE LOS ANTERIORES \n")
print("\n")
print("\n")
print(" DE UN TOTAL DE "+str(assigner_sh_2020)+" VULNERABILIDADES PUBLICADAS EN 2020, LAS ESTADÍSTICAS DE ASIGNADORES CVE SON LAS SIGUIENTES : \n")
print("     -      EN "+str(jpcert_sh_2020)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES VULTURES@JPCERT\n")
print("     -      EN "+str(mitre_sh_2020)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES CVE@MITRE \n")
print("     -      EN "+str(cisco_sh_2020)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES TALOS-CNA@CISCO \n")
print("     -      EN "+str(github_sh_2020)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY-ADVISORIES@GITHUB \n")
print("     -      EN "+str(redhat_sh_2020)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES SECALERT@REDHAT \n")
print("     -      EN "+str(qualcomm_sh_2020)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY.CNA@QUALCOMM \n")
print("     -      EN "+str(apache_sh_2020)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY@APACHE.ORG \n")
print("     -      EN "+str(oracle_sh_2020)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES SECALERT_US@ORACLE \n")
print("     -      EN "+str(microsoft_sh_2020)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURE@MICROSOFT \n")
print("     -      EN "+str(cert_sh_2020)+" VULNERABILIDADES EL ASIGNADOR DE CVE INFO@CERT.VDE \n")
print("     -      EN "+str(trendmicro_sh_2020)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY@TRENDMICRO \n")
print("     -      EN "+str(nozomi_sh_2020)+" VULNERABILIDADES EL ASIGNADOR DE CVE PRODSEC@NOZOMINETWORKS \n")
print("     -      EN "+str(hq_sh_2020)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES ICS-CERT@HQ.DHS.GOV \n")
print("     -      EN "+str(kaspersky_sh_2020)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES VULNERABILITY@KASPERSKY \n")
print("     -      EN "+str(schneider_sh_2020)+" VULNERABILIDADES EL ASIGNADOR DE CVE CYBERSECURITY@SCHNEIDER-ELECTRIC \n")
print("     -      EN "+str(apple_sh_2020)+" VULNERABILIDADES EL ASIGNADOR DE CVE PRODUCT-SECURITY@APPLE \n")
print("     -      EN "+str(android_sh_2020)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY@ANDROID \n")
print("     -      EN "+str(bitdefender_sh_2020)+" VULNERABILIDADES EL ASIGNADOR DE CVE CVE-REQUESTS@BITDEFENDER \n")
print("     -      EN "+str(mcafee_sh_2020)+" VULNERABILIDADES EL ASIGNADOR DE CVE PSIRT@MCAFEE \n")
print("     -      EN "+str(mozilla_sh_2020)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY@MOZILLA \n")
print("     -      EN "+str(hpe_sh_2020)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY-ALERT@HPE \n")
print("     -      EN "+str(fsecure_sh_2020)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES CVE-NOTIFICATIONS-US@F-SECURE.COM \n")
print("     -      EN "+str(rapid7_sh_2020)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES CVE@RAPID7 \n")
print("     -      EN "+str(other_assigner_sh_2020)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES DISTINTO DE LOS ANTERIORES \n")
print("\n")
print("\n")
print(" DE UN TOTAL DE "+str(assigner_sh_2019)+" VULNERABILIDADES PUBLICADAS EN 2019, LAS ESTADÍSTICAS DE ASIGNADORES CVE SON LAS SIGUIENTES : \n")
print("     -      EN "+str(jpcert_sh_2019)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES VULTURES@JPCERT\n")
print("     -      EN "+str(mitre_sh_2019)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES CVE@MITRE \n")
print("     -      EN "+str(cisco_sh_2019)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES TALOS-CNA@CISCO \n")
print("     -      EN "+str(github_sh_2019)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY-ADVISORIES@GITHUB \n")
print("     -      EN "+str(redhat_sh_2019)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES SECALERT@REDHAT \n")
print("     -      EN "+str(qualcomm_sh_2019)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY.CNA@QUALCOMM \n")
print("     -      EN "+str(apache_sh_2019)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY@APACHE.ORG \n")
print("     -      EN "+str(oracle_sh_2019)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES SECALERT_US@ORACLE \n")
print("     -      EN "+str(microsoft_sh_2019)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURE@MICROSOFT \n")
print("     -      EN "+str(cert_sh_2019)+" VULNERABILIDADES EL ASIGNADOR DE CVE INFO@CERT.VDE \n")
print("     -      EN "+str(trendmicro_sh_2019)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY@TRENDMICRO \n")
print("     -      EN "+str(nozomi_sh_2019)+" VULNERABILIDADES EL ASIGNADOR DE CVE PRODSEC@NOZOMINETWORKS \n")
print("     -      EN "+str(hq_sh_2019)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES ICS-CERT@HQ.DHS.GOV \n")
print("     -      EN "+str(kaspersky_sh_2019)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES VULNERABILITY@KASPERSKY \n")
print("     -      EN "+str(schneider_sh_2019)+" VULNERABILIDADES EL ASIGNADOR DE CVE CYBERSECURITY@SCHNEIDER-ELECTRIC \n")
print("     -      EN "+str(apple_sh_2019)+" VULNERABILIDADES EL ASIGNADOR DE CVE PRODUCT-SECURITY@APPLE \n")
print("     -      EN "+str(android_sh_2019)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY@ANDROID \n")
print("     -      EN "+str(bitdefender_sh_2019)+" VULNERABILIDADES EL ASIGNADOR DE CVE CVE-REQUESTS@BITDEFENDER \n")
print("     -      EN "+str(mcafee_sh_2019)+" VULNERABILIDADES EL ASIGNADOR DE CVE PSIRT@MCAFEE \n")
print("     -      EN "+str(mozilla_sh_2019)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY@MOZILLA \n")
print("     -      EN "+str(hpe_sh_2019)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY-ALERT@HPE \n")
print("     -      EN "+str(fsecure_sh_2019)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES CVE-NOTIFICATIONS-US@F-SECURE.COM \n")
print("     -      EN "+str(rapid7_sh_2019)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES CVE@RAPID7 \n")
print("     -      EN "+str(other_assigner_sh_2019)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES DISTINTO DE LOS ANTERIORES \n")
print("\n")
print("\n")
print(" DE UN TOTAL DE "+str(assigner_sh_2018)+" VULNERABILIDADES PUBLICADAS EN 2018 O ANTERIORMENTE, LAS ESTADÍSTICAS DE ASIGNADORES CVE SON LAS SIGUIENTES : \n")
print("     -      EN "+str(jpcert_sh_2018)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES VULTURES@JPCERT\n")
print("     -      EN "+str(mitre_sh_2018)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES CVE@MITRE \n")
print("     -      EN "+str(cisco_sh_2018)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES TALOS-CNA@CISCO \n")
print("     -      EN "+str(github_sh_2018)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY-ADVISORIES@GITHUB \n")
print("     -      EN "+str(redhat_sh_2018)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES SECALERT@REDHAT \n")
print("     -      EN "+str(qualcomm_sh_2018)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY.CNA@QUALCOMM \n")
print("     -      EN "+str(apache_sh_2018)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY@APACHE.ORG \n")
print("     -      EN "+str(oracle_sh_2018)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES SECALERT_US@ORACLE \n")
print("     -      EN "+str(microsoft_sh_2018)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURE@MICROSOFT \n")
print("     -      EN "+str(cert_sh_2018)+" VULNERABILIDADES EL ASIGNADOR DE CVE INFO@CERT.VDE \n")
print("     -      EN "+str(trendmicro_sh_2018)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY@TRENDMICRO \n")
print("     -      EN "+str(nozomi_sh_2018)+" VULNERABILIDADES EL ASIGNADOR DE CVE PRODSEC@NOZOMINETWORKS \n")
print("     -      EN "+str(hq_sh_2018)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES ICS-CERT@HQ.DHS.GOV \n")
print("     -      EN "+str(kaspersky_sh_2018)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES VULNERABILITY@KASPERSKY \n")
print("     -      EN "+str(schneider_sh_2018)+" VULNERABILIDADES EL ASIGNADOR DE CVE CYBERSECURITY@SCHNEIDER-ELECTRIC \n")
print("     -      EN "+str(apple_sh_2018)+" VULNERABILIDADES EL ASIGNADOR DE CVE PRODUCT-SECURITY@APPLE \n")
print("     -      EN "+str(android_sh_2018)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY@ANDROID \n")
print("     -      EN "+str(bitdefender_sh_2018)+" VULNERABILIDADES EL ASIGNADOR DE CVE CVE-REQUESTS@BITDEFENDER \n")
print("     -      EN "+str(mcafee_sh_2018)+" VULNERABILIDADES EL ASIGNADOR DE CVE PSIRT@MCAFEE \n")
print("     -      EN "+str(mozilla_sh_2018)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY@MOZILLA \n")
print("     -      EN "+str(hpe_sh_2018)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY-ALERT@HPE \n")
print("     -      EN "+str(fsecure_sh_2018)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES CVE-NOTIFICATIONS-US@F-SECURE.COM \n")
print("     -      EN "+str(rapid7_sh_2018)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES CVE@RAPID7 \n")
print("     -      EN "+str(other_assigner_sh_2018)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES DISTINTO DE LOS ANTERIORES \n")
print("\n")


print("************************** ESTADÍSTICAS ASIGNADOR CVE SEGÚN FECHA DE PUBLICACIÓN PARTE SMART HOME********************************")
print("\n")
print("\n")
print(" DE UN TOTAL DE "+str(total_assigner_sh)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ESTÁ DEFINIDO, LAS ESTADÍSTICAS DE ASSIGNER SEGUN FECHA DE PUBLICACION SON LAS SIGUIENTES  : \n")
print("\n")
print("  -  EN  "+str(jpcert_sh)+" VULNERABILIDADES DONDE EL ASIGNADOR ES VULTURES@JPCERT, LAS ESTADÍSTICAS SEGUN FECHA DE PUBLICACION SON LAS SIGUIENTES : \n")
print("     -      UN TOTAL DE "+str(jpcert_sh_2023)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES VULTURES@JPCERT, FUERON PUBLICADAS EN 2023 \n")
print("     -      UN TOTAL DE "+str(jpcert_sh_2022)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES VULTURES@JPCERT, FUERON PUBLICADAS EN 2022 \n")
print("     -      UN TOTAL DE "+str(jpcert_sh_2021)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES VULTURES@JPCERT, FUERON PUBLICADAS EN 2021 \n")
print("     -      UN TOTAL DE "+str(jpcert_sh_2020)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES VULTURES@JPCERT, FUERON PUBLICADAS EN 2020 \n")
print("     -      UN TOTAL DE "+str(jpcert_sh_2019)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES VULTURES@JPCERT, FUERON PUBLICADAS EN 2019 \n")
print("     -      UN TOTAL DE "+str(jpcert_sh_2018)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES VULTURES@JPCERT, FUERON PUBLICADAS EN 2018 O ANTERIORMENTE \n")
print("\n")
print("  -  EN  "+str(mitre_sh)+" VULNERABILIDADES DONDE EL ASIGNADOR ES CVE@MITRE, LAS ESTADÍSTICAS SEGUN FECHA DE PUBLICACION SON LAS SIGUIENTES : \n")
print("     -      UN TOTAL DE "+str(mitre_sh_2023)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES CVE@MITRE, FUERON PUBLICADAS EN 2023 \n")
print("     -      UN TOTAL DE "+str(mitre_sh_2022)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES CVE@MITRE, FUERON PUBLICADAS EN 2022 \n")
print("     -      UN TOTAL DE "+str(mitre_sh_2021)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES CVE@MITRE, FUERON PUBLICADAS EN 2021 \n")
print("     -      UN TOTAL DE "+str(mitre_sh_2020)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES CVE@MITRE, FUERON PUBLICADAS EN 2020 \n")
print("     -      UN TOTAL DE "+str(mitre_sh_2019)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES CVE@MITRE, FUERON PUBLICADAS EN 2019 \n")
print("     -      UN TOTAL DE "+str(mitre_sh_2018)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES CVE@MITRE, FUERON PUBLICADAS EN 2018 O ANTERIORMENTE \n")
print("\n")
print("  -  EN  "+str(cisco_sh)+" VULNERABILIDADES DONDE EL ASIGNADOR ES TALOS-CNA@CISCO, LAS ESTADÍSTICAS SEGUN FECHA DE PUBLICACION SON LAS SIGUIENTES : \n")
print("     -      UN TOTAL DE "+str(cisco_sh_2023)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES TALOS-CNA@CISCO, FUERON PUBLICADAS EN 2023 \n")
print("     -      UN TOTAL DE "+str(cisco_sh_2022)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES TALOS-CNA@CISCO, FUERON PUBLICADAS EN 2022 \n")
print("     -      UN TOTAL DE "+str(cisco_sh_2021)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES TALOS-CNA@CISCO, FUERON PUBLICADAS EN 2021 \n")
print("     -      UN TOTAL DE "+str(cisco_sh_2020)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES TALOS-CNA@CISCO, FUERON PUBLICADAS EN 2020 \n")
print("     -      UN TOTAL DE "+str(cisco_sh_2019)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES TALOS-CNA@CISCO, FUERON PUBLICADAS EN 2019 \n")
print("     -      UN TOTAL DE "+str(cisco_sh_2018)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES TALOS-CNA@CISCO, FUERON PUBLICADAS EN 2018 O ANTERIORMENTE \n")
print("\n")
print("  -  EN  "+str(github_sh)+" VULNERABILIDADES DONDE EL ASIGNADOR ES SECURITY-ADVISORIES@GITHUB, LAS ESTADÍSTICAS SEGUN FECHA DE PUBLICACION SON LAS SIGUIENTES : \n")
print("     -      UN TOTAL DE "+str(github_sh_2023)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY-ADVISORIES@GITHUB, FUERON PUBLICADAS EN 2023 \n")
print("     -      UN TOTAL DE "+str(github_sh_2022)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY-ADVISORIES@GITHUB, FUERON PUBLICADAS EN 2022 \n")
print("     -      UN TOTAL DE "+str(github_sh_2021)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY-ADVISORIES@GITHUB, FUERON PUBLICADAS EN 2021 \n")
print("     -      UN TOTAL DE "+str(github_sh_2020)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY-ADVISORIES@GITHUB, FUERON PUBLICADAS EN 2020 \n")
print("     -      UN TOTAL DE "+str(github_sh_2019)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY-ADVISORIES@GITHUB, FUERON PUBLICADAS EN 2019 \n")
print("     -      UN TOTAL DE "+str(github_sh_2018)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY-ADVISORIES@GITHUB, FUERON PUBLICADAS EN 2018 O ANTERIORMENTE \n")
print("\n")
print("  -  EN  "+str(redhat_sh)+" VULNERABILIDADES DONDE EL ASIGNADOR ES SECALERT@REDHAT, LAS ESTADÍSTICAS SEGUN FECHA DE PUBLICACION SON LAS SIGUIENTES : \n")
print("     -      UN TOTAL DE "+str(redhat_sh_2023)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECALERT@REDHAT, FUERON PUBLICADAS EN 2023 \n")
print("     -      UN TOTAL DE "+str(redhat_sh_2022)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECALERT@REDHAT, FUERON PUBLICADAS EN 2022 \n")
print("     -      UN TOTAL DE "+str(redhat_sh_2021)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECALERT@REDHAT, FUERON PUBLICADAS EN 2021 \n")
print("     -      UN TOTAL DE "+str(redhat_sh_2020)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECALERT@REDHAT, FUERON PUBLICADAS EN 2020 \n")
print("     -      UN TOTAL DE "+str(redhat_sh_2019)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECALERT@REDHAT, FUERON PUBLICADAS EN 2019 \n")
print("     -      UN TOTAL DE "+str(redhat_sh_2018)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECALERT@REDHAT, FUERON PUBLICADAS EN 2018 O ANTERIORMENTE \n")
print("\n")
print("  -  EN  "+str(qualcomm_sh)+" VULNERABILIDADES DONDE EL ASIGNADOR ES SECURITY.CNA@QUALCOMM, LAS ESTADÍSTICAS SEGUN FECHA DE PUBLICACION SON LAS SIGUIENTES : \n")
print("     -      UN TOTAL DE "+str(qualcomm_sh_2023)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY.CNA@QUALCOMM, FUERON PUBLICADAS EN 2023 \n")
print("     -      UN TOTAL DE "+str(qualcomm_sh_2022)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY.CNA@QUALCOMM, FUERON PUBLICADAS EN 2022 \n")
print("     -      UN TOTAL DE "+str(qualcomm_sh_2021)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY.CNA@QUALCOMM, FUERON PUBLICADAS EN 2021 \n")
print("     -      UN TOTAL DE "+str(qualcomm_sh_2020)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY.CNA@QUALCOMM, FUERON PUBLICADAS EN 2020 \n")
print("     -      UN TOTAL DE "+str(qualcomm_sh_2019)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY.CNA@QUALCOMM, FUERON PUBLICADAS EN 2019 \n")
print("     -      UN TOTAL DE "+str(qualcomm_sh_2018)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY.CNA@QUALCOMM, FUERON PUBLICADAS EN 2018 O ANTERIORMENTE \n")
print("\n")
print("  -  EN  "+str(apache_sh)+" VULNERABILIDADES DONDE EL ASIGNADOR ES SECURITY@APACHE.ORG, LAS ESTADÍSTICAS SEGUN FECHA DE PUBLICACION SON LAS SIGUIENTES : \n")
print("     -      UN TOTAL DE "+str(apache_sh_2023)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY@APACHE.ORG, FUERON PUBLICADAS EN 2023 \n")
print("     -      UN TOTAL DE "+str(apache_sh_2022)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY@APACHE.ORG, FUERON PUBLICADAS EN 2022 \n")
print("     -      UN TOTAL DE "+str(apache_sh_2021)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY@APACHE.ORG, FUERON PUBLICADAS EN 2021 \n")
print("     -      UN TOTAL DE "+str(apache_sh_2020)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY@APACHE.ORG, FUERON PUBLICADAS EN 2020 \n")
print("     -      UN TOTAL DE "+str(apache_sh_2019)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY@APACHE.ORG, FUERON PUBLICADAS EN 2019 \n")
print("     -      UN TOTAL DE "+str(apache_sh_2018)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY@APACHE.ORG, FUERON PUBLICADAS EN 2018 O ANTERIORMENTE \n")
print("\n")
print("  -  EN  "+str(oracle_sh)+" VULNERABILIDADES DONDE EL ASIGNADOR ES SECALERT_US@ORACLE, LAS ESTADÍSTICAS SEGUN FECHA DE PUBLICACION SON LAS SIGUIENTES : \n")
print("     -      UN TOTAL DE "+str(oracle_sh_2023)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECALERT_US@ORACLE, FUERON PUBLICADAS EN 2023 \n")
print("     -      UN TOTAL DE "+str(oracle_sh_2022)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECALERT_US@ORACLE, FUERON PUBLICADAS EN 2022 \n")
print("     -      UN TOTAL DE "+str(oracle_sh_2021)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECALERT_US@ORACLE, FUERON PUBLICADAS EN 2021 \n")
print("     -      UN TOTAL DE "+str(oracle_sh_2020)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECALERT_US@ORACLE, FUERON PUBLICADAS EN 2020 \n")
print("     -      UN TOTAL DE "+str(oracle_sh_2019)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECALERT_US@ORACLE, FUERON PUBLICADAS EN 2019 \n")
print("     -      UN TOTAL DE "+str(oracle_sh_2018)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECALERT_US@ORACLE, FUERON PUBLICADAS EN 2018 O ANTERIORMENTE \n")
print("\n")
print("  -  EN  "+str(microsoft_sh)+" VULNERABILIDADES DONDE EL ASIGNADOR ES SECURE@MICROSOFT, LAS ESTADÍSTICAS SEGUN FECHA DE PUBLICACION SON LAS SIGUIENTES : \n")
print("     -      UN TOTAL DE "+str(microsoft_sh_2023)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURE@MICROSOFT, FUERON PUBLICADAS EN 2023 \n")
print("     -      UN TOTAL DE "+str(microsoft_sh_2022)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURE@MICROSOFT, FUERON PUBLICADAS EN 2022 \n")
print("     -      UN TOTAL DE "+str(microsoft_sh_2021)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURE@MICROSOFT, FUERON PUBLICADAS EN 2021 \n")
print("     -      UN TOTAL DE "+str(microsoft_sh_2020)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURE@MICROSOFT, FUERON PUBLICADAS EN 2020 \n")
print("     -      UN TOTAL DE "+str(microsoft_sh_2019)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURE@MICROSOFT, FUERON PUBLICADAS EN 2019 \n")
print("     -      UN TOTAL DE "+str(microsoft_sh_2018)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURE@MICROSOFT, FUERON PUBLICADAS EN 2018 O ANTERIORMENTE \n")
print("\n")
print("  -  EN  "+str(cert_sh)+" VULNERABILIDADES DONDE EL ASIGNADOR ES INFO@CERT.VDE, LAS ESTADÍSTICAS SEGUN FECHA DE PUBLICACION SON LAS SIGUIENTES : \n")
print("     -      UN TOTAL DE "+str(cert_sh_2023)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES INFO@CERT.VDE, FUERON PUBLICADAS EN 2023 \n")
print("     -      UN TOTAL DE "+str(cert_sh_2022)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES INFO@CERT.VDE, FUERON PUBLICADAS EN 2022 \n")
print("     -      UN TOTAL DE "+str(cert_sh_2021)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES INFO@CERT.VDE, FUERON PUBLICADAS EN 2021 \n")
print("     -      UN TOTAL DE "+str(cert_sh_2020)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES INFO@CERT.VDE, FUERON PUBLICADAS EN 2020 \n")
print("     -      UN TOTAL DE "+str(cert_sh_2019)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES INFO@CERT.VDE, FUERON PUBLICADAS EN 2019 \n")
print("     -      UN TOTAL DE "+str(cert_sh_2018)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES INFO@CERT.VDE, FUERON PUBLICADAS EN 2018 O ANTERIORMENTE \n")
print("\n")
print("  -  EN  "+str(trendmicro_sh)+" VULNERABILIDADES DONDE EL ASIGNADOR ES SECURITY@TRENDMICRO, LAS ESTADÍSTICAS SEGUN FECHA DE PUBLICACION SON LAS SIGUIENTES : \n")
print("     -      UN TOTAL DE "+str(trendmicro_sh_2023)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY@TRENDMICRO, FUERON PUBLICADAS EN 2023 \n")
print("     -      UN TOTAL DE "+str(trendmicro_sh_2022)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY@TRENDMICRO, FUERON PUBLICADAS EN 2022 \n")
print("     -      UN TOTAL DE "+str(trendmicro_sh_2021)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY@TRENDMICRO, FUERON PUBLICADAS EN 2021 \n")
print("     -      UN TOTAL DE "+str(trendmicro_sh_2020)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY@TRENDMICRO, FUERON PUBLICADAS EN 2020 \n")
print("     -      UN TOTAL DE "+str(trendmicro_sh_2019)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY@TRENDMICRO, FUERON PUBLICADAS EN 2019 \n")
print("     -      UN TOTAL DE "+str(trendmicro_sh_2018)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY@TRENDMICRO, FUERON PUBLICADAS EN 2018 O ANTERIORMENTE \n")
print("\n")
print("  -  EN  "+str(nozomi_sh)+" VULNERABILIDADES DONDE EL ASIGNADOR ES PRODSEC@NOZOMINETWORKS, LAS ESTADÍSTICAS SEGUN FECHA DE PUBLICACION SON LAS SIGUIENTES : \n")
print("     -      UN TOTAL DE "+str(nozomi_sh_2023)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES PRODSEC@NOZOMINETWORKS, FUERON PUBLICADAS EN 2023 \n")
print("     -      UN TOTAL DE "+str(nozomi_sh_2022)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES PRODSEC@NOZOMINETWORKS, FUERON PUBLICADAS EN 2022 \n")
print("     -      UN TOTAL DE "+str(nozomi_sh_2021)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES PRODSEC@NOZOMINETWORKS, FUERON PUBLICADAS EN 2021 \n")
print("     -      UN TOTAL DE "+str(nozomi_sh_2020)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES PRODSEC@NOZOMINETWORKS, FUERON PUBLICADAS EN 2020 \n")
print("     -      UN TOTAL DE "+str(nozomi_sh_2019)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES PRODSEC@NOZOMINETWORKS, FUERON PUBLICADAS EN 2019 \n")
print("     -      UN TOTAL DE "+str(nozomi_sh_2018)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES PRODSEC@NOZOMINETWORKS, FUERON PUBLICADAS EN 2018 O ANTERIORMENTE \n")
print("\n")
print("  -  EN  "+str(hq_sh)+" VULNERABILIDADES DONDE EL ASIGNADOR ES ICS-CERT@HQ.DHS.GOV, LAS ESTADÍSTICAS SEGUN FECHA DE PUBLICACION SON LAS SIGUIENTES : \n")
print("     -      UN TOTAL DE "+str(hq_sh_2023)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES ICS-CERT@HQ.DHS.GOV, FUERON PUBLICADAS EN 2023 \n")
print("     -      UN TOTAL DE "+str(hq_sh_2022)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES ICS-CERT@HQ.DHS.GOV, FUERON PUBLICADAS EN 2022 \n")
print("     -      UN TOTAL DE "+str(hq_sh_2021)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES ICS-CERT@HQ.DHS.GOV, FUERON PUBLICADAS EN 2021 \n")
print("     -      UN TOTAL DE "+str(hq_sh_2020)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES ICS-CERT@HQ.DHS.GOV, FUERON PUBLICADAS EN 2020 \n")
print("     -      UN TOTAL DE "+str(hq_sh_2019)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES ICS-CERT@HQ.DHS.GOV, FUERON PUBLICADAS EN 2019 \n")
print("     -      UN TOTAL DE "+str(hq_sh_2018)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES ICS-CERT@HQ.DHS.GOV, FUERON PUBLICADAS EN 2018 O ANTERIORMENTE \n")
print("\n")
print("  -  EN  "+str(kaspersky_sh)+" VULNERABILIDADES DONDE EL ASIGNADOR ES VULNERABILITY@KASPERSKY, LAS ESTADÍSTICAS SEGUN FECHA DE PUBLICACION SON LAS SIGUIENTES : \n")
print("     -      UN TOTAL DE "+str(kaspersky_sh_2023)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES VULNERABILITY@KASPERSKY, FUERON PUBLICADAS EN 2023 \n")
print("     -      UN TOTAL DE "+str(kaspersky_sh_2022)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES VULNERABILITY@KASPERSKY, FUERON PUBLICADAS EN 2022 \n")
print("     -      UN TOTAL DE "+str(kaspersky_sh_2021)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES VULNERABILITY@KASPERSKY, FUERON PUBLICADAS EN 2021 \n")
print("     -      UN TOTAL DE "+str(kaspersky_sh_2020)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES VULNERABILITY@KASPERSKY, FUERON PUBLICADAS EN 2020 \n")
print("     -      UN TOTAL DE "+str(kaspersky_sh_2019)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES VULNERABILITY@KASPERSKY, FUERON PUBLICADAS EN 2019 \n")
print("     -      UN TOTAL DE "+str(kaspersky_sh_2018)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES VULNERABILITY@KASPERSKY, FUERON PUBLICADAS EN 2018 O ANTERIORMENTE \n")
print("\n")
print("  -  EN  "+str(schneider_sh)+" VULNERABILIDADES DONDE EL ASIGNADOR ES CYBERSECURITY@SCHNEIDER-ELECTRIC, LAS ESTADÍSTICAS SEGUN FECHA DE PUBLICACION SON LAS SIGUIENTES : \n")
print("     -      UN TOTAL DE "+str(schneider_sh_2023)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES CYBERSECURITY@SCHNEIDER-ELECTRIC, FUERON PUBLICADAS EN 2023 \n")
print("     -      UN TOTAL DE "+str(schneider_sh_2022)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES CYBERSECURITY@SCHNEIDER-ELECTRIC, FUERON PUBLICADAS EN 2022 \n")
print("     -      UN TOTAL DE "+str(schneider_sh_2021)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES CYBERSECURITY@SCHNEIDER-ELECTRIC, FUERON PUBLICADAS EN 2021 \n")
print("     -      UN TOTAL DE "+str(schneider_sh_2020)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES CYBERSECURITY@SCHNEIDER-ELECTRIC, FUERON PUBLICADAS EN 2020 \n")
print("     -      UN TOTAL DE "+str(schneider_sh_2019)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES CYBERSECURITY@SCHNEIDER-ELECTRIC, FUERON PUBLICADAS EN 2019 \n")
print("     -      UN TOTAL DE "+str(schneider_sh_2018)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES CYBERSECURITY@SCHNEIDER-ELECTRIC, FUERON PUBLICADAS EN 2018 O ANTERIORMENTE \n")
print("\n")
print("  -  EN  "+str(apple_sh)+" VULNERABILIDADES DONDE EL ASIGNADOR ES PRODUCT-SECURITY@APPLE, LAS ESTADÍSTICAS SEGUN FECHA DE PUBLICACION SON LAS SIGUIENTES : \n")
print("     -      UN TOTAL DE "+str(apple_sh_2023)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES PRODUCT-SECURITY@APPLE, FUERON PUBLICADAS EN 2023 \n")
print("     -      UN TOTAL DE "+str(apple_sh_2022)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES PRODUCT-SECURITY@APPLE, FUERON PUBLICADAS EN 2022 \n")
print("     -      UN TOTAL DE "+str(apple_sh_2021)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES PRODUCT-SECURITY@APPLE, FUERON PUBLICADAS EN 2021 \n")
print("     -      UN TOTAL DE "+str(apple_sh_2020)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES PRODUCT-SECURITY@APPLE, FUERON PUBLICADAS EN 2020 \n")
print("     -      UN TOTAL DE "+str(apple_sh_2019)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES PRODUCT-SECURITY@APPLE, FUERON PUBLICADAS EN 2019 \n")
print("     -      UN TOTAL DE "+str(apple_sh_2018)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES PRODUCT-SECURITY@APPLE, FUERON PUBLICADAS EN 2018 O ANTERIORMENTE \n")
print("\n")
print("  -  EN  "+str(android_sh)+" VULNERABILIDADES DONDE EL ASIGNADOR ES SECURITY@ANDROID, LAS ESTADÍSTICAS SEGUN FECHA DE PUBLICACION SON LAS SIGUIENTES : \n")
print("     -      UN TOTAL DE "+str(android_sh_2023)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY@ANDROID, FUERON PUBLICADAS EN 2023 \n")
print("     -      UN TOTAL DE "+str(android_sh_2022)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY@ANDROID, FUERON PUBLICADAS EN 2022 \n")
print("     -      UN TOTAL DE "+str(android_sh_2021)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY@ANDROID, FUERON PUBLICADAS EN 2021 \n")
print("     -      UN TOTAL DE "+str(android_sh_2020)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY@ANDROID, FUERON PUBLICADAS EN 2020 \n")
print("     -      UN TOTAL DE "+str(android_sh_2019)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY@ANDROID, FUERON PUBLICADAS EN 2019 \n")
print("     -      UN TOTAL DE "+str(android_sh_2018)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY@ANDROID, FUERON PUBLICADAS EN 2018 O ANTERIORMENTE \n")
print("\n")
print("  -  EN  "+str(bitdefender_sh)+" VULNERABILIDADES DONDE EL ASIGNADOR ES CVE-REQUESTS@BITDEFENDER, LAS ESTADÍSTICAS SEGUN FECHA DE PUBLICACION SON LAS SIGUIENTES : \n")
print("     -      UN TOTAL DE "+str(bitdefender_sh_2023)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES CVE-REQUESTS@BITDEFENDER, FUERON PUBLICADAS EN 2023 \n")
print("     -      UN TOTAL DE "+str(bitdefender_sh_2022)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES CVE-REQUESTS@BITDEFENDER, FUERON PUBLICADAS EN 2022 \n")
print("     -      UN TOTAL DE "+str(bitdefender_sh_2021)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES CVE-REQUESTS@BITDEFENDER, FUERON PUBLICADAS EN 2021 \n")
print("     -      UN TOTAL DE "+str(bitdefender_sh_2020)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES CVE-REQUESTS@BITDEFENDER, FUERON PUBLICADAS EN 2020 \n")
print("     -      UN TOTAL DE "+str(bitdefender_sh_2019)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES CVE-REQUESTS@BITDEFENDER, FUERON PUBLICADAS EN 2019 \n")
print("     -      UN TOTAL DE "+str(bitdefender_sh_2018)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES CVE-REQUESTS@BITDEFENDER, FUERON PUBLICADAS EN 2018 O ANTERIORMENTE \n")
print("\n")
print("  -  EN  "+str(mcafee_sh)+" VULNERABILIDADES DONDE EL ASIGNADOR ES PSIRT@MCAFEE, LAS ESTADÍSTICAS SEGUN FECHA DE PUBLICACION SON LAS SIGUIENTES : \n")
print("     -      UN TOTAL DE "+str(mcafee_sh_2023)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES PSIRT@MCAFEE, FUERON PUBLICADAS EN 2023 \n")
print("     -      UN TOTAL DE "+str(mcafee_sh_2022)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES PSIRT@MCAFEE, FUERON PUBLICADAS EN 2022 \n")
print("     -      UN TOTAL DE "+str(mcafee_sh_2021)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES PSIRT@MCAFEE, FUERON PUBLICADAS EN 2021 \n")
print("     -      UN TOTAL DE "+str(mcafee_sh_2020)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES PSIRT@MCAFEE, FUERON PUBLICADAS EN 2020 \n")
print("     -      UN TOTAL DE "+str(mcafee_sh_2019)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES PSIRT@MCAFEE, FUERON PUBLICADAS EN 2019 \n")
print("     -      UN TOTAL DE "+str(mcafee_sh_2018)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES PSIRT@MCAFEE, FUERON PUBLICADAS EN 2018 O ANTERIORMENTE \n")
print("\n")
print("  -  EN  "+str(mozilla_sh)+" VULNERABILIDADES DONDE EL ASIGNADOR ES SECURITY@MOZILLA, LAS ESTADÍSTICAS SEGUN FECHA DE PUBLICACION SON LAS SIGUIENTES : \n")
print("     -      UN TOTAL DE "+str(mozilla_sh_2023)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY@MOZILLA, FUERON PUBLICADAS EN 2023 \n")
print("     -      UN TOTAL DE "+str(mozilla_sh_2022)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY@MOZILLA, FUERON PUBLICADAS EN 2022 \n")
print("     -      UN TOTAL DE "+str(mozilla_sh_2021)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY@MOZILLA, FUERON PUBLICADAS EN 2021 \n")
print("     -      UN TOTAL DE "+str(mozilla_sh_2020)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY@MOZILLA, FUERON PUBLICADAS EN 2020 \n")
print("     -      UN TOTAL DE "+str(mozilla_sh_2019)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY@MOZILLA, FUERON PUBLICADAS EN 2019 \n")
print("     -      UN TOTAL DE "+str(mozilla_sh_2018)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY@MOZILLA, FUERON PUBLICADAS EN 2018 O ANTERIORMENTE \n")
print("\n")
print("  -  EN  "+str(hpe_sh)+" VULNERABILIDADES DONDE EL ASIGNADOR ES SECURITY-ALERT@HPE, LAS ESTADÍSTICAS SEGUN FECHA DE PUBLICACION SON LAS SIGUIENTES : \n")
print("     -      UN TOTAL DE "+str(hpe_sh_2023)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY-ADVISORIES@HPE, FUERON PUBLICADAS EN 2023 \n")
print("     -      UN TOTAL DE "+str(hpe_sh_2022)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY-ADVISORIES@HPE, FUERON PUBLICADAS EN 2022 \n")
print("     -      UN TOTAL DE "+str(hpe_sh_2021)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY-ADVISORIES@HPE, FUERON PUBLICADAS EN 2021 \n")
print("     -      UN TOTAL DE "+str(hpe_sh_2020)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY-ADVISORIES@HPE, FUERON PUBLICADAS EN 2020 \n")
print("     -      UN TOTAL DE "+str(hpe_sh_2019)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY-ADVISORIES@HPE, FUERON PUBLICADAS EN 2019 \n")
print("     -      UN TOTAL DE "+str(hpe_sh_2018)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY-ADVISORIES@HPE, FUERON PUBLICADAS EN 2018 O ANTERIORMENTE \n")
print("\n")
print("  -  EN  "+str(rapid7_sh)+" VULNERABILIDADES DONDE EL ASIGNADOR ES CVE@RAPID7, LAS ESTADÍSTICAS SEGUN FECHA DE PUBLICACION SON LAS SIGUIENTES : \n")
print("     -      UN TOTAL DE "+str(rapid7_sh_2023)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES CVE@RAPID7, FUERON PUBLICADAS EN 2023 \n")
print("     -      UN TOTAL DE "+str(rapid7_sh_2022)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES CVE@RAPID7, FUERON PUBLICADAS EN 2022 \n")
print("     -      UN TOTAL DE "+str(rapid7_sh_2021)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES CVE@RAPID7, FUERON PUBLICADAS EN 2021 \n")
print("     -      UN TOTAL DE "+str(rapid7_sh_2020)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES CVE@RAPID7, FUERON PUBLICADAS EN 2020 \n")
print("     -      UN TOTAL DE "+str(rapid7_sh_2019)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES CVE@RAPID7, FUERON PUBLICADAS EN 2019 \n")
print("     -      UN TOTAL DE "+str(rapid7_sh_2018)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES CVE@RAPID7, FUERON PUBLICADAS EN 2018 O ANTERIORMENTE \n")
print("\n")
print("  -  EN  "+str(fsecure_sh)+" VULNERABILIDADES DONDE EL ASIGNADOR ES CVE-NOTIFICATIONS-US@F-SECURE, LAS ESTADÍSTICAS SEGUN FECHA DE PUBLICACION SON LAS SIGUIENTES : \n")
print("     -      UN TOTAL DE "+str(fsecure_sh_2023)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES CVE-NOTIFICATIONS-US@F-SECURE, FUERON PUBLICADAS EN 2023 \n")
print("     -      UN TOTAL DE "+str(fsecure_sh_2022)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES CVE-NOTIFICATIONS-US@F-SECURE, FUERON PUBLICADAS EN 2022 \n")
print("     -      UN TOTAL DE "+str(fsecure_sh_2021)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES CVE-NOTIFICATIONS-US@F-SECURE, FUERON PUBLICADAS EN 2021 \n")
print("     -      UN TOTAL DE "+str(fsecure_sh_2020)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES CVE-NOTIFICATIONS-US@F-SECURE, FUERON PUBLICADAS EN 2020 \n")
print("     -      UN TOTAL DE "+str(fsecure_sh_2019)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES CVE-NOTIFICATIONS-US@F-SECURE, FUERON PUBLICADAS EN 2019 \n")
print("     -      UN TOTAL DE "+str(fsecure_sh_2018)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES CVE-NOTIFICATIONS-US@F-SECURE, FUERON PUBLICADAS EN 2018 O ANTERIORMENTE \n")
print("\n")
print("  -  EN  "+str(other_assigner_sh)+" VULNERABILIDADES DONDE EL ASIGNADOR ES OTRO DISTINTO A  LOS ANTERIORES, LAS ESTADÍSTICAS SEGUN FECHA DE PUBLICACION SON LAS SIGUIENTES : \n")
print("     -      UN TOTAL DE "+str(other_assigner_sh_2023)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES OTRO DISTINTO A LOS ANTERIORES, FUERON PUBLICADAS EN 2023 \n")
print("     -      UN TOTAL DE "+str(other_assigner_sh_2022)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES OTRO DISTINTO A LOS ANTERIORES, FUERON PUBLICADAS EN 2022 \n")
print("     -      UN TOTAL DE "+str(other_assigner_sh_2021)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES OTRO DISTINTO A LOS ANTERIORES, FUERON PUBLICADAS EN 2021 \n")
print("     -      UN TOTAL DE "+str(other_assigner_sh_2020)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES OTRO DISTINTO A LOS ANTERIORES, FUERON PUBLICADAS EN 2020 \n")
print("     -      UN TOTAL DE "+str(other_assigner_sh_2019)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES OTRO DISTINTO A LOS ANTERIORES, FUERON PUBLICADAS EN 2019 \n")
print("     -      UN TOTAL DE "+str(other_assigner_sh_2018)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES OTRO DISTINTO A LOS ANTERIORES, FUERON PUBLICADAS EN 2018 O ANTERIORMENTE \n")
print("\n")





print("************************** PORCENTAJE FECHA DE PUBLICACION Y CVE ASIGNADOR CVE PARTE SMART HOME********************************")
print("\n")
print("\n")
print(" -  DE UN TOTAL DE "+str(total_assigner_sh)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ESTÁ DEFINIDO, LOS PORCENTAJES DE ASSIGNER Y FECHA DE PUBLICACION SON LOS SIGUIENTES  : \n")
print("\n")
print("EN EL "+str(float(((assigner_sh_2023*100)/(assigner_sh_2023+assigner_sh_2022+assigner_sh_2021+assigner_sh_2020+assigner_sh_2019+assigner_sh_2018))))+" % DE LAS VULNERABILIDADES PUBLICADAS EN EL 2023, LOS PORCENTAJES DE ASIGNADORES CVE SON LOS SIGUIENTES : \n")
print("     -      EN EL "+str(float(((jpcert_sh_2023*100)/(assigner_sh_2023))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES VULTURES@JPCERT\n")
print("     -      EN EL "+str(float(((mitre_sh_2023*100)/(assigner_sh_2023))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES CVE@MITRE \n")
print("     -      EN EL "+str(float(((cisco_sh_2023*100)/(assigner_sh_2023))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES TALOS-CNA@CISCO \n")
print("     -      EN EL "+str(float(((github_sh_2023*100)/(assigner_sh_2023))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY-ADVISORIES@GITHUB \n")
print("     -      EN EL "+str(float(((redhat_sh_2023*100)/(assigner_sh_2023))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES SECALERT@REDHAT\n")
print("     -      EN EL "+str(float(((qualcomm_sh_2023*100)/(assigner_sh_2023))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY.CNA@QUALCOMM \n")
print("     -      EN EL "+str(float(((apache_sh_2023*100)/(assigner_sh_2023))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY@APACHE.ORG \n")
print("     -      EN EL "+str(float(((oracle_sh_2023*100)/(assigner_sh_2023))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES SECALERT_US@ORACLE \n")
print("     -      EN EL "+str(float(((microsoft_sh_2023*100)/(assigner_sh_2023))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURE@MICROSOFT \n")
print("     -      EN EL "+str(float(((cert_sh_2023*100)/(assigner_sh_2023))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE INFO@CERT.VDE \n")
print("     -      EN EL "+str(float(((trendmicro_sh_2023*100)/(assigner_sh_2023))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY@TRENDMICRO \n")
print("     -      EN EL "+str(float(((nozomi_sh_2023*100)/(assigner_sh_2023))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE PRODSEC@NOZOMINETWORKS \n")
print("     -      EN EL "+str(float(((hq_sh_2023*100)/(assigner_sh_2023))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES ICS-CERT@HQ.DHS.GOV \n")
print("     -      EN EL "+str(float(((kaspersky_sh_2023*100)/(assigner_sh_2023))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES VULNERABILITY@KASPERSKY \n")
print("     -      EN EL "+str(float(((schneider_sh_2023*100)/(assigner_sh_2023))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE CYBERSECURITY@SCHNEIDER-ELECTRIC \n")
print("     -      EN EL "+str(float(((apple_sh_2023*100)/(assigner_sh_2023))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE PRODUCT-SECURITY@APPLE \n")
print("     -      EN EL "+str(float(((android_sh_2023*100)/(assigner_sh_2023))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY@ANDROID \n")
print("     -      EN EL "+str(float(((bitdefender_sh_2023*100)/(assigner_sh_2023))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE CVE-REQUESTS@BITDEFENDER \n")
print("     -      EN EL "+str(float(((mcafee_sh_2023*100)/(assigner_sh_2023))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE PSIRT@MCAFEE \n")
print("     -      EN EL "+str(float(((mozilla_sh_2023*100)/(assigner_sh_2023))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY@MOZILLA \n")
print("     -      EN EL "+str(float(((hpe_sh_2023*100)/(assigner_sh_2023))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY-ALERT@HPE \n")
print("     -      EN EL "+str(float(((fsecure_sh_2023*100)/(assigner_sh_2023))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES CVE-NOTIFICATIONS-US@F-SECURE \n")
print("     -      EN EL "+str(float(((rapid7_sh_2023*100)/(assigner_sh_2023))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES CVE@RAPID7 \n")
print("     -      EN EL "+str(float(((other_assigner_sh_2023*100)/(assigner_sh_2023))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES DISTINTO A LOS ANTERIORES \n")
print("\n")

print("EN EL "+str(float(((assigner_sh_2022*100)/(assigner_sh_2023+assigner_sh_2022+assigner_sh_2021+assigner_sh_2020+assigner_sh_2019+assigner_sh_2018))))+" % DE LAS VULNERABILIDADES PUBLICADAS EN EL 2022, LOS PORCENTAJES DE ASIGNADORES CVE SON LOS SIGUIENTES : \n")
print("     -      EN EL "+str(float(((jpcert_sh_2022*100)/(assigner_sh_2022))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES VULTURES@JPCERT\n")
print("     -      EN EL "+str(float(((mitre_sh_2022*100)/(assigner_sh_2022))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES CVE@MITRE \n")
print("     -      EN EL "+str(float(((cisco_sh_2022*100)/(assigner_sh_2022))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES TALOS-CNA@CISCO \n")
print("     -      EN EL "+str(float(((github_sh_2022*100)/(assigner_sh_2022))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY-ADVISORIES@GITHUB \n")
print("     -      EN EL "+str(float(((redhat_sh_2022*100)/(assigner_sh_2022))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES SECALERT@REDHAT\n")
print("     -      EN EL "+str(float(((qualcomm_sh_2022*100)/(assigner_sh_2022))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY.CNA@QUALCOMM \n")
print("     -      EN EL "+str(float(((apache_sh_2022*100)/(assigner_sh_2022))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY@APACHE.ORG \n")
print("     -      EN EL "+str(float(((oracle_sh_2022*100)/(assigner_sh_2022))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES SECALERT_US@ORACLE \n")
print("     -      EN EL "+str(float(((microsoft_sh_2022*100)/(assigner_sh_2022))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURE@MICROSOFT \n")
print("     -      EN EL "+str(float(((cert_sh_2022*100)/(assigner_sh_2022))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE INFO@CERT.VDE \n")
print("     -      EN EL "+str(float(((trendmicro_sh_2022*100)/(assigner_sh_2022))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY@TRENDMICRO \n")
print("     -      EN EL "+str(float(((nozomi_sh_2022*100)/(assigner_sh_2022))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE PRODSEC@NOZOMINETWORKS \n")
print("     -      EN EL "+str(float(((hq_sh_2022*100)/(assigner_sh_2022))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES ICS-CERT@HQ.DHS.GOV \n")
print("     -      EN EL "+str(float(((kaspersky_sh_2022*100)/(assigner_sh_2022))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES VULNERABILITY@KASPERSKY \n")
print("     -      EN EL "+str(float(((schneider_sh_2022*100)/(assigner_sh_2022))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE CYBERSECURITY@SCHNEIDER-ELECTRIC \n")
print("     -      EN EL "+str(float(((apple_sh_2022*100)/(assigner_sh_2022))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE PRODUCT-SECURITY@APPLE \n")
print("     -      EN EL "+str(float(((android_sh_2022*100)/(assigner_sh_2022))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY@ANDROID \n")
print("     -      EN EL "+str(float(((bitdefender_sh_2022*100)/(assigner_sh_2022))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE CVE-REQUESTS@BITDEFENDER \n")
print("     -      EN EL "+str(float(((mcafee_sh_2022*100)/(assigner_sh_2022))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE PSIRT@MCAFEE \n")
print("     -      EN EL "+str(float(((mozilla_sh_2022*100)/(assigner_sh_2022))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY@MOZILLA \n")
print("     -      EN EL "+str(float(((hpe_sh_2022*100)/(assigner_sh_2022))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY-ALERT@HPE \n")
print("     -      EN EL "+str(float(((fsecure_sh_2022*100)/(assigner_sh_2022))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES CVE-NOTIFICATIONS-US@F-SECURE \n")
print("     -      EN EL "+str(float(((rapid7_sh_2022*100)/(assigner_sh_2022))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES CVE@RAPID7 \n")
print("     -      EN EL "+str(float(((other_assigner_sh_2022*100)/(assigner_sh_2022))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES DISTINTO A LOS ANTERIORES \n")
print("\n")

print("EN EL "+str(float(((assigner_sh_2021*100)/(assigner_sh_2023+assigner_sh_2022+assigner_sh_2021+assigner_sh_2020+assigner_sh_2019+assigner_sh_2018))))+" % DE LAS VULNERABILIDADES PUBLICADAS EN EL 2021, LOS PORCENTAJES DE ASIGNADORES CVE SON LOS SIGUIENTES : \n")
print("     -      EN EL "+str(float(((jpcert_sh_2021*100)/(assigner_sh_2021))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES VULTURES@JPCERT\n")
print("     -      EN EL "+str(float(((mitre_sh_2021*100)/(assigner_sh_2021))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES CVE@MITRE \n")
print("     -      EN EL "+str(float(((cisco_sh_2021*100)/(assigner_sh_2021))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES TALOS-CNA@CISCO \n")
print("     -      EN EL "+str(float(((github_sh_2021*100)/(assigner_sh_2021))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY-ADVISORIES@GITHUB \n")
print("     -      EN EL "+str(float(((redhat_sh_2021*100)/(assigner_sh_2021))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES SECALERT@REDHAT\n")
print("     -      EN EL "+str(float(((qualcomm_sh_2021*100)/(assigner_sh_2021))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY.CNA@QUALCOMM \n")
print("     -      EN EL "+str(float(((apache_sh_2021*100)/(assigner_sh_2021))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY@APACHE.ORG \n")
print("     -      EN EL "+str(float(((oracle_sh_2021*100)/(assigner_sh_2021))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES SECALERT_US@ORACLE \n")
print("     -      EN EL "+str(float(((microsoft_sh_2021*100)/(assigner_sh_2021))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURE@MICROSOFT \n")
print("     -      EN EL "+str(float(((cert_sh_2021*100)/(assigner_sh_2021))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE INFO@CERT.VDE \n")
print("     -      EN EL "+str(float(((trendmicro_sh_2021*100)/(assigner_sh_2021))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY@TRENDMICRO \n")
print("     -      EN EL "+str(float(((nozomi_sh_2021*100)/(assigner_sh_2021))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE PRODSEC@NOZOMINETWORKS \n")
print("     -      EN EL "+str(float(((hq_sh_2021*100)/(assigner_sh_2021))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES ICS-CERT@HQ.DHS.GOV \n")
print("     -      EN EL "+str(float(((kaspersky_sh_2021*100)/(assigner_sh_2021))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES VULNERABILITY@KASPERSKY \n")
print("     -      EN EL "+str(float(((schneider_sh_2021*100)/(assigner_sh_2021))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE CYBERSECURITY@SCHNEIDER-ELECTRIC \n")
print("     -      EN EL "+str(float(((apple_sh_2021*100)/(assigner_sh_2021))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE PRODUCT-SECURITY@APPLE \n")
print("     -      EN EL "+str(float(((android_sh_2021*100)/(assigner_sh_2021))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY@ANDROID \n")
print("     -      EN EL "+str(float(((bitdefender_sh_2021*100)/(assigner_sh_2021))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE CVE-REQUESTS@BITDEFENDER \n")
print("     -      EN EL "+str(float(((mcafee_sh_2021*100)/(assigner_sh_2021))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE PSIRT@MCAFEE \n")
print("     -      EN EL "+str(float(((mozilla_sh_2021*100)/(assigner_sh_2021))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY@MOZILLA \n")
print("     -      EN EL "+str(float(((hpe_sh_2021*100)/(assigner_sh_2021))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY-ALERT@HPE \n")
print("     -      EN EL "+str(float(((fsecure_sh_2021*100)/(assigner_sh_2021))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES CVE-NOTIFICATIONS-US@F-SECURE \n")
print("     -      EN EL "+str(float(((rapid7_sh_2021*100)/(assigner_sh_2021))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES CVE@RAPID7 \n")
print("     -      EN EL "+str(float(((other_assigner_sh_2021*100)/(assigner_sh_2021))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES DISTINTO A LOS ANTERIORES \n")
print("\n")

print("EN EL "+str(float(((assigner_sh_2020*100)/(assigner_sh_2023+assigner_sh_2022+assigner_sh_2021+assigner_sh_2020+assigner_sh_2019+assigner_sh_2018))))+" % DE LAS VULNERABILIDADES PUBLICADAS EN EL 2020, LOS PORCENTAJES DE ASIGNADORES CVE SON LOS SIGUIENTES : \n")
print("     -      EN EL "+str(float(((jpcert_sh_2020*100)/(assigner_sh_2020))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES VULTURES@JPCERT\n")
print("     -      EN EL "+str(float(((mitre_sh_2020*100)/(assigner_sh_2020))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES CVE@MITRE \n")
print("     -      EN EL "+str(float(((cisco_sh_2020*100)/(assigner_sh_2020))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES TALOS-CNA@CISCO \n")
print("     -      EN EL "+str(float(((github_sh_2020*100)/(assigner_sh_2020))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY-ADVISORIES@GITHUB \n")
print("     -      EN EL "+str(float(((redhat_sh_2020*100)/(assigner_sh_2020))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES SECALERT@REDHAT\n")
print("     -      EN EL "+str(float(((qualcomm_sh_2020*100)/(assigner_sh_2020))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY.CNA@QUALCOMM \n")
print("     -      EN EL "+str(float(((apache_sh_2020*100)/(assigner_sh_2020))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY@APACHE.ORG \n")
print("     -      EN EL "+str(float(((oracle_sh_2020*100)/(assigner_sh_2020))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES SECALERT_US@ORACLE \n")
print("     -      EN EL "+str(float(((microsoft_sh_2020*100)/(assigner_sh_2020))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURE@MICROSOFT \n")
print("     -      EN EL "+str(float(((cert_sh_2020*100)/(assigner_sh_2020))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE INFO@CERT.VDE \n")
print("     -      EN EL "+str(float(((trendmicro_sh_2020*100)/(assigner_sh_2020))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY@TRENDMICRO \n")
print("     -      EN EL "+str(float(((nozomi_sh_2020*100)/(assigner_sh_2020))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE PRODSEC@NOZOMINETWORKS \n")
print("     -      EN EL "+str(float(((hq_sh_2020*100)/(assigner_sh_2020))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES ICS-CERT@HQ.DHS.GOV \n")
print("     -      EN EL "+str(float(((kaspersky_sh_2020*100)/(assigner_sh_2020))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES VULNERABILITY@KASPERSKY \n")
print("     -      EN EL "+str(float(((schneider_sh_2020*100)/(assigner_sh_2020))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE CYBERSECURITY@SCHNEIDER-ELECTRIC \n")
print("     -      EN EL "+str(float(((apple_sh_2020*100)/(assigner_sh_2020))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE PRODUCT-SECURITY@APPLE \n")
print("     -      EN EL "+str(float(((android_sh_2020*100)/(assigner_sh_2020))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY@ANDROID \n")
print("     -      EN EL "+str(float(((bitdefender_sh_2020*100)/(assigner_sh_2020))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE CVE-REQUESTS@BITDEFENDER \n")
print("     -      EN EL "+str(float(((mcafee_sh_2020*100)/(assigner_sh_2020))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE PSIRT@MCAFEE \n")
print("     -      EN EL "+str(float(((mozilla_sh_2020*100)/(assigner_sh_2020))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY@MOZILLA \n")
print("     -      EN EL "+str(float(((hpe_sh_2020*100)/(assigner_sh_2020))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY-ALERT@HPE \n")
print("     -      EN EL "+str(float(((fsecure_sh_2020*100)/(assigner_sh_2020))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES CVE-NOTIFICATIONS-US@F-SECURE \n")
print("     -      EN EL "+str(float(((rapid7_sh_2020*100)/(assigner_sh_2020))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES CVE@RAPID7 \n")
print("     -      EN EL "+str(float(((other_assigner_sh_2020*100)/(assigner_sh_2020))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES DISTINTO A LOS ANTERIORES \n")
print("\n")

print("EN EL "+str(float(((assigner_sh_2019*100)/(assigner_sh_2023+assigner_sh_2022+assigner_sh_2021+assigner_sh_2020+assigner_sh_2019+assigner_sh_2018))))+" % DE LAS VULNERABILIDADES PUBLICADAS EN EL 2019, LOS PORCENTAJES DE ASIGNADORES CVE SON LOS SIGUIENTES : \n")
print("     -      EN EL "+str(float(((jpcert_sh_2019*100)/(assigner_sh_2019))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES VULTURES@JPCERT\n")
print("     -      EN EL "+str(float(((mitre_sh_2019*100)/(assigner_sh_2019))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES CVE@MITRE \n")
print("     -      EN EL "+str(float(((cisco_sh_2019*100)/(assigner_sh_2019))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES TALOS-CNA@CISCO \n")
print("     -      EN EL "+str(float(((github_sh_2019*100)/(assigner_sh_2019))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY-ADVISORIES@GITHUB \n")
print("     -      EN EL "+str(float(((redhat_sh_2019*100)/(assigner_sh_2019))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES SECALERT@REDHAT\n")
print("     -      EN EL "+str(float(((qualcomm_sh_2019*100)/(assigner_sh_2019))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY.CNA@QUALCOMM \n")
print("     -      EN EL "+str(float(((apache_sh_2019*100)/(assigner_sh_2019))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY@APACHE.ORG \n")
print("     -      EN EL "+str(float(((oracle_sh_2019*100)/(assigner_sh_2019))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES SECALERT_US@ORACLE \n")
print("     -      EN EL "+str(float(((microsoft_sh_2019*100)/(assigner_sh_2019))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURE@MICROSOFT \n")
print("     -      EN EL "+str(float(((cert_sh_2019*100)/(assigner_sh_2019))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE INFO@CERT.VDE \n")
print("     -      EN EL "+str(float(((trendmicro_sh_2019*100)/(assigner_sh_2019))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY@TRENDMICRO \n")
print("     -      EN EL "+str(float(((nozomi_sh_2019*100)/(assigner_sh_2019))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE PRODSEC@NOZOMINETWORKS \n")
print("     -      EN EL "+str(float(((hq_sh_2019*100)/(assigner_sh_2019))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES ICS-CERT@HQ.DHS.GOV \n")
print("     -      EN EL "+str(float(((kaspersky_sh_2019*100)/(assigner_sh_2019))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES VULNERABILITY@KASPERSKY \n")
print("     -      EN EL "+str(float(((schneider_sh_2019*100)/(assigner_sh_2019))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE CYBERSECURITY@SCHNEIDER-ELECTRIC \n")
print("     -      EN EL "+str(float(((apple_sh_2019*100)/(assigner_sh_2019))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE PRODUCT-SECURITY@APPLE \n")
print("     -      EN EL "+str(float(((android_sh_2019*100)/(assigner_sh_2019))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY@ANDROID \n")
print("     -      EN EL "+str(float(((bitdefender_sh_2019*100)/(assigner_sh_2019))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE CVE-REQUESTS@BITDEFENDER \n")
print("     -      EN EL "+str(float(((mcafee_sh_2019*100)/(assigner_sh_2019))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE PSIRT@MCAFEE \n")
print("     -      EN EL "+str(float(((mozilla_sh_2019*100)/(assigner_sh_2019))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY@MOZILLA \n")
print("     -      EN EL "+str(float(((hpe_sh_2019*100)/(assigner_sh_2019))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY-ALERT@HPE \n")
print("     -      EN EL "+str(float(((fsecure_sh_2019*100)/(assigner_sh_2019))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES CVE-NOTIFICATIONS-US@F-SECURE \n")
print("     -      EN EL "+str(float(((rapid7_sh_2019*100)/(assigner_sh_2019))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES CVE@RAPID7 \n")
print("     -      EN EL "+str(float(((other_assigner_sh_2019*100)/(assigner_sh_2019))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES DISTINTO A LOS ANTERIORES \n")
print("\n")

print("EN EL "+str(float(((assigner_sh_2018*100)/(assigner_sh_2023+assigner_sh_2022+assigner_sh_2021+assigner_sh_2020+assigner_sh_2019+assigner_sh_2018))))+" % DE LAS VULNERABILIDADES PUBLICADAS EN EL 2018 O ANTERIORMENTE, LOS PORCENTAJES DE ASIGNADORES CVE SON LOS SIGUIENTES : \n")
print("     -      EN EL "+str(float(((jpcert_sh_2018*100)/(assigner_sh_2018))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES VULTURES@JPCERT\n")
print("     -      EN EL "+str(float(((mitre_sh_2018*100)/(assigner_sh_2018))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES CVE@MITRE \n")
print("     -      EN EL "+str(float(((cisco_sh_2018*100)/(assigner_sh_2018))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES TALOS-CNA@CISCO \n")
print("     -      EN EL "+str(float(((github_sh_2018*100)/(assigner_sh_2018))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY-ADVISORIES@GITHUB \n")
print("     -      EN EL "+str(float(((redhat_sh_2018*100)/(assigner_sh_2018))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES SECALERT@REDHAT\n")
print("     -      EN EL "+str(float(((qualcomm_sh_2018*100)/(assigner_sh_2018))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY.CNA@QUALCOMM \n")
print("     -      EN EL "+str(float(((apache_sh_2018*100)/(assigner_sh_2018))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY@APACHE.ORG \n")
print("     -      EN EL "+str(float(((oracle_sh_2018*100)/(assigner_sh_2018))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES SECALERT_US@ORACLE \n")
print("     -      EN EL "+str(float(((microsoft_sh_2018*100)/(assigner_sh_2018))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURE@MICROSOFT \n")
print("     -      EN EL "+str(float(((cert_sh_2018*100)/(assigner_sh_2018))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE INFO@CERT.VDE \n")
print("     -      EN EL "+str(float(((trendmicro_sh_2018*100)/(assigner_sh_2018))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY@TRENDMICRO \n")
print("     -      EN EL "+str(float(((nozomi_sh_2018*100)/(assigner_sh_2018))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE PRODSEC@NOZOMINETWORKS \n")
print("     -      EN EL "+str(float(((hq_sh_2018*100)/(assigner_sh_2018))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES ICS-CERT@HQ.DHS.GOV \n")
print("     -      EN EL "+str(float(((kaspersky_sh_2018*100)/(assigner_sh_2018))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES VULNERABILITY@KASPERSKY \n")
print("     -      EN EL "+str(float(((schneider_sh_2018*100)/(assigner_sh_2018))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE CYBERSECURITY@SCHNEIDER-ELECTRIC \n")
print("     -      EN EL "+str(float(((apple_sh_2018*100)/(assigner_sh_2018))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE PRODUCT-SECURITY@APPLE \n")
print("     -      EN EL "+str(float(((android_sh_2018*100)/(assigner_sh_2018))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY@ANDROID \n")
print("     -      EN EL "+str(float(((bitdefender_sh_2018*100)/(assigner_sh_2018))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE CVE-REQUESTS@BITDEFENDER \n")
print("     -      EN EL "+str(float(((mcafee_sh_2018*100)/(assigner_sh_2018))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE PSIRT@MCAFEE \n")
print("     -      EN EL "+str(float(((mozilla_sh_2018*100)/(assigner_sh_2018))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY@MOZILLA \n")
print("     -      EN EL "+str(float(((hpe_sh_2018*100)/(assigner_sh_2018))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY-ALERT@HPE \n")
print("     -      EN EL "+str(float(((fsecure_sh_2018*100)/(assigner_sh_2018))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES CVE-NOTIFICATIONS-US@F-SECURE \n")
print("     -      EN EL "+str(float(((rapid7_sh_2018*100)/(assigner_sh_2018))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES CVE@RAPID7 \n")
print("     -      EN EL "+str(float(((other_assigner_sh_2018*100)/(assigner_sh_2018))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES DISTINTO A LOS ANTERIORES \n")
print("\n")





print("************************** PORCENTAJE ASIGNADOR CVE SEGÚN FECHA DE PUBLICACIÓN PARTE SMART HOME********************************")
print("\n")
print("\n")
print(" -  DE UN TOTAL DE "+str(total_assigner_sh)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ESTÁ DEFINIDO, LOS PORCENTAJES DE ASSIGNER SEGUN FECHA DE PUBLICACION SON LOS SIGUIENTES  : \n")
print("\n")
print("EN EL "+str(float(((jpcert_sh*100)/total_assigner_sh)))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR ES VULTURES@JPCERT, LOS PORCENTAJES SEGUN FECHA DE PUBLICACION SON LOS SIGUIENTES : \n")
print("     -      EL "+str(float(((jpcert_sh_2023*100)/(jpcert_sh))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES VULTURES@JPCERT, FUERON PUBLICADAS EN 2023 \n")
print("     -      EL "+str(float(((jpcert_sh_2022*100)/(jpcert_sh))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES VULTURES@JPCERT, FUERON PUBLICADAS EN 2022 \n")
print("     -      EL "+str(float(((jpcert_sh_2021*100)/(jpcert_sh))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES VULTURES@JPCERT, FUERON PUBLICADAS EN 2021 \n")
print("     -      EL "+str(float(((jpcert_sh_2020*100)/(jpcert_sh))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES VULTURES@JPCERT, FUERON PUBLICADAS EN 2020 \n")
print("     -      EL "+str(float(((jpcert_sh_2019*100)/(jpcert_sh))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES VULTURES@JPCERT, FUERON PUBLICADAS EN 2019 \n")
print("     -      EL "+str(float(((jpcert_sh_2018*100)/(jpcert_sh))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES VULTURES@JPCERT, FUERON PUBLICADAS EN 2018 O ANTERIORMENTE \n")
print("\n")
print("\n")
print("EN EL "+str(float(((mitre_sh*100)/total_assigner_sh)))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR ES CVE@MITRE, LOS PORCENTAJES SEGUN FECHA DE PUBLICACION SON LOS SIGUIENTES : \n")
print("     -      EL "+str(float(((mitre_sh_2023*100)/(mitre_sh))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES CVE@MITRE, FUERON PUBLICADAS EN 2023 \n")
print("     -      EL "+str(float(((mitre_sh_2022*100)/(mitre_sh))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES CVE@MITRE, FUERON PUBLICADAS EN 2022 \n")
print("     -      EL "+str(float(((mitre_sh_2021*100)/(mitre_sh))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES CVE@MITRE, FUERON PUBLICADAS EN 2021 \n")
print("     -      EL "+str(float(((mitre_sh_2020*100)/(mitre_sh))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES CVE@MITRE, FUERON PUBLICADAS EN 2020 \n")
print("     -      EL "+str(float(((mitre_sh_2019*100)/(mitre_sh))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES CVE@MITRE, FUERON PUBLICADAS EN 2019 \n")
print("     -      EL "+str(float(((mitre_sh_2018*100)/(mitre_sh))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES CVE@MITRE, FUERON PUBLICADAS EN 2018 O ANTERIORMENTE \n")
print("\n")
print("\n")
print("EN EL "+str(float(((cisco_sh*100)/total_assigner_sh)))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR ES TALOS-CNA@CISCO, LOS PORCENTAJES SEGUN FECHA DE PUBLICACION SON LOS SIGUIENTES : \n")
print("     -      EL "+str(float(((cisco_sh_2023*100)/(cisco_sh))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES TALOS-CNA@CISCO, FUERON PUBLICADAS EN 2023 \n")
print("     -      EL "+str(float(((cisco_sh_2022*100)/(cisco_sh))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES TALOS-CNA@CISCO, FUERON PUBLICADAS EN 2022 \n")
print("     -      EL "+str(float(((cisco_sh_2021*100)/(cisco_sh))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES TALOS-CNA@CISCO, FUERON PUBLICADAS EN 2021 \n")
print("     -      EL "+str(float(((cisco_sh_2020*100)/(cisco_sh))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES TALOS-CNA@CISCO, FUERON PUBLICADAS EN 2020 \n")
print("     -      EL "+str(float(((cisco_sh_2019*100)/(cisco_sh))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES TALOS-CNA@CISCO, FUERON PUBLICADAS EN 2019 \n")
print("     -      EL "+str(float(((cisco_sh_2018*100)/(cisco_sh))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES TALOS-CNA@CISCO, FUERON PUBLICADAS EN 2018 O ANTERIORMENTE \n")
print("\n")
print("\n")
print("EN EL "+str(float(((github_sh*100)/total_assigner_sh)))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR ES SECURITY-ADVISORIES@GITHUB, LOS PORCENTAJES SEGUN FECHA DE PUBLICACION SON LOS SIGUIENTES : \n")
print("     -      EL "+str(float(((github_sh_2023*100)/(github_sh))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY-ADVISORIES@GITHUB, FUERON PUBLICADAS EN 2023 \n")
print("     -      EL "+str(float(((github_sh_2022*100)/(github_sh))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY-ADVISORIES@GITHUB, FUERON PUBLICADAS EN 2022 \n")
print("     -      EL "+str(float(((github_sh_2021*100)/(github_sh))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY-ADVISORIES@GITHUB, FUERON PUBLICADAS EN 2021 \n")
print("     -      EL "+str(float(((github_sh_2020*100)/(github_sh))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY-ADVISORIES@GITHUB, FUERON PUBLICADAS EN 2020 \n")
print("     -      EL "+str(float(((github_sh_2019*100)/(github_sh))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY-ADVISORIES@GITHUB, FUERON PUBLICADAS EN 2019 \n")
print("     -      EL "+str(float(((github_sh_2018*100)/(github_sh))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY-ADVISORIES@GITHUB, FUERON PUBLICADAS EN 2018 O ANTERIORMENTE \n")
print("\n")
print("\n")
if(redhat_sh>0):
    print("EN EL "+str(float(((redhat_sh*100)/total_assigner_sh)))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR ES SECALERT@REDHAT, LOS PORCENTAJES SEGUN FECHA DE PUBLICACION SON LOS SIGUIENTES : \n")
    print("     -      EL "+str(float(((redhat_sh_2023*100)/(redhat_sh))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECALERT@REDHAT, FUERON PUBLICADAS EN 2023 \n")
    print("     -      EL "+str(float(((redhat_sh_2022*100)/(redhat_sh))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECALERT@REDHAT, FUERON PUBLICADAS EN 2022 \n")
    print("     -      EL "+str(float(((redhat_sh_2021*100)/(redhat_sh))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECALERT@REDHAT, FUERON PUBLICADAS EN 2021 \n")
    print("     -      EL "+str(float(((redhat_sh_2020*100)/(redhat_sh))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECALERT@REDHAT, FUERON PUBLICADAS EN 2020 \n")
    print("     -      EL "+str(float(((redhat_sh_2019*100)/(redhat_sh))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECALERT@REDHAT, FUERON PUBLICADAS EN 2019 \n")
    print("     -      EL "+str(float(((redhat_sh_2018*100)/(redhat_sh))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECALERT@REDHAT, FUERON PUBLICADAS EN 2018 O ANTERIORMENTE \n")
    print("\n")
    print("\n")
if(qualcomm_sh>0):
    print("EN EL "+str(float(((qualcomm_sh*100)/total_assigner_sh)))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR ES SECURITY.CNA@QUALCOMM, LOS PORCENTAJES SEGUN FECHA DE PUBLICACION SON LOS SIGUIENTES : \n")
    print("     -      EL "+str(float(((qualcomm_sh_2023*100)/(qualcomm_sh))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY.CNA@QUALCOMM, FUERON PUBLICADAS EN 2023 \n")
    print("     -      EL "+str(float(((qualcomm_sh_2022*100)/(qualcomm_sh))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY.CNA@QUALCOMM, FUERON PUBLICADAS EN 2022 \n")
    print("     -      EL "+str(float(((qualcomm_sh_2021*100)/(qualcomm_sh))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY.CNA@QUALCOMM, FUERON PUBLICADAS EN 2021 \n")
    print("     -      EL "+str(float(((qualcomm_sh_2020*100)/(qualcomm_sh))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY.CNA@QUALCOMM, FUERON PUBLICADAS EN 2020 \n")
    print("     -      EL "+str(float(((qualcomm_sh_2019*100)/(qualcomm_sh))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY.CNA@QUALCOMM, FUERON PUBLICADAS EN 2019 \n")
    print("     -      EL "+str(float(((qualcomm_sh_2018*100)/(qualcomm_sh))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY.CNA@QUALCOMM, FUERON PUBLICADAS EN 2018 O ANTERIORMENTE \n")
    print("\n")
    print("\n")
if(apache_sh>0):
    print("EN EL "+str(float(((apache_sh*100)/total_assigner_sh)))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR ES SECURITY@APACHE.ORG, LOS PORCENTAJES SEGUN FECHA DE PUBLICACION SON LOS SIGUIENTES : \n")
    print("     -      EL "+str(float(((apache_sh_2023*100)/(apache_sh))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY@APACHE.ORG, FUERON PUBLICADAS EN 2023 \n")
    print("     -      EL "+str(float(((apache_sh_2022*100)/(apache_sh))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY@APACHE.ORG, FUERON PUBLICADAS EN 2022 \n")
    print("     -      EL "+str(float(((apache_sh_2021*100)/(apache_sh))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY@APACHE.ORG, FUERON PUBLICADAS EN 2021 \n")
    print("     -      EL "+str(float(((apache_sh_2020*100)/(apache_sh))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY@APACHE.ORG, FUERON PUBLICADAS EN 2020 \n")
    print("     -      EL "+str(float(((apache_sh_2019*100)/(apache_sh))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY@APACHE.ORG, FUERON PUBLICADAS EN 2019 \n")
    print("     -      EL "+str(float(((apache_sh_2018*100)/(apache_sh))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY@APACHE.ORG, FUERON PUBLICADAS EN 2018 O ANTERIORMENTE \n")
    print("\n")
    print("\n")
if(oracle_sh>0):
    print("EN EL "+str(float(((oracle_sh*100)/total_assigner_sh)))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR ES SECALERT_US@ORACLE, LOS PORCENTAJES SEGUN FECHA DE PUBLICACION SON LOS SIGUIENTES : \n")
    print("     -      EL "+str(float(((oracle_sh_2023*100)/(oracle_sh))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECALERT_US@ORACLE, FUERON PUBLICADAS EN 2023 \n")
    print("     -      EL "+str(float(((oracle_sh_2022*100)/(oracle_sh))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECALERT_US@ORACLE, FUERON PUBLICADAS EN 2022 \n")
    print("     -      EL "+str(float(((oracle_sh_2021*100)/(oracle_sh))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECALERT_US@ORACLE, FUERON PUBLICADAS EN 2021 \n")
    print("     -      EL "+str(float(((oracle_sh_2020*100)/(oracle_sh))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECALERT_US@ORACLE, FUERON PUBLICADAS EN 2020 \n")
    print("     -      EL "+str(float(((oracle_sh_2019*100)/(oracle_sh))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECALERT_US@ORACLE, FUERON PUBLICADAS EN 2019 \n")
    print("     -      EL "+str(float(((oracle_sh_2018*100)/(oracle_sh))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECALERT_US@ORACLE, FUERON PUBLICADAS EN 2018 O ANTERIORMENTE \n")
    print("\n")
    print("\n")
if(microsoft_sh>0):
    print("EN EL "+str(float(((microsoft_sh*100)/total_assigner_sh)))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR ES SECURE@MICROSOFT, LOS PORCENTAJES SEGUN FECHA DE PUBLICACION SON LOS SIGUIENTES : \n")
    print("     -      EL "+str(float(((microsoft_sh_2023*100)/(microsoft_sh))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURE@MICROSOFT, FUERON PUBLICADAS EN 2023 \n")
    print("     -      EL "+str(float(((microsoft_sh_2022*100)/(microsoft_sh))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURE@MICROSOFT, FUERON PUBLICADAS EN 2022 \n")
    print("     -      EL "+str(float(((microsoft_sh_2021*100)/(microsoft_sh))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURE@MICROSOFT, FUERON PUBLICADAS EN 2021 \n")
    print("     -      EL "+str(float(((microsoft_sh_2020*100)/(microsoft_sh))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURE@MICROSOFT, FUERON PUBLICADAS EN 2020 \n")
    print("     -      EL "+str(float(((microsoft_sh_2019*100)/(microsoft_sh))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURE@MICROSOFT, FUERON PUBLICADAS EN 2019 \n")
    print("     -      EL "+str(float(((microsoft_sh_2018*100)/(microsoft_sh))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURE@MICROSOFT, FUERON PUBLICADAS EN 2018 O ANTERIORMENTE \n")
    print("\n")
    print("\n")
if(cert_sh>0):
    print("EN EL "+str(float(((cert_sh*100)/total_assigner_sh)))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR INFO@CERT.VDE, LOS PORCENTAJES SEGUN FECHA DE PUBLICACION SON LOS SIGUIENTES : \n")
    print("     -      EL "+str(float(((cert_sh_2023*100)/(cert_sh))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE INFO@CERT.VDE, FUERON PUBLICADAS EN 2023 \n")
    print("     -      EL "+str(float(((cert_sh_2022*100)/(cert_sh))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE INFO@CERT.VDE, FUERON PUBLICADAS EN 2022 \n")
    print("     -      EL "+str(float(((cert_sh_2021*100)/(cert_sh))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE INFO@CERT.VDE, FUERON PUBLICADAS EN 2021 \n")
    print("     -      EL "+str(float(((cert_sh_2020*100)/(cert_sh))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE INFO@CERT.VDE, FUERON PUBLICADAS EN 2020 \n")
    print("     -      EL "+str(float(((cert_sh_2019*100)/(cert_sh))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE INFO@CERT.VDE, FUERON PUBLICADAS EN 2019 \n")
    print("     -      EL "+str(float(((cert_sh_2018*100)/(cert_sh))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE INFO@CERT.VDE, FUERON PUBLICADAS EN 2018 O ANTERIORMENTE \n")
    print("\n")
    print("\n")
if(trendmicro_sh>0):
    print("EN EL "+str(float(((trendmicro_sh*100)/total_assigner_sh)))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR ES SECURITY@TRENDMICRO, LOS PORCENTAJES SEGUN FECHA DE PUBLICACION SON LOS SIGUIENTES : \n")
    print("     -      EL "+str(float(((trendmicro_sh_2023*100)/(trendmicro_sh))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY@TRENDMICRO, FUERON PUBLICADAS EN 2023 \n")
    print("     -      EL "+str(float(((trendmicro_sh_2022*100)/(trendmicro_sh))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY@TRENDMICRO, FUERON PUBLICADAS EN 2022 \n")
    print("     -      EL "+str(float(((trendmicro_sh_2021*100)/(trendmicro_sh))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY@TRENDMICRO, FUERON PUBLICADAS EN 2021 \n")
    print("     -      EL "+str(float(((trendmicro_sh_2020*100)/(trendmicro_sh))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY@TRENDMICRO, FUERON PUBLICADAS EN 2020 \n")
    print("     -      EL "+str(float(((trendmicro_sh_2019*100)/(trendmicro_sh))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY@TRENDMICRO, FUERON PUBLICADAS EN 2019 \n")
    print("     -      EL "+str(float(((trendmicro_sh_2018*100)/(trendmicro_sh))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY@TRENDMICRO, FUERON PUBLICADAS EN 2018 O ANTERIORMENTE \n")
    print("\n")
    print("\n")
if(nozomi_sh>0):
    print("EN EL "+str(float(((nozomi_sh*100)/total_assigner_sh)))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR PRODSEC@NOZOMINETWORKS, LOS PORCENTAJES SEGUN FECHA DE PUBLICACION SON LOS SIGUIENTES : \n")
    print("     -      EL "+str(float(((nozomi_sh_2023*100)/(nozomi_sh))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE PRODSEC@NOZOMINETWORKS, FUERON PUBLICADAS EN 2023 \n")
    print("     -      EL "+str(float(((nozomi_sh_2022*100)/(nozomi_sh))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE PRODSEC@NOZOMINETWORKS, FUERON PUBLICADAS EN 2022 \n")
    print("     -      EL "+str(float(((nozomi_sh_2021*100)/(nozomi_sh))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE PRODSEC@NOZOMINETWORKS, FUERON PUBLICADAS EN 2021 \n")
    print("     -      EL "+str(float(((nozomi_sh_2020*100)/(nozomi_sh))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE PRODSEC@NOZOMINETWORKS, FUERON PUBLICADAS EN 2020 \n")
    print("     -      EL "+str(float(((nozomi_sh_2019*100)/(nozomi_sh))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE PRODSEC@NOZOMINETWORKS, FUERON PUBLICADAS EN 2019 \n")
    print("     -      EL "+str(float(((nozomi_sh_2018*100)/(nozomi_sh))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE PRODSEC@NOZOMINETWORKS, FUERON PUBLICADAS EN 2018 O ANTERIORMENTE \n")
    print("\n")
    print("\n")
if(hq_sh>0):
    print("EN EL "+str(float(((hq_sh*100)/total_assigner_sh)))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR ES ICS-CERT@HQ.DHS.GOV, LOS PORCENTAJES SEGUN FECHA DE PUBLICACION SON LOS SIGUIENTES : \n")
    print("     -      EL "+str(float(((hq_sh_2023*100)/(hq_sh))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES ICS-CERT@HQ.DHS.GOV, FUERON PUBLICADAS EN 2023 \n")
    print("     -      EL "+str(float(((hq_sh_2022*100)/(hq_sh))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES ICS-CERT@HQ.DHS.GOV, FUERON PUBLICADAS EN 2022 \n")
    print("     -      EL "+str(float(((hq_sh_2021*100)/(hq_sh))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES ICS-CERT@HQ.DHS.GOV, FUERON PUBLICADAS EN 2021 \n")
    print("     -      EL "+str(float(((hq_sh_2020*100)/(hq_sh))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES ICS-CERT@HQ.DHS.GOV, FUERON PUBLICADAS EN 2020 \n")
    print("     -      EL "+str(float(((hq_sh_2019*100)/(hq_sh))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES ICS-CERT@HQ.DHS.GOV, FUERON PUBLICADAS EN 2019 \n")
    print("     -      EL "+str(float(((hq_sh_2018*100)/(hq_sh))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES ICS-CERT@HQ.DHS.GOV, FUERON PUBLICADAS EN 2018 O ANTERIORMENTE \n")
    print("\n")
    print("\n")
if(kaspersky_sh>0):
    print("EN EL "+str(float(((kaspersky_sh*100)/total_assigner_sh)))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR ES VULNERABILITY@KASPERSKY, LOS PORCENTAJES SEGUN FECHA DE PUBLICACION SON LOS SIGUIENTES : \n")
    print("     -      EL "+str(float(((kaspersky_sh_2023*100)/(kaspersky_sh))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES VULNERABILITY@KASPERSKY, FUERON PUBLICADAS EN 2023 \n")
    print("     -      EL "+str(float(((kaspersky_sh_2022*100)/(kaspersky_sh))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES VULNERABILITY@KASPERSKY, FUERON PUBLICADAS EN 2022 \n")
    print("     -      EL "+str(float(((kaspersky_sh_2021*100)/(kaspersky_sh))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES VULNERABILITY@KASPERSKY, FUERON PUBLICADAS EN 2021 \n")
    print("     -      EL "+str(float(((kaspersky_sh_2020*100)/(kaspersky_sh))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES VULNERABILITY@KASPERSKY, FUERON PUBLICADAS EN 2020 \n")
    print("     -      EL "+str(float(((kaspersky_sh_2019*100)/(kaspersky_sh))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES VULNERABILITY@KASPERSKY, FUERON PUBLICADAS EN 2019 \n")
    print("     -      EL "+str(float(((kaspersky_sh_2018*100)/(kaspersky_sh))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES VULNERABILITY@KASPERSKY, FUERON PUBLICADAS EN 2018 O ANTERIORMENTE \n")
    print("\n")
    print("\n")
if(schneider_sh>0):
    print("EN EL "+str(float(((schneider_sh*100)/total_assigner_sh)))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR CYBERSECURITY@SCHNEIDER-ELECTRIC, LOS PORCENTAJES SEGUN FECHA DE PUBLICACION SON LOS SIGUIENTES : \n")
    print("     -      EL "+str(float(((schneider_sh_2023*100)/(schneider_sh))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE CYBERSECURITY@SCHNEIDER-ELECTRIC, FUERON PUBLICADAS EN 2023 \n")
    print("     -      EL "+str(float(((schneider_sh_2022*100)/(schneider_sh))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE CYBERSECURITY@SCHNEIDER-ELECTRIC, FUERON PUBLICADAS EN 2022 \n")
    print("     -      EL "+str(float(((schneider_sh_2021*100)/(schneider_sh))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE CYBERSECURITY@SCHNEIDER-ELECTRIC, FUERON PUBLICADAS EN 2021 \n")
    print("     -      EL "+str(float(((schneider_sh_2020*100)/(schneider_sh))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE CYBERSECURITY@SCHNEIDER-ELECTRIC, FUERON PUBLICADAS EN 2020 \n")
    print("     -      EL "+str(float(((schneider_sh_2019*100)/(schneider_sh))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE CYBERSECURITY@SCHNEIDER-ELECTRIC, FUERON PUBLICADAS EN 2019 \n")
    print("     -      EL "+str(float(((schneider_sh_2018*100)/(schneider_sh))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE CYBERSECURITY@SCHNEIDER-ELECTRIC, FUERON PUBLICADAS EN 2018 O ANTERIORMENTE \n")
    print("\n")
    print("\n")
if(apple_sh>0):
    print("EN EL "+str(float(((apple_sh*100)/total_assigner_sh)))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR PRODUCT-SECURITY@APPLE, LOS PORCENTAJES SEGUN FECHA DE PUBLICACION SON LOS SIGUIENTES : \n")
    print("     -      EL "+str(float(((apple_sh_2023*100)/(apple_sh))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE PRODUCT-SECURITY@APPLE, FUERON PUBLICADAS EN 2023 \n")
    print("     -      EL "+str(float(((apple_sh_2022*100)/(apple_sh))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE PRODUCT-SECURITY@APPLE, FUERON PUBLICADAS EN 2022 \n")
    print("     -      EL "+str(float(((apple_sh_2021*100)/(apple_sh))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE PRODUCT-SECURITY@APPLE, FUERON PUBLICADAS EN 2021 \n")
    print("     -      EL "+str(float(((apple_sh_2020*100)/(apple_sh))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE PRODUCT-SECURITY@APPLE, FUERON PUBLICADAS EN 2020 \n")
    print("     -      EL "+str(float(((apple_sh_2019*100)/(apple_sh))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE PRODUCT-SECURITY@APPLE, FUERON PUBLICADAS EN 2019 \n")
    print("     -      EL "+str(float(((apple_sh_2018*100)/(apple_sh))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE PRODUCT-SECURITY@APPLE, FUERON PUBLICADAS EN 2018 O ANTERIORMENTE \n")
    print("\n")
    print("\n")
if(android_sh>0):
    print("EN EL "+str(float(((android_sh*100)/total_assigner_sh)))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR ES SECURITY@ANDROID, LOS PORCENTAJES SEGUN FECHA DE PUBLICACION SON LOS SIGUIENTES : \n")
    print("     -      EL "+str(float(((android_sh_2023*100)/(android_sh))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY@ANDROID, FUERON PUBLICADAS EN 2023 \n")
    print("     -      EL "+str(float(((android_sh_2022*100)/(android_sh))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY@ANDROID, FUERON PUBLICADAS EN 2022 \n")
    print("     -      EL "+str(float(((android_sh_2021*100)/(android_sh))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY@ANDROID, FUERON PUBLICADAS EN 2021 \n")
    print("     -      EL "+str(float(((android_sh_2020*100)/(android_sh))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY@ANDROID, FUERON PUBLICADAS EN 2020 \n")
    print("     -      EL "+str(float(((android_sh_2019*100)/(android_sh))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY@ANDROID, FUERON PUBLICADAS EN 2019 \n")
    print("     -      EL "+str(float(((android_sh_2018*100)/(android_sh))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY@ANDROID, FUERON PUBLICADAS EN 2018 O ANTERIORMENTE \n")
    print("\n")
    print("\n")
if(bitdefender_sh>0):
    print("EN EL "+str(float(((bitdefender_sh*100)/total_assigner_sh)))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR CVE-REQUESTS@BITDEFENDER, LOS PORCENTAJES SEGUN FECHA DE PUBLICACION SON LOS SIGUIENTES : \n")
    print("     -      EL "+str(float(((bitdefender_sh_2023*100)/(bitdefender_sh))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE CVE-REQUESTS@BITDEFENDER, FUERON PUBLICADAS EN 2023 \n")
    print("     -      EL "+str(float(((bitdefender_sh_2022*100)/(bitdefender_sh))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE CVE-REQUESTS@BITDEFENDER, FUERON PUBLICADAS EN 2022 \n")
    print("     -      EL "+str(float(((bitdefender_sh_2021*100)/(bitdefender_sh))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE CVE-REQUESTS@BITDEFENDER, FUERON PUBLICADAS EN 2021 \n")
    print("     -      EL "+str(float(((bitdefender_sh_2020*100)/(bitdefender_sh))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE CVE-REQUESTS@BITDEFENDER, FUERON PUBLICADAS EN 2020 \n")
    print("     -      EL "+str(float(((bitdefender_sh_2019*100)/(bitdefender_sh))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE CVE-REQUESTS@BITDEFENDER, FUERON PUBLICADAS EN 2019 \n")
    print("     -      EL "+str(float(((bitdefender_sh_2018*100)/(bitdefender_sh))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE CVE-REQUESTS@BITDEFENDER, FUERON PUBLICADAS EN 2018 O ANTERIORMENTE \n")
    print("\n")
    print("\n")
if(mcafee_sh>0):
    print("EN EL "+str(float(((mcafee_sh*100)/total_assigner_sh)))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR PSIRT@MCAFEE, LOS PORCENTAJES SEGUN FECHA DE PUBLICACION SON LOS SIGUIENTES : \n")
    print("     -      EL "+str(float(((mcafee_sh_2023*100)/(mcafee_sh))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE PSIRT@MCAFEE, FUERON PUBLICADAS EN 2023 \n")
    print("     -      EL "+str(float(((mcafee_sh_2022*100)/(mcafee_sh))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE PSIRT@MCAFEE, FUERON PUBLICADAS EN 2022 \n")
    print("     -      EL "+str(float(((mcafee_sh_2021*100)/(mcafee_sh))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE PSIRT@MCAFEE, FUERON PUBLICADAS EN 2021 \n")
    print("     -      EL "+str(float(((mcafee_sh_2020*100)/(mcafee_sh))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE PSIRT@MCAFEE, FUERON PUBLICADAS EN 2020 \n")
    print("     -      EL "+str(float(((mcafee_sh_2019*100)/(mcafee_sh))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE PSIRT@MCAFEE, FUERON PUBLICADAS EN 2019 \n")
    print("     -      EL "+str(float(((mcafee_sh_2018*100)/(mcafee_sh))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE PSIRT@MCAFEE, FUERON PUBLICADAS EN 2018 O ANTERIORMENTE \n")
    print("\n")
    print("\n")
if(mozilla_sh>0):
    print("EN EL "+str(float(((mozilla_sh*100)/total_assigner_sh)))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR ES SECURITY@MOZILLA, LOS PORCENTAJES SEGUN FECHA DE PUBLICACION SON LOS SIGUIENTES : \n")
    print("     -      EL "+str(float(((mozilla_sh_2023*100)/(mozilla_sh))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY@MOZILLA, FUERON PUBLICADAS EN 2023 \n")
    print("     -      EL "+str(float(((mozilla_sh_2022*100)/(mozilla_sh))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY@MOZILLA, FUERON PUBLICADAS EN 2022 \n")
    print("     -      EL "+str(float(((mozilla_sh_2021*100)/(mozilla_sh))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY@MOZILLA, FUERON PUBLICADAS EN 2021 \n")
    print("     -      EL "+str(float(((mozilla_sh_2020*100)/(mozilla_sh))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY@MOZILLA, FUERON PUBLICADAS EN 2020 \n")
    print("     -      EL "+str(float(((mozilla_sh_2019*100)/(mozilla_sh))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY@MOZILLA, FUERON PUBLICADAS EN 2019 \n")
    print("     -      EL "+str(float(((mozilla_sh_2018*100)/(mozilla_sh))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY@MOZILLA, FUERON PUBLICADAS EN 2018 O ANTERIORMENTE \n")
    print("\n")
    print("\n")
if(hpe_sh>0):
    print("EN EL "+str(float(((hpe_sh*100)/total_assigner_sh)))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR ES SECURITY-ALERT@HPE, LOS PORCENTAJES SEGUN FECHA DE PUBLICACION SON LOS SIGUIENTES : \n")
    print("     -      EL "+str(float(((hpe_sh_2023*100)/(hpe_sh))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY-ALERT@HPE, FUERON PUBLICADAS EN 2023 \n")
    print("     -      EL "+str(float(((hpe_sh_2022*100)/(hpe_sh))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY-ALERT@HPE, FUERON PUBLICADAS EN 2022 \n")
    print("     -      EL "+str(float(((hpe_sh_2021*100)/(hpe_sh))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY-ALERT@HPE, FUERON PUBLICADAS EN 2021 \n")
    print("     -      EL "+str(float(((hpe_sh_2020*100)/(hpe_sh))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY-ALERT@HPE, FUERON PUBLICADAS EN 2020 \n")
    print("     -      EL "+str(float(((hpe_sh_2019*100)/(hpe_sh))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY-ALERT@HPE, FUERON PUBLICADAS EN 2019 \n")
    print("     -      EL "+str(float(((hpe_sh_2018*100)/(hpe_sh))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY-ALERT@HPE, FUERON PUBLICADAS EN 2018 O ANTERIORMENTE \n")
    print("\n")
    print("\n")
if(rapid7_sh>0):
    print("EN EL "+str(float(((rapid7_sh*100)/total_assigner_sh)))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR ES CVE@RAPID7, LOS PORCENTAJES SEGUN FECHA DE PUBLICACION SON LOS SIGUIENTES : \n")
    print("     -      EL "+str(float(((rapid7_sh_2023*100)/(rapid7_sh))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES CVE@RAPID7, FUERON PUBLICADAS EN 2023 \n")
    print("     -      EL "+str(float(((rapid7_sh_2022*100)/(rapid7_sh))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES CVE@RAPID7, FUERON PUBLICADAS EN 2022 \n")
    print("     -      EL "+str(float(((rapid7_sh_2021*100)/(rapid7_sh))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES CVE@RAPID7, FUERON PUBLICADAS EN 2021 \n")
    print("     -      EL "+str(float(((rapid7_sh_2020*100)/(rapid7_sh))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES CVE@RAPID7, FUERON PUBLICADAS EN 2020 \n")
    print("     -      EL "+str(float(((rapid7_sh_2019*100)/(rapid7_sh))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES CVE@RAPID7, FUERON PUBLICADAS EN 2019 \n")
    print("     -      EL "+str(float(((rapid7_sh_2018*100)/(rapid7_sh))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES CVE@RAPID7, FUERON PUBLICADAS EN 2018 O ANTERIORMENTE \n")
    print("\n")
    print("\n")
if(fsecure_sh>0):
    print("EN EL "+str(float(((fsecure_sh*100)/total_assigner_sh)))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR ES CVE-NOTIFICATIONS-US@F-SECURE, LOS PORCENTAJES SEGUN FECHA DE PUBLICACION SON LOS SIGUIENTES : \n")
    print("     -      EL "+str(float(((fsecure_sh_2023*100)/(fsecure_sh))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES CVE-NOTIFICATIONS-US@F-SECURE, FUERON PUBLICADAS EN 2023 \n")
    print("     -      EL "+str(float(((fsecure_sh_2022*100)/(fsecure_sh))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES CVE-NOTIFICATIONS-US@F-SECURE, FUERON PUBLICADAS EN 2022 \n")
    print("     -      EL "+str(float(((fsecure_sh_2021*100)/(fsecure_sh))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES CVE-NOTIFICATIONS-US@F-SECURE, FUERON PUBLICADAS EN 2021 \n")
    print("     -      EL "+str(float(((fsecure_sh_2020*100)/(fsecure_sh))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES CVE-NOTIFICATIONS-US@F-SECURE, FUERON PUBLICADAS EN 2020 \n")
    print("     -      EL "+str(float(((fsecure_sh_2019*100)/(fsecure_sh))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES CVE-NOTIFICATIONS-US@F-SECURE, FUERON PUBLICADAS EN 2019 \n")
    print("     -      EL "+str(float(((fsecure_sh_2018*100)/(fsecure_sh))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES CVE-NOTIFICATIONS-US@F-SECURE, FUERON PUBLICADAS EN 2018 O ANTERIORMENTE \n")
    print("\n")
    print("\n")
if(other_assigner_sh>0):
    print("EN EL "+str(float(((other_assigner_sh*100)/total_assigner_sh)))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR OTRO DISTINTO A LOS ANTERIORES, LOS PORCENTAJES SEGUN FECHA DE PUBLICACION SON LOS SIGUIENTES : \n")
    print("     -      EL "+str(float(((other_assigner_sh_2023*100)/(other_assigner_sh))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE OTRO DISTINTO A LOS ANTERIORES, FUERON PUBLICADAS EN 2023 \n")
    print("     -      EL "+str(float(((other_assigner_sh_2022*100)/(other_assigner_sh))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE OTRO DISTINTO A LOS ANTERIORES, FUERON PUBLICADAS EN 2022 \n")
    print("     -      EL "+str(float(((other_assigner_sh_2021*100)/(other_assigner_sh))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE OTRO DISTINTO A LOS ANTERIORES, FUERON PUBLICADAS EN 2021 \n")
    print("     -      EL "+str(float(((other_assigner_sh_2020*100)/(other_assigner_sh))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE OTRO DISTINTO A LOS ANTERIORES, FUERON PUBLICADAS EN 2020 \n")
    print("     -      EL "+str(float(((other_assigner_sh_2019*100)/(other_assigner_sh))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE OTRO DISTINTO A LOS ANTERIORES, FUERON PUBLICADAS EN 2019 \n")
    print("     -      EL "+str(float(((other_assigner_sh_2018*100)/(other_assigner_sh))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE OTRO DISTINTO A LOS ANTERIORES, FUERON PUBLICADAS EN 2018 O ANTERIORMENTE \n")
    print("\n")






























































    
    
    
    
    
    
    
    
print("**************************ESTADÍSTICAS CVE RELACION FECHA DE PUBLICACION Y ASIGNADOR PARTE IOT Y SMART HOME CONJUNTAS********************************")
print("\n")
print("\n")
print(" -  DE UN TOTAL DE "+str(total_assigner_iot+total_assigner_iot)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ESTÁ DEFINIDO, LAS ESTADÍSTICAS DE ASSIGNER Y FECHA DE PUBLICACION SON LAS SIGUIENTES  : \n")
print("\n")
print(" DE UN TOTAL DE "+str(assigner_iot_2023+assigner_sh_2023)+" VULNERABILIDADES PUBLICADAS EN 2023, LAS ESTADÍSTICAS DE ASIGNADORES CVE SON LAS SIGUIENTES : \n")
print("     -      EN "+str(jpcert_iot_2023+jpcert_sh_2023)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES VULTURES@JPCERT\n")
print("     -      EN "+str(mitre_iot_2023+mitre_sh_2023)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES CVE@MITRE \n")
print("     -      EN "+str(cisco_iot_2023+cisco_sh_2023)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES TALOS-CNA@CISCO \n")
print("     -      EN "+str(github_iot_2023+github_sh_2023)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY-ADVISORIES@GITHUB \n")
print("     -      EN "+str(redhat_iot_2023+redhat_sh_2023)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES SECALERT@REDHAT \n")
print("     -      EN "+str(qualcomm_iot_2023+qualcomm_sh_2023)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY.CNA@QUALCOMM \n")
print("     -      EN "+str(apache_iot_2023+apache_sh_2023)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY@APACHE.ORG \n")
print("     -      EN "+str(oracle_iot_2023+oracle_sh_2023)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES SECALERT_US@ORACLE \n")
print("     -      EN "+str(microsoft_iot_2023+microsoft_sh_2023)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURE@MICROSOFT \n")
print("     -      EN "+str(cert_iot_2023+cert_sh_2023)+" VULNERABILIDADES EL ASIGNADOR DE CVE INFO@CERT.VDE \n")
print("     -      EN "+str(trendmicro_iot_2023+trendmicro_sh_2023)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY@TRENDMICRO \n")
print("     -      EN "+str(nozomi_iot_2023+nozomi_sh_2023)+" VULNERABILIDADES EL ASIGNADOR DE CVE PRODSEC@NOZOMINETWORKS \n")
print("     -      EN "+str(hq_iot_2023+hq_sh_2023)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES ICS-CERT@HQ.DHS.GOV \n")
print("     -      EN "+str(kaspersky_iot_2023+kaspersky_sh_2023)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES VULNERABILITY@KASPERSKY \n")
print("     -      EN "+str(schneider_iot_2023+schneider_sh_2023)+" VULNERABILIDADES EL ASIGNADOR DE CVE CYBERSECURITY@SCHNEIDER-ELECTRIC \n")
print("     -      EN "+str(apple_iot_2023+apple_sh_2023)+" VULNERABILIDADES EL ASIGNADOR DE CVE PRODUCT-SECURITY@APPLE \n")
print("     -      EN "+str(android_iot_2023+android_sh_2023)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY@ANDROID \n")
print("     -      EN "+str(bitdefender_iot_2023+bitdefender_sh_2023)+" VULNERABILIDADES EL ASIGNADOR DE CVE CVE-REQUESTS@BITDEFENDER \n")
print("     -      EN "+str(mcafee_iot_2023+mcafee_sh_2023)+" VULNERABILIDADES EL ASIGNADOR DE CVE PSIRT@MCAFEE \n")
print("     -      EN "+str(mozilla_iot_2023+mozilla_sh_2023)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY@MOZILLA \n")
print("     -      EN "+str(hpe_iot_2023+hpe_sh_2023)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY-ALERT@HPE \n")
print("     -      EN "+str(fsecure_iot_2023+fsecure_sh_2023)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES CVE-NOTIFICATIONS-US@F-SECURE.COM \n")
print("     -      EN "+str(rapid7_iot_2023+rapid7_sh_2023)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES CVE@RAPID7 \n")
print("     -      EN "+str(other_assigner_iot_2023+other_assigner_sh_2023)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES DISTINTO DE LOS ANTERIORES \n")
print("\n")



print("\n")
print(" DE UN TOTAL DE "+str(assigner_iot_2022+assigner_sh_2022)+" VULNERABILIDADES PUBLICADAS EN 2022, LAS ESTADÍSTICAS DE ASIGNADORES CVE SON LAS SIGUIENTES : \n")
print("     -      EN "+str(jpcert_iot_2022+jpcert_sh_2022)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES VULTURES@JPCERT\n")
print("     -      EN "+str(mitre_iot_2022+mitre_sh_2022)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES CVE@MITRE \n")
print("     -      EN "+str(cisco_iot_2022+cisco_sh_2022)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES TALOS-CNA@CISCO \n")
print("     -      EN "+str(github_iot_2022+github_sh_2022)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY-ADVISORIES@GITHUB \n")
print("     -      EN "+str(redhat_iot_2022+redhat_sh_2022)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES SECALERT@REDHAT \n")
print("     -      EN "+str(qualcomm_iot_2022+qualcomm_sh_2022)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY.CNA@QUALCOMM \n")
print("     -      EN "+str(apache_iot_2022+apache_sh_2022)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY@APACHE.ORG \n")
print("     -      EN "+str(oracle_iot_2022+oracle_sh_2022)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES SECALERT_US@ORACLE \n")
print("     -      EN "+str(microsoft_iot_2022+microsoft_sh_2022)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURE@MICROSOFT \n")
print("     -      EN "+str(cert_iot_2022+cert_sh_2022)+" VULNERABILIDADES EL ASIGNADOR DE CVE INFO@CERT.VDE \n")
print("     -      EN "+str(trendmicro_iot_2022+trendmicro_sh_2022)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY@TRENDMICRO \n")
print("     -      EN "+str(nozomi_iot_2022+nozomi_sh_2022)+" VULNERABILIDADES EL ASIGNADOR DE CVE PRODSEC@NOZOMINETWORKS \n")
print("     -      EN "+str(hq_iot_2022+hq_sh_2022)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES ICS-CERT@HQ.DHS.GOV \n")
print("     -      EN "+str(kaspersky_iot_2022+kaspersky_sh_2022)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES VULNERABILITY@KASPERSKY \n")
print("     -      EN "+str(schneider_iot_2022+schneider_sh_2022)+" VULNERABILIDADES EL ASIGNADOR DE CVE CYBERSECURITY@SCHNEIDER-ELECTRIC \n")
print("     -      EN "+str(apple_iot_2022+apple_sh_2022)+" VULNERABILIDADES EL ASIGNADOR DE CVE PRODUCT-SECURITY@APPLE \n")
print("     -      EN "+str(android_iot_2022+android_sh_2022)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY@ANDROID \n")
print("     -      EN "+str(bitdefender_iot_2022+bitdefender_sh_2022)+" VULNERABILIDADES EL ASIGNADOR DE CVE CVE-REQUESTS@BITDEFENDER \n")
print("     -      EN "+str(mcafee_iot_2022+mcafee_sh_2022)+" VULNERABILIDADES EL ASIGNADOR DE CVE PSIRT@MCAFEE \n")
print("     -      EN "+str(mozilla_iot_2022+mozilla_sh_2022)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY@MOZILLA \n")
print("     -      EN "+str(hpe_iot_2022+hpe_sh_2022)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY-ALERT@HPE \n")
print("     -      EN "+str(fsecure_iot_2022+fsecure_sh_2022)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES CVE-NOTIFICATIONS-US@F-SECURE.COM \n")
print("     -      EN "+str(rapid7_iot_2022+rapid7_sh_2022)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES CVE@RAPID7 \n")
print("     -      EN "+str(other_assigner_iot_2022+other_assigner_sh_2022)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES DISTINTO DE LOS ANTERIORES \n")
print("\n")



print("\n")
print(" DE UN TOTAL DE "+str(assigner_iot_2021+assigner_sh_2021)+" VULNERABILIDADES PUBLICADAS EN 2021, LAS ESTADÍSTICAS DE ASIGNADORES CVE SON LAS SIGUIENTES : \n")
print("     -      EN "+str(jpcert_iot_2021+jpcert_sh_2021)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES VULTURES@JPCERT\n")
print("     -      EN "+str(mitre_iot_2021+mitre_sh_2021)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES CVE@MITRE \n")
print("     -      EN "+str(cisco_iot_2021+cisco_sh_2021)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES TALOS-CNA@CISCO \n")
print("     -      EN "+str(github_iot_2021+github_sh_2021)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY-ADVISORIES@GITHUB \n")
print("     -      EN "+str(redhat_iot_2021+redhat_sh_2021)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES SECALERT@REDHAT \n")
print("     -      EN "+str(qualcomm_iot_2021+qualcomm_sh_2021)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY.CNA@QUALCOMM \n")
print("     -      EN "+str(apache_iot_2021+apache_sh_2021)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY@APACHE.ORG \n")
print("     -      EN "+str(oracle_iot_2021+oracle_sh_2021)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES SECALERT_US@ORACLE \n")
print("     -      EN "+str(microsoft_iot_2021+microsoft_sh_2021)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURE@MICROSOFT \n")
print("     -      EN "+str(cert_iot_2021+cert_sh_2021)+" VULNERABILIDADES EL ASIGNADOR DE CVE INFO@CERT.VDE \n")
print("     -      EN "+str(trendmicro_iot_2021+trendmicro_sh_2021)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY@TRENDMICRO \n")
print("     -      EN "+str(nozomi_iot_2021+nozomi_sh_2021)+" VULNERABILIDADES EL ASIGNADOR DE CVE PRODSEC@NOZOMINETWORKS \n")
print("     -      EN "+str(hq_iot_2021+hq_sh_2021)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES ICS-CERT@HQ.DHS.GOV \n")
print("     -      EN "+str(kaspersky_iot_2021+kaspersky_sh_2021)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES VULNERABILITY@KASPERSKY \n")
print("     -      EN "+str(schneider_iot_2021+schneider_sh_2021)+" VULNERABILIDADES EL ASIGNADOR DE CVE CYBERSECURITY@SCHNEIDER-ELECTRIC \n")
print("     -      EN "+str(apple_iot_2021+apple_sh_2021)+" VULNERABILIDADES EL ASIGNADOR DE CVE PRODUCT-SECURITY@APPLE \n")
print("     -      EN "+str(android_iot_2021+android_sh_2021)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY@ANDROID \n")
print("     -      EN "+str(bitdefender_iot_2021+bitdefender_sh_2021)+" VULNERABILIDADES EL ASIGNADOR DE CVE CVE-REQUESTS@BITDEFENDER \n")
print("     -      EN "+str(mcafee_iot_2021+mcafee_sh_2021)+" VULNERABILIDADES EL ASIGNADOR DE CVE PSIRT@MCAFEE \n")
print("     -      EN "+str(mozilla_iot_2021+mozilla_sh_2021)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY@MOZILLA \n")
print("     -      EN "+str(hpe_iot_2021+hpe_sh_2021)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY-ALERT@HPE \n")
print("     -      EN "+str(fsecure_iot_2021+fsecure_sh_2021)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES CVE-NOTIFICATIONS-US@F-SECURE.COM \n")
print("     -      EN "+str(rapid7_iot_2021+rapid7_sh_2021)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES CVE@RAPID7 \n")
print("     -      EN "+str(other_assigner_iot_2021+other_assigner_sh_2021)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES DISTINTO DE LOS ANTERIORES \n")
print("\n")



print("\n")
print(" DE UN TOTAL DE "+str(assigner_iot_2020+assigner_sh_2020)+" VULNERABILIDADES PUBLICADAS EN 2020, LAS ESTADÍSTICAS DE ASIGNADORES CVE SON LAS SIGUIENTES : \n")
print("     -      EN "+str(jpcert_iot_2020+jpcert_sh_2020)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES VULTURES@JPCERT\n")
print("     -      EN "+str(mitre_iot_2020+mitre_sh_2020)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES CVE@MITRE \n")
print("     -      EN "+str(cisco_iot_2020+cisco_sh_2020)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES TALOS-CNA@CISCO \n")
print("     -      EN "+str(github_iot_2020+github_sh_2020)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY-ADVISORIES@GITHUB \n")
print("     -      EN "+str(redhat_iot_2020+redhat_sh_2020)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES SECALERT@REDHAT \n")
print("     -      EN "+str(qualcomm_iot_2020+qualcomm_sh_2020)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY.CNA@QUALCOMM \n")
print("     -      EN "+str(apache_iot_2020+apache_sh_2020)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY@APACHE.ORG \n")
print("     -      EN "+str(oracle_iot_2020+oracle_sh_2020)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES SECALERT_US@ORACLE \n")
print("     -      EN "+str(microsoft_iot_2020+microsoft_sh_2020)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURE@MICROSOFT \n")
print("     -      EN "+str(cert_iot_2020+cert_sh_2020)+" VULNERABILIDADES EL ASIGNADOR DE CVE INFO@CERT.VDE \n")
print("     -      EN "+str(trendmicro_iot_2020+trendmicro_sh_2020)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY@TRENDMICRO \n")
print("     -      EN "+str(nozomi_iot_2020+nozomi_sh_2020)+" VULNERABILIDADES EL ASIGNADOR DE CVE PRODSEC@NOZOMINETWORKS \n")
print("     -      EN "+str(hq_iot_2020+hq_sh_2020)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES ICS-CERT@HQ.DHS.GOV \n")
print("     -      EN "+str(kaspersky_iot_2020+kaspersky_sh_2020)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES VULNERABILITY@KASPERSKY \n")
print("     -      EN "+str(schneider_iot_2020+schneider_sh_2020)+" VULNERABILIDADES EL ASIGNADOR DE CVE CYBERSECURITY@SCHNEIDER-ELECTRIC \n")
print("     -      EN "+str(apple_iot_2020+apple_sh_2020)+" VULNERABILIDADES EL ASIGNADOR DE CVE PRODUCT-SECURITY@APPLE \n")
print("     -      EN "+str(android_iot_2020+android_sh_2020)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY@ANDROID \n")
print("     -      EN "+str(bitdefender_iot_2020+bitdefender_sh_2020)+" VULNERABILIDADES EL ASIGNADOR DE CVE CVE-REQUESTS@BITDEFENDER \n")
print("     -      EN "+str(mcafee_iot_2020+mcafee_sh_2020)+" VULNERABILIDADES EL ASIGNADOR DE CVE PSIRT@MCAFEE \n")
print("     -      EN "+str(mozilla_iot_2020+mozilla_sh_2020)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY@MOZILLA \n")
print("     -      EN "+str(hpe_iot_2020+hpe_sh_2020)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY-ALERT@HPE \n")
print("     -      EN "+str(fsecure_iot_2020+fsecure_sh_2020)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES CVE-NOTIFICATIONS-US@F-SECURE.COM \n")
print("     -      EN "+str(rapid7_iot_2020+rapid7_sh_2020)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES CVE@RAPID7 \n")
print("     -      EN "+str(other_assigner_iot_2020+other_assigner_sh_2020)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES DISTINTO DE LOS ANTERIORES \n")
print("\n")



print("\n")
print(" DE UN TOTAL DE "+str(assigner_iot_2019+assigner_sh_2019)+" VULNERABILIDADES PUBLICADAS EN 2019, LAS ESTADÍSTICAS DE ASIGNADORES CVE SON LAS SIGUIENTES : \n")
print("     -      EN "+str(jpcert_iot_2019+jpcert_sh_2019)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES VULTURES@JPCERT\n")
print("     -      EN "+str(mitre_iot_2019+mitre_sh_2019)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES CVE@MITRE \n")
print("     -      EN "+str(cisco_iot_2019+cisco_sh_2019)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES TALOS-CNA@CISCO \n")
print("     -      EN "+str(github_iot_2019+github_sh_2019)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY-ADVISORIES@GITHUB \n")
print("     -      EN "+str(redhat_iot_2019+redhat_sh_2019)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES SECALERT@REDHAT \n")
print("     -      EN "+str(qualcomm_iot_2019+qualcomm_sh_2019)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY.CNA@QUALCOMM \n")
print("     -      EN "+str(apache_iot_2019+apache_sh_2019)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY@APACHE.ORG \n")
print("     -      EN "+str(oracle_iot_2019+oracle_sh_2019)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES SECALERT_US@ORACLE \n")
print("     -      EN "+str(microsoft_iot_2019+microsoft_sh_2019)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURE@MICROSOFT \n")
print("     -      EN "+str(cert_iot_2019+cert_sh_2019)+" VULNERABILIDADES EL ASIGNADOR DE CVE INFO@CERT.VDE \n")
print("     -      EN "+str(trendmicro_iot_2019+trendmicro_sh_2019)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY@TRENDMICRO \n")
print("     -      EN "+str(nozomi_iot_2019+nozomi_sh_2019)+" VULNERABILIDADES EL ASIGNADOR DE CVE PRODSEC@NOZOMINETWORKS \n")
print("     -      EN "+str(hq_iot_2019+hq_sh_2019)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES ICS-CERT@HQ.DHS.GOV \n")
print("     -      EN "+str(kaspersky_iot_2019+kaspersky_sh_2019)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES VULNERABILITY@KASPERSKY \n")
print("     -      EN "+str(schneider_iot_2019+schneider_sh_2019)+" VULNERABILIDADES EL ASIGNADOR DE CVE CYBERSECURITY@SCHNEIDER-ELECTRIC \n")
print("     -      EN "+str(apple_iot_2019+apple_sh_2019)+" VULNERABILIDADES EL ASIGNADOR DE CVE PRODUCT-SECURITY@APPLE \n")
print("     -      EN "+str(android_iot_2019+android_sh_2019)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY@ANDROID \n")
print("     -      EN "+str(bitdefender_iot_2019+bitdefender_sh_2019)+" VULNERABILIDADES EL ASIGNADOR DE CVE CVE-REQUESTS@BITDEFENDER \n")
print("     -      EN "+str(mcafee_iot_2019+mcafee_sh_2019)+" VULNERABILIDADES EL ASIGNADOR DE CVE PSIRT@MCAFEE \n")
print("     -      EN "+str(mozilla_iot_2019+mozilla_sh_2019)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY@MOZILLA \n")
print("     -      EN "+str(hpe_iot_2019+hpe_sh_2019)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY-ALERT@HPE \n")
print("     -      EN "+str(fsecure_iot_2019+fsecure_sh_2019)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES CVE-NOTIFICATIONS-US@F-SECURE.COM \n")
print("     -      EN "+str(rapid7_iot_2019+rapid7_sh_2019)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES CVE@RAPID7 \n")
print("     -      EN "+str(other_assigner_iot_2019+other_assigner_sh_2019)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES DISTINTO DE LOS ANTERIORES \n")
print("\n")



print("\n")
print(" DE UN TOTAL DE "+str(assigner_iot_2018+assigner_sh_2018)+" VULNERABILIDADES PUBLICADAS EN 2018 O ANTERIORMENTE, LAS ESTADÍSTICAS DE ASIGNADORES CVE SON LAS SIGUIENTES : \n")
print("     -      EN "+str(jpcert_iot_2018+jpcert_sh_2018)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES VULTURES@JPCERT\n")
print("     -      EN "+str(mitre_iot_2018+mitre_sh_2018)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES CVE@MITRE \n")
print("     -      EN "+str(cisco_iot_2018+cisco_sh_2018)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES TALOS-CNA@CISCO \n")
print("     -      EN "+str(github_iot_2018+github_sh_2018)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY-ADVISORIES@GITHUB \n")
print("     -      EN "+str(redhat_iot_2018+redhat_sh_2018)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES SECALERT@REDHAT \n")
print("     -      EN "+str(qualcomm_iot_2018+qualcomm_sh_2018)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY.CNA@QUALCOMM \n")
print("     -      EN "+str(apache_iot_2018+apache_sh_2018)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY@APACHE.ORG \n")
print("     -      EN "+str(oracle_iot_2018+oracle_sh_2018)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES SECALERT_US@ORACLE \n")
print("     -      EN "+str(microsoft_iot_2018+microsoft_sh_2018)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURE@MICROSOFT \n")
print("     -      EN "+str(cert_iot_2018+cert_sh_2018)+" VULNERABILIDADES EL ASIGNADOR DE CVE INFO@CERT.VDE \n")
print("     -      EN "+str(trendmicro_iot_2018+trendmicro_sh_2018)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY@TRENDMICRO \n")
print("     -      EN "+str(nozomi_iot_2018+nozomi_sh_2018)+" VULNERABILIDADES EL ASIGNADOR DE CVE PRODSEC@NOZOMINETWORKS \n")
print("     -      EN "+str(hq_iot_2018+hq_sh_2018)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES ICS-CERT@HQ.DHS.GOV \n")
print("     -      EN "+str(kaspersky_iot_2018+kaspersky_sh_2018)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES VULNERABILITY@KASPERSKY \n")
print("     -      EN "+str(schneider_iot_2018+schneider_sh_2018)+" VULNERABILIDADES EL ASIGNADOR DE CVE CYBERSECURITY@SCHNEIDER-ELECTRIC \n")
print("     -      EN "+str(apple_iot_2018+apple_sh_2018)+" VULNERABILIDADES EL ASIGNADOR DE CVE PRODUCT-SECURITY@APPLE \n")
print("     -      EN "+str(android_iot_2018+android_sh_2018)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY@ANDROID \n")
print("     -      EN "+str(bitdefender_iot_2018+bitdefender_sh_2018)+" VULNERABILIDADES EL ASIGNADOR DE CVE CVE-REQUESTS@BITDEFENDER \n")
print("     -      EN "+str(mcafee_iot_2018+mcafee_sh_2018)+" VULNERABILIDADES EL ASIGNADOR DE CVE PSIRT@MCAFEE \n")
print("     -      EN "+str(mozilla_iot_2018+mozilla_sh_2018)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY@MOZILLA \n")
print("     -      EN "+str(hpe_iot_2018+hpe_sh_2018)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY-ALERT@HPE \n")
print("     -      EN "+str(fsecure_iot_2018+fsecure_sh_2018)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES CVE-NOTIFICATIONS-US@F-SECURE.COM \n")
print("     -      EN "+str(rapid7_iot_2018+rapid7_sh_2018)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES CVE@RAPID7 \n")
print("     -      EN "+str(other_assigner_iot_2018+other_assigner_sh_2018)+" VULNERABILIDADES EL ASIGNADOR DE CVE ES DISTINTO DE LOS ANTERIORES \n")
print("\n")




print("************************** ESTADÍSTICAS ASIGNADOR CVE SEGÚN FECHA DE PUBLICACIÓN PARTE IOT Y SMART HOME CONJUNTAS********************************")
print("\n")

print(" DE UN TOTAL DE "+str(jpcert_sh+jpcert_iot)+" VULNERABILIDADES PUBLICADAS DONDE EL ASIGNADOR DE CVE ES VULTURES@JPCERT, LAS ESTADÍSTICAS SEGÚN LA FECHA DE PUBLICACION SON : \n")
print("     -      UN TOTAL DE "+str(jpcert_sh_2023+jpcert_iot_2023)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES VULTURES@JPCERTFUERON PUBLICADAS EN 2023 \n")
print("     -      UN TOTAL DE "+str(jpcert_sh_2022+jpcert_iot_2022)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES VULTURES@JPCERTFUERON PUBLICADAS EN 2022 \n")
print("     -      UN TOTAL DE "+str(jpcert_sh_2021+jpcert_iot_2021)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES VULTURES@JPCERTFUERON PUBLICADAS EN 2021 \n")
print("     -      UN TOTAL DE "+str(jpcert_sh_2020+jpcert_iot_2020)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES VULTURES@JPCERTFUERON PUBLICADAS EN 2020 \n")
print("     -      UN TOTAL DE "+str(jpcert_sh_2019+jpcert_iot_2019)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES VULTURES@JPCERTFUERON PUBLICADAS EN 2019 \n")
print("     -      UN TOTAL DE "+str(jpcert_sh_2018+jpcert_iot_2018)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES VULTURES@JPCERTFUERON PUBLICADAS EN 2018 O ANTERIORMENTE \n")
print("\n")

print(" DE UN TOTAL DE "+str(mitre_sh+mitre_iot)+" VULNERABILIDADES PUBLICADAS DONDE EL ASIGNADOR DE CVE ES CVE@MITRE, LAS ESTADÍSTICAS SEGÚN LA FECHA DE PUBLICACION SON : \n")
print("     -      UN TOTAL DE "+str(mitre_sh_2023+mitre_iot_2023)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES CVE@MITRE FUERON PUBLICADAS EN 2023 \n")
print("     -      UN TOTAL DE "+str(mitre_sh_2022+mitre_iot_2022)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES CVE@MITRE FUERON PUBLICADAS EN 2022 \n")
print("     -      UN TOTAL DE "+str(mitre_sh_2021+mitre_iot_2021)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES CVE@MITRE FUERON PUBLICADAS EN 2021 \n")
print("     -      UN TOTAL DE "+str(mitre_sh_2020+mitre_iot_2020)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES CVE@MITRE FUERON PUBLICADAS EN 2020 \n")
print("     -      UN TOTAL DE "+str(mitre_sh_2019+mitre_iot_2019)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES CVE@MITRE FUERON PUBLICADAS EN 2019 \n")
print("     -      UN TOTAL DE "+str(mitre_sh_2018+mitre_iot_2018)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES CVE@MITRE FUERON PUBLICADAS EN 2018 O ANTERIORMENTE \n")
print("\n")

print(" DE UN TOTAL DE "+str(cisco_sh+cisco_iot)+" VULNERABILIDADES PUBLICADAS DONDE EL ASIGNADOR DE CVE ES TALOS-CNA@CISCO, LAS ESTADÍSTICAS SEGÚN LA FECHA DE PUBLICACION SON : \n")
print("     -      UN TOTAL DE "+str(cisco_sh_2023+cisco_iot_2023)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES TALOS-CNA@CISCO FUERON PUBLICADAS EN 2023 \n")
print("     -      UN TOTAL DE "+str(cisco_sh_2022+cisco_iot_2022)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES TALOS-CNA@CISCO FUERON PUBLICADAS EN 2022 \n")
print("     -      UN TOTAL DE "+str(cisco_sh_2021+cisco_iot_2021)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES TALOS-CNA@CISCO FUERON PUBLICADAS EN 2021 \n")
print("     -      UN TOTAL DE "+str(cisco_sh_2020+cisco_iot_2020)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES TALOS-CNA@CISCO FUERON PUBLICADAS EN 2020 \n")
print("     -      UN TOTAL DE "+str(cisco_sh_2019+cisco_iot_2019)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES TALOS-CNA@CISCO FUERON PUBLICADAS EN 2019 \n")
print("     -      UN TOTAL DE "+str(cisco_sh_2018+cisco_iot_2018)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES TALOS-CNA@CISCO FUERON PUBLICADAS EN 2018 O ANTERIORMENTE \n")
print("\n")

print(" DE UN TOTAL DE "+str(github_sh+github_iot)+" VULNERABILIDADES PUBLICADAS DONDE EL ASIGNADOR DE CVE ES SECURITY-ADVISORIES@GITHUB, LAS ESTADÍSTICAS SEGÚN LA FECHA DE PUBLICACION SON : \n")
print("     -      UN TOTAL DE "+str(github_sh_2023+github_iot_2023)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY-ADVISORIES@GITHUB FUERON PUBLICADAS EN 2023 \n")
print("     -      UN TOTAL DE "+str(github_sh_2022+github_iot_2022)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY-ADVISORIES@GITHUB FUERON PUBLICADAS EN 2022 \n")
print("     -      UN TOTAL DE "+str(github_sh_2021+github_iot_2021)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY-ADVISORIES@GITHUB FUERON PUBLICADAS EN 2021 \n")
print("     -      UN TOTAL DE "+str(github_sh_2020+github_iot_2020)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY-ADVISORIES@GITHUB FUERON PUBLICADAS EN 2020 \n")
print("     -      UN TOTAL DE "+str(github_sh_2019+github_iot_2019)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY-ADVISORIES@GITHUB FUERON PUBLICADAS EN 2019 \n")
print("     -      UN TOTAL DE "+str(github_sh_2018+github_iot_2018)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY-ADVISORIES@GITHUB FUERON PUBLICADAS EN 2018 O ANTERIORMENTE \n")
print("\n")

print(" DE UN TOTAL DE "+str(redhat_sh+redhat_iot)+" VULNERABILIDADES PUBLICADAS DONDE EL ASIGNADOR DE CVE ES SECALERT@REDHAT, LAS ESTADÍSTICAS SEGÚN LA FECHA DE PUBLICACION SON : \n")
print("     -      UN TOTAL DE "+str(redhat_sh_2023+redhat_iot_2023)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECALERT@REDHAT FUERON PUBLICADAS EN 2023 \n")
print("     -      UN TOTAL DE "+str(redhat_sh_2022+redhat_iot_2022)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECALERT@REDHAT FUERON PUBLICADAS EN 2022 \n")
print("     -      UN TOTAL DE "+str(redhat_sh_2021+redhat_iot_2021)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECALERT@REDHAT FUERON PUBLICADAS EN 2021 \n")
print("     -      UN TOTAL DE "+str(redhat_sh_2020+redhat_iot_2020)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECALERT@REDHAT FUERON PUBLICADAS EN 2020 \n")
print("     -      UN TOTAL DE "+str(redhat_sh_2019+redhat_iot_2019)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECALERT@REDHAT FUERON PUBLICADAS EN 2019 \n")
print("     -      UN TOTAL DE "+str(redhat_sh_2018+redhat_iot_2018)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECALERT@REDHAT FUERON PUBLICADAS EN 2018 O ANTERIORMENTE \n")
print("\n")

print(" DE UN TOTAL DE "+str(qualcomm_sh+qualcomm_iot)+" VULNERABILIDADES PUBLICADAS DONDE EL ASIGNADOR DE CVE ES SECURITY.CNA@QUALCOMM, LAS ESTADÍSTICAS SEGÚN LA FECHA DE PUBLICACION SON : \n")
print("     -      UN TOTAL DE "+str(qualcomm_sh_2023+qualcomm_iot_2023)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY.CNA@QUALCOMM FUERON PUBLICADAS EN 2023 \n")
print("     -      UN TOTAL DE "+str(qualcomm_sh_2022+qualcomm_iot_2022)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY.CNA@QUALCOMM FUERON PUBLICADAS EN 2022 \n")
print("     -      UN TOTAL DE "+str(qualcomm_sh_2021+qualcomm_iot_2021)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY.CNA@QUALCOMM FUERON PUBLICADAS EN 2021 \n")
print("     -      UN TOTAL DE "+str(qualcomm_sh_2020+qualcomm_iot_2020)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY.CNA@QUALCOMM FUERON PUBLICADAS EN 2020 \n")
print("     -      UN TOTAL DE "+str(qualcomm_sh_2019+qualcomm_iot_2019)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY.CNA@QUALCOMM FUERON PUBLICADAS EN 2019 \n")
print("     -      UN TOTAL DE "+str(qualcomm_sh_2018+qualcomm_iot_2018)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY.CNA@QUALCOMM FUERON PUBLICADAS EN 2018 O ANTERIORMENTE \n")
print("\n")

print(" DE UN TOTAL DE "+str(apache_sh+apache_iot)+" VULNERABILIDADES PUBLICADAS DONDE EL ASIGNADOR DE CVE ES SECURITY@APACHE.ORG, LAS ESTADÍSTICAS SEGÚN LA FECHA DE PUBLICACION SON : \n")
print("     -      UN TOTAL DE "+str(apache_sh_2023+apache_iot_2023)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY@APACHE.ORG FUERON PUBLICADAS EN 2023 \n")
print("     -      UN TOTAL DE "+str(apache_sh_2022+apache_iot_2022)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY@APACHE.ORG FUERON PUBLICADAS EN 2022 \n")
print("     -      UN TOTAL DE "+str(apache_sh_2021+apache_iot_2021)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY@APACHE.ORG FUERON PUBLICADAS EN 2021 \n")
print("     -      UN TOTAL DE "+str(apache_sh_2020+apache_iot_2020)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY@APACHE.ORG FUERON PUBLICADAS EN 2020 \n")
print("     -      UN TOTAL DE "+str(apache_sh_2019+apache_iot_2019)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY@APACHE.ORG FUERON PUBLICADAS EN 2019 \n")
print("     -      UN TOTAL DE "+str(apache_sh_2018+apache_iot_2018)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY@APACHE.ORG FUERON PUBLICADAS EN 2018 O ANTERIORMENTE \n")
print("\n")

print(" DE UN TOTAL DE "+str(oracle_sh+oracle_iot)+" VULNERABILIDADES PUBLICADAS DONDE EL ASIGNADOR DE CVE ES SECALERT_US@ORACLE, LAS ESTADÍSTICAS SEGÚN LA FECHA DE PUBLICACION SON : \n")
print("     -      UN TOTAL DE "+str(oracle_sh_2023+oracle_iot_2023)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECALERT_US@ORACLE FUERON PUBLICADAS EN 2023 \n")
print("     -      UN TOTAL DE "+str(oracle_sh_2022+oracle_iot_2022)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECALERT_US@ORACLE FUERON PUBLICADAS EN 2022 \n")
print("     -      UN TOTAL DE "+str(oracle_sh_2021+oracle_iot_2021)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECALERT_US@ORACLE FUERON PUBLICADAS EN 2021 \n")
print("     -      UN TOTAL DE "+str(oracle_sh_2020+oracle_iot_2020)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECALERT_US@ORACLE FUERON PUBLICADAS EN 2020 \n")
print("     -      UN TOTAL DE "+str(oracle_sh_2019+oracle_iot_2019)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECALERT_US@ORACLE FUERON PUBLICADAS EN 2019 \n")
print("     -      UN TOTAL DE "+str(oracle_sh_2018+oracle_iot_2018)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECALERT_US@ORACLE FUERON PUBLICADAS EN 2018 O ANTERIORMENTE \n")
print("\n")


print(" DE UN TOTAL DE "+str(microsoft_sh+microsoft_iot)+" VULNERABILIDADES PUBLICADAS DONDE EL ASIGNADOR DE CVE ES SECURE@MICROSOFT, LAS ESTADÍSTICAS SEGÚN LA FECHA DE PUBLICACION SON : \n")
print("     -      UN TOTAL DE "+str(microsoft_sh_2023+microsoft_iot_2023)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURE@MICROSOFT FUERON PUBLICADAS EN 2023 \n")
print("     -      UN TOTAL DE "+str(microsoft_sh_2022+microsoft_iot_2022)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURE@MICROSOFT FUERON PUBLICADAS EN 2022 \n")
print("     -      UN TOTAL DE "+str(microsoft_sh_2021+microsoft_iot_2021)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURE@MICROSOFT FUERON PUBLICADAS EN 2021 \n")
print("     -      UN TOTAL DE "+str(microsoft_sh_2020+microsoft_iot_2020)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURE@MICROSOFT FUERON PUBLICADAS EN 2020 \n")
print("     -      UN TOTAL DE "+str(microsoft_sh_2019+microsoft_iot_2019)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURE@MICROSOFT FUERON PUBLICADAS EN 2019 \n")
print("     -      UN TOTAL DE "+str(microsoft_sh_2018+microsoft_iot_2018)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURE@MICROSOFT FUERON PUBLICADAS EN 2018 O ANTERIORMENTE \n")
print("\n")


print(" DE UN TOTAL DE "+str(cert_sh+cert_iot)+" VULNERABILIDADES PUBLICADAS DONDE EL ASIGNADOR DE CVE INFO@CERT.VDE, LAS ESTADÍSTICAS SEGÚN LA FECHA DE PUBLICACION SON : \n")
print("     -      UN TOTAL DE "+str(cert_sh_2023+cert_iot_2023)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE INFO@CERT.VDE FUERON PUBLICADAS EN 2023 \n")
print("     -      UN TOTAL DE "+str(cert_sh_2022+cert_iot_2022)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE INFO@CERT.VDE FUERON PUBLICADAS EN 2022 \n")
print("     -      UN TOTAL DE "+str(cert_sh_2021+cert_iot_2021)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE INFO@CERT.VDE FUERON PUBLICADAS EN 2021 \n")
print("     -      UN TOTAL DE "+str(cert_sh_2020+cert_iot_2020)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE INFO@CERT.VDE FUERON PUBLICADAS EN 2020 \n")
print("     -      UN TOTAL DE "+str(cert_sh_2019+cert_iot_2019)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE INFO@CERT.VDE FUERON PUBLICADAS EN 2019 \n")
print("     -      UN TOTAL DE "+str(cert_sh_2018+cert_iot_2018)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE INFO@CERT.VDE FUERON PUBLICADAS EN 2018 O ANTERIORMENTE \n")
print("\n")


print(" DE UN TOTAL DE "+str(trendmicro_sh+trendmicro_iot)+" VULNERABILIDADES PUBLICADAS DONDE EL ASIGNADOR DE CVE ES SECURITY@TRENDMICRO, LAS ESTADÍSTICAS SEGÚN LA FECHA DE PUBLICACION SON : \n")
print("     -      UN TOTAL DE "+str(trendmicro_sh_2023+trendmicro_iot_2023)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY@TRENDMICRO FUERON PUBLICADAS EN 2023 \n")
print("     -      UN TOTAL DE "+str(trendmicro_sh_2022+trendmicro_iot_2022)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY@TRENDMICRO FUERON PUBLICADAS EN 2022 \n")
print("     -      UN TOTAL DE "+str(trendmicro_sh_2021+trendmicro_iot_2021)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY@TRENDMICRO FUERON PUBLICADAS EN 2021 \n")
print("     -      UN TOTAL DE "+str(trendmicro_sh_2020+trendmicro_iot_2020)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY@TRENDMICRO FUERON PUBLICADAS EN 2020 \n")
print("     -      UN TOTAL DE "+str(trendmicro_sh_2019+trendmicro_iot_2019)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY@TRENDMICRO FUERON PUBLICADAS EN 2019 \n")
print("     -      UN TOTAL DE "+str(trendmicro_sh_2018+trendmicro_iot_2018)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY@TRENDMICRO FUERON PUBLICADAS EN 2018 O ANTERIORMENTE \n")
print("\n")


print(" DE UN TOTAL DE "+str(nozomi_sh+nozomi_iot)+" VULNERABILIDADES PUBLICADAS DONDE EL ASIGNADOR DE CVE PRODSEC@NOZOMINETWORKS, LAS ESTADÍSTICAS SEGÚN LA FECHA DE PUBLICACION SON : \n")
print("     -      UN TOTAL DE "+str(nozomi_sh_2023+nozomi_iot_2023)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE PRODSEC@NOZOMINETWORKS FUERON PUBLICADAS EN 2023 \n")
print("     -      UN TOTAL DE "+str(nozomi_sh_2022+nozomi_iot_2022)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE PRODSEC@NOZOMINETWORKS FUERON PUBLICADAS EN 2022 \n")
print("     -      UN TOTAL DE "+str(nozomi_sh_2021+nozomi_iot_2021)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE PRODSEC@NOZOMINETWORKS FUERON PUBLICADAS EN 2021 \n")
print("     -      UN TOTAL DE "+str(nozomi_sh_2020+nozomi_iot_2020)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE PRODSEC@NOZOMINETWORKS FUERON PUBLICADAS EN 2020 \n")
print("     -      UN TOTAL DE "+str(nozomi_sh_2019+nozomi_iot_2019)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE PRODSEC@NOZOMINETWORKS FUERON PUBLICADAS EN 2019 \n")
print("     -      UN TOTAL DE "+str(nozomi_sh_2018+nozomi_iot_2018)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE PRODSEC@NOZOMINETWORKS FUERON PUBLICADAS EN 2018 O ANTERIORMENTE \n")
print("\n")


print(" DE UN TOTAL DE "+str(hq_sh+hq_iot)+" VULNERABILIDADES PUBLICADAS DONDE EL ASIGNADOR DE CVE ES ICS-CERT@HQ.DHS.GOV, LAS ESTADÍSTICAS SEGÚN LA FECHA DE PUBLICACION SON : \n")
print("     -      UN TOTAL DE "+str(hq_sh_2023+hq_iot_2023)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES ICS-CERT@HQ.DHS.GOV FUERON PUBLICADAS EN 2023 \n")
print("     -      UN TOTAL DE "+str(hq_sh_2022+hq_iot_2022)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES ICS-CERT@HQ.DHS.GOV FUERON PUBLICADAS EN 2022 \n")
print("     -      UN TOTAL DE "+str(hq_sh_2021+hq_iot_2021)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES ICS-CERT@HQ.DHS.GOV FUERON PUBLICADAS EN 2021 \n")
print("     -      UN TOTAL DE "+str(hq_sh_2020+hq_iot_2020)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES ICS-CERT@HQ.DHS.GOV FUERON PUBLICADAS EN 2020 \n")
print("     -      UN TOTAL DE "+str(hq_sh_2019+hq_iot_2019)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES ICS-CERT@HQ.DHS.GOV FUERON PUBLICADAS EN 2019 \n")
print("     -      UN TOTAL DE "+str(hq_sh_2018+hq_iot_2018)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES ICS-CERT@HQ.DHS.GOV FUERON PUBLICADAS EN 2018 O ANTERIORMENTE \n")
print("\n")

print(" DE UN TOTAL DE "+str(kaspersky_sh+kaspersky_iot)+" VULNERABILIDADES PUBLICADAS DONDE EL ASIGNADOR DE CVE ES VULNERABILITY@KASPERSKY, LAS ESTADÍSTICAS SEGÚN LA FECHA DE PUBLICACION SON : \n")
print("     -      UN TOTAL DE "+str(kaspersky_sh_2023+kaspersky_iot_2023)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES VULNERABILITY@KASPERSKY FUERON PUBLICADAS EN 2023 \n")
print("     -      UN TOTAL DE "+str(kaspersky_sh_2022+kaspersky_iot_2022)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES VULNERABILITY@KASPERSKY FUERON PUBLICADAS EN 2022 \n")
print("     -      UN TOTAL DE "+str(kaspersky_sh_2021+kaspersky_iot_2021)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES VULNERABILITY@KASPERSKY FUERON PUBLICADAS EN 2021 \n")
print("     -      UN TOTAL DE "+str(kaspersky_sh_2020+kaspersky_iot_2020)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES VULNERABILITY@KASPERSKY FUERON PUBLICADAS EN 2020 \n")
print("     -      UN TOTAL DE "+str(kaspersky_sh_2019+kaspersky_iot_2019)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES VULNERABILITY@KASPERSKY FUERON PUBLICADAS EN 2019 \n")
print("     -      UN TOTAL DE "+str(kaspersky_sh_2018+kaspersky_iot_2018)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES VULNERABILITY@KASPERSKY FUERON PUBLICADAS EN 2018 O ANTERIORMENTE \n")
print("\n")


print(" DE UN TOTAL DE "+str(schneider_sh+schneider_iot)+" VULNERABILIDADES PUBLICADAS DONDE EL ASIGNADOR DE CVE CYBERSECURITY@SCHNEIDER-ELECTRIC, LAS ESTADÍSTICAS SEGÚN LA FECHA DE PUBLICACION SON : \n")
print("     -      UN TOTAL DE "+str(schneider_sh_2023+schneider_iot_2023)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE CYBERSECURITY@SCHNEIDER-ELECTRIC FUERON PUBLICADAS EN 2023 \n")
print("     -      UN TOTAL DE "+str(schneider_sh_2022+schneider_iot_2022)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE CYBERSECURITY@SCHNEIDER-ELECTRIC FUERON PUBLICADAS EN 2022 \n")
print("     -      UN TOTAL DE "+str(schneider_sh_2021+schneider_iot_2021)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE CYBERSECURITY@SCHNEIDER-ELECTRIC FUERON PUBLICADAS EN 2021 \n")
print("     -      UN TOTAL DE "+str(schneider_sh_2020+schneider_iot_2020)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE CYBERSECURITY@SCHNEIDER-ELECTRIC FUERON PUBLICADAS EN 2020 \n")
print("     -      UN TOTAL DE "+str(schneider_sh_2019+schneider_iot_2019)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE CYBERSECURITY@SCHNEIDER-ELECTRIC FUERON PUBLICADAS EN 2019 \n")
print("     -      UN TOTAL DE "+str(schneider_sh_2018+schneider_iot_2018)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE CYBERSECURITY@SCHNEIDER-ELECTRIC FUERON PUBLICADAS EN 2018 O ANTERIORMENTE \n")
print("\n")

print(" DE UN TOTAL DE "+str(apple_sh+apple_iot)+" VULNERABILIDADES PUBLICADAS DONDE EL ASIGNADOR DE CVE PRODUCT-SECURITY@APPLE, LAS ESTADÍSTICAS SEGÚN LA FECHA DE PUBLICACION SON : \n")
print("     -      UN TOTAL DE "+str(apple_sh_2023+apple_iot_2023)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE PRODUCT-SECURITY@APPLE FUERON PUBLICADAS EN 2023 \n")
print("     -      UN TOTAL DE "+str(apple_sh_2022+apple_iot_2022)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE PRODUCT-SECURITY@APPLE FUERON PUBLICADAS EN 2022 \n")
print("     -      UN TOTAL DE "+str(apple_sh_2021+apple_iot_2021)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE PRODUCT-SECURITY@APPLE FUERON PUBLICADAS EN 2021 \n")
print("     -      UN TOTAL DE "+str(apple_sh_2020+apple_iot_2020)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE PRODUCT-SECURITY@APPLE FUERON PUBLICADAS EN 2020 \n")
print("     -      UN TOTAL DE "+str(apple_sh_2019+apple_iot_2019)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE PRODUCT-SECURITY@APPLE FUERON PUBLICADAS EN 2019 \n")
print("     -      UN TOTAL DE "+str(apple_sh_2018+apple_iot_2018)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE PRODUCT-SECURITY@APPLE FUERON PUBLICADAS EN 2018 O ANTERIORMENTE \n")
print("\n")

print(" DE UN TOTAL DE "+str(android_sh+android_iot)+" VULNERABILIDADES PUBLICADAS DONDE EL ASIGNADOR DE CVE ES SECURITY@ANDROID, LAS ESTADÍSTICAS SEGÚN LA FECHA DE PUBLICACION SON : \n")
print("     -      UN TOTAL DE "+str(android_sh_2023+android_iot_2023)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY@ANDROID FUERON PUBLICADAS EN 2023 \n")
print("     -      UN TOTAL DE "+str(android_sh_2022+android_iot_2022)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY@ANDROID FUERON PUBLICADAS EN 2022 \n")
print("     -      UN TOTAL DE "+str(android_sh_2021+android_iot_2021)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY@ANDROID FUERON PUBLICADAS EN 2021 \n")
print("     -      UN TOTAL DE "+str(android_sh_2020+android_iot_2020)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY@ANDROID FUERON PUBLICADAS EN 2020 \n")
print("     -      UN TOTAL DE "+str(android_sh_2019+android_iot_2019)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY@ANDROID FUERON PUBLICADAS EN 2019 \n")
print("     -      UN TOTAL DE "+str(android_sh_2018+android_iot_2018)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY@ANDROID FUERON PUBLICADAS EN 2018 O ANTERIORMENTE \n")
print("\n")

print(" DE UN TOTAL DE "+str(bitdefender_sh+bitdefender_iot)+" VULNERABILIDADES PUBLICADAS DONDE EL ASIGNADOR DE CVE CVE-REQUESTS@BITDEFENDER, LAS ESTADÍSTICAS SEGÚN LA FECHA DE PUBLICACION SON : \n")
print("     -      UN TOTAL DE "+str(bitdefender_sh_2023+bitdefender_iot_2023)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE CVE-REQUESTS@BITDEFENDER FUERON PUBLICADAS EN 2023 \n")
print("     -      UN TOTAL DE "+str(bitdefender_sh_2022+bitdefender_iot_2022)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE CVE-REQUESTS@BITDEFENDER FUERON PUBLICADAS EN 2022 \n")
print("     -      UN TOTAL DE "+str(bitdefender_sh_2021+bitdefender_iot_2021)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE CVE-REQUESTS@BITDEFENDER FUERON PUBLICADAS EN 2021 \n")
print("     -      UN TOTAL DE "+str(bitdefender_sh_2020+bitdefender_iot_2020)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE CVE-REQUESTS@BITDEFENDER FUERON PUBLICADAS EN 2020 \n")
print("     -      UN TOTAL DE "+str(bitdefender_sh_2019+bitdefender_iot_2019)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE CVE-REQUESTS@BITDEFENDER FUERON PUBLICADAS EN 2019 \n")
print("     -      UN TOTAL DE "+str(bitdefender_sh_2018+bitdefender_iot_2018)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE CVE-REQUESTS@BITDEFENDER FUERON PUBLICADAS EN 2018 O ANTERIORMENTE \n")
print("\n")

print(" DE UN TOTAL DE "+str(mcafee_sh+mcafee_iot)+" VULNERABILIDADES PUBLICADAS DONDE EL ASIGNADOR DE CVE PSIRT@MCAFEE, LAS ESTADÍSTICAS SEGÚN LA FECHA DE PUBLICACION SON : \n")
print("     -      UN TOTAL DE "+str(mcafee_sh_2023+mcafee_iot_2023)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE PSIRT@MCAFEE FUERON PUBLICADAS EN 2023 \n")
print("     -      UN TOTAL DE "+str(mcafee_sh_2022+mcafee_iot_2022)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE PSIRT@MCAFEE FUERON PUBLICADAS EN 2022 \n")
print("     -      UN TOTAL DE "+str(mcafee_sh_2021+mcafee_iot_2021)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE PSIRT@MCAFEE FUERON PUBLICADAS EN 2021 \n")
print("     -      UN TOTAL DE "+str(mcafee_sh_2020+mcafee_iot_2020)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE PSIRT@MCAFEE FUERON PUBLICADAS EN 2020 \n")
print("     -      UN TOTAL DE "+str(mcafee_sh_2019+mcafee_iot_2019)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE PSIRT@MCAFEE FUERON PUBLICADAS EN 2019 \n")
print("     -      UN TOTAL DE "+str(mcafee_sh_2018+mcafee_iot_2018)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE PSIRT@MCAFEE FUERON PUBLICADAS EN 2018 O ANTERIORMENTE \n")
print("\n")


print(" DE UN TOTAL DE "+str(mozilla_sh+mozilla_iot)+" VULNERABILIDADES PUBLICADAS DONDE EL ASIGNADOR DE CVE ES SECURITY@MOZILLA, LAS ESTADÍSTICAS SEGÚN LA FECHA DE PUBLICACION SON : \n")
print("     -      UN TOTAL DE "+str(mozilla_sh_2023+mozilla_iot_2023)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY@MOZILLA FUERON PUBLICADAS EN 2023 \n")
print("     -      UN TOTAL DE "+str(mozilla_sh_2022+mozilla_iot_2022)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY@MOZILLA FUERON PUBLICADAS EN 2022 \n")
print("     -      UN TOTAL DE "+str(mozilla_sh_2021+mozilla_iot_2021)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY@MOZILLA FUERON PUBLICADAS EN 2021 \n")
print("     -      UN TOTAL DE "+str(mozilla_sh_2020+mozilla_iot_2020)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY@MOZILLA FUERON PUBLICADAS EN 2020 \n")
print("     -      UN TOTAL DE "+str(mozilla_sh_2019+mozilla_iot_2019)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY@MOZILLA FUERON PUBLICADAS EN 2019 \n")
print("     -      UN TOTAL DE "+str(mozilla_sh_2018+mozilla_iot_2018)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY@MOZILLA FUERON PUBLICADAS EN 2018 O ANTERIORMENTE \n")
print("\n")


print(" DE UN TOTAL DE "+str(hpe_sh+hpe_iot)+" VULNERABILIDADES PUBLICADAS DONDE EL ASIGNADOR DE CVE ES SECURITY-ALERT@HPE, LAS ESTADÍSTICAS SEGÚN LA FECHA DE PUBLICACION SON : \n")
print("     -      UN TOTAL DE "+str(hpe_sh_2023+hpe_iot_2023)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY-ALERT@HPE FUERON PUBLICADAS EN 2023 \n")
print("     -      UN TOTAL DE "+str(hpe_sh_2022+hpe_iot_2022)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY-ALERT@HPE FUERON PUBLICADAS EN 2022 \n")
print("     -      UN TOTAL DE "+str(hpe_sh_2021+hpe_iot_2021)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY-ALERT@HPE FUERON PUBLICADAS EN 2021 \n")
print("     -      UN TOTAL DE "+str(hpe_sh_2020+hpe_iot_2020)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY-ALERT@HPE FUERON PUBLICADAS EN 2020 \n")
print("     -      UN TOTAL DE "+str(hpe_sh_2019+hpe_iot_2019)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY-ALERT@HPE FUERON PUBLICADAS EN 2019 \n")
print("     -      UN TOTAL DE "+str(hpe_sh_2018+hpe_iot_2018)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY-ALERT@HPE FUERON PUBLICADAS EN 2018 O ANTERIORMENTE \n")
print("\n")


print(" DE UN TOTAL DE "+str(rapid7_sh+rapid7_iot)+" VULNERABILIDADES PUBLICADAS DONDE EL ASIGNADOR DE CVE ES CVE@RAPID7, LAS ESTADÍSTICAS SEGÚN LA FECHA DE PUBLICACION SON : \n")
print("     -      UN TOTAL DE "+str(rapid7_sh_2023+rapid7_iot_2023)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES CVE@RAPID7 FUERON PUBLICADAS EN 2023 \n")
print("     -      UN TOTAL DE "+str(rapid7_sh_2022+rapid7_iot_2022)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES CVE@RAPID7 FUERON PUBLICADAS EN 2022 \n")
print("     -      UN TOTAL DE "+str(rapid7_sh_2021+rapid7_iot_2021)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES CVE@RAPID7 FUERON PUBLICADAS EN 2021 \n")
print("     -      UN TOTAL DE "+str(rapid7_sh_2020+rapid7_iot_2020)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES CVE@RAPID7 FUERON PUBLICADAS EN 2020 \n")
print("     -      UN TOTAL DE "+str(rapid7_sh_2019+rapid7_iot_2019)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES CVE@RAPID7 FUERON PUBLICADAS EN 2019 \n")
print("     -      UN TOTAL DE "+str(rapid7_sh_2018+rapid7_iot_2018)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES CVE@RAPID7 FUERON PUBLICADAS EN 2018 O ANTERIORMENTE \n")
print("\n")



print(" DE UN TOTAL DE "+str(fsecure_sh+fsecure_iot)+" VULNERABILIDADES PUBLICADAS DONDE EL ASIGNADOR DE CVE ES CVE-NOTIFICATIONS-US@F-SECURE, LAS ESTADÍSTICAS SEGÚN LA FECHA DE PUBLICACION SON : \n")
print("     -      UN TOTAL DE "+str(fsecure_sh_2023+fsecure_iot_2023)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES CVE-NOTIFICATIONS-US@F-SECURE FUERON PUBLICADAS EN 2023 \n")
print("     -      UN TOTAL DE "+str(fsecure_sh_2022+fsecure_iot_2022)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES CVE-NOTIFICATIONS-US@F-SECURE FUERON PUBLICADAS EN 2022 \n")
print("     -      UN TOTAL DE "+str(fsecure_sh_2021+fsecure_iot_2021)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES CVE-NOTIFICATIONS-US@F-SECURE FUERON PUBLICADAS EN 2021 \n")
print("     -      UN TOTAL DE "+str(fsecure_sh_2020+fsecure_iot_2020)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES CVE-NOTIFICATIONS-US@F-SECURE FUERON PUBLICADAS EN 2020 \n")
print("     -      UN TOTAL DE "+str(fsecure_sh_2019+fsecure_iot_2019)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES CVE-NOTIFICATIONS-US@F-SECURE FUERON PUBLICADAS EN 2019 \n")
print("     -      UN TOTAL DE "+str(fsecure_sh_2018+fsecure_iot_2018)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES CVE-NOTIFICATIONS-US@F-SECURE FUERON PUBLICADAS EN 2018 O ANTERIORMENTE \n")
print("\n")



print(" DE UN TOTAL DE "+str(other_assigner_sh+other_assigner_iot)+" VULNERABILIDADES PUBLICADAS DONDE EL ASIGNADOR DE CVE ES OTRO DISTINTO A LOS ANTERIORES, LAS ESTADÍSTICAS SEGÚN LA FECHA DE PUBLICACION SON : \n")
print("     -      UN TOTAL DE "+str(other_assigner_sh_2023+other_assigner_iot_2023)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES OTRO DISTINTO A LOS ANTERIORES FUERON PUBLICADAS EN 2023 \n")
print("     -      UN TOTAL DE "+str(other_assigner_sh_2022+other_assigner_iot_2022)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES OTRO DISTINTO A LOS ANTERIORES FUERON PUBLICADAS EN 2022 \n")
print("     -      UN TOTAL DE "+str(other_assigner_sh_2021+other_assigner_iot_2021)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES OTRO DISTINTO A LOS ANTERIORES FUERON PUBLICADAS EN 2021 \n")
print("     -      UN TOTAL DE "+str(other_assigner_sh_2020+other_assigner_iot_2020)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES OTRO DISTINTO A LOS ANTERIORES FUERON PUBLICADAS EN 2020 \n")
print("     -      UN TOTAL DE "+str(other_assigner_sh_2019+other_assigner_iot_2019)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES OTRO DISTINTO A LOS ANTERIORES FUERON PUBLICADAS EN 2019 \n")
print("     -      UN TOTAL DE "+str(other_assigner_sh_2018+other_assigner_iot_2018)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES OTRO DISTINTO A LOS ANTERIORES FUERON PUBLICADAS EN 2018 O ANTERIORMENTE \n")
print("\n")






print("************************** PORCENTAJE FECHA DE PUBLICACION Y ASIGNADOR CVE PARTE IOT Y SMART HOME CONJUNTAS********************************")
print("\n")
print("\n")
print("\n")
print(" -  DE UN TOTAL DE "+str(total_assigner_sh+total_assigner_iot)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ESTÁ DEFINIDO, LOS PORCENTAJES DE ASSIGNER Y FECHA DE PUBLICACION SON LOS SIGUIENTES  : \n")
print("\n")
print("EN EL "+str(float((((assigner_sh_2023+assigner_iot_2023)*100)/(assigner_sh_2023+assigner_sh_2022+assigner_sh_2021+assigner_sh_2020+assigner_sh_2019+assigner_sh_2018+assigner_iot_2023+assigner_iot_2022+assigner_iot_2021+assigner_iot_2020+assigner_iot_2019+assigner_iot_2018))))+" % DE LAS VULNERABILIDADES PUBLICADAS EN EL 2023, LOS PORCENTAJES DE ASIGNADORES CVE SON LOS SIGUIENTES : \n")
print("     -      EN EL "+str(float((((jpcert_sh_2023+jpcert_iot_2023)*100)/(assigner_sh_2023+assigner_iot_2023))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES VULTURES@JPCERT\n")
print("     -      EN EL "+str(float((((mitre_sh_2023+mitre_iot_2023)*100)/(assigner_sh_2023+assigner_iot_2023))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES CVE@MITRE \n")
print("     -      EN EL "+str(float((((cisco_sh_2023+cisco_iot_2023)*100)/(assigner_sh_2023+assigner_iot_2023))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES TALOS-CNA@CISCO \n")
print("     -      EN EL "+str(float((((github_sh_2023+github_iot_2023)*100)/(assigner_sh_2023+assigner_iot_2023))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY-ADVISORIES@GITHUB \n")
print("     -      EN EL "+str(float((((redhat_sh_2023+redhat_iot_2023)*100)/(assigner_sh_2023+assigner_iot_2023))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES SECALERT@REDHAT\n")
print("     -      EN EL "+str(float((((qualcomm_sh_2023+qualcomm_iot_2023)*100)/(assigner_sh_2023+assigner_iot_2023))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY.CNA@QUALCOMM \n")
print("     -      EN EL "+str(float((((apache_sh_2023+apache_iot_2023)*100)/(assigner_sh_2023+assigner_iot_2023))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY@APACHE.ORG \n")
print("     -      EN EL "+str(float((((oracle_sh_2023+oracle_iot_2023)*100)/(assigner_sh_2023+assigner_iot_2023))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES SECALERT_US@ORACLE \n")
print("     -      EN EL "+str(float((((microsoft_sh_2023+microsoft_iot_2023)*100)/(assigner_sh_2023+assigner_iot_2023))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURE@MICROSOFT \n")
print("     -      EN EL "+str(float((((cert_sh_2023+cert_iot_2023)*100)/(assigner_sh_2023+assigner_iot_2023))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE INFO@CERT.VDE \n")
print("     -      EN EL "+str(float((((trendmicro_sh_2023+trendmicro_iot_2023)*100)/(assigner_sh_2023+assigner_iot_2023))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY@TRENDMICRO \n")
print("     -      EN EL "+str(float((((nozomi_sh_2023+nozomi_iot_2023)*100)/(assigner_sh_2023+assigner_iot_2023))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE PRODSEC@NOZOMINETWORKS \n")
print("     -      EN EL "+str(float((((hq_sh_2023+hq_iot_2023)*100)/(assigner_sh_2023+assigner_iot_2023))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES ICS-CERT@HQ.DHS.GOV \n")
print("     -      EN EL "+str(float((((kaspersky_sh_2023+kaspersky_iot_2023)*100)/(assigner_sh_2023+assigner_iot_2023))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES VULNERABILITY@KASPERSKY \n")
print("     -      EN EL "+str(float((((schneider_sh_2023+schneider_iot_2023)*100)/(assigner_sh_2023+assigner_iot_2023))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE CYBERSECURITY@SCHNEIDER-ELECTRIC \n")
print("     -      EN EL "+str(float((((apple_sh_2023+apple_iot_2023)*100)/(assigner_sh_2023+assigner_iot_2023))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE PRODUCT-SECURITY@APPLE \n")
print("     -      EN EL "+str(float((((android_sh_2023+android_iot_2023)*100)/(assigner_sh_2023+assigner_iot_2023))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY@ANDROID \n")
print("     -      EN EL "+str(float((((bitdefender_sh_2023+bitdefender_iot_2023)*100)/(assigner_sh_2023+assigner_iot_2023))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE CVE-REQUESTS@BITDEFENDER \n")
print("     -      EN EL "+str(float((((mcafee_sh_2023+mcafee_iot_2023)*100)/(assigner_sh_2023+assigner_iot_2023))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE PSIRT@MCAFEE \n")
print("     -      EN EL "+str(float((((mozilla_sh_2023+mozilla_iot_2023)*100)/(assigner_sh_2023+assigner_iot_2023))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY@MOZILLA \n")
print("     -      EN EL "+str(float((((hpe_sh_2023+hpe_iot_2023)*100)/(assigner_sh_2023+assigner_iot_2023))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY-ALERT@HPE \n")
print("     -      EN EL "+str(float((((fsecure_sh_2023+fsecure_iot_2023)*100)/(assigner_sh_2023+assigner_iot_2023))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES CVE-NOTIFICATIONS-US@F-SECURE \n")
print("     -      EN EL "+str(float((((rapid7_sh_2023+rapid7_iot_2023)*100)/(assigner_sh_2023+assigner_iot_2023))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES CVE@RAPID7 \n")
print("     -      EN EL "+str(float((((other_assigner_sh_2023+other_assigner_iot_2023)*100)/(assigner_sh_2023+assigner_iot_2023))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES DISTINTO A LOS ANTERIORES \n")
print("\n")



print("\n")
print("EN EL "+str(float((((assigner_sh_2022+assigner_iot_2022)*100)/(assigner_sh_2022+assigner_sh_2022+assigner_sh_2021+assigner_sh_2020+assigner_sh_2019+assigner_sh_2018+assigner_iot_2022+assigner_iot_2022+assigner_iot_2021+assigner_iot_2020+assigner_iot_2019+assigner_iot_2018))))+" % DE LAS VULNERABILIDADES PUBLICADAS EN EL 2022, LOS PORCENTAJES DE ASIGNADORES CVE SON LOS SIGUIENTES : \n")
print("     -      EN EL "+str(float((((jpcert_sh_2022+jpcert_iot_2022)*100)/(assigner_sh_2022+assigner_iot_2022))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES VULTURES@JPCERT\n")
print("     -      EN EL "+str(float((((mitre_sh_2022+mitre_iot_2022)*100)/(assigner_sh_2022+assigner_iot_2022))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES CVE@MITRE \n")
print("     -      EN EL "+str(float((((cisco_sh_2022+cisco_iot_2022)*100)/(assigner_sh_2022+assigner_iot_2022))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES TALOS-CNA@CISCO \n")
print("     -      EN EL "+str(float((((github_sh_2022+github_iot_2022)*100)/(assigner_sh_2022+assigner_iot_2022))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY-ADVISORIES@GITHUB \n")
print("     -      EN EL "+str(float((((redhat_sh_2022+redhat_iot_2022)*100)/(assigner_sh_2022+assigner_iot_2022))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES SECALERT@REDHAT\n")
print("     -      EN EL "+str(float((((qualcomm_sh_2022+qualcomm_iot_2022)*100)/(assigner_sh_2022+assigner_iot_2022))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY.CNA@QUALCOMM \n")
print("     -      EN EL "+str(float((((apache_sh_2022+apache_iot_2022)*100)/(assigner_sh_2022+assigner_iot_2022))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY@APACHE.ORG \n")
print("     -      EN EL "+str(float((((oracle_sh_2022+oracle_iot_2022)*100)/(assigner_sh_2022+assigner_iot_2022))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES SECALERT_US@ORACLE \n")
print("     -      EN EL "+str(float((((microsoft_sh_2022+microsoft_iot_2022)*100)/(assigner_sh_2022+assigner_iot_2022))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURE@MICROSOFT \n")
print("     -      EN EL "+str(float((((cert_sh_2022+cert_iot_2022)*100)/(assigner_sh_2022+assigner_iot_2022))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE INFO@CERT.VDE \n")
print("     -      EN EL "+str(float((((trendmicro_sh_2022+trendmicro_iot_2022)*100)/(assigner_sh_2022+assigner_iot_2022))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY@TRENDMICRO \n")
print("     -      EN EL "+str(float((((nozomi_sh_2022+nozomi_iot_2022)*100)/(assigner_sh_2022+assigner_iot_2022))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE PRODSEC@NOZOMINETWORKS \n")
print("     -      EN EL "+str(float((((hq_sh_2022+hq_iot_2022)*100)/(assigner_sh_2022+assigner_iot_2022))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES ICS-CERT@HQ.DHS.GOV \n")
print("     -      EN EL "+str(float((((kaspersky_sh_2022+kaspersky_iot_2022)*100)/(assigner_sh_2022+assigner_iot_2022))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES VULNERABILITY@KASPERSKY \n")
print("     -      EN EL "+str(float((((schneider_sh_2022+schneider_iot_2022)*100)/(assigner_sh_2022+assigner_iot_2022))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE CYBERSECURITY@SCHNEIDER-ELECTRIC \n")
print("     -      EN EL "+str(float((((apple_sh_2022+apple_iot_2022)*100)/(assigner_sh_2022+assigner_iot_2022))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE PRODUCT-SECURITY@APPLE \n")
print("     -      EN EL "+str(float((((android_sh_2022+android_iot_2022)*100)/(assigner_sh_2022+assigner_iot_2022))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY@ANDROID \n")
print("     -      EN EL "+str(float((((bitdefender_sh_2022+bitdefender_iot_2022)*100)/(assigner_sh_2022+assigner_iot_2022))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE CVE-REQUESTS@BITDEFENDER \n")
print("     -      EN EL "+str(float((((mcafee_sh_2022+mcafee_iot_2022)*100)/(assigner_sh_2022+assigner_iot_2022))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE PSIRT@MCAFEE \n")
print("     -      EN EL "+str(float((((mozilla_sh_2022+mozilla_iot_2022)*100)/(assigner_sh_2022+assigner_iot_2022))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY@MOZILLA \n")
print("     -      EN EL "+str(float((((hpe_sh_2022+hpe_iot_2022)*100)/(assigner_sh_2022+assigner_iot_2022))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY-ALERT@HPE \n")
print("     -      EN EL "+str(float((((fsecure_sh_2022+fsecure_iot_2022)*100)/(assigner_sh_2022+assigner_iot_2022))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES CVE-NOTIFICATIONS-US@F-SECURE \n")
print("     -      EN EL "+str(float((((rapid7_sh_2022+rapid7_iot_2022)*100)/(assigner_sh_2022+assigner_iot_2022))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES CVE@RAPID7 \n")
print("     -      EN EL "+str(float((((other_assigner_sh_2022+other_assigner_iot_2022)*100)/(assigner_sh_2022+assigner_iot_2022))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES DISTINTO A LOS ANTERIORES \n")
print("\n")



print("\n")
print("EN EL "+str(float((((assigner_sh_2021+assigner_iot_2021)*100)/(assigner_sh_2021+assigner_sh_2021+assigner_sh_2021+assigner_sh_2020+assigner_sh_2019+assigner_sh_2018+assigner_iot_2021+assigner_iot_2021+assigner_iot_2021+assigner_iot_2020+assigner_iot_2019+assigner_iot_2018))))+" % DE LAS VULNERABILIDADES PUBLICADAS EN EL 2021, LOS PORCENTAJES DE ASIGNADORES CVE SON LOS SIGUIENTES : \n")
print("     -      EN EL "+str(float((((jpcert_sh_2021+jpcert_iot_2021)*100)/(assigner_sh_2021+assigner_iot_2021))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES VULTURES@JPCERT\n")
print("     -      EN EL "+str(float((((mitre_sh_2021+mitre_iot_2021)*100)/(assigner_sh_2021+assigner_iot_2021))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES CVE@MITRE \n")
print("     -      EN EL "+str(float((((cisco_sh_2021+cisco_iot_2021)*100)/(assigner_sh_2021+assigner_iot_2021))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES TALOS-CNA@CISCO \n")
print("     -      EN EL "+str(float((((github_sh_2021+github_iot_2021)*100)/(assigner_sh_2021+assigner_iot_2021))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY-ADVISORIES@GITHUB \n")
print("     -      EN EL "+str(float((((redhat_sh_2021+redhat_iot_2021)*100)/(assigner_sh_2021+assigner_iot_2021))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES SECALERT@REDHAT\n")
print("     -      EN EL "+str(float((((qualcomm_sh_2021+qualcomm_iot_2021)*100)/(assigner_sh_2021+assigner_iot_2021))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY.CNA@QUALCOMM \n")
print("     -      EN EL "+str(float((((apache_sh_2021+apache_iot_2021)*100)/(assigner_sh_2021+assigner_iot_2021))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY@APACHE.ORG \n")
print("     -      EN EL "+str(float((((oracle_sh_2021+oracle_iot_2021)*100)/(assigner_sh_2021+assigner_iot_2021))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES SECALERT_US@ORACLE \n")
print("     -      EN EL "+str(float((((microsoft_sh_2021+microsoft_iot_2021)*100)/(assigner_sh_2021+assigner_iot_2021))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURE@MICROSOFT \n")
print("     -      EN EL "+str(float((((cert_sh_2021+cert_iot_2021)*100)/(assigner_sh_2021+assigner_iot_2021))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE INFO@CERT.VDE \n")
print("     -      EN EL "+str(float((((trendmicro_sh_2021+trendmicro_iot_2021)*100)/(assigner_sh_2021+assigner_iot_2021))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY@TRENDMICRO \n")
print("     -      EN EL "+str(float((((nozomi_sh_2021+nozomi_iot_2021)*100)/(assigner_sh_2021+assigner_iot_2021))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE PRODSEC@NOZOMINETWORKS \n")
print("     -      EN EL "+str(float((((hq_sh_2021+hq_iot_2021)*100)/(assigner_sh_2021+assigner_iot_2021))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES ICS-CERT@HQ.DHS.GOV \n")
print("     -      EN EL "+str(float((((kaspersky_sh_2021+kaspersky_iot_2021)*100)/(assigner_sh_2021+assigner_iot_2021))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES VULNERABILITY@KASPERSKY \n")
print("     -      EN EL "+str(float((((schneider_sh_2021+schneider_iot_2021)*100)/(assigner_sh_2021+assigner_iot_2021))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE CYBERSECURITY@SCHNEIDER-ELECTRIC \n")
print("     -      EN EL "+str(float((((apple_sh_2021+apple_iot_2021)*100)/(assigner_sh_2021+assigner_iot_2021))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE PRODUCT-SECURITY@APPLE \n")
print("     -      EN EL "+str(float((((android_sh_2021+android_iot_2021)*100)/(assigner_sh_2021+assigner_iot_2021))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY@ANDROID \n")
print("     -      EN EL "+str(float((((bitdefender_sh_2021+bitdefender_iot_2021)*100)/(assigner_sh_2021+assigner_iot_2021))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE CVE-REQUESTS@BITDEFENDER \n")
print("     -      EN EL "+str(float((((mcafee_sh_2021+mcafee_iot_2021)*100)/(assigner_sh_2021+assigner_iot_2021))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE PSIRT@MCAFEE \n")
print("     -      EN EL "+str(float((((mozilla_sh_2021+mozilla_iot_2021)*100)/(assigner_sh_2021+assigner_iot_2021))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY@MOZILLA \n")
print("     -      EN EL "+str(float((((hpe_sh_2021+hpe_iot_2021)*100)/(assigner_sh_2021+assigner_iot_2021))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY-ALERT@HPE \n")
print("     -      EN EL "+str(float((((fsecure_sh_2021+fsecure_iot_2021)*100)/(assigner_sh_2021+assigner_iot_2021))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES CVE-NOTIFICATIONS-US@F-SECURE \n")
print("     -      EN EL "+str(float((((rapid7_sh_2021+rapid7_iot_2021)*100)/(assigner_sh_2021+assigner_iot_2021))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES CVE@RAPID7 \n")
print("     -      EN EL "+str(float((((other_assigner_sh_2021+other_assigner_iot_2021)*100)/(assigner_sh_2021+assigner_iot_2021))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES DISTINTO A LOS ANTERIORES \n")
print("\n")



print("\n")
print("EN EL "+str(float((((assigner_sh_2020+assigner_iot_2020)*100)/(assigner_sh_2020+assigner_sh_2020+assigner_sh_2020+assigner_sh_2020+assigner_sh_2019+assigner_sh_2018+assigner_iot_2020+assigner_iot_2020+assigner_iot_2020+assigner_iot_2020+assigner_iot_2019+assigner_iot_2018))))+" % DE LAS VULNERABILIDADES PUBLICADAS EN EL 2020, LOS PORCENTAJES DE ASIGNADORES CVE SON LOS SIGUIENTES : \n")
print("     -      EN EL "+str(float((((jpcert_sh_2020+jpcert_iot_2020)*100)/(assigner_sh_2020+assigner_iot_2020))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES VULTURES@JPCERT\n")
print("     -      EN EL "+str(float((((mitre_sh_2020+mitre_iot_2020)*100)/(assigner_sh_2020+assigner_iot_2020))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES CVE@MITRE \n")
print("     -      EN EL "+str(float((((cisco_sh_2020+cisco_iot_2020)*100)/(assigner_sh_2020+assigner_iot_2020))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES TALOS-CNA@CISCO \n")
print("     -      EN EL "+str(float((((github_sh_2020+github_iot_2020)*100)/(assigner_sh_2020+assigner_iot_2020))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY-ADVISORIES@GITHUB \n")
print("     -      EN EL "+str(float((((redhat_sh_2020+redhat_iot_2020)*100)/(assigner_sh_2020+assigner_iot_2020))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES SECALERT@REDHAT\n")
print("     -      EN EL "+str(float((((qualcomm_sh_2020+qualcomm_iot_2020)*100)/(assigner_sh_2020+assigner_iot_2020))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY.CNA@QUALCOMM \n")
print("     -      EN EL "+str(float((((apache_sh_2020+apache_iot_2020)*100)/(assigner_sh_2020+assigner_iot_2020))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY@APACHE.ORG \n")
print("     -      EN EL "+str(float((((oracle_sh_2020+oracle_iot_2020)*100)/(assigner_sh_2020+assigner_iot_2020))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES SECALERT_US@ORACLE \n")
print("     -      EN EL "+str(float((((microsoft_sh_2020+microsoft_iot_2020)*100)/(assigner_sh_2020+assigner_iot_2020))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURE@MICROSOFT \n")
print("     -      EN EL "+str(float((((cert_sh_2020+cert_iot_2020)*100)/(assigner_sh_2020+assigner_iot_2020))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE INFO@CERT.VDE \n")
print("     -      EN EL "+str(float((((trendmicro_sh_2020+trendmicro_iot_2020)*100)/(assigner_sh_2020+assigner_iot_2020))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY@TRENDMICRO \n")
print("     -      EN EL "+str(float((((nozomi_sh_2020+nozomi_iot_2020)*100)/(assigner_sh_2020+assigner_iot_2020))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE PRODSEC@NOZOMINETWORKS \n")
print("     -      EN EL "+str(float((((hq_sh_2020+hq_iot_2020)*100)/(assigner_sh_2020+assigner_iot_2020))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES ICS-CERT@HQ.DHS.GOV \n")
print("     -      EN EL "+str(float((((kaspersky_sh_2020+kaspersky_iot_2020)*100)/(assigner_sh_2020+assigner_iot_2020))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES VULNERABILITY@KASPERSKY \n")
print("     -      EN EL "+str(float((((schneider_sh_2020+schneider_iot_2020)*100)/(assigner_sh_2020+assigner_iot_2020))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE CYBERSECURITY@SCHNEIDER-ELECTRIC \n")
print("     -      EN EL "+str(float((((apple_sh_2020+apple_iot_2020)*100)/(assigner_sh_2020+assigner_iot_2020))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE PRODUCT-SECURITY@APPLE \n")
print("     -      EN EL "+str(float((((android_sh_2020+android_iot_2020)*100)/(assigner_sh_2020+assigner_iot_2020))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY@ANDROID \n")
print("     -      EN EL "+str(float((((bitdefender_sh_2020+bitdefender_iot_2020)*100)/(assigner_sh_2020+assigner_iot_2020))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE CVE-REQUESTS@BITDEFENDER \n")
print("     -      EN EL "+str(float((((mcafee_sh_2020+mcafee_iot_2020)*100)/(assigner_sh_2020+assigner_iot_2020))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE PSIRT@MCAFEE \n")
print("     -      EN EL "+str(float((((mozilla_sh_2020+mozilla_iot_2020)*100)/(assigner_sh_2020+assigner_iot_2020))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY@MOZILLA \n")
print("     -      EN EL "+str(float((((hpe_sh_2020+hpe_iot_2020)*100)/(assigner_sh_2020+assigner_iot_2020))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY-ALERT@HPE \n")
print("     -      EN EL "+str(float((((fsecure_sh_2020+fsecure_iot_2020)*100)/(assigner_sh_2020+assigner_iot_2020))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES CVE-NOTIFICATIONS-US@F-SECURE \n")
print("     -      EN EL "+str(float((((rapid7_sh_2020+rapid7_iot_2020)*100)/(assigner_sh_2020+assigner_iot_2020))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES CVE@RAPID7 \n")
print("     -      EN EL "+str(float((((other_assigner_sh_2020+other_assigner_iot_2020)*100)/(assigner_sh_2020+assigner_iot_2020))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES DISTINTO A LOS ANTERIORES \n")
print("\n")



print("\n")
print("EN EL "+str(float((((assigner_sh_2019+assigner_iot_2019)*100)/(assigner_sh_2019+assigner_sh_2019+assigner_sh_2019+assigner_sh_2019+assigner_sh_2019+assigner_sh_2018+assigner_iot_2019+assigner_iot_2019+assigner_iot_2019+assigner_iot_2019+assigner_iot_2019+assigner_iot_2018))))+" % DE LAS VULNERABILIDADES PUBLICADAS EN EL 2019, LOS PORCENTAJES DE ASIGNADORES CVE SON LOS SIGUIENTES : \n")
print("     -      EN EL "+str(float((((jpcert_sh_2019+jpcert_iot_2019)*100)/(assigner_sh_2019+assigner_iot_2019))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES VULTURES@JPCERT\n")
print("     -      EN EL "+str(float((((mitre_sh_2019+mitre_iot_2019)*100)/(assigner_sh_2019+assigner_iot_2019))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES CVE@MITRE \n")
print("     -      EN EL "+str(float((((cisco_sh_2019+cisco_iot_2019)*100)/(assigner_sh_2019+assigner_iot_2019))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES TALOS-CNA@CISCO \n")
print("     -      EN EL "+str(float((((github_sh_2019+github_iot_2019)*100)/(assigner_sh_2019+assigner_iot_2019))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY-ADVISORIES@GITHUB \n")
print("     -      EN EL "+str(float((((redhat_sh_2019+redhat_iot_2019)*100)/(assigner_sh_2019+assigner_iot_2019))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES SECALERT@REDHAT\n")
print("     -      EN EL "+str(float((((qualcomm_sh_2019+qualcomm_iot_2019)*100)/(assigner_sh_2019+assigner_iot_2019))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY.CNA@QUALCOMM \n")
print("     -      EN EL "+str(float((((apache_sh_2019+apache_iot_2019)*100)/(assigner_sh_2019+assigner_iot_2019))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY@APACHE.ORG \n")
print("     -      EN EL "+str(float((((oracle_sh_2019+oracle_iot_2019)*100)/(assigner_sh_2019+assigner_iot_2019))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES SECALERT_US@ORACLE \n")
print("     -      EN EL "+str(float((((microsoft_sh_2019+microsoft_iot_2019)*100)/(assigner_sh_2019+assigner_iot_2019))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURE@MICROSOFT \n")
print("     -      EN EL "+str(float((((cert_sh_2019+cert_iot_2019)*100)/(assigner_sh_2019+assigner_iot_2019))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE INFO@CERT.VDE \n")
print("     -      EN EL "+str(float((((trendmicro_sh_2019+trendmicro_iot_2019)*100)/(assigner_sh_2019+assigner_iot_2019))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY@TRENDMICRO \n")
print("     -      EN EL "+str(float((((nozomi_sh_2019+nozomi_iot_2019)*100)/(assigner_sh_2019+assigner_iot_2019))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE PRODSEC@NOZOMINETWORKS \n")
print("     -      EN EL "+str(float((((hq_sh_2019+hq_iot_2019)*100)/(assigner_sh_2019+assigner_iot_2019))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES ICS-CERT@HQ.DHS.GOV \n")
print("     -      EN EL "+str(float((((kaspersky_sh_2019+kaspersky_iot_2019)*100)/(assigner_sh_2019+assigner_iot_2019))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES VULNERABILITY@KASPERSKY \n")
print("     -      EN EL "+str(float((((schneider_sh_2019+schneider_iot_2019)*100)/(assigner_sh_2019+assigner_iot_2019))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE CYBERSECURITY@SCHNEIDER-ELECTRIC \n")
print("     -      EN EL "+str(float((((apple_sh_2019+apple_iot_2019)*100)/(assigner_sh_2019+assigner_iot_2019))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE PRODUCT-SECURITY@APPLE \n")
print("     -      EN EL "+str(float((((android_sh_2019+android_iot_2019)*100)/(assigner_sh_2019+assigner_iot_2019))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY@ANDROID \n")
print("     -      EN EL "+str(float((((bitdefender_sh_2019+bitdefender_iot_2019)*100)/(assigner_sh_2019+assigner_iot_2019))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE CVE-REQUESTS@BITDEFENDER \n")
print("     -      EN EL "+str(float((((mcafee_sh_2019+mcafee_iot_2019)*100)/(assigner_sh_2019+assigner_iot_2019))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE PSIRT@MCAFEE \n")
print("     -      EN EL "+str(float((((mozilla_sh_2019+mozilla_iot_2019)*100)/(assigner_sh_2019+assigner_iot_2019))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY@MOZILLA \n")
print("     -      EN EL "+str(float((((hpe_sh_2019+hpe_iot_2019)*100)/(assigner_sh_2019+assigner_iot_2019))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY-ALERT@HPE \n")
print("     -      EN EL "+str(float((((fsecure_sh_2019+fsecure_iot_2019)*100)/(assigner_sh_2019+assigner_iot_2019))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES CVE-NOTIFICATIONS-US@F-SECURE \n")
print("     -      EN EL "+str(float((((rapid7_sh_2019+rapid7_iot_2019)*100)/(assigner_sh_2019+assigner_iot_2019))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES CVE@RAPID7 \n")
print("     -      EN EL "+str(float((((other_assigner_sh_2019+other_assigner_iot_2019)*100)/(assigner_sh_2019+assigner_iot_2019))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES DISTINTO A LOS ANTERIORES \n")
print("\n")



print("\n")
print("EN EL "+str(float((((assigner_sh_2018+assigner_iot_2018)*100)/(assigner_sh_2018+assigner_sh_2018+assigner_sh_2018+assigner_sh_2018+assigner_sh_2018+assigner_sh_2018+assigner_iot_2018+assigner_iot_2018+assigner_iot_2018+assigner_iot_2018+assigner_iot_2018+assigner_iot_2018))))+" % DE LAS VULNERABILIDADES PUBLICADAS EN EL 2018 O ANTERIORMENTE, LOS PORCENTAJES DE ASIGNADORES CVE SON LOS SIGUIENTES : \n")
print("     -      EN EL "+str(float((((jpcert_sh_2018+jpcert_iot_2018)*100)/(assigner_sh_2018+assigner_iot_2018))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES VULTURES@JPCERT\n")
print("     -      EN EL "+str(float((((mitre_sh_2018+mitre_iot_2018)*100)/(assigner_sh_2018+assigner_iot_2018))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES CVE@MITRE \n")
print("     -      EN EL "+str(float((((cisco_sh_2018+cisco_iot_2018)*100)/(assigner_sh_2018+assigner_iot_2018))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES TALOS-CNA@CISCO \n")
print("     -      EN EL "+str(float((((github_sh_2018+github_iot_2018)*100)/(assigner_sh_2018+assigner_iot_2018))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY-ADVISORIES@GITHUB \n")
print("     -      EN EL "+str(float((((redhat_sh_2018+redhat_iot_2018)*100)/(assigner_sh_2018+assigner_iot_2018))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES SECALERT@REDHAT\n")
print("     -      EN EL "+str(float((((qualcomm_sh_2018+qualcomm_iot_2018)*100)/(assigner_sh_2018+assigner_iot_2018))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY.CNA@QUALCOMM \n")
print("     -      EN EL "+str(float((((apache_sh_2018+apache_iot_2018)*100)/(assigner_sh_2018+assigner_iot_2018))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY@APACHE.ORG \n")
print("     -      EN EL "+str(float((((oracle_sh_2018+oracle_iot_2018)*100)/(assigner_sh_2018+assigner_iot_2018))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES SECALERT_US@ORACLE \n")
print("     -      EN EL "+str(float((((microsoft_sh_2018+microsoft_iot_2018)*100)/(assigner_sh_2018+assigner_iot_2018))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURE@MICROSOFT \n")
print("     -      EN EL "+str(float((((cert_sh_2018+cert_iot_2018)*100)/(assigner_sh_2018+assigner_iot_2018))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE INFO@CERT.VDE \n")
print("     -      EN EL "+str(float((((trendmicro_sh_2018+trendmicro_iot_2018)*100)/(assigner_sh_2018+assigner_iot_2018))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY@TRENDMICRO \n")
print("     -      EN EL "+str(float((((nozomi_sh_2018+nozomi_iot_2018)*100)/(assigner_sh_2018+assigner_iot_2018))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE PRODSEC@NOZOMINETWORKS \n")
print("     -      EN EL "+str(float((((hq_sh_2018+hq_iot_2018)*100)/(assigner_sh_2018+assigner_iot_2018))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES ICS-CERT@HQ.DHS.GOV \n")
print("     -      EN EL "+str(float((((kaspersky_sh_2018+kaspersky_iot_2018)*100)/(assigner_sh_2018+assigner_iot_2018))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES VULNERABILITY@KASPERSKY \n")
print("     -      EN EL "+str(float((((schneider_sh_2018+schneider_iot_2018)*100)/(assigner_sh_2018+assigner_iot_2018))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE CYBERSECURITY@SCHNEIDER-ELECTRIC \n")
print("     -      EN EL "+str(float((((apple_sh_2018+apple_iot_2018)*100)/(assigner_sh_2018+assigner_iot_2018))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE PRODUCT-SECURITY@APPLE \n")
print("     -      EN EL "+str(float((((android_sh_2018+android_iot_2018)*100)/(assigner_sh_2018+assigner_iot_2018))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY@ANDROID \n")
print("     -      EN EL "+str(float((((bitdefender_sh_2018+bitdefender_iot_2018)*100)/(assigner_sh_2018+assigner_iot_2018))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE CVE-REQUESTS@BITDEFENDER \n")
print("     -      EN EL "+str(float((((mcafee_sh_2018+mcafee_iot_2018)*100)/(assigner_sh_2018+assigner_iot_2018))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE PSIRT@MCAFEE \n")
print("     -      EN EL "+str(float((((mozilla_sh_2018+mozilla_iot_2018)*100)/(assigner_sh_2018+assigner_iot_2018))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY@MOZILLA \n")
print("     -      EN EL "+str(float((((hpe_sh_2018+hpe_iot_2018)*100)/(assigner_sh_2018+assigner_iot_2018))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES SECURITY-ALERT@HPE \n")
print("     -      EN EL "+str(float((((fsecure_sh_2018+fsecure_iot_2018)*100)/(assigner_sh_2018+assigner_iot_2018))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES CVE-NOTIFICATIONS-US@F-SECURE \n")
print("     -      EN EL "+str(float((((rapid7_sh_2018+rapid7_iot_2018)*100)/(assigner_sh_2018+assigner_iot_2018))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES CVE@RAPID7 \n")
print("     -      EN EL "+str(float((((other_assigner_sh_2018+other_assigner_iot_2018)*100)/(assigner_sh_2018+assigner_iot_2018))))+" % DE LAS VULNERABILIDADES EL ASIGNADOR DE CVE ES DISTINTO A LOS ANTERIORES \n")
print("\n")




print("************************** PORCENTAJE ASIGNADOR CVE SEGÚN FECHA DE PUBLICACIÓN PARTE IOT Y SMART HOME CONJUNTAS********************************")
print("\n")
print("\n")
print(" -  DE UN TOTAL DE "+str(total_assigner_sh+total_assigner_iot)+" VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ESTÁ DEFINIDO, LOS PORCENTAJES DE ASSIGNER SEGUN LA FECHA DE PUBLICACION SON LOS SIGUIENTES  : \n")
print("\n")
print("EN EL "+str(float((((jpcert_sh+jpcert_iot)*100)/(total_assigner_sh+total_assigner_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR ES VULTURES@JPCERT, LOS PORCENTAJES SEGUN FECHA DE PUBLICACION SON LOS SIGUIENTES : \n")
print("     -      EL "+str(float((((jpcert_sh_2023+jpcert_iot_2023)*100)/(jpcert_sh+jpcert_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES VULTURES@JPCERT, FUERON PUBLICADAS EN 2023 \n")
print("     -      EL "+str(float((((jpcert_sh_2022+jpcert_iot_2022)*100)/(jpcert_sh+jpcert_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES VULTURES@JPCERT, FUERON PUBLICADAS EN 2022 \n")
print("     -      EL "+str(float((((jpcert_sh_2021+jpcert_iot_2021)*100)/(jpcert_sh+jpcert_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES VULTURES@JPCERT, FUERON PUBLICADAS EN 2021 \n")
print("     -      EL "+str(float((((jpcert_sh_2020+jpcert_iot_2020)*100)/(jpcert_sh+jpcert_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES VULTURES@JPCERT, FUERON PUBLICADAS EN 2020 \n")
print("     -      EL "+str(float((((jpcert_sh_2019+jpcert_iot_2019)*100)/(jpcert_sh+jpcert_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES VULTURES@JPCERT, FUERON PUBLICADAS EN 2019 \n")
print("     -      EL "+str(float((((jpcert_sh_2018+jpcert_iot_2018)*100)/(jpcert_sh+jpcert_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES VULTURES@JPCERT, FUERON PUBLICADAS EN 2018 O ANTERIORMENTE \n")
print("\n")




print("\n")
print("EN EL "+str(float((((mitre_sh+mitre_iot)*100)/(total_assigner_sh+total_assigner_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR ES CVE@MITRE, LOS PORCENTAJES SEGUN FECHA DE PUBLICACION SON LOS SIGUIENTES : \n")
print("     -      EL "+str(float((((mitre_sh_2023+mitre_iot_2023)*100)/(mitre_sh+mitre_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES CVE@MITRE, FUERON PUBLICADAS EN 2023 \n")
print("     -      EL "+str(float((((mitre_sh_2022+mitre_iot_2022)*100)/(mitre_sh+mitre_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES CVE@MITRE, FUERON PUBLICADAS EN 2022 \n")
print("     -      EL "+str(float((((mitre_sh_2021+mitre_iot_2021)*100)/(mitre_sh+mitre_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES CVE@MITRE, FUERON PUBLICADAS EN 2021 \n")
print("     -      EL "+str(float((((mitre_sh_2020+mitre_iot_2020)*100)/(mitre_sh+mitre_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES CVE@MITRE, FUERON PUBLICADAS EN 2020 \n")
print("     -      EL "+str(float((((mitre_sh_2019+mitre_iot_2019)*100)/(mitre_sh+mitre_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES CVE@MITRE, FUERON PUBLICADAS EN 2019 \n")
print("     -      EL "+str(float((((mitre_sh_2018+mitre_iot_2018)*100)/(mitre_sh+mitre_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES CVE@MITRE, FUERON PUBLICADAS EN 2018 O ANTERIORMENTE \n")
print("\n")



print("\n")
print("EN EL "+str(float((((cisco_sh+cisco_iot)*100)/(total_assigner_sh+total_assigner_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR ES TALOS-CNA@CISCO, LOS PORCENTAJES SEGUN FECHA DE PUBLICACION SON LOS SIGUIENTES : \n")
print("     -      EL "+str(float((((cisco_sh_2023+cisco_iot_2023)*100)/(cisco_sh+cisco_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES TALOS-CNA@CISCO, FUERON PUBLICADAS EN 2023 \n")
print("     -      EL "+str(float((((cisco_sh_2022+cisco_iot_2022)*100)/(cisco_sh+cisco_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES TALOS-CNA@CISCO, FUERON PUBLICADAS EN 2022 \n")
print("     -      EL "+str(float((((cisco_sh_2021+cisco_iot_2021)*100)/(cisco_sh+cisco_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES TALOS-CNA@CISCO, FUERON PUBLICADAS EN 2021 \n")
print("     -      EL "+str(float((((cisco_sh_2020+cisco_iot_2020)*100)/(cisco_sh+cisco_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES TALOS-CNA@CISCO, FUERON PUBLICADAS EN 2020 \n")
print("     -      EL "+str(float((((cisco_sh_2019+cisco_iot_2019)*100)/(cisco_sh+cisco_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES TALOS-CNA@CISCO, FUERON PUBLICADAS EN 2019 \n")
print("     -      EL "+str(float((((cisco_sh_2018+cisco_iot_2018)*100)/(cisco_sh+cisco_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES TALOS-CNA@CISCO, FUERON PUBLICADAS EN 2018 O ANTERIORMENTE \n")
print("\n")




print("\n")
print("EN EL "+str(float((((github_sh+github_iot)*100)/(total_assigner_sh+total_assigner_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR ES SECURITY-ADVISORIES@GITHUB, LOS PORCENTAJES SEGUN FECHA DE PUBLICACION SON LOS SIGUIENTES : \n")
print("     -      EL "+str(float((((github_sh_2023+github_iot_2023)*100)/(github_sh+github_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY-ADVISORIES@GITHUB, FUERON PUBLICADAS EN 2023 \n")
print("     -      EL "+str(float((((github_sh_2022+github_iot_2022)*100)/(github_sh+github_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY-ADVISORIES@GITHUB, FUERON PUBLICADAS EN 2022 \n")
print("     -      EL "+str(float((((github_sh_2021+github_iot_2021)*100)/(github_sh+github_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY-ADVISORIES@GITHUB, FUERON PUBLICADAS EN 2021 \n")
print("     -      EL "+str(float((((github_sh_2020+github_iot_2020)*100)/(github_sh+github_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY-ADVISORIES@GITHUB, FUERON PUBLICADAS EN 2020 \n")
print("     -      EL "+str(float((((github_sh_2019+github_iot_2019)*100)/(github_sh+github_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY-ADVISORIES@GITHUB, FUERON PUBLICADAS EN 2019 \n")
print("     -      EL "+str(float((((github_sh_2018+github_iot_2018)*100)/(github_sh+github_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY-ADVISORIES@GITHUB, FUERON PUBLICADAS EN 2018 O ANTERIORMENTE \n")
print("\n")


if((redhat_sh+redhat_iot)>0):
    print("\n")
    print("EN EL "+str(float((((redhat_sh+redhat_iot)*100)/(total_assigner_sh+total_assigner_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR ES SECALERT@REDHAT, LOS PORCENTAJES SEGUN FECHA DE PUBLICACION SON LOS SIGUIENTES : \n")
    print("     -      EL "+str(float((((redhat_sh_2023+redhat_iot_2023)*100)/(redhat_sh+redhat_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECALERT@REDHAT, FUERON PUBLICADAS EN 2023 \n")
    print("     -      EL "+str(float((((redhat_sh_2022+redhat_iot_2022)*100)/(redhat_sh+redhat_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECALERT@REDHAT, FUERON PUBLICADAS EN 2022 \n")
    print("     -      EL "+str(float((((redhat_sh_2021+redhat_iot_2021)*100)/(redhat_sh+redhat_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECALERT@REDHAT, FUERON PUBLICADAS EN 2021 \n")
    print("     -      EL "+str(float((((redhat_sh_2020+redhat_iot_2020)*100)/(redhat_sh+redhat_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECALERT@REDHAT, FUERON PUBLICADAS EN 2020 \n")
    print("     -      EL "+str(float((((redhat_sh_2019+redhat_iot_2019)*100)/(redhat_sh+redhat_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECALERT@REDHAT, FUERON PUBLICADAS EN 2019 \n")
    print("     -      EL "+str(float((((redhat_sh_2018+redhat_iot_2018)*100)/(redhat_sh+redhat_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECALERT@REDHAT, FUERON PUBLICADAS EN 2018 O ANTERIORMENTE \n")
    print("\n")


if((qualcomm_sh+qualcomm_iot)>0):
    print("\n")
    print("EN EL "+str(float((((qualcomm_sh+qualcomm_iot)*100)/(total_assigner_sh+total_assigner_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR ES SECURITY.CNA@QUALCOMM, LOS PORCENTAJES SEGUN FECHA DE PUBLICACION SON LOS SIGUIENTES : \n")
    print("     -      EL "+str(float((((qualcomm_sh_2023+qualcomm_iot_2023)*100)/(qualcomm_sh+qualcomm_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY.CNA@QUALCOMM, FUERON PUBLICADAS EN 2023 \n")
    print("     -      EL "+str(float((((qualcomm_sh_2022+qualcomm_iot_2022)*100)/(qualcomm_sh+qualcomm_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY.CNA@QUALCOMM, FUERON PUBLICADAS EN 2022 \n")
    print("     -      EL "+str(float((((qualcomm_sh_2021+qualcomm_iot_2021)*100)/(qualcomm_sh+qualcomm_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY.CNA@QUALCOMM, FUERON PUBLICADAS EN 2021 \n")
    print("     -      EL "+str(float((((qualcomm_sh_2020+qualcomm_iot_2020)*100)/(qualcomm_sh+qualcomm_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY.CNA@QUALCOMM, FUERON PUBLICADAS EN 2020 \n")
    print("     -      EL "+str(float((((qualcomm_sh_2019+qualcomm_iot_2019)*100)/(qualcomm_sh+qualcomm_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY.CNA@QUALCOMM, FUERON PUBLICADAS EN 2019 \n")
    print("     -      EL "+str(float((((qualcomm_sh_2018+qualcomm_iot_2018)*100)/(qualcomm_sh+qualcomm_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY.CNA@QUALCOMM, FUERON PUBLICADAS EN 2018 O ANTERIORMENTE \n")
    print("\n")


if((apache_sh+apache_iot)>0):
    print("\n")
    print("EN EL "+str(float((((apache_sh+apache_iot)*100)/(total_assigner_sh+total_assigner_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR ES SECURITY@APACHE.ORG, LOS PORCENTAJES SEGUN FECHA DE PUBLICACION SON LOS SIGUIENTES : \n")
    print("     -      EL "+str(float((((apache_sh_2023+apache_iot_2023)*100)/(apache_sh+apache_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY@APACHE.ORG, FUERON PUBLICADAS EN 2023 \n")
    print("     -      EL "+str(float((((apache_sh_2022+apache_iot_2022)*100)/(apache_sh+apache_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY@APACHE.ORG, FUERON PUBLICADAS EN 2022 \n")
    print("     -      EL "+str(float((((apache_sh_2021+apache_iot_2021)*100)/(apache_sh+apache_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY@APACHE.ORG, FUERON PUBLICADAS EN 2021 \n")
    print("     -      EL "+str(float((((apache_sh_2020+apache_iot_2020)*100)/(apache_sh+apache_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY@APACHE.ORG, FUERON PUBLICADAS EN 2020 \n")
    print("     -      EL "+str(float((((apache_sh_2019+apache_iot_2019)*100)/(apache_sh+apache_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY@APACHE.ORG, FUERON PUBLICADAS EN 2019 \n")
    print("     -      EL "+str(float((((apache_sh_2018+apache_iot_2018)*100)/(apache_sh+apache_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY@APACHE.ORG, FUERON PUBLICADAS EN 2018 O ANTERIORMENTE \n")
    print("\n")


if((oracle_sh+oracle_iot)>0):
    print("\n")
    print("EN EL "+str(float((((oracle_sh+oracle_iot)*100)/(total_assigner_sh+total_assigner_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR ES SECALERT_US@ORACLE, LOS PORCENTAJES SEGUN FECHA DE PUBLICACION SON LOS SIGUIENTES : \n")
    print("     -      EL "+str(float((((oracle_sh_2023+oracle_iot_2023)*100)/(oracle_sh+oracle_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECALERT_US@ORACLE, FUERON PUBLICADAS EN 2023 \n")
    print("     -      EL "+str(float((((oracle_sh_2022+oracle_iot_2022)*100)/(oracle_sh+oracle_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECALERT_US@ORACLE, FUERON PUBLICADAS EN 2022 \n")
    print("     -      EL "+str(float((((oracle_sh_2021+oracle_iot_2021)*100)/(oracle_sh+oracle_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECALERT_US@ORACLE, FUERON PUBLICADAS EN 2021 \n")
    print("     -      EL "+str(float((((oracle_sh_2020+oracle_iot_2020)*100)/(oracle_sh+oracle_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECALERT_US@ORACLE, FUERON PUBLICADAS EN 2020 \n")
    print("     -      EL "+str(float((((oracle_sh_2019+oracle_iot_2019)*100)/(oracle_sh+oracle_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECALERT_US@ORACLE, FUERON PUBLICADAS EN 2019 \n")
    print("     -      EL "+str(float((((oracle_sh_2018+oracle_iot_2018)*100)/(oracle_sh+oracle_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECALERT_US@ORACLE, FUERON PUBLICADAS EN 2018 O ANTERIORMENTE \n")
    print("\n")


if((microsoft_sh+microsoft_iot)>0):
    print("\n")
    print("EN EL "+str(float((((microsoft_sh+microsoft_iot)*100)/(total_assigner_sh+total_assigner_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR ES SECURE@MICROSOFT, LOS PORCENTAJES SEGUN FECHA DE PUBLICACION SON LOS SIGUIENTES : \n")
    print("     -      EL "+str(float((((microsoft_sh_2023+microsoft_iot_2023)*100)/(microsoft_sh+microsoft_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURE@MICROSOFT, FUERON PUBLICADAS EN 2023 \n")
    print("     -      EL "+str(float((((microsoft_sh_2022+microsoft_iot_2022)*100)/(microsoft_sh+microsoft_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURE@MICROSOFT, FUERON PUBLICADAS EN 2022 \n")
    print("     -      EL "+str(float((((microsoft_sh_2021+microsoft_iot_2021)*100)/(microsoft_sh+microsoft_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURE@MICROSOFT, FUERON PUBLICADAS EN 2021 \n")
    print("     -      EL "+str(float((((microsoft_sh_2020+microsoft_iot_2020)*100)/(microsoft_sh+microsoft_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURE@MICROSOFT, FUERON PUBLICADAS EN 2020 \n")
    print("     -      EL "+str(float((((microsoft_sh_2019+microsoft_iot_2019)*100)/(microsoft_sh+microsoft_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURE@MICROSOFT, FUERON PUBLICADAS EN 2019 \n")
    print("     -      EL "+str(float((((microsoft_sh_2018+microsoft_iot_2018)*100)/(microsoft_sh+microsoft_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURE@MICROSOFT, FUERON PUBLICADAS EN 2018 O ANTERIORMENTE \n")
    print("\n")

if((cert_sh+cert_iot)>0):
    print("\n")
    print("EN EL "+str(float((((cert_sh+cert_iot)*100)/(total_assigner_sh+total_assigner_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR INFO@CERT.VDE, LOS PORCENTAJES SEGUN FECHA DE PUBLICACION SON LOS SIGUIENTES : \n")
    print("     -      EL "+str(float((((cert_sh_2023+cert_iot_2023)*100)/(cert_sh+cert_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE INFO@CERT.VDE, FUERON PUBLICADAS EN 2023 \n")
    print("     -      EL "+str(float((((cert_sh_2022+cert_iot_2022)*100)/(cert_sh+cert_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE INFO@CERT.VDE, FUERON PUBLICADAS EN 2022 \n")
    print("     -      EL "+str(float((((cert_sh_2021+cert_iot_2021)*100)/(cert_sh+cert_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE INFO@CERT.VDE, FUERON PUBLICADAS EN 2021 \n")
    print("     -      EL "+str(float((((cert_sh_2020+cert_iot_2020)*100)/(cert_sh+cert_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE INFO@CERT.VDE, FUERON PUBLICADAS EN 2020 \n")
    print("     -      EL "+str(float((((cert_sh_2019+cert_iot_2019)*100)/(cert_sh+cert_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE INFO@CERT.VDE, FUERON PUBLICADAS EN 2019 \n")
    print("     -      EL "+str(float((((cert_sh_2018+cert_iot_2018)*100)/(cert_sh+cert_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE INFO@CERT.VDE, FUERON PUBLICADAS EN 2018 O ANTERIORMENTE \n")
    print("\n")


if((trendmicro_sh+trendmicro_iot)>0):
    print("\n")
    print("EN EL "+str(float((((trendmicro_sh+trendmicro_iot)*100)/(total_assigner_sh+total_assigner_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR ES SECURITY@TRENDMICRO, LOS PORCENTAJES SEGUN FECHA DE PUBLICACION SON LOS SIGUIENTES : \n")
    print("     -      EL "+str(float((((trendmicro_sh_2023+trendmicro_iot_2023)*100)/(trendmicro_sh+trendmicro_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY@TRENDMICRO, FUERON PUBLICADAS EN 2023 \n")
    print("     -      EL "+str(float((((trendmicro_sh_2022+trendmicro_iot_2022)*100)/(trendmicro_sh+trendmicro_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY@TRENDMICRO, FUERON PUBLICADAS EN 2022 \n")
    print("     -      EL "+str(float((((trendmicro_sh_2021+trendmicro_iot_2021)*100)/(trendmicro_sh+trendmicro_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY@TRENDMICRO, FUERON PUBLICADAS EN 2021 \n")
    print("     -      EL "+str(float((((trendmicro_sh_2020+trendmicro_iot_2020)*100)/(trendmicro_sh+trendmicro_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY@TRENDMICRO, FUERON PUBLICADAS EN 2020 \n")
    print("     -      EL "+str(float((((trendmicro_sh_2019+trendmicro_iot_2019)*100)/(trendmicro_sh+trendmicro_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY@TRENDMICRO, FUERON PUBLICADAS EN 2019 \n")
    print("     -      EL "+str(float((((trendmicro_sh_2018+trendmicro_iot_2018)*100)/(trendmicro_sh+trendmicro_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY@TRENDMICRO, FUERON PUBLICADAS EN 2018 O ANTERIORMENTE \n")
    print("\n")

if((nozomi_sh+nozomi_iot)>0):
    print("\n")
    print("EN EL "+str(float((((nozomi_sh+nozomi_iot)*100)/(total_assigner_sh+total_assigner_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR PRODSEC@NOZOMINETWORKS, LOS PORCENTAJES SEGUN FECHA DE PUBLICACION SON LOS SIGUIENTES : \n")
    print("     -      EL "+str(float((((nozomi_sh_2023+nozomi_iot_2023)*100)/(nozomi_sh+nozomi_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE PRODSEC@NOZOMINETWORKS, FUERON PUBLICADAS EN 2023 \n")
    print("     -      EL "+str(float((((nozomi_sh_2022+nozomi_iot_2022)*100)/(nozomi_sh+nozomi_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE PRODSEC@NOZOMINETWORKS, FUERON PUBLICADAS EN 2022 \n")
    print("     -      EL "+str(float((((nozomi_sh_2021+nozomi_iot_2021)*100)/(nozomi_sh+nozomi_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE PRODSEC@NOZOMINETWORKS, FUERON PUBLICADAS EN 2021 \n")
    print("     -      EL "+str(float((((nozomi_sh_2020+nozomi_iot_2020)*100)/(nozomi_sh+nozomi_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE PRODSEC@NOZOMINETWORKS, FUERON PUBLICADAS EN 2020 \n")
    print("     -      EL "+str(float((((nozomi_sh_2019+nozomi_iot_2019)*100)/(nozomi_sh+nozomi_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE PRODSEC@NOZOMINETWORKS, FUERON PUBLICADAS EN 2019 \n")
    print("     -      EL "+str(float((((nozomi_sh_2018+nozomi_iot_2018)*100)/(nozomi_sh+nozomi_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE PRODSEC@NOZOMINETWORKS, FUERON PUBLICADAS EN 2018 O ANTERIORMENTE \n")
    print("\n")


if((hq_sh+hq_iot)>0):
    print("\n")
    print("EN EL "+str(float((((hq_sh+hq_iot)*100)/(total_assigner_sh+total_assigner_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR ES ICS-CERT@HQ.DHS.GOV, LOS PORCENTAJES SEGUN FECHA DE PUBLICACION SON LOS SIGUIENTES : \n")
    print("     -      EL "+str(float((((hq_sh_2023+hq_iot_2023)*100)/(hq_sh+hq_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES ICS-CERT@HQ.DHS.GOV, FUERON PUBLICADAS EN 2023 \n")
    print("     -      EL "+str(float((((hq_sh_2022+hq_iot_2022)*100)/(hq_sh+hq_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES ICS-CERT@HQ.DHS.GOV, FUERON PUBLICADAS EN 2022 \n")
    print("     -      EL "+str(float((((hq_sh_2021+hq_iot_2021)*100)/(hq_sh+hq_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES ICS-CERT@HQ.DHS.GOV, FUERON PUBLICADAS EN 2021 \n")
    print("     -      EL "+str(float((((hq_sh_2020+hq_iot_2020)*100)/(hq_sh+hq_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES ICS-CERT@HQ.DHS.GOV, FUERON PUBLICADAS EN 2020 \n")
    print("     -      EL "+str(float((((hq_sh_2019+hq_iot_2019)*100)/(hq_sh+hq_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES ICS-CERT@HQ.DHS.GOV, FUERON PUBLICADAS EN 2019 \n")
    print("     -      EL "+str(float((((hq_sh_2018+hq_iot_2018)*100)/(hq_sh+hq_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES ICS-CERT@HQ.DHS.GOV, FUERON PUBLICADAS EN 2018 O ANTERIORMENTE \n")
    print("\n")


if((kaspersky_sh+kaspersky_iot)>0):
    print("\n")
    print("EN EL "+str(float((((kaspersky_sh+kaspersky_iot)*100)/(total_assigner_sh+total_assigner_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR ES VULNERABILITY@KASPERSKY, LOS PORCENTAJES SEGUN FECHA DE PUBLICACION SON LOS SIGUIENTES : \n")
    print("     -      EL "+str(float((((kaspersky_sh_2023+kaspersky_iot_2023)*100)/(kaspersky_sh+kaspersky_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES VULNERABILITY@KASPERSKY, FUERON PUBLICADAS EN 2023 \n")
    print("     -      EL "+str(float((((kaspersky_sh_2022+kaspersky_iot_2022)*100)/(kaspersky_sh+kaspersky_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES VULNERABILITY@KASPERSKY, FUERON PUBLICADAS EN 2022 \n")
    print("     -      EL "+str(float((((kaspersky_sh_2021+kaspersky_iot_2021)*100)/(kaspersky_sh+kaspersky_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES VULNERABILITY@KASPERSKY, FUERON PUBLICADAS EN 2021 \n")
    print("     -      EL "+str(float((((kaspersky_sh_2020+kaspersky_iot_2020)*100)/(kaspersky_sh+kaspersky_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES VULNERABILITY@KASPERSKY, FUERON PUBLICADAS EN 2020 \n")
    print("     -      EL "+str(float((((kaspersky_sh_2019+kaspersky_iot_2019)*100)/(kaspersky_sh+kaspersky_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES VULNERABILITY@KASPERSKY, FUERON PUBLICADAS EN 2019 \n")
    print("     -      EL "+str(float((((kaspersky_sh_2018+kaspersky_iot_2018)*100)/(kaspersky_sh+kaspersky_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES VULNERABILITY@KASPERSKY, FUERON PUBLICADAS EN 2018 O ANTERIORMENTE \n")
    print("\n")


if((schneider_sh+schneider_iot)>0):
    print("\n")
    print("EN EL "+str(float((((schneider_sh+schneider_iot)*100)/(total_assigner_sh+total_assigner_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR CYBERSECURITY@SCHNEIDER-ELECTRIC, LOS PORCENTAJES SEGUN FECHA DE PUBLICACION SON LOS SIGUIENTES : \n")
    print("     -      EL "+str(float((((schneider_sh_2023+schneider_iot_2023)*100)/(schneider_sh+schneider_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE CYBERSECURITY@SCHNEIDER-ELECTRIC, FUERON PUBLICADAS EN 2023 \n")
    print("     -      EL "+str(float((((schneider_sh_2022+schneider_iot_2022)*100)/(schneider_sh+schneider_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE CYBERSECURITY@SCHNEIDER-ELECTRIC, FUERON PUBLICADAS EN 2022 \n")
    print("     -      EL "+str(float((((schneider_sh_2021+schneider_iot_2021)*100)/(schneider_sh+schneider_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE CYBERSECURITY@SCHNEIDER-ELECTRIC, FUERON PUBLICADAS EN 2021 \n")
    print("     -      EL "+str(float((((schneider_sh_2020+schneider_iot_2020)*100)/(schneider_sh+schneider_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE CYBERSECURITY@SCHNEIDER-ELECTRIC, FUERON PUBLICADAS EN 2020 \n")
    print("     -      EL "+str(float((((schneider_sh_2019+schneider_iot_2019)*100)/(schneider_sh+schneider_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE CYBERSECURITY@SCHNEIDER-ELECTRIC, FUERON PUBLICADAS EN 2019 \n")
    print("     -      EL "+str(float((((schneider_sh_2018+schneider_iot_2018)*100)/(schneider_sh+schneider_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE CYBERSECURITY@SCHNEIDER-ELECTRIC, FUERON PUBLICADAS EN 2018 O ANTERIORMENTE \n")
    print("\n")

if((apple_sh+apple_iot)>0):
    print("\n")
    print("EN EL "+str(float((((apple_sh+apple_iot)*100)/(total_assigner_sh+total_assigner_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR PRODUCT-SECURITY@APPLE, LOS PORCENTAJES SEGUN FECHA DE PUBLICACION SON LOS SIGUIENTES : \n")
    print("     -      EL "+str(float((((apple_sh_2023+apple_iot_2023)*100)/(apple_sh+apple_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE PRODUCT-SECURITY@APPLE, FUERON PUBLICADAS EN 2023 \n")
    print("     -      EL "+str(float((((apple_sh_2022+apple_iot_2022)*100)/(apple_sh+apple_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE PRODUCT-SECURITY@APPLE, FUERON PUBLICADAS EN 2022 \n")
    print("     -      EL "+str(float((((apple_sh_2021+apple_iot_2021)*100)/(apple_sh+apple_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE PRODUCT-SECURITY@APPLE, FUERON PUBLICADAS EN 2021 \n")
    print("     -      EL "+str(float((((apple_sh_2020+apple_iot_2020)*100)/(apple_sh+apple_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE PRODUCT-SECURITY@APPLE, FUERON PUBLICADAS EN 2020 \n")
    print("     -      EL "+str(float((((apple_sh_2019+apple_iot_2019)*100)/(apple_sh+apple_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE PRODUCT-SECURITY@APPLE, FUERON PUBLICADAS EN 2019 \n")
    print("     -      EL "+str(float((((apple_sh_2018+apple_iot_2018)*100)/(apple_sh+apple_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE PRODUCT-SECURITY@APPLE, FUERON PUBLICADAS EN 2018 O ANTERIORMENTE \n")
    print("\n")

if((android_sh+android_iot)>0):

    print("\n")
    print("EN EL "+str(float((((android_sh+android_iot)*100)/(total_assigner_sh+total_assigner_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR ES SECURITY@ANDROID, LOS PORCENTAJES SEGUN FECHA DE PUBLICACION SON LOS SIGUIENTES : \n")
    print("     -      EL "+str(float((((android_sh_2023+android_iot_2023)*100)/(android_sh+android_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY@ANDROID, FUERON PUBLICADAS EN 2023 \n")
    print("     -      EL "+str(float((((android_sh_2022+android_iot_2022)*100)/(android_sh+android_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY@ANDROID, FUERON PUBLICADAS EN 2022 \n")
    print("     -      EL "+str(float((((android_sh_2021+android_iot_2021)*100)/(android_sh+android_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY@ANDROID, FUERON PUBLICADAS EN 2021 \n")
    print("     -      EL "+str(float((((android_sh_2020+android_iot_2020)*100)/(android_sh+android_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY@ANDROID, FUERON PUBLICADAS EN 2020 \n")
    print("     -      EL "+str(float((((android_sh_2019+android_iot_2019)*100)/(android_sh+android_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY@ANDROID, FUERON PUBLICADAS EN 2019 \n")
    print("     -      EL "+str(float((((android_sh_2018+android_iot_2018)*100)/(android_sh+android_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY@ANDROID, FUERON PUBLICADAS EN 2018 O ANTERIORMENTE \n")
    print("\n")


if((bitdefender_sh+bitdefender_iot)>0):
    print("\n")
    print("EN EL "+str(float((((bitdefender_sh+bitdefender_iot)*100)/(total_assigner_sh+total_assigner_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR CVE-REQUESTS@BITDEFENDER, LOS PORCENTAJES SEGUN FECHA DE PUBLICACION SON LOS SIGUIENTES : \n")
    print("     -      EL "+str(float((((bitdefender_sh_2023+bitdefender_iot_2023)*100)/(bitdefender_sh+bitdefender_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE CVE-REQUESTS@BITDEFENDER, FUERON PUBLICADAS EN 2023 \n")
    print("     -      EL "+str(float((((bitdefender_sh_2022+bitdefender_iot_2022)*100)/(bitdefender_sh+bitdefender_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE CVE-REQUESTS@BITDEFENDER, FUERON PUBLICADAS EN 2022 \n")
    print("     -      EL "+str(float((((bitdefender_sh_2021+bitdefender_iot_2021)*100)/(bitdefender_sh+bitdefender_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE CVE-REQUESTS@BITDEFENDER, FUERON PUBLICADAS EN 2021 \n")
    print("     -      EL "+str(float((((bitdefender_sh_2020+bitdefender_iot_2020)*100)/(bitdefender_sh+bitdefender_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE CVE-REQUESTS@BITDEFENDER, FUERON PUBLICADAS EN 2020 \n")
    print("     -      EL "+str(float((((bitdefender_sh_2019+bitdefender_iot_2019)*100)/(bitdefender_sh+bitdefender_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE CVE-REQUESTS@BITDEFENDER, FUERON PUBLICADAS EN 2019 \n")
    print("     -      EL "+str(float((((bitdefender_sh_2018+bitdefender_iot_2018)*100)/(bitdefender_sh+bitdefender_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE CVE-REQUESTS@BITDEFENDER, FUERON PUBLICADAS EN 2018 O ANTERIORMENTE \n")
    print("\n")


if((mcafee_sh+mcafee_iot)>0):
    print("\n")
    print("EN EL "+str(float((((mcafee_sh+mcafee_iot)*100)/(total_assigner_sh+total_assigner_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR PSIRT@MCAFEE, LOS PORCENTAJES SEGUN FECHA DE PUBLICACION SON LOS SIGUIENTES : \n")
    print("     -      EL "+str(float((((mcafee_sh_2023+mcafee_iot_2023)*100)/(mcafee_sh+mcafee_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE PSIRT@MCAFEE, FUERON PUBLICADAS EN 2023 \n")
    print("     -      EL "+str(float((((mcafee_sh_2022+mcafee_iot_2022)*100)/(mcafee_sh+mcafee_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE PSIRT@MCAFEE, FUERON PUBLICADAS EN 2022 \n")
    print("     -      EL "+str(float((((mcafee_sh_2021+mcafee_iot_2021)*100)/(mcafee_sh+mcafee_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE PSIRT@MCAFEE, FUERON PUBLICADAS EN 2021 \n")
    print("     -      EL "+str(float((((mcafee_sh_2020+mcafee_iot_2020)*100)/(mcafee_sh+mcafee_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE PSIRT@MCAFEE, FUERON PUBLICADAS EN 2020 \n")
    print("     -      EL "+str(float((((mcafee_sh_2019+mcafee_iot_2019)*100)/(mcafee_sh+mcafee_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE PSIRT@MCAFEE, FUERON PUBLICADAS EN 2019 \n")
    print("     -      EL "+str(float((((mcafee_sh_2018+mcafee_iot_2018)*100)/(mcafee_sh+mcafee_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE PSIRT@MCAFEE, FUERON PUBLICADAS EN 2018 O ANTERIORMENTE \n")
    print("\n")


if((mozilla_sh+mozilla_iot)>0):
    print("\n")
    print("EN EL "+str(float((((mozilla_sh+mozilla_iot)*100)/(total_assigner_sh+total_assigner_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR ES SECURITY@MOZILLA, LOS PORCENTAJES SEGUN FECHA DE PUBLICACION SON LOS SIGUIENTES : \n")
    print("     -      EL "+str(float((((mozilla_sh_2023+mozilla_iot_2023)*100)/(mozilla_sh+mozilla_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY@MOZILLA, FUERON PUBLICADAS EN 2023 \n")
    print("     -      EL "+str(float((((mozilla_sh_2022+mozilla_iot_2022)*100)/(mozilla_sh+mozilla_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY@MOZILLA, FUERON PUBLICADAS EN 2022 \n")
    print("     -      EL "+str(float((((mozilla_sh_2021+mozilla_iot_2021)*100)/(mozilla_sh+mozilla_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY@MOZILLA, FUERON PUBLICADAS EN 2021 \n")
    print("     -      EL "+str(float((((mozilla_sh_2020+mozilla_iot_2020)*100)/(mozilla_sh+mozilla_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY@MOZILLA, FUERON PUBLICADAS EN 2020 \n")
    print("     -      EL "+str(float((((mozilla_sh_2019+mozilla_iot_2019)*100)/(mozilla_sh+mozilla_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY@MOZILLA, FUERON PUBLICADAS EN 2019 \n")
    print("     -      EL "+str(float((((mozilla_sh_2018+mozilla_iot_2018)*100)/(mozilla_sh+mozilla_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY@MOZILLA, FUERON PUBLICADAS EN 2018 O ANTERIORMENTE \n")
    print("\n")

if((hpe_sh+hpe_iot)>0):
    print("\n")
    print("EN EL "+str(float((((hpe_sh+hpe_iot)*100)/(total_assigner_sh+total_assigner_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR ES SECURITY-ALERT@HPE, LOS PORCENTAJES SEGUN FECHA DE PUBLICACION SON LOS SIGUIENTES : \n")
    print("     -      EL "+str(float((((hpe_sh_2023+hpe_iot_2023)*100)/(hpe_sh+hpe_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY-ALERT@HPE, FUERON PUBLICADAS EN 2023 \n")
    print("     -      EL "+str(float((((hpe_sh_2022+hpe_iot_2022)*100)/(hpe_sh+hpe_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY-ALERT@HPE, FUERON PUBLICADAS EN 2022 \n")
    print("     -      EL "+str(float((((hpe_sh_2021+hpe_iot_2021)*100)/(hpe_sh+hpe_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY-ALERT@HPE, FUERON PUBLICADAS EN 2021 \n")
    print("     -      EL "+str(float((((hpe_sh_2020+hpe_iot_2020)*100)/(hpe_sh+hpe_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY-ALERT@HPE, FUERON PUBLICADAS EN 2020 \n")
    print("     -      EL "+str(float((((hpe_sh_2019+hpe_iot_2019)*100)/(hpe_sh+hpe_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY-ALERT@HPE, FUERON PUBLICADAS EN 2019 \n")
    print("     -      EL "+str(float((((hpe_sh_2018+hpe_iot_2018)*100)/(hpe_sh+hpe_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES SECURITY-ALERT@HPE, FUERON PUBLICADAS EN 2018 O ANTERIORMENTE \n")
    print("\n")



if((fsecure_sh+fsecure_iot)>0):
    print("\n")
    print("EN EL "+str(float((((fsecure_sh+fsecure_iot)*100)/(total_assigner_sh+total_assigner_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR ES CVE-NOTIFICATIONS-US@F-SECURE, LOS PORCENTAJES SEGUN FECHA DE PUBLICACION SON LOS SIGUIENTES : \n")
    print("     -      EL "+str(float((((fsecure_sh_2023+fsecure_iot_2023)*100)/(fsecure_sh+fsecure_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES CVE-NOTIFICATIONS-US@F-SECURE, FUERON PUBLICADAS EN 2023 \n")
    print("     -      EL "+str(float((((fsecure_sh_2022+fsecure_iot_2022)*100)/(fsecure_sh+fsecure_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES CVE-NOTIFICATIONS-US@F-SECURE, FUERON PUBLICADAS EN 2022 \n")
    print("     -      EL "+str(float((((fsecure_sh_2021+fsecure_iot_2021)*100)/(fsecure_sh+fsecure_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES CVE-NOTIFICATIONS-US@F-SECURE, FUERON PUBLICADAS EN 2021 \n")
    print("     -      EL "+str(float((((fsecure_sh_2020+fsecure_iot_2020)*100)/(fsecure_sh+fsecure_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES CVE-NOTIFICATIONS-US@F-SECURE, FUERON PUBLICADAS EN 2020 \n")
    print("     -      EL "+str(float((((fsecure_sh_2019+fsecure_iot_2019)*100)/(fsecure_sh+fsecure_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES CVE-NOTIFICATIONS-US@F-SECURE, FUERON PUBLICADAS EN 2019 \n")
    print("     -      EL "+str(float((((fsecure_sh_2018+fsecure_iot_2018)*100)/(fsecure_sh+fsecure_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES CVE-NOTIFICATIONS-US@F-SECURE, FUERON PUBLICADAS EN 2018 O ANTERIORMENTE \n")
    print("\n")


if((rapid7_sh+rapid7_iot)>0):
    print("\n")
    print("EN EL "+str(float((((rapid7_sh+rapid7_iot)*100)/(total_assigner_sh+total_assigner_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR ES CVE@RAPID7, LOS PORCENTAJES SEGUN FECHA DE PUBLICACION SON LOS SIGUIENTES : \n")
    print("     -      EL "+str(float((((rapid7_sh_2023+rapid7_iot_2023)*100)/(rapid7_sh+rapid7_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES CVE@RAPID7, FUERON PUBLICADAS EN 2023 \n")
    print("     -      EL "+str(float((((rapid7_sh_2022+rapid7_iot_2022)*100)/(rapid7_sh+rapid7_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES CVE@RAPID7, FUERON PUBLICADAS EN 2022 \n")
    print("     -      EL "+str(float((((rapid7_sh_2021+rapid7_iot_2021)*100)/(rapid7_sh+rapid7_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES CVE@RAPID7, FUERON PUBLICADAS EN 2021 \n")
    print("     -      EL "+str(float((((rapid7_sh_2020+rapid7_iot_2020)*100)/(rapid7_sh+rapid7_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES CVE@RAPID7, FUERON PUBLICADAS EN 2020 \n")
    print("     -      EL "+str(float((((rapid7_sh_2019+rapid7_iot_2019)*100)/(rapid7_sh+rapid7_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES CVE@RAPID7, FUERON PUBLICADAS EN 2019 \n")
    print("     -      EL "+str(float((((rapid7_sh_2018+rapid7_iot_2018)*100)/(rapid7_sh+rapid7_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES CVE@RAPID7, FUERON PUBLICADAS EN 2018 O ANTERIORMENTE \n")
    print("\n")

if((other_assigner_sh+other_assigner_iot)>0):

    print("\n")
    print("EN EL "+str(float((((other_assigner_sh+other_assigner_iot)*100)/(total_assigner_sh+total_assigner_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR ES OTRO DISTINTO A LOS ANTERIORES, LOS PORCENTAJES SEGUN FECHA DE PUBLICACION SON LOS SIGUIENTES : \n")
    print("     -      EL "+str(float((((other_assigner_sh_2023+other_assigner_iot_2023)*100)/(other_assigner_sh+other_assigner_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES OTRO DISTINTO A LOS ANTERIORES, FUERON PUBLICADAS EN 2023 \n")
    print("     -      EL "+str(float((((other_assigner_sh_2022+other_assigner_iot_2022)*100)/(other_assigner_sh+other_assigner_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES OTRO DISTINTO A LOS ANTERIORES, FUERON PUBLICADAS EN 2022 \n")
    print("     -      EL "+str(float((((other_assigner_sh_2021+other_assigner_iot_2021)*100)/(other_assigner_sh+other_assigner_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES OTRO DISTINTO A LOS ANTERIORES, FUERON PUBLICADAS EN 2021 \n")
    print("     -      EL "+str(float((((other_assigner_sh_2020+other_assigner_iot_2020)*100)/(other_assigner_sh+other_assigner_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES OTRO DISTINTO A LOS ANTERIORES, FUERON PUBLICADAS EN 2020 \n")
    print("     -      EL "+str(float((((other_assigner_sh_2019+other_assigner_iot_2019)*100)/(other_assigner_sh+other_assigner_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES OTRO DISTINTO A LOS ANTERIORES, FUERON PUBLICADAS EN 2019 \n")
    print("     -      EL "+str(float((((other_assigner_sh_2018+other_assigner_iot_2018)*100)/(other_assigner_sh+other_assigner_iot))))+" % DE LAS VULNERABILIDADES DONDE EL ASIGNADOR DE CVE ES OTRO DISTINTO A LOS ANTERIORES, FUERON PUBLICADAS EN 2018 O ANTERIORMENTE \n")
    print("\n")

















































































































































