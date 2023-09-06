
#VECTOR STRING CON PUNTUACION DE IMPACTO PARTE CVSSV2



import pandas as pd

#Abro los ficheros con los que voy a tratar


df_cve_iot=pd.read_excel('cves_iot_2023.xlsx')
df_cve_sh=pd.read_excel('cves_smart_home_2023.xlsx')


# PUNTUACION DE IMPACTO 10

#Variable para almacenar numero de vulnerabilidades con una puntuacion de IMPACTO concreta
cvssV2_IMPACT_score_10_iot=0

#Tipo de vector de acceso segun puntuacion de IMPACTO
cvssV2_IMPACT_score_10_iot_accessvector_NETWORK=0
cvssV2_IMPACT_score_10_iot_accessvector_PHYSICAL=0
cvssV2_IMPACT_score_10_iot_accessvector_LOCAL=0
cvssV2_IMPACT_score_10_iot_accessvector_ADJACENT_NETWORK=0

#Complejidad de acceso segun puntuacion de IMPACTO
cvssV2_IMPACT_score_10_iot_accesscomplexity_HIGH=0
cvssV2_IMPACT_score_10_iot_accesscomplexity_LOW=0
cvssV2_IMPACT_score_10_iot_accesscomplexity_MEDIUM=0
cvssV2_IMPACT_score_10_iot_accesscomplexity_NONE=0

#Nivel de autenticacion segun puntuacion de IMPACTO
cvssV2_IMPACT_score_10_iot_authentication_SINGLE=0
cvssV2_IMPACT_score_10_iot_authentication_MULTIPLE=0
cvssV2_IMPACT_score_10_iot_authentication_NONE=0

#Impacto de confidencialidad segun puntuacion de IMPACTO
cvssV2_IMPACT_score_10_iot_confidentialityImpact_COMPLETE=0
cvssV2_IMPACT_score_10_iot_confidentialityImpact_PARTIAL=0
cvssV2_IMPACT_score_10_iot_confidentialityImpact_NONE=0

#Impacto de integridad segun puntuacion de IMPACTO
cvssV2_IMPACT_score_10_iot_integrityImpact_COMPLETE=0
cvssV2_IMPACT_score_10_iot_integrityImpact_PARTIAL=0
cvssV2_IMPACT_score_10_iot_integrityImpact_NONE=0

#Impacto de disponibilidad segun puntuacion de IMPACTO
cvssV2_IMPACT_score_10_iot_availabilityImpact_COMPLETE=0
cvssV2_IMPACT_score_10_iot_availabilityImpact_PARTIAL=0
cvssV2_IMPACT_score_10_iot_availabilityImpact_NONE=0


# PUNTUACION DE IMPACTO 9

cvssV2_IMPACT_score_9_iot=0

cvssV2_IMPACT_score_9_iot_accessvector_NETWORK=0
cvssV2_IMPACT_score_9_iot_accessvector_PHYSICAL=0
cvssV2_IMPACT_score_9_iot_accessvector_LOCAL=0
cvssV2_IMPACT_score_9_iot_accessvector_ADJACENT_NETWORK=0

cvssV2_IMPACT_score_9_iot_accesscomplexity_HIGH=0
cvssV2_IMPACT_score_9_iot_accesscomplexity_LOW=0
cvssV2_IMPACT_score_9_iot_accesscomplexity_MEDIUM=0
cvssV2_IMPACT_score_9_iot_accesscomplexity_NONE=0

cvssV2_IMPACT_score_9_iot_authentication_SINGLE=0
cvssV2_IMPACT_score_9_iot_authentication_MULTIPLE=0
cvssV2_IMPACT_score_9_iot_authentication_NONE=0

cvssV2_IMPACT_score_9_iot_confidentialityImpact_COMPLETE=0
cvssV2_IMPACT_score_9_iot_confidentialityImpact_PARTIAL=0
cvssV2_IMPACT_score_9_iot_confidentialityImpact_NONE=0


cvssV2_IMPACT_score_9_iot_integrityImpact_COMPLETE=0
cvssV2_IMPACT_score_9_iot_integrityImpact_PARTIAL=0
cvssV2_IMPACT_score_9_iot_integrityImpact_NONE=0


cvssV2_IMPACT_score_9_iot_availabilityImpact_COMPLETE=0
cvssV2_IMPACT_score_9_iot_availabilityImpact_PARTIAL=0
cvssV2_IMPACT_score_9_iot_availabilityImpact_NONE=0


# PUNTUACION DE IMPACTO 8

cvssV2_IMPACT_score_8_iot=0

cvssV2_IMPACT_score_8_iot_accessvector_NETWORK=0
cvssV2_IMPACT_score_8_iot_accessvector_PHYSICAL=0
cvssV2_IMPACT_score_8_iot_accessvector_LOCAL=0
cvssV2_IMPACT_score_8_iot_accessvector_ADJACENT_NETWORK=0

cvssV2_IMPACT_score_8_iot_accesscomplexity_HIGH=0
cvssV2_IMPACT_score_8_iot_accesscomplexity_LOW=0
cvssV2_IMPACT_score_8_iot_accesscomplexity_MEDIUM=0
cvssV2_IMPACT_score_8_iot_accesscomplexity_NONE=0

cvssV2_IMPACT_score_8_iot_authentication_SINGLE=0
cvssV2_IMPACT_score_8_iot_authentication_MULTIPLE=0
cvssV2_IMPACT_score_8_iot_authentication_NONE=0

cvssV2_IMPACT_score_8_iot_confidentialityImpact_COMPLETE=0
cvssV2_IMPACT_score_8_iot_confidentialityImpact_PARTIAL=0
cvssV2_IMPACT_score_8_iot_confidentialityImpact_NONE=0


cvssV2_IMPACT_score_8_iot_integrityImpact_COMPLETE=0
cvssV2_IMPACT_score_8_iot_integrityImpact_PARTIAL=0
cvssV2_IMPACT_score_8_iot_integrityImpact_NONE=0


cvssV2_IMPACT_score_8_iot_availabilityImpact_COMPLETE=0
cvssV2_IMPACT_score_8_iot_availabilityImpact_PARTIAL=0
cvssV2_IMPACT_score_8_iot_availabilityImpact_NONE=0


# PUNTUACION DE IMPACTO 7

cvssV2_IMPACT_score_7_iot=0

cvssV2_IMPACT_score_7_iot_accessvector_NETWORK=0
cvssV2_IMPACT_score_7_iot_accessvector_PHYSICAL=0
cvssV2_IMPACT_score_7_iot_accessvector_LOCAL=0
cvssV2_IMPACT_score_7_iot_accessvector_ADJACENT_NETWORK=0

cvssV2_IMPACT_score_7_iot_accesscomplexity_HIGH=0
cvssV2_IMPACT_score_7_iot_accesscomplexity_LOW=0
cvssV2_IMPACT_score_7_iot_accesscomplexity_MEDIUM=0
cvssV2_IMPACT_score_7_iot_accesscomplexity_NONE=0

cvssV2_IMPACT_score_7_iot_authentication_SINGLE=0
cvssV2_IMPACT_score_7_iot_authentication_MULTIPLE=0
cvssV2_IMPACT_score_7_iot_authentication_NONE=0

cvssV2_IMPACT_score_7_iot_confidentialityImpact_COMPLETE=0
cvssV2_IMPACT_score_7_iot_confidentialityImpact_PARTIAL=0
cvssV2_IMPACT_score_7_iot_confidentialityImpact_NONE=0


cvssV2_IMPACT_score_7_iot_integrityImpact_COMPLETE=0
cvssV2_IMPACT_score_7_iot_integrityImpact_PARTIAL=0
cvssV2_IMPACT_score_7_iot_integrityImpact_NONE=0


cvssV2_IMPACT_score_7_iot_availabilityImpact_COMPLETE=0
cvssV2_IMPACT_score_7_iot_availabilityImpact_PARTIAL=0
cvssV2_IMPACT_score_7_iot_availabilityImpact_NONE=0

# PUNTUACION DE IMPACTO 6

cvssV2_IMPACT_score_6_iot=0

cvssV2_IMPACT_score_6_iot_accessvector_NETWORK=0
cvssV2_IMPACT_score_6_iot_accessvector_PHYSICAL=0
cvssV2_IMPACT_score_6_iot_accessvector_LOCAL=0
cvssV2_IMPACT_score_6_iot_accessvector_ADJACENT_NETWORK=0

cvssV2_IMPACT_score_6_iot_accesscomplexity_HIGH=0
cvssV2_IMPACT_score_6_iot_accesscomplexity_LOW=0
cvssV2_IMPACT_score_6_iot_accesscomplexity_MEDIUM=0
cvssV2_IMPACT_score_6_iot_accesscomplexity_NONE=0

cvssV2_IMPACT_score_6_iot_authentication_SINGLE=0
cvssV2_IMPACT_score_6_iot_authentication_MULTIPLE=0
cvssV2_IMPACT_score_6_iot_authentication_NONE=0

cvssV2_IMPACT_score_6_iot_confidentialityImpact_COMPLETE=0
cvssV2_IMPACT_score_6_iot_confidentialityImpact_PARTIAL=0
cvssV2_IMPACT_score_6_iot_confidentialityImpact_NONE=0


cvssV2_IMPACT_score_6_iot_integrityImpact_COMPLETE=0
cvssV2_IMPACT_score_6_iot_integrityImpact_PARTIAL=0
cvssV2_IMPACT_score_6_iot_integrityImpact_NONE=0


cvssV2_IMPACT_score_6_iot_availabilityImpact_COMPLETE=0
cvssV2_IMPACT_score_6_iot_availabilityImpact_PARTIAL=0
cvssV2_IMPACT_score_6_iot_availabilityImpact_NONE=0


# PUNTUACION DE IMPACTO 5

cvssV2_IMPACT_score_5_iot=0

cvssV2_IMPACT_score_5_iot_accessvector_NETWORK=0
cvssV2_IMPACT_score_5_iot_accessvector_PHYSICAL=0
cvssV2_IMPACT_score_5_iot_accessvector_LOCAL=0
cvssV2_IMPACT_score_5_iot_accessvector_ADJACENT_NETWORK=0

cvssV2_IMPACT_score_5_iot_accesscomplexity_HIGH=0
cvssV2_IMPACT_score_5_iot_accesscomplexity_LOW=0
cvssV2_IMPACT_score_5_iot_accesscomplexity_MEDIUM=0
cvssV2_IMPACT_score_5_iot_accesscomplexity_NONE=0

cvssV2_IMPACT_score_5_iot_authentication_SINGLE=0
cvssV2_IMPACT_score_5_iot_authentication_MULTIPLE=0
cvssV2_IMPACT_score_5_iot_authentication_NONE=0

cvssV2_IMPACT_score_5_iot_confidentialityImpact_COMPLETE=0
cvssV2_IMPACT_score_5_iot_confidentialityImpact_PARTIAL=0
cvssV2_IMPACT_score_5_iot_confidentialityImpact_NONE=0


cvssV2_IMPACT_score_5_iot_integrityImpact_COMPLETE=0
cvssV2_IMPACT_score_5_iot_integrityImpact_PARTIAL=0
cvssV2_IMPACT_score_5_iot_integrityImpact_NONE=0


cvssV2_IMPACT_score_5_iot_availabilityImpact_COMPLETE=0
cvssV2_IMPACT_score_5_iot_availabilityImpact_PARTIAL=0
cvssV2_IMPACT_score_5_iot_availabilityImpact_NONE=0



# PUNTUACION DE IMPACTO 4
cvssV2_IMPACT_score_4_iot=0

cvssV2_IMPACT_score_4_iot_accessvector_NETWORK=0
cvssV2_IMPACT_score_4_iot_accessvector_PHYSICAL=0
cvssV2_IMPACT_score_4_iot_accessvector_LOCAL=0
cvssV2_IMPACT_score_4_iot_accessvector_ADJACENT_NETWORK=0

cvssV2_IMPACT_score_4_iot_accesscomplexity_HIGH=0
cvssV2_IMPACT_score_4_iot_accesscomplexity_LOW=0
cvssV2_IMPACT_score_4_iot_accesscomplexity_MEDIUM=0
cvssV2_IMPACT_score_4_iot_accesscomplexity_NONE=0

cvssV2_IMPACT_score_4_iot_authentication_SINGLE=0
cvssV2_IMPACT_score_4_iot_authentication_MULTIPLE=0
cvssV2_IMPACT_score_4_iot_authentication_NONE=0

cvssV2_IMPACT_score_4_iot_confidentialityImpact_COMPLETE=0
cvssV2_IMPACT_score_4_iot_confidentialityImpact_PARTIAL=0
cvssV2_IMPACT_score_4_iot_confidentialityImpact_NONE=0


cvssV2_IMPACT_score_4_iot_integrityImpact_COMPLETE=0
cvssV2_IMPACT_score_4_iot_integrityImpact_PARTIAL=0
cvssV2_IMPACT_score_4_iot_integrityImpact_NONE=0


cvssV2_IMPACT_score_4_iot_availabilityImpact_COMPLETE=0
cvssV2_IMPACT_score_4_iot_availabilityImpact_PARTIAL=0
cvssV2_IMPACT_score_4_iot_availabilityImpact_NONE=0

# PUNTUACION DE IMPACTO 3

cvssV2_IMPACT_score_3_iot=0

cvssV2_IMPACT_score_3_iot_accessvector_NETWORK=0
cvssV2_IMPACT_score_3_iot_accessvector_PHYSICAL=0
cvssV2_IMPACT_score_3_iot_accessvector_LOCAL=0
cvssV2_IMPACT_score_3_iot_accessvector_ADJACENT_NETWORK=0

cvssV2_IMPACT_score_3_iot_accesscomplexity_HIGH=0
cvssV2_IMPACT_score_3_iot_accesscomplexity_LOW=0
cvssV2_IMPACT_score_3_iot_accesscomplexity_MEDIUM=0
cvssV2_IMPACT_score_3_iot_accesscomplexity_NONE=0

cvssV2_IMPACT_score_3_iot_authentication_SINGLE=0
cvssV2_IMPACT_score_3_iot_authentication_MULTIPLE=0
cvssV2_IMPACT_score_3_iot_authentication_NONE=0

cvssV2_IMPACT_score_3_iot_confidentialityImpact_COMPLETE=0
cvssV2_IMPACT_score_3_iot_confidentialityImpact_PARTIAL=0
cvssV2_IMPACT_score_3_iot_confidentialityImpact_NONE=0


cvssV2_IMPACT_score_3_iot_integrityImpact_COMPLETE=0
cvssV2_IMPACT_score_3_iot_integrityImpact_PARTIAL=0
cvssV2_IMPACT_score_3_iot_integrityImpact_NONE=0


cvssV2_IMPACT_score_3_iot_availabilityImpact_COMPLETE=0
cvssV2_IMPACT_score_3_iot_availabilityImpact_PARTIAL=0
cvssV2_IMPACT_score_3_iot_availabilityImpact_NONE=0


# PUNTUACION DE IMPACTO 2

cvssV2_IMPACT_score_2_iot=0

cvssV2_IMPACT_score_2_iot_accessvector_NETWORK=0
cvssV2_IMPACT_score_2_iot_accessvector_PHYSICAL=0
cvssV2_IMPACT_score_2_iot_accessvector_LOCAL=0
cvssV2_IMPACT_score_2_iot_accessvector_ADJACENT_NETWORK=0

cvssV2_IMPACT_score_2_iot_accesscomplexity_HIGH=0
cvssV2_IMPACT_score_2_iot_accesscomplexity_LOW=0
cvssV2_IMPACT_score_2_iot_accesscomplexity_MEDIUM=0
cvssV2_IMPACT_score_2_iot_accesscomplexity_NONE=0

cvssV2_IMPACT_score_2_iot_authentication_SINGLE=0
cvssV2_IMPACT_score_2_iot_authentication_MULTIPLE=0
cvssV2_IMPACT_score_2_iot_authentication_NONE=0

cvssV2_IMPACT_score_2_iot_confidentialityImpact_COMPLETE=0
cvssV2_IMPACT_score_2_iot_confidentialityImpact_PARTIAL=0
cvssV2_IMPACT_score_2_iot_confidentialityImpact_NONE=0


cvssV2_IMPACT_score_2_iot_integrityImpact_COMPLETE=0
cvssV2_IMPACT_score_2_iot_integrityImpact_PARTIAL=0
cvssV2_IMPACT_score_2_iot_integrityImpact_NONE=0


cvssV2_IMPACT_score_2_iot_availabilityImpact_COMPLETE=0
cvssV2_IMPACT_score_2_iot_availabilityImpact_PARTIAL=0
cvssV2_IMPACT_score_2_iot_availabilityImpact_NONE=0

# PUNTUACION DE IMPACTO 1

cvssV2_IMPACT_score_1_iot=0

cvssV2_IMPACT_score_1_iot_accessvector_NETWORK=0
cvssV2_IMPACT_score_1_iot_accessvector_PHYSICAL=0
cvssV2_IMPACT_score_1_iot_accessvector_LOCAL=0
cvssV2_IMPACT_score_1_iot_accessvector_ADJACENT_NETWORK=0

cvssV2_IMPACT_score_1_iot_accesscomplexity_HIGH=0
cvssV2_IMPACT_score_1_iot_accesscomplexity_LOW=0
cvssV2_IMPACT_score_1_iot_accesscomplexity_MEDIUM=0
cvssV2_IMPACT_score_1_iot_accesscomplexity_NONE=0

cvssV2_IMPACT_score_1_iot_authentication_SINGLE=0
cvssV2_IMPACT_score_1_iot_authentication_MULTIPLE=0
cvssV2_IMPACT_score_1_iot_authentication_NONE=0

cvssV2_IMPACT_score_1_iot_confidentialityImpact_COMPLETE=0
cvssV2_IMPACT_score_1_iot_confidentialityImpact_PARTIAL=0
cvssV2_IMPACT_score_1_iot_confidentialityImpact_NONE=0


cvssV2_IMPACT_score_1_iot_integrityImpact_COMPLETE=0
cvssV2_IMPACT_score_1_iot_integrityImpact_PARTIAL=0
cvssV2_IMPACT_score_1_iot_integrityImpact_NONE=0


cvssV2_IMPACT_score_1_iot_availabilityImpact_COMPLETE=0
cvssV2_IMPACT_score_1_iot_availabilityImpact_PARTIAL=0
cvssV2_IMPACT_score_1_iot_availabilityImpact_NONE=0

# PUNTUACION DE IMPACTO 0

cvssV2_IMPACT_score_0_iot=0

cvssV2_IMPACT_score_0_iot_accessvector_NETWORK=0
cvssV2_IMPACT_score_0_iot_accessvector_PHYSICAL=0
cvssV2_IMPACT_score_0_iot_accessvector_LOCAL=0
cvssV2_IMPACT_score_0_iot_accessvector_ADJACENT_NETWORK=0

cvssV2_IMPACT_score_0_iot_accesscomplexity_HIGH=0
cvssV2_IMPACT_score_0_iot_accesscomplexity_LOW=0
cvssV2_IMPACT_score_0_iot_accesscomplexity_MEDIUM=0
cvssV2_IMPACT_score_0_iot_accesscomplexity_NONE=0

cvssV2_IMPACT_score_0_iot_authentication_SINGLE=0
cvssV2_IMPACT_score_0_iot_authentication_MULTIPLE=0
cvssV2_IMPACT_score_0_iot_authentication_NONE=0

cvssV2_IMPACT_score_0_iot_confidentialityImpact_COMPLETE=0
cvssV2_IMPACT_score_0_iot_confidentialityImpact_PARTIAL=0
cvssV2_IMPACT_score_0_iot_confidentialityImpact_NONE=0


cvssV2_IMPACT_score_0_iot_integrityImpact_COMPLETE=0
cvssV2_IMPACT_score_0_iot_integrityImpact_PARTIAL=0
cvssV2_IMPACT_score_0_iot_integrityImpact_NONE=0


cvssV2_IMPACT_score_0_iot_availabilityImpact_COMPLETE=0
cvssV2_IMPACT_score_0_iot_availabilityImpact_PARTIAL=0
cvssV2_IMPACT_score_0_iot_availabilityImpact_NONE=0


# NO PUNTUACION DE IMPACTO

cvssV2_no_IMPACT_score_iot=0

cvssV2_no_IMPACT_score_iot_accessvector_NETWORK=0
cvssV2_no_IMPACT_score_iot_accessvector_PHYSICAL=0
cvssV2_no_IMPACT_score_iot_accessvector_LOCAL=0
cvssV2_no_IMPACT_score_iot_accessvector_ADJACENT_NETWORK=0

cvssV2_no_IMPACT_score_iot_accesscomplexity_HIGH=0
cvssV2_no_IMPACT_score_iot_accesscomplexity_LOW=0
cvssV2_no_IMPACT_score_iot_accesscomplexity_MEDIUM=0
cvssV2_no_IMPACT_score_iot_accesscomplexity_NONE=0

cvssV2_no_IMPACT_score_iot_authentication_SINGLE=0
cvssV2_no_IMPACT_score_iot_authentication_MULTIPLE=0
cvssV2_no_IMPACT_score_iot_authentication_NONE=0

cvssV2_no_IMPACT_score_iot_confidentialityImpact_COMPLETE=0
cvssV2_no_IMPACT_score_iot_confidentialityImpact_PARTIAL=0
cvssV2_no_IMPACT_score_iot_confidentialityImpact_NONE=0


cvssV2_no_IMPACT_score_iot_integrityImpact_COMPLETE=0
cvssV2_no_IMPACT_score_iot_integrityImpact_PARTIAL=0
cvssV2_no_IMPACT_score_iot_integrityImpact_NONE=0


cvssV2_no_IMPACT_score_iot_availabilityImpact_COMPLETE=0
cvssV2_no_IMPACT_score_iot_availabilityImpact_PARTIAL=0
cvssV2_no_IMPACT_score_iot_availabilityImpact_NONE=0

#Compruebo la PUNTUACION DE IMPACTO CVE CVSS3 para IOT

for j in range(0,len(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"])):
    
    if(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"][j] =='NONE'):
        cvssV2_no_IMPACT_score_iot+=1  
        #Compruebo el vector de acceso
        if(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.accessVector"][j]=='NETWORK'):
            cvssV2_no_IMPACT_score_iot_accessvector_NETWORK+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.accessVector"][j]=='LOCAL'):
            cvssV2_no_IMPACT_score_iot_accessvector_LOCAL+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.accessVector"][j]=='PHYSICAL'):
            cvssV2_no_IMPACT_score_iot_accessvector_PHYSICAL+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.accessVector"][j]=='ADJACENT_NETWORK'):
            cvssV2_no_IMPACT_score_iot_accessvector_ADJACENT_NETWORK+=1
        #Compruebo la complejidad de acceso  
        if(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.accessComplexity"][j]=='HIGH'):
            cvssV2_no_IMPACT_score_iot_accesscomplexity_HIGH+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.accessComplexity"][j]=='LOW'):
            cvssV2_no_IMPACT_score_iot_accesscomplexity_LOW+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.accessComplexity"][j]=='MEDIUM'):
            cvssV2_no_IMPACT_score_iot_accesscomplexity_MEDIUM+=1
        else:
            cvssV2_no_IMPACT_score_iot_accesscomplexity_NONE+=1  
                
        #Compruebo el nivel de autenticacion
        if(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.authentication"][j]=="SINGLE"):
            cvssV2_no_IMPACT_score_iot_authentication_SINGLE+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.authentication"][j]=="MULTIPLE"):
            cvssV2_no_IMPACT_score_iot_authentication_MULTIPLE+=1
        else:
            cvssV2_no_IMPACT_score_iot_authentication_NONE+=1
           
        #Compruebo el impacto de confidencialidad
        if(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.confidentialityImpact"][j]=='COMPLETE'):
            cvssV2_no_IMPACT_score_iot_confidentialityImpact_COMPLETE+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.confidentialityImpact"][j]=='PARTIAL'):
            cvssV2_no_IMPACT_score_iot_confidentialityImpact_PARTIAL+=1
        else:
            cvssV2_no_IMPACT_score_iot_confidentialityImpact_NONE+=1 
            
        #Compruebo el impacto de integridad   
        if(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.integrityImpact"][j]=='COMPLETE'):
            cvssV2_no_IMPACT_score_iot_integrityImpact_COMPLETE+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.integrityImpact"][j]=='PARTIAL'):
            cvssV2_no_IMPACT_score_iot_integrityImpact_PARTIAL+=1
        else:
            cvssV2_no_IMPACT_score_iot_integrityImpact_NONE+=1    
            
        #Compruebo el impacto de disponibilidad
        if(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.availabilityImpact"][j]=='COMPLETE'):
            cvssV2_no_IMPACT_score_iot_availabilityImpact_COMPLETE+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.availabilityImpact"][j]=='PARTIAL'):
            cvssV2_no_IMPACT_score_iot_availabilityImpact_PARTIAL+=1
        else:
            cvssV2_no_IMPACT_score_iot_availabilityImpact_NONE+=1
    
    elif(((float(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"][j])) < 10.0) and ((float(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"][j])) >=9.0)):
        cvssV2_IMPACT_score_9_iot+=1   
        if(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.accessVector"][j]=='NETWORK'):
            cvssV2_IMPACT_score_9_iot_accessvector_NETWORK+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.accessVector"][j]=='LOCAL'):
            cvssV2_IMPACT_score_9_iot_accessvector_LOCAL+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.accessVector"][j]=='PHYSICAL'):
            cvssV2_IMPACT_score_9_iot_accessvector_PHYSICAL+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.accessVector"][j]=='ADJACENT_NETWORK'):
            cvssV2_IMPACT_score_9_iot_accessvector_ADJACENT_NETWORK+=1
            
        if(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.accessComplexity"][j]=='HIGH'):
            cvssV2_IMPACT_score_9_iot_accesscomplexity_HIGH+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.accessComplexity"][j]=='LOW'):
            cvssV2_IMPACT_score_9_iot_accesscomplexity_LOW+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.accessComplexity"][j]=='MEDIUM'):
            cvssV2_IMPACT_score_9_iot_accesscomplexity_MEDIUM+=1
        else:
            cvssV2_IMPACT_score_9_iot_accesscomplexity_NONE+=1  
                
        if(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.authentication"][j]=="SINGLE"):
            cvssV2_IMPACT_score_9_iot_authentication_SINGLE+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.authentication"][j]=="MULTIPLE"):
            cvssV2_IMPACT_score_9_iot_authentication_MULTIPLE+=1
        else:
            cvssV2_IMPACT_score_9_iot_authentication_NONE+=1
                
        if(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.confidentialityImpact"][j]=='COMPLETE'):
            cvssV2_IMPACT_score_9_iot_confidentialityImpact_COMPLETE+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.confidentialityImpact"][j]=='PARTIAL'):
            cvssV2_IMPACT_score_9_iot_confidentialityImpact_PARTIAL+=1
        else:
            cvssV2_IMPACT_score_9_iot_confidentialityImpact_NONE+=1 
            
            
        if(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.integrityImpact"][j]=='COMPLETE'):
            cvssV2_IMPACT_score_9_iot_integrityImpact_COMPLETE+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.integrityImpact"][j]=='PARTIAL'):
            cvssV2_IMPACT_score_9_iot_integrityImpact_PARTIAL+=1
        else:
            cvssV2_IMPACT_score_9_iot_integrityImpact_NONE+=1    
            
          
        if(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.availabilityImpact"][j]=='COMPLETE'):
            cvssV2_IMPACT_score_9_iot_availabilityImpact_COMPLETE+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.availabilityImpact"][j]=='PARTIAL'):
            cvssV2_IMPACT_score_9_iot_availabilityImpact_PARTIAL+=1
        else:
            cvssV2_IMPACT_score_9_iot_availabilityImpact_NONE+=1
        
            
    elif(((float(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"][j])) < 9.0) and ((float(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"][j])) >=8.0)):
        cvssV2_IMPACT_score_8_iot+=1
           
        if(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.accessVector"][j]=='NETWORK'):
            cvssV2_IMPACT_score_8_iot_accessvector_NETWORK+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.accessVector"][j]=='LOCAL'):
            cvssV2_IMPACT_score_8_iot_accessvector_LOCAL+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.accessVector"][j]=='PHYSICAL'):
            cvssV2_IMPACT_score_8_iot_accessvector_PHYSICAL+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.accessVector"][j]=='ADJACENT_NETWORK'):
            cvssV2_IMPACT_score_8_iot_accessvector_ADJACENT_NETWORK+=1
            
        if(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.accessComplexity"][j]=='HIGH'):
            cvssV2_IMPACT_score_8_iot_accesscomplexity_HIGH+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.accessComplexity"][j]=='LOW'):
            cvssV2_IMPACT_score_8_iot_accesscomplexity_LOW+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.accessComplexity"][j]=='MEDIUM'):
            cvssV2_IMPACT_score_8_iot_accesscomplexity_MEDIUM+=1
        else:
            cvssV2_IMPACT_score_8_iot_accesscomplexity_NONE+=1  
                
        if(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.authentication"][j]=="SINGLE"):
            cvssV2_IMPACT_score_8_iot_authentication_SINGLE+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.authentication"][j]=="MULTIPLE"):
            cvssV2_IMPACT_score_8_iot_authentication_MULTIPLE+=1
        else:
            cvssV2_IMPACT_score_8_iot_authentication_NONE+=1
                
        if(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.confidentialityImpact"][j]=='COMPLETE'):
            cvssV2_IMPACT_score_8_iot_confidentialityImpact_COMPLETE+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.confidentialityImpact"][j]=='PARTIAL'):
            cvssV2_IMPACT_score_8_iot_confidentialityImpact_PARTIAL+=1
        else:
            cvssV2_IMPACT_score_8_iot_confidentialityImpact_NONE+=1 
            
            
        if(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.integrityImpact"][j]=='COMPLETE'):
            cvssV2_IMPACT_score_8_iot_integrityImpact_COMPLETE+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.integrityImpact"][j]=='PARTIAL'):
            cvssV2_IMPACT_score_8_iot_integrityImpact_PARTIAL+=1
        else:
            cvssV2_IMPACT_score_8_iot_integrityImpact_NONE+=1    
            
          
        if(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.availabilityImpact"][j]=='COMPLETE'):
            cvssV2_IMPACT_score_8_iot_availabilityImpact_COMPLETE+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.availabilityImpact"][j]=='PARTIAL'):
            cvssV2_IMPACT_score_8_iot_availabilityImpact_PARTIAL+=1
        else:
            cvssV2_IMPACT_score_8_iot_availabilityImpact_NONE+=1
           

            
    elif(((float(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"][j])) < 8.0) and ((float(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"][j])) >=7.0)):
        
        cvssV2_IMPACT_score_7_iot+=1
           
        if(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.accessVector"][j]=='NETWORK'):
            cvssV2_IMPACT_score_7_iot_accessvector_NETWORK+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.accessVector"][j]=='LOCAL'):
            cvssV2_IMPACT_score_7_iot_accessvector_LOCAL+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.accessVector"][j]=='PHYSICAL'):
            cvssV2_IMPACT_score_7_iot_accessvector_PHYSICAL+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.accessVector"][j]=='ADJACENT_NETWORK'):
            cvssV2_IMPACT_score_7_iot_accessvector_ADJACENT_NETWORK+=1
            
        if(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.accessComplexity"][j]=='HIGH'):
            cvssV2_IMPACT_score_7_iot_accesscomplexity_HIGH+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.accessComplexity"][j]=='LOW'):
            cvssV2_IMPACT_score_7_iot_accesscomplexity_LOW+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.accessComplexity"][j]=='MEDIUM'):
            cvssV2_IMPACT_score_7_iot_accesscomplexity_MEDIUM+=1
        else:
            cvssV2_IMPACT_score_7_iot_accesscomplexity_NONE+=1  
                
        if(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.authentication"][j]=="SINGLE"):
            cvssV2_IMPACT_score_7_iot_authentication_SINGLE+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.authentication"][j]=="MULTIPLE"):
            cvssV2_IMPACT_score_7_iot_authentication_MULTIPLE+=1
        else:
            cvssV2_IMPACT_score_7_iot_authentication_NONE+=1
                
        if(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.confidentialityImpact"][j]=='COMPLETE'):
            cvssV2_IMPACT_score_7_iot_confidentialityImpact_COMPLETE+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.confidentialityImpact"][j]=='PARTIAL'):
            cvssV2_IMPACT_score_7_iot_confidentialityImpact_PARTIAL+=1
        else:
            cvssV2_IMPACT_score_7_iot_confidentialityImpact_NONE+=1 
            
            
        if(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.integrityImpact"][j]=='COMPLETE'):
            cvssV2_IMPACT_score_7_iot_integrityImpact_COMPLETE+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.integrityImpact"][j]=='PARTIAL'):
            cvssV2_IMPACT_score_7_iot_integrityImpact_PARTIAL+=1
        else:
            cvssV2_IMPACT_score_7_iot_integrityImpact_NONE+=1    
            
          
        if(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.availabilityImpact"][j]=='COMPLETE'):
            cvssV2_IMPACT_score_7_iot_availabilityImpact_COMPLETE+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.availabilityImpact"][j]=='PARTIAL'):
            cvssV2_IMPACT_score_7_iot_availabilityImpact_PARTIAL+=1
        else:
            cvssV2_IMPACT_score_7_iot_availabilityImpact_NONE+=1   
        

    elif(((float(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"][j])) < 7.0) and ((float(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"][j])) >=6.0)):
        
        cvssV2_IMPACT_score_6_iot+=1
           
        if(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.accessVector"][j]=='NETWORK'):
            cvssV2_IMPACT_score_6_iot_accessvector_NETWORK+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.accessVector"][j]=='LOCAL'):
            cvssV2_IMPACT_score_6_iot_accessvector_LOCAL+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.accessVector"][j]=='PHYSICAL'):
            cvssV2_IMPACT_score_6_iot_accessvector_PHYSICAL+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.accessVector"][j]=='ADJACENT_NETWORK'):
            cvssV2_IMPACT_score_6_iot_accessvector_ADJACENT_NETWORK+=1
            
        if(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.accessComplexity"][j]=='HIGH'):
            cvssV2_IMPACT_score_6_iot_accesscomplexity_HIGH+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.accessComplexity"][j]=='LOW'):
            cvssV2_IMPACT_score_6_iot_accesscomplexity_LOW+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.accessComplexity"][j]=='MEDIUM'):
            cvssV2_IMPACT_score_6_iot_accesscomplexity_MEDIUM+=1
        else:
            cvssV2_IMPACT_score_6_iot_accesscomplexity_NONE+=1  
                
        if(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.authentication"][j]=="SINGLE"):
            cvssV2_IMPACT_score_6_iot_authentication_SINGLE+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.authentication"][j]=="MULTIPLE"):
            cvssV2_IMPACT_score_6_iot_authentication_MULTIPLE+=1
        else:
            cvssV2_IMPACT_score_6_iot_authentication_NONE+=1
                
        if(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.confidentialityImpact"][j]=='COMPLETE'):
            cvssV2_IMPACT_score_6_iot_confidentialityImpact_COMPLETE+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.confidentialityImpact"][j]=='PARTIAL'):
            cvssV2_IMPACT_score_6_iot_confidentialityImpact_PARTIAL+=1
        else:
            cvssV2_IMPACT_score_6_iot_confidentialityImpact_NONE+=1 
            
            
        if(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.integrityImpact"][j]=='COMPLETE'):
            cvssV2_IMPACT_score_6_iot_integrityImpact_COMPLETE+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.integrityImpact"][j]=='PARTIAL'):
            cvssV2_IMPACT_score_6_iot_integrityImpact_PARTIAL+=1
        else:
            cvssV2_IMPACT_score_6_iot_integrityImpact_NONE+=1    
            
          
        if(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.availabilityImpact"][j]=='COMPLETE'):
            cvssV2_IMPACT_score_6_iot_availabilityImpact_COMPLETE+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.availabilityImpact"][j]=='PARTIAL'):
            cvssV2_IMPACT_score_6_iot_availabilityImpact_PARTIAL+=1
        else:
            cvssV2_IMPACT_score_6_iot_availabilityImpact_NONE+=1  
            
            
            
    elif(((float(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"][j])) < 6.0) and ((float(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"][j])) >=5.0)):
        
        cvssV2_IMPACT_score_5_iot+=1
           
        if(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.accessVector"][j]=='NETWORK'):
            cvssV2_IMPACT_score_5_iot_accessvector_NETWORK+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.accessVector"][j]=='LOCAL'):
            cvssV2_IMPACT_score_5_iot_accessvector_LOCAL+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.accessVector"][j]=='PHYSICAL'):
            cvssV2_IMPACT_score_5_iot_accessvector_PHYSICAL+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.accessVector"][j]=='ADJACENT_NETWORK'):
            cvssV2_IMPACT_score_5_iot_accessvector_ADJACENT_NETWORK+=1
            
        if(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.accessComplexity"][j]=='HIGH'):
            cvssV2_IMPACT_score_5_iot_accesscomplexity_HIGH+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.accessComplexity"][j]=='LOW'):
            cvssV2_IMPACT_score_5_iot_accesscomplexity_LOW+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.accessComplexity"][j]=='MEDIUM'):
            cvssV2_IMPACT_score_5_iot_accesscomplexity_MEDIUM+=1
        else:
            cvssV2_IMPACT_score_5_iot_accesscomplexity_NONE+=1  
                
        if(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.authentication"][j]=="SINGLE"):
            cvssV2_IMPACT_score_5_iot_authentication_SINGLE+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.authentication"][j]=="MULTIPLE"):
            cvssV2_IMPACT_score_5_iot_authentication_MULTIPLE+=1
        else:
            cvssV2_IMPACT_score_5_iot_authentication_NONE+=1
                
        if(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.confidentialityImpact"][j]=='COMPLETE'):
            cvssV2_IMPACT_score_5_iot_confidentialityImpact_COMPLETE+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.confidentialityImpact"][j]=='PARTIAL'):
            cvssV2_IMPACT_score_5_iot_confidentialityImpact_PARTIAL+=1
        else:
            cvssV2_IMPACT_score_5_iot_confidentialityImpact_NONE+=1 
            
            
        if(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.integrityImpact"][j]=='COMPLETE'):
            cvssV2_IMPACT_score_5_iot_integrityImpact_COMPLETE+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.integrityImpact"][j]=='PARTIAL'):
            cvssV2_IMPACT_score_5_iot_integrityImpact_PARTIAL+=1
        else:
            cvssV2_IMPACT_score_5_iot_integrityImpact_NONE+=1    
            
          
        if(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.availabilityImpact"][j]=='COMPLETE'):
            cvssV2_IMPACT_score_5_iot_availabilityImpact_COMPLETE+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.availabilityImpact"][j]=='PARTIAL'):
            cvssV2_IMPACT_score_5_iot_availabilityImpact_PARTIAL+=1
        else:
            cvssV2_IMPACT_score_5_iot_availabilityImpact_NONE+=1

    elif(((float(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"][j])) < 5.0) and ((float(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"][j])) >=4.0)):
        cvssV2_IMPACT_score_4_iot+=1
           
        if(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.accessVector"][j]=='NETWORK'):
            cvssV2_IMPACT_score_4_iot_accessvector_NETWORK+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.accessVector"][j]=='LOCAL'):
            cvssV2_IMPACT_score_4_iot_accessvector_LOCAL+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.accessVector"][j]=='PHYSICAL'):
            cvssV2_IMPACT_score_4_iot_accessvector_PHYSICAL+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.accessVector"][j]=='ADJACENT_NETWORK'):
            cvssV2_IMPACT_score_4_iot_accessvector_ADJACENT_NETWORK+=1
            
        if(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.accessComplexity"][j]=='HIGH'):
            cvssV2_IMPACT_score_4_iot_accesscomplexity_HIGH+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.accessComplexity"][j]=='LOW'):
            cvssV2_IMPACT_score_4_iot_accesscomplexity_LOW+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.accessComplexity"][j]=='MEDIUM'):
            cvssV2_IMPACT_score_4_iot_accesscomplexity_MEDIUM+=1
        else:
            cvssV2_IMPACT_score_4_iot_accesscomplexity_NONE+=1  
                
        if(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.authentication"][j]=="SINGLE"):
            cvssV2_IMPACT_score_4_iot_authentication_SINGLE+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.authentication"][j]=="MULTIPLE"):
            cvssV2_IMPACT_score_4_iot_authentication_MULTIPLE+=1
        else:
            cvssV2_IMPACT_score_4_iot_authentication_NONE+=1
                
        if(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.confidentialityImpact"][j]=='COMPLETE'):
            cvssV2_IMPACT_score_4_iot_confidentialityImpact_COMPLETE+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.confidentialityImpact"][j]=='PARTIAL'):
            cvssV2_IMPACT_score_4_iot_confidentialityImpact_PARTIAL+=1
        else:
            cvssV2_IMPACT_score_4_iot_confidentialityImpact_NONE+=1 
            
            
        if(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.integrityImpact"][j]=='COMPLETE'):
            cvssV2_IMPACT_score_4_iot_integrityImpact_COMPLETE+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.integrityImpact"][j]=='PARTIAL'):
            cvssV2_IMPACT_score_4_iot_integrityImpact_PARTIAL+=1
        else:
            cvssV2_IMPACT_score_4_iot_integrityImpact_NONE+=1    
            
          
        if(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.availabilityImpact"][j]=='COMPLETE'):
            cvssV2_IMPACT_score_4_iot_availabilityImpact_COMPLETE+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.availabilityImpact"][j]=='PARTIAL'):
            cvssV2_IMPACT_score_4_iot_availabilityImpact_PARTIAL+=1
        else:
            cvssV2_IMPACT_score_4_iot_availabilityImpact_NONE+=1

    elif(((float(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"][j])) < 4.0) and ((float(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"][j])) >=3.0)):
        cvssV2_IMPACT_score_3_iot+=1
           
        if(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.accessVector"][j]=='NETWORK'):
            cvssV2_IMPACT_score_3_iot_accessvector_NETWORK+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.accessVector"][j]=='LOCAL'):
            cvssV2_IMPACT_score_3_iot_accessvector_LOCAL+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.accessVector"][j]=='PHYSICAL'):
            cvssV2_IMPACT_score_3_iot_accessvector_PHYSICAL+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.accessVector"][j]=='ADJACENT_NETWORK'):
            cvssV2_IMPACT_score_3_iot_accessvector_ADJACENT_NETWORK+=1
            
        if(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.accessComplexity"][j]=='HIGH'):
            cvssV2_IMPACT_score_3_iot_accesscomplexity_HIGH+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.accessComplexity"][j]=='LOW'):
            cvssV2_IMPACT_score_3_iot_accesscomplexity_LOW+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.accessComplexity"][j]=='MEDIUM'):
            cvssV2_IMPACT_score_3_iot_accesscomplexity_MEDIUM+=1
        else:
            cvssV2_IMPACT_score_3_iot_accesscomplexity_NONE+=1  
                
        if(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.authentication"][j]=="SINGLE"):
            cvssV2_IMPACT_score_3_iot_authentication_SINGLE+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.authentication"][j]=="MULTIPLE"):
            cvssV2_IMPACT_score_3_iot_authentication_MULTIPLE+=1
        else:
            cvssV2_IMPACT_score_3_iot_authentication_NONE+=1
                
        if(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.confidentialityImpact"][j]=='COMPLETE'):
            cvssV2_IMPACT_score_3_iot_confidentialityImpact_COMPLETE+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.confidentialityImpact"][j]=='PARTIAL'):
            cvssV2_IMPACT_score_3_iot_confidentialityImpact_PARTIAL+=1
        else:
            cvssV2_IMPACT_score_3_iot_confidentialityImpact_NONE+=1 
            
            
        if(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.integrityImpact"][j]=='COMPLETE'):
            cvssV2_IMPACT_score_3_iot_integrityImpact_COMPLETE+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.integrityImpact"][j]=='PARTIAL'):
            cvssV2_IMPACT_score_3_iot_integrityImpact_PARTIAL+=1
        else:
            cvssV2_IMPACT_score_3_iot_integrityImpact_NONE+=1    
            
          
        if(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.availabilityImpact"][j]=='COMPLETE'):
            cvssV2_IMPACT_score_3_iot_availabilityImpact_COMPLETE+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.availabilityImpact"][j]=='PARTIAL'):
            cvssV2_IMPACT_score_3_iot_availabilityImpact_PARTIAL+=1
        else:
            cvssV2_IMPACT_score_3_iot_availabilityImpact_NONE+=1

            
    elif(((float(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"][j])) < 3.0) and ((float(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"][j])) >=2.0)):
        
        cvssV2_IMPACT_score_2_iot+=1
           
        if(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.accessVector"][j]=='NETWORK'):
            cvssV2_IMPACT_score_2_iot_accessvector_NETWORK+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.accessVector"][j]=='LOCAL'):
            cvssV2_IMPACT_score_2_iot_accessvector_LOCAL+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.accessVector"][j]=='PHYSICAL'):
            cvssV2_IMPACT_score_2_iot_accessvector_PHYSICAL+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.accessVector"][j]=='ADJACENT_NETWORK'):
            cvssV2_IMPACT_score_2_iot_accessvector_ADJACENT_NETWORK+=1
            
        if(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.accessComplexity"][j]=='HIGH'):
            cvssV2_IMPACT_score_2_iot_accesscomplexity_HIGH+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.accessComplexity"][j]=='LOW'):
            cvssV2_IMPACT_score_2_iot_accesscomplexity_LOW+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.accessComplexity"][j]=='MEDIUM'):
            cvssV2_IMPACT_score_2_iot_accesscomplexity_MEDIUM+=1
        else:
            cvssV2_IMPACT_score_2_iot_accesscomplexity_NONE+=1  
                
        if(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.authentication"][j]=="SINGLE"):
            cvssV2_IMPACT_score_2_iot_authentication_SINGLE+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.authentication"][j]=="MULTIPLE"):
            cvssV2_IMPACT_score_2_iot_authentication_MULTIPLE+=1
        else:
            cvssV2_IMPACT_score_2_iot_authentication_NONE+=1
                
        if(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.confidentialityImpact"][j]=='COMPLETE'):
            cvssV2_IMPACT_score_2_iot_confidentialityImpact_COMPLETE+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.confidentialityImpact"][j]=='PARTIAL'):
            cvssV2_IMPACT_score_2_iot_confidentialityImpact_PARTIAL+=1
        else:
            cvssV2_IMPACT_score_2_iot_confidentialityImpact_NONE+=1 
            
            
        if(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.integrityImpact"][j]=='COMPLETE'):
            cvssV2_IMPACT_score_2_iot_integrityImpact_COMPLETE+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.integrityImpact"][j]=='PARTIAL'):
            cvssV2_IMPACT_score_2_iot_integrityImpact_PARTIAL+=1
        else:
            cvssV2_IMPACT_score_2_iot_integrityImpact_NONE+=1    
            
          
        if(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.availabilityImpact"][j]=='COMPLETE'):
            cvssV2_IMPACT_score_2_iot_availabilityImpact_COMPLETE+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.availabilityImpact"][j]=='PARTIAL'):
            cvssV2_IMPACT_score_2_iot_availabilityImpact_PARTIAL+=1
        else:
            cvssV2_IMPACT_score_2_iot_availabilityImpact_NONE+=1

            
    elif(((float(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"][j])) < 2.0) and ((float(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"][j])) >=1.0)):
        cvssV2_IMPACT_score_1_iot+=1
           
        if(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.accessVector"][j]=='NETWORK'):
            cvssV2_IMPACT_score_1_iot_accessvector_NETWORK+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.accessVector"][j]=='LOCAL'):
            cvssV2_IMPACT_score_1_iot_accessvector_LOCAL+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.accessVector"][j]=='PHYSICAL'):
            cvssV2_IMPACT_score_1_iot_accessvector_PHYSICAL+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.accessVector"][j]=='ADJACENT_NETWORK'):
            cvssV2_IMPACT_score_1_iot_accessvector_ADJACENT_NETWORK+=1
            
        if(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.accessComplexity"][j]=='HIGH'):
            cvssV2_IMPACT_score_1_iot_accesscomplexity_HIGH+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.accessComplexity"][j]=='LOW'):
            cvssV2_IMPACT_score_1_iot_accesscomplexity_LOW+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.accessComplexity"][j]=='MEDIUM'):
            cvssV2_IMPACT_score_1_iot_accesscomplexity_MEDIUM+=1
        else:
            cvssV2_IMPACT_score_1_iot_accesscomplexity_NONE+=1  
                
        if(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.authentication"][j]=="SINGLE"):
            cvssV2_IMPACT_score_1_iot_authentication_SINGLE+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.authentication"][j]=="MULTIPLE"):
            cvssV2_IMPACT_score_1_iot_authentication_MULTIPLE+=1
        else:
            cvssV2_IMPACT_score_1_iot_authentication_NONE+=1
                
        if(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.confidentialityImpact"][j]=='COMPLETE'):
            cvssV2_IMPACT_score_1_iot_confidentialityImpact_COMPLETE+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.confidentialityImpact"][j]=='PARTIAL'):
            cvssV2_IMPACT_score_1_iot_confidentialityImpact_PARTIAL+=1
        else:
            cvssV2_IMPACT_score_1_iot_confidentialityImpact_NONE+=1 
            
            
        if(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.integrityImpact"][j]=='COMPLETE'):
            cvssV2_IMPACT_score_1_iot_integrityImpact_COMPLETE+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.integrityImpact"][j]=='PARTIAL'):
            cvssV2_IMPACT_score_1_iot_integrityImpact_PARTIAL+=1
        else:
            cvssV2_IMPACT_score_1_iot_integrityImpact_NONE+=1    
            
          
        if(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.availabilityImpact"][j]=='COMPLETE'):
            cvssV2_IMPACT_score_1_iot_availabilityImpact_COMPLETE+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.availabilityImpact"][j]=='PARTIAL'):
            cvssV2_IMPACT_score_1_iot_availabilityImpact_PARTIAL+=1
        else:
            cvssV2_IMPACT_score_1_iot_availabilityImpact_NONE+=1
    elif(((float(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"][j])) < 1.0) and ((float(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"][j])) >=0.0)):
        cvssV2_IMPACT_score_0_iot+=1
           
        if(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.accessVector"][j]=='NETWORK'):
            cvssV2_IMPACT_score_0_iot_accessvector_NETWORK+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.accessVector"][j]=='LOCAL'):
            cvssV2_IMPACT_score_0_iot_accessvector_LOCAL+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.accessVector"][j]=='PHYSICAL'):
            cvssV2_IMPACT_score_0_iot_accessvector_PHYSICAL+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.accessVector"][j]=='ADJACENT_NETWORK'):
            cvssV2_IMPACT_score_0_iot_accessvector_ADJACENT_NETWORK+=1
            
        if(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.accessComplexity"][j]=='HIGH'):
            cvssV2_IMPACT_score_0_iot_accesscomplexity_HIGH+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.accessComplexity"][j]=='LOW'):
            cvssV2_IMPACT_score_0_iot_accesscomplexity_LOW+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.accessComplexity"][j]=='MEDIUM'):
            cvssV2_IMPACT_score_0_iot_accesscomplexity_MEDIUM+=1
        else:
            cvssV2_IMPACT_score_0_iot_accesscomplexity_NONE+=1  
                
        if(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.authentication"][j]=="SINGLE"):
            cvssV2_IMPACT_score_0_iot_authentication_SINGLE+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.authentication"][j]=="MULTIPLE"):
            cvssV2_IMPACT_score_0_iot_authentication_MULTIPLE+=1
        else:
            cvssV2_IMPACT_score_0_iot_authentication_NONE+=1
                
        if(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.confidentialityImpact"][j]=='COMPLETE'):
            cvssV2_IMPACT_score_0_iot_confidentialityImpact_COMPLETE+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.confidentialityImpact"][j]=='PARTIAL'):
            cvssV2_IMPACT_score_0_iot_confidentialityImpact_PARTIAL+=1
        else:
            cvssV2_IMPACT_score_0_iot_confidentialityImpact_NONE+=1 
            
            
        if(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.integrityImpact"][j]=='COMPLETE'):
            cvssV2_IMPACT_score_0_iot_integrityImpact_COMPLETE+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.integrityImpact"][j]=='PARTIAL'):
            cvssV2_IMPACT_score_0_iot_integrityImpact_PARTIAL+=1
        else:
            cvssV2_IMPACT_score_0_iot_integrityImpact_NONE+=1    
            
          
        if(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.availabilityImpact"][j]=='COMPLETE'):
            cvssV2_IMPACT_score_0_iot_availabilityImpact_COMPLETE+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.availabilityImpact"][j]=='PARTIAL'):
            cvssV2_IMPACT_score_0_iot_availabilityImpact_PARTIAL+=1
        else:
            cvssV2_IMPACT_score_0_iot_availabilityImpact_NONE+=1

    elif(((float(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"][j])) == 10.0)):
        cvssV2_IMPACT_score_10_iot+=1
           
        if(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.accessVector"][j]=='NETWORK'):
            cvssV2_IMPACT_score_10_iot_accessvector_NETWORK+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.accessVector"][j]=='LOCAL'):
            cvssV2_IMPACT_score_10_iot_accessvector_LOCAL+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.accessVector"][j]=='PHYSICAL'):
            cvssV2_IMPACT_score_10_iot_accessvector_PHYSICAL+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.accessVector"][j]=='ADJACENT_NETWORK'):
            cvssV2_IMPACT_score_10_iot_accessvector_ADJACENT_NETWORK+=1
            
        if(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.accessComplexity"][j]=='HIGH'):
            cvssV2_IMPACT_score_10_iot_accesscomplexity_HIGH+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.accessComplexity"][j]=='LOW'):
            cvssV2_IMPACT_score_10_iot_accesscomplexity_LOW+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.accessComplexity"][j]=='MEDIUM'):
            cvssV2_IMPACT_score_10_iot_accesscomplexity_MEDIUM+=1
        else:
            cvssV2_IMPACT_score_10_iot_accesscomplexity_NONE+=1  
                
        if(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.authentication"][j]=="SINGLE"):
            cvssV2_IMPACT_score_10_iot_authentication_SINGLE+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.authentication"][j]=="MULTIPLE"):
            cvssV2_IMPACT_score_10_iot_authentication_MULTIPLE+=1
        else:
            cvssV2_IMPACT_score_10_iot_authentication_NONE+=1
                
        if(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.confidentialityImpact"][j]=='COMPLETE'):
            cvssV2_IMPACT_score_10_iot_confidentialityImpact_COMPLETE+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.confidentialityImpact"][j]=='PARTIAL'):
            cvssV2_IMPACT_score_10_iot_confidentialityImpact_PARTIAL+=1
        else:
            cvssV2_IMPACT_score_10_iot_confidentialityImpact_NONE+=1 
            
            
        if(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.integrityImpact"][j]=='COMPLETE'):
            cvssV2_IMPACT_score_10_iot_integrityImpact_COMPLETE+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.integrityImpact"][j]=='PARTIAL'):
            cvssV2_IMPACT_score_10_iot_integrityImpact_PARTIAL+=1
        else:
            cvssV2_IMPACT_score_10_iot_integrityImpact_NONE+=1    
            
          
        if(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.availabilityImpact"][j]=='COMPLETE'):
            cvssV2_IMPACT_score_10_iot_availabilityImpact_COMPLETE+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.availabilityImpact"][j]=='PARTIAL'):
            cvssV2_IMPACT_score_10_iot_availabilityImpact_PARTIAL+=1
        else:
            cvssV2_IMPACT_score_10_iot_availabilityImpact_NONE+=1
            
            
            
print("________________________ ESTADÍSTICAS RELACION ELEMENTOS VECTOR STRING-PUNTUACION DE IMPACTO CVSSV2 PARTE IOT________________________")
print("\n")        
            
            
    
print("\n")
print(" DE UN TOTAL DE "+str(len(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.availabilityImpact"]))+" VULNERABILIDADES , LAS ESTADISTICAS DE ELEMENTOS DE VECTOR STRING SEGUN PUNTUACION DE IMPACTO SON LAS SIGUIENTES:  \n")
print("\n")
print("      -    EN  "+str(cvssV2_IMPACT_score_10_iot)+" VULNERABILIDADES LA PUNTUACION DE IMPACTO ES 10. LAS ESTADÍSTICAS DEL VECTOR STRING SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_10_iot_accessvector_NETWORK)+" VULNERABILIDADES EL VECTOR DE ACCESO ES NETWORK ")
print("            -    EN  "+str(cvssV2_IMPACT_score_10_iot_accessvector_LOCAL)+" VULNERABILIDADES EL VECTOR DE ACCESO ES LOCAL ")
print("            -    EN  "+str(cvssV2_IMPACT_score_10_iot_accessvector_PHYSICAL)+" VULNERABILIDADES EL VECTOR DE ACCESO ES PHYSICAL ")
print("            -    EN  "+str(cvssV2_IMPACT_score_10_iot_accessvector_ADJACENT_NETWORK)+" VULNERABILIDADES EL VECTOR DE ACCESO ES ADJACENT_NETWORK ")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_10_iot_accesscomplexity_HIGH)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES ALTA ")
print("            -    EN  "+str(cvssV2_IMPACT_score_10_iot_accesscomplexity_LOW)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES BAJA ")
print("            -    EN  "+str(cvssV2_IMPACT_score_10_iot_accesscomplexity_MEDIUM)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES MEDIA ")
print("            -    EN  "+str(cvssV2_IMPACT_score_10_iot_accesscomplexity_NONE)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO NO VIENE ESPECIFICADA ")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_10_iot_authentication_SINGLE)+" VULNERABILIDADES SE REQUIERE AUTENTICACIÓN SENCILLA ")
print("            -    EN  "+str(cvssV2_IMPACT_score_10_iot_authentication_MULTIPLE)+" VULNERABILIDADES SE REQUIERE AUTENTICACIÓN MULTIPLE")
print("            -    EN  "+str(cvssV2_IMPACT_score_10_iot_authentication_NONE)+" VULNERABILIDADES NO SE REQUIERE AUTENTICACIÓN")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_10_iot_confidentialityImpact_COMPLETE)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES COMPLETO ")
print("            -    EN  "+str(cvssV2_IMPACT_score_10_iot_confidentialityImpact_PARTIAL)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES PARCIAL" )
print("            -    EN  "+str(cvssV2_IMPACT_score_10_iot_confidentialityImpact_NONE)+" VULNERABILIDADES NO EXISTE IMPACTO DE CONFIDENCIALIDAD ")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_10_iot_integrityImpact_COMPLETE)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES COMPLETO ")
print("            -    EN  "+str(cvssV2_IMPACT_score_10_iot_integrityImpact_PARTIAL)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES PARCIAL" )
print("            -    EN  "+str(cvssV2_IMPACT_score_10_iot_integrityImpact_NONE)+" VULNERABILIDADES NO EXISTE IMPACTO DE INTEGRIDAD ")
print("\n")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_10_iot_availabilityImpact_COMPLETE)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES COMPLETO ")
print("            -    EN  "+str(cvssV2_IMPACT_score_10_iot_availabilityImpact_PARTIAL)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES PARCIAL" )
print("            -    EN  "+str(cvssV2_IMPACT_score_10_iot_availabilityImpact_NONE)+" VULNERABILIDADES NO EXISTE IMPACTO DE DISPONIBILIDAD ")
print("\n")
print("\n")
print("      -    EN  "+str(cvssV2_IMPACT_score_9_iot)+" VULNERABILIDADES LA PUNTUACION DE IMPACTO ESTÁ ENTRE 9 Y 10. LAS ESTADÍSTICAS DEL VECTOR STRING SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_9_iot_accessvector_NETWORK)+" VULNERABILIDADES EL VECTOR DE ACCESO ES NETWORK ")
print("            -    EN  "+str(cvssV2_IMPACT_score_9_iot_accessvector_LOCAL)+" VULNERABILIDADES EL VECTOR DE ACCESO ES LOCAL ")
print("            -    EN  "+str(cvssV2_IMPACT_score_9_iot_accessvector_PHYSICAL)+" VULNERABILIDADES EL VECTOR DE ACCESO ES PHYSICAL ")
print("            -    EN  "+str(cvssV2_IMPACT_score_9_iot_accessvector_ADJACENT_NETWORK)+" VULNERABILIDADES EL VECTOR DE ACCESO ES ADJACENT_NETWORK ")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_9_iot_accesscomplexity_HIGH)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES ALTA ")
print("            -    EN  "+str(cvssV2_IMPACT_score_9_iot_accesscomplexity_LOW)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES BAJA ")
print("            -    EN  "+str(cvssV2_IMPACT_score_9_iot_accesscomplexity_MEDIUM)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES MEDIA ")
print("            -    EN  "+str(cvssV2_IMPACT_score_9_iot_accesscomplexity_NONE)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO NO VIENE ESPECIFICADA ")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_9_iot_authentication_SINGLE)+" VULNERABILIDADES SE REQUIERE AUTENTICACIÓN SENCILLA ")
print("            -    EN  "+str(cvssV2_IMPACT_score_9_iot_authentication_MULTIPLE)+" VULNERABILIDADES SE REQUIERE AUTENTICACIÓN MULTIPLE")
print("            -    EN  "+str(cvssV2_IMPACT_score_9_iot_authentication_NONE)+" VULNERABILIDADES NO SE REQUIERE AUTENTICACIÓN")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_9_iot_confidentialityImpact_COMPLETE)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES COMPLETO ")
print("            -    EN  "+str(cvssV2_IMPACT_score_9_iot_confidentialityImpact_PARTIAL)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES PARCIAL" )
print("            -    EN  "+str(cvssV2_IMPACT_score_9_iot_confidentialityImpact_NONE)+" VULNERABILIDADES NO EXISTE IMPACTO DE CONFIDENCIALIDAD ")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_9_iot_integrityImpact_COMPLETE)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES COMPLETO ")
print("            -    EN  "+str(cvssV2_IMPACT_score_9_iot_integrityImpact_PARTIAL)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES PARCIAL" )
print("            -    EN  "+str(cvssV2_IMPACT_score_9_iot_integrityImpact_NONE)+" VULNERABILIDADES NO EXISTE IMPACTO DE INTEGRIDAD ")
print("\n")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_9_iot_availabilityImpact_COMPLETE)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES COMPLETO ")
print("            -    EN  "+str(cvssV2_IMPACT_score_9_iot_availabilityImpact_PARTIAL)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES PARCIAL" )
print("            -    EN  "+str(cvssV2_IMPACT_score_9_iot_availabilityImpact_NONE)+" VULNERABILIDADES NO EXISTE IMPACTO DE DISPONIBILIDAD ")
print("\n")
print("\n")
print("\n")
print("      -    EN  "+str(cvssV2_IMPACT_score_8_iot)+" VULNERABILIDADES LA PUNTUACION DE IMPACTO ESTÁ ENTRE 8 Y 9. LAS ESTADÍSTICAS DEL VECTOR STRING SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_8_iot_accessvector_NETWORK)+" VULNERABILIDADES EL VECTOR DE ACCESO ES NETWORK ")
print("            -    EN  "+str(cvssV2_IMPACT_score_8_iot_accessvector_LOCAL)+" VULNERABILIDADES EL VECTOR DE ACCESO ES LOCAL ")
print("            -    EN  "+str(cvssV2_IMPACT_score_8_iot_accessvector_PHYSICAL)+" VULNERABILIDADES EL VECTOR DE ACCESO ES PHYSICAL ")
print("            -    EN  "+str(cvssV2_IMPACT_score_8_iot_accessvector_ADJACENT_NETWORK)+" VULNERABILIDADES EL VECTOR DE ACCESO ES ADJACENT_NETWORK ")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_8_iot_accesscomplexity_HIGH)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES ALTA ")
print("            -    EN  "+str(cvssV2_IMPACT_score_8_iot_accesscomplexity_LOW)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES BAJA ")
print("            -    EN  "+str(cvssV2_IMPACT_score_8_iot_accesscomplexity_MEDIUM)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES MEDIA ")
print("            -    EN  "+str(cvssV2_IMPACT_score_8_iot_accesscomplexity_NONE)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO NO VIENE ESPECIFICADA ")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_8_iot_authentication_SINGLE)+" VULNERABILIDADES SE REQUIERE AUTENTICACIÓN SENCILLA ")
print("            -    EN  "+str(cvssV2_IMPACT_score_8_iot_authentication_MULTIPLE)+" VULNERABILIDADES SE REQUIERE AUTENTICACIÓN MULTIPLE")
print("            -    EN  "+str(cvssV2_IMPACT_score_8_iot_authentication_NONE)+" VULNERABILIDADES NO SE REQUIERE AUTENTICACIÓN")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_8_iot_confidentialityImpact_COMPLETE)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES COMPLETO ")
print("            -    EN  "+str(cvssV2_IMPACT_score_8_iot_confidentialityImpact_PARTIAL)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES PARCIAL" )
print("            -    EN  "+str(cvssV2_IMPACT_score_8_iot_confidentialityImpact_NONE)+" VULNERABILIDADES NO EXISTE IMPACTO DE CONFIDENCIALIDAD ")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_8_iot_integrityImpact_COMPLETE)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES COMPLETO ")
print("            -    EN  "+str(cvssV2_IMPACT_score_8_iot_integrityImpact_PARTIAL)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES PARCIAL" )
print("            -    EN  "+str(cvssV2_IMPACT_score_8_iot_integrityImpact_NONE)+" VULNERABILIDADES NO EXISTE IMPACTO DE INTEGRIDAD ")
print("\n")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_8_iot_availabilityImpact_COMPLETE)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES COMPLETO ")
print("            -    EN  "+str(cvssV2_IMPACT_score_8_iot_availabilityImpact_PARTIAL)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES PARCIAL" )
print("            -    EN  "+str(cvssV2_IMPACT_score_8_iot_availabilityImpact_NONE)+" VULNERABILIDADES NO EXISTE IMPACTO DE DISPONIBILIDAD ")
print("\n")
print("\n")
print("\n")
print("      -    EN  "+str(cvssV2_IMPACT_score_7_iot)+" VULNERABILIDADES LA PUNTUACION DE IMPACTO ESTÁ ENTRE 7 Y 8. LAS ESTADÍSTICAS DEL VECTOR STRING SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_7_iot_accessvector_NETWORK)+" VULNERABILIDADES EL VECTOR DE ACCESO ES NETWORK ")
print("            -    EN  "+str(cvssV2_IMPACT_score_7_iot_accessvector_LOCAL)+" VULNERABILIDADES EL VECTOR DE ACCESO ES LOCAL ")
print("            -    EN  "+str(cvssV2_IMPACT_score_7_iot_accessvector_PHYSICAL)+" VULNERABILIDADES EL VECTOR DE ACCESO ES PHYSICAL ")
print("            -    EN  "+str(cvssV2_IMPACT_score_7_iot_accessvector_ADJACENT_NETWORK)+" VULNERABILIDADES EL VECTOR DE ACCESO ES ADJACENT_NETWORK ")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_7_iot_accesscomplexity_HIGH)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES ALTA ")
print("            -    EN  "+str(cvssV2_IMPACT_score_7_iot_accesscomplexity_LOW)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES BAJA ")
print("            -    EN  "+str(cvssV2_IMPACT_score_7_iot_accesscomplexity_MEDIUM)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES MEDIA ")
print("            -    EN  "+str(cvssV2_IMPACT_score_7_iot_accesscomplexity_NONE)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO NO VIENE ESPECIFICADA ")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_7_iot_authentication_SINGLE)+" VULNERABILIDADES SE REQUIERE AUTENTICACIÓN SENCILLA ")
print("            -    EN  "+str(cvssV2_IMPACT_score_7_iot_authentication_MULTIPLE)+" VULNERABILIDADES SE REQUIERE AUTENTICACIÓN MULTIPLE")
print("            -    EN  "+str(cvssV2_IMPACT_score_7_iot_authentication_NONE)+" VULNERABILIDADES NO SE REQUIERE AUTENTICACIÓN")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_7_iot_confidentialityImpact_COMPLETE)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES COMPLETO ")
print("            -    EN  "+str(cvssV2_IMPACT_score_7_iot_confidentialityImpact_PARTIAL)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES PARCIAL" )
print("            -    EN  "+str(cvssV2_IMPACT_score_7_iot_confidentialityImpact_NONE)+" VULNERABILIDADES NO EXISTE IMPACTO DE CONFIDENCIALIDAD ")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_7_iot_integrityImpact_COMPLETE)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES COMPLETO ")
print("            -    EN  "+str(cvssV2_IMPACT_score_7_iot_integrityImpact_PARTIAL)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES PARCIAL" )
print("            -    EN  "+str(cvssV2_IMPACT_score_7_iot_integrityImpact_NONE)+" VULNERABILIDADES NO EXISTE IMPACTO DE INTEGRIDAD ")
print("\n")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_7_iot_availabilityImpact_COMPLETE)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES COMPLETO ")
print("            -    EN  "+str(cvssV2_IMPACT_score_7_iot_availabilityImpact_PARTIAL)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES PARCIAL" )
print("            -    EN  "+str(cvssV2_IMPACT_score_7_iot_availabilityImpact_NONE)+" VULNERABILIDADES NO EXISTE IMPACTO DE DISPONIBILIDAD ")
print("\n")
print("\n")
print("      -    EN  "+str(cvssV2_IMPACT_score_6_iot)+" VULNERABILIDADES LA PUNTUACION DE IMPACTO ESTÁ ENTRE 6 Y 7. LAS ESTADÍSTICAS DEL VECTOR STRING SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_6_iot_accessvector_NETWORK)+" VULNERABILIDADES EL VECTOR DE ACCESO ES NETWORK ")
print("            -    EN  "+str(cvssV2_IMPACT_score_6_iot_accessvector_LOCAL)+" VULNERABILIDADES EL VECTOR DE ACCESO ES LOCAL ")
print("            -    EN  "+str(cvssV2_IMPACT_score_6_iot_accessvector_PHYSICAL)+" VULNERABILIDADES EL VECTOR DE ACCESO ES PHYSICAL ")
print("            -    EN  "+str(cvssV2_IMPACT_score_6_iot_accessvector_ADJACENT_NETWORK)+" VULNERABILIDADES EL VECTOR DE ACCESO ES ADJACENT_NETWORK ")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_6_iot_accesscomplexity_HIGH)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES ALTA ")
print("            -    EN  "+str(cvssV2_IMPACT_score_6_iot_accesscomplexity_LOW)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES BAJA ")
print("            -    EN  "+str(cvssV2_IMPACT_score_6_iot_accesscomplexity_MEDIUM)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES MEDIA ")
print("            -    EN  "+str(cvssV2_IMPACT_score_6_iot_accesscomplexity_NONE)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO NO VIENE ESPECIFICADA ")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_6_iot_authentication_SINGLE)+" VULNERABILIDADES SE REQUIERE AUTENTICACIÓN SENCILLA ")
print("            -    EN  "+str(cvssV2_IMPACT_score_6_iot_authentication_MULTIPLE)+" VULNERABILIDADES SE REQUIERE AUTENTICACIÓN MULTIPLE")
print("            -    EN  "+str(cvssV2_IMPACT_score_6_iot_authentication_NONE)+" VULNERABILIDADES NO SE REQUIERE AUTENTICACIÓN")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_6_iot_confidentialityImpact_COMPLETE)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES COMPLETO ")
print("            -    EN  "+str(cvssV2_IMPACT_score_6_iot_confidentialityImpact_PARTIAL)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES PARCIAL" )
print("            -    EN  "+str(cvssV2_IMPACT_score_6_iot_confidentialityImpact_NONE)+" VULNERABILIDADES NO EXISTE IMPACTO DE CONFIDENCIALIDAD ")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_6_iot_integrityImpact_COMPLETE)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES COMPLETO ")
print("            -    EN  "+str(cvssV2_IMPACT_score_6_iot_integrityImpact_PARTIAL)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES PARCIAL" )
print("            -    EN  "+str(cvssV2_IMPACT_score_6_iot_integrityImpact_NONE)+" VULNERABILIDADES NO EXISTE IMPACTO DE INTEGRIDAD ")
print("\n")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_6_iot_availabilityImpact_COMPLETE)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES COMPLETO ")
print("            -    EN  "+str(cvssV2_IMPACT_score_6_iot_availabilityImpact_PARTIAL)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES PARCIAL" )
print("            -    EN  "+str(cvssV2_IMPACT_score_6_iot_availabilityImpact_NONE)+" VULNERABILIDADES NO EXISTE IMPACTO DE DISPONIBILIDAD ")
print("\n")
print("\n")
print("      -    EN  "+str(cvssV2_IMPACT_score_5_iot)+" VULNERABILIDADES LA PUNTUACION DE IMPACTO ESTÁ ENTRE 5 Y 6. LAS ESTADÍSTICAS DEL VECTOR STRING SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_5_iot_accessvector_NETWORK)+" VULNERABILIDADES EL VECTOR DE ACCESO ES NETWORK ")
print("            -    EN  "+str(cvssV2_IMPACT_score_5_iot_accessvector_LOCAL)+" VULNERABILIDADES EL VECTOR DE ACCESO ES LOCAL ")
print("            -    EN  "+str(cvssV2_IMPACT_score_5_iot_accessvector_PHYSICAL)+" VULNERABILIDADES EL VECTOR DE ACCESO ES PHYSICAL ")
print("            -    EN  "+str(cvssV2_IMPACT_score_5_iot_accessvector_ADJACENT_NETWORK)+" VULNERABILIDADES EL VECTOR DE ACCESO ES ADJACENT_NETWORK ")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_5_iot_accesscomplexity_HIGH)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES ALTA ")
print("            -    EN  "+str(cvssV2_IMPACT_score_5_iot_accesscomplexity_LOW)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES BAJA ")
print("            -    EN  "+str(cvssV2_IMPACT_score_5_iot_accesscomplexity_MEDIUM)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES MEDIA ")
print("            -    EN  "+str(cvssV2_IMPACT_score_5_iot_accesscomplexity_NONE)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO NO VIENE ESPECIFICADA ")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_5_iot_authentication_SINGLE)+" VULNERABILIDADES SE REQUIERE AUTENTICACIÓN SENCILLA ")
print("            -    EN  "+str(cvssV2_IMPACT_score_5_iot_authentication_MULTIPLE)+" VULNERABILIDADES SE REQUIERE AUTENTICACIÓN MULTIPLE")
print("            -    EN  "+str(cvssV2_IMPACT_score_5_iot_authentication_NONE)+" VULNERABILIDADES NO SE REQUIERE AUTENTICACIÓN")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_5_iot_confidentialityImpact_COMPLETE)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES COMPLETO ")
print("            -    EN  "+str(cvssV2_IMPACT_score_5_iot_confidentialityImpact_PARTIAL)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES PARCIAL" )
print("            -    EN  "+str(cvssV2_IMPACT_score_5_iot_confidentialityImpact_NONE)+" VULNERABILIDADES NO EXISTE IMPACTO DE CONFIDENCIALIDAD ")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_5_iot_integrityImpact_COMPLETE)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES COMPLETO ")
print("            -    EN  "+str(cvssV2_IMPACT_score_5_iot_integrityImpact_PARTIAL)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES PARCIAL" )
print("            -    EN  "+str(cvssV2_IMPACT_score_5_iot_integrityImpact_NONE)+" VULNERABILIDADES NO EXISTE IMPACTO DE INTEGRIDAD ")
print("\n")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_5_iot_availabilityImpact_COMPLETE)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES COMPLETO ")
print("            -    EN  "+str(cvssV2_IMPACT_score_5_iot_availabilityImpact_PARTIAL)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES PARCIAL" )
print("            -    EN  "+str(cvssV2_IMPACT_score_5_iot_availabilityImpact_NONE)+" VULNERABILIDADES NO EXISTE IMPACTO DE DISPONIBILIDAD ")
print("\n")
print("\n")
print("      -    EN  "+str(cvssV2_IMPACT_score_4_iot)+" VULNERABILIDADES LA PUNTUACION DE IMPACTO ESTÁ ENTRE 4 Y 5. LAS ESTADÍSTICAS DEL VECTOR STRING SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_4_iot_accessvector_NETWORK)+" VULNERABILIDADES EL VECTOR DE ACCESO ES NETWORK ")
print("            -    EN  "+str(cvssV2_IMPACT_score_4_iot_accessvector_LOCAL)+" VULNERABILIDADES EL VECTOR DE ACCESO ES LOCAL ")
print("            -    EN  "+str(cvssV2_IMPACT_score_4_iot_accessvector_PHYSICAL)+" VULNERABILIDADES EL VECTOR DE ACCESO ES PHYSICAL ")
print("            -    EN  "+str(cvssV2_IMPACT_score_4_iot_accessvector_ADJACENT_NETWORK)+" VULNERABILIDADES EL VECTOR DE ACCESO ES ADJACENT_NETWORK ")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_4_iot_accesscomplexity_HIGH)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES ALTA ")
print("            -    EN  "+str(cvssV2_IMPACT_score_4_iot_accesscomplexity_LOW)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES BAJA ")
print("            -    EN  "+str(cvssV2_IMPACT_score_4_iot_accesscomplexity_MEDIUM)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES MEDIA ")
print("            -    EN  "+str(cvssV2_IMPACT_score_4_iot_accesscomplexity_NONE)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO NO VIENE ESPECIFICADA ")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_4_iot_authentication_SINGLE)+" VULNERABILIDADES SE REQUIERE AUTENTICACIÓN SENCILLA ")
print("            -    EN  "+str(cvssV2_IMPACT_score_4_iot_authentication_MULTIPLE)+" VULNERABILIDADES SE REQUIERE AUTENTICACIÓN MULTIPLE")
print("            -    EN  "+str(cvssV2_IMPACT_score_4_iot_authentication_NONE)+" VULNERABILIDADES NO SE REQUIERE AUTENTICACIÓN")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_4_iot_confidentialityImpact_COMPLETE)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES COMPLETO ")
print("            -    EN  "+str(cvssV2_IMPACT_score_4_iot_confidentialityImpact_PARTIAL)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES PARCIAL" )
print("            -    EN  "+str(cvssV2_IMPACT_score_4_iot_confidentialityImpact_NONE)+" VULNERABILIDADES NO EXISTE IMPACTO DE CONFIDENCIALIDAD ")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_4_iot_integrityImpact_COMPLETE)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES COMPLETO ")
print("            -    EN  "+str(cvssV2_IMPACT_score_4_iot_integrityImpact_PARTIAL)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES PARCIAL" )
print("            -    EN  "+str(cvssV2_IMPACT_score_4_iot_integrityImpact_NONE)+" VULNERABILIDADES NO EXISTE IMPACTO DE INTEGRIDAD ")
print("\n")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_4_iot_availabilityImpact_COMPLETE)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES COMPLETO ")
print("            -    EN  "+str(cvssV2_IMPACT_score_4_iot_availabilityImpact_PARTIAL)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES PARCIAL" )
print("            -    EN  "+str(cvssV2_IMPACT_score_4_iot_availabilityImpact_NONE)+" VULNERABILIDADES NO EXISTE IMPACTO DE DISPONIBILIDAD ")
print("\n")
print("\n")
print("      -    EN  "+str(cvssV2_IMPACT_score_3_iot)+" VULNERABILIDADES LA PUNTUACION DE IMPACTO ESTÁ ENTRE 3 Y 4. LAS ESTADÍSTICAS DEL VECTOR STRING SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_3_iot_accessvector_NETWORK)+" VULNERABILIDADES EL VECTOR DE ACCESO ES NETWORK ")
print("            -    EN  "+str(cvssV2_IMPACT_score_3_iot_accessvector_LOCAL)+" VULNERABILIDADES EL VECTOR DE ACCESO ES LOCAL ")
print("            -    EN  "+str(cvssV2_IMPACT_score_3_iot_accessvector_PHYSICAL)+" VULNERABILIDADES EL VECTOR DE ACCESO ES PHYSICAL ")
print("            -    EN  "+str(cvssV2_IMPACT_score_3_iot_accessvector_ADJACENT_NETWORK)+" VULNERABILIDADES EL VECTOR DE ACCESO ES ADJACENT_NETWORK ")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_3_iot_accesscomplexity_HIGH)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES ALTA ")
print("            -    EN  "+str(cvssV2_IMPACT_score_3_iot_accesscomplexity_LOW)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES BAJA ")
print("            -    EN  "+str(cvssV2_IMPACT_score_3_iot_accesscomplexity_MEDIUM)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES MEDIA ")
print("            -    EN  "+str(cvssV2_IMPACT_score_3_iot_accesscomplexity_NONE)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO NO VIENE ESPECIFICADA ")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_3_iot_authentication_SINGLE)+" VULNERABILIDADES SE REQUIERE AUTENTICACIÓN SENCILLA ")
print("            -    EN  "+str(cvssV2_IMPACT_score_3_iot_authentication_MULTIPLE)+" VULNERABILIDADES SE REQUIERE AUTENTICACIÓN MULTIPLE")
print("            -    EN  "+str(cvssV2_IMPACT_score_3_iot_authentication_NONE)+" VULNERABILIDADES NO SE REQUIERE AUTENTICACIÓN")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_3_iot_confidentialityImpact_COMPLETE)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES COMPLETO ")
print("            -    EN  "+str(cvssV2_IMPACT_score_3_iot_confidentialityImpact_PARTIAL)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES PARCIAL" )
print("            -    EN  "+str(cvssV2_IMPACT_score_3_iot_confidentialityImpact_NONE)+" VULNERABILIDADES NO EXISTE IMPACTO DE CONFIDENCIALIDAD ")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_3_iot_integrityImpact_COMPLETE)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES COMPLETO ")
print("            -    EN  "+str(cvssV2_IMPACT_score_3_iot_integrityImpact_PARTIAL)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES PARCIAL" )
print("            -    EN  "+str(cvssV2_IMPACT_score_3_iot_integrityImpact_NONE)+" VULNERABILIDADES NO EXISTE IMPACTO DE INTEGRIDAD ")
print("\n")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_3_iot_availabilityImpact_COMPLETE)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES COMPLETO ")
print("            -    EN  "+str(cvssV2_IMPACT_score_3_iot_availabilityImpact_PARTIAL)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES PARCIAL" )
print("            -    EN  "+str(cvssV2_IMPACT_score_3_iot_availabilityImpact_NONE)+" VULNERABILIDADES NO EXISTE IMPACTO DE DISPONIBILIDAD ")
print("\n")
print("\n")
print("      -    EN  "+str(cvssV2_IMPACT_score_2_iot)+" VULNERABILIDADES LA PUNTUACION DE IMPACTO ESTÁ ENTRE 2 Y 3. LAS ESTADÍSTICAS DEL VECTOR STRING SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_2_iot_accessvector_NETWORK)+" VULNERABILIDADES EL VECTOR DE ACCESO ES NETWORK ")
print("            -    EN  "+str(cvssV2_IMPACT_score_2_iot_accessvector_LOCAL)+" VULNERABILIDADES EL VECTOR DE ACCESO ES LOCAL ")
print("            -    EN  "+str(cvssV2_IMPACT_score_2_iot_accessvector_PHYSICAL)+" VULNERABILIDADES EL VECTOR DE ACCESO ES PHYSICAL ")
print("            -    EN  "+str(cvssV2_IMPACT_score_2_iot_accessvector_ADJACENT_NETWORK)+" VULNERABILIDADES EL VECTOR DE ACCESO ES ADJACENT_NETWORK ")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_2_iot_accesscomplexity_HIGH)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES ALTA ")
print("            -    EN  "+str(cvssV2_IMPACT_score_2_iot_accesscomplexity_LOW)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES BAJA ")
print("            -    EN  "+str(cvssV2_IMPACT_score_2_iot_accesscomplexity_MEDIUM)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES MEDIA ")
print("            -    EN  "+str(cvssV2_IMPACT_score_2_iot_accesscomplexity_NONE)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO NO VIENE ESPECIFICADA ")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_2_iot_authentication_SINGLE)+" VULNERABILIDADES SE REQUIERE AUTENTICACIÓN SENCILLA ")
print("            -    EN  "+str(cvssV2_IMPACT_score_2_iot_authentication_MULTIPLE)+" VULNERABILIDADES SE REQUIERE AUTENTICACIÓN MULTIPLE")
print("            -    EN  "+str(cvssV2_IMPACT_score_2_iot_authentication_NONE)+" VULNERABILIDADES NO SE REQUIERE AUTENTICACIÓN")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_2_iot_confidentialityImpact_COMPLETE)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES COMPLETO ")
print("            -    EN  "+str(cvssV2_IMPACT_score_2_iot_confidentialityImpact_PARTIAL)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES PARCIAL" )
print("            -    EN  "+str(cvssV2_IMPACT_score_2_iot_confidentialityImpact_NONE)+" VULNERABILIDADES NO EXISTE IMPACTO DE CONFIDENCIALIDAD ")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_2_iot_integrityImpact_COMPLETE)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES COMPLETO ")
print("            -    EN  "+str(cvssV2_IMPACT_score_2_iot_integrityImpact_PARTIAL)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES PARCIAL" )
print("            -    EN  "+str(cvssV2_IMPACT_score_2_iot_integrityImpact_NONE)+" VULNERABILIDADES NO EXISTE IMPACTO DE INTEGRIDAD ")
print("\n")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_2_iot_availabilityImpact_COMPLETE)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES COMPLETO ")
print("            -    EN  "+str(cvssV2_IMPACT_score_2_iot_availabilityImpact_PARTIAL)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES PARCIAL" )
print("            -    EN  "+str(cvssV2_IMPACT_score_2_iot_availabilityImpact_NONE)+" VULNERABILIDADES NO EXISTE IMPACTO DE DISPONIBILIDAD ")
print("\n")
print("\n")
print("      -    EN  "+str(cvssV2_IMPACT_score_1_iot)+" VULNERABILIDADES LA PUNTUACION DE IMPACTO ESTÁ ENTRE 1 Y 2. LAS ESTADÍSTICAS DEL VECTOR STRING SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_1_iot_accessvector_NETWORK)+" VULNERABILIDADES EL VECTOR DE ACCESO ES NETWORK ")
print("            -    EN  "+str(cvssV2_IMPACT_score_1_iot_accessvector_LOCAL)+" VULNERABILIDADES EL VECTOR DE ACCESO ES LOCAL ")
print("            -    EN  "+str(cvssV2_IMPACT_score_1_iot_accessvector_PHYSICAL)+" VULNERABILIDADES EL VECTOR DE ACCESO ES PHYSICAL ")
print("            -    EN  "+str(cvssV2_IMPACT_score_1_iot_accessvector_ADJACENT_NETWORK)+" VULNERABILIDADES EL VECTOR DE ACCESO ES ADJACENT_NETWORK ")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_1_iot_accesscomplexity_HIGH)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES ALTA ")
print("            -    EN  "+str(cvssV2_IMPACT_score_1_iot_accesscomplexity_LOW)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES BAJA ")
print("            -    EN  "+str(cvssV2_IMPACT_score_1_iot_accesscomplexity_MEDIUM)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES MEDIA ")
print("            -    EN  "+str(cvssV2_IMPACT_score_1_iot_accesscomplexity_NONE)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO NO VIENE ESPECIFICADA ")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_1_iot_authentication_SINGLE)+" VULNERABILIDADES SE REQUIERE AUTENTICACIÓN SENCILLA ")
print("            -    EN  "+str(cvssV2_IMPACT_score_1_iot_authentication_MULTIPLE)+" VULNERABILIDADES SE REQUIERE AUTENTICACIÓN MULTIPLE")
print("            -    EN  "+str(cvssV2_IMPACT_score_1_iot_authentication_NONE)+" VULNERABILIDADES NO SE REQUIERE AUTENTICACIÓN")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_1_iot_confidentialityImpact_COMPLETE)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES COMPLETO ")
print("            -    EN  "+str(cvssV2_IMPACT_score_1_iot_confidentialityImpact_PARTIAL)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES PARCIAL" )
print("            -    EN  "+str(cvssV2_IMPACT_score_1_iot_confidentialityImpact_NONE)+" VULNERABILIDADES NO EXISTE IMPACTO DE CONFIDENCIALIDAD ")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_1_iot_integrityImpact_COMPLETE)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES COMPLETO ")
print("            -    EN  "+str(cvssV2_IMPACT_score_1_iot_integrityImpact_PARTIAL)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES PARCIAL" )
print("            -    EN  "+str(cvssV2_IMPACT_score_1_iot_integrityImpact_NONE)+" VULNERABILIDADES NO EXISTE IMPACTO DE INTEGRIDAD ")
print("\n")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_1_iot_availabilityImpact_COMPLETE)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES COMPLETO ")
print("            -    EN  "+str(cvssV2_IMPACT_score_1_iot_availabilityImpact_PARTIAL)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES PARCIAL" )
print("            -    EN  "+str(cvssV2_IMPACT_score_1_iot_availabilityImpact_NONE)+" VULNERABILIDADES NO EXISTE IMPACTO DE DISPONIBILIDAD ")
print("\n")
print("      -    EN  "+str(cvssV2_IMPACT_score_0_iot)+" VULNERABILIDADES LA PUNTUACION DE IMPACTO ESTÁ ENTRE 0 Y 1. LAS ESTADÍSTICAS DEL VECTOR STRING SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_0_iot_accessvector_NETWORK)+" VULNERABILIDADES EL VECTOR DE ACCESO ES NETWORK ")
print("            -    EN  "+str(cvssV2_IMPACT_score_0_iot_accessvector_LOCAL)+" VULNERABILIDADES EL VECTOR DE ACCESO ES LOCAL ")
print("            -    EN  "+str(cvssV2_IMPACT_score_0_iot_accessvector_PHYSICAL)+" VULNERABILIDADES EL VECTOR DE ACCESO ES PHYSICAL ")
print("            -    EN  "+str(cvssV2_IMPACT_score_0_iot_accessvector_ADJACENT_NETWORK)+" VULNERABILIDADES EL VECTOR DE ACCESO ES ADJACENT_NETWORK ")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_0_iot_accesscomplexity_HIGH)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES ALTA ")
print("            -    EN  "+str(cvssV2_IMPACT_score_0_iot_accesscomplexity_LOW)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES BAJA ")
print("            -    EN  "+str(cvssV2_IMPACT_score_0_iot_accesscomplexity_MEDIUM)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES MEDIA ")
print("            -    EN  "+str(cvssV2_IMPACT_score_0_iot_accesscomplexity_NONE)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO NO VIENE ESPECIFICADA ")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_0_iot_authentication_SINGLE)+" VULNERABILIDADES SE REQUIERE AUTENTICACIÓN SENCILLA ")
print("            -    EN  "+str(cvssV2_IMPACT_score_0_iot_authentication_MULTIPLE)+" VULNERABILIDADES SE REQUIERE AUTENTICACIÓN MULTIPLE")
print("            -    EN  "+str(cvssV2_IMPACT_score_0_iot_authentication_NONE)+" VULNERABILIDADES NO SE REQUIERE AUTENTICACIÓN")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_0_iot_confidentialityImpact_COMPLETE)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES COMPLETO ")
print("            -    EN  "+str(cvssV2_IMPACT_score_0_iot_confidentialityImpact_PARTIAL)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES PARCIAL" )
print("            -    EN  "+str(cvssV2_IMPACT_score_0_iot_confidentialityImpact_NONE)+" VULNERABILIDADES NO EXISTE IMPACTO DE CONFIDENCIALIDAD ")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_0_iot_integrityImpact_COMPLETE)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES COMPLETO ")
print("            -    EN  "+str(cvssV2_IMPACT_score_0_iot_integrityImpact_PARTIAL)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES PARCIAL" )
print("            -    EN  "+str(cvssV2_IMPACT_score_0_iot_integrityImpact_NONE)+" VULNERABILIDADES NO EXISTE IMPACTO DE INTEGRIDAD ")
print("\n")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_0_iot_availabilityImpact_COMPLETE)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES COMPLETO ")
print("            -    EN  "+str(cvssV2_IMPACT_score_0_iot_availabilityImpact_PARTIAL)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES PARCIAL" )
print("            -    EN  "+str(cvssV2_IMPACT_score_0_iot_availabilityImpact_NONE)+" VULNERABILIDADES NO EXISTE IMPACTO DE DISPONIBILIDAD ")
print("\n")
print("\n")
print("      -    EN  "+str(cvssV2_no_IMPACT_score_iot)+" VULNERABILIDADES LA PUNTUACION DE IMPACTO NO ESTÁ ESPECIFICADA. LAS ESTADÍSTICAS DEL VECTOR STRING SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(cvssV2_no_IMPACT_score_iot_accessvector_NETWORK)+" VULNERABILIDADES EL VECTOR DE ACCESO ES NETWORK ")
print("            -    EN  "+str(cvssV2_no_IMPACT_score_iot_accessvector_LOCAL)+" VULNERABILIDADES EL VECTOR DE ACCESO ES LOCAL ")
print("            -    EN  "+str(cvssV2_no_IMPACT_score_iot_accessvector_PHYSICAL)+" VULNERABILIDADES EL VECTOR DE ACCESO ES PHYSICAL ")
print("            -    EN  "+str(cvssV2_no_IMPACT_score_iot_accessvector_ADJACENT_NETWORK)+" VULNERABILIDADES EL VECTOR DE ACCESO ES ADJACENT_NETWORK ")
print("\n")
print("            -    EN  "+str(cvssV2_no_IMPACT_score_iot_accesscomplexity_HIGH)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES ALTA ")
print("            -    EN  "+str(cvssV2_no_IMPACT_score_iot_accesscomplexity_LOW)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES BAJA ")
print("            -    EN  "+str(cvssV2_no_IMPACT_score_iot_accesscomplexity_MEDIUM)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES MEDIA ")
print("            -    EN  "+str(cvssV2_no_IMPACT_score_iot_accesscomplexity_NONE)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO NO VIENE ESPECIFICADA ")
print("\n")
print("            -    EN  "+str(cvssV2_no_IMPACT_score_iot_authentication_SINGLE)+" VULNERABILIDADES SE REQUIERE AUTENTICACIÓN SENCILLA ")
print("            -    EN  "+str(cvssV2_no_IMPACT_score_iot_authentication_MULTIPLE)+" VULNERABILIDADES SE REQUIERE AUTENTICACIÓN MULTIPLE")
print("            -    EN  "+str(cvssV2_no_IMPACT_score_iot_authentication_NONE)+" VULNERABILIDADES NO SE REQUIERE AUTENTICACIÓN")
print("\n")
print("            -    EN  "+str(cvssV2_no_IMPACT_score_iot_confidentialityImpact_COMPLETE)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES COMPLETO ")
print("            -    EN  "+str(cvssV2_no_IMPACT_score_iot_confidentialityImpact_PARTIAL)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES PARCIAL" )
print("            -    EN  "+str(cvssV2_no_IMPACT_score_iot_confidentialityImpact_NONE)+" VULNERABILIDADES NO EXISTE IMPACTO DE CONFIDENCIALIDAD ")
print("\n")
print("            -    EN  "+str(cvssV2_no_IMPACT_score_iot_integrityImpact_COMPLETE)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES COMPLETO ")
print("            -    EN  "+str(cvssV2_no_IMPACT_score_iot_integrityImpact_PARTIAL)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES PARCIAL" )
print("            -    EN  "+str(cvssV2_no_IMPACT_score_iot_integrityImpact_NONE)+" VULNERABILIDADES NO EXISTE IMPACTO DE INTEGRIDAD ")
print("\n")
print("\n")
print("            -    EN  "+str(cvssV2_no_IMPACT_score_iot_availabilityImpact_COMPLETE)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES COMPLETO ")
print("            -    EN  "+str(cvssV2_no_IMPACT_score_iot_availabilityImpact_PARTIAL)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES PARCIAL" )
print("            -    EN  "+str(cvssV2_no_IMPACT_score_iot_availabilityImpact_NONE)+" VULNERABILIDADES NO EXISTE IMPACTO DE DISPONIBILIDAD ")
print("\n")

            
          
            
            
        
            
print("________________________PORCENTAJES ELEMENTOS VECTOR STRING-PUNTUACION DE IMPACTO CVSSV2 PARTE IOT________________________")
print("\n")        
            
            
    
print("\n")
print(" DE UN TOTAL DE "+str(len(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.availabilityImpact"]))+" VULNERABILIDADES , LOS PORCENTAJES DE ELEMENTOS DE VECTOR STRING SEGUND PUNTUACION DE IMPACTO SON LAS SIGUIENTES:  \n")
print("\n")
if(cvssV2_IMPACT_score_10_iot>0):
    print("      -    EN EL "+str(float(((cvssV2_IMPACT_score_10_iot*100)/len(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"]))))+" % DE  VULNERABILIDADES LA PUNTUACION DE IMPACTO ES 10. LOS PORCENTAJES DEL VECTOR STRING SON LOS SIGUIENTES:  \n")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_10_iot_accessvector_NETWORK*100)/cvssV2_IMPACT_score_10_iot)))+" % DE  VULNERABILIDADES EL VECTOR DE ACCESO ES NETWORK ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_10_iot_accessvector_LOCAL*100)/cvssV2_IMPACT_score_10_iot)))+" % DE  VULNERABILIDADES EL VECTOR DE ACCESO ES LOCAL ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_10_iot_accessvector_PHYSICAL*100)/cvssV2_IMPACT_score_10_iot)))+" % DE  VULNERABILIDADES EL VECTOR DE ACCESO ES PHYSICAL ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_10_iot_accessvector_ADJACENT_NETWORK*100)/cvssV2_IMPACT_score_10_iot)))+" % DE  VULNERABILIDADES EL VECTOR DE ACCESO ES ADJACENT_NETWORK ")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_10_iot_accesscomplexity_HIGH*100)/cvssV2_IMPACT_score_10_iot)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES ALTA ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_10_iot_accesscomplexity_LOW*100)/cvssV2_IMPACT_score_10_iot)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES BAJA ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_10_iot_accesscomplexity_MEDIUM*100)/cvssV2_IMPACT_score_10_iot)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES MEDIA ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_10_iot_accesscomplexity_NONE*100)/cvssV2_IMPACT_score_10_iot)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ACCESO NO VIENE ESPECIFICADA ")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_10_iot_authentication_SINGLE*100)/cvssV2_IMPACT_score_10_iot)))+" % DE  VULNERABILIDADES SE REQUIERE AUTENTICACIÓN SENCILLA ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_10_iot_authentication_MULTIPLE*100)/cvssV2_IMPACT_score_10_iot)))+" % DE  VULNERABILIDADES SE REQUIERE AUTENTICACIÓN MÚLTIPLE")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_10_iot_authentication_NONE*100)/cvssV2_IMPACT_score_10_iot)))+" % DE  VULNERABILIDADES NO VIENE ESPECIFICADO SI SE REQUIERE AUTENTICACIÓN")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_10_iot_confidentialityImpact_COMPLETE*100)/cvssV2_IMPACT_score_10_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES COMPLETO ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_10_iot_confidentialityImpact_PARTIAL*100)/cvssV2_IMPACT_score_10_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES PARCIAL" )
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_10_iot_confidentialityImpact_NONE*100)/cvssV2_IMPACT_score_10_iot)))+" % DE  VULNERABILIDADES NO EXISTE IMPACTO DE CONFIDENCIALIDAD ")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_10_iot_integrityImpact_COMPLETE*100)/cvssV2_IMPACT_score_10_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES COMPLETO ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_10_iot_integrityImpact_PARTIAL*100)/cvssV2_IMPACT_score_10_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES PARCIAL" )
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_10_iot_integrityImpact_NONE*100)/cvssV2_IMPACT_score_10_iot)))+" % DE  VULNERABILIDADES NO EXISTE IMPACTO DE INTEGRIDAD ")
    print("\n")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_10_iot_availabilityImpact_COMPLETE*100)/cvssV2_IMPACT_score_10_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES COMPLETO ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_10_iot_availabilityImpact_PARTIAL*100)/cvssV2_IMPACT_score_10_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES PARCIAL" )
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_10_iot_availabilityImpact_NONE*100)/cvssV2_IMPACT_score_10_iot)))+" % DE  VULNERABILIDADES NO EXISTE IMPACTO DE DISPONIBILIDAD ")
print("\n")
if(cvssV2_IMPACT_score_9_iot>0):
    print("      -    EN EL "+str(float(((cvssV2_IMPACT_score_9_iot*100)/len(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"]))))+" % DE  VULNERABILIDADES LA PUNTUACION DE IMPACTO ESTÁ ENTRE 9 Y 10. LOS PORCENTAJES DEL VECTOR STRING SON LOS SIGUIENTES:  \n")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_9_iot_accessvector_NETWORK*100)/cvssV2_IMPACT_score_9_iot)))+" % DE  VULNERABILIDADES EL VECTOR DE ACCESO ES NETWORK ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_9_iot_accessvector_LOCAL*100)/cvssV2_IMPACT_score_9_iot)))+" % DE  VULNERABILIDADES EL VECTOR DE ACCESO ES LOCAL ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_9_iot_accessvector_PHYSICAL*100)/cvssV2_IMPACT_score_9_iot)))+" % DE  VULNERABILIDADES EL VECTOR DE ACCESO ES PHYSICAL ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_9_iot_accessvector_ADJACENT_NETWORK*100)/cvssV2_IMPACT_score_9_iot)))+" % DE  VULNERABILIDADES EL VECTOR DE ACCESO ES ADJACENT_NETWORK ")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_9_iot_accesscomplexity_HIGH*100)/cvssV2_IMPACT_score_9_iot)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES ALTA ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_9_iot_accesscomplexity_LOW*100)/cvssV2_IMPACT_score_9_iot)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES BAJA ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_9_iot_accesscomplexity_MEDIUM*100)/cvssV2_IMPACT_score_9_iot)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES MEDIA ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_9_iot_accesscomplexity_NONE*100)/cvssV2_IMPACT_score_9_iot)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ACCESO NO VIENE ESPECIFICADA ")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_9_iot_authentication_SINGLE*100)/cvssV2_IMPACT_score_9_iot)))+" % DE  VULNERABILIDADES SE REQUIERE AUTENTICACIÓN SENCILLA ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_9_iot_authentication_MULTIPLE*100)/cvssV2_IMPACT_score_9_iot)))+" % DE  VULNERABILIDADES SE REQUIERE AUTENTICACIÓN MÚLTIPLE")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_9_iot_authentication_NONE*100)/cvssV2_IMPACT_score_9_iot)))+" % DE  VULNERABILIDADES NO VIENE ESPECIFICADO SI SE REQUIERE AUTENTICACIÓN")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_9_iot_confidentialityImpact_COMPLETE*100)/cvssV2_IMPACT_score_9_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES COMPLETO ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_9_iot_confidentialityImpact_PARTIAL*100)/cvssV2_IMPACT_score_9_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES PARCIAL" )
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_9_iot_confidentialityImpact_NONE*100)/cvssV2_IMPACT_score_9_iot)))+" % DE  VULNERABILIDADES NO EXISTE IMPACTO DE CONFIDENCIALIDAD ")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_9_iot_integrityImpact_COMPLETE*100)/cvssV2_IMPACT_score_9_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES COMPLETO ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_9_iot_integrityImpact_PARTIAL*100)/cvssV2_IMPACT_score_9_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES PARCIAL" )
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_9_iot_integrityImpact_NONE*100)/cvssV2_IMPACT_score_9_iot)))+" % DE  VULNERABILIDADES NO EXISTE IMPACTO DE INTEGRIDAD ")
    print("\n")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_9_iot_availabilityImpact_COMPLETE*100)/cvssV2_IMPACT_score_9_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES COMPLETO ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_9_iot_availabilityImpact_PARTIAL*100)/cvssV2_IMPACT_score_9_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES PARCIAL" )
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_9_iot_availabilityImpact_NONE*100)/cvssV2_IMPACT_score_9_iot)))+" % DE  VULNERABILIDADES NO EXISTE IMPACTO DE DISPONIBILIDAD ")           
print("\n")
if(cvssV2_IMPACT_score_8_iot>0):
    print("      -    EN EL "+str(float(((cvssV2_IMPACT_score_8_iot*100)/len(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"]))))+" % DE  VULNERABILIDADES LA PUNTUACION DE IMPACTO ESTÁ ENTRE 8 Y 9. LOS PORCENTAJES DEL VECTOR STRING SON LOS SIGUIENTES:  \n")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_8_iot_accessvector_NETWORK*100)/cvssV2_IMPACT_score_8_iot)))+" % DE  VULNERABILIDADES EL VECTOR DE ACCESO ES NETWORK ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_8_iot_accessvector_LOCAL*100)/cvssV2_IMPACT_score_8_iot)))+" % DE  VULNERABILIDADES EL VECTOR DE ACCESO ES LOCAL ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_8_iot_accessvector_PHYSICAL*100)/cvssV2_IMPACT_score_8_iot)))+" % DE  VULNERABILIDADES EL VECTOR DE ACCESO ES PHYSICAL ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_8_iot_accessvector_ADJACENT_NETWORK*100)/cvssV2_IMPACT_score_8_iot)))+" % DE  VULNERABILIDADES EL VECTOR DE ACCESO ES ADJACENT_NETWORK ")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_8_iot_accesscomplexity_HIGH*100)/cvssV2_IMPACT_score_8_iot)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES ALTA ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_8_iot_accesscomplexity_LOW*100)/cvssV2_IMPACT_score_8_iot)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES BAJA ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_8_iot_accesscomplexity_MEDIUM*100)/cvssV2_IMPACT_score_8_iot)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES MEDIA ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_8_iot_accesscomplexity_NONE*100)/cvssV2_IMPACT_score_8_iot)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ACCESO NO VIENE ESPECIFICADA ")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_8_iot_authentication_SINGLE*100)/cvssV2_IMPACT_score_8_iot)))+" % DE  VULNERABILIDADES SE REQUIERE AUTENTICACIÓN SENCILLA ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_8_iot_authentication_MULTIPLE*100)/cvssV2_IMPACT_score_8_iot)))+" % DE  VULNERABILIDADES SE REQUIERE AUTENTICACIÓN MÚLTIPLE")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_8_iot_authentication_NONE*100)/cvssV2_IMPACT_score_8_iot)))+" % DE  VULNERABILIDADES NO VIENE ESPECIFICADO SI SE REQUIERE AUTENTICACIÓN")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_8_iot_confidentialityImpact_COMPLETE*100)/cvssV2_IMPACT_score_8_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES COMPLETO ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_8_iot_confidentialityImpact_PARTIAL*100)/cvssV2_IMPACT_score_8_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES PARCIAL" )
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_8_iot_confidentialityImpact_NONE*100)/cvssV2_IMPACT_score_8_iot)))+" % DE  VULNERABILIDADES NO EXISTE IMPACTO DE CONFIDENCIALIDAD ")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_8_iot_integrityImpact_COMPLETE*100)/cvssV2_IMPACT_score_8_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES COMPLETO ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_8_iot_integrityImpact_PARTIAL*100)/cvssV2_IMPACT_score_8_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES PARCIAL" )
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_8_iot_integrityImpact_NONE*100)/cvssV2_IMPACT_score_8_iot)))+" % DE  VULNERABILIDADES NO EXISTE IMPACTO DE INTEGRIDAD ")
    print("\n")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_8_iot_availabilityImpact_COMPLETE*100)/cvssV2_IMPACT_score_8_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES COMPLETO ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_8_iot_availabilityImpact_PARTIAL*100)/cvssV2_IMPACT_score_8_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES PARCIAL" )
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_8_iot_availabilityImpact_NONE*100)/cvssV2_IMPACT_score_8_iot)))+" % DE  VULNERABILIDADES NO EXISTE IMPACTO DE DISPONIBILIDAD ")           
    print("\n")
if(cvssV2_IMPACT_score_7_iot>0):
    print("      -    EN EL "+str(float(((cvssV2_IMPACT_score_7_iot*100)/len(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"]))))+" % DE  VULNERABILIDADES LA PUNTUACION DE IMPACTO ESTÁ ENTRE 7 Y 8. LOS PORCENTAJES DEL VECTOR STRING SON LOS SIGUIENTES:  \n")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_7_iot_accessvector_NETWORK*100)/cvssV2_IMPACT_score_7_iot)))+" % DE  VULNERABILIDADES EL VECTOR DE ACCESO ES NETWORK ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_7_iot_accessvector_LOCAL*100)/cvssV2_IMPACT_score_7_iot)))+" % DE  VULNERABILIDADES EL VECTOR DE ACCESO ES LOCAL ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_7_iot_accessvector_PHYSICAL*100)/cvssV2_IMPACT_score_7_iot)))+" % DE  VULNERABILIDADES EL VECTOR DE ACCESO ES PHYSICAL ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_7_iot_accessvector_ADJACENT_NETWORK*100)/cvssV2_IMPACT_score_7_iot)))+" % DE  VULNERABILIDADES EL VECTOR DE ACCESO ES ADJACENT_NETWORK ")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_7_iot_accesscomplexity_HIGH*100)/cvssV2_IMPACT_score_7_iot)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES ALTA ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_7_iot_accesscomplexity_LOW*100)/cvssV2_IMPACT_score_7_iot)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES BAJA ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_7_iot_accesscomplexity_MEDIUM*100)/cvssV2_IMPACT_score_7_iot)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES MEDIA ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_7_iot_accesscomplexity_NONE*100)/cvssV2_IMPACT_score_7_iot)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ACCESO NO VIENE ESPECIFICADA ")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_7_iot_authentication_SINGLE*100)/cvssV2_IMPACT_score_7_iot)))+" % DE  VULNERABILIDADES SE REQUIERE AUTENTICACIÓN SENCILLA ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_7_iot_authentication_MULTIPLE*100)/cvssV2_IMPACT_score_7_iot)))+" % DE  VULNERABILIDADES SE REQUIERE AUTENTICACIÓN MÚLTIPLE")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_7_iot_authentication_NONE*100)/cvssV2_IMPACT_score_7_iot)))+" % DE  VULNERABILIDADES NO VIENE ESPECIFICADO SI SE REQUIERE AUTENTICACIÓN")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_7_iot_confidentialityImpact_COMPLETE*100)/cvssV2_IMPACT_score_7_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES COMPLETO ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_7_iot_confidentialityImpact_PARTIAL*100)/cvssV2_IMPACT_score_7_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES PARCIAL" )
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_7_iot_confidentialityImpact_NONE*100)/cvssV2_IMPACT_score_7_iot)))+" % DE  VULNERABILIDADES NO EXISTE IMPACTO DE CONFIDENCIALIDAD ")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_7_iot_integrityImpact_COMPLETE*100)/cvssV2_IMPACT_score_7_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES COMPLETO ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_7_iot_integrityImpact_PARTIAL*100)/cvssV2_IMPACT_score_7_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES PARCIAL" )
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_7_iot_integrityImpact_NONE*100)/cvssV2_IMPACT_score_7_iot)))+" % DE  VULNERABILIDADES NO EXISTE IMPACTO DE INTEGRIDAD ")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_7_iot_availabilityImpact_COMPLETE*100)/cvssV2_IMPACT_score_7_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES COMPLETO ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_7_iot_availabilityImpact_PARTIAL*100)/cvssV2_IMPACT_score_7_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES PARCIAL" )
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_7_iot_availabilityImpact_NONE*100)/cvssV2_IMPACT_score_7_iot)))+" % DE  VULNERABILIDADES NO EXISTE IMPACTO DE DISPONIBILIDAD ")           
    print("\n")
if(cvssV2_IMPACT_score_6_iot>0):
    print("      -    EN EL "+str(float(((cvssV2_IMPACT_score_6_iot*100)/len(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"]))))+" % DE  VULNERABILIDADES LA PUNTUACION DE IMPACTO ESTÁ ENTRE 6 Y 7. LOS PORCENTAJES DEL VECTOR STRING SON LOS SIGUIENTES:  \n")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_6_iot_accessvector_NETWORK*100)/cvssV2_IMPACT_score_6_iot)))+" % DE  VULNERABILIDADES EL VECTOR DE ACCESO ES NETWORK ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_6_iot_accessvector_LOCAL*100)/cvssV2_IMPACT_score_6_iot)))+" % DE  VULNERABILIDADES EL VECTOR DE ACCESO ES LOCAL ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_6_iot_accessvector_PHYSICAL*100)/cvssV2_IMPACT_score_6_iot)))+" % DE  VULNERABILIDADES EL VECTOR DE ACCESO ES PHYSICAL ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_6_iot_accessvector_ADJACENT_NETWORK*100)/cvssV2_IMPACT_score_6_iot)))+" % DE  VULNERABILIDADES EL VECTOR DE ACCESO ES ADJACENT_NETWORK ")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_6_iot_accesscomplexity_HIGH*100)/cvssV2_IMPACT_score_6_iot)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES ALTA ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_6_iot_accesscomplexity_LOW*100)/cvssV2_IMPACT_score_6_iot)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES BAJA ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_6_iot_accesscomplexity_MEDIUM*100)/cvssV2_IMPACT_score_6_iot)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES MEDIA ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_6_iot_accesscomplexity_NONE*100)/cvssV2_IMPACT_score_6_iot)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ACCESO NO VIENE ESPECIFICADA ")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_6_iot_authentication_SINGLE*100)/cvssV2_IMPACT_score_6_iot)))+" % DE  VULNERABILIDADES SE REQUIERE AUTENTICACIÓN SENCILLA ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_6_iot_authentication_MULTIPLE*100)/cvssV2_IMPACT_score_6_iot)))+" % DE  VULNERABILIDADES SE REQUIERE AUTENTICACIÓN MÚLTIPLE")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_6_iot_authentication_NONE*100)/cvssV2_IMPACT_score_6_iot)))+" % DE  VULNERABILIDADES NO VIENE ESPECIFICADO SI SE REQUIERE AUTENTICACIÓN")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_6_iot_confidentialityImpact_COMPLETE*100)/cvssV2_IMPACT_score_6_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES COMPLETO ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_6_iot_confidentialityImpact_PARTIAL*100)/cvssV2_IMPACT_score_6_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES PARCIAL" )
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_6_iot_confidentialityImpact_NONE*100)/cvssV2_IMPACT_score_6_iot)))+" % DE  VULNERABILIDADES NO EXISTE IMPACTO DE CONFIDENCIALIDAD ")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_6_iot_integrityImpact_COMPLETE*100)/cvssV2_IMPACT_score_6_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES COMPLETO ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_6_iot_integrityImpact_PARTIAL*100)/cvssV2_IMPACT_score_6_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES PARCIAL" )
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_6_iot_integrityImpact_NONE*100)/cvssV2_IMPACT_score_6_iot)))+" % DE  VULNERABILIDADES NO EXISTE IMPACTO DE INTEGRIDAD ")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_6_iot_availabilityImpact_COMPLETE*100)/cvssV2_IMPACT_score_6_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES COMPLETO ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_6_iot_availabilityImpact_PARTIAL*100)/cvssV2_IMPACT_score_6_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES PARCIAL" )
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_6_iot_availabilityImpact_NONE*100)/cvssV2_IMPACT_score_6_iot)))+" % DE  VULNERABILIDADES NO EXISTE IMPACTO DE DISPONIBILIDAD ")   
    print("\n")
if(cvssV2_IMPACT_score_5_iot>0):
    print("      -    EN EL "+str(float(((cvssV2_IMPACT_score_5_iot*100)/len(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"]))))+" % DE  VULNERABILIDADES LA PUNTUACION DE IMPACTO ESTÁ ENTRE 5 Y 6. LOS PORCENTAJES DEL VECTOR STRING SON LOS SIGUIENTES:  \n")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_5_iot_accessvector_NETWORK*100)/cvssV2_IMPACT_score_5_iot)))+" % DE  VULNERABILIDADES EL VECTOR DE ACCESO ES NETWORK ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_5_iot_accessvector_LOCAL*100)/cvssV2_IMPACT_score_5_iot)))+" % DE  VULNERABILIDADES EL VECTOR DE ACCESO ES LOCAL ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_5_iot_accessvector_PHYSICAL*100)/cvssV2_IMPACT_score_5_iot)))+" % DE  VULNERABILIDADES EL VECTOR DE ACCESO ES PHYSICAL ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_5_iot_accessvector_ADJACENT_NETWORK*100)/cvssV2_IMPACT_score_5_iot)))+" % DE  VULNERABILIDADES EL VECTOR DE ACCESO ES ADJACENT_NETWORK ")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_5_iot_accesscomplexity_HIGH*100)/cvssV2_IMPACT_score_5_iot)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES ALTA ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_5_iot_accesscomplexity_LOW*100)/cvssV2_IMPACT_score_5_iot)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES BAJA ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_5_iot_accesscomplexity_MEDIUM*100)/cvssV2_IMPACT_score_5_iot)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES MEDIA ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_5_iot_accesscomplexity_NONE*100)/cvssV2_IMPACT_score_5_iot)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ACCESO NO VIENE ESPECIFICADA ")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_5_iot_authentication_SINGLE*100)/cvssV2_IMPACT_score_5_iot)))+" % DE  VULNERABILIDADES SE REQUIERE AUTENTICACIÓN SENCILLA ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_5_iot_authentication_MULTIPLE*100)/cvssV2_IMPACT_score_5_iot)))+" % DE  VULNERABILIDADES SE REQUIERE AUTENTICACIÓN MÚLTIPLE")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_5_iot_authentication_NONE*100)/cvssV2_IMPACT_score_5_iot)))+" % DE  VULNERABILIDADES NO VIENE ESPECIFICADO SI SE REQUIERE AUTENTICACIÓN")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_5_iot_confidentialityImpact_COMPLETE*100)/cvssV2_IMPACT_score_5_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES COMPLETO ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_5_iot_confidentialityImpact_PARTIAL*100)/cvssV2_IMPACT_score_5_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES PARCIAL" )
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_5_iot_confidentialityImpact_NONE*100)/cvssV2_IMPACT_score_5_iot)))+" % DE  VULNERABILIDADES NO EXISTE IMPACTO DE CONFIDENCIALIDAD ")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_5_iot_integrityImpact_COMPLETE*100)/cvssV2_IMPACT_score_5_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES COMPLETO ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_5_iot_integrityImpact_PARTIAL*100)/cvssV2_IMPACT_score_5_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES PARCIAL" )
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_5_iot_integrityImpact_NONE*100)/cvssV2_IMPACT_score_5_iot)))+" % DE  VULNERABILIDADES NO EXISTE IMPACTO DE INTEGRIDAD ")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_5_iot_availabilityImpact_COMPLETE*100)/cvssV2_IMPACT_score_5_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES COMPLETO ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_5_iot_availabilityImpact_PARTIAL*100)/cvssV2_IMPACT_score_5_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES PARCIAL" )
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_5_iot_availabilityImpact_NONE*100)/cvssV2_IMPACT_score_5_iot)))+" % DE  VULNERABILIDADES NO EXISTE IMPACTO DE DISPONIBILIDAD ")
    print("\n")
if(cvssV2_IMPACT_score_4_iot>0):
    print("      -    EN EL "+str(float(((cvssV2_IMPACT_score_4_iot*100)/len(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"]))))+" % DE  VULNERABILIDADES LA PUNTUACION DE IMPACTO ESTÁ ENTRE 4 Y 5. LOS PORCENTAJES DEL VECTOR STRING SON LOS SIGUIENTES:  \n")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_4_iot_accessvector_NETWORK*100)/cvssV2_IMPACT_score_4_iot)))+" % DE  VULNERABILIDADES EL VECTOR DE ACCESO ES NETWORK ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_4_iot_accessvector_LOCAL*100)/cvssV2_IMPACT_score_4_iot)))+" % DE  VULNERABILIDADES EL VECTOR DE ACCESO ES LOCAL ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_4_iot_accessvector_PHYSICAL*100)/cvssV2_IMPACT_score_4_iot)))+" % DE  VULNERABILIDADES EL VECTOR DE ACCESO ES PHYSICAL ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_4_iot_accessvector_ADJACENT_NETWORK*100)/cvssV2_IMPACT_score_4_iot)))+" % DE  VULNERABILIDADES EL VECTOR DE ACCESO ES ADJACENT_NETWORK ")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_4_iot_accesscomplexity_HIGH*100)/cvssV2_IMPACT_score_4_iot)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES ALTA ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_4_iot_accesscomplexity_LOW*100)/cvssV2_IMPACT_score_4_iot)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES BAJA ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_4_iot_accesscomplexity_MEDIUM*100)/cvssV2_IMPACT_score_4_iot)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES MEDIA ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_4_iot_accesscomplexity_NONE*100)/cvssV2_IMPACT_score_4_iot)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ACCESO NO VIENE ESPECIFICADA ")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_4_iot_authentication_SINGLE*100)/cvssV2_IMPACT_score_4_iot)))+" % DE  VULNERABILIDADES SE REQUIERE AUTENTICACIÓN SENCILLA ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_4_iot_authentication_MULTIPLE*100)/cvssV2_IMPACT_score_4_iot)))+" % DE  VULNERABILIDADES SE REQUIERE AUTENTICACIÓN MÚLTIPLE")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_4_iot_authentication_NONE*100)/cvssV2_IMPACT_score_4_iot)))+" % DE  VULNERABILIDADES NO VIENE ESPECIFICADO SI SE REQUIERE AUTENTICACIÓN")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_4_iot_confidentialityImpact_COMPLETE*100)/cvssV2_IMPACT_score_4_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES COMPLETO ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_4_iot_confidentialityImpact_PARTIAL*100)/cvssV2_IMPACT_score_4_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES PARCIAL" )
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_4_iot_confidentialityImpact_NONE*100)/cvssV2_IMPACT_score_4_iot)))+" % DE  VULNERABILIDADES NO EXISTE IMPACTO DE CONFIDENCIALIDAD ")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_4_iot_integrityImpact_COMPLETE*100)/cvssV2_IMPACT_score_4_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES COMPLETO ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_4_iot_integrityImpact_PARTIAL*100)/cvssV2_IMPACT_score_4_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES PARCIAL" )
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_4_iot_integrityImpact_NONE*100)/cvssV2_IMPACT_score_4_iot)))+" % DE  VULNERABILIDADES NO EXISTE IMPACTO DE INTEGRIDAD ")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_4_iot_availabilityImpact_COMPLETE*100)/cvssV2_IMPACT_score_4_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES COMPLETO ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_4_iot_availabilityImpact_PARTIAL*100)/cvssV2_IMPACT_score_4_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES PARCIAL" )
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_4_iot_availabilityImpact_NONE*100)/cvssV2_IMPACT_score_4_iot)))+" % DE  VULNERABILIDADES NO EXISTE IMPACTO DE DISPONIBILIDAD ")
    print("\n") 
if(cvssV2_IMPACT_score_3_iot>0):
    print("      -    EN EL "+str(float(((cvssV2_IMPACT_score_3_iot*100)/len(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"]))))+" % DE  VULNERABILIDADES LA PUNTUACION DE IMPACTO ESTÁ ENTRE 3 Y 4. LOS PORCENTAJES DEL VECTOR STRING SON LOS SIGUIENTES:  \n")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_3_iot_accessvector_NETWORK*100)/cvssV2_IMPACT_score_3_iot)))+" % DE  VULNERABILIDADES EL VECTOR DE ACCESO ES NETWORK ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_3_iot_accessvector_LOCAL*100)/cvssV2_IMPACT_score_3_iot)))+" % DE  VULNERABILIDADES EL VECTOR DE ACCESO ES LOCAL ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_3_iot_accessvector_PHYSICAL*100)/cvssV2_IMPACT_score_3_iot)))+" % DE  VULNERABILIDADES EL VECTOR DE ACCESO ES PHYSICAL ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_3_iot_accessvector_ADJACENT_NETWORK*100)/cvssV2_IMPACT_score_3_iot)))+" % DE  VULNERABILIDADES EL VECTOR DE ACCESO ES ADJACENT_NETWORK ")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_3_iot_accesscomplexity_HIGH*100)/cvssV2_IMPACT_score_3_iot)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES ALTA ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_3_iot_accesscomplexity_LOW*100)/cvssV2_IMPACT_score_3_iot)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES BAJA ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_3_iot_accesscomplexity_MEDIUM*100)/cvssV2_IMPACT_score_3_iot)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES MEDIA ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_3_iot_accesscomplexity_NONE*100)/cvssV2_IMPACT_score_3_iot)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ACCESO NO VIENE ESPECIFICADA ")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_3_iot_authentication_SINGLE*100)/cvssV2_IMPACT_score_3_iot)))+" % DE  VULNERABILIDADES SE REQUIERE AUTENTICACIÓN SENCILLA ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_3_iot_authentication_MULTIPLE*100)/cvssV2_IMPACT_score_3_iot)))+" % DE  VULNERABILIDADES SE REQUIERE AUTENTICACIÓN MÚLTIPLE")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_3_iot_authentication_NONE*100)/cvssV2_IMPACT_score_3_iot)))+" % DE  VULNERABILIDADES NO VIENE ESPECIFICADO SI SE REQUIERE AUTENTICACIÓN")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_3_iot_confidentialityImpact_COMPLETE*100)/cvssV2_IMPACT_score_3_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES COMPLETO ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_3_iot_confidentialityImpact_PARTIAL*100)/cvssV2_IMPACT_score_3_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES PARCIAL" )
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_3_iot_confidentialityImpact_NONE*100)/cvssV2_IMPACT_score_3_iot)))+" % DE  VULNERABILIDADES NO EXISTE IMPACTO DE CONFIDENCIALIDAD ")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_3_iot_integrityImpact_COMPLETE*100)/cvssV2_IMPACT_score_3_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES COMPLETO ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_3_iot_integrityImpact_PARTIAL*100)/cvssV2_IMPACT_score_3_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES PARCIAL" )
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_3_iot_integrityImpact_NONE*100)/cvssV2_IMPACT_score_3_iot)))+" % DE  VULNERABILIDADES NO EXISTE IMPACTO DE INTEGRIDAD ")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_3_iot_availabilityImpact_COMPLETE*100)/cvssV2_IMPACT_score_3_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES COMPLETO ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_3_iot_availabilityImpact_PARTIAL*100)/cvssV2_IMPACT_score_3_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES PARCIAL" )
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_3_iot_availabilityImpact_NONE*100)/cvssV2_IMPACT_score_3_iot)))+" % DE  VULNERABILIDADES NO EXISTE IMPACTO DE DISPONIBILIDAD ")
    print("\n")
if(cvssV2_IMPACT_score_2_iot>0):
    print("      -    EN EL "+str(float(((cvssV2_IMPACT_score_2_iot*100)/len(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"]))))+" % DE  VULNERABILIDADES LA PUNTUACION DE IMPACTO ESTÁ ENTRE 2 Y 3. LOS PORCENTAJES DEL VECTOR STRING SON LOS SIGUIENTES:  \n")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_2_iot_accessvector_NETWORK*100)/cvssV2_IMPACT_score_2_iot)))+" % DE  VULNERABILIDADES EL VECTOR DE ACCESO ES NETWORK ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_2_iot_accessvector_LOCAL*100)/cvssV2_IMPACT_score_2_iot)))+" % DE  VULNERABILIDADES EL VECTOR DE ACCESO ES LOCAL ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_2_iot_accessvector_PHYSICAL*100)/cvssV2_IMPACT_score_2_iot)))+" % DE  VULNERABILIDADES EL VECTOR DE ACCESO ES PHYSICAL ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_2_iot_accessvector_ADJACENT_NETWORK*100)/cvssV2_IMPACT_score_2_iot)))+" % DE  VULNERABILIDADES EL VECTOR DE ACCESO ES ADJACENT_NETWORK ")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_2_iot_accesscomplexity_HIGH*100)/cvssV2_IMPACT_score_2_iot)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES ALTA ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_2_iot_accesscomplexity_LOW*100)/cvssV2_IMPACT_score_2_iot)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES BAJA ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_2_iot_accesscomplexity_MEDIUM*100)/cvssV2_IMPACT_score_2_iot)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES MEDIA ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_2_iot_accesscomplexity_NONE*100)/cvssV2_IMPACT_score_2_iot)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ACCESO NO VIENE ESPECIFICADA ")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_2_iot_authentication_SINGLE*100)/cvssV2_IMPACT_score_2_iot)))+" % DE  VULNERABILIDADES SE REQUIERE AUTENTICACIÓN SENCILLA ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_2_iot_authentication_MULTIPLE*100)/cvssV2_IMPACT_score_2_iot)))+" % DE  VULNERABILIDADES SE REQUIERE AUTENTICACIÓN MÚLTIPLE")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_2_iot_authentication_NONE*100)/cvssV2_IMPACT_score_2_iot)))+" % DE  VULNERABILIDADES NO VIENE ESPECIFICADO SI SE REQUIERE AUTENTICACIÓN")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_2_iot_confidentialityImpact_COMPLETE*100)/cvssV2_IMPACT_score_2_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES COMPLETO ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_2_iot_confidentialityImpact_PARTIAL*100)/cvssV2_IMPACT_score_2_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES PARCIAL" )
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_2_iot_confidentialityImpact_NONE*100)/cvssV2_IMPACT_score_2_iot)))+" % DE  VULNERABILIDADES NO EXISTE IMPACTO DE CONFIDENCIALIDAD ")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_2_iot_integrityImpact_COMPLETE*100)/cvssV2_IMPACT_score_2_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES COMPLETO ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_2_iot_integrityImpact_PARTIAL*100)/cvssV2_IMPACT_score_2_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES PARCIAL" )
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_2_iot_integrityImpact_NONE*100)/cvssV2_IMPACT_score_2_iot)))+" % DE  VULNERABILIDADES NO EXISTE IMPACTO DE INTEGRIDAD ")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_2_iot_availabilityImpact_COMPLETE*100)/cvssV2_IMPACT_score_2_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES COMPLETO ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_2_iot_availabilityImpact_PARTIAL*100)/cvssV2_IMPACT_score_2_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES PARCIAL" )
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_2_iot_availabilityImpact_NONE*100)/cvssV2_IMPACT_score_2_iot)))+" % DE  VULNERABILIDADES NO EXISTE IMPACTO DE DISPONIBILIDAD ")
    print("\n")  
if(cvssV2_IMPACT_score_1_iot>0):
    print("      -    EN EL "+str(float(((cvssV2_IMPACT_score_1_iot*100)/len(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"]))))+" % DE  VULNERABILIDADES LA PUNTUACION DE IMPACTO ESTÁ ENTRE 1 Y 2. LOS PORCENTAJES DEL VECTOR STRING SON LOS SIGUIENTES:  \n")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_1_iot_accessvector_NETWORK*100)/cvssV2_IMPACT_score_1_iot)))+" % DE  VULNERABILIDADES EL VECTOR DE ACCESO ES NETWORK ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_1_iot_accessvector_LOCAL*100)/cvssV2_IMPACT_score_1_iot)))+" % DE  VULNERABILIDADES EL VECTOR DE ACCESO ES LOCAL ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_1_iot_accessvector_PHYSICAL*100)/cvssV2_IMPACT_score_1_iot)))+" % DE  VULNERABILIDADES EL VECTOR DE ACCESO ES PHYSICAL ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_1_iot_accessvector_ADJACENT_NETWORK*100)/cvssV2_IMPACT_score_1_iot)))+" % DE  VULNERABILIDADES EL VECTOR DE ACCESO ES ADJACENT_NETWORK ")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_1_iot_accesscomplexity_HIGH*100)/cvssV2_IMPACT_score_1_iot)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES ALTA ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_1_iot_accesscomplexity_LOW*100)/cvssV2_IMPACT_score_1_iot)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES BAJA ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_1_iot_accesscomplexity_MEDIUM*100)/cvssV2_IMPACT_score_1_iot)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES MEDIA ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_1_iot_accesscomplexity_NONE*100)/cvssV2_IMPACT_score_1_iot)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ACCESO NO VIENE ESPECIFICADA ")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_1_iot_authentication_SINGLE*100)/cvssV2_IMPACT_score_1_iot)))+" % DE  VULNERABILIDADES SE REQUIERE AUTENTICACIÓN SENCILLA ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_1_iot_authentication_MULTIPLE*100)/cvssV2_IMPACT_score_1_iot)))+" % DE  VULNERABILIDADES SE REQUIERE AUTENTICACIÓN MÚLTIPLE")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_1_iot_authentication_NONE*100)/cvssV2_IMPACT_score_1_iot)))+" % DE  VULNERABILIDADES NO VIENE ESPECIFICADO SI SE REQUIERE AUTENTICACIÓN")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_1_iot_confidentialityImpact_COMPLETE*100)/cvssV2_IMPACT_score_1_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES COMPLETO ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_1_iot_confidentialityImpact_PARTIAL*100)/cvssV2_IMPACT_score_1_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES PARCIAL" )
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_1_iot_confidentialityImpact_NONE*100)/cvssV2_IMPACT_score_1_iot)))+" % DE  VULNERABILIDADES NO EXISTE IMPACTO DE CONFIDENCIALIDAD ")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_1_iot_integrityImpact_COMPLETE*100)/cvssV2_IMPACT_score_1_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES COMPLETO ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_1_iot_integrityImpact_PARTIAL*100)/cvssV2_IMPACT_score_1_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES PARCIAL" )
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_1_iot_integrityImpact_NONE*100)/cvssV2_IMPACT_score_1_iot)))+" % DE  VULNERABILIDADES NO EXISTE IMPACTO DE INTEGRIDAD ")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_1_iot_availabilityImpact_COMPLETE*100)/cvssV2_IMPACT_score_1_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES COMPLETO ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_1_iot_availabilityImpact_PARTIAL*100)/cvssV2_IMPACT_score_1_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES PARCIAL" )
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_1_iot_availabilityImpact_NONE*100)/cvssV2_IMPACT_score_1_iot)))+" % DE  VULNERABILIDADES NO EXISTE IMPACTO DE DISPONIBILIDAD ")
    print("\n")   
if(cvssV2_IMPACT_score_0_iot):
    print("\n")
    print("      -    EN EL "+str(float(((cvssV2_IMPACT_score_0_iot*100)/len(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"]))))+" % DE  VULNERABILIDADES LA PUNTUACION DE IMPACTO ESTÁ ENTRE 0 Y 1. LOS PORCENTAJES DEL VECTOR STRING SON LOS SIGUIENTES:  \n")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_0_iot_accessvector_NETWORK*100)/cvssV2_IMPACT_score_0_iot)))+" % DE  VULNERABILIDADES EL VECTOR DE ACCESO ES NETWORK ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_0_iot_accessvector_LOCAL*100)/cvssV2_IMPACT_score_0_iot)))+" % DE  VULNERABILIDADES EL VECTOR DE ACCESO ES LOCAL ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_0_iot_accessvector_PHYSICAL*100)/cvssV2_IMPACT_score_0_iot)))+" % DE  VULNERABILIDADES EL VECTOR DE ACCESO ES PHYSICAL ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_0_iot_accessvector_ADJACENT_NETWORK*100)/cvssV2_IMPACT_score_0_iot)))+" % DE  VULNERABILIDADES EL VECTOR DE ACCESO ES ADJACENT_NETWORK ")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_0_iot_accesscomplexity_HIGH*100)/cvssV2_IMPACT_score_0_iot)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES ALTA ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_0_iot_accesscomplexity_LOW*100)/cvssV2_IMPACT_score_0_iot)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES BAJA ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_0_iot_accesscomplexity_MEDIUM*100)/cvssV2_IMPACT_score_0_iot)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES MEDIA ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_0_iot_accesscomplexity_NONE*100)/cvssV2_IMPACT_score_0_iot)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ACCESO NO VIENE ESPECIFICADA ")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_0_iot_authentication_SINGLE*100)/cvssV2_IMPACT_score_0_iot)))+" % DE  VULNERABILIDADES SE REQUIERE AUTENTICACIÓN SENCILLA ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_0_iot_authentication_MULTIPLE*100)/cvssV2_IMPACT_score_0_iot)))+" % DE  VULNERABILIDADES SE REQUIERE AUTENTICACIÓN MÚLTIPLE")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_0_iot_authentication_NONE*100)/cvssV2_IMPACT_score_0_iot)))+" % DE  VULNERABILIDADES NO VIENE ESPECIFICADO SI SE REQUIERE AUTENTICACIÓN")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_0_iot_confidentialityImpact_COMPLETE*100)/cvssV2_IMPACT_score_0_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES COMPLETO ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_0_iot_confidentialityImpact_PARTIAL*100)/cvssV2_IMPACT_score_0_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES PARCIAL" )
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_0_iot_confidentialityImpact_NONE*100)/cvssV2_IMPACT_score_0_iot)))+" % DE  VULNERABILIDADES NO EXISTE IMPACTO DE CONFIDENCIALIDAD ")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_0_iot_integrityImpact_COMPLETE*100)/cvssV2_IMPACT_score_0_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES COMPLETO ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_0_iot_integrityImpact_PARTIAL*100)/cvssV2_IMPACT_score_0_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES PARCIAL" )
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_0_iot_integrityImpact_NONE*100)/cvssV2_IMPACT_score_0_iot)))+" % DE  VULNERABILIDADES NO EXISTE IMPACTO DE INTEGRIDAD ")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_0_iot_availabilityImpact_COMPLETE*100)/cvssV2_IMPACT_score_0_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES COMPLETO ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_0_iot_availabilityImpact_PARTIAL*100)/cvssV2_IMPACT_score_0_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES PARCIAL" )
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_0_iot_availabilityImpact_NONE*100)/cvssV2_IMPACT_score_0_iot)))+" % DE  VULNERABILIDADES NO EXISTE IMPACTO DE DISPONIBILIDAD ")     
print("\n")
print("      -    EN EL "+str(float(((cvssV2_no_IMPACT_score_iot*100)/len(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"]))))+" % DE  VULNERABILIDADES LA PUNTUACION DE IMPACTO NO VIENE ESPECIFICADA. LOS PORCENTAJES DEL VECTOR STRING SON LOS SIGUIENTES:  \n")
print("\n")
print("            -    EN EL "+str(float(((cvssV2_no_IMPACT_score_iot_accessvector_NETWORK*100)/cvssV2_no_IMPACT_score_iot)))+" % DE  VULNERABILIDADES EL VECTOR DE ACCESO ES NETWORK ")
print("            -    EN EL "+str(float(((cvssV2_no_IMPACT_score_iot_accessvector_LOCAL*100)/cvssV2_no_IMPACT_score_iot)))+" % DE  VULNERABILIDADES EL VECTOR DE ACCESO ES LOCAL ")
print("            -    EN EL "+str(float(((cvssV2_no_IMPACT_score_iot_accessvector_PHYSICAL*100)/cvssV2_no_IMPACT_score_iot)))+" % DE  VULNERABILIDADES EL VECTOR DE ACCESO ES PHYSICAL ")
print("            -    EN EL "+str(float(((cvssV2_no_IMPACT_score_iot_accessvector_ADJACENT_NETWORK*100)/cvssV2_no_IMPACT_score_iot)))+" % DE  VULNERABILIDADES EL VECTOR DE ACCESO ES ADJACENT_NETWORK ")
print("\n")
print("            -    EN EL "+str(float(((cvssV2_no_IMPACT_score_iot_accesscomplexity_HIGH*100)/cvssV2_no_IMPACT_score_iot)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES ALTA ")
print("            -    EN EL "+str(float(((cvssV2_no_IMPACT_score_iot_accesscomplexity_LOW*100)/cvssV2_no_IMPACT_score_iot)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES BAJA ")
print("            -    EN EL "+str(float(((cvssV2_no_IMPACT_score_iot_accesscomplexity_MEDIUM*100)/cvssV2_no_IMPACT_score_iot)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES MEDIA ")
print("            -    EN EL "+str(float(((cvssV2_no_IMPACT_score_iot_accesscomplexity_NONE*100)/cvssV2_no_IMPACT_score_iot)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ACCESO NO VIENE ESPECIFICADA ")
print("\n")
print("            -    EN EL "+str(float(((cvssV2_no_IMPACT_score_iot_authentication_SINGLE*100)/cvssV2_no_IMPACT_score_iot)))+" % DE  VULNERABILIDADES SE REQUIERE AUTENTICACIÓN SENCILLA ")
print("            -    EN EL "+str(float(((cvssV2_no_IMPACT_score_iot_authentication_MULTIPLE*100)/cvssV2_no_IMPACT_score_iot)))+" % DE  VULNERABILIDADES SE REQUIERE AUTENTICACIÓN MÚLTIPLE")
print("            -    EN EL "+str(float(((cvssV2_no_IMPACT_score_iot_authentication_NONE*100)/cvssV2_no_IMPACT_score_iot)))+" % DE  VULNERABILIDADES NO VIENE ESPECIFICADO SI SE REQUIERE AUTENTICACIÓN")
print("\n")
print("            -    EN EL "+str(float(((cvssV2_no_IMPACT_score_iot_confidentialityImpact_COMPLETE*100)/cvssV2_no_IMPACT_score_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES COMPLETO ")
print("            -    EN EL "+str(float(((cvssV2_no_IMPACT_score_iot_confidentialityImpact_PARTIAL*100)/cvssV2_no_IMPACT_score_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES PARCIAL" )
print("            -    EN EL "+str(float(((cvssV2_no_IMPACT_score_iot_confidentialityImpact_NONE*100)/cvssV2_no_IMPACT_score_iot)))+" % DE  VULNERABILIDADES NO EXISTE IMPACTO DE CONFIDENCIALIDAD ")
print("\n")
print("            -    EN EL "+str(float(((cvssV2_no_IMPACT_score_iot_integrityImpact_COMPLETE*100)/cvssV2_no_IMPACT_score_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES COMPLETO ")
print("            -    EN EL "+str(float(((cvssV2_no_IMPACT_score_iot_integrityImpact_PARTIAL*100)/cvssV2_no_IMPACT_score_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES PARCIAL" )
print("            -    EN EL "+str(float(((cvssV2_no_IMPACT_score_iot_integrityImpact_NONE*100)/cvssV2_no_IMPACT_score_iot)))+" % DE  VULNERABILIDADES NO EXISTE IMPACTO DE INTEGRIDAD ")
print("\n")
print("            -    EN EL "+str(float(((cvssV2_no_IMPACT_score_iot_availabilityImpact_COMPLETE*100)/cvssV2_no_IMPACT_score_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES COMPLETO ")
print("            -    EN EL "+str(float(((cvssV2_no_IMPACT_score_iot_availabilityImpact_PARTIAL*100)/cvssV2_no_IMPACT_score_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES PARCIAL" )
print("            -    EN EL "+str(float(((cvssV2_no_IMPACT_score_iot_availabilityImpact_NONE*100)/cvssV2_no_IMPACT_score_iot)))+" % DE  VULNERABILIDADES NO EXISTE IMPACTO DE DISPONIBILIDAD ")
print("\n")       
            
            
        
            
       

    
    
    
# PUNTUACION DE IMPACTO 10
cvssV2_IMPACT_score_10_sh=0

cvssV2_IMPACT_score_10_sh_accessvector_NETWORK=0
cvssV2_IMPACT_score_10_sh_accessvector_PHYSICAL=0
cvssV2_IMPACT_score_10_sh_accessvector_LOCAL=0
cvssV2_IMPACT_score_10_sh_accessvector_ADJACENT_NETWORK=0

cvssV2_IMPACT_score_10_sh_accesscomplexity_HIGH=0
cvssV2_IMPACT_score_10_sh_accesscomplexity_LOW=0
cvssV2_IMPACT_score_10_sh_accesscomplexity_MEDIUM=0
cvssV2_IMPACT_score_10_sh_accesscomplexity_NONE=0

cvssV2_IMPACT_score_10_sh_authentication_SINGLE=0
cvssV2_IMPACT_score_10_sh_authentication_MULTIPLE=0
cvssV2_IMPACT_score_10_sh_authentication_NONE=0

cvssV2_IMPACT_score_10_sh_confidentialityImpact_COMPLETE=0
cvssV2_IMPACT_score_10_sh_confidentialityImpact_PARTIAL=0
cvssV2_IMPACT_score_10_sh_confidentialityImpact_NONE=0


cvssV2_IMPACT_score_10_sh_integrityImpact_COMPLETE=0
cvssV2_IMPACT_score_10_sh_integrityImpact_PARTIAL=0
cvssV2_IMPACT_score_10_sh_integrityImpact_NONE=0


cvssV2_IMPACT_score_10_sh_availabilityImpact_COMPLETE=0
cvssV2_IMPACT_score_10_sh_availabilityImpact_PARTIAL=0
cvssV2_IMPACT_score_10_sh_availabilityImpact_NONE=0


# PUNTUACION DE IMPACTO 9

cvssV2_IMPACT_score_9_sh=0

cvssV2_IMPACT_score_9_sh_accessvector_NETWORK=0
cvssV2_IMPACT_score_9_sh_accessvector_PHYSICAL=0
cvssV2_IMPACT_score_9_sh_accessvector_LOCAL=0
cvssV2_IMPACT_score_9_sh_accessvector_ADJACENT_NETWORK=0

cvssV2_IMPACT_score_9_sh_accesscomplexity_HIGH=0
cvssV2_IMPACT_score_9_sh_accesscomplexity_LOW=0
cvssV2_IMPACT_score_9_sh_accesscomplexity_MEDIUM=0
cvssV2_IMPACT_score_9_sh_accesscomplexity_NONE=0

cvssV2_IMPACT_score_9_sh_authentication_SINGLE=0
cvssV2_IMPACT_score_9_sh_authentication_MULTIPLE=0
cvssV2_IMPACT_score_9_sh_authentication_NONE=0

cvssV2_IMPACT_score_9_sh_confidentialityImpact_COMPLETE=0
cvssV2_IMPACT_score_9_sh_confidentialityImpact_PARTIAL=0
cvssV2_IMPACT_score_9_sh_confidentialityImpact_NONE=0


cvssV2_IMPACT_score_9_sh_integrityImpact_COMPLETE=0
cvssV2_IMPACT_score_9_sh_integrityImpact_PARTIAL=0
cvssV2_IMPACT_score_9_sh_integrityImpact_NONE=0


cvssV2_IMPACT_score_9_sh_availabilityImpact_COMPLETE=0
cvssV2_IMPACT_score_9_sh_availabilityImpact_PARTIAL=0
cvssV2_IMPACT_score_9_sh_availabilityImpact_NONE=0


# PUNTUACION DE IMPACTO 8

cvssV2_IMPACT_score_8_sh=0

cvssV2_IMPACT_score_8_sh_accessvector_NETWORK=0
cvssV2_IMPACT_score_8_sh_accessvector_PHYSICAL=0
cvssV2_IMPACT_score_8_sh_accessvector_LOCAL=0
cvssV2_IMPACT_score_8_sh_accessvector_ADJACENT_NETWORK=0

cvssV2_IMPACT_score_8_sh_accesscomplexity_HIGH=0
cvssV2_IMPACT_score_8_sh_accesscomplexity_LOW=0
cvssV2_IMPACT_score_8_sh_accesscomplexity_MEDIUM=0
cvssV2_IMPACT_score_8_sh_accesscomplexity_NONE=0

cvssV2_IMPACT_score_8_sh_authentication_SINGLE=0
cvssV2_IMPACT_score_8_sh_authentication_MULTIPLE=0
cvssV2_IMPACT_score_8_sh_authentication_NONE=0

cvssV2_IMPACT_score_8_sh_confidentialityImpact_COMPLETE=0
cvssV2_IMPACT_score_8_sh_confidentialityImpact_PARTIAL=0
cvssV2_IMPACT_score_8_sh_confidentialityImpact_NONE=0


cvssV2_IMPACT_score_8_sh_integrityImpact_COMPLETE=0
cvssV2_IMPACT_score_8_sh_integrityImpact_PARTIAL=0
cvssV2_IMPACT_score_8_sh_integrityImpact_NONE=0


cvssV2_IMPACT_score_8_sh_availabilityImpact_COMPLETE=0
cvssV2_IMPACT_score_8_sh_availabilityImpact_PARTIAL=0
cvssV2_IMPACT_score_8_sh_availabilityImpact_NONE=0


# PUNTUACION DE IMPACTO 7

cvssV2_IMPACT_score_7_sh=0

cvssV2_IMPACT_score_7_sh_accessvector_NETWORK=0
cvssV2_IMPACT_score_7_sh_accessvector_PHYSICAL=0
cvssV2_IMPACT_score_7_sh_accessvector_LOCAL=0
cvssV2_IMPACT_score_7_sh_accessvector_ADJACENT_NETWORK=0

cvssV2_IMPACT_score_7_sh_accesscomplexity_HIGH=0
cvssV2_IMPACT_score_7_sh_accesscomplexity_LOW=0
cvssV2_IMPACT_score_7_sh_accesscomplexity_MEDIUM=0
cvssV2_IMPACT_score_7_sh_accesscomplexity_NONE=0

cvssV2_IMPACT_score_7_sh_authentication_SINGLE=0
cvssV2_IMPACT_score_7_sh_authentication_MULTIPLE=0
cvssV2_IMPACT_score_7_sh_authentication_NONE=0

cvssV2_IMPACT_score_7_sh_confidentialityImpact_COMPLETE=0
cvssV2_IMPACT_score_7_sh_confidentialityImpact_PARTIAL=0
cvssV2_IMPACT_score_7_sh_confidentialityImpact_NONE=0


cvssV2_IMPACT_score_7_sh_integrityImpact_COMPLETE=0
cvssV2_IMPACT_score_7_sh_integrityImpact_PARTIAL=0
cvssV2_IMPACT_score_7_sh_integrityImpact_NONE=0


cvssV2_IMPACT_score_7_sh_availabilityImpact_COMPLETE=0
cvssV2_IMPACT_score_7_sh_availabilityImpact_PARTIAL=0
cvssV2_IMPACT_score_7_sh_availabilityImpact_NONE=0

# PUNTUACION DE IMPACTO 6

cvssV2_IMPACT_score_6_sh=0

cvssV2_IMPACT_score_6_sh_accessvector_NETWORK=0
cvssV2_IMPACT_score_6_sh_accessvector_PHYSICAL=0
cvssV2_IMPACT_score_6_sh_accessvector_LOCAL=0
cvssV2_IMPACT_score_6_sh_accessvector_ADJACENT_NETWORK=0

cvssV2_IMPACT_score_6_sh_accesscomplexity_HIGH=0
cvssV2_IMPACT_score_6_sh_accesscomplexity_LOW=0
cvssV2_IMPACT_score_6_sh_accesscomplexity_MEDIUM=0
cvssV2_IMPACT_score_6_sh_accesscomplexity_NONE=0

cvssV2_IMPACT_score_6_sh_authentication_SINGLE=0
cvssV2_IMPACT_score_6_sh_authentication_MULTIPLE=0
cvssV2_IMPACT_score_6_sh_authentication_NONE=0

cvssV2_IMPACT_score_6_sh_confidentialityImpact_COMPLETE=0
cvssV2_IMPACT_score_6_sh_confidentialityImpact_PARTIAL=0
cvssV2_IMPACT_score_6_sh_confidentialityImpact_NONE=0


cvssV2_IMPACT_score_6_sh_integrityImpact_COMPLETE=0
cvssV2_IMPACT_score_6_sh_integrityImpact_PARTIAL=0
cvssV2_IMPACT_score_6_sh_integrityImpact_NONE=0


cvssV2_IMPACT_score_6_sh_availabilityImpact_COMPLETE=0
cvssV2_IMPACT_score_6_sh_availabilityImpact_PARTIAL=0
cvssV2_IMPACT_score_6_sh_availabilityImpact_NONE=0


# PUNTUACION DE IMPACTO 5

cvssV2_IMPACT_score_5_sh=0

cvssV2_IMPACT_score_5_sh_accessvector_NETWORK=0
cvssV2_IMPACT_score_5_sh_accessvector_PHYSICAL=0
cvssV2_IMPACT_score_5_sh_accessvector_LOCAL=0
cvssV2_IMPACT_score_5_sh_accessvector_ADJACENT_NETWORK=0

cvssV2_IMPACT_score_5_sh_accesscomplexity_HIGH=0
cvssV2_IMPACT_score_5_sh_accesscomplexity_LOW=0
cvssV2_IMPACT_score_5_sh_accesscomplexity_MEDIUM=0
cvssV2_IMPACT_score_5_sh_accesscomplexity_NONE=0

cvssV2_IMPACT_score_5_sh_authentication_SINGLE=0
cvssV2_IMPACT_score_5_sh_authentication_MULTIPLE=0
cvssV2_IMPACT_score_5_sh_authentication_NONE=0

cvssV2_IMPACT_score_5_sh_confidentialityImpact_COMPLETE=0
cvssV2_IMPACT_score_5_sh_confidentialityImpact_PARTIAL=0
cvssV2_IMPACT_score_5_sh_confidentialityImpact_NONE=0


cvssV2_IMPACT_score_5_sh_integrityImpact_COMPLETE=0
cvssV2_IMPACT_score_5_sh_integrityImpact_PARTIAL=0
cvssV2_IMPACT_score_5_sh_integrityImpact_NONE=0


cvssV2_IMPACT_score_5_sh_availabilityImpact_COMPLETE=0
cvssV2_IMPACT_score_5_sh_availabilityImpact_PARTIAL=0
cvssV2_IMPACT_score_5_sh_availabilityImpact_NONE=0



# PUNTUACION DE IMPACTO 4
cvssV2_IMPACT_score_4_sh=0

cvssV2_IMPACT_score_4_sh_accessvector_NETWORK=0
cvssV2_IMPACT_score_4_sh_accessvector_PHYSICAL=0
cvssV2_IMPACT_score_4_sh_accessvector_LOCAL=0
cvssV2_IMPACT_score_4_sh_accessvector_ADJACENT_NETWORK=0

cvssV2_IMPACT_score_4_sh_accesscomplexity_HIGH=0
cvssV2_IMPACT_score_4_sh_accesscomplexity_LOW=0
cvssV2_IMPACT_score_4_sh_accesscomplexity_MEDIUM=0
cvssV2_IMPACT_score_4_sh_accesscomplexity_NONE=0

cvssV2_IMPACT_score_4_sh_authentication_SINGLE=0
cvssV2_IMPACT_score_4_sh_authentication_MULTIPLE=0
cvssV2_IMPACT_score_4_sh_authentication_NONE=0

cvssV2_IMPACT_score_4_sh_confidentialityImpact_COMPLETE=0
cvssV2_IMPACT_score_4_sh_confidentialityImpact_PARTIAL=0
cvssV2_IMPACT_score_4_sh_confidentialityImpact_NONE=0


cvssV2_IMPACT_score_4_sh_integrityImpact_COMPLETE=0
cvssV2_IMPACT_score_4_sh_integrityImpact_PARTIAL=0
cvssV2_IMPACT_score_4_sh_integrityImpact_NONE=0


cvssV2_IMPACT_score_4_sh_availabilityImpact_COMPLETE=0
cvssV2_IMPACT_score_4_sh_availabilityImpact_PARTIAL=0
cvssV2_IMPACT_score_4_sh_availabilityImpact_NONE=0

# PUNTUACION DE IMPACTO 3

cvssV2_IMPACT_score_3_sh=0

cvssV2_IMPACT_score_3_sh_accessvector_NETWORK=0
cvssV2_IMPACT_score_3_sh_accessvector_PHYSICAL=0
cvssV2_IMPACT_score_3_sh_accessvector_LOCAL=0
cvssV2_IMPACT_score_3_sh_accessvector_ADJACENT_NETWORK=0

cvssV2_IMPACT_score_3_sh_accesscomplexity_HIGH=0
cvssV2_IMPACT_score_3_sh_accesscomplexity_LOW=0
cvssV2_IMPACT_score_3_sh_accesscomplexity_MEDIUM=0
cvssV2_IMPACT_score_3_sh_accesscomplexity_NONE=0

cvssV2_IMPACT_score_3_sh_authentication_SINGLE=0
cvssV2_IMPACT_score_3_sh_authentication_MULTIPLE=0
cvssV2_IMPACT_score_3_sh_authentication_NONE=0

cvssV2_IMPACT_score_3_sh_confidentialityImpact_COMPLETE=0
cvssV2_IMPACT_score_3_sh_confidentialityImpact_PARTIAL=0
cvssV2_IMPACT_score_3_sh_confidentialityImpact_NONE=0


cvssV2_IMPACT_score_3_sh_integrityImpact_COMPLETE=0
cvssV2_IMPACT_score_3_sh_integrityImpact_PARTIAL=0
cvssV2_IMPACT_score_3_sh_integrityImpact_NONE=0


cvssV2_IMPACT_score_3_sh_availabilityImpact_COMPLETE=0
cvssV2_IMPACT_score_3_sh_availabilityImpact_PARTIAL=0
cvssV2_IMPACT_score_3_sh_availabilityImpact_NONE=0


# PUNTUACION DE IMPACTO 2

cvssV2_IMPACT_score_2_sh=0

cvssV2_IMPACT_score_2_sh_accessvector_NETWORK=0
cvssV2_IMPACT_score_2_sh_accessvector_PHYSICAL=0
cvssV2_IMPACT_score_2_sh_accessvector_LOCAL=0
cvssV2_IMPACT_score_2_sh_accessvector_ADJACENT_NETWORK=0

cvssV2_IMPACT_score_2_sh_accesscomplexity_HIGH=0
cvssV2_IMPACT_score_2_sh_accesscomplexity_LOW=0
cvssV2_IMPACT_score_2_sh_accesscomplexity_MEDIUM=0
cvssV2_IMPACT_score_2_sh_accesscomplexity_NONE=0

cvssV2_IMPACT_score_2_sh_authentication_SINGLE=0
cvssV2_IMPACT_score_2_sh_authentication_MULTIPLE=0
cvssV2_IMPACT_score_2_sh_authentication_NONE=0

cvssV2_IMPACT_score_2_sh_confidentialityImpact_COMPLETE=0
cvssV2_IMPACT_score_2_sh_confidentialityImpact_PARTIAL=0
cvssV2_IMPACT_score_2_sh_confidentialityImpact_NONE=0


cvssV2_IMPACT_score_2_sh_integrityImpact_COMPLETE=0
cvssV2_IMPACT_score_2_sh_integrityImpact_PARTIAL=0
cvssV2_IMPACT_score_2_sh_integrityImpact_NONE=0


cvssV2_IMPACT_score_2_sh_availabilityImpact_COMPLETE=0
cvssV2_IMPACT_score_2_sh_availabilityImpact_PARTIAL=0
cvssV2_IMPACT_score_2_sh_availabilityImpact_NONE=0

# PUNTUACION DE IMPACTO 1

cvssV2_IMPACT_score_1_sh=0

cvssV2_IMPACT_score_1_sh_accessvector_NETWORK=0
cvssV2_IMPACT_score_1_sh_accessvector_PHYSICAL=0
cvssV2_IMPACT_score_1_sh_accessvector_LOCAL=0
cvssV2_IMPACT_score_1_sh_accessvector_ADJACENT_NETWORK=0

cvssV2_IMPACT_score_1_sh_accesscomplexity_HIGH=0
cvssV2_IMPACT_score_1_sh_accesscomplexity_LOW=0
cvssV2_IMPACT_score_1_sh_accesscomplexity_MEDIUM=0
cvssV2_IMPACT_score_1_sh_accesscomplexity_NONE=0

cvssV2_IMPACT_score_1_sh_authentication_SINGLE=0
cvssV2_IMPACT_score_1_sh_authentication_MULTIPLE=0
cvssV2_IMPACT_score_1_sh_authentication_NONE=0

cvssV2_IMPACT_score_1_sh_confidentialityImpact_COMPLETE=0
cvssV2_IMPACT_score_1_sh_confidentialityImpact_PARTIAL=0
cvssV2_IMPACT_score_1_sh_confidentialityImpact_NONE=0


cvssV2_IMPACT_score_1_sh_integrityImpact_COMPLETE=0
cvssV2_IMPACT_score_1_sh_integrityImpact_PARTIAL=0
cvssV2_IMPACT_score_1_sh_integrityImpact_NONE=0


cvssV2_IMPACT_score_1_sh_availabilityImpact_COMPLETE=0
cvssV2_IMPACT_score_1_sh_availabilityImpact_PARTIAL=0
cvssV2_IMPACT_score_1_sh_availabilityImpact_NONE=0

# PUNTUACION DE IMPACTO 0

cvssV2_IMPACT_score_0_sh=0

cvssV2_IMPACT_score_0_sh_accessvector_NETWORK=0
cvssV2_IMPACT_score_0_sh_accessvector_PHYSICAL=0
cvssV2_IMPACT_score_0_sh_accessvector_LOCAL=0
cvssV2_IMPACT_score_0_sh_accessvector_ADJACENT_NETWORK=0

cvssV2_IMPACT_score_0_sh_accesscomplexity_HIGH=0
cvssV2_IMPACT_score_0_sh_accesscomplexity_LOW=0
cvssV2_IMPACT_score_0_sh_accesscomplexity_MEDIUM=0
cvssV2_IMPACT_score_0_sh_accesscomplexity_NONE=0

cvssV2_IMPACT_score_0_sh_authentication_SINGLE=0
cvssV2_IMPACT_score_0_sh_authentication_MULTIPLE=0
cvssV2_IMPACT_score_0_sh_authentication_NONE=0

cvssV2_IMPACT_score_0_sh_confidentialityImpact_COMPLETE=0
cvssV2_IMPACT_score_0_sh_confidentialityImpact_PARTIAL=0
cvssV2_IMPACT_score_0_sh_confidentialityImpact_NONE=0


cvssV2_IMPACT_score_0_sh_integrityImpact_COMPLETE=0
cvssV2_IMPACT_score_0_sh_integrityImpact_PARTIAL=0
cvssV2_IMPACT_score_0_sh_integrityImpact_NONE=0


cvssV2_IMPACT_score_0_sh_availabilityImpact_COMPLETE=0
cvssV2_IMPACT_score_0_sh_availabilityImpact_PARTIAL=0
cvssV2_IMPACT_score_0_sh_availabilityImpact_NONE=0


# NO PUNTUACION DE IMPACTO

cvssV2_no_IMPACT_score_sh=0

cvssV2_no_IMPACT_score_sh_accessvector_NETWORK=0
cvssV2_no_IMPACT_score_sh_accessvector_PHYSICAL=0
cvssV2_no_IMPACT_score_sh_accessvector_LOCAL=0
cvssV2_no_IMPACT_score_sh_accessvector_ADJACENT_NETWORK=0

cvssV2_no_IMPACT_score_sh_accesscomplexity_HIGH=0
cvssV2_no_IMPACT_score_sh_accesscomplexity_LOW=0
cvssV2_no_IMPACT_score_sh_accesscomplexity_MEDIUM=0
cvssV2_no_IMPACT_score_sh_accesscomplexity_NONE=0

cvssV2_no_IMPACT_score_sh_authentication_SINGLE=0
cvssV2_no_IMPACT_score_sh_authentication_MULTIPLE=0
cvssV2_no_IMPACT_score_sh_authentication_NONE=0

cvssV2_no_IMPACT_score_sh_confidentialityImpact_COMPLETE=0
cvssV2_no_IMPACT_score_sh_confidentialityImpact_PARTIAL=0
cvssV2_no_IMPACT_score_sh_confidentialityImpact_NONE=0


cvssV2_no_IMPACT_score_sh_integrityImpact_COMPLETE=0
cvssV2_no_IMPACT_score_sh_integrityImpact_PARTIAL=0
cvssV2_no_IMPACT_score_sh_integrityImpact_NONE=0


cvssV2_no_IMPACT_score_sh_availabilityImpact_COMPLETE=0
cvssV2_no_IMPACT_score_sh_availabilityImpact_PARTIAL=0
cvssV2_no_IMPACT_score_sh_availabilityImpact_NONE=0

#Compruebo la PUNTUACION DE IMPACTO CVE CVSS3 para SMART HOME

for j in range(0,len(df_cve_sh["CVE_Items.impact.baseMetricV2.impactScore"])):
    
    if(df_cve_sh["CVE_Items.impact.baseMetricV2.impactScore"][j] =='NONE'):
        cvssV2_no_IMPACT_score_sh+=1  
        if(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.accessVector"][j]=='NETWORK'):
            cvssV2_no_IMPACT_score_sh_accessvector_NETWORK+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.accessVector"][j]=='LOCAL'):
            cvssV2_no_IMPACT_score_sh_accessvector_LOCAL+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.accessVector"][j]=='PHYSICAL'):
            cvssV2_no_IMPACT_score_sh_accessvector_PHYSICAL+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.accessVector"][j]=='ADJACENT_NETWORK'):
            cvssV2_no_IMPACT_score_sh_accessvector_ADJACENT_NETWORK+=1
            
        if(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.accessComplexity"][j]=='HIGH'):
            cvssV2_no_IMPACT_score_sh_accesscomplexity_HIGH+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.accessComplexity"][j]=='LOW'):
            cvssV2_no_IMPACT_score_sh_accesscomplexity_LOW+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.accessComplexity"][j]=='MEDIUM'):
            cvssV2_no_IMPACT_score_sh_accesscomplexity_MEDIUM+=1
        else:
            cvssV2_no_IMPACT_score_sh_accesscomplexity_NONE+=1  
                
        if(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.authentication"][j]=="SINGLE"):
            cvssV2_no_IMPACT_score_sh_authentication_SINGLE+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.authentication"][j]=="MULTIPLE"):
            cvssV2_no_IMPACT_score_sh_authentication_MULTIPLE+=1
        else:
            cvssV2_no_IMPACT_score_sh_authentication_NONE+=1
                
        if(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.confidentialityImpact"][j]=='COMPLETE'):
            cvssV2_no_IMPACT_score_sh_confidentialityImpact_COMPLETE+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.confidentialityImpact"][j]=='PARTIAL'):
            cvssV2_no_IMPACT_score_sh_confidentialityImpact_PARTIAL+=1
        else:
            cvssV2_no_IMPACT_score_sh_confidentialityImpact_NONE+=1 
            
            
        if(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.integrityImpact"][j]=='COMPLETE'):
            cvssV2_no_IMPACT_score_sh_integrityImpact_COMPLETE+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.integrityImpact"][j]=='PARTIAL'):
            cvssV2_no_IMPACT_score_sh_integrityImpact_PARTIAL+=1
        else:
            cvssV2_no_IMPACT_score_sh_integrityImpact_NONE+=1    
            
          
        if(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.availabilityImpact"][j]=='COMPLETE'):
            cvssV2_no_IMPACT_score_sh_availabilityImpact_COMPLETE+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.availabilityImpact"][j]=='PARTIAL'):
            cvssV2_no_IMPACT_score_sh_availabilityImpact_PARTIAL+=1
        else:
            cvssV2_no_IMPACT_score_sh_availabilityImpact_NONE+=1
    
    elif(((float(df_cve_sh["CVE_Items.impact.baseMetricV2.impactScore"][j])) < 10.0) and ((float(df_cve_sh["CVE_Items.impact.baseMetricV2.impactScore"][j])) >=9.0)):
        cvssV2_IMPACT_score_9_sh+=1  
        if(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.accessVector"][j]=='NETWORK'):
            cvssV2_IMPACT_score_9_sh_accessvector_NETWORK+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.accessVector"][j]=='LOCAL'):
            cvssV2_IMPACT_score_9_sh_accessvector_LOCAL+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.accessVector"][j]=='PHYSICAL'):
            cvssV2_IMPACT_score_9_sh_accessvector_PHYSICAL+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.accessVector"][j]=='ADJACENT_NETWORK'):
            cvssV2_IMPACT_score_9_sh_accessvector_ADJACENT_NETWORK+=1
            
        if(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.accessComplexity"][j]=='HIGH'):
            cvssV2_IMPACT_score_9_sh_accesscomplexity_HIGH+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.accessComplexity"][j]=='LOW'):
            cvssV2_IMPACT_score_9_sh_accesscomplexity_LOW+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.accessComplexity"][j]=='MEDIUM'):
            cvssV2_IMPACT_score_9_sh_accesscomplexity_MEDIUM+=1
        else:
            cvssV2_IMPACT_score_9_sh_accesscomplexity_NONE+=1  
                
        if(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.authentication"][j]=="SINGLE"):
            cvssV2_IMPACT_score_9_sh_authentication_SINGLE+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.authentication"][j]=="MULTIPLE"):
            cvssV2_IMPACT_score_9_sh_authentication_MULTIPLE+=1
        else:
            cvssV2_IMPACT_score_9_sh_authentication_NONE+=1
                
        if(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.confidentialityImpact"][j]=='COMPLETE'):
            cvssV2_IMPACT_score_9_sh_confidentialityImpact_COMPLETE+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.confidentialityImpact"][j]=='PARTIAL'):
            cvssV2_IMPACT_score_9_sh_confidentialityImpact_PARTIAL+=1
        else:
            cvssV2_IMPACT_score_9_sh_confidentialityImpact_NONE+=1 
            
            
        if(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.integrityImpact"][j]=='COMPLETE'):
            cvssV2_IMPACT_score_9_sh_integrityImpact_COMPLETE+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.integrityImpact"][j]=='PARTIAL'):
            cvssV2_IMPACT_score_9_sh_integrityImpact_PARTIAL+=1
        else:
            cvssV2_IMPACT_score_9_sh_integrityImpact_NONE+=1    
            
          
        if(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.availabilityImpact"][j]=='COMPLETE'):
            cvssV2_IMPACT_score_9_sh_availabilityImpact_COMPLETE+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.availabilityImpact"][j]=='PARTIAL'):
            cvssV2_IMPACT_score_9_sh_availabilityImpact_PARTIAL+=1
        else:
            cvssV2_IMPACT_score_9_sh_availabilityImpact_NONE+=1
        
            
    elif(((float(df_cve_sh["CVE_Items.impact.baseMetricV2.impactScore"][j])) < 9.0) and ((float(df_cve_sh["CVE_Items.impact.baseMetricV2.impactScore"][j])) >=8.0)):
        cvssV2_IMPACT_score_8_sh+=1   
        if(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.accessVector"][j]=='NETWORK'):
            cvssV2_IMPACT_score_8_sh_accessvector_NETWORK+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.accessVector"][j]=='LOCAL'):
            cvssV2_IMPACT_score_8_sh_accessvector_LOCAL+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.accessVector"][j]=='PHYSICAL'):
            cvssV2_IMPACT_score_8_sh_accessvector_PHYSICAL+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.accessVector"][j]=='ADJACENT_NETWORK'):
            cvssV2_IMPACT_score_8_sh_accessvector_ADJACENT_NETWORK+=1
            
        if(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.accessComplexity"][j]=='HIGH'):
            cvssV2_IMPACT_score_8_sh_accesscomplexity_HIGH+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.accessComplexity"][j]=='LOW'):
            cvssV2_IMPACT_score_8_sh_accesscomplexity_LOW+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.accessComplexity"][j]=='MEDIUM'):
            cvssV2_IMPACT_score_8_sh_accesscomplexity_MEDIUM+=1
        else:
            cvssV2_IMPACT_score_8_sh_accesscomplexity_NONE+=1  
                
        if(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.authentication"][j]=="SINGLE"):
            cvssV2_IMPACT_score_8_sh_authentication_SINGLE+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.authentication"][j]=="MULTIPLE"):
            cvssV2_IMPACT_score_8_sh_authentication_MULTIPLE+=1
        else:
            cvssV2_IMPACT_score_8_sh_authentication_NONE+=1
                
        if(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.confidentialityImpact"][j]=='COMPLETE'):
            cvssV2_IMPACT_score_8_sh_confidentialityImpact_COMPLETE+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.confidentialityImpact"][j]=='PARTIAL'):
            cvssV2_IMPACT_score_8_sh_confidentialityImpact_PARTIAL+=1
        else:
            cvssV2_IMPACT_score_8_sh_confidentialityImpact_NONE+=1 
            
            
        if(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.integrityImpact"][j]=='COMPLETE'):
            cvssV2_IMPACT_score_8_sh_integrityImpact_COMPLETE+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.integrityImpact"][j]=='PARTIAL'):
            cvssV2_IMPACT_score_8_sh_integrityImpact_PARTIAL+=1
        else:
            cvssV2_IMPACT_score_8_sh_integrityImpact_NONE+=1    
            
          
        if(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.availabilityImpact"][j]=='COMPLETE'):
            cvssV2_IMPACT_score_8_sh_availabilityImpact_COMPLETE+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.availabilityImpact"][j]=='PARTIAL'):
            cvssV2_IMPACT_score_8_sh_availabilityImpact_PARTIAL+=1
        else:
            cvssV2_IMPACT_score_8_sh_availabilityImpact_NONE+=1
           

            
    elif(((float(df_cve_sh["CVE_Items.impact.baseMetricV2.impactScore"][j])) < 8.0) and ((float(df_cve_sh["CVE_Items.impact.baseMetricV2.impactScore"][j])) >=7.0)):
        cvssV2_IMPACT_score_7_sh+=1  
        if(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.accessVector"][j]=='NETWORK'):
            cvssV2_IMPACT_score_7_sh_accessvector_NETWORK+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.accessVector"][j]=='LOCAL'):
            cvssV2_IMPACT_score_7_sh_accessvector_LOCAL+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.accessVector"][j]=='PHYSICAL'):
            cvssV2_IMPACT_score_7_sh_accessvector_PHYSICAL+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.accessVector"][j]=='ADJACENT_NETWORK'):
            cvssV2_IMPACT_score_7_sh_accessvector_ADJACENT_NETWORK+=1
            
        if(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.accessComplexity"][j]=='HIGH'):
            cvssV2_IMPACT_score_7_sh_accesscomplexity_HIGH+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.accessComplexity"][j]=='LOW'):
            cvssV2_IMPACT_score_7_sh_accesscomplexity_LOW+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.accessComplexity"][j]=='MEDIUM'):
            cvssV2_IMPACT_score_7_sh_accesscomplexity_MEDIUM+=1
        else:
            cvssV2_IMPACT_score_7_sh_accesscomplexity_NONE+=1  
                
        if(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.authentication"][j]=="SINGLE"):
            cvssV2_IMPACT_score_7_sh_authentication_SINGLE+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.authentication"][j]=="MULTIPLE"):
            cvssV2_IMPACT_score_7_sh_authentication_MULTIPLE+=1
        else:
            cvssV2_IMPACT_score_7_sh_authentication_NONE+=1
                
        if(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.confidentialityImpact"][j]=='COMPLETE'):
            cvssV2_IMPACT_score_7_sh_confidentialityImpact_COMPLETE+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.confidentialityImpact"][j]=='PARTIAL'):
            cvssV2_IMPACT_score_7_sh_confidentialityImpact_PARTIAL+=1
        else:
            cvssV2_IMPACT_score_7_sh_confidentialityImpact_NONE+=1 
            
            
        if(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.integrityImpact"][j]=='COMPLETE'):
            cvssV2_IMPACT_score_7_sh_integrityImpact_COMPLETE+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.integrityImpact"][j]=='PARTIAL'):
            cvssV2_IMPACT_score_7_sh_integrityImpact_PARTIAL+=1
        else:
            cvssV2_IMPACT_score_7_sh_integrityImpact_NONE+=1    
            
          
        if(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.availabilityImpact"][j]=='COMPLETE'):
            cvssV2_IMPACT_score_7_sh_availabilityImpact_COMPLETE+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.availabilityImpact"][j]=='PARTIAL'):
            cvssV2_IMPACT_score_7_sh_availabilityImpact_PARTIAL+=1
        else:
            cvssV2_IMPACT_score_7_sh_availabilityImpact_NONE+=1   
        

    elif(((float(df_cve_sh["CVE_Items.impact.baseMetricV2.impactScore"][j])) < 7.0) and ((float(df_cve_sh["CVE_Items.impact.baseMetricV2.impactScore"][j])) >=6.0)):
        cvssV2_IMPACT_score_6_sh+=1  
        if(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.accessVector"][j]=='NETWORK'):
            cvssV2_IMPACT_score_6_sh_accessvector_NETWORK+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.accessVector"][j]=='LOCAL'):
            cvssV2_IMPACT_score_6_sh_accessvector_LOCAL+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.accessVector"][j]=='PHYSICAL'):
            cvssV2_IMPACT_score_6_sh_accessvector_PHYSICAL+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.accessVector"][j]=='ADJACENT_NETWORK'):
            cvssV2_IMPACT_score_6_sh_accessvector_ADJACENT_NETWORK+=1
            
        if(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.accessComplexity"][j]=='HIGH'):
            cvssV2_IMPACT_score_6_sh_accesscomplexity_HIGH+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.accessComplexity"][j]=='LOW'):
            cvssV2_IMPACT_score_6_sh_accesscomplexity_LOW+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.accessComplexity"][j]=='MEDIUM'):
            cvssV2_IMPACT_score_6_sh_accesscomplexity_MEDIUM+=1
        else:
            cvssV2_IMPACT_score_6_sh_accesscomplexity_NONE+=1  
                
        if(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.authentication"][j]=="SINGLE"):
            cvssV2_IMPACT_score_6_sh_authentication_SINGLE+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.authentication"][j]=="MULTIPLE"):
            cvssV2_IMPACT_score_6_sh_authentication_MULTIPLE+=1
        else:
            cvssV2_IMPACT_score_6_sh_authentication_NONE+=1
                
        if(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.confidentialityImpact"][j]=='COMPLETE'):
            cvssV2_IMPACT_score_6_sh_confidentialityImpact_COMPLETE+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.confidentialityImpact"][j]=='PARTIAL'):
            cvssV2_IMPACT_score_6_sh_confidentialityImpact_PARTIAL+=1
        else:
            cvssV2_IMPACT_score_6_sh_confidentialityImpact_NONE+=1 
            
            
        if(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.integrityImpact"][j]=='COMPLETE'):
            cvssV2_IMPACT_score_6_sh_integrityImpact_COMPLETE+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.integrityImpact"][j]=='PARTIAL'):
            cvssV2_IMPACT_score_6_sh_integrityImpact_PARTIAL+=1
        else:
            cvssV2_IMPACT_score_6_sh_integrityImpact_NONE+=1    
            
          
        if(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.availabilityImpact"][j]=='COMPLETE'):
            cvssV2_IMPACT_score_6_sh_availabilityImpact_COMPLETE+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.availabilityImpact"][j]=='PARTIAL'):
            cvssV2_IMPACT_score_6_sh_availabilityImpact_PARTIAL+=1
        else:
            cvssV2_IMPACT_score_6_sh_availabilityImpact_NONE+=1  
            
            
            
    elif(((float(df_cve_sh["CVE_Items.impact.baseMetricV2.impactScore"][j])) < 6.0) and ((float(df_cve_sh["CVE_Items.impact.baseMetricV2.impactScore"][j])) >=5.0)):
        cvssV2_IMPACT_score_5_sh+=1   
        if(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.accessVector"][j]=='NETWORK'):
            cvssV2_IMPACT_score_5_sh_accessvector_NETWORK+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.accessVector"][j]=='LOCAL'):
            cvssV2_IMPACT_score_5_sh_accessvector_LOCAL+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.accessVector"][j]=='PHYSICAL'):
            cvssV2_IMPACT_score_5_sh_accessvector_PHYSICAL+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.accessVector"][j]=='ADJACENT_NETWORK'):
            cvssV2_IMPACT_score_5_sh_accessvector_ADJACENT_NETWORK+=1
            
        if(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.accessComplexity"][j]=='HIGH'):
            cvssV2_IMPACT_score_5_sh_accesscomplexity_HIGH+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.accessComplexity"][j]=='LOW'):
            cvssV2_IMPACT_score_5_sh_accesscomplexity_LOW+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.accessComplexity"][j]=='MEDIUM'):
            cvssV2_IMPACT_score_5_sh_accesscomplexity_MEDIUM+=1
        else:
            cvssV2_IMPACT_score_5_sh_accesscomplexity_NONE+=1  
                
        if(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.authentication"][j]=="SINGLE"):
            cvssV2_IMPACT_score_5_sh_authentication_SINGLE+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.authentication"][j]=="MULTIPLE"):
            cvssV2_IMPACT_score_5_sh_authentication_MULTIPLE+=1
        else:
            cvssV2_IMPACT_score_5_sh_authentication_NONE+=1
                
        if(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.confidentialityImpact"][j]=='COMPLETE'):
            cvssV2_IMPACT_score_5_sh_confidentialityImpact_COMPLETE+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.confidentialityImpact"][j]=='PARTIAL'):
            cvssV2_IMPACT_score_5_sh_confidentialityImpact_PARTIAL+=1
        else:
            cvssV2_IMPACT_score_5_sh_confidentialityImpact_NONE+=1 
            
            
        if(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.integrityImpact"][j]=='COMPLETE'):
            cvssV2_IMPACT_score_5_sh_integrityImpact_COMPLETE+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.integrityImpact"][j]=='PARTIAL'):
            cvssV2_IMPACT_score_5_sh_integrityImpact_PARTIAL+=1
        else:
            cvssV2_IMPACT_score_5_sh_integrityImpact_NONE+=1    
            
          
        if(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.availabilityImpact"][j]=='COMPLETE'):
            cvssV2_IMPACT_score_5_sh_availabilityImpact_COMPLETE+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.availabilityImpact"][j]=='PARTIAL'):
            cvssV2_IMPACT_score_5_sh_availabilityImpact_PARTIAL+=1
        else:
            cvssV2_IMPACT_score_5_sh_availabilityImpact_NONE+=1

    elif(((float(df_cve_sh["CVE_Items.impact.baseMetricV2.impactScore"][j])) < 5.0) and ((float(df_cve_sh["CVE_Items.impact.baseMetricV2.impactScore"][j])) >=4.0)):
        cvssV2_IMPACT_score_4_sh+=1  
        if(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.accessVector"][j]=='NETWORK'):
            cvssV2_IMPACT_score_4_sh_accessvector_NETWORK+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.accessVector"][j]=='LOCAL'):
            cvssV2_IMPACT_score_4_sh_accessvector_LOCAL+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.accessVector"][j]=='PHYSICAL'):
            cvssV2_IMPACT_score_4_sh_accessvector_PHYSICAL+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.accessVector"][j]=='ADJACENT_NETWORK'):
            cvssV2_IMPACT_score_4_sh_accessvector_ADJACENT_NETWORK+=1
            
        if(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.accessComplexity"][j]=='HIGH'):
            cvssV2_IMPACT_score_4_sh_accesscomplexity_HIGH+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.accessComplexity"][j]=='LOW'):
            cvssV2_IMPACT_score_4_sh_accesscomplexity_LOW+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.accessComplexity"][j]=='MEDIUM'):
            cvssV2_IMPACT_score_4_sh_accesscomplexity_MEDIUM+=1
        else:
            cvssV2_IMPACT_score_4_sh_accesscomplexity_NONE+=1  
                
        if(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.authentication"][j]=="SINGLE"):
            cvssV2_IMPACT_score_4_sh_authentication_SINGLE+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.authentication"][j]=="MULTIPLE"):
            cvssV2_IMPACT_score_4_sh_authentication_MULTIPLE+=1
        else:
            cvssV2_IMPACT_score_4_sh_authentication_NONE+=1
                
        if(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.confidentialityImpact"][j]=='COMPLETE'):
            cvssV2_IMPACT_score_4_sh_confidentialityImpact_COMPLETE+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.confidentialityImpact"][j]=='PARTIAL'):
            cvssV2_IMPACT_score_4_sh_confidentialityImpact_PARTIAL+=1
        else:
            cvssV2_IMPACT_score_4_sh_confidentialityImpact_NONE+=1 
            
            
        if(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.integrityImpact"][j]=='COMPLETE'):
            cvssV2_IMPACT_score_4_sh_integrityImpact_COMPLETE+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.integrityImpact"][j]=='PARTIAL'):
            cvssV2_IMPACT_score_4_sh_integrityImpact_PARTIAL+=1
        else:
            cvssV2_IMPACT_score_4_sh_integrityImpact_NONE+=1    
            
          
        if(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.availabilityImpact"][j]=='COMPLETE'):
            cvssV2_IMPACT_score_4_sh_availabilityImpact_COMPLETE+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.availabilityImpact"][j]=='PARTIAL'):
            cvssV2_IMPACT_score_4_sh_availabilityImpact_PARTIAL+=1
        else:
            cvssV2_IMPACT_score_4_sh_availabilityImpact_NONE+=1

    elif(((float(df_cve_sh["CVE_Items.impact.baseMetricV2.impactScore"][j])) < 4.0) and ((float(df_cve_sh["CVE_Items.impact.baseMetricV2.impactScore"][j])) >=3.0)):
        cvssV2_IMPACT_score_3_sh+=1   
        if(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.accessVector"][j]=='NETWORK'):
            cvssV2_IMPACT_score_3_sh_accessvector_NETWORK+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.accessVector"][j]=='LOCAL'):
            cvssV2_IMPACT_score_3_sh_accessvector_LOCAL+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.accessVector"][j]=='PHYSICAL'):
            cvssV2_IMPACT_score_3_sh_accessvector_PHYSICAL+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.accessVector"][j]=='ADJACENT_NETWORK'):
            cvssV2_IMPACT_score_3_sh_accessvector_ADJACENT_NETWORK+=1
            
        if(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.accessComplexity"][j]=='HIGH'):
            cvssV2_IMPACT_score_3_sh_accesscomplexity_HIGH+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.accessComplexity"][j]=='LOW'):
            cvssV2_IMPACT_score_3_sh_accesscomplexity_LOW+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.accessComplexity"][j]=='MEDIUM'):
            cvssV2_IMPACT_score_3_sh_accesscomplexity_MEDIUM+=1
        else:
            cvssV2_IMPACT_score_3_sh_accesscomplexity_NONE+=1  
                
        if(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.authentication"][j]=="SINGLE"):
            cvssV2_IMPACT_score_3_sh_authentication_SINGLE+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.authentication"][j]=="MULTIPLE"):
            cvssV2_IMPACT_score_3_sh_authentication_MULTIPLE+=1
        else:
            cvssV2_IMPACT_score_3_sh_authentication_NONE+=1
                
        if(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.confidentialityImpact"][j]=='COMPLETE'):
            cvssV2_IMPACT_score_3_sh_confidentialityImpact_COMPLETE+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.confidentialityImpact"][j]=='PARTIAL'):
            cvssV2_IMPACT_score_3_sh_confidentialityImpact_PARTIAL+=1
        else:
            cvssV2_IMPACT_score_3_sh_confidentialityImpact_NONE+=1 
            
            
        if(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.integrityImpact"][j]=='COMPLETE'):
            cvssV2_IMPACT_score_3_sh_integrityImpact_COMPLETE+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.integrityImpact"][j]=='PARTIAL'):
            cvssV2_IMPACT_score_3_sh_integrityImpact_PARTIAL+=1
        else:
            cvssV2_IMPACT_score_3_sh_integrityImpact_NONE+=1    
            
          
        if(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.availabilityImpact"][j]=='COMPLETE'):
            cvssV2_IMPACT_score_3_sh_availabilityImpact_COMPLETE+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.availabilityImpact"][j]=='PARTIAL'):
            cvssV2_IMPACT_score_3_sh_availabilityImpact_PARTIAL+=1
        else:
            cvssV2_IMPACT_score_3_sh_availabilityImpact_NONE+=1

            
    elif(((float(df_cve_sh["CVE_Items.impact.baseMetricV2.impactScore"][j])) < 3.0) and ((float(df_cve_sh["CVE_Items.impact.baseMetricV2.impactScore"][j])) >=2.0)):
        cvssV2_IMPACT_score_2_sh+=1   
        if(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.accessVector"][j]=='NETWORK'):
            cvssV2_IMPACT_score_2_sh_accessvector_NETWORK+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.accessVector"][j]=='LOCAL'):
            cvssV2_IMPACT_score_2_sh_accessvector_LOCAL+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.accessVector"][j]=='PHYSICAL'):
            cvssV2_IMPACT_score_2_sh_accessvector_PHYSICAL+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.accessVector"][j]=='ADJACENT_NETWORK'):
            cvssV2_IMPACT_score_2_sh_accessvector_ADJACENT_NETWORK+=1
            
        if(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.accessComplexity"][j]=='HIGH'):
            cvssV2_IMPACT_score_2_sh_accesscomplexity_HIGH+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.accessComplexity"][j]=='LOW'):
            cvssV2_IMPACT_score_2_sh_accesscomplexity_LOW+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.accessComplexity"][j]=='MEDIUM'):
            cvssV2_IMPACT_score_2_sh_accesscomplexity_MEDIUM+=1
        else:
            cvssV2_IMPACT_score_2_sh_accesscomplexity_NONE+=1  
                
        if(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.authentication"][j]=="SINGLE"):
            cvssV2_IMPACT_score_2_sh_authentication_SINGLE+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.authentication"][j]=="MULTIPLE"):
            cvssV2_IMPACT_score_2_sh_authentication_MULTIPLE+=1
        else:
            cvssV2_IMPACT_score_2_sh_authentication_NONE+=1
                
        if(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.confidentialityImpact"][j]=='COMPLETE'):
            cvssV2_IMPACT_score_2_sh_confidentialityImpact_COMPLETE+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.confidentialityImpact"][j]=='PARTIAL'):
            cvssV2_IMPACT_score_2_sh_confidentialityImpact_PARTIAL+=1
        else:
            cvssV2_IMPACT_score_2_sh_confidentialityImpact_NONE+=1 
            
            
        if(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.integrityImpact"][j]=='COMPLETE'):
            cvssV2_IMPACT_score_2_sh_integrityImpact_COMPLETE+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.integrityImpact"][j]=='PARTIAL'):
            cvssV2_IMPACT_score_2_sh_integrityImpact_PARTIAL+=1
        else:
            cvssV2_IMPACT_score_2_sh_integrityImpact_NONE+=1    
            
          
        if(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.availabilityImpact"][j]=='COMPLETE'):
            cvssV2_IMPACT_score_2_sh_availabilityImpact_COMPLETE+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.availabilityImpact"][j]=='PARTIAL'):
            cvssV2_IMPACT_score_2_sh_availabilityImpact_PARTIAL+=1
        else:
            cvssV2_IMPACT_score_2_sh_availabilityImpact_NONE+=1

            
    elif(((float(df_cve_sh["CVE_Items.impact.baseMetricV2.impactScore"][j])) < 2.0) and ((float(df_cve_sh["CVE_Items.impact.baseMetricV2.impactScore"][j])) >=1.0)):
        cvssV2_IMPACT_score_1_sh+=1   
        if(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.accessVector"][j]=='NETWORK'):
            cvssV2_IMPACT_score_1_sh_accessvector_NETWORK+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.accessVector"][j]=='LOCAL'):
            cvssV2_IMPACT_score_1_sh_accessvector_LOCAL+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.accessVector"][j]=='PHYSICAL'):
            cvssV2_IMPACT_score_1_sh_accessvector_PHYSICAL+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.accessVector"][j]=='ADJACENT_NETWORK'):
            cvssV2_IMPACT_score_1_sh_accessvector_ADJACENT_NETWORK+=1
            
        if(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.accessComplexity"][j]=='HIGH'):
            cvssV2_IMPACT_score_1_sh_accesscomplexity_HIGH+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.accessComplexity"][j]=='LOW'):
            cvssV2_IMPACT_score_1_sh_accesscomplexity_LOW+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.accessComplexity"][j]=='MEDIUM'):
            cvssV2_IMPACT_score_1_sh_accesscomplexity_MEDIUM+=1
        else:
            cvssV2_IMPACT_score_1_sh_accesscomplexity_NONE+=1  
                
        if(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.authentication"][j]=="SINGLE"):
            cvssV2_IMPACT_score_1_sh_authentication_SINGLE+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.authentication"][j]=="MULTIPLE"):
            cvssV2_IMPACT_score_1_sh_authentication_MULTIPLE+=1
        else:
            cvssV2_IMPACT_score_1_sh_authentication_NONE+=1
                
        if(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.confidentialityImpact"][j]=='COMPLETE'):
            cvssV2_IMPACT_score_1_sh_confidentialityImpact_COMPLETE+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.confidentialityImpact"][j]=='PARTIAL'):
            cvssV2_IMPACT_score_1_sh_confidentialityImpact_PARTIAL+=1
        else:
            cvssV2_IMPACT_score_1_sh_confidentialityImpact_NONE+=1 
            
            
        if(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.integrityImpact"][j]=='COMPLETE'):
            cvssV2_IMPACT_score_1_sh_integrityImpact_COMPLETE+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.integrityImpact"][j]=='PARTIAL'):
            cvssV2_IMPACT_score_1_sh_integrityImpact_PARTIAL+=1
        else:
            cvssV2_IMPACT_score_1_sh_integrityImpact_NONE+=1    
            
          
        if(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.availabilityImpact"][j]=='COMPLETE'):
            cvssV2_IMPACT_score_1_sh_availabilityImpact_COMPLETE+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.availabilityImpact"][j]=='PARTIAL'):
            cvssV2_IMPACT_score_1_sh_availabilityImpact_PARTIAL+=1
        else:
            cvssV2_IMPACT_score_1_sh_availabilityImpact_NONE+=1
    elif(((float(df_cve_sh["CVE_Items.impact.baseMetricV2.impactScore"][j])) < 1.0) and ((float(df_cve_sh["CVE_Items.impact.baseMetricV2.impactScore"][j])) >=0.0)):
        cvssV2_IMPACT_score_0_sh+=1   
        if(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.accessVector"][j]=='NETWORK'):
            cvssV2_IMPACT_score_0_sh_accessvector_NETWORK+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.accessVector"][j]=='LOCAL'):
            cvssV2_IMPACT_score_0_sh_accessvector_LOCAL+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.accessVector"][j]=='PHYSICAL'):
            cvssV2_IMPACT_score_0_sh_accessvector_PHYSICAL+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.accessVector"][j]=='ADJACENT_NETWORK'):
            cvssV2_IMPACT_score_0_sh_accessvector_ADJACENT_NETWORK+=1
            
        if(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.accessComplexity"][j]=='HIGH'):
            cvssV2_IMPACT_score_0_sh_accesscomplexity_HIGH+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.accessComplexity"][j]=='LOW'):
            cvssV2_IMPACT_score_0_sh_accesscomplexity_LOW+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.accessComplexity"][j]=='MEDIUM'):
            cvssV2_IMPACT_score_0_sh_accesscomplexity_MEDIUM+=1
        else:
            cvssV2_IMPACT_score_0_sh_accesscomplexity_NONE+=1  
                
        if(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.authentication"][j]=="SINGLE"):
            cvssV2_IMPACT_score_0_sh_authentication_SINGLE+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.authentication"][j]=="MULTIPLE"):
            cvssV2_IMPACT_score_0_sh_authentication_MULTIPLE+=1
        else:
            cvssV2_IMPACT_score_0_sh_authentication_NONE+=1
                
        if(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.confidentialityImpact"][j]=='COMPLETE'):
            cvssV2_IMPACT_score_0_sh_confidentialityImpact_COMPLETE+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.confidentialityImpact"][j]=='PARTIAL'):
            cvssV2_IMPACT_score_0_sh_confidentialityImpact_PARTIAL+=1
        else:
            cvssV2_IMPACT_score_0_sh_confidentialityImpact_NONE+=1 
            
            
        if(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.integrityImpact"][j]=='COMPLETE'):
            cvssV2_IMPACT_score_0_sh_integrityImpact_COMPLETE+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.integrityImpact"][j]=='PARTIAL'):
            cvssV2_IMPACT_score_0_sh_integrityImpact_PARTIAL+=1
        else:
            cvssV2_IMPACT_score_0_sh_integrityImpact_NONE+=1    
            
          
        if(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.availabilityImpact"][j]=='COMPLETE'):
            cvssV2_IMPACT_score_0_sh_availabilityImpact_COMPLETE+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.availabilityImpact"][j]=='PARTIAL'):
            cvssV2_IMPACT_score_0_sh_availabilityImpact_PARTIAL+=1
        else:
            cvssV2_IMPACT_score_0_sh_availabilityImpact_NONE+=1

    elif(((float(df_cve_sh["CVE_Items.impact.baseMetricV2.impactScore"][j])) == 10.0)):
        cvssV2_IMPACT_score_10_sh+=1   
        if(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.accessVector"][j]=='NETWORK'):
            cvssV2_IMPACT_score_10_sh_accessvector_NETWORK+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.accessVector"][j]=='LOCAL'):
            cvssV2_IMPACT_score_10_sh_accessvector_LOCAL+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.accessVector"][j]=='PHYSICAL'):
            cvssV2_IMPACT_score_10_sh_accessvector_PHYSICAL+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.accessVector"][j]=='ADJACENT_NETWORK'):
            cvssV2_IMPACT_score_10_sh_accessvector_ADJACENT_NETWORK+=1
            
        if(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.accessComplexity"][j]=='HIGH'):
            cvssV2_IMPACT_score_10_sh_accesscomplexity_HIGH+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.accessComplexity"][j]=='LOW'):
            cvssV2_IMPACT_score_10_sh_accesscomplexity_LOW+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.accessComplexity"][j]=='MEDIUM'):
            cvssV2_IMPACT_score_10_sh_accesscomplexity_MEDIUM+=1
        else:
            cvssV2_IMPACT_score_10_sh_accesscomplexity_NONE+=1  
                
        if(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.authentication"][j]=="SINGLE"):
            cvssV2_IMPACT_score_10_sh_authentication_SINGLE+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.authentication"][j]=="MULTIPLE"):
            cvssV2_IMPACT_score_10_sh_authentication_MULTIPLE+=1
        else:
            cvssV2_IMPACT_score_10_sh_authentication_NONE+=1
                
        if(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.confidentialityImpact"][j]=='COMPLETE'):
            cvssV2_IMPACT_score_10_sh_confidentialityImpact_COMPLETE+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.confidentialityImpact"][j]=='PARTIAL'):
            cvssV2_IMPACT_score_10_sh_confidentialityImpact_PARTIAL+=1
        else:
            cvssV2_IMPACT_score_10_sh_confidentialityImpact_NONE+=1 
            
            
        if(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.integrityImpact"][j]=='COMPLETE'):
            cvssV2_IMPACT_score_10_sh_integrityImpact_COMPLETE+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.integrityImpact"][j]=='PARTIAL'):
            cvssV2_IMPACT_score_10_sh_integrityImpact_PARTIAL+=1
        else:
            cvssV2_IMPACT_score_10_sh_integrityImpact_NONE+=1    
            
          
        if(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.availabilityImpact"][j]=='COMPLETE'):
            cvssV2_IMPACT_score_10_sh_availabilityImpact_COMPLETE+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.availabilityImpact"][j]=='PARTIAL'):
            cvssV2_IMPACT_score_10_sh_availabilityImpact_PARTIAL+=1
        else:
            cvssV2_IMPACT_score_10_sh_availabilityImpact_NONE+=1
            
            
            
print("________________________ESTADISTICAS ELEMENTOS VECTOR STRING SEGUN PUNTUACION DE IMPACTO CVSSV2 PARTE SMART HOME________________________")
print("\n")        
            
            
    
print("\n")
print(" DE UN TOTAL DE "+str(len(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.availabilityImpact"]))+" VULNERABILIDADES , LAS ESTADISTICAS DE PUNTUACION DE IMPACTO SON LAS SIGUIENTES:  \n")
print("\n")
print("      -    EN  "+str(cvssV2_IMPACT_score_10_sh)+" VULNERABILIDADES LA PUNTUACION DE IMPACTO ES 10. LAS ESTADÍSTICAS DEL VECTOR STRING SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_10_sh_accessvector_NETWORK)+" VULNERABILIDADES EL VECTOR DE ACCESO ES NETWORK ")
print("            -    EN  "+str(cvssV2_IMPACT_score_10_sh_accessvector_LOCAL)+" VULNERABILIDADES EL VECTOR DE ACCESO ES LOCAL ")
print("            -    EN  "+str(cvssV2_IMPACT_score_10_sh_accessvector_PHYSICAL)+" VULNERABILIDADES EL VECTOR DE ACCESO ES PHYSICAL ")
print("            -    EN  "+str(cvssV2_IMPACT_score_10_sh_accessvector_ADJACENT_NETWORK)+" VULNERABILIDADES EL VECTOR DE ACCESO ES ADJACENT_NETWORK ")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_10_sh_accesscomplexity_HIGH)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES ALTA ")
print("            -    EN  "+str(cvssV2_IMPACT_score_10_sh_accesscomplexity_LOW)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES BAJA ")
print("            -    EN  "+str(cvssV2_IMPACT_score_10_sh_accesscomplexity_MEDIUM)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES MEDIA ")
print("            -    EN  "+str(cvssV2_IMPACT_score_10_sh_accesscomplexity_NONE)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO NO VIENE ESPECIFICADA ")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_10_sh_authentication_SINGLE)+" VULNERABILIDADES SE REQUIERE AUTENTICACIÓN SENCILLA ")
print("            -    EN  "+str(cvssV2_IMPACT_score_10_sh_authentication_MULTIPLE)+" VULNERABILIDADES SE REQUIERE AUTENTICACIÓN MULTIPLE")
print("            -    EN  "+str(cvssV2_IMPACT_score_10_sh_authentication_NONE)+" VULNERABILIDADES NO SE REQUIERE AUTENTICACIÓN")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_10_sh_confidentialityImpact_COMPLETE)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES COMPLETO ")
print("            -    EN  "+str(cvssV2_IMPACT_score_10_sh_confidentialityImpact_PARTIAL)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES PARCIAL" )
print("            -    EN  "+str(cvssV2_IMPACT_score_10_sh_confidentialityImpact_NONE)+" VULNERABILIDADES NO EXISTE IMPACTO DE CONFIDENCIALIDAD ")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_10_sh_integrityImpact_COMPLETE)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES COMPLETO ")
print("            -    EN  "+str(cvssV2_IMPACT_score_10_sh_integrityImpact_PARTIAL)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES PARCIAL" )
print("            -    EN  "+str(cvssV2_IMPACT_score_10_sh_integrityImpact_NONE)+" VULNERABILIDADES NO EXISTE IMPACTO DE INTEGRIDAD ")
print("\n")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_10_sh_availabilityImpact_COMPLETE)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES COMPLETO ")
print("            -    EN  "+str(cvssV2_IMPACT_score_10_sh_availabilityImpact_PARTIAL)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES PARCIAL" )
print("            -    EN  "+str(cvssV2_IMPACT_score_10_sh_availabilityImpact_NONE)+" VULNERABILIDADES NO EXISTE IMPACTO DE DISPONIBILIDAD ")
print("\n")
print("\n")
print("      -    EN  "+str(cvssV2_IMPACT_score_9_sh)+" VULNERABILIDADES LA PUNTUACION DE IMPACTO ESTÁ ENTRE 9 Y 10. LAS ESTADÍSTICAS DEL VECTOR STRING SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_9_sh_accessvector_NETWORK)+" VULNERABILIDADES EL VECTOR DE ACCESO ES NETWORK ")
print("            -    EN  "+str(cvssV2_IMPACT_score_9_sh_accessvector_LOCAL)+" VULNERABILIDADES EL VECTOR DE ACCESO ES LOCAL ")
print("            -    EN  "+str(cvssV2_IMPACT_score_9_sh_accessvector_PHYSICAL)+" VULNERABILIDADES EL VECTOR DE ACCESO ES PHYSICAL ")
print("            -    EN  "+str(cvssV2_IMPACT_score_9_sh_accessvector_ADJACENT_NETWORK)+" VULNERABILIDADES EL VECTOR DE ACCESO ES ADJACENT_NETWORK ")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_9_sh_accesscomplexity_HIGH)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES ALTA ")
print("            -    EN  "+str(cvssV2_IMPACT_score_9_sh_accesscomplexity_LOW)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES BAJA ")
print("            -    EN  "+str(cvssV2_IMPACT_score_9_sh_accesscomplexity_MEDIUM)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES MEDIA ")
print("            -    EN  "+str(cvssV2_IMPACT_score_9_sh_accesscomplexity_NONE)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO NO VIENE ESPECIFICADA ")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_9_sh_authentication_SINGLE)+" VULNERABILIDADES SE REQUIERE AUTENTICACIÓN SENCILLA ")
print("            -    EN  "+str(cvssV2_IMPACT_score_9_sh_authentication_MULTIPLE)+" VULNERABILIDADES SE REQUIERE AUTENTICACIÓN MULTIPLE")
print("            -    EN  "+str(cvssV2_IMPACT_score_9_sh_authentication_NONE)+" VULNERABILIDADES NO SE REQUIERE AUTENTICACIÓN")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_9_sh_confidentialityImpact_COMPLETE)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES COMPLETO ")
print("            -    EN  "+str(cvssV2_IMPACT_score_9_sh_confidentialityImpact_PARTIAL)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES PARCIAL" )
print("            -    EN  "+str(cvssV2_IMPACT_score_9_sh_confidentialityImpact_NONE)+" VULNERABILIDADES NO EXISTE IMPACTO DE CONFIDENCIALIDAD ")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_9_sh_integrityImpact_COMPLETE)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES COMPLETO ")
print("            -    EN  "+str(cvssV2_IMPACT_score_9_sh_integrityImpact_PARTIAL)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES PARCIAL" )
print("            -    EN  "+str(cvssV2_IMPACT_score_9_sh_integrityImpact_NONE)+" VULNERABILIDADES NO EXISTE IMPACTO DE INTEGRIDAD ")
print("\n")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_9_sh_availabilityImpact_COMPLETE)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES COMPLETO ")
print("            -    EN  "+str(cvssV2_IMPACT_score_9_sh_availabilityImpact_PARTIAL)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES PARCIAL" )
print("            -    EN  "+str(cvssV2_IMPACT_score_9_sh_availabilityImpact_NONE)+" VULNERABILIDADES NO EXISTE IMPACTO DE DISPONIBILIDAD ")
print("\n")
print("\n")
print("\n")
print("      -    EN  "+str(cvssV2_IMPACT_score_8_sh)+" VULNERABILIDADES LA PUNTUACION DE IMPACTO ESTÁ ENTRE 8 Y 9. LAS ESTADÍSTICAS DEL VECTOR STRING SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_8_sh_accessvector_NETWORK)+" VULNERABILIDADES EL VECTOR DE ACCESO ES NETWORK ")
print("            -    EN  "+str(cvssV2_IMPACT_score_8_sh_accessvector_LOCAL)+" VULNERABILIDADES EL VECTOR DE ACCESO ES LOCAL ")
print("            -    EN  "+str(cvssV2_IMPACT_score_8_sh_accessvector_PHYSICAL)+" VULNERABILIDADES EL VECTOR DE ACCESO ES PHYSICAL ")
print("            -    EN  "+str(cvssV2_IMPACT_score_8_sh_accessvector_ADJACENT_NETWORK)+" VULNERABILIDADES EL VECTOR DE ACCESO ES ADJACENT_NETWORK ")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_8_sh_accesscomplexity_HIGH)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES ALTA ")
print("            -    EN  "+str(cvssV2_IMPACT_score_8_sh_accesscomplexity_LOW)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES BAJA ")
print("            -    EN  "+str(cvssV2_IMPACT_score_8_sh_accesscomplexity_MEDIUM)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES MEDIA ")
print("            -    EN  "+str(cvssV2_IMPACT_score_8_sh_accesscomplexity_NONE)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO NO VIENE ESPECIFICADA ")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_8_sh_authentication_SINGLE)+" VULNERABILIDADES SE REQUIERE AUTENTICACIÓN SENCILLA ")
print("            -    EN  "+str(cvssV2_IMPACT_score_8_sh_authentication_MULTIPLE)+" VULNERABILIDADES SE REQUIERE AUTENTICACIÓN MULTIPLE")
print("            -    EN  "+str(cvssV2_IMPACT_score_8_sh_authentication_NONE)+" VULNERABILIDADES NO SE REQUIERE AUTENTICACIÓN")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_8_sh_confidentialityImpact_COMPLETE)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES COMPLETO ")
print("            -    EN  "+str(cvssV2_IMPACT_score_8_sh_confidentialityImpact_PARTIAL)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES PARCIAL" )
print("            -    EN  "+str(cvssV2_IMPACT_score_8_sh_confidentialityImpact_NONE)+" VULNERABILIDADES NO EXISTE IMPACTO DE CONFIDENCIALIDAD ")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_8_sh_integrityImpact_COMPLETE)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES COMPLETO ")
print("            -    EN  "+str(cvssV2_IMPACT_score_8_sh_integrityImpact_PARTIAL)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES PARCIAL" )
print("            -    EN  "+str(cvssV2_IMPACT_score_8_sh_integrityImpact_NONE)+" VULNERABILIDADES NO EXISTE IMPACTO DE INTEGRIDAD ")
print("\n")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_8_sh_availabilityImpact_COMPLETE)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES COMPLETO ")
print("            -    EN  "+str(cvssV2_IMPACT_score_8_sh_availabilityImpact_PARTIAL)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES PARCIAL" )
print("            -    EN  "+str(cvssV2_IMPACT_score_8_sh_availabilityImpact_NONE)+" VULNERABILIDADES NO EXISTE IMPACTO DE DISPONIBILIDAD ")
print("\n")
print("\n")
print("\n")
print("      -    EN  "+str(cvssV2_IMPACT_score_7_sh)+" VULNERABILIDADES LA PUNTUACION DE IMPACTO ESTÁ ENTRE 7 Y 8. LAS ESTADÍSTICAS DEL VECTOR STRING SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_7_sh_accessvector_NETWORK)+" VULNERABILIDADES EL VECTOR DE ACCESO ES NETWORK ")
print("            -    EN  "+str(cvssV2_IMPACT_score_7_sh_accessvector_LOCAL)+" VULNERABILIDADES EL VECTOR DE ACCESO ES LOCAL ")
print("            -    EN  "+str(cvssV2_IMPACT_score_7_sh_accessvector_PHYSICAL)+" VULNERABILIDADES EL VECTOR DE ACCESO ES PHYSICAL ")
print("            -    EN  "+str(cvssV2_IMPACT_score_7_sh_accessvector_ADJACENT_NETWORK)+" VULNERABILIDADES EL VECTOR DE ACCESO ES ADJACENT_NETWORK ")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_7_sh_accesscomplexity_HIGH)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES ALTA ")
print("            -    EN  "+str(cvssV2_IMPACT_score_7_sh_accesscomplexity_LOW)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES BAJA ")
print("            -    EN  "+str(cvssV2_IMPACT_score_7_sh_accesscomplexity_MEDIUM)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES MEDIA ")
print("            -    EN  "+str(cvssV2_IMPACT_score_7_sh_accesscomplexity_NONE)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO NO VIENE ESPECIFICADA ")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_7_sh_authentication_SINGLE)+" VULNERABILIDADES SE REQUIERE AUTENTICACIÓN SENCILLA ")
print("            -    EN  "+str(cvssV2_IMPACT_score_7_sh_authentication_MULTIPLE)+" VULNERABILIDADES SE REQUIERE AUTENTICACIÓN MULTIPLE")
print("            -    EN  "+str(cvssV2_IMPACT_score_7_sh_authentication_NONE)+" VULNERABILIDADES NO SE REQUIERE AUTENTICACIÓN")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_7_sh_confidentialityImpact_COMPLETE)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES COMPLETO ")
print("            -    EN  "+str(cvssV2_IMPACT_score_7_sh_confidentialityImpact_PARTIAL)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES PARCIAL" )
print("            -    EN  "+str(cvssV2_IMPACT_score_7_sh_confidentialityImpact_NONE)+" VULNERABILIDADES NO EXISTE IMPACTO DE CONFIDENCIALIDAD ")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_7_sh_integrityImpact_COMPLETE)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES COMPLETO ")
print("            -    EN  "+str(cvssV2_IMPACT_score_7_sh_integrityImpact_PARTIAL)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES PARCIAL" )
print("            -    EN  "+str(cvssV2_IMPACT_score_7_sh_integrityImpact_NONE)+" VULNERABILIDADES NO EXISTE IMPACTO DE INTEGRIDAD ")
print("\n")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_7_sh_availabilityImpact_COMPLETE)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES COMPLETO ")
print("            -    EN  "+str(cvssV2_IMPACT_score_7_sh_availabilityImpact_PARTIAL)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES PARCIAL" )
print("            -    EN  "+str(cvssV2_IMPACT_score_7_sh_availabilityImpact_NONE)+" VULNERABILIDADES NO EXISTE IMPACTO DE DISPONIBILIDAD ")
print("\n")
print("\n")
print("      -    EN  "+str(cvssV2_IMPACT_score_6_sh)+" VULNERABILIDADES LA PUNTUACION DE IMPACTO ESTÁ ENTRE 6 Y 7. LAS ESTADÍSTICAS DEL VECTOR STRING SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_6_sh_accessvector_NETWORK)+" VULNERABILIDADES EL VECTOR DE ACCESO ES NETWORK ")
print("            -    EN  "+str(cvssV2_IMPACT_score_6_sh_accessvector_LOCAL)+" VULNERABILIDADES EL VECTOR DE ACCESO ES LOCAL ")
print("            -    EN  "+str(cvssV2_IMPACT_score_6_sh_accessvector_PHYSICAL)+" VULNERABILIDADES EL VECTOR DE ACCESO ES PHYSICAL ")
print("            -    EN  "+str(cvssV2_IMPACT_score_6_sh_accessvector_ADJACENT_NETWORK)+" VULNERABILIDADES EL VECTOR DE ACCESO ES ADJACENT_NETWORK ")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_6_sh_accesscomplexity_HIGH)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES ALTA ")
print("            -    EN  "+str(cvssV2_IMPACT_score_6_sh_accesscomplexity_LOW)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES BAJA ")
print("            -    EN  "+str(cvssV2_IMPACT_score_6_sh_accesscomplexity_MEDIUM)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES MEDIA ")
print("            -    EN  "+str(cvssV2_IMPACT_score_6_sh_accesscomplexity_NONE)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO NO VIENE ESPECIFICADA ")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_6_sh_authentication_SINGLE)+" VULNERABILIDADES SE REQUIERE AUTENTICACIÓN SENCILLA ")
print("            -    EN  "+str(cvssV2_IMPACT_score_6_sh_authentication_MULTIPLE)+" VULNERABILIDADES SE REQUIERE AUTENTICACIÓN MULTIPLE")
print("            -    EN  "+str(cvssV2_IMPACT_score_6_sh_authentication_NONE)+" VULNERABILIDADES NO SE REQUIERE AUTENTICACIÓN")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_6_sh_confidentialityImpact_COMPLETE)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES COMPLETO ")
print("            -    EN  "+str(cvssV2_IMPACT_score_6_sh_confidentialityImpact_PARTIAL)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES PARCIAL" )
print("            -    EN  "+str(cvssV2_IMPACT_score_6_sh_confidentialityImpact_NONE)+" VULNERABILIDADES NO EXISTE IMPACTO DE CONFIDENCIALIDAD ")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_6_sh_integrityImpact_COMPLETE)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES COMPLETO ")
print("            -    EN  "+str(cvssV2_IMPACT_score_6_sh_integrityImpact_PARTIAL)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES PARCIAL" )
print("            -    EN  "+str(cvssV2_IMPACT_score_6_sh_integrityImpact_NONE)+" VULNERABILIDADES NO EXISTE IMPACTO DE INTEGRIDAD ")
print("\n")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_6_sh_availabilityImpact_COMPLETE)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES COMPLETO ")
print("            -    EN  "+str(cvssV2_IMPACT_score_6_sh_availabilityImpact_PARTIAL)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES PARCIAL" )
print("            -    EN  "+str(cvssV2_IMPACT_score_6_sh_availabilityImpact_NONE)+" VULNERABILIDADES NO EXISTE IMPACTO DE DISPONIBILIDAD ")
print("\n")
print("\n")
print("      -    EN  "+str(cvssV2_IMPACT_score_5_sh)+" VULNERABILIDADES LA PUNTUACION DE IMPACTO ESTÁ ENTRE 5 Y 6. LAS ESTADÍSTICAS DEL VECTOR STRING SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_5_sh_accessvector_NETWORK)+" VULNERABILIDADES EL VECTOR DE ACCESO ES NETWORK ")
print("            -    EN  "+str(cvssV2_IMPACT_score_5_sh_accessvector_LOCAL)+" VULNERABILIDADES EL VECTOR DE ACCESO ES LOCAL ")
print("            -    EN  "+str(cvssV2_IMPACT_score_5_sh_accessvector_PHYSICAL)+" VULNERABILIDADES EL VECTOR DE ACCESO ES PHYSICAL ")
print("            -    EN  "+str(cvssV2_IMPACT_score_5_sh_accessvector_ADJACENT_NETWORK)+" VULNERABILIDADES EL VECTOR DE ACCESO ES ADJACENT_NETWORK ")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_5_sh_accesscomplexity_HIGH)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES ALTA ")
print("            -    EN  "+str(cvssV2_IMPACT_score_5_sh_accesscomplexity_LOW)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES BAJA ")
print("            -    EN  "+str(cvssV2_IMPACT_score_5_sh_accesscomplexity_MEDIUM)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES MEDIA ")
print("            -    EN  "+str(cvssV2_IMPACT_score_5_sh_accesscomplexity_NONE)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO NO VIENE ESPECIFICADA ")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_5_sh_authentication_SINGLE)+" VULNERABILIDADES SE REQUIERE AUTENTICACIÓN SENCILLA ")
print("            -    EN  "+str(cvssV2_IMPACT_score_5_sh_authentication_MULTIPLE)+" VULNERABILIDADES SE REQUIERE AUTENTICACIÓN MULTIPLE")
print("            -    EN  "+str(cvssV2_IMPACT_score_5_sh_authentication_NONE)+" VULNERABILIDADES NO SE REQUIERE AUTENTICACIÓN")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_5_sh_confidentialityImpact_COMPLETE)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES COMPLETO ")
print("            -    EN  "+str(cvssV2_IMPACT_score_5_sh_confidentialityImpact_PARTIAL)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES PARCIAL" )
print("            -    EN  "+str(cvssV2_IMPACT_score_5_sh_confidentialityImpact_NONE)+" VULNERABILIDADES NO EXISTE IMPACTO DE CONFIDENCIALIDAD ")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_5_sh_integrityImpact_COMPLETE)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES COMPLETO ")
print("            -    EN  "+str(cvssV2_IMPACT_score_5_sh_integrityImpact_PARTIAL)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES PARCIAL" )
print("            -    EN  "+str(cvssV2_IMPACT_score_5_sh_integrityImpact_NONE)+" VULNERABILIDADES NO EXISTE IMPACTO DE INTEGRIDAD ")
print("\n")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_5_sh_availabilityImpact_COMPLETE)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES COMPLETO ")
print("            -    EN  "+str(cvssV2_IMPACT_score_5_sh_availabilityImpact_PARTIAL)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES PARCIAL" )
print("            -    EN  "+str(cvssV2_IMPACT_score_5_sh_availabilityImpact_NONE)+" VULNERABILIDADES NO EXISTE IMPACTO DE DISPONIBILIDAD ")
print("\n")
print("\n")
print("      -    EN  "+str(cvssV2_IMPACT_score_4_sh)+" VULNERABILIDADES LA PUNTUACION DE IMPACTO ESTÁ ENTRE 4 Y 5. LAS ESTADÍSTICAS DEL VECTOR STRING SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_4_sh_accessvector_NETWORK)+" VULNERABILIDADES EL VECTOR DE ACCESO ES NETWORK ")
print("            -    EN  "+str(cvssV2_IMPACT_score_4_sh_accessvector_LOCAL)+" VULNERABILIDADES EL VECTOR DE ACCESO ES LOCAL ")
print("            -    EN  "+str(cvssV2_IMPACT_score_4_sh_accessvector_PHYSICAL)+" VULNERABILIDADES EL VECTOR DE ACCESO ES PHYSICAL ")
print("            -    EN  "+str(cvssV2_IMPACT_score_4_sh_accessvector_ADJACENT_NETWORK)+" VULNERABILIDADES EL VECTOR DE ACCESO ES ADJACENT_NETWORK ")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_4_sh_accesscomplexity_HIGH)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES ALTA ")
print("            -    EN  "+str(cvssV2_IMPACT_score_4_sh_accesscomplexity_LOW)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES BAJA ")
print("            -    EN  "+str(cvssV2_IMPACT_score_4_sh_accesscomplexity_MEDIUM)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES MEDIA ")
print("            -    EN  "+str(cvssV2_IMPACT_score_4_sh_accesscomplexity_NONE)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO NO VIENE ESPECIFICADA ")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_4_sh_authentication_SINGLE)+" VULNERABILIDADES SE REQUIERE AUTENTICACIÓN SENCILLA ")
print("            -    EN  "+str(cvssV2_IMPACT_score_4_sh_authentication_MULTIPLE)+" VULNERABILIDADES SE REQUIERE AUTENTICACIÓN MULTIPLE")
print("            -    EN  "+str(cvssV2_IMPACT_score_4_sh_authentication_NONE)+" VULNERABILIDADES NO SE REQUIERE AUTENTICACIÓN")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_4_sh_confidentialityImpact_COMPLETE)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES COMPLETO ")
print("            -    EN  "+str(cvssV2_IMPACT_score_4_sh_confidentialityImpact_PARTIAL)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES PARCIAL" )
print("            -    EN  "+str(cvssV2_IMPACT_score_4_sh_confidentialityImpact_NONE)+" VULNERABILIDADES NO EXISTE IMPACTO DE CONFIDENCIALIDAD ")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_4_sh_integrityImpact_COMPLETE)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES COMPLETO ")
print("            -    EN  "+str(cvssV2_IMPACT_score_4_sh_integrityImpact_PARTIAL)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES PARCIAL" )
print("            -    EN  "+str(cvssV2_IMPACT_score_4_sh_integrityImpact_NONE)+" VULNERABILIDADES NO EXISTE IMPACTO DE INTEGRIDAD ")
print("\n")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_4_sh_availabilityImpact_COMPLETE)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES COMPLETO ")
print("            -    EN  "+str(cvssV2_IMPACT_score_4_sh_availabilityImpact_PARTIAL)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES PARCIAL" )
print("            -    EN  "+str(cvssV2_IMPACT_score_4_sh_availabilityImpact_NONE)+" VULNERABILIDADES NO EXISTE IMPACTO DE DISPONIBILIDAD ")
print("\n")
print("\n")
print("      -    EN  "+str(cvssV2_IMPACT_score_3_sh)+" VULNERABILIDADES LA PUNTUACION DE IMPACTO ESTÁ ENTRE 3 Y 4. LAS ESTADÍSTICAS DEL VECTOR STRING SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_3_sh_accessvector_NETWORK)+" VULNERABILIDADES EL VECTOR DE ACCESO ES NETWORK ")
print("            -    EN  "+str(cvssV2_IMPACT_score_3_sh_accessvector_LOCAL)+" VULNERABILIDADES EL VECTOR DE ACCESO ES LOCAL ")
print("            -    EN  "+str(cvssV2_IMPACT_score_3_sh_accessvector_PHYSICAL)+" VULNERABILIDADES EL VECTOR DE ACCESO ES PHYSICAL ")
print("            -    EN  "+str(cvssV2_IMPACT_score_3_sh_accessvector_ADJACENT_NETWORK)+" VULNERABILIDADES EL VECTOR DE ACCESO ES ADJACENT_NETWORK ")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_3_sh_accesscomplexity_HIGH)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES ALTA ")
print("            -    EN  "+str(cvssV2_IMPACT_score_3_sh_accesscomplexity_LOW)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES BAJA ")
print("            -    EN  "+str(cvssV2_IMPACT_score_3_sh_accesscomplexity_MEDIUM)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES MEDIA ")
print("            -    EN  "+str(cvssV2_IMPACT_score_3_sh_accesscomplexity_NONE)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO NO VIENE ESPECIFICADA ")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_3_sh_authentication_SINGLE)+" VULNERABILIDADES SE REQUIERE AUTENTICACIÓN SENCILLA ")
print("            -    EN  "+str(cvssV2_IMPACT_score_3_sh_authentication_MULTIPLE)+" VULNERABILIDADES SE REQUIERE AUTENTICACIÓN MULTIPLE")
print("            -    EN  "+str(cvssV2_IMPACT_score_3_sh_authentication_NONE)+" VULNERABILIDADES NO SE REQUIERE AUTENTICACIÓN")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_3_sh_confidentialityImpact_COMPLETE)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES COMPLETO ")
print("            -    EN  "+str(cvssV2_IMPACT_score_3_sh_confidentialityImpact_PARTIAL)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES PARCIAL" )
print("            -    EN  "+str(cvssV2_IMPACT_score_3_sh_confidentialityImpact_NONE)+" VULNERABILIDADES NO EXISTE IMPACTO DE CONFIDENCIALIDAD ")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_3_sh_integrityImpact_COMPLETE)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES COMPLETO ")
print("            -    EN  "+str(cvssV2_IMPACT_score_3_sh_integrityImpact_PARTIAL)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES PARCIAL" )
print("            -    EN  "+str(cvssV2_IMPACT_score_3_sh_integrityImpact_NONE)+" VULNERABILIDADES NO EXISTE IMPACTO DE INTEGRIDAD ")
print("\n")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_3_sh_availabilityImpact_COMPLETE)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES COMPLETO ")
print("            -    EN  "+str(cvssV2_IMPACT_score_3_sh_availabilityImpact_PARTIAL)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES PARCIAL" )
print("            -    EN  "+str(cvssV2_IMPACT_score_3_sh_availabilityImpact_NONE)+" VULNERABILIDADES NO EXISTE IMPACTO DE DISPONIBILIDAD ")
print("\n")
print("\n")
print("      -    EN  "+str(cvssV2_IMPACT_score_2_sh)+" VULNERABILIDADES LA PUNTUACION DE IMPACTO ESTÁ ENTRE 2 Y 3. LAS ESTADÍSTICAS DEL VECTOR STRING SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_2_sh_accessvector_NETWORK)+" VULNERABILIDADES EL VECTOR DE ACCESO ES NETWORK ")
print("            -    EN  "+str(cvssV2_IMPACT_score_2_sh_accessvector_LOCAL)+" VULNERABILIDADES EL VECTOR DE ACCESO ES LOCAL ")
print("            -    EN  "+str(cvssV2_IMPACT_score_2_sh_accessvector_PHYSICAL)+" VULNERABILIDADES EL VECTOR DE ACCESO ES PHYSICAL ")
print("            -    EN  "+str(cvssV2_IMPACT_score_2_sh_accessvector_ADJACENT_NETWORK)+" VULNERABILIDADES EL VECTOR DE ACCESO ES ADJACENT_NETWORK ")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_2_sh_accesscomplexity_HIGH)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES ALTA ")
print("            -    EN  "+str(cvssV2_IMPACT_score_2_sh_accesscomplexity_LOW)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES BAJA ")
print("            -    EN  "+str(cvssV2_IMPACT_score_2_sh_accesscomplexity_MEDIUM)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES MEDIA ")
print("            -    EN  "+str(cvssV2_IMPACT_score_2_sh_accesscomplexity_NONE)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO NO VIENE ESPECIFICADA ")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_2_sh_authentication_SINGLE)+" VULNERABILIDADES SE REQUIERE AUTENTICACIÓN SENCILLA ")
print("            -    EN  "+str(cvssV2_IMPACT_score_2_sh_authentication_MULTIPLE)+" VULNERABILIDADES SE REQUIERE AUTENTICACIÓN MULTIPLE")
print("            -    EN  "+str(cvssV2_IMPACT_score_2_sh_authentication_NONE)+" VULNERABILIDADES NO SE REQUIERE AUTENTICACIÓN")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_2_sh_confidentialityImpact_COMPLETE)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES COMPLETO ")
print("            -    EN  "+str(cvssV2_IMPACT_score_2_sh_confidentialityImpact_PARTIAL)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES PARCIAL" )
print("            -    EN  "+str(cvssV2_IMPACT_score_2_sh_confidentialityImpact_NONE)+" VULNERABILIDADES NO EXISTE IMPACTO DE CONFIDENCIALIDAD ")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_2_sh_integrityImpact_COMPLETE)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES COMPLETO ")
print("            -    EN  "+str(cvssV2_IMPACT_score_2_sh_integrityImpact_PARTIAL)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES PARCIAL" )
print("            -    EN  "+str(cvssV2_IMPACT_score_2_sh_integrityImpact_NONE)+" VULNERABILIDADES NO EXISTE IMPACTO DE INTEGRIDAD ")
print("\n")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_2_sh_availabilityImpact_COMPLETE)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES COMPLETO ")
print("            -    EN  "+str(cvssV2_IMPACT_score_2_sh_availabilityImpact_PARTIAL)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES PARCIAL" )
print("            -    EN  "+str(cvssV2_IMPACT_score_2_sh_availabilityImpact_NONE)+" VULNERABILIDADES NO EXISTE IMPACTO DE DISPONIBILIDAD ")
print("\n")
print("\n")
print("      -    EN  "+str(cvssV2_IMPACT_score_1_sh)+" VULNERABILIDADES LA PUNTUACION DE IMPACTO ESTÁ ENTRE 1 Y 2. LAS ESTADÍSTICAS DEL VECTOR STRING SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_1_sh_accessvector_NETWORK)+" VULNERABILIDADES EL VECTOR DE ACCESO ES NETWORK ")
print("            -    EN  "+str(cvssV2_IMPACT_score_1_sh_accessvector_LOCAL)+" VULNERABILIDADES EL VECTOR DE ACCESO ES LOCAL ")
print("            -    EN  "+str(cvssV2_IMPACT_score_1_sh_accessvector_PHYSICAL)+" VULNERABILIDADES EL VECTOR DE ACCESO ES PHYSICAL ")
print("            -    EN  "+str(cvssV2_IMPACT_score_1_sh_accessvector_ADJACENT_NETWORK)+" VULNERABILIDADES EL VECTOR DE ACCESO ES ADJACENT_NETWORK ")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_1_sh_accesscomplexity_HIGH)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES ALTA ")
print("            -    EN  "+str(cvssV2_IMPACT_score_1_sh_accesscomplexity_LOW)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES BAJA ")
print("            -    EN  "+str(cvssV2_IMPACT_score_1_sh_accesscomplexity_MEDIUM)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES MEDIA ")
print("            -    EN  "+str(cvssV2_IMPACT_score_1_sh_accesscomplexity_NONE)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO NO VIENE ESPECIFICADA ")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_1_sh_authentication_SINGLE)+" VULNERABILIDADES SE REQUIERE AUTENTICACIÓN SENCILLA ")
print("            -    EN  "+str(cvssV2_IMPACT_score_1_sh_authentication_MULTIPLE)+" VULNERABILIDADES SE REQUIERE AUTENTICACIÓN MULTIPLE")
print("            -    EN  "+str(cvssV2_IMPACT_score_1_sh_authentication_NONE)+" VULNERABILIDADES NO SE REQUIERE AUTENTICACIÓN")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_1_sh_confidentialityImpact_COMPLETE)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES COMPLETO ")
print("            -    EN  "+str(cvssV2_IMPACT_score_1_sh_confidentialityImpact_PARTIAL)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES PARCIAL" )
print("            -    EN  "+str(cvssV2_IMPACT_score_1_sh_confidentialityImpact_NONE)+" VULNERABILIDADES NO EXISTE IMPACTO DE CONFIDENCIALIDAD ")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_1_sh_integrityImpact_COMPLETE)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES COMPLETO ")
print("            -    EN  "+str(cvssV2_IMPACT_score_1_sh_integrityImpact_PARTIAL)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES PARCIAL" )
print("            -    EN  "+str(cvssV2_IMPACT_score_1_sh_integrityImpact_NONE)+" VULNERABILIDADES NO EXISTE IMPACTO DE INTEGRIDAD ")
print("\n")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_1_sh_availabilityImpact_COMPLETE)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES COMPLETO ")
print("            -    EN  "+str(cvssV2_IMPACT_score_1_sh_availabilityImpact_PARTIAL)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES PARCIAL" )
print("            -    EN  "+str(cvssV2_IMPACT_score_1_sh_availabilityImpact_NONE)+" VULNERABILIDADES NO EXISTE IMPACTO DE DISPONIBILIDAD ")
print("\n")
print("      -    EN  "+str(cvssV2_IMPACT_score_0_sh)+" VULNERABILIDADES LA PUNTUACION DE IMPACTO ESTÁ ENTRE 0 Y 1. LAS ESTADÍSTICAS DEL VECTOR STRING SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_0_sh_accessvector_NETWORK)+" VULNERABILIDADES EL VECTOR DE ACCESO ES NETWORK ")
print("            -    EN  "+str(cvssV2_IMPACT_score_0_sh_accessvector_LOCAL)+" VULNERABILIDADES EL VECTOR DE ACCESO ES LOCAL ")
print("            -    EN  "+str(cvssV2_IMPACT_score_0_sh_accessvector_PHYSICAL)+" VULNERABILIDADES EL VECTOR DE ACCESO ES PHYSICAL ")
print("            -    EN  "+str(cvssV2_IMPACT_score_0_sh_accessvector_ADJACENT_NETWORK)+" VULNERABILIDADES EL VECTOR DE ACCESO ES ADJACENT_NETWORK ")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_0_sh_accesscomplexity_HIGH)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES ALTA ")
print("            -    EN  "+str(cvssV2_IMPACT_score_0_sh_accesscomplexity_LOW)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES BAJA ")
print("            -    EN  "+str(cvssV2_IMPACT_score_0_sh_accesscomplexity_MEDIUM)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES MEDIA ")
print("            -    EN  "+str(cvssV2_IMPACT_score_0_sh_accesscomplexity_NONE)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO NO VIENE ESPECIFICADA ")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_0_sh_authentication_SINGLE)+" VULNERABILIDADES SE REQUIERE AUTENTICACIÓN SENCILLA ")
print("            -    EN  "+str(cvssV2_IMPACT_score_0_sh_authentication_MULTIPLE)+" VULNERABILIDADES SE REQUIERE AUTENTICACIÓN MULTIPLE")
print("            -    EN  "+str(cvssV2_IMPACT_score_0_sh_authentication_NONE)+" VULNERABILIDADES NO SE REQUIERE AUTENTICACIÓN")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_0_sh_confidentialityImpact_COMPLETE)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES COMPLETO ")
print("            -    EN  "+str(cvssV2_IMPACT_score_0_sh_confidentialityImpact_PARTIAL)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES PARCIAL" )
print("            -    EN  "+str(cvssV2_IMPACT_score_0_sh_confidentialityImpact_NONE)+" VULNERABILIDADES NO EXISTE IMPACTO DE CONFIDENCIALIDAD ")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_0_sh_integrityImpact_COMPLETE)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES COMPLETO ")
print("            -    EN  "+str(cvssV2_IMPACT_score_0_sh_integrityImpact_PARTIAL)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES PARCIAL" )
print("            -    EN  "+str(cvssV2_IMPACT_score_0_sh_integrityImpact_NONE)+" VULNERABILIDADES NO EXISTE IMPACTO DE INTEGRIDAD ")
print("\n")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_0_sh_availabilityImpact_COMPLETE)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES COMPLETO ")
print("            -    EN  "+str(cvssV2_IMPACT_score_0_sh_availabilityImpact_PARTIAL)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES PARCIAL" )
print("            -    EN  "+str(cvssV2_IMPACT_score_0_sh_availabilityImpact_NONE)+" VULNERABILIDADES NO EXISTE IMPACTO DE DISPONIBILIDAD ")
print("\n")
print("\n")
print("      -    EN  "+str(cvssV2_no_IMPACT_score_sh)+" VULNERABILIDADES LA PUNTUACION DE IMPACTO NO ESTÁ ESPECIFICADA. LAS ESTADÍSTICAS DEL VECTOR STRING SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(cvssV2_no_IMPACT_score_sh_accessvector_NETWORK)+" VULNERABILIDADES EL VECTOR DE ACCESO ES NETWORK ")
print("            -    EN  "+str(cvssV2_no_IMPACT_score_sh_accessvector_LOCAL)+" VULNERABILIDADES EL VECTOR DE ACCESO ES LOCAL ")
print("            -    EN  "+str(cvssV2_no_IMPACT_score_sh_accessvector_PHYSICAL)+" VULNERABILIDADES EL VECTOR DE ACCESO ES PHYSICAL ")
print("            -    EN  "+str(cvssV2_no_IMPACT_score_sh_accessvector_ADJACENT_NETWORK)+" VULNERABILIDADES EL VECTOR DE ACCESO ES ADJACENT_NETWORK ")
print("\n")
print("            -    EN  "+str(cvssV2_no_IMPACT_score_sh_accesscomplexity_HIGH)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES ALTA ")
print("            -    EN  "+str(cvssV2_no_IMPACT_score_sh_accesscomplexity_LOW)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES BAJA ")
print("            -    EN  "+str(cvssV2_no_IMPACT_score_sh_accesscomplexity_MEDIUM)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES MEDIA ")
print("            -    EN  "+str(cvssV2_no_IMPACT_score_sh_accesscomplexity_NONE)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO NO VIENE ESPECIFICADA ")
print("\n")
print("            -    EN  "+str(cvssV2_no_IMPACT_score_sh_authentication_SINGLE)+" VULNERABILIDADES SE REQUIERE AUTENTICACIÓN SENCILLA ")
print("            -    EN  "+str(cvssV2_no_IMPACT_score_sh_authentication_MULTIPLE)+" VULNERABILIDADES SE REQUIERE AUTENTICACIÓN MULTIPLE")
print("            -    EN  "+str(cvssV2_no_IMPACT_score_sh_authentication_NONE)+" VULNERABILIDADES NO SE REQUIERE AUTENTICACIÓN")
print("\n")
print("            -    EN  "+str(cvssV2_no_IMPACT_score_sh_confidentialityImpact_COMPLETE)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES COMPLETO ")
print("            -    EN  "+str(cvssV2_no_IMPACT_score_sh_confidentialityImpact_PARTIAL)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES PARCIAL" )
print("            -    EN  "+str(cvssV2_no_IMPACT_score_sh_confidentialityImpact_NONE)+" VULNERABILIDADES NO EXISTE IMPACTO DE CONFIDENCIALIDAD ")
print("\n")
print("            -    EN  "+str(cvssV2_no_IMPACT_score_sh_integrityImpact_COMPLETE)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES COMPLETO ")
print("            -    EN  "+str(cvssV2_no_IMPACT_score_sh_integrityImpact_PARTIAL)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES PARCIAL" )
print("            -    EN  "+str(cvssV2_no_IMPACT_score_sh_integrityImpact_NONE)+" VULNERABILIDADES NO EXISTE IMPACTO DE INTEGRIDAD ")
print("\n")
print("\n")
print("            -    EN  "+str(cvssV2_no_IMPACT_score_sh_availabilityImpact_COMPLETE)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES COMPLETO ")
print("            -    EN  "+str(cvssV2_no_IMPACT_score_sh_availabilityImpact_PARTIAL)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES PARCIAL" )
print("            -    EN  "+str(cvssV2_no_IMPACT_score_sh_availabilityImpact_NONE)+" VULNERABILIDADES NO EXISTE IMPACTO DE DISPONIBILIDAD ")
print("\n")

            
          
            
            
        
            
print("________________________PORCENTAJES ELEMENTOS VECTOR STRING-PUNTUACION DE IMPACTO CVSSV2 PARTE SMART HOME________________________")
print("\n")        
            
            
    
print("\n")
print(" DE UN TOTAL DE "+str(len(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.availabilityImpact"]))+" VULNERABILIDADES , LOS PORCENTAJES DE ELEMENTOS DE VECTOR STRING SEGUND PUNTUACION DE IMPACTO SON LOS SIGUIENTES:  \n")
print("\n")
print("      -    EN EL "+str(float(((cvssV2_IMPACT_score_10_sh*100)/len(df_cve_sh["CVE_Items.impact.baseMetricV2.impactScore"]))))+" % DE  VULNERABILIDADES LA PUNTUACION DE IMPACTO ES 10. LOS PORCENTAJES DEL VECTOR STRING SON LOS SIGUIENTES:  \n")
print("\n")
print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_10_sh_accessvector_NETWORK*100)/cvssV2_IMPACT_score_10_sh)))+" % DE  VULNERABILIDADES EL VECTOR DE ACCESO ES NETWORK ")
print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_10_sh_accessvector_LOCAL*100)/cvssV2_IMPACT_score_10_sh)))+" % DE  VULNERABILIDADES EL VECTOR DE ACCESO ES LOCAL ")
print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_10_sh_accessvector_PHYSICAL*100)/cvssV2_IMPACT_score_10_sh)))+" % DE  VULNERABILIDADES EL VECTOR DE ACCESO ES PHYSICAL ")
print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_10_sh_accessvector_ADJACENT_NETWORK*100)/cvssV2_IMPACT_score_10_sh)))+" % DE  VULNERABILIDADES EL VECTOR DE ACCESO ES ADJACENT_NETWORK ")
print("\n")
print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_10_sh_accesscomplexity_HIGH*100)/cvssV2_IMPACT_score_10_sh)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES ALTA ")
print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_10_sh_accesscomplexity_LOW*100)/cvssV2_IMPACT_score_10_sh)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES BAJA ")
print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_10_sh_accesscomplexity_MEDIUM*100)/cvssV2_IMPACT_score_10_sh)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES MEDIA ")
print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_10_sh_accesscomplexity_NONE*100)/cvssV2_IMPACT_score_10_sh)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ACCESO NO VIENE ESPECIFICADA ")
print("\n")
print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_10_sh_authentication_SINGLE*100)/cvssV2_IMPACT_score_10_sh)))+" % DE  VULNERABILIDADES SE REQUIERE AUTENTICACIÓN SENCILLA ")
print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_10_sh_authentication_MULTIPLE*100)/cvssV2_IMPACT_score_10_sh)))+" % DE  VULNERABILIDADES SE REQUIERE AUTENTICACIÓN MÚLTIPLE")
print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_10_sh_authentication_NONE*100)/cvssV2_IMPACT_score_10_sh)))+" % DE  VULNERABILIDADES NO VIENE ESPECIFICADO SI SE REQUIERE AUTENTICACIÓN")
print("\n")
print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_10_sh_confidentialityImpact_COMPLETE*100)/cvssV2_IMPACT_score_10_sh)))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES COMPLETO ")
print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_10_sh_confidentialityImpact_PARTIAL*100)/cvssV2_IMPACT_score_10_sh)))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES PARCIAL" )
print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_10_sh_confidentialityImpact_NONE*100)/cvssV2_IMPACT_score_10_sh)))+" % DE  VULNERABILIDADES NO EXISTE IMPACTO DE CONFIDENCIALIDAD ")
print("\n")
print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_10_sh_integrityImpact_COMPLETE*100)/cvssV2_IMPACT_score_10_sh)))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES COMPLETO ")
print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_10_sh_integrityImpact_PARTIAL*100)/cvssV2_IMPACT_score_10_sh)))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES PARCIAL" )
print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_10_sh_integrityImpact_NONE*100)/cvssV2_IMPACT_score_10_sh)))+" % DE  VULNERABILIDADES NO EXISTE IMPACTO DE INTEGRIDAD ")
print("\n")
print("\n")
print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_10_sh_availabilityImpact_COMPLETE*100)/cvssV2_IMPACT_score_10_sh)))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES COMPLETO ")
print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_10_sh_availabilityImpact_PARTIAL*100)/cvssV2_IMPACT_score_10_sh)))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES PARCIAL" )
print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_10_sh_availabilityImpact_NONE*100)/cvssV2_IMPACT_score_10_sh)))+" % DE  VULNERABILIDADES NO EXISTE IMPACTO DE DISPONIBILIDAD ")
print("\n") 
if(cvssV2_IMPACT_score_9_sh>0):
    print("      -    EN EL "+str(float(((cvssV2_IMPACT_score_9_sh*100)/len(df_cve_sh["CVE_Items.impact.baseMetricV2.impactScore"]))))+" % DE  VULNERABILIDADES LA PUNTUACION DE IMPACTO ESTÁ ENTRE 9 Y 10. LOS PORCENTAJES DEL VECTOR STRING SON LOS SIGUIENTES:  \n")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_9_sh_accessvector_NETWORK*100)/cvssV2_IMPACT_score_9_sh)))+" % DE  VULNERABILIDADES EL VECTOR DE ACCESO ES NETWORK ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_9_sh_accessvector_LOCAL*100)/cvssV2_IMPACT_score_9_sh)))+" % DE  VULNERABILIDADES EL VECTOR DE ACCESO ES LOCAL ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_9_sh_accessvector_PHYSICAL*100)/cvssV2_IMPACT_score_9_sh)))+" % DE  VULNERABILIDADES EL VECTOR DE ACCESO ES PHYSICAL ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_9_sh_accessvector_ADJACENT_NETWORK*100)/cvssV2_IMPACT_score_9_sh)))+" % DE  VULNERABILIDADES EL VECTOR DE ACCESO ES ADJACENT_NETWORK ")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_9_sh_accesscomplexity_HIGH*100)/cvssV2_IMPACT_score_9_sh)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES ALTA ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_9_sh_accesscomplexity_LOW*100)/cvssV2_IMPACT_score_9_sh)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES BAJA ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_9_sh_accesscomplexity_MEDIUM*100)/cvssV2_IMPACT_score_9_sh)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES MEDIA ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_9_sh_accesscomplexity_NONE*100)/cvssV2_IMPACT_score_9_sh)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ACCESO NO VIENE ESPECIFICADA ")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_9_sh_authentication_SINGLE*100)/cvssV2_IMPACT_score_9_sh)))+" % DE  VULNERABILIDADES SE REQUIERE AUTENTICACIÓN SENCILLA ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_9_sh_authentication_MULTIPLE*100)/cvssV2_IMPACT_score_9_sh)))+" % DE  VULNERABILIDADES SE REQUIERE AUTENTICACIÓN MÚLTIPLE")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_9_sh_authentication_NONE*100)/cvssV2_IMPACT_score_9_sh)))+" % DE  VULNERABILIDADES NO VIENE ESPECIFICADO SI SE REQUIERE AUTENTICACIÓN")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_9_sh_confidentialityImpact_COMPLETE*100)/cvssV2_IMPACT_score_9_sh)))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES COMPLETO ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_9_sh_confidentialityImpact_PARTIAL*100)/cvssV2_IMPACT_score_9_sh)))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES PARCIAL" )
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_9_sh_confidentialityImpact_NONE*100)/cvssV2_IMPACT_score_9_sh)))+" % DE  VULNERABILIDADES NO EXISTE IMPACTO DE CONFIDENCIALIDAD ")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_9_sh_integrityImpact_COMPLETE*100)/cvssV2_IMPACT_score_9_sh)))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES COMPLETO ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_9_sh_integrityImpact_PARTIAL*100)/cvssV2_IMPACT_score_9_sh)))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES PARCIAL" )
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_9_sh_integrityImpact_NONE*100)/cvssV2_IMPACT_score_9_sh)))+" % DE  VULNERABILIDADES NO EXISTE IMPACTO DE INTEGRIDAD ")
    print("\n")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_9_sh_availabilityImpact_COMPLETE*100)/cvssV2_IMPACT_score_9_sh)))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES COMPLETO ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_9_sh_availabilityImpact_PARTIAL*100)/cvssV2_IMPACT_score_9_sh)))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES PARCIAL" )
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_9_sh_availabilityImpact_NONE*100)/cvssV2_IMPACT_score_9_sh)))+" % DE  VULNERABILIDADES NO EXISTE IMPACTO DE DISPONIBILIDAD ")           
    print("\n")
if(cvssV2_IMPACT_score_8_sh >0):
    print("      -    EN EL "+str(float(((cvssV2_IMPACT_score_8_sh*100)/len(df_cve_sh["CVE_Items.impact.baseMetricV2.impactScore"]))))+" % DE  VULNERABILIDADES LA PUNTUACION DE IMPACTO ESTÁ ENTRE 8 Y 9. LOS PORCENTAJES DEL VECTOR STRING SON LOS SIGUIENTES:  \n")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_8_sh_accessvector_NETWORK*100)/cvssV2_IMPACT_score_8_sh)))+" % DE  VULNERABILIDADES EL VECTOR DE ACCESO ES NETWORK ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_8_sh_accessvector_LOCAL*100)/cvssV2_IMPACT_score_8_sh)))+" % DE  VULNERABILIDADES EL VECTOR DE ACCESO ES LOCAL ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_8_sh_accessvector_PHYSICAL*100)/cvssV2_IMPACT_score_8_sh)))+" % DE  VULNERABILIDADES EL VECTOR DE ACCESO ES PHYSICAL ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_8_sh_accessvector_ADJACENT_NETWORK*100)/cvssV2_IMPACT_score_8_sh)))+" % DE  VULNERABILIDADES EL VECTOR DE ACCESO ES ADJACENT_NETWORK ")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_8_sh_accesscomplexity_HIGH*100)/cvssV2_IMPACT_score_8_sh)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES ALTA ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_8_sh_accesscomplexity_LOW*100)/cvssV2_IMPACT_score_8_sh)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES BAJA ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_8_sh_accesscomplexity_MEDIUM*100)/cvssV2_IMPACT_score_8_sh)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES MEDIA ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_8_sh_accesscomplexity_NONE*100)/cvssV2_IMPACT_score_8_sh)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ACCESO NO VIENE ESPECIFICADA ")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_8_sh_authentication_SINGLE*100)/cvssV2_IMPACT_score_8_sh)))+" % DE  VULNERABILIDADES SE REQUIERE AUTENTICACIÓN SENCILLA ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_8_sh_authentication_MULTIPLE*100)/cvssV2_IMPACT_score_8_sh)))+" % DE  VULNERABILIDADES SE REQUIERE AUTENTICACIÓN MÚLTIPLE")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_8_sh_authentication_NONE*100)/cvssV2_IMPACT_score_8_sh)))+" % DE  VULNERABILIDADES NO VIENE ESPECIFICADO SI SE REQUIERE AUTENTICACIÓN")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_8_sh_confidentialityImpact_COMPLETE*100)/cvssV2_IMPACT_score_8_sh)))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES COMPLETO ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_8_sh_confidentialityImpact_PARTIAL*100)/cvssV2_IMPACT_score_8_sh)))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES PARCIAL" )
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_8_sh_confidentialityImpact_NONE*100)/cvssV2_IMPACT_score_8_sh)))+" % DE  VULNERABILIDADES NO EXISTE IMPACTO DE CONFIDENCIALIDAD ")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_8_sh_integrityImpact_COMPLETE*100)/cvssV2_IMPACT_score_8_sh)))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES COMPLETO ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_8_sh_integrityImpact_PARTIAL*100)/cvssV2_IMPACT_score_8_sh)))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES PARCIAL" )
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_8_sh_integrityImpact_NONE*100)/cvssV2_IMPACT_score_8_sh)))+" % DE  VULNERABILIDADES NO EXISTE IMPACTO DE INTEGRIDAD ")
    print("\n")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_8_sh_availabilityImpact_COMPLETE*100)/cvssV2_IMPACT_score_8_sh)))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES COMPLETO ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_8_sh_availabilityImpact_PARTIAL*100)/cvssV2_IMPACT_score_8_sh)))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES PARCIAL" )
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_8_sh_availabilityImpact_NONE*100)/cvssV2_IMPACT_score_8_sh)))+" % DE  VULNERABILIDADES NO EXISTE IMPACTO DE DISPONIBILIDAD ")           
    print("\n")
if(cvssV2_IMPACT_score_7_sh >0):
    print("      -    EN EL "+str(float(((cvssV2_IMPACT_score_7_sh*100)/len(df_cve_sh["CVE_Items.impact.baseMetricV2.impactScore"]))))+" % DE  VULNERABILIDADES LA PUNTUACION DE IMPACTO ESTÁ ENTRE 7 Y 8. LOS PORCENTAJES DEL VECTOR STRING SON LOS SIGUIENTES:  \n")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_7_sh_accessvector_NETWORK*100)/cvssV2_IMPACT_score_7_sh)))+" % DE  VULNERABILIDADES EL VECTOR DE ACCESO ES NETWORK ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_7_sh_accessvector_LOCAL*100)/cvssV2_IMPACT_score_7_sh)))+" % DE  VULNERABILIDADES EL VECTOR DE ACCESO ES LOCAL ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_7_sh_accessvector_PHYSICAL*100)/cvssV2_IMPACT_score_7_sh)))+" % DE  VULNERABILIDADES EL VECTOR DE ACCESO ES PHYSICAL ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_7_sh_accessvector_ADJACENT_NETWORK*100)/cvssV2_IMPACT_score_7_sh)))+" % DE  VULNERABILIDADES EL VECTOR DE ACCESO ES ADJACENT_NETWORK ")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_7_sh_accesscomplexity_HIGH*100)/cvssV2_IMPACT_score_7_sh)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES ALTA ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_7_sh_accesscomplexity_LOW*100)/cvssV2_IMPACT_score_7_sh)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES BAJA ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_7_sh_accesscomplexity_MEDIUM*100)/cvssV2_IMPACT_score_7_sh)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES MEDIA ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_7_sh_accesscomplexity_NONE*100)/cvssV2_IMPACT_score_7_sh)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ACCESO NO VIENE ESPECIFICADA ")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_7_sh_authentication_SINGLE*100)/cvssV2_IMPACT_score_7_sh)))+" % DE  VULNERABILIDADES SE REQUIERE AUTENTICACIÓN SENCILLA ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_7_sh_authentication_MULTIPLE*100)/cvssV2_IMPACT_score_7_sh)))+" % DE  VULNERABILIDADES SE REQUIERE AUTENTICACIÓN MÚLTIPLE")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_7_sh_authentication_NONE*100)/cvssV2_IMPACT_score_7_sh)))+" % DE  VULNERABILIDADES NO VIENE ESPECIFICADO SI SE REQUIERE AUTENTICACIÓN")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_7_sh_confidentialityImpact_COMPLETE*100)/cvssV2_IMPACT_score_7_sh)))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES COMPLETO ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_7_sh_confidentialityImpact_PARTIAL*100)/cvssV2_IMPACT_score_7_sh)))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES PARCIAL" )
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_7_sh_confidentialityImpact_NONE*100)/cvssV2_IMPACT_score_7_sh)))+" % DE  VULNERABILIDADES NO EXISTE IMPACTO DE CONFIDENCIALIDAD ")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_7_sh_integrityImpact_COMPLETE*100)/cvssV2_IMPACT_score_7_sh)))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES COMPLETO ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_7_sh_integrityImpact_PARTIAL*100)/cvssV2_IMPACT_score_7_sh)))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES PARCIAL" )
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_7_sh_integrityImpact_NONE*100)/cvssV2_IMPACT_score_7_sh)))+" % DE  VULNERABILIDADES NO EXISTE IMPACTO DE INTEGRIDAD ")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_7_sh_availabilityImpact_COMPLETE*100)/cvssV2_IMPACT_score_7_sh)))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES COMPLETO ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_7_sh_availabilityImpact_PARTIAL*100)/cvssV2_IMPACT_score_7_sh)))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES PARCIAL" )
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_7_sh_availabilityImpact_NONE*100)/cvssV2_IMPACT_score_7_sh)))+" % DE  VULNERABILIDADES NO EXISTE IMPACTO DE DISPONIBILIDAD ")           
    print("\n")
if(cvssV2_IMPACT_score_6_sh >0):
    print("      -    EN EL "+str(float(((cvssV2_IMPACT_score_6_sh*100)/len(df_cve_sh["CVE_Items.impact.baseMetricV2.impactScore"]))))+" % DE  VULNERABILIDADES LA PUNTUACION DE IMPACTO ESTÁ ENTRE 6 Y 7. LOS PORCENTAJES DEL VECTOR STRING SON LOS SIGUIENTES:  \n")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_6_sh_accessvector_NETWORK*100)/cvssV2_IMPACT_score_6_sh)))+" % DE  VULNERABILIDADES EL VECTOR DE ACCESO ES NETWORK ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_6_sh_accessvector_LOCAL*100)/cvssV2_IMPACT_score_6_sh)))+" % DE  VULNERABILIDADES EL VECTOR DE ACCESO ES LOCAL ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_6_sh_accessvector_PHYSICAL*100)/cvssV2_IMPACT_score_6_sh)))+" % DE  VULNERABILIDADES EL VECTOR DE ACCESO ES PHYSICAL ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_6_sh_accessvector_ADJACENT_NETWORK*100)/cvssV2_IMPACT_score_6_sh)))+" % DE  VULNERABILIDADES EL VECTOR DE ACCESO ES ADJACENT_NETWORK ")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_6_sh_accesscomplexity_HIGH*100)/cvssV2_IMPACT_score_6_sh)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES ALTA ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_6_sh_accesscomplexity_LOW*100)/cvssV2_IMPACT_score_6_sh)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES BAJA ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_6_sh_accesscomplexity_MEDIUM*100)/cvssV2_IMPACT_score_6_sh)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES MEDIA ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_6_sh_accesscomplexity_NONE*100)/cvssV2_IMPACT_score_6_sh)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ACCESO NO VIENE ESPECIFICADA ")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_6_sh_authentication_SINGLE*100)/cvssV2_IMPACT_score_6_sh)))+" % DE  VULNERABILIDADES SE REQUIERE AUTENTICACIÓN SENCILLA ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_6_sh_authentication_MULTIPLE*100)/cvssV2_IMPACT_score_6_sh)))+" % DE  VULNERABILIDADES SE REQUIERE AUTENTICACIÓN MÚLTIPLE")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_6_sh_authentication_NONE*100)/cvssV2_IMPACT_score_6_sh)))+" % DE  VULNERABILIDADES NO VIENE ESPECIFICADO SI SE REQUIERE AUTENTICACIÓN")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_6_sh_confidentialityImpact_COMPLETE*100)/cvssV2_IMPACT_score_6_sh)))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES COMPLETO ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_6_sh_confidentialityImpact_PARTIAL*100)/cvssV2_IMPACT_score_6_sh)))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES PARCIAL" )
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_6_sh_confidentialityImpact_NONE*100)/cvssV2_IMPACT_score_6_sh)))+" % DE  VULNERABILIDADES NO EXISTE IMPACTO DE CONFIDENCIALIDAD ")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_6_sh_integrityImpact_COMPLETE*100)/cvssV2_IMPACT_score_6_sh)))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES COMPLETO ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_6_sh_integrityImpact_PARTIAL*100)/cvssV2_IMPACT_score_6_sh)))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES PARCIAL" )
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_6_sh_integrityImpact_NONE*100)/cvssV2_IMPACT_score_6_sh)))+" % DE  VULNERABILIDADES NO EXISTE IMPACTO DE INTEGRIDAD ")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_6_sh_availabilityImpact_COMPLETE*100)/cvssV2_IMPACT_score_6_sh)))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES COMPLETO ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_6_sh_availabilityImpact_PARTIAL*100)/cvssV2_IMPACT_score_6_sh)))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES PARCIAL" )
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_6_sh_availabilityImpact_NONE*100)/cvssV2_IMPACT_score_6_sh)))+" % DE  VULNERABILIDADES NO EXISTE IMPACTO DE DISPONIBILIDAD ")   
    print("\n")
if(cvssV2_IMPACT_score_5_sh >0):
    print("      -    EN EL "+str(float(((cvssV2_IMPACT_score_5_sh*100)/len(df_cve_sh["CVE_Items.impact.baseMetricV2.impactScore"]))))+" % DE  VULNERABILIDADES LA PUNTUACION DE IMPACTO ESTÁ ENTRE 5 Y 6. LOS PORCENTAJES DEL VECTOR STRING SON LOS SIGUIENTES:  \n")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_5_sh_accessvector_NETWORK*100)/cvssV2_IMPACT_score_5_sh)))+" % DE  VULNERABILIDADES EL VECTOR DE ACCESO ES NETWORK ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_5_sh_accessvector_LOCAL*100)/cvssV2_IMPACT_score_5_sh)))+" % DE  VULNERABILIDADES EL VECTOR DE ACCESO ES LOCAL ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_5_sh_accessvector_PHYSICAL*100)/cvssV2_IMPACT_score_5_sh)))+" % DE  VULNERABILIDADES EL VECTOR DE ACCESO ES PHYSICAL ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_5_sh_accessvector_ADJACENT_NETWORK*100)/cvssV2_IMPACT_score_5_sh)))+" % DE  VULNERABILIDADES EL VECTOR DE ACCESO ES ADJACENT_NETWORK ")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_5_sh_accesscomplexity_HIGH*100)/cvssV2_IMPACT_score_5_sh)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES ALTA ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_5_sh_accesscomplexity_LOW*100)/cvssV2_IMPACT_score_5_sh)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES BAJA ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_5_sh_accesscomplexity_MEDIUM*100)/cvssV2_IMPACT_score_5_sh)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES MEDIA ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_5_sh_accesscomplexity_NONE*100)/cvssV2_IMPACT_score_5_sh)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ACCESO NO VIENE ESPECIFICADA ")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_5_sh_authentication_SINGLE*100)/cvssV2_IMPACT_score_5_sh)))+" % DE  VULNERABILIDADES SE REQUIERE AUTENTICACIÓN SENCILLA ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_5_sh_authentication_MULTIPLE*100)/cvssV2_IMPACT_score_5_sh)))+" % DE  VULNERABILIDADES SE REQUIERE AUTENTICACIÓN MÚLTIPLE")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_5_sh_authentication_NONE*100)/cvssV2_IMPACT_score_5_sh)))+" % DE  VULNERABILIDADES NO VIENE ESPECIFICADO SI SE REQUIERE AUTENTICACIÓN")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_5_sh_confidentialityImpact_COMPLETE*100)/cvssV2_IMPACT_score_5_sh)))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES COMPLETO ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_5_sh_confidentialityImpact_PARTIAL*100)/cvssV2_IMPACT_score_5_sh)))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES PARCIAL" )
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_5_sh_confidentialityImpact_NONE*100)/cvssV2_IMPACT_score_5_sh)))+" % DE  VULNERABILIDADES NO EXISTE IMPACTO DE CONFIDENCIALIDAD ")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_5_sh_integrityImpact_COMPLETE*100)/cvssV2_IMPACT_score_5_sh)))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES COMPLETO ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_5_sh_integrityImpact_PARTIAL*100)/cvssV2_IMPACT_score_5_sh)))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES PARCIAL" )
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_5_sh_integrityImpact_NONE*100)/cvssV2_IMPACT_score_5_sh)))+" % DE  VULNERABILIDADES NO EXISTE IMPACTO DE INTEGRIDAD ")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_5_sh_availabilityImpact_COMPLETE*100)/cvssV2_IMPACT_score_5_sh)))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES COMPLETO ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_5_sh_availabilityImpact_PARTIAL*100)/cvssV2_IMPACT_score_5_sh)))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES PARCIAL" )
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_5_sh_availabilityImpact_NONE*100)/cvssV2_IMPACT_score_5_sh)))+" % DE  VULNERABILIDADES NO EXISTE IMPACTO DE DISPONIBILIDAD ")
    print("\n")
if(cvssV2_IMPACT_score_4_sh >0):
    print("      -    EN EL "+str(float(((cvssV2_IMPACT_score_4_sh*100)/len(df_cve_sh["CVE_Items.impact.baseMetricV2.impactScore"]))))+" % DE  VULNERABILIDADES LA PUNTUACION DE IMPACTO ESTÁ ENTRE 4 Y 5. LOS PORCENTAJES DEL VECTOR STRING SON LOS SIGUIENTES:  \n")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_4_sh_accessvector_NETWORK*100)/cvssV2_IMPACT_score_4_sh)))+" % DE  VULNERABILIDADES EL VECTOR DE ACCESO ES NETWORK ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_4_sh_accessvector_LOCAL*100)/cvssV2_IMPACT_score_4_sh)))+" % DE  VULNERABILIDADES EL VECTOR DE ACCESO ES LOCAL ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_4_sh_accessvector_PHYSICAL*100)/cvssV2_IMPACT_score_4_sh)))+" % DE  VULNERABILIDADES EL VECTOR DE ACCESO ES PHYSICAL ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_4_sh_accessvector_ADJACENT_NETWORK*100)/cvssV2_IMPACT_score_4_sh)))+" % DE  VULNERABILIDADES EL VECTOR DE ACCESO ES ADJACENT_NETWORK ")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_4_sh_accesscomplexity_HIGH*100)/cvssV2_IMPACT_score_4_sh)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES ALTA ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_4_sh_accesscomplexity_LOW*100)/cvssV2_IMPACT_score_4_sh)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES BAJA ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_4_sh_accesscomplexity_MEDIUM*100)/cvssV2_IMPACT_score_4_sh)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES MEDIA ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_4_sh_accesscomplexity_NONE*100)/cvssV2_IMPACT_score_4_sh)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ACCESO NO VIENE ESPECIFICADA ")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_4_sh_authentication_SINGLE*100)/cvssV2_IMPACT_score_4_sh)))+" % DE  VULNERABILIDADES SE REQUIERE AUTENTICACIÓN SENCILLA ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_4_sh_authentication_MULTIPLE*100)/cvssV2_IMPACT_score_4_sh)))+" % DE  VULNERABILIDADES SE REQUIERE AUTENTICACIÓN MÚLTIPLE")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_4_sh_authentication_NONE*100)/cvssV2_IMPACT_score_4_sh)))+" % DE  VULNERABILIDADES NO VIENE ESPECIFICADO SI SE REQUIERE AUTENTICACIÓN")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_4_sh_confidentialityImpact_COMPLETE*100)/cvssV2_IMPACT_score_4_sh)))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES COMPLETO ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_4_sh_confidentialityImpact_PARTIAL*100)/cvssV2_IMPACT_score_4_sh)))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES PARCIAL" )
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_4_sh_confidentialityImpact_NONE*100)/cvssV2_IMPACT_score_4_sh)))+" % DE  VULNERABILIDADES NO EXISTE IMPACTO DE CONFIDENCIALIDAD ")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_4_sh_integrityImpact_COMPLETE*100)/cvssV2_IMPACT_score_4_sh)))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES COMPLETO ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_4_sh_integrityImpact_PARTIAL*100)/cvssV2_IMPACT_score_4_sh)))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES PARCIAL" )
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_4_sh_integrityImpact_NONE*100)/cvssV2_IMPACT_score_4_sh)))+" % DE  VULNERABILIDADES NO EXISTE IMPACTO DE INTEGRIDAD ")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_4_sh_availabilityImpact_COMPLETE*100)/cvssV2_IMPACT_score_4_sh)))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES COMPLETO ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_4_sh_availabilityImpact_PARTIAL*100)/cvssV2_IMPACT_score_4_sh)))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES PARCIAL" )
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_4_sh_availabilityImpact_NONE*100)/cvssV2_IMPACT_score_4_sh)))+" % DE  VULNERABILIDADES NO EXISTE IMPACTO DE DISPONIBILIDAD ")
    print("\n") 
if(cvssV2_IMPACT_score_3_sh >0):
    print("      -    EN EL "+str(float(((cvssV2_IMPACT_score_3_sh*100)/len(df_cve_sh["CVE_Items.impact.baseMetricV2.impactScore"]))))+" % DE  VULNERABILIDADES LA PUNTUACION DE IMPACTO ESTÁ ENTRE 3 Y 4. LOS PORCENTAJES DEL VECTOR STRING SON LOS SIGUIENTES:  \n")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_3_sh_accessvector_NETWORK*100)/cvssV2_IMPACT_score_3_sh)))+" % DE  VULNERABILIDADES EL VECTOR DE ACCESO ES NETWORK ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_3_sh_accessvector_LOCAL*100)/cvssV2_IMPACT_score_3_sh)))+" % DE  VULNERABILIDADES EL VECTOR DE ACCESO ES LOCAL ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_3_sh_accessvector_PHYSICAL*100)/cvssV2_IMPACT_score_3_sh)))+" % DE  VULNERABILIDADES EL VECTOR DE ACCESO ES PHYSICAL ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_3_sh_accessvector_ADJACENT_NETWORK*100)/cvssV2_IMPACT_score_3_sh)))+" % DE  VULNERABILIDADES EL VECTOR DE ACCESO ES ADJACENT_NETWORK ")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_3_sh_accesscomplexity_HIGH*100)/cvssV2_IMPACT_score_3_sh)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES ALTA ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_3_sh_accesscomplexity_LOW*100)/cvssV2_IMPACT_score_3_sh)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES BAJA ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_3_sh_accesscomplexity_MEDIUM*100)/cvssV2_IMPACT_score_3_sh)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES MEDIA ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_3_sh_accesscomplexity_NONE*100)/cvssV2_IMPACT_score_3_sh)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ACCESO NO VIENE ESPECIFICADA ")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_3_sh_authentication_SINGLE*100)/cvssV2_IMPACT_score_3_sh)))+" % DE  VULNERABILIDADES SE REQUIERE AUTENTICACIÓN SENCILLA ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_3_sh_authentication_MULTIPLE*100)/cvssV2_IMPACT_score_3_sh)))+" % DE  VULNERABILIDADES SE REQUIERE AUTENTICACIÓN MÚLTIPLE")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_3_sh_authentication_NONE*100)/cvssV2_IMPACT_score_3_sh)))+" % DE  VULNERABILIDADES NO VIENE ESPECIFICADO SI SE REQUIERE AUTENTICACIÓN")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_3_sh_confidentialityImpact_COMPLETE*100)/cvssV2_IMPACT_score_3_sh)))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES COMPLETO ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_3_sh_confidentialityImpact_PARTIAL*100)/cvssV2_IMPACT_score_3_sh)))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES PARCIAL" )
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_3_sh_confidentialityImpact_NONE*100)/cvssV2_IMPACT_score_3_sh)))+" % DE  VULNERABILIDADES NO EXISTE IMPACTO DE CONFIDENCIALIDAD ")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_3_sh_integrityImpact_COMPLETE*100)/cvssV2_IMPACT_score_3_sh)))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES COMPLETO ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_3_sh_integrityImpact_PARTIAL*100)/cvssV2_IMPACT_score_3_sh)))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES PARCIAL" )
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_3_sh_integrityImpact_NONE*100)/cvssV2_IMPACT_score_3_sh)))+" % DE  VULNERABILIDADES NO EXISTE IMPACTO DE INTEGRIDAD ")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_3_sh_availabilityImpact_COMPLETE*100)/cvssV2_IMPACT_score_3_sh)))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES COMPLETO ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_3_sh_availabilityImpact_PARTIAL*100)/cvssV2_IMPACT_score_3_sh)))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES PARCIAL" )
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_3_sh_availabilityImpact_NONE*100)/cvssV2_IMPACT_score_3_sh)))+" % DE  VULNERABILIDADES NO EXISTE IMPACTO DE DISPONIBILIDAD ")
    print("\n")
if(cvssV2_IMPACT_score_2_sh>0):
    print("      -    EN EL "+str(float(((cvssV2_IMPACT_score_2_sh*100)/len(df_cve_sh["CVE_Items.impact.baseMetricV2.impactScore"]))))+" % DE  VULNERABILIDADES LA PUNTUACION DE IMPACTO ESTÁ ENTRE 2 Y 3. LOS PORCENTAJES DEL VECTOR STRING SON LOS SIGUIENTES:  \n")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_2_sh_accessvector_NETWORK*100)/cvssV2_IMPACT_score_2_sh)))+" % DE  VULNERABILIDADES EL VECTOR DE ACCESO ES NETWORK ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_2_sh_accessvector_LOCAL*100)/cvssV2_IMPACT_score_2_sh)))+" % DE  VULNERABILIDADES EL VECTOR DE ACCESO ES LOCAL ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_2_sh_accessvector_PHYSICAL*100)/cvssV2_IMPACT_score_2_sh)))+" % DE  VULNERABILIDADES EL VECTOR DE ACCESO ES PHYSICAL ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_2_sh_accessvector_ADJACENT_NETWORK*100)/cvssV2_IMPACT_score_2_sh)))+" % DE  VULNERABILIDADES EL VECTOR DE ACCESO ES ADJACENT_NETWORK ")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_2_sh_accesscomplexity_HIGH*100)/cvssV2_IMPACT_score_2_sh)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES ALTA ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_2_sh_accesscomplexity_LOW*100)/cvssV2_IMPACT_score_2_sh)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES BAJA ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_2_sh_accesscomplexity_MEDIUM*100)/cvssV2_IMPACT_score_2_sh)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES MEDIA ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_2_sh_accesscomplexity_NONE*100)/cvssV2_IMPACT_score_2_sh)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ACCESO NO VIENE ESPECIFICADA ")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_2_sh_authentication_SINGLE*100)/cvssV2_IMPACT_score_2_sh)))+" % DE  VULNERABILIDADES SE REQUIERE AUTENTICACIÓN SENCILLA ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_2_sh_authentication_MULTIPLE*100)/cvssV2_IMPACT_score_2_sh)))+" % DE  VULNERABILIDADES SE REQUIERE AUTENTICACIÓN MÚLTIPLE")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_2_sh_authentication_NONE*100)/cvssV2_IMPACT_score_2_sh)))+" % DE  VULNERABILIDADES NO VIENE ESPECIFICADO SI SE REQUIERE AUTENTICACIÓN")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_2_sh_confidentialityImpact_COMPLETE*100)/cvssV2_IMPACT_score_2_sh)))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES COMPLETO ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_2_sh_confidentialityImpact_PARTIAL*100)/cvssV2_IMPACT_score_2_sh)))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES PARCIAL" )
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_2_sh_confidentialityImpact_NONE*100)/cvssV2_IMPACT_score_2_sh)))+" % DE  VULNERABILIDADES NO EXISTE IMPACTO DE CONFIDENCIALIDAD ")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_2_sh_integrityImpact_COMPLETE*100)/cvssV2_IMPACT_score_2_sh)))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES COMPLETO ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_2_sh_integrityImpact_PARTIAL*100)/cvssV2_IMPACT_score_2_sh)))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES PARCIAL" )
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_2_sh_integrityImpact_NONE*100)/cvssV2_IMPACT_score_2_sh)))+" % DE  VULNERABILIDADES NO EXISTE IMPACTO DE INTEGRIDAD ")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_2_sh_availabilityImpact_COMPLETE*100)/cvssV2_IMPACT_score_2_sh)))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES COMPLETO ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_2_sh_availabilityImpact_PARTIAL*100)/cvssV2_IMPACT_score_2_sh)))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES PARCIAL" )
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_2_sh_availabilityImpact_NONE*100)/cvssV2_IMPACT_score_2_sh)))+" % DE  VULNERABILIDADES NO EXISTE IMPACTO DE DISPONIBILIDAD ")
    print("\n")  
if(cvssV2_IMPACT_score_1_sh>0):
    print("      -    EN EL "+str(float(((cvssV2_IMPACT_score_1_sh*100)/len(df_cve_sh["CVE_Items.impact.baseMetricV2.impactScore"]))))+" % DE  VULNERABILIDADES LA PUNTUACION DE IMPACTO ESTÁ ENTRE 1 Y 2. LOS PORCENTAJES DEL VECTOR STRING SON LOS SIGUIENTES:  \n")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_1_sh_accessvector_NETWORK*100)/cvssV2_IMPACT_score_1_sh)))+" % DE  VULNERABILIDADES EL VECTOR DE ACCESO ES NETWORK ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_1_sh_accessvector_LOCAL*100)/cvssV2_IMPACT_score_1_sh)))+" % DE  VULNERABILIDADES EL VECTOR DE ACCESO ES LOCAL ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_1_sh_accessvector_PHYSICAL*100)/cvssV2_IMPACT_score_1_sh)))+" % DE  VULNERABILIDADES EL VECTOR DE ACCESO ES PHYSICAL ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_1_sh_accessvector_ADJACENT_NETWORK*100)/cvssV2_IMPACT_score_1_sh)))+" % DE  VULNERABILIDADES EL VECTOR DE ACCESO ES ADJACENT_NETWORK ")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_1_sh_accesscomplexity_HIGH*100)/cvssV2_IMPACT_score_1_sh)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES ALTA ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_1_sh_accesscomplexity_LOW*100)/cvssV2_IMPACT_score_1_sh)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES BAJA ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_1_sh_accesscomplexity_MEDIUM*100)/cvssV2_IMPACT_score_1_sh)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES MEDIA ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_1_sh_accesscomplexity_NONE*100)/cvssV2_IMPACT_score_1_sh)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ACCESO NO VIENE ESPECIFICADA ")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_1_sh_authentication_SINGLE*100)/cvssV2_IMPACT_score_1_sh)))+" % DE  VULNERABILIDADES SE REQUIERE AUTENTICACIÓN SENCILLA ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_1_sh_authentication_MULTIPLE*100)/cvssV2_IMPACT_score_1_sh)))+" % DE  VULNERABILIDADES SE REQUIERE AUTENTICACIÓN MÚLTIPLE")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_1_sh_authentication_NONE*100)/cvssV2_IMPACT_score_1_sh)))+" % DE  VULNERABILIDADES NO VIENE ESPECIFICADO SI SE REQUIERE AUTENTICACIÓN")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_1_sh_confidentialityImpact_COMPLETE*100)/cvssV2_IMPACT_score_1_sh)))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES COMPLETO ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_1_sh_confidentialityImpact_PARTIAL*100)/cvssV2_IMPACT_score_1_sh)))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES PARCIAL" )
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_1_sh_confidentialityImpact_NONE*100)/cvssV2_IMPACT_score_1_sh)))+" % DE  VULNERABILIDADES NO EXISTE IMPACTO DE CONFIDENCIALIDAD ")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_1_sh_integrityImpact_COMPLETE*100)/cvssV2_IMPACT_score_1_sh)))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES COMPLETO ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_1_sh_integrityImpact_PARTIAL*100)/cvssV2_IMPACT_score_1_sh)))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES PARCIAL" )
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_1_sh_integrityImpact_NONE*100)/cvssV2_IMPACT_score_1_sh)))+" % DE  VULNERABILIDADES NO EXISTE IMPACTO DE INTEGRIDAD ")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_1_sh_availabilityImpact_COMPLETE*100)/cvssV2_IMPACT_score_1_sh)))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES COMPLETO ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_1_sh_availabilityImpact_PARTIAL*100)/cvssV2_IMPACT_score_1_sh)))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES PARCIAL" )
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_1_sh_availabilityImpact_NONE*100)/cvssV2_IMPACT_score_1_sh)))+" % DE  VULNERABILIDADES NO EXISTE IMPACTO DE DISPONIBILIDAD ")
    print("\n")   
if(cvssV2_IMPACT_score_0_sh):
    print("\n")
    print("      -    EN EL "+str(float(((cvssV2_IMPACT_score_0_sh*100)/len(df_cve_sh["CVE_Items.impact.baseMetricV2.impactScore"]))))+" % DE  VULNERABILIDADES LA PUNTUACION DE IMPACTO ESTÁ ENTRE 0 Y 1. LOS PORCENTAJES DEL VECTOR STRING SON LOS SIGUIENTES:  \n")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_0_sh_accessvector_NETWORK*100)/cvssV2_IMPACT_score_0_sh)))+" % DE  VULNERABILIDADES EL VECTOR DE ACCESO ES NETWORK ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_0_sh_accessvector_LOCAL*100)/cvssV2_IMPACT_score_0_sh)))+" % DE  VULNERABILIDADES EL VECTOR DE ACCESO ES LOCAL ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_0_sh_accessvector_PHYSICAL*100)/cvssV2_IMPACT_score_0_sh)))+" % DE  VULNERABILIDADES EL VECTOR DE ACCESO ES PHYSICAL ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_0_sh_accessvector_ADJACENT_NETWORK*100)/cvssV2_IMPACT_score_0_sh)))+" % DE  VULNERABILIDADES EL VECTOR DE ACCESO ES ADJACENT_NETWORK ")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_0_sh_accesscomplexity_HIGH*100)/cvssV2_IMPACT_score_0_sh)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES ALTA ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_0_sh_accesscomplexity_LOW*100)/cvssV2_IMPACT_score_0_sh)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES BAJA ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_0_sh_accesscomplexity_MEDIUM*100)/cvssV2_IMPACT_score_0_sh)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES MEDIA ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_0_sh_accesscomplexity_NONE*100)/cvssV2_IMPACT_score_0_sh)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ACCESO NO VIENE ESPECIFICADA ")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_0_sh_authentication_SINGLE*100)/cvssV2_IMPACT_score_0_sh)))+" % DE  VULNERABILIDADES SE REQUIERE AUTENTICACIÓN SENCILLA ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_0_sh_authentication_MULTIPLE*100)/cvssV2_IMPACT_score_0_sh)))+" % DE  VULNERABILIDADES SE REQUIERE AUTENTICACIÓN MÚLTIPLE")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_0_sh_authentication_NONE*100)/cvssV2_IMPACT_score_0_sh)))+" % DE  VULNERABILIDADES NO VIENE ESPECIFICADO SI SE REQUIERE AUTENTICACIÓN")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_0_sh_confidentialityImpact_COMPLETE*100)/cvssV2_IMPACT_score_0_sh)))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES COMPLETO ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_0_sh_confidentialityImpact_PARTIAL*100)/cvssV2_IMPACT_score_0_sh)))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES PARCIAL" )
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_0_sh_confidentialityImpact_NONE*100)/cvssV2_IMPACT_score_0_sh)))+" % DE  VULNERABILIDADES NO EXISTE IMPACTO DE CONFIDENCIALIDAD ")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_0_sh_integrityImpact_COMPLETE*100)/cvssV2_IMPACT_score_0_sh)))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES COMPLETO ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_0_sh_integrityImpact_PARTIAL*100)/cvssV2_IMPACT_score_0_sh)))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES PARCIAL" )
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_0_sh_integrityImpact_NONE*100)/cvssV2_IMPACT_score_0_sh)))+" % DE  VULNERABILIDADES NO EXISTE IMPACTO DE INTEGRIDAD ")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_0_sh_availabilityImpact_COMPLETE*100)/cvssV2_IMPACT_score_0_sh)))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES COMPLETO ")
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_0_sh_availabilityImpact_PARTIAL*100)/cvssV2_IMPACT_score_0_sh)))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES PARCIAL" )
    print("            -    EN EL "+str(float(((cvssV2_IMPACT_score_0_sh_availabilityImpact_NONE*100)/cvssV2_IMPACT_score_0_sh)))+" % DE  VULNERABILIDADES NO EXISTE IMPACTO DE DISPONIBILIDAD ")     
print("\n")
print("      -    EN EL "+str(float(((cvssV2_no_IMPACT_score_sh*100)/len(df_cve_sh["CVE_Items.impact.baseMetricV2.impactScore"]))))+" % DE  VULNERABILIDADES LA PUNTUACION DE IMPACTO NO VIENE ESPECIFICADA. LOS PORCENTAJES DEL VECTOR STRING SON LOS SIGUIENTES:  \n")
print("\n")
print("            -    EN EL "+str(float(((cvssV2_no_IMPACT_score_sh_accessvector_NETWORK*100)/cvssV2_no_IMPACT_score_sh)))+" % DE  VULNERABILIDADES EL VECTOR DE ACCESO ES NETWORK ")
print("            -    EN EL "+str(float(((cvssV2_no_IMPACT_score_sh_accessvector_LOCAL*100)/cvssV2_no_IMPACT_score_sh)))+" % DE  VULNERABILIDADES EL VECTOR DE ACCESO ES LOCAL ")
print("            -    EN EL "+str(float(((cvssV2_no_IMPACT_score_sh_accessvector_PHYSICAL*100)/cvssV2_no_IMPACT_score_sh)))+" % DE  VULNERABILIDADES EL VECTOR DE ACCESO ES PHYSICAL ")
print("            -    EN EL "+str(float(((cvssV2_no_IMPACT_score_sh_accessvector_ADJACENT_NETWORK*100)/cvssV2_no_IMPACT_score_sh)))+" % DE  VULNERABILIDADES EL VECTOR DE ACCESO ES ADJACENT_NETWORK ")
print("\n")
print("            -    EN EL "+str(float(((cvssV2_no_IMPACT_score_sh_accesscomplexity_HIGH*100)/cvssV2_no_IMPACT_score_sh)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES ALTA ")
print("            -    EN EL "+str(float(((cvssV2_no_IMPACT_score_sh_accesscomplexity_LOW*100)/cvssV2_no_IMPACT_score_sh)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES BAJA ")
print("            -    EN EL "+str(float(((cvssV2_no_IMPACT_score_sh_accesscomplexity_MEDIUM*100)/cvssV2_no_IMPACT_score_sh)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES MEDIA ")
print("            -    EN EL "+str(float(((cvssV2_no_IMPACT_score_sh_accesscomplexity_NONE*100)/cvssV2_no_IMPACT_score_sh)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ACCESO NO VIENE ESPECIFICADA ")
print("\n")
print("            -    EN EL "+str(float(((cvssV2_no_IMPACT_score_sh_authentication_SINGLE*100)/cvssV2_no_IMPACT_score_sh)))+" % DE  VULNERABILIDADES SE REQUIERE AUTENTICACIÓN SENCILLA ")
print("            -    EN EL "+str(float(((cvssV2_no_IMPACT_score_sh_authentication_MULTIPLE*100)/cvssV2_no_IMPACT_score_sh)))+" % DE  VULNERABILIDADES SE REQUIERE AUTENTICACIÓN MÚLTIPLE")
print("            -    EN EL "+str(float(((cvssV2_no_IMPACT_score_sh_authentication_NONE*100)/cvssV2_no_IMPACT_score_sh)))+" % DE  VULNERABILIDADES NO VIENE ESPECIFICADO SI SE REQUIERE AUTENTICACIÓN")
print("\n")
print("            -    EN EL "+str(float(((cvssV2_no_IMPACT_score_sh_confidentialityImpact_COMPLETE*100)/cvssV2_no_IMPACT_score_sh)))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES COMPLETO ")
print("            -    EN EL "+str(float(((cvssV2_no_IMPACT_score_sh_confidentialityImpact_PARTIAL*100)/cvssV2_no_IMPACT_score_sh)))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES PARCIAL" )
print("            -    EN EL "+str(float(((cvssV2_no_IMPACT_score_sh_confidentialityImpact_NONE*100)/cvssV2_no_IMPACT_score_sh)))+" % DE  VULNERABILIDADES NO EXISTE IMPACTO DE CONFIDENCIALIDAD ")
print("\n")
print("            -    EN EL "+str(float(((cvssV2_no_IMPACT_score_sh_integrityImpact_COMPLETE*100)/cvssV2_no_IMPACT_score_sh)))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES COMPLETO ")
print("            -    EN EL "+str(float(((cvssV2_no_IMPACT_score_sh_integrityImpact_PARTIAL*100)/cvssV2_no_IMPACT_score_sh)))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES PARCIAL" )
print("            -    EN EL "+str(float(((cvssV2_no_IMPACT_score_sh_integrityImpact_NONE*100)/cvssV2_no_IMPACT_score_sh)))+" % DE  VULNERABILIDADES NO EXISTE IMPACTO DE INTEGRIDAD ")
print("\n")
print("            -    EN EL "+str(float(((cvssV2_no_IMPACT_score_sh_availabilityImpact_COMPLETE*100)/cvssV2_no_IMPACT_score_sh)))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES COMPLETO ")
print("            -    EN EL "+str(float(((cvssV2_no_IMPACT_score_sh_availabilityImpact_PARTIAL*100)/cvssV2_no_IMPACT_score_sh)))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES PARCIAL" )
print("            -    EN EL "+str(float(((cvssV2_no_IMPACT_score_sh_availabilityImpact_NONE*100)/cvssV2_no_IMPACT_score_sh)))+" % DE  VULNERABILIDADES NO EXISTE IMPACTO DE DISPONIBILIDAD ")
print("\n")       
            
            
        
            
       

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    


            
        
            
print("________________________ESTADÍSTICAS ELEMENTOS VECTOR STRING-PUNTUACION DE IMPACTO CVSSV2 ________________________")
print("\n")        
print("\n")
print(" DE UN TOTAL DE "+str((len(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.availabilityImpact"]))+(len(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.availabilityImpact"])))+" VULNERABILIDADES , LAS ESTADISTICAS DE ELEMENTOS DE VECTOR STRING SEGUN PUNTUACION DE IMPACTO SON LAS SIGUIENTES:  \n")
print("\n")
print("      -    EN  "+str(cvssV2_IMPACT_score_10_sh+cvssV2_IMPACT_score_10_iot)+" VULNERABILIDADES LA PUNTUACION DE IMPACTO ES 10. LAS ESTADÍSTICAS DEL VECTOR STRING SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_10_sh_accessvector_NETWORK+cvssV2_IMPACT_score_10_iot_accessvector_NETWORK)+" VULNERABILIDADES EL VECTOR DE ACCESO ES NETWORK ")
print("            -    EN  "+str(cvssV2_IMPACT_score_10_sh_accessvector_LOCAL+cvssV2_IMPACT_score_10_iot_accessvector_LOCAL)+" VULNERABILIDADES EL VECTOR DE ACCESO ES LOCAL ")
print("            -    EN  "+str(cvssV2_IMPACT_score_10_sh_accessvector_PHYSICAL+cvssV2_IMPACT_score_10_iot_accessvector_PHYSICAL)+" VULNERABILIDADES EL VECTOR DE ACCESO ES PHYSICAL ")
print("            -    EN  "+str(cvssV2_IMPACT_score_10_sh_accessvector_ADJACENT_NETWORK+cvssV2_IMPACT_score_10_iot_accessvector_ADJACENT_NETWORK)+" VULNERABILIDADES EL VECTOR DE ACCESO ES ADJACENT_NETWORK ")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_10_sh_accesscomplexity_HIGH+cvssV2_IMPACT_score_10_iot_accesscomplexity_HIGH)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES ALTA ")
print("            -    EN  "+str(cvssV2_IMPACT_score_10_sh_accesscomplexity_LOW+cvssV2_IMPACT_score_10_iot_accesscomplexity_LOW)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES BAJA ")
print("            -    EN  "+str(cvssV2_IMPACT_score_10_sh_accesscomplexity_MEDIUM+cvssV2_IMPACT_score_10_iot_accesscomplexity_MEDIUM)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES MEDIA ")
print("            -    EN  "+str(cvssV2_IMPACT_score_10_sh_accesscomplexity_NONE+cvssV2_IMPACT_score_10_iot_accesscomplexity_NONE)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO NO VIENE ESPECIFICADA ")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_10_iot_authentication_SINGLE+cvssV2_IMPACT_score_10_sh_authentication_SINGLE)+" VULNERABILIDADES LA AUTENTICACIÓN ES SENCILLA ")
print("            -    EN  "+str(cvssV2_IMPACT_score_10_iot_authentication_MULTIPLE+cvssV2_IMPACT_score_10_sh_authentication_MULTIPLE)+" VULNERABILIDADES LA AUTENTICACIÓN ES MÚLTIPLE")
print("            -    EN  "+str(cvssV2_IMPACT_score_10_iot_authentication_NONE+cvssV2_IMPACT_score_10_sh_authentication_NONE)+" VULNERABILIDADES LA AUTENTICACIÓN NO VIENE ESPECIFICADA ")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_10_sh_confidentialityImpact_COMPLETE+cvssV2_IMPACT_score_10_iot_confidentialityImpact_COMPLETE)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES COMPLETO ")
print("            -    EN  "+str(cvssV2_IMPACT_score_10_sh_confidentialityImpact_PARTIAL+cvssV2_IMPACT_score_10_iot_confidentialityImpact_PARTIAL)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES PARCIAL" )
print("            -    EN  "+str(cvssV2_IMPACT_score_10_sh_confidentialityImpact_NONE+cvssV2_IMPACT_score_10_iot_confidentialityImpact_NONE)+" VULNERABILIDADES NO EXISTE IMPACTO DE CONFIDENCIALIDAD ")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_10_sh_integrityImpact_COMPLETE+cvssV2_IMPACT_score_10_iot_integrityImpact_COMPLETE)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES COMPLETO ")
print("            -    EN  "+str(cvssV2_IMPACT_score_10_sh_integrityImpact_PARTIAL+cvssV2_IMPACT_score_10_iot_integrityImpact_PARTIAL)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES PARCIAL" )
print("            -    EN  "+str(cvssV2_IMPACT_score_10_sh_integrityImpact_NONE+cvssV2_IMPACT_score_10_iot_integrityImpact_NONE)+" VULNERABILIDADES NO EXISTE IMPACTO DE INTEGRIDAD ")
print("\n")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_10_sh_availabilityImpact_COMPLETE+cvssV2_IMPACT_score_10_iot_availabilityImpact_COMPLETE)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES COMPLETO ")
print("            -    EN  "+str(cvssV2_IMPACT_score_10_sh_availabilityImpact_PARTIAL+cvssV2_IMPACT_score_10_iot_availabilityImpact_PARTIAL)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES PARCIAL" )
print("            -    EN  "+str(cvssV2_IMPACT_score_10_sh_availabilityImpact_NONE+cvssV2_IMPACT_score_10_iot_availabilityImpact_NONE)+" VULNERABILIDADES NO EXISTE IMPACTO DE DISPONIBILIDAD ")
print("\n")
print("      -    EN  "+str(cvssV2_IMPACT_score_9_sh+cvssV2_IMPACT_score_9_iot)+" VULNERABILIDADES LA PUNTUACION DE IMPACTO ESTÁ ENTRE 9 Y 10. LAS ESTADÍSTICAS DEL VECTOR STRING SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_9_sh_accessvector_NETWORK+cvssV2_IMPACT_score_9_iot_accessvector_NETWORK)+" VULNERABILIDADES EL VECTOR DE ACCESO ES NETWORK ")
print("            -    EN  "+str(cvssV2_IMPACT_score_9_sh_accessvector_LOCAL+cvssV2_IMPACT_score_9_iot_accessvector_LOCAL)+" VULNERABILIDADES EL VECTOR DE ACCESO ES LOCAL ")
print("            -    EN  "+str(cvssV2_IMPACT_score_9_sh_accessvector_PHYSICAL+cvssV2_IMPACT_score_9_iot_accessvector_PHYSICAL)+" VULNERABILIDADES EL VECTOR DE ACCESO ES PHYSICAL ")
print("            -    EN  "+str(cvssV2_IMPACT_score_9_sh_accessvector_ADJACENT_NETWORK+cvssV2_IMPACT_score_9_iot_accessvector_ADJACENT_NETWORK)+" VULNERABILIDADES EL VECTOR DE ACCESO ES ADJACENT_NETWORK ")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_9_sh_accesscomplexity_HIGH+cvssV2_IMPACT_score_9_iot_accesscomplexity_HIGH)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES ALTA ")
print("            -    EN  "+str(cvssV2_IMPACT_score_9_sh_accesscomplexity_LOW+cvssV2_IMPACT_score_9_iot_accesscomplexity_LOW)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES BAJA ")
print("            -    EN  "+str(cvssV2_IMPACT_score_9_sh_accesscomplexity_MEDIUM+cvssV2_IMPACT_score_9_iot_accesscomplexity_MEDIUM)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES MEDIA ")
print("            -    EN  "+str(cvssV2_IMPACT_score_9_sh_accesscomplexity_NONE+cvssV2_IMPACT_score_9_iot_accesscomplexity_NONE)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO NO VIENE ESPECIFICADA ")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_9_iot_authentication_SINGLE+cvssV2_IMPACT_score_9_sh_authentication_SINGLE)+" VULNERABILIDADES LA AUTENTICACIÓN ES SENCILLA ")
print("            -    EN  "+str(cvssV2_IMPACT_score_9_iot_authentication_MULTIPLE+cvssV2_IMPACT_score_9_sh_authentication_MULTIPLE)+" VULNERABILIDADES LA AUTENTICACIÓN ES MÚLTIPLE")
print("            -    EN  "+str(cvssV2_IMPACT_score_9_iot_authentication_NONE+cvssV2_IMPACT_score_9_sh_authentication_NONE)+" VULNERABILIDADES LA AUTENTICACIÓN NO VIENE ESPECIFICADA ")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_9_sh_confidentialityImpact_COMPLETE+cvssV2_IMPACT_score_9_iot_confidentialityImpact_COMPLETE)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES COMPLETO ")
print("            -    EN  "+str(cvssV2_IMPACT_score_9_sh_confidentialityImpact_PARTIAL+cvssV2_IMPACT_score_9_iot_confidentialityImpact_PARTIAL)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES PARCIAL" )
print("            -    EN  "+str(cvssV2_IMPACT_score_9_sh_confidentialityImpact_NONE+cvssV2_IMPACT_score_9_iot_confidentialityImpact_NONE)+" VULNERABILIDADES NO EXISTE IMPACTO DE CONFIDENCIALIDAD ")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_9_sh_integrityImpact_COMPLETE+cvssV2_IMPACT_score_9_iot_integrityImpact_COMPLETE)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES COMPLETO ")
print("            -    EN  "+str(cvssV2_IMPACT_score_9_sh_integrityImpact_PARTIAL+cvssV2_IMPACT_score_9_iot_integrityImpact_PARTIAL)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES PARCIAL" )
print("            -    EN  "+str(cvssV2_IMPACT_score_9_sh_integrityImpact_NONE+cvssV2_IMPACT_score_9_iot_integrityImpact_NONE)+" VULNERABILIDADES NO EXISTE IMPACTO DE INTEGRIDAD ")
print("\n")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_9_sh_availabilityImpact_COMPLETE+cvssV2_IMPACT_score_9_iot_availabilityImpact_COMPLETE)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES COMPLETO ")
print("            -    EN  "+str(cvssV2_IMPACT_score_9_sh_availabilityImpact_PARTIAL+cvssV2_IMPACT_score_9_iot_availabilityImpact_PARTIAL)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES PARCIAL" )
print("            -    EN  "+str(cvssV2_IMPACT_score_9_sh_availabilityImpact_NONE+cvssV2_IMPACT_score_9_iot_availabilityImpact_NONE)+" VULNERABILIDADES NO EXISTE IMPACTO DE DISPONIBILIDAD ")
print("\n")
print("      -    EN  "+str(cvssV2_IMPACT_score_8_sh+cvssV2_IMPACT_score_8_iot)+" VULNERABILIDADES LA PUNTUACION DE IMPACTO ESTÁ ENTRE 8 Y 9. LAS ESTADÍSTICAS DEL VECTOR STRING SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_8_sh_accessvector_NETWORK+cvssV2_IMPACT_score_8_iot_accessvector_NETWORK)+" VULNERABILIDADES EL VECTOR DE ACCESO ES NETWORK ")
print("            -    EN  "+str(cvssV2_IMPACT_score_8_sh_accessvector_LOCAL+cvssV2_IMPACT_score_8_iot_accessvector_LOCAL)+" VULNERABILIDADES EL VECTOR DE ACCESO ES LOCAL ")
print("            -    EN  "+str(cvssV2_IMPACT_score_8_sh_accessvector_PHYSICAL+cvssV2_IMPACT_score_8_iot_accessvector_PHYSICAL)+" VULNERABILIDADES EL VECTOR DE ACCESO ES PHYSICAL ")
print("            -    EN  "+str(cvssV2_IMPACT_score_8_sh_accessvector_ADJACENT_NETWORK+cvssV2_IMPACT_score_8_iot_accessvector_ADJACENT_NETWORK)+" VULNERABILIDADES EL VECTOR DE ACCESO ES ADJACENT_NETWORK ")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_8_sh_accesscomplexity_HIGH+cvssV2_IMPACT_score_8_iot_accesscomplexity_HIGH)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES ALTA ")
print("            -    EN  "+str(cvssV2_IMPACT_score_8_sh_accesscomplexity_LOW+cvssV2_IMPACT_score_8_iot_accesscomplexity_LOW)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES BAJA ")
print("            -    EN  "+str(cvssV2_IMPACT_score_8_sh_accesscomplexity_MEDIUM+cvssV2_IMPACT_score_8_iot_accesscomplexity_MEDIUM)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES MEDIA ")
print("            -    EN  "+str(cvssV2_IMPACT_score_8_sh_accesscomplexity_NONE+cvssV2_IMPACT_score_8_iot_accesscomplexity_NONE)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO NO VIENE ESPECIFICADA ")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_8_iot_authentication_SINGLE+cvssV2_IMPACT_score_8_sh_authentication_SINGLE)+" VULNERABILIDADES LA AUTENTICACIÓN ES SENCILLA ")
print("            -    EN  "+str(cvssV2_IMPACT_score_8_iot_authentication_MULTIPLE+cvssV2_IMPACT_score_8_sh_authentication_MULTIPLE)+" VULNERABILIDADES LA AUTENTICACIÓN ES MÚLTIPLE")
print("            -    EN  "+str(cvssV2_IMPACT_score_8_iot_authentication_NONE+cvssV2_IMPACT_score_8_sh_authentication_NONE)+" VULNERABILIDADES LA AUTENTICACIÓN NO VIENE ESPECIFICADA ")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_8_sh_confidentialityImpact_COMPLETE+cvssV2_IMPACT_score_8_iot_confidentialityImpact_COMPLETE)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES COMPLETO ")
print("            -    EN  "+str(cvssV2_IMPACT_score_8_sh_confidentialityImpact_PARTIAL+cvssV2_IMPACT_score_8_iot_confidentialityImpact_PARTIAL)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES PARCIAL" )
print("            -    EN  "+str(cvssV2_IMPACT_score_8_sh_confidentialityImpact_NONE+cvssV2_IMPACT_score_8_iot_confidentialityImpact_NONE)+" VULNERABILIDADES NO EXISTE IMPACTO DE CONFIDENCIALIDAD ")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_8_sh_integrityImpact_COMPLETE+cvssV2_IMPACT_score_8_iot_integrityImpact_COMPLETE)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES COMPLETO ")
print("            -    EN  "+str(cvssV2_IMPACT_score_8_sh_integrityImpact_PARTIAL+cvssV2_IMPACT_score_8_iot_integrityImpact_PARTIAL)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES PARCIAL" )
print("            -    EN  "+str(cvssV2_IMPACT_score_8_sh_integrityImpact_NONE+cvssV2_IMPACT_score_8_iot_integrityImpact_NONE)+" VULNERABILIDADES NO EXISTE IMPACTO DE INTEGRIDAD ")
print("\n")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_8_sh_availabilityImpact_COMPLETE+cvssV2_IMPACT_score_8_iot_availabilityImpact_COMPLETE)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES COMPLETO ")
print("            -    EN  "+str(cvssV2_IMPACT_score_8_sh_availabilityImpact_PARTIAL+cvssV2_IMPACT_score_8_iot_availabilityImpact_PARTIAL)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES PARCIAL" )
print("            -    EN  "+str(cvssV2_IMPACT_score_8_sh_availabilityImpact_NONE+cvssV2_IMPACT_score_8_iot_availabilityImpact_NONE)+" VULNERABILIDADES NO EXISTE IMPACTO DE DISPONIBILIDAD ")    
print("\n")
print("      -    EN  "+str(cvssV2_IMPACT_score_7_sh+cvssV2_IMPACT_score_7_iot)+" VULNERABILIDADES LA PUNTUACION DE IMPACTO ESTÁ ENTRE 7 Y 8. LAS ESTADÍSTICAS DEL VECTOR STRING SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_7_sh_accessvector_NETWORK+cvssV2_IMPACT_score_7_iot_accessvector_NETWORK)+" VULNERABILIDADES EL VECTOR DE ACCESO ES NETWORK ")
print("            -    EN  "+str(cvssV2_IMPACT_score_7_sh_accessvector_LOCAL+cvssV2_IMPACT_score_7_iot_accessvector_LOCAL)+" VULNERABILIDADES EL VECTOR DE ACCESO ES LOCAL ")
print("            -    EN  "+str(cvssV2_IMPACT_score_7_sh_accessvector_PHYSICAL+cvssV2_IMPACT_score_7_iot_accessvector_PHYSICAL)+" VULNERABILIDADES EL VECTOR DE ACCESO ES PHYSICAL ")
print("            -    EN  "+str(cvssV2_IMPACT_score_7_sh_accessvector_ADJACENT_NETWORK+cvssV2_IMPACT_score_7_iot_accessvector_ADJACENT_NETWORK)+" VULNERABILIDADES EL VECTOR DE ACCESO ES ADJACENT_NETWORK ")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_7_sh_accesscomplexity_HIGH+cvssV2_IMPACT_score_7_iot_accesscomplexity_HIGH)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES ALTA ")
print("            -    EN  "+str(cvssV2_IMPACT_score_7_sh_accesscomplexity_LOW+cvssV2_IMPACT_score_7_iot_accesscomplexity_LOW)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES BAJA ")
print("            -    EN  "+str(cvssV2_IMPACT_score_7_sh_accesscomplexity_MEDIUM+cvssV2_IMPACT_score_7_iot_accesscomplexity_MEDIUM)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES MEDIA ")
print("            -    EN  "+str(cvssV2_IMPACT_score_7_sh_accesscomplexity_NONE+cvssV2_IMPACT_score_7_iot_accesscomplexity_NONE)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO NO VIENE ESPECIFICADA ")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_7_iot_authentication_SINGLE+cvssV2_IMPACT_score_7_sh_authentication_SINGLE)+" VULNERABILIDADES LA AUTENTICACIÓN ES SENCILLA ")
print("            -    EN  "+str(cvssV2_IMPACT_score_7_iot_authentication_MULTIPLE+cvssV2_IMPACT_score_7_sh_authentication_MULTIPLE)+" VULNERABILIDADES LA AUTENTICACIÓN ES MÚLTIPLE")
print("            -    EN  "+str(cvssV2_IMPACT_score_7_iot_authentication_NONE+cvssV2_IMPACT_score_7_sh_authentication_NONE)+" VULNERABILIDADES LA AUTENTICACIÓN NO VIENE ESPECIFICADA ")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_7_sh_confidentialityImpact_COMPLETE+cvssV2_IMPACT_score_7_iot_confidentialityImpact_COMPLETE)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES COMPLETO ")
print("            -    EN  "+str(cvssV2_IMPACT_score_7_sh_confidentialityImpact_PARTIAL+cvssV2_IMPACT_score_7_iot_confidentialityImpact_PARTIAL)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES PARCIAL" )
print("            -    EN  "+str(cvssV2_IMPACT_score_7_sh_confidentialityImpact_NONE+cvssV2_IMPACT_score_7_iot_confidentialityImpact_NONE)+" VULNERABILIDADES NO EXISTE IMPACTO DE CONFIDENCIALIDAD ")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_7_sh_integrityImpact_COMPLETE+cvssV2_IMPACT_score_7_iot_integrityImpact_COMPLETE)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES COMPLETO ")
print("            -    EN  "+str(cvssV2_IMPACT_score_7_sh_integrityImpact_PARTIAL+cvssV2_IMPACT_score_7_iot_integrityImpact_PARTIAL)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES PARCIAL" )
print("            -    EN  "+str(cvssV2_IMPACT_score_7_sh_integrityImpact_NONE+cvssV2_IMPACT_score_7_iot_integrityImpact_NONE)+" VULNERABILIDADES NO EXISTE IMPACTO DE INTEGRIDAD ")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_7_sh_availabilityImpact_COMPLETE+cvssV2_IMPACT_score_7_iot_availabilityImpact_COMPLETE)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES COMPLETO ")
print("            -    EN  "+str(cvssV2_IMPACT_score_7_sh_availabilityImpact_PARTIAL+cvssV2_IMPACT_score_7_iot_availabilityImpact_PARTIAL)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES PARCIAL" )
print("            -    EN  "+str(cvssV2_IMPACT_score_7_sh_availabilityImpact_NONE+cvssV2_IMPACT_score_7_iot_availabilityImpact_NONE)+" VULNERABILIDADES NO EXISTE IMPACTO DE DISPONIBILIDAD ")
print("\n")
print("      -    EN  "+str(cvssV2_IMPACT_score_6_sh+cvssV2_IMPACT_score_6_iot)+" VULNERABILIDADES LA PUNTUACION DE IMPACTO ESTÁ ENTRE 6 Y 7. LAS ESTADÍSTICAS DEL VECTOR STRING SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_6_sh_accessvector_NETWORK+cvssV2_IMPACT_score_6_iot_accessvector_NETWORK)+" VULNERABILIDADES EL VECTOR DE ACCESO ES NETWORK ")
print("            -    EN  "+str(cvssV2_IMPACT_score_6_sh_accessvector_LOCAL+cvssV2_IMPACT_score_6_iot_accessvector_LOCAL)+" VULNERABILIDADES EL VECTOR DE ACCESO ES LOCAL ")
print("            -    EN  "+str(cvssV2_IMPACT_score_6_sh_accessvector_PHYSICAL+cvssV2_IMPACT_score_6_iot_accessvector_PHYSICAL)+" VULNERABILIDADES EL VECTOR DE ACCESO ES PHYSICAL ")
print("            -    EN  "+str(cvssV2_IMPACT_score_6_sh_accessvector_ADJACENT_NETWORK+cvssV2_IMPACT_score_6_iot_accessvector_ADJACENT_NETWORK)+" VULNERABILIDADES EL VECTOR DE ACCESO ES ADJACENT_NETWORK ")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_6_sh_accesscomplexity_HIGH+cvssV2_IMPACT_score_6_iot_accesscomplexity_HIGH)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES ALTA ")
print("            -    EN  "+str(cvssV2_IMPACT_score_6_sh_accesscomplexity_LOW+cvssV2_IMPACT_score_6_iot_accesscomplexity_LOW)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES BAJA ")
print("            -    EN  "+str(cvssV2_IMPACT_score_6_sh_accesscomplexity_MEDIUM+cvssV2_IMPACT_score_6_iot_accesscomplexity_MEDIUM)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES MEDIA ")
print("            -    EN  "+str(cvssV2_IMPACT_score_6_sh_accesscomplexity_NONE+cvssV2_IMPACT_score_6_iot_accesscomplexity_NONE)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO NO VIENE ESPECIFICADA ")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_6_iot_authentication_SINGLE+cvssV2_IMPACT_score_6_sh_authentication_SINGLE)+" VULNERABILIDADES LA AUTENTICACIÓN ES SENCILLA ")
print("            -    EN  "+str(cvssV2_IMPACT_score_6_iot_authentication_MULTIPLE+cvssV2_IMPACT_score_6_sh_authentication_MULTIPLE)+" VULNERABILIDADES LA AUTENTICACIÓN ES MÚLTIPLE")
print("            -    EN  "+str(cvssV2_IMPACT_score_6_iot_authentication_NONE+cvssV2_IMPACT_score_6_sh_authentication_NONE)+" VULNERABILIDADES LA AUTENTICACIÓN NO VIENE ESPECIFICADA ")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_6_sh_confidentialityImpact_COMPLETE+cvssV2_IMPACT_score_6_iot_confidentialityImpact_COMPLETE)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES COMPLETO ")
print("            -    EN  "+str(cvssV2_IMPACT_score_6_sh_confidentialityImpact_PARTIAL+cvssV2_IMPACT_score_6_iot_confidentialityImpact_PARTIAL)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES PARCIAL" )
print("            -    EN  "+str(cvssV2_IMPACT_score_6_sh_confidentialityImpact_NONE+cvssV2_IMPACT_score_6_iot_confidentialityImpact_NONE)+" VULNERABILIDADES NO EXISTE IMPACTO DE CONFIDENCIALIDAD ")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_6_sh_integrityImpact_COMPLETE+cvssV2_IMPACT_score_6_iot_integrityImpact_COMPLETE)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES COMPLETO ")
print("            -    EN  "+str(cvssV2_IMPACT_score_6_sh_integrityImpact_PARTIAL+cvssV2_IMPACT_score_6_iot_integrityImpact_PARTIAL)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES PARCIAL" )
print("            -    EN  "+str(cvssV2_IMPACT_score_6_sh_integrityImpact_NONE+cvssV2_IMPACT_score_6_iot_integrityImpact_NONE)+" VULNERABILIDADES NO EXISTE IMPACTO DE INTEGRIDAD ")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_6_sh_availabilityImpact_COMPLETE+cvssV2_IMPACT_score_6_iot_availabilityImpact_COMPLETE)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES COMPLETO ")
print("            -    EN  "+str(cvssV2_IMPACT_score_6_sh_availabilityImpact_PARTIAL+cvssV2_IMPACT_score_6_iot_availabilityImpact_PARTIAL)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES PARCIAL" )
print("            -    EN  "+str(cvssV2_IMPACT_score_6_sh_availabilityImpact_NONE+cvssV2_IMPACT_score_6_iot_availabilityImpact_NONE)+" VULNERABILIDADES NO EXISTE IMPACTO DE DISPONIBILIDAD ")
print("\n")
print("      -    EN  "+str(cvssV2_IMPACT_score_5_sh+cvssV2_IMPACT_score_5_iot)+" VULNERABILIDADES LA PUNTUACION DE IMPACTO ESTÁ ENTRE 5 Y 6. LAS ESTADÍSTICAS DEL VECTOR STRING SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_5_sh_accessvector_NETWORK+cvssV2_IMPACT_score_5_iot_accessvector_NETWORK)+" VULNERABILIDADES EL VECTOR DE ACCESO ES NETWORK ")
print("            -    EN  "+str(cvssV2_IMPACT_score_5_sh_accessvector_LOCAL+cvssV2_IMPACT_score_5_iot_accessvector_LOCAL)+" VULNERABILIDADES EL VECTOR DE ACCESO ES LOCAL ")
print("            -    EN  "+str(cvssV2_IMPACT_score_5_sh_accessvector_PHYSICAL+cvssV2_IMPACT_score_5_iot_accessvector_PHYSICAL)+" VULNERABILIDADES EL VECTOR DE ACCESO ES PHYSICAL ")
print("            -    EN  "+str(cvssV2_IMPACT_score_5_sh_accessvector_ADJACENT_NETWORK+cvssV2_IMPACT_score_5_iot_accessvector_ADJACENT_NETWORK)+" VULNERABILIDADES EL VECTOR DE ACCESO ES ADJACENT_NETWORK ")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_5_sh_accesscomplexity_HIGH+cvssV2_IMPACT_score_5_iot_accesscomplexity_HIGH)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES ALTA ")
print("            -    EN  "+str(cvssV2_IMPACT_score_5_sh_accesscomplexity_LOW+cvssV2_IMPACT_score_5_iot_accesscomplexity_LOW)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES BAJA ")
print("            -    EN  "+str(cvssV2_IMPACT_score_5_sh_accesscomplexity_MEDIUM+cvssV2_IMPACT_score_5_iot_accesscomplexity_MEDIUM)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES MEDIA ")
print("            -    EN  "+str(cvssV2_IMPACT_score_5_sh_accesscomplexity_NONE+cvssV2_IMPACT_score_5_iot_accesscomplexity_NONE)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO NO VIENE ESPECIFICADA ")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_5_iot_authentication_SINGLE+cvssV2_IMPACT_score_5_sh_authentication_SINGLE)+" VULNERABILIDADES LA AUTENTICACIÓN ES SENCILLA ")
print("            -    EN  "+str(cvssV2_IMPACT_score_5_iot_authentication_MULTIPLE+cvssV2_IMPACT_score_5_sh_authentication_MULTIPLE)+" VULNERABILIDADES LA AUTENTICACIÓN ES MÚLTIPLE")
print("            -    EN  "+str(cvssV2_IMPACT_score_5_iot_authentication_NONE+cvssV2_IMPACT_score_5_sh_authentication_NONE)+" VULNERABILIDADES LA AUTENTICACIÓN NO VIENE ESPECIFICADA ")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_5_sh_confidentialityImpact_COMPLETE+cvssV2_IMPACT_score_5_iot_confidentialityImpact_COMPLETE)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES COMPLETO ")
print("            -    EN  "+str(cvssV2_IMPACT_score_5_sh_confidentialityImpact_PARTIAL+cvssV2_IMPACT_score_5_iot_confidentialityImpact_PARTIAL)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES PARCIAL" )
print("            -    EN  "+str(cvssV2_IMPACT_score_5_sh_confidentialityImpact_NONE+cvssV2_IMPACT_score_5_iot_confidentialityImpact_NONE)+" VULNERABILIDADES NO EXISTE IMPACTO DE CONFIDENCIALIDAD ")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_5_sh_integrityImpact_COMPLETE+cvssV2_IMPACT_score_5_iot_integrityImpact_COMPLETE)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES COMPLETO ")
print("            -    EN  "+str(cvssV2_IMPACT_score_5_sh_integrityImpact_PARTIAL+cvssV2_IMPACT_score_5_iot_integrityImpact_PARTIAL)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES PARCIAL" )
print("            -    EN  "+str(cvssV2_IMPACT_score_5_sh_integrityImpact_NONE+cvssV2_IMPACT_score_5_iot_integrityImpact_NONE)+" VULNERABILIDADES NO EXISTE IMPACTO DE INTEGRIDAD ")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_5_sh_availabilityImpact_COMPLETE+cvssV2_IMPACT_score_5_iot_availabilityImpact_COMPLETE)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES COMPLETO ")
print("            -    EN  "+str(cvssV2_IMPACT_score_5_sh_availabilityImpact_PARTIAL+cvssV2_IMPACT_score_5_iot_availabilityImpact_PARTIAL)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES PARCIAL" )
print("            -    EN  "+str(cvssV2_IMPACT_score_5_sh_availabilityImpact_NONE+cvssV2_IMPACT_score_5_iot_availabilityImpact_NONE)+" VULNERABILIDADES NO EXISTE IMPACTO DE DISPONIBILIDAD ")
print("\n")
print("      -    EN  "+str(cvssV2_IMPACT_score_4_sh+cvssV2_IMPACT_score_4_iot)+" VULNERABILIDADES LA PUNTUACION DE IMPACTO ESTÁ ENTRE 4 Y 5. LAS ESTADÍSTICAS DEL VECTOR STRING SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_4_sh_accessvector_NETWORK+cvssV2_IMPACT_score_4_iot_accessvector_NETWORK)+" VULNERABILIDADES EL VECTOR DE ACCESO ES NETWORK ")
print("            -    EN  "+str(cvssV2_IMPACT_score_4_sh_accessvector_LOCAL+cvssV2_IMPACT_score_4_iot_accessvector_LOCAL)+" VULNERABILIDADES EL VECTOR DE ACCESO ES LOCAL ")
print("            -    EN  "+str(cvssV2_IMPACT_score_4_sh_accessvector_PHYSICAL+cvssV2_IMPACT_score_4_iot_accessvector_PHYSICAL)+" VULNERABILIDADES EL VECTOR DE ACCESO ES PHYSICAL ")
print("            -    EN  "+str(cvssV2_IMPACT_score_4_sh_accessvector_ADJACENT_NETWORK+cvssV2_IMPACT_score_4_iot_accessvector_ADJACENT_NETWORK)+" VULNERABILIDADES EL VECTOR DE ACCESO ES ADJACENT_NETWORK ")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_4_sh_accesscomplexity_HIGH+cvssV2_IMPACT_score_4_iot_accesscomplexity_HIGH)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES ALTA ")
print("            -    EN  "+str(cvssV2_IMPACT_score_4_sh_accesscomplexity_LOW+cvssV2_IMPACT_score_4_iot_accesscomplexity_LOW)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES BAJA ")
print("            -    EN  "+str(cvssV2_IMPACT_score_4_sh_accesscomplexity_MEDIUM+cvssV2_IMPACT_score_4_iot_accesscomplexity_MEDIUM)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES MEDIA ")
print("            -    EN  "+str(cvssV2_IMPACT_score_4_sh_accesscomplexity_NONE+cvssV2_IMPACT_score_4_iot_accesscomplexity_NONE)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO NO VIENE ESPECIFICADA ")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_4_iot_authentication_SINGLE+cvssV2_IMPACT_score_4_sh_authentication_SINGLE)+" VULNERABILIDADES LA AUTENTICACIÓN ES SENCILLA ")
print("            -    EN  "+str(cvssV2_IMPACT_score_4_iot_authentication_MULTIPLE+cvssV2_IMPACT_score_4_sh_authentication_MULTIPLE)+" VULNERABILIDADES LA AUTENTICACIÓN ES MÚLTIPLE")
print("            -    EN  "+str(cvssV2_IMPACT_score_4_iot_authentication_NONE+cvssV2_IMPACT_score_4_sh_authentication_NONE)+" VULNERABILIDADES LA AUTENTICACIÓN NO VIENE ESPECIFICADA ")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_4_sh_confidentialityImpact_COMPLETE+cvssV2_IMPACT_score_4_iot_confidentialityImpact_COMPLETE)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES COMPLETO ")
print("            -    EN  "+str(cvssV2_IMPACT_score_4_sh_confidentialityImpact_PARTIAL+cvssV2_IMPACT_score_4_iot_confidentialityImpact_PARTIAL)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES PARCIAL" )
print("            -    EN  "+str(cvssV2_IMPACT_score_4_sh_confidentialityImpact_NONE+cvssV2_IMPACT_score_4_iot_confidentialityImpact_NONE)+" VULNERABILIDADES NO EXISTE IMPACTO DE CONFIDENCIALIDAD ")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_4_sh_integrityImpact_COMPLETE+cvssV2_IMPACT_score_4_iot_integrityImpact_COMPLETE)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES COMPLETO ")
print("            -    EN  "+str(cvssV2_IMPACT_score_4_sh_integrityImpact_PARTIAL+cvssV2_IMPACT_score_4_iot_integrityImpact_PARTIAL)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES PARCIAL" )
print("            -    EN  "+str(cvssV2_IMPACT_score_4_sh_integrityImpact_NONE+cvssV2_IMPACT_score_4_iot_integrityImpact_NONE)+" VULNERABILIDADES NO EXISTE IMPACTO DE INTEGRIDAD ")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_4_sh_availabilityImpact_COMPLETE+cvssV2_IMPACT_score_4_iot_availabilityImpact_COMPLETE)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES COMPLETO ")
print("            -    EN  "+str(cvssV2_IMPACT_score_4_sh_availabilityImpact_PARTIAL+cvssV2_IMPACT_score_4_iot_availabilityImpact_PARTIAL)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES PARCIAL" )
print("            -    EN  "+str(cvssV2_IMPACT_score_4_sh_availabilityImpact_NONE+cvssV2_IMPACT_score_4_iot_availabilityImpact_NONE)+" VULNERABILIDADES NO EXISTE IMPACTO DE DISPONIBILIDAD ")
print("\n")
print("      -    EN  "+str(cvssV2_IMPACT_score_3_sh+cvssV2_IMPACT_score_3_iot)+" VULNERABILIDADES LA PUNTUACION DE IMPACTO ESTÁ ENTRE 3 Y 4. LAS ESTADÍSTICAS DEL VECTOR STRING SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_3_sh_accessvector_NETWORK+cvssV2_IMPACT_score_3_iot_accessvector_NETWORK)+" VULNERABILIDADES EL VECTOR DE ACCESO ES NETWORK ")
print("            -    EN  "+str(cvssV2_IMPACT_score_3_sh_accessvector_LOCAL+cvssV2_IMPACT_score_3_iot_accessvector_LOCAL)+" VULNERABILIDADES EL VECTOR DE ACCESO ES LOCAL ")
print("            -    EN  "+str(cvssV2_IMPACT_score_3_sh_accessvector_PHYSICAL+cvssV2_IMPACT_score_3_iot_accessvector_PHYSICAL)+" VULNERABILIDADES EL VECTOR DE ACCESO ES PHYSICAL ")
print("            -    EN  "+str(cvssV2_IMPACT_score_3_sh_accessvector_ADJACENT_NETWORK+cvssV2_IMPACT_score_3_iot_accessvector_ADJACENT_NETWORK)+" VULNERABILIDADES EL VECTOR DE ACCESO ES ADJACENT_NETWORK ")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_3_sh_accesscomplexity_HIGH+cvssV2_IMPACT_score_3_iot_accesscomplexity_HIGH)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES ALTA ")
print("            -    EN  "+str(cvssV2_IMPACT_score_3_sh_accesscomplexity_LOW+cvssV2_IMPACT_score_3_iot_accesscomplexity_LOW)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES BAJA ")
print("            -    EN  "+str(cvssV2_IMPACT_score_3_sh_accesscomplexity_MEDIUM+cvssV2_IMPACT_score_3_iot_accesscomplexity_MEDIUM)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES MEDIA ")
print("            -    EN  "+str(cvssV2_IMPACT_score_3_sh_accesscomplexity_NONE+cvssV2_IMPACT_score_3_iot_accesscomplexity_NONE)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO NO VIENE ESPECIFICADA ")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_3_iot_authentication_SINGLE+cvssV2_IMPACT_score_3_sh_authentication_SINGLE)+" VULNERABILIDADES LA AUTENTICACIÓN ES SENCILLA ")
print("            -    EN  "+str(cvssV2_IMPACT_score_3_iot_authentication_MULTIPLE+cvssV2_IMPACT_score_3_sh_authentication_MULTIPLE)+" VULNERABILIDADES LA AUTENTICACIÓN ES MÚLTIPLE")
print("            -    EN  "+str(cvssV2_IMPACT_score_3_iot_authentication_NONE+cvssV2_IMPACT_score_3_sh_authentication_NONE)+" VULNERABILIDADES LA AUTENTICACIÓN NO VIENE ESPECIFICADA ")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_3_sh_confidentialityImpact_COMPLETE+cvssV2_IMPACT_score_3_iot_confidentialityImpact_COMPLETE)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES COMPLETO ")
print("            -    EN  "+str(cvssV2_IMPACT_score_3_sh_confidentialityImpact_PARTIAL+cvssV2_IMPACT_score_3_iot_confidentialityImpact_PARTIAL)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES PARCIAL" )
print("            -    EN  "+str(cvssV2_IMPACT_score_3_sh_confidentialityImpact_NONE+cvssV2_IMPACT_score_3_iot_confidentialityImpact_NONE)+" VULNERABILIDADES NO EXISTE IMPACTO DE CONFIDENCIALIDAD ")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_3_sh_integrityImpact_COMPLETE+cvssV2_IMPACT_score_3_iot_integrityImpact_COMPLETE)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES COMPLETO ")
print("            -    EN  "+str(cvssV2_IMPACT_score_3_sh_integrityImpact_PARTIAL+cvssV2_IMPACT_score_3_iot_integrityImpact_PARTIAL)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES PARCIAL" )
print("            -    EN  "+str(cvssV2_IMPACT_score_3_sh_integrityImpact_NONE+cvssV2_IMPACT_score_3_iot_integrityImpact_NONE)+" VULNERABILIDADES NO EXISTE IMPACTO DE INTEGRIDAD ")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_3_sh_availabilityImpact_COMPLETE+cvssV2_IMPACT_score_3_iot_availabilityImpact_COMPLETE)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES COMPLETO ")
print("            -    EN  "+str(cvssV2_IMPACT_score_3_sh_availabilityImpact_PARTIAL+cvssV2_IMPACT_score_3_iot_availabilityImpact_PARTIAL)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES PARCIAL" )
print("            -    EN  "+str(cvssV2_IMPACT_score_3_sh_availabilityImpact_NONE+cvssV2_IMPACT_score_3_iot_availabilityImpact_NONE)+" VULNERABILIDADES NO EXISTE IMPACTO DE DISPONIBILIDAD ")
print("\n")
print("      -    EN  "+str(cvssV2_IMPACT_score_2_sh+cvssV2_IMPACT_score_2_iot)+" VULNERABILIDADES LA PUNTUACION DE IMPACTO ESTÁ ENTRE 2 Y 3. LAS ESTADÍSTICAS DEL VECTOR STRING SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_2_sh_accessvector_NETWORK+cvssV2_IMPACT_score_2_iot_accessvector_NETWORK)+" VULNERABILIDADES EL VECTOR DE ACCESO ES NETWORK ")
print("            -    EN  "+str(cvssV2_IMPACT_score_2_sh_accessvector_LOCAL+cvssV2_IMPACT_score_2_iot_accessvector_LOCAL)+" VULNERABILIDADES EL VECTOR DE ACCESO ES LOCAL ")
print("            -    EN  "+str(cvssV2_IMPACT_score_2_sh_accessvector_PHYSICAL+cvssV2_IMPACT_score_2_iot_accessvector_PHYSICAL)+" VULNERABILIDADES EL VECTOR DE ACCESO ES PHYSICAL ")
print("            -    EN  "+str(cvssV2_IMPACT_score_2_sh_accessvector_ADJACENT_NETWORK+cvssV2_IMPACT_score_2_iot_accessvector_ADJACENT_NETWORK)+" VULNERABILIDADES EL VECTOR DE ACCESO ES ADJACENT_NETWORK ")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_2_sh_accesscomplexity_HIGH+cvssV2_IMPACT_score_2_iot_accesscomplexity_HIGH)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES ALTA ")
print("            -    EN  "+str(cvssV2_IMPACT_score_2_sh_accesscomplexity_LOW+cvssV2_IMPACT_score_2_iot_accesscomplexity_LOW)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES BAJA ")
print("            -    EN  "+str(cvssV2_IMPACT_score_2_sh_accesscomplexity_MEDIUM+cvssV2_IMPACT_score_2_iot_accesscomplexity_MEDIUM)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES MEDIA ")
print("            -    EN  "+str(cvssV2_IMPACT_score_2_sh_accesscomplexity_NONE+cvssV2_IMPACT_score_2_iot_accesscomplexity_NONE)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO NO VIENE ESPECIFICADA ")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_2_iot_authentication_SINGLE+cvssV2_IMPACT_score_2_sh_authentication_SINGLE)+" VULNERABILIDADES LA AUTENTICACIÓN ES SENCILLA ")
print("            -    EN  "+str(cvssV2_IMPACT_score_2_iot_authentication_MULTIPLE+cvssV2_IMPACT_score_2_sh_authentication_MULTIPLE)+" VULNERABILIDADES LA AUTENTICACIÓN ES MÚLTIPLE")
print("            -    EN  "+str(cvssV2_IMPACT_score_2_iot_authentication_NONE+cvssV2_IMPACT_score_2_sh_authentication_NONE)+" VULNERABILIDADES LA AUTENTICACIÓN NO VIENE ESPECIFICADA ")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_2_sh_confidentialityImpact_COMPLETE+cvssV2_IMPACT_score_2_iot_confidentialityImpact_COMPLETE)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES COMPLETO ")
print("            -    EN  "+str(cvssV2_IMPACT_score_2_sh_confidentialityImpact_PARTIAL+cvssV2_IMPACT_score_2_iot_confidentialityImpact_PARTIAL)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES PARCIAL" )
print("            -    EN  "+str(cvssV2_IMPACT_score_2_sh_confidentialityImpact_NONE+cvssV2_IMPACT_score_2_iot_confidentialityImpact_NONE)+" VULNERABILIDADES NO EXISTE IMPACTO DE CONFIDENCIALIDAD ")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_2_sh_integrityImpact_COMPLETE+cvssV2_IMPACT_score_2_iot_integrityImpact_COMPLETE)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES COMPLETO ")
print("            -    EN  "+str(cvssV2_IMPACT_score_2_sh_integrityImpact_PARTIAL+cvssV2_IMPACT_score_2_iot_integrityImpact_PARTIAL)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES PARCIAL" )
print("            -    EN  "+str(cvssV2_IMPACT_score_2_sh_integrityImpact_NONE+cvssV2_IMPACT_score_2_iot_integrityImpact_NONE)+" VULNERABILIDADES NO EXISTE IMPACTO DE INTEGRIDAD ")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_2_sh_availabilityImpact_COMPLETE+cvssV2_IMPACT_score_2_iot_availabilityImpact_COMPLETE)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES COMPLETO ")
print("            -    EN  "+str(cvssV2_IMPACT_score_2_sh_availabilityImpact_PARTIAL+cvssV2_IMPACT_score_2_iot_availabilityImpact_PARTIAL)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES PARCIAL" )
print("            -    EN  "+str(cvssV2_IMPACT_score_2_sh_availabilityImpact_NONE+cvssV2_IMPACT_score_2_iot_availabilityImpact_NONE)+" VULNERABILIDADES NO EXISTE IMPACTO DE DISPONIBILIDAD ")
print("\n")
print("      -    EN  "+str(cvssV2_IMPACT_score_1_sh+cvssV2_IMPACT_score_1_iot)+" VULNERABILIDADES LA PUNTUACION DE IMPACTO ESTÁ ENTRE 1 Y 2. LAS ESTADÍSTICAS DEL VECTOR STRING SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_1_sh_accessvector_NETWORK+cvssV2_IMPACT_score_1_iot_accessvector_NETWORK)+" VULNERABILIDADES EL VECTOR DE ACCESO ES NETWORK ")
print("            -    EN  "+str(cvssV2_IMPACT_score_1_sh_accessvector_LOCAL+cvssV2_IMPACT_score_1_iot_accessvector_LOCAL)+" VULNERABILIDADES EL VECTOR DE ACCESO ES LOCAL ")
print("            -    EN  "+str(cvssV2_IMPACT_score_1_sh_accessvector_PHYSICAL+cvssV2_IMPACT_score_1_iot_accessvector_PHYSICAL)+" VULNERABILIDADES EL VECTOR DE ACCESO ES PHYSICAL ")
print("            -    EN  "+str(cvssV2_IMPACT_score_1_sh_accessvector_ADJACENT_NETWORK+cvssV2_IMPACT_score_1_iot_accessvector_ADJACENT_NETWORK)+" VULNERABILIDADES EL VECTOR DE ACCESO ES ADJACENT_NETWORK ")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_1_sh_accesscomplexity_HIGH+cvssV2_IMPACT_score_1_iot_accesscomplexity_HIGH)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES ALTA ")
print("            -    EN  "+str(cvssV2_IMPACT_score_1_sh_accesscomplexity_LOW+cvssV2_IMPACT_score_1_iot_accesscomplexity_LOW)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES BAJA ")
print("            -    EN  "+str(cvssV2_IMPACT_score_1_sh_accesscomplexity_MEDIUM+cvssV2_IMPACT_score_1_iot_accesscomplexity_MEDIUM)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES MEDIA ")
print("            -    EN  "+str(cvssV2_IMPACT_score_1_sh_accesscomplexity_NONE+cvssV2_IMPACT_score_1_iot_accesscomplexity_NONE)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO NO VIENE ESPECIFICADA ")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_1_iot_authentication_SINGLE+cvssV2_IMPACT_score_1_sh_authentication_SINGLE)+" VULNERABILIDADES LA AUTENTICACIÓN ES SENCILLA ")
print("            -    EN  "+str(cvssV2_IMPACT_score_1_iot_authentication_MULTIPLE+cvssV2_IMPACT_score_1_sh_authentication_MULTIPLE)+" VULNERABILIDADES LA AUTENTICACIÓN ES MÚLTIPLE")
print("            -    EN  "+str(cvssV2_IMPACT_score_1_iot_authentication_NONE+cvssV2_IMPACT_score_1_sh_authentication_NONE)+" VULNERABILIDADES LA AUTENTICACIÓN NO VIENE ESPECIFICADA ")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_1_sh_confidentialityImpact_COMPLETE+cvssV2_IMPACT_score_1_iot_confidentialityImpact_COMPLETE)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES COMPLETO ")
print("            -    EN  "+str(cvssV2_IMPACT_score_1_sh_confidentialityImpact_PARTIAL+cvssV2_IMPACT_score_1_iot_confidentialityImpact_PARTIAL)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES PARCIAL" )
print("            -    EN  "+str(cvssV2_IMPACT_score_1_sh_confidentialityImpact_NONE+cvssV2_IMPACT_score_1_iot_confidentialityImpact_NONE)+" VULNERABILIDADES NO EXISTE IMPACTO DE CONFIDENCIALIDAD ")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_1_sh_integrityImpact_COMPLETE+cvssV2_IMPACT_score_1_iot_integrityImpact_COMPLETE)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES COMPLETO ")
print("            -    EN  "+str(cvssV2_IMPACT_score_1_sh_integrityImpact_PARTIAL+cvssV2_IMPACT_score_1_iot_integrityImpact_PARTIAL)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES PARCIAL" )
print("            -    EN  "+str(cvssV2_IMPACT_score_1_sh_integrityImpact_NONE+cvssV2_IMPACT_score_1_iot_integrityImpact_NONE)+" VULNERABILIDADES NO EXISTE IMPACTO DE INTEGRIDAD ")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_1_sh_availabilityImpact_COMPLETE+cvssV2_IMPACT_score_1_iot_availabilityImpact_COMPLETE)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES COMPLETO ")
print("            -    EN  "+str(cvssV2_IMPACT_score_1_sh_availabilityImpact_PARTIAL+cvssV2_IMPACT_score_1_iot_availabilityImpact_PARTIAL)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES PARCIAL" )
print("            -    EN  "+str(cvssV2_IMPACT_score_1_sh_availabilityImpact_NONE+cvssV2_IMPACT_score_1_iot_availabilityImpact_NONE)+" VULNERABILIDADES NO EXISTE IMPACTO DE DISPONIBILIDAD ")
print("\n")
print("      -    EN  "+str(cvssV2_IMPACT_score_0_sh+cvssV2_IMPACT_score_0_iot)+" VULNERABILIDADES LA PUNTUACION DE IMPACTO ESTÁ ENTRE 0 Y 1. LAS ESTADÍSTICAS DEL VECTOR STRING SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_0_sh_accessvector_NETWORK+cvssV2_IMPACT_score_0_iot_accessvector_NETWORK)+" VULNERABILIDADES EL VECTOR DE ACCESO ES NETWORK ")
print("            -    EN  "+str(cvssV2_IMPACT_score_0_sh_accessvector_LOCAL+cvssV2_IMPACT_score_0_iot_accessvector_LOCAL)+" VULNERABILIDADES EL VECTOR DE ACCESO ES LOCAL ")
print("            -    EN  "+str(cvssV2_IMPACT_score_0_sh_accessvector_PHYSICAL+cvssV2_IMPACT_score_0_iot_accessvector_PHYSICAL)+" VULNERABILIDADES EL VECTOR DE ACCESO ES PHYSICAL ")
print("            -    EN  "+str(cvssV2_IMPACT_score_0_sh_accessvector_ADJACENT_NETWORK+cvssV2_IMPACT_score_0_iot_accessvector_ADJACENT_NETWORK)+" VULNERABILIDADES EL VECTOR DE ACCESO ES ADJACENT_NETWORK ")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_0_sh_accesscomplexity_HIGH+cvssV2_IMPACT_score_0_iot_accesscomplexity_HIGH)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES ALTA ")
print("            -    EN  "+str(cvssV2_IMPACT_score_0_sh_accesscomplexity_LOW+cvssV2_IMPACT_score_0_iot_accesscomplexity_LOW)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES BAJA ")
print("            -    EN  "+str(cvssV2_IMPACT_score_0_sh_accesscomplexity_MEDIUM+cvssV2_IMPACT_score_0_iot_accesscomplexity_MEDIUM)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES MEDIA ")
print("            -    EN  "+str(cvssV2_IMPACT_score_0_sh_accesscomplexity_NONE+cvssV2_IMPACT_score_0_iot_accesscomplexity_NONE)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO NO VIENE ESPECIFICADA ")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_0_iot_authentication_SINGLE+cvssV2_IMPACT_score_0_sh_authentication_SINGLE)+" VULNERABILIDADES LA AUTENTICACIÓN ES SENCILLA ")
print("            -    EN  "+str(cvssV2_IMPACT_score_0_iot_authentication_MULTIPLE+cvssV2_IMPACT_score_0_sh_authentication_MULTIPLE)+" VULNERABILIDADES LA AUTENTICACIÓN ES MÚLTIPLE")
print("            -    EN  "+str(cvssV2_IMPACT_score_0_iot_authentication_NONE+cvssV2_IMPACT_score_0_sh_authentication_NONE)+" VULNERABILIDADES LA AUTENTICACIÓN NO VIENE ESPECIFICADA ")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_0_sh_confidentialityImpact_COMPLETE+cvssV2_IMPACT_score_0_iot_confidentialityImpact_COMPLETE)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES COMPLETO ")
print("            -    EN  "+str(cvssV2_IMPACT_score_0_sh_confidentialityImpact_PARTIAL+cvssV2_IMPACT_score_0_iot_confidentialityImpact_PARTIAL)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES PARCIAL" )
print("            -    EN  "+str(cvssV2_IMPACT_score_0_sh_confidentialityImpact_NONE+cvssV2_IMPACT_score_0_iot_confidentialityImpact_NONE)+" VULNERABILIDADES NO EXISTE IMPACTO DE CONFIDENCIALIDAD ")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_0_sh_integrityImpact_COMPLETE+cvssV2_IMPACT_score_0_iot_integrityImpact_COMPLETE)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES COMPLETO ")
print("            -    EN  "+str(cvssV2_IMPACT_score_0_sh_integrityImpact_PARTIAL+cvssV2_IMPACT_score_0_iot_integrityImpact_PARTIAL)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES PARCIAL" )
print("            -    EN  "+str(cvssV2_IMPACT_score_0_sh_integrityImpact_NONE+cvssV2_IMPACT_score_0_iot_integrityImpact_NONE)+" VULNERABILIDADES NO EXISTE IMPACTO DE INTEGRIDAD ")
print("\n")
print("            -    EN  "+str(cvssV2_IMPACT_score_0_sh_availabilityImpact_COMPLETE+cvssV2_IMPACT_score_0_iot_availabilityImpact_COMPLETE)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES COMPLETO ")
print("            -    EN  "+str(cvssV2_IMPACT_score_0_sh_availabilityImpact_PARTIAL+cvssV2_IMPACT_score_0_iot_availabilityImpact_PARTIAL)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES PARCIAL" )
print("            -    EN  "+str(cvssV2_IMPACT_score_0_sh_availabilityImpact_NONE+cvssV2_IMPACT_score_0_iot_availabilityImpact_NONE)+" VULNERABILIDADES NO EXISTE IMPACTO DE DISPONIBILIDAD ")
print("\n")       
print("      -    EN  "+str(cvssV2_no_IMPACT_score_sh+cvssV2_no_IMPACT_score_iot)+" VULNERABILIDADES LA PUNTUACION DE IMPACTO ESTÁ NO ESTÁ ESPECIFICADA. LAS ESTADÍSTICAS DEL VECTOR STRING SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(cvssV2_no_IMPACT_score_sh_accessvector_NETWORK+cvssV2_no_IMPACT_score_iot_accessvector_NETWORK)+" VULNERABILIDADES EL VECTOR DE ACCESO ES NETWORK ")
print("            -    EN  "+str(cvssV2_no_IMPACT_score_sh_accessvector_LOCAL+cvssV2_no_IMPACT_score_iot_accessvector_LOCAL)+" VULNERABILIDADES EL VECTOR DE ACCESO ES LOCAL ")
print("            -    EN  "+str(cvssV2_no_IMPACT_score_sh_accessvector_PHYSICAL+cvssV2_no_IMPACT_score_iot_accessvector_PHYSICAL)+" VULNERABILIDADES EL VECTOR DE ACCESO ES PHYSICAL ")
print("            -    EN  "+str(cvssV2_no_IMPACT_score_sh_accessvector_ADJACENT_NETWORK+cvssV2_no_IMPACT_score_iot_accessvector_ADJACENT_NETWORK)+" VULNERABILIDADES EL VECTOR DE ACCESO ES ADJACENT_NETWORK ")
print("\n")
print("            -    EN  "+str(cvssV2_no_IMPACT_score_sh_accesscomplexity_HIGH+cvssV2_no_IMPACT_score_iot_accesscomplexity_HIGH)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES ALTA ")
print("            -    EN  "+str(cvssV2_no_IMPACT_score_sh_accesscomplexity_LOW+cvssV2_no_IMPACT_score_iot_accesscomplexity_LOW)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES BAJA ")
print("            -    EN  "+str(cvssV2_no_IMPACT_score_sh_accesscomplexity_MEDIUM+cvssV2_no_IMPACT_score_iot_accesscomplexity_MEDIUM)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES MEDIA ")
print("            -    EN  "+str(cvssV2_no_IMPACT_score_sh_accesscomplexity_NONE+cvssV2_no_IMPACT_score_iot_accesscomplexity_NONE)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO NO VIENE ESPECIFICADA ")
print("\n")
print("            -    EN  "+str(cvssV2_no_IMPACT_score_iot_authentication_SINGLE+cvssV2_no_IMPACT_score_sh_authentication_SINGLE)+" VULNERABILIDADES LA AUTENTICACIÓN ES SENCILLA ")
print("            -    EN  "+str(cvssV2_no_IMPACT_score_iot_authentication_MULTIPLE+cvssV2_no_IMPACT_score_sh_authentication_MULTIPLE)+" VULNERABILIDADES LA AUTENTICACIÓN ES MÚLTIPLE")
print("            -    EN  "+str(cvssV2_no_IMPACT_score_iot_authentication_NONE+cvssV2_no_IMPACT_score_sh_authentication_NONE)+" VULNERABILIDADES LA AUTENTICACIÓN NO VIENE ESPECIFICADA ")
print("\n")
print("            -    EN  "+str(cvssV2_no_IMPACT_score_sh_confidentialityImpact_COMPLETE+cvssV2_no_IMPACT_score_iot_confidentialityImpact_COMPLETE)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES COMPLETO ")
print("            -    EN  "+str(cvssV2_no_IMPACT_score_sh_confidentialityImpact_PARTIAL+cvssV2_no_IMPACT_score_iot_confidentialityImpact_PARTIAL)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES PARCIAL" )
print("            -    EN  "+str(cvssV2_no_IMPACT_score_sh_confidentialityImpact_NONE+cvssV2_no_IMPACT_score_iot_confidentialityImpact_NONE)+" VULNERABILIDADES NO EXISTE IMPACTO DE CONFIDENCIALIDAD ")
print("\n")
print("            -    EN  "+str(cvssV2_no_IMPACT_score_sh_integrityImpact_COMPLETE+cvssV2_no_IMPACT_score_iot_integrityImpact_COMPLETE)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES COMPLETO ")
print("            -    EN  "+str(cvssV2_no_IMPACT_score_sh_integrityImpact_PARTIAL+cvssV2_no_IMPACT_score_iot_integrityImpact_PARTIAL)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES PARCIAL" )
print("            -    EN  "+str(cvssV2_no_IMPACT_score_sh_integrityImpact_NONE+cvssV2_no_IMPACT_score_iot_integrityImpact_NONE)+" VULNERABILIDADES NO EXISTE IMPACTO DE INTEGRIDAD ")
print("\n")
print("            -    EN  "+str(cvssV2_no_IMPACT_score_sh_availabilityImpact_COMPLETE+cvssV2_no_IMPACT_score_iot_availabilityImpact_COMPLETE)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES COMPLETO ")
print("            -    EN  "+str(cvssV2_no_IMPACT_score_sh_availabilityImpact_PARTIAL+cvssV2_no_IMPACT_score_iot_availabilityImpact_PARTIAL)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES PARCIAL" )
print("            -    EN  "+str(cvssV2_no_IMPACT_score_sh_availabilityImpact_NONE+cvssV2_no_IMPACT_score_iot_availabilityImpact_NONE)+" VULNERABILIDADES NO EXISTE IMPACTO DE DISPONIBILIDAD ")                
print("\n")
print("\n")       










print("________________________PORCENTAJES ELEMENTOS VECTOR STRING-PUNTUACION DE IMPACTO CVSSV2 IOT Y SMART HOME________________________")
print("\n")           
print("\n")
print(" DE UN TOTAL DE "+str((len(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.availabilityImpact"]))+(len(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.availabilityImpact"])))+" VULNERABILIDADES , LOS PORCENTAJES DE ELEMENTOS DE VECTOR STRING SEGUN PUNTUACION DE IMPACTO SON LAS SIGUIENTES:  \n")
print("\n")
if((cvssV2_IMPACT_score_10_sh+cvssV2_IMPACT_score_10_iot)>0):
    print("      -    EN EL "+str(float((((cvssV2_IMPACT_score_10_sh+cvssV2_IMPACT_score_10_iot)*100)/(len(df_cve_sh["CVE_Items.impact.baseMetricV2.impactScore"])+len(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"])))))+" % DE  VULNERABILIDADES LA PUNTUACION DE IMPACTO ES 10. LOS PORCENTAJES DEL VECTOR STRING SON LOS SIGUIENTES:  \n")
    print("\n")
    print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_10_sh_accessvector_NETWORK+cvssV2_IMPACT_score_10_iot_accessvector_NETWORK)*100)/(cvssV2_IMPACT_score_10_sh+cvssV2_IMPACT_score_10_iot))))+" % DE  VULNERABILIDADES EL VECTOR DE ACCESO ES NETWORK ")
    print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_10_sh_accessvector_LOCAL+cvssV2_IMPACT_score_10_iot_accessvector_LOCAL)*100)/(cvssV2_IMPACT_score_10_sh+cvssV2_IMPACT_score_10_iot))))+" % DE  VULNERABILIDADES EL VECTOR DE ACCESO ES LOCAL ")
    print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_10_sh_accessvector_PHYSICAL+cvssV2_IMPACT_score_10_iot_accessvector_PHYSICAL)*100)/(cvssV2_IMPACT_score_10_sh+cvssV2_IMPACT_score_10_iot))))+" % DE  VULNERABILIDADES EL VECTOR DE ACCESO ES PHYSICAL ")
    print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_10_sh_accessvector_ADJACENT_NETWORK+cvssV2_IMPACT_score_10_iot_accessvector_ADJACENT_NETWORK)*100)/(cvssV2_IMPACT_score_10_sh+cvssV2_IMPACT_score_10_iot))))+" % DE  VULNERABILIDADES EL VECTOR DE ACCESO ES ADJACENT_NETWORK ")
    print("\n")
    print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_10_sh_accesscomplexity_HIGH+cvssV2_IMPACT_score_10_iot_accesscomplexity_HIGH)*100)/(cvssV2_IMPACT_score_10_sh+cvssV2_IMPACT_score_10_iot))))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES ALTA ")
    print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_10_sh_accesscomplexity_LOW+cvssV2_IMPACT_score_10_iot_accesscomplexity_LOW)*100)/(cvssV2_IMPACT_score_10_sh+cvssV2_IMPACT_score_10_iot))))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES BAJA ")
    print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_10_sh_accesscomplexity_MEDIUM+cvssV2_IMPACT_score_10_iot_accesscomplexity_MEDIUM)*100)/(cvssV2_IMPACT_score_10_sh+cvssV2_IMPACT_score_10_iot))))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES MEDIA ")
    print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_10_sh_accesscomplexity_NONE+cvssV2_IMPACT_score_10_iot_accesscomplexity_NONE)*100)/(cvssV2_IMPACT_score_10_sh+cvssV2_IMPACT_score_10_iot))))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ACCESO NO VIENE ESPECIFICADA ")
    print("\n")
    print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_1_iot_authentication_SINGLE+cvssV2_IMPACT_score_1_sh_authentication_SINGLE)*100)/(cvssV2_IMPACT_score_10_sh+cvssV2_IMPACT_score_10_iot))))+" % DE  VULNERABILIDADES SE REQUIERE UNA AUTENTICACIÓN SENCILLA ")
    print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_1_iot_authentication_MULTIPLE+cvssV2_IMPACT_score_1_sh_authentication_MULTIPLE)*100)/(cvssV2_IMPACT_score_10_sh+cvssV2_IMPACT_score_10_iot))))+" % DE  VULNERABILIDADES SE REQUIERE UNA AUTENTICACIÓN MÚLTIPLE")
    print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_1_iot_authentication_NONE+cvssV2_IMPACT_score_1_sh_authentication_NONE)*100)/(cvssV2_IMPACT_score_10_sh+cvssV2_IMPACT_score_10_iot))))+" % DE  VULNERABILIDADES NO VIENEN ESPECIFICADAS LA AUTENTICACIÓN REQUERIDA ")
    print("\n")
    print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_10_sh_confidentialityImpact_COMPLETE+cvssV2_IMPACT_score_10_iot_confidentialityImpact_COMPLETE)*100)/(cvssV2_IMPACT_score_10_sh+cvssV2_IMPACT_score_10_iot))))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES COMPLETO ")
    print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_10_sh_confidentialityImpact_PARTIAL+cvssV2_IMPACT_score_10_iot_confidentialityImpact_PARTIAL)*100)/(cvssV2_IMPACT_score_10_sh+cvssV2_IMPACT_score_10_iot))))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES PARCIAL" )
    print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_10_sh_confidentialityImpact_NONE+cvssV2_IMPACT_score_10_iot_confidentialityImpact_NONE)*100)/(cvssV2_IMPACT_score_10_sh+cvssV2_IMPACT_score_10_iot))))+" % DE  VULNERABILIDADES NO EXISTE IMPACTO DE CONFIDENCIALIDAD ")
    print("\n")
    print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_10_sh_integrityImpact_COMPLETE+cvssV2_IMPACT_score_10_iot_integrityImpact_COMPLETE)*100)/(cvssV2_IMPACT_score_10_sh+cvssV2_IMPACT_score_10_iot))))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES COMPLETO ")
    print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_10_sh_integrityImpact_PARTIAL+cvssV2_IMPACT_score_10_iot_integrityImpact_PARTIAL)*100)/(cvssV2_IMPACT_score_10_sh+cvssV2_IMPACT_score_10_iot))))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES PARCIAL" )
    print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_10_sh_integrityImpact_NONE+cvssV2_IMPACT_score_10_iot_integrityImpact_NONE)*100)/(cvssV2_IMPACT_score_10_sh+cvssV2_IMPACT_score_10_iot))))+" % DE  VULNERABILIDADES NO EXISTE IMPACTO DE INTEGRIDAD ")
    print("\n")
    print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_10_sh_availabilityImpact_COMPLETE+cvssV2_IMPACT_score_10_iot_availabilityImpact_COMPLETE)*100)/(cvssV2_IMPACT_score_10_sh+cvssV2_IMPACT_score_10_iot))))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES COMPLETO ")
    print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_10_sh_availabilityImpact_PARTIAL+cvssV2_IMPACT_score_10_iot_availabilityImpact_PARTIAL)*100)/(cvssV2_IMPACT_score_10_sh+cvssV2_IMPACT_score_10_iot))))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES PARCIAL" )
    print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_10_sh_availabilityImpact_NONE+cvssV2_IMPACT_score_10_iot_availabilityImpact_NONE)*100)/(cvssV2_IMPACT_score_10_sh+cvssV2_IMPACT_score_10_iot))))+" % DE  VULNERABILIDADES NO EXISTE IMPACTO DE DISPONIBILIDAD ")
    print("\n")
if((cvssV2_IMPACT_score_9_sh+cvssV2_IMPACT_score_9_iot)>0):
    print("      -    EN EL "+str(float((((cvssV2_IMPACT_score_9_sh+cvssV2_IMPACT_score_9_iot)*100)/(len(df_cve_sh["CVE_Items.impact.baseMetricV2.impactScore"])+len(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"])))))+" % DE  VULNERABILIDADES LA PUNTUACION DE IMPACTO ESTÁ ENTRE 9 Y 10. LOS PORCENTAJES DEL VECTOR STRING SON LOS SIGUIENTES:  \n")
    print("\n")
    print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_9_sh_accessvector_NETWORK+cvssV2_IMPACT_score_9_iot_accessvector_NETWORK)*100)/(cvssV2_IMPACT_score_9_sh+cvssV2_IMPACT_score_9_iot))))+" % DE  VULNERABILIDADES EL VECTOR DE ACCESO ES NETWORK ")
    print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_9_sh_accessvector_LOCAL+cvssV2_IMPACT_score_9_iot_accessvector_LOCAL)*100)/(cvssV2_IMPACT_score_9_sh+cvssV2_IMPACT_score_9_iot))))+" % DE  VULNERABILIDADES EL VECTOR DE ACCESO ES LOCAL ")
    print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_9_sh_accessvector_PHYSICAL+cvssV2_IMPACT_score_9_iot_accessvector_PHYSICAL)*100)/(cvssV2_IMPACT_score_9_sh+cvssV2_IMPACT_score_9_iot))))+" % DE  VULNERABILIDADES EL VECTOR DE ACCESO ES PHYSICAL ")
    print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_9_sh_accessvector_ADJACENT_NETWORK+cvssV2_IMPACT_score_9_iot_accessvector_ADJACENT_NETWORK)*100)/(cvssV2_IMPACT_score_9_sh+cvssV2_IMPACT_score_9_iot))))+" % DE  VULNERABILIDADES EL VECTOR DE ACCESO ES ADJACENT_NETWORK ")
    print("\n")
    print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_9_sh_accesscomplexity_HIGH+cvssV2_IMPACT_score_9_iot_accesscomplexity_HIGH)*100)/(cvssV2_IMPACT_score_9_sh+cvssV2_IMPACT_score_9_iot))))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES ALTA ")
    print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_9_sh_accesscomplexity_LOW+cvssV2_IMPACT_score_9_iot_accesscomplexity_LOW)*100)/(cvssV2_IMPACT_score_9_sh+cvssV2_IMPACT_score_9_iot))))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES BAJA ")
    print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_9_sh_accesscomplexity_MEDIUM+cvssV2_IMPACT_score_9_iot_accesscomplexity_MEDIUM)*100)/(cvssV2_IMPACT_score_9_sh+cvssV2_IMPACT_score_9_iot))))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES MEDIA ")
    print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_9_sh_accesscomplexity_NONE+cvssV2_IMPACT_score_9_iot_accesscomplexity_NONE)*100)/(cvssV2_IMPACT_score_9_sh+cvssV2_IMPACT_score_9_iot))))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ACCESO NO VIENE ESPECIFICADA ")
    print("\n")
    print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_1_iot_authentication_SINGLE+cvssV2_IMPACT_score_1_sh_authentication_SINGLE)*100)/(cvssV2_IMPACT_score_9_sh+cvssV2_IMPACT_score_9_iot))))+" % DE  VULNERABILIDADES SE REQUIERE UNA AUTENTICACIÓN SENCILLA ")
    print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_1_iot_authentication_MULTIPLE+cvssV2_IMPACT_score_1_sh_authentication_MULTIPLE)*100)/(cvssV2_IMPACT_score_9_sh+cvssV2_IMPACT_score_9_iot))))+" % DE  VULNERABILIDADES SE REQUIERE UNA AUTENTICACIÓN MÚLTIPLE")
    print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_1_iot_authentication_NONE+cvssV2_IMPACT_score_1_sh_authentication_NONE)*100)/(cvssV2_IMPACT_score_9_sh+cvssV2_IMPACT_score_9_iot))))+" % DE  VULNERABILIDADES NO VIENEN ESPECIFICADAS LA AUTENTICACIÓN REQUERIDA ")
    print("\n")
    print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_9_sh_confidentialityImpact_COMPLETE+cvssV2_IMPACT_score_9_iot_confidentialityImpact_COMPLETE)*100)/(cvssV2_IMPACT_score_9_sh+cvssV2_IMPACT_score_9_iot))))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES COMPLETO ")
    print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_9_sh_confidentialityImpact_PARTIAL+cvssV2_IMPACT_score_9_iot_confidentialityImpact_PARTIAL)*100)/(cvssV2_IMPACT_score_9_sh+cvssV2_IMPACT_score_9_iot))))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES PARCIAL" )
    print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_9_sh_confidentialityImpact_NONE+cvssV2_IMPACT_score_9_iot_confidentialityImpact_NONE)*100)/(cvssV2_IMPACT_score_9_sh+cvssV2_IMPACT_score_9_iot))))+" % DE  VULNERABILIDADES NO EXISTE IMPACTO DE CONFIDENCIALIDAD ")
    print("\n")
    print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_9_sh_integrityImpact_COMPLETE+cvssV2_IMPACT_score_9_iot_integrityImpact_COMPLETE)*100)/(cvssV2_IMPACT_score_9_sh+cvssV2_IMPACT_score_9_iot))))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES COMPLETO ")
    print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_9_sh_integrityImpact_PARTIAL+cvssV2_IMPACT_score_9_iot_integrityImpact_PARTIAL)*100)/(cvssV2_IMPACT_score_9_sh+cvssV2_IMPACT_score_9_iot))))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES PARCIAL" )
    print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_9_sh_integrityImpact_NONE+cvssV2_IMPACT_score_9_iot_integrityImpact_NONE)*100)/(cvssV2_IMPACT_score_9_sh+cvssV2_IMPACT_score_9_iot))))+" % DE  VULNERABILIDADES NO EXISTE IMPACTO DE INTEGRIDAD ")
    print("\n")
    print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_9_sh_availabilityImpact_COMPLETE+cvssV2_IMPACT_score_9_iot_availabilityImpact_COMPLETE)*100)/(cvssV2_IMPACT_score_9_sh+cvssV2_IMPACT_score_9_iot))))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES COMPLETO ")
    print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_9_sh_availabilityImpact_PARTIAL+cvssV2_IMPACT_score_9_iot_availabilityImpact_PARTIAL)*100)/(cvssV2_IMPACT_score_9_sh+cvssV2_IMPACT_score_9_iot))))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES PARCIAL" )
    print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_9_sh_availabilityImpact_NONE+cvssV2_IMPACT_score_9_iot_availabilityImpact_NONE)*100)/(cvssV2_IMPACT_score_9_sh+cvssV2_IMPACT_score_9_iot))))+" % DE  VULNERABILIDADES NO EXISTE IMPACTO DE DISPONIBILIDAD ")      
    print("\n")
if((cvssV2_IMPACT_score_8_sh+cvssV2_IMPACT_score_8_iot)>0):
    print("      -    EN EL "+str(float((((cvssV2_IMPACT_score_8_sh+cvssV2_IMPACT_score_8_iot)*100)/(len(df_cve_sh["CVE_Items.impact.baseMetricV2.impactScore"])+len(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"])))))+" % DE  VULNERABILIDADES LA PUNTUACION DE IMPACTO ESTÁ ENTRE 8 Y 9. LOS PORCENTAJES DEL VECTOR STRING SON LOS SIGUIENTES:  \n")
    print("\n")
    print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_8_sh_accessvector_NETWORK+cvssV2_IMPACT_score_8_iot_accessvector_NETWORK)*100)/(cvssV2_IMPACT_score_8_sh+cvssV2_IMPACT_score_8_iot))))+" % DE  VULNERABILIDADES EL VECTOR DE ACCESO ES NETWORK ")
    print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_8_sh_accessvector_LOCAL+cvssV2_IMPACT_score_8_iot_accessvector_LOCAL)*100)/(cvssV2_IMPACT_score_8_sh+cvssV2_IMPACT_score_8_iot))))+" % DE  VULNERABILIDADES EL VECTOR DE ACCESO ES LOCAL ")
    print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_8_sh_accessvector_PHYSICAL+cvssV2_IMPACT_score_8_iot_accessvector_PHYSICAL)*100)/(cvssV2_IMPACT_score_8_sh+cvssV2_IMPACT_score_8_iot))))+" % DE  VULNERABILIDADES EL VECTOR DE ACCESO ES PHYSICAL ")
    print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_8_sh_accessvector_ADJACENT_NETWORK+cvssV2_IMPACT_score_8_iot_accessvector_ADJACENT_NETWORK)*100)/(cvssV2_IMPACT_score_8_sh+cvssV2_IMPACT_score_8_iot))))+" % DE  VULNERABILIDADES EL VECTOR DE ACCESO ES ADJACENT_NETWORK ")
    print("\n")
    print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_8_sh_accesscomplexity_HIGH+cvssV2_IMPACT_score_8_iot_accesscomplexity_HIGH)*100)/(cvssV2_IMPACT_score_8_sh+cvssV2_IMPACT_score_8_iot))))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES ALTA ")
    print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_8_sh_accesscomplexity_LOW+cvssV2_IMPACT_score_8_iot_accesscomplexity_LOW)*100)/(cvssV2_IMPACT_score_8_sh+cvssV2_IMPACT_score_8_iot))))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES BAJA ")
    print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_8_sh_accesscomplexity_MEDIUM+cvssV2_IMPACT_score_8_iot_accesscomplexity_MEDIUM)*100)/(cvssV2_IMPACT_score_8_sh+cvssV2_IMPACT_score_8_iot))))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES MEDIA ")
    print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_8_sh_accesscomplexity_NONE+cvssV2_IMPACT_score_8_iot_accesscomplexity_NONE)*100)/(cvssV2_IMPACT_score_8_sh+cvssV2_IMPACT_score_8_iot))))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ACCESO NO VIENE ESPECIFICADA ")
    print("\n")
    print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_1_iot_authentication_SINGLE+cvssV2_IMPACT_score_1_sh_authentication_SINGLE)*100)/(cvssV2_IMPACT_score_8_sh+cvssV2_IMPACT_score_8_iot))))+" % DE  VULNERABILIDADES SE REQUIERE UNA AUTENTICACIÓN SENCILLA ")
    print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_1_iot_authentication_MULTIPLE+cvssV2_IMPACT_score_1_sh_authentication_MULTIPLE)*100)/(cvssV2_IMPACT_score_8_sh+cvssV2_IMPACT_score_8_iot))))+" % DE  VULNERABILIDADES SE REQUIERE UNA AUTENTICACIÓN MÚLTIPLE")
    print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_1_iot_authentication_NONE+cvssV2_IMPACT_score_1_sh_authentication_NONE)*100)/(cvssV2_IMPACT_score_8_sh+cvssV2_IMPACT_score_8_iot))))+" % DE  VULNERABILIDADES NO VIENEN ESPECIFICADAS LA AUTENTICACIÓN REQUERIDA ")
    print("\n")
    print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_8_sh_confidentialityImpact_COMPLETE+cvssV2_IMPACT_score_8_iot_confidentialityImpact_COMPLETE)*100)/(cvssV2_IMPACT_score_8_sh+cvssV2_IMPACT_score_8_iot))))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES COMPLETO ")
    print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_8_sh_confidentialityImpact_PARTIAL+cvssV2_IMPACT_score_8_iot_confidentialityImpact_PARTIAL)*100)/(cvssV2_IMPACT_score_8_sh+cvssV2_IMPACT_score_8_iot))))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES PARCIAL" )
    print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_8_sh_confidentialityImpact_NONE+cvssV2_IMPACT_score_8_iot_confidentialityImpact_NONE)*100)/(cvssV2_IMPACT_score_8_sh+cvssV2_IMPACT_score_8_iot))))+" % DE  VULNERABILIDADES NO EXISTE IMPACTO DE CONFIDENCIALIDAD ")
    print("\n")
    print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_8_sh_integrityImpact_COMPLETE+cvssV2_IMPACT_score_8_iot_integrityImpact_COMPLETE)*100)/(cvssV2_IMPACT_score_8_sh+cvssV2_IMPACT_score_8_iot))))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES COMPLETO ")
    print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_8_sh_integrityImpact_PARTIAL+cvssV2_IMPACT_score_8_iot_integrityImpact_PARTIAL)*100)/(cvssV2_IMPACT_score_8_sh+cvssV2_IMPACT_score_8_iot))))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES PARCIAL" )
    print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_8_sh_integrityImpact_NONE+cvssV2_IMPACT_score_8_iot_integrityImpact_NONE)*100)/(cvssV2_IMPACT_score_8_sh+cvssV2_IMPACT_score_8_iot))))+" % DE  VULNERABILIDADES NO EXISTE IMPACTO DE INTEGRIDAD ")
    print("\n")
    print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_8_sh_availabilityImpact_COMPLETE+cvssV2_IMPACT_score_8_iot_availabilityImpact_COMPLETE)*100)/(cvssV2_IMPACT_score_8_sh+cvssV2_IMPACT_score_8_iot))))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES COMPLETO ")
    print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_8_sh_availabilityImpact_PARTIAL+cvssV2_IMPACT_score_8_iot_availabilityImpact_PARTIAL)*100)/(cvssV2_IMPACT_score_8_sh+cvssV2_IMPACT_score_8_iot))))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES PARCIAL" )
    print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_8_sh_availabilityImpact_NONE+cvssV2_IMPACT_score_8_iot_availabilityImpact_NONE)*100)/(cvssV2_IMPACT_score_8_sh+cvssV2_IMPACT_score_8_iot))))+" % DE  VULNERABILIDADES NO EXISTE IMPACTO DE DISPONIBILIDAD ")
    print("\n")
if((cvssV2_IMPACT_score_7_sh+cvssV2_IMPACT_score_7_iot)>0):
    print("      -    EN EL "+str(float((((cvssV2_IMPACT_score_7_sh+cvssV2_IMPACT_score_7_iot)*100)/(len(df_cve_sh["CVE_Items.impact.baseMetricV2.impactScore"])+len(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"])))))+" % DE  VULNERABILIDADES LA PUNTUACION DE IMPACTO ESTÁ ENTRE 7 Y 8. LOS PORCENTAJES DEL VECTOR STRING SON LOS SIGUIENTES:  \n")
    print("\n")
    print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_7_sh_accessvector_NETWORK+cvssV2_IMPACT_score_7_iot_accessvector_NETWORK)*100)/(cvssV2_IMPACT_score_7_sh+cvssV2_IMPACT_score_7_iot))))+" % DE  VULNERABILIDADES EL VECTOR DE ACCESO ES NETWORK ")
    print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_7_sh_accessvector_LOCAL+cvssV2_IMPACT_score_7_iot_accessvector_LOCAL)*100)/(cvssV2_IMPACT_score_7_sh+cvssV2_IMPACT_score_7_iot))))+" % DE  VULNERABILIDADES EL VECTOR DE ACCESO ES LOCAL ")
    print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_7_sh_accessvector_PHYSICAL+cvssV2_IMPACT_score_7_iot_accessvector_PHYSICAL)*100)/(cvssV2_IMPACT_score_7_sh+cvssV2_IMPACT_score_7_iot))))+" % DE  VULNERABILIDADES EL VECTOR DE ACCESO ES PHYSICAL ")
    print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_7_sh_accessvector_ADJACENT_NETWORK+cvssV2_IMPACT_score_7_iot_accessvector_ADJACENT_NETWORK)*100)/(cvssV2_IMPACT_score_7_sh+cvssV2_IMPACT_score_7_iot))))+" % DE  VULNERABILIDADES EL VECTOR DE ACCESO ES ADJACENT_NETWORK ")
    print("\n")
    print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_7_sh_accesscomplexity_HIGH+cvssV2_IMPACT_score_7_iot_accesscomplexity_HIGH)*100)/(cvssV2_IMPACT_score_7_sh+cvssV2_IMPACT_score_7_iot))))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES ALTA ")
    print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_7_sh_accesscomplexity_LOW+cvssV2_IMPACT_score_7_iot_accesscomplexity_LOW)*100)/(cvssV2_IMPACT_score_7_sh+cvssV2_IMPACT_score_7_iot))))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES BAJA ")
    print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_7_sh_accesscomplexity_MEDIUM+cvssV2_IMPACT_score_7_iot_accesscomplexity_MEDIUM)*100)/(cvssV2_IMPACT_score_7_sh+cvssV2_IMPACT_score_7_iot))))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES MEDIA ")
    print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_7_sh_accesscomplexity_NONE+cvssV2_IMPACT_score_7_iot_accesscomplexity_NONE)*100)/(cvssV2_IMPACT_score_7_sh+cvssV2_IMPACT_score_7_iot))))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ACCESO NO VIENE ESPECIFICADA ")
    print("\n")
    print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_1_iot_authentication_SINGLE+cvssV2_IMPACT_score_1_sh_authentication_SINGLE)*100)/(cvssV2_IMPACT_score_7_sh+cvssV2_IMPACT_score_7_iot))))+" % DE  VULNERABILIDADES SE REQUIERE UNA AUTENTICACIÓN SENCILLA ")
    print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_1_iot_authentication_MULTIPLE+cvssV2_IMPACT_score_1_sh_authentication_MULTIPLE)*100)/(cvssV2_IMPACT_score_7_sh+cvssV2_IMPACT_score_7_iot))))+" % DE  VULNERABILIDADES SE REQUIERE UNA AUTENTICACIÓN MÚLTIPLE")
    print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_1_iot_authentication_NONE+cvssV2_IMPACT_score_1_sh_authentication_NONE)*100)/(cvssV2_IMPACT_score_7_sh+cvssV2_IMPACT_score_7_iot))))+" % DE  VULNERABILIDADES NO VIENEN ESPECIFICADAS LA AUTENTICACIÓN REQUERIDA ")
    print("\n")
    print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_7_sh_confidentialityImpact_COMPLETE+cvssV2_IMPACT_score_7_iot_confidentialityImpact_COMPLETE)*100)/(cvssV2_IMPACT_score_7_sh+cvssV2_IMPACT_score_7_iot))))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES COMPLETO ")
    print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_7_sh_confidentialityImpact_PARTIAL+cvssV2_IMPACT_score_7_iot_confidentialityImpact_PARTIAL)*100)/(cvssV2_IMPACT_score_7_sh+cvssV2_IMPACT_score_7_iot))))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES PARCIAL" )
    print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_7_sh_confidentialityImpact_NONE+cvssV2_IMPACT_score_7_iot_confidentialityImpact_NONE)*100)/(cvssV2_IMPACT_score_7_sh+cvssV2_IMPACT_score_7_iot))))+" % DE  VULNERABILIDADES NO EXISTE IMPACTO DE CONFIDENCIALIDAD ")
    print("\n")
    print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_7_sh_integrityImpact_COMPLETE+cvssV2_IMPACT_score_7_iot_integrityImpact_COMPLETE)*100)/(cvssV2_IMPACT_score_7_sh+cvssV2_IMPACT_score_7_iot))))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES COMPLETO ")
    print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_7_sh_integrityImpact_PARTIAL+cvssV2_IMPACT_score_7_iot_integrityImpact_PARTIAL)*100)/(cvssV2_IMPACT_score_7_sh+cvssV2_IMPACT_score_7_iot))))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES PARCIAL" )
    print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_7_sh_integrityImpact_NONE+cvssV2_IMPACT_score_7_iot_integrityImpact_NONE)*100)/(cvssV2_IMPACT_score_7_sh+cvssV2_IMPACT_score_7_iot))))+" % DE  VULNERABILIDADES NO EXISTE IMPACTO DE INTEGRIDAD ")
    print("\n")
    print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_7_sh_availabilityImpact_COMPLETE+cvssV2_IMPACT_score_7_iot_availabilityImpact_COMPLETE)*100)/(cvssV2_IMPACT_score_7_sh+cvssV2_IMPACT_score_7_iot))))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES COMPLETO ")
    print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_7_sh_availabilityImpact_PARTIAL+cvssV2_IMPACT_score_7_iot_availabilityImpact_PARTIAL)*100)/(cvssV2_IMPACT_score_7_sh+cvssV2_IMPACT_score_7_iot))))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES PARCIAL" )
    print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_7_sh_availabilityImpact_NONE+cvssV2_IMPACT_score_7_iot_availabilityImpact_NONE)*100)/(cvssV2_IMPACT_score_7_sh+cvssV2_IMPACT_score_7_iot))))+" % DE  VULNERABILIDADES NO EXISTE IMPACTO DE DISPONIBILIDAD ")      
    print("\n")
if((cvssV2_IMPACT_score_6_sh+cvssV2_IMPACT_score_6_iot)>0):
    print("      -    EN EL "+str(float((((cvssV2_IMPACT_score_6_sh+cvssV2_IMPACT_score_6_iot)*100)/(len(df_cve_sh["CVE_Items.impact.baseMetricV2.impactScore"])+len(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"])))))+" % DE  VULNERABILIDADES LA PUNTUACION DE IMPACTO ESTÁ ENTRE 6 Y 7. LOS PORCENTAJES DEL VECTOR STRING SON LOS SIGUIENTES:  \n")
    print("\n")
    print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_6_sh_accessvector_NETWORK+cvssV2_IMPACT_score_6_iot_accessvector_NETWORK)*100)/(cvssV2_IMPACT_score_6_sh+cvssV2_IMPACT_score_6_iot))))+" % DE  VULNERABILIDADES EL VECTOR DE ACCESO ES NETWORK ")
    print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_6_sh_accessvector_LOCAL+cvssV2_IMPACT_score_6_iot_accessvector_LOCAL)*100)/(cvssV2_IMPACT_score_6_sh+cvssV2_IMPACT_score_6_iot))))+" % DE  VULNERABILIDADES EL VECTOR DE ACCESO ES LOCAL ")
    print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_6_sh_accessvector_PHYSICAL+cvssV2_IMPACT_score_6_iot_accessvector_PHYSICAL)*100)/(cvssV2_IMPACT_score_6_sh+cvssV2_IMPACT_score_6_iot))))+" % DE  VULNERABILIDADES EL VECTOR DE ACCESO ES PHYSICAL ")
    print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_6_sh_accessvector_ADJACENT_NETWORK+cvssV2_IMPACT_score_6_iot_accessvector_ADJACENT_NETWORK)*100)/(cvssV2_IMPACT_score_6_sh+cvssV2_IMPACT_score_6_iot))))+" % DE  VULNERABILIDADES EL VECTOR DE ACCESO ES ADJACENT_NETWORK ")
    print("\n")
    print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_6_sh_accesscomplexity_HIGH+cvssV2_IMPACT_score_6_iot_accesscomplexity_HIGH)*100)/(cvssV2_IMPACT_score_6_sh+cvssV2_IMPACT_score_6_iot))))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES ALTA ")
    print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_6_sh_accesscomplexity_LOW+cvssV2_IMPACT_score_6_iot_accesscomplexity_LOW)*100)/(cvssV2_IMPACT_score_6_sh+cvssV2_IMPACT_score_6_iot))))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES BAJA ")
    print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_6_sh_accesscomplexity_MEDIUM+cvssV2_IMPACT_score_6_iot_accesscomplexity_MEDIUM)*100)/(cvssV2_IMPACT_score_6_sh+cvssV2_IMPACT_score_6_iot))))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES MEDIA ")
    print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_6_sh_accesscomplexity_NONE+cvssV2_IMPACT_score_6_iot_accesscomplexity_NONE)*100)/(cvssV2_IMPACT_score_6_sh+cvssV2_IMPACT_score_6_iot))))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ACCESO NO VIENE ESPECIFICADA ")
    print("\n")
    print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_1_iot_authentication_SINGLE+cvssV2_IMPACT_score_1_sh_authentication_SINGLE)*100)/(cvssV2_IMPACT_score_6_sh+cvssV2_IMPACT_score_6_iot))))+" % DE  VULNERABILIDADES SE REQUIERE UNA AUTENTICACIÓN SENCILLA ")
    print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_1_iot_authentication_MULTIPLE+cvssV2_IMPACT_score_1_sh_authentication_MULTIPLE)*100)/(cvssV2_IMPACT_score_6_sh+cvssV2_IMPACT_score_6_iot))))+" % DE  VULNERABILIDADES SE REQUIERE UNA AUTENTICACIÓN MÚLTIPLE")
    print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_1_iot_authentication_NONE+cvssV2_IMPACT_score_1_sh_authentication_NONE)*100)/(cvssV2_IMPACT_score_6_sh+cvssV2_IMPACT_score_6_iot))))+" % DE  VULNERABILIDADES NO VIENEN ESPECIFICADAS LA AUTENTICACIÓN REQUERIDA ")
    print("\n")
    print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_6_sh_confidentialityImpact_COMPLETE+cvssV2_IMPACT_score_6_iot_confidentialityImpact_COMPLETE)*100)/(cvssV2_IMPACT_score_6_sh+cvssV2_IMPACT_score_6_iot))))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES COMPLETO ")
    print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_6_sh_confidentialityImpact_PARTIAL+cvssV2_IMPACT_score_6_iot_confidentialityImpact_PARTIAL)*100)/(cvssV2_IMPACT_score_6_sh+cvssV2_IMPACT_score_6_iot))))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES PARCIAL" )
    print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_6_sh_confidentialityImpact_NONE+cvssV2_IMPACT_score_6_iot_confidentialityImpact_NONE)*100)/(cvssV2_IMPACT_score_6_sh+cvssV2_IMPACT_score_6_iot))))+" % DE  VULNERABILIDADES NO EXISTE IMPACTO DE CONFIDENCIALIDAD ")
    print("\n")
    print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_6_sh_integrityImpact_COMPLETE+cvssV2_IMPACT_score_6_iot_integrityImpact_COMPLETE)*100)/(cvssV2_IMPACT_score_6_sh+cvssV2_IMPACT_score_6_iot))))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES COMPLETO ")
    print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_6_sh_integrityImpact_PARTIAL+cvssV2_IMPACT_score_6_iot_integrityImpact_PARTIAL)*100)/(cvssV2_IMPACT_score_6_sh+cvssV2_IMPACT_score_6_iot))))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES PARCIAL" )
    print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_6_sh_integrityImpact_NONE+cvssV2_IMPACT_score_6_iot_integrityImpact_NONE)*100)/(cvssV2_IMPACT_score_6_sh+cvssV2_IMPACT_score_6_iot))))+" % DE  VULNERABILIDADES NO EXISTE IMPACTO DE INTEGRIDAD ")
    print("\n")
    print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_6_sh_availabilityImpact_COMPLETE+cvssV2_IMPACT_score_6_iot_availabilityImpact_COMPLETE)*100)/(cvssV2_IMPACT_score_6_sh+cvssV2_IMPACT_score_6_iot))))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES COMPLETO ")
    print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_6_sh_availabilityImpact_PARTIAL+cvssV2_IMPACT_score_6_iot_availabilityImpact_PARTIAL)*100)/(cvssV2_IMPACT_score_6_sh+cvssV2_IMPACT_score_6_iot))))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES PARCIAL" )
    print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_6_sh_availabilityImpact_NONE+cvssV2_IMPACT_score_6_iot_availabilityImpact_NONE)*100)/(cvssV2_IMPACT_score_6_sh+cvssV2_IMPACT_score_6_iot))))+" % DE  VULNERABILIDADES NO EXISTE IMPACTO DE DISPONIBILIDAD ")      
    print("\n")
if((cvssV2_IMPACT_score_5_sh+cvssV2_IMPACT_score_5_iot)>0):
    print("      -    EN EL "+str(float((((cvssV2_IMPACT_score_5_sh+cvssV2_IMPACT_score_5_iot)*100)/(len(df_cve_sh["CVE_Items.impact.baseMetricV2.impactScore"])+len(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"])))))+" % DE  VULNERABILIDADES LA PUNTUACION DE IMPACTO ESTÁ ENTRE 5 Y 6. LOS PORCENTAJES DEL VECTOR STRING SON LOS SIGUIENTES:  \n")
    print("\n")
    print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_5_sh_accessvector_NETWORK+cvssV2_IMPACT_score_5_iot_accessvector_NETWORK)*100)/(cvssV2_IMPACT_score_5_sh+cvssV2_IMPACT_score_5_iot))))+" % DE  VULNERABILIDADES EL VECTOR DE ACCESO ES NETWORK ")
    print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_5_sh_accessvector_LOCAL+cvssV2_IMPACT_score_5_iot_accessvector_LOCAL)*100)/(cvssV2_IMPACT_score_5_sh+cvssV2_IMPACT_score_5_iot))))+" % DE  VULNERABILIDADES EL VECTOR DE ACCESO ES LOCAL ")
    print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_5_sh_accessvector_PHYSICAL+cvssV2_IMPACT_score_5_iot_accessvector_PHYSICAL)*100)/(cvssV2_IMPACT_score_5_sh+cvssV2_IMPACT_score_5_iot))))+" % DE  VULNERABILIDADES EL VECTOR DE ACCESO ES PHYSICAL ")
    print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_5_sh_accessvector_ADJACENT_NETWORK+cvssV2_IMPACT_score_5_iot_accessvector_ADJACENT_NETWORK)*100)/(cvssV2_IMPACT_score_5_sh+cvssV2_IMPACT_score_5_iot))))+" % DE  VULNERABILIDADES EL VECTOR DE ACCESO ES ADJACENT_NETWORK ")
    print("\n")
    print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_5_sh_accesscomplexity_HIGH+cvssV2_IMPACT_score_5_iot_accesscomplexity_HIGH)*100)/(cvssV2_IMPACT_score_5_sh+cvssV2_IMPACT_score_5_iot))))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES ALTA ")
    print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_5_sh_accesscomplexity_LOW+cvssV2_IMPACT_score_5_iot_accesscomplexity_LOW)*100)/(cvssV2_IMPACT_score_5_sh+cvssV2_IMPACT_score_5_iot))))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES BAJA ")
    print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_5_sh_accesscomplexity_MEDIUM+cvssV2_IMPACT_score_5_iot_accesscomplexity_MEDIUM)*100)/(cvssV2_IMPACT_score_5_sh+cvssV2_IMPACT_score_5_iot))))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES MEDIA ")
    print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_5_sh_accesscomplexity_NONE+cvssV2_IMPACT_score_5_iot_accesscomplexity_NONE)*100)/(cvssV2_IMPACT_score_5_sh+cvssV2_IMPACT_score_5_iot))))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ACCESO NO VIENE ESPECIFICADA ")
    print("\n")
    print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_1_iot_authentication_SINGLE+cvssV2_IMPACT_score_1_sh_authentication_SINGLE)*100)/(cvssV2_IMPACT_score_5_sh+cvssV2_IMPACT_score_5_iot))))+" % DE  VULNERABILIDADES SE REQUIERE UNA AUTENTICACIÓN SENCILLA ")
    print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_1_iot_authentication_MULTIPLE+cvssV2_IMPACT_score_1_sh_authentication_MULTIPLE)*100)/(cvssV2_IMPACT_score_5_sh+cvssV2_IMPACT_score_5_iot))))+" % DE  VULNERABILIDADES SE REQUIERE UNA AUTENTICACIÓN MÚLTIPLE")
    print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_1_iot_authentication_NONE+cvssV2_IMPACT_score_1_sh_authentication_NONE)*100)/(cvssV2_IMPACT_score_5_sh+cvssV2_IMPACT_score_5_iot))))+" % DE  VULNERABILIDADES NO VIENEN ESPECIFICADAS LA AUTENTICACIÓN REQUERIDA ")
    print("\n")
    print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_5_sh_confidentialityImpact_COMPLETE+cvssV2_IMPACT_score_5_iot_confidentialityImpact_COMPLETE)*100)/(cvssV2_IMPACT_score_5_sh+cvssV2_IMPACT_score_5_iot))))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES COMPLETO ")
    print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_5_sh_confidentialityImpact_PARTIAL+cvssV2_IMPACT_score_5_iot_confidentialityImpact_PARTIAL)*100)/(cvssV2_IMPACT_score_5_sh+cvssV2_IMPACT_score_5_iot))))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES PARCIAL" )
    print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_5_sh_confidentialityImpact_NONE+cvssV2_IMPACT_score_5_iot_confidentialityImpact_NONE)*100)/(cvssV2_IMPACT_score_5_sh+cvssV2_IMPACT_score_5_iot))))+" % DE  VULNERABILIDADES NO EXISTE IMPACTO DE CONFIDENCIALIDAD ")
    print("\n")
    print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_5_sh_integrityImpact_COMPLETE+cvssV2_IMPACT_score_5_iot_integrityImpact_COMPLETE)*100)/(cvssV2_IMPACT_score_5_sh+cvssV2_IMPACT_score_5_iot))))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES COMPLETO ")
    print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_5_sh_integrityImpact_PARTIAL+cvssV2_IMPACT_score_5_iot_integrityImpact_PARTIAL)*100)/(cvssV2_IMPACT_score_5_sh+cvssV2_IMPACT_score_5_iot))))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES PARCIAL" )
    print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_5_sh_integrityImpact_NONE+cvssV2_IMPACT_score_5_iot_integrityImpact_NONE)*100)/(cvssV2_IMPACT_score_5_sh+cvssV2_IMPACT_score_5_iot))))+" % DE  VULNERABILIDADES NO EXISTE IMPACTO DE INTEGRIDAD ")
    print("\n")
    print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_5_sh_availabilityImpact_COMPLETE+cvssV2_IMPACT_score_5_iot_availabilityImpact_COMPLETE)*100)/(cvssV2_IMPACT_score_5_sh+cvssV2_IMPACT_score_5_iot))))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES COMPLETO ")
    print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_5_sh_availabilityImpact_PARTIAL+cvssV2_IMPACT_score_5_iot_availabilityImpact_PARTIAL)*100)/(cvssV2_IMPACT_score_5_sh+cvssV2_IMPACT_score_5_iot))))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES PARCIAL" )
    print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_5_sh_availabilityImpact_NONE+cvssV2_IMPACT_score_5_iot_availabilityImpact_NONE)*100)/(cvssV2_IMPACT_score_5_sh+cvssV2_IMPACT_score_5_iot))))+" % DE  VULNERABILIDADES NO EXISTE IMPACTO DE DISPONIBILIDAD ")
    print("\n")
if((cvssV2_IMPACT_score_4_sh+cvssV2_IMPACT_score_4_iot)>0):
    print("      -    EN EL "+str(float((((cvssV2_IMPACT_score_4_sh+cvssV2_IMPACT_score_4_iot)*100)/(len(df_cve_sh["CVE_Items.impact.baseMetricV2.impactScore"])+len(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"])))))+" % DE  VULNERABILIDADES LA PUNTUACION DE IMPACTO ESTÁ ENTRE 4 Y 5. LOS PORCENTAJES DEL VECTOR STRING SON LOS SIGUIENTES:  \n")
    print("\n")
    print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_4_sh_accessvector_NETWORK+cvssV2_IMPACT_score_4_iot_accessvector_NETWORK)*100)/(cvssV2_IMPACT_score_4_sh+cvssV2_IMPACT_score_4_iot))))+" % DE  VULNERABILIDADES EL VECTOR DE ACCESO ES NETWORK ")
    print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_4_sh_accessvector_LOCAL+cvssV2_IMPACT_score_4_iot_accessvector_LOCAL)*100)/(cvssV2_IMPACT_score_4_sh+cvssV2_IMPACT_score_4_iot))))+" % DE  VULNERABILIDADES EL VECTOR DE ACCESO ES LOCAL ")
    print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_4_sh_accessvector_PHYSICAL+cvssV2_IMPACT_score_4_iot_accessvector_PHYSICAL)*100)/(cvssV2_IMPACT_score_4_sh+cvssV2_IMPACT_score_4_iot))))+" % DE  VULNERABILIDADES EL VECTOR DE ACCESO ES PHYSICAL ")
    print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_4_sh_accessvector_ADJACENT_NETWORK+cvssV2_IMPACT_score_4_iot_accessvector_ADJACENT_NETWORK)*100)/(cvssV2_IMPACT_score_4_sh+cvssV2_IMPACT_score_4_iot))))+" % DE  VULNERABILIDADES EL VECTOR DE ACCESO ES ADJACENT_NETWORK ")
    print("\n")
    print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_4_sh_accesscomplexity_HIGH+cvssV2_IMPACT_score_4_iot_accesscomplexity_HIGH)*100)/(cvssV2_IMPACT_score_4_sh+cvssV2_IMPACT_score_4_iot))))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES ALTA ")
    print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_4_sh_accesscomplexity_LOW+cvssV2_IMPACT_score_4_iot_accesscomplexity_LOW)*100)/(cvssV2_IMPACT_score_4_sh+cvssV2_IMPACT_score_4_iot))))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES BAJA ")
    print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_4_sh_accesscomplexity_MEDIUM+cvssV2_IMPACT_score_4_iot_accesscomplexity_MEDIUM)*100)/(cvssV2_IMPACT_score_4_sh+cvssV2_IMPACT_score_4_iot))))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES MEDIA ")
    print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_4_sh_accesscomplexity_NONE+cvssV2_IMPACT_score_4_iot_accesscomplexity_NONE)*100)/(cvssV2_IMPACT_score_4_sh+cvssV2_IMPACT_score_4_iot))))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ACCESO NO VIENE ESPECIFICADA ")
    print("\n")
    print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_1_iot_authentication_SINGLE+cvssV2_IMPACT_score_1_sh_authentication_SINGLE)*100)/(cvssV2_IMPACT_score_4_sh+cvssV2_IMPACT_score_4_iot))))+" % DE  VULNERABILIDADES SE REQUIERE UNA AUTENTICACIÓN SENCILLA ")
    print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_1_iot_authentication_MULTIPLE+cvssV2_IMPACT_score_1_sh_authentication_MULTIPLE)*100)/(cvssV2_IMPACT_score_4_sh+cvssV2_IMPACT_score_4_iot))))+" % DE  VULNERABILIDADES SE REQUIERE UNA AUTENTICACIÓN MÚLTIPLE")
    print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_1_iot_authentication_NONE+cvssV2_IMPACT_score_1_sh_authentication_NONE)*100)/(cvssV2_IMPACT_score_4_sh+cvssV2_IMPACT_score_4_iot))))+" % DE  VULNERABILIDADES NO VIENEN ESPECIFICADAS LA AUTENTICACIÓN REQUERIDA ")
    print("\n")
    print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_4_sh_confidentialityImpact_COMPLETE+cvssV2_IMPACT_score_4_iot_confidentialityImpact_COMPLETE)*100)/(cvssV2_IMPACT_score_4_sh+cvssV2_IMPACT_score_4_iot))))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES COMPLETO ")
    print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_4_sh_confidentialityImpact_PARTIAL+cvssV2_IMPACT_score_4_iot_confidentialityImpact_PARTIAL)*100)/(cvssV2_IMPACT_score_4_sh+cvssV2_IMPACT_score_4_iot))))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES PARCIAL" )
    print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_4_sh_confidentialityImpact_NONE+cvssV2_IMPACT_score_4_iot_confidentialityImpact_NONE)*100)/(cvssV2_IMPACT_score_4_sh+cvssV2_IMPACT_score_4_iot))))+" % DE  VULNERABILIDADES NO EXISTE IMPACTO DE CONFIDENCIALIDAD ")
    print("\n")
    print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_4_sh_integrityImpact_COMPLETE+cvssV2_IMPACT_score_4_iot_integrityImpact_COMPLETE)*100)/(cvssV2_IMPACT_score_4_sh+cvssV2_IMPACT_score_4_iot))))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES COMPLETO ")
    print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_4_sh_integrityImpact_PARTIAL+cvssV2_IMPACT_score_4_iot_integrityImpact_PARTIAL)*100)/(cvssV2_IMPACT_score_4_sh+cvssV2_IMPACT_score_4_iot))))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES PARCIAL" )
    print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_4_sh_integrityImpact_NONE+cvssV2_IMPACT_score_4_iot_integrityImpact_NONE)*100)/(cvssV2_IMPACT_score_4_sh+cvssV2_IMPACT_score_4_iot))))+" % DE  VULNERABILIDADES NO EXISTE IMPACTO DE INTEGRIDAD ")
    print("\n")
    print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_4_sh_availabilityImpact_COMPLETE+cvssV2_IMPACT_score_4_iot_availabilityImpact_COMPLETE)*100)/(cvssV2_IMPACT_score_4_sh+cvssV2_IMPACT_score_4_iot))))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES COMPLETO ")
    print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_4_sh_availabilityImpact_PARTIAL+cvssV2_IMPACT_score_4_iot_availabilityImpact_PARTIAL)*100)/(cvssV2_IMPACT_score_4_sh+cvssV2_IMPACT_score_4_iot))))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES PARCIAL" )
    print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_4_sh_availabilityImpact_NONE+cvssV2_IMPACT_score_4_iot_availabilityImpact_NONE)*100)/(cvssV2_IMPACT_score_4_sh+cvssV2_IMPACT_score_4_iot))))+" % DE  VULNERABILIDADES NO EXISTE IMPACTO DE DISPONIBILIDAD ")      
    print("\n")
if((cvssV2_IMPACT_score_3_sh+cvssV2_IMPACT_score_3_iot)>0):
    print("      -    EN EL "+str(float((((cvssV2_IMPACT_score_3_sh+cvssV2_IMPACT_score_3_iot)*100)/(len(df_cve_sh["CVE_Items.impact.baseMetricV2.impactScore"])+len(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"])))))+" % DE  VULNERABILIDADES LA PUNTUACION DE IMPACTO ESTÁ ENTRE 3 Y 4. LOS PORCENTAJES DEL VECTOR STRING SON LOS SIGUIENTES:  \n")
    print("\n")
    print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_3_sh_accessvector_NETWORK+cvssV2_IMPACT_score_3_iot_accessvector_NETWORK)*100)/(cvssV2_IMPACT_score_3_sh+cvssV2_IMPACT_score_3_iot))))+" % DE  VULNERABILIDADES EL VECTOR DE ACCESO ES NETWORK ")
    print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_3_sh_accessvector_LOCAL+cvssV2_IMPACT_score_3_iot_accessvector_LOCAL)*100)/(cvssV2_IMPACT_score_3_sh+cvssV2_IMPACT_score_3_iot))))+" % DE  VULNERABILIDADES EL VECTOR DE ACCESO ES LOCAL ")
    print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_3_sh_accessvector_PHYSICAL+cvssV2_IMPACT_score_3_iot_accessvector_PHYSICAL)*100)/(cvssV2_IMPACT_score_3_sh+cvssV2_IMPACT_score_3_iot))))+" % DE  VULNERABILIDADES EL VECTOR DE ACCESO ES PHYSICAL ")
    print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_3_sh_accessvector_ADJACENT_NETWORK+cvssV2_IMPACT_score_3_iot_accessvector_ADJACENT_NETWORK)*100)/(cvssV2_IMPACT_score_3_sh+cvssV2_IMPACT_score_3_iot))))+" % DE  VULNERABILIDADES EL VECTOR DE ACCESO ES ADJACENT_NETWORK ")
    print("\n")
    print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_3_sh_accesscomplexity_HIGH+cvssV2_IMPACT_score_3_iot_accesscomplexity_HIGH)*100)/(cvssV2_IMPACT_score_3_sh+cvssV2_IMPACT_score_3_iot))))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES ALTA ")
    print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_3_sh_accesscomplexity_LOW+cvssV2_IMPACT_score_3_iot_accesscomplexity_LOW)*100)/(cvssV2_IMPACT_score_3_sh+cvssV2_IMPACT_score_3_iot))))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES BAJA ")
    print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_3_sh_accesscomplexity_MEDIUM+cvssV2_IMPACT_score_3_iot_accesscomplexity_MEDIUM)*100)/(cvssV2_IMPACT_score_3_sh+cvssV2_IMPACT_score_3_iot))))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES MEDIA ")
    print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_3_sh_accesscomplexity_NONE+cvssV2_IMPACT_score_3_iot_accesscomplexity_NONE)*100)/(cvssV2_IMPACT_score_3_sh+cvssV2_IMPACT_score_3_iot))))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ACCESO NO VIENE ESPECIFICADA ")
    print("\n")
    print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_1_iot_authentication_SINGLE+cvssV2_IMPACT_score_1_sh_authentication_SINGLE)*100)/(cvssV2_IMPACT_score_3_sh+cvssV2_IMPACT_score_3_iot))))+" % DE  VULNERABILIDADES SE REQUIERE UNA AUTENTICACIÓN SENCILLA ")
    print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_1_iot_authentication_MULTIPLE+cvssV2_IMPACT_score_1_sh_authentication_MULTIPLE)*100)/(cvssV2_IMPACT_score_3_sh+cvssV2_IMPACT_score_3_iot))))+" % DE  VULNERABILIDADES SE REQUIERE UNA AUTENTICACIÓN MÚLTIPLE")
    print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_1_iot_authentication_NONE+cvssV2_IMPACT_score_1_sh_authentication_NONE)*100)/(cvssV2_IMPACT_score_3_sh+cvssV2_IMPACT_score_3_iot))))+" % DE  VULNERABILIDADES NO VIENEN ESPECIFICADAS LA AUTENTICACIÓN REQUERIDA ")
    print("\n")
    print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_3_sh_confidentialityImpact_COMPLETE+cvssV2_IMPACT_score_3_iot_confidentialityImpact_COMPLETE)*100)/(cvssV2_IMPACT_score_3_sh+cvssV2_IMPACT_score_3_iot))))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES COMPLETO ")
    print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_3_sh_confidentialityImpact_PARTIAL+cvssV2_IMPACT_score_3_iot_confidentialityImpact_PARTIAL)*100)/(cvssV2_IMPACT_score_3_sh+cvssV2_IMPACT_score_3_iot))))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES PARCIAL" )
    print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_3_sh_confidentialityImpact_NONE+cvssV2_IMPACT_score_3_iot_confidentialityImpact_NONE)*100)/(cvssV2_IMPACT_score_3_sh+cvssV2_IMPACT_score_3_iot))))+" % DE  VULNERABILIDADES NO EXISTE IMPACTO DE CONFIDENCIALIDAD ")
    print("\n")
    print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_3_sh_integrityImpact_COMPLETE+cvssV2_IMPACT_score_3_iot_integrityImpact_COMPLETE)*100)/(cvssV2_IMPACT_score_3_sh+cvssV2_IMPACT_score_3_iot))))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES COMPLETO ")
    print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_3_sh_integrityImpact_PARTIAL+cvssV2_IMPACT_score_3_iot_integrityImpact_PARTIAL)*100)/(cvssV2_IMPACT_score_3_sh+cvssV2_IMPACT_score_3_iot))))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES PARCIAL" )
    print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_3_sh_integrityImpact_NONE+cvssV2_IMPACT_score_3_iot_integrityImpact_NONE)*100)/(cvssV2_IMPACT_score_3_sh+cvssV2_IMPACT_score_3_iot))))+" % DE  VULNERABILIDADES NO EXISTE IMPACTO DE INTEGRIDAD ")
    print("\n")
    print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_3_sh_availabilityImpact_COMPLETE+cvssV2_IMPACT_score_3_iot_availabilityImpact_COMPLETE)*100)/(cvssV2_IMPACT_score_3_sh+cvssV2_IMPACT_score_3_iot))))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES COMPLETO ")
    print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_3_sh_availabilityImpact_PARTIAL+cvssV2_IMPACT_score_3_iot_availabilityImpact_PARTIAL)*100)/(cvssV2_IMPACT_score_3_sh+cvssV2_IMPACT_score_3_iot))))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES PARCIAL" )
    print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_3_sh_availabilityImpact_NONE+cvssV2_IMPACT_score_3_iot_availabilityImpact_NONE)*100)/(cvssV2_IMPACT_score_3_sh+cvssV2_IMPACT_score_3_iot))))+" % DE  VULNERABILIDADES NO EXISTE IMPACTO DE DISPONIBILIDAD ")      
    print("\n")
if((cvssV2_IMPACT_score_2_sh+cvssV2_IMPACT_score_2_iot)>0):
	print("      -    EN EL "+str(float((((cvssV2_IMPACT_score_2_sh+cvssV2_IMPACT_score_2_iot)*100)/(len(df_cve_sh["CVE_Items.impact.baseMetricV2.impactScore"])+len(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"])))))+" % DE  VULNERABILIDADES LA PUNTUACION DE IMPACTO ESTÁ ENTRE 2 Y 3. LOS PORCENTAJES DEL VECTOR STRING SON LOS SIGUIENTES:  \n")
	print("\n")
	print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_2_sh_accessvector_NETWORK+cvssV2_IMPACT_score_2_iot_accessvector_NETWORK)*100)/(cvssV2_IMPACT_score_2_sh+cvssV2_IMPACT_score_2_iot))))+" % DE  VULNERABILIDADES EL VECTOR DE ACCESO ES NETWORK ")
	print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_2_sh_accessvector_LOCAL+cvssV2_IMPACT_score_2_iot_accessvector_LOCAL)*100)/(cvssV2_IMPACT_score_2_sh+cvssV2_IMPACT_score_2_iot))))+" % DE  VULNERABILIDADES EL VECTOR DE ACCESO ES LOCAL ")
	print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_2_sh_accessvector_PHYSICAL+cvssV2_IMPACT_score_2_iot_accessvector_PHYSICAL)*100)/(cvssV2_IMPACT_score_2_sh+cvssV2_IMPACT_score_2_iot))))+" % DE  VULNERABILIDADES EL VECTOR DE ACCESO ES PHYSICAL ")
	print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_2_sh_accessvector_ADJACENT_NETWORK+cvssV2_IMPACT_score_2_iot_accessvector_ADJACENT_NETWORK)*100)/(cvssV2_IMPACT_score_2_sh+cvssV2_IMPACT_score_2_iot))))+" % DE  VULNERABILIDADES EL VECTOR DE ACCESO ES ADJACENT_NETWORK ")
	print("\n")
	print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_2_sh_accesscomplexity_HIGH+cvssV2_IMPACT_score_2_iot_accesscomplexity_HIGH)*100)/(cvssV2_IMPACT_score_2_sh+cvssV2_IMPACT_score_2_iot))))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES ALTA ")
	print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_2_sh_accesscomplexity_LOW+cvssV2_IMPACT_score_2_iot_accesscomplexity_LOW)*100)/(cvssV2_IMPACT_score_2_sh+cvssV2_IMPACT_score_2_iot))))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES BAJA ")
	print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_2_sh_accesscomplexity_MEDIUM+cvssV2_IMPACT_score_2_iot_accesscomplexity_MEDIUM)*100)/(cvssV2_IMPACT_score_2_sh+cvssV2_IMPACT_score_2_iot))))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES MEDIA ")
	print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_2_sh_accesscomplexity_NONE+cvssV2_IMPACT_score_2_iot_accesscomplexity_NONE)*100)/(cvssV2_IMPACT_score_2_sh+cvssV2_IMPACT_score_2_iot))))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ACCESO NO VIENE ESPECIFICADA ")
	print("\n")
	print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_1_iot_authentication_SINGLE+cvssV2_IMPACT_score_1_sh_authentication_SINGLE)*100)/(cvssV2_IMPACT_score_2_sh+cvssV2_IMPACT_score_2_iot))))+" % DE  VULNERABILIDADES SE REQUIERE UNA AUTENTICACIÓN SENCILLA ")
	print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_1_iot_authentication_MULTIPLE+cvssV2_IMPACT_score_1_sh_authentication_MULTIPLE)*100)/(cvssV2_IMPACT_score_2_sh+cvssV2_IMPACT_score_2_iot))))+" % DE  VULNERABILIDADES SE REQUIERE UNA AUTENTICACIÓN MÚLTIPLE")
	print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_1_iot_authentication_NONE+cvssV2_IMPACT_score_1_sh_authentication_NONE)*100)/(cvssV2_IMPACT_score_2_sh+cvssV2_IMPACT_score_2_iot))))+" % DE  VULNERABILIDADES NO VIENEN ESPECIFICADAS LA AUTENTICACIÓN REQUERIDA ")
	print("\n")
	print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_2_sh_confidentialityImpact_COMPLETE+cvssV2_IMPACT_score_2_iot_confidentialityImpact_COMPLETE)*100)/(cvssV2_IMPACT_score_2_sh+cvssV2_IMPACT_score_2_iot))))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES COMPLETO ")
	print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_2_sh_confidentialityImpact_PARTIAL+cvssV2_IMPACT_score_2_iot_confidentialityImpact_PARTIAL)*100)/(cvssV2_IMPACT_score_2_sh+cvssV2_IMPACT_score_2_iot))))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES PARCIAL" )
	print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_2_sh_confidentialityImpact_NONE+cvssV2_IMPACT_score_2_iot_confidentialityImpact_NONE)*100)/(cvssV2_IMPACT_score_2_sh+cvssV2_IMPACT_score_2_iot))))+" % DE  VULNERABILIDADES NO EXISTE IMPACTO DE CONFIDENCIALIDAD ")
	print("\n")
	print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_2_sh_integrityImpact_COMPLETE+cvssV2_IMPACT_score_2_iot_integrityImpact_COMPLETE)*100)/(cvssV2_IMPACT_score_2_sh+cvssV2_IMPACT_score_2_iot))))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES COMPLETO ")
	print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_2_sh_integrityImpact_PARTIAL+cvssV2_IMPACT_score_2_iot_integrityImpact_PARTIAL)*100)/(cvssV2_IMPACT_score_2_sh+cvssV2_IMPACT_score_2_iot))))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES PARCIAL" )
	print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_2_sh_integrityImpact_NONE+cvssV2_IMPACT_score_2_iot_integrityImpact_NONE)*100)/(cvssV2_IMPACT_score_2_sh+cvssV2_IMPACT_score_2_iot))))+" % DE  VULNERABILIDADES NO EXISTE IMPACTO DE INTEGRIDAD ")
	print("\n")
	print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_2_sh_availabilityImpact_COMPLETE+cvssV2_IMPACT_score_2_iot_availabilityImpact_COMPLETE)*100)/(cvssV2_IMPACT_score_2_sh+cvssV2_IMPACT_score_2_iot))))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES COMPLETO ")
	print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_2_sh_availabilityImpact_PARTIAL+cvssV2_IMPACT_score_2_iot_availabilityImpact_PARTIAL)*100)/(cvssV2_IMPACT_score_2_sh+cvssV2_IMPACT_score_2_iot))))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES PARCIAL" )
	print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_2_sh_availabilityImpact_NONE+cvssV2_IMPACT_score_2_iot_availabilityImpact_NONE)*100)/(cvssV2_IMPACT_score_2_sh+cvssV2_IMPACT_score_2_iot))))+" % DE  VULNERABILIDADES NO EXISTE IMPACTO DE DISPONIBILIDAD ")      
print("\n")
if((cvssV2_IMPACT_score_1_sh+cvssV2_IMPACT_score_1_iot)>0):
	print("      -    EN EL "+str(float((((cvssV2_IMPACT_score_1_sh+cvssV2_IMPACT_score_1_iot)*100)/(len(df_cve_sh["CVE_Items.impact.baseMetricV2.impactScore"])+len(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"])))))+" % DE  VULNERABILIDADES LA PUNTUACION DE IMPACTO ESTÁ ENTRE 1 y 2. LOS PORCENTAJES DEL VECTOR STRING SON LOS SIGUIENTES:  \n")
	print("\n")
	print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_1_sh_accessvector_NETWORK+cvssV2_IMPACT_score_1_iot_accessvector_NETWORK)*100)/(cvssV2_IMPACT_score_1_sh+cvssV2_IMPACT_score_1_iot))))+" % DE  VULNERABILIDADES EL VECTOR DE ACCESO ES NETWORK ")
	print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_1_sh_accessvector_LOCAL+cvssV2_IMPACT_score_1_iot_accessvector_LOCAL)*100)/(cvssV2_IMPACT_score_1_sh+cvssV2_IMPACT_score_1_iot))))+" % DE  VULNERABILIDADES EL VECTOR DE ACCESO ES LOCAL ")
	print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_1_sh_accessvector_PHYSICAL+cvssV2_IMPACT_score_1_iot_accessvector_PHYSICAL)*100)/(cvssV2_IMPACT_score_1_sh+cvssV2_IMPACT_score_1_iot))))+" % DE  VULNERABILIDADES EL VECTOR DE ACCESO ES PHYSICAL ")
	print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_1_sh_accessvector_ADJACENT_NETWORK+cvssV2_IMPACT_score_1_iot_accessvector_ADJACENT_NETWORK)*100)/(cvssV2_IMPACT_score_1_sh+cvssV2_IMPACT_score_1_iot))))+" % DE  VULNERABILIDADES EL VECTOR DE ACCESO ES ADJACENT_NETWORK ")
	print("\n")
	print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_1_sh_accesscomplexity_HIGH+cvssV2_IMPACT_score_1_iot_accesscomplexity_HIGH)*100)/(cvssV2_IMPACT_score_1_sh+cvssV2_IMPACT_score_1_iot))))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES ALTA ")
	print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_1_sh_accesscomplexity_LOW+cvssV2_IMPACT_score_1_iot_accesscomplexity_LOW)*100)/(cvssV2_IMPACT_score_1_sh+cvssV2_IMPACT_score_1_iot))))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES BAJA ")
	print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_1_sh_accesscomplexity_MEDIUM+cvssV2_IMPACT_score_1_iot_accesscomplexity_MEDIUM)*100)/(cvssV2_IMPACT_score_1_sh+cvssV2_IMPACT_score_1_iot))))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES MEDIA ")
	print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_1_sh_accesscomplexity_NONE+cvssV2_IMPACT_score_1_iot_accesscomplexity_NONE)*100)/(cvssV2_IMPACT_score_1_sh+cvssV2_IMPACT_score_1_iot))))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ACCESO NO VIENE ESPECIFICADA ")
	print("\n")
	print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_1_iot_authentication_SINGLE+cvssV2_IMPACT_score_1_sh_authentication_SINGLE)*100)/(cvssV2_IMPACT_score_1_sh+cvssV2_IMPACT_score_1_iot))))+" % DE  VULNERABILIDADES SE REQUIERE UNA AUTENTICACIÓN SENCILLA ")
	print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_1_iot_authentication_MULTIPLE+cvssV2_IMPACT_score_1_sh_authentication_MULTIPLE)*100)/(cvssV2_IMPACT_score_1_sh+cvssV2_IMPACT_score_1_iot))))+" % DE  VULNERABILIDADES SE REQUIERE UNA AUTENTICACIÓN MÚLTIPLE")
	print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_1_iot_authentication_NONE+cvssV2_IMPACT_score_1_sh_authentication_NONE)*100)/(cvssV2_IMPACT_score_1_sh+cvssV2_IMPACT_score_1_iot))))+" % DE  VULNERABILIDADES NO VIENEN ESPECIFICADAS LA AUTENTICACIÓN REQUERIDA ")
	print("\n")
	print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_1_sh_confidentialityImpact_COMPLETE+cvssV2_IMPACT_score_1_iot_confidentialityImpact_COMPLETE)*100)/(cvssV2_IMPACT_score_1_sh+cvssV2_IMPACT_score_1_iot))))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES COMPLETO ")
	print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_1_sh_confidentialityImpact_PARTIAL+cvssV2_IMPACT_score_1_iot_confidentialityImpact_PARTIAL)*100)/(cvssV2_IMPACT_score_1_sh+cvssV2_IMPACT_score_1_iot))))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES PARCIAL" )
	print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_1_sh_confidentialityImpact_NONE+cvssV2_IMPACT_score_1_iot_confidentialityImpact_NONE)*100)/(cvssV2_IMPACT_score_1_sh+cvssV2_IMPACT_score_1_iot))))+" % DE  VULNERABILIDADES NO EXISTE IMPACTO DE CONFIDENCIALIDAD ")
	print("\n")
	print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_1_sh_integrityImpact_COMPLETE+cvssV2_IMPACT_score_1_iot_integrityImpact_COMPLETE)*100)/(cvssV2_IMPACT_score_1_sh+cvssV2_IMPACT_score_1_iot))))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES COMPLETO ")
	print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_1_sh_integrityImpact_PARTIAL+cvssV2_IMPACT_score_1_iot_integrityImpact_PARTIAL)*100)/(cvssV2_IMPACT_score_1_sh+cvssV2_IMPACT_score_1_iot))))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES PARCIAL" )
	print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_1_sh_integrityImpact_NONE+cvssV2_IMPACT_score_1_iot_integrityImpact_NONE)*100)/(cvssV2_IMPACT_score_1_sh+cvssV2_IMPACT_score_1_iot))))+" % DE  VULNERABILIDADES NO EXISTE IMPACTO DE INTEGRIDAD ")
	print("\n")
	print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_1_sh_availabilityImpact_COMPLETE+cvssV2_IMPACT_score_1_iot_availabilityImpact_COMPLETE)*100)/(cvssV2_IMPACT_score_1_sh+cvssV2_IMPACT_score_1_iot))))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES COMPLETO ")
	print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_1_sh_availabilityImpact_PARTIAL+cvssV2_IMPACT_score_1_iot_availabilityImpact_PARTIAL)*100)/(cvssV2_IMPACT_score_1_sh+cvssV2_IMPACT_score_1_iot))))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES PARCIAL" )
	print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_1_sh_availabilityImpact_NONE+cvssV2_IMPACT_score_1_iot_availabilityImpact_NONE)*100)/(cvssV2_IMPACT_score_1_sh+cvssV2_IMPACT_score_1_iot))))+" % DE  VULNERABILIDADES NO EXISTE IMPACTO DE DISPONIBILIDAD ")      
print("\n")
if((cvssV2_IMPACT_score_0_sh+cvssV2_IMPACT_score_0_iot)>0):
	print("      -    EN EL "+str(float((((cvssV2_IMPACT_score_0_sh+cvssV2_IMPACT_score_0_iot)*100)/(len(df_cve_sh["CVE_Items.impact.baseMetricV2.impactScore"])+len(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"])))))+" % DE  VULNERABILIDADES LA PUNTUACION DE IMPACTO ESTÁ ENTRE 0 y 1. LOS PORCENTAJES DEL VECTOR STRING SON LOS SIGUIENTES:  \n")
	print("\n")
	print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_0_sh_accessvector_NETWORK+cvssV2_IMPACT_score_0_iot_accessvector_NETWORK)*100)/(cvssV2_IMPACT_score_0_sh+cvssV2_IMPACT_score_0_iot))))+" % DE  VULNERABILIDADES EL VECTOR DE ACCESO ES NETWORK ")
	print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_0_sh_accessvector_LOCAL+cvssV2_IMPACT_score_0_iot_accessvector_LOCAL)*100)/(cvssV2_IMPACT_score_0_sh+cvssV2_IMPACT_score_0_iot))))+" % DE  VULNERABILIDADES EL VECTOR DE ACCESO ES LOCAL ")
	print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_0_sh_accessvector_PHYSICAL+cvssV2_IMPACT_score_0_iot_accessvector_PHYSICAL)*100)/(cvssV2_IMPACT_score_0_sh+cvssV2_IMPACT_score_0_iot))))+" % DE  VULNERABILIDADES EL VECTOR DE ACCESO ES PHYSICAL ")
	print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_0_sh_accessvector_ADJACENT_NETWORK+cvssV2_IMPACT_score_0_iot_accessvector_ADJACENT_NETWORK)*100)/(cvssV2_IMPACT_score_0_sh+cvssV2_IMPACT_score_0_iot))))+" % DE  VULNERABILIDADES EL VECTOR DE ACCESO ES ADJACENT_NETWORK ")
	print("\n")
	print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_0_sh_accesscomplexity_HIGH+cvssV2_IMPACT_score_0_iot_accesscomplexity_HIGH)*100)/(cvssV2_IMPACT_score_0_sh+cvssV2_IMPACT_score_0_iot))))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES ALTA ")
	print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_0_sh_accesscomplexity_LOW+cvssV2_IMPACT_score_0_iot_accesscomplexity_LOW)*100)/(cvssV2_IMPACT_score_0_sh+cvssV2_IMPACT_score_0_iot))))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES BAJA ")
	print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_0_sh_accesscomplexity_MEDIUM+cvssV2_IMPACT_score_0_iot_accesscomplexity_MEDIUM)*100)/(cvssV2_IMPACT_score_0_sh+cvssV2_IMPACT_score_0_iot))))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES MEDIA ")
	print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_0_sh_accesscomplexity_NONE+cvssV2_IMPACT_score_0_iot_accesscomplexity_NONE)*100)/(cvssV2_IMPACT_score_0_sh+cvssV2_IMPACT_score_0_iot))))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ACCESO NO VIENE ESPECIFICADA ")
	print("\n")
	print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_0_iot_authentication_SINGLE+cvssV2_IMPACT_score_0_sh_authentication_SINGLE)*100)/(cvssV2_IMPACT_score_0_sh+cvssV2_IMPACT_score_0_iot))))+" % DE  VULNERABILIDADES SE REQUIERE UNA AUTENTICACIÓN SENCILLA ")
	print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_0_iot_authentication_MULTIPLE+cvssV2_IMPACT_score_0_sh_authentication_MULTIPLE)*100)/(cvssV2_IMPACT_score_0_sh+cvssV2_IMPACT_score_0_iot))))+" % DE  VULNERABILIDADES SE REQUIERE UNA AUTENTICACIÓN MÚLTIPLE")
	print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_0_iot_authentication_NONE+cvssV2_IMPACT_score_0_sh_authentication_NONE)*100)/(cvssV2_IMPACT_score_0_sh+cvssV2_IMPACT_score_0_iot))))+" % DE  VULNERABILIDADES NO VIENEN ESPECIFICADAS LA AUTENTICACIÓN REQUERIDA ")
	print("\n")
	print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_0_sh_confidentialityImpact_COMPLETE+cvssV2_IMPACT_score_0_iot_confidentialityImpact_COMPLETE)*100)/(cvssV2_IMPACT_score_0_sh+cvssV2_IMPACT_score_0_iot))))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES COMPLETO ")
	print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_0_sh_confidentialityImpact_PARTIAL+cvssV2_IMPACT_score_0_iot_confidentialityImpact_PARTIAL)*100)/(cvssV2_IMPACT_score_0_sh+cvssV2_IMPACT_score_0_iot))))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES PARCIAL" )
	print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_0_sh_confidentialityImpact_NONE+cvssV2_IMPACT_score_0_iot_confidentialityImpact_NONE)*100)/(cvssV2_IMPACT_score_0_sh+cvssV2_IMPACT_score_0_iot))))+" % DE  VULNERABILIDADES NO EXISTE IMPACTO DE CONFIDENCIALIDAD ")
	print("\n")
	print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_0_sh_integrityImpact_COMPLETE+cvssV2_IMPACT_score_0_iot_integrityImpact_COMPLETE)*100)/(cvssV2_IMPACT_score_0_sh+cvssV2_IMPACT_score_0_iot))))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES COMPLETO ")
	print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_0_sh_integrityImpact_PARTIAL+cvssV2_IMPACT_score_0_iot_integrityImpact_PARTIAL)*100)/(cvssV2_IMPACT_score_0_sh+cvssV2_IMPACT_score_0_iot))))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES PARCIAL" )
	print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_0_sh_integrityImpact_NONE+cvssV2_IMPACT_score_0_iot_integrityImpact_NONE)*100)/(cvssV2_IMPACT_score_0_sh+cvssV2_IMPACT_score_0_iot))))+" % DE  VULNERABILIDADES NO EXISTE IMPACTO DE INTEGRIDAD ")
	print("\n")
	print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_0_sh_availabilityImpact_COMPLETE+cvssV2_IMPACT_score_0_iot_availabilityImpact_COMPLETE)*100)/(cvssV2_IMPACT_score_0_sh+cvssV2_IMPACT_score_0_iot))))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES COMPLETO ")
	print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_0_sh_availabilityImpact_PARTIAL+cvssV2_IMPACT_score_0_iot_availabilityImpact_PARTIAL)*100)/(cvssV2_IMPACT_score_0_sh+cvssV2_IMPACT_score_0_iot))))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES PARCIAL" )
	print("            -    EN EL "+str(float((((cvssV2_IMPACT_score_0_sh_availabilityImpact_NONE+cvssV2_IMPACT_score_0_iot_availabilityImpact_NONE)*100)/(cvssV2_IMPACT_score_0_sh+cvssV2_IMPACT_score_0_iot))))+" % DE  VULNERABILIDADES NO EXISTE IMPACTO DE DISPONIBILIDAD ")      
print("\n")
print("      -    EN EL "+str(float((((cvssV2_no_IMPACT_score_sh+cvssV2_no_IMPACT_score_iot)*100)/(len(df_cve_sh["CVE_Items.impact.baseMetricV2.impactScore"])+len(df_cve_iot["CVE_Items.impact.baseMetricV2.impactScore"])))))+" % DE  VULNERABILIDADES LA PUNTUACION DE IMPACTO NO VIENE ESPECIFICADA. LOS PORCENTAJES DEL VECTOR STRING SON LOS SIGUIENTES:  \n")
print("\n")
print("            -    EN EL "+str(float((((cvssV2_no_IMPACT_score_sh_accessvector_NETWORK+cvssV2_no_IMPACT_score_iot_accessvector_NETWORK)*100)/(cvssV2_no_IMPACT_score_sh+cvssV2_no_IMPACT_score_iot))))+" % DE  VULNERABILIDADES EL VECTOR DE ACCESO ES NETWORK ")
print("            -    EN EL "+str(float((((cvssV2_no_IMPACT_score_sh_accessvector_LOCAL+cvssV2_no_IMPACT_score_iot_accessvector_LOCAL)*100)/(cvssV2_no_IMPACT_score_sh+cvssV2_no_IMPACT_score_iot))))+" % DE  VULNERABILIDADES EL VECTOR DE ACCESO ES LOCAL ")
print("            -    EN EL "+str(float((((cvssV2_no_IMPACT_score_sh_accessvector_PHYSICAL+cvssV2_no_IMPACT_score_iot_accessvector_PHYSICAL)*100)/(cvssV2_no_IMPACT_score_sh+cvssV2_no_IMPACT_score_iot))))+" % DE  VULNERABILIDADES EL VECTOR DE ACCESO ES PHYSICAL ")
print("            -    EN EL "+str(float((((cvssV2_no_IMPACT_score_sh_accessvector_ADJACENT_NETWORK+cvssV2_no_IMPACT_score_iot_accessvector_ADJACENT_NETWORK)*100)/(cvssV2_no_IMPACT_score_sh+cvssV2_no_IMPACT_score_iot))))+" % DE  VULNERABILIDADES EL VECTOR DE ACCESO ES ADJACENT_NETWORK ")
print("\n")
print("            -    EN EL "+str(float((((cvssV2_no_IMPACT_score_sh_accesscomplexity_HIGH+cvssV2_no_IMPACT_score_iot_accesscomplexity_HIGH)*100)/(cvssV2_no_IMPACT_score_sh+cvssV2_no_IMPACT_score_iot))))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES ALTA ")
print("            -    EN EL "+str(float((((cvssV2_no_IMPACT_score_sh_accesscomplexity_LOW+cvssV2_no_IMPACT_score_iot_accesscomplexity_LOW)*100)/(cvssV2_no_IMPACT_score_sh+cvssV2_no_IMPACT_score_iot))))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES BAJA ")
print("            -    EN EL "+str(float((((cvssV2_no_IMPACT_score_sh_accesscomplexity_MEDIUM+cvssV2_no_IMPACT_score_iot_accesscomplexity_MEDIUM)*100)/(cvssV2_no_IMPACT_score_sh+cvssV2_no_IMPACT_score_iot))))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES MEDIA ")
print("            -    EN EL "+str(float((((cvssV2_no_IMPACT_score_sh_accesscomplexity_NONE+cvssV2_no_IMPACT_score_iot_accesscomplexity_NONE)*100)/(cvssV2_no_IMPACT_score_sh+cvssV2_no_IMPACT_score_iot))))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ACCESO NO VIENE ESPECIFICADA ")
print("\n")
print("            -    EN EL "+str(float((((cvssV2_no_IMPACT_score_iot_authentication_SINGLE+cvssV2_no_IMPACT_score_sh_authentication_SINGLE)*100)/(cvssV2_no_IMPACT_score_sh+cvssV2_no_IMPACT_score_iot))))+" % DE  VULNERABILIDADES SE REQUIERE UNA AUTENTICACIÓN SENCILLA ")
print("            -    EN EL "+str(float((((cvssV2_no_IMPACT_score_iot_authentication_MULTIPLE+cvssV2_no_IMPACT_score_sh_authentication_MULTIPLE)*100)/(cvssV2_no_IMPACT_score_sh+cvssV2_no_IMPACT_score_iot))))+" % DE  VULNERABILIDADES SE REQUIERE UNA AUTENTICACIÓN MÚLTIPLE")
print("            -    EN EL "+str(float((((cvssV2_no_IMPACT_score_iot_authentication_NONE+cvssV2_no_IMPACT_score_sh_authentication_NONE)*100)/(cvssV2_no_IMPACT_score_sh+cvssV2_no_IMPACT_score_iot))))+" % DE  VULNERABILIDADES NO VIENEN ESPECIFICADAS LA AUTENTICACIÓN REQUERIDA ")
print("\n")
print("            -    EN EL "+str(float((((cvssV2_no_IMPACT_score_sh_confidentialityImpact_COMPLETE+cvssV2_no_IMPACT_score_iot_confidentialityImpact_COMPLETE)*100)/(cvssV2_no_IMPACT_score_sh+cvssV2_no_IMPACT_score_iot))))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES COMPLETO ")
print("            -    EN EL "+str(float((((cvssV2_no_IMPACT_score_sh_confidentialityImpact_PARTIAL+cvssV2_no_IMPACT_score_iot_confidentialityImpact_PARTIAL)*100)/(cvssV2_no_IMPACT_score_sh+cvssV2_no_IMPACT_score_iot))))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES PARCIAL" )
print("            -    EN EL "+str(float((((cvssV2_no_IMPACT_score_sh_confidentialityImpact_NONE+cvssV2_no_IMPACT_score_iot_confidentialityImpact_NONE)*100)/(cvssV2_no_IMPACT_score_sh+cvssV2_no_IMPACT_score_iot))))+" % DE  VULNERABILIDADES NO EXISTE IMPACTO DE CONFIDENCIALIDAD ")
print("\n")
print("            -    EN EL "+str(float((((cvssV2_no_IMPACT_score_sh_integrityImpact_COMPLETE+cvssV2_no_IMPACT_score_iot_integrityImpact_COMPLETE)*100)/(cvssV2_no_IMPACT_score_sh+cvssV2_no_IMPACT_score_iot))))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES COMPLETO ")
print("            -    EN EL "+str(float((((cvssV2_no_IMPACT_score_sh_integrityImpact_PARTIAL+cvssV2_no_IMPACT_score_iot_integrityImpact_PARTIAL)*100)/(cvssV2_no_IMPACT_score_sh+cvssV2_no_IMPACT_score_iot))))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES PARCIAL" )
print("            -    EN EL "+str(float((((cvssV2_no_IMPACT_score_sh_integrityImpact_NONE+cvssV2_no_IMPACT_score_iot_integrityImpact_NONE)*100)/(cvssV2_no_IMPACT_score_sh+cvssV2_no_IMPACT_score_iot))))+" % DE  VULNERABILIDADES NO EXISTE IMPACTO DE INTEGRIDAD ")
print("\n")
print("            -    EN EL "+str(float((((cvssV2_no_IMPACT_score_sh_availabilityImpact_COMPLETE+cvssV2_no_IMPACT_score_iot_availabilityImpact_COMPLETE)*100)/(cvssV2_no_IMPACT_score_sh+cvssV2_no_IMPACT_score_iot))))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES COMPLETO ")
print("            -    EN EL "+str(float((((cvssV2_no_IMPACT_score_sh_availabilityImpact_PARTIAL+cvssV2_no_IMPACT_score_iot_availabilityImpact_PARTIAL)*100)/(cvssV2_no_IMPACT_score_sh+cvssV2_no_IMPACT_score_iot))))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES PARCIAL" )
print("            -    EN EL "+str(float((((cvssV2_no_IMPACT_score_sh_availabilityImpact_NONE+cvssV2_no_IMPACT_score_iot_availabilityImpact_NONE)*100)/(cvssV2_no_IMPACT_score_sh+cvssV2_no_IMPACT_score_iot))))+" % DE  VULNERABILIDADES NO EXISTE IMPACTO DE DISPONIBILIDAD ")      
print("\n")