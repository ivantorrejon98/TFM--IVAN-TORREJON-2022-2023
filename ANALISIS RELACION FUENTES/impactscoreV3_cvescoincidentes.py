import pandas as pd


df_cve_iot=pd.read_excel('cves_iot_2023.xlsx')
df_cve_sh=pd.read_excel('cves_smart_home_2023.xlsx')

cves=['CVE-2023-23379','CVE-2022-29859','CVE-2022-34326','CVE-2022-34021','CVE-2021-43702','CVE-2019-12266','CVE-2022-23265','CVE-2021-43573','CVE-2021-1441','CVE-2022-33005','CVE-2023-0847','CVE-2023-23575','CVE-2023-27389','CVE-2023-27917','CVE-2023-25017','CVE-2023-25018','CVE-2022-25075','CVE-2020-8105','CVE-2021-35395','CVE-2021-28372']




#Variables para almacenar el impacto de confidencialidad
cvssV3_IMPACT_score_CRITICAL_iot_confidentialityImpact_HIGH=0
cvssV3_IMPACT_score_CRITICAL_iot_confidentialityImpact_LOW=0
cvssV3_IMPACT_score_CRITICAL_iot_confidentialityImpact_NONE=0

#Variables para almacenar el impacto de integridad
cvssV3_IMPACT_score_CRITICAL_iot_integrityImpact_HIGH=0
cvssV3_IMPACT_score_CRITICAL_iot_integrityImpact_LOW=0
cvssV3_IMPACT_score_CRITICAL_iot_integrityImpact_NONE=0

#Variables para almacenar el impacto de disponibilidad
cvssV3_IMPACT_score_CRITICAL_iot_availabilityImpact_HIGH=0
cvssV3_IMPACT_score_CRITICAL_iot_availabilityImpact_LOW=0
cvssV3_IMPACT_score_CRITICAL_iot_availabilityImpact_NONE=0



#Variables para almacenar el impacto de confidencialidad
cvssV3_IMPACT_score_HIGH_iot_confidentialityImpact_HIGH=0
cvssV3_IMPACT_score_HIGH_iot_confidentialityImpact_LOW=0
cvssV3_IMPACT_score_HIGH_iot_confidentialityImpact_NONE=0

#Variables para almacenar el impacto de integridad
cvssV3_IMPACT_score_HIGH_iot_integrityImpact_HIGH=0
cvssV3_IMPACT_score_HIGH_iot_integrityImpact_LOW=0
cvssV3_IMPACT_score_HIGH_iot_integrityImpact_NONE=0

#Variables para almacenar el impacto de disponibilidad
cvssV3_IMPACT_score_HIGH_iot_availabilityImpact_HIGH=0
cvssV3_IMPACT_score_HIGH_iot_availabilityImpact_LOW=0
cvssV3_IMPACT_score_HIGH_iot_availabilityImpact_NONE=0


#Variables para almacenar el impacto de confidencialidad
cvssV3_IMPACT_score_MEDIUM_iot_confidentialityImpact_HIGH=0
cvssV3_IMPACT_score_MEDIUM_iot_confidentialityImpact_LOW=0
cvssV3_IMPACT_score_MEDIUM_iot_confidentialityImpact_NONE=0

#Variables para almacenar el impacto de integridad
cvssV3_IMPACT_score_MEDIUM_iot_integrityImpact_HIGH=0
cvssV3_IMPACT_score_MEDIUM_iot_integrityImpact_LOW=0
cvssV3_IMPACT_score_MEDIUM_iot_integrityImpact_NONE=0

#Variables para almacenar el impacto de disponibilidad
cvssV3_IMPACT_score_MEDIUM_iot_availabilityImpact_HIGH=0
cvssV3_IMPACT_score_MEDIUM_iot_availabilityImpact_LOW=0
cvssV3_IMPACT_score_MEDIUM_iot_availabilityImpact_NONE=0


#Variables para almacenar el impacto de confidencialidad
cvssV3_IMPACT_score_LOW_iot_confidentialityImpact_HIGH=0
cvssV3_IMPACT_score_LOW_iot_confidentialityImpact_LOW=0
cvssV3_IMPACT_score_LOW_iot_confidentialityImpact_NONE=0

#Variables para almacenar el impacto de integridad
cvssV3_IMPACT_score_LOW_iot_integrityImpact_HIGH=0
cvssV3_IMPACT_score_LOW_iot_integrityImpact_LOW=0
cvssV3_IMPACT_score_LOW_iot_integrityImpact_NONE=0

#Variables para almacenar el impacto de disponibilidad
cvssV3_IMPACT_score_LOW_iot_availabilityImpact_HIGH=0
cvssV3_IMPACT_score_LOW_iot_availabilityImpact_LOW=0
cvssV3_IMPACT_score_LOW_iot_availabilityImpact_NONE=0

#Variables para almacenar el nivel de puntuacion de impacto
cvssV3_IMPACT_score_CRITICAL_iot=0
cvssV3_IMPACT_score_HIGH_iot=0
cvssV3_IMPACT_score_MEDIUM_iot=0
cvssV3_IMPACT_score_LOW_iot=0

#Recorro las distintas filas del fichero
for j in range(0,len(df_cve_iot["CVE_Items.impact.baseMetricV3.impactScore"])):
	if((df_cve_iot["CVE_Items.cve.CVE_data_meta.ID"][j].replace('[','').replace(']','').replace("'","").replace("","").replace(" ","")) in cves):
		if(df_cve_iot["CVE_Items.impact.baseMetricV3.impactScore"][j] !='NONE'):
			#Compruebo nivel de puntuacion de impacto
			if(((float(df_cve_iot["CVE_Items.impact.baseMetricV3.impactScore"][j])) <= 10.0) and ((float(df_cve_iot["CVE_Items.impact.baseMetricV3.impactScore"][j])) >=9.0)):
				cvssV3_IMPACT_score_CRITICAL_iot+=1
				#Compruebo impacto de confidencialidad
				if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.confidentialityImpact"][j]=='HIGH'):
					cvssV3_IMPACT_score_CRITICAL_iot_confidentialityImpact_HIGH+=1
				elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.confidentialityImpact"][j]=='LOW'):
					cvssV3_IMPACT_score_CRITICAL_iot_confidentialityImpact_LOW+=1
				else:
					cvssV3_IMPACT_score_CRITICAL_iot_confidentialityImpact_NONE+=1 

				#Compruebo impacto de integridad
				if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"][j]=='HIGH'):
					cvssV3_IMPACT_score_CRITICAL_iot_integrityImpact_HIGH+=1
				elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"][j]=='LOW'):
					cvssV3_IMPACT_score_CRITICAL_iot_integrityImpact_LOW+=1
				else:
					cvssV3_IMPACT_score_CRITICAL_iot_integrityImpact_NONE+=1    

				#Compruebo impacto de disponibilidad
				if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"][j]=='HIGH'):
					cvssV3_IMPACT_score_CRITICAL_iot_availabilityImpact_HIGH+=1
				elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"][j]=='LOW'):
					cvssV3_IMPACT_score_CRITICAL_iot_availabilityImpact_LOW+=1
				else:
					cvssV3_IMPACT_score_CRITICAL_iot_availabilityImpact_NONE+=1
					
			elif(((float(df_cve_iot["CVE_Items.impact.baseMetricV3.impactScore"][j])) < 9.0) and ((float(df_cve_iot["CVE_Items.impact.baseMetricV3.impactScore"][j])) >=7.0)):
				cvssV3_IMPACT_score_HIGH_iot+=1
				if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.confidentialityImpact"][j]=='HIGH'):
					cvssV3_IMPACT_score_HIGH_iot_confidentialityImpact_HIGH+=1
				elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.confidentialityImpact"][j]=='LOW'):
					cvssV3_IMPACT_score_HIGH_iot_confidentialityImpact_LOW+=1
				else:
					cvssV3_IMPACT_score_HIGH_iot_confidentialityImpact_NONE+=1 


				if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"][j]=='HIGH'):
					cvssV3_IMPACT_score_HIGH_iot_integrityImpact_HIGH+=1
				elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"][j]=='LOW'):
					cvssV3_IMPACT_score_HIGH_iot_integrityImpact_LOW+=1
				else:
					cvssV3_IMPACT_score_HIGH_iot_integrityImpact_NONE+=1    


				if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"][j]=='HIGH'):
					cvssV3_IMPACT_score_HIGH_iot_availabilityImpact_HIGH+=1
				elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"][j]=='LOW'):
					cvssV3_IMPACT_score_HIGH_iot_availabilityImpact_LOW+=1
				else:
					cvssV3_IMPACT_score_HIGH_iot_availabilityImpact_NONE+=1
			
			elif(((float(df_cve_iot["CVE_Items.impact.baseMetricV3.impactScore"][j])) < 7.0) and ((float(df_cve_iot["CVE_Items.impact.baseMetricV3.impactScore"][j])) >=4.0)):
				cvssV3_IMPACT_score_MEDIUM_iot+=1
				if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.confidentialityImpact"][j]=='HIGH'):
					cvssV3_IMPACT_score_MEDIUM_iot_confidentialityImpact_HIGH+=1
				elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.confidentialityImpact"][j]=='LOW'):
					cvssV3_IMPACT_score_MEDIUM_iot_confidentialityImpact_LOW+=1
				else:
					cvssV3_IMPACT_score_MEDIUM_iot_confidentialityImpact_NONE+=1 


				if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"][j]=='HIGH'):
					cvssV3_IMPACT_score_MEDIUM_iot_integrityImpact_HIGH+=1
				elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"][j]=='LOW'):
					cvssV3_IMPACT_score_MEDIUM_iot_integrityImpact_LOW+=1
				else:
					cvssV3_IMPACT_score_MEDIUM_iot_integrityImpact_NONE+=1    


				if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"][j]=='HIGH'):
					cvssV3_IMPACT_score_MEDIUM_iot_availabilityImpact_HIGH+=1
				elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"][j]=='LOW'):
					cvssV3_IMPACT_score_MEDIUM_iot_availabilityImpact_LOW+=1
				else:
					cvssV3_IMPACT_score_MEDIUM_iot_availabilityImpact_NONE+=1
					
			else:
				cvssV3_IMPACT_score_LOW_iot+=1
				if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.confidentialityImpact"][j]=='HIGH'):
					cvssV3_IMPACT_score_LOW_iot_confidentialityImpact_HIGH+=1
				elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.confidentialityImpact"][j]=='LOW'):
					cvssV3_IMPACT_score_LOW_iot_confidentialityImpact_LOW+=1
				else:
					cvssV3_IMPACT_score_LOW_iot_confidentialityImpact_NONE+=1 


				if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"][j]=='HIGH'):
					cvssV3_IMPACT_score_LOW_iot_integrityImpact_HIGH+=1
				elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"][j]=='LOW'):
					cvssV3_IMPACT_score_LOW_iot_integrityImpact_LOW+=1
				else:
					cvssV3_IMPACT_score_LOW_iot_integrityImpact_NONE+=1    


				if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"][j]=='HIGH'):
					cvssV3_IMPACT_score_LOW_iot_availabilityImpact_HIGH+=1
				elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"][j]=='LOW'):
					cvssV3_IMPACT_score_LOW_iot_availabilityImpact_LOW+=1
				else:
					cvssV3_IMPACT_score_LOW_iot_availabilityImpact_NONE+=1
					

print("\n")
print("\n")
print("*************************ESTADÍSTICAS RELACIÓN SEVERIDAD DE IMPACTO CON IMPACTO DE CONFIDENCIALIDAD/INTEGRIDAD/DISPONIBILIDAD SEGÚN VECTOR CVSSV3*************************")
print("\n")        
            
            
    
print("\n")
print(" DE UN TOTAL DE "+str(len(cves))+" VULNERABILIDADES , LAS ESTADISTICAS DE RELACIÓN DE SEVERIDAD DE IMPACTO CON IMPACTO DE CONFIDENCIALIDAD/INTEGRIDAD/DISPONIBILIDAD SEGÚN VECTOR CVSSV3 SON LAS SIGUIENTES:  \n")
print("\n")
print("      -    EN  "+str(cvssV3_IMPACT_score_CRITICAL_iot)+" VULNERABILIDADES LA SEVERIDAD DE IMPACTO ES CRITICA. LAS ESTADÍSTICAS DE IMPACTO SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(cvssV3_IMPACT_score_CRITICAL_iot_confidentialityImpact_HIGH)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO ")
print("            -    EN  "+str(cvssV3_IMPACT_score_CRITICAL_iot_confidentialityImpact_LOW)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO" )
print("            -    EN  "+str(cvssV3_IMPACT_score_CRITICAL_iot_confidentialityImpact_NONE)+" VULNERABILIDADES NO SE PRODUCE IMPACTO DE CONFIDENCIALIDAD ")
print("\n")
print("            -    EN  "+str(cvssV3_IMPACT_score_CRITICAL_iot_integrityImpact_HIGH)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO ")
print("            -    EN  "+str(cvssV3_IMPACT_score_CRITICAL_iot_integrityImpact_LOW)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO" )
print("            -    EN  "+str(cvssV3_IMPACT_score_CRITICAL_iot_integrityImpact_NONE)+" VULNERABILIDADES NO SE PRODUCE IMPACTO DE INTEGRIDAD ")
print("\n")
print("\n")
print("            -    EN  "+str(cvssV3_IMPACT_score_CRITICAL_iot_availabilityImpact_HIGH)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO ")
print("            -    EN  "+str(cvssV3_IMPACT_score_CRITICAL_iot_availabilityImpact_LOW)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO" )
print("            -    EN  "+str(cvssV3_IMPACT_score_CRITICAL_iot_availabilityImpact_NONE)+" VULNERABILIDADES NO SE PRODUCE IMPACTO DE DISPONIBILIDAD ")


print("      -    EN  "+str(cvssV3_IMPACT_score_HIGH_iot)+" VULNERABILIDADES LA SEVERIDAD DE IMPACTO ES ALTA. LAS ESTADÍSTICAS DE IMPACTO SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(cvssV3_IMPACT_score_HIGH_iot_confidentialityImpact_HIGH)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO ")
print("            -    EN  "+str(cvssV3_IMPACT_score_HIGH_iot_confidentialityImpact_LOW)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO" )
print("            -    EN  "+str(cvssV3_IMPACT_score_HIGH_iot_confidentialityImpact_NONE)+" VULNERABILIDADES NO SE PRODUCE IMPACTO DE CONFIDENCIALIDAD ")
print("\n")
print("            -    EN  "+str(cvssV3_IMPACT_score_HIGH_iot_integrityImpact_HIGH)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO ")
print("            -    EN  "+str(cvssV3_IMPACT_score_HIGH_iot_integrityImpact_LOW)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO" )
print("            -    EN  "+str(cvssV3_IMPACT_score_HIGH_iot_integrityImpact_NONE)+" VULNERABILIDADES NO SE PRODUCE IMPACTO DE INTEGRIDAD ")
print("\n")
print("\n")
print("            -    EN  "+str(cvssV3_IMPACT_score_HIGH_iot_availabilityImpact_HIGH)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO ")
print("            -    EN  "+str(cvssV3_IMPACT_score_HIGH_iot_availabilityImpact_LOW)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO" )
print("            -    EN  "+str(cvssV3_IMPACT_score_HIGH_iot_availabilityImpact_NONE)+" VULNERABILIDADES NO SE PRODUCE IMPACTO DE DISPONIBILIDAD ")


print("      -    EN  "+str(cvssV3_IMPACT_score_MEDIUM_iot)+" VULNERABILIDADES LA SEVERIDAD DE IMPACTO ES MEDIA. LAS ESTADÍSTICAS DE IMPACTO SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(cvssV3_IMPACT_score_MEDIUM_iot_confidentialityImpact_HIGH)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO ")
print("            -    EN  "+str(cvssV3_IMPACT_score_MEDIUM_iot_confidentialityImpact_LOW)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO" )
print("            -    EN  "+str(cvssV3_IMPACT_score_MEDIUM_iot_confidentialityImpact_NONE)+" VULNERABILIDADES NO SE PRODUCE IMPACTO DE CONFIDENCIALIDAD ")
print("\n")
print("            -    EN  "+str(cvssV3_IMPACT_score_MEDIUM_iot_integrityImpact_HIGH)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO ")
print("            -    EN  "+str(cvssV3_IMPACT_score_MEDIUM_iot_integrityImpact_LOW)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO" )
print("            -    EN  "+str(cvssV3_IMPACT_score_MEDIUM_iot_integrityImpact_NONE)+" VULNERABILIDADES NO SE PRODUCE IMPACTO DE INTEGRIDAD ")
print("\n")
print("\n")
print("            -    EN  "+str(cvssV3_IMPACT_score_MEDIUM_iot_availabilityImpact_HIGH)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO ")
print("            -    EN  "+str(cvssV3_IMPACT_score_MEDIUM_iot_availabilityImpact_LOW)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO" )
print("            -    EN  "+str(cvssV3_IMPACT_score_MEDIUM_iot_availabilityImpact_NONE)+" VULNERABILIDADES NO SE PRODUCE IMPACTO DE DISPONIBILIDAD ")


print("      -    EN  "+str(cvssV3_IMPACT_score_LOW_iot)+" VULNERABILIDADES LA SEVERIDAD DE IMPACTO ES BAJA. LAS ESTADÍSTICAS DE IMPACTO SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(cvssV3_IMPACT_score_LOW_iot_confidentialityImpact_HIGH)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO ")
print("            -    EN  "+str(cvssV3_IMPACT_score_LOW_iot_confidentialityImpact_LOW)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO" )
print("            -    EN  "+str(cvssV3_IMPACT_score_LOW_iot_confidentialityImpact_NONE)+" VULNERABILIDADES NO SE PRODUCE IMPACTO DE CONFIDENCIALIDAD ")
print("\n")
print("            -    EN  "+str(cvssV3_IMPACT_score_LOW_iot_integrityImpact_HIGH)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO ")
print("            -    EN  "+str(cvssV3_IMPACT_score_LOW_iot_integrityImpact_LOW)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO" )
print("            -    EN  "+str(cvssV3_IMPACT_score_LOW_iot_integrityImpact_NONE)+" VULNERABILIDADES NO SE PRODUCE IMPACTO DE INTEGRIDAD ")
print("\n")
print("\n")
print("            -    EN  "+str(cvssV3_IMPACT_score_LOW_iot_availabilityImpact_HIGH)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO ")
print("            -    EN  "+str(cvssV3_IMPACT_score_LOW_iot_availabilityImpact_LOW)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO" )
print("            -    EN  "+str(cvssV3_IMPACT_score_LOW_iot_availabilityImpact_NONE)+" VULNERABILIDADES NO SE PRODUCE IMPACTO DE DISPONIBILIDAD ")





print("\n")
print("\n")
print("*************************PORCENTAJES RELACIÓN SEVERIDAD DE IMPACTO CON IMPACTO DE CONFIDENCIALIDAD/INTEGRIDAD/DISPONIBILIDAD SEGÚN VECTOR CVSSV3*************************")
print("\n")        
            
            
    
print("\n")
print(" DE UN TOTAL DE "+str(len(cves))+" VULNERABILIDADES , LOS PORCENTAJES DE RELACIÓN DE SEVERIDAD DE IMPACTO CON IMPACTO DE CONFIDENCIALIDAD/INTEGRIDAD/DISPONIBILIDAD SEGÚN VECTOR CVSSV3 SON LOS SIGUIENTES:  \n")
print("\n")
if(cvssV3_IMPACT_score_CRITICAL_iot>0):
    print("      -    EN EL "+str(float(((cvssV3_IMPACT_score_CRITICAL_iot*100)/len(cves))))+" % DE  VULNERABILIDADES LA SEVERIDAD DE IMPACTO ES CRITICA. LOS PORCENTAJES DE RELACION DE IMPACT SCORE CON CONFIDENTIALITY/INTEGRITY/AVAILABILITY IMPACT SON LOS SIGUIENTES:  \n")
    print("\n")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV3_IMPACT_score_CRITICAL_iot_confidentialityImpact_HIGH*100)/cvssV3_IMPACT_score_CRITICAL_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO ")
    print("            -    EN EL "+str(float(((cvssV3_IMPACT_score_CRITICAL_iot_confidentialityImpact_LOW*100)/cvssV3_IMPACT_score_CRITICAL_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO" )
    print("            -    EN EL "+str(float(((cvssV3_IMPACT_score_CRITICAL_iot_confidentialityImpact_NONE*100)/cvssV3_IMPACT_score_CRITICAL_iot)))+" % DE  VULNERABILIDADES NO SE PRODUCE IMPACTO DE CONFIDENCIALIDAD ")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV3_IMPACT_score_CRITICAL_iot_integrityImpact_HIGH*100)/cvssV3_IMPACT_score_CRITICAL_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO ")
    print("            -    EN EL "+str(float(((cvssV3_IMPACT_score_CRITICAL_iot_integrityImpact_LOW*100)/cvssV3_IMPACT_score_CRITICAL_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO" )
    print("            -    EN EL "+str(float(((cvssV3_IMPACT_score_CRITICAL_iot_integrityImpact_NONE*100)/cvssV3_IMPACT_score_CRITICAL_iot)))+" % DE  VULNERABILIDADES NO SE PRODUCE IMPACTO DE INTEGRIDAD ")
    print("\n")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV3_IMPACT_score_CRITICAL_iot_availabilityImpact_HIGH*100)/cvssV3_IMPACT_score_CRITICAL_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO ")
    print("            -    EN EL "+str(float(((cvssV3_IMPACT_score_CRITICAL_iot_availabilityImpact_LOW*100)/cvssV3_IMPACT_score_CRITICAL_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO" )
    print("            -    EN EL "+str(float(((cvssV3_IMPACT_score_CRITICAL_iot_availabilityImpact_NONE*100)/cvssV3_IMPACT_score_CRITICAL_iot)))+" % DE  VULNERABILIDADES NO SE PRODUCE IMPACTO DE DISPONIBILIDAD ")
    print("\n")
    print("\n")       
    
    
    
if(cvssV3_IMPACT_score_HIGH_iot>0):
    print("      -    EN EL "+str(float(((cvssV3_IMPACT_score_HIGH_iot*100)/len(cves))))+" % DE  VULNERABILIDADES LA SEVERIDAD DE IMPACTO ES ALTA. LOS PORCENTAJES DE RELACION DE IMPACT SCORE CON CONFIDENTIALITY/INTEGRITY/AVAILABILITY IMPACT SON LOS SIGUIENTES:  \n")
    print("\n")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV3_IMPACT_score_HIGH_iot_confidentialityImpact_HIGH*100)/cvssV3_IMPACT_score_HIGH_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO ")
    print("            -    EN EL "+str(float(((cvssV3_IMPACT_score_HIGH_iot_confidentialityImpact_LOW*100)/cvssV3_IMPACT_score_HIGH_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO" )
    print("            -    EN EL "+str(float(((cvssV3_IMPACT_score_HIGH_iot_confidentialityImpact_NONE*100)/cvssV3_IMPACT_score_HIGH_iot)))+" % DE  VULNERABILIDADES NO SE PRODUCE IMPACTO DE CONFIDENCIALIDAD ")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV3_IMPACT_score_HIGH_iot_integrityImpact_HIGH*100)/cvssV3_IMPACT_score_HIGH_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO ")
    print("            -    EN EL "+str(float(((cvssV3_IMPACT_score_HIGH_iot_integrityImpact_LOW*100)/cvssV3_IMPACT_score_HIGH_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO" )
    print("            -    EN EL "+str(float(((cvssV3_IMPACT_score_HIGH_iot_integrityImpact_NONE*100)/cvssV3_IMPACT_score_HIGH_iot)))+" % DE  VULNERABILIDADES NO SE PRODUCE IMPACTO DE INTEGRIDAD ")
    print("\n")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV3_IMPACT_score_HIGH_iot_availabilityImpact_HIGH*100)/cvssV3_IMPACT_score_HIGH_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO ")
    print("            -    EN EL "+str(float(((cvssV3_IMPACT_score_HIGH_iot_availabilityImpact_LOW*100)/cvssV3_IMPACT_score_HIGH_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO" )
    print("            -    EN EL "+str(float(((cvssV3_IMPACT_score_HIGH_iot_availabilityImpact_NONE*100)/cvssV3_IMPACT_score_HIGH_iot)))+" % DE  VULNERABILIDADES NO SE PRODUCE IMPACTO DE DISPONIBILIDAD ")
    print("\n")
    print("\n")
    
if(cvssV3_IMPACT_score_MEDIUM_iot>0):
    print("      -    EN EL "+str(float(((cvssV3_IMPACT_score_MEDIUM_iot*100)/len(cves))))+" % DE  VULNERABILIDADES LA SEVERIDAD DE IMPACTO ES MEDIA. LOS PORCENTAJES DE RELACION DE IMPACT SCORE CON CONFIDENTIALITY/INTEGRITY/AVAILABILITY IMPACT SON LOS SIGUIENTES:  \n")
    print("\n")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV3_IMPACT_score_MEDIUM_iot_confidentialityImpact_HIGH*100)/cvssV3_IMPACT_score_MEDIUM_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO ")
    print("            -    EN EL "+str(float(((cvssV3_IMPACT_score_MEDIUM_iot_confidentialityImpact_LOW*100)/cvssV3_IMPACT_score_MEDIUM_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO" )
    print("            -    EN EL "+str(float(((cvssV3_IMPACT_score_MEDIUM_iot_confidentialityImpact_NONE*100)/cvssV3_IMPACT_score_MEDIUM_iot)))+" % DE  VULNERABILIDADES NO SE PRODUCE IMPACTO DE CONFIDENCIALIDAD ")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV3_IMPACT_score_MEDIUM_iot_integrityImpact_HIGH*100)/cvssV3_IMPACT_score_MEDIUM_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO ")
    print("            -    EN EL "+str(float(((cvssV3_IMPACT_score_MEDIUM_iot_integrityImpact_LOW*100)/cvssV3_IMPACT_score_MEDIUM_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO" )
    print("            -    EN EL "+str(float(((cvssV3_IMPACT_score_MEDIUM_iot_integrityImpact_NONE*100)/cvssV3_IMPACT_score_MEDIUM_iot)))+" % DE  VULNERABILIDADES NO SE PRODUCE IMPACTO DE INTEGRIDAD ")
    print("\n")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV3_IMPACT_score_MEDIUM_iot_availabilityImpact_HIGH*100)/cvssV3_IMPACT_score_MEDIUM_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO ")
    print("            -    EN EL "+str(float(((cvssV3_IMPACT_score_MEDIUM_iot_availabilityImpact_LOW*100)/cvssV3_IMPACT_score_MEDIUM_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO" )
    print("            -    EN EL "+str(float(((cvssV3_IMPACT_score_MEDIUM_iot_availabilityImpact_NONE*100)/cvssV3_IMPACT_score_MEDIUM_iot)))+" % DE  VULNERABILIDADES NO SE PRODUCE IMPACTO DE DISPONIBILIDAD ")
    print("\n")
    print("\n")
    
if(cvssV3_IMPACT_score_LOW_iot>0):
    print("      -    EN EL "+str(float(((cvssV3_IMPACT_score_LOW_iot*100)/len(cves))))+" % DE  VULNERABILIDADES LA SEVERIDAD DE IMPACTO ES BAJA. LOS PORCENTAJES DE RELACION DE IMPACT SCORE CON CONFIDENTIALITY/INTEGRITY/AVAILABILITY IMPACT SON LOS SIGUIENTES:  \n")
    print("\n")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV3_IMPACT_score_LOW_iot_confidentialityImpact_HIGH*100)/cvssV3_IMPACT_score_LOW_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO ")
    print("            -    EN EL "+str(float(((cvssV3_IMPACT_score_LOW_iot_confidentialityImpact_LOW*100)/cvssV3_IMPACT_score_LOW_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO" )
    print("            -    EN EL "+str(float(((cvssV3_IMPACT_score_LOW_iot_confidentialityImpact_NONE*100)/cvssV3_IMPACT_score_LOW_iot)))+" % DE  VULNERABILIDADES NO SE PRODUCE IMPACTO DE CONFIDENCIALIDAD ")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV3_IMPACT_score_LOW_iot_integrityImpact_HIGH*100)/cvssV3_IMPACT_score_LOW_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO ")
    print("            -    EN EL "+str(float(((cvssV3_IMPACT_score_LOW_iot_integrityImpact_LOW*100)/cvssV3_IMPACT_score_LOW_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO" )
    print("            -    EN EL "+str(float(((cvssV3_IMPACT_score_LOW_iot_integrityImpact_NONE*100)/cvssV3_IMPACT_score_LOW_iot)))+" % DE  VULNERABILIDADES NO SE PRODUCE IMPACTO DE INTEGRIDAD ")
    print("\n")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV3_IMPACT_score_LOW_iot_availabilityImpact_HIGH*100)/cvssV3_IMPACT_score_LOW_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO ")
    print("            -    EN EL "+str(float(((cvssV3_IMPACT_score_LOW_iot_availabilityImpact_LOW*100)/cvssV3_IMPACT_score_LOW_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO" )
    print("            -    EN EL "+str(float(((cvssV3_IMPACT_score_LOW_iot_availabilityImpact_NONE*100)/cvssV3_IMPACT_score_LOW_iot)))+" % DE  VULNERABILIDADES NO SE PRODUCE IMPACTO DE DISPONIBILIDAD ")
    print("\n")
    print("\n")
    
    

    
    
    