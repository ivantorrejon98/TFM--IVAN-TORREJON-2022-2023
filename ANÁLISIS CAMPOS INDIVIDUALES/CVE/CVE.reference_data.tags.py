#*******************************************************ETIQUETAS ASOCIADAS A DATOS DE REFERENCIA CVE****************************************************************


import pandas as pd

#Abro los ficheros con los que voy a tratar


df_cve_sh=pd.read_excel('cves_iot_2023.xlsx')
df_cve_sh=pd.read_excel('cves_smart_home_2023.xlsx')


#Variables donde almacenare el contador de los distintos TAGS DE referencias externas para la parte de IOT
tag_thirdpartyadv_iot=0
tag_exploit_iot=0
tag_techndescript_iot=0
tag_issuetrack_iot=0
tag_patch_iot=0
tag_vendadv_iot=0
tag_brokenlink_iot=0
tag_usgovern_iot=0
tag_mailist_iot=0
tag_product_iot=0
tag_permissions_iot=0
tag_vdb_iot=0
tag_release_iot=0
tag_mitigation_iot=0
tag_other_iot=0
counter_tags_iot=0

#Recorro los valores de REFERENCE DATA TAGS para la parte IOT


#Comprobamos LA ETIQUETA asociado a la referencia 
for j in range(0,len(df_cve_iot["CVE_Items.cve.references.reference_data.tags"])):
    if('[' in df_cve_iot["CVE_Items.cve.references.reference_data.tags"][j]):
        #Obtengo los distintos valores de referencias de tags
        aux=df_cve_iot["CVE_Items.cve.references.reference_data.tags"][j].split(",")
        for l in range(0,len(aux)):
            if(len(aux)>0):
                aux_str=aux[l].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
                if(aux_str!='NONE' and aux_str!='null' and aux_str!='NotApplicable'):
                    #Aumento el contador de numero de tags existentes que tengan valor definido
                    counter_tags_iot+=1
                    if(aux_str == "ThirdPartyAdvisory"):
                        tag_thirdpartyadv_iot+=1
                    elif(aux_str == "Exploit"):
                        tag_exploit_iot+=1
                    elif(aux_str == "TechnicalDescription"):
                        tag_techndescript_iot+=1
                    elif(aux_str == "IssueTracking"):
                        tag_issuetrack_iot+=1
                    elif(aux_str == "Patch"):
                        tag_patch_iot+=1
                    elif(aux_str == "VendorAdvisory"):
                        tag_vendadv_iot+=1
                    elif(aux_str == "BrokenLink"):
                        tag_brokenlink_iot+=1
                    elif(aux_str == "USGovernmentResource"):
                        tag_usgovern_iot+=1
                    elif(aux_str == "MailingList"):
                        tag_mailist_iot+=1
                    elif(aux_str == "Product"):
                        tag_product_iot+=1
                    elif(aux_str == "PermissionsRequired"):
                        tag_permissions_iot+=1
                    elif(aux_str == "VDBEntry"):
                        tag_vdb_iot+=1
                    elif(aux_str == "ReleaseNotes"):
                        tag_release_iot+=1
                    elif(aux_str == "Mitigation"):
                        tag_mitigation_iot+=1
                    else:
                        print(aux_str)
                        tag_other_iot+=1 
    else:
        aux_str=df_cve_iot["CVE_Items.cve.references.reference_data.tags"][j].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
        if(aux_str!='NONE' and aux_str!='null' and aux_str!='NotApplicable'):
            counter_tags_iot+=1
            if(aux_str == "ThirdPartyAdvisory"):
                tag_thirdpartyadv_iot+=1
            elif(aux_str == "Exploit"):
                tag_exploit_iot+=1
            elif(aux_str == "TechnicalDescription"):
                tag_techndescript_iot+=1
            elif(aux_str == "IssueTracking"):
                tag_issuetrack_iot+=1
            elif(aux_str == "Patch"):
                tag_patch_iot+=1
            elif(aux_str == "VendorAdvisory"):
                tag_vendadv_iot+=1
            elif(aux_str == "BrokenLink"):
                tag_brokenlink_iot+=1
            elif(aux_str == "USGovernmentResource"):
                tag_usgovern_iot+=1
            elif(aux_str == "MailingList"):
                tag_mailist_iot+=1
            elif(aux_str == "Product"):
                tag_product_iot+=1
            elif(aux_str == "PermissionsRequired"):
                tag_permissions_iot+=1
            elif(aux_str == "VDBEntry"):
                tag_vdb_iot+=1
            elif(aux_str == "ReleaseNotes"):
                tag_release_iot+=1
            elif(aux_str == "Mitigation"):
                tag_mitigation_iot+=1
            else:
                print(aux_str)
                tag_other_iot+=1 
        



        
print("************************** ESTADÍSTICAS ETIQUETAS ASOCIADAS A REFERENCIAS CVE IOT********************************")
print("\n")
print(" DE UN TOTAL DE "+str(counter_tags_iot)+" REFERENCIAS, LAS ESTADÍSTICAS DE LAS ETIQUETAS ASOCIADAS A LAS REFERENCIAS SON LAS SIGUIENTES :")
print("\n")
print("       -  EN "+str(tag_thirdpartyadv_iot)+" REFERENCIAS LA ETIQUETA ES THIRD PARTY ADVISORY \n")
print("       -  EN "+str(tag_exploit_iot)+" REFERENCIAS LA ETIQUETA ES EXPLOIT \n")
print("       -  EN "+str(tag_techndescript_iot)+" REFERENCIAS LA ETIQUETA ES TECHNICAL DESCRIPTION \n")
print("       -  EN "+str(tag_issuetrack_iot)+" REFERENCIAS LA ETIQUETA ES ISSUE TRACKING \n")
print("       -  EN "+str(tag_patch_iot)+" REFERENCIAS LA ETIQUETA ES PATCH \n")
print("       -  EN "+str(tag_vendadv_iot)+" REFERENCIAS LA ETIQUETA ES VENDOR ADVISORY \n")
print("       -  EN "+str(tag_brokenlink_iot)+" REFERENCIAS LA ETIQUETA ES BROKEN LINK \n")
print("       -  EN "+str(tag_usgovern_iot)+" REFERENCIAS LA ETIQUETA ES US GOVERNMENT RESOURCE \n")
print("       -  EN "+str(tag_mailist_iot)+" REFERENCIAS LA ETIQUETA ES MAILIST \n")
print("       -  EN "+str(tag_product_iot)+" REFERENCIAS LA ETIQUETA ES PRODUCT \n")
print("       -  EN "+str(tag_permissions_iot)+" REFERENCIAS LA ETIQUETA ES PERMISSIONS REQUIRED \n")
print("       -  EN "+str(tag_vdb_iot)+" REFERENCIAS LA ETIQUETA ES VDB ENTRY \n")
print("       -  EN "+str(tag_release_iot)+" REFERENCIAS LA ETIQUETA ES RELEASE \n")
print("       -  EN "+str(tag_mitigation_iot)+" REFERENCIAS LA ETIQUETA ES MITIGATION \n")
print("       -  EN "+str(tag_other_iot)+" REFERENCIAS LA ETIQUETA ES DISTINTO A LOS ANTERIORES \n")
print("\n")

print("**************************PORCENTAJES ETIQUETAS ASOCIADAS A REFERENCIAS CVE IOT********************************")
print("\n")
print("\n")
print(" DE UN TOTAL DE "+str(counter_tags_iot)+" REFERENCIAS, LOS PORCENTAJES DE LAS ETIQUETAS ASOCIADAS A LAS REFERENCIAS SON LOS SIGUIENTES :")
print("\n")
print("       -  EN EL "+str(float(((tag_thirdpartyadv_iot*100)/counter_tags_iot)))+" % DE LAS REFERENCIAS LA ETIQUETA ES THIRD PARTY ADVISORY \n")
print("       -  EN EL "+str(float(((tag_exploit_iot*100)/counter_tags_iot)))+" % DE LAS REFERENCIAS LA ETIQUETA ES EXPLOIT \n")
print("       -  EN EL "+str(float(((tag_techndescript_iot*100)/counter_tags_iot)))+" % DE LAS REFERENCIAS LA ETIQUETA ES TECHNICAL DESCRIPTION \n")
print("       -  EN EL "+str(float(((tag_issuetrack_iot*100)/counter_tags_iot)))+" % DE LAS REFERENCIAS LA ETIQUETA ES ISSUE TRACKING \n")
print("       -  EN EL "+str(float(((tag_patch_iot*100)/counter_tags_iot)))+" % DE LAS REFERENCIAS LA ETIQUETA ES PATCH \n")
print("       -  EN EL "+str(float(((tag_vendadv_iot*100)/counter_tags_iot)))+" % DE LAS REFERENCIAS LA ETIQUETA ES VENDOR ADVISORY \n")
print("       -  EN EL "+str(float(((tag_brokenlink_iot*100)/counter_tags_iot)))+" % DE LAS REFERENCIAS LA ETIQUETA ES BROKEN LINK \n")
print("       -  EN EL "+str(float(((tag_usgovern_iot*100)/counter_tags_iot)))+" % DE LAS REFERENCIAS LA ETIQUETA ES US GOVERNMENT RESOURCE \n")
print("       -  EN EL "+str(float(((tag_mailist_iot*100)/counter_tags_iot)))+" % DE LAS REFERENCIAS LA ETIQUETA ES MAILIST \n")
print("       -  EN EL "+str(float(((tag_product_iot*100)/counter_tags_iot)))+" % DE LAS REFERENCIAS LA ETIQUETA ES PRODUCT \n")
print("       -  EN EL "+str(float(((tag_permissions_iot*100)/counter_tags_iot)))+" % DE LAS REFERENCIAS LA ETIQUETA ES PERMISSIONS REQUIRED \n")
print("       -  EN EL "+str(float(((tag_vdb_iot*100)/counter_tags_iot)))+" % DE LAS REFERENCIAS LA ETIQUETA ES VDB ENTRY \n")   
print("       -  EN EL "+str(float(((tag_release_iot*100)/counter_tags_iot)))+" % DE LAS REFERENCIAS LA ETIQUETA ES RELEASE \n")
print("       -  EN EL "+str(float(((tag_mitigation_iot*100)/counter_tags_iot)))+" % DE LAS REFERENCIAS LA ETIQUETA ES MITIGATION \n")
print("       -  EN EL "+str(float(((tag_other_iot*100)/counter_tags_iot)))+" % DE LAS REFERENCIAS LA ETIQUETA ES DISTINTO A LOS ANTERIORES \n")


#Variables donde almacenare el contador de los distintos TAGS DE referencias externas para la parte de SMART HOME
tag_thirdpartyadv_sh=0
tag_exploit_sh=0
tag_techndescript_sh=0
tag_issuetrack_sh=0
tag_patch_sh=0
tag_vendadv_sh=0
tag_brokenlink_sh=0
tag_usgovern_sh=0
tag_mailist_sh=0
tag_product_sh=0
tag_permissions_sh=0
tag_vdb_sh=0
tag_release_sh=0
tag_mitigation_sh=0
tag_other_sh=0
counter_tags_sh=0





#Recorro los valores de REFERENCE DATA TAGS para la PARTE SMART HOME



#Comprobamos LA ETIQUETA asociado a la referencia 
for j in range(0,len(df_cve_sh["CVE_Items.cve.references.reference_data.tags"])):
    if('[' in df_cve_sh["CVE_Items.cve.references.reference_data.tags"][j]):
        #Obtengo los distintos valores de referencias de tags
        aux=df_cve_sh["CVE_Items.cve.references.reference_data.tags"][j].split(",")
        for l in range(0,len(aux)):
            if(len(aux)>0):
                aux_str=aux[l].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
                if(aux_str!='NONE' and aux_str!='null' and aux_str!='NotApplicable'):
                    #Aumento el contador de numero de tags existentes que tengan valor definido
                    counter_tags_sh+=1
                    if(aux_str == "ThirdPartyAdvisory"):
                        tag_thirdpartyadv_sh+=1
                    elif(aux_str == "Exploit"):
                        tag_exploit_sh+=1
                    elif(aux_str == "TechnicalDescription"):
                        tag_techndescript_sh+=1
                    elif(aux_str == "IssueTracking"):
                        tag_issuetrack_sh+=1
                    elif(aux_str == "Patch"):
                        tag_patch_sh+=1
                    elif(aux_str == "VendorAdvisory"):
                        tag_vendadv_sh+=1
                    elif(aux_str == "BrokenLink"):
                        tag_brokenlink_sh+=1
                    elif(aux_str == "USGovernmentResource"):
                        tag_usgovern_sh+=1
                    elif(aux_str == "MailingList"):
                        tag_mailist_sh+=1
                    elif(aux_str == "Product"):
                        tag_product_sh+=1
                    elif(aux_str == "PermissionsRequired"):
                        tag_permissions_sh+=1
                    elif(aux_str == "VDBEntry"):
                        tag_vdb_sh+=1
                    elif(aux_str == "ReleaseNotes"):
                        tag_release_sh+=1
                    elif(aux_str == "Mitigation"):
                        tag_mitigation_sh+=1
                    else:
                        print(aux_str)
                        tag_other_sh+=1 
    else:
        aux_str=df_cve_sh["CVE_Items.cve.references.reference_data.tags"][j].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
        if(aux_str!='NONE' and aux_str!='null' and aux_str!='NotApplicable'):
            counter_tags_sh+=1
            if(aux_str == "ThirdPartyAdvisory"):
                tag_thirdpartyadv_sh+=1
            elif(aux_str == "Exploit"):
                tag_exploit_sh+=1
            elif(aux_str == "TechnicalDescription"):
                tag_techndescript_sh+=1
            elif(aux_str == "IssueTracking"):
                tag_issuetrack_sh+=1
            elif(aux_str == "Patch"):
                tag_patch_sh+=1
            elif(aux_str == "VendorAdvisory"):
                tag_vendadv_sh+=1
            elif(aux_str == "BrokenLink"):
                tag_brokenlink_sh+=1
            elif(aux_str == "USGovernmentResource"):
                tag_usgovern_sh+=1
            elif(aux_str == "MailingList"):
                tag_mailist_sh+=1
            elif(aux_str == "Product"):
                tag_product_sh+=1
            elif(aux_str == "PermissionsRequired"):
                tag_permissions_sh+=1
            elif(aux_str == "VDBEntry"):
                tag_vdb_sh+=1
            elif(aux_str == "ReleaseNotes"):
                tag_release_sh+=1
            elif(aux_str == "Mitigation"):
                tag_mitigation_sh+=1
            else:
                print(aux_str)
                tag_other_sh+=1 
        



        
print("**************************ESTADÍSTICAS ETIQUETAS ASOCIADAS A REFERENCIAS CVE SMART HOME********************************")
print("\n")
print(" DE UN TOTAL DE "+str(counter_tags_sh)+" REFERENCIAS, LAS ESTADÍSTICAS DE LAS ETIQUETAS ASOCIADAS A LAS REFERENCIAS SON LAS SIGUIENTES :")
print("\n")
print("       -  EN "+str(tag_thirdpartyadv_sh)+" REFERENCIAS LA ETIQUETA ES THIRD PARTY ADVISORY \n")
print("       -  EN "+str(tag_exploit_sh)+" REFERENCIAS LA ETIQUETA ES EXPLOIT \n")
print("       -  EN "+str(tag_techndescript_sh)+" REFERENCIAS LA ETIQUETA ES TECHNICAL DESCRIPTION \n")
print("       -  EN "+str(tag_issuetrack_sh)+" REFERENCIAS LA ETIQUETA ES ISSUE TRACKING \n")
print("       -  EN "+str(tag_patch_sh)+" REFERENCIAS LA ETIQUETA ES PATCH \n")
print("       -  EN "+str(tag_vendadv_sh)+" REFERENCIAS LA ETIQUETA ES VENDOR ADVISORY \n")
print("       -  EN "+str(tag_brokenlink_sh)+" REFERENCIAS LA ETIQUETA ES BROKEN LINK \n")
print("       -  EN "+str(tag_usgovern_sh)+" REFERENCIAS LA ETIQUETA ES US GOVERNMENT RESOURCE \n")
print("       -  EN "+str(tag_mailist_sh)+" REFERENCIAS LA ETIQUETA ES MAILIST \n")
print("       -  EN "+str(tag_product_sh)+" REFERENCIAS LA ETIQUETA ES PRODUCT \n")
print("       -  EN "+str(tag_permissions_sh)+" REFERENCIAS LA ETIQUETA ES PERMISSIONS REQUIRED \n")
print("       -  EN "+str(tag_vdb_sh)+" REFERENCIAS LA ETIQUETA ES VDB ENTRY \n")
print("       -  EN "+str(tag_release_sh)+" REFERENCIAS LA ETIQUETA ES RELEASE \n")
print("       -  EN "+str(tag_mitigation_sh)+" REFERENCIAS LA ETIQUETA ES MITIGATION \n")
print("       -  EN "+str(tag_other_sh)+" REFERENCIAS LA ETIQUETA ES DISTINTO A LOS ANTERIORES \n")
print("\n")

print("**************************PORCENTAJES ETIQUETAS ASOCIADAS A REFERENCIAS CVE SMART HOME********************************")
print("\n")
print("\n")
print(" DE UN TOTAL DE "+str(counter_tags_sh)+" REFERENCIAS, LOS PORCENTAJES DE LAS ETIQUETAS ASOCIADAS A LAS REFERENCIAS SON LOS SIGUIENTES :")
print("\n")
print("       -  EN EL "+str(float(((tag_thirdpartyadv_sh*100)/counter_tags_sh)))+" % DE LAS REFERENCIAS LA ETIQUETA ES THIRD PARTY ADVISORY \n")
print("       -  EN EL "+str(float(((tag_exploit_sh*100)/counter_tags_sh)))+" % DE LAS REFERENCIAS LA ETIQUETA ES EXPLOIT \n")
print("       -  EN EL "+str(float(((tag_techndescript_sh*100)/counter_tags_sh)))+" % DE LAS REFERENCIAS LA ETIQUETA ES TECHNICAL DESCRIPTION \n")
print("       -  EN EL "+str(float(((tag_issuetrack_sh*100)/counter_tags_sh)))+" % DE LAS REFERENCIAS LA ETIQUETA ES ISSUE TRACKING \n")
print("       -  EN EL "+str(float(((tag_patch_sh*100)/counter_tags_sh)))+" % DE LAS REFERENCIAS LA ETIQUETA ES PATCH \n")
print("       -  EN EL "+str(float(((tag_vendadv_sh*100)/counter_tags_sh)))+" % DE LAS REFERENCIAS LA ETIQUETA ES VENDOR ADVISORY \n")
print("       -  EN EL "+str(float(((tag_brokenlink_sh*100)/counter_tags_sh)))+" % DE LAS REFERENCIAS LA ETIQUETA ES BROKEN LINK \n")
print("       -  EN EL "+str(float(((tag_usgovern_sh*100)/counter_tags_sh)))+" % DE LAS REFERENCIAS LA ETIQUETA ES US GOVERNMENT RESOURCE \n")
print("       -  EN EL "+str(float(((tag_mailist_sh*100)/counter_tags_sh)))+" % DE LAS REFERENCIAS LA ETIQUETA ES MAILIST \n")
print("       -  EN EL "+str(float(((tag_product_sh*100)/counter_tags_sh)))+" % DE LAS REFERENCIAS LA ETIQUETA ES PRODUCT \n")
print("       -  EN EL "+str(float(((tag_permissions_sh*100)/counter_tags_sh)))+" % DE LAS REFERENCIAS LA ETIQUETA ES PERMISSIONS REQUIRED \n")
print("       -  EN EL "+str(float(((tag_vdb_sh*100)/counter_tags_sh)))+" % DE LAS REFERENCIAS LA ETIQUETA ES VDB ENTRY \n")   
print("       -  EN EL "+str(float(((tag_release_sh*100)/counter_tags_sh)))+" % DE LAS REFERENCIAS LA ETIQUETA ES RELEASE \n")
print("       -  EN EL "+str(float(((tag_mitigation_sh*100)/counter_tags_sh)))+" % DE LAS REFERENCIAS LA ETIQUETA ES MITIGATION \n")
print("       -  EN EL "+str(float(((tag_other_sh*100)/counter_tags_sh)))+" % DE LAS REFERENCIAS LA ETIQUETA ES DISTINTO A LOS ANTERIORES \n")



print("\n")
print("\n")
print("**************************ESTADÍSTICAS ETIQUETAS ASOCIADAS A REFERENCIAS CVE PARTE IOT Y SMART HOME CONJUNTAS*******************************")
print("\n")
print("\n")
print(" DE UN TOTAL DE "+str(counter_tags_sh+counter_tags_iot)+" REFERENCIAS, LAS ESTADÍSTICAS DE LAS ETIQUETAS ASOCIADAS A LAS REFERENCIAS SON LAS SIGUIENTES :")
print("\n")
print("      -  EN "+str(tag_thirdpartyadv_sh+tag_thirdpartyadv_iot)+" REFERENCIAS LA ETIQUETA ES THIRD PARTY ADVISORY \n")
print("      -  EN "+str(tag_exploit_sh+tag_exploit_iot)+" REFERENCIAS LA ETIQUETA ES EXPLOIT \n")
print("      -  EN "+str(tag_techndescript_sh+tag_techndescript_iot)+" REFERENCIAS LA ETIQUETA ES TECHNICAL DESCRIPTION \n")
print("      -  EN "+str(tag_issuetrack_sh+tag_issuetrack_iot)+" REFERENCIAS LA ETIQUETA ES ISSUE TRACKING \n")
print("      -  EN "+str(tag_patch_sh+tag_patch_iot)+" REFERENCIAS LA ETIQUETA ES PATCH \n")
print("      -  EN "+str(tag_vendadv_sh+tag_vendadv_iot)+" REFERENCIAS LA ETIQUETA ES VENDOR ADVISORY \n")
print("      -  EN "+str(tag_brokenlink_sh+tag_brokenlink_iot)+" LAS REFERENCIAS LA ETIQUETA ES BROKEN LINK \n")
print("      -  EN "+str(tag_usgovern_sh+tag_usgovern_iot)+" REFERENCIAS LA ETIQUETA ES US GOVERNMENT RESOURCE \n")
print("      -  EN "+str(tag_mailist_sh+tag_mailist_iot)+" REFERENCIAS LA ETIQUETA ES MAILIST \n")
print("      -  EN "+str(tag_product_sh+tag_product_iot)+" REFERENCIAS LA ETIQUETA ES PRODUCT \n")
print("      -  EN "+str(tag_permissions_sh+tag_permissions_iot)+" REFERENCIAS LA ETIQUETA ES PERMISSIONS REQUIRED \n")
print("      -  EN "+str(tag_vdb_sh+tag_vdb_iot)+" REFERENCIAS LA ETIQUETA ES VDB ENTRY \n")
print("      -  EN "+str(tag_release_sh+tag_release_iot)+" REFERENCIAS LA ETIQUETA ES RELEASE \n")
print("      -  EN "+str(tag_mitigation_sh+tag_mitigation_iot)+" REFERENCIAS LA ETIQUETA ES MITIGATION \n")
print("      -  EN "+str(tag_other_sh+tag_other_iot)+" REFERENCIAS LA ETIQUETA ES DISTINTO A LOS ANTERIORES \n")





print("\n")
print("\n")
print("**************************PORCENTAJES ETIQUETAS ASOCIADAS A REFERENCIAS CVE PARTE IOT Y SMART HOME CONJUNTAS*******************************")
print("\n")
print("\n")
print(" DE UN TOTAL DE "+str(counter_tags_sh+counter_tags_iot)+" REFERENCIAS, LOS PORCENTAJES DE LAS ETIQUETAS ASOCIADAS A LAS REFERENCIAS SON LOS SIGUIENTES :")
print("\n")
print("      -  EN EL "+str(float((((tag_thirdpartyadv_sh+tag_thirdpartyadv_iot)*100)/(counter_tags_sh+counter_tags_iot))))+" % DE LAS REFERENCIAS LA ETIQUETA ES THIRD PARTY ADVISORY \n")
print("      -  EN EL "+str(float((((tag_exploit_sh+tag_exploit_iot)*100)/(counter_tags_sh+counter_tags_iot))))+" % DE LAS REFERENCIAS LA ETIQUETA ES EXPLOIT \n")
print("      -  EN EL "+str(float((((tag_techndescript_sh+tag_techndescript_iot)*100)/(counter_tags_sh+counter_tags_iot))))+" % DE LAS REFERENCIAS LA ETIQUETA ES TECHNICAL DESCRIPTION \n")
print("      -  EN EL "+str(float((((tag_issuetrack_sh+tag_issuetrack_iot)*100)/(counter_tags_sh+counter_tags_iot))))+" % DE LAS REFERENCIAS LA ETIQUETA ES ISSUE TRACKING \n")
print("      -  EN EL "+str(float((((tag_patch_sh+tag_patch_iot)*100)/(counter_tags_sh+counter_tags_iot))))+" % DE LAS REFERENCIAS LA ETIQUETA ES PATCH \n")
print("      -  EN EL "+str(float((((tag_vendadv_sh+tag_vendadv_iot)*100)/(counter_tags_sh+counter_tags_iot))))+" % DE LAS REFERENCIAS LA ETIQUETA ES VENDOR ADVISORY \n")
print("      -  EN EL "+str(float((((tag_brokenlink_sh+tag_brokenlink_iot)*100)/(counter_tags_sh+counter_tags_iot))))+" % DE LAS REFERENCIAS LA ETIQUETA ES BROKEN LINK \n")
print("      -  EN EL "+str(float((((tag_usgovern_sh+tag_usgovern_iot)*100)/(counter_tags_sh+counter_tags_iot))))+" % DE LAS REFERENCIAS LA ETIQUETA ES US GOVERNMENT RESOURCE \n")
print("      -  EN EL "+str(float((((tag_mailist_sh+tag_mailist_iot)*100)/(counter_tags_sh+counter_tags_iot))))+" % DE LAS REFERENCIAS LA ETIQUETA ES MAILIST \n")
print("      -  EN EL "+str(float((((tag_product_sh+tag_product_iot)*100)/(counter_tags_sh+counter_tags_iot))))+" % DE LAS REFERENCIAS LA ETIQUETA ES PRODUCT \n")
print("      -  EN EL "+str(float((((tag_permissions_sh+tag_permissions_iot)*100)/(counter_tags_sh+counter_tags_iot))))+" % DE LAS REFERENCIAS LA ETIQUETA ES PERMISSIONS REQUIRED \n")
print("      -  EN EL "+str(float((((tag_vdb_sh+tag_vdb_iot)*100)/(counter_tags_sh+counter_tags_iot))))+" % DE LAS REFERENCIAS LA ETIQUETA ES VDB ENTRY \n")
print("      -  EN EL "+str(float((((tag_release_sh+tag_release_iot)*100)/(counter_tags_sh+counter_tags_iot))))+" % DE LAS REFERENCIAS LA ETIQUETA ES RELEASE \n")
print("      -  EN EL "+str(float((((tag_mitigation_sh+tag_mitigation_iot)*100)/(counter_tags_sh+counter_tags_iot))))+" % DE LAS REFERENCIAS LA ETIQUETA ES MITIGATION \n")
print("      -  EN EL "+str(float((((tag_other_sh+tag_other_iot)*100)/(counter_tags_sh+counter_tags_iot))))+" % DE LAS REFERENCIAS LA ETIQUETA ES DISTINTO A LOS ANTERIORES \n")

