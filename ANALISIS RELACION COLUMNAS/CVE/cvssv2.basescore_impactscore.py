
import pandas as pd

#Abro los ficheros con los que voy a tratar

df_cve_iot=pd.read_excel('cves_iot_2023.xlsx')
df_cve_sh=pd.read_excel('cves_smart_home_2023.xlsx')


#Variables donde almacenare el contador de niveles de  IMPACTO segun severidad

count_high_severity_cvssV2_iot_0_impact=0
count_high_severity_cvssV2_iot_0_impact=0
count_high_severity_cvssV2_iot_1_impact=0
count_high_severity_cvssV2_iot_1_impact=0
count_high_severity_cvssV2_iot_2_impact=0
count_high_severity_cvssV2_iot_2_impact=0
count_high_severity_cvssV2_iot_3_impact=0
count_high_severity_cvssV2_iot_3_impact=0
count_high_severity_cvssV2_iot_4_impact=0
count_high_severity_cvssV2_iot_4_impact=0
count_high_severity_cvssV2_iot_5_impact=0
count_high_severity_cvssV2_iot_5_impact=0
count_high_severity_cvssV2_iot_6_impact=0
count_high_severity_cvssV2_iot_6_impact=0
count_high_severity_cvssV2_iot_7_impact=0
count_high_severity_cvssV2_iot_7_impact=0
count_high_severity_cvssV2_iot_8_impact=0
count_high_severity_cvssV2_iot_8_impact=0
count_high_severity_cvssV2_iot_9_impact=0
count_high_severity_cvssV2_iot_9_impact=0
count_high_severity_cvssV2_iot_10_impact=0
count_high_severity_cvssV2_iot_10_impact=0
count_high_severity_cvssV2_iot_impact=0
counter_high_severity_cvssV2_iot_impact=0
count_high_severity_cvssV2_iot_impact=0
counter_high_severity_cvssV2_iot_impact=0
counter_high_severity_cvssV2_iot=0

count_low_severity_cvssV2_iot_0_impact=0
count_low_severity_cvssV2_iot_0_impact=0
count_low_severity_cvssV2_iot_1_impact=0
count_low_severity_cvssV2_iot_1_impact=0
count_low_severity_cvssV2_iot_2_impact=0
count_low_severity_cvssV2_iot_2_impact=0
count_low_severity_cvssV2_iot_3_impact=0
count_low_severity_cvssV2_iot_3_impact=0
count_low_severity_cvssV2_iot_4_impact=0
count_low_severity_cvssV2_iot_4_impact=0
count_low_severity_cvssV2_iot_5_impact=0
count_low_severity_cvssV2_iot_5_impact=0
count_low_severity_cvssV2_iot_6_impact=0
count_low_severity_cvssV2_iot_6_impact=0
count_low_severity_cvssV2_iot_7_impact=0
count_low_severity_cvssV2_iot_7_impact=0
count_low_severity_cvssV2_iot_8_impact=0
count_low_severity_cvssV2_iot_8_impact=0
count_low_severity_cvssV2_iot_9_impact=0
count_low_severity_cvssV2_iot_9_impact=0
count_low_severity_cvssV2_iot_10_impact=0
count_low_severity_cvssV2_iot_10_impact=0
count_low_severity_cvssV2_iot_impact=0
count_low_severity_cvssV2_iot_impact=0
counter_low_severity_cvssV2_iot_impact=0
counter_low_severity_cvssV2_iot_impact=0
counter_low_severity_cvssV2_iot=0

count_medium_severity_cvssV2_iot_0_impact=0
count_medium_severity_cvssV2_iot_0_impact=0
count_medium_severity_cvssV2_iot_1_impact=0
count_medium_severity_cvssV2_iot_1_impact=0
count_medium_severity_cvssV2_iot_2_impact=0
count_medium_severity_cvssV2_iot_2_impact=0
count_medium_severity_cvssV2_iot_3_impact=0
count_medium_severity_cvssV2_iot_3_impact=0
count_medium_severity_cvssV2_iot_4_impact=0
count_medium_severity_cvssV2_iot_4_impact=0
count_medium_severity_cvssV2_iot_5_impact=0
count_medium_severity_cvssV2_iot_5_impact=0
count_medium_severity_cvssV2_iot_6_impact=0
count_medium_severity_cvssV2_iot_6_impact=0
count_medium_severity_cvssV2_iot_7_impact=0
count_medium_severity_cvssV2_iot_7_impact=0
count_medium_severity_cvssV2_iot_8_impact=0
count_medium_severity_cvssV2_iot_8_impact=0
count_medium_severity_cvssV2_iot_9_impact=0
count_medium_severity_cvssV2_iot_9_impact=0
count_medium_severity_cvssV2_iot_10_impact=0
count_medium_severity_cvssV2_iot_10_impact=0
count_medium_severity_cvssV2_iot_impact=0
count_medium_severity_cvssV2_iot_impact=0
counter_medium_severity_cvssV2_iot_impact=0
counter_medium_severity_cvssV2_iot_impact=0
counter_medium_severity_cvssV2_iot=0

#Recorro los valores de SEVERIDAD BASE y aumento los contadores segun su valor

for j in range(0,len(df_cve_iot["CVE_Items.impact.baseMetricV2.severity"])):
    if(df_cve_iot["CVE_Items.impact.baseMetricV2.severity"][j]=='HIGH'):
        counter_high_severity_cvssV2_iot+=1
        if(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"][j] !='NONE'):
            counter_high_severity_cvssV2_iot_impact+=1
            count_high_severity_cvssV2_iot_impact+=float(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"][j])
            if(((float(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"][j])) < 10.0) and ((float(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"][j])) >=9.0)):
                count_high_severity_cvssV2_iot_9_impact+=1
            elif(((float(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"][j])) < 9.0) and ((float(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"][j])) >=8.0)):
                count_high_severity_cvssV2_iot_8_impact+=1
            elif(((float(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"][j])) < 8.0) and ((float(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"][j])) >=7.0)):
                count_high_severity_cvssV2_iot_7_impact+=1
            elif(((float(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"][j])) < 7.0) and ((float(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"][j])) >=6.0)):
                count_high_severity_cvssV2_iot_6_impact+=1
            elif(((float(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"][j])) < 6.0) and ((float(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"][j])) >=5.0)):
                count_high_severity_cvssV2_iot_5_impact+=1
            elif(((float(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"][j])) < 5.0) and ((float(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"][j])) >=4.0)):
                count_high_severity_cvssV2_iot_4_impact+=1
            elif(((float(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"][j])) < 4.0) and ((float(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"][j])) >=3.0)):
                count_high_severity_cvssV2_iot_3_impact+=1
            elif(((float(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"][j])) < 3.0) and ((float(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"][j])) >=2.0)):
                count_high_severity_cvssV2_iot_2_impact+=1
            elif(((float(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"][j])) < 2.0) and ((float(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"][j])) >=1.0)):
                count_high_severity_cvssV2_iot_1_impact+=1
            elif(((float(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"][j])) < 1.0) and ((float(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"][j])) >=0.0)):
                count_high_severity_cvssV2_iot_0_impact+=1
            elif(((float(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"][j])) == 10.0)):
                count_high_severity_cvssV2_iot_10_impact+=1
    
    elif(df_cve_iot["CVE_Items.impact.baseMetricV2.severity"][j]=='LOW'):
        counter_low_severity_cvssV2_iot+=1
        if(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"][j] !='NONE'):
            counter_low_severity_cvssV2_iot_impact+=1
            count_low_severity_cvssV2_iot_impact+=float(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"][j])
            if(((float(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"][j])) < 10.0) and ((float(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"][j])) >=9.0)):
                count_low_severity_cvssV2_iot_9_impact+=1
            elif(((float(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"][j])) < 9.0) and ((float(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"][j])) >=8.0)):
                count_low_severity_cvssV2_iot_8_impact+=1
            elif(((float(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"][j])) < 8.0) and ((float(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"][j])) >=7.0)):
                count_low_severity_cvssV2_iot_7_impact+=1
            elif(((float(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"][j])) < 7.0) and ((float(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"][j])) >=6.0)):
                count_low_severity_cvssV2_iot_6_impact+=1
            elif(((float(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"][j])) < 6.0) and ((float(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"][j])) >=5.0)):
                count_low_severity_cvssV2_iot_5_impact+=1
            elif(((float(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"][j])) < 5.0) and ((float(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"][j])) >=4.0)):
                count_low_severity_cvssV2_iot_4_impact+=1
            elif(((float(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"][j])) < 4.0) and ((float(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"][j])) >=3.0)):
                count_low_severity_cvssV2_iot_3_impact+=1
            elif(((float(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"][j])) < 3.0) and ((float(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"][j])) >=2.0)):
                count_low_severity_cvssV2_iot_2_impact+=1
            elif(((float(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"][j])) < 2.0) and ((float(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"][j])) >=1.0)):
                count_low_severity_cvssV2_iot_1_impact+=1
            elif(((float(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"][j])) < 1.0) and ((float(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"][j])) >=0.0)):
                count_low_severity_cvssV2_iot_0_impact+=1
            elif(((float(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"][j])) == 10.0)):
                count_low_severity_cvssV2_iot_10_impact+=1
    
        
                
    elif(df_cve_iot["CVE_Items.impact.baseMetricV2.severity"][j]=='MEDIUM'):
        counter_medium_severity_cvssV2_iot+=1
        if(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"][j] !='NONE'):
            counter_medium_severity_cvssV2_iot_impact+=1
            count_medium_severity_cvssV2_iot_impact+=float(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"][j])
            if(((float(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"][j])) < 10.0) and ((float(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"][j])) >=9.0)):
                count_medium_severity_cvssV2_iot_9_impact+=1
            elif(((float(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"][j])) < 9.0) and ((float(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"][j])) >=8.0)):
                count_medium_severity_cvssV2_iot_8_impact+=1
            elif(((float(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"][j])) < 8.0) and ((float(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"][j])) >=7.0)):
                count_medium_severity_cvssV2_iot_7_impact+=1
            elif(((float(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"][j])) < 7.0) and ((float(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"][j])) >=6.0)):
                count_medium_severity_cvssV2_iot_6_impact+=1
            elif(((float(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"][j])) < 6.0) and ((float(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"][j])) >=5.0)):
                count_medium_severity_cvssV2_iot_5_impact+=1
            elif(((float(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"][j])) < 5.0) and ((float(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"][j])) >=4.0)):
                count_medium_severity_cvssV2_iot_4_impact+=1
            elif(((float(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"][j])) < 4.0) and ((float(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"][j])) >=3.0)):
                count_medium_severity_cvssV2_iot_3_impact+=1
            elif(((float(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"][j])) < 3.0) and ((float(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"][j])) >=2.0)):
                count_medium_severity_cvssV2_iot_2_impact+=1
            elif(((float(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"][j])) < 2.0) and ((float(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"][j])) >=1.0)):
                count_medium_severity_cvssV2_iot_1_impact+=1
            elif(((float(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"][j])) < 1.0) and ((float(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"][j])) >=0.0)):
                count_medium_severity_cvssV2_iot_0_impact+=1
            elif(((float(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"][j])) == 10.0)):
                count_medium_severity_cvssV2_iot_10_impact+=1
    
        
    elif(df_cve_iot["CVE_Items.impact.baseMetricV2.severity"][j]=='CRITICAL'):
        counter_critical_severity_cvssV2_iot+=1
        if(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"][j] !='NONE'):
            counter_critical_severity_cvssV2_iot_impact+=1
            count_critical_severity_cvssV2_iot_impact+=float(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"][j])
            if(((float(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"][j])) < 10.0) and ((float(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"][j])) >=9.0)):
                count_critical_severity_cvssV2_iot_9_impact+=1
            elif(((float(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"][j])) < 9.0) and ((float(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"][j])) >=8.0)):
                count_critical_severity_cvssV2_iot_8_impact+=1
            elif(((float(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"][j])) < 8.0) and ((float(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"][j])) >=7.0)):
                count_critical_severity_cvssV2_iot_7_impact+=1
            elif(((float(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"][j])) < 7.0) and ((float(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"][j])) >=6.0)):
                count_critical_severity_cvssV2_iot_6_impact+=1
            elif(((float(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"][j])) < 6.0) and ((float(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"][j])) >=5.0)):
                count_critical_severity_cvssV2_iot_5_impact+=1
            elif(((float(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"][j])) < 5.0) and ((float(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"][j])) >=4.0)):
                count_critical_severity_cvssV2_iot_4_impact+=1
            elif(((float(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"][j])) < 4.0) and ((float(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"][j])) >=3.0)):
                count_critical_severity_cvssV2_iot_3_impact+=1
            elif(((float(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"][j])) < 3.0) and ((float(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"][j])) >=2.0)):
                count_critical_severity_cvssV2_iot_2_impact+=1
            elif(((float(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"][j])) < 2.0) and ((float(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"][j])) >=1.0)):
                count_critical_severity_cvssV2_iot_1_impact+=1
            elif(((float(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"][j])) < 1.0) and ((float(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"][j])) >=0.0)):
                count_critical_severity_cvssV2_iot_0_impact+=1
            elif(((float(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"][j])) == 10.0)):
                count_critical_severity_cvssV2_iot_10_impact+=1
    
        


print("************************** ESTADÍSTICAS SEVERIDAD BASE EN CVE CVSSV2 IOT********************************")
print("\n")
print("\n")
print(" DE UN TOTAL DE "+str(counter_high_severity_cvssV2_iot+counter_low_severity_cvssV2_iot+counter_medium_severity_cvssV2_iot)+" VULNERABILIDADES DONDE LA SEVERIDAD ESTÁ DEFINIDA, LAS ESTADÍSTICAS DE PUNTUACION DE IMPACTO Y IMPACTO SON LAS SIGUIENTES :")
print("\n")
print("  - EN  "+str(counter_high_severity_cvssV2_iot)+" VULNERABILIDADES DONDE LA SEVERIDAD ES ALTA, LAS ESTADISTICAS DE PUNTUACION DE IMPACTO SON LAS SIGUIENTES:  \n")
print("\n")
print("      -    EN  "+str(count_high_severity_cvssV2_iot_10_impact)+" VULNERABILIDADES DONDE LA SEVERIDAD ES ALTA, LA PUNTUACION DE IMPACTO ES 10  \n")
print("      -    EN  "+str(count_high_severity_cvssV2_iot_9_impact)+" VULNERABILIDADES DONDE LA SEVERIDAD ES ALTA, LA PUNTUACION DE IMPACTO ESTÁ ENTRE 9 Y 10  \n")
print("      -    EN  "+str(count_high_severity_cvssV2_iot_8_impact)+" VULNERABILIDADES DONDE LA SEVERIDAD ES ALTA, LA PUNTUACION DE IMPACTO ESTÁ ENTRE 8 Y 9  \n")
print("      -    EN  "+str(count_high_severity_cvssV2_iot_7_impact)+" VULNERABILIDADES DONDE LA SEVERIDAD ES ALTA, LA PUNTUACION DE IMPACTO ESTÁ ENTRE 7 Y 8  \n")
print("      -    EN  "+str(count_high_severity_cvssV2_iot_6_impact)+" VULNERABILIDADES DONDE LA SEVERIDAD ES ALTA, LA PUNTUACION DE IMPACTO ESTÁ ENTRE 6 Y 7  \n")
print("      -    EN  "+str(count_high_severity_cvssV2_iot_5_impact)+" VULNERABILIDADES DONDE LA SEVERIDAD ES ALTA, LA PUNTUACION DE IMPACTO ESTÁ ENTRE 5 Y 6  \n")
print("      -    EN  "+str(count_high_severity_cvssV2_iot_4_impact)+" VULNERABILIDADES DONDE LA SEVERIDAD ES ALTA, LA PUNTUACION DE IMPACTO ESTÁ ENTRE 4 Y 5  \n")
print("      -    EN  "+str(count_high_severity_cvssV2_iot_3_impact)+" VULNERABILIDADES DONDE LA SEVERIDAD ES ALTA, LA PUNTUACION DE IMPACTO ESTÁ ENTRE 3 Y 4  \n")
print("      -    EN  "+str(count_high_severity_cvssV2_iot_2_impact)+" VULNERABILIDADES DONDE LA SEVERIDAD ES ALTA, LA PUNTUACION DE IMPACTO ESTÁ ENTRE 2 Y 3  \n")
print("      -    EN  "+str(count_high_severity_cvssV2_iot_1_impact)+" VULNERABILIDADES DONDE LA SEVERIDAD ES ALTA, LA PUNTUACION DE IMPACTO ESTÁ ENTRE 1 Y 2  \n")
print("      -    EN  "+str(count_high_severity_cvssV2_iot_0_impact)+" VULNERABILIDADES DONDE LA SEVERIDAD ES ALTA, LA PUNTUACION DE IMPACTO ESTÁ ENTRE 0 Y 1  \n")
print("\n")

print("  - EN "+str(counter_low_severity_cvssV2_iot)+" VULNERABILIDADES DONDE LA SEVERIDAD ES BAJA, LAS ESTADISTICAS DE PUNTUACION DE IMPACTO SON LAS SIGUIENTES:  \n")
print("\n")
print("      -    EN  "+str(count_low_severity_cvssV2_iot_10_impact)+" VULNERABILIDADES DONDE LA SEVERIDAD ES BAJA, LA PUNTUACION DE IMPACTO ES 10  \n")
print("      -    EN  "+str(count_low_severity_cvssV2_iot_9_impact)+" VULNERABILIDADES DONDE LA SEVERIDAD ES BAJA, LA PUNTUACION DE IMPACTO ESTÁ ENTRE 9 Y 10  \n")
print("      -    EN  "+str(count_low_severity_cvssV2_iot_8_impact)+" VULNERABILIDADES DONDE LA SEVERIDAD ES BAJA, LA PUNTUACION DE IMPACTO ESTÁ ENTRE 8 Y 9  \n")
print("      -    EN  "+str(count_low_severity_cvssV2_iot_7_impact)+" VULNERABILIDADES DONDE LA SEVERIDAD ES BAJA, LA PUNTUACION DE IMPACTO ESTÁ ENTRE 7 Y 8  \n")
print("      -    EN  "+str(count_low_severity_cvssV2_iot_6_impact)+" VULNERABILIDADES DONDE LA SEVERIDAD ES BAJA, LA PUNTUACION DE IMPACTO ESTÁ ENTRE 6 Y 7  \n")
print("      -    EN  "+str(count_low_severity_cvssV2_iot_5_impact)+" VULNERABILIDADES DONDE LA SEVERIDAD ES BAJA, LA PUNTUACION DE IMPACTO ESTÁ ENTRE 5 Y 6  \n")
print("      -    EN  "+str(count_low_severity_cvssV2_iot_4_impact)+" VULNERABILIDADES DONDE LA SEVERIDAD ES BAJA, LA PUNTUACION DE IMPACTO ESTÁ ENTRE 4 Y 5  \n")
print("      -    EN  "+str(count_low_severity_cvssV2_iot_3_impact)+" VULNERABILIDADES DONDE LA SEVERIDAD ES BAJA, LA PUNTUACION DE IMPACTO ESTÁ ENTRE 3 Y 4 \ n")
print("      -    EN  "+str(count_low_severity_cvssV2_iot_2_impact)+" VULNERABILIDADES DONDE LA SEVERIDAD ES BAJA, LA PUNTUACION DE IMPACTO ESTÁ ENTRE 2 Y 3  \n")
print("      -    EN  "+str(count_low_severity_cvssV2_iot_1_impact)+" VULNERABILIDADES DONDE LA SEVERIDAD ES BAJA, LA PUNTUACION DE IMPACTO ESTÁ ENTRE 1 Y 2  \n")
print("      -    EN  "+str(count_low_severity_cvssV2_iot_0_impact)+" VULNERABILIDADES DONDE LA SEVERIDAD ES BAJA, LA PUNTUACION DE IMPACTO ESTÁ ENTRE 0 Y 1  \n")
print("\n")

print("  - EN  "+str(counter_medium_severity_cvssV2_iot)+" VULNERABILIDADES DONDE LA SEVERIDAD ES MEDIA, LAS ESTADISTICAS DE PUNTUACION DE IMPACTO SON LAS SIGUIENTES:  \n")
print("\n")
print("      -    EN  "+str(count_medium_severity_cvssV2_iot_10_impact)+" VULNERABILIDADES DONDE LA SEVERIDAD ES MEDIA, LA PUNTUACION DE IMPACTO ES 10  \n")
print("      -    EN  "+str(count_medium_severity_cvssV2_iot_9_impact)+" VULNERABILIDADES DONDE LA SEVERIDAD ES MEDIA, LA PUNTUACION DE IMPACTO ESTÁ ENTRE 9 Y 10  \n")
print("      -    EN  "+str(count_medium_severity_cvssV2_iot_8_impact)+" VULNERABILIDADES DONDE LA SEVERIDAD ES MEDIA, LA PUNTUACION DE IMPACTO ESTÁ ENTRE 8 Y 9  \n")
print("      -    EN  "+str(count_medium_severity_cvssV2_iot_7_impact)+" VULNERABILIDADES DONDE LA SEVERIDAD ES MEDIA, LA PUNTUACION DE IMPACTO ESTÁ ENTRE 7 Y 8  \n")
print("      -    EN  "+str(count_medium_severity_cvssV2_iot_6_impact)+" VULNERABILIDADES DONDE LA SEVERIDAD ES MEDIA, LA PUNTUACION DE IMPACTO ESTÁ ENTRE 6 Y 7  \n")
print("      -    EN  "+str(count_medium_severity_cvssV2_iot_5_impact)+" VULNERABILIDADES DONDE LA SEVERIDAD ES MEDIA, LA PUNTUACION DE IMPACTO ESTÁ ENTRE 5 Y 6  \n")
print("      -    EN  "+str(count_medium_severity_cvssV2_iot_4_impact)+" VULNERABILIDADES DONDE LA SEVERIDAD ES MEDIA, LA PUNTUACION DE IMPACTO ESTÁ ENTRE 4 Y 5  \n")
print("      -    EN  "+str(count_medium_severity_cvssV2_iot_3_impact)+" VULNERABILIDADES DONDE LA SEVERIDAD ES MEDIA, LA PUNTUACION DE IMPACTO ESTÁ ENTRE 3 Y 4 \ n")
print("      -    EN  "+str(count_medium_severity_cvssV2_iot_2_impact)+" VULNERABILIDADES DONDE LA SEVERIDAD ES MEDIA, LA PUNTUACION DE IMPACTO ESTÁ ENTRE 2 Y 3  \n")
print("      -    EN  "+str(count_medium_severity_cvssV2_iot_1_impact)+" VULNERABILIDADES DONDE LA SEVERIDAD ES MEDIA, LA PUNTUACION DE IMPACTO ESTÁ ENTRE 1 Y 2  \n")
print("      -    EN  "+str(count_medium_severity_cvssV2_iot_0_impact)+" VULNERABILIDADES DONDE LA SEVERIDAD ES MEDIA, LA PUNTUACION DE IMPACTO ESTÁ ENTRE 0 Y 1  \n")
print("\n")

print("**************************PORCENTAJE SEVERIDAD BASE EN CVE CVSSV2 IOT********************************")
print("\n")
print("\n")
print(" DE UN TOTAL DE "+str(counter_high_severity_cvssV2_iot+counter_low_severity_cvssV2_iot+counter_medium_severity_cvssV2_iot)+" VULNERABILIDADES DONDE LA SEVERIDAD ESTÁ DEFINIDA, LOS PORCENTAJES DE PUNTUACION DE IMPACTO Y IMPACTO SON LOS SIGUIENTES :")
print("\n")
print("  - EN  EL "+str(float(((counter_high_severity_cvssV2_iot*100)/len(df_cve_iot["CVE_Items.impact.baseMetricV2.severity"]))))+" % DE LAS VULNERABILIDADES DONDE LA SEVERIDAD ES ALTA, LOS PORCENTAJES DE PUNTUACION DE IMPACTO SON LOS SIGUIENTES:  \n")
print("\n")
print("      -    EN  EL "+str(float(((count_high_severity_cvssV2_iot_10_impact*100)/counter_high_severity_cvssV2_iot_impact)))+" % DE VULNERABILIDADES CON SEVERIDAD ALTA, LA PUNTUACION DE IMPACTO ES 10  \n")
print("      -    EN  EL "+str(float(((count_high_severity_cvssV2_iot_9_impact*100)/counter_high_severity_cvssV2_iot_impact)))+" % DE VULNERABILIDADES CON SEVERIDAD ALTA, LA PUNTUACION DE IMPACTO ESTA ENTRE 9 Y 10  \n")
print("      -    EN  EL "+str(float(((count_high_severity_cvssV2_iot_8_impact*100)/counter_high_severity_cvssV2_iot_impact)))+" % DE VULNERABILIDADES CON SEVERIDAD ALTA, LA PUNTUACION DE IMPACTO ESTA ENTRE 8 Y 9  \n")
print("      -    EN  EL "+str(float(((count_high_severity_cvssV2_iot_7_impact*100)/counter_high_severity_cvssV2_iot_impact)))+" % DE VULNERABILIDADES CON SEVERIDAD ALTA, LA PUNTUACION DE IMPACTO ESTA ENTRE 7 Y 8  \n")
print("      -    EN  EL "+str(float(((count_high_severity_cvssV2_iot_6_impact*100)/counter_high_severity_cvssV2_iot_impact)))+" % DE VULNERABILIDADES CON SEVERIDAD ALTA, LA PUNTUACION DE IMPACTO ESTA ENTRE 6 Y 7  \n")
print("      -    EN  EL "+str(float(((count_high_severity_cvssV2_iot_5_impact*100)/counter_high_severity_cvssV2_iot_impact)))+" % DE VULNERABILIDADES CON SEVERIDAD ALTA, LA PUNTUACION DE IMPACTO ESTA ENTRE 5 Y 6  \n")
print("      -    EN  EL "+str(float(((count_high_severity_cvssV2_iot_4_impact*100)/counter_high_severity_cvssV2_iot_impact)))+" % DE VULNERABILIDADES CON SEVERIDAD ALTA, LA PUNTUACION DE IMPACTO ESTA ENTRE 4 Y 5  \n")
print("      -    EN  EL "+str(float(((count_high_severity_cvssV2_iot_3_impact*100)/counter_high_severity_cvssV2_iot_impact)))+" % DE VULNERABILIDADES CON SEVERIDAD ALTA, LA PUNTUACION DE IMPACTO ESTA ENTRE 3 Y 4  \n")
print("      -    EN  EL "+str(float(((count_high_severity_cvssV2_iot_2_impact*100)/counter_high_severity_cvssV2_iot_impact)))+" % DE VULNERABILIDADES CON SEVERIDAD ALTA, LA PUNTUACION DE IMPACTO ESTA ENTRE 2 Y 3  \n")
print("      -    EN  EL "+str(float(((count_high_severity_cvssV2_iot_1_impact*100)/counter_high_severity_cvssV2_iot_impact)))+" % DE VULNERABILIDADES CON SEVERIDAD ALTA, LA PUNTUACION DE IMPACTO ESTA ENTRE 1 Y 2  \n") 
print("      -    EN  EL "+str(float(((count_high_severity_cvssV2_iot_0_impact*100)/counter_high_severity_cvssV2_iot_impact)))+" % DE VULNERABILIDADES CON SEVERIDAD ALTA, LA PUNTUACION DE IMPACTO ESTA ENTRE 0 Y 1 \n")      
print("      -    LA PUNTUACION MEDIA DE IMPACTO EN LAS VULNERABILIDADES CON SEVERIDAD ALTA ES : "+str(float((count_high_severity_cvssV2_iot_impact/counter_high_severity_cvssV2_iot_impact)))+"\n")      

print("  - EN  EL "+str(float(((counter_low_severity_cvssV2_iot*100)/len(df_cve_iot["CVE_Items.impact.baseMetricV2.severity"]))))+" % DE LAS VULNERABILIDADES DONDE LA SEVERIDAD ES BAJA, LOS PORCENTAJES DE PUNTUACION DE IMPACTO SON LOS SIGUIENTES:  \n")
print("\n")
print("      -    EN  EL "+str(float(((count_low_severity_cvssV2_iot_10_impact*100)/counter_low_severity_cvssV2_iot_impact)))+" % DE VULNERABILIDADES CON SEVERIDAD BAJA, LA PUNTUACION DE IMPACTO ES 10  \n")
print("      -    EN  EL "+str(float(((count_low_severity_cvssV2_iot_9_impact*100)/counter_low_severity_cvssV2_iot_impact)))+" % DE VULNERABILIDADES CON SEVERIDAD BAJA, LA PUNTUACION DE IMPACTO ESTA ENTRE 9 Y 10  \n")
print("      -    EN  EL "+str(float(((count_low_severity_cvssV2_iot_8_impact*100)/counter_low_severity_cvssV2_iot_impact)))+" % DE VULNERABILIDADES CON SEVERIDAD BAJA, LA PUNTUACION DE IMPACTO ESTA ENTRE 8 Y 9  \n")
print("      -    EN  EL "+str(float(((count_low_severity_cvssV2_iot_7_impact*100)/counter_low_severity_cvssV2_iot_impact)))+" % DE VULNERABILIDADES CON SEVERIDAD BAJA, LA PUNTUACION DE IMPACTO ESTA ENTRE 7 Y 8  \n")
print("      -    EN  EL "+str(float(((count_low_severity_cvssV2_iot_6_impact*100)/counter_low_severity_cvssV2_iot_impact)))+" % DE VULNERABILIDADES CON SEVERIDAD BAJA, LA PUNTUACION DE IMPACTO ESTA ENTRE 6 Y 7  \n")
print("      -    EN  EL "+str(float(((count_low_severity_cvssV2_iot_5_impact*100)/counter_low_severity_cvssV2_iot_impact)))+" % DE VULNERABILIDADES CON SEVERIDAD BAJA, LA PUNTUACION DE IMPACTO ESTA ENTRE 5 Y 6  \n")
print("      -    EN  EL "+str(float(((count_low_severity_cvssV2_iot_4_impact*100)/counter_low_severity_cvssV2_iot_impact)))+" % DE VULNERABILIDADES CON SEVERIDAD BAJA, LA PUNTUACION DE IMPACTO ESTA ENTRE 4 Y 5  \n")
print("      -    EN  EL "+str(float(((count_low_severity_cvssV2_iot_3_impact*100)/counter_low_severity_cvssV2_iot_impact)))+" % DE VULNERABILIDADES CON SEVERIDAD BAJA, LA PUNTUACION DE IMPACTO ESTA ENTRE 3 Y 4  \n")
print("      -    EN  EL "+str(float(((count_low_severity_cvssV2_iot_2_impact*100)/counter_low_severity_cvssV2_iot_impact)))+" % DE VULNERABILIDADES CON SEVERIDAD BAJA, LA PUNTUACION DE IMPACTO ESTA ENTRE 2 Y 3  \n")
print("      -    EN  EL "+str(float(((count_low_severity_cvssV2_iot_1_impact*100)/counter_low_severity_cvssV2_iot_impact)))+" % DE VULNERABILIDADES CON SEVERIDAD BAJA, LA PUNTUACION DE IMPACTO ESTA ENTRE 1 Y 2  \n") 
print("      -    EN  EL "+str(float(((count_low_severity_cvssV2_iot_0_impact*100)/counter_low_severity_cvssV2_iot_impact)))+" % DE VULNERABILIDADES CON SEVERIDAD BAJA, LA PUNTUACION DE IMPACTO ESTA ENTRE 0 Y 1 \n")      
print("      -    LA PUNTUACION MEDIA DE IMPACTO EN LAS VULNERABILIDADES CON SEVERIDAD BAJA ES : "+str(float((count_low_severity_cvssV2_iot_impact/counter_low_severity_cvssV2_iot_impact)))+"\n")      
print("\n")

print("  - EN  EL "+str(float(((counter_medium_severity_cvssV2_iot*100)/len(df_cve_iot["CVE_Items.impact.baseMetricV2.severity"]))))+" % DE LAS VULNERABILIDADES DONDE LA SEVERIDAD ES MEDIA, LOS PORCENTAJES DE PUNTUACION DE IMPACTO SON LOS SIGUIENTES:  \n")
print("\n")
print("      -    EN  EL "+str(float(((count_medium_severity_cvssV2_iot_10_impact*100)/counter_medium_severity_cvssV2_iot_impact)))+" % DE VULNERABILIDADES CON SEVERIDAD MEDIA, LA PUNTUACION DE IMPACTO ES 10  \n")
print("      -    EN  EL "+str(float(((count_medium_severity_cvssV2_iot_9_impact*100)/counter_medium_severity_cvssV2_iot_impact)))+" % DE VULNERABILIDADES CON SEVERIDAD MEDIA, LA PUNTUACION DE IMPACTO ESTA ENTRE 9 Y 10  \n")
print("      -    EN  EL "+str(float(((count_medium_severity_cvssV2_iot_8_impact*100)/counter_medium_severity_cvssV2_iot_impact)))+" % DE VULNERABILIDADES CON SEVERIDAD MEDIA, LA PUNTUACION DE IMPACTO ESTA ENTRE 8 Y 9  \n")
print("      -    EN  EL "+str(float(((count_medium_severity_cvssV2_iot_7_impact*100)/counter_medium_severity_cvssV2_iot_impact)))+" % DE VULNERABILIDADES CON SEVERIDAD MEDIA, LA PUNTUACION DE IMPACTO ESTA ENTRE 7 Y 8  \n")
print("      -    EN  EL "+str(float(((count_medium_severity_cvssV2_iot_6_impact*100)/counter_medium_severity_cvssV2_iot_impact)))+" % DE VULNERABILIDADES CON SEVERIDAD MEDIA, LA PUNTUACION DE IMPACTO ESTA ENTRE 6 Y 7  \n")
print("      -    EN  EL "+str(float(((count_medium_severity_cvssV2_iot_5_impact*100)/counter_medium_severity_cvssV2_iot_impact)))+" % DE VULNERABILIDADES CON SEVERIDAD MEDIA, LA PUNTUACION DE IMPACTO ESTA ENTRE 5 Y 6  \n")
print("      -    EN  EL "+str(float(((count_medium_severity_cvssV2_iot_4_impact*100)/counter_medium_severity_cvssV2_iot_impact)))+" % DE VULNERABILIDADES CON SEVERIDAD MEDIA, LA PUNTUACION DE IMPACTO ESTA ENTRE 4 Y 5  \n")
print("      -    EN  EL "+str(float(((count_medium_severity_cvssV2_iot_3_impact*100)/counter_medium_severity_cvssV2_iot_impact)))+" % DE VULNERABILIDADES CON SEVERIDAD MEDIA, LA PUNTUACION DE IMPACTO ESTA ENTRE 3 Y 4  \n")
print("      -    EN  EL "+str(float(((count_medium_severity_cvssV2_iot_2_impact*100)/counter_medium_severity_cvssV2_iot_impact)))+" % DE VULNERABILIDADES CON SEVERIDAD MEDIA, LA PUNTUACION DE IMPACTO ESTA ENTRE 2 Y 3  \n")
print("      -    EN  EL "+str(float(((count_medium_severity_cvssV2_iot_1_impact*100)/counter_medium_severity_cvssV2_iot_impact)))+" % DE VULNERABILIDADES CON SEVERIDAD MEDIA, LA PUNTUACION DE IMPACTO ESTA ENTRE 1 Y 2  \n") 
print("      -    EN  EL "+str(float(((count_medium_severity_cvssV2_iot_0_impact*100)/counter_medium_severity_cvssV2_iot_impact)))+" % DE VULNERABILIDADES CON SEVERIDAD MEDIA, LA PUNTUACION DE IMPACTO ESTA ENTRE 0 Y 1 \n")      
print("      -    LA PUNTUACION MEDIA DE IMPACTO EN LAS VULNERABILIDADES CON SEVERIDAD MEDIA ES : "+str(float((count_medium_severity_cvssV2_iot_impact/counter_medium_severity_cvssV2_iot_impact)))+"\n")      
print("\n")


#Variables donde almacenare el contador de niveles de IMPACTO segun severidad

count_high_severity_cvssV2_sh_0_impact=0
count_high_severity_cvssV2_sh_0_impact=0
count_high_severity_cvssV2_sh_1_impact=0
count_high_severity_cvssV2_sh_1_impact=0
count_high_severity_cvssV2_sh_2_impact=0
count_high_severity_cvssV2_sh_2_impact=0
count_high_severity_cvssV2_sh_3_impact=0
count_high_severity_cvssV2_sh_3_impact=0
count_high_severity_cvssV2_sh_4_impact=0
count_high_severity_cvssV2_sh_4_impact=0
count_high_severity_cvssV2_sh_5_impact=0
count_high_severity_cvssV2_sh_5_impact=0
count_high_severity_cvssV2_sh_6_impact=0
count_high_severity_cvssV2_sh_6_impact=0
count_high_severity_cvssV2_sh_7_impact=0
count_high_severity_cvssV2_sh_7_impact=0
count_high_severity_cvssV2_sh_8_impact=0
count_high_severity_cvssV2_sh_8_impact=0
count_high_severity_cvssV2_sh_9_impact=0
count_high_severity_cvssV2_sh_9_impact=0
count_high_severity_cvssV2_sh_10_impact=0
count_high_severity_cvssV2_sh_10_impact=0
count_high_severity_cvssV2_sh_impact=0
counter_high_severity_cvssV2_sh_impact=0
count_high_severity_cvssV2_sh_impact=0
counter_high_severity_cvssV2_sh_impact=0
counter_high_severity_cvssV2_sh=0

count_low_severity_cvssV2_sh_0_impact=0
count_low_severity_cvssV2_sh_0_impact=0
count_low_severity_cvssV2_sh_1_impact=0
count_low_severity_cvssV2_sh_1_impact=0
count_low_severity_cvssV2_sh_2_impact=0
count_low_severity_cvssV2_sh_2_impact=0
count_low_severity_cvssV2_sh_3_impact=0
count_low_severity_cvssV2_sh_3_impact=0
count_low_severity_cvssV2_sh_4_impact=0
count_low_severity_cvssV2_sh_4_impact=0
count_low_severity_cvssV2_sh_5_impact=0
count_low_severity_cvssV2_sh_5_impact=0
count_low_severity_cvssV2_sh_6_impact=0
count_low_severity_cvssV2_sh_6_impact=0
count_low_severity_cvssV2_sh_7_impact=0
count_low_severity_cvssV2_sh_7_impact=0
count_low_severity_cvssV2_sh_8_impact=0
count_low_severity_cvssV2_sh_8_impact=0
count_low_severity_cvssV2_sh_9_impact=0
count_low_severity_cvssV2_sh_9_impact=0
count_low_severity_cvssV2_sh_10_impact=0
count_low_severity_cvssV2_sh_10_impact=0
count_low_severity_cvssV2_sh_impact=0
count_low_severity_cvssV2_sh_impact=0
counter_low_severity_cvssV2_sh_impact=0
counter_low_severity_cvssV2_sh_impact=0
counter_low_severity_cvssV2_sh=0

count_medium_severity_cvssV2_sh_0_impact=0
count_medium_severity_cvssV2_sh_0_impact=0
count_medium_severity_cvssV2_sh_1_impact=0
count_medium_severity_cvssV2_sh_1_impact=0
count_medium_severity_cvssV2_sh_2_impact=0
count_medium_severity_cvssV2_sh_2_impact=0
count_medium_severity_cvssV2_sh_3_impact=0
count_medium_severity_cvssV2_sh_3_impact=0
count_medium_severity_cvssV2_sh_4_impact=0
count_medium_severity_cvssV2_sh_4_impact=0
count_medium_severity_cvssV2_sh_5_impact=0
count_medium_severity_cvssV2_sh_5_impact=0
count_medium_severity_cvssV2_sh_6_impact=0
count_medium_severity_cvssV2_sh_6_impact=0
count_medium_severity_cvssV2_sh_7_impact=0
count_medium_severity_cvssV2_sh_7_impact=0
count_medium_severity_cvssV2_sh_8_impact=0
count_medium_severity_cvssV2_sh_8_impact=0
count_medium_severity_cvssV2_sh_9_impact=0
count_medium_severity_cvssV2_sh_9_impact=0
count_medium_severity_cvssV2_sh_10_impact=0
count_medium_severity_cvssV2_sh_10_impact=0
count_medium_severity_cvssV2_sh_impact=0
count_medium_severity_cvssV2_sh_impact=0
counter_medium_severity_cvssV2_sh_impact=0
counter_medium_severity_cvssV2_sh_impact=0
counter_medium_severity_cvssV2_sh=0



#Recorro los valores de SEVERIDAD BASE y aumento los contadores segun su valor

for j in range(0,len(df_cve_sh["CVE_Items.impact.baseMetricV2.severity"])):
    if(df_cve_sh["CVE_Items.impact.baseMetricV2.severity"][j]=='HIGH'):
        counter_high_severity_cvssV2_sh+=1
        if(df_cve_sh["CVE_Items.impact.baseMetricV2.impactScore"][j] !='NONE'):
            counter_high_severity_cvssV2_sh_impact+=1
            count_high_severity_cvssV2_sh_impact+=float(df_cve_sh["CVE_Items.impact.baseMetricV2.impactScore"][j])
            if(((float(df_cve_sh["CVE_Items.impact.baseMetricV2.impactScore"][j])) < 10.0) and ((float(df_cve_sh["CVE_Items.impact.baseMetricV2.impactScore"][j])) >=9.0)):
                count_high_severity_cvssV2_sh_9_impact+=1
            elif(((float(df_cve_sh["CVE_Items.impact.baseMetricV2.impactScore"][j])) < 9.0) and ((float(df_cve_sh["CVE_Items.impact.baseMetricV2.impactScore"][j])) >=8.0)):
                count_high_severity_cvssV2_sh_8_impact+=1
            elif(((float(df_cve_sh["CVE_Items.impact.baseMetricV2.impactScore"][j])) < 8.0) and ((float(df_cve_sh["CVE_Items.impact.baseMetricV2.impactScore"][j])) >=7.0)):
                count_high_severity_cvssV2_sh_7_impact+=1
            elif(((float(df_cve_sh["CVE_Items.impact.baseMetricV2.impactScore"][j])) < 7.0) and ((float(df_cve_sh["CVE_Items.impact.baseMetricV2.impactScore"][j])) >=6.0)):
                count_high_severity_cvssV2_sh_6_impact+=1
            elif(((float(df_cve_sh["CVE_Items.impact.baseMetricV2.impactScore"][j])) < 6.0) and ((float(df_cve_sh["CVE_Items.impact.baseMetricV2.impactScore"][j])) >=5.0)):
                count_high_severity_cvssV2_sh_5_impact+=1
            elif(((float(df_cve_sh["CVE_Items.impact.baseMetricV2.impactScore"][j])) < 5.0) and ((float(df_cve_sh["CVE_Items.impact.baseMetricV2.impactScore"][j])) >=4.0)):
                count_high_severity_cvssV2_sh_4_impact+=1
            elif(((float(df_cve_sh["CVE_Items.impact.baseMetricV2.impactScore"][j])) < 4.0) and ((float(df_cve_sh["CVE_Items.impact.baseMetricV2.impactScore"][j])) >=3.0)):
                count_high_severity_cvssV2_sh_3_impact+=1
            elif(((float(df_cve_sh["CVE_Items.impact.baseMetricV2.impactScore"][j])) < 3.0) and ((float(df_cve_sh["CVE_Items.impact.baseMetricV2.impactScore"][j])) >=2.0)):
                count_high_severity_cvssV2_sh_2_impact+=1
            elif(((float(df_cve_sh["CVE_Items.impact.baseMetricV2.impactScore"][j])) < 2.0) and ((float(df_cve_sh["CVE_Items.impact.baseMetricV2.impactScore"][j])) >=1.0)):
                count_high_severity_cvssV2_sh_1_impact+=1
            elif(((float(df_cve_sh["CVE_Items.impact.baseMetricV2.impactScore"][j])) < 1.0) and ((float(df_cve_sh["CVE_Items.impact.baseMetricV2.impactScore"][j])) >=0.0)):
                count_high_severity_cvssV2_sh_0_impact+=1
            elif(((float(df_cve_sh["CVE_Items.impact.baseMetricV2.impactScore"][j])) == 10.0)):
                count_high_severity_cvssV2_sh_10_impact+=1
    
        
    elif(df_cve_sh["CVE_Items.impact.baseMetricV2.severity"][j]=='LOW'):
        counter_low_severity_cvssV2_sh+=1
        if(df_cve_sh["CVE_Items.impact.baseMetricV2.impactScore"][j] !='NONE'):
            counter_low_severity_cvssV2_sh_impact+=1
            count_low_severity_cvssV2_sh_impact+=float(df_cve_sh["CVE_Items.impact.baseMetricV2.impactScore"][j])
            if(((float(df_cve_sh["CVE_Items.impact.baseMetricV2.impactScore"][j])) < 10.0) and ((float(df_cve_sh["CVE_Items.impact.baseMetricV2.impactScore"][j])) >=9.0)):
                count_low_severity_cvssV2_sh_9_impact+=1
            elif(((float(df_cve_sh["CVE_Items.impact.baseMetricV2.impactScore"][j])) < 9.0) and ((float(df_cve_sh["CVE_Items.impact.baseMetricV2.impactScore"][j])) >=8.0)):
                count_low_severity_cvssV2_sh_8_impact+=1
            elif(((float(df_cve_sh["CVE_Items.impact.baseMetricV2.impactScore"][j])) < 8.0) and ((float(df_cve_sh["CVE_Items.impact.baseMetricV2.impactScore"][j])) >=7.0)):
                count_low_severity_cvssV2_sh_7_impact+=1
            elif(((float(df_cve_sh["CVE_Items.impact.baseMetricV2.impactScore"][j])) < 7.0) and ((float(df_cve_sh["CVE_Items.impact.baseMetricV2.impactScore"][j])) >=6.0)):
                count_low_severity_cvssV2_sh_6_impact+=1
            elif(((float(df_cve_sh["CVE_Items.impact.baseMetricV2.impactScore"][j])) < 6.0) and ((float(df_cve_sh["CVE_Items.impact.baseMetricV2.impactScore"][j])) >=5.0)):
                count_low_severity_cvssV2_sh_5_impact+=1
            elif(((float(df_cve_sh["CVE_Items.impact.baseMetricV2.impactScore"][j])) < 5.0) and ((float(df_cve_sh["CVE_Items.impact.baseMetricV2.impactScore"][j])) >=4.0)):
                count_low_severity_cvssV2_sh_4_impact+=1
            elif(((float(df_cve_sh["CVE_Items.impact.baseMetricV2.impactScore"][j])) < 4.0) and ((float(df_cve_sh["CVE_Items.impact.baseMetricV2.impactScore"][j])) >=3.0)):
                count_low_severity_cvssV2_sh_3_impact+=1
            elif(((float(df_cve_sh["CVE_Items.impact.baseMetricV2.impactScore"][j])) < 3.0) and ((float(df_cve_sh["CVE_Items.impact.baseMetricV2.impactScore"][j])) >=2.0)):
                count_low_severity_cvssV2_sh_2_impact+=1
            elif(((float(df_cve_sh["CVE_Items.impact.baseMetricV2.impactScore"][j])) < 2.0) and ((float(df_cve_sh["CVE_Items.impact.baseMetricV2.impactScore"][j])) >=1.0)):
                count_low_severity_cvssV2_sh_1_impact+=1
            elif(((float(df_cve_sh["CVE_Items.impact.baseMetricV2.impactScore"][j])) < 1.0) and ((float(df_cve_sh["CVE_Items.impact.baseMetricV2.impactScore"][j])) >=0.0)):
                count_low_severity_cvssV2_sh_0_impact+=1
            elif(((float(df_cve_sh["CVE_Items.impact.baseMetricV2.impactScore"][j])) == 10.0)):
                count_low_severity_cvssV2_sh_10_impact+=1
    
        
                
    elif(df_cve_sh["CVE_Items.impact.baseMetricV2.severity"][j]=='MEDIUM'):
        counter_medium_severity_cvssV2_sh+=1
        if(df_cve_sh["CVE_Items.impact.baseMetricV2.impactScore"][j] !='NONE'):
            counter_medium_severity_cvssV2_sh_impact+=1
            count_medium_severity_cvssV2_sh_impact+=float(df_cve_sh["CVE_Items.impact.baseMetricV2.impactScore"][j])
            if(((float(df_cve_sh["CVE_Items.impact.baseMetricV2.impactScore"][j])) < 10.0) and ((float(df_cve_sh["CVE_Items.impact.baseMetricV2.impactScore"][j])) >=9.0)):
                count_medium_severity_cvssV2_sh_9_impact+=1
            elif(((float(df_cve_sh["CVE_Items.impact.baseMetricV2.impactScore"][j])) < 9.0) and ((float(df_cve_sh["CVE_Items.impact.baseMetricV2.impactScore"][j])) >=8.0)):
                count_medium_severity_cvssV2_sh_8_impact+=1
            elif(((float(df_cve_sh["CVE_Items.impact.baseMetricV2.impactScore"][j])) < 8.0) and ((float(df_cve_sh["CVE_Items.impact.baseMetricV2.impactScore"][j])) >=7.0)):
                count_medium_severity_cvssV2_sh_7_impact+=1
            elif(((float(df_cve_sh["CVE_Items.impact.baseMetricV2.impactScore"][j])) < 7.0) and ((float(df_cve_sh["CVE_Items.impact.baseMetricV2.impactScore"][j])) >=6.0)):
                count_medium_severity_cvssV2_sh_6_impact+=1
            elif(((float(df_cve_sh["CVE_Items.impact.baseMetricV2.impactScore"][j])) < 6.0) and ((float(df_cve_sh["CVE_Items.impact.baseMetricV2.impactScore"][j])) >=5.0)):
                count_medium_severity_cvssV2_sh_5_impact+=1
            elif(((float(df_cve_sh["CVE_Items.impact.baseMetricV2.impactScore"][j])) < 5.0) and ((float(df_cve_sh["CVE_Items.impact.baseMetricV2.impactScore"][j])) >=4.0)):
                count_medium_severity_cvssV2_sh_4_impact+=1
            elif(((float(df_cve_sh["CVE_Items.impact.baseMetricV2.impactScore"][j])) < 4.0) and ((float(df_cve_sh["CVE_Items.impact.baseMetricV2.impactScore"][j])) >=3.0)):
                count_medium_severity_cvssV2_sh_3_impact+=1
            elif(((float(df_cve_sh["CVE_Items.impact.baseMetricV2.impactScore"][j])) < 3.0) and ((float(df_cve_sh["CVE_Items.impact.baseMetricV2.impactScore"][j])) >=2.0)):
                count_medium_severity_cvssV2_sh_2_impact+=1
            elif(((float(df_cve_sh["CVE_Items.impact.baseMetricV2.impactScore"][j])) < 2.0) and ((float(df_cve_sh["CVE_Items.impact.baseMetricV2.impactScore"][j])) >=1.0)):
                count_medium_severity_cvssV2_sh_1_impact+=1
            elif(((float(df_cve_sh["CVE_Items.impact.baseMetricV2.impactScore"][j])) < 1.0) and ((float(df_cve_sh["CVE_Items.impact.baseMetricV2.impactScore"][j])) >=0.0)):
                count_medium_severity_cvssV2_sh_0_impact+=1
            elif(((float(df_cve_sh["CVE_Items.impact.baseMetricV2.impactScore"][j])) == 10.0)):
                count_medium_severity_cvssV2_sh_10_impact+=1
    


print("************************** ESTADÍSTICAS SEVERIDAD BASE EN CVE CVSSV2 SMART HOME********************************")
print("\n")
print("\n")
print(" DE UN TOTAL DE "+str(counter_high_severity_cvssV2_sh+counter_low_severity_cvssV2_sh+counter_medium_severity_cvssV2_sh)+" VULNERABILIDADES DONDE LA SEVERIDAD ESTÁ DEFINIDA, LAS ESTADÍSTICAS DE PUNTUACION DE IMPACTO Y IMPACTO SON LAS SIGUIENTES :")
print("\n")
print("  - EN  "+str(counter_high_severity_cvssV2_sh)+" VULNERABILIDADES DONDE LA SEVERIDAD ES ALTA, LAS ESTADISTICAS DE PUNTUACION DE IMPACTO SON LAS SIGUIENTES:  \n")
print("\n")
print("      -    EN  "+str(count_high_severity_cvssV2_sh_10_impact)+" VULNERABILIDADES DONDE LA SEVERIDAD ES ALTA, LA PUNTUACION DE IMPACTO ES 10  \n")
print("      -    EN  "+str(count_high_severity_cvssV2_sh_9_impact)+" VULNERABILIDADES DONDE LA SEVERIDAD ES ALTA, LA PUNTUACION DE IMPACTO ESTÁ ENTRE 9 Y 10  \n")
print("      -    EN  "+str(count_high_severity_cvssV2_sh_8_impact)+" VULNERABILIDADES DONDE LA SEVERIDAD ES ALTA, LA PUNTUACION DE IMPACTO ESTÁ ENTRE 8 Y 9  \n")
print("      -    EN  "+str(count_high_severity_cvssV2_sh_7_impact)+" VULNERABILIDADES DONDE LA SEVERIDAD ES ALTA, LA PUNTUACION DE IMPACTO ESTÁ ENTRE 7 Y 8  \n")
print("      -    EN  "+str(count_high_severity_cvssV2_sh_6_impact)+" VULNERABILIDADES DONDE LA SEVERIDAD ES ALTA, LA PUNTUACION DE IMPACTO ESTÁ ENTRE 6 Y 7  \n")
print("      -    EN  "+str(count_high_severity_cvssV2_sh_5_impact)+" VULNERABILIDADES DONDE LA SEVERIDAD ES ALTA, LA PUNTUACION DE IMPACTO ESTÁ ENTRE 5 Y 6  \n")
print("      -    EN  "+str(count_high_severity_cvssV2_sh_4_impact)+" VULNERABILIDADES DONDE LA SEVERIDAD ES ALTA, LA PUNTUACION DE IMPACTO ESTÁ ENTRE 4 Y 5  \n")
print("      -    EN  "+str(count_high_severity_cvssV2_sh_3_impact)+" VULNERABILIDADES DONDE LA SEVERIDAD ES ALTA, LA PUNTUACION DE IMPACTO ESTÁ ENTRE 3 Y 4  \n")
print("      -    EN  "+str(count_high_severity_cvssV2_sh_2_impact)+" VULNERABILIDADES DONDE LA SEVERIDAD ES ALTA, LA PUNTUACION DE IMPACTO ESTÁ ENTRE 2 Y 3  \n")
print("      -    EN  "+str(count_high_severity_cvssV2_sh_1_impact)+" VULNERABILIDADES DONDE LA SEVERIDAD ES ALTA, LA PUNTUACION DE IMPACTO ESTÁ ENTRE 1 Y 2  \n")
print("      -    EN  "+str(count_high_severity_cvssV2_sh_0_impact)+" VULNERABILIDADES DONDE LA SEVERIDAD ES ALTA, LA PUNTUACION DE IMPACTO ESTÁ ENTRE 0 Y 1  \n")
print("\n")
print("\n")
print("  - EN "+str(counter_low_severity_cvssV2_sh)+" VULNERABILIDADES DONDE LA SEVERIDAD ES BAJA, LAS ESTADISTICAS DE PUNTUACION DE IMPACTO SON LAS SIGUIENTES:  \n")
print("\n")
print("      -    EN  "+str(count_low_severity_cvssV2_sh_10_impact)+" VULNERABILIDADES DONDE LA SEVERIDAD ES BAJA, LA PUNTUACION DE IMPACTO ES 10  \n")
print("      -    EN  "+str(count_low_severity_cvssV2_sh_9_impact)+" VULNERABILIDADES DONDE LA SEVERIDAD ES BAJA, LA PUNTUACION DE IMPACTO ESTÁ ENTRE 9 Y 10  \n")
print("      -    EN  "+str(count_low_severity_cvssV2_sh_8_impact)+" VULNERABILIDADES DONDE LA SEVERIDAD ES BAJA, LA PUNTUACION DE IMPACTO ESTÁ ENTRE 8 Y 9  \n")
print("      -    EN  "+str(count_low_severity_cvssV2_sh_7_impact)+" VULNERABILIDADES DONDE LA SEVERIDAD ES BAJA, LA PUNTUACION DE IMPACTO ESTÁ ENTRE 7 Y 8  \n")
print("      -    EN  "+str(count_low_severity_cvssV2_sh_6_impact)+" VULNERABILIDADES DONDE LA SEVERIDAD ES BAJA, LA PUNTUACION DE IMPACTO ESTÁ ENTRE 6 Y 7  \n")
print("      -    EN  "+str(count_low_severity_cvssV2_sh_5_impact)+" VULNERABILIDADES DONDE LA SEVERIDAD ES BAJA, LA PUNTUACION DE IMPACTO ESTÁ ENTRE 5 Y 6  \n")
print("      -    EN  "+str(count_low_severity_cvssV2_sh_4_impact)+" VULNERABILIDADES DONDE LA SEVERIDAD ES BAJA, LA PUNTUACION DE IMPACTO ESTÁ ENTRE 4 Y 5  \n")
print("      -    EN  "+str(count_low_severity_cvssV2_sh_3_impact)+" VULNERABILIDADES DONDE LA SEVERIDAD ES BAJA, LA PUNTUACION DE IMPACTO ESTÁ ENTRE 3 Y 4 \ n")
print("      -    EN  "+str(count_low_severity_cvssV2_sh_2_impact)+" VULNERABILIDADES DONDE LA SEVERIDAD ES BAJA, LA PUNTUACION DE IMPACTO ESTÁ ENTRE 2 Y 3  \n")
print("      -    EN  "+str(count_low_severity_cvssV2_sh_1_impact)+" VULNERABILIDADES DONDE LA SEVERIDAD ES BAJA, LA PUNTUACION DE IMPACTO ESTÁ ENTRE 1 Y 2  \n")
print("      -    EN  "+str(count_low_severity_cvssV2_sh_0_impact)+" VULNERABILIDADES DONDE LA SEVERIDAD ES BAJA, LA PUNTUACION DE IMPACTO ESTÁ ENTRE 0 Y 1  \n")
print("\n")

print("  - EN  "+str(counter_medium_severity_cvssV2_sh)+" VULNERABILIDADES DONDE LA SEVERIDAD ES MEDIA, LAS ESTADISTICAS DE PUNTUACION DE IMPACTO SON LAS SIGUIENTES:  \n")
print("\n")
print("      -    EN  "+str(count_medium_severity_cvssV2_sh_10_impact)+" VULNERABILIDADES DONDE LA SEVERIDAD ES MEDIA, LA PUNTUACION DE IMPACTO ES 10  \n")
print("      -    EN  "+str(count_medium_severity_cvssV2_sh_9_impact)+" VULNERABILIDADES DONDE LA SEVERIDAD ES MEDIA, LA PUNTUACION DE IMPACTO ESTÁ ENTRE 9 Y 10  \n")
print("      -    EN  "+str(count_medium_severity_cvssV2_sh_8_impact)+" VULNERABILIDADES DONDE LA SEVERIDAD ES MEDIA, LA PUNTUACION DE IMPACTO ESTÁ ENTRE 8 Y 9  \n")
print("      -    EN  "+str(count_medium_severity_cvssV2_sh_7_impact)+" VULNERABILIDADES DONDE LA SEVERIDAD ES MEDIA, LA PUNTUACION DE IMPACTO ESTÁ ENTRE 7 Y 8  \n")
print("      -    EN  "+str(count_medium_severity_cvssV2_sh_6_impact)+" VULNERABILIDADES DONDE LA SEVERIDAD ES MEDIA, LA PUNTUACION DE IMPACTO ESTÁ ENTRE 6 Y 7  \n")
print("      -    EN  "+str(count_medium_severity_cvssV2_sh_5_impact)+" VULNERABILIDADES DONDE LA SEVERIDAD ES MEDIA, LA PUNTUACION DE IMPACTO ESTÁ ENTRE 5 Y 6  \n")
print("      -    EN  "+str(count_medium_severity_cvssV2_sh_4_impact)+" VULNERABILIDADES DONDE LA SEVERIDAD ES MEDIA, LA PUNTUACION DE IMPACTO ESTÁ ENTRE 4 Y 5  \n")
print("      -    EN  "+str(count_medium_severity_cvssV2_sh_3_impact)+" VULNERABILIDADES DONDE LA SEVERIDAD ES MEDIA, LA PUNTUACION DE IMPACTO ESTÁ ENTRE 3 Y 4 \ n")
print("      -    EN  "+str(count_medium_severity_cvssV2_sh_2_impact)+" VULNERABILIDADES DONDE LA SEVERIDAD ES MEDIA, LA PUNTUACION DE IMPACTO ESTÁ ENTRE 2 Y 3  \n")
print("      -    EN  "+str(count_medium_severity_cvssV2_sh_1_impact)+" VULNERABILIDADES DONDE LA SEVERIDAD ES MEDIA, LA PUNTUACION DE IMPACTO ESTÁ ENTRE 1 Y 2  \n")
print("      -    EN  "+str(count_medium_severity_cvssV2_sh_0_impact)+" VULNERABILIDADES DONDE LA SEVERIDAD ES MEDIA, LA PUNTUACION DE IMPACTO ESTÁ ENTRE 0 Y 1  \n")
print("\n")


print("**************************PORCENTAJE SEVERIDAD BASE EN CVE CVSSV2 SMART HOME********************************")
print("\n")
print("\n")
print(" DE UN TOTAL DE "+str(counter_high_severity_cvssV2_sh+counter_low_severity_cvssV2_sh+counter_medium_severity_cvssV2_sh)+" VULNERABILIDADES DONDE LA SEVERIDAD ESTÁ DEFINIDA, LOS PORCENTAJES DE PUNTUACION DE IMPACTO Y IMPACTO SON LOS SIGUIENTES :")
print("\n")
print("  - EN  EL "+str(float(((counter_high_severity_cvssV2_sh*100)/len(df_cve_sh["CVE_Items.impact.baseMetricV2.severity"]))))+" % DE LAS VULNERABILIDADES DONDE LA SEVERIDAD ES ALTA, LOS PORCENTAJES DE PUNTUACION DE IMPACTO SON LOS SIGUIENTES:  \n")
print("\n")
print("      -    EN  EL "+str(float(((count_high_severity_cvssV2_sh_10_impact*100)/counter_high_severity_cvssV2_sh_impact)))+" % DE VULNERABILIDADES CON SEVERIDAD ALTA, LA PUNTUACION DE IMPACTO ES 10  \n")
print("      -    EN  EL "+str(float(((count_high_severity_cvssV2_sh_9_impact*100)/counter_high_severity_cvssV2_sh_impact)))+" % DE VULNERABILIDADES CON SEVERIDAD ALTA, LA PUNTUACION DE IMPACTO ESTA ENTRE 9 Y 10  \n")
print("      -    EN  EL "+str(float(((count_high_severity_cvssV2_sh_8_impact*100)/counter_high_severity_cvssV2_sh_impact)))+" % DE VULNERABILIDADES CON SEVERIDAD ALTA, LA PUNTUACION DE IMPACTO ESTA ENTRE 8 Y 9  \n")
print("      -    EN  EL "+str(float(((count_high_severity_cvssV2_sh_7_impact*100)/counter_high_severity_cvssV2_sh_impact)))+" % DE VULNERABILIDADES CON SEVERIDAD ALTA, LA PUNTUACION DE IMPACTO ESTA ENTRE 7 Y 8  \n")
print("      -    EN  EL "+str(float(((count_high_severity_cvssV2_sh_6_impact*100)/counter_high_severity_cvssV2_sh_impact)))+" % DE VULNERABILIDADES CON SEVERIDAD ALTA, LA PUNTUACION DE IMPACTO ESTA ENTRE 6 Y 7  \n")
print("      -    EN  EL "+str(float(((count_high_severity_cvssV2_sh_5_impact*100)/counter_high_severity_cvssV2_sh_impact)))+" % DE VULNERABILIDADES CON SEVERIDAD ALTA, LA PUNTUACION DE IMPACTO ESTA ENTRE 5 Y 6  \n")
print("      -    EN  EL "+str(float(((count_high_severity_cvssV2_sh_4_impact*100)/counter_high_severity_cvssV2_sh_impact)))+" % DE VULNERABILIDADES CON SEVERIDAD ALTA, LA PUNTUACION DE IMPACTO ESTA ENTRE 4 Y 5  \n")
print("      -    EN  EL "+str(float(((count_high_severity_cvssV2_sh_3_impact*100)/counter_high_severity_cvssV2_sh_impact)))+" % DE VULNERABILIDADES CON SEVERIDAD ALTA, LA PUNTUACION DE IMPACTO ESTA ENTRE 3 Y 4  \n")
print("      -    EN  EL "+str(float(((count_high_severity_cvssV2_sh_2_impact*100)/counter_high_severity_cvssV2_sh_impact)))+" % DE VULNERABILIDADES CON SEVERIDAD ALTA, LA PUNTUACION DE IMPACTO ESTA ENTRE 2 Y 3  \n")
print("      -    EN  EL "+str(float(((count_high_severity_cvssV2_sh_1_impact*100)/counter_high_severity_cvssV2_sh_impact)))+" % DE VULNERABILIDADES CON SEVERIDAD ALTA, LA PUNTUACION DE IMPACTO ESTA ENTRE 1 Y 2  \n") 
print("      -    EN  EL "+str(float(((count_high_severity_cvssV2_sh_0_impact*100)/counter_high_severity_cvssV2_sh_impact)))+" % DE VULNERABILIDADES CON SEVERIDAD ALTA, LA PUNTUACION DE IMPACTO ESTA ENTRE 0 Y 1 \n")      
print("      -    LA PUNTUACION MEDIA DE IMPACTO EN LAS VULNERABILIDADES CON SEVERIDAD ALTA ES : "+str(float((count_high_severity_cvssV2_sh_impact/counter_high_severity_cvssV2_sh_impact)))+"\n")      

print("  - EN  EL "+str(float(((counter_low_severity_cvssV2_sh*100)/len(df_cve_sh["CVE_Items.impact.baseMetricV2.severity"]))))+" % DE LAS VULNERABILIDADES DONDE LA SEVERIDAD ES BAJA, LOS PORCENTAJES DE PUNTUACION DE IMPACTO SON LOS SIGUIENTES:  \n")
print("\n")
print("      -    EN  EL "+str(float(((count_low_severity_cvssV2_sh_10_impact*100)/counter_low_severity_cvssV2_sh_impact)))+" % DE VULNERABILIDADES CON SEVERIDAD BAJA, LA PUNTUACION DE IMPACTO ES 10  \n")
print("      -    EN  EL "+str(float(((count_low_severity_cvssV2_sh_9_impact*100)/counter_low_severity_cvssV2_sh_impact)))+" % DE VULNERABILIDADES CON SEVERIDAD BAJA, LA PUNTUACION DE IMPACTO ESTA ENTRE 9 Y 10  \n")
print("      -    EN  EL "+str(float(((count_low_severity_cvssV2_sh_8_impact*100)/counter_low_severity_cvssV2_sh_impact)))+" % DE VULNERABILIDADES CON SEVERIDAD BAJA, LA PUNTUACION DE IMPACTO ESTA ENTRE 8 Y 9  \n")
print("      -    EN  EL "+str(float(((count_low_severity_cvssV2_sh_7_impact*100)/counter_low_severity_cvssV2_sh_impact)))+" % DE VULNERABILIDADES CON SEVERIDAD BAJA, LA PUNTUACION DE IMPACTO ESTA ENTRE 7 Y 8  \n")
print("      -    EN  EL "+str(float(((count_low_severity_cvssV2_sh_6_impact*100)/counter_low_severity_cvssV2_sh_impact)))+" % DE VULNERABILIDADES CON SEVERIDAD BAJA, LA PUNTUACION DE IMPACTO ESTA ENTRE 6 Y 7  \n")
print("      -    EN  EL "+str(float(((count_low_severity_cvssV2_sh_5_impact*100)/counter_low_severity_cvssV2_sh_impact)))+" % DE VULNERABILIDADES CON SEVERIDAD BAJA, LA PUNTUACION DE IMPACTO ESTA ENTRE 5 Y 6  \n")
print("      -    EN  EL "+str(float(((count_low_severity_cvssV2_sh_4_impact*100)/counter_low_severity_cvssV2_sh_impact)))+" % DE VULNERABILIDADES CON SEVERIDAD BAJA, LA PUNTUACION DE IMPACTO ESTA ENTRE 4 Y 5  \n")
print("      -    EN  EL "+str(float(((count_low_severity_cvssV2_sh_3_impact*100)/counter_low_severity_cvssV2_sh_impact)))+" % DE VULNERABILIDADES CON SEVERIDAD BAJA, LA PUNTUACION DE IMPACTO ESTA ENTRE 3 Y 4  \n")
print("      -    EN  EL "+str(float(((count_low_severity_cvssV2_sh_2_impact*100)/counter_low_severity_cvssV2_sh_impact)))+" % DE VULNERABILIDADES CON SEVERIDAD BAJA, LA PUNTUACION DE IMPACTO ESTA ENTRE 2 Y 3  \n")
print("      -    EN  EL "+str(float(((count_low_severity_cvssV2_sh_1_impact*100)/counter_low_severity_cvssV2_sh_impact)))+" % DE VULNERABILIDADES CON SEVERIDAD BAJA, LA PUNTUACION DE IMPACTO ESTA ENTRE 1 Y 2  \n") 
print("      -    EN  EL "+str(float(((count_low_severity_cvssV2_sh_0_impact*100)/counter_low_severity_cvssV2_sh_impact)))+" % DE VULNERABILIDADES CON SEVERIDAD BAJA, LA PUNTUACION DE IMPACTO ESTA ENTRE 0 Y 1 \n")      
print("      -    LA PUNTUACION MEDIA DE IMPACTO EN LAS VULNERABILIDADES CON SEVERIDAD BAJA ES : "+str(float((count_low_severity_cvssV2_sh_impact/counter_low_severity_cvssV2_sh_impact)))+"\n")      
print("\n")

print("  - EN  EL "+str(float(((counter_medium_severity_cvssV2_sh*100)/len(df_cve_sh["CVE_Items.impact.baseMetricV2.severity"]))))+" % DE LAS VULNERABILIDADES DONDE LA SEVERIDAD ES MEDIA, LOS PORCENTAJES DE PUNTUACION DE IMPACTO SON LOS SIGUIENTES:  \n")
print("\n")
print("      -    EN  EL "+str(float(((count_medium_severity_cvssV2_sh_10_impact*100)/counter_medium_severity_cvssV2_sh_impact)))+" % DE VULNERABILIDADES CON SEVERIDAD MEDIA, LA PUNTUACION DE IMPACTO ES 10  \n")
print("      -    EN  EL "+str(float(((count_medium_severity_cvssV2_sh_9_impact*100)/counter_medium_severity_cvssV2_sh_impact)))+" % DE VULNERABILIDADES CON SEVERIDAD MEDIA, LA PUNTUACION DE IMPACTO ESTA ENTRE 9 Y 10  \n")
print("      -    EN  EL "+str(float(((count_medium_severity_cvssV2_sh_8_impact*100)/counter_medium_severity_cvssV2_sh_impact)))+" % DE VULNERABILIDADES CON SEVERIDAD MEDIA, LA PUNTUACION DE IMPACTO ESTA ENTRE 8 Y 9  \n")
print("      -    EN  EL "+str(float(((count_medium_severity_cvssV2_sh_7_impact*100)/counter_medium_severity_cvssV2_sh_impact)))+" % DE VULNERABILIDADES CON SEVERIDAD MEDIA, LA PUNTUACION DE IMPACTO ESTA ENTRE 7 Y 8  \n")
print("      -    EN  EL "+str(float(((count_medium_severity_cvssV2_sh_6_impact*100)/counter_medium_severity_cvssV2_sh_impact)))+" % DE VULNERABILIDADES CON SEVERIDAD MEDIA, LA PUNTUACION DE IMPACTO ESTA ENTRE 6 Y 7  \n")
print("      -    EN  EL "+str(float(((count_medium_severity_cvssV2_sh_5_impact*100)/counter_medium_severity_cvssV2_sh_impact)))+" % DE VULNERABILIDADES CON SEVERIDAD MEDIA, LA PUNTUACION DE IMPACTO ESTA ENTRE 5 Y 6  \n")
print("      -    EN  EL "+str(float(((count_medium_severity_cvssV2_sh_4_impact*100)/counter_medium_severity_cvssV2_sh_impact)))+" % DE VULNERABILIDADES CON SEVERIDAD MEDIA, LA PUNTUACION DE IMPACTO ESTA ENTRE 4 Y 5  \n")
print("      -    EN  EL "+str(float(((count_medium_severity_cvssV2_sh_3_impact*100)/counter_medium_severity_cvssV2_sh_impact)))+" % DE VULNERABILIDADES CON SEVERIDAD MEDIA, LA PUNTUACION DE IMPACTO ESTA ENTRE 3 Y 4  \n")
print("      -    EN  EL "+str(float(((count_medium_severity_cvssV2_sh_2_impact*100)/counter_medium_severity_cvssV2_sh_impact)))+" % DE VULNERABILIDADES CON SEVERIDAD MEDIA, LA PUNTUACION DE IMPACTO ESTA ENTRE 2 Y 3  \n")
print("      -    EN  EL "+str(float(((count_medium_severity_cvssV2_sh_1_impact*100)/counter_medium_severity_cvssV2_sh_impact)))+" % DE VULNERABILIDADES CON SEVERIDAD MEDIA, LA PUNTUACION DE IMPACTO ESTA ENTRE 1 Y 2  \n") 
print("      -    EN  EL "+str(float(((count_medium_severity_cvssV2_sh_0_impact*100)/counter_medium_severity_cvssV2_sh_impact)))+" % DE VULNERABILIDADES CON SEVERIDAD MEDIA, LA PUNTUACION DE IMPACTO ESTA ENTRE 0 Y 1 \n")      
print("      -    LA PUNTUACION MEDIA DE IMPACTO EN LAS VULNERABILIDADES CON SEVERIDAD MEDIA ES : "+str(float((count_medium_severity_cvssV2_sh_impact/counter_medium_severity_cvssV2_sh_impact)))+"\n")      
print("\n")



print("************************** ESTADÍSTICAS SEVERIDAD BASE EN CVE CVSSV2 PARTE IOT Y SMART HOME CONJUNTAS ********************************")
print("\n")
print("\n")
print(" DE UN TOTAL DE "+str(counter_high_severity_cvssV2_sh+counter_low_severity_cvssV2_sh+counter_medium_severity_cvssV2_sh+counter_high_severity_cvssV2_iot+counter_low_severity_cvssV2_iot+counter_medium_severity_cvssV2_iot)+" VULNERABILIDADES DONDE LA SEVERIDAD ESTÁ DEFINIDA, LAS ESTADÍSTICAS DE PUNTUACION DE IMPACTO Y IMPACTO SON LAS SIGUIENTES :")
print("\n")
print("  - EN  "+str(counter_high_severity_cvssV2_sh+counter_high_severity_cvssV2_iot)+" VULNERABILIDADES DONDE LA SEVERIDAD ES ALTA, LAS ESTADISTICAS DE PUNTUACION DE IMPACTO SON LAS SIGUIENTES:  \n")
print("\n")
print("      -    EN  "+str(count_high_severity_cvssV2_sh_10_impact+count_high_severity_cvssV2_iot_10_impact)+" VULNERABILIDADES DONDE LA SEVERIDAD ES ALTA, LA PUNTUACION DE IMPACTO ES 10  \n")
print("      -    EN  "+str(count_high_severity_cvssV2_sh_9_impact+count_high_severity_cvssV2_iot_9_impact)+" VULNERABILIDADES DONDE LA SEVERIDAD ES ALTA, LA PUNTUACION DE IMPACTO ESTÁ ENTRE 9 Y 10  \n")
print("      -    EN  "+str(count_high_severity_cvssV2_sh_8_impact+count_high_severity_cvssV2_iot_8_impact)+" VULNERABILIDADES DONDE LA SEVERIDAD ES ALTA, LA PUNTUACION DE IMPACTO ESTÁ ENTRE 8 Y 9  \n")
print("      -    EN  "+str(count_high_severity_cvssV2_sh_7_impact+count_high_severity_cvssV2_iot_7_impact)+" VULNERABILIDADES DONDE LA SEVERIDAD ES ALTA, LA PUNTUACION DE IMPACTO ESTÁ ENTRE 7 Y 8  \n")
print("      -    EN  "+str(count_high_severity_cvssV2_sh_6_impact+count_high_severity_cvssV2_iot_6_impact)+" VULNERABILIDADES DONDE LA SEVERIDAD ES ALTA, LA PUNTUACION DE IMPACTO ESTÁ ENTRE 6 Y 7  \n")
print("      -    EN  "+str(count_high_severity_cvssV2_sh_5_impact+count_high_severity_cvssV2_iot_5_impact)+" VULNERABILIDADES DONDE LA SEVERIDAD ES ALTA, LA PUNTUACION DE IMPACTO ESTÁ ENTRE 5 Y 6  \n")
print("      -    EN  "+str(count_high_severity_cvssV2_sh_4_impact+count_high_severity_cvssV2_iot_4_impact)+" VULNERABILIDADES DONDE LA SEVERIDAD ES ALTA, LA PUNTUACION DE IMPACTO ESTÁ ENTRE 4 Y 5  \n")
print("      -    EN  "+str(count_high_severity_cvssV2_sh_3_impact+count_high_severity_cvssV2_iot_3_impact)+" VULNERABILIDADES DONDE LA SEVERIDAD ES ALTA, LA PUNTUACION DE IMPACTO ESTÁ ENTRE 3 Y 4  \n")
print("      -    EN  "+str(count_high_severity_cvssV2_sh_2_impact+count_high_severity_cvssV2_iot_2_impact)+" VULNERABILIDADES DONDE LA SEVERIDAD ES ALTA, LA PUNTUACION DE IMPACTO ESTÁ ENTRE 2 Y 3  \n")
print("      -    EN  "+str(count_high_severity_cvssV2_sh_1_impact+count_high_severity_cvssV2_iot_1_impact)+" VULNERABILIDADES DONDE LA SEVERIDAD ES ALTA, LA PUNTUACION DE IMPACTO ESTÁ ENTRE 1 Y 2  \n")
print("      -    EN  "+str(count_high_severity_cvssV2_sh_0_impact+count_high_severity_cvssV2_iot_0_impact)+" VULNERABILIDADES DONDE LA SEVERIDAD ES ALTA, LA PUNTUACION DE IMPACTO ESTÁ ENTRE 0 Y 1  \n")
print("\n")

print("  - EN  "+str(counter_low_severity_cvssV2_sh+counter_low_severity_cvssV2_iot)+" VULNERABILIDADES DONDE LA SEVERIDAD ES BAJA, LAS ESTADISTICAS DE PUNTUACION DE IMPACTO SON LAS SIGUIENTES:  \n")
print("\n")
print("      -    EN  "+str(count_low_severity_cvssV2_sh_10_impact+count_low_severity_cvssV2_iot_10_impact)+" VULNERABILIDADES DONDE LA SEVERIDAD ES BAJA, LA PUNTUACION DE IMPACTO ES 10  \n")
print("      -    EN  "+str(count_low_severity_cvssV2_sh_9_impact+count_low_severity_cvssV2_iot_9_impact)+" VULNERABILIDADES DONDE LA SEVERIDAD ES BAJA, LA PUNTUACION DE IMPACTO ESTÁ ENTRE 9 Y 10  \n")
print("      -    EN  "+str(count_low_severity_cvssV2_sh_8_impact+count_low_severity_cvssV2_iot_8_impact)+" VULNERABILIDADES DONDE LA SEVERIDAD ES BAJA, LA PUNTUACION DE IMPACTO ESTÁ ENTRE 8 Y 9  \n")
print("      -    EN  "+str(count_low_severity_cvssV2_sh_7_impact+count_low_severity_cvssV2_iot_7_impact)+" VULNERABILIDADES DONDE LA SEVERIDAD ES BAJA, LA PUNTUACION DE IMPACTO ESTÁ ENTRE 7 Y 8  \n")
print("      -    EN  "+str(count_low_severity_cvssV2_sh_6_impact+count_low_severity_cvssV2_iot_6_impact)+" VULNERABILIDADES DONDE LA SEVERIDAD ES BAJA, LA PUNTUACION DE IMPACTO ESTÁ ENTRE 6 Y 7  \n")
print("      -    EN  "+str(count_low_severity_cvssV2_sh_5_impact+count_low_severity_cvssV2_iot_5_impact)+" VULNERABILIDADES DONDE LA SEVERIDAD ES BAJA, LA PUNTUACION DE IMPACTO ESTÁ ENTRE 5 Y 6  \n")
print("      -    EN  "+str(count_low_severity_cvssV2_sh_4_impact+count_low_severity_cvssV2_iot_4_impact)+" VULNERABILIDADES DONDE LA SEVERIDAD ES BAJA, LA PUNTUACION DE IMPACTO ESTÁ ENTRE 4 Y 5  \n")
print("      -    EN  "+str(count_low_severity_cvssV2_sh_3_impact+count_low_severity_cvssV2_iot_3_impact)+" VULNERABILIDADES DONDE LA SEVERIDAD ES BAJA, LA PUNTUACION DE IMPACTO ESTÁ ENTRE 3 Y 4 \ n")
print("      -    EN  "+str(count_low_severity_cvssV2_sh_2_impact+count_low_severity_cvssV2_iot_2_impact)+" VULNERABILIDADES DONDE LA SEVERIDAD ES BAJA, LA PUNTUACION DE IMPACTO ESTÁ ENTRE 2 Y 3  \n")
print("      -    EN  "+str(count_low_severity_cvssV2_sh_1_impact+count_low_severity_cvssV2_iot_1_impact)+" VULNERABILIDADES DONDE LA SEVERIDAD ES BAJA, LA PUNTUACION DE IMPACTO ESTÁ ENTRE 1 Y 2  \n")
print("      -    EN  "+str(count_low_severity_cvssV2_sh_0_impact+count_low_severity_cvssV2_iot_0_impact)+" VULNERABILIDADES DONDE LA SEVERIDAD ES BAJA, LA PUNTUACION DE IMPACTO ESTÁ ENTRE 0 Y 1  \n")
print("\n")

print("  - EN  "+str(counter_medium_severity_cvssV2_sh+counter_medium_severity_cvssV2_iot)+" VULNERABILIDADES DONDE LA SEVERIDAD ES MEDIA, LAS ESTADISTICAS DE PUNTUACION DE IMPACTO SON LAS SIGUIENTES:  \n")
print("\n")
print("      -    EN  "+str(count_medium_severity_cvssV2_sh_10_impact+count_medium_severity_cvssV2_iot_10_impact)+" VULNERABILIDADES DONDE LA SEVERIDAD ES MEDIA, LA PUNTUACION DE IMPACTO ES 10  \n")
print("      -    EN  "+str(count_medium_severity_cvssV2_sh_9_impact+count_medium_severity_cvssV2_iot_9_impact)+" VULNERABILIDADES DONDE LA SEVERIDAD ES MEDIA, LA PUNTUACION DE IMPACTO ESTÁ ENTRE 9 Y 10  \n")
print("      -    EN  "+str(count_medium_severity_cvssV2_sh_8_impact+count_medium_severity_cvssV2_iot_8_impact)+" VULNERABILIDADES DONDE LA SEVERIDAD ES MEDIA, LA PUNTUACION DE IMPACTO ESTÁ ENTRE 8 Y 9  \n")
print("      -    EN  "+str(count_medium_severity_cvssV2_sh_7_impact+count_medium_severity_cvssV2_iot_7_impact)+" VULNERABILIDADES DONDE LA SEVERIDAD ES MEDIA, LA PUNTUACION DE IMPACTO ESTÁ ENTRE 7 Y 8  \n")
print("      -    EN  "+str(count_medium_severity_cvssV2_sh_6_impact+count_medium_severity_cvssV2_iot_6_impact)+" VULNERABILIDADES DONDE LA SEVERIDAD ES MEDIA, LA PUNTUACION DE IMPACTO ESTÁ ENTRE 6 Y 7  \n")
print("      -    EN  "+str(count_medium_severity_cvssV2_sh_5_impact+count_medium_severity_cvssV2_iot_5_impact)+" VULNERABILIDADES DONDE LA SEVERIDAD ES MEDIA, LA PUNTUACION DE IMPACTO ESTÁ ENTRE 5 Y 6  \n")
print("      -    EN  "+str(count_medium_severity_cvssV2_sh_4_impact+count_medium_severity_cvssV2_iot_4_impact)+" VULNERABILIDADES DONDE LA SEVERIDAD ES MEDIA, LA PUNTUACION DE IMPACTO ESTÁ ENTRE 4 Y 5  \n")
print("      -    EN  "+str(count_medium_severity_cvssV2_sh_3_impact+count_medium_severity_cvssV2_iot_3_impact)+" VULNERABILIDADES DONDE LA SEVERIDAD ES MEDIA, LA PUNTUACION DE IMPACTO ESTÁ ENTRE 3 Y 4 \ n")
print("      -    EN  "+str(count_medium_severity_cvssV2_sh_2_impact+count_medium_severity_cvssV2_iot_2_impact)+" VULNERABILIDADES DONDE LA SEVERIDAD ES MEDIA, LA PUNTUACION DE IMPACTO ESTÁ ENTRE 2 Y 3  \n")
print("      -    EN  "+str(count_medium_severity_cvssV2_sh_1_impact+count_medium_severity_cvssV2_iot_1_impact)+" VULNERABILIDADES DONDE LA SEVERIDAD ES MEDIA, LA PUNTUACION DE IMPACTO ESTÁ ENTRE 1 Y 2  \n")
print("      -    EN  "+str(count_medium_severity_cvssV2_sh_0_impact+count_medium_severity_cvssV2_iot_0_impact)+" VULNERABILIDADES DONDE LA SEVERIDAD ES MEDIA, LA PUNTUACION DE IMPACTO ESTÁ ENTRE 0 Y 1  \n")
print("\n")

print("**************************PORCENTAJE SEVERIDAD BASE EN CVE CVSSV2 PARTE IOT Y SMART HOME CONJUNTAS********************************")
print("\n")
print("\n")
print(" DE UN TOTAL DE "+str(counter_high_severity_cvssV2_sh+counter_low_severity_cvssV2_sh+counter_medium_severity_cvssV2_sh+counter_high_severity_cvssV2_iot+counter_low_severity_cvssV2_iot+counter_medium_severity_cvssV2_iot)+" VULNERABILIDADES DONDE LA SEVERIDAD ESTÁ DEFINIDA, LOS PORCENTAJES DE PUNTUACION DE IMPACTO Y IMPACTO SON LOS SIGUIENTES :")
print("\n")
print("EN EL "+str(float((((counter_high_severity_cvssV2_sh+counter_high_severity_cvssV2_iot)*100)/(len(df_cve_sh["CVE_Items.impact.baseMetricV2.severity"])+len(df_cve_iot["CVE_Items.impact.baseMetricV2.severity"])))))+"% DE LAS VULNERABILIDADES DONDE LA SEVERIDAD ES ALTA, LOS PORCENTAJES DE PUNTUACION DE IMPACTO SON LOS SIGUIENTES: \n")
print("\n")
print("      -    EN  EL "+str(float((((count_high_severity_cvssV2_sh_10_impact+count_high_severity_cvssV2_iot_10_impact)*100)/(counter_high_severity_cvssV2_sh_impact+counter_high_severity_cvssV2_iot_impact))))+" % DE VULNERABILIDADES CON SEVERIDAD ALTA, LA PUNTUACION DE IMPACTO ES 10  \n")
print("      -    EN  EL "+str(float((((count_high_severity_cvssV2_sh_9_impact+count_high_severity_cvssV2_iot_9_impact)*100)/(counter_high_severity_cvssV2_sh_impact+counter_high_severity_cvssV2_iot_impact))))+" % DE VULNERABILIDADES CON SEVERIDAD ALTA, LA PUNTUACION DE IMPACTO ESTA ENTRE 9 Y 10  \n")
print("      -    EN  EL "+str(float((((count_high_severity_cvssV2_sh_8_impact+count_high_severity_cvssV2_iot_8_impact)*100)/(counter_high_severity_cvssV2_sh_impact+counter_high_severity_cvssV2_iot_impact))))+" % DE VULNERABILIDADES CON SEVERIDAD ALTA, LA PUNTUACION DE IMPACTO ESTA ENTRE 8 Y 9  \n")
print("      -    EN  EL "+str(float((((count_high_severity_cvssV2_sh_7_impact+count_high_severity_cvssV2_iot_7_impact)*100)/(counter_high_severity_cvssV2_sh_impact+counter_high_severity_cvssV2_iot_impact))))+" % DE VULNERABILIDADES CON SEVERIDAD ALTA, LA PUNTUACION DE IMPACTO ESTA ENTRE 7 Y 8  \n")
print("      -    EN  EL "+str(float((((count_high_severity_cvssV2_sh_6_impact+count_high_severity_cvssV2_iot_6_impact)*100)/(counter_high_severity_cvssV2_sh_impact+counter_high_severity_cvssV2_iot_impact))))+" % DE VULNERABILIDADES CON SEVERIDAD ALTA, LA PUNTUACION DE IMPACTO ESTA ENTRE 6 Y 7  \n")
print("      -    EN  EL "+str(float((((count_high_severity_cvssV2_sh_5_impact+count_high_severity_cvssV2_iot_5_impact)*100)/(counter_high_severity_cvssV2_sh_impact+counter_high_severity_cvssV2_iot_impact))))+" % DE VULNERABILIDADES CON SEVERIDAD ALTA, LA PUNTUACION DE IMPACTO ESTA ENTRE 5 Y 6  \n")
print("      -    EN  EL "+str(float((((count_high_severity_cvssV2_sh_4_impact+count_high_severity_cvssV2_iot_4_impact)*100)/(counter_high_severity_cvssV2_sh_impact+counter_high_severity_cvssV2_iot_impact))))+" % DE VULNERABILIDADES CON SEVERIDAD ALTA, LA PUNTUACION DE IMPACTO ESTA ENTRE 4 Y 5  \n")
print("      -    EN  EL "+str(float((((count_high_severity_cvssV2_sh_3_impact+count_high_severity_cvssV2_iot_3_impact)*100)/(counter_high_severity_cvssV2_sh_impact+counter_high_severity_cvssV2_iot_impact))))+" % DE VULNERABILIDADES CON SEVERIDAD ALTA, LA PUNTUACION DE IMPACTO ESTA ENTRE 3 Y 4  \n")
print("      -    EN  EL "+str(float((((count_high_severity_cvssV2_sh_2_impact+count_high_severity_cvssV2_iot_2_impact)*100)/(counter_high_severity_cvssV2_sh_impact+counter_high_severity_cvssV2_iot_impact))))+" % DE VULNERABILIDADES CON SEVERIDAD ALTA, LA PUNTUACION DE IMPACTO ESTA ENTRE 2 Y 3  \n")
print("      -    EN  EL "+str(float((((count_high_severity_cvssV2_sh_1_impact+count_high_severity_cvssV2_iot_1_impact)*100)/(counter_high_severity_cvssV2_sh_impact+counter_high_severity_cvssV2_iot_impact))))+" % DE VULNERABILIDADES CON SEVERIDAD ALTA, LA PUNTUACION DE IMPACTO ESTA ENTRE 1 Y 2  \n") 
print("      -    EN  EL "+str(float((((count_high_severity_cvssV2_sh_0_impact+count_high_severity_cvssV2_iot_0_impact)*100)/(counter_high_severity_cvssV2_sh_impact+counter_high_severity_cvssV2_iot_impact))))+" % DE VULNERABILIDADES CON SEVERIDAD ALTA, LA PUNTUACION DE IMPACTO ESTA ENTRE 0 Y 1 \n")      
print("      -    LA PUNTUACION MEDIA DE IMPACTO EN LAS VULNERABILIDADES CON SEVERIDAD ALTA ES : "+str(float(((count_high_severity_cvssV2_sh_impact+count_high_severity_cvssV2_iot_impact)/(counter_high_severity_cvssV2_sh_impact+counter_high_severity_cvssV2_iot_impact))))+"\n")      
print("\n")
print("\n")
print("EN EL "+str(float((((counter_low_severity_cvssV2_sh+counter_low_severity_cvssV2_iot)*100)/(len(df_cve_sh["CVE_Items.impact.baseMetricV2.severity"])+len(df_cve_iot["CVE_Items.impact.baseMetricV2.severity"])))))+"% DE LAS VULNERABILIDADES DONDE LA SEVERIDAD ES BAJA, LOS PORCENTAJES DE PUNTUACION DE IMPACTO SON LOS SIGUIENTES: \n")
print("\n")
print("      -    EN  EL "+str(float((((count_low_severity_cvssV2_sh_10_impact+count_low_severity_cvssV2_iot_10_impact)*100)/(counter_low_severity_cvssV2_sh_impact+counter_low_severity_cvssV2_iot_impact))))+" % DE VULNERABILIDADES CON SEVERIDAD BAJA, LA PUNTUACION DE IMPACTO ES 10  \n")
print("      -    EN  EL "+str(float((((count_low_severity_cvssV2_sh_9_impact+count_low_severity_cvssV2_iot_9_impact)*100)/(counter_low_severity_cvssV2_sh_impact+counter_low_severity_cvssV2_iot_impact))))+" % DE VULNERABILIDADES CON SEVERIDAD BAJA, LA PUNTUACION DE IMPACTO ESTA ENTRE 9 Y 10  \n")
print("      -    EN  EL "+str(float((((count_low_severity_cvssV2_sh_8_impact+count_low_severity_cvssV2_iot_8_impact)*100)/(counter_low_severity_cvssV2_sh_impact+counter_low_severity_cvssV2_iot_impact))))+" % DE VULNERABILIDADES CON SEVERIDAD BAJA, LA PUNTUACION DE IMPACTO ESTA ENTRE 8 Y 9  \n")
print("      -    EN  EL "+str(float((((count_low_severity_cvssV2_sh_7_impact+count_low_severity_cvssV2_iot_7_impact)*100)/(counter_low_severity_cvssV2_sh_impact+counter_low_severity_cvssV2_iot_impact))))+" % DE VULNERABILIDADES CON SEVERIDAD BAJA, LA PUNTUACION DE IMPACTO ESTA ENTRE 7 Y 8  \n")
print("      -    EN  EL "+str(float((((count_low_severity_cvssV2_sh_6_impact+count_low_severity_cvssV2_iot_6_impact)*100)/(counter_low_severity_cvssV2_sh_impact+counter_low_severity_cvssV2_iot_impact))))+" % DE VULNERABILIDADES CON SEVERIDAD BAJA, LA PUNTUACION DE IMPACTO ESTA ENTRE 6 Y 7  \n")
print("      -    EN  EL "+str(float((((count_low_severity_cvssV2_sh_5_impact+count_low_severity_cvssV2_iot_5_impact)*100)/(counter_low_severity_cvssV2_sh_impact+counter_low_severity_cvssV2_iot_impact))))+" % DE VULNERABILIDADES CON SEVERIDAD BAJA, LA PUNTUACION DE IMPACTO ESTA ENTRE 5 Y 6  \n")
print("      -    EN  EL "+str(float((((count_low_severity_cvssV2_sh_4_impact+count_low_severity_cvssV2_iot_4_impact)*100)/(counter_low_severity_cvssV2_sh_impact+counter_low_severity_cvssV2_iot_impact))))+" % DE VULNERABILIDADES CON SEVERIDAD BAJA, LA PUNTUACION DE IMPACTO ESTA ENTRE 4 Y 5  \n")
print("      -    EN  EL "+str(float((((count_low_severity_cvssV2_sh_3_impact+count_low_severity_cvssV2_iot_3_impact)*100)/(counter_low_severity_cvssV2_sh_impact+counter_low_severity_cvssV2_iot_impact))))+" % DE VULNERABILIDADES CON SEVERIDAD BAJA, LA PUNTUACION DE IMPACTO ESTA ENTRE 3 Y 4  \n")
print("      -    EN  EL "+str(float((((count_low_severity_cvssV2_sh_2_impact+count_low_severity_cvssV2_iot_2_impact)*100)/(counter_low_severity_cvssV2_sh_impact+counter_low_severity_cvssV2_iot_impact))))+" % DE VULNERABILIDADES CON SEVERIDAD BAJA, LA PUNTUACION DE IMPACTO ESTA ENTRE 2 Y 3  \n")
print("      -    EN  EL "+str(float((((count_low_severity_cvssV2_sh_1_impact+count_low_severity_cvssV2_iot_1_impact)*100)/(counter_low_severity_cvssV2_sh_impact+counter_low_severity_cvssV2_iot_impact))))+" % DE VULNERABILIDADES CON SEVERIDAD BAJA, LA PUNTUACION DE IMPACTO ESTA ENTRE 1 Y 2  \n") 
print("      -    EN  EL "+str(float((((count_low_severity_cvssV2_sh_0_impact+count_low_severity_cvssV2_iot_0_impact)*100)/(counter_low_severity_cvssV2_sh_impact+counter_low_severity_cvssV2_iot_impact))))+" % DE VULNERABILIDADES CON SEVERIDAD BAJA, LA PUNTUACION DE IMPACTO ESTA ENTRE 0 Y 1 \n")      
print("      -    LA PUNTUACION MEDIA DE IMPACTO EN LAS VULNERABILIDADES CON SEVERIDAD BAJA ES : "+str(float(((count_low_severity_cvssV2_sh_impact+count_low_severity_cvssV2_iot_impact)/(counter_low_severity_cvssV2_sh_impact+counter_low_severity_cvssV2_iot_impact))))+"\n")      
print("\n")
print("EN EL "+str(float((((counter_medium_severity_cvssV2_sh+counter_medium_severity_cvssV2_iot)*100)/(len(df_cve_sh["CVE_Items.impact.baseMetricV2.severity"])+len(df_cve_iot["CVE_Items.impact.baseMetricV2.severity"])))))+"% DE LAS VULNERABILIDADES DONDE LA SEVERIDAD ES MEDIA, LOS PORCENTAJES DE PUNTUACION DE IMPACTO SON LOS SIGUIENTES: \n")
print("\n")
print("      -    EN  EL "+str(float((((count_medium_severity_cvssV2_sh_10_impact+count_medium_severity_cvssV2_iot_10_impact)*100)/(counter_medium_severity_cvssV2_sh_impact+counter_medium_severity_cvssV2_iot_impact))))+" % DE VULNERABILIDADES CON SEVERIDAD MEDIA, LA PUNTUACION DE IMPACTO ES 10  \n")
print("      -    EN  EL "+str(float((((count_medium_severity_cvssV2_sh_9_impact+count_medium_severity_cvssV2_iot_9_impact)*100)/(counter_medium_severity_cvssV2_sh_impact+counter_medium_severity_cvssV2_iot_impact))))+" % DE VULNERABILIDADES CON SEVERIDAD MEDIA, LA PUNTUACION DE IMPACTO ESTA ENTRE 9 Y 10  \n")
print("      -    EN  EL "+str(float((((count_medium_severity_cvssV2_sh_8_impact+count_medium_severity_cvssV2_iot_8_impact)*100)/(counter_medium_severity_cvssV2_sh_impact+counter_medium_severity_cvssV2_iot_impact))))+" % DE VULNERABILIDADES CON SEVERIDAD MEDIA, LA PUNTUACION DE IMPACTO ESTA ENTRE 8 Y 9  \n")
print("      -    EN  EL "+str(float((((count_medium_severity_cvssV2_sh_7_impact+count_medium_severity_cvssV2_iot_7_impact)*100)/(counter_medium_severity_cvssV2_sh_impact+counter_medium_severity_cvssV2_iot_impact))))+" % DE VULNERABILIDADES CON SEVERIDAD MEDIA, LA PUNTUACION DE IMPACTO ESTA ENTRE 7 Y 8  \n")
print("      -    EN  EL "+str(float((((count_medium_severity_cvssV2_sh_6_impact+count_medium_severity_cvssV2_iot_6_impact)*100)/(counter_medium_severity_cvssV2_sh_impact+counter_medium_severity_cvssV2_iot_impact))))+" % DE VULNERABILIDADES CON SEVERIDAD MEDIA, LA PUNTUACION DE IMPACTO ESTA ENTRE 6 Y 7  \n")
print("      -    EN  EL "+str(float((((count_medium_severity_cvssV2_sh_5_impact+count_medium_severity_cvssV2_iot_5_impact)*100)/(counter_medium_severity_cvssV2_sh_impact+counter_medium_severity_cvssV2_iot_impact))))+" % DE VULNERABILIDADES CON SEVERIDAD MEDIA, LA PUNTUACION DE IMPACTO ESTA ENTRE 5 Y 6  \n")
print("      -    EN  EL "+str(float((((count_medium_severity_cvssV2_sh_4_impact+count_medium_severity_cvssV2_iot_4_impact)*100)/(counter_medium_severity_cvssV2_sh_impact+counter_medium_severity_cvssV2_iot_impact))))+" % DE VULNERABILIDADES CON SEVERIDAD MEDIA, LA PUNTUACION DE IMPACTO ESTA ENTRE 4 Y 5  \n")
print("      -    EN  EL "+str(float((((count_medium_severity_cvssV2_sh_3_impact+count_medium_severity_cvssV2_iot_3_impact)*100)/(counter_medium_severity_cvssV2_sh_impact+counter_medium_severity_cvssV2_iot_impact))))+" % DE VULNERABILIDADES CON SEVERIDAD MEDIA, LA PUNTUACION DE IMPACTO ESTA ENTRE 3 Y 4  \n")
print("      -    EN  EL "+str(float((((count_medium_severity_cvssV2_sh_2_impact+count_medium_severity_cvssV2_iot_2_impact)*100)/(counter_medium_severity_cvssV2_sh_impact+counter_medium_severity_cvssV2_iot_impact))))+" % DE VULNERABILIDADES CON SEVERIDAD MEDIA, LA PUNTUACION DE IMPACTO ESTA ENTRE 2 Y 3  \n")
print("      -    EN  EL "+str(float((((count_medium_severity_cvssV2_sh_1_impact+count_medium_severity_cvssV2_iot_1_impact)*100)/(counter_medium_severity_cvssV2_sh_impact+counter_medium_severity_cvssV2_iot_impact))))+" % DE VULNERABILIDADES CON SEVERIDAD MEDIA, LA PUNTUACION DE IMPACTO ESTA ENTRE 1 Y 2  \n") 
print("      -    EN  EL "+str(float((((count_medium_severity_cvssV2_sh_0_impact+count_medium_severity_cvssV2_iot_0_impact)*100)/(counter_medium_severity_cvssV2_sh_impact+counter_medium_severity_cvssV2_iot_impact))))+" % DE VULNERABILIDADES CON SEVERIDAD MEDIA, LA PUNTUACION DE IMPACTO ESTA ENTRE 0 Y 1 \n")      
print("      -    LA PUNTUACION MEDIA DE IMPACTO EN LAS VULNERABILIDADES CON SEVERIDAD MEDIA ES : "+str(float(((count_medium_severity_cvssV2_sh_impact+count_medium_severity_cvssV2_iot_impact)/(counter_medium_severity_cvssV2_sh_impact+counter_medium_severity_cvssV2_iot_impact))))+"\n")      
