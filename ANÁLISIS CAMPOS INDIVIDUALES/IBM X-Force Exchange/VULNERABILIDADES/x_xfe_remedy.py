

import pandas as pd

#Abro los ficheros con los que voy a tratar

df_vulnibm_iot = pd.read_excel('vulnerabilidades_ibm_iot_2023.xlsx')

#Variables para almacenar los distintos remedios para las vulnerabilidades
count_vulnibm_iot_remedy=0
count_vulnibm_iot_noremedy=0
count_vulnibm_iot_refer=0
count_vulnibm_iot_upgrade=0
count_vulnibm_iot_applypatch=0


#Comprobamos el contenido de xfe_remedy
for r in range(0,len(df_vulnibm_iot["x_xfe_remedy"])):
    if(df_vulnibm_iot["x_xfe_remedy"][r]!='NONE'):
        count_vulnibm_iot_remedy+=1
        if('No remedy' in df_vulnibm_iot["x_xfe_remedy"][r]):
            count_vulnibm_iot_noremedy+=1
        elif('Refer to' in df_vulnibm_iot["x_xfe_remedy"][r]):
            count_vulnibm_iot_refer+=1       
        elif('Upgrade to the latest' in df_vulnibm_iot["x_xfe_remedy"][r]):
            count_vulnibm_iot_upgrade+=1
        elif(('apply' in df_vulnibm_iot["x_xfe_remedy"][r] or 'Apply' in df_vulnibm_iot["x_xfe_remedy"][r]) and ('patch' in df_vulnibm_iot["x_xfe_remedy"][r] or 'Patch' in df_vulnibm_iot["x_xfe_remedy"][r])):
            count_vulnibm_iot_applypatch+=1
            
            
            
print("**************************ESTADÍSTICAS REMEDIO VULNERABILIDADES IBM PARTE IOT**************************")
print("\n")                            
print("\n")
print(" DE UN TOTAL DE "+str(count_vulnibm_iot_remedy)+" VALORES DE REMEDIO DE VULNERABILIDADES :\n") 
print("\n")
print("   - LAS ESTADISTICAS DE REMEDIO SON LAS SIGUIENTES:  \n")
print("      -    EN  "+str(count_vulnibm_iot_noremedy)+" VULNERABILIDADES NO HAY NINGUN REMEDIO \n")
print("      -    EN  "+str(count_vulnibm_iot_upgrade)+" VULNERABILIDADES EL REMEDIO ES ACTUALIZAR A LA ULTIMA VERSION DEL PRODUCTO  \n")
print("      -    EN  "+str(count_vulnibm_iot_applypatch)+" VULNERABILIDADES EL REMEDIO ES APLICAR UN PARCHE \n")
print("      -    EN  "+str(count_vulnibm_iot_refer)+" VULNERABILIDADES EL REMEDIO ES REFERIRSE A UN SITIO OFICIAL PARA CONSEGUIR INFORMACION SOBRE LA VULNERABILIDAD  \n")
      
print("**************************PORCENTAJES REMEDIO VULNERABILIDADES IBM PARTE IOT **************************")
print("\n")                            
print("\n")
print(" DE UN TOTAL DE "+str(count_vulnibm_iot_remedy)+" VALORES DE REMEDIO DE VULNERABILIDADES :\n") 
print("\n")
print("   - LOS PORCENTAJES DE REMEDIO SON LOS SIGUIENTES:  \n")
if(count_vulnibm_iot_remedy>0):
    print("      -    EN EL "+str(float((count_vulnibm_iot_noremedy*100)/count_vulnibm_iot_remedy))+" % DE VULNERABILIDADES NO HAY NINGUN REMEDIO \n")
    print("      -    EN EL "+str(float((count_vulnibm_iot_upgrade*100)/count_vulnibm_iot_remedy))+" % DE VULNERABILIDADES EL REMEDIO ES ACTUALIZAR A LA ULTIMA VERSION DEL PRODUCTO \n")
    print("      -    EN EL "+str(float((count_vulnibm_iot_applypatch*100)/count_vulnibm_iot_remedy))+" % DE VULNERABILIDADES EL REMEDIO ES APLICAR UN PARCHE \n")   
    print("      -    EN EL "+str(float((count_vulnibm_iot_refer*100)/count_vulnibm_iot_remedy))+" % DE VULNERABILIDADES EL REMEDIO ES REFERIRSE A UN SITIO OFICIAL PARA CONSEGUIR INFORMACION SOBRE LA VULNERABILIDAD \n")

        
        
df_vulnibm_sh = pd.read_excel('vulnerabilidades_ibm_smart_home_2023.xlsx')


#Variables para almacenar el remedio de las vulnerabilidades para la parte smart home
count_vulnibm_sh_remedy=0
count_vulnibm_sh_noremedy=0
count_vulnibm_sh_refer=0
count_vulnibm_sh_refer_mediatek=0
count_vulnibm_sh_refer_intel=0
count_vulnibm_sh_refer_cisco=0
count_vulnibm_sh_refer_lenovo=0
count_vulnibm_sh_refer_apple=0
count_vulnibm_sh_refer_adobe=0
count_vulnibm_sh_refer_siemens=0
count_vulnibm_sh_refer_ibm=0
count_vulnibm_sh_refer_oracle=0
count_vulnibm_sh_refer_mozilla=0
count_vulnibm_sh_refer_another=0
count_vulnibm_sh_upgrade=0
count_vulnibm_sh_applypatch=0
      
#Comprobamos el contenido de xfe_remedy
for r in range(0,len(df_vulnibm_sh["x_xfe_remedy"])):
    if(df_vulnibm_sh["x_xfe_remedy"][r]!='NONE'):
        count_vulnibm_sh_remedy+=1
        if('No remedy' in df_vulnibm_sh["x_xfe_remedy"][r]):
            count_vulnibm_sh_noremedy+=1
        elif('Refer to' in df_vulnibm_sh["x_xfe_remedy"][r]):
            count_vulnibm_sh_refer+=1
        elif('Upgrade to the latest' in df_vulnibm_sh["x_xfe_remedy"][r]):
            count_vulnibm_sh_upgrade+=1
        elif(('apply' in df_vulnibm_sh["x_xfe_remedy"][r] or 'Apply' in df_vulnibm_sh["x_xfe_remedy"][r]) and ('patch' in df_vulnibm_sh["x_xfe_remedy"][r] or 'Patch' in df_vulnibm_sh["x_xfe_remedy"][r])):
            count_vulnibm_sh_applypatch+=1
        
print("**************************ESTADÍSTICAS REMEDIO VULNERABILIDADES IBM PARTE SMART HOME**************************")
print("\n")                            
print("\n")
print(" DE UN TOTAL DE "+str(count_vulnibm_sh_remedy)+" VALORES DE REMEDIO DE VULNERABILIDADES :\n") 
print("\n")
print("   - LAS ESTADISTICAS DE REMEDIO SON LAS SIGUIENTES:  \n")
print("      -    EN  "+str(count_vulnibm_sh_noremedy)+" VULNERABILIDADES NO HAY NINGUN REMEDIO  \n")
print("      -    EN  "+str(count_vulnibm_sh_upgrade)+" VULNERABILIDADES EL REMEDIO ES ACTUALIZAR A LA ULTIMA VERSION DEL PRODUCTO  \n")
print("      -    EN  "+str(count_vulnibm_sh_applypatch)+" VULNERABILIDADES EL REMEDIO ES APLICAR UN PARCHE \n")
print("      -    EN  "+str(count_vulnibm_sh_refer)+" VULNERABILIDADES EL REMEDIO ES REFERIRSE A UN SITIO OFICIAL PARA CONSEGUIR INFORMACION SOBRE LA VULNERABILIDAD  \n")

print("**************************PORCENTAJES REMEDIO VULNERABILIDADES IBM PARTE SMART HOME **************************")
print("\n")                            
print("\n")
print(" DE UN TOTAL DE "+str(count_vulnibm_sh_remedy)+" VALORES DE REMEDIO DE VULNERABILIDADES :\n") 
print("\n")
print("   - LOS PORCENTAJES DE REMEDIO SON LOS SIGUIENTES:  \n")
if(count_vulnibm_sh_remedy>0):
    print("      -    EN EL "+str(float((count_vulnibm_sh_noremedy*100)/count_vulnibm_sh_remedy))+" % DE VULNERABILIDADES NO HAY NINGUN REMEDIO \n")
    print("      -    EN EL "+str(float((count_vulnibm_sh_upgrade*100)/count_vulnibm_sh_remedy))+" % DE VULNERABILIDADES EL REMEDIO ES ACTUALIZAR A LA ULTIMA VERSION DEL PRODUCTO \n")
    print("      -    EN EL "+str(float((count_vulnibm_sh_applypatch*100)/count_vulnibm_sh_remedy))+" % DE VULNERABILIDADES EL REMEDIO ES APLICAR UN PARCHE \n")   
    print("      -    EN EL "+str(float((count_vulnibm_sh_refer*100)/count_vulnibm_sh_remedy))+" % DE VULNERABILIDADES EL REMEDIO ES REFERIRSE A UN SITIO OFICIAL PARA CONSEGUIR INFORMACION SOBRE LA VULNERABILIDAD \n")





print("**************************ESTADÍSTICAS REMEDIO VULNERABILIDADES IBM PARTE IOT Y SMART HOME CONJUNTAS**************************")
print("\n")                            
print("\n")
print(" DE UN TOTAL DE "+str(count_vulnibm_sh_remedy+count_vulnibm_iot_remedy)+" VALORES DE REMEDIO DE VULNERABILIDADES :\n") 
print("\n")
print("   - LAS ESTADISTICAS DE REMEDIO SON LAS SIGUIENTES:  \n")
print("      -    EN  "+str(count_vulnibm_sh_noremedy+count_vulnibm_iot_noremedy)+" VULNERABILIDADES NO HAY NINGUN REMEDIO  \n")
print("      -    EN  "+str(count_vulnibm_sh_upgrade+count_vulnibm_iot_upgrade)+" VULNERABILIDADES EL REMEDIO ES ACTUALIZAR A LA ULTIMA VERSION DEL PRODUCTO  \n")
print("      -    EN  "+str(count_vulnibm_sh_applypatch+count_vulnibm_iot_applypatch)+" VULNERABILIDADES EL REMEDIO ES APLICAR UN PARCHE \n")
print("      -    EN  "+str(count_vulnibm_iot_refer+count_vulnibm_sh_refer)+" VULNERABILIDADES EL REMEDIO ES REFERIRSE A UN SITIO OFICIAL PARA CONSEGUIR INFORMACION SOBRE LA VULNERABILIDAD  \n")

print("**************************PORCENTAJES REMEDIO VULNERABILIDADES IBM PARTE IOT Y SMART HOME CONJUNTAS **************************")
print("\n")                            
print("\n")
print(" DE UN TOTAL DE "+str(count_vulnibm_sh_remedy+count_vulnibm_iot_remedy)+" VALORES DE REMEDIO DE VULNERABILIDADES :\n") 
print("\n")
print("   - LOS PORCENTAJES DE REMEDIO SON LOS SIGUIENTES:  \n")
if((count_vulnibm_sh_remedy+count_vulnibm_iot_remedy)>0):
    print("      -    EN EL "+str(float(((count_vulnibm_sh_noremedy+count_vulnibm_iot_noremedy)*100)/(count_vulnibm_sh_remedy+count_vulnibm_iot_remedy)))+" % DE VULNERABILIDADES NO HAY NINGUN REMEDIO \n")
    print("      -    EN EL "+str(float(((count_vulnibm_sh_upgrade+count_vulnibm_iot_upgrade)*100)/(count_vulnibm_sh_remedy+count_vulnibm_iot_remedy)))+" % DE VULNERABILIDADES EL REMEDIO ES ACTUALIZAR A LA ULTIMA VERSION DEL PRODUCTO \n")
    print("      -    EN EL "+str(float(((count_vulnibm_sh_applypatch+count_vulnibm_iot_applypatch)*100)/(count_vulnibm_sh_remedy+count_vulnibm_iot_remedy)))+" % DE VULNERABILIDADES EL REMEDIO ES APLICAR UN PARCHE \n")   
    print("      -    EN EL "+str(float(((count_vulnibm_sh_refer+count_vulnibm_iot_refer)*100)/(count_vulnibm_sh_remedy+count_vulnibm_iot_remedy)))+" % DE VULNERABILIDADES EL REMEDIO ES REFERIRSE A UN SITIO OFICIAL PARA CONSEGUIR INFORMACION SOBRE LA VULNERABILIDAD \n")





