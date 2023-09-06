

import pandas as pd
from datetime import datetime,timedelta



#Abro los ficheros con los que voy a tratar




df_vulnibm_iot = pd.read_excel('vulnerabilidades_ibm_iot_2023.xlsx')
#Variable donde almacenare el contador de un valor determinado de enlace de referencia
count_vulnibm_iot_linktargetgithub=0
count_vulnibm_iot_linktargetcvemitre=0
count_vulnibm_iot_linktargetapple=0
count_vulnibm_iot_linktargetcisco=0
count_vulnibm_iot_linktargetsecuritysnyk=0
count_vulnibm_iot_linktargetintel=0
count_vulnibm_iot_linktargetcisagov=0
count_vulnibm_iot_linktargetmendio=0
count_vulnibm_iot_linktargetother=0

#Variable donde almacenare el contador de valores totales de enlace de referencia
counter_vulnibm_iot_linktargets=0
#Variable donde almacenare el contador de valores totales definidos de enlace de referencia
counter_vulnibm_iot_linktargets_defined=0

#Comprobamos el contenido de enlace de referencia
for r in range(0,len(df_vulnibm_iot["x_xfe_references_link_target"])):  
    #Si existen varios valores de enlace de referencia en una misma fila
    if('[' in df_vulnibm_iot["x_xfe_references_link_target"][r]):
            #Obtengo los valores de enlace de referencia para la fila actual
            aux=df_vulnibm_iot["x_xfe_references_link_target"][r].split(",")
            #Recorro los valores de enlace de referencia
            for k in range(0,len(aux)):
                if(len(aux)>0):
                    #Obtengo el valor actual de enlace de referencia y compruebo cual es
                    aux_str=aux[k].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
                    if('github' in aux_str):
                        counter_vulnibm_iot_linktargets+=1
                        counter_vulnibm_iot_linktargets_defined+=1
                        count_vulnibm_iot_linktargetgithub+=1
                    elif('cve.mitre' in aux_str):
                        counter_vulnibm_iot_linktargets+=1
                        counter_vulnibm_iot_linktargets_defined+=1
                        count_vulnibm_iot_linktargetcvemitre+=1
                    elif('apple' in aux_str):
                        counter_vulnibm_iot_linktargets+=1
                        counter_vulnibm_iot_linktargets_defined+=1
                        count_vulnibm_iot_linktargetapple+=1
                    elif('cisco' in aux_str):
                        counter_vulnibm_iot_linktargets+=1
                        counter_vulnibm_iot_linktargets_defined+=1
                        count_vulnibm_iot_linktargetcisco+=1
                    elif('security.snyk' in aux_str):
                        counter_vulnibm_iot_linktargets+=1
                        counter_vulnibm_iot_linktargets_defined+=1
                        count_vulnibm_iot_linktargetsecuritysnyk+=1
                    elif('intel' in aux_str):
                        counter_vulnibm_iot_linktargets+=1
                        counter_vulnibm_iot_linktargets_defined+=1
                        count_vulnibm_iot_linktargetintel+=1
                    elif('cisa.gov' in aux_str):
                        counter_vulnibm_iot_linktargets+=1
                        counter_vulnibm_iot_linktargets_defined+=1
                        count_vulnibm_iot_linktargetcisagov+=1
                    elif('mend.io' in aux_str):
                        counter_vulnibm_iot_linktargets+=1
                        counter_vulnibm_iot_linktargets_defined+=1
                        count_vulnibm_iot_linktargetmendio+=1
                    else:
                        counter_vulnibm_iot_linktargets+=1
                        count_vulnibm_iot_linktargetother+=1
    #Si existe un unico valor de enlace de referencia para la fila actual
    else:
        if('github' in df_vulnibm_iot["x_xfe_references_link_target"][r]):
            counter_vulnibm_iot_linktargets+=1
            counter_vulnibm_iot_linktargets_defined+=1
            count_vulnibm_iot_linktargetgithub+=1
        elif('cve.mitre' in df_vulnibm_iot["x_xfe_references_link_target"][r]):
            counter_vulnibm_iot_linktargets+=1
            counter_vulnibm_iot_linktargets_defined+=1
            count_vulnibm_iot_linktargetcvemitre+=1
        elif('apple' in df_vulnibm_iot["x_xfe_references_link_target"][r]):
            counter_vulnibm_iot_linktargets+=1
            counter_vulnibm_iot_linktargets_defined+=1
            count_vulnibm_iot_linktargetapple+=1
        elif('cisco' in df_vulnibm_iot["x_xfe_references_link_target"][r]):
            counter_vulnibm_iot_linktargets+=1
            counter_vulnibm_iot_linktargets_defined+=1
            count_vulnibm_iot_linktargetcisco+=1
        elif('security.snyk' in df_vulnibm_iot["x_xfe_references_link_target"][r]):
            counter_vulnibm_iot_linktargets+=1
            counter_vulnibm_iot_linktargets_defined+=1
            count_vulnibm_iot_linktargetsecuritysnyk+=1
        elif('intel' in df_vulnibm_iot["x_xfe_references_link_target"][r]):
            counter_vulnibm_iot_linktargets+=1
            counter_vulnibm_iot_linktargets_defined+=1
            count_vulnibm_iot_linktargetintel+=1
        elif('cisa.gov' in df_vulnibm_iot["x_xfe_references_link_target"][r]):
            counter_vulnibm_iot_linktargets+=1
            counter_vulnibm_iot_linktargets_defined+=1
            count_vulnibm_iot_linktargetcisagov+=1
        elif('mend.io' in df_vulnibm_iot["x_xfe_references_link_target"][r]):
            counter_vulnibm_iot_linktargets+=1
            counter_vulnibm_iot_linktargets_defined+=1
            count_vulnibm_iot_linktargetmendio+=1
        else:
            counter_vulnibm_iot_linktargets+=1
            count_vulnibm_iot_linktargetother+=1
        
        

print("*******************************************************ESTADÍSTICAS ENLACES DE REFERENCIAS VULNERABILIDADES IBM PARTE IOT*******************************************************")
print("\n")                            
                
print("\n")
print(" DE UN TOTAL DE "+str(counter_vulnibm_iot_linktargets)+" ENLACES DE REFERENCIAS , DEFINIMOS EL VALOR DE "+str(counter_vulnibm_iot_linktargets_defined)+" .LAS ESTADISTICAS DE ENLACES DE REFERENCIAS SON LAS SIGUIENTES:  \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_linktargetgithub)+" ENTRADAS EL ENLACE DE REFERENCIA ES GITHUB.COM  \n")
print("      -    EN  "+str(count_vulnibm_iot_linktargetcvemitre)+" ENTRADAS EL ENLACE DE REFERENCIA ES CVE.MITRE  \n")
print("      -    EN  "+str(count_vulnibm_iot_linktargetapple)+" ENTRADAS EL ENLACE DE REFERENCIA ES APPLE.COM  \n")
print("      -    EN  "+str(count_vulnibm_iot_linktargetcisco)+" ENTRADAS EL ENLACE DE REFERENCIA ES CISCO.COM  \n")
print("      -    EN  "+str(count_vulnibm_iot_linktargetsecuritysnyk)+" ENTRADAS EL ENLACE DE REFERENCIA ES SECURITY.SNYK  \n")
print("      -    EN  "+str(count_vulnibm_iot_linktargetintel)+" ENTRADAS EL ENLACE DE REFERENCIA ES INTEL.COM  \n")
print("      -    EN  "+str(count_vulnibm_iot_linktargetcisagov)+" ENTRADAS EL ENLACE DE REFERENCIA ES CISA.GOV  \n")
print("      -    EN  "+str(count_vulnibm_iot_linktargetmendio)+" ENTRADAS EL ENLACE DE REFERENCIA ES MEND.IO \n")
print("      -    EN  "+str(count_vulnibm_iot_linktargetother)+" ENTRADAS EL ENLACE DE REFERENCIA ES DISTINTO A LOS ANTERIORES  \n")
print("\n") 



print("*******************************************************PORCENTAJES ENLACES DE REFERENCIAS VULNERABILIDADES IBM PARTE IOT*******************************************************")
print("\n")                            
                
print("\n")
print(" DE UN TOTAL DE "+str(counter_vulnibm_iot_linktargets)+" VALORES DE ENLACE DE REFERENCIA, DEFINIMOS SU VALOR EN EL "+str((counter_vulnibm_iot_linktargets_defined*100)/(counter_vulnibm_iot_linktargets))+" % DE ELLAS . LOS PORCENTAJES DE ENLACE DE REFERENCIA SON LOS SIGUIENTES:\n") 
print("\n")
print("   - LOS PORCENTAJES DE ENLACE DE REFERENCIA SON LOS SIGUIENTES:  \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_linktargetgithub*100)/counter_vulnibm_iot_linktargets)))+" % DE ENTRADAS EL ENLACE DE REFERENCIA ES GITHUB.COM \n ")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_linktargetcvemitre*100)/counter_vulnibm_iot_linktargets)))+" % DE ENTRADAS EL ENLACE DE REFERENCIA ES CVE.MITRE \n ")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_linktargetapple*100)/counter_vulnibm_iot_linktargets)))+" % DE ENTRADAS EL ENLACE DE REFERENCIA ES APPLE.COM \n ")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_linktargetcisco*100)/counter_vulnibm_iot_linktargets)))+" % DE ENTRADAS EL ENLACE DE REFERENCIA ES CISCO.COM \n ")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_linktargetsecuritysnyk*100)/counter_vulnibm_iot_linktargets)))+" % DE ENTRADAS EL ENLACE DE REFERENCIA ES SECURITY.SNYK \n ")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_linktargetintel*100)/counter_vulnibm_iot_linktargets)))+" % DE ENTRADAS EL ENLACE DE REFERENCIA ES INTEL.COM \n ")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_linktargetcisagov*100)/counter_vulnibm_iot_linktargets)))+" % DE ENTRADAS EL ENLACE DE REFERENCIA ES CISA.GOV \n ")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_linktargetmendio*100)/counter_vulnibm_iot_linktargets)))+" % DE ENTRADAS EL ENLACE DE REFERENCIA ES MEND.IO \n ")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_linktargetother*100)/counter_vulnibm_iot_linktargets)))+" % DE ENTRADAS EL ENLACE DE REFERENCIA ES DISTINTO A LOS ANTERIORES \n ")



#Abro los ficheros con los que voy a tratar




df_vulnibm_sh = pd.read_excel('vulnerabilidades_ibm_smart_home_2023.xlsx')
#Variable donde almacenare el contador de un valor determinado de enlace de referencia
count_vulnibm_sh_linktargetgithub=0
count_vulnibm_sh_linktargetcvemitre=0
count_vulnibm_sh_linktargetadobe=0
count_vulnibm_sh_linktargetcisco=0
count_vulnibm_sh_linktargetsecuritysnyk=0
count_vulnibm_sh_linktargetnpmjs=0
count_vulnibm_sh_linktargetzerodayinitiative=0
count_vulnibm_sh_linktargetmicrosoft=0
count_vulnibm_sh_linktargetother=0

#Variable donde almacenare el contador de valores totales de enlace de referencia
counter_vulnibm_sh_linktargets=0
#Variable donde almacenare el contador de valores totales definidos de enlace de referencia
counter_vulnibm_sh_linktargets_defined=0
#Comprobamos el contenido de linktarget
for r in range(0,len(df_vulnibm_sh["x_xfe_references_link_target"])):  
    #Si existen varios valores de enlace de referencia en una misma fila
    if('[' in df_vulnibm_sh["x_xfe_references_link_target"][r]):
            #Obtengo los valores de enlace de referencia para la fila actual
            aux=df_vulnibm_sh["x_xfe_references_link_target"][r].split(",")
            #Recorro los valores
            for k in range(0,len(aux)):
                if(len(aux)>0):
                    #Obtengo el valor actual de enlace de referencia y compruebo cual es
                    aux_str=aux[k].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
                    if('github' in aux_str):
                        counter_vulnibm_sh_linktargets+=1
                        counter_vulnibm_sh_linktargets_defined+=1
                        count_vulnibm_sh_linktargetgithub+=1
                    elif('cve.mitre' in aux_str):
                        counter_vulnibm_sh_linktargets+=1
                        counter_vulnibm_sh_linktargets_defined+=1
                        count_vulnibm_sh_linktargetcvemitre+=1
                    elif('adobe' in aux_str):
                        counter_vulnibm_sh_linktargets+=1
                        counter_vulnibm_sh_linktargets_defined+=1
                        count_vulnibm_sh_linktargetadobe+=1
                    elif('cisco' in aux_str):
                        counter_vulnibm_sh_linktargets+=1
                        counter_vulnibm_sh_linktargets_defined+=1
                        count_vulnibm_sh_linktargetcisco+=1
                    elif('security.snyk' in aux_str):
                        counter_vulnibm_sh_linktargets+=1
                        counter_vulnibm_sh_linktargets_defined+=1
                        count_vulnibm_sh_linktargetsecuritysnyk+=1
                    elif('npmjs' in aux_str):
                        counter_vulnibm_sh_linktargets+=1
                        counter_vulnibm_sh_linktargets_defined+=1
                        count_vulnibm_sh_linktargetnpmjs+=1
                    elif('zerodayinitiative' in aux_str):
                        counter_vulnibm_sh_linktargets+=1
                        counter_vulnibm_sh_linktargets_defined+=1
                        count_vulnibm_sh_linktargetzerodayinitiative+=1
                    elif('microsoft' in aux_str):
                        counter_vulnibm_sh_linktargets+=1
                        counter_vulnibm_sh_linktargets_defined+=1
                        count_vulnibm_sh_linktargetmicrosoft+=1
                    else:
                        counter_vulnibm_sh_linktargets+=1
                        count_vulnibm_sh_linktargetother+=1
    #Si existe un unico valor de enlace de referencia para la fila actual
    else:
        if('github' in df_vulnibm_sh["x_xfe_references_link_target"][r]):
            counter_vulnibm_sh_linktargets+=1
            counter_vulnibm_sh_linktargets_defined+=1
            count_vulnibm_sh_linktargetgithub+=1
        elif('cve.mitre' in df_vulnibm_sh["x_xfe_references_link_target"][r]):
            counter_vulnibm_sh_linktargets+=1
            counter_vulnibm_sh_linktargets_defined+=1
            count_vulnibm_sh_linktargetcvemitre+=1
        elif('adobe' in df_vulnibm_sh["x_xfe_references_link_target"][r]):
            counter_vulnibm_sh_linktargets+=1
            counter_vulnibm_sh_linktargets_defined+=1
            count_vulnibm_sh_linktargetadobe+=1
        elif('cisco' in df_vulnibm_sh["x_xfe_references_link_target"][r]):
            counter_vulnibm_sh_linktargets+=1
            counter_vulnibm_sh_linktargets_defined+=1
            count_vulnibm_sh_linktargetcisco+=1
        elif('security.snyk' in df_vulnibm_sh["x_xfe_references_link_target"][r]):
            counter_vulnibm_sh_linktargets+=1
            counter_vulnibm_sh_linktargets_defined+=1
            count_vulnibm_sh_linktargetsecuritysnyk+=1
        elif('npmjs' in df_vulnibm_sh["x_xfe_references_link_target"][r]):
            counter_vulnibm_sh_linktargets+=1
            counter_vulnibm_sh_linktargets_defined+=1
            count_vulnibm_sh_linktargetnpmjs+=1
        elif('zerodayinitiative' in df_vulnibm_sh["x_xfe_references_link_target"][r]):
            counter_vulnibm_sh_linktargets+=1
            counter_vulnibm_sh_linktargets_defined+=1
            count_vulnibm_sh_linktargetzerodayinitiative+=1
        elif('microsoft' in df_vulnibm_sh["x_xfe_references_link_target"][r]):
            counter_vulnibm_sh_linktargets+=1
            counter_vulnibm_sh_linktargets_defined+=1
            count_vulnibm_sh_linktargetmicrosoft+=1
        else:
            counter_vulnibm_sh_linktargets+=1
            count_vulnibm_sh_linktargetother+=1
        
        

print("*******************************************************ESTADÍSTICAS ENLACES DE REFERENCIAS VULNERABILIDADES IBM PARTE SMART HOME*******************************************************")
print("\n")                            
                
print("\n")
print(" DE UN TOTAL DE "+str(counter_vulnibm_sh_linktargets)+" ENLACES DE REFERENCIAS , DEFINIMOS EL VALOR DE "+str(counter_vulnibm_sh_linktargets_defined)+" .LAS ESTADISTICAS DE ENLACES DE REFERENCIAS SON LAS SIGUIENTES:  \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_sh_linktargetgithub)+" ENTRADAS EL ENLACE DE REFERENCIA ES GITHUB.COM  \n")
print("      -    EN  "+str(count_vulnibm_sh_linktargetcvemitre)+" ENTRADAS EL ENLACE DE REFERENCIA ES CVE.MITRE  \n")
print("      -    EN  "+str(count_vulnibm_sh_linktargetadobe)+" ENTRADAS EL ENLACE DE REFERENCIA ES ADOBE.COM  \n")
print("      -    EN  "+str(count_vulnibm_sh_linktargetcisco)+" ENTRADAS EL ENLACE DE REFERENCIA ES CISCO.COM  \n")
print("      -    EN  "+str(count_vulnibm_sh_linktargetsecuritysnyk)+" ENTRADAS EL ENLACE DE REFERENCIA ES SECURITY.SNYK  \n")
print("      -    EN  "+str(count_vulnibm_sh_linktargetnpmjs)+" ENTRADAS EL ENLACE DE REFERENCIA ES NPMJS.COM  \n")
print("      -    EN  "+str(count_vulnibm_sh_linktargetzerodayinitiative)+" ENTRADAS EL ENLACE DE REFERENCIA ES ZERODAYINITIATIVE  \n")
print("      -    EN  "+str(count_vulnibm_sh_linktargetmicrosoft)+" ENTRADAS EL ENLACE DE REFERENCIA ES MICROSOFT.COM \n")
print("      -    EN  "+str(count_vulnibm_sh_linktargetother)+" ENTRADAS EL ENLACE DE REFERENCIA ES DISTINTO A LOS ANTERIORES  \n")
print("\n") 



print("*******************************************************PORCENTAJES ENLACES DE REFERENCIAS VULNERABILIDADES IBM PARTE SMART HOME*******************************************************")
print("\n")                            
                
print("\n")
print(" DE UN TOTAL DE "+str(counter_vulnibm_sh_linktargets)+" VALORES DE ENLACE DE REFERENCIA, DEFINIMOS SU VALOR EN EL "+str((counter_vulnibm_sh_linktargets_defined*100)/(counter_vulnibm_sh_linktargets))+" % DE ELLAS . LOS PORCENTAJES DE ENLACE DE REFERENCIA SON LOS SIGUIENTES:\n") 
print("\n")
print("   - LOS PORCENTAJES DE ENLACE DE REFERENCIA SON LOS SIGUIENTES:  \n")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_linktargetgithub*100)/counter_vulnibm_sh_linktargets)))+" % DE ENTRADAS EL ENLACE DE REFERENCIA ES GITHUB.COM \n ")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_linktargetcvemitre*100)/counter_vulnibm_sh_linktargets)))+" % DE ENTRADAS EL ENLACE DE REFERENCIA ES CVE.MITRE \n ")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_linktargetadobe*100)/counter_vulnibm_sh_linktargets)))+" % DE ENTRADAS EL ENLACE DE REFERENCIA ES ADOBE.COM \n ")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_linktargetcisco*100)/counter_vulnibm_sh_linktargets)))+" % DE ENTRADAS EL ENLACE DE REFERENCIA ES CISCO.COM \n ")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_linktargetsecuritysnyk*100)/counter_vulnibm_sh_linktargets)))+" % DE ENTRADAS EL ENLACE DE REFERENCIA ES SECURITY.SNYK \n ")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_linktargetnpmjs*100)/counter_vulnibm_sh_linktargets)))+" % DE ENTRADAS EL ENLACE DE REFERENCIA ES NPMJS.COM \n ")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_linktargetzerodayinitiative*100)/counter_vulnibm_sh_linktargets)))+" % DE ENTRADAS EL ENLACE DE REFERENCIA ES ZERODAYINITIATIVE \n ")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_linktargetmicrosoft*100)/counter_vulnibm_sh_linktargets)))+" % DE ENTRADAS EL ENLACE DE REFERENCIA ES MICROSOFT.COM \n ")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_linktargetother*100)/counter_vulnibm_sh_linktargets)))+" % DE ENTRADAS EL ENLACE DE REFERENCIA ES DISTINTO A LOS ANTERIORES \n ")




















