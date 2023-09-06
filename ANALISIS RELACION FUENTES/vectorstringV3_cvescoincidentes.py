import pandas as pd


df_cve_iot=pd.read_excel('cves_iot_2023.xlsx')
df_cve_sh=pd.read_excel('cves_smart_home_2023.xlsx')

cves=['CVE-2023-23379','CVE-2022-29859','CVE-2022-34326','CVE-2022-34021','CVE-2021-43702','CVE-2019-12266','CVE-2022-23265','CVE-2021-43573','CVE-2021-1441','CVE-2022-33005','CVE-2023-0847','CVE-2023-23575','CVE-2023-27389','CVE-2023-27917','CVE-2023-25017','CVE-2023-25018','CVE-2022-25075','CVE-2020-8105','CVE-2021-35395','CVE-2021-28372']





##################################Analisis de los elementos de VECTOR CVSSV3 para los CVES coincidentes#########################    
    
#Variables para almacenar distintos elementos del VECTOR CVSSV3 segun la SEVERIDAD BASE
cvssV3_BASE_severity_critical_iot=0

#Variables para almacenar version
cvssV3_BASE_severity_critical_iot_version_3_0=0
cvssV3_BASE_severity_critical_iot_version_3_1=0

#Variables para almacenar vector de ataque
cvssV3_BASE_severity_critical_iot_attackvector_NETWORK=0
cvssV3_BASE_severity_critical_iot_attackvector_PHYSICAL=0
cvssV3_BASE_severity_critical_iot_attackvector_LOCAL=0
cvssV3_BASE_severity_critical_iot_attackvector_ADJACENT_NETWORK=0

#Variables para almacenar complejidad de ataque
cvssV3_BASE_severity_critical_iot_attackcomplexity_HIGH=0
cvssV3_BASE_severity_critical_iot_attackcomplexity_LOW=0
cvssV3_BASE_severity_critical_iot_attackcomplexity_MEDIUM=0
cvssV3_BASE_severity_critical_iot_attackcomplexity_NONE=0

#Variables para almacenar privilegios requeridos
cvssV3_BASE_severity_critical_iot_privilegesrequired_HIGH=0
cvssV3_BASE_severity_critical_iot_privilegesrequired_LOW=0
cvssV3_BASE_severity_critical_iot_privilegesrequired_MEDIUM=0
cvssV3_BASE_severity_critical_iot_privilegesrequired_NONE=0

#Variables para almacenar si se requiere la interaccion del usuario
cvssV3_BASE_severity_critical_iot_userinteraction_REQUIRED=0
cvssV3_BASE_severity_critical_iot_userinteraction_NONEREQUIRED=0

#Variables para almacenar EL ALCANCE
cvssV3_BASE_severity_critical_iot_scope_CHANGED=0
cvssV3_BASE_severity_critical_iot_scope_UNCHANGED=0
cvssV3_BASE_severity_critical_iot_scope_NONE=0

#Variables para almacenar el impacto de confidencialidad
cvssV3_BASE_severity_critical_iot_confidentialityImpact_HIGH=0
cvssV3_BASE_severity_critical_iot_confidentialityImpact_LOW=0
cvssV3_BASE_severity_critical_iot_confidentialityImpact_MEDIUM=0
cvssV3_BASE_severity_critical_iot_confidentialityImpact_NONE=0

#Variables para almacenar el impacto de integridad
cvssV3_BASE_severity_critical_iot_integrityImpact_HIGH=0
cvssV3_BASE_severity_critical_iot_integrityImpact_LOW=0
cvssV3_BASE_severity_critical_iot_integrityImpact_MEDIUM=0
cvssV3_BASE_severity_critical_iot_integrityImpact_NONE=0

#Variables para almacenar el impacto de disponibilidad
cvssV3_BASE_severity_critical_iot_availabilityImpact_HIGH=0
cvssV3_BASE_severity_critical_iot_availabilityImpact_LOW=0
cvssV3_BASE_severity_critical_iot_availabilityImpact_MEDIUM=0
cvssV3_BASE_severity_critical_iot_availabilityImpact_NONE=0
   
    
#Variables para almacenar distintos elementos del VECTOR CVSSV3 segun la SEVERIDAD BASE
cvssV3_BASE_severity_high_iot=0

#Variables para almacenar version
cvssV3_BASE_severity_high_iot_version_3_0=0
cvssV3_BASE_severity_high_iot_version_3_1=0

#Variables para almacenar vector de ataque
cvssV3_BASE_severity_high_iot_attackvector_NETWORK=0
cvssV3_BASE_severity_high_iot_attackvector_PHYSICAL=0
cvssV3_BASE_severity_high_iot_attackvector_LOCAL=0
cvssV3_BASE_severity_high_iot_attackvector_ADJACENT_NETWORK=0

#Variables para almacenar complejidad de ataque
cvssV3_BASE_severity_high_iot_attackcomplexity_HIGH=0
cvssV3_BASE_severity_high_iot_attackcomplexity_LOW=0
cvssV3_BASE_severity_high_iot_attackcomplexity_MEDIUM=0
cvssV3_BASE_severity_high_iot_attackcomplexity_NONE=0

#Variables para almacenar privilegios requeridos
cvssV3_BASE_severity_high_iot_privilegesrequired_HIGH=0
cvssV3_BASE_severity_high_iot_privilegesrequired_LOW=0
cvssV3_BASE_severity_high_iot_privilegesrequired_MEDIUM=0
cvssV3_BASE_severity_high_iot_privilegesrequired_NONE=0

#Variables para almacenar si se requiere la interaccion del usuario
cvssV3_BASE_severity_high_iot_userinteraction_REQUIRED=0
cvssV3_BASE_severity_high_iot_userinteraction_NONEREQUIRED=0

#Variables para almacenar EL ALCANCE
cvssV3_BASE_severity_high_iot_scope_CHANGED=0
cvssV3_BASE_severity_high_iot_scope_UNCHANGED=0
cvssV3_BASE_severity_high_iot_scope_NONE=0

#Variables para almacenar el impacto de confidencialidad
cvssV3_BASE_severity_high_iot_confidentialityImpact_HIGH=0
cvssV3_BASE_severity_high_iot_confidentialityImpact_LOW=0
cvssV3_BASE_severity_high_iot_confidentialityImpact_MEDIUM=0
cvssV3_BASE_severity_high_iot_confidentialityImpact_NONE=0

#Variables para almacenar el impacto de integridad
cvssV3_BASE_severity_high_iot_integrityImpact_HIGH=0
cvssV3_BASE_severity_high_iot_integrityImpact_LOW=0
cvssV3_BASE_severity_high_iot_integrityImpact_MEDIUM=0
cvssV3_BASE_severity_high_iot_integrityImpact_NONE=0

#Variables para almacenar el impacto de disponibilidad
cvssV3_BASE_severity_high_iot_availabilityImpact_HIGH=0
cvssV3_BASE_severity_high_iot_availabilityImpact_LOW=0
cvssV3_BASE_severity_high_iot_availabilityImpact_MEDIUM=0
cvssV3_BASE_severity_high_iot_availabilityImpact_NONE=0




#Variables para almacenar distintos elementos del VECTOR CVSSV3 segun la SEVERIDAD BASE
cvssV3_BASE_severity_medium_iot=0

#Variables para almacenar version
cvssV3_BASE_severity_medium_iot_version_3_0=0
cvssV3_BASE_severity_medium_iot_version_3_1=0

#Variables para almacenar vector de ataque
cvssV3_BASE_severity_medium_iot_attackvector_NETWORK=0
cvssV3_BASE_severity_medium_iot_attackvector_PHYSICAL=0
cvssV3_BASE_severity_medium_iot_attackvector_LOCAL=0
cvssV3_BASE_severity_medium_iot_attackvector_ADJACENT_NETWORK=0

#Variables para almacenar complejidad de ataque
cvssV3_BASE_severity_medium_iot_attackcomplexity_HIGH=0
cvssV3_BASE_severity_medium_iot_attackcomplexity_LOW=0
cvssV3_BASE_severity_medium_iot_attackcomplexity_MEDIUM=0
cvssV3_BASE_severity_medium_iot_attackcomplexity_NONE=0

#Variables para almacenar privilegios requeridos
cvssV3_BASE_severity_medium_iot_privilegesrequired_HIGH=0
cvssV3_BASE_severity_medium_iot_privilegesrequired_LOW=0
cvssV3_BASE_severity_medium_iot_privilegesrequired_MEDIUM=0
cvssV3_BASE_severity_medium_iot_privilegesrequired_NONE=0

#Variables para almacenar si se requiere la interaccion del usuario
cvssV3_BASE_severity_medium_iot_userinteraction_REQUIRED=0
cvssV3_BASE_severity_medium_iot_userinteraction_NONEREQUIRED=0

#Variables para almacenar EL ALCANCE
cvssV3_BASE_severity_medium_iot_scope_CHANGED=0
cvssV3_BASE_severity_medium_iot_scope_UNCHANGED=0
cvssV3_BASE_severity_medium_iot_scope_NONE=0

#Variables para almacenar el impacto de confidencialidad
cvssV3_BASE_severity_medium_iot_confidentialityImpact_HIGH=0
cvssV3_BASE_severity_medium_iot_confidentialityImpact_LOW=0
cvssV3_BASE_severity_medium_iot_confidentialityImpact_MEDIUM=0
cvssV3_BASE_severity_medium_iot_confidentialityImpact_NONE=0

#Variables para almacenar el impacto de integridad
cvssV3_BASE_severity_medium_iot_integrityImpact_HIGH=0
cvssV3_BASE_severity_medium_iot_integrityImpact_LOW=0
cvssV3_BASE_severity_medium_iot_integrityImpact_MEDIUM=0
cvssV3_BASE_severity_medium_iot_integrityImpact_NONE=0

#Variables para almacenar el impacto de disponibilidad
cvssV3_BASE_severity_medium_iot_availabilityImpact_HIGH=0
cvssV3_BASE_severity_medium_iot_availabilityImpact_LOW=0
cvssV3_BASE_severity_medium_iot_availabilityImpact_MEDIUM=0
cvssV3_BASE_severity_medium_iot_availabilityImpact_NONE=0




#Variables para almacenar distintos elementos del VECTOR CVSSV3 segun la SEVERIDAD BASE
cvssV3_BASE_severity_low_iot=0

#Variables para almacenar version
cvssV3_BASE_severity_low_iot_version_3_0=0
cvssV3_BASE_severity_low_iot_version_3_1=0

#Variables para almacenar vector de ataque
cvssV3_BASE_severity_low_iot_attackvector_NETWORK=0
cvssV3_BASE_severity_low_iot_attackvector_PHYSICAL=0
cvssV3_BASE_severity_low_iot_attackvector_LOCAL=0
cvssV3_BASE_severity_low_iot_attackvector_ADJACENT_NETWORK=0

#Variables para almacenar complejidad de ataque
cvssV3_BASE_severity_low_iot_attackcomplexity_HIGH=0
cvssV3_BASE_severity_low_iot_attackcomplexity_LOW=0
cvssV3_BASE_severity_low_iot_attackcomplexity_MEDIUM=0
cvssV3_BASE_severity_low_iot_attackcomplexity_NONE=0

#Variables para almacenar privilegios requeridos
cvssV3_BASE_severity_low_iot_privilegesrequired_HIGH=0
cvssV3_BASE_severity_low_iot_privilegesrequired_LOW=0
cvssV3_BASE_severity_low_iot_privilegesrequired_MEDIUM=0
cvssV3_BASE_severity_low_iot_privilegesrequired_NONE=0

#Variables para almacenar si se requiere la interaccion del usuario
cvssV3_BASE_severity_low_iot_userinteraction_REQUIRED=0
cvssV3_BASE_severity_low_iot_userinteraction_NONEREQUIRED=0

#Variables para almacenar EL ALCANCE
cvssV3_BASE_severity_low_iot_scope_CHANGED=0
cvssV3_BASE_severity_low_iot_scope_UNCHANGED=0
cvssV3_BASE_severity_low_iot_scope_NONE=0

#Variables para almacenar el impacto de confidencialidad
cvssV3_BASE_severity_low_iot_confidentialityImpact_HIGH=0
cvssV3_BASE_severity_low_iot_confidentialityImpact_LOW=0
cvssV3_BASE_severity_low_iot_confidentialityImpact_MEDIUM=0
cvssV3_BASE_severity_low_iot_confidentialityImpact_NONE=0

#Variables para almacenar el impacto de integridad
cvssV3_BASE_severity_low_iot_integrityImpact_HIGH=0
cvssV3_BASE_severity_low_iot_integrityImpact_LOW=0
cvssV3_BASE_severity_low_iot_integrityImpact_MEDIUM=0
cvssV3_BASE_severity_low_iot_integrityImpact_NONE=0

#Variables para almacenar el impacto de disponibilidad
cvssV3_BASE_severity_low_iot_availabilityImpact_HIGH=0
cvssV3_BASE_severity_low_iot_availabilityImpact_LOW=0
cvssV3_BASE_severity_low_iot_availabilityImpact_MEDIUM=0
cvssV3_BASE_severity_low_iot_availabilityImpact_NONE=0



#Buscamos los CVES coincidentes y analizamos los elementos de su VECTOR CVSSV3
for j in range(0,len(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"])):
    if((df_cve_iot["CVE_Items.cve.CVE_data_meta.ID"][j].replace('[','').replace(']','').replace("'","").replace("","").replace(" ","")) in cves):
        if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"][j] != 'NONE'):
            if(((float(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"][j])) <= 10.0) and ((float(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"][j])) >=9.0)):
                cvssV3_BASE_severity_critical_iot+=1
                if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.version"][j] =='3.1'):
                    cvssV3_BASE_severity_critical_iot_version_3_1+=1
                elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.version"][j] =='3.0'):
                    cvssV3_BASE_severity_critical_iot_version_3_0+=1

                if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.attackVector"][j]=='NETWORK'):
                    cvssV3_BASE_severity_critical_iot_attackvector_NETWORK+=1
                elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.attackVector"][j]=='LOCAL'):
                    cvssV3_BASE_severity_critical_iot_attackvector_LOCAL+=1
                elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.attackVector"][j]=='PHYSICAL'):
                    cvssV3_BASE_severity_critical_iot_attackvector_PHYSICAL+=1
                elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.attackVector"][j]=='ADJACENT_NETWORK'):
                    cvssV3_BASE_severity_critical_iot_attackvector_ADJACENT_NETWORK+=1

                if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.attackComplexity"][j]=='HIGH'):
                    cvssV3_BASE_severity_critical_iot_attackcomplexity_HIGH+=1
                elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.attackComplexity"][j]=='LOW'):
                    cvssV3_BASE_severity_critical_iot_attackcomplexity_LOW+=1
                elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.attackComplexity"][j]=='MEDIUM'):
                    cvssV3_BASE_severity_critical_iot_attackcomplexity_MEDIUM+=1
                else:
                    cvssV3_BASE_severity_critical_iot_attackcomplexity_NONE+=1  

                if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.privilegesRequired"][j]=='HIGH'):
                    cvssV3_BASE_severity_critical_iot_privilegesrequired_HIGH+=1
                elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.privilegesRequired"][j]=='LOW'):
                    cvssV3_BASE_severity_critical_iot_privilegesrequired_LOW+=1
                elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.privilegesRequired"][j]=='MEDIUM'):
                    cvssV3_BASE_severity_critical_iot_privilegesrequired_MEDIUM+=1
                else:
                    cvssV3_BASE_severity_critical_iot_privilegesrequired_NONE+=1


                if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.userInteraction"][j]=='REQUIRED'):
                    cvssV3_BASE_severity_critical_iot_userinteraction_REQUIRED+=1
                else:
                    cvssV3_BASE_severity_critical_iot_userinteraction_NONEREQUIRED+=1


                if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.scope"][j] =='CHANGED'):
                    cvssV3_BASE_severity_critical_iot_scope_CHANGED+=1
                elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.scope"][j] =='UNCHANGED'):
                    cvssV3_BASE_severity_critical_iot_scope_UNCHANGED+=1
                else:
                    cvssV3_BASE_severity_critical_iot_scope_NONE+=1


                if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.confidentialityImpact"][j]=='HIGH'):
                    cvssV3_BASE_severity_critical_iot_confidentialityImpact_HIGH+=1
                elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.confidentialityImpact"][j]=='LOW'):
                    cvssV3_BASE_severity_critical_iot_confidentialityImpact_LOW+=1
                elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.confidentialityImpact"][j]=='MEDIUM'):
                    cvssV3_BASE_severity_critical_iot_confidentialityImpact_MEDIUM+=1
                else:
                    cvssV3_BASE_severity_critical_iot_confidentialityImpact_NONE+=1 


                if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"][j]=='HIGH'):
                    cvssV3_BASE_severity_critical_iot_integrityImpact_HIGH+=1
                elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"][j]=='LOW'):
                    cvssV3_BASE_severity_critical_iot_integrityImpact_LOW+=1
                elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"][j]=='MEDIUM'):
                    cvssV3_BASE_severity_critical_iot_integrityImpact_MEDIUM+=1
                else:
                    cvssV3_BASE_severity_critical_iot_integrityImpact_NONE+=1    


                if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"][j]=='HIGH'):
                    cvssV3_BASE_severity_critical_iot_availabilityImpact_HIGH+=1
                elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"][j]=='LOW'):
                    cvssV3_BASE_severity_critical_iot_availabilityImpact_LOW+=1
                elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"][j]=='MEDIUM'):
                    cvssV3_BASE_severity_critical_iot_availabilityImpact_MEDIUM+=1
                else:
                    cvssV3_BASE_severity_critical_iot_availabilityImpact_NONE+=1
                    
            elif(((float(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"][j])) < 9.0) and ((float(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"][j])) >=7.0)):
                cvssV3_BASE_severity_high_iot+=1


                if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.version"][j] =='3.1'):
                    cvssV3_BASE_severity_high_iot_version_3_1+=1
                elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.version"][j] =='3.0'):
                    cvssV3_BASE_severity_high_iot_version_3_0+=1

                if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.attackVector"][j]=='NETWORK'):
                    cvssV3_BASE_severity_high_iot_attackvector_NETWORK+=1
                elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.attackVector"][j]=='LOCAL'):
                    cvssV3_BASE_severity_high_iot_attackvector_LOCAL+=1
                elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.attackVector"][j]=='PHYSICAL'):
                    cvssV3_BASE_severity_high_iot_attackvector_PHYSICAL+=1
                elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.attackVector"][j]=='ADJACENT_NETWORK'):
                    cvssV3_BASE_severity_high_iot_attackvector_ADJACENT_NETWORK+=1

                if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.attackComplexity"][j]=='HIGH'):
                    cvssV3_BASE_severity_high_iot_attackcomplexity_HIGH+=1
                elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.attackComplexity"][j]=='LOW'):
                    cvssV3_BASE_severity_high_iot_attackcomplexity_LOW+=1
                elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.attackComplexity"][j]=='MEDIUM'):
                    cvssV3_BASE_severity_high_iot_attackcomplexity_MEDIUM+=1
                else:
                    cvssV3_BASE_severity_high_iot_attackcomplexity_NONE+=1  

                if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.privilegesRequired"][j]=='HIGH'):
                    cvssV3_BASE_severity_high_iot_privilegesrequired_HIGH+=1
                elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.privilegesRequired"][j]=='LOW'):
                    cvssV3_BASE_severity_high_iot_privilegesrequired_LOW+=1
                elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.privilegesRequired"][j]=='MEDIUM'):
                    cvssV3_BASE_severity_high_iot_privilegesrequired_MEDIUM+=1
                else:
                    cvssV3_BASE_severity_high_iot_privilegesrequired_NONE+=1


                if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.userInteraction"][j]=='REQUIRED'):
                    cvssV3_BASE_severity_high_iot_userinteraction_REQUIRED+=1
                else:
                    cvssV3_BASE_severity_high_iot_userinteraction_NONEREQUIRED+=1


                if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.scope"][j] =='CHANGED'):
                    cvssV3_BASE_severity_high_iot_scope_CHANGED+=1
                elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.scope"][j] =='UNCHANGED'):
                    cvssV3_BASE_severity_high_iot_scope_UNCHANGED+=1
                else:
                    cvssV3_BASE_severity_high_iot_scope_NONE+=1


                if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.confidentialityImpact"][j]=='HIGH'):
                    cvssV3_BASE_severity_high_iot_confidentialityImpact_HIGH+=1
                elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.confidentialityImpact"][j]=='LOW'):
                    cvssV3_BASE_severity_high_iot_confidentialityImpact_LOW+=1
                elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.confidentialityImpact"][j]=='MEDIUM'):
                    cvssV3_BASE_severity_high_iot_confidentialityImpact_MEDIUM+=1
                else:
                    cvssV3_BASE_severity_high_iot_confidentialityImpact_NONE+=1 


                if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"][j]=='HIGH'):
                    cvssV3_BASE_severity_high_iot_integrityImpact_HIGH+=1
                elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"][j]=='LOW'):
                    cvssV3_BASE_severity_high_iot_integrityImpact_LOW+=1
                elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"][j]=='MEDIUM'):
                    cvssV3_BASE_severity_high_iot_integrityImpact_MEDIUM+=1
                else:
                    cvssV3_BASE_severity_high_iot_integrityImpact_NONE+=1    


                if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"][j]=='HIGH'):
                    cvssV3_BASE_severity_high_iot_availabilityImpact_HIGH+=1
                elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"][j]=='LOW'):
                    cvssV3_BASE_severity_high_iot_availabilityImpact_LOW+=1
                elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"][j]=='MEDIUM'):
                    cvssV3_BASE_severity_high_iot_availabilityImpact_MEDIUM+=1
                else:
                    cvssV3_BASE_severity_high_iot_availabilityImpact_NONE+=1

            elif(((float(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"][j])) < 7.0) and ((float(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"][j])) >=4.0)):
                cvssV3_BASE_severity_medium_iot+=1


                if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.version"][j] =='3.1'):
                    cvssV3_BASE_severity_medium_iot_version_3_1+=1
                elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.version"][j] =='3.0'):
                    cvssV3_BASE_severity_medium_iot_version_3_0+=1

                if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.attackVector"][j]=='NETWORK'):
                    cvssV3_BASE_severity_medium_iot_attackvector_NETWORK+=1
                elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.attackVector"][j]=='LOCAL'):
                    cvssV3_BASE_severity_medium_iot_attackvector_LOCAL+=1
                elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.attackVector"][j]=='PHYSICAL'):
                    cvssV3_BASE_severity_medium_iot_attackvector_PHYSICAL+=1
                elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.attackVector"][j]=='ADJACENT_NETWORK'):
                    cvssV3_BASE_severity_medium_iot_attackvector_ADJACENT_NETWORK+=1

                if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.attackComplexity"][j]=='HIGH'):
                    cvssV3_BASE_severity_medium_iot_attackcomplexity_HIGH+=1
                elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.attackComplexity"][j]=='LOW'):
                    cvssV3_BASE_severity_medium_iot_attackcomplexity_LOW+=1
                elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.attackComplexity"][j]=='MEDIUM'):
                    cvssV3_BASE_severity_medium_iot_attackcomplexity_MEDIUM+=1
                else:
                    cvssV3_BASE_severity_medium_iot_attackcomplexity_NONE+=1  

                if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.privilegesRequired"][j]=='HIGH'):
                    cvssV3_BASE_severity_medium_iot_privilegesrequired_HIGH+=1
                elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.privilegesRequired"][j]=='LOW'):
                    cvssV3_BASE_severity_medium_iot_privilegesrequired_LOW+=1
                elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.privilegesRequired"][j]=='MEDIUM'):
                    cvssV3_BASE_severity_medium_iot_privilegesrequired_MEDIUM+=1
                else:
                    cvssV3_BASE_severity_medium_iot_privilegesrequired_NONE+=1


                if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.userInteraction"][j]=='REQUIRED'):
                    cvssV3_BASE_severity_medium_iot_userinteraction_REQUIRED+=1
                else:
                    cvssV3_BASE_severity_medium_iot_userinteraction_NONEREQUIRED+=1


                if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.scope"][j] =='CHANGED'):
                    cvssV3_BASE_severity_medium_iot_scope_CHANGED+=1
                elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.scope"][j] =='UNCHANGED'):
                    cvssV3_BASE_severity_medium_iot_scope_UNCHANGED+=1
                else:
                    cvssV3_BASE_severity_medium_iot_scope_NONE+=1


                if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.confidentialityImpact"][j]=='HIGH'):
                    cvssV3_BASE_severity_medium_iot_confidentialityImpact_HIGH+=1
                elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.confidentialityImpact"][j]=='LOW'):
                    cvssV3_BASE_severity_medium_iot_confidentialityImpact_LOW+=1
                elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.confidentialityImpact"][j]=='MEDIUM'):
                    cvssV3_BASE_severity_medium_iot_confidentialityImpact_MEDIUM+=1
                else:
                    cvssV3_BASE_severity_medium_iot_confidentialityImpact_NONE+=1 


                if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"][j]=='HIGH'):
                    cvssV3_BASE_severity_medium_iot_integrityImpact_HIGH+=1
                elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"][j]=='LOW'):
                    cvssV3_BASE_severity_medium_iot_integrityImpact_LOW+=1
                elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"][j]=='MEDIUM'):
                    cvssV3_BASE_severity_medium_iot_integrityImpact_MEDIUM+=1
                else:
                    cvssV3_BASE_severity_medium_iot_integrityImpact_NONE+=1    


                if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"][j]=='HIGH'):
                    cvssV3_BASE_severity_medium_iot_availabilityImpact_HIGH+=1
                elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"][j]=='LOW'):
                    cvssV3_BASE_severity_medium_iot_availabilityImpact_LOW+=1
                elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"][j]=='MEDIUM'):
                    cvssV3_BASE_severity_medium_iot_availabilityImpact_MEDIUM+=1
                else:
                    cvssV3_BASE_severity_medium_iot_availabilityImpact_NONE+=1

            elif(((float(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"][j])) < 4.0) and ((float(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"][j])) >=0.0)):
                cvssV3_BASE_severity_low_iot+=1


                if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.version"][j] =='3.1'):
                    cvssV3_BASE_severity_low_iot_version_3_1+=1
                elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.version"][j] =='3.0'):
                    cvssV3_BASE_severity_low_iot_version_3_0+=1

                if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.attackVector"][j]=='NETWORK'):
                    cvssV3_BASE_severity_low_iot_attackvector_NETWORK+=1
                elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.attackVector"][j]=='LOCAL'):
                    cvssV3_BASE_severity_low_iot_attackvector_LOCAL+=1
                elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.attackVector"][j]=='PHYSICAL'):
                    cvssV3_BASE_severity_low_iot_attackvector_PHYSICAL+=1
                elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.attackVector"][j]=='ADJACENT_NETWORK'):
                    cvssV3_BASE_severity_low_iot_attackvector_ADJACENT_NETWORK+=1

                if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.attackComplexity"][j]=='HIGH'):
                    cvssV3_BASE_severity_low_iot_attackcomplexity_HIGH+=1
                elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.attackComplexity"][j]=='LOW'):
                    cvssV3_BASE_severity_low_iot_attackcomplexity_LOW+=1
                elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.attackComplexity"][j]=='MEDIUM'):
                    cvssV3_BASE_severity_low_iot_attackcomplexity_MEDIUM+=1
                else:
                    cvssV3_BASE_severity_low_iot_attackcomplexity_NONE+=1  

                if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.privilegesRequired"][j]=='HIGH'):
                    cvssV3_BASE_severity_low_iot_privilegesrequired_HIGH+=1
                elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.privilegesRequired"][j]=='LOW'):
                    cvssV3_BASE_severity_low_iot_privilegesrequired_LOW+=1
                elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.privilegesRequired"][j]=='MEDIUM'):
                    cvssV3_BASE_severity_low_iot_privilegesrequired_MEDIUM+=1
                else:
                    cvssV3_BASE_severity_low_iot_privilegesrequired_NONE+=1


                if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.userInteraction"][j]=='REQUIRED'):
                    cvssV3_BASE_severity_low_iot_userinteraction_REQUIRED+=1
                else:
                    cvssV3_BASE_severity_low_iot_userinteraction_NONEREQUIRED+=1


                if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.scope"][j] =='CHANGED'):
                    cvssV3_BASE_severity_low_iot_scope_CHANGED+=1
                elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.scope"][j] =='UNCHANGED'):
                    cvssV3_BASE_severity_low_iot_scope_UNCHANGED+=1
                else:
                    cvssV3_BASE_severity_low_iot_scope_NONE+=1


                if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.confidentialityImpact"][j]=='HIGH'):
                    cvssV3_BASE_severity_low_iot_confidentialityImpact_HIGH+=1
                elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.confidentialityImpact"][j]=='LOW'):
                    cvssV3_BASE_severity_low_iot_confidentialityImpact_LOW+=1
                elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.confidentialityImpact"][j]=='MEDIUM'):
                    cvssV3_BASE_severity_low_iot_confidentialityImpact_MEDIUM+=1
                else:
                    cvssV3_BASE_severity_low_iot_confidentialityImpact_NONE+=1 


                if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"][j]=='HIGH'):
                    cvssV3_BASE_severity_low_iot_integrityImpact_HIGH+=1
                elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"][j]=='LOW'):
                    cvssV3_BASE_severity_low_iot_integrityImpact_LOW+=1
                elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"][j]=='MEDIUM'):
                    cvssV3_BASE_severity_low_iot_integrityImpact_MEDIUM+=1
                else:
                    cvssV3_BASE_severity_low_iot_integrityImpact_NONE+=1    


                if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"][j]=='HIGH'):
                    cvssV3_BASE_severity_low_iot_availabilityImpact_HIGH+=1
                elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"][j]=='LOW'):
                    cvssV3_BASE_severity_low_iot_availabilityImpact_LOW+=1
                elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"][j]=='MEDIUM'):
                    cvssV3_BASE_severity_low_iot_availabilityImpact_MEDIUM+=1
                else:
                    cvssV3_BASE_severity_low_iot_availabilityImpact_NONE+=1






print("\n")
print("\n")
print("********************ESTADÍSTICAS ELEMENTOS VECTOR CVSSV3 SEGÚN SEVERIDAD BASE********************")
print("\n")        
            
            
    
print("\n")
print(" DE UN TOTAL DE "+str(len(cves))+" VULNERABILIDADES , LAS ESTADISTICAS DE LOS ELEMENTOS DEL VECTOR CVSSV3 SEGUN SEVERIDAD BASE SON LAS SIGUIENTES:  \n")
print("\n")
print("      -    EN  "+str(cvssV3_BASE_severity_critical_iot)+" VULNERABILIDADES LA SEVERIDAD ES CRITICA. LAS ESTADÍSTICAS DEL VECTOR CVSSV3 SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_severity_critical_iot_version_3_1)+" VULNERABILIDADES LA VERSIÓN DEL VECTOR ES LA 3.1 ")
print("            -    EN  "+str(cvssV3_BASE_severity_critical_iot_version_3_0)+" VULNERABILIDADES LA VERSIÓN DEL VECTOR ES LA 3.0 ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_severity_critical_iot_attackvector_NETWORK)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES LA RED ")
print("            -    EN  "+str(cvssV3_BASE_severity_critical_iot_attackvector_LOCAL)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES LOCAL ")
print("            -    EN  "+str(cvssV3_BASE_severity_critical_iot_attackvector_PHYSICAL)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES FÍSICO ")
print("            -    EN  "+str(cvssV3_BASE_severity_critical_iot_attackvector_ADJACENT_NETWORK)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES UNA RED ADYACENTE ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_severity_critical_iot_attackcomplexity_HIGH)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA ")
print("            -    EN  "+str(cvssV3_BASE_severity_critical_iot_attackcomplexity_LOW)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_severity_critical_iot_privilegesrequired_HIGH)+" VULNERABILIDADES SE REQUIEREN PRIVILEGIOS ALTOS ")
print("            -    EN  "+str(cvssV3_BASE_severity_critical_iot_privilegesrequired_LOW)+" VULNERABILIDADES SE REQUIEREN PRIVILEGIOS BAJOS")
print("            -    EN  "+str(cvssV3_BASE_severity_critical_iot_privilegesrequired_NONE)+" VULNERABILIDADES NO VIENEN ESPECIFICADAS SI SE REQUIEREN PRIVILEGIOS")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_severity_critical_iot_userinteraction_REQUIRED)+" VULNERABILIDADES SE REQUIERE INTERACCIÓN DE USUARIO ")
print("            -    EN  "+str(cvssV3_BASE_severity_critical_iot_userinteraction_NONEREQUIRED)+" VULNERABILIDADES NO SE REQUIERE INTERACCIÓN DE USUARIO")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_severity_critical_iot_scope_CHANGED)+" VULNERABILIDADES ES ALCANCE ES CAMBIADO ")
print("            -    EN  "+str(cvssV3_BASE_severity_critical_iot_scope_UNCHANGED)+" VULNERABILIDADES ES ALCANCE NO ES CAMBIADO")
print("            -    EN  "+str(cvssV3_BASE_severity_critical_iot_scope_NONE)+" VULNERABILIDADES EL ALCANCE NO VIENE ESPECIFICADO ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_severity_critical_iot_confidentialityImpact_HIGH)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO ")
print("            -    EN  "+str(cvssV3_BASE_severity_critical_iot_confidentialityImpact_LOW)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO" )
print("            -    EN  "+str(cvssV3_BASE_severity_critical_iot_confidentialityImpact_NONE)+" VULNERABILIDADES NO EXISTE IMPACTO DE CONFIDENCIALIDAD ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_severity_critical_iot_integrityImpact_HIGH)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO ")
print("            -    EN  "+str(cvssV3_BASE_severity_critical_iot_integrityImpact_LOW)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO" )
print("            -    EN  "+str(cvssV3_BASE_severity_critical_iot_integrityImpact_NONE)+" VULNERABILIDADES NO EXISTE IMPACTO DE INTEGRIDAD ")
print("\n")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_severity_critical_iot_availabilityImpact_HIGH)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO ")
print("            -    EN  "+str(cvssV3_BASE_severity_critical_iot_availabilityImpact_LOW)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO" )
print("            -    EN  "+str(cvssV3_BASE_severity_critical_iot_availabilityImpact_NONE)+" VULNERABILIDADES NO EXISTE IMPACTO DE DISPONIBILIDAD ")
print("\n")
print("\n")

print("      -    EN  "+str(cvssV3_BASE_severity_high_iot)+" VULNERABILIDADES LA SEVERIDAD ES ALTA. LAS ESTADÍSTICAS DEL VECTOR CVSSV3 SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_severity_high_iot_version_3_1)+" VULNERABILIDADES LA VERSIÓN DEL VECTOR ES LA 3.1 ")
print("            -    EN  "+str(cvssV3_BASE_severity_high_iot_version_3_0)+" VULNERABILIDADES LA VERSIÓN DEL VECTOR ES LA 3.0 ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_severity_high_iot_attackvector_NETWORK)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES LA RED ")
print("            -    EN  "+str(cvssV3_BASE_severity_high_iot_attackvector_LOCAL)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES LOCAL ")
print("            -    EN  "+str(cvssV3_BASE_severity_high_iot_attackvector_PHYSICAL)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES FÍSICO ")
print("            -    EN  "+str(cvssV3_BASE_severity_high_iot_attackvector_ADJACENT_NETWORK)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES UNA RED ADYACENTE ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_severity_high_iot_attackcomplexity_HIGH)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA ")
print("            -    EN  "+str(cvssV3_BASE_severity_high_iot_attackcomplexity_LOW)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_severity_high_iot_privilegesrequired_HIGH)+" VULNERABILIDADES SE REQUIEREN PRIVILEGIOS ALTOS ")
print("            -    EN  "+str(cvssV3_BASE_severity_high_iot_privilegesrequired_LOW)+" VULNERABILIDADES SE REQUIEREN PRIVILEGIOS BAJOS")
print("            -    EN  "+str(cvssV3_BASE_severity_high_iot_privilegesrequired_NONE)+" VULNERABILIDADES NO VIENEN ESPECIFICADAS SI SE REQUIEREN PRIVILEGIOS")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_severity_high_iot_userinteraction_REQUIRED)+" VULNERABILIDADES SE REQUIERE INTERACCIÓN DE USUARIO ")
print("            -    EN  "+str(cvssV3_BASE_severity_high_iot_userinteraction_NONEREQUIRED)+" VULNERABILIDADES NO SE REQUIERE INTERACCIÓN DE USUARIO")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_severity_high_iot_scope_CHANGED)+" VULNERABILIDADES ES ALCANCE ES CAMBIADO ")
print("            -    EN  "+str(cvssV3_BASE_severity_high_iot_scope_UNCHANGED)+" VULNERABILIDADES ES ALCANCE NO ES CAMBIADO")
print("            -    EN  "+str(cvssV3_BASE_severity_high_iot_scope_NONE)+" VULNERABILIDADES EL ALCANCE NO VIENE ESPECIFICADO ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_severity_high_iot_confidentialityImpact_HIGH)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO ")
print("            -    EN  "+str(cvssV3_BASE_severity_high_iot_confidentialityImpact_LOW)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO" )
print("            -    EN  "+str(cvssV3_BASE_severity_high_iot_confidentialityImpact_NONE)+" VULNERABILIDADES NO EXISTE IMPACTO DE CONFIDENCIALIDAD ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_severity_high_iot_integrityImpact_HIGH)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO ")
print("            -    EN  "+str(cvssV3_BASE_severity_high_iot_integrityImpact_LOW)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO" )
print("            -    EN  "+str(cvssV3_BASE_severity_high_iot_integrityImpact_NONE)+" VULNERABILIDADES NO EXISTE IMPACTO DE INTEGRIDAD ")
print("\n")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_severity_high_iot_availabilityImpact_HIGH)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO ")
print("            -    EN  "+str(cvssV3_BASE_severity_high_iot_availabilityImpact_LOW)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO" )
print("            -    EN  "+str(cvssV3_BASE_severity_high_iot_availabilityImpact_NONE)+" VULNERABILIDADES NO EXISTE IMPACTO DE DISPONIBILIDAD ")
print("\n")
print("\n")

print("      -    EN  "+str(cvssV3_BASE_severity_medium_iot)+" VULNERABILIDADES LA SEVERIDAD ES MEDIA. LAS ESTADÍSTICAS DEL VECTOR CVSSV3 SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_severity_medium_iot_version_3_1)+" VULNERABILIDADES LA VERSIÓN DEL VECTOR ES LA 3.1 ")
print("            -    EN  "+str(cvssV3_BASE_severity_medium_iot_version_3_0)+" VULNERABILIDADES LA VERSIÓN DEL VECTOR ES LA 3.0 ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_severity_medium_iot_attackvector_NETWORK)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES LA RED ")
print("            -    EN  "+str(cvssV3_BASE_severity_medium_iot_attackvector_LOCAL)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES LOCAL ")
print("            -    EN  "+str(cvssV3_BASE_severity_medium_iot_attackvector_PHYSICAL)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES FÍSICO ")
print("            -    EN  "+str(cvssV3_BASE_severity_medium_iot_attackvector_ADJACENT_NETWORK)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES UNA RED ADYACENTE ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_severity_medium_iot_attackcomplexity_HIGH)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA ")
print("            -    EN  "+str(cvssV3_BASE_severity_medium_iot_attackcomplexity_LOW)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_severity_medium_iot_privilegesrequired_HIGH)+" VULNERABILIDADES SE REQUIEREN PRIVILEGIOS ALTOS ")
print("            -    EN  "+str(cvssV3_BASE_severity_medium_iot_privilegesrequired_LOW)+" VULNERABILIDADES SE REQUIEREN PRIVILEGIOS BAJOS")
print("            -    EN  "+str(cvssV3_BASE_severity_medium_iot_privilegesrequired_NONE)+" VULNERABILIDADES NO VIENEN ESPECIFICADAS SI SE REQUIEREN PRIVILEGIOS")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_severity_medium_iot_userinteraction_REQUIRED)+" VULNERABILIDADES SE REQUIERE INTERACCIÓN DE USUARIO ")
print("            -    EN  "+str(cvssV3_BASE_severity_medium_iot_userinteraction_NONEREQUIRED)+" VULNERABILIDADES NO SE REQUIERE INTERACCIÓN DE USUARIO")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_severity_medium_iot_scope_CHANGED)+" VULNERABILIDADES ES ALCANCE ES CAMBIADO ")
print("            -    EN  "+str(cvssV3_BASE_severity_medium_iot_scope_UNCHANGED)+" VULNERABILIDADES ES ALCANCE NO ES CAMBIADO")
print("            -    EN  "+str(cvssV3_BASE_severity_medium_iot_scope_NONE)+" VULNERABILIDADES EL ALCANCE NO VIENE ESPECIFICADO ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_severity_medium_iot_confidentialityImpact_HIGH)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO ")
print("            -    EN  "+str(cvssV3_BASE_severity_medium_iot_confidentialityImpact_LOW)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO" )
print("            -    EN  "+str(cvssV3_BASE_severity_medium_iot_confidentialityImpact_NONE)+" VULNERABILIDADES NO EXISTE IMPACTO DE CONFIDENCIALIDAD ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_severity_medium_iot_integrityImpact_HIGH)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO ")
print("            -    EN  "+str(cvssV3_BASE_severity_medium_iot_integrityImpact_LOW)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO" )
print("            -    EN  "+str(cvssV3_BASE_severity_medium_iot_integrityImpact_NONE)+" VULNERABILIDADES NO EXISTE IMPACTO DE INTEGRIDAD ")
print("\n")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_severity_medium_iot_availabilityImpact_HIGH)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO ")
print("            -    EN  "+str(cvssV3_BASE_severity_medium_iot_availabilityImpact_LOW)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO" )
print("            -    EN  "+str(cvssV3_BASE_severity_medium_iot_availabilityImpact_NONE)+" VULNERABILIDADES NO EXISTE IMPACTO DE DISPONIBILIDAD ")
print("\n")
print("\n")


print("      -    EN  "+str(cvssV3_BASE_severity_low_iot)+" VULNERABILIDADES LA SEVERIDAD ES BAJA. LAS ESTADÍSTICAS DEL VECTOR CVSSV3 SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_severity_low_iot_version_3_1)+" VULNERABILIDADES LA VERSIÓN DEL VECTOR ES LA 3.1 ")
print("            -    EN  "+str(cvssV3_BASE_severity_low_iot_version_3_0)+" VULNERABILIDADES LA VERSIÓN DEL VECTOR ES LA 3.0 ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_severity_low_iot_attackvector_NETWORK)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES LA RED ")
print("            -    EN  "+str(cvssV3_BASE_severity_low_iot_attackvector_LOCAL)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES LOCAL ")
print("            -    EN  "+str(cvssV3_BASE_severity_low_iot_attackvector_PHYSICAL)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES FÍSICO ")
print("            -    EN  "+str(cvssV3_BASE_severity_low_iot_attackvector_ADJACENT_NETWORK)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES UNA RED ADYACENTE ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_severity_low_iot_attackcomplexity_HIGH)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA ")
print("            -    EN  "+str(cvssV3_BASE_severity_low_iot_attackcomplexity_LOW)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_severity_low_iot_privilegesrequired_HIGH)+" VULNERABILIDADES SE REQUIEREN PRIVILEGIOS ALTOS ")
print("            -    EN  "+str(cvssV3_BASE_severity_low_iot_privilegesrequired_LOW)+" VULNERABILIDADES SE REQUIEREN PRIVILEGIOS BAJOS")
print("            -    EN  "+str(cvssV3_BASE_severity_low_iot_privilegesrequired_NONE)+" VULNERABILIDADES NO VIENEN ESPECIFICADAS SI SE REQUIEREN PRIVILEGIOS")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_severity_low_iot_userinteraction_REQUIRED)+" VULNERABILIDADES SE REQUIERE INTERACCIÓN DE USUARIO ")
print("            -    EN  "+str(cvssV3_BASE_severity_low_iot_userinteraction_NONEREQUIRED)+" VULNERABILIDADES NO SE REQUIERE INTERACCIÓN DE USUARIO")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_severity_low_iot_scope_CHANGED)+" VULNERABILIDADES ES ALCANCE ES CAMBIADO ")
print("            -    EN  "+str(cvssV3_BASE_severity_low_iot_scope_UNCHANGED)+" VULNERABILIDADES ES ALCANCE NO ES CAMBIADO")
print("            -    EN  "+str(cvssV3_BASE_severity_low_iot_scope_NONE)+" VULNERABILIDADES EL ALCANCE NO VIENE ESPECIFICADO ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_severity_low_iot_confidentialityImpact_HIGH)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO ")
print("            -    EN  "+str(cvssV3_BASE_severity_low_iot_confidentialityImpact_LOW)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO" )
print("            -    EN  "+str(cvssV3_BASE_severity_low_iot_confidentialityImpact_NONE)+" VULNERABILIDADES NO EXISTE IMPACTO DE CONFIDENCIALIDAD ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_severity_low_iot_integrityImpact_HIGH)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO ")
print("            -    EN  "+str(cvssV3_BASE_severity_low_iot_integrityImpact_LOW)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO" )
print("            -    EN  "+str(cvssV3_BASE_severity_low_iot_integrityImpact_NONE)+" VULNERABILIDADES NO EXISTE IMPACTO DE INTEGRIDAD ")
print("\n")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_severity_low_iot_availabilityImpact_HIGH)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO ")
print("            -    EN  "+str(cvssV3_BASE_severity_low_iot_availabilityImpact_LOW)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO" )

print("            -    EN  "+str(cvssV3_BASE_severity_low_iot_availabilityImpact_NONE)+" VULNERABILIDADES NO EXISTE IMPACTO DE DISPONIBILIDAD ")
print("\n")
print("\n")

print("\n")
print("\n")
print("********************PORCENTAJES ELEMENTOS VECTOR CVSSV3 SEGUN SEVERIDAD BASE********************")
print("\n")        
            
print("\n")
print(" DE UN TOTAL DE "+str(len(cves))+" VULNERABILIDADES ,  LOS PORCENTAJES DE LOS ELEMENTOS DEL VECTOR CVSSV3 SEGUN SEVERIDAD BASE SON LOS SIGUIENTES:   \n")
print("\n")
print("      -    EN EL "+str(float(((cvssV3_BASE_severity_critical_iot*100)/len(cves))))+" % DE  VULNERABILIDADES LA SEVERIDAD ES CRITICA. LOS PORCENTAJES DEL VECTOR CVSSV3 SON LOS SIGUIENTES:  \n")
print("\n")
print("            -    EN EL "+str(float(((cvssV3_BASE_severity_critical_iot_version_3_1*100)/cvssV3_BASE_severity_critical_iot)))+" % DE  VULNERABILIDADES LA VERSIÓN DEL VECTOR ES LA 3.1 ")
print("            -    EN EL "+str(float(((cvssV3_BASE_severity_critical_iot_version_3_0*100)/cvssV3_BASE_severity_critical_iot)))+" % DE  VULNERABILIDADES LA VERSIÓN DEL VECTOR ES LA 3.0 ")
print("\n")
print("            -    EN EL "+str(float(((cvssV3_BASE_severity_critical_iot_attackvector_NETWORK*100)/cvssV3_BASE_severity_critical_iot)))+" % DE  VULNERABILIDADES EL VECTOR DE ATAQUE ES LA RED ")
print("            -    EN EL "+str(float(((cvssV3_BASE_severity_critical_iot_attackvector_LOCAL*100)/cvssV3_BASE_severity_critical_iot)))+" % DE  VULNERABILIDADES EL VECTOR DE ATAQUE ES LOCAL ")
print("            -    EN EL "+str(float(((cvssV3_BASE_severity_critical_iot_attackvector_PHYSICAL*100)/cvssV3_BASE_severity_critical_iot)))+" % DE  VULNERABILIDADES EL VECTOR DE ATAQUE ES FÍSICO ")
print("            -    EN EL "+str(float(((cvssV3_BASE_severity_critical_iot_attackvector_ADJACENT_NETWORK*100)/cvssV3_BASE_severity_critical_iot)))+" % DE  VULNERABILIDADES EL VECTOR DE ATAQUE ES UNA RED ADYACENTE ")
print("\n")
print("            -    EN EL "+str(float(((cvssV3_BASE_severity_critical_iot_attackcomplexity_HIGH*100)/cvssV3_BASE_severity_critical_iot)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA ")
print("            -    EN EL "+str(float(((cvssV3_BASE_severity_critical_iot_attackcomplexity_LOW*100)/cvssV3_BASE_severity_critical_iot)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA ")
print("\n")
print("            -    EN EL "+str(float(((cvssV3_BASE_severity_critical_iot_privilegesrequired_HIGH*100)/cvssV3_BASE_severity_critical_iot)))+" % DE  VULNERABILIDADES SE REQUIEREN PRIVILEGIOS ALTOS ")
print("            -    EN EL "+str(float(((cvssV3_BASE_severity_critical_iot_privilegesrequired_LOW*100)/cvssV3_BASE_severity_critical_iot)))+" % DE  VULNERABILIDADES SE REQUIEREN PRIVILEGIOS BAJOS")
print("            -    EN EL "+str(float(((cvssV3_BASE_severity_critical_iot_privilegesrequired_NONE*100)/cvssV3_BASE_severity_critical_iot)))+" % DE  VULNERABILIDADES NO VIENEN ESPECIFICADAS SI SE REQUIEREN PRIVILEGIOS")
print("\n")
print("            -    EN EL "+str(float(((cvssV3_BASE_severity_critical_iot_userinteraction_REQUIRED*100)/cvssV3_BASE_severity_critical_iot)))+" % DE  VULNERABILIDADES SE REQUIERE INTERACCIÓN DE USUARIO ")
print("            -    EN EL "+str(float(((cvssV3_BASE_severity_critical_iot_userinteraction_NONEREQUIRED*100)/cvssV3_BASE_severity_critical_iot)))+" % DE  VULNERABILIDADES NO SE REQUIERE INTERACCIÓN DE USUARIO")
print("\n")
print("            -    EN EL "+str(float(((cvssV3_BASE_severity_critical_iot_scope_CHANGED*100)/cvssV3_BASE_severity_critical_iot)))+" % DE  VULNERABILIDADES ES ALCANCE ES CAMBIADO ")
print("            -    EN EL "+str(float(((cvssV3_BASE_severity_critical_iot_scope_UNCHANGED*100)/cvssV3_BASE_severity_critical_iot)))+" % DE  VULNERABILIDADES ES ALCANCE NO ES CAMBIADO")
print("            -    EN EL "+str(float(((cvssV3_BASE_severity_critical_iot_scope_NONE*100)/cvssV3_BASE_severity_critical_iot)))+" % DE  VULNERABILIDADES EL ALCANCE NO VIENE ESPECIFICADO ")
print("\n")
print("            -    EN EL "+str(float(((cvssV3_BASE_severity_critical_iot_confidentialityImpact_HIGH*100)/cvssV3_BASE_severity_critical_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO ")
print("            -    EN EL "+str(float(((cvssV3_BASE_severity_critical_iot_confidentialityImpact_LOW*100)/cvssV3_BASE_severity_critical_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO" )
print("            -    EN EL "+str(float(((cvssV3_BASE_severity_critical_iot_confidentialityImpact_NONE*100)/cvssV3_BASE_severity_critical_iot)))+" % DE  VULNERABILIDADES NO EXISTE IMPACTO DE CONFIDENCIALIDAD ")
print("\n")
print("            -    EN EL "+str(float(((cvssV3_BASE_severity_critical_iot_integrityImpact_HIGH*100)/cvssV3_BASE_severity_critical_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO ")
print("            -    EN EL "+str(float(((cvssV3_BASE_severity_critical_iot_integrityImpact_LOW*100)/cvssV3_BASE_severity_critical_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO" )
print("            -    EN EL "+str(float(((cvssV3_BASE_severity_critical_iot_integrityImpact_NONE*100)/cvssV3_BASE_severity_critical_iot)))+" % DE  VULNERABILIDADES NO EXISTE IMPACTO DE INTEGRIDAD ")
print("\n")
print("\n")
print("            -    EN EL "+str(float(((cvssV3_BASE_severity_critical_iot_availabilityImpact_HIGH*100)/cvssV3_BASE_severity_critical_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO ")
print("            -    EN EL "+str(float(((cvssV3_BASE_severity_critical_iot_availabilityImpact_LOW*100)/cvssV3_BASE_severity_critical_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO" )
print("            -    EN EL "+str(float(((cvssV3_BASE_severity_critical_iot_availabilityImpact_NONE*100)/cvssV3_BASE_severity_critical_iot)))+" % DE  VULNERABILIDADES NO EXISTE IMPACTO DE DISPONIBILIDAD ")
print("\n")
print("\n")     

if(cvssV3_BASE_severity_high_iot>0):
    print("      -    EN EL "+str(float(((cvssV3_BASE_severity_high_iot*100)/len(cves))))+" % DE  VULNERABILIDADES LA SEVERIDAD ES ALTA. LOS PORCENTAJES DEL VECTOR CVSSV3 SON LOS SIGUIENTES:  \n")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV3_BASE_severity_high_iot_version_3_1*100)/cvssV3_BASE_severity_high_iot)))+" % DE  VULNERABILIDADES LA VERSIÓN DEL VECTOR ES LA 3.1 ")
    print("            -    EN EL "+str(float(((cvssV3_BASE_severity_high_iot_version_3_0*100)/cvssV3_BASE_severity_high_iot)))+" % DE  VULNERABILIDADES LA VERSIÓN DEL VECTOR ES LA 3.0 ")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV3_BASE_severity_high_iot_attackvector_NETWORK*100)/cvssV3_BASE_severity_high_iot)))+" % DE  VULNERABILIDADES EL VECTOR DE ATAQUE ES LA RED ")
    print("            -    EN EL "+str(float(((cvssV3_BASE_severity_high_iot_attackvector_LOCAL*100)/cvssV3_BASE_severity_high_iot)))+" % DE  VULNERABILIDADES EL VECTOR DE ATAQUE ES LOCAL ")
    print("            -    EN EL "+str(float(((cvssV3_BASE_severity_high_iot_attackvector_PHYSICAL*100)/cvssV3_BASE_severity_high_iot)))+" % DE  VULNERABILIDADES EL VECTOR DE ATAQUE ES FÍSICO ")
    print("            -    EN EL "+str(float(((cvssV3_BASE_severity_high_iot_attackvector_ADJACENT_NETWORK*100)/cvssV3_BASE_severity_high_iot)))+" % DE  VULNERABILIDADES EL VECTOR DE ATAQUE ES UNA RED ADYACENTE ")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV3_BASE_severity_high_iot_attackcomplexity_HIGH*100)/cvssV3_BASE_severity_high_iot)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA ")
    print("            -    EN EL "+str(float(((cvssV3_BASE_severity_high_iot_attackcomplexity_LOW*100)/cvssV3_BASE_severity_high_iot)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA ")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV3_BASE_severity_high_iot_privilegesrequired_HIGH*100)/cvssV3_BASE_severity_high_iot)))+" % DE  VULNERABILIDADES SE REQUIEREN PRIVILEGIOS ALTOS ")
    print("            -    EN EL "+str(float(((cvssV3_BASE_severity_high_iot_privilegesrequired_LOW*100)/cvssV3_BASE_severity_high_iot)))+" % DE  VULNERABILIDADES SE REQUIEREN PRIVILEGIOS BAJOS")
    print("            -    EN EL "+str(float(((cvssV3_BASE_severity_high_iot_privilegesrequired_NONE*100)/cvssV3_BASE_severity_high_iot)))+" % DE  VULNERABILIDADES NO VIENEN ESPECIFICADAS SI SE REQUIEREN PRIVILEGIOS")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV3_BASE_severity_high_iot_userinteraction_REQUIRED*100)/cvssV3_BASE_severity_high_iot)))+" % DE  VULNERABILIDADES SE REQUIERE INTERACCIÓN DE USUARIO ")
    print("            -    EN EL "+str(float(((cvssV3_BASE_severity_high_iot_userinteraction_NONEREQUIRED*100)/cvssV3_BASE_severity_high_iot)))+" % DE  VULNERABILIDADES NO SE REQUIERE INTERACCIÓN DE USUARIO")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV3_BASE_severity_high_iot_scope_CHANGED*100)/cvssV3_BASE_severity_high_iot)))+" % DE  VULNERABILIDADES ES ALCANCE ES CAMBIADO ")
    print("            -    EN EL "+str(float(((cvssV3_BASE_severity_high_iot_scope_UNCHANGED*100)/cvssV3_BASE_severity_high_iot)))+" % DE  VULNERABILIDADES ES ALCANCE NO ES CAMBIADO")
    print("            -    EN EL "+str(float(((cvssV3_BASE_severity_high_iot_scope_NONE*100)/cvssV3_BASE_severity_high_iot)))+" % DE  VULNERABILIDADES EL ALCANCE NO VIENE ESPECIFICADO ")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV3_BASE_severity_high_iot_confidentialityImpact_HIGH*100)/cvssV3_BASE_severity_high_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO ")
    print("            -    EN EL "+str(float(((cvssV3_BASE_severity_high_iot_confidentialityImpact_LOW*100)/cvssV3_BASE_severity_high_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO" )
    print("            -    EN EL "+str(float(((cvssV3_BASE_severity_high_iot_confidentialityImpact_NONE*100)/cvssV3_BASE_severity_high_iot)))+" % DE  VULNERABILIDADES NO EXISTE IMPACTO DE CONFIDENCIALIDAD ")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV3_BASE_severity_high_iot_integrityImpact_HIGH*100)/cvssV3_BASE_severity_high_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO ")
    print("            -    EN EL "+str(float(((cvssV3_BASE_severity_high_iot_integrityImpact_LOW*100)/cvssV3_BASE_severity_high_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO" )
    print("            -    EN EL "+str(float(((cvssV3_BASE_severity_high_iot_integrityImpact_NONE*100)/cvssV3_BASE_severity_high_iot)))+" % DE  VULNERABILIDADES NO EXISTE IMPACTO DE INTEGRIDAD ")
    print("\n")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV3_BASE_severity_high_iot_availabilityImpact_HIGH*100)/cvssV3_BASE_severity_high_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO ")
    print("            -    EN EL "+str(float(((cvssV3_BASE_severity_high_iot_availabilityImpact_LOW*100)/cvssV3_BASE_severity_high_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO" )
    print("            -    EN EL "+str(float(((cvssV3_BASE_severity_high_iot_availabilityImpact_NONE*100)/cvssV3_BASE_severity_high_iot)))+" % DE  VULNERABILIDADES NO EXISTE IMPACTO DE DISPONIBILIDAD ")
    print("\n")
    print("\n")     


if(cvssV3_BASE_severity_medium_iot>0):
    print("      -    EN EL "+str(float(((cvssV3_BASE_severity_medium_iot*100)/len(cves))))+" % DE  VULNERABILIDADES LA SEVERIDAD ES MEDIA. LOS PORCENTAJES DEL VECTOR CVSSV3 SON LOS SIGUIENTES:  \n")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV3_BASE_severity_medium_iot_version_3_1*100)/cvssV3_BASE_severity_medium_iot)))+" % DE  VULNERABILIDADES LA VERSIÓN DEL VECTOR ES LA 3.1 ")
    print("            -    EN EL "+str(float(((cvssV3_BASE_severity_medium_iot_version_3_0*100)/cvssV3_BASE_severity_medium_iot)))+" % DE  VULNERABILIDADES LA VERSIÓN DEL VECTOR ES LA 3.0 ")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV3_BASE_severity_medium_iot_attackvector_NETWORK*100)/cvssV3_BASE_severity_medium_iot)))+" % DE  VULNERABILIDADES EL VECTOR DE ATAQUE ES LA RED ")
    print("            -    EN EL "+str(float(((cvssV3_BASE_severity_medium_iot_attackvector_LOCAL*100)/cvssV3_BASE_severity_medium_iot)))+" % DE  VULNERABILIDADES EL VECTOR DE ATAQUE ES LOCAL ")
    print("            -    EN EL "+str(float(((cvssV3_BASE_severity_medium_iot_attackvector_PHYSICAL*100)/cvssV3_BASE_severity_medium_iot)))+" % DE  VULNERABILIDADES EL VECTOR DE ATAQUE ES FÍSICO ")
    print("            -    EN EL "+str(float(((cvssV3_BASE_severity_medium_iot_attackvector_ADJACENT_NETWORK*100)/cvssV3_BASE_severity_medium_iot)))+" % DE  VULNERABILIDADES EL VECTOR DE ATAQUE ES UNA RED ADYACENTE ")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV3_BASE_severity_medium_iot_attackcomplexity_HIGH*100)/cvssV3_BASE_severity_medium_iot)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA ")
    print("            -    EN EL "+str(float(((cvssV3_BASE_severity_medium_iot_attackcomplexity_LOW*100)/cvssV3_BASE_severity_medium_iot)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA ")

    print("\n")
    print("            -    EN EL "+str(float(((cvssV3_BASE_severity_medium_iot_privilegesrequired_HIGH*100)/cvssV3_BASE_severity_medium_iot)))+" % DE  VULNERABILIDADES SE REQUIEREN PRIVILEGIOS ALTOS ")
    print("            -    EN EL "+str(float(((cvssV3_BASE_severity_medium_iot_privilegesrequired_LOW*100)/cvssV3_BASE_severity_medium_iot)))+" % DE  VULNERABILIDADES SE REQUIEREN PRIVILEGIOS BAJOS")
    print("            -    EN EL "+str(float(((cvssV3_BASE_severity_medium_iot_privilegesrequired_NONE*100)/cvssV3_BASE_severity_medium_iot)))+" % DE  VULNERABILIDADES NO SE REQUIEREN PRIVILEGIOS ")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV3_BASE_severity_medium_iot_userinteraction_REQUIRED*100)/cvssV3_BASE_severity_medium_iot)))+" % DE  VULNERABILIDADES SE REQUIERE INTERACCIÓN DE USUARIO ")
    print("            -    EN EL "+str(float(((cvssV3_BASE_severity_medium_iot_userinteraction_NONEREQUIRED*100)/cvssV3_BASE_severity_medium_iot)))+" % DE VULNERABILIDADES NO SE REQUIERE INTERACCIÓN DE USUARIO")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV3_BASE_severity_medium_iot_scope_CHANGED*100)/cvssV3_BASE_severity_medium_iot)))+" % DE  VULNERABILIDADES ES ALCANCE ES CAMBIADO ")
    print("            -    EN EL "+str(float(((cvssV3_BASE_severity_medium_iot_scope_UNCHANGED*100)/cvssV3_BASE_severity_medium_iot)))+" % DE  VULNERABILIDADES ES ALCANCE ES NO CAMBIADO")
    print("            -    EN EL "+str(float(((cvssV3_BASE_severity_medium_iot_scope_NONE*100)/cvssV3_BASE_severity_medium_iot)))+" % DE  VULNERABILIDADES EL ALCANCE NO VIENE ESPECIFICADO ")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV3_BASE_severity_medium_iot_confidentialityImpact_HIGH*100)/cvssV3_BASE_severity_medium_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO ")
    print("            -    EN EL "+str(float(((cvssV3_BASE_severity_medium_iot_confidentialityImpact_LOW*100)/cvssV3_BASE_severity_medium_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO" )
    print("            -    EN EL "+str(float(((cvssV3_BASE_severity_medium_iot_confidentialityImpact_NONE*100)/cvssV3_BASE_severity_medium_iot)))+" % DE  VULNERABILIDADES NO SE PRODUCE IMPACTO DE CONFIDENCIALIDAD NO VIENE ESPECIFICADO ")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV3_BASE_severity_medium_iot_integrityImpact_HIGH*100)/cvssV3_BASE_severity_medium_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO ")
    print("            -    EN EL "+str(float(((cvssV3_BASE_severity_medium_iot_integrityImpact_LOW*100)/cvssV3_BASE_severity_medium_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO" )
    print("            -    EN EL "+str(float(((cvssV3_BASE_severity_medium_iot_integrityImpact_NONE*100)/cvssV3_BASE_severity_medium_iot)))+" % DE  VULNERABILIDADES NO SE PRODUCE IMPACTO DE INTEGRIDAD NO VIENE ESPECIFICADO ")
    print("\n")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV3_BASE_severity_medium_iot_availabilityImpact_HIGH*100)/cvssV3_BASE_severity_medium_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO ")
    print("            -    EN EL "+str(float(((cvssV3_BASE_severity_medium_iot_availabilityImpact_LOW*100)/cvssV3_BASE_severity_medium_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO" )
    print("            -    EN EL "+str(float(((cvssV3_BASE_severity_medium_iot_availabilityImpact_NONE*100)/cvssV3_BASE_severity_medium_iot)))+" % DE  VULNERABILIDADES NO SE PRODUCE IMPACTO DE DISPONIBILIDAD NO VIENE ESPECIFICADO ")
    print("\n")
    print("\n")     


if(cvssV3_BASE_severity_low_iot>0):
    print("      -    EN EL "+str(float(((cvssV3_BASE_severity_low_iot*100)/len(cves))))+" % DE  VULNERABILIDADES LA SEVERIDAD ES BAJA. LOS PORCENTAJES DEL VECTOR CVSSV3 SON LOS SIGUIENTES:  \n")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV3_BASE_severity_low_iot_version_3_1*100)/cvssV3_BASE_severity_low_iot)))+" % DE  VULNERABILIDADES LA VERSIÓN DEL VECTOR ES LA 3.1 ")
    print("            -    EN EL "+str(float(((cvssV3_BASE_severity_low_iot_version_3_0*100)/cvssV3_BASE_severity_low_iot)))+" % DE  VULNERABILIDADES LA VERSIÓN DEL VECTOR ES LA 3.0 ")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV3_BASE_severity_low_iot_attackvector_NETWORK*100)/cvssV3_BASE_severity_low_iot)))+" % DE  VULNERABILIDADES EL VECTOR DE ATAQUE ES LA RED ")
    print("            -    EN EL "+str(float(((cvssV3_BASE_severity_low_iot_attackvector_LOCAL*100)/cvssV3_BASE_severity_low_iot)))+" % DE  VULNERABILIDADES EL VECTOR DE ATAQUE ES LOCAL ")
    print("            -    EN EL "+str(float(((cvssV3_BASE_severity_low_iot_attackvector_PHYSICAL*100)/cvssV3_BASE_severity_low_iot)))+" % DE  VULNERABILIDADES EL VECTOR DE ATAQUE ES FÍSICO ")
    print("            -    EN EL "+str(float(((cvssV3_BASE_severity_low_iot_attackvector_ADJACENT_NETWORK*100)/cvssV3_BASE_severity_low_iot)))+" % DE  VULNERABILIDADES EL VECTOR DE ATAQUE ES UNA RED ADYACENTE ")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV3_BASE_severity_low_iot_attackcomplexity_HIGH*100)/cvssV3_BASE_severity_low_iot)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA ")
    print("            -    EN EL "+str(float(((cvssV3_BASE_severity_low_iot_attackcomplexity_LOW*100)/cvssV3_BASE_severity_low_iot)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA ")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV3_BASE_severity_low_iot_privilegesrequired_HIGH*100)/cvssV3_BASE_severity_low_iot)))+" % DE  VULNERABILIDADES SE REQUIEREN PRIVILEGIOS ALTOS ")
    print("            -    EN EL "+str(float(((cvssV3_BASE_severity_low_iot_privilegesrequired_LOW*100)/cvssV3_BASE_severity_low_iot)))+" % DE  VULNERABILIDADES SE REQUIEREN PRIVILEGIOS BAJOS")
    print("            -    EN EL "+str(float(((cvssV3_BASE_severity_low_iot_privilegesrequired_NONE*100)/cvssV3_BASE_severity_low_iot)))+" % DE  VULNERABILIDADES NO VIENEN ESPECIFICADAS SI SE REQUIEREN PRIVILEGIOS")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV3_BASE_severity_low_iot_userinteraction_REQUIRED*100)/cvssV3_BASE_severity_low_iot)))+" % DE  VULNERABILIDADES SE REQUIERE INTERACCIÓN DE USUARIO ")
    print("            -    EN EL "+str(float(((cvssV3_BASE_severity_low_iot_userinteraction_NONEREQUIRED*100)/cvssV3_BASE_severity_low_iot)))+" % DE  VULNERABILIDADES NO SE REQUIERE INTERACCIÓN DE USUARIO")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV3_BASE_severity_low_iot_scope_CHANGED*100)/cvssV3_BASE_severity_low_iot)))+" % DE  VULNERABILIDADES ES ALCANCE ES CAMBIADO ")
    print("            -    EN EL "+str(float(((cvssV3_BASE_severity_low_iot_scope_UNCHANGED*100)/cvssV3_BASE_severity_low_iot)))+" % DE  VULNERABILIDADES ES ALCANCE NO ES CAMBIADO")
    print("            -    EN EL "+str(float(((cvssV3_BASE_severity_low_iot_scope_NONE*100)/cvssV3_BASE_severity_low_iot)))+" % DE  VULNERABILIDADES EL ALCANCE NO VIENE ESPECIFICADO ")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV3_BASE_severity_low_iot_confidentialityImpact_HIGH*100)/cvssV3_BASE_severity_low_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO ")
    print("            -    EN EL "+str(float(((cvssV3_BASE_severity_low_iot_confidentialityImpact_LOW*100)/cvssV3_BASE_severity_low_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO" )
    print("            -    EN EL "+str(float(((cvssV3_BASE_severity_low_iot_confidentialityImpact_NONE*100)/cvssV3_BASE_severity_low_iot)))+" % DE  VULNERABILIDADES NO EXISTE IMPACTO DE CONFIDENCIALIDAD ")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV3_BASE_severity_low_iot_integrityImpact_HIGH*100)/cvssV3_BASE_severity_low_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO ")
    print("            -    EN EL "+str(float(((cvssV3_BASE_severity_low_iot_integrityImpact_LOW*100)/cvssV3_BASE_severity_low_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO" )
    print("            -    EN EL "+str(float(((cvssV3_BASE_severity_low_iot_integrityImpact_NONE*100)/cvssV3_BASE_severity_low_iot)))+" % DE  VULNERABILIDADES NO EXISTE IMPACTO DE INTEGRIDAD ")
    print("\n")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV3_BASE_severity_low_iot_availabilityImpact_HIGH*100)/cvssV3_BASE_severity_low_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO ")
    print("            -    EN EL "+str(float(((cvssV3_BASE_severity_low_iot_availabilityImpact_LOW*100)/cvssV3_BASE_severity_low_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO" )
    print("            -    EN EL "+str(float(((cvssV3_BASE_severity_low_iot_availabilityImpact_NONE*100)/cvssV3_BASE_severity_low_iot)))+" % DE  VULNERABILIDADES NO EXISTE IMPACTO DE DISPONIBILIDAD ")
    print("\n")
    print("\n")     



















