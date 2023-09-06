



import pandas as pd

#Abro los ficheros con los que voy a tratar

df_cve_iot=pd.read_excel('cves_iot_2023.xlsx')
df_cve_sh=pd.read_excel('cves_smart_home_2023.xlsx')



#Variables donde almacenare el contador de PUNTUACION BASE CVE CVSS3  y la fecha de publicacion de la vulnerabilidad para IOT

CV3_BASE_score_9_iot=0
count_lastpublidate_2023_cve_iot_score9=0
count_lastpublidate_2022_cve_iot_score9=0
count_lastpublidate_2021_cve_iot_score9=0
count_lastpublidate_2020_cve_iot_score9=0
count_lastpublidate_2019_cve_iot_score9=0
count_lastpublidate_2018_cve_iot_score9=0
CV3_BASE_score_8_iot=0
count_lastpublidate_2023_cve_iot_score8=0
count_lastpublidate_2022_cve_iot_score8=0
count_lastpublidate_2021_cve_iot_score8=0
count_lastpublidate_2020_cve_iot_score8=0
count_lastpublidate_2019_cve_iot_score8=0
count_lastpublidate_2018_cve_iot_score8=0
CV3_BASE_score_7_iot=0
count_lastpublidate_2023_cve_iot_score7=0
count_lastpublidate_2022_cve_iot_score7=0
count_lastpublidate_2021_cve_iot_score7=0
count_lastpublidate_2020_cve_iot_score7=0
count_lastpublidate_2019_cve_iot_score7=0
count_lastpublidate_2018_cve_iot_score7=0
CV3_BASE_score_6_iot=0
count_lastpublidate_2023_cve_iot_score6=0
count_lastpublidate_2022_cve_iot_score6=0
count_lastpublidate_2021_cve_iot_score6=0
count_lastpublidate_2020_cve_iot_score6=0
count_lastpublidate_2019_cve_iot_score6=0
count_lastpublidate_2018_cve_iot_score6=0
CV3_BASE_score_5_iot=0
count_lastpublidate_2023_cve_iot_score5=0
count_lastpublidate_2022_cve_iot_score5=0
count_lastpublidate_2021_cve_iot_score5=0
count_lastpublidate_2020_cve_iot_score5=0
count_lastpublidate_2019_cve_iot_score5=0
count_lastpublidate_2018_cve_iot_score5=0
CV3_BASE_score_4_iot=0
count_lastpublidate_2023_cve_iot_score4=0
count_lastpublidate_2022_cve_iot_score4=0
count_lastpublidate_2021_cve_iot_score4=0
count_lastpublidate_2020_cve_iot_score4=0
count_lastpublidate_2019_cve_iot_score4=0
count_lastpublidate_2018_cve_iot_score4=0
CV3_BASE_score_3_iot=0
count_lastpublidate_2023_cve_iot_score3=0
count_lastpublidate_2022_cve_iot_score3=0
count_lastpublidate_2021_cve_iot_score3=0
count_lastpublidate_2020_cve_iot_score3=0
count_lastpublidate_2019_cve_iot_score3=0
count_lastpublidate_2018_cve_iot_score3=0
CV3_BASE_score_2_iot=0
count_lastpublidate_2023_cve_iot_score2=0
count_lastpublidate_2022_cve_iot_score2=0
count_lastpublidate_2021_cve_iot_score2=0
count_lastpublidate_2020_cve_iot_score2=0
count_lastpublidate_2019_cve_iot_score2=0
count_lastpublidate_2018_cve_iot_score2=0
CV3_BASE_score_1_iot=0
count_lastpublidate_2023_cve_iot_score1=0
count_lastpublidate_2022_cve_iot_score1=0
count_lastpublidate_2021_cve_iot_score1=0
count_lastpublidate_2020_cve_iot_score1=0
count_lastpublidate_2019_cve_iot_score1=0
count_lastpublidate_2018_cve_iot_score1=0
CV3_BASE_score_0_iot=0
count_lastpublidate_2023_cve_iot_score0=0
count_lastpublidate_2022_cve_iot_score0=0
count_lastpublidate_2021_cve_iot_score0=0
count_lastpublidate_2020_cve_iot_score0=0
count_lastpublidate_2019_cve_iot_score0=0
count_lastpublidate_2018_cve_iot_score0=0
CV3_BASE_score_10_iot=0
count_lastpublidate_2023_cve_iot_score10=0
count_lastpublidate_2022_cve_iot_score10=0
count_lastpublidate_2021_cve_iot_score10=0
count_lastpublidate_2020_cve_iot_score10=0
count_lastpublidate_2019_cve_iot_score10=0
count_lastpublidate_2018_cve_iot_score10=0


#Compruebo la PUNTUACION BASE CVE CVSS3 y despues el anio de PUBLICACION para IOT

for j in range(0,len(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"])):
    if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"][j]!="NONE"):
        if(((float(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"][j])) < 10.0) and ((float(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"][j])) >=9.0)):
            CV3_BASE_score_9_iot+=1
            str_anio_publidate_cve_iot=df_cve_iot["CVE_Items.publishedDate"][j].split("-")
            anio_publidate_cve_iot=int(str_anio_publidate_cve_iot[0])
            if(anio_publidate_cve_iot >= 2023):
                count_lastpublidate_2023_cve_iot_score9+=1
            elif(anio_publidate_cve_iot >= 2022):
                count_lastpublidate_2022_cve_iot_score9+=1
            elif(anio_publidate_cve_iot >= 2021):
                count_lastpublidate_2021_cve_iot_score9+=1
            elif(anio_publidate_cve_iot >= 2020):
                count_lastpublidate_2020_cve_iot_score9+=1
            elif(anio_publidate_cve_iot >= 2019):
                count_lastpublidate_2019_cve_iot_score9+=1
            else:
                count_lastpublidate_2018_cve_iot_score9+=1
        elif(((float(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"][j])) < 9.0) and ((float(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"][j])) >=8.0)):
            CV3_BASE_score_8_iot+=1
            str_anio_publidate_cve_iot=df_cve_iot["CVE_Items.publishedDate"][j].split("-")
            anio_publidate_cve_iot=int(str_anio_publidate_cve_iot[0])
            if(anio_publidate_cve_iot >= 2023):
                count_lastpublidate_2023_cve_iot_score8+=1
            elif(anio_publidate_cve_iot >= 2022):
                count_lastpublidate_2022_cve_iot_score8+=1
            elif(anio_publidate_cve_iot >= 2021):
                count_lastpublidate_2021_cve_iot_score8+=1
            elif(anio_publidate_cve_iot >= 2020):
                count_lastpublidate_2020_cve_iot_score8+=1
            elif(anio_publidate_cve_iot >= 2019):
                count_lastpublidate_2019_cve_iot_score8+=1
            else:
                count_lastpublidate_2018_cve_iot_score8+=1
        elif(((float(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"][j])) < 8.0) and ((float(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"][j])) >=7.0)):
            CV3_BASE_score_7_iot+=1
            str_anio_publidate_cve_iot=df_cve_iot["CVE_Items.publishedDate"][j].split("-")
            anio_publidate_cve_iot=int(str_anio_publidate_cve_iot[0])
            if(anio_publidate_cve_iot >= 2023):
                count_lastpublidate_2023_cve_iot_score7+=1
            elif(anio_publidate_cve_iot >= 2022):
                count_lastpublidate_2022_cve_iot_score7+=1
            elif(anio_publidate_cve_iot >= 2021):
                count_lastpublidate_2021_cve_iot_score7+=1
            elif(anio_publidate_cve_iot >= 2020):
                count_lastpublidate_2020_cve_iot_score7+=1
            elif(anio_publidate_cve_iot >= 2019):
                count_lastpublidate_2019_cve_iot_score7+=1
            else:
                count_lastpublidate_2018_cve_iot_score7+=1
        elif(((float(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"][j])) < 7.0) and ((float(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"][j])) >=6.0)):
            CV3_BASE_score_6_iot+=1
            str_anio_publidate_cve_iot=df_cve_iot["CVE_Items.publishedDate"][j].split("-")
            anio_publidate_cve_iot=int(str_anio_publidate_cve_iot[0])
            if(anio_publidate_cve_iot >= 2023):
                count_lastpublidate_2023_cve_iot_score6+=1
            elif(anio_publidate_cve_iot >= 2022):
                count_lastpublidate_2022_cve_iot_score6+=1
            elif(anio_publidate_cve_iot >= 2021):
                count_lastpublidate_2021_cve_iot_score6+=1
            elif(anio_publidate_cve_iot >= 2020):
                count_lastpublidate_2020_cve_iot_score6+=1
            elif(anio_publidate_cve_iot >= 2019):
                count_lastpublidate_2019_cve_iot_score6+=1
            else:
                count_lastpublidate_2018_cve_iot_score6+=1
        elif(((float(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"][j])) < 6.0) and ((float(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"][j])) >=5.0)):
            CV3_BASE_score_5_iot+=1
            str_anio_publidate_cve_iot=df_cve_iot["CVE_Items.publishedDate"][j].split("-")
            anio_publidate_cve_iot=int(str_anio_publidate_cve_iot[0])
            if(anio_publidate_cve_iot >= 2023):
                count_lastpublidate_2023_cve_iot_score5+=1
            elif(anio_publidate_cve_iot >= 2022):
                count_lastpublidate_2022_cve_iot_score5+=1
            elif(anio_publidate_cve_iot >= 2021):
                count_lastpublidate_2021_cve_iot_score5+=1
            elif(anio_publidate_cve_iot >= 2020):
                count_lastpublidate_2020_cve_iot_score5+=1
            elif(anio_publidate_cve_iot >= 2019):
                count_lastpublidate_2019_cve_iot_score5+=1
            else:
                count_lastpublidate_2018_cve_iot_score5+=1
        elif(((float(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"][j])) < 5.0) and ((float(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"][j])) >=4.0)):
            CV3_BASE_score_4_iot+=1
            str_anio_publidate_cve_iot=df_cve_iot["CVE_Items.publishedDate"][j].split("-")
            anio_publidate_cve_iot=int(str_anio_publidate_cve_iot[0])
            if(anio_publidate_cve_iot >= 2023):
                count_lastpublidate_2023_cve_iot_score4+=1
            elif(anio_publidate_cve_iot >= 2022):
                count_lastpublidate_2022_cve_iot_score4+=1
            elif(anio_publidate_cve_iot >= 2021):
                count_lastpublidate_2021_cve_iot_score4+=1
            elif(anio_publidate_cve_iot >= 2020):
                count_lastpublidate_2020_cve_iot_score4+=1
            elif(anio_publidate_cve_iot >= 2019):
                count_lastpublidate_2019_cve_iot_score4+=1
            else:
                count_lastpublidate_2018_cve_iot_score4+=1
        elif(((float(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"][j])) < 4.0) and ((float(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"][j])) >=3.0)):
            CV3_BASE_score_3_iot+=1
            str_anio_publidate_cve_iot=df_cve_iot["CVE_Items.publishedDate"][j].split("-")
            anio_publidate_cve_iot=int(str_anio_publidate_cve_iot[0])
            if(anio_publidate_cve_iot >= 2023):
                count_lastpublidate_2023_cve_iot_score3+=1
            elif(anio_publidate_cve_iot >= 2022):
                count_lastpublidate_2022_cve_iot_score3+=1
            elif(anio_publidate_cve_iot >= 2021):
                count_lastpublidate_2021_cve_iot_score3+=1
            elif(anio_publidate_cve_iot >= 2020):
                count_lastpublidate_2020_cve_iot_score3+=1
            elif(anio_publidate_cve_iot >= 2019):
                count_lastpublidate_2019_cve_iot_score3+=1
            else:
                count_lastpublidate_2018_cve_iot_score3+=1
        elif(((float(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"][j])) < 3.0) and ((float(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"][j])) >=2.0)):
            CV3_BASE_score_2_iot+=1
            str_anio_publidate_cve_iot=df_cve_iot["CVE_Items.publishedDate"][j].split("-")
            anio_publidate_cve_iot=int(str_anio_publidate_cve_iot[0])
            if(anio_publidate_cve_iot >= 2023):
                count_lastpublidate_2023_cve_iot_score2+=1
            elif(anio_publidate_cve_iot >= 2022):
                count_lastpublidate_2022_cve_iot_score2+=1
            elif(anio_publidate_cve_iot >= 2021):
                count_lastpublidate_2021_cve_iot_score2+=1
            elif(anio_publidate_cve_iot >= 2020):
                count_lastpublidate_2020_cve_iot_score2+=1
            elif(anio_publidate_cve_iot >= 2019):
                count_lastpublidate_2019_cve_iot_score2+=1
            else:
                count_lastpublidate_2018_cve_iot_score2+=1
        elif(((float(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"][j])) < 2.0) and ((float(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"][j])) >=1.0)):
            CV3_BASE_score_1_iot+=1
            str_anio_publidate_cve_iot=df_cve_iot["CVE_Items.publishedDate"][j].split("-")
            anio_publidate_cve_iot=int(str_anio_publidate_cve_iot[0])
            if(anio_publidate_cve_iot >= 2023):
                count_lastpublidate_2023_cve_iot_score1+=1
            elif(anio_publidate_cve_iot >= 2022):
                count_lastpublidate_2022_cve_iot_score1+=1
            elif(anio_publidate_cve_iot >= 2021):
                count_lastpublidate_2021_cve_iot_score1+=1
            elif(anio_publidate_cve_iot >= 2020):
                count_lastpublidate_2020_cve_iot_score1+=1
            elif(anio_publidate_cve_iot >= 2019):
                count_lastpublidate_2019_cve_iot_score1+=1
            else:
                count_lastpublidate_2018_cve_iot_score1+=1
        elif(((float(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"][j])) < 1.0) and ((float(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"][j])) >=0.0)):
            CV3_BASE_score_0_iot+=1
            str_anio_publidate_cve_iot=df_cve_iot["CVE_Items.publishedDate"][j].split("-")
            anio_publidate_cve_iot=int(str_anio_publidate_cve_iot[0])
            if(anio_publidate_cve_iot >= 2023):
                count_lastpublidate_2023_cve_iot_score0+=1
            elif(anio_publidate_cve_iot >= 2022):
                count_lastpublidate_2022_cve_iot_score0+=1
            elif(anio_publidate_cve_iot >= 2021):
                count_lastpublidate_2021_cve_iot_score0+=1
            elif(anio_publidate_cve_iot >= 2020):
                count_lastpublidate_2020_cve_iot_score0+=1
            elif(anio_publidate_cve_iot >= 2019):
                count_lastpublidate_2019_cve_iot_score0+=1
            else:
                count_lastpublidate_2018_cve_iot_score0+=1
        elif(((float(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"][j])) == 10.0)):
            CV3_BASE_score_10_iot+=1
            str_anio_publidate_cve_iot=df_cve_iot["CVE_Items.publishedDate"][j].split("-")
            anio_publidate_cve_iot=int(str_anio_publidate_cve_iot[0])
            if(anio_publidate_cve_iot >= 2023):
                count_lastpublidate_2023_cve_iot_score10+=1
            elif(anio_publidate_cve_iot >= 2022):
                count_lastpublidate_2022_cve_iot_score10+=1
            elif(anio_publidate_cve_iot >= 2021):
                count_lastpublidate_2021_cve_iot_score10+=1
            elif(anio_publidate_cve_iot >= 2020):
                count_lastpublidate_2020_cve_iot_score10+=1
            elif(anio_publidate_cve_iot >= 2019):
                count_lastpublidate_2019_cve_iot_score10+=1
            else:
                count_lastpublidate_2018_cve_iot_score10+=1
    
print("************************** ESTADÍSTICAS PUNTUACION BASE/AÑO DE PUBLICACION EN CVE CVSSV3 IOT********************************")
print("\n")
print("\n")
print("DE UN TOTAL DE "+str(len(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"]))+" VULNERABILIDADES, LAS ESTADÍSTICAS DE FECHA DE FECHA DE PUBLICACIÓN DE LAS VULNERABILIDADES SEGÚN SU PUNTUACIÓN BASE SON LAS SIGUIENTES :  \n")
print("\n")

print(" -  EN "+str(CV3_BASE_score_10_iot)+" VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
print("       -     EN "+str(count_lastpublidate_2023_cve_iot_score10)+" VULNERABILIDADES PUBLICADAS EN 2023 LA PUNTUACION BASE ES 10 \n")
print("       -     EN "+str(count_lastpublidate_2022_cve_iot_score10)+" VULNERABILIDADES PUBLICADAS EN 2022 LA PUNTUACION BASE ES 10 \n")
print("       -     EN "+str(count_lastpublidate_2021_cve_iot_score10)+" VULNERABILIDADES PUBLICADAS EN 2021 LA PUNTUACION BASE ES 10 \n")
print("       -     EN "+str(count_lastpublidate_2020_cve_iot_score10)+" VULNERABILIDADES PUBLICADAS EN 2020 LA PUNTUACION BASE ES 10 \n")
print("       -     EN "+str(count_lastpublidate_2019_cve_iot_score10)+" VULNERABILIDADES PUBLICADAS EN 2019 LA PUNTUACION BASE ES 10 \n")
print("       -     EN "+str(count_lastpublidate_2018_cve_iot_score10)+" VULNERABILIDADES PUBLICADAS EN 2018 O ANTES LA PUNTUACION BASE ES 10 \n")

print(" -  EN "+str(CV3_BASE_score_9_iot)+" VULNERABILIDADES LA PUNTUACION BASE ESTÁ ENTRE 9 Y 10 \n")
print("       -     EN "+str(count_lastpublidate_2023_cve_iot_score9)+" VULNERABILIDADES PUBLICADAS EN 2023 LA PUNTUACION BASE ESTÁ ENTRE 9 Y 10 \n")
print("       -     EN "+str(count_lastpublidate_2022_cve_iot_score9)+" VULNERABILIDADES PUBLICADAS EN 2022 LA PUNTUACION BASE ESTÁ ENTRE 9 Y 10 \n")
print("       -     EN "+str(count_lastpublidate_2021_cve_iot_score9)+" VULNERABILIDADES PUBLICADAS EN 2021 LA PUNTUACION BASE ESTÁ ENTRE 9 Y 10 \n")
print("       -     EN "+str(count_lastpublidate_2020_cve_iot_score9)+" VULNERABILIDADES PUBLICADAS EN 2020 LA PUNTUACION BASE ESTÁ ENTRE 9 Y 10 \n")
print("       -     EN "+str(count_lastpublidate_2019_cve_iot_score9)+" VULNERABILIDADES PUBLICADAS EN 2019 LA PUNTUACION BASE ESTÁ ENTRE 9 Y 10 \n")
print("       -     EN "+str(count_lastpublidate_2018_cve_iot_score9)+" VULNERABILIDADES PUBLICADAS EN 2018 O ANTES LA PUNTUACION BASE ESTÁ ENTRE 9 Y 10 \n")

print(" -  EN "+str(CV3_BASE_score_8_iot)+" VULNERABILIDADES LA PUNTUACION BASE ESTÁ ENTRE 8 Y 9 \n")
print("       -     EN "+str(count_lastpublidate_2023_cve_iot_score8)+" VULNERABILIDADES PUBLICADAS EN 2023 LA PUNTUACION BASE ESTÁ ENTRE 8 Y 9 \n")
print("       -     EN "+str(count_lastpublidate_2022_cve_iot_score8)+" VULNERABILIDADES PUBLICADAS EN 2022 LA PUNTUACION BASE ESTÁ ENTRE 8 Y 9 \n")
print("       -     EN "+str(count_lastpublidate_2021_cve_iot_score8)+" VULNERABILIDADES PUBLICADAS EN 2021 LA PUNTUACION BASE ESTÁ ENTRE 8 Y 9 \n")
print("       -     EN "+str(count_lastpublidate_2020_cve_iot_score8)+" VULNERABILIDADES PUBLICADAS EN 2020 LA PUNTUACION BASE ESTÁ ENTRE 8 Y 9 \n")
print("       -     EN "+str(count_lastpublidate_2019_cve_iot_score8)+" VULNERABILIDADES PUBLICADAS EN 2019 LA PUNTUACION BASE ESTÁ ENTRE 8 Y 9 \n")
print("       -     EN "+str(count_lastpublidate_2018_cve_iot_score8)+" VULNERABILIDADES PUBLICADAS EN 2018 O ANTES LA PUNTUACION BASE ESTÁ ENTRE 8 Y 9 \n")

print(" -  EN "+str(CV3_BASE_score_7_iot)+" VULNERABILIDADES LA PUNTUACION BASE ESTÁ ENTRE 7 Y 8 \n")
print("       -     EN "+str(count_lastpublidate_2023_cve_iot_score7)+" VULNERABILIDADES PUBLICADAS EN 2023 LA PUNTUACION BASE ESTÁ ENTRE 7 Y 8 \n")
print("       -     EN "+str(count_lastpublidate_2022_cve_iot_score7)+" VULNERABILIDADES PUBLICADAS EN 2022 LA PUNTUACION BASE ESTÁ ENTRE 7 Y 8 \n")
print("       -     EN "+str(count_lastpublidate_2021_cve_iot_score7)+" VULNERABILIDADES PUBLICADAS EN 2021 LA PUNTUACION BASE ESTÁ ENTRE 7 Y 8 \n")
print("       -     EN "+str(count_lastpublidate_2020_cve_iot_score7)+" VULNERABILIDADES PUBLICADAS EN 2020 LA PUNTUACION BASE ESTÁ ENTRE 7 Y 8 \n")
print("       -     EN "+str(count_lastpublidate_2019_cve_iot_score7)+" VULNERABILIDADES PUBLICADAS EN 2019 LA PUNTUACION BASE ESTÁ ENTRE 7 Y 8 \n")
print("       -     EN "+str(count_lastpublidate_2018_cve_iot_score7)+" VULNERABILIDADES PUBLICADAS EN 2018 O ANTES LA PUNTUACION BASE ESTÁ ENTRE 7 Y 8 \n")

print(" -  EN "+str(CV3_BASE_score_6_iot)+" VULNERABILIDADES LA PUNTUACION BASE ESTÁ ENTRE 6 y 7 \n")
print("       -     EN "+str(count_lastpublidate_2023_cve_iot_score6)+" VULNERABILIDADES PUBLICADAS EN 2023 LA PUNTUACION BASE ESTÁ ENTRE 6 y 7 \n")
print("       -     EN "+str(count_lastpublidate_2022_cve_iot_score6)+" VULNERABILIDADES PUBLICADAS EN 2022 LA PUNTUACION BASE ESTÁ ENTRE 6 y 7 \n")
print("       -     EN "+str(count_lastpublidate_2021_cve_iot_score6)+" VULNERABILIDADES PUBLICADAS EN 2021 LA PUNTUACION BASE ESTÁ ENTRE 6 y 7 \n")
print("       -     EN "+str(count_lastpublidate_2020_cve_iot_score6)+" VULNERABILIDADES PUBLICADAS EN 2020 LA PUNTUACION BASE ESTÁ ENTRE 6 y 7 \n")
print("       -     EN "+str(count_lastpublidate_2019_cve_iot_score6)+" VULNERABILIDADES PUBLICADAS EN 2019 LA PUNTUACION BASE ESTÁ ENTRE 6 y 7 \n")
print("       -     EN "+str(count_lastpublidate_2018_cve_iot_score6)+" VULNERABILIDADES PUBLICADAS EN 2018 O ANTES LA PUNTUACION BASE ESTÁ ENTRE 6 y 7 \n")

print(" -  EN "+str(CV3_BASE_score_5_iot)+" VULNERABILIDADES LA PUNTUACION BASE ESTÁ ENTRE 5 y 6 \n")
print("       -     EN "+str(count_lastpublidate_2023_cve_iot_score5)+" VULNERABILIDADES PUBLICADAS EN 2023 LA PUNTUACION BASE ESTÁ ENTRE 5 y 6 \n")
print("       -     EN "+str(count_lastpublidate_2022_cve_iot_score5)+" VULNERABILIDADES PUBLICADAS EN 2022 LA PUNTUACION BASE ESTÁ ENTRE 5 y 6 \n")
print("       -     EN "+str(count_lastpublidate_2021_cve_iot_score5)+" VULNERABILIDADES PUBLICADAS EN 2021 LA PUNTUACION BASE ESTÁ ENTRE 5 y 6 \n")
print("       -     EN "+str(count_lastpublidate_2020_cve_iot_score5)+" VULNERABILIDADES PUBLICADAS EN 2020 LA PUNTUACION BASE ESTÁ ENTRE 5 y 6 \n")
print("       -     EN "+str(count_lastpublidate_2019_cve_iot_score5)+" VULNERABILIDADES PUBLICADAS EN 2019 LA PUNTUACION BASE ESTÁ ENTRE 5 y 6 \n")
print("       -     EN "+str(count_lastpublidate_2018_cve_iot_score5)+" VULNERABILIDADES PUBLICADAS EN 2018 O ANTES LA PUNTUACION BASE ESTÁ ENTRE 5 y 6 \n")

print(" -  EN "+str(CV3_BASE_score_4_iot)+" VULNERABILIDADES LA PUNTUACION BASE ESTÁ ENTRE 4 y 5 \n")
print("       -     EN "+str(count_lastpublidate_2023_cve_iot_score4)+" VULNERABILIDADES PUBLICADAS EN 2023 LA PUNTUACION BASE ESTÁ ENTRE 4 y 5 \n")
print("       -     EN "+str(count_lastpublidate_2022_cve_iot_score4)+" VULNERABILIDADES PUBLICADAS EN 2022 LA PUNTUACION BASE ESTÁ ENTRE 4 y 5 \n")
print("       -     EN "+str(count_lastpublidate_2021_cve_iot_score4)+" VULNERABILIDADES PUBLICADAS EN 2021 LA PUNTUACION BASE ESTÁ ENTRE 4 y 5 \n")
print("       -     EN "+str(count_lastpublidate_2020_cve_iot_score4)+" VULNERABILIDADES PUBLICADAS EN 2020 LA PUNTUACION BASE ESTÁ ENTRE 4 y 5 \n")
print("       -     EN "+str(count_lastpublidate_2019_cve_iot_score4)+" VULNERABILIDADES PUBLICADAS EN 2019 LA PUNTUACION BASE ESTÁ ENTRE 4 y 5 \n")
print("       -     EN "+str(count_lastpublidate_2018_cve_iot_score4)+" VULNERABILIDADES PUBLICADAS EN 2018 O ANTES LA PUNTUACION BASE ESTÁ ENTRE 4 y 5 \n")

print(" -  EN "+str(CV3_BASE_score_3_iot)+" VULNERABILIDADES LA PUNTUACION BASE ESTÁ ENTRE 3 y 4 \n")
print("       -     EN "+str(count_lastpublidate_2023_cve_iot_score3)+" VULNERABILIDADES PUBLICADAS EN 2023 LA PUNTUACION BASE ESTÁ ENTRE 3 y 4 \n")
print("       -     EN "+str(count_lastpublidate_2022_cve_iot_score3)+" VULNERABILIDADES PUBLICADAS EN 2022 LA PUNTUACION BASE ESTÁ ENTRE 3 y 4 \n")
print("       -     EN "+str(count_lastpublidate_2021_cve_iot_score3)+" VULNERABILIDADES PUBLICADAS EN 2021 LA PUNTUACION BASE ESTÁ ENTRE 3 y 4 \n")
print("       -     EN "+str(count_lastpublidate_2020_cve_iot_score3)+" VULNERABILIDADES PUBLICADAS EN 2020 LA PUNTUACION BASE ESTÁ ENTRE 3 y 4 \n")
print("       -     EN "+str(count_lastpublidate_2019_cve_iot_score3)+" VULNERABILIDADES PUBLICADAS EN 2019 LA PUNTUACION BASE ESTÁ ENTRE 3 y 4 \n")
print("       -     EN "+str(count_lastpublidate_2018_cve_iot_score3)+" VULNERABILIDADES PUBLICADAS EN 2018 O ANTES LA PUNTUACION BASE ESTÁ ENTRE 3 y 4 \n")

print(" -  EN "+str(CV3_BASE_score_2_iot)+" VULNERABILIDADES LA PUNTUACION BASE ESTÁ ENTRE 2 y 3 \n")
print("       -     EN "+str(count_lastpublidate_2023_cve_iot_score2)+" VULNERABILIDADES PUBLICADAS EN 2023 LA PUNTUACION BASE ESTÁ ENTRE 2 y 3 \n")
print("       -     EN "+str(count_lastpublidate_2022_cve_iot_score2)+" VULNERABILIDADES PUBLICADAS EN 2022 LA PUNTUACION BASE ESTÁ ENTRE 2 y 3 \n")
print("       -     EN "+str(count_lastpublidate_2021_cve_iot_score2)+" VULNERABILIDADES PUBLICADAS EN 2021 LA PUNTUACION BASE ESTÁ ENTRE 2 y 3 \n")
print("       -     EN "+str(count_lastpublidate_2020_cve_iot_score2)+" VULNERABILIDADES PUBLICADAS EN 2020 LA PUNTUACION BASE ESTÁ ENTRE 2 y 3 \n")
print("       -     EN "+str(count_lastpublidate_2019_cve_iot_score2)+" VULNERABILIDADES PUBLICADAS EN 2019 LA PUNTUACION BASE ESTÁ ENTRE 2 y 3 \n")
print("       -     EN "+str(count_lastpublidate_2018_cve_iot_score2)+" VULNERABILIDADES PUBLICADAS EN 2018 O ANTES LA PUNTUACION BASE ESTÁ ENTRE 2 y 3 \n")

print(" -  EN "+str(CV3_BASE_score_1_iot)+" VULNERABILIDADES LA PUNTUACION BASE ESTÁ ENTRE 1 y 2 \n")
print("       -     EN "+str(count_lastpublidate_2023_cve_iot_score1)+" VULNERABILIDADES PUBLICADAS EN 2023 LA PUNTUACION BASE ESTÁ ENTRE 1 y 2 \n")
print("       -     EN "+str(count_lastpublidate_2022_cve_iot_score1)+" VULNERABILIDADES PUBLICADAS EN 2022 LA PUNTUACION BASE ESTÁ ENTRE 1 y 2 \n")
print("       -     EN "+str(count_lastpublidate_2021_cve_iot_score1)+" VULNERABILIDADES PUBLICADAS EN 2021 LA PUNTUACION BASE ESTÁ ENTRE 1 y 2 \n")
print("       -     EN "+str(count_lastpublidate_2020_cve_iot_score1)+" VULNERABILIDADES PUBLICADAS EN 2020 LA PUNTUACION BASE ESTÁ ENTRE 1 y 2 \n")
print("       -     EN "+str(count_lastpublidate_2019_cve_iot_score1)+" VULNERABILIDADES PUBLICADAS EN 2019 LA PUNTUACION BASE ESTÁ ENTRE 1 y 2 \n")
print("       -     EN "+str(count_lastpublidate_2018_cve_iot_score1)+" VULNERABILIDADES PUBLICADAS EN 2018 O ANTES LA PUNTUACION BASE ESTÁ ENTRE 1 y 2 \n")

print(" -  EN "+str(CV3_BASE_score_0_iot)+" VULNERABILIDADES LA PUNTUACION BASE ESTÁ ENTRE 0 y 1 \n")
print("       -     EN "+str(count_lastpublidate_2023_cve_iot_score0)+" VULNERABILIDADES PUBLICADAS EN 2023 LA PUNTUACION BASE ESTÁ ENTRE 0 y 1 \n")
print("       -     EN "+str(count_lastpublidate_2022_cve_iot_score0)+" VULNERABILIDADES PUBLICADAS EN 2022 LA PUNTUACION BASE ESTÁ ENTRE 0 y 1 \n")
print("       -     EN "+str(count_lastpublidate_2021_cve_iot_score0)+" VULNERABILIDADES PUBLICADAS EN 2021 LA PUNTUACION BASE ESTÁ ENTRE 0 y 1 \n")
print("       -     EN "+str(count_lastpublidate_2020_cve_iot_score0)+" VULNERABILIDADES PUBLICADAS EN 2020 LA PUNTUACION BASE ESTÁ ENTRE 0 y 1 \n")
print("       -     EN "+str(count_lastpublidate_2019_cve_iot_score0)+" VULNERABILIDADES PUBLICADAS EN 2019 LA PUNTUACION BASE ESTÁ ENTRE 0 y 1 \n")
print("       -     EN "+str(count_lastpublidate_2018_cve_iot_score0)+" VULNERABILIDADES PUBLICADAS EN 2018 O ANTES LA PUNTUACION BASE ESTÁ ENTRE 0 y 1 \n")
print("\n")
print("***************************PORCENTAJE PUNTUACION BASE/AÑO DE PUBLICACION EN CVE CVSSV3 IOT********************************")
print("\n")
print("\n")
print("DE UN TOTAL DE "+str(len(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"]))+" VULNERABILIDADES, LOS PORCENTAJES DE FECHA DE PUBLICACIÓN DE LAS VULNERABILIDADES SEGÚN SU PUNTUACIÓN BASE SON LOS SIGUIENTES :  \n")
print("\n")
if(CV3_BASE_score_10_iot>0):
    print(" -  EN EL "+str(float(((CV3_BASE_score_10_iot*100)/len(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"]))))+"% DE LAS VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
    print("       -     EN EL "+str(float(((count_lastpublidate_2023_cve_iot_score10*100)/CV3_BASE_score_10_iot)))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2023 LA PUNTUACION BASE ES 10 \n")
    print("       -     EN EL "+str(float(((count_lastpublidate_2022_cve_iot_score10*100)/CV3_BASE_score_10_iot)))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2022 LA PUNTUACION BASE ES 10 \n")
    print("       -     EN EL "+str(float(((count_lastpublidate_2021_cve_iot_score10*100)/CV3_BASE_score_10_iot)))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2021 LA PUNTUACION BASE ES 10 \n")
    print("       -     EN EL "+str(float(((count_lastpublidate_2020_cve_iot_score10*100)/CV3_BASE_score_10_iot)))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2020 LA PUNTUACION BASE ES 10 \n")
    print("       -     EN EL "+str(float(((count_lastpublidate_2019_cve_iot_score10*100)/CV3_BASE_score_10_iot)))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2019 LA PUNTUACION BASE ES 10 \n")
    print("       -     EN EL "+str(float(((count_lastpublidate_2018_cve_iot_score10*100)/CV3_BASE_score_10_iot)))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2018 O ANTERIORMENTE LA PUNTUACION BASE ES 10 \n")
    
if(CV3_BASE_score_9_iot>0):
    print(" -  EN EL "+str(float(((CV3_BASE_score_9_iot*100)/len(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"]))))+"% DE LAS VULNERABILIDADES LA PUNTUACION BASE ESTÁ ENTRE 9 Y 10 \n")
    print("       -     EN EL "+str(float(((count_lastpublidate_2023_cve_iot_score9*100)/CV3_BASE_score_9_iot)))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2023 LA PUNTUACION BASE ESTÁ ENTRE 9 Y 10 \n")
    print("       -     EN EL "+str(float(((count_lastpublidate_2022_cve_iot_score9*100)/CV3_BASE_score_9_iot)))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2022 LA PUNTUACION BASE ESTÁ ENTRE 9 Y 10 \n")
    print("       -     EN EL "+str(float(((count_lastpublidate_2021_cve_iot_score9*100)/CV3_BASE_score_9_iot)))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2021 LA PUNTUACION BASE ESTÁ ENTRE 9 Y 10 \n")
    print("       -     EN EL "+str(float(((count_lastpublidate_2020_cve_iot_score9*100)/CV3_BASE_score_9_iot)))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2020 LA PUNTUACION BASE ESTÁ ENTRE 9 Y 10 \n")
    print("       -     EN EL "+str(float(((count_lastpublidate_2019_cve_iot_score9*100)/CV3_BASE_score_9_iot)))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2019 LA PUNTUACION BASE ESTÁ ENTRE 9 Y 10 \n")
    print("       -     EN EL "+str(float(((count_lastpublidate_2018_cve_iot_score9*100)/CV3_BASE_score_9_iot)))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2018 O ANTERIORMENTE LA PUNTUACION BASE ESTÁ ENTRE 9 Y 10 \n")


if(CV3_BASE_score_8_iot>0):
    print(" -  EN EL "+str(float(((CV3_BASE_score_8_iot*100)/len(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"]))))+"% DE LAS VULNERABILIDADES LA PUNTUACION BASE ESTÁ ENTRE 8 y 9 \n")
    print("       -     EN EL "+str(float(((count_lastpublidate_2023_cve_iot_score8*100)/CV3_BASE_score_8_iot)))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2023 LA PUNTUACION BASE ESTÁ ENTRE 8 y 9 \n")
    print("       -     EN EL "+str(float(((count_lastpublidate_2022_cve_iot_score8*100)/CV3_BASE_score_8_iot)))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2022 LA PUNTUACION BASE ESTÁ ENTRE 8 y 9 \n")
    print("       -     EN EL "+str(float(((count_lastpublidate_2021_cve_iot_score8*100)/CV3_BASE_score_8_iot)))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2021 LA PUNTUACION BASE ESTÁ ENTRE 8 y 9 \n")
    print("       -     EN EL "+str(float(((count_lastpublidate_2020_cve_iot_score8*100)/CV3_BASE_score_8_iot)))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2020 LA PUNTUACION BASE ESTÁ ENTRE 8 y 9 \n")
    print("       -     EN EL "+str(float(((count_lastpublidate_2019_cve_iot_score8*100)/CV3_BASE_score_8_iot)))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2019 LA PUNTUACION BASE ESTÁ ENTRE 8 y 9 \n")
    print("       -     EN EL "+str(float(((count_lastpublidate_2018_cve_iot_score8*100)/CV3_BASE_score_8_iot)))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2018 O ANTERIORMENTE LA PUNTUACION BASE ESTÁ ENTRE 8 y 9 \n")

if(CV3_BASE_score_7_iot>0):
    print(" -  EN EL "+str(float(((CV3_BASE_score_7_iot*100)/len(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"]))))+"% DE LAS VULNERABILIDADES LA PUNTUACION BASE ESTÁ ENTRE 7 y 8 \n")
    print("       -     EN EL "+str(float(((count_lastpublidate_2023_cve_iot_score7*100)/CV3_BASE_score_7_iot)))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2023 LA PUNTUACION BASE ESTÁ ENTRE 7 y 8 \n")
    print("       -     EN EL "+str(float(((count_lastpublidate_2022_cve_iot_score7*100)/CV3_BASE_score_7_iot)))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2022 LA PUNTUACION BASE ESTÁ ENTRE 7 y 8 \n")
    print("       -     EN EL "+str(float(((count_lastpublidate_2021_cve_iot_score7*100)/CV3_BASE_score_7_iot)))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2021 LA PUNTUACION BASE ESTÁ ENTRE 7 y 8 \n")
    print("       -     EN EL "+str(float(((count_lastpublidate_2020_cve_iot_score7*100)/CV3_BASE_score_7_iot)))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2020 LA PUNTUACION BASE ESTÁ ENTRE 7 y 8 \n")
    print("       -     EN EL "+str(float(((count_lastpublidate_2019_cve_iot_score7*100)/CV3_BASE_score_7_iot)))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2019 LA PUNTUACION BASE ESTÁ ENTRE 7 y 8 \n")
    print("       -     EN EL "+str(float(((count_lastpublidate_2018_cve_iot_score7*100)/CV3_BASE_score_7_iot)))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2018 O ANTERIORMENTE LA PUNTUACION BASE ESTÁ ENTRE 7 y 8 \n")
if(CV3_BASE_score_6_iot>0):
    print(" -  EN EL "+str(float(((CV3_BASE_score_6_iot*100)/len(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"]))))+"% DE LAS VULNERABILIDADES LA PUNTUACION BASE ESTÁ ENTRE 6 y 7 \n")
    print("       -     EN EL "+str(float(((count_lastpublidate_2023_cve_iot_score6*100)/CV3_BASE_score_6_iot)))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2023 LA PUNTUACION BASE ESTÁ ENTRE 6 y 7 \n")
    print("       -     EN EL "+str(float(((count_lastpublidate_2022_cve_iot_score6*100)/CV3_BASE_score_6_iot)))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2022 LA PUNTUACION BASE ESTÁ ENTRE 6 y 7 \n")
    print("       -     EN EL "+str(float(((count_lastpublidate_2021_cve_iot_score6*100)/CV3_BASE_score_6_iot)))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2021 LA PUNTUACION BASE ESTÁ ENTRE 6 y 7 \n")
    print("       -     EN EL "+str(float(((count_lastpublidate_2020_cve_iot_score6*100)/CV3_BASE_score_6_iot)))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2020 LA PUNTUACION BASE ESTÁ ENTRE 6 y 7 \n")
    print("       -     EN EL "+str(float(((count_lastpublidate_2019_cve_iot_score6*100)/CV3_BASE_score_6_iot)))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2019 LA PUNTUACION BASE ESTÁ ENTRE 6 y 7 \n")
    print("       -     EN EL "+str(float(((count_lastpublidate_2018_cve_iot_score6*100)/CV3_BASE_score_6_iot)))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2018 O ANTERIORMENTE LA PUNTUACION BASE ESTÁ ENTRE 6 y 7 \n")
if(CV3_BASE_score_5_iot>0):
    print(" -  EN EL "+str(float(((CV3_BASE_score_5_iot*100)/len(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"]))))+"% DE LAS VULNERABILIDADES LA PUNTUACION BASE ESTÁ ENTRE 5 y 6 \n")
    print("       -     EN EL "+str(float(((count_lastpublidate_2023_cve_iot_score5*100)/CV3_BASE_score_5_iot)))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2023 LA PUNTUACION BASE ESTÁ ENTRE 5 y 6 \n")
    print("       -     EN EL "+str(float(((count_lastpublidate_2022_cve_iot_score5*100)/CV3_BASE_score_5_iot)))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2022 LA PUNTUACION BASE ESTÁ ENTRE 5 y 6 \n")
    print("       -     EN EL "+str(float(((count_lastpublidate_2021_cve_iot_score5*100)/CV3_BASE_score_5_iot)))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2021 LA PUNTUACION BASE ESTÁ ENTRE 5 y 6 \n")
    print("       -     EN EL "+str(float(((count_lastpublidate_2020_cve_iot_score5*100)/CV3_BASE_score_5_iot)))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2020 LA PUNTUACION BASE ESTÁ ENTRE 5 y 6 \n")
    print("       -     EN EL "+str(float(((count_lastpublidate_2019_cve_iot_score5*100)/CV3_BASE_score_5_iot)))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2019 LA PUNTUACION BASE ESTÁ ENTRE 5 y 6 \n")
    print("       -     EN EL "+str(float(((count_lastpublidate_2018_cve_iot_score5*100)/CV3_BASE_score_5_iot)))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2018 O ANTERIORMENTE LA PUNTUACION BASE ESTÁ ENTRE 5 y 6 \n")
if(CV3_BASE_score_4_iot>0):
    print(" -  EN EL "+str(float(((CV3_BASE_score_4_iot*100)/len(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"]))))+"% DE LAS VULNERABILIDADES LA PUNTUACION BASE ESTÁ ENTRE 4 y 5 \n")
    print("       -     EN EL "+str(float(((count_lastpublidate_2023_cve_iot_score4*100)/CV3_BASE_score_4_iot)))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2023 LA PUNTUACION BASE ESTÁ ENTRE 4 y 5 \n")
    print("       -     EN EL "+str(float(((count_lastpublidate_2022_cve_iot_score4*100)/CV3_BASE_score_4_iot)))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2022 LA PUNTUACION BASE ESTÁ ENTRE 4 y 5 \n")
    print("       -     EN EL "+str(float(((count_lastpublidate_2021_cve_iot_score4*100)/CV3_BASE_score_4_iot)))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2021 LA PUNTUACION BASE ESTÁ ENTRE 4 y 5 \n")
    print("       -     EN EL "+str(float(((count_lastpublidate_2020_cve_iot_score4*100)/CV3_BASE_score_4_iot)))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2020 LA PUNTUACION BASE ESTÁ ENTRE 4 y 5 \n")
    print("       -     EN EL "+str(float(((count_lastpublidate_2019_cve_iot_score4*100)/CV3_BASE_score_4_iot)))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2019 LA PUNTUACION BASE ESTÁ ENTRE 4 y 5 \n")
    print("       -     EN EL "+str(float(((count_lastpublidate_2018_cve_iot_score4*100)/CV3_BASE_score_4_iot)))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2018 O ANTERIORMENTE LA PUNTUACION BASE ESTÁ ENTRE 4 y 5 \n")
if(CV3_BASE_score_3_iot>0):
    print(" -  EN EL "+str(float(((CV3_BASE_score_3_iot*100)/len(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"]))))+"% DE LAS VULNERABILIDADES LA PUNTUACION BASE ESTÁ ENTRE 3 y 4 \n")
    print("       -     EN EL "+str(float(((count_lastpublidate_2023_cve_iot_score3*100)/CV3_BASE_score_3_iot)))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2023 LA PUNTUACION BASE ESTÁ ENTRE 3 y 4 \n")
    print("       -     EN EL "+str(float(((count_lastpublidate_2022_cve_iot_score3*100)/CV3_BASE_score_3_iot)))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2022 LA PUNTUACION BASE ESTÁ ENTRE 3 y 4 \n")
    print("       -     EN EL "+str(float(((count_lastpublidate_2021_cve_iot_score3*100)/CV3_BASE_score_3_iot)))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2021 LA PUNTUACION BASE ESTÁ ENTRE 3 y 4 \n")
    print("       -     EN EL "+str(float(((count_lastpublidate_2020_cve_iot_score3*100)/CV3_BASE_score_3_iot)))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2020 LA PUNTUACION BASE ESTÁ ENTRE 3 y 4 \n")
    print("       -     EN EL "+str(float(((count_lastpublidate_2019_cve_iot_score3*100)/CV3_BASE_score_3_iot)))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2019 LA PUNTUACION BASE ESTÁ ENTRE 3 y 4 \n")
    print("       -     EN EL "+str(float(((count_lastpublidate_2018_cve_iot_score3*100)/CV3_BASE_score_3_iot)))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2018 O ANTERIORMENTE LA PUNTUACION BASE ESTÁ ENTRE 3 y 4 \n")
if(CV3_BASE_score_2_iot>0):
    print(" -  EN EL "+str(float(((CV3_BASE_score_2_iot*100)/len(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"]))))+"% DE LAS VULNERABILIDADES LA PUNTUACION BASE ESTÁ ENTRE 2 y 3 \n")
    print("       -     EN EL "+str(float(((count_lastpublidate_2023_cve_iot_score2*100)/CV3_BASE_score_2_iot)))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2023 LA PUNTUACION BASE ESTÁ ENTRE 2 y 3 \n")
    print("       -     EN EL "+str(float(((count_lastpublidate_2022_cve_iot_score2*100)/CV3_BASE_score_2_iot)))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2022 LA PUNTUACION BASE ESTÁ ENTRE 2 y 3 \n")
    print("       -     EN EL "+str(float(((count_lastpublidate_2021_cve_iot_score2*100)/CV3_BASE_score_2_iot)))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2021 LA PUNTUACION BASE ESTÁ ENTRE 2 y 3 \n")
    print("       -     EN EL "+str(float(((count_lastpublidate_2020_cve_iot_score2*100)/CV3_BASE_score_2_iot)))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2020 LA PUNTUACION BASE ESTÁ ENTRE 2 y 3 \n")
    print("       -     EN EL "+str(float(((count_lastpublidate_2019_cve_iot_score2*100)/CV3_BASE_score_2_iot)))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2019 LA PUNTUACION BASE ESTÁ ENTRE 2 y 3 \n")
    print("       -     EN EL "+str(float(((count_lastpublidate_2018_cve_iot_score2*100)/CV3_BASE_score_2_iot)))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2018 O ANTERIORMENTE LA PUNTUACION BASE ESTÁ ENTRE 2 y 3 \n")
if(CV3_BASE_score_1_iot>0):
    print(" -  EN EL "+str(float(((CV3_BASE_score_1_iot*100)/len(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"]))))+"% DE LAS VULNERABILIDADES LA PUNTUACION BASE ESTÁ ENTRE 1 y 2 \n")
    print("       -     EN EL "+str(float(((count_lastpublidate_2023_cve_iot_score1*100)/CV3_BASE_score_1_iot)))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2023 LA PUNTUACION BASE ESTÁ ENTRE 1 y 2 \n")
    print("       -     EN EL "+str(float(((count_lastpublidate_2022_cve_iot_score1*100)/CV3_BASE_score_1_iot)))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2022 LA PUNTUACION BASE ESTÁ ENTRE 1 y 2 \n")
    print("       -     EN EL "+str(float(((count_lastpublidate_2021_cve_iot_score1*100)/CV3_BASE_score_1_iot)))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2021 LA PUNTUACION BASE ESTÁ ENTRE 1 y 2 \n")
    print("       -     EN EL "+str(float(((count_lastpublidate_2020_cve_iot_score1*100)/CV3_BASE_score_1_iot)))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2020 LA PUNTUACION BASE ESTÁ ENTRE 1 y 2 \n")
    print("       -     EN EL "+str(float(((count_lastpublidate_2019_cve_iot_score1*100)/CV3_BASE_score_1_iot)))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2019 LA PUNTUACION BASE ESTÁ ENTRE 1 y 2 \n")
    print("       -     EN EL "+str(float(((count_lastpublidate_2018_cve_iot_score1*100)/CV3_BASE_score_1_iot)))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2018 O ANTERIORMENTE LA PUNTUACION BASE ESTÁ ENTRE 1 y 2 \n")
if(CV3_BASE_score_0_iot>0):
    print(" -  EN EL "+str(float(((CV3_BASE_score_0_iot*100)/len(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"]))))+"% DE LAS VULNERABILIDADES LA PUNTUACION BASE ESTÁ ENTRE 0 y 1 \n")
    print("       -     EN EL "+str(float(((count_lastpublidate_2023_cve_iot_score0*100)/CV3_BASE_score_0_iot)))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2023 LA PUNTUACION BASE ESTÁ ENTRE 0 y 1 \n")
    print("       -     EN EL "+str(float(((count_lastpublidate_2022_cve_iot_score0*100)/CV3_BASE_score_0_iot)))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2022 LA PUNTUACION BASE ESTÁ ENTRE 0 y 1 \n")
    print("       -     EN EL "+str(float(((count_lastpublidate_2021_cve_iot_score0*100)/CV3_BASE_score_0_iot)))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2021 LA PUNTUACION BASE ESTÁ ENTRE 0 y 1 \n")
    print("       -     EN EL "+str(float(((count_lastpublidate_2020_cve_iot_score0*100)/CV3_BASE_score_0_iot)))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2020 LA PUNTUACION BASE ESTÁ ENTRE 0 y 1 \n")
    print("       -     EN EL "+str(float(((count_lastpublidate_2019_cve_iot_score0*100)/CV3_BASE_score_0_iot)))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2019 LA PUNTUACION BASE ESTÁ ENTRE 0 y 1 \n")
    print("       -     EN EL "+str(float(((count_lastpublidate_2018_cve_iot_score0*100)/CV3_BASE_score_0_iot)))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2018 O ANTERIORMENTE LA PUNTUACION BASE ESTÁ ENTRE 0 y 1 \n")




#Variables donde almacenare el contador de PUNTUACION BASE CVE CVSS3  y la fecha de publicacion de la vulnerabilidad para SMART HOME

CV3_BASE_score_9_sh=0
count_lastpublidate_2023_cve_sh_score9=0
count_lastpublidate_2022_cve_sh_score9=0
count_lastpublidate_2021_cve_sh_score9=0
count_lastpublidate_2020_cve_sh_score9=0
count_lastpublidate_2019_cve_sh_score9=0
count_lastpublidate_2018_cve_sh_score9=0
CV3_BASE_score_8_sh=0
count_lastpublidate_2023_cve_sh_score8=0
count_lastpublidate_2022_cve_sh_score8=0
count_lastpublidate_2021_cve_sh_score8=0
count_lastpublidate_2020_cve_sh_score8=0
count_lastpublidate_2019_cve_sh_score8=0
count_lastpublidate_2018_cve_sh_score8=0
CV3_BASE_score_7_sh=0
count_lastpublidate_2023_cve_sh_score7=0
count_lastpublidate_2022_cve_sh_score7=0
count_lastpublidate_2021_cve_sh_score7=0
count_lastpublidate_2020_cve_sh_score7=0
count_lastpublidate_2019_cve_sh_score7=0
count_lastpublidate_2018_cve_sh_score7=0
CV3_BASE_score_6_sh=0
count_lastpublidate_2023_cve_sh_score6=0
count_lastpublidate_2022_cve_sh_score6=0
count_lastpublidate_2021_cve_sh_score6=0
count_lastpublidate_2020_cve_sh_score6=0
count_lastpublidate_2019_cve_sh_score6=0
count_lastpublidate_2018_cve_sh_score6=0
CV3_BASE_score_5_sh=0
count_lastpublidate_2023_cve_sh_score5=0
count_lastpublidate_2022_cve_sh_score5=0
count_lastpublidate_2021_cve_sh_score5=0
count_lastpublidate_2020_cve_sh_score5=0
count_lastpublidate_2019_cve_sh_score5=0
count_lastpublidate_2018_cve_sh_score5=0
CV3_BASE_score_4_sh=0
count_lastpublidate_2023_cve_sh_score4=0
count_lastpublidate_2022_cve_sh_score4=0
count_lastpublidate_2021_cve_sh_score4=0
count_lastpublidate_2020_cve_sh_score4=0
count_lastpublidate_2019_cve_sh_score4=0
count_lastpublidate_2018_cve_sh_score4=0
CV3_BASE_score_3_sh=0
count_lastpublidate_2023_cve_sh_score3=0
count_lastpublidate_2022_cve_sh_score3=0
count_lastpublidate_2021_cve_sh_score3=0
count_lastpublidate_2020_cve_sh_score3=0
count_lastpublidate_2019_cve_sh_score3=0
count_lastpublidate_2018_cve_sh_score3=0
CV3_BASE_score_2_sh=0
count_lastpublidate_2023_cve_sh_score2=0
count_lastpublidate_2022_cve_sh_score2=0
count_lastpublidate_2021_cve_sh_score2=0
count_lastpublidate_2020_cve_sh_score2=0
count_lastpublidate_2019_cve_sh_score2=0
count_lastpublidate_2018_cve_sh_score2=0
CV3_BASE_score_1_sh=0
count_lastpublidate_2023_cve_sh_score1=0
count_lastpublidate_2022_cve_sh_score1=0
count_lastpublidate_2021_cve_sh_score1=0
count_lastpublidate_2020_cve_sh_score1=0
count_lastpublidate_2019_cve_sh_score1=0
count_lastpublidate_2018_cve_sh_score1=0
CV3_BASE_score_0_sh=0
count_lastpublidate_2023_cve_sh_score0=0
count_lastpublidate_2022_cve_sh_score0=0
count_lastpublidate_2021_cve_sh_score0=0
count_lastpublidate_2020_cve_sh_score0=0
count_lastpublidate_2019_cve_sh_score0=0
count_lastpublidate_2018_cve_sh_score0=0
CV3_BASE_score_10_sh=0
count_lastpublidate_2023_cve_sh_score10=0
count_lastpublidate_2022_cve_sh_score10=0
count_lastpublidate_2021_cve_sh_score10=0
count_lastpublidate_2020_cve_sh_score10=0
count_lastpublidate_2019_cve_sh_score10=0
count_lastpublidate_2018_cve_sh_score10=0


#Compruebo la PUNTUACION BASE CVE CVSS3 y despues el anio de PUBLICACION para SMART HOME

for j in range(0,len(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"])):
    if(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"][j]!="NONE"):
        if(((float(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"][j])) < 10.0) and ((float(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"][j])) >=9.0)):
            CV3_BASE_score_9_sh+=1
            str_anio_publidate_cve_sh=df_cve_sh["CVE_Items.publishedDate"][j].split("-")
            anio_publidate_cve_sh=int(str_anio_publidate_cve_sh[0])
            if(anio_publidate_cve_sh >= 2023):
                count_lastpublidate_2023_cve_sh_score9+=1
            elif(anio_publidate_cve_sh >= 2022):
                count_lastpublidate_2022_cve_sh_score9+=1
            elif(anio_publidate_cve_sh >= 2021):
                count_lastpublidate_2021_cve_sh_score9+=1
            elif(anio_publidate_cve_sh >= 2020):
                count_lastpublidate_2020_cve_sh_score9+=1
            elif(anio_publidate_cve_sh >= 2019):
                count_lastpublidate_2019_cve_sh_score9+=1
            else:
                count_lastpublidate_2018_cve_sh_score9+=1
        elif(((float(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"][j])) < 9.0) and ((float(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"][j])) >=8.0)):
            CV3_BASE_score_8_sh+=1
            str_anio_publidate_cve_sh=df_cve_sh["CVE_Items.publishedDate"][j].split("-")
            anio_publidate_cve_sh=int(str_anio_publidate_cve_sh[0])
            if(anio_publidate_cve_sh >= 2023):
                count_lastpublidate_2023_cve_sh_score8+=1
            elif(anio_publidate_cve_sh >= 2022):
                count_lastpublidate_2022_cve_sh_score8+=1
            elif(anio_publidate_cve_sh >= 2021):
                count_lastpublidate_2021_cve_sh_score8+=1
            elif(anio_publidate_cve_sh >= 2020):
                count_lastpublidate_2020_cve_sh_score8+=1
            elif(anio_publidate_cve_sh >= 2019):
                count_lastpublidate_2019_cve_sh_score8+=1
            else:
                count_lastpublidate_2018_cve_sh_score8+=1
        elif(((float(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"][j])) < 8.0) and ((float(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"][j])) >=7.0)):
            CV3_BASE_score_7_sh+=1
            str_anio_publidate_cve_sh=df_cve_sh["CVE_Items.publishedDate"][j].split("-")
            anio_publidate_cve_sh=int(str_anio_publidate_cve_sh[0])
            if(anio_publidate_cve_sh >= 2023):
                count_lastpublidate_2023_cve_sh_score7+=1
            elif(anio_publidate_cve_sh >= 2022):
                count_lastpublidate_2022_cve_sh_score7+=1
            elif(anio_publidate_cve_sh >= 2021):
                count_lastpublidate_2021_cve_sh_score7+=1
            elif(anio_publidate_cve_sh >= 2020):
                count_lastpublidate_2020_cve_sh_score7+=1
            elif(anio_publidate_cve_sh >= 2019):
                count_lastpublidate_2019_cve_sh_score7+=1
            else:
                count_lastpublidate_2018_cve_sh_score7+=1
        elif(((float(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"][j])) < 7.0) and ((float(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"][j])) >=6.0)):
            CV3_BASE_score_6_sh+=1
            str_anio_publidate_cve_sh=df_cve_sh["CVE_Items.publishedDate"][j].split("-")
            anio_publidate_cve_sh=int(str_anio_publidate_cve_sh[0])
            if(anio_publidate_cve_sh >= 2023):
                count_lastpublidate_2023_cve_sh_score6+=1
            elif(anio_publidate_cve_sh >= 2022):
                count_lastpublidate_2022_cve_sh_score6+=1
            elif(anio_publidate_cve_sh >= 2021):
                count_lastpublidate_2021_cve_sh_score6+=1
            elif(anio_publidate_cve_sh >= 2020):
                count_lastpublidate_2020_cve_sh_score6+=1
            elif(anio_publidate_cve_sh >= 2019):
                count_lastpublidate_2019_cve_sh_score6+=1
            else:
                count_lastpublidate_2018_cve_sh_score6+=1
        elif(((float(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"][j])) < 6.0) and ((float(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"][j])) >=5.0)):
            CV3_BASE_score_5_sh+=1
            str_anio_publidate_cve_sh=df_cve_sh["CVE_Items.publishedDate"][j].split("-")
            anio_publidate_cve_sh=int(str_anio_publidate_cve_sh[0])
            if(anio_publidate_cve_sh >= 2023):
                count_lastpublidate_2023_cve_sh_score5+=1
            elif(anio_publidate_cve_sh >= 2022):
                count_lastpublidate_2022_cve_sh_score5+=1
            elif(anio_publidate_cve_sh >= 2021):
                count_lastpublidate_2021_cve_sh_score5+=1
            elif(anio_publidate_cve_sh >= 2020):
                count_lastpublidate_2020_cve_sh_score5+=1
            elif(anio_publidate_cve_sh >= 2019):
                count_lastpublidate_2019_cve_sh_score5+=1
            else:
                count_lastpublidate_2018_cve_sh_score5+=1
        elif(((float(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"][j])) < 5.0) and ((float(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"][j])) >=4.0)):
            CV3_BASE_score_4_sh+=1
            str_anio_publidate_cve_sh=df_cve_sh["CVE_Items.publishedDate"][j].split("-")
            anio_publidate_cve_sh=int(str_anio_publidate_cve_sh[0])
            if(anio_publidate_cve_sh >= 2023):
                count_lastpublidate_2023_cve_sh_score4+=1
            elif(anio_publidate_cve_sh >= 2022):
                count_lastpublidate_2022_cve_sh_score4+=1
            elif(anio_publidate_cve_sh >= 2021):
                count_lastpublidate_2021_cve_sh_score4+=1
            elif(anio_publidate_cve_sh >= 2020):
                count_lastpublidate_2020_cve_sh_score4+=1
            elif(anio_publidate_cve_sh >= 2019):
                count_lastpublidate_2019_cve_sh_score4+=1
            else:
                count_lastpublidate_2018_cve_sh_score4+=1
        elif(((float(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"][j])) < 4.0) and ((float(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"][j])) >=3.0)):
            CV3_BASE_score_3_sh+=1
            str_anio_publidate_cve_sh=df_cve_sh["CVE_Items.publishedDate"][j].split("-")
            anio_publidate_cve_sh=int(str_anio_publidate_cve_sh[0])
            if(anio_publidate_cve_sh >= 2023):
                count_lastpublidate_2023_cve_sh_score3+=1
            elif(anio_publidate_cve_sh >= 2022):
                count_lastpublidate_2022_cve_sh_score3+=1
            elif(anio_publidate_cve_sh >= 2021):
                count_lastpublidate_2021_cve_sh_score3+=1
            elif(anio_publidate_cve_sh >= 2020):
                count_lastpublidate_2020_cve_sh_score3+=1
            elif(anio_publidate_cve_sh >= 2019):
                count_lastpublidate_2019_cve_sh_score3+=1
            else:
                count_lastpublidate_2018_cve_sh_score3+=1
        elif(((float(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"][j])) < 3.0) and ((float(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"][j])) >=2.0)):
            CV3_BASE_score_2_sh+=1
            str_anio_publidate_cve_sh=df_cve_sh["CVE_Items.publishedDate"][j].split("-")
            anio_publidate_cve_sh=int(str_anio_publidate_cve_sh[0])
            if(anio_publidate_cve_sh >= 2023):
                count_lastpublidate_2023_cve_sh_score2+=1
            elif(anio_publidate_cve_sh >= 2022):
                count_lastpublidate_2022_cve_sh_score2+=1
            elif(anio_publidate_cve_sh >= 2021):
                count_lastpublidate_2021_cve_sh_score2+=1
            elif(anio_publidate_cve_sh >= 2020):
                count_lastpublidate_2020_cve_sh_score2+=1
            elif(anio_publidate_cve_sh >= 2019):
                count_lastpublidate_2019_cve_sh_score2+=1
            else:
                count_lastpublidate_2018_cve_sh_score2+=1
        elif(((float(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"][j])) < 2.0) and ((float(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"][j])) >=1.0)):
            CV3_BASE_score_1_sh+=1
            str_anio_publidate_cve_sh=df_cve_sh["CVE_Items.publishedDate"][j].split("-")
            anio_publidate_cve_sh=int(str_anio_publidate_cve_sh[0])
            if(anio_publidate_cve_sh >= 2023):
                count_lastpublidate_2023_cve_sh_score1+=1
            elif(anio_publidate_cve_sh >= 2022):
                count_lastpublidate_2022_cve_sh_score1+=1
            elif(anio_publidate_cve_sh >= 2021):
                count_lastpublidate_2021_cve_sh_score1+=1
            elif(anio_publidate_cve_sh >= 2020):
                count_lastpublidate_2020_cve_sh_score1+=1
            elif(anio_publidate_cve_sh >= 2019):
                count_lastpublidate_2019_cve_sh_score1+=1
            else:
                count_lastpublidate_2018_cve_sh_score1+=1
        elif(((float(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"][j])) < 1.0) and ((float(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"][j])) >=0.0)):
            CV3_BASE_score_0_sh+=1
            str_anio_publidate_cve_sh=df_cve_sh["CVE_Items.publishedDate"][j].split("-")
            anio_publidate_cve_sh=int(str_anio_publidate_cve_sh[0])
            if(anio_publidate_cve_sh >= 2023):
                count_lastpublidate_2023_cve_sh_score0+=1
            elif(anio_publidate_cve_sh >= 2022):
                count_lastpublidate_2022_cve_sh_score0+=1
            elif(anio_publidate_cve_sh >= 2021):
                count_lastpublidate_2021_cve_sh_score0+=1
            elif(anio_publidate_cve_sh >= 2020):
                count_lastpublidate_2020_cve_sh_score0+=1
            elif(anio_publidate_cve_sh >= 2019):
                count_lastpublidate_2019_cve_sh_score0+=1
            else:
                count_lastpublidate_2018_cve_sh_score0+=1
        elif(((float(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"][j])) == 10.0)):
            CV3_BASE_score_10_sh+=1
            str_anio_publidate_cve_sh=df_cve_sh["CVE_Items.publishedDate"][j].split("-")
            anio_publidate_cve_sh=int(str_anio_publidate_cve_sh[0])
            if(anio_publidate_cve_sh >= 2023):
                count_lastpublidate_2023_cve_sh_score10+=1
            elif(anio_publidate_cve_sh >= 2022):
                count_lastpublidate_2022_cve_sh_score10+=1
            elif(anio_publidate_cve_sh >= 2021):
                count_lastpublidate_2021_cve_sh_score10+=1
            elif(anio_publidate_cve_sh >= 2020):
                count_lastpublidate_2020_cve_sh_score10+=1
            elif(anio_publidate_cve_sh >= 2019):
                count_lastpublidate_2019_cve_sh_score10+=1
            else:
                count_lastpublidate_2018_cve_sh_score10+=1
    
print("************************** ESTADÍSTICAS PUNTUACION BASE/AÑO DE PUBLICACION EN CVE CVSSV3 SMART HOME********************************")
print("\n")
print("\n")
print("DE UN TOTAL DE "+str(len(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"]))+" VULNERABILIDADES, LAS ESTADÍSTICAS DE FECHA DE FECHA DE PUBLICACIÓN DE LAS VULNERABILIDADES SEGÚN SU PUNTUACIÓN BASE SON LAS SIGUIENTES :  \n")
print("\n")

print(" -  EN "+str(CV3_BASE_score_10_sh)+" VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
print("       -     EN "+str(count_lastpublidate_2023_cve_sh_score10)+" VULNERABILIDADES PUBLICADAS EN 2023 LA PUNTUACION BASE ES 10 \n")
print("       -     EN "+str(count_lastpublidate_2022_cve_sh_score10)+" VULNERABILIDADES PUBLICADAS EN 2022 LA PUNTUACION BASE ES 10 \n")
print("       -     EN "+str(count_lastpublidate_2021_cve_sh_score10)+" VULNERABILIDADES PUBLICADAS EN 2021 LA PUNTUACION BASE ES 10 \n")
print("       -     EN "+str(count_lastpublidate_2020_cve_sh_score10)+" VULNERABILIDADES PUBLICADAS EN 2020 LA PUNTUACION BASE ES 10 \n")
print("       -     EN "+str(count_lastpublidate_2019_cve_sh_score10)+" VULNERABILIDADES PUBLICADAS EN 2019 LA PUNTUACION BASE ES 10 \n")
print("       -     EN "+str(count_lastpublidate_2018_cve_sh_score10)+" VULNERABILIDADES PUBLICADAS EN 2018 O ANTES LA PUNTUACION BASE ES 10 \n")

print(" -  EN "+str(CV3_BASE_score_9_sh)+" VULNERABILIDADES LA PUNTUACION BASE ESTÁ ENTRE 9 Y 10 \n")
print("       -     EN "+str(count_lastpublidate_2023_cve_sh_score9)+" VULNERABILIDADES PUBLICADAS EN 2023 LA PUNTUACION BASE ESTÁ ENTRE 9 Y 10 \n")
print("       -     EN "+str(count_lastpublidate_2022_cve_sh_score9)+" VULNERABILIDADES PUBLICADAS EN 2022 LA PUNTUACION BASE ESTÁ ENTRE 9 Y 10 \n")
print("       -     EN "+str(count_lastpublidate_2021_cve_sh_score9)+" VULNERABILIDADES PUBLICADAS EN 2021 LA PUNTUACION BASE ESTÁ ENTRE 9 Y 10 \n")
print("       -     EN "+str(count_lastpublidate_2020_cve_sh_score9)+" VULNERABILIDADES PUBLICADAS EN 2020 LA PUNTUACION BASE ESTÁ ENTRE 9 Y 10 \n")
print("       -     EN "+str(count_lastpublidate_2019_cve_sh_score9)+" VULNERABILIDADES PUBLICADAS EN 2019 LA PUNTUACION BASE ESTÁ ENTRE 9 Y 10 \n")
print("       -     EN "+str(count_lastpublidate_2018_cve_sh_score9)+" VULNERABILIDADES PUBLICADAS EN 2018 O ANTES LA PUNTUACION BASE ESTÁ ENTRE 9 Y 10 \n")

print(" -  EN "+str(CV3_BASE_score_8_sh)+" VULNERABILIDADES LA PUNTUACION BASE ESTÁ ENTRE 8 Y 9 \n")
print("       -     EN "+str(count_lastpublidate_2023_cve_sh_score8)+" VULNERABILIDADES PUBLICADAS EN 2023 LA PUNTUACION BASE ESTÁ ENTRE 8 Y 9 \n")
print("       -     EN "+str(count_lastpublidate_2022_cve_sh_score8)+" VULNERABILIDADES PUBLICADAS EN 2022 LA PUNTUACION BASE ESTÁ ENTRE 8 Y 9 \n")
print("       -     EN "+str(count_lastpublidate_2021_cve_sh_score8)+" VULNERABILIDADES PUBLICADAS EN 2021 LA PUNTUACION BASE ESTÁ ENTRE 8 Y 9 \n")
print("       -     EN "+str(count_lastpublidate_2020_cve_sh_score8)+" VULNERABILIDADES PUBLICADAS EN 2020 LA PUNTUACION BASE ESTÁ ENTRE 8 Y 9 \n")
print("       -     EN "+str(count_lastpublidate_2019_cve_sh_score8)+" VULNERABILIDADES PUBLICADAS EN 2019 LA PUNTUACION BASE ESTÁ ENTRE 8 Y 9 \n")
print("       -     EN "+str(count_lastpublidate_2018_cve_sh_score8)+" VULNERABILIDADES PUBLICADAS EN 2018 O ANTES LA PUNTUACION BASE ESTÁ ENTRE 8 Y 9 \n")

print(" -  EN "+str(CV3_BASE_score_7_sh)+" VULNERABILIDADES LA PUNTUACION BASE ESTÁ ENTRE 7 Y 8 \n")
print("       -     EN "+str(count_lastpublidate_2023_cve_sh_score7)+" VULNERABILIDADES PUBLICADAS EN 2023 LA PUNTUACION BASE ESTÁ ENTRE 7 Y 8 \n")
print("       -     EN "+str(count_lastpublidate_2022_cve_sh_score7)+" VULNERABILIDADES PUBLICADAS EN 2022 LA PUNTUACION BASE ESTÁ ENTRE 7 Y 8 \n")
print("       -     EN "+str(count_lastpublidate_2021_cve_sh_score7)+" VULNERABILIDADES PUBLICADAS EN 2021 LA PUNTUACION BASE ESTÁ ENTRE 7 Y 8 \n")
print("       -     EN "+str(count_lastpublidate_2020_cve_sh_score7)+" VULNERABILIDADES PUBLICADAS EN 2020 LA PUNTUACION BASE ESTÁ ENTRE 7 Y 8 \n")
print("       -     EN "+str(count_lastpublidate_2019_cve_sh_score7)+" VULNERABILIDADES PUBLICADAS EN 2019 LA PUNTUACION BASE ESTÁ ENTRE 7 Y 8 \n")
print("       -     EN "+str(count_lastpublidate_2018_cve_sh_score7)+" VULNERABILIDADES PUBLICADAS EN 2018 O ANTES LA PUNTUACION BASE ESTÁ ENTRE 7 Y 8 \n")

print(" -  EN "+str(CV3_BASE_score_6_sh)+" VULNERABILIDADES LA PUNTUACION BASE ESTÁ ENTRE 6 y 7 \n")
print("       -     EN "+str(count_lastpublidate_2023_cve_sh_score6)+" VULNERABILIDADES PUBLICADAS EN 2023 LA PUNTUACION BASE ESTÁ ENTRE 6 y 7 \n")
print("       -     EN "+str(count_lastpublidate_2022_cve_sh_score6)+" VULNERABILIDADES PUBLICADAS EN 2022 LA PUNTUACION BASE ESTÁ ENTRE 6 y 7 \n")
print("       -     EN "+str(count_lastpublidate_2021_cve_sh_score6)+" VULNERABILIDADES PUBLICADAS EN 2021 LA PUNTUACION BASE ESTÁ ENTRE 6 y 7 \n")
print("       -     EN "+str(count_lastpublidate_2020_cve_sh_score6)+" VULNERABILIDADES PUBLICADAS EN 2020 LA PUNTUACION BASE ESTÁ ENTRE 6 y 7 \n")
print("       -     EN "+str(count_lastpublidate_2019_cve_sh_score6)+" VULNERABILIDADES PUBLICADAS EN 2019 LA PUNTUACION BASE ESTÁ ENTRE 6 y 7 \n")
print("       -     EN "+str(count_lastpublidate_2018_cve_sh_score6)+" VULNERABILIDADES PUBLICADAS EN 2018 O ANTES LA PUNTUACION BASE ESTÁ ENTRE 6 y 7 \n")

print(" -  EN "+str(CV3_BASE_score_5_sh)+" VULNERABILIDADES LA PUNTUACION BASE ESTÁ ENTRE 5 y 6 \n")
print("       -     EN "+str(count_lastpublidate_2023_cve_sh_score5)+" VULNERABILIDADES PUBLICADAS EN 2023 LA PUNTUACION BASE ESTÁ ENTRE 5 y 6 \n")
print("       -     EN "+str(count_lastpublidate_2022_cve_sh_score5)+" VULNERABILIDADES PUBLICADAS EN 2022 LA PUNTUACION BASE ESTÁ ENTRE 5 y 6 \n")
print("       -     EN "+str(count_lastpublidate_2021_cve_sh_score5)+" VULNERABILIDADES PUBLICADAS EN 2021 LA PUNTUACION BASE ESTÁ ENTRE 5 y 6 \n")
print("       -     EN "+str(count_lastpublidate_2020_cve_sh_score5)+" VULNERABILIDADES PUBLICADAS EN 2020 LA PUNTUACION BASE ESTÁ ENTRE 5 y 6 \n")
print("       -     EN "+str(count_lastpublidate_2019_cve_sh_score5)+" VULNERABILIDADES PUBLICADAS EN 2019 LA PUNTUACION BASE ESTÁ ENTRE 5 y 6 \n")
print("       -     EN "+str(count_lastpublidate_2018_cve_sh_score5)+" VULNERABILIDADES PUBLICADAS EN 2018 O ANTES LA PUNTUACION BASE ESTÁ ENTRE 5 y 6 \n")

print(" -  EN "+str(CV3_BASE_score_4_sh)+" VULNERABILIDADES LA PUNTUACION BASE ESTÁ ENTRE 4 y 5 \n")
print("       -     EN "+str(count_lastpublidate_2023_cve_sh_score4)+" VULNERABILIDADES PUBLICADAS EN 2023 LA PUNTUACION BASE ESTÁ ENTRE 4 y 5 \n")
print("       -     EN "+str(count_lastpublidate_2022_cve_sh_score4)+" VULNERABILIDADES PUBLICADAS EN 2022 LA PUNTUACION BASE ESTÁ ENTRE 4 y 5 \n")
print("       -     EN "+str(count_lastpublidate_2021_cve_sh_score4)+" VULNERABILIDADES PUBLICADAS EN 2021 LA PUNTUACION BASE ESTÁ ENTRE 4 y 5 \n")
print("       -     EN "+str(count_lastpublidate_2020_cve_sh_score4)+" VULNERABILIDADES PUBLICADAS EN 2020 LA PUNTUACION BASE ESTÁ ENTRE 4 y 5 \n")
print("       -     EN "+str(count_lastpublidate_2019_cve_sh_score4)+" VULNERABILIDADES PUBLICADAS EN 2019 LA PUNTUACION BASE ESTÁ ENTRE 4 y 5 \n")
print("       -     EN "+str(count_lastpublidate_2018_cve_sh_score4)+" VULNERABILIDADES PUBLICADAS EN 2018 O ANTES LA PUNTUACION BASE ESTÁ ENTRE 4 y 5 \n")

print(" -  EN "+str(CV3_BASE_score_3_sh)+" VULNERABILIDADES LA PUNTUACION BASE ESTÁ ENTRE 3 y 4 \n")
print("       -     EN "+str(count_lastpublidate_2023_cve_sh_score3)+" VULNERABILIDADES PUBLICADAS EN 2023 LA PUNTUACION BASE ESTÁ ENTRE 3 y 4 \n")
print("       -     EN "+str(count_lastpublidate_2022_cve_sh_score3)+" VULNERABILIDADES PUBLICADAS EN 2022 LA PUNTUACION BASE ESTÁ ENTRE 3 y 4 \n")
print("       -     EN "+str(count_lastpublidate_2021_cve_sh_score3)+" VULNERABILIDADES PUBLICADAS EN 2021 LA PUNTUACION BASE ESTÁ ENTRE 3 y 4 \n")
print("       -     EN "+str(count_lastpublidate_2020_cve_sh_score3)+" VULNERABILIDADES PUBLICADAS EN 2020 LA PUNTUACION BASE ESTÁ ENTRE 3 y 4 \n")
print("       -     EN "+str(count_lastpublidate_2019_cve_sh_score3)+" VULNERABILIDADES PUBLICADAS EN 2019 LA PUNTUACION BASE ESTÁ ENTRE 3 y 4 \n")
print("       -     EN "+str(count_lastpublidate_2018_cve_sh_score3)+" VULNERABILIDADES PUBLICADAS EN 2018 O ANTES LA PUNTUACION BASE ESTÁ ENTRE 3 y 4 \n")

print(" -  EN "+str(CV3_BASE_score_2_sh)+" VULNERABILIDADES LA PUNTUACION BASE ESTÁ ENTRE 2 y 3 \n")
print("       -     EN "+str(count_lastpublidate_2023_cve_sh_score2)+" VULNERABILIDADES PUBLICADAS EN 2023 LA PUNTUACION BASE ESTÁ ENTRE 2 y 3 \n")
print("       -     EN "+str(count_lastpublidate_2022_cve_sh_score2)+" VULNERABILIDADES PUBLICADAS EN 2022 LA PUNTUACION BASE ESTÁ ENTRE 2 y 3 \n")
print("       -     EN "+str(count_lastpublidate_2021_cve_sh_score2)+" VULNERABILIDADES PUBLICADAS EN 2021 LA PUNTUACION BASE ESTÁ ENTRE 2 y 3 \n")
print("       -     EN "+str(count_lastpublidate_2020_cve_sh_score2)+" VULNERABILIDADES PUBLICADAS EN 2020 LA PUNTUACION BASE ESTÁ ENTRE 2 y 3 \n")
print("       -     EN "+str(count_lastpublidate_2019_cve_sh_score2)+" VULNERABILIDADES PUBLICADAS EN 2019 LA PUNTUACION BASE ESTÁ ENTRE 2 y 3 \n")
print("       -     EN "+str(count_lastpublidate_2018_cve_sh_score2)+" VULNERABILIDADES PUBLICADAS EN 2018 O ANTES LA PUNTUACION BASE ESTÁ ENTRE 2 y 3 \n")

print(" -  EN "+str(CV3_BASE_score_1_sh)+" VULNERABILIDADES LA PUNTUACION BASE ESTÁ ENTRE 1 y 2 \n")
print("       -     EN "+str(count_lastpublidate_2023_cve_sh_score1)+" VULNERABILIDADES PUBLICADAS EN 2023 LA PUNTUACION BASE ESTÁ ENTRE 1 y 2 \n")
print("       -     EN "+str(count_lastpublidate_2022_cve_sh_score1)+" VULNERABILIDADES PUBLICADAS EN 2022 LA PUNTUACION BASE ESTÁ ENTRE 1 y 2 \n")
print("       -     EN "+str(count_lastpublidate_2021_cve_sh_score1)+" VULNERABILIDADES PUBLICADAS EN 2021 LA PUNTUACION BASE ESTÁ ENTRE 1 y 2 \n")
print("       -     EN "+str(count_lastpublidate_2020_cve_sh_score1)+" VULNERABILIDADES PUBLICADAS EN 2020 LA PUNTUACION BASE ESTÁ ENTRE 1 y 2 \n")
print("       -     EN "+str(count_lastpublidate_2019_cve_sh_score1)+" VULNERABILIDADES PUBLICADAS EN 2019 LA PUNTUACION BASE ESTÁ ENTRE 1 y 2 \n")
print("       -     EN "+str(count_lastpublidate_2018_cve_sh_score1)+" VULNERABILIDADES PUBLICADAS EN 2018 O ANTES LA PUNTUACION BASE ESTÁ ENTRE 1 y 2 \n")

print(" -  EN "+str(CV3_BASE_score_0_sh)+" VULNERABILIDADES LA PUNTUACION BASE ESTÁ ENTRE 0 y 1 \n")
print("       -     EN "+str(count_lastpublidate_2023_cve_sh_score0)+" VULNERABILIDADES PUBLICADAS EN 2023 LA PUNTUACION BASE ESTÁ ENTRE 0 y 1 \n")
print("       -     EN "+str(count_lastpublidate_2022_cve_sh_score0)+" VULNERABILIDADES PUBLICADAS EN 2022 LA PUNTUACION BASE ESTÁ ENTRE 0 y 1 \n")
print("       -     EN "+str(count_lastpublidate_2021_cve_sh_score0)+" VULNERABILIDADES PUBLICADAS EN 2021 LA PUNTUACION BASE ESTÁ ENTRE 0 y 1 \n")
print("       -     EN "+str(count_lastpublidate_2020_cve_sh_score0)+" VULNERABILIDADES PUBLICADAS EN 2020 LA PUNTUACION BASE ESTÁ ENTRE 0 y 1 \n")
print("       -     EN "+str(count_lastpublidate_2019_cve_sh_score0)+" VULNERABILIDADES PUBLICADAS EN 2019 LA PUNTUACION BASE ESTÁ ENTRE 0 y 1 \n")
print("       -     EN "+str(count_lastpublidate_2018_cve_sh_score0)+" VULNERABILIDADES PUBLICADAS EN 2018 O ANTES LA PUNTUACION BASE ESTÁ ENTRE 0 y 1 \n")
print("\n")
print("***************************PORCENTAJE PUNTUACION BASE/AÑO DE PUBLICACION EN CVE CVSSV3 SMART HOME********************************")
print("\n")
print("\n")
print("DE UN TOTAL DE "+str(len(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"]))+" VULNERABILIDADES, LOS PORCENTAJES DE FECHA DE PUBLICACIÓN DE LAS VULNERABILIDADES SEGÚN SU PUNTUACIÓN BASE SON LOS SIGUIENTES :  \n")
print("\n")
if(CV3_BASE_score_10_sh>0):
    print(" -  EN EL "+str(float(((CV3_BASE_score_10_sh*100)/len(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"]))))+"% DE LAS VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
    print("       -     EN EL "+str(float(((count_lastpublidate_2023_cve_sh_score10*100)/CV3_BASE_score_10_sh)))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2023 LA PUNTUACION BASE ES 10 \n")
    print("       -     EN EL "+str(float(((count_lastpublidate_2022_cve_sh_score10*100)/CV3_BASE_score_10_sh)))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2022 LA PUNTUACION BASE ES 10 \n")
    print("       -     EN EL "+str(float(((count_lastpublidate_2021_cve_sh_score10*100)/CV3_BASE_score_10_sh)))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2021 LA PUNTUACION BASE ES 10 \n")
    print("       -     EN EL "+str(float(((count_lastpublidate_2020_cve_sh_score10*100)/CV3_BASE_score_10_sh)))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2020 LA PUNTUACION BASE ES 10 \n")
    print("       -     EN EL "+str(float(((count_lastpublidate_2019_cve_sh_score10*100)/CV3_BASE_score_10_sh)))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2019 LA PUNTUACION BASE ES 10 \n")
    print("       -     EN EL "+str(float(((count_lastpublidate_2018_cve_sh_score10*100)/CV3_BASE_score_10_sh)))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2018 O ANTERIORMENTE LA PUNTUACION BASE ES 10 \n")
    
if(CV3_BASE_score_9_sh>0):
    print(" -  EN EL "+str(float(((CV3_BASE_score_9_sh*100)/len(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"]))))+"% DE LAS VULNERABILIDADES LA PUNTUACION BASE ESTÁ ENTRE 9 Y 10 \n")
    print("       -     EN EL "+str(float(((count_lastpublidate_2023_cve_sh_score9*100)/CV3_BASE_score_9_sh)))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2023 LA PUNTUACION BASE ESTÁ ENTRE 9 Y 10 \n")
    print("       -     EN EL "+str(float(((count_lastpublidate_2022_cve_sh_score9*100)/CV3_BASE_score_9_sh)))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2022 LA PUNTUACION BASE ESTÁ ENTRE 9 Y 10 \n")
    print("       -     EN EL "+str(float(((count_lastpublidate_2021_cve_sh_score9*100)/CV3_BASE_score_9_sh)))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2021 LA PUNTUACION BASE ESTÁ ENTRE 9 Y 10 \n")
    print("       -     EN EL "+str(float(((count_lastpublidate_2020_cve_sh_score9*100)/CV3_BASE_score_9_sh)))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2020 LA PUNTUACION BASE ESTÁ ENTRE 9 Y 10 \n")
    print("       -     EN EL "+str(float(((count_lastpublidate_2019_cve_sh_score9*100)/CV3_BASE_score_9_sh)))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2019 LA PUNTUACION BASE ESTÁ ENTRE 9 Y 10 \n")
    print("       -     EN EL "+str(float(((count_lastpublidate_2018_cve_sh_score9*100)/CV3_BASE_score_9_sh)))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2018 O ANTERIORMENTE LA PUNTUACION BASE ESTÁ ENTRE 9 Y 10 \n")


if(CV3_BASE_score_8_sh>0):
    print(" -  EN EL "+str(float(((CV3_BASE_score_8_sh*100)/len(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"]))))+"% DE LAS VULNERABILIDADES LA PUNTUACION BASE ESTÁ ENTRE 8 y 9 \n")
    print("       -     EN EL "+str(float(((count_lastpublidate_2023_cve_sh_score8*100)/CV3_BASE_score_8_sh)))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2023 LA PUNTUACION BASE ESTÁ ENTRE 8 y 9 \n")
    print("       -     EN EL "+str(float(((count_lastpublidate_2022_cve_sh_score8*100)/CV3_BASE_score_8_sh)))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2022 LA PUNTUACION BASE ESTÁ ENTRE 8 y 9 \n")
    print("       -     EN EL "+str(float(((count_lastpublidate_2021_cve_sh_score8*100)/CV3_BASE_score_8_sh)))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2021 LA PUNTUACION BASE ESTÁ ENTRE 8 y 9 \n")
    print("       -     EN EL "+str(float(((count_lastpublidate_2020_cve_sh_score8*100)/CV3_BASE_score_8_sh)))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2020 LA PUNTUACION BASE ESTÁ ENTRE 8 y 9 \n")
    print("       -     EN EL "+str(float(((count_lastpublidate_2019_cve_sh_score8*100)/CV3_BASE_score_8_sh)))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2019 LA PUNTUACION BASE ESTÁ ENTRE 8 y 9 \n")
    print("       -     EN EL "+str(float(((count_lastpublidate_2018_cve_sh_score8*100)/CV3_BASE_score_8_sh)))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2018 O ANTERIORMENTE LA PUNTUACION BASE ESTÁ ENTRE 8 y 9 \n")

if(CV3_BASE_score_7_sh>0):
    print(" -  EN EL "+str(float(((CV3_BASE_score_7_sh*100)/len(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"]))))+"% DE LAS VULNERABILIDADES LA PUNTUACION BASE ESTÁ ENTRE 7 y 8 \n")
    print("       -     EN EL "+str(float(((count_lastpublidate_2023_cve_sh_score7*100)/CV3_BASE_score_7_sh)))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2023 LA PUNTUACION BASE ESTÁ ENTRE 7 y 8 \n")
    print("       -     EN EL "+str(float(((count_lastpublidate_2022_cve_sh_score7*100)/CV3_BASE_score_7_sh)))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2022 LA PUNTUACION BASE ESTÁ ENTRE 7 y 8 \n")
    print("       -     EN EL "+str(float(((count_lastpublidate_2021_cve_sh_score7*100)/CV3_BASE_score_7_sh)))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2021 LA PUNTUACION BASE ESTÁ ENTRE 7 y 8 \n")
    print("       -     EN EL "+str(float(((count_lastpublidate_2020_cve_sh_score7*100)/CV3_BASE_score_7_sh)))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2020 LA PUNTUACION BASE ESTÁ ENTRE 7 y 8 \n")
    print("       -     EN EL "+str(float(((count_lastpublidate_2019_cve_sh_score7*100)/CV3_BASE_score_7_sh)))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2019 LA PUNTUACION BASE ESTÁ ENTRE 7 y 8 \n")
    print("       -     EN EL "+str(float(((count_lastpublidate_2018_cve_sh_score7*100)/CV3_BASE_score_7_sh)))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2018 O ANTERIORMENTE LA PUNTUACION BASE ESTÁ ENTRE 7 y 8 \n")
if(CV3_BASE_score_6_sh>0):
    print(" -  EN EL "+str(float(((CV3_BASE_score_6_sh*100)/len(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"]))))+"% DE LAS VULNERABILIDADES LA PUNTUACION BASE ESTÁ ENTRE 6 y 7 \n")
    print("       -     EN EL "+str(float(((count_lastpublidate_2023_cve_sh_score6*100)/CV3_BASE_score_6_sh)))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2023 LA PUNTUACION BASE ESTÁ ENTRE 6 y 7 \n")
    print("       -     EN EL "+str(float(((count_lastpublidate_2022_cve_sh_score6*100)/CV3_BASE_score_6_sh)))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2022 LA PUNTUACION BASE ESTÁ ENTRE 6 y 7 \n")
    print("       -     EN EL "+str(float(((count_lastpublidate_2021_cve_sh_score6*100)/CV3_BASE_score_6_sh)))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2021 LA PUNTUACION BASE ESTÁ ENTRE 6 y 7 \n")
    print("       -     EN EL "+str(float(((count_lastpublidate_2020_cve_sh_score6*100)/CV3_BASE_score_6_sh)))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2020 LA PUNTUACION BASE ESTÁ ENTRE 6 y 7 \n")
    print("       -     EN EL "+str(float(((count_lastpublidate_2019_cve_sh_score6*100)/CV3_BASE_score_6_sh)))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2019 LA PUNTUACION BASE ESTÁ ENTRE 6 y 7 \n")
    print("       -     EN EL "+str(float(((count_lastpublidate_2018_cve_sh_score6*100)/CV3_BASE_score_6_sh)))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2018 O ANTERIORMENTE LA PUNTUACION BASE ESTÁ ENTRE 6 y 7 \n")
if(CV3_BASE_score_5_sh>0):
    print(" -  EN EL "+str(float(((CV3_BASE_score_5_sh*100)/len(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"]))))+"% DE LAS VULNERABILIDADES LA PUNTUACION BASE ESTÁ ENTRE 5 y 6 \n")
    print("       -     EN EL "+str(float(((count_lastpublidate_2023_cve_sh_score5*100)/CV3_BASE_score_5_sh)))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2023 LA PUNTUACION BASE ESTÁ ENTRE 5 y 6 \n")
    print("       -     EN EL "+str(float(((count_lastpublidate_2022_cve_sh_score5*100)/CV3_BASE_score_5_sh)))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2022 LA PUNTUACION BASE ESTÁ ENTRE 5 y 6 \n")
    print("       -     EN EL "+str(float(((count_lastpublidate_2021_cve_sh_score5*100)/CV3_BASE_score_5_sh)))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2021 LA PUNTUACION BASE ESTÁ ENTRE 5 y 6 \n")
    print("       -     EN EL "+str(float(((count_lastpublidate_2020_cve_sh_score5*100)/CV3_BASE_score_5_sh)))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2020 LA PUNTUACION BASE ESTÁ ENTRE 5 y 6 \n")
    print("       -     EN EL "+str(float(((count_lastpublidate_2019_cve_sh_score5*100)/CV3_BASE_score_5_sh)))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2019 LA PUNTUACION BASE ESTÁ ENTRE 5 y 6 \n")
    print("       -     EN EL "+str(float(((count_lastpublidate_2018_cve_sh_score5*100)/CV3_BASE_score_5_sh)))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2018 O ANTERIORMENTE LA PUNTUACION BASE ESTÁ ENTRE 5 y 6 \n")
if(CV3_BASE_score_4_sh>0):
    print(" -  EN EL "+str(float(((CV3_BASE_score_4_sh*100)/len(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"]))))+"% DE LAS VULNERABILIDADES LA PUNTUACION BASE ESTÁ ENTRE 4 y 5 \n")
    print("       -     EN EL "+str(float(((count_lastpublidate_2023_cve_sh_score4*100)/CV3_BASE_score_4_sh)))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2023 LA PUNTUACION BASE ESTÁ ENTRE 4 y 5 \n")
    print("       -     EN EL "+str(float(((count_lastpublidate_2022_cve_sh_score4*100)/CV3_BASE_score_4_sh)))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2022 LA PUNTUACION BASE ESTÁ ENTRE 4 y 5 \n")
    print("       -     EN EL "+str(float(((count_lastpublidate_2021_cve_sh_score4*100)/CV3_BASE_score_4_sh)))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2021 LA PUNTUACION BASE ESTÁ ENTRE 4 y 5 \n")
    print("       -     EN EL "+str(float(((count_lastpublidate_2020_cve_sh_score4*100)/CV3_BASE_score_4_sh)))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2020 LA PUNTUACION BASE ESTÁ ENTRE 4 y 5 \n")
    print("       -     EN EL "+str(float(((count_lastpublidate_2019_cve_sh_score4*100)/CV3_BASE_score_4_sh)))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2019 LA PUNTUACION BASE ESTÁ ENTRE 4 y 5 \n")
    print("       -     EN EL "+str(float(((count_lastpublidate_2018_cve_sh_score4*100)/CV3_BASE_score_4_sh)))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2018 O ANTERIORMENTE LA PUNTUACION BASE ESTÁ ENTRE 4 y 5 \n")
if(CV3_BASE_score_3_sh>0):
    print(" -  EN EL "+str(float(((CV3_BASE_score_3_sh*100)/len(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"]))))+"% DE LAS VULNERABILIDADES LA PUNTUACION BASE ESTÁ ENTRE 3 y 4 \n")
    print("       -     EN EL "+str(float(((count_lastpublidate_2023_cve_sh_score3*100)/CV3_BASE_score_3_sh)))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2023 LA PUNTUACION BASE ESTÁ ENTRE 3 y 4 \n")
    print("       -     EN EL "+str(float(((count_lastpublidate_2022_cve_sh_score3*100)/CV3_BASE_score_3_sh)))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2022 LA PUNTUACION BASE ESTÁ ENTRE 3 y 4 \n")
    print("       -     EN EL "+str(float(((count_lastpublidate_2021_cve_sh_score3*100)/CV3_BASE_score_3_sh)))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2021 LA PUNTUACION BASE ESTÁ ENTRE 3 y 4 \n")
    print("       -     EN EL "+str(float(((count_lastpublidate_2020_cve_sh_score3*100)/CV3_BASE_score_3_sh)))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2020 LA PUNTUACION BASE ESTÁ ENTRE 3 y 4 \n")
    print("       -     EN EL "+str(float(((count_lastpublidate_2019_cve_sh_score3*100)/CV3_BASE_score_3_sh)))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2019 LA PUNTUACION BASE ESTÁ ENTRE 3 y 4 \n")
    print("       -     EN EL "+str(float(((count_lastpublidate_2018_cve_sh_score3*100)/CV3_BASE_score_3_sh)))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2018 O ANTERIORMENTE LA PUNTUACION BASE ESTÁ ENTRE 3 y 4 \n")
if(CV3_BASE_score_2_sh>0):
    print(" -  EN EL "+str(float(((CV3_BASE_score_2_sh*100)/len(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"]))))+"% DE LAS VULNERABILIDADES LA PUNTUACION BASE ESTÁ ENTRE 2 y 3 \n")
    print("       -     EN EL "+str(float(((count_lastpublidate_2023_cve_sh_score2*100)/CV3_BASE_score_2_sh)))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2023 LA PUNTUACION BASE ESTÁ ENTRE 2 y 3 \n")
    print("       -     EN EL "+str(float(((count_lastpublidate_2022_cve_sh_score2*100)/CV3_BASE_score_2_sh)))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2022 LA PUNTUACION BASE ESTÁ ENTRE 2 y 3 \n")
    print("       -     EN EL "+str(float(((count_lastpublidate_2021_cve_sh_score2*100)/CV3_BASE_score_2_sh)))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2021 LA PUNTUACION BASE ESTÁ ENTRE 2 y 3 \n")
    print("       -     EN EL "+str(float(((count_lastpublidate_2020_cve_sh_score2*100)/CV3_BASE_score_2_sh)))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2020 LA PUNTUACION BASE ESTÁ ENTRE 2 y 3 \n")
    print("       -     EN EL "+str(float(((count_lastpublidate_2019_cve_sh_score2*100)/CV3_BASE_score_2_sh)))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2019 LA PUNTUACION BASE ESTÁ ENTRE 2 y 3 \n")
    print("       -     EN EL "+str(float(((count_lastpublidate_2018_cve_sh_score2*100)/CV3_BASE_score_2_sh)))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2018 O ANTERIORMENTE LA PUNTUACION BASE ESTÁ ENTRE 2 y 3 \n")
if(CV3_BASE_score_1_sh>0):
    print(" -  EN EL "+str(float(((CV3_BASE_score_1_sh*100)/len(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"]))))+"% DE LAS VULNERABILIDADES LA PUNTUACION BASE ESTÁ ENTRE 1 y 2 \n")
    print("       -     EN EL "+str(float(((count_lastpublidate_2023_cve_sh_score1*100)/CV3_BASE_score_1_sh)))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2023 LA PUNTUACION BASE ESTÁ ENTRE 1 y 2 \n")
    print("       -     EN EL "+str(float(((count_lastpublidate_2022_cve_sh_score1*100)/CV3_BASE_score_1_sh)))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2022 LA PUNTUACION BASE ESTÁ ENTRE 1 y 2 \n")
    print("       -     EN EL "+str(float(((count_lastpublidate_2021_cve_sh_score1*100)/CV3_BASE_score_1_sh)))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2021 LA PUNTUACION BASE ESTÁ ENTRE 1 y 2 \n")
    print("       -     EN EL "+str(float(((count_lastpublidate_2020_cve_sh_score1*100)/CV3_BASE_score_1_sh)))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2020 LA PUNTUACION BASE ESTÁ ENTRE 1 y 2 \n")
    print("       -     EN EL "+str(float(((count_lastpublidate_2019_cve_sh_score1*100)/CV3_BASE_score_1_sh)))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2019 LA PUNTUACION BASE ESTÁ ENTRE 1 y 2 \n")
    print("       -     EN EL "+str(float(((count_lastpublidate_2018_cve_sh_score1*100)/CV3_BASE_score_1_sh)))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2018 O ANTERIORMENTE LA PUNTUACION BASE ESTÁ ENTRE 1 y 2 \n")
if(CV3_BASE_score_0_sh>0):
    print(" -  EN EL "+str(float(((CV3_BASE_score_0_sh*100)/len(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"]))))+"% DE LAS VULNERABILIDADES LA PUNTUACION BASE ESTÁ ENTRE 0 y 1 \n")
    print("       -     EN EL "+str(float(((count_lastpublidate_2023_cve_sh_score0*100)/CV3_BASE_score_0_sh)))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2023 LA PUNTUACION BASE ESTÁ ENTRE 0 y 1 \n")
    print("       -     EN EL "+str(float(((count_lastpublidate_2022_cve_sh_score0*100)/CV3_BASE_score_0_sh)))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2022 LA PUNTUACION BASE ESTÁ ENTRE 0 y 1 \n")
    print("       -     EN EL "+str(float(((count_lastpublidate_2021_cve_sh_score0*100)/CV3_BASE_score_0_sh)))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2021 LA PUNTUACION BASE ESTÁ ENTRE 0 y 1 \n")
    print("       -     EN EL "+str(float(((count_lastpublidate_2020_cve_sh_score0*100)/CV3_BASE_score_0_sh)))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2020 LA PUNTUACION BASE ESTÁ ENTRE 0 y 1 \n")
    print("       -     EN EL "+str(float(((count_lastpublidate_2019_cve_sh_score0*100)/CV3_BASE_score_0_sh)))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2019 LA PUNTUACION BASE ESTÁ ENTRE 0 y 1 \n")
    print("       -     EN EL "+str(float(((count_lastpublidate_2018_cve_sh_score0*100)/CV3_BASE_score_0_sh)))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2018 O ANTERIORMENTE LA PUNTUACION BASE ESTÁ ENTRE 0 y 1 \n")






print("************************** ESTADÍSTICAS PUNTUACION BASE/AÑO DE PUBLICACION EN CVE CVSSV3 PARTE IOT Y SMART HOME CONJUNTAS********************************")
print("\n")
print("\n")
print("DE UN TOTAL DE "+str(len(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"])+len(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"]))+" VULNERABILIDADES, LAS ESTADÍSTICAS DE FECHA DE FECHA DE PUBLICACIÓN DE LAS VULNERABILIDADES SEGÚN SU PUNTUACIÓN BASE SON LAS SIGUIENTES :  \n")
print("\n")
print(" -  EN "+str(CV3_BASE_score_10_sh+CV3_BASE_score_10_iot)+" VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
print("       -     EN "+str(count_lastpublidate_2023_cve_sh_score10+count_lastpublidate_2023_cve_sh_score10)+" VULNERABILIDADES PUBLICADAS EN 2023 LA PUNTUACION BASE ES 10 \n")
print("       -     EN "+str(count_lastpublidate_2022_cve_sh_score10+count_lastpublidate_2022_cve_sh_score10)+" VULNERABILIDADES PUBLICADAS EN 2022 LA PUNTUACION BASE ES 10 \n")
print("       -     EN "+str(count_lastpublidate_2021_cve_sh_score10+count_lastpublidate_2021_cve_sh_score10)+" VULNERABILIDADES PUBLICADAS EN 2021 LA PUNTUACION BASE ES 10 \n")
print("       -     EN "+str(count_lastpublidate_2020_cve_sh_score10+count_lastpublidate_2020_cve_sh_score10)+" VULNERABILIDADES PUBLICADAS EN 2020 LA PUNTUACION BASE ES 10 \n")
print("       -     EN "+str(count_lastpublidate_2019_cve_sh_score10+count_lastpublidate_2019_cve_sh_score10)+" VULNERABILIDADES PUBLICADAS EN 2019 LA PUNTUACION BASE ES 10 \n")
print("       -     EN "+str(count_lastpublidate_2018_cve_sh_score10+count_lastpublidate_2018_cve_sh_score10)+" VULNERABILIDADES PUBLICADAS EN 2018 O ANTES LA PUNTUACION BASE ES 10 \n")


print("\n")
print(" -  EN "+str(CV3_BASE_score_9_sh+CV3_BASE_score_9_iot)+" VULNERABILIDADES LA PUNTUACION BASE ESTÁ ENTRE 9 Y 10 \n")
print("       -     EN "+str(count_lastpublidate_2023_cve_sh_score9+count_lastpublidate_2023_cve_sh_score9)+" VULNERABILIDADES PUBLICADAS EN 2023 LA PUNTUACION BASE ESTÁ ENTRE 9 Y 10 \n")
print("       -     EN "+str(count_lastpublidate_2022_cve_sh_score9+count_lastpublidate_2022_cve_sh_score9)+" VULNERABILIDADES PUBLICADAS EN 2022 LA PUNTUACION BASE ESTÁ ENTRE 9 Y 10 \n")
print("       -     EN "+str(count_lastpublidate_2021_cve_sh_score9+count_lastpublidate_2021_cve_sh_score9)+" VULNERABILIDADES PUBLICADAS EN 2021 LA PUNTUACION BASE ESTÁ ENTRE 9 Y 10 \n")
print("       -     EN "+str(count_lastpublidate_2020_cve_sh_score9+count_lastpublidate_2020_cve_sh_score9)+" VULNERABILIDADES PUBLICADAS EN 2020 LA PUNTUACION BASE ESTÁ ENTRE 9 Y 10 \n")
print("       -     EN "+str(count_lastpublidate_2019_cve_sh_score9+count_lastpublidate_2019_cve_sh_score9)+" VULNERABILIDADES PUBLICADAS EN 2019 LA PUNTUACION BASE ESTÁ ENTRE 9 Y 10 \n")
print("       -     EN "+str(count_lastpublidate_2018_cve_sh_score9+count_lastpublidate_2018_cve_sh_score9)+" VULNERABILIDADES PUBLICADAS EN 2018 O ANTES LA PUNTUACION BASE ESTÁ ENTRE 9 Y 10 \n")


print("\n")
print(" -  EN "+str(CV3_BASE_score_8_sh+CV3_BASE_score_8_iot)+" VULNERABILIDADES LA PUNTUACION BASE ESTÁ ENTRE 8 y 9 \n")
print("       -     EN "+str(count_lastpublidate_2023_cve_sh_score8+count_lastpublidate_2023_cve_sh_score8)+" VULNERABILIDADES PUBLICADAS EN 2023 LA PUNTUACION BASE ESTÁ ENTRE 8 y 9 \n")
print("       -     EN "+str(count_lastpublidate_2022_cve_sh_score8+count_lastpublidate_2022_cve_sh_score8)+" VULNERABILIDADES PUBLICADAS EN 2022 LA PUNTUACION BASE ESTÁ ENTRE 8 y 9 \n")
print("       -     EN "+str(count_lastpublidate_2021_cve_sh_score8+count_lastpublidate_2021_cve_sh_score8)+" VULNERABILIDADES PUBLICADAS EN 2021 LA PUNTUACION BASE ESTÁ ENTRE 8 y 9 \n")
print("       -     EN "+str(count_lastpublidate_2020_cve_sh_score8+count_lastpublidate_2020_cve_sh_score8)+" VULNERABILIDADES PUBLICADAS EN 2020 LA PUNTUACION BASE ESTÁ ENTRE 8 y 9 \n")
print("       -     EN "+str(count_lastpublidate_2019_cve_sh_score8+count_lastpublidate_2019_cve_sh_score8)+" VULNERABILIDADES PUBLICADAS EN 2019 LA PUNTUACION BASE ESTÁ ENTRE 8 y 9 \n")
print("       -     EN "+str(count_lastpublidate_2018_cve_sh_score8+count_lastpublidate_2018_cve_sh_score8)+" VULNERABILIDADES PUBLICADAS EN 2018 O ANTES LA PUNTUACION BASE ESTÁ ENTRE 8 y 9 \n")



print("\n")
print(" -  EN "+str(CV3_BASE_score_7_sh+CV3_BASE_score_7_iot)+" VULNERABILIDADES LA PUNTUACION BASE ESTÁ ENTRE 7 y 8 \n")
print("       -     EN "+str(count_lastpublidate_2023_cve_sh_score7+count_lastpublidate_2023_cve_sh_score7)+" VULNERABILIDADES PUBLICADAS EN 2023 LA PUNTUACION BASE ESTÁ ENTRE 7 y 8 \n")
print("       -     EN "+str(count_lastpublidate_2022_cve_sh_score7+count_lastpublidate_2022_cve_sh_score7)+" VULNERABILIDADES PUBLICADAS EN 2022 LA PUNTUACION BASE ESTÁ ENTRE 7 y 8 \n")
print("       -     EN "+str(count_lastpublidate_2021_cve_sh_score7+count_lastpublidate_2021_cve_sh_score7)+" VULNERABILIDADES PUBLICADAS EN 2021 LA PUNTUACION BASE ESTÁ ENTRE 7 y 8 \n")
print("       -     EN "+str(count_lastpublidate_2020_cve_sh_score7+count_lastpublidate_2020_cve_sh_score7)+" VULNERABILIDADES PUBLICADAS EN 2020 LA PUNTUACION BASE ESTÁ ENTRE 7 y 8 \n")
print("       -     EN "+str(count_lastpublidate_2019_cve_sh_score7+count_lastpublidate_2019_cve_sh_score7)+" VULNERABILIDADES PUBLICADAS EN 2019 LA PUNTUACION BASE ESTÁ ENTRE 7 y 8 \n")
print("       -     EN "+str(count_lastpublidate_2018_cve_sh_score7+count_lastpublidate_2018_cve_sh_score7)+" VULNERABILIDADES PUBLICADAS EN 2018 O ANTES LA PUNTUACION BASE ESTÁ ENTRE 7 y 8 \n")


print("\n")
print(" -  EN "+str(CV3_BASE_score_6_sh+CV3_BASE_score_6_iot)+" VULNERABILIDADES LA PUNTUACION BASE ESTÁ ENTRE 6 y 7 \n")
print("       -     EN "+str(count_lastpublidate_2023_cve_sh_score6+count_lastpublidate_2023_cve_sh_score6)+" VULNERABILIDADES PUBLICADAS EN 2023 LA PUNTUACION BASE ESTÁ ENTRE 6 y 7 \n")
print("       -     EN "+str(count_lastpublidate_2022_cve_sh_score6+count_lastpublidate_2022_cve_sh_score6)+" VULNERABILIDADES PUBLICADAS EN 2022 LA PUNTUACION BASE ESTÁ ENTRE 6 y 7 \n")
print("       -     EN "+str(count_lastpublidate_2021_cve_sh_score6+count_lastpublidate_2021_cve_sh_score6)+" VULNERABILIDADES PUBLICADAS EN 2021 LA PUNTUACION BASE ESTÁ ENTRE 6 y 7 \n")
print("       -     EN "+str(count_lastpublidate_2020_cve_sh_score6+count_lastpublidate_2020_cve_sh_score6)+" VULNERABILIDADES PUBLICADAS EN 2020 LA PUNTUACION BASE ESTÁ ENTRE 6 y 7 \n")
print("       -     EN "+str(count_lastpublidate_2019_cve_sh_score6+count_lastpublidate_2019_cve_sh_score6)+" VULNERABILIDADES PUBLICADAS EN 2019 LA PUNTUACION BASE ESTÁ ENTRE 6 y 7 \n")
print("       -     EN "+str(count_lastpublidate_2018_cve_sh_score6+count_lastpublidate_2018_cve_sh_score6)+" VULNERABILIDADES PUBLICADAS EN 2018 O ANTES LA PUNTUACION BASE ESTÁ ENTRE 6 y 7 \n")


print("\n")
print(" -  EN "+str(CV3_BASE_score_5_sh+CV3_BASE_score_5_iot)+" VULNERABILIDADES LA PUNTUACION BASE ESTÁ ENTRE 5 y 6 \n")
print("       -     EN "+str(count_lastpublidate_2023_cve_sh_score5+count_lastpublidate_2023_cve_sh_score5)+" VULNERABILIDADES PUBLICADAS EN 2023 LA PUNTUACION BASE ESTÁ ENTRE 5 y 6 \n")
print("       -     EN "+str(count_lastpublidate_2022_cve_sh_score5+count_lastpublidate_2022_cve_sh_score5)+" VULNERABILIDADES PUBLICADAS EN 2022 LA PUNTUACION BASE ESTÁ ENTRE 5 y 6 \n")
print("       -     EN "+str(count_lastpublidate_2021_cve_sh_score5+count_lastpublidate_2021_cve_sh_score5)+" VULNERABILIDADES PUBLICADAS EN 2021 LA PUNTUACION BASE ESTÁ ENTRE 5 y 6 \n")
print("       -     EN "+str(count_lastpublidate_2020_cve_sh_score5+count_lastpublidate_2020_cve_sh_score5)+" VULNERABILIDADES PUBLICADAS EN 2020 LA PUNTUACION BASE ESTÁ ENTRE 5 y 6 \n")
print("       -     EN "+str(count_lastpublidate_2019_cve_sh_score5+count_lastpublidate_2019_cve_sh_score5)+" VULNERABILIDADES PUBLICADAS EN 2019 LA PUNTUACION BASE ESTÁ ENTRE 5 y 6 \n")
print("       -     EN "+str(count_lastpublidate_2018_cve_sh_score5+count_lastpublidate_2018_cve_sh_score5)+" VULNERABILIDADES PUBLICADAS EN 2018 O ANTES LA PUNTUACION BASE ESTÁ ENTRE 5 y 6 \n")


print("\n")
print(" -  EN "+str(CV3_BASE_score_4_sh+CV3_BASE_score_4_iot)+" VULNERABILIDADES LA PUNTUACION BASE ESTÁ ENTRE 4 y 5 \n")
print("       -     EN "+str(count_lastpublidate_2023_cve_sh_score4+count_lastpublidate_2023_cve_sh_score4)+" VULNERABILIDADES PUBLICADAS EN 2023 LA PUNTUACION BASE ESTÁ ENTRE 4 y 5 \n")
print("       -     EN "+str(count_lastpublidate_2022_cve_sh_score4+count_lastpublidate_2022_cve_sh_score4)+" VULNERABILIDADES PUBLICADAS EN 2022 LA PUNTUACION BASE ESTÁ ENTRE 4 y 5 \n")
print("       -     EN "+str(count_lastpublidate_2021_cve_sh_score4+count_lastpublidate_2021_cve_sh_score4)+" VULNERABILIDADES PUBLICADAS EN 2021 LA PUNTUACION BASE ESTÁ ENTRE 4 y 5 \n")
print("       -     EN "+str(count_lastpublidate_2020_cve_sh_score4+count_lastpublidate_2020_cve_sh_score4)+" VULNERABILIDADES PUBLICADAS EN 2020 LA PUNTUACION BASE ESTÁ ENTRE 4 y 5 \n")
print("       -     EN "+str(count_lastpublidate_2019_cve_sh_score4+count_lastpublidate_2019_cve_sh_score4)+" VULNERABILIDADES PUBLICADAS EN 2019 LA PUNTUACION BASE ESTÁ ENTRE 4 y 5 \n")
print("       -     EN "+str(count_lastpublidate_2018_cve_sh_score4+count_lastpublidate_2018_cve_sh_score4)+" VULNERABILIDADES PUBLICADAS EN 2018 O ANTES LA PUNTUACION BASE ESTÁ ENTRE 4 y 5 \n")


print("\n")
print(" -  EN "+str(CV3_BASE_score_3_sh+CV3_BASE_score_3_iot)+" VULNERABILIDADES LA PUNTUACION BASE ESTÁ ENTRE 3 y 4 \n")
print("       -     EN "+str(count_lastpublidate_2023_cve_sh_score3+count_lastpublidate_2023_cve_sh_score3)+" VULNERABILIDADES PUBLICADAS EN 2023 LA PUNTUACION BASE ESTÁ ENTRE 3 y 4 \n")
print("       -     EN "+str(count_lastpublidate_2022_cve_sh_score3+count_lastpublidate_2022_cve_sh_score3)+" VULNERABILIDADES PUBLICADAS EN 2022 LA PUNTUACION BASE ESTÁ ENTRE 3 y 4 \n")
print("       -     EN "+str(count_lastpublidate_2021_cve_sh_score3+count_lastpublidate_2021_cve_sh_score3)+" VULNERABILIDADES PUBLICADAS EN 2021 LA PUNTUACION BASE ESTÁ ENTRE 3 y 4 \n")
print("       -     EN "+str(count_lastpublidate_2020_cve_sh_score3+count_lastpublidate_2020_cve_sh_score3)+" VULNERABILIDADES PUBLICADAS EN 2020 LA PUNTUACION BASE ESTÁ ENTRE 3 y 4 \n")
print("       -     EN "+str(count_lastpublidate_2019_cve_sh_score3+count_lastpublidate_2019_cve_sh_score3)+" VULNERABILIDADES PUBLICADAS EN 2019 LA PUNTUACION BASE ESTÁ ENTRE 3 y 4 \n")
print("       -     EN "+str(count_lastpublidate_2018_cve_sh_score3+count_lastpublidate_2018_cve_sh_score3)+" VULNERABILIDADES PUBLICADAS EN 2018 O ANTES LA PUNTUACION BASE ESTÁ ENTRE 3 y 4 \n")

print("\n")
print(" -  EN "+str(CV3_BASE_score_2_sh+CV3_BASE_score_2_iot)+" VULNERABILIDADES LA PUNTUACION BASE ESTÁ ENTRE 2 y 3 \n")
print("       -     EN "+str(count_lastpublidate_2023_cve_sh_score2+count_lastpublidate_2023_cve_sh_score2)+" VULNERABILIDADES PUBLICADAS EN 2023 LA PUNTUACION BASE ESTÁ ENTRE 2 y 3 \n")
print("       -     EN "+str(count_lastpublidate_2022_cve_sh_score2+count_lastpublidate_2022_cve_sh_score2)+" VULNERABILIDADES PUBLICADAS EN 2022 LA PUNTUACION BASE ESTÁ ENTRE 2 y 3 \n")
print("       -     EN "+str(count_lastpublidate_2021_cve_sh_score2+count_lastpublidate_2021_cve_sh_score2)+" VULNERABILIDADES PUBLICADAS EN 2021 LA PUNTUACION BASE ESTÁ ENTRE 2 y 3 \n")
print("       -     EN "+str(count_lastpublidate_2020_cve_sh_score2+count_lastpublidate_2020_cve_sh_score2)+" VULNERABILIDADES PUBLICADAS EN 2020 LA PUNTUACION BASE ESTÁ ENTRE 2 y 3 \n")
print("       -     EN "+str(count_lastpublidate_2019_cve_sh_score2+count_lastpublidate_2019_cve_sh_score2)+" VULNERABILIDADES PUBLICADAS EN 2019 LA PUNTUACION BASE ESTÁ ENTRE 2 y 3 \n")
print("       -     EN "+str(count_lastpublidate_2018_cve_sh_score2+count_lastpublidate_2018_cve_sh_score2)+" VULNERABILIDADES PUBLICADAS EN 2018 O ANTES LA PUNTUACION BASE ESTÁ ENTRE 2 y 3 \n")


print("\n")
print(" -  EN "+str(CV3_BASE_score_1_sh+CV3_BASE_score_1_iot)+" VULNERABILIDADES LA PUNTUACION BASE ESTÁ ENTRE 1 y 2 \n")
print("       -     EN "+str(count_lastpublidate_2023_cve_sh_score1+count_lastpublidate_2023_cve_sh_score1)+" VULNERABILIDADES PUBLICADAS EN 2023 LA PUNTUACION BASE ESTÁ ENTRE 1 y 2 \n")
print("       -     EN "+str(count_lastpublidate_2022_cve_sh_score1+count_lastpublidate_2022_cve_sh_score1)+" VULNERABILIDADES PUBLICADAS EN 2022 LA PUNTUACION BASE ESTÁ ENTRE 1 y 2 \n")
print("       -     EN "+str(count_lastpublidate_2021_cve_sh_score1+count_lastpublidate_2021_cve_sh_score1)+" VULNERABILIDADES PUBLICADAS EN 2021 LA PUNTUACION BASE ESTÁ ENTRE 1 y 2 \n")
print("       -     EN "+str(count_lastpublidate_2020_cve_sh_score1+count_lastpublidate_2020_cve_sh_score1)+" VULNERABILIDADES PUBLICADAS EN 2020 LA PUNTUACION BASE ESTÁ ENTRE 1 y 2 \n")
print("       -     EN "+str(count_lastpublidate_2019_cve_sh_score1+count_lastpublidate_2019_cve_sh_score1)+" VULNERABILIDADES PUBLICADAS EN 2019 LA PUNTUACION BASE ESTÁ ENTRE 1 y 2 \n")
print("       -     EN "+str(count_lastpublidate_2018_cve_sh_score1+count_lastpublidate_2018_cve_sh_score1)+" VULNERABILIDADES PUBLICADAS EN 2018 O ANTES LA PUNTUACION BASE ESTÁ ENTRE 1 y 2 \n")


print("\n")
print(" -  EN "+str(CV3_BASE_score_0_sh+CV3_BASE_score_0_iot)+" VULNERABILIDADES LA PUNTUACION BASE ESTÁ ENTRE 0 y 1 \n")
print("       -     EN "+str(count_lastpublidate_2023_cve_sh_score0+count_lastpublidate_2023_cve_sh_score0)+" VULNERABILIDADES PUBLICADAS EN 2023 LA PUNTUACION BASE ESTÁ ENTRE 0 y 1 \n")
print("       -     EN "+str(count_lastpublidate_2022_cve_sh_score0+count_lastpublidate_2022_cve_sh_score0)+" VULNERABILIDADES PUBLICADAS EN 2022 LA PUNTUACION BASE ESTÁ ENTRE 0 y 1 \n")
print("       -     EN "+str(count_lastpublidate_2021_cve_sh_score0+count_lastpublidate_2021_cve_sh_score0)+" VULNERABILIDADES PUBLICADAS EN 2021 LA PUNTUACION BASE ESTÁ ENTRE 0 y 1 \n")
print("       -     EN "+str(count_lastpublidate_2020_cve_sh_score0+count_lastpublidate_2020_cve_sh_score0)+" VULNERABILIDADES PUBLICADAS EN 2020 LA PUNTUACION BASE ESTÁ ENTRE 0 y 1 \n")
print("       -     EN "+str(count_lastpublidate_2019_cve_sh_score0+count_lastpublidate_2019_cve_sh_score0)+" VULNERABILIDADES PUBLICADAS EN 2019 LA PUNTUACION BASE ESTÁ ENTRE 0 y 1 \n")
print("       -     EN "+str(count_lastpublidate_2018_cve_sh_score0+count_lastpublidate_2018_cve_sh_score0)+" VULNERABILIDADES PUBLICADAS EN 2018 O ANTES LA PUNTUACION BASE ESTÁ ENTRE 0 y 1 \n")



print("***************************PORCENTAJE PUNTUACION BASE/AÑO DE PUBLICACION EN CVE CVSSV3 PARTE IOT Y SMART HOME CONJUNTAS********************************")
print("\n")
print("\n")
print("DE UN TOTAL DE "+str(len(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"])+len(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"]))+" VULNERABILIDADES, LOS PORCENTAJES DE FECHA DE FECHA DE PUBLICACIÓN DE LAS VULNERABILIDADES SEGÚN SU PUNTUACIÓN BASE SON LOS SIGUIENTES :  \n")
print("\n")
if((CV3_BASE_score_10_sh+CV3_BASE_score_10_iot)>0):
    print(" -  EN EL "+str(float((((CV3_BASE_score_10_sh+CV3_BASE_score_10_iot)*100)/(len(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"])+len(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"])))))+"% DE LAS VULNERABILIDADES LA PUNTUACION BASE ES 10 \n")
    print("       -     EN EL "+str(float((((count_lastpublidate_2023_cve_sh_score10+count_lastpublidate_2023_cve_iot_score10)*100)/(CV3_BASE_score_10_sh+CV3_BASE_score_10_iot))))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2023 LA PUNTUACION BASE ES 10 \n")
    print("       -     EN EL "+str(float((((count_lastpublidate_2022_cve_sh_score10+count_lastpublidate_2022_cve_iot_score10)*100)/(CV3_BASE_score_10_sh+CV3_BASE_score_10_iot))))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2022 LA PUNTUACION BASE ES 10 \n")
    print("       -     EN EL "+str(float((((count_lastpublidate_2021_cve_sh_score10+count_lastpublidate_2021_cve_iot_score10)*100)/(CV3_BASE_score_10_sh+CV3_BASE_score_10_iot))))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2021 LA PUNTUACION BASE ES 10 \n")
    print("       -     EN EL "+str(float((((count_lastpublidate_2020_cve_sh_score10+count_lastpublidate_2020_cve_iot_score10)*100)/(CV3_BASE_score_10_sh+CV3_BASE_score_10_iot))))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2020 LA PUNTUACION BASE ES 10 \n")
    print("       -     EN EL "+str(float((((count_lastpublidate_2019_cve_sh_score10+count_lastpublidate_2019_cve_iot_score10)*100)/(CV3_BASE_score_10_sh+CV3_BASE_score_10_iot))))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2019 LA PUNTUACION BASE ES 10 \n")
    print("       -     EN EL "+str(float((((count_lastpublidate_2018_cve_sh_score10+count_lastpublidate_2018_cve_iot_score10)*100)/(CV3_BASE_score_10_sh+CV3_BASE_score_10_iot))))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2018 O ANTERIORMENTE LA PUNTUACION BASE ES 10 \n")

if((CV3_BASE_score_9_sh+CV3_BASE_score_9_iot)>0):
    print(" -  EN EL "+str(float((((CV3_BASE_score_9_sh+CV3_BASE_score_9_iot)*100)/(len(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"])+len(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"])))))+"% DE LAS VULNERABILIDADES LA PUNTUACION BASE ESTÁ ENTRE 9 Y 10 \n")
    print("       -     EN EL "+str(float((((count_lastpublidate_2023_cve_sh_score9+count_lastpublidate_2023_cve_iot_score9)*100)/(CV3_BASE_score_9_sh+CV3_BASE_score_9_iot))))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2023 LA PUNTUACION BASE ESTÁ ENTRE 9 Y 10 \n")
    print("       -     EN EL "+str(float((((count_lastpublidate_2022_cve_sh_score9+count_lastpublidate_2022_cve_iot_score9)*100)/(CV3_BASE_score_9_sh+CV3_BASE_score_9_iot))))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2022 LA PUNTUACION BASE ESTÁ ENTRE 9 Y 10 \n")
    print("       -     EN EL "+str(float((((count_lastpublidate_2021_cve_sh_score9+count_lastpublidate_2021_cve_iot_score9)*100)/(CV3_BASE_score_9_sh+CV3_BASE_score_9_iot))))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2021 LA PUNTUACION BASE ESTÁ ENTRE 9 Y 10 \n")
    print("       -     EN EL "+str(float((((count_lastpublidate_2020_cve_sh_score9+count_lastpublidate_2020_cve_iot_score9)*100)/(CV3_BASE_score_9_sh+CV3_BASE_score_9_iot))))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2020 LA PUNTUACION BASE ESTÁ ENTRE 9 Y 10 \n")
    print("       -     EN EL "+str(float((((count_lastpublidate_2019_cve_sh_score9+count_lastpublidate_2019_cve_iot_score9)*100)/(CV3_BASE_score_9_sh+CV3_BASE_score_9_iot))))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2019 LA PUNTUACION BASE ESTÁ ENTRE 9 Y 10 \n")
    print("       -     EN EL "+str(float((((count_lastpublidate_2018_cve_sh_score9+count_lastpublidate_2018_cve_iot_score9)*100)/(CV3_BASE_score_9_sh+CV3_BASE_score_9_iot))))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2018 O ANTERIORMENTE LA PUNTUACION BASE ESTÁ ENTRE 9 Y 10 \n")

if((CV3_BASE_score_8_sh+CV3_BASE_score_8_iot)>0):
    print(" -  EN EL "+str(float((((CV3_BASE_score_8_sh+CV3_BASE_score_8_iot)*100)/(len(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"])+len(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"])))))+"% DE LAS VULNERABILIDADES LA PUNTUACION BASE ESTÁ ENTRE 8 Y 9 \n")
    print("       -     EN EL "+str(float((((count_lastpublidate_2023_cve_sh_score8+count_lastpublidate_2023_cve_iot_score8)*100)/(CV3_BASE_score_8_sh+CV3_BASE_score_8_iot))))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2023 LA PUNTUACION BASE ESTÁ ENTRE 8 Y 9 \n")
    print("       -     EN EL "+str(float((((count_lastpublidate_2022_cve_sh_score8+count_lastpublidate_2022_cve_iot_score8)*100)/(CV3_BASE_score_8_sh+CV3_BASE_score_8_iot))))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2022 LA PUNTUACION BASE ESTÁ ENTRE 8 Y 9 \n")
    print("       -     EN EL "+str(float((((count_lastpublidate_2021_cve_sh_score8+count_lastpublidate_2021_cve_iot_score8)*100)/(CV3_BASE_score_8_sh+CV3_BASE_score_8_iot))))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2021 LA PUNTUACION BASE ESTÁ ENTRE 8 Y 9 \n")
    print("       -     EN EL "+str(float((((count_lastpublidate_2020_cve_sh_score8+count_lastpublidate_2020_cve_iot_score8)*100)/(CV3_BASE_score_8_sh+CV3_BASE_score_8_iot))))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2020 LA PUNTUACION BASE ESTÁ ENTRE 8 Y 9 \n")
    print("       -     EN EL "+str(float((((count_lastpublidate_2019_cve_sh_score8+count_lastpublidate_2019_cve_iot_score8)*100)/(CV3_BASE_score_8_sh+CV3_BASE_score_8_iot))))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2019 LA PUNTUACION BASE ESTÁ ENTRE 8 Y 9 \n")
    print("       -     EN EL "+str(float((((count_lastpublidate_2018_cve_sh_score8+count_lastpublidate_2018_cve_iot_score8)*100)/(CV3_BASE_score_8_sh+CV3_BASE_score_8_iot))))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2018 O ANTERIORMENTE LA PUNTUACION BASE ESTÁ ENTRE 8 Y 9 \n")

if((CV3_BASE_score_7_sh+CV3_BASE_score_7_iot)>0):
    print(" -  EN EL "+str(float((((CV3_BASE_score_7_sh+CV3_BASE_score_7_iot)*100)/(len(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"])+len(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"])))))+"% DE LAS VULNERABILIDADES LA PUNTUACION BASE ESTÁ ENTRE 7 y 8 \n")
    print("       -     EN EL "+str(float((((count_lastpublidate_2023_cve_sh_score7+count_lastpublidate_2023_cve_iot_score7)*100)/(CV3_BASE_score_7_sh+CV3_BASE_score_7_iot))))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2023 LA PUNTUACION BASE ESTÁ ENTRE 7 y 8 \n")
    print("       -     EN EL "+str(float((((count_lastpublidate_2022_cve_sh_score7+count_lastpublidate_2022_cve_iot_score7)*100)/(CV3_BASE_score_7_sh+CV3_BASE_score_7_iot))))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2022 LA PUNTUACION BASE ESTÁ ENTRE 7 y 8 \n")
    print("       -     EN EL "+str(float((((count_lastpublidate_2021_cve_sh_score7+count_lastpublidate_2021_cve_iot_score7)*100)/(CV3_BASE_score_7_sh+CV3_BASE_score_7_iot))))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2021 LA PUNTUACION BASE ESTÁ ENTRE 7 y 8 \n")
    print("       -     EN EL "+str(float((((count_lastpublidate_2020_cve_sh_score7+count_lastpublidate_2020_cve_iot_score7)*100)/(CV3_BASE_score_7_sh+CV3_BASE_score_7_iot))))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2020 LA PUNTUACION BASE ESTÁ ENTRE 7 y 8 \n")
    print("       -     EN EL "+str(float((((count_lastpublidate_2019_cve_sh_score7+count_lastpublidate_2019_cve_iot_score7)*100)/(CV3_BASE_score_7_sh+CV3_BASE_score_7_iot))))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2019 LA PUNTUACION BASE ESTÁ ENTRE 7 y 8 \n")
    print("       -     EN EL "+str(float((((count_lastpublidate_2018_cve_sh_score7+count_lastpublidate_2018_cve_iot_score7)*100)/(CV3_BASE_score_7_sh+CV3_BASE_score_7_iot))))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2018 O ANTERIORMENTE LA PUNTUACION BASE ESTÁ ENTRE 7 y 8 \n")


if((CV3_BASE_score_6_sh+CV3_BASE_score_6_iot)>0):
    print(" -  EN EL "+str(float((((CV3_BASE_score_6_sh+CV3_BASE_score_6_iot)*100)/(len(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"])+len(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"])))))+"% DE LAS VULNERABILIDADES LA PUNTUACION BASE ESTÁ ENTRE 6 y 7 \n")
    print("       -     EN EL "+str(float((((count_lastpublidate_2023_cve_sh_score6+count_lastpublidate_2023_cve_iot_score6)*100)/(CV3_BASE_score_6_sh+CV3_BASE_score_6_iot))))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2023 LA PUNTUACION BASE ESTÁ ENTRE 6 y 7 \n")
    print("       -     EN EL "+str(float((((count_lastpublidate_2022_cve_sh_score6+count_lastpublidate_2022_cve_iot_score6)*100)/(CV3_BASE_score_6_sh+CV3_BASE_score_6_iot))))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2022 LA PUNTUACION BASE ESTÁ ENTRE 6 y 7 \n")
    print("       -     EN EL "+str(float((((count_lastpublidate_2021_cve_sh_score6+count_lastpublidate_2021_cve_iot_score6)*100)/(CV3_BASE_score_6_sh+CV3_BASE_score_6_iot))))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2021 LA PUNTUACION BASE ESTÁ ENTRE 6 y 7 \n")
    print("       -     EN EL "+str(float((((count_lastpublidate_2020_cve_sh_score6+count_lastpublidate_2020_cve_iot_score6)*100)/(CV3_BASE_score_6_sh+CV3_BASE_score_6_iot))))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2020 LA PUNTUACION BASE ESTÁ ENTRE 6 y 7 \n")
    print("       -     EN EL "+str(float((((count_lastpublidate_2019_cve_sh_score6+count_lastpublidate_2019_cve_iot_score6)*100)/(CV3_BASE_score_6_sh+CV3_BASE_score_6_iot))))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2019 LA PUNTUACION BASE ESTÁ ENTRE 6 y 7 \n")
    print("       -     EN EL "+str(float((((count_lastpublidate_2018_cve_sh_score6+count_lastpublidate_2018_cve_iot_score6)*100)/(CV3_BASE_score_6_sh+CV3_BASE_score_6_iot))))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2018 O ANTERIORMENTE LA PUNTUACION BASE ESTÁ ENTRE 6 y 7 \n")

if((CV3_BASE_score_5_sh+CV3_BASE_score_5_iot)>0):
    print(" -  EN EL "+str(float((((CV3_BASE_score_5_sh+CV3_BASE_score_5_iot)*100)/(len(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"])+len(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"])))))+"% DE LAS VULNERABILIDADES LA PUNTUACION BASE ESTÁ ENTRE 5 y 6 \n")
    print("       -     EN EL "+str(float((((count_lastpublidate_2023_cve_sh_score5+count_lastpublidate_2023_cve_iot_score5)*100)/(CV3_BASE_score_5_sh+CV3_BASE_score_5_iot))))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2023 LA PUNTUACION BASE ESTÁ ENTRE 5 y 6 \n")
    print("       -     EN EL "+str(float((((count_lastpublidate_2022_cve_sh_score5+count_lastpublidate_2022_cve_iot_score5)*100)/(CV3_BASE_score_5_sh+CV3_BASE_score_5_iot))))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2022 LA PUNTUACION BASE ESTÁ ENTRE 5 y 6 \n")
    print("       -     EN EL "+str(float((((count_lastpublidate_2021_cve_sh_score5+count_lastpublidate_2021_cve_iot_score5)*100)/(CV3_BASE_score_5_sh+CV3_BASE_score_5_iot))))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2021 LA PUNTUACION BASE ESTÁ ENTRE 5 y 6 \n")
    print("       -     EN EL "+str(float((((count_lastpublidate_2020_cve_sh_score5+count_lastpublidate_2020_cve_iot_score5)*100)/(CV3_BASE_score_5_sh+CV3_BASE_score_5_iot))))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2020 LA PUNTUACION BASE ESTÁ ENTRE 5 y 6 \n")
    print("       -     EN EL "+str(float((((count_lastpublidate_2019_cve_sh_score5+count_lastpublidate_2019_cve_iot_score5)*100)/(CV3_BASE_score_5_sh+CV3_BASE_score_5_iot))))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2019 LA PUNTUACION BASE ESTÁ ENTRE 5 y 6 \n")
    print("       -     EN EL "+str(float((((count_lastpublidate_2018_cve_sh_score5+count_lastpublidate_2018_cve_iot_score5)*100)/(CV3_BASE_score_5_sh+CV3_BASE_score_5_iot))))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2018 O ANTERIORMENTE LA PUNTUACION BASE ESTÁ ENTRE 5 y 6 \n")

if((CV3_BASE_score_4_sh+CV3_BASE_score_4_iot)>0):
    print(" -  EN EL "+str(float((((CV3_BASE_score_4_sh+CV3_BASE_score_4_iot)*100)/(len(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"])+len(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"])))))+"% DE LAS VULNERABILIDADES LA PUNTUACION BASE ESTÁ ENTRE 4 y 5 \n")
    print("       -     EN EL "+str(float((((count_lastpublidate_2023_cve_sh_score4+count_lastpublidate_2023_cve_iot_score4)*100)/(CV3_BASE_score_4_sh+CV3_BASE_score_4_iot))))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2023 LA PUNTUACION BASE ESTÁ ENTRE 4 y 5 \n")
    print("       -     EN EL "+str(float((((count_lastpublidate_2022_cve_sh_score4+count_lastpublidate_2022_cve_iot_score4)*100)/(CV3_BASE_score_4_sh+CV3_BASE_score_4_iot))))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2022 LA PUNTUACION BASE ESTÁ ENTRE 4 y 5 \n")
    print("       -     EN EL "+str(float((((count_lastpublidate_2021_cve_sh_score4+count_lastpublidate_2021_cve_iot_score4)*100)/(CV3_BASE_score_4_sh+CV3_BASE_score_4_iot))))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2021 LA PUNTUACION BASE ESTÁ ENTRE 4 y 5 \n")
    print("       -     EN EL "+str(float((((count_lastpublidate_2020_cve_sh_score4+count_lastpublidate_2020_cve_iot_score4)*100)/(CV3_BASE_score_4_sh+CV3_BASE_score_4_iot))))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2020 LA PUNTUACION BASE ESTÁ ENTRE 4 y 5 \n")
    print("       -     EN EL "+str(float((((count_lastpublidate_2019_cve_sh_score4+count_lastpublidate_2019_cve_iot_score4)*100)/(CV3_BASE_score_4_sh+CV3_BASE_score_4_iot))))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2019 LA PUNTUACION BASE ESTÁ ENTRE 4 y 5 \n")
    print("       -     EN EL "+str(float((((count_lastpublidate_2018_cve_sh_score4+count_lastpublidate_2018_cve_iot_score4)*100)/(CV3_BASE_score_4_sh+CV3_BASE_score_4_iot))))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2018 O ANTERIORMENTE LA PUNTUACION BASE ESTÁ ENTRE 4 y 5 \n")

if((CV3_BASE_score_3_sh+CV3_BASE_score_3_iot)>0):

    print(" -  EN EL "+str(float((((CV3_BASE_score_3_sh+CV3_BASE_score_3_iot)*100)/(len(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"])+len(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"])))))+"% DE LAS VULNERABILIDADES LA PUNTUACION BASE ESTÁ ENTRE 3 y 4 \n")
    print("       -     EN EL "+str(float((((count_lastpublidate_2023_cve_sh_score3+count_lastpublidate_2023_cve_iot_score3)*100)/(CV3_BASE_score_3_sh+CV3_BASE_score_3_iot))))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2023 LA PUNTUACION BASE ESTÁ ENTRE 3 y 4 \n")
    print("       -     EN EL "+str(float((((count_lastpublidate_2022_cve_sh_score3+count_lastpublidate_2022_cve_iot_score3)*100)/(CV3_BASE_score_3_sh+CV3_BASE_score_3_iot))))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2022 LA PUNTUACION BASE ESTÁ ENTRE 3 y 4 \n")
    print("       -     EN EL "+str(float((((count_lastpublidate_2021_cve_sh_score3+count_lastpublidate_2021_cve_iot_score3)*100)/(CV3_BASE_score_3_sh+CV3_BASE_score_3_iot))))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2021 LA PUNTUACION BASE ESTÁ ENTRE 3 y 4 \n")
    print("       -     EN EL "+str(float((((count_lastpublidate_2020_cve_sh_score3+count_lastpublidate_2020_cve_iot_score3)*100)/(CV3_BASE_score_3_sh+CV3_BASE_score_3_iot))))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2020 LA PUNTUACION BASE ESTÁ ENTRE 3 y 4 \n")
    print("       -     EN EL "+str(float((((count_lastpublidate_2019_cve_sh_score3+count_lastpublidate_2019_cve_iot_score3)*100)/(CV3_BASE_score_3_sh+CV3_BASE_score_3_iot))))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2019 LA PUNTUACION BASE ESTÁ ENTRE 3 y 4 \n")
    print("       -     EN EL "+str(float((((count_lastpublidate_2018_cve_sh_score3+count_lastpublidate_2018_cve_iot_score3)*100)/(CV3_BASE_score_3_sh+CV3_BASE_score_3_iot))))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2018 O ANTERIORMENTE LA PUNTUACION BASE ESTÁ ENTRE 3 y 4 \n")

if((CV3_BASE_score_2_sh+CV3_BASE_score_2_iot)>0):

    print(" -  EN EL "+str(float((((CV3_BASE_score_2_sh+CV3_BASE_score_2_iot)*100)/(len(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"])+len(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"])))))+"% DE LAS VULNERABILIDADES LA PUNTUACION BASE ESTÁ ENTRE 2 y 3 \n")
    print("       -     EN EL "+str(float((((count_lastpublidate_2023_cve_sh_score2+count_lastpublidate_2023_cve_iot_score2)*100)/(CV3_BASE_score_2_sh+CV3_BASE_score_2_iot))))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2023 LA PUNTUACION BASE ESTÁ ENTRE 2 y 3 \n")
    print("       -     EN EL "+str(float((((count_lastpublidate_2022_cve_sh_score2+count_lastpublidate_2022_cve_iot_score2)*100)/(CV3_BASE_score_2_sh+CV3_BASE_score_2_iot))))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2022 LA PUNTUACION BASE ESTÁ ENTRE 2 y 3 \n")
    print("       -     EN EL "+str(float((((count_lastpublidate_2021_cve_sh_score2+count_lastpublidate_2021_cve_iot_score2)*100)/(CV3_BASE_score_2_sh+CV3_BASE_score_2_iot))))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2021 LA PUNTUACION BASE ESTÁ ENTRE 2 y 3 \n")
    print("       -     EN EL "+str(float((((count_lastpublidate_2020_cve_sh_score2+count_lastpublidate_2020_cve_iot_score2)*100)/(CV3_BASE_score_2_sh+CV3_BASE_score_2_iot))))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2020 LA PUNTUACION BASE ESTÁ ENTRE 2 y 3 \n")
    print("       -     EN EL "+str(float((((count_lastpublidate_2019_cve_sh_score2+count_lastpublidate_2019_cve_iot_score2)*100)/(CV3_BASE_score_2_sh+CV3_BASE_score_2_iot))))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2019 LA PUNTUACION BASE ESTÁ ENTRE 2 y 3 \n")
    print("       -     EN EL "+str(float((((count_lastpublidate_2018_cve_sh_score2+count_lastpublidate_2018_cve_iot_score2)*100)/(CV3_BASE_score_2_sh+CV3_BASE_score_2_iot))))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2018 O ANTERIORMENTE LA PUNTUACION BASE ESTÁ ENTRE 2 y 3 \n")


if((CV3_BASE_score_1_sh+CV3_BASE_score_1_iot)>0):
    print(" -  EN EL "+str(float((((CV3_BASE_score_1_sh+CV3_BASE_score_1_iot)*100)/(len(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"])+len(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"])))))+"% DE LAS VULNERABILIDADES LA PUNTUACION BASE  ESTÁ ENTRE 1 y 2 \n")
    print("       -     EN EL "+str(float((((count_lastpublidate_2023_cve_sh_score1+count_lastpublidate_2023_cve_iot_score1)*100)/(CV3_BASE_score_1_sh+CV3_BASE_score_1_iot))))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2023 LA PUNTUACION BASE ESTÁ ENTRE 1 y 2 \n")
    print("       -     EN EL "+str(float((((count_lastpublidate_2022_cve_sh_score1+count_lastpublidate_2022_cve_iot_score1)*100)/(CV3_BASE_score_1_sh+CV3_BASE_score_1_iot))))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2022 LA PUNTUACION BASE ESTÁ ENTRE 1 y 2 \n")
    print("       -     EN EL "+str(float((((count_lastpublidate_2021_cve_sh_score1+count_lastpublidate_2021_cve_iot_score1)*100)/(CV3_BASE_score_1_sh+CV3_BASE_score_1_iot))))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2021 LA PUNTUACION BASE ESTÁ ENTRE 1 y 2 \n")
    print("       -     EN EL "+str(float((((count_lastpublidate_2020_cve_sh_score1+count_lastpublidate_2020_cve_iot_score1)*100)/(CV3_BASE_score_1_sh+CV3_BASE_score_1_iot))))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2020 LA PUNTUACION BASE ESTÁ ENTRE 1 y 2 \n")
    print("       -     EN EL "+str(float((((count_lastpublidate_2019_cve_sh_score1+count_lastpublidate_2019_cve_iot_score1)*100)/(CV3_BASE_score_1_sh+CV3_BASE_score_1_iot))))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2019 LA PUNTUACION BASE ESTÁ ENTRE 1 y 2 \n")
    print("       -     EN EL "+str(float((((count_lastpublidate_2018_cve_sh_score1+count_lastpublidate_2018_cve_iot_score1)*100)/(CV3_BASE_score_1_sh+CV3_BASE_score_1_iot))))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2018 O ANTERIORMENTE LA PUNTUACION BASE ESTÁ ENTRE 1 y 2 \n")

if((CV3_BASE_score_0_sh+CV3_BASE_score_0_iot)>0):

    print(" -  EN EL "+str(float((((CV3_BASE_score_0_sh+CV3_BASE_score_0_iot)*100)/(len(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"])+len(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"])))))+"% DE LAS VULNERABILIDADES LA PUNTUACION  BASE ESTÁ ENTRE 0 y 1 \n")
    print("       -     EN EL "+str(float((((count_lastpublidate_2023_cve_sh_score0+count_lastpublidate_2023_cve_iot_score0)*100)/(CV3_BASE_score_0_sh+CV3_BASE_score_0_iot))))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2023 LA PUNTUACION BASE ESTÁ ENTRE 0 y 1 \n")
    print("       -     EN EL "+str(float((((count_lastpublidate_2022_cve_sh_score0+count_lastpublidate_2022_cve_iot_score0)*100)/(CV3_BASE_score_0_sh+CV3_BASE_score_0_iot))))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2022 LA PUNTUACION BASE ESTÁ ENTRE 0 y 1 \n")
    print("       -     EN EL "+str(float((((count_lastpublidate_2021_cve_sh_score0+count_lastpublidate_2021_cve_iot_score0)*100)/(CV3_BASE_score_0_sh+CV3_BASE_score_0_iot))))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2021 LA PUNTUACION BASE ESTÁ ENTRE 0 y 1 \n")
    print("       -     EN EL "+str(float((((count_lastpublidate_2020_cve_sh_score0+count_lastpublidate_2020_cve_iot_score0)*100)/(CV3_BASE_score_0_sh+CV3_BASE_score_0_iot))))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2020 LA PUNTUACION BASE ESTÁ ENTRE 0 y 1 \n")
    print("       -     EN EL "+str(float((((count_lastpublidate_2019_cve_sh_score0+count_lastpublidate_2019_cve_iot_score0)*100)/(CV3_BASE_score_0_sh+CV3_BASE_score_0_iot))))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2019 LA PUNTUACION BASE ESTÁ ENTRE 0 y 1 \n")
    print("       -     EN EL "+str(float((((count_lastpublidate_2018_cve_sh_score0+count_lastpublidate_2018_cve_iot_score0)*100)/(CV3_BASE_score_0_sh+CV3_BASE_score_0_iot))))+"% DE LAS VULNERABILIDADES PUBLICADAS EN 2018 O ANTERIORMENTE LA PUNTUACION BASE ESTÁ ENTRE 0 y 1 \n")



