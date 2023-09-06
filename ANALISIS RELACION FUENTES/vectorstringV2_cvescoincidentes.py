import pandas as pd


df_cve_iot=pd.read_excel('cves_iot_2023.xlsx')
df_cve_sh=pd.read_excel('cves_smart_home_2023.xlsx')

cves=['CVE-2023-23379','CVE-2022-29859','CVE-2022-34326','CVE-2022-34021','CVE-2021-43702','CVE-2019-12266','CVE-2022-23265','CVE-2021-43573','CVE-2021-1441','CVE-2022-33005','CVE-2023-0847','CVE-2023-23575','CVE-2023-27389','CVE-2023-27917','CVE-2023-25017','CVE-2023-25018','CVE-2022-25075','CVE-2020-8105','CVE-2021-35395','CVE-2021-28372']




cvssV2_BASE_severity_high_iot=0

#Tipo de vector de acceso segun puntuacion BASE
cvssV2_BASE_severity_high_iot_accessvector_NETWORK=0
cvssV2_BASE_severity_high_iot_accessvector_PHYSICAL=0
cvssV2_BASE_severity_high_iot_accessvector_LOCAL=0
cvssV2_BASE_severity_high_iot_accessvector_ADJACENT_NETWORK=0

#Complejidad de acceso segun puntuacion BASE
cvssV2_BASE_severity_high_iot_accesscomplexity_HIGH=0
cvssV2_BASE_severity_high_iot_accesscomplexity_LOW=0
cvssV2_BASE_severity_high_iot_accesscomplexity_MEDIUM=0
cvssV2_BASE_severity_high_iot_accesscomplexity_NONE=0

#Nivel de autenticacion segun puntuacion BASE
cvssV2_BASE_severity_high_iot_authentication_SINGLE=0
cvssV2_BASE_severity_high_iot_authentication_MULTIPLE=0
cvssV2_BASE_severity_high_iot_authentication_NONE=0

#Impacto de confidencialidad segun puntuacion BASE
cvssV2_BASE_severity_high_iot_confidentialityImpact_COMPLETE=0
cvssV2_BASE_severity_high_iot_confidentialityImpact_PARTIAL=0
cvssV2_BASE_severity_high_iot_confidentialityImpact_NONE=0

#Impacto de integridad segun puntuacion BASE
cvssV2_BASE_severity_high_iot_integrityImpact_COMPLETE=0
cvssV2_BASE_severity_high_iot_integrityImpact_PARTIAL=0
cvssV2_BASE_severity_high_iot_integrityImpact_NONE=0

#Impacto de disponibilidad segun puntuacion BASE
cvssV2_BASE_severity_high_iot_availabilityImpact_COMPLETE=0
cvssV2_BASE_severity_high_iot_availabilityImpact_PARTIAL=0
cvssV2_BASE_severity_high_iot_availabilityImpact_NONE=0



cvssV2_BASE_severity_medium_iot=0

#Tipo de vector de acceso segun puntuacion BASE
cvssV2_BASE_severity_medium_iot_accessvector_NETWORK=0
cvssV2_BASE_severity_medium_iot_accessvector_PHYSICAL=0
cvssV2_BASE_severity_medium_iot_accessvector_LOCAL=0
cvssV2_BASE_severity_medium_iot_accessvector_ADJACENT_NETWORK=0

#Complejidad de acceso segun puntuacion BASE
cvssV2_BASE_severity_medium_iot_accesscomplexity_HIGH=0
cvssV2_BASE_severity_medium_iot_accesscomplexity_LOW=0
cvssV2_BASE_severity_medium_iot_accesscomplexity_MEDIUM=0
cvssV2_BASE_severity_medium_iot_accesscomplexity_NONE=0

#Nivel de autenticacion segun puntuacion BASE
cvssV2_BASE_severity_medium_iot_authentication_SINGLE=0
cvssV2_BASE_severity_medium_iot_authentication_MULTIPLE=0
cvssV2_BASE_severity_medium_iot_authentication_NONE=0

#Impacto de confidencialidad segun puntuacion BASE
cvssV2_BASE_severity_medium_iot_confidentialityImpact_COMPLETE=0
cvssV2_BASE_severity_medium_iot_confidentialityImpact_PARTIAL=0
cvssV2_BASE_severity_medium_iot_confidentialityImpact_NONE=0

#Impacto de integridad segun puntuacion BASE
cvssV2_BASE_severity_medium_iot_integrityImpact_COMPLETE=0
cvssV2_BASE_severity_medium_iot_integrityImpact_PARTIAL=0
cvssV2_BASE_severity_medium_iot_integrityImpact_NONE=0

#Impacto de disponibilidad segun puntuacion BASE
cvssV2_BASE_severity_medium_iot_availabilityImpact_COMPLETE=0
cvssV2_BASE_severity_medium_iot_availabilityImpact_PARTIAL=0
cvssV2_BASE_severity_medium_iot_availabilityImpact_NONE=0


cvssV2_BASE_severity_low_iot=0

#Tipo de vector de acceso segun puntuacion BASE
cvssV2_BASE_severity_low_iot_accessvector_NETWORK=0
cvssV2_BASE_severity_low_iot_accessvector_PHYSICAL=0
cvssV2_BASE_severity_low_iot_accessvector_LOCAL=0
cvssV2_BASE_severity_low_iot_accessvector_ADJACENT_NETWORK=0

#Complejidad de acceso segun puntuacion BASE
cvssV2_BASE_severity_low_iot_accesscomplexity_HIGH=0
cvssV2_BASE_severity_low_iot_accesscomplexity_LOW=0
cvssV2_BASE_severity_low_iot_accesscomplexity_MEDIUM=0
cvssV2_BASE_severity_low_iot_accesscomplexity_NONE=0

#Nivel de autenticacion segun puntuacion BASE
cvssV2_BASE_severity_low_iot_authentication_SINGLE=0
cvssV2_BASE_severity_low_iot_authentication_MULTIPLE=0
cvssV2_BASE_severity_low_iot_authentication_NONE=0

#Impacto de confidencialidad segun puntuacion BASE
cvssV2_BASE_severity_low_iot_confidentialityImpact_COMPLETE=0
cvssV2_BASE_severity_low_iot_confidentialityImpact_PARTIAL=0
cvssV2_BASE_severity_low_iot_confidentialityImpact_NONE=0

#Impacto de integridad segun puntuacion BASE
cvssV2_BASE_severity_low_iot_integrityImpact_COMPLETE=0
cvssV2_BASE_severity_low_iot_integrityImpact_PARTIAL=0
cvssV2_BASE_severity_low_iot_integrityImpact_NONE=0

#Impacto de disponibilidad segun puntuacion BASE
cvssV2_BASE_severity_low_iot_availabilityImpact_COMPLETE=0
cvssV2_BASE_severity_low_iot_availabilityImpact_PARTIAL=0
cvssV2_BASE_severity_low_iot_availabilityImpact_NONE=0



#Buscamos los CVES coincidentes y analizamos los elementos de su VECTOR CVSSV2
for j in range(0,len(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.baseScore"])):
    if((df_cve_iot["CVE_Items.cve.CVE_data_meta.ID"][j].replace('[','').replace(']','').replace("'","").replace("","").replace(" ","")) in cves):
        if(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.baseScore"][j] != 'NONE'):
            if(((float(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.baseScore"][j])) <=10.0) and ((float(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.baseScore"][j])) >=7.0)):
                cvssV2_BASE_severity_high_iot+=1
                if(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.accessVector"][j]=='NETWORK'):
                    cvssV2_BASE_severity_high_iot_accessvector_NETWORK+=1
                elif(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.accessVector"][j]=='LOCAL'):
                    cvssV2_BASE_severity_high_iot_accessvector_LOCAL+=1
                elif(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.accessVector"][j]=='ADJACENT_NETWORK'):
                    cvssV2_BASE_severity_high_iot_accessvector_ADJACENT_NETWORK+=1

                if(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.accessComplexity"][j]=='HIGH'):
                    cvssV2_BASE_severity_high_iot_accesscomplexity_HIGH+=1
                elif(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.accessComplexity"][j]=='LOW'):
                    cvssV2_BASE_severity_high_iot_accesscomplexity_LOW+=1
                elif(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.accessComplexity"][j]=='MEDIUM'):
                    cvssV2_BASE_severity_high_iot_accesscomplexity_MEDIUM+=1
                else:
                    cvssV2_BASE_severity_high_iot_accesscomplexity_NONE+=1  

                if(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.authentication"][j]=='SINGLE'):
                    cvssV2_BASE_severity_high_iot_authentication_SINGLE+=1
                elif(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.authentication"][j]=='MULTIPLE'):
                    cvssV2_BASE_severity_high_iot_authentication_MULTIPLE+=1
                else:
                    cvssV2_BASE_severity_high_iot_authentication_NONE+=1

                if(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.confidentialityImpact"][j]=='COMPLETE'):
                    cvssV2_BASE_severity_high_iot_confidentialityImpact_COMPLETE+=1
                elif(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.confidentialityImpact"][j]=='PARTIAL'):
                    cvssV2_BASE_severity_high_iot_confidentialityImpact_PARTIAL+=1
                else:
                    cvssV2_BASE_severity_high_iot_confidentialityImpact_NONE+=1 


                if(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.integrityImpact"][j]=='COMPLETE'):
                    cvssV2_BASE_severity_high_iot_integrityImpact_COMPLETE+=1
                elif(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.integrityImpact"][j]=='PARTIAL'):
                    cvssV2_BASE_severity_high_iot_integrityImpact_PARTIAL+=1
                else:
                    cvssV2_BASE_severity_high_iot_integrityImpact_NONE+=1    


                if(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.availabilityImpact"][j]=='COMPLETE'):
                    cvssV2_BASE_severity_high_iot_availabilityImpact_COMPLETE+=1
                elif(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.availabilityImpact"][j]=='PARTIAL'):
                    cvssV2_BASE_severity_high_iot_availabilityImpact_PARTIAL+=1
                else:
                    cvssV2_BASE_severity_high_iot_availabilityImpact_NONE+=1

            elif(((float(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.baseScore"][j])) < 7.0) and ((float(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.baseScore"][j])) >=4.0)):
                cvssV2_BASE_severity_medium_iot+=1

                if(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.accessVector"][j]=='NETWORK'):
                    cvssV2_BASE_severity_high_iot_accessvector_NETWORK+=1
                elif(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.accessVector"][j]=='LOCAL'):
                    cvssV2_BASE_severity_medium_iot_accessvector_LOCAL+=1
                elif(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.accessVector"][j]=='ADJACENT_NETWORK'):
                    cvssV2_BASE_severity_medium_iot_accessvector_ADJACENT_NETWORK+=1

                if(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.accessComplexity"][j]=='HIGH'):
                    cvssV2_BASE_severity_medium_iot_accesscomplexity_HIGH+=1
                elif(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.accessComplexity"][j]=='LOW'):
                    cvssV2_BASE_severity_high_iot_accesscomplexity_LOW+=1
                elif(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.accessComplexity"][j]=='MEDIUM'):
                    cvssV2_BASE_severity_medium_iot_accesscomplexity_MEDIUM+=1
                else:
                    cvssV2_BASE_severity_medium_iot_accesscomplexity_NONE+=1  

                if(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.authentication"][j]=='SINGLE'):
                    cvssV2_BASE_severity_medium_iot_authentication_SINGLE+=1
                elif(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.authentication"][j]=='MULTIPLE'):
                    cvssV2_BASE_severity_medium_iot_authentication_MULTIPLE+=1
                else:
                    cvssV2_BASE_severity_medium_iot_authentication_NONE+=1


                if(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.confidentialityImpact"][j]=='COMPLETE'):
                    cvssV2_BASE_severity_medium_iot_confidentialityImpact_COMPLETE+=1
                elif(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.confidentialityImpact"][j]=='PARTIAL'):
                    cvssV2_BASE_severity_medium_iot_confidentialityImpact_PARTIAL+=1
                else:
                    cvssV2_BASE_severity_medium_iot_confidentialityImpact_NONE+=1 


                if(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.integrityImpact"][j]=='COMPLETE'):
                    cvssV2_BASE_severity_medium_iot_integrityImpact_COMPLETE+=1
                elif(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.integrityImpact"][j]=='PARTIAL'):
                    cvssV2_BASE_severity_medium_iot_integrityImpact_PARTIAL+=1
                else:
                    cvssV2_BASE_severity_medium_iot_integrityImpact_NONE+=1    


                if(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.availabilityImpact"][j]=='COMPLETE'):
                    cvssV2_BASE_severity_medium_iot_availabilityImpact_COMPLETE+=1
                elif(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.availabilityImpact"][j]=='PARTIAL'):
                    cvssV2_BASE_severity_medium_iot_availabilityImpact_PARTIAL+=1
                else:
                    cvssV2_BASE_severity_medium_iot_availabilityImpact_NONE+=1

            elif(((float(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.baseScore"][j])) < 4.0) and ((float(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.baseScore"][j])) >=0.0)):
                cvssV2_BASE_severity_low_iot+=1

                if(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.accessVector"][j]=='NETWORK'):
                    cvssV2_BASE_severity_high_iot_accessvector_NETWORK+=1
                elif(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.accessVector"][j]=='LOCAL'):
                    cvssV2_BASE_severity_low_iot_accessvector_LOCAL+=1
                elif(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.accessVector"][j]=='ADJACENT_NETWORK'):
                    cvssV2_BASE_severity_low_iot_accessvector_ADJACENT_NETWORK+=1

                if(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.accessComplexity"][j]=='HIGH'):
                    cvssV2_BASE_severity_low_iot_accesscomplexity_HIGH+=1
                elif(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.accessComplexity"][j]=='LOW'):
                    cvssV2_BASE_severity_high_iot_accesscomplexity_LOW+=1
                elif(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.accessComplexity"][j]=='MEDIUM'):
                    cvssV2_BASE_severity_low_iot_accesscomplexity_MEDIUM+=1
                else:
                    cvssV2_BASE_severity_low_iot_accesscomplexity_NONE+=1  

                if(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.authentication"][j]=='SINGLE'):
                    cvssV2_BASE_severity_low_iot_authentication_SINGLE+=1
                elif(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.authentication"][j]=='MULTIPLE'):
                    cvssV2_BASE_severity_low_iot_authentication_MULTIPLE+=1
                else:
                    cvssV2_BASE_severity_low_iot_authentication_NONE+=1

                if(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.confidentialityImpact"][j]=='COMPLETE'):
                    cvssV2_BASE_severity_low_iot_confidentialityImpact_COMPLETE+=1
                elif(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.confidentialityImpact"][j]=='PARTIAL'):
                    cvssV2_BASE_severity_low_iot_confidentialityImpact_PARTIAL+=1
                else:
                    cvssV2_BASE_severity_low_iot_confidentialityImpact_NONE+=1 


                if(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.integrityImpact"][j]=='COMPLETE'):
                    cvssV2_BASE_severity_low_iot_integrityImpact_COMPLETE+=1
                elif(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.integrityImpact"][j]=='PARTIAL'):
                    cvssV2_BASE_severity_low_iot_integrityImpact_PARTIAL+=1
                else:
                    cvssV2_BASE_severity_low_iot_integrityImpact_NONE+=1    


                if(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.availabilityImpact"][j]=='COMPLETE'):
                    cvssV2_BASE_severity_low_iot_availabilityImpact_COMPLETE+=1
                elif(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.availabilityImpact"][j]=='PARTIAL'):
                    cvssV2_BASE_severity_low_iot_availabilityImpact_PARTIAL+=1
                else:
                    cvssV2_BASE_severity_low_iot_availabilityImpact_NONE+=1

print("\n")                
print("\n")                
print("*************************ESTADÍSTICAS ELEMENTOS VECTOR CVSSV2 SEGÚN SEVERIDAD BASE*************************")
print("\n")        



print("\n")
print(" DE UN TOTAL DE "+str(len(cves))+" VULNERABILIDADES , LAS ESTADISTICAS DE LA RELACION DE ELEMENTOS DEL VECTOR CVSSV2 SEGUN SEVERIDAD BASE SON LAS SIGUIENTES:  \n")
print("\n")
print("      -    EN  "+str(cvssV2_BASE_severity_high_iot)+" VULNERABILIDADES LA SEVERIDAD ES ALTA. LAS ESTADÍSTICAS DEL VECTOR CVSSV2 SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(cvssV2_BASE_severity_high_iot_accessvector_NETWORK)+" VULNERABILIDADES EL VECTOR DE ACCESO ES LA RED ")
print("            -    EN  "+str(cvssV2_BASE_severity_high_iot_accessvector_LOCAL)+" VULNERABILIDADES EL VECTOR DE ACCESO ES LOCAL ")
print("            -    EN  "+str(cvssV2_BASE_severity_high_iot_accessvector_ADJACENT_NETWORK)+" VULNERABILIDADES EL VECTOR DE ACCESO ES UNA RED ADYACENTE ")
print("\n")
print("            -    EN  "+str(cvssV2_BASE_severity_high_iot_accesscomplexity_HIGH)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES ALTA ")
print("            -    EN  "+str(cvssV2_BASE_severity_high_iot_accesscomplexity_LOW)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES BAJA ")
print("            -    EN  "+str(cvssV2_BASE_severity_high_iot_accesscomplexity_MEDIUM)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES MEDIA ")
print("\n")
print("            -    EN  "+str(cvssV2_BASE_severity_high_iot_authentication_SINGLE)+" VULNERABILIDADES LA AUTENTICACION ES SENCILLA")
print("            -    EN  "+str(cvssV2_BASE_severity_high_iot_authentication_MULTIPLE)+" VULNERABILIDADES LA AUTENTICACION ES MULTIPLE")
print("            -    EN  "+str(cvssV2_BASE_severity_high_iot_authentication_NONE)+" VULNERABILIDADES NO SE REQUIERE NINGUNA AUTENTICACION DEL USUARIO")
print("\n")
print("            -    EN  "+str(cvssV2_BASE_severity_high_iot_confidentialityImpact_COMPLETE)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES COMPLETO ")
print("            -    EN  "+str(cvssV2_BASE_severity_high_iot_confidentialityImpact_PARTIAL)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES PARCIAL" )
print("            -    EN  "+str(cvssV2_BASE_severity_high_iot_confidentialityImpact_NONE)+" VULNERABILIDADES NO SE PRODUCE IMPACTO DE CONFIDENCIALIDAD ")
print("\n")
print("            -    EN  "+str(cvssV2_BASE_severity_high_iot_integrityImpact_COMPLETE)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES COMPLETO ")
print("            -    EN  "+str(cvssV2_BASE_severity_high_iot_integrityImpact_PARTIAL)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES PARCIAL" )
print("            -    EN  "+str(cvssV2_BASE_severity_high_iot_integrityImpact_NONE)+" VULNERABILIDADES NO SE PRODUCE IMPACTO DE CONFIDENCIALIDAD ")
print("\n")
print("\n")
print("            -    EN  "+str(cvssV2_BASE_severity_high_iot_availabilityImpact_COMPLETE)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES COMPLETO ")
print("            -    EN  "+str(cvssV2_BASE_severity_high_iot_availabilityImpact_PARTIAL)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES PARCIAL" )
print("            -    EN  "+str(cvssV2_BASE_severity_high_iot_availabilityImpact_NONE)+" VULNERABILIDADES NO SE PRODUCE IMPACTO DE CONFIDENCIALIDAD ")
print("\n")
print("\n")

print("      -    EN  "+str(cvssV2_BASE_severity_medium_iot)+" VULNERABILIDADES LA SEVERIDAD ES MEDIA. LAS ESTADÍSTICAS DEL VECTOR CVSSV2 SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(cvssV2_BASE_severity_medium_iot_accessvector_NETWORK)+" VULNERABILIDADES EL VECTOR DE ACCESO ES LA RED ")
print("            -    EN  "+str(cvssV2_BASE_severity_medium_iot_accessvector_LOCAL)+" VULNERABILIDADES EL VECTOR DE ACCESO ES LOCAL ")
print("            -    EN  "+str(cvssV2_BASE_severity_medium_iot_accessvector_ADJACENT_NETWORK)+" VULNERABILIDADES EL VECTOR DE ACCESO ES UNA RED ADYACENTE ")
print("\n")
print("            -    EN  "+str(cvssV2_BASE_severity_medium_iot_accesscomplexity_HIGH)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES ALTA ")
print("            -    EN  "+str(cvssV2_BASE_severity_medium_iot_accesscomplexity_LOW)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES BAJA ")
print("            -    EN  "+str(cvssV2_BASE_severity_medium_iot_accesscomplexity_MEDIUM)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES MEDIA ")
print("\n")
print("            -    EN  "+str(cvssV2_BASE_severity_medium_iot_authentication_SINGLE)+" VULNERABILIDADES LA AUTENTICACION ES SENCILLA")
print("            -    EN  "+str(cvssV2_BASE_severity_medium_iot_authentication_MULTIPLE)+" VULNERABILIDADES LA AUTENTICACION ES MULTIPLE")
print("            -    EN  "+str(cvssV2_BASE_severity_medium_iot_authentication_NONE)+" VULNERABILIDADES NO SE REQUIERE NINGUNA AUTENTICACION DEL USUARIO")
print("\n")
print("            -    EN  "+str(cvssV2_BASE_severity_medium_iot_confidentialityImpact_COMPLETE)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES COMPLETO ")
print("            -    EN  "+str(cvssV2_BASE_severity_medium_iot_confidentialityImpact_PARTIAL)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES PARCIAL" )
print("            -    EN  "+str(cvssV2_BASE_severity_medium_iot_confidentialityImpact_NONE)+" VULNERABILIDADES NO SE PRODUCE IMPACTO DE CONFIDENCIALIDAD ")
print("\n")
print("            -    EN  "+str(cvssV2_BASE_severity_medium_iot_integrityImpact_COMPLETE)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES COMPLETO ")
print("            -    EN  "+str(cvssV2_BASE_severity_medium_iot_integrityImpact_PARTIAL)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES PARCIAL" )
print("            -    EN  "+str(cvssV2_BASE_severity_medium_iot_integrityImpact_NONE)+" VULNERABILIDADES NO SE PRODUCE IMPACTO DE CONFIDENCIALIDAD ")
print("\n")
print("\n")
print("            -    EN  "+str(cvssV2_BASE_severity_medium_iot_availabilityImpact_COMPLETE)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES COMPLETO ")
print("            -    EN  "+str(cvssV2_BASE_severity_medium_iot_availabilityImpact_PARTIAL)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES PARCIAL" )
print("            -    EN  "+str(cvssV2_BASE_severity_medium_iot_availabilityImpact_NONE)+" VULNERABILIDADES NO SE PRODUCE IMPACTO DE CONFIDENCIALIDAD ")
print("\n")
print("\n")
print("      -    EN  "+str(cvssV2_BASE_severity_low_iot)+" VULNERABILIDADES LA SEVERIDAD ES BAJA. LAS ESTADÍSTICAS DEL VECTOR CVSSV2 SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(cvssV2_BASE_severity_low_iot_accessvector_NETWORK)+" VULNERABILIDADES EL VECTOR DE ACCESO ES LA RED ")
print("            -    EN  "+str(cvssV2_BASE_severity_low_iot_accessvector_LOCAL)+" VULNERABILIDADES EL VECTOR DE ACCESO ES LOCAL ")
print("            -    EN  "+str(cvssV2_BASE_severity_low_iot_accessvector_ADJACENT_NETWORK)+" VULNERABILIDADES EL VECTOR DE ACCESO ES UNA RED ADYACENTE ")
print("\n")
print("            -    EN  "+str(cvssV2_BASE_severity_low_iot_accesscomplexity_HIGH)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES ALTA ")
print("            -    EN  "+str(cvssV2_BASE_severity_low_iot_accesscomplexity_LOW)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES BAJA ")
print("            -    EN  "+str(cvssV2_BASE_severity_low_iot_accesscomplexity_MEDIUM)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES MEDIA ")
print("\n")
print("            -    EN  "+str(cvssV2_BASE_severity_low_iot_authentication_SINGLE)+" VULNERABILIDADES LA AUTENTICACION ES SENCILLA")
print("            -    EN  "+str(cvssV2_BASE_severity_low_iot_authentication_MULTIPLE)+" VULNERABILIDADES LA AUTENTICACION ES MULTIPLE")
print("            -    EN  "+str(cvssV2_BASE_severity_low_iot_authentication_NONE)+" VULNERABILIDADES NO SE REQUIERE NINGUNA AUTENTICACION DEL USUARIO")
print("\n")
print("            -    EN  "+str(cvssV2_BASE_severity_low_iot_confidentialityImpact_COMPLETE)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES COMPLETO ")
print("            -    EN  "+str(cvssV2_BASE_severity_low_iot_confidentialityImpact_PARTIAL)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES PARCIAL" )
print("            -    EN  "+str(cvssV2_BASE_severity_low_iot_confidentialityImpact_NONE)+" VULNERABILIDADES NO SE PRODUCE IMPACTO DE CONFIDENCIALIDAD ")
print("\n")
print("            -    EN  "+str(cvssV2_BASE_severity_low_iot_integrityImpact_COMPLETE)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES COMPLETO ")
print("            -    EN  "+str(cvssV2_BASE_severity_low_iot_integrityImpact_PARTIAL)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES PARCIAL" )
print("            -    EN  "+str(cvssV2_BASE_severity_low_iot_integrityImpact_NONE)+" VULNERABILIDADES NO SE PRODUCE IMPACTO DE CONFIDENCIALIDAD ")
print("\n")
print("\n")
print("            -    EN  "+str(cvssV2_BASE_severity_low_iot_availabilityImpact_COMPLETE)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES COMPLETO ")
print("            -    EN  "+str(cvssV2_BASE_severity_low_iot_availabilityImpact_PARTIAL)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES PARCIAL" )
print("            -    EN  "+str(cvssV2_BASE_severity_low_iot_availabilityImpact_NONE)+" VULNERABILIDADES NO SE PRODUCE IMPACTO DE CONFIDENCIALIDAD ")
print("\n")
print("\n")

print("\n")
print("\n")
print("*************************PORCENTAJES ELEMENTOS VECTOR CVSSV2 SEGUN SEVERIDAD BASE*************************")
print("\n")        

print("\n")
print(" DE UN TOTAL DE "+str(len(cves))+" VULNERABILIDADES ,  LOS PORCENTAJES DE LA RELACION DE ELEMENTOS DEL VECTOR CVSSV2 SEGUN SEVERIDAD BASE SON LOS SIGUIENTES:   \n")
print("\n")
print("      -    EN EL "+str(float(((cvssV2_BASE_severity_high_iot*100)/len(cves))))+" % DE  VULNERABILIDADES LA SEVERIDAD ES ALTA. LOS PORCENTAJES DEL VECTOR CVSSV2 SON LOS SIGUIENTES:  \n")
print("\n")
print("            -    EN EL "+str(float(((cvssV2_BASE_severity_high_iot_accessvector_NETWORK*100)/cvssV2_BASE_severity_high_iot)))+" % DE  VULNERABILIDADES EL VECTOR DE ACCESO ES LA RED ")
print("            -    EN EL "+str(float(((cvssV2_BASE_severity_high_iot_accessvector_LOCAL*100)/cvssV2_BASE_severity_high_iot)))+" % DE  VULNERABILIDADES EL VECTOR DE ACCESO ES LOCAL ")
print("            -    EN EL "+str(float(((cvssV2_BASE_severity_high_iot_accessvector_ADJACENT_NETWORK*100)/cvssV2_BASE_severity_high_iot)))+" % DE  VULNERABILIDADES EL VECTOR DE ACCESO ES UNA RED ADYACENTE ")
print("\n")
print("            -    EN EL "+str(float(((cvssV2_BASE_severity_high_iot_accesscomplexity_HIGH*100)/cvssV2_BASE_severity_high_iot)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES ALTA ")
print("            -    EN EL "+str(float(((cvssV2_BASE_severity_high_iot_accesscomplexity_LOW*100)/cvssV2_BASE_severity_high_iot)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES BAJA ")
print("            -    EN EL "+str(float(((cvssV2_BASE_severity_high_iot_accesscomplexity_MEDIUM*100)/cvssV2_BASE_severity_high_iot)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES MEDIA ")
print("\n")
print("            -    EN EL "+str(float(((cvssV2_BASE_severity_high_iot_authentication_SINGLE*100)/cvssV2_BASE_severity_high_iot)))+" % DE  VULNERABILIDADES LA AUTENTICACION ES SENCILLA ")
print("            -    EN EL "+str(float(((cvssV2_BASE_severity_high_iot_authentication_MULTIPLE*100)/cvssV2_BASE_severity_high_iot)))+" % DE  VULNERABILIDADES LA AUTENTICACION ES MULTIPLE")
print("            -    EN EL "+str(float(((cvssV2_BASE_severity_high_iot_authentication_NONE*100)/cvssV2_BASE_severity_high_iot)))+" % DE  VULNERABILIDADES NO SE REQUIERE NINGUNA AUTENTICACION DEL USUARIO")
print("\n")
print("            -    EN EL "+str(float(((cvssV2_BASE_severity_high_iot_confidentialityImpact_COMPLETE*100)/cvssV2_BASE_severity_high_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES COMPLETO ")
print("            -    EN EL "+str(float(((cvssV2_BASE_severity_high_iot_confidentialityImpact_PARTIAL*100)/cvssV2_BASE_severity_high_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES PARCIAL" )
print("            -    EN EL "+str(float(((cvssV2_BASE_severity_high_iot_confidentialityImpact_NONE*100)/cvssV2_BASE_severity_high_iot)))+" % DE  VULNERABILIDADES NO SE PRODUCE IMPACTO DE CONFIDENCIALIDAD ")
print("\n")
print("            -    EN EL "+str(float(((cvssV2_BASE_severity_high_iot_integrityImpact_COMPLETE*100)/cvssV2_BASE_severity_high_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES COMPLETO ")
print("            -    EN EL "+str(float(((cvssV2_BASE_severity_high_iot_integrityImpact_PARTIAL*100)/cvssV2_BASE_severity_high_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES PARCIAL" )
print("            -    EN EL "+str(float(((cvssV2_BASE_severity_high_iot_integrityImpact_NONE*100)/cvssV2_BASE_severity_high_iot)))+" % DE  VULNERABILIDADES NO SE PRODUCE IMPACTO DE CONFIDENCIALIDAD ")
print("\n")
print("\n")
print("            -    EN EL "+str(float(((cvssV2_BASE_severity_high_iot_availabilityImpact_COMPLETE*100)/cvssV2_BASE_severity_high_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES COMPLETO ")
print("            -    EN EL "+str(float(((cvssV2_BASE_severity_high_iot_availabilityImpact_PARTIAL*100)/cvssV2_BASE_severity_high_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES PARCIAL" )
print("            -    EN EL "+str(float(((cvssV2_BASE_severity_high_iot_availabilityImpact_NONE*100)/cvssV2_BASE_severity_high_iot)))+" % DE  VULNERABILIDADES NO SE PRODUCE IMPACTO DE CONFIDENCIALIDAD ")
print("\n")
print("\n")     


if(cvssV2_BASE_severity_medium_iot>0):
    print("      -    EN EL "+str(float(((cvssV2_BASE_severity_medium_iot*100)/len(cves))))+" % DE VULNERABILIDADES LA SEVERIDAD ES MEDIA. LOS PORCENTAJES DEL VECTOR CVSSV2 SON LOS SIGUIENTES:  \n")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV2_BASE_severity_medium_iot_accessvector_NETWORK*100)/cvssV2_BASE_severity_medium_iot)))+" % DE VULNERABILIDADES EL VECTOR DE ACCESO ES LA RED ")
    print("            -    EN EL "+str(float(((cvssV2_BASE_severity_medium_iot_accessvector_LOCAL*100)/cvssV2_BASE_severity_medium_iot)))+" % DE  VULNERABILIDADES EL VECTOR DE ACCESO ES LOCAL ")
    print("            -    EN EL "+str(float(((cvssV2_BASE_severity_medium_iot_accessvector_ADJACENT_NETWORK*100)/cvssV2_BASE_severity_medium_iot)))+" % DE  VULNERABILIDADES EL VECTOR DE ACCESO ES UNA RED ADYACENTE ")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV2_BASE_severity_medium_iot_accesscomplexity_HIGH*100)/cvssV2_BASE_severity_medium_iot)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES ALTA ")
    print("            -    EN EL "+str(float(((cvssV2_BASE_severity_medium_iot_accesscomplexity_LOW*100)/cvssV2_BASE_severity_medium_iot)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES BAJA ")
    print("            -    EN EL "+str(float(((cvssV2_BASE_severity_medium_iot_accesscomplexity_MEDIUM*100)/cvssV2_BASE_severity_medium_iot)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES MEDIA ")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV2_BASE_severity_medium_iot_authentication_SINGLE*100)/cvssV2_BASE_severity_medium_iot)))+" % DE  VULNERABILIDADES LA AUTENTICACION ES SENCILLA ")
    print("            -    EN EL "+str(float(((cvssV2_BASE_severity_medium_iot_authentication_MULTIPLE*100)/cvssV2_BASE_severity_medium_iot)))+" % DE  VULNERABILIDADES LA AUTENTICACION ES MULTIPLE")
    print("            -    EN EL "+str(float(((cvssV2_BASE_severity_medium_iot_authentication_NONE*100)/cvssV2_BASE_severity_medium_iot)))+" % DE  VULNERABILIDADES NO SE REQUIERE NINGUNA AUTENTICACION DEL USUARIO")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV2_BASE_severity_medium_iot_confidentialityImpact_COMPLETE*100)/cvssV2_BASE_severity_medium_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES COMPLETO ")
    print("            -    EN EL "+str(float(((cvssV2_BASE_severity_medium_iot_confidentialityImpact_PARTIAL*100)/cvssV2_BASE_severity_medium_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES PARCIAL" )
    print("            -    EN EL "+str(float(((cvssV2_BASE_severity_medium_iot_confidentialityImpact_NONE*100)/cvssV2_BASE_severity_medium_iot)))+" % DE  VULNERABILIDADES NO SE PRODUCE IMPACTO DE CONFIDENCIALIDAD ")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV2_BASE_severity_medium_iot_integrityImpact_COMPLETE*100)/cvssV2_BASE_severity_medium_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES COMPLETO ")
    print("            -    EN EL "+str(float(((cvssV2_BASE_severity_medium_iot_integrityImpact_PARTIAL*100)/cvssV2_BASE_severity_medium_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES PARCIAL" )
    print("            -    EN EL "+str(float(((cvssV2_BASE_severity_medium_iot_integrityImpact_NONE*100)/cvssV2_BASE_severity_medium_iot)))+" % DE  VULNERABILIDADES NO SE PRODUCE IMPACTO DE CONFIDENCIALIDAD ")
    print("\n")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV2_BASE_severity_medium_iot_availabilityImpact_COMPLETE*100)/cvssV2_BASE_severity_medium_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES COMPLETO ")
    print("            -    EN EL "+str(float(((cvssV2_BASE_severity_medium_iot_availabilityImpact_PARTIAL*100)/cvssV2_BASE_severity_medium_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES PARCIAL" )
    print("            -    EN EL "+str(float(((cvssV2_BASE_severity_medium_iot_availabilityImpact_NONE*100)/cvssV2_BASE_severity_medium_iot)))+" % DE  VULNERABILIDADES NO SE PRODUCE IMPACTO DE CONFIDENCIALIDAD ")
    print("\n")
    print("\n")  


if(cvssV2_BASE_severity_low_iot>0):
    print("      -    EN EL "+str(float(((cvssV2_BASE_severity_low_iot*100)/len(cves))))+" % DE  VULNERABILIDADES LA SEVERIDAD ES BAJA. LOS PORCENTAJES DEL VECTOR CVSSV2 SON LOS SIGUIENTES:  \n")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV2_BASE_severity_low_iot_accessvector_NETWORK*100)/cvssV2_BASE_severity_low_iot)))+" % DE  VULNERABILIDADES EL VECTOR DE ACCESO ES LA RED ")
    print("            -    EN EL "+str(float(((cvssV2_BASE_severity_low_iot_accessvector_LOCAL*100)/cvssV2_BASE_severity_low_iot)))+" % DE  VULNERABILIDADES EL VECTOR DE ACCESO ES LOCAL ")
    print("            -    EN EL "+str(float(((cvssV2_BASE_severity_low_iot_accessvector_ADJACENT_NETWORK*100)/cvssV2_BASE_severity_low_iot)))+" % DE  VULNERABILIDADES EL VECTOR DE ACCESO ES UNA RED ADYACENTE ")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV2_BASE_severity_low_iot_accesscomplexity_HIGH*100)/cvssV2_BASE_severity_low_iot)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES ALTA ")
    print("            -    EN EL "+str(float(((cvssV2_BASE_severity_low_iot_accesscomplexity_LOW*100)/cvssV2_BASE_severity_low_iot)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES BAJA ")
    print("            -    EN EL "+str(float(((cvssV2_BASE_severity_low_iot_accesscomplexity_MEDIUM*100)/cvssV2_BASE_severity_low_iot)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES MEDIA ")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV2_BASE_severity_low_iot_authentication_SINGLE*100)/cvssV2_BASE_severity_low_iot)))+" % DE  VULNERABILIDADES LA AUTENTICACION ES SENCILLA ")
    print("            -    EN EL "+str(float(((cvssV2_BASE_severity_low_iot_authentication_MULTIPLE*100)/cvssV2_BASE_severity_low_iot)))+" % DE  VULNERABILIDADES LA AUTENTICACION ES MULTIPLE")
    print("            -    EN EL "+str(float(((cvssV2_BASE_severity_low_iot_authentication_NONE*100)/cvssV2_BASE_severity_low_iot)))+" % DE  VULNERABILIDADES NO SE REQUIERE NINGUNA AUTENTICACION DEL USUARIO")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV2_BASE_severity_low_iot_confidentialityImpact_COMPLETE*100)/cvssV2_BASE_severity_low_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES COMPLETO ")
    print("            -    EN EL "+str(float(((cvssV2_BASE_severity_low_iot_confidentialityImpact_PARTIAL*100)/cvssV2_BASE_severity_low_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES PARCIAL" )
    print("            -    EN EL "+str(float(((cvssV2_BASE_severity_low_iot_confidentialityImpact_NONE*100)/cvssV2_BASE_severity_low_iot)))+" % DE  VULNERABILIDADES NO SE PRODUCE IMPACTO DE CONFIDENCIALIDAD ")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV2_BASE_severity_low_iot_integrityImpact_COMPLETE*100)/cvssV2_BASE_severity_low_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES COMPLETO ")
    print("            -    EN EL "+str(float(((cvssV2_BASE_severity_low_iot_integrityImpact_PARTIAL*100)/cvssV2_BASE_severity_low_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES PARCIAL" )
    print("            -    EN EL "+str(float(((cvssV2_BASE_severity_low_iot_integrityImpact_NONE*100)/cvssV2_BASE_severity_low_iot)))+" % DE  VULNERABILIDADES NO SE PRODUCE IMPACTO DE CONFIDENCIALIDAD ")
    print("\n")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV2_BASE_severity_low_iot_availabilityImpact_COMPLETE*100)/cvssV2_BASE_severity_low_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES COMPLETO ")
    print("            -    EN EL "+str(float(((cvssV2_BASE_severity_low_iot_availabilityImpact_PARTIAL*100)/cvssV2_BASE_severity_low_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES PARCIAL" )
    print("            -    EN EL "+str(float(((cvssV2_BASE_severity_low_iot_availabilityImpact_NONE*100)/cvssV2_BASE_severity_low_iot)))+" % DE  VULNERABILIDADES NO SE PRODUCE IMPACTO DE CONFIDENCIALIDAD ")
    print("\n")
    print("\n") 


