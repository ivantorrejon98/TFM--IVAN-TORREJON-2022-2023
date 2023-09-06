

import pandas as pd

#Abro los ficheros con los que voy a tratar


df_cve_iot=pd.read_excel('cves_iot_2023.xlsx')
df_cve_sh=pd.read_excel('cves_smart_home_2023.xlsx')


print("********************RELACION ENTRE COMPLEJIDAD DE ATAQUE, VECTOR DE ATAQUE Y VERSION  CVSSV3 PARTE IOT********************")
#Variables para almacenar los distintos de contadores de version de vector, vector de ataque, complejidad de ataque para la parte IOT
attack_vector_cvssv3_iot=0
attack_vector_cvssv3_0_iot=0
attack_vector_cvssv3_1_iot=0

#Variables donde aumento el contador segun la relacion entre el vector de ataque, su complejidad de ataque y la version
#Por cada tipo de vector de ataque tengo una variable con su version, otra con su complejidad de ataque, y otra donde combina las tres variables
attack_vector_cvssv3_network_iot=0
attack_vector_cvssv3_network3_0_iot=0
attack_vector_cvssv3_network3_1_iot=0
attack_vector_cvssv3_network_low_iot=0
attack_vector_cvssv3_network_low3_0_iot=0
attack_vector_cvssv3_network_low3_1_iot=0
attack_vector_cvssv3_network_high_iot=0
attack_vector_cvssv3_network_high3_0_iot=0
attack_vector_cvssv3_network_high3_1_iot=0
attack_vector_cvssv3_network_medium_iot=0
attack_vector_cvssv3_network_medium3_0_iot=0
attack_vector_cvssv3_network_medium3_1_iot=0

attack_vector_cvssv3_adjacent_iot=0
attack_vector_cvssv3_adjacent3_0_iot=0
attack_vector_cvssv3_adjacent3_1_iot=0
attack_vector_cvssv3_adjacent_low_iot=0
attack_vector_cvssv3_adjacent_low3_0_iot=0
attack_vector_cvssv3_adjacent_low3_1_iot=0
attack_vector_cvssv3_adjacent_high_iot=0
attack_vector_cvssv3_adjacent_high3_0_iot=0
attack_vector_cvssv3_adjacent_high3_1_iot=0
attack_vector_cvssv3_adjacent_medium_iot=0
attack_vector_cvssv3_adjacent_medium3_0_iot=0
attack_vector_cvssv3_adjacent_medium3_1_iot=0

attack_vector_cvssv3_local_iot=0
attack_vector_cvssv3_local3_0_iot=0
attack_vector_cvssv3_local3_1_iot=0
attack_vector_cvssv3_local_low_iot=0
attack_vector_cvssv3_local_low3_0_iot=0
attack_vector_cvssv3_local_low3_1_iot=0
attack_vector_cvssv3_local_high_iot=0
attack_vector_cvssv3_local_high3_0_iot=0
attack_vector_cvssv3_local_high3_1_iot=0
attack_vector_cvssv3_local_medium_iot=0
attack_vector_cvssv3_local_medium3_0_iot=0
attack_vector_cvssv3_local_medium3_1_iot=0

attack_vector_cvssv3_physical_iot=0
attack_vector_cvssv3_physical3_0_iot=0
attack_vector_cvssv3_physical3_1_iot=0
attack_vector_cvssv3_physical_low_iot=0
attack_vector_cvssv3_physical_low3_0_iot=0
attack_vector_cvssv3_physical_low3_1_iot=0
attack_vector_cvssv3_physical_high_iot=0
attack_vector_cvssv3_physical_high3_0_iot=0
attack_vector_cvssv3_physical_high3_1_iot=0
attack_vector_cvssv3_physical_medium_iot=0
attack_vector_cvssv3_physical_medium3_0_iot=0
attack_vector_cvssv3_physical_medium3_1_iot=0




#Recorro cada fila del fichero comprobando valores. Primeramente compruebo que el vector de ataque no sea nulo y aumento el contador

for j in range(0,len(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.attackVector"])):
    if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.attackVector"][j]!='NONE'):
        attack_vector_cvssv3_iot+=1
        #Compruebo si la version del vector es 3.1 o 3.0
        if("3.1" in df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.vectorString"][j]):
            attack_vector_cvssv3_1_iot+=1
            #Compruebo el tipo de vector de ataque
            if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.attackVector"][j]=='NETWORK'):
                attack_vector_cvssv3_network_iot+=1
                attack_vector_cvssv3_network3_1_iot+=1
                #Compruebo la complejidad de ataque
                if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.attackComplexity"][j]=='HIGH'):
                    attack_vector_cvssv3_network_high_iot+=1
                    attack_vector_cvssv3_network_high3_1_iot+=1
                elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.attackComplexity"][j]=='LOW'):
                    attack_vector_cvssv3_network_low_iot+=1
                    attack_vector_cvssv3_network_low3_1_iot+=1
                elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.attackComplexity"][j]=='MEDIUM'):
                    attack_vector_cvssv3_network_medium_iot+=1
                    attack_vector_cvssv3_network_medium3_1_iot+=1        
            elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.attackVector"][j]=='LOCAL'):
                attack_vector_cvssv3_local_iot+=1
                attack_vector_cvssv3_local3_1_iot+=1
                if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.attackComplexity"][j]=='HIGH'):
                    attack_vector_cvssv3_local_high_iot+=1
                    attack_vector_cvssv3_local_high3_1_iot+=1
                elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.attackComplexity"][j]=='LOW'):
                    attack_vector_cvssv3_local_low_iot+=1
                    attack_vector_cvssv3_local_low3_1_iot+=1
                elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.attackComplexity"][j]=='MEDIUM'):
                    attack_vector_cvssv3_local_medium_iot+=1
                    attack_vector_cvssv3_local_medium3_1_iot+=1
                
                
            elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.attackVector"][j]=='PHYSICAL'):
                attack_vector_cvssv3_physical_iot+=1
                attack_vector_cvssv3_physical3_1_iot+=1
                if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.attackComplexity"][j]=='HIGH'):
                    attack_vector_cvssv3_physical_high_iot+=1
                    attack_vector_cvssv3_physical_high3_1_iot+=1
                elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.attackComplexity"][j]=='LOW'):
                    attack_vector_cvssv3_physical_low_iot+=1
                    attack_vector_cvssv3_physical_low3_1_iot+=1
                elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.attackComplexity"][j]=='MEDIUM'):
                    attack_vector_cvssv3_physical_medium_iot+=1
                    attack_vector_cvssv3_physical_medium3_1_iot+=1
            elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.attackVector"][j]=='ADJACENT_NETWORK'):
                attack_vector_cvssv3_adjacent_iot+=1
                attack_vector_cvssv3_adjacent3_1_iot+=1
                if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.attackComplexity"][j]=='HIGH'):
                    attack_vector_cvssv3_adjacent_high_iot+=1
                    attack_vector_cvssv3_adjacent_high3_1_iot+=1
                elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.attackComplexity"][j]=='LOW'):
                    attack_vector_cvssv3_adjacent_low_iot+=1
                    attack_vector_cvssv3_adjacent_low3_1_iot+=1
                elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.attackComplexity"][j]=='MEDIUM'):
                    attack_vector_cvssv3_adjacent_medium_iot+=1
                    attack_vector_cvssv3_adjacent_medium3_1_iot+=1
        else:
            if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.vectorString"][j]!='NONE'):
                attack_vector_cvssv3_0_iot+=1
                if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.attackVector"][j]=='NETWORK'):
                    attack_vector_cvssv3_network_iot+=1
                    attack_vector_cvssv3_network3_0_iot+=1
                    if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.attackComplexity"][j]=='HIGH'):
                        attack_vector_cvssv3_network_high_iot+=1
                        attack_vector_cvssv3_network_high3_0_iot+=1
                    elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.attackComplexity"][j]=='LOW'):
                        attack_vector_cvssv3_network_low_iot+=1
                        attack_vector_cvssv3_network_low3_0_iot+=1
                    elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.attackComplexity"][j]=='MEDIUM'):
                        attack_vector_cvssv3_network_medium_iot+=1
                        attack_vector_cvssv3_network_medium3_0_iot+=1        
                elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.attackVector"][j]=='LOCAL'):
                    attack_vector_cvssv3_local_iot+=1
                    attack_vector_cvssv3_local3_0_iot+=1
                    if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.attackComplexity"][j]=='HIGH'):
                        attack_vector_cvssv3_local_high_iot+=1
                        attack_vector_cvssv3_local_high3_0_iot+=1
                    elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.attackComplexity"][j]=='LOW'):
                        attack_vector_cvssv3_local_low_iot+=1
                        attack_vector_cvssv3_local_low3_0_iot+=1
                    elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.attackComplexity"][j]=='MEDIUM'):
                        attack_vector_cvssv3_local_medium_iot+=1
                        attack_vector_cvssv3_local_medium3_0_iot+=1


                elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.attackVector"][j]=='PHYSICAL'):
                    attack_vector_cvssv3_physical_iot+=1
                    attack_vector_cvssv3_physical3_0_iot+=1
                    if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.attackComplexity"][j]=='HIGH'):
                        attack_vector_cvssv3_physical_high_iot+=1
                        attack_vector_cvssv3_physical_high3_0_iot+=1
                    elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.attackComplexity"][j]=='LOW'):
                        attack_vector_cvssv3_physical_low_iot+=1
                        attack_vector_cvssv3_physical_low3_0_iot+=1
                    elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.attackComplexity"][j]=='MEDIUM'):
                        attack_vector_cvssv3_physical_medium_iot+=1
                        attack_vector_cvssv3_physical_medium3_0_iot+=1
                elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.attackVector"][j]=='ADJACENT_NETWORK'):
                    attack_vector_cvssv3_adjacent_iot+=1
                    attack_vector_cvssv3_adjacent3_0_iot+=1
                    if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.attackComplexity"][j]=='HIGH'):
                        attack_vector_cvssv3_adjacent_high_iot+=1
                        attack_vector_cvssv3_adjacent_high3_0_iot+=1
                    elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.attackComplexity"][j]=='LOW'):
                        attack_vector_cvssv3_adjacent_low_iot+=1
                        attack_vector_cvssv3_adjacent_low3_0_iot+=1
                    elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.attackComplexity"][j]=='MEDIUM'):
                        attack_vector_cvssv3_adjacent_medium_iot+=1
                        attack_vector_cvssv3_adjacent_medium3_0_iot+=1
                        
                        
                        
                        
print("************************** ESTADÍSTICAS VERSIONVERSION VECTOR CVSSV3/VECTOR DE ATAQUE/COMPLEJIDAD DE ATAQUE CVSSV3 CVE IOT********************************")
print("\n")
print(" DE UN TOTAL DE "+str(attack_vector_cvssv3_iot)+" VECTORES DE ATAQUE, LAS ESTADÍSTICAS DE VECTOR DE ATAQUE SON LAS SIGUIENTES: \n")
print("\n")
print(" - EN UN TOTAL DE "+str(attack_vector_cvssv3_network_iot)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES NETWORK. "+str(attack_vector_cvssv3_network3_1_iot)+" CON LA VERSIÓN CVSS 3.1 Y "+str(attack_vector_cvssv3_network3_0_iot)+" CON LA VERSIÓN CVSS 3.0 \n")
print(" - EN UN TOTAL DE "+str(attack_vector_cvssv3_local_iot)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES LOCAL. "+str(attack_vector_cvssv3_local3_1_iot)+" CON LA VERSIÓN CVSS 3.1 Y "+str(attack_vector_cvssv3_local3_0_iot)+" CON LA VERSIÓN CVSS 3.0 \n")
print(" - EN UN TOTAL DE "+str(attack_vector_cvssv3_physical_iot)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES FÍSICO. "+str(attack_vector_cvssv3_physical3_1_iot)+" CON LA VERSIÓN CVSS 3.1 Y "+str(attack_vector_cvssv3_physical3_0_iot)+" CON LA VERSIÓN CVSS 3.0 \n")
print(" - EN UN TOTAL DE "+str(attack_vector_cvssv3_adjacent_iot)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES ADYACENTE. "+str(attack_vector_cvssv3_adjacent3_1_iot)+" CON LA VERSIÓN CVSS 3.1 Y "+str(attack_vector_cvssv3_adjacent3_0_iot)+" CON LA VERSIÓN CVSS 3.0 \n")
print("\n")

print("***********************************************************************************************************************************")
print(" - UN TOTAL DE "+str(attack_vector_cvssv3_1_iot)+" VECTORES CVSSV3 TIENEN LA VERSION CVSS 3.1. DE ESTOS VECTORES, LAS ESTADÍSTICAS DE VECTOR DE ATAQUE SON LAS SIGUIENTES :\n")
print("\n")
print("       -    EN UN TOTAL DE "+str(attack_vector_cvssv3_network3_1_iot)+" VULNERABILIDADES CUYA VERSIÓN DE VECTOR DE ATAQUE ES 3.1, EL VECTOR DE ATAQUE ES NETWORK. DE ESTAS VULNERABILIDADES, LAS ESTADÍSTICAS DE COMPLEJIDAD DE ATAQUE SON LAS SIGUIENTES \n")
print("                   -    EN UN TOTAL DE "+str(attack_vector_cvssv3_network_high3_1_iot)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
print("                   -    EN UN TOTAL DE "+str(attack_vector_cvssv3_network_low3_1_iot)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
print("                   -    EN UN TOTAL DE "+str(attack_vector_cvssv3_network_medium3_1_iot)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA \n")

print("\n")
print("       -    EN UN TOTAL DE "+str(attack_vector_cvssv3_local3_1_iot)+" VULNERABILIDADES CUYA VERSIÓN DE VECTOR DE ATAQUE ES 3.1, EL VECTOR DE ATAQUE ES LOCAL. DE ESTAS VULNERABILIDADES, LAS ESTADÍSTICAS DE COMPLEJIDAD DE ATAQUE SON LAS SIGUIENTES \n")
print("                   -    EN UN TOTAL DE "+str(attack_vector_cvssv3_local_high3_1_iot)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
print("                   -    EN UN TOTAL DE "+str(attack_vector_cvssv3_local_low3_1_iot)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
print("                   -    EN UN TOTAL DE "+str(attack_vector_cvssv3_local_medium3_1_iot)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA \n")


print("\n")
print("       -    EN UN TOTAL DE "+str(attack_vector_cvssv3_physical3_1_iot)+" VULNERABILIDADES CUYA VERSIÓN DE VECTOR DE ATAQUE ES 3.1, EL VECTOR DE ATAQUE ES FÍSICO. DE ESTAS VULNERABILIDADES, LAS ESTADÍSTICAS DE COMPLEJIDAD DE ATAQUE SON LAS SIGUIENTES \n")
print("                   -    EN UN TOTAL DE "+str(attack_vector_cvssv3_physical_high3_1_iot)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
print("                   -    EN UN TOTAL DE "+str(attack_vector_cvssv3_physical_low3_1_iot)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
print("                   -    EN UN TOTAL DE "+str(attack_vector_cvssv3_physical_medium3_1_iot)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA \n")


print("\n")
print("       -    EN UN TOTAL DE "+str(attack_vector_cvssv3_adjacent3_1_iot)+" VULNERABILIDADES CUYA VERSIÓN DE VECTOR DE ATAQUE ES 3.1, EL VECTOR DE ATAQUE ES ADYACENTE. DE ESTAS VULNERABILIDADES, LAS ESTADÍSTICAS DE COMPLEJIDAD DE ATAQUE SON LAS SIGUIENTES \n")
print("                   -    EN UN TOTAL DE "+str(attack_vector_cvssv3_adjacent_high3_1_iot)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
print("                   -    EN UN TOTAL DE "+str(attack_vector_cvssv3_adjacent_low3_1_iot)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
print("                   -    EN UN TOTAL DE "+str(attack_vector_cvssv3_adjacent_medium3_1_iot)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA \n")


print("***********************************************************************************************************************************")
print(" - UN TOTAL DE "+str(attack_vector_cvssv3_0_iot)+" VECTORES CVSSV3 TIENEN LA VERSION CVSS 3.0. DE ESTOS VECTORES, LAS ESTADÍSTICAS DE VECTOR DE ATAQUE SON LAS SIGUIENTES :\n")
print("\n")
print("       -    EN UN TOTAL DE "+str(attack_vector_cvssv3_network3_0_iot)+" VULNERABILIDADES CUYA VERSIÓN DE VECTOR DE ATAQUE ES 3.0, EL VECTOR DE ATAQUE ES NETWORK. DE ESTAS VULNERABILIDADES, LAS ESTADÍSTICAS DE COMPLEJIDAD DE ATAQUE SON LAS SIGUIENTES \n")
print("                   -    EN UN TOTAL DE "+str(attack_vector_cvssv3_network_high3_0_iot)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
print("                   -    EN UN TOTAL DE "+str(attack_vector_cvssv3_network_low3_0_iot)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
print("                   -    EN UN TOTAL DE "+str(attack_vector_cvssv3_network_medium3_0_iot)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA \n")

print("\n")
print("       -    EN UN TOTAL DE "+str(attack_vector_cvssv3_local3_0_iot)+" VULNERABILIDADES CUYA VERSIÓN DE VECTOR DE ATAQUE ES 3.0, EL VECTOR DE ATAQUE ES LOCAL. DE ESTAS VULNERABILIDADES, LAS ESTADÍSTICAS DE COMPLEJIDAD DE ATAQUE SON LAS SIGUIENTES \n")
print("                   -    EN UN TOTAL DE "+str(attack_vector_cvssv3_local_high3_0_iot)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
print("                   -    EN UN TOTAL DE "+str(attack_vector_cvssv3_local_low3_0_iot)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
print("                   -    EN UN TOTAL DE "+str(attack_vector_cvssv3_local_medium3_0_iot)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA \n")


print("\n")
print("       -    EN UN TOTAL DE "+str(attack_vector_cvssv3_physical3_0_iot)+" VULNERABILIDADES CUYA VERSIÓN DE VECTOR DE ATAQUE ES 3.0, EL VECTOR DE ATAQUE ES FÍSICO. DE ESTAS VULNERABILIDADES, LAS ESTADÍSTICAS DE COMPLEJIDAD DE ATAQUE SON LAS SIGUIENTES \n")
print("                   -    EN UN TOTAL DE "+str(attack_vector_cvssv3_physical_high3_0_iot)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
print("                   -    EN UN TOTAL DE "+str(attack_vector_cvssv3_physical_low3_0_iot)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
print("                   -    EN UN TOTAL DE "+str(attack_vector_cvssv3_physical_medium3_0_iot)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA \n")


print("\n")
print("       -    EN UN TOTAL DE "+str(attack_vector_cvssv3_adjacent3_0_iot)+" VULNERABILIDADES CUYA VERSIÓN DE VECTOR DE ATAQUE ES 3.0, EL VECTOR DE ATAQUE ES ADYACENTE. DE ESTAS VULNERABILIDADES, LAS ESTADÍSTICAS DE COMPLEJIDAD DE ATAQUE SON LAS SIGUIENTES \n")
print("                   -    EN UN TOTAL DE "+str(attack_vector_cvssv3_adjacent_high3_0_iot)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
print("                   -    EN UN TOTAL DE "+str(attack_vector_cvssv3_adjacent_low3_0_iot)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
print("                   -    EN UN TOTAL DE "+str(attack_vector_cvssv3_adjacent_medium3_0_iot)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA \n")
print("\n")










print("**************************PORCENTAJES VERSION VECTOR CVSSV3/VECTOR DE ATAQUE/COMPLEJIDAD DE ATAQUE CVSSV3 CVE IOT********************************")
print("\n")
print(" DE UN TOTAL DE "+str(attack_vector_cvssv3_iot)+" VECTORES DE ATAQUE, LAS ESTADÍSTICAS DE PORCENTAJES DE VECTOR DE ATAQUE SON LAS SIGUIENTES: \n")
print("\n")
print(" - EN EL "+str(float(((attack_vector_cvssv3_network_iot*100)/(attack_vector_cvssv3_iot))))+" % DE VULNERABILIDADES EL VECTOR DE ATAQUE ES NETWORK.  EL "+str(float(((attack_vector_cvssv3_network3_1_iot*100)/(attack_vector_cvssv3_network_iot))))+" % DE ELLOS CON LA VERSIÓN CVSS 3.1 Y EL "+str(float(((attack_vector_cvssv3_network3_0_iot*100)/(attack_vector_cvssv3_network_iot))))+" % CON LA VERSIÓN CVSS 3.0 \n")
print(" - EN EL "+str(float(((attack_vector_cvssv3_local_iot*100)/(attack_vector_cvssv3_iot))))+" % DE VULNERABILIDADES EL VECTOR DE ATAQUE ES LOCAL. EL "+str(float(((attack_vector_cvssv3_local3_1_iot*100)/(attack_vector_cvssv3_local_iot))))+" % DE ELLOS CON LA VERSIÓN CVSS 3.1 Y EL "+str(float(((attack_vector_cvssv3_local3_0_iot*100)/(attack_vector_cvssv3_local_iot))))+" % CON LA VERSIÓN CVSS 3.0 \n")
print(" - EN EL "+str(float(((attack_vector_cvssv3_physical_iot*100)/(attack_vector_cvssv3_iot))))+" % DE VULNERABILIDADES EL VECTOR DE ATAQUE ES FÍSICO. EL "+str(float(((attack_vector_cvssv3_physical3_1_iot*100)/(attack_vector_cvssv3_physical_iot))))+" % DE ELLOS CON LA VERSIÓN CVSS 3.1 Y EL "+str(float(((attack_vector_cvssv3_physical3_0_iot*100)/(attack_vector_cvssv3_physical_iot))))+" % CON LA VERSIÓN CVSS 3.0 \n")
print(" - EN EL "+str(float(((attack_vector_cvssv3_adjacent_iot*100)/(attack_vector_cvssv3_iot))))+" % DE VULNERABILIDADES EL VECTOR DE ATAQUE ES ADYACENTE. EL "+str(float(((attack_vector_cvssv3_adjacent3_1_iot*100)/(attack_vector_cvssv3_adjacent_iot))))+" % DE ELLOS CON LA VERSIÓN CVSS 3.1 Y EL "+str(float(((attack_vector_cvssv3_adjacent3_0_iot*100)/(attack_vector_cvssv3_adjacent_iot))))+" % CON LA VERSIÓN CVSS 3.0 \n")
print("\n")
print("***********************************************************************************************************************************")
print(" - EL "+str(float(((attack_vector_cvssv3_1_iot*100)/(attack_vector_cvssv3_iot))))+" % DEL TOTAL DE VECTORES CVSSV3 TIENEN LA VERSION CVSS 3.1. DE ESTOS VECTORES, LAS ESTADÍSTICAS DE PORCENTAJE DE VECTOR DE ATAQUE SON LAS SIGUIENTES :\n")
print("\n")
print("       -    EN EL "+str(float(((attack_vector_cvssv3_network3_1_iot*100)/(attack_vector_cvssv3_1_iot))))+" % VULNERABILIDADES CUYA VERSIÓN DE VECTOR DE ATAQUE ES 3.1, EL VECTOR DE ATAQUE ES NETWORK. DE ESTAS VULNERABILIDADES, LAS ESTADÍSTICAS DE PORCENTAJES DE COMPLEJIDAD DE ATAQUE SON LAS SIGUIENTES :\n")
print("                   -    EN EL "+str(float(((attack_vector_cvssv3_network_high3_1_iot*100)/(attack_vector_cvssv3_network3_1_iot))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
print("                   -    EN EL "+str(float(((attack_vector_cvssv3_network_low3_1_iot*100)/(attack_vector_cvssv3_network3_1_iot))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
print("                   -    EN EL "+str(float(((attack_vector_cvssv3_network_medium3_1_iot*100)/(attack_vector_cvssv3_network3_1_iot))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA \n")

print("\n")
print("       -    EN EL "+str(float(((attack_vector_cvssv3_local3_1_iot*100)/(attack_vector_cvssv3_1_iot))))+" % VULNERABILIDADES CUYA VERSIÓN DE VECTOR DE ATAQUE ES 3.1, EL VECTOR DE ATAQUE ES LOCAL. DE ESTAS VULNERABILIDADES, LAS ESTADÍSTICAS DE PORCENTAJES DE COMPLEJIDAD DE ATAQUE SON LAS SIGUIENTES :\n")
print("                   -    EN EL "+str(float(((attack_vector_cvssv3_local_high3_1_iot*100)/(attack_vector_cvssv3_local3_1_iot))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
print("                   -    EN EL "+str(float(((attack_vector_cvssv3_local_low3_1_iot*100)/(attack_vector_cvssv3_local3_1_iot))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
print("                   -    EN EL "+str(float(((attack_vector_cvssv3_local_medium3_1_iot*100)/(attack_vector_cvssv3_local3_1_iot))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA \n")


print("       -    EN EL "+str(float(((attack_vector_cvssv3_physical3_1_iot*100)/(attack_vector_cvssv3_1_iot))))+" % VULNERABILIDADES CUYA VERSIÓN DE VECTOR DE ATAQUE ES 3.1, EL VECTOR DE ATAQUE ES FÍSICO. DE ESTAS VULNERABILIDADES, LAS ESTADÍSTICAS DE PORCENTAJES DE COMPLEJIDAD DE ATAQUE SON LAS SIGUIENTES :\n")
print("                   -    EN EL "+str(float(((attack_vector_cvssv3_physical_high3_1_iot*100)/(attack_vector_cvssv3_physical3_1_iot))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
print("                   -    EN EL "+str(float(((attack_vector_cvssv3_physical_low3_1_iot*100)/(attack_vector_cvssv3_physical3_1_iot))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
print("                   -    EN EL "+str(float(((attack_vector_cvssv3_physical_medium3_1_iot*100)/(attack_vector_cvssv3_physical3_1_iot))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA \n")


print("       -    EN EL "+str(float(((attack_vector_cvssv3_adjacent3_1_iot*100)/(attack_vector_cvssv3_1_iot))))+" % VULNERABILIDADES CUYA VERSIÓN DE VECTOR DE ATAQUE ES 3.1, EL VECTOR DE ATAQUE ES ADYACENTE. DE ESTAS VULNERABILIDADES, LAS ESTADÍSTICAS DE PORCENTAJES DE COMPLEJIDAD DE ATAQUE SON LAS SIGUIENTES :\n")
print("                   -    EN EL "+str(float(((attack_vector_cvssv3_adjacent_high3_1_iot*100)/(attack_vector_cvssv3_adjacent3_1_iot))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
print("                   -    EN EL "+str(float(((attack_vector_cvssv3_adjacent_low3_1_iot*100)/(attack_vector_cvssv3_adjacent3_1_iot))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
print("                   -    EN EL "+str(float(((attack_vector_cvssv3_adjacent_medium3_1_iot*100)/(attack_vector_cvssv3_adjacent3_1_iot))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA \n")



print("***********************************************************************************************************************************")
print(" - EL "+str(float(((attack_vector_cvssv3_0_iot*100)/(attack_vector_cvssv3_iot))))+" % DEL TOTAL DE VECTORES CVSSV3 TIENEN LA VERSION CVSS 3.0. DE ESTOS VECTORES, LAS ESTADÍSTICAS DE PORCENTAJE DE VECTOR DE ATAQUE SON LAS SIGUIENTES :\n")
print("\n")
print("       -    EN EL "+str(float(((attack_vector_cvssv3_network3_0_iot*100)/(attack_vector_cvssv3_0_iot))))+" % VULNERABILIDADES CUYA VERSIÓN DE VECTOR DE ATAQUE ES 3.0, EL VECTOR DE ATAQUE ES NETWORK. DE ESTAS VULNERABILIDADES, LAS ESTADÍSTICAS DE PORCENTAJES DE COMPLEJIDAD DE ATAQUE SON LAS SIGUIENTES :\n")
print("                   -    EN EL "+str(float(((attack_vector_cvssv3_network_high3_0_iot*100)/(attack_vector_cvssv3_network3_0_iot))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
print("                   -    EN EL "+str(float(((attack_vector_cvssv3_network_low3_0_iot*100)/(attack_vector_cvssv3_network3_0_iot))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
print("                   -    EN EL "+str(float(((attack_vector_cvssv3_network_medium3_0_iot*100)/(attack_vector_cvssv3_network3_0_iot))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA \n")

print("\n")
print("       -    EN EL "+str(float(((attack_vector_cvssv3_local3_0_iot*100)/(attack_vector_cvssv3_0_iot))))+" % VULNERABILIDADES CUYA VERSIÓN DE VECTOR DE ATAQUE ES 3.0, EL VECTOR DE ATAQUE ES LOCAL. DE ESTAS VULNERABILIDADES, LAS ESTADÍSTICAS DE PORCENTAJES DE COMPLEJIDAD DE ATAQUE SON LAS SIGUIENTES :\n")
print("                   -    EN EL "+str(float(((attack_vector_cvssv3_local_high3_0_iot*100)/(attack_vector_cvssv3_local3_0_iot))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
print("                   -    EN EL "+str(float(((attack_vector_cvssv3_local_low3_0_iot*100)/(attack_vector_cvssv3_local3_0_iot))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
print("                   -    EN EL "+str(float(((attack_vector_cvssv3_local_medium3_0_iot*100)/(attack_vector_cvssv3_local3_0_iot))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA \n")


print("       -    EN EL "+str(float(((attack_vector_cvssv3_physical3_0_iot*100)/(attack_vector_cvssv3_0_iot))))+" % VULNERABILIDADES CUYA VERSIÓN DE VECTOR DE ATAQUE ES 3.0, EL VECTOR DE ATAQUE ES FÍSICO. DE ESTAS VULNERABILIDADES, LAS ESTADÍSTICAS DE PORCENTAJES DE COMPLEJIDAD DE ATAQUE SON LAS SIGUIENTES :\n")
print("                   -    EN EL "+str(float(((attack_vector_cvssv3_physical_high3_0_iot*100)/(attack_vector_cvssv3_physical3_0_iot))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
print("                   -    EN EL "+str(float(((attack_vector_cvssv3_physical_low3_0_iot*100)/(attack_vector_cvssv3_physical3_0_iot))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
print("                   -    EN EL "+str(float(((attack_vector_cvssv3_physical_medium3_0_iot*100)/(attack_vector_cvssv3_physical3_0_iot))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA \n")


print("       -    EN EL "+str(float(((attack_vector_cvssv3_adjacent3_0_iot*100)/(attack_vector_cvssv3_0_iot))))+" % VULNERABILIDADES CUYA VERSIÓN DE VECTOR DE ATAQUE ES 3.0, EL VECTOR DE ATAQUE ES ADYACENTE. DE ESTAS VULNERABILIDADES, LAS ESTADÍSTICAS DE PORCENTAJES DE COMPLEJIDAD DE ATAQUE SON LAS SIGUIENTES :\n")
print("                   -    EN EL "+str(float(((attack_vector_cvssv3_adjacent_high3_0_iot*100)/(attack_vector_cvssv3_adjacent3_0_iot))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
print("                   -    EN EL "+str(float(((attack_vector_cvssv3_adjacent_low3_0_iot*100)/(attack_vector_cvssv3_adjacent3_0_iot))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
print("                   -    EN EL "+str(float(((attack_vector_cvssv3_adjacent_medium3_0_iot*100)/(attack_vector_cvssv3_adjacent3_0_iot))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA \n")


print("\n")



print("********************RELACION ENTRE COMPLEJIDAD DE ATAQUE, VECTOR DE ATAQUE Y VERSION  CVSSV3 PARTE SMART HOME********************")
#Variables para almacenar los distintos de contadores de version de vector, vector de ataque, complejidad de ataque para la parte SMART HOME
attack_vector_cvssv3_sh=0
attack_vector_cvssv3_0_sh=0
attack_vector_cvssv3_1_sh=0

#Variables donde aumento el contador segun la relacion entre el vector de ataque, su complejidad de ataque y la version
#Por cada tipo de vector de ataque tengo una variable con su version, otra con su complejidad de ataque, y otra donde combina las tres variables
attack_vector_cvssv3_network_sh=0
attack_vector_cvssv3_network3_0_sh=0
attack_vector_cvssv3_network3_1_sh=0
attack_vector_cvssv3_network_low_sh=0
attack_vector_cvssv3_network_low3_0_sh=0
attack_vector_cvssv3_network_low3_1_sh=0
attack_vector_cvssv3_network_high_sh=0
attack_vector_cvssv3_network_high3_0_sh=0
attack_vector_cvssv3_network_high3_1_sh=0
attack_vector_cvssv3_network_medium_sh=0
attack_vector_cvssv3_network_medium3_0_sh=0
attack_vector_cvssv3_network_medium3_1_sh=0

attack_vector_cvssv3_adjacent_sh=0
attack_vector_cvssv3_adjacent3_0_sh=0
attack_vector_cvssv3_adjacent3_1_sh=0
attack_vector_cvssv3_adjacent_low_sh=0
attack_vector_cvssv3_adjacent_low3_0_sh=0
attack_vector_cvssv3_adjacent_low3_1_sh=0
attack_vector_cvssv3_adjacent_high_sh=0
attack_vector_cvssv3_adjacent_high3_0_sh=0
attack_vector_cvssv3_adjacent_high3_1_sh=0
attack_vector_cvssv3_adjacent_medium_sh=0
attack_vector_cvssv3_adjacent_medium3_0_sh=0
attack_vector_cvssv3_adjacent_medium3_1_sh=0

attack_vector_cvssv3_local_sh=0
attack_vector_cvssv3_local3_0_sh=0
attack_vector_cvssv3_local3_1_sh=0
attack_vector_cvssv3_local_low_sh=0
attack_vector_cvssv3_local_low3_0_sh=0
attack_vector_cvssv3_local_low3_1_sh=0
attack_vector_cvssv3_local_high_sh=0
attack_vector_cvssv3_local_high3_0_sh=0
attack_vector_cvssv3_local_high3_1_sh=0
attack_vector_cvssv3_local_medium_sh=0
attack_vector_cvssv3_local_medium3_0_sh=0
attack_vector_cvssv3_local_medium3_1_sh=0

attack_vector_cvssv3_physical_sh=0
attack_vector_cvssv3_physical3_0_sh=0
attack_vector_cvssv3_physical3_1_sh=0
attack_vector_cvssv3_physical_low_sh=0
attack_vector_cvssv3_physical_low3_0_sh=0
attack_vector_cvssv3_physical_low3_1_sh=0
attack_vector_cvssv3_physical_high_sh=0
attack_vector_cvssv3_physical_high3_0_sh=0
attack_vector_cvssv3_physical_high3_1_sh=0
attack_vector_cvssv3_physical_medium_sh=0
attack_vector_cvssv3_physical_medium3_0_sh=0
attack_vector_cvssv3_physical_medium3_1_sh=0




#Recorro cada fila del fichero comprobando valores. Primeramente compruebo que el vector de ataque no sea nulo y aumento el contador

for j in range(0,len(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.attackVector"])):
    if(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.attackVector"][j]!='NONE'):
        attack_vector_cvssv3_sh+=1
        #Compruebo si la version del vector es 3.1 o 3.0
        if("3.1" in df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.vectorString"][j]):
            attack_vector_cvssv3_1_sh+=1
            #Compruebo el tipo de vector de ataque
            if(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.attackVector"][j]=='NETWORK'):
                attack_vector_cvssv3_network_sh+=1
                attack_vector_cvssv3_network3_1_sh+=1
                #Compruebo la complejidad de ataque
                if(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.attackComplexity"][j]=='HIGH'):
                    attack_vector_cvssv3_network_high_sh+=1
                    attack_vector_cvssv3_network_high3_1_sh+=1
                elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.attackComplexity"][j]=='LOW'):
                    attack_vector_cvssv3_network_low_sh+=1
                    attack_vector_cvssv3_network_low3_1_sh+=1
                elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.attackComplexity"][j]=='MEDIUM'):
                    attack_vector_cvssv3_network_medium_sh+=1
                    attack_vector_cvssv3_network_medium3_1_sh+=1        
            elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.attackVector"][j]=='LOCAL'):
                attack_vector_cvssv3_local_sh+=1
                attack_vector_cvssv3_local3_1_sh+=1
                if(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.attackComplexity"][j]=='HIGH'):
                    attack_vector_cvssv3_local_high_sh+=1
                    attack_vector_cvssv3_local_high3_1_sh+=1
                elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.attackComplexity"][j]=='LOW'):
                    attack_vector_cvssv3_local_low_sh+=1
                    attack_vector_cvssv3_local_low3_1_sh+=1
                elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.attackComplexity"][j]=='MEDIUM'):
                    attack_vector_cvssv3_local_medium_sh+=1
                    attack_vector_cvssv3_local_medium3_1_sh+=1
                
                
            elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.attackVector"][j]=='PHYSICAL'):
                attack_vector_cvssv3_physical_sh+=1
                attack_vector_cvssv3_physical3_1_sh+=1
                if(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.attackComplexity"][j]=='HIGH'):
                    attack_vector_cvssv3_physical_high_sh+=1
                    attack_vector_cvssv3_physical_high3_1_sh+=1
                elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.attackComplexity"][j]=='LOW'):
                    attack_vector_cvssv3_physical_low_sh+=1
                    attack_vector_cvssv3_physical_low3_1_sh+=1
                elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.attackComplexity"][j]=='MEDIUM'):
                    attack_vector_cvssv3_physical_medium_sh+=1
                    attack_vector_cvssv3_physical_medium3_1_sh+=1
            elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.attackVector"][j]=='ADJACENT_NETWORK'):
                attack_vector_cvssv3_adjacent_sh+=1
                attack_vector_cvssv3_adjacent3_1_sh+=1
                if(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.attackComplexity"][j]=='HIGH'):
                    attack_vector_cvssv3_adjacent_high_sh+=1
                    attack_vector_cvssv3_adjacent_high3_1_sh+=1
                elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.attackComplexity"][j]=='LOW'):
                    attack_vector_cvssv3_adjacent_low_sh+=1
                    attack_vector_cvssv3_adjacent_low3_1_sh+=1
                elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.attackComplexity"][j]=='MEDIUM'):
                    attack_vector_cvssv3_adjacent_medium_sh+=1
                    attack_vector_cvssv3_adjacent_medium3_1_sh+=1
        else:
            if(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.vectorString"][j]!='NONE'):
                attack_vector_cvssv3_0_sh+=1
                if(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.attackVector"][j]=='NETWORK'):
                    attack_vector_cvssv3_network_sh+=1
                    attack_vector_cvssv3_network3_0_sh+=1
                    if(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.attackComplexity"][j]=='HIGH'):
                        attack_vector_cvssv3_network_high_sh+=1
                        attack_vector_cvssv3_network_high3_0_sh+=1
                    elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.attackComplexity"][j]=='LOW'):
                        attack_vector_cvssv3_network_low_sh+=1
                        attack_vector_cvssv3_network_low3_0_sh+=1
                    elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.attackComplexity"][j]=='MEDIUM'):
                        attack_vector_cvssv3_network_medium_sh+=1
                        attack_vector_cvssv3_network_medium3_0_sh+=1        
                elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.attackVector"][j]=='LOCAL'):
                    attack_vector_cvssv3_local_sh+=1
                    attack_vector_cvssv3_local3_0_sh+=1
                    if(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.attackComplexity"][j]=='HIGH'):
                        attack_vector_cvssv3_local_high_sh+=1
                        attack_vector_cvssv3_local_high3_0_sh+=1
                    elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.attackComplexity"][j]=='LOW'):
                        attack_vector_cvssv3_local_low_sh+=1
                        attack_vector_cvssv3_local_low3_0_sh+=1
                    elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.attackComplexity"][j]=='MEDIUM'):
                        attack_vector_cvssv3_local_medium_sh+=1
                        attack_vector_cvssv3_local_medium3_0_sh+=1


                elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.attackVector"][j]=='PHYSICAL'):
                    attack_vector_cvssv3_physical_sh+=1
                    attack_vector_cvssv3_physical3_0_sh+=1
                    if(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.attackComplexity"][j]=='HIGH'):
                        attack_vector_cvssv3_physical_high_sh+=1
                        attack_vector_cvssv3_physical_high3_0_sh+=1
                    elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.attackComplexity"][j]=='LOW'):
                        attack_vector_cvssv3_physical_low_sh+=1
                        attack_vector_cvssv3_physical_low3_0_sh+=1
                    elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.attackComplexity"][j]=='MEDIUM'):
                        attack_vector_cvssv3_physical_medium_sh+=1
                        attack_vector_cvssv3_physical_medium3_0_sh+=1
                elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.attackVector"][j]=='ADJACENT_NETWORK'):
                    attack_vector_cvssv3_adjacent_sh+=1
                    attack_vector_cvssv3_adjacent3_0_sh+=1
                    if(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.attackComplexity"][j]=='HIGH'):
                        attack_vector_cvssv3_adjacent_high_sh+=1
                        attack_vector_cvssv3_adjacent_high3_0_sh+=1
                    elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.attackComplexity"][j]=='LOW'):
                        attack_vector_cvssv3_adjacent_low_sh+=1
                        attack_vector_cvssv3_adjacent_low3_0_sh+=1
                    elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.attackComplexity"][j]=='MEDIUM'):
                        attack_vector_cvssv3_adjacent_medium_sh+=1
                        attack_vector_cvssv3_adjacent_medium3_0_sh+=1
                        
                        
                        
                        
print("************************** ESTADÍSTICAS VERSION VECTOR CVSSV3/VECTOR DE ATAQUE/COMPLEJIDAD DE ATAQUE CVSSV3 CVE SMART HOME********************************")
print("\n")
print(" DE UN TOTAL DE "+str(attack_vector_cvssv3_sh)+" VECTORES DE ATAQUE, LAS ESTADÍSTICAS DE VECTOR DE ATAQUE SON LAS SIGUIENTES: \n")
print("\n")
print(" - EN UN TOTAL DE "+str(attack_vector_cvssv3_network_sh)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES NETWORK. "+str(attack_vector_cvssv3_network3_1_sh)+" CON LA VERSIÓN CVSS 3.1 Y "+str(attack_vector_cvssv3_network3_0_sh)+" CON LA VERSIÓN CVSS 3.0 \n")
print(" - EN UN TOTAL DE "+str(attack_vector_cvssv3_local_sh)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES LOCAL. "+str(attack_vector_cvssv3_local3_1_sh)+" CON LA VERSIÓN CVSS 3.1 Y "+str(attack_vector_cvssv3_local3_0_sh)+" CON LA VERSIÓN CVSS 3.0 \n")
print(" - EN UN TOTAL DE "+str(attack_vector_cvssv3_physical_sh)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES FÍSICO. "+str(attack_vector_cvssv3_physical3_1_sh)+" CON LA VERSIÓN CVSS 3.1 Y "+str(attack_vector_cvssv3_physical3_0_sh)+" CON LA VERSIÓN CVSS 3.0 \n")
print(" - EN UN TOTAL DE "+str(attack_vector_cvssv3_adjacent_sh)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES ADYACENTE. "+str(attack_vector_cvssv3_adjacent3_1_sh)+" CON LA VERSIÓN CVSS 3.1 Y "+str(attack_vector_cvssv3_adjacent3_0_sh)+" CON LA VERSIÓN CVSS 3.0 \n")
print("\n")

print("***********************************************************************************************************************************")
print(" - UN TOTAL DE "+str(attack_vector_cvssv3_1_sh)+" VECTORES CVSSV3 TIENEN LA VERSION CVSS 3.1. DE ESTOS VECTORES, LAS ESTADÍSTICAS DE VECTOR DE ATAQUE SON LAS SIGUIENTES :\n")
print("\n")
print("       -    EN UN TOTAL DE "+str(attack_vector_cvssv3_network3_1_sh)+" VULNERABILIDADES CUYA VERSIÓN DE VECTOR DE ATAQUE ES 3.1, EL VECTOR DE ATAQUE ES NETWORK. DE ESTAS VULNERABILIDADES, LAS ESTADÍSTICAS DE COMPLEJIDAD DE ATAQUE SON LAS SIGUIENTES \n")
print("                   -    EN UN TOTAL DE "+str(attack_vector_cvssv3_network_high3_1_sh)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
print("                   -    EN UN TOTAL DE "+str(attack_vector_cvssv3_network_low3_1_sh)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
print("                   -    EN UN TOTAL DE "+str(attack_vector_cvssv3_network_medium3_1_sh)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA \n")

print("\n")
print("       -    EN UN TOTAL DE "+str(attack_vector_cvssv3_local3_1_sh)+" VULNERABILIDADES CUYA VERSIÓN DE VECTOR DE ATAQUE ES 3.1, EL VECTOR DE ATAQUE ES LOCAL. DE ESTAS VULNERABILIDADES, LAS ESTADÍSTICAS DE COMPLEJIDAD DE ATAQUE SON LAS SIGUIENTES \n")
print("                   -    EN UN TOTAL DE "+str(attack_vector_cvssv3_local_high3_1_sh)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
print("                   -    EN UN TOTAL DE "+str(attack_vector_cvssv3_local_low3_1_sh)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
print("                   -    EN UN TOTAL DE "+str(attack_vector_cvssv3_local_medium3_1_sh)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA \n")


print("\n")
print("       -    EN UN TOTAL DE "+str(attack_vector_cvssv3_physical3_1_sh)+" VULNERABILIDADES CUYA VERSIÓN DE VECTOR DE ATAQUE ES 3.1, EL VECTOR DE ATAQUE ES FÍSICO. DE ESTAS VULNERABILIDADES, LAS ESTADÍSTICAS DE COMPLEJIDAD DE ATAQUE SON LAS SIGUIENTES \n")
print("                   -    EN UN TOTAL DE "+str(attack_vector_cvssv3_physical_high3_1_sh)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
print("                   -    EN UN TOTAL DE "+str(attack_vector_cvssv3_physical_low3_1_sh)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
print("                   -    EN UN TOTAL DE "+str(attack_vector_cvssv3_physical_medium3_1_sh)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA \n")


print("\n")
print("       -    EN UN TOTAL DE "+str(attack_vector_cvssv3_adjacent3_1_sh)+" VULNERABILIDADES CUYA VERSIÓN DE VECTOR DE ATAQUE ES 3.1, EL VECTOR DE ATAQUE ES ADYACENTE. DE ESTAS VULNERABILIDADES, LAS ESTADÍSTICAS DE COMPLEJIDAD DE ATAQUE SON LAS SIGUIENTES \n")
print("                   -    EN UN TOTAL DE "+str(attack_vector_cvssv3_adjacent_high3_1_sh)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
print("                   -    EN UN TOTAL DE "+str(attack_vector_cvssv3_adjacent_low3_1_sh)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
print("                   -    EN UN TOTAL DE "+str(attack_vector_cvssv3_adjacent_medium3_1_sh)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA \n")


print("***********************************************************************************************************************************")
print(" - UN TOTAL DE "+str(attack_vector_cvssv3_0_sh)+" VECTORES CVSSV3 TIENEN LA VERSION CVSS 3.0. DE ESTOS VECTORES, LAS ESTADÍSTICAS DE VECTOR DE ATAQUE SON LAS SIGUIENTES :\n")
print("\n")
print("       -    EN UN TOTAL DE "+str(attack_vector_cvssv3_network3_0_sh)+" VULNERABILIDADES CUYA VERSIÓN DE VECTOR DE ATAQUE ES 3.0, EL VECTOR DE ATAQUE ES NETWORK. DE ESTAS VULNERABILIDADES, LAS ESTADÍSTICAS DE COMPLEJIDAD DE ATAQUE SON LAS SIGUIENTES \n")
print("                   -    EN UN TOTAL DE "+str(attack_vector_cvssv3_network_high3_0_sh)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
print("                   -    EN UN TOTAL DE "+str(attack_vector_cvssv3_network_low3_0_sh)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
print("                   -    EN UN TOTAL DE "+str(attack_vector_cvssv3_network_medium3_0_sh)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA \n")

print("\n")
print("       -    EN UN TOTAL DE "+str(attack_vector_cvssv3_local3_0_sh)+" VULNERABILIDADES CUYA VERSIÓN DE VECTOR DE ATAQUE ES 3.0, EL VECTOR DE ATAQUE ES LOCAL. DE ESTAS VULNERABILIDADES, LAS ESTADÍSTICAS DE COMPLEJIDAD DE ATAQUE SON LAS SIGUIENTES \n")
print("                   -    EN UN TOTAL DE "+str(attack_vector_cvssv3_local_high3_0_sh)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
print("                   -    EN UN TOTAL DE "+str(attack_vector_cvssv3_local_low3_0_sh)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
print("                   -    EN UN TOTAL DE "+str(attack_vector_cvssv3_local_medium3_0_sh)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA \n")


print("\n")
print("       -    EN UN TOTAL DE "+str(attack_vector_cvssv3_physical3_0_sh)+" VULNERABILIDADES CUYA VERSIÓN DE VECTOR DE ATAQUE ES 3.0, EL VECTOR DE ATAQUE ES FÍSICO. DE ESTAS VULNERABILIDADES, LAS ESTADÍSTICAS DE COMPLEJIDAD DE ATAQUE SON LAS SIGUIENTES \n")
print("                   -    EN UN TOTAL DE "+str(attack_vector_cvssv3_physical_high3_0_sh)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
print("                   -    EN UN TOTAL DE "+str(attack_vector_cvssv3_physical_low3_0_sh)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
print("                   -    EN UN TOTAL DE "+str(attack_vector_cvssv3_physical_medium3_0_sh)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA \n")


print("\n")
print("       -    EN UN TOTAL DE "+str(attack_vector_cvssv3_adjacent3_0_sh)+" VULNERABILIDADES CUYA VERSIÓN DE VECTOR DE ATAQUE ES 3.0, EL VECTOR DE ATAQUE ES ADYACENTE. DE ESTAS VULNERABILIDADES, LAS ESTADÍSTICAS DE COMPLEJIDAD DE ATAQUE SON LAS SIGUIENTES \n")
print("                   -    EN UN TOTAL DE "+str(attack_vector_cvssv3_adjacent_high3_0_sh)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
print("                   -    EN UN TOTAL DE "+str(attack_vector_cvssv3_adjacent_low3_0_sh)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
print("                   -    EN UN TOTAL DE "+str(attack_vector_cvssv3_adjacent_medium3_0_sh)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA \n")
print("\n")










print("**************************PORCENTAJES VERSION VECTOR CVSSV3/VECTOR DE ATAQUE/COMPLEJIDAD DE ATAQUE CVSSV3 CVE SMART HOME********************************")
print("\n")
print(" DE UN TOTAL DE "+str(attack_vector_cvssv3_sh)+" VECTORES DE ATAQUE, LAS ESTADÍSTICAS DE PORCENTAJES DE VECTOR DE ATAQUE SON LAS SIGUIENTES: \n")
print("\n")
print(" - EN EL "+str(float(((attack_vector_cvssv3_network_sh*100)/(attack_vector_cvssv3_sh))))+" % DE VULNERABILIDADES EL VECTOR DE ATAQUE ES NETWORK.  EL "+str(float(((attack_vector_cvssv3_network3_1_sh*100)/(attack_vector_cvssv3_network_sh))))+" % DE ELLOS CON LA VERSIÓN CVSS 3.1 Y EL "+str(float(((attack_vector_cvssv3_network3_0_sh*100)/(attack_vector_cvssv3_network_sh))))+" % CON LA VERSIÓN CVSS 3.0 \n")
print(" - EN EL "+str(float(((attack_vector_cvssv3_local_sh*100)/(attack_vector_cvssv3_sh))))+" % DE VULNERABILIDADES EL VECTOR DE ATAQUE ES LOCAL. EL "+str(float(((attack_vector_cvssv3_local3_1_sh*100)/(attack_vector_cvssv3_local_sh))))+" % DE ELLOS CON LA VERSIÓN CVSS 3.1 Y EL "+str(float(((attack_vector_cvssv3_local3_0_sh*100)/(attack_vector_cvssv3_local_sh))))+" % CON LA VERSIÓN CVSS 3.0 \n")
print(" - EN EL "+str(float(((attack_vector_cvssv3_physical_sh*100)/(attack_vector_cvssv3_sh))))+" % DE VULNERABILIDADES EL VECTOR DE ATAQUE ES FÍSICO. EL "+str(float(((attack_vector_cvssv3_physical3_1_sh*100)/(attack_vector_cvssv3_physical_sh))))+" % DE ELLOS CON LA VERSIÓN CVSS 3.1 Y EL "+str(float(((attack_vector_cvssv3_physical3_0_sh*100)/(attack_vector_cvssv3_physical_sh))))+" % CON LA VERSIÓN CVSS 3.0 \n")
print(" - EN EL "+str(float(((attack_vector_cvssv3_adjacent_sh*100)/(attack_vector_cvssv3_sh))))+" % DE VULNERABILIDADES EL VECTOR DE ATAQUE ES ADYACENTE. EL "+str(float(((attack_vector_cvssv3_adjacent3_1_sh*100)/(attack_vector_cvssv3_adjacent_sh))))+" % DE ELLOS CON LA VERSIÓN CVSS 3.1 Y EL "+str(float(((attack_vector_cvssv3_adjacent3_0_sh*100)/(attack_vector_cvssv3_adjacent_sh))))+" % CON LA VERSIÓN CVSS 3.0 \n")
print("\n")
print("***********************************************************************************************************************************")
print(" - EL "+str(float(((attack_vector_cvssv3_1_sh*100)/(attack_vector_cvssv3_sh))))+" % DEL TOTAL DE VECTORES CVSSV3 TIENEN LA VERSION CVSS 3.1. DE ESTOS VECTORES, LAS ESTADÍSTICAS DE PORCENTAJE DE VECTOR DE ATAQUE SON LAS SIGUIENTES :\n")
print("\n")
print("       -    EN EL "+str(float(((attack_vector_cvssv3_network3_1_sh*100)/(attack_vector_cvssv3_1_sh))))+" % VULNERABILIDADES CUYA VERSIÓN DE VECTOR DE ATAQUE ES 3.1, EL VECTOR DE ATAQUE ES NETWORK. DE ESTAS VULNERABILIDADES, LAS ESTADÍSTICAS DE PORCENTAJES DE COMPLEJIDAD DE ATAQUE SON LAS SIGUIENTES :\n")
print("                   -    EN EL "+str(float(((attack_vector_cvssv3_network_high3_1_sh*100)/(attack_vector_cvssv3_network3_1_sh))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
print("                   -    EN EL "+str(float(((attack_vector_cvssv3_network_low3_1_sh*100)/(attack_vector_cvssv3_network3_1_sh))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
print("                   -    EN EL "+str(float(((attack_vector_cvssv3_network_medium3_1_sh*100)/(attack_vector_cvssv3_network3_1_sh))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA \n")

print("\n")
print("       -    EN EL "+str(float(((attack_vector_cvssv3_local3_1_sh*100)/(attack_vector_cvssv3_1_sh))))+" % VULNERABILIDADES CUYA VERSIÓN DE VECTOR DE ATAQUE ES 3.1, EL VECTOR DE ATAQUE ES LOCAL. DE ESTAS VULNERABILIDADES, LAS ESTADÍSTICAS DE PORCENTAJES DE COMPLEJIDAD DE ATAQUE SON LAS SIGUIENTES :\n")
print("                   -    EN EL "+str(float(((attack_vector_cvssv3_local_high3_1_sh*100)/(attack_vector_cvssv3_local3_1_sh))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
print("                   -    EN EL "+str(float(((attack_vector_cvssv3_local_low3_1_sh*100)/(attack_vector_cvssv3_local3_1_sh))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
print("                   -    EN EL "+str(float(((attack_vector_cvssv3_local_medium3_1_sh*100)/(attack_vector_cvssv3_local3_1_sh))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA \n")


print("       -    EN EL "+str(float(((attack_vector_cvssv3_physical3_1_sh*100)/(attack_vector_cvssv3_1_sh))))+" % VULNERABILIDADES CUYA VERSIÓN DE VECTOR DE ATAQUE ES 3.1, EL VECTOR DE ATAQUE ES FÍSICO. DE ESTAS VULNERABILIDADES, LAS ESTADÍSTICAS DE PORCENTAJES DE COMPLEJIDAD DE ATAQUE SON LAS SIGUIENTES :\n")
print("                   -    EN EL "+str(float(((attack_vector_cvssv3_physical_high3_1_sh*100)/(attack_vector_cvssv3_physical3_1_sh))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
print("                   -    EN EL "+str(float(((attack_vector_cvssv3_physical_low3_1_sh*100)/(attack_vector_cvssv3_physical3_1_sh))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
print("                   -    EN EL "+str(float(((attack_vector_cvssv3_physical_medium3_1_sh*100)/(attack_vector_cvssv3_physical3_1_sh))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA \n")


print("       -    EN EL "+str(float(((attack_vector_cvssv3_adjacent3_1_sh*100)/(attack_vector_cvssv3_1_sh))))+" % VULNERABILIDADES CUYA VERSIÓN DE VECTOR DE ATAQUE ES 3.1, EL VECTOR DE ATAQUE ES ADYACENTE. DE ESTAS VULNERABILIDADES, LAS ESTADÍSTICAS DE PORCENTAJES DE COMPLEJIDAD DE ATAQUE SON LAS SIGUIENTES :\n")
print("                   -    EN EL "+str(float(((attack_vector_cvssv3_adjacent_high3_1_sh*100)/(attack_vector_cvssv3_adjacent3_1_sh))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
print("                   -    EN EL "+str(float(((attack_vector_cvssv3_adjacent_low3_1_sh*100)/(attack_vector_cvssv3_adjacent3_1_sh))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
print("                   -    EN EL "+str(float(((attack_vector_cvssv3_adjacent_medium3_1_sh*100)/(attack_vector_cvssv3_adjacent3_1_sh))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA \n")



print("***********************************************************************************************************************************")
print(" - EL "+str(float(((attack_vector_cvssv3_0_sh*100)/(attack_vector_cvssv3_sh))))+" % DEL TOTAL DE VECTORES CVSSV3 TIENEN LA VERSION CVSS 3.0. DE ESTOS VECTORES, LAS ESTADÍSTICAS DE PORCENTAJE DE VECTOR DE ATAQUE SON LAS SIGUIENTES :\n")
print("\n")
print("       -    EN EL "+str(float(((attack_vector_cvssv3_network3_0_sh*100)/(attack_vector_cvssv3_0_sh))))+" % VULNERABILIDADES CUYA VERSIÓN DE VECTOR DE ATAQUE ES 3.0, EL VECTOR DE ATAQUE ES NETWORK. DE ESTAS VULNERABILIDADES, LAS ESTADÍSTICAS DE PORCENTAJES DE COMPLEJIDAD DE ATAQUE SON LAS SIGUIENTES :\n")
print("                   -    EN EL "+str(float(((attack_vector_cvssv3_network_high3_0_sh*100)/(attack_vector_cvssv3_network3_0_sh))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
print("                   -    EN EL "+str(float(((attack_vector_cvssv3_network_low3_0_sh*100)/(attack_vector_cvssv3_network3_0_sh))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
print("                   -    EN EL "+str(float(((attack_vector_cvssv3_network_medium3_0_sh*100)/(attack_vector_cvssv3_network3_0_sh))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA \n")

print("\n")
print("       -    EN EL "+str(float(((attack_vector_cvssv3_local3_0_sh*100)/(attack_vector_cvssv3_0_sh))))+" % VULNERABILIDADES CUYA VERSIÓN DE VECTOR DE ATAQUE ES 3.0, EL VECTOR DE ATAQUE ES LOCAL. DE ESTAS VULNERABILIDADES, LAS ESTADÍSTICAS DE PORCENTAJES DE COMPLEJIDAD DE ATAQUE SON LAS SIGUIENTES :\n")
print("                   -    EN EL "+str(float(((attack_vector_cvssv3_local_high3_0_sh*100)/(attack_vector_cvssv3_local3_0_sh))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
print("                   -    EN EL "+str(float(((attack_vector_cvssv3_local_low3_0_sh*100)/(attack_vector_cvssv3_local3_0_sh))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
print("                   -    EN EL "+str(float(((attack_vector_cvssv3_local_medium3_0_sh*100)/(attack_vector_cvssv3_local3_0_sh))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA \n")

if(attack_vector_cvssv3_physical3_0_sh>0):
    print("       -    EN EL "+str(float(((attack_vector_cvssv3_physical3_0_sh*100)/(attack_vector_cvssv3_0_sh))))+" % VULNERABILIDADES CUYA VERSIÓN DE VECTOR DE ATAQUE ES 3.0, EL VECTOR DE ATAQUE ES FÍSICO. DE ESTAS VULNERABILIDADES, LAS ESTADÍSTICAS DE PORCENTAJES DE COMPLEJIDAD DE ATAQUE SON LAS SIGUIENTES :\n")
    print("                   -    EN EL "+str(float(((attack_vector_cvssv3_physical_high3_0_sh*100)/(attack_vector_cvssv3_physical3_0_sh))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
    print("                   -    EN EL "+str(float(((attack_vector_cvssv3_physical_low3_0_sh*100)/(attack_vector_cvssv3_physical3_0_sh))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
    print("                   -    EN EL "+str(float(((attack_vector_cvssv3_physical_medium3_0_sh*100)/(attack_vector_cvssv3_physical3_0_sh))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA \n")


print("       -    EN EL "+str(float(((attack_vector_cvssv3_adjacent3_0_sh*100)/(attack_vector_cvssv3_0_sh))))+" % VULNERABILIDADES CUYA VERSIÓN DE VECTOR DE ATAQUE ES 3.0, EL VECTOR DE ATAQUE ES ADYACENTE. DE ESTAS VULNERABILIDADES, LAS ESTADÍSTICAS DE PORCENTAJES DE COMPLEJIDAD DE ATAQUE SON LAS SIGUIENTES :\n")
print("                   -    EN EL "+str(float(((attack_vector_cvssv3_adjacent_high3_0_sh*100)/(attack_vector_cvssv3_adjacent3_0_sh))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
print("                   -    EN EL "+str(float(((attack_vector_cvssv3_adjacent_low3_0_sh*100)/(attack_vector_cvssv3_adjacent3_0_sh))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
print("                   -    EN EL "+str(float(((attack_vector_cvssv3_adjacent_medium3_0_sh*100)/(attack_vector_cvssv3_adjacent3_0_sh))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA \n")





print("\n")





































print("************************** ESTADÍSTICAS VERSION VECTOR CVSSV3/VECTOR DE ATAQUE/COMPLEJIDAD DE ATAQUE CVSSV3 CVE PARTE IOT Y SMART HOME CONJUNTAS********************************")
print("\n")
print(" DE UN TOTAL DE "+str(attack_vector_cvssv3_sh+attack_vector_cvssv3_iot)+" VECTORES DE ATAQUE, LAS ESTADÍSTICAS DE VECTOR DE ATAQUE SON LAS SIGUIENTES: \n")
print("\n")
print(" - EN UN TOTAL DE "+str(attack_vector_cvssv3_network_sh+attack_vector_cvssv3_network_iot)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES NETWORK. "+str(attack_vector_cvssv3_network3_1_sh+attack_vector_cvssv3_network3_1_iot)+" CON LA VERSIÓN CVSS 3.1 Y "+str(attack_vector_cvssv3_network3_0_sh+attack_vector_cvssv3_network3_0_iot)+" CON LA VERSIÓN CVSS 3.0 \n")
print(" - EN UN TOTAL DE "+str(attack_vector_cvssv3_local_sh+attack_vector_cvssv3_local_iot)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES LOCAL. "+str(attack_vector_cvssv3_local3_1_sh+attack_vector_cvssv3_local3_1_iot)+" CON LA VERSIÓN CVSS 3.1 Y "+str(attack_vector_cvssv3_local3_0_sh+attack_vector_cvssv3_local3_0_iot)+" CON LA VERSIÓN CVSS 3.0 \n")
print(" - EN UN TOTAL DE "+str(attack_vector_cvssv3_physical_sh+attack_vector_cvssv3_physical_iot)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES FÍSICO. "+str(attack_vector_cvssv3_physical3_1_sh+attack_vector_cvssv3_physical3_1_iot)+" CON LA VERSIÓN CVSS 3.1 Y "+str(attack_vector_cvssv3_physical3_0_sh+attack_vector_cvssv3_physical3_0_iot)+" CON LA VERSIÓN CVSS 3.0 \n")
print(" - EN UN TOTAL DE "+str(attack_vector_cvssv3_adjacent_sh+attack_vector_cvssv3_adjacent_iot)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES ADYACENTE. "+str(attack_vector_cvssv3_adjacent3_1_sh+attack_vector_cvssv3_adjacent3_1_iot)+" CON LA VERSIÓN CVSS 3.1 Y "+str(attack_vector_cvssv3_adjacent3_0_sh+attack_vector_cvssv3_adjacent3_0_iot)+" CON LA VERSIÓN CVSS 3.0 \n")
print("\n")

print("***********************************************************************************************************************************")
print(" - UN TOTAL DE "+str(attack_vector_cvssv3_1_sh+attack_vector_cvssv3_1_iot)+" VECTORES CVSSV3 TIENEN LA VERSION CVSS 3.1. DE ESTOS VECTORES, LAS ESTADÍSTICAS DE VECTOR DE ATAQUE SON LAS SIGUIENTES :\n")
print("\n")
print("       -    EN UN TOTAL DE "+str(attack_vector_cvssv3_network3_1_sh+attack_vector_cvssv3_network3_1_iot)+" VULNERABILIDADES CUYA VERSIÓN DE VECTOR DE ATAQUE ES 3.1, EL VECTOR DE ATAQUE ES NETWORK. DE ESTAS VULNERABILIDADES, LAS ESTADÍSTICAS DE COMPLEJIDAD DE ATAQUE SON LAS SIGUIENTES \n")
print("                   -    EN UN TOTAL DE "+str(attack_vector_cvssv3_network_high3_1_sh+attack_vector_cvssv3_network_high3_1_iot)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
print("                   -    EN UN TOTAL DE "+str(attack_vector_cvssv3_network_low3_1_sh+attack_vector_cvssv3_network_low3_1_iot)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
print("                   -    EN UN TOTAL DE "+str(attack_vector_cvssv3_network_medium3_1_sh+attack_vector_cvssv3_network_medium3_1_iot)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA \n")

print("\n")
print("       -    EN UN TOTAL DE "+str(attack_vector_cvssv3_local3_1_sh+attack_vector_cvssv3_local3_1_iot)+" VULNERABILIDADES CUYA VERSIÓN DE VECTOR DE ATAQUE ES 3.1, EL VECTOR DE ATAQUE ES LOCAL. DE ESTAS VULNERABILIDADES, LAS ESTADÍSTICAS DE COMPLEJIDAD DE ATAQUE SON LAS SIGUIENTES \n")
print("                   -    EN UN TOTAL DE "+str(attack_vector_cvssv3_local_high3_1_sh+attack_vector_cvssv3_local_high3_1_iot)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
print("                   -    EN UN TOTAL DE "+str(attack_vector_cvssv3_local_low3_1_sh+attack_vector_cvssv3_local_low3_1_iot)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
print("                   -    EN UN TOTAL DE "+str(attack_vector_cvssv3_local_medium3_1_sh+attack_vector_cvssv3_local_medium3_1_iot)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA \n")


print("\n")
print("       -    EN UN TOTAL DE "+str(attack_vector_cvssv3_physical3_1_sh+attack_vector_cvssv3_physical3_1_iot)+" VULNERABILIDADES CUYA VERSIÓN DE VECTOR DE ATAQUE ES 3.1, EL VECTOR DE ATAQUE ES FÍSICO. DE ESTAS VULNERABILIDADES, LAS ESTADÍSTICAS DE COMPLEJIDAD DE ATAQUE SON LAS SIGUIENTES \n")
print("                   -    EN UN TOTAL DE "+str(attack_vector_cvssv3_physical_high3_1_sh+attack_vector_cvssv3_physical_high3_1_iot)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
print("                   -    EN UN TOTAL DE "+str(attack_vector_cvssv3_physical_low3_1_sh+attack_vector_cvssv3_physical_low3_1_iot)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
print("                   -    EN UN TOTAL DE "+str(attack_vector_cvssv3_physical_medium3_1_sh+attack_vector_cvssv3_physical_medium3_1_iot)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA \n")


print("\n")
print("       -    EN UN TOTAL DE "+str(attack_vector_cvssv3_adjacent3_1_sh+attack_vector_cvssv3_adjacent3_1_iot)+" VULNERABILIDADES CUYA VERSIÓN DE VECTOR DE ATAQUE ES 3.1, EL VECTOR DE ATAQUE ES ADYACENTE. DE ESTAS VULNERABILIDADES, LAS ESTADÍSTICAS DE COMPLEJIDAD DE ATAQUE SON LAS SIGUIENTES \n")
print("                   -    EN UN TOTAL DE "+str(attack_vector_cvssv3_adjacent_high3_1_sh+attack_vector_cvssv3_adjacent_high3_1_iot)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
print("                   -    EN UN TOTAL DE "+str(attack_vector_cvssv3_adjacent_low3_1_sh+attack_vector_cvssv3_adjacent_low3_1_iot)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
print("                   -    EN UN TOTAL DE "+str(attack_vector_cvssv3_adjacent_medium3_1_sh+attack_vector_cvssv3_adjacent_medium3_1_iot)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA \n")


print("***********************************************************************************************************************************")
print(" - UN TOTAL DE "+str(attack_vector_cvssv3_0_sh+attack_vector_cvssv3_0_iot)+" VECTORES CVSSV3 TIENEN LA VERSION CVSS 3.0. DE ESTOS VECTORES, LAS ESTADÍSTICAS DE VECTOR DE ATAQUE SON LAS SIGUIENTES :\n")
print("\n")
print("       -    EN UN TOTAL DE "+str(attack_vector_cvssv3_network3_0_sh+attack_vector_cvssv3_network3_0_iot)+" VULNERABILIDADES CUYA VERSIÓN DE VECTOR DE ATAQUE ES 3.0, EL VECTOR DE ATAQUE ES NETWORK. DE ESTAS VULNERABILIDADES, LAS ESTADÍSTICAS DE COMPLEJIDAD DE ATAQUE SON LAS SIGUIENTES \n")
print("                   -    EN UN TOTAL DE "+str(attack_vector_cvssv3_network_high3_0_sh+attack_vector_cvssv3_network_high3_0_iot)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
print("                   -    EN UN TOTAL DE "+str(attack_vector_cvssv3_network_low3_0_sh+attack_vector_cvssv3_network_low3_0_iot)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
print("                   -    EN UN TOTAL DE "+str(attack_vector_cvssv3_network_medium3_0_sh+attack_vector_cvssv3_network_medium3_0_iot)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA \n")

print("\n")
print("       -    EN UN TOTAL DE "+str(attack_vector_cvssv3_local3_0_sh+attack_vector_cvssv3_local3_0_iot)+" VULNERABILIDADES CUYA VERSIÓN DE VECTOR DE ATAQUE ES 3.0, EL VECTOR DE ATAQUE ES LOCAL. DE ESTAS VULNERABILIDADES, LAS ESTADÍSTICAS DE COMPLEJIDAD DE ATAQUE SON LAS SIGUIENTES \n")
print("                   -    EN UN TOTAL DE "+str(attack_vector_cvssv3_local_high3_0_sh+attack_vector_cvssv3_local_high3_0_iot)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
print("                   -    EN UN TOTAL DE "+str(attack_vector_cvssv3_local_low3_0_sh+attack_vector_cvssv3_local_low3_0_iot)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
print("                   -    EN UN TOTAL DE "+str(attack_vector_cvssv3_local_medium3_0_sh+attack_vector_cvssv3_local_medium3_0_iot)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA \n")


print("\n")
print("       -    EN UN TOTAL DE "+str(attack_vector_cvssv3_physical3_0_sh+attack_vector_cvssv3_physical3_0_iot)+" VULNERABILIDADES CUYA VERSIÓN DE VECTOR DE ATAQUE ES 3.0, EL VECTOR DE ATAQUE ES FÍSICO. DE ESTAS VULNERABILIDADES, LAS ESTADÍSTICAS DE COMPLEJIDAD DE ATAQUE SON LAS SIGUIENTES \n")
print("                   -    EN UN TOTAL DE "+str(attack_vector_cvssv3_physical_high3_0_sh+attack_vector_cvssv3_physical_high3_0_iot)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
print("                   -    EN UN TOTAL DE "+str(attack_vector_cvssv3_physical_low3_0_sh+attack_vector_cvssv3_physical_low3_0_iot)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
print("                   -    EN UN TOTAL DE "+str(attack_vector_cvssv3_physical_medium3_0_sh+attack_vector_cvssv3_physical_medium3_0_iot)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA \n")


print("\n")
print("       -    EN UN TOTAL DE "+str(attack_vector_cvssv3_adjacent3_0_sh+attack_vector_cvssv3_adjacent3_0_iot)+" VULNERABILIDADES CUYA VERSIÓN DE VECTOR DE ATAQUE ES 3.0, EL VECTOR DE ATAQUE ES ADYACENTE. DE ESTAS VULNERABILIDADES, LAS ESTADÍSTICAS DE COMPLEJIDAD DE ATAQUE SON LAS SIGUIENTES \n")
print("                   -    EN UN TOTAL DE "+str(attack_vector_cvssv3_adjacent_high3_0_sh+attack_vector_cvssv3_adjacent_high3_0_iot)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
print("                   -    EN UN TOTAL DE "+str(attack_vector_cvssv3_adjacent_low3_0_sh+attack_vector_cvssv3_adjacent_low3_0_iot)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
print("                   -    EN UN TOTAL DE "+str(attack_vector_cvssv3_adjacent_medium3_0_sh+attack_vector_cvssv3_adjacent_medium3_0_iot)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA \n")
print("\n")




















print("**************************PORCENTAJES VERSION VECTOR CVSSV3/VECTOR DE ATAQUE/COMPLEJIDAD DE ATAQUE CVSSV3 CVE PARTE IOT Y SMART HOME CONJUNTAS********************************")
print("\n")
print(" DE UN TOTAL DE "+str(attack_vector_cvssv3_sh+attack_vector_cvssv3_iot)+" VECTORES DE ATAQUE, LAS ESTADÍSTICAS DE PORCENTAJES DE VECTOR DE ATAQUE SON LAS SIGUIENTES: \n")
print("\n")
print(" - EN EL "+str(float((((attack_vector_cvssv3_network_sh+attack_vector_cvssv3_network_iot)*100)/(attack_vector_cvssv3_sh+attack_vector_cvssv3_iot))))+" % DE VULNERABILIDADES EL VECTOR DE ATAQUE ES NETWORK.  EL "+str(float((((attack_vector_cvssv3_network3_1_sh+attack_vector_cvssv3_network3_1_iot)*100)/(attack_vector_cvssv3_network_sh+attack_vector_cvssv3_network_iot))))+" % DE ELLOS CON LA VERSIÓN CVSS 3.1 Y EL "+str(float((((attack_vector_cvssv3_network3_0_sh+attack_vector_cvssv3_network3_0_iot)*100)/(attack_vector_cvssv3_network_sh+attack_vector_cvssv3_network_iot))))+" % CON LA VERSIÓN CVSS 3.0 \n")
print(" - EN EL "+str(float((((attack_vector_cvssv3_local_sh+attack_vector_cvssv3_local_iot)*100)/(attack_vector_cvssv3_sh+attack_vector_cvssv3_iot))))+" % DE VULNERABILIDADES EL VECTOR DE ATAQUE ES LOCAL. EL "+str(float((((attack_vector_cvssv3_local3_1_sh+attack_vector_cvssv3_local3_1_iot)*100)/(attack_vector_cvssv3_local_sh+attack_vector_cvssv3_local_iot))))+" % DE ELLOS CON LA VERSIÓN CVSS 3.1 Y EL "+str(float((((attack_vector_cvssv3_local3_0_sh+attack_vector_cvssv3_local3_0_iot)*100)/(attack_vector_cvssv3_local_sh+attack_vector_cvssv3_local_iot))))+" % CON LA VERSIÓN CVSS 3.0 \n")
print(" - EN EL "+str(float((((attack_vector_cvssv3_physical_sh+attack_vector_cvssv3_physical_iot)*100)/(attack_vector_cvssv3_sh+attack_vector_cvssv3_iot))))+" % DE VULNERABILIDADES EL VECTOR DE ATAQUE ES FÍSICO. EL "+str(float((((attack_vector_cvssv3_physical3_1_sh+attack_vector_cvssv3_physical3_1_iot)*100)/(attack_vector_cvssv3_physical_sh+attack_vector_cvssv3_physical_iot))))+" % DE ELLOS CON LA VERSIÓN CVSS 3.1 Y EL "+str(float((((attack_vector_cvssv3_physical3_0_sh+attack_vector_cvssv3_physical3_0_iot)*100)/(attack_vector_cvssv3_physical_sh+attack_vector_cvssv3_physical_iot))))+" % CON LA VERSIÓN CVSS 3.0 \n")
print(" - EN EL "+str(float((((attack_vector_cvssv3_adjacent_sh+attack_vector_cvssv3_adjacent_iot)*100)/(attack_vector_cvssv3_sh+attack_vector_cvssv3_iot))))+" % DE VULNERABILIDADES EL VECTOR DE ATAQUE ES ADYACENTE. EL "+str(float((((attack_vector_cvssv3_adjacent3_1_sh+attack_vector_cvssv3_adjacent3_1_iot)*100)/(attack_vector_cvssv3_adjacent_sh+attack_vector_cvssv3_adjacent_iot))))+" % DE ELLOS CON LA VERSIÓN CVSS 3.1 Y EL "+str(float((((attack_vector_cvssv3_adjacent3_0_sh+attack_vector_cvssv3_adjacent3_0_iot)*100)/(attack_vector_cvssv3_adjacent_sh+attack_vector_cvssv3_adjacent_iot))))+" % CON LA VERSIÓN CVSS 3.0 \n")
print("\n")
print("***********************************************************************************************************************************")
print(" - EL "+str(float((((attack_vector_cvssv3_1_sh+attack_vector_cvssv3_1_iot)*100)/(attack_vector_cvssv3_sh+attack_vector_cvssv3_iot))))+" % DEL TOTAL DE VECTORES CVSSV3 TIENEN LA VERSION CVSS 3.1. DE ESTOS VECTORES, LAS ESTADÍSTICAS DE PORCENTAJE DE VECTOR DE ATAQUE SON LAS SIGUIENTES :\n")
print("\n")
print("       -    EN EL "+str(float((((attack_vector_cvssv3_network3_1_sh+attack_vector_cvssv3_network3_1_iot)*100)/(attack_vector_cvssv3_1_sh+attack_vector_cvssv3_1_iot))))+" % VULNERABILIDADES CUYA VERSIÓN DE VECTOR DE ATAQUE ES 3.1, EL VECTOR DE ATAQUE ES NETWORK. DE ESTAS VULNERABILIDADES, LAS ESTADÍSTICAS DE PORCENTAJES DE COMPLEJIDAD DE ATAQUE SON LAS SIGUIENTES :\n")
print("                   -    EN EL "+str(float((((attack_vector_cvssv3_network_high3_1_sh+attack_vector_cvssv3_network_high3_1_iot)*100)/(attack_vector_cvssv3_network3_1_sh+attack_vector_cvssv3_network3_1_iot))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
print("                   -    EN EL "+str(float((((attack_vector_cvssv3_network_low3_1_sh+attack_vector_cvssv3_network_low3_1_iot)*100)/(attack_vector_cvssv3_network3_1_sh+attack_vector_cvssv3_network3_1_iot))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
print("                   -    EN EL "+str(float((((attack_vector_cvssv3_network_medium3_1_sh+attack_vector_cvssv3_network_medium3_1_iot)*100)/(attack_vector_cvssv3_network3_1_sh+attack_vector_cvssv3_network3_1_iot))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA \n")

print("\n")
print("       -    EN EL "+str(float((((attack_vector_cvssv3_local3_1_sh+attack_vector_cvssv3_local3_1_iot)*100)/(attack_vector_cvssv3_1_sh+attack_vector_cvssv3_1_iot))))+" % VULNERABILIDADES CUYA VERSIÓN DE VECTOR DE ATAQUE ES 3.1, EL VECTOR DE ATAQUE ES LOCAL. DE ESTAS VULNERABILIDADES, LAS ESTADÍSTICAS DE PORCENTAJES DE COMPLEJIDAD DE ATAQUE SON LAS SIGUIENTES :\n")
print("                   -    EN EL "+str(float((((attack_vector_cvssv3_local_high3_1_sh+attack_vector_cvssv3_local_high3_1_iot)*100)/(attack_vector_cvssv3_local3_1_sh+attack_vector_cvssv3_local3_1_iot))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
print("                   -    EN EL "+str(float((((attack_vector_cvssv3_local_low3_1_sh+attack_vector_cvssv3_local_low3_1_iot)*100)/(attack_vector_cvssv3_local3_1_sh+attack_vector_cvssv3_local3_1_iot))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
print("                   -    EN EL "+str(float((((attack_vector_cvssv3_local_medium3_1_sh+attack_vector_cvssv3_local_medium3_1_iot)*100)/(attack_vector_cvssv3_local3_1_sh+attack_vector_cvssv3_local3_1_iot))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA \n")


print("\n")
print("       -    EN EL "+str(float((((attack_vector_cvssv3_physical3_1_sh+attack_vector_cvssv3_physical3_1_iot)*100)/(attack_vector_cvssv3_1_sh+attack_vector_cvssv3_1_iot))))+" % VULNERABILIDADES CUYA VERSIÓN DE VECTOR DE ATAQUE ES 3.1, EL VECTOR DE ATAQUE ES FÍSICO. DE ESTAS VULNERABILIDADES, LAS ESTADÍSTICAS DE PORCENTAJES DE COMPLEJIDAD DE ATAQUE SON LAS SIGUIENTES :\n")
print("                   -    EN EL "+str(float((((attack_vector_cvssv3_physical_high3_1_sh+attack_vector_cvssv3_physical_high3_1_iot)*100)/(attack_vector_cvssv3_physical3_1_sh+attack_vector_cvssv3_physical3_1_iot))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
print("                   -    EN EL "+str(float((((attack_vector_cvssv3_physical_low3_1_sh+attack_vector_cvssv3_physical_low3_1_iot)*100)/(attack_vector_cvssv3_physical3_1_sh+attack_vector_cvssv3_physical3_1_iot))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
print("                   -    EN EL "+str(float((((attack_vector_cvssv3_physical_medium3_1_sh+attack_vector_cvssv3_physical_medium3_1_iot)*100)/(attack_vector_cvssv3_physical3_1_sh+attack_vector_cvssv3_physical3_1_iot))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA \n")


print("\n")
print("       -    EN EL "+str(float((((attack_vector_cvssv3_adjacent3_1_sh+attack_vector_cvssv3_adjacent3_1_iot)*100)/(attack_vector_cvssv3_1_sh+attack_vector_cvssv3_1_iot))))+" % VULNERABILIDADES CUYA VERSIÓN DE VECTOR DE ATAQUE ES 3.1, EL VECTOR DE ATAQUE ES ADYACENTE. DE ESTAS VULNERABILIDADES, LAS ESTADÍSTICAS DE PORCENTAJES DE COMPLEJIDAD DE ATAQUE SON LAS SIGUIENTES :\n")
print("                   -    EN EL "+str(float((((attack_vector_cvssv3_adjacent_high3_1_sh+attack_vector_cvssv3_adjacent_high3_1_iot)*100)/(attack_vector_cvssv3_adjacent3_1_sh+attack_vector_cvssv3_adjacent3_1_iot))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
print("                   -    EN EL "+str(float((((attack_vector_cvssv3_adjacent_low3_1_sh+attack_vector_cvssv3_adjacent_low3_1_iot)*100)/(attack_vector_cvssv3_adjacent3_1_sh+attack_vector_cvssv3_adjacent3_1_iot))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
print("                   -    EN EL "+str(float((((attack_vector_cvssv3_adjacent_medium3_1_sh+attack_vector_cvssv3_adjacent_medium3_1_iot)*100)/(attack_vector_cvssv3_adjacent3_1_sh+attack_vector_cvssv3_adjacent3_1_iot))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA \n")

print("***********************************************************************************************************************************")
print(" - EL "+str(float((((attack_vector_cvssv3_0_sh+attack_vector_cvssv3_0_iot)*100)/(attack_vector_cvssv3_sh+attack_vector_cvssv3_iot))))+" % DEL TOTAL DE VECTORES CVSSV3 TIENEN LA VERSION CVSS 3.0. DE ESTOS VECTORES, LAS ESTADÍSTICAS DE PORCENTAJE DE VECTOR DE ATAQUE SON LAS SIGUIENTES :\n")
print("\n")
print("       -    EN EL "+str(float((((attack_vector_cvssv3_network3_0_sh+attack_vector_cvssv3_network3_0_iot)*100)/(attack_vector_cvssv3_0_sh+attack_vector_cvssv3_0_iot))))+" % VULNERABILIDADES CUYA VERSIÓN DE VECTOR DE ATAQUE ES 3.0, EL VECTOR DE ATAQUE ES NETWORK. DE ESTAS VULNERABILIDADES, LAS ESTADÍSTICAS DE PORCENTAJES DE COMPLEJIDAD DE ATAQUE SON LAS SIGUIENTES :\n")
print("                   -    EN EL "+str(float((((attack_vector_cvssv3_network_high3_0_sh+attack_vector_cvssv3_network_high3_0_iot)*100)/(attack_vector_cvssv3_network3_0_sh+attack_vector_cvssv3_network3_0_iot))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
print("                   -    EN EL "+str(float((((attack_vector_cvssv3_network_low3_0_sh+attack_vector_cvssv3_network_low3_0_iot)*100)/(attack_vector_cvssv3_network3_0_sh+attack_vector_cvssv3_network3_0_iot))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
print("                   -    EN EL "+str(float((((attack_vector_cvssv3_network_medium3_0_sh+attack_vector_cvssv3_network_medium3_0_iot)*100)/(attack_vector_cvssv3_network3_0_sh+attack_vector_cvssv3_network3_0_iot))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA \n")

print("\n")
print("       -    EN EL "+str(float((((attack_vector_cvssv3_local3_0_sh+attack_vector_cvssv3_local3_0_iot)*100)/(attack_vector_cvssv3_0_sh+attack_vector_cvssv3_0_iot))))+" % VULNERABILIDADES CUYA VERSIÓN DE VECTOR DE ATAQUE ES 3.0, EL VECTOR DE ATAQUE ES LOCAL. DE ESTAS VULNERABILIDADES, LAS ESTADÍSTICAS DE PORCENTAJES DE COMPLEJIDAD DE ATAQUE SON LAS SIGUIENTES :\n")
print("                   -    EN EL "+str(float((((attack_vector_cvssv3_local_high3_0_sh+attack_vector_cvssv3_local_high3_0_iot)*100)/(attack_vector_cvssv3_local3_0_sh+attack_vector_cvssv3_local3_0_iot))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
print("                   -    EN EL "+str(float((((attack_vector_cvssv3_local_low3_0_sh+attack_vector_cvssv3_local_low3_0_iot)*100)/(attack_vector_cvssv3_local3_0_sh+attack_vector_cvssv3_local3_0_iot))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
print("                   -    EN EL "+str(float((((attack_vector_cvssv3_local_medium3_0_sh+attack_vector_cvssv3_local_medium3_0_iot)*100)/(attack_vector_cvssv3_local3_0_sh+attack_vector_cvssv3_local3_0_iot))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA \n")

if((attack_vector_cvssv3_physical3_0_sh+attack_vector_cvssv3_physical3_0_iot)>0):
    
    print("       -    EN EL "+str(float((((attack_vector_cvssv3_physical3_0_sh+attack_vector_cvssv3_physical3_0_iot)*100)/(attack_vector_cvssv3_0_sh+attack_vector_cvssv3_0_iot))))+" % VULNERABILIDADES CUYA VERSIÓN DE VECTOR DE ATAQUE ES 3.0, EL VECTOR DE ATAQUE ES FÍSICO. DE ESTAS VULNERABILIDADES, LAS ESTADÍSTICAS DE PORCENTAJES DE COMPLEJIDAD DE ATAQUE SON LAS SIGUIENTES :\n")
    print("                   -    EN EL "+str(float((((attack_vector_cvssv3_physical_high3_0_sh+attack_vector_cvssv3_physical_high3_0_iot)*100)/(attack_vector_cvssv3_physical3_0_sh+attack_vector_cvssv3_physical3_0_iot))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
    print("                   -    EN EL "+str(float((((attack_vector_cvssv3_physical_low3_0_sh+attack_vector_cvssv3_physical_low3_0_iot)*100)/(attack_vector_cvssv3_physical3_0_sh+attack_vector_cvssv3_physical3_0_iot))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
    print("                   -    EN EL "+str(float((((attack_vector_cvssv3_physical_medium3_0_sh+attack_vector_cvssv3_physical_medium3_0_iot)*100)/(attack_vector_cvssv3_physical3_0_sh+attack_vector_cvssv3_physical3_0_iot))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA \n")


print("       -    EN EL "+str(float((((attack_vector_cvssv3_adjacent3_0_sh+attack_vector_cvssv3_adjacent3_0_iot)*100)/(attack_vector_cvssv3_0_sh+attack_vector_cvssv3_0_iot))))+" % VULNERABILIDADES CUYA VERSIÓN DE VECTOR DE ATAQUE ES 3.0, EL VECTOR DE ATAQUE ES ADYACENTE. DE ESTAS VULNERABILIDADES, LAS ESTADÍSTICAS DE PORCENTAJES DE COMPLEJIDAD DE ATAQUE SON LAS SIGUIENTES :\n")
print("                   -    EN EL "+str(float((((attack_vector_cvssv3_adjacent_high3_0_sh+attack_vector_cvssv3_adjacent_high3_0_iot)*100)/(attack_vector_cvssv3_adjacent3_0_sh+attack_vector_cvssv3_adjacent3_0_iot))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA \n")
print("                   -    EN EL "+str(float((((attack_vector_cvssv3_adjacent_low3_0_sh+attack_vector_cvssv3_adjacent_low3_0_iot)*100)/(attack_vector_cvssv3_adjacent3_0_sh+attack_vector_cvssv3_adjacent3_0_iot))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA \n")
print("                   -    EN EL "+str(float((((attack_vector_cvssv3_adjacent_medium3_0_sh+attack_vector_cvssv3_adjacent_medium3_0_iot)*100)/(attack_vector_cvssv3_adjacent3_0_sh+attack_vector_cvssv3_adjacent3_0_iot))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA \n")





print("\n")

















