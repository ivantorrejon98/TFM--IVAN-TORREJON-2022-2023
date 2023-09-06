

import pandas as pd

#Abro los ficheros con los que voy a tratar


df_cve_iot=pd.read_excel('cves_iot_2023.xlsx')
df_cve_sh=pd.read_excel('cves_smart_home_2023.xlsx')


#Variables para almacenar los distintos de contadores de vector de acceso y su complejidad de acceso para la parte IOT
access_vector_cvssv2_iot=0

#Variables donde aumento el contador segun la relacion entre el vector de acceso y su complejidad de acceso
#Por cada tipo de vector de acceso tengo una variable con su complejidad de acceso
access_vector_cvssv2_network_iot=0
access_vector_cvssv2_network_low_iot=0
access_vector_cvssv2_network_high_iot=0
access_vector_cvssv2_network_medium_iot=0


access_vector_cvssv2_adjacent_iot=0
access_vector_cvssv2_adjacent_low_iot=0
access_vector_cvssv2_adjacent_high_iot=0
access_vector_cvssv2_adjacent_medium_iot=0


access_vector_cvssv2_local_iot=0
access_vector_cvssv2_local_low_iot=0
access_vector_cvssv2_local_high_iot=0
access_vector_cvssv2_local_medium_iot=0


access_vector_cvssv2_physical_iot=0
access_vector_cvssv2_physical_low_iot=0
access_vector_cvssv2_physical_high_iot=0
access_vector_cvssv2_physical_medium_iot=0





#Recorro cada fila del fichero comprobando valores. Primeramente compruebo que el vector de ACCESO no sea nulo y aumento el contador

for j in range(0,len(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.accessVector"])):
    if(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.accessVector"][j]!='NONE'):
        access_vector_cvssv2_iot+=1
        #Compruebo el tipo de vector de ACCESO
        if(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.accessVector"][j]=='NETWORK'):
            access_vector_cvssv2_network_iot+=1
            #Compruebo la complejidad de ACCESO
            if(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.accessComplexity"][j]=='HIGH'):
                access_vector_cvssv2_network_high_iot+=1
            elif(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.accessComplexity"][j]=='LOW'):
                access_vector_cvssv2_network_low_iot+=1
            elif(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.accessComplexity"][j]=='MEDIUM'):
                access_vector_cvssv2_network_medium_iot+=1       
        elif(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.accessVector"][j]=='LOCAL'):
            access_vector_cvssv2_local_iot+=1
            if(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.accessComplexity"][j]=='HIGH'):
                access_vector_cvssv2_local_high_iot+=1
            elif(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.accessComplexity"][j]=='LOW'):
                access_vector_cvssv2_local_low_iot+=1
            elif(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.accessComplexity"][j]=='MEDIUM'):
                access_vector_cvssv2_local_medium_iot+=1

        elif(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.accessVector"][j]=='PHYSICAL'):
            access_vector_cvssv2_physical_iot+=1
            if(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.accessComplexity"][j]=='HIGH'):
                access_vector_cvssv2_physical_high_iot+=1
            elif(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.accessComplexity"][j]=='LOW'):
                access_vector_cvssv2_physical_low_iot+=1
            elif(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.accessComplexity"][j]=='MEDIUM'):
                access_vector_cvssv2_physical_medium_iot+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.accessVector"][j]=='ADJACENT_NETWORK'):
            access_vector_cvssv2_adjacent_iot+=1
            if(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.accessComplexity"][j]=='HIGH'):
                access_vector_cvssv2_adjacent_high_iot+=1
            elif(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.accessComplexity"][j]=='LOW'):
                access_vector_cvssv2_adjacent_low_iot+=1
            elif(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.accessComplexity"][j]=='MEDIUM'):
                access_vector_cvssv2_adjacent_medium_iot+=1
        
                        
                        
                        
                        
print("**************************ESTADÍSTICAS VECTOR DE ACCESO/COMPLEJIDAD DE ACCESO SEGÚN VECTOR CVSSV2 CVE IOT********************************")
print("\n")
print(" DE UN TOTAL DE "+str(access_vector_cvssv2_iot)+" VECTORES DE ACCESO, LAS ESTADÍSTICAS DE VECTOR DE ACCCESO SON LAS SIGUIENTES: \n")
print("\n")
print(" - EN UN TOTAL DE "+str(access_vector_cvssv2_network_iot)+" VULNERABILIDADES EL VECTOR DE ACCESO ES NETWORK. \n")
print(" - EN UN TOTAL DE "+str(access_vector_cvssv2_local_iot)+" VULNERABILIDADES EL VECTOR DE ACCESO ES LOCAL. \n")
print(" - EN UN TOTAL DE "+str(access_vector_cvssv2_physical_iot)+" VULNERABILIDADES EL VECTOR DE ACCESO ES FÍSICO. \n")
print(" - EN UN TOTAL DE "+str(access_vector_cvssv2_adjacent_iot)+" VULNERABILIDADES EL VECTOR DE ACCESO ES ADYACENTE. \n")

print("***********************************************************************************************************************************")
print("\n")
print("       -    EN UN TOTAL DE "+str(access_vector_cvssv2_network_iot)+" VULNERABILIDADES CUYO VECTOR DE ACCESO ES NETWORK, LAS ESTADÍSTICAS DE COMPLEJIDAD DE ACCESO SON LAS SIGUIENTES \n")
print("                   -    EN UN TOTAL DE "+str(access_vector_cvssv2_network_high_iot)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES ALTA \n")
print("                   -    EN UN TOTAL DE "+str(access_vector_cvssv2_network_low_iot)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES BAJA \n")
print("                   -    EN UN TOTAL DE "+str(access_vector_cvssv2_network_medium_iot)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES MEDIA \n")

print("\n")
print("       -    EN UN TOTAL DE "+str(access_vector_cvssv2_local_iot)+" VULNERABILIDADES CUYO VECTOR DE ACCESO ES LOCAL, LAS ESTADÍSTICAS DE COMPLEJIDAD DE ACCESO SON LAS SIGUIENTES \n")
print("                   -    EN UN TOTAL DE "+str(access_vector_cvssv2_local_high_iot)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES ALTA \n")
print("                   -    EN UN TOTAL DE "+str(access_vector_cvssv2_local_low_iot)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES BAJA \n")
print("                   -    EN UN TOTAL DE "+str(access_vector_cvssv2_local_medium_iot)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES MEDIA \n")


print("\n")
print("       -    EN UN TOTAL DE "+str(access_vector_cvssv2_physical_iot)+" VULNERABILIDADES CUYO VECTOR DE ACCESO ES FÍSICO, LAS ESTADÍSTICAS DE COMPLEJIDAD DE ACCESO SON LAS SIGUIENTES \n")
print("                   -    EN UN TOTAL DE "+str(access_vector_cvssv2_physical_high_iot)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES ALTA \n")
print("                   -    EN UN TOTAL DE "+str(access_vector_cvssv2_physical_low_iot)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES BAJA \n")
print("                   -    EN UN TOTAL DE "+str(access_vector_cvssv2_physical_medium_iot)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES MEDIA \n")


print("\n")
print("       -    EN UN TOTAL DE "+str(access_vector_cvssv2_adjacent_iot)+" VULNERABILIDADES CUYO VECTOR DE ACCESO ES ADYACENTE, LAS ESTADÍSTICAS DE COMPLEJIDAD DE ACCESO SON LAS SIGUIENTES \n")
print("                   -    EN UN TOTAL DE "+str(access_vector_cvssv2_adjacent_high_iot)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES ALTA \n")
print("                   -    EN UN TOTAL DE "+str(access_vector_cvssv2_adjacent_low_iot)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES BAJA \n")
print("                   -    EN UN TOTAL DE "+str(access_vector_cvssv2_adjacent_medium_iot)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES MEDIA \n")












print("**************************PORCENTAJES VECTOR DE ACCESO/COMPLEJIDAD DE ACCESO SEGÚN VECTOR CVSSV2 CVE IOT********************************")
print("\n")
print(" DE UN TOTAL DE "+str(access_vector_cvssv2_iot)+" VECTORES DE ACCESO, LAS ESTADÍSTICAS DE PORCENTAJES SON LAS SIGUIENTES: \n")
print("\n")
print(" - EN EL "+str(float(((access_vector_cvssv2_network_iot*100)/(access_vector_cvssv2_iot))))+" % DE VULNERABILIDADES EL VECTOR DE ACCESO ES NETWORK.   \n")
print(" - EN EL "+str(float(((access_vector_cvssv2_local_iot*100)/(access_vector_cvssv2_iot))))+" % DE VULNERABILIDADES EL VECTOR DE ACCESO ES LOCAL.  \n")
print(" - EN EL "+str(float(((access_vector_cvssv2_physical_iot*100)/(access_vector_cvssv2_iot))))+" % DE VULNERABILIDADES EL VECTOR DE ACCESO ES FÍSICO.  \n")
print(" - EN EL "+str(float(((access_vector_cvssv2_adjacent_iot*100)/(access_vector_cvssv2_iot))))+" % DE VULNERABILIDADES EL VECTOR DE ACCESO ES ADYACENTE.  \n")
print("\n")
print("***********************************************************************************************************************************")

print("\n")
print("       -    EN EL "+str(float(((access_vector_cvssv2_network_iot*100)/(access_vector_cvssv2_iot))))+" % DE VULNERABILIDADES CUYO VECTOR DE ACCESO ES NETWORK, LAS ESTADÍSTICAS DE PORCENTAJES DE COMPLEJIDAD DE ACCESO SON LAS SIGUIENTES :\n")
print("                   -    EN EL "+str(float(((access_vector_cvssv2_network_high_iot*100)/(access_vector_cvssv2_network_iot))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES ALTA \n")
print("                   -    EN EL "+str(float(((access_vector_cvssv2_network_low_iot*100)/(access_vector_cvssv2_network_iot))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES BAJA \n")
print("                   -    EN EL "+str(float(((access_vector_cvssv2_network_medium_iot*100)/(access_vector_cvssv2_network_iot))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES MEDIA \n")

print("\n")
print("       -    EN EL "+str(float(((access_vector_cvssv2_local_iot*100)/(access_vector_cvssv2_iot))))+" % DE VULNERABILIDADES CUYO VECTOR DE ACCESO ES LOCAL, LAS ESTADÍSTICAS DE PORCENTAJES DE COMPLEJIDAD DE ACCESO SON LAS SIGUIENTES :\n")
print("                   -    EN EL "+str(float(((access_vector_cvssv2_local_high_iot*100)/(access_vector_cvssv2_local_iot))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES ALTA \n")
print("                   -    EN EL "+str(float(((access_vector_cvssv2_local_low_iot*100)/(access_vector_cvssv2_local_iot))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES BAJA \n")
print("                   -    EN EL "+str(float(((access_vector_cvssv2_local_medium_iot*100)/(access_vector_cvssv2_local_iot))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES MEDIA \n")

if(access_vector_cvssv2_physical_iot>0):
    print("       -    EN EL "+str(float(((access_vector_cvssv2_physical_iot*100)/(access_vector_cvssv2_iot))))+" % DE VULNERABILIDADES CUYO VECTOR DE ACCESO ES FÍSICO, LAS ESTADÍSTICAS DE PORCENTAJES DE COMPLEJIDAD DE ACCESO SON LAS SIGUIENTES :\n")
    print("                   -    EN EL "+str(float(((access_vector_cvssv2_physical_high_iot*100)/(access_vector_cvssv2_physical_iot))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES ALTA \n")
    print("                   -    EN EL "+str(float(((access_vector_cvssv2_physical_low_iot*100)/(access_vector_cvssv2_physical_iot))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES BAJA \n")
    print("                   -    EN EL "+str(float(((access_vector_cvssv2_physical_medium_iot*100)/(access_vector_cvssv2_physical_iot))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES MEDIA \n")


print("       -    EN EL "+str(float(((access_vector_cvssv2_adjacent_iot*100)/(access_vector_cvssv2_iot))))+" % DE VULNERABILIDADES CUYO VECTOR DE ACCESO ES ADYACENTE, LAS ESTADÍSTICAS DE PORCENTAJES DE COMPLEJIDAD DE ACCESO SON LAS SIGUIENTES :\n")
print("                   -    EN EL "+str(float(((access_vector_cvssv2_adjacent_high_iot*100)/(access_vector_cvssv2_adjacent_iot))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES ALTA \n")
print("                   -    EN EL "+str(float(((access_vector_cvssv2_adjacent_low_iot*100)/(access_vector_cvssv2_adjacent_iot))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES BAJA \n")
print("                   -    EN EL "+str(float(((access_vector_cvssv2_adjacent_medium_iot*100)/(access_vector_cvssv2_adjacent_iot))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES MEDIA \n")


#Variables para almacenar los distintos de contadores de vector de acceso y su complejidad de acceso para la parte SMART HOME
access_vector_cvssv2_sh=0


#Variables donde aumento el contador segun la relacion entre el vector de acceso y su complejidad de acceso
#Por cada tipo de vector de acceso tengo una variable con su complejidad de acceso
access_vector_cvssv2_network_sh=0
access_vector_cvssv2_network_low_sh=0
access_vector_cvssv2_network_high_sh=0
access_vector_cvssv2_network_medium_sh=0


access_vector_cvssv2_adjacent_sh=0
access_vector_cvssv2_adjacent_low_sh=0
access_vector_cvssv2_adjacent_high_sh=0
access_vector_cvssv2_adjacent_medium_sh=0


access_vector_cvssv2_local_sh=0
access_vector_cvssv2_local_low_sh=0
access_vector_cvssv2_local_high_sh=0
access_vector_cvssv2_local_medium_sh=0


access_vector_cvssv2_physical_sh=0
access_vector_cvssv2_physical_low_sh=0
access_vector_cvssv2_physical_high_sh=0
access_vector_cvssv2_physical_medium_sh=0





#Recorro cada fila del fichero comprobando valores. Primeramente compruebo que el vector de ACCESO no sea nulo y aumento el contador

for j in range(0,len(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.accessVector"])):
    if(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.accessVector"][j]!='NONE'):
        access_vector_cvssv2_sh+=1
        #Compruebo el tipo de vector de ACCESO
        if(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.accessVector"][j]=='NETWORK'):
            access_vector_cvssv2_network_sh+=1
            #Compruebo la complejidad de ACCESO
            if(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.accessComplexity"][j]=='HIGH'):
                access_vector_cvssv2_network_high_sh+=1
            elif(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.accessComplexity"][j]=='LOW'):
                access_vector_cvssv2_network_low_sh+=1
            elif(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.accessComplexity"][j]=='MEDIUM'):
                access_vector_cvssv2_network_medium_sh+=1       
        elif(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.accessVector"][j]=='LOCAL'):
            access_vector_cvssv2_local_sh+=1
            if(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.accessComplexity"][j]=='HIGH'):
                access_vector_cvssv2_local_high_sh+=1
            elif(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.accessComplexity"][j]=='LOW'):
                access_vector_cvssv2_local_low_sh+=1
            elif(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.accessComplexity"][j]=='MEDIUM'):
                access_vector_cvssv2_local_medium_sh+=1

        elif(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.accessVector"][j]=='PHYSICAL'):
            access_vector_cvssv2_physical_sh+=1
            if(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.accessComplexity"][j]=='HIGH'):
                access_vector_cvssv2_physical_high_sh+=1
            elif(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.accessComplexity"][j]=='LOW'):
                access_vector_cvssv2_physical_low_sh+=1
            elif(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.accessComplexity"][j]=='MEDIUM'):
                access_vector_cvssv2_physical_medium_sh+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.accessVector"][j]=='ADJACENT_NETWORK'):
            access_vector_cvssv2_adjacent_sh+=1
            if(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.accessComplexity"][j]=='HIGH'):
                access_vector_cvssv2_adjacent_high_sh+=1
            elif(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.accessComplexity"][j]=='LOW'):
                access_vector_cvssv2_adjacent_low_sh+=1
            elif(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.accessComplexity"][j]=='MEDIUM'):
                access_vector_cvssv2_adjacent_medium_sh+=1
        
                        
                        
                        
                        
print("**************************ESTADÍSTICAS VECTOR DE ACCESO/COMPLEJIDAD DE ACCESO SEGÚN VECTOR CVSSV2 CVE SMART HOME********************************")
print("\n")
print(" DE UN TOTAL DE "+str(access_vector_cvssv2_sh)+" VECTORES DE ACCESO, LAS ESTADÍSTICAS DE SON LAS SIGUIENTES: \n")
print("\n")
print(" - EN UN TOTAL DE "+str(access_vector_cvssv2_network_sh)+" VULNERABILIDADES EL VECTOR DE ACCESO ES NETWORK. \n")
print(" - EN UN TOTAL DE "+str(access_vector_cvssv2_local_sh)+" VULNERABILIDADES EL VECTOR DE ACCESO ES LOCAL. \n")
print(" - EN UN TOTAL DE "+str(access_vector_cvssv2_physical_sh)+" VULNERABILIDADES EL VECTOR DE ACCESO ES FÍSICO. \n")
print(" - EN UN TOTAL DE "+str(access_vector_cvssv2_adjacent_sh)+" VULNERABILIDADES EL VECTOR DE ACCESO ES ADYACENTE. \n")

print("***********************************************************************************************************************************")
print("\n")
print("       -    EN UN TOTAL DE "+str(access_vector_cvssv2_network_sh)+" VULNERABILIDADES CUYO VECTOR DE ACCESO ES NETWORK, LAS ESTADÍSTICAS DE COMPLEJIDAD DE ACCESO SON LAS SIGUIENTES \n")
print("                   -    EN UN TOTAL DE "+str(access_vector_cvssv2_network_high_sh)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES ALTA \n")
print("                   -    EN UN TOTAL DE "+str(access_vector_cvssv2_network_low_sh)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES BAJA \n")
print("                   -    EN UN TOTAL DE "+str(access_vector_cvssv2_network_medium_sh)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES MEDIA \n")

print("\n")
print("       -    EN UN TOTAL DE "+str(access_vector_cvssv2_local_sh)+" VULNERABILIDADES CUYO VECTOR DE ACCESO ES LOCAL, LAS ESTADÍSTICAS DE COMPLEJIDAD DE ACCESO SON LAS SIGUIENTES \n")
print("                   -    EN UN TOTAL DE "+str(access_vector_cvssv2_local_high_sh)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES ALTA \n")
print("                   -    EN UN TOTAL DE "+str(access_vector_cvssv2_local_low_sh)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES BAJA \n")
print("                   -    EN UN TOTAL DE "+str(access_vector_cvssv2_local_medium_sh)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES MEDIA \n")


print("\n")
print("       -    EN UN TOTAL DE "+str(access_vector_cvssv2_physical_sh)+" VULNERABILIDADES CUYO VECTOR DE ACCESO ES FÍSICO, LAS ESTADÍSTICAS DE COMPLEJIDAD DE ACCESO SON LAS SIGUIENTES \n")
print("                   -    EN UN TOTAL DE "+str(access_vector_cvssv2_physical_high_sh)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES ALTA \n")
print("                   -    EN UN TOTAL DE "+str(access_vector_cvssv2_physical_low_sh)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES BAJA \n")
print("                   -    EN UN TOTAL DE "+str(access_vector_cvssv2_physical_medium_sh)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES MEDIA \n")


print("\n")
print("       -    EN UN TOTAL DE "+str(access_vector_cvssv2_adjacent_sh)+" VULNERABILIDADES CUYO VECTOR DE ACCESO ES ADYACENTE, LAS ESTADÍSTICAS DE COMPLEJIDAD DE ACCESO SON LAS SIGUIENTES \n")
print("                   -    EN UN TOTAL DE "+str(access_vector_cvssv2_adjacent_high_sh)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES ALTA \n")
print("                   -    EN UN TOTAL DE "+str(access_vector_cvssv2_adjacent_low_sh)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES BAJA \n")
print("                   -    EN UN TOTAL DE "+str(access_vector_cvssv2_adjacent_medium_sh)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES MEDIA \n")












print("**************************PORCENTAJES VECTOR DE ACCESO/COMPLEJIDAD DE ACCESO SEGÚN VECTOR CVSSV2 CVE SMART HOME********************************")
print("\n")
print(" DE UN TOTAL DE "+str(access_vector_cvssv2_sh)+" VECTORES DE ACCESO, LAS ESTADÍSTICAS DE PORCENTAJES SON LAS SIGUIENTES: \n")
print("\n")
print(" - EN EL "+str(float(((access_vector_cvssv2_network_sh*100)/(access_vector_cvssv2_sh))))+" % DE VULNERABILIDADES EL VECTOR DE ACCESO ES NETWORK.  \n")
print(" - EN EL "+str(float(((access_vector_cvssv2_local_sh*100)/(access_vector_cvssv2_sh))))+" % DE VULNERABILIDADES EL VECTOR DE ACCESO ES LOCAL.  \n")
print(" - EN EL "+str(float(((access_vector_cvssv2_physical_sh*100)/(access_vector_cvssv2_sh))))+" % DE VULNERABILIDADES EL VECTOR DE ACCESO ES FÍSICO.  \n")
print(" - EN EL "+str(float(((access_vector_cvssv2_adjacent_sh*100)/(access_vector_cvssv2_sh))))+" % DE VULNERABILIDADES EL VECTOR DE ACCESO ES ADYACENTE.  \n")
print("\n")
print("***********************************************************************************************************************************")

print("\n")
print("       -    EN EL "+str(float(((access_vector_cvssv2_network_sh*100)/(access_vector_cvssv2_sh))))+" % DE VULNERABILIDADES CUYO VECTOR DE ACCESO ES NETWORK, LAS ESTADÍSTICAS DE PORCENTAJES DE COMPLEJIDAD DE ACCESO SON LAS SIGUIENTES :\n")
print("                   -    EN EL "+str(float(((access_vector_cvssv2_network_high_sh*100)/(access_vector_cvssv2_network_sh))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES ALTA \n")
print("                   -    EN EL "+str(float(((access_vector_cvssv2_network_low_sh*100)/(access_vector_cvssv2_network_sh))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES BAJA \n")
print("                   -    EN EL "+str(float(((access_vector_cvssv2_network_medium_sh*100)/(access_vector_cvssv2_network_sh))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES MEDIA \n")

print("\n")
print("       -    EN EL "+str(float(((access_vector_cvssv2_local_sh*100)/(access_vector_cvssv2_sh))))+" % DE VULNERABILIDADES CUYO VECTOR DE ACCESO ES LOCAL, LAS ESTADÍSTICAS DE PORCENTAJES DE COMPLEJIDAD DE ACCESO SON LAS SIGUIENTES :\n")
print("                   -    EN EL "+str(float(((access_vector_cvssv2_local_high_sh*100)/(access_vector_cvssv2_local_sh))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES ALTA \n")
print("                   -    EN EL "+str(float(((access_vector_cvssv2_local_low_sh*100)/(access_vector_cvssv2_local_sh))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES BAJA \n")
print("                   -    EN EL "+str(float(((access_vector_cvssv2_local_medium_sh*100)/(access_vector_cvssv2_local_sh))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES MEDIA \n")

if(access_vector_cvssv2_physical_sh>0):
    print("       -    EN EL "+str(float(((access_vector_cvssv2_physical_sh*100)/(access_vector_cvssv2_sh))))+" % DE VULNERABILIDADES CUYO VECTOR DE ACCESO ES FÍSICO, LAS ESTADÍSTICAS DE PORCENTAJES DE COMPLEJIDAD DE ACCESO SON LAS SIGUIENTES :\n")
    print("                   -    EN EL "+str(float(((access_vector_cvssv2_physical_high_sh*100)/(access_vector_cvssv2_physical_sh))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES ALTA \n")
    print("                   -    EN EL "+str(float(((access_vector_cvssv2_physical_low_sh*100)/(access_vector_cvssv2_physical_sh))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES BAJA \n")
    print("                   -    EN EL "+str(float(((access_vector_cvssv2_physical_medium_sh*100)/(access_vector_cvssv2_physical_sh))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES MEDIA \n")


print("       -    EN EL "+str(float(((access_vector_cvssv2_adjacent_sh*100)/(access_vector_cvssv2_sh))))+" % DE VULNERABILIDADES CUYO VECTOR DE ACCESO ES ADYACENTE, LAS ESTADÍSTICAS DE PORCENTAJES DE COMPLEJIDAD DE ACCESO SON LAS SIGUIENTES :\n")
print("                   -    EN EL "+str(float(((access_vector_cvssv2_adjacent_high_sh*100)/(access_vector_cvssv2_adjacent_sh))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES ALTA \n")
print("                   -    EN EL "+str(float(((access_vector_cvssv2_adjacent_low_sh*100)/(access_vector_cvssv2_adjacent_sh))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES BAJA \n")
print("                   -    EN EL "+str(float(((access_vector_cvssv2_adjacent_medium_sh*100)/(access_vector_cvssv2_adjacent_sh))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES MEDIA \n")













print("**************************ESTADÍSTICAS VECTOR DE ACCESO/COMPLEJIDAD DE ACCESO SEGÚN VECTOR CVSSV2 CVE PARTE IOT Y SMART HOME CONJUNTAS********************************")
print("\n")
print(" DE UN TOTAL DE "+str(access_vector_cvssv2_sh+access_vector_cvssv2_iot)+" VECTORES DE ACCESO, LAS ESTADÍSTICAS DE VECTOR DE ACCESO SON LAS SIGUIENTES: \n")
print("\n")
print(" - EN UN TOTAL DE "+str(access_vector_cvssv2_network_sh+access_vector_cvssv2_network_iot)+" VULNERABILIDADES EL VECTOR DE ACCESO ES NETWORK.  \n")
print(" - EN UN TOTAL DE "+str(access_vector_cvssv2_local_sh+access_vector_cvssv2_local_iot)+" VULNERABILIDADES EL VECTOR DE ACCESO ES LOCAL.  \n")
print(" - EN UN TOTAL DE "+str(access_vector_cvssv2_physical_sh+access_vector_cvssv2_physical_iot)+" VULNERABILIDADES EL VECTOR DE ACCESO ES FÍSICO.  \n")
print(" - EN UN TOTAL DE "+str(access_vector_cvssv2_adjacent_sh+access_vector_cvssv2_adjacent_iot)+" VULNERABILIDADES EL VECTOR DE ACCESO ES ADYACENTE.  \n")
print("\n")

print("***********************************************************************************************************************************")
print("\n")
print("       -    EN UN TOTAL DE "+str(access_vector_cvssv2_network_sh+access_vector_cvssv2_network_iot)+" VULNERABILIDADES CUYO VECTOR DE ACCESO ES NETWORK, LAS ESTADÍSTICAS DE COMPLEJIDAD DE ACCESO SON LAS SIGUIENTES \n")
print("                   -    EN UN TOTAL DE "+str(access_vector_cvssv2_network_high_sh+access_vector_cvssv2_network_high_iot)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES ALTA \n")
print("                   -    EN UN TOTAL DE "+str(access_vector_cvssv2_network_low_sh+access_vector_cvssv2_network_low_iot)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES BAJA \n")
print("                   -    EN UN TOTAL DE "+str(access_vector_cvssv2_network_medium_sh+access_vector_cvssv2_network_medium_iot)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES MEDIA \n")

print("\n")
print("       -    EN UN TOTAL DE "+str(access_vector_cvssv2_local_sh+access_vector_cvssv2_local_iot)+" VULNERABILIDADES CUYO VECTOR DE ACCESO ES LOCAL, LAS ESTADÍSTICAS DE COMPLEJIDAD DE ACCESO SON LAS SIGUIENTES \n")
print("                   -    EN UN TOTAL DE "+str(access_vector_cvssv2_local_high_sh+access_vector_cvssv2_local_high_iot)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES ALTA \n")
print("                   -    EN UN TOTAL DE "+str(access_vector_cvssv2_local_low_sh+access_vector_cvssv2_local_low_iot)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES BAJA \n")
print("                   -    EN UN TOTAL DE "+str(access_vector_cvssv2_local_medium_sh+access_vector_cvssv2_local_medium_iot)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES MEDIA \n")


print("\n")
print("       -    EN UN TOTAL DE "+str(access_vector_cvssv2_physical_sh+access_vector_cvssv2_physical_iot)+" VULNERABILIDADES CUYO VECTOR DE ACCESO ES FÍSICO, LAS ESTADÍSTICAS DE COMPLEJIDAD DE ACCESO SON LAS SIGUIENTES \n")
print("                   -    EN UN TOTAL DE "+str(access_vector_cvssv2_physical_high_sh+access_vector_cvssv2_physical_high_iot)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES ALTA \n")
print("                   -    EN UN TOTAL DE "+str(access_vector_cvssv2_physical_low_sh+access_vector_cvssv2_physical_low_iot)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES BAJA \n")
print("                   -    EN UN TOTAL DE "+str(access_vector_cvssv2_physical_medium_sh+access_vector_cvssv2_physical_medium_iot)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES MEDIA \n")


print("\n")
print("       -    EN UN TOTAL DE "+str(access_vector_cvssv2_adjacent_sh+access_vector_cvssv2_adjacent_iot)+" VULNERABILIDADES CUYO VECTOR DE ACCESO ES ADYACENTE, LAS ESTADÍSTICAS DE COMPLEJIDAD DE ACCESO SON LAS SIGUIENTES \n")
print("                   -    EN UN TOTAL DE "+str(access_vector_cvssv2_adjacent_high_sh+access_vector_cvssv2_adjacent_high_iot)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES ALTA \n")
print("                   -    EN UN TOTAL DE "+str(access_vector_cvssv2_adjacent_low_sh+access_vector_cvssv2_adjacent_low_iot)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES BAJA \n")
print("                   -    EN UN TOTAL DE "+str(access_vector_cvssv2_adjacent_medium_sh+access_vector_cvssv2_adjacent_medium_iot)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES MEDIA \n")


print("**************************PORCENTAJES VECTOR DE ACCESO/COMPLEJIDAD DE ACCESO SEGÚN VECTOR CVSSV2 CVE PARTE IOT Y SMART HOME CONJJUNTAS********************************")
print("\n")
print(" DE UN TOTAL DE "+str(access_vector_cvssv2_sh+access_vector_cvssv2_iot)+" VECTORES DE ACCESO, LAS ESTADÍSTICAS DE PORCENTAJES SON LAS SIGUIENTES: \n")
print("\n")
print(" - EN EL "+str(float((((access_vector_cvssv2_network_sh+access_vector_cvssv2_network_iot)*100)/(access_vector_cvssv2_sh+access_vector_cvssv2_iot))))+" % DE VULNERABILIDADES EL VECTOR DE ACCESO ES NETWORK. \n")
print(" - EN EL "+str(float((((access_vector_cvssv2_local_sh+access_vector_cvssv2_local_iot)*100)/(access_vector_cvssv2_sh+access_vector_cvssv2_iot))))+" % DE VULNERABILIDADES EL VECTOR DE ACCESO ES LOCAL. \n")
print(" - EN EL "+str(float((((access_vector_cvssv2_physical_sh+access_vector_cvssv2_physical_iot)*100)/(access_vector_cvssv2_sh+access_vector_cvssv2_iot))))+" % DE VULNERABILIDADES EL VECTOR DE ACCESO ES FÍSICO. \n")
print(" - EN EL "+str(float((((access_vector_cvssv2_adjacent_sh+access_vector_cvssv2_adjacent_iot)*100)/(access_vector_cvssv2_sh+access_vector_cvssv2_iot))))+" % DE VULNERABILIDADES EL VECTOR DE ACCESO ES ADYACENTE. \n")
print("\n")
print("***********************************************************************************************************************************")
print("\n")
print("       -    EN EL "+str(float((((access_vector_cvssv2_network_sh+access_vector_cvssv2_network_iot)*100)/(access_vector_cvssv2_sh+access_vector_cvssv2_iot))))+" % DE VULNERABILIDADES CUYO VECTOR DE ACCESO ES NETWORK. LAS ESTADÍSTICAS DE PORCENTAJES DE COMPLEJIDAD DE ACCESO SON LAS SIGUIENTES :\n")
print("                   -    EN EL "+str(float((((access_vector_cvssv2_network_high_sh+access_vector_cvssv2_network_high_iot)*100)/(access_vector_cvssv2_network_sh+access_vector_cvssv2_network_iot))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES ALTA \n")
print("                   -    EN EL "+str(float((((access_vector_cvssv2_network_low_sh+access_vector_cvssv2_network_low_iot)*100)/(access_vector_cvssv2_network_sh+access_vector_cvssv2_network_iot))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES BAJA \n")
print("                   -    EN EL "+str(float((((access_vector_cvssv2_network_medium_sh+access_vector_cvssv2_network_medium_iot)*100)/(access_vector_cvssv2_network_sh+access_vector_cvssv2_network_iot))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES MEDIA \n")

print("\n")
print("       -    EN EL "+str(float((((access_vector_cvssv2_local_sh+access_vector_cvssv2_local_iot)*100)/(access_vector_cvssv2_sh+access_vector_cvssv2_iot))))+" % DE VULNERABILIDADES CUYO VECTOR DE ACCESO ES LOCAL. LAS ESTADÍSTICAS DE PORCENTAJES DE COMPLEJIDAD DE ACCESO SON LAS SIGUIENTES :\n")
print("                   -    EN EL "+str(float((((access_vector_cvssv2_local_high_sh+access_vector_cvssv2_local_high_iot)*100)/(access_vector_cvssv2_local_sh+access_vector_cvssv2_local_iot))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES ALTA \n")
print("                   -    EN EL "+str(float((((access_vector_cvssv2_local_low_sh+access_vector_cvssv2_local_low_iot)*100)/(access_vector_cvssv2_local_sh+access_vector_cvssv2_local_iot))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES BAJA \n")
print("                   -    EN EL "+str(float((((access_vector_cvssv2_local_medium_sh+access_vector_cvssv2_local_medium_iot)*100)/(access_vector_cvssv2_local_sh+access_vector_cvssv2_local_iot))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES MEDIA \n")

if(access_vector_cvssv2_physical_sh+access_vector_cvssv2_physical_iot>0):
    print("\n")
    print("       -    EN EL "+str(float((((access_vector_cvssv2_physical_sh+access_vector_cvssv2_physical_iot)*100)/(access_vector_cvssv2_sh+access_vector_cvssv2_iot))))+" % DE VULNERABILIDADES CUYO VECTOR DE ACCESO ES FÍSICO. LAS ESTADÍSTICAS DE PORCENTAJES DE COMPLEJIDAD DE ACCESO SON LAS SIGUIENTES :\n")
    print("                   -    EN EL "+str(float((((access_vector_cvssv2_physical_high_sh+access_vector_cvssv2_physical_high_iot)*100)/(access_vector_cvssv2_physical_sh+access_vector_cvssv2_physical_iot))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES ALTA \n")
    print("                   -    EN EL "+str(float((((access_vector_cvssv2_physical_low_sh+access_vector_cvssv2_physical_low_iot)*100)/(access_vector_cvssv2_physical_sh+access_vector_cvssv2_physical_iot))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES BAJA \n")
    print("                   -    EN EL "+str(float((((access_vector_cvssv2_physical_medium_sh+access_vector_cvssv2_physical_medium_iot)*100)/(access_vector_cvssv2_physical_sh+access_vector_cvssv2_physical_iot))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES MEDIA \n")


print("\n")
print("       -    EN EL "+str(float((((access_vector_cvssv2_adjacent_sh+access_vector_cvssv2_adjacent_iot)*100)/(access_vector_cvssv2_sh+access_vector_cvssv2_iot))))+" % DE VULNERABILIDADES CUYO VECTOR DE ACCESO ES ADYACENTE. LAS ESTADÍSTICAS DE PORCENTAJES DE COMPLEJIDAD DE ACCESO SON LAS SIGUIENTES :\n")
print("                   -    EN EL "+str(float((((access_vector_cvssv2_adjacent_high_sh+access_vector_cvssv2_adjacent_high_iot)*100)/(access_vector_cvssv2_adjacent_sh+access_vector_cvssv2_adjacent_iot))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES ALTA \n")
print("                   -    EN EL "+str(float((((access_vector_cvssv2_adjacent_low_sh+access_vector_cvssv2_adjacent_low_iot)*100)/(access_vector_cvssv2_adjacent_sh+access_vector_cvssv2_adjacent_iot))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES BAJA \n")
print("                   -    EN EL "+str(float((((access_vector_cvssv2_adjacent_medium_sh+access_vector_cvssv2_adjacent_medium_iot)*100)/(access_vector_cvssv2_adjacent_sh+access_vector_cvssv2_adjacent_iot))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES MEDIA \n")




