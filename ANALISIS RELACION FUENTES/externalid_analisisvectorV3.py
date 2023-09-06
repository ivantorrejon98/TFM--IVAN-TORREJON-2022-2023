import pandas as pd


df_vulnibm_iot=pd.read_excel('vulnerabilidades_ibm_iot_2023.xlsx')


external_references_ids=['CVE-2023-23379','CVE-2023-23575','CVE-2023-27389','CVE-2023-27917','CVE-2023-25017','CVE-2023-25018','CVE-2023-0847','CVE-2022-33005']




##################################Analisis de los elementos de VECTOR CVSSV3 para los IDS DE REFERENCIAS EXTERNAS coincidentes#########################    
    
#Variables para almacenar distintos elementos del VECTOR CVSSV3 segun la SEVERIDAD BASE
cvssV3_BASE_severity_critical_iot=0



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



#Buscamos los IDS DE REFERENCIAS EXTERNAS coincidentes y analizamos los elementos de su VECTOR CVSSV3
for j in range(0,len(df_vulnibm_iot["x_xfe_risk_level"])):
    if((df_vulnibm_iot["external_references_external_id"][j].replace('[','').replace(']','').replace("'","").replace("","").replace(" ",""))  in external_references_ids):
        if(df_vulnibm_iot["x_xfe_risk_level"][j] != 'None'):
            if(((float(df_vulnibm_iot["x_xfe_risk_level"][j])) <= 10.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][j])) >=9.0)):
                cvssV3_BASE_severity_critical_iot+=1

                if(df_vulnibm_iot["x_xfe_cvss_access_vector"][j]=='Network'):
                    cvssV3_BASE_severity_critical_iot_attackvector_NETWORK+=1
                elif(df_vulnibm_iot["x_xfe_cvss_access_vector"][j]=='Local'):
                    cvssV3_BASE_severity_critical_iot_attackvector_LOCAL+=1
                elif(df_vulnibm_iot["x_xfe_cvss_access_vector"][j]=='Physical'):
                    cvssV3_BASE_severity_critical_iot_attackvector_PHYSICAL+=1
                elif(df_vulnibm_iot["x_xfe_cvss_access_vector"][j]=='Adjacent Network'):
                    cvssV3_BASE_severity_critical_iot_attackvector_ADJACENT_NETWORK+=1

                if(df_vulnibm_iot["x_xfe_cvss_access_complexity"][j]=='High'):
                    cvssV3_BASE_severity_critical_iot_attackcomplexity_HIGH+=1
                elif(df_vulnibm_iot["x_xfe_cvss_access_complexity"][j]=='Low'):
                    cvssV3_BASE_severity_critical_iot_attackcomplexity_LOW+=1
                elif(df_vulnibm_iot["x_xfe_cvss_access_complexity"][j]=='Medium'):
                    cvssV3_BASE_severity_critical_iot_attackcomplexity_MEDIUM+=1
                else:
                    cvssV3_BASE_severity_critical_iot_attackcomplexity_NONE+=1  

                if(df_vulnibm_iot["x_xfe_cvss_privilegesrequired"][j]=='High'):
                    cvssV3_BASE_severity_critical_iot_privilegesrequired_HIGH+=1
                elif(df_vulnibm_iot["x_xfe_cvss_privilegesrequired"][j]=='Low'):
                    cvssV3_BASE_severity_critical_iot_privilegesrequired_LOW+=1
                elif(df_vulnibm_iot["x_xfe_cvss_privilegesrequired"][j]=='Medium'):
                    cvssV3_BASE_severity_critical_iot_privilegesrequired_MEDIUM+=1
                else:
                    cvssV3_BASE_severity_critical_iot_privilegesrequired_NONE+=1


                if(df_vulnibm_iot["x_xfe_cvss_userinteraction"][j]=='Required'):
                    cvssV3_BASE_severity_critical_iot_userinteraction_REQUIRED+=1
                else:
                    cvssV3_BASE_severity_critical_iot_userinteraction_NONEREQUIRED+=1


                if(df_vulnibm_iot["x_xfe_cvss_scope"][j] =='Changed'):
                    cvssV3_BASE_severity_critical_iot_scope_CHANGED+=1
                elif(df_vulnibm_iot["x_xfe_cvss_scope"][j] =='Unchanged'):
                    cvssV3_BASE_severity_critical_iot_scope_UNCHANGED+=1
                else:
                    cvssV3_BASE_severity_critical_iot_scope_NONE+=1


                if(df_vulnibm_iot["x_xfe_cvss_confidentiality_impact"][j]=='High'):
                    cvssV3_BASE_severity_critical_iot_confidentialityImpact_HIGH+=1
                elif(df_vulnibm_iot["x_xfe_cvss_confidentiality_impact"][j]=='Low'):
                    cvssV3_BASE_severity_critical_iot_confidentialityImpact_LOW+=1
                elif(df_vulnibm_iot["x_xfe_cvss_confidentiality_impact"][j]=='Medium'):
                    cvssV3_BASE_severity_critical_iot_confidentialityImpact_MEDIUM+=1
                else:
                    cvssV3_BASE_severity_critical_iot_confidentialityImpact_NONE+=1 


                if(df_vulnibm_iot["x_xfe_cvss_integrity_impact"][j]=='High'):
                    cvssV3_BASE_severity_critical_iot_integrityImpact_HIGH+=1
                elif(df_vulnibm_iot["x_xfe_cvss_integrity_impact"][j]=='Low'):
                    cvssV3_BASE_severity_critical_iot_integrityImpact_LOW+=1
                elif(df_vulnibm_iot["x_xfe_cvss_integrity_impact"][j]=='Medium'):
                    cvssV3_BASE_severity_critical_iot_integrityImpact_MEDIUM+=1
                else:
                    cvssV3_BASE_severity_critical_iot_integrityImpact_NONE+=1    


                if(df_vulnibm_iot["x_xfe_cvss_availability_impact"][j]=='High'):
                    cvssV3_BASE_severity_critical_iot_availabilityImpact_HIGH+=1
                elif(df_vulnibm_iot["x_xfe_cvss_availability_impact"][j]=='Low'):
                    cvssV3_BASE_severity_critical_iot_availabilityImpact_LOW+=1
                elif(df_vulnibm_iot["x_xfe_cvss_availability_impact"][j]=='Medium'):
                    cvssV3_BASE_severity_critical_iot_availabilityImpact_MEDIUM+=1
                else:
                    cvssV3_BASE_severity_critical_iot_availabilityImpact_NONE+=1
                    
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][j])) < 9.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][j])) >=7.0)):
                cvssV3_BASE_severity_high_iot+=1


                if(df_vulnibm_iot["x_xfe_cvss_access_vector"][j]=='Network'):
                    cvssV3_BASE_severity_high_iot_attackvector_NETWORK+=1
                elif(df_vulnibm_iot["x_xfe_cvss_access_vector"][j]=='Local'):
                    cvssV3_BASE_severity_high_iot_attackvector_LOCAL+=1
                elif(df_vulnibm_iot["x_xfe_cvss_access_vector"][j]=='Physical'):
                    cvssV3_BASE_severity_high_iot_attackvector_PHYSICAL+=1
                elif(df_vulnibm_iot["x_xfe_cvss_access_vector"][j]=='Adjacent Network'):
                    cvssV3_BASE_severity_high_iot_attackvector_ADJACENT_NETWORK+=1

                if(df_vulnibm_iot["x_xfe_cvss_access_complexity"][j]=='High'):
                    cvssV3_BASE_severity_high_iot_attackcomplexity_HIGH+=1
                elif(df_vulnibm_iot["x_xfe_cvss_access_complexity"][j]=='Low'):
                    cvssV3_BASE_severity_high_iot_attackcomplexity_LOW+=1
                elif(df_vulnibm_iot["x_xfe_cvss_access_complexity"][j]=='Medium'):
                    cvssV3_BASE_severity_high_iot_attackcomplexity_MEDIUM+=1
                else:
                    cvssV3_BASE_severity_high_iot_attackcomplexity_NONE+=1  

                if(df_vulnibm_iot["x_xfe_cvss_privilegesrequired"][j]=='High'):
                    cvssV3_BASE_severity_high_iot_privilegesrequired_HIGH+=1
                elif(df_vulnibm_iot["x_xfe_cvss_privilegesrequired"][j]=='Low'):
                    cvssV3_BASE_severity_high_iot_privilegesrequired_LOW+=1
                elif(df_vulnibm_iot["x_xfe_cvss_privilegesrequired"][j]=='Medium'):
                    cvssV3_BASE_severity_high_iot_privilegesrequired_MEDIUM+=1
                else:
                    cvssV3_BASE_severity_high_iot_privilegesrequired_NONE+=1


                if(df_vulnibm_iot["x_xfe_cvss_userinteraction"][j]=='Required'):
                    cvssV3_BASE_severity_high_iot_userinteraction_REQUIRED+=1
                else:
                    cvssV3_BASE_severity_high_iot_userinteraction_NONEREQUIRED+=1


                if(df_vulnibm_iot["x_xfe_cvss_scope"][j] =='Changed'):
                    cvssV3_BASE_severity_high_iot_scope_CHANGED+=1
                elif(df_vulnibm_iot["x_xfe_cvss_scope"][j] =='Unchanged'):
                    cvssV3_BASE_severity_high_iot_scope_UNCHANGED+=1
                else:
                    cvssV3_BASE_severity_high_iot_scope_NONE+=1


                if(df_vulnibm_iot["x_xfe_cvss_confidentiality_impact"][j]=='High'):
                    cvssV3_BASE_severity_high_iot_confidentialityImpact_HIGH+=1
                elif(df_vulnibm_iot["x_xfe_cvss_confidentiality_impact"][j]=='Low'):
                    cvssV3_BASE_severity_high_iot_confidentialityImpact_LOW+=1
                elif(df_vulnibm_iot["x_xfe_cvss_confidentiality_impact"][j]=='Medium'):
                    cvssV3_BASE_severity_high_iot_confidentialityImpact_MEDIUM+=1
                else:
                    cvssV3_BASE_severity_high_iot_confidentialityImpact_NONE+=1 


                if(df_vulnibm_iot["x_xfe_cvss_integrity_impact"][j]=='High'):
                    cvssV3_BASE_severity_high_iot_integrityImpact_HIGH+=1
                elif(df_vulnibm_iot["x_xfe_cvss_integrity_impact"][j]=='Low'):
                    cvssV3_BASE_severity_high_iot_integrityImpact_LOW+=1
                elif(df_vulnibm_iot["x_xfe_cvss_integrity_impact"][j]=='Medium'):
                    cvssV3_BASE_severity_high_iot_integrityImpact_MEDIUM+=1
                else:
                    cvssV3_BASE_severity_high_iot_integrityImpact_NONE+=1    


                if(df_vulnibm_iot["x_xfe_cvss_availability_impact"][j]=='High'):
                    cvssV3_BASE_severity_high_iot_availabilityImpact_HIGH+=1
                elif(df_vulnibm_iot["x_xfe_cvss_availability_impact"][j]=='Low'):
                    cvssV3_BASE_severity_high_iot_availabilityImpact_LOW+=1
                elif(df_vulnibm_iot["x_xfe_cvss_availability_impact"][j]=='Medium'):
                    cvssV3_BASE_severity_high_iot_availabilityImpact_MEDIUM+=1
                else:
                    cvssV3_BASE_severity_high_iot_availabilityImpact_NONE+=1

            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][j])) < 7.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][j])) >=4.0)):
                cvssV3_BASE_severity_medium_iot+=1


                if(df_vulnibm_iot["x_xfe_cvss_access_vector"][j]=='Network'):
                    cvssV3_BASE_severity_medium_iot_attackvector_NETWORK+=1
                elif(df_vulnibm_iot["x_xfe_cvss_access_vector"][j]=='Local'):
                    cvssV3_BASE_severity_medium_iot_attackvector_LOCAL+=1
                elif(df_vulnibm_iot["x_xfe_cvss_access_vector"][j]=='Physical'):
                    cvssV3_BASE_severity_medium_iot_attackvector_PHYSICAL+=1
                elif(df_vulnibm_iot["x_xfe_cvss_access_vector"][j]=='Adjacent Network'):
                    cvssV3_BASE_severity_medium_iot_attackvector_ADJACENT_NETWORK+=1

                if(df_vulnibm_iot["x_xfe_cvss_access_complexity"][j]=='High'):
                    cvssV3_BASE_severity_medium_iot_attackcomplexity_HIGH+=1
                elif(df_vulnibm_iot["x_xfe_cvss_access_complexity"][j]=='Low'):
                    cvssV3_BASE_severity_medium_iot_attackcomplexity_LOW+=1
                elif(df_vulnibm_iot["x_xfe_cvss_access_complexity"][j]=='Medium'):
                    cvssV3_BASE_severity_medium_iot_attackcomplexity_MEDIUM+=1
                else:
                    cvssV3_BASE_severity_medium_iot_attackcomplexity_NONE+=1  

                if(df_vulnibm_iot["x_xfe_cvss_privilegesrequired"][j]=='High'):
                    cvssV3_BASE_severity_medium_iot_privilegesrequired_HIGH+=1
                elif(df_vulnibm_iot["x_xfe_cvss_privilegesrequired"][j]=='Low'):
                    cvssV3_BASE_severity_medium_iot_privilegesrequired_LOW+=1
                elif(df_vulnibm_iot["x_xfe_cvss_privilegesrequired"][j]=='Medium'):
                    cvssV3_BASE_severity_medium_iot_privilegesrequired_MEDIUM+=1
                else:
                    cvssV3_BASE_severity_medium_iot_privilegesrequired_NONE+=1


                if(df_vulnibm_iot["x_xfe_cvss_userinteraction"][j]=='Required'):
                    cvssV3_BASE_severity_medium_iot_userinteraction_REQUIRED+=1
                else:
                    cvssV3_BASE_severity_medium_iot_userinteraction_NONEREQUIRED+=1


                if(df_vulnibm_iot["x_xfe_cvss_scope"][j] =='Changed'):
                    cvssV3_BASE_severity_medium_iot_scope_CHANGED+=1
                elif(df_vulnibm_iot["x_xfe_cvss_scope"][j] =='Unchanged'):
                    cvssV3_BASE_severity_medium_iot_scope_UNCHANGED+=1
                else:
                    cvssV3_BASE_severity_medium_iot_scope_NONE+=1


                if(df_vulnibm_iot["x_xfe_cvss_confidentiality_impact"][j]=='High'):
                    cvssV3_BASE_severity_medium_iot_confidentialityImpact_HIGH+=1
                elif(df_vulnibm_iot["x_xfe_cvss_confidentiality_impact"][j]=='Low'):
                    cvssV3_BASE_severity_medium_iot_confidentialityImpact_LOW+=1
                elif(df_vulnibm_iot["x_xfe_cvss_confidentiality_impact"][j]=='Medium'):
                    cvssV3_BASE_severity_medium_iot_confidentialityImpact_MEDIUM+=1
                else:
                    cvssV3_BASE_severity_medium_iot_confidentialityImpact_NONE+=1 


                if(df_vulnibm_iot["x_xfe_cvss_integrity_impact"][j]=='High'):
                    cvssV3_BASE_severity_medium_iot_integrityImpact_HIGH+=1
                elif(df_vulnibm_iot["x_xfe_cvss_integrity_impact"][j]=='Low'):
                    cvssV3_BASE_severity_medium_iot_integrityImpact_LOW+=1
                elif(df_vulnibm_iot["x_xfe_cvss_integrity_impact"][j]=='Medium'):
                    cvssV3_BASE_severity_medium_iot_integrityImpact_MEDIUM+=1
                else:
                    cvssV3_BASE_severity_medium_iot_integrityImpact_NONE+=1    


                if(df_vulnibm_iot["x_xfe_cvss_availability_impact"][j]=='High'):
                    cvssV3_BASE_severity_medium_iot_availabilityImpact_HIGH+=1
                elif(df_vulnibm_iot["x_xfe_cvss_availability_impact"][j]=='Low'):
                    cvssV3_BASE_severity_medium_iot_availabilityImpact_LOW+=1
                elif(df_vulnibm_iot["x_xfe_cvss_availability_impact"][j]=='Medium'):
                    cvssV3_BASE_severity_medium_iot_availabilityImpact_MEDIUM+=1
                else:
                    cvssV3_BASE_severity_medium_iot_availabilityImpact_NONE+=1

            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][j])) < 4.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][j])) >=0.0)):
                cvssV3_BASE_severity_low_iot+=1



                if(df_vulnibm_iot["x_xfe_cvss_access_vector"][j]=='Network'):
                    cvssV3_BASE_severity_low_iot_attackvector_NETWORK+=1
                elif(df_vulnibm_iot["x_xfe_cvss_access_vector"][j]=='Local'):
                    cvssV3_BASE_severity_low_iot_attackvector_LOCAL+=1
                elif(df_vulnibm_iot["x_xfe_cvss_access_vector"][j]=='Physical'):
                    cvssV3_BASE_severity_low_iot_attackvector_PHYSICAL+=1
                elif(df_vulnibm_iot["x_xfe_cvss_access_vector"][j]=='Adjacent Network'):
                    cvssV3_BASE_severity_low_iot_attackvector_ADJACENT_NETWORK+=1

                if(df_vulnibm_iot["x_xfe_cvss_access_complexity"][j]=='High'):
                    cvssV3_BASE_severity_low_iot_attackcomplexity_HIGH+=1
                elif(df_vulnibm_iot["x_xfe_cvss_access_complexity"][j]=='Low'):
                    cvssV3_BASE_severity_low_iot_attackcomplexity_LOW+=1
                elif(df_vulnibm_iot["x_xfe_cvss_access_complexity"][j]=='Medium'):
                    cvssV3_BASE_severity_low_iot_attackcomplexity_MEDIUM+=1
                else:
                    cvssV3_BASE_severity_low_iot_attackcomplexity_NONE+=1  

                if(df_vulnibm_iot["x_xfe_cvss_privilegesrequired"][j]=='High'):
                    cvssV3_BASE_severity_low_iot_privilegesrequired_HIGH+=1
                elif(df_vulnibm_iot["x_xfe_cvss_privilegesrequired"][j]=='Low'):
                    cvssV3_BASE_severity_low_iot_privilegesrequired_LOW+=1
                elif(df_vulnibm_iot["x_xfe_cvss_privilegesrequired"][j]=='Medium'):
                    cvssV3_BASE_severity_low_iot_privilegesrequired_MEDIUM+=1
                else:
                    cvssV3_BASE_severity_low_iot_privilegesrequired_NONE+=1


                if(df_vulnibm_iot["x_xfe_cvss_userinteraction"][j]=='Required'):
                    cvssV3_BASE_severity_low_iot_userinteraction_REQUIRED+=1
                else:
                    cvssV3_BASE_severity_low_iot_userinteraction_NONEREQUIRED+=1


                if(df_vulnibm_iot["x_xfe_cvss_scope"][j] =='Changed'):
                    cvssV3_BASE_severity_low_iot_scope_CHANGED+=1
                elif(df_vulnibm_iot["x_xfe_cvss_scope"][j] =='Unchanged'):
                    cvssV3_BASE_severity_low_iot_scope_UNCHANGED+=1
                else:
                    cvssV3_BASE_severity_low_iot_scope_NONE+=1


                if(df_vulnibm_iot["x_xfe_cvss_confidentiality_impact"][j]=='High'):
                    cvssV3_BASE_severity_low_iot_confidentialityImpact_HIGH+=1
                elif(df_vulnibm_iot["x_xfe_cvss_confidentiality_impact"][j]=='Low'):
                    cvssV3_BASE_severity_low_iot_confidentialityImpact_LOW+=1
                elif(df_vulnibm_iot["x_xfe_cvss_confidentiality_impact"][j]=='Medium'):
                    cvssV3_BASE_severity_low_iot_confidentialityImpact_MEDIUM+=1
                else:
                    cvssV3_BASE_severity_low_iot_confidentialityImpact_NONE+=1 


                if(df_vulnibm_iot["x_xfe_cvss_integrity_impact"][j]=='High'):
                    cvssV3_BASE_severity_low_iot_integrityImpact_HIGH+=1
                elif(df_vulnibm_iot["x_xfe_cvss_integrity_impact"][j]=='Low'):
                    cvssV3_BASE_severity_low_iot_integrityImpact_LOW+=1
                elif(df_vulnibm_iot["x_xfe_cvss_integrity_impact"][j]=='Medium'):
                    cvssV3_BASE_severity_low_iot_integrityImpact_MEDIUM+=1
                else:
                    cvssV3_BASE_severity_low_iot_integrityImpact_NONE+=1    


                if(df_vulnibm_iot["x_xfe_cvss_availability_impact"][j]=='High'):
                    cvssV3_BASE_severity_low_iot_availabilityImpact_HIGH+=1
                elif(df_vulnibm_iot["x_xfe_cvss_availability_impact"][j]=='Low'):
                    cvssV3_BASE_severity_low_iot_availabilityImpact_LOW+=1
                elif(df_vulnibm_iot["x_xfe_cvss_availability_impact"][j]=='Medium'):
                    cvssV3_BASE_severity_low_iot_availabilityImpact_MEDIUM+=1
                else:
                    cvssV3_BASE_severity_low_iot_availabilityImpact_NONE+=1






print("\n")
print("\n")
print("********************ESTADÍSTICAS ELEMENTOS VECTOR CVSSV3 SEGÚN SEVERIDAD BASE********************")
print("\n")        
            
            
    
print("\n")
print(" DE UN TOTAL DE "+str(len(external_references_ids))+" VULNERABILIDADES , LAS ESTADISTICAS DE LOS ELEMENTOS DEL VECTOR CVSSV3 SEGUN SEVERIDAD SON LAS SIGUIENTES:  \n")
print("\n")
print("      -    EN  "+str(cvssV3_BASE_severity_critical_iot)+" VULNERABILIDADES LA SEVERIDAD ES CRITICA. LAS ESTADÍSTICAS DEL VECTOR CVSSV3 SON LAS SIGUIENTES:  \n")
print("\n")
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
print("            -    EN  "+str(cvssV3_BASE_severity_critical_iot_privilegesrequired_NONE)+" VULNERABILIDADES NO SE REQUIEREN PRIVILEGIOS")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_severity_critical_iot_userinteraction_REQUIRED)+" VULNERABILIDADES SE REQUIERE INTERACCIÓN DE USUARIO ")
print("            -    EN  "+str(cvssV3_BASE_severity_critical_iot_userinteraction_NONEREQUIRED)+" VULNERABILIDADES NO SE REQUIERE INTERACCIÓN DE USUARIO")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_severity_critical_iot_scope_CHANGED)+" VULNERABILIDADES ES ALCANCE ES CAMBIADO ")
print("            -    EN  "+str(cvssV3_BASE_severity_critical_iot_scope_UNCHANGED)+" VULNERABILIDADES ES ALCANCE NO ES CAMBIADO")
print("            -    EN  "+str(cvssV3_BASE_severity_critical_iot_scope_NONE)+" VULNERABILIDADES EL ALCANCE   ")
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
print("            -    EN  "+str(cvssV3_BASE_severity_high_iot_privilegesrequired_NONE)+" VULNERABILIDADES NO SE REQUIEREN PRIVILEGIOS")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_severity_high_iot_userinteraction_REQUIRED)+" VULNERABILIDADES SE REQUIERE INTERACCIÓN DE USUARIO ")
print("            -    EN  "+str(cvssV3_BASE_severity_high_iot_userinteraction_NONEREQUIRED)+" VULNERABILIDADES NO SE REQUIERE INTERACCIÓN DE USUARIO")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_severity_high_iot_scope_CHANGED)+" VULNERABILIDADES ES ALCANCE ES CAMBIADO ")
print("            -    EN  "+str(cvssV3_BASE_severity_high_iot_scope_UNCHANGED)+" VULNERABILIDADES ES ALCANCE NO ES CAMBIADO")
print("            -    EN  "+str(cvssV3_BASE_severity_high_iot_scope_NONE)+" VULNERABILIDADES EL ALCANCE   ")
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
print("            -    EN  "+str(cvssV3_BASE_severity_medium_iot_privilegesrequired_NONE)+" VULNERABILIDADES NO SE REQUIEREN PRIVILEGIOS")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_severity_medium_iot_userinteraction_REQUIRED)+" VULNERABILIDADES SE REQUIERE INTERACCIÓN DE USUARIO ")
print("            -    EN  "+str(cvssV3_BASE_severity_medium_iot_userinteraction_NONEREQUIRED)+" VULNERABILIDADES NO SE REQUIERE INTERACCIÓN DE USUARIO")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_severity_medium_iot_scope_CHANGED)+" VULNERABILIDADES ES ALCANCE ES CAMBIADO ")
print("            -    EN  "+str(cvssV3_BASE_severity_medium_iot_scope_UNCHANGED)+" VULNERABILIDADES ES ALCANCE NO ES CAMBIADO")
print("            -    EN  "+str(cvssV3_BASE_severity_medium_iot_scope_NONE)+" VULNERABILIDADES EL ALCANCE   ")
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
print("            -    EN  "+str(cvssV3_BASE_severity_low_iot_privilegesrequired_NONE)+" VULNERABILIDADES NO SE REQUIEREN PRIVILEGIOS")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_severity_low_iot_userinteraction_REQUIRED)+" VULNERABILIDADES SE REQUIERE INTERACCIÓN DE USUARIO ")
print("            -    EN  "+str(cvssV3_BASE_severity_low_iot_userinteraction_NONEREQUIRED)+" VULNERABILIDADES NO SE REQUIERE INTERACCIÓN DE USUARIO")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_severity_low_iot_scope_CHANGED)+" VULNERABILIDADES ES ALCANCE ES CAMBIADO ")
print("            -    EN  "+str(cvssV3_BASE_severity_low_iot_scope_UNCHANGED)+" VULNERABILIDADES ES ALCANCE NO ES CAMBIADO")
print("            -    EN  "+str(cvssV3_BASE_severity_low_iot_scope_NONE)+" VULNERABILIDADES EL ALCANCE   ")
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
print("********************PORCENTAJES ELEMENTOS VECTOR CVSSV3  CVSSV3 SEGUN SEVERIDAD********************")
print("\n")        
            
print("\n")
print(" DE UN TOTAL DE "+str(len(external_references_ids))+" VULNERABILIDADES ,  LOS PORCENTAJES DE LOS ELEMENTOS DEL VECTOR CVSSV3 SEGUN SEVERIDAD SON LOS SIGUIENTES:   \n")
print("\n")
print("      -    EN EL "+str(float(((cvssV3_BASE_severity_critical_iot*100)/len(external_references_ids))))+" % DE  VULNERABILIDADES LA SEVERIDAD ES CRITICA. LOS PORCENTAJES DEL VECTOR CVSSV3 SON LOS SIGUIENTES:  \n")
print("\n")
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
print("            -    EN EL "+str(float(((cvssV3_BASE_severity_critical_iot_privilegesrequired_NONE*100)/cvssV3_BASE_severity_critical_iot)))+" % DE  VULNERABILIDADES NO SE REQUIEREN PRIVILEGIOS")
print("\n")
print("            -    EN EL "+str(float(((cvssV3_BASE_severity_critical_iot_userinteraction_REQUIRED*100)/cvssV3_BASE_severity_critical_iot)))+" % DE  VULNERABILIDADES SE REQUIERE INTERACCIÓN DE USUARIO ")
print("            -    EN EL "+str(float(((cvssV3_BASE_severity_critical_iot_userinteraction_NONEREQUIRED*100)/cvssV3_BASE_severity_critical_iot)))+" % DE  VULNERABILIDADES NO SE REQUIERE INTERACCIÓN DE USUARIO")
print("\n")
print("            -    EN EL "+str(float(((cvssV3_BASE_severity_critical_iot_scope_CHANGED*100)/cvssV3_BASE_severity_critical_iot)))+" % DE  VULNERABILIDADES ES ALCANCE ES CAMBIADO ")
print("            -    EN EL "+str(float(((cvssV3_BASE_severity_critical_iot_scope_UNCHANGED*100)/cvssV3_BASE_severity_critical_iot)))+" % DE  VULNERABILIDADES ES ALCANCE NO ES CAMBIADO")
print("            -    EN EL "+str(float(((cvssV3_BASE_severity_critical_iot_scope_NONE*100)/cvssV3_BASE_severity_critical_iot)))+" % DE  VULNERABILIDADES EL ALCANCE   ")
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
    print("      -    EN EL "+str(float(((cvssV3_BASE_severity_high_iot*100)/len(external_references_ids))))+" % DE  VULNERABILIDADES LA SEVERIDAD ES ALTA. LOS PORCENTAJES DEL VECTOR CVSSV3 SON LOS SIGUIENTES:  \n")
    print("\n")
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
    print("            -    EN EL "+str(float(((cvssV3_BASE_severity_high_iot_privilegesrequired_NONE*100)/cvssV3_BASE_severity_high_iot)))+" % DE  VULNERABILIDADES NO SE REQUIEREN PRIVILEGIOS")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV3_BASE_severity_high_iot_userinteraction_REQUIRED*100)/cvssV3_BASE_severity_high_iot)))+" % DE  VULNERABILIDADES SE REQUIERE INTERACCIÓN DE USUARIO ")
    print("            -    EN EL "+str(float(((cvssV3_BASE_severity_high_iot_userinteraction_NONEREQUIRED*100)/cvssV3_BASE_severity_high_iot)))+" % DE  VULNERABILIDADES NO SE REQUIERE INTERACCIÓN DE USUARIO")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV3_BASE_severity_high_iot_scope_CHANGED*100)/cvssV3_BASE_severity_high_iot)))+" % DE  VULNERABILIDADES ES ALCANCE ES CAMBIADO ")
    print("            -    EN EL "+str(float(((cvssV3_BASE_severity_high_iot_scope_UNCHANGED*100)/cvssV3_BASE_severity_high_iot)))+" % DE  VULNERABILIDADES ES ALCANCE NO ES CAMBIADO")
    print("            -    EN EL "+str(float(((cvssV3_BASE_severity_high_iot_scope_NONE*100)/cvssV3_BASE_severity_high_iot)))+" % DE  VULNERABILIDADES EL ALCANCE   ")
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
    print("      -    EN EL "+str(float(((cvssV3_BASE_severity_medium_iot*100)/len(external_references_ids))))+" % DE  VULNERABILIDADES LA SEVERIDAD ES MEDIA. LOS PORCENTAJES DEL VECTOR CVSSV3 SON LOS SIGUIENTES:  \n")
    print("\n")
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
    print("            -    EN EL "+str(float(((cvssV3_BASE_severity_medium_iot_scope_NONE*100)/cvssV3_BASE_severity_medium_iot)))+" % DE  VULNERABILIDADES EL ALCANCE   ")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV3_BASE_severity_medium_iot_confidentialityImpact_HIGH*100)/cvssV3_BASE_severity_medium_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO ")
    print("            -    EN EL "+str(float(((cvssV3_BASE_severity_medium_iot_confidentialityImpact_LOW*100)/cvssV3_BASE_severity_medium_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO" )
    print("            -    EN EL "+str(float(((cvssV3_BASE_severity_medium_iot_confidentialityImpact_NONE*100)/cvssV3_BASE_severity_medium_iot)))+" % DE  VULNERABILIDADES NO SE PRODUCE IMPACTO DE CONFIDENCIALIDAD   ")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV3_BASE_severity_medium_iot_integrityImpact_HIGH*100)/cvssV3_BASE_severity_medium_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO ")
    print("            -    EN EL "+str(float(((cvssV3_BASE_severity_medium_iot_integrityImpact_LOW*100)/cvssV3_BASE_severity_medium_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO" )
    print("            -    EN EL "+str(float(((cvssV3_BASE_severity_medium_iot_integrityImpact_NONE*100)/cvssV3_BASE_severity_medium_iot)))+" % DE  VULNERABILIDADES NO SE PRODUCE IMPACTO DE INTEGRIDAD   ")
    print("\n")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV3_BASE_severity_medium_iot_availabilityImpact_HIGH*100)/cvssV3_BASE_severity_medium_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO ")
    print("            -    EN EL "+str(float(((cvssV3_BASE_severity_medium_iot_availabilityImpact_LOW*100)/cvssV3_BASE_severity_medium_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO" )
    print("            -    EN EL "+str(float(((cvssV3_BASE_severity_medium_iot_availabilityImpact_NONE*100)/cvssV3_BASE_severity_medium_iot)))+" % DE  VULNERABILIDADES NO SE PRODUCE IMPACTO DE DISPONIBILIDAD   ")
    print("\n")
    print("\n")     


if(cvssV3_BASE_severity_low_iot>0):
    print("      -    EN EL "+str(float(((cvssV3_BASE_severity_low_iot*100)/len(external_references_ids))))+" % DE  VULNERABILIDADES LA SEVERIDAD ES BAJA. LOS PORCENTAJES DEL VECTOR CVSSV3 SON LOS SIGUIENTES:  \n")
    print("\n")
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
    print("            -    EN EL "+str(float(((cvssV3_BASE_severity_low_iot_privilegesrequired_NONE*100)/cvssV3_BASE_severity_low_iot)))+" % DE  VULNERABILIDADES NO SE REQUIEREN PRIVILEGIOS")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV3_BASE_severity_low_iot_userinteraction_REQUIRED*100)/cvssV3_BASE_severity_low_iot)))+" % DE  VULNERABILIDADES SE REQUIERE INTERACCIÓN DE USUARIO ")
    print("            -    EN EL "+str(float(((cvssV3_BASE_severity_low_iot_userinteraction_NONEREQUIRED*100)/cvssV3_BASE_severity_low_iot)))+" % DE  VULNERABILIDADES NO SE REQUIERE INTERACCIÓN DE USUARIO")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV3_BASE_severity_low_iot_scope_CHANGED*100)/cvssV3_BASE_severity_low_iot)))+" % DE  VULNERABILIDADES ES ALCANCE ES CAMBIADO ")
    print("            -    EN EL "+str(float(((cvssV3_BASE_severity_low_iot_scope_UNCHANGED*100)/cvssV3_BASE_severity_low_iot)))+" % DE  VULNERABILIDADES ES ALCANCE NO ES CAMBIADO")
    print("            -    EN EL "+str(float(((cvssV3_BASE_severity_low_iot_scope_NONE*100)/cvssV3_BASE_severity_low_iot)))+" % DE  VULNERABILIDADES EL ALCANCE   ")
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



















