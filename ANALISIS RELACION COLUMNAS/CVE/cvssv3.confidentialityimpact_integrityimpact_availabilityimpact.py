




import pandas as pd

#Abro los ficheros con los que voy a tratar


df_cve_iot=pd.read_excel('cves_iot_2023.xlsx')
df_cve_sh=pd.read_excel('cves_smart_home_2023.xlsx')


print("*********************RELACION COLUMNAS IMPACTO DE CONFIDENCIALIDAD/INTEGRIDAD/DISPONIBILIDAD CVSSV3 PARTE IOT*********************")
print("\n")
print("\n")



#Variables donde almacenare el impacto de confidencialidad
high_confidentiality_iot_cvssv3=0

#Variables donde almacenare el nivel de integridad segun un nivel especificado de confidencialidad
high_confidentiality_lowintegrity_iot_cvssv3=0
high_confidentiality_highintegrity_iot_cvssv3=0
high_confidentiality_mediumintegrity_iot_cvssv3=0
high_confidentiality_noneintegrity_iot_cvssv3=0

#Variables donde almacenare el nivel de disponibilidad segun un nivel especificado de confidencialidad
high_confidentiality_lowavailability_iot_cvssv3=0
high_confidentiality_highavailability_iot_cvssv3=0
high_confidentiality_mediumavailability_iot_cvssv3=0
high_confidentiality_noneavailability_iot_cvssv3=0

low_confidentiality_iot_cvssv3=0
low_confidentiality_lowintegrity_iot_cvssv3=0
low_confidentiality_highintegrity_iot_cvssv3=0
low_confidentiality_mediumintegrity_iot_cvssv3=0
low_confidentiality_noneintegrity_iot_cvssv3=0
low_confidentiality_lowavailability_iot_cvssv3=0
low_confidentiality_highavailability_iot_cvssv3=0
low_confidentiality_mediumavailability_iot_cvssv3=0
low_confidentiality_noneavailability_iot_cvssv3=0

medium_confidentiality_iot_cvssv3=0
medium_confidentiality_lowintegrity_iot_cvssv3=0
medium_confidentiality_highintegrity_iot_cvssv3=0
medium_confidentiality_mediumintegrity_iot_cvssv3=0
medium_confidentiality_noneintegrity_iot_cvssv3=0
medium_confidentiality_lowavailability_iot_cvssv3=0
medium_confidentiality_highavailability_iot_cvssv3=0
medium_confidentiality_mediumavailability_iot_cvssv3=0
medium_confidentiality_noneavailability_iot_cvssv3=0

none_confidentiality_iot_cvssv3=0
none_confidentiality_lowintegrity_iot_cvssv3=0
none_confidentiality_highintegrity_iot_cvssv3=0
none_confidentiality_mediumintegrity_iot_cvssv3=0
none_confidentiality_noneintegrity_iot_cvssv3=0
none_confidentiality_lowavailability_iot_cvssv3=0
none_confidentiality_highavailability_iot_cvssv3=0
none_confidentiality_mediumavailability_iot_cvssv3=0
none_confidentiality_noneavailability_iot_cvssv3=0

#Variables donde almacenare el impacto de integridad
high_integrity_iot_cvssv3=0
#Variables donde almacenare el nivel de confidencialidad segun un nivel especificado de integridad
high_integrity_lowconfidentiality_iot_cvssv3=0
high_integrity_highconfidentiality_iot_cvssv3=0
high_integrity_mediumconfidentiality_iot_cvssv3=0
high_integrity_noneconfidentiality_iot_cvssv3=0
#Variables donde almacenare el nivel de disponibilidad segun un nivel especificado de integridad
high_integrity_lowavailability_iot_cvssv3=0
high_integrity_highavailability_iot_cvssv3=0
high_integrity_mediumavailability_iot_cvssv3=0
high_integrity_noneavailability_iot_cvssv3=0

low_integrity_iot_cvssv3=0
low_integrity_lowconfidentiality_iot_cvssv3=0
low_integrity_highconfidentiality_iot_cvssv3=0
low_integrity_mediumconfidentiality_iot_cvssv3=0
low_integrity_noneconfidentiality_iot_cvssv3=0
low_integrity_lowavailability_iot_cvssv3=0
low_integrity_highavailability_iot_cvssv3=0
low_integrity_mediumavailability_iot_cvssv3=0
low_integrity_noneavailability_iot_cvssv3=0

medium_integrity_iot_cvssv3=0
medium_integrity_lowconfidentiality_iot_cvssv3=0
medium_integrity_highconfidentiality_iot_cvssv3=0
medium_integrity_mediumconfidentiality_iot_cvssv3=0
medium_integrity_noneconfidentiality_iot_cvssv3=0
medium_integrity_lowavailability_iot_cvssv3=0
medium_integrity_highavailability_iot_cvssv3=0
medium_integrity_mediumavailability_iot_cvssv3=0
medium_integrity_noneavailability_iot_cvssv3=0

none_integrity_iot_cvssv3=0
none_integrity_lowconfidentiality_iot_cvssv3=0
none_integrity_highconfidentiality_iot_cvssv3=0
none_integrity_mediumconfidentiality_iot_cvssv3=0
none_integrity_noneconfidentiality_iot_cvssv3=0
none_integrity_lowavailability_iot_cvssv3=0
none_integrity_highavailability_iot_cvssv3=0
none_integrity_mediumavailability_iot_cvssv3=0
none_integrity_noneavailability_iot_cvssv3=0


#Variables donde almacenare un valor de disponibilidad concreto
high_availability_iot_cvssv3=0
#Variables donde almacenare el nivel de confidencialidad segun un nivel especificado de disponibilidad
high_availability_lowconfidentiality_iot_cvssv3=0
high_availability_highconfidentiality_iot_cvssv3=0
high_availability_mediumconfidentiality_iot_cvssv3=0
high_availability_noneconfidentiality_iot_cvssv3=0
#Variables donde almacenare el nivel de integridad segun un nivel especificado de disponibilidad
high_availability_lowintegrity_iot_cvssv3=0
high_availability_highintegrity_iot_cvssv3=0
high_availability_mediumintegrity_iot_cvssv3=0
high_availability_noneintegrity_iot_cvssv3=0

low_availability_iot_cvssv3=0
low_availability_lowconfidentiality_iot_cvssv3=0
low_availability_highconfidentiality_iot_cvssv3=0
low_availability_mediumconfidentiality_iot_cvssv3=0
low_availability_noneconfidentiality_iot_cvssv3=0
low_availability_lowintegrity_iot_cvssv3=0
low_availability_highintegrity_iot_cvssv3=0
low_availability_mediumintegrity_iot_cvssv3=0
low_availability_noneintegrity_iot_cvssv3=0


medium_availability_iot_cvssv3=0
medium_availability_lowconfidentiality_iot_cvssv3=0
medium_availability_highconfidentiality_iot_cvssv3=0
medium_availability_mediumconfidentiality_iot_cvssv3=0
medium_availability_noneconfidentiality_iot_cvssv3=0
medium_availability_lowintegrity_iot_cvssv3=0
medium_availability_highintegrity_iot_cvssv3=0
medium_availability_mediumintegrity_iot_cvssv3=0
medium_availability_noneintegrity_iot_cvssv3=0



none_availability_iot_cvssv3=0
none_availability_lowconfidentiality_iot_cvssv3=0
none_availability_highconfidentiality_iot_cvssv3=0
none_availability_mediumconfidentiality_iot_cvssv3=0
none_availability_noneconfidentiality_iot_cvssv3=0
none_availability_lowintegrity_iot_cvssv3=0
none_availability_highintegrity_iot_cvssv3=0
none_availability_mediumintegrity_iot_cvssv3=0
none_availability_noneintegrity_iot_cvssv3=0



#Primeramente recorro los distintos valores de confidencialidad y posteriormente consulto los valores de integridad y voy aumentando contadores
for j in range(0,len(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.confidentialityImpact"])):
    if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.confidentialityImpact"][j]=='HIGH'):
        high_confidentiality_iot_cvssv3+=1
        if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"][j]=='HIGH'):
            high_confidentiality_highintegrity_iot_cvssv3+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"][j]=='LOW'):
            high_confidentiality_lowintegrity_iot_cvssv3+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"][j]=='MEDIUM'):
            high_confidentiality_mediumintegrity_iot_cvssv3+=1
        else:
            high_confidentiality_noneintegrity_iot_cvssv3+=1
            
    elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.confidentialityImpact"][j]=='LOW'):
        low_confidentiality_iot_cvssv3+=1
        if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"][j]=='HIGH'):
            low_confidentiality_highintegrity_iot_cvssv3+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"][j]=='LOW'):
            low_confidentiality_lowintegrity_iot_cvssv3+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"][j]=='MEDIUM'):
            low_confidentiality_mediumintegrity_iot_cvssv3+=1
        else:
            low_confidentiality_noneintegrity_iot_cvssv3+=1
            
    elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.confidentialityImpact"][j]=='MEDIUM'):
        medium_confidentiality_iot_cvssv3+=1
        if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"][j]=='HIGH'):
            medium_confidentiality_highintegrity_iot_cvssv3+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"][j]=='LOW'):
            medium_confidentiality_lowintegrity_iot_cvssv3+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"][j]=='MEDIUM'):
            medium_confidentiality_mediumintegrity_iot_cvssv3+=1
        else:
            medium_confidentiality_noneintegrity_iot_cvssv3+=1
    else:
        none_confidentiality_iot_cvssv3+=1
        if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"][j]=='HIGH'):
            none_confidentiality_highintegrity_iot_cvssv3+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"][j]=='LOW'):
            none_confidentiality_lowintegrity_iot_cvssv3+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"][j]=='MEDIUM'):
            none_confidentiality_mediumintegrity_iot_cvssv3+=1
        else:
            none_confidentiality_noneintegrity_iot_cvssv3+=1
            
            
            
            
            
            
            
            
            
            
            
 #Recorro los distintos valores de confidencialidad y posteriormente consulto los valores de disponibilidad y voy aumentando contadores           
for h in range(0,len(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.confidentialityImpact"])):
    if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.confidentialityImpact"][h]=='HIGH'):
        if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"][h]=='HIGH'):
            high_confidentiality_highavailability_iot_cvssv3+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"][h]=='LOW'):
            high_confidentiality_lowavailability_iot_cvssv3+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"][h]=='MEDIUM'):
            high_confidentiality_mediumavailability_iot_cvssv3+=1
        else:
            high_confidentiality_noneavailability_iot_cvssv3+=1
            
    elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.confidentialityImpact"][h]=='LOW'):
        if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"][h]=='HIGH'):
            low_confidentiality_highavailability_iot_cvssv3+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"][h]=='LOW'):
            low_confidentiality_lowavailability_iot_cvssv3+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"][h]=='MEDIUM'):
            low_confidentiality_mediumavailability_iot_cvssv3+=1
        else:
            low_confidentiality_noneavailability_iot_cvssv3+=1
            
    elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.confidentialityImpact"][h]=='MEDIUM'):
        if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"][h]=='HIGH'):
            medium_confidentiality_highavailability_iot_cvssv3+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"][h]=='LOW'):
            medium_confidentiality_lowavailability_iot_cvssv3+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"][h]=='MEDIUM'):
            medium_confidentiality_mediumavailability_iot_cvssv3+=1
        else:
            medium_confidentiality_noneavailability_iot_cvssv3+=1
    else:
        if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"][h]=='HIGH'):
            none_confidentiality_highavailability_iot_cvssv3+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"][h]=='LOW'):
            none_confidentiality_lowavailability_iot_cvssv3+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"][h]=='MEDIUM'):
            none_confidentiality_mediumavailability_iot_cvssv3+=1
        else:
            none_confidentiality_noneavailability_iot_cvssv3+=1




            
            
            
#Primeramente recorro los distintos valores de disponibilidad y posteriormente consulto los valores de integridad y voy aumentando contadores
for k in range(0,len(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"])):
    if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"][k]=='HIGH'):
        high_availability_iot_cvssv3+=1
        if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"][k]=='HIGH'):
            high_availability_highintegrity_iot_cvssv3+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"][k]=='LOW'):
            high_availability_lowintegrity_iot_cvssv3+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"][k]=='MEDIUM'):
            high_availability_mediumintegrity_iot_cvssv3+=1
        else:
            high_availability_noneintegrity_iot_cvssv3+=1
            
    elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"][k]=='LOW'):
        low_availability_iot_cvssv3+=1
        if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"][k]=='HIGH'):
            low_availability_highintegrity_iot_cvssv3+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"][k]=='LOW'):
            low_availability_lowintegrity_iot_cvssv3+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"][k]=='MEDIUM'):
            low_availability_mediumintegrity_iot_cvssv3+=1
        else:
            low_availability_noneintegrity_iot_cvssv3+=1
            
    elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"][k]=='MEDIUM'):
        medium_availability_iot_cvssv3+=1
        if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"][k]=='HIGH'):
            medium_availability_highintegrity_iot_cvssv3+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"][k]=='LOW'):
            medium_availability_lowintegrity_iot_cvssv3+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"][k]=='MEDIUM'):
            medium_availability_mediumintegrity_iot_cvssv3+=1
        else:
            medium_availability_noneintegrity_iot_cvssv3+=1
    else:
        none_availability_iot_cvssv3+=1
        if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"][k]=='HIGH'):
            none_availability_highintegrity_iot_cvssv3+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"][k]=='LOW'):
            none_availability_lowintegrity_iot_cvssv3+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"][k]=='MEDIUM'):
            none_availability_mediumintegrity_iot_cvssv3+=1
        else:
            none_availability_noneintegrity_iot_cvssv3+=1
            
            
            
            
#Primeramente recorro los distintos valores de disponibilidad y posteriormente consulto los valores de confidencialidad y voy aumentando contadores            
for l in range(0,len(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"])):
    if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"][l]=='HIGH'):
        if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.confidentialityImpact"][l]=='HIGH'):
            high_availability_highconfidentiality_iot_cvssv3+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.confidentialityImpact"][l]=='LOW'):
            high_availability_lowconfidentiality_iot_cvssv3+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.confidentialityImpact"][l]=='MEDIUM'):
            high_availability_mediumconfidentiality_iot_cvssv3+=1
        else:
            high_availability_noneconfidentiality_iot_cvssv3+=1
            
    elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"][l]=='LOW'):
        if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.confidentialityImpact"][l]=='HIGH'):
            low_availability_highconfidentiality_iot_cvssv3+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.confidentialityImpact"][l]=='LOW'):
            low_availability_lowconfidentiality_iot_cvssv3+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.confidentialityImpact"][l]=='MEDIUM'):
            low_availability_mediumconfidentiality_iot_cvssv3+=1
        else:
            low_availability_noneconfidentiality_iot_cvssv3+=1
            
    elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"][l]=='MEDIUM'):
        if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.confidentialityImpact"][l]=='HIGH'):
            medium_availability_highconfidentiality_iot_cvssv3+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.confidentialityImpact"][l]=='LOW'):
            medium_availability_lowconfidentiality_iot_cvssv3+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.confidentialityImpact"][l]=='MEDIUM'):
            medium_availability_mediumconfidentiality_iot_cvssv3+=1
        else:
            medium_availability_noneconfidentiality_iot_cvssv3+=1
    else:
        if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.confidentialityImpact"][l]=='HIGH'):
            none_availability_highconfidentiality_iot_cvssv3+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.confidentialityImpact"][l]=='LOW'):
            none_availability_lowconfidentiality_iot_cvssv3+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.confidentialityImpact"][l]=='MEDIUM'):
            none_availability_mediumconfidentiality_iot_cvssv3+=1
        else:
            none_availability_noneconfidentiality_iot_cvssv3+=1
            
            
            

#Primeramente recorro los distintos valores de integridad y posteriormente consulto los valores de confidencialidad y voy aumentando contadores
for n in range(0,len(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"])):
    if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"][n]=='HIGH'):
        high_integrity_iot_cvssv3+=1
        if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.confidentialityImpact"][n]=='HIGH'):
            high_integrity_highconfidentiality_iot_cvssv3+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.confidentialityImpact"][n]=='LOW'):
            high_integrity_lowconfidentiality_iot_cvssv3+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.confidentialityImpact"][n]=='MEDIUM'):
            high_integrity_mediumconfidentiality_iot_cvssv3+=1
        else:
            high_integrity_noneconfidentiality_iot_cvssv3+=1
            
    elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"][n]=='LOW'):
        low_integrity_iot_cvssv3+=1
        if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.confidentialityImpact"][n]=='HIGH'):
            low_integrity_highconfidentiality_iot_cvssv3+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.confidentialityImpact"][n]=='LOW'):
            low_integrity_lowconfidentiality_iot_cvssv3+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.confidentialityImpact"][n]=='MEDIUM'):
            low_integrity_mediumconfidentiality_iot_cvssv3+=1
        else:
            low_integrity_noneconfidentiality_iot_cvssv3+=1
            
    elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"][n]=='MEDIUM'):
        medium_integrity_iot_cvssv3+=1
        if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.confidentialityImpact"][n]=='HIGH'):
            medium_integrity_highconfidentiality_iot_cvssv3+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.confidentialityImpact"][n]=='LOW'):
            medium_integrity_lowconfidentiality_iot_cvssv3+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.confidentialityImpact"][n]=='MEDIUM'):
            medium_integrity_mediumconfidentiality_iot_cvssv3+=1
        else:
            medium_integrity_noneconfidentiality_iot_cvssv3+=1
    else:
        none_integrity_iot_cvssv3+=1
        if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.confidentialityImpact"][n]=='HIGH'):
            none_integrity_highconfidentiality_iot_cvssv3+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.confidentialityImpact"][n]=='LOW'):
            none_integrity_lowconfidentiality_iot_cvssv3+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.confidentialityImpact"][n]=='MEDIUM'):
            none_integrity_mediumconfidentiality_iot_cvssv3+=1
        else:
            none_integrity_noneconfidentiality_iot_cvssv3+=1
            
            
            
            
            
#Primeramente recorro los distintos valores de integridad y posteriormente consulto los valores de disponibilidad y voy aumentando contadores            
for p in range(0,len(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"])):
    if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"][p]=='HIGH'):
        if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"][p]=='HIGH'):
            high_integrity_highavailability_iot_cvssv3+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"][p]=='LOW'):
            high_integrity_lowavailability_iot_cvssv3+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"][p]=='MEDIUM'):
            high_integrity_mediumavailability_iot_cvssv3+=1
        else:
            high_integrity_noneavailability_iot_cvssv3+=1
            
    elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"][p]=='LOW'):
        if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"][p]=='HIGH'):
            low_integrity_highavailability_iot_cvssv3+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"][p]=='LOW'):
            low_integrity_lowavailability_iot_cvssv3+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"][p]=='MEDIUM'):
            low_integrity_mediumavailability_iot_cvssv3+=1
        else:
            low_integrity_noneavailability_iot_cvssv3+=1
            
    elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"][p]=='MEDIUM'):
        if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"][p]=='HIGH'):
            medium_integrity_highavailability_iot_cvssv3+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"][p]=='LOW'):
            medium_integrity_lowavailability_iot_cvssv3+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"][p]=='MEDIUM'):
            medium_integrity_mediumavailability_iot_cvssv3+=1
        else:
            medium_integrity_noneavailability_iot_cvssv3+=1
    else:
        if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"][p]=='HIGH'):
            none_integrity_highavailability_iot_cvssv3+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"][p]=='LOW'):
            none_integrity_lowavailability_iot_cvssv3+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"][p]=='MEDIUM'):
            none_integrity_mediumavailability_iot_cvssv3+=1
        else:
            none_integrity_noneavailability_iot_cvssv3+=1
            
            
            
print("************************** ESTADÍSTICAS RELACIÓN IMPACTO DE CONFIDENCIALIDAD/INTEGRIDAD/DISPONIBILIDAD CVSSV3 CVE IOT********************************")
print("\n")
print(" DE UN TOTAL DE "+str(high_confidentiality_iot_cvssv3+medium_confidentiality_iot_cvssv3+low_confidentiality_iot_cvssv3+none_confidentiality_iot_cvssv3)+" VULNERABILIDADES, LAS ESTADÍSTICAS DE IMPACTO DE CONFIDENCIALIDAD/INTEGRIDAD Y DISPONIBILIDAD SON LAS SIGUIENTES: \n")
print("\n")
print(" - DE UN TOTAL DE "+str(high_confidentiality_iot_cvssv3)+" VULNERABILIDADES DONDE EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
print("      - LAS ESTADÍSTICAS DE IMPACTO DE INTEGRIDAD SON LAS SIGUIENTES : \n")
print("             - UN TOTAL DE "+str(high_confidentiality_highintegrity_iot_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD ALTO \n")
print("             - UN TOTAL DE "+str(high_confidentiality_lowintegrity_iot_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD BAJO \n")
print("             - UN TOTAL DE "+str(high_confidentiality_mediumintegrity_iot_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD MEDIO \n")
print("             - UN TOTAL DE "+str(high_confidentiality_noneintegrity_iot_cvssv3)+" VULNERABILIDADES NO EXISTE AFECTACION/IMPACTO A LA INTEGRIDAD DEL SISTEMA: \n")
print("\n")
print("      - LAS ESTADÍSTICAS DE IMPACTO DE DISPONIBILIDAD SON LAS SIGUIENTES : \n")
print("             - UN TOTAL DE "+str(high_confidentiality_highavailability_iot_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD ALTO \n")
print("             - UN TOTAL DE "+str(high_confidentiality_lowavailability_iot_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD BAJO \n")
print("             - UN TOTAL DE "+str(high_confidentiality_mediumavailability_iot_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD MEDIO \n")
print("             - UN TOTAL DE "+str(high_confidentiality_noneavailability_iot_cvssv3)+" VULNERABILIDADES NO EXISTE AFECTACION/IMPACTO A LA DISPONIBILIDAD DEL SISTEMA: \n")

print(" - DE UN TOTAL DE "+str(low_confidentiality_iot_cvssv3)+" VULNERABILIDADES DONDE EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
print("      - LAS ESTADÍSTICAS DE IMPACTO DE INTEGRIDAD SON LAS SIGUIENTES : \n")
print("             - UN TOTAL DE "+str(low_confidentiality_highintegrity_iot_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD ALTO \n")
print("             - UN TOTAL DE "+str(low_confidentiality_lowintegrity_iot_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD BAJO \n")
print("             - UN TOTAL DE "+str(low_confidentiality_mediumintegrity_iot_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD MEDIO \n")
print("             - UN TOTAL DE "+str(low_confidentiality_noneintegrity_iot_cvssv3)+" VULNERABILIDADES NO EXISTE AFECTACION/IMPACTO A LA INTEGRIDAD DEL SISTEMA: \n")
print("\n")
print("      - LAS ESTADÍSTICAS DE IMPACTO DE DISPONIBILIDAD SON LAS SIGUIENTES : \n")
print("             - UN TOTAL DE "+str(low_confidentiality_highavailability_iot_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD ALTO \n")
print("             - UN TOTAL DE "+str(low_confidentiality_lowavailability_iot_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD BAJO \n")
print("             - UN TOTAL DE "+str(low_confidentiality_mediumavailability_iot_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD MEDIO \n")
print("             - UN TOTAL DE "+str(low_confidentiality_noneavailability_iot_cvssv3)+" VULNERABILIDADES NO EXISTE AFECTACION/IMPACTO A LA DISPONIBILIDAD DEL SISTEMA: \n")

print(" - DE UN TOTAL DE "+str(medium_confidentiality_iot_cvssv3)+" VULNERABILIDADES DONDE EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO \n")
print("      - LAS ESTADÍSTICAS DE IMPACTO DE INTEGRIDAD SON LAS SIGUIENTES : \n")
print("             - UN TOTAL DE "+str(medium_confidentiality_highintegrity_iot_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD ALTO \n")
print("             - UN TOTAL DE "+str(medium_confidentiality_lowintegrity_iot_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD BAJO \n")
print("             - UN TOTAL DE "+str(medium_confidentiality_mediumintegrity_iot_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD MEDIO \n")
print("             - UN TOTAL DE "+str(medium_confidentiality_noneintegrity_iot_cvssv3)+" VULNERABILIDADES NO EXISTE AFECTACION/IMPACTO A LA INTEGRIDAD DEL SISTEMA: \n")
print("\n")
print("      - LAS ESTADÍSTICAS DE IMPACTO DE DISPONIBILIDAD SON LAS SIGUIENTES : \n")
print("             - UN TOTAL DE "+str(medium_confidentiality_highavailability_iot_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD ALTO \n")
print("             - UN TOTAL DE "+str(medium_confidentiality_lowavailability_iot_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD BAJO \n")
print("             - UN TOTAL DE "+str(medium_confidentiality_mediumavailability_iot_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD MEDIO \n")
print("             - UN TOTAL DE "+str(medium_confidentiality_noneavailability_iot_cvssv3)+" VULNERABILIDADES NO EXISTE AFECTACION/IMPACTO A LA DISPONIBILIDAD DEL SISTEMA: \n")

print(" - DE UN TOTAL DE "+str(none_confidentiality_iot_cvssv3)+" VULNERABILIDADES DONDE NO EXISTE AFECTACION/IMPACTO A LA CONFIDENCIALIDAD DEL SISTEMA \n")
print("      - LAS ESTADÍSTICAS DE IMPACTO DE INTEGRIDAD SON LAS SIGUIENTES : \n")
print("             - UN TOTAL DE "+str(none_confidentiality_highintegrity_iot_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD ALTO \n")
print("             - UN TOTAL DE "+str(none_confidentiality_lowintegrity_iot_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD BAJO \n")
print("             - UN TOTAL DE "+str(none_confidentiality_mediumintegrity_iot_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD MEDIO \n")
print("             - UN TOTAL DE "+str(none_confidentiality_noneintegrity_iot_cvssv3)+" VULNERABILIDADES NO EXISTE AFECTACION/IMPACTO A LA INTEGRIDAD DEL SISTEMA: \n")
print("\n")
print("      - LAS ESTADÍSTICAS DE IMPACTO DE DISPONIBILIDAD SON LAS SIGUIENTES : \n")
print("             - UN TOTAL DE "+str(none_confidentiality_highavailability_iot_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD ALTO \n")
print("             - UN TOTAL DE "+str(none_confidentiality_lowavailability_iot_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD BAJO \n")
print("             - UN TOTAL DE "+str(none_confidentiality_mediumavailability_iot_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD MEDIO \n")
print("             - UN TOTAL DE "+str(none_confidentiality_noneavailability_iot_cvssv3)+" VULNERABILIDADES NO EXISTE AFECTACION/IMPACTO A LA DISPONIBILIDAD DEL SISTEMA: \n")

print("*************************************************************************************************************************")

print("\n")
print(" - DE UN TOTAL DE "+str(high_availability_iot_cvssv3)+" VULNERABILIDADES DONDE EL IMPACTO DE DISPONIBILIDAD ES ALTO \n")
print("      - LAS ESTADÍSTICAS DE IMPACTO DE INTEGRIDAD SON LAS SIGUIENTES : \n")
print("             - UN TOTAL DE "+str(high_availability_highintegrity_iot_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD ALTO \n")
print("             - UN TOTAL DE "+str(high_availability_lowintegrity_iot_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD BAJO \n")
print("             - UN TOTAL DE "+str(high_availability_mediumintegrity_iot_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD MEDIO \n")
print("             - UN TOTAL DE "+str(high_availability_noneintegrity_iot_cvssv3)+" VULNERABILIDADES NO EXISTE AFECTACION/IMPACTO A LA INTEGRIDAD DEL SISTEMA: \n")
print("\n")
print("      - LAS ESTADÍSTICAS DE IMPACTO DE CONFIDENCIALIDAD SON LAS SIGUIENTES : \n")
print("             - UN TOTAL DE "+str(high_availability_highconfidentiality_iot_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD ALTO \n")
print("             - UN TOTAL DE "+str(high_availability_lowconfidentiality_iot_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD BAJO \n")
print("             - UN TOTAL DE "+str(high_availability_mediumconfidentiality_iot_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD MEDIO \n")
print("             - UN TOTAL DE "+str(high_availability_noneconfidentiality_iot_cvssv3)+" VULNERABILIDADES NO EXISTE AFECTACION/IMPACTO A LA CONFIDENCIALIDAD DEL SISTEMA: \n")
print("\n")
print(" - DE UN TOTAL DE "+str(low_availability_iot_cvssv3)+" VULNERABILIDADES DONDE EL IMPACTO DE DISPONIBILIDAD ES BAJO \n")
print("      - LAS ESTADÍSTICAS DE IMPACTO DE INTEGRIDAD SON LAS SIGUIENTES : \n")
print("             - UN TOTAL DE "+str(low_availability_highintegrity_iot_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD ALTO \n")
print("             - UN TOTAL DE "+str(low_availability_lowintegrity_iot_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD BAJO \n")
print("             - UN TOTAL DE "+str(low_availability_mediumintegrity_iot_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD MEDIO \n")
print("             - UN TOTAL DE "+str(low_availability_noneintegrity_iot_cvssv3)+" VULNERABILIDADES NO EXISTE AFECTACION/IMPACTO A LA INTEGRIDAD DEL SISTEMA: \n")
print("\n")
print("      - LAS ESTADÍSTICAS DE IMPACTO DE CONFIDENCIALIDAD SON LAS SIGUIENTES : \n")
print("             - UN TOTAL DE "+str(low_availability_highconfidentiality_iot_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD ALTO \n")
print("             - UN TOTAL DE "+str(low_availability_lowconfidentiality_iot_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD BAJO \n")
print("             - UN TOTAL DE "+str(low_availability_mediumconfidentiality_iot_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD MEDIO \n")
print("             - UN TOTAL DE "+str(low_availability_noneconfidentiality_iot_cvssv3)+" VULNERABILIDADES NO EXISTE AFECTACION/IMPACTO A LA CONFIDENCIALIDAD DEL SISTEMA: \n")
print("\n")
print(" - DE UN TOTAL DE "+str(medium_availability_iot_cvssv3)+" VULNERABILIDADES DONDE EL IMPACTO DE DISPONIBILIDAD ES MEDIO \n")
print("      - LAS ESTADÍSTICAS DE IMPACTO DE INTEGRIDAD SON LAS SIGUIENTES : \n")
print("             - UN TOTAL DE "+str(medium_availability_highintegrity_iot_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD ALTO \n")
print("             - UN TOTAL DE "+str(medium_availability_lowintegrity_iot_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD BAJO \n")
print("             - UN TOTAL DE "+str(medium_availability_mediumintegrity_iot_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD MEDIO \n")
print("             - UN TOTAL DE "+str(medium_availability_noneintegrity_iot_cvssv3)+" VULNERABILIDADES NO EXISTE AFECTACION/IMPACTO A LA INTEGRIDAD DEL SISTEMA: \n")
print("\n")
print("      - LAS ESTADÍSTICAS DE IMPACTO DE CONFIDENCIALIDAD SON LAS SIGUIENTES : \n")
print("             - UN TOTAL DE "+str(medium_availability_highconfidentiality_iot_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD ALTO \n")
print("             - UN TOTAL DE "+str(medium_availability_lowconfidentiality_iot_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD BAJO \n")
print("             - UN TOTAL DE "+str(medium_availability_mediumconfidentiality_iot_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD MEDIO \n")
print("             - UN TOTAL DE "+str(medium_availability_noneconfidentiality_iot_cvssv3)+" VULNERABILIDADES NO EXISTE AFECTACION/IMPACTO A LA CONFIDENCIALIDAD DEL SISTEMA: \n")
print("\n")
print(" - DE UN TOTAL DE "+str(none_availability_iot_cvssv3)+" VULNERABILIDADES DONDE NO EXISTE AFECTACION/IMPACTO A LA DISPONIBILIDAD DEL SISTEMA \n")
print("      - LAS ESTADÍSTICAS DE IMPACTO DE INTEGRIDAD SON LAS SIGUIENTES : \n")
print("             - UN TOTAL DE "+str(none_availability_highintegrity_iot_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD ALTO \n")
print("             - UN TOTAL DE "+str(none_availability_lowintegrity_iot_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD BAJO \n")
print("             - UN TOTAL DE "+str(none_availability_mediumintegrity_iot_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD MEDIO \n")
print("             - UN TOTAL DE "+str(none_availability_noneintegrity_iot_cvssv3)+" VULNERABILIDADES NO EXISTE AFECTACION/IMPACTO A LA INTEGRIDAD DEL SISTEMA: \n")
print("\n")
print("      - LAS ESTADÍSTICAS DE IMPACTO DE CONFIDENCIALIDAD SON LAS SIGUIENTES : \n")
print("             - UN TOTAL DE "+str(none_availability_highconfidentiality_iot_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD ALTO \n")
print("             - UN TOTAL DE "+str(none_availability_lowconfidentiality_iot_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD BAJO \n")
print("             - UN TOTAL DE "+str(none_availability_mediumconfidentiality_iot_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD MEDIO \n")
print("             - UN TOTAL DE "+str(none_availability_noneconfidentiality_iot_cvssv3)+" VULNERABILIDADES NO EXISTE AFECTACION/IMPACTO A LA CONFIDENCIALIDAD DEL SISTEMA: \n")


print("*************************************************************************************************************************")
print("\n")
print(" - DE UN TOTAL DE "+str(high_integrity_iot_cvssv3)+" VULNERABILIDADES DONDE EL IMPACTO DE INTEGRIDAD ES ALTO \n")
print("      - LAS ESTADÍSTICAS DE IMPACTO DE CONFIDENCIALIDAD SON LAS SIGUIENTES : \n")
print("             - UN TOTAL DE "+str(high_integrity_highconfidentiality_iot_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD ALTO \n")
print("             - UN TOTAL DE "+str(high_integrity_lowconfidentiality_iot_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD BAJO \n")
print("             - UN TOTAL DE "+str(high_integrity_mediumconfidentiality_iot_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD MEDIO \n")
print("             - UN TOTAL DE "+str(high_integrity_noneconfidentiality_iot_cvssv3)+" VULNERABILIDADES NO EXISTE AFECTACION/IMPACTO A LA CONFIDENCIALIDAD DEL SISTEMA: \n")
print("\n")
print("      - LAS ESTADÍSTICAS DE IMPACTO DE DISPONIBILIDAD SON LAS SIGUIENTES : \n")
print("             - UN TOTAL DE "+str(high_integrity_highavailability_iot_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD ALTO \n")
print("             - UN TOTAL DE "+str(high_integrity_lowavailability_iot_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD BAJO \n")
print("             - UN TOTAL DE "+str(high_integrity_mediumavailability_iot_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD MEDIO \n")
print("             - UN TOTAL DE "+str(high_integrity_noneavailability_iot_cvssv3)+" VULNERABILIDADES NO EXISTE AFECTACION/IMPACTO A LA DISPONIBILIDAD DEL SISTEMA: \n")

print(" - DE UN TOTAL DE "+str(low_integrity_iot_cvssv3)+" VULNERABILIDADES DONDE EL IMPACTO DE INTEGRIDAD ES BAJO \n")
print("      - LAS ESTADÍSTICAS DE IMPACTO DE CONFIDENCIALIDAD SON LAS SIGUIENTES : \n")
print("             - UN TOTAL DE "+str(low_integrity_highconfidentiality_iot_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD ALTO \n")
print("             - UN TOTAL DE "+str(low_integrity_lowconfidentiality_iot_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD BAJO \n")
print("             - UN TOTAL DE "+str(low_integrity_mediumconfidentiality_iot_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD MEDIO \n")
print("             - UN TOTAL DE "+str(low_integrity_noneconfidentiality_iot_cvssv3)+" VULNERABILIDADES NO EXISTE AFECTACION/IMPACTO A LA CONFIDENCIALIDAD DEL SISTEMA: \n")
print("\n")
print("      - LAS ESTADÍSTICAS DE IMPACTO DE DISPONIBILIDAD SON LAS SIGUIENTES : \n")
print("             - UN TOTAL DE "+str(low_integrity_highavailability_iot_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD ALTO \n")
print("             - UN TOTAL DE "+str(low_integrity_lowavailability_iot_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD BAJO \n")
print("             - UN TOTAL DE "+str(low_integrity_mediumavailability_iot_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD MEDIO \n")
print("             - UN TOTAL DE "+str(low_integrity_noneavailability_iot_cvssv3)+" VULNERABILIDADES NO EXISTE AFECTACION/IMPACTO A LA DISPONIBILIDAD DEL SISTEMA: \n")

print(" - DE UN TOTAL DE "+str(medium_integrity_iot_cvssv3)+" VULNERABILIDADES DONDE EL IMPACTO DE INTEGRIDAD ES MEDIO \n")
print("      - LAS ESTADÍSTICAS DE IMPACTO DE CONFIDENCIALIDAD SON LAS SIGUIENTES : \n")
print("             - UN TOTAL DE "+str(medium_integrity_highconfidentiality_iot_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD ALTO \n")
print("             - UN TOTAL DE "+str(medium_integrity_lowconfidentiality_iot_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD BAJO \n")
print("             - UN TOTAL DE "+str(medium_integrity_mediumconfidentiality_iot_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD MEDIO \n")
print("             - UN TOTAL DE "+str(medium_integrity_noneconfidentiality_iot_cvssv3)+" VULNERABILIDADES NO EXISTE AFECTACION/IMPACTO A LA CONFIDENCIALIDAD DEL SISTEMA: \n")
print("\n")
print("      - LAS ESTADÍSTICAS DE IMPACTO DE DISPONIBILIDAD SON LAS SIGUIENTES : \n")
print("             - UN TOTAL DE "+str(medium_integrity_highavailability_iot_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD ALTO \n")
print("             - UN TOTAL DE "+str(medium_integrity_lowavailability_iot_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD BAJO \n")
print("             - UN TOTAL DE "+str(medium_integrity_mediumavailability_iot_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD MEDIO \n")
print("             - UN TOTAL DE "+str(medium_integrity_noneavailability_iot_cvssv3)+" VULNERABILIDADES NO EXISTE AFECTACION/IMPACTO A LA DISPONIBILIDAD DEL SISTEMA: \n")

print(" - DE UN TOTAL DE "+str(none_integrity_iot_cvssv3)+" VULNERABILIDADES DONDE NO EXISTE AFECTACION/IMPACTO A LA INTEGRIDAD DEL SISTEMA \n")
print("      - LAS ESTADÍSTICAS DE IMPACTO DE CONFIDENCIALIDAD SON LAS SIGUIENTES : \n")
print("             - UN TOTAL DE "+str(none_integrity_highconfidentiality_iot_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD ALTO \n")
print("             - UN TOTAL DE "+str(none_integrity_lowconfidentiality_iot_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD BAJO \n")
print("             - UN TOTAL DE "+str(none_integrity_mediumconfidentiality_iot_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD MEDIO \n")
print("             - UN TOTAL DE "+str(none_integrity_noneconfidentiality_iot_cvssv3)+" VULNERABILIDADES NO EXISTE AFECTACION/IMPACTO A LA CONFIDENCIALIDAD DEL SISTEMA: \n")
print("\n")
print("      - LAS ESTADÍSTICAS DE IMPACTO DE DISPONIBILIDAD SON LAS SIGUIENTES : \n")
print("             - UN TOTAL DE "+str(none_integrity_highavailability_iot_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD ALTO \n")
print("             - UN TOTAL DE "+str(none_integrity_lowavailability_iot_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD BAJO \n")
print("             - UN TOTAL DE "+str(none_integrity_mediumavailability_iot_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD MEDIO \n")
print("             - UN TOTAL DE "+str(none_integrity_noneavailability_iot_cvssv3)+" VULNERABILIDADES NO EXISTE AFECTACION/IMPACTO A LA DISPONIBILIDAD DEL SISTEMA: \n")



print("_________________________________________________________________________________________________________________________________________________________________")





print("************************** PORCENTAJES RELACIÓN IMPACTO DE CONFIDENCIALIDAD/INTEGRIDAD/DISPONIBILIDAD CVSSV3 CVE IOT********************************")
print("\n")
print(" DE UN TOTAL DE "+str(high_confidentiality_iot_cvssv3+medium_confidentiality_iot_cvssv3+low_confidentiality_iot_cvssv3+none_confidentiality_iot_cvssv3)+" VULNERABILIDADES, LOS PORCENTAJES DE RELACIÓN DE IMPACTO DE CONFIDENCIALIDAD/INTEGRIDAD/DISPONIBILIDAD SON LOS SIGUIENTES: \n")
print("\n")
print(" - EN EL  "+str(float(((high_confidentiality_iot_cvssv3*100)/len(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"]))))+" % DE LAS VULNERABILIDADES, DONDE EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
print("      - LOS PORCENTAJES DE IMPACTO DE INTEGRIDAD SON LOS SIGUIENTES : \n")
print("             - EL "+str(float(((high_confidentiality_highintegrity_iot_cvssv3*100)/(high_confidentiality_iot_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD ALTO \n")
print("             - EL "+str(float(((high_confidentiality_lowintegrity_iot_cvssv3*100)/(high_confidentiality_iot_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD BAJO \n")
print("             - EL "+str(float(((high_confidentiality_mediumintegrity_iot_cvssv3*100)/(high_confidentiality_iot_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD MEDIO \n")
print("             - EL "+str(float(((high_confidentiality_noneintegrity_iot_cvssv3*100)/(high_confidentiality_iot_cvssv3))))+" % DE LAS VULNERABILIDADES NO EXISTE AFECTACION/IMPACTO A LA INTEGRIDAD DEL SISTEMA \n")
print("\n")
print("      - LOS PORCENTAJES DE IMPACTO DE DISPONIBILIDAD SON LOS SIGUIENTES : \n")
print("             - EL "+str(float(((high_confidentiality_highavailability_iot_cvssv3*100)/(high_confidentiality_iot_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD ALTO \n")
print("             - EL "+str(float(((high_confidentiality_lowavailability_iot_cvssv3*100)/(high_confidentiality_iot_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD BAJO \n")
print("             - EL "+str(float(((high_confidentiality_mediumavailability_iot_cvssv3*100)/(high_confidentiality_iot_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD MEDIO \n")
print("             - EL "+str(float(((high_confidentiality_noneavailability_iot_cvssv3*100)/(high_confidentiality_iot_cvssv3))))+" % DE LAS VULNERABILIDADES NO EXISTE AFECTACION/IMPACTO A LA DISPONIBILIDAD DEL SISTEMA \n")

print("\n")
print(" - EN EL  "+str(float(((low_confidentiality_iot_cvssv3*100)/len(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"]))))+" % DE LAS VULNERABILIDADES, DONDE EL IMPACTO DE CONFIDENCIALIDAD ES BAJO: \n")
print("      - LOS PORCENTAJES DE IMPACTO DE INTEGRIDAD SON LOS SIGUIENTES : \n")
print("             - EL "+str(float(((high_confidentiality_highintegrity_iot_cvssv3*100)/(high_confidentiality_iot_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD ALTO \n")
print("             - EL "+str(float(((high_confidentiality_lowintegrity_iot_cvssv3*100)/(high_confidentiality_iot_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD BAJO \n")
print("             - EL "+str(float(((high_confidentiality_mediumintegrity_iot_cvssv3*100)/(high_confidentiality_iot_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD MEDIO \n")
print("             - EL "+str(float(((high_confidentiality_noneintegrity_iot_cvssv3*100)/(high_confidentiality_iot_cvssv3))))+" % DE LAS VULNERABILIDADES NO EXISTE AFECTACION/IMPACTO A LA INTEGRIDAD DEL SISTEMA \n")
print("\n")
print("      - LOS PORCENTAJES DE IMPACTO DE DISPONIBILIDAD SON LOS SIGUIENTES : \n")
print("             - EL "+str(float(((high_confidentiality_highavailability_iot_cvssv3*100)/(high_confidentiality_iot_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD ALTO \n")
print("             - EL "+str(float(((high_confidentiality_lowavailability_iot_cvssv3*100)/(high_confidentiality_iot_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD BAJO \n")
print("             - EL "+str(float(((high_confidentiality_mediumavailability_iot_cvssv3*100)/(high_confidentiality_iot_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD MEDIO \n")
print("             - EL "+str(float(((high_confidentiality_noneavailability_iot_cvssv3*100)/(high_confidentiality_iot_cvssv3))))+" % DE LAS VULNERABILIDADES NO EXISTE AFECTACION/IMPACTO A LA DISPONIBILIDAD DEL SISTEMA \n")


print("\n")
print(" - EN EL  "+str(float(((medium_confidentiality_iot_cvssv3*100)/len(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"]))))+" % DE LAS VULNERABILIDADES, DONDE EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO \n")
print("      - LOS PORCENTAJES DE IMPACTO DE INTEGRIDAD SON LOS SIGUIENTES : \n")
print("             - EL "+str(float(((high_confidentiality_highintegrity_iot_cvssv3*100)/(high_confidentiality_iot_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD ALTO \n")
print("             - EL "+str(float(((high_confidentiality_lowintegrity_iot_cvssv3*100)/(high_confidentiality_iot_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD BAJO \n")
print("             - EL "+str(float(((high_confidentiality_mediumintegrity_iot_cvssv3*100)/(high_confidentiality_iot_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD MEDIO \n")
print("             - EL "+str(float(((high_confidentiality_noneintegrity_iot_cvssv3*100)/(high_confidentiality_iot_cvssv3))))+" % DE LAS VULNERABILIDADES NO EXISTE AFECTACION/IMPACTO A LA INTEGRIDAD DEL SISTEMA \n")
print("\n")
print("      - LOS PORCENTAJES DE IMPACTO DE DISPONIBILIDAD SON LOS SIGUIENTES : \n")
print("             - EL "+str(float(((high_confidentiality_highavailability_iot_cvssv3*100)/(high_confidentiality_iot_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD ALTO \n")
print("             - EL "+str(float(((high_confidentiality_lowavailability_iot_cvssv3*100)/(high_confidentiality_iot_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD BAJO \n")
print("             - EL "+str(float(((high_confidentiality_mediumavailability_iot_cvssv3*100)/(high_confidentiality_iot_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD MEDIO \n")
print("             - EL "+str(float(((high_confidentiality_noneavailability_iot_cvssv3*100)/(high_confidentiality_iot_cvssv3))))+" % DE LAS VULNERABILIDADES NO EXISTE AFECTACION/IMPACTO A LA DISPONIBILIDAD DEL SISTEMA \n")


print("\n")
print(" - EN EL  "+str(float(((none_confidentiality_iot_cvssv3*100)/len(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"]))))+" % DE LAS VULNERABILIDADES, DONDE NO EXISTE AFECTACION/IMPACTO A LA CONFIDENCIALIDAD DEL SISTEMA \n")
print("      - LOS PORCENTAJES DE IMPACTO DE INTEGRIDAD SON LOS SIGUIENTES : \n")
print("             - EL "+str(float(((high_confidentiality_highintegrity_iot_cvssv3*100)/(high_confidentiality_iot_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD ALTO \n")
print("             - EL "+str(float(((high_confidentiality_lowintegrity_iot_cvssv3*100)/(high_confidentiality_iot_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD BAJO \n")
print("             - EL "+str(float(((high_confidentiality_mediumintegrity_iot_cvssv3*100)/(high_confidentiality_iot_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD MEDIO \n")
print("             - EL "+str(float(((high_confidentiality_noneintegrity_iot_cvssv3*100)/(high_confidentiality_iot_cvssv3))))+" % DE LAS VULNERABILIDADES NO EXISTE AFECTACION/IMPACTO A LA INTEGRIDAD DEL SISTEMA \n")
print("\n")
print("      - LOS PORCENTAJES DE IMPACTO DE DISPONIBILIDAD SON LOS SIGUIENTES : \n")
print("             - EL "+str(float(((high_confidentiality_highavailability_iot_cvssv3*100)/(high_confidentiality_iot_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD ALTO \n")
print("             - EL "+str(float(((high_confidentiality_lowavailability_iot_cvssv3*100)/(high_confidentiality_iot_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD BAJO \n")
print("             - EL "+str(float(((high_confidentiality_mediumavailability_iot_cvssv3*100)/(high_confidentiality_iot_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD MEDIO \n")
print("             - EL "+str(float(((high_confidentiality_noneavailability_iot_cvssv3*100)/(high_confidentiality_iot_cvssv3))))+" % DE LAS VULNERABILIDADES NO EXISTE AFECTACION/IMPACTO A LA DISPONIBILIDAD DEL SISTEMA \n")




print("*************************************************************************************************************************")


print("\n")
print(" - EN EL  "+str(float(((high_integrity_iot_cvssv3*100)/len(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"]))))+" % DE LAS VULNERABILIDADES, DONDE EL IMPACTO DE INTEGRIDAD ES ALTO \n")
print("      - LOS PORCENTAJES DE IMPACTO DE CONFIDENCIALIDAD SON LOS SIGUIENTES : \n")
print("             - EL "+str(float(((high_integrity_highconfidentiality_iot_cvssv3*100)/(high_integrity_iot_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD ALTO \n")
print("             - EL "+str(float(((high_integrity_lowconfidentiality_iot_cvssv3*100)/(high_integrity_iot_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD BAJO \n")
print("             - EL "+str(float(((high_integrity_mediumconfidentiality_iot_cvssv3*100)/(high_integrity_iot_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD MEDIO \n")
print("             - EL "+str(float(((high_integrity_noneconfidentiality_iot_cvssv3*100)/(high_integrity_iot_cvssv3))))+" % DE LAS VULNERABILIDADES NO EXISTE AFECTACION/IMPACTO A LA CONFIDENCIALIDAD DEL SISTEMA \n")
print("\n")
print("      - LOS PORCENTAJES DE IMPACTO DE DISPONIBILIDAD SON LOS SIGUIENTES : \n")
print("             - EL "+str(float(((high_integrity_highavailability_iot_cvssv3*100)/(high_integrity_iot_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD ALTO \n")
print("             - EL "+str(float(((high_integrity_lowavailability_iot_cvssv3*100)/(high_integrity_iot_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD BAJO \n")
print("             - EL "+str(float(((high_integrity_mediumavailability_iot_cvssv3*100)/(high_integrity_iot_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD MEDIO \n")
print("             - EL "+str(float(((high_integrity_noneavailability_iot_cvssv3*100)/(high_integrity_iot_cvssv3))))+" % DE LAS VULNERABILIDADES NO EXISTE AFECTACION/IMPACTO A LA DISPONIBILIDAD DEL SISTEMA \n")




print("\n")
print(" - EN EL  "+str(float(((low_integrity_iot_cvssv3*100)/len(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"]))))+" % DE LAS VULNERABILIDADES, DONDE EL IMPACTO DE INTEGRIDAD ES BAJO \n")
print("      - LOS PORCENTAJES DE IMPACTO DE CONFIDENCIALIDAD SON LOS SIGUIENTES : \n")
print("             - EL "+str(float(((low_integrity_highconfidentiality_iot_cvssv3*100)/(low_integrity_iot_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD ALTO \n")
print("             - EL "+str(float(((low_integrity_lowconfidentiality_iot_cvssv3*100)/(low_integrity_iot_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD BAJO \n")
print("             - EL "+str(float(((low_integrity_mediumconfidentiality_iot_cvssv3*100)/(low_integrity_iot_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD MEDIO \n")
print("             - EL "+str(float(((low_integrity_noneconfidentiality_iot_cvssv3*100)/(low_integrity_iot_cvssv3))))+" % DE LAS VULNERABILIDADES NO EXISTE AFECTACION/IMPACTO A LA CONFIDENCIALIDAD DEL SISTEMA \n")
print("\n")
print("      - LOS PORCENTAJES DE IMPACTO DE DISPONIBILIDAD SON LOS SIGUIENTES : \n")
print("             - EL "+str(float(((low_integrity_highavailability_iot_cvssv3*100)/(low_integrity_iot_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD ALTO \n")
print("             - EL "+str(float(((low_integrity_lowavailability_iot_cvssv3*100)/(low_integrity_iot_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD BAJO \n")
print("             - EL "+str(float(((low_integrity_mediumavailability_iot_cvssv3*100)/(low_integrity_iot_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD MEDIO \n")
print("             - EL "+str(float(((low_integrity_noneavailability_iot_cvssv3*100)/(low_integrity_iot_cvssv3))))+" % DE LAS VULNERABILIDADES NO EXISTE AFECTACION/IMPACTO A LA DISPONIBILIDAD DEL SISTEMA \n")


if(medium_integrity_iot_cvssv3>0):
    print("\n")
    print(" - EN EL  "+str(float(((medium_integrity_iot_cvssv3*100)/len(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"]))))+" % DE LAS VULNERABILIDADES, DONDE EL IMPACTO DE INTEGRIDAD ES MEDIO \n")

    print("      - LOS PORCENTAJES DE IMPACTO DE CONFIDENCIALIDAD SON LOS SIGUIENTES : \n")
    print("             - EL "+str(float(((medium_integrity_highconfidentiality_iot_cvssv3*100)/(medium_integrity_iot_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD ALTO \n")
    print("             - EL "+str(float(((medium_integrity_lowconfidentiality_iot_cvssv3*100)/(medium_integrity_iot_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD BAJO \n")
    print("             - EL "+str(float(((medium_integrity_mediumconfidentiality_iot_cvssv3*100)/(medium_integrity_iot_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD MEDIO \n")
    print("             - EL "+str(float(((medium_integrity_noneconfidentiality_iot_cvssv3*100)/(medium_integrity_iot_cvssv3))))+" % DE LAS VULNERABILIDADES NO EXISTE AFECTACION/IMPACTO A LA CONFIDENCIALIDAD DEL SISTEMA \n")
    print("\n")
    print("      - LOS PORCENTAJES DE IMPACTO DE DISPONIBILIDAD SON LOS SIGUIENTES : \n")
    print("             - EL "+str(float(((medium_integrity_highavailability_iot_cvssv3*100)/(medium_integrity_iot_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD ALTO \n")
    print("             - EL "+str(float(((medium_integrity_lowavailability_iot_cvssv3*100)/(medium_integrity_iot_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD BAJO \n")
    print("             - EL "+str(float(((medium_integrity_mediumavailability_iot_cvssv3*100)/(medium_integrity_iot_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD MEDIO \n")
    print("             - EL "+str(float(((medium_integrity_noneavailability_iot_cvssv3*100)/(medium_integrity_iot_cvssv3))))+" % DE LAS VULNERABILIDADES NO EXISTE AFECTACION/IMPACTO A LA DISPONIBILIDAD DEL SISTEMA \n")



print("\n")
print(" - EN EL  "+str(float(((none_integrity_iot_cvssv3*100)/len(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"]))))+" % DE LAS VULNERABILIDADES, DONDE NO EXISTE AFECTACION/IMPACTO A LA INTEGRIDAD DEL SISTEMA \n")
print("      - LOS PORCENTAJES DE IMPACTO DE CONFIDENCIALIDAD SON LOS SIGUIENTES : \n")
print("             - EL "+str(float(((none_integrity_highconfidentiality_iot_cvssv3*100)/(none_integrity_iot_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD ALTO \n")
print("             - EL "+str(float(((none_integrity_lowconfidentiality_iot_cvssv3*100)/(none_integrity_iot_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD BAJO \n")
print("             - EL "+str(float(((none_integrity_mediumconfidentiality_iot_cvssv3*100)/(none_integrity_iot_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD MEDIO \n")
print("             - EL "+str(float(((none_integrity_noneconfidentiality_iot_cvssv3*100)/(none_integrity_iot_cvssv3))))+" % DE LAS VULNERABILIDADES NO EXISTE AFECTACION/IMPACTO A LA CONFIDENCIALIDAD DEL SISTEMA \n")
print("\n")
print("      - LOS PORCENTAJES DE IMPACTO DE DISPONIBILIDAD SON LOS SIGUIENTES : \n")
print("             - EL "+str(float(((none_integrity_highavailability_iot_cvssv3*100)/(none_integrity_iot_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD ALTO \n")
print("             - EL "+str(float(((none_integrity_lowavailability_iot_cvssv3*100)/(none_integrity_iot_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD BAJO \n")
print("             - EL "+str(float(((none_integrity_mediumavailability_iot_cvssv3*100)/(none_integrity_iot_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD MEDIO \n")
print("             - EL "+str(float(((none_integrity_noneavailability_iot_cvssv3*100)/(none_integrity_iot_cvssv3))))+" % DE LAS VULNERABILIDADES NO EXISTE AFECTACION/IMPACTO A LA DISPONIBILIDAD DEL SISTEMA \n")



print("*************************************************************************************************************************")


print("\n")
print(" - EN EL  "+str(float(((high_availability_iot_cvssv3*100)/len(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"]))))+" % DE LAS VULNERABILIDADES, DONDE EL IMPACTO DE DISPONIBILIDAD ES ALTO \n")
print("      - LOS PORCENTAJES DE IMPACTO DE CONFIDENCIALIDAD SON LOS SIGUIENTES : \n")
print("             - EL "+str(float(((high_availability_highconfidentiality_iot_cvssv3*100)/(high_availability_iot_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD ALTO \n")
print("             - EL "+str(float(((high_availability_lowconfidentiality_iot_cvssv3*100)/(high_availability_iot_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD BAJO \n")
print("             - EL "+str(float(((high_availability_mediumconfidentiality_iot_cvssv3*100)/(high_availability_iot_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD MEDIO \n")
print("             - EL "+str(float(((high_availability_noneconfidentiality_iot_cvssv3*100)/(high_availability_iot_cvssv3))))+" % DE LAS VULNERABILIDADES NO EXISTE AFECTACION/IMPACTO A LA CONFIDENCIALIDAD DEL SISTEMA \n")
print("\n")
print("      - LOS PORCENTAJES DE IMPACTO DE INTEGRIDAD SON LOS SIGUIENTES : \n")
print("             - EL "+str(float(((high_availability_highintegrity_iot_cvssv3*100)/(high_availability_iot_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD ALTO \n")
print("             - EL "+str(float(((high_availability_lowintegrity_iot_cvssv3*100)/(high_availability_iot_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD BAJO \n")
print("             - EL "+str(float(((high_availability_mediumintegrity_iot_cvssv3*100)/(high_availability_iot_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD MEDIO \n")
print("             - EL "+str(float(((high_availability_noneintegrity_iot_cvssv3*100)/(high_availability_iot_cvssv3))))+" % DE LAS VULNERABILIDADES NO EXISTE AFECTACION/IMPACTO A LA INTEGRIDAD DEL SISTEMA \n")


print("\n")
print(" - EN EL  "+str(float(((low_availability_iot_cvssv3*100)/len(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"]))))+" % DE LAS VULNERABILIDADES, DONDE EL IMPACTO DE DISPONIBILIDAD ES BAJO \n")
print("      - LOS PORCENTAJES DE IMPACTO DE CONFIDENCIALIDAD SON LOS SIGUIENTES : \n")
print("             - EL "+str(float(((low_availability_highconfidentiality_iot_cvssv3*100)/(low_availability_iot_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD ALTO \n")
print("             - EL "+str(float(((low_availability_lowconfidentiality_iot_cvssv3*100)/(low_availability_iot_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD BAJO \n")
print("             - EL "+str(float(((low_availability_mediumconfidentiality_iot_cvssv3*100)/(low_availability_iot_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD MEDIO \n")
print("             - EL "+str(float(((low_availability_noneconfidentiality_iot_cvssv3*100)/(low_availability_iot_cvssv3))))+" % DE LAS VULNERABILIDADES NO EXISTE AFECTACION/IMPACTO A LA CONFIDENCIALIDAD DEL SISTEMA \n")
print("\n")
print("      - LOS PORCENTAJES DE IMPACTO DE INTEGRIDAD SON LOS SIGUIENTES : \n")
print("             - EL "+str(float(((low_availability_highintegrity_iot_cvssv3*100)/(low_availability_iot_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD ALTO \n")
print("             - EL "+str(float(((low_availability_lowintegrity_iot_cvssv3*100)/(low_availability_iot_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD BAJO \n")
print("             - EL "+str(float(((low_availability_mediumintegrity_iot_cvssv3*100)/(low_availability_iot_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD MEDIO \n")
print("             - EL "+str(float(((low_availability_noneintegrity_iot_cvssv3*100)/(low_availability_iot_cvssv3))))+" % DE LAS VULNERABILIDADES NO EXISTE AFECTACION/IMPACTO A LA INTEGRIDAD DEL SISTEMA \n")


if(medium_availability_iot_cvssv3>0):
    print("\n")
    print(" - EN EL  "+str(float(((medium_availability_iot_cvssv3*100)/len(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"]))))+" % DE LAS VULNERABILIDADES, DONDE EL IMPACTO DE DISPONIBILIDAD ES MEDIO \n")
    print("      - LOS PORCENTAJES DE IMPACTO DE CONFIDENCIALIDAD SON LOS SIGUIENTES : \n")
    print("             - EL "+str(float(((medium_availability_highconfidentiality_iot_cvssv3*100)/(medium_availability_iot_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD ALTO \n")
    print("             - EL "+str(float(((medium_availability_lowconfidentiality_iot_cvssv3*100)/(medium_availability_iot_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD BAJO \n")
    print("             - EL "+str(float(((medium_availability_mediumconfidentiality_iot_cvssv3*100)/(medium_availability_iot_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD MEDIO \n")
    print("             - EL "+str(float(((medium_availability_noneconfidentiality_iot_cvssv3*100)/(medium_availability_iot_cvssv3))))+" % DE LAS VULNERABILIDADES NO EXISTE AFECTACION/IMPACTO A LA CONFIDENCIALIDAD DEL SISTEMA \n")
    print("\n")
    print("      - LOS PORCENTAJES DE IMPACTO DE INTEGRIDAD SON LOS SIGUIENTES : \n")
    print("             - EL "+str(float(((medium_availability_highintegrity_iot_cvssv3*100)/(medium_availability_iot_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD ALTO \n")
    print("             - EL "+str(float(((medium_availability_lowintegrity_iot_cvssv3*100)/(medium_availability_iot_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD BAJO \n")
    print("             - EL "+str(float(((medium_availability_mediumintegrity_iot_cvssv3*100)/(medium_availability_iot_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD MEDIO \n")
    print("             - EL "+str(float(((medium_availability_noneintegrity_iot_cvssv3*100)/(medium_availability_iot_cvssv3))))+" % DE LAS VULNERABILIDADES NO EXISTE AFECTACION/IMPACTO A LA INTEGRIDAD DEL SISTEMA \n")



print("\n")
print(" - EN EL  "+str(float(((none_availability_iot_cvssv3*100)/len(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"]))))+" % DE LAS VULNERABILIDADES, DONDE NO EXISTE AFECTACION/IMPACTO A LA DISPONIBILIDAD DEL SISTEMA \n")
print("      - LOS PORCENTAJES DE IMPACTO DE CONFIDENCIALIDAD SON LOS SIGUIENTES : \n")
print("             - EL "+str(float(((none_availability_highconfidentiality_iot_cvssv3*100)/(none_availability_iot_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD ALTO \n")
print("             - EL "+str(float(((none_availability_lowconfidentiality_iot_cvssv3*100)/(none_availability_iot_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD BAJO \n")
print("             - EL "+str(float(((none_availability_mediumconfidentiality_iot_cvssv3*100)/(none_availability_iot_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD MEDIO \n")
print("             - EL "+str(float(((none_availability_noneconfidentiality_iot_cvssv3*100)/(none_availability_iot_cvssv3))))+" % DE LAS VULNERABILIDADES NO EXISTE AFECTACION/IMPACTO A LA CONFIDENCIALIDAD DEL SISTEMA \n")
print("\n")
print("      - LOS PORCENTAJES DE IMPACTO DE INTEGRIDAD SON LOS SIGUIENTES : \n")
print("             - EL "+str(float(((none_availability_highintegrity_iot_cvssv3*100)/(none_availability_iot_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD ALTO \n")
print("             - EL "+str(float(((none_availability_lowintegrity_iot_cvssv3*100)/(none_availability_iot_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD BAJO \n")
print("             - EL "+str(float(((none_availability_mediumintegrity_iot_cvssv3*100)/(none_availability_iot_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD MEDIO \n")
print("             - EL "+str(float(((none_availability_noneintegrity_iot_cvssv3*100)/(none_availability_iot_cvssv3))))+" % DE LAS VULNERABILIDADES NO EXISTE AFECTACION/IMPACTO A LA INTEGRIDAD DEL SISTEMA \n")

























print("*********************RELACION COLUMNAS IMPACTO DE CONFIDENCIALIDAD/INTEGRIDAD/DISPONIBILIDAD CVSSV3 PARTE SMART HOME*********************")
print("\n")
print("\n")



#Variables donde almacenare el impacto de confidencialidad
high_confidentiality_sh_cvssv3=0

#Variables donde almacenare el nivel de integridad segun un nivel especificado de confidencialidad
high_confidentiality_lowintegrity_sh_cvssv3=0
high_confidentiality_highintegrity_sh_cvssv3=0
high_confidentiality_mediumintegrity_sh_cvssv3=0
high_confidentiality_noneintegrity_sh_cvssv3=0

#Variables donde almacenare el nivel de disponibilidad segun un nivel especificado de confidencialidad
high_confidentiality_lowavailability_sh_cvssv3=0
high_confidentiality_highavailability_sh_cvssv3=0
high_confidentiality_mediumavailability_sh_cvssv3=0
high_confidentiality_noneavailability_sh_cvssv3=0

low_confidentiality_sh_cvssv3=0
low_confidentiality_lowintegrity_sh_cvssv3=0
low_confidentiality_highintegrity_sh_cvssv3=0
low_confidentiality_mediumintegrity_sh_cvssv3=0
low_confidentiality_noneintegrity_sh_cvssv3=0
low_confidentiality_lowavailability_sh_cvssv3=0
low_confidentiality_highavailability_sh_cvssv3=0
low_confidentiality_mediumavailability_sh_cvssv3=0
low_confidentiality_noneavailability_sh_cvssv3=0

medium_confidentiality_sh_cvssv3=0
medium_confidentiality_lowintegrity_sh_cvssv3=0
medium_confidentiality_highintegrity_sh_cvssv3=0
medium_confidentiality_mediumintegrity_sh_cvssv3=0
medium_confidentiality_noneintegrity_sh_cvssv3=0
medium_confidentiality_lowavailability_sh_cvssv3=0
medium_confidentiality_highavailability_sh_cvssv3=0
medium_confidentiality_mediumavailability_sh_cvssv3=0
medium_confidentiality_noneavailability_sh_cvssv3=0

none_confidentiality_sh_cvssv3=0
none_confidentiality_lowintegrity_sh_cvssv3=0
none_confidentiality_highintegrity_sh_cvssv3=0
none_confidentiality_mediumintegrity_sh_cvssv3=0
none_confidentiality_noneintegrity_sh_cvssv3=0
none_confidentiality_lowavailability_sh_cvssv3=0
none_confidentiality_highavailability_sh_cvssv3=0
none_confidentiality_mediumavailability_sh_cvssv3=0
none_confidentiality_noneavailability_sh_cvssv3=0

#Variables donde almacenare el impacto de integridad
high_integrity_sh_cvssv3=0
#Variables donde almacenare el nivel de confidencialidad segun un nivel especificado de integridad
high_integrity_lowconfidentiality_sh_cvssv3=0
high_integrity_highconfidentiality_sh_cvssv3=0
high_integrity_mediumconfidentiality_sh_cvssv3=0
high_integrity_noneconfidentiality_sh_cvssv3=0
#Variables donde almacenare el nivel de disponibilidad segun un nivel especificado de integridad
high_integrity_lowavailability_sh_cvssv3=0
high_integrity_highavailability_sh_cvssv3=0
high_integrity_mediumavailability_sh_cvssv3=0
high_integrity_noneavailability_sh_cvssv3=0

low_integrity_sh_cvssv3=0
low_integrity_lowconfidentiality_sh_cvssv3=0
low_integrity_highconfidentiality_sh_cvssv3=0
low_integrity_mediumconfidentiality_sh_cvssv3=0
low_integrity_noneconfidentiality_sh_cvssv3=0
low_integrity_lowavailability_sh_cvssv3=0
low_integrity_highavailability_sh_cvssv3=0
low_integrity_mediumavailability_sh_cvssv3=0
low_integrity_noneavailability_sh_cvssv3=0

medium_integrity_sh_cvssv3=0
medium_integrity_lowconfidentiality_sh_cvssv3=0
medium_integrity_highconfidentiality_sh_cvssv3=0
medium_integrity_mediumconfidentiality_sh_cvssv3=0
medium_integrity_noneconfidentiality_sh_cvssv3=0
medium_integrity_lowavailability_sh_cvssv3=0
medium_integrity_highavailability_sh_cvssv3=0
medium_integrity_mediumavailability_sh_cvssv3=0
medium_integrity_noneavailability_sh_cvssv3=0

none_integrity_sh_cvssv3=0
none_integrity_lowconfidentiality_sh_cvssv3=0
none_integrity_highconfidentiality_sh_cvssv3=0
none_integrity_mediumconfidentiality_sh_cvssv3=0
none_integrity_noneconfidentiality_sh_cvssv3=0
none_integrity_lowavailability_sh_cvssv3=0
none_integrity_highavailability_sh_cvssv3=0
none_integrity_mediumavailability_sh_cvssv3=0
none_integrity_noneavailability_sh_cvssv3=0


#Variables donde almacenare un valor de disponibilidad concreto
high_availability_sh_cvssv3=0
#Variables donde almacenare el nivel de confidencialidad segun un nivel especificado de disponibilidad
high_availability_lowconfidentiality_sh_cvssv3=0
high_availability_highconfidentiality_sh_cvssv3=0
high_availability_mediumconfidentiality_sh_cvssv3=0
high_availability_noneconfidentiality_sh_cvssv3=0
#Variables donde almacenare el nivel de integridad segun un nivel especificado de disponibilidad
high_availability_lowintegrity_sh_cvssv3=0
high_availability_highintegrity_sh_cvssv3=0
high_availability_mediumintegrity_sh_cvssv3=0
high_availability_noneintegrity_sh_cvssv3=0

low_availability_sh_cvssv3=0
low_availability_lowconfidentiality_sh_cvssv3=0
low_availability_highconfidentiality_sh_cvssv3=0
low_availability_mediumconfidentiality_sh_cvssv3=0
low_availability_noneconfidentiality_sh_cvssv3=0
low_availability_lowintegrity_sh_cvssv3=0
low_availability_highintegrity_sh_cvssv3=0
low_availability_mediumintegrity_sh_cvssv3=0
low_availability_noneintegrity_sh_cvssv3=0


medium_availability_sh_cvssv3=0
medium_availability_lowconfidentiality_sh_cvssv3=0
medium_availability_highconfidentiality_sh_cvssv3=0
medium_availability_mediumconfidentiality_sh_cvssv3=0
medium_availability_noneconfidentiality_sh_cvssv3=0
medium_availability_lowintegrity_sh_cvssv3=0
medium_availability_highintegrity_sh_cvssv3=0
medium_availability_mediumintegrity_sh_cvssv3=0
medium_availability_noneintegrity_sh_cvssv3=0



none_availability_sh_cvssv3=0
none_availability_lowconfidentiality_sh_cvssv3=0
none_availability_highconfidentiality_sh_cvssv3=0
none_availability_mediumconfidentiality_sh_cvssv3=0
none_availability_noneconfidentiality_sh_cvssv3=0
none_availability_lowintegrity_sh_cvssv3=0
none_availability_highintegrity_sh_cvssv3=0
none_availability_mediumintegrity_sh_cvssv3=0
none_availability_noneintegrity_sh_cvssv3=0



#Primeramente recorro los distintos valores de confidencialidad y posteriormente consulto los valores de integridad y voy aumentando contadores
for j in range(0,len(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.confidentialityImpact"])):
    if(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.confidentialityImpact"][j]=='HIGH'):
        high_confidentiality_sh_cvssv3+=1
        if(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"][j]=='HIGH'):
            high_confidentiality_highintegrity_sh_cvssv3+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"][j]=='LOW'):
            high_confidentiality_lowintegrity_sh_cvssv3+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"][j]=='MEDIUM'):
            high_confidentiality_mediumintegrity_sh_cvssv3+=1
        else:
            high_confidentiality_noneintegrity_sh_cvssv3+=1
            
    elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.confidentialityImpact"][j]=='LOW'):
        low_confidentiality_sh_cvssv3+=1
        if(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"][j]=='HIGH'):
            low_confidentiality_highintegrity_sh_cvssv3+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"][j]=='LOW'):
            low_confidentiality_lowintegrity_sh_cvssv3+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"][j]=='MEDIUM'):
            low_confidentiality_mediumintegrity_sh_cvssv3+=1
        else:
            low_confidentiality_noneintegrity_sh_cvssv3+=1
            
    elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.confidentialityImpact"][j]=='MEDIUM'):
        medium_confidentiality_sh_cvssv3+=1
        if(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"][j]=='HIGH'):
            medium_confidentiality_highintegrity_sh_cvssv3+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"][j]=='LOW'):
            medium_confidentiality_lowintegrity_sh_cvssv3+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"][j]=='MEDIUM'):
            medium_confidentiality_mediumintegrity_sh_cvssv3+=1
        else:
            medium_confidentiality_noneintegrity_sh_cvssv3+=1
    else:
        none_confidentiality_sh_cvssv3+=1
        if(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"][j]=='HIGH'):
            none_confidentiality_highintegrity_sh_cvssv3+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"][j]=='LOW'):
            none_confidentiality_lowintegrity_sh_cvssv3+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"][j]=='MEDIUM'):
            none_confidentiality_mediumintegrity_sh_cvssv3+=1
        else:
            none_confidentiality_noneintegrity_sh_cvssv3+=1
            
            
            
            
            
            
            
            
            
            
            
 #Recorro los distintos valores de confidencialidad y posteriormente consulto los valores de disponibilidad y voy aumentando contadores           
for h in range(0,len(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.confidentialityImpact"])):
    if(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.confidentialityImpact"][h]=='HIGH'):
        if(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"][h]=='HIGH'):
            high_confidentiality_highavailability_sh_cvssv3+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"][h]=='LOW'):
            high_confidentiality_lowavailability_sh_cvssv3+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"][h]=='MEDIUM'):
            high_confidentiality_mediumavailability_sh_cvssv3+=1
        else:
            high_confidentiality_noneavailability_sh_cvssv3+=1
            
    elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.confidentialityImpact"][h]=='LOW'):
        if(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"][h]=='HIGH'):
            low_confidentiality_highavailability_sh_cvssv3+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"][h]=='LOW'):
            low_confidentiality_lowavailability_sh_cvssv3+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"][h]=='MEDIUM'):
            low_confidentiality_mediumavailability_sh_cvssv3+=1
        else:
            low_confidentiality_noneavailability_sh_cvssv3+=1
            
    elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.confidentialityImpact"][h]=='MEDIUM'):
        if(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"][h]=='HIGH'):
            medium_confidentiality_highavailability_sh_cvssv3+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"][h]=='LOW'):
            medium_confidentiality_lowavailability_sh_cvssv3+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"][h]=='MEDIUM'):
            medium_confidentiality_mediumavailability_sh_cvssv3+=1
        else:
            medium_confidentiality_noneavailability_sh_cvssv3+=1
    else:
        if(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"][h]=='HIGH'):
            none_confidentiality_highavailability_sh_cvssv3+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"][h]=='LOW'):
            none_confidentiality_lowavailability_sh_cvssv3+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"][h]=='MEDIUM'):
            none_confidentiality_mediumavailability_sh_cvssv3+=1
        else:
            none_confidentiality_noneavailability_sh_cvssv3+=1




            
            
            
#Primeramente recorro los distintos valores de disponibilidad y posteriormente consulto los valores de integridad y voy aumentando contadores
for k in range(0,len(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"])):
    if(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"][k]=='HIGH'):
        high_availability_sh_cvssv3+=1
        if(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"][k]=='HIGH'):
            high_availability_highintegrity_sh_cvssv3+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"][k]=='LOW'):
            high_availability_lowintegrity_sh_cvssv3+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"][k]=='MEDIUM'):
            high_availability_mediumintegrity_sh_cvssv3+=1
        else:
            high_availability_noneintegrity_sh_cvssv3+=1
            
    elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"][k]=='LOW'):
        low_availability_sh_cvssv3+=1
        if(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"][k]=='HIGH'):
            low_availability_highintegrity_sh_cvssv3+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"][k]=='LOW'):
            low_availability_lowintegrity_sh_cvssv3+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"][k]=='MEDIUM'):
            low_availability_mediumintegrity_sh_cvssv3+=1
        else:
            low_availability_noneintegrity_sh_cvssv3+=1
            
    elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"][k]=='MEDIUM'):
        medium_availability_sh_cvssv3+=1
        if(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"][k]=='HIGH'):
            medium_availability_highintegrity_sh_cvssv3+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"][k]=='LOW'):
            medium_availability_lowintegrity_sh_cvssv3+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"][k]=='MEDIUM'):
            medium_availability_mediumintegrity_sh_cvssv3+=1
        else:
            medium_availability_noneintegrity_sh_cvssv3+=1
    else:
        none_availability_sh_cvssv3+=1
        if(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"][k]=='HIGH'):
            none_availability_highintegrity_sh_cvssv3+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"][k]=='LOW'):
            none_availability_lowintegrity_sh_cvssv3+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"][k]=='MEDIUM'):
            none_availability_mediumintegrity_sh_cvssv3+=1
        else:
            none_availability_noneintegrity_sh_cvssv3+=1
            
            
            
            
#Primeramente recorro los distintos valores de disponibilidad y posteriormente consulto los valores de confidencialidad y voy aumentando contadores            
for l in range(0,len(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"])):
    if(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"][l]=='HIGH'):
        if(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.confidentialityImpact"][l]=='HIGH'):
            high_availability_highconfidentiality_sh_cvssv3+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.confidentialityImpact"][l]=='LOW'):
            high_availability_lowconfidentiality_sh_cvssv3+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.confidentialityImpact"][l]=='MEDIUM'):
            high_availability_mediumconfidentiality_sh_cvssv3+=1
        else:
            high_availability_noneconfidentiality_sh_cvssv3+=1
            
    elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"][l]=='LOW'):
        if(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.confidentialityImpact"][l]=='HIGH'):
            low_availability_highconfidentiality_sh_cvssv3+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.confidentialityImpact"][l]=='LOW'):
            low_availability_lowconfidentiality_sh_cvssv3+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.confidentialityImpact"][l]=='MEDIUM'):
            low_availability_mediumconfidentiality_sh_cvssv3+=1
        else:
            low_availability_noneconfidentiality_sh_cvssv3+=1
            
    elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"][l]=='MEDIUM'):
        if(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.confidentialityImpact"][l]=='HIGH'):
            medium_availability_highconfidentiality_sh_cvssv3+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.confidentialityImpact"][l]=='LOW'):
            medium_availability_lowconfidentiality_sh_cvssv3+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.confidentialityImpact"][l]=='MEDIUM'):
            medium_availability_mediumconfidentiality_sh_cvssv3+=1
        else:
            medium_availability_noneconfidentiality_sh_cvssv3+=1
    else:
        if(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.confidentialityImpact"][l]=='HIGH'):
            none_availability_highconfidentiality_sh_cvssv3+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.confidentialityImpact"][l]=='LOW'):
            none_availability_lowconfidentiality_sh_cvssv3+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.confidentialityImpact"][l]=='MEDIUM'):
            none_availability_mediumconfidentiality_sh_cvssv3+=1
        else:
            none_availability_noneconfidentiality_sh_cvssv3+=1
            
            
            

#Primeramente recorro los distintos valores de integridad y posteriormente consulto los valores de confidencialidad y voy aumentando contadores
for n in range(0,len(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"])):
    if(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"][n]=='HIGH'):
        high_integrity_sh_cvssv3+=1
        if(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.confidentialityImpact"][n]=='HIGH'):
            high_integrity_highconfidentiality_sh_cvssv3+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.confidentialityImpact"][n]=='LOW'):
            high_integrity_lowconfidentiality_sh_cvssv3+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.confidentialityImpact"][n]=='MEDIUM'):
            high_integrity_mediumconfidentiality_sh_cvssv3+=1
        else:
            high_integrity_noneconfidentiality_sh_cvssv3+=1
            
    elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"][n]=='LOW'):
        low_integrity_sh_cvssv3+=1
        if(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.confidentialityImpact"][n]=='HIGH'):
            low_integrity_highconfidentiality_sh_cvssv3+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.confidentialityImpact"][n]=='LOW'):
            low_integrity_lowconfidentiality_sh_cvssv3+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.confidentialityImpact"][n]=='MEDIUM'):
            low_integrity_mediumconfidentiality_sh_cvssv3+=1
        else:
            low_integrity_noneconfidentiality_sh_cvssv3+=1
            
    elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"][n]=='MEDIUM'):
        medium_integrity_sh_cvssv3+=1
        if(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.confidentialityImpact"][n]=='HIGH'):
            medium_integrity_highconfidentiality_sh_cvssv3+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.confidentialityImpact"][n]=='LOW'):
            medium_integrity_lowconfidentiality_sh_cvssv3+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.confidentialityImpact"][n]=='MEDIUM'):
            medium_integrity_mediumconfidentiality_sh_cvssv3+=1
        else:
            medium_integrity_noneconfidentiality_sh_cvssv3+=1
    else:
        none_integrity_sh_cvssv3+=1
        if(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.confidentialityImpact"][n]=='HIGH'):
            none_integrity_highconfidentiality_sh_cvssv3+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.confidentialityImpact"][n]=='LOW'):
            none_integrity_lowconfidentiality_sh_cvssv3+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.confidentialityImpact"][n]=='MEDIUM'):
            none_integrity_mediumconfidentiality_sh_cvssv3+=1
        else:
            none_integrity_noneconfidentiality_sh_cvssv3+=1
            
            
            
            
            
#Primeramente recorro los distintos valores de integridad y posteriormente consulto los valores de disponibilidad y voy aumentando contadores            
for p in range(0,len(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"])):
    if(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"][p]=='HIGH'):
        if(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"][p]=='HIGH'):
            high_integrity_highavailability_sh_cvssv3+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"][p]=='LOW'):
            high_integrity_lowavailability_sh_cvssv3+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"][p]=='MEDIUM'):
            high_integrity_mediumavailability_sh_cvssv3+=1
        else:
            high_integrity_noneavailability_sh_cvssv3+=1
            
    elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"][p]=='LOW'):
        if(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"][p]=='HIGH'):
            low_integrity_highavailability_sh_cvssv3+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"][p]=='LOW'):
            low_integrity_lowavailability_sh_cvssv3+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"][p]=='MEDIUM'):
            low_integrity_mediumavailability_sh_cvssv3+=1
        else:
            low_integrity_noneavailability_sh_cvssv3+=1
            
    elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"][p]=='MEDIUM'):
        if(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"][p]=='HIGH'):
            medium_integrity_highavailability_sh_cvssv3+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"][p]=='LOW'):
            medium_integrity_lowavailability_sh_cvssv3+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"][p]=='MEDIUM'):
            medium_integrity_mediumavailability_sh_cvssv3+=1
        else:
            medium_integrity_noneavailability_sh_cvssv3+=1
    else:
        if(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"][p]=='HIGH'):
            none_integrity_highavailability_sh_cvssv3+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"][p]=='LOW'):
            none_integrity_lowavailability_sh_cvssv3+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"][p]=='MEDIUM'):
            none_integrity_mediumavailability_sh_cvssv3+=1
        else:
            none_integrity_noneavailability_sh_cvssv3+=1
            
            
            
print("************************** ESTADÍSTICAS RELACIÓN IMPACTO DE CONFIDENCIALIDAD/INTEGRIDAD/DISPONIBILIDAD CVSSV3 CVE SMART HOME********************************")
print("\n")
print(" DE UN TOTAL DE "+str(high_confidentiality_sh_cvssv3+medium_confidentiality_sh_cvssv3+low_confidentiality_sh_cvssv3+none_confidentiality_sh_cvssv3)+" VULNERABILIDADES, LAS ESTADÍSTICAS DE IMPACTO DE CONFIDENCIALIDAD/INTEGRIDAD Y DISPONIBILIDAD SON LAS SIGUIENTES: \n")
print("\n")
print(" - DE UN TOTAL DE "+str(high_confidentiality_sh_cvssv3)+" VULNERABILIDADES DONDE EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
print("      - LAS ESTADÍSTICAS DE IMPACTO DE INTEGRIDAD SON LAS SIGUIENTES : \n")
print("             - UN TOTAL DE "+str(high_confidentiality_highintegrity_sh_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD ALTO \n")
print("             - UN TOTAL DE "+str(high_confidentiality_lowintegrity_sh_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD BAJO \n")
print("             - UN TOTAL DE "+str(high_confidentiality_mediumintegrity_sh_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD MEDIO \n")
print("             - UN TOTAL DE "+str(high_confidentiality_noneintegrity_sh_cvssv3)+" VULNERABILIDADES NO EXISTE AFECTACION/IMPACTO A LA INTEGRIDAD DEL SISTEMA: \n")
print("\n")
print("      - LAS ESTADÍSTICAS DE IMPACTO DE DISPONIBILIDAD SON LAS SIGUIENTES : \n")
print("             - UN TOTAL DE "+str(high_confidentiality_highavailability_sh_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD ALTO \n")
print("             - UN TOTAL DE "+str(high_confidentiality_lowavailability_sh_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD BAJO \n")
print("             - UN TOTAL DE "+str(high_confidentiality_mediumavailability_sh_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD MEDIO \n")
print("             - UN TOTAL DE "+str(high_confidentiality_noneavailability_sh_cvssv3)+" VULNERABILIDADES NO EXISTE AFECTACION/IMPACTO A LA DISPONIBILIDAD DEL SISTEMA: \n")

print(" - DE UN TOTAL DE "+str(low_confidentiality_sh_cvssv3)+" VULNERABILIDADES DONDE EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
print("      - LAS ESTADÍSTICAS DE IMPACTO DE INTEGRIDAD SON LAS SIGUIENTES : \n")
print("             - UN TOTAL DE "+str(low_confidentiality_highintegrity_sh_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD ALTO \n")
print("             - UN TOTAL DE "+str(low_confidentiality_lowintegrity_sh_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD BAJO \n")
print("             - UN TOTAL DE "+str(low_confidentiality_mediumintegrity_sh_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD MEDIO \n")
print("             - UN TOTAL DE "+str(low_confidentiality_noneintegrity_sh_cvssv3)+" VULNERABILIDADES NO EXISTE AFECTACION/IMPACTO A LA INTEGRIDAD DEL SISTEMA: \n")
print("\n")
print("      - LAS ESTADÍSTICAS DE IMPACTO DE DISPONIBILIDAD SON LAS SIGUIENTES : \n")
print("             - UN TOTAL DE "+str(low_confidentiality_highavailability_sh_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD ALTO \n")
print("             - UN TOTAL DE "+str(low_confidentiality_lowavailability_sh_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD BAJO \n")
print("             - UN TOTAL DE "+str(low_confidentiality_mediumavailability_sh_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD MEDIO \n")
print("             - UN TOTAL DE "+str(low_confidentiality_noneavailability_sh_cvssv3)+" VULNERABILIDADES NO EXISTE AFECTACION/IMPACTO A LA DISPONIBILIDAD DEL SISTEMA: \n")

print(" - DE UN TOTAL DE "+str(medium_confidentiality_sh_cvssv3)+" VULNERABILIDADES DONDE EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO \n")
print("      - LAS ESTADÍSTICAS DE IMPACTO DE INTEGRIDAD SON LAS SIGUIENTES : \n")
print("             - UN TOTAL DE "+str(medium_confidentiality_highintegrity_sh_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD ALTO \n")
print("             - UN TOTAL DE "+str(medium_confidentiality_lowintegrity_sh_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD BAJO \n")
print("             - UN TOTAL DE "+str(medium_confidentiality_mediumintegrity_sh_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD MEDIO \n")
print("             - UN TOTAL DE "+str(medium_confidentiality_noneintegrity_sh_cvssv3)+" VULNERABILIDADES NO EXISTE AFECTACION/IMPACTO A LA INTEGRIDAD DEL SISTEMA: \n")
print("\n")
print("      - LAS ESTADÍSTICAS DE IMPACTO DE DISPONIBILIDAD SON LAS SIGUIENTES : \n")
print("             - UN TOTAL DE "+str(medium_confidentiality_highavailability_sh_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD ALTO \n")
print("             - UN TOTAL DE "+str(medium_confidentiality_lowavailability_sh_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD BAJO \n")
print("             - UN TOTAL DE "+str(medium_confidentiality_mediumavailability_sh_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD MEDIO \n")
print("             - UN TOTAL DE "+str(medium_confidentiality_noneavailability_sh_cvssv3)+" VULNERABILIDADES NO EXISTE AFECTACION/IMPACTO A LA DISPONIBILIDAD DEL SISTEMA: \n")

print(" - DE UN TOTAL DE "+str(none_confidentiality_sh_cvssv3)+" VULNERABILIDADES DONDE NO EXISTE AFECTACION/IMPACTO A LA CONFIDENCIALIDAD DEL SISTEMA \n")
print("      - LAS ESTADÍSTICAS DE IMPACTO DE INTEGRIDAD SON LAS SIGUIENTES : \n")
print("             - UN TOTAL DE "+str(none_confidentiality_highintegrity_sh_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD ALTO \n")
print("             - UN TOTAL DE "+str(none_confidentiality_lowintegrity_sh_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD BAJO \n")
print("             - UN TOTAL DE "+str(none_confidentiality_mediumintegrity_sh_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD MEDIO \n")
print("             - UN TOTAL DE "+str(none_confidentiality_noneintegrity_sh_cvssv3)+" VULNERABILIDADES NO EXISTE AFECTACION/IMPACTO A LA INTEGRIDAD DEL SISTEMA: \n")
print("\n")
print("      - LAS ESTADÍSTICAS DE IMPACTO DE DISPONIBILIDAD SON LAS SIGUIENTES : \n")
print("             - UN TOTAL DE "+str(none_confidentiality_highavailability_sh_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD ALTO \n")
print("             - UN TOTAL DE "+str(none_confidentiality_lowavailability_sh_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD BAJO \n")
print("             - UN TOTAL DE "+str(none_confidentiality_mediumavailability_sh_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD MEDIO \n")
print("             - UN TOTAL DE "+str(none_confidentiality_noneavailability_sh_cvssv3)+" VULNERABILIDADES NO EXISTE AFECTACION/IMPACTO A LA DISPONIBILIDAD DEL SISTEMA: \n")

print("*************************************************************************************************************************")

print("\n")
print(" - DE UN TOTAL DE "+str(high_availability_sh_cvssv3)+" VULNERABILIDADES DONDE EL IMPACTO DE DISPONIBILIDAD ES ALTO \n")
print("      - LAS ESTADÍSTICAS DE IMPACTO DE INTEGRIDAD SON LAS SIGUIENTES : \n")
print("             - UN TOTAL DE "+str(high_availability_highintegrity_sh_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD ALTO \n")
print("             - UN TOTAL DE "+str(high_availability_lowintegrity_sh_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD BAJO \n")
print("             - UN TOTAL DE "+str(high_availability_mediumintegrity_sh_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD MEDIO \n")
print("             - UN TOTAL DE "+str(high_availability_noneintegrity_sh_cvssv3)+" VULNERABILIDADES NO EXISTE AFECTACION/IMPACTO A LA INTEGRIDAD DEL SISTEMA: \n")
print("\n")
print("      - LAS ESTADÍSTICAS DE IMPACTO DE CONFIDENCIALIDAD SON LAS SIGUIENTES : \n")
print("             - UN TOTAL DE "+str(high_availability_highconfidentiality_sh_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD ALTO \n")
print("             - UN TOTAL DE "+str(high_availability_lowconfidentiality_sh_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD BAJO \n")
print("             - UN TOTAL DE "+str(high_availability_mediumconfidentiality_sh_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD MEDIO \n")
print("             - UN TOTAL DE "+str(high_availability_noneconfidentiality_sh_cvssv3)+" VULNERABILIDADES NO EXISTE AFECTACION/IMPACTO A LA CONFIDENCIALIDAD DEL SISTEMA: \n")
print("\n")
print(" - DE UN TOTAL DE "+str(low_availability_sh_cvssv3)+" VULNERABILIDADES DONDE EL IMPACTO DE DISPONIBILIDAD ES BAJO \n")
print("      - LAS ESTADÍSTICAS DE IMPACTO DE INTEGRIDAD SON LAS SIGUIENTES : \n")
print("             - UN TOTAL DE "+str(low_availability_highintegrity_sh_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD ALTO \n")
print("             - UN TOTAL DE "+str(low_availability_lowintegrity_sh_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD BAJO \n")
print("             - UN TOTAL DE "+str(low_availability_mediumintegrity_sh_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD MEDIO \n")
print("             - UN TOTAL DE "+str(low_availability_noneintegrity_sh_cvssv3)+" VULNERABILIDADES NO EXISTE AFECTACION/IMPACTO A LA INTEGRIDAD DEL SISTEMA: \n")
print("\n")
print("      - LAS ESTADÍSTICAS DE IMPACTO DE CONFIDENCIALIDAD SON LAS SIGUIENTES : \n")
print("             - UN TOTAL DE "+str(low_availability_highconfidentiality_sh_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD ALTO \n")
print("             - UN TOTAL DE "+str(low_availability_lowconfidentiality_sh_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD BAJO \n")
print("             - UN TOTAL DE "+str(low_availability_mediumconfidentiality_sh_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD MEDIO \n")
print("             - UN TOTAL DE "+str(low_availability_noneconfidentiality_sh_cvssv3)+" VULNERABILIDADES NO EXISTE AFECTACION/IMPACTO A LA CONFIDENCIALIDAD DEL SISTEMA: \n")
print("\n")
print(" - DE UN TOTAL DE "+str(medium_availability_sh_cvssv3)+" VULNERABILIDADES DONDE EL IMPACTO DE DISPONIBILIDAD ES MEDIO \n")
print("      - LAS ESTADÍSTICAS DE IMPACTO DE INTEGRIDAD SON LAS SIGUIENTES : \n")
print("             - UN TOTAL DE "+str(medium_availability_highintegrity_sh_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD ALTO \n")
print("             - UN TOTAL DE "+str(medium_availability_lowintegrity_sh_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD BAJO \n")
print("             - UN TOTAL DE "+str(medium_availability_mediumintegrity_sh_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD MEDIO \n")
print("             - UN TOTAL DE "+str(medium_availability_noneintegrity_sh_cvssv3)+" VULNERABILIDADES NO EXISTE AFECTACION/IMPACTO A LA INTEGRIDAD DEL SISTEMA: \n")
print("\n")
print("      - LAS ESTADÍSTICAS DE IMPACTO DE CONFIDENCIALIDAD SON LAS SIGUIENTES : \n")
print("             - UN TOTAL DE "+str(medium_availability_highconfidentiality_sh_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD ALTO \n")
print("             - UN TOTAL DE "+str(medium_availability_lowconfidentiality_sh_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD BAJO \n")
print("             - UN TOTAL DE "+str(medium_availability_mediumconfidentiality_sh_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD MEDIO \n")
print("             - UN TOTAL DE "+str(medium_availability_noneconfidentiality_sh_cvssv3)+" VULNERABILIDADES NO EXISTE AFECTACION/IMPACTO A LA CONFIDENCIALIDAD DEL SISTEMA: \n")
print("\n")
print(" - DE UN TOTAL DE "+str(none_availability_sh_cvssv3)+" VULNERABILIDADES DONDE NO EXISTE AFECTACION/IMPACTO A LA DISPONIBILIDAD DEL SISTEMA \n")
print("      - LAS ESTADÍSTICAS DE IMPACTO DE INTEGRIDAD SON LAS SIGUIENTES : \n")
print("             - UN TOTAL DE "+str(none_availability_highintegrity_sh_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD ALTO \n")
print("             - UN TOTAL DE "+str(none_availability_lowintegrity_sh_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD BAJO \n")
print("             - UN TOTAL DE "+str(none_availability_mediumintegrity_sh_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD MEDIO \n")
print("             - UN TOTAL DE "+str(none_availability_noneintegrity_sh_cvssv3)+" VULNERABILIDADES NO EXISTE AFECTACION/IMPACTO A LA INTEGRIDAD DEL SISTEMA: \n")
print("\n")
print("      - LAS ESTADÍSTICAS DE IMPACTO DE CONFIDENCIALIDAD SON LAS SIGUIENTES : \n")
print("             - UN TOTAL DE "+str(none_availability_highconfidentiality_sh_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD ALTO \n")
print("             - UN TOTAL DE "+str(none_availability_lowconfidentiality_sh_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD BAJO \n")
print("             - UN TOTAL DE "+str(none_availability_mediumconfidentiality_sh_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD MEDIO \n")
print("             - UN TOTAL DE "+str(none_availability_noneconfidentiality_sh_cvssv3)+" VULNERABILIDADES NO EXISTE AFECTACION/IMPACTO A LA CONFIDENCIALIDAD DEL SISTEMA: \n")


print("*************************************************************************************************************************")
print("\n")
print(" - DE UN TOTAL DE "+str(high_integrity_sh_cvssv3)+" VULNERABILIDADES DONDE EL IMPACTO DE INTEGRIDAD ES ALTO \n")
print("      - LAS ESTADÍSTICAS DE IMPACTO DE CONFIDENCIALIDAD SON LAS SIGUIENTES : \n")
print("             - UN TOTAL DE "+str(high_integrity_highconfidentiality_sh_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD ALTO \n")
print("             - UN TOTAL DE "+str(high_integrity_lowconfidentiality_sh_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD BAJO \n")
print("             - UN TOTAL DE "+str(high_integrity_mediumconfidentiality_sh_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD MEDIO \n")
print("             - UN TOTAL DE "+str(high_integrity_noneconfidentiality_sh_cvssv3)+" VULNERABILIDADES NO EXISTE AFECTACION/IMPACTO A LA CONFIDENCIALIDAD DEL SISTEMA: \n")
print("\n")
print("      - LAS ESTADÍSTICAS DE IMPACTO DE DISPONIBILIDAD SON LAS SIGUIENTES : \n")
print("             - UN TOTAL DE "+str(high_integrity_highavailability_sh_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD ALTO \n")
print("             - UN TOTAL DE "+str(high_integrity_lowavailability_sh_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD BAJO \n")
print("             - UN TOTAL DE "+str(high_integrity_mediumavailability_sh_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD MEDIO \n")
print("             - UN TOTAL DE "+str(high_integrity_noneavailability_sh_cvssv3)+" VULNERABILIDADES NO EXISTE AFECTACION/IMPACTO A LA DISPONIBILIDAD DEL SISTEMA: \n")

print(" - DE UN TOTAL DE "+str(low_integrity_sh_cvssv3)+" VULNERABILIDADES DONDE EL IMPACTO DE INTEGRIDAD ES BAJO \n")
print("      - LAS ESTADÍSTICAS DE IMPACTO DE CONFIDENCIALIDAD SON LAS SIGUIENTES : \n")
print("             - UN TOTAL DE "+str(low_integrity_highconfidentiality_sh_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD ALTO \n")
print("             - UN TOTAL DE "+str(low_integrity_lowconfidentiality_sh_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD BAJO \n")
print("             - UN TOTAL DE "+str(low_integrity_mediumconfidentiality_sh_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD MEDIO \n")
print("             - UN TOTAL DE "+str(low_integrity_noneconfidentiality_sh_cvssv3)+" VULNERABILIDADES NO EXISTE AFECTACION/IMPACTO A LA CONFIDENCIALIDAD DEL SISTEMA: \n")
print("\n")
print("      - LAS ESTADÍSTICAS DE IMPACTO DE DISPONIBILIDAD SON LAS SIGUIENTES : \n")
print("             - UN TOTAL DE "+str(low_integrity_highavailability_sh_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD ALTO \n")
print("             - UN TOTAL DE "+str(low_integrity_lowavailability_sh_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD BAJO \n")
print("             - UN TOTAL DE "+str(low_integrity_mediumavailability_sh_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD MEDIO \n")
print("             - UN TOTAL DE "+str(low_integrity_noneavailability_sh_cvssv3)+" VULNERABILIDADES NO EXISTE AFECTACION/IMPACTO A LA DISPONIBILIDAD DEL SISTEMA: \n")

print(" - DE UN TOTAL DE "+str(medium_integrity_sh_cvssv3)+" VULNERABILIDADES DONDE EL IMPACTO DE INTEGRIDAD ES MEDIO \n")
print("      - LAS ESTADÍSTICAS DE IMPACTO DE CONFIDENCIALIDAD SON LAS SIGUIENTES : \n")
print("             - UN TOTAL DE "+str(medium_integrity_highconfidentiality_sh_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD ALTO \n")
print("             - UN TOTAL DE "+str(medium_integrity_lowconfidentiality_sh_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD BAJO \n")
print("             - UN TOTAL DE "+str(medium_integrity_mediumconfidentiality_sh_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD MEDIO \n")
print("             - UN TOTAL DE "+str(medium_integrity_noneconfidentiality_sh_cvssv3)+" VULNERABILIDADES NO EXISTE AFECTACION/IMPACTO A LA CONFIDENCIALIDAD DEL SISTEMA: \n")
print("\n")
print("      - LAS ESTADÍSTICAS DE IMPACTO DE DISPONIBILIDAD SON LAS SIGUIENTES : \n")
print("             - UN TOTAL DE "+str(medium_integrity_highavailability_sh_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD ALTO \n")
print("             - UN TOTAL DE "+str(medium_integrity_lowavailability_sh_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD BAJO \n")
print("             - UN TOTAL DE "+str(medium_integrity_mediumavailability_sh_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD MEDIO \n")
print("             - UN TOTAL DE "+str(medium_integrity_noneavailability_sh_cvssv3)+" VULNERABILIDADES NO EXISTE AFECTACION/IMPACTO A LA DISPONIBILIDAD DEL SISTEMA: \n")

print(" - DE UN TOTAL DE "+str(none_integrity_sh_cvssv3)+" VULNERABILIDADES DONDE NO EXISTE AFECTACION/IMPACTO A LA INTEGRIDAD DEL SISTEMA \n")
print("      - LAS ESTADÍSTICAS DE IMPACTO DE CONFIDENCIALIDAD SON LAS SIGUIENTES : \n")
print("             - UN TOTAL DE "+str(none_integrity_highconfidentiality_sh_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD ALTO \n")
print("             - UN TOTAL DE "+str(none_integrity_lowconfidentiality_sh_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD BAJO \n")
print("             - UN TOTAL DE "+str(none_integrity_mediumconfidentiality_sh_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD MEDIO \n")
print("             - UN TOTAL DE "+str(none_integrity_noneconfidentiality_sh_cvssv3)+" VULNERABILIDADES NO EXISTE AFECTACION/IMPACTO A LA CONFIDENCIALIDAD DEL SISTEMA: \n")
print("\n")
print("      - LAS ESTADÍSTICAS DE IMPACTO DE DISPONIBILIDAD SON LAS SIGUIENTES : \n")
print("             - UN TOTAL DE "+str(none_integrity_highavailability_sh_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD ALTO \n")
print("             - UN TOTAL DE "+str(none_integrity_lowavailability_sh_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD BAJO \n")
print("             - UN TOTAL DE "+str(none_integrity_mediumavailability_sh_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD MEDIO \n")
print("             - UN TOTAL DE "+str(none_integrity_noneavailability_sh_cvssv3)+" VULNERABILIDADES NO EXISTE AFECTACION/IMPACTO A LA DISPONIBILIDAD DEL SISTEMA: \n")



print("_________________________________________________________________________________________________________________________________________________________________")





print("************************** PORCENTAJES RELACIÓN IMPACTO DE CONFIDENCIALIDAD/INTEGRIDAD/DISPONIBILIDAD CVSSV3 CVE SMART HOME********************************")
print("\n")
print(" DE UN TOTAL DE "+str(high_confidentiality_sh_cvssv3+medium_confidentiality_sh_cvssv3+low_confidentiality_sh_cvssv3+none_confidentiality_sh_cvssv3)+" VULNERABILIDADES, LOS PORCENTAJES DE RELACIÓN DE IMPACTO DE CONFIDENCIALIDAD/INTEGRIDAD/DISPONIBILIDAD SON LOS SIGUIENTES: \n")
print("\n")
print(" - EN EL  "+str(float(((high_confidentiality_sh_cvssv3*100)/len(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"]))))+" % DE LAS VULNERABILIDADES, DONDE EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
print("      - LOS PORCENTAJES DE IMPACTO DE INTEGRIDAD SON LOS SIGUIENTES : \n")
print("             - EL "+str(float(((high_confidentiality_highintegrity_sh_cvssv3*100)/(high_confidentiality_sh_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD ALTO \n")
print("             - EL "+str(float(((high_confidentiality_lowintegrity_sh_cvssv3*100)/(high_confidentiality_sh_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD BAJO \n")
print("             - EL "+str(float(((high_confidentiality_mediumintegrity_sh_cvssv3*100)/(high_confidentiality_sh_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD MEDIO \n")
print("             - EL "+str(float(((high_confidentiality_noneintegrity_sh_cvssv3*100)/(high_confidentiality_sh_cvssv3))))+" % DE LAS VULNERABILIDADES NO EXISTE AFECTACION/IMPACTO A LA INTEGRIDAD DEL SISTEMA \n")
print("\n")
print("      - LOS PORCENTAJES DE IMPACTO DE DISPONIBILIDAD SON LOS SIGUIENTES : \n")
print("             - EL "+str(float(((high_confidentiality_highavailability_sh_cvssv3*100)/(high_confidentiality_sh_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD ALTO \n")
print("             - EL "+str(float(((high_confidentiality_lowavailability_sh_cvssv3*100)/(high_confidentiality_sh_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD BAJO \n")
print("             - EL "+str(float(((high_confidentiality_mediumavailability_sh_cvssv3*100)/(high_confidentiality_sh_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD MEDIO \n")
print("             - EL "+str(float(((high_confidentiality_noneavailability_sh_cvssv3*100)/(high_confidentiality_sh_cvssv3))))+" % DE LAS VULNERABILIDADES NO EXISTE AFECTACION/IMPACTO A LA DISPONIBILIDAD DEL SISTEMA \n")

print("\n")
print(" - EN EL  "+str(float(((low_confidentiality_sh_cvssv3*100)/len(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"]))))+" % DE LAS VULNERABILIDADES, DONDE EL IMPACTO DE CONFIDENCIALIDAD ES BAJO: \n")
print("      - LOS PORCENTAJES DE IMPACTO DE INTEGRIDAD SON LOS SIGUIENTES : \n")
print("             - EL "+str(float(((high_confidentiality_highintegrity_sh_cvssv3*100)/(high_confidentiality_sh_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD ALTO \n")
print("             - EL "+str(float(((high_confidentiality_lowintegrity_sh_cvssv3*100)/(high_confidentiality_sh_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD BAJO \n")
print("             - EL "+str(float(((high_confidentiality_mediumintegrity_sh_cvssv3*100)/(high_confidentiality_sh_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD MEDIO \n")
print("             - EL "+str(float(((high_confidentiality_noneintegrity_sh_cvssv3*100)/(high_confidentiality_sh_cvssv3))))+" % DE LAS VULNERABILIDADES NO EXISTE AFECTACION/IMPACTO A LA INTEGRIDAD DEL SISTEMA \n")
print("\n")
print("      - LOS PORCENTAJES DE IMPACTO DE DISPONIBILIDAD SON LOS SIGUIENTES : \n")
print("             - EL "+str(float(((high_confidentiality_highavailability_sh_cvssv3*100)/(high_confidentiality_sh_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD ALTO \n")
print("             - EL "+str(float(((high_confidentiality_lowavailability_sh_cvssv3*100)/(high_confidentiality_sh_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD BAJO \n")
print("             - EL "+str(float(((high_confidentiality_mediumavailability_sh_cvssv3*100)/(high_confidentiality_sh_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD MEDIO \n")
print("             - EL "+str(float(((high_confidentiality_noneavailability_sh_cvssv3*100)/(high_confidentiality_sh_cvssv3))))+" % DE LAS VULNERABILIDADES NO EXISTE AFECTACION/IMPACTO A LA DISPONIBILIDAD DEL SISTEMA \n")


print("\n")
print(" - EN EL  "+str(float(((medium_confidentiality_sh_cvssv3*100)/len(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"]))))+" % DE LAS VULNERABILIDADES, DONDE EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO \n")
print("      - LOS PORCENTAJES DE IMPACTO DE INTEGRIDAD SON LOS SIGUIENTES : \n")
print("             - EL "+str(float(((high_confidentiality_highintegrity_sh_cvssv3*100)/(high_confidentiality_sh_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD ALTO \n")
print("             - EL "+str(float(((high_confidentiality_lowintegrity_sh_cvssv3*100)/(high_confidentiality_sh_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD BAJO \n")
print("             - EL "+str(float(((high_confidentiality_mediumintegrity_sh_cvssv3*100)/(high_confidentiality_sh_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD MEDIO \n")
print("             - EL "+str(float(((high_confidentiality_noneintegrity_sh_cvssv3*100)/(high_confidentiality_sh_cvssv3))))+" % DE LAS VULNERABILIDADES NO EXISTE AFECTACION/IMPACTO A LA INTEGRIDAD DEL SISTEMA \n")
print("\n")
print("      - LOS PORCENTAJES DE IMPACTO DE DISPONIBILIDAD SON LOS SIGUIENTES : \n")
print("             - EL "+str(float(((high_confidentiality_highavailability_sh_cvssv3*100)/(high_confidentiality_sh_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD ALTO \n")
print("             - EL "+str(float(((high_confidentiality_lowavailability_sh_cvssv3*100)/(high_confidentiality_sh_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD BAJO \n")
print("             - EL "+str(float(((high_confidentiality_mediumavailability_sh_cvssv3*100)/(high_confidentiality_sh_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD MEDIO \n")
print("             - EL "+str(float(((high_confidentiality_noneavailability_sh_cvssv3*100)/(high_confidentiality_sh_cvssv3))))+" % DE LAS VULNERABILIDADES NO EXISTE AFECTACION/IMPACTO A LA DISPONIBILIDAD DEL SISTEMA \n")


print("\n")
print(" - EN EL  "+str(float(((none_confidentiality_sh_cvssv3*100)/len(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"]))))+" % DE LAS VULNERABILIDADES, DONDE NO EXISTE AFECTACION/IMPACTO A LA CONFIDENCIALIDAD DEL SISTEMA \n")
print("      - LOS PORCENTAJES DE IMPACTO DE INTEGRIDAD SON LOS SIGUIENTES : \n")
print("             - EL "+str(float(((high_confidentiality_highintegrity_sh_cvssv3*100)/(high_confidentiality_sh_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD ALTO \n")
print("             - EL "+str(float(((high_confidentiality_lowintegrity_sh_cvssv3*100)/(high_confidentiality_sh_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD BAJO \n")
print("             - EL "+str(float(((high_confidentiality_mediumintegrity_sh_cvssv3*100)/(high_confidentiality_sh_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD MEDIO \n")
print("             - EL "+str(float(((high_confidentiality_noneintegrity_sh_cvssv3*100)/(high_confidentiality_sh_cvssv3))))+" % DE LAS VULNERABILIDADES NO EXISTE AFECTACION/IMPACTO A LA INTEGRIDAD DEL SISTEMA \n")
print("\n")
print("      - LOS PORCENTAJES DE IMPACTO DE DISPONIBILIDAD SON LOS SIGUIENTES : \n")
print("             - EL "+str(float(((high_confidentiality_highavailability_sh_cvssv3*100)/(high_confidentiality_sh_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD ALTO \n")
print("             - EL "+str(float(((high_confidentiality_lowavailability_sh_cvssv3*100)/(high_confidentiality_sh_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD BAJO \n")
print("             - EL "+str(float(((high_confidentiality_mediumavailability_sh_cvssv3*100)/(high_confidentiality_sh_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD MEDIO \n")
print("             - EL "+str(float(((high_confidentiality_noneavailability_sh_cvssv3*100)/(high_confidentiality_sh_cvssv3))))+" % DE LAS VULNERABILIDADES NO EXISTE AFECTACION/IMPACTO A LA DISPONIBILIDAD DEL SISTEMA \n")



print("*************************************************************************************************************************")


print("\n")
print(" - EN EL  "+str(float(((high_integrity_sh_cvssv3*100)/len(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"]))))+" % DE LAS VULNERABILIDADES, DONDE EL IMPACTO DE INTEGRIDAD ES ALTO \n")
print("      - LOS PORCENTAJES DE IMPACTO DE CONFIDENCIALIDAD SON LOS SIGUIENTES : \n")
print("             - EL "+str(float(((high_integrity_highconfidentiality_sh_cvssv3*100)/(high_integrity_sh_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD ALTO \n")
print("             - EL "+str(float(((high_integrity_lowconfidentiality_sh_cvssv3*100)/(high_integrity_sh_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD BAJO \n")
print("             - EL "+str(float(((high_integrity_mediumconfidentiality_sh_cvssv3*100)/(high_integrity_sh_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD MEDIO \n")
print("             - EL "+str(float(((high_integrity_noneconfidentiality_sh_cvssv3*100)/(high_integrity_sh_cvssv3))))+" % DE LAS VULNERABILIDADES NO EXISTE AFECTACION/IMPACTO A LA CONFIDENCIALIDAD DEL SISTEMA \n")
print("\n")
print("      - LOS PORCENTAJES DE IMPACTO DE DISPONIBILIDAD SON LOS SIGUIENTES : \n")
print("             - EL "+str(float(((high_integrity_highavailability_sh_cvssv3*100)/(high_integrity_sh_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD ALTO \n")
print("             - EL "+str(float(((high_integrity_lowavailability_sh_cvssv3*100)/(high_integrity_sh_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD BAJO \n")
print("             - EL "+str(float(((high_integrity_mediumavailability_sh_cvssv3*100)/(high_integrity_sh_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD MEDIO \n")
print("             - EL "+str(float(((high_integrity_noneavailability_sh_cvssv3*100)/(high_integrity_sh_cvssv3))))+" % DE LAS VULNERABILIDADES NO EXISTE AFECTACION/IMPACTO A LA DISPONIBILIDAD DEL SISTEMA \n")




print("\n")
print(" - EN EL  "+str(float(((low_integrity_sh_cvssv3*100)/len(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"]))))+" % DE LAS VULNERABILIDADES, DONDE EL IMPACTO DE INTEGRIDAD ES BAJO \n")
print("      - LOS PORCENTAJES DE IMPACTO DE CONFIDENCIALIDAD SON LOS SIGUIENTES : \n")
print("             - EL "+str(float(((low_integrity_highconfidentiality_sh_cvssv3*100)/(low_integrity_sh_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD ALTO \n")
print("             - EL "+str(float(((low_integrity_lowconfidentiality_sh_cvssv3*100)/(low_integrity_sh_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD BAJO \n")
print("             - EL "+str(float(((low_integrity_mediumconfidentiality_sh_cvssv3*100)/(low_integrity_sh_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD MEDIO \n")
print("             - EL "+str(float(((low_integrity_noneconfidentiality_sh_cvssv3*100)/(low_integrity_sh_cvssv3))))+" % DE LAS VULNERABILIDADES NO EXISTE AFECTACION/IMPACTO A LA CONFIDENCIALIDAD DEL SISTEMA \n")
print("\n")
print("      - LOS PORCENTAJES DE IMPACTO DE DISPONIBILIDAD SON LOS SIGUIENTES : \n")
print("             - EL "+str(float(((low_integrity_highavailability_sh_cvssv3*100)/(low_integrity_sh_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD ALTO \n")
print("             - EL "+str(float(((low_integrity_lowavailability_sh_cvssv3*100)/(low_integrity_sh_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD BAJO \n")
print("             - EL "+str(float(((low_integrity_mediumavailability_sh_cvssv3*100)/(low_integrity_sh_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD MEDIO \n")
print("             - EL "+str(float(((low_integrity_noneavailability_sh_cvssv3*100)/(low_integrity_sh_cvssv3))))+" % DE LAS VULNERABILIDADES NO EXISTE AFECTACION/IMPACTO A LA DISPONIBILIDAD DEL SISTEMA \n")


if(medium_integrity_sh_cvssv3>0):
    print("\n")
    print(" - EN EL  "+str(float(((medium_integrity_sh_cvssv3*100)/len(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"]))))+" % DE LAS VULNERABILIDADES, DONDE EL IMPACTO DE INTEGRIDAD ES MEDIO \n")

    print("      - LOS PORCENTAJES DE IMPACTO DE CONFIDENCIALIDAD SON LOS SIGUIENTES : \n")
    print("             - EL "+str(float(((medium_integrity_highconfidentiality_sh_cvssv3*100)/(medium_integrity_sh_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD ALTO \n")
    print("             - EL "+str(float(((medium_integrity_lowconfidentiality_sh_cvssv3*100)/(medium_integrity_sh_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD BAJO \n")
    print("             - EL "+str(float(((medium_integrity_mediumconfidentiality_sh_cvssv3*100)/(medium_integrity_sh_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD MEDIO \n")
    print("             - EL "+str(float(((medium_integrity_noneconfidentiality_sh_cvssv3*100)/(medium_integrity_sh_cvssv3))))+" % DE LAS VULNERABILIDADES NO EXISTE AFECTACION/IMPACTO A LA CONFIDENCIALIDAD DEL SISTEMA \n")
    print("\n")
    print("      - LOS PORCENTAJES DE IMPACTO DE DISPONIBILIDAD SON LOS SIGUIENTES : \n")
    print("             - EL "+str(float(((medium_integrity_highavailability_sh_cvssv3*100)/(medium_integrity_sh_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD ALTO \n")
    print("             - EL "+str(float(((medium_integrity_lowavailability_sh_cvssv3*100)/(medium_integrity_sh_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD BAJO \n")
    print("             - EL "+str(float(((medium_integrity_mediumavailability_sh_cvssv3*100)/(medium_integrity_sh_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD MEDIO \n")
    print("             - EL "+str(float(((medium_integrity_noneavailability_sh_cvssv3*100)/(medium_integrity_sh_cvssv3))))+" % DE LAS VULNERABILIDADES NO EXISTE AFECTACION/IMPACTO A LA DISPONIBILIDAD DEL SISTEMA \n")



print("\n")
print(" - EN EL  "+str(float(((none_integrity_sh_cvssv3*100)/len(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"]))))+" % DE LAS VULNERABILIDADES, DONDE NO EXISTE AFECTACION/IMPACTO A LA INTEGRIDAD DEL SISTEMA \n")
print("      - LOS PORCENTAJES DE IMPACTO DE CONFIDENCIALIDAD SON LOS SIGUIENTES : \n")
print("             - EL "+str(float(((none_integrity_highconfidentiality_sh_cvssv3*100)/(none_integrity_sh_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD ALTO \n")
print("             - EL "+str(float(((none_integrity_lowconfidentiality_sh_cvssv3*100)/(none_integrity_sh_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD BAJO \n")
print("             - EL "+str(float(((none_integrity_mediumconfidentiality_sh_cvssv3*100)/(none_integrity_sh_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD MEDIO \n")
print("             - EL "+str(float(((none_integrity_noneconfidentiality_sh_cvssv3*100)/(none_integrity_sh_cvssv3))))+" % DE LAS VULNERABILIDADES NO EXISTE AFECTACION/IMPACTO A LA CONFIDENCIALIDAD DEL SISTEMA \n")
print("\n")
print("      - LOS PORCENTAJES DE IMPACTO DE DISPONIBILIDAD SON LOS SIGUIENTES : \n")
print("             - EL "+str(float(((none_integrity_highavailability_sh_cvssv3*100)/(none_integrity_sh_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD ALTO \n")
print("             - EL "+str(float(((none_integrity_lowavailability_sh_cvssv3*100)/(none_integrity_sh_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD BAJO \n")
print("             - EL "+str(float(((none_integrity_mediumavailability_sh_cvssv3*100)/(none_integrity_sh_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD MEDIO \n")
print("             - EL "+str(float(((none_integrity_noneavailability_sh_cvssv3*100)/(none_integrity_sh_cvssv3))))+" % DE LAS VULNERABILIDADES NO EXISTE AFECTACION/IMPACTO A LA DISPONIBILIDAD DEL SISTEMA \n")



print("*************************************************************************************************************************")


print("\n")
print(" - EN EL  "+str(float(((high_availability_sh_cvssv3*100)/len(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"]))))+" % DE LAS VULNERABILIDADES, DONDE EL IMPACTO DE DISPONIBILIDAD ES ALTO \n")
print("      - LOS PORCENTAJES DE IMPACTO DE CONFIDENCIALIDAD SON LOS SIGUIENTES : \n")
print("             - EL "+str(float(((high_availability_highconfidentiality_sh_cvssv3*100)/(high_availability_sh_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD ALTO \n")
print("             - EL "+str(float(((high_availability_lowconfidentiality_sh_cvssv3*100)/(high_availability_sh_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD BAJO \n")
print("             - EL "+str(float(((high_availability_mediumconfidentiality_sh_cvssv3*100)/(high_availability_sh_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD MEDIO \n")
print("             - EL "+str(float(((high_availability_noneconfidentiality_sh_cvssv3*100)/(high_availability_sh_cvssv3))))+" % DE LAS VULNERABILIDADES NO EXISTE AFECTACION/IMPACTO A LA CONFIDENCIALIDAD DEL SISTEMA \n")
print("\n")
print("      - LOS PORCENTAJES DE IMPACTO DE INTEGRIDAD SON LOS SIGUIENTES : \n")
print("             - EL "+str(float(((high_availability_highintegrity_sh_cvssv3*100)/(high_availability_sh_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD ALTO \n")
print("             - EL "+str(float(((high_availability_lowintegrity_sh_cvssv3*100)/(high_availability_sh_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD BAJO \n")
print("             - EL "+str(float(((high_availability_mediumintegrity_sh_cvssv3*100)/(high_availability_sh_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD MEDIO \n")
print("             - EL "+str(float(((high_availability_noneintegrity_sh_cvssv3*100)/(high_availability_sh_cvssv3))))+" % DE LAS VULNERABILIDADES NO EXISTE AFECTACION/IMPACTO A LA INTEGRIDAD DEL SISTEMA \n")


print("\n")
print(" - EN EL  "+str(float(((low_availability_sh_cvssv3*100)/len(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"]))))+" % DE LAS VULNERABILIDADES, DONDE EL IMPACTO DE DISPONIBILIDAD ES BAJO \n")
print("      - LOS PORCENTAJES DE IMPACTO DE CONFIDENCIALIDAD SON LOS SIGUIENTES : \n")
print("             - EL "+str(float(((low_availability_highconfidentiality_sh_cvssv3*100)/(low_availability_sh_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD ALTO \n")
print("             - EL "+str(float(((low_availability_lowconfidentiality_sh_cvssv3*100)/(low_availability_sh_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD BAJO \n")
print("             - EL "+str(float(((low_availability_mediumconfidentiality_sh_cvssv3*100)/(low_availability_sh_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD MEDIO \n")
print("             - EL "+str(float(((low_availability_noneconfidentiality_sh_cvssv3*100)/(low_availability_sh_cvssv3))))+" % DE LAS VULNERABILIDADES NO EXISTE AFECTACION/IMPACTO A LA CONFIDENCIALIDAD DEL SISTEMA \n")
print("\n")
print("      - LOS PORCENTAJES DE IMPACTO DE INTEGRIDAD SON LOS SIGUIENTES : \n")
print("             - EL "+str(float(((low_availability_highintegrity_sh_cvssv3*100)/(low_availability_sh_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD ALTO \n")
print("             - EL "+str(float(((low_availability_lowintegrity_sh_cvssv3*100)/(low_availability_sh_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD BAJO \n")
print("             - EL "+str(float(((low_availability_mediumintegrity_sh_cvssv3*100)/(low_availability_sh_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD MEDIO \n")
print("             - EL "+str(float(((low_availability_noneintegrity_sh_cvssv3*100)/(low_availability_sh_cvssv3))))+" % DE LAS VULNERABILIDADES NO EXISTE AFECTACION/IMPACTO A LA INTEGRIDAD DEL SISTEMA \n")


if(medium_availability_sh_cvssv3>0):
    print("\n")
    print(" - EN EL  "+str(float(((medium_availability_sh_cvssv3*100)/len(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"]))))+" % DE LAS VULNERABILIDADES, DONDE EL IMPACTO DE DISPONIBILIDAD ES MEDIO \n")
    print("      - LOS PORCENTAJES DE IMPACTO DE CONFIDENCIALIDAD SON LOS SIGUIENTES : \n")
    print("             - EL "+str(float(((medium_availability_highconfidentiality_sh_cvssv3*100)/(medium_availability_sh_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD ALTO \n")
    print("             - EL "+str(float(((medium_availability_lowconfidentiality_sh_cvssv3*100)/(medium_availability_sh_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD BAJO \n")
    print("             - EL "+str(float(((medium_availability_mediumconfidentiality_sh_cvssv3*100)/(medium_availability_sh_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD MEDIO \n")
    print("             - EL "+str(float(((medium_availability_noneconfidentiality_sh_cvssv3*100)/(medium_availability_sh_cvssv3))))+" % DE LAS VULNERABILIDADES NO EXISTE AFECTACION/IMPACTO A LA CONFIDENCIALIDAD DEL SISTEMA \n")
    print("\n")
    print("      - LOS PORCENTAJES DE IMPACTO DE INTEGRIDAD SON LOS SIGUIENTES : \n")
    print("             - EL "+str(float(((medium_availability_highintegrity_sh_cvssv3*100)/(medium_availability_sh_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD ALTO \n")
    print("             - EL "+str(float(((medium_availability_lowintegrity_sh_cvssv3*100)/(medium_availability_sh_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD BAJO \n")
    print("             - EL "+str(float(((medium_availability_mediumintegrity_sh_cvssv3*100)/(medium_availability_sh_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD MEDIO \n")
    print("             - EL "+str(float(((medium_availability_noneintegrity_sh_cvssv3*100)/(medium_availability_sh_cvssv3))))+" % DE LAS VULNERABILIDADES NO EXISTE AFECTACION/IMPACTO A LA INTEGRIDAD DEL SISTEMA \n")



print("\n")
print(" - EN EL  "+str(float(((none_availability_sh_cvssv3*100)/len(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"]))))+" % DE LAS VULNERABILIDADES, DONDE NO EXISTE AFECTACION/IMPACTO A LA DISPONIBILIDAD DEL SISTEMA \n")
print("      - LOS PORCENTAJES DE IMPACTO DE CONFIDENCIALIDAD SON LOS SIGUIENTES : \n")
print("             - EL "+str(float(((none_availability_highconfidentiality_sh_cvssv3*100)/(none_availability_sh_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD ALTO \n")
print("             - EL "+str(float(((none_availability_lowconfidentiality_sh_cvssv3*100)/(none_availability_sh_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD BAJO \n")
print("             - EL "+str(float(((none_availability_mediumconfidentiality_sh_cvssv3*100)/(none_availability_sh_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD MEDIO \n")
print("             - EL "+str(float(((none_availability_noneconfidentiality_sh_cvssv3*100)/(none_availability_sh_cvssv3))))+" % DE LAS VULNERABILIDADES NO EXISTE AFECTACION/IMPACTO A LA CONFIDENCIALIDAD DEL SISTEMA \n")
print("\n")
print("      - LOS PORCENTAJES DE IMPACTO DE INTEGRIDAD SON LOS SIGUIENTES : \n")
print("             - EL "+str(float(((none_availability_highintegrity_sh_cvssv3*100)/(none_availability_sh_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD ALTO \n")
print("             - EL "+str(float(((none_availability_lowintegrity_sh_cvssv3*100)/(none_availability_sh_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD BAJO \n")
print("             - EL "+str(float(((none_availability_mediumintegrity_sh_cvssv3*100)/(none_availability_sh_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD MEDIO \n")
print("             - EL "+str(float(((none_availability_noneintegrity_sh_cvssv3*100)/(none_availability_sh_cvssv3))))+" % DE LAS VULNERABILIDADES NO EXISTE AFECTACION/IMPACTO A LA INTEGRIDAD DEL SISTEMA \n")
















































print("_________________________________________________________________________________________________________________________________________________________________")



print("**************************ESTADÍSTICAS IMPACTO DE CONFIDENCIALIDAD/INTEGRIDAD/DISPONIBILIDAD CVSSV3 CVE IOT Y SMART HOME CONJUNTAMENTE********************************")
print("\n")
print(" DE UN TOTAL DE "+str(high_confidentiality_sh_cvssv3+medium_confidentiality_sh_cvssv3+low_confidentiality_sh_cvssv3+none_confidentiality_sh_cvssv3+high_confidentiality_iot_cvssv3+medium_confidentiality_iot_cvssv3+low_confidentiality_iot_cvssv3+none_confidentiality_iot_cvssv3)+" VULNERABILIDADES, LAS ESTADÍSTICAS DE IMPACTO DE CONFIDENCIALIDAD/INTEGRIDAD/DISPONIBILIDAD SON LAS SIGUIENTES: \n")
print("\n")
print(" - DE UN TOTAL DE "+str(high_confidentiality_sh_cvssv3+high_confidentiality_iot_cvssv3)+" VULNERABILIDADES DONDE EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
print("      - LAS ESTADÍSTICAS DE IMPACTO DE INTEGRIDAD SON LAS SIGUIENTES : \n")
print("             - UN TOTAL DE "+str(high_confidentiality_highintegrity_sh_cvssv3+high_confidentiality_highintegrity_iot_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD ALTO \n")
print("             - UN TOTAL DE "+str(high_confidentiality_lowintegrity_sh_cvssv3+high_confidentiality_lowintegrity_iot_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD BAJO \n")
print("             - UN TOTAL DE "+str(high_confidentiality_mediumintegrity_sh_cvssv3+high_confidentiality_mediumintegrity_iot_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD MEDIO \n")
print("             - UN TOTAL DE "+str(high_confidentiality_noneintegrity_sh_cvssv3+high_confidentiality_noneintegrity_iot_cvssv3)+" VULNERABILIDADES NO EXISTE AFECTACION/IMPACTO A LA INTEGRIDAD DEL SISTEMA: \n")
print("\n")
print("      - LAS ESTADÍSTICAS DE IMPACTO DE DISPONIBILIDAD SON LAS SIGUIENTES : \n")
print("             - UN TOTAL DE "+str(high_confidentiality_highavailability_sh_cvssv3+high_confidentiality_highavailability_iot_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD ALTO \n")
print("             - UN TOTAL DE "+str(high_confidentiality_lowavailability_sh_cvssv3+high_confidentiality_lowavailability_iot_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD BAJO \n")
print("             - UN TOTAL DE "+str(high_confidentiality_mediumavailability_sh_cvssv3+high_confidentiality_mediumavailability_iot_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD MEDIO \n")
print("             - UN TOTAL DE "+str(high_confidentiality_noneavailability_sh_cvssv3+high_confidentiality_noneavailability_iot_cvssv3)+" VULNERABILIDADES NO EXISTE AFECTACION/IMPACTO A LA DISPONIBILIDAD DEL SISTEMA: \n")


print("\n")
print(" - DE UN TOTAL DE "+str(low_confidentiality_sh_cvssv3+low_confidentiality_iot_cvssv3)+" VULNERABILIDADES DONDE EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
print("      - LAS ESTADÍSTICAS DE IMPACTO DE INTEGRIDAD SON LAS SIGUIENTES : \n")
print("             - UN TOTAL DE "+str(low_confidentiality_highintegrity_sh_cvssv3+low_confidentiality_highintegrity_iot_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD ALTO \n")
print("             - UN TOTAL DE "+str(low_confidentiality_lowintegrity_sh_cvssv3+low_confidentiality_lowintegrity_iot_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD BAJO \n")
print("             - UN TOTAL DE "+str(low_confidentiality_mediumintegrity_sh_cvssv3+low_confidentiality_mediumintegrity_iot_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD MEDIO \n")
print("             - UN TOTAL DE "+str(low_confidentiality_noneintegrity_sh_cvssv3+low_confidentiality_noneintegrity_iot_cvssv3)+" VULNERABILIDADES NO EXISTE AFECTACION/IMPACTO A LA INTEGRIDAD DEL SISTEMA: \n")
print("\n")
print("      - LAS ESTADÍSTICAS DE IMPACTO DE DISPONIBILIDAD SON LAS SIGUIENTES : \n")
print("             - UN TOTAL DE "+str(low_confidentiality_highavailability_sh_cvssv3+low_confidentiality_highavailability_iot_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD ALTO \n")
print("             - UN TOTAL DE "+str(low_confidentiality_lowavailability_sh_cvssv3+low_confidentiality_lowavailability_iot_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD BAJO \n")
print("             - UN TOTAL DE "+str(low_confidentiality_mediumavailability_sh_cvssv3+low_confidentiality_mediumavailability_iot_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD MEDIO \n")
print("             - UN TOTAL DE "+str(low_confidentiality_noneavailability_sh_cvssv3+low_confidentiality_noneavailability_iot_cvssv3)+" VULNERABILIDADES NO EXISTE AFECTACION/IMPACTO A LA DISPONIBILIDAD DEL SISTEMA: \n")


print("\n")
print(" - DE UN TOTAL DE "+str(medium_confidentiality_sh_cvssv3+medium_confidentiality_iot_cvssv3)+" VULNERABILIDADES DONDE EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO \n")
print("      - LAS ESTADÍSTICAS DE IMPACTO DE INTEGRIDAD SON LAS SIGUIENTES : \n")
print("             - UN TOTAL DE "+str(medium_confidentiality_highintegrity_sh_cvssv3+medium_confidentiality_highintegrity_iot_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD ALTO \n")
print("             - UN TOTAL DE "+str(medium_confidentiality_lowintegrity_sh_cvssv3+medium_confidentiality_lowintegrity_iot_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD BAJO \n")
print("             - UN TOTAL DE "+str(medium_confidentiality_mediumintegrity_sh_cvssv3+medium_confidentiality_mediumintegrity_iot_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD MEDIO \n")
print("             - UN TOTAL DE "+str(medium_confidentiality_noneintegrity_sh_cvssv3+medium_confidentiality_noneintegrity_iot_cvssv3)+" VULNERABILIDADES NO EXISTE AFECTACION/IMPACTO A LA INTEGRIDAD DEL SISTEMA: \n")
print("\n")
print("      - LAS ESTADÍSTICAS DE IMPACTO DE DISPONIBILIDAD SON LAS SIGUIENTES : \n")
print("             - UN TOTAL DE "+str(medium_confidentiality_highavailability_sh_cvssv3+medium_confidentiality_highavailability_iot_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD ALTO \n")
print("             - UN TOTAL DE "+str(medium_confidentiality_lowavailability_sh_cvssv3+medium_confidentiality_lowavailability_iot_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD BAJO \n")
print("             - UN TOTAL DE "+str(medium_confidentiality_mediumavailability_sh_cvssv3+medium_confidentiality_mediumavailability_iot_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD MEDIO \n")
print("             - UN TOTAL DE "+str(medium_confidentiality_noneavailability_sh_cvssv3+medium_confidentiality_noneavailability_iot_cvssv3)+" VULNERABILIDADES NO EXISTE AFECTACION/IMPACTO A LA DISPONIBILIDAD DEL SISTEMA: \n")


print("\n")
print(" - DE UN TOTAL DE "+str(none_confidentiality_sh_cvssv3+none_confidentiality_iot_cvssv3)+" VULNERABILIDADES DONDE NO EXISTE AFECTACION/IMPACTO A LA CONFIDENCIALIDAD DEL SISTEMA \n")
print("      - LAS ESTADÍSTICAS DE IMPACTO DE INTEGRIDAD SON LAS SIGUIENTES : \n")
print("             - UN TOTAL DE "+str(none_confidentiality_highintegrity_sh_cvssv3+none_confidentiality_highintegrity_iot_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD ALTO \n")
print("             - UN TOTAL DE "+str(none_confidentiality_lowintegrity_sh_cvssv3+none_confidentiality_lowintegrity_iot_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD BAJO \n")
print("             - UN TOTAL DE "+str(none_confidentiality_mediumintegrity_sh_cvssv3+none_confidentiality_mediumintegrity_iot_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD MEDIO \n")
print("             - UN TOTAL DE "+str(none_confidentiality_noneintegrity_sh_cvssv3+none_confidentiality_noneintegrity_iot_cvssv3)+" VULNERABILIDADES NO EXISTE AFECTACION/IMPACTO A LA INTEGRIDAD DEL SISTEMA: \n")
print("\n")
print("      - LAS ESTADÍSTICAS DE IMPACTO DE DISPONIBILIDAD SON LAS SIGUIENTES : \n")
print("             - UN TOTAL DE "+str(none_confidentiality_highavailability_sh_cvssv3+none_confidentiality_highavailability_iot_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD ALTO \n")
print("             - UN TOTAL DE "+str(none_confidentiality_lowavailability_sh_cvssv3+none_confidentiality_lowavailability_iot_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD BAJO \n")
print("             - UN TOTAL DE "+str(none_confidentiality_mediumavailability_sh_cvssv3+none_confidentiality_mediumavailability_iot_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD MEDIO \n")
print("             - UN TOTAL DE "+str(none_confidentiality_noneavailability_sh_cvssv3+none_confidentiality_noneavailability_iot_cvssv3)+" VULNERABILIDADES NO EXISTE AFECTACION/IMPACTO A LA DISPONIBILIDAD DEL SISTEMA: \n")




print("*************************************************************************************************************************")




print("\n")
print(" - DE UN TOTAL DE "+str(high_integrity_sh_cvssv3+high_integrity_iot_cvssv3)+" VULNERABILIDADES DONDE EL IMPACTO DE INTEGRIDAD ES ALTO \n")
print("      - LAS ESTADÍSTICAS DE IMPACTO DE CONFIDENCIALIDAD SON LAS SIGUIENTES : \n")
print("             - UN TOTAL DE "+str(high_integrity_highconfidentiality_sh_cvssv3+high_integrity_highconfidentiality_iot_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD ALTO \n")
print("             - UN TOTAL DE "+str(high_integrity_lowconfidentiality_sh_cvssv3+high_integrity_lowconfidentiality_iot_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD BAJO \n")
print("             - UN TOTAL DE "+str(high_integrity_mediumconfidentiality_sh_cvssv3+high_integrity_mediumconfidentiality_iot_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD MEDIO \n")
print("             - UN TOTAL DE "+str(high_integrity_noneconfidentiality_sh_cvssv3+high_integrity_noneconfidentiality_iot_cvssv3)+" VULNERABILIDADES NO EXISTE AFECTACION/IMPACTO A LA CONFIDENCIALIDAD DEL SISTEMA: \n")
print("\n")
print("      - LAS ESTADÍSTICAS DE IMPACTO DE DISPONIBILIDAD SON LAS SIGUIENTES : \n")
print("             - UN TOTAL DE "+str(high_integrity_highavailability_sh_cvssv3+high_integrity_highavailability_iot_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD ALTO \n")
print("             - UN TOTAL DE "+str(high_integrity_lowavailability_sh_cvssv3+high_integrity_lowavailability_iot_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD BAJO \n")
print("             - UN TOTAL DE "+str(high_integrity_mediumavailability_sh_cvssv3+high_integrity_mediumavailability_iot_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD MEDIO \n")
print("             - UN TOTAL DE "+str(high_integrity_noneavailability_sh_cvssv3+high_integrity_noneavailability_iot_cvssv3)+" VULNERABILIDADES NO EXISTE AFECTACION/IMPACTO A LA DISPONIBILIDAD DEL SISTEMA: \n")



print("\n")
print(" - DE UN TOTAL DE "+str(low_integrity_sh_cvssv3+low_integrity_iot_cvssv3)+" VULNERABILIDADES DONDE EL IMPACTO DE INTEGRIDAD ES BAJO \n")
print("      - LAS ESTADÍSTICAS DE IMPACTO DE CONFIDENCIALIDAD SON LAS SIGUIENTES : \n")
print("             - UN TOTAL DE "+str(low_integrity_highconfidentiality_sh_cvssv3+low_integrity_highconfidentiality_iot_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD ALTO \n")
print("             - UN TOTAL DE "+str(low_integrity_lowconfidentiality_sh_cvssv3+low_integrity_lowconfidentiality_iot_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD BAJO \n")
print("             - UN TOTAL DE "+str(low_integrity_mediumconfidentiality_sh_cvssv3+low_integrity_mediumconfidentiality_iot_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD MEDIO \n")
print("             - UN TOTAL DE "+str(low_integrity_noneconfidentiality_sh_cvssv3+low_integrity_noneconfidentiality_iot_cvssv3)+" VULNERABILIDADES NO EXISTE AFECTACION/IMPACTO A LA CONFIDENCIALIDAD DEL SISTEMA: \n")
print("\n")
print("      - LAS ESTADÍSTICAS DE IMPACTO DE DISPONIBILIDAD SON LAS SIGUIENTES : \n")
print("             - UN TOTAL DE "+str(low_integrity_highavailability_sh_cvssv3+low_integrity_highavailability_iot_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD ALTO \n")
print("             - UN TOTAL DE "+str(low_integrity_lowavailability_sh_cvssv3+low_integrity_lowavailability_iot_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD BAJO \n")
print("             - UN TOTAL DE "+str(low_integrity_mediumavailability_sh_cvssv3+low_integrity_mediumavailability_iot_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD MEDIO \n")
print("             - UN TOTAL DE "+str(low_integrity_noneavailability_sh_cvssv3+low_integrity_noneavailability_iot_cvssv3)+" VULNERABILIDADES NO EXISTE AFECTACION/IMPACTO A LA DISPONIBILIDAD DEL SISTEMA: \n")



print("\n")
print(" - DE UN TOTAL DE "+str(medium_integrity_sh_cvssv3+medium_integrity_iot_cvssv3)+" VULNERABILIDADES DONDE EL IMPACTO DE INTEGRIDAD ES MEDIO \n")
print("      - LAS ESTADÍSTICAS DE IMPACTO DE CONFIDENCIALIDAD SON LAS SIGUIENTES : \n")
print("             - UN TOTAL DE "+str(medium_integrity_highconfidentiality_sh_cvssv3+medium_integrity_highconfidentiality_iot_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD ALTO \n")
print("             - UN TOTAL DE "+str(medium_integrity_lowconfidentiality_sh_cvssv3+medium_integrity_lowconfidentiality_iot_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD BAJO \n")
print("             - UN TOTAL DE "+str(medium_integrity_mediumconfidentiality_sh_cvssv3+medium_integrity_mediumconfidentiality_iot_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD MEDIO \n")
print("             - UN TOTAL DE "+str(medium_integrity_noneconfidentiality_sh_cvssv3+medium_integrity_noneconfidentiality_iot_cvssv3)+" VULNERABILIDADES NO EXISTE AFECTACION/IMPACTO A LA CONFIDENCIALIDAD DEL SISTEMA: \n")
print("\n")
print("      - LAS ESTADÍSTICAS DE IMPACTO DE DISPONIBILIDAD SON LAS SIGUIENTES : \n")
print("             - UN TOTAL DE "+str(medium_integrity_highavailability_sh_cvssv3+medium_integrity_highavailability_iot_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD ALTO \n")
print("             - UN TOTAL DE "+str(medium_integrity_lowavailability_sh_cvssv3+medium_integrity_lowavailability_iot_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD BAJO \n")
print("             - UN TOTAL DE "+str(medium_integrity_mediumavailability_sh_cvssv3+medium_integrity_mediumavailability_iot_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD MEDIO \n")
print("             - UN TOTAL DE "+str(medium_integrity_noneavailability_sh_cvssv3+medium_integrity_noneavailability_iot_cvssv3)+" VULNERABILIDADES NO EXISTE AFECTACION/IMPACTO A LA DISPONIBILIDAD DEL SISTEMA: \n")



print("\n")
print(" - DE UN TOTAL DE "+str(none_integrity_sh_cvssv3+none_integrity_iot_cvssv3)+" VULNERABILIDADES DONDE NO EXISTE AFECTACION/IMPACTO A LA INTEGRIDAD DEL SISTEMA \n")
print("      - LAS ESTADÍSTICAS DE IMPACTO DE CONFIDENCIALIDAD SON LAS SIGUIENTES : \n")
print("             - UN TOTAL DE "+str(none_integrity_highconfidentiality_sh_cvssv3+none_integrity_highconfidentiality_iot_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD ALTO \n")
print("             - UN TOTAL DE "+str(none_integrity_lowconfidentiality_sh_cvssv3+none_integrity_lowconfidentiality_iot_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD BAJO \n")
print("             - UN TOTAL DE "+str(none_integrity_mediumconfidentiality_sh_cvssv3+none_integrity_mediumconfidentiality_iot_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD MEDIO \n")
print("             - UN TOTAL DE "+str(none_integrity_noneconfidentiality_sh_cvssv3+none_integrity_noneconfidentiality_iot_cvssv3)+" VULNERABILIDADES NO EXISTE AFECTACION/IMPACTO A LA CONFIDENCIALIDAD DEL SISTEMA: \n")
print("\n")
print("      - LAS ESTADÍSTICAS DE IMPACTO DE DISPONIBILIDAD SON LAS SIGUIENTES : \n")
print("             - UN TOTAL DE "+str(none_integrity_highavailability_sh_cvssv3+none_integrity_highavailability_iot_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD ALTO \n")
print("             - UN TOTAL DE "+str(none_integrity_lowavailability_sh_cvssv3+none_integrity_lowavailability_iot_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD BAJO \n")
print("             - UN TOTAL DE "+str(none_integrity_mediumavailability_sh_cvssv3+none_integrity_mediumavailability_iot_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD MEDIO \n")
print("             - UN TOTAL DE "+str(none_integrity_noneavailability_sh_cvssv3+none_integrity_noneavailability_iot_cvssv3)+" VULNERABILIDADES NO EXISTE AFECTACION/IMPACTO A LA DISPONIBILIDAD DEL SISTEMA: \n")



print("*************************************************************************************************************************")


print("\n")
print(" - DE UN TOTAL DE "+str(high_availability_sh_cvssv3+high_availability_iot_cvssv3)+" VULNERABILIDADES DONDE EL IMPACTO DE DISPONIBILIDAD ES ALTO \n")
print("      - LAS ESTADÍSTICAS DE IMPACTO DE CONFIDENCIALIDAD SON LAS SIGUIENTES : \n")
print("             - UN TOTAL DE "+str(high_availability_highconfidentiality_sh_cvssv3+high_availability_highconfidentiality_iot_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD ALTO \n")
print("             - UN TOTAL DE "+str(high_availability_lowconfidentiality_sh_cvssv3+high_availability_lowconfidentiality_iot_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD BAJO \n")
print("             - UN TOTAL DE "+str(high_availability_mediumconfidentiality_sh_cvssv3+high_availability_mediumconfidentiality_iot_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD MEDIO \n")
print("             - UN TOTAL DE "+str(high_availability_noneconfidentiality_sh_cvssv3+high_availability_noneconfidentiality_iot_cvssv3)+" VULNERABILIDADES NO EXISTE AFECTACION/IMPACTO A LA CONFIDENCIALIDAD DEL SISTEMA: \n")
print("\n")
print("      - LAS ESTADÍSTICAS DE IMPACTO DE INTEGRIDAD SON LAS SIGUIENTES : \n")
print("             - UN TOTAL DE "+str(high_availability_highintegrity_sh_cvssv3+high_availability_highintegrity_iot_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD ALTO \n")
print("             - UN TOTAL DE "+str(high_availability_lowintegrity_sh_cvssv3+high_availability_lowintegrity_iot_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD BAJO \n")
print("             - UN TOTAL DE "+str(high_availability_mediumintegrity_sh_cvssv3+high_availability_mediumintegrity_iot_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD MEDIO \n")
print("             - UN TOTAL DE "+str(high_availability_noneintegrity_sh_cvssv3+high_availability_noneintegrity_iot_cvssv3)+" VULNERABILIDADES NO EXISTE AFECTACION/IMPACTO A LA INTEGRIDAD DEL SISTEMA: \n")




print("\n")
print(" - DE UN TOTAL DE "+str(low_availability_sh_cvssv3+low_availability_iot_cvssv3)+" VULNERABILIDADES DONDE EL IMPACTO DE DISPONIBILIDAD ES BAJO \n")
print("      - LAS ESTADÍSTICAS DE IMPACTO DE CONFIDENCIALIDAD SON LAS SIGUIENTES : \n")
print("             - UN TOTAL DE "+str(low_availability_highconfidentiality_sh_cvssv3+low_availability_highconfidentiality_iot_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD ALTO \n")
print("             - UN TOTAL DE "+str(low_availability_lowconfidentiality_sh_cvssv3+low_availability_lowconfidentiality_iot_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD BAJO \n")
print("             - UN TOTAL DE "+str(low_availability_mediumconfidentiality_sh_cvssv3+low_availability_mediumconfidentiality_iot_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD MEDIO \n")
print("             - UN TOTAL DE "+str(low_availability_noneconfidentiality_sh_cvssv3+low_availability_noneconfidentiality_iot_cvssv3)+" VULNERABILIDADES NO EXISTE AFECTACION/IMPACTO A LA CONFIDENCIALIDAD DEL SISTEMA: \n")
print("\n")
print("      - LAS ESTADÍSTICAS DE IMPACTO DE INTEGRIDAD SON LAS SIGUIENTES : \n")
print("             - UN TOTAL DE "+str(low_availability_highintegrity_sh_cvssv3+low_availability_highintegrity_iot_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD ALTO \n")
print("             - UN TOTAL DE "+str(low_availability_lowintegrity_sh_cvssv3+low_availability_lowintegrity_iot_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD BAJO \n")
print("             - UN TOTAL DE "+str(low_availability_mediumintegrity_sh_cvssv3+low_availability_mediumintegrity_iot_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD MEDIO \n")
print("             - UN TOTAL DE "+str(low_availability_noneintegrity_sh_cvssv3+low_availability_noneintegrity_iot_cvssv3)+" VULNERABILIDADES NO EXISTE AFECTACION/IMPACTO A LA INTEGRIDAD DEL SISTEMA: \n")




print("\n")
print(" - DE UN TOTAL DE "+str(medium_availability_sh_cvssv3+medium_availability_iot_cvssv3)+" VULNERABILIDADES DONDE EL IMPACTO DE DISPONIBILIDAD ES MEDIO \n")
print("      - LAS ESTADÍSTICAS DE IMPACTO DE CONFIDENCIALIDAD SON LAS SIGUIENTES : \n")
print("             - UN TOTAL DE "+str(medium_availability_highconfidentiality_sh_cvssv3+medium_availability_highconfidentiality_iot_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD ALTO \n")
print("             - UN TOTAL DE "+str(medium_availability_lowconfidentiality_sh_cvssv3+medium_availability_lowconfidentiality_iot_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD BAJO \n")
print("             - UN TOTAL DE "+str(medium_availability_mediumconfidentiality_sh_cvssv3+medium_availability_mediumconfidentiality_iot_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD MEDIO \n")
print("             - UN TOTAL DE "+str(medium_availability_noneconfidentiality_sh_cvssv3+medium_availability_noneconfidentiality_iot_cvssv3)+" VULNERABILIDADES NO EXISTE AFECTACION/IMPACTO A LA CONFIDENCIALIDAD DEL SISTEMA: \n")
print("\n")
print("      - LAS ESTADÍSTICAS DE IMPACTO DE INTEGRIDAD SON LAS SIGUIENTES : \n")
print("             - UN TOTAL DE "+str(medium_availability_highintegrity_sh_cvssv3+medium_availability_highintegrity_iot_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD ALTO \n")
print("             - UN TOTAL DE "+str(medium_availability_lowintegrity_sh_cvssv3+medium_availability_lowintegrity_iot_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD BAJO \n")
print("             - UN TOTAL DE "+str(medium_availability_mediumintegrity_sh_cvssv3+medium_availability_mediumintegrity_iot_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD MEDIO \n")
print("             - UN TOTAL DE "+str(medium_availability_noneintegrity_sh_cvssv3+medium_availability_noneintegrity_iot_cvssv3)+" VULNERABILIDADES NO EXISTE AFECTACION/IMPACTO A LA INTEGRIDAD DEL SISTEMA: \n")


print("\n")
print(" - DE UN TOTAL DE "+str(none_availability_sh_cvssv3+none_availability_iot_cvssv3)+" VULNERABILIDADES DONDE NO EXISTE AFECTACION/IMPACTO A LA DISPONIBILIDAD DEL SISTEMA \n")
print("      - LAS ESTADÍSTICAS DE IMPACTO DE CONFIDENCIALIDAD SON LAS SIGUIENTES : \n")
print("             - UN TOTAL DE "+str(none_availability_highconfidentiality_sh_cvssv3+none_availability_highconfidentiality_iot_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD ALTO \n")
print("             - UN TOTAL DE "+str(none_availability_lowconfidentiality_sh_cvssv3+none_availability_lowconfidentiality_iot_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD BAJO \n")
print("             - UN TOTAL DE "+str(none_availability_mediumconfidentiality_sh_cvssv3+none_availability_mediumconfidentiality_iot_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD MEDIO \n")
print("             - UN TOTAL DE "+str(none_availability_noneconfidentiality_sh_cvssv3+none_availability_noneconfidentiality_iot_cvssv3)+" VULNERABILIDADES NO EXISTE AFECTACION/IMPACTO A LA CONFIDENCIALIDAD DEL SISTEMA: \n")
print("\n")
print("      - LAS ESTADÍSTICAS DE IMPACTO DE INTEGRIDAD SON LAS SIGUIENTES : \n")
print("             - UN TOTAL DE "+str(none_availability_highintegrity_sh_cvssv3+none_availability_highintegrity_iot_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD ALTO \n")
print("             - UN TOTAL DE "+str(none_availability_lowintegrity_sh_cvssv3+none_availability_lowintegrity_iot_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD BAJO \n")
print("             - UN TOTAL DE "+str(none_availability_mediumintegrity_sh_cvssv3+none_availability_mediumintegrity_iot_cvssv3)+" VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD MEDIO \n")
print("             - UN TOTAL DE "+str(none_availability_noneintegrity_sh_cvssv3+none_availability_noneintegrity_iot_cvssv3)+" VULNERABILIDADES NO EXISTE AFECTACION/IMPACTO A LA INTEGRIDAD DEL SISTEMA: \n")














print("_________________________________________________________________________________________________________________________________________________________________")




total_vulnerabilities_cvssv3=len(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"])+len(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"])


print("************************** PORCENTAJE IMPACTO DE CONFIDENCIALIDAD/INTEGRIDAD/DISPONIBILIDAD CVSSV3 CVE IOT Y SMART HOME CONJUNTAS********************************")
print("\n")
print(" DE UN TOTAL DE "+str(total_vulnerabilities_cvssv3)+" VULNERABILIDADES, LOS PORCENTAJES DE IMPACTO DE CONFIDENCIALIDAD/INTEGRIDAD/DISPONIBILIDAD SON LOS SIGUIENTES: \n")
print("\n")

print(" - EN EL  "+str(float((((high_confidentiality_iot_cvssv3+high_confidentiality_sh_cvssv3)*100)/(len(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"])+len(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"])))))+" % DE LAS VULNERABILIDADES, DONDE EL IMPACTO DE CONFIDENCIALIDAD ES ALTO \n")
print("      - LOS PORCENTAJES DE IMPACTO DE INTEGRIDAD SON LOS SIGUIENTES : \n")
print("             - EL "+str(float((((high_confidentiality_highintegrity_sh_cvssv3+high_confidentiality_highintegrity_iot_cvssv3)*100)/(high_confidentiality_sh_cvssv3+high_confidentiality_iot_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD ALTO \n")
print("             - EL "+str(float((((high_confidentiality_lowintegrity_sh_cvssv3+high_confidentiality_lowintegrity_iot_cvssv3)*100)/(high_confidentiality_sh_cvssv3+high_confidentiality_iot_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD BAJO \n")
print("             - EL "+str(float((((high_confidentiality_mediumintegrity_sh_cvssv3+high_confidentiality_mediumintegrity_iot_cvssv3)*100)/(high_confidentiality_sh_cvssv3+high_confidentiality_iot_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD MEDIO \n")
print("             - EL "+str(float((((high_confidentiality_noneintegrity_sh_cvssv3+high_confidentiality_noneintegrity_iot_cvssv3)*100)/(high_confidentiality_sh_cvssv3+high_confidentiality_iot_cvssv3))))+" % DE LAS VULNERABILIDADES NO EXISTE AFECTACION/IMPACTO A LA INTEGRIDAD DEL SISTEMA \n")
print("\n")
print("      - LOS PORCENTAJES DE IMPACTO DE DISPONIBILIDAD SON LOS SIGUIENTES : \n")
print("             - EL "+str(float((((high_confidentiality_highavailability_sh_cvssv3+high_confidentiality_highavailability_iot_cvssv3)*100)/(high_confidentiality_sh_cvssv3+high_confidentiality_iot_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD ALTO \n")
print("             - EL "+str(float((((high_confidentiality_lowavailability_sh_cvssv3+high_confidentiality_lowavailability_iot_cvssv3)*100)/(high_confidentiality_sh_cvssv3+high_confidentiality_iot_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD BAJO \n")
print("             - EL "+str(float((((high_confidentiality_mediumavailability_sh_cvssv3+high_confidentiality_mediumavailability_iot_cvssv3)*100)/(high_confidentiality_sh_cvssv3+high_confidentiality_iot_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD MEDIO \n")
print("             - EL "+str(float((((high_confidentiality_noneavailability_sh_cvssv3+high_confidentiality_noneavailability_iot_cvssv3)*100)/(high_confidentiality_sh_cvssv3+high_confidentiality_iot_cvssv3))))+" % DE LAS VULNERABILIDADES NO EXISTE AFECTACION/IMPACTO A LA DISPONIBILIDAD DEL SISTEMA \n")

print("\n")
print(" - EN EL  "+str(float((((low_confidentiality_iot_cvssv3+low_confidentiality_sh_cvssv3)*100)/(len(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"])+len(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"])))))+" % DE LAS VULNERABILIDADES, DONDE EL IMPACTO DE CONFIDENCIALIDAD ES BAJO \n")
print("      - LOS PORCENTAJES DE IMPACTO DE INTEGRIDAD SON LOS SIGUIENTES : \n")
print("             - EL "+str(float((((low_confidentiality_highintegrity_sh_cvssv3+low_confidentiality_highintegrity_iot_cvssv3)*100)/(low_confidentiality_sh_cvssv3+low_confidentiality_iot_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD ALTO \n")
print("             - EL "+str(float((((low_confidentiality_lowintegrity_sh_cvssv3+low_confidentiality_lowintegrity_iot_cvssv3)*100)/(low_confidentiality_sh_cvssv3+low_confidentiality_iot_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD BAJO \n")
print("             - EL "+str(float((((low_confidentiality_mediumintegrity_sh_cvssv3+low_confidentiality_mediumintegrity_iot_cvssv3)*100)/(low_confidentiality_sh_cvssv3+low_confidentiality_iot_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD MEDIO \n")
print("             - EL "+str(float((((low_confidentiality_noneintegrity_sh_cvssv3+low_confidentiality_noneintegrity_iot_cvssv3)*100)/(low_confidentiality_sh_cvssv3+low_confidentiality_iot_cvssv3))))+" % DE LAS VULNERABILIDADES NO EXISTE AFECTACION/IMPACTO A LA INTEGRIDAD DEL SISTEMA \n")
print("\n")
print("      - LOS PORCENTAJES DE IMPACTO DE DISPONIBILIDAD SON LOS SIGUIENTES : \n")
print("             - EL "+str(float((((low_confidentiality_highavailability_sh_cvssv3+low_confidentiality_highavailability_iot_cvssv3)*100)/(low_confidentiality_sh_cvssv3+low_confidentiality_iot_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD ALTO \n")
print("             - EL "+str(float((((low_confidentiality_lowavailability_sh_cvssv3+low_confidentiality_lowavailability_iot_cvssv3)*100)/(low_confidentiality_sh_cvssv3+low_confidentiality_iot_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD BAJO \n")
print("             - EL "+str(float((((low_confidentiality_mediumavailability_sh_cvssv3+low_confidentiality_mediumavailability_iot_cvssv3)*100)/(low_confidentiality_sh_cvssv3+low_confidentiality_iot_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD MEDIO \n")
print("             - EL "+str(float((((low_confidentiality_noneavailability_sh_cvssv3+low_confidentiality_noneavailability_iot_cvssv3)*100)/(low_confidentiality_sh_cvssv3+low_confidentiality_iot_cvssv3))))+" % DE LAS VULNERABILIDADES NO EXISTE AFECTACION/IMPACTO A LA DISPONIBILIDAD DEL SISTEMA \n")

if((medium_confidentiality_sh_cvssv3+medium_confidentiality_iot_cvssv3)>0):
    print("\n")
    print(" - EN EL  "+str(float((((medium_confidentiality_iot_cvssv3+medium_confidentiality_sh_cvssv3)*100)/(len(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"])+len(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"])))))+" % DE LAS VULNERABILIDADES, DONDE EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO \n")
    print("      - LOS PORCENTAJES DE IMPACTO DE INTEGRIDAD SON LOS SIGUIENTES : \n")
    print("             - EL "+str(float((((medium_confidentiality_highintegrity_sh_cvssv3+medium_confidentiality_highintegrity_iot_cvssv3)*100)/(medium_confidentiality_sh_cvssv3+medium_confidentiality_iot_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD ALTO \n")
    print("             - EL "+str(float((((medium_confidentiality_lowintegrity_sh_cvssv3+medium_confidentiality_lowintegrity_iot_cvssv3)*100)/(medium_confidentiality_sh_cvssv3+medium_confidentiality_iot_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD BAJO \n")
    print("             - EL "+str(float((((medium_confidentiality_mediumintegrity_sh_cvssv3+medium_confidentiality_mediumintegrity_iot_cvssv3)*100)/(medium_confidentiality_sh_cvssv3+medium_confidentiality_iot_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD MEDIO \n")
    print("             - EL "+str(float((((medium_confidentiality_noneintegrity_sh_cvssv3+medium_confidentiality_noneintegrity_iot_cvssv3)*100)/(medium_confidentiality_sh_cvssv3+medium_confidentiality_iot_cvssv3))))+" % DE LAS VULNERABILIDADES NO EXISTE AFECTACION/IMPACTO A LA INTEGRIDAD DEL SISTEMA \n")
    print("\n")
    print("      - LOS PORCENTAJES DE IMPACTO DE DISPONIBILIDAD SON LOS SIGUIENTES : \n")
    print("             - EL "+str(float((((medium_confidentiality_highavailability_sh_cvssv3+medium_confidentiality_highavailability_iot_cvssv3)*100)/(medium_confidentiality_sh_cvssv3+medium_confidentiality_iot_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD ALTO \n")
    print("             - EL "+str(float((((medium_confidentiality_lowavailability_sh_cvssv3+medium_confidentiality_lowavailability_iot_cvssv3)*100)/(medium_confidentiality_sh_cvssv3+medium_confidentiality_iot_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD BAJO \n")
    print("             - EL "+str(float((((medium_confidentiality_mediumavailability_sh_cvssv3+medium_confidentiality_mediumavailability_iot_cvssv3)*100)/(medium_confidentiality_sh_cvssv3+medium_confidentiality_iot_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD MEDIO \n")
    print("             - EL "+str(float((((medium_confidentiality_noneavailability_sh_cvssv3+medium_confidentiality_noneavailability_iot_cvssv3)*100)/(medium_confidentiality_sh_cvssv3+medium_confidentiality_iot_cvssv3))))+" % DE LAS VULNERABILIDADES NO EXISTE AFECTACION/IMPACTO A LA DISPONIBILIDAD DEL SISTEMA \n")



print("\n")
print(" - EN EL  "+str(float((((none_confidentiality_iot_cvssv3+none_confidentiality_sh_cvssv3)*100)/(len(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"])+len(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"])))))+" % DE LAS VULNERABILIDADES, DONDE NO EXISTE AFECTACION/IMPACTO A LA CONFIDENCIALIDAD DEL SISTEMA \n")
print("      - LOS PORCENTAJES DE IMPACTO DE INTEGRIDAD SON LOS SIGUIENTES : \n")
print("             - EL "+str(float((((none_confidentiality_highintegrity_sh_cvssv3+none_confidentiality_highintegrity_iot_cvssv3)*100)/(none_confidentiality_sh_cvssv3+none_confidentiality_iot_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD ALTO \n")
print("             - EL "+str(float((((none_confidentiality_lowintegrity_sh_cvssv3+none_confidentiality_lowintegrity_iot_cvssv3)*100)/(none_confidentiality_sh_cvssv3+none_confidentiality_iot_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD BAJO \n")
print("             - EL "+str(float((((none_confidentiality_mediumintegrity_sh_cvssv3+none_confidentiality_mediumintegrity_iot_cvssv3)*100)/(none_confidentiality_sh_cvssv3+none_confidentiality_iot_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD MEDIO \n")
print("             - EL "+str(float((((none_confidentiality_noneintegrity_sh_cvssv3+none_confidentiality_noneintegrity_iot_cvssv3)*100)/(none_confidentiality_sh_cvssv3+none_confidentiality_iot_cvssv3))))+" % DE LAS VULNERABILIDADES NO EXISTE AFECTACION/IMPACTO A LA INTEGRIDAD DEL SISTEMA \n")
print("\n")
print("      - LOS PORCENTAJES DE IMPACTO DE DISPONIBILIDAD SON LOS SIGUIENTES : \n")
print("             - EL "+str(float((((none_confidentiality_highavailability_sh_cvssv3+none_confidentiality_highavailability_iot_cvssv3)*100)/(none_confidentiality_sh_cvssv3+none_confidentiality_iot_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD ALTO \n")
print("             - EL "+str(float((((none_confidentiality_lowavailability_sh_cvssv3+none_confidentiality_lowavailability_iot_cvssv3)*100)/(none_confidentiality_sh_cvssv3+none_confidentiality_iot_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD BAJO \n")
print("             - EL "+str(float((((none_confidentiality_mediumavailability_sh_cvssv3+none_confidentiality_mediumavailability_iot_cvssv3)*100)/(none_confidentiality_sh_cvssv3+none_confidentiality_iot_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD MEDIO \n")
print("             - EL "+str(float((((none_confidentiality_noneavailability_sh_cvssv3+none_confidentiality_noneavailability_iot_cvssv3)*100)/(none_confidentiality_sh_cvssv3+none_confidentiality_iot_cvssv3))))+" % DE LAS VULNERABILIDADES NO EXISTE AFECTACION/IMPACTO A LA DISPONIBILIDAD DEL SISTEMA \n")

print("*************************************************************************************************************************")
print(" - EN EL  "+str(float((((high_integrity_sh_cvssv3+high_integrity_iot_cvssv3)*100)/(len(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"])+len(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"])))))+" % DE LAS VULNERABILIDADES, DONDE EL IMPACTO DE INTEGRIDAD ES ALTO \n")
print("      - LOS PORCENTAJES DE IMPACTO DE CONFIDENCIALIDAD SON LOS SIGUIENTES : \n")
print("             - EL "+str(float((((high_integrity_highconfidentiality_sh_cvssv3+high_integrity_highconfidentiality_iot_cvssv3)*100)/(high_integrity_sh_cvssv3+high_integrity_iot_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD ALTO \n")
print("             - EL "+str(float((((high_integrity_lowconfidentiality_sh_cvssv3+high_integrity_lowconfidentiality_iot_cvssv3)*100)/(high_integrity_sh_cvssv3+high_integrity_iot_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD BAJO \n")
print("             - EL "+str(float((((high_integrity_mediumconfidentiality_sh_cvssv3+high_integrity_mediumconfidentiality_iot_cvssv3)*100)/(high_integrity_sh_cvssv3+high_integrity_iot_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD MEDIO \n")
print("             - EL "+str(float((((high_integrity_noneconfidentiality_sh_cvssv3+high_integrity_noneconfidentiality_iot_cvssv3)*100)/(high_integrity_sh_cvssv3+high_integrity_iot_cvssv3))))+" % DE LAS VULNERABILIDADES NO EXISTE AFECTACION/IMPACTO A LA CONFIDENCIALIDAD DEL SISTEMA \n")
print("\n")
print("      - LOS PORCENTAJES DE IMPACTO DE DISPONIBILIDAD SON LOS SIGUIENTES : \n")
print("             - EL "+str(float((((high_integrity_highavailability_sh_cvssv3+high_integrity_highavailability_iot_cvssv3)*100)/(high_integrity_sh_cvssv3+high_integrity_iot_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD ALTO \n")
print("             - EL "+str(float((((high_integrity_lowavailability_sh_cvssv3+high_integrity_lowavailability_iot_cvssv3)*100)/(high_integrity_sh_cvssv3+high_integrity_iot_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD BAJO \n")
print("             - EL "+str(float((((high_integrity_mediumavailability_sh_cvssv3+high_integrity_mediumavailability_iot_cvssv3)*100)/(high_integrity_sh_cvssv3+high_integrity_iot_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD MEDIO \n")
print("             - EL "+str(float((((high_integrity_noneavailability_sh_cvssv3+high_integrity_noneavailability_iot_cvssv3)*100)/(high_integrity_sh_cvssv3+high_integrity_iot_cvssv3))))+" % DE LAS VULNERABILIDADES NO EXISTE AFECTACION/IMPACTO A LA DISPONIBILIDAD DEL SISTEMA \n")


print(" - EN EL  "+str(float((((low_integrity_sh_cvssv3+low_integrity_iot_cvssv3)*100)/(len(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"])+len(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"])))))+" % DE LAS VULNERABILIDADES, DONDE EL IMPACTO DE INTEGRIDAD ES BAJO \n")
print("      - LOS PORCENTAJES DE IMPACTO DE CONFIDENCIALIDAD SON LOS SIGUIENTES : \n")
print("             - EL "+str(float((((low_integrity_highconfidentiality_sh_cvssv3+low_integrity_highconfidentiality_iot_cvssv3)*100)/(low_integrity_sh_cvssv3+low_integrity_iot_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD ALTO \n")
print("             - EL "+str(float((((low_integrity_lowconfidentiality_sh_cvssv3+low_integrity_lowconfidentiality_iot_cvssv3)*100)/(low_integrity_sh_cvssv3+low_integrity_iot_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD BAJO \n")
print("             - EL "+str(float((((low_integrity_mediumconfidentiality_sh_cvssv3+low_integrity_mediumconfidentiality_iot_cvssv3)*100)/(low_integrity_sh_cvssv3+low_integrity_iot_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD MEDIO \n")
print("             - EL "+str(float((((low_integrity_noneconfidentiality_sh_cvssv3+low_integrity_noneconfidentiality_iot_cvssv3)*100)/(low_integrity_sh_cvssv3+low_integrity_iot_cvssv3))))+" % DE LAS VULNERABILIDADES NO EXISTE AFECTACION/IMPACTO A LA CONFIDENCIALIDAD DEL SISTEMA \n")
print("\n")
print("      - LOS PORCENTAJES DE IMPACTO DE DISPONIBILIDAD SON LOS SIGUIENTES : \n")
print("             - EL "+str(float((((low_integrity_highavailability_sh_cvssv3+low_integrity_highavailability_iot_cvssv3)*100)/(low_integrity_sh_cvssv3+low_integrity_iot_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD ALTO \n")
print("             - EL "+str(float((((low_integrity_lowavailability_sh_cvssv3+low_integrity_lowavailability_iot_cvssv3)*100)/(low_integrity_sh_cvssv3+low_integrity_iot_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD BAJO \n")
print("             - EL "+str(float((((low_integrity_mediumavailability_sh_cvssv3+low_integrity_mediumavailability_iot_cvssv3)*100)/(low_integrity_sh_cvssv3+low_integrity_iot_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD MEDIO \n")
print("             - EL "+str(float((((low_integrity_noneavailability_sh_cvssv3+low_integrity_noneavailability_iot_cvssv3)*100)/(low_integrity_sh_cvssv3+low_integrity_iot_cvssv3))))+" % DE LAS VULNERABILIDADES NO EXISTE AFECTACION/IMPACTO A LA DISPONIBILIDAD DEL SISTEMA \n")



if((medium_integrity_sh_cvssv3+medium_integrity_iot_cvssv3)>0):
    print(" - EN EL  "+str(float((((medium_integrity_sh_cvssv3+medium_integrity_iot_cvssv3)*100)/(len(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"])+len(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"])))))+" % DE LAS VULNERABILIDADES, DONDE EL IMPACTO DE INTEGRIDAD ES MEDIO \n")
    print("      - LOS PORCENTAJES DE IMPACTO DE CONFIDENCIALIDAD SON LOS SIGUIENTES : \n")
    print("             - EL "+str(float((((medium_integrity_highconfidentiality_sh_cvssv3+medium_integrity_highconfidentiality_iot_cvssv3)*100)/(medium_integrity_sh_cvssv3+medium_integrity_iot_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD ALTO \n")
    print("             - EL "+str(float((((medium_integrity_lowconfidentiality_sh_cvssv3+medium_integrity_lowconfidentiality_iot_cvssv3)*100)/(medium_integrity_sh_cvssv3+medium_integrity_iot_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD BAJO \n")
    print("             - EL "+str(float((((medium_integrity_mediumconfidentiality_sh_cvssv3+medium_integrity_mediumconfidentiality_iot_cvssv3)*100)/(medium_integrity_sh_cvssv3+medium_integrity_iot_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD MEDIO \n")
    print("             - EL "+str(float((((medium_integrity_noneconfidentiality_sh_cvssv3+medium_integrity_noneconfidentiality_iot_cvssv3)*100)/(medium_integrity_sh_cvssv3+medium_integrity_iot_cvssv3))))+" % DE LAS VULNERABILIDADES NO EXISTE AFECTACION/IMPACTO A LA CONFIDENCIALIDAD DEL SISTEMA \n")
    print("\n")
    print("      - LOS PORCENTAJES DE IMPACTO DE DISPONIBILIDAD SON LOS SIGUIENTES : \n")
    print("             - EL "+str(float((((medium_integrity_highavailability_sh_cvssv3+medium_integrity_highavailability_iot_cvssv3)*100)/(medium_integrity_sh_cvssv3+medium_integrity_iot_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD ALTO \n")
    print("             - EL "+str(float((((medium_integrity_lowavailability_sh_cvssv3+medium_integrity_lowavailability_iot_cvssv3)*100)/(medium_integrity_sh_cvssv3+medium_integrity_iot_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD BAJO \n")
    print("             - EL "+str(float((((medium_integrity_mediumavailability_sh_cvssv3+medium_integrity_mediumavailability_iot_cvssv3)*100)/(medium_integrity_sh_cvssv3+medium_integrity_iot_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD MEDIO \n")
    print("             - EL "+str(float((((medium_integrity_noneavailability_sh_cvssv3+medium_integrity_noneavailability_iot_cvssv3)*100)/(medium_integrity_sh_cvssv3+medium_integrity_iot_cvssv3))))+" % DE LAS VULNERABILIDADES NO EXISTE AFECTACION/IMPACTO A LA DISPONIBILIDAD DEL SISTEMA \n")



print(" - EN EL  "+str(float((((none_integrity_sh_cvssv3+none_integrity_iot_cvssv3)*100)/(len(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"])+len(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"])))))+" % DE LAS VULNERABILIDADES, DONDE NO EXISTE AFECTACION/IMPACTO A LA INTEGRIDAD DEL SISTEMA \n")
print("      - LOS PORCENTAJES DE IMPACTO DE CONFIDENCIALIDAD SON LOS SIGUIENTES : \n")
print("             - EL "+str(float((((none_integrity_highconfidentiality_sh_cvssv3+none_integrity_highconfidentiality_iot_cvssv3)*100)/(none_integrity_sh_cvssv3+none_integrity_iot_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD ALTO \n")
print("             - EL "+str(float((((none_integrity_lowconfidentiality_sh_cvssv3+none_integrity_lowconfidentiality_iot_cvssv3)*100)/(none_integrity_sh_cvssv3+none_integrity_iot_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD BAJO \n")
print("             - EL "+str(float((((none_integrity_mediumconfidentiality_sh_cvssv3+none_integrity_mediumconfidentiality_iot_cvssv3)*100)/(none_integrity_sh_cvssv3+none_integrity_iot_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD MEDIO \n")
print("             - EL "+str(float((((none_integrity_noneconfidentiality_sh_cvssv3+none_integrity_noneconfidentiality_iot_cvssv3)*100)/(none_integrity_sh_cvssv3+none_integrity_iot_cvssv3))))+" % DE LAS VULNERABILIDADES NO EXISTE AFECTACION/IMPACTO A LA CONFIDENCIALIDAD DEL SISTEMA \n")
print("\n")
print("      - LOS PORCENTAJES DE IMPACTO DE DISPONIBILIDAD SON LOS SIGUIENTES : \n")
print("             - EL "+str(float((((none_integrity_highavailability_sh_cvssv3+none_integrity_highavailability_iot_cvssv3)*100)/(none_integrity_sh_cvssv3+none_integrity_iot_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD ALTO \n")
print("             - EL "+str(float((((none_integrity_lowavailability_sh_cvssv3+none_integrity_lowavailability_iot_cvssv3)*100)/(none_integrity_sh_cvssv3+none_integrity_iot_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD BAJO \n")
print("             - EL "+str(float((((none_integrity_mediumavailability_sh_cvssv3+none_integrity_mediumavailability_iot_cvssv3)*100)/(none_integrity_sh_cvssv3+none_integrity_iot_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD MEDIO \n")
print("             - EL "+str(float((((none_integrity_noneavailability_sh_cvssv3+none_integrity_noneavailability_iot_cvssv3)*100)/(none_integrity_sh_cvssv3+none_integrity_iot_cvssv3))))+" % DE LAS VULNERABILIDADES NO EXISTE AFECTACION/IMPACTO A LA DISPONIBILIDAD DEL SISTEMA \n")




print("*************************************************************************************************************************")

print(" - EN EL  "+str(float((((high_availability_sh_cvssv3+high_availability_iot_cvssv3)*100)/(total_vulnerabilities_cvssv3))))+" % DE LAS VULNERABILIDADES, DONDE EL IMPACTO DE DISPONIBILIDAD ES ALTO \n")
print("      - LOS PORCENTAJES DE IMPACTO DE CONFIDENCIALIDAD SON LOS SIGUIENTES : \n")
print("             - EL "+str(float((((high_availability_highconfidentiality_sh_cvssv3+high_availability_highconfidentiality_iot_cvssv3)*100)/(high_availability_sh_cvssv3+high_availability_iot_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD ALTO \n")
print("             - EL "+str(float((((high_availability_lowconfidentiality_sh_cvssv3+high_availability_lowconfidentiality_iot_cvssv3)*100)/(high_availability_sh_cvssv3+high_availability_iot_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD BAJO \n")
print("             - EL "+str(float((((high_availability_mediumconfidentiality_sh_cvssv3+high_availability_mediumconfidentiality_iot_cvssv3)*100)/(high_availability_sh_cvssv3+high_availability_iot_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD MEDIO \n")
print("             - EL "+str(float((((high_availability_noneconfidentiality_sh_cvssv3+high_availability_noneconfidentiality_iot_cvssv3)*100)/(high_availability_sh_cvssv3+high_availability_iot_cvssv3))))+" % DE LAS VULNERABILIDADES NO EXISTE AFECTACION/IMPACTO A LA CONFIDENCIALIDAD DEL SISTEMA \n")
print("\n")
print("      - LOS PORCENTAJES DE IMPACTO DE INTEGRIDAD SON LOS SIGUIENTES : \n")
print("             - EL "+str(float((((high_availability_highintegrity_sh_cvssv3+high_availability_highintegrity_iot_cvssv3)*100)/(high_availability_sh_cvssv3+high_availability_iot_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD ALTO \n")
print("             - EL "+str(float((((high_availability_lowintegrity_sh_cvssv3+high_availability_lowintegrity_iot_cvssv3)*100)/(high_availability_sh_cvssv3+high_availability_iot_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD BAJO \n")
print("             - EL "+str(float((((high_availability_mediumintegrity_sh_cvssv3+high_availability_mediumintegrity_iot_cvssv3)*100)/(high_availability_sh_cvssv3+high_availability_iot_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD MEDIO \n")
print("             - EL "+str(float((((high_availability_noneintegrity_sh_cvssv3+high_availability_noneintegrity_iot_cvssv3)*100)/(high_availability_sh_cvssv3+high_availability_iot_cvssv3))))+" % DE LAS VULNERABILIDADES NO EXISTE AFECTACION/IMPACTO A LA INTEGRIDAD DEL SISTEMA \n")



print(" - EN EL  "+str(float((((low_availability_sh_cvssv3+low_availability_iot_cvssv3)*100)/(total_vulnerabilities_cvssv3))))+" % DE LAS VULNERABILIDADES, DONDE EL IMPACTO DE DISPONIBILIDAD ES BAJO \n")
print("      - LOS PORCENTAJES DE IMPACTO DE CONFIDENCIALIDAD SON LOS SIGUIENTES : \n")
print("             - EL "+str(float((((low_availability_highconfidentiality_sh_cvssv3+low_availability_highconfidentiality_iot_cvssv3)*100)/(low_availability_sh_cvssv3+low_availability_iot_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD ALTO \n")
print("             - EL "+str(float((((low_availability_lowconfidentiality_sh_cvssv3+low_availability_lowconfidentiality_iot_cvssv3)*100)/(low_availability_sh_cvssv3+low_availability_iot_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD BAJO \n")
print("             - EL "+str(float((((low_availability_mediumconfidentiality_sh_cvssv3+low_availability_mediumconfidentiality_iot_cvssv3)*100)/(low_availability_sh_cvssv3+low_availability_iot_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD MEDIO \n")
print("             - EL "+str(float((((low_availability_noneconfidentiality_sh_cvssv3+low_availability_noneconfidentiality_iot_cvssv3)*100)/(low_availability_sh_cvssv3+low_availability_iot_cvssv3))))+" % DE LAS VULNERABILIDADES NO EXISTE AFECTACION/IMPACTO A LA CONFIDENCIALIDAD DEL SISTEMA \n")
print("\n")
print("      - LOS PORCENTAJES DE IMPACTO DE INTEGRIDAD SON LOS SIGUIENTES : \n")
print("             - EL "+str(float((((low_availability_highintegrity_sh_cvssv3+low_availability_highintegrity_iot_cvssv3)*100)/(low_availability_sh_cvssv3+low_availability_iot_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD ALTO \n")
print("             - EL "+str(float((((low_availability_lowintegrity_sh_cvssv3+low_availability_lowintegrity_iot_cvssv3)*100)/(low_availability_sh_cvssv3+low_availability_iot_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD BAJO \n")
print("             - EL "+str(float((((low_availability_mediumintegrity_sh_cvssv3+low_availability_mediumintegrity_iot_cvssv3)*100)/(low_availability_sh_cvssv3+low_availability_iot_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD MEDIO \n")
print("             - EL "+str(float((((low_availability_noneintegrity_sh_cvssv3+low_availability_noneintegrity_iot_cvssv3)*100)/(low_availability_sh_cvssv3+low_availability_iot_cvssv3))))+" % DE LAS VULNERABILIDADES NO EXISTE AFECTACION/IMPACTO A LA INTEGRIDAD DEL SISTEMA \n")



if((medium_availability_sh_cvssv3+medium_availability_iot_cvssv3)>0):
    print(" - EN EL  "+str(float((((medium_availability_sh_cvssv3+medium_availability_iot_cvssv3)*100)/(total_vulnerabilities_cvssv3))))+" % DE LAS VULNERABILIDADES, DONDE EL IMPACTO DE DISPONIBILIDAD ES MEDIO \n")
    print("      - LOS PORCENTAJES DE IMPACTO DE CONFIDENCIALIDAD SON LOS SIGUIENTES : \n")
    print("             - EL "+str(float((((medium_availability_highconfidentiality_sh_cvssv3+medium_availability_highconfidentiality_iot_cvssv3)*100)/(medium_availability_sh_cvssv3+medium_availability_iot_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD ALTO \n")
    print("             - EL "+str(float((((medium_availability_lowconfidentiality_sh_cvssv3+medium_availability_lowconfidentiality_iot_cvssv3)*100)/(medium_availability_sh_cvssv3+medium_availability_iot_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD BAJO \n")
    print("             - EL "+str(float((((medium_availability_mediumconfidentiality_sh_cvssv3+medium_availability_mediumconfidentiality_iot_cvssv3)*100)/(medium_availability_sh_cvssv3+medium_availability_iot_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD MEDIO \n")
    print("             - EL "+str(float((((medium_availability_noneconfidentiality_sh_cvssv3+medium_availability_noneconfidentiality_iot_cvssv3)*100)/(medium_availability_sh_cvssv3+medium_availability_iot_cvssv3))))+" % DE LAS VULNERABILIDADES NO EXISTE AFECTACION/IMPACTO A LA CONFIDENCIALIDAD DEL SISTEMA \n")
    print("\n")
    print("      - LOS PORCENTAJES DE IMPACTO DE INTEGRIDAD SON LOS SIGUIENTES : \n")
    print("             - EL "+str(float((((medium_availability_highintegrity_sh_cvssv3+medium_availability_highintegrity_iot_cvssv3)*100)/(medium_availability_sh_cvssv3+medium_availability_iot_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD ALTO \n")
    print("             - EL "+str(float((((medium_availability_lowintegrity_sh_cvssv3+medium_availability_lowintegrity_iot_cvssv3)*100)/(medium_availability_sh_cvssv3+medium_availability_iot_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD BAJO \n")
    print("             - EL "+str(float((((medium_availability_mediumintegrity_sh_cvssv3+medium_availability_mediumintegrity_iot_cvssv3)*100)/(medium_availability_sh_cvssv3+medium_availability_iot_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD MEDIO \n")
    print("             - EL "+str(float((((medium_availability_noneintegrity_sh_cvssv3+medium_availability_noneintegrity_iot_cvssv3)*100)/(medium_availability_sh_cvssv3+medium_availability_iot_cvssv3))))+" % DE LAS VULNERABILIDADES NO EXISTE AFECTACION/IMPACTO A LA INTEGRIDAD DEL SISTEMA \n")



print(" - EN EL  "+str(float((((none_availability_sh_cvssv3+none_availability_iot_cvssv3)*100)/(total_vulnerabilities_cvssv3))))+" % DE LAS VULNERABILIDADES, DONDE NO EXISTE AFECTACION/IMPACTO A LA DISPONIBILIDAD DEL SISTEMA \n")
print("      - LOS PORCENTAJES DE IMPACTO DE CONFIDENCIALIDAD SON LOS SIGUIENTES : \n")
print("             - EL "+str(float((((none_availability_highconfidentiality_sh_cvssv3+none_availability_highconfidentiality_iot_cvssv3)*100)/(none_availability_sh_cvssv3+none_availability_iot_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD ALTO \n")
print("             - EL "+str(float((((none_availability_lowconfidentiality_sh_cvssv3+none_availability_lowconfidentiality_iot_cvssv3)*100)/(none_availability_sh_cvssv3+none_availability_iot_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD BAJO \n")
print("             - EL "+str(float((((none_availability_mediumconfidentiality_sh_cvssv3+none_availability_mediumconfidentiality_iot_cvssv3)*100)/(none_availability_sh_cvssv3+none_availability_iot_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD MEDIO \n")
print("             - EL "+str(float((((none_availability_noneconfidentiality_sh_cvssv3+none_availability_noneconfidentiality_iot_cvssv3)*100)/(none_availability_sh_cvssv3+none_availability_iot_cvssv3))))+" % DE LAS VULNERABILIDADES NO EXISTE AFECTACION/IMPACTO A LA CONFIDENCIALIDAD DEL SISTEMA \n")
print("\n")
print("      - LOS PORCENTAJES DE IMPACTO DE INTEGRIDAD SON LOS SIGUIENTES : \n")
print("             - EL "+str(float((((none_availability_highintegrity_sh_cvssv3+none_availability_highintegrity_iot_cvssv3)*100)/(none_availability_sh_cvssv3+none_availability_iot_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD ALTO \n")
print("             - EL "+str(float((((none_availability_lowintegrity_sh_cvssv3+none_availability_lowintegrity_iot_cvssv3)*100)/(none_availability_sh_cvssv3+none_availability_iot_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD BAJO \n")
print("             - EL "+str(float((((none_availability_mediumintegrity_sh_cvssv3+none_availability_mediumintegrity_iot_cvssv3)*100)/(none_availability_sh_cvssv3+none_availability_iot_cvssv3))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD MEDIO \n")
print("             - EL "+str(float((((none_availability_noneintegrity_sh_cvssv3+none_availability_noneintegrity_iot_cvssv3)*100)/(none_availability_sh_cvssv3+none_availability_iot_cvssv3))))+" % DE LAS VULNERABILIDADES NO EXISTE AFECTACION/IMPACTO A LA INTEGRIDAD DEL SISTEMA \n")








































































