
import pandas as pd

#Abro los ficheros con los que voy a tratar


df_cpe_iot=pd.read_excel('cpes_iot_2023.xlsx')
df_cpe_sh=pd.read_excel('cpes_smart_home_2023.xlsx')

#Variables donde almacenare el contador de tipo de referencia para IOT
count_none_ref_type_iot=0
count_version_ref_type_iot=0
count_product_ref_type_iot=0
count_advisory_ref_type_iot=0
count_changelog_ref_type_iot=0
count_vendor_ref_type_iot=0


for r in range(0,len(df_cpe_iot["cpes.refs.type"])):
    if('[' in df_cpe_iot["cpes.refs.type"][r]):
        aux=df_cpe_iot["cpes.refs.type"][r].split(",")
        for k in range(0,len(aux)):
            if(len(aux)>0):
                aux_str=aux[k].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
                if(aux_str == 'NONE'):
                    count_none_ref_type_iot+=1  
                elif(aux_str == 'Version'):
                    count_version_ref_type_iot+=1 
                elif(aux_str == 'Product'):
                    count_product_ref_type_iot+=1 
                elif(aux_str == 'Advisory'):
                    count_advisory_ref_type_iot+=1 
                elif((aux_str == 'Change Log') or (aux_str == 'ChangeLog')):
                    count_changelog_ref_type_iot+=1 
                elif(aux_str == 'Vendor'):
                    count_vendor_ref_type_iot+=1
                
    else:
        if(df_cpe_iot["cpes.refs.type"][r] == 'NONE'):
            count_none_ref_type_iot+=1  
        elif(df_cpe_iot["cpes.refs.type"][r] == 'Version'):
            count_version_ref_type_iot+=1 
        elif(df_cpe_iot["cpes.refs.type"][r] == 'Product'):
            count_product_ref_type_iot+=1 
        elif(df_cpe_iot["cpes.refs.type"][r] == 'Advisory'):
            count_advisory_ref_type_iot+=1 
        elif((df_cpe_iot["cpes.refs.type"][r] == 'Change Log') or(df_cpe_iot["cpes.refs.type"][r] == 'ChangeLog')):
            count_changelog_ref_type_iot+=1
        elif(df_cpe_iot["cpes.refs.type"][r] == 'Vendor'):
                count_vendor_ref_type_iot+=1
            
print("**************************ESTADÍSTICAS TIPOS DE REFERENCIA CPE IOT********************************")
print("\n")
print("EN LOS CPES HAY "+str(count_version_ref_type_iot)+" REFERENCIAS DE TIPO VERSION \n")
print("EN LOS CPES HAY "+str(count_product_ref_type_iot)+" REFERENCIAS DE TIPO PRODUCTO \n")
print("EN LOS CPES HAY "+str(count_advisory_ref_type_iot)+" REFERENCIAS DE TIPO ASESOR \n")
print("EN LOS CPES HAY "+str(count_changelog_ref_type_iot)+" REFERENCIAS DE TIPO CAMBIAR REGISTRO \n")
print("EN LOS CPES HAY "+str(count_vendor_ref_type_iot)+" REFERENCIAS DE TIPO VENDEDOR \n")
print("HAY  "+str(count_none_ref_type_iot)+" CPES EN LOS QUE NO EXISTEN REFERENCIAS \n")
print("\n")
print("**************************PORCENTAJE TIPO DE REFERENCIA CPE IOT********************************")
print("\n")
print("EL "+str(float(((count_version_ref_type_iot*100)/len(df_cpe_iot["cpes.refs.type"]))))+" % DE LOS CPES TIENEN REFERENCIAS DE TIPO VERSION \n")
print("EL "+str(float(((count_product_ref_type_iot*100)/len(df_cpe_iot["cpes.refs.type"]))))+" % DE LOS CPES TIENEN REFERENCIAS DE TIPO PRODUCTO \n")
print("EL "+str(float(((count_advisory_ref_type_iot*100)/len(df_cpe_iot["cpes.refs.type"]))))+" % DE LOS CPES TIENEN REFERENCIAS DE TIPO ASESOR \n")
print("EL "+str(float(((count_changelog_ref_type_iot*100)/len(df_cpe_iot["cpes.refs.type"]))))+" % DE LOS CPES TIENEN REFERENCIAS DE TIPO CAMBIAR REGISTRO \n")
print("EL "+str(float(((count_vendor_ref_type_iot*100)/len(df_cpe_iot["cpes.refs.type"]))))+" % DE LOS CPES TIENEN REFERENCIAS DE TIPO VENDEDOR \n")
print("EL "+str(float(((count_none_ref_type_iot*100)/len(df_cpe_iot["cpes.refs.type"]))))+" % DE LOS CPES NO TIENEN REFERENCIAS ESPECIFICADAS \n")
print("\n")



#Variables donde almacenare el contador de tipo de referencia para SMART HOME
count_none_ref_type_sh=0
count_version_ref_type_sh=0
count_product_ref_type_sh=0
count_advisory_ref_type_sh=0
count_changelog_ref_type_sh=0
count_vendor_ref_type_sh=0

for g in range(0,len(df_cpe_sh["cpes.refs.type"])):
    if('[' in df_cpe_sh["cpes.refs.type"][g]):
        aux=df_cpe_sh["cpes.refs.type"][g].split(",")
        for l in range(0,len(aux)):
            if(len(aux)>0):
                aux_str=aux[l].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
                if(aux_str == 'NONE'):
                    count_none_ref_type_sh+=1  
                elif(aux_str == 'Version'):
                    count_version_ref_type_sh+=1 
                elif(aux_str == 'Product'):
                    count_product_ref_type_sh+=1 
                elif(aux_str == 'Advisory'):
                    count_advisory_ref_type_sh+=1 
                elif((aux_str == 'Change Log') or (aux_str == 'ChangeLog')):
                    count_changelog_ref_type_sh+=1 
                elif(aux_str == 'Vendor'):
                    count_vendor_ref_type_sh+=1
    else:
        if(df_cpe_sh["cpes.refs.type"][g] == 'NONE'):
            count_none_ref_type_sh+=1  
        elif(df_cpe_sh["cpes.refs.type"][g] == 'Version'):
            count_version_ref_type_sh+=1 
        elif(df_cpe_sh["cpes.refs.type"][g] == 'Product'):
            count_product_ref_type_sh+=1 
        elif(df_cpe_sh["cpes.refs.type"][g] == 'Advisory'):
            count_advisory_ref_type_sh+=1 
        elif((df_cpe_sh["cpes.refs.type"][g] == 'Change Log') or(df_cpe_iot["cpes.refs.type"][g] == 'ChangeLog')):
            count_changelog_ref_type_sh+=1 
        elif(df_cpe_sh["cpes.refs.type"][g] == 'Vendor'):
                count_vendor_ref_type_sh+=1
print("**************************ESTADÍSTICAS TIPOS DE REFERENCIA CPE SMART HOME********************************")
print("\n")
print("EN LOS CPES HAY "+str(count_version_ref_type_sh)+" REFERENCIAS DE TIPO VERSION \n")
print("EN LOS CPES HAY "+str(count_product_ref_type_sh)+" REFERENCIAS DE TIPO PRODUCTO \n")
print("EN LOS CPES HAY "+str(count_advisory_ref_type_sh)+" REFERENCIAS DE TIPO ASESOR \n")
print("EN LOS CPES HAY "+str(count_changelog_ref_type_sh)+" REFERENCIAS DE TIPO CAMBIAR REGISTRO \n")
print("EN LOS CPES HAY "+str(count_vendor_ref_type_sh)+" REFERENCIAS DE TIPO VENDEDOR \n")
print("HAY  "+str(count_none_ref_type_sh)+" CPES EN LOS QUE NO EXISTEN REFERENCIAS \n")
print("\n")
print("**************************PORCENTAJE TIPO DE REFERENCIA CPE SMART HOME********************************")
print("\n")
print("EL "+str(float(((count_version_ref_type_sh*100)/len(df_cpe_sh["cpes.refs.type"]))))+" % DE LOS CPES TIENEN REFERENCIAS DE TIPO VERSION \n")
print("EL "+str(float(((count_product_ref_type_sh*100)/len(df_cpe_sh["cpes.refs.type"]))))+" % DE LOS CPES TIENEN REFERENCIAS DE TIPO PRODUCTO \n")
print("EL "+str(float(((count_advisory_ref_type_sh*100)/len(df_cpe_sh["cpes.refs.type"]))))+" % DE LOS CPES TIENEN REFERENCIAS DE TIPO ASESOR \n")
print("EL "+str(float(((count_changelog_ref_type_sh*100)/len(df_cpe_sh["cpes.refs.type"]))))+" % DE LOS CPES TIENEN REFERENCIAS DE TIPO CAMBIAR REGISTRO \n")
print("EL "+str(float(((count_vendor_ref_type_sh*100)/len(df_cpe_sh["cpes.refs.type"]))))+" % DE LOS CPES TIENEN REFERENCIAS DE TIPO VENDEDOR \n")
print("EL "+str(float(((count_none_ref_type_sh*100)/len(df_cpe_sh["cpes.refs.type"]))))+" % DE LOS CPES NO TIENEN REFERENCIAS ESPECIFICADAS \n")
print("\n")







print("**************************ESTADÍSTICAS TIPOS DE REFERENCIA CPE PARTE IOT Y SMART HOME CONJUNTAS ********************************")
print("\n")
print("EN LOS CPES HAY "+str(count_version_ref_type_sh+count_version_ref_type_iot)+" REFERENCIAS DE TIPO VERSION \n")
print("EN LOS CPES HAY "+str(count_product_ref_type_sh+count_product_ref_type_iot)+" REFERENCIAS DE TIPO PRODUCTO \n")
print("EN LOS CPES HAY "+str(count_advisory_ref_type_sh+count_advisory_ref_type_iot)+" REFERENCIAS DE TIPO ASESOR \n")
print("EN LOS CPES HAY "+str(count_changelog_ref_type_sh+count_changelog_ref_type_iot)+" REFERENCIAS DE TIPO CAMBIAR REGISTRO \n")
print("EN LOS CPES HAY "+str(count_vendor_ref_type_sh+count_vendor_ref_type_iot)+" REFERENCIAS DE TIPO VENDEDOR \n")
print("HAY  "+str(count_none_ref_type_sh+count_none_ref_type_iot)+" CPES EN LOS QUE NO EXISTEN REFERENCIAS \n")
print("\n")
print("**************************PORCENTAJE TIPO DE REFERENCIA CPE PARTE IOT Y SMART HOME CONJUNTAS********************************")
print("\n")
print("EL "+str(float((((count_version_ref_type_sh+count_version_ref_type_iot)*100)/(len(df_cpe_sh["cpes.refs.type"])+len(df_cpe_iot["cpes.refs.type"])))))+" % DE LOS CPES TIENEN REFERENCIAS DE TIPO VERSION \n")
print("EL "+str(float((((count_product_ref_type_sh+count_product_ref_type_iot)*100)/(len(df_cpe_sh["cpes.refs.type"])+len(df_cpe_iot["cpes.refs.type"])))))+" % DE LOS CPES TIENEN REFERENCIAS DE TIPO PRODUCTO \n")
print("EL "+str(float((((count_advisory_ref_type_sh+count_advisory_ref_type_iot)*100)/(len(df_cpe_sh["cpes.refs.type"])+len(df_cpe_iot["cpes.refs.type"])))))+" % DE LOS CPES TIENEN REFERENCIAS DE TIPO ASESOR \n")
print("EL "+str(float((((count_changelog_ref_type_sh+count_changelog_ref_type_iot)*100)/(len(df_cpe_sh["cpes.refs.type"])+len(df_cpe_iot["cpes.refs.type"])))))+" % DE LOS CPES TIENEN REFERENCIAS DE TIPO CAMBIAR REGISTRO \n")
print("EL "+str(float((((count_vendor_ref_type_sh+count_vendor_ref_type_iot)*100)/(len(df_cpe_sh["cpes.refs.type"])+len(df_cpe_iot["cpes.refs.type"])))))+" % DE LOS CPES TIENEN REFERENCIAS DE TIPO VENDEDOR \n")
print("EL "+str(float((((count_none_ref_type_sh+count_none_ref_type_iot)*100)/(len(df_cpe_sh["cpes.refs.type"])+len(df_cpe_iot["cpes.refs.type"])))))+" % DE LOS CPES NO TIENEN REFERENCIAS ESPECIFICADAS \n")
print("\n")
    
