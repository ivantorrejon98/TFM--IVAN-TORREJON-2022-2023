	
import pandas as pd
from datetime import datetime,timedelta



#Abro los ficheros con los que voy a tratar




df_vulnibm_iot = pd.read_excel('vulnerabilidades_ibm_iot_2023.xlsx')

#Variables donde almacenare el contador total de valores de CONSECUENCIAS DE ATAQUE
count_conseq_vulnibm_iot=0
#Variables para almacenar el contador de valores de puntuacion temporal dado un valor especifico de CONSECUENCIAS DE ATAQUE
count_obtaininfoconseq_tempscore_9_vulnibm_iot=0
count_obtaininfoconseq_tempscore_8_vulnibm_iot=0
count_obtaininfoconseq_tempscore_7_vulnibm_iot=0
count_obtaininfoconseq_tempscore_6_vulnibm_iot=0
count_obtaininfoconseq_tempscore_5_vulnibm_iot=0
count_obtaininfoconseq_tempscore_4_vulnibm_iot=0
count_obtaininfoconseq_tempscore_3_vulnibm_iot=0
count_obtaininfoconseq_tempscore_2_vulnibm_iot=0
count_obtaininfoconseq_tempscore_1_vulnibm_iot=0
count_obtaininfoconseq_tempscore_0_vulnibm_iot=0
count_obtaininfoconseq_tempscore_10_vulnibm_iot=0
#Variable para almacenar el contador total de valores de una determinada consecuencia
count_obtaininfoconseq_vulnibm_iot=0
#Variable para almacenar el contador de valores donde el valor de puntuacion temporal viene especificado para una consecuencia especifica
count_obtaininfoconseq_vulnibm_iot_specified=0

count_xss_conseq_tempscore_9_vulnibm_iot=0
count_xss_conseq_tempscore_8_vulnibm_iot=0
count_xss_conseq_tempscore_7_vulnibm_iot=0
count_xss_conseq_tempscore_6_vulnibm_iot=0
count_xss_conseq_tempscore_5_vulnibm_iot=0
count_xss_conseq_tempscore_4_vulnibm_iot=0
count_xss_conseq_tempscore_3_vulnibm_iot=0
count_xss_conseq_tempscore_2_vulnibm_iot=0
count_xss_conseq_tempscore_1_vulnibm_iot=0
count_xss_conseq_tempscore_0_vulnibm_iot=0
count_xss_conseq_tempscore_10_vulnibm_iot=0
count_xss_conseq_vulnibm_iot=0
count_xss_conseq_vulnibm_iot_specified=0

count_gainacc_conseq_tempscore_9_vulnibm_iot=0
count_gainacc_conseq_tempscore_8_vulnibm_iot=0
count_gainacc_conseq_tempscore_7_vulnibm_iot=0
count_gainacc_conseq_tempscore_6_vulnibm_iot=0
count_gainacc_conseq_tempscore_5_vulnibm_iot=0
count_gainacc_conseq_tempscore_4_vulnibm_iot=0
count_gainacc_conseq_tempscore_3_vulnibm_iot=0
count_gainacc_conseq_tempscore_2_vulnibm_iot=0
count_gainacc_conseq_tempscore_1_vulnibm_iot=0
count_gainacc_conseq_tempscore_0_vulnibm_iot=0
count_gainacc_conseq_tempscore_10_vulnibm_iot=0
count_gainacc_conseq_vulnibm_iot=0
count_gainacc_conseq_vulnibm_iot_specified=0

count_gainpriv_conseq_tempscore_9_vulnibm_iot=0
count_gainpriv_conseq_tempscore_8_vulnibm_iot=0
count_gainpriv_conseq_tempscore_7_vulnibm_iot=0
count_gainpriv_conseq_tempscore_6_vulnibm_iot=0
count_gainpriv_conseq_tempscore_5_vulnibm_iot=0
count_gainpriv_conseq_tempscore_4_vulnibm_iot=0
count_gainpriv_conseq_tempscore_3_vulnibm_iot=0
count_gainpriv_conseq_tempscore_2_vulnibm_iot=0
count_gainpriv_conseq_tempscore_1_vulnibm_iot=0
count_gainpriv_conseq_tempscore_0_vulnibm_iot=0
count_gainpriv_conseq_tempscore_10_vulnibm_iot=0
count_gainpriv_conseq_vulnibm_iot=0
count_gainpriv_conseq_vulnibm_iot_specified=0

count_denialofserv_conseq_tempscore_9_vulnibm_iot=0
count_denialofserv_conseq_tempscore_8_vulnibm_iot=0
count_denialofserv_conseq_tempscore_7_vulnibm_iot=0
count_denialofserv_conseq_tempscore_6_vulnibm_iot=0
count_denialofserv_conseq_tempscore_5_vulnibm_iot=0
count_denialofserv_conseq_tempscore_4_vulnibm_iot=0
count_denialofserv_conseq_tempscore_3_vulnibm_iot=0
count_denialofserv_conseq_tempscore_2_vulnibm_iot=0
count_denialofserv_conseq_tempscore_1_vulnibm_iot=0
count_denialofserv_conseq_tempscore_0_vulnibm_iot=0
count_denialofserv_conseq_tempscore_10_vulnibm_iot=0
count_denialofserv_conseq_vulnibm_iot=0
count_denialofserv_conseq_vulnibm_iot_specified=0

count_bypassec_conseq_tempscore_9_vulnibm_iot=0
count_bypassec_conseq_tempscore_8_vulnibm_iot=0
count_bypassec_conseq_tempscore_7_vulnibm_iot=0
count_bypassec_conseq_tempscore_6_vulnibm_iot=0
count_bypassec_conseq_tempscore_5_vulnibm_iot=0
count_bypassec_conseq_tempscore_4_vulnibm_iot=0
count_bypassec_conseq_tempscore_3_vulnibm_iot=0
count_bypassec_conseq_tempscore_2_vulnibm_iot=0
count_bypassec_conseq_tempscore_1_vulnibm_iot=0
count_bypassec_conseq_tempscore_0_vulnibm_iot=0
count_bypassec_conseq_tempscore_10_vulnibm_iot=0
count_bypassec_conseq_vulnibm_iot=0
count_bypassec_conseq_vulnibm_iot_specified=0

count_filemani_conseq_tempscore_9_vulnibm_iot=0
count_filemani_conseq_tempscore_8_vulnibm_iot=0
count_filemani_conseq_tempscore_7_vulnibm_iot=0
count_filemani_conseq_tempscore_6_vulnibm_iot=0
count_filemani_conseq_tempscore_5_vulnibm_iot=0
count_filemani_conseq_tempscore_4_vulnibm_iot=0
count_filemani_conseq_tempscore_3_vulnibm_iot=0
count_filemani_conseq_tempscore_2_vulnibm_iot=0
count_filemani_conseq_tempscore_1_vulnibm_iot=0
count_filemani_conseq_tempscore_0_vulnibm_iot=0
count_filemani_conseq_tempscore_10_vulnibm_iot=0
count_filemani_conseq_vulnibm_iot=0
count_filemani_conseq_vulnibm_iot_specified=0


count_other_conseq_tempscore_9_vulnibm_iot=0
count_other_conseq_tempscore_8_vulnibm_iot=0
count_other_conseq_tempscore_7_vulnibm_iot=0
count_other_conseq_tempscore_6_vulnibm_iot=0
count_other_conseq_tempscore_5_vulnibm_iot=0
count_other_conseq_tempscore_4_vulnibm_iot=0
count_other_conseq_tempscore_3_vulnibm_iot=0
count_other_conseq_tempscore_2_vulnibm_iot=0
count_other_conseq_tempscore_1_vulnibm_iot=0
count_other_conseq_tempscore_0_vulnibm_iot=0
count_other_conseq_tempscore_10_vulnibm_iot=0
count_other_conseq_vulnibm_iot=0
count_other_conseq_vulnibm_iot_specified=0

#Recorro los valores de CONSECUENCIAS y aumento los contadores segun su valor

for r in range(0,len(df_vulnibm_iot["x_xfe_consequences"])):  
    #Obtengo el valor de consecuencia
    aux_str=df_vulnibm_iot["x_xfe_consequences"][r].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
    if(aux_str!='NONE' or aux_str!='None'):
        count_conseq_vulnibm_iot+=1
        #Compruebo el valor de consequence
        if(('ObtainInformation' in aux_str) or ('Obtain Information' in aux_str)):
            count_obtaininfoconseq_vulnibm_iot+=1
            #Compruebo el valor de puntuacion temporal
            if(((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) < 10.0) and ((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) >=9.0)):
                count_obtaininfoconseq_vulnibm_iot_specified+=1
                count_obtaininfoconseq_tempscore_9_vulnibm_iot+=1
            elif(((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) < 9.0) and ((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) >=8.0)):
                count_obtaininfoconseq_vulnibm_iot_specified+=1
                count_obtaininfoconseq_tempscore_8_vulnibm_iot+=1
            elif(((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) < 8.0) and ((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) >=7.0)):
                count_obtaininfoconseq_vulnibm_iot_specified+=1
                count_obtaininfoconseq_tempscore_7_vulnibm_iot+=1
            elif(((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) < 7.0) and ((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) >=6.0)):
                count_obtaininfoconseq_vulnibm_iot_specified+=1
                count_obtaininfoconseq_tempscore_6_vulnibm_iot+=1
            elif(((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) < 6.0) and ((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) >=5.0)):
                count_obtaininfoconseq_vulnibm_iot_specified+=1
                count_obtaininfoconseq_tempscore_5_vulnibm_iot+=1
            elif(((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) < 5.0) and ((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) >=4.0)):
                count_obtaininfoconseq_vulnibm_iot_specified+=1
                count_obtaininfoconseq_tempscore_4_vulnibm_iot+=1
            elif(((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) < 4.0) and ((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) >=3.0)):
                count_obtaininfoconseq_vulnibm_iot_specified+=1
                count_obtaininfoconseq_tempscore_3_vulnibm_iot+=1
            elif(((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) < 3.0) and ((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) >=2.0)):
                count_obtaininfoconseq_vulnibm_iot_specified+=1
                count_obtaininfoconseq_tempscore_2_vulnibm_iot+=1
            elif(((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) < 2.0) and ((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) >=1.0)):
                count_obtaininfoconseq_vulnibm_iot_specified+=1
                count_obtaininfoconseq_tempscore_1_vulnibm_iot+=1
            elif(((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) < 1.0) and ((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) >=0.0)):
                count_obtaininfoconseq_vulnibm_iot_specified+=1
                count_obtaininfoconseq_tempscore_0_vulnibm_iot+=1
            elif(((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) == 10.0)):
                count_obtaininfoconseq_vulnibm_iot_specified+=1
                count_obtaininfoconseq_tempscore_10_vulnibm_iot+=1
                
        elif('Scripting' in aux_str):
            count_xss_conseq_vulnibm_iot+=1
            if(((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) < 10.0) and ((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) >=9.0)):
                count_xss_conseq_vulnibm_iot_specified+=1
                count_xss_conseq_tempscore_9_vulnibm_iot+=1
            elif(((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) < 9.0) and ((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) >=8.0)):
                count_xss_conseq_vulnibm_iot_specified+=1
                count_xss_conseq_tempscore_8_vulnibm_iot+=1
            elif(((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) < 8.0) and ((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) >=7.0)):
                count_xss_conseq_vulnibm_iot_specified+=1
                count_xss_conseq_tempscore_7_vulnibm_iot+=1
            elif(((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) < 7.0) and ((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) >=6.0)):
                count_xss_conseq_vulnibm_iot_specified+=1
                count_xss_conseq_tempscore_6_vulnibm_iot+=1
            elif(((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) < 6.0) and ((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) >=5.0)):
                count_xss_conseq_vulnibm_iot_specified+=1
                count_xss_conseq_tempscore_5_vulnibm_iot+=1
            elif(((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) < 5.0) and ((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) >=4.0)):
                count_xss_conseq_vulnibm_iot_specified+=1
                count_xss_conseq_tempscore_4_vulnibm_iot+=1
            elif(((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) < 4.0) and ((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) >=3.0)):
                count_xss_conseq_vulnibm_iot_specified+=1
                count_xss_conseq_tempscore_3_vulnibm_iot+=1
            elif(((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) < 3.0) and ((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) >=2.0)):
                count_xss_conseq_vulnibm_iot_specified+=1
                count_xss_conseq_tempscore_2_vulnibm_iot+=1
            elif(((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) < 2.0) and ((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) >=1.0)):
                count_xss_conseq_vulnibm_iot_specified+=1
                count_xss_conseq_tempscore_1_vulnibm_iot+=1
            elif(((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) < 1.0) and ((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) >=0.0)):
                count_xss_conseq_vulnibm_iot_specified+=1
                count_xss_conseq_tempscore_0_vulnibm_iot+=1
            elif(((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) == 10.0)):
                count_xss_conseq_vulnibm_iot_specified+=1
                count_xss_conseq_tempscore_10_vulnibm_iot+=1
                
        elif('Access' in aux_str):
            count_gainacc_conseq_vulnibm_iot+=1
            if(((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) < 10.0) and ((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) >=9.0)):
                count_gainacc_conseq_vulnibm_iot_specified+=1
                count_gainacc_conseq_tempscore_9_vulnibm_iot+=1
            elif(((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) < 9.0) and ((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) >=8.0)):
                count_gainacc_conseq_vulnibm_iot_specified+=1
                count_gainacc_conseq_tempscore_8_vulnibm_iot+=1
            elif(((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) < 8.0) and ((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) >=7.0)):
                count_gainacc_conseq_vulnibm_iot_specified+=1
                count_gainacc_conseq_tempscore_7_vulnibm_iot+=1
            elif(((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) < 7.0) and ((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) >=6.0)):
                count_gainacc_conseq_vulnibm_iot_specified+=1
                count_gainacc_conseq_tempscore_6_vulnibm_iot+=1
            elif(((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) < 6.0) and ((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) >=5.0)):
                count_gainacc_conseq_vulnibm_iot_specified+=1
                count_gainacc_conseq_tempscore_5_vulnibm_iot+=1
            elif(((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) < 5.0) and ((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) >=4.0)):
                count_gainacc_conseq_vulnibm_iot_specified+=1
                count_gainacc_conseq_tempscore_4_vulnibm_iot+=1
            elif(((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) < 4.0) and ((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) >=3.0)):
                count_gainacc_conseq_vulnibm_iot_specified+=1
                count_gainacc_conseq_tempscore_3_vulnibm_iot+=1
            elif(((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) < 3.0) and ((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) >=2.0)):
                count_gainacc_conseq_vulnibm_iot_specified+=1
                count_gainacc_conseq_tempscore_2_vulnibm_iot+=1
            elif(((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) < 2.0) and ((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) >=1.0)):
                count_gainacc_conseq_vulnibm_iot_specified+=1
                count_gainacc_conseq_tempscore_1_vulnibm_iot+=1
            elif(((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) < 1.0) and ((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) >=0.0)):
                count_gainacc_conseq_vulnibm_iot_specified+=1
                count_gainacc_conseq_tempscore_0_vulnibm_iot+=1
            elif(((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) == 10.0)):
                count_gainacc_conseq_vulnibm_iot_specified+=1
                count_gainacc_conseq_tempscore_10_vulnibm_iot+=1
                
        elif('Privilege' in aux_str):
            count_gainpriv_conseq_vulnibm_iot+=1
            if(((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) < 10.0) and ((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) >=9.0)):
                count_gainpriv_conseq_vulnibm_iot_specified+=1
                count_gainpriv_conseq_tempscore_9_vulnibm_iot+=1
            elif(((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) < 9.0) and ((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) >=8.0)):
                count_gainpriv_conseq_vulnibm_iot_specified+=1
                count_gainpriv_conseq_tempscore_8_vulnibm_iot+=1
            elif(((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) < 8.0) and ((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) >=7.0)):
                count_gainpriv_conseq_vulnibm_iot_specified+=1
                count_gainpriv_conseq_tempscore_7_vulnibm_iot+=1
            elif(((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) < 7.0) and ((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) >=6.0)):
                count_gainpriv_conseq_vulnibm_iot_specified+=1
                count_gainpriv_conseq_tempscore_6_vulnibm_iot+=1
            elif(((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) < 6.0) and ((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) >=5.0)):
                count_gainpriv_conseq_vulnibm_iot_specified+=1
                count_gainpriv_conseq_tempscore_5_vulnibm_iot+=1
            elif(((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) < 5.0) and ((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) >=4.0)):
                count_gainpriv_conseq_vulnibm_iot_specified+=1
                count_gainpriv_conseq_tempscore_4_vulnibm_iot+=1
            elif(((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) < 4.0) and ((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) >=3.0)):
                count_gainpriv_conseq_vulnibm_iot_specified+=1
                count_gainpriv_conseq_tempscore_3_vulnibm_iot+=1
            elif(((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) < 3.0) and ((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) >=2.0)):
                count_gainpriv_conseq_vulnibm_iot_specified+=1
                count_gainpriv_conseq_tempscore_2_vulnibm_iot+=1
            elif(((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) < 2.0) and ((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) >=1.0)):
                count_gainpriv_conseq_vulnibm_iot_specified+=1
                count_gainpriv_conseq_tempscore_1_vulnibm_iot+=1
            elif(((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) < 1.0) and ((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) >=0.0)):
                count_gainpriv_conseq_vulnibm_iot_specified+=1
                count_gainpriv_conseq_tempscore_0_vulnibm_iot+=1
            elif(((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) == 10.0)):
                count_gainpriv_conseq_vulnibm_iot_specified+=1
                count_gainpriv_conseq_tempscore_10_vulnibm_iot+=1
                
        elif('Denial' in aux_str):
            count_denialofserv_conseq_vulnibm_iot+=1
            if(((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) < 10.0) and ((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) >=9.0)):
                count_denialofserv_conseq_vulnibm_iot_specified+=1
                count_denialofserv_conseq_tempscore_9_vulnibm_iot+=1
            elif(((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) < 9.0) and ((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) >=8.0)):
                count_denialofserv_conseq_vulnibm_iot_specified+=1
                count_denialofserv_conseq_tempscore_8_vulnibm_iot+=1
            elif(((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) < 8.0) and ((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) >=7.0)):
                count_denialofserv_conseq_vulnibm_iot_specified+=1
                count_denialofserv_conseq_tempscore_7_vulnibm_iot+=1
            elif(((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) < 7.0) and ((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) >=6.0)):
                count_denialofserv_conseq_vulnibm_iot_specified+=1
                count_denialofserv_conseq_tempscore_6_vulnibm_iot+=1
            elif(((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) < 6.0) and ((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) >=5.0)):
                count_denialofserv_conseq_vulnibm_iot_specified+=1
                count_denialofserv_conseq_tempscore_5_vulnibm_iot+=1
            elif(((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) < 5.0) and ((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) >=4.0)):
                count_denialofserv_conseq_vulnibm_iot_specified+=1
                count_denialofserv_conseq_tempscore_4_vulnibm_iot+=1
            elif(((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) < 4.0) and ((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) >=3.0)):
                count_denialofserv_conseq_vulnibm_iot_specified+=1
                count_denialofserv_conseq_tempscore_3_vulnibm_iot+=1
            elif(((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) < 3.0) and ((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) >=2.0)):
                count_denialofserv_conseq_vulnibm_iot_specified+=1
                count_denialofserv_conseq_tempscore_2_vulnibm_iot+=1
            elif(((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) < 2.0) and ((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) >=1.0)):
                count_denialofserv_conseq_vulnibm_iot_specified+=1
                count_denialofserv_conseq_tempscore_1_vulnibm_iot+=1
            elif(((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) < 1.0) and ((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) >=0.0)):
                count_denialofserv_conseq_vulnibm_iot_specified+=1
                count_denialofserv_conseq_tempscore_0_vulnibm_iot+=1
            elif(((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) == 10.0)):
                count_denialofserv_conseq_vulnibm_iot_specified+=1
                count_denialofserv_conseq_tempscore_10_vulnibm_iot+=1
        
        elif('Bypass' in aux_str):
            count_bypassec_conseq_vulnibm_iot+=1
            if(((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) < 10.0) and ((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) >=9.0)):
                count_bypassec_conseq_vulnibm_iot_specified+=1
                count_bypassec_conseq_tempscore_9_vulnibm_iot+=1
            elif(((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) < 9.0) and ((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) >=8.0)):
                count_bypassec_conseq_vulnibm_iot_specified+=1
                count_bypassec_conseq_tempscore_8_vulnibm_iot+=1
            elif(((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) < 8.0) and ((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) >=7.0)):
                count_bypassec_conseq_vulnibm_iot_specified+=1
                count_bypassec_conseq_tempscore_7_vulnibm_iot+=1
            elif(((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) < 7.0) and ((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) >=6.0)):
                count_bypassec_conseq_vulnibm_iot_specified+=1
                count_bypassec_conseq_tempscore_6_vulnibm_iot+=1
            elif(((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) < 6.0) and ((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) >=5.0)):
                count_bypassec_conseq_vulnibm_iot_specified+=1
                count_bypassec_conseq_tempscore_5_vulnibm_iot+=1
            elif(((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) < 5.0) and ((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) >=4.0)):
                count_bypassec_conseq_vulnibm_iot_specified+=1
                count_bypassec_conseq_tempscore_4_vulnibm_iot+=1
            elif(((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) < 4.0) and ((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) >=3.0)):
                count_bypassec_conseq_vulnibm_iot_specified+=1
                count_bypassec_conseq_tempscore_3_vulnibm_iot+=1
            elif(((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) < 3.0) and ((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) >=2.0)):
                count_bypassec_conseq_vulnibm_iot_specified+=1
                count_bypassec_conseq_tempscore_2_vulnibm_iot+=1
            elif(((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) < 2.0) and ((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) >=1.0)):
                count_bypassec_conseq_vulnibm_iot_specified+=1
                count_bypassec_conseq_tempscore_1_vulnibm_iot+=1
            elif(((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) < 1.0) and ((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) >=0.0)):
                count_bypassec_conseq_vulnibm_iot_specified+=1
                count_bypassec_conseq_tempscore_0_vulnibm_iot+=1
            elif(((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) == 10.0)):
                count_bypassec_conseq_vulnibm_iot_specified+=1
                count_bypassec_conseq_tempscore_10_vulnibm_iot+=1
                
        elif('Manipulation' in aux_str):
            count_filemani_conseq_vulnibm_iot+=1
            if(((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) < 10.0) and ((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) >=9.0)):
                count_filemani_conseq_vulnibm_iot_specified+=1
                count_filemani_conseq_tempscore_9_vulnibm_iot+=1
            elif(((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) < 9.0) and ((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) >=8.0)):
                count_filemani_conseq_vulnibm_iot_specified+=1
                count_filemani_conseq_tempscore_8_vulnibm_iot+=1
            elif(((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) < 8.0) and ((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) >=7.0)):
                count_filemani_conseq_vulnibm_iot_specified+=1
                count_filemani_conseq_tempscore_7_vulnibm_iot+=1
            elif(((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) < 7.0) and ((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) >=6.0)):
                count_filemani_conseq_vulnibm_iot_specified+=1
                count_filemani_conseq_tempscore_6_vulnibm_iot+=1
            elif(((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) < 6.0) and ((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) >=5.0)):
                count_filemani_conseq_vulnibm_iot_specified+=1
                count_filemani_conseq_tempscore_5_vulnibm_iot+=1
            elif(((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) < 5.0) and ((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) >=4.0)):
                count_filemani_conseq_vulnibm_iot_specified+=1
                count_filemani_conseq_tempscore_4_vulnibm_iot+=1
            elif(((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) < 4.0) and ((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) >=3.0)):
                count_filemani_conseq_vulnibm_iot_specified+=1
                count_filemani_conseq_tempscore_3_vulnibm_iot+=1
            elif(((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) < 3.0) and ((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) >=2.0)):
                count_filemani_conseq_vulnibm_iot_specified+=1
                count_filemani_conseq_tempscore_2_vulnibm_iot+=1
            elif(((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) < 2.0) and ((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) >=1.0)):
                count_filemani_conseq_vulnibm_iot_specified+=1
                count_filemani_conseq_tempscore_1_vulnibm_iot+=1
            elif(((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) < 1.0) and ((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) >=0.0)):
                count_filemani_conseq_vulnibm_iot_specified+=1
                count_filemani_conseq_tempscore_0_vulnibm_iot+=1
            elif(((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) == 10.0)):
                count_filemani_conseq_vulnibm_iot_specified+=1
                count_filemani_conseq_tempscore_10_vulnibm_iot+=1
                
        elif('Other' in aux_str):
            count_other_conseq_vulnibm_iot+=1
            if(((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) < 10.0) and ((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) >=9.0)):
                count_other_conseq_vulnibm_iot_specified+=1
                count_other_conseq_tempscore_9_vulnibm_iot+=1
            elif(((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) < 9.0) and ((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) >=8.0)):
                count_other_conseq_vulnibm_iot_specified+=1
                count_other_conseq_tempscore_8_vulnibm_iot+=1
            elif(((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) < 8.0) and ((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) >=7.0)):
                count_other_conseq_vulnibm_iot_specified+=1
                count_other_conseq_tempscore_7_vulnibm_iot+=1
            elif(((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) < 7.0) and ((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) >=6.0)):
                count_other_conseq_vulnibm_iot_specified+=1
                count_other_conseq_tempscore_6_vulnibm_iot+=1
            elif(((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) < 6.0) and ((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) >=5.0)):
                count_other_conseq_vulnibm_iot_specified+=1
                count_other_conseq_tempscore_5_vulnibm_iot+=1
            elif(((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) < 5.0) and ((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) >=4.0)):
                count_other_conseq_vulnibm_iot_specified+=1
                count_other_conseq_tempscore_4_vulnibm_iot+=1
            elif(((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) < 4.0) and ((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) >=3.0)):
                count_other_conseq_vulnibm_iot_specified+=1
                count_other_conseq_tempscore_3_vulnibm_iot+=1
            elif(((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) < 3.0) and ((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) >=2.0)):
                count_other_conseq_vulnibm_iot_specified+=1
                count_other_conseq_tempscore_2_vulnibm_iot+=1
            elif(((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) < 2.0) and ((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) >=1.0)):
                count_other_conseq_vulnibm_iot_specified+=1
                count_other_conseq_tempscore_1_vulnibm_iot+=1
            elif(((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) < 1.0) and ((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) >=0.0)):
                count_other_conseq_vulnibm_iot_specified+=1
                count_other_conseq_tempscore_0_vulnibm_iot+=1
            elif(((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) == 10.0)):
                count_other_conseq_vulnibm_iot_specified+=1
                count_other_conseq_tempscore_10_vulnibm_iot+=1
                
        
                
        
                
                
                
                
                
                
                
                
                
                
                
print("***************************ESTADÍSTICAS CONSECUENCIAS DE ATAQUE/PUNTUACION TEMPORAL VULNERABILIDADES IBM PARTE IOT***************************")
print("\n")                            
print("\n")
print(" DE UN TOTAL DE "+str(count_conseq_vulnibm_iot)+" VULNERABILIDADES DONDE LA CONSECUENCIA VIENE ESPECIFICADA:\n") 
print("\n")
print("   - LAS ESTADISTICAS DE CONSECUENCIAS SON LAS SIGUIENTES:  \n")
print("      -    EN  "+str(count_obtaininfoconseq_vulnibm_iot)+" VULNERABILIDADES LA CONSECUENCIA ES LA OBTENCION DE INFORMACION. LA PUNTUACION TEMPORAL VIENE ESPECIFICADA ES  "+str(count_obtaininfoconseq_vulnibm_iot_specified)+" VULNERABILIDADES. LAS ESTADÍSTICAS DE PUNTUACION TEMPORAL SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_obtaininfoconseq_tempscore_9_vulnibm_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN  "+str(count_obtaininfoconseq_tempscore_8_vulnibm_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN  "+str(count_obtaininfoconseq_tempscore_7_vulnibm_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN  "+str(count_obtaininfoconseq_tempscore_6_vulnibm_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN  "+str(count_obtaininfoconseq_tempscore_5_vulnibm_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN  "+str(count_obtaininfoconseq_tempscore_4_vulnibm_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN  "+str(count_obtaininfoconseq_tempscore_3_vulnibm_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN  "+str(count_obtaininfoconseq_tempscore_2_vulnibm_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN  "+str(count_obtaininfoconseq_tempscore_1_vulnibm_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN  "+str(count_obtaininfoconseq_tempscore_0_vulnibm_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 0 \n")
print("            -    EN  "+str(count_obtaininfoconseq_tempscore_10_vulnibm_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES 10 \n")
print("\n")
print("      -    EN  "+str(count_xss_conseq_vulnibm_iot)+" VULNERABILIDADES LA CONSECUENCIA ES CROSS-SITE SCRIPTING. LA PUNTUACION TEMPORAL VIENE ESPECIFICADA ES  "+str(count_xss_conseq_vulnibm_iot_specified)+" VULNERABILIDADES. LAS ESTADÍSTICAS DE PUNTUACION TEMPORAL SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_xss_conseq_tempscore_9_vulnibm_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN  "+str(count_xss_conseq_tempscore_8_vulnibm_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN  "+str(count_xss_conseq_tempscore_7_vulnibm_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN  "+str(count_xss_conseq_tempscore_6_vulnibm_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN  "+str(count_xss_conseq_tempscore_5_vulnibm_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN  "+str(count_xss_conseq_tempscore_4_vulnibm_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN  "+str(count_xss_conseq_tempscore_3_vulnibm_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN  "+str(count_xss_conseq_tempscore_2_vulnibm_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN  "+str(count_xss_conseq_tempscore_1_vulnibm_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN  "+str(count_xss_conseq_tempscore_0_vulnibm_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 0 \n")
print("            -    EN  "+str(count_xss_conseq_tempscore_10_vulnibm_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES 10 \n")
print("\n")
print("      -    EN  "+str(count_gainacc_conseq_vulnibm_iot)+" VULNERABILIDADES LA CONSECUENCIA ES LA OBTENCION DE ACCESO. LA PUNTUACION TEMPORAL VIENE ESPECIFICADA ES  "+str(count_gainacc_conseq_vulnibm_iot_specified)+" VULNERABILIDADES. LAS ESTADÍSTICAS DE PUNTUACION TEMPORAL SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_gainacc_conseq_tempscore_9_vulnibm_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN  "+str(count_gainacc_conseq_tempscore_8_vulnibm_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN  "+str(count_gainacc_conseq_tempscore_7_vulnibm_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN  "+str(count_gainacc_conseq_tempscore_6_vulnibm_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN  "+str(count_gainacc_conseq_tempscore_5_vulnibm_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN  "+str(count_gainacc_conseq_tempscore_4_vulnibm_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN  "+str(count_gainacc_conseq_tempscore_3_vulnibm_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN  "+str(count_gainacc_conseq_tempscore_2_vulnibm_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN  "+str(count_gainacc_conseq_tempscore_1_vulnibm_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN  "+str(count_gainacc_conseq_tempscore_0_vulnibm_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 0 \n")
print("            -    EN  "+str(count_gainacc_conseq_tempscore_10_vulnibm_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES 10 \n")
print("\n")
print("      -    EN  "+str(count_gainpriv_conseq_vulnibm_iot)+" VULNERABILIDADES LA CONSECUENCIA ES LA OBTENCION DE PRIVILEGIOS. LA PUNTUACION TEMPORAL VIENE ESPECIFICADA ES  "+str(count_gainpriv_conseq_vulnibm_iot_specified)+" VULNERABILIDADES. LAS ESTADÍSTICAS DE PUNTUACION TEMPORAL SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_gainpriv_conseq_tempscore_9_vulnibm_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN  "+str(count_gainpriv_conseq_tempscore_8_vulnibm_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN  "+str(count_gainpriv_conseq_tempscore_7_vulnibm_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN  "+str(count_gainpriv_conseq_tempscore_6_vulnibm_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN  "+str(count_gainpriv_conseq_tempscore_5_vulnibm_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN  "+str(count_gainpriv_conseq_tempscore_4_vulnibm_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN  "+str(count_gainpriv_conseq_tempscore_3_vulnibm_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN  "+str(count_gainpriv_conseq_tempscore_2_vulnibm_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN  "+str(count_gainpriv_conseq_tempscore_1_vulnibm_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN  "+str(count_gainpriv_conseq_tempscore_0_vulnibm_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 0 \n")
print("            -    EN  "+str(count_gainpriv_conseq_tempscore_10_vulnibm_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES 10 \n")
print("\n")
print("      -    EN  "+str(count_denialofserv_conseq_vulnibm_iot)+" VULNERABILIDADES LA CONSECUENCIA ES LA DENEGACION DE SERVICIO. LA PUNTUACION TEMPORAL VIENE ESPECIFICADA ES  "+str(count_denialofserv_conseq_vulnibm_iot_specified)+" VULNERABILIDADES. LAS ESTADÍSTICAS DE PUNTUACION TEMPORAL SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_denialofserv_conseq_tempscore_9_vulnibm_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN  "+str(count_denialofserv_conseq_tempscore_8_vulnibm_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN  "+str(count_denialofserv_conseq_tempscore_7_vulnibm_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN  "+str(count_denialofserv_conseq_tempscore_6_vulnibm_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN  "+str(count_denialofserv_conseq_tempscore_5_vulnibm_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN  "+str(count_denialofserv_conseq_tempscore_4_vulnibm_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN  "+str(count_denialofserv_conseq_tempscore_3_vulnibm_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN  "+str(count_denialofserv_conseq_tempscore_2_vulnibm_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN  "+str(count_denialofserv_conseq_tempscore_1_vulnibm_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN  "+str(count_denialofserv_conseq_tempscore_0_vulnibm_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 0 \n")
print("            -    EN  "+str(count_denialofserv_conseq_tempscore_10_vulnibm_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES 10 \n")
print("\n")
print("      -    EN  "+str(count_filemani_conseq_vulnibm_iot)+" VULNERABILIDADES LA CONSECUENCIA ES LA MANIPULACION DE FICHEROS. LA PUNTUACION TEMPORAL VIENE ESPECIFICADA ES  "+str(count_filemani_conseq_vulnibm_iot_specified)+" VULNERABILIDADES. LAS ESTADÍSTICAS DE PUNTUACION TEMPORAL SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_filemani_conseq_tempscore_9_vulnibm_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN  "+str(count_filemani_conseq_tempscore_8_vulnibm_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN  "+str(count_filemani_conseq_tempscore_7_vulnibm_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN  "+str(count_filemani_conseq_tempscore_6_vulnibm_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN  "+str(count_filemani_conseq_tempscore_5_vulnibm_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN  "+str(count_filemani_conseq_tempscore_4_vulnibm_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN  "+str(count_filemani_conseq_tempscore_3_vulnibm_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN  "+str(count_filemani_conseq_tempscore_2_vulnibm_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN  "+str(count_filemani_conseq_tempscore_1_vulnibm_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN  "+str(count_filemani_conseq_tempscore_0_vulnibm_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 0 \n")
print("            -    EN  "+str(count_filemani_conseq_tempscore_10_vulnibm_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES 10 \n")
print("\n")
print("      -    EN  "+str(count_other_conseq_vulnibm_iot)+" VULNERABILIDADES LA CONSECUENCIA ES OTRA DISTINTA A LAS ANTERIORES. LA PUNTUACION TEMPORAL VIENE ESPECIFICADA ES  "+str(count_other_conseq_vulnibm_iot_specified)+" VULNERABILIDADES. LAS ESTADÍSTICAS DE PUNTUACION TEMPORAL SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_other_conseq_tempscore_9_vulnibm_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN  "+str(count_other_conseq_tempscore_8_vulnibm_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN  "+str(count_other_conseq_tempscore_7_vulnibm_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN  "+str(count_other_conseq_tempscore_6_vulnibm_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN  "+str(count_other_conseq_tempscore_5_vulnibm_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN  "+str(count_other_conseq_tempscore_4_vulnibm_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN  "+str(count_other_conseq_tempscore_3_vulnibm_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN  "+str(count_other_conseq_tempscore_2_vulnibm_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN  "+str(count_other_conseq_tempscore_1_vulnibm_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN  "+str(count_other_conseq_tempscore_0_vulnibm_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 0 \n")
print("            -    EN  "+str(count_other_conseq_tempscore_10_vulnibm_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES 10 \n")
print("\n")






print("***************************PORCENTAJES CONSECUENCIAS DE ATAQUE/PUNTUACION TEMPORAL VULNERABILIDADES IBM IOT ***************************")
print("\n")                            
print("\n")
print(" DE UN TOTAL DE "+str(count_conseq_vulnibm_iot)+" VULNERABILIDADES :\n") 
print("\n")
print("   - LOS PORCENTAJES DE CONSECUENCIAS SON LOS SIGUIENTES:  \n")
if(count_obtaininfoconseq_vulnibm_iot>0):
    print("      -    EN EL "+str(float((count_obtaininfoconseq_vulnibm_iot*100)/count_conseq_vulnibm_iot))+" % DE VULNERABILIDADES LA CONSECUENCIA ES LA OBTENCION DE INFORMACION. LA PUNTUACION TEMPORAL VIENE ESPECIFICADA EN EL "+str(float((count_obtaininfoconseq_vulnibm_iot_specified*100)/count_obtaininfoconseq_vulnibm_iot))+" % DE ELLAS. LOS PORCENTAJES DE PUNTUACION TEMPORAL SON LOS SIGUIENTES :  \n")
    print("            -    EN EL "+str(float((count_obtaininfoconseq_tempscore_9_vulnibm_iot*100)/count_obtaininfoconseq_vulnibm_iot))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 9 \n")
    print("            -    EN EL "+str(float((count_obtaininfoconseq_tempscore_8_vulnibm_iot*100)/count_obtaininfoconseq_vulnibm_iot))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 8 \n")
    print("            -    EN EL "+str(float((count_obtaininfoconseq_tempscore_7_vulnibm_iot*100)/count_obtaininfoconseq_vulnibm_iot))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 7  \n")
    print("            -    EN EL "+str(float((count_obtaininfoconseq_tempscore_6_vulnibm_iot*100)/count_obtaininfoconseq_vulnibm_iot))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 6  \n")
    print("            -    EN EL "+str(float((count_obtaininfoconseq_tempscore_5_vulnibm_iot*100)/count_obtaininfoconseq_vulnibm_iot))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 5  \n")
    print("            -    EN EL "+str(float((count_obtaininfoconseq_tempscore_4_vulnibm_iot*100)/count_obtaininfoconseq_vulnibm_iot))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 4  \n")
    print("            -    EN EL "+str(float((count_obtaininfoconseq_tempscore_3_vulnibm_iot*100)/count_obtaininfoconseq_vulnibm_iot))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 3  \n")
    print("            -    EN EL "+str(float((count_obtaininfoconseq_tempscore_2_vulnibm_iot*100)/count_obtaininfoconseq_vulnibm_iot))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 2  \n")
    print("            -    EN EL "+str(float((count_obtaininfoconseq_tempscore_1_vulnibm_iot*100)/count_obtaininfoconseq_vulnibm_iot))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 1  \n")
    print("            -    EN EL "+str(float((count_obtaininfoconseq_tempscore_0_vulnibm_iot*100)/count_obtaininfoconseq_vulnibm_iot))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 0  \n")
    print("            -    EN EL "+str(float((count_obtaininfoconseq_tempscore_10_vulnibm_iot*100)/count_obtaininfoconseq_vulnibm_iot))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 10  \n")
    print("\n")
if(count_xss_conseq_vulnibm_iot>0):
    print("      -    EN EL "+str(float((count_xss_conseq_vulnibm_iot*100)/count_conseq_vulnibm_iot))+" % DE VULNERABILIDADES LA CONSECUENCIA ES CROSS-SITE SCRIPTING. LA PUNTUACION TEMPORAL VIENE ESPECIFICADA EN EL "+str(float((count_xss_conseq_vulnibm_iot_specified*100)/count_xss_conseq_vulnibm_iot))+" % DE ELLAS. LOS PORCENTAJES DE PUNTUACION TEMPORAL SON LOS SIGUIENTES :  \n")
    print("            -    EN EL "+str(float((count_xss_conseq_tempscore_9_vulnibm_iot*100)/count_xss_conseq_vulnibm_iot))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 9 \n")
    print("            -    EN EL "+str(float((count_xss_conseq_tempscore_8_vulnibm_iot*100)/count_xss_conseq_vulnibm_iot))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 8 \n")
    print("            -    EN EL "+str(float((count_xss_conseq_tempscore_7_vulnibm_iot*100)/count_xss_conseq_vulnibm_iot))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 7  \n")
    print("            -    EN EL "+str(float((count_xss_conseq_tempscore_6_vulnibm_iot*100)/count_xss_conseq_vulnibm_iot))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 6  \n")
    print("            -    EN EL "+str(float((count_xss_conseq_tempscore_5_vulnibm_iot*100)/count_xss_conseq_vulnibm_iot))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 5  \n")
    print("            -    EN EL "+str(float((count_xss_conseq_tempscore_4_vulnibm_iot*100)/count_xss_conseq_vulnibm_iot))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 4  \n")
    print("            -    EN EL "+str(float((count_xss_conseq_tempscore_3_vulnibm_iot*100)/count_xss_conseq_vulnibm_iot))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 3  \n")
    print("            -    EN EL "+str(float((count_xss_conseq_tempscore_2_vulnibm_iot*100)/count_xss_conseq_vulnibm_iot))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 2  \n")
    print("            -    EN EL "+str(float((count_xss_conseq_tempscore_1_vulnibm_iot*100)/count_xss_conseq_vulnibm_iot))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 1  \n")
    print("            -    EN EL "+str(float((count_xss_conseq_tempscore_0_vulnibm_iot*100)/count_xss_conseq_vulnibm_iot))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 0  \n")
    print("            -    EN EL "+str(float((count_xss_conseq_tempscore_10_vulnibm_iot*100)/count_xss_conseq_vulnibm_iot))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 10  \n")
    print("\n")
if(count_gainacc_conseq_vulnibm_iot>0):
    print("      -    EN EL "+str(float((count_gainacc_conseq_vulnibm_iot*100)/count_conseq_vulnibm_iot))+" % DE VULNERABILIDADES LA CONSECUENCIA ES LA OBTENCION DE ACCESO. LA PUNTUACION TEMPORAL VIENE ESPECIFICADA EN EL "+str(float((count_gainacc_conseq_vulnibm_iot_specified*100)/count_gainacc_conseq_vulnibm_iot))+" % DE ELLAS. LOS PORCENTAJES DE PUNTUACION TEMPORAL SON LOS SIGUIENTES :  \n")
    print("            -    EN EL "+str(float((count_gainacc_conseq_tempscore_9_vulnibm_iot*100)/count_gainacc_conseq_vulnibm_iot))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 9 \n")
    print("            -    EN EL "+str(float((count_gainacc_conseq_tempscore_8_vulnibm_iot*100)/count_gainacc_conseq_vulnibm_iot))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 8 \n")
    print("            -    EN EL "+str(float((count_gainacc_conseq_tempscore_7_vulnibm_iot*100)/count_gainacc_conseq_vulnibm_iot))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 7  \n")
    print("            -    EN EL "+str(float((count_gainacc_conseq_tempscore_6_vulnibm_iot*100)/count_gainacc_conseq_vulnibm_iot))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 6  \n")
    print("            -    EN EL "+str(float((count_gainacc_conseq_tempscore_5_vulnibm_iot*100)/count_gainacc_conseq_vulnibm_iot))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 5  \n")
    print("            -    EN EL "+str(float((count_gainacc_conseq_tempscore_4_vulnibm_iot*100)/count_gainacc_conseq_vulnibm_iot))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 4  \n")
    print("            -    EN EL "+str(float((count_gainacc_conseq_tempscore_3_vulnibm_iot*100)/count_gainacc_conseq_vulnibm_iot))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 3  \n")
    print("            -    EN EL "+str(float((count_gainacc_conseq_tempscore_2_vulnibm_iot*100)/count_gainacc_conseq_vulnibm_iot))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 2  \n")
    print("            -    EN EL "+str(float((count_gainacc_conseq_tempscore_1_vulnibm_iot*100)/count_gainacc_conseq_vulnibm_iot))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 1  \n")
    print("            -    EN EL "+str(float((count_gainacc_conseq_tempscore_0_vulnibm_iot*100)/count_gainacc_conseq_vulnibm_iot))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 0  \n")
    print("            -    EN EL "+str(float((count_gainacc_conseq_tempscore_10_vulnibm_iot*100)/count_gainacc_conseq_vulnibm_iot))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 10  \n")
    print("\n")
if(count_gainpriv_conseq_vulnibm_iot>0):
    print("      -    EN EL "+str(float((count_gainpriv_conseq_vulnibm_iot*100)/count_conseq_vulnibm_iot))+" % DE VULNERABILIDADES LA CONSECUENCIA ES LA OBTENCION DE PRIVILEGIOS. LA PUNTUACION TEMPORAL VIENE ESPECIFICADA EN EL "+str(float((count_gainpriv_conseq_vulnibm_iot_specified*100)/count_gainpriv_conseq_vulnibm_iot))+" % DE ELLAS. LOS PORCENTAJES DE PUNTUACION TEMPORAL SON LOS SIGUIENTES :  \n")
    print("            -    EN EL "+str(float((count_gainpriv_conseq_tempscore_9_vulnibm_iot*100)/count_gainpriv_conseq_vulnibm_iot))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 9 \n")
    print("            -    EN EL "+str(float((count_gainpriv_conseq_tempscore_8_vulnibm_iot*100)/count_gainpriv_conseq_vulnibm_iot))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 8 \n")
    print("            -    EN EL "+str(float((count_gainpriv_conseq_tempscore_7_vulnibm_iot*100)/count_gainpriv_conseq_vulnibm_iot))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 7  \n")
    print("            -    EN EL "+str(float((count_gainpriv_conseq_tempscore_6_vulnibm_iot*100)/count_gainpriv_conseq_vulnibm_iot))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 6  \n")
    print("            -    EN EL "+str(float((count_gainpriv_conseq_tempscore_5_vulnibm_iot*100)/count_gainpriv_conseq_vulnibm_iot))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 5  \n")
    print("            -    EN EL "+str(float((count_gainpriv_conseq_tempscore_4_vulnibm_iot*100)/count_gainpriv_conseq_vulnibm_iot))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 4  \n")
    print("            -    EN EL "+str(float((count_gainpriv_conseq_tempscore_3_vulnibm_iot*100)/count_gainpriv_conseq_vulnibm_iot))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 3  \n")
    print("            -    EN EL "+str(float((count_gainpriv_conseq_tempscore_2_vulnibm_iot*100)/count_gainpriv_conseq_vulnibm_iot))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 2  \n")
    print("            -    EN EL "+str(float((count_gainpriv_conseq_tempscore_1_vulnibm_iot*100)/count_gainpriv_conseq_vulnibm_iot))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 1  \n")
    print("            -    EN EL "+str(float((count_gainpriv_conseq_tempscore_0_vulnibm_iot*100)/count_gainpriv_conseq_vulnibm_iot))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 0  \n")
    print("            -    EN EL "+str(float((count_gainpriv_conseq_tempscore_10_vulnibm_iot*100)/count_gainpriv_conseq_vulnibm_iot))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 10  \n")
    print("\n")

if(count_denialofserv_conseq_vulnibm_iot>0):
    print("      -    EN EL "+str(float((count_denialofserv_conseq_vulnibm_iot*100)/count_conseq_vulnibm_iot))+" % DE VULNERABILIDADES LA CONSECUENCIA ES UNA DENEGACION DE SERVICIO. LA PUNTUACION TEMPORAL VIENE ESPECIFICADA EN EL "+str(float((count_denialofserv_conseq_vulnibm_iot_specified*100)/count_denialofserv_conseq_vulnibm_iot))+" % DE ELLAS. LOS PORCENTAJES DE PUNTUACION TEMPORAL SON LOS SIGUIENTES :  \n")
    print("            -    EN EL "+str(float((count_denialofserv_conseq_tempscore_9_vulnibm_iot*100)/count_denialofserv_conseq_vulnibm_iot))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 9 \n")
    print("            -    EN EL "+str(float((count_denialofserv_conseq_tempscore_8_vulnibm_iot*100)/count_denialofserv_conseq_vulnibm_iot))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 8 \n")
    print("            -    EN EL "+str(float((count_denialofserv_conseq_tempscore_7_vulnibm_iot*100)/count_denialofserv_conseq_vulnibm_iot))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 7  \n")
    print("            -    EN EL "+str(float((count_denialofserv_conseq_tempscore_6_vulnibm_iot*100)/count_denialofserv_conseq_vulnibm_iot))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 6  \n")
    print("            -    EN EL "+str(float((count_denialofserv_conseq_tempscore_5_vulnibm_iot*100)/count_denialofserv_conseq_vulnibm_iot))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 5  \n")
    print("            -    EN EL "+str(float((count_denialofserv_conseq_tempscore_4_vulnibm_iot*100)/count_denialofserv_conseq_vulnibm_iot))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 4  \n")
    print("            -    EN EL "+str(float((count_denialofserv_conseq_tempscore_3_vulnibm_iot*100)/count_denialofserv_conseq_vulnibm_iot))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 3  \n")
    print("            -    EN EL "+str(float((count_denialofserv_conseq_tempscore_2_vulnibm_iot*100)/count_denialofserv_conseq_vulnibm_iot))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 2  \n")
    print("            -    EN EL "+str(float((count_denialofserv_conseq_tempscore_1_vulnibm_iot*100)/count_denialofserv_conseq_vulnibm_iot))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 1  \n")
    print("            -    EN EL "+str(float((count_denialofserv_conseq_tempscore_0_vulnibm_iot*100)/count_denialofserv_conseq_vulnibm_iot))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 0  \n")
    print("            -    EN EL "+str(float((count_denialofserv_conseq_tempscore_10_vulnibm_iot*100)/count_denialofserv_conseq_vulnibm_iot))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 10  \n")
    print("\n")
    
if(count_bypassec_conseq_vulnibm_iot>0):
    print("      -    EN EL "+str(float((count_bypassec_conseq_vulnibm_iot*100)/count_conseq_vulnibm_iot))+" % DE VULNERABILIDADES LA CONSECUENCIA ES SOBREPASAR LA SEGURIDAD. LA PUNTUACION TEMPORAL VIENE ESPECIFICADA EN EL "+str(float((count_bypassec_conseq_vulnibm_iot_specified*100)/count_bypassec_conseq_vulnibm_iot))+" % DE ELLAS. LOS PORCENTAJES DE PUNTUACION TEMPORAL SON LOS SIGUIENTES :  \n")
    print("            -    EN EL "+str(float((count_bypassec_conseq_tempscore_9_vulnibm_iot*100)/count_bypassec_conseq_vulnibm_iot))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 9 \n")
    print("            -    EN EL "+str(float((count_bypassec_conseq_tempscore_8_vulnibm_iot*100)/count_bypassec_conseq_vulnibm_iot))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 8 \n")
    print("            -    EN EL "+str(float((count_bypassec_conseq_tempscore_7_vulnibm_iot*100)/count_bypassec_conseq_vulnibm_iot))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 7  \n")
    print("            -    EN EL "+str(float((count_bypassec_conseq_tempscore_6_vulnibm_iot*100)/count_bypassec_conseq_vulnibm_iot))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 6  \n")
    print("            -    EN EL "+str(float((count_bypassec_conseq_tempscore_5_vulnibm_iot*100)/count_bypassec_conseq_vulnibm_iot))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 5  \n")
    print("            -    EN EL "+str(float((count_bypassec_conseq_tempscore_4_vulnibm_iot*100)/count_bypassec_conseq_vulnibm_iot))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 4  \n")
    print("            -    EN EL "+str(float((count_bypassec_conseq_tempscore_3_vulnibm_iot*100)/count_bypassec_conseq_vulnibm_iot))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 3  \n")
    print("            -    EN EL "+str(float((count_bypassec_conseq_tempscore_2_vulnibm_iot*100)/count_bypassec_conseq_vulnibm_iot))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 2  \n")
    print("            -    EN EL "+str(float((count_bypassec_conseq_tempscore_1_vulnibm_iot*100)/count_bypassec_conseq_vulnibm_iot))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 1  \n")
    print("            -    EN EL "+str(float((count_bypassec_conseq_tempscore_0_vulnibm_iot*100)/count_bypassec_conseq_vulnibm_iot))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 0  \n")
    print("            -    EN EL "+str(float((count_bypassec_conseq_tempscore_10_vulnibm_iot*100)/count_bypassec_conseq_vulnibm_iot))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 10  \n")
    print("\n")    

if(count_filemani_conseq_vulnibm_iot>0):
    print("      -    EN EL "+str(float((count_filemani_conseq_vulnibm_iot*100)/count_conseq_vulnibm_iot))+" % DE VULNERABILIDADES LA CONSECUENCIA ES LA MANIPULACION DE FICHEROS. LA PUNTUACION TEMPORAL VIENE ESPECIFICADA EN EL "+str(float((count_filemani_conseq_vulnibm_iot_specified*100)/count_filemani_conseq_vulnibm_iot))+" % DE ELLAS. LOS PORCENTAJES DE PUNTUACION TEMPORAL SON LOS SIGUIENTES :  \n")
    print("            -    EN EL "+str(float((count_filemani_conseq_tempscore_9_vulnibm_iot*100)/count_filemani_conseq_vulnibm_iot))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 9 \n")
    print("            -    EN EL "+str(float((count_filemani_conseq_tempscore_8_vulnibm_iot*100)/count_filemani_conseq_vulnibm_iot))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 8 \n")
    print("            -    EN EL "+str(float((count_filemani_conseq_tempscore_7_vulnibm_iot*100)/count_filemani_conseq_vulnibm_iot))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 7  \n")
    print("            -    EN EL "+str(float((count_filemani_conseq_tempscore_6_vulnibm_iot*100)/count_filemani_conseq_vulnibm_iot))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 6  \n")
    print("            -    EN EL "+str(float((count_filemani_conseq_tempscore_5_vulnibm_iot*100)/count_filemani_conseq_vulnibm_iot))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 5  \n")
    print("            -    EN EL "+str(float((count_filemani_conseq_tempscore_4_vulnibm_iot*100)/count_filemani_conseq_vulnibm_iot))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 4  \n")
    print("            -    EN EL "+str(float((count_filemani_conseq_tempscore_3_vulnibm_iot*100)/count_filemani_conseq_vulnibm_iot))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 3  \n")
    print("            -    EN EL "+str(float((count_filemani_conseq_tempscore_2_vulnibm_iot*100)/count_filemani_conseq_vulnibm_iot))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 2  \n")
    print("            -    EN EL "+str(float((count_filemani_conseq_tempscore_1_vulnibm_iot*100)/count_filemani_conseq_vulnibm_iot))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 1  \n")
    print("            -    EN EL "+str(float((count_filemani_conseq_tempscore_0_vulnibm_iot*100)/count_filemani_conseq_vulnibm_iot))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 0  \n")
    print("            -    EN EL "+str(float((count_filemani_conseq_tempscore_10_vulnibm_iot*100)/count_filemani_conseq_vulnibm_iot))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 10  \n")
    print("\n")
    
if(count_other_conseq_vulnibm_iot>0):
    print("      -    EN EL "+str(float((count_other_conseq_vulnibm_iot*100)/count_conseq_vulnibm_iot))+" % DE VULNERABILIDADES LA CONSECUENCIA ES OTRA DISTINTA A LAS ANTERIORES. LA PUNTUACION TEMPORAL VIENE ESPECIFICADA EN EL "+str(float((count_other_conseq_vulnibm_iot_specified*100)/count_other_conseq_vulnibm_iot))+" % DE ELLAS. LOS PORCENTAJES DE PUNTUACION TEMPORAL SON LOS SIGUIENTES :  \n")
    print("            -    EN EL "+str(float((count_other_conseq_tempscore_9_vulnibm_iot*100)/count_other_conseq_vulnibm_iot))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 9 \n")
    print("            -    EN EL "+str(float((count_other_conseq_tempscore_8_vulnibm_iot*100)/count_other_conseq_vulnibm_iot))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 8 \n")
    print("            -    EN EL "+str(float((count_other_conseq_tempscore_7_vulnibm_iot*100)/count_other_conseq_vulnibm_iot))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 7  \n")
    print("            -    EN EL "+str(float((count_other_conseq_tempscore_6_vulnibm_iot*100)/count_other_conseq_vulnibm_iot))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 6  \n")
    print("            -    EN EL "+str(float((count_other_conseq_tempscore_5_vulnibm_iot*100)/count_other_conseq_vulnibm_iot))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 5  \n")
    print("            -    EN EL "+str(float((count_other_conseq_tempscore_4_vulnibm_iot*100)/count_other_conseq_vulnibm_iot))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 4  \n")
    print("            -    EN EL "+str(float((count_other_conseq_tempscore_3_vulnibm_iot*100)/count_other_conseq_vulnibm_iot))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 3  \n")
    print("            -    EN EL "+str(float((count_other_conseq_tempscore_2_vulnibm_iot*100)/count_other_conseq_vulnibm_iot))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 2  \n")
    print("            -    EN EL "+str(float((count_other_conseq_tempscore_1_vulnibm_iot*100)/count_other_conseq_vulnibm_iot))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 1  \n")
    print("            -    EN EL "+str(float((count_other_conseq_tempscore_0_vulnibm_iot*100)/count_other_conseq_vulnibm_iot))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 0  \n")
    print("            -    EN EL "+str(float((count_other_conseq_tempscore_10_vulnibm_iot*100)/count_other_conseq_vulnibm_iot))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 10  \n")
    print("\n")
          
          
          
          
          
          
          
          
          
          
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
df_vulnibm_sh = pd.read_excel('vulnerabilidades_ibm_smart_home_2023.xlsx')        

#Variables donde almacenare el contador total de valores de CONSECUENCIAS DE ATAQUE
count_conseq_vulnibm_sh=0
#Variables para almacenar el contador de valores de puntuacion temporal dado un valor especifico de CONSECUENCIAS DE ATAQUE
count_obtaininfoconseq_tempscore_9_vulnibm_sh=0
count_obtaininfoconseq_tempscore_8_vulnibm_sh=0
count_obtaininfoconseq_tempscore_7_vulnibm_sh=0
count_obtaininfoconseq_tempscore_6_vulnibm_sh=0
count_obtaininfoconseq_tempscore_5_vulnibm_sh=0
count_obtaininfoconseq_tempscore_4_vulnibm_sh=0
count_obtaininfoconseq_tempscore_3_vulnibm_sh=0
count_obtaininfoconseq_tempscore_2_vulnibm_sh=0
count_obtaininfoconseq_tempscore_1_vulnibm_sh=0
count_obtaininfoconseq_tempscore_0_vulnibm_sh=0
count_obtaininfoconseq_tempscore_10_vulnibm_sh=0
#Variable para almacenar el contador total de valores de una determinada consecuencia
count_obtaininfoconseq_vulnibm_sh=0
#Variable para almacenar el contador de valores donde el valor de puntuacion temporal viene especificado para una consecuencia especifica
count_obtaininfoconseq_vulnibm_sh_specified=0

count_xss_conseq_tempscore_9_vulnibm_sh=0
count_xss_conseq_tempscore_8_vulnibm_sh=0
count_xss_conseq_tempscore_7_vulnibm_sh=0
count_xss_conseq_tempscore_6_vulnibm_sh=0
count_xss_conseq_tempscore_5_vulnibm_sh=0
count_xss_conseq_tempscore_4_vulnibm_sh=0
count_xss_conseq_tempscore_3_vulnibm_sh=0
count_xss_conseq_tempscore_2_vulnibm_sh=0
count_xss_conseq_tempscore_1_vulnibm_sh=0
count_xss_conseq_tempscore_0_vulnibm_sh=0
count_xss_conseq_tempscore_10_vulnibm_sh=0
count_xss_conseq_vulnibm_sh=0
count_xss_conseq_vulnibm_sh_specified=0

count_gainacc_conseq_tempscore_9_vulnibm_sh=0
count_gainacc_conseq_tempscore_8_vulnibm_sh=0
count_gainacc_conseq_tempscore_7_vulnibm_sh=0
count_gainacc_conseq_tempscore_6_vulnibm_sh=0
count_gainacc_conseq_tempscore_5_vulnibm_sh=0
count_gainacc_conseq_tempscore_4_vulnibm_sh=0
count_gainacc_conseq_tempscore_3_vulnibm_sh=0
count_gainacc_conseq_tempscore_2_vulnibm_sh=0
count_gainacc_conseq_tempscore_1_vulnibm_sh=0
count_gainacc_conseq_tempscore_0_vulnibm_sh=0
count_gainacc_conseq_tempscore_10_vulnibm_sh=0
count_gainacc_conseq_vulnibm_sh=0
count_gainacc_conseq_vulnibm_sh_specified=0

count_gainpriv_conseq_tempscore_9_vulnibm_sh=0
count_gainpriv_conseq_tempscore_8_vulnibm_sh=0
count_gainpriv_conseq_tempscore_7_vulnibm_sh=0
count_gainpriv_conseq_tempscore_6_vulnibm_sh=0
count_gainpriv_conseq_tempscore_5_vulnibm_sh=0
count_gainpriv_conseq_tempscore_4_vulnibm_sh=0
count_gainpriv_conseq_tempscore_3_vulnibm_sh=0
count_gainpriv_conseq_tempscore_2_vulnibm_sh=0
count_gainpriv_conseq_tempscore_1_vulnibm_sh=0
count_gainpriv_conseq_tempscore_0_vulnibm_sh=0
count_gainpriv_conseq_tempscore_10_vulnibm_sh=0
count_gainpriv_conseq_vulnibm_sh=0
count_gainpriv_conseq_vulnibm_sh_specified=0

count_denialofserv_conseq_tempscore_9_vulnibm_sh=0
count_denialofserv_conseq_tempscore_8_vulnibm_sh=0
count_denialofserv_conseq_tempscore_7_vulnibm_sh=0
count_denialofserv_conseq_tempscore_6_vulnibm_sh=0
count_denialofserv_conseq_tempscore_5_vulnibm_sh=0
count_denialofserv_conseq_tempscore_4_vulnibm_sh=0
count_denialofserv_conseq_tempscore_3_vulnibm_sh=0
count_denialofserv_conseq_tempscore_2_vulnibm_sh=0
count_denialofserv_conseq_tempscore_1_vulnibm_sh=0
count_denialofserv_conseq_tempscore_0_vulnibm_sh=0
count_denialofserv_conseq_tempscore_10_vulnibm_sh=0
count_denialofserv_conseq_vulnibm_sh=0
count_denialofserv_conseq_vulnibm_sh_specified=0

count_bypassec_conseq_tempscore_9_vulnibm_sh=0
count_bypassec_conseq_tempscore_8_vulnibm_sh=0
count_bypassec_conseq_tempscore_7_vulnibm_sh=0
count_bypassec_conseq_tempscore_6_vulnibm_sh=0
count_bypassec_conseq_tempscore_5_vulnibm_sh=0
count_bypassec_conseq_tempscore_4_vulnibm_sh=0
count_bypassec_conseq_tempscore_3_vulnibm_sh=0
count_bypassec_conseq_tempscore_2_vulnibm_sh=0
count_bypassec_conseq_tempscore_1_vulnibm_sh=0
count_bypassec_conseq_tempscore_0_vulnibm_sh=0
count_bypassec_conseq_tempscore_10_vulnibm_sh=0
count_bypassec_conseq_vulnibm_sh=0
count_bypassec_conseq_vulnibm_sh_specified=0

count_filemani_conseq_tempscore_9_vulnibm_sh=0
count_filemani_conseq_tempscore_8_vulnibm_sh=0
count_filemani_conseq_tempscore_7_vulnibm_sh=0
count_filemani_conseq_tempscore_6_vulnibm_sh=0
count_filemani_conseq_tempscore_5_vulnibm_sh=0
count_filemani_conseq_tempscore_4_vulnibm_sh=0
count_filemani_conseq_tempscore_3_vulnibm_sh=0
count_filemani_conseq_tempscore_2_vulnibm_sh=0
count_filemani_conseq_tempscore_1_vulnibm_sh=0
count_filemani_conseq_tempscore_0_vulnibm_sh=0
count_filemani_conseq_tempscore_10_vulnibm_sh=0
count_filemani_conseq_vulnibm_sh=0
count_filemani_conseq_vulnibm_sh_specified=0


count_other_conseq_tempscore_9_vulnibm_sh=0
count_other_conseq_tempscore_8_vulnibm_sh=0
count_other_conseq_tempscore_7_vulnibm_sh=0
count_other_conseq_tempscore_6_vulnibm_sh=0
count_other_conseq_tempscore_5_vulnibm_sh=0
count_other_conseq_tempscore_4_vulnibm_sh=0
count_other_conseq_tempscore_3_vulnibm_sh=0
count_other_conseq_tempscore_2_vulnibm_sh=0
count_other_conseq_tempscore_1_vulnibm_sh=0
count_other_conseq_tempscore_0_vulnibm_sh=0
count_other_conseq_tempscore_10_vulnibm_sh=0
count_other_conseq_vulnibm_sh=0
count_other_conseq_vulnibm_sh_specified=0

#Recorro los valores de CONSECUENCIAS y aumento los contadores segun su valor

for r in range(0,len(df_vulnibm_sh["x_xfe_consequences"])):  
    #Obtengo el valor de consecuencia
    aux_str=df_vulnibm_sh["x_xfe_consequences"][r].replace('[', '').replace(']', '').replace(" ",'').replace("'","").replace("'","")
    if(aux_str!='NONE' or aux_str!='None'):
        count_conseq_vulnibm_sh+=1
        #Compruebo el valor de consequence
        if(('ObtainInformation' in aux_str) or ('Obtain Information' in aux_str)):
            count_obtaininfoconseq_vulnibm_sh+=1
            #Compruebo el valor de puntuacion temporal
            if(((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) < 10.0) and ((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) >=9.0)):
                count_obtaininfoconseq_vulnibm_sh_specified+=1
                count_obtaininfoconseq_tempscore_9_vulnibm_sh+=1
            elif(((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) < 9.0) and ((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) >=8.0)):
                count_obtaininfoconseq_vulnibm_sh_specified+=1
                count_obtaininfoconseq_tempscore_8_vulnibm_sh+=1
            elif(((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) < 8.0) and ((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) >=7.0)):
                count_obtaininfoconseq_vulnibm_sh_specified+=1
                count_obtaininfoconseq_tempscore_7_vulnibm_sh+=1
            elif(((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) < 7.0) and ((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) >=6.0)):
                count_obtaininfoconseq_vulnibm_sh_specified+=1
                count_obtaininfoconseq_tempscore_6_vulnibm_sh+=1
            elif(((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) < 6.0) and ((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) >=5.0)):
                count_obtaininfoconseq_vulnibm_sh_specified+=1
                count_obtaininfoconseq_tempscore_5_vulnibm_sh+=1
            elif(((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) < 5.0) and ((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) >=4.0)):
                count_obtaininfoconseq_vulnibm_sh_specified+=1
                count_obtaininfoconseq_tempscore_4_vulnibm_sh+=1
            elif(((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) < 4.0) and ((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) >=3.0)):
                count_obtaininfoconseq_vulnibm_sh_specified+=1
                count_obtaininfoconseq_tempscore_3_vulnibm_sh+=1
            elif(((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) < 3.0) and ((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) >=2.0)):
                count_obtaininfoconseq_vulnibm_sh_specified+=1
                count_obtaininfoconseq_tempscore_2_vulnibm_sh+=1
            elif(((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) < 2.0) and ((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) >=1.0)):
                count_obtaininfoconseq_vulnibm_sh_specified+=1
                count_obtaininfoconseq_tempscore_1_vulnibm_sh+=1
            elif(((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) < 1.0) and ((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) >=0.0)):
                count_obtaininfoconseq_vulnibm_sh_specified+=1
                count_obtaininfoconseq_tempscore_0_vulnibm_sh+=1
            elif(((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) == 10.0)):
                count_obtaininfoconseq_vulnibm_sh_specified+=1
                count_obtaininfoconseq_tempscore_10_vulnibm_sh+=1
                
        elif('Scripting' in aux_str):
            count_xss_conseq_vulnibm_sh+=1
            if(((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) < 10.0) and ((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) >=9.0)):
                count_xss_conseq_vulnibm_sh_specified+=1
                count_xss_conseq_tempscore_9_vulnibm_sh+=1
            elif(((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) < 9.0) and ((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) >=8.0)):
                count_xss_conseq_vulnibm_sh_specified+=1
                count_xss_conseq_tempscore_8_vulnibm_sh+=1
            elif(((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) < 8.0) and ((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) >=7.0)):
                count_xss_conseq_vulnibm_sh_specified+=1
                count_xss_conseq_tempscore_7_vulnibm_sh+=1
            elif(((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) < 7.0) and ((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) >=6.0)):
                count_xss_conseq_vulnibm_sh_specified+=1
                count_xss_conseq_tempscore_6_vulnibm_sh+=1
            elif(((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) < 6.0) and ((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) >=5.0)):
                count_xss_conseq_vulnibm_sh_specified+=1
                count_xss_conseq_tempscore_5_vulnibm_sh+=1
            elif(((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) < 5.0) and ((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) >=4.0)):
                count_xss_conseq_vulnibm_sh_specified+=1
                count_xss_conseq_tempscore_4_vulnibm_sh+=1
            elif(((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) < 4.0) and ((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) >=3.0)):
                count_xss_conseq_vulnibm_sh_specified+=1
                count_xss_conseq_tempscore_3_vulnibm_sh+=1
            elif(((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) < 3.0) and ((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) >=2.0)):
                count_xss_conseq_vulnibm_sh_specified+=1
                count_xss_conseq_tempscore_2_vulnibm_sh+=1
            elif(((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) < 2.0) and ((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) >=1.0)):
                count_xss_conseq_vulnibm_sh_specified+=1
                count_xss_conseq_tempscore_1_vulnibm_sh+=1
            elif(((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) < 1.0) and ((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) >=0.0)):
                count_xss_conseq_vulnibm_sh_specified+=1
                count_xss_conseq_tempscore_0_vulnibm_sh+=1
            elif(((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) == 10.0)):
                count_xss_conseq_vulnibm_sh_specified+=1
                count_xss_conseq_tempscore_10_vulnibm_sh+=1
                
        elif('Access' in aux_str):
            count_gainacc_conseq_vulnibm_sh+=1
            if(isinstance(df_vulnibm_sh["x_xfe_temporal_score"][r],float)):
                if(((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) < 10.0) and ((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) >=9.0)):
                    count_gainacc_conseq_vulnibm_sh_specified+=1
                    count_gainacc_conseq_tempscore_9_vulnibm_sh+=1
                elif(((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) < 9.0) and ((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) >=8.0)):
                    count_gainacc_conseq_vulnibm_sh_specified+=1
                    count_gainacc_conseq_tempscore_8_vulnibm_sh+=1
                elif(((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) < 8.0) and ((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) >=7.0)):
                    count_gainacc_conseq_vulnibm_sh_specified+=1
                    count_gainacc_conseq_tempscore_7_vulnibm_sh+=1
                elif(((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) < 7.0) and ((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) >=6.0)):
                    count_gainacc_conseq_vulnibm_sh_specified+=1
                    count_gainacc_conseq_tempscore_6_vulnibm_sh+=1
                elif(((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) < 6.0) and ((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) >=5.0)):
                    count_gainacc_conseq_vulnibm_sh_specified+=1
                    count_gainacc_conseq_tempscore_5_vulnibm_sh+=1
                elif(((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) < 5.0) and ((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) >=4.0)):
                    count_gainacc_conseq_vulnibm_sh_specified+=1
                    count_gainacc_conseq_tempscore_4_vulnibm_sh+=1
                elif(((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) < 4.0) and ((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) >=3.0)):
                    count_gainacc_conseq_vulnibm_sh_specified+=1
                    count_gainacc_conseq_tempscore_3_vulnibm_sh+=1
                elif(((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) < 3.0) and ((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) >=2.0)):
                    count_gainacc_conseq_vulnibm_sh_specified+=1
                    count_gainacc_conseq_tempscore_2_vulnibm_sh+=1
                elif(((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) < 2.0) and ((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) >=1.0)):
                    count_gainacc_conseq_vulnibm_sh_specified+=1
                    count_gainacc_conseq_tempscore_1_vulnibm_sh+=1
                elif(((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) < 1.0) and ((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) >=0.0)):
                    count_gainacc_conseq_vulnibm_sh_specified+=1
                    count_gainacc_conseq_tempscore_0_vulnibm_sh+=1
                elif(((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) == 10.0)):
                    count_gainacc_conseq_vulnibm_sh_specified+=1
                    count_gainacc_conseq_tempscore_10_vulnibm_sh+=1
                
        elif('Privilege' in aux_str):
            count_gainpriv_conseq_vulnibm_sh+=1
            if(((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) < 10.0) and ((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) >=9.0)):
                count_gainpriv_conseq_vulnibm_sh_specified+=1
                count_gainpriv_conseq_tempscore_9_vulnibm_sh+=1
            elif(((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) < 9.0) and ((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) >=8.0)):
                count_gainpriv_conseq_vulnibm_sh_specified+=1
                count_gainpriv_conseq_tempscore_8_vulnibm_sh+=1
            elif(((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) < 8.0) and ((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) >=7.0)):
                count_gainpriv_conseq_vulnibm_sh_specified+=1
                count_gainpriv_conseq_tempscore_7_vulnibm_sh+=1
            elif(((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) < 7.0) and ((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) >=6.0)):
                count_gainpriv_conseq_vulnibm_sh_specified+=1
                count_gainpriv_conseq_tempscore_6_vulnibm_sh+=1
            elif(((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) < 6.0) and ((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) >=5.0)):
                count_gainpriv_conseq_vulnibm_sh_specified+=1
                count_gainpriv_conseq_tempscore_5_vulnibm_sh+=1
            elif(((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) < 5.0) and ((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) >=4.0)):
                count_gainpriv_conseq_vulnibm_sh_specified+=1
                count_gainpriv_conseq_tempscore_4_vulnibm_sh+=1
            elif(((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) < 4.0) and ((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) >=3.0)):
                count_gainpriv_conseq_vulnibm_sh_specified+=1
                count_gainpriv_conseq_tempscore_3_vulnibm_sh+=1
            elif(((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) < 3.0) and ((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) >=2.0)):
                count_gainpriv_conseq_vulnibm_sh_specified+=1
                count_gainpriv_conseq_tempscore_2_vulnibm_sh+=1
            elif(((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) < 2.0) and ((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) >=1.0)):
                count_gainpriv_conseq_vulnibm_sh_specified+=1
                count_gainpriv_conseq_tempscore_1_vulnibm_sh+=1
            elif(((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) < 1.0) and ((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) >=0.0)):
                count_gainpriv_conseq_vulnibm_sh_specified+=1
                count_gainpriv_conseq_tempscore_0_vulnibm_sh+=1
            elif(((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) == 10.0)):
                count_gainpriv_conseq_vulnibm_sh_specified+=1
                count_gainpriv_conseq_tempscore_10_vulnibm_sh+=1
                
        elif('Denial' in aux_str):
            count_denialofserv_conseq_vulnibm_sh+=1
            if(((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) < 10.0) and ((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) >=9.0)):
                count_denialofserv_conseq_vulnibm_sh_specified+=1
                count_denialofserv_conseq_tempscore_9_vulnibm_sh+=1
            elif(((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) < 9.0) and ((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) >=8.0)):
                count_denialofserv_conseq_vulnibm_sh_specified+=1
                count_denialofserv_conseq_tempscore_8_vulnibm_sh+=1
            elif(((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) < 8.0) and ((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) >=7.0)):
                count_denialofserv_conseq_vulnibm_sh_specified+=1
                count_denialofserv_conseq_tempscore_7_vulnibm_sh+=1
            elif(((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) < 7.0) and ((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) >=6.0)):
                count_denialofserv_conseq_vulnibm_sh_specified+=1
                count_denialofserv_conseq_tempscore_6_vulnibm_sh+=1
            elif(((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) < 6.0) and ((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) >=5.0)):
                count_denialofserv_conseq_vulnibm_sh_specified+=1
                count_denialofserv_conseq_tempscore_5_vulnibm_sh+=1
            elif(((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) < 5.0) and ((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) >=4.0)):
                count_denialofserv_conseq_vulnibm_sh_specified+=1
                count_denialofserv_conseq_tempscore_4_vulnibm_sh+=1
            elif(((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) < 4.0) and ((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) >=3.0)):
                count_denialofserv_conseq_vulnibm_sh_specified+=1
                count_denialofserv_conseq_tempscore_3_vulnibm_sh+=1
            elif(((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) < 3.0) and ((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) >=2.0)):
                count_denialofserv_conseq_vulnibm_sh_specified+=1
                count_denialofserv_conseq_tempscore_2_vulnibm_sh+=1
            elif(((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) < 2.0) and ((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) >=1.0)):
                count_denialofserv_conseq_vulnibm_sh_specified+=1
                count_denialofserv_conseq_tempscore_1_vulnibm_sh+=1
            elif(((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) < 1.0) and ((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) >=0.0)):
                count_denialofserv_conseq_vulnibm_sh_specified+=1
                count_denialofserv_conseq_tempscore_0_vulnibm_sh+=1
            elif(((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) == 10.0)):
                count_denialofserv_conseq_vulnibm_sh_specified+=1
                count_denialofserv_conseq_tempscore_10_vulnibm_sh+=1
        
        elif('Bypass' in aux_str):
            count_bypassec_conseq_vulnibm_sh+=1
            if(((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) < 10.0) and ((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) >=9.0)):
                count_bypassec_conseq_vulnibm_sh_specified+=1
                count_bypassec_conseq_tempscore_9_vulnibm_sh+=1
            elif(((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) < 9.0) and ((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) >=8.0)):
                count_bypassec_conseq_vulnibm_sh_specified+=1
                count_bypassec_conseq_tempscore_8_vulnibm_sh+=1
            elif(((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) < 8.0) and ((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) >=7.0)):
                count_bypassec_conseq_vulnibm_sh_specified+=1
                count_bypassec_conseq_tempscore_7_vulnibm_sh+=1
            elif(((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) < 7.0) and ((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) >=6.0)):
                count_bypassec_conseq_vulnibm_sh_specified+=1
                count_bypassec_conseq_tempscore_6_vulnibm_sh+=1
            elif(((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) < 6.0) and ((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) >=5.0)):
                count_bypassec_conseq_vulnibm_sh_specified+=1
                count_bypassec_conseq_tempscore_5_vulnibm_sh+=1
            elif(((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) < 5.0) and ((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) >=4.0)):
                count_bypassec_conseq_vulnibm_sh_specified+=1
                count_bypassec_conseq_tempscore_4_vulnibm_sh+=1
            elif(((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) < 4.0) and ((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) >=3.0)):
                count_bypassec_conseq_vulnibm_sh_specified+=1
                count_bypassec_conseq_tempscore_3_vulnibm_sh+=1
            elif(((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) < 3.0) and ((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) >=2.0)):
                count_bypassec_conseq_vulnibm_sh_specified+=1
                count_bypassec_conseq_tempscore_2_vulnibm_sh+=1
            elif(((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) < 2.0) and ((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) >=1.0)):
                count_bypassec_conseq_vulnibm_sh_specified+=1
                count_bypassec_conseq_tempscore_1_vulnibm_sh+=1
            elif(((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) < 1.0) and ((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) >=0.0)):
                count_bypassec_conseq_vulnibm_sh_specified+=1
                count_bypassec_conseq_tempscore_0_vulnibm_sh+=1
            elif(((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) == 10.0)):
                count_bypassec_conseq_vulnibm_sh_specified+=1
                count_bypassec_conseq_tempscore_10_vulnibm_sh+=1
                
        elif('Manipulation' in aux_str):
            count_filemani_conseq_vulnibm_sh+=1
            if(((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) < 10.0) and ((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) >=9.0)):
                count_filemani_conseq_vulnibm_sh_specified+=1
                count_filemani_conseq_tempscore_9_vulnibm_sh+=1
            elif(((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) < 9.0) and ((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) >=8.0)):
                count_filemani_conseq_vulnibm_sh_specified+=1
                count_filemani_conseq_tempscore_8_vulnibm_sh+=1
            elif(((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) < 8.0) and ((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) >=7.0)):
                count_filemani_conseq_vulnibm_sh_specified+=1
                count_filemani_conseq_tempscore_7_vulnibm_sh+=1
            elif(((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) < 7.0) and ((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) >=6.0)):
                count_filemani_conseq_vulnibm_sh_specified+=1
                count_filemani_conseq_tempscore_6_vulnibm_sh+=1
            elif(((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) < 6.0) and ((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) >=5.0)):
                count_filemani_conseq_vulnibm_sh_specified+=1
                count_filemani_conseq_tempscore_5_vulnibm_sh+=1
            elif(((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) < 5.0) and ((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) >=4.0)):
                count_filemani_conseq_vulnibm_sh_specified+=1
                count_filemani_conseq_tempscore_4_vulnibm_sh+=1
            elif(((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) < 4.0) and ((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) >=3.0)):
                count_filemani_conseq_vulnibm_sh_specified+=1
                count_filemani_conseq_tempscore_3_vulnibm_sh+=1
            elif(((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) < 3.0) and ((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) >=2.0)):
                count_filemani_conseq_vulnibm_sh_specified+=1
                count_filemani_conseq_tempscore_2_vulnibm_sh+=1
            elif(((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) < 2.0) and ((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) >=1.0)):
                count_filemani_conseq_vulnibm_sh_specified+=1
                count_filemani_conseq_tempscore_1_vulnibm_sh+=1
            elif(((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) < 1.0) and ((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) >=0.0)):
                count_filemani_conseq_vulnibm_sh_specified+=1
                count_filemani_conseq_tempscore_0_vulnibm_sh+=1
            elif(((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) == 10.0)):
                count_filemani_conseq_vulnibm_sh_specified+=1
                count_filemani_conseq_tempscore_10_vulnibm_sh+=1
                
        elif('Other' in aux_str):
            count_other_conseq_vulnibm_sh+=1
            if(((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) < 10.0) and ((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) >=9.0)):
                count_other_conseq_vulnibm_sh_specified+=1
                count_other_conseq_tempscore_9_vulnibm_sh+=1
            elif(((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) < 9.0) and ((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) >=8.0)):
                count_other_conseq_vulnibm_sh_specified+=1
                count_other_conseq_tempscore_8_vulnibm_sh+=1
            elif(((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) < 8.0) and ((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) >=7.0)):
                count_other_conseq_vulnibm_sh_specified+=1
                count_other_conseq_tempscore_7_vulnibm_sh+=1
            elif(((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) < 7.0) and ((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) >=6.0)):
                count_other_conseq_vulnibm_sh_specified+=1
                count_other_conseq_tempscore_6_vulnibm_sh+=1
            elif(((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) < 6.0) and ((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) >=5.0)):
                count_other_conseq_vulnibm_sh_specified+=1
                count_other_conseq_tempscore_5_vulnibm_sh+=1
            elif(((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) < 5.0) and ((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) >=4.0)):
                count_other_conseq_vulnibm_sh_specified+=1
                count_other_conseq_tempscore_4_vulnibm_sh+=1
            elif(((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) < 4.0) and ((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) >=3.0)):
                count_other_conseq_vulnibm_sh_specified+=1
                count_other_conseq_tempscore_3_vulnibm_sh+=1
            elif(((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) < 3.0) and ((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) >=2.0)):
                count_other_conseq_vulnibm_sh_specified+=1
                count_other_conseq_tempscore_2_vulnibm_sh+=1
            elif(((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) < 2.0) and ((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) >=1.0)):
                count_other_conseq_vulnibm_sh_specified+=1
                count_other_conseq_tempscore_1_vulnibm_sh+=1
            elif(((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) < 1.0) and ((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) >=0.0)):
                count_other_conseq_vulnibm_sh_specified+=1
                count_other_conseq_tempscore_0_vulnibm_sh+=1
            elif(((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) == 10.0)):
                count_other_conseq_vulnibm_sh_specified+=1
                count_other_conseq_tempscore_10_vulnibm_sh+=1
                
        
                
        
                
                
                
                
                
                
                
                
                
                
                
print("***************************ESTADÍSTICAS CONSECUENCIAS DE ATAQUE/PUNTUACION TEMPORAL VULNERABILIDADES IBM PARTE SMART HOME***************************")
print("\n")                            
print("\n")
print(" DE UN TOTAL DE "+str(count_conseq_vulnibm_sh)+" VULNERABILIDADES DONDE LA CONSECUENCIA VIENE ESPECIFICADA:\n") 
print("\n")
print("   - LAS ESTADISTICAS DE CONSECUENCIAS SON LAS SIGUIENTES:  \n")
print("      -    EN  "+str(count_obtaininfoconseq_vulnibm_sh)+" VULNERABILIDADES LA CONSECUENCIA ES LA OBTENCION DE INFORMACION. LA PUNTUACION TEMPORAL VIENE ESPECIFICADA ES  "+str(count_obtaininfoconseq_vulnibm_sh_specified)+" VULNERABILIDADES. LAS ESTADÍSTICAS DE PUNTUACION TEMPORAL SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_obtaininfoconseq_tempscore_9_vulnibm_sh)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN  "+str(count_obtaininfoconseq_tempscore_8_vulnibm_sh)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN  "+str(count_obtaininfoconseq_tempscore_7_vulnibm_sh)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN  "+str(count_obtaininfoconseq_tempscore_6_vulnibm_sh)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN  "+str(count_obtaininfoconseq_tempscore_5_vulnibm_sh)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN  "+str(count_obtaininfoconseq_tempscore_4_vulnibm_sh)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN  "+str(count_obtaininfoconseq_tempscore_3_vulnibm_sh)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN  "+str(count_obtaininfoconseq_tempscore_2_vulnibm_sh)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN  "+str(count_obtaininfoconseq_tempscore_1_vulnibm_sh)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN  "+str(count_obtaininfoconseq_tempscore_0_vulnibm_sh)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 0 \n")
print("            -    EN  "+str(count_obtaininfoconseq_tempscore_10_vulnibm_sh)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES 10 \n")
print("\n")
print("      -    EN  "+str(count_xss_conseq_vulnibm_sh)+" VULNERABILIDADES LA CONSECUENCIA ES CROSS-SITE SCRIPTING. LA PUNTUACION TEMPORAL VIENE ESPECIFICADA ES  "+str(count_xss_conseq_vulnibm_sh_specified)+" VULNERABILIDADES. LAS ESTADÍSTICAS DE PUNTUACION TEMPORAL SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_xss_conseq_tempscore_9_vulnibm_sh)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN  "+str(count_xss_conseq_tempscore_8_vulnibm_sh)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN  "+str(count_xss_conseq_tempscore_7_vulnibm_sh)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN  "+str(count_xss_conseq_tempscore_6_vulnibm_sh)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN  "+str(count_xss_conseq_tempscore_5_vulnibm_sh)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN  "+str(count_xss_conseq_tempscore_4_vulnibm_sh)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN  "+str(count_xss_conseq_tempscore_3_vulnibm_sh)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN  "+str(count_xss_conseq_tempscore_2_vulnibm_sh)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN  "+str(count_xss_conseq_tempscore_1_vulnibm_sh)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN  "+str(count_xss_conseq_tempscore_0_vulnibm_sh)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 0 \n")
print("            -    EN  "+str(count_xss_conseq_tempscore_10_vulnibm_sh)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES 10 \n")
print("\n")
print("      -    EN  "+str(count_gainacc_conseq_vulnibm_sh)+" VULNERABILIDADES LA CONSECUENCIA ES LA OBTENCION DE ACCESO. LA PUNTUACION TEMPORAL VIENE ESPECIFICADA ES  "+str(count_gainacc_conseq_vulnibm_sh_specified)+" VULNERABILIDADES. LAS ESTADÍSTICAS DE PUNTUACION TEMPORAL SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_gainacc_conseq_tempscore_9_vulnibm_sh)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN  "+str(count_gainacc_conseq_tempscore_8_vulnibm_sh)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN  "+str(count_gainacc_conseq_tempscore_7_vulnibm_sh)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN  "+str(count_gainacc_conseq_tempscore_6_vulnibm_sh)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN  "+str(count_gainacc_conseq_tempscore_5_vulnibm_sh)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN  "+str(count_gainacc_conseq_tempscore_4_vulnibm_sh)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN  "+str(count_gainacc_conseq_tempscore_3_vulnibm_sh)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN  "+str(count_gainacc_conseq_tempscore_2_vulnibm_sh)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN  "+str(count_gainacc_conseq_tempscore_1_vulnibm_sh)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN  "+str(count_gainacc_conseq_tempscore_0_vulnibm_sh)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 0 \n")
print("            -    EN  "+str(count_gainacc_conseq_tempscore_10_vulnibm_sh)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES 10 \n")
print("\n")
print("      -    EN  "+str(count_gainpriv_conseq_vulnibm_sh)+" VULNERABILIDADES LA CONSECUENCIA ES LA OBTENCION DE PRIVILEGIOS. LA PUNTUACION TEMPORAL VIENE ESPECIFICADA ES  "+str(count_gainpriv_conseq_vulnibm_sh_specified)+" VULNERABILIDADES. LAS ESTADÍSTICAS DE PUNTUACION TEMPORAL SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_gainpriv_conseq_tempscore_9_vulnibm_sh)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN  "+str(count_gainpriv_conseq_tempscore_8_vulnibm_sh)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN  "+str(count_gainpriv_conseq_tempscore_7_vulnibm_sh)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN  "+str(count_gainpriv_conseq_tempscore_6_vulnibm_sh)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN  "+str(count_gainpriv_conseq_tempscore_5_vulnibm_sh)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN  "+str(count_gainpriv_conseq_tempscore_4_vulnibm_sh)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN  "+str(count_gainpriv_conseq_tempscore_3_vulnibm_sh)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN  "+str(count_gainpriv_conseq_tempscore_2_vulnibm_sh)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN  "+str(count_gainpriv_conseq_tempscore_1_vulnibm_sh)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN  "+str(count_gainpriv_conseq_tempscore_0_vulnibm_sh)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 0 \n")
print("            -    EN  "+str(count_gainpriv_conseq_tempscore_10_vulnibm_sh)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES 10 \n")
print("\n")
print("      -    EN  "+str(count_denialofserv_conseq_vulnibm_sh)+" VULNERABILIDADES LA CONSECUENCIA ES LA DENEGACION DE SERVICIO. LA PUNTUACION TEMPORAL VIENE ESPECIFICADA ES  "+str(count_denialofserv_conseq_vulnibm_sh_specified)+" VULNERABILIDADES. LAS ESTADÍSTICAS DE PUNTUACION TEMPORAL SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_denialofserv_conseq_tempscore_9_vulnibm_sh)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN  "+str(count_denialofserv_conseq_tempscore_8_vulnibm_sh)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN  "+str(count_denialofserv_conseq_tempscore_7_vulnibm_sh)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN  "+str(count_denialofserv_conseq_tempscore_6_vulnibm_sh)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN  "+str(count_denialofserv_conseq_tempscore_5_vulnibm_sh)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN  "+str(count_denialofserv_conseq_tempscore_4_vulnibm_sh)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN  "+str(count_denialofserv_conseq_tempscore_3_vulnibm_sh)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN  "+str(count_denialofserv_conseq_tempscore_2_vulnibm_sh)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN  "+str(count_denialofserv_conseq_tempscore_1_vulnibm_sh)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN  "+str(count_denialofserv_conseq_tempscore_0_vulnibm_sh)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 0 \n")
print("            -    EN  "+str(count_denialofserv_conseq_tempscore_10_vulnibm_sh)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES 10 \n")
print("\n")
print("      -    EN  "+str(count_filemani_conseq_vulnibm_sh)+" VULNERABILIDADES LA CONSECUENCIA ES LA MANIPULACION DE FICHEROS. LA PUNTUACION TEMPORAL VIENE ESPECIFICADA ES  "+str(count_filemani_conseq_vulnibm_sh_specified)+" VULNERABILIDADES. LAS ESTADÍSTICAS DE PUNTUACION TEMPORAL SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_filemani_conseq_tempscore_9_vulnibm_sh)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN  "+str(count_filemani_conseq_tempscore_8_vulnibm_sh)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN  "+str(count_filemani_conseq_tempscore_7_vulnibm_sh)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN  "+str(count_filemani_conseq_tempscore_6_vulnibm_sh)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN  "+str(count_filemani_conseq_tempscore_5_vulnibm_sh)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN  "+str(count_filemani_conseq_tempscore_4_vulnibm_sh)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN  "+str(count_filemani_conseq_tempscore_3_vulnibm_sh)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN  "+str(count_filemani_conseq_tempscore_2_vulnibm_sh)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN  "+str(count_filemani_conseq_tempscore_1_vulnibm_sh)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN  "+str(count_filemani_conseq_tempscore_0_vulnibm_sh)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 0 \n")
print("            -    EN  "+str(count_filemani_conseq_tempscore_10_vulnibm_sh)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES 10 \n")
print("\n")
print("      -    EN  "+str(count_other_conseq_vulnibm_sh)+" VULNERABILIDADES LA CONSECUENCIA ES OTRA DISTINTA A LAS ANTERIORES. LA PUNTUACION TEMPORAL VIENE ESPECIFICADA ES  "+str(count_other_conseq_vulnibm_sh_specified)+" VULNERABILIDADES. LAS ESTADÍSTICAS DE PUNTUACION TEMPORAL SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_other_conseq_tempscore_9_vulnibm_sh)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN  "+str(count_other_conseq_tempscore_8_vulnibm_sh)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN  "+str(count_other_conseq_tempscore_7_vulnibm_sh)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN  "+str(count_other_conseq_tempscore_6_vulnibm_sh)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN  "+str(count_other_conseq_tempscore_5_vulnibm_sh)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN  "+str(count_other_conseq_tempscore_4_vulnibm_sh)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN  "+str(count_other_conseq_tempscore_3_vulnibm_sh)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN  "+str(count_other_conseq_tempscore_2_vulnibm_sh)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN  "+str(count_other_conseq_tempscore_1_vulnibm_sh)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN  "+str(count_other_conseq_tempscore_0_vulnibm_sh)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 0 \n")
print("            -    EN  "+str(count_other_conseq_tempscore_10_vulnibm_sh)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES 10 \n")
print("\n")






print("***************************PORCENTAJES CONSECUENCIAS DE ATAQUE/PUNTUACION TEMPORAL VULNERABILIDADES IBM SMART HOME ***************************")
print("\n")                            
print("\n")
print(" DE UN TOTAL DE "+str(count_conseq_vulnibm_sh)+" VULNERABILIDADES :\n") 
print("\n")
print("   - LOS PORCENTAJES DE CONSECUENCIAS SON LOS SIGUIENTES:  \n")
if(count_obtaininfoconseq_vulnibm_sh>0):
    print("      -    EN EL "+str(float((count_obtaininfoconseq_vulnibm_sh*100)/count_conseq_vulnibm_sh))+" % DE VULNERABILIDADES LA CONSECUENCIA ES LA OBTENCION DE INFORMACION. LA PUNTUACION TEMPORAL VIENE ESPECIFICADA EN EL "+str(float((count_obtaininfoconseq_vulnibm_sh_specified*100)/count_obtaininfoconseq_vulnibm_sh))+" % DE ELLAS. LOS PORCENTAJES DE PUNTUACION TEMPORAL SON LOS SIGUIENTES :  \n")
    print("            -    EN EL "+str(float((count_obtaininfoconseq_tempscore_9_vulnibm_sh*100)/count_obtaininfoconseq_vulnibm_sh))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 9 \n")
    print("            -    EN EL "+str(float((count_obtaininfoconseq_tempscore_8_vulnibm_sh*100)/count_obtaininfoconseq_vulnibm_sh))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 8 \n")
    print("            -    EN EL "+str(float((count_obtaininfoconseq_tempscore_7_vulnibm_sh*100)/count_obtaininfoconseq_vulnibm_sh))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 7  \n")
    print("            -    EN EL "+str(float((count_obtaininfoconseq_tempscore_6_vulnibm_sh*100)/count_obtaininfoconseq_vulnibm_sh))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 6  \n")
    print("            -    EN EL "+str(float((count_obtaininfoconseq_tempscore_5_vulnibm_sh*100)/count_obtaininfoconseq_vulnibm_sh))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 5  \n")
    print("            -    EN EL "+str(float((count_obtaininfoconseq_tempscore_4_vulnibm_sh*100)/count_obtaininfoconseq_vulnibm_sh))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 4  \n")
    print("            -    EN EL "+str(float((count_obtaininfoconseq_tempscore_3_vulnibm_sh*100)/count_obtaininfoconseq_vulnibm_sh))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 3  \n")
    print("            -    EN EL "+str(float((count_obtaininfoconseq_tempscore_2_vulnibm_sh*100)/count_obtaininfoconseq_vulnibm_sh))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 2  \n")
    print("            -    EN EL "+str(float((count_obtaininfoconseq_tempscore_1_vulnibm_sh*100)/count_obtaininfoconseq_vulnibm_sh))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 1  \n")
    print("            -    EN EL "+str(float((count_obtaininfoconseq_tempscore_0_vulnibm_sh*100)/count_obtaininfoconseq_vulnibm_sh))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 0  \n")
    print("            -    EN EL "+str(float((count_obtaininfoconseq_tempscore_10_vulnibm_sh*100)/count_obtaininfoconseq_vulnibm_sh))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 10  \n")
    print("\n")
if(count_xss_conseq_vulnibm_sh>0):
    print("      -    EN EL "+str(float((count_xss_conseq_vulnibm_sh*100)/count_conseq_vulnibm_sh))+" % DE VULNERABILIDADES LA CONSECUENCIA ES CROSS-SITE SCRIPTING. LA PUNTUACION TEMPORAL VIENE ESPECIFICADA EN EL "+str(float((count_xss_conseq_vulnibm_sh_specified*100)/count_xss_conseq_vulnibm_sh))+" % DE ELLAS. LOS PORCENTAJES DE PUNTUACION TEMPORAL SON LOS SIGUIENTES :  \n")
    print("            -    EN EL "+str(float((count_xss_conseq_tempscore_9_vulnibm_sh*100)/count_xss_conseq_vulnibm_sh))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 9 \n")
    print("            -    EN EL "+str(float((count_xss_conseq_tempscore_8_vulnibm_sh*100)/count_xss_conseq_vulnibm_sh))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 8 \n")
    print("            -    EN EL "+str(float((count_xss_conseq_tempscore_7_vulnibm_sh*100)/count_xss_conseq_vulnibm_sh))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 7  \n")
    print("            -    EN EL "+str(float((count_xss_conseq_tempscore_6_vulnibm_sh*100)/count_xss_conseq_vulnibm_sh))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 6  \n")
    print("            -    EN EL "+str(float((count_xss_conseq_tempscore_5_vulnibm_sh*100)/count_xss_conseq_vulnibm_sh))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 5  \n")
    print("            -    EN EL "+str(float((count_xss_conseq_tempscore_4_vulnibm_sh*100)/count_xss_conseq_vulnibm_sh))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 4  \n")
    print("            -    EN EL "+str(float((count_xss_conseq_tempscore_3_vulnibm_sh*100)/count_xss_conseq_vulnibm_sh))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 3  \n")
    print("            -    EN EL "+str(float((count_xss_conseq_tempscore_2_vulnibm_sh*100)/count_xss_conseq_vulnibm_sh))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 2  \n")
    print("            -    EN EL "+str(float((count_xss_conseq_tempscore_1_vulnibm_sh*100)/count_xss_conseq_vulnibm_sh))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 1  \n")
    print("            -    EN EL "+str(float((count_xss_conseq_tempscore_0_vulnibm_sh*100)/count_xss_conseq_vulnibm_sh))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 0  \n")
    print("            -    EN EL "+str(float((count_xss_conseq_tempscore_10_vulnibm_sh*100)/count_xss_conseq_vulnibm_sh))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 10  \n")
    print("\n")
if(count_gainacc_conseq_vulnibm_sh>0):
    print("      -    EN EL "+str(float((count_gainacc_conseq_vulnibm_sh*100)/count_conseq_vulnibm_sh))+" % DE VULNERABILIDADES LA CONSECUENCIA ES LA OBTENCION DE ACCESO. LA PUNTUACION TEMPORAL VIENE ESPECIFICADA EN EL "+str(float((count_gainacc_conseq_vulnibm_sh_specified*100)/count_gainacc_conseq_vulnibm_sh))+" % DE ELLAS. LOS PORCENTAJES DE PUNTUACION TEMPORAL SON LOS SIGUIENTES :  \n")
    print("            -    EN EL "+str(float((count_gainacc_conseq_tempscore_9_vulnibm_sh*100)/count_gainacc_conseq_vulnibm_sh))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 9 \n")
    print("            -    EN EL "+str(float((count_gainacc_conseq_tempscore_8_vulnibm_sh*100)/count_gainacc_conseq_vulnibm_sh))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 8 \n")
    print("            -    EN EL "+str(float((count_gainacc_conseq_tempscore_7_vulnibm_sh*100)/count_gainacc_conseq_vulnibm_sh))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 7  \n")
    print("            -    EN EL "+str(float((count_gainacc_conseq_tempscore_6_vulnibm_sh*100)/count_gainacc_conseq_vulnibm_sh))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 6  \n")
    print("            -    EN EL "+str(float((count_gainacc_conseq_tempscore_5_vulnibm_sh*100)/count_gainacc_conseq_vulnibm_sh))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 5  \n")
    print("            -    EN EL "+str(float((count_gainacc_conseq_tempscore_4_vulnibm_sh*100)/count_gainacc_conseq_vulnibm_sh))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 4  \n")
    print("            -    EN EL "+str(float((count_gainacc_conseq_tempscore_3_vulnibm_sh*100)/count_gainacc_conseq_vulnibm_sh))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 3  \n")
    print("            -    EN EL "+str(float((count_gainacc_conseq_tempscore_2_vulnibm_sh*100)/count_gainacc_conseq_vulnibm_sh))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 2  \n")
    print("            -    EN EL "+str(float((count_gainacc_conseq_tempscore_1_vulnibm_sh*100)/count_gainacc_conseq_vulnibm_sh))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 1  \n")
    print("            -    EN EL "+str(float((count_gainacc_conseq_tempscore_0_vulnibm_sh*100)/count_gainacc_conseq_vulnibm_sh))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 0  \n")
    print("            -    EN EL "+str(float((count_gainacc_conseq_tempscore_10_vulnibm_sh*100)/count_gainacc_conseq_vulnibm_sh))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 10  \n")
    print("\n")
if(count_gainpriv_conseq_vulnibm_sh>0):
    print("      -    EN EL "+str(float((count_gainpriv_conseq_vulnibm_sh*100)/count_conseq_vulnibm_sh))+" % DE VULNERABILIDADES LA CONSECUENCIA ES LA OBTENCION DE PRIVILEGIOS. LA PUNTUACION TEMPORAL VIENE ESPECIFICADA EN EL "+str(float((count_gainpriv_conseq_vulnibm_sh_specified*100)/count_gainpriv_conseq_vulnibm_sh))+" % DE ELLAS. LOS PORCENTAJES DE PUNTUACION TEMPORAL SON LOS SIGUIENTES :  \n")
    print("            -    EN EL "+str(float((count_gainpriv_conseq_tempscore_9_vulnibm_sh*100)/count_gainpriv_conseq_vulnibm_sh))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 9 \n")
    print("            -    EN EL "+str(float((count_gainpriv_conseq_tempscore_8_vulnibm_sh*100)/count_gainpriv_conseq_vulnibm_sh))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 8 \n")
    print("            -    EN EL "+str(float((count_gainpriv_conseq_tempscore_7_vulnibm_sh*100)/count_gainpriv_conseq_vulnibm_sh))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 7  \n")
    print("            -    EN EL "+str(float((count_gainpriv_conseq_tempscore_6_vulnibm_sh*100)/count_gainpriv_conseq_vulnibm_sh))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 6  \n")
    print("            -    EN EL "+str(float((count_gainpriv_conseq_tempscore_5_vulnibm_sh*100)/count_gainpriv_conseq_vulnibm_sh))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 5  \n")
    print("            -    EN EL "+str(float((count_gainpriv_conseq_tempscore_4_vulnibm_sh*100)/count_gainpriv_conseq_vulnibm_sh))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 4  \n")
    print("            -    EN EL "+str(float((count_gainpriv_conseq_tempscore_3_vulnibm_sh*100)/count_gainpriv_conseq_vulnibm_sh))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 3  \n")
    print("            -    EN EL "+str(float((count_gainpriv_conseq_tempscore_2_vulnibm_sh*100)/count_gainpriv_conseq_vulnibm_sh))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 2  \n")
    print("            -    EN EL "+str(float((count_gainpriv_conseq_tempscore_1_vulnibm_sh*100)/count_gainpriv_conseq_vulnibm_sh))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 1  \n")
    print("            -    EN EL "+str(float((count_gainpriv_conseq_tempscore_0_vulnibm_sh*100)/count_gainpriv_conseq_vulnibm_sh))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 0  \n")
    print("            -    EN EL "+str(float((count_gainpriv_conseq_tempscore_10_vulnibm_sh*100)/count_gainpriv_conseq_vulnibm_sh))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 10  \n")
    print("\n")

if(count_denialofserv_conseq_vulnibm_sh>0):
    print("      -    EN EL "+str(float((count_denialofserv_conseq_vulnibm_sh*100)/count_conseq_vulnibm_sh))+" % DE VULNERABILIDADES LA CONSECUENCIA ES UNA DENEGACION DE SERVICIO. LA PUNTUACION TEMPORAL VIENE ESPECIFICADA EN EL "+str(float((count_denialofserv_conseq_vulnibm_sh_specified*100)/count_denialofserv_conseq_vulnibm_sh))+" % DE ELLAS. LOS PORCENTAJES DE PUNTUACION TEMPORAL SON LOS SIGUIENTES :  \n")
    print("            -    EN EL "+str(float((count_denialofserv_conseq_tempscore_9_vulnibm_sh*100)/count_denialofserv_conseq_vulnibm_sh))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 9 \n")
    print("            -    EN EL "+str(float((count_denialofserv_conseq_tempscore_8_vulnibm_sh*100)/count_denialofserv_conseq_vulnibm_sh))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 8 \n")
    print("            -    EN EL "+str(float((count_denialofserv_conseq_tempscore_7_vulnibm_sh*100)/count_denialofserv_conseq_vulnibm_sh))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 7  \n")
    print("            -    EN EL "+str(float((count_denialofserv_conseq_tempscore_6_vulnibm_sh*100)/count_denialofserv_conseq_vulnibm_sh))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 6  \n")
    print("            -    EN EL "+str(float((count_denialofserv_conseq_tempscore_5_vulnibm_sh*100)/count_denialofserv_conseq_vulnibm_sh))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 5  \n")
    print("            -    EN EL "+str(float((count_denialofserv_conseq_tempscore_4_vulnibm_sh*100)/count_denialofserv_conseq_vulnibm_sh))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 4  \n")
    print("            -    EN EL "+str(float((count_denialofserv_conseq_tempscore_3_vulnibm_sh*100)/count_denialofserv_conseq_vulnibm_sh))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 3  \n")
    print("            -    EN EL "+str(float((count_denialofserv_conseq_tempscore_2_vulnibm_sh*100)/count_denialofserv_conseq_vulnibm_sh))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 2  \n")
    print("            -    EN EL "+str(float((count_denialofserv_conseq_tempscore_1_vulnibm_sh*100)/count_denialofserv_conseq_vulnibm_sh))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 1  \n")
    print("            -    EN EL "+str(float((count_denialofserv_conseq_tempscore_0_vulnibm_sh*100)/count_denialofserv_conseq_vulnibm_sh))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 0  \n")
    print("            -    EN EL "+str(float((count_denialofserv_conseq_tempscore_10_vulnibm_sh*100)/count_denialofserv_conseq_vulnibm_sh))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 10  \n")
    print("\n")
    
if(count_bypassec_conseq_vulnibm_sh>0):
    print("      -    EN EL "+str(float((count_bypassec_conseq_vulnibm_sh*100)/count_conseq_vulnibm_sh))+" % DE VULNERABILIDADES LA CONSECUENCIA ES SOBREPASAR LA SEGURIDAD. LA PUNTUACION TEMPORAL VIENE ESPECIFICADA EN EL "+str(float((count_bypassec_conseq_vulnibm_sh_specified*100)/count_bypassec_conseq_vulnibm_sh))+" % DE ELLAS. LOS PORCENTAJES DE PUNTUACION TEMPORAL SON LOS SIGUIENTES :  \n")
    print("            -    EN EL "+str(float((count_bypassec_conseq_tempscore_9_vulnibm_sh*100)/count_bypassec_conseq_vulnibm_sh))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 9 \n")
    print("            -    EN EL "+str(float((count_bypassec_conseq_tempscore_8_vulnibm_sh*100)/count_bypassec_conseq_vulnibm_sh))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 8 \n")
    print("            -    EN EL "+str(float((count_bypassec_conseq_tempscore_7_vulnibm_sh*100)/count_bypassec_conseq_vulnibm_sh))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 7  \n")
    print("            -    EN EL "+str(float((count_bypassec_conseq_tempscore_6_vulnibm_sh*100)/count_bypassec_conseq_vulnibm_sh))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 6  \n")
    print("            -    EN EL "+str(float((count_bypassec_conseq_tempscore_5_vulnibm_sh*100)/count_bypassec_conseq_vulnibm_sh))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 5  \n")
    print("            -    EN EL "+str(float((count_bypassec_conseq_tempscore_4_vulnibm_sh*100)/count_bypassec_conseq_vulnibm_sh))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 4  \n")
    print("            -    EN EL "+str(float((count_bypassec_conseq_tempscore_3_vulnibm_sh*100)/count_bypassec_conseq_vulnibm_sh))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 3  \n")
    print("            -    EN EL "+str(float((count_bypassec_conseq_tempscore_2_vulnibm_sh*100)/count_bypassec_conseq_vulnibm_sh))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 2  \n")
    print("            -    EN EL "+str(float((count_bypassec_conseq_tempscore_1_vulnibm_sh*100)/count_bypassec_conseq_vulnibm_sh))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 1  \n")
    print("            -    EN EL "+str(float((count_bypassec_conseq_tempscore_0_vulnibm_sh*100)/count_bypassec_conseq_vulnibm_sh))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 0  \n")
    print("            -    EN EL "+str(float((count_bypassec_conseq_tempscore_10_vulnibm_sh*100)/count_bypassec_conseq_vulnibm_sh))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 10  \n")
    print("\n")    

if(count_filemani_conseq_vulnibm_sh>0):
    print("      -    EN EL "+str(float((count_filemani_conseq_vulnibm_sh*100)/count_conseq_vulnibm_sh))+" % DE VULNERABILIDADES LA CONSECUENCIA ES LA MANIPULACION DE FICHEROS. LA PUNTUACION TEMPORAL VIENE ESPECIFICADA EN EL "+str(float((count_filemani_conseq_vulnibm_sh_specified*100)/count_filemani_conseq_vulnibm_sh))+" % DE ELLAS. LOS PORCENTAJES DE PUNTUACION TEMPORAL SON LOS SIGUIENTES :  \n")
    print("            -    EN EL "+str(float((count_filemani_conseq_tempscore_9_vulnibm_sh*100)/count_filemani_conseq_vulnibm_sh))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 9 \n")
    print("            -    EN EL "+str(float((count_filemani_conseq_tempscore_8_vulnibm_sh*100)/count_filemani_conseq_vulnibm_sh))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 8 \n")
    print("            -    EN EL "+str(float((count_filemani_conseq_tempscore_7_vulnibm_sh*100)/count_filemani_conseq_vulnibm_sh))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 7  \n")
    print("            -    EN EL "+str(float((count_filemani_conseq_tempscore_6_vulnibm_sh*100)/count_filemani_conseq_vulnibm_sh))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 6  \n")
    print("            -    EN EL "+str(float((count_filemani_conseq_tempscore_5_vulnibm_sh*100)/count_filemani_conseq_vulnibm_sh))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 5  \n")
    print("            -    EN EL "+str(float((count_filemani_conseq_tempscore_4_vulnibm_sh*100)/count_filemani_conseq_vulnibm_sh))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 4  \n")
    print("            -    EN EL "+str(float((count_filemani_conseq_tempscore_3_vulnibm_sh*100)/count_filemani_conseq_vulnibm_sh))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 3  \n")
    print("            -    EN EL "+str(float((count_filemani_conseq_tempscore_2_vulnibm_sh*100)/count_filemani_conseq_vulnibm_sh))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 2  \n")
    print("            -    EN EL "+str(float((count_filemani_conseq_tempscore_1_vulnibm_sh*100)/count_filemani_conseq_vulnibm_sh))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 1  \n")
    print("            -    EN EL "+str(float((count_filemani_conseq_tempscore_0_vulnibm_sh*100)/count_filemani_conseq_vulnibm_sh))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 0  \n")
    print("            -    EN EL "+str(float((count_filemani_conseq_tempscore_10_vulnibm_sh*100)/count_filemani_conseq_vulnibm_sh))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 10  \n")
    print("\n")
    
if(count_other_conseq_vulnibm_sh>0):
    print("      -    EN EL "+str(float((count_other_conseq_vulnibm_sh*100)/count_conseq_vulnibm_sh))+" % DE VULNERABILIDADES LA CONSECUENCIA ES OTRA DISTINTA A LAS ANTERIORES. LA PUNTUACION TEMPORAL VIENE ESPECIFICADA EN EL "+str(float((count_other_conseq_vulnibm_sh_specified*100)/count_other_conseq_vulnibm_sh))+" % DE ELLAS. LOS PORCENTAJES DE PUNTUACION TEMPORAL SON LOS SIGUIENTES :  \n")
    print("            -    EN EL "+str(float((count_other_conseq_tempscore_9_vulnibm_sh*100)/count_other_conseq_vulnibm_sh))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 9 \n")
    print("            -    EN EL "+str(float((count_other_conseq_tempscore_8_vulnibm_sh*100)/count_other_conseq_vulnibm_sh))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 8 \n")
    print("            -    EN EL "+str(float((count_other_conseq_tempscore_7_vulnibm_sh*100)/count_other_conseq_vulnibm_sh))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 7  \n")
    print("            -    EN EL "+str(float((count_other_conseq_tempscore_6_vulnibm_sh*100)/count_other_conseq_vulnibm_sh))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 6  \n")
    print("            -    EN EL "+str(float((count_other_conseq_tempscore_5_vulnibm_sh*100)/count_other_conseq_vulnibm_sh))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 5  \n")
    print("            -    EN EL "+str(float((count_other_conseq_tempscore_4_vulnibm_sh*100)/count_other_conseq_vulnibm_sh))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 4  \n")
    print("            -    EN EL "+str(float((count_other_conseq_tempscore_3_vulnibm_sh*100)/count_other_conseq_vulnibm_sh))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 3  \n")
    print("            -    EN EL "+str(float((count_other_conseq_tempscore_2_vulnibm_sh*100)/count_other_conseq_vulnibm_sh))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 2  \n")
    print("            -    EN EL "+str(float((count_other_conseq_tempscore_1_vulnibm_sh*100)/count_other_conseq_vulnibm_sh))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 1  \n")
    print("            -    EN EL "+str(float((count_other_conseq_tempscore_0_vulnibm_sh*100)/count_other_conseq_vulnibm_sh))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 0  \n")
    print("            -    EN EL "+str(float((count_other_conseq_tempscore_10_vulnibm_sh*100)/count_other_conseq_vulnibm_sh))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 10  \n")
    print("\n")
          
          
          
          
          
          
          
          
          
  
                              
                              
                              
                              
                              
                              
                              
                              
                              
                              
                              
                              
                              
                              
                              
                              
                              
                                                            
print("***************************ESTADÍSTICAS CONSECUENCIAS DE ATAQUE/PUNTUACION TEMPORAL VULNERABILIDADES IBM PARTE IOT Y SMART HOME***************************")
print("\n")                            
print("\n")
print(" DE UN TOTAL DE "+str(count_conseq_vulnibm_sh+count_conseq_vulnibm_iot)+" VULNERABILIDADES DONDE LA CONSECUENCIA VIENE ESPECIFICADA:\n") 
print("\n")
print("   - LAS ESTADISTICAS DE CONSECUENCIAS SON LAS SIGUIENTES:  \n")
print("      -    EN  "+str(count_obtaininfoconseq_vulnibm_sh+count_obtaininfoconseq_vulnibm_iot)+" VULNERABILIDADES LA CONSECUENCIA ES LA OBTENCION DE INFORMACION. LA PUNTUACION TEMPORAL VIENE ESPECIFICADA ES  "+str(count_obtaininfoconseq_vulnibm_sh_specified+count_obtaininfoconseq_vulnibm_iot_specified)+" VULNERABILIDADES. LAS ESTADÍSTICAS DE PUNTUACION TEMPORAL SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_obtaininfoconseq_tempscore_9_vulnibm_sh+count_obtaininfoconseq_tempscore_9_vulnibm_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN  "+str(count_obtaininfoconseq_tempscore_8_vulnibm_sh+count_obtaininfoconseq_tempscore_8_vulnibm_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN  "+str(count_obtaininfoconseq_tempscore_7_vulnibm_sh+count_obtaininfoconseq_tempscore_7_vulnibm_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN  "+str(count_obtaininfoconseq_tempscore_6_vulnibm_sh+count_obtaininfoconseq_tempscore_6_vulnibm_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN  "+str(count_obtaininfoconseq_tempscore_5_vulnibm_sh+count_obtaininfoconseq_tempscore_5_vulnibm_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN  "+str(count_obtaininfoconseq_tempscore_4_vulnibm_sh+count_obtaininfoconseq_tempscore_4_vulnibm_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN  "+str(count_obtaininfoconseq_tempscore_3_vulnibm_sh+count_obtaininfoconseq_tempscore_3_vulnibm_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN  "+str(count_obtaininfoconseq_tempscore_2_vulnibm_sh+count_obtaininfoconseq_tempscore_2_vulnibm_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN  "+str(count_obtaininfoconseq_tempscore_1_vulnibm_sh+count_obtaininfoconseq_tempscore_1_vulnibm_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN  "+str(count_obtaininfoconseq_tempscore_0_vulnibm_sh+count_obtaininfoconseq_tempscore_0_vulnibm_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 0 \n")
print("            -    EN  "+str(count_obtaininfoconseq_tempscore_10_vulnibm_sh+count_obtaininfoconseq_tempscore_10_vulnibm_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES 10 \n")
print("\n")
print("      -    EN  "+str(count_xss_conseq_vulnibm_sh+count_xss_conseq_vulnibm_iot)+" VULNERABILIDADES LA CONSECUENCIA ES CROSS-SITE SCRIPTING. LA PUNTUACION TEMPORAL VIENE ESPECIFICADA ES  "+str(count_xss_conseq_vulnibm_sh_specified+count_xss_conseq_vulnibm_iot_specified)+" VULNERABILIDADES. LAS ESTADÍSTICAS DE PUNTUACION TEMPORAL SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_xss_conseq_tempscore_9_vulnibm_sh+count_xss_conseq_tempscore_9_vulnibm_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN  "+str(count_xss_conseq_tempscore_8_vulnibm_sh+count_xss_conseq_tempscore_8_vulnibm_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN  "+str(count_xss_conseq_tempscore_7_vulnibm_sh+count_xss_conseq_tempscore_7_vulnibm_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN  "+str(count_xss_conseq_tempscore_6_vulnibm_sh+count_xss_conseq_tempscore_6_vulnibm_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN  "+str(count_xss_conseq_tempscore_5_vulnibm_sh+count_xss_conseq_tempscore_5_vulnibm_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN  "+str(count_xss_conseq_tempscore_4_vulnibm_sh+count_xss_conseq_tempscore_4_vulnibm_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN  "+str(count_xss_conseq_tempscore_3_vulnibm_sh+count_xss_conseq_tempscore_3_vulnibm_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN  "+str(count_xss_conseq_tempscore_2_vulnibm_sh+count_xss_conseq_tempscore_2_vulnibm_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN  "+str(count_xss_conseq_tempscore_1_vulnibm_sh+count_xss_conseq_tempscore_1_vulnibm_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN  "+str(count_xss_conseq_tempscore_0_vulnibm_sh+count_xss_conseq_tempscore_0_vulnibm_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 0 \n")
print("            -    EN  "+str(count_xss_conseq_tempscore_10_vulnibm_sh+count_xss_conseq_tempscore_10_vulnibm_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES 10 \n")
print("\n")
print("      -    EN  "+str(count_gainacc_conseq_vulnibm_sh+count_gainacc_conseq_vulnibm_iot)+" VULNERABILIDADES LA CONSECUENCIA ES LA OBTENCION DE ACCESO. LA PUNTUACION TEMPORAL VIENE ESPECIFICADA ES  "+str(count_gainacc_conseq_vulnibm_sh_specified+count_gainacc_conseq_vulnibm_iot_specified)+" VULNERABILIDADES. LAS ESTADÍSTICAS DE PUNTUACION TEMPORAL SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_gainacc_conseq_tempscore_9_vulnibm_sh+count_gainacc_conseq_tempscore_9_vulnibm_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN  "+str(count_gainacc_conseq_tempscore_8_vulnibm_sh+count_gainacc_conseq_tempscore_8_vulnibm_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN  "+str(count_gainacc_conseq_tempscore_7_vulnibm_sh+count_gainacc_conseq_tempscore_7_vulnibm_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN  "+str(count_gainacc_conseq_tempscore_6_vulnibm_sh+count_gainacc_conseq_tempscore_6_vulnibm_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN  "+str(count_gainacc_conseq_tempscore_5_vulnibm_sh+count_gainacc_conseq_tempscore_5_vulnibm_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN  "+str(count_gainacc_conseq_tempscore_4_vulnibm_sh+count_gainacc_conseq_tempscore_4_vulnibm_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN  "+str(count_gainacc_conseq_tempscore_3_vulnibm_sh+count_gainacc_conseq_tempscore_3_vulnibm_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN  "+str(count_gainacc_conseq_tempscore_2_vulnibm_sh+count_gainacc_conseq_tempscore_2_vulnibm_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN  "+str(count_gainacc_conseq_tempscore_1_vulnibm_sh+count_gainacc_conseq_tempscore_1_vulnibm_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN  "+str(count_gainacc_conseq_tempscore_0_vulnibm_sh+count_gainacc_conseq_tempscore_0_vulnibm_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 0 \n")
print("            -    EN  "+str(count_gainacc_conseq_tempscore_10_vulnibm_sh+count_gainacc_conseq_tempscore_10_vulnibm_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES 10 \n")
print("\n")
print("      -    EN  "+str(count_gainpriv_conseq_vulnibm_sh+count_gainpriv_conseq_vulnibm_iot)+" VULNERABILIDADES LA CONSECUENCIA ES LA OBTENCION DE PRIVILEGIOS. LA PUNTUACION TEMPORAL VIENE ESPECIFICADA ES  "+str(count_gainpriv_conseq_vulnibm_sh_specified+count_gainpriv_conseq_vulnibm_iot_specified)+" VULNERABILIDADES. LAS ESTADÍSTICAS DE PUNTUACION TEMPORAL SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_gainpriv_conseq_tempscore_9_vulnibm_sh+count_gainpriv_conseq_tempscore_9_vulnibm_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN  "+str(count_gainpriv_conseq_tempscore_8_vulnibm_sh+count_gainpriv_conseq_tempscore_8_vulnibm_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN  "+str(count_gainpriv_conseq_tempscore_7_vulnibm_sh+count_gainpriv_conseq_tempscore_7_vulnibm_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN  "+str(count_gainpriv_conseq_tempscore_6_vulnibm_sh+count_gainpriv_conseq_tempscore_6_vulnibm_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN  "+str(count_gainpriv_conseq_tempscore_5_vulnibm_sh+count_gainpriv_conseq_tempscore_5_vulnibm_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN  "+str(count_gainpriv_conseq_tempscore_4_vulnibm_sh+count_gainpriv_conseq_tempscore_4_vulnibm_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN  "+str(count_gainpriv_conseq_tempscore_3_vulnibm_sh+count_gainpriv_conseq_tempscore_3_vulnibm_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN  "+str(count_gainpriv_conseq_tempscore_2_vulnibm_sh+count_gainpriv_conseq_tempscore_2_vulnibm_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN  "+str(count_gainpriv_conseq_tempscore_1_vulnibm_sh+count_gainpriv_conseq_tempscore_1_vulnibm_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN  "+str(count_gainpriv_conseq_tempscore_0_vulnibm_sh+count_gainpriv_conseq_tempscore_0_vulnibm_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 0 \n")
print("            -    EN  "+str(count_gainpriv_conseq_tempscore_10_vulnibm_sh+count_gainpriv_conseq_tempscore_10_vulnibm_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES 10 \n")
print("\n")
print("      -    EN  "+str(count_denialofserv_conseq_vulnibm_sh+count_denialofserv_conseq_vulnibm_iot)+" VULNERABILIDADES LA CONSECUENCIA ES UNA DENEGACION DE SERVICIO. LA PUNTUACION TEMPORAL VIENE ESPECIFICADA ES  "+str(count_denialofserv_conseq_vulnibm_sh_specified+count_denialofserv_conseq_vulnibm_iot_specified)+" VULNERABILIDADES. LAS ESTADÍSTICAS DE PUNTUACION TEMPORAL SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_denialofserv_conseq_tempscore_9_vulnibm_sh+count_denialofserv_conseq_tempscore_9_vulnibm_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN  "+str(count_denialofserv_conseq_tempscore_8_vulnibm_sh+count_denialofserv_conseq_tempscore_8_vulnibm_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN  "+str(count_denialofserv_conseq_tempscore_7_vulnibm_sh+count_denialofserv_conseq_tempscore_7_vulnibm_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN  "+str(count_denialofserv_conseq_tempscore_6_vulnibm_sh+count_denialofserv_conseq_tempscore_6_vulnibm_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN  "+str(count_denialofserv_conseq_tempscore_5_vulnibm_sh+count_denialofserv_conseq_tempscore_5_vulnibm_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN  "+str(count_denialofserv_conseq_tempscore_4_vulnibm_sh+count_denialofserv_conseq_tempscore_4_vulnibm_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN  "+str(count_denialofserv_conseq_tempscore_3_vulnibm_sh+count_denialofserv_conseq_tempscore_3_vulnibm_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN  "+str(count_denialofserv_conseq_tempscore_2_vulnibm_sh+count_denialofserv_conseq_tempscore_2_vulnibm_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN  "+str(count_denialofserv_conseq_tempscore_1_vulnibm_sh+count_denialofserv_conseq_tempscore_1_vulnibm_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN  "+str(count_denialofserv_conseq_tempscore_0_vulnibm_sh+count_denialofserv_conseq_tempscore_0_vulnibm_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 0 \n")
print("            -    EN  "+str(count_denialofserv_conseq_tempscore_10_vulnibm_sh+count_denialofserv_conseq_tempscore_10_vulnibm_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES 10 \n")
print("\n")
print("      -    EN  "+str(count_bypassec_conseq_vulnibm_sh+count_bypassec_conseq_vulnibm_iot)+" VULNERABILIDADES LA CONSECUENCIA ES SOBREPASAR LA SEGURIDAD. LA PUNTUACION TEMPORAL VIENE ESPECIFICADA ES  "+str(count_bypassec_conseq_vulnibm_sh_specified+count_bypassec_conseq_vulnibm_iot_specified)+" VULNERABILIDADES. LAS ESTADÍSTICAS DE PUNTUACION TEMPORAL SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_bypassec_conseq_tempscore_9_vulnibm_sh+count_bypassec_conseq_tempscore_9_vulnibm_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN  "+str(count_bypassec_conseq_tempscore_8_vulnibm_sh+count_bypassec_conseq_tempscore_8_vulnibm_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN  "+str(count_bypassec_conseq_tempscore_7_vulnibm_sh+count_bypassec_conseq_tempscore_7_vulnibm_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN  "+str(count_bypassec_conseq_tempscore_6_vulnibm_sh+count_bypassec_conseq_tempscore_6_vulnibm_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN  "+str(count_bypassec_conseq_tempscore_5_vulnibm_sh+count_bypassec_conseq_tempscore_5_vulnibm_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN  "+str(count_bypassec_conseq_tempscore_4_vulnibm_sh+count_bypassec_conseq_tempscore_4_vulnibm_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN  "+str(count_bypassec_conseq_tempscore_3_vulnibm_sh+count_bypassec_conseq_tempscore_3_vulnibm_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN  "+str(count_bypassec_conseq_tempscore_2_vulnibm_sh+count_bypassec_conseq_tempscore_2_vulnibm_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN  "+str(count_bypassec_conseq_tempscore_1_vulnibm_sh+count_bypassec_conseq_tempscore_1_vulnibm_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN  "+str(count_bypassec_conseq_tempscore_0_vulnibm_sh+count_bypassec_conseq_tempscore_0_vulnibm_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 0 \n")
print("            -    EN  "+str(count_bypassec_conseq_tempscore_10_vulnibm_sh+count_bypassec_conseq_tempscore_10_vulnibm_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES 10 \n")
print("\n")
print("      -    EN  "+str(count_filemani_conseq_vulnibm_sh+count_filemani_conseq_vulnibm_iot)+" VULNERABILIDADES LA CONSECUENCIA ES LA MANIPULACION DE FICHEROS. LA PUNTUACION TEMPORAL VIENE ESPECIFICADA ES  "+str(count_filemani_conseq_vulnibm_sh_specified+count_filemani_conseq_vulnibm_iot_specified)+" VULNERABILIDADES. LAS ESTADÍSTICAS DE PUNTUACION TEMPORAL SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_filemani_conseq_tempscore_9_vulnibm_sh+count_filemani_conseq_tempscore_9_vulnibm_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN  "+str(count_filemani_conseq_tempscore_8_vulnibm_sh+count_filemani_conseq_tempscore_8_vulnibm_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN  "+str(count_filemani_conseq_tempscore_7_vulnibm_sh+count_filemani_conseq_tempscore_7_vulnibm_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN  "+str(count_filemani_conseq_tempscore_6_vulnibm_sh+count_filemani_conseq_tempscore_6_vulnibm_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN  "+str(count_filemani_conseq_tempscore_5_vulnibm_sh+count_filemani_conseq_tempscore_5_vulnibm_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN  "+str(count_filemani_conseq_tempscore_4_vulnibm_sh+count_filemani_conseq_tempscore_4_vulnibm_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN  "+str(count_filemani_conseq_tempscore_3_vulnibm_sh+count_filemani_conseq_tempscore_3_vulnibm_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN  "+str(count_filemani_conseq_tempscore_2_vulnibm_sh+count_filemani_conseq_tempscore_2_vulnibm_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN  "+str(count_filemani_conseq_tempscore_1_vulnibm_sh+count_filemani_conseq_tempscore_1_vulnibm_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN  "+str(count_filemani_conseq_tempscore_0_vulnibm_sh+count_filemani_conseq_tempscore_0_vulnibm_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 0 \n")
print("            -    EN  "+str(count_filemani_conseq_tempscore_10_vulnibm_sh+count_filemani_conseq_tempscore_10_vulnibm_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES 10 \n")
print("\n")
print("      -    EN  "+str(count_other_conseq_vulnibm_sh+count_other_conseq_vulnibm_iot)+" VULNERABILIDADES LA CONSECUENCIA ES OTRA DISTINTA A LAS ANTERIORES. LA PUNTUACION TEMPORAL VIENE ESPECIFICADA ES  "+str(count_other_conseq_vulnibm_sh_specified+count_other_conseq_vulnibm_iot_specified)+" VULNERABILIDADES. LAS ESTADÍSTICAS DE PUNTUACION TEMPORAL SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_other_conseq_tempscore_9_vulnibm_sh+count_other_conseq_tempscore_9_vulnibm_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN  "+str(count_other_conseq_tempscore_8_vulnibm_sh+count_other_conseq_tempscore_8_vulnibm_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN  "+str(count_other_conseq_tempscore_7_vulnibm_sh+count_other_conseq_tempscore_7_vulnibm_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN  "+str(count_other_conseq_tempscore_6_vulnibm_sh+count_other_conseq_tempscore_6_vulnibm_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN  "+str(count_other_conseq_tempscore_5_vulnibm_sh+count_other_conseq_tempscore_5_vulnibm_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN  "+str(count_other_conseq_tempscore_4_vulnibm_sh+count_other_conseq_tempscore_4_vulnibm_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN  "+str(count_other_conseq_tempscore_3_vulnibm_sh+count_other_conseq_tempscore_3_vulnibm_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN  "+str(count_other_conseq_tempscore_2_vulnibm_sh+count_other_conseq_tempscore_2_vulnibm_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN  "+str(count_other_conseq_tempscore_1_vulnibm_sh+count_other_conseq_tempscore_1_vulnibm_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN  "+str(count_other_conseq_tempscore_0_vulnibm_sh+count_other_conseq_tempscore_0_vulnibm_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 0 \n")
print("            -    EN  "+str(count_other_conseq_tempscore_10_vulnibm_sh+count_other_conseq_tempscore_10_vulnibm_iot)+" VULNERABILIDADES LA PUNTUACION TEMPORAL ES 10 \n")
print("\n")









print("***************************PORCENTAJES ACCESS CONSECUENCIAS DE ATAQUE/PUNTUACION TEMPORAL VULNERABILIDADES IBM PARTE IOT Y SMART HOME ***************************")
print("\n")                            
print("\n")
print(" DE UN TOTAL DE "+str(count_conseq_vulnibm_sh+count_conseq_vulnibm_iot)+" VULNERABILIDADES :\n") 
print("\n")
print("   - LOS PORCENTAJES DE CONSECUENCIAS SON LOS SIGUIENTES:  \n")
if((count_obtaininfoconseq_vulnibm_sh+count_obtaininfoconseq_vulnibm_iot)>0):
    print("      -    EN EL "+str(float(((count_obtaininfoconseq_vulnibm_sh+count_obtaininfoconseq_vulnibm_iot)*100)/(count_conseq_vulnibm_sh+count_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES LA CONSECUENCIA ES LA OBTENCION DE INFORMACION. LA PUNTUACION TEMPORAL VIENE ESPECIFICADA EN EL "+str(float(((count_obtaininfoconseq_vulnibm_sh_specified+count_obtaininfoconseq_vulnibm_iot_specified)*100)/(count_obtaininfoconseq_vulnibm_sh+count_obtaininfoconseq_vulnibm_iot)))+" % DE ELLAS. LOS PORCENTAJES DE PUNTUACION TEMPORAL SON LOS SIGUIENTES :  \n")
    print("            -    EN EL "+str(float(((count_obtaininfoconseq_tempscore_9_vulnibm_sh+count_obtaininfoconseq_tempscore_9_vulnibm_iot)*100)/(count_obtaininfoconseq_vulnibm_sh+count_obtaininfoconseq_vulnibm_iot)))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 9 \n")
    print("            -    EN EL "+str(float(((count_obtaininfoconseq_tempscore_8_vulnibm_sh+count_obtaininfoconseq_tempscore_8_vulnibm_iot)*100)/(count_obtaininfoconseq_vulnibm_sh+count_obtaininfoconseq_vulnibm_iot)))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 8 \n")
    print("            -    EN EL "+str(float(((count_obtaininfoconseq_tempscore_7_vulnibm_sh+count_obtaininfoconseq_tempscore_7_vulnibm_iot)*100)/(count_obtaininfoconseq_vulnibm_sh+count_obtaininfoconseq_vulnibm_iot)))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 7  \n")
    print("            -    EN EL "+str(float(((count_obtaininfoconseq_tempscore_6_vulnibm_sh+count_obtaininfoconseq_tempscore_6_vulnibm_iot)*100)/(count_obtaininfoconseq_vulnibm_sh+count_obtaininfoconseq_vulnibm_iot)))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 6  \n")
    print("            -    EN EL "+str(float(((count_obtaininfoconseq_tempscore_5_vulnibm_sh+count_obtaininfoconseq_tempscore_5_vulnibm_iot)*100)/(count_obtaininfoconseq_vulnibm_sh+count_obtaininfoconseq_vulnibm_iot)))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 5  \n")
    print("            -    EN EL "+str(float(((count_obtaininfoconseq_tempscore_4_vulnibm_sh+count_obtaininfoconseq_tempscore_4_vulnibm_iot)*100)/(count_obtaininfoconseq_vulnibm_sh+count_obtaininfoconseq_vulnibm_iot)))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 4  \n")
    print("            -    EN EL "+str(float(((count_obtaininfoconseq_tempscore_3_vulnibm_sh+count_obtaininfoconseq_tempscore_3_vulnibm_iot)*100)/(count_obtaininfoconseq_vulnibm_sh+count_obtaininfoconseq_vulnibm_iot)))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 3  \n")
    print("            -    EN EL "+str(float(((count_obtaininfoconseq_tempscore_2_vulnibm_sh+count_obtaininfoconseq_tempscore_2_vulnibm_iot)*100)/(count_obtaininfoconseq_vulnibm_sh+count_obtaininfoconseq_vulnibm_iot)))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 2  \n")
    print("            -    EN EL "+str(float(((count_obtaininfoconseq_tempscore_1_vulnibm_sh+count_obtaininfoconseq_tempscore_1_vulnibm_iot)*100)/(count_obtaininfoconseq_vulnibm_sh+count_obtaininfoconseq_vulnibm_iot)))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 1  \n")
    print("            -    EN EL "+str(float(((count_obtaininfoconseq_tempscore_0_vulnibm_sh+count_obtaininfoconseq_tempscore_0_vulnibm_iot)*100)/(count_obtaininfoconseq_vulnibm_sh+count_obtaininfoconseq_vulnibm_iot)))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 0  \n")
    print("            -    EN EL "+str(float(((count_obtaininfoconseq_tempscore_10_vulnibm_sh+count_obtaininfoconseq_tempscore_10_vulnibm_iot)*100)/(count_obtaininfoconseq_vulnibm_sh+count_obtaininfoconseq_vulnibm_iot)))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES 10  \n")
    print("\n")
if((count_xss_conseq_vulnibm_sh+count_xss_conseq_vulnibm_iot)>0):
    print("      -    EN EL "+str(float(((count_xss_conseq_vulnibm_sh+count_xss_conseq_vulnibm_iot)*100)/(count_conseq_vulnibm_sh+count_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES LA CONSECUENCIA ES CROSS-SITE SCRIPTING. LA PUNTUACION TEMPORAL VIENE ESPECIFICADA EN EL "+str(float(((count_xss_conseq_vulnibm_sh_specified+count_xss_conseq_vulnibm_iot_specified)*100)/(count_xss_conseq_vulnibm_sh+count_xss_conseq_vulnibm_iot)))+" % DE ELLAS. LOS PORCENTAJES DE PUNTUACION TEMPORAL SON LOS SIGUIENTES :  \n")
    print("            -    EN EL "+str(float(((count_xss_conseq_tempscore_9_vulnibm_sh+count_xss_conseq_tempscore_9_vulnibm_iot)*100)/(count_xss_conseq_vulnibm_sh+count_xss_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 9 \n")
    print("            -    EN EL "+str(float(((count_xss_conseq_tempscore_8_vulnibm_sh+count_xss_conseq_tempscore_8_vulnibm_iot)*100)/(count_xss_conseq_vulnibm_sh+count_xss_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 8 \n")
    print("            -    EN EL "+str(float(((count_xss_conseq_tempscore_7_vulnibm_sh+count_xss_conseq_tempscore_7_vulnibm_iot)*100)/(count_xss_conseq_vulnibm_sh+count_xss_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 7  \n")
    print("            -    EN EL "+str(float(((count_xss_conseq_tempscore_6_vulnibm_sh+count_xss_conseq_tempscore_6_vulnibm_iot)*100)/(count_xss_conseq_vulnibm_sh+count_xss_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 6  \n")
    print("            -    EN EL "+str(float(((count_xss_conseq_tempscore_5_vulnibm_sh+count_xss_conseq_tempscore_5_vulnibm_iot)*100)/(count_xss_conseq_vulnibm_sh+count_xss_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 5  \n")
    print("            -    EN EL "+str(float(((count_xss_conseq_tempscore_4_vulnibm_sh+count_xss_conseq_tempscore_4_vulnibm_iot)*100)/(count_xss_conseq_vulnibm_sh+count_xss_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 4  \n")
    print("            -    EN EL "+str(float(((count_xss_conseq_tempscore_3_vulnibm_sh+count_xss_conseq_tempscore_3_vulnibm_iot)*100)/(count_xss_conseq_vulnibm_sh+count_xss_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 3  \n")
    print("            -    EN EL "+str(float(((count_xss_conseq_tempscore_2_vulnibm_sh+count_xss_conseq_tempscore_2_vulnibm_iot)*100)/(count_xss_conseq_vulnibm_sh+count_xss_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 2  \n")
    print("            -    EN EL "+str(float(((count_xss_conseq_tempscore_1_vulnibm_sh+count_xss_conseq_tempscore_1_vulnibm_iot)*100)/(count_xss_conseq_vulnibm_sh+count_xss_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 1  \n")
    print("            -    EN EL "+str(float(((count_xss_conseq_tempscore_0_vulnibm_sh+count_xss_conseq_tempscore_0_vulnibm_iot)*100)/(count_xss_conseq_vulnibm_sh+count_xss_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 0  \n")
    print("            -    EN EL "+str(float(((count_xss_conseq_tempscore_10_vulnibm_sh+count_xss_conseq_tempscore_10_vulnibm_iot)*100)/(count_xss_conseq_vulnibm_sh+count_xss_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES 10  \n")
if((count_gainacc_conseq_vulnibm_sh+count_gainacc_conseq_vulnibm_iot)>0):
    print("      -    EN EL "+str(float(((count_gainacc_conseq_vulnibm_sh+count_gainacc_conseq_vulnibm_iot)*100)/(count_conseq_vulnibm_sh+count_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES LA CONSECUENCIA ES LA OBTENCION DE ACCESO. LA PUNTUACION TEMPORAL VIENE ESPECIFICADA EN EL "+str(float(((count_gainacc_conseq_vulnibm_sh_specified+count_gainacc_conseq_vulnibm_iot_specified)*100)/(count_gainacc_conseq_vulnibm_sh+count_gainacc_conseq_vulnibm_iot)))+" % DE ELLAS. LOS PORCENTAJES DE PUNTUACION TEMPORAL SON LOS SIGUIENTES :  \n")
    print("            -    EN EL "+str(float(((count_gainacc_conseq_tempscore_9_vulnibm_sh+count_gainacc_conseq_tempscore_9_vulnibm_iot)*100)/(count_gainacc_conseq_vulnibm_sh+count_gainacc_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 9 \n")
    print("            -    EN EL "+str(float(((count_gainacc_conseq_tempscore_8_vulnibm_sh+count_gainacc_conseq_tempscore_8_vulnibm_iot)*100)/(count_gainacc_conseq_vulnibm_sh+count_gainacc_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 8 \n")
    print("            -    EN EL "+str(float(((count_gainacc_conseq_tempscore_7_vulnibm_sh+count_gainacc_conseq_tempscore_7_vulnibm_iot)*100)/(count_gainacc_conseq_vulnibm_sh+count_gainacc_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 7  \n")
    print("            -    EN EL "+str(float(((count_gainacc_conseq_tempscore_6_vulnibm_sh+count_gainacc_conseq_tempscore_6_vulnibm_iot)*100)/(count_gainacc_conseq_vulnibm_sh+count_gainacc_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 6  \n")
    print("            -    EN EL "+str(float(((count_gainacc_conseq_tempscore_5_vulnibm_sh+count_gainacc_conseq_tempscore_5_vulnibm_iot)*100)/(count_gainacc_conseq_vulnibm_sh+count_gainacc_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 5  \n")
    print("            -    EN EL "+str(float(((count_gainacc_conseq_tempscore_4_vulnibm_sh+count_gainacc_conseq_tempscore_4_vulnibm_iot)*100)/(count_gainacc_conseq_vulnibm_sh+count_gainacc_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 4  \n")
    print("            -    EN EL "+str(float(((count_gainacc_conseq_tempscore_3_vulnibm_sh+count_gainacc_conseq_tempscore_3_vulnibm_iot)*100)/(count_gainacc_conseq_vulnibm_sh+count_gainacc_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 3  \n")
    print("            -    EN EL "+str(float(((count_gainacc_conseq_tempscore_2_vulnibm_sh+count_gainacc_conseq_tempscore_2_vulnibm_iot)*100)/(count_gainacc_conseq_vulnibm_sh+count_gainacc_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 2  \n")
    print("            -    EN EL "+str(float(((count_gainacc_conseq_tempscore_1_vulnibm_sh+count_gainacc_conseq_tempscore_1_vulnibm_iot)*100)/(count_gainacc_conseq_vulnibm_sh+count_gainacc_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 1  \n")
    print("            -    EN EL "+str(float(((count_gainacc_conseq_tempscore_0_vulnibm_sh+count_gainacc_conseq_tempscore_0_vulnibm_iot)*100)/(count_gainacc_conseq_vulnibm_sh+count_gainacc_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 0  \n")
    print("            -    EN EL "+str(float(((count_gainacc_conseq_tempscore_10_vulnibm_sh+count_gainacc_conseq_tempscore_10_vulnibm_iot)*100)/(count_gainacc_conseq_vulnibm_sh+count_gainacc_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES 10  \n")
if((count_gainpriv_conseq_vulnibm_sh+count_gainpriv_conseq_vulnibm_iot)>0):
    print("      -    EN EL "+str(float(((count_gainpriv_conseq_vulnibm_sh+count_gainpriv_conseq_vulnibm_iot)*100)/(count_conseq_vulnibm_sh+count_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES LA CONSECUENCIA ES LA OBTENCION DE PRIVILEGIOS. LA PUNTUACION TEMPORAL VIENE ESPECIFICADA EN EL "+str(float(((count_gainpriv_conseq_vulnibm_sh_specified+count_gainpriv_conseq_vulnibm_iot_specified)*100)/(count_gainpriv_conseq_vulnibm_sh+count_gainpriv_conseq_vulnibm_iot)))+" % DE ELLAS. LOS PORCENTAJES DE PUNTUACION TEMPORAL SON LOS SIGUIENTES :  \n")
    print("            -    EN EL "+str(float(((count_gainpriv_conseq_tempscore_9_vulnibm_sh+count_gainpriv_conseq_tempscore_9_vulnibm_iot)*100)/(count_gainpriv_conseq_vulnibm_sh+count_gainpriv_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 9 \n")
    print("            -    EN EL "+str(float(((count_gainpriv_conseq_tempscore_8_vulnibm_sh+count_gainpriv_conseq_tempscore_8_vulnibm_iot)*100)/(count_gainpriv_conseq_vulnibm_sh+count_gainpriv_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 8 \n")
    print("            -    EN EL "+str(float(((count_gainpriv_conseq_tempscore_7_vulnibm_sh+count_gainpriv_conseq_tempscore_7_vulnibm_iot)*100)/(count_gainpriv_conseq_vulnibm_sh+count_gainpriv_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 7  \n")
    print("            -    EN EL "+str(float(((count_gainpriv_conseq_tempscore_6_vulnibm_sh+count_gainpriv_conseq_tempscore_6_vulnibm_iot)*100)/(count_gainpriv_conseq_vulnibm_sh+count_gainpriv_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 6  \n")
    print("            -    EN EL "+str(float(((count_gainpriv_conseq_tempscore_5_vulnibm_sh+count_gainpriv_conseq_tempscore_5_vulnibm_iot)*100)/(count_gainpriv_conseq_vulnibm_sh+count_gainpriv_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 5  \n")
    print("            -    EN EL "+str(float(((count_gainpriv_conseq_tempscore_4_vulnibm_sh+count_gainpriv_conseq_tempscore_4_vulnibm_iot)*100)/(count_gainpriv_conseq_vulnibm_sh+count_gainpriv_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 4  \n")
    print("            -    EN EL "+str(float(((count_gainpriv_conseq_tempscore_3_vulnibm_sh+count_gainpriv_conseq_tempscore_3_vulnibm_iot)*100)/(count_gainpriv_conseq_vulnibm_sh+count_gainpriv_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 3  \n")
    print("            -    EN EL "+str(float(((count_gainpriv_conseq_tempscore_2_vulnibm_sh+count_gainpriv_conseq_tempscore_2_vulnibm_iot)*100)/(count_gainpriv_conseq_vulnibm_sh+count_gainpriv_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 2  \n")
    print("            -    EN EL "+str(float(((count_gainpriv_conseq_tempscore_1_vulnibm_sh+count_gainpriv_conseq_tempscore_1_vulnibm_iot)*100)/(count_gainpriv_conseq_vulnibm_sh+count_gainpriv_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 1  \n")
    print("            -    EN EL "+str(float(((count_gainpriv_conseq_tempscore_0_vulnibm_sh+count_gainpriv_conseq_tempscore_0_vulnibm_iot)*100)/(count_gainpriv_conseq_vulnibm_sh+count_gainpriv_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 0  \n")
    print("            -    EN EL "+str(float(((count_gainpriv_conseq_tempscore_10_vulnibm_sh+count_gainpriv_conseq_tempscore_10_vulnibm_iot)*100)/(count_gainpriv_conseq_vulnibm_sh+count_gainpriv_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES 10  \n")
    
if((count_denialofserv_conseq_vulnibm_sh+count_denialofserv_conseq_vulnibm_iot)>0):
    print("      -    EN EL "+str(float(((count_denialofserv_conseq_vulnibm_sh+count_denialofserv_conseq_vulnibm_iot)*100)/(count_conseq_vulnibm_sh+count_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES LA CONSECUENCIA ES UNA DENEGACIÓN DE SERVICIO. LA PUNTUACION TEMPORAL VIENE ESPECIFICADA EN EL "+str(float(((count_denialofserv_conseq_vulnibm_sh_specified+count_denialofserv_conseq_vulnibm_iot_specified)*100)/(count_denialofserv_conseq_vulnibm_sh+count_denialofserv_conseq_vulnibm_iot)))+" % DE ELLAS. LOS PORCENTAJES DE PUNTUACION TEMPORAL SON LOS SIGUIENTES :  \n")
    print("            -    EN EL "+str(float(((count_denialofserv_conseq_tempscore_9_vulnibm_sh+count_denialofserv_conseq_tempscore_9_vulnibm_iot)*100)/(count_denialofserv_conseq_vulnibm_sh+count_denialofserv_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 9 \n")
    print("            -    EN EL "+str(float(((count_denialofserv_conseq_tempscore_8_vulnibm_sh+count_denialofserv_conseq_tempscore_8_vulnibm_iot)*100)/(count_denialofserv_conseq_vulnibm_sh+count_denialofserv_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 8 \n")
    print("            -    EN EL "+str(float(((count_denialofserv_conseq_tempscore_7_vulnibm_sh+count_denialofserv_conseq_tempscore_7_vulnibm_iot)*100)/(count_denialofserv_conseq_vulnibm_sh+count_denialofserv_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 7  \n")
    print("            -    EN EL "+str(float(((count_denialofserv_conseq_tempscore_6_vulnibm_sh+count_denialofserv_conseq_tempscore_6_vulnibm_iot)*100)/(count_denialofserv_conseq_vulnibm_sh+count_denialofserv_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 6  \n")
    print("            -    EN EL "+str(float(((count_denialofserv_conseq_tempscore_5_vulnibm_sh+count_denialofserv_conseq_tempscore_5_vulnibm_iot)*100)/(count_denialofserv_conseq_vulnibm_sh+count_denialofserv_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 5  \n")
    print("            -    EN EL "+str(float(((count_denialofserv_conseq_tempscore_4_vulnibm_sh+count_denialofserv_conseq_tempscore_4_vulnibm_iot)*100)/(count_denialofserv_conseq_vulnibm_sh+count_denialofserv_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 4  \n")
    print("            -    EN EL "+str(float(((count_denialofserv_conseq_tempscore_3_vulnibm_sh+count_denialofserv_conseq_tempscore_3_vulnibm_iot)*100)/(count_denialofserv_conseq_vulnibm_sh+count_denialofserv_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 3  \n")
    print("            -    EN EL "+str(float(((count_denialofserv_conseq_tempscore_2_vulnibm_sh+count_denialofserv_conseq_tempscore_2_vulnibm_iot)*100)/(count_denialofserv_conseq_vulnibm_sh+count_denialofserv_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 2  \n")
    print("            -    EN EL "+str(float(((count_denialofserv_conseq_tempscore_1_vulnibm_sh+count_denialofserv_conseq_tempscore_1_vulnibm_iot)*100)/(count_denialofserv_conseq_vulnibm_sh+count_denialofserv_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 1  \n")
    print("            -    EN EL "+str(float(((count_denialofserv_conseq_tempscore_0_vulnibm_sh+count_denialofserv_conseq_tempscore_0_vulnibm_iot)*100)/(count_denialofserv_conseq_vulnibm_sh+count_denialofserv_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 0  \n")
    print("            -    EN EL "+str(float(((count_denialofserv_conseq_tempscore_10_vulnibm_sh+count_denialofserv_conseq_tempscore_10_vulnibm_iot)*100)/(count_denialofserv_conseq_vulnibm_sh+count_denialofserv_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES 10  \n")
if((count_bypassec_conseq_vulnibm_sh+count_bypassec_conseq_vulnibm_iot)>0):
    print("      -    EN EL "+str(float(((count_bypassec_conseq_vulnibm_sh+count_bypassec_conseq_vulnibm_iot)*100)/(count_conseq_vulnibm_sh+count_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES LA CONSECUENCIA ES SOBREPASAR LA SEGURIDAD. LA PUNTUACION TEMPORAL VIENE ESPECIFICADA EN EL "+str(float(((count_bypassec_conseq_vulnibm_sh_specified+count_bypassec_conseq_vulnibm_iot_specified)*100)/(count_bypassec_conseq_vulnibm_sh+count_bypassec_conseq_vulnibm_iot)))+" % DE ELLAS. LOS PORCENTAJES DE PUNTUACION TEMPORAL SON LOS SIGUIENTES :  \n")
    print("            -    EN EL "+str(float(((count_bypassec_conseq_tempscore_9_vulnibm_sh+count_bypassec_conseq_tempscore_9_vulnibm_iot)*100)/(count_bypassec_conseq_vulnibm_sh+count_bypassec_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 9 \n")
    print("            -    EN EL "+str(float(((count_bypassec_conseq_tempscore_8_vulnibm_sh+count_bypassec_conseq_tempscore_8_vulnibm_iot)*100)/(count_bypassec_conseq_vulnibm_sh+count_bypassec_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 8 \n")
    print("            -    EN EL "+str(float(((count_bypassec_conseq_tempscore_7_vulnibm_sh+count_bypassec_conseq_tempscore_7_vulnibm_iot)*100)/(count_bypassec_conseq_vulnibm_sh+count_bypassec_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 7  \n")
    print("            -    EN EL "+str(float(((count_bypassec_conseq_tempscore_6_vulnibm_sh+count_bypassec_conseq_tempscore_6_vulnibm_iot)*100)/(count_bypassec_conseq_vulnibm_sh+count_bypassec_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 6  \n")
    print("            -    EN EL "+str(float(((count_bypassec_conseq_tempscore_5_vulnibm_sh+count_bypassec_conseq_tempscore_5_vulnibm_iot)*100)/(count_bypassec_conseq_vulnibm_sh+count_bypassec_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 5  \n")
    print("            -    EN EL "+str(float(((count_bypassec_conseq_tempscore_4_vulnibm_sh+count_bypassec_conseq_tempscore_4_vulnibm_iot)*100)/(count_bypassec_conseq_vulnibm_sh+count_bypassec_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 4  \n")
    print("            -    EN EL "+str(float(((count_bypassec_conseq_tempscore_3_vulnibm_sh+count_bypassec_conseq_tempscore_3_vulnibm_iot)*100)/(count_bypassec_conseq_vulnibm_sh+count_bypassec_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 3  \n")
    print("            -    EN EL "+str(float(((count_bypassec_conseq_tempscore_2_vulnibm_sh+count_bypassec_conseq_tempscore_2_vulnibm_iot)*100)/(count_bypassec_conseq_vulnibm_sh+count_bypassec_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 2  \n")
    print("            -    EN EL "+str(float(((count_bypassec_conseq_tempscore_1_vulnibm_sh+count_bypassec_conseq_tempscore_1_vulnibm_iot)*100)/(count_bypassec_conseq_vulnibm_sh+count_bypassec_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 1  \n")
    print("            -    EN EL "+str(float(((count_bypassec_conseq_tempscore_0_vulnibm_sh+count_bypassec_conseq_tempscore_0_vulnibm_iot)*100)/(count_bypassec_conseq_vulnibm_sh+count_bypassec_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 0  \n")
    print("            -    EN EL "+str(float(((count_bypassec_conseq_tempscore_10_vulnibm_sh+count_bypassec_conseq_tempscore_10_vulnibm_iot)*100)/(count_bypassec_conseq_vulnibm_sh+count_bypassec_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES 10  \n")
if((count_filemani_conseq_vulnibm_sh+count_filemani_conseq_vulnibm_iot)>0):
    print("      -    EN EL "+str(float(((count_filemani_conseq_vulnibm_sh+count_filemani_conseq_vulnibm_iot)*100)/(count_conseq_vulnibm_sh+count_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES LA CONSECUENCIA ES LA MANIPULACION DE FICHEROS. LA PUNTUACION TEMPORAL VIENE ESPECIFICADA EN EL "+str(float(((count_filemani_conseq_vulnibm_sh_specified+count_filemani_conseq_vulnibm_iot_specified)*100)/(count_filemani_conseq_vulnibm_sh+count_filemani_conseq_vulnibm_iot)))+" % DE ELLAS. LOS PORCENTAJES DE PUNTUACION TEMPORAL SON LOS SIGUIENTES :  \n")
    print("            -    EN EL "+str(float(((count_filemani_conseq_tempscore_9_vulnibm_sh+count_filemani_conseq_tempscore_9_vulnibm_iot)*100)/(count_filemani_conseq_vulnibm_sh+count_filemani_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 9 \n")
    print("            -    EN EL "+str(float(((count_filemani_conseq_tempscore_8_vulnibm_sh+count_filemani_conseq_tempscore_8_vulnibm_iot)*100)/(count_filemani_conseq_vulnibm_sh+count_filemani_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 8 \n")
    print("            -    EN EL "+str(float(((count_filemani_conseq_tempscore_7_vulnibm_sh+count_filemani_conseq_tempscore_7_vulnibm_iot)*100)/(count_filemani_conseq_vulnibm_sh+count_filemani_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 7  \n")
    print("            -    EN EL "+str(float(((count_filemani_conseq_tempscore_6_vulnibm_sh+count_filemani_conseq_tempscore_6_vulnibm_iot)*100)/(count_filemani_conseq_vulnibm_sh+count_filemani_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 6  \n")
    print("            -    EN EL "+str(float(((count_filemani_conseq_tempscore_5_vulnibm_sh+count_filemani_conseq_tempscore_5_vulnibm_iot)*100)/(count_filemani_conseq_vulnibm_sh+count_filemani_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 5  \n")
    print("            -    EN EL "+str(float(((count_filemani_conseq_tempscore_4_vulnibm_sh+count_filemani_conseq_tempscore_4_vulnibm_iot)*100)/(count_filemani_conseq_vulnibm_sh+count_filemani_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 4  \n")
    print("            -    EN EL "+str(float(((count_filemani_conseq_tempscore_3_vulnibm_sh+count_filemani_conseq_tempscore_3_vulnibm_iot)*100)/(count_filemani_conseq_vulnibm_sh+count_filemani_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 3  \n")
    print("            -    EN EL "+str(float(((count_filemani_conseq_tempscore_2_vulnibm_sh+count_filemani_conseq_tempscore_2_vulnibm_iot)*100)/(count_filemani_conseq_vulnibm_sh+count_filemani_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 2  \n")
    print("            -    EN EL "+str(float(((count_filemani_conseq_tempscore_1_vulnibm_sh+count_filemani_conseq_tempscore_1_vulnibm_iot)*100)/(count_filemani_conseq_vulnibm_sh+count_filemani_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 1  \n")
    print("            -    EN EL "+str(float(((count_filemani_conseq_tempscore_0_vulnibm_sh+count_filemani_conseq_tempscore_0_vulnibm_iot)*100)/(count_filemani_conseq_vulnibm_sh+count_filemani_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 0  \n")
    print("            -    EN EL "+str(float(((count_filemani_conseq_tempscore_10_vulnibm_sh+count_filemani_conseq_tempscore_10_vulnibm_iot)*100)/(count_filemani_conseq_vulnibm_sh+count_filemani_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES 10  \n")
    
if((count_other_conseq_vulnibm_sh+count_other_conseq_vulnibm_iot)>0):
    print("      -    EN EL "+str(float(((count_other_conseq_vulnibm_sh+count_other_conseq_vulnibm_iot)*100)/(count_conseq_vulnibm_sh+count_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES LA CONSECUENCIA ES OTRA DISTINTA A LAS ANTERIORES. LA PUNTUACION TEMPORAL VIENE ESPECIFICADA EN EL "+str(float(((count_other_conseq_vulnibm_sh_specified+count_other_conseq_vulnibm_iot_specified)*100)/(count_other_conseq_vulnibm_sh+count_other_conseq_vulnibm_iot)))+" % DE ELLAS. LOS PORCENTAJES DE PUNTUACION TEMPORAL SON LOS SIGUIENTES :  \n")
    print("            -    EN EL "+str(float(((count_other_conseq_tempscore_9_vulnibm_sh+count_other_conseq_tempscore_9_vulnibm_iot)*100)/(count_other_conseq_vulnibm_sh+count_other_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 9 \n")
    print("            -    EN EL "+str(float(((count_other_conseq_tempscore_8_vulnibm_sh+count_other_conseq_tempscore_8_vulnibm_iot)*100)/(count_other_conseq_vulnibm_sh+count_other_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 8 \n")
    print("            -    EN EL "+str(float(((count_other_conseq_tempscore_7_vulnibm_sh+count_other_conseq_tempscore_7_vulnibm_iot)*100)/(count_other_conseq_vulnibm_sh+count_other_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 7  \n")
    print("            -    EN EL "+str(float(((count_other_conseq_tempscore_6_vulnibm_sh+count_other_conseq_tempscore_6_vulnibm_iot)*100)/(count_other_conseq_vulnibm_sh+count_other_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 6  \n")
    print("            -    EN EL "+str(float(((count_other_conseq_tempscore_5_vulnibm_sh+count_other_conseq_tempscore_5_vulnibm_iot)*100)/(count_other_conseq_vulnibm_sh+count_other_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 5  \n")
    print("            -    EN EL "+str(float(((count_other_conseq_tempscore_4_vulnibm_sh+count_other_conseq_tempscore_4_vulnibm_iot)*100)/(count_other_conseq_vulnibm_sh+count_other_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 4  \n")
    print("            -    EN EL "+str(float(((count_other_conseq_tempscore_3_vulnibm_sh+count_other_conseq_tempscore_3_vulnibm_iot)*100)/(count_other_conseq_vulnibm_sh+count_other_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 3  \n")
    print("            -    EN EL "+str(float(((count_other_conseq_tempscore_2_vulnibm_sh+count_other_conseq_tempscore_2_vulnibm_iot)*100)/(count_other_conseq_vulnibm_sh+count_other_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 2  \n")
    print("            -    EN EL "+str(float(((count_other_conseq_tempscore_1_vulnibm_sh+count_other_conseq_tempscore_1_vulnibm_iot)*100)/(count_other_conseq_vulnibm_sh+count_other_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 1  \n")
    print("            -    EN EL "+str(float(((count_other_conseq_tempscore_0_vulnibm_sh+count_other_conseq_tempscore_0_vulnibm_iot)*100)/(count_other_conseq_vulnibm_sh+count_other_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES MAYOR O IGUAL QUE 0  \n")
    print("            -    EN EL "+str(float(((count_other_conseq_tempscore_10_vulnibm_sh+count_other_conseq_tempscore_10_vulnibm_iot)*100)/(count_other_conseq_vulnibm_sh+count_other_conseq_vulnibm_iot)))+" % DE VULNERABILIDADES LA PUNTUACION TEMPORAL ES 10  \n")


    
    
    
    
    
    
    
    
    

	
	