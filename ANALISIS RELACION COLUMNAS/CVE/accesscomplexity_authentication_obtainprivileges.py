
import pandas as pd

#Abro los ficheros con los que voy a tratar


df_cve_iot=pd.read_excel('cves_iot_2023.xlsx')
df_cve_sh=pd.read_excel('cves_smart_home_2023.xlsx')


#En las variables con esta nomenclatura almacenaré el contador de niveles de complejidad de acceso
high_accesscomplexity_iot=0

#En las variables con esta nomenclatura almacenaré el contador de valores en la relación del tipo de autenticación según complejidad
high_accesscomplexity_single_authentication_iot=0

#En las variables con esta nomenclatura almacenaré el contador de valores de la relación de complejidad de acceso y autenticación junto con la comprobación de la obtención de privilegios de todos/otros o usuarios
high_accesscomplexity_single_authentication_allprivilegetrue_iot=0
high_accesscomplexity_single_authentication_userprivilegetrue_iot=0
high_accesscomplexity_single_authentication_otherprivilegetrue_iot=0
high_accesscomplexity_single_authentication_allprivilegefalse_iot=0
high_accesscomplexity_single_authentication_userprivilegefalse_iot=0
high_accesscomplexity_single_authentication_otherprivilegefalse_iot=0

high_accesscomplexity_multiple_authentication_iot=0

high_accesscomplexity_multiple_authentication_allprivilegetrue_iot=0
high_accesscomplexity_multiple_authentication_userprivilegetrue_iot=0
high_accesscomplexity_multiple_authentication_otherprivilegetrue_iot=0
high_accesscomplexity_multiple_authentication_allprivilegefalse_iot=0
high_accesscomplexity_multiple_authentication_userprivilegefalse_iot=0
high_accesscomplexity_multiple_authentication_otherprivilegefalse_iot=0

high_accesscomplexity_none_authentication_iot=0

high_accesscomplexity_none_authentication_allprivilegetrue_iot=0
high_accesscomplexity_none_authentication_userprivilegetrue_iot=0
high_accesscomplexity_none_authentication_otherprivilegetrue_iot=0
high_accesscomplexity_none_authentication_allprivilegefalse_iot=0
high_accesscomplexity_none_authentication_userprivilegefalse_iot=0
high_accesscomplexity_none_authentication_otherprivilegefalse_iot=0



low_accesscomplexity_iot=0

low_accesscomplexity_single_authentication_iot=0

low_accesscomplexity_single_authentication_allprivilegetrue_iot=0
low_accesscomplexity_single_authentication_userprivilegetrue_iot=0
low_accesscomplexity_single_authentication_otherprivilegetrue_iot=0
low_accesscomplexity_single_authentication_allprivilegefalse_iot=0
low_accesscomplexity_single_authentication_userprivilegefalse_iot=0
low_accesscomplexity_single_authentication_otherprivilegefalse_iot=0

low_accesscomplexity_multiple_authentication_iot=0

low_accesscomplexity_multiple_authentication_allprivilegetrue_iot=0
low_accesscomplexity_multiple_authentication_userprivilegetrue_iot=0
low_accesscomplexity_multiple_authentication_otherprivilegetrue_iot=0
low_accesscomplexity_multiple_authentication_allprivilegefalse_iot=0
low_accesscomplexity_multiple_authentication_userprivilegefalse_iot=0
low_accesscomplexity_multiple_authentication_otherprivilegefalse_iot=0

low_accesscomplexity_none_authentication_iot=0

low_accesscomplexity_none_authentication_allprivilegetrue_iot=0
low_accesscomplexity_none_authentication_userprivilegetrue_iot=0
low_accesscomplexity_none_authentication_otherprivilegetrue_iot=0
low_accesscomplexity_none_authentication_allprivilegefalse_iot=0
low_accesscomplexity_none_authentication_userprivilegefalse_iot=0
low_accesscomplexity_none_authentication_otherprivilegefalse_iot=0



medium_accesscomplexity_iot=0

medium_accesscomplexity_single_authentication_iot=0

medium_accesscomplexity_single_authentication_allprivilegetrue_iot=0
medium_accesscomplexity_single_authentication_userprivilegetrue_iot=0
medium_accesscomplexity_single_authentication_otherprivilegetrue_iot=0
medium_accesscomplexity_single_authentication_allprivilegefalse_iot=0
medium_accesscomplexity_single_authentication_userprivilegefalse_iot=0
medium_accesscomplexity_single_authentication_otherprivilegefalse_iot=0

medium_accesscomplexity_multiple_authentication_iot=0

medium_accesscomplexity_multiple_authentication_allprivilegetrue_iot=0
medium_accesscomplexity_multiple_authentication_userprivilegetrue_iot=0
medium_accesscomplexity_multiple_authentication_otherprivilegetrue_iot=0
medium_accesscomplexity_multiple_authentication_allprivilegefalse_iot=0
medium_accesscomplexity_multiple_authentication_userprivilegefalse_iot=0
medium_accesscomplexity_multiple_authentication_otherprivilegefalse_iot=0

medium_accesscomplexity_none_authentication_iot=0

medium_accesscomplexity_none_authentication_allprivilegetrue_iot=0
medium_accesscomplexity_none_authentication_userprivilegetrue_iot=0
medium_accesscomplexity_none_authentication_otherprivilegetrue_iot=0
medium_accesscomplexity_none_authentication_allprivilegefalse_iot=0
medium_accesscomplexity_none_authentication_userprivilegefalse_iot=0
medium_accesscomplexity_none_authentication_otherprivilegefalse_iot=0

#Recorro los valores de complejidad de acceso
for j in range(0,len(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.accessComplexity"])):
    #Compruebo el valor de complejidad de acceso
    if(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.accessComplexity"][j]=='HIGH'):
        high_accesscomplexity_iot+=1
        #Compruebo el valor de authenticación
        if(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.authentication"][j]=="SINGLE"):
            high_accesscomplexity_single_authentication_iot+=1
            #Compruebo los privilegios que obtiene
            if(df_cve_iot["CVE_Items.impact.baseMetricV2.obtainOtherPrivilege"][j] is True):
                high_accesscomplexity_single_authentication_otherprivilegetrue_iot+=1
            elif(df_cve_iot["CVE_Items.impact.baseMetricV2.obtainOtherPrivilege"][j] is False):
                high_accesscomplexity_single_authentication_otherprivilegefalse_iot+=1
                
            if(df_cve_iot["CVE_Items.impact.baseMetricV2.obtainAllPrivilege"][j] is True):
                high_accesscomplexity_single_authentication_allprivilegetrue_iot+=1
            elif(df_cve_iot["CVE_Items.impact.baseMetricV2.obtainAllPrivilege"][j] is False):
                high_accesscomplexity_single_authentication_allprivilegefalse_iot+=1
                
            if(df_cve_iot["CVE_Items.impact.baseMetricV2.obtainUserPrivilege"][j] is True):
                high_accesscomplexity_single_authentication_userprivilegetrue_iot+=1
            elif(df_cve_iot["CVE_Items.impact.baseMetricV2.obtainUserPrivilege"][j] is False):
                high_accesscomplexity_single_authentication_userprivilegefalse_iot+=1   
                       
        elif(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.authentication"][j]=="MULTIPLE"):
            high_accesscomplexity_multiple_authentication_iot+=1
            
            if(df_cve_iot["CVE_Items.impact.baseMetricV2.obtainOtherPrivilege"][j] is True):
                high_accesscomplexity_multiple_authentication_otherprivilegetrue_iot+=1
            elif(df_cve_iot["CVE_Items.impact.baseMetricV2.obtainOtherPrivilege"][j] is False):
                high_accesscomplexity_multiple_authentication_otherprivilegefalse_iot+=1
                
            if(df_cve_iot["CVE_Items.impact.baseMetricV2.obtainAllPrivilege"][j] is True):
                high_accesscomplexity_multiple_authentication_allprivilegetrue_iot+=1
            elif(df_cve_iot["CVE_Items.impact.baseMetricV2.obtainAllPrivilege"][j] is False):
                high_accesscomplexity_multiple_authentication_allprivilegefalse_iot+=1
                
            if(df_cve_iot["CVE_Items.impact.baseMetricV2.obtainUserPrivilege"][j] is True):
                high_accesscomplexity_multiple_authentication_userprivilegetrue_iot+=1
            elif(df_cve_iot["CVE_Items.impact.baseMetricV2.obtainUserPrivilege"][j] is False):
                high_accesscomplexity_multiple_authentication_userprivilegefalse_iot+=1  
        else:
            high_accesscomplexity_none_authentication_iot+=1
            
            if(df_cve_iot["CVE_Items.impact.baseMetricV2.obtainOtherPrivilege"][j] is True):
                high_accesscomplexity_none_authentication_otherprivilegetrue_iot+=1
            elif(df_cve_iot["CVE_Items.impact.baseMetricV2.obtainOtherPrivilege"][j] is False):
                high_accesscomplexity_none_authentication_otherprivilegefalse_iot+=1
                
            if(df_cve_iot["CVE_Items.impact.baseMetricV2.obtainAllPrivilege"][j] is True):
                high_accesscomplexity_none_authentication_allprivilegetrue_iot+=1
            elif(df_cve_iot["CVE_Items.impact.baseMetricV2.obtainAllPrivilege"][j] is False):
                high_accesscomplexity_none_authentication_allprivilegefalse_iot+=1
                
            if(df_cve_iot["CVE_Items.impact.baseMetricV2.obtainUserPrivilege"][j] is True):
                high_accesscomplexity_none_authentication_userprivilegetrue_iot+=1
            elif(df_cve_iot["CVE_Items.impact.baseMetricV2.obtainUserPrivilege"][j] is False):
                high_accesscomplexity_none_authentication_userprivilegefalse_iot+=1  
            
            
            
    elif(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.accessComplexity"][j]=='LOW'):
        low_accesscomplexity_iot+=1
        
        if(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.authentication"][j]=="SINGLE"):
            low_accesscomplexity_single_authentication_iot+=1
            
            if(df_cve_iot["CVE_Items.impact.baseMetricV2.obtainOtherPrivilege"][j] is True):
                low_accesscomplexity_single_authentication_otherprivilegetrue_iot+=1
            elif(df_cve_iot["CVE_Items.impact.baseMetricV2.obtainOtherPrivilege"][j] is False):
                low_accesscomplexity_single_authentication_otherprivilegefalse_iot+=1
                
            if(df_cve_iot["CVE_Items.impact.baseMetricV2.obtainAllPrivilege"][j] is True):
                low_accesscomplexity_single_authentication_allprivilegetrue_iot+=1
            elif(df_cve_iot["CVE_Items.impact.baseMetricV2.obtainAllPrivilege"][j] is False):
                low_accesscomplexity_single_authentication_allprivilegefalse_iot+=1
                
            if(df_cve_iot["CVE_Items.impact.baseMetricV2.obtainUserPrivilege"][j] is True):
                low_accesscomplexity_single_authentication_userprivilegetrue_iot+=1
            elif(df_cve_iot["CVE_Items.impact.baseMetricV2.obtainUserPrivilege"][j] is False):
                low_accesscomplexity_single_authentication_userprivilegefalse_iot+=1   
                       
        elif(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.authentication"][j]=="MULTIPLE"):
            low_accesscomplexity_multiple_authentication_iot+=1
            
            if(df_cve_iot["CVE_Items.impact.baseMetricV2.obtainOtherPrivilege"][j] is True):
                low_accesscomplexity_multiple_authentication_otherprivilegetrue_iot+=1
            elif(df_cve_iot["CVE_Items.impact.baseMetricV2.obtainOtherPrivilege"][j] is False):
                low_accesscomplexity_multiple_authentication_otherprivilegefalse_iot+=1
                
            if(df_cve_iot["CVE_Items.impact.baseMetricV2.obtainAllPrivilege"][j] is True):
                low_accesscomplexity_multiple_authentication_allprivilegetrue_iot+=1
            elif(df_cve_iot["CVE_Items.impact.baseMetricV2.obtainAllPrivilege"][j] is False):
                low_accesscomplexity_multiple_authentication_allprivilegefalse_iot+=1
                
            if(df_cve_iot["CVE_Items.impact.baseMetricV2.obtainUserPrivilege"][j] is True):
                low_accesscomplexity_multiple_authentication_userprivilegetrue_iot+=1
            elif(df_cve_iot["CVE_Items.impact.baseMetricV2.obtainUserPrivilege"][j] is False):
                low_accesscomplexity_multiple_authentication_userprivilegefalse_iot+=1  
        else:
            low_accesscomplexity_none_authentication_iot+=1
            
            if(df_cve_iot["CVE_Items.impact.baseMetricV2.obtainOtherPrivilege"][j] is True):
                low_accesscomplexity_none_authentication_otherprivilegetrue_iot+=1
            elif(df_cve_iot["CVE_Items.impact.baseMetricV2.obtainOtherPrivilege"][j] is False):
                low_accesscomplexity_none_authentication_otherprivilegefalse_iot+=1
                
            if(df_cve_iot["CVE_Items.impact.baseMetricV2.obtainAllPrivilege"][j] is True):
                low_accesscomplexity_none_authentication_allprivilegetrue_iot+=1
            elif(df_cve_iot["CVE_Items.impact.baseMetricV2.obtainAllPrivilege"][j] is False):
                low_accesscomplexity_none_authentication_allprivilegefalse_iot+=1
                
            if(df_cve_iot["CVE_Items.impact.baseMetricV2.obtainUserPrivilege"][j] is True):
                low_accesscomplexity_none_authentication_userprivilegetrue_iot+=1
            elif(df_cve_iot["CVE_Items.impact.baseMetricV2.obtainUserPrivilege"][j] is False):
                low_accesscomplexity_none_authentication_userprivilegefalse_iot+=1  
                
    elif(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.accessComplexity"][j]=='MEDIUM'):
        medium_accesscomplexity_iot+=1
        
        
        if(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.authentication"][j]=="SINGLE"):
            medium_accesscomplexity_single_authentication_iot+=1
            
            if(df_cve_iot["CVE_Items.impact.baseMetricV2.obtainOtherPrivilege"][j] is True):
                medium_accesscomplexity_single_authentication_otherprivilegetrue_iot+=1
            elif(df_cve_iot["CVE_Items.impact.baseMetricV2.obtainOtherPrivilege"][j] is False):
                medium_accesscomplexity_single_authentication_otherprivilegefalse_iot+=1
                
            if(df_cve_iot["CVE_Items.impact.baseMetricV2.obtainAllPrivilege"][j] is True):
                medium_accesscomplexity_single_authentication_allprivilegetrue_iot+=1
            elif(df_cve_iot["CVE_Items.impact.baseMetricV2.obtainAllPrivilege"][j] is False):
                medium_accesscomplexity_single_authentication_allprivilegefalse_iot+=1
                
            if(df_cve_iot["CVE_Items.impact.baseMetricV2.obtainUserPrivilege"][j] is True):
                medium_accesscomplexity_single_authentication_userprivilegetrue_iot+=1
            elif(df_cve_iot["CVE_Items.impact.baseMetricV2.obtainUserPrivilege"][j] is False):
                medium_accesscomplexity_single_authentication_userprivilegefalse_iot+=1   
                       
        elif(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.authentication"][j]=="MULTIPLE"):
            medium_accesscomplexity_multiple_authentication_iot+=1
            
            if(df_cve_iot["CVE_Items.impact.baseMetricV2.obtainOtherPrivilege"][j] is True):
                medium_accesscomplexity_multiple_authentication_otherprivilegetrue_iot+=1
            elif(df_cve_iot["CVE_Items.impact.baseMetricV2.obtainOtherPrivilege"][j] is False):
                medium_accesscomplexity_multiple_authentication_otherprivilegefalse_iot+=1
                
            if(df_cve_iot["CVE_Items.impact.baseMetricV2.obtainAllPrivilege"][j] is True):
                medium_accesscomplexity_multiple_authentication_allprivilegetrue_iot+=1
            elif(df_cve_iot["CVE_Items.impact.baseMetricV2.obtainAllPrivilege"][j] is False):
                medium_accesscomplexity_multiple_authentication_allprivilegefalse_iot+=1
                
            if(df_cve_iot["CVE_Items.impact.baseMetricV2.obtainUserPrivilege"][j] is True):
                medium_accesscomplexity_multiple_authentication_userprivilegetrue_iot+=1
            elif(df_cve_iot["CVE_Items.impact.baseMetricV2.obtainUserPrivilege"][j] is False):
                medium_accesscomplexity_multiple_authentication_userprivilegefalse_iot+=1  
        else:
            medium_accesscomplexity_none_authentication_iot+=1
            
            if(df_cve_iot["CVE_Items.impact.baseMetricV2.obtainOtherPrivilege"][j] is True):
                medium_accesscomplexity_none_authentication_otherprivilegetrue_iot+=1
            elif(df_cve_iot["CVE_Items.impact.baseMetricV2.obtainOtherPrivilege"][j] is False):
                medium_accesscomplexity_none_authentication_otherprivilegefalse_iot+=1
                
            if(df_cve_iot["CVE_Items.impact.baseMetricV2.obtainAllPrivilege"][j] is True):
                medium_accesscomplexity_none_authentication_allprivilegetrue_iot+=1
            elif(df_cve_iot["CVE_Items.impact.baseMetricV2.obtainAllPrivilege"][j] is False):
                medium_accesscomplexity_none_authentication_allprivilegefalse_iot+=1
                
            if(df_cve_iot["CVE_Items.impact.baseMetricV2.obtainUserPrivilege"][j] is True):
                medium_accesscomplexity_none_authentication_userprivilegetrue_iot+=1
            elif(df_cve_iot["CVE_Items.impact.baseMetricV2.obtainUserPrivilege"][j] is False):
                medium_accesscomplexity_none_authentication_userprivilegefalse_iot+=1  
                
                
                
print("*************************************ESTADÍSTICAS COMPLEJIDAD DE ACCESO/AUTENTICACION-OBTENCION DE PRIVILEGIOS DE TODOS/OTROS/USUARIOS PARTE IOT*************************************")
print("\n")                 
                
print("\n")
print(" DE UN TOTAL DE "+str(len(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.accessComplexity"]))+" VULNERABILIDADES , LAS ESTADISTICAS DE COMPLEJIDAD DE ACCESO SON LAS SIGUIENTES:  \n")
print("\n")
print("      -    EN  "+str(high_accesscomplexity_iot)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES ALTA. LAS ESTADÍSTICAS DE AUTENTICACIÓN LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(high_accesscomplexity_single_authentication_iot)+" VULNERABILIDADES LA AUTENTICACIÓN ES SENCILLA. LAS ESTADÍSTICAS DE PRIVILEGIOS OBTENIDOS SON LAS SIGUIENTES: ")
print("                       -    EN  "+str(high_accesscomplexity_single_authentication_otherprivilegetrue_iot)+" VULNERABILIDADES SE OBTIENEN PRIVILEGIOS DISTINTOS A LOS DE USUARIO ")
print("                       -    EN  "+str(high_accesscomplexity_single_authentication_otherprivilegefalse_iot)+" VULNERABILIDADES NO SE OBTIENEN PRIVILEGIOS DISTINTOS A LOS DE USUARIO ")
print("\n")
print("                       -    EN  "+str(high_accesscomplexity_single_authentication_userprivilegetrue_iot)+" VULNERABILIDADES SE OBTIENEN LOS PRIVILEGIOS DE USUARIOS")
print("                       -    EN  "+str(high_accesscomplexity_single_authentication_userprivilegefalse_iot)+" VULNERABILIDADES NO SE OBTIENEN LOS PRIVILEGIOS DE USUARIOS ")
print("\n")
print("                       -    EN  "+str(high_accesscomplexity_single_authentication_allprivilegetrue_iot)+" VULNERABILIDADES SE OBTIENEN TODOS LOS PRIVILEGIOS")
print("                       -    EN  "+str(high_accesscomplexity_single_authentication_allprivilegefalse_iot)+" VULNERABILIDADES NO SE OBTIENEN TODOS LOS PRIVILEGIOS ")
print("\n")
print("            -    EN  "+str(high_accesscomplexity_multiple_authentication_iot)+" VULNERABILIDADES LA AUTENTICACIÓN ES MULTIPLE. LAS ESTADÍSTICAS DE PRIVILEGIOS OBTENIDOS SON LAS SIGUIENTES: ")
print("                       -    EN  "+str(high_accesscomplexity_multiple_authentication_otherprivilegetrue_iot)+" VULNERABILIDADES SE OBTIENEN PRIVILEGIOS DISTINTOS A LOS DE USUARIO ")
print("                       -    EN  "+str(high_accesscomplexity_multiple_authentication_otherprivilegefalse_iot)+" VULNERABILIDADES NO SE OBTIENEN PRIVILEGIOS DISTINTOS A LOS DE USUARIO ")
print("\n")
print("                       -    EN  "+str(high_accesscomplexity_multiple_authentication_userprivilegetrue_iot)+" VULNERABILIDADES SE OBTIENEN LOS PRIVILEGIOS DE USUARIOS")
print("                       -    EN  "+str(high_accesscomplexity_multiple_authentication_userprivilegefalse_iot)+" VULNERABILIDADES NO SE OBTIENEN LOS PRIVILEGIOS DE USUARIOS ")
print("\n")
print("                       -    EN  "+str(high_accesscomplexity_multiple_authentication_allprivilegetrue_iot)+" VULNERABILIDADES SE OBTIENEN TODOS LOS PRIVILEGIOS")
print("                       -    EN  "+str(high_accesscomplexity_multiple_authentication_allprivilegefalse_iot)+" VULNERABILIDADES NO SE OBTIENEN TODOS LOS PRIVILEGIOS ")
print("\n")
print("            -    EN  "+str(high_accesscomplexity_none_authentication_iot)+" VULNERABILIDADES NO SE REQUIERE AUTENTICACION. LAS ESTADÍSTICAS DE PRIVILEGIOS OBTENIDOS SON LAS SIGUIENTES: ")
print("                       -    EN  "+str(high_accesscomplexity_none_authentication_otherprivilegetrue_iot)+" VULNERABILIDADES SE OBTIENEN PRIVILEGIOS DISTINTOS A LOS DE USUARIO ")
print("                       -    EN  "+str(high_accesscomplexity_none_authentication_otherprivilegefalse_iot)+" VULNERABILIDADES NO SE OBTIENEN PRIVILEGIOS DISTINTOS A LOS DE USUARIO ")
print("\n")
print("                       -    EN  "+str(high_accesscomplexity_none_authentication_userprivilegetrue_iot)+" VULNERABILIDADES SE OBTIENEN LOS PRIVILEGIOS DE USUARIOS")
print("                       -    EN  "+str(high_accesscomplexity_none_authentication_userprivilegefalse_iot)+" VULNERABILIDADES NO SE OBTIENEN LOS PRIVILEGIOS DE USUARIOS ")
print("\n")
print("                       -    EN  "+str(high_accesscomplexity_none_authentication_allprivilegetrue_iot)+" VULNERABILIDADES SE OBTIENEN TODOS LOS PRIVILEGIOS")
print("                       -    EN  "+str(high_accesscomplexity_none_authentication_allprivilegefalse_iot)+" VULNERABILIDADES NO SE OBTIENEN TODOS LOS PRIVILEGIOS ")
print("\n")
print("\n")
print("      -    EN  "+str(low_accesscomplexity_iot)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES BAJA. LAS ESTADÍSTICAS DE AUTENTICACIÓN LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(low_accesscomplexity_single_authentication_iot)+" VULNERABILIDADES LA AUTENTICACIÓN ES SENCILLA. LAS ESTADÍSTICAS DE PRIVILEGIOS OBTENIDOS SON LAS SIGUIENTES: ")
print("                       -    EN  "+str(low_accesscomplexity_single_authentication_otherprivilegetrue_iot)+" VULNERABILIDADES SE OBTIENEN PRIVILEGIOS DISTINTOS A LOS DE USUARIO ")
print("                       -    EN  "+str(low_accesscomplexity_single_authentication_otherprivilegefalse_iot)+" VULNERABILIDADES NO SE OBTIENEN PRIVILEGIOS DISTINTOS A LOS DE USUARIO ")
print("\n")
print("                       -    EN  "+str(low_accesscomplexity_single_authentication_userprivilegetrue_iot)+" VULNERABILIDADES SE OBTIENEN LOS PRIVILEGIOS DE USUARIOS")
print("                       -    EN  "+str(low_accesscomplexity_single_authentication_userprivilegefalse_iot)+" VULNERABILIDADES NO SE OBTIENEN LOS PRIVILEGIOS DE USUARIOS ")
print("\n")
print("                       -    EN  "+str(low_accesscomplexity_single_authentication_allprivilegetrue_iot)+" VULNERABILIDADES SE OBTIENEN TODOS LOS PRIVILEGIOS")
print("                       -    EN  "+str(low_accesscomplexity_single_authentication_allprivilegefalse_iot)+" VULNERABILIDADES NO SE OBTIENEN TODOS LOS PRIVILEGIOS ")
print("\n")
print("            -    EN  "+str(low_accesscomplexity_multiple_authentication_iot)+" VULNERABILIDADES LA AUTENTICACIÓN ES MULTIPLE. LAS ESTADÍSTICAS DE PRIVILEGIOS OBTENIDOS SON LAS SIGUIENTES: ")
print("                       -    EN  "+str(low_accesscomplexity_multiple_authentication_otherprivilegetrue_iot)+" VULNERABILIDADES SE OBTIENEN PRIVILEGIOS DISTINTOS A LOS DE USUARIO ")
print("                       -    EN  "+str(low_accesscomplexity_multiple_authentication_otherprivilegefalse_iot)+" VULNERABILIDADES NO SE OBTIENEN PRIVILEGIOS DISTINTOS A LOS DE USUARIO ")
print("\n")
print("                       -    EN  "+str(low_accesscomplexity_multiple_authentication_userprivilegetrue_iot)+" VULNERABILIDADES SE OBTIENEN LOS PRIVILEGIOS DE USUARIOS")
print("                       -    EN  "+str(low_accesscomplexity_multiple_authentication_userprivilegefalse_iot)+" VULNERABILIDADES NO SE OBTIENEN LOS PRIVILEGIOS DE USUARIOS ")
print("\n")
print("                       -    EN  "+str(low_accesscomplexity_multiple_authentication_allprivilegetrue_iot)+" VULNERABILIDADES SE OBTIENEN TODOS LOS PRIVILEGIOS")
print("                       -    EN  "+str(low_accesscomplexity_multiple_authentication_allprivilegefalse_iot)+" VULNERABILIDADES NO SE OBTIENEN TODOS LOS PRIVILEGIOS ")
print("\n")
print("            -    EN  "+str(low_accesscomplexity_none_authentication_iot)+" VULNERABILIDADES NO SE REQUIERE AUTENTICACION. LAS ESTADÍSTICAS DE PRIVILEGIOS OBTENIDOS SON LAS SIGUIENTES: ")
print("                       -    EN  "+str(low_accesscomplexity_none_authentication_otherprivilegetrue_iot)+" VULNERABILIDADES SE OBTIENEN PRIVILEGIOS DISTINTOS A LOS DE USUARIO ")
print("                       -    EN  "+str(low_accesscomplexity_none_authentication_otherprivilegefalse_iot)+" VULNERABILIDADES NO SE OBTIENEN PRIVILEGIOS DISTINTOS A LOS DE USUARIO ")
print("\n")
print("                       -    EN  "+str(low_accesscomplexity_none_authentication_userprivilegetrue_iot)+" VULNERABILIDADES SE OBTIENEN LOS PRIVILEGIOS DE USUARIOS")
print("                       -    EN  "+str(low_accesscomplexity_none_authentication_userprivilegefalse_iot)+" VULNERABILIDADES NO SE OBTIENEN LOS PRIVILEGIOS DE USUARIOS ")
print("\n")
print("                       -    EN  "+str(low_accesscomplexity_none_authentication_allprivilegetrue_iot)+" VULNERABILIDADES SE OBTIENEN TODOS LOS PRIVILEGIOS")
print("                       -    EN  "+str(low_accesscomplexity_none_authentication_allprivilegefalse_iot)+" VULNERABILIDADES NO SE OBTIENEN TODOS LOS PRIVILEGIOS ")
print("\n")
print("      -    EN  "+str(medium_accesscomplexity_iot)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES MEDIA. LAS ESTADÍSTICAS DE AUTENTICACIÓN LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(medium_accesscomplexity_single_authentication_iot)+" VULNERABILIDADES LA AUTENTICACIÓN ES SENCILLA. LAS ESTADÍSTICAS DE PRIVILEGIOS OBTENIDOS SON LAS SIGUIENTES: ")
print("                       -    EN  "+str(medium_accesscomplexity_single_authentication_otherprivilegetrue_iot)+" VULNERABILIDADES SE OBTIENEN PRIVILEGIOS DISTINTOS A LOS DE USUARIO ")
print("                       -    EN  "+str(medium_accesscomplexity_single_authentication_otherprivilegefalse_iot)+" VULNERABILIDADES NO SE OBTIENEN PRIVILEGIOS DISTINTOS A LOS DE USUARIO ")
print("\n")
print("                       -    EN  "+str(medium_accesscomplexity_single_authentication_userprivilegetrue_iot)+" VULNERABILIDADES SE OBTIENEN LOS PRIVILEGIOS DE USUARIOS")
print("                       -    EN  "+str(medium_accesscomplexity_single_authentication_userprivilegefalse_iot)+" VULNERABILIDADES NO SE OBTIENEN LOS PRIVILEGIOS DE USUARIOS ")
print("\n")
print("                       -    EN  "+str(medium_accesscomplexity_single_authentication_allprivilegetrue_iot)+" VULNERABILIDADES SE OBTIENEN TODOS LOS PRIVILEGIOS")
print("                       -    EN  "+str(medium_accesscomplexity_single_authentication_allprivilegefalse_iot)+" VULNERABILIDADES NO SE OBTIENEN TODOS LOS PRIVILEGIOS ")
print("\n")
print("            -    EN  "+str(medium_accesscomplexity_multiple_authentication_iot)+" VULNERABILIDADES LA AUTENTICACIÓN ES MULTIPLE. LAS ESTADÍSTICAS DE PRIVILEGIOS OBTENIDOS SON LAS SIGUIENTES: ")
print("                       -    EN  "+str(medium_accesscomplexity_multiple_authentication_otherprivilegetrue_iot)+" VULNERABILIDADES SE OBTIENEN PRIVILEGIOS DISTINTOS A LOS DE USUARIO ")
print("                       -    EN  "+str(medium_accesscomplexity_multiple_authentication_otherprivilegefalse_iot)+" VULNERABILIDADES NO SE OBTIENEN PRIVILEGIOS DISTINTOS A LOS DE USUARIO ")
print("\n")
print("                       -    EN  "+str(medium_accesscomplexity_multiple_authentication_userprivilegetrue_iot)+" VULNERABILIDADES SE OBTIENEN LOS PRIVILEGIOS DE USUARIOS")
print("                       -    EN  "+str(medium_accesscomplexity_multiple_authentication_userprivilegefalse_iot)+" VULNERABILIDADES NO SE OBTIENEN LOS PRIVILEGIOS DE USUARIOS ")
print("\n")
print("                       -    EN  "+str(medium_accesscomplexity_multiple_authentication_allprivilegetrue_iot)+" VULNERABILIDADES SE OBTIENEN TODOS LOS PRIVILEGIOS")
print("                       -    EN  "+str(medium_accesscomplexity_multiple_authentication_allprivilegefalse_iot)+" VULNERABILIDADES NO SE OBTIENEN TODOS LOS PRIVILEGIOS ")
print("\n")
print("            -    EN  "+str(medium_accesscomplexity_none_authentication_iot)+" VULNERABILIDADES NO SE REQUIERE AUTENTICACION. LAS ESTADÍSTICAS DE PRIVILEGIOS OBTENIDOS SON LAS SIGUIENTES: ")
print("                       -    EN  "+str(medium_accesscomplexity_none_authentication_otherprivilegetrue_iot)+" VULNERABILIDADES SE OBTIENEN PRIVILEGIOS DISTINTOS A LOS DE USUARIO ")
print("                       -    EN  "+str(medium_accesscomplexity_none_authentication_otherprivilegefalse_iot)+" VULNERABILIDADES NO SE OBTIENEN PRIVILEGIOS DISTINTOS A LOS DE USUARIO ")
print("\n")
print("                       -    EN  "+str(medium_accesscomplexity_none_authentication_userprivilegetrue_iot)+" VULNERABILIDADES SE OBTIENEN LOS PRIVILEGIOS DE USUARIOS")
print("                       -    EN  "+str(medium_accesscomplexity_none_authentication_userprivilegefalse_iot)+" VULNERABILIDADES NO SE OBTIENEN LOS PRIVILEGIOS DE USUARIOS ")
print("\n")
print("                       -    EN  "+str(medium_accesscomplexity_none_authentication_allprivilegetrue_iot)+" VULNERABILIDADES SE OBTIENEN TODOS LOS PRIVILEGIOS")
print("                       -    EN  "+str(medium_accesscomplexity_none_authentication_allprivilegefalse_iot)+" VULNERABILIDADES NO SE OBTIENEN TODOS LOS PRIVILEGIOS ")
print("\n")
print("\n")










print("*************************************PORCENTAJES COMPLEJIDAD DE ACCESO/AUTENTICACION-OBTENCION DE PRIVILEGIOS DE TODOS/OTROS/USUARIOS  PARTE IOT*************************************")
print("\n")
print(" DE UN TOTAL DE "+str(len(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.accessComplexity"]))+" VULNERABILIDADES , LOS PORCENTAJES DE COMPLEJIDAD DE ACCESO SON LOS SIGUIENTES:  \n")
print("\n")
print("      -    EN  EL "+str(float(((high_accesscomplexity_iot*100)/len(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.accessComplexity"]))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES ALTA. LOS PORCENTAJES DE AUTENTICACIÓN SON LOS SIGUIENTES:  \n")
print("\n")
if(high_accesscomplexity_single_authentication_iot>0):
    print("            -    EN  EL "+str(float(((high_accesscomplexity_single_authentication_iot*100)/high_accesscomplexity_iot)))+" % DE VULNERABILIDADES LA AUTENTICACIÓN ES SENCILLA. LOS PORCENTAJES DE PRIVILEGIOS OBTENIDOS SON LOS SIGUIENTES: ")
    print("                       -    EN  EL "+str(float(((high_accesscomplexity_single_authentication_otherprivilegetrue_iot*100)/high_accesscomplexity_single_authentication_iot)))+" % DE VULNERABILIDADES SE OBTIENEN PRIVILEGIOS DISTINTOS A LOS DE USUARIO ")
    print("                       -    EN  EL "+str(float(((high_accesscomplexity_single_authentication_otherprivilegefalse_iot*100)/high_accesscomplexity_single_authentication_iot)))+" % DE VULNERABILIDADES NO SE OBTIENEN PRIVILEGIOS DISTINTOS A LOS DE USUARIO ")
    print("\n")
    print("                       -    EN  EL "+str(float(((high_accesscomplexity_single_authentication_userprivilegetrue_iot*100)/high_accesscomplexity_single_authentication_iot)))+" % DE VULNERABILIDADES SE OBTIENEN LOS PRIVILEGIOS DE USUARIOS")
    print("                       -    EN  EL "+str(float(((high_accesscomplexity_single_authentication_userprivilegefalse_iot*100)/high_accesscomplexity_single_authentication_iot)))+" % DE VULNERABILIDADES NO SE OBTIENEN LOS PRIVILEGIOS DE USUARIOS ")
    print("\n")
    print("                       -    EN  EL "+str(float(((high_accesscomplexity_single_authentication_allprivilegetrue_iot*100)/high_accesscomplexity_single_authentication_iot)))+" % DE VULNERABILIDADES SE OBTIENEN TODOS LOS PRIVILEGIOS")
    print("                       -    EN  EL "+str(float(((high_accesscomplexity_single_authentication_allprivilegefalse_iot*100)/high_accesscomplexity_single_authentication_iot)))+" % DE VULNERABILIDADES NO SE OBTIENEN TODOS LOS PRIVILEGIOS ")
    print("\n") 
if(high_accesscomplexity_multiple_authentication_iot>0):
    print("            -    EN  EL "+str(float(((high_accesscomplexity_multiple_authentication_iot*100)/high_accesscomplexity_iot)))+" % DE VULNERABILIDADES LA AUTENTICACIÓN ES MULTIPLE. LOS PORCENTAJES DE PRIVILEGIOS OBTENIDOS SON LOS SIGUIENTES: ")
    print("                       -    EN  EL "+str(float(((high_accesscomplexity_multiple_authentication_otherprivilegetrue_iot*100)/high_accesscomplexity_multiple_authentication_iot)))+" % DE VULNERABILIDADES SE OBTIENEN PRIVILEGIOS DISTINTOS A LOS DE USUARIO ")
    print("                       -    EN  EL "+str(float(((high_accesscomplexity_multiple_authentication_otherprivilegefalse_iot*100)/high_accesscomplexity_multiple_authentication_iot)))+" % DE VULNERABILIDADES NO SE OBTIENEN PRIVILEGIOS DISTINTOS A LOS DE USUARIO ")
    print("\n")
    print("                       -    EN  EL "+str(float(((high_accesscomplexity_multiple_authentication_userprivilegetrue_iot*100)/high_accesscomplexity_multiple_authentication_iot)))+" % DE VULNERABILIDADES SE OBTIENEN LOS PRIVILEGIOS DE USUARIOS")
    print("                       -    EN  EL "+str(float(((high_accesscomplexity_multiple_authentication_userprivilegefalse_iot*100)/high_accesscomplexity_multiple_authentication_iot)))+" % DE VULNERABILIDADES NO SE OBTIENEN LOS PRIVILEGIOS DE USUARIOS ")
    print("\n")
    print("                       -    EN  EL "+str(float(((high_accesscomplexity_multiple_authentication_allprivilegetrue_iot*100)/high_accesscomplexity_multiple_authentication_iot)))+" % DE VULNERABILIDADES SE OBTIENEN TODOS LOS PRIVILEGIOS")
    print("                       -    EN  EL "+str(float(((high_accesscomplexity_multiple_authentication_allprivilegefalse_iot*100)/high_accesscomplexity_multiple_authentication_iot)))+" % DE VULNERABILIDADES NO SE OBTIENEN TODOS LOS PRIVILEGIOS ")
    print("\n")
if(high_accesscomplexity_none_authentication_iot>0):
    print("            -    EN  EL "+str(float(((high_accesscomplexity_none_authentication_iot*100)/high_accesscomplexity_iot)))+" % DE VULNERABILIDADES NO SE REQUIERE AUTENTICACION. LOS PORCENTAJES DE PRIVILEGIOS OBTENIDOS SON LOS SIGUIENTES: ")
    print("                       -    EN  EL "+str(float(((high_accesscomplexity_none_authentication_otherprivilegetrue_iot*100)/high_accesscomplexity_none_authentication_iot)))+" % DE VULNERABILIDADES SE OBTIENEN PRIVILEGIOS DISTINTOS A LOS DE USUARIO ")
    print("                       -    EN  EL "+str(float(((high_accesscomplexity_none_authentication_otherprivilegefalse_iot*100)/high_accesscomplexity_none_authentication_iot)))+" % DE VULNERABILIDADES NO SE OBTIENEN PRIVILEGIOS DISTINTOS A LOS DE USUARIO ")
    print("\n")
    print("                       -    EN  EL "+str(float(((high_accesscomplexity_none_authentication_userprivilegetrue_iot*100)/high_accesscomplexity_none_authentication_iot)))+" % DE VULNERABILIDADES SE OBTIENEN LOS PRIVILEGIOS DE USUARIOS")
    print("                       -    EN  EL "+str(float(((high_accesscomplexity_none_authentication_userprivilegefalse_iot*100)/high_accesscomplexity_none_authentication_iot)))+" % DE VULNERABILIDADES NO SE OBTIENEN LOS PRIVILEGIOS DE USUARIOS ")
    print("\n")
    print("                       -    EN  EL "+str(float(((high_accesscomplexity_none_authentication_allprivilegetrue_iot*100)/high_accesscomplexity_none_authentication_iot)))+" % DE VULNERABILIDADES SE OBTIENEN TODOS LOS PRIVILEGIOS")
    print("                       -    EN  EL "+str(float(((high_accesscomplexity_none_authentication_allprivilegefalse_iot*100)/high_accesscomplexity_none_authentication_iot)))+" % DE VULNERABILIDADES NO SE OBTIENEN TODOS LOS PRIVILEGIOS ")
    print("\n") 
print("\n")
print("      -    EN  EL "+str(float(((low_accesscomplexity_iot*100)/len(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.accessComplexity"]))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES BAJA. LOS PORCENTAJES DE AUTENTICACIÓN SON LOS SIGUIENTES:  \n")
print("\n")
if(low_accesscomplexity_single_authentication_iot>0):
    print("            -    EN  EL "+str(float(((low_accesscomplexity_single_authentication_iot*100)/low_accesscomplexity_iot)))+" % DE VULNERABILIDADES LA AUTENTICACIÓN ES SENCILLA. LOS PORCENTAJES DE PRIVILEGIOS OBTENIDOS SON LOS SIGUIENTES: ")
    print("                       -    EN  EL "+str(float(((low_accesscomplexity_single_authentication_otherprivilegetrue_iot*100)/low_accesscomplexity_single_authentication_iot)))+" % DE VULNERABILIDADES SE OBTIENEN PRIVILEGIOS DISTINTOS A LOS DE USUARIO ")
    print("                       -    EN  EL "+str(float(((low_accesscomplexity_single_authentication_otherprivilegefalse_iot*100)/low_accesscomplexity_single_authentication_iot)))+" % DE VULNERABILIDADES NO SE OBTIENEN PRIVILEGIOS DISTINTOS A LOS DE USUARIO ")
    print("\n")
    print("                       -    EN  EL "+str(float(((low_accesscomplexity_single_authentication_userprivilegetrue_iot*100)/low_accesscomplexity_single_authentication_iot)))+" % DE VULNERABILIDADES SE OBTIENEN LOS PRIVILEGIOS DE USUARIOS")
    print("                       -    EN  EL "+str(float(((low_accesscomplexity_single_authentication_userprivilegefalse_iot*100)/low_accesscomplexity_single_authentication_iot)))+" % DE VULNERABILIDADES NO SE OBTIENEN LOS PRIVILEGIOS DE USUARIOS ")
    print("\n")
    print("                       -    EN  EL "+str(float(((low_accesscomplexity_single_authentication_allprivilegetrue_iot*100)/low_accesscomplexity_single_authentication_iot)))+" % DE VULNERABILIDADES SE OBTIENEN TODOS LOS PRIVILEGIOS")
    print("                       -    EN  EL "+str(float(((low_accesscomplexity_single_authentication_allprivilegefalse_iot*100)/low_accesscomplexity_single_authentication_iot)))+" % DE VULNERABILIDADES NO SE OBTIENEN TODOS LOS PRIVILEGIOS ")
    print("\n") 
if(low_accesscomplexity_multiple_authentication_iot>0):
    print("            -    EN  EL "+str(float(((low_accesscomplexity_multiple_authentication_iot*100)/low_accesscomplexity_iot)))+" % DE VULNERABILIDADES LA AUTENTICACIÓN ES MULTIPLE. LOS PORCENTAJES DE PRIVILEGIOS OBTENIDOS SON LOS SIGUIENTES: ")
    print("                       -    EN  EL "+str(float(((low_accesscomplexity_multiple_authentication_otherprivilegetrue_iot*100)/low_accesscomplexity_multiple_authentication_iot)))+" % DE VULNERABILIDADES SE OBTIENEN PRIVILEGIOS DISTINTOS A LOS DE USUARIO ")
    print("                       -    EN  EL "+str(float(((low_accesscomplexity_multiple_authentication_otherprivilegefalse_iot*100)/low_accesscomplexity_multiple_authentication_iot)))+" % DE VULNERABILIDADES NO SE OBTIENEN PRIVILEGIOS DISTINTOS A LOS DE USUARIO ")
    print("\n")
    print("                       -    EN  EL "+str(float(((low_accesscomplexity_multiple_authentication_userprivilegetrue_iot*100)/low_accesscomplexity_multiple_authentication_iot)))+" % DE VULNERABILIDADES SE OBTIENEN LOS PRIVILEGIOS DE USUARIOS")
    print("                       -    EN  EL "+str(float(((low_accesscomplexity_multiple_authentication_userprivilegefalse_iot*100)/low_accesscomplexity_multiple_authentication_iot)))+" % DE VULNERABILIDADES NO SE OBTIENEN LOS PRIVILEGIOS DE USUARIOS ")
    print("\n")
    print("                       -    EN  EL "+str(float(((low_accesscomplexity_multiple_authentication_allprivilegetrue_iot*100)/low_accesscomplexity_multiple_authentication_iot)))+" % DE VULNERABILIDADES SE OBTIENEN TODOS LOS PRIVILEGIOS")
    print("                       -    EN  EL "+str(float(((low_accesscomplexity_multiple_authentication_allprivilegefalse_iot*100)/low_accesscomplexity_multiple_authentication_iot)))+" % DE VULNERABILIDADES NO SE OBTIENEN TODOS LOS PRIVILEGIOS ")
    print("\n") 
if(low_accesscomplexity_none_authentication_iot>0):
    print("            -    EN  EL "+str(float(((low_accesscomplexity_none_authentication_iot*100)/low_accesscomplexity_iot)))+" % DE VULNERABILIDADES NO SE REQUIERE AUTENTICACION. LOS PORCENTAJES DE PRIVILEGIOS OBTENIDOS SON LOS SIGUIENTES: ")
    print("                       -    EN  EL "+str(float(((low_accesscomplexity_none_authentication_otherprivilegetrue_iot*100)/low_accesscomplexity_none_authentication_iot)))+" % DE VULNERABILIDADES SE OBTIENEN PRIVILEGIOS DISTINTOS A LOS DE USUARIO ")
    print("                       -    EN  EL "+str(float(((low_accesscomplexity_none_authentication_otherprivilegefalse_iot*100)/low_accesscomplexity_none_authentication_iot)))+" % DE VULNERABILIDADES NO SE OBTIENEN PRIVILEGIOS DISTINTOS A LOS DE USUARIO ")
    print("\n")
    print("                       -    EN  EL "+str(float(((low_accesscomplexity_none_authentication_userprivilegetrue_iot*100)/low_accesscomplexity_none_authentication_iot)))+" % DE VULNERABILIDADES SE OBTIENEN LOS PRIVILEGIOS DE USUARIOS")
    print("                       -    EN  EL "+str(float(((low_accesscomplexity_none_authentication_userprivilegefalse_iot*100)/low_accesscomplexity_none_authentication_iot)))+" % DE VULNERABILIDADES NO SE OBTIENEN LOS PRIVILEGIOS DE USUARIOS ")
    print("\n")
    print("                       -    EN  EL "+str(float(((low_accesscomplexity_none_authentication_allprivilegetrue_iot*100)/low_accesscomplexity_none_authentication_iot)))+" % DE VULNERABILIDADES SE OBTIENEN TODOS LOS PRIVILEGIOS")
    print("                       -    EN  EL "+str(float(((low_accesscomplexity_none_authentication_allprivilegefalse_iot*100)/low_accesscomplexity_none_authentication_iot)))+" % DE VULNERABILIDADES NO SE OBTIENEN TODOS LOS PRIVILEGIOS ")
    print("\n") 
print("\n")
print("      -    EN  EL "+str(float(((medium_accesscomplexity_iot*100)/len(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.accessComplexity"]))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES MEDIA. LOS PORCENTAJES DE AUTENTICACIÓN SON LOS SIGUIENTES:  \n")
print("\n")
if(medium_accesscomplexity_single_authentication_iot>0):
    print("            -    EN  EL "+str(float(((medium_accesscomplexity_single_authentication_iot*100)/medium_accesscomplexity_iot)))+" % DE VULNERABILIDADES LA AUTENTICACIÓN ES SENCILLA. LOS PORCENTAJES DE PRIVILEGIOS OBTENIDOS SON LOS SIGUIENTES: ")
    print("                       -    EN  EL "+str(float(((medium_accesscomplexity_single_authentication_otherprivilegetrue_iot*100)/medium_accesscomplexity_single_authentication_iot)))+" % DE VULNERABILIDADES SE OBTIENEN PRIVILEGIOS DISTINTOS A LOS DE USUARIO ")
    print("                       -    EN  EL "+str(float(((medium_accesscomplexity_single_authentication_otherprivilegefalse_iot*100)/medium_accesscomplexity_single_authentication_iot)))+" % DE VULNERABILIDADES NO SE OBTIENEN PRIVILEGIOS DISTINTOS A LOS DE USUARIO ")
    print("\n")
    print("                       -    EN  EL "+str(float(((medium_accesscomplexity_single_authentication_userprivilegetrue_iot*100)/medium_accesscomplexity_single_authentication_iot)))+" % DE VULNERABILIDADES SE OBTIENEN LOS PRIVILEGIOS DE USUARIOS")
    print("                       -    EN  EL "+str(float(((medium_accesscomplexity_single_authentication_userprivilegefalse_iot*100)/medium_accesscomplexity_single_authentication_iot)))+" % DE VULNERABILIDADES NO SE OBTIENEN LOS PRIVILEGIOS DE USUARIOS ")
    print("\n")
    print("                       -    EN  EL "+str(float(((medium_accesscomplexity_single_authentication_allprivilegetrue_iot*100)/medium_accesscomplexity_single_authentication_iot)))+" % DE VULNERABILIDADES SE OBTIENEN TODOS LOS PRIVILEGIOS")
    print("                       -    EN  EL "+str(float(((medium_accesscomplexity_single_authentication_allprivilegefalse_iot*100)/medium_accesscomplexity_single_authentication_iot)))+" % DE VULNERABILIDADES NO SE OBTIENEN TODOS LOS PRIVILEGIOS ")
    print("\n") 
if(medium_accesscomplexity_multiple_authentication_iot>0):
    print("            -    EN  EL "+str(float(((medium_accesscomplexity_multiple_authentication_iot*100)/medium_accesscomplexity_iot)))+" % DE VULNERABILIDADES LA AUTENTICACIÓN ES MULTIPLE. LOS PORCENTAJES DE PRIVILEGIOS OBTENIDOS SON LOS SIGUIENTES: ")
    print("                       -    EN  EL "+str(float(((medium_accesscomplexity_multiple_authentication_otherprivilegetrue_iot*100)/medium_accesscomplexity_multiple_authentication_iot)))+" % DE VULNERABILIDADES SE OBTIENEN PRIVILEGIOS DISTINTOS A LOS DE USUARIO ")
    print("                       -    EN  EL "+str(float(((medium_accesscomplexity_multiple_authentication_otherprivilegefalse_iot*100)/medium_accesscomplexity_multiple_authentication_iot)))+" % DE VULNERABILIDADES NO SE OBTIENEN PRIVILEGIOS DISTINTOS A LOS DE USUARIO ")
    print("\n")
    print("                       -    EN  EL "+str(float(((medium_accesscomplexity_multiple_authentication_userprivilegetrue_iot*100)/medium_accesscomplexity_multiple_authentication_iot)))+" % DE VULNERABILIDADES SE OBTIENEN LOS PRIVILEGIOS DE USUARIOS")
    print("                       -    EN  EL "+str(float(((medium_accesscomplexity_multiple_authentication_userprivilegefalse_iot*100)/medium_accesscomplexity_multiple_authentication_iot)))+" % DE VULNERABILIDADES NO SE OBTIENEN LOS PRIVILEGIOS DE USUARIOS ")
    print("\n")
    print("                       -    EN  EL "+str(float(((medium_accesscomplexity_multiple_authentication_allprivilegetrue_iot*100)/medium_accesscomplexity_multiple_authentication_iot)))+" % DE VULNERABILIDADES SE OBTIENEN TODOS LOS PRIVILEGIOS")
    print("                       -    EN  EL "+str(float(((medium_accesscomplexity_multiple_authentication_allprivilegefalse_iot*100)/medium_accesscomplexity_multiple_authentication_iot)))+" % DE VULNERABILIDADES NO SE OBTIENEN TODOS LOS PRIVILEGIOS ")
    print("\n")
if(medium_accesscomplexity_none_authentication_iot>0):
    print("            -    EN  EL "+str(float(((medium_accesscomplexity_none_authentication_iot*100)/medium_accesscomplexity_iot)))+" % DE VULNERABILIDADES NO SE REQUIERE AUTENTICACION. LOS PORCENTAJES DE PRIVILEGIOS OBTENIDOS SON LOS SIGUIENTES: ")
    print("                       -    EN  EL "+str(float(((medium_accesscomplexity_none_authentication_otherprivilegetrue_iot*100)/medium_accesscomplexity_none_authentication_iot)))+" % DE VULNERABILIDADES SE OBTIENEN PRIVILEGIOS DISTINTOS A LOS DE USUARIO ")
    print("                       -    EN  EL "+str(float(((medium_accesscomplexity_none_authentication_otherprivilegefalse_iot*100)/medium_accesscomplexity_none_authentication_iot)))+" % DE VULNERABILIDADES NO SE OBTIENEN PRIVILEGIOS DISTINTOS A LOS DE USUARIO ")
    print("\n")
    print("                       -    EN  EL "+str(float(((medium_accesscomplexity_none_authentication_userprivilegetrue_iot*100)/medium_accesscomplexity_none_authentication_iot)))+" % DE VULNERABILIDADES SE OBTIENEN LOS PRIVILEGIOS DE USUARIOS")
    print("                       -    EN  EL "+str(float(((medium_accesscomplexity_none_authentication_userprivilegefalse_iot*100)/medium_accesscomplexity_none_authentication_iot)))+" % DE VULNERABILIDADES NO SE OBTIENEN LOS PRIVILEGIOS DE USUARIOS ")
    print("\n")
    print("                       -    EN  EL "+str(float(((medium_accesscomplexity_none_authentication_allprivilegetrue_iot*100)/medium_accesscomplexity_none_authentication_iot)))+" % DE VULNERABILIDADES SE OBTIENEN TODOS LOS PRIVILEGIOS")
    print("                       -    EN  EL "+str(float(((medium_accesscomplexity_none_authentication_allprivilegefalse_iot*100)/medium_accesscomplexity_none_authentication_iot)))+" % DE VULNERABILIDADES NO SE OBTIENEN TODOS LOS PRIVILEGIOS ")
    print("\n") 





#En las variables con esta nomenclatura almacenaré el contador de niveles de complejidad de acceso
high_accesscomplexity_sh=0

#En las variables con esta nomenclatura almacenaré el contador de valores en la relación del tipo de autenticación según complejidad
high_accesscomplexity_single_authentication_sh=0

#En las variables con esta nomenclatura almacenaré el contador de valores de la relación de complejidad de acceso y autenticación junto con la comprobación de la obtención de privilegios de todos/otros o usuarios
high_accesscomplexity_single_authentication_allprivilegetrue_sh=0
high_accesscomplexity_single_authentication_userprivilegetrue_sh=0
high_accesscomplexity_single_authentication_otherprivilegetrue_sh=0
high_accesscomplexity_single_authentication_allprivilegefalse_sh=0
high_accesscomplexity_single_authentication_userprivilegefalse_sh=0
high_accesscomplexity_single_authentication_otherprivilegefalse_sh=0

high_accesscomplexity_multiple_authentication_sh=0

high_accesscomplexity_multiple_authentication_allprivilegetrue_sh=0
high_accesscomplexity_multiple_authentication_userprivilegetrue_sh=0
high_accesscomplexity_multiple_authentication_otherprivilegetrue_sh=0
high_accesscomplexity_multiple_authentication_allprivilegefalse_sh=0
high_accesscomplexity_multiple_authentication_userprivilegefalse_sh=0
high_accesscomplexity_multiple_authentication_otherprivilegefalse_sh=0

high_accesscomplexity_none_authentication_sh=0

high_accesscomplexity_none_authentication_allprivilegetrue_sh=0
high_accesscomplexity_none_authentication_userprivilegetrue_sh=0
high_accesscomplexity_none_authentication_otherprivilegetrue_sh=0
high_accesscomplexity_none_authentication_allprivilegefalse_sh=0
high_accesscomplexity_none_authentication_userprivilegefalse_sh=0
high_accesscomplexity_none_authentication_otherprivilegefalse_sh=0



low_accesscomplexity_sh=0

low_accesscomplexity_single_authentication_sh=0

low_accesscomplexity_single_authentication_allprivilegetrue_sh=0
low_accesscomplexity_single_authentication_userprivilegetrue_sh=0
low_accesscomplexity_single_authentication_otherprivilegetrue_sh=0
low_accesscomplexity_single_authentication_allprivilegefalse_sh=0
low_accesscomplexity_single_authentication_userprivilegefalse_sh=0
low_accesscomplexity_single_authentication_otherprivilegefalse_sh=0

low_accesscomplexity_multiple_authentication_sh=0

low_accesscomplexity_multiple_authentication_allprivilegetrue_sh=0
low_accesscomplexity_multiple_authentication_userprivilegetrue_sh=0
low_accesscomplexity_multiple_authentication_otherprivilegetrue_sh=0
low_accesscomplexity_multiple_authentication_allprivilegefalse_sh=0
low_accesscomplexity_multiple_authentication_userprivilegefalse_sh=0
low_accesscomplexity_multiple_authentication_otherprivilegefalse_sh=0

low_accesscomplexity_none_authentication_sh=0

low_accesscomplexity_none_authentication_allprivilegetrue_sh=0
low_accesscomplexity_none_authentication_userprivilegetrue_sh=0
low_accesscomplexity_none_authentication_otherprivilegetrue_sh=0
low_accesscomplexity_none_authentication_allprivilegefalse_sh=0
low_accesscomplexity_none_authentication_userprivilegefalse_sh=0
low_accesscomplexity_none_authentication_otherprivilegefalse_sh=0



medium_accesscomplexity_sh=0

medium_accesscomplexity_single_authentication_sh=0

medium_accesscomplexity_single_authentication_allprivilegetrue_sh=0
medium_accesscomplexity_single_authentication_userprivilegetrue_sh=0
medium_accesscomplexity_single_authentication_otherprivilegetrue_sh=0
medium_accesscomplexity_single_authentication_allprivilegefalse_sh=0
medium_accesscomplexity_single_authentication_userprivilegefalse_sh=0
medium_accesscomplexity_single_authentication_otherprivilegefalse_sh=0

medium_accesscomplexity_multiple_authentication_sh=0

medium_accesscomplexity_multiple_authentication_allprivilegetrue_sh=0
medium_accesscomplexity_multiple_authentication_userprivilegetrue_sh=0
medium_accesscomplexity_multiple_authentication_otherprivilegetrue_sh=0
medium_accesscomplexity_multiple_authentication_allprivilegefalse_sh=0
medium_accesscomplexity_multiple_authentication_userprivilegefalse_sh=0
medium_accesscomplexity_multiple_authentication_otherprivilegefalse_sh=0

medium_accesscomplexity_none_authentication_sh=0

medium_accesscomplexity_none_authentication_allprivilegetrue_sh=0
medium_accesscomplexity_none_authentication_userprivilegetrue_sh=0
medium_accesscomplexity_none_authentication_otherprivilegetrue_sh=0
medium_accesscomplexity_none_authentication_allprivilegefalse_sh=0
medium_accesscomplexity_none_authentication_userprivilegefalse_sh=0
medium_accesscomplexity_none_authentication_otherprivilegefalse_sh=0

#Recorro los valores de complejidad de acceso
for j in range(0,len(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.accessComplexity"])):
    #Compruebo el valor de complejidad de acceso
    if(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.accessComplexity"][j]=='HIGH'):
        high_accesscomplexity_sh+=1
        #Compruebo el valor de authenticación
        if(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.authentication"][j]=="SINGLE"):
            high_accesscomplexity_single_authentication_sh+=1
            #Compruebo los privilegios que obtiene
            if(df_cve_sh["CVE_Items.impact.baseMetricV2.obtainOtherPrivilege"][j] is True):
                high_accesscomplexity_single_authentication_otherprivilegetrue_sh+=1
            elif(df_cve_sh["CVE_Items.impact.baseMetricV2.obtainOtherPrivilege"][j] is False):
                high_accesscomplexity_single_authentication_otherprivilegefalse_sh+=1
                
            if(df_cve_sh["CVE_Items.impact.baseMetricV2.obtainAllPrivilege"][j] is True):
                high_accesscomplexity_single_authentication_allprivilegetrue_sh+=1
            elif(df_cve_sh["CVE_Items.impact.baseMetricV2.obtainAllPrivilege"][j] is False):
                high_accesscomplexity_single_authentication_allprivilegefalse_sh+=1
                
            if(df_cve_sh["CVE_Items.impact.baseMetricV2.obtainUserPrivilege"][j] is True):
                high_accesscomplexity_single_authentication_userprivilegetrue_sh+=1
            elif(df_cve_sh["CVE_Items.impact.baseMetricV2.obtainUserPrivilege"][j] is False):
                high_accesscomplexity_single_authentication_userprivilegefalse_sh+=1   
                       
        elif(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.authentication"][j]=="MULTIPLE"):
            high_accesscomplexity_multiple_authentication_sh+=1
            
            if(df_cve_sh["CVE_Items.impact.baseMetricV2.obtainOtherPrivilege"][j] is True):
                high_accesscomplexity_multiple_authentication_otherprivilegetrue_sh+=1
            elif(df_cve_sh["CVE_Items.impact.baseMetricV2.obtainOtherPrivilege"][j] is False):
                high_accesscomplexity_multiple_authentication_otherprivilegefalse_sh+=1
                
            if(df_cve_sh["CVE_Items.impact.baseMetricV2.obtainAllPrivilege"][j] is True):
                high_accesscomplexity_multiple_authentication_allprivilegetrue_sh+=1
            elif(df_cve_sh["CVE_Items.impact.baseMetricV2.obtainAllPrivilege"][j] is False):
                high_accesscomplexity_multiple_authentication_allprivilegefalse_sh+=1
                
            if(df_cve_sh["CVE_Items.impact.baseMetricV2.obtainUserPrivilege"][j] is True):
                high_accesscomplexity_multiple_authentication_userprivilegetrue_sh+=1
            elif(df_cve_sh["CVE_Items.impact.baseMetricV2.obtainUserPrivilege"][j] is False):
                high_accesscomplexity_multiple_authentication_userprivilegefalse_sh+=1  
        else:
            high_accesscomplexity_none_authentication_sh+=1
            
            if(df_cve_sh["CVE_Items.impact.baseMetricV2.obtainOtherPrivilege"][j] is True):
                high_accesscomplexity_none_authentication_otherprivilegetrue_sh+=1
            elif(df_cve_sh["CVE_Items.impact.baseMetricV2.obtainOtherPrivilege"][j] is False):
                high_accesscomplexity_none_authentication_otherprivilegefalse_sh+=1
                
            if(df_cve_sh["CVE_Items.impact.baseMetricV2.obtainAllPrivilege"][j] is True):
                high_accesscomplexity_none_authentication_allprivilegetrue_sh+=1
            elif(df_cve_sh["CVE_Items.impact.baseMetricV2.obtainAllPrivilege"][j] is False):
                high_accesscomplexity_none_authentication_allprivilegefalse_sh+=1
                
            if(df_cve_sh["CVE_Items.impact.baseMetricV2.obtainUserPrivilege"][j] is True):
                high_accesscomplexity_none_authentication_userprivilegetrue_sh+=1
            elif(df_cve_sh["CVE_Items.impact.baseMetricV2.obtainUserPrivilege"][j] is False):
                high_accesscomplexity_none_authentication_userprivilegefalse_sh+=1  
            
            
            
    elif(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.accessComplexity"][j]=='LOW'):
        low_accesscomplexity_sh+=1
        
        if(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.authentication"][j]=="SINGLE"):
            low_accesscomplexity_single_authentication_sh+=1
            
            if(df_cve_sh["CVE_Items.impact.baseMetricV2.obtainOtherPrivilege"][j] is True):
                low_accesscomplexity_single_authentication_otherprivilegetrue_sh+=1
            elif(df_cve_sh["CVE_Items.impact.baseMetricV2.obtainOtherPrivilege"][j] is False):
                low_accesscomplexity_single_authentication_otherprivilegefalse_sh+=1
                
            if(df_cve_sh["CVE_Items.impact.baseMetricV2.obtainAllPrivilege"][j] is True):
                low_accesscomplexity_single_authentication_allprivilegetrue_sh+=1
            elif(df_cve_sh["CVE_Items.impact.baseMetricV2.obtainAllPrivilege"][j] is False):
                low_accesscomplexity_single_authentication_allprivilegefalse_sh+=1
                
            if(df_cve_sh["CVE_Items.impact.baseMetricV2.obtainUserPrivilege"][j] is True):
                low_accesscomplexity_single_authentication_userprivilegetrue_sh+=1
            elif(df_cve_sh["CVE_Items.impact.baseMetricV2.obtainUserPrivilege"][j] is False):
                low_accesscomplexity_single_authentication_userprivilegefalse_sh+=1   
                       
        elif(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.authentication"][j]=="MULTIPLE"):
            low_accesscomplexity_multiple_authentication_sh+=1
            
            if(df_cve_sh["CVE_Items.impact.baseMetricV2.obtainOtherPrivilege"][j] is True):
                low_accesscomplexity_multiple_authentication_otherprivilegetrue_sh+=1
            elif(df_cve_sh["CVE_Items.impact.baseMetricV2.obtainOtherPrivilege"][j] is False):
                low_accesscomplexity_multiple_authentication_otherprivilegefalse_sh+=1
                
            if(df_cve_sh["CVE_Items.impact.baseMetricV2.obtainAllPrivilege"][j] is True):
                low_accesscomplexity_multiple_authentication_allprivilegetrue_sh+=1
            elif(df_cve_sh["CVE_Items.impact.baseMetricV2.obtainAllPrivilege"][j] is False):
                low_accesscomplexity_multiple_authentication_allprivilegefalse_sh+=1
                
            if(df_cve_sh["CVE_Items.impact.baseMetricV2.obtainUserPrivilege"][j] is True):
                low_accesscomplexity_multiple_authentication_userprivilegetrue_sh+=1
            elif(df_cve_sh["CVE_Items.impact.baseMetricV2.obtainUserPrivilege"][j] is False):
                low_accesscomplexity_multiple_authentication_userprivilegefalse_sh+=1  
        else:
            low_accesscomplexity_none_authentication_sh+=1
            
            if(df_cve_sh["CVE_Items.impact.baseMetricV2.obtainOtherPrivilege"][j] is True):
                low_accesscomplexity_none_authentication_otherprivilegetrue_sh+=1
            elif(df_cve_sh["CVE_Items.impact.baseMetricV2.obtainOtherPrivilege"][j] is False):
                low_accesscomplexity_none_authentication_otherprivilegefalse_sh+=1
                
            if(df_cve_sh["CVE_Items.impact.baseMetricV2.obtainAllPrivilege"][j] is True):
                low_accesscomplexity_none_authentication_allprivilegetrue_sh+=1
            elif(df_cve_sh["CVE_Items.impact.baseMetricV2.obtainAllPrivilege"][j] is False):
                low_accesscomplexity_none_authentication_allprivilegefalse_sh+=1
                
            if(df_cve_sh["CVE_Items.impact.baseMetricV2.obtainUserPrivilege"][j] is True):
                low_accesscomplexity_none_authentication_userprivilegetrue_sh+=1
            elif(df_cve_sh["CVE_Items.impact.baseMetricV2.obtainUserPrivilege"][j] is False):
                low_accesscomplexity_none_authentication_userprivilegefalse_sh+=1  
                
    elif(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.accessComplexity"][j]=='MEDIUM'):
        medium_accesscomplexity_sh+=1
        
        
        if(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.authentication"][j]=="SINGLE"):
            medium_accesscomplexity_single_authentication_sh+=1
            
            if(df_cve_sh["CVE_Items.impact.baseMetricV2.obtainOtherPrivilege"][j] is True):
                medium_accesscomplexity_single_authentication_otherprivilegetrue_sh+=1
            elif(df_cve_sh["CVE_Items.impact.baseMetricV2.obtainOtherPrivilege"][j] is False):
                medium_accesscomplexity_single_authentication_otherprivilegefalse_sh+=1
                
            if(df_cve_sh["CVE_Items.impact.baseMetricV2.obtainAllPrivilege"][j] is True):
                medium_accesscomplexity_single_authentication_allprivilegetrue_sh+=1
            elif(df_cve_sh["CVE_Items.impact.baseMetricV2.obtainAllPrivilege"][j] is False):
                medium_accesscomplexity_single_authentication_allprivilegefalse_sh+=1
                
            if(df_cve_sh["CVE_Items.impact.baseMetricV2.obtainUserPrivilege"][j] is True):
                medium_accesscomplexity_single_authentication_userprivilegetrue_sh+=1
            elif(df_cve_sh["CVE_Items.impact.baseMetricV2.obtainUserPrivilege"][j] is False):
                medium_accesscomplexity_single_authentication_userprivilegefalse_sh+=1   
                       
        elif(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.authentication"][j]=="MULTIPLE"):
            medium_accesscomplexity_multiple_authentication_sh+=1
            
            if(df_cve_sh["CVE_Items.impact.baseMetricV2.obtainOtherPrivilege"][j] is True):
                medium_accesscomplexity_multiple_authentication_otherprivilegetrue_sh+=1
            elif(df_cve_sh["CVE_Items.impact.baseMetricV2.obtainOtherPrivilege"][j] is False):
                medium_accesscomplexity_multiple_authentication_otherprivilegefalse_sh+=1
                
            if(df_cve_sh["CVE_Items.impact.baseMetricV2.obtainAllPrivilege"][j] is True):
                medium_accesscomplexity_multiple_authentication_allprivilegetrue_sh+=1
            elif(df_cve_sh["CVE_Items.impact.baseMetricV2.obtainAllPrivilege"][j] is False):
                medium_accesscomplexity_multiple_authentication_allprivilegefalse_sh+=1
                
            if(df_cve_sh["CVE_Items.impact.baseMetricV2.obtainUserPrivilege"][j] is True):
                medium_accesscomplexity_multiple_authentication_userprivilegetrue_sh+=1
            elif(df_cve_sh["CVE_Items.impact.baseMetricV2.obtainUserPrivilege"][j] is False):
                medium_accesscomplexity_multiple_authentication_userprivilegefalse_sh+=1  
        else:
            medium_accesscomplexity_none_authentication_sh+=1
            
            if(df_cve_sh["CVE_Items.impact.baseMetricV2.obtainOtherPrivilege"][j] is True):
                medium_accesscomplexity_none_authentication_otherprivilegetrue_sh+=1
            elif(df_cve_sh["CVE_Items.impact.baseMetricV2.obtainOtherPrivilege"][j] is False):
                medium_accesscomplexity_none_authentication_otherprivilegefalse_sh+=1
                
            if(df_cve_sh["CVE_Items.impact.baseMetricV2.obtainAllPrivilege"][j] is True):
                medium_accesscomplexity_none_authentication_allprivilegetrue_sh+=1
            elif(df_cve_sh["CVE_Items.impact.baseMetricV2.obtainAllPrivilege"][j] is False):
                medium_accesscomplexity_none_authentication_allprivilegefalse_sh+=1
                
            if(df_cve_sh["CVE_Items.impact.baseMetricV2.obtainUserPrivilege"][j] is True):
                medium_accesscomplexity_none_authentication_userprivilegetrue_sh+=1
            elif(df_cve_sh["CVE_Items.impact.baseMetricV2.obtainUserPrivilege"][j] is False):
                medium_accesscomplexity_none_authentication_userprivilegefalse_sh+=1  
                
                
                
print("************************************* ESTADÍSTICAS COMPLEJIDAD DE ACCESO/AUTENTICACION-OBTENCION DE PRIVILEGIOS DE TODOS/OTROS/USUARIOS PARTE SMART HOME*************************************")
print("\n")                 
                
print("\n")
print(" DE UN TOTAL DE "+str(len(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.accessComplexity"]))+" VULNERABILIDADES , LAS ESTADISTICAS DE COMPLEJIDAD DE ACCESO SON LAS SIGUIENTES:  \n")
print("\n")
print("      -    EN  "+str(high_accesscomplexity_sh)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES ALTA. LAS ESTADÍSTICAS DE AUTENTICACIÓN LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(high_accesscomplexity_single_authentication_sh)+" VULNERABILIDADES LA AUTENTICACIÓN ES SENCILLA. LAS ESTADÍSTICAS DE PRIVILEGIOS OBTENIDOS SON LAS SIGUIENTES: ")
print("                       -    EN  "+str(high_accesscomplexity_single_authentication_otherprivilegetrue_sh)+" VULNERABILIDADES SE OBTIENEN PRIVILEGIOS DISTINTOS A LOS DE USUARIO ")
print("                       -    EN  "+str(high_accesscomplexity_single_authentication_otherprivilegefalse_sh)+" VULNERABILIDADES NO SE OBTIENEN PRIVILEGIOS DISTINTOS A LOS DE USUARIO ")
print("\n")
print("                       -    EN  "+str(high_accesscomplexity_single_authentication_userprivilegetrue_sh)+" VULNERABILIDADES SE OBTIENEN LOS PRIVILEGIOS DE USUARIOS")
print("                       -    EN  "+str(high_accesscomplexity_single_authentication_userprivilegefalse_sh)+" VULNERABILIDADES NO SE OBTIENEN LOS PRIVILEGIOS DE USUARIOS ")
print("\n")
print("                       -    EN  "+str(high_accesscomplexity_single_authentication_allprivilegetrue_sh)+" VULNERABILIDADES SE OBTIENEN TODOS LOS PRIVILEGIOS")
print("                       -    EN  "+str(high_accesscomplexity_single_authentication_allprivilegefalse_sh)+" VULNERABILIDADES NO SE OBTIENEN TODOS LOS PRIVILEGIOS ")
print("\n")
print("            -    EN  "+str(high_accesscomplexity_multiple_authentication_sh)+" VULNERABILIDADES LA AUTENTICACIÓN ES MULTIPLE. LAS ESTADÍSTICAS DE PRIVILEGIOS OBTENIDOS SON LAS SIGUIENTES: ")
print("                       -    EN  "+str(high_accesscomplexity_multiple_authentication_otherprivilegetrue_sh)+" VULNERABILIDADES SE OBTIENEN PRIVILEGIOS DISTINTOS A LOS DE USUARIO ")
print("                       -    EN  "+str(high_accesscomplexity_multiple_authentication_otherprivilegefalse_sh)+" VULNERABILIDADES NO SE OBTIENEN PRIVILEGIOS DISTINTOS A LOS DE USUARIO ")
print("\n")
print("                       -    EN  "+str(high_accesscomplexity_multiple_authentication_userprivilegetrue_sh)+" VULNERABILIDADES SE OBTIENEN LOS PRIVILEGIOS DE USUARIOS")
print("                       -    EN  "+str(high_accesscomplexity_multiple_authentication_userprivilegefalse_sh)+" VULNERABILIDADES NO SE OBTIENEN LOS PRIVILEGIOS DE USUARIOS ")
print("\n")
print("                       -    EN  "+str(high_accesscomplexity_multiple_authentication_allprivilegetrue_sh)+" VULNERABILIDADES SE OBTIENEN TODOS LOS PRIVILEGIOS")
print("                       -    EN  "+str(high_accesscomplexity_multiple_authentication_allprivilegefalse_sh)+" VULNERABILIDADES NO SE OBTIENEN TODOS LOS PRIVILEGIOS ")
print("\n")
print("            -    EN  "+str(high_accesscomplexity_none_authentication_sh)+" VULNERABILIDADES NO SE REQUIERE AUTENTICACION. LAS ESTADÍSTICAS DE PRIVILEGIOS OBTENIDOS SON LAS SIGUIENTES: ")
print("                       -    EN  "+str(high_accesscomplexity_none_authentication_otherprivilegetrue_sh)+" VULNERABILIDADES SE OBTIENEN PRIVILEGIOS DISTINTOS A LOS DE USUARIO ")
print("                       -    EN  "+str(high_accesscomplexity_none_authentication_otherprivilegefalse_sh)+" VULNERABILIDADES NO SE OBTIENEN PRIVILEGIOS DISTINTOS A LOS DE USUARIO ")
print("\n")
print("                       -    EN  "+str(high_accesscomplexity_none_authentication_userprivilegetrue_sh)+" VULNERABILIDADES SE OBTIENEN LOS PRIVILEGIOS DE USUARIOS")
print("                       -    EN  "+str(high_accesscomplexity_none_authentication_userprivilegefalse_sh)+" VULNERABILIDADES NO SE OBTIENEN LOS PRIVILEGIOS DE USUARIOS ")
print("\n")
print("                       -    EN  "+str(high_accesscomplexity_none_authentication_allprivilegetrue_sh)+" VULNERABILIDADES SE OBTIENEN TODOS LOS PRIVILEGIOS")
print("                       -    EN  "+str(high_accesscomplexity_none_authentication_allprivilegefalse_sh)+" VULNERABILIDADES NO SE OBTIENEN TODOS LOS PRIVILEGIOS ")
print("\n")
print("\n")
print("      -    EN  "+str(low_accesscomplexity_sh)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES BAJA. LAS ESTADÍSTICAS DE AUTENTICACIÓN LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(low_accesscomplexity_single_authentication_sh)+" VULNERABILIDADES LA AUTENTICACIÓN ES SENCILLA. LAS ESTADÍSTICAS DE PRIVILEGIOS OBTENIDOS SON LAS SIGUIENTES: ")
print("                       -    EN  "+str(low_accesscomplexity_single_authentication_otherprivilegetrue_sh)+" VULNERABILIDADES SE OBTIENEN PRIVILEGIOS DISTINTOS A LOS DE USUARIO ")
print("                       -    EN  "+str(low_accesscomplexity_single_authentication_otherprivilegefalse_sh)+" VULNERABILIDADES NO SE OBTIENEN PRIVILEGIOS DISTINTOS A LOS DE USUARIO ")
print("\n")
print("                       -    EN  "+str(low_accesscomplexity_single_authentication_userprivilegetrue_sh)+" VULNERABILIDADES SE OBTIENEN LOS PRIVILEGIOS DE USUARIOS")
print("                       -    EN  "+str(low_accesscomplexity_single_authentication_userprivilegefalse_sh)+" VULNERABILIDADES NO SE OBTIENEN LOS PRIVILEGIOS DE USUARIOS ")
print("\n")
print("                       -    EN  "+str(low_accesscomplexity_single_authentication_allprivilegetrue_sh)+" VULNERABILIDADES SE OBTIENEN TODOS LOS PRIVILEGIOS")
print("                       -    EN  "+str(low_accesscomplexity_single_authentication_allprivilegefalse_sh)+" VULNERABILIDADES NO SE OBTIENEN TODOS LOS PRIVILEGIOS ")
print("\n")
print("            -    EN  "+str(low_accesscomplexity_multiple_authentication_sh)+" VULNERABILIDADES LA AUTENTICACIÓN ES MULTIPLE. LAS ESTADÍSTICAS DE PRIVILEGIOS OBTENIDOS SON LAS SIGUIENTES: ")
print("                       -    EN  "+str(low_accesscomplexity_multiple_authentication_otherprivilegetrue_sh)+" VULNERABILIDADES SE OBTIENEN PRIVILEGIOS DISTINTOS A LOS DE USUARIO ")
print("                       -    EN  "+str(low_accesscomplexity_multiple_authentication_otherprivilegefalse_sh)+" VULNERABILIDADES NO SE OBTIENEN PRIVILEGIOS DISTINTOS A LOS DE USUARIO ")
print("\n")
print("                       -    EN  "+str(low_accesscomplexity_multiple_authentication_userprivilegetrue_sh)+" VULNERABILIDADES SE OBTIENEN LOS PRIVILEGIOS DE USUARIOS")
print("                       -    EN  "+str(low_accesscomplexity_multiple_authentication_userprivilegefalse_sh)+" VULNERABILIDADES NO SE OBTIENEN LOS PRIVILEGIOS DE USUARIOS ")
print("\n")
print("                       -    EN  "+str(low_accesscomplexity_multiple_authentication_allprivilegetrue_sh)+" VULNERABILIDADES SE OBTIENEN TODOS LOS PRIVILEGIOS")
print("                       -    EN  "+str(low_accesscomplexity_multiple_authentication_allprivilegefalse_sh)+" VULNERABILIDADES NO SE OBTIENEN TODOS LOS PRIVILEGIOS ")
print("\n")
print("            -    EN  "+str(low_accesscomplexity_none_authentication_sh)+" VULNERABILIDADES NO SE REQUIERE AUTENTICACION. LAS ESTADÍSTICAS DE PRIVILEGIOS OBTENIDOS SON LAS SIGUIENTES: ")
print("                       -    EN  "+str(low_accesscomplexity_none_authentication_otherprivilegetrue_sh)+" VULNERABILIDADES SE OBTIENEN PRIVILEGIOS DISTINTOS A LOS DE USUARIO ")
print("                       -    EN  "+str(low_accesscomplexity_none_authentication_otherprivilegefalse_sh)+" VULNERABILIDADES NO SE OBTIENEN PRIVILEGIOS DISTINTOS A LOS DE USUARIO ")
print("\n")
print("                       -    EN  "+str(low_accesscomplexity_none_authentication_userprivilegetrue_sh)+" VULNERABILIDADES SE OBTIENEN LOS PRIVILEGIOS DE USUARIOS")
print("                       -    EN  "+str(low_accesscomplexity_none_authentication_userprivilegefalse_sh)+" VULNERABILIDADES NO SE OBTIENEN LOS PRIVILEGIOS DE USUARIOS ")
print("\n")
print("                       -    EN  "+str(low_accesscomplexity_none_authentication_allprivilegetrue_sh)+" VULNERABILIDADES SE OBTIENEN TODOS LOS PRIVILEGIOS")
print("                       -    EN  "+str(low_accesscomplexity_none_authentication_allprivilegefalse_sh)+" VULNERABILIDADES NO SE OBTIENEN TODOS LOS PRIVILEGIOS ")
print("\n")
print("      -    EN  "+str(medium_accesscomplexity_sh)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES MEDIA. LAS ESTADÍSTICAS DE AUTENTICACIÓN LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(medium_accesscomplexity_single_authentication_sh)+" VULNERABILIDADES LA AUTENTICACIÓN ES SENCILLA. LAS ESTADÍSTICAS DE PRIVILEGIOS OBTENIDOS SON LAS SIGUIENTES: ")
print("                       -    EN  "+str(medium_accesscomplexity_single_authentication_otherprivilegetrue_sh)+" VULNERABILIDADES SE OBTIENEN PRIVILEGIOS DISTINTOS A LOS DE USUARIO ")
print("                       -    EN  "+str(medium_accesscomplexity_single_authentication_otherprivilegefalse_sh)+" VULNERABILIDADES NO SE OBTIENEN PRIVILEGIOS DISTINTOS A LOS DE USUARIO ")
print("\n")
print("                       -    EN  "+str(medium_accesscomplexity_single_authentication_userprivilegetrue_sh)+" VULNERABILIDADES SE OBTIENEN LOS PRIVILEGIOS DE USUARIOS")
print("                       -    EN  "+str(medium_accesscomplexity_single_authentication_userprivilegefalse_sh)+" VULNERABILIDADES NO SE OBTIENEN LOS PRIVILEGIOS DE USUARIOS ")
print("\n")
print("                       -    EN  "+str(medium_accesscomplexity_single_authentication_allprivilegetrue_sh)+" VULNERABILIDADES SE OBTIENEN TODOS LOS PRIVILEGIOS")
print("                       -    EN  "+str(medium_accesscomplexity_single_authentication_allprivilegefalse_sh)+" VULNERABILIDADES NO SE OBTIENEN TODOS LOS PRIVILEGIOS ")
print("\n")
print("            -    EN  "+str(medium_accesscomplexity_multiple_authentication_sh)+" VULNERABILIDADES LA AUTENTICACIÓN ES MULTIPLE. LAS ESTADÍSTICAS DE PRIVILEGIOS OBTENIDOS SON LAS SIGUIENTES: ")
print("                       -    EN  "+str(medium_accesscomplexity_multiple_authentication_otherprivilegetrue_sh)+" VULNERABILIDADES SE OBTIENEN PRIVILEGIOS DISTINTOS A LOS DE USUARIO ")
print("                       -    EN  "+str(medium_accesscomplexity_multiple_authentication_otherprivilegefalse_sh)+" VULNERABILIDADES NO SE OBTIENEN PRIVILEGIOS DISTINTOS A LOS DE USUARIO ")
print("\n")
print("                       -    EN  "+str(medium_accesscomplexity_multiple_authentication_userprivilegetrue_sh)+" VULNERABILIDADES SE OBTIENEN LOS PRIVILEGIOS DE USUARIOS")
print("                       -    EN  "+str(medium_accesscomplexity_multiple_authentication_userprivilegefalse_sh)+" VULNERABILIDADES NO SE OBTIENEN LOS PRIVILEGIOS DE USUARIOS ")
print("\n")
print("                       -    EN  "+str(medium_accesscomplexity_multiple_authentication_allprivilegetrue_sh)+" VULNERABILIDADES SE OBTIENEN TODOS LOS PRIVILEGIOS")
print("                       -    EN  "+str(medium_accesscomplexity_multiple_authentication_allprivilegefalse_sh)+" VULNERABILIDADES NO SE OBTIENEN TODOS LOS PRIVILEGIOS ")
print("\n")
print("            -    EN  "+str(medium_accesscomplexity_none_authentication_sh)+" VULNERABILIDADES NO SE REQUIERE AUTENTICACION. LAS ESTADÍSTICAS DE PRIVILEGIOS OBTENIDOS SON LAS SIGUIENTES: ")
print("                       -    EN  "+str(medium_accesscomplexity_none_authentication_otherprivilegetrue_sh)+" VULNERABILIDADES SE OBTIENEN PRIVILEGIOS DISTINTOS A LOS DE USUARIO ")
print("                       -    EN  "+str(medium_accesscomplexity_none_authentication_otherprivilegefalse_sh)+" VULNERABILIDADES NO SE OBTIENEN PRIVILEGIOS DISTINTOS A LOS DE USUARIO ")
print("\n")
print("                       -    EN  "+str(medium_accesscomplexity_none_authentication_userprivilegetrue_sh)+" VULNERABILIDADES SE OBTIENEN LOS PRIVILEGIOS DE USUARIOS")
print("                       -    EN  "+str(medium_accesscomplexity_none_authentication_userprivilegefalse_sh)+" VULNERABILIDADES NO SE OBTIENEN LOS PRIVILEGIOS DE USUARIOS ")
print("\n")
print("                       -    EN  "+str(medium_accesscomplexity_none_authentication_allprivilegetrue_sh)+" VULNERABILIDADES SE OBTIENEN TODOS LOS PRIVILEGIOS")
print("                       -    EN  "+str(medium_accesscomplexity_none_authentication_allprivilegefalse_sh)+" VULNERABILIDADES NO SE OBTIENEN TODOS LOS PRIVILEGIOS ")
print("\n")
print("\n")










print("*************************************PORCENTAJES COMPLEJIDAD DE ACCESO/AUTENTICACION-OBTENCION DE PRIVILEGIOS DE TODOS/OTROS/USUARIOS PARTE SMART HOME*************************************")
print("\n")
print(" DE UN TOTAL DE "+str(len(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.accessComplexity"]))+" VULNERABILIDADES , LOS PORCENTAJES DE COMPLEJIDAD DE ACCESO SON LOS SIGUIENTES:  \n")
print("\n")
print("      -    EN  EL "+str(float(((high_accesscomplexity_sh*100)/len(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.accessComplexity"]))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES ALTA. LOS PORCENTAJES DE AUTENTICACIÓN SON LOS SIGUIENTES:  \n")
print("\n")
if(high_accesscomplexity_single_authentication_sh>0):
    print("            -    EN  EL "+str(float(((high_accesscomplexity_single_authentication_sh*100)/high_accesscomplexity_sh)))+" % DE VULNERABILIDADES LA AUTENTICACIÓN ES SENCILLA. LOS PORCENTAJES DE PRIVILEGIOS OBTENIDOS SON LOS SIGUIENTES: ")
    print("                       -    EN  EL "+str(float(((high_accesscomplexity_single_authentication_otherprivilegetrue_sh*100)/high_accesscomplexity_single_authentication_sh)))+" % DE VULNERABILIDADES SE OBTIENEN PRIVILEGIOS DISTINTOS A LOS DE USUARIO ")
    print("                       -    EN  EL "+str(float(((high_accesscomplexity_single_authentication_otherprivilegefalse_sh*100)/high_accesscomplexity_single_authentication_sh)))+" % DE VULNERABILIDADES NO SE OBTIENEN PRIVILEGIOS DISTINTOS A LOS DE USUARIO ")
    print("\n")
    print("                       -    EN  EL "+str(float(((high_accesscomplexity_single_authentication_userprivilegetrue_sh*100)/high_accesscomplexity_single_authentication_sh)))+" % DE VULNERABILIDADES SE OBTIENEN LOS PRIVILEGIOS DE USUARIOS")
    print("                       -    EN  EL "+str(float(((high_accesscomplexity_single_authentication_userprivilegefalse_sh*100)/high_accesscomplexity_single_authentication_sh)))+" % DE VULNERABILIDADES NO SE OBTIENEN LOS PRIVILEGIOS DE USUARIOS ")
    print("\n")
    print("                       -    EN  EL "+str(float(((high_accesscomplexity_single_authentication_allprivilegetrue_sh*100)/high_accesscomplexity_single_authentication_sh)))+" % DE VULNERABILIDADES SE OBTIENEN TODOS LOS PRIVILEGIOS")
    print("                       -    EN  EL "+str(float(((high_accesscomplexity_single_authentication_allprivilegefalse_sh*100)/high_accesscomplexity_single_authentication_sh)))+" % DE VULNERABILIDADES NO SE OBTIENEN TODOS LOS PRIVILEGIOS ")
    print("\n") 
if(high_accesscomplexity_multiple_authentication_sh>0):
    print("            -    EN  EL "+str(float(((high_accesscomplexity_multiple_authentication_sh*100)/high_accesscomplexity_sh)))+" % DE VULNERABILIDADES LA AUTENTICACIÓN ES MULTIPLE. LOS PORCENTAJES DE PRIVILEGIOS OBTENIDOS SON LOS SIGUIENTES: ")
    print("                       -    EN  EL "+str(float(((high_accesscomplexity_multiple_authentication_otherprivilegetrue_sh*100)/high_accesscomplexity_multiple_authentication_sh)))+" % DE VULNERABILIDADES SE OBTIENEN PRIVILEGIOS DISTINTOS A LOS DE USUARIO ")
    print("                       -    EN  EL "+str(float(((high_accesscomplexity_multiple_authentication_otherprivilegefalse_sh*100)/high_accesscomplexity_multiple_authentication_sh)))+" % DE VULNERABILIDADES NO SE OBTIENEN PRIVILEGIOS DISTINTOS A LOS DE USUARIO ")
    print("\n")
    print("                       -    EN  EL "+str(float(((high_accesscomplexity_multiple_authentication_userprivilegetrue_sh*100)/high_accesscomplexity_multiple_authentication_sh)))+" % DE VULNERABILIDADES SE OBTIENEN LOS PRIVILEGIOS DE USUARIOS")
    print("                       -    EN  EL "+str(float(((high_accesscomplexity_multiple_authentication_userprivilegefalse_sh*100)/high_accesscomplexity_multiple_authentication_sh)))+" % DE VULNERABILIDADES NO SE OBTIENEN LOS PRIVILEGIOS DE USUARIOS ")
    print("\n")
    print("                       -    EN  EL "+str(float(((high_accesscomplexity_multiple_authentication_allprivilegetrue_sh*100)/high_accesscomplexity_multiple_authentication_sh)))+" % DE VULNERABILIDADES SE OBTIENEN TODOS LOS PRIVILEGIOS")
    print("                       -    EN  EL "+str(float(((high_accesscomplexity_multiple_authentication_allprivilegefalse_sh*100)/high_accesscomplexity_multiple_authentication_sh)))+" % DE VULNERABILIDADES NO SE OBTIENEN TODOS LOS PRIVILEGIOS ")
    print("\n")
if(high_accesscomplexity_none_authentication_sh>0):
    print("            -    EN  EL "+str(float(((high_accesscomplexity_none_authentication_sh*100)/high_accesscomplexity_sh)))+" % DE VULNERABILIDADES NO SE REQUIERE AUTENTICACION. LOS PORCENTAJES DE PRIVILEGIOS OBTENIDOS SON LOS SIGUIENTES: ")
    print("                       -    EN  EL "+str(float(((high_accesscomplexity_none_authentication_otherprivilegetrue_sh*100)/high_accesscomplexity_none_authentication_sh)))+" % DE VULNERABILIDADES SE OBTIENEN PRIVILEGIOS DISTINTOS A LOS DE USUARIO ")
    print("                       -    EN  EL "+str(float(((high_accesscomplexity_none_authentication_otherprivilegefalse_sh*100)/high_accesscomplexity_none_authentication_sh)))+" % DE VULNERABILIDADES NO SE OBTIENEN PRIVILEGIOS DISTINTOS A LOS DE USUARIO ")
    print("\n")
    print("                       -    EN  EL "+str(float(((high_accesscomplexity_none_authentication_userprivilegetrue_sh*100)/high_accesscomplexity_none_authentication_sh)))+" % DE VULNERABILIDADES SE OBTIENEN LOS PRIVILEGIOS DE USUARIOS")
    print("                       -    EN  EL "+str(float(((high_accesscomplexity_none_authentication_userprivilegefalse_sh*100)/high_accesscomplexity_none_authentication_sh)))+" % DE VULNERABILIDADES NO SE OBTIENEN LOS PRIVILEGIOS DE USUARIOS ")
    print("\n")
    print("                       -    EN  EL "+str(float(((high_accesscomplexity_none_authentication_allprivilegetrue_sh*100)/high_accesscomplexity_none_authentication_sh)))+" % DE VULNERABILIDADES SE OBTIENEN TODOS LOS PRIVILEGIOS")
    print("                       -    EN  EL "+str(float(((high_accesscomplexity_none_authentication_allprivilegefalse_sh*100)/high_accesscomplexity_none_authentication_sh)))+" % DE VULNERABILIDADES NO SE OBTIENEN TODOS LOS PRIVILEGIOS ")
    print("\n") 
print("\n")
print("      -    EN  EL "+str(float(((low_accesscomplexity_sh*100)/len(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.accessComplexity"]))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES BAJA. LOS PORCENTAJES DE AUTENTICACIÓN SON LOS SIGUIENTES:  \n")
print("\n")
if(low_accesscomplexity_single_authentication_sh>0):
    print("            -    EN  EL "+str(float(((low_accesscomplexity_single_authentication_sh*100)/low_accesscomplexity_sh)))+" % DE VULNERABILIDADES LA AUTENTICACIÓN ES SENCILLA. LOS PORCENTAJES DE PRIVILEGIOS OBTENIDOS SON LOS SIGUIENTES: ")
    print("                       -    EN  EL "+str(float(((low_accesscomplexity_single_authentication_otherprivilegetrue_sh*100)/low_accesscomplexity_single_authentication_sh)))+" % DE VULNERABILIDADES SE OBTIENEN PRIVILEGIOS DISTINTOS A LOS DE USUARIO ")
    print("                       -    EN  EL "+str(float(((low_accesscomplexity_single_authentication_otherprivilegefalse_sh*100)/low_accesscomplexity_single_authentication_sh)))+" % DE VULNERABILIDADES NO SE OBTIENEN PRIVILEGIOS DISTINTOS A LOS DE USUARIO ")
    print("\n")
    print("                       -    EN  EL "+str(float(((low_accesscomplexity_single_authentication_userprivilegetrue_sh*100)/low_accesscomplexity_single_authentication_sh)))+" % DE VULNERABILIDADES SE OBTIENEN LOS PRIVILEGIOS DE USUARIOS")
    print("                       -    EN  EL "+str(float(((low_accesscomplexity_single_authentication_userprivilegefalse_sh*100)/low_accesscomplexity_single_authentication_sh)))+" % DE VULNERABILIDADES NO SE OBTIENEN LOS PRIVILEGIOS DE USUARIOS ")
    print("\n")
    print("                       -    EN  EL "+str(float(((low_accesscomplexity_single_authentication_allprivilegetrue_sh*100)/low_accesscomplexity_single_authentication_sh)))+" % DE VULNERABILIDADES SE OBTIENEN TODOS LOS PRIVILEGIOS")
    print("                       -    EN  EL "+str(float(((low_accesscomplexity_single_authentication_allprivilegefalse_sh*100)/low_accesscomplexity_single_authentication_sh)))+" % DE VULNERABILIDADES NO SE OBTIENEN TODOS LOS PRIVILEGIOS ")
    print("\n") 
if(low_accesscomplexity_multiple_authentication_sh>0):
    print("            -    EN  EL "+str(float(((low_accesscomplexity_multiple_authentication_sh*100)/low_accesscomplexity_sh)))+" % DE VULNERABILIDADES LA AUTENTICACIÓN ES MULTIPLE. LOS PORCENTAJES DE PRIVILEGIOS OBTENIDOS SON LOS SIGUIENTES: ")
    print("                       -    EN  EL "+str(float(((low_accesscomplexity_multiple_authentication_otherprivilegetrue_sh*100)/low_accesscomplexity_multiple_authentication_sh)))+" % DE VULNERABILIDADES SE OBTIENEN PRIVILEGIOS DISTINTOS A LOS DE USUARIO ")
    print("                       -    EN  EL "+str(float(((low_accesscomplexity_multiple_authentication_otherprivilegefalse_sh*100)/low_accesscomplexity_multiple_authentication_sh)))+" % DE VULNERABILIDADES NO SE OBTIENEN PRIVILEGIOS DISTINTOS A LOS DE USUARIO ")
    print("\n")
    print("                       -    EN  EL "+str(float(((low_accesscomplexity_multiple_authentication_userprivilegetrue_sh*100)/low_accesscomplexity_multiple_authentication_sh)))+" % DE VULNERABILIDADES SE OBTIENEN LOS PRIVILEGIOS DE USUARIOS")
    print("                       -    EN  EL "+str(float(((low_accesscomplexity_multiple_authentication_userprivilegefalse_sh*100)/low_accesscomplexity_multiple_authentication_sh)))+" % DE VULNERABILIDADES NO SE OBTIENEN LOS PRIVILEGIOS DE USUARIOS ")
    print("\n")
    print("                       -    EN  EL "+str(float(((low_accesscomplexity_multiple_authentication_allprivilegetrue_sh*100)/low_accesscomplexity_multiple_authentication_sh)))+" % DE VULNERABILIDADES SE OBTIENEN TODOS LOS PRIVILEGIOS")
    print("                       -    EN  EL "+str(float(((low_accesscomplexity_multiple_authentication_allprivilegefalse_sh*100)/low_accesscomplexity_multiple_authentication_sh)))+" % DE VULNERABILIDADES NO SE OBTIENEN TODOS LOS PRIVILEGIOS ")
    print("\n") 
if(low_accesscomplexity_none_authentication_sh>0):
    print("            -    EN  EL "+str(float(((low_accesscomplexity_none_authentication_sh*100)/low_accesscomplexity_sh)))+" % DE VULNERABILIDADES NO SE REQUIERE AUTENTICACION. LOS PORCENTAJES DE PRIVILEGIOS OBTENIDOS SON LOS SIGUIENTES: ")
    print("                       -    EN  EL "+str(float(((low_accesscomplexity_none_authentication_otherprivilegetrue_sh*100)/low_accesscomplexity_none_authentication_sh)))+" % DE VULNERABILIDADES SE OBTIENEN PRIVILEGIOS DISTINTOS A LOS DE USUARIO ")
    print("                       -    EN  EL "+str(float(((low_accesscomplexity_none_authentication_otherprivilegefalse_sh*100)/low_accesscomplexity_none_authentication_sh)))+" % DE VULNERABILIDADES NO SE OBTIENEN PRIVILEGIOS DISTINTOS A LOS DE USUARIO ")
    print("\n")
    print("                       -    EN  EL "+str(float(((low_accesscomplexity_none_authentication_userprivilegetrue_sh*100)/low_accesscomplexity_none_authentication_sh)))+" % DE VULNERABILIDADES SE OBTIENEN LOS PRIVILEGIOS DE USUARIOS")
    print("                       -    EN  EL "+str(float(((low_accesscomplexity_none_authentication_userprivilegefalse_sh*100)/low_accesscomplexity_none_authentication_sh)))+" % DE VULNERABILIDADES NO SE OBTIENEN LOS PRIVILEGIOS DE USUARIOS ")
    print("\n")
    print("                       -    EN  EL "+str(float(((low_accesscomplexity_none_authentication_allprivilegetrue_sh*100)/low_accesscomplexity_none_authentication_sh)))+" % DE VULNERABILIDADES SE OBTIENEN TODOS LOS PRIVILEGIOS")
    print("                       -    EN  EL "+str(float(((low_accesscomplexity_none_authentication_allprivilegefalse_sh*100)/low_accesscomplexity_none_authentication_sh)))+" % DE VULNERABILIDADES NO SE OBTIENEN TODOS LOS PRIVILEGIOS ")
    print("\n") 
print("\n")
print("      -    EN  EL "+str(float(((medium_accesscomplexity_sh*100)/len(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.accessComplexity"]))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES MEDIA. LOS PORCENTAJES DE AUTENTICACIÓN SON LOS SIGUIENTES:  \n")
print("\n")
if(medium_accesscomplexity_single_authentication_sh>0):
    print("            -    EN  EL "+str(float(((medium_accesscomplexity_single_authentication_sh*100)/medium_accesscomplexity_sh)))+" % DE VULNERABILIDADES LA AUTENTICACIÓN ES SENCILLA. LOS PORCENTAJES DE PRIVILEGIOS OBTENIDOS SON LOS SIGUIENTES: ")
    print("                       -    EN  EL "+str(float(((medium_accesscomplexity_single_authentication_otherprivilegetrue_sh*100)/medium_accesscomplexity_single_authentication_sh)))+" % DE VULNERABILIDADES SE OBTIENEN PRIVILEGIOS DISTINTOS A LOS DE USUARIO ")
    print("                       -    EN  EL "+str(float(((medium_accesscomplexity_single_authentication_otherprivilegefalse_sh*100)/medium_accesscomplexity_single_authentication_sh)))+" % DE VULNERABILIDADES NO SE OBTIENEN PRIVILEGIOS DISTINTOS A LOS DE USUARIO ")
    print("\n")
    print("                       -    EN  EL "+str(float(((medium_accesscomplexity_single_authentication_userprivilegetrue_sh*100)/medium_accesscomplexity_single_authentication_sh)))+" % DE VULNERABILIDADES SE OBTIENEN LOS PRIVILEGIOS DE USUARIOS")
    print("                       -    EN  EL "+str(float(((medium_accesscomplexity_single_authentication_userprivilegefalse_sh*100)/medium_accesscomplexity_single_authentication_sh)))+" % DE VULNERABILIDADES NO SE OBTIENEN LOS PRIVILEGIOS DE USUARIOS ")
    print("\n")
    print("                       -    EN  EL "+str(float(((medium_accesscomplexity_single_authentication_allprivilegetrue_sh*100)/medium_accesscomplexity_single_authentication_sh)))+" % DE VULNERABILIDADES SE OBTIENEN TODOS LOS PRIVILEGIOS")
    print("                       -    EN  EL "+str(float(((medium_accesscomplexity_single_authentication_allprivilegefalse_sh*100)/medium_accesscomplexity_single_authentication_sh)))+" % DE VULNERABILIDADES NO SE OBTIENEN TODOS LOS PRIVILEGIOS ")
    print("\n") 
if(medium_accesscomplexity_multiple_authentication_sh>0):
    print("            -    EN  EL "+str(float(((medium_accesscomplexity_multiple_authentication_sh*100)/medium_accesscomplexity_sh)))+" % DE VULNERABILIDADES LA AUTENTICACIÓN ES MULTIPLE. LOS PORCENTAJES DE PRIVILEGIOS OBTENIDOS SON LOS SIGUIENTES: ")
    print("                       -    EN  EL "+str(float(((medium_accesscomplexity_multiple_authentication_otherprivilegetrue_sh*100)/medium_accesscomplexity_multiple_authentication_sh)))+" % DE VULNERABILIDADES SE OBTIENEN PRIVILEGIOS DISTINTOS A LOS DE USUARIO ")
    print("                       -    EN  EL "+str(float(((medium_accesscomplexity_multiple_authentication_otherprivilegefalse_sh*100)/medium_accesscomplexity_multiple_authentication_sh)))+" % DE VULNERABILIDADES NO SE OBTIENEN PRIVILEGIOS DISTINTOS A LOS DE USUARIO ")
    print("\n")
    print("                       -    EN  EL "+str(float(((medium_accesscomplexity_multiple_authentication_userprivilegetrue_sh*100)/medium_accesscomplexity_multiple_authentication_sh)))+" % DE VULNERABILIDADES SE OBTIENEN LOS PRIVILEGIOS DE USUARIOS")
    print("                       -    EN  EL "+str(float(((medium_accesscomplexity_multiple_authentication_userprivilegefalse_sh*100)/medium_accesscomplexity_multiple_authentication_sh)))+" % DE VULNERABILIDADES NO SE OBTIENEN LOS PRIVILEGIOS DE USUARIOS ")
    print("\n")
    print("                       -    EN  EL "+str(float(((medium_accesscomplexity_multiple_authentication_allprivilegetrue_sh*100)/medium_accesscomplexity_multiple_authentication_sh)))+" % DE VULNERABILIDADES SE OBTIENEN TODOS LOS PRIVILEGIOS")
    print("                       -    EN  EL "+str(float(((medium_accesscomplexity_multiple_authentication_allprivilegefalse_sh*100)/medium_accesscomplexity_multiple_authentication_sh)))+" % DE VULNERABILIDADES NO SE OBTIENEN TODOS LOS PRIVILEGIOS ")
    print("\n")
if(medium_accesscomplexity_none_authentication_sh>0):
    print("            -    EN  EL "+str(float(((medium_accesscomplexity_none_authentication_sh*100)/medium_accesscomplexity_sh)))+" % DE VULNERABILIDADES NO SE REQUIERE AUTENTICACION. LOS PORCENTAJES DE PRIVILEGIOS OBTENIDOS SON LOS SIGUIENTES: ")
    print("                       -    EN  EL "+str(float(((medium_accesscomplexity_none_authentication_otherprivilegetrue_sh*100)/medium_accesscomplexity_none_authentication_sh)))+" % DE VULNERABILIDADES SE OBTIENEN PRIVILEGIOS DISTINTOS A LOS DE USUARIO ")
    print("                       -    EN  EL "+str(float(((medium_accesscomplexity_none_authentication_otherprivilegefalse_sh*100)/medium_accesscomplexity_none_authentication_sh)))+" % DE VULNERABILIDADES NO SE OBTIENEN PRIVILEGIOS DISTINTOS A LOS DE USUARIO ")
    print("\n")
    print("                       -    EN  EL "+str(float(((medium_accesscomplexity_none_authentication_userprivilegetrue_sh*100)/medium_accesscomplexity_none_authentication_sh)))+" % DE VULNERABILIDADES SE OBTIENEN LOS PRIVILEGIOS DE USUARIOS")
    print("                       -    EN  EL "+str(float(((medium_accesscomplexity_none_authentication_userprivilegefalse_sh*100)/medium_accesscomplexity_none_authentication_sh)))+" % DE VULNERABILIDADES NO SE OBTIENEN LOS PRIVILEGIOS DE USUARIOS ")
    print("\n")
    print("                       -    EN  EL "+str(float(((medium_accesscomplexity_none_authentication_allprivilegetrue_sh*100)/medium_accesscomplexity_none_authentication_sh)))+" % DE VULNERABILIDADES SE OBTIENEN TODOS LOS PRIVILEGIOS")
    print("                       -    EN  EL "+str(float(((medium_accesscomplexity_none_authentication_allprivilegefalse_sh*100)/medium_accesscomplexity_none_authentication_sh)))+" % DE VULNERABILIDADES NO SE OBTIENEN TODOS LOS PRIVILEGIOS ")
    print("\n") 







print("************************************* ESTADÍSTICAS COMPLEJIDAD DE ACCESO/AUTENTICACION-OBTENCION DE PRIVILEGIOS DE TODOS/OTROS/USUARIOS PARTE IOT Y SMART HOME CONJUNTAS *************************************")
print("\n")                           
print(" DE UN TOTAL DE "+str((len(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.accessComplexity"]))+(len(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.accessComplexity"])))+" VULNERABILIDADES , LAS ESTADISTICAS DE COMPLEJIDAD DE ACCESO SON LAS SIGUIENTES:  \n")
print("\n")
print("      -    EN  "+str(high_accesscomplexity_sh+high_accesscomplexity_iot)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES ALTA. LAS ESTADÍSTICAS DE AUTENTICACIÓN LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(high_accesscomplexity_single_authentication_sh+high_accesscomplexity_single_authentication_iot)+" VULNERABILIDADES LA AUTENTICACIÓN ES SENCILLA. LAS ESTADÍSTICAS DE PRIVILEGIOS OBTENIDOS SON LAS SIGUIENTES: ")
print("                       -    EN  "+str(high_accesscomplexity_single_authentication_otherprivilegetrue_sh+high_accesscomplexity_single_authentication_otherprivilegetrue_iot)+" VULNERABILIDADES SE OBTIENEN OTROS PRIVILEGIOS DISTINTOS A LOS DE USUARIO")
print("                       -    EN  "+str(high_accesscomplexity_single_authentication_otherprivilegefalse_sh+high_accesscomplexity_single_authentication_otherprivilegefalse_iot)+" VULNERABILIDADES NO SE OBTIENEN OTROS PRIVILEGIOS DISTINTOS A LOS DE USUARIO")
print("\n")
print("                       -    EN  "+str(high_accesscomplexity_single_authentication_userprivilegetrue_sh+high_accesscomplexity_single_authentication_userprivilegetrue_iot)+" VULNERABILIDADES SE OBTIENEN LOS PRIVILEGIOS DE USUARIOS")
print("                       -    EN  "+str(high_accesscomplexity_single_authentication_userprivilegefalse_sh+high_accesscomplexity_single_authentication_userprivilegefalse_iot)+" VULNERABILIDADES NO SE OBTIENEN LOS PRIVILEGIOS DE USUARIOS ")
print("\n")
print("                       -    EN  "+str(high_accesscomplexity_single_authentication_allprivilegetrue_sh+high_accesscomplexity_single_authentication_allprivilegetrue_iot)+" VULNERABILIDADES SE OBTIENEN TODOS LOS PRIVILEGIOS")
print("                       -    EN  "+str(high_accesscomplexity_single_authentication_allprivilegefalse_sh+high_accesscomplexity_single_authentication_allprivilegefalse_iot)+" VULNERABILIDADES NO SE OBTIENEN TODOS LOS PRIVILEGIOS ")
print("\n")
print("\n")
print("            -    EN  "+str(high_accesscomplexity_multiple_authentication_sh+high_accesscomplexity_multiple_authentication_iot)+" VULNERABILIDADES LA AUTENTICACIÓN ES MULTIPLE. LAS ESTADÍSTICAS DE PRIVILEGIOS OBTENIDOS SON LAS SIGUIENTES: ")
print("                       -    EN  "+str(high_accesscomplexity_multiple_authentication_otherprivilegetrue_sh+high_accesscomplexity_multiple_authentication_otherprivilegetrue_iot)+" VULNERABILIDADES SE OBTIENEN OTROS PRIVILEGIOS DISTINTOS A LOS DE USUARIO")
print("                       -    EN  "+str(high_accesscomplexity_multiple_authentication_otherprivilegefalse_sh+high_accesscomplexity_multiple_authentication_otherprivilegefalse_iot)+" VULNERABILIDADES NO SE OBTIENEN OTROS PRIVILEGIOS DISTINTOS A LOS DE USUARIO")
print("\n")
print("                       -    EN  "+str(high_accesscomplexity_multiple_authentication_userprivilegetrue_sh+high_accesscomplexity_multiple_authentication_userprivilegetrue_iot)+" VULNERABILIDADES SE OBTIENEN LOS PRIVILEGIOS DE USUARIOS")
print("                       -    EN  "+str(high_accesscomplexity_multiple_authentication_userprivilegefalse_sh+high_accesscomplexity_multiple_authentication_userprivilegefalse_iot)+" VULNERABILIDADES NO SE OBTIENEN LOS PRIVILEGIOS DE USUARIOS ")
print("\n")
print("                       -    EN  "+str(high_accesscomplexity_multiple_authentication_allprivilegetrue_sh+high_accesscomplexity_multiple_authentication_allprivilegetrue_iot)+" VULNERABILIDADES SE OBTIENEN TODOS LOS PRIVILEGIOS")
print("                       -    EN  "+str(high_accesscomplexity_multiple_authentication_allprivilegefalse_sh+high_accesscomplexity_multiple_authentication_allprivilegefalse_iot)+" VULNERABILIDADES NO SE OBTIENEN TODOS LOS PRIVILEGIOS ")
print("\n")
print("\n")
print("            -    EN  "+str(high_accesscomplexity_none_authentication_sh+high_accesscomplexity_none_authentication_iot)+" VULNERABILIDADES NO SE REQUIERE AUTENTICACION. LAS ESTADÍSTICAS DE PRIVILEGIOS OBTENIDOS SON LAS SIGUIENTES: ")
print("                       -    EN  "+str(high_accesscomplexity_none_authentication_otherprivilegetrue_sh+high_accesscomplexity_none_authentication_otherprivilegetrue_iot)+" VULNERABILIDADES SE OBTIENEN OTROS PRIVILEGIOS DISTINTOS A LOS DE USUARIO")
print("                       -    EN  "+str(high_accesscomplexity_none_authentication_otherprivilegefalse_sh+high_accesscomplexity_none_authentication_otherprivilegefalse_iot)+" VULNERABILIDADES NO SE OBTIENEN OTROS PRIVILEGIOS DISTINTOS A LOS DE USUARIO")
print("\n")
print("                       -    EN  "+str(high_accesscomplexity_none_authentication_userprivilegetrue_sh+high_accesscomplexity_none_authentication_userprivilegetrue_iot)+" VULNERABILIDADES SE OBTIENEN LOS PRIVILEGIOS DE USUARIOS")
print("                       -    EN  "+str(high_accesscomplexity_none_authentication_userprivilegefalse_sh+high_accesscomplexity_none_authentication_userprivilegefalse_iot)+" VULNERABILIDADES NO SE OBTIENEN LOS PRIVILEGIOS DE USUARIOS ")
print("\n")
print("                       -    EN  "+str(high_accesscomplexity_none_authentication_allprivilegetrue_sh+high_accesscomplexity_none_authentication_allprivilegetrue_iot)+" VULNERABILIDADES SE OBTIENEN TODOS LOS PRIVILEGIOS")
print("                       -    EN  "+str(high_accesscomplexity_none_authentication_allprivilegefalse_sh+high_accesscomplexity_none_authentication_allprivilegefalse_iot)+" VULNERABILIDADES NO SE OBTIENEN TODOS LOS PRIVILEGIOS ")
print("\n")
print("      -    EN  "+str(low_accesscomplexity_sh+low_accesscomplexity_iot)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES BAJA. LAS ESTADÍSTICAS DE AUTENTICACIÓN LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(low_accesscomplexity_single_authentication_sh+low_accesscomplexity_single_authentication_iot)+" VULNERABILIDADES LA AUTENTICACIÓN ES SENCILLA. LAS ESTADÍSTICAS DE PRIVILEGIOS OBTENIDOS SON LAS SIGUIENTES: ")
print("                       -    EN  "+str(low_accesscomplexity_single_authentication_otherprivilegetrue_sh+low_accesscomplexity_single_authentication_otherprivilegetrue_iot)+" VULNERABILIDADES SE OBTIENEN OTROS PRIVILEGIOS DISTINTOS A LOS DE USUARIO")
print("                       -    EN  "+str(low_accesscomplexity_single_authentication_otherprivilegefalse_sh+low_accesscomplexity_single_authentication_otherprivilegefalse_iot)+" VULNERABILIDADES NO SE OBTIENEN OTROS PRIVILEGIOS DISTINTOS A LOS DE USUARIO")
print("\n")
print("                       -    EN  "+str(low_accesscomplexity_single_authentication_userprivilegetrue_sh+low_accesscomplexity_single_authentication_userprivilegetrue_iot)+" VULNERABILIDADES SE OBTIENEN LOS PRIVILEGIOS DE USUARIOS")
print("                       -    EN  "+str(low_accesscomplexity_single_authentication_userprivilegefalse_sh+low_accesscomplexity_single_authentication_userprivilegefalse_iot)+" VULNERABILIDADES NO SE OBTIENEN LOS PRIVILEGIOS DE USUARIOS ")
print("\n")
print("                       -    EN  "+str(low_accesscomplexity_single_authentication_allprivilegetrue_sh+low_accesscomplexity_single_authentication_allprivilegetrue_iot)+" VULNERABILIDADES SE OBTIENEN TODOS LOS PRIVILEGIOS")
print("                       -    EN  "+str(low_accesscomplexity_single_authentication_allprivilegefalse_sh+low_accesscomplexity_single_authentication_allprivilegefalse_iot)+" VULNERABILIDADES NO SE OBTIENEN TODOS LOS PRIVILEGIOS ")
print("\n")
print("\n")
print("            -    EN  "+str(low_accesscomplexity_multiple_authentication_sh+low_accesscomplexity_multiple_authentication_iot)+" VULNERABILIDADES LA AUTENTICACIÓN ES MULTIPLE. LAS ESTADÍSTICAS DE PRIVILEGIOS OBTENIDOS SON LAS SIGUIENTES: ")
print("                       -    EN  "+str(low_accesscomplexity_multiple_authentication_otherprivilegetrue_sh+low_accesscomplexity_multiple_authentication_otherprivilegetrue_iot)+" VULNERABILIDADES SE OBTIENEN OTROS PRIVILEGIOS DISTINTOS A LOS DE USUARIO")
print("                       -    EN  "+str(low_accesscomplexity_multiple_authentication_otherprivilegefalse_sh+low_accesscomplexity_multiple_authentication_otherprivilegefalse_iot)+" VULNERABILIDADES NO SE OBTIENEN OTROS PRIVILEGIOS DISTINTOS A LOS DE USUARIO")
print("\n")
print("                       -    EN  "+str(low_accesscomplexity_multiple_authentication_userprivilegetrue_sh+low_accesscomplexity_multiple_authentication_userprivilegetrue_iot)+" VULNERABILIDADES SE OBTIENEN LOS PRIVILEGIOS DE USUARIOS")
print("                       -    EN  "+str(low_accesscomplexity_multiple_authentication_userprivilegefalse_sh+low_accesscomplexity_multiple_authentication_userprivilegefalse_iot)+" VULNERABILIDADES NO SE OBTIENEN LOS PRIVILEGIOS DE USUARIOS ")
print("\n")
print("                       -    EN  "+str(low_accesscomplexity_multiple_authentication_allprivilegetrue_sh+low_accesscomplexity_multiple_authentication_allprivilegetrue_iot)+" VULNERABILIDADES SE OBTIENEN TODOS LOS PRIVILEGIOS")
print("                       -    EN  "+str(low_accesscomplexity_multiple_authentication_allprivilegefalse_sh+low_accesscomplexity_multiple_authentication_allprivilegefalse_iot)+" VULNERABILIDADES NO SE OBTIENEN TODOS LOS PRIVILEGIOS ")
print("\n")
print("\n")
print("            -    EN  "+str(low_accesscomplexity_none_authentication_sh+low_accesscomplexity_none_authentication_iot)+" VULNERABILIDADES NO SE REQUIERE AUTENTICACION. LAS ESTADÍSTICAS DE PRIVILEGIOS OBTENIDOS SON LAS SIGUIENTES: ")
print("                       -    EN  "+str(low_accesscomplexity_none_authentication_otherprivilegetrue_sh+low_accesscomplexity_none_authentication_otherprivilegetrue_iot)+" VULNERABILIDADES SE OBTIENEN OTROS PRIVILEGIOS DISTINTOS A LOS DE USUARIO")
print("                       -    EN  "+str(low_accesscomplexity_none_authentication_otherprivilegefalse_sh+low_accesscomplexity_none_authentication_otherprivilegefalse_iot)+" VULNERABILIDADES NO SE OBTIENEN OTROS PRIVILEGIOS DISTINTOS A LOS DE USUARIO")
print("\n")
print("                       -    EN  "+str(low_accesscomplexity_none_authentication_userprivilegetrue_sh+low_accesscomplexity_none_authentication_userprivilegetrue_iot)+" VULNERABILIDADES SE OBTIENEN LOS PRIVILEGIOS DE USUARIOS")
print("                       -    EN  "+str(low_accesscomplexity_none_authentication_userprivilegefalse_sh+low_accesscomplexity_none_authentication_userprivilegefalse_iot)+" VULNERABILIDADES NO SE OBTIENEN LOS PRIVILEGIOS DE USUARIOS ")
print("\n")
print("                       -    EN  "+str(low_accesscomplexity_none_authentication_allprivilegetrue_sh+low_accesscomplexity_none_authentication_allprivilegetrue_iot)+" VULNERABILIDADES SE OBTIENEN TODOS LOS PRIVILEGIOS")
print("                       -    EN  "+str(low_accesscomplexity_none_authentication_allprivilegefalse_sh+low_accesscomplexity_none_authentication_allprivilegefalse_iot)+" VULNERABILIDADES NO SE OBTIENEN TODOS LOS PRIVILEGIOS ")
print("\n")
print("      -    EN  "+str(medium_accesscomplexity_sh+medium_accesscomplexity_iot)+" VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES MEDIA. LAS ESTADÍSTICAS DE AUTENTICACIÓN LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(medium_accesscomplexity_single_authentication_sh+medium_accesscomplexity_single_authentication_iot)+" VULNERABILIDADES LA AUTENTICACIÓN ES SENCILLA. LAS ESTADÍSTICAS DE PRIVILEGIOS OBTENIDOS SON LAS SIGUIENTES: ")
print("                       -    EN  "+str(medium_accesscomplexity_single_authentication_otherprivilegetrue_sh+medium_accesscomplexity_single_authentication_otherprivilegetrue_iot)+" VULNERABILIDADES SE OBTIENEN OTROS PRIVILEGIOS DISTINTOS A LOS DE USUARIO")
print("                       -    EN  "+str(medium_accesscomplexity_single_authentication_otherprivilegefalse_sh+medium_accesscomplexity_single_authentication_otherprivilegefalse_iot)+" VULNERABILIDADES NO SE OBTIENEN OTROS PRIVILEGIOS DISTINTOS A LOS DE USUARIO")
print("\n")
print("                       -    EN  "+str(medium_accesscomplexity_single_authentication_userprivilegetrue_sh+medium_accesscomplexity_single_authentication_userprivilegetrue_iot)+" VULNERABILIDADES SE OBTIENEN LOS PRIVILEGIOS DE USUARIOS")
print("                       -    EN  "+str(medium_accesscomplexity_single_authentication_userprivilegefalse_sh+medium_accesscomplexity_single_authentication_userprivilegefalse_iot)+" VULNERABILIDADES NO SE OBTIENEN LOS PRIVILEGIOS DE USUARIOS ")
print("\n")
print("                       -    EN  "+str(medium_accesscomplexity_single_authentication_allprivilegetrue_sh+medium_accesscomplexity_single_authentication_allprivilegetrue_iot)+" VULNERABILIDADES SE OBTIENEN TODOS LOS PRIVILEGIOS")
print("                       -    EN  "+str(medium_accesscomplexity_single_authentication_allprivilegefalse_sh+medium_accesscomplexity_single_authentication_allprivilegefalse_iot)+" VULNERABILIDADES NO SE OBTIENEN TODOS LOS PRIVILEGIOS ")
print("\n")
print("\n")
print("            -    EN  "+str(medium_accesscomplexity_multiple_authentication_sh+medium_accesscomplexity_multiple_authentication_iot)+" VULNERABILIDADES LA AUTENTICACIÓN ES MULTIPLE. LAS ESTADÍSTICAS DE PRIVILEGIOS OBTENIDOS SON LAS SIGUIENTES: ")
print("                       -    EN  "+str(medium_accesscomplexity_multiple_authentication_otherprivilegetrue_sh+medium_accesscomplexity_multiple_authentication_otherprivilegetrue_iot)+" VULNERABILIDADES SE OBTIENEN OTROS PRIVILEGIOS DISTINTOS A LOS DE USUARIO")
print("                       -    EN  "+str(medium_accesscomplexity_multiple_authentication_otherprivilegefalse_sh+medium_accesscomplexity_multiple_authentication_otherprivilegefalse_iot)+" VULNERABILIDADES NO SE OBTIENEN OTROS PRIVILEGIOS DISTINTOS A LOS DE USUARIO")
print("\n")
print("                       -    EN  "+str(medium_accesscomplexity_multiple_authentication_userprivilegetrue_sh+medium_accesscomplexity_multiple_authentication_userprivilegetrue_iot)+" VULNERABILIDADES SE OBTIENEN LOS PRIVILEGIOS DE USUARIOS")
print("                       -    EN  "+str(medium_accesscomplexity_multiple_authentication_userprivilegefalse_sh+medium_accesscomplexity_multiple_authentication_userprivilegefalse_iot)+" VULNERABILIDADES NO SE OBTIENEN LOS PRIVILEGIOS DE USUARIOS ")
print("\n")
print("                       -    EN  "+str(medium_accesscomplexity_multiple_authentication_allprivilegetrue_sh+medium_accesscomplexity_multiple_authentication_allprivilegetrue_iot)+" VULNERABILIDADES SE OBTIENEN TODOS LOS PRIVILEGIOS")
print("                       -    EN  "+str(medium_accesscomplexity_multiple_authentication_allprivilegefalse_sh+medium_accesscomplexity_multiple_authentication_allprivilegefalse_iot)+" VULNERABILIDADES NO SE OBTIENEN TODOS LOS PRIVILEGIOS ")
print("\n")
print("\n")
print("            -    EN  "+str(medium_accesscomplexity_none_authentication_sh+medium_accesscomplexity_none_authentication_iot)+" VULNERABILIDADES NO SE REQUIERE AUTENTICACION. LAS ESTADÍSTICAS DE PRIVILEGIOS OBTENIDOS SON LAS SIGUIENTES: ")
print("                       -    EN  "+str(medium_accesscomplexity_none_authentication_otherprivilegetrue_sh+medium_accesscomplexity_none_authentication_otherprivilegetrue_iot)+" VULNERABILIDADES SE OBTIENEN OTROS PRIVILEGIOS DISTINTOS A LOS DE USUARIO")
print("                       -    EN  "+str(medium_accesscomplexity_none_authentication_otherprivilegefalse_sh+medium_accesscomplexity_none_authentication_otherprivilegefalse_iot)+" VULNERABILIDADES NO SE OBTIENEN OTROS PRIVILEGIOS DISTINTOS A LOS DE USUARIO")
print("\n")
print("                       -    EN  "+str(medium_accesscomplexity_none_authentication_userprivilegetrue_sh+medium_accesscomplexity_none_authentication_userprivilegetrue_iot)+" VULNERABILIDADES SE OBTIENEN LOS PRIVILEGIOS DE USUARIOS")
print("                       -    EN  "+str(medium_accesscomplexity_none_authentication_userprivilegefalse_sh+medium_accesscomplexity_none_authentication_userprivilegefalse_iot)+" VULNERABILIDADES NO SE OBTIENEN LOS PRIVILEGIOS DE USUARIOS ")
print("\n")
print("                       -    EN  "+str(medium_accesscomplexity_none_authentication_allprivilegetrue_sh+medium_accesscomplexity_none_authentication_allprivilegetrue_iot)+" VULNERABILIDADES SE OBTIENEN TODOS LOS PRIVILEGIOS")
print("                       -    EN  "+str(medium_accesscomplexity_none_authentication_allprivilegefalse_sh+medium_accesscomplexity_none_authentication_allprivilegefalse_iot)+" VULNERABILIDADES NO SE OBTIENEN TODOS LOS PRIVILEGIOS ")
print("\n")

















print("*************************************PORCENTAJES COMPLEJIDAD DE ACCESO/AUTENTICACION-OBTENCION DE PRIVILEGIOS DE TODOS/OTROS/USUARIOS PARTE IOT Y SMART HOME CONJUNTAS*************************************")
print("\n")
print(" DE UN TOTAL DE "+str((len(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.accessComplexity"]))+(len(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.accessComplexity"])))+" VULNERABILIDADES , LOS PORCENTAJES DE COMPLEJIDAD DE ACCESO SON LOS SIGUIENTES:  \n")
print("\n")
print("      -    EN  EL "+str(float((((high_accesscomplexity_sh+high_accesscomplexity_iot)*100)/(len(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.accessComplexity"])+len(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.accessComplexity"])))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES ALTA. LOS PORCENTAJES DE AUTENTICACIÓN SON LOS SIGUIENTES:  \n")
print("\n")
if((high_accesscomplexity_single_authentication_sh+high_accesscomplexity_single_authentication_iot)>0):
    print("            -    EN  EL "+str(float((((high_accesscomplexity_single_authentication_sh+high_accesscomplexity_single_authentication_iot)*100)/(high_accesscomplexity_sh+high_accesscomplexity_iot))))+" % DE VULNERABILIDADES LA AUTENTICACIÓN ES SENCILLA. LOS PORCENTAJES DE PRIVILEGIOS OBTENIDOS SON LOS SIGUIENTES: ")
    print("                       -    EN  EL "+str(float((((high_accesscomplexity_single_authentication_otherprivilegetrue_sh+high_accesscomplexity_single_authentication_otherprivilegetrue_iot)*100)/(high_accesscomplexity_single_authentication_sh+high_accesscomplexity_single_authentication_iot))))+" % DE VULNERABILIDADES SE OBTIENEN OTROS PRIVILEGIOS DISTINTOS A LOS DE USUARIO")
    print("                       -    EN  EL "+str(float((((high_accesscomplexity_single_authentication_otherprivilegefalse_sh+high_accesscomplexity_single_authentication_otherprivilegefalse_iot)*100)/(high_accesscomplexity_single_authentication_sh+high_accesscomplexity_single_authentication_iot))))+" % DE VULNERABILIDADES NO SE OBTIENEN OTROS PRIVILEGIOS DISTINTOS A LOS DE USUARIO")
    print("\n")
    print("                       -    EN  EL "+str(float((((high_accesscomplexity_single_authentication_userprivilegetrue_sh+high_accesscomplexity_single_authentication_userprivilegetrue_iot)*100)/(high_accesscomplexity_single_authentication_sh+high_accesscomplexity_single_authentication_iot))))+" % DE VULNERABILIDADES SE OBTIENEN LOS PRIVILEGIOS DE USUARIOS")
    print("                       -    EN  EL "+str(float((((high_accesscomplexity_single_authentication_userprivilegefalse_sh+high_accesscomplexity_single_authentication_userprivilegefalse_iot)*100)/(high_accesscomplexity_single_authentication_sh+high_accesscomplexity_single_authentication_iot))))+" % DE VULNERABILIDADES NO SE OBTIENEN LOS PRIVILEGIOS DE USUARIOS ")
    print("\n")
    print("                       -    EN  EL "+str(float((((high_accesscomplexity_single_authentication_allprivilegetrue_sh+high_accesscomplexity_single_authentication_allprivilegetrue_iot)*100)/(high_accesscomplexity_single_authentication_sh+high_accesscomplexity_single_authentication_iot))))+" % DE VULNERABILIDADES SE OBTIENEN TODOS LOS PRIVILEGIOS")
    print("                       -    EN  EL "+str(float((((high_accesscomplexity_single_authentication_allprivilegefalse_sh+high_accesscomplexity_single_authentication_allprivilegefalse_iot)*100)/(high_accesscomplexity_single_authentication_sh+high_accesscomplexity_single_authentication_iot))))+" % DE VULNERABILIDADES NO SE OBTIENEN TODOS LOS PRIVILEGIOS ")
    print("\n")
if((high_accesscomplexity_multiple_authentication_sh+high_accesscomplexity_multiple_authentication_iot)>0):
    print("            -    EN  EL "+str(float((((high_accesscomplexity_multiple_authentication_sh+high_accesscomplexity_multiple_authentication_iot)*100)/(high_accesscomplexity_sh+high_accesscomplexity_iot))))+" % DE VULNERABILIDADES LA AUTENTICACIÓN ES MULTIPLE. LOS PORCENTAJES DE PRIVILEGIOS OBTENIDOS SON LOS SIGUIENTES: ")
    print("                       -    EN  EL "+str(float((((high_accesscomplexity_multiple_authentication_otherprivilegetrue_sh+high_accesscomplexity_multiple_authentication_otherprivilegetrue_iot)*100)/(high_accesscomplexity_multiple_authentication_sh+high_accesscomplexity_multiple_authentication_iot))))+" % DE VULNERABILIDADES SE OBTIENEN OTROS PRIVILEGIOS DISTINTOS A LOS DE USUARIO")
    print("                       -    EN  EL "+str(float((((high_accesscomplexity_multiple_authentication_otherprivilegefalse_sh+high_accesscomplexity_multiple_authentication_otherprivilegefalse_iot)*100)/(high_accesscomplexity_multiple_authentication_sh+high_accesscomplexity_multiple_authentication_iot))))+" % DE VULNERABILIDADES NO SE OBTIENEN OTROS PRIVILEGIOS DISTINTOS A LOS DE USUARIO")
    print("\n")
    print("                       -    EN  EL "+str(float((((high_accesscomplexity_multiple_authentication_userprivilegetrue_sh+high_accesscomplexity_multiple_authentication_userprivilegetrue_iot)*100)/(high_accesscomplexity_multiple_authentication_sh+high_accesscomplexity_multiple_authentication_iot))))+" % DE VULNERABILIDADES SE OBTIENEN LOS PRIVILEGIOS DE USUARIOS")
    print("                       -    EN  EL "+str(float((((high_accesscomplexity_multiple_authentication_userprivilegefalse_sh+high_accesscomplexity_multiple_authentication_userprivilegefalse_iot)*100)/(high_accesscomplexity_multiple_authentication_sh+high_accesscomplexity_multiple_authentication_iot))))+" % DE VULNERABILIDADES NO SE OBTIENEN LOS PRIVILEGIOS DE USUARIOS ")
    print("\n")
    print("                       -    EN  EL "+str(float((((high_accesscomplexity_multiple_authentication_allprivilegetrue_sh+high_accesscomplexity_multiple_authentication_allprivilegetrue_iot)*100)/(high_accesscomplexity_multiple_authentication_sh+high_accesscomplexity_multiple_authentication_iot))))+" % DE VULNERABILIDADES SE OBTIENEN TODOS LOS PRIVILEGIOS")
    print("                       -    EN  EL "+str(float((((high_accesscomplexity_multiple_authentication_allprivilegefalse_sh+high_accesscomplexity_multiple_authentication_allprivilegefalse_iot)*100)/(high_accesscomplexity_multiple_authentication_sh+high_accesscomplexity_multiple_authentication_iot))))+" % DE VULNERABILIDADES NO SE OBTIENEN TODOS LOS PRIVILEGIOS ")
    print("\n") 
if((high_accesscomplexity_none_authentication_sh+high_accesscomplexity_none_authentication_iot)>0):
    print("            -    EN  EL "+str(float((((high_accesscomplexity_none_authentication_sh+high_accesscomplexity_none_authentication_iot)*100)/(high_accesscomplexity_sh+high_accesscomplexity_iot))))+" % DE VULNERABILIDADES NO SE REQUIERE AUTENTICACION. LOS PORCENTAJES DE PRIVILEGIOS OBTENIDOS SON LOS SIGUIENTES: ")
    print("                       -    EN  EL "+str(float((((high_accesscomplexity_none_authentication_otherprivilegetrue_sh+high_accesscomplexity_none_authentication_otherprivilegetrue_iot)*100)/(high_accesscomplexity_none_authentication_sh+high_accesscomplexity_none_authentication_iot))))+" % DE VULNERABILIDADES SE OBTIENEN OTROS PRIVILEGIOS DISTINTOS A LOS DE USUARIO")
    print("                       -    EN  EL "+str(float((((high_accesscomplexity_none_authentication_otherprivilegefalse_sh+high_accesscomplexity_none_authentication_otherprivilegefalse_iot)*100)/(high_accesscomplexity_none_authentication_sh+high_accesscomplexity_none_authentication_iot))))+" % DE VULNERABILIDADES NO SE OBTIENEN OTROS PRIVILEGIOS DISTINTOS A LOS DE USUARIO")
    print("\n")
    print("                       -    EN  EL "+str(float((((high_accesscomplexity_none_authentication_userprivilegetrue_sh+high_accesscomplexity_none_authentication_userprivilegetrue_iot)*100)/(high_accesscomplexity_none_authentication_sh+high_accesscomplexity_none_authentication_iot))))+" % DE VULNERABILIDADES SE OBTIENEN LOS PRIVILEGIOS DE USUARIOS")
    print("                       -    EN  EL "+str(float((((high_accesscomplexity_none_authentication_userprivilegefalse_sh+high_accesscomplexity_none_authentication_userprivilegefalse_iot)*100)/(high_accesscomplexity_none_authentication_sh+high_accesscomplexity_none_authentication_iot))))+" % DE VULNERABILIDADES NO SE OBTIENEN LOS PRIVILEGIOS DE USUARIOS ")
    print("\n")
    print("                       -    EN  EL "+str(float((((high_accesscomplexity_none_authentication_allprivilegetrue_sh+high_accesscomplexity_none_authentication_allprivilegetrue_iot)*100)/(high_accesscomplexity_none_authentication_sh+high_accesscomplexity_none_authentication_iot))))+" % DE VULNERABILIDADES SE OBTIENEN TODOS LOS PRIVILEGIOS")
    print("                       -    EN  EL "+str(float((((high_accesscomplexity_none_authentication_allprivilegefalse_sh+high_accesscomplexity_none_authentication_allprivilegefalse_iot)*100)/(high_accesscomplexity_none_authentication_sh+high_accesscomplexity_none_authentication_iot))))+" % DE VULNERABILIDADES NO SE OBTIENEN TODOS LOS PRIVILEGIOS ")
    print("\n") 
    print("      -    EN  EL "+str(float((((low_accesscomplexity_sh+low_accesscomplexity_iot)*100)/(len(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.accessComplexity"])+len(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.accessComplexity"])))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES BAJA. LOS PORCENTAJES DE AUTENTICACIÓN SON LOS SIGUIENTES:  \n")
    print("\n")
if((low_accesscomplexity_single_authentication_sh+low_accesscomplexity_single_authentication_iot)>0):
    print("            -    EN  EL "+str(float((((low_accesscomplexity_single_authentication_sh+low_accesscomplexity_single_authentication_iot)*100)/(low_accesscomplexity_sh+low_accesscomplexity_iot))))+" % DE VULNERABILIDADES LA AUTENTICACIÓN ES SENCILLA. LOS PORCENTAJES DE PRIVILEGIOS OBTENIDOS SON LOS SIGUIENTES: ")
    print("                       -    EN  EL "+str(float((((low_accesscomplexity_single_authentication_otherprivilegetrue_sh+low_accesscomplexity_single_authentication_otherprivilegetrue_iot)*100)/(low_accesscomplexity_single_authentication_sh+low_accesscomplexity_single_authentication_iot))))+" % DE VULNERABILIDADES SE OBTIENEN OTROS PRIVILEGIOS DISTINTOS A LOS DE USUARIO")
    print("                       -    EN  EL "+str(float((((low_accesscomplexity_single_authentication_otherprivilegefalse_sh+low_accesscomplexity_single_authentication_otherprivilegefalse_iot)*100)/(low_accesscomplexity_single_authentication_sh+low_accesscomplexity_single_authentication_iot))))+" % DE VULNERABILIDADES NO SE OBTIENEN OTROS PRIVILEGIOS DISTINTOS A LOS DE USUARIO")
    print("\n")
    print("                       -    EN  EL "+str(float((((low_accesscomplexity_single_authentication_userprivilegetrue_sh+low_accesscomplexity_single_authentication_userprivilegetrue_iot)*100)/(low_accesscomplexity_single_authentication_sh+low_accesscomplexity_single_authentication_iot))))+" % DE VULNERABILIDADES SE OBTIENEN LOS PRIVILEGIOS DE USUARIOS")
    print("                       -    EN  EL "+str(float((((low_accesscomplexity_single_authentication_userprivilegefalse_sh+low_accesscomplexity_single_authentication_userprivilegefalse_iot)*100)/(low_accesscomplexity_single_authentication_sh+low_accesscomplexity_single_authentication_iot))))+" % DE VULNERABILIDADES NO SE OBTIENEN LOS PRIVILEGIOS DE USUARIOS ")
    print("\n")
    print("                       -    EN  EL "+str(float((((low_accesscomplexity_single_authentication_allprivilegetrue_sh+low_accesscomplexity_single_authentication_allprivilegetrue_iot)*100)/(low_accesscomplexity_single_authentication_sh+low_accesscomplexity_single_authentication_iot))))+" % DE VULNERABILIDADES SE OBTIENEN TODOS LOS PRIVILEGIOS")
    print("                       -    EN  EL "+str(float((((low_accesscomplexity_single_authentication_allprivilegefalse_sh+low_accesscomplexity_single_authentication_allprivilegefalse_iot)*100)/(low_accesscomplexity_single_authentication_sh+low_accesscomplexity_single_authentication_iot))))+" % DE VULNERABILIDADES NO SE OBTIENEN TODOS LOS PRIVILEGIOS ")
    print("\n") 
if((low_accesscomplexity_multiple_authentication_sh+low_accesscomplexity_multiple_authentication_iot)>0):
    print("            -    EN  EL "+str(float((((low_accesscomplexity_multiple_authentication_sh+low_accesscomplexity_multiple_authentication_iot)*100)/(low_accesscomplexity_sh+low_accesscomplexity_iot))))+" % DE VULNERABILIDADES LA AUTENTICACIÓN ES MULTIPLE. LOS PORCENTAJES DE PRIVILEGIOS OBTENIDOS SON LOS SIGUIENTES: ")
    print("                       -    EN  EL "+str(float((((low_accesscomplexity_multiple_authentication_otherprivilegetrue_sh+low_accesscomplexity_multiple_authentication_otherprivilegetrue_iot)*100)/(low_accesscomplexity_multiple_authentication_sh+low_accesscomplexity_multiple_authentication_iot))))+" % DE VULNERABILIDADES SE OBTIENEN OTROS PRIVILEGIOS DISTINTOS A LOS DE USUARIO")
    print("                       -    EN  EL "+str(float((((low_accesscomplexity_multiple_authentication_otherprivilegefalse_sh+low_accesscomplexity_multiple_authentication_otherprivilegefalse_iot)*100)/(low_accesscomplexity_multiple_authentication_sh+low_accesscomplexity_multiple_authentication_iot))))+" % DE VULNERABILIDADES NO SE OBTIENEN OTROS PRIVILEGIOS DISTINTOS A LOS DE USUARIO")
    print("\n")
    print("                       -    EN  EL "+str(float((((low_accesscomplexity_multiple_authentication_userprivilegetrue_sh+low_accesscomplexity_multiple_authentication_userprivilegetrue_iot)*100)/(low_accesscomplexity_multiple_authentication_sh+low_accesscomplexity_multiple_authentication_iot))))+" % DE VULNERABILIDADES SE OBTIENEN LOS PRIVILEGIOS DE USUARIOS")
    print("                       -    EN  EL "+str(float((((low_accesscomplexity_multiple_authentication_userprivilegefalse_sh+low_accesscomplexity_multiple_authentication_userprivilegefalse_iot)*100)/(low_accesscomplexity_multiple_authentication_sh+low_accesscomplexity_multiple_authentication_iot))))+" % DE VULNERABILIDADES NO SE OBTIENEN LOS PRIVILEGIOS DE USUARIOS ")
    print("\n")
    print("                       -    EN  EL "+str(float((((low_accesscomplexity_multiple_authentication_allprivilegetrue_sh+low_accesscomplexity_multiple_authentication_allprivilegetrue_iot)*100)/(low_accesscomplexity_multiple_authentication_sh+low_accesscomplexity_multiple_authentication_iot))))+" % DE VULNERABILIDADES SE OBTIENEN TODOS LOS PRIVILEGIOS")
    print("                       -    EN  EL "+str(float((((low_accesscomplexity_multiple_authentication_allprivilegefalse_sh+low_accesscomplexity_multiple_authentication_allprivilegefalse_iot)*100)/(low_accesscomplexity_multiple_authentication_sh+low_accesscomplexity_multiple_authentication_iot))))+" % DE VULNERABILIDADES NO SE OBTIENEN TODOS LOS PRIVILEGIOS ")
    print("\n") 
if((low_accesscomplexity_none_authentication_sh+low_accesscomplexity_none_authentication_iot)>0):
    print("            -    EN  EL "+str(float((((low_accesscomplexity_none_authentication_sh+low_accesscomplexity_none_authentication_iot)*100)/(low_accesscomplexity_sh+low_accesscomplexity_iot))))+" % DE VULNERABILIDADES NO SE REQUIERE AUTENTICACION. LOS PORCENTAJES DE PRIVILEGIOS OBTENIDOS SON LOS SIGUIENTES: ")
    print("                       -    EN  EL "+str(float((((low_accesscomplexity_none_authentication_otherprivilegetrue_sh+low_accesscomplexity_none_authentication_otherprivilegetrue_iot)*100)/(low_accesscomplexity_none_authentication_sh+low_accesscomplexity_none_authentication_iot))))+" % DE VULNERABILIDADES SE OBTIENEN OTROS PRIVILEGIOS DISTINTOS A LOS DE USUARIO")
    print("                       -    EN  EL "+str(float((((low_accesscomplexity_none_authentication_otherprivilegefalse_sh+low_accesscomplexity_none_authentication_otherprivilegefalse_iot)*100)/(low_accesscomplexity_none_authentication_sh+low_accesscomplexity_none_authentication_iot))))+" % DE VULNERABILIDADES NO SE OBTIENEN OTROS PRIVILEGIOS DISTINTOS A LOS DE USUARIO")
    print("\n")
    print("                       -    EN  EL "+str(float((((low_accesscomplexity_none_authentication_userprivilegetrue_sh+low_accesscomplexity_none_authentication_userprivilegetrue_iot)*100)/(low_accesscomplexity_none_authentication_sh+low_accesscomplexity_none_authentication_iot))))+" % DE VULNERABILIDADES SE OBTIENEN LOS PRIVILEGIOS DE USUARIOS")
    print("                       -    EN  EL "+str(float((((low_accesscomplexity_none_authentication_userprivilegefalse_sh+low_accesscomplexity_none_authentication_userprivilegefalse_iot)*100)/(low_accesscomplexity_none_authentication_sh+low_accesscomplexity_none_authentication_iot))))+" % DE VULNERABILIDADES NO SE OBTIENEN LOS PRIVILEGIOS DE USUARIOS ")
    print("\n")
    print("                       -    EN  EL "+str(float((((low_accesscomplexity_none_authentication_allprivilegetrue_sh+low_accesscomplexity_none_authentication_allprivilegetrue_iot)*100)/(low_accesscomplexity_none_authentication_sh+low_accesscomplexity_none_authentication_iot))))+" % DE VULNERABILIDADES SE OBTIENEN TODOS LOS PRIVILEGIOS")
    print("                       -    EN  EL "+str(float((((low_accesscomplexity_none_authentication_allprivilegefalse_sh+low_accesscomplexity_none_authentication_allprivilegefalse_iot)*100)/(low_accesscomplexity_none_authentication_sh+low_accesscomplexity_none_authentication_iot))))+" % DE VULNERABILIDADES NO SE OBTIENEN TODOS LOS PRIVILEGIOS ")
    print("\n") 
    print("      -    EN  EL "+str(float((((medium_accesscomplexity_sh+medium_accesscomplexity_iot)*100)/(len(df_cve_sh["CVE_Items.impact.baseMetricV2.cvssV2.accessComplexity"])+len(df_cve_iot["CVE_Items.impact.baseMetricV2.cvssV2.accessComplexity"])))))+" % DE VULNERABILIDADES LA COMPLEJIDAD DE ACCESO ES MEDIA. LOS PORCENTAJES DE AUTENTICACIÓN SON LOS SIGUIENTES:  \n")
    print("\n")
if((medium_accesscomplexity_single_authentication_sh+medium_accesscomplexity_single_authentication_iot)>0):
    print("            -    EN  EL "+str(float((((medium_accesscomplexity_single_authentication_sh+medium_accesscomplexity_single_authentication_iot)*100)/(medium_accesscomplexity_sh+medium_accesscomplexity_iot))))+" % DE VULNERABILIDADES LA AUTENTICACIÓN ES SENCILLA. LOS PORCENTAJES DE PRIVILEGIOS OBTENIDOS SON LOS SIGUIENTES: ")
    print("                       -    EN  EL "+str(float((((medium_accesscomplexity_single_authentication_otherprivilegetrue_sh+medium_accesscomplexity_single_authentication_otherprivilegetrue_iot)*100)/(medium_accesscomplexity_single_authentication_sh+medium_accesscomplexity_single_authentication_iot))))+" % DE VULNERABILIDADES SE OBTIENEN OTROS PRIVILEGIOS DISTINTOS A LOS DE USUARIO")
    print("                       -    EN  EL "+str(float((((medium_accesscomplexity_single_authentication_otherprivilegefalse_sh+medium_accesscomplexity_single_authentication_otherprivilegefalse_iot)*100)/(medium_accesscomplexity_single_authentication_sh+medium_accesscomplexity_single_authentication_iot))))+" % DE VULNERABILIDADES NO SE OBTIENEN OTROS PRIVILEGIOS DISTINTOS A LOS DE USUARIO")
    print("\n")
    print("                       -    EN  EL "+str(float((((medium_accesscomplexity_single_authentication_userprivilegetrue_sh+medium_accesscomplexity_single_authentication_userprivilegetrue_iot)*100)/(medium_accesscomplexity_single_authentication_sh+medium_accesscomplexity_single_authentication_iot))))+" % DE VULNERABILIDADES SE OBTIENEN LOS PRIVILEGIOS DE USUARIOS")
    print("                       -    EN  EL "+str(float((((medium_accesscomplexity_single_authentication_userprivilegefalse_sh+medium_accesscomplexity_single_authentication_userprivilegefalse_iot)*100)/(medium_accesscomplexity_single_authentication_sh+medium_accesscomplexity_single_authentication_iot))))+" % DE VULNERABILIDADES NO SE OBTIENEN LOS PRIVILEGIOS DE USUARIOS ")
    print("\n")
    print("                       -    EN  EL "+str(float((((medium_accesscomplexity_single_authentication_allprivilegetrue_sh+medium_accesscomplexity_single_authentication_allprivilegetrue_iot)*100)/(medium_accesscomplexity_single_authentication_sh+medium_accesscomplexity_single_authentication_iot))))+" % DE VULNERABILIDADES SE OBTIENEN TODOS LOS PRIVILEGIOS")
    print("                       -    EN  EL "+str(float((((medium_accesscomplexity_single_authentication_allprivilegefalse_sh+medium_accesscomplexity_single_authentication_allprivilegefalse_iot)*100)/(medium_accesscomplexity_single_authentication_sh+medium_accesscomplexity_single_authentication_iot))))+" % DE VULNERABILIDADES NO SE OBTIENEN TODOS LOS PRIVILEGIOS ")
    print("\n") 
if((medium_accesscomplexity_multiple_authentication_sh+medium_accesscomplexity_multiple_authentication_iot)>0):
    print("            -    EN  EL "+str(float((((medium_accesscomplexity_multiple_authentication_sh+medium_accesscomplexity_multiple_authentication_iot)*100)/(medium_accesscomplexity_sh+medium_accesscomplexity_iot))))+" % DE VULNERABILIDADES LA AUTENTICACIÓN ES MULTIPLE. LOS PORCENTAJES DE PRIVILEGIOS OBTENIDOS SON LOS SIGUIENTES: ")
    print("                       -    EN  EL "+str(float((((medium_accesscomplexity_multiple_authentication_otherprivilegetrue_sh+medium_accesscomplexity_multiple_authentication_otherprivilegetrue_iot)*100)/(medium_accesscomplexity_multiple_authentication_sh+medium_accesscomplexity_multiple_authentication_iot))))+" % DE VULNERABILIDADES SE OBTIENEN OTROS PRIVILEGIOS DISTINTOS A LOS DE USUARIO")
    print("                       -    EN  EL "+str(float((((medium_accesscomplexity_multiple_authentication_otherprivilegefalse_sh+medium_accesscomplexity_multiple_authentication_otherprivilegefalse_iot)*100)/(medium_accesscomplexity_multiple_authentication_sh+medium_accesscomplexity_multiple_authentication_iot))))+" % DE VULNERABILIDADES NO SE OBTIENEN OTROS PRIVILEGIOS DISTINTOS A LOS DE USUARIO")
    print("\n")
    print("                       -    EN  EL "+str(float((((medium_accesscomplexity_multiple_authentication_userprivilegetrue_sh+medium_accesscomplexity_multiple_authentication_userprivilegetrue_iot)*100)/(medium_accesscomplexity_multiple_authentication_sh+medium_accesscomplexity_multiple_authentication_iot))))+" % DE VULNERABILIDADES SE OBTIENEN LOS PRIVILEGIOS DE USUARIOS")
    print("                       -    EN  EL "+str(float((((medium_accesscomplexity_multiple_authentication_userprivilegefalse_sh+medium_accesscomplexity_multiple_authentication_userprivilegefalse_iot)*100)/(medium_accesscomplexity_multiple_authentication_sh+medium_accesscomplexity_multiple_authentication_iot))))+" % DE VULNERABILIDADES NO SE OBTIENEN LOS PRIVILEGIOS DE USUARIOS ")
    print("\n")
    print("                       -    EN  EL "+str(float((((medium_accesscomplexity_multiple_authentication_allprivilegetrue_sh+medium_accesscomplexity_multiple_authentication_allprivilegetrue_iot)*100)/(medium_accesscomplexity_multiple_authentication_sh+medium_accesscomplexity_multiple_authentication_iot))))+" % DE VULNERABILIDADES SE OBTIENEN TODOS LOS PRIVILEGIOS")
    print("                       -    EN  EL "+str(float((((medium_accesscomplexity_multiple_authentication_allprivilegefalse_sh+medium_accesscomplexity_multiple_authentication_allprivilegefalse_iot)*100)/(medium_accesscomplexity_multiple_authentication_sh+medium_accesscomplexity_multiple_authentication_iot))))+" % DE VULNERABILIDADES NO SE OBTIENEN TODOS LOS PRIVILEGIOS ")
    print("\n") 
if((medium_accesscomplexity_none_authentication_sh+medium_accesscomplexity_none_authentication_iot)>0):
    print("            -    EN  EL "+str(float((((medium_accesscomplexity_none_authentication_sh+medium_accesscomplexity_none_authentication_iot)*100)/(medium_accesscomplexity_sh+medium_accesscomplexity_iot))))+" % DE VULNERABILIDADES NO SE REQUIERE AUTENTICACION. LOS PORCENTAJES DE PRIVILEGIOS OBTENIDOS SON LOS SIGUIENTES: ")
    print("                       -    EN  EL "+str(float((((medium_accesscomplexity_none_authentication_otherprivilegetrue_sh+medium_accesscomplexity_none_authentication_otherprivilegetrue_iot)*100)/(medium_accesscomplexity_none_authentication_sh+medium_accesscomplexity_none_authentication_iot))))+" % DE VULNERABILIDADES SE OBTIENEN OTROS PRIVILEGIOS DISTINTOS A LOS DE USUARIO")
    print("                       -    EN  EL "+str(float((((medium_accesscomplexity_none_authentication_otherprivilegefalse_sh+medium_accesscomplexity_none_authentication_otherprivilegefalse_iot)*100)/(medium_accesscomplexity_none_authentication_sh+medium_accesscomplexity_none_authentication_iot))))+" % DE VULNERABILIDADES NO SE OBTIENEN OTROS PRIVILEGIOS DISTINTOS A LOS DE USUARIO")
    print("\n")
    print("                       -    EN  EL "+str(float((((medium_accesscomplexity_none_authentication_userprivilegetrue_sh+medium_accesscomplexity_none_authentication_userprivilegetrue_iot)*100)/(medium_accesscomplexity_none_authentication_sh+medium_accesscomplexity_none_authentication_iot))))+" % DE VULNERABILIDADES SE OBTIENEN LOS PRIVILEGIOS DE USUARIOS")
    print("                       -    EN  EL "+str(float((((medium_accesscomplexity_none_authentication_userprivilegefalse_sh+medium_accesscomplexity_none_authentication_userprivilegefalse_iot)*100)/(medium_accesscomplexity_none_authentication_sh+medium_accesscomplexity_none_authentication_iot))))+" % DE VULNERABILIDADES NO SE OBTIENEN LOS PRIVILEGIOS DE USUARIOS ")
    print("\n")
    print("                       -    EN  EL "+str(float((((medium_accesscomplexity_none_authentication_allprivilegetrue_sh+medium_accesscomplexity_none_authentication_allprivilegetrue_iot)*100)/(medium_accesscomplexity_none_authentication_sh+medium_accesscomplexity_none_authentication_iot))))+" % DE VULNERABILIDADES SE OBTIENEN TODOS LOS PRIVILEGIOS")
    print("                       -    EN  EL "+str(float((((medium_accesscomplexity_none_authentication_allprivilegefalse_sh+medium_accesscomplexity_none_authentication_allprivilegefalse_iot)*100)/(medium_accesscomplexity_none_authentication_sh+medium_accesscomplexity_none_authentication_iot))))+" % DE VULNERABILIDADES NO SE OBTIENEN TODOS LOS PRIVILEGIOS ")
    print("\n") 
	
	
	















































	
	
	
	
	
	