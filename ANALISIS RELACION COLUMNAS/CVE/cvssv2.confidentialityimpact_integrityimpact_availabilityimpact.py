


import pandas as pd

#Abro los ficheros con los que voy a tratar


df_cve_iot=pd.read_excel('cves_iot_2023.xlsx')
df_cve_sh=pd.read_excel('cves_smart_home_2023.xlsx')




print("***************************RELACION IMPACTO CONFIDENCIALIDAD/INTEGRIDAD/DISPONIBILIDAD CVSSV2 PARTE IOT***************************")
print("\n")
print("\n")

#Variables donde almacenare el contador de nivel especifico de confidencialidad
complete_confidentiality_iot_cvssv2=0
#Variables donde almacenare el contador de nivel de integridad segun valor de confidencialidad dado
complete_confidentiality_partialintegrity_iot_cvssv2=0
complete_confidentiality_completeintegrity_iot_cvssv2=0
complete_confidentiality_noneintegrity_iot_cvssv2=0
#Variables donde almacenare el contador de nivel de integridad segun valor de disponibilidad  dado
complete_confidentiality_partialavailability_iot_cvssv2=0
complete_confidentiality_completeavailability_iot_cvssv2=0
complete_confidentiality_noneavailability_iot_cvssv2=0

partial_confidentiality_iot_cvssv2=0

partial_confidentiality_partialintegrity_iot_cvssv2=0
partial_confidentiality_completeintegrity_iot_cvssv2=0
partial_confidentiality_noneintegrity_iot_cvssv2=0

partial_confidentiality_partialavailability_iot_cvssv2=0
partial_confidentiality_completeavailability_iot_cvssv2=0
partial_confidentiality_noneavailability_iot_cvssv2=0


none_confidentiality_iot_cvssv2=0

none_confidentiality_partialintegrity_iot_cvssv2=0
none_confidentiality_completeintegrity_iot_cvssv2=0
none_confidentiality_noneintegrity_iot_cvssv2=0

none_confidentiality_partialavailability_iot_cvssv2=0
none_confidentiality_completeavailability_iot_cvssv2=0
none_confidentiality_noneavailability_iot_cvssv2=0

#Variables donde almacenare el contador de nivel especifico de integridad
complete_integrity_iot_cvssv2=0
#Variables donde almacenare el contador de nivel de confidencialidad segun valor de integridad dado
complete_integrity_partialconfidentiality_iot_cvssv2=0
complete_integrity_completeconfidentiality_iot_cvssv2=0
complete_integrity_noneconfidentiality_iot_cvssv2=0
#Variables donde almacenare el contador de nivel de disponibilidadd segun valor de integridad dado
complete_integrity_partialavailability_iot_cvssv2=0
complete_integrity_completeavailability_iot_cvssv2=0
complete_integrity_noneavailability_iot_cvssv2=0

partial_integrity_iot_cvssv2=0

partial_integrity_partialconfidentiality_iot_cvssv2=0
partial_integrity_completeconfidentiality_iot_cvssv2=0

partial_integrity_noneconfidentiality_iot_cvssv2=0
partial_integrity_partialavailability_iot_cvssv2=0
partial_integrity_completeavailability_iot_cvssv2=0
partial_integrity_noneavailability_iot_cvssv2=0


none_integrity_iot_cvssv2=0

none_integrity_partialconfidentiality_iot_cvssv2=0
none_integrity_completeconfidentiality_iot_cvssv2=0
none_integrity_noneconfidentiality_iot_cvssv2=0

none_integrity_partialavailability_iot_cvssv2=0
none_integrity_completeavailability_iot_cvssv2=0
none_integrity_noneavailability_iot_cvssv2=0


#Variables donde almacenare el contador de nivel especifico de disponibilidad
complete_availability_iot_cvssv2=0
#Variables donde almacenare el contador de nivel de confidencialidad segun valor de disponibilidad dado
complete_availability_partialconfidentiality_iot_cvssv2=0
complete_availability_completeconfidentiality_iot_cvssv2=0
complete_availability_noneconfidentiality_iot_cvssv2=0
#Variables donde almacenare el contador de nivel de integridad segun valor de disponibilidad dado
complete_availability_partialintegrity_iot_cvssv2=0
complete_availability_completeintegrity_iot_cvssv2=0
complete_availability_noneintegrity_iot_cvssv2=0

partial_availability_iot_cvssv2=0

partial_availability_partialconfidentiality_iot_cvssv2=0
partial_availability_completeconfidentiality_iot_cvssv2=0
partial_availability_noneconfidentiality_iot_cvssv2=0

partial_availability_partialintegrity_iot_cvssv2=0
partial_availability_completeintegrity_iot_cvssv2=0
partial_availability_noneintegrity_iot_cvssv2=0

none_availability_iot_cvssv2=0

none_availability_partialconfidentiality_iot_cvssv2=0
none_availability_completeconfidentiality_iot_cvssv2=0
none_availability_noneconfidentiality_iot_cvssv2=0

none_availability_partialintegrity_iot_cvssv2=0
none_availability_completeintegrity_iot_cvssv2=0
none_availability_noneintegrity_iot_cvssv2=0



#Recorro los distintos valores de confidencialidad y los comparo con los valores de integridad
for j in range(0,len(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.confidentialityImpact"])):
    if(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.confidentialityImpact"][j]=='COMPLETE'):
        complete_confidentiality_iot_cvssv2+=1
        if(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.integrityImpact"][j]=='COMPLETE'):
            complete_confidentiality_completeintegrity_iot_cvssv2+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.integrityImpact"][j]=='PARTIAL'):
            complete_confidentiality_partialintegrity_iot_cvssv2+=1
        else:
            complete_confidentiality_noneintegrity_iot_cvssv2+=1
            
    elif(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.confidentialityImpact"][j]=='PARTIAL'):
        partial_confidentiality_iot_cvssv2+=1
        if(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.integrityImpact"][j]=='COMPLETE'):
            partial_confidentiality_completeintegrity_iot_cvssv2+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.integrityImpact"][j]=='PARTIAL'):
            partial_confidentiality_partialintegrity_iot_cvssv2+=1
        else:
            partial_confidentiality_noneintegrity_iot_cvssv2+=1

    else:
        none_confidentiality_iot_cvssv2+=1
        if(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.integrityImpact"][j]=='COMPLETE'):
            none_confidentiality_completeintegrity_iot_cvssv2+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.integrityImpact"][j]=='PARTIAL'):
            none_confidentiality_partialintegrity_iot_cvssv2+=1
        else:
            none_confidentiality_noneintegrity_iot_cvssv2+=1
            
            
            
            
            
            
            
            
            
            
            
#Recorro los distintos valores de confidencialidad y los comparo con los valores de disponibilidad           
for h in range(0,len(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.confidentialityImpact"])):
    if(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.confidentialityImpact"][h]=='COMPLETE'):
        if(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.availabilityImpact"][h]=='COMPLETE'):
            complete_confidentiality_completeavailability_iot_cvssv2+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.availabilityImpact"][h]=='PARTIAL'):
            complete_confidentiality_partialavailability_iot_cvssv2+=1
        else:
            complete_confidentiality_noneavailability_iot_cvssv2+=1
            
    elif(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.confidentialityImpact"][h]=='PARTIAL'):
        if(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.availabilityImpact"][h]=='COMPLETE'):
            partial_confidentiality_completeavailability_iot_cvssv2+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.availabilityImpact"][h]=='PARTIAL'):
            partial_confidentiality_partialavailability_iot_cvssv2+=1
        else:
            partial_confidentiality_noneavailability_iot_cvssv2+=1

    else:
        if(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.availabilityImpact"][h]=='COMPLETE'):
            none_confidentiality_completeavailability_iot_cvssv2+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.availabilityImpact"][h]=='PARTIAL'):
            none_confidentiality_partialavailability_iot_cvssv2+=1
        else:
            none_confidentiality_noneavailability_iot_cvssv2+=1




            
            
            
#Recorro los distintos valores de disponibilidad y los comparo con los valores de integridad
for k in range(0,len(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.availabilityImpact"])):
    if(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.availabilityImpact"][k]=='COMPLETE'):
        complete_availability_iot_cvssv2+=1
        if(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.integrityImpact"][k]=='COMPLETE'):
            complete_availability_completeintegrity_iot_cvssv2+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.integrityImpact"][k]=='PARTIAL'):
            complete_availability_partialintegrity_iot_cvssv2+=1
        else:
            complete_availability_noneintegrity_iot_cvssv2+=1
            
    elif(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.availabilityImpact"][k]=='PARTIAL'):
        partial_availability_iot_cvssv2+=1
        if(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.integrityImpact"][k]=='COMPLETE'):
            partial_availability_completeintegrity_iot_cvssv2+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.integrityImpact"][k]=='PARTIAL'):
            partial_availability_partialintegrity_iot_cvssv2+=1
        else:
            partial_availability_noneintegrity_iot_cvssv2+=1
    else:
        none_availability_iot_cvssv2+=1
        if(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.integrityImpact"][k]=='COMPLETE'):
            none_availability_completeintegrity_iot_cvssv2+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.integrityImpact"][k]=='PARTIAL'):
            none_availability_partialintegrity_iot_cvssv2+=1
        else:
            none_availability_noneintegrity_iot_cvssv2+=1
            
            
            
            
#Recorro los distintos valores de disponibilidad y los comparo con los valores de confidencialidad            
for l in range(0,len(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.availabilityImpact"])):
    if(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.availabilityImpact"][l]=='COMPLETE'):
        if(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.confidentialityImpact"][l]=='COMPLETE'):
            complete_availability_completeconfidentiality_iot_cvssv2+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.confidentialityImpact"][l]=='PARTIAL'):
            complete_availability_partialconfidentiality_iot_cvssv2+=1
        else:
            complete_availability_noneconfidentiality_iot_cvssv2+=1
            
    elif(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.availabilityImpact"][l]=='PARTIAL'):
        if(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.confidentialityImpact"][l]=='COMPLETE'):
            partial_availability_completeconfidentiality_iot_cvssv2+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.confidentialityImpact"][l]=='PARTIAL'):
            partial_availability_partialconfidentiality_iot_cvssv2+=1
        else:
            partial_availability_noneconfidentiality_iot_cvssv2+=1

    else:
        if(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.confidentialityImpact"][l]=='COMPLETE'):
            none_availability_completeconfidentiality_iot_cvssv2+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.confidentialityImpact"][l]=='PARTIAL'):
            none_availability_partialconfidentiality_iot_cvssv2+=1
        else:
            none_availability_noneconfidentiality_iot_cvssv2+=1
            
            
            

#Recorro los distintos valores de integridad y los comparo con los valores de confidencialidad
for n in range(0,len(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.integrityImpact"])):
    if(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.integrityImpact"][n]=='COMPLETE'):
        complete_integrity_iot_cvssv2+=1
        if(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.confidentialityImpact"][n]=='COMPLETE'):
            complete_integrity_completeconfidentiality_iot_cvssv2+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.confidentialityImpact"][n]=='PARTIAL'):
            complete_integrity_partialconfidentiality_iot_cvssv2+=1
        else:
            complete_integrity_noneconfidentiality_iot_cvssv2+=1
            
    elif(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.integrityImpact"][n]=='PARTIAL'):
        partial_integrity_iot_cvssv2+=1
        if(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.confidentialityImpact"][n]=='COMPLETE'):
            partial_integrity_completeconfidentiality_iot_cvssv2+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.confidentialityImpact"][n]=='PARTIAL'):
            partial_integrity_partialconfidentiality_iot_cvssv2+=1
        else:
            partial_integrity_noneconfidentiality_iot_cvssv2+=1
    else:
        none_integrity_iot_cvssv2+=1
        if(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.confidentialityImpact"][n]=='COMPLETE'):
            none_integrity_completeconfidentiality_iot_cvssv2+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.confidentialityImpact"][n]=='PARTIAL'):
            none_integrity_partialconfidentiality_iot_cvssv2+=1
        else:
            none_integrity_noneconfidentiality_iot_cvssv2+=1
            
            
            
            
            
#Recorro los distintos valores de integridad y los comparo con los valores de disponibilidad            
for p in range(0,len(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.integrityImpact"])):
    if(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.integrityImpact"][p]=='COMPLETE'):
        if(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.availabilityImpact"][p]=='COMPLETE'):
            complete_integrity_completeavailability_iot_cvssv2+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.availabilityImpact"][p]=='PARTIAL'):
            complete_integrity_partialavailability_iot_cvssv2+=1
        else:
            complete_integrity_noneavailability_iot_cvssv2+=1
            
    elif(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.integrityImpact"][p]=='PARTIAL'):
        if(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.availabilityImpact"][p]=='COMPLETE'):
            partial_integrity_completeavailability_iot_cvssv2+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.availabilityImpact"][p]=='PARTIAL'):
            partial_integrity_partialavailability_iot_cvssv2+=1
        else:
            partial_integrity_noneavailability_iot_cvssv2+=1
            
    else:
        if(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.availabilityImpact"][p]=='COMPLETE'):
            none_integrity_completeavailability_iot_cvssv2+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.availabilityImpact"][p]=='PARTIAL'):
            none_integrity_partialavailability_iot_cvssv2+=1

        else:
            none_integrity_noneavailability_iot_cvssv2+=1
            
            
            
print("************************** ESTADÍSTICAS IMPACTO CONFIDENCIALIDAD/INTEGRIDAD/DISPONIBILIDAD CVSSV2 CVE IOT********************************")
print("\n")
print(" DE UN TOTAL DE "+str(complete_confidentiality_iot_cvssv2+partial_confidentiality_iot_cvssv2+none_confidentiality_iot_cvssv2)+" VULNERABILIDADES, LAS ESTADÍSTICAS DE RELACION DE VALORES DE IMPACTO DE CONFIDENCIALIDAD/INTEGRIDAD/DISPONIBILIDAD SON LAS SIGUIENTES: \n")
print("\n")
print(" - DE UN TOTAL DE "+str(complete_confidentiality_iot_cvssv2)+" VULNERABILIDADES DONDE EL IMPACTO DE CONFIDENCIALIDAD ES COMPLETO \n")
print("      - LAS ESTADÍSTICAS DE IMPACTO DE INTEGRIDAD SON LAS SIGUIENTES : \n")
print("             - UN TOTAL DE "+str(complete_confidentiality_completeintegrity_iot_cvssv2)+" VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD COMPLETO \n")
print("             - UN TOTAL DE "+str(complete_confidentiality_partialintegrity_iot_cvssv2)+" VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD PARCIAL \n")
print("             - UN TOTAL DE "+str(complete_confidentiality_noneintegrity_iot_cvssv2)+" VULNERABILIDADES NO TIENEN IMPACTO EN LA INTEGRIDAD DEL SISTEMA/PRODUCTO: \n")
print("\n")
print("      - LAS ESTADÍSTICAS DE IMPACTO DE DISPONIBILIDAD SON LAS SIGUIENTES : \n")
print("             - UN TOTAL DE "+str(complete_confidentiality_completeavailability_iot_cvssv2)+" VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD COMPLETO \n")
print("             - UN TOTAL DE "+str(complete_confidentiality_partialavailability_iot_cvssv2)+" VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD PARCIAL \n")
print("             - UN TOTAL DE "+str(complete_confidentiality_noneavailability_iot_cvssv2)+" VULNERABILIDADES NO TIENEN IMPACTO EN LA DISPONIBILIDAD DEL SISTEMA/PRODUCTO: \n")

print(" - DE UN TOTAL DE "+str(partial_confidentiality_iot_cvssv2)+" VULNERABILIDADES DONDE EL IMPACTO DE CONFIDENCIALIDAD ES PARCIAL: \n")
print("      - LAS ESTADÍSTICAS DE IMPACTO DE INTEGRIDAD SON LAS SIGUIENTES : \n")
print("             - UN TOTAL DE "+str(partial_confidentiality_completeintegrity_iot_cvssv2)+" VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD COMPLETO \n")
print("             - UN TOTAL DE "+str(partial_confidentiality_partialintegrity_iot_cvssv2)+" VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD PARCIAL \n")
print("             - UN TOTAL DE "+str(partial_confidentiality_noneintegrity_iot_cvssv2)+" VULNERABILIDADES NO TIENEN IMPACTO EN LA INTEGRIDAD DEL SISTEMA/PRODUCTO: \n")
print("\n")
print("      - LAS ESTADÍSTICAS DE IMPACTO DE DISPONIBILIDAD SON LAS SIGUIENTES : \n")
print("             - UN TOTAL DE "+str(partial_confidentiality_completeavailability_iot_cvssv2)+" VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD COMPLETO \n")
print("             - UN TOTAL DE "+str(partial_confidentiality_partialavailability_iot_cvssv2)+" VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD PARCIAL \n")
print("             - UN TOTAL DE "+str(partial_confidentiality_noneavailability_iot_cvssv2)+" VULNERABILIDADES NO TIENEN IMPACTO EN LA DISPONIBILIDAD DEL SISTEMA/PRODUCTO: \n")



print(" - DE UN TOTAL DE "+str(none_confidentiality_iot_cvssv2)+" VULNERABILIDADES DONDE EL IMPACTO DE CONFIDENCIALIDAD NO TIENE EFECTO EN EL SISTEMA/PRODUCTO VULNERABLE \n")
print("      - LAS ESTADÍSTICAS DE IMPACTO DE INTEGRIDAD SON LAS SIGUIENTES : \n")
print("             - UN TOTAL DE "+str(none_confidentiality_completeintegrity_iot_cvssv2)+" VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD COMPLETO \n")
print("             - UN TOTAL DE "+str(none_confidentiality_partialintegrity_iot_cvssv2)+" VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD PARCIAL \n")
print("             - UN TOTAL DE "+str(none_confidentiality_noneintegrity_iot_cvssv2)+" VULNERABILIDADES NO TIENEN IMPACTO EN LA INTEGRIDAD DEL SISTEMA/PRODUCTO: \n")
print("\n")
print("      - LAS ESTADÍSTICAS DE IMPACTO DE DISPONIBILIDAD SON LAS SIGUIENTES : \n")
print("             - UN TOTAL DE "+str(none_confidentiality_completeavailability_iot_cvssv2)+" VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD COMPLETO \n")
print("             - UN TOTAL DE "+str(none_confidentiality_partialavailability_iot_cvssv2)+" VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD PARCIAL \n")
print("             - UN TOTAL DE "+str(none_confidentiality_noneavailability_iot_cvssv2)+" VULNERABILIDADES NO TIENEN IMPACTO EN LA DISPONIBILIDAD DEL SISTEMA/PRODUCTO: \n")

print("*************************************************************************************************************************")

print("\n")
print(" - DE UN TOTAL DE "+str(complete_availability_iot_cvssv2)+" VULNERABILIDADES DONDE EL IMPACTO DE DISPONIBILIDAD ES COMPLETO \n")
print("      - LAS ESTADÍSTICAS DE IMPACTO DE INTEGRIDAD SON LAS SIGUIENTES : \n")
print("             - UN TOTAL DE "+str(complete_availability_completeintegrity_iot_cvssv2)+" VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD COMPLETO \n")
print("             - UN TOTAL DE "+str(complete_availability_partialintegrity_iot_cvssv2)+" VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD PARCIAL \n")
print("             - UN TOTAL DE "+str(complete_availability_noneintegrity_iot_cvssv2)+" VULNERABILIDADES NO TIENEN IMPACTO EN LA INTEGRIDAD DEL SISTEMA/PRODUCTO: \n")
print("\n")
print("      - LAS ESTADÍSTICAS DE IMPACTO DE CONFIDENCIALIDAD SON LAS SIGUIENTES : \n")
print("             - UN TOTAL DE "+str(complete_availability_completeconfidentiality_iot_cvssv2)+" VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD COMPLETO \n")
print("             - UN TOTAL DE "+str(complete_availability_partialconfidentiality_iot_cvssv2)+" VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD PARCIAL \n")
print("             - UN TOTAL DE "+str(complete_availability_noneconfidentiality_iot_cvssv2)+" VULNERABILIDADES NO TIENEN IMPACTO EN LA CONFIDENCIALIDAD DEL SISTEMA/PRODUCTO: \n")
print("\n")
print(" - DE UN TOTAL DE "+str(partial_availability_iot_cvssv2)+" VULNERABILIDADES DONDE EL IMPACTO DE DISPONIBILIDAD ES PARCIAL: \n")
print("      - LAS ESTADÍSTICAS DE IMPACTO DE INTEGRIDAD SON LAS SIGUIENTES : \n")
print("             - UN TOTAL DE "+str(partial_availability_completeintegrity_iot_cvssv2)+" VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD COMPLETO \n")
print("             - UN TOTAL DE "+str(partial_availability_partialintegrity_iot_cvssv2)+" VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD PARCIAL \n")
print("             - UN TOTAL DE "+str(partial_availability_noneintegrity_iot_cvssv2)+" VULNERABILIDADES NO TIENEN IMPACTO EN LA INTEGRIDAD DEL SISTEMA/PRODUCTO: \n")
print("\n")
print("      - LAS ESTADÍSTICAS DE IMPACTO DE CONFIDENCIALIDAD SON LAS SIGUIENTES : \n")
print("             - UN TOTAL DE "+str(partial_availability_completeconfidentiality_iot_cvssv2)+" VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD COMPLETO \n")
print("             - UN TOTAL DE "+str(partial_availability_partialconfidentiality_iot_cvssv2)+" VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD PARCIAL \n")
print("             - UN TOTAL DE "+str(partial_availability_noneconfidentiality_iot_cvssv2)+" VULNERABILIDADES NO TIENEN IMPACTO EN LA CONFIDENCIALIDAD DEL SISTEMA/PRODUCTO: \n")
print("\n")

print("\n")
print(" - DE UN TOTAL DE "+str(none_availability_iot_cvssv2)+" VULNERABILIDADES DONDE EL IMPACTO DE DISPONIBILIDAD NO TIENE EFECTO EN EL SISTEMA/PRODUCTO VULNERABLE \n")
print("      - LAS ESTADÍSTICAS DE IMPACTO DE INTEGRIDAD SON LAS SIGUIENTES : \n")
print("             - UN TOTAL DE "+str(none_availability_completeintegrity_iot_cvssv2)+" VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD COMPLETO \n")
print("             - UN TOTAL DE "+str(none_availability_partialintegrity_iot_cvssv2)+" VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD PARCIAL \n")
print("             - UN TOTAL DE "+str(none_availability_noneintegrity_iot_cvssv2)+" VULNERABILIDADES NO TIENEN IMPACTO EN LA INTEGRIDAD DEL SISTEMA/PRODUCTO: \n")
print("\n")
print("      - LAS ESTADÍSTICAS DE IMPACTO DE CONFIDENCIALIDAD SON LAS SIGUIENTES : \n")
print("             - UN TOTAL DE "+str(none_availability_completeconfidentiality_iot_cvssv2)+" VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD COMPLETO \n")
print("             - UN TOTAL DE "+str(none_availability_partialconfidentiality_iot_cvssv2)+" VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD PARCIAL \n")
print("             - UN TOTAL DE "+str(none_availability_noneconfidentiality_iot_cvssv2)+" VULNERABILIDADES NO TIENEN IMPACTO EN LA CONFIDENCIALIDAD DEL SISTEMA/PRODUCTO: \n")


print("*************************************************************************************************************************")
print("\n")
print(" - DE UN TOTAL DE "+str(complete_integrity_iot_cvssv2)+" VULNERABILIDADES DONDE EL IMPACTO DE INTEGRIDAD ES COMPLETO \n")
print("      - LAS ESTADÍSTICAS DE IMPACTO DE CONFIDENCIALIDAD SON LAS SIGUIENTES : \n")
print("             - UN TOTAL DE "+str(complete_integrity_completeconfidentiality_iot_cvssv2)+" VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD COMPLETO \n")
print("             - UN TOTAL DE "+str(complete_integrity_partialconfidentiality_iot_cvssv2)+" VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD PARCIAL \n")
print("             - UN TOTAL DE "+str(complete_integrity_noneconfidentiality_iot_cvssv2)+" VULNERABILIDADES NO TIENEN IMPACTO EN LA CONFIDENCIALIDAD DEL SISTEMA/PRODUCTO: \n")
print("\n")
print("      - LAS ESTADÍSTICAS DE IMPACTO DE DISPONIBILIDAD SON LAS SIGUIENTES : \n")
print("             - UN TOTAL DE "+str(complete_integrity_completeavailability_iot_cvssv2)+" VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD COMPLETO \n")
print("             - UN TOTAL DE "+str(complete_integrity_partialavailability_iot_cvssv2)+" VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD PARCIAL \n")
print("             - UN TOTAL DE "+str(complete_integrity_noneavailability_iot_cvssv2)+" VULNERABILIDADES NO TIENEN IMPACTO EN LA DISPONIBILIDAD DEL SISTEMA/PRODUCTO: \n")

print(" - DE UN TOTAL DE "+str(partial_integrity_iot_cvssv2)+" VULNERABILIDADES DONDE EL IMPACTO DE INTEGRIDAD ES PARCIAL: \n")
print("      - LAS ESTADÍSTICAS DE IMPACTO DE CONFIDENCIALIDAD SON LAS SIGUIENTES : \n")
print("             - UN TOTAL DE "+str(partial_integrity_completeconfidentiality_iot_cvssv2)+" VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD COMPLETO \n")
print("             - UN TOTAL DE "+str(partial_integrity_partialconfidentiality_iot_cvssv2)+" VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD PARCIAL \n")
print("             - UN TOTAL DE "+str(partial_integrity_noneconfidentiality_iot_cvssv2)+" VULNERABILIDADES NO TIENEN IMPACTO EN LA CONFIDENCIALIDAD DEL SISTEMA/PRODUCTO: \n")
print("\n")
print("      - LAS ESTADÍSTICAS DE IMPACTO DE DISPONIBILIDAD SON LAS SIGUIENTES : \n")
print("             - UN TOTAL DE "+str(partial_integrity_completeavailability_iot_cvssv2)+" VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD COMPLETO \n")
print("             - UN TOTAL DE "+str(partial_integrity_partialavailability_iot_cvssv2)+" VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD PARCIAL \n")
print("             - UN TOTAL DE "+str(partial_integrity_noneavailability_iot_cvssv2)+" VULNERABILIDADES NO TIENEN IMPACTO EN LA DISPONIBILIDAD DEL SISTEMA/PRODUCTO: \n")


print(" - DE UN TOTAL DE "+str(none_integrity_iot_cvssv2)+" VULNERABILIDADES DONDE EL IMPACTO DE INTEGRIDAD NO TIENE EFECTO EN EL SISTEMA/PRODUCTO VULNERABLE \n")
print("      - LAS ESTADÍSTICAS DE IMPACTO DE CONFIDENCIALIDAD SON LAS SIGUIENTES : \n")
print("             - UN TOTAL DE "+str(none_integrity_completeconfidentiality_iot_cvssv2)+" VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD COMPLETO \n")
print("             - UN TOTAL DE "+str(none_integrity_partialconfidentiality_iot_cvssv2)+" VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD PARCIAL \n")
print("             - UN TOTAL DE "+str(none_integrity_noneconfidentiality_iot_cvssv2)+" VULNERABILIDADES NO TIENEN IMPACTO EN LA CONFIDENCIALIDAD DEL SISTEMA/PRODUCTO: \n")
print("\n")
print("      - LAS ESTADÍSTICAS DE IMPACTO DE DISPONIBILIDAD SON LAS SIGUIENTES : \n")
print("             - UN TOTAL DE "+str(none_integrity_completeavailability_iot_cvssv2)+" VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD COMPLETO \n")
print("             - UN TOTAL DE "+str(none_integrity_partialavailability_iot_cvssv2)+" VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD PARCIAL \n")
print("             - UN TOTAL DE "+str(none_integrity_noneavailability_iot_cvssv2)+" VULNERABILIDADES NO TIENEN IMPACTO EN LA DISPONIBILIDAD DEL SISTEMA/PRODUCTO: \n")



print("*************************************************************************************************************************")



total_vulnerabilities_iot_cvssv2=complete_confidentiality_iot_cvssv2+partial_confidentiality_iot_cvssv2+none_confidentiality_iot_cvssv2


print("************************** PORCENTAJE IMPACTO CONFIDENCIALIDAD/INTEGRIDAD/DISPONIBILIDAD CVSSV2 CVE IOT********************************")
print("\n")
print(" DE UN TOTAL DE "+str(complete_confidentiality_iot_cvssv2+partial_confidentiality_iot_cvssv2+none_confidentiality_iot_cvssv2)+" VULNERABILIDADES, LOS PORCENTAJES DE VALORES DE RELACION DE VALORES DE IMPACTO DE CONFIDENCIALIDAD/INTEGRIDAD Y DISPONIBILIDAD SON LOS SIGUIENTES: \n")
print("\n")
print(" - EN EL  "+str(float(((complete_confidentiality_iot_cvssv2*100)/(total_vulnerabilities_iot_cvssv2))))+" % DE LAS VULNERABILIDADES, DONDE EL IMPACTO DE CONFIDENCIALIDAD ES COMPLETO \n")
print("      - LOS PORCENTAJES DE IMPACTO DE INTEGRIDAD SON LOS SIGUIENTES : \n")
print("             - EL "+str(float(((complete_confidentiality_completeintegrity_iot_cvssv2*100)/(complete_confidentiality_iot_cvssv2))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD COMPLETO \n")
print("             - EL "+str(float(((complete_confidentiality_partialintegrity_iot_cvssv2*100)/(complete_confidentiality_iot_cvssv2))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD PARCIAL \n")
print("             - EL "+str(float(((complete_confidentiality_noneintegrity_iot_cvssv2*100)/(complete_confidentiality_iot_cvssv2))))+" % DE LAS VULNERABILIDADES NO TIENEN IMPACTO EN LA INTEGRIDAD DEL SISTEMA/PRODUCTO \n")
print("\n")
print("      - LOS PORCENTAJES DE IMPACTO DE DISPONIBILIDAD SON LOS SIGUIENTES : \n")
print("             - EL "+str(float(((complete_confidentiality_completeavailability_iot_cvssv2*100)/(complete_confidentiality_iot_cvssv2))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD COMPLETO \n")
print("             - EL "+str(float(((complete_confidentiality_partialavailability_iot_cvssv2*100)/(complete_confidentiality_iot_cvssv2))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD PARCIAL \n")
print("             - EL "+str(float(((complete_confidentiality_noneavailability_iot_cvssv2*100)/(complete_confidentiality_iot_cvssv2))))+" % DE LAS VULNERABILIDADES NO TIENEN IMPACTO EN LA DISPONIBILIDAD DEL SISTEMA/PRODUCTO \n")

print("\n")
print(" - EN EL  "+str(float(((partial_confidentiality_iot_cvssv2*100)/(total_vulnerabilities_iot_cvssv2))))+" % DE LAS VULNERABILIDADES, DONDE EL IMPACTO DE CONFIDENCIALIDAD ES PARCIAL: \n")
print("      - LOS PORCENTAJES DE IMPACTO DE INTEGRIDAD SON LOS SIGUIENTES : \n")
print("             - EL "+str(float(((complete_confidentiality_completeintegrity_iot_cvssv2*100)/(complete_confidentiality_iot_cvssv2))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD COMPLETO \n")
print("             - EL "+str(float(((complete_confidentiality_partialintegrity_iot_cvssv2*100)/(complete_confidentiality_iot_cvssv2))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD PARCIAL \n")
print("             - EL "+str(float(((complete_confidentiality_noneintegrity_iot_cvssv2*100)/(complete_confidentiality_iot_cvssv2))))+" % DE LAS VULNERABILIDADES NO TIENEN IMPACTO EN LA INTEGRIDAD DEL SISTEMA/PRODUCTO \n")
print("\n")
print("      - LOS PORCENTAJES DE IMPACTO DE DISPONIBILIDAD SON LOS SIGUIENTES : \n")
print("             - EL "+str(float(((complete_confidentiality_completeavailability_iot_cvssv2*100)/(complete_confidentiality_iot_cvssv2))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD COMPLETO \n")
print("             - EL "+str(float(((complete_confidentiality_partialavailability_iot_cvssv2*100)/(complete_confidentiality_iot_cvssv2))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD PARCIAL \n")
print("             - EL "+str(float(((complete_confidentiality_noneavailability_iot_cvssv2*100)/(complete_confidentiality_iot_cvssv2))))+" % DE LAS VULNERABILIDADES NO TIENEN IMPACTO EN LA DISPONIBILIDAD DEL SISTEMA/PRODUCTO \n")


print("\n")
print(" - EN EL  "+str(float(((none_confidentiality_iot_cvssv2*100)/(total_vulnerabilities_iot_cvssv2))))+" % DE LAS VULNERABILIDADES, DONDE EL IMPACTO DE CONFIDENCIALIDAD NO TIENE EFECTO EN EL SISTEMA/PRODUCTO VULNERABLE \n")
print("      - LOS PORCENTAJES DE IMPACTO DE INTEGRIDAD SON LOS SIGUIENTES : \n")
print("             - EL "+str(float(((complete_confidentiality_completeintegrity_iot_cvssv2*100)/(complete_confidentiality_iot_cvssv2))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD COMPLETO \n")
print("             - EL "+str(float(((complete_confidentiality_partialintegrity_iot_cvssv2*100)/(complete_confidentiality_iot_cvssv2))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD PARCIAL \n")
print("             - EL "+str(float(((complete_confidentiality_noneintegrity_iot_cvssv2*100)/(complete_confidentiality_iot_cvssv2))))+" % DE LAS VULNERABILIDADES NO TIENEN IMPACTO EN LA INTEGRIDAD DEL SISTEMA/PRODUCTO \n")
print("\n")
print("      - LOS PORCENTAJES DE IMPACTO DE DISPONIBILIDAD SON LOS SIGUIENTES : \n")
print("             - EL "+str(float(((complete_confidentiality_completeavailability_iot_cvssv2*100)/(complete_confidentiality_iot_cvssv2))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD COMPLETO \n")
print("             - EL "+str(float(((complete_confidentiality_partialavailability_iot_cvssv2*100)/(complete_confidentiality_iot_cvssv2))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD PARCIAL \n")
print("             - EL "+str(float(((complete_confidentiality_noneavailability_iot_cvssv2*100)/(complete_confidentiality_iot_cvssv2))))+" % DE LAS VULNERABILIDADES NO TIENEN IMPACTO EN LA DISPONIBILIDAD DEL SISTEMA/PRODUCTO \n")



print("*************************************************************************************************************************")


print("\n")
print(" - EN EL  "+str(float(((complete_integrity_iot_cvssv2*100)/(total_vulnerabilities_iot_cvssv2))))+" % DE LAS VULNERABILIDADES, DONDE EL IMPACTO DE INTEGRIDAD ES COMPLETO \n")
print("      - LOS PORCENTAJES DE IMPACTO DE CONFIDENCIALIDAD SON LOS SIGUIENTES : \n")
print("             - EL "+str(float(((complete_integrity_completeconfidentiality_iot_cvssv2*100)/(complete_integrity_iot_cvssv2))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD COMPLETO \n")
print("             - EL "+str(float(((complete_integrity_partialconfidentiality_iot_cvssv2*100)/(complete_integrity_iot_cvssv2))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD PARCIAL \n")
print("             - EL "+str(float(((complete_integrity_noneconfidentiality_iot_cvssv2*100)/(complete_integrity_iot_cvssv2))))+" % DE LAS VULNERABILIDADES NO TIENEN IMPACTO EN LA CONFIDENCIALIDAD DEL SISTEMA/PRODUCTO \n")
print("\n")
print("      - LOS PORCENTAJES DE IMPACTO DE DISPONIBILIDAD SON LOS SIGUIENTES : \n")
print("             - EL "+str(float(((complete_integrity_completeavailability_iot_cvssv2*100)/(complete_integrity_iot_cvssv2))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD COMPLETO \n")
print("             - EL "+str(float(((complete_integrity_partialavailability_iot_cvssv2*100)/(complete_integrity_iot_cvssv2))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD PARCIAL \n")
print("             - EL "+str(float(((complete_integrity_noneavailability_iot_cvssv2*100)/(complete_integrity_iot_cvssv2))))+" % DE LAS VULNERABILIDADES NO TIENEN IMPACTO EN LA DISPONIBILIDAD DEL SISTEMA/PRODUCTO \n")




print("\n")
print(" - EN EL  "+str(float(((partial_integrity_iot_cvssv2*100)/(total_vulnerabilities_iot_cvssv2))))+" % DE LAS VULNERABILIDADES, DONDE EL IMPACTO DE INTEGRIDAD ES PARCIAL: \n")
print("      - LOS PORCENTAJES DE IMPACTO DE CONFIDENCIALIDAD SON LOS SIGUIENTES : \n")
print("             - EL "+str(float(((partial_integrity_completeconfidentiality_iot_cvssv2*100)/(partial_integrity_iot_cvssv2))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD COMPLETO \n")
print("             - EL "+str(float(((partial_integrity_partialconfidentiality_iot_cvssv2*100)/(partial_integrity_iot_cvssv2))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD PARCIAL \n")
print("             - EL "+str(float(((partial_integrity_noneconfidentiality_iot_cvssv2*100)/(partial_integrity_iot_cvssv2))))+" % DE LAS VULNERABILIDADES NO TIENEN IMPACTO EN LA CONFIDENCIALIDAD DEL SISTEMA/PRODUCTO \n")
print("\n")
print("      - LOS PORCENTAJES DE IMPACTO DE DISPONIBILIDAD SON LOS SIGUIENTES : \n")
print("             - EL "+str(float(((partial_integrity_completeavailability_iot_cvssv2*100)/(partial_integrity_iot_cvssv2))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD COMPLETO \n")
print("             - EL "+str(float(((partial_integrity_partialavailability_iot_cvssv2*100)/(partial_integrity_iot_cvssv2))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD PARCIAL \n")
print("             - EL "+str(float(((partial_integrity_noneavailability_iot_cvssv2*100)/(partial_integrity_iot_cvssv2))))+" % DE LAS VULNERABILIDADES NO TIENEN IMPACTO EN LA DISPONIBILIDAD DEL SISTEMA/PRODUCTO \n")




print("\n")
print(" - EN EL  "+str(float(((none_integrity_iot_cvssv2*100)/(total_vulnerabilities_iot_cvssv2))))+" % DE LAS VULNERABILIDADES, DONDE EL IMPACTO DE INTEGRIDAD NO TIENE EFECTO EN EL SISTEMA/PRODUCTO VULNERABLE \n")
print("      - LOS PORCENTAJES DE IMPACTO DE CONFIDENCIALIDAD SON LOS SIGUIENTES : \n")
print("             - EL "+str(float(((none_integrity_completeconfidentiality_iot_cvssv2*100)/(none_integrity_iot_cvssv2))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD COMPLETO \n")
print("             - EL "+str(float(((none_integrity_partialconfidentiality_iot_cvssv2*100)/(none_integrity_iot_cvssv2))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD PARCIAL \n")
print("             - EL "+str(float(((none_integrity_noneconfidentiality_iot_cvssv2*100)/(none_integrity_iot_cvssv2))))+" % DE LAS VULNERABILIDADES NO TIENEN IMPACTO EN LA CONFIDENCIALIDAD DEL SISTEMA/PRODUCTO \n")
print("\n")
print("      - LOS PORCENTAJES DE IMPACTO DE DISPONIBILIDAD SON LOS SIGUIENTES : \n")
print("             - EL "+str(float(((none_integrity_completeavailability_iot_cvssv2*100)/(none_integrity_iot_cvssv2))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD COMPLETO \n")
print("             - EL "+str(float(((none_integrity_partialavailability_iot_cvssv2*100)/(none_integrity_iot_cvssv2))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD PARCIAL \n")
print("             - EL "+str(float(((none_integrity_noneavailability_iot_cvssv2*100)/(none_integrity_iot_cvssv2))))+" % DE LAS VULNERABILIDADES NO TIENEN IMPACTO EN LA DISPONIBILIDAD DEL SISTEMA/PRODUCTO \n")



print("*************************************************************************************************************************")


print("\n")
print(" - EN EL  "+str(float(((complete_availability_iot_cvssv2*100)/(total_vulnerabilities_iot_cvssv2))))+" % DE LAS VULNERABILIDADES, DONDE EL IMPACTO DE DISPONIBILIDAD ES COMPLETO \n")
print("      - LOS PORCENTAJES DE IMPACTO DE CONFIDENCIALIDAD SON LOS SIGUIENTES : \n")
print("             - EL "+str(float(((complete_availability_completeconfidentiality_iot_cvssv2*100)/(complete_availability_iot_cvssv2))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD COMPLETO \n")
print("             - EL "+str(float(((complete_availability_partialconfidentiality_iot_cvssv2*100)/(complete_availability_iot_cvssv2))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD PARCIAL \n")
print("             - EL "+str(float(((complete_availability_noneconfidentiality_iot_cvssv2*100)/(complete_availability_iot_cvssv2))))+" % DE LAS VULNERABILIDADES NO TIENEN IMPACTO EN LA CONFIDENCIALIDAD DEL SISTEMA/PRODUCTO \n")
print("\n")
print("      - LOS PORCENTAJES DE IMPACTO DE INTEGRIDAD SON LOS SIGUIENTES : \n")
print("             - EL "+str(float(((complete_availability_completeintegrity_iot_cvssv2*100)/(complete_availability_iot_cvssv2))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD COMPLETO \n")
print("             - EL "+str(float(((complete_availability_partialintegrity_iot_cvssv2*100)/(complete_availability_iot_cvssv2))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD PARCIAL \n")
print("             - EL "+str(float(((complete_availability_noneintegrity_iot_cvssv2*100)/(complete_availability_iot_cvssv2))))+" % DE LAS VULNERABILIDADES NO TIENEN IMPACTO EN LA INTEGRIDAD DEL SISTEMA/PRODUCTO \n")


print("\n")
print(" - EN EL  "+str(float(((partial_availability_iot_cvssv2*100)/(total_vulnerabilities_iot_cvssv2))))+" % DE LAS VULNERABILIDADES, DONDE EL IMPACTO DE DISPONIBILIDAD ES PARCIAL: \n")
print("      - LOS PORCENTAJES DE IMPACTO DE CONFIDENCIALIDAD SON LOS SIGUIENTES : \n")
print("             - EL "+str(float(((partial_availability_completeconfidentiality_iot_cvssv2*100)/(partial_availability_iot_cvssv2))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD COMPLETO \n")
print("             - EL "+str(float(((partial_availability_partialconfidentiality_iot_cvssv2*100)/(partial_availability_iot_cvssv2))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD PARCIAL \n")
print("             - EL "+str(float(((partial_availability_noneconfidentiality_iot_cvssv2*100)/(partial_availability_iot_cvssv2))))+" % DE LAS VULNERABILIDADES NO TIENEN IMPACTO EN LA CONFIDENCIALIDAD DEL SISTEMA/PRODUCTO \n")
print("\n")
print("      - LOS PORCENTAJES DE IMPACTO DE INTEGRIDAD SON LOS SIGUIENTES : \n")
print("             - EL "+str(float(((partial_availability_completeintegrity_iot_cvssv2*100)/(partial_availability_iot_cvssv2))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD COMPLETO \n")
print("             - EL "+str(float(((partial_availability_partialintegrity_iot_cvssv2*100)/(partial_availability_iot_cvssv2))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD PARCIAL \n")
print("             - EL "+str(float(((partial_availability_noneintegrity_iot_cvssv2*100)/(partial_availability_iot_cvssv2))))+" % DE LAS VULNERABILIDADES NO TIENEN IMPACTO EN LA INTEGRIDAD DEL SISTEMA/PRODUCTO \n")



print("\n")
print(" - EN EL  "+str(float(((none_availability_iot_cvssv2*100)/(total_vulnerabilities_iot_cvssv2))))+" % DE LAS VULNERABILIDADES, DONDE EL IMPACTO DE DISPONIBILIDAD NO TIENE EFECTO EN EL SISTEMA/PRODUCTO VULNERABLE \n")
print("      - LOS PORCENTAJES DE IMPACTO DE CONFIDENCIALIDAD SON LOS SIGUIENTES : \n")
print("             - EL "+str(float(((none_availability_completeconfidentiality_iot_cvssv2*100)/(none_availability_iot_cvssv2))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD COMPLETO \n")
print("             - EL "+str(float(((none_availability_partialconfidentiality_iot_cvssv2*100)/(none_availability_iot_cvssv2))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD PARCIAL \n")
print("             - EL "+str(float(((none_availability_noneconfidentiality_iot_cvssv2*100)/(none_availability_iot_cvssv2))))+" % DE LAS VULNERABILIDADES NO TIENEN IMPACTO EN LA CONFIDENCIALIDAD DEL SISTEMA/PRODUCTO \n")
print("\n")
print("      - LOS PORCENTAJES DE IMPACTO DE INTEGRIDAD SON LOS SIGUIENTES : \n")
print("             - EL "+str(float(((none_availability_completeintegrity_iot_cvssv2*100)/(none_availability_iot_cvssv2))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD COMPLETO \n")
print("             - EL "+str(float(((none_availability_partialintegrity_iot_cvssv2*100)/(none_availability_iot_cvssv2))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD PARCIAL \n")
print("             - EL "+str(float(((none_availability_noneintegrity_iot_cvssv2*100)/(none_availability_iot_cvssv2))))+" % DE LAS VULNERABILIDADES NO TIENEN IMPACTO EN LA INTEGRIDAD DEL SISTEMA/PRODUCTO \n")











print("\n")
print("___________________________________________________________________________________________________________________________________")
print("\n")
print("\n")






print("***************************RELACION IMPACTO CONFIDENCIALIDAD/INTEGRIDAD/DISPONIBILIDAD CVSSV3 PARTE SMART HOME***************************")
print("\n")
print("\n")

#Variables donde almacenare el contador de nivel especifico de confidencialidad
complete_confidentiality_sh_cvssv2=0
#Variables donde almacenare el contador de nivel de integridad segun valor de confidencialidad dado
complete_confidentiality_partialintegrity_sh_cvssv2=0
complete_confidentiality_completeintegrity_sh_cvssv2=0
complete_confidentiality_noneintegrity_sh_cvssv2=0
#Variables donde almacenare el contador de nivel de integridad segun valor de disponibilidad  dado
complete_confidentiality_partialavailability_sh_cvssv2=0
complete_confidentiality_completeavailability_sh_cvssv2=0
complete_confidentiality_noneavailability_sh_cvssv2=0

partial_confidentiality_sh_cvssv2=0

partial_confidentiality_partialintegrity_sh_cvssv2=0
partial_confidentiality_completeintegrity_sh_cvssv2=0
partial_confidentiality_noneintegrity_sh_cvssv2=0

partial_confidentiality_partialavailability_sh_cvssv2=0
partial_confidentiality_completeavailability_sh_cvssv2=0
partial_confidentiality_noneavailability_sh_cvssv2=0


none_confidentiality_sh_cvssv2=0

none_confidentiality_partialintegrity_sh_cvssv2=0
none_confidentiality_completeintegrity_sh_cvssv2=0
none_confidentiality_noneintegrity_sh_cvssv2=0

none_confidentiality_partialavailability_sh_cvssv2=0
none_confidentiality_completeavailability_sh_cvssv2=0
none_confidentiality_noneavailability_sh_cvssv2=0

#Variables donde almacenare el contador de nivel especifico de integridad
complete_integrity_sh_cvssv2=0
#Variables donde almacenare el contador de nivel de confidencialidad segun valor de integridad dado
complete_integrity_partialconfidentiality_sh_cvssv2=0
complete_integrity_completeconfidentiality_sh_cvssv2=0
complete_integrity_noneconfidentiality_sh_cvssv2=0
#Variables donde almacenare el contador de nivel de disponibilidadd segun valor de integridad dado
complete_integrity_partialavailability_sh_cvssv2=0
complete_integrity_completeavailability_sh_cvssv2=0
complete_integrity_noneavailability_sh_cvssv2=0

partial_integrity_sh_cvssv2=0

partial_integrity_partialconfidentiality_sh_cvssv2=0
partial_integrity_completeconfidentiality_sh_cvssv2=0

partial_integrity_noneconfidentiality_sh_cvssv2=0
partial_integrity_partialavailability_sh_cvssv2=0
partial_integrity_completeavailability_sh_cvssv2=0
partial_integrity_noneavailability_sh_cvssv2=0


none_integrity_sh_cvssv2=0

none_integrity_partialconfidentiality_sh_cvssv2=0
none_integrity_completeconfidentiality_sh_cvssv2=0
none_integrity_noneconfidentiality_sh_cvssv2=0

none_integrity_partialavailability_sh_cvssv2=0
none_integrity_completeavailability_sh_cvssv2=0
none_integrity_noneavailability_sh_cvssv2=0


#Variables donde almacenare el contador de nivel especifico de disponibilidad
complete_availability_sh_cvssv2=0
#Variables donde almacenare el contador de nivel de confidencialidad segun valor de disponibilidad dado
complete_availability_partialconfidentiality_sh_cvssv2=0
complete_availability_completeconfidentiality_sh_cvssv2=0
complete_availability_noneconfidentiality_sh_cvssv2=0
#Variables donde almacenare el contador de nivel de integridad segun valor de disponibilidad dado
complete_availability_partialintegrity_sh_cvssv2=0
complete_availability_completeintegrity_sh_cvssv2=0
complete_availability_noneintegrity_sh_cvssv2=0

partial_availability_sh_cvssv2=0

partial_availability_partialconfidentiality_sh_cvssv2=0
partial_availability_completeconfidentiality_sh_cvssv2=0
partial_availability_noneconfidentiality_sh_cvssv2=0

partial_availability_partialintegrity_sh_cvssv2=0
partial_availability_completeintegrity_sh_cvssv2=0
partial_availability_noneintegrity_sh_cvssv2=0

none_availability_sh_cvssv2=0

none_availability_partialconfidentiality_sh_cvssv2=0
none_availability_completeconfidentiality_sh_cvssv2=0
none_availability_noneconfidentiality_sh_cvssv2=0

none_availability_partialintegrity_sh_cvssv2=0
none_availability_completeintegrity_sh_cvssv2=0
none_availability_noneintegrity_sh_cvssv2=0



#Recorro los distintos valores de confidencialidad y los comparo con los valores de integridad
for j in range(0,len(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.confidentialityImpact"])):
    if(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.confidentialityImpact"][j]=='COMPLETE'):
        complete_confidentiality_sh_cvssv2+=1
        if(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.integrityImpact"][j]=='COMPLETE'):
            complete_confidentiality_completeintegrity_sh_cvssv2+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.integrityImpact"][j]=='PARTIAL'):
            complete_confidentiality_partialintegrity_sh_cvssv2+=1
        else:
            complete_confidentiality_noneintegrity_sh_cvssv2+=1
            
    elif(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.confidentialityImpact"][j]=='PARTIAL'):
        partial_confidentiality_sh_cvssv2+=1
        if(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.integrityImpact"][j]=='COMPLETE'):
            partial_confidentiality_completeintegrity_sh_cvssv2+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.integrityImpact"][j]=='PARTIAL'):
            partial_confidentiality_partialintegrity_sh_cvssv2+=1
        else:
            partial_confidentiality_noneintegrity_sh_cvssv2+=1

    else:
        none_confidentiality_sh_cvssv2+=1
        if(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.integrityImpact"][j]=='COMPLETE'):
            none_confidentiality_completeintegrity_sh_cvssv2+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.integrityImpact"][j]=='PARTIAL'):
            none_confidentiality_partialintegrity_sh_cvssv2+=1
        else:
            none_confidentiality_noneintegrity_sh_cvssv2+=1
            
            
            
            
            
            
            
            
            
            
            
#Recorro los distintos valores de confidencialidad y los comparo con los valores de disponibilidad           
for h in range(0,len(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.confidentialityImpact"])):
    if(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.confidentialityImpact"][h]=='COMPLETE'):
        if(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.availabilityImpact"][h]=='COMPLETE'):
            complete_confidentiality_completeavailability_sh_cvssv2+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.availabilityImpact"][h]=='PARTIAL'):
            complete_confidentiality_partialavailability_sh_cvssv2+=1
        else:
            complete_confidentiality_noneavailability_sh_cvssv2+=1
            
    elif(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.confidentialityImpact"][h]=='PARTIAL'):
        if(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.availabilityImpact"][h]=='COMPLETE'):
            partial_confidentiality_completeavailability_sh_cvssv2+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.availabilityImpact"][h]=='PARTIAL'):
            partial_confidentiality_partialavailability_sh_cvssv2+=1
        else:
            partial_confidentiality_noneavailability_sh_cvssv2+=1

    else:
        if(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.availabilityImpact"][h]=='COMPLETE'):
            none_confidentiality_completeavailability_sh_cvssv2+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.availabilityImpact"][h]=='PARTIAL'):
            none_confidentiality_partialavailability_sh_cvssv2+=1
        else:
            none_confidentiality_noneavailability_sh_cvssv2+=1




            
            
            
#Recorro los distintos valores de disponibilidad y los comparo con los valores de integridad
for k in range(0,len(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.availabilityImpact"])):
    if(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.availabilityImpact"][k]=='COMPLETE'):
        complete_availability_sh_cvssv2+=1
        if(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.integrityImpact"][k]=='COMPLETE'):
            complete_availability_completeintegrity_sh_cvssv2+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.integrityImpact"][k]=='PARTIAL'):
            complete_availability_partialintegrity_sh_cvssv2+=1
        else:
            complete_availability_noneintegrity_sh_cvssv2+=1
            
    elif(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.availabilityImpact"][k]=='PARTIAL'):
        partial_availability_sh_cvssv2+=1
        if(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.integrityImpact"][k]=='COMPLETE'):
            partial_availability_completeintegrity_sh_cvssv2+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.integrityImpact"][k]=='PARTIAL'):
            partial_availability_partialintegrity_sh_cvssv2+=1
        else:
            partial_availability_noneintegrity_sh_cvssv2+=1
    else:
        none_availability_sh_cvssv2+=1
        if(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.integrityImpact"][k]=='COMPLETE'):
            none_availability_completeintegrity_sh_cvssv2+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.integrityImpact"][k]=='PARTIAL'):
            none_availability_partialintegrity_sh_cvssv2+=1
        else:
            none_availability_noneintegrity_sh_cvssv2+=1
            
            
            
            
#Recorro los distintos valores de disponibilidad y los comparo con los valores de confidencialidad            
for l in range(0,len(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.availabilityImpact"])):
    if(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.availabilityImpact"][l]=='COMPLETE'):
        if(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.confidentialityImpact"][l]=='COMPLETE'):
            complete_availability_completeconfidentiality_sh_cvssv2+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.confidentialityImpact"][l]=='PARTIAL'):
            complete_availability_partialconfidentiality_sh_cvssv2+=1
        else:
            complete_availability_noneconfidentiality_sh_cvssv2+=1
            
    elif(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.availabilityImpact"][l]=='PARTIAL'):
        if(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.confidentialityImpact"][l]=='COMPLETE'):
            partial_availability_completeconfidentiality_sh_cvssv2+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.confidentialityImpact"][l]=='PARTIAL'):
            partial_availability_partialconfidentiality_sh_cvssv2+=1
        else:
            partial_availability_noneconfidentiality_sh_cvssv2+=1

    else:
        if(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.confidentialityImpact"][l]=='COMPLETE'):
            none_availability_completeconfidentiality_sh_cvssv2+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.confidentialityImpact"][l]=='PARTIAL'):
            none_availability_partialconfidentiality_sh_cvssv2+=1
        else:
            none_availability_noneconfidentiality_sh_cvssv2+=1
            
            
            

#Recorro los distintos valores de integridad y los comparo con los valores de confidencialidad
for n in range(0,len(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.integrityImpact"])):
    if(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.integrityImpact"][n]=='COMPLETE'):
        complete_integrity_sh_cvssv2+=1
        if(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.confidentialityImpact"][n]=='COMPLETE'):
            complete_integrity_completeconfidentiality_sh_cvssv2+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.confidentialityImpact"][n]=='PARTIAL'):
            complete_integrity_partialconfidentiality_sh_cvssv2+=1
        else:
            complete_integrity_noneconfidentiality_sh_cvssv2+=1
            
    elif(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.integrityImpact"][n]=='PARTIAL'):
        partial_integrity_sh_cvssv2+=1
        if(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.confidentialityImpact"][n]=='COMPLETE'):
            partial_integrity_completeconfidentiality_sh_cvssv2+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.confidentialityImpact"][n]=='PARTIAL'):
            partial_integrity_partialconfidentiality_sh_cvssv2+=1
        else:
            partial_integrity_noneconfidentiality_sh_cvssv2+=1
    else:
        none_integrity_sh_cvssv2+=1
        if(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.confidentialityImpact"][n]=='COMPLETE'):
            none_integrity_completeconfidentiality_sh_cvssv2+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.confidentialityImpact"][n]=='PARTIAL'):
            none_integrity_partialconfidentiality_sh_cvssv2+=1
        else:
            none_integrity_noneconfidentiality_sh_cvssv2+=1
            
            
            
            
            
#Recorro los distintos valores de integridad y los comparo con los valores de disponibilidad            
for p in range(0,len(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.integrityImpact"])):
    if(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.integrityImpact"][p]=='COMPLETE'):
        if(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.availabilityImpact"][p]=='COMPLETE'):
            complete_integrity_completeavailability_sh_cvssv2+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.availabilityImpact"][p]=='PARTIAL'):
            complete_integrity_partialavailability_sh_cvssv2+=1
        else:
            complete_integrity_noneavailability_sh_cvssv2+=1
            
    elif(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.integrityImpact"][p]=='PARTIAL'):
        if(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.availabilityImpact"][p]=='COMPLETE'):
            partial_integrity_completeavailability_sh_cvssv2+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.availabilityImpact"][p]=='PARTIAL'):
            partial_integrity_partialavailability_sh_cvssv2+=1
        else:
            partial_integrity_noneavailability_sh_cvssv2+=1
            
    else:
        if(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.availabilityImpact"][p]=='COMPLETE'):
            none_integrity_completeavailability_sh_cvssv2+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.availabilityImpact"][p]=='PARTIAL'):
            none_integrity_partialavailability_sh_cvssv2+=1

        else:
            none_integrity_noneavailability_sh_cvssv2+=1
            
            
            
print("************************** ESTADÍSTICAS IMPACTO CONFIDENCIALIDAD/INTEGRIDAD/DISPONIBILIDAD CVSSV2 CVE SMART HOME********************************")
print("\n")
print(" DE UN TOTAL DE "+str(complete_confidentiality_sh_cvssv2+partial_confidentiality_sh_cvssv2+none_confidentiality_sh_cvssv2)+" VULNERABILIDADES, LAS ESTADÍSTICAS DE RELACION DE VALORES DE IMPACTO DE CONFIDENCIALIDAD/INTEGRIDAD/DISPONIBILIDAD SON LAS SIGUIENTES: \n")
print("\n")
print(" - DE UN TOTAL DE "+str(complete_confidentiality_sh_cvssv2)+" VULNERABILIDADES DONDE EL IMPACTO DE CONFIDENCIALIDAD ES COMPLETO \n")
print("      - LAS ESTADÍSTICAS DE IMPACTO DE INTEGRIDAD SON LAS SIGUIENTES : \n")
print("             - UN TOTAL DE "+str(complete_confidentiality_completeintegrity_sh_cvssv2)+" VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD COMPLETO \n")
print("             - UN TOTAL DE "+str(complete_confidentiality_partialintegrity_sh_cvssv2)+" VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD PARCIAL \n")
print("             - UN TOTAL DE "+str(complete_confidentiality_noneintegrity_sh_cvssv2)+" VULNERABILIDADES NO TIENEN IMPACTO EN LA INTEGRIDAD DEL SISTEMA/PRODUCTO: \n")
print("\n")
print("      - LAS ESTADÍSTICAS DE IMPACTO DE DISPONIBILIDAD SON LAS SIGUIENTES : \n")
print("             - UN TOTAL DE "+str(complete_confidentiality_completeavailability_sh_cvssv2)+" VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD COMPLETO \n")
print("             - UN TOTAL DE "+str(complete_confidentiality_partialavailability_sh_cvssv2)+" VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD PARCIAL \n")
print("             - UN TOTAL DE "+str(complete_confidentiality_noneavailability_sh_cvssv2)+" VULNERABILIDADES NO TIENEN IMPACTO EN LA DISPONIBILIDAD DEL SISTEMA/PRODUCTO: \n")

print(" - DE UN TOTAL DE "+str(partial_confidentiality_sh_cvssv2)+" VULNERABILIDADES DONDE EL IMPACTO DE CONFIDENCIALIDAD ES PARCIAL: \n")
print("      - LAS ESTADÍSTICAS DE IMPACTO DE INTEGRIDAD SON LAS SIGUIENTES : \n")
print("             - UN TOTAL DE "+str(partial_confidentiality_completeintegrity_sh_cvssv2)+" VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD COMPLETO \n")
print("             - UN TOTAL DE "+str(partial_confidentiality_partialintegrity_sh_cvssv2)+" VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD PARCIAL \n")
print("             - UN TOTAL DE "+str(partial_confidentiality_noneintegrity_sh_cvssv2)+" VULNERABILIDADES NO TIENEN IMPACTO EN LA INTEGRIDAD DEL SISTEMA/PRODUCTO: \n")
print("\n")
print("      - LAS ESTADÍSTICAS DE IMPACTO DE DISPONIBILIDAD SON LAS SIGUIENTES : \n")
print("             - UN TOTAL DE "+str(partial_confidentiality_completeavailability_sh_cvssv2)+" VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD COMPLETO \n")
print("             - UN TOTAL DE "+str(partial_confidentiality_partialavailability_sh_cvssv2)+" VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD PARCIAL \n")
print("             - UN TOTAL DE "+str(partial_confidentiality_noneavailability_sh_cvssv2)+" VULNERABILIDADES NO TIENEN IMPACTO EN LA DISPONIBILIDAD DEL SISTEMA/PRODUCTO: \n")



print(" - DE UN TOTAL DE "+str(none_confidentiality_sh_cvssv2)+" VULNERABILIDADES DONDE EL IMPACTO DE CONFIDENCIALIDAD NO TIENE EFECTO EN EL SISTEMA/PRODUCTO VULNERABLE \n")
print("      - LAS ESTADÍSTICAS DE IMPACTO DE INTEGRIDAD SON LAS SIGUIENTES : \n")
print("             - UN TOTAL DE "+str(none_confidentiality_completeintegrity_sh_cvssv2)+" VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD COMPLETO \n")
print("             - UN TOTAL DE "+str(none_confidentiality_partialintegrity_sh_cvssv2)+" VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD PARCIAL \n")
print("             - UN TOTAL DE "+str(none_confidentiality_noneintegrity_sh_cvssv2)+" VULNERABILIDADES NO TIENEN IMPACTO EN LA INTEGRIDAD DEL SISTEMA/PRODUCTO: \n")
print("\n")
print("      - LAS ESTADÍSTICAS DE IMPACTO DE DISPONIBILIDAD SON LAS SIGUIENTES : \n")
print("             - UN TOTAL DE "+str(none_confidentiality_completeavailability_sh_cvssv2)+" VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD COMPLETO \n")
print("             - UN TOTAL DE "+str(none_confidentiality_partialavailability_sh_cvssv2)+" VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD PARCIAL \n")
print("             - UN TOTAL DE "+str(none_confidentiality_noneavailability_sh_cvssv2)+" VULNERABILIDADES NO TIENEN IMPACTO EN LA DISPONIBILIDAD DEL SISTEMA/PRODUCTO: \n")

print("*************************************************************************************************************************")

print("\n")
print(" - DE UN TOTAL DE "+str(complete_availability_sh_cvssv2)+" VULNERABILIDADES DONDE EL IMPACTO DE DISPONIBILIDAD ES COMPLETO \n")
print("      - LAS ESTADÍSTICAS DE IMPACTO DE INTEGRIDAD SON LAS SIGUIENTES : \n")
print("             - UN TOTAL DE "+str(complete_availability_completeintegrity_sh_cvssv2)+" VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD COMPLETO \n")
print("             - UN TOTAL DE "+str(complete_availability_partialintegrity_sh_cvssv2)+" VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD PARCIAL \n")
print("             - UN TOTAL DE "+str(complete_availability_noneintegrity_sh_cvssv2)+" VULNERABILIDADES NO TIENEN IMPACTO EN LA INTEGRIDAD DEL SISTEMA/PRODUCTO: \n")
print("\n")
print("      - LAS ESTADÍSTICAS DE IMPACTO DE CONFIDENCIALIDAD SON LAS SIGUIENTES : \n")
print("             - UN TOTAL DE "+str(complete_availability_completeconfidentiality_sh_cvssv2)+" VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD COMPLETO \n")
print("             - UN TOTAL DE "+str(complete_availability_partialconfidentiality_sh_cvssv2)+" VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD PARCIAL \n")
print("             - UN TOTAL DE "+str(complete_availability_noneconfidentiality_sh_cvssv2)+" VULNERABILIDADES NO TIENEN IMPACTO EN LA CONFIDENCIALIDAD DEL SISTEMA/PRODUCTO: \n")
print("\n")
print(" - DE UN TOTAL DE "+str(partial_availability_sh_cvssv2)+" VULNERABILIDADES DONDE EL IMPACTO DE DISPONIBILIDAD ES PARCIAL: \n")
print("      - LAS ESTADÍSTICAS DE IMPACTO DE INTEGRIDAD SON LAS SIGUIENTES : \n")
print("             - UN TOTAL DE "+str(partial_availability_completeintegrity_sh_cvssv2)+" VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD COMPLETO \n")
print("             - UN TOTAL DE "+str(partial_availability_partialintegrity_sh_cvssv2)+" VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD PARCIAL \n")
print("             - UN TOTAL DE "+str(partial_availability_noneintegrity_sh_cvssv2)+" VULNERABILIDADES NO TIENEN IMPACTO EN LA INTEGRIDAD DEL SISTEMA/PRODUCTO: \n")
print("\n")
print("      - LAS ESTADÍSTICAS DE IMPACTO DE CONFIDENCIALIDAD SON LAS SIGUIENTES : \n")
print("             - UN TOTAL DE "+str(partial_availability_completeconfidentiality_sh_cvssv2)+" VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD COMPLETO \n")
print("             - UN TOTAL DE "+str(partial_availability_partialconfidentiality_sh_cvssv2)+" VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD PARCIAL \n")
print("             - UN TOTAL DE "+str(partial_availability_noneconfidentiality_sh_cvssv2)+" VULNERABILIDADES NO TIENEN IMPACTO EN LA CONFIDENCIALIDAD DEL SISTEMA/PRODUCTO: \n")
print("\n")

print("\n")
print(" - DE UN TOTAL DE "+str(none_availability_sh_cvssv2)+" VULNERABILIDADES DONDE EL IMPACTO DE DISPONIBILIDAD NO TIENE EFECTO EN EL SISTEMA/PRODUCTO VULNERABLE \n")
print("      - LAS ESTADÍSTICAS DE IMPACTO DE INTEGRIDAD SON LAS SIGUIENTES : \n")
print("             - UN TOTAL DE "+str(none_availability_completeintegrity_sh_cvssv2)+" VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD COMPLETO \n")
print("             - UN TOTAL DE "+str(none_availability_partialintegrity_sh_cvssv2)+" VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD PARCIAL \n")
print("             - UN TOTAL DE "+str(none_availability_noneintegrity_sh_cvssv2)+" VULNERABILIDADES NO TIENEN IMPACTO EN LA INTEGRIDAD DEL SISTEMA/PRODUCTO: \n")
print("\n")
print("      - LAS ESTADÍSTICAS DE IMPACTO DE CONFIDENCIALIDAD SON LAS SIGUIENTES : \n")
print("             - UN TOTAL DE "+str(none_availability_completeconfidentiality_sh_cvssv2)+" VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD COMPLETO \n")
print("             - UN TOTAL DE "+str(none_availability_partialconfidentiality_sh_cvssv2)+" VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD PARCIAL \n")
print("             - UN TOTAL DE "+str(none_availability_noneconfidentiality_sh_cvssv2)+" VULNERABILIDADES NO TIENEN IMPACTO EN LA CONFIDENCIALIDAD DEL SISTEMA/PRODUCTO: \n")


print("*************************************************************************************************************************")
print("\n")
print(" - DE UN TOTAL DE "+str(complete_integrity_sh_cvssv2)+" VULNERABILIDADES DONDE EL IMPACTO DE INTEGRIDAD ES COMPLETO \n")
print("      - LAS ESTADÍSTICAS DE IMPACTO DE CONFIDENCIALIDAD SON LAS SIGUIENTES : \n")
print("             - UN TOTAL DE "+str(complete_integrity_completeconfidentiality_sh_cvssv2)+" VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD COMPLETO \n")
print("             - UN TOTAL DE "+str(complete_integrity_partialconfidentiality_sh_cvssv2)+" VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD PARCIAL \n")
print("             - UN TOTAL DE "+str(complete_integrity_noneconfidentiality_sh_cvssv2)+" VULNERABILIDADES NO TIENEN IMPACTO EN LA CONFIDENCIALIDAD DEL SISTEMA/PRODUCTO: \n")
print("\n")
print("      - LAS ESTADÍSTICAS DE IMPACTO DE DISPONIBILIDAD SON LAS SIGUIENTES : \n")
print("             - UN TOTAL DE "+str(complete_integrity_completeavailability_sh_cvssv2)+" VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD COMPLETO \n")
print("             - UN TOTAL DE "+str(complete_integrity_partialavailability_sh_cvssv2)+" VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD PARCIAL \n")
print("             - UN TOTAL DE "+str(complete_integrity_noneavailability_sh_cvssv2)+" VULNERABILIDADES NO TIENEN IMPACTO EN LA DISPONIBILIDAD DEL SISTEMA/PRODUCTO: \n")

print(" - DE UN TOTAL DE "+str(partial_integrity_sh_cvssv2)+" VULNERABILIDADES DONDE EL IMPACTO DE INTEGRIDAD ES PARCIAL: \n")
print("      - LAS ESTADÍSTICAS DE IMPACTO DE CONFIDENCIALIDAD SON LAS SIGUIENTES : \n")
print("             - UN TOTAL DE "+str(partial_integrity_completeconfidentiality_sh_cvssv2)+" VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD COMPLETO \n")
print("             - UN TOTAL DE "+str(partial_integrity_partialconfidentiality_sh_cvssv2)+" VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD PARCIAL \n")
print("             - UN TOTAL DE "+str(partial_integrity_noneconfidentiality_sh_cvssv2)+" VULNERABILIDADES NO TIENEN IMPACTO EN LA CONFIDENCIALIDAD DEL SISTEMA/PRODUCTO: \n")
print("\n")
print("      - LAS ESTADÍSTICAS DE IMPACTO DE DISPONIBILIDAD SON LAS SIGUIENTES : \n")
print("             - UN TOTAL DE "+str(partial_integrity_completeavailability_sh_cvssv2)+" VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD COMPLETO \n")
print("             - UN TOTAL DE "+str(partial_integrity_partialavailability_sh_cvssv2)+" VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD PARCIAL \n")
print("             - UN TOTAL DE "+str(partial_integrity_noneavailability_sh_cvssv2)+" VULNERABILIDADES NO TIENEN IMPACTO EN LA DISPONIBILIDAD DEL SISTEMA/PRODUCTO: \n")


print(" - DE UN TOTAL DE "+str(none_integrity_sh_cvssv2)+" VULNERABILIDADES DONDE EL IMPACTO DE INTEGRIDAD NO TIENE EFECTO EN EL SISTEMA/PRODUCTO VULNERABLE \n")
print("      - LAS ESTADÍSTICAS DE IMPACTO DE CONFIDENCIALIDAD SON LAS SIGUIENTES : \n")
print("             - UN TOTAL DE "+str(none_integrity_completeconfidentiality_sh_cvssv2)+" VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD COMPLETO \n")
print("             - UN TOTAL DE "+str(none_integrity_partialconfidentiality_sh_cvssv2)+" VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD PARCIAL \n")
print("             - UN TOTAL DE "+str(none_integrity_noneconfidentiality_sh_cvssv2)+" VULNERABILIDADES NO TIENEN IMPACTO EN LA CONFIDENCIALIDAD DEL SISTEMA/PRODUCTO: \n")
print("\n")
print("      - LAS ESTADÍSTICAS DE IMPACTO DE DISPONIBILIDAD SON LAS SIGUIENTES : \n")
print("             - UN TOTAL DE "+str(none_integrity_completeavailability_sh_cvssv2)+" VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD COMPLETO \n")
print("             - UN TOTAL DE "+str(none_integrity_partialavailability_sh_cvssv2)+" VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD PARCIAL \n")
print("             - UN TOTAL DE "+str(none_integrity_noneavailability_sh_cvssv2)+" VULNERABILIDADES NO TIENEN IMPACTO EN LA DISPONIBILIDAD DEL SISTEMA/PRODUCTO: \n")



print("*************************************************************************************************************************")



total_vulnerabilities_sh_cvssv2=complete_confidentiality_sh_cvssv2+partial_confidentiality_sh_cvssv2+none_confidentiality_sh_cvssv2


print("************************** PORCENTAJE IMPACTO CONFIDENCIALIDAD/INTEGRIDAD/DISPONIBILIDAD XVSSV2 CVE SMART HOME********************************")
print("\n")
print(" DE UN TOTAL DE "+str(complete_confidentiality_sh_cvssv2+partial_confidentiality_sh_cvssv2+none_confidentiality_sh_cvssv2)+" VULNERABILIDADES, LOS PORCENTAJES DE VALORES DE RELACION DE VALORES DE IMPACTO DE CONFIDENCIALIDAD/INTEGRIDAD Y DISPONIBILIDAD SON LOS SIGUIENTES: \n")
print("\n")
print(" - EN EL  "+str(float(((complete_confidentiality_sh_cvssv2*100)/(total_vulnerabilities_sh_cvssv2))))+" % DE LAS VULNERABILIDADES, DONDE EL IMPACTO DE CONFIDENCIALIDAD ES COMPLETO \n")
print("      - LOS PORCENTAJES DE IMPACTO DE INTEGRIDAD SON LOS SIGUIENTES : \n")
print("             - EL "+str(float(((complete_confidentiality_completeintegrity_sh_cvssv2*100)/(complete_confidentiality_sh_cvssv2))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD COMPLETO \n")
print("             - EL "+str(float(((complete_confidentiality_partialintegrity_sh_cvssv2*100)/(complete_confidentiality_sh_cvssv2))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD PARCIAL \n")
print("             - EL "+str(float(((complete_confidentiality_noneintegrity_sh_cvssv2*100)/(complete_confidentiality_sh_cvssv2))))+" % DE LAS VULNERABILIDADES NO TIENEN IMPACTO EN LA INTEGRIDAD DEL SISTEMA/PRODUCTO \n")
print("\n")
print("      - LOS PORCENTAJES DE IMPACTO DE DISPONIBILIDAD SON LOS SIGUIENTES : \n")
print("             - EL "+str(float(((complete_confidentiality_completeavailability_sh_cvssv2*100)/(complete_confidentiality_sh_cvssv2))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD COMPLETO \n")
print("             - EL "+str(float(((complete_confidentiality_partialavailability_sh_cvssv2*100)/(complete_confidentiality_sh_cvssv2))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD PARCIAL \n")
print("             - EL "+str(float(((complete_confidentiality_noneavailability_sh_cvssv2*100)/(complete_confidentiality_sh_cvssv2))))+" % DE LAS VULNERABILIDADES NO TIENEN IMPACTO EN LA DISPONIBILIDAD DEL SISTEMA/PRODUCTO \n")

print("\n")
print(" - EN EL  "+str(float(((partial_confidentiality_sh_cvssv2*100)/(total_vulnerabilities_sh_cvssv2))))+" % DE LAS VULNERABILIDADES, DONDE EL IMPACTO DE CONFIDENCIALIDAD ES PARCIAL: \n")
print("      - LOS PORCENTAJES DE IMPACTO DE INTEGRIDAD SON LOS SIGUIENTES : \n")
print("             - EL "+str(float(((complete_confidentiality_completeintegrity_sh_cvssv2*100)/(complete_confidentiality_sh_cvssv2))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD COMPLETO \n")
print("             - EL "+str(float(((complete_confidentiality_partialintegrity_sh_cvssv2*100)/(complete_confidentiality_sh_cvssv2))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD PARCIAL \n")
print("             - EL "+str(float(((complete_confidentiality_noneintegrity_sh_cvssv2*100)/(complete_confidentiality_sh_cvssv2))))+" % DE LAS VULNERABILIDADES NO TIENEN IMPACTO EN LA INTEGRIDAD DEL SISTEMA/PRODUCTO \n")
print("\n")
print("      - LOS PORCENTAJES DE IMPACTO DE DISPONIBILIDAD SON LOS SIGUIENTES : \n")
print("             - EL "+str(float(((complete_confidentiality_completeavailability_sh_cvssv2*100)/(complete_confidentiality_sh_cvssv2))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD COMPLETO \n")
print("             - EL "+str(float(((complete_confidentiality_partialavailability_sh_cvssv2*100)/(complete_confidentiality_sh_cvssv2))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD PARCIAL \n")
print("             - EL "+str(float(((complete_confidentiality_noneavailability_sh_cvssv2*100)/(complete_confidentiality_sh_cvssv2))))+" % DE LAS VULNERABILIDADES NO TIENEN IMPACTO EN LA DISPONIBILIDAD DEL SISTEMA/PRODUCTO \n")


print("\n")
print(" - EN EL  "+str(float(((none_confidentiality_sh_cvssv2*100)/(total_vulnerabilities_sh_cvssv2))))+" % DE LAS VULNERABILIDADES, DONDE EL IMPACTO DE CONFIDENCIALIDAD NO TIENE EFECTO EN EL SISTEMA/PRODUCTO VULNERABLE \n")
print("      - LOS PORCENTAJES DE IMPACTO DE INTEGRIDAD SON LOS SIGUIENTES : \n")
print("             - EL "+str(float(((complete_confidentiality_completeintegrity_sh_cvssv2*100)/(complete_confidentiality_sh_cvssv2))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD COMPLETO \n")
print("             - EL "+str(float(((complete_confidentiality_partialintegrity_sh_cvssv2*100)/(complete_confidentiality_sh_cvssv2))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD PARCIAL \n")
print("             - EL "+str(float(((complete_confidentiality_noneintegrity_sh_cvssv2*100)/(complete_confidentiality_sh_cvssv2))))+" % DE LAS VULNERABILIDADES NO TIENEN IMPACTO EN LA INTEGRIDAD DEL SISTEMA/PRODUCTO \n")
print("\n")
print("      - LOS PORCENTAJES DE IMPACTO DE DISPONIBILIDAD SON LOS SIGUIENTES : \n")
print("             - EL "+str(float(((complete_confidentiality_completeavailability_sh_cvssv2*100)/(complete_confidentiality_sh_cvssv2))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD COMPLETO \n")
print("             - EL "+str(float(((complete_confidentiality_partialavailability_sh_cvssv2*100)/(complete_confidentiality_sh_cvssv2))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD PARCIAL \n")
print("             - EL "+str(float(((complete_confidentiality_noneavailability_sh_cvssv2*100)/(complete_confidentiality_sh_cvssv2))))+" % DE LAS VULNERABILIDADES NO TIENEN IMPACTO EN LA DISPONIBILIDAD DEL SISTEMA/PRODUCTO \n")



print("*************************************************************************************************************************")


print("\n")
print(" - EN EL  "+str(float(((complete_integrity_sh_cvssv2*100)/(total_vulnerabilities_sh_cvssv2))))+" % DE LAS VULNERABILIDADES, DONDE EL IMPACTO DE INTEGRIDAD ES COMPLETO \n")
print("      - LOS PORCENTAJES DE IMPACTO DE CONFIDENCIALIDAD SON LOS SIGUIENTES : \n")
print("             - EL "+str(float(((complete_integrity_completeconfidentiality_sh_cvssv2*100)/(complete_integrity_sh_cvssv2))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD COMPLETO \n")
print("             - EL "+str(float(((complete_integrity_partialconfidentiality_sh_cvssv2*100)/(complete_integrity_sh_cvssv2))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD PARCIAL \n")
print("             - EL "+str(float(((complete_integrity_noneconfidentiality_sh_cvssv2*100)/(complete_integrity_sh_cvssv2))))+" % DE LAS VULNERABILIDADES NO TIENEN IMPACTO EN LA CONFIDENCIALIDAD DEL SISTEMA/PRODUCTO \n")
print("\n")
print("      - LOS PORCENTAJES DE IMPACTO DE DISPONIBILIDAD SON LOS SIGUIENTES : \n")
print("             - EL "+str(float(((complete_integrity_completeavailability_sh_cvssv2*100)/(complete_integrity_sh_cvssv2))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD COMPLETO \n")
print("             - EL "+str(float(((complete_integrity_partialavailability_sh_cvssv2*100)/(complete_integrity_sh_cvssv2))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD PARCIAL \n")
print("             - EL "+str(float(((complete_integrity_noneavailability_sh_cvssv2*100)/(complete_integrity_sh_cvssv2))))+" % DE LAS VULNERABILIDADES NO TIENEN IMPACTO EN LA DISPONIBILIDAD DEL SISTEMA/PRODUCTO \n")




print("\n")
print(" - EN EL  "+str(float(((partial_integrity_sh_cvssv2*100)/(total_vulnerabilities_sh_cvssv2))))+" % DE LAS VULNERABILIDADES, DONDE EL IMPACTO DE INTEGRIDAD ES PARCIAL: \n")
print("      - LOS PORCENTAJES DE IMPACTO DE CONFIDENCIALIDAD SON LOS SIGUIENTES : \n")
print("             - EL "+str(float(((partial_integrity_completeconfidentiality_sh_cvssv2*100)/(partial_integrity_sh_cvssv2))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD COMPLETO \n")
print("             - EL "+str(float(((partial_integrity_partialconfidentiality_sh_cvssv2*100)/(partial_integrity_sh_cvssv2))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD PARCIAL \n")
print("             - EL "+str(float(((partial_integrity_noneconfidentiality_sh_cvssv2*100)/(partial_integrity_sh_cvssv2))))+" % DE LAS VULNERABILIDADES NO TIENEN IMPACTO EN LA CONFIDENCIALIDAD DEL SISTEMA/PRODUCTO \n")
print("\n")
print("      - LOS PORCENTAJES DE IMPACTO DE DISPONIBILIDAD SON LOS SIGUIENTES : \n")
print("             - EL "+str(float(((partial_integrity_completeavailability_sh_cvssv2*100)/(partial_integrity_sh_cvssv2))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD COMPLETO \n")
print("             - EL "+str(float(((partial_integrity_partialavailability_sh_cvssv2*100)/(partial_integrity_sh_cvssv2))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD PARCIAL \n")
print("             - EL "+str(float(((partial_integrity_noneavailability_sh_cvssv2*100)/(partial_integrity_sh_cvssv2))))+" % DE LAS VULNERABILIDADES NO TIENEN IMPACTO EN LA DISPONIBILIDAD DEL SISTEMA/PRODUCTO \n")




print("\n")
print(" - EN EL  "+str(float(((none_integrity_sh_cvssv2*100)/(total_vulnerabilities_sh_cvssv2))))+" % DE LAS VULNERABILIDADES, DONDE EL IMPACTO DE INTEGRIDAD NO TIENE EFECTO EN EL SISTEMA/PRODUCTO VULNERABLE \n")
print("      - LOS PORCENTAJES DE IMPACTO DE CONFIDENCIALIDAD SON LOS SIGUIENTES : \n")
print("             - EL "+str(float(((none_integrity_completeconfidentiality_sh_cvssv2*100)/(none_integrity_sh_cvssv2))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD COMPLETO \n")
print("             - EL "+str(float(((none_integrity_partialconfidentiality_sh_cvssv2*100)/(none_integrity_sh_cvssv2))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD PARCIAL \n")
print("             - EL "+str(float(((none_integrity_noneconfidentiality_sh_cvssv2*100)/(none_integrity_sh_cvssv2))))+" % DE LAS VULNERABILIDADES NO TIENEN IMPACTO EN LA CONFIDENCIALIDAD DEL SISTEMA/PRODUCTO \n")
print("\n")
print("      - LOS PORCENTAJES DE IMPACTO DE DISPONIBILIDAD SON LOS SIGUIENTES : \n")
print("             - EL "+str(float(((none_integrity_completeavailability_sh_cvssv2*100)/(none_integrity_sh_cvssv2))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD COMPLETO \n")
print("             - EL "+str(float(((none_integrity_partialavailability_sh_cvssv2*100)/(none_integrity_sh_cvssv2))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD PARCIAL \n")
print("             - EL "+str(float(((none_integrity_noneavailability_sh_cvssv2*100)/(none_integrity_sh_cvssv2))))+" % DE LAS VULNERABILIDADES NO TIENEN IMPACTO EN LA DISPONIBILIDAD DEL SISTEMA/PRODUCTO \n")



print("*************************************************************************************************************************")


print("\n")
print(" - EN EL  "+str(float(((complete_availability_sh_cvssv2*100)/(total_vulnerabilities_sh_cvssv2))))+" % DE LAS VULNERABILIDADES, DONDE EL IMPACTO DE DISPONIBILIDAD ES COMPLETO \n")
print("      - LOS PORCENTAJES DE IMPACTO DE CONFIDENCIALIDAD SON LOS SIGUIENTES : \n")
print("             - EL "+str(float(((complete_availability_completeconfidentiality_sh_cvssv2*100)/(complete_availability_sh_cvssv2))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD COMPLETO \n")
print("             - EL "+str(float(((complete_availability_partialconfidentiality_sh_cvssv2*100)/(complete_availability_sh_cvssv2))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD PARCIAL \n")
print("             - EL "+str(float(((complete_availability_noneconfidentiality_sh_cvssv2*100)/(complete_availability_sh_cvssv2))))+" % DE LAS VULNERABILIDADES NO TIENEN IMPACTO EN LA CONFIDENCIALIDAD DEL SISTEMA/PRODUCTO \n")
print("\n")
print("      - LOS PORCENTAJES DE IMPACTO DE INTEGRIDAD SON LOS SIGUIENTES : \n")
print("             - EL "+str(float(((complete_availability_completeintegrity_sh_cvssv2*100)/(complete_availability_sh_cvssv2))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD COMPLETO \n")
print("             - EL "+str(float(((complete_availability_partialintegrity_sh_cvssv2*100)/(complete_availability_sh_cvssv2))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD PARCIAL \n")
print("             - EL "+str(float(((complete_availability_noneintegrity_sh_cvssv2*100)/(complete_availability_sh_cvssv2))))+" % DE LAS VULNERABILIDADES NO TIENEN IMPACTO EN LA INTEGRIDAD DEL SISTEMA/PRODUCTO \n")


print("\n")
print(" - EN EL  "+str(float(((partial_availability_sh_cvssv2*100)/(total_vulnerabilities_sh_cvssv2))))+" % DE LAS VULNERABILIDADES, DONDE EL IMPACTO DE DISPONIBILIDAD ES PARCIAL: \n")
print("      - LOS PORCENTAJES DE IMPACTO DE CONFIDENCIALIDAD SON LOS SIGUIENTES : \n")
print("             - EL "+str(float(((partial_availability_completeconfidentiality_sh_cvssv2*100)/(partial_availability_sh_cvssv2))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD COMPLETO \n")
print("             - EL "+str(float(((partial_availability_partialconfidentiality_sh_cvssv2*100)/(partial_availability_sh_cvssv2))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD PARCIAL \n")
print("             - EL "+str(float(((partial_availability_noneconfidentiality_sh_cvssv2*100)/(partial_availability_sh_cvssv2))))+" % DE LAS VULNERABILIDADES NO TIENEN IMPACTO EN LA CONFIDENCIALIDAD DEL SISTEMA/PRODUCTO \n")
print("\n")
print("      - LOS PORCENTAJES DE IMPACTO DE INTEGRIDAD SON LOS SIGUIENTES : \n")
print("             - EL "+str(float(((partial_availability_completeintegrity_sh_cvssv2*100)/(partial_availability_sh_cvssv2))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD COMPLETO \n")
print("             - EL "+str(float(((partial_availability_partialintegrity_sh_cvssv2*100)/(partial_availability_sh_cvssv2))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD PARCIAL \n")
print("             - EL "+str(float(((partial_availability_noneintegrity_sh_cvssv2*100)/(partial_availability_sh_cvssv2))))+" % DE LAS VULNERABILIDADES NO TIENEN IMPACTO EN LA INTEGRIDAD DEL SISTEMA/PRODUCTO \n")



print("\n")
print(" - EN EL  "+str(float(((none_availability_sh_cvssv2*100)/(total_vulnerabilities_sh_cvssv2))))+" % DE LAS VULNERABILIDADES, DONDE EL IMPACTO DE DISPONIBILIDAD NO TIENE EFECTO EN EL SISTEMA/PRODUCTO VULNERABLE \n")
print("      - LOS PORCENTAJES DE IMPACTO DE CONFIDENCIALIDAD SON LOS SIGUIENTES : \n")
print("             - EL "+str(float(((none_availability_completeconfidentiality_sh_cvssv2*100)/(none_availability_sh_cvssv2))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD COMPLETO \n")
print("             - EL "+str(float(((none_availability_partialconfidentiality_sh_cvssv2*100)/(none_availability_sh_cvssv2))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD PARCIAL \n")
print("             - EL "+str(float(((none_availability_noneconfidentiality_sh_cvssv2*100)/(none_availability_sh_cvssv2))))+" % DE LAS VULNERABILIDADES NO TIENEN IMPACTO EN LA CONFIDENCIALIDAD DEL SISTEMA/PRODUCTO \n")
print("\n")
print("      - LOS PORCENTAJES DE IMPACTO DE INTEGRIDAD SON LOS SIGUIENTES : \n")
print("             - EL "+str(float(((none_availability_completeintegrity_sh_cvssv2*100)/(none_availability_sh_cvssv2))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD COMPLETO \n")
print("             - EL "+str(float(((none_availability_partialintegrity_sh_cvssv2*100)/(none_availability_sh_cvssv2))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD PARCIAL \n")
print("             - EL "+str(float(((none_availability_noneintegrity_sh_cvssv2*100)/(none_availability_sh_cvssv2))))+" % DE LAS VULNERABILIDADES NO TIENEN IMPACTO EN LA INTEGRIDAD DEL SISTEMA/PRODUCTO \n")



print("\n")
print("___________________________________________________________________________________________________________________________________")
print("\n")
print("\n")



print("**************************ESTADÍSTICAS IMPACTO CONFIDENCIALIDAD/INTEGRIDAD/DISPONIBILIDAD CVSSV2 CVE IOT Y SMART HOME CONJUNTAMENTE********************************")
print("\n")
print(" DE UN TOTAL DE "+str(complete_confidentiality_sh_cvssv2+partial_confidentiality_sh_cvssv2+none_confidentiality_sh_cvssv2+complete_confidentiality_iot_cvssv2+partial_confidentiality_iot_cvssv2+none_confidentiality_iot_cvssv2)+" VULNERABILIDADES, LAS ESTADÍSTICAS DE VALORES DE CONFIDENCIALIDAD/INTEGRIDAD/DISPONIBILIDAD SON LAS SIGUIENTES: \n")
print("\n")
print(" - DE UN TOTAL DE "+str(complete_confidentiality_sh_cvssv2+complete_confidentiality_iot_cvssv2)+" VULNERABILIDADES DONDE EL IMPACTO DE CONFIDENCIALIDAD ES COMPLETO \n")
print("      - LAS ESTADÍSTICAS DE IMPACTO DE INTEGRIDAD SON LAS SIGUIENTES : \n")
print("             - UN TOTAL DE "+str(complete_confidentiality_completeintegrity_sh_cvssv2+complete_confidentiality_completeintegrity_iot_cvssv2)+" VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD COMPLETO \n")
print("             - UN TOTAL DE "+str(complete_confidentiality_partialintegrity_sh_cvssv2+complete_confidentiality_partialintegrity_iot_cvssv2)+" VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD PARCIAL \n")
print("             - UN TOTAL DE "+str(complete_confidentiality_noneintegrity_sh_cvssv2+complete_confidentiality_noneintegrity_iot_cvssv2)+" VULNERABILIDADES NO TIENEN IMPACTO EN LA INTEGRIDAD DEL SISTEMA/PRODUCTO: \n")
print("\n")
print("      - LAS ESTADÍSTICAS DE IMPACTO DE DISPONIBILIDAD SON LAS SIGUIENTES : \n")
print("             - UN TOTAL DE "+str(complete_confidentiality_completeavailability_sh_cvssv2+complete_confidentiality_completeavailability_iot_cvssv2)+" VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD COMPLETO \n")
print("             - UN TOTAL DE "+str(complete_confidentiality_partialavailability_sh_cvssv2+complete_confidentiality_partialavailability_iot_cvssv2)+" VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD PARCIAL \n")
print("             - UN TOTAL DE "+str(complete_confidentiality_noneavailability_sh_cvssv2+complete_confidentiality_noneavailability_iot_cvssv2)+" VULNERABILIDADES NO TIENEN IMPACTO EN LA DISPONIBILIDAD DEL SISTEMA/PRODUCTO: \n")


print("\n")
print(" - DE UN TOTAL DE "+str(partial_confidentiality_sh_cvssv2+partial_confidentiality_iot_cvssv2)+" VULNERABILIDADES DONDE EL IMPACTO DE CONFIDENCIALIDAD ES PARCIAL: \n")
print("      - LAS ESTADÍSTICAS DE IMPACTO DE INTEGRIDAD SON LAS SIGUIENTES : \n")
print("             - UN TOTAL DE "+str(partial_confidentiality_completeintegrity_sh_cvssv2+partial_confidentiality_completeintegrity_iot_cvssv2)+" VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD COMPLETO \n")
print("             - UN TOTAL DE "+str(partial_confidentiality_partialintegrity_sh_cvssv2+partial_confidentiality_partialintegrity_iot_cvssv2)+" VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD PARCIAL \n")
print("             - UN TOTAL DE "+str(partial_confidentiality_noneintegrity_sh_cvssv2+partial_confidentiality_noneintegrity_iot_cvssv2)+" VULNERABILIDADES NO TIENEN IMPACTO EN LA INTEGRIDAD DEL SISTEMA/PRODUCTO: \n")
print("\n")
print("      - LAS ESTADÍSTICAS DE IMPACTO DE DISPONIBILIDAD SON LAS SIGUIENTES : \n")
print("             - UN TOTAL DE "+str(partial_confidentiality_completeavailability_sh_cvssv2+partial_confidentiality_completeavailability_iot_cvssv2)+" VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD COMPLETO \n")
print("             - UN TOTAL DE "+str(partial_confidentiality_partialavailability_sh_cvssv2+partial_confidentiality_partialavailability_iot_cvssv2)+" VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD PARCIAL \n")
print("             - UN TOTAL DE "+str(partial_confidentiality_noneavailability_sh_cvssv2+partial_confidentiality_noneavailability_iot_cvssv2)+" VULNERABILIDADES NO TIENEN IMPACTO EN LA DISPONIBILIDAD DEL SISTEMA/PRODUCTO: \n")


print("\n")
print(" - DE UN TOTAL DE "+str(none_confidentiality_sh_cvssv2+none_confidentiality_iot_cvssv2)+" VULNERABILIDADES DONDE EL IMPACTO DE CONFIDENCIALIDAD NO TIENE EFECTO EN EL SISTEMA/PRODUCTO VULNERABLE \n")
print("      - LAS ESTADÍSTICAS DE IMPACTO DE INTEGRIDAD SON LAS SIGUIENTES : \n")
print("             - UN TOTAL DE "+str(none_confidentiality_completeintegrity_sh_cvssv2+none_confidentiality_completeintegrity_iot_cvssv2)+" VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD COMPLETO \n")
print("             - UN TOTAL DE "+str(none_confidentiality_partialintegrity_sh_cvssv2+none_confidentiality_partialintegrity_iot_cvssv2)+" VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD PARCIAL \n")
print("             - UN TOTAL DE "+str(none_confidentiality_noneintegrity_sh_cvssv2+none_confidentiality_noneintegrity_iot_cvssv2)+" VULNERABILIDADES NO TIENEN IMPACTO EN LA INTEGRIDAD DEL SISTEMA/PRODUCTO: \n")
print("\n")
print("      - LAS ESTADÍSTICAS DE IMPACTO DE DISPONIBILIDAD SON LAS SIGUIENTES : \n")
print("             - UN TOTAL DE "+str(none_confidentiality_completeavailability_sh_cvssv2+none_confidentiality_completeavailability_iot_cvssv2)+" VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD COMPLETO \n")
print("             - UN TOTAL DE "+str(none_confidentiality_partialavailability_sh_cvssv2+none_confidentiality_partialavailability_iot_cvssv2)+" VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD PARCIAL \n")
print("             - UN TOTAL DE "+str(none_confidentiality_noneavailability_sh_cvssv2+none_confidentiality_noneavailability_iot_cvssv2)+" VULNERABILIDADES NO TIENEN IMPACTO EN LA DISPONIBILIDAD DEL SISTEMA/PRODUCTO: \n")




print("*************************************************************************************************************************")




print("\n")
print(" - DE UN TOTAL DE "+str(complete_integrity_sh_cvssv2+complete_integrity_iot_cvssv2)+" VULNERABILIDADES DONDE EL IMPACTO DE INTEGRIDAD ES COMPLETO \n")
print("      - LAS ESTADÍSTICAS DE IMPACTO DE CONFIDENCIALIDAD SON LAS SIGUIENTES : \n")
print("             - UN TOTAL DE "+str(complete_integrity_completeconfidentiality_sh_cvssv2+complete_integrity_completeconfidentiality_iot_cvssv2)+" VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD COMPLETO \n")
print("             - UN TOTAL DE "+str(complete_integrity_partialconfidentiality_sh_cvssv2+complete_integrity_partialconfidentiality_iot_cvssv2)+" VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD PARCIAL \n")
print("             - UN TOTAL DE "+str(complete_integrity_noneconfidentiality_sh_cvssv2+complete_integrity_noneconfidentiality_iot_cvssv2)+" VULNERABILIDADES NO TIENEN IMPACTO EN LA CONFIDENCIALIDAD DEL SISTEMA/PRODUCTO: \n")
print("\n")
print("      - LAS ESTADÍSTICAS DE IMPACTO DE DISPONIBILIDAD SON LAS SIGUIENTES : \n")
print("             - UN TOTAL DE "+str(complete_integrity_completeavailability_sh_cvssv2+complete_integrity_completeavailability_iot_cvssv2)+" VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD COMPLETO \n")
print("             - UN TOTAL DE "+str(complete_integrity_partialavailability_sh_cvssv2+complete_integrity_partialavailability_iot_cvssv2)+" VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD PARCIAL \n")
print("             - UN TOTAL DE "+str(complete_integrity_noneavailability_sh_cvssv2+complete_integrity_noneavailability_iot_cvssv2)+" VULNERABILIDADES NO TIENEN IMPACTO EN LA DISPONIBILIDAD DEL SISTEMA/PRODUCTO: \n")



print("\n")
print(" - DE UN TOTAL DE "+str(partial_integrity_sh_cvssv2+partial_integrity_iot_cvssv2)+" VULNERABILIDADES DONDE EL IMPACTO DE INTEGRIDAD ES PARCIAL: \n")
print("      - LAS ESTADÍSTICAS DE IMPACTO DE CONFIDENCIALIDAD SON LAS SIGUIENTES : \n")
print("             - UN TOTAL DE "+str(partial_integrity_completeconfidentiality_sh_cvssv2+partial_integrity_completeconfidentiality_iot_cvssv2)+" VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD COMPLETO \n")
print("             - UN TOTAL DE "+str(partial_integrity_partialconfidentiality_sh_cvssv2+partial_integrity_partialconfidentiality_iot_cvssv2)+" VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD PARCIAL \n")
print("             - UN TOTAL DE "+str(partial_integrity_noneconfidentiality_sh_cvssv2+partial_integrity_noneconfidentiality_iot_cvssv2)+" VULNERABILIDADES NO TIENEN IMPACTO EN LA CONFIDENCIALIDAD DEL SISTEMA/PRODUCTO: \n")
print("\n")
print("      - LAS ESTADÍSTICAS DE IMPACTO DE DISPONIBILIDAD SON LAS SIGUIENTES : \n")
print("             - UN TOTAL DE "+str(partial_integrity_completeavailability_sh_cvssv2+partial_integrity_completeavailability_iot_cvssv2)+" VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD COMPLETO \n")
print("             - UN TOTAL DE "+str(partial_integrity_partialavailability_sh_cvssv2+partial_integrity_partialavailability_iot_cvssv2)+" VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD PARCIAL \n")
print("             - UN TOTAL DE "+str(partial_integrity_noneavailability_sh_cvssv2+partial_integrity_noneavailability_iot_cvssv2)+" VULNERABILIDADES NO TIENEN IMPACTO EN LA DISPONIBILIDAD DEL SISTEMA/PRODUCTO: \n")


print("\n")
print(" - DE UN TOTAL DE "+str(none_integrity_sh_cvssv2+none_integrity_iot_cvssv2)+" VULNERABILIDADES DONDE EL IMPACTO DE INTEGRIDAD NO TIENE EFECTO EN EL SISTEMA/PRODUCTO VULNERABLE \n")
print("      - LAS ESTADÍSTICAS DE IMPACTO DE CONFIDENCIALIDAD SON LAS SIGUIENTES : \n")
print("             - UN TOTAL DE "+str(none_integrity_completeconfidentiality_sh_cvssv2+none_integrity_completeconfidentiality_iot_cvssv2)+" VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD COMPLETO \n")
print("             - UN TOTAL DE "+str(none_integrity_partialconfidentiality_sh_cvssv2+none_integrity_partialconfidentiality_iot_cvssv2)+" VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD PARCIAL \n")
print("             - UN TOTAL DE "+str(none_integrity_noneconfidentiality_sh_cvssv2+none_integrity_noneconfidentiality_iot_cvssv2)+" VULNERABILIDADES NO TIENEN IMPACTO EN LA CONFIDENCIALIDAD DEL SISTEMA/PRODUCTO: \n")
print("\n")
print("      - LAS ESTADÍSTICAS DE IMPACTO DE DISPONIBILIDAD SON LAS SIGUIENTES : \n")
print("             - UN TOTAL DE "+str(none_integrity_completeavailability_sh_cvssv2+none_integrity_completeavailability_iot_cvssv2)+" VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD COMPLETO \n")
print("             - UN TOTAL DE "+str(none_integrity_partialavailability_sh_cvssv2+none_integrity_partialavailability_iot_cvssv2)+" VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD PARCIAL \n")
print("             - UN TOTAL DE "+str(none_integrity_noneavailability_sh_cvssv2+none_integrity_noneavailability_iot_cvssv2)+" VULNERABILIDADES NO TIENEN IMPACTO EN LA DISPONIBILIDAD DEL SISTEMA/PRODUCTO: \n")



print("*************************************************************************************************************************")


print("\n")
print(" - DE UN TOTAL DE "+str(complete_availability_sh_cvssv2+complete_availability_iot_cvssv2)+" VULNERABILIDADES DONDE EL IMPACTO DE DISPONIBILIDAD ES COMPLETO \n")
print("      - LAS ESTADÍSTICAS DE IMPACTO DE CONFIDENCIALIDAD SON LAS SIGUIENTES : \n")
print("             - UN TOTAL DE "+str(complete_availability_completeconfidentiality_sh_cvssv2+complete_availability_completeconfidentiality_iot_cvssv2)+" VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD COMPLETO \n")
print("             - UN TOTAL DE "+str(complete_availability_partialconfidentiality_sh_cvssv2+complete_availability_partialconfidentiality_iot_cvssv2)+" VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD PARCIAL \n")
print("             - UN TOTAL DE "+str(complete_availability_noneconfidentiality_sh_cvssv2+complete_availability_noneconfidentiality_iot_cvssv2)+" VULNERABILIDADES NO TIENEN IMPACTO EN LA CONFIDENCIALIDAD DEL SISTEMA/PRODUCTO: \n")
print("\n")
print("      - LAS ESTADÍSTICAS DE IMPACTO DE INTEGRIDAD SON LAS SIGUIENTES : \n")
print("             - UN TOTAL DE "+str(complete_availability_completeintegrity_sh_cvssv2+complete_availability_completeintegrity_iot_cvssv2)+" VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD COMPLETO \n")
print("             - UN TOTAL DE "+str(complete_availability_partialintegrity_sh_cvssv2+complete_availability_partialintegrity_iot_cvssv2)+" VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD PARCIAL \n")
print("             - UN TOTAL DE "+str(complete_availability_noneintegrity_sh_cvssv2+complete_availability_noneintegrity_iot_cvssv2)+" VULNERABILIDADES NO TIENEN IMPACTO EN LA INTEGRIDAD DEL SISTEMA/PRODUCTO: \n")




print("\n")
print(" - DE UN TOTAL DE "+str(partial_availability_sh_cvssv2+partial_availability_iot_cvssv2)+" VULNERABILIDADES DONDE EL IMPACTO DE DISPONIBILIDAD ES PARCIAL: \n")
print("      - LAS ESTADÍSTICAS DE IMPACTO DE CONFIDENCIALIDAD SON LAS SIGUIENTES : \n")
print("             - UN TOTAL DE "+str(partial_availability_completeconfidentiality_sh_cvssv2+partial_availability_completeconfidentiality_iot_cvssv2)+" VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD COMPLETO \n")
print("             - UN TOTAL DE "+str(partial_availability_partialconfidentiality_sh_cvssv2+partial_availability_partialconfidentiality_iot_cvssv2)+" VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD PARCIAL \n")
print("             - UN TOTAL DE "+str(partial_availability_noneconfidentiality_sh_cvssv2+partial_availability_noneconfidentiality_iot_cvssv2)+" VULNERABILIDADES NO TIENEN IMPACTO EN LA CONFIDENCIALIDAD DEL SISTEMA/PRODUCTO: \n")
print("\n")
print("      - LAS ESTADÍSTICAS DE IMPACTO DE INTEGRIDAD SON LAS SIGUIENTES : \n")
print("             - UN TOTAL DE "+str(partial_availability_completeintegrity_sh_cvssv2+partial_availability_completeintegrity_iot_cvssv2)+" VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD COMPLETO \n")
print("             - UN TOTAL DE "+str(partial_availability_partialintegrity_sh_cvssv2+partial_availability_partialintegrity_iot_cvssv2)+" VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD PARCIAL \n")
print("             - UN TOTAL DE "+str(partial_availability_noneintegrity_sh_cvssv2+partial_availability_noneintegrity_iot_cvssv2)+" VULNERABILIDADES NO TIENEN IMPACTO EN LA INTEGRIDAD DEL SISTEMA/PRODUCTO: \n")



print("\n")
print(" - DE UN TOTAL DE "+str(none_availability_sh_cvssv2+none_availability_iot_cvssv2)+" VULNERABILIDADES DONDE EL IMPACTO DE DISPONIBILIDAD NO TIENE EFECTO EN EL SISTEMA/PRODUCTO VULNERABLE \n")
print("      - LAS ESTADÍSTICAS DE IMPACTO DE CONFIDENCIALIDAD SON LAS SIGUIENTES : \n")
print("             - UN TOTAL DE "+str(none_availability_completeconfidentiality_sh_cvssv2+none_availability_completeconfidentiality_iot_cvssv2)+" VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD COMPLETO \n")
print("             - UN TOTAL DE "+str(none_availability_partialconfidentiality_sh_cvssv2+none_availability_partialconfidentiality_iot_cvssv2)+" VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD PARCIAL \n")
print("             - UN TOTAL DE "+str(none_availability_noneconfidentiality_sh_cvssv2+none_availability_noneconfidentiality_iot_cvssv2)+" VULNERABILIDADES NO TIENEN IMPACTO EN LA CONFIDENCIALIDAD DEL SISTEMA/PRODUCTO: \n")
print("\n")
print("      - LAS ESTADÍSTICAS DE IMPACTO DE INTEGRIDAD SON LAS SIGUIENTES : \n")
print("             - UN TOTAL DE "+str(none_availability_completeintegrity_sh_cvssv2+none_availability_completeintegrity_iot_cvssv2)+" VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD COMPLETO \n")
print("             - UN TOTAL DE "+str(none_availability_partialintegrity_sh_cvssv2+none_availability_partialintegrity_iot_cvssv2)+" VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD PARCIAL \n")
print("             - UN TOTAL DE "+str(none_availability_noneintegrity_sh_cvssv2+none_availability_noneintegrity_iot_cvssv2)+" VULNERABILIDADES NO TIENEN IMPACTO EN LA INTEGRIDAD DEL SISTEMA/PRODUCTO: \n")



















total_vulnerabilities_cvssv2=len(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.availabilityImpact"])+len(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.availabilityImpact"])


print("************************** PORCENTAJES IMPACTO CONFIDENCIALIDAD/INTEGRIDAD/DISPONIBILIDAD CVSSV2 CVE PARTE IOT Y SMART HOME CONJUNTAMENTE********************************")
print("\n")
print(" DE UN TOTAL DE "+str(total_vulnerabilities_cvssv2)+" VULNERABILIDADES, LOS PORCENTAJES DE VALORES DE CONFIDENCIALIDAD/INTEGRIDAD/DISPONIBILIDAD SON LOS SIGUIENTES: \n")
print("\n")
print(" - EN EL  "+str(float((((complete_confidentiality_sh_cvssv2+complete_confidentiality_iot_cvssv2)*100)/(total_vulnerabilities_cvssv2))))+" % DE LAS VULNERABILIDADES, DONDE EL IMPACTO DE CONFIDENCIALIDAD ES COMPLETO \n")
print("      - LOS PORCENTAJES DE IMPACTO DE INTEGRIDAD SON LOS SIGUIENTES : \n")
print("             - EL "+str(float((((complete_confidentiality_completeintegrity_sh_cvssv2+complete_confidentiality_completeintegrity_iot_cvssv2)*100)/(complete_confidentiality_sh_cvssv2+complete_confidentiality_iot_cvssv2))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD COMPLETO \n")
print("             - EL "+str(float((((complete_confidentiality_partialintegrity_sh_cvssv2+complete_confidentiality_partialintegrity_iot_cvssv2)*100)/(complete_confidentiality_sh_cvssv2+complete_confidentiality_iot_cvssv2))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD PARCIAL \n")
print("             - EL "+str(float((((complete_confidentiality_noneintegrity_sh_cvssv2+complete_confidentiality_noneintegrity_iot_cvssv2)*100)/(complete_confidentiality_sh_cvssv2+complete_confidentiality_iot_cvssv2))))+" % DE LAS VULNERABILIDADES NO TIENEN IMPACTO EN LA INTEGRIDAD DEL SISTEMA/PRODUCTO \n")
print("\n")
print("      - LOS PORCENTAJES DE IMPACTO DE DISPONIBILIDAD SON LOS SIGUIENTES : \n")
print("             - EL "+str(float((((complete_confidentiality_completeavailability_sh_cvssv2+complete_confidentiality_completeavailability_iot_cvssv2)*100)/(complete_confidentiality_sh_cvssv2+complete_confidentiality_iot_cvssv2))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD COMPLETO \n")
print("             - EL "+str(float((((complete_confidentiality_partialavailability_sh_cvssv2+complete_confidentiality_partialavailability_iot_cvssv2)*100)/(complete_confidentiality_sh_cvssv2+complete_confidentiality_iot_cvssv2))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD PARCIAL \n")
print("             - EL "+str(float((((complete_confidentiality_noneavailability_sh_cvssv2+complete_confidentiality_noneavailability_iot_cvssv2)*100)/(complete_confidentiality_sh_cvssv2+complete_confidentiality_iot_cvssv2))))+" % DE LAS VULNERABILIDADES NO TIENEN IMPACTO EN LA DISPONIBILIDAD DEL SISTEMA/PRODUCTO \n")

print("\n")
print(" - EN EL  "+str(float((((partial_confidentiality_sh_cvssv2+partial_confidentiality_iot_cvssv2)*100)/(total_vulnerabilities_cvssv2))))+" % DE LAS VULNERABILIDADES, DONDE EL IMPACTO DE CONFIDENCIALIDAD ES PARCIAL: \n")
print("      - LOS PORCENTAJES DE IMPACTO DE INTEGRIDAD SON LOS SIGUIENTES : \n")
print("             - EL "+str(float((((partial_confidentiality_completeintegrity_sh_cvssv2+partial_confidentiality_completeintegrity_iot_cvssv2)*100)/(partial_confidentiality_sh_cvssv2+partial_confidentiality_iot_cvssv2))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD COMPLETO \n")
print("             - EL "+str(float((((partial_confidentiality_partialintegrity_sh_cvssv2+partial_confidentiality_partialintegrity_iot_cvssv2)*100)/(partial_confidentiality_sh_cvssv2+partial_confidentiality_iot_cvssv2))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD PARCIAL \n")
print("             - EL "+str(float((((partial_confidentiality_noneintegrity_sh_cvssv2+partial_confidentiality_noneintegrity_iot_cvssv2)*100)/(partial_confidentiality_sh_cvssv2+partial_confidentiality_iot_cvssv2))))+" % DE LAS VULNERABILIDADES NO TIENEN IMPACTO EN LA INTEGRIDAD DEL SISTEMA/PRODUCTO \n")
print("\n")
print("      - LOS PORCENTAJES DE IMPACTO DE DISPONIBILIDAD SON LOS SIGUIENTES : \n")
print("             - EL "+str(float((((partial_confidentiality_completeavailability_sh_cvssv2+partial_confidentiality_completeavailability_iot_cvssv2)*100)/(partial_confidentiality_sh_cvssv2+partial_confidentiality_iot_cvssv2))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD COMPLETO \n")
print("             - EL "+str(float((((partial_confidentiality_partialavailability_sh_cvssv2+partial_confidentiality_partialavailability_iot_cvssv2)*100)/(partial_confidentiality_sh_cvssv2+partial_confidentiality_iot_cvssv2))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD PARCIAL \n")
print("             - EL "+str(float((((partial_confidentiality_noneavailability_sh_cvssv2+partial_confidentiality_noneavailability_iot_cvssv2)*100)/(partial_confidentiality_sh_cvssv2+partial_confidentiality_iot_cvssv2))))+" % DE LAS VULNERABILIDADES NO TIENEN IMPACTO EN LA DISPONIBILIDAD DEL SISTEMA/PRODUCTO \n")



print("\n")
print(" - EN EL  "+str(float((((none_confidentiality_sh_cvssv2+none_confidentiality_iot_cvssv2)*100)/(total_vulnerabilities_cvssv2))))+" % DE LAS VULNERABILIDADES, DONDE EL IMPACTO DE CONFIDENCIALIDAD NO TIENE EFECTO EN EL SISTEMA/PRODUCTO VULNERABLE \n")
print("      - LOS PORCENTAJES DE IMPACTO DE INTEGRIDAD SON LOS SIGUIENTES : \n")
print("             - EL "+str(float((((none_confidentiality_completeintegrity_sh_cvssv2+none_confidentiality_completeintegrity_iot_cvssv2)*100)/(none_confidentiality_sh_cvssv2+none_confidentiality_iot_cvssv2))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD COMPLETO \n")
print("             - EL "+str(float((((none_confidentiality_partialintegrity_sh_cvssv2+none_confidentiality_partialintegrity_iot_cvssv2)*100)/(none_confidentiality_sh_cvssv2+none_confidentiality_iot_cvssv2))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD PARCIAL \n")
print("             - EL "+str(float((((none_confidentiality_noneintegrity_sh_cvssv2+none_confidentiality_noneintegrity_iot_cvssv2)*100)/(none_confidentiality_sh_cvssv2+none_confidentiality_iot_cvssv2))))+" % DE LAS VULNERABILIDADES NO TIENEN IMPACTO EN LA INTEGRIDAD DEL SISTEMA/PRODUCTO \n")
print("\n")
print("      - LOS PORCENTAJES DE IMPACTO DE DISPONIBILIDAD SON LOS SIGUIENTES : \n")
print("             - EL "+str(float((((none_confidentiality_completeavailability_sh_cvssv2+none_confidentiality_completeavailability_iot_cvssv2)*100)/(none_confidentiality_sh_cvssv2+none_confidentiality_iot_cvssv2))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD COMPLETO \n")
print("             - EL "+str(float((((none_confidentiality_partialavailability_sh_cvssv2+none_confidentiality_partialavailability_iot_cvssv2)*100)/(none_confidentiality_sh_cvssv2+none_confidentiality_iot_cvssv2))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD PARCIAL \n")
print("             - EL "+str(float((((none_confidentiality_noneavailability_sh_cvssv2+none_confidentiality_noneavailability_iot_cvssv2)*100)/(none_confidentiality_sh_cvssv2+none_confidentiality_iot_cvssv2))))+" % DE LAS VULNERABILIDADES NO TIENEN IMPACTO EN LA DISPONIBILIDAD DEL SISTEMA/PRODUCTO \n")

print("*************************************************************************************************************************")
print(" - EN EL  "+str(float((((complete_integrity_sh_cvssv2+complete_integrity_iot_cvssv2)*100)/(len(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.integrityImpact"])+len(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.integrityImpact"])))))+" % DE LAS VULNERABILIDADES, DONDE EL IMPACTO DE INTEGRIDAD ES COMPLETO \n")
print("      - LOS PORCENTAJES DE IMPACTO DE CONFIDENCIALIDAD SON LOS SIGUIENTES : \n")
print("             - EL "+str(float((((complete_integrity_completeconfidentiality_sh_cvssv2+complete_integrity_completeconfidentiality_iot_cvssv2)*100)/(complete_integrity_sh_cvssv2+complete_integrity_iot_cvssv2))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD COMPLETO \n")
print("             - EL "+str(float((((complete_integrity_partialconfidentiality_sh_cvssv2+complete_integrity_partialconfidentiality_iot_cvssv2)*100)/(complete_integrity_sh_cvssv2+complete_integrity_iot_cvssv2))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD PARCIAL \n")
print("             - EL "+str(float((((complete_integrity_noneconfidentiality_sh_cvssv2+complete_integrity_noneconfidentiality_iot_cvssv2)*100)/(complete_integrity_sh_cvssv2+complete_integrity_iot_cvssv2))))+" % DE LAS VULNERABILIDADES NO TIENEN IMPACTO EN LA CONFIDENCIALIDAD DEL SISTEMA/PRODUCTO \n")
print("\n")
print("      - LOS PORCENTAJES DE IMPACTO DE DISPONIBILIDAD SON LOS SIGUIENTES : \n")
print("             - EL "+str(float((((complete_integrity_completeavailability_sh_cvssv2+complete_integrity_completeavailability_iot_cvssv2)*100)/(complete_integrity_sh_cvssv2+complete_integrity_iot_cvssv2))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD COMPLETO \n")
print("             - EL "+str(float((((complete_integrity_partialavailability_sh_cvssv2+complete_integrity_partialavailability_iot_cvssv2)*100)/(complete_integrity_sh_cvssv2+complete_integrity_iot_cvssv2))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD PARCIAL \n")
print("             - EL "+str(float((((complete_integrity_noneavailability_sh_cvssv2+complete_integrity_noneavailability_iot_cvssv2)*100)/(complete_integrity_sh_cvssv2+complete_integrity_iot_cvssv2))))+" % DE LAS VULNERABILIDADES NO TIENEN IMPACTO EN LA DISPONIBILIDAD DEL SISTEMA/PRODUCTO \n")


print(" - EN EL  "+str(float((((partial_integrity_sh_cvssv2+partial_integrity_iot_cvssv2)*100)/(len(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.integrityImpact"])+len(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.integrityImpact"])))))+" % DE LAS VULNERABILIDADES, DONDE EL IMPACTO DE INTEGRIDAD ES PARCIAL: \n")
print("      - LOS PORCENTAJES DE IMPACTO DE CONFIDENCIALIDAD SON LOS SIGUIENTES : \n")
print("             - EL "+str(float((((partial_integrity_completeconfidentiality_sh_cvssv2+partial_integrity_completeconfidentiality_iot_cvssv2)*100)/(partial_integrity_sh_cvssv2+partial_integrity_iot_cvssv2))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD COMPLETO \n")
print("             - EL "+str(float((((partial_integrity_partialconfidentiality_sh_cvssv2+partial_integrity_partialconfidentiality_iot_cvssv2)*100)/(partial_integrity_sh_cvssv2+partial_integrity_iot_cvssv2))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD PARCIAL \n")
print("             - EL "+str(float((((partial_integrity_noneconfidentiality_sh_cvssv2+partial_integrity_noneconfidentiality_iot_cvssv2)*100)/(partial_integrity_sh_cvssv2+partial_integrity_iot_cvssv2))))+" % DE LAS VULNERABILIDADES NO TIENEN IMPACTO EN LA CONFIDENCIALIDAD DEL SISTEMA/PRODUCTO \n")
print("\n")
print("      - LOS PORCENTAJES DE IMPACTO DE DISPONIBILIDAD SON LOS SIGUIENTES : \n")
print("             - EL "+str(float((((partial_integrity_completeavailability_sh_cvssv2+partial_integrity_completeavailability_iot_cvssv2)*100)/(partial_integrity_sh_cvssv2+partial_integrity_iot_cvssv2))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD COMPLETO \n")
print("             - EL "+str(float((((partial_integrity_partialavailability_sh_cvssv2+partial_integrity_partialavailability_iot_cvssv2)*100)/(partial_integrity_sh_cvssv2+partial_integrity_iot_cvssv2))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD PARCIAL \n")
print("             - EL "+str(float((((partial_integrity_noneavailability_sh_cvssv2+partial_integrity_noneavailability_iot_cvssv2)*100)/(partial_integrity_sh_cvssv2+partial_integrity_iot_cvssv2))))+" % DE LAS VULNERABILIDADES NO TIENEN IMPACTO EN LA DISPONIBILIDAD DEL SISTEMA/PRODUCTO \n")




print(" - EN EL  "+str(float((((none_integrity_sh_cvssv2+none_integrity_iot_cvssv2)*100)/(len(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.integrityImpact"])+len(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.integrityImpact"])))))+" % DE LAS VULNERABILIDADES, DONDE EL IMPACTO DE INTEGRIDAD NO TIENE EFECTO EN EL SISTEMA/PRODUCTO VULNERABLE \n")
print("      - LOS PORCENTAJES DE IMPACTO DE CONFIDENCIALIDAD SON LOS SIGUIENTES : \n")
print("             - EL "+str(float((((none_integrity_completeconfidentiality_sh_cvssv2+none_integrity_completeconfidentiality_iot_cvssv2)*100)/(none_integrity_sh_cvssv2+none_integrity_iot_cvssv2))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD COMPLETO \n")
print("             - EL "+str(float((((none_integrity_partialconfidentiality_sh_cvssv2+none_integrity_partialconfidentiality_iot_cvssv2)*100)/(none_integrity_sh_cvssv2+none_integrity_iot_cvssv2))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD PARCIAL \n")
print("             - EL "+str(float((((none_integrity_noneconfidentiality_sh_cvssv2+none_integrity_noneconfidentiality_iot_cvssv2)*100)/(none_integrity_sh_cvssv2+none_integrity_iot_cvssv2))))+" % DE LAS VULNERABILIDADES NO TIENEN IMPACTO EN LA CONFIDENCIALIDAD DEL SISTEMA/PRODUCTO \n")
print("\n")
print("      - LOS PORCENTAJES DE IMPACTO DE DISPONIBILIDAD SON LOS SIGUIENTES : \n")
print("             - EL "+str(float((((none_integrity_completeavailability_sh_cvssv2+none_integrity_completeavailability_iot_cvssv2)*100)/(none_integrity_sh_cvssv2+none_integrity_iot_cvssv2))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD COMPLETO \n")
print("             - EL "+str(float((((none_integrity_partialavailability_sh_cvssv2+none_integrity_partialavailability_iot_cvssv2)*100)/(none_integrity_sh_cvssv2+none_integrity_iot_cvssv2))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE DISPONIBILIDAD PARCIAL \n")
print("             - EL "+str(float((((none_integrity_noneavailability_sh_cvssv2+none_integrity_noneavailability_iot_cvssv2)*100)/(none_integrity_sh_cvssv2+none_integrity_iot_cvssv2))))+" % DE LAS VULNERABILIDADES NO TIENEN IMPACTO EN LA DISPONIBILIDAD DEL SISTEMA/PRODUCTO \n")




print("*************************************************************************************************************************")

print(" - EN EL  "+str(float((((complete_availability_sh_cvssv2+complete_availability_iot_cvssv2)*100)/(total_vulnerabilities_cvssv2))))+" % DE LAS VULNERABILIDADES, DONDE EL IMPACTO DE DISPONIBILIDAD ES COMPLETO \n")
print("      - LOS PORCENTAJES DE IMPACTO DE CONFIDENCIALIDAD SON LOS SIGUIENTES : \n")
print("             - EL "+str(float((((complete_availability_completeconfidentiality_sh_cvssv2+complete_availability_completeconfidentiality_iot_cvssv2)*100)/(complete_availability_sh_cvssv2+complete_availability_iot_cvssv2))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD COMPLETO \n")
print("             - EL "+str(float((((complete_availability_partialconfidentiality_sh_cvssv2+complete_availability_partialconfidentiality_iot_cvssv2)*100)/(complete_availability_sh_cvssv2+complete_availability_iot_cvssv2))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD PARCIAL \n")
print("             - EL "+str(float((((complete_availability_noneconfidentiality_sh_cvssv2+complete_availability_noneconfidentiality_iot_cvssv2)*100)/(complete_availability_sh_cvssv2+complete_availability_iot_cvssv2))))+" % DE LAS VULNERABILIDADES NO TIENEN IMPACTO EN LA CONFIDENCIALIDAD DEL SISTEMA/PRODUCTO \n")
print("\n")
print("      - LOS PORCENTAJES DE IMPACTO DE INTEGRIDAD SON LOS SIGUIENTES : \n")
print("             - EL "+str(float((((complete_availability_completeintegrity_sh_cvssv2+complete_availability_completeintegrity_iot_cvssv2)*100)/(complete_availability_sh_cvssv2+complete_availability_iot_cvssv2))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD COMPLETO \n")
print("             - EL "+str(float((((complete_availability_partialintegrity_sh_cvssv2+complete_availability_partialintegrity_iot_cvssv2)*100)/(complete_availability_sh_cvssv2+complete_availability_iot_cvssv2))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD PARCIAL \n")
print("             - EL "+str(float((((complete_availability_noneintegrity_sh_cvssv2+complete_availability_noneintegrity_iot_cvssv2)*100)/(complete_availability_sh_cvssv2+complete_availability_iot_cvssv2))))+" % DE LAS VULNERABILIDADES NO TIENEN IMPACTO EN LA INTEGRIDAD DEL SISTEMA/PRODUCTO \n")



print(" - EN EL  "+str(float((((partial_availability_sh_cvssv2+partial_availability_iot_cvssv2)*100)/(total_vulnerabilities_cvssv2))))+" % DE LAS VULNERABILIDADES, DONDE EL IMPACTO DE DISPONIBILIDAD ES PARCIAL: \n")
print("      - LOS PORCENTAJES DE IMPACTO DE CONFIDENCIALIDAD SON LOS SIGUIENTES : \n")
print("             - EL "+str(float((((partial_availability_completeconfidentiality_sh_cvssv2+partial_availability_completeconfidentiality_iot_cvssv2)*100)/(partial_availability_sh_cvssv2+partial_availability_iot_cvssv2))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD COMPLETO \n")
print("             - EL "+str(float((((partial_availability_partialconfidentiality_sh_cvssv2+partial_availability_partialconfidentiality_iot_cvssv2)*100)/(partial_availability_sh_cvssv2+partial_availability_iot_cvssv2))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD PARCIAL \n")
print("             - EL "+str(float((((partial_availability_noneconfidentiality_sh_cvssv2+partial_availability_noneconfidentiality_iot_cvssv2)*100)/(partial_availability_sh_cvssv2+partial_availability_iot_cvssv2))))+" % DE LAS VULNERABILIDADES NO TIENEN IMPACTO EN LA CONFIDENCIALIDAD DEL SISTEMA/PRODUCTO \n")
print("\n")
print("      - LOS PORCENTAJES DE IMPACTO DE INTEGRIDAD SON LOS SIGUIENTES : \n")
print("             - EL "+str(float((((partial_availability_completeintegrity_sh_cvssv2+partial_availability_completeintegrity_iot_cvssv2)*100)/(partial_availability_sh_cvssv2+partial_availability_iot_cvssv2))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD COMPLETO \n")
print("             - EL "+str(float((((partial_availability_partialintegrity_sh_cvssv2+partial_availability_partialintegrity_iot_cvssv2)*100)/(partial_availability_sh_cvssv2+partial_availability_iot_cvssv2))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD PARCIAL \n")
print("             - EL "+str(float((((partial_availability_noneintegrity_sh_cvssv2+partial_availability_noneintegrity_iot_cvssv2)*100)/(partial_availability_sh_cvssv2+partial_availability_iot_cvssv2))))+" % DE LAS VULNERABILIDADES NO TIENEN IMPACTO EN LA INTEGRIDAD DEL SISTEMA/PRODUCTO \n")



print(" - EN EL  "+str(float((((none_availability_sh_cvssv2+none_availability_iot_cvssv2)*100)/(total_vulnerabilities_cvssv2))))+" % DE LAS VULNERABILIDADES, DONDE EL IMPACTO DE DISPONIBILIDAD NO TIENE EFECTO EN EL SISTEMA/PRODUCTO VULNERABLE \n")
print("      - LOS PORCENTAJES DE IMPACTO DE CONFIDENCIALIDAD SON LOS SIGUIENTES : \n")
print("             - EL "+str(float((((none_availability_completeconfidentiality_sh_cvssv2+none_availability_completeconfidentiality_iot_cvssv2)*100)/(none_availability_sh_cvssv2+none_availability_iot_cvssv2))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD COMPLETO \n")
print("             - EL "+str(float((((none_availability_partialconfidentiality_sh_cvssv2+none_availability_partialconfidentiality_iot_cvssv2)*100)/(none_availability_sh_cvssv2+none_availability_iot_cvssv2))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD PARCIAL \n")
print("             - EL "+str(float((((none_availability_noneconfidentiality_sh_cvssv2+none_availability_noneconfidentiality_iot_cvssv2)*100)/(none_availability_sh_cvssv2+none_availability_iot_cvssv2))))+" % DE LAS VULNERABILIDADES NO TIENEN IMPACTO EN LA CONFIDENCIALIDAD DEL SISTEMA/PRODUCTO \n")
print("\n")
print("      - LOS PORCENTAJES DE IMPACTO DE INTEGRIDAD SON LOS SIGUIENTES : \n")
print("             - EL "+str(float((((none_availability_completeintegrity_sh_cvssv2+none_availability_completeintegrity_iot_cvssv2)*100)/(none_availability_sh_cvssv2+none_availability_iot_cvssv2))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD COMPLETO \n")
print("             - EL "+str(float((((none_availability_partialintegrity_sh_cvssv2+none_availability_partialintegrity_iot_cvssv2)*100)/(none_availability_sh_cvssv2+none_availability_iot_cvssv2))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD PARCIAL \n")
print("             - EL "+str(float((((none_availability_noneintegrity_sh_cvssv2+none_availability_noneintegrity_iot_cvssv2)*100)/(none_availability_sh_cvssv2+none_availability_iot_cvssv2))))+" % DE LAS VULNERABILIDADES NO TIENEN IMPACTO EN LA INTEGRIDAD DEL SISTEMA/PRODUCTO \n")




