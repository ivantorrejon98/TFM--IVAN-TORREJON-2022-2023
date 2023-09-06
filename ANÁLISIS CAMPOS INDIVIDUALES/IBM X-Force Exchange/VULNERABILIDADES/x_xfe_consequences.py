

import pandas as pd

#Abro los ficheros con los que voy a tratar

df_vuln_ibm_iot = pd.read_excel('vulnerabilidades_ibm_iot_2023.xlsx')
df_vuln_ibm_sh=pd.read_excel('vulnerabilidades_ibm_smart_home_2023.xlsx')




#Variables donde almacenare el contador de tipos de consecuencia para vulnerabilidades IBM IOT
obtaininfo_conseq_vuln_ibm_iot=0
gainprivileg_conseq_vuln_ibm_iot=0
xss_conseq_vuln_ibm_iot=0
bypassec_conseq_vuln_ibm_iot=0
gainaccess_conseq_vuln_ibm_iot=0
filemani_conseq_vuln_ibm_iot=0
dos_conseq_vuln_ibm_iot=0
other_iot=0
#Compruebo el tipo de consuencia en vulnerabilidades IBM para IOT

for i in range(0,len(df_vuln_ibm_iot["x_xfe_consequences"])):
    if(df_vuln_ibm_iot["x_xfe_consequences"][i]!='NONE' and df_vuln_ibm_iot["x_xfe_consequences"][i]!='Other'):
        if(df_vuln_ibm_iot["x_xfe_consequences"][i]=='Obtain Information'):
            obtaininfo_conseq_vuln_ibm_iot+=1
        elif(df_vuln_ibm_iot["x_xfe_consequences"][i]=='Gain Privileges' or df_vuln_ibm_iot["x_xfe_consequences"][i]=='Gain Privilege'):
            gainprivileg_conseq_vuln_ibm_iot+=1
        elif(df_vuln_ibm_iot["x_xfe_consequences"][i]=='Cross-Site Scripting'):
            xss_conseq_vuln_ibm_iot+=1
        elif(df_vuln_ibm_iot["x_xfe_consequences"][i]=='Bypass Security'):
            bypassec_conseq_vuln_ibm_iot+=1
        elif(df_vuln_ibm_iot["x_xfe_consequences"][i]=='Gain Access'):
            gainaccess_conseq_vuln_ibm_iot+=1
        elif(df_vuln_ibm_iot["x_xfe_consequences"][i]=='File Manipulation' or df_vuln_ibm_iot["x_xfe_consequences"][i]=='Data Manipulation'):
            filemani_conseq_vuln_ibm_iot+=1
        elif(df_vuln_ibm_iot["x_xfe_consequences"][i]=='Denial of Service'):
            dos_conseq_vuln_ibm_iot+=1
    else:
        other_iot+=1
        
consequences_iot=len(df_vuln_ibm_iot["x_xfe_consequences"])-other_iot

print("**************************ESTADÍSTICAS CONSECUENCIAS EN VULNERABILIDADES IBM IOT********************************")
print("\n")
print("EN "+str(obtaininfo_conseq_vuln_ibm_iot)+" VULNERABILIDADES LA CONSECUENCIA ES LA OBTENCION DE INFORMACIÓN \n")
print("EN "+str(gainprivileg_conseq_vuln_ibm_iot)+" VULNERABILIDADES LA CONSECUENCIA ES LA OBTENCION DE  PRIVILEGIOS \n")
print("EN "+str(xss_conseq_vuln_ibm_iot)+" VULNERABILIDADES LA CONSECUENCIA ES UN ATAQUE DE CROSS SITE SCRIPTING \n")
print("EN "+str(bypassec_conseq_vuln_ibm_iot)+" VULNERABILIDADES LA CONSECUENCIA ES SOBREPASAR LA SEGURIDAD \n")
print("EN "+str(gainaccess_conseq_vuln_ibm_iot)+" VULNERABILIDADES LA CONSECUENCIA ES LA OBTENCION DE ACCESO \n")
print("EN "+str(filemani_conseq_vuln_ibm_iot)+" VULNERABILIDADES LA CONSECUENCIA ES LA MANIPULACION DE ARCHIVOS/DATOS \n")
print("EN "+str(dos_conseq_vuln_ibm_iot)+" VULNERABILIDADES LA CONSECUENCIA ES UNA DENEGACION DE SERVICIO \n")
print("\n")
print("***************************PORCENTAJE CONSECUENCIAS EN VULNERABILIDADES IBM IOT********************************")
print("\n")
print("EN EL "+str(float(((obtaininfo_conseq_vuln_ibm_iot*100)/consequences_iot)))+"% DE LAS VULNERABILIDADES LA CONSECUENCIA ES LA OBTENCION DE INFORMACIÓN \n")
print("EN EL "+str(float(((gainprivileg_conseq_vuln_ibm_iot*100)/consequences_iot)))+"% DE LAS VULNERABILIDADES LA CONSECUENCIA ES LA OBTENCION DE  PRIVILEGIOS \n")
print("EN EL "+str(float(((xss_conseq_vuln_ibm_iot*100)/consequences_iot)))+"% DE LAS VULNERABILIDADES LA CONSECUENCIA ES UN ATAQUE DE CROSS SITE SCRIPTING \n")
print("EN EL "+str(float(((bypassec_conseq_vuln_ibm_iot*100)/consequences_iot)))+"% DE LAS VULNERABILIDADES LA CONSECUENCIA ES SOBREPASAR LA SEGURIDAD \n")
print("EN EL "+str(float(((gainaccess_conseq_vuln_ibm_iot*100)/consequences_iot)))+"% DE LAS VULNERABILIDADES LA CONSECUENCIA ES LA OBTENCION DE ACCESO \n")
print("EN EL "+str(float(((filemani_conseq_vuln_ibm_iot*100)/consequences_iot)))+"% DE LAS VULNERABILIDADES LA CONSECUENCIA ES LA MANIPULACION DE ARCHIVOS/DATOS \n")
print("EN EL "+str(float(((dos_conseq_vuln_ibm_iot*100)/consequences_iot)))+"% DE LAS VULNERABILIDADES LA CONSECUENCIA ES UNA DENEGACION DE SERVICIO \n")
print("\n")




#Variables donde almacenare el contador de tipos de consecuencia para vulnerabilidades IBM SMART HOME
obtaininfo_conseq_vuln_ibm_sh=0
gainprivileg_conseq_vuln_ibm_sh=0
xss_conseq_vuln_ibm_sh=0
bypassec_conseq_vuln_ibm_sh=0
gainaccess_conseq_vuln_ibm_sh=0
filemani_conseq_vuln_ibm_sh=0
dos_conseq_vuln_ibm_sh=0
other_sh=0
#Compruebo el tipo de consecuencia en vulnerabilidades IBM para SMART HOME

for j in range(0,len(df_vuln_ibm_sh["x_xfe_consequences"])):
    if(df_vuln_ibm_sh["x_xfe_consequences"][j]!='NONE' and df_vuln_ibm_sh["x_xfe_consequences"][j]!='Other'):
        if(df_vuln_ibm_sh["x_xfe_consequences"][j]=='Obtain Information'):
            obtaininfo_conseq_vuln_ibm_sh+=1
        elif(df_vuln_ibm_sh["x_xfe_consequences"][j]=='Gain Privileges' or df_vuln_ibm_sh["x_xfe_consequences"][j]=='Gain Privilege'):
            gainprivileg_conseq_vuln_ibm_sh+=1
        elif(df_vuln_ibm_sh["x_xfe_consequences"][j]=='Cross-Site Scripting'):
            xss_conseq_vuln_ibm_sh+=1
        elif(df_vuln_ibm_sh["x_xfe_consequences"][j]=='Bypass Security'):
            bypassec_conseq_vuln_ibm_sh+=1
        elif(df_vuln_ibm_sh["x_xfe_consequences"][j]=='Gain Access'):
            gainaccess_conseq_vuln_ibm_sh+=1
        elif(df_vuln_ibm_sh["x_xfe_consequences"][j]=='File Manipulation' or df_vuln_ibm_sh["x_xfe_consequences"][j]=='Data Manipulation'):
            filemani_conseq_vuln_ibm_sh+=1
        elif(df_vuln_ibm_sh["x_xfe_consequences"][j]=='Denial of Service'):
            dos_conseq_vuln_ibm_sh+=1
    else:
        other_sh+=1




consequences_sh=len(df_vuln_ibm_sh["x_xfe_consequences"])-other_sh

print("**************************ESTADÍSTICAS CONSECUENCIAS EN VULNERABILIDADES IBM SMART HOME********************************")
print("\n")
print("EN "+str(obtaininfo_conseq_vuln_ibm_sh)+" VULNERABILIDADES LA CONSECUENCIA ES LA OBTENCION DE INFORMACIÓN \n")
print("EN "+str(gainprivileg_conseq_vuln_ibm_sh)+" VULNERABILIDADES LA CONSECUENCIA ES LA OBTENCION DE  PRIVILEGIOS \n")
print("EN "+str(xss_conseq_vuln_ibm_sh)+" VULNERABILIDADES LA CONSECUENCIA ES UN ATAQUE DE CROSS SITE SCRIPTING \n")
print("EN "+str(bypassec_conseq_vuln_ibm_sh)+" VULNERABILIDADES LA CONSECUENCIA ES SOBREPASAR LA SEGURIDAD \n")
print("EN "+str(gainaccess_conseq_vuln_ibm_sh)+" VULNERABILIDADES LA CONSECUENCIA ES LA OBTENCION DE ACCESO \n")
print("EN "+str(filemani_conseq_vuln_ibm_sh)+" VULNERABILIDADES LA CONSECUENCIA ES LA MANIPULACION DE ARCHIVOS \n")
print("EN "+str(dos_conseq_vuln_ibm_sh)+" VULNERABILIDADES LA CONSECUENCIA ES UNA DENEGACION DE SERVICIO \n")
print("\n")
print("***************************PORCENTAJE CONSECUENCIAS EN VULNERABILIDADES IBM SMART HOME********************************")
print("\n")
print("EN EL "+str(float(((obtaininfo_conseq_vuln_ibm_sh*100)/consequences_sh)))+"% DE LAS VULNERABILIDADES LA CONSECUENCIA ES LA OBTENCION DE INFORMACIÓN \n")
print("EN EL "+str(float(((gainprivileg_conseq_vuln_ibm_sh*100)/consequences_sh)))+"% DE LAS VULNERABILIDADES LA CONSECUENCIA ES LA OBTENCION DE  PRIVILEGIOS \n")
print("EN EL "+str(float(((xss_conseq_vuln_ibm_sh*100)/consequences_sh)))+"% DE LAS VULNERABILIDADES LA CONSECUENCIA ES UN ATAQUE DE CROSS SITE SCRIPTING \n")
print("EN EL "+str(float(((bypassec_conseq_vuln_ibm_sh*100)/consequences_sh)))+"% DE LAS VULNERABILIDADES LA CONSECUENCIA ES SOBREPASAR LA SEGURIDAD \n")
print("EN EL "+str(float(((gainaccess_conseq_vuln_ibm_sh*100)/consequences_sh)))+"% DE LAS VULNERABILIDADES LA CONSECUENCIA ES LA OBTENCION DE ACCESO \n")
print("EN EL "+str(float(((filemani_conseq_vuln_ibm_sh*100)/consequences_sh)))+"% DE LAS VULNERABILIDADES LA CONSECUENCIA ES LA MANIPULACION DE ARCHIVOS/DATOS \n")
print("EN EL "+str(float(((dos_conseq_vuln_ibm_sh*100)/consequences_sh)))+"% DE LAS VULNERABILIDADES LA CONSECUENCIA ES UNA DENEGACION DE SERVICIO \n")
print("\n")






print("**************************ESTADÍSTICAS CONSECUENCIAS EN VULNERABILIDADES IBM PARTE IOT Y SMART HOME CONJUNTAS********************************")
print("\n")
print("EN "+str(obtaininfo_conseq_vuln_ibm_sh+obtaininfo_conseq_vuln_ibm_iot)+" VULNERABILIDADES LA CONSECUENCIA ES LA OBTENCION DE INFORMACIÓN \n")
print("EN "+str(gainprivileg_conseq_vuln_ibm_sh+gainprivileg_conseq_vuln_ibm_iot)+" VULNERABILIDADES LA CONSECUENCIA ES LA OBTENCION DE  PRIVILEGIOS \n")
print("EN "+str(xss_conseq_vuln_ibm_sh+xss_conseq_vuln_ibm_iot)+" VULNERABILIDADES LA CONSECUENCIA ES UN ATAQUE DE CROSS SITE SCRIPTING \n")
print("EN "+str(bypassec_conseq_vuln_ibm_sh+bypassec_conseq_vuln_ibm_iot)+" VULNERABILIDADES LA CONSECUENCIA ES SOBREPASAR LA SEGURIDAD \n")
print("EN "+str(gainaccess_conseq_vuln_ibm_sh+gainaccess_conseq_vuln_ibm_iot)+" VULNERABILIDADES LA CONSECUENCIA ES LA OBTENCION DE ACCESO \n")
print("EN "+str(filemani_conseq_vuln_ibm_sh+filemani_conseq_vuln_ibm_iot)+" VULNERABILIDADES LA CONSECUENCIA ES LA MANIPULACION DE ARCHIVOS/DATOS \n")
print("EN "+str(dos_conseq_vuln_ibm_sh+dos_conseq_vuln_ibm_iot)+" VULNERABILIDADES LA CONSECUENCIA ES UNA DENEGACION DE SERVICIO \n")
print("\n")
print("***************************PORCENTAJE CONSECUENCIAS EN VULNERABILIDADES IBM PARTE IOT Y SMART HOME CONJUNTAS********************************")
print("\n")
print("EN EL "+str(float((((obtaininfo_conseq_vuln_ibm_sh+obtaininfo_conseq_vuln_ibm_iot)*100)/(consequences_iot+consequences_sh))))+"% DE LAS VULNERABILIDADES LA CONSECUENCIA ES LA OBTENCION DE INFORMACIÓN \n")
print("EN EL "+str(float((((gainprivileg_conseq_vuln_ibm_sh+gainprivileg_conseq_vuln_ibm_iot)*100)/(consequences_iot+consequences_sh))))+"% DE LAS VULNERABILIDADES LA CONSECUENCIA ES LA OBTENCION DE  PRIVILEGIOS \n")
print("EN EL "+str(float((((xss_conseq_vuln_ibm_sh+xss_conseq_vuln_ibm_iot)*100)/(consequences_iot+consequences_sh))))+"% DE LAS VULNERABILIDADES LA CONSECUENCIA ES UN ATAQUE DE CROSS SITE SCRIPTING \n")
print("EN EL "+str(float((((bypassec_conseq_vuln_ibm_sh+bypassec_conseq_vuln_ibm_iot)*100)/(consequences_iot+consequences_sh))))+"% DE LAS VULNERABILIDADES LA CONSECUENCIA ES SOBREPASAR LA SEGURIDAD \n")
print("EN EL "+str(float((((gainaccess_conseq_vuln_ibm_sh+gainaccess_conseq_vuln_ibm_iot)*100)/(consequences_iot+consequences_sh))))+"% DE LAS VULNERABILIDADES LA CONSECUENCIA ES LA OBTENCION DE ACCESO \n")
print("EN EL "+str(float((((filemani_conseq_vuln_ibm_sh+filemani_conseq_vuln_ibm_iot)*100)/(consequences_iot+consequences_sh))))+"% DE LAS VULNERABILIDADES LA CONSECUENCIA ES LA MANIPULACION DE ARCHIVOS/DATOS \n")
print("EN EL "+str(float((((dos_conseq_vuln_ibm_sh+dos_conseq_vuln_ibm_iot)*100)/(consequences_iot+consequences_sh))))+"% DE LAS VULNERABILIDADES LA CONSECUENCIA ES UNA DENEGACION DE SERVICIO \n")
print("\n")























