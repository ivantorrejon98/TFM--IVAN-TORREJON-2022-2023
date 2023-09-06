

import pandas as pd
from datetime import datetime,timedelta



#Abro los ficheros con los que voy a tratar




df_vulnibm_iot = pd.read_excel('vulnerabilidades_ibm_iot_2023.xlsx')

#Variable para almacenar el numero total de valores de privilegios requeridos
count_vulnibm_iot_privileges_required=0
#Variable para almacenar el numero total de valores de un valor especifico de privilegios requeridos
count_vulnibm_iot_highprivreq=0
#Variable para almacenar el contador de valores de interacción de usuario según un valor específico de privilegios requeridos
count_vulnibm_iot_highprivreq_userrequired=0
count_vulnibm_iot_highprivreq_usernorequired=0

count_vulnibm_iot_lowprivreq=0
count_vulnibm_iot_lowprivreq_userrequired=0
count_vulnibm_iot_lowprivreq_usernorequired=0


#Comprobamos el contenido de PRIVILEGIOS REQUERIDOS
for r in range(0,len(df_vulnibm_iot["x_xfe_cvss_privilegesrequired"])):  
    #Obtengo el valor de privilegios requeridos
    if(isinstance(df_vulnibm_iot["x_xfe_cvss_privilegesrequired"][r],str)):
        aux_str=str(df_vulnibm_iot["x_xfe_cvss_privilegesrequired"][r].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'",""))
        #Si el valor de privilegios esta definido
        if(aux_str!='NONE' or aux_str!='None'):
            count_vulnibm_iot_privileges_required+=1
            #Comprobamos el valor de privilegios requeridos
            if('High' in aux_str):
                count_vulnibm_iot_highprivreq+=1
                #Comprobamos si se requiere la interaccion del usuario
                if(df_vulnibm_iot["x_xfe_cvss_userinteraction"][r] =='Required'):
                    count_vulnibm_iot_highprivreq_userrequired+=1
                else:
                    count_vulnibm_iot_highprivreq_usernorequired+=1

            elif('Low' in aux_str):
                count_vulnibm_iot_lowprivreq+=1
                if(df_vulnibm_iot["x_xfe_cvss_userinteraction"][r] =='Required'):
                    count_vulnibm_iot_lowprivreq_userrequired+=1
                else:
                    count_vulnibm_iot_lowprivreq_usernorequired+=1
                
                
                
                
print("**********************************************ESTADÍSTICAS PRIVILEGIOS REQUERIDOS/INTERACCION DE USUARIO VULNERABILIDADES IBM PARTE IOT**********************************************")
print("\n")                            
print("\n")
print(" DE UN TOTAL DE "+str(count_vulnibm_iot_privileges_required)+" VULNERABILIDADES CON PRIVILEGIOS DEFINIDOS:\n") 
print("\n")
print("   - LAS ESTADISTICAS DE VALORES DE PRIVILEGIOS REQUERIDOS SON LAS SIGUIENTES:  \n")
print("      -    EN  "+str(count_vulnibm_iot_highprivreq)+" VULNERABILIDADES SE REQUIERE UN NIVEL ALTO DE PRIVILEGIOS, LAS ESTADÍSTICAS DE INTERACCION DE USUARIO SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_highprivreq_userrequired)+" VULNERABILIDADES SE REQUIERE INTERACCION DE USUARIO \n")
print("            -    EN  "+str(count_vulnibm_iot_highprivreq_usernorequired)+" VULNERABILIDADES NO SE REQUIERE INTERACCION DE USUARIO \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_lowprivreq)+" VULNERABILIDADES SE REQUIERE UN NIVEL BAJO DE PRIVILEGIOS, LAS ESTADÍSTICAS DE INTERACCION DE USUARIO SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_lowprivreq_userrequired)+" VULNERABILIDADES SE REQUIERE INTERACCION DE USUARIO \n")
print("            -    EN  "+str(count_vulnibm_iot_lowprivreq_usernorequired)+" VULNERABILIDADES NO SE REQUIERE INTERACCION DE USUARIO \n")
print("\n")


print("**********************************************PORCENTAJE PRIVILEGIOS REQUERIDOS/INTERACCION DE USUARIO VULNERABILIDADES IBM PARTE IOT**********************************************")
print("\n")                            
print("\n")
print(" DE UN TOTAL DE "+str(count_vulnibm_iot_privileges_required)+" VULNERABILIDADES CON PRIVILEGIOS DEFINIDOS :\n") 
print("\n")
print("   - LOS PORCENTAJES DE VALORES DE PRIVILEGIOS REQUERIDOS SON LOS SIGUIENTES:  \n")
print("      -    EN EL  "+str(float(((count_vulnibm_iot_highprivreq*100)/count_vulnibm_iot_privileges_required)))+" % DE VULNERABILIDADES SE REQUIERE UN NIVEL ALTO DE PRIVILEGIOS, LOS PORCENTAJES DE INTERACCION DE USUARIO SON LOS SIGUIENTES :  \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_highprivreq_userrequired*100)/count_vulnibm_iot_highprivreq)))+" % DE VULNERABILIDADES SE REQUIERE INTERACCION DE USUARIO \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_highprivreq_usernorequired*100)/count_vulnibm_iot_highprivreq)))+" % DE VULNERABILIDADES NO SE REQUIERE INTERACCION DE USUARIO \n")
print("\n")
print("      -    EN EL  "+str(float(((count_vulnibm_iot_lowprivreq*100)/count_vulnibm_iot_privileges_required)))+" % DE VULNERABILIDADES SE REQUIERE UN NIVEL BAJO DE PRIVILEGIOS, LOS PORCENTAJES DE INTERACCION DE USUARIO SON LOS SIGUIENTES :  \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_lowprivreq_userrequired*100)/count_vulnibm_iot_lowprivreq)))+" % DE VULNERABILIDADES SE REQUIERE INTERACCION DE USUARIO \n")
print("            -    EN EL  "+str(float(((count_vulnibm_iot_lowprivreq_usernorequired*100)/count_vulnibm_iot_lowprivreq)))+" % DE VULNERABILIDADES NO SE REQUIERE INTERACCION DE USUARIO \n")
print("\n")


#Abro los ficheros con los que voy a tratar




df_vulnibm_sh = pd.read_excel('vulnerabilidades_ibm_smart_home_2023.xlsx')
#Variable para almacenar el contador de valores totales de privilegios requeridos
count_vulnibm_sh_privileges_required=0
#Variable para almacenar el contador de valores de un nivel de privilegios requeridos especifico
count_vulnibm_sh_highprivreq=0
#Variable para almacenar el contador de valores de interaccion de usuario requerida segun un nivel especifico de privilegios requeridos
count_vulnibm_sh_highprivreq_userrequired=0
count_vulnibm_sh_highprivreq_usernorequired=0

count_vulnibm_sh_lowprivreq=0
count_vulnibm_sh_lowprivreq_userrequired=0
count_vulnibm_sh_lowprivreq_usernorequired=0


#Comprobamos el contenido de PRIVILEGIOS REQUERIDOS
for r in range(0,len(df_vulnibm_sh["x_xfe_cvss_privilegesrequired"])):  
    #Compruebo el nivel de privilegios requeridos
    if(isinstance(df_vulnibm_sh["x_xfe_cvss_privilegesrequired"][r],str)):
        aux_str=df_vulnibm_sh["x_xfe_cvss_privilegesrequired"][r].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
        #Compruebo que el valor de privilegios requeridos no sea nulo
        if(aux_str!='NONE' or aux_str!='None'):
            count_vulnibm_sh_privileges_required+=1
            #Compruebo el valor de privilegios requeridos
            if('High' in aux_str):
                count_vulnibm_sh_highprivreq+=1
                #Compruebo el valor de interaccion de usuario
                if(df_vulnibm_sh["x_xfe_cvss_userinteraction"][r] =='Required' ):
                    count_vulnibm_sh_highprivreq_userrequired+=1
                else:
                    count_vulnibm_sh_highprivreq_usernorequired+=1

            elif('Low' in aux_str):
                count_vulnibm_sh_lowprivreq+=1
                if(df_vulnibm_sh["x_xfe_cvss_userinteraction"][r] =='Required' ):
                    count_vulnibm_sh_lowprivreq_userrequired+=1
                else:
                    count_vulnibm_sh_lowprivreq_usernorequired+=1

                
                
print("**********************************************ESTADÍSTICAS PRIVILEGIOS REQUERIDOS/INTERACCION DE USUARIO VULNERABILIDADES IBM PARTE SMART HOME**********************************************")
print("\n")                            
print("\n")
print(" DE UN TOTAL DE "+str(count_vulnibm_sh_privileges_required)+" VULNERABILIDADES CON PRIVILEGIOS DEFINIDOS:\n") 
print("\n")
print("   - LAS ESTADISTICAS DE VALORES DE PRIVILEGIOS REQUERIDOS SON LAS SIGUIENTES:  \n")
print("      -    EN  "+str(count_vulnibm_sh_highprivreq)+" VULNERABILIDADES SE REQUIERE UN NIVEL ALTO DE PRIVILEGIOS, LAS ESTADÍSTICAS DE INTERACCION DE USUARIO SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_sh_highprivreq_userrequired)+" VULNERABILIDADES SE REQUIERE INTERACCION DE USUARIO \n")
print("            -    EN  "+str(count_vulnibm_sh_highprivreq_usernorequired)+" VULNERABILIDADES NO SE REQUIERE INTERACCION DE USUARIO \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_sh_lowprivreq)+" VULNERABILIDADES SE REQUIERE UN NIVEL BAJO DE PRIVILEGIOS, LAS ESTADÍSTICAS DE INTERACCION DE USUARIO SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_sh_lowprivreq_userrequired)+" VULNERABILIDADES SE REQUIERE INTERACCION DE USUARIO \n")
print("            -    EN  "+str(count_vulnibm_sh_lowprivreq_usernorequired)+" VULNERABILIDADES NO SE REQUIERE INTERACCION DE USUARIO \n")
print("\n")


print("**********************************************PORCENTAJE PRIVILEGIOS REQUERIDOS/INTERACCION DE USUARIO VULNERABILIDADES IBM PARTE SMART HOME**********************************************")
print("\n")                            
print("\n")
print(" DE UN TOTAL DE "+str(count_vulnibm_sh_privileges_required)+" VULNERABILIDADES CON PRIVILEGIOS DEFINIDOS :\n") 
print("\n")
print("   - LOS PORCENTAJES DE VALORES DE PRIVILEGIOS REQUERIDOS SON LOS SIGUIENTES:  \n")
print("      -    EN EL  "+str(float(((count_vulnibm_sh_highprivreq*100)/count_vulnibm_sh_privileges_required)))+" % DE VULNERABILIDADES SE REQUIERE UN NIVEL ALTO DE PRIVILEGIOS, LOS PORCENTAJES DE INTERACCION DE USUARIO SON LOS SIGUIENTES :  \n")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_highprivreq_userrequired*100)/count_vulnibm_sh_highprivreq)))+" % DE VULNERABILIDADES SE REQUIERE INTERACCION DE USUARIO \n")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_highprivreq_usernorequired*100)/count_vulnibm_sh_highprivreq)))+" % DE VULNERABILIDADES NO SE REQUIERE INTERACCION DE USUARIO \n")
print("\n")
print("      -    EN EL  "+str(float(((count_vulnibm_sh_lowprivreq*100)/count_vulnibm_sh_privileges_required)))+" % DE VULNERABILIDADES SE REQUIERE UN NIVEL BAJO DE PRIVILEGIOS, LOS PORCENTAJES DE INTERACCION DE USUARIO SON LOS SIGUIENTES :  \n")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_lowprivreq_userrequired*100)/count_vulnibm_sh_lowprivreq)))+" % DE VULNERABILIDADES SE REQUIERE INTERACCION DE USUARIO \n")
print("            -    EN EL  "+str(float(((count_vulnibm_sh_lowprivreq_usernorequired*100)/count_vulnibm_sh_lowprivreq)))+" % DE VULNERABILIDADES NO SE REQUIERE INTERACCION DE USUARIO \n")
print("\n")
print("\n")

print("**********************************************ESTADÍSTICAS PRIVILEGIOS REQUERIDOS/INTERACCION DE USUARIO VULNERABILIDADES IBM PARTE IOT Y SMART HOME CONJUNTAS**********************************************")
print("\n")                            
print("\n")
print(" DE UN TOTAL DE "+str(count_vulnibm_sh_privileges_required+count_vulnibm_iot_privileges_required)+" VULNERABILIDADES CON PRIVILEGIOS DEFINIDOS:\n") 
print("\n")
print("   - LAS ESTADISTICAS DE VALORES DE PRIVILEGIOS REQUERIDOS SON LAS SIGUIENTES:  \n")
print("      -    EN  "+str(count_vulnibm_sh_highprivreq+count_vulnibm_iot_highprivreq)+" VULNERABILIDADES SE REQUIERE UN NIVEL ALTO DE PRIVILEGIOS, LAS ESTADÍSTICAS DE INTERACCION DE USUARIO SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_sh_highprivreq_userrequired+count_vulnibm_iot_highprivreq_userrequired)+" VULNERABILIDADES SE REQUIERE INTERACCION DE USUARIO \n")
print("            -    EN  "+str(count_vulnibm_sh_highprivreq_usernorequired+count_vulnibm_iot_highprivreq_usernorequired)+" VULNERABILIDADES NO SE REQUIERE INTERACCION DE USUARIO \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_sh_lowprivreq+count_vulnibm_iot_lowprivreq)+" VULNERABILIDADES SE REQUIERE UN NIVEL BAJO DE PRIVILEGIOS, LAS ESTADÍSTICAS DE INTERACCION DE USUARIO SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_sh_lowprivreq_userrequired+count_vulnibm_iot_lowprivreq_userrequired)+" VULNERABILIDADES SE REQUIERE INTERACCION DE USUARIO \n")
print("            -    EN  "+str(count_vulnibm_sh_lowprivreq_usernorequired+count_vulnibm_iot_lowprivreq_usernorequired)+" VULNERABILIDADES NO SE REQUIERE INTERACCION DE USUARIO \n")
print("\n")
print("\n")
print("\n")
print("**********************************************PORCENTAJES PRIVILEGIOS REQUERIDOS/INTERACCION DE USUARIO VULNERABILIDADES IBM PARTE IOT Y SMART HOME CONJUNTAS**********************************************")
print("\n")                            
print("\n")
print(" DE UN TOTAL DE "+str(count_vulnibm_iot_privileges_required+count_vulnibm_sh_privileges_required)+" VULNERABILIDADES CON PRIVILEGIOS DEFINIDOS:\n")
print("\n")
print("   - LOS PORCENTAJES DE VALORES DE PRIVILEGIOS REQUERIDOS SON LOS SIGUIENTES:  \n")
print("      -    EN EL "+str(float((((count_vulnibm_iot_highprivreq+count_vulnibm_sh_highprivreq)*100)/(count_vulnibm_iot_privileges_required+count_vulnibm_sh_privileges_required))))+" % DE VULNERABILIDADES EL NIVEL DE PRIVILEGIOS REQUERIDOS ES ALTO, LOS PORCENTAJES DE INTERACCION DE USUARIO SON LOS SIGUIENTES :  \n")
print("            -    EN EL"+str(float((((count_vulnibm_iot_highprivreq_userrequired+count_vulnibm_sh_highprivreq_userrequired)*100)/(count_vulnibm_iot_highprivreq+count_vulnibm_sh_highprivreq))))+" % DE VULNERABILIDADES SE REQUIERE INTERACCION DE USUARIO \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_highprivreq_usernorequired+count_vulnibm_sh_highprivreq_usernorequired)*100)/(count_vulnibm_iot_highprivreq+count_vulnibm_sh_highprivreq))))+" % DE VULNERABILIDADES NO SE REQUIERE INTERACCION DE USUARIO \n")
print("\n")
print("      -    EN EL "+str(float((((count_vulnibm_iot_lowprivreq+count_vulnibm_sh_lowprivreq)*100)/(count_vulnibm_iot_privileges_required+count_vulnibm_sh_privileges_required))))+" % DE VULNERABILIDADES EL NIVEL DE PRIVILEGIOS REQUERIDOS ES BAJO, LOS PORCENTAJES DE INTERACCION DE USUARIO  SON LOS SIGUIENTES :  \n")
print("            -    EN EL"+str(float((((count_vulnibm_iot_lowprivreq_userrequired+count_vulnibm_sh_lowprivreq_userrequired)*100)/(count_vulnibm_iot_lowprivreq+count_vulnibm_sh_lowprivreq))))+" % DE VULNERABILIDADES SE REQUIERE INTERACCION DE USUARIO  \n")
print("            -    EN EL "+str(float((((count_vulnibm_iot_lowprivreq_usernorequired+count_vulnibm_sh_lowprivreq_usernorequired)*100)/(count_vulnibm_iot_lowprivreq+count_vulnibm_sh_lowprivreq))))+" % DE VULNERABILIDADES NO SE REQUIERE INTERACCION DE USUARIO \n")
print("\n")















































































