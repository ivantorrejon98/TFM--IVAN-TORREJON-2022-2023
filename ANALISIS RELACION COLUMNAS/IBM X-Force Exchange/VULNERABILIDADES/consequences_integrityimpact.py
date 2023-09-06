
import pandas as pd
from datetime import datetime,timedelta



#Abro los ficheros con los que voy a tratar




df_vulnibm_iot = pd.read_excel('vulnerabilidades_ibm_iot_2023.xlsx')

#Variables donde almacenare el valor total de consecuencias
count_conseq_vulnibm_iot=0
#Variables para almacenar el impacto de INTEGRIDAD dada una consecuencia concreto
count_obtaininfoconseq_highintimpact_vulnibm_iot=0
count_obtaininfoconseq_lowintimpact_vulnibm_iot=0
count_obtaininfoconseq_mediumintimpact_vulnibm_iot=0
count_obtaininfoconseq_vulnibm_iot=0
#Variable para almacenar el numero total de valores para los que el impacto de INTEGRIDAD viene especificado para una consecuencia concreta
count_obtaininfoconseq_vulnibm_iot_specified=0

count_xss_conseq_highintimpact_vulnibm_iot=0
count_xss_conseq_lowintimpact_vulnibm_iot=0
count_xss_conseq_mediumintimpact_vulnibm_iot=0
count_xss_conseq_vulnibm_iot=0
count_xss_conseq_vulnibm_iot_specified=0

count_gainacc_conseq_highintimpact_vulnibm_iot=0
count_gainacc_conseq_lowintimpact_vulnibm_iot=0
count_gainacc_conseq_mediumintimpact_vulnibm_iot=0
count_gainacc_conseq_vulnibm_iot=0
count_gainacc_conseq_vulnibm_iot_specified=0

count_gainpriv_conseq_highintimpact_vulnibm_iot=0
count_gainpriv_conseq_lowintimpact_vulnibm_iot=0
count_gainpriv_conseq_mediumintimpact_vulnibm_iot=0
count_gainpriv_conseq_vulnibm_iot=0
count_gainpriv_conseq_vulnibm_iot_specified=0

count_denialofserv_conseq_highintimpact_vulnibm_iot=0
count_denialofserv_conseq_lowintimpact_vulnibm_iot=0
count_denialofserv_conseq_mediumintimpact_vulnibm_iot=0
count_denialofserv_conseq_vulnibm_iot=0
count_denialofserv_conseq_vulnibm_iot_specified=0

count_bypassec_conseq_highintimpact_vulnibm_iot=0
count_bypassec_conseq_lowintimpact_vulnibm_iot=0
count_bypassec_conseq_mediumintimpact_vulnibm_iot=0
count_bypassec_conseq_vulnibm_iot=0
count_bypassec_conseq_vulnibm_iot_specified=0

count_filemani_conseq_highintimpact_vulnibm_iot=0
count_filemani_conseq_lowintimpact_vulnibm_iot=0
count_filemani_conseq_mediumintimpact_vulnibm_iot=0
count_filemani_conseq_vulnibm_iot=0
count_filemani_conseq_vulnibm_iot_specified=0


count_other_conseq_highintimpact_vulnibm_iot=0
count_other_conseq_lowintimpact_vulnibm_iot=0
count_other_conseq_mediumintimpact_vulnibm_iot=0
count_other_conseq_vulnibm_iot=0
count_other_conseq_vulnibm_iot_specified=0

#Recorro los valores de CONSECUENCIAS y aumento los contadores segun su valor

for r in range(0,len(df_vulnibm_iot["x_xfe_consequences"])):                       
    aux_str=df_vulnibm_iot["x_xfe_consequences"][r].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
    if(aux_str!='NONE' or aux_str!='None'):
        count_conseq_vulnibm_iot+=1
        #Compruebo el valor de consecuencia
        if(('ObtainInformation' in aux_str) or ('Obtain Information' in aux_str)):
            count_obtaininfoconseq_vulnibm_iot+=1
            #Compruebo el valor de impacto de INTEGRIDAD
            if(df_vulnibm_iot["x_xfe_cvss_integrity_impact"][r]=='High'):
                count_obtaininfoconseq_vulnibm_iot_specified+=1
                count_obtaininfoconseq_highintimpact_vulnibm_iot+=1
            elif(df_vulnibm_iot["x_xfe_cvss_integrity_impact"][r]=='Low'):
                count_obtaininfoconseq_vulnibm_iot_specified+=1
                count_obtaininfoconseq_lowintimpact_vulnibm_iot+=1
            elif(df_vulnibm_iot["x_xfe_cvss_integrity_impact"][r]=='Medium'):
                count_obtaininfoconseq_vulnibm_iot_specified+=1
                count_obtaininfoconseq_mediumintimpact_vulnibm_iot+=1
        elif('Scripting' in aux_str):
            count_xss_conseq_vulnibm_iot+=1
            if(df_vulnibm_iot["x_xfe_cvss_integrity_impact"][r]=='High'):
                count_xss_conseq_vulnibm_iot_specified+=1
                count_xss_conseq_highintimpact_vulnibm_iot+=1
            elif(df_vulnibm_iot["x_xfe_cvss_integrity_impact"][r]=='Low'):
                count_xss_conseq_vulnibm_iot_specified+=1
                count_xss_conseq_lowintimpact_vulnibm_iot+=1
            elif(df_vulnibm_iot["x_xfe_cvss_integrity_impact"][r]=='Medium'):
                count_xss_conseq_vulnibm_iot_specified+=1
                count_xss_conseq_mediumintimpact_vulnibm_iot+=1
                
        elif('Access' in aux_str):
            count_gainacc_conseq_vulnibm_iot+=1
            if(df_vulnibm_iot["x_xfe_cvss_integrity_impact"][r]=='High'):
                count_gainacc_conseq_vulnibm_iot_specified+=1
                count_gainacc_conseq_highintimpact_vulnibm_iot+=1
            elif(df_vulnibm_iot["x_xfe_cvss_integrity_impact"][r]=='Low'):
                count_gainacc_conseq_vulnibm_iot_specified+=1
                count_gainacc_conseq_lowintimpact_vulnibm_iot+=1
            elif(df_vulnibm_iot["x_xfe_cvss_integrity_impact"][r]=='Medium'):
                count_gainacc_conseq_vulnibm_iot_specified+=1
                count_gainacc_conseq_mediumintimpact_vulnibm_iot+=1
                
        elif('Privilege' in aux_str):
            count_gainpriv_conseq_vulnibm_iot+=1
            if(df_vulnibm_iot["x_xfe_cvss_integrity_impact"][r]=='High'):
                count_gainpriv_conseq_vulnibm_iot_specified+=1
                count_gainpriv_conseq_highintimpact_vulnibm_iot+=1
            elif(df_vulnibm_iot["x_xfe_cvss_integrity_impact"][r]=='Low'):
                count_gainpriv_conseq_vulnibm_iot_specified+=1
                count_gainpriv_conseq_lowintimpact_vulnibm_iot+=1
            elif(df_vulnibm_iot["x_xfe_cvss_integrity_impact"][r]=='Medium'):
                count_gainpriv_conseq_vulnibm_iot_specified+=1
                count_gainpriv_conseq_mediumintimpact_vulnibm_iot+=1
                
        elif('Denial' in aux_str):
            count_denialofserv_conseq_vulnibm_iot+=1
            if(df_vulnibm_iot["x_xfe_cvss_integrity_impact"][r]=='High'):
                count_denialofserv_conseq_vulnibm_iot_specified+=1
                count_denialofserv_conseq_highintimpact_vulnibm_iot+=1
            elif(df_vulnibm_iot["x_xfe_cvss_integrity_impact"][r]=='Low'):
                count_denialofserv_conseq_vulnibm_iot_specified+=1
                count_denialofserv_conseq_lowintimpact_vulnibm_iot+=1
            elif(df_vulnibm_iot["x_xfe_cvss_integrity_impact"][r]=='Medium'):
                count_denialofserv_conseq_vulnibm_iot_specified+=1
                count_denialofserv_conseq_mediumintimpact_vulnibm_iot+=1
        
        elif('Bypass' in aux_str):
            count_bypassec_conseq_vulnibm_iot+=1
            if(df_vulnibm_iot["x_xfe_cvss_integrity_impact"][r]=='High'):
                count_bypassec_conseq_vulnibm_iot_specified+=1
                count_bypassec_conseq_highintimpact_vulnibm_iot+=1
            elif(df_vulnibm_iot["x_xfe_cvss_integrity_impact"][r]=='Low'):
                count_bypassec_conseq_vulnibm_iot_specified+=1
                count_bypassec_conseq_lowintimpact_vulnibm_iot+=1
            elif(df_vulnibm_iot["x_xfe_cvss_integrity_impact"][r]=='Medium'):
                count_bypassec_conseq_vulnibm_iot_specified+=1
                count_bypassec_conseq_mediumintimpact_vulnibm_iot+=1
                
        elif('Manipulation' in aux_str):
            count_filemani_conseq_vulnibm_iot+=1
            if(df_vulnibm_iot["x_xfe_cvss_integrity_impact"][r]=='High'):
                count_filemani_conseq_vulnibm_iot_specified+=1
                count_filemani_conseq_highintimpact_vulnibm_iot+=1
            elif(df_vulnibm_iot["x_xfe_cvss_integrity_impact"][r]=='Low'):
                count_filemani_conseq_vulnibm_iot_specified+=1
                count_filemani_conseq_lowintimpact_vulnibm_iot+=1
            elif(df_vulnibm_iot["x_xfe_cvss_integrity_impact"][r]=='Medium'):
                count_filemani_conseq_vulnibm_iot_specified+=1
                count_filemani_conseq_mediumintimpact_vulnibm_iot+=1
                
        elif('Other' in aux_str):
            count_other_conseq_vulnibm_iot+=1
            if(df_vulnibm_iot["x_xfe_cvss_integrity_impact"][r]=='High'):
                count_other_conseq_vulnibm_iot_specified+=1
                count_other_conseq_highintimpact_vulnibm_iot+=1
            elif(df_vulnibm_iot["x_xfe_cvss_integrity_impact"][r]=='Low'):
                count_other_conseq_vulnibm_iot_specified+=1
                count_other_conseq_lowintimpact_vulnibm_iot+=1
            elif(df_vulnibm_iot["x_xfe_cvss_integrity_impact"][r]=='Medium'):
                count_other_conseq_vulnibm_iot_specified+=1
                count_other_conseq_mediumintimpact_vulnibm_iot+=1
                
        
                
        
                
                
                
                
                
                
                
                
                
                
                
print("*******************ESTADÍSTICAS CONSECUENCIAS DE EXPLOTACION VULNERABILIDAD/IMPACTO DE INTEGRIDAD VULNERABILIDADES IBM PARTE IOT*******************")
print("\n")                            
print("\n")
print(" DE UN TOTAL DE "+str(count_conseq_vulnibm_iot)+" VULNERABILIDADES DONDE LA CONSECUENCIA VIENE ESPECIFICADA:\n") 
print("\n")
print("   - LAS ESTADISTICAS DE CONSECUENCIAS SON LAS SIGUIENTES:  \n")
print("      -    EN  "+str(count_obtaininfoconseq_vulnibm_iot)+" VULNERABILIDADES LA CONSECUENCIA ES LA OBTENCION DE INFORMACION. EL IMPACTO DE INTEGRIDAD VIENE ESPECIFICADO ES  "+str(count_obtaininfoconseq_vulnibm_iot_specified)+" VULNERABILIDADES. LAS ESTADÍSTICAS DE IMPACTO DE INTEGRIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_obtaininfoconseq_highintimpact_vulnibm_iot)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
print("            -    EN  "+str(count_obtaininfoconseq_lowintimpact_vulnibm_iot)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
print("            -    EN  "+str(count_obtaininfoconseq_mediumintimpact_vulnibm_iot)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO\n")
print("\n")
print("      -    EN  "+str(count_xss_conseq_vulnibm_iot)+" VULNERABILIDADES LA CONSECUENCIA ES UN ATAQUE DE CROSS-SITE SCRIPTING. EL IMPACTO DE INTEGRIDAD VIENE ESPECIFICADO ES  "+str(count_xss_conseq_vulnibm_iot_specified)+" VULNERABILIDADES. LAS ESTADÍSTICAS DE IMPACTO DE INTEGRIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_xss_conseq_highintimpact_vulnibm_iot)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
print("            -    EN  "+str(count_xss_conseq_lowintimpact_vulnibm_iot)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
print("            -    EN  "+str(count_xss_conseq_mediumintimpact_vulnibm_iot)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO\n")
print("\n")
print("      -    EN  "+str(count_gainacc_conseq_vulnibm_iot)+" VULNERABILIDADES LA CONSECUENCIA ES LA OBTENCIÓN DE ACCESO. EL IMPACTO DE INTEGRIDAD VIENE ESPECIFICADO ES  "+str(count_gainacc_conseq_vulnibm_iot_specified)+" VULNERABILIDADES. LAS ESTADÍSTICAS DE IMPACTO DE INTEGRIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_gainacc_conseq_highintimpact_vulnibm_iot)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
print("            -    EN  "+str(count_gainacc_conseq_lowintimpact_vulnibm_iot)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
print("            -    EN  "+str(count_gainacc_conseq_mediumintimpact_vulnibm_iot)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO\n")
print("\n")
print("      -    EN  "+str(count_gainpriv_conseq_vulnibm_iot)+" VULNERABILIDADES LA CONSECUENCIA ES LA OBTENCIÓN DE PRIVILEGIOS. EL IMPACTO DE INTEGRIDAD VIENE ESPECIFICADO ES  "+str(count_gainpriv_conseq_vulnibm_iot_specified)+" VULNERABILIDADES. LAS ESTADÍSTICAS DE IMPACTO DE INTEGRIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_gainpriv_conseq_highintimpact_vulnibm_iot)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
print("            -    EN  "+str(count_gainpriv_conseq_lowintimpact_vulnibm_iot)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
print("            -    EN  "+str(count_gainpriv_conseq_mediumintimpact_vulnibm_iot)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO\n")
print("\n")
print("      -    EN  "+str(count_denialofserv_conseq_vulnibm_iot)+" VULNERABILIDADES LA CONSECUENCIA ES UNA DENEGACIÓN DE SERVICIO. EL IMPACTO DE INTEGRIDAD VIENE ESPECIFICADO ES  "+str(count_denialofserv_conseq_vulnibm_iot_specified)+" VULNERABILIDADES. LAS ESTADÍSTICAS DE IMPACTO DE INTEGRIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_denialofserv_conseq_highintimpact_vulnibm_iot)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
print("            -    EN  "+str(count_denialofserv_conseq_lowintimpact_vulnibm_iot)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
print("            -    EN  "+str(count_denialofserv_conseq_mediumintimpact_vulnibm_iot)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO\n")
print("\n")
print("      -    EN  "+str(count_filemani_conseq_vulnibm_iot)+" VULNERABILIDADES LA CONSECUENCIA ES LA MANIPULACIÓN DE FICHEROS. EL IMPACTO DE INTEGRIDAD VIENE ESPECIFICADO ES  "+str(count_filemani_conseq_vulnibm_iot_specified)+" VULNERABILIDADES. LAS ESTADÍSTICAS DE IMPACTO DE INTEGRIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_filemani_conseq_highintimpact_vulnibm_iot)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
print("            -    EN  "+str(count_filemani_conseq_lowintimpact_vulnibm_iot)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
print("            -    EN  "+str(count_filemani_conseq_mediumintimpact_vulnibm_iot)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO\n")
print("\n")
print("      -    EN  "+str(count_other_conseq_vulnibm_iot)+" VULNERABILIDADES LA CONSECUENCIA ES OTRA DISTINTA A LAS ANTERIORES. EL IMPACTO DE INTEGRIDAD VIENE ESPECIFICADO ES  "+str(count_other_conseq_vulnibm_iot_specified)+" VULNERABILIDADES. LAS ESTADÍSTICAS DE IMPACTO DE INTEGRIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_other_conseq_highintimpact_vulnibm_iot)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
print("            -    EN  "+str(count_other_conseq_lowintimpact_vulnibm_iot)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
print("            -    EN  "+str(count_other_conseq_mediumintimpact_vulnibm_iot)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO\n")
print("\n")






print("*******************PORCENTAJES CONSECUENCIAS DE EXPLOTACION VULNERABILIDAD/IMPACTO DE INTEGRIDAD VULNERABILIDADES IBM IOT *******************")
print("\n")                            
print("\n")
print(" DE UN TOTAL DE "+str(count_conseq_vulnibm_iot)+" VULNERABILIDADES :\n") 
print("\n")
print("   - LOS PORCENTAJES DE CONSECUENCIAS SON LOS SIGUIENTES:  \n")
if(count_obtaininfoconseq_vulnibm_iot>0):
    print("      -    EN EL "+str(float((count_obtaininfoconseq_vulnibm_iot*100)/count_conseq_vulnibm_iot))+" % DE VULNERABILIDADES LA CONSECUENCIA ES LA OBTENCION DE INFORMACION. EL IMPACTO DE INTEGRIDAD VIENE ESPECIFICADO EN EL "+str(float((count_obtaininfoconseq_vulnibm_iot_specified*100)/count_obtaininfoconseq_vulnibm_iot))+" % DE ELLAS. LOS PORCENTAJES DE IMPACTO DE INTEGRIDAD SON LOS SIGUIENTES :  \n")
    print("            -    EN EL "+str(float((count_obtaininfoconseq_highintimpact_vulnibm_iot*100)/count_obtaininfoconseq_vulnibm_iot))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
    print("            -    EN EL "+str(float((count_obtaininfoconseq_lowintimpact_vulnibm_iot*100)/count_obtaininfoconseq_vulnibm_iot))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
    print("            -    EN EL "+str(float((count_obtaininfoconseq_mediumintimpact_vulnibm_iot*100)/count_obtaininfoconseq_vulnibm_iot))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO  \n")
    print("\n")
if(count_xss_conseq_vulnibm_iot>0):
    print("      -    EN EL "+str(float((count_xss_conseq_vulnibm_iot*100)/count_conseq_vulnibm_iot))+" % DE VULNERABILIDADES LA CONSECUENCIA ES UN ATAQUE DE CROSS-SITE SCRIPTING. EL IMPACTO DE INTEGRIDAD VIENE ESPECIFICADO EN EL "+str(float((count_xss_conseq_vulnibm_iot_specified*100)/count_xss_conseq_vulnibm_iot))+" % DE ELLAS. LOS PORCENTAJES DE IMPACTO DE INTEGRIDAD SON LOS SIGUIENTES :  \n")
    print("            -    EN EL "+str(float((count_xss_conseq_highintimpact_vulnibm_iot*100)/count_xss_conseq_vulnibm_iot))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
    print("            -    EN EL "+str(float((count_xss_conseq_lowintimpact_vulnibm_iot*100)/count_xss_conseq_vulnibm_iot))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
    print("            -    EN EL "+str(float((count_xss_conseq_mediumintimpact_vulnibm_iot*100)/count_xss_conseq_vulnibm_iot))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO  \n")
    print("\n")
if(count_gainacc_conseq_vulnibm_iot>0):
    print("      -    EN EL "+str(float((count_gainacc_conseq_vulnibm_iot*100)/count_conseq_vulnibm_iot))+" % DE VULNERABILIDADES LA CONSECUENCIA ES LA OBTENCIÓN DE ACCESO. EL IMPACTO DE INTEGRIDAD VIENE ESPECIFICADO EN EL "+str(float((count_gainacc_conseq_vulnibm_iot_specified*100)/count_gainacc_conseq_vulnibm_iot))+" % DE ELLAS. LOS PORCENTAJES DE IMPACTO DE INTEGRIDAD SON LOS SIGUIENTES :  \n")
    print("            -    EN EL "+str(float((count_gainacc_conseq_highintimpact_vulnibm_iot*100)/count_gainacc_conseq_vulnibm_iot))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
    print("            -    EN EL "+str(float((count_gainacc_conseq_lowintimpact_vulnibm_iot*100)/count_gainacc_conseq_vulnibm_iot))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
    print("            -    EN EL "+str(float((count_gainacc_conseq_mediumintimpact_vulnibm_iot*100)/count_gainacc_conseq_vulnibm_iot))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO  \n")
    print("\n")
if(count_gainpriv_conseq_vulnibm_iot>0):
    print("      -    EN EL "+str(float((count_gainpriv_conseq_vulnibm_iot*100)/count_conseq_vulnibm_iot))+" % DE VULNERABILIDADES LA CONSECUENCIA ES LA OBTENCIÓN DE PRIVILEGIOS. EL IMPACTO DE INTEGRIDAD VIENE ESPECIFICADO EN EL "+str(float((count_gainpriv_conseq_vulnibm_iot_specified*100)/count_gainpriv_conseq_vulnibm_iot))+" % DE ELLAS. LOS PORCENTAJES DE IMPACTO DE INTEGRIDAD SON LOS SIGUIENTES :  \n")
    print("            -    EN EL "+str(float((count_gainpriv_conseq_highintimpact_vulnibm_iot*100)/count_gainpriv_conseq_vulnibm_iot))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
    print("            -    EN EL "+str(float((count_gainpriv_conseq_lowintimpact_vulnibm_iot*100)/count_gainpriv_conseq_vulnibm_iot))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
    print("            -    EN EL "+str(float((count_gainpriv_conseq_mediumintimpact_vulnibm_iot*100)/count_gainpriv_conseq_vulnibm_iot))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO  \n")
    print("\n")

if(count_denialofserv_conseq_vulnibm_iot>0):
    print("      -    EN EL "+str(float((count_denialofserv_conseq_vulnibm_iot*100)/count_conseq_vulnibm_iot))+" % DE VULNERABILIDADES LA CONSECUENCIA ES UNA DENEGACIÓN DE SERVICIO. EL IMPACTO DE INTEGRIDAD VIENE ESPECIFICADO EN EL "+str(float((count_denialofserv_conseq_vulnibm_iot_specified*100)/count_denialofserv_conseq_vulnibm_iot))+" % DE ELLAS. LOS PORCENTAJES DE IMPACTO DE INTEGRIDAD SON LOS SIGUIENTES :  \n")
    print("            -    EN EL "+str(float((count_denialofserv_conseq_highintimpact_vulnibm_iot*100)/count_denialofserv_conseq_vulnibm_iot))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
    print("            -    EN EL "+str(float((count_denialofserv_conseq_lowintimpact_vulnibm_iot*100)/count_denialofserv_conseq_vulnibm_iot))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
    print("            -    EN EL "+str(float((count_denialofserv_conseq_mediumintimpact_vulnibm_iot*100)/count_denialofserv_conseq_vulnibm_iot))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO  \n")
    print("\n")
    
if(count_bypassec_conseq_vulnibm_iot>0):
    print("      -    EN EL "+str(float((count_bypassec_conseq_vulnibm_iot*100)/count_conseq_vulnibm_iot))+" % DE VULNERABILIDADES LA CONSECUENCIA ES SOBREPASAR LA SEGURIDAD. EL IMPACTO DE INTEGRIDAD VIENE ESPECIFICADO EN EL "+str(float((count_bypassec_conseq_vulnibm_iot_specified*100)/count_bypassec_conseq_vulnibm_iot))+" % DE ELLAS. LOS PORCENTAJES DE IMPACTO DE INTEGRIDAD SON LOS SIGUIENTES :  \n")
    print("            -    EN EL "+str(float((count_bypassec_conseq_highintimpact_vulnibm_iot*100)/count_bypassec_conseq_vulnibm_iot))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
    print("            -    EN EL "+str(float((count_bypassec_conseq_lowintimpact_vulnibm_iot*100)/count_bypassec_conseq_vulnibm_iot))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
    print("            -    EN EL "+str(float((count_bypassec_conseq_mediumintimpact_vulnibm_iot*100)/count_bypassec_conseq_vulnibm_iot))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO  \n")
    print("\n")    

if(count_filemani_conseq_vulnibm_iot>0):
    print("      -    EN EL "+str(float((count_filemani_conseq_vulnibm_iot*100)/count_conseq_vulnibm_iot))+" % DE VULNERABILIDADES LA CONSECUENCIA ES LA MANIPULACION DE FICHEROS. EL IMPACTO DE INTEGRIDAD VIENE ESPECIFICADO EN EL "+str(float((count_filemani_conseq_vulnibm_iot_specified*100)/count_filemani_conseq_vulnibm_iot))+" % DE ELLAS. LOS PORCENTAJES DE IMPACTO DE INTEGRIDAD SON LOS SIGUIENTES :  \n")
    print("            -    EN EL "+str(float((count_filemani_conseq_highintimpact_vulnibm_iot*100)/count_filemani_conseq_vulnibm_iot))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
    print("            -    EN EL "+str(float((count_filemani_conseq_lowintimpact_vulnibm_iot*100)/count_filemani_conseq_vulnibm_iot))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
    print("            -    EN EL "+str(float((count_filemani_conseq_mediumintimpact_vulnibm_iot*100)/count_filemani_conseq_vulnibm_iot))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO  \n")
    print("\n")
    
if(count_other_conseq_vulnibm_iot>0):
    print("      -    EN EL "+str(float((count_other_conseq_vulnibm_iot*100)/count_conseq_vulnibm_iot))+" % DE VULNERABILIDADES LA CONSECUENCIA ES OTRA DISTINTA A LAS ANTERIORES. EL IMPACTO DE INTEGRIDAD VIENE ESPECIFICADO EN EL "+str(float((count_other_conseq_vulnibm_iot_specified*100)/count_other_conseq_vulnibm_iot))+" % DE ELLAS. LOS PORCENTAJES DE IMPACTO DE INTEGRIDAD SON LOS SIGUIENTES :  \n")
    print("            -    EN EL "+str(float((count_other_conseq_highintimpact_vulnibm_iot*100)/count_other_conseq_vulnibm_iot))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
    print("            -    EN EL "+str(float((count_other_conseq_lowintimpact_vulnibm_iot*100)/count_other_conseq_vulnibm_iot))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
    print("            -    EN EL "+str(float((count_other_conseq_mediumintimpact_vulnibm_iot*100)/count_other_conseq_vulnibm_iot))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO  \n")
    print("\n")
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
df_vulnibm_sh = pd.read_excel('vulnerabilidades_ibm_smart_home_2023.xlsx')

#Variables donde almacenare el valor total de consecuencias
count_conseq_vulnibm_sh=0
#Variables para almacenar el impacto de INTEGRIDAD dada una consecuencia concreto
count_obtaininfoconseq_highintimpact_vulnibm_sh=0
count_obtaininfoconseq_lowintimpact_vulnibm_sh=0
count_obtaininfoconseq_mediumintimpact_vulnibm_sh=0
count_obtaininfoconseq_vulnibm_sh=0
#Variable para almacenar el numero total de valores para los que el impacto de INTEGRIDAD viene especificado para una consecuencia concreta
count_obtaininfoconseq_vulnibm_sh_specified=0

count_xss_conseq_highintimpact_vulnibm_sh=0
count_xss_conseq_lowintimpact_vulnibm_sh=0
count_xss_conseq_mediumintimpact_vulnibm_sh=0
count_xss_conseq_vulnibm_sh=0
count_xss_conseq_vulnibm_sh_specified=0

count_gainacc_conseq_highintimpact_vulnibm_sh=0
count_gainacc_conseq_lowintimpact_vulnibm_sh=0
count_gainacc_conseq_mediumintimpact_vulnibm_sh=0
count_gainacc_conseq_vulnibm_sh=0
count_gainacc_conseq_vulnibm_sh_specified=0

count_gainpriv_conseq_highintimpact_vulnibm_sh=0
count_gainpriv_conseq_lowintimpact_vulnibm_sh=0
count_gainpriv_conseq_mediumintimpact_vulnibm_sh=0
count_gainpriv_conseq_vulnibm_sh=0
count_gainpriv_conseq_vulnibm_sh_specified=0

count_denialofserv_conseq_highintimpact_vulnibm_sh=0
count_denialofserv_conseq_lowintimpact_vulnibm_sh=0
count_denialofserv_conseq_mediumintimpact_vulnibm_sh=0
count_denialofserv_conseq_vulnibm_sh=0
count_denialofserv_conseq_vulnibm_sh_specified=0

count_bypassec_conseq_highintimpact_vulnibm_sh=0
count_bypassec_conseq_lowintimpact_vulnibm_sh=0
count_bypassec_conseq_mediumintimpact_vulnibm_sh=0
count_bypassec_conseq_vulnibm_sh=0
count_bypassec_conseq_vulnibm_sh_specified=0

count_filemani_conseq_highintimpact_vulnibm_sh=0
count_filemani_conseq_lowintimpact_vulnibm_sh=0
count_filemani_conseq_mediumintimpact_vulnibm_sh=0
count_filemani_conseq_vulnibm_sh=0
count_filemani_conseq_vulnibm_sh_specified=0


count_other_conseq_highintimpact_vulnibm_sh=0
count_other_conseq_lowintimpact_vulnibm_sh=0
count_other_conseq_mediumintimpact_vulnibm_sh=0
count_other_conseq_vulnibm_sh=0
count_other_conseq_vulnibm_sh_specified=0

#Recorro los valores de CONSECUENCIAS y aumento los contadores segun su valor

for r in range(0,len(df_vulnibm_sh["x_xfe_consequences"])):                       
    aux_str=df_vulnibm_sh["x_xfe_consequences"][r].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
    if(aux_str!='NONE' or aux_str!='None'):
        count_conseq_vulnibm_sh+=1
        #Compruebo el valor de consecuencia
        if(('ObtainInformation' in aux_str) or ('Obtain Information' in aux_str)):
            count_obtaininfoconseq_vulnibm_sh+=1
            #Compruebo el valor de impacto de INTEGRIDAD
            if(df_vulnibm_sh["x_xfe_cvss_integrity_impact"][r]=='High'):
                count_obtaininfoconseq_vulnibm_sh_specified+=1
                count_obtaininfoconseq_highintimpact_vulnibm_sh+=1
            elif(df_vulnibm_sh["x_xfe_cvss_integrity_impact"][r]=='Low'):
                count_obtaininfoconseq_vulnibm_sh_specified+=1
                count_obtaininfoconseq_lowintimpact_vulnibm_sh+=1
            elif(df_vulnibm_sh["x_xfe_cvss_integrity_impact"][r]=='Medium'):
                count_obtaininfoconseq_vulnibm_sh_specified+=1
                count_obtaininfoconseq_mediumintimpact_vulnibm_sh+=1
        elif('Scripting' in aux_str):
            count_xss_conseq_vulnibm_sh+=1
            if(df_vulnibm_sh["x_xfe_cvss_integrity_impact"][r]=='High'):
                count_xss_conseq_vulnibm_sh_specified+=1
                count_xss_conseq_highintimpact_vulnibm_sh+=1
            elif(df_vulnibm_sh["x_xfe_cvss_integrity_impact"][r]=='Low'):
                count_xss_conseq_vulnibm_sh_specified+=1
                count_xss_conseq_lowintimpact_vulnibm_sh+=1
            elif(df_vulnibm_sh["x_xfe_cvss_integrity_impact"][r]=='Medium'):
                count_xss_conseq_vulnibm_sh_specified+=1
                count_xss_conseq_mediumintimpact_vulnibm_sh+=1
                
        elif('Access' in aux_str):
            count_gainacc_conseq_vulnibm_sh+=1
            if(df_vulnibm_sh["x_xfe_cvss_integrity_impact"][r]=='High'):
                count_gainacc_conseq_vulnibm_sh_specified+=1
                count_gainacc_conseq_highintimpact_vulnibm_sh+=1
            elif(df_vulnibm_sh["x_xfe_cvss_integrity_impact"][r]=='Low'):
                count_gainacc_conseq_vulnibm_sh_specified+=1
                count_gainacc_conseq_lowintimpact_vulnibm_sh+=1
            elif(df_vulnibm_sh["x_xfe_cvss_integrity_impact"][r]=='Medium'):
                count_gainacc_conseq_vulnibm_sh_specified+=1
                count_gainacc_conseq_mediumintimpact_vulnibm_sh+=1
                
        elif('Privilege' in aux_str):
            count_gainpriv_conseq_vulnibm_sh+=1
            if(df_vulnibm_sh["x_xfe_cvss_integrity_impact"][r]=='High'):
                count_gainpriv_conseq_vulnibm_sh_specified+=1
                count_gainpriv_conseq_highintimpact_vulnibm_sh+=1
            elif(df_vulnibm_sh["x_xfe_cvss_integrity_impact"][r]=='Low'):
                count_gainpriv_conseq_vulnibm_sh_specified+=1
                count_gainpriv_conseq_lowintimpact_vulnibm_sh+=1
            elif(df_vulnibm_sh["x_xfe_cvss_integrity_impact"][r]=='Medium'):
                count_gainpriv_conseq_vulnibm_sh_specified+=1
                count_gainpriv_conseq_mediumintimpact_vulnibm_sh+=1
                
        elif('Denial' in aux_str):
            count_denialofserv_conseq_vulnibm_sh+=1
            if(df_vulnibm_sh["x_xfe_cvss_integrity_impact"][r]=='High'):
                count_denialofserv_conseq_vulnibm_sh_specified+=1
                count_denialofserv_conseq_highintimpact_vulnibm_sh+=1
            elif(df_vulnibm_sh["x_xfe_cvss_integrity_impact"][r]=='Low'):
                count_denialofserv_conseq_vulnibm_sh_specified+=1
                count_denialofserv_conseq_lowintimpact_vulnibm_sh+=1
            elif(df_vulnibm_sh["x_xfe_cvss_integrity_impact"][r]=='Medium'):
                count_denialofserv_conseq_vulnibm_sh_specified+=1
                count_denialofserv_conseq_mediumintimpact_vulnibm_sh+=1
        
        elif('Bypass' in aux_str):
            count_bypassec_conseq_vulnibm_sh+=1
            if(df_vulnibm_sh["x_xfe_cvss_integrity_impact"][r]=='High'):
                count_bypassec_conseq_vulnibm_sh_specified+=1
                count_bypassec_conseq_highintimpact_vulnibm_sh+=1
            elif(df_vulnibm_sh["x_xfe_cvss_integrity_impact"][r]=='Low'):
                count_bypassec_conseq_vulnibm_sh_specified+=1
                count_bypassec_conseq_lowintimpact_vulnibm_sh+=1
            elif(df_vulnibm_sh["x_xfe_cvss_integrity_impact"][r]=='Medium'):
                count_bypassec_conseq_vulnibm_sh_specified+=1
                count_bypassec_conseq_mediumintimpact_vulnibm_sh+=1
                
        elif('Manipulation' in aux_str):
            count_filemani_conseq_vulnibm_sh+=1
            if(df_vulnibm_sh["x_xfe_cvss_integrity_impact"][r]=='High'):
                count_filemani_conseq_vulnibm_sh_specified+=1
                count_filemani_conseq_highintimpact_vulnibm_sh+=1
            elif(df_vulnibm_sh["x_xfe_cvss_integrity_impact"][r]=='Low'):
                count_filemani_conseq_vulnibm_sh_specified+=1
                count_filemani_conseq_lowintimpact_vulnibm_sh+=1
            elif(df_vulnibm_sh["x_xfe_cvss_integrity_impact"][r]=='Medium'):
                count_filemani_conseq_vulnibm_sh_specified+=1
                count_filemani_conseq_mediumintimpact_vulnibm_sh+=1
                
        elif('Other' in aux_str):
            count_other_conseq_vulnibm_sh+=1
            if(df_vulnibm_sh["x_xfe_cvss_integrity_impact"][r]=='High'):
                count_other_conseq_vulnibm_sh_specified+=1
                count_other_conseq_highintimpact_vulnibm_sh+=1
            elif(df_vulnibm_sh["x_xfe_cvss_integrity_impact"][r]=='Low'):
                count_other_conseq_vulnibm_sh_specified+=1
                count_other_conseq_lowintimpact_vulnibm_sh+=1
            elif(df_vulnibm_sh["x_xfe_cvss_integrity_impact"][r]=='Medium'):
                count_other_conseq_vulnibm_sh_specified+=1
                count_other_conseq_mediumintimpact_vulnibm_sh+=1
                
        
                
        
                
                
                
                
                
                
                
                
                
                
                
print("*******************ESTADÍSTICAS CONSECUENCIAS DE EXPLOTACION VULNERABILIDAD/IMPACTO DE INTEGRIDAD VULNERABILIDADES IBM PARTE SMART HOME*******************")
print("\n")                            
print("\n")
print(" DE UN TOTAL DE "+str(count_conseq_vulnibm_sh)+" VULNERABILIDADES DONDE LA CONSECUENCIA VIENE ESPECIFICADA:\n") 
print("\n")
print("   - LAS ESTADISTICAS DE CONSECUENCIAS SON LAS SIGUIENTES:  \n")
print("      -    EN  "+str(count_obtaininfoconseq_vulnibm_sh)+" VULNERABILIDADES LA CONSECUENCIA ES LA OBTENCION DE INFORMACION. EL IMPACTO DE INTEGRIDAD VIENE ESPECIFICADO ES  "+str(count_obtaininfoconseq_vulnibm_sh_specified)+" VULNERABILIDADES. LAS ESTADÍSTICAS DE IMPACTO DE INTEGRIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_obtaininfoconseq_highintimpact_vulnibm_sh)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
print("            -    EN  "+str(count_obtaininfoconseq_lowintimpact_vulnibm_sh)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
print("            -    EN  "+str(count_obtaininfoconseq_mediumintimpact_vulnibm_sh)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO\n")
print("\n")
print("      -    EN  "+str(count_xss_conseq_vulnibm_sh)+" VULNERABILIDADES LA CONSECUENCIA ES UN ATAQUE DE CROSS-SITE SCRIPTING. EL IMPACTO DE INTEGRIDAD VIENE ESPECIFICADO ES  "+str(count_xss_conseq_vulnibm_sh_specified)+" VULNERABILIDADES. LAS ESTADÍSTICAS DE IMPACTO DE INTEGRIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_xss_conseq_highintimpact_vulnibm_sh)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
print("            -    EN  "+str(count_xss_conseq_lowintimpact_vulnibm_sh)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
print("            -    EN  "+str(count_xss_conseq_mediumintimpact_vulnibm_sh)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO\n")
print("\n")
print("      -    EN  "+str(count_gainacc_conseq_vulnibm_sh)+" VULNERABILIDADES LA CONSECUENCIA ES LA OBTENCIÓN DE ACCESO. EL IMPACTO DE INTEGRIDAD VIENE ESPECIFICADO ES  "+str(count_gainacc_conseq_vulnibm_sh_specified)+" VULNERABILIDADES. LAS ESTADÍSTICAS DE IMPACTO DE INTEGRIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_gainacc_conseq_highintimpact_vulnibm_sh)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
print("            -    EN  "+str(count_gainacc_conseq_lowintimpact_vulnibm_sh)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
print("            -    EN  "+str(count_gainacc_conseq_mediumintimpact_vulnibm_sh)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO\n")
print("\n")
print("      -    EN  "+str(count_gainpriv_conseq_vulnibm_sh)+" VULNERABILIDADES LA CONSECUENCIA ES LA OBTENCIÓN DE PRIVILEGIOS. EL IMPACTO DE INTEGRIDAD VIENE ESPECIFICADO ES  "+str(count_gainpriv_conseq_vulnibm_sh_specified)+" VULNERABILIDADES. LAS ESTADÍSTICAS DE IMPACTO DE INTEGRIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_gainpriv_conseq_highintimpact_vulnibm_sh)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
print("            -    EN  "+str(count_gainpriv_conseq_lowintimpact_vulnibm_sh)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
print("            -    EN  "+str(count_gainpriv_conseq_mediumintimpact_vulnibm_sh)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO\n")
print("\n")
print("      -    EN  "+str(count_denialofserv_conseq_vulnibm_sh)+" VULNERABILIDADES LA CONSECUENCIA ES UNA DENEGACIÓN DE SERVICIO. EL IMPACTO DE INTEGRIDAD VIENE ESPECIFICADO ES  "+str(count_denialofserv_conseq_vulnibm_sh_specified)+" VULNERABILIDADES. LAS ESTADÍSTICAS DE IMPACTO DE INTEGRIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_denialofserv_conseq_highintimpact_vulnibm_sh)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
print("            -    EN  "+str(count_denialofserv_conseq_lowintimpact_vulnibm_sh)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
print("            -    EN  "+str(count_denialofserv_conseq_mediumintimpact_vulnibm_sh)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO\n")
print("\n")
print("      -    EN  "+str(count_filemani_conseq_vulnibm_sh)+" VULNERABILIDADES LA CONSECUENCIA ES LA MANIPULACIÓN DE FICHEROS. EL IMPACTO DE INTEGRIDAD VIENE ESPECIFICADO ES  "+str(count_filemani_conseq_vulnibm_sh_specified)+" VULNERABILIDADES. LAS ESTADÍSTICAS DE IMPACTO DE INTEGRIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_filemani_conseq_highintimpact_vulnibm_sh)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
print("            -    EN  "+str(count_filemani_conseq_lowintimpact_vulnibm_sh)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
print("            -    EN  "+str(count_filemani_conseq_mediumintimpact_vulnibm_sh)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO\n")
print("\n")
print("      -    EN  "+str(count_other_conseq_vulnibm_sh)+" VULNERABILIDADES LA CONSECUENCIA ES OTRA DISTINTA A LAS ANTERIORES. EL IMPACTO DE INTEGRIDAD VIENE ESPECIFICADO ES  "+str(count_other_conseq_vulnibm_sh_specified)+" VULNERABILIDADES. LAS ESTADÍSTICAS DE IMPACTO DE INTEGRIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_other_conseq_highintimpact_vulnibm_sh)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
print("            -    EN  "+str(count_other_conseq_lowintimpact_vulnibm_sh)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
print("            -    EN  "+str(count_other_conseq_mediumintimpact_vulnibm_sh)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO\n")
print("\n")






print("*******************PORCENTAJES CONSECUENCIAS DE EXPLOTACION VULNERABILIDAD/IMPACTO DE INTEGRIDAD VULNERABILIDADES IBM SMART HOME *******************")
print("\n")                            
print("\n")
print(" DE UN TOTAL DE "+str(count_conseq_vulnibm_sh)+" VULNERABILIDADES :\n") 
print("\n")
print("   - LOS PORCENTAJES DE CONSECUENCIAS SON LOS SIGUIENTES:  \n")
if(count_obtaininfoconseq_vulnibm_sh>0):
    print("      -    EN EL "+str(float((count_obtaininfoconseq_vulnibm_sh*100)/count_conseq_vulnibm_sh))+" % DE VULNERABILIDADES LA CONSECUENCIA ES LA OBTENCION DE INFORMACION. EL IMPACTO DE INTEGRIDAD VIENE ESPECIFICADO EN EL "+str(float((count_obtaininfoconseq_vulnibm_sh_specified*100)/count_obtaininfoconseq_vulnibm_sh))+" % DE ELLAS. LOS PORCENTAJES DE IMPACTO DE INTEGRIDAD SON LOS SIGUIENTES :  \n")
    print("            -    EN EL "+str(float((count_obtaininfoconseq_highintimpact_vulnibm_sh*100)/count_obtaininfoconseq_vulnibm_sh))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
    print("            -    EN EL "+str(float((count_obtaininfoconseq_lowintimpact_vulnibm_sh*100)/count_obtaininfoconseq_vulnibm_sh))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
    print("            -    EN EL "+str(float((count_obtaininfoconseq_mediumintimpact_vulnibm_sh*100)/count_obtaininfoconseq_vulnibm_sh))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO  \n")
    print("\n")
if(count_xss_conseq_vulnibm_sh>0):
    print("      -    EN EL "+str(float((count_xss_conseq_vulnibm_sh*100)/count_conseq_vulnibm_sh))+" % DE VULNERABILIDADES LA CONSECUENCIA ES UN ATAQUE DE CROSS-SITE SCRIPTING. EL IMPACTO DE INTEGRIDAD VIENE ESPECIFICADO EN EL "+str(float((count_xss_conseq_vulnibm_sh_specified*100)/count_xss_conseq_vulnibm_sh))+" % DE ELLAS. LOS PORCENTAJES DE IMPACTO DE INTEGRIDAD SON LOS SIGUIENTES :  \n")
    print("            -    EN EL "+str(float((count_xss_conseq_highintimpact_vulnibm_sh*100)/count_xss_conseq_vulnibm_sh))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
    print("            -    EN EL "+str(float((count_xss_conseq_lowintimpact_vulnibm_sh*100)/count_xss_conseq_vulnibm_sh))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
    print("            -    EN EL "+str(float((count_xss_conseq_mediumintimpact_vulnibm_sh*100)/count_xss_conseq_vulnibm_sh))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO  \n")
    print("\n")
if(count_gainacc_conseq_vulnibm_sh>0):
    print("      -    EN EL "+str(float((count_gainacc_conseq_vulnibm_sh*100)/count_conseq_vulnibm_sh))+" % DE VULNERABILIDADES LA CONSECUENCIA ES LA OBTENCIÓN DE ACCESO. EL IMPACTO DE INTEGRIDAD VIENE ESPECIFICADO EN EL "+str(float((count_gainacc_conseq_vulnibm_sh_specified*100)/count_gainacc_conseq_vulnibm_sh))+" % DE ELLAS. LOS PORCENTAJES DE IMPACTO DE INTEGRIDAD SON LOS SIGUIENTES :  \n")
    print("            -    EN EL "+str(float((count_gainacc_conseq_highintimpact_vulnibm_sh*100)/count_gainacc_conseq_vulnibm_sh))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
    print("            -    EN EL "+str(float((count_gainacc_conseq_lowintimpact_vulnibm_sh*100)/count_gainacc_conseq_vulnibm_sh))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
    print("            -    EN EL "+str(float((count_gainacc_conseq_mediumintimpact_vulnibm_sh*100)/count_gainacc_conseq_vulnibm_sh))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO  \n")
    print("\n")
if(count_gainpriv_conseq_vulnibm_sh>0):
    print("      -    EN EL "+str(float((count_gainpriv_conseq_vulnibm_sh*100)/count_conseq_vulnibm_sh))+" % DE VULNERABILIDADES LA CONSECUENCIA ES LA OBTENCIÓN DE PRIVILEGIOS. EL IMPACTO DE INTEGRIDAD VIENE ESPECIFICADO EN EL "+str(float((count_gainpriv_conseq_vulnibm_sh_specified*100)/count_gainpriv_conseq_vulnibm_sh))+" % DE ELLAS. LOS PORCENTAJES DE IMPACTO DE INTEGRIDAD SON LOS SIGUIENTES :  \n")
    print("            -    EN EL "+str(float((count_gainpriv_conseq_highintimpact_vulnibm_sh*100)/count_gainpriv_conseq_vulnibm_sh))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
    print("            -    EN EL "+str(float((count_gainpriv_conseq_lowintimpact_vulnibm_sh*100)/count_gainpriv_conseq_vulnibm_sh))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
    print("            -    EN EL "+str(float((count_gainpriv_conseq_mediumintimpact_vulnibm_sh*100)/count_gainpriv_conseq_vulnibm_sh))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO  \n")
    print("\n")

if(count_denialofserv_conseq_vulnibm_sh>0):
    print("      -    EN EL "+str(float((count_denialofserv_conseq_vulnibm_sh*100)/count_conseq_vulnibm_sh))+" % DE VULNERABILIDADES LA CONSECUENCIA ES UNA DENEGACIÓN DE SERVICIO. EL IMPACTO DE INTEGRIDAD VIENE ESPECIFICADO EN EL "+str(float((count_denialofserv_conseq_vulnibm_sh_specified*100)/count_denialofserv_conseq_vulnibm_sh))+" % DE ELLAS. LOS PORCENTAJES DE IMPACTO DE INTEGRIDAD SON LOS SIGUIENTES :  \n")
    print("            -    EN EL "+str(float((count_denialofserv_conseq_highintimpact_vulnibm_sh*100)/count_denialofserv_conseq_vulnibm_sh))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
    print("            -    EN EL "+str(float((count_denialofserv_conseq_lowintimpact_vulnibm_sh*100)/count_denialofserv_conseq_vulnibm_sh))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
    print("            -    EN EL "+str(float((count_denialofserv_conseq_mediumintimpact_vulnibm_sh*100)/count_denialofserv_conseq_vulnibm_sh))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO  \n")
    print("\n")
    
if(count_bypassec_conseq_vulnibm_sh>0):
    print("      -    EN EL "+str(float((count_bypassec_conseq_vulnibm_sh*100)/count_conseq_vulnibm_sh))+" % DE VULNERABILIDADES LA CONSECUENCIA ES SOBREPASAR LA SEGURIDAD. EL IMPACTO DE INTEGRIDAD VIENE ESPECIFICADO EN EL "+str(float((count_bypassec_conseq_vulnibm_sh_specified*100)/count_bypassec_conseq_vulnibm_sh))+" % DE ELLAS. LOS PORCENTAJES DE IMPACTO DE INTEGRIDAD SON LOS SIGUIENTES :  \n")
    print("            -    EN EL "+str(float((count_bypassec_conseq_highintimpact_vulnibm_sh*100)/count_bypassec_conseq_vulnibm_sh))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
    print("            -    EN EL "+str(float((count_bypassec_conseq_lowintimpact_vulnibm_sh*100)/count_bypassec_conseq_vulnibm_sh))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
    print("            -    EN EL "+str(float((count_bypassec_conseq_mediumintimpact_vulnibm_sh*100)/count_bypassec_conseq_vulnibm_sh))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO  \n")
    print("\n")    

if(count_filemani_conseq_vulnibm_sh>0):
    print("      -    EN EL "+str(float((count_filemani_conseq_vulnibm_sh*100)/count_conseq_vulnibm_sh))+" % DE VULNERABILIDADES LA CONSECUENCIA ES LA MANIPULACION DE FICHEROS. EL IMPACTO DE INTEGRIDAD VIENE ESPECIFICADO EN EL "+str(float((count_filemani_conseq_vulnibm_sh_specified*100)/count_filemani_conseq_vulnibm_sh))+" % DE ELLAS. LOS PORCENTAJES DE IMPACTO DE INTEGRIDAD SON LOS SIGUIENTES :  \n")
    print("            -    EN EL "+str(float((count_filemani_conseq_highintimpact_vulnibm_sh*100)/count_filemani_conseq_vulnibm_sh))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
    print("            -    EN EL "+str(float((count_filemani_conseq_lowintimpact_vulnibm_sh*100)/count_filemani_conseq_vulnibm_sh))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
    print("            -    EN EL "+str(float((count_filemani_conseq_mediumintimpact_vulnibm_sh*100)/count_filemani_conseq_vulnibm_sh))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO  \n")
    print("\n")
    
if(count_other_conseq_vulnibm_sh>0):
    print("      -    EN EL "+str(float((count_other_conseq_vulnibm_sh*100)/count_conseq_vulnibm_sh))+" % DE VULNERABILIDADES LA CONSECUENCIA ES OTRA DISTINTA A LAS ANTERIORES. EL IMPACTO DE INTEGRIDAD VIENE ESPECIFICADO EN EL "+str(float((count_other_conseq_vulnibm_sh_specified*100)/count_other_conseq_vulnibm_sh))+" % DE ELLAS. LOS PORCENTAJES DE IMPACTO DE INTEGRIDAD SON LOS SIGUIENTES :  \n")
    print("            -    EN EL "+str(float((count_other_conseq_highintimpact_vulnibm_sh*100)/count_other_conseq_vulnibm_sh))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
    print("            -    EN EL "+str(float((count_other_conseq_lowintimpact_vulnibm_sh*100)/count_other_conseq_vulnibm_sh))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
    print("            -    EN EL "+str(float((count_other_conseq_mediumintimpact_vulnibm_sh*100)/count_other_conseq_vulnibm_sh))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO  \n")
    print("\n")
          
   
    
    
    
print("*******************ESTADÍSTICAS CONSECUENCIAS DE EXPLOTACION VULNERABILIDAD/IMPACTO DE INTEGRIDAD VULNERABILIDADES IBM PARTE IOT Y SMART HOME CONJUNTAS*******************")
print("\n")                            
print("\n")
print(" DE UN TOTAL DE "+str(count_conseq_vulnibm_sh+count_conseq_vulnibm_iot)+" VULNERABILIDADES DONDE LA CONSECUENCIA VIENE ESPECIFICADA:\n") 
print("\n")
print("   - LAS ESTADISTICAS DE CONSECUENCIAS SON LAS SIGUIENTES:  \n")
print("      -    EN  "+str(count_obtaininfoconseq_vulnibm_sh+count_obtaininfoconseq_vulnibm_iot)+" VULNERABILIDADES LA CONSECUENCIA ES LA OBTENCION DE INFORMACION. EL IMPACTO DE INTEGRIDAD VIENE ESPECIFICADO ES  "+str(count_obtaininfoconseq_vulnibm_sh_specified+count_obtaininfoconseq_vulnibm_iot_specified)+" VULNERABILIDADES. LAS ESTADÍSTICAS DE IMPACTO DE INTEGRIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_obtaininfoconseq_highintimpact_vulnibm_sh+count_obtaininfoconseq_highintimpact_vulnibm_iot)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
print("            -    EN  "+str(count_obtaininfoconseq_lowintimpact_vulnibm_sh+count_obtaininfoconseq_lowintimpact_vulnibm_iot)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
print("            -    EN  "+str(count_obtaininfoconseq_mediumintimpact_vulnibm_sh+count_obtaininfoconseq_mediumintimpact_vulnibm_iot)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO\n")
print("\n")
print("      -    EN  "+str(count_xss_conseq_vulnibm_sh+count_xss_conseq_vulnibm_iot)+" VULNERABILIDADES LA CONSECUENCIA ES UN ATAQUE DE CROSS-SITE SCRIPTING. EL IMPACTO DE INTEGRIDAD VIENE ESPECIFICADO ES  "+str(count_xss_conseq_vulnibm_sh_specified+count_xss_conseq_vulnibm_iot_specified)+" VULNERABILIDADES. LAS ESTADÍSTICAS DE IMPACTO DE INTEGRIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_xss_conseq_highintimpact_vulnibm_sh+count_xss_conseq_highintimpact_vulnibm_iot)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
print("            -    EN  "+str(count_xss_conseq_lowintimpact_vulnibm_sh+count_xss_conseq_lowintimpact_vulnibm_iot)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
print("            -    EN  "+str(count_xss_conseq_mediumintimpact_vulnibm_sh+count_xss_conseq_mediumintimpact_vulnibm_iot)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO\n")
print("\n")
print("      -    EN  "+str(count_gainacc_conseq_vulnibm_sh+count_gainacc_conseq_vulnibm_iot)+" VULNERABILIDADES LA CONSECUENCIA ES LA OBTENCIÓN DE ACCESO. EL IMPACTO DE INTEGRIDAD VIENE ESPECIFICADO ES  "+str(count_gainacc_conseq_vulnibm_sh_specified+count_gainacc_conseq_vulnibm_iot_specified)+" VULNERABILIDADES. LAS ESTADÍSTICAS DE IMPACTO DE INTEGRIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_gainacc_conseq_highintimpact_vulnibm_sh+count_gainacc_conseq_highintimpact_vulnibm_iot)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
print("            -    EN  "+str(count_gainacc_conseq_lowintimpact_vulnibm_sh+count_gainacc_conseq_lowintimpact_vulnibm_iot)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
print("            -    EN  "+str(count_gainacc_conseq_mediumintimpact_vulnibm_sh+count_gainacc_conseq_mediumintimpact_vulnibm_iot)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO\n")
print("\n")
print("      -    EN  "+str(count_gainpriv_conseq_vulnibm_sh+count_gainpriv_conseq_vulnibm_iot)+" VULNERABILIDADES LA CONSECUENCIA ES LA OBTENCIÓN DE PRIVILEGIOS. EL IMPACTO DE INTEGRIDAD VIENE ESPECIFICADO ES  "+str(count_gainpriv_conseq_vulnibm_sh_specified+count_gainpriv_conseq_vulnibm_iot_specified)+" VULNERABILIDADES. LAS ESTADÍSTICAS DE IMPACTO DE INTEGRIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_gainpriv_conseq_highintimpact_vulnibm_sh+count_gainpriv_conseq_highintimpact_vulnibm_iot)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
print("            -    EN  "+str(count_gainpriv_conseq_lowintimpact_vulnibm_sh+count_gainpriv_conseq_lowintimpact_vulnibm_iot)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
print("            -    EN  "+str(count_gainpriv_conseq_mediumintimpact_vulnibm_sh+count_gainpriv_conseq_mediumintimpact_vulnibm_iot)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO\n")
print("\n")
print("      -    EN  "+str(count_denialofserv_conseq_vulnibm_sh+count_denialofserv_conseq_vulnibm_iot)+" VULNERABILIDADES LA CONSECUENCIA ES UNA DENEGACIÓN DE SERVICIO. EL IMPACTO DE INTEGRIDAD VIENE ESPECIFICADO ES  "+str(count_denialofserv_conseq_vulnibm_sh_specified+count_denialofserv_conseq_vulnibm_iot_specified)+" VULNERABILIDADES. LAS ESTADÍSTICAS DE IMPACTO DE INTEGRIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_denialofserv_conseq_highintimpact_vulnibm_sh+count_denialofserv_conseq_highintimpact_vulnibm_iot)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
print("            -    EN  "+str(count_denialofserv_conseq_lowintimpact_vulnibm_sh+count_denialofserv_conseq_lowintimpact_vulnibm_iot)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
print("            -    EN  "+str(count_denialofserv_conseq_mediumintimpact_vulnibm_sh+count_denialofserv_conseq_mediumintimpact_vulnibm_iot)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO\n")
print("\n")
print("      -    EN  "+str(count_bypassec_conseq_vulnibm_sh+count_bypassec_conseq_vulnibm_iot)+" VULNERABILIDADES LA CONSECUENCIA ES SOBREPASAR LA SEGURIDAD. EL IMPACTO DE INTEGRIDAD VIENE ESPECIFICADO ES  "+str(count_bypassec_conseq_vulnibm_sh_specified+count_bypassec_conseq_vulnibm_iot_specified)+" VULNERABILIDADES. LAS ESTADÍSTICAS DE IMPACTO DE INTEGRIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_bypassec_conseq_highintimpact_vulnibm_sh+count_bypassec_conseq_highintimpact_vulnibm_iot)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
print("            -    EN  "+str(count_bypassec_conseq_lowintimpact_vulnibm_sh+count_bypassec_conseq_lowintimpact_vulnibm_iot)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
print("            -    EN  "+str(count_bypassec_conseq_mediumintimpact_vulnibm_sh+count_bypassec_conseq_mediumintimpact_vulnibm_iot)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO\n")
print("\n")
print("      -    EN  "+str(count_filemani_conseq_vulnibm_sh+count_filemani_conseq_vulnibm_iot)+" VULNERABILIDADES LA CONSECUENCIA ES LA MANIPULACION DE FICHEROS. EL IMPACTO DE INTEGRIDAD VIENE ESPECIFICADO ES  "+str(count_filemani_conseq_vulnibm_sh_specified+count_filemani_conseq_vulnibm_iot_specified)+" VULNERABILIDADES. LAS ESTADÍSTICAS DE IMPACTO DE INTEGRIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_filemani_conseq_highintimpact_vulnibm_sh+count_filemani_conseq_highintimpact_vulnibm_iot)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
print("            -    EN  "+str(count_filemani_conseq_lowintimpact_vulnibm_sh+count_filemani_conseq_lowintimpact_vulnibm_iot)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
print("            -    EN  "+str(count_filemani_conseq_mediumintimpact_vulnibm_sh+count_filemani_conseq_mediumintimpact_vulnibm_iot)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO\n")
print("\n")
print("      -    EN  "+str(count_other_conseq_vulnibm_sh+count_other_conseq_vulnibm_iot)+" VULNERABILIDADES LA CONSECUENCIA ES DISTINTA A LAS ANTERIORES. EL IMPACTO DE INTEGRIDAD VIENE ESPECIFICADO ES  "+str(count_other_conseq_vulnibm_sh_specified+count_other_conseq_vulnibm_iot_specified)+" VULNERABILIDADES. LAS ESTADÍSTICAS DE IMPACTO DE INTEGRIDAD SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_other_conseq_highintimpact_vulnibm_sh+count_other_conseq_highintimpact_vulnibm_iot)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
print("            -    EN  "+str(count_other_conseq_lowintimpact_vulnibm_sh+count_other_conseq_lowintimpact_vulnibm_iot)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
print("            -    EN  "+str(count_other_conseq_mediumintimpact_vulnibm_sh+count_other_conseq_mediumintimpact_vulnibm_iot)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO\n")
print("\n")









print("*******************PORCENTAJES CONSECUENCIAS DE EXPLOTACION VULNERABILIDAD/IMPACTO DE INTEGRIDAD VULNERABILIDADES IBM PARTE IOT Y SMART HOME CONJUNTAS*******************")
print("\n")                            
print("\n")
print(" DE UN TOTAL DE "+str(count_conseq_vulnibm_sh+count_conseq_vulnibm_iot)+" VULNERABILIDADES :\n") 
print("\n")
print("   - LOS PORCENTAJES DE CONSECUENCIAS SON LOS SIGUIENTES:  \n")
if((count_obtaininfoconseq_vulnibm_sh+count_obtaininfoconseq_vulnibm_iot)>0):
    print("      -    EN EL "+str(float(((count_obtaininfoconseq_vulnibm_sh+count_obtaininfoconseq_vulnibm_iot)*100)/(count_conseq_vulnibm_sh+count_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES LA CONSECUENCIA ES LA OBTENCION DE INFORMACION. EL IMPACTO DE INTEGRIDAD VIENE ESPECIFICADO EN EL "+str(float(((count_obtaininfoconseq_vulnibm_sh_specified+count_obtaininfoconseq_vulnibm_iot_specified)*100)/(count_obtaininfoconseq_vulnibm_sh+count_obtaininfoconseq_vulnibm_iot)))+" % DE ELLAS. LOS PORCENTAJES DE IMPACTO DE INTEGRIDAD SON LOS SIGUIENTES :  \n")
    print("            -    EN EL "+str(float(((count_obtaininfoconseq_highintimpact_vulnibm_sh+count_obtaininfoconseq_highintimpact_vulnibm_iot)*100)/(count_obtaininfoconseq_vulnibm_sh+count_obtaininfoconseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
    print("            -    EN EL "+str(float(((count_obtaininfoconseq_lowintimpact_vulnibm_sh+count_obtaininfoconseq_lowintimpact_vulnibm_iot)*100)/(count_obtaininfoconseq_vulnibm_sh+count_obtaininfoconseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
    print("            -    EN EL "+str(float(((count_obtaininfoconseq_mediumintimpact_vulnibm_sh+count_obtaininfoconseq_mediumintimpact_vulnibm_iot)*100)/(count_obtaininfoconseq_vulnibm_sh+count_obtaininfoconseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO  \n")
    print("\n")
if((count_xss_conseq_vulnibm_sh+count_xss_conseq_vulnibm_iot)>0):
    print("      -    EN EL "+str(float(((count_xss_conseq_vulnibm_sh+count_xss_conseq_vulnibm_iot)*100)/(count_conseq_vulnibm_sh+count_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES LA CONSECUENCIA ES UN ATAQUE DE CROSS-SITE SCRIPTING. EL IMPACTO DE INTEGRIDAD VIENE ESPECIFICADO EN EL "+str(float(((count_xss_conseq_vulnibm_sh_specified+count_xss_conseq_vulnibm_iot_specified)*100)/(count_xss_conseq_vulnibm_sh+count_xss_conseq_vulnibm_iot)))+" % DE ELLAS. LOS PORCENTAJES DE IMPACTO DE INTEGRIDAD SON LOS SIGUIENTES :  \n")
    print("            -    EN EL "+str(float(((count_xss_conseq_highintimpact_vulnibm_sh+count_xss_conseq_highintimpact_vulnibm_iot)*100)/(count_xss_conseq_vulnibm_sh+count_xss_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
    print("            -    EN EL "+str(float(((count_xss_conseq_lowintimpact_vulnibm_sh+count_xss_conseq_lowintimpact_vulnibm_iot)*100)/(count_xss_conseq_vulnibm_sh+count_xss_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
    print("            -    EN EL "+str(float(((count_xss_conseq_mediumintimpact_vulnibm_sh+count_xss_conseq_mediumintimpact_vulnibm_iot)*100)/(count_xss_conseq_vulnibm_sh+count_xss_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO  \n")
    print("\n")
if((count_gainacc_conseq_vulnibm_sh+count_gainacc_conseq_vulnibm_iot)>0):
    print("      -    EN EL "+str(float(((count_gainacc_conseq_vulnibm_sh+count_gainacc_conseq_vulnibm_iot)*100)/(count_conseq_vulnibm_sh+count_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES LA CONSECUENCIA ES LA OBTENCIÓN DE ACCESO. EL IMPACTO DE INTEGRIDAD VIENE ESPECIFICADO EN EL "+str(float(((count_gainacc_conseq_vulnibm_sh_specified+count_gainacc_conseq_vulnibm_iot_specified)*100)/(count_gainacc_conseq_vulnibm_sh+count_gainacc_conseq_vulnibm_iot)))+" % DE ELLAS. LOS PORCENTAJES DE IMPACTO DE INTEGRIDAD SON LOS SIGUIENTES :  \n")
    print("            -    EN EL "+str(float(((count_gainacc_conseq_highintimpact_vulnibm_sh+count_gainacc_conseq_highintimpact_vulnibm_iot)*100)/(count_gainacc_conseq_vulnibm_sh+count_gainacc_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
    print("            -    EN EL "+str(float(((count_gainacc_conseq_lowintimpact_vulnibm_sh+count_gainacc_conseq_lowintimpact_vulnibm_iot)*100)/(count_gainacc_conseq_vulnibm_sh+count_gainacc_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
    print("            -    EN EL "+str(float(((count_gainacc_conseq_mediumintimpact_vulnibm_sh+count_gainacc_conseq_mediumintimpact_vulnibm_iot)*100)/(count_gainacc_conseq_vulnibm_sh+count_gainacc_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO  \n")
    print("\n")
if((count_gainpriv_conseq_vulnibm_sh+count_gainpriv_conseq_vulnibm_iot)>0):
    print("      -    EN EL "+str(float(((count_gainpriv_conseq_vulnibm_sh+count_gainpriv_conseq_vulnibm_iot)*100)/(count_conseq_vulnibm_sh+count_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES LA CONSECUENCIA ES LA OBTENCIÓN DE PRIVILEGIOS. EL IMPACTO DE INTEGRIDAD VIENE ESPECIFICADO EN EL "+str(float(((count_gainpriv_conseq_vulnibm_sh_specified+count_gainpriv_conseq_vulnibm_iot_specified)*100)/(count_gainpriv_conseq_vulnibm_sh+count_gainpriv_conseq_vulnibm_iot)))+" % DE ELLAS. LOS PORCENTAJES DE IMPACTO DE INTEGRIDAD SON LOS SIGUIENTES :  \n")
    print("            -    EN EL "+str(float(((count_gainpriv_conseq_highintimpact_vulnibm_sh+count_gainpriv_conseq_highintimpact_vulnibm_iot)*100)/(count_gainpriv_conseq_vulnibm_sh+count_gainpriv_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
    print("            -    EN EL "+str(float(((count_gainpriv_conseq_lowintimpact_vulnibm_sh+count_gainpriv_conseq_lowintimpact_vulnibm_iot)*100)/(count_gainpriv_conseq_vulnibm_sh+count_gainpriv_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
    print("            -    EN EL "+str(float(((count_gainpriv_conseq_mediumintimpact_vulnibm_sh+count_gainpriv_conseq_mediumintimpact_vulnibm_iot)*100)/(count_gainpriv_conseq_vulnibm_sh+count_gainpriv_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO  \n")
    print("\n")
    
if((count_denialofserv_conseq_vulnibm_sh+count_denialofserv_conseq_vulnibm_iot)>0):
    print("      -    EN EL "+str(float(((count_denialofserv_conseq_vulnibm_sh+count_denialofserv_conseq_vulnibm_iot)*100)/(count_conseq_vulnibm_sh+count_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES LA CONSECUENCIA ES UNA DENEGACIÓN DE SERVICIO. EL IMPACTO DE INTEGRIDAD VIENE ESPECIFICADO EN EL "+str(float(((count_denialofserv_conseq_vulnibm_sh_specified+count_denialofserv_conseq_vulnibm_iot_specified)*100)/(count_denialofserv_conseq_vulnibm_sh+count_denialofserv_conseq_vulnibm_iot)))+" % DE ELLAS. LOS PORCENTAJES DE IMPACTO DE INTEGRIDAD SON LOS SIGUIENTES :  \n")
    print("            -    EN EL "+str(float(((count_denialofserv_conseq_highintimpact_vulnibm_sh+count_denialofserv_conseq_highintimpact_vulnibm_iot)*100)/(count_denialofserv_conseq_vulnibm_sh+count_denialofserv_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
    print("            -    EN EL "+str(float(((count_denialofserv_conseq_lowintimpact_vulnibm_sh+count_denialofserv_conseq_lowintimpact_vulnibm_iot)*100)/(count_denialofserv_conseq_vulnibm_sh+count_denialofserv_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
    print("            -    EN EL "+str(float(((count_denialofserv_conseq_mediumintimpact_vulnibm_sh+count_denialofserv_conseq_mediumintimpact_vulnibm_iot)*100)/(count_denialofserv_conseq_vulnibm_sh+count_denialofserv_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO  \n")
    print("\n")
if((count_bypassec_conseq_vulnibm_sh+count_bypassec_conseq_vulnibm_iot)>0):
    print("      -    EN EL "+str(float(((count_bypassec_conseq_vulnibm_sh+count_bypassec_conseq_vulnibm_iot)*100)/(count_conseq_vulnibm_sh+count_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES LA CONSECUENCIA ES SOBREPASAR LA SEGURIDAD. EL IMPACTO DE INTEGRIDAD VIENE ESPECIFICADO EN EL "+str(float(((count_bypassec_conseq_vulnibm_sh_specified+count_bypassec_conseq_vulnibm_iot_specified)*100)/(count_bypassec_conseq_vulnibm_sh+count_bypassec_conseq_vulnibm_iot)))+" % DE ELLAS. LOS PORCENTAJES DE IMPACTO DE INTEGRIDAD SON LOS SIGUIENTES :  \n")
    print("            -    EN EL "+str(float(((count_bypassec_conseq_highintimpact_vulnibm_sh+count_bypassec_conseq_highintimpact_vulnibm_iot)*100)/(count_bypassec_conseq_vulnibm_sh+count_bypassec_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
    print("            -    EN EL "+str(float(((count_bypassec_conseq_lowintimpact_vulnibm_sh+count_bypassec_conseq_lowintimpact_vulnibm_iot)*100)/(count_bypassec_conseq_vulnibm_sh+count_bypassec_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
    print("            -    EN EL "+str(float(((count_bypassec_conseq_mediumintimpact_vulnibm_sh+count_bypassec_conseq_mediumintimpact_vulnibm_iot)*100)/(count_bypassec_conseq_vulnibm_sh+count_bypassec_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO  \n")
    print("\n")
if((count_filemani_conseq_vulnibm_sh+count_filemani_conseq_vulnibm_iot)>0):
    print("      -    EN EL "+str(float(((count_filemani_conseq_vulnibm_sh+count_filemani_conseq_vulnibm_iot)*100)/(count_conseq_vulnibm_sh+count_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES LA CONSECUENCIA ES LA MANIPULACION DE FICHEROS. EL IMPACTO DE INTEGRIDAD VIENE ESPECIFICADO EN EL "+str(float(((count_filemani_conseq_vulnibm_sh_specified+count_filemani_conseq_vulnibm_iot_specified)*100)/(count_filemani_conseq_vulnibm_sh+count_filemani_conseq_vulnibm_iot)))+" % DE ELLAS. LOS PORCENTAJES DE IMPACTO DE INTEGRIDAD SON LOS SIGUIENTES :  \n")
    print("            -    EN EL "+str(float(((count_filemani_conseq_highintimpact_vulnibm_sh+count_filemani_conseq_highintimpact_vulnibm_iot)*100)/(count_filemani_conseq_vulnibm_sh+count_filemani_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
    print("            -    EN EL "+str(float(((count_filemani_conseq_lowintimpact_vulnibm_sh+count_filemani_conseq_lowintimpact_vulnibm_iot)*100)/(count_filemani_conseq_vulnibm_sh+count_filemani_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
    print("            -    EN EL "+str(float(((count_filemani_conseq_mediumintimpact_vulnibm_sh+count_filemani_conseq_mediumintimpact_vulnibm_iot)*100)/(count_filemani_conseq_vulnibm_sh+count_filemani_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO  \n")
    print("\n")
    
if((count_other_conseq_vulnibm_sh+count_other_conseq_vulnibm_iot)>0):
    print("      -    EN EL "+str(float(((count_other_conseq_vulnibm_sh+count_other_conseq_vulnibm_iot)*100)/(count_conseq_vulnibm_sh+count_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES LA CONSECUENCIA ES DISTINTA A LAS ANTERIORES. EL IMPACTO DE INTEGRIDAD VIENE ESPECIFICADO EN EL "+str(float(((count_other_conseq_vulnibm_sh_specified+count_other_conseq_vulnibm_iot_specified)*100)/(count_other_conseq_vulnibm_sh+count_other_conseq_vulnibm_iot)))+" % DE ELLAS. LOS PORCENTAJES DE IMPACTO DE INTEGRIDAD SON LOS SIGUIENTES :  \n")
    print("            -    EN EL "+str(float(((count_other_conseq_highintimpact_vulnibm_sh+count_other_conseq_highintimpact_vulnibm_iot)*100)/(count_other_conseq_vulnibm_sh+count_other_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO \n")
    print("            -    EN EL "+str(float(((count_other_conseq_lowintimpact_vulnibm_sh+count_other_conseq_lowintimpact_vulnibm_iot)*100)/(count_other_conseq_vulnibm_sh+count_other_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO \n")
    print("            -    EN EL "+str(float(((count_other_conseq_mediumintimpact_vulnibm_sh+count_other_conseq_mediumintimpact_vulnibm_iot)*100)/(count_other_conseq_vulnibm_sh+count_other_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO  \n")
    print("\n")
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	