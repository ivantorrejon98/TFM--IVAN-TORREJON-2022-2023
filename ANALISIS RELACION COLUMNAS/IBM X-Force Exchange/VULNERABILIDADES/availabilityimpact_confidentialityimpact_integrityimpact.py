import pandas as pd
from datetime import datetime,timedelta



#Abro los ficheros con los que voy a tratar




df_vulnibm_iot = pd.read_excel('vulnerabilidades_ibm_iot_2023.xlsx')




#Contador de valores para un valor de disponibilidad concreto
high_availability_iot_vulnibm=0
#Contador de valores de confidencialidad para un valor de disponibilidad concreto
high_availability_lowconfidentiality_iot_vulnibm=0
high_availability_highconfidentiality_iot_vulnibm=0
high_availability_noneconfidentiality_iot_vulnibm=0
#Contador de valores de integridad para un valor de disponibilidad concreto
high_availability_lowintegrity_iot_vulnibm=0
high_availability_highintegrity_iot_vulnibm=0
high_availability_noneintegrity_iot_vulnibm=0

low_availability_iot_vulnibm=0
low_availability_lowconfidentiality_iot_vulnibm=0
low_availability_highconfidentiality_iot_vulnibm=0
low_availability_noneconfidentiality_iot_vulnibm=0
low_availability_lowintegrity_iot_vulnibm=0
low_availability_highintegrity_iot_vulnibm=0
low_availability_noneintegrity_iot_vulnibm=0

none_availability_iot_vulnibm=0
none_availability_lowconfidentiality_iot_vulnibm=0
none_availability_highconfidentiality_iot_vulnibm=0
none_availability_noneconfidentiality_iot_vulnibm=0
none_availability_lowintegrity_iot_vulnibm=0
none_availability_highintegrity_iot_vulnibm=0
none_availability_noneintegrity_iot_vulnibm=0




#Compruebo el valor de integridad
for j in range(0,len( df_vulnibm_iot["x_xfe_cvss_availability_impact"])):
    if( df_vulnibm_iot["x_xfe_cvss_availability_impact"][j]=='High'):
        high_availability_iot_vulnibm+=1
        #Compruebo el valor de integridad
        if( df_vulnibm_iot["x_xfe_cvss_confidentiality_impact"][j]=='High'):
            high_availability_highconfidentiality_iot_vulnibm+=1
        elif( df_vulnibm_iot["x_xfe_cvss_confidentiality_impact"][j]=='Low'):
            high_availability_lowconfidentiality_iot_vulnibm+=1
        else:
            high_availability_noneconfidentiality_iot_vulnibm+=1
            
    elif( df_vulnibm_iot["x_xfe_cvss_availability_impact"][j]=='Low'):
        low_availability_iot_vulnibm+=1
        if( df_vulnibm_iot["x_xfe_cvss_confidentiality_impact"][j]=='High'):
            low_availability_highconfidentiality_iot_vulnibm+=1
        elif( df_vulnibm_iot["x_xfe_cvss_confidentiality_impact"][j]=='Low'):
            low_availability_lowconfidentiality_iot_vulnibm+=1
        else:
            low_availability_noneconfidentiality_iot_vulnibm+=1
            
    else:
        none_availability_iot_vulnibm+=1
        if( df_vulnibm_iot["x_xfe_cvss_confidentiality_impact"][j]=='High'):
            none_availability_highconfidentiality_iot_vulnibm+=1
        elif( df_vulnibm_iot["x_xfe_cvss_confidentiality_impact"][j]=='Low'):
            none_availability_lowconfidentiality_iot_vulnibm+=1
        else:
            none_availability_noneconfidentiality_iot_vulnibm+=1
            
            
#Compruebo el valor de integridad          
for h in range(0,len( df_vulnibm_iot["x_xfe_cvss_availability_impact"])):
    if( df_vulnibm_iot["x_xfe_cvss_availability_impact"][h]=='High'):
        #Compruebo el valor de disponibilidad
        if( df_vulnibm_iot["x_xfe_cvss_integrity_impact"][h]=='High'):
            high_availability_highintegrity_iot_vulnibm+=1
        elif( df_vulnibm_iot["x_xfe_cvss_integrity_impact"][h]=='Low'):
            high_availability_lowintegrity_iot_vulnibm+=1
        else:
            high_availability_noneintegrity_iot_vulnibm+=1
            
    elif( df_vulnibm_iot["x_xfe_cvss_availability_impact"][h]=='Low'):
        if( df_vulnibm_iot["x_xfe_cvss_integrity_impact"][h]=='High'):
            low_availability_highintegrity_iot_vulnibm+=1
        elif( df_vulnibm_iot["x_xfe_cvss_integrity_impact"][h]=='Low'):
            low_availability_lowintegrity_iot_vulnibm+=1
        else:
            low_availability_noneintegrity_iot_vulnibm+=1
    else:
        if( df_vulnibm_iot["x_xfe_cvss_integrity_impact"][h]=='High'):
            none_availability_highintegrity_iot_vulnibm+=1
        elif( df_vulnibm_iot["x_xfe_cvss_integrity_impact"][h]=='Low'):
            none_availability_lowintegrity_iot_vulnibm+=1
        else:
            none_availability_noneintegrity_iot_vulnibm+=1




            
print("**************************ESTADÍSTICAS RELACION IMPACTO DE DISPONIBILIDAD CON IMPACTO DE CONFIDENCIALIDAD E INTEGRIDAD PARA OBJETOS DE VULNERABILIDADES PARTE IBM IOT********************************")
print("\n")
print(" DE UN TOTAL DE "+str(high_availability_iot_vulnibm+low_availability_iot_vulnibm+none_availability_iot_vulnibm)+" VULNERABILIDADES, LAS ESTADÍSTICAS DE IMPACTO DE DISPONIBILIDAD SON LAS SIGUIENTES: \n")
print("\n")
print(" - DE UN TOTAL DE "+str(high_availability_iot_vulnibm)+" VULNERABILIDADES DONDE EL IMPACTO DE DISPONIBILIDAD ES ALTO : \n")
print("      - LAS ESTADÍSTICAS DE IMPACTO DE CONFIDENCIALIDAD SON LAS SIGUIENTES : \n")
print("             - UN TOTAL DE "+str(high_availability_highconfidentiality_iot_vulnibm)+" VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD ALTO \n")
print("             - UN TOTAL DE "+str(high_availability_lowconfidentiality_iot_vulnibm)+" VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD BAJO  \n")
print("             - UN TOTAL DE "+str(high_availability_noneconfidentiality_iot_vulnibm)+" VULNERABILIDADES UNA EXPLOTACIÓN NO TIENE EFECTO EN EL IMPACTO DE CONFIDENCIALIDAD \n")
print("\n")
print("      - LAS ESTADÍSTICAS DE IMPACTO DE INTEGRIDAD SON LAS SIGUIENTES : \n")
print("             - UN TOTAL DE "+str(high_availability_highintegrity_iot_vulnibm)+" VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD ALTO \n")
print("             - UN TOTAL DE "+str(high_availability_lowintegrity_iot_vulnibm)+" VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD BAJO  \n")
print("             - UN TOTAL DE "+str(high_availability_noneintegrity_iot_vulnibm)+" VULNERABILIDADES UNA EXPLOTACIÓN NO TIENE EFECTO EN EL IMPACTO DE INTEGRIDAD \n")

print(" - DE UN TOTAL DE "+str(low_availability_iot_vulnibm)+" VULNERABILIDADES DONDE EL IMPACTO DE DISPONIBILIDAD ES BAJO :  \n")
print("      - LAS ESTADÍSTICAS DE IMPACTO DE CONFIDENCIALIDAD SON LAS SIGUIENTES : \n")
print("             - UN TOTAL DE "+str(low_availability_highconfidentiality_iot_vulnibm)+" VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD ALTO \n")
print("             - UN TOTAL DE "+str(low_availability_lowconfidentiality_iot_vulnibm)+" VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD BAJO  \n")
print("             - UN TOTAL DE "+str(low_availability_noneconfidentiality_iot_vulnibm)+" VULNERABILIDADES UNA EXPLOTACIÓN NO TIENE EFECTO EN EL IMPACTO DE CONFIDENCIALIDAD \n")
print("\n")
print("      - LAS ESTADÍSTICAS DE IMPACTO DE INTEGRIDAD SON LAS SIGUIENTES : \n")
print("             - UN TOTAL DE "+str(low_availability_highintegrity_iot_vulnibm)+" VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD ALTO \n")
print("             - UN TOTAL DE "+str(low_availability_lowintegrity_iot_vulnibm)+" VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD BAJO  \n")
print("             - UN TOTAL DE "+str(low_availability_noneintegrity_iot_vulnibm)+" VULNERABILIDADES UNA EXPLOTACIÓN NO TIENE EFECTO EN EL IMPACTO DE INTEGRIDAD \n")

print(" - DE UN TOTAL DE "+str(none_availability_iot_vulnibm)+" VULNERABILIDADES DONDE UNA EXPLOTACIÓN NO TIENE EFECTO EN EL IMPACTO DE DISPONIBILIDAD :  \n")
print("      - LAS ESTADÍSTICAS DE IMPACTO DE CONFIDENCIALIDAD SON LAS SIGUIENTES : \n")
print("             - UN TOTAL DE "+str(none_availability_highconfidentiality_iot_vulnibm)+" VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD ALTO \n")
print("             - UN TOTAL DE "+str(none_availability_lowconfidentiality_iot_vulnibm)+" VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD BAJO  \n")
print("             - UN TOTAL DE "+str(none_availability_noneconfidentiality_iot_vulnibm)+" VULNERABILIDADES UNA EXPLOTACIÓN NO TIENE EFECTO EN EL IMPACTO DE CONFIDENCIALIDAD \n")
print("\n")
print("      - LAS ESTADÍSTICAS DE IMPACTO DE INTEGRIDAD SON LAS SIGUIENTES : \n")
print("             - UN TOTAL DE "+str(none_availability_highintegrity_iot_vulnibm)+" VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD ALTO \n")
print("             - UN TOTAL DE "+str(none_availability_lowintegrity_iot_vulnibm)+" VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD BAJO  \n")
print("             - UN TOTAL DE "+str(none_availability_noneintegrity_iot_vulnibm)+" VULNERABILIDADES UNA EXPLOTACIÓN NO TIENE EFECTO EN EL IMPACTO DE INTEGRIDAD \n")
print("\n")
print("\n")




print("************************** PORCENTAJE IMPACTO DE INTEGRIDAD CON IMPACTO DE CONFIDENCIALIDAD Y DISPONIBILIDAD  PARA OBJETOS DE VULNERABILIDADES IBM PARTE IOT********************************")
print("\n")
print(" DE UN TOTAL DE "+str(high_availability_iot_vulnibm+low_availability_iot_vulnibm+none_availability_iot_vulnibm)+" VULNERABILIDADES, LOS PORCENTAJES DE IMPACTO DE DISPONIBILIDAD SON LOS SIGUIENTES: \n")
print("\n")
print(" - EN EL  "+str(float(((high_availability_iot_vulnibm*100)/len( df_vulnibm_iot["x_xfe_cvss_availability_impact"]))))+" % DE LAS VULNERABILIDADES, DONDE EL IMPACTO DE DISPONIBILIDAD ES ALTO \n")
print("      - LOS PORCENTAJES DE IMPACTO DE CONFIDENCIALIDAD SON LOS SIGUIENTES : \n")
print("             - EL "+str(float(((high_availability_highconfidentiality_iot_vulnibm*100)/(high_availability_iot_vulnibm))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD ALTO \n")
print("             - EL "+str(float(((high_availability_lowconfidentiality_iot_vulnibm*100)/(high_availability_iot_vulnibm))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD BAJO  \n")
print("             - EL "+str(float(((high_availability_noneconfidentiality_iot_vulnibm*100)/(high_availability_iot_vulnibm))))+" % DE LAS VULNERABILIDADES UNA EXPLOTACIÓN NO TIENE EFECTO EN EL IMPACTO DE CONFIDENCIALIDAD  \n")
print("\n")
print("      - LOS PORCENTAJES DE IMPACTO DE INTEGRIDAD SON LOS SIGUIENTES : \n")
print("             - EL "+str(float(((high_availability_highintegrity_iot_vulnibm*100)/(high_availability_iot_vulnibm))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD ALTO \n")
print("             - EL "+str(float(((high_availability_lowintegrity_iot_vulnibm*100)/(high_availability_iot_vulnibm))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD BAJO  \n")
print("             - EL "+str(float(((high_availability_noneintegrity_iot_vulnibm*100)/(high_availability_iot_vulnibm))))+" % DE LAS VULNERABILIDADES UNA EXPLOTACIÓN NO TIENE EFECTO EN EL IMPACTO DE INTEGRIDAD   \n")

print("\n")
print(" - EN EL  "+str(float(((low_availability_iot_vulnibm*100)/len( df_vulnibm_iot["x_xfe_cvss_availability_impact"]))))+" % DE LAS VULNERABILIDADES, DONDE EL IMPACTO DE DISPONIBILIDAD ES BAJO: \n")
print("      - LOS PORCENTAJES DE IMPACTO DE CONFIDENCIALIDAD SON LOS SIGUIENTES : \n")
print("             - EL "+str(float(((low_availability_highconfidentiality_iot_vulnibm*100)/(low_availability_iot_vulnibm))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD ALTO \n")
print("             - EL "+str(float(((low_availability_lowconfidentiality_iot_vulnibm*100)/(low_availability_iot_vulnibm))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD BAJO  \n")
print("             - EL "+str(float(((low_availability_noneconfidentiality_iot_vulnibm*100)/(low_availability_iot_vulnibm))))+" % DE LAS VULNERABILIDADES UNA EXPLOTACIÓN NO TIENE EFECTO EN EL IMPACTO DE CONFIDENCIALIDAD  \n")
print("\n")
print("      - LOS PORCENTAJES DE IMPACTO DE INTEGRIDAD SON LOS SIGUIENTES : \n")
print("             - EL "+str(float(((low_availability_highintegrity_iot_vulnibm*100)/(low_availability_iot_vulnibm))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD ALTO \n")
print("             - EL "+str(float(((low_availability_lowintegrity_iot_vulnibm*100)/(low_availability_iot_vulnibm))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD BAJO  \n")
print("             - EL "+str(float(((low_availability_noneintegrity_iot_vulnibm*100)/(low_availability_iot_vulnibm))))+" % DE LAS VULNERABILIDADES UNA EXPLOTACIÓN NO TIENE EFECTO EN EL IMPACTO DE INTEGRIDAD   \n")


print("\n")
print(" - EN EL  "+str(float(((none_availability_iot_vulnibm*100)/len( df_vulnibm_iot["x_xfe_cvss_availability_impact"]))))+" % DE LAS VULNERABILIDADES, DONDE UNA EXPLOTACIÓN NO TIENE EFECTO EN EL IMPACTO DE DISPONIBILIDAD :  \n")
print("      - LOS PORCENTAJES DE IMPACTO DE CONFIDENCIALIDAD SON LOS SIGUIENTES : \n")
print("             - EL "+str(float(((none_availability_highconfidentiality_iot_vulnibm*100)/(none_availability_iot_vulnibm))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD ALTO \n")
print("             - EL "+str(float(((none_availability_lowconfidentiality_iot_vulnibm*100)/(none_availability_iot_vulnibm))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD BAJO  \n")
print("             - EL "+str(float(((none_availability_noneconfidentiality_iot_vulnibm*100)/(none_availability_iot_vulnibm))))+" % DE LAS VULNERABILIDADES UNA EXPLOTACIÓN NO TIENE EFECTO EN EL IMPACTO DE CONFIDENCIALIDAD  \n")
print("\n")
print("      - LOS PORCENTAJES DE IMPACTO DE INTEGRIDAD SON LOS SIGUIENTES : \n")
print("             - EL "+str(float(((none_availability_highintegrity_iot_vulnibm*100)/(none_availability_iot_vulnibm))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD ALTO \n")
print("             - EL "+str(float(((none_availability_lowintegrity_iot_vulnibm*100)/(none_availability_iot_vulnibm))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD BAJO  \n")
print("             - EL "+str(float(((none_availability_noneintegrity_iot_vulnibm*100)/(none_availability_iot_vulnibm))))+" % DE LAS VULNERABILIDADES UNA EXPLOTACIÓN NO TIENE EFECTO EN EL IMPACTO DE INTEGRIDAD   \n")













import pandas as pd
from datetime import datetime,timedelta



#Abro los ficheros con los que voy a tratar




df_vulnibm_sh = pd.read_excel('vulnerabilidades_ibm_smart_home_2023.xlsx')




#Contador de valores para un valor de disponibilidad concreto
high_availability_sh_vulnibm=0
#Contador de valores de confidencialidad para un valor de disponibilidad concreto
high_availability_lowconfidentiality_sh_vulnibm=0
high_availability_highconfidentiality_sh_vulnibm=0
high_availability_noneconfidentiality_sh_vulnibm=0
#Contador de valores de integridad para un valor de disponibilidad concreto
high_availability_lowintegrity_sh_vulnibm=0
high_availability_highintegrity_sh_vulnibm=0
high_availability_noneintegrity_sh_vulnibm=0

low_availability_sh_vulnibm=0
low_availability_lowconfidentiality_sh_vulnibm=0
low_availability_highconfidentiality_sh_vulnibm=0
low_availability_noneconfidentiality_sh_vulnibm=0
low_availability_lowintegrity_sh_vulnibm=0
low_availability_highintegrity_sh_vulnibm=0
low_availability_noneintegrity_sh_vulnibm=0

none_availability_sh_vulnibm=0
none_availability_lowconfidentiality_sh_vulnibm=0
none_availability_highconfidentiality_sh_vulnibm=0
none_availability_noneconfidentiality_sh_vulnibm=0
none_availability_lowintegrity_sh_vulnibm=0
none_availability_highintegrity_sh_vulnibm=0
none_availability_noneintegrity_sh_vulnibm=0




#Compruebo el valor de integridad
for j in range(0,len( df_vulnibm_sh["x_xfe_cvss_availability_impact"])):
    if( df_vulnibm_sh["x_xfe_cvss_availability_impact"][j]=='High'):
        high_availability_sh_vulnibm+=1
        #Compruebo el valor de CONFIDENCIALIDAD
        if( df_vulnibm_sh["x_xfe_cvss_confidentiality_impact"][j]=='High'):
            high_availability_highconfidentiality_sh_vulnibm+=1
        elif( df_vulnibm_sh["x_xfe_cvss_confidentiality_impact"][j]=='Low'):
            high_availability_lowconfidentiality_sh_vulnibm+=1
        else:
            high_availability_noneconfidentiality_sh_vulnibm+=1
            
    elif( df_vulnibm_sh["x_xfe_cvss_availability_impact"][j]=='Low'):
        low_availability_sh_vulnibm+=1
        if( df_vulnibm_sh["x_xfe_cvss_confidentiality_impact"][j]=='High'):
            low_availability_highconfidentiality_sh_vulnibm+=1
        elif( df_vulnibm_sh["x_xfe_cvss_confidentiality_impact"][j]=='Low'):
            low_availability_lowconfidentiality_sh_vulnibm+=1
        else:
            low_availability_noneconfidentiality_sh_vulnibm+=1
            
    else:
        none_availability_sh_vulnibm+=1
        if( df_vulnibm_sh["x_xfe_cvss_confidentiality_impact"][j]=='High'):
            none_availability_highconfidentiality_sh_vulnibm+=1
        elif( df_vulnibm_sh["x_xfe_cvss_confidentiality_impact"][j]=='Low'):
            none_availability_lowconfidentiality_sh_vulnibm+=1
        else:
            none_availability_noneconfidentiality_sh_vulnibm+=1
            
            
#Compruebo el valor de integridad           
for h in range(0,len( df_vulnibm_sh["x_xfe_cvss_availability_impact"])):
    if( df_vulnibm_sh["x_xfe_cvss_availability_impact"][h]=='High'):
        #Compruebo el valor de disponibilidad
        if( df_vulnibm_sh["x_xfe_cvss_integrity_impact"][h]=='High'):
            high_availability_highintegrity_sh_vulnibm+=1
        elif( df_vulnibm_sh["x_xfe_cvss_integrity_impact"][h]=='Low'):
            high_availability_lowintegrity_sh_vulnibm+=1
        else:
            high_availability_noneintegrity_sh_vulnibm+=1
            
    elif( df_vulnibm_sh["x_xfe_cvss_availability_impact"][h]=='Low'):
        if( df_vulnibm_sh["x_xfe_cvss_integrity_impact"][h]=='High'):
            low_availability_highintegrity_sh_vulnibm+=1
        elif( df_vulnibm_sh["x_xfe_cvss_integrity_impact"][h]=='Low'):
            low_availability_lowintegrity_sh_vulnibm+=1
        else:
            low_availability_noneintegrity_sh_vulnibm+=1
    else:
        if( df_vulnibm_sh["x_xfe_cvss_integrity_impact"][h]=='High'):
            none_availability_highintegrity_sh_vulnibm+=1
        elif( df_vulnibm_sh["x_xfe_cvss_integrity_impact"][h]=='Low'):
            none_availability_lowintegrity_sh_vulnibm+=1
        else:
            none_availability_noneintegrity_sh_vulnibm+=1



print("\n")
print("\n")            
print("**************************ESTADÍSTICAS RELACION IMPACTO DE DISPONIBILIDAD CON IMPACTO DE CONFIDENCIALIDAD E INTEGRIDAD  PARA OBJETOS DE VULNERABILIDADES PARTE IBM SMART HOME********************************")
print("\n")
print(" DE UN TOTAL DE "+str(high_availability_sh_vulnibm+low_availability_sh_vulnibm+none_availability_sh_vulnibm)+" VULNERABILIDADES, LAS ESTADÍSTICAS DE IMPACTO DE DISPONIBILIDAD SON LAS SIGUIENTES: \n")
print("\n")
print(" - DE UN TOTAL DE "+str(high_availability_sh_vulnibm)+" VULNERABILIDADES DONDE EL IMPACTO DE DISPONIBILIDAD ES ALTO : \n")
print("      - LAS ESTADÍSTICAS DE IMPACTO DE CONFIDENCIALIDAD SON LAS SIGUIENTES : \n")
print("             - UN TOTAL DE "+str(high_availability_highconfidentiality_sh_vulnibm)+" VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD ALTO \n")
print("             - UN TOTAL DE "+str(high_availability_lowconfidentiality_sh_vulnibm)+" VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD BAJO  \n")
print("             - UN TOTAL DE "+str(high_availability_noneconfidentiality_sh_vulnibm)+" VULNERABILIDADES UNA EXPLOTACIÓN NO TIENE EFECTO EN EL IMPACTO DE CONFIDENCIALIDAD \n")
print("\n")
print("      - LAS ESTADÍSTICAS DE IMPACTO DE INTEGRIDAD SON LAS SIGUIENTES : \n")
print("             - UN TOTAL DE "+str(high_availability_highintegrity_sh_vulnibm)+" VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD ALTO \n")
print("             - UN TOTAL DE "+str(high_availability_lowintegrity_sh_vulnibm)+" VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD BAJO  \n")
print("             - UN TOTAL DE "+str(high_availability_noneintegrity_sh_vulnibm)+" VULNERABILIDADES UNA EXPLOTACIÓN NO TIENE EFECTO EN EL IMPACTO DE INTEGRIDAD \n")

print(" - DE UN TOTAL DE "+str(low_availability_sh_vulnibm)+" VULNERABILIDADES DONDE EL IMPACTO DE DISPONIBILIDAD ES BAJO :  \n")
print("      - LAS ESTADÍSTICAS DE IMPACTO DE CONFIDENCIALIDAD SON LAS SIGUIENTES : \n")
print("             - UN TOTAL DE "+str(low_availability_highconfidentiality_sh_vulnibm)+" VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD ALTO \n")
print("             - UN TOTAL DE "+str(low_availability_lowconfidentiality_sh_vulnibm)+" VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD BAJO  \n")
print("             - UN TOTAL DE "+str(low_availability_noneconfidentiality_sh_vulnibm)+" VULNERABILIDADES UNA EXPLOTACIÓN NO TIENE EFECTO EN EL IMPACTO DE CONFIDENCIALIDAD \n")
print("\n")
print("      - LAS ESTADÍSTICAS DE IMPACTO DE INTEGRIDAD SON LAS SIGUIENTES : \n")
print("             - UN TOTAL DE "+str(low_availability_highintegrity_sh_vulnibm)+" VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD ALTO \n")
print("             - UN TOTAL DE "+str(low_availability_lowintegrity_sh_vulnibm)+" VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD BAJO  \n")
print("             - UN TOTAL DE "+str(low_availability_noneintegrity_sh_vulnibm)+" VULNERABILIDADES UNA EXPLOTACIÓN NO TIENE EFECTO EN EL IMPACTO DE INTEGRIDAD \n")

print(" - DE UN TOTAL DE "+str(none_availability_sh_vulnibm)+" VULNERABILIDADES DONDE UNA EXPLOTACIÓN NO TIENE EFECTO EN EL IMPACTO DE DISPONIBILIDAD :  \n")
print("      - LAS ESTADÍSTICAS DE IMPACTO DE CONFIDENCIALIDAD SON LAS SIGUIENTES : \n")
print("             - UN TOTAL DE "+str(none_availability_highconfidentiality_sh_vulnibm)+" VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD ALTO \n")
print("             - UN TOTAL DE "+str(none_availability_lowconfidentiality_sh_vulnibm)+" VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD BAJO  \n")
print("             - UN TOTAL DE "+str(none_availability_noneconfidentiality_sh_vulnibm)+" VULNERABILIDADES UNA EXPLOTACIÓN NO TIENE EFECTO EN EL IMPACTO DE CONFIDENCIALIDAD \n")
print("\n")
print("      - LAS ESTADÍSTICAS DE IMPACTO DE INTEGRIDAD SON LAS SIGUIENTES : \n")
print("             - UN TOTAL DE "+str(none_availability_highintegrity_sh_vulnibm)+" VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD ALTO \n")
print("             - UN TOTAL DE "+str(none_availability_lowintegrity_sh_vulnibm)+" VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD BAJO  \n")
print("             - UN TOTAL DE "+str(none_availability_noneintegrity_sh_vulnibm)+" VULNERABILIDADES UNA EXPLOTACIÓN NO TIENE EFECTO EN EL IMPACTO DE INTEGRIDAD \n")
print("\n")
print("\n")




print("************************** PORCENTAJE RELACION IMPACTO DE DISPONIBILIDAD CON IMPACTO DE CONFIDENCIALIDAD E INTEGRIDAD  PARA OBJETOS DE VULNERABILIDADES IBM PARTE SMART HOME********************************")
print("\n")
print(" DE UN TOTAL DE "+str(high_availability_sh_vulnibm+low_availability_sh_vulnibm+none_availability_sh_vulnibm)+" VULNERABILIDADES, LOS PORCENTAJES DE IMPACTO DE DISPONIBILIDAD SON LOS SIGUIENTES: \n")
print("\n")
print(" - EN EL  "+str(float(((high_availability_sh_vulnibm*100)/len( df_vulnibm_sh["x_xfe_cvss_availability_impact"]))))+" % DE LAS VULNERABILIDADES, DONDE EL IMPACTO DE DISPONIBILIDAD ES ALTO : \n")
print("      - LOS PORCENTAJES DE IMPACTO DE CONFIDENCIALIDAD SON LOS SIGUIENTES : \n")
print("             - EL "+str(float(((high_availability_highconfidentiality_sh_vulnibm*100)/(high_availability_sh_vulnibm))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD ALTO \n")
print("             - EL "+str(float(((high_availability_lowconfidentiality_sh_vulnibm*100)/(high_availability_sh_vulnibm))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD BAJO  \n")
print("             - EL "+str(float(((high_availability_noneconfidentiality_sh_vulnibm*100)/(high_availability_sh_vulnibm))))+" % DE LAS VULNERABILIDADES UNA EXPLOTACIÓN NO TIENE EFECTO EN EL IMPACTO DE CONFIDENCIALIDAD  \n")
print("\n")
print("      - LOS PORCENTAJES DE IMPACTO DE INTEGRIDAD SON LOS SIGUIENTES : \n")
print("             - EL "+str(float(((high_availability_highintegrity_sh_vulnibm*100)/(high_availability_sh_vulnibm))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD ALTO \n")
print("             - EL "+str(float(((high_availability_lowintegrity_sh_vulnibm*100)/(high_availability_sh_vulnibm))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD BAJO  \n")
print("             - EL "+str(float(((high_availability_noneintegrity_sh_vulnibm*100)/(high_availability_sh_vulnibm))))+" % DE LAS VULNERABILIDADES UNA EXPLOTACIÓN NO TIENE EFECTO EN EL IMPACTO DE INTEGRIDAD   \n")

print("\n")
print(" - EN EL  "+str(float(((low_availability_sh_vulnibm*100)/len( df_vulnibm_sh["x_xfe_cvss_availability_impact"]))))+" % DE LAS VULNERABILIDADES, DONDE EL IMPACTO DE DISPONIBILIDAD ES BAJO: \n")
print("      - LOS PORCENTAJES DE IMPACTO DE CONFIDENCIALIDAD SON LOS SIGUIENTES : \n")
print("             - EL "+str(float(((low_availability_highconfidentiality_sh_vulnibm*100)/(low_availability_sh_vulnibm))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD ALTO \n")
print("             - EL "+str(float(((low_availability_lowconfidentiality_sh_vulnibm*100)/(low_availability_sh_vulnibm))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD BAJO  \n")
print("             - EL "+str(float(((low_availability_noneconfidentiality_sh_vulnibm*100)/(low_availability_sh_vulnibm))))+" % DE LAS VULNERABILIDADES UNA EXPLOTACIÓN NO TIENE EFECTO EN EL IMPACTO DE CONFIDENCIALIDAD  \n")
print("\n")
print("      - LOS PORCENTAJES DE IMPACTO DE INTEGRIDAD SON LOS SIGUIENTES : \n")
print("             - EL "+str(float(((low_availability_highintegrity_sh_vulnibm*100)/(low_availability_sh_vulnibm))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD ALTO \n")
print("             - EL "+str(float(((low_availability_lowintegrity_sh_vulnibm*100)/(low_availability_sh_vulnibm))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD BAJO  \n")
print("             - EL "+str(float(((low_availability_noneintegrity_sh_vulnibm*100)/(low_availability_sh_vulnibm))))+" % DE LAS VULNERABILIDADES UNA EXPLOTACIÓN NO TIENE EFECTO EN EL IMPACTO DE INTEGRIDAD   \n")


print("\n")
print(" - EN EL  "+str(float(((none_availability_sh_vulnibm*100)/len( df_vulnibm_sh["x_xfe_cvss_availability_impact"]))))+" % DE LAS VULNERABILIDADES, DONDE UNA EXPLOTACIÓN NO TIENE EFECTO EN EL IMPACTO DE DISPONIBILIDAD :  \n")
print("      - LOS PORCENTAJES DE IMPACTO DE CONFIDENCIALIDAD SON LOS SIGUIENTES : \n")
print("             - EL "+str(float(((none_availability_highconfidentiality_sh_vulnibm*100)/(none_availability_sh_vulnibm))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD ALTO \n")
print("             - EL "+str(float(((none_availability_lowconfidentiality_sh_vulnibm*100)/(none_availability_sh_vulnibm))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD BAJO  \n")
print("             - EL "+str(float(((none_availability_noneconfidentiality_sh_vulnibm*100)/(none_availability_sh_vulnibm))))+" % DE LAS VULNERABILIDADES UNA EXPLOTACIÓN NO TIENE EFECTO EN EL IMPACTO DE CONFIDENCIALIDAD  \n")
print("\n")
print("      - LOS PORCENTAJES DE IMPACTO DE INTEGRIDAD SON LOS SIGUIENTES : \n")
print("             - EL "+str(float(((none_availability_highintegrity_sh_vulnibm*100)/(none_availability_sh_vulnibm))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD ALTO \n")
print("             - EL "+str(float(((none_availability_lowintegrity_sh_vulnibm*100)/(none_availability_sh_vulnibm))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD BAJO  \n")
print("             - EL "+str(float(((none_availability_noneintegrity_sh_vulnibm*100)/(none_availability_sh_vulnibm))))+" % DE LAS VULNERABILIDADES UNA EXPLOTACIÓN NO TIENE EFECTO EN EL IMPACTO DE INTEGRIDAD   \n")
print("\n")
print("\n")
print("\n")
























print("**************************ESTADÍSTICAS RELACION IMPACTO DE DISPONIBILIDAD CON IMPACTO DE CONFIDENCIALIDAD E INTEGRIDAD  PARA OBJETOS DE VULNERABILIDADES IBM  PARTE IOT Y SMART HOME CONJUNTAS********************************")
print("\n")
print(" DE UN TOTAL DE "+str(high_availability_sh_vulnibm+low_availability_sh_vulnibm+none_availability_sh_vulnibm+high_availability_iot_vulnibm+low_availability_iot_vulnibm+none_availability_iot_vulnibm)+" VULNERABILIDADES, LAS ESTADÍSTICAS DE IMPACTO DE DISPONIBILIDAD SON LAS SIGUIENTES: \n")
print("\n")
print(" - DE UN TOTAL DE "+str(high_availability_sh_vulnibm+high_availability_iot_vulnibm)+" VULNERABILIDADES DONDE EL IMPACTO DE DISPONIBILIDAD ES ALTO : \n")
print("      - LAS ESTADÍSTICAS DE IMPACTO DE CONFIDENCIALIDAD SON LAS SIGUIENTES : \n")
print("             - UN TOTAL DE "+str(high_availability_highconfidentiality_sh_vulnibm+high_availability_highconfidentiality_iot_vulnibm)+" VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD ALTO \n")
print("             - UN TOTAL DE "+str(high_availability_lowconfidentiality_sh_vulnibm+high_availability_lowconfidentiality_iot_vulnibm)+" VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD BAJO  \n")
print("             - UN TOTAL DE "+str(high_availability_noneconfidentiality_sh_vulnibm+high_availability_noneconfidentiality_iot_vulnibm)+" VULNERABILIDADES UNA EXPLOTACIÓN NO TIENE EFECTO EN EL IMPACTO DE CONFIDENCIALIDAD \n")
print("\n")
print("      - LAS ESTADÍSTICAS DE IMPACTO DE INTEGRIDAD SON LAS SIGUIENTES : \n")
print("             - UN TOTAL DE "+str(high_availability_highintegrity_sh_vulnibm+high_availability_highintegrity_iot_vulnibm)+" VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD ALTO \n")
print("             - UN TOTAL DE "+str(high_availability_lowintegrity_sh_vulnibm+high_availability_lowintegrity_iot_vulnibm)+" VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD BAJO  \n")
print("             - UN TOTAL DE "+str(high_availability_noneintegrity_sh_vulnibm+high_availability_noneintegrity_iot_vulnibm)+" VULNERABILIDADES UNA EXPLOTACIÓN NO TIENE EFECTO EN EL IMPACTO DE INTEGRIDAD \n")


print("\n")
print(" - DE UN TOTAL DE "+str(low_availability_sh_vulnibm+low_availability_iot_vulnibm)+" VULNERABILIDADES DONDE EL IMPACTO DE DISPONIBILIDAD ES BAJO : \n")
print("      - LAS ESTADÍSTICAS DE IMPACTO DE CONFIDENCIALIDAD SON LAS SIGUIENTES : \n")
print("             - UN TOTAL DE "+str(low_availability_highconfidentiality_sh_vulnibm+low_availability_highconfidentiality_iot_vulnibm)+" VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD ALTO \n")
print("             - UN TOTAL DE "+str(low_availability_lowconfidentiality_sh_vulnibm+low_availability_lowconfidentiality_iot_vulnibm)+" VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD BAJO  \n")
print("             - UN TOTAL DE "+str(low_availability_noneconfidentiality_sh_vulnibm+low_availability_noneconfidentiality_iot_vulnibm)+" VULNERABILIDADES UNA EXPLOTACIÓN NO TIENE EFECTO EN EL IMPACTO DE CONFIDENCIALIDAD \n")
print("\n")
print("      - LAS ESTADÍSTICAS DE IMPACTO DE INTEGRIDAD SON LAS SIGUIENTES : \n")
print("             - UN TOTAL DE "+str(low_availability_highintegrity_sh_vulnibm+low_availability_highintegrity_iot_vulnibm)+" VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD ALTO \n")
print("             - UN TOTAL DE "+str(low_availability_lowintegrity_sh_vulnibm+low_availability_lowintegrity_iot_vulnibm)+" VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD BAJO  \n")
print("             - UN TOTAL DE "+str(low_availability_noneintegrity_sh_vulnibm+low_availability_noneintegrity_iot_vulnibm)+" VULNERABILIDADES UNA EXPLOTACIÓN NO TIENE EFECTO EN EL IMPACTO DE INTEGRIDAD \n")


print("\n")
print(" - DE UN TOTAL DE "+str(none_availability_sh_vulnibm+none_availability_sh_vulnibm)+" VULNERABILIDADES DONDE UNA EXPLOTACIÓN NO TIENE EFECTO EN EL IMPACTO DE DISPONIBILIDAD:  \n")
print("      - LAS ESTADÍSTICAS DE IMPACTO DE CONFIDENCIALIDAD SON LAS SIGUIENTES : \n")
print("             - UN TOTAL DE "+str(none_availability_highconfidentiality_sh_vulnibm+none_availability_highconfidentiality_iot_vulnibm)+" VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD ALTO \n")
print("             - UN TOTAL DE "+str(none_availability_lowconfidentiality_sh_vulnibm+none_availability_lowconfidentiality_iot_vulnibm)+" VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD BAJO  \n")
print("             - UN TOTAL DE "+str(none_availability_noneconfidentiality_sh_vulnibm+none_availability_noneconfidentiality_iot_vulnibm)+" VULNERABILIDADES UNA EXPLOTACIÓN NO TIENE EFECTO EN EL IMPACTO DE CONFIDENCIALIDAD \n")
print("\n")
print("      - LAS ESTADÍSTICAS DE IMPACTO DE INTEGRIDAD SON LAS SIGUIENTES : \n")
print("             - UN TOTAL DE "+str(none_availability_highintegrity_sh_vulnibm+none_availability_highintegrity_iot_vulnibm)+" VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD ALTO \n")
print("             - UN TOTAL DE "+str(none_availability_lowintegrity_sh_vulnibm+none_availability_lowintegrity_iot_vulnibm)+" VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD BAJO  \n")
print("             - UN TOTAL DE "+str(none_availability_noneintegrity_sh_vulnibm+none_availability_noneintegrity_iot_vulnibm)+" VULNERABILIDADES UNA EXPLOTACIÓN NO TIENE EFECTO EN EL IMPACTO DE INTEGRIDAD: \n")
print("\n")
print("\n")
print("\n")



print("************************** PORCENTAJES RELACION IMPACTO DE DISPONIBILIDAD CON IMPACTO DE CONFIDENCIALIDAD E INTEGRIDAD  PARA OBJETOS DE VULNERABILIDADES IBM  PARTE IOT Y SMART HOME CONJUNTAS********************************")
print("\n")
print(" DE UN TOTAL DE "+str((len(df_vulnibm_iot["x_xfe_cvss_availability_impact"])+len(df_vulnibm_sh["x_xfe_cvss_availability_impact"])))+" VULNERABILIDADES, LOS PORCENTAJES DE IMPACTO DE DISPONIBILIDAD  SON LOS SIGUIENTES: \n")
print("\n")

print(" - EN EL  "+str(float((((high_availability_iot_vulnibm+high_availability_sh_vulnibm)*100)/(len(df_vulnibm_iot["x_xfe_cvss_availability_impact"])+len(df_vulnibm_sh["x_xfe_cvss_availability_impact"])))))+" % DE LAS VULNERABILIDADES, DONDE EL IMPACTO DE DISPONIBILIDAD ES ALTO :\n")
print("      - LOS PORCENTAJES DE IMPACTO DE CONFIDENCIALIDAD SON LOS SIGUIENTES : \n")
print("             - EL "+str(float((((high_availability_highconfidentiality_sh_vulnibm+high_availability_highconfidentiality_iot_vulnibm)*100)/(high_availability_sh_vulnibm+high_availability_iot_vulnibm))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD ALTO \n")
print("             - EL "+str(float((((high_availability_lowconfidentiality_sh_vulnibm+high_availability_lowconfidentiality_iot_vulnibm)*100)/(high_availability_sh_vulnibm+high_availability_iot_vulnibm))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD BAJO  \n")
print("             - EL "+str(float((((high_availability_noneconfidentiality_sh_vulnibm+high_availability_noneconfidentiality_iot_vulnibm)*100)/(high_availability_sh_vulnibm+high_availability_iot_vulnibm))))+" % DE LAS VULNERABILIDADES UNA EXPLOTACIÓN NO TIENE EFECTO EN EL IMPACTO DE CONFIDENCIALIDAD  \n")
print("\n")
print("      - LOS PORCENTAJES DE IMPACTO DE INTEGRIDAD SON LOS SIGUIENTES : \n")
print("             - EL "+str(float((((high_availability_highintegrity_sh_vulnibm+high_availability_highintegrity_iot_vulnibm)*100)/(high_availability_sh_vulnibm+high_availability_iot_vulnibm))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD ALTO \n")
print("             - EL "+str(float((((high_availability_lowintegrity_sh_vulnibm+high_availability_lowintegrity_iot_vulnibm)*100)/(high_availability_sh_vulnibm+high_availability_iot_vulnibm))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD BAJO  \n")
print("             - EL "+str(float((((high_availability_noneintegrity_sh_vulnibm+high_availability_noneintegrity_iot_vulnibm)*100)/(high_availability_sh_vulnibm+high_availability_iot_vulnibm))))+" % DE LAS VULNERABILIDADES UNA EXPLOTACIÓN NO TIENE EFECTO EN EL IMPACTO DE INTEGRIDAD  \n")

print("\n")
print(" - EN EL  "+str(float((((low_availability_iot_vulnibm+low_availability_sh_vulnibm)*100)/(len( df_vulnibm_iot["x_xfe_cvss_availability_impact"])+len( df_vulnibm_sh["x_xfe_cvss_availability_impact"])))))+" % DE LAS VULNERABILIDADES, DONDE EL IMPACTO DE DISPONIBILIDAD ES BAJO  :\n")
print("      - LOS PORCENTAJES DE IMPACTO DE CONFIDENCIALIDAD SON LOS SIGUIENTES : \n")
print("             - EL "+str(float((((low_availability_highconfidentiality_sh_vulnibm+low_availability_highconfidentiality_iot_vulnibm)*100)/(low_availability_sh_vulnibm+low_availability_iot_vulnibm))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD ALTO \n")
print("             - EL "+str(float((((low_availability_lowconfidentiality_sh_vulnibm+low_availability_lowconfidentiality_iot_vulnibm)*100)/(low_availability_sh_vulnibm+low_availability_iot_vulnibm))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD BAJO  \n")
print("             - EL "+str(float((((low_availability_noneconfidentiality_sh_vulnibm+low_availability_noneconfidentiality_iot_vulnibm)*100)/(low_availability_sh_vulnibm+low_availability_iot_vulnibm))))+" % DE LAS VULNERABILIDADES UNA EXPLOTACIÓN NO TIENE EFECTO EN EL IMPACTO DE CONFIDENCIALIDAD  \n")
print("\n")
print("      - LOS PORCENTAJES DE IMPACTO DE INTEGRIDAD SON LOS SIGUIENTES : \n")
print("             - EL "+str(float((((low_availability_highintegrity_sh_vulnibm+low_availability_highintegrity_iot_vulnibm)*100)/(low_availability_sh_vulnibm+low_availability_iot_vulnibm))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD ALTO \n")
print("             - EL "+str(float((((low_availability_lowintegrity_sh_vulnibm+low_availability_lowintegrity_iot_vulnibm)*100)/(low_availability_sh_vulnibm+low_availability_iot_vulnibm))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD BAJO  \n")
print("             - EL "+str(float((((low_availability_noneintegrity_sh_vulnibm+low_availability_noneintegrity_iot_vulnibm)*100)/(low_availability_sh_vulnibm+low_availability_iot_vulnibm))))+" % DE LAS VULNERABILIDADES UNA EXPLOTACIÓN NO TIENE EFECTO EN EL IMPACTO DE INTEGRIDAD  \n")


print("\n")
print(" - EN EL  "+str(float((((none_availability_sh_vulnibm+none_availability_sh_vulnibm)*100)/(len( df_vulnibm_iot["x_xfe_cvss_availability_impact"])+len( df_vulnibm_sh["x_xfe_cvss_availability_impact"])))))+" % DE LAS VULNERABILIDADES, DONDE UNA EXPLOTACIÓN NO TIENE EFECTO EN EL IMPACTO DE DISPONIBILIDAD  :\n")
print("      - LOS PORCENTAJES DE IMPACTO DE CONFIDENCIALIDAD SON LOS SIGUIENTES : \n")
print("             - EL "+str(float((((none_availability_highconfidentiality_sh_vulnibm+none_availability_highconfidentiality_iot_vulnibm)*100)/(none_availability_sh_vulnibm+none_availability_iot_vulnibm))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD ALTO \n")
print("             - EL "+str(float((((none_availability_lowconfidentiality_sh_vulnibm+none_availability_lowconfidentiality_iot_vulnibm)*100)/(none_availability_sh_vulnibm+none_availability_iot_vulnibm))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE CONFIDENCIALIDAD BAJO  \n")
print("             - EL "+str(float((((none_availability_noneconfidentiality_sh_vulnibm+none_availability_noneconfidentiality_iot_vulnibm)*100)/(none_availability_sh_vulnibm+none_availability_iot_vulnibm))))+" % DE LAS VULNERABILIDADES UNA EXPLOTACIÓN NO TIENE EFECTO EN EL IMPACTO DE CONFIDENCIALIDAD  \n")
print("\n")
print("      - LOS PORCENTAJES DE IMPACTO DE INTEGRIDAD SON LOS SIGUIENTES : \n")
print("             - EL "+str(float((((none_availability_highintegrity_sh_vulnibm+none_availability_highintegrity_iot_vulnibm)*100)/(none_availability_sh_vulnibm+none_availability_iot_vulnibm))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD ALTO \n")
print("             - EL "+str(float((((none_availability_lowintegrity_sh_vulnibm+none_availability_lowintegrity_iot_vulnibm)*100)/(none_availability_sh_vulnibm+none_availability_iot_vulnibm))))+" % DE LAS VULNERABILIDADES TIENEN IMPACTO DE INTEGRIDAD BAJO  \n")
print("             - EL "+str(float((((none_availability_noneintegrity_sh_vulnibm+none_availability_noneintegrity_iot_vulnibm)*100)/(none_availability_sh_vulnibm+none_availability_iot_vulnibm))))+" % DE LAS VULNERABILIDADES UNA EXPLOTACIÓN NO TIENE EFECTO EN EL IMPACTO DE INTEGRIDAD  \n")